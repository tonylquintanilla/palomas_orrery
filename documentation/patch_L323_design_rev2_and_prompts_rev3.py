"""
patch_L323_design_rev2_and_prompts_rev3.py

Records in L-323 that its two owed documents are written, and moves its
Gap to what is actually left.

WHAT IT DOES (one file: LEDGER_CONSOLIDATED.md)
  1. L-323's Gap is replaced. It currently says the design record needs
     a revision and the prompts need a revision 3; both now exist. The
     new Gap is the one thing left: sending revision 3 to the checkers,
     which is L-321's round, and the belt VALUES that come back from it.
  2. Two Notes are added. One records what the revision settled and what
     it corrected. One records a measurement made while writing it: the
     altitude figures are not where the original design record said they
     were, and were not there at its own SHA either.
  3. L-305 item 6 gains a boundary: it must not touch the belt `note`
     fields in data/objects_config.json that repeat the span prose.
     Those change at item 7 with the edge rows, and editing them twice
     is the same double-store failure L-323 is about.
  4. The ledger's header gains a currency stamp.

RUN THIS AFTER SAVING THE TWO DOCUMENTS
  Save both into documentation/ first, so the paths this patch writes
  into the ledger are true when it writes them:
    DESIGN_a_figure_in_prose_needs_a_home_rev2_20260912.md
    L321_slice1_prompts_rev3_20260912.md

WHAT IS PERMANENT AND WHAT IS NOT
  This script is disposable and one-shot. The two documents and the
  ledger record are permanent.

HOW TO RUN IT (Tony)
  Save this file into the orrery repo root -- the same folder as
  LEDGER_CONSOLIDATED.md -- open it in VS Code, and click Run.
  Equivalent command: python patch_L323_design_rev2_and_prompts_rev3.py

  Success: four "ok" lines, one "stamp updated" line, then
           "patch applied".
  Failure: one ERROR or ANCHOR FAIL line. NOTHING is written. Undo is
           Discard Changes in GitHub Desktop.

  The patch also checks that both documents are in documentation/ before
  it writes, and stops if either is missing. A ledger that names a file
  which is not there is the kind of claim this project does not make.

AFTER IT RUNS
  Run ledger_index.py (Run button). Expect
  "OK: 319 L-blocks parsed, no consistency problems."

BASE
  Built on orrery 62ee5149e611e325455e56bb3b09486daeea0040 at
  https://github.com/tonylquintanilla/palomas_orrery
  The guard fingerprints content OUTSIDE the INDEX zone, which
  ledger_index.py regenerates.

Written September 12, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = "LEDGER_CONSOLIDATED.md"
BASE_FP = "214db996f85cb3bf0f0e6c67f6b92c48"

INDEX_START = b"<!-- INDEX:START"
INDEX_END = b"<!-- INDEX:END -->"

REQUIRED_DOCS = [
    os.path.join("documentation",
                 "DESIGN_a_figure_in_prose_needs_a_home_rev2_20260912.md"),
    os.path.join("documentation",
                 "L321_slice1_prompts_rev3_20260912.md"),
]


def fingerprint(data):
    lf = data.replace(b"\r\n", b"\n")
    a = lf.index(INDEX_START)
    b = lf.index(INDEX_END) + len(INDEX_END)
    return hashlib.md5(lf[:a] + lf[b:]).hexdigest()


GAP_OLD = (
    b"**Gap:** corrected 2026-09-12 against the repo; the prior wording\n"
    b"described a state that ended at `56f96004`.\n"
    b"The DESIGN RECORD EXISTS --\n"
    b"`documentation/DESIGN_a_figure_in_prose_needs_a_home_20260912.md`,\n"
    b"built on `a4ead59a`. What is owed is a REVISION, not a first draft:\n"
    b"the record POSES the tuple-versus-two-scalars question (its question\n"
    b"1) rather than answering it, and the third review round's rulings --\n"
    b"two scalars, one frame, and the split that leaves the drawn 100 where\n"
    b"it is drawn -- live only in this block's Notes above. A session\n"
    b"writing a second record from scratch would not read them.\n"
    b"The WORKSHEET PROMPTS are at revision 2 --\n"
    b"`documentation/L321_slice1_prompts_rev2_20260912.md`, superseding the\n"
    b"2026-09-11 prompts. Rev 2 fixed the first of the three defects: the\n"
    b"inner-belt conversion is no longer stated as consistent, and both\n"
    b"belts now carry the conversion on the prompt. TWO survive into rev 3.\n"
    b"Row 5 still cites Baker et al. (2018) as supporting rows 2 AND 3,\n"
    b"where the string cites Baker for the PEAK only; row 11 gets the outer\n"
    b"belt right and is the model. And rows 3 and 8 still ask whether a\n"
    b"stated span is correct rather than whether an edge exists at all,\n"
    b"which is the question this item is actually about. Rev 3 is a small\n"
    b"edit on rev 2, not a rewrite.\n"
    b"Rev 2's stated dependency is satisfied. At `56f96004` the bow shock's\n"
    b"Lugaz-midpoint sentence survives only inside archived patch scripts\n"
    b"in `documentation/`, and both the hover and its `shell_configs.py`\n"
    b"twin attribute the standoff to Jelinek. [verified @56f96004]\n"
)

GAP_NEW = (
    b"**Note (2026-09-12) -- both owed documents are written.**\n"
    b"`documentation/DESIGN_a_figure_in_prose_needs_a_home_rev2_20260912.md`\n"
    b"supersedes the 2026-09-12 record, which stays as the review request\n"
    b"that produced it. The revision states the design as settled rather\n"
    b"than as five questions: the diagnosis corrected to a Note becoming a\n"
    b"store; three frames named, with L as the store's; ruling B amended so\n"
    b"the STORE holds one frame and the STRING derives its presentations;\n"
    b"and the five questions answered -- two scalars named `_INNER_EDGE`\n"
    b"and `_OUTER_EDGE` in L, interpolation as the rule with the scanner's\n"
    b"citation window as the real blind spot, the magnetotail split into a\n"
    b"drawn shape and an observed LOWER BOUND, discovery routed through the\n"
    b"scanner's existing list, and \"3 to 7\" over \"3.0 to 7.0\".\n"
    b"A second review round read the revision before it landed, and three\n"
    b"of its corrections are in it. The peak rows are disposed of rather\n"
    b"than only noted, and they are TWO cases:\n"
    b"`EARTH_VAN_ALLEN_OUTER_RADII` is the midpoint of an L band by its own\n"
    b"Source line, so calling it R_E is a conversion nobody performed and\n"
    b"its unit moves to L with the edge rows; `EARTH_VAN_ALLEN_INNER_RADII`\n"
    b"carries Baker at geocentric r ~ 1.5 R_E AND the CIRBE paper at\n"
    b"L = 1.5 for the same number, so its frame is a worksheet question and\n"
    b"not a relabel. The magnetotail row is given a FORM -- one scalar read\n"
    b"as \"observed to at least\" -- because Ness reports ONE crossing at an\n"
    b"uncertain distance, and a near/far pair would assert two edges of an\n"
    b"extent the source never states. And the unit token is named\n"
    b"`l_shell` rather than `l`, so item 7 does not invent one under time\n"
    b"pressure; the vocabulary itself stays L-322 ruling 1's.\n"
    b"`documentation/L321_slice1_prompts_rev3_20260912.md` supersedes rev 2\n"
    b"and is ready to send: the sequencing dependency is discharged, row 5\n"
    b"cites Baker for the peak only, row 11 names both sources the string\n"
    b"names, the four extent rows ask whether an EDGE EXISTS rather than\n"
    b"which span is right and are marked DISCOVERY, and the frame note\n"
    b"names L. [verified @62ee5149]\n"
    b"**Note (2026-09-12) -- the altitude figures were never where the\n"
    b"record said.** Revision 1 placed the belts' kilometre extents in the\n"
    b"GUI tooltip \"and its twin in `shell_configs.py`\". They are in\n"
    b"neither. All four typed extents are in `earth_visualization_shells.py`\n"
    b"-- 1,000 to 6,000 km and 13,000 to 60,000 km in\n"
    b"`earth_magnetosphere_info` at lines 745 and 747, and the two Earth-\n"
    b"radii spans in `belt_texts` at 892 and 896. The `shell_configs.py`\n"
    b"tooltip carries the two flux peaks, both interpolated, and no span in\n"
    b"any frame. Re-measured at `a4ead59a`, the record's own SHA, so no\n"
    b"later patch moved them: the record was wrong when written. The\n"
    b"tooltip is a PARTIAL twin, and on the figures at issue here it was\n"
    b"already doing the right thing. Rev 3's prompt 3 pastes it for\n"
    b"completeness and rows nothing from it. [verified @62ee5149]\n"
    b"**Gap:** send revision 3 to the checkers -- that round is L-321's,\n"
    b"competitive pattern, each prompt to two checkers independently. The\n"
    b"belt edge VALUES come back from it and land with L-305 item 7, which\n"
    b"is where ruling C puts them. Nothing else in this item is owed.\n"
)

STAMP_OLD = (
    b"a391262e.\n"
    b"Review and RICE update Tony 6-21-2026"
)

STAMP_NEW = (
    b"a391262e.\n"
    b"Module updated: September 12, 2026 with Anthropic's Claude Opus 5\n"
    b"(L-323: the design record's revision 2 and the L-321 worksheet\n"
    b"prompts' revision 3 are written; the Gap moves to sending them),\n"
    b"built on 62ee5149.\n"
    b"Review and RICE update Tony 6-21-2026"
)

L305_BOUNDARY_OLD = (
    b"and `end_radii`. (7) Hover text in `earth_visualization_shells.py`\n"
)

L305_BOUNDARY_NEW = (
    b"and `end_radii`. BOUNDARY (2026-09-12, adopted from the review of\n"
    b"L-323's design revision): item 6 does NOT touch the belt `note`\n"
    b"fields in that same file that repeat the span prose. Those change at\n"
    b"item 7 with the edge rows. Editing them at item 6 and again at item 7\n"
    b"is the double-store failure L-323 names, performed on the fix.\n"
    b"(7) Hover text in `earth_visualization_shells.py`\n"
)

EDITS = [
    ("ledger: L-323 both documents written, Gap moved", GAP_OLD, GAP_NEW),
    ("ledger: L-305 item 6 boundary on the belt note fields",
     L305_BOUNDARY_OLD, L305_BOUNDARY_NEW),
    ("ledger: currency stamp", STAMP_OLD, STAMP_NEW),
]


def main():
    here = os.path.dirname(os.path.abspath(__file__))

    missing = [d for d in REQUIRED_DOCS
               if not os.path.exists(os.path.join(here, d))]
    if missing:
        print("ERROR: this patch writes these paths into the ledger, and "
              "they are not on disk yet:")
        for d in missing:
            print("  %s" % d.replace(os.sep, "/"))
        print("Save both documents into documentation/ first, then Run "
              "again. NOTHING was written.")
        return 1

    full = os.path.join(here, TARGET)
    if not os.path.exists(full):
        print("ERROR: %s not found. Save this script into the orrery repo "
              "root and Run again." % TARGET)
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

    print("ok  both documents confirmed on disk in documentation/")
    for label in applied:
        print("ok  %s" % label)
    if stamped:
        print("stamp updated  %s" % TARGET)
    print("patch applied (%d bytes)" % len(new))
    print("")
    print("NEXT: run ledger_index.py -- expect")
    print("  'OK: 319 L-blocks parsed, no consistency problems.'")
    return 0


if __name__ == "__main__":
    sys.exit(main())
