#!/usr/bin/env python3
"""speak.py — a voice layer over velocidad, for learning by ear.

Two registers, one idea: turn the velocidad trove into something you can *hear*,
narrated as a **map of systems and concepts** rather than a flat list of cards.

    drill    Interactive voice flashcards. Speaks the front, waits while you
             answer out loud, then speaks the back (+ note). Eyes/hands free,
             active recall. The same SRS deck the CLI uses.

    listen   Renders a deck OR a concept/pattern bank to ONE continuous audio
             file for the gym, the car, a walk — repeated passive listening.
             Narrated with orienting waypoints and a recall beat (a silent gap
             after each prompt so retrieval still fires while you listen).

No third-party deps. Reuses velocidad.py's real parser so it never drifts from
the CLI. Default engine is macOS `say` (free, on-device, offline); ElevenLabs is
an opt-in upgrade for material that's worth premium narration.

Examples
--------
  # Voice-drill a scenario's deck (active recall, hands free)
  python3 scripts/speak.py drill -s spanish --scenario mcdonalds

  # Render the chunk bank to a phone-friendly audio map for the car
  python3 scripts/speak.py listen -s spanish --scenario mcdonalds \
      --bank chunks --m4a -o ~/Desktop/spanish-chunks-map.m4a

  # Render a deck's box 1 to audio, slower, different voice
  python3 scripts/speak.py listen -s spanish --box 1 --voice Samantha --rate 170 --m4a

  # Premium narration (needs ELEVENLABS_API_KEY + a voice id)
  python3 scripts/speak.py listen -s spanish --scenario mcdonalds \
      --bank chunks --engine elevenlabs --voice <voice_id> -o map.mp3
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

# Reuse the CLI's parser + study registry — single source of truth.
SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import velocidad as v  # noqa: E402

# ── silence / pacing primitives (macOS `say` inline commands) ────────────────
BEAT = "[[slnc 350]]"      # short breath between clauses
PAUSE = "[[slnc 900]]"     # between items
RECALL = "[[slnc 2600]]"   # the retrieval gap after a prompt — answer in your head
WAYPOINT = "[[slnc 1300]]"  # arriving at a new section of the map

DEFAULT_VOICE = "Samantha"
DEFAULT_RATE = 185


# ── sources: cards and banks ─────────────────────────────────────────────────
def resolve_srs_dir(study: v.Study, scenario: str | None) -> Path:
    return (study.scenarios_dir / scenario / "srs") if scenario else study.srs_dir


def load_cards(study: v.Study, scenario: str | None, boxes: list[int] | None) -> list[dict]:
    srs_dir = resolve_srs_dir(study, scenario)
    if not srs_dir.exists():
        sys.exit(f"no SRS deck at {srs_dir}")
    deck = scenario or "main"
    boxes = boxes or [1, 2, 3, 4]
    return v.collect_cards(study, srs_dir, boxes, deck)


def bank_path(study: v.Study, scenario: str | None, which: str) -> Path:
    """chunks|patterns bank — scenario-local if it exists, else study-level."""
    leaf = "chunks/reference.md" if which == "chunks" else "patterns/reference.md"
    if scenario:
        p = study.scenarios_dir / scenario / leaf
        if p.exists():
            return p
    return study.root / leaf


def parse_bank(path: Path) -> list[tuple[str, str, str]]:
    """Light markdown→items: returns (section, title, gloss) tuples.

    Handles both bank shapes:
      • table style  (| Concept | gloss | Status |)  → concept + gloss
      • heading style (### Pattern\\n Use when: ...)   → name + first prose line
    Code fences and status legends are skipped.
    """
    items: list[tuple[str, str, str]] = []
    section = ""
    pending_title = ""
    in_fence = False
    for raw in path.read_text().splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.startswith("## "):
            section = clean_md(line[3:])
            pending_title = ""
            continue
        if line.startswith("### "):
            pending_title = clean_md(line[4:])
            continue
        # heading-style body: first non-empty prose line after a ### becomes the gloss
        if pending_title and line.strip() and not line.startswith(("|", "#", "Status")):
            items.append((section, pending_title, clean_md(line)))
            pending_title = ""
            continue
        # table row: | col1 | col2 | ... |
        if line.startswith("|") and "|" in line[1:]:
            cols = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cols) < 2:
                continue
            title = clean_md(cols[0])
            if not title or title.lower() in ("concept", "chunk", "pattern", "front"):
                continue
            if set(title) <= set("-: "):  # separator row
                continue
            gloss = clean_md(cols[1])
            items.append((section, title, gloss))
    return items


def clean_md(text: str) -> str:
    text = re.sub(r"[*_`>#]", "", text)
    text = re.sub(r"\[\[[^\]]+\]\]", "", text)   # stray inline say-commands
    text = re.sub(r"\s+", " ", text).strip()
    text = text.strip('"')
    return text


# ── narration: build a spoken "map" ──────────────────────────────────────────
def speakable(text: str) -> str:
    """Make raw card/bank text flow as speech: expand a few SAA-isms, drop
    bracket noise, soften slashes/arrows into words."""
    t = clean_md(text)
    t = t.replace("→", " then ").replace("/", " or ").replace(" vs. ", " versus ")
    t = t.replace(" vs ", " versus ").replace("&", " and ")
    t = re.sub(r"\s+", " ", t).strip()
    return t


def script_from_cards(cards: list[dict], label: str) -> str:
    parts = [
        f"Velocidad audio map. {label}. {len(cards)} concepts. "
        f"After each prompt, answer in your head before I do.", WAYPOINT,
    ]
    last_domain = None
    for i, c in enumerate(cards, 1):
        domain = c.get("Domain") or c.get("Tags") or c.get("Type") or ""
        if domain and domain != last_domain:
            parts += [WAYPOINT, f"Section: {domain}.", BEAT]
            last_domain = domain
        parts += [
            f"{i}. {speakable(c['Front'])}", RECALL,
            f"The answer. {speakable(c['Back'])}", BEAT,
        ]
        if c.get("Note"):
            parts += [f"Worth noting. {speakable(c['Note'])}", PAUSE]
        else:
            parts.append(PAUSE)
    parts += [WAYPOINT, "End of map. Walk it again tomorrow."]
    return "\n".join(parts)


def script_from_bank(items: list[tuple[str, str, str]], label: str) -> str:
    parts = [
        f"Velocidad concept map. {label}. {len(items)} concepts.", WAYPOINT,
    ]
    last_section = None
    for section, title, gloss in items:
        if section and section != last_section:
            parts += [WAYPOINT, f"Section: {section}.", BEAT]
            last_section = section
        parts += [f"{speakable(title)}.", BEAT, f"{speakable(gloss)}", PAUSE]
    parts += [WAYPOINT, "End of map."]
    return "\n".join(parts)


# ── engines ──────────────────────────────────────────────────────────────────
def say_live(text: str, voice: str, rate: int) -> None:
    subprocess.run(["say", "-v", voice, "-r", str(rate), text], check=False)


def say_to_file(script: str, out: Path, voice: str, rate: int, want_m4a: bool) -> Path:
    aiff = out.with_suffix(".aiff")
    subprocess.run(["say", "-v", voice, "-r", str(rate), "-o", str(aiff), script], check=True)
    if want_m4a:
        m4a = out.with_suffix(".m4a")
        subprocess.run(
            ["afconvert", str(aiff), str(m4a), "-f", "m4af", "-d", "aac"], check=True
        )
        aiff.unlink(missing_ok=True)
        return m4a
    return aiff


def elevenlabs_to_file(script: str, out: Path, voice_id: str) -> Path:
    """Premium narration. Strips say-only [[slnc]] commands; uses urllib (no deps)."""
    import json
    import urllib.request

    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key:
        sys.exit("ELEVENLABS_API_KEY not set — needed for --engine elevenlabs")
    clean = re.sub(r"\[\[slnc \d+\]\]", " ... ", script)  # render pauses as ellipses
    body = json.dumps({
        "text": clean,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
    }).encode()
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    req = urllib.request.Request(
        url, data=body,
        headers={"xi-api-key": key, "Content-Type": "application/json",
                 "Accept": "audio/mpeg"},
    )
    mp3 = out.with_suffix(".mp3")
    with urllib.request.urlopen(req) as resp, mp3.open("wb") as f:
        f.write(resp.read())
    return mp3


# ── modes ────────────────────────────────────────────────────────────────────
def do_drill(args, study: v.Study) -> None:
    cards = load_cards(study, args.scenario, args.box)
    if not cards:
        sys.exit("no cards due / found")
    import random
    random.shuffle(cards)
    if args.limit:
        cards = cards[: args.limit]
    print(f"  Voice drill — {len(cards)} cards "
          f"({study.display}{'/' + args.scenario if args.scenario else ''}). "
          f"Enter to reveal, q to quit.\n")
    for i, c in enumerate(cards, 1):
        domain = c.get("Domain", "")
        print(f"  [{i}/{len(cards)}] {domain}")
        print(f"  ► {c['Front']}")
        say_live(speakable(c["Front"]), args.voice, args.rate)
        try:
            if input("    [say it → Enter] ").strip().lower() == "q":
                break
        except (EOFError, KeyboardInterrupt):
            break
        print(f"  ✦ {c['Back']}")
        say_live("The answer. " + speakable(c["Back"]), args.voice, args.rate)
        if c.get("Note"):
            print(f"    {c['Note']}")
            if args.notes:
                say_live("Worth noting. " + speakable(c["Note"]), args.voice, args.rate)
        print()
    print("  Done. (Drill mode doesn't grade — use ./velocidad srs for the Leitner update.)")


def do_listen(args, study: v.Study) -> None:
    scen = args.scenario
    if args.bank:
        items = parse_bank(bank_path(study, scen, args.bank))
        if args.section:
            items = [it for it in items if args.section.lower() in it[0].lower()]
        if args.limit:
            items = items[: args.limit]
        if not items:
            sys.exit("no bank items matched")
        label = f"{study.display}{' ' + scen if scen else ''} — {args.bank}"
        script = script_from_bank(items, label)
        n = len(items)
    else:
        cards = load_cards(study, scen, args.box)
        if args.limit:
            cards = cards[: args.limit]
        if not cards:
            sys.exit("no cards found")
        label = f"{study.display}{' ' + scen if scen else ''} — deck"
        script = script_from_cards(cards, label)
        n = len(cards)

    default_name = f"{study.name}{'-' + scen if scen else ''}{'-' + args.bank if args.bank else '-deck'}"
    out = Path(args.out).expanduser() if args.out else (SCRIPTS.parent / "audio" / default_name)
    out.parent.mkdir(parents=True, exist_ok=True)

    if args.script_only:
        txt = out.with_suffix(".txt")
        txt.write_text(re.sub(r"\[\[slnc \d+\]\]", "", script))
        print(f"  wrote narration script → {txt}")
        return

    if args.engine == "elevenlabs":
        path = elevenlabs_to_file(script, out, args.voice)
    else:
        path = say_to_file(script, out, args.voice, args.rate, args.m4a)
    size = path.stat().st_size
    print(f"  rendered {n} concepts → {path}  ({size/1024:.0f} KB)")
    print(f"  listen: open '{path}'   (or AirDrop it to your phone)")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["drill", "listen"])
    ap.add_argument("-s", "--study", default="spanish",
                    help="study key (default: spanish)")
    ap.add_argument("--scenario", help="scenario slug, e.g. mcdonalds")
    ap.add_argument("--box", type=lambda x: [int(n) for n in x.split(",")],
                    help="box(es) to pull, e.g. 1 or 1,2")
    ap.add_argument("--bank", choices=["chunks", "patterns"],
                    help="listen mode: narrate a concept/pattern bank instead of cards")
    ap.add_argument("--section", help="listen mode: only sections matching this text")
    ap.add_argument("--limit", type=int, help="cap number of items")
    ap.add_argument("--voice", default=DEFAULT_VOICE,
                    help=f"say voice or elevenlabs voice_id (default: {DEFAULT_VOICE})")
    ap.add_argument("--rate", type=int, default=DEFAULT_RATE,
                    help=f"say words-per-minute (default: {DEFAULT_RATE})")
    ap.add_argument("--engine", choices=["say", "elevenlabs"], default="say")
    ap.add_argument("--m4a", action="store_true",
                    help="listen mode: convert to phone-friendly .m4a (say engine)")
    ap.add_argument("-o", "--out", help="listen mode: output file path")
    ap.add_argument("--script-only", action="store_true",
                    help="listen mode: write the narration text, don't synthesize")
    ap.add_argument("--notes", action="store_true",
                    help="drill mode: also speak the Note line")
    args = ap.parse_args()

    if args.study not in v.STUDIES:
        sys.exit(f"unknown study '{args.study}' — choices: {', '.join(v.STUDIES)}")
    study = v.STUDIES[args.study]

    if args.mode == "drill":
        do_drill(args, study)
    else:
        do_listen(args, study)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
