# 005 — Every copy is a promise to keep it true, and the cost is paid at invalidation

**Cluster:** Copies & locality

## The principle

Making a copy is the easy half, and it's the half that feels like the win. The real work starts the
moment the original changes, because now you owe an answer to a question with no free reply: when do
you stop trusting the copy? Keep it perfectly fresh and you've given back the speed you came for, by
doing work on every change. Let it drift and you're knowingly handing out something old. No option is
both free and fresh.

So the true cost of any copy is not the memory it occupies — it's the *invalidation discipline* it
commits you to forever after. Whenever someone says "just cache it," the honest reply is "and what's
our rule for when it's wrong?" That rule *is* the cost.

## Picture it

A correction slip arrives in the stacks: book seven has a new edition, and the cart still holds the
old one. The librarian has exactly three honest choices. Swap the cart copy the instant the slip lands
(always fresh, but she's running to the stacks constantly again). Put a timer on every cart copy and
toss it after an hour no matter what (simple, but she's knowingly wrong for up to an hour). Or let it
ride and keep handing back whatever's on the cart (fast, but she doesn't even know when she's lying).
Every choice pays somewhere; the only question is where.

## Why it must be true

The copy and the source were equal at one instant and drift apart on the next write. Closing that gap
requires *work*, and the named strategies are just different schedules for paying it:

- **TTL (time-to-live):** the copy self-destructs after a set age. You pre-commit to a maximum
  staleness and do zero per-write bookkeeping. Cheap and openly approximate.
- **Write-through:** update the copy and the source *together*, on every write. The copy never lies,
  but every write pays the tax of touching two places.
- **Write-back (write-behind):** update the copy now, the source later. Writes fly, but a crash before
  "later" loses whatever hadn't synced — speed bought with risk.

There's also *what to evict* when the cache is full (LRU, LFU), and a failure mode that earns its own
name: when many hot copies share one expiry, they all die on the same tick and every reader stampedes
the source at once — a **cache stampede** (thundering herd). The fix is to *jitter* expiries, or let
one request rebuild while others briefly serve the stale value. All of it is the same bill: the cost
of a copy, paid at invalidation.

## The trade-off

You are choosing *where* to pay the freshness cost, not whether. TTL pays in bounded staleness;
write-through pays in slower writes; write-back pays in risk of loss on crash. Tighter freshness always
costs more work or more coupling; looser freshness costs correctness you must prove is acceptable.
There is no strategy that is simultaneously fresh, cheap, and crash-safe.

## Names you'll meet

- **TTL / time-to-live** — a timer capping maximum staleness; the cheap, approximate choice.
- **Write-through** — update copy and source together; always fresh, slower writes.
- **Write-back / write-behind** — update copy now, source later; fast writes, risk of loss.
- **Cache-aside / lazy loading** — the app fills the cache on a miss and invalidates on write.
- **Eviction policy (LRU / LFU)** — what gets dropped when the cache is full.
- **Cache stampede / thundering herd** — many hot copies expire together and a herd hits the source;
  fixed by jittered expiries or single-flight rebuilds.

## Connects to

- **Back → 004 (the cache bet).** The bet only stays profitable with a rule for when to stop trusting
  the copy. This entry is that rule, and its price.
- **Back → 001–003.** Invalidation is the consistency trade-off in work clothes: how stale a copy may
  be is just where you set the dial for that copy.
- **Forward → 006 (CDN).** Push the copy to a hundred cities and you've made this promise a hundred
  times over — invalidation, globally.

## Drill prompts

- When is the real cost of a cached copy paid? *(At invalidation, not creation; the copy is a standing
  promise to keep it true.)*
- Name the three freshness strategies and what each costs. *(TTL — bounded staleness, cheap;
  write-through — always fresh, slow writes; write-back — fast writes, risk of loss.)*
- A hot key expires and the backing store melts on the tick — name it and the fix. *(Cache stampede;
  jitter the TTLs or single-flight the rebuild.)*
