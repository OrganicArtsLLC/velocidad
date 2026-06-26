# Case Studies — the worked designs

The principles (001–025) are the *vocabulary*. These case studies are where the vocabulary is *spoken*:
each one designs a real system end-to-end, and every design decision is tagged with the principle it
applies. They are the best practice there is for the design-conversation skill the Velocidad engine
trains — the muscle that turns "I know what a queue is" into "I can derive, aloud and under pressure,
exactly where this design needs one and why."

Each case study also doubles as an interleaved review: a single design pulls a dozen principles back by
number, so working through C01 → C08 re-exercises the whole codex from eight different angles.

## Entry shape

One file per design: `CNN-slug.md`.

| Section | What it holds |
|---------|---------------|
| **The system** | One line: what we're building. |
| **Requirements** | What it does, plus the scale or constraint that makes it *hard*. |
| **The shape** | The single dimension that decides the architecture. |
| **The design walk** | The system built decision by decision, each tagged with the principle it applies. |
| **The hard part** | The one bottleneck that makes this design interesting. |
| **The principle map** | A table: each decision → the principle(s) it exercises. |
| **Concrete building blocks** | Vendor-neutral component categories (with illustrative examples). |
| **What this case teaches** | The one idea to carry away. |

## Index

| # | System | Headline principles | The lesson |
|---|--------|---------------------|------------|
| [C01](C01-url-shortener.md) | URL shortener | 001, 002, 004, 006, 007, 008, 009, 013, 014, 021 | A read-dominated system; cache and edge everything |
| [C02](C02-social-newsfeed.md) | Social newsfeed | 001, 002, 004, 007, 010, 011, 022 | The read-vs-write war, won by choosing *when* to do the work |
| [C03](C03-game-leaderboard.md) | Game leaderboard | 001, 002, 004, 007, 008, 010, 011 + data structure | When the *data structure* is the bottleneck |
| [C04](C04-chat-application.md) | Chat application | 001, 004, 005, 007, 008, 010, 011, 012, 013 | Containing state you can't make stateless |
| [C05](C05-video-pipeline.md) | Video pipeline | 006, 009, 010, 011, 012, 021, 022, 023, 024 | Decoupling as a force multiplier |
| [C06](C06-hotel-reservation.md) | Hotel reservation | 001, 002, 003, 004, 007, 012 | Turning the consistency dial the *opposite* way |
| [C07](C07-web-crawler.md) | Web crawler | 001, 005, 007, 008, 010, 012, 013, 015, 022, 023 | Distributed work at internet scale; not repeating yourself |
| [C08](C08-stock-exchange.md) | Stock exchange | 001, 002, 003, 007 *inverted*, 010, 011, 012, 014, 025 + event sourcing | When correctness *inverts* the scale-out instinct |

**The set, in one breath.** C01 is a *read* problem; C02 a *read-vs-write* war; C03 turns on the *data
structure*; C04 *contains* unavoidable state; C05 is *decoupling* in full; C06 is the *anti-C02* (turn
the dial hard to consistency); C07 is *distributed work* at internet scale; and C08 *inverts* scale-out
for correctness and lands the thesis: **the principles are trades, not rules.** Across all eight, the
most-exercised principles are the consistency dial (001/002), caching (004), the queue (010), and
scale-out/statelessness (007/008) — the load-bearing walls of nearly every system.

## How they finish the study

These are the chapters where the whole codex clicks, because you watch the same handful of trades —
replicate, cache, decouple, isolate, right-size — recombine into wildly different systems. The names of
the systems change; the trades don't. Drilling them with the Velocidad engine means *designing one aloud
before you feel ready*, capturing every trade-off you fumbled, and redeploying on the next system until
the recognition is automatic.
