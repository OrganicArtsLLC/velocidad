# System Changelog

How the Velocidad system itself evolves. Every adjustment to methodology, prompts, or structure gets logged here.

The system is recursive: it learns how you learn, and then it changes to learn better.

---

## v0.1.0 — February 19, 2026

- Initial system design
- 5-Part Daily Engine defined
- Real-world deployment targets identified
- Language architecture map created
- Meta-observation layer added
- Worlds based on the learner's actual people and places

## v0.3.0 — April 2, 2026

**Technical track: SRS expansion to 41 cards**

- Grew `technical/srs/box1.md` from 13 → 41 cards across all 4 domains
- AI Tooling (+7): RAG, temperature, tool use / function calling, system vs user prompt, embeddings, escape route pattern, chain of thought
- Software Engineering (+7): leaky abstraction, side effects, magic numbers, defensive copy, coupling vs cohesion, idempotent HTTP, optimistic vs pessimistic locking
- DevOps & Platform (+7): artifact contract, gate definition, environment-as-context, IaC + drift elimination, blue-green deployment, blast radius, Three Ways
- Python & Data (+7): pure functions, dependency injection, context managers, generator vs list, enumerate, pathlib, exception hierarchy
- All 41 cards verified parseable by dashboard parser

## v0.2.0 — March/April 2026

**Technical track added + interactive dashboard**

- Built full `technical/` parallel learning engine:
  - 4 domain scenario ladders (ai-tooling, devops-platform, python-data, software-engineering)
  - SRS boxes with Leitner format (technical flavor: `**Key:** value`)
  - Technical chunk bank (53 items) and pattern bank (16 patterns)
  - Session template and prompt set (master, distiller, srs-generator, meta-observer)
  - Seeded 13 initial SRS cards across all 4 domains
- Ingested a 92-document technical library from a private source directory:
  - `technical/library/foundations/` — 60 foundational SE/DevOps/Systems docs
  - `technical/library/ai-ml/` — 19 AI/ML reference docs
  - `technical/library/books/` — 13 key texts (DDIA, DevOps Handbook, SICP, etc.)
  - `technical/library/INDEX.md` — 92-doc catalog with author, year, domain tags, priority ratings, reading paths, re-acquisition notes
  - Source directory emptied after ingestion; `.gitignore` excludes binaries; INDEX.md is the permanent record
- Built `dashboard.py` — 943-line interactive terminal UI using `rich`:
  - SRS review for both Spanish and Technical tracks with grading + auto-promotion between box files
  - Library browser (92 docs, reading paths, opens PDFs in system viewer via `open`)
  - Chunk and pattern browsers for both tracks
  - Session launcher
  - Verified parsers: Spanish SRS 35, Technical SRS 41, Spanish chunks 319, Technical chunks 53, Spanish patterns 30, Technical patterns 16, Library docs 92, Worlds 5
- Added `start-dashboard.sh` launcher and `requirements.txt`

## Adjustments Log

<!--
Format:
- [date] WHAT changed → WHY → RESULT (if known)

Example:
- [2026-02-25] Increased drill reps from 10 to 15 → friction log showed patterns not sticking in single session → TBD
- [2026-03-01] Added "house workers" scenario to weekly rotation → real deployment opportunity arose → immediate improvement in directional vocabulary
-->
