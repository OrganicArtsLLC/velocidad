# C07 — Designing a Web Crawler

**Headline principles:** 001, 005, 007, 008, 010, 012, 013, 015, 022, 023

---

## The system

Crawl the web: fetch a page, extract its links, follow them, store the content — across billions of pages,
without looping, hammering, or drowning.

## Requirements

- **Functional:** fetch → extract links → enqueue new ones → store content; repeat at internet scale.
- **The traps that make it hard:** don't re-crawl the same page (the web is full of loops); don't hammer
  any one site (politeness); spread the work across many crawlers without collisions.

## The shape

A giant **breadth-first search** over a graph the size of the internet. A BFS centers on a *to-do list* —
here the **frontier**, a queue of URLs to visit. So the system is a stateless fleet eating from one
enormous shared queue: the spreading-the-work + decoupling pattern, very large.

## The design walk

1. **Frontier = distributed queue** of URLs. *(010.)*
2. **Crawler fleet** — stateless, scaled out *(007, 008)*, on cheap interruptible capacity *(022)* — pulls
   URLs, fetches, and parses links.
3. **Dedup before enqueue** — check each discovered URL against a **"seen" set** and drop duplicates. This
   stops the infinite loop. *(012 idempotency / 005 membership; often a bloom filter at scale.)*
4. **Content to cheap durable storage**, tiered down as it cools. *(023.)*
5. **Politeness:** partition the frontier *by domain* and rate-limit per domain, so a thousand crawlers
   never gang up on one site. *(013 — isolation around who you may hammer.)*
6. **Trap survival:** one malicious or broken site (a crawler trap, endless generated URLs) must not sink
   the fleet — bound it, time it out, move on. *(015, 013.)*

## The hard part — dedup at scale

Knowing cheaply whether you've already seen a URL among *billions*. Skip the check and the crawler loops
forever; do it naïvely and the seen-set won't fit in memory. Trade a little precision for a lot of memory:
a **bloom filter** answers "**definitely** not seen" or "**probably** seen" (it has false positives but no
false negatives) — exactly the right trade for a crawler, where a rare false positive just means skipping
one page. *Not re-doing the done* is the real engineering; the to-do list is easy.

## The principle map

| Design decision | Principle(s) |
|-----------------|--------------|
| Frontier as a distributed queue | 010 |
| Stateless, scaled-out, interruptible crawler fleet | 007, 008, 022 |
| Dedup / seen-set before enqueue (bloom filter) | 012, 005 |
| Content storage tiered by age | 023 |
| Per-domain partition + rate-limit (politeness) | 013 |
| Time out / isolate crawler traps | 015, 013 |

## Concrete building blocks

- **Frontier:** a distributed message queue.
- **Seen-set:** a scalable key-value store, or an in-memory bloom filter, for membership checks.
- **Content:** cheap object storage with lifecycle tiering to archival storage.
- **Crawlers:** a stateless fleet on interruptible compute.

## What this case teaches

At internet scale the obvious work (fetching) is trivial; the engineering is in *not repeating it* (dedup)
and *not being destructive* (politeness/isolation) — the queue and isolation principles, very large.
