#!/usr/bin/env python3
"""
Velocidad — multi-study daily engine.

One entry point for every study in the Velocidad learning engine. The engine handles the
mechanical work (SRS review, session scaffolding, surfacing the master prompt) so agent mode
handles the learning.

Usage:
    velocidad [--study NAME] start [--scenario NAME]   Morning routine
    velocidad [--study NAME] srs [--box N] [--calibrate]   Interactive SRS review
    velocidad daily [--calibrate]                      Interleaved review across ALL studies
    velocidad [--study NAME] blitz                     Rapid production drill (if the study has one)
    velocidad [--study NAME] recall                    Free-recall drill from the chunk/pattern banks
    velocidad [--study NAME] add [--scenario NAME]     Add SRS cards (format-checked, no silent drops)
    velocidad [--study NAME] stats                     Learning analytics (accuracy, calibration, leeches)
    velocidad [--study NAME] coach                     Agent prompt built from YOUR weak spots
    velocidad [--study NAME] finish                    Post-session wrap-up
    velocidad [--study NAME] prompt [--scenario NAME]  Show the study's master prompt
    velocidad status                                   Dashboard for ALL studies
    velocidad --study NAME status                      Dashboard for one study

--study defaults to "spanish" (the first/reference study), so `./velocidad start` is unchanged.
Studies are registered in STUDIES below; adding one is a config entry + its directories.
See docs/STUDY-SPEC.md for the study model, docs/KNOWLEDGE-ENGINE-OVERVIEW.md for the engine,
and docs/LEARNING-SCIENCE.md for what daily/recall/stats/coach/--calibrate are for.
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
import time
from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path
from typing import Optional


# ─── Configuration ───────────────────────────────────────────────────────────

ROOT = Path(__file__).resolve().parent.parent
BOX_SCHEDULE = {1: 1, 2: 2, 3: 3, 4: 7}  # box number: days between reviews

# ANSI color codes
C = {
    "0": "\033[0m", "b": "\033[1m", "d": "\033[2m",
    "r": "\033[31m", "g": "\033[32m", "y": "\033[33m",
    "bl": "\033[34m", "m": "\033[35m", "c": "\033[36m",
}


def s(text: str, *codes: str) -> str:
    """Style text with ANSI codes. s('hello', 'b', 'g') = bold green."""
    prefix = "".join(C.get(code, "") for code in codes)
    return f"{prefix}{text}{C['0']}" if prefix else text


# ─── Study registry ──────────────────────────────────────────────────────────

# Rapid-drill segments: (title, instruction, example). None = study has no blitz.
SPANISH_BLITZ = [
    ("GREETING CHAIN", "Produce every greeting you know. Don't stop talking.",
     "Hola, buenos días, buenas tardes, ¿cómo está?..."),
    ("PATTERN SPAM", "Pick ONE pattern. Generate as many variants as possible.",
     "Quiero + verb: comer, ir, hablar, aprender, pagar, ver..."),
    ("NUMBER SPRINT", "Count as high as you can. Then do money amounts.",
     "Uno, dos, tres... Son tres con cincuenta, son diez..."),
    ("SCENARIO NARRATION", "Narrate a full McDonald's visit start to finish.",
     "Voy a ir a McDonald's. Buenos días. Quiero un café..."),
    ("EMOTIONAL PHRASES", "Say heritage/family phrases with real feeling.",
     "Te quiero, papá. Estoy aprendiendo español..."),
]

PHILOSOPHY_DRILL = [
    ("POSITION SPRINT", "State a thinker's position + warrant + strongest objection, cold. As many as you can.",
     "Plato: knowledge is of the Forms, because the sensible world won't sit still... objection: Third Man."),
    ("STEELMAN SPRINT", "Pick a view you reject. State its strongest version and its best reason.",
     "The strongest case for X is... and the best reason a smart person holds it is..."),
    ("DEFINITION SPRINT", "Pin loaded terms precisely: justice, virtue, the Will, substance, telos.",
     "By 'virtue' Aristotle means a stable disposition (hexis), a mean between two vices..."),
    ("WARRANT SPRINT", "Make a claim, then immediately supply the warrant. No bare conclusions.",
     "Claim: ___. Because (warrant): ___. Support: ___."),
    ("OBJECTION SPRINT", "Name the strongest objection to each position you hold, and a first answer.",
     "The objection to the cogito is the Cartesian circle; a first answer is..."),
]

@dataclass
class Study:
    name: str
    display: str
    root: Path
    srs_format: str               # "plain" (Key: value) or "bold" (**Key:** value)
    friction_keys: list[str]
    blitz_segments: Optional[list] = None
    blitz_label: str = "5-MINUTE BLITZ"
    greeting: str = ""

    @property
    def srs_dir(self) -> Path: return self.root / "srs"
    @property
    def sessions_dir(self) -> Path: return self.root / "sessions"
    @property
    def scenarios_dir(self) -> Path: return self.root / "scenarios"
    @property
    def chunks_file(self) -> Path: return self.root / "chunks" / "reference.md"
    @property
    def patterns_file(self) -> Path: return self.root / "patterns" / "reference.md"
    @property
    def prompts_dir(self) -> Path: return self.root / "prompts"
    @property
    def review_log(self) -> Path: return self.srs_dir / ".last-review.json"

    def scenarios(self) -> list[str]:
        """Scenario slugs = subdirs of scenarios/ that contain a scenario.md."""
        if not self.scenarios_dir.exists():
            return []
        return sorted(
            d.name for d in self.scenarios_dir.iterdir()
            if d.is_dir() and (d / "scenario.md").exists()
        )


FRICTION_SPANISH = ["production_gaps", "comprehension_gaps", "recurring_errors",
                    "pronunciation_targets", "avoidance_patterns"]
FRICTION_PHILOSOPHY = ["production_gaps", "comprehension_gaps", "recurring_errors",
                       "missing_warrants", "misattributions", "strawman_reaches",
                       "avoidance_patterns"]

# Studies are directory plugins (see docs/adr/0002-study-plugin-architecture.md). Each entry
# points at a top-level study directory. Spanish is the reference study; register additional
# studies here as you add their directories (e.g. a `philosophy/` study — PHILOSOPHY_DRILL and
# FRICTION_PHILOSOPHY above are ready to wire in).
STUDIES: dict[str, Study] = {
    "spanish": Study(
        name="spanish", display="Spanish", root=ROOT / "spanish", srs_format="plain",
        friction_keys=FRICTION_SPANISH, blitz_segments=SPANISH_BLITZ,
        blitz_label="5-MINUTE BLITZ", greeting="Buenos días",
    ),
}
DEFAULT_STUDY = "spanish"


def resolve_study(name: Optional[str]) -> Study:
    return STUDIES[name or DEFAULT_STUDY]


# ─── SRS engine (format-aware; in-place edits) ───────────────────────────────
# Mirrors dashboard.py's parser/updater. The closing delimiter is matched with a
# lookahead so cards sharing a single --- separator are all captured.

def parse_srs_cards(path: Path, fmt: str) -> list[dict]:
    if not path.exists():
        return []
    text = path.read_text()
    raw_blocks = re.findall(r'\n---\n(.*?)(?=\n---)', text, re.DOTALL)
    cards: list[dict] = []
    for raw in raw_blocks:
        card: dict = {}
        if fmt == "plain":
            for line in raw.strip().splitlines():
                if ":" in line:
                    k, _, v = line.partition(":")
                    card[k.strip()] = v.strip()
        else:  # bold — **Key:** value
            for line in raw.strip().splitlines():
                m = re.match(r"\*\*(\w+):\*\*\s*(.*?)(\s{2})?$", line)
                if m:
                    card[m.group(1)] = m.group(2).strip()
        if "Front" in card and "Back" in card:
            card["_file"] = str(path)
            card["_raw"] = raw
            card["_fmt"] = fmt
            cards.append(card)
    return cards


def get_boxes(study: Study) -> dict[int, list[dict]]:
    return {n: parse_srs_cards(study.srs_dir / f"box{n}.md", study.srs_format)
            for n in range(1, 5)}


def count_cards_per_box(study: Study) -> dict[int, int]:
    return {n: len(parse_srs_cards(study.srs_dir / f"box{n}.md", study.srs_format))
            for n in range(1, 5)}


def update_card_srs(card: dict, passed: bool, fmt: str) -> str:
    """Update a card's Box/Streak in its source file; move file on promotion."""
    path = Path(card["_file"])
    text = path.read_text()
    old_raw = card["_raw"]
    streak = int(card.get("Streak", 0))
    box_num = int(card.get("Box", 1))

    if passed:
        streak += 1
        if streak >= 2 and box_num < 4:
            new_box, streak = box_num + 1, 0
        else:
            new_box = box_num
    else:
        streak, new_box = 0, 1

    new_raw = old_raw
    if fmt == "plain":
        new_raw = re.sub(r"(?m)^Box: \d+$", f"Box: {new_box}", new_raw)
        new_raw = re.sub(r"(?m)^Streak: \d+$", f"Streak: {streak}", new_raw)
    else:
        new_raw = re.sub(r"\*\*Box:\*\* \d+", f"**Box:** {new_box}", new_raw)
        new_raw = re.sub(r"\*\*Streak:\*\* \d+", f"**Streak:** {streak}", new_raw)

    old_marker = f"\n---\n{old_raw}\n---"

    if new_box != box_num:
        # Collapse the card + its two delimiters into one --- so neighbors don't merge.
        path.write_text(text.replace(old_marker, "\n---", 1))
        target = path.parent / f"box{new_box}.md"
        if not target.exists():                       # create target so the card is never lost
            target.write_text(f"# SRS — Box {new_box}\n")
        target.write_text(target.read_text().rstrip("\n") + f"\n\n---\n{new_raw}\n---\n")
        return s(f"  ↑ Promoted → Box {new_box}!", "g")
    else:
        path.write_text(text.replace(old_marker, f"\n---\n{new_raw}\n---", 1))
        if passed:
            return s(f"  ✓ Streak {streak}/2" + (" — almost there!" if streak == 1 else ""), "g")
        return s("  ✗ Stays in Box 1", "y")


