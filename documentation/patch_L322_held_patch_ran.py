"""patch_L322_held_patch_ran.py -- correct L-322's record: the held
patch ran.

Built on orrery 27ab0f92a8d350bb4661eedbfb3258ca7d2da3b4
at https://github.com/tonylquintanilla/palomas_orrery

RUN:  save into the palomas_orrery repo ROOT, open in VS Code, Run.
Equivalent command line: python patch_L322_held_patch_ran.py
Then run ledger_index.py (Run). Expect
"OK: 317 L-blocks parsed, no consistency problems."

WHY. L-322 says of `patch_L305_store_drift_units.py`: "It is NOT to be
run," and its Tony-action says to file it UNRUN. Both are now false --
it was run against the gallery on 2026-09-12 and pushed at
`e498a763`, and the live run confirmed no regression. A ledger that
describes a state which is not real is the drift this project exists to
catch, so the correction is recorded visibly rather than swapped in.

TWO edits, both to the [L-322] block: the held-patch bullet, and the
Tony-action.

GUARD: fingerprints the ledger OUTSIDE its ledger_index.py INDEX zone,
line endings normalised. All or nothing.
"""

import hashlib
import os
import sys

TARGET = "LEDGER_CONSOLIDATED.md"
EXPECT_FP = "fdad39d3233ff1435d8be951b4be4cf5"
INDEX_START = b"<!-- INDEX:START"
INDEX_END = b"<!-- INDEX:END -->"

EDITS = [
    (b"""**The held patch.** `patch_L305_store_drift_units.py` extends the
  gallery's suffix table and makes L-305's fifteen pointers green. It
  was written, tested (15 of 15 MATCH, no regression on the existing 53)
  and HELD UNRUN, because it puts a naming vocabulary for orrery
  constants inside the gallery repo. It is NOT to be run. [Tony's
  ruling, 2026-09-11]""",
     b"""**The held patch, and it RAN.**
  `patch_L305_store_drift_units.py` extends the gallery's suffix table
  and makes L-305's fifteen pointers green. It was written, tested
  (15 of 15 MATCH, no regression on the existing 53) and HELD UNRUN on
  2026-09-11, because it puts a naming vocabulary for orrery constants
  inside the gallery repo. **On 2026-09-12 it was run by mistake and
  pushed at gallery `e498a763`.** The live maintenance run confirmed no
  regression: 53 pointers, 48 match, 0 DRIFT, 0 UNIT MISMATCH, 5 could
  not be examined -- the same result in the new wording. **Tony's
  ruling on being told (2026-09-12): it STAYS, not reverted.** Retiring
  the suffix reader now would contradict ruling 3 -- the store has no
  `# Unit:` lines yet, and dropping the reader before they exist puts
  46 of 48 checks dark while the run stays green. The code splits in
  two: the scalar-unit comparison rule and the UNIT MISMATCH verdict
  SURVIVE this item, being about how two values compare rather than
  about reading a name; the six suffix entries for non-length units
  RETIRE with the reader. `patch_L322_mark_transitional.py` (gallery,
  comments only, no behaviour change) records that split in the file
  and names the trap: `_DIMENSIONLESS` as a SUFFIX invites renaming a
  constant to turn it green, and no constant is to be named to satisfy
  that table. L-305's fifteen get `# Unit:` lines; the twelve that
  report NO UNIT until the export lands stay one class row here.""",),

    (b"""**Tony-action (do):** commit
`documentation/DESIGN_unit_field_and_export_20260911.md` and
`documentation/DESIGN_unit_field_and_export_rev2_20260911.md`, and the
held `patch_L305_store_drift_units.py` into the GALLERY repo's
`documentation/` UNRUN.""",
     b"""**Tony-action (do):** commit
`documentation/DESIGN_unit_field_and_export_20260911.md` and
`documentation/DESIGN_unit_field_and_export_rev2_20260911.md`. The
spent `patch_L305_store_drift_units.py` and
`patch_L322_mark_transitional.py` move into the GALLERY repo's
`documentation/` as spent patches, not held ones.""",),
]


def fail(msg):
    print("FAILURE: " + msg)
    print("NOTHING was written.")
    print("Undo is Discard Changes in GitHub Desktop.")
    sys.exit(1)


def main():
    if not os.path.exists(TARGET):
        fail("%s not found. Run this from the palomas_orrery repo root."
             % TARGET)
    raw = open(TARGET, "rb").read()
    was_crlf = b"\r\n" in raw
    content = raw.replace(b"\r\n", b"\n") if was_crlf else raw

    a = content.index(INDEX_START)
    b = content.index(INDEX_END) + len(INDEX_END)
    fp = hashlib.md5(content[:a] + content[b:]).hexdigest()
    if fp != EXPECT_FP:
        fail("BASE MOVED. Body fingerprint %s, expected %s.\n"
             "         (an ledger_index.py run alone would NOT do this)."
             % (fp, EXPECT_FP))
    print("ok   base fingerprint matches%s"
          % (" (CRLF)" if was_crlf else ""))

    out = content
    for i, (old, new) in enumerate(EDITS, 1):
        n = out.count(old)
        if n != 1:
            fail("ANCHOR FAIL on edit %d: expected 1 match, got %d.\n"
                 "         %r" % (i, n, old[:70]))
        out = out.replace(old, new)
        print("ok   edit %d applied" % i)

    bad = [c for c in out if c > 127]
    if bad:
        fail("encoding gate: %d non-ASCII bytes." % len(bad))
    print("ok   encoding gate: ASCII clean")

    final = out.replace(b"\n", b"\r\n") if was_crlf else out
    with open(TARGET, "wb") as f:
        f.write(final)
    print("patch applied (%d bytes, was %d)" % (len(final), len(raw)))
    print("")
    print("NEXT: run ledger_index.py (Run button), then commit and push.")


if __name__ == "__main__":
    main()
