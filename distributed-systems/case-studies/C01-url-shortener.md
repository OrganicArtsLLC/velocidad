# C01 — Designing a URL Shortener

**Headline principles:** 001, 002, 004, 006, 007, 008, 009, 013, 014, 021

---

## The system

Take a long URL, return a short code; given the short code, redirect to the long URL.

## Requirements

- **Functional:** `create(longURL) → shortCode`; `redirect(shortCode) → longURL`.
- **The scale that makes it hard:**
  - *Wildly read-heavy* — each link is created once and may be clicked thousands of times (on the order
    of 1000:1 reads to writes).
  - *Low-latency redirects* — nobody waits on a redirect.
  - *High availability* — a dead shortener breaks every link ever made, not one page.
  - *Effectively permanent* data; *simple* access (lookup by key, no complex queries).

## The shape

A huge pile of tiny, key-based, read-dominated lookups with a trickle of writes. No joins, no reports.
That shape chooses the architecture.

## The design walk

1. **Storage → key-value, availability-leaning.** A pure `code → URL` lookup at scale, where a new link
   being readable a second later is fine → a key-value store, eventual consistency. *(002 — match the
   store to the access pattern; 001/002 — turn the dial toward availability.)*
2. **Read path → cache hard.** A few links get most of the clicks — enormous repetition → an in-memory
   cache in front; huge hit rate, the database barely feels it. *(004 — the cache bet.)*
3. **Edge.** Redirects are global and cacheable → push the hot mappings toward a CDN. *(006 — latency is
   distance.)*
4. **App tier → stateless scale-out.** The redirect holds no per-user state → many stateless servers
   behind a load balancer, auto-scaled. *(007 scale-out, 008 statelessness, 009 elasticity, 021
   pay-per-use.)*
5. **Availability → independent failure domains.** A broken link is a broken promise to the whole
   internet → every layer spans independent zones. *(013 blast radius, 014 availability product /
   independence.)*

## The hard part — key generation

Hashing the URL and truncating risks **collisions** (two URLs hash to one code, and one overwrites the
other). Instead, keep an ever-increasing **counter** and encode it in **base-62** (0–9, a–z, A–Z): a
never-repeating counter never collides, and six base-62 characters already cover ~56 billion codes
(62⁶ ≈ 5.68 × 10¹⁰). A single global counter would be a bottleneck and a single point of failure, so
hand each server a **pre-allocated block** of numbers; it issues codes from its block with no
coordination on the hot path. *(013 — no single point of failure, no shared fate on the hot path.)*

> Idempotency footnote: if "same long URL → same short code" is required, dedup on create (look up an
> existing mapping first). *(012.)*

## The principle map

| Design decision | Principle(s) |
|-----------------|--------------|
| Key-value store, eventual consistency | 001, 002 |
| Cache in front of the database | 004 |
| Push redirects to the edge | 006 |
| Stateless redirect tier behind a load balancer | 007, 008 |
| Auto-scale the tier / pay for use | 009, 021 |
| Independent failure domains for availability | 013, 014 |
| Distributed base-62 counter (no single point of failure) | 013 |
| Dedup identical URLs (optional) | 012 |

## Concrete building blocks

- **Mappings:** a managed key-value store keyed on `shortCode`.
- **Redirect tier:** stateless compute behind a load balancer (containers, or functions for a serverless
  variant).
- **Cache:** an in-memory key-value cache (e.g. Redis or Memcached) in front of the store.
- **Edge:** a CDN for the hot, cacheable redirects.
- **Counter:** a key-generation service handing out base-62 ranges.

## What this case teaches

The cheapest systems are the ones whose *shape* matches a simple component. A read-dominated key lookup
wants exactly: key-value store, cache, edge, stateless fleet. The only real engineering is generating
keys without a bottleneck — solved by handing out ranges so the hot path needs no coordination.
