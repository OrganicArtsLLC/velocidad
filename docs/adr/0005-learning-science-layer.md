# 0005 — A learning-science layer on top of the Leitner core

**Status:** Accepted · 2026-06-10

## Context

Through v0.6.0 the engine's drill side was a 4-box Leitner deck reviewed per study, with no memory
of any review beyond a per-box "last reviewed" date. That left real learning-science levers on the
table:

- **No review history.** The system could not say which cards or domains were weak, whether
  retention was improving, or which cards were *leeches* (cards that fail repeatedly because they
  are badly encoded, not because the material is hard).
- **Blocked practice only.** Each study was reviewed in its own session. Interleaving related and
  unrelated material is one of the most robust findings in the retention literature, and the engine
  actively prevented it.
- **No metacognition.** Pass/fail grading captures recall but not *calibration* — whether confidence
  tracks competence. Overconfidence on "solid" material is invisible until it fails in a real room.
- **Cued recall only.** Flashcards test recognition of a specific cue. Free recall (blurting),
  elaborative interrogation, and teach-it-back are stronger consolidation signals, and the engine
  had banks full of material with no tool that exercised them that way.
- **The flywheel had a manual gap.** Friction logs and review results existed, but turning "what is
  failing" into "what to drill next" required the learner to do the synthesis by hand.

## Decision

Add an **additive** learning-science layer to `scripts/velocidad.py`; the Leitner core
(boxes, promotion on 2 straight passes, demotion to Box 1 on any miss, `BOX_SCHEDULE`) is unchanged,
and so is the card file format — existing decks need no migration.

1. **Review history.** Every graded card appends one JSON line to `<deck>/srs/.review-history.jsonl`
   (per main deck and per scenario deck, gitignored like `.last-review.json`). Box files remain the
   only source of truth for scheduling; the history powers analytics only, so losing it loses
   nothing but charts.
2. **Richer grading.** Review accepts `y / h / n` — `h` ("got it, but slow/shaky") passes for box
   movement but is logged distinctly. `--calibrate` adds an optional 1–3 confidence rating after
   the retrieval attempt, before the reveal; `stats` reports pass rate per confidence level.
3. **`daily`** — cross-study interleaved review: due cards from every study, round-robin merged so
   consecutive cards switch studies.
4. **`stats`** — volume, 7/30-day recall, review-day streak, weakest-first domain breakdown,
   calibration table, and leech detection (≥3 lifetime fails).
5. **`recall`** — free-recall drill: brain-dump a random substantial section of the chunk/pattern
   banks from memory, then diff against the bank.
6. **`add`** — guided card capture that writes the study's exact format and **verifies the parser
   sees the new card**, closing the long-standing "hand-formatted card silently drops" trap.
7. **`coach`** — composes leeches + weak domains + the latest session friction into one paste-ready
   agent prompt (re-encode, drill, delete list). This closes the flywheel: the system's own data
   decides what gets fixed next.

Prompt-side, the same layer-completion: the Distributed Systems study gains `interrogator.md`
(Feynman / elaborative-interrogation mode), and each study's prompt set is rounded out with its
`distiller.md`, `srs-generator.md`, and `meta-observer.md`. `docs/LEARNING-SCIENCE.md` documents
which research finding each tool operationalizes and how they compose into the daily flow.

## Consequences

- `dashboard.py` grading does **not** write review history yet; cards graded there are invisible to
  `stats`/`coach` until it adopts `log_history` (it shares the parser/updater contract already).
- The history file is append-only JSONL with a `kind` field (`card`, `recall`); new event kinds can
  be added without migration. Records carry `front[:120]` as the card identity — editing a card's
  Front line orphans its history, which is acceptable (a rewritten card *should* restart its record;
  rewriting is the prescribed cure for leeches).
- `daily` and `srs` now mark boxes as reviewed **only if at least one card was graded** (previously
  an immediate quit still marked the whole session done).
- Everything remains stdlib-only and format-aware, so every study ships the full layer unchanged.
