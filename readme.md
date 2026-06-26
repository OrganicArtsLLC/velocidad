# Velocidad-AI

[![License](https://img.shields.io/badge/license-CONTENT--LICENSE-blue)](CONTENT-LICENSE)
[![Author](https://img.shields.io/badge/by-Joshua%20Ayson-black)](https://joshuaayson.com/projects/)

**An antifragile learning engine powered by agent mode — starting with Spanish fluency.**

Speak first. Fail. Log what broke. Drill the friction. Speak again.

---

## Core Hypothesis

Speed to conversational Spanish comes from **production pressure**, not comprehension study.

> Fluency = Retrieval under pressure + Pattern recognition + Motor memory

The same flywheel generalizes: Spanish is the **first study**, not the whole product. See
[Beyond Spanish](#beyond-spanish).

## How It Works

### The 5-Part Daily Engine (25-30 min)

1. **Speak First** (5-7 min) — Roleplay scenario, Spanish only, no prep
2. **Extract Friction** (3 min) — Log what you couldn't say, hesitated on, didn't understand
3. **Targeted Micro-Drills** (7-10 min) — 10 production + 5 repair + 5 variation reps
4. **Shadowing** (5 min) — Native audio: listen once, shadow 3x
5. **Micro-Deploy** (optional) — One real interaction, even 20 seconds

### The Flywheel

```
Deploy → Capture → Distill → Rehearse → Redeploy
```

Bedrock is a byproduct of interaction, not a prerequisite.

### Depth-First Progression

- **Week 1:** McDonald's scenario (order, clarify, small talk, pay) — the safe lab
- **Week 2:** Errands scenario (find items, ask for help, checkout)
- **Week 3:** Vecinos scenario (greetings, weather, plans, small talk with neighbors)

Each week goes deep on one scenario. Patterns compound across contexts.

## Agent Services

| Service | Prompt | Purpose |
|---|---|---|
| **Master** | `spanish/prompts/master.md` | All-in-one daily engine (session + distill + drill + plan) |
| **Session Runner** | `spanish/prompts/session-runner.md` | Roleplay-only mode with NPC characters |
| **Distiller** | `spanish/prompts/distiller.md` | Extract friction, chunks, patterns from transcripts |
| **SRS Generator** | `spanish/prompts/srs-generator.md` | Create spaced repetition cards from failures |
| **Session Planner** | `spanish/prompts/session-planner.md` | Plan tomorrow's session + micro-deploy mission |
| **Meta-Observer** | `spanish/prompts/meta-observer.md` | Weekly system review — how the learner learns, what to adjust |

What we **don't** build: dashboards, gamification, progress trees, curriculum planners.

## The Living Library

The `spanish/language-reference/` directory is a self-contained Spanish learning compendium — useful to agent mode learners running sessions AND to anyone browsing the repo who wants a solid reference.

**Four sections, one library:**

| Section | Files | What you get |
|---------|-------|--------------|
| **System** | 00-05 | How Spanish works: sounds, gender, pronouns, verbs, sentence structure |
| **Reference** | 06-10 | Look things up: 1,000 words, cognate rules, verb tables, numbers, prepositions |
| **Methods** | 11-14 | How to learn: 18 acquisition methods, 200 cloze exercises, 165+ keyword mnemonics, AI reverse engineering |
| **Field Guides** | FIELD-MANUAL + others | Deploy in the real world: tactical reference, German bridges, priority order |

**Highlights:**
- **[Core Vocabulary](spanish/language-reference/06-core-vocabulary.md)** — 1,000 words in 4 frequency bands with example sentences
- **[Cognate Accelerator](spanish/language-reference/07-cognate-accelerator.md)** — 18 suffix rules that unlock 3,000+ words from English
- **[Rapid Acquisition Methods](spanish/language-reference/11-rapid-acquisition-methods.md)** — Every proven technique from Output Hypothesis to Memory Palace
- **[Cloze Exercises](spanish/language-reference/12-cloze-method.md)** — 200 fill-in-the-blank exercises across 6 skill tiers
- **[Mnemonic Dictionary](spanish/language-reference/13-mnemonic-dictionary.md)** — Vivid keyword images for words that won't stick
- **[AI Reverse Engineering Handbook](spanish/language-reference/14-ai-reverse-engineering-handbook.md)** — The meta of the meta: 7-layer stack, interference maps, error archaeology, compression theory, 7 novel AI techniques

Browse the full index: [spanish/language-reference/README.md](spanish/language-reference/README.md)

## Project Structure

The repo root is a generic **engine**; each **study** is a directory that plugs into it.
Spanish ships today as the reference study; Philosophy and Distributed Systems are on the way.

```
velocidad/
├── config/
│   ├── learner-profile-template.yaml  # Profile schema to copy into your data dir
│   ├── paths.yaml.template            # Points the engine at your private data dir
│   └── rules-of-immersion.md          # The rules the agent must follow
├── meta/
│   └── system-changelog.md            # How the engine itself evolves
├── velocidad                          # CLI launcher → ./velocidad <command>
├── scripts/
│   ├── velocidad.py                   # The engine CLI (SRS, daily review, stats, coach)
│   └── speak.py                       # Optional voice layer (drill/listen by ear)
├── docs/                              # Engine methodology + specs (see Documentation)
│   ├── KNOWLEDGE-ENGINE-OVERVIEW.md   # What this engine is + the production flywheel
│   ├── STUDY-SPEC.md                  # How to add a new study
│   ├── SCENARIO-LADDER-TEMPLATE.md    # Blank L1-L5 scenario scaffold
│   ├── LEARNER-DATA-SPEC.md           # Learner data directory contract
│   ├── LEARNING-SCIENCE.md            # The drill layer: what each tool does to memory
│   ├── USER-GUIDE.md                  # The operator's manual (a day / a week)
│   ├── TECHNICAL-TRACK.md             # Guide: building a professional/technical study
│   ├── design.md                      # Vision, architecture, implementation
│   └── adr/                           # Architecture decision records
├── spanish/                           # 🇪🇸 The Spanish study (first / reference study)
│   ├── scenarios/
│   │   ├── mcdonalds/scenario.md      # The safe lab — ordering, small talk
│   │   ├── casa/scenario.md           # House workers — directions, logistics
│   │   ├── vecinos/scenario.md        # Neighbors — real friendship
│   │   └── errands/scenario.md        # Local errands — daily deployment
│   ├── prompts/                       # 6 agent mode prompts (see table above)
│   ├── sessions/TEMPLATE.md           # Session folder structure
│   ├── srs/box1-4.md                  # 4-box Leitner SRS (blank template state)
│   ├── language-reference/            # 📚 The Living Library (see below)
│   ├── chunks/reference.md            # Universal phrase reference
│   ├── patterns/reference.md          # Universal sentence templates
│   └── meta/                          # language-architecture.md, memory-techniques.md
├── philosophy/                        # 🏛️ Philosophy study (coming)
└── distributed-systems/               # 💻 Distributed Systems study (coming)
```

> **Your personal sessions, SRS state, mastery tracking, and profile live in a separate
> private directory — see [Architecture](#architecture) below.**

## Quick Start

```bash
# 1. Copy the paths config template
cp config/paths.yaml.template config/paths.yaml

# 2. Edit config/paths.yaml — point learner_data_dir at your private data directory
#    Example: ../[your-private-repo]/velocidad
#    See docs/LEARNER-DATA-SPEC.md for what that directory needs to contain.

# 3. Run the engine (no dependencies — Python 3.10+ standard library only)
./velocidad start                 # morning routine: surfaces today's prompt + due cards
./velocidad status                # dashboard across all studies
./velocidad --help                # every command

# The CLI does the mechanical work (SRS review, session scaffolding, surfacing the
# master prompt). Agent mode does the learning: paste the prompt it shows you into
# Claude/GPT, tell it the scenario (e.g. "Today's scenario: mcdonalds"), and go.
```

You can also skip the CLI and paste `spanish/prompts/master.md` into the agent directly.

**First time?** `docs/USER-GUIDE.md` walks through a full day and week. `docs/LEARNER-DATA-SPEC.md` has the learner-data initialization checklist.

## Architecture

Velocidad-AI separates two concerns that most learning tools merge together:

**Engine (this repo — public)**  
The methodology, prompts, scenario ladders, and universal reference material. Stateless — contains no knowledge about you. Can be forked, improved, shared.

**Learner data (your private repo)**  
Your profile, your sessions, your SRS card state, your mastery tracking, your observations about how you learn. Grows with every session. Stays private. Implements the contract in `docs/LEARNER-DATA-SPEC.md`.

The coupling between them is intentional and minimal: `config/paths.yaml` (gitignored) tells the engine where your data lives. The prompts reference `{learner_data_dir}/profile.yaml` — a documented path you configure once.

```
velocidad/             ← engine (public)
  config/paths.yaml    ← gitignored, points at your data dir
  docs/LEARNER-DATA-SPEC.md  ← the contract
  spanish/prompts/     ← reads from {learner_data_dir}

[your-private-repo]/velocidad/  ← learner data (private, your repo)
  profile.yaml
  sessions/
  srs/
  progress/
  meta/learning-observations.md
```

See the [Learner Data Spec](docs/LEARNER-DATA-SPEC.md) for the full directory tree and file schemas.

---

## Beyond Spanish

The same engine generalizes to any **study** where skill is built under pressure — professional and
technical fluency, philosophy and discourse, public speaking, negotiation. The flywheel, SRS,
friction log, and L1-L5 ladder are study-agnostic; only the scenarios and reference content change.
Spanish is the reference study; **Philosophy** and **Distributed Systems** studies are coming.

- [`docs/KNOWLEDGE-ENGINE-OVERVIEW.md`](docs/KNOWLEDGE-ENGINE-OVERVIEW.md) — what the engine is and which studies fit
- [`docs/STUDY-SPEC.md`](docs/STUDY-SPEC.md) — how to build a new study that plugs into the engine
- [`docs/TECHNICAL-TRACK.md`](docs/TECHNICAL-TRACK.md) — worked guide for professional / technical studies

---

## Design Principles

- **Retrieval dominance** — Speak before seeing answers
- **Contextual repetition** — Same scenario, different angles
- **Emotional salience** — Real scenarios you'll actually use
- **Minimal cognitive overload** — 25-30 min, one scenario per week
- **Pattern compounding** — Week 1 patterns return in Week 2
- **Motor repetition** — Say it out loud; mouth muscle matters

## Documentation

- [Knowledge Engine Overview](docs/KNOWLEDGE-ENGINE-OVERVIEW.md) — What the engine is and how the flywheel works
- [User Guide](docs/USER-GUIDE.md) — The operator's manual: a day, a week, and what to do when something won't stick
- [Learning Science](docs/LEARNING-SCIENCE.md) — What each drill tool does to your memory
- [Language Reference Library](spanish/language-reference/README.md) — Complete index of all Spanish reference material with reading orders
- [Learner Data Spec](docs/LEARNER-DATA-SPEC.md) — The contract between engine and personal data directory
- [Study Spec](docs/STUDY-SPEC.md) — How to add a new study to the engine
- [Scenario Ladder Template](docs/SCENARIO-LADDER-TEMPLATE.md) — Blank L1-L5 scaffold for building scenarios
- [Design Document](docs/design.md) — Vision, architecture, ideas, implementation plan

---

## Fork This For Yourself

The methodology is universal. The data is yours.

**Step 1: Create your learner data directory**  
Anywhere in a private repo. Run through the initialization checklist in `docs/LEARNER-DATA-SPEC.md` — creates the directory tree, profile file, blank SRS boxes, and progress tracking files.

**Step 2: Configure the path**
```bash
cp config/paths.yaml.template config/paths.yaml
# Edit config/paths.yaml — set learner_data_dir to your directory path
```

**Step 3: Customize three things:**

1. **`profile.yaml`** — Your motivation, real deployment targets (the actual people you'll practice with), and learning tendencies. Be specific. This is what the agent reads to personalize every session.

2. **`spanish/scenarios/`** — The included scenarios reflect one person's life. Swap in yours. Each scenario is a markdown file with a 5-level ladder.

3. **`spanish/meta/language-architecture.md`** — The engine version is built for Spanish. If you're learning something else, start a new study (see `docs/STUDY-SPEC.md`) and write its architecture for that system.

**What you don't need to touch to get started:** prompts, session template, chunk/pattern reference files. All universal.

---

**Organization:** Organic Arts LLC  
**Engine License:** [GPL-3.0-or-later](LICENSE) — prompts, config, meta, methodology  
**Content License:** [CC BY-SA 4.0](CONTENT-LICENSE) — language-reference, scenarios, chunks, patterns, session templates  
**Status:** Active  
**Last Updated:** June 2026