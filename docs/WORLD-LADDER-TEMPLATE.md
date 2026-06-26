# World / Scenario Ladder Template

Use this template to create a new scenario file for any Velocidad domain.

Scenario files live in `{domain}/scenarios/` or `worlds/` and define a single real-world
deployment context: where you'll practice, what success looks like at each level, and what
vocabulary/structure is specifically needed for that context.

Name files with a short, memorable slug: `mcdonalds.md`, `client-standup.md`, `job-interview.md`.

---

## Template

---

```markdown
# [Scenario Name]

## What This Scenario Is

[2-3 sentences describing the real-world context. Who are you talking to? Where? What's the
actual transaction or interaction? Be specific about the people and situations you actually face.]

## Why It Matters

[Why is this the right place to practice? What's the stake? What happens if you freeze?
What's the win condition?]

## The L1-L5 Ladder

Progress in this scenario follows five levels. You move up when you can **reliably** perform the
current level under actual pressure — not when you can do it in a practice session with notes.

### L1: Survival

**Success definition:** I can complete the fundamental transaction without it breaking down.

**What I can do at L1:**
- [Primary functional output — ordering, greeting, closing a ticket, answering a question]
- [Secondary functional output]
- [Recovery: if I don't understand, I can signal that clearly]

**What I cannot do yet at L1:**
- [Off-script extension — any variation from the core transaction fails]
- [Small talk — I can't sustain anything beyond the core task]

**Essential vocabulary for L1:**
- [Core term 1]
- [Core term 2]
- [Core term 3]
- (Keep to 8-12 items maximum)

**Session goals at L1:**
- Complete the transaction three times in a row without a freeze
- Understand the NPC's responses well enough to know if I succeeded
- Use the repair phrase at least once ("¿Me lo puede repetir?" or equivalent)

---

### L2: Clarification

**Success definition:** I can ask for help, control the pace, and recover when I don't understand.

**What I can do at L2:**
- [Asking for repetition, slower speech, clarification in the target form]
- [Basic repair sequence: I didn't get that → what does X mean → can you spell that?]
- [Handling one unexpected response from the NPC without the transaction breaking]

**What I cannot do yet at L2:**
- [Real-time variation — I still need the conversation to stay close to the expected script]

**Additional vocabulary for L2:**
- [Repair phrase 1]
- [Repair phrase 2]
- [Clarification phrase]

**Session goals at L2:**
- Use a repair phrase naturally (not as a script recitation)
- Handle one curveball from the NPC
- Complete the transaction even when it goes slightly off-script

---

### L3: Small Talk

**Success definition:** I can exchange pleasantries, reference shared context, and leave the
transaction feeling like a brief human connection, not just a function call.

**What I can do at L3:**
- [Greet and be greeted beyond the bare minimum]
- [Reference something observable — weather, busyness, a greeting that invites a response]
- [Exit gracefully with warmth]

**What I cannot do yet at L3:**
- [Sustaining a topic for more than one or two exchanges]
- [Initiating a topic I haven't prepared]

**Additional vocabulary for L3:**
- [Small talk opener]
- [Response to common small talk]
- [Graceful exit phrase]

**Session goals at L3:**
- Add one genuine human moment to the transaction
- Sustain a topic (not just exchange pleasantries and move on) for at least 3 exchanges
- Notice whether the other person is engaging or deflecting

---

### L4: Real Conversation

**Success definition:** I can sustain a topic for several minutes and contribute meaningfully
beyond surface pleasantries.

**What I can do at L4:**
- [Share an opinion or preference]
- [Ask a follow-up question based on their response]
- [Disagree politely or add nuance]
- [Reference something from a previous interaction]

**What I cannot do yet at L4:**
- [Abstract or complex topics — politics, complex feelings, explaining something difficult]
- [Humor that lands in the other language's register]

**Additional vocabulary for L4:**
- [Opinion framing phrase]
- [Agreeing / adding / diverging phrases]
- [Follow-up question openers]

**Session goals at L4:**
- Have a 5-minute conversation about a topic beyond the transaction
- Use at least one sentence that was not prepared beforehand
- Listen well enough to follow up on what they said

---

### L5: Relationship

**Success definition:** This person knows me. I know them. The interaction is genuinely social.

**What I can do at L5:**
- [Be myself — humor, opinions, stories in the target form]
- [Reference shared history]
- [Disagree, joke, or express something emotionally real]
- [Sustain conversation about complex or abstract topics]

**What the relationship feels like at L5:**
- [What does a successful L5 interaction look like? What tangible signal confirms I'm there?]

---

## Cultural/Contextual Notes

[Any domain-specific or cultural context that affects how this scenario works. What are the
unwritten rules? What signals warmth vs. professionalism? What is a faux pas?]

---

## Common Traps

[What goes wrong for learners in this specific scenario? What are the most common freezes,
errors, or avoidance patterns? Document the failure modes here so the agent can watch for them.]

---

## Session Constraints for Agent

[Domain- or scenario-specific rules for the agent beyond the base rules-of-immersion. Examples:]

- NPC speaks at [speed] — don't slow down for learner unless they use repair phrase
- NPC is [friendly/formal/rushed/patient] and should stay in character
- Introduce [specific unexpected element] to trigger the L2 repair sequence
- End every session with a moment that requires the learner to extend beyond the transaction
```

---

## Example: Spanish — McDonald's Scenario

See `worlds/mcdonalds.md` in this repository for a complete reference example.

---

## Notes on Progression

- **Move up a level only when you hit consistent success under real pressure**, not practice sessions.
  Real pressure = actual stakes, not simulated.
- **Entry line + goal + exit line** is the minimum for a Level 1 win. Define these clearly.
- **L2 is often where the real work starts.** L1 is survival. L2 is the first time you have to adapt.
- **Sessions at the same level are valuable.** Don't rush. Depth before breadth.

---

*Last Updated: April 10, 2026*
