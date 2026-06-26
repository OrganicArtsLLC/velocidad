# Velocidad Domain Specification

**Version:** 1.0.0
**Status:** Active
**License:** GPL-3.0-or-later (this document is engine metadata)

---

## What Is a Domain?

A **domain** is a named learning environment that plugs into the Velocidad engine.

The engine provides the methodology: the Deploy → Capture → Distill → Drill → Redeploy flywheel,
the 4-box Leitner SRS system, the friction log format, and the six agent prompts. A domain provides
the content: the scenarios, the reference material, and the contextual vocabulary for a specific
subject area.

**The Spanish track is the reference domain implementation.** Every pattern described in this spec
is demonstrated live in the `worlds/`, `language-reference/`, `chunks/`, and `patterns/` directories
of this repository.

Any directory that satisfies this spec is a valid Velocidad domain.

---

## Required Domain Structure

```
{domain_name}/
├── domain-config.md          # Domain metadata and agent behavior rules
├── scenarios/                # Deployment contexts (equiv. to worlds/)
│   ├── SCENARIO-01.md        # One scenario per real-world deployment context
│   ├── SCENARIO-02.md
│   └── ...
├── reference/                # Domain reference library (equiv. to language-reference/)
│   └── *.md                  # Topic-organized reference files
├── chunks/
│   └── bank.md               # Production chunks (vocabulary, phrases, formulas)
└── patterns/
    └── bank.md               # Sentence/output templates for this domain
```

---

## File Specifications

### `domain-config.md`

This is the control file for the agent. It replaces the learner profile's world-specific context
and the `config/rules-of-immersion.md` overrides.

```markdown
# Domain: [Name]

## Description
[One sentence: what skill this domain builds and why production pressure matters here.]

## Deployment Contexts
[List the real-world situations where you can practice this domain under actual stakes.]
- Context 1: ...
- Context 2: ...

## Production Pressure Notes
[What makes performing in this domain hard? What is the "speaking without a script" equivalent?]

## Immersion Rules (domain-specific, extends base rules-of-immersion)
[Add to or override the base rules from config/rules-of-immersion.md for this domain.]
1. ...
2. ...

## Friction Types (domain-specific, extends base 5)
[Add friction categories specific to this domain beyond the base five.]
- [Friction type]: [Description]

## Success Metrics
[What does L1→L5 progress feel like in this domain? What's the observable evidence?]

## Notes for Agent
[Any domain-specific guidance for the AI agent running partner/NPC/evaluator role.]
```

### `scenarios/SCENARIO-XX.md`

One file per deployment scenario. Uses the L1-L5 ladder structure defined in
`docs/WORLD-LADDER-TEMPLATE.md`. Each scenario describes a real context where you can
practice this domain under actual pressure.

A domain should have at minimum 2-3 scenarios. The Spanish reference implementation has 5
(mcdonalds, casa, vecinos, familia, errands).

### `reference/*.md`

Domain reference files are the equivalent of `language-reference/` for Spanish. They contain
organized, learnable content for systematic study.

Organize reference files by topic, not by difficulty. The agent uses them opportunistically —
when friction from a session points to a gap, the agent references the appropriate file.

Examples of reference organization:
- Spanish: `verbs-core-20.md`, `connectors.md`, `repair-phrases.md`
- Music theory: `intervals.md`, `chord-types.md`, `rhythm-patterns.md`
- Technical vocabulary: `data-architecture-terms.md`, `api-design-patterns.md`

**License note:** Reference content you create is your original educational work. Use CC BY-SA 4.0
if you publish it. Do not include copyrighted third-party content — summarize or cite instead.

### `chunks/bank.md`

Production chunks are the minimal units you need to produce under pressure. Not vocabulary lists —
these are things you can say in a realistic deployment scenario.

Format: `chunk in target form — English translation / description`

Examples:
- Spanish: `¿Me lo puede repetir? — Can you repeat that?`
- Music theory: `The I → IV → V → I progression — basic cadence formula`

### `patterns/bank.md`

Sentence/output templates showing the structural patterns of the domain. These are fill-in-the-blank
scaffolds that let you improvise once you have the pattern.

Format: `[Template] — [Description] — [Example]`

Examples:
- Spanish: `[Subject] + quiero + [infinitive] — wanting/ordering — Quiero un café`
- Technical: `[Component] exposes a [type] endpoint that accepts [input] and returns [output]`

---

## Optional Domain Structure

```
{domain_name}/
├── srs/                      # Domain-specific SRS boxes
│   ├── box1.md
│   ├── box2.md
│   ├── box3.md
│   └── box4.md
├── sessions/                 # Domain session archive
│   ├── TEMPLATE.md
│   └── YYYY-MM-DD/
│       ├── plan.md
│       ├── transcript.md
│       ├── friction.json
│       └── debrief.md
└── meta/
    └── domain-architecture.md  # How this domain's content system is organized
```

The SRS boxes and session archive can live in the learner data directory (see
`docs/LEARNER-DATA-SPEC.md`) rather than in the domain definition. This allows the domain
definition to remain static while the learner's progress accumulates in their private repo.
Recommended: keep domain definition files (scenarios, reference, chunks, patterns) in the
engine/domain repo; keep SRS cards and session records in the private learner data directory.

---

## Domain Configuration in `paths.yaml`

When you implement a domain, register it in `config/paths.yaml`:

```yaml
domains:
  - name: spanish
    display: "🇪🇸 Spanish"
    path: "."               # This repo IS the Spanish domain reference implementation
  - name: your-domain
    display: "📚 Your Domain"
    path: "../your-private-repo/your-domain-data"
```

The dashboard and agent prompts use this configuration to locate domain content.

---

## Domain Quality Checklist

Before considering a domain "ready to use":

- [ ] `domain-config.md` complete with all required fields
- [ ] At least 2 scenarios at L1-L3 in `scenarios/`
- [ ] At least one reference file in `reference/`
- [ ] At least 20 production chunks in `chunks/bank.md`
- [ ] At least 10 sentence patterns in `patterns/bank.md`
- [ ] Registered in `config/paths.yaml`
- [ ] Runs successfully with `prompts/master.md` (agent can complete a session)

The domain is useful before it is complete. Start with one scenario at L1 and expand.

---

## Domain Publishing (if sharing with others)

If you want to publish your domain for others to use:

1. Ensure all content is original or properly licensed for redistribution
2. Set the appropriate license:
   - Domain config + scenario structure (methodology): GPL-3.0-or-later
   - Educational reference content (your original material): CC BY-SA 4.0
3. Write `domain-config.md` with no personal/employer-specific context
4. Anonymize scenario files — replace your specific contacts with archetypes ("coworker," "client")
5. Create a blank `chunks/bank.md` template or a starter set of universal chunks
6. Publish as a standalone directory or as a PR to a community domain registry

---

## See Also

- `docs/KNOWLEDGE-ENGINE-OVERVIEW.md` — What this engine is and how it works
- `docs/WORLD-LADDER-TEMPLATE.md` — L1-L5 scaffold template for building scenarios
- `docs/TECHNICAL-TRACK.md` — Example: how to adapt this engine for professional/technical domains
- `docs/LEARNER-DATA-SPEC.md` — The private learner data contract (sessions, SRS, profile)

---

*Last Updated: April 10, 2026*
