# Velocidad-AI: Design Document

The distilled architecture from concept to implementation.

---

## Vision

### The Core Hypothesis

Speed to conversational Spanish comes from **production pressure**, not comprehension study.

$$\text{Fluency} = \text{Retrieval under pressure} + \text{Pattern recognition} + \text{Motor memory}$$

### Why This Exists

Traditional language learning is backwards. It teaches grammar before speaking, breadth before depth, and recognition before production. Duolingo gamifies the wrong loop: you tap correct answers instead of producing speech under pressure.

Velocidad inverts the model: **speak first, fail, log the failure, drill exactly what broke, speak again.**

### The Anti-Duolingo Philosophy

| What fails | What works |
|---|---|
| Passive consumption (reading lessons) | Active production (speak first) |
| Perfectionism (grammar before speaking) | Useful imperfection (repair phrases) |
| Broad but shallow (1000 random words) | Narrow but deep (100 phrases, 1 context) |
| Delayed production (study then speak) | Immediate production (speak, fail, log, drill) |
| Gamification (streaks, points) | Real-world stakes (actual ordering) |
| Teacher-led curriculum | Friction-driven curriculum |

### What Success Looks Like

- **Week 1-2:** Awkward, lots of friction, but patterns emerging
- **Week 3-4:** Your core scenario becomes comfortable
- **Week 5-8:** Scenarios stack, repair phrases automatic
- **Week 12:** Conversationally operational (not perfect, but useful)

---

## Architecture

### The Flywheel (Core Engine)

The entire system is one closed loop:

```
Deploy → Capture → Distill → Rehearse → Redeploy
   ↑                                        |
   └────────────────────────────────────────┘
```

**Deploy:** Speak in a scenario (roleplay or real world)
**Capture:** Log what broke (friction log)
**Distill:** AI converts friction into targeted drills
**Rehearse:** Drill exactly what failed + spaced repetition
**Redeploy:** Same scenario, one rung harder

Bedrock is a **byproduct** of interaction, not a prerequisite.

### The 5-Part Daily Engine (25-30 min)

This never changes shape. It only increases depth.

1. **Speak First** (5-7 min) — Roleplay scenario, Spanish only, no prep
2. **Extract Friction** (3 min) — Log: couldn't say, hesitated, didn't understand, felt awkward
3. **Targeted Micro-Drills** (7-10 min) — 10 production reps, 5 repair reps, 5 variation reps
4. **Shadowing** (5 min) — 30-60 sec native audio, listen once, shadow 3x
5. **Micro-Deploy** (optional) — One real interaction, even 20 seconds

### The Agent Services (Deliberately Minimal)

Six prompts cover the full loop. Most days you only need the master prompt.

| Prompt | Purpose |
|---|---|
| `master.md` | All-in-one daily engine (session + distill + drill + plan) |
| `session-runner.md` | Roleplay-only mode |
| `distiller.md` | Extract friction, chunks, patterns from a transcript |
| `srs-generator.md` | Generate spaced-repetition cards from failures |
| `session-planner.md` | Plan tomorrow's session + micro-deploy mission |
| `meta-observer.md` | Weekly recursive system review |

What we **don't** build: dashboards, progress trees, gamification, curriculum planning tools, elaborate tracking.

### Depth-First Progression Model

One main scenario per week, deep. Light maintenance of previous scenarios.

```
Week 1: McDonald's scenario  (order, clarify, small talk, pay, handle mistakes)
Week 2: Errands scenario     (find items, ask help, checkout) + mcdonalds maintenance
Week 3: Vecinos scenario     (greetings, weather, plans) + previous maintenance
Week 4+: Scenarios stack     (patterns compound across contexts)
```

Key: each week goes DEEP on one scenario. Breadth comes from compounding, not scattering.

### Hansuru Tier System (Exposure Control)

Borrowed from the Hansuru risk management framework:

- **Tier 1 — Daily Engine** (non-negotiable): Chunk drills, shadowing, call-response. Even on bad days.
- **Tier 2 — Insurance Layer**: Repair phrases, freeze recovery, pronunciation fixes. Makes Tier 3 survivable.
- **Tier 3 — Controlled Deployment**: Real conversations under constraint. Timeboxed, topic-bounded, scripted entry + exit. Optional daily, mandatory weekly.
- **Tier 4 — Immersion Spike**: 2-4 hour Spanish-only blocks. Scheduled, not impulsive. Permanently raises baseline.

### Deployment Test Harness

Speaking is your production environment. You need staging.

| Stage | Environment |
|---|---|
| Dev | Speaking alone, reading aloud, drill prompts |
| Staging | AI roleplay, scripted conversations, voice notes |
| Production | Real humans in the wild |

Before Tier 3 deployment: entry line ready, fallback line ready, exit line ready, topic bounded, success defined.

---

## Ideas

The powerful concepts that differentiate this from any language app.

### 1. Friction-Driven Curriculum

Your curriculum is not a textbook. It is **your actual gaps**. Every session produces:
- What you wanted to say but couldn't
- What you heard but didn't understand
- What you avoided
- What broke 3+ times

Those become tomorrow's Tier 1 drills. The system evolves around YOUR specific weaknesses.

### 2. The Hidden Accelerator (30-Second Daily Story)

Record yourself describing something in Spanish (30 seconds). Agent corrects. Re-record corrected version. That's it.

Why it's powerful: self-expression (not scripted), error correction loop, compounding fluency, personal stories create emotional salience.

### 3. Pattern Genome

Language taught as combinatorics, not vocabulary. Build a pattern tree:

