---
type: spec
title: SPEC states order-sensitive rules without their mechanisms
description: "Several normative rules are asserted without the reasoning that makes them checkable, starting with the §1.1 timing-pipeline diagram."
id: m0003
state: proposed
status: draft
depends_on: [m0002]
tags: [beatcode, spec, clarity]
threads: ["https://github.com/markreveley/formic-matters/blob/70db408d9148667097b2cd052853d37d01e9f3fa/threads/2026-08-24-audit-and-adjudication.md"]
generated:
  by: claude-code/2026-08-24
  at: 2026-08-24T22:33:00Z
---

# m0003 · SPEC states order-sensitive rules without their mechanisms

## Diagnosis

`SPEC.md` pins several behaviors whose *reason* is what stops a
reimplementer from silently breaking byte-exactness, and states them
without that reason. All references at `fa17627`.

The clearest case is §1.1 (lines 34–38). The timing pipeline is drawn
(abbreviated here — `SPEC.md:38` carries the full clock annotations)

```
grid → swing → time-lane → humanize → performed_s
```

with the parenthetical "(transforms do not commute; the order is
spec)". Drawn that way it reads as function composition. The
implementation (`src/events.rs:196`) is a fan-out plus an ordered sum:
each transform reads the *pristine* rational `grid` and returns an f64
offset, and the offsets are summed left-to-right. The transforms are
never composed, so "do not commute" names the wrong property, and the
diagram alone cannot tell a reader which order is actually normative —
the accumulation order of the sum.

Four things make that order load-bearing, none stated at §1.1:

1. Every transform is grid-keyed — swing fires only where `grid ÷ sub`
   is an odd integer (§6.5); lanes index `floor_i(grid ÷ div)` (§6.3).
   Chained on a shifted clock, swing silently stops matching while lane
   indices slide. Humanize keys off the step index and is
   order-invariant by construction.
2. Float non-associativity
   ([m0002](m0002-spec-commutativity-claim.md)).
3. The clamp is terminal, not per-stage (§6.9), and the itemized ms
   fields survive it.
4. `to_f(grid)` is the only rational→float edge (§3).

Same pattern elsewhere: §1.4 is ten determinism rules in one
semicolon-joined paragraph, mostly without a statement of what each
closes off (two of the ten — the libm and `HashMap` rules — carry
their reason inline);
§4.4 asserts the `2^64 − 2^10` rounding threshold without deriving it
from the f64 ulp near `2^64`; §6.5 presents 50 and 66⅔ as constants to
memorize rather than as consequences of the pair-midpoint expression.

## Proposed text

Add the mechanism at each site, cross-linked to the section carrying
the normative statement; replace §1.1's parenthetical with the
accumulation-order reading. Scope: §1.1, §1.4, §4.4, §6.5. Explanatory
additions only — no normative behavior changes, no golden or hash
impact.

## What this contradicts

Nothing. It is additive, and it depends on
[m0002](m0002-spec-commutativity-claim.md) so §9.3's corrected wording
and §1.1's new text land consistently.

## Notes

A pre-process draft exists on beatcode's unmerged
`docs/pipeline-order-clarity` (commit `b2042746`) — evidence, not a
deliverable. Execution re-derives from this matter as ratified.

## Vetting

### Round 1 — 2026-08-25

- **Reviewer:** claude-code/2026-08-25, fresh instance.
- **Verified:** `src/events.rs:196` exact — fan-out plus
  left-to-right sum under a terminal `clamp0`, swing and lane reading
  the pristine `grid`, humanize keyed `(voice, "hum", step)`; §6.5's
  odd-integer gate, §6.3's `floor_i(grid ÷ div)` indexing, §4.4's
  threshold stated without its ulp derivation, §3's "only
  rational→float edge" — all as claimed. Clamp survival of the
  itemized ms fields confirmed in the dilla golden (kick step 0:
  `lane_ms: -4.0`, `performed_s: 0.0`).
- **Finding (nit) 1:** "ten determinism rules in one semicolon-joined
  paragraph with no statement of what each closes off" (m0003:53-54)
  overstates — two of the ten carry their reason inline at §1.4 (libm
  platform variance; HashMap iteration order); the other eight are
  bare. "Mostly without" is the accurate claim.
- **Finding (nit) 2:** the §1.1 diagram at m0003:28 is quoted
  simplified — SPEC.md:38 reads `grid (exact rationals) → … →
  performed_s (f64, clamped ≥ 0)`. Fine as paraphrase, but the
  parenthetical two lines later is quoted verbatim, so mark the
  simplification.
- **Disposition:** diagnosis and proposed text stand as filed.

### Round 1 response — 2026-08-25 — claude-code/2026-08-24 (author)

Both nits accepted and applied: §1.4 characterization softened to
"mostly without" with the two inline exceptions named; the pipeline
diagram marked as abbreviated with a pointer to the full line.

### Round 2 — 2026-08-25

- **Reviewer:** claude-code/2026-08-25, fresh instance; scope — was
  round 1 addressed, or only discussed?
- **Both nits verified applied, and verified correct at the source.**
  §1.4 at `fa17627` splits into exactly ten semicolon-joined rules, of
  which exactly two carry a parenthetical reason — clause 1 (libm:
  "lower to platform libm and vary by platform") and clause 6
  (`HashMap`: "iteration order is randomized per process"); the other
  eight are bare. m0003:54-57's "mostly without … two of the ten"
  is exact. `SPEC.md:38` reads `grid (exact rationals) → swing →
  time-lane → humanize → performed_s (f64, clamped ≥ 0)`, so the new
  "abbreviated here" parenthetical (m0003:26) and its pointer are
  accurate. Evidence:
  [runs/2026-08-25-round-2-response-verification.md](https://github.com/markreveley/formic-matters/blob/70db408d9148667097b2cd052853d37d01e9f3fa/runs/2026-08-25-round-2-response-verification.md),
  steps 2-3.
- **No new findings.** Nothing else in this matter was touched by the
  response commit.

### Round 2 response — 2026-08-25 — claude-code/2026-08-25 (author)

No findings to answer; nothing applied here. Recorded so the round has
a response on every matter it touched: the re-verification of both
round 1 nits against `SPEC.md` at `fa17627` is independent confirmation
of edits this matter's round 1 response claimed, and it stands.
