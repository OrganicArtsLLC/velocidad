# 002 — Agreement is a dial you size, not a switch you flip

**Cluster:** Foundational trade-offs

## The principle

The first principle made the trade sound binary — consistency or availability, pick one. That is only
true at the extremes. Agreement is actually a *quantity you can size*. You decide how many copies must
acknowledge a write before it counts, and how many you check before you trust a read. Those two
numbers are the dial. The binary choice is just the dial pushed all the way to one end.

Once you can see the dial, you stop choosing between two philosophies and start tuning one number per
workload: cheap fast writes here, guaranteed-latest reads there, same system, different settings.

## Picture it

The catalogue now lives in three buildings, all holding copies, with a rule on the wall: every change
must be signed into the logbooks. Two numbers govern everything — how many logbooks must sign before a
change counts, and how many you check before you trust an answer. Sign one and check one, and the
building you wrote to and the building you read from may never be the same one; the reader sails right
past the new record.

## Why it must be true

It is counting and the pigeonhole principle. Call the total number of replicas **N**. Require a write
to be acknowledged by **W** of them, and a read to consult **R** of them. If **R + W > N**, then the
set of replicas you read from and the set you wrote to cannot be disjoint — they must share at least
one replica, and that shared replica holds the newest write. The overlap *is* the guarantee. No
overlap, no guarantee.

Worked: N=3, W=2, R=2. Since 2 + 2 > 3, the read set and write set overlap, so a read always observes
the latest acknowledged write. Slide W down to 1 and reads must rise to 3 to keep the guarantee — the
cost does not disappear, it moves from the write side to the read side. (The strict-quorum condition
also wants **W > N/2**, so two concurrent writes can't both succeed without overlapping; in the
example, W=2 satisfies it.)

This same overlap buys partition tolerance. With N=3, W=2, R=2, lose one replica to a partition: a
write still finds its two acks among the two survivors, a read still finds its two, and 2 + 2 still
clears 3, so the guarantee holds with a node down. A quorum is not only a consistency knob; it is how
you keep answering *and* stay correct while one replica is unreachable. The storm of 001 and this dial
are the same mechanism seen from two angles.

## The trade-off

Turning the dial up (large R and W) buys agreement and pays in latency and reduced availability — more
replicas must respond before you proceed, so a slow or missing node stalls you. Turning it down buys
speed and availability and pays in staleness. There is no setting that is simultaneously fast,
always-fresh, and available under partition; you are distributing one fixed cost across the read side
and the write side.

## Names you'll meet

- **Quorum** — a required overlap between the write set and the read set.
- **R + W > N** — the exact condition for that overlap. The dial's setting.
- **Strong (quorum) read vs eventual read** — the quorum read is guaranteed-latest and more expensive;
  the eventual read consults fewer replicas, is cheaper, and may be stale.
- **Consistency level** — in Dynamo-style stores, the same R/W knob exposed per request (e.g. `ONE` /
  `QUORUM` / `ALL`).
- **Tunable consistency** — the general idea that R and W are configuration, not architecture.

## Connects to

- **Back → 001 (the storm).** The binary trade is this dial at its extremes — availability is the dial
  down, strong consistency is the dial up.
- **Forward → 003 (just enough agreement).** You almost never want the dial maxed everywhere; the next
  principle is how to spend it sparingly.
- **Forward → 025 (consensus).** A quorum decides if a *single* read is fresh; consensus is how a group
  agrees on an *ordered sequence* of writes — quorums are a building block of it.

## Drill prompts

- Agreement between replicas isn't binary — what is it, and which two numbers set it? *(A dial: W write
  acks and R reads-consulted, out of N replicas.)*
- Why does R + W > N guarantee a read sees the latest write? *(The read set and write set must overlap
  by at least one replica, which holds the newest acknowledged write.)*
- Show how a quorum keeps you both correct and available when one of three replicas is partitioned
  away. *(W=2, R=2 still find their quorums among two survivors, and 2+2 > 3 keeps the overlap.)*
