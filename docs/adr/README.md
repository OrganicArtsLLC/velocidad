# Architecture Decision Records

This directory holds the load-bearing decisions behind the Velocidad **engine** — the "why" you need
to improve the core without re-deriving it. Format is lightweight [Nygard-style](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions):
each record has **Status / Context / Decision / Consequences**, is numbered `NNNN-title.md`, and is
append-only (supersede, don't rewrite history).

| # | Title | Status |
|---|-------|--------|
| [0001](0001-record-architecture-decisions.md) | Record architecture decisions | Accepted |
| [0002](0002-study-plugin-architecture.md) | Studies are directory plugins on a generic engine | Accepted |
| [0003](0003-spanish-study-relocation.md) | Move the Spanish study out of the repo root into `spanish/` | Accepted |
| [0005](0005-learning-science-layer.md) | A learning-science layer on top of the Leitner core | Accepted |

> Number 0004 is intentionally skipped: it recorded an internal build/release process that does not
> apply to this independently-maintained public repo.

> For the *what* and *how* (the study contract, file formats, the flywheel), see `docs/STUDY-SPEC.md`,
> `docs/KNOWLEDGE-ENGINE-OVERVIEW.md`, and the running log in `meta/system-changelog.md`. ADRs capture
> the *why* behind the structural choices those docs assume.
