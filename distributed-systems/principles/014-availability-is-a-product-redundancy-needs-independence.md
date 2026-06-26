# 014 — A system is only as available as the product of its dependencies; redundancy needs independence

**Cluster:** Resilience

## The principle

When a system needs several things working *at once* to function, their availabilities don't average —
they multiply. Five dependencies at 99% each yield about 95% together, because all five must hold
simultaneously. Every dependency you add *in series* is a tax that can only drag the total down. So the
first lever is to depend on fewer things.

The second lever is redundancy — with a sharp condition. Two copies of something raise availability only
if they fail *independently*. Redundancy where both copies share a single point of failure (the same
power feed, the same zone, the same deploy) is a fiction: one event takes both, and your "parallel" is
secretly "series." Independence is the entire game; correlated failure is its silent killer.

## Picture it

The library opens only if the door unlocks AND the lights come on AND the catalogue boots AND staff show
up AND the network is alive — five things, each up 99% of the time. To be open you need all five at
once, so you multiply: ~95%, a whole month a year you didn't budget for. And the "two backup generators"
you trusted? Both wired to the same fuse box — the fuse blows, both die, the redundancy was never real.

## Why it must be true

Two ways components combine, opposite arithmetic. **In series** (you need *all* of them): availability is
the product of each, so it only falls as you add links — 0.99⁵ ≈ 0.951. **In parallel** (you need *any
one*): the system is down only if *every* copy is down, so you multiply the *failure* probabilities —
two 99% parts give 1 − (0.01)² = 0.9999, and availability climbs.

The catch lives entirely in the word "independent." Multiplying failure probabilities assumes the copies
can't fail together. The moment they share a fate — a power source, a region, a release, a shared
dependency — that assumption breaks and the parallel collapses back toward series. This is why serious
redundancy is built on *physical* separation (separate facilities with separate power and network): you
are not just buying a second copy, you are buying an *uncorrelated* one. (Adding "nines" gets ~10× harder
each step: 99.9% ≈ 8.8 h/yr down, 99.99% ≈ 53 min/yr, 99.999% ≈ 5 min/yr.)

## The trade-off

Redundancy buys higher availability and pays in cost and complexity (you run and pay for spare capacity
that mostly sits idle), and only delivers its math if you also pay for genuine independence —
geographically and operationally separated copies, which are more expensive and harder to keep in sync
than co-located ones. Shortening the dependency chain buys availability and may cost features or
flexibility you were getting from those dependencies.

## Names you'll meet

- **The nines** — availability as 99.9%, 99.99%, …; each nine roughly 10× less downtime.
- **Availability in series vs parallel** — needed-all multiplies down; any-one multiplies up.
- **Redundancy** — a spare copy so one failure isn't fatal.
- **Single point of failure (SPOF)** — a dependency with no independent backup.
- **Correlated failure** — copies that share a fate and die together.
- **Cross-zone / cross-region standby** — redundancy made independent by physical separation.

## Connects to

- **Back → 013 (blast radius).** Containment limits how far a fault spreads; this principle is how you
  stay *up* through it — with independent spares — and the math of why it works.
- **Back → 007 (scale out).** Scaling out already gave you many workers; independence is the condition
  that turns "many workers" into "higher availability" rather than just "more capacity."
- **Forward → 016 (disaster recovery).** When even independent redundancy isn't enough (a whole region),
  you *bound the loss* instead.

## Drill prompts

- How do the availabilities of needed dependencies combine, and what's the implication? *(They multiply
  in series, so each one lowers the total; shorten the chain and add independent redundancy.)*
- When does adding a redundant copy *not* help? *(When it fails in correlation with the original — shared
  power, zone, or deploy; independence is required.)*
- Two servers placed in the same failure domain "for redundancy" — the flaw and the fix? *(Shared fate;
  put the second copy in an independent failure domain.)*
