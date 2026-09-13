"""
patch_L324_removal_crosscheck_and_row_shape_guard.py

Closes the L-324 build in two parts, plus the ledger record.

PART 1 -- constants_change_report.py stops printing a false removal.
    The tool reported EARTH_BOW_SHOCK_STANDOFF_RADII as REMOVED when the
    constant was sitting in the file the whole time; it simply could not
    read a value spread over three lines. The `removed` list is built
    from the git diff alone. This patch asks the working copy whether
    the name still exists before printing that verdict, and reports
    "STILL PRESENT -- value unreadable" instead, which fails the run.
    The tool already parsed both revisions with Python's own ast reader
    to build its name list; it never consulted it here.

PART 2 -- test_status_lines.py gains a mechanical row-shape guard.
    A top-level assignment whose value is NOT a container literal must
    fit on the assignment's own line. Container literals -- a dict or a
    list -- may span lines, because a lookup table cannot fit on one and
    the change report reads their entries separately.

    This is why the guard is not "one assignment per line":
    constants_new.py holds four multi-line top-level assignments today
    and ALL FOUR are container literals -- CENTER_BODY_RADII,
    KNOWN_ORBITAL_PERIODS, stellar_class_labels, spectral_subclass_temps.
    A skill sentence saying "one assignment per line" would have been
    false about four rows on the day it was written.

    test_status_lines.py runs on the whole store every maintenance run,
    not on a diff, so this check cannot be skipped by nobody touching
    the line.

PART 3 -- LEDGER_CONSOLIDATED.md records the ruling and what was built,
    and gains two header stamps: one for this change, and one for the
    2026-09-12 L-305 item 4 build, which did not stamp the file. That
    retroactive stamp is added on Tony's explicit approval.

WHAT IS PERMANENT AND WHAT IS NOT
    This script is disposable and one-shot. The two checks it installs
    are permanent, and so is the ledger record.

HOW TO RUN IT (Tony)
    Save this file into the orrery repo root -- the same folder as
    constants_change_report.py -- open it in VS Code, and click Run.
    Equivalent command: python patch_L324_removal_crosscheck_and_row_shape_guard.py

    Success: one "ok" line per edit, three "stamp updated" lines, then
             "patch applied".
    Failure: one ERROR or ANCHOR FAIL line. NOTHING is written, to ANY
             of the three files -- all three are written together or
             none is. Undo is Discard Changes in GitHub Desktop.

AFTER IT RUNS
    1. Run test_status_lines.py (Run button). Expect a new "Row shape:"
       line reporting how many assignments it read and 0 failed.
    2. Run orrery_maintenance_run.py (Run button) as usual.
    3. Run ledger_index.py (Run button) as a parse check. Expect
       "OK: 319 L-blocks parsed, no consistency problems." No index row
       changes, because no title, status, score or date changed.

BASE
    Built on orrery bbd2dbe90a0d3ffb9f7b7e72b038eef39a537ca4 at
    https://github.com/tonylquintanilla/palomas_orrery
    The ledger guard fingerprints content OUTSIDE the INDEX zone, which
    ledger_index.py regenerates.

Written September 12, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

INDEX_START = b"<!-- INDEX:START"
INDEX_END = b"<!-- INDEX:END -->"

REPORT = "constants_change_report.py"
CHECKER = "test_status_lines.py"
LEDGER = "LEDGER_CONSOLIDATED.md"

BASE_FP = {
    REPORT: "0801618bbb5fb5bfe412cb7a38aa74b3",
    CHECKER: "5b06497dde15c4224afa764509a35d33",
    LEDGER: "1b367ee800d683895c6bca8bf1d58826",
}


def fingerprint(path, data):
    lf = data.replace(b"\r\n", b"\n")
    if path == LEDGER:
        a = lf.index(INDEX_START)
        b = lf.index(INDEX_END) + len(INDEX_END)
        lf = lf[:a] + lf[b:]
    return hashlib.md5(lf).hexdigest()


# ============================================================ PART 1

REPORT_STAMP_OLD = (
    b"Module updated: August 25, 2026 with Anthropic's Claude Opus 5\n"
    b"    (L-249 step 1: NAME = EXPR over tracked constants is a third case,\n"
    b"    DERIVED, so following the unit-variant convention no longer fails\n"
    b"    this gate).\n"
)

REPORT_STAMP_NEW = (
    b"Module updated: August 25, 2026 with Anthropic's Claude Opus 5\n"
    b"    (L-249 step 1: NAME = EXPR over tracked constants is a third case,\n"
    b"    DERIVED, so following the unit-variant convention no longer fails\n"
    b"    this gate).\n"
    b"Module updated: September 12, 2026 with Anthropic's Claude Opus 5\n"
    b"    (L-324: a removal verdict is cross-checked against the working\n"
    b"    copy before it is printed. A name the diff dropped but the file\n"
    b"    still assigns is reported unreadable, not removed).\n"
)

REPORT_FUNC_OLD = b'def parse_derived(line, tracked):\n'

REPORT_FUNC_NEW = (
    b'def working_copy_names(here):\n'
    b'    """Every name assigned at module level in the WORKING copy.\n'
    b'\n'
    b'    module_level_names() returns the UNION of base and working, which\n'
    b'    cannot answer the one question a removal verdict rests on: does\n'
    b'    this name still exist NOW. So this reads the working copy alone.\n'
    b'\n'
    b'    Returns None if the file cannot be read or parsed. None means the\n'
    b'    cross-check did not happen, and the caller says so rather than\n'
    b'    letting an unchecked verdict print as if it had been checked.\n'
    b'    """\n'
    b'    try:\n'
    b'        with open(os.path.join(here, TARGET), \'rb\') as handle:\n'
    b'            tree = ast.parse(handle.read().decode(\'utf-8\', \'replace\'))\n'
    b'    except (OSError, SyntaxError, ValueError):\n'
    b'        return None\n'
    b'    names = set()\n'
    b'    for node in tree.body:\n'
    b'        if isinstance(node, ast.Assign):\n'
    b'            targets = node.targets\n'
    b'        elif isinstance(node, ast.AnnAssign):\n'
    b'            targets = [node.target]\n'
    b'        else:\n'
    b'            continue\n'
    b'        for target in targets:\n'
    b'            if isinstance(target, ast.Name):\n'
    b'                names.add(target.id)\n'
    b'    return names\n'
    b'\n'
    b'\n'
    b'def parse_derived(line, tracked):\n'
)

