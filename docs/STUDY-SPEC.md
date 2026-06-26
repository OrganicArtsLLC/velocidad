# Velocidad Study Specification

**Version:** 2.0.0
**Status:** Active
**License:** GPL-3.0-or-later (this document is engine metadata)

> **v2.0 rename:** what earlier versions called a *domain* is now a **study**, and the contexts
> inside it (earlier "worlds") are now uniformly **scenarios**. One vocabulary across every study.
> See `meta/system-changelog.md` for the migration.

---

## What Is a Study?

A **study** is a named, self-contained learning subject that plugs into the Velocidad engine.

The engine provides the **methodology**: the Deploy → Capture → Distill → Drill → Redeploy
flywheel, the 4-box Leitner SRS system, the friction-log format, and the agent prompts. A study
provides the **content**: the scenarios, the reference material, and the contextual vocabulary for
one subject area.

Velocidad is built to host an **open-ended number of studies**, each pursued in coordination with
real work and real stakes. The studies in this repo:

| Study | Status | What it builds |
|-------|--------|----------------|
| **Spanish** | First / reference study (`spanish/`) | Conversational Spanish with the real people in daily life |
| **Philosophy** | Planned (`philosophy/`) | Rhetoric, argument, and the positions of the great thinkers — argued aloud, under pressure |
| **Distributed Systems** | Planned (`distributed-systems/`) | Professional/technical fluency — system design, architecture, and the language of the field, performed under pressure |

**Spanish is the reference implementation.** Every pattern in this spec is demonstrated live in the
`spanish/` study (`spanish/scenarios/`, `spanish/language-reference/`, `spanish/chunks/`,
`spanish/patterns/`). Any directory that satisfies this spec is a valid Velocidad study.

### Terminology (one vocabulary, all studies)

- **Study** — a top-level subject (Spanish, Philosophy, Distributed Systems). "Track" is an
  accepted loose synonym in prose.
- **Scenario** — a deployment context inside a study: the real situation you practice under
  pressure, defined by an L1–L5 ladder (`docs/SCENARIO-LADDER-TEMPLATE.md`).
- **Chunk** — a minimal production unit you must be able to say/write under pressure.
- **Pattern** — a fill-in-the-blank template that lets you improvise once internalized.
- **Friction** — what broke under pressure; the only source of the curriculum.

---

## Required Study Structure

```
{study_name}/
├── study-config.md           # Study metadata and agent behavior rules
├── scenarios/                # Deployment contexts (L1–L5 ladders)
│   ├── scenario-01.md        # One file per real-world deployment context
│   ├── scenario-02.md
│   └── ...
├── reference/                # Study reference library (the "how it works" material)
│   └── *.md                  # Topic-organized reference files
├── chunks/
│   └── reference.md          # Production chunks (vocabulary, phrases, formulas)
└── patterns/
    └── reference.md          # Sentence / output templates for this study
```

> **Note on the reference study's layout.** The Spanish study lives in `spanish/`, a structural peer of
> any other study. It keeps two minor internal variations from this spec for historical reasons:
> `spanish/language-reference/` instead of `reference/`, and `spanish/scenarios/<name>/scenario.md`
> (a folder per scenario rather than a flat file). New studies (`philosophy/`, `distributed-systems/`)
> should follow the structure above. (Spanish moved out of the repo root in 2026-06; see
> `docs/adr/0003-spanish-study-relocation.md`.)

---

## File Specifications

### `study-config.md`

The control file for the agent. It carries the study-specific context and behavior rules that the
generic engine prompts don't know about.

```markdown
# Study: [Name]

## Description
[One sentence: what skill this study builds and why production pressure matters here.]

## Deployment Contexts
[The real-world situations where you can practice this study under actual stakes.]
- Context 1: ...
- Context 2: ...

## Production Pressure Notes
[What makes performing in this study hard? What is the "speaking without a script" equivalent?]

## Immersion Rules (study-specific, extends config/rules-of-immersion.md)
[Add to or override the base immersion rules for this study.]
1. ...

## Friction Types (study-specific, extends the base 5)
[Friction categories specific to this study beyond the base five.]
- [Friction type]: [Description]

## Success Metrics
[What does L1→L5 progress feel like here? What's the observable evidence?]

## Notes for Agent
[Study-specific guidance for the AI playing partner / NPC / evaluator.]
```

### `scenarios/scenario-XX.md`

One file per deployment scenario, using the L1–L5 ladder in `docs/SCENARIO-LADDER-TEMPLATE.md`.
Each describes a real context where you can practice under actual pressure.

