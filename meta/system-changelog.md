# System Changelog

How the Velocidad system itself evolves. Every adjustment to methodology, prompts, or structure gets logged here.

The system is recursive: it learns how you learn, and then it changes to learn better.

---

## v0.2.0 — April 2026

**Generalized into a domain-agnostic engine + engine/learner-data separation**

- Reframed the project as a reusable production-first fluency engine: any domain that can be
  simulated, fails discretely, and improves with repetition can plug in
  (`docs/KNOWLEDGE-ENGINE-OVERVIEW.md`).
- Added the domain contract (`docs/DOMAIN-SPEC.md`) and a worked guide for professional /
  technical vocabulary domains (`docs/TECHNICAL-TRACK.md`).
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
- Worlds based on the learner's actual people and places

## Adjustments Log

<!--
Format:
- [date] WHAT changed → WHY → RESULT (if known)
-->