REPORT_SPLIT_OLD = (
    b"    derived_changed, derived_added, derived_removed = derived\n"
    b"\n"
    b"    if not (changed or added or removed or unparsed or derived_changed\n"
    b"            or derived_added or derived_removed):\n"
)

REPORT_SPLIT_NEW = (
    b"    derived_changed, derived_added, derived_removed = derived\n"
    b"\n"
    b"    # A name can leave the DIFF without leaving the FILE. The diff\n"
    b"    # reads lines: rewrite a value in a shape this reader cannot\n"
    b"    # parse -- a right-hand side spread over several lines, say --\n"
    b"    # and the name's old line vanishes with no new one to replace\n"
    b"    # it, which is indistinguishable from a deletion. So ask the\n"
    b"    # file itself before saying REMOVED. A wrong verdict is worse\n"
    b"    # than an announced gap: it reads as a fact and nobody\n"
    b"    # re-checks it. L-324.\n"
    b"    present = working_copy_names(here)\n"
    b"    unreadable = []\n"
    b"    if present is None:\n"
    b"        removal_note = ('working copy could not be parsed -- removal'\n"
    b"                        ' verdicts below are from the diff alone and'\n"
    b"                        ' were NOT cross-checked')\n"
    b"    else:\n"
    b"        unreadable = [(n, b) for n, b in removed if n in present]\n"
    b"        removed = [(n, b) for n, b in removed if n not in present]\n"
    b"        removal_note = ('%d removal verdict(s) cross-checked against'\n"
    b"                        ' the %d name(s) the working copy assigns'\n"
    b"                        % (len(removed) + len(unreadable), len(present)))\n"
    b"\n"
    b"    if not (changed or added or removed or unreadable or unparsed\n"
    b"            or derived_changed or derived_added or derived_removed):\n"
)

REPORT_PRINT_OLD = (
    b"    for name, before in removed:\n"
    b"        print('  %-30s REMOVED (was %s)' % (name, before))\n"
    b"        print()\n"
)

