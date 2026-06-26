# 011 — When many parties care about one event, publish it and let them subscribe

**Cluster:** Decoupling

## The principle

When one event matters to many independent systems, the naïve design has the source call each one
directly. That makes the source responsible for *knowing the entire audience* — and that responsibility
only grows: every new listener is a change to the speaker. The coupling here isn't in time (that was the
queue); it's in *knowledge*. The producer knows too much about who consumes it.

Delete that knowledge. Have the source announce the event to a shared channel and let interested parties
subscribe themselves. The producer publishes into the void; who listens, and how many, is none of its
concern. Adding the seventh consumer changes nothing about the speaker. Broadcast beats point-to-point
whenever an event has an open-ended audience.

## Picture it

Instead of the order desk phoning the kitchen, then billing, then loyalty, then analytics — one by one,
learning a new number for every new department — it pins a notice to a bulletin board: "Order #417
placed." Every department that cares has subscribed to that board and reads the notice on its own. The
order desk has no idea who's reading. It doesn't want to know. It announces and walks away.

## Why it must be true

Direct calls encode the consumer list into the producer's code, so the producer's change-rate is tied
to the *whole system's* growth — the worst kind of coupling, because it punishes exactly the thing you
want (adding capability). Publish-subscribe inverts the dependency: the producer depends only on a
*topic* (an abstraction), and consumers depend on that same topic. Now producer and consumers vary
independently — the textbook payoff of loose coupling.

It's a different *shape* from the queue, and the distinction is load-bearing. A queue is point-to-point:
one message is consumed *once*, by one worker from a pool — for *distributing work*. Pub/sub is fan-out:
one event is delivered to *every* subscriber, each with its own copy — for *announcing that something
happened*. Combine them — publish to a topic that fans out into one durable queue per consumer — and you
get broadcast *plus* each consumer's own buffered, at-its-own-pace processing.

## The trade-off

Pub/sub buys producer-consumer independence (add subscribers freely) and pays in indirection and weaker
end-to-end visibility: the producer no longer knows whether anyone acted on the event, error handling
moves to each subscriber, and reasoning about "what happens when X is published" now means tracing a
fan-out instead of reading one call site. You also inherit at-least-once delivery and duplicate handling
(012), amplified because the event lands in many places.

## Names you'll meet

- **Publish-subscribe (pub/sub)** — one event broadcast to many independent subscribers.
- **Topic** — the channel publishers announce to and subscribers listen on.
- **Fan-out** — one event delivered to many consumers at once.
- **Event bus / event router** — a channel that can *route* events to different targets by content.
- **Topic-to-queue fan-out** — one event into several durable queues, one per consumer; broadcast plus
  per-consumer buffering.

## Connects to

- **Back → 010 (the queue).** Same wing, different axis: 010 decouples in *time* (one-to-one), 011
  decouples in *knowledge* (one-to-many). They compose — fan-out a topic into per-consumer queues.
- **Back → 008 (statelessness).** Both are the loose-coupling instinct: remove a dependency (private
  state there, audience knowledge here) so parts can change independently.
- **Forward → 012 (idempotency).** Fan-out multiplies deliveries and thus duplicates, making idempotent
  consumers even more necessary.

## Drill prompts

- When many systems care about one event, what's the pattern, and which coupling does it remove?
  *(Publish-subscribe; it removes the producer's knowledge of the audience.)*
- Queue vs pub/sub — the one-line distinction? *(Queue = one message consumed once, to distribute work;
  pub/sub = one event delivered to every subscriber, to announce it happened.)*
- A signup must trigger ever-more downstream systems without editing the signup code — pattern?
  *(Publish a "signup" event to a topic; let downstreams subscribe.)*
