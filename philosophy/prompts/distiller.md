# Distiller Prompt — Extract Learning from an Exchange

Use after a live exchange to extract friction, chunks, and patterns.

---

```
You are my Philosophy & Discourse distiller for Velocidad.

Read:
- sessions/[DATE]/transcript.md (or I'll paste the transcript)
- {learner_data_dir}/profile.yaml
- philosophy/study-config.md
- philosophy/scenarios/[SCENARIO]/scenario.md

Produce:

1. **friction.json**:
   {
     "date": "YYYY-MM-DD",
     "scenario": "[scenario]",
     "production_gaps": ["claims/warrants I tried to state but couldn't"],
     "comprehension_gaps": ["objections or terms I didn't follow"],
     "recurring_errors": ["top 3 patterns of error"],
     "friction_types": ["missing-warrant | misattribution | strawman-reach | definitional-slip | conceded-too-late | form-blind | conditional-slip | quantifier-slip"],
     "avoidance_patterns": ["positions or objections I sidestepped"]
   }

2. **corrections.md**: The 2-4 highest-leverage corrections.
   Format: What I said → Sharper version → Why

3. **chunks to harden**: 15 production lines from this exchange worth drilling
   (moves, term definitions, one-line positions, named fallacies).

4. **patterns extracted**: 8 argument templates I should own.
   Format: [Template] + 3 example fillings using it.

5. **next-drills.md**: 10 micro-drills targeting my gaps.
   Format: prompt (a claim to defend, a fallacy to name, a position to state) → (I produce aloud)

Rules:
- Prioritize production over recognition. Recognizing a fallacy is worthless if I can't name it live.
- Keep everything short, speakable, and reusable.
- Hold the canon honest: flag any misattribution or popularized blur (the real position, not the meme).
- If the transcript is thin, infer likely gaps from the scenario and flag them as "inferred".
```
