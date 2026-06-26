# Velocidad: Knowledge Engine Overview

**Version:** 1.0.0
**Status:** Active

---

## What This Engine Is

Velocidad is a **production-first fluency engine** for any domain where skill is built under pressure.

The premise: in most skill domains, there is a gap between *knowing* something and *executing it under
real conditions*. You can know 2,000 Spanish words and freeze in a conversation. You can study system
architecture for a year and fumble through a whiteboard interview. You can practice a piece of music
at home and lose it on stage.

The gap is not knowledge. The gap is **production under pressure** — and it closes only through
deliberate exposure to the conditions that activate it.

Velocidad uses an AI agent to simulate those conditions before you face them in the real world.

---

## The Core Mechanism

### The Flywheel

```
Deploy → Capture → Distill → Drill → Redeploy
```

1. **Deploy:** Perform in a simulated realistic scenario before you feel ready
2. **Capture:** Log what broke (friction log — 5 friction types)
3. **Distill:** Extract the gaps into the smallest learnable units
4. **Drill:** Repeat those units under production pressure until they are automatic
5. **Redeploy:** Return to the scenario with the gaps closed — note what opened new gaps

Each cycle is short (25-30 minutes). The point is frequency and honest friction capture, not
comprehensive study.

### The Friction Log

What breaks under pressure is specific. The friction log captures five categories:

1. **Production gaps** — things I tried to execute but couldn't
2. **Comprehension gaps** — things I didn't understand
3. **Recurring errors** — patterns of mistakes (show up across sessions)
4. **Target areas** — output qualities causing confusion or failure (accent, syntax, vocabulary choice)
5. **Avoidance patterns** — content or structures I navigate around instead of engaging

If you don't log friction, the flywheel stops. The entire system is built around making friction
capture easy enough that it happens every session.

### The SRS System

Gaps become cards. Cards live in a 4-box Leitner system:

- Box 1: New or just failed → review daily
- Box 2: Getting it → review every 2 days
- Box 3: Almost owned → review every 3 days
- Box 4: Mastered → review weekly

The SRS system does one thing: it ensures that what broke in a session gets reviewed until it is
automatic. Fail → drop back a box. Succeed twice → advance.

---

## Why Production-First Works

Traditional skill acquisition is **recognition-first**: study → understand → eventually produce.

Production-first is **inverse**: produce (under real pressure) → identify gaps → study only what
broke → produce again.

Recognition-first feels safe. It builds confidence through comprehension before requiring performance.
The cost: you can recognize far more than you can produce, and production pressure collapses the gap
in ways that recognize-first mastery does not survive.

Production-first is uncomfortable early. You will fail sessions, freeze, avoid vocabulary you haven't
drilled. This is the mechanism — every failure is a higher-quality SRS card than anything you'd have
created by studying first.

---

## The Agent's Role

The AI agent serves as:

- **Scenario partner / NPC:** Simulates the deployment context (customer, colleague, interviewer)
- **Friction observer:** Notes hesitation, errors, avoidance patterns during the session
- **Distiller:** Extracts gaps from the session and generates targeted SRS cards
- **Session planner:** Prepares the next session based on friction patterns
- **Meta-observer:** Identifies learning patterns over time and adjusts the system

The agent does not lecture. It creates pressure, observes what breaks, and helps you close the gaps.

Six prompts cover the full workflow:
- `master.md` — Complete engine (use this daily)
- `session-runner.md` — Scenario roleplay only
- `distiller.md` — Extract friction from session transcript
- `srs-generator.md` — Create targeted SRS cards from friction log
- `session-planner.md` — Plan the next session
- `meta-observer.md` — Weekly recursive system review

---

## Applicable Domains

The engine requires three things from a domain to work:

1. **Production under pressure can be simulated.** The AI agent can credibly play a scenario
   partner, evaluator, or interviewer who creates realistic pressure.

2. **Failure is discrete and capturable.** What broke can be described specifically enough to
   convert into a learnable unit.

3. **Repetition closes gaps.** The skill builds through deliberate practice, not just exposure.

Domains that satisfy these criteria:

- **Language learning** (current reference implementation: Spanish)
- **Professional vocabulary** (technical interviews, product reviews, stakeholder meetings)
- **Music performance** (sight-reading, improvisation, performance anxiety)
- **Public speaking** (structuring arguments, managing nerves on delivery)
- **Sales and negotiation** (objection handling, framing)
- **Leadership and communication** (difficult conversations, institutional language)
- **Medical and legal vocabulary** (professional communication under time pressure)

The Spanish track is the reference implementation. The `docs/DOMAIN-SPEC.md` defines how to build
a new domain that plugs into the same engine.

---

## Repository Structure

The engine is separated from personal data by design. What lives here:

- **Engine prompts:** `prompts/` — the methodology (6 prompts, GPL-3.0)
- **Reference domain (Spanish):** `worlds/`, `language-reference/`, `chunks/reference.md`,
  `patterns/reference.md` — the reference implementation (CC BY-SA 4.0)
- **Config templates:** `config/` — path configuration and learner profile templates
- **Domain spec:** `docs/DOMAIN-SPEC.md` — how to add a new domain
- **Learner data spec:** `docs/LEARNER-DATA-SPEC.md` — what your private data directory must contain

What lives in your private data directory (never in this repo):

- Your sessions, SRS cards, profile, mastery tracking
- Any domain with personal/employer context
- Any reference material that is not your original work

See `docs/LEARNER-DATA-SPEC.md` for the full spec.

---

## Adding a Domain

1. Read `docs/DOMAIN-SPEC.md`
2. Create the required directory structure in your private data directory (or a separate repo)
3. Register it in `config/paths.yaml` under `domains:`
4. Run `prompts/master.md` and tell the agent which domain to use

The domain doesn't need to be complete to be useful. Start with one scenario at L1.

---

## License

The Velocidad engine and this document: **GPL-3.0-or-later**
Reference domain content (Spanish): **CC BY-SA 4.0** (see `CONTENT-LICENSE`)

---

*Last Updated: April 10, 2026*
