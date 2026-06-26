# 🏛️ Philosophy & Discourse — A Velocidad Study

**Build the ability to argue real positions under pressure** — to state what a thinker actually held,
defend it, steelman the opposition, and answer objections without hand-waving.

This is a **study** that plugs into the [Velocidad knowledge engine](../docs/KNOWLEDGE-ENGINE-OVERVIEW.md).
Spanish is the reference study; this one applies the identical engine to argument and rhetoric. See
[`docs/STUDY-SPEC.md`](../docs/STUDY-SPEC.md) for the contract every study satisfies.

---

## Core Hypothesis

The gap is not knowledge — it's **production under pressure**. You can have read Aristotle and still
lose the argument because you can't deploy the position aloud when a live mind pushes back. Comprehension
collapses in the arena; only rehearsed production survives it.

> Argument fluency = Composure under pressure + Reception without drowning + Moves drilled to reflex

The same flywheel that turns conversational failure into Spanish fluency turns half-formed opinions into
rigorous argument.

## How It Works — the Daily Engine (25-30 min)

```
Deploy → Capture → Distill → Drill → Redeploy
```

1. **Deploy** — argue a real position in a scenario before you feel ready (Spanish-counter equivalent:
   defending a claim in real time against a sharp interlocutor)
2. **Capture** — log what broke: a missing warrant, a misattribution, a strawman you reached for
3. **Distill** — turn each gap into the smallest learnable unit (a move, a definition, a one-line position)
4. **Drill** — repeat under pressure until the move fires cold, in under ten seconds
5. **Redeploy** — return to the argument with the gap closed; note what opened a new one

## The Scenarios (L1–L5 ladders)

Each scenario is a deployment context with a five-level ladder (`scenarios/<slug>/scenario.md`):

| Scenario | What it drills |
|----------|----------------|
| `steelman-debate` | The signature move: state the opposition at its strongest, then rebut |
| `socratic-dialogue` | Hold a definite claim under relentless questioning; refine or retract honestly |
| `stoic-reflection` | Deploy the dichotomy of control on a real situation — applied, not recited |
| `position-defense` | Reconstruct a named thinker's actual view and defend it faithfully |
| `rhetorical-composition` | Build a persuasive case with the three appeals and the five canons |
| `fundamentals-logic` | Judge validity, name fallacies, produce counterexamples — on live arguments |
| `fundamentals-rhetoric` | The live moves at training weight: pause, receive, locate, answer |
| `fundamentals-philosophy` | Turn the canon into ammunition you can fire in one line |

## The Reference Shelf

Original educational summaries (`reference/`, CC BY-SA 4.0). The agent pulls from these when session
friction exposes a gap:

- **[discourse-codex.md](reference/discourse-codex.md)** — the spine: the five domains of a live exchange
- **[logic-codex.md](reference/logic-codex.md)** — the formal floor: validity, the conditional, quantifiers, counterexamples
- **[rhetoric-toolkit.md](reference/rhetoric-toolkit.md)** — appeals, canons, Toulmin, stasis, the steelman, fallacies
- **[positions-of-the-greats.md](reference/positions-of-the-greats.md)** — one-line index across the canon
- Thinker files: [Plato & Aristotle](reference/classical-plato-aristotle.md) ·
  [the Stoics](reference/stoics-seneca-marcus.md) · [Cicero](reference/cicero-rhetoric-politics.md) ·
  [Descartes & Schopenhauer](reference/moderns-descartes-schopenhauer.md)

## Production Units

- **[chunks/reference.md](chunks/reference.md)** — the minimal lines to say under pressure (moves, term
  definitions, one-line positions, named fallacies)
- **[patterns/reference.md](patterns/reference.md)** — fill-in-the-blank argument scaffolds
  (claim→warrant→support, steelman-then-rebut, concede-and-refine, state-a-position)

## How to Run It

```bash
# Run the all-in-one daily engine against a scenario
./velocidad -s philosophy prompt --scenario steelman-debate

# Drill the SRS deck (moves, positions, fallacies)
./velocidad -s philosophy srs
```

Or paste `prompts/master.md` into agent mode with the repo open and name your scenario. The other
prompts (`distiller.md`, `srs-generator.md`, `meta-observer.md`) run individual stages of the loop.

To register the study with the engine, add it to `config/paths.yaml` under `studies:` (see
[`docs/STUDY-SPEC.md`](../docs/STUDY-SPEC.md) §Registering a Study).

## Friction Types (what to hunt)

Beyond the engine's base five, this study names:

- **Missing warrant** — stated a claim, couldn't supply the reason that connects evidence to conclusion
- **Misattribution** — wrong thinker, or the popular blur instead of the real view
- **Strawman reach** — could only argue against a weak version of the opposition
- **Definitional slip** — used a loaded term without pinning its meaning
- **Conceded-too-late / dug-in** — failed to update when the objection was decisive

## License

- Study methodology (config, scenario structure, prompts): **GPL-3.0-or-later** (the engine)
- Original educational reference content (the codices, chunks, patterns): **CC BY-SA 4.0**

All reference content here is original work written to teach the ideas — summarized and cited, never
copied from copyrighted texts. Attributions and dates follow standard scholarship; where a specific
attribution is uncertain it is stated generically rather than asserted.

---

*A Velocidad study. The study is useful before it is complete — start with one scenario at L1 and expand.*
