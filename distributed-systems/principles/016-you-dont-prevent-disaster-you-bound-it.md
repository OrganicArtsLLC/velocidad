# 016 — You don't prevent disaster, you bound it: pick how much you can lose and how long you can be down

**Cluster:** Resilience

## The principle

Some failures are total — a region goes dark, a building floods — and you cannot drive their probability
to zero. So disaster recovery is not a prevention problem; it's a *budgeting* problem. You answer two
cold questions in advance: when catastrophe strikes, how much data can the business afford to lose, and
how long can it afford to be down? Those two numbers determine everything else.

The temptation is to answer both with "nothing" and "instantly" — but that means paying for a full,
warm, duplicate system forever, against a day that may never come. The discipline is to name what the
business can *actually* tolerate and buy *exactly* that much recovery — no more.

## Picture it

The master ledger — every record the library has. To survive a fire you copy it to a vault across town,
and two questions decide the cost. How *often* do you copy it (copy daily, and a 4 p.m. fire loses a day
of changes)? And how *ready* is the vault — a cold storage room you'll need a week to rebuild from, or a
fully-staffed twin branch that opens in minutes? Cheap and lossy at one end; a second whole library,
always warm, at the other.

## Why it must be true

The two numbers map directly to two costs. **RPO (recovery point objective)** — the maximum data loss,
measured in time — sets your backup *frequency*: an RPO of one hour means capturing state at least
hourly, because anything since the last capture is what you lose. **RTO (recovery time objective)** — the
maximum downtime — sets how *warm* you keep the standby, because cold things take longer to start.

That second axis is a spectrum of increasing cost for decreasing RTO:

- **Backup and restore** — just data in a vault; cheapest, slowest.
- **Pilot light** — core always-on, the rest ready to launch.
- **Warm standby** — a scaled-down live copy you scale up on disaster.
- **Active-active (multi-site)** — a full twin already serving; near-zero RPO/RTO, highest cost.

There is no free recovery — every notch of less loss and less downtime is paid for continuously, whether
or not disaster ever arrives. So you buy to the business's stated tolerance, not to zero.

## The trade-off

Lower RPO costs more frequent (and more expensive) data capture and replication; lower RTO costs a
warmer, more fully-provisioned standby running idle. Pushing both toward zero converges on running two
full systems forever — maximal safety, maximal cost. The skill is matching the recovery tier to a stated
business tolerance, not to fear.

## Names you'll meet

- **RPO (recovery point objective)** — max acceptable data loss, in time → backup frequency.
- **RTO (recovery time objective)** — max acceptable downtime → how warm the standby is.
- **Backup and restore** — cheapest; large RPO/RTO. Data kept elsewhere, restored on demand.
- **Pilot light** — core running, the rest ready to start.
- **Warm standby** — a scaled-down live copy, scaled up on disaster.
- **Active-active / multi-site** — a full live twin; near-zero RPO/RTO, highest cost.

## Connects to

- **Closes the resilience cluster.** Principles 013–015 keep you up through *partial* failures; this one
  handles the *total* loss you can only bound, not prevent.
- **Back → 014 (independence).** DR is independence taken to its largest scale — a copy in another region,
  uncorrelated with the disaster that took the first.
- **Back → 001–003 (the trade).** Same shape: you can't have everything (zero loss + zero downtime + low
  cost), so you name what you need and pay precisely for it.
- **Forward → cost & security clusters.** "Buy exactly what the requirement needs, no more" is also the
  cost-optimization instinct and the least-privilege instinct in different clothes.

## Drill prompts

- DR isn't prevention — it's what, and it's driven by which two numbers? *(Bounding the loss; RPO (how
  much data you can lose) and RTO (how long you can be down).)*
- What does RPO set, and what does RTO set? *(RPO sets backup frequency; RTO sets how warm the standby
  is — which strategy on the spectrum.)*
- Lose at most 5 minutes of data, back within 15 minutes, but no full live second site — numbers and
  strategy? *(RPO 5 min / RTO 15 min → warm standby.)*
