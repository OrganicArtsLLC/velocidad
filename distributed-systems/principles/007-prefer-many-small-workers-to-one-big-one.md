# 007 — Prefer many small workers to one big one, and put a dispatcher in front

**Cluster:** Spreading the work

## The principle

When one worker can't keep up, you have exactly two moves: make the worker bigger, or add more
workers. Making it bigger — *scaling up* — is seductive because nothing else has to change. But a
single machine has a ceiling you will eventually hit, and until then it remains one machine: when it
dies, everything dies with it. A ceiling and a single point of failure are the same machine described
twice.

Adding more workers — *scaling out* — has no fixed ceiling (the line is still long, add another) and
no single death that stops everything. The price is that you now need something in front to spread
incoming work across them, and the workers must not depend on one another. That price is almost always
worth paying.

## Picture it

The library is slammed — one desk, a line to the street. You can hire one superhuman librarian at a
giant desk (fast, but there's a limit to any one person, and the day she's sick the library stops), or
you can open a second desk, a third, a fourth. With many desks you need one person at the door whose
only job is to glance at the lines and point each newcomer to the shortest one. That person is the
load balancer.

## Why it must be true

Vertical scaling rides a single resource curve — bigger CPU, more RAM — which has hard physical and
economic ceilings and concentrates all risk in one failure domain. Horizontal scaling turns capacity
into something you add in units, so throughput grows roughly linearly (until a shared bottleneck, like
the database, becomes the new limit) and the failure of any one unit removes only its share. The cost
it imposes is coordination: a **load balancer** to distribute requests, and workers independent enough
that any of them can take any request (that independence is 008).

Load balancers come in two depths of attention. One operates at the connection level — it distributes
connections fast without looking inside them (raw speed, a fixed entry point). The other reads the
request — path, host, header — and routes by *what's being asked*. Which you want turns on one
question: does the routing decision need to know the content of the request?

## The trade-off

Scaling out buys unbounded capacity and fault tolerance, and pays in coordination complexity: a
dispatcher to run, a network hop, and a hard requirement that workers hold no private state. Scaling up
buys simplicity and pays in a hard ceiling plus a single point of failure. In practice you often do
both — scale a unit up to a sensible size, then scale those units out.

## Names you'll meet

- **Scale up / vertical** — a bigger single machine. Ceiling plus single point of failure.
- **Scale out / horizontal** — more machines. No fixed ceiling; survives the loss of one.
- **Load balancer** — the dispatcher that spreads work across workers.
- **Layer-7 (application) load balancer** — reads the request and routes by path, host, or header.
- **Layer-4 (network/transport) load balancer** — distributes raw connections fast, without inspecting
  them.
- **Round-robin / least-connections** — *how* the dispatcher picks the next worker.

## Connects to

- **Forward → 008 (statelessness).** Scale-out only works if any worker can take any request, which
  requires the workers to keep no private per-user state. 008 is the precondition this principle quietly
  assumed.
- **Forward → 009 (elastic capacity).** Once you have many workers behind a dispatcher, the next
  question is *how many* — and the answer is "a number that tracks demand."
- **Back → 004–006 (copies & locality).** Those multiplied copies of *data*; this wing multiplies the
  *work*. Both are the same instinct: don't make one thing carry everything.

## Drill prompts

- When one worker isn't enough, what's the move — and why not the obvious one? *(Add workers / scale
  out; a bigger worker keeps the ceiling and the single point of failure.)*
- What decides a layer-7 load balancer vs a layer-4 one? *(Whether routing must read the request's
  content — path/host → L7; raw speed and a fixed entry point → L4.)*
- Why doesn't scaling out give *perfectly* linear throughput forever? *(A shared dependency — often the
  database — eventually becomes the bottleneck.)*
