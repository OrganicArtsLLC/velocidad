# C06 — Designing a Hotel Reservation System

**Headline principles:** 001, 002, 003, 004, 007, 012

---

## The system

Search hotels and availability; book a room — with an absolute guarantee of **no double-booking**.

## Requirements

- **Functional:** `search/availability`; `book(room)`.
- **The constraint that rules everything:** two requests for the last room → exactly one wins, ever.
  Search is read-heavy and should be fast; bookings are rarer but must be *correct*.

## The shape

The system has **two personalities with opposite consistency needs**, and the whole design is refusing to
treat them as one:

- **Search** — read-heavy, perfectly fine slightly stale (showing a just-booked room is a minor, fixable
  annoyance).
- **Booking** — must be *strongly consistent and atomic*; there is no acceptable amount of "eventually."

This is the deliberate mirror of the newsfeed (C02), which leaned everything toward availability.

## The design walk

1. **Search side** — cache hard *(004)*, eventually consistent *(001, 002)*, scaled out *(007)*, pushed
   wide. A stale listing is acceptable here.
2. **Booking side** — turn the **dial to strong consistency** *(003 — pointed at correctness, not
   thrift)*. The claim on a room is a single **atomic, conditional operation**: "reserve room X *only if*
   still free." The database serializes concurrent attempts so exactly one succeeds.
3. **Idempotent booking** *(012)* — a double-click or retried request (after a timeout) must not create
   two reservations; an idempotency key makes the repeat a no-op.
4. **Hold-with-timeout** — reserve the room for a short window while the user pays; auto-release if they
   don't confirm (a small reserve → confirm/compensate saga), so half-finished bookings don't lock rooms.

## The hard part — knowing *where* to be strict

The discipline is drawing the line: make the *whole* system strongly consistent and you've built the slow,
expensive cathedral 003 warned against; make the *booking* eventual and you sell rooms twice. The skill
isn't "use strong consistency" — it's knowing the *one place* you must, and relaxing everywhere else.

## The principle map

| Design decision | Principle(s) |
|-----------------|--------------|
| Cached, eventually-consistent search | 001, 002, 004, 007 |
| Atomic conditional write on booking (strong) | 003 |
| Idempotent booking (no double reserve) | 012 |
| Timed hold (reserve → confirm/compensate) | saga (003-family) |

## Concrete building blocks

- **Search:** an in-memory cache plus a search index over a catalog.
- **Booking:** a transactional store — a relational transaction, or a conditional write / transaction on a
  store that supports atomic conditional updates.
- **Holds:** a TTL on the reservation record so abandoned holds auto-release.

## What this case teaches

The consistency dial (001–003) is the same knob as the newsfeed — turned to the *opposite* end. Relax
everywhere you can; turn it hard *exactly* where being wrong is unforgivable, and nowhere else.
