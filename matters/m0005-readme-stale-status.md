---
type: fix
title: beatcode README claims the implementation does not exist
description: "README says Specification seed and heads its command list Commands (once built); the implementation is merged to main with all tests green."
id: m0005
state: proposed
status: draft
tags: [beatcode, docs]
runs: ["https://github.com/markreveley/formic-matters/blob/70db408d9148667097b2cd052853d37d01e9f3fa/runs/2026-08-24-render-reproduction.md"]
generated:
  by: claude-code/2026-08-24
  at: 2026-08-24T22:33:00Z
---

# m0005 · beatcode README claims the implementation does not exist

## Diagnosis

`README.md` (lines 40–45 and 54 at `fa17627`) states:

> **Status.** Specification seed. This repo currently contains the
> complete behavioral spec, its golden conformance vectors, and the
> example scores; the implementation is built from them per PLAN.md.

and heads the command list "Commands (once built)".

The implementation is merged to `main`: `fa17627` is the merge of
PR #2, with 14 modules under `src/`, 48 tests green across 15 binaries,
and render hashes committed to `goldens/renders-v0.1.txt` — reproduced
independently in
[runs/2026-08-24-render-reproduction.md](https://github.com/markreveley/formic-matters/blob/70db408d9148667097b2cd052853d37d01e9f3fa/runs/2026-08-24-render-reproduction.md).

A reader arriving at the repo is told the product does not exist.

## Proposed fix

Update the Status section and the command heading to reflect a built,
verified v0.1. How the repo should *position* itself — spec-first
reference with a conforming implementation, versus working tool — is
the operator's call and is settled during vetting of this matter, not
assumed; that choice determines the wording.
