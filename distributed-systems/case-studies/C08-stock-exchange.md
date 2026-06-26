# C08 — Designing a Stock Exchange (the finale)

**Headline principles:** 001, 002, 003, 007 (inverted), 010, 011, 012, 014, 025 — and **event sourcing**

---

## The system

A matching engine: accept buy/sell orders, match them by price-time priority, confirm fills — with
microsecond latency, strict ordering, perfect correctness, and a complete audit trail.

## Requirements

Every one is non-negotiable: **ultra-low latency**; **strict ordering** (price-time priority — fairness is
the law); **absolute correctness** (no lost or duplicated trades); a perfect **audit trail**; **high
availability**.

## The shape — where the principles invert

Two requirements are at war with everything the earlier clusters preached. **Strict ordering** and
**perfect correctness** hate distribution: spread the matching across machines and you inherit the storm
(001) — they disagree on order, and "who was first" becomes ambiguous, which in a market is illegal. So the
hot path inverts the scale-out instinct: it wants to be a **single, deterministic, in-memory engine**
processing one strictly-ordered stream. Not a fleet. One sequenced writer.

## The design walk

1. **A sequenced, append-only log is the source of truth.** Every order is appended in strict order —
   **event sourcing**: store the ordered *events*, not the current state; the state is the replay. The log
   gives *ordering* (a sequence by definition), the *audit trail*, and *replayability*.
2. **The matching engine consumes the log in order, in memory, on one machine** — blindingly fast and
   *deterministic*: same log in → same trades out, every time.
3. **High availability by replication, not sharding.** Replicate the log to standby engines that replay the
   *same* sequence into the *same* state; if the primary dies, a replica — already identical — takes over.
   Agreeing on that one ordered log across replicas is **consensus** (025); determinism + a consensus-
   replicated log buys availability *without* sacrificing ordering. *(001, 014, 025.)*
4. **Async, eventually-consistent periphery.** Settlement, portfolios, notifications, and market-data feeds
   are fed asynchronously from trade events *(010, 011)*, built as eventually-consistent read models (CQRS,
   002), idempotent *(012)*. Strict core; relaxed, large periphery.

## The hard part — knowing when to break your own rules

The difficulty is *judgment*, not technology. The earlier clusters screamed "distribute, scale out, never
trust one machine"; correctness here screams the opposite — "one deterministic sequencer, or you lose
ordering." The master move is recognizing that this requirement *inverts* the usual principle, and reaching
for replication-of-a-deterministic-log (consensus over the ordered events) to recover the availability you
gave up.

## The principle map

| Design decision | Principle(s) |
|-----------------|--------------|
| Sequenced append-only log = source of truth | event sourcing (ordering + audit + replay) |
| Single in-memory deterministic matching engine | **007 inverted** (refuse scale-out for the hot path) |
| HA via consensus-replicated log to standby replicas | 001, 014, 025 |
| Strong consistency on the match | 003 |
| Async downstream (settlement, feeds) | 010, 011 |
| Eventually-consistent read models (portfolios) | 002 |
| Idempotent order handling | 012 |

## Concrete building blocks

- **Order log:** a strictly-ordered, replicated append-only log (a consensus-backed log or ordered stream).
- **Engine:** low-latency, in-memory compute (co-located, fast networking) running deterministic matching.
- **Downstream:** databases and streams feeding eventually-consistent read models for settlement and feeds.

This design is more architectural than a pick of off-the-shelf services — the lesson is the *shape*, not
the products.

## What this case teaches — the thesis

A URL shortener (C01) and a stock exchange (C08) could not be more different, yet both are built from the
same two dozen-plus trades — recombined, and here *inverted*. The principles are **trades, not rules**;
mastery is knowing which trade each problem demands, even when it's the opposite of the last one. The
product names are weather; the trades are physics. That recognition is the whole point of the codex.
