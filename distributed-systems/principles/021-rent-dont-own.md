# 021 — Don't own capacity for your peak; rent it for your need

**Cluster:** Cost

## The principle

If you *own* the capacity to handle your busiest moment, you pay for that capacity every moment —
including the vast majority of the time you don't need it. You can't size for the average (you'd collapse
on the busy day), so you size for the peak, and the difference between peak and average becomes capacity
you bought, power you burn, money you spend, to sit idle. The spikier the load, the more of your spend is
air.

The fix is to rent instead of own: turn capacity on when load arrives and off when it leaves, and pay
only for what you actually use. The idle gap isn't *managed* down — it's *deleted*, because you never
paid for the empty room.

## Picture it

You don't build a ballroom for a three-hundred-guest wedding — you rent one for the night and hand back
the keys in the morning. Owning means paying for three-hundred-guests of space on the ordinary days it
holds eight: lights, heat, upkeep, all running for a nearly-empty room. Renting means paying for the one
night you fill it, and nothing on the three hundred nights you don't.

## Why it must be true

Owned capacity is a fixed cost paid regardless of utilization, so cost-per-useful-work scales with how
*idle* you are; a system that peaks at 10× its average and is provisioned for the peak runs ~90% wasted
by construction. Rented, metered capacity makes cost track *usage* instead of *provisioning*, so the idle
hours cost nothing and the waste vanishes rather than being merely tolerated. This is the cloud's
foundational economic shift — capital expense (buy the asset, own the idle) to operating expense (rent
the use, pay the meter) — and it's the cost-side reading of the same elasticity that buys resilience
(009): the fleet that breathes with demand also *bills* with demand.

The trade-off that sets up everything downstream: the per-hour *rental* rate is higher than the amortized
per-hour cost of something owned outright. So renting wins decisively when utilization is low or spiky,
and the savings shrink as usage becomes steady and predictable — which is exactly what the next principle
prices.

## The trade-off

Pay-as-you-go buys "cost tracks usage, zero waste at idle" and pays a premium *per hour* relative to
owning, plus a dependence on the rental market's prices and availability. For steady, predictable,
always-on load, that premium can make renting more expensive than owning or committing — so renting is the
right default for spiky and uncertain demand, not for everything.

## Names you'll meet

- **Pay-as-you-go** — billed for actual usage, by hour, minute, or request.
- **Elasticity** — capacity turned on and off with load.
- **Capex vs opex** — own-the-asset vs rent-the-use.
- **Utilization** — how much of what you pay for you actually use.
- **On-demand** — the metered, no-commitment rate.
- **Serverless** — pay per request; costs nothing at zero traffic.

## Connects to

- **Opens the cost cluster.** The last constraint every system answers to.
- **Back → 009 (elasticity).** Same mechanism, read as a bill: the fleet that scales with demand also
  costs with demand.
- **Forward → 022 (commitment pricing).** Renting's catch — the walk-up rate is the priciest hour — is
  what commitment discounts address for the steady part of your need.

## Drill prompts

- Why is owning capacity for your peak wasteful, and what's the fix? *(You pay for the idle gap between
  peak and average; rent metered capacity, pay for what you use, size to demand.)*
- What's the trade-off that limits pay-as-you-go? *(The per-hour rental rate is higher than owned; it wins
  for idle or spiky use, less so for steady use.)*
- A fleet sized for the yearly peak runs full-size all year at 80% idle — the waste and the fix? *(Paying
  for peak year-round; elastic pay-as-you-go that scales down off-peak.)*
