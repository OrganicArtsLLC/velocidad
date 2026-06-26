# 012 — Handing work off trades a certain reply for a possible repeat; make consumers idempotent

**Cluster:** Decoupling

## The principle

The instant you stop handing work *across* (a direct call you watch complete) and start handing it *off*
(a message you drop and leave), you lose certainty. A message can be lost; a confirmation can be lost;
and from the sender's side those two look identical — silence. The only safe response to silence is to
send again, which means some messages arrive twice.

You cannot cheaply guarantee "exactly once" across an unreliable gap, so honest systems choose
*at-least-once*: never lose a message, even if that means occasionally repeating one. That pushes the
responsibility onto the receiver, and the move is not to *prevent* duplicates but to make them *not
matter*. Build the consumer so processing the same message twice has the same effect as once. Then a
repeat is free.

## Picture it

You send the kitchen a ticket — "make one sandwich" — and hear nothing back. Maybe the ticket was lost,
maybe the reply was; you can't tell, so you send it again. How many sandwiches arrive? You don't know —
unless the kitchen was built to notice it already made that exact ticket. When the work was handed
across and watched, the count was certain: exactly one. The moment tickets go in a box, that certainty
is traded away.

## Why it must be true

Across an unreliable channel you pick which failure you tolerate. *At-most-once* (don't retry) never
duplicates but silently drops on failure. *At-least-once* (retry until acknowledged) never drops but can
deliver twice. True *exactly-once delivery* would require perfect, atomic agreement between sender and
receiver across the very network that is failing — which is impractical in general; where systems claim
it, they are doing at-least-once delivery plus deduplication or transactional effects under the hood.
So at-least-once is the default, and correctness moves to the consumer via **idempotency**.

Idempotency means applying the operation twice lands in the same state as applying it once. "Set the
balance to 100" is naturally idempotent; "add 100" is not. The general technique: attach a unique id to
each message and have the consumer record which ids it has already processed, ignoring repeats. The
design rule: assume duplicates will happen and make handling them a no-op — don't bet on the transport
to save you.

## The trade-off

At-least-once buys durability (no lost work) and pays in duplicates the consumer must neutralize.
Idempotency buys safety against those duplicates and pays in extra state and a check on the hot path (a
dedup store of seen ids, kept correct and bounded). Choosing at-most-once instead avoids dedup but
silently loses work — fine for best-effort metrics, fatal for money. Strict ordered, deduplicated
delivery is available in some systems but costs throughput.

## Names you'll meet

- **At-least-once** — never lose; may duplicate. The sane default.
- **At-most-once** — never duplicate; may lose. Fine for metrics, fatal for money.
- **Exactly-once** — what everyone wants; in practice at-least-once delivery plus idempotent processing.
- **Idempotency** — doing it twice equals doing it once; the real defense.
- **Idempotency key / dedup key** — the unique id the consumer checks before acting.
- **Ordered / FIFO delivery** — ordering plus a dedup window, usually at lower throughput than
  best-effort delivery.

## Connects to

- **Back → 010–011 (queue + pub/sub).** This is the bill for both: any time you hand work off through a
  buffer or a topic, delivery is at-least-once and duplicates are on the table.
- **Back → 001–003 (consistency).** Same family of truth: across an unreliable network you can't have
  everything. Name what you actually need and engineer around the gap.
- **Forward → resilience patterns (013–016).** Retries, dead-letter queues, and compensating
  transactions all assume this and build on idempotency.

## Drill prompts

- What do you lose by handing work off, and what's the fix? *(Certainty of delivery; assume at-least-once
  and make the consumer idempotent so a repeat is harmless.)*
- Why not just demand exactly-once from the queue? *(True exactly-once delivery across an unreliable
  network is impractical; "exactly-once" systems are at-least-once + dedup, so correctness still lives
  in the consumer.)*
- A payment service double-charges on a redelivered message — the real fix? *(An idempotency key in the
  consumer — "already processed this id?" — not "make the queue exactly-once.")*
