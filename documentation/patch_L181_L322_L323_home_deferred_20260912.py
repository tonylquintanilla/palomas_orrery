"""
patch_L181_L322_L323_home_deferred_20260912.py

Homes the five deferred items from the 2026-09-12 build review into open
ledger items, and corrects L-323's Gap against what is actually in the
repo at 56f96004.

WHAT IT DOES (six edits, one file: LEDGER_CONSOLIDATED.md)
  1. L-322 metadata: upd 2026-09-11 -> 2026-09-12.
  2. L-322 body: a Note homing the FOUR deferred test_status_lines.py
     rules as one class -- three checker additions plus the dict blind
     spot. L-322 owns that checker, so its files are the files this work
     opens.
  3. L-322 Ref: test_status_lines.py added to the file list.
  4. L-181 metadata: upd 2026-08-25 -> 2026-09-12.
  5. L-181 body: a Note homing the retired "Verified: April 2026" stamp
     as a CLASS -- 42 surviving stamps across four live modules, named
     by file with counts. L-181 already owns the source-of-truth sweep
     across those files.
  6. L-323 Gap: replaced. The design record EXISTS; a revision is owed.
     The prompts are at rev 2, which fixed one of the three defects; two
     survive. A Note is added recording the landing commit, whose message
     names a handle that does not exist.

WHAT IS PERMANENT AND WHAT IS NOT
  This script is disposable and one-shot. What it installs is permanent:
  five items that previously lived only in a handoff now have ledger
  homes, and L-323's Gap now describes the repo rather than a state that
  ended at 56f96004.

HOW TO RUN IT (Tony)
  Save this file into the orrery repo root -- the same folder as
  LEDGER_CONSOLIDATED.md -- open it in VS Code, and click Run.
  Equivalent command: python patch_L181_L322_L323_home_deferred_20260912.py

  Success: six "ok" lines, a "stamp updated" line, then
           "patch applied (N bytes)".
  Failure: one ERROR or ANCHOR FAIL line. NOTHING is written either way.
           Undo is Discard Changes in GitHub Desktop.

AFTER IT RUNS
  Run ledger_index.py (Run button). The two upd dates changed, so the
  generated index needs regenerating. Expect:
  "OK: 319 L-blocks parsed, no consistency problems."

BASE
  Built on orrery 56f96004c4a0421d529411a8bbbd2d9cf70b0fd9 at
  https://github.com/tonylquintanilla/palomas_orrery
  The guard fingerprints the content OUTSIDE the INDEX zone, because
  ledger_index.py rewrites that zone and a guard must not fence what a
  generator rewrites.

Written September 12, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = "LEDGER_CONSOLIDATED.md"
BASE_FP = "9522a285067c612474b66de1fd4fd01d"

INDEX_START = b"<!-- INDEX:START"
INDEX_END = b"<!-- INDEX:END -->"


def fingerprint(data):
    """md5 of LF-normalized content outside the generated INDEX zone."""
    lf = data.replace(b"\r\n", b"\n")
    a = lf.index(INDEX_START)
    b = lf.index(INDEX_END) + len(INDEX_END)
    return hashlib.md5(lf[:a] + lf[b:]).hexdigest()


# ---------------------------------------------------------------- edits

STAMP_OLD = (
    b"Studio's prior art; L-168's title), built on 1ee1cc61.\n"
    b"Review and RICE update Tony 6-21-2026"
)

STAMP_NEW = (
    b"Studio's prior art; L-168's title), built on 1ee1cc61.\n"
    b"Module updated: September 12, 2026 with Anthropic's Claude Opus 5\n"
    b"(five items deferred by the 2026-09-12 build review are homed:\n"
    b"four test_status_lines.py rules to L-322, the retired\n"
    b"\"Verified: April 2026\" stamp class to L-181; L-323's Gap corrected\n"
    b"against the repo), built on 56f96004.\n"
    b"Review and RICE update Tony 6-21-2026"
)

L322_META_OLD = (
    b"<!-- L:322 status:OPEN upd:2026-09-11 section:A flag: rice:4/5/70/6 -->"
)
L322_META_NEW = (
    b"<!-- L:322 status:OPEN upd:2026-09-12 section:A flag: rice:4/5/70/6 -->"
)

L322_NOTE_OLD = (
    b"`documentation/` as spent patches, not held ones.\n"
    b"**Ref:** L-305, L-306 (approximations are not promoted), L-314,"
)

L322_NOTE_NEW = (
    b"`documentation/` as spent patches, not held ones.\n"
    b"**Note (2026-09-12) -- four deferred rules for `test_status_lines.py`,\n"
    b"as one class.** Deferred by the build review of 2026-09-12 and homed\n"
    b"here, because this item owns the checker and its files are the files\n"
    b"the work opens. Three additions, all of them reporting BY NAME rather\n"
    b"than by count: the derived rows whose input is `declared pending`;\n"
    b"the derived rows whose right-hand side is a bare literal; and a check\n"
    b"that a pending row's handle exists in the ledger. One blind spot: a\n"
    b"status line attached to a dict rather than to an assignment is\n"
    b"invisible to the parser. None exist today, so this guards a shape the\n"
    b"store may grow rather than a defect it has -- and a parser that cannot\n"
    b"see a shape reports nothing when the shape arrives, which is A Check\n"
    b"That Cannot Fail. These four were carried only in a handoff until\n"
    b"now. [verified @56f96004]\n"
    b"**Ref:** L-305, L-306 (approximations are not promoted), L-314,"
)

L322_REF_OLD = (
    b"`constants_new.py`, `provenance_scanner.py`, `orrery_maintenance_run.py`,\n"
    b"`celestial_objects.py`,"
)
L322_REF_NEW = (
    b"`constants_new.py`, `provenance_scanner.py`, `orrery_maintenance_run.py`,\n"
    b"`test_status_lines.py`, `celestial_objects.py`,"
)

L181_META_OLD = (
    b"<!-- L:181 status:OPEN upd:2026-08-25 section:A flag: rice:5/5/70/5 -->"
)
L181_META_NEW = (
    b"<!-- L:181 status:OPEN upd:2026-09-12 section:A flag: rice:5/5/70/5 -->"
)

L181_NOTE_OLD = (
    b"reachability count.\n"
    b"**Ref:** FABLE_shell_consistency_audit_report.md section 2 (Job 2),"
)

L181_NOTE_NEW = (
    b"reachability count.\n"
    b"**Note (2026-09-12) -- the retired `# Verified: April 2026` stamp, as\n"
    b"a CLASS.** The annotation format was retired on 2026-08-02 and 42\n"
    b"stamps survive in live modules: `shell_configs.py` 14,\n"
    b"`earth_visualization_shells.py` 13, `jupiter_visualization_shells.py`\n"
    b"9, `comet_visualization_shells.py` 6. Two more sit in\n"
    b"`test_citation_inheritance.py` as fixtures and are out of scope. They\n"
    b"land here because this item already owns the single-source-of-truth\n"
    b"sweep across those same files: one class row, not 42 instance rows.\n"
    b"Deferred by the build review of 2026-09-12, which named ONE instance,\n"
    b"at line 725 of `earth_visualization_shells.py`; that line is blank,\n"
    b"and the stamp at 725 belongs to `comet_visualization_shells.py`. A\n"
    b"count of 42 is a size -- the four filenames are what makes it\n"
    b"actionable. [verified @56f96004]\n"
    b"**Ref:** FABLE_shell_consistency_audit_report.md section 2 (Job 2),"
)

L323_GAP_OLD = (
    b"**Gap:** the design record and the revision 3 worksheet prompts are\n"
    b"OWED and were not written on 2026-09-12. The 2026-09-11 prompts must\n"
    b"NOT be sent as they stand: prompt 3 tells the checkers the inner belt\n"
    b"figures are consistent (converted, 1.1 R_E is 638 km against the\n"
    b"tooltip's 1,000, so they are not), row 5 hands the inner span a Baker\n"
    b"citation the string never makes (the string cites Baker for the PEAK;\n"
    b"row 11 gets the outer belt right), and the belt rows still ask which\n"
    b"span is correct rather than whether an edge exists at all.\n"
)

L323_GAP_NEW = (
    b"**Note (2026-09-12) -- the landing commit is not findable by handle.**\n"
    b"This block and L-324 landed at `56f96004`, whose commit message reads\n"
    b"\"L305 L325 L324\". There is no L-325 anywhere in the repo, so a later\n"
    b"search for this item's landing commit by its own handle finds\n"
    b"nothing. Recorded rather than fixed: the message is already pushed.\n"
    b"[verified @56f96004]\n"
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

EDITS = [
    ("L-322 upd date", L322_META_OLD, L322_META_NEW),
    ("L-322 Note: four test_status_lines.py rules", L322_NOTE_OLD, L322_NOTE_NEW),
    ("L-322 Ref: test_status_lines.py", L322_REF_OLD, L322_REF_NEW),
    ("L-181 upd date", L181_META_OLD, L181_META_NEW),
    ("L-181 Note: 42 retired stamps, by file", L181_NOTE_OLD, L181_NOTE_NEW),
    ("L-323 Gap corrected + landing-commit Note", L323_GAP_OLD, L323_GAP_NEW),
]

STAMP_EDIT = ("header stamp", STAMP_OLD, STAMP_NEW)


def main():
    if not os.path.exists(TARGET):
        print("ERROR: %s not found. Save this script into the orrery repo "
              "root, next to %s, and Run again." % (TARGET, TARGET))
        return 1

    with open(TARGET, "rb") as f:
        data = f.read()

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
        print("NOTHING was written. Undo is not needed; nothing changed.")
        return 1

    is_crlf = data.count(b"\r\n") > 0
    new = data
    applied = []

    for label, old, repl in EDITS + [STAMP_EDIT]:
        o, r = old, repl
        if is_crlf:
            o = o.replace(b"\n", b"\r\n")
            r = r.replace(b"\n", b"\r\n")
        n = new.count(o)
        if n != 1:
            print("ANCHOR FAIL: %s -- expected 1 match, found %d." % (label, n))
            print("NOTHING was written. Undo is Discard Changes in GitHub "
                  "Desktop.")
            return 1
        new = new.replace(o, r)
        applied.append(label)

    # ASCII gate: this file is ASCII at base and must stay that way.
    non_ascii = sum(1 for ch in new if ch > 127)
    if non_ascii:
        print("ERROR: patch would introduce %d non-ASCII byte(s). NOTHING "
              "written." % non_ascii)
        return 1

    with open(TARGET, "wb") as f:
        f.write(new)

    for label in applied[:-1]:
        print("ok  %s" % label)
    print("stamp updated  %s -- Module updated line for 2026-09-12"
          % TARGET)
    print("patch applied (%d bytes)" % len(new))
    print("")
    print("NEXT: run ledger_index.py (Run button). Two upd dates changed, so")
    print("the generated INDEX zone needs regenerating. Expect:")
    print('  "OK: 319 L-blocks parsed, no consistency problems."')
    return 0


if __name__ == "__main__":
    sys.exit(main())