```
Intent → Action → Object → Modifier → Social softener
```

Master "Quiero..." then systematically expand: quiero un cafe, quiero uno grande, quiero decir que..., quiero que me ayudes, quisiera...

One pattern generates dozens of usable sentences.

### 4. Volatility Harvesting for Language

Deliberately introduce stress in waves to prevent overfitting to clean practice:
- Week 1: stable scripted cafe
- Week 2: speed increase
- Week 3: slang + interruptions
- Week 4: random topic shifts

Embarrassment = signal. Mistakes = volatility harvest. This is antifragile fluency.

### 5. Digital Twin (Learner Telemetry)

The agent builds a live model of your linguistic system:
- Pattern mastery levels
- Verbs you overuse vs. avoid
- Missing connectors
- Average sentence length trend
- Repair usage rate
- Stress-induced regression points

The twin predicts what will break next. That's not magic; it's telemetry.

### 6. Narrative Binding

Instead of random sessions, the agent builds a continuous story:
- Day 1: you arrive in a Spanish-speaking town
- Day 2: visit the cafe
- Day 3: meet a neighbor
- Day 4: buy groceries
- Day 5: plan a run

Same vocabulary reused across different emotional contexts. Memory loves story.

### 7. Semantic Field Saturation

Instead of scattered words, saturate one field completely: heat, taste, preference, payment, size, time, politeness (all within "coffee"). The brain stores connected clusters better than isolated words.

### 8. Compression & Expansion Cycles

Alternate between:
- **Compression days:** say the same idea with fewer words
- **Expansion days:** add detail, nuance, connectors

This builds control and range.

### 9. Retrieval Pressure Optimization

Always speak BEFORE seeing the answer. The struggle is the point. If hesitation > 3 seconds, log it. The agent dynamically balances comfort and stretch.

### 10. Conversation Moves (Not Just Words)

Teach "moves" that make you feel fluent:
- Ask a follow-up
- Clarify what you heard
- Show interest
- Soften a request
- Exit politely

These are what separate "knows words" from "can converse."

---

## Implementation

### MVP Scope (Build This First)

**Four scenarios (in `spanish/scenarios/`):**
- `spanish/scenarios/mcdonalds/` — the safe lab
- `spanish/scenarios/casa/` — house workers
- `spanish/scenarios/vecinos/` — neighbors
- `spanish/scenarios/errands/` — daily errands

**1 shared system:**
- friction log → SRS generation → next session drills

**Six agent prompts:**
1. Session Runner (roleplay)
2. Distiller (friction extraction)
3. SRS Generator (card creation)
4. Session Planner (tomorrow's plan)
5. Meta-Observer (weekly system review)
6. Master prompt that chains the daily loop

### Technical Stack Decisions Needed

| Decision | Options | Lean |
|---|---|---|
| Runtime | Python CLI, plain markdown, or web app | Plain markdown + agent mode prompts |
| Voice vs. text | Text-only, voice input, or both | Text first (speak aloud, type responses) |
| Friction logging | Manual markdown, structured JSON, or both | Markdown with JSON friction files |
| SRS engine | Markdown boxes (box1-4), Anki export, or custom | Markdown boxes (transparent, editable) |
| Shadowing sources | Manual curation, YouTube links, TTS | TTS + curated links |
| Agent model split | All Sonnet, or Sonnet daily + Opus weekly | Sonnet 4.5 daily, Opus weekly refactor |

### Repo Structure (MVP)

```
velocidad/
├── readme.md
├── docs/
│   └── design.md                    # This document
├── config/
│   ├── learner-profile-template.yaml  # Profile schema to copy into your data dir
│   ├── paths.yaml.template          # Points the engine at your private data dir
│   └── rules-of-immersion.md        # Agent behavior constraints
└── spanish/                         # The Spanish study (first / reference study)
    ├── scenarios/
    │   ├── mcdonalds/scenario.md    # Ladder + NPC lines
    │   ├── casa/scenario.md
    │   ├── vecinos/scenario.md
    │   └── errands/scenario.md
    ├── sessions/
    │   └── TEMPLATE.md              # Session folder structure (lives in learner data dir)
    ├── srs/
    │   ├── box1.md                  # Review today
    │   ├── box2.md                  # Review in 2 days
    │   ├── box3.md                  # Review in 7 days
    │   └── box4.md                  # Review in 21 days
    ├── chunks/
    │   └── reference.md             # Universal phrase reference
    ├── patterns/
    │   └── reference.md             # Universal sentence templates
    └── prompts/
        ├── master.md                # All-in-one daily prompt
        ├── session-runner.md        # Roleplay prompt
        ├── distiller.md             # Friction extraction prompt
        ├── srs-generator.md         # Card generation prompt
        ├── session-planner.md       # Tomorrow planner prompt
        └── meta-observer.md         # Weekly system review prompt
```

Personal sessions, SRS state, and profile live in a separate private learner-data directory
(see `docs/LEARNER-DATA-SPEC.md`), not in the engine repo.

### What to Build, In Order

1. **Config files** — learner profile + immersion rules
2. **First scenario (mcdonalds)** — scenario ladder with NPC lines
3. **Prompts** — the daily loop prompts + master prompt
4. **Session template** — empty session folder structure
5. **SRS skeleton** — empty box files with instructions
6. **Chunk + pattern banks** — empty with starter entries
7. **Run the first session** — immediately, Day 1

### The Operating Principle

You don't wait to be ready. You deploy under guardrails. You log friction. You reinforce bedrock precisely where it cracks.

---

*Last Updated: April 10, 2026*
