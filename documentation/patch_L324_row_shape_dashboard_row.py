"""
patch_L324_row_shape_dashboard_row.py

Two fixes, both from Tony reading the maintenance dashboard and not
finding the new check.

PART 1 -- the guard gets its own dashboard row.
    The dashboard prints ONE line per checker: the last meaningful line
    of that tool's output. test_status_lines.py ends on its status-line
    verdict, so the row-shape numbers printed above it never reached the
    dashboard. The guard was gating the whole time -- a shape failure
    exits 1 and fails the Status lines row -- but a PASS showed nothing
    at all, which cannot be told apart from a check that never ran.

    test_status_lines.py gains a --shape-only mode that runs the guard
    alone and ends on its own verdict. orrery_maintenance_run.py gains
    a "Row shape" row that calls it. The guard still runs inside the
    full report as well; that redundancy is deliberate and cheap.

PART 2 -- a shape failure is no longer called a malformed status line.
    Introduced by the previous patch, and my error. Shape failures were
    merged into the status-line failure list, so on a failure the
    closing line read "1 of 19 status lines are malformed" -- false on
    both counts. No status line was malformed, and 19 is the denominator
    for status lines, not for the 103 assignments the shape check reads.
    The two kinds are now counted, named and reported separately.

PART 3 -- LEDGER_CONSOLIDATED.md records both, and its Gap moves on.

WHAT IS PERMANENT AND WHAT IS NOT
    This script is disposable and one-shot. The --shape-only mode, the
    dashboard row and the corrected reporting are permanent.

HOW TO RUN IT (Tony)
    Save this file into the orrery repo root -- the same folder as
    test_status_lines.py -- open it in VS Code, and click Run.
    Equivalent command: python patch_L324_row_shape_dashboard_row.py

    Success: one "ok" line per edit, three "stamp updated" lines, then
             "patch applied".
    Failure: one ERROR or ANCHOR FAIL line. NOTHING is written, to ANY
             of the three files. Undo is Discard Changes in GitHub
             Desktop.

AFTER IT RUNS
    1. Run test_status_lines.py (Run button). Its closing lines now
       report both counts separately.
    2. Run orrery_maintenance_run.py (Run button). A new "Row shape"
       row appears in the indented checker list, between "Status lines"
       and "Scanner recognition 1d/1e", reading
       "All 103 row shapes in constants_new.py fit the assignment's own
       line." The gating total goes from 12 to 13.
    3. Run ledger_index.py (Run button) as a parse check. Expect
       "OK: 319 L-blocks parsed, no consistency problems."

BASE
    Built on orrery 6284215b25da248a79fcc16c3d5e5df88dc279e8 at
    https://github.com/tonylquintanilla/palomas_orrery

Written September 12, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

INDEX_START = b"<!-- INDEX:START"
INDEX_END = b"<!-- INDEX:END -->"

CHECKER = "test_status_lines.py"
RUNNER = "orrery_maintenance_run.py"
LEDGER = "LEDGER_CONSOLIDATED.md"

BASE_FP = {
    CHECKER: "85e6aa9da34b9a32a5af64de60355661",
    RUNNER: "048464f05d8d150f0a269dc62583bc51",
    LEDGER: "3cb96041832d1173a216748bef37a0f7",
}


def fingerprint(path, data):
    lf = data.replace(b"\r\n", b"\n")
    if path == LEDGER:
        a = lf.index(INDEX_START)
        b = lf.index(INDEX_END) + len(INDEX_END)
        lf = lf[:a] + lf[b:]
    return hashlib.md5(lf).hexdigest()


# ============================================================ PART 1 + 2

CHECKER_STAMP_OLD = (
    b"Module updated: September 12, 2026 with Anthropic's Claude Opus 5\n"
    b"    (L-324: a row-shape guard. A value that is not a container\n"
    b"    literal must fit on the assignment's own line).\n"
)

CHECKER_STAMP_NEW = (
    b"Module updated: September 12, 2026 with Anthropic's Claude Opus 5\n"
    b"    (L-324: a row-shape guard. A value that is not a container\n"
    b"    literal must fit on the assignment's own line).\n"
    b"Module updated: September 12, 2026 with Anthropic's Claude Opus 5\n"
    b"    (L-324 follow-on: --shape-only runs the guard alone so the\n"
    b"    maintenance dashboard can carry it as its own row, and a shape\n"
    b"    failure is no longer counted as a malformed status line).\n"
)

CHECKER_MAIN_OLD = (
    b"def main():\n"
    b"    here = os.path.dirname(os.path.abspath(__file__))\n"
    b"    path = os.path.join(here, TARGET)\n"
    b"    if not os.path.exists(path):\n"
    b'        print("ERROR: %s is not beside this script." % TARGET)\n'
    b"        return 1\n"
    b"\n"
    b'    with open(path, "r") as handle:\n'
    b"        text = handle.read()\n"
    b"\n"
    b"    rows = parse_rows(text)\n"
    b"    known = set(row.name for row in rows)\n"
    b"    failures, softs = check_rows(rows, known)\n"
    b"\n"
    b"    shape_failures, shape_checked = check_row_shape(text)\n"
    b"    failures = failures + shape_failures\n"
)

CHECKER_MAIN_NEW = (
    b"def report_shape_only(text):\n"
    b'    """The row-shape guard alone, for the maintenance dashboard.\n'
    b"\n"
    b"    The dashboard prints ONE line per checker -- the last meaningful\n"
    b"    line of that tool's output -- so a guard reporting from inside\n"
    b"    another tool's summary never reaches it, even while it gates.\n"
    b"    A failure was visible, because it failed the row. A PASS was\n"
    b"    not, and a pass nobody can see is indistinguishable from a\n"
    b"    check that never ran.\n"
    b"\n"
    b"    So this mode ends on its own verdict, and that verdict names\n"
    b"    how many assignments were read. L-324.\n"
    b'    """\n'
    b"    failures, checked = check_row_shape(text)\n"
    b'    print("=" * 70)\n'
    b'    print("  ROW SHAPE -- %s" % TARGET)\n'
    b'    print("=" * 70)\n'
    b'    print("")\n'
    b'    print("A value that is not a container literal must fit on the")\n'
    b'    print("assignment\'s own line, because constants_change_report.py")\n'
    b'    print("reads values line by line off a git diff. Container")\n'
    b'    print("literals -- a dict or a list -- are exempt: a lookup table")\n'
    b'    print("cannot fit on one line and the report reads its entries")\n'
    b'    print("separately.")\n'
    b'    print("")\n'
    b"    if failures:\n"
    b'        print("FAILURES (%d):" % len(failures))\n'
    b"        for name, message in failures:\n"
    b'            print("  %-44s %s" % (name, message))\n'
    b'        print("")\n'
    b'        print("%d of %d row shapes are wrong in %s."\n'
    b"              % (len(failures), checked, TARGET))\n"
    b"        return 1\n"
    b'    print("All %d row shapes in %s fit the assignment\'s own line."\n'
    b"          % (checked, TARGET))\n"
    b"    return 0\n"
    b"\n"
    b"\n"
    b"def main():\n"
    b"    here = os.path.dirname(os.path.abspath(__file__))\n"
    b"    path = os.path.join(here, TARGET)\n"
    b"    if not os.path.exists(path):\n"
    b'        print("ERROR: %s is not beside this script." % TARGET)\n'
    b"        return 1\n"
    b"\n"
    b'    with open(path, "r") as handle:\n'
    b"        text = handle.read()\n"
    b"\n"
    b'    if "--shape-only" in sys.argv[1:]:\n'
    b"        return report_shape_only(text)\n"
    b"\n"
    b"    rows = parse_rows(text)\n"
    b"    known = set(row.name for row in rows)\n"
    b"    grammar_failures, softs = check_rows(rows, known)\n"
    b"\n"
    b"    shape_failures, shape_checked = check_row_shape(text)\n"
    b"    failures = grammar_failures + shape_failures\n"
)

