# Pattern Reference — templates for the design conversation

Reusable templates for *talking through a system design under pressure* — the production skill this
study trains. Master the template, fill in the blanks for any system, and you can walk a design aloud
without freezing. These are the sentence-stems and skeletons; the principles (001–025) are the content
you pour into them.

**How to use:**
1. Read the template skeleton.
2. Run it against a case study you've already studied — say each step aloud.
3. Then run it against a *new* prompt you haven't seen, with a timer.
4. A template is mastered when you can drive a 20-minute design with it and never go blank.

---

## Tier 1 — Core templates (use in every design)

### 1. The opening: requirements before architecture

**Formula:** *Functional requirements → the dimension that makes it hard → scale numbers → explicit
non-goals.*

Never start drawing boxes. Start here:

- "Functionally, the system must: `<verbs the API exposes>`."
- "What makes this *hard* is `<the one dimension>` — is it read-heavy, write-heavy, latency-critical,
  consistency-critical, or bursty?"
- "Roughly what scale: `<reads/sec, writes/sec, data size, users>`?"
- "What are we *not* solving — `<explicit non-goals>`?"

> The whole architecture falls out of the answer to "what makes this hard." Find that dimension first.

### 2. Find the shape: the one question that decides the design

**Formula:** *State the single axis the design turns on, as a question.*

Every canonical design has one pivot. Name it out loud:

- Read-heavy key lookup? → "It's a read problem; cache and edge everything." (C01)
- Read *vs* write with skew? → "When do we build the view — at write or at read time?" (C02)
- The query is a scan? → "The bottleneck is the *data structure*, not scale." (C03)
- Unavoidable per-connection state? → "How do we *contain* state we can't externalize?" (C04)
- Slow/heavy/bursty work? → "Hand it off through a queue; nothing waits." (C05)
- A correctness invariant? → "*Where exactly* must we be strongly consistent, and nowhere else?" (C06)
- Internet-scale work? → "The hard part is *not repeating* work and *not being destructive*." (C07)
- Ordering + correctness on the hot path? → "Does this *invert* scale-out into one sequenced writer?" (C08)

### 3. The design walk: one decision, one principle, one trade-off

**Formula:** *For each component — the decision, the principle it applies, and the cost it accepts.*

Speak each step as a triple, so every choice is justified and its price is admitted:

> "I'll `<decision>`, which applies `<principle NNN>`. The trade-off I'm accepting is `<cost>`."

Examples:
- "I'll put an in-memory cache in front of the store (004); the trade-off is staleness bounded by a TTL
  (005)."
- "I'll make the workers stateless and externalize sessions (008); the trade-off is one extra hop per
  request."
- "I'll book with an atomic conditional write (003); the trade-off is lower throughput on that path,
  which is fine because bookings are rare."

A design narrated as decisions-without-trade-offs is a memorized recipe. Decisions-*with*-trade-offs is
engineering.

---

## Tier 2 — Pressure templates

### 4. Articulating a trade-off (the move interviewers and reviewers reward)

**Formula:** *"Option A buys `<X>` and pays in `<Y>`; option B buys `<Y>` and pays in `<X>`. I choose
`<one>` because the requirement says `<which of X/Y matters here>`."*

Never present a choice as "the right answer." Present it as a trade resolved by *this system's*
requirement. This is the codex's whole thesis (the principles are trades, not rules) spoken aloud.

### 5. Back-of-the-envelope estimation

**Formula:** *users → requests/sec → storage/yr → does one machine do it?*

- Daily actives × actions/day ÷ 86,400 ≈ average requests/sec; multiply by a peak factor (≈ 2–10×).
- Items/day × bytes/item × 365 ≈ yearly storage.
- Compare to a single machine's rough ceiling to decide: one box, or scale out?

Round aggressively. The point is the order of magnitude that tells you *whether you need distribution at
all* — the cheapest system is the one that fits on one box.

### 6. The failure interrogation

**Formula:** *Walk each component and ask "what happens when this dies?"*

For every box you drew:
- "If this node dies mid-request — is the work lost, retried, or duplicated?" (012)
- "If this dependency goes slow — does it cascade?" (timeout / circuit breaker, 015)
- "If this whole zone goes dark — do we stay up?" (independence, 013/014)
- "If this is overwhelmed — does the queue absorb it or does it collapse?" (010)

A design isn't done when it works; it's done when you've said how it fails.

### 7. Knowing when to break the rules

**Formula:** *"The usual move here is `<principle>`, but this requirement `<inverts/overrides>` it,
because `<reason>`, so instead I'll `<the inverted choice>`."*

The senior signal is recognizing when a requirement flips the default — strict ordering refusing
scale-out (C08), unavoidable state refusing statelessness (C04), one invariant demanding strong
consistency in an otherwise eventual system (C06). State the rule, then state why *this* problem is the
exception.

---

## Drill loop (how to practice these with the engine)

1. The agent gives you a design prompt (a case study, or a new system).
2. You drive it with templates 1 → 3, narrating decisions as trade-off triples.
3. The agent interrupts with template 6 ("what happens when X dies?") and template 4 ("why not the other
   option?").
4. Capture every place you froze or stated a trade-off backwards — those are your SRS cards.
5. Redeploy on the next prompt; watch the closed gaps hold.
