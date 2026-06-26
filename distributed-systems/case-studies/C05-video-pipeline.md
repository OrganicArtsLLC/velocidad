# C05 — Designing a Video-Processing Pipeline

**Headline principles:** 006, 009, 010, 011, 012, 021, 022, 023, 024

---

## The system

A user uploads a video; the system transcodes it into many renditions (resolutions and formats) and makes
it streamable.

## Requirements

- **Functional:** accept upload → transcode to many renditions → deliver.
- **The scale that makes it hard:** transcoding is *slow* (minutes), *heavy* (CPU-bound), and *bursty*;
  the upload must feel instant; source and outputs are large; delivery is global.

## The shape

"Slow + heavy + bursty + don't-make-them-wait" is the exact fingerprint of **principle 010** — hand the
work off, don't hand it across. Upload and transcoding must be fully decoupled.

## The design walk

1. **Upload to object storage**, return immediately ("got it, processing"). *(Mind data gravity — keep
   compute near the data, 024.)*
2. **Drop a transcode job on a queue.** *(010 — the heart of the design.)*
3. **Elastic fleet of workers** pulls jobs and transcodes; each job can restart safely, so run on cheap
   **interruptible** capacity *(022)*. The fleet **scales with queue depth** — a flood lengthens the
   queue, more workers spin up; quiet → near-zero. *(009, 021.)*
4. **Idempotent workers** — a retried job doesn't double-output or double-charge. *(012.)*
5. **Renditions back to storage; a "video ready" event fans out** to update the catalog and notify the
   user. *(011.)*
6. **Deliver via CDN** to viewers worldwide *(006)*. Cold, rarely-watched outputs tier down to cheaper
   storage *(023)*.

## The hard part — there almost isn't one

Because the decoupling is clean, every hard thing becomes easy: a *spike* becomes a longer queue
(load-leveling), a *worker death* becomes a re-queued job, *cost* becomes elastic, *slowness* becomes
invisible. The "hard part" of slow heavy work *dissolves* the moment nothing waits for it — the purest
demonstration of the queue's power.

## The principle map

| Design decision | Principle(s) |
|-----------------|--------------|
| Upload returns immediately; job queued | 010 |
| Interruptible workers on reclaimable capacity | 022 |
| Fleet scales with queue depth / pay-per-use | 009, 021 |
| Idempotent jobs (safe retries) | 012 |
| "Ready" event fan-out | 011 |
| CDN delivery; tier cold renditions | 006, 023 |
| Compute near the data | 024 |

## Concrete building blocks

- **Storage:** object storage for source and renditions.
- **Jobs:** a message queue between upload and the worker fleet.
- **Transcode:** an elastic worker fleet on interruptible compute (or a managed transcoding service).
- **Orchestration:** functions or a workflow engine to coordinate stages.
- **Notify:** a pub/sub topic for the "ready" event.
- **Deliver:** a CDN.

## What this case teaches

Decoupling is a force multiplier: one clean queue between producer and consumer turns bursts, failures,
cost, and latency from four separate problems into non-problems.