CHECKER_CLOSE_OLD = (
    b"    if failures:\n"
    b'        print("FAILURES (%d):" % len(failures))\n'
    b"        for name, message in failures:\n"
    b'            print("  %-44s %s" % (name, message))\n'
    b'        print("")\n'
    b'        print("Results: %d checked, %d failed."\n'
    b"              % (len(with_status), len(failures)))\n"
    b'        print("")\n'
    b'        print("%d of %d status lines are malformed in %s."\n'
    b"              % (len(failures), len(with_status), TARGET))\n"
    b"        return 1\n"
    b"\n"
    b'    print("Results: %d checked, 0 failed." % len(with_status))\n'
    b'    print("")\n'
    b'    print("All %d status lines in %s are well formed; %d rows carry none."\n'
    b"          % (len(with_status), TARGET, len(rows) - len(with_status)))\n"
    b"    return 0\n"
)

CHECKER_CLOSE_NEW = (
    b"    # Two checks, two denominators. Status-line grammar is judged\n"
    b"    # against the rows that CARRY a status line; row shape is judged\n"
    b"    # against every top-level assignment. Merging the counts made a\n"
    b"    # shape failure print as a malformed status line, which names\n"
    b"    # the wrong thing and sends the reader to the wrong place.\n"
    b"    if failures:\n"
    b'        print("FAILURES (%d):" % len(failures))\n'
    b"        for name, message in failures:\n"
    b'            print("  %-44s %s" % (name, message))\n'
    b'        print("")\n'
    b'        print("Results: %d status line(s) checked, %d malformed;"\n'
    b'              " %d row shape(s) read, %d wrong."\n'
    b"              % (len(with_status), len(grammar_failures),\n"
    b"                 shape_checked, len(shape_failures)))\n"
    b'        print("")\n'
    b"        parts = []\n"
    b"        if grammar_failures:\n"
    b'            parts.append("%d of %d status lines are malformed"\n'
    b"                         % (len(grammar_failures), len(with_status)))\n"
    b"        if shape_failures:\n"
    b'            parts.append("%d of %d row shapes are wrong"\n'
    b"                         % (len(shape_failures), shape_checked))\n"
    b'        print("%s in %s." % (" and ".join(parts), TARGET))\n'
    b"        return 1\n"
    b"\n"
    b'    print("Results: %d status line(s) checked, 0 malformed;"\n'
    b'          " %d row shape(s) read, 0 wrong."\n'
    b"          % (len(with_status), shape_checked))\n"
    b'    print("")\n'
    b'    print("All %d status lines in %s are well formed; %d rows carry none."\n'
    b"          % (len(with_status), TARGET, len(rows) - len(with_status)))\n"
    b"    return 0\n"
)