A study should have at minimum 2–3 scenarios. The Spanish reference study has 4 (mcdonalds, casa,
vecinos, errands).

### `reference/*.md`

Organized, learnable content for systematic study — the equivalent of `language-reference/` for
Spanish. Organize by topic, not by difficulty. The agent uses these opportunistically: when session
friction points to a gap, it pulls the relevant reference file.

Examples of reference organization:
- Spanish: `verbs-core-20.md`, `connectors.md`, `repair-phrases.md`
- Distributed Systems: `data-architecture-terms.md`, `api-design-patterns.md`
- Philosophy: `stoics-marcus-seneca.md`, `classical-plato-aristotle.md`, `rhetoric-toolkit.md`

**License note:** reference content you create is your original educational work — use CC BY-SA 4.0
if you publish it. Do not include copyrighted third-party content; summarize or cite instead.

### `chunks/reference.md`

Production chunks are the minimal units you must produce under pressure. Not vocabulary lists —
things you can actually say in a realistic scenario.

Format: `chunk in target form — English translation / description`

- Spanish: `¿Me lo puede repetir? — Can you repeat that?`
- Distributed Systems: `the tradeoff here is X for Y — naming a design decision`
- Philosophy: `to steelman your position — restating an opponent's argument at its strongest`

### `patterns/reference.md`

Output templates — fill-in-the-blank scaffolds that let you improvise once you own the pattern.

Format: `[Template] — [Description] — [Example]`

- Spanish: `[Subject] + quiero + [infinitive] — wanting/ordering — Quiero un café`
- Distributed Systems: `[Component] exposes a [type] endpoint that accepts [input] and returns [output]`
- Philosophy: `[Thinker] holds that [claim] because [warrant]; the strongest objection is [counter]`

---

## Optional Study Structure

```
{study_name}/
├── srs/                      # Study-specific SRS boxes
│   ├── box1.md … box4.md
├── sessions/                 # Study session archive
│   ├── TEMPLATE.md
│   └── YYYY-MM-DD/ { plan.md, transcript.md, friction.json, debrief.md }
└── meta/
    └── study-architecture.md # How this study's content system is organized
```

SRS boxes and the session archive can live in the learner data directory (see
`docs/LEARNER-DATA-SPEC.md`) rather than in the study definition. This keeps the study definition
static while the learner's progress accumulates in their private repo. Recommended: keep study
definition files (scenarios, reference, chunks, patterns) in the engine/study repo; keep SRS cards
and session records in the private learner data directory.

---

## Registering a Study in `paths.yaml`

```yaml
studies:
  - name: spanish
    display: "🇪🇸 Spanish"
    path: "./spanish"               # the Spanish reference study
  - name: philosophy
    display: "🏛️ Philosophy"
    path: "./philosophy"
  - name: your-study
    display: "📚 Your Study"
    path: "../your-private-repo/your-study-data"
```

The dashboard and agent prompts use this configuration to locate study content.

---

## Study Quality Checklist

Before considering a study "ready to use":

- [ ] `study-config.md` complete with all required fields
- [ ] At least 2 scenarios at L1–L3 in `scenarios/`
- [ ] At least one reference file in `reference/`
- [ ] At least 20 production chunks in `chunks/reference.md`
- [ ] At least 10 sentence patterns in `patterns/reference.md`
- [ ] Registered in `config/paths.yaml`
- [ ] Runs successfully with the master prompt (agent can complete a session)

The study is useful before it is complete. Start with one scenario at L1 and expand.

---

## Publishing a Study (if sharing with others)

1. Ensure all content is original or properly licensed for redistribution
2. Set the license: methodology (study config + scenario structure) → GPL-3.0-or-later;
   original educational reference content → CC BY-SA 4.0
3. Write `study-config.md` with no personal/employer-specific context
4. Anonymize scenario files — replace specific contacts with archetypes ("coworker," "client")
5. Provide a blank `chunks/reference.md` template or a starter set of universal chunks
6. Publish as a standalone directory or as a PR to a community study registry

---

## See Also

- `docs/KNOWLEDGE-ENGINE-OVERVIEW.md` — what this engine is and how it works
- `docs/SCENARIO-LADDER-TEMPLATE.md` — L1–L5 scaffold for building scenarios
- `docs/TECHNICAL-TRACK.md` — worked guide: building a professional/technical study
- `docs/LEARNER-DATA-SPEC.md` — the private learner data contract (sessions, SRS, profile)

---

*Last Updated: June 2026*
