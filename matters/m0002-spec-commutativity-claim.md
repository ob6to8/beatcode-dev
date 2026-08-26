---
type: fix
title: SPEC §9.3 justifies mix order with a false commutativity claim
description: "SPEC §9.3 says float addition does not commute; commutativity is not what fails — associativity is."
id: m0002
state: proposed
status: draft
tags: [beatcode, spec, determinism]
threads: ["https://github.com/markreveley/formic-matters/blob/70db408d9148667097b2cd052853d37d01e9f3fa/threads/2026-08-24-audit-and-adjudication.md"]
generated:
  by: claude-code/2026-08-24
  at: 2026-08-24T22:33:00Z
---

# m0002 · SPEC §9.3 justifies mix order with a false commutativity claim

## Diagnosis

`SPEC.md` §9.3 (lines 750–752 at `fa17627`) justifies the normative
mix-accumulation order with:

> Order is normative: float addition does not commute in rounding, so
> overlapping events must be summed in exactly this order.

IEEE-754 addition **is** commutative: for the finite operands in play,
`a + b` and `b + a` produce bit-identical results, sign of zero
included. What fails is **associativity** — `(a + b) + c ≠ a + (b + c)`
in general. Permuting a multi-term summation changes the result because
it re-associates the sum, not because two-operand addition is
order-dependent.

The conclusion §9.3 draws is correct; the stated reason is not. §9.3 is
normative text a reimplementer reads to decide which reorderings are
safe, so a wrong reason there can license a wrong optimization. The
spec's own §6.2 (lines 484–488) states the same constraint correctly
("strict left-to-right association"), which makes §9.3 the outlier.

**Scope.** §9.3 only. §1.1's "(transforms do not commute; the order is
spec)" is a different statement — its defect is a missing mechanism,
not a false claim about float arithmetic — and belongs to
[m0003](m0003-spec-order-rules-lack-mechanism.md). The first attempt's
version of this matter conflated the two sites; the audit separated
them.

## Proposed fix

Restate §9.3 in association terms: float addition is commutative but
not associative, so any permutation of the overlapping-event sum
re-associates it and changes its rounding; the sorted-event,
frame-order accumulation is therefore normative.

## Notes

A pre-process draft of a similar change exists in beatcode on the
unmerged branch `docs/pipeline-order-clarity`, commit `b2042746`. It is
evidence, not a deliverable — it predates this process. Execution
re-derives from this matter as ratified.
