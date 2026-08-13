"""Patch: resolve the handoff's anchors and record the plan update.

Run command:

    python patch_handoff_anchor_close.py

Save this file into the REPO ROOT (the folder holding
LEDGER_CONSOLIDATED.md), open it in VS Code, and click Run. It edits
documentation/HANDOFF_20260812b_L192_attachment.md only.

Why: the handoff was written before the final push, so it carries an
unresolved anchor ("plus whatever SHA carries this amendment") and a
closing line naming `c5218f6` / `d5437f0`. Both HEADs have moved since.
A next session doing the SHA round trip against those numbers would
find a mismatch and have to reconcile by hand -- which is the exact
failure the anchor exists to prevent.

Also adds the master plan v18 and summary update, which happened after
Part 2's text was fixed and is recorded nowhere in the handoff.

No generator to run afterwards. Commit and push. The new SHA will not
match the one written here either; that is expected and harmless,
because these anchors name the state the handoff DESCRIBES, and this
amendment describes no code.

Success prints one `ok` line per edit, then `patch applied (N bytes)`.
Failure prints a single ERROR or ANCHOR FAIL line and writes nothing.
"""

import hashlib
import os
import sys

TARGET = os.path.join('documentation',
                      'HANDOFF_20260812b_L192_attachment.md')


EDITS = [
    # ---- 1. resolve the Part 2 anchor ---------------------------------
    (b"""Everything above was written at `c5218f6`. The session continued.
Anchor for this part: `00219d9`, plus whatever SHA carries this
amendment.""",
     b"""Everything above was written at `c5218f6`. The session continued.

**Anchor for this part: `6b99acec3d980c9de7e1770ef752d82a54c01db8`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery at `c2202dcc2c4ed210160ce6033b70346aef194b68` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both verified live at session close.** The work described below was
built on `00219d9` and pushed at `6b99ace`."""),

    # ---- 2. record the master plan update -----------------------------
    (b"""## Next session

L-192's build, with fork 2 as the first question rather than the
fifth.""",
     b"""## Master plan v17 -> v18, summary current at 8/13

`documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md` gains a "New in v18"
lineage entry covering L-186, L-188, L-189, protocol v3.39, the
attachment rule, and the checker's design review. No phase structure
changed and no Track 0 or Track 2 work moved.

`MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md` was two days and four
protocol versions stale. Three corrections beyond the new section:

- The status table showed L-186 as "mechanical half done, six
  duplicate_identity sites remain." Those six were never data problems.
- L-188 and L-189 were listed as open, with L-189 marked "NEXT
  SESSION'S BUILD." Both are done.
- It read "Protocol at v3.35," described the v3.36 Register Rule
  amendment as NOT YET APPLIED, and said "The Artifact Bounds the
  Audit" had no drafted text anywhere in the repo. Both landed in
  v3.37. **A snapshot asserting that an applied rule does not exist yet
  is worse than one that is merely old** -- somebody reads it and
  writes the rule a second time.

That third one is the argument for updating the readable snapshot in
the same session as the work, not a week later.

## Next session

L-192's build, with fork 2 as the first question rather than the
fifth."""),

    # ---- 3. closing anchor --------------------------------------------
    (b"""*Handoff prepared August 2026 with Anthropic's Claude Opus 5, built on
`c5218f6202965bc051044e59988e1a040a234fc9` at
https://github.com/tonylquintanilla/palomas_orrery and
`d5437f08f94feccd70b697729b52cdc44df8b51d` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io*""",
     b"""*Handoff prepared August 2026 with Anthropic's Claude Opus 5.
Part 1 built on `c5218f6202965bc051044e59988e1a040a234fc9`, Part 2 on
`00219d9852c65d653ae49855d3138050dd8f76dd` and pushed at
`6b99acec3d980c9de7e1770ef752d82a54c01db8`, at
https://github.com/tonylquintanilla/palomas_orrery. Gallery at
`c2202dcc2c4ed210160ce6033b70346aef194b68` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io --
untouched by this session; it moved on its own nightly fetch.*"""),
]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, TARGET)

    if not os.path.exists(path):
        print(f"ERROR: {TARGET} not found under {here}")
        return 1

    with open(path, 'rb') as f:
        data = f.read()

    fp = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
    print(f"base fingerprint: {fp}  ({len(data)} bytes)")

    is_crlf = data.count(b'\r\n') > 0
    if is_crlf:
        print("note: file uses CRLF; anchors translated")

    staged = data
    for i, (old, new) in enumerate(EDITS, 1):
        o, n = old, new
        if is_crlf:
            o = o.replace(b'\n', b'\r\n')
            n = n.replace(b'\n', b'\r\n')
        count = staged.count(o)
        if count != 1:
            head = o.split(b'\n')[0][:70]
            print(f"ANCHOR FAIL edit {i}: expected 1 match, got {count}: "
                  f"{head!r}")
            print("nothing written")
            return 1
        staged = staged.replace(o, n, 1)
        print(f"ok  edit {i}")

    with open(path, 'wb') as f:
        f.write(staged)

    print(f"patch applied ({len(staged)} bytes)")
    print("")
    print("No generator to run. Commit and push.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
