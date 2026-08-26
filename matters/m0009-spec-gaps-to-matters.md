---
type: spec
title: SPEC-GAPS becomes a derived view over matters
description: "The nine SPEC-GAPS entries are retroactively filed spec matters; SPEC-GAPS.md is regenerated from them, not maintained by hand."
id: m0009
state: proposed
status: draft
tags: [beatcode, spec, process]
generated:
  by: claude-code/2026-08-24
  at: 2026-08-24T22:33:00Z
---

# m0009 · SPEC-GAPS becomes a derived view over matters

## Diagnosis

`SPEC-GAPS.md` in beatcode (nine numbered entries at `fa17627`) is
already matters-shaped: each entry is a section citation, a decision,
and a rationale — the same artifact as a `spec` matter in state
`executed`, maintained in a parallel format. Left as-is there are two
collections recording decisions about beatcode, and they will drift.

## Proposed text

- Each SPEC-GAPS entry becomes a `spec` matter filed via the
  retroactive path (doctrine §11) — evidence attached, reaching
  `executed` on operator acknowledgment — tagged `gap`.
- `SPEC-GAPS.md` is **regenerated** from the query
  `type: spec, state: executed, tags: [gap]` rather than deleted —
  preserving the one readable document a builder wants, while making it
  derived (doctrine §12).

## What this contradicts

Nothing in normative text. It retires SPEC-GAPS.md as a hand-maintained
source and re-founds it as a view.

## Dependency

The retroactive path is designed (doctrine §11); what this waits on is
index/view generation from the framework's matter tooling —
[m0008](https://github.com/markreveley/formic-matters/blob/70db408d9148667097b2cd052853d37d01e9f3fa/matters/m0008-matter-tooling.md),
pinned at its pre-split text — filing nine matters by hand without it
is churn. A cross-collection `depends_on` is not expressible (§7), so
the constraint this matter's frontmatter carried in the framework
collection stands here as prose: execution waits on that tooling
being available to this installation.
