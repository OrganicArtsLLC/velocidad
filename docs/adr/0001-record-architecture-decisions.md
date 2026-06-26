# 0001 — Record architecture decisions

**Status:** Accepted · 2026-06-05

## Context

Velocidad is a markdown-first learning engine with a small Python CLI and Rich dashboard, no test
suite, and a deliberately low-ceremony codebase. Its load-bearing decisions (why the engine is
study-agnostic, why personal data is kept out of the engine repo) lived only in code comments,
`README`, and `meta/system-changelog.md`. As the engine grew to host multiple studies, "why is it
shaped this way?" got expensive to answer, and the risk of a well-meaning change breaking an
unstated invariant rose.

## Decision

Keep Architecture Decision Records in `docs/adr/`, Nygard-style (**Status / Context / Decision /
Consequences**), numbered `NNNN-title.md`, append-only. Record decisions that constrain the *structure*
of the engine — not routine feature work. `meta/system-changelog.md` remains the chronological "what
changed" log; ADRs are the durable "why it's allowed to be this way."

## Consequences

- A new contributor (human or agent) can read `docs/adr/` and understand the core's invariants before
  editing.
- Small overhead per structural decision; none for ordinary content/feature changes.
- Supersession is explicit: a later ADR marks an earlier one `Superseded`, preserving the trail.
