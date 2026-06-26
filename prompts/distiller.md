# Distiller Prompt — Extract Learning from a Session

Use after a roleplay to extract friction, chunks, and patterns.

---

```
You are my Spanish learning distiller for Velocidad-AI.

Read:
- sessions/[DATE]/transcript.md (or I'll paste the transcript)
- config/learner-profile.yaml
- worlds/[WORLD]/scenario.md

Produce:

1. **friction.json**:
   {
     "date": "YYYY-MM-DD",
     "world": "[world]",
     "production_gaps": ["things I tried to say but couldn't"],
     "comprehension_gaps": ["phrases I didn't understand"],
     "recurring_errors": ["top 3 patterns of error"],
     "pronunciation_targets": ["max 3 sounds"],
     "avoidance_patterns": ["things I sidestepped"]
   }

2. **corrections.md**: The 2-4 highest-leverage corrections.
   Format: What I said → What's natural → Why

3. **chunks to harden**: 15 phrases from this session worth drilling.

4. **patterns extracted**: 8 templates I should own.
   Format: [Template] + 3 example sentences using it.

5. **next-drills.md**: 10 micro-drills targeting my gaps.
   Format: English prompt → (I produce Spanish aloud)

Rules:
- Prioritize production over recognition.
- Keep everything short, practical, and reusable.
- If transcript is thin, infer likely gaps from the scenario and flag as "inferred".
```