# ─── Review history (append-only learning record) ───────────────────────────
# Every graded card appends one JSON line to <deck>/srs/.review-history.jsonl
# (gitignored — personal state). stats, coach, and leech detection read it.
# Box files stay the source of truth for scheduling; losing the history only
# costs analytics, never cards.

def history_path(srs_dir: Path) -> Path:
    return srs_dir / ".review-history.jsonl"


def log_history(srs_dir: Path, record: dict) -> None:
    path = history_path(srs_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def load_history(study: Study) -> list[dict]:
    """All review events for a study: main deck + every per-scenario deck."""
    paths = [history_path(study.srs_dir)]
    if study.scenarios_dir.exists():
        paths.extend(sorted(study.scenarios_dir.glob("*/srs/.review-history.jsonl")))
    events: list[dict] = []
    for p in paths:
        if not p.exists():
            continue
        for line in p.read_text().splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return events


def card_events(events: list[dict]) -> list[dict]:
    return [e for e in events if e.get("kind", "card") == "card"]


def recent(events: list[dict], days: int) -> list[dict]:
    cutoff = (date.today() - timedelta(days=days - 1)).isoformat()
    return [e for e in events if e.get("date", "") >= cutoff]


def accuracy(events: list[dict]) -> Optional[float]:
    if not events:
        return None
    ok = sum(1 for e in events if e.get("result") in ("pass", "hard"))
    return ok / len(events)


def review_day_streak(events: list[dict]) -> int:
    """Consecutive days with >=1 graded card, ending today or yesterday."""
    days = {e["date"] for e in events if "date" in e}
    if not days:
        return 0
    d = date.today()
    if d.isoformat() not in days:
        d -= timedelta(days=1)
        if d.isoformat() not in days:
            return 0
    streak = 0
    while d.isoformat() in days:
        streak += 1
        d -= timedelta(days=1)
    return streak


def find_leeches(events: list[dict], min_fails: int = 3) -> list[tuple[str, int, int]]:
    """Cards that keep failing = badly encoded, not 'hard'. Returns
    (front, fails, reviews) sorted by fail count, worst first."""
    fails: dict[str, int] = {}
    seen: dict[str, int] = {}
    for e in events:
        front = e.get("front", "")
        if not front:
            continue
        seen[front] = seen.get(front, 0) + 1
        if e.get("result") == "fail":
            fails[front] = fails.get(front, 0) + 1
    leeches = [(f, n, seen[f]) for f, n in fails.items() if n >= min_fails]
    return sorted(leeches, key=lambda t: -t[1])


def domain_breakdown(events: list[dict], min_reviews: int = 3) -> list[tuple[str, int, float]]:
    """(domain, reviews, accuracy) sorted weakest first."""
    by_dom: dict[str, list[int]] = {}
    for e in events:
        dom = e.get("domain") or "(untagged)"
        ok = 1 if e.get("result") in ("pass", "hard") else 0
        by_dom.setdefault(dom, []).append(ok)
    rows = [(d, len(v), sum(v) / len(v)) for d, v in by_dom.items() if len(v) >= min_reviews]
    return sorted(rows, key=lambda t: t[2])


# ─── Review schedule ─────────────────────────────────────────────────────────

def load_review_log(review_log: Path) -> dict:
    if review_log.exists():
        return json.loads(review_log.read_text())
    return {}


def save_review_log(review_log: Path, log: dict) -> None:
    review_log.parent.mkdir(parents=True, exist_ok=True)
    review_log.write_text(json.dumps(log, indent=2) + "\n")


def boxes_due_today(review_log: Path) -> list[int]:
    log = load_review_log(review_log)
    today = date.today()
    due: list[int] = []
    for box_num, interval in BOX_SCHEDULE.items():
        last = log.get(f"box{box_num}")
        if last is None:
            due.append(box_num)
        elif (today - date.fromisoformat(last)).days >= interval:
            due.append(box_num)
    return due


# ─── Sessions ────────────────────────────────────────────────────────────────

def today_str() -> str:
    return date.today().isoformat()


def get_latest_scenario(study: Study) -> str:
    """Most recent session's scenario (reads 'scenario', falls back to legacy 'world')."""
    fallback = (study.scenarios() or ["session"])[0]
    if not study.sessions_dir.exists():
        return fallback
    dirs = sorted(
        (d for d in study.sessions_dir.iterdir()
         if d.is_dir() and re.match(r"\d{4}-\d{2}-\d{2}", d.name)),
        reverse=True,
    )
    for d in dirs:
        friction = d / "friction.json"
        if friction.exists():
            try:
                data = json.loads(friction.read_text())
                return data.get("scenario", data.get("world", fallback))
            except (json.JSONDecodeError, KeyError):
                pass
    return fallback


def count_sessions(study: Study) -> int:
    if not study.sessions_dir.exists():
        return 0
    return len([d for d in study.sessions_dir.iterdir()
                if d.is_dir() and re.match(r"\d{4}-\d{2}-\d{2}", d.name)])


def create_session_folder(study: Study, scenario: str, level: str = "L1") -> Path:
    folder = study.sessions_dir / today_str()
    if folder.exists():
        return folder
    folder.mkdir(parents=True, exist_ok=True)

    (folder / "plan.md").write_text(
        f"# Session Plan — {today_str()}\n\n"
        f"Study: {study.name}\n"
        f"Scenario: {scenario}\n"
        f"Ladder: {level}\n"
        f"Focus: \n\n"
        f"## Warmup (3x each)\n1. \n2. \n3. \n\n"
        f"## Session Goal\n\n\n"
        f"## Micro-Deploy Mission\n"
        f"- Where: \n- Entry: \n- Goal: \n- Exit: \n- Win condition: \n"
    )
    (folder / "transcript.md").write_text(
        f"# Session Transcript — {today_str()}\n\n"
        f"Study: {study.name}\nScenario: {scenario}\nLevel: {level}\n\n---\n\n"
    )
    friction = {"date": today_str(), "study": study.name, "scenario": scenario}
    friction.update({k: [] for k in study.friction_keys})
    (folder / "friction.json").write_text(json.dumps(friction, indent=2) + "\n")
    (folder / "debrief.md").write_text(
        f"# Session Debrief — {today_str()}\n\n"
        f"## What Worked\n\n\n## What Broke\n\n\n## Corrections (top 3)\n\n\n"
        f"## Deploy Report\n- Deployed: \n- Where: \n- What happened: \n\n"
        f"## Tomorrow's Focus\n\n"
    )
    return folder


# ─── Display helpers ─────────────────────────────────────────────────────────

def banner(text: str) -> None:
    width = 56
    print()
    print(s("═" * width, "c"))
    print(s(f"  {text}", "b"))
    print(s("═" * width, "c"))
    print()


def section(title: str) -> None:
    print(s(f"\n{'─' * 50}", "d"))
    print(s(f"  {title}", "b"))
    print(s("─" * 50, "d"))


def show_status(study: Study) -> None:
    counts = count_cards_per_box(study)
    total = sum(counts.values())
    due = boxes_due_today(study.review_log)
    sessions = count_sessions(study)

    print(f"  {s('SRS Cards:', 'b')}")
    for box_num in range(1, 5):
        count = counts.get(box_num, 0)
        due_tag = s(" ← DUE", "y") if box_num in due else ""
        bar = s("█" * min(count, 30), "g" if box_num == 4 else "c")
        print(f"    Box {box_num}: {count:3d}  {bar}{due_tag}")
    print(f"    {'─' * 36}")
    print(f"    Total: {total} cards  |  Mastered: {counts.get(4, 0)}")
    print()
    print(f"  {s('Progress:', 'b')}")
    print(f"    Sessions completed: {sessions}")
    print(f"    Current scenario: {get_latest_scenario(study)}")
    print(f"    Scenarios available: {len(study.scenarios())}")

    events = card_events(load_history(study))
    if events:
        streak = review_day_streak(events)
        last7 = recent(events, 7)
        acc7 = accuracy(last7)
        line = f"    Review streak: {streak} day{'s' if streak != 1 else ''}"
        if acc7 is not None:
            line += f"  |  Last 7 days: {len(last7)} reviews, {acc7 * 100:.0f}% recall"
        print(line)


def show_status_all() -> None:
    banner("VELOCIDAD — All Studies")
    for st in STUDIES.values():
        if not st.root.exists():
            continue
        counts = count_cards_per_box(st)
        due = sum(counts.get(b, 0) for b in boxes_due_today(st.review_log))
        section(f"{st.display}  [{st.name}]")
        print(f"  SRS: {sum(counts.values())} cards "
              f"(due: {s(str(due), 'y')}, mastered: {s(str(counts.get(4, 0)), 'g')})  |  "
              f"Scenarios: {len(st.scenarios())}  |  Sessions: {count_sessions(st)}")
    print()
    print(s("  Drill one study:  ./velocidad --study <name> <command>", "d"))
    print()


# ─── SRS review ──────────────────────────────────────────────────────────────

def collect_cards(study: Study, srs_dir: Path, boxes: list[int], deck: str = "main") -> list[dict]:
    """Parse cards from the given boxes and attach the context the grading loop
    and history log need (_study/_deck/_srs_dir ride along with _file/_raw/_fmt)."""
    cards: list[dict] = []
    for n in boxes:
        for c in parse_srs_cards(srs_dir / f"box{n}.md", study.srs_format):
            c["_study"] = study.name
            c["_deck"] = deck
            c["_srs_dir"] = srs_dir
            cards.append(c)
    return cards


def grade_cards(cards: list[dict], calibrate: bool = False) -> tuple[int, int]:
    """Shared interactive grading loop. y = clean recall, h = got it but slow/shaky
    (passes for box movement, logged as 'hard' for analytics), n = miss.
    With calibrate=True, asks for a confidence rating after the attempt, before the
    reveal — pass rate per confidence level shows up in `stats` as calibration.
    Marks each graded card with _graded so callers know what was actually reviewed."""
    total = len(cards)
    correct = wrong = 0
    print(s("  Say the answer OUT LOUD, then Enter to reveal.  "
            "[y] got it  [h] hard  [n] missed  [q] quit\n", "d"))

    for i, card in enumerate(cards, 1):
        tag = card.get("Domain", card.get("Tags", card.get("Type", "")))
        counter = f"[{i}/{total}]"
        box_lbl = f"(Box {card.get('Box', '?')})"
        study_lbl = s(f" {card['_study']}", "c") if card.get("_show_study") else ""
        print(f"  {s(counter, 'd')}{study_lbl} {s(tag, 'm')} {s(box_lbl, 'd')}")
        print(f"  {s('►', 'y')} {card['Front']}")
        shown = time.time()
        try:
            input(s("    [SAY IT → Enter] ", "d"))
        except (EOFError, KeyboardInterrupt):
            print(s("\n  Review stopped.", "y"))
            break
        secs = round(time.time() - shown, 1)

        conf = None
        if calibrate:
            while True:
                try:
                    c_in = input(s("    Confidence? [1 guess / 2 shaky / 3 solid / Enter skip]: ", "c")).strip()
                except (EOFError, KeyboardInterrupt):
                    c_in = ""
                if c_in in ("", "1", "2", "3"):
                    break
            conf = int(c_in) if c_in else None

        print(f"  {s('✦', 'g')} {s(card['Back'], 'b')}")
        if card.get("Note"):
            print(f"    {s(card['Note'], 'd')}")
        while True:
            try:
                r = input(s("    Recall? [y/h/n/q]: ", "c")).strip().lower()
            except (EOFError, KeyboardInterrupt):
                r = "q"
            if r in ("y", "h", "n", "q", ""):
                break
        if r == "q":
            print(s("\n  Review stopped early.", "y"))
            break
        passed = r in ("y", "h", "")
        result = {"y": "pass", "": "pass", "h": "hard", "n": "fail"}[r]
        msg = update_card_srs(card, passed, card["_fmt"])
        card["_graded"] = True
        log_history(card["_srs_dir"], {
            "ts": int(time.time()), "date": today_str(), "kind": "card",
            "study": card["_study"], "deck": card.get("_deck", "main"),
            "front": card["Front"][:120], "domain": tag,
            "box": int(card.get("Box", 1) or 1),
            "result": result, "conf": conf, "secs": secs,
        })
        if passed:
            correct += 1
        else:
            wrong += 1
        print(msg)
        print()
    return correct, wrong


def finish_review(correct: int, wrong: int) -> None:
    section("REVIEW COMPLETE")
    reviewed = correct + wrong
    acc = (correct / reviewed * 100) if reviewed else 0
    print(f"  Correct: {s(str(correct), 'g')}  Wrong: {s(str(wrong), 'r')}  "
          f"Accuracy: {s(f'{acc:.0f}%', 'b')}")
    print()


def mark_boxes_reviewed(review_log: Path, boxes: list[int]) -> None:
    log = load_review_log(review_log)
    for box_num in boxes:
        log[f"box{box_num}"] = today_str()
    save_review_log(review_log, log)


def run_srs_review(study: Study, box_filter: Optional[list[int]] = None,
                   scenario: Optional[str] = None, calibrate: bool = False) -> None:
    if scenario:
        srs_dir = study.scenarios_dir / scenario / "srs"
        if not srs_dir.exists():
            print(s(f"  No SRS deck for scenario '{scenario}' ({srs_dir.relative_to(ROOT)}).", "y"))
            return
        label = f"{study.display} / {scenario}"
        deck = scenario
    else:
        srs_dir = study.srs_dir
        label = study.display
        deck = "main"
    review_log = srs_dir / ".last-review.json"

    due = box_filter or boxes_due_today(review_log)
    cards = collect_cards(study, srs_dir, due, deck)
    if not cards:
        print(s("  No cards due for review. ✓", "g"))
        return

    random.shuffle(cards)
    box_label = ", ".join(str(b) for b in sorted(due))
    section(f"SRS REVIEW — {len(cards)} cards from Box {box_label}  ({label})")
    correct, wrong = grade_cards(cards, calibrate)

    # Mark boxes done only if at least one card was actually graded.
    if any(c.get("_graded") for c in cards):
        mark_boxes_reviewed(review_log, due)
    finish_review(correct, wrong)


def run_daily(calibrate: bool = False) -> None:
    """Interleaved review: due cards from EVERY study, round-robin merged so
    consecutive cards switch studies. Interleaving feels harder than blocked
    review — that difficulty is the point (see docs/LEARNING-SCIENCE.md)."""
    per_study: list[tuple[Study, list[int], list[dict]]] = []
    for st in STUDIES.values():
        if not st.root.exists():
            continue
        due = boxes_due_today(st.review_log)
        cards = collect_cards(st, st.srs_dir, due)
        if cards:
            random.shuffle(cards)
            for c in cards:
                c["_show_study"] = True
            per_study.append((st, due, cards))

    if not per_study:
        print(s("  Nothing due in any study. ✓", "g"))
        return

    queues = [list(cards) for _, _, cards in per_study]
    mixed: list[dict] = []
    while any(queues):
        for q in queues:
            if q:
                mixed.append(q.pop(0))

    names = ", ".join(st.display for st, _, _ in per_study)
    banner(f"DAILY INTERLEAVED REVIEW — {len(mixed)} cards ({names})")
    correct, wrong = grade_cards(mixed, calibrate)

    for st, due, cards in per_study:
        if any(c.get("_graded") for c in cards):
            mark_boxes_reviewed(st.review_log, due)
    finish_review(correct, wrong)


# ─── Warmup + blitz ──────────────────────────────────────────────────────────

def get_warmup(study: Study, count: int = 5) -> list[str]:
    cards: list[dict] = []
    for n in (1, 2):
        cards.extend(parse_srs_cards(study.srs_dir / f"box{n}.md", study.srs_format))
    if not cards:
        cards = [c for n in (3, 4)
                 for c in parse_srs_cards(study.srs_dir / f"box{n}.md", study.srs_format)]
    # Prefer production/position cards if typed
    preferred = [c for c in cards if c.get("Type", "").lower() in ("prod", "production", "position")]
    pool = preferred or cards
    if not pool:
        return []
    random.shuffle(pool)
    return [c["Back"] for c in pool[:count]]


def run_blitz(study: Study) -> None:
    if not study.blitz_segments:
        print(s(f"  No rapid drill configured for the {study.display} study.", "y"))
        return
    banner(f"{study.blitz_label} — Produce, produce, produce!")
    print(s("  SAY EVERYTHING OUT LOUD. Speed matters.\n", "y"))
    try:
        input(s("  Press Enter to start the clock... ", "c"))
    except (EOFError, KeyboardInterrupt):
        return
    start = time.time()
    for idx, (title, instruction, hint) in enumerate(study.blitz_segments, 1):
        elapsed = time.time() - start
        remaining = max(0, 300 - elapsed)
        if remaining <= 0:
            break
        seg = min(60, remaining)
        print(f"\n  {s(f'MINUTE {idx}:', 'b')} {s(title, 'm')}")
        print(f"  {instruction}")
        print(s(f"  e.g. {hint}", "d"))
        end = time.time() + seg
        try:
            while time.time() < end:
                left = int(end - time.time())
                m, sec = divmod(left, 60)
                sys.stdout.write(f"\r  ⏱  {s(f'{m}:{sec:02d}', 'y')} remaining    ")
                sys.stdout.flush()
                time.sleep(0.5)
        except KeyboardInterrupt:
            print(s("\n\n  Drill stopped.", "y"))
            return
        sys.stdout.write(f"\r  ⏱  {s('TIME!', 'r')}               \n")
    total = int(time.time() - start)
    m, sec = divmod(total, 60)
    print(f"\n  {s('DRILL COMPLETE!', 'b', 'g')}  ({m}:{sec:02d})\n")


# ─── Master prompt ───────────────────────────────────────────────────────────

def show_prompt(study: Study, scenario: str = "", level: str = "L1") -> None:
    prompt_file = study.prompts_dir / "master.md"
    if not prompt_file.exists():
        print(s(f"  No master prompt for {study.display} ({prompt_file} not found).", "r"))
        return
    content = prompt_file.read_text()
    # Generic placeholder fill: [SCENARIO …] and [L1/L2/L3 …]
    if scenario:
        content = re.sub(r"\[SCENARIO[^\]]*\]", scenario, content)
    content = re.sub(r"\[L1/L2/L3[^\]]*\]", level, content)

    section(f"MASTER PROMPT — {study.display} — copy into agent mode")
    print(s(f"  Study: {study.name}   Scenario: {scenario or '(choose)'}   Level: {level}\n", "d"))
    print(content)
    print()


# ─── Commands ────────────────────────────────────────────────────────────────

def run_start(study: Study, scenario: Optional[str] = None) -> None:
    if scenario is None:
        scenario = get_latest_scenario(study)
    level = "L1"
    day = count_sessions(study) + 1
    hello = f"{study.greeting} — " if study.greeting else ""
    banner(f"VELOCIDAD — {study.display} — {hello}Day {day}")

    section("STATUS")
    show_status(study)

    due = boxes_due_today(study.review_log)
    have_due = any(count_cards_per_box(study).get(b, 0) for b in due)
    if have_due:
        try:
            r = input(s("\n  SRS cards due. Review now? [Y/n]: ", "c")).strip().lower()
        except (EOFError, KeyboardInterrupt):
            r = "n"
        if r != "n":
            run_srs_review(study, due)
    else:
        print(s("\n  No SRS cards due today. ✓", "g"))

    warmup = get_warmup(study)
    if warmup:
        section("WARMUP — say each aloud 3x")
        for i, p in enumerate(warmup, 1):
            print(f"  {i}. {s(p, 'b')}")
        try:
            input(s("\n  [Warmup done → Enter] ", "d"))
        except (EOFError, KeyboardInterrupt):
            print()

    if study.blitz_segments:
        try:
            b = input(s("  Run the rapid drill? [y/N]: ", "c")).strip().lower()
        except (EOFError, KeyboardInterrupt):
            b = "n"
        if b == "y":
            run_blitz(study)

    folder = create_session_folder(study, scenario, level)
    section("SESSION READY")
    print(f"  Study:    {s(study.display, 'b')}")
    print(f"  Scenario: {s(scenario, 'b')}")
    print(f"  Folder:   {s(str(folder.relative_to(ROOT)), 'd')}")
    print("\n  Next: paste the master prompt into agent mode.\n")
    try:
        r = input(s("  Show master prompt now? [Y/n]: ", "c")).strip().lower()
    except (EOFError, KeyboardInterrupt):
        r = "n"
    if r != "n":
        show_prompt(study, scenario, level)


def run_finish(study: Study) -> None:
    banner(f"SESSION COMPLETE — {study.display}")
    folder = study.sessions_dir / today_str()
    if not folder.exists():
        print(s("  No session folder for today. Run './velocidad start' first.", "y"))
        return

    section("DEPLOYMENT REPORT")
    try:
        deployed = input(s("  Did you deploy this in a real exchange today? [y/n]: ", "c")).strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        return
    if deployed == "y":
        try:
            where = input(s("  Where? ", "c")).strip()
            what = input(s("  What happened? (1 sentence): ", "c")).strip()
        except (EOFError, KeyboardInterrupt):
            where = what = ""
        debrief = folder / "debrief.md"
        if debrief.exists():
            t = debrief.read_text().replace(
                "- Deployed: \n- Where: \n- What happened: ",
                f"- Deployed: Yes\n- Where: {where}\n- What happened: {what}",
            )
            debrief.write_text(t)
            print(s("  ✓ Logged to debrief.md", "g"))
    else:
        print(s("  No deploy today. That's OK — deploy tomorrow.", "y"))

    section("CURRENT STATUS")
    show_status(study)

    section("NEXT STEPS")
    print("  Paste these prompts into agent mode (in this study's prompts/ dir):")
    print(f"   1. {s('distiller', 'b')}      → extract friction from your session")
    print(f"   2. {s('srs-generator', 'b')}  → create cards for Box 1")
    print(f"   Prompts: {s(str(study.prompts_dir.relative_to(ROOT)) + '/', 'd')}")
    print()


# ─── Stats (learning analytics from the review history) ─────────────────────

def run_stats(study: Study) -> None:
    banner(f"LEARNING STATS — {study.display}")
    events = card_events(load_history(study))
    if not events:
        print(s("  No review history yet. It accrues automatically as you review:", "y"))
        print(s("    ./velocidad daily          (interleaved, all studies)", "d"))
        print(s(f"    ./velocidad -s {study.name} srs --calibrate", "d"))
        print()
        return

    section("VOLUME & RETENTION")
    streak = review_day_streak(events)
    for label, days in (("Last 7 days", 7), ("Last 30 days", 30)):
        window = recent(events, days)
        acc = accuracy(window)
        hard = sum(1 for e in window if e.get("result") == "hard")
        if window:
            print(f"  {label}: {len(window)} reviews  |  recall {s(f'{acc * 100:.0f}%', 'b')}"
                  f"  ({hard} hard)")
        else:
            print(f"  {label}: 0 reviews")
    print(f"  Review-day streak: {s(str(streak), 'b')}  |  Lifetime reviews: {len(events)}")

    rows = domain_breakdown(recent(events, 30))
    if rows:
        section("BY DOMAIN — weakest first (last 30 days)")
        for dom, n, acc in rows:
            color = "r" if acc < 0.7 else ("y" if acc < 0.85 else "g")
            print(f"  {s(f'{acc * 100:3.0f}%', color)}  {dom}  ({n} reviews)")

    rated = [e for e in events if e.get("conf")]
    if rated:
        section("CALIBRATION — does confidence match reality?")
        for conf, label in ((1, "1 guess"), (2, "2 shaky"), (3, "3 solid")):
            sub = [e for e in rated if e.get("conf") == conf]
            if sub:
                acc = accuracy(sub)
                print(f"  {label}: {len(sub)} cards → {acc * 100:.0f}% correct")
        solid = [e for e in rated if e.get("conf") == 3]
        solid_acc = accuracy(solid)
        if solid_acc is not None and solid_acc < 0.85 and len(solid) >= 5:
            print(s("  ⚠ 'Solid' cards fail too often — you're overconfident. Slow down on the reveal.", "y"))

    leeches = find_leeches(events)
    if leeches:
        section(f"LEECHES — {len(leeches)} cards that keep failing (re-encode, don't re-grind)")
        for front, fails, total in leeches[:8]:
            print(f"  {s(f'✗{fails}/{total}', 'r')}  {front[:70]}")
        print(s(f"\n  A card that fails {leeches[0][1]} times isn't hard — it's badly written.", "d"))
        print(s(f"  Run:  ./velocidad -s {study.name} coach   → a re-encoding prompt for agent mode", "d"))
    print()


def run_stats_all() -> None:
    banner("LEARNING STATS — All Studies")
    any_data = False
    for st in STUDIES.values():
        if not st.root.exists():
            continue
        events = card_events(load_history(st))
        section(f"{st.display}  [{st.name}]")
        if not events:
            print(s("  No review history yet.", "d"))
            continue
        any_data = True
        last7 = recent(events, 7)
        acc7 = accuracy(last7)
        acc_txt = f", recall {acc7 * 100:.0f}%" if acc7 is not None else ""
        print(f"  7-day: {len(last7)} reviews{acc_txt}  |  streak: {review_day_streak(events)}d"
              f"  |  leeches: {len(find_leeches(events))}  |  lifetime: {len(events)}")
    print()
    if any_data:
        print(s("  Detail:  ./velocidad --study <name> stats", "d"))
        print()


# ─── Add cards (format-checked capture) ──────────────────────────────────────

def format_card(fmt: str, fields: dict[str, str]) -> str:
    """Render a card body in the study's exact SRS format. Bold format keeps the
    two-trailing-space house style so markdown renders line breaks."""
    if fmt == "plain":
        order = ["Type", "Tags", "Front", "Back", "Box", "Streak", "Note"]
        return "\n".join(f"{k}: {fields[k]}" for k in order if fields.get(k))
    order = ["Type", "Domain", "Front", "Back", "Box", "Streak", "Note"]
    return "\n".join(f"**{k}:** {fields[k]}  " for k in order if fields.get(k))


def append_card(path: Path, fmt: str, fields: dict[str, str]) -> bool:
    """Append a card and verify the parser actually sees it (the whole point —
    a hand-formatted card that parses wrong silently vanishes from review)."""
    before = len(parse_srs_cards(path, fmt))
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        box = fields.get("Box", "1")
        path.write_text(f"# SRS — Box {box}\n")
    raw = format_card(fmt, fields)
    path.write_text(path.read_text().rstrip("\n") + f"\n\n---\n{raw}\n---\n")
    return len(parse_srs_cards(path, fmt)) == before + 1


def run_add(study: Study, scenario: Optional[str] = None, box: int = 1) -> None:
    if scenario:
        srs_dir = study.scenarios_dir / scenario / "srs"
        label = f"{study.display} / {scenario}"
    else:
        srs_dir = study.srs_dir
        label = study.display
    path = srs_dir / f"box{box}.md"
    tag_field = "Tags" if study.srs_format == "plain" else "Domain"

    banner(f"ADD SRS CARDS — {label} → box{box}.md")
    print(s("  Front/Back required; the rest optional. Empty Front ends the loop.\n", "d"))
    added = 0
    while True:
        try:
            front = input(s("  Front: ", "c")).strip()
            if not front:
                break
            back = input(s("  Back:  ", "c")).strip()
            if not back:
                print(s("  Back is required — card skipped.", "y"))
                continue
            ctype = input(s("  Type (optional): ", "c")).strip()
            tag = input(s(f"  {tag_field} (optional): ", "c")).strip()
            note = input(s("  Note (optional): ", "c")).strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        fields = {"Type": ctype, tag_field: tag, "Front": front, "Back": back,
                  "Box": str(box), "Streak": "0", "Note": note}
        if append_card(path, study.srs_format, fields):
            added += 1
            print(s(f"  ✓ Added and verified — the parser sees it. ({path.relative_to(ROOT)})\n", "g"))
        else:
            print(s("  ⚠ Card written but the parser did NOT pick it up — check the file by hand.", "r"))
            print(s(f"    {path}\n", "r"))
    if added:
        print(s(f"  {added} card{'s' if added != 1 else ''} added to Box {box}.", "g"))
    print()


# ─── Free recall (blurting) ──────────────────────────────────────────────────

def bank_sections(study: Study) -> list[tuple[str, str, str]]:
    """(source, title, body) for every substantial ##/### section in the banks."""
    out: list[tuple[str, str, str]] = []
    for src, path in (("chunks", study.chunks_file), ("patterns", study.patterns_file)):
        if not path.exists():
            continue
        parts = re.split(r"(?m)^(#{2,3} .+)$", path.read_text())
        for i in range(1, len(parts) - 1, 2):
            title = parts[i].lstrip("#").strip()
            body = parts[i + 1].strip()
            if len(body) >= 120:
                out.append((src, title, body))
    return out


def run_recall(study: Study) -> None:
    """Free-recall drill: dump everything you know about a bank section from
    memory FIRST, then diff against the bank. Retrieval without cues is the
    strongest consolidation signal there is — flashcards only test cued recall."""
    sections = bank_sections(study)
    if not sections:
        print(s(f"  No bank sections found for {study.display} "
                f"(need {study.chunks_file.relative_to(ROOT)} or patterns).", "y"))
        return

    banner(f"FREE RECALL — {study.display}")
    while True:
        src, title, body = random.choice(sections)
        print(f"  Topic: {s(title, 'b')}  {s(f'(from the {src} bank)', 'd')}")
        try:
            r = input(s("\n  [Enter] start  [r] reroll topic  [q] quit: ", "c")).strip().lower()
        except (EOFError, KeyboardInterrupt):
            return
        if r == "q":
            return
        if r == "r":
            print()
            continue
        print(s("\n  Brain-dump OUT LOUD (or on paper) everything you know about this topic.", "y"))
        print(s("  Every item, every distinction, every example. Don't stop early.", "y"))
        start = time.time()
        try:
            input(s("\n  [Done dumping → Enter] ", "d"))
        except (EOFError, KeyboardInterrupt):
            return
        secs = round(time.time() - start, 1)
        section(f"THE BANK SAYS — {title}")
        print(body)
        print()
        print(s("  Name ALOUD 1–3 things you missed. Each one is a card:", "y"))
        print(s(f"    ./velocidad -s {study.name} add", "d"))
        log_history(study.srs_dir, {
            "ts": int(time.time()), "date": today_str(), "kind": "recall",
            "study": study.name, "section": title, "secs": secs,
        })
        try:
            again = input(s("\n  Another round? [y/N]: ", "c")).strip().lower()
        except (EOFError, KeyboardInterrupt):
            return
        if again != "y":
            return
        print()


# ─── Coach (your data → a targeted agent prompt) ────────────────────────────

def latest_friction(study: Study) -> Optional[dict]:
    """Most recent session friction.json that has at least one non-empty list."""
    if not study.sessions_dir.exists():
        return None
    dirs = sorted(
        (d for d in study.sessions_dir.iterdir()
         if d.is_dir() and re.match(r"\d{4}-\d{2}-\d{2}", d.name)),
        reverse=True,
    )
    for d in dirs:
        f = d / "friction.json"
        if not f.exists():
            continue
        try:
            data = json.loads(f.read_text())
        except json.JSONDecodeError:
            continue
        if any(isinstance(v, list) and v for v in data.values()):
            return data
    return None


def all_current_cards(study: Study) -> dict[str, dict]:
    """front[:120] → card, across the main deck and every scenario deck."""
    lookup: dict[str, dict] = {}
    dirs = [study.srs_dir]
    if study.scenarios_dir.exists():
        dirs.extend(sorted(d / "srs" for d in study.scenarios_dir.iterdir()
                           if (d / "srs").is_dir()))
    for srs_dir in dirs:
        for n in range(1, 5):
            for c in parse_srs_cards(srs_dir / f"box{n}.md", study.srs_format):
                lookup[c["Front"][:120]] = c
    return lookup


CARD_FORMAT_SAMPLES = {
    "plain": (
        "---\n"
        "Type: prod\n"
        "Tags: [tags]\n"
        "Front: [cue]\n"
        "Back: [target answer]\n"
        "Box: 1\n"
        "Streak: 0\n"
        "Note: [optional]\n"
        "---"
    ),
    "bold": (
        "---\n"
        "**Type:** [type]  \n"
        "**Domain:** [domain]  \n"
        "**Front:** [cue]  \n"
        "**Back:** [target answer]  \n"
        "**Box:** 1  \n"
        "**Streak:** 0  \n"
        "**Note:** [optional]  \n"
        "---"
    ),
}


def run_coach(study: Study) -> None:
    """Compose leeches + weak domains + latest friction into one paste-ready
    agent prompt: re-encode what keeps failing, drill what's weak. This closes
    the flywheel — the system's own data decides what gets fixed next."""
    events = card_events(load_history(study))
    leeches = find_leeches(events)
    weak = [(d, n, a) for d, n, a in domain_breakdown(recent(events, 30)) if a < 0.75]
    friction = latest_friction(study)

    if not leeches and not weak and not friction:
        print(s(f"  Nothing to coach on yet for {study.display} — no leeches, no weak", "y"))
        print(s("  domains, no friction logged. Review and deploy first; the data will come:", "y"))
        print(s(f"    ./velocidad daily        ./velocidad -s {study.name} recall", "d"))
        print()
        return

    cards = all_current_cards(study)
    lines: list[str] = []
    lines.append(f"# Coach Session — Velocidad {study.display} — {today_str()}")
    lines.append("")
    lines.append("You are my learning coach for the Velocidad "
                 f"{study.display} study. My own review data (below) says exactly "
                 "what is failing. Work through it with me, one item at a time, "
                 "production-first — make me produce before you explain.")
    lines.append("")

    if leeches:
        lines.append("## 1. Re-encode these leech cards")
        lines.append("")
        lines.append("These cards keep failing. A card that fails repeatedly is badly *encoded*, "
                     "not 'hard' — re-grinding it is wasted reps. For EACH card below:")
        lines.append("- Diagnose why it fails: too big? no retrieval cue? interference with a sibling card? abstract back with no example?")
        lines.append("- Quiz me once to see where it actually breaks.")
        lines.append("- Rewrite it as 1–3 sharper cards: smaller scope, concrete example in the back, "
                     "a vivid anchor or mnemonic in the Note.")
        lines.append("")
        for front, fails, total in leeches[:8]:
            card = cards.get(front)
            back = f"\n  - Current back: {card['Back']}" if card else ""
            lines.append(f"- **{front}** — failed {fails}/{total} reviews{back}")
        lines.append("")

    if weak:
        lines.append(f"## {'2' if leeches else '1'}. Drill these weak domains")
        lines.append("")
        lines.append("Recall over the last 30 days, weakest first. Run 10-rep production "
                     "drills per domain (define it / use it / contrast it — under 15 seconds each), "
                     "then one elaboration question per domain: 'why is this true?' or "
                     "'how does this connect to something I already know cold?'")
        lines.append("")
        for dom, n, a in weak:
            lines.append(f"- **{dom}** — {a * 100:.0f}% recall ({n} reviews)")
        lines.append("")

    if friction:
        n = sum(1 for _ in (leeches, weak) if _) + 1
        lines.append(f"## {n}. Latest friction (session {friction.get('date', '?')}, "
                     f"scenario: {friction.get('scenario', friction.get('world', '?'))})")
        lines.append("")
        for key, val in friction.items():
            if isinstance(val, list) and val:
                lines.append(f"- **{key}**: " + "; ".join(str(v) for v in val))
        lines.append("")

    lines.append("## Output")
    lines.append("")
    lines.append("1. Replacement + new SRS cards, each wrapped in its own `---`…`---` with a "
                 "blank line between, in EXACTLY this format:")
    lines.append("")
    lines.append("```")
    lines.append(CARD_FORMAT_SAMPLES[study.srs_format])
    lines.append("```")
    lines.append("")
    lines.append("2. A delete list: the exact Front lines of old leech cards I should remove.")
    lines.append("3. One sentence: the single highest-leverage thing to drill tomorrow.")

    section(f"COACH PROMPT — {study.display} — paste into agent mode")
    print("\n".join(lines))
    print()


# ─── CLI ─────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="velocidad",
        description="Velocidad — multi-study daily engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Studies: " + ", ".join(STUDIES) + f"  (default: {DEFAULT_STUDY})\n\n"
            "  ./velocidad start                          Morning routine (default study)\n"
            "  ./velocidad srs --box 1                    Review one box of the SRS deck\n"
            "  ./velocidad srs --scenario mcdonalds       Review a scenario's own deck\n"
            "  ./velocidad prompt --scenario mcdonalds    Show the master prompt for a scenario\n"
            "  ./velocidad status                         Dashboard for ALL studies\n"
            "  ./velocidad daily --calibrate              Interleaved review, all studies, with confidence\n"
            "  ./velocidad stats                          Accuracy, calibration, leeches\n"
            "  ./velocidad coach                          Agent prompt built from your weak spots\n"
        ),
    )
    parser.add_argument("--study", "-s", choices=list(STUDIES), default=None,
                        help=f"Which study (default: {DEFAULT_STUDY}; 'status' with no --study shows all)")
    sub = parser.add_subparsers(dest="command")

    start_p = sub.add_parser("start", help="Morning routine")
    start_p.add_argument("--scenario", help="Today's scenario")

    srs_p = sub.add_parser("srs", help="SRS card review")
    srs_p.add_argument("--box", type=int, choices=[1, 2, 3, 4], help="Review a specific box")
    srs_p.add_argument("--scenario", help="Review a scenario's own deck (e.g. aws-saa-c03)")
    srs_p.add_argument("--calibrate", action="store_true",
                       help="Rate confidence before each reveal (calibration data for stats)")

    daily_p = sub.add_parser("daily", help="Interleaved SRS review across ALL studies")
    daily_p.add_argument("--calibrate", action="store_true",
                         help="Rate confidence before each reveal")

    sub.add_parser("blitz", help="Rapid production drill (if the study has one)")
    sub.add_parser("recall", help="Free-recall (blurting) drill from the chunk/pattern banks")
    sub.add_parser("stats", help="Learning analytics (all studies, or one with --study)")
    sub.add_parser("coach", help="Agent prompt built from your leeches, weak domains, and friction")
    sub.add_parser("finish", help="Post-session wrap-up")
    sub.add_parser("status", help="Dashboard (all studies, or one with --study)")

    add_p = sub.add_parser("add", help="Add SRS cards interactively (format-checked)")
    add_p.add_argument("--scenario", help="Add to a scenario's own deck instead of the main deck")
    add_p.add_argument("--box", type=int, choices=[1, 2, 3, 4], default=1,
                       help="Target box (default 1)")

    prompt_p = sub.add_parser("prompt", help="Show the study's master prompt")
    prompt_p.add_argument("--scenario", default="")
    prompt_p.add_argument("--level", default="L1")

    return parser


