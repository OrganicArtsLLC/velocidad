# Velocidad: Technical Track Guide

**Version:** 1.1.0
**Status:** Active

---

## What the Technical Track Is

The Velocidad engine builds production fluency in any study. Most documentation focuses on the
Spanish language learning study. This guide explains how to apply the same engine to **professional
and technical vocabulary** — the language of your actual job. (In this repo, the planned
`distributed-systems/` study is a worked instance of this guide.)

"Technical vocabulary" means the phrases, patterns, and conceptual language that distinguish
someone who can perform in a professional context from someone who technically knows the material
but fumbles when executing under pressure:

- A developer who can code but freezes in architecture reviews
- A data engineer who understands the concepts but stumbles when stakeholders ask questions
- A new manager who has the ideas but whose phrasing undermines their authority in meetings
- A practitioner who knows the tools but uses the wrong vocabulary register in documentation

The gap is rarely knowledge. It is production fluency — the difference between knowing a term and
being able to deploy it accurately, contextually, and confidently under pressure.

---

## How This Differs From Spanish

In the Spanish study, the deployment context is a specific physical interaction (ordering food,
talking to a neighbor). The target form is another language.

In a technical study:
- **Deployment contexts** are professional scenarios: design reviews, team standups, incident
  response, slack threads, documentation, interviews, stakeholder presentations
- **Target form** is accurate, confident professional language — the vocabulary register that
  signals mastery, not just familiarity
- **Production pressure** comes from stakes: a colleague's evaluation, a deadline, a live interview
- **The NPC / scene partner** is the agent simulating a colleague, interviewer, or stakeholder

Everything else — the L1-L5 ladder, friction log, SRS boxes, session structure — is identical.

---

## Study Structure for a Technical Track

A technical study directory follows the same spec as any study (see `docs/STUDY-SPEC.md`).

```
{study_name}/                  # e.g., "distributed-systems", "platform-engineering"
├── study-config.md
├── scenarios/
│   ├── arch-review.md         # "I need to explain my design to a senior engineer"
│   ├── incident-postmortem.md # "I need to present a postmortem to stakeholders"
│   ├── pair-review.md         # "I need to talk through my code in a PR review"
│   └── onboarding.md          # "I need to explain the codebase to a new team member"
├── reference/
│   ├── architecture-vocab.md  # Terms and patterns for discussing system design
│   ├── data-models.md         # Vocabulary for representing and explaining data
│   └── stakeholder-language.md # Vocabulary for translating technical work into business terms
├── chunks/reference.md             # Production phrases: "the tradeoff here is...", "given that..."
└── patterns/reference.md           # Sentence templates: "This component [verb] by [mechanism]..."
```

**Keep private:**
- `scenarios/` files that reference specific coworkers, internal projects, employer-specific tooling
- `reference/` files synthesized from copyrighted books, internal documentation, or proprietary specs
- `chunks/reference.md` entries built from real colleague interactions
- Any content that would identify your employer or expose internal processes

**Safe to publish:**
- Generic scenario structure (no real names, no employer-specific context)
- Vocabulary organized around public-domain concepts (general architecture terms, standard patterns)
- Blank study template (the scaffold, not the populated content)

---

## Building Your Technical Study

### Step 1: Choose your vocabulary area

You don't need one big "technical" study. You need the specific vocabulary area where your
production fluency is weakest. Examples:

- System design vocabulary (for architecture interviews or design reviews)
- SQL and data modeling vocabulary (for stakeholder-facing data work)
- Product management language (for engineers who present to product and business teams)
- Platform / infrastructure vocabulary (Kubernetes, CI/CD, SRE concepts under pressure)
- API design vocabulary (for tech leads reviewing API PRs with junior engineers)

Smaller is better. One scenario and one reference file is enough to start.

### Step 2: Map your real deployment contexts

Where do you actually need to perform? Not hypothetically — concretely:

- Tuesday 10am standup where your manager asks why the migration is delayed
- Thursday sprint review where the PM asks whether the feature is ready to ship
- Async Slack thread where a stakeholder asks for a technical risk summary
- Job interview where the interviewer asks how you'd design a rate limiter

Write those specific contexts as your scenarios. Use the `docs/SCENARIO-LADDER-TEMPLATE.md` scaffold.

### Step 3: Populate reference files from public sources

Build reference files that compile the vocabulary you need — organized by topic, not difficulty.
Use public-domain sources, your own synthesis of concepts, and vocabulary extracted from your
own friction sessions.

**Never paste copyrighted content.** Summarize, rephrase, or write your own explanation.
The reference file is your own articulation of the concept, not a transcript of someone else's.

### Step 4: Practice with the agent on L1 scenarios

Run the master prompt. Tell the agent which study you are using. Ask it to play the L1 scenario
— the simplest version of your deployment context.

Log what broke. Build SRS cards from the gaps. Drill. Return.

### Step 5: Advance based on real-world evidence

L2 is not "I can do it in practice." L2 is "I handled it in a real meeting before breaking down."
The ladder is evidence-based. Move up when the real context confirms it, not when the simulation does.

---

## Agent Rules for Technical Studies

In the `study-config.md` for a technical study, include these immersion rules:

1. **Use realistic professional register** — not over-formal, not casual. Read the scenario's
   tone and match it.
2. **The NPC has an objective, not a script** — they want to understand the system, evaluate the
   design, or get a status update. They will ask follow-up questions if the answer is vague.
3. **Flag production failures specifically** — if the learner says "it's kind of like, the thing
   that handles the... the processing part," flag "processing infrastructure" or the precise term
4. **Never front-load vocabulary** — don't explain terms before the session. Log the gap and return.
5. **Time pressure is real** — in meeting simulations, introduce time pressure ("we have 5 minutes")
6. **Evaluation role** — in interview simulations, the NPC is evaluating and may decline to advance

---

## Example: Blank Study Template

A blank starter study directory for a generic technical vocabulary study. Copy this structure and
fill in your content.

```
generic-technical-study/
├── study-config.md               # Fill in: name, deployment contexts, friction types
├── scenarios/
│   └── design-review.md          # Fill in: L1-L5 ladder for explaining a system design
├── reference/
│   └── core-vocabulary.md        # Fill in: 20-30 terms that come up most in your context
├── chunks/reference.md                # Start blank; build from sessions
└── patterns/reference.md              # 5-10 starter patterns; add from sessions
```

This template is intentionally empty. Your content fills it. The study becomes valuable as you
build it through real friction sessions — not before.

---

## What Not to Do

- **Don't build a vocabulary list first and practice second.** That's recognition-first. Start with
  a deployment scenario and see what you can't produce.
- **Don't populate reference files from copyrighted books by copying text.** Summarize concepts in
  your own words. Test your understanding by writing the explanation yourself.
- **Don't advance the ladder based on simulation.** Only real stakes count for level progression.
- **Don't make the study too broad.** "All technical vocabulary" is not a study. "How I explain
  database design decisions to my PM" is a study.

---

## See Also

- `docs/STUDY-SPEC.md` — Full study specification
- `docs/SCENARIO-LADDER-TEMPLATE.md` — Scaffold for building scenario files
- `docs/KNOWLEDGE-ENGINE-OVERVIEW.md` — Engine overview and production-first methodology
- `docs/LEARNER-DATA-SPEC.md` — Learner data structure (where your private content lives)

---

*Last Updated: June 2026*
