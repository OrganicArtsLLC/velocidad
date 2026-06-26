# 019 — Expose as little as possible; the smallest attack surface is the safest

**Cluster:** Security & boundaries

## The principle

Every component you expose to the outside is something an attacker can reach and try. The most powerful
security move isn't a better lock on a door — it's *not having the door* at all. Most of a system has no
reason to face the public internet: databases, internal services, application servers. Put them where
the outside can't reach them, and you remove whole categories of attack for free.

So you divide the system into a small public zone holding only what genuinely must face the world, and a
large private zone holding everything else, with a guarded boundary between them where identity is
checked. The total count of exposed entry points is your attack surface, and the discipline is to keep it
as small as the job allows.

## Picture it

A building has a public lobby anyone can walk into — that's where you want the world — and back rooms,
the archive, the vault, reachable only *through* the building, never from the sidewalk. Nobody puts the
safe in the lobby. The valuable, fragile things live deep inside, past a checkpoint. The cardinal sin is
a door from the street straight into the vault: a database with a public address is exactly that.

## Why it must be true

Attack surface is the set of reachable entry points; risk scales with it, because each exposed endpoint
is independently probeable by anyone on the network it faces. Reducing exposure removes attacks
unconditionally — an unreachable service can't be hit regardless of its own flaws. So you place
components by necessity: public-facing only what must be (the edge, the load balancer, the public API),
everything else in a private zone with no inbound route from the internet, and narrow, controlled paths
(outbound-only egress, a single hardened admin path) where private components need limited contact with
the outside.

The boundary between public and private is a *trust boundary* — the line where you stop assuming and
start verifying. In a cloud, this is also where the shared-responsibility split lives: the provider
secures the underlying infrastructure, but *what you choose to expose* is yours. Minimizing the surface
is the one control that makes every other control's job smaller.

## The trade-off

A small surface buys whole categories of attack removed at no ongoing cost, and pays in convenience:
private components are harder to reach for legitimate administration and integration, so you must build
controlled paths (jump hosts, managed access, outbound-only gateways) instead of just connecting
directly. Over-isolating can slow development and tempt people into risky shortcuts; the goal is *as
small as the job allows*, not smaller.

## Names you'll meet

- **Attack surface** — the set of exposed, reachable entry points.
- **Trust boundary** — the line where public meets private; where you verify.
- **Public vs private network segment** — has, or has no, route in from the internet.
- **Private network / VPC** — the isolated network you place components within.
- **Outbound-only gateway (NAT)** — lets private components reach out without being reachable.
- **Bastion / managed session access** — a controlled admin path to private components without public
  addresses.

## Connects to

- **Back → 018 (defense in depth).** Not-exposing is the cheapest, outermost layer — the door that
  doesn't exist needs no lock.
- **Back → 013 (blast radius).** Public/private segmentation is fault isolation for *reachability* — a
  compromised public edge still can't directly touch the private interior.
- **Forward → 020 (encryption).** Even inside the private zone you assume a breach and protect the data
  itself — the next, innermost layer.

## Drill prompts

- What's the most powerful security move, and the rule it implies? *(Don't expose what doesn't need
  exposing; minimize attack surface and keep valuables private behind a guarded boundary.)*
- Why does reducing exposure beat hardening exposure? *(An unreachable service can't be attacked
  regardless of its flaws; it removes attacks unconditionally.)*
- A database has a public address open to the world — wrong placement and the fix? *(Move it to a private
  segment with no public route, reachable only from the app tier.)*