# ============================================================ RUNNER

RUNNER_STAMP_OLD = (
    b"Module updated: September 2026 with Anthropic's Claude Opus 5 (L-305: the\n"
    b"CHECKERS list gains test_status_lines.py, which enforces the Status Line\n"
    b"grammar on every constants_new.py row that carries one.)\n"
)

RUNNER_STAMP_NEW = (
    b"Module updated: September 2026 with Anthropic's Claude Opus 5 (L-305: the\n"
    b"CHECKERS list gains test_status_lines.py, which enforces the Status Line\n"
    b"grammar on every constants_new.py row that carries one.)\n"
    b"Module updated: September 12, 2026 with Anthropic's Claude Opus 5 (L-324:\n"
    b"the CHECKERS list gains Row shape -- the same script run --shape-only --\n"
    b"so the row-shape guard reports its own numbers here instead of printing\n"
    b"them above another checker's verdict, where the dashboard never saw them.)\n"
)

RUNNER_ROW_OLD = (
    b"    ('Status lines', ['test_status_lines.py'], None),\n"
)

RUNNER_ROW_NEW = (
    b"    ('Status lines', ['test_status_lines.py'], None),\n"
    b"    # The same script, --shape-only. The row-shape guard also runs\n"
    b"    # inside the row above and gates there, so this is not what\n"
    b"    # makes it enforce. It is what makes it VISIBLE: the dashboard\n"
    b"    # shows one line per checker and that line was the status-line\n"
    b"    # verdict, so a passing guard printed nothing here and could\n"
    b"    # not be told from a guard that never ran. L-324.\n"
    b"    ('Row shape', ['test_status_lines.py', '--shape-only'], None),\n"
)