REPORT_PRINT_NEW = (
    b"    for name, before in unreadable:\n"
    b"        print('  %-30s STILL PRESENT -- value unreadable' % name)\n"
    b"        print('      The diff dropped this name (was %s), but the'\n"
    b"              % before)\n"
    b"        print('      working copy still assigns it at module level.')\n"
    b"        print('      Its value is written in a shape this reader')\n"
    b"        print('      cannot see -- most often a right-hand side')\n"
    b"        print('      spread over more than one line. This is NOT a')\n"
    b"        print('      removal, and the value has NOT been checked.')\n"
    b"        print('      Put the assignment on one line, or read it by')\n"
    b"        print('      hand before committing.')\n"
    b"        print()\n"
    b"\n"
    b"    for name, before in removed:\n"
    b"        print('  %-30s REMOVED (was %s)' % (name, before))\n"
    b"        print()\n"
)

REPORT_SUMMARY_OLD = (
    b"    print('-' * 70)\n"
    b"    print('  %d changed, %d added, %d removed'\n"
    b"          % (len(changed), len(added), len(removed)))\n"
)

REPORT_SUMMARY_NEW = (
    b"    print('-' * 70)\n"
    b"    print('  %d changed, %d added, %d removed'\n"
    b"          % (len(changed), len(added), len(removed)))\n"
    b"    print('  %s' % removal_note)\n"
    b"    if unreadable:\n"
    b"        print('  %d name(s) the diff called gone that the file still'\n"
    b"              ' assigns: %s'\n"
    b"              % (len(unreadable), ', '.join(n for n, _ in unreadable)))\n"
)

REPORT_RETURN_OLD = (
    b"    return 1 if (bare or unclear or unparsed or derived_bare) else 0\n"
)

REPORT_RETURN_NEW = (
    b"    return 1 if (bare or unclear or unparsed or derived_bare\n"
    b"                 or unreadable) else 0\n"
)

# ============================================================ PART 2

CHECKER_STAMP_OLD = (
    b"Module created: September 2026 with Anthropic's Claude Opus 5.\n"
)

CHECKER_STAMP_NEW = (
    b"Module created: September 2026 with Anthropic's Claude Opus 5.\n"
    b"Module updated: September 12, 2026 with Anthropic's Claude Opus 5\n"
    b"    (L-324: a row-shape guard. A value that is not a container\n"
    b"    literal must fit on the assignment's own line).\n"
)

CHECKER_IMPORT_OLD = b"import os\nimport re\nimport sys\n"
CHECKER_IMPORT_NEW = b"import ast\nimport os\nimport re\nimport sys\n"

CHECKER_FUNC_OLD = (
    b"def main():\n"
    b"    here = os.path.dirname(os.path.abspath(__file__))\n"
)

CHECKER_FUNC_NEW = (
    b"def check_row_shape(text):\n"
    b'    """Return (failures, checked) for the shape of every top-level row.\n'
    b"\n"
    b"    A value that is not a container literal must fit on the\n"
    b"    assignment's own line. constants_change_report.py reads values\n"
    b"    line by line off a git diff, so a right-hand side spread over\n"
    b"    several lines leaves the name with nothing readable after the\n"
    b"    equals sign -- which it once reported as a REMOVED constant.\n"
    b"\n"
    b"    Container literals are exempt and must be. A dict or list is a\n"
    b"    lookup table that cannot fit on one line, and the change report\n"
    b"    reads its entries separately. Four rows here are exactly that:\n"
    b"    CENTER_BODY_RADII, KNOWN_ORBITAL_PERIODS, stellar_class_labels\n"
    b"    and spectral_subclass_temps. A flat one-assignment-per-line rule\n"
    b"    would be false about all four.\n"
    b"\n"
    b"    This runs on the whole file every time rather than on a diff, so\n"
    b"    it also sees rows nobody touched this session. L-324.\n"
    b'    """\n'
    b"    try:\n"
    b"        tree = ast.parse(text)\n"
    b"    except SyntaxError as exc:\n"
    b"        return ([(TARGET, 'could not be parsed (%s)' % exc)], 0)\n"
    b"    failures = []\n"
    b"    checked = 0\n"
    b"    for node in tree.body:\n"
    b"        if isinstance(node, ast.Assign):\n"
    b"            targets = node.targets\n"
    b"        elif isinstance(node, ast.AnnAssign):\n"
    b"            targets = [node.target]\n"
    b"        else:\n"
    b"            continue\n"
    b"        checked += 1\n"
    b"        if isinstance(node.value,\n"
    b"                      (ast.Dict, ast.List, ast.Tuple, ast.Set)):\n"
    b"            continue\n"
    b"        if getattr(node, 'end_lineno', node.lineno) == node.lineno:\n"
    b"            continue\n"
    b"        for target in targets:\n"
    b"            if isinstance(target, ast.Name):\n"
    b"                failures.append((\n"
    b"                    target.id,\n"
    b"                    'value spans lines %d-%d; a non-container value '\n"
    b"                    'must fit on its own line (L-324)'\n"
    b"                    % (node.lineno, node.end_lineno)))\n"
    b"    return (failures, checked)\n"
    b"\n"
    b"\n"
    b"def main():\n"
    b"    here = os.path.dirname(os.path.abspath(__file__))\n"
)

