---
type: spec
title: Framework installation record
description: "beatcode-dev adopts Formic Matters: the specification copied verbatim at the ratified commit, the conventions and tooling, and the imported beatcode matters — recorded per §14, reaching executed on operator acknowledgment per §11."
id: m0010
state: proposed
status: draft
tags: [beatcode-dev, bootstrap]
generated:
  by: claude-code/2026-08-26
  at: 2026-08-26T17:36:59Z
---

# m0010 · Framework installation record

## The installation

This repository is the first consumer installation of
[Formic Matters](https://github.com/markreveley/formic-matters),
created by the framework's split matter —
[m0012](https://github.com/markreveley/formic-matters/blob/70db408d9148667097b2cd052853d37d01e9f3fa/matters/m0012-formic-matters-split.md),
ratified by the operator at framework commit `85fe451` and executed
2026-08-26. The governed systems, named as tags (§1):
[beatcode](https://github.com/markreveley/beatcode), the instrument,
and this installation itself.

What the installing commits carry, per §14 and m0012's ratified
installation mechanism:

- `doctrine/matters.md` — the specification, copied **byte-verbatim**
  from the framework at its m0001-ratified commit
  `85fe4511326a30516ed2bf86a2e2a2b9d05c3d25`; sha256
  `5adc0aafe92c5ead0269c681c8802516572765cf77b22549ea5acc45d8dda7bd`,
  verified before the installing commit was made.
- `doctrine/installation.md` — the installation record: framework
  repository, source commit, hash, and the three verification
  commands.
- The directory conventions: `matters/`, `threads/`, `runs/`,
  `tools/`.
- `tools/gen-index.py` — the interim generator, copied from the
  framework at `70db408d9148667097b2cd052853d37d01e9f3fa` with exactly
  one edit, itemized below.
- This matter, the repository README, and the derived
  `matters/index.md`.

## ID allocation

Imported matters keep their framework IDs — m0002–m0005 and m0009 —
and this collection's own sequence allocates above the highest
imported ID (m0012, plan step 3), so this first matter is **m0010**.
Slots m0001 and m0006–m0008 are vacant here, deliberately: they are
the framework's self-hosted matters and never existed in this
collection. §14's "installation's first matter" means first *filed*,
not lowest-numbered.

## The import

m0002–m0005 and m0009 — the `beatcode`-tagged matters — enter this
collection copied from the framework at
`70db408d9148667097b2cd052853d37d01e9f3fa` (its pre-move tree),
bodies verbatim except the two edit classes m0012's ratified plan
licenses, every instance itemized here and in m0012's execution
record:

1. **Re-pins** (plan step 4) — every relative reference into the
   framework's `threads/` and `runs/`, frontmatter citation fields
   included, becomes a pinned absolute reference at
   `https://github.com/markreveley/formic-matters/blob/70db408d9148667097b2cd052853d37d01e9f3fa/…`:
   - m0002 frontmatter `threads:` (1 entry);
   - m0003 frontmatter `threads:` (1 entry); body, Vetting round 2,
     the round-2-response-verification run link;
   - m0004 frontmatter `threads:` and `runs:` (2 entries); body,
     Claims rows C2 and C5, the render-reproduction run links; body,
     Vetting round 2, the round-2-response-verification run link;
   - m0005 frontmatter `runs:` (1 entry); body, Diagnosis, the
     render-reproduction run link.
2. **m0009's dependency** (m0012, "Dependencies across the split") —
   `depends_on: [m0008]` is dropped from the frontmatter (§7:
   `depends_on` is same-collection only) and restated as a prose
   precondition in its `## Dependency` section, whose m0008 reference
   becomes a pinned absolute reference at the same commit.

## Unruled choices (§15)

Recorded here so operator acknowledgment confirms them deliberately:

- the m0010 numbering reading above (first-filed, vacant low slots);
- the installation record's location and form
  (`doctrine/installation.md`, beside the copy);
- the one edit to the copied generator: its generated-index header's
  m0008 link is re-pointed to the pinned framework URL, so the derived
  index never carries a dangling relative link here;
- `.gitkeep` placeholders holding the empty `threads/` and `runs/`
  directories;
- the repository README's wording;
- `Matter: m0010` trailers on the installing commits themselves —
  §8/§14 require trailers only *after* the bootstrap; carried anyway
  for greppability;
- this matter's `type: spec` (the deliverable is text and the review
  question is accuracy — the framework's m0013 precedent) and its use
  of the §11 retroactive path, below;
- the session that performed this installation is exported as a thread
  in the *framework* repository (its execution thread for m0012),
  dated 2026-08-26 — not duplicated here (§9.2 keeps primary sources
  singular).

## Retroactive

Why this path: §14's bootstrap exception — the process is not in this
repository until these commits land, so they cannot be gated by a
prior matter here; §1 names this exception. The work was not
un-vetted: its plan is the framework's m0012, ratified by the operator
at framework commit `85fe451` after review, and its launch is the
operator's own act recorded there (f4) and in the execution thread.
Filed `proposed` with the evidence above; explicit operator
acknowledgment (§11) moves it directly to `executed`. The §7 gate does
not apply on this path; this matter has no dependencies.

## Execution

The installing commits, on this repository's `main` (§14):

- the bootstrap commit,
  `1c73c02495cf08d6e63b0f8c474bd66633b32319` — the specification copy
  (hash verified pre-commit), the installation record, the
  conventions, the tooling copy, this matter, the README, and the
  first derived index;
- the import commit, in which this section's final form lands —
  m0002–m0005 and m0009 with the itemized edits above, and the index
  regenerated over all six matters.

Deviations from m0012's ratified plan: none beyond the itemized,
licensed edits and the recorded unruled choices above. Date:
2026-08-26. Actor: claude-code/2026-08-26, the dev agent the operator
launched against m0012 (framework-side record on m0012 itself).
