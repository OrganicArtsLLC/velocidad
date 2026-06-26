# 013 — You can't prevent failure, so contain it: trap each fault in a blast radius

**Cluster:** Resilience

## The principle

Failure is not an edge case you can engineer away — hardware dies, networks drop, bad deploys ship. So
the useful question is never "how do I stop it from failing" but "when it fails, how *much* fails?" The
answer is decided in advance, by where you draw the walls.

Partition the system into compartments with real isolation between them, and a fault is trapped in the
compartment it started in — partial damage instead of total. The walls don't make failure less likely;
they cap how far it travels. An unpartitioned system turns every local fault into a global one. A
partitioned one keeps the fire in one wing.

## Picture it

A candle tips in one reading room. In a library that's one big open hall, the fire spreads and you lose
everything. In a library with fire doors between the wings, the room burns, the doors seal, and the rest
doesn't even smell smoke. Same candle, same fire — the only difference is where someone drew the walls.
(A ship survives a hull breach the same way: sealed bulkheads, one floods, it still floats.)

## Why it must be true

A shared resource is a shared fate: anything all parts depend on — one process, one database, one pool,
one zone — is a path along which a single fault propagates to everything touching it. Isolation breaks
the path. By giving each partition its own resources (its own capacity, its own failure domain), you
bound the set of things any one fault can reach to that partition alone. This is the same containment
idea that reappears as the circuit breaker (a wall around a slow dependency, 015) and as independent
redundancy (walls so two copies don't share a fate, 014).

## The trade-off

Containment buys a bounded blast radius and pays in complexity and reduced sharing: more partitions mean
more moving parts and more walls to maintain, and capacity sliced into cells is less fluidly shared (a
quiet cell can't lend its spare capacity across the wall to a busy one). You pay that complexity
continuously to avoid paying total loss all at once.

## Names you'll meet

- **Blast radius** — how much fails when one thing fails.
- **Bulkhead** — a wall that isolates one part's failure from the rest (e.g. separate connection pools
  or thread pools per dependency).
- **Fault isolation / failure domain** — the boundary a fault cannot cross.
- **Cell-based architecture** — splitting a system into independent cells that each serve a slice of
  traffic.
- **Availability zone / region** — physically separate facilities; the largest fire doors a cloud gives
  you. Spreading across them survives the loss of one.

## Connects to

- **Opens the resilience cluster.** The earlier wings spread systems out; this principle starts the work
  of keeping them standing when pieces break.
- **Forward → 014 (availability as a product).** Containing failure is half; staying *open* through it
  needs an independent spare ready to carry the load — the redundancy math.
- **Forward → 015 (failure is normal).** The circuit breaker is this same containment, drawn around a
  slow dependency instead of a fire.
- **Back → 009 (health checks).** Detecting and removing a dead worker is containment at the fleet level.

## Drill prompts

- If you can't prevent failure, what do you design for instead? *(Containment — partition so a fault is
  trapped in its blast radius rather than going global.)*
- Why does a shared resource hurt resilience? *(Shared resource = shared fate; it's a path a single
  fault uses to reach everything that depends on it.)*
- An app runs entirely in one failure domain and that domain goes down — name the failure and the fix.
  *(The blast radius was the whole system; spread across independent failure domains.)*
