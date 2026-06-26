# System Changelog

How the Velocidad system itself evolves. Every adjustment to methodology, prompts, or structure gets logged here.

The system is recursive: it learns how you learn, and then it changes to learn better.

---

## v2.0.0 — June 2026

**Multi-study architecture + study/scenario vocabulary**

- Renamed the core vocabulary: a top-level subject is now a **study** (was "domain"), and a
  deployment context inside it is a **scenario** (was "world"). One vocabulary across every study.
- Moved the Spanish study out of the repo root into `spanish/`, making the root a clean, generic
  engine and Spanish a structural peer of future studies (`philosophy/`, `distributed-systems/`).
  See `docs/adr/0003-spanish-study-relocation.md`.
- Replaced `docs/DOMAIN-SPEC.md` with `docs/STUDY-SPEC.md` and `docs/WORLD-LADDER-TEMPLATE.md`
  with `docs/SCENARIO-LADDER-TEMPLATE.md`.
- Added `docs/LEARNING-SCIENCE.md` (the drill layer), `docs/USER-GUIDE.md` (the operator's
  manual), and `docs/adr/` (architecture decision records).

## v0.2.0 — April 2026

**Generalized into a study-agnostic engine + engine/learner-data separation**

- Reframed the project as a reusable production-first fluency engine: any study that can be
  simulated, fails discretely, and improves with repetition can plug in
  (`docs/KNOWLEDGE-ENGINE-OVERVIEW.md`).
- Added the study contract (`docs/STUDY-SPEC.md`) and a worked guide for professional /
  technical studies (`docs/TECHNICAL-TRACK.md`).
- Separated the public engine from private learner data via `docs/LEARNER-DATA-SPEC.md` and
  `config/paths.yaml.template` — sessions, SRS state, and profile live in a private data directory.
- Grew the prompt set to six (`master`, `session-runner`, `distiller`, `srs-generator`,
  `session-planner`, `meta-observer`).
- Standardized universal content as `chunks/reference.md` and `patterns/reference.md`.

## v0.1.0 — February 19, 2026

- Initial system design
- 5-Part Daily Engine defined
- Real-world deployment targets identified
- Language architecture map created
- Meta-observation layer added
- Scenarios based on the learner's actual people and places

## Adjustments Log

<!--
Format:
- [date] WHAT changed → WHY → RESULT (if known)
-->
