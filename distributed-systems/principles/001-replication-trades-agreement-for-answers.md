# 001 — When a replicated system can't talk to itself, it must trade agreement for answers

**Cluster:** Foundational trade-offs

## The principle

Copy a piece of data into two places and you have bought a problem you cannot design away. As long as
the two copies can communicate, they stay in agreement and nobody notices. The instant they cannot
communicate — a dropped link, a network partition — you are forced to choose. You can keep answering
requests and let the copies diverge, or you can keep the copies in agreement and stop answering until
they can talk again. You cannot do both.

This is not a fact about any particular database. It is a fact about copies. Two replicas, two bank
branches, two caches of the same value — the moment a replicated system loses contact with itself,
*agreement* and *availability* become a trade, and you spend one to buy the other.

## Picture it

Two librarians run the same catalogue from two buildings across town, every record mirrored between
them. A storm takes down the phone line. A reader walks into the east building and asks to change a
record. Allow the change and the two buildings now disagree — the west librarian is handing someone
the old record. Refuse it until the line is back and the buildings always agree — but the reader is
now waiting, and you have stopped answering. The storm is the partition; those two answers are the
whole map.

## Why it must be true

Agreement between two copies *is* a message — it requires the copies to exchange information. A
partition is, by definition, the copies being unable to exchange information. So during a partition,
on-demand agreement is precisely the thing you cannot have. Two honest options remain: answer with
possibly-stale data, or withhold the answer until agreement becomes possible. There is no third door,
because "answer correctly and immediately while disconnected" would require sending a message across a
line that is down.

The trade does not vanish in clear weather. Even with the network healthy, if you want every replica
to agree on every read, each read must check across the system first — and that check costs latency.
Drop the check and reads get fast, but a reader can see a value another replica has already changed.
So the full law has two halves: **under a partition**, agreement or availability; **otherwise**,
agreement or latency. Strong agreement is never free.

## The trade-off

You are choosing, per workload, which pain you can tolerate. Choosing to keep answering means
accepting temporary disagreement (stale or conflicting reads). Choosing to stay in agreement means
accepting unavailability during a partition and added latency the rest of the time. The choice is the
design; everything built on top is an answer to this one question.

## Names you'll meet

- **CAP theorem** — the formal statement: when a network partition occurs, a distributed system can
  guarantee *consistency* (here meaning linearizability — every read sees the latest write) or
  *availability* (every reachable node answers), not both. CAP is about the partition case only.
- **PACELC** — the more complete framing: *if* **P**artitioned, choose **C** or **A**; **e**lse,
  choose **L**atency or **C**onsistency. It adds the clear-weather half CAP omits.
- **CP vs AP** — shorthand for which side a store chose: CP keeps agreeing (and may refuse to answer),
  AP keeps answering (and may diverge).
- **Strong vs eventual consistency** — "every read returns the latest write" vs "replicas converge
  over time." Many stores let you pick per request, often at roughly double the cost for the strong
  read (it must contact a quorum; see 002).

## Connects to

- **Forward → 002 (the dial).** Agreement is not binary; it is a quantity you tune by deciding how
  many replicas must agree before you answer.
- **Forward → 003 (just enough agreement).** You rarely want maximum agreement everywhere; the skill
  is buying the cheapest guarantee that holds.
- **Sibling → the fallacies of distributed computing.** "The network is reliable" is the lie this
  principle exists to correct. The storm is the assumption, not the edge case.

## Drill prompts

- What must any replicated system trade during a partition, and why? *(Agreement for answers — because
  agreement is a message and the line is down.)*
- Even with no partition, what are you still trading, per PACELC? *(Latency for consistency — strong
  agreement always costs a round trip.)*
- State the CAP theorem precisely, including what its "C" and "A" actually mean. *(C = linearizability;
  A = every non-failing node responds; the choice is forced only during a partition.)*
