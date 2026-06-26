# Velocidad-AI: Learner Data Specification

**Version:** 1.1.0  
**Status:** Active  
**Purpose:** Defines the contract between the Velocidad-AI engine and a learner's personal data directory.

---

## Domain-Agnostic Note

This specification applies to **any learning domain**, not only Spanish.

The Velocidad-AI engine is a production-first fluency methodology that works for any domain where
you need to perform under pressure — foreign language, technical vocabulary, professional register,
communication skills. Each domain lives in its own directory and implements this contract.

Multiple domain directories can coexist:
```
[your-private-repo]/
  velocidad/            # Spanish track (implements this spec)
  velocidad-technical/  # Technical track (implements this spec in a separate dir)
```

The `config/paths.yaml` file maps domain names to directory paths. See `docs/DOMAIN-SPEC.md` for
the full domain structure specification.

The rest of this document uses the Spanish track as the **reference implementation example**.
All field names, file names, and examples are the Spanish-track version. When building a different
domain, substitute your domain's vocabulary, deployment contexts, and scenario files accordingly.

---

## Overview

The Velocidad-AI engine (this repository) is stateless with respect to your personal data. It
contains methodology, prompts, worlds, and universal reference content — but nothing about you.

Your personal data lives in a directory that **implements this spec**. The engine reads from it; your
progress accumulates in it. The two grow independently.

