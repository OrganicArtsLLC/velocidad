# 017 — Give every identity exactly the access it needs; every extra permission is a door for your worst day

**Cluster:** Security & boundaries

## The principle

The damage of a compromised identity is set not by how careful its holder is, but by what its access
*could reach*. A credential will eventually leak — phishing, a reused password, a laptop on a train — so
the size of your worst day is decided in advance, by how much each identity was allowed to touch.

So you invert the default. Instead of granting broad access and clawing it back when something goes
wrong, you start from *zero* and add back only the specific permissions a job genuinely requires. Deny
by default; grant the narrow exception on purpose. Over-granting is convenient and quietly pre-decides a
catastrophe; least privilege turns the same leak into a contained incident.

## Picture it

The night janitor needs the front door, the supply closet, and the offices he cleans — and nothing else.
Handing him the *master key* (because it was easier than thinking about which doors he needs) means the
day that key is lost or copied, the rare-manuscripts vault is open too. The fix is a key ring with
exactly his doors on it. Every key on a ring is a door an attacker gets for free the moment they get the
person.

## Why it must be true

Access is the attacker's reach. A compromised actor can do precisely what that actor was permitted to do
— no more, no less — so scoping permissions tightly bounds the blast radius of any single compromise
(it's 013's containment applied to authorization). The strongest forms minimize not just *what* but *how
long*: temporary, short-lived credentials that expire beat long-lived secrets sitting on a server,
because a stolen short-lived key is useless tomorrow and there is no master credential to find.

The cost is up-front thought — you must enumerate what each role actually needs — and that friction is
exactly why broad grants happen. Least privilege is a discipline against convenience, and its payoff is
paid out only on the bad day, which is why it's so easy to skip and so important not to.

## The trade-off

Least privilege buys a small blast radius per compromise and pays in operational friction: someone must
work out, and keep updating, the minimal permission set for each role, and over-tightening can break
legitimate work and generate access requests. Broad grants buy convenience now and pay catastrophically
later. Short-lived credentials buy safety and pay in the machinery to issue and rotate them.

## Names you'll meet

- **Least privilege** — minimum access required, nothing more.
- **Deny by default** — start from zero; grant narrow exceptions deliberately.
- **Access policy** — the rules scoping who can do what to which resource.
- **Role / assumed credentials** — temporary, scoped, expiring access; preferable to long-lived keys.
- **Scoped / resource-level permissions** — grant on *this* specific resource, not the whole service.
- **Separation of duties** — no single identity can both perform and approve a sensitive action.

## Connects to

- **Opens the security cluster.** The first rule every breach report returns to.
- **Back → 013 (blast radius).** Least privilege is containment applied to permissions — scoping how far
  a compromised credential can reach.
- **Forward → 018 (defense in depth).** Because a key *will* leak despite best efforts, you never rely on
  access control alone — you layer other controls behind it.

## Drill prompts

- How much access should an identity get, and what's the default? *(Exactly what its job needs and no
  more; deny by default, grant the minimum on purpose.)*
- Why prefer short-lived assumed credentials over long-lived keys? *(They expire and aren't a master key
  to steal off a server — a stolen one is useless tomorrow.)*
- A service needs to write one specific resource — the right scope vs the lazy one? *(A role scoped to
  that one resource; not full access to the whole service.)*
