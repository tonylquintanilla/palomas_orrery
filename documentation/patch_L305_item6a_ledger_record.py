"""
patch_L305_item6a_ledger_record.py

  *** RUN THIS ONE FROM THE ORRERY REPO ***
  C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github

Records L-305 item 6a in the ledger, after the live run said it worked
rather than before.

WHAT CHANGES (1 file: LEDGER_CONSOLIDATED.md)

  1. L-305 gains a Note: item 6 is split, 6a landed at gallery
     0f51ce4f, and the live gallery run verified it -- Served
     reachability byte-identical on all eight files, Store drift 48
     match and 0 DRIFT against orrery 77eb1439, up from 46 and 2.

  2. The same Note records that Gap (2)'s closing sentence is
     SUPERSEDED. Gap (2) was closed on 2026-09-11 expecting item 6 to
     serve the magnetotail figure as "to about 1,000 R_E" and move the
     served row from declared to V_SOURCED. L-323's design revision,
     written and reviewed on 2026-09-12, puts that figure in a STORE
     row at item 7 instead, as a lower bound read "observed to at
     least". Two plans for one number were sitting in the ledger; the
     later one wins and the older one now says so.

  3. The ledger's header gains a currency stamp.

WHY THIS RUNS NOW AND NOT EARLIER

  The patch that did the work shipped before this one deliberately. A
  ledger entry written ahead of the run is a claim about the future;
  the live check has now made it a claim about the past. Same reason a
  handoff is checked against the render.

WHAT IS PERMANENT AND WHAT IS NOT

  This script is disposable and one-shot. The record is permanent.

HOW TO RUN IT (Tony)

  Save this file into the ORRERY repo root -- the folder holding
  LEDGER_CONSOLIDATED.md -- open it in VS Code, and click Run.
  Equivalent command: python patch_L305_item6a_ledger_record.py

  Success: two "ok" lines, one "stamp updated" line, then
           "patch applied".
  Failure: one ERROR or ANCHOR FAIL line. NOTHING is written. Undo is
           Discard Changes in GitHub Desktop.

AFTER IT RUNS

  Run ledger_index.py (Run button). No block was added, so expect
  "OK: 320 L-blocks parsed, no consistency problems."

BASE

  Built on orrery 77eb1439024f080c3717c625939fb63486bc41a6 at
  https://github.com/tonylquintanilla/palomas_orrery
  Gallery at 0f51ce4f0e07469434629e541b6de002372962a4, which is the
  commit the live run verified.

Written September 12, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = "LEDGER_CONSOLIDATED.md"
BASE_FP = "e158c534b4ddea4e03424c1e72b9efb3"

INDEX_START = b"<!-- INDEX:START"
INDEX_END = b"<!-- INDEX:END -->"


def fingerprint(data):
    lf = data.replace(b"\r\n", b"\n")
    a = lf.index(INDEX_START)
    b = lf.index(INDEX_END) + len(INDEX_END)
    return hashlib.md5(lf[:a] + lf[b:]).hexdigest()


NOTE_OLD = (
    b"(8) Live store-drift run reads MATCH by name for every new pointer;\n"
    b"then Mode 5 on both, phone first.\n"
    b"**Ref:** L-291, L-292, L-298 (the orrery-vs-exhibit gap, made concrete),\n"
)

NOTE_NEW = (
    b"(8) Live store-drift run reads MATCH by name for every new pointer;\n"
    b"then Mode 5 on both, phone first.\n"
    b"**Note (2026-09-12) -- item 6 is split, and 6a has landed.** 6a is the\n"
    b"half that was wrong TODAY, independent of anything the L-321\n"
    b"worksheets return, and it is in the gallery at `0f51ce4f`. Two values\n"
    b"that had drifted from the store they point at:\n"
    b"`EARTH_MAGNETOPAUSE_STANDOFF_RADII` served 10.0 against a stored\n"
    b"10.25, and `EARTH_BOW_SHOCK_STANDOFF_RADII` served 12.5 against a\n"
    b"stored 13.51. Both now serve the stored figure exactly, which is what\n"
    b"the drift check compares. Three retired claims went with them: the bow\n"
    b"shock's source said the value was drawn at the midpoint of Lugaz's\n"
    b"11-14 R_E, and now names Jelinek eq. 14 with Lugaz as corroboration;\n"
    b"its note cited Farris & Russell (1994) for the model FORM, which is a\n"
    b"miscitation because that paper is a standoff relation taking obstacle\n"
    b"shape as an INPUT; and the magnetotail's `_declared` asserted an\n"
    b"observed extent for the real tail.\n"
    b"The tail retirement RESTATES NO FIGURE, on purpose. Writing the old\n"
    b"number into the served prose to explain its removal would leave the\n"
    b"same figure in the same place with nothing able to check it, which is\n"
    b"the failure being fixed. The observed extent arrives at item 7, from a\n"
    b"store row.\n"
    b"**Note (2026-09-12) -- verified by the run, not by the patch.** The\n"
    b"live gallery run at `0f51ce4f`: Served reachability passes with all\n"
    b"eight probed files byte-identical to the working copy, and Store drift\n"
    b"reports 48 MATCH, 0 DRIFT, 0 UNIT MISMATCH against orrery `77eb1439`,\n"
    b"up from 46 MATCH and 2 DRIFT before the patch. The 5 pointers it could\n"
    b"not examine are the same five L-322 measured on 2026-09-11 -- four\n"
    b"`planet_poles` entries and a function default, none of them top-level\n"
    b"constants -- and are unchanged by this work. A first live run was\n"
    b"inconclusive rather than wrong: three files came back STALE because\n"
    b"the gallery had not been pushed, and the run declined to call itself a\n"
    b"pass.\n"
    b"**Note (2026-09-12) -- Gap (2)'s closing plan is SUPERSEDED by L-323.**\n"
    b"Gap (2) was closed on 2026-09-11 expecting item 6 to write the\n"
    b"magnetotail figure as \"to about 1,000 R_E\" carrying its qualifier, and\n"
    b"to move the served row from declared to V_SOURCED. L-323's design\n"
    b"revision of 2026-09-12, reviewed twice, puts that figure in a STORE row\n"
    b"at item 7 instead, in a different form: ONE SCALAR read \"observed to at\n"
    b"least\", because Ness reports one crossing at an uncertain distance and\n"
    b"a stated extent would assert two edges the source never gives. Serving\n"
    b"it from prose at item 6 is the shape L-323 exists to remove. Two plans\n"
    b"for one number were sitting in this block; the later one wins, and 6a\n"
    b"has already acted on it.\n"
    b"**Note (2026-09-12) -- what 6b still owes, and what it waits on.**\n"
    b"Serve the shape parameters, the cut angle, the declared conditions and\n"
    b"the validity range, and retire the magnetotail row's `base_radii` and\n"
    b"`end_radii`. All of it describes the Shue and Jelinek models on the\n"
    b"SERVED side, and `gallery/feature_renderers.js` has no magnetosphere\n"
    b"code at all yet -- that is item 5, the port. Serving parameters nothing\n"
    b"reads would publish a claim no one can see. 6b follows item 5.\n"
    b"The BOUNDARY above held: `van_allen_belts` is byte-identical before and\n"
    b"after 6a, and so are the magnetotail's drawing parameters. Checked by\n"
    b"comparing the parsed structures, not by reading the diff.\n"
    b"**Ref:** L-291, L-292, L-298 (the orrery-vs-exhibit gap, made concrete),\n"
)

STAMP_OLD = (
    b"pressure reopens that decision), built on d2430676.\n"
    b"Review and RICE update Tony 6-21-2026"
)

STAMP_NEW = (
    b"pressure reopens that decision), built on d2430676.\n"
    b"Module updated: September 12, 2026 with Anthropic's Claude Opus 5\n"
    b"(L-305 item 6a recorded after the live gallery run verified it at\n"
    b"0f51ce4f: two drifted values corrected, three claims retired, and\n"
    b"Gap (2)'s closing plan marked superseded by L-323), built on\n"
    b"77eb1439.\n"
    b"Review and RICE update Tony 6-21-2026"
)

EDITS = [
    ("ledger: L-305 item 6a recorded and 6b scoped", NOTE_OLD, NOTE_NEW),
    ("ledger: currency stamp", STAMP_OLD, STAMP_NEW),
]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    full = os.path.join(here, TARGET)

    if not os.path.exists(full):
        print("ERROR: %s not found." % TARGET)
        print("This patch belongs in the ORRERY repo root, not the gallery.")
        print("NOTHING was written.")
        return 1

    with open(full, "rb") as handle:
        data = handle.read()

    try:
        fp = fingerprint(data)
    except ValueError:
        print("ERROR: INDEX zone markers not found in %s. NOTHING written."
              % TARGET)
        return 1

    if fp != BASE_FP:
        print("ERROR: base moved. %s does not match the tree this patch was "
              "built against." % TARGET)
        print("  expected %s" % BASE_FP)
        print("  found    %s" % fp)
        print("NOTHING was written.")
        return 1

    is_crlf = data.count(b"\r\n") > 0
    new = data
    applied = []
    stamped = False

    for label, old, repl in EDITS:
        o, r = old, repl
        if is_crlf:
            o = o.replace(b"\n", b"\r\n")
            r = r.replace(b"\n", b"\r\n")
        n = new.count(o)
        if n != 1:
            print("ANCHOR FAIL: %s -- expected 1 match, found %d."
                  % (label, n))
            print("NOTHING was written. Undo is Discard Changes in GitHub "
                  "Desktop.")
            return 1
        new = new.replace(o, r)
        if label.endswith("currency stamp"):
            stamped = True
        else:
            applied.append(label)

    non_ascii = sum(1 for ch in new if ch > 127)
    if non_ascii:
        print("ERROR: patch would introduce %d non-ASCII byte(s). NOTHING "
              "written." % non_ascii)
        return 1

    with open(full, "wb") as handle:
        handle.write(new)

    for label in applied:
        print("ok  %s" % label)
    if stamped:
        print("stamp updated  %s" % TARGET)
    print("patch applied (%d bytes)" % len(new))
    print("")
    print("NEXT: run ledger_index.py -- no block was added, so expect")
    print("  'OK: 320 L-blocks parsed, no consistency problems.'")
    return 0


if __name__ == "__main__":
    sys.exit(main())
