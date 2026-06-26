# 003 — You don't buy correctness; you buy the cheapest guarantee the story needs

**Cluster:** Foundational trade-offs

## The principle

Strong consistency sounds like the responsible default. It is also the most expensive setting in the
system, and you almost never need it everywhere. The skill is not *getting* strong consistency — it is
naming the smallest promise that keeps the user trusting the system, and buying only that.

Over-buying consistency is a bill you pay forever, on every read, to fix a problem exactly one person
was having for exactly one second. The discipline is to find the specific felt gap and close just that
gap.

## Picture it

A reader changes her address in the east building, drives across town, opens the west building, and
her old address is still showing. The data is not lost — the buildings will sync in a second. But she
does not experience "a sync delay." She experiences being lied to: *I just did that.* That specific
betrayal, and only that one, is what the cheap guarantees exist to fix.

## Why it must be true

The trades from 001 and 002 are paid per read, forever. Cranking the global dial to maximum charges
every reader the quorum tax to fix a gap that only the writer — and only just after writing — actually
feels. Weaker, named guarantees exist precisely because the felt problems are *local and specific*, so
the fix can be local and specific too. You pay for coordination only where a human would otherwise
notice its absence.

The two guarantees that close the gaps people actually feel:

- **Read-your-writes consistency:** you always see your own latest change, even if others see it a
  moment late. Fixes "where did my change go?"
- **Monotonic reads:** once you have seen a value, you never get handed an older one. Fixes "wait, it
  went backwards."

Neither makes the whole system agree. Each closes one felt gap, cheaply. (See the glossary for how
these *session guarantees* sit between strong and eventual consistency, and for the precise meaning of
linearizability, sequential, causal, and eventual consistency.)

## The trade-off

The cheap guarantees buy *perceived* correctness without paying for *global* correctness — but they
are narrower than strong consistency. Read-your-writes does nothing for a *different* user reading
your change; monotonic reads don't stop two users seeing different-but-each-self-consistent values.
When the requirement truly is "all observers agree on one current value," you must pay for the quorum
read (002) or true consensus (025). The error in both directions is a mismatch: over-buying global
strong consistency for a local felt gap, or under-buying when the invariant really is global.

## Names you'll meet

- **Read-your-writes** — the writer always observes their own latest change.
- **Monotonic reads** — a reader never observes time running backwards.
- **Session consistency** — read-your-writes + monotonic reads, scoped to one user's session.
- **Route-read-to-primary** — the practical implementation of read-your-writes: send *this* read to the
  authoritative copy right after a write, while everyone else uses cheap replica reads.
- **Single strong read** — buy a quorum read for just the one request that needs it, not the whole
  table.
- **Replica lag** — the staleness you accept everywhere you did *not* need the guarantee.

## Connects to

- **Back → 002 (the dial).** This is how you spend the dial: not maxed everywhere, but turned up only on
  the specific reads a human would otherwise notice.
- **Back → 001 (the storm).** Together, 001–003 are one arc: the storm forces the choice, the dial sizes
  it, taste spends it.
- **Forward → 004 (caching).** The most aggressive "stale on purpose" trade of all — keep a copy you
  know may be stale right next to the reader, because it is worth it.

## Drill prompts

- What do you actually buy when you "add consistency," and what's the rule for how much? *(The specific
  guarantee the story needs; buy the cheapest one that holds, not global strong consistency.)*
- Name the two cheap session guarantees and the felt problem each fixes. *(Read-your-writes — "where's
  my change?"; monotonic reads — "it went backwards.")*
- A user updates a profile then immediately sees the old version. Cheapest fix vs the trap? *(Route that
  read to the primary / strong-read just that one call; the trap is making the whole table strongly
  consistent.)*
