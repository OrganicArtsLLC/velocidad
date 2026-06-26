# 018 — Never rely on a single line of defense; layer independent controls of different kinds

**Cluster:** Security & boundaries

## The principle

Any single control will eventually fail — a lock is picked, a key leaks, a flaw nobody knew about is
found. So a defense made of one perfect wall has a fatal property: the day it's beaten, the attacker has
*everything*. Strength that depends on never failing is not strength.

The fix is to stack multiple *independent* controls of *different kinds*, so a breach requires defeating
all of them and no single failure is total. Independence and variety are the point — two locks that fall
to the same skill barely help; a lock, an identity check, segmentation, and encryption fail for
different reasons, so beating one tells the attacker nothing about the next.

## Picture it

Protect the vault not with one magnificent unpickable lock, but with a decent lock *and* an inner gate
*and* a guard who checks names *and* a safe *and* manuscripts sealed in individual cases. A thief who
picks the front lock meets the gate; past the gate, the guard; past the guard, the safe. No single
failure is a breach. The single perfect lock is a single point of total failure — beat it once, win
everything.

## Why it must be true

Security controls have failure probabilities like anything else, and a single control is a single point
of failure: its breach is the system's breach. Independent layered controls compose like parallel
redundancy in reverse (014) — to win, the attacker must defeat *every* layer, and if the layers fail
independently, the chance of beating all of them is the product of small numbers, which is tiny. Variety
enforces the independence: same-kind controls share weaknesses (one exploit beats both); different-kind
controls don't.

The crucial corollary is *don't trust the inside because something cleared the outside*. A hard
perimeter around a soft interior collapses the moment an attacker is in — which is how the worst breaches
read: "they got through the firewall and then moved freely." Identity and encryption checks *inside* the
perimeter are what make a foothold not a victory.

## The trade-off

Defense in depth buys resilience to any one control's failure and pays in cost, latency, and friction:
each layer is something to build, run, and pass through — more checks, more configuration, more places a
misconfiguration can lock out legitimate users. Layers must be genuinely independent to pay off; piling
on same-kind controls adds cost without adding much real depth.

## Names you'll meet

- **Defense in depth** — multiple independent layered controls.
- **Layered security** — controls at the edge, network, host, application, and data levels.
- **Network firewall / security group** — instance- or subnet-level filtering of allowed traffic (a
  layer).
- **Web application firewall (WAF)** — filtering of malicious requests at the application edge (a layer).
- **Zero trust** — verify every request on its own merits, even inside the perimeter; never trust by
  network location alone.
- **Network segmentation** — internal walls so a foothold in one tier can't freely reach the others.

## Connects to

- **Back → 017 (least privilege).** Because a key *will* leak, access control can't be your only defense —
  layer others behind it.
- **Back → 014 (redundancy + independence).** Same math, inverted: redundancy needs independent *copies*;
  defense in depth needs independent *controls*. Independence is the shared key.
- **Forward → 019 (attack surface).** One of the layers is simply *not exposing* most of the system — the
  cheapest control is the door that doesn't exist.

## Drill prompts

- Why not rely on one strong control, and what's the fix? *(Any single control fails eventually — a
  single point of total failure; layer independent controls of different kinds.)*
- Why must the layers be *different in kind*? *(Same-kind controls share weaknesses — one exploit beats
  all; different kinds fail independently.)*
- A database sits behind a perimeter firewall, but a compromised internal app reads all of it — the
  missing principle and one inner layer? *(Defense in depth / zero trust; segment so only the app tier
  reaches the DB, plus identity checks and encryption at rest.)*
