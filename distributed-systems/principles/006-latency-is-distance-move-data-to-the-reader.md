# 006 — Latency is distance; move the data to the reader, not the reader to the data

**Cluster:** Copies & locality

## The principle

Past a certain point, the slow part of a request isn't the computing — it's the *travel*. A perfect
server in one region is still slow for a reader on the other side of the planet, because the request
has to cross an ocean and the answer has to cross back, and the speed of light is not negotiable. You
cannot out-engineer distance.

So you stop trying to. Instead of making the far thing faster, you put a copy of it *near* the reader.
The cheapest, most reliable latency win in all of systems isn't a faster algorithm — it's a shorter
trip.

## Picture it

One library, readers everywhere — Tokyo, Berlin, São Paulo. The Tokyo reader waits not because the
book is hard to find but because the *request itself* is swimming halfway around the planet and back.
So you open a small branch in each city, stocked with copies of the most-asked books. The reader's
question now stops at the nearest branch instead of crossing the ocean. You haven't escaped the cache's
bet — you've made it a hundred times over, in a hundred towns.

## Why it must be true

Network latency has a hard floor set by physics: distance divided by the speed of light in the medium,
plus the delay of every hop in between. No amount of server speed touches that floor; the only lever is
to shorten the distance, which means holding a copy close to demand. A **content delivery network
(CDN)** is exactly that — a mesh of caches (**edge locations**) placed near users. A request hits the
nearest edge; a hit answers from next door, a miss makes the long trip to the **origin** once and then
stocks the copy so the next neighbor doesn't pay it.

Because it is still the cache bet (004) under the same invalidation promise (005), the same filter
decides what belongs there. Content **shared across many readers** and **tolerant of slight staleness**
caches beautifully — one edge copy serves a whole city. Content that is **unique per person** or **must
be exact to the second** fails the bet twice (no reuse, no tolerance for stale) and belongs at the
origin. There is also a sibling move: instead of moving a copy of the data to the reader, route the
reader to the nearest *whole system* (latency-based routing). Same principle — close beats far.

## The trade-off

Every edge copy is another replica that can disagree with the origin (the storm of 001, globalized) and
another invalidation promise to keep (005). You trade global consistency and operational simplicity for
dramatically lower read latency on shareable, stale-tolerant content. Pushing the wrong content to the
edge — per-user or must-be-fresh data — pays the consistency cost with none of the latency benefit.

## Names you'll meet

- **CDN** — the mesh of neighborhood caches.
- **Edge location / point of presence (PoP)** — a cache placed close to users.
- **Origin** — the home system the edge falls back to on a miss.
- **Latency-based routing** — the sibling move: send the reader to the nearest region or replica.
- **Static vs dynamic content** — shared and stable content caches at the edge; per-user, fresh content
  does not.
- **Edge invalidation / cache purge** — how you revoke a stale edge copy when the source changes.

## Connects to

- **Back → 004–005 (cache bet + invalidation).** A CDN *is* caching, drawn on a map; it inherits the
  bet (needs reuse) and the promise (needs an invalidation rule).
- **Back → 001 (copies trade agreement).** A hundred edge copies are a hundred more things that can
  disagree with the origin.
- **Forward → 007 (scale out).** This wing moved copies of *data* closer; the next wing multiplies the
  *work* — spreading load across many workers.

## Drill prompts

- When latency is the problem, what's the cheapest lever and why? *(Move the data to the reader —
  distance is the floor and you can't out-compute it.)*
- What content belongs at the edge, and what disqualifies it? *(Shared + stale-tolerant belongs;
  unique-per-user or must-be-exact does not — it fails the cache bet twice.)*
- Why is there a hard floor on latency that faster servers can't beat? *(Propagation delay — distance
  over the speed of light, plus per-hop delay — is physical, not computational.)*
