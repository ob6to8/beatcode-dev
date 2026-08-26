#!/usr/bin/env python3
"""Regenerate matters/index.md from the frontmatter of every matter.

Interim (m0008 is the real tool). Exists so the doctrine's claim that
views are derived (doctrine/matters.md §12) is executable rather than
aspirational. Uses a real YAML parser deliberately: the archived first
attempt shipped invalid frontmatter that a line-splitting parser
masked. Also enforces the state -> status derivation (doctrine §12).

Requires PyYAML. Run from the repo root.
"""
import glob
import io
import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("gen-index: PyYAML is required (pip install pyyaml)")

STATE_ORDER = ["proposed", "ratified", "staged", "executed",
               "rejected", "withdrawn", "superseded"]

STATUS_FOR_STATE = {
    "proposed": "draft",
    "ratified": "stable", "staged": "stable", "executed": "stable",
    "rejected": "deprecated", "withdrawn": "deprecated",
    "superseded": "deprecated",
}


def frontmatter(path):
    text = io.open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        sys.exit(f"{path}: no frontmatter block")
    try:
        fields = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        sys.exit(f"{path}: frontmatter is not valid YAML: {e}")
    if not isinstance(fields, dict) or not fields.get("type"):
        sys.exit(f"{path}: empty or missing 'type' (OKF requires it)")
    for key in ("id", "title", "description", "state"):
        if not fields.get(key):
            sys.exit(f"{path}: missing '{key}'")
    state = fields["state"]
    if state not in STATE_ORDER:
        sys.exit(f"{path}: unknown state '{state}'")
    want = STATUS_FOR_STATE[state]
    if fields.get("status") != want:
        sys.exit(f"{path}: status must be '{want}' for state '{state}' "
                 f"(doctrine §12: status is derived, never hand-set)")
    if not os.path.basename(path).startswith(fields["id"] + "-"):
        sys.exit(f"{path}: filename does not start with id '{fields['id']}'")
    fields["file"] = os.path.basename(path)
    return fields


def fmt_list(v):
    if v is None:
        return "—"
    if isinstance(v, list):
        return ", ".join(str(x) for x in v) if v else "—"
    return str(v)


def main():
    rows = [frontmatter(p) for p in sorted(glob.glob("matters/m*.md"))]

    out = ["---", 'okf_version: "0.2"', "---", "",
           "# Matters", "",
           "Derived from the frontmatter of every matter in this directory.",
           "**Do not hand-edit** — run `tools/gen-index.py`. "
           "See [m0008](https://github.com/markreveley/formic-matters/"
           "blob/70db408d9148667097b2cd052853d37d01e9f3fa/matters/"
           "m0008-matter-tooling.md), the framework's tooling matter.",
           ""]

    for state in STATE_ORDER:
        group = [r for r in rows if r["state"] == state]
        if not group:
            continue
        out += [f"## {state}", "",
                "| | Type | Tags | Matter | Description |",
                "|---|---|---|---|---|"]
        for r in group:
            out.append(f"| `{r['id']}` | {r['type']} | "
                       f"{fmt_list(r.get('tags'))} | "
                       f"[{r['title']}]({r['file']}) | {r['description']} |")
        out.append("")

    linked = [r for r in rows if r.get("depends_on") or r.get("implements")]
    if linked:
        out += ["## Ordering", "",
                "`implements` names the spec a matter serves; `depends_on` "
                "constrains execution order.", "",
                "| Matter | Implements | Depends on |", "|---|---|---|"]
        for r in linked:
            out.append(f"| `{r['id']}` | {fmt_list(r.get('implements'))} | "
                       f"{fmt_list(r.get('depends_on'))} |")
        out.append("")

    io.open("matters/index.md", "w", encoding="utf-8").write("\n".join(out))
    print(f"{len(rows)} matters indexed")


if __name__ == "__main__":
    main()
