# 020 — Assume the channel is intercepted and the disk is stolen; make the data useless without a key

**Cluster:** Security & boundaries

## The principle

Every other control tries to keep the attacker out; this one assumes they got in anyway. A disk walks out
a back door, a connection is sniffed on the wire — assume it *will* happen, and the question becomes
whether the stolen copy is readable or just noise. Encrypt the data, and a breach yields gibberish
instead of secrets.

Data is exposed in two states — *at rest* (sitting on disk) and *in transit* (moving over the network) —
so it must be protected in both. But encryption doesn't remove the problem; it *concentrates* it. Now the
entire safety of the data rests on the keys: lose them and you can't read your own records; store them
next to the data and a single theft takes both. So the real discipline isn't the cipher — it's guarding
the keys, separate from what they unlock.

## Picture it

A document is vulnerable when it sits in the archive (a thief lifts the whole ledger) and when it moves
(a courier intercepted on the road). So every ledger on the shelf is written in a cipher only the key
unlocks, and every document a courier carries is sealed in a strongbox for the journey. Steal the shelf
or stop the courier — you hold gibberish. *Unless* the key was taped to the box: keep the keys in their
own guarded vault, never beside the data.

## Why it must be true

Encryption makes ciphertext computationally useless without the key, so it converts "the attacker has the
data" into "the attacker has noise" — *provided* the key is out of reach. That proviso moves the whole
security problem from a large, hard-to-guard surface (all the data, everywhere) to a small, tractable one
(the keys). Hence the rules that make encryption real: keys live in a dedicated, access-controlled store
*separate* from the data, are rotated, and are governed by least privilege (017) so only the right
identities can use them.

Both states matter because they're different exposures: encryption at rest defeats stolen drives and
database dumps; encryption in transit (TLS) defeats network interception. Doing one and not the other
leaves the matching hole wide open — at-rest encryption is no help if the data crosses the wire in
plaintext.

## The trade-off

Encryption buys "a breach yields nothing readable" and pays in key-management burden and some performance
and operational overhead. The burden is the real cost: keys must be stored apart from the data, access-
controlled, rotated, and recoverable — lose them and the data is gone as surely as if it were deleted; co-
locate them with the data and you've encrypted nothing in practice. Encryption also does not protect data
*in use* (decrypted in memory) without more specialized techniques.

## Names you'll meet

- **Encryption at rest** — stored data is ciphered; a stolen disk or database dump is unreadable.
- **Encryption in transit** — data on the wire is sealed; interception yields gibberish.
- **TLS / HTTPS** — the standard for in-transit encryption.
- **Key management service** — a managed, access-controlled, rotating key store kept separate from the
  data.
- **Customer-managed / self-managed keys** — keys you control and rotate, often for compliance.
- **Key rotation / separation of duties** — keys change over time and live apart from the data they
  protect.

## Connects to

- **Closes the security cluster.** The innermost layer: after small keys (017), many walls (018), and few
  doors (019), protect the data itself so a breach is still survivable.
- **Back → 017 (least privilege).** Key management *is* least privilege applied to the keys — only the
  right identities may use them.
- **Back → 013 / 016 (containment, DR).** Same instinct that ends the resilience cluster: assume failure,
  make its damage small. Encryption makes a successful breach yield nothing.

## Drill prompts

- Assume a breach — how do you make stolen data worthless, and where does the real problem move? *(Encrypt
  at rest and in transit; the problem becomes guarding the keys, kept separate from the data.)*
- Why protect both at rest and in transit? *(Different exposures — stolen disk vs sniffed wire; doing one
  leaves the other hole open.)*
- A DB is encrypted at rest, but the connection is plaintext and the key sits on the same server — name
  the two holes. *(No encryption in transit — use TLS; and the key stored beside the data — use a
  separate, managed key store.)*
