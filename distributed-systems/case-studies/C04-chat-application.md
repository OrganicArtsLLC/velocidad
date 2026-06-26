# C04 — Designing a Chat Application

**Headline principles:** 001, 004, 005, 007, 008, 010, 011, 012, 013

---

## The system

Real-time 1:1 and group messaging: deliver messages instantly to online users, show presence, keep
ordered history.

## Requirements

- **Functional:** `send(msg)`; real-time `deliver` to online recipients; `presence` (who's online);
  `history`; per-conversation ordering.
- **The scale that makes it hard:** millions of *simultaneous open connections*; delivery in
  milliseconds; the server must *push* (it can't wait to be polled).

## The shape

To push a message the instant it's sent, the server holds a **persistent connection** (e.g. a WebSocket)
to each user — and that connection is **state pinned to one machine** (the exact thing 008 warns against,
here unavoidable). Sender and recipient are usually on *different* servers, so the core question is: how
does a message cross from the receiving server to the one holding the recipient's open line?

## The design walk

1. **Thin stateful gateway tier** holds the live connections — the only stateful part, kept small. *(008's
   exception, contained — 013.)*
2. **Connection registry:** "user B's line is on server 7" — a fast in-memory store. *(004.)*
3. **Message journey:** the receiving server stores the message durably (ordered) → looks up the recipient
   in the registry → delivers across servers via a **pub/sub backplane**. *(011 — fan-out turned inward to
   route between your own servers.)*
4. **Offline recipient:** no live line → the message waits in durable storage / a queue, delivered on
   reconnect. *(010.)*
5. **Presence:** an in-memory store with heartbeat **TTLs** — online while the line keeps pinging. *(004,
   005.)*
6. **Ordering and no duplicates:** sequence numbers per conversation; at-least-once delivery made safe by
   **idempotent** dedup so a retried message isn't shown twice. *(012.)*
7. Eventual consistency across edges is fine. *(001.)*

## The hard part — unavoidable connection state

A live socket physically lives on one machine; it can't be externalized like a session token. So rather
than pretend it's stateless, you **quarantine** the state to a thin gateway, front it with a registry, and
route across the fleet with pub/sub — containing the statefulness (013) while keeping everything else
stateless (008).

## The principle map

| Design decision | Principle(s) |
|-----------------|--------------|
| Thin gateway holds sockets (contained state) | 008 (exception), 013 |
| Connection registry + presence in memory | 004, 005 |
| Cross-server delivery via pub/sub backplane | 011 |
| Offline messages queued for pull | 010 |
| Sequence numbers + dedup (no double-show) | 012 |
| Eventual across edges; stateless app tier | 001, 007, 008 |

## Concrete building blocks

- **Connections:** a persistent-connection gateway (WebSocket servers, or a managed connection service).
- **Messages:** a store that preserves per-conversation order (e.g. a timestamp/sequence sort key).
- **Presence and connection registry:** an in-memory store with TTLs.
- **Backplane:** a pub/sub channel or stream to route messages between gateway servers.

## What this case teaches

Statelessness is a principle, not a law. When state is physically unavoidable (an open socket), you
*contain* it and route around it — the principle's exception, handled by another principle (isolation).
