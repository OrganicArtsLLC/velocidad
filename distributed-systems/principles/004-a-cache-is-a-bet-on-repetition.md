# 004 — A cache is a bet that the recent past predicts the near future

**Cluster:** Copies & locality

## The principle

A cache keeps a copy of an answer close to whoever keeps asking, so you stop paying the full cost of
fetching it. But the copy is frozen at the moment you took it, and the real thing can move on without
telling you. So every time you serve from the cache you are making a wager: that what was asked
recently will be asked again soon, and that the answer hasn't changed in the meantime.

That wager only pays when there is *repetition*. If every request is unique — nothing ever asked twice
— the copy is never reused and you paid to keep it for nothing. The price of the speed is staleness:
you trade "always exactly right" for "usually right, and fast."

## Picture it

The librarian notices the same ten books get requested all day, and each time she walks to the back
stacks to fetch one. So she puts those ten on a cart by the desk and just turns around when someone
asks — seconds instead of minutes. The catch she has accepted: the real book in the stacks could get a
correction slip tomorrow, and her cart copy won't know. Every time she hands over the cart copy she is
betting it's still good enough.

## Why it must be true

Caching works because real workloads are not uniform — a small set of items gets requested far more
than the rest (temporal and popularity locality). A copy near the asker turns a slow, expensive fetch
into a fast, cheap one *for that slice*. The size of the win is exactly the **hit rate**: the fraction
of requests the copy can answer. High hit rate and you've nearly erased the fetch; low hit rate and
you've added a thing to maintain while still fetching.

The catch is structural, not a bug: the instant you hold a second copy of something mutable, the two
can disagree. There is no free, always-fresh copy — freshness costs the work of checking or updating
(that bill is 005). A cache is worth it only when the saved fetches outweigh the staleness you've
agreed to tolerate.

## The trade-off

You are trading freshness and memory for latency and load. The cache adds a component that can be
wrong, can be stale, and must be invalidated; in return it removes most of the read traffic from the
expensive backing store. The bet pays in proportion to repetition and read-heaviness; on unique,
write-heavy, or correctness-critical data it loses on both sides.

## Names you'll meet

- **Cache hit / miss** — whether the answer was already on the cart.
- **Hit rate** — fraction of requests the cache served; the scoreboard for the bet.
- **Locality** (temporal, spatial, popularity) — *why* the bet pays: recent and popular things get
  re-asked.
- **In-memory cache** — the managed cart you put in front of a database (e.g. a key-value store like
  Redis or Memcached).
- **Read-through vs cache-aside** — *who* fills the cache on a miss: the cache itself, or your
  application code.

## Connects to

- **Back → 001–003.** Those were about *agreement* between copies; this wing is about *copies kept
  close*. A cache is the same "extra copy" problem pushed to its most aggressive, deliberately-stale
  extreme.
- **Forward → 005 (invalidation).** The bet only stays profitable if you have a rule for when to stop
  trusting the copy. Making the copy is easy; keeping it honest is the bill.
- **Forward → 006 (locality / CDN).** "Close" generalizes from the front desk to every city — the same
  bet drawn on a map.

## Drill prompts

- What is a cache actually betting on, and what do you pay for the speed? *(That the recent past
  predicts the near future — repetition; you pay in staleness.)*
- What single number tells you whether a cache was worth it? *(The hit rate.)*
- When is reaching for a cache the *wrong* move? *(When requests are unique per call — hit rate near
  zero — or when the data must be exact to the moment.)*
