---
okf_version: "0.2"
---

# Matters

Derived from the frontmatter of every matter in this directory.
**Do not hand-edit** — run `tools/gen-index.py`. See [m0008](https://github.com/markreveley/formic-matters/blob/70db408d9148667097b2cd052853d37d01e9f3fa/matters/m0008-matter-tooling.md), the framework's tooling matter.

## proposed

| | Type | Tags | Matter | Description |
|---|---|---|---|---|
| `m0002` | fix | beatcode, spec, determinism | [SPEC §9.3 justifies mix order with a false commutativity claim](m0002-spec-commutativity-claim.md) | SPEC §9.3 says float addition does not commute; commutativity is not what fails — associativity is. |
| `m0003` | spec | beatcode, spec, clarity | [SPEC states order-sensitive rules without their mechanisms](m0003-spec-order-rules-lack-mechanism.md) | Several normative rules are asserted without the reasoning that makes them checkable, starting with the §1.1 timing-pipeline diagram. |
| `m0004` | fix | beatcode, spec, render, claims-dag | [SPEC §9.4 track length mixes an index with a count](m0004-track-length-index-count.md) | frames = last + 22050 yields a 22,049-frame silent tail, one short of the comment's half second; the tail is the oracle's own behavior — resolved, prose-only fix. |
| `m0005` | fix | beatcode, docs | [beatcode README claims the implementation does not exist](m0005-readme-stale-status.md) | README says Specification seed and heads its command list Commands (once built); the implementation is merged to main with all tests green. |
| `m0009` | spec | beatcode, spec, process | [SPEC-GAPS becomes a derived view over matters](m0009-spec-gaps-to-matters.md) | The nine SPEC-GAPS entries are retroactively filed spec matters; SPEC-GAPS.md is regenerated from them, not maintained by hand. |

## executed

| | Type | Tags | Matter | Description |
|---|---|---|---|---|
| `m0010` | spec | beatcode-dev, bootstrap | [Framework installation record](m0010-framework-installation.md) | beatcode-dev adopts Formic Matters: the specification copied verbatim at the ratified commit, the conventions and tooling, and the imported beatcode matters — recorded per §14, reaching executed on operator acknowledgment per §11. |

## Ordering

`implements` names the spec a matter serves; `depends_on` constrains execution order.

| Matter | Implements | Depends on |
|---|---|---|
| `m0003` | — | m0002 |
