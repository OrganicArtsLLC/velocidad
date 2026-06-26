# Distributed Systems — A Principles Codex

A vendor-agnostic learning map for distributed systems: the durable trade-offs that survive every
product name, framework, and cloud. This is the **Distributed Systems study** for the Velocidad
knowledge engine — a browsable reference you read, drill, and perform under pressure until the
trade-offs are automatic.

> Product names are weather. The trade-offs are physics. Learn the physics once, and you can re-derive
> the right design no matter what this season's services are called.

---

## What this codex is

Most distributed-systems material teaches you *a product* — this database, that queue, this cloud's
service catalogue. Those names change. The thing underneath them does not. A cache is a bet on
repetition whether you spell it Redis, Memcached, or a hash map; a quorum is the same overlap of read
and write sets whether the console calls it "strong reads" or "consistency level QUORUM."

This codex isolates the durable half. Each entry states one principle plainly, gives you a concrete
picture to anchor it, explains *why it must be true* (so you remember it by understanding, not
memorization), names the trade-off it forces, and lists the terms you will meet in the wild — with
real technologies mentioned only as illustration, never as the lesson.

It is organized as a **codex**, not a textbook: short, self-contained entries you can read in any
order and drill individually. Read top to bottom and it builds an argument; pull a single entry and it
stands alone.

---

## How it's organized

```
distributed-systems/
├── README.md            ← you are here
├── principles/          ← 25 durable principles, grouped into 8 clusters
├── case-studies/        ← 8 worked system designs that apply the principles
├── chunks/reference.md  ← a glossary: precise definitions of the key terms
└── patterns/reference.md← templates for talking through a design under pressure
```

### The principles (25)

The principles run in a deliberate order, clustered into the chapters of one argument:

| Cluster | Principles | The thread |
|---------|-----------|------------|
| **Foundational trade-offs** | 001–003 | When you copy data, agreement becomes a trade you size and spend |
| **Copies & locality** | 004–006 | Keep copies close for speed; pay for it at invalidation |
| **Spreading the work** | 007–009 | Many small interchangeable workers beat one big one |
| **Decoupling** | 010–012 | Put a buffer between producer and consumer; pay the bill in idempotency |
| **Resilience** | 013–016 | You can't prevent failure, so contain and bound it |
| **Security & boundaries** | 017–020 | Least access, layered defense, small surface, useless-without-a-key |
| **Cost** | 021–024 | Buy exactly what the requirement needs — measured in dollars |
| **Agreement at the core** | 025 | How a set of replicas actually agrees on one order (consensus) |

(Consensus is numbered last because it is the deepest mechanism, not the first lesson — but it is the
machinery that 001–002 quietly assume and that the stock-exchange case study, C08, leans on hardest.
Read it once the surrounding trade-offs feel natural.)

### The case studies (8)

The principles are the vocabulary; the case studies *speak* it. Each designs one canonical system
end-to-end and tags every decision with the principle it applies:

| # | System | What it teaches |
|---|--------|-----------------|
| C01 | URL shortener | A read-dominated system; cache and edge everything |
| C02 | Social newsfeed | The read-vs-write war; fan-out on write vs read |
| C03 | Game leaderboard | When the *data structure* is the bottleneck |
| C04 | Chat application | Containing state you cannot make stateless |
| C05 | Video pipeline | Decoupling as a force multiplier |
| C06 | Hotel reservation | Turning the consistency dial hard the *other* way |
| C07 | Web crawler | Distributed work at internet scale; not repeating yourself |
| C08 | Stock exchange | When correctness *inverts* the scale-out instinct |

---

## How to use it with the Velocidad engine

Velocidad is production-first: you perform before you feel ready, capture what broke, drill only the
gaps, and redeploy. For this study, "production" is a **design conversation** — a whiteboard review, a
system-design interview, a real architecture decision — where you must reason aloud under time
pressure.

The flywheel applied here:

1. **Deploy.** Have the agent pose a design prompt (use a case study, or invent one). Talk through the
   architecture aloud, naming the trade-offs as you go.
2. **Capture.** Log what broke: a principle you reached for but couldn't justify, a term you fumbled, a
   trade-off you got backwards.
3. **Distill.** Turn each gap into the smallest learnable unit — usually one principle entry or one
   glossary term.
4. **Drill.** Each principle entry ends with **Drill prompts** — short questions that force you to
   reproduce the principle, the mechanism, and the trade-off from memory. Run them as SRS cards.
5. **Redeploy.** Take the next design prompt and watch the closed gaps hold while new ones open.

The agent prompts that drive this (`session-runner`, `distiller`, `srs-generator`, …) are shared
across every Velocidad study; see the engine overview in `docs/KNOWLEDGE-ENGINE-OVERVIEW.md`. Point
the master prompt at this study and a case study, and start designing before you're ready.

`patterns/reference.md` gives you the **templates for the design conversation itself** — how to open
with requirements, find the dimension that makes the problem hard, and walk the design decision by
decision. `chunks/reference.md` is the **glossary** — precise definitions of every load-bearing term,
including the consistency models and consensus vocabulary that are most often misstated.

---

## A note on rigor

Distributed systems is full of claims that are subtly wrong when stated casually ("exactly-once
delivery," "the CAP theorem says pick two of three," "a redundant copy doubles availability"). This
codex tries hard to state each guarantee precisely and to flag where the real condition is narrower
than the slogan. Where a claim is genuinely uncertain or depends on the system, it is stated
qualitatively rather than asserted as a false specific. The glossary is the place to check the exact
definition of any term used loosely in an entry.

---

## License

Educational content: **CC BY-SA 4.0** (see the repository's `CONTENT-LICENSE`). The Velocidad engine
itself: **GPL-3.0-or-later**.
