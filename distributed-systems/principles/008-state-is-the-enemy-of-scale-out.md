# 008 — State is the enemy of scaling out; push private state out of the worker

**Cluster:** Spreading the work

## The principle

The whole promise of scaling out is that any worker can take any request. The moment a worker keeps
something in its own private memory that the next request will need, that promise breaks: the user is
now chained to that one worker, and a dispatcher free to route anywhere will eventually send them
somewhere that has never heard of them. Private memory feels like an optimization. Under scale-out it's
a liability.

So the discipline is to make workers *forgetful on purpose*. Whatever must persist about a user goes
into a shared store every worker can reach, and the workers themselves keep nothing private. Stateless
workers are interchangeable — and interchangeability is the entire point, because it's what lets the
dispatcher route freely and lets a dead or replaced worker take nothing down with it.

## Picture it

You're halfway through a task at desk one, which is holding your half-filled form in a drawer. You step
away and come back, and the dispatcher helpfully sends you to desk three — which has never heard of
you. Your form is gone. The fix isn't to pin you to desk one forever (now desk one is overloaded and
your form dies if it faints). The fix is that no desk keeps your form in a private drawer at all — it
lives in a shared filing room in the back that every desk can open.

## Why it must be true

A request handled by a stateful worker carries an implicit dependency: "the context I need is in *this*
worker's memory." That dependency couples the request to one failure domain and one queue, which
defeats both the load distribution and the fault tolerance scale-out was supposed to buy. There are two
ways to honor the dependency. *Sticky sessions* keep routing the user back to the worker that holds
their state — preserving the coupling, so load goes uneven and a worker's death loses its users' state.
*Externalizing state* moves the context into a shared store (a cache or database) the workers all
reach, so the workers hold nothing and become truly interchangeable; the cost is one extra hop per
request.

The deeper reading: this is the "extra copy" problem from the data wings, inverted. There you *wanted*
copies close; here you want the worker to hold *no* copy, so there's nothing to go stale or to lose
when it dies.

## The trade-off

Statelessness buys free routing, easy replacement, and elastic scaling, and pays in one extra network
hop per request (to the shared store) plus a new dependency on that store's availability and speed.
Sticky sessions avoid the hop but pay in uneven load and lost state on failure. The shared store itself
becomes hot and important — often it's a cache, inheriting 004's bet and 005's invalidation promise.

## Names you'll meet

- **Stateless** — a worker that keeps no private per-request state; interchangeable.
- **Stateful** — a worker holding context the next request needs; chained to itself.
- **Sticky sessions / session affinity** — pin a user to the worker that holds their state; the
  shortcut, not the design.
- **Externalized session store** — session state in a shared cache or database so the worker tier stays
  stateless.
- **Shared-nothing** — workers share no private state; all shared state lives in a common store.

## Connects to

- **Back → 007 (scale out).** This is the precondition 007 assumed: scale-out only works if workers are
  interchangeable, which requires they hold no private state.
- **Forward → 009 (elastic capacity).** You can only add and remove workers freely if removing one loses
  nothing. Statelessness is what makes a fleet disposable.
- **Back → 004–005 (caching).** The shared session store is often itself a cache — same bet, same
  invalidation promise, now holding the state the workers refuse to keep.

## Drill prompts

- Why can't stateful workers scale out, and what's the fix? *(Private state chains a user to one worker;
  push state to a shared store so any worker can serve anyone.)*
- Sticky sessions vs externalized state — the trade? *(Sticky is simple but uneven and loses state on a
  worker's death; externalized is one extra hop but interchangeable and resilient.)*
- A web tier keeps sessions in each server's local memory and a scale-in event logs users out — fix?
  *(Externalize the session to a shared store so any server can serve any user.)*
