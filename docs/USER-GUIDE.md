# Velocidad User Guide — the Operator's Manual

Every other doc in this repo explains *why* the engine is built the way it is. This one explains
what to do with your hands. It threads the CLI commands, the agent prompts, and the real-world
deploys into one routine: a day, a week, and a decision table for when something won't stick.

Assumes setup is done (`docs/LEARNER-DATA-SPEC.md` has the first-time checklist) and you know the
vocabulary: a **study** is a subject (`spanish`, `philosophy`, `distributed-systems`), a
**scenario** is a deployment context inside one, and the flywheel is
**Deploy → Capture → Distill → Drill → Redeploy**.

---

## A day with the engine (~30–45 min total, most of it the session)

### 1. Morning review — `daily` (5–15 min)

```bash
./velocidad daily              # add --calibrate about twice a week
```

One pass through every card due in **all** studies, interleaved — a Spanish chunk, then a
system-design card, then a philosophy compression. It will feel choppier than reviewing one study
at a time. That's by design; don't smooth it out.

Grading, honestly:

- **`y`** — produced it clean, at speed. Out loud. (Saying it in your head is recognition, not
  production — grade that `h` at best.)
- **`h`** — got there, but slow, partial, or shaky. Still advances the card, but `stats` tracks it:
  a domain full of `h` will fail you in a real room even though the deck looks green.
- **`n`** — anything else. Be ruthless; a false `y` costs you twice later.
- With `--calibrate`: after your attempt, before the reveal, rate 1 (guess) / 2 (shaky) / 3 (solid).
  Don't overthink it — the value is in the aggregate honesty check, not any single rating.

Skipped a day? Just run `daily` today. Never run junk reviews to protect the streak number.

### 2. Pick today's study and start it (2 min)

```bash
./velocidad -s spanish start            # or philosophy / distributed-systems
```

`start` shows status, offers the study's own SRS pass (skip if `daily` covered it), runs a warmup,
optionally the blitz drill, creates today's session folder (`sessions/YYYY-MM-DD/` with `plan.md`,
`transcript.md`, `friction.json`, `debrief.md`), and prints the master prompt.

### 3. The session — agent mode (15–30 min)

Paste the master prompt into agent mode (Claude/GPT), tell it the scenario and level, and do the
session. The master prompts are built production-first: you produce under constraint, the agent
tracks friction silently, then it debriefs you. Two rules while you're in it:

- **Produce out loud / in writing before looking anything up.** The reaching is the rep.
- **Let it finish the debrief.** The friction log JSON and the SRS card block at the end are the
  whole harvest; a session without them is cardio, not training.

### 4. Capture while it's hot (5 min)

The master prompt's later phases usually produce the friction log and cards inline. If you ran a
session elsewhere (a real meeting, a real call, a debate), use the study's `distiller.md` prompt on
your raw notes instead — same output shape.

Then bank it:

- Paste the friction JSON into today's `sessions/YYYY-MM-DD/friction.json`.
- Enter the cards with `./velocidad -s <study> add` — it writes the exact format and verifies the
  parser sees each card. (Pasting by hand into `box1.md` works but is how cards historically got
  silently dropped.)
- Anything for the banks (a chunk that worked, a pattern skeleton) gets appended to
  `chunks/reference.md` / `patterns/reference.md`.

### 5. Close the day — `finish` + the real deploy

```bash
./velocidad -s spanish finish
```

Logs whether you deployed in the real world today. That question is the entire point of the
system — the session was rehearsal for an exchange with reality: the Spanish order at the counter,
the precise term in the code review, the position argued on its merits, the warm boundary on the
phone call. If the answer is "no" too many days in a row, shrink the deploy until it's unavoidable
(one sentence counts), not the study time.

---

## The week (one sitting, ~30–45 min — pick a fixed day)

```bash
./velocidad stats                        # 1. read the instruments, all studies
./velocidad -s <study> stats             # 2. detail on your active studies
./velocidad -s <study> coach             # 3. → paste into agent mode
./velocidad -s <study> recall            # 4. blurt one big topic; card the misses
```

1. **`stats`** — three questions: Is recall trending up? Is the "3 solid" calibration row ≥85%
   (if not: you're overconfident — run more `--calibrate` sessions and slow down before the
   reveal)? Are there leeches?
