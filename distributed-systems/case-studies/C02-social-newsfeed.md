# C02 — Designing a Social Newsfeed

**Headline principles:** 001, 002, 004, 007, 010, 011, 022

---

## The system

Users post; users follow each other; each user's feed shows the recent posts of everyone they follow,
newest first.

## Requirements

- **Functional:** `post(user, content)`; `follow(a, b)`; `getFeed(user) → recent posts of followees,
  newest first`.
- **The scale that makes it hard:**
  - *Read-heavy* — people scroll far more than they post; the feed must load fast.
  - *Wildly uneven follower counts* — most users have hundreds; a few have tens or hundreds of millions.
    This asymmetry is the whole problem.

## The shape

The essential question is *when you build the feed*: at write time (push the post into every follower's
feed) or at read time (gather followees' posts live when the user opens the app). That one timing choice
is the design.

## The design walk

1. **Fan-out on write (push).** On post, push a copy into each follower's prebuilt feed → instant reads.
   *(011 — pub/sub fan-out; 004 — the prebuilt feed is a cache.)*
2. **Do the fan-out off the hot path.** Post returns immediately; a queue carries the spray-into-feeds
   work → posting always feels instant. *(010 — decouple in time.)*
3. **Eventual consistency is fine.** A post appearing in feeds a second or two later is invisible. *(001,
   002 — dial toward availability.)*
4. **Fan-out on read (pull) — the alternative.** Cheap writes (store once), expensive reads (gather and
   merge live every open).

## The hard part — the celebrity problem

Under pure **fan-out-on-write**, a celebrity with 100M followers turns *one post* into *100M writes* —
write amplification that backs up every queue and melts the system. Pure **fan-out-on-read** for everyone
instead makes the *common* case (normal feed loads) slow to protect the *rare* one.

**The hybrid** is the industry answer: **push** for normal accounts (cheap fan-out, instant feeds),
**pull** for the handful of celebrities (skip the write storm; fetch their posts live and merge at read
time). Match the strategy to the *shape of the account* — the same classify-then-match instinct as
pricing the spike differently from the baseline. *(022.)*

## The principle map

| Design decision | Principle(s) |
|-----------------|--------------|
| Push posts into follower feeds (fan-out) | 011 |
| Fan-out via a queue, off the post path | 010 |
| Prebuilt feed served from cache | 004 |
| "Appears a second late" is acceptable | 001, 002 |
| Stateless feed/API tier, scaled out | 007 |
| Hybrid: push normals, pull celebrities | 022 (classify and match) |

## Concrete building blocks

- **Posts and the social graph:** a scalable key-value or wide-column store.
- **Fan-out:** a message queue feeding a pool of workers that write into feed stores.
- **Feeds:** an in-memory store holding each user's prebuilt feed list.
- **Post events:** a pub/sub topic or event bus, so new consumers can subscribe without changing the
  producer.

## What this case teaches

The shortener was a read problem; the newsfeed is a *read-vs-write* war won by choosing *when* to do the
work — and by refusing a single global strategy when the data (follower counts) is wildly uneven. "Both,
matched to the slice" beats "pick one."
