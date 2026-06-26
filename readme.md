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

- **Week 1:** Coffee World (order, clarify, small talk, pay)
- **Week 2:** Grocery World (find items, ask help, checkout)
- **Week 3:** Small Talk World (weather, plans, compliments)

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
│   ├── learner-profile.yaml     # Your context, people, learning style
│   └── rules-of-immersion.md    # 15 rules the agent must follow
├── meta/
│   ├── language-architecture.md  # Spanish decomposed into 6 layers
│   ├── learning-observations.md  # What works for you (agent-updated)
│   └── system-changelog.md       # How the system evolves
├── worlds/
│   ├── mcdonalds/scenario.md     # The safe lab — ordering, small talk
│   ├── casa/scenario.md          # House workers — directions, logistics
│   ├── vecinos/scenario.md       # Neighbor family — real friendship
│   └── errands/scenario.md       # Local errands — daily deployment
├── prompts/                       # 6 agent mode prompts (see table above)
├── sessions/                      # Daily transcripts + friction logs
│   └── TEMPLATE.md               # Session folder structure
├── srs/
│   ├── box1.md                   # New / just failed (daily review)
│   ├── box2.md                   # Getting it (every other day)
│   ├── box3.md                   # Almost owned (every 3 days)
│   └── box4.md                   # Mastered (weekly)
├── language-reference/             # 📚 The Living Library (see below)
│   ├── README.md                  # Library index with reading orders
│   ├── 00-05                      # System: how Spanish works (6 layers)
│   ├── 06-core-vocabulary.md      # 1,000 essential words by frequency
│   ├── 07-cognate-accelerator.md  # 18 suffix rules → 3,000+ words from English
│   ├── 08-verb-reference.md       # 50 verbs, full conjugation tables
│   ├── 09-numbers-time-dates.md   # Complete numeric system
│   ├── 10-prepositions.md         # 20 prepositions + por vs para deep dive
│   ├── 11-rapid-acquisition-methods.md  # 18 proven learning methods
│   ├── 12-cloze-method.md         # Cloze deletion theory + 200 exercises
│   ├── 13-mnemonic-dictionary.md  # 165+ keyword mnemonics for hard words
│   ├── 14-ai-reverse-engineering-handbook.md  # Meta-meta: AI X-ray into Spanish as a system
│   ├── FIELD-MANUAL.md            # Daily deployment reference
│   └── *.md                       # Visual ref, German bridges, priority order
├── chunks/
│   └── reference.md              # Universal phrase reference (engine copy)
├── patterns/
│   └── reference.md              # Universal sentence templates (engine copy)
├── technical/
│   ├── library/                  # 92 ingested reference docs + INDEX.md
│   ├── srs/                      # Technical SRS boxes (41 cards in box1)
│   ├── domains/                  # 4 domain scenario ladders
│   ├── chunks/bank.md            # Technical vocabulary bank
│   ├── patterns/bank.md          # Technical sentence pattern bank
│   ├── sessions/                 # Technical session records
│   └── prompts/                  # Technical track prompts
├── dashboard.py                   # Interactive terminal dashboard (both tracks)
├── start-dashboard.sh             # Dashboard launcher
├── requirements.txt               # Python deps (rich)
├── publish-public.sh              # Orphan clone release script (no history exposed)
└── docs/
    ├── KNOWLEDGE-ENGINE-OVERVIEW.md  # What this engine is + the production flywheel
    ├── DOMAIN-SPEC.md                # How to add a new domain (Spanish, technical, etc.)
    ├── LEARNER-DATA-SPEC.md          # Learner data directory contract
    ├── WORLD-LADDER-TEMPLATE.md      # Blank L1-L5 scenario scaffold
    ├── TECHNICAL-TRACK.md            # Guide for professional vocabulary domains
    ├── design.md                     # Vision, architecture, implementation
    └── seed/                         # Original brainstorm archive
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

### Releasing the Engine Publicly

#### Two-remote workflow

The recommended setup uses two remotes:

```
origin  → your-private-backup-repo   ← VS Code Sync, git push, git pull all go here
public  → velocidad (public)           ← blocked by pre-push hook; publish via script only
```

Add the named remote once:
```bash
git remote add public https://github.com/OrganicArtsLLC/velocidad.git
```

#### Three layers of protection

1. **Remote routing** — `origin` points at your private backup. Normal git operations (`push`, `pull`, `fetch`) never touch the public repo.
2. **Pre-push hook** — `.git/hooks/pre-push` hard-blocks any direct `git push` to the public repo URL — including VS Code's Sync button. Attempting it prints an error and exits.
3. **Verification scan** — `./publish-public.sh` scans the build snapshot for personal data patterns before committing. If anything leaks through, the publish aborts and the build dir is removed.

