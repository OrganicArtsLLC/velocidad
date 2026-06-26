# 0002 — Studies are directory plugins on a generic engine

**Status:** Accepted · 2026-06-05

## Context

Velocidad began as a Spanish-fluency tool and grew into a multi-subject engine (Spanish, plus
planned Philosophy and Distributed Systems studies). The methodology (the Deploy → Capture →
Distill → Drill → Redeploy flywheel, the 4-box Leitner SRS, the friction log, the agent prompts) is
identical across subjects; only the *content* differs. We needed a way to add a subject without
touching engine internals.

## Decision

A **study is a directory** that implements `docs/STUDY-SPEC.md` (`scenarios/`, `srs/`, `chunks/`,
`patterns/`, reference material, and a study config). The engine treats studies uniformly:

- `scripts/velocidad.py` holds a `Study` dataclass whose every path (`srs_dir`, `sessions_dir`,
  `scenarios_dir`, `chunks_file`, `patterns_file`, `prompts_dir`, `review_log`) is **derived from a
  single `root`**. Registering a study = one entry in the `STUDIES` dict (name, display, `root`,
  `srs_format` ∈ {plain, bold}, `friction_keys`, optional `blitz_segments`) plus its directories.
- `dashboard.py` mirrors this with per-study path constants and routing dicts.
- The SRS parser is **format-aware** (plain `Key: value` vs bold `**Key:** value`) selected per study.

**Source of truth, recorded so it isn't mis-assumed:** the `STUDIES` dict in `velocidad.py` and the
constants in `dashboard.py` are authoritative. `config/paths.yaml` (and its template) is **documentation
for the agent prompts only** — the Python tools do not read it. A future change that "wires up
paths.yaml" must update the tools deliberately, not assume they already consume it.

## Consequences

- Adding a study is additive and low-risk: a config entry + a directory tree. No engine surgery.
- Because all paths derive from `root`, relocating a study is a one-line change (see ADR-0003).
- The `paths.yaml`-is-not-read gotcha is now documented; it has surprised readers before.
- Two SRS formats coexist by design (Spanish is `plain` for historical reasons; everything else is
  `bold`). A study declares its format; the shared parser/updater handle both.
