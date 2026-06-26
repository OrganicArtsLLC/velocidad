# 025 — Consensus is how a set of replicas agrees on one order, despite failures

**Cluster:** Agreement at the core

## The principle

The quorum dial (002) decides whether a *single* read is fresh. But many systems need something stronger:
a group of replicas that all agree on the *same sequence of decisions* — the same total order of writes,
the same elected leader, the same value committed — even while machines crash and messages are lost and
delayed. That agreement-on-an-ordered-history is **consensus**, and it is the machinery underneath
strongly-consistent stores, leader election, distributed locks, and replicated configuration.

You rarely implement consensus yourself; you *recognize when you need it* and reach for a system that
provides it. The principle to keep is what it guarantees, what it costs, and why it can't be cheated.

## Picture it

A committee of librarians must keep their logbooks identical, deciding the order of every change as a
group — but some members fall asleep mid-meeting and some messages between them get lost. The rule they
adopt: nothing is final until a *majority* has written it down. Because any two majorities share at least
one member, the next majority always contains someone who remembers the last decision, so the record can
never fork into two contradictory histories — no matter who dozed off.

## Why it must be true

Consensus rests on **majority quorums**. With 2f + 1 nodes, any two majorities of f + 1 must overlap in at
least one node, and that overlap carries the latest committed decision forward — so the system can lose up
to **f** nodes and still never contradict itself. The dominant pattern is a **replicated log** (state-
machine replication): nodes agree on an append-only ordered log of operations, and each replica applies
the same log to reach the same state. Agree on the order once, and every replica is deterministically
identical.

Two facts bound what's possible:

- **Safety is unconditional; liveness is not.** A correct consensus algorithm *never* returns two
  conflicting decisions, even under arbitrary delays. But the **FLP impossibility result** proves that in
  a fully asynchronous network where even one node may crash, no deterministic algorithm can *guarantee*
  it always terminates. Real systems sidestep this with timeouts and randomization (assuming "partial
  synchrony"): they stay always-safe and make progress whenever a majority is connected and timely.
- **It needs a majority to make progress.** Lose the majority (a partition leaves you on the minority
  side) and the system stops accepting writes rather than risk a fork — it chooses consistency over
  availability (a CP choice, 001).

## The trade-off

Consensus buys a single agreed order — strong consistency, a consistent leader, an audit-able log — and
pays in latency and availability. Every committed decision costs a round trip to a majority, so it is
slower than a local write; throughput is bounded because decisions are funneled through one ordered stream
(often a single leader); and it deliberately becomes *unavailable* on the minority side of a partition.
You also need an **odd** number of nodes (3, 5, 7) to get the best failure tolerance per node — five nodes
tolerate two failures, an efficient sweet spot for many systems.

## Names you'll meet

- **Consensus** — agreement on one value or one ordered history among nodes, despite failures.
- **Paxos** — the foundational consensus algorithm; provably safe, famously hard to follow.
- **Raft** — a consensus algorithm designed for understandability: a strong leader, randomized election
  timeouts, terms, and majority-committed log replication.
- **Replicated log / state-machine replication** — agree on an ordered log, apply it identically
  everywhere.
- **Quorum (majority)** — f + 1 of 2f + 1 nodes; overlapping majorities are why it's safe.
- **Leader election** — a common use of consensus: agree on exactly one coordinator at a time.
- **Two-phase commit (2PC)** — an atomic-commit protocol, *not* fault-tolerant consensus; it blocks if the
  coordinator fails. Don't confuse the two.
- **Byzantine fault tolerance** — consensus tolerating *arbitrary/malicious* nodes (not just crashes),
  which needs 3f + 1 nodes; far more expensive, used where participants aren't trusted.

## Connects to

- **Back → 002 (the dial).** A quorum read checks freshness for one value; consensus agrees on a whole
  ordered history. Majority overlap is the shared idea, scaled up.
- **Back → 001 (the storm).** Consensus is the CP answer to the storm: on a partition, the minority stops
  rather than fork.
- **Forward → C08 (stock exchange).** The finale leans on exactly this — a replicated, ordered log plus
  deterministic replay — to get correctness and availability at once.

## Drill prompts

- What does consensus give you that a single quorum read doesn't? *(Agreement on an entire ordered history
  of decisions, not the freshness of one value.)*
- Why does a consensus system need a majority, and what does it do on the minority side of a partition?
  *(Overlapping majorities prevent a fork; the minority side stops accepting writes — it chooses
  consistency over availability.)*
- State what FLP impossibility does and doesn't forbid. *(In a fully asynchronous network with one
  possible crash, no deterministic algorithm can guarantee termination; it does not forbid safety, and
  real systems make progress under partial synchrony via timeouts.)*
- How many nodes to tolerate two failures, and why odd numbers? *(Five — 2f+1 with f=2; odd counts give
  the best fault tolerance per node since a majority needs f+1.)*
