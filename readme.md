# Velocidad-AI

[![License](https://img.shields.io/badge/license-CONTENT--LICENSE-blue)](CONTENT-LICENSE)
[![Author](https://img.shields.io/badge/by-Joshua%20Ayson-black)](https://joshuaayson.com/projects/)

**An antifragile Spanish fluency engine powered by agent mode.**

Speak first. Fail. Log what broke. Drill the friction. Speak again.

---

## Core Hypothesis

Speed to conversational Spanish comes from **production pressure**, not comprehension study.

> Fluency = Retrieval under pressure + Pattern recognition + Motor memory

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

- **Week 1:** McDonald's World (order, clarify, small talk, pay) — the safe lab
- **Week 2:** Errands World (find items, ask for help, checkout)
- **Week 3:** Vecinos World (greetings, weather, plans, small talk with neighbors)

Each week goes deep on one scenario. Patterns compound across contexts.

## Agent Services

| Service | Prompt | Purpose |
|---|---|---|
| **Master** | `prompts/master.md` | All-in-one daily engine (session + distill + drill + plan) |
| **Session Runner** | `prompts/session-runner.md` | Roleplay-only mode with NPC characters |
| **Distiller** | `prompts/distiller.md` | Extract friction, chunks, patterns from transcripts |
| **SRS Generator** | `prompts/srs-generator.md` | Create spaced repetition cards from failures |
| **Session Planner** | `prompts/session-planner.md` | Plan tomorrow's session + micro-deploy mission |
| **Meta-Observer** | `prompts/meta-observer.md` | Weekly system review — how the learner learns, what to adjust |

What we **don't** build: dashboards, gamification, progress trees, curriculum planners.

## The Living Library

The `language-reference/` directory is a self-contained Spanish learning compendium — useful to agent mode learners running sessions AND to anyone browsing the repo who wants a solid reference.

**Four sections, one library:**

| Section | Files | What you get |
|---------|-------|--------------|
| **System** | 00-05 | How Spanish works: sounds, gender, pronouns, verbs, sentence structure |
| **Reference** | 06-10 | Look things up: 1,000 words, cognate rules, verb tables, numbers, prepositions |
| **Methods** | 11-14 | How to learn: 18 acquisition methods, 200 cloze exercises, 165+ keyword mnemonics, AI reverse engineering |
| **Field Guides** | FIELD-MANUAL + others | Deploy in the real world: tactical reference, German bridges, priority order |

**Highlights:**
- **[Core Vocabulary](language-reference/06-core-vocabulary.md)** — 1,000 words in 4 frequency bands with example sentences
- **[Cognate Accelerator](language-reference/07-cognate-accelerator.md)** — 18 suffix rules that unlock 3,000+ words from English
- **[Rapid Acquisition Methods](language-reference/11-rapid-acquisition-methods.md)** — Every proven technique from Output Hypothesis to Memory Palace
- **[Cloze Exercises](language-reference/12-cloze-method.md)** — 200 fill-in-the-blank exercises across 6 skill tiers
- **[Mnemonic Dictionary](language-reference/13-mnemonic-dictionary.md)** — Vivid keyword images for words that won't stick
- **[AI Reverse Engineering Handbook](language-reference/14-ai-reverse-engineering-handbook.md)** — The meta of the meta: 7-layer stack, interference maps, error archaeology, compression theory, 7 novel AI techniques

Browse the full index: [language-reference/README.md](language-reference/README.md)

## Project Structure

```
velocidad/
├── config/
│   ├── learner-profile-template.yaml  # Profile schema to copy into your data dir
│   ├── paths.yaml.template            # Points the engine at your private data dir
│   └── rules-of-immersion.md          # 15 rules the agent must follow
├── meta/
│   ├── language-architecture.md       # Spanish decomposed into 6 layers
│   ├── memory-techniques.md           # Mnemonics + retention methods
│   └── system-changelog.md            # How the system evolves
├── worlds/
│   ├── mcdonalds/scenario.md          # The safe lab — ordering, small talk
│   ├── casa/scenario.md               # House workers — directions, logistics
│   ├── vecinos/scenario.md            # Neighbors — real friendship
│   └── errands/scenario.md            # Local errands — daily deployment
├── prompts/                           # 6 agent mode prompts (see table above)
├── sessions/                          # Daily transcripts + friction logs
│   └── TEMPLATE.md                    # Session folder structure
├── srs/
│   ├── box1.md                        # New / just failed (daily review)
│   ├── box2.md                        # Getting it (every other day)
│   ├── box3.md                        # Almost owned (every 3 days)
│   └── box4.md                        # Mastered (weekly)
├── language-reference/                # 📚 The Living Library (see below)
│   ├── README.md                      # Library index with reading orders
│   ├── 00-05                          # System: how Spanish works (6 layers)
│   ├── 06-core-vocabulary.md          # 1,000 essential words by frequency
│   ├── 07-cognate-accelerator.md      # 18 suffix rules → 3,000+ words from English
│   ├── 08-verb-reference.md           # 50 verbs, full conjugation tables
│   ├── 09-numbers-time-dates.md       # Complete numeric system
│   ├── 10-prepositions.md             # 20 prepositions + por vs para deep dive
│   ├── 11-rapid-acquisition-methods.md  # 18 proven learning methods
│   ├── 12-cloze-method.md             # Cloze deletion theory + 200 exercises
│   ├── 13-mnemonic-dictionary.md      # 165+ keyword mnemonics for hard words
│   ├── 14-ai-reverse-engineering-handbook.md  # Meta-meta: AI X-ray into Spanish
│   ├── FIELD-MANUAL.md                # Daily deployment reference
│   └── *.md                           # Visual ref, German bridges, priority order
├── chunks/
│   └── reference.md                   # Universal phrase reference
├── patterns/
│   └── reference.md                   # Universal sentence templates
└── docs/
    ├── KNOWLEDGE-ENGINE-OVERVIEW.md   # What this engine is + the production flywheel
    ├── DOMAIN-SPEC.md                 # How to add a new domain
    ├── LEARNER-DATA-SPEC.md           # Learner data directory contract
    ├── WORLD-LADDER-TEMPLATE.md       # Blank L1-L5 scenario scaffold
    ├── TECHNICAL-TRACK.md             # Guide for professional vocabulary domains
    └── design.md                      # Vision, architecture, implementation
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

# 3. Open VS Code with agent mode (or any Claude/GPT interface)
# 4. Paste the contents of prompts/master.md into the agent
# 5. Tell it which world to run (e.g., "Today's world: mcdonalds")
# 6. Do the session. The agent handles everything else.
```

**First time?** `docs/LEARNER-DATA-SPEC.md` has the initialization checklist — seven files to create, takes about ten minutes.

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
  prompts/             ← reads from {learner_data_dir}

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

The same engine generalizes to any domain where skill is built under pressure — professional and
technical vocabulary, public speaking, music performance, negotiation. The flywheel, SRS, friction
log, and L1-L5 ladder are domain-agnostic; only the scenarios and reference content change.

- [`docs/KNOWLEDGE-ENGINE-OVERVIEW.md`](docs/KNOWLEDGE-ENGINE-OVERVIEW.md) — what the engine is and which domains fit
- [`docs/DOMAIN-SPEC.md`](docs/DOMAIN-SPEC.md) — how to build a new domain that plugs into the engine
- [`docs/TECHNICAL-TRACK.md`](docs/TECHNICAL-TRACK.md) — worked guide for professional / technical vocabulary domains

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
- [Language Reference Library](language-reference/README.md) — Complete index of all reference material with reading orders
- [Learner Data Spec](docs/LEARNER-DATA-SPEC.md) — The contract between engine and personal data directory
- [Domain Spec](docs/DOMAIN-SPEC.md) — How to add a new domain to the engine
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

**Step 3: Customize three things in your learner data directory:**

1. **`profile.yaml`** — Your motivation, real deployment targets (the actual people you'll practice with), and learning tendencies. Be specific. This is what the agent reads to personalize every session.

2. **`worlds/`** (in your data dir, or fork from engine) — The included worlds reflect one person's life. Swap in yours. Each world is a markdown file with a 5-level scenario ladder.

3. **`meta/language-architecture.md`** — The engine version is built for Spanish. If you're learning something else, copy it to your data directory and rewrite the 6 layers for that system.

**What you don't need to touch to get started:** prompts, session template, chunk/pattern reference files. All universal.

---

**Organization:** Organic Arts LLC  
**Engine License:** [GPL-3.0-or-later](LICENSE) — prompts, config, meta, methodology  
**Content License:** [CC BY-SA 4.0](CONTENT-LICENSE) — language-reference, worlds, chunks, patterns, session templates  
**Status:** Active  
**Last Updated:** April 10, 2026