**Benefits:**
- Your sessions, SRS state, and progress are in your private repo (not in the engine's git history)
- The engine can be updated without touching your data
- Multiple learners can use the same engine with their own data directories
- Your data directory is portable — move it, back it up, version it independently

---

## Required Directory Structure

```
{learner_data_dir}/
├── README.md                        # Describes this as your personal learner data
├── profile.yaml                     # Who you are (follows profile schema below)
├── sessions/                        # WORM — never modify past sessions
│   ├── YYYY-MM-DD/                  # One folder per session day
│   │   ├── plan.md                  # Pre-session: world, level, focus, warmup
│   │   ├── transcript.md            # During: full roleplay in Spanish
│   │   ├── friction.json            # Post: what broke (schema below)
│   │   └── debrief.md               # Post: corrections, chunks, patterns, next plan
│   └── ...
├── srs/                             # 4-box Leitner system (personal card state)
│   ├── box1.md                      # New / just failed — review daily
│   ├── box2.md                      # Getting it — review every 2 days
│   ├── box3.md                      # Almost owned — review every 3 days
│   └── box4.md                      # Mastered — review weekly
├── progress/                        # Personal mastery tracking
│   ├── metrics.md                   # Weekly velocity scorecard
│   ├── chunks.md                    # Which chunks from the reference you've mastered
│   └── patterns.md                  # Which patterns from the reference you've mastered
└── meta/                            # Personal learning observations
    └── learning-observations.md     # How you learn — updated by agent after sessions
```

---

## File Schemas

### `profile.yaml`

```yaml
name: "Your name"

level:
  self_assessment: "brief description of current level"
  can_do:
    - "list what you can currently do"
  cannot_yet:
    - "list what you can't do yet"

motivation:
  primary: "Why are you learning Spanish?"
  emotional_anchors:
    - "specific people or situations that make this real"
  identity_shift: "The person you're becoming, not the student you are"

deployment_targets:
  - name: "Name or role of real person"
    context: "Where and how you'll practice with them"
    stakes: low | medium | high
    frequency: "how often"
    scenario_type: "what kind of interaction"

learning_style:
  strengths:
    - "how you learn best"
  watch_outs:
    - "patterns that slow you down"
  accelerators:
    - "techniques that work for you specifically"

current_worlds:
  - world: "mcdonalds"
    level: L1
    last_session: "YYYY-MM-DD"
    deploy_count: 0
```

---

### `friction.json`

Schema for the post-session friction log. One file per session folder.

```json
{
  "date": "YYYY-MM-DD",
  "world": "mcdonalds | casa | vecinos | familia | errands",
  "ladder_level": "L1 | L2 | L3 | L4 | L5",
  "production_gaps": [
    "Things I tried to say but couldn't — describe the scenario, not just the word"
  ],
  "comprehension_gaps": [
    "Things the NPC said that I didn't understand"
  ],
  "recurring_errors": [
    "Top 3 patterns of mistakes — be specific"
  ],
  "pronunciation_targets": [
    "Max 3 sounds causing confusion or miscommunication"
  ],
  "avoidance_patterns": [
    "Topics or structures I navigated around instead of engaging"
  ]
}
```

---

### `srs/box*.md`

Each SRS box file holds cards in this format. Cards progress Box 1 → 4. Fail = back to Box 1.

```markdown
---
Type: prod | comp | transform | variation | repair
Tags: [world, level, topic]
Front: [Production prompt in English] or [Comprehension prompt in Spanish]
Back: [Expected Spanish production] or [English meaning]
Box: 1
Streak: 0
Note: optional context or common error
---
```

**Box advancement rules:**
- Get it right twice in a row (Streak ≥ 2) → advance one box
- Any failure → drop to Box 1, reset Streak to 0
- Say the answer OUT LOUD. Under 5 seconds = pass. Hesitation = fail.

**Card type definitions:**
- `prod` — English prompt → produce Spanish (core skill)
- `comp` — Spanish prompt → understand meaning (comprehension)
- `transform` — modify a sentence (negate, make formal, change tense)
- `variation` — swap one component in a known pattern (flex the template)
- `repair` — situation prompt → produce the correct repair phrase

---

### `progress/chunks.md`

Tracks which universal chunks (from `chunks/reference.md` in the engine) you've mastered.
Use the same symbol system as the reference file.

```markdown
# My Chunk Mastery

References: {engine_path}/chunks/reference.md

## Mastered — Box 4
Chunks you own completely. No hesitation in production or comprehension.

- Hola
- Muchas gracias
- [chunk] — [brief note if helpful]

## Active — Boxes 1-3
Chunks currently in your SRS rotation. Drilling now.

- [chunk] — Box [N], current error: [what breaks]

## Not Yet Started
Chunks identified to learn next. Add from reference as you're ready.

- [chunk]
```

---

### `progress/patterns.md`

Tracks which universal patterns (from `patterns/reference.md`) you've internalized.

```markdown
# My Pattern Mastery

References: {engine_path}/patterns/reference.md

## Mastered ✓
Can generate 5+ variants without hesitation.

- Pattern name — last verified: YYYY-MM-DD

## Drilling ⚡
In active SRS rotation. Can generate but need reinforcement.

- Pattern name — stuck point: [what aspect breaks]

## Not Yet Started
Identified, not yet drilled.

- Pattern name
```

---

### `progress/metrics.md`

Weekly velocity scorecard. The only metric that matters: are you speaking more Spanish to real people?

```markdown
# Velocidad Progress Metrics

## Weekly Scorecard

| Week | Sessions | Deploys | Chunks Box 4 | Patterns Owned | Real Convos | Notes |
|------|----------|---------|--------------|----------------|-------------|-------|
| YYYY-WNN | 0 | 0 | 0 | 0 | 0 | |

## World Level Progression

| World | Current Level | Last Session | Deploy Count |
|-------|---------------|--------------|--------------|
| mcdonalds | L1 | — | 0 |
| casa | L1 | — | 0 |
| vecinos | L1 | — | 0 |
| familia | L1 | — | 0 |
| errands | L1 | — | 0 |
```

---

### `meta/learning-observations.md`

Updated by the agent after sessions. Records what works, what doesn't, and system adjustments.

```markdown
# Learning Observations

## How I Learn Best
[Your learning patterns — filled in by both you and the agent over time]

## What Works
- [date] — specific observation about what accelerated learning

## What Doesn't Work
- [date] — specific observation about what slowed or blocked learning

## Breakthrough Moments
- [date] — specific moment when something clicked

## System Adjustments Made
- [date] — WHAT changed → WHY → RESULT (if known)
```

---

## How the Engine Reads Your Data

The Velocidad-AI prompts are designed to be pasted into agent mode with context loaded from
your learner data directory. When using any prompt:

1. **Open your data directory** alongside the engine repository in your editor
2. **Load the required context files** listed at the top of each prompt
3. **The agent reads your profile, SRS state, and observations** to personalize the session
4. **After the session, write outputs** (friction.json, debrief.md, SRS updates) back to your data directory

### Configuring the path

Copy `config/paths.yaml.template` to `config/paths.yaml` (gitignored in the engine repo)
and set `learner_data_dir` to your personal data directory's absolute or relative path.

```yaml
# config/paths.yaml (gitignored — do not commit)
learner_data_dir: "../[your-private-repo]/velocidad"
```

---

## Initialization Checklist

Setting up a new learner data directory:

- [ ] Create directory structure from the tree above
- [ ] Fill in `profile.yaml` — be specific about deployment targets and emotional anchors
- [ ] Copy blank SRS box templates from `sessions/TEMPLATE.md`
- [ ] Set `config/paths.yaml` in the engine to point to your directory
- [ ] Run your first session with `prompts/session-runner.md`
- [ ] Write your first `meta/learning-observations.md` entry after the session

---

## Versioning

This spec follows semantic versioning:
- **Major** — breaking changes to directory structure or required schemas
- **Minor** — new optional files or fields
- **Patch** — clarifications, examples, documentation

When the spec version bumps major, a migration guide will be provided.

---

*Velocidad-AI Learner Data Spec v1.0.0 — March 2026*
