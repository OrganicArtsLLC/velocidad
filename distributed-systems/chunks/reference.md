# Term Reference — the load-bearing vocabulary

The precise definitions behind the principles. Distributed systems is full of terms that are casually
misstated; this is where to check the *exact* meaning of anything an entry used loosely. Treat each term
as a "chunk" to master — you should be able to state the definition cold and name the principle it
belongs to.

**How to use:** before a design session, skim the section for the trade-offs you'll be reasoning about.
When a friction-log entry is "I fumbled the definition of X," that term becomes an SRS card. Track your
own mastery in your private progress file.

---

## Consistency models (most-misstated section — learn these precisely)

These are guarantees about what a read may return when data is replicated. They run from strongest
(most coordination, most latency) to weakest (least coordination, most availability).

| Term | Precise meaning | Note |
|------|-----------------|------|
| **Linearizability** (a.k.a. atomic / strong consistency) | Every operation appears to take effect instantaneously at a single point between its invocation and its response, and this order is consistent with **real time** (if A completes before B begins, A is ordered before B). A read always returns the most recent completed write. | The "C" in CAP. The strongest single-object guarantee. |
| **Sequential consistency** | All operations appear in *some* single total order, and each process's operations appear in that order in their program order — but the total order need **not** match real time. | Weaker than linearizability: it drops the real-time requirement. |
| **Causal consistency** | Operations that are causally related (one could have influenced another) are seen in the same order by all processes; concurrent (unrelated) operations may be seen in different orders. | A useful middle ground; available under partition. |
| **Eventual consistency** | If no new updates are made, all replicas *eventually* converge to the same value. No guarantee about ordering or how long convergence takes. | The weakest common guarantee; maximally available. |
| **Strong eventual consistency** | Eventual, plus: replicas that have received the same set of updates are in the same state, with no conflicts (e.g. via CRDTs). | Convergence without coordination, for mergeable data types. |

### Session guarantees (cheap, client-centric — see principle 003)

| Term | Precise meaning |
|------|-----------------|
| **Read-your-writes** | A process always sees the effect of its *own* previous writes. |
| **Monotonic reads** | If a process reads a value, any later read returns that value or a newer one — never an older one. |
| **Monotonic writes** | A process's writes are applied in the order it issued them. |
| **Writes-follow-reads** | A write that follows a read is ordered after the write that read observed. |
| **Session consistency** | The above session guarantees, scoped to one client session. Sits between strong and eventual. |

---

## The foundational theorems

| Term | Precise statement | Common misstatement to avoid |
|------|-------------------|------------------------------|
| **CAP theorem** | When a network **partition** occurs, a distributed system must choose between **C** (linearizability — every read sees the latest write) and **A** (every request to a non-failing node returns a response). It cannot guarantee both *during the partition*. | "Pick two of three." CAP is *not* "consistency, availability, partition-tolerance, choose two" — partitions are not optional, so the real choice is C-vs-A *when partitioned*. |
| **PACELC** | **If** **P**artitioned, choose **C** or **A**; **E**lse (normal operation), choose **L**atency or **C**onsistency. Extends CAP to the no-partition case. | Forgetting the "else": even with a healthy network, strong consistency costs latency. |
| **FLP impossibility** | In a fully **asynchronous** system where even one process may crash, no deterministic consensus algorithm can guarantee it always **terminates**. | It does *not* say consensus is impossible — it forbids *guaranteed termination*, not *safety*. Real systems use timeouts/partial synchrony to make progress in practice. |

---

## Quorums & replication

| Term | Precise meaning |
|------|-----------------|
| **Replica (N)** | A copy of the data; N is the number of replicas. |
| **Write quorum (W)** | Number of replicas that must acknowledge a write before it counts. |
| **Read quorum (R)** | Number of replicas consulted on a read. |
| **R + W > N** | The condition guaranteeing the read set and write set overlap, so a read sees the latest acknowledged write. For correctness under concurrent writes, also want **W > N/2**. |
| **Quorum (majority)** | More than half the nodes (f + 1 of 2f + 1). Any two majorities overlap — the basis of consensus safety. |
| **Leader / primary** | The replica that orders writes; followers replicate from it. |
| **Replication lag** | The delay before a write reaches a follower replica; the staleness window for replica reads. |

---

## Consensus & coordination (see principle 025)

| Term | Precise meaning |
|------|-----------------|
| **Consensus** | Getting a set of nodes to agree on one value, or one ordered history of values, despite crashes and message loss. |
| **Paxos** | The foundational consensus algorithm; provably safe, hard to understand; "Multi-Paxos" agrees on a sequence. |
| **Raft** | A consensus algorithm designed for understandability: strong leader, randomized election timeouts, numbered terms, majority-committed log. |
| **State-machine replication** | Replicas apply the *same ordered log of commands* and therefore reach the *same state*. The standard way to build a fault-tolerant service from consensus. |
| **Leader election** | Using consensus to agree on exactly one coordinator at a time. |
| **Two-phase commit (2PC)** | An *atomic-commit* protocol across participants. **Not** fault-tolerant consensus — it **blocks** if the coordinator fails mid-protocol. |
| **Byzantine fault tolerance (BFT)** | Consensus tolerating *arbitrary or malicious* nodes (not just crashes); needs 3f + 1 nodes to tolerate f, vs 2f + 1 for crash faults. |

