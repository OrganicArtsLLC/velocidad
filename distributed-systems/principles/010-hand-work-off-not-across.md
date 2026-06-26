# 010 — When work is slow or bursty, hand it off, not across

**Cluster:** Decoupling

## The principle

When one step is slow, or work arrives in bursts, making the caller wait for it is fragile in two ways:
a single slow item freezes everyone behind it, and a flood that arrives faster than you can serve has
nowhere to go but the floor. The fix is to put a buffer between the thing that creates work and the
thing that does it, so each runs at its own pace.

That one buffer buys two distinct things. It decouples the two sides *in time* — the producer drops the
work and moves on, never blocked by the consumer. And it *levels load* — a spike that would crush the
consumer becomes a queue that lengthens and then drains. You give up the instant answer; you get
survival in return.

## Picture it

The coffee shop. You don't stand at the register while your drink is made — the cashier writes your
name on a cup and puts it in a line for the baristas. You step aside; the register keeps moving. The
baristas pull cups at their own pace and call your name when it's done. Without that line, one slow
drink jams the whole register, and a morning rush bounces customers off a wall. With it, the flood
becomes a backlog — held safely, drained steadily.

## Why it must be true

A synchronous call binds producer and consumer into one timeline and one fate: the producer's
throughput is capped by the consumer's slowest moment, and a consumer outage propagates straight back
to the producer. Inserting a queue breaks both bindings. Temporally, the producer's only job is to
enqueue — a fast, bounded operation — so its latency no longer tracks the consumer's. Under load, the
queue acts as a shock absorber: the arrival rate can briefly exceed the service rate without loss,
because the backlog stores the difference (this is load leveling). The costs are real and worth naming:
added end-to-end latency, results that are *eventual* rather than immediate, and the need to handle
messages that never succeed — which get shunted to a **dead-letter queue** so one poison item can't jam
the line forever.

## The trade-off

A queue buys time-decoupling and burst absorption, and pays in latency (the result is no longer
immediate), in eventual-not-synchronous semantics (the caller must be built to not expect an answer
now), and in new operational surface: queue depth to monitor, redelivery to handle, dead letters to
triage. Note also that a queue *bounds* a burst into a backlog but does not create capacity — if the
average arrival rate exceeds the average service rate, the backlog grows without bound and you must
scale consumers (queue depth is a natural signal for 009).

## Names you'll meet

- **Queue** — the buffer between producer and consumer.
- **Producer / consumer** — the two sides the buffer decouples.
- **Asynchronous** — the producer doesn't wait for the work to finish.
- **Load leveling / buffering** — a spike becomes a backlog instead of a collapse.
- **Dead-letter queue (DLQ)** — where repeatedly-failing messages go so they don't block the line.
- **Backpressure** — signaling upstream to slow down when the queue is filling faster than it drains.

## Connects to

- **Back → 007–009 (spreading the work).** That wing made the *workers* scale; this one protects them —
  the queue lets an elastic fleet drain a burst instead of being crushed by it.
- **Forward → 011 (pub/sub).** A queue is one producer to one consumer pool (point-to-point). When
  *many* parties care about one event, you need a different shape — broadcast.
- **Forward → 012 (idempotency).** The moment you hand work off through a buffer, you lose the certainty
  of a direct reply — which is the bill 012 pays.

## Drill prompts

- When a step is slow or bursty, what do you do, and what two things does it buy? *(Put a queue between
  producer and consumer; it decouples in time and levels load — a spike becomes a backlog.)*
- What does a queue trade away for that resilience? *(Immediacy — results become eventual, not instant —
  plus added latency and operational surface.)*
- Does a queue add capacity? *(No — it bounds a temporary burst; if average arrival exceeds average
  service rate, you must scale consumers.)*
