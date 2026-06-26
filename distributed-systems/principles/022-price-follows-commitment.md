# 022 — Price follows commitment; match each slice of the need to the matching deal

**Cluster:** Cost

## The principle

The same unit of capacity has different prices depending on what you're willing to promise about using
it. Full flexibility — buy now, leave anytime — costs the most. A long commitment costs far less, because
you've removed the provider's uncertainty. And accepting *interruption* — take whatever's spare, give it
back on demand — costs least of all. You are not really pricing the resource; you're pricing your
*commitment* to it.

So you don't pick one deal for everything. You split your need by how *predictable* each part is, and buy
each part on the matching terms: commit the steady, always-on baseline for the deep discount; pay the
flexible premium only for the unpredictable spike; and hand interruptible work to the cheapest,
reclaimable seat.

## Picture it

Three ways to buy the same hotel room: walk up tonight at full rate but leave whenever; promise a year
for a big discount but pay whether or not you show; or take whatever room is empty right now at a deep
discount and accept being bumped when a full-price guest arrives. None is "best" — each fits a different
guest. The error is paying the walk-up rate for the guest who's there every single night.

## Why it must be true

Commitment transfers risk from you to the provider's planning, and they discount you for taking it on. A
reservation guarantees them steady demand, so they price it below the volatile walk-up rate; interruptible
capacity is their *spare*, sold cheap precisely because they can reclaim it when a full-price buyer
appears. The economics therefore reward you for honestly classifying your load:

- **Baseline** (steady, 24/7, predictable) → commit → biggest discount.
- **Spike** (unpredictable, must be available) → flexible / on-demand → pay the premium only on what you
  actually burst into.
- **Interruptible** (can pause and resume — batch, rendering, queue workers) → reclaimable / spot →
  cheapest, because a reclaim just means "retry later."

The strongest real designs *blend* all three across one workload — the same idea as 021 taken one level
finer: 021 says rent your need; 022 says price each slice of that need by its predictability.

## The trade-off

Committing buys a deep discount and pays in lock-in: you owe the spend whether or not you use it, so an
over-sized or soon-obsolete commitment locks in waste. On-demand buys flexibility and pays the top rate.
Interruptible capacity buys the deepest discount and pays in reclaim risk — it can be taken away
mid-task, so only fault-tolerant, resumable work belongs there. The mistake in every direction is a
mismatch: flexible pricing for steady load, or a long commitment for a spike.

## Names you'll meet

- **On-demand** — walk-up rate; flexible, priciest per hour; for spiky or short work.
- **Reserved / committed-use** — multi-year or multi-month commitment for a big discount; for the steady
  baseline.
- **Savings plan (commit-to-spend)** — commit to a spend or usage level for a discount; more flexible
  than reserving specific capacity.
- **Spot / preemptible / spare capacity** — deeply discounted but *reclaimable*; for interruptible work.
- **Commitment / utilization-based discount** — less money for more promise.

## Connects to

- **Back → 021 (rent don't own).** This refines renting: among ways to rent, price drops as commitment
  rises, so price each slice of your need by its predictability.
- **Forward → 023 (right-sizing).** A commitment only saves if it's the *right size* — over-committing to
  capacity you don't need locks in waste for the term.
- **Echoes 016 (DR) and 017 (least privilege).** Same shape: classify the need precisely, buy exactly the
  tier it requires, no more.

## Drill prompts

- What sets the price of the same capacity, and how do you use that? *(Your commitment; commit the steady
  baseline for the discount, stay on-demand for spikes, use reclaimable capacity for interruptible work.)*
- Why is interruptible (spot) capacity so cheap, and what's the catch? *(It's the provider's spare, sold
  cheap because they can reclaim it; only fault-tolerant, resumable work belongs there.)*
- A 24/7 database and a nightly resumable batch job both run on-demand — fix each? *(Database →
  reserved/committed-use; batch → reclaimable/spot capacity.)*
