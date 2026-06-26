# 015 — Treat a dependency's failure as the normal case: fail fast, retry with jitter, stop hammering the dead, degrade

**Cluster:** Resilience

## The principle

A dependency will fail, and usually it fails by going *slow* before it goes *dead* — it doesn't refuse
your call, it just never answers. If your code waits on it, the dependency's sickness becomes yours:
callers pile up waiting, their callers pile up behind them, and a healthy system is paralyzed by one
silent failure. The naïve virtues make it worse — "wait a little longer" freezes you, "try again
immediately" stampedes the thing that's already drowning.

So you replace instinct with discipline. Never wait forever (timeout). Retry, but back off and add
randomness so retries don't synchronize into a flood. Once something is clearly down, stop calling it
for a while (circuit breaker), giving it room to heal. And serve a reduced answer rather than no answer
(graceful degradation).

## Picture it

One supplier goes dark, and every clerk who needs them stands frozen, holding a dead phone line, waiting
— and the readers in front of those clerks wait too. The paralysis spreads backward through the whole
library from one silent phone. "Wait longer" is how a clerk gets frozen; "call again right now," times a
thousand clerks, is how the supplier never recovers. The cure is bounded waits, spaced retries, knowing
when to stop dialing, and handing the reader a cached answer instead of nothing.

## Why it must be true

Waiting threads and connections are finite; a slow dependency consumes them and the caller runs out,
which is how a downstream slowdown becomes an upstream outage — a *cascade*. The four moves each cut one
path of that cascade:

- **Timeout** caps how long any one call can tie up a resource — no infinite waits, no freeze.
- **Retry with exponential backoff + jitter** recovers from transient faults without synchronizing into
  a thundering herd; the jitter de-correlates retries (the same anti-stampede trick as TTL jitter, 005).
- **Circuit breaker** trips after repeated failures and fails *fast* for a cooldown, so you stop spending
  resources on a corpse and stop preventing its recovery; it then probes and closes when healthy.
- **Graceful degradation** keeps the critical path alive by dropping or substituting non-critical
  dependencies (a cached value, a default, "back soon").

Together they treat failure as expected and *contained*, not exceptional and *contagious*.

## The trade-off

These patterns buy isolation from a failing dependency and pay in complexity and correctness care.
Timeouts too tight abandon calls that would have succeeded; too loose, they don't protect you. Retries
risk duplicating work, so they are only safe when the operation is idempotent (012). A circuit breaker
trades some availability during its open window (it fails fast even calls that might have worked) for
the dependency's chance to recover. Graceful degradation trades feature completeness for staying up.

## Names you'll meet

- **Timeout** — a cap on how long you'll wait; never infinite.
- **Retry with exponential backoff + jitter** — retry transient faults without a synchronized stampede.
- **Circuit breaker** — stop calling a clearly-down dependency, fail fast, then probe.
- **Graceful degradation / fallback** — serve a reduced answer rather than nothing.
- **Fail fast** — return quickly on failure instead of hanging.
- **Bulkhead** — isolate the resources (pool, threads) a failing dependency can consume (see 013).

## Connects to

- **Back → 013 (blast radius).** Timeouts and circuit breakers are fire doors drawn around a slow
  dependency — containment at the call level.
- **Back → 005 (TTL jitter).** Backoff jitter is the same de-correlation trick that fixes cache
  stampedes — desynchronize the herd.
- **Back → 012 (idempotency).** Retries are only safe if the operation is idempotent; 013–015 lean on
  012.
- **Forward → 016 (disaster recovery).** These handle the *small* failures; DR handles the total ones you
  can't fail-fast through.

## Drill prompts

- A dependency fails — what four moves keep its failure from becoming yours? *(Timeout; retry with
  backoff + jitter; circuit breaker; graceful degradation.)*
- Why is an immediate retry loop dangerous? *(It stampedes an already-overloaded dependency — a retry
  storm; back off and jitter instead.)*
- Why are retries unsafe without idempotency? *(A retried-but-actually-succeeded call repeats the
  side effect; idempotency makes the repeat a no-op.)*