def main() -> None:
    args = build_parser().parse_args()

    # Cross-study commands first
    if args.command == "daily":
        run_daily(args.calibrate)
        return
    if args.command == "status" and args.study is None:
        show_status_all()
        return
    if args.command == "stats" and args.study is None:
        run_stats_all()
        return

    study = resolve_study(args.study)

    if args.command is None:
        build_parser().print_help()
        print()
        banner(f"VELOCIDAD — {study.display} — Quick Status")
        show_status(study)
        print()
        return

    if args.command == "start":
        run_start(study, args.scenario)
    elif args.command == "srs":
        run_srs_review(study, [args.box] if args.box else None, args.scenario, args.calibrate)
    elif args.command == "blitz":
        run_blitz(study)
    elif args.command == "recall":
        run_recall(study)
    elif args.command == "stats":
        run_stats(study)
    elif args.command == "coach":
        run_coach(study)
    elif args.command == "add":
        run_add(study, args.scenario, args.box)
    elif args.command == "finish":
        run_finish(study)
    elif args.command == "status":
        banner(f"VELOCIDAD — {study.display}")
        show_status(study)
        print()
    elif args.command == "prompt":
        scenario = args.scenario or get_latest_scenario(study)
        show_prompt(study, scenario, args.level)


if __name__ == "__main__":
    main()