CHECKER_WIRE_OLD = (
    b"    failures, softs = check_rows(rows, known)\n"
)

CHECKER_WIRE_NEW = (
    b"    failures, softs = check_rows(rows, known)\n"
    b"\n"
    b"    shape_failures, shape_checked = check_row_shape(text)\n"
    b"    failures = failures + shape_failures\n"
)

CHECKER_PRINT_OLD = (
    b'    print("  These are scored by the scanner\'s window inference, which the")\n'
    b'    print("  Status Line rule says to delete. That walk is L-322\'s.")\n'
    b'    print("")\n'
)

CHECKER_PRINT_NEW = (
    b'    print("  These are scored by the scanner\'s window inference, which the")\n'
    b'    print("  Status Line rule says to delete. That walk is L-322\'s.")\n'
    b'    print("")\n'
    b'    print("Row shape: %d top-level assignment(s) read, %d failed."\n'
    b'          % (shape_checked, len(shape_failures)))\n'
    b'    print("  A value that is not a container literal must fit on the")\n'
    b'    print("  assignment\'s own line, because constants_change_report.py")\n'
    b'    print("  reads values line by line (L-324).")\n'
    b'    print("")\n'
)

# ============================================================ PART 3

LEDGER_GAP_OLD = b"**Gap:** decide which fix, then do it.\n"

LEDGER_GAP_NEW = (
    b"**Note (2026-09-12) -- Tony's ruling: make it mechanical, not a rule.**\n"
    b"Asked whether the convention could be a guard rather than a line in a\n"
    b"skill that a session can overlook. It can, and building it found what\n"
    b"a written rule would have got wrong. `constants_new.py` holds FOUR\n"
    b"multi-line top-level assignments today -- `CENTER_BODY_RADII`,\n"
    b"`KNOWN_ORBITAL_PERIODS`, `stellar_class_labels` and\n"
    b"`spectral_subclass_temps` -- and all four are container literals, a\n"
    b"dict or a list. A lookup table cannot fit on one line and should not.\n"
    b"So the rule is NOT one assignment per line. It is that a value which\n"
    b"is not a container literal must fit on the assignment's own line. A\n"
    b"skill sentence saying \"one assignment per line\" would have been false\n"
    b"about four rows on the day it was written, and nothing would have\n"
    b"caught that, because a sentence in a skill is never run against the\n"
    b"file it describes. [verified @bbd2dbe9]\n"
    b"**Note (2026-09-12) -- what was built, in two halves.** First, the\n"
    b"false verdict is gone. `constants_change_report.py` now asks the\n"
    b"working copy whether a name still exists before printing REMOVED,\n"
    b"and prints `STILL PRESENT -- value unreadable` instead, which fails\n"
    b"the run and says the value was not checked. The tool already parsed\n"
    b"both revisions with `ast` to build its name list; it simply never\n"
    b"asked it here, so `removed` came from the diff hunk alone. Second,\n"
    b"the guard. `test_status_lines.py` walks every top-level assignment\n"
    b"and fails any non-container value spanning more than one line,\n"
    b"naming the row and its line span. That file reads the whole store\n"
    b"every maintenance run rather than a diff, so the check cannot be\n"
    b"skipped by nobody touching the line -- which is the failure mode a\n"
    b"skill rule has and this does not.\n"
    b"**Note (2026-09-12) -- the two halves answer different questions.**\n"
    b"The guard stops the shape being written. The cross-check stops the\n"
    b"tool lying when it is written anyway -- by a hand edit, a merge, or\n"
    b"a file the guard does not read. Neither makes the other redundant.\n"
    b"**Gap:** confirm both on the next maintenance run, then close. The\n"
    b"change report prints how many removal verdicts it cross-checked and\n"
    b"against how many names; the checker prints how many assignments it\n"
    b"read and how many failed. Both are new lines, so a pass carries its\n"
    b"own evidence rather than being inferred from silence.\n"
)

