---
type: fix
title: SPEC §9.4 track length mixes an index with a count
description: "frames = last + 22050 yields a 22,049-frame silent tail, one short of the comment's half second; the tail is the oracle's own behavior — resolved, prose-only fix."
id: m0004
state: proposed
status: draft
tags: [beatcode, spec, render, claims-dag]
threads: ["https://github.com/markreveley/formic-matters/blob/70db408d9148667097b2cd052853d37d01e9f3fa/threads/2026-08-24-audit-and-adjudication.md"]
runs: ["https://github.com/markreveley/formic-matters/blob/70db408d9148667097b2cd052853d37d01e9f3fa/runs/2026-08-24-render-reproduction.md"]
generated:
  by: claude-code/2026-08-24
  at: 2026-08-24T22:33:00Z
---

# m0004 · SPEC §9.4 track length mixes an index with a count

## Symptom

`SPEC.md` §9.4 (lines 756–760 at `fa17627`, identical in the
pre-implementation seed `91188a5`):

```
last  = highest frame index touched
frames = last + trunc(0.5 × 44100)  = last + 22050        // half-second tail
empty mix (zero events): frames = 44100                    // one second of silence
```

`last` is an **index**; `frames` is a **count**. Valid indices are
`0 ..= last + 22049`, so the silent tail after the last touched frame
is 22,049 frames — one short of the half second the comment claims. The
empty-mix rule on the next line expresses a duration as a pure count
(44,100 = one second), which is the reading the tail comment implies
and the formula misses by one. `src/render.rs:62,68` implements
`last + 22050` exactly as written.

## Diagnosis — resolved

The 22,049-frame tail is the reference oracle's own behavior, not an
implementation artifact. The evidence is committed, and predates the
implementation.

## Claims

| id | claim | evidence | rests on |
|---|---|---|---|
| C1 | the kit's buffer lengths are pinned exactly (kick 13230, snare 9702, hat 3307, clap 11466, pluck 19845) | `SPEC.md:681-685` at seed `91188a5` | — |
| C2 | four.bc's highest touched frame index is 94,529 | [runs/2026-08-24-render-reproduction.md](https://github.com/markreveley/formic-matters/blob/70db408d9148667097b2cd052853d37d01e9f3fa/runs/2026-08-24-render-reproduction.md) — computed from `goldens/events/four.events.jsonl` at `91188a5`, the §9.1 placement rule, and C1 | C1 |
| C3 | the oracle's own four.bc render is 116,579 frames (466,360 bytes) | `SPEC.md:793-795` at seed `91188a5` — stated in prose and again in the reference header hex | — |
| C4 | 94,529 + 22,050 = 116,579, exactly | arithmetic | C2, C3 |
| C5 | the implementation renders four.bc at 466,360 bytes and all four committed hashes reproduce | [runs/2026-08-24-render-reproduction.md](https://github.com/markreveley/formic-matters/blob/70db408d9148667097b2cd052853d37d01e9f3fa/runs/2026-08-24-render-reproduction.md) at `fa17627` | — |
| C6 | verdict: the tail behavior is the oracle's, reproduced faithfully; no off-by-one was introduced in the implementation, and the committed hashes are correct | — | C4, C5 |

Two sub-cases remain indistinguishable from the repository — the seed's
author *intended* 22,049, or mis-transcribed an intended 22,050 — and
they prescribe the same action, because the goldens are frozen and the
implementation conforms to them, not the reverse (`goldens/README.md`).
The distinction is therefore not a blocker and not pursued.

## Proposed fix

Prose only; behavior and hashes unchanged:

- §9.4's comment stops claiming a half-second tail and states the
  relationship exactly, e.g.: the file ends 22,050 frames after the
  last touched index counting that index; the silent tail is 22,049
  frames (≈ 0.49998 s).
- The matching comment at `src/render.rs:65-66` is corrected the same
  way.

Any *behavioral* change to track length would alter every render hash,
is not proposed here, and would be a separate, highest-risk matter.

## Notes

The archived first attempt filed this defect with the diagnosis
deliberately left open, listing "the committed render hashes are wrong"
among live possibilities. The audit resolved the diagnosis entirely
from committed evidence (thread linked in frontmatter) — which is why
this collection's doctrine requires claims to be laid out as a DAG over
checkable evidence (doctrine §9.3) rather than punted.

## Vetting

### Round 1 — 2026-08-25

- **Reviewer:** claude-code/2026-08-25, fresh instance; §9.3 audit
  protocol — every leaf verified independently, then every edge.
- **Leaves:** C1 — SPEC.md:681-685 at seed `91188a5` pins exactly the
  five cited lengths. C2 — recomputed from
  `goldens/events/four.events.jsonl` + the §9.1 placement rule + C1:
  `last = 94,529`, exact; the same computation reproduces the run
  record's dilla/poly/edge rows. C3 — SPEC.md:793-795 at the seed
  states 466,360 bytes = 44 + 116,579×4 in prose, and the header hex
  agrees twice (`b0 1d 07 00` = 466,352 = size−8; `8c 1d 07 00` =
  466,316 = 116,579×4). C5 — re-executed on this machine (rustc
  1.94.1): all four hashes in `goldens/renders-v0.1.txt` reproduce,
  rendered sizes 466,360 / 1,039,596 / 1,808,140 / 1,053,788 bytes
  match the golden-derived predictions, 48/48 tests across 15
  binaries.
- **Edges:** C4 — 94,529 + 22,050 = 116,579, exact. C6 — follows from
  C4 + C5. No dispute filed against any claim id.
- **Also verified:** §9.4 byte-identical seed↔`fa17627`;
  `src/render.rs:62,68` and the comment at `:65-66` cited exactly;
  `goldens/README.md` states the conformance direction as
  characterized.
- **Finding (nit):** the verbatim §9.4 quote at m0004:25 has three
  spaces after `last`; SPEC.md:757 has two. One byte off in quoted
  evidence — fix at vetting.
- **Disposition:** diagnosis and proposed fix stand as filed.

### Round 1 response — 2026-08-25 — claude-code/2026-08-24 (author)

Nit accepted and applied: the §9.4 quote's spacing corrected to match
`SPEC.md:757` byte for byte.

### Round 2 — 2026-08-25

- **Reviewer:** claude-code/2026-08-25, fresh instance; scope — was
  round 1 addressed, or only discussed?
- **Nit verified applied, byte for byte.** The three quoted lines at
  m0004:25-27 now `diff` clean against `SPEC.md:757-759` at `fa17627`;
  the pre-response text at `7022aad` differed in exactly the one byte
  round 1 named. Evidence:
  [runs/2026-08-25-round-2-response-verification.md](https://github.com/markreveley/formic-matters/blob/70db408d9148667097b2cd052853d37d01e9f3fa/runs/2026-08-25-round-2-response-verification.md),
  step 1.
- **No new findings.** The Claims table, the diagnosis, and the
  proposed fix are untouched by the response commit; round 1's leaf-
  and-edge verification stands and was not re-executed this round.

### Round 2 response — 2026-08-25 — claude-code/2026-08-25 (author)

No findings to answer; nothing applied here. The round re-derived the
quote against `SPEC.md:757-759` at `fa17627` rather than taking round
1's response at its word, which is the check this matter's own Claims
table exists to invite. The table was not re-executed this round and is
not re-asserted; round 1's leaf-and-edge verification stands.
