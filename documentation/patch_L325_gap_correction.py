"""
patch_L325_gap_correction.py

Corrects a claim I put into L-325's Gap this morning that the live
gallery run falsified within the hour.

HOW TO RUN
    Save into the orrery repo ROOT, open in VS Code, click Run.
    Equivalent: python patch_L325_gap_correction.py
    Archive it to documentation/ once it has run.

WHY
    patch_L326_protocol_v3_58.py rewrote L-325's Gap and carried one
    sentence straight out of the 2026-09-12 handoff: that L-305 item 6
    still serves 10.0 and 12.5, so the live Store drift check reports
    2 DRIFT. It does not. The gallery at eab070a9 serves 10.25 and
    13.51, and the live run against orrery 047d676d reports 53
    pointers with 0 DRIFT.

    The sentence was recalled from a handoff, not fetched from the
    served file, and it was already false when written.

WHAT IT CHANGES -- one file, one edit
    LEDGER_CONSOLIDATED.md
      L-325's Gap: both halves recorded closed, with the served
      values and the drift result, plus a Correction paragraph
      naming how the wrong sentence got in.

    L-325's STATUS is untouched and stays OPEN. Whether the item
    closes is Tony's call, not this patch's.

GENERATED ZONE
    The ledger is fingerprinted OUTSIDE its INDEX zone, so running
    ledger_index.py before this patch does not make it refuse.

PERMANENT HALF
    The ledger edit. The script is one-shot.

AFTER IT RUNS
    python ledger_index.py   (expect 321 L-blocks parsed)

UNDO
    Discard Changes in GitHub Desktop.

Built on orrery 047d676dda4396b482191668c68b4d2c3e2e374d at
https://github.com/tonylquintanilla/palomas_orrery
Gallery state checked: eab070a94e53296c05b384eb342085884ef56341 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io

Written September 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

LEDGER = "LEDGER_CONSOLIDATED.md"
FINGERPRINT = "0feece57701b08675238e823325ae8fa"
ZONE = (b"<!-- INDEX:START", b"<!-- INDEX:END -->")

OLD = b"""**Gap (half closed 2026-09-14).** The rule LANDED: A Derived Row Stores
the Figure Its Sources Support [CRITICAL] is in `provenance-discipline`
2.12, under The Store Carries the Verified Figure, carrying the scope
paragraph about L-314 unchanged. See L-326. Still open: L-305 item 6
still serves 10.0 and 12.5, so the gallery's live Store drift check
reports 2 DRIFT until it lands."""

NEW = b"""**Gap (both halves closed 2026-09-14).** The RULE landed: A Derived Row
Stores the Figure Its Sources Support [CRITICAL] is in
`provenance-discipline` 2.12, under The Store Carries the Verified
Figure, carrying the scope paragraph about L-314 unchanged. See L-326.
The SERVING half landed too: the gallery serves 10.25 and 13.51 at
`/features/earth/earth_magnetosphere/magnetopause/standoff/value` and
`.../bow_shock/standoff/value`, and the live Store drift run against
orrery `047d676d` reports 53 pointers, 48 match, 0 DRIFT, 0 UNIT
MISMATCH, 5 not examined. [verified @eab070a9]
**Correction (2026-09-14).** This Gap was rewritten earlier the same day
to say that L-305 item 6 still served 10.0 and 12.5 and that the drift
check reported 2 DRIFT. That sentence was carried out of the 2026-09-12
handoff and never checked against the served file. It was already false
when it was written, and the live gallery run falsified it within the
hour. Fetched vs Recalled, at the ledger layer: a handoff is a claim,
the artifact is the fact."""


def fail(msg):
    print("ERROR: " + msg)
    sys.exit(1)


def main():
    if not os.path.exists(LEDGER):
        fail("%s not found. Run this from the orrery repo ROOT." % LEDGER)

    with open(LEDGER, "rb") as f:
        raw = f.read()
    lf = raw.replace(b"\r\n", b"\n")

    a = lf.find(ZONE[0])
    z = lf.find(ZONE[1])
    if a < 0 or z < 0:
        fail("INDEX zone markers not found in %s." % LEDGER)
    actual = hashlib.md5(lf[:a] + lf[z + len(ZONE[1]):]).hexdigest()
    if actual != FINGERPRINT:
        fail("%s does not match the tree this patch was built against.\n"
             "       expected md5 %s\n"
             "       found    md5 %s\n"
             "       Pull at 047d676d, or the patch has already run."
             % (LEDGER, FINGERPRINT, actual))

    n = lf.count(OLD)
    if n != 1:
        fail("ANCHOR FAIL: found %d matches, expected 1." % n)
    out = lf.replace(OLD, NEW, 1)

    if b"\r" in out:
        fail("result carries CR bytes.")
    bad = sorted(set(c for c in out if c > 127))
    if bad:
        fail("result carries non-ASCII bytes %r" % bad[:8])

    if b"\r\n" in raw:
        out = out.replace(b"\n", b"\r\n")
    with open(LEDGER, "wb") as f:
        f.write(out)

    print("ok  L-325 Gap corrected -- both halves closed, correction recorded")
    print("ok  L-325 status untouched (still OPEN)")
    print("patch applied")
    print("")
    print("Next: python ledger_index.py  (expect 321 L-blocks parsed)")


if __name__ == "__main__":
    main()