# ============================================================ LEDGER

LEDGER_GAP_OLD = (
    b"**Gap:** confirm both on the next maintenance run, then close. The\n"
    b"change report prints how many removal verdicts it cross-checked and\n"
    b"against how many names; the checker prints how many assignments it\n"
    b"read and how many failed. Both are new lines, so a pass carries its\n"
    b"own evidence rather than being inferred from silence.\n"
)

LEDGER_GAP_NEW = (
    b"**Note (2026-09-12) -- the guard gated but did not SHOW, and the\n"
    b"failure line named the wrong thing.** Tony read the maintenance\n"
    b"dashboard after the build and could not find the check. The\n"
    b"dashboard prints one line per checker -- the last meaningful line of\n"
    b"that tool's output -- so the row-shape numbers printed above\n"
    b"`test_status_lines.py`'s status-line verdict and never reached it.\n"
    b"The guard was gating the whole time: a shape failure exits 1 and\n"
    b"fails the Status lines row. But a PASS showed nothing, and a pass\n"
    b"nobody can see is indistinguishable from a check that never ran,\n"
    b"which is this protocol's A Check That Cannot Fail read from the\n"
    b"visibility side. Fixed with its own row: `test_status_lines.py\n"
    b"--shape-only`, registered in `orrery_maintenance_run.py` as `Row\n"
    b"shape`, ending on a verdict that names how many assignments it\n"
    b"read. Gating checkers go 12 to 13.\n"
    b"**Note (2026-09-12) -- a defect this item's own build introduced.**\n"
    b"Shape failures were appended to the status-line failure list, so on\n"
    b"a shape failure the closing line read \"1 of 19 status lines are\n"
    b"malformed\". No status line was malformed, and 19 is the wrong\n"
    b"denominator: the shape check reads 103 assignments, the grammar\n"
    b"check judges the 19 rows that carry a status line. Two checks, two\n"
    b"denominators, now counted and named separately. Caught by running\n"
    b"the failure path rather than by reading the code.\n"
    b"**Gap:** confirm `Row shape` appears in the dashboard's checker list\n"
    b"reporting 103 read and 0 wrong, then close. The first half is\n"
    b"already confirmed: the run at `6284215b` passed 12 of 12 gating\n"
    b"checkers, with the change report reporting no changes to\n"
    b"`constants_new.py` and the status-line checker clean.\n"
)

LEDGER_STAMP_OLD = (
    b"(L-324 built mechanically on Tony's ruling: the change report\n"
    b"cross-checks a removal against the working copy, and\n"
    b"test_status_lines.py guards row shape), built on bbd2dbe9.\n"
    b"Review and RICE update Tony 6-21-2026"
)

LEDGER_STAMP_NEW = (
    b"(L-324 built mechanically on Tony's ruling: the change report\n"
    b"cross-checks a removal against the working copy, and\n"
    b"test_status_lines.py guards row shape), built on bbd2dbe9.\n"
    b"Module updated: September 12, 2026 with Anthropic's Claude Opus 5\n"
    b"(L-324 follow-on: the row-shape guard gets its own dashboard row,\n"
    b"and a shape failure is no longer counted as a malformed status\n"
    b"line), built on 6284215b.\n"
    b"Review and RICE update Tony 6-21-2026"
)