#### Installing the pre-push hook

```bash
cat > .git/hooks/pre-push << 'EOF'
#!/usr/bin/env bash
PUBLIC_URL="https://github.com/OrganicArtsLLC/velocidad.git"
PUBLIC_SSH="git@github.com:OrganicArtsLLC/velocidad.git"
PUSH_URL="$2"
if [[ "$PUSH_URL" == "$PUBLIC_URL" || "$PUSH_URL" == "$PUBLIC_SSH" ]]; then
  echo "✗ BLOCKED: Direct push to the public repo is not allowed."
  echo "  Use: ./publish-public.sh"
  echo "  The script creates a clean orphan commit with no history."
  exit 1
fi
EOF
chmod +x .git/hooks/pre-push
```

#### Publishing a release

```bash
./publish-public.sh
./publish-public.sh "feat: add three new cloze exercises"   # custom commit message
```

This creates an orphan clone — a fresh git repository with a single flat commit containing only engine files. Your private history stays local. The public repo shows no history of personal data, SRS state, or profile iterations. Run it anytime to update the public release.

---

## Technical Track

Parallel to the Spanish engine, a **professional fluency track** for software engineering, DevOps, AI tooling, and Python.

The same mechanics — SRS, chunks, patterns, domain scenarios — applied to the vocabulary you need to be authoritative in architecture discussions, code reviews, and platform work.

### Technical Domains

| Domain | Purpose | Scenario Ladder |
|--------|---------|----------------|
| **Software Engineering** | Code review, ADRs, design patterns, design discussions | L1 Pattern Recognition → L4 Design Docs |
| **DevOps & Platform** | platform tooling, pipelines, baseline/drift language | L1 Core Concepts → L5 Institutional Authority |
| **AI Tooling** | Agent mode, prompting, RAG, failure diagnosis | L1 Single-Turn → L4 System Design |
| **Python & Data** | Typed Python, testable code, data pipelines | L1 Typed Functions → L4 Production Systems |

### Technical Engine Layout

```
technical/
├── library/
│   ├── foundations/         # 60 foundational SE/DevOps/Systems texts
│   ├── ai-ml/              # 19 AI/ML reference docs
│   ├── books/              # 13 key books (DDIA, DevOps Handbook, etc.)
│   └── INDEX.md            # 92-document catalog with priorities + reading paths
├── srs/
│   ├── box1.md             # 41 cards across all 4 domains (daily review)
│   ├── box2.md             # Getting it (every other day)
│   ├── box3.md             # Almost owned (every 3 days)
│   └── box4.md             # Mastered (weekly)
├── domains/
│   ├── ai-tooling/scenario.md
│   ├── devops-platform/scenario.md
│   ├── python-data/scenario.md
│   └── software-engineering/scenario.md
├── chunks/bank.md          # Technical term bank
├── patterns/bank.md        # Sentence templates for technical language
├── sessions/
│   └── TEMPLATE.md         # Session folder: plan / transcript / friction / debrief
└── prompts/                # Technical track agent prompts
    ├── master.md
    ├── distiller.md
    ├── srs-generator.md
    └── meta-observer.md
```

### Interactive Dashboard

Both tracks are navigable from a single terminal dashboard:

```bash
./start-dashboard.sh
```

- SRS review with grading and automatic card promotion between boxes
- Library browser (92 docs, reading paths, opens PDFs in system viewer)
- Chunk and pattern browsers for both tracks
- Session launcher with domain + level selection

Requires: `pip install rich`

---

## Design Principles

- **Retrieval dominance** — Speak before seeing answers
- **Contextual repetition** — Same scenario, different angles
- **Emotional salience** — Real scenarios you'll actually use
- **Minimal cognitive overload** — 25-30 min, one scenario per week
- **Pattern compounding** — Week 1 patterns return in Week 2
- **Motor repetition** — Say it out loud; mouth muscle matters

## Documentation

- [Language Reference Library](language-reference/README.md) — Complete index of all reference material with reading orders
- [Learner Data Spec](docs/LEARNER-DATA-SPEC.md) — The contract between engine and personal data directory
- [Design Document](docs/design.md) — Vision, architecture, ideas, implementation plan
- [Seed Conversation](docs/seed/chatgpt-seed-conversation.md) — Original brainstorm that spawned this project

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