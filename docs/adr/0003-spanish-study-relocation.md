# 0003 — Move the Spanish study out of the repo root into `spanish/`

**Status:** Accepted · 2026-06

## Context

Spanish was the first study and was built *as* the repo: its content (`scenarios/`/`worlds/`, `srs/`,
`chunks/`, `patterns/`, `prompts/`, `sessions/`, `language-reference/`, parts of `meta/`) lived at the
repo root, while later studies were envisioned as self-contained folders (`philosophy/`,
`distributed-systems/`). The engine, config, and docs hardcoded "Spanish = root" (`Study(root=ROOT)`,
dashboard `ROOT/"srs"`, `paths.yaml` `path: "."`). This blurred the line between *engine* and *the
first study's content*, and made the root the only place that wasn't generic.

## Decision

Relocate the Spanish study into `spanish/`, making it a structural peer of any other study and the
root a clean, generic engine.

- **Content** moved via `git mv` (history preserved): `spanish/{scenarios,prompts,language-reference,
  chunks,patterns,sessions/TEMPLATE.md,meta/{language-architecture,memory-techniques}.md}`.
- **Engine** stays at root: `config/` templates, `docs/` (+ this `adr/`), `meta/system-changelog.md`,
  and the CLI/dashboard (forthcoming).
- **Code change is minimal** because of ADR-0002: `Study(root=ROOT) → Study(root=ROOT/"spanish")`;
  dashboard Spanish constants repoint to a `SPANISH` base; `paths.yaml.template` `"." → "./spanish"`.

This supersedes the "grandfathered reference study at root" framing in earlier drafts of
`docs/STUDY-SPEC.md`.

## Consequences

- The root is now generic; every study (including Spanish) lives under `<study>/`.
- The in-repo Spanish SRS deck ships intentionally **empty** — a learner's real deck lives in their
  private learner data directory (`docs/LEARNER-DATA-SPEC.md`), not in the engine repo. The CLI shows
  0 cards / no sessions for Spanish until a learner adds their own. This is the clean-engine state,
  not a regression.
- Spanish keeps two minor internal variations from the spec (`language-reference/` instead of
  `reference/`; `scenarios/<name>/scenario.md`). Normalizing them is deliberately out of scope — a
  separate content migration, not part of the structural move.
