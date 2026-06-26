# C03 — Designing a Game Leaderboard

**Headline principles:** 001, 002, 004, 007, 008, 010, 011 + data structure

---

## The system

Real-time ranking of millions of players by score: show the top-N, and a given player's own rank.

## Requirements

- **Functional:** `updateScore(player, score)`; `topN()`; `rank(player)`.
- **The scale that makes it hard:** tens of millions of players, constant updates and reads, must feel
  *live* (stale is fine; *slow to answer* is not).

## The shape

The essential difficulty is the **rank query**. In an ordinary table, "what's my rank?" means *count
every player with a higher score* — a full scan, millions of rows, per query. The naïve store makes the
read impossible; the fix is a structure that already knows the order.

## The design walk

1. **Sorted set as the live store.** Keep players in score order *at all times*, maintained on each
   update. Updating a score is cheap; top-N is "read the first N"; rank is a near-instant lookup, not a
   scan. *(Echoes 002 — match the structure to the access pattern — applied to the data structure:
   precompute the order so you never recompute it.)*
2. **In memory for speed.** The leaderboard lives in RAM — it *is* a live read model / cache. *(004.)*
3. **Durable scores behind it.** The authoritative scores sit in a normal database; the leaderboard is
   rebuilt or updated from them.
4. **Fed by a stream.** Score changes arrive as events. *(010 queue / 011 fan-out.)*
5. **Eventual is fine; scale the serving tier.** A half-second of lag is invisible *(001, 002)*; the API
   tier is stateless and scaled out *(007, 008)*.

## The hard part — the rank query

The bottleneck isn't *scale*, it's the *shape of the data*: no amount of caching or scaling rescues a
structure that forces a scan. A **sorted set** (e.g. a Redis sorted set / ZSET) gives O(log n) updates
and rank lookups — it moves the cost from the billions of reads onto the cheap writes by maintaining
order continuously.

## The principle map

| Design decision | Principle(s) |
|-----------------|--------------|
| Sorted set so rank is a lookup, not a scan | data-structure choice (rhymes with 002) |
| Leaderboard in memory (live read model) | 004 |
| Eventual consistency acceptable | 001, 002 |
| Score updates via a stream | 010, 011 |
| Stateless, scaled-out serving tier | 007, 008 |

## Concrete building blocks

- **Leaderboard:** an in-memory store with a sorted-set structure (e.g. Redis sorted sets).
- **Durable scores:** a scalable database of record.
- **Score events:** a stream or queue feeding the leaderboard.

## What this case teaches

Sometimes the bottleneck is neither where data lives nor when work happens, but the *shape* of the data.
The right structure doesn't optimize the hot query — it *deletes* it.