LEDGER_STAMP_OLD = (
    b"\"Verified: April 2026\" stamp class to L-181; L-323's Gap corrected\n"
    b"against the repo), built on 56f96004.\n"
    b"Review and RICE update Tony 6-21-2026"
)

LEDGER_STAMP_NEW = (
    b"\"Verified: April 2026\" stamp class to L-181; L-323's Gap corrected\n"
    b"against the repo), built on 56f96004.\n"
    b"Module updated: September 12, 2026 with Anthropic's Claude Opus 5\n"
    b"(L-305 item 4: fifteen new magnetosphere rows, both standoffs\n"
    b"superseded and derived, three retired claims removed; L-323 and\n"
    b"L-324 opened; the bow shock hover's Lugaz-midpoint sentence deleted\n"
    b"and its attribution moved to Jelinek), built on 5b88007f. Recorded\n"
    b"later the same day by a following session, on Tony's approval: that\n"
    b"build edited this file without stamping it.\n"
    b"Module updated: September 12, 2026 with Anthropic's Claude Opus 5\n"
    b"(L-324 built mechanically on Tony's ruling: the change report\n"
    b"cross-checks a removal against the working copy, and\n"
    b"test_status_lines.py guards row shape), built on bbd2dbe9.\n"
    b"Review and RICE update Tony 6-21-2026"
)

EDITS = {
    REPORT: [
        ("report: working_copy_names()", REPORT_FUNC_OLD, REPORT_FUNC_NEW),
        ("report: split removals from unreadables",
         REPORT_SPLIT_OLD, REPORT_SPLIT_NEW),
        ("report: STILL PRESENT block", REPORT_PRINT_OLD, REPORT_PRINT_NEW),
        ("report: summary names them",
         REPORT_SUMMARY_OLD, REPORT_SUMMARY_NEW),
        ("report: unreadable fails the run",
         REPORT_RETURN_OLD, REPORT_RETURN_NEW),
    ],
    CHECKER: [
        ("checker: import ast", CHECKER_IMPORT_OLD, CHECKER_IMPORT_NEW),
        ("checker: check_row_shape()", CHECKER_FUNC_OLD, CHECKER_FUNC_NEW),
        ("checker: wired into main", CHECKER_WIRE_OLD, CHECKER_WIRE_NEW),
        ("checker: coverage line", CHECKER_PRINT_OLD, CHECKER_PRINT_NEW),
    ],
    LEDGER: [
        ("ledger: L-324 ruling, build record and Gap",
         LEDGER_GAP_OLD, LEDGER_GAP_NEW),
    ],
}

STAMPS = {
    REPORT: ("report", REPORT_STAMP_OLD, REPORT_STAMP_NEW),
    CHECKER: ("checker", CHECKER_STAMP_OLD, CHECKER_STAMP_NEW),
    LEDGER: ("ledger", LEDGER_STAMP_OLD, LEDGER_STAMP_NEW),
}


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    originals = {}

    for path in (REPORT, CHECKER, LEDGER):
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

    # Apply everything in memory first. Nothing reaches disk until all
    # three files have accepted every anchor -- one failure leaves the
    # working copy exactly as it was.
    updated = {}
    applied = []
    stamped = []

    for path, data in originals.items():
        is_crlf = data.count(b"\r\n") > 0
        new = data
        for label, old, repl in list(EDITS[path]) + [
                ("%s: currency stamp" % STAMPS[path][0],
                 STAMPS[path][1], STAMPS[path][2])]:
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
    print("  1. Run test_status_lines.py -- expect a new 'Row shape:' line")
    print("     reading 103 assignment(s) and 0 failed.")
    print("  2. Run orrery_maintenance_run.py as usual.")
    print("  3. Run ledger_index.py as a parse check -- expect")
    print("     'OK: 319 L-blocks parsed, no consistency problems.'")
    return 0


if __name__ == "__main__":
    sys.exit(main())
