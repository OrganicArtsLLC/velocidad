# The Learning-Science Layer

What the engine's drill tools actually do to your memory, and how to compose them. The flywheel
(Deploy → Capture → Distill → Drill → Redeploy) is the strategy; this layer makes the **Drill**
quarter of the wheel earn its keep. Added in v0.7.0 (see `docs/adr/0005-learning-science-layer.md`).

The premise, in one line: **difficulty during practice is not the enemy of learning — it is the
mechanism.** Every tool below manufactures a specific, productive difficulty and then measures
whether it's working.

---

## The tools, and the finding each one operationalizes

### `./velocidad daily` — interleaving

Pulls every due card from **all** studies and round-robin merges them, so a Spanish chunk is
followed by a system-design card is followed by a philosophy compression. Blocked practice (one
subject at a time) *feels* smoother and tests worse; interleaved practice feels scratchy and retains
dramatically better, because every card forces a fresh context switch — you must retrieve the
*kind* of answer before the answer.

Use it as the default morning review. Reach for per-study `srs` only when you're deliberately
loading one study before a session or an exam.

### `srs --calibrate` / `daily --calibrate` — metacognitive calibration

After you attempt a card and before the reveal, you rate confidence: `1` guess, `2` shaky,
`3` solid. `stats` then shows pass rate per confidence level. The number that matters is the
**"3 solid" row**: if it's below ~85%, your feeling of knowing is lying to you — and that feeling
is exactly what you'll be relying on mid-meeting, mid-conversation, mid-exam when there's no
reveal step. Judgments of learning are trainable; rating them is the training.

Run with `--calibrate` a couple of sessions per week — enough data to see the table move, not so
much friction that reviews drag.

### The `h` grade — honest pass/fail resolution

`y` got it clean · `h` got it, but slow or shaky · `n` missed. `h` still counts as a pass for box
movement (the Leitner core is unchanged), but it's recorded separately. A domain full of `h` is a
domain that will fail under time pressure even though the deck says it's fine — `stats` makes that
visible instead of letting it hide inside "correct."

### `./velocidad recall` — free recall (blurting) and the generation effect

Picks a substantial section of your chunk or pattern bank, shows you only the **title**, and makes
you dump everything you know out loud before revealing the section. Cards test *cued* recall — the
front hands you the retrieval hook. Real rooms don't. Free recall forces you to generate the
structure of the topic yourself, and the diff at the end ("name aloud 1–3 things you missed") is a
precision-guided card generator: every miss goes straight into `add`.

Use it 2–3× a week per active study, and always before a deploy that will draw on a whole topic
rather than single facts.

### `./velocidad add` — frictionless, format-safe capture

Guided card entry that writes the study's exact SRS format (plain or bold) and then **re-parses the
file to verify the card is visible**. The historic failure mode — a hand-formatted card that the
parser silently drops, so you never review it again — is structurally closed. Capture cost is the
biggest predictor of whether friction actually becomes cards; this makes capture cheap.

### `./velocidad stats` — the instrument panel

Review volume and recall rate (7/30 days), review-day streak, weakest-first domain breakdown,
the calibration table, and **leeches**. None of this is gamification; every number maps to an
action: a weak domain → `coach` or `interrogator`, a bad calibration row → more `--calibrate`
reps, a broken streak → shrink the session, never skip it.

### Leeches → `./velocidad coach` — re-encode, don't re-grind

A card that has failed 3+ times is not "hard," it is **badly encoded**: too big, no retrieval cue,
interfering with a sibling card, or abstract with no example. Re-grinding it wastes reps and
poisons morale. `coach` collects your leeches (with their current backs), your sub-75% domains,
and your latest session friction, and emits one paste-ready agent prompt whose job is to
*rewrite* the failing material — smaller cards, concrete examples, vivid anchors — and hand back a
delete list for the originals.

This is the flywheel closing: the system's own data, not your mood, decides what gets fixed next.

### `distributed-systems/prompts/interrogator.md` — Feynman mode / elaborative interrogation

For material that survives the deck but isn't *owned*. Four rounds: teach it to a junior, survive
why/when/compare/invert probes at the edges, apply it under a realistic constraint, then distill
cards from exactly where you broke. Explaining *why* a fact is true binds it to everything else
you know in a way that the fact alone never achieves. One topic, ~20 minutes, weekly per active
technical domain is plenty.

---

## How it composes — a day and a week

(The full step-by-step routine, including the session and deploy phases these slot into, is in
`docs/USER-GUIDE.md` — the operator's manual.)

**Daily (~15 min before any session work)**

```
./velocidad daily              # interleaved review, all studies (add --calibrate 2×/week)
./velocidad -s <study> start   # then the normal flywheel: session, deploy, distill
./velocidad -s <study> add     # capture today's friction as cards while it's hot
```

**Weekly (~30 min, pairs with each study's meta-observer prompt)**

```
./velocidad stats                      # where is recall weak? is calibration honest?
./velocidad -s <study> coach           # → agent mode: re-encode leeches, drill weak domains
./velocidad -s <study> recall          # blurt one big topic; card the misses
# + interrogator.md on the weakest technical domain
```

**The order of escalation when something won't stick:**

1. It fails once → normal Leitner demotion, no action.
2. It fails repeatedly (leech) → `coach`: rewrite the card, don't re-grind it.
3. It passes cards but feels thin → `recall` on its bank section.
4. It survives recall but can't be defended → `interrogator` (Feynman mode).
5. It survives all of that → it's owned; the only remaining test is a real deploy.

---

## What this layer deliberately does NOT do

- **No algorithm worship.** The 4-box Leitner schedule stays. The gains here come from *what* gets
  reviewed and *how it's encoded*, not from a fancier interval function on the same bad cards.
- **No streaks-as-product.** The streak number exists because consistency beats intensity for
  spaced practice, not as a thing to protect with junk reviews.
- **No replacement for deploys.** Every metric in `stats` is instrumentation. The scoreboard is
  still the only-metric-that-matters: real production, in real rooms, this week.
