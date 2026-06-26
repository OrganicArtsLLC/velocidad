# 009 — Capacity is a living set; size it to demand and route only to the living

**Cluster:** Spreading the work

## The principle

A fixed number of workers is wrong almost all the time — too many when it's quiet (paying for idle),
too few when it counts (the queue collapses). Demand breathes, so capacity should breathe with it: add
workers when load rises, remove them when it falls. You stop sizing for the peak and start sizing for
now.

And spare capacity is worthless if you keep handing work to something that's broken. A worker can be
"running" and yet serving no one. So the second half: something must continuously check who is actually
alive and route only to those, replacing the ones that aren't. Redundancy without failure *detection*
is theater.

## Picture it

Three in the morning, the library is empty and ten librarians stand idle at ten desks. Noon, the line's
out the door and there are still only ten. Meanwhile a clerk quietly faints behind a desk — slumped,
silent — while the door person, not noticing, keeps cheerfully sending people to them. A fixed roster
fails both ways at once: wrong size for the crowd, and blind to the dead.

## Why it must be true

Two independent failures, two mechanisms. *Elasticity* couples the worker count to a live demand signal
(queue length, CPU, request rate): cross a threshold and the fleet grows; fall below and it shrinks.
This tracks cost to usage and keeps latency stable across the swing. *Health checking* has the
dispatcher continuously probe each worker and remove from rotation any that fail to respond correctly;
a new worker only joins once it passes, and a persistently failing one is replaced.

The crucial subtlety: **"running" is not "healthy."** A process can be wedged — accepting connections
but answering nothing — while the host still reports up. So the check must test an actual correct
response, not mere liveness. Together, elasticity and health checking turn the fleet from a static guess
into a self-sizing, self-healing system — which is only safe *because* the workers are stateless (008):
you can add, remove, and replace them freely because none of them holds anything you'd lose.

## The trade-off

Elasticity buys cost-tracking-demand and stable latency, and pays in lag (scaling takes time, so sharp
spikes can still outrun it — a queue, 010, absorbs the gap) and in churn (workers starting and stopping
have their own cost). Health checking buys fast removal of the dead and pays in tuning: too sensitive
and you evict healthy workers on a blip; too lax and you keep routing to a corpse.

## Names you'll meet

- **Elasticity / auto-scaling** — capacity that grows and shrinks automatically with load.
- **Scaling policy (target tracking)** — "hold average CPU near X" — add or remove workers to keep it.
- **Health check** — the probe that decides who is in rotation and replaces the dead.
- **Liveness vs readiness** — is the process up at all, vs is it actually able to serve.
- **Connection draining / graceful deregistration** — let in-flight requests finish before a worker
  leaves.
- **Desired / min / max capacity** — the bounds the living set may move between.

## Connects to

- **Back → 008 (statelessness).** A fleet can grow and shrink freely only if removing a worker loses
  nothing — exactly what stateless workers guarantee. 008 makes 009 safe.
- **Back → 007 (scale out).** This answers the "how many?" scale-out raises: not a fixed number, a
  living one.
- **Forward → 010 (queues) and 013–016 (resilience).** Failure detection here is the same instinct as
  redundancy and failover at the system level — notice the dead and route around them.

## Drill prompts

- Why is a fixed fleet wrong, and what are the two fixes? *(Demand breathes — so size to demand
  (elasticity) and route only to the living (health checks).)*
- Why isn't "the process is running" good enough for a health check? *(A process can be wedged while the
  host reports up; the check must test a correct response, not mere liveness.)*
- An instance hangs but stays "running" and users time out on it — what's missing? *(A health check that
  removes it from rotation and replaces it.)*