2. **`coach`** — emits a prompt built from *your* failing data: leeches to re-encode, weak domains
   to drill, your latest friction. Paste it into agent mode and do what it says: the agent rewrites
   the failing cards smaller and sharper, you enter them via `add`, and you **delete the originals**
   it lists. Re-encoding beats re-grinding, every time.
3. **`recall`** — one free-recall round per active study. Misses become cards immediately.
4. **Interrogator** (distributed-systems) — take the weakest domain `stats` showed and run
   `distributed-systems/prompts/interrogator.md` on it: teach it, survive the why/when/compare
   probes, card exactly where you broke. ~20 minutes, once a week, on one topic only.
5. **Meta-observer** — paste the week's friction logs + the study's `meta-observer.md` into agent
   mode. It answers the only weekly question that matters (*did I deploy more this week than
   last?*) and sets next week's scenario rotation.
6. Add one line to your weekly scorecard. Thirty seconds; do it while the meta-observer output
   is in front of you.

---

## Cert prep (per-scenario decks)

Cert scenarios (e.g. `aws-saa-c03`) carry their **own** deck at
`distributed-systems/scenarios/<name>/srs/`, separate from the main study deck and on its own
review clock:

```bash
./velocidad -s distributed-systems srs --scenario aws-saa-c03      # review the cert deck
./velocidad -s distributed-systems add --scenario aws-saa-c03      # bank gaps from a practice test
./velocidad -s distributed-systems stats                           # cert-deck history is included here
```

After a practice exam, treat the score report as a session: distill the misses, `add` them to the
scenario deck, and let `coach` pick up whatever keeps failing.

---

## Which tool, when

| Symptom | Tool |
|---|---|
| It's morning | `daily` |
| New gap discovered (session, meeting, practice test) | `add` — same day, while it's hot |
| A card failed once or twice | Nothing. That's Leitner working. |
| The same card keeps failing (a leech in `stats`) | `coach` → rewrite the card, delete the original |
| Cards pass but the topic feels thin / I couldn't survey it | `recall` on its bank section |
| Survives recall but I can't defend it under follow-ups | `interrogator` (distributed-systems) — Feynman mode |
| A whole domain is weak in `stats` | `coach`, or a session targeted at that domain |
| My "solid" cards keep failing | More `--calibrate` reps; pause before the reveal |
| Tight on time, want raw production volume | `blitz` (spanish / philosophy) |
| Just had a REAL exchange (call, review, debate) | The study's `distiller.md` on your raw notes |
| It's the weekly sitting | `stats` → `coach` → `recall` → meta-observer |
| Everything passes everywhere | You're under-deploying. Go use it in a real room today. |

---

## Command cheat sheet

```bash
# Daily
./velocidad daily [--calibrate]                  # interleaved review, ALL studies
./velocidad -s <study> start [--scenario X]      # morning routine + session scaffold + master prompt
./velocidad -s <study> finish                    # deploy log + next steps
./velocidad -s <study> add [--scenario X] [--box N]   # format-checked card capture

# Drills
./velocidad -s <study> srs [--box N] [--scenario X] [--calibrate]
./velocidad -s <study> blitz                     # 5-min rapid production
./velocidad -s <study> recall                    # free-recall from the banks

# Instruments & maintenance
./velocidad status                               # dashboard, all studies
./velocidad stats                                # analytics summary; -s <study> for detail
./velocidad -s <study> coach                     # re-encoding prompt from your own data
./velocidad -s <study> prompt [--scenario X] [--level LN]   # print the master prompt

./start-dashboard.sh                             # rich TUI (browsers for library/banks/scenarios)
```

Agent prompts, per study, in `<study>/prompts/`: `master` (the daily session), `distiller` (raw
notes → friction + cards), `srs-generator` (friction → cards), `meta-observer` (weekly),
plus `session-runner`/`session-planner` (Spanish) and `interrogator` (Distributed Systems).

---

## The rules that keep it honest

1. **Out loud or it didn't happen.** Every drill in this system is a production drill.
2. **Sessions are WORM.** Never edit a past `transcript.md`. Banks and `meta/` files are living.
3. **Grade against production, not recognition.** "I'd have known it if…" is an `n`.
4. **Leeches get rewritten, not re-ground.** A card failing 3+ times is a card-authoring bug.
5. **The streak serves spacing; it is not a product.** Miss a day, resume — no junk reviews.
6. **Instrumentation is not the scoreboard.** `stats` can be all green while you learn nothing
   real. The scoreboard is the one metric: more real deploys this week than last.