---

## Caching & locality

| Term | Precise meaning |
|------|-----------------|
| **Hit rate** | Fraction of requests served from the cache; the measure of whether the cache bet pays. |
| **TTL (time-to-live)** | A timer after which a cached copy is treated as expired. Caps maximum staleness. |
| **Write-through / write-back** | Update cache and source together (fresh, slow writes) / update cache now and source later (fast writes, risk of loss). |
| **Cache-aside (lazy loading)** | The application loads on a miss and invalidates on write. |
| **Eviction policy (LRU / LFU)** | What to drop when the cache is full: least-recently-used / least-frequently-used. |
| **Cache stampede (thundering herd)** | Many hot entries expire together and a flood hits the source at once. Fixed by jittered TTLs or single-flight rebuild. |
| **CDN / edge / origin** | A mesh of caches near users (edge / points of presence) that fall back to the home system (origin) on a miss. |

---

## Decoupling & messaging

| Term | Precise meaning |
|------|-----------------|
| **Queue (point-to-point)** | A buffer where each message is consumed **once**, by one worker from a pool. For distributing work. |
| **Publish-subscribe (fan-out)** | One event delivered to **every** subscriber, each with its own copy. For announcing that something happened. |
| **At-most-once** | Never duplicates; may drop on failure. |
| **At-least-once** | Never drops; may duplicate. The common default. |
| **Exactly-once** | The ideal of no loss and no duplication. In practice, at-least-once **delivery** plus idempotent **processing** (or transactional effects) — true exactly-once delivery is not achievable over an unreliable network in general. |
| **Idempotency** | Applying an operation twice has the same effect as applying it once. The real defense against duplicates. |
| **Dead-letter queue (DLQ)** | Where messages that repeatedly fail are set aside so they don't block the line. |
| **Backpressure** | Signaling producers to slow down when consumers can't keep up. |

---

## Scaling & resilience

| Term | Precise meaning |
|------|-----------------|
| **Vertical / horizontal scaling** | A bigger machine (ceiling + single point of failure) / more machines (no fixed ceiling, survives a loss). |
| **Stateless / stateful worker** | Keeps no private per-request state (interchangeable) / holds context the next request needs (chained to itself). |
| **Elasticity / auto-scaling** | Capacity that grows and shrinks automatically with a demand signal. |
| **Health check (liveness vs readiness)** | A probe deciding who's in rotation: liveness = "is the process up," readiness = "can it actually serve." |
| **Blast radius / bulkhead / failure domain** | How much fails when one thing fails / a wall isolating one part / the boundary a fault can't cross. |
| **The nines** | Availability targets: 99.9% ≈ 8.8 h/yr down, 99.99% ≈ 53 min/yr, 99.999% ≈ 5 min/yr. Each nine ≈ 10× less downtime. |
| **Series vs parallel availability** | Need-all multiplies availabilities down; need-any multiplies *failure* probabilities (climbs) — but only if failures are **independent**. |
| **Correlated failure / SPOF** | Copies that share a fate and die together / a dependency with no independent backup. |
| **Circuit breaker** | After repeated failures, stop calling a dependency (fail fast) for a cooldown, then probe. |
| **Exponential backoff + jitter** | Increasing, randomized retry delays so retries don't synchronize into a storm. |
| **RPO / RTO** | Max acceptable data loss (→ backup frequency) / max acceptable downtime (→ how warm the standby is). |

---

## Data-structure & architecture terms used in the case studies

| Term | Precise meaning |
|------|-----------------|
| **Sorted set** | A structure keeping elements in score order with O(log n) updates and rank lookups; turns "what's my rank?" from a scan into a lookup (C03). |
| **Bloom filter** | A probabilistic set membership structure with **false positives but no false negatives**: it answers "definitely not present" or "possibly present." Trades a little precision for large memory savings (C07). |
| **Event sourcing** | Store the ordered *events* (the log), not just current state; current state is a replay of the log. Gives ordering, audit, and replayability (C08). |
| **CQRS** | Command-Query Responsibility Segregation: separate the write model from one or more read models, often eventually consistent. |
| **Fan-out on write / read** | Build each consumer's view at write time (fast reads, costly writes) / gather it live at read time (cheap writes, costly reads) (C02). |
| **Data gravity / egress** | Data is cheap to store and expensive to move across boundaries; "egress" is the (often asymmetric) cost of moving data out. |
