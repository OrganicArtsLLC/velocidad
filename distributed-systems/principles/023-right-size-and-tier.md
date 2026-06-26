# 023 — Push every workload to the cheapest resource that meets its requirement; right-size and tier

**Cluster:** Cost

## The principle

Two quiet wastes follow from the same reflex — buy big, buy fast, never look again. One is
over-provisioning: a resource far larger than the load will ever use, billed in full while it runs at a
fraction of capacity forever. The other is over-fast storage: keeping rarely-touched data on the most
expensive, instant-access tier "so it's always ready," paying premium rent on a warehouse nobody visits.

The fix is to match the resource to the *actual* need. Right-size compute to measured load — shrink what's
over-provisioned, grow only when the numbers demand it. And tier data by access pattern — hot data on
fast, dear storage; cold data on cheap, slow storage — with lifecycle rules migrating it down as it ages.
Pay for the size and speed you *use*, not the size and speed you *might*.

## Picture it

A library has a hot shelf at the front desk — instant, expensive — and a deep archive in a cheap basement
across town — slow, nearly free. Renting a grand ballroom for a book club of six is the over-provisioned
machine. Keeping a years-old tax receipt on the gold-plated front-desk shelf is cold data on hot storage.
The art isn't picking a shelf; it's matching each item to the shelf its use deserves — and moving things
down as they cool.

## Why it must be true

Cost is paid on what you *provision*; value is produced by what you *use*; so any gap between them is pure
waste — and the gap has two common forms. Over-provisioned compute: the bill tracks instance size, not
utilization, so a box at 10% CPU wastes ~90% of its cost; right-sizing closes the gap by fitting the box
to observed load. Mis-tiered storage: storage classes trade retrieval speed and cost against storage
price, and data's value usually *decays* with age (queried hard when new, almost never later), so paying
hot-tier prices for cold data is a standing overcharge. Lifecycle policies automate the migration because
access patterns are predictable enough to schedule; where they aren't, automatic tiering observes and
moves data for you.

This is the same "buy exactly what the requirement needs" discipline as disaster recovery (016) and least
privilege (017) — here the requirement is a measured utilization or access frequency, and "no more than
needed" is spent in dollars.

## The trade-off

Right-sizing buys lower cost and pays in vigilance and a little headroom risk: usage changes, so a
too-tight size can throttle a workload under an unexpected spike, and keeping sizes matched is ongoing
work, not a one-time fix. Tiering buys cheaper storage for cold data and pays in retrieval latency and
sometimes retrieval cost — pulling something back from the cheapest archive tier can be slow and is
occasionally billed, so mis-tiering *hot* data the wrong way costs more than it saves.

## Names you'll meet

- **Right-sizing** — fit the resource to measured load.
- **Over-provisioning** — paying for capacity you don't use.
- **Storage classes / tiers** — hot / cool / cold options trading retrieval speed and cost against
  storage price.
- **Lifecycle policy** — automatically migrate data across tiers as it ages.
- **Automatic / intelligent tiering** — moves data between tiers for you when the access pattern is
  unpredictable.
- **Utilization metrics** — the real-usage signal that drives right-sizing.

## Connects to

- **Back → 022 (commitment).** A commitment only saves if it's the right size; right-size *before*
  committing, or you lock in waste for the term.
- **Back → 016 and 017.** Same instinct — buy exactly what the requirement needs — now measured in
  utilization and access frequency.
- **Forward → 024 (architecture).** Right-sizing optimizes *within* a design; the next principle changes
  the design itself, which dwarfs it.

## Drill prompts

- Two common cost wastes from "buy big," and the two fixes? *(Over-provisioned compute → right-size to
  real usage; cold data on hot storage → tier it down with lifecycle rules.)*
- Why does mis-tiered storage waste money? *(Data's value decays with age but the hot-tier price doesn't;
  cold data on hot storage is a standing overcharge.)*
- Years of logs sit in the hottest tier, accessed for a month then rarely, kept for years — the fix? *(A
  lifecycle policy migrating them to infrequent-access, then archival storage.)*