EDITS = {
    CHECKER: [
        ("checker: --shape-only mode", CHECKER_MAIN_OLD, CHECKER_MAIN_NEW),
        ("checker: two denominators, named separately",
         CHECKER_CLOSE_OLD, CHECKER_CLOSE_NEW),
    ],
    RUNNER: [
        ("runner: Row shape row", RUNNER_ROW_OLD, RUNNER_ROW_NEW),
    ],
    LEDGER: [
        ("ledger: L-324 visibility note, defect note and Gap",
         LEDGER_GAP_OLD, LEDGER_GAP_NEW),
    ],
}

STAMPS = {
    CHECKER: CHECKER_STAMP_OLD, RUNNER: RUNNER_STAMP_OLD,
    LEDGER: LEDGER_STAMP_OLD,
}
STAMPS_NEW = {
    CHECKER: CHECKER_STAMP_NEW, RUNNER: RUNNER_STAMP_NEW,
    LEDGER: LEDGER_STAMP_NEW,
}


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    originals = {}

    for path in (CHECKER, RUNNER, LEDGER):
        full = os.path.join(here, path)
        if not os.path.exists(full):
            print("ERROR: %s not found. Save this script into the orrery "
                  "repo root and Run again." % path)
            return 1
        with open(full, "rb") as handle:
            originals[path] = handle.read()

    for path, data in originals.items():
        try:
            fp = fingerprint(path, data)
        except ValueError:
            print("ERROR: INDEX zone markers not found in %s. NOTHING "
                  "written." % path)
            return 1
        if fp != BASE_FP[path]:
            print("ERROR: base moved. %s does not match the tree this patch "
                  "was built against." % path)
            print("  expected %s" % BASE_FP[path])
            print("  found    %s" % fp)
            print("NOTHING was written, to any of the three files.")
            return 1

    updated = {}
    applied = []
    stamped = []

    for path, data in originals.items():
        is_crlf = data.count(b"\r\n") > 0
        new = data
        todo = list(EDITS[path]) + [
            ("%s: currency stamp" % path, STAMPS[path], STAMPS_NEW[path])]
        for label, old, repl in todo:
            o, r = old, repl
            if is_crlf:
                o = o.replace(b"\n", b"\r\n")
                r = r.replace(b"\n", b"\r\n")
            n = new.count(o)
            if n != 1:
                print("ANCHOR FAIL: %s -- expected 1 match in %s, found %d."
                      % (label, path, n))
                print("NOTHING was written, to any of the three files.")
                print("Undo is Discard Changes in GitHub Desktop.")
                return 1
            new = new.replace(o, r)
            if label.endswith("currency stamp"):
                stamped.append(path)
            else:
                applied.append(label)
        non_ascii = sum(1 for ch in new if ch > 127)
        if non_ascii:
            print("ERROR: patch would introduce %d non-ASCII byte(s) into "
                  "%s. NOTHING written." % (non_ascii, path))
            return 1
        updated[path] = new

    for path, new in updated.items():
        with open(os.path.join(here, path), "wb") as handle:
            handle.write(new)

    for label in applied:
        print("ok  %s" % label)
    for path in stamped:
        print("stamp updated  %s" % path)
    print("patch applied (%d files)" % len(updated))
    print("")
    print("NEXT:")
    print("  1. Run test_status_lines.py -- the closing lines now report")
    print("     the two counts separately.")
    print("  2. Run orrery_maintenance_run.py -- a new 'Row shape' row")
    print("     appears after 'Status lines'. Gating total goes 12 -> 13.")
    print("  3. Run ledger_index.py as a parse check -- expect")
    print("     'OK: 319 L-blocks parsed, no consistency problems.'")
    return 0


if __name__ == "__main__":
    sys.exit(main())
