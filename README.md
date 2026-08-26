# beatcode-dev

The first consumer installation of
[Formic Matters](https://github.com/markreveley/formic-matters), the
matter framework — governing
[beatcode](https://github.com/markreveley/beatcode), the instrument,
and this installation itself.

Every change to a governed system begins as a **matter** here:
proposed, vetted, ratified by the operator, then executed by a dev
agent the operator launches (spec §3). The normative definition is the
installed copy at [`doctrine/matters.md`](doctrine/matters.md) —
byte-verbatim from the framework at its ratified commit, pinned and
verifiable via [`doctrine/installation.md`](doctrine/installation.md).
The collection is [`matters/`](matters/index.md).

**Provenance, dated (spec §9.4).** Installed 2026-08-26 per the
framework's split matter
([m0012](https://github.com/markreveley/formic-matters/blob/70db408d9148667097b2cd052853d37d01e9f3fa/matters/m0012-formic-matters-split.md)),
recorded on this collection's first matter,
[m0010](matters/m0010-framework-installation.md). The collection
imports the beatcode-facing matters m0002–m0005 and m0009 from the
framework with IDs preserved; new IDs allocate from m0010. Slots
m0001 and m0006–m0008 are vacant here, deliberately — those are the
framework's own self-hosted matters.

## Layout

```
doctrine/matters.md       the installed Formic Matters specification (verbatim, pinned)
doctrine/installation.md  the installation record — framework repo, source commit, hash
matters/                  flat collection, one file per matter
matters/index.md          derived listing — regenerate with tools/gen-index.py, never hand-edit
threads/                  verbatim session exports; primary sources
runs/                     append-only verification records
tools/                    interim scripts, copied from the framework (m0008 is the real tooling)
```

The collection is markdown with YAML frontmatter — OKF v0.2 as a
documented dialect (spec §12): readable with no tooling, links as
plain relative paths, one concept per file. Cross-collection
references into the framework are pinned absolute URLs at immutable
commits (spec §9.4; m0012 plan step 4).
