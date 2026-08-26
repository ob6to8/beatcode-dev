# Installation record — Formic Matters

This repository installs the Formic Matters framework by verbatim
copy, pinned (framework spec §14; mechanism ratified on the
framework's
[m0012](https://github.com/markreveley/formic-matters/blob/70db408d9148667097b2cd052853d37d01e9f3fa/matters/m0012-formic-matters-split.md)).

- **Framework repository:** <https://github.com/markreveley/formic-matters>
- **Source commit** (the m0001-ratified commit):
  `85fe4511326a30516ed2bf86a2e2a2b9d05c3d25`
- **sha256 of the copied `doctrine/matters.md`:**
  `5adc0aafe92c5ead0269c681c8802516572765cf77b22549ea5acc45d8dda7bd`
- **Installed:** 2026-08-26, recorded on
  [m0010](../matters/m0010-framework-installation.md), this
  installation's first matter.

Anyone verifies the installation without trusting any agent — two
commands, the same shape the framework README uses for a ratification
(the first runs in a clone of the framework repository, the second
here):

```
git show 85fe4511326a30516ed2bf86a2e2a2b9d05c3d25:doctrine/matters.md | sha256sum
sha256sum doctrine/matters.md        # here, over this repository's copy
```

The two agreeing — and equal to the recorded hash above — means the
copy is the ratified text. A byte-level `diff` of the same two inputs
needs both repositories on one machine; the hashes are the portable
form.

The copy is byte-verbatim, so its internal relative references
describe the framework repository's tree, not this one: links into
`../threads/` and `../runs/`, and to framework matters (m0001,
m0006–m0008, m0011–m0013), resolve against
<https://github.com/markreveley/formic-matters/tree/85fe4511326a30516ed2bf86a2e2a2b9d05c3d25>,
the source commit. The §11 reference to m0009 happens to resolve here
as well, because m0009 lives in this collection.

**Upgrades are matters.** This installation re-copies at a newer
ratified framework commit by filing a `spec` matter in its own
collection ("adopt framework at `<commit>`"); framework upgrades go
through this installation's own process.
