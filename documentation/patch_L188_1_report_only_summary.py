"""patch_L188_1_report_only_summary.py -- L-188.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the same folder as
maintenance_run.py), open it in VS Code, and click Run.

    python patch_L188_1_report_only_summary.py

Success prints one `ok` line and then `patch applied`. Failure prints a
single ERROR or ANCHOR FAIL line and writes NOTHING.

WHAT IT DOES
------------
One file, four edits, one behaviour: the runner's last line stops
saying the same thing regardless of what was found.

THE DEFECT. Eleven of the thirteen CHECKERS rows are pass/fail -- they
exit non-zero when something is wrong. Two are REPORT-ONLY by design:
`worksheet_checker.py` and `provenance_scanner.py` exit 0 whatever they
find, and exit 1 only when they could not run at all. The summary line
counted all thirteen the same way, so it read

    All 13 checkers passed

above a row reporting 289 Tier-1 findings and another reporting 68 of
110 rows routed. Both true. Read together, the last line tells someone
scanning for a verdict that there is nothing to act on.

That is the shape the protocol's own gate names: a line that reads
identically whether the scanner found 289 or 0 cannot inform, because
it cannot move. The runner already applies this reasoning to the
worksheet checker's own summary line, which carries a denominator "so
the number moves when something moves." The runner's line did not.

THE FIX. `CHECKERS` rows gain an optional fourth field marking a tool
report-only, set on exactly the two that are. The summary then counts
the gating checkers in its headline and quotes the report-only tools'
own verdicts underneath:

    11 of 11 gating checkers passed -- 83.0s total
    2 report-only, exit 0 whatever they find:
      Worksheet checker         68 of 110 routed, 8 clean
      Provenance scanner        289 TIER-1 FINDINGS IN THE SCANNED TREE

The quoted text is each tool's own note, the same string already
printed in its row -- not a restatement. A restatement would be a
second copy of a number, free to drift from the first.

The block prints in BOTH branches. When a gating checker fails, the
scanner's count is still the thing the push call turns on, so hiding it
behind a failure would be the same defect wearing different clothes.

EXIT CODE IS UNCHANGED. Any checker exiting non-zero still fails the
run, report-only included -- for those two, a non-zero exit means the
tool could not run, which is a real failure and not a finding.

WHAT IS PERMANENT AND WHAT IS NOT
---------------------------------
This script is disposable and one-shot. Permanent: the `report_only`
field in CHECKERS and the summary block that reads it.

AFTER RUNNING
-------------
1. python maintenance_run.py     (read the last four lines)
2. Archive this script to documentation/. Until you do, it sits in the
   repo root as a .py file and the scanner scores its FINGERPRINTS dict
   as one Tier-1 finding -- which is why the count reads 290 rather
   than 289 between running this and archiving it.

Module created: August 17, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys


FINGERPRINTS = {
    'maintenance_run.py': '6f68d607545fb59d748270acd4aa1674',
}


# ---- edit 1: the docstring's OUTPUT section states the distinction --

DOC_ANCHOR = '''EXIT CODE
---------
0 when every checker passed, 1 when any failed. The generators do not
affect it -- a regenerated file is the normal case, not a problem.'''

DOC_NEW = '''GATING AND REPORT-ONLY
----------------------
Eleven checkers are pass/fail: a problem makes them exit non-zero.
Two are REPORT-ONLY -- worksheet_checker.py and provenance_scanner.py
exit 0 whatever they find, and exit 1 only when they could not run.
They are marked in the CHECKERS table, and the summary counts the
gating eleven in its headline and quotes the two report-only verdicts
underneath.

The block quotes each tool's own note rather than restating it. A
restatement would be a second copy of a number, free to drift from the
first, and the whole point of the line is that it moves when the number
moves.

EXIT CODE
---------
0 when every checker passed, 1 when any failed. The generators do not
affect it -- a regenerated file is the normal case, not a problem.
Report-only tools take part: a non-zero exit from one of them means it
could not run, which is a failure and not a finding.'''


# ---- edit 2: the two report-only rows are marked --------------------

TABLE_ANCHOR = """    ('Worksheet checker', ['worksheet_checker.py'], 'WORKSHEET CHECK:'),
    ('Worksheet checker tests', ['test_worksheet_checker.py'], None),
    ('Worksheet key round trip', ['test_worksheet_keys.py'], None),
    ('Builder marker join', ['test_worksheet_request_builder.py'], None),
    ('Extractor pins', ['test_extractor_pins.py'], None),
    ('Provenance scanner', ['provenance_scanner.py'], 'TIER-1 FINDINGS'),
]"""

TABLE_NEW = """    # A fourth field marks a tool REPORT-ONLY: it exits 0 whatever it
    # finds, so "passed" says only that it ran. Exactly two are, and
    # both are deliberate -- their numbers are the verdict, not their
    # exit codes. Omit the field and a row gates, which is the safe
    # default for anything added later.
    ('Worksheet checker', ['worksheet_checker.py'], 'WORKSHEET CHECK:',
     True),
    ('Worksheet checker tests', ['test_worksheet_checker.py'], None),
    ('Worksheet key round trip', ['test_worksheet_keys.py'], None),
    ('Builder marker join', ['test_worksheet_request_builder.py'], None),
    ('Extractor pins', ['test_extractor_pins.py'], None),
    ('Provenance scanner', ['provenance_scanner.py'], 'TIER-1 FINDINGS',
     True),
]"""


# ---- edit 3: the loop reads the optional field -----------------------

LOOP_ANCHOR = """    for label, argv_tail, hint in CHECKERS:
        rc, output, seconds = run_tool(project_dir, argv_tail)"""

LOOP_NEW = """    for entry in CHECKERS:
        label, argv_tail, hint = entry[0], entry[1], entry[2]
        report_only = entry[3] if len(entry) > 3 else False
        rc, output, seconds = run_tool(project_dir, argv_tail)"""

APPEND_ANCHOR = """        print_row(label, seconds, note)
        results.append((label, rc, seconds, note, output, True))
    print()"""

APPEND_NEW = """        print_row(label, seconds, note)
        results.append((label, rc, seconds, note, output, True,
                        report_only))
    print()"""


# ---- edit 4: the summary ---------------------------------------------

SUMMARY_ANCHOR = """    # ---- summary ------------------------------------------------------
    failed = [row for row in results if row[5] and row[1] != 0]
    total = sum(row[2] for row in results)

    print('=' * 70)
    if failed:
        print('  %d of %d checkers FAILED -- %.1fs total'
              % (len(failed), len(CHECKERS), total))
        print('  ' + ', '.join(row[0] for row in failed))
    else:
        print('  All %d checkers passed -- %.1fs total' % (len(CHECKERS), total))
    print('=' * 70)"""

SUMMARY_NEW = """    # ---- summary ------------------------------------------------------
    # A generator row is a 6-tuple and a checker row a 7-tuple, so the
    # report-only flag is read with a length guard rather than an index.
    checkers = [row for row in results if row[5]]
    failed = [row for row in checkers if row[1] != 0]
    report_only = [row for row in checkers if len(row) > 6 and row[6]]
    gating = [row for row in checkers if row not in report_only]
    total = sum(row[2] for row in results)

    print('=' * 70)
    if failed:
        print('  %d of %d checkers FAILED -- %.1fs total'
              % (len(failed), len(checkers), total))
        print('  ' + ', '.join(row[0] for row in failed))
    else:
        print('  %d of %d gating checkers passed -- %.1fs total'
              % (len(gating), len(gating), total))

    # Printed in BOTH branches on purpose. The scanner's count is the
    # number the push call turns on, so hiding it behind a failure
    # would be the same defect this block exists to remove. Each line
    # quotes the tool's own note -- the string already printed in its
    # row above -- rather than restating it, because a restatement is a
    # second copy of a number and free to drift from the first.
    if report_only:
        print('  %d report-only, exit 0 whatever they find:'
              % len(report_only))
        for row in report_only:
            print('    %-27s %s' % (row[0], row[3]))
    print('=' * 70)"""


DETAIL_ANCHOR = """    # ---- detail for failures only -------------------------------------
    for label, rc, seconds, note, output, is_checker in results:
        if rc == 0:
            continue"""

DETAIL_NEW = """    # ---- detail for failures only -------------------------------------
    # Indexed rather than unpacked: checker rows carry a seventh field
    # and generator rows do not, so a fixed-width unpack here raises on
    # the first checker row. It compiled cleanly and died on the run --
    # the compiler cannot see a tuple width.
    for row in results:
        label, rc, note, output = row[0], row[1], row[3], row[4]
        if rc == 0:
            continue"""


# ---- the row comment matches what is stored -------------------------

COMMENT_ANCHOR = """    results = []      # (label, rc, seconds, note, output)"""

COMMENT_NEW = """    # (label, rc, seconds, note, output, is_checker[, report_only])
    # Checker rows carry the seventh field; generator rows stop at six.
    # Read it with a length guard, never by unpacking a fixed width.
    results = []"""


PLAN = [
    ('maintenance_run.py', [
        (DOC_ANCHOR, DOC_NEW),
        (TABLE_ANCHOR, TABLE_NEW),
        (LOOP_ANCHOR, LOOP_NEW),
        (APPEND_ANCHOR, APPEND_NEW),
        (COMMENT_ANCHOR, COMMENT_NEW),
        (SUMMARY_ANCHOR, SUMMARY_NEW),
        (DETAIL_ANCHOR, DETAIL_NEW),
    ]),
]


def fingerprint(data):
    """Content fingerprint: line endings normalized before hashing."""
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def non_ascii(data):
    return [b for b in data if b > 127]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)

    for name, _edits in PLAN:
        if not os.path.isfile(name):
            print('ERROR: %s not found. Run this from the repo root.' % name)
            return 1
        with open(name, 'rb') as handle:
            data = handle.read()
        seen = fingerprint(data)
        want = FINGERPRINTS[name]
        if seen != want:
            print('ERROR: %s has moved. Expected %s, found %s.'
                  % (name, want, seen))
            print('       Nothing written. Built against '
                  'ae1883bd5ccce525b1734e99f48ed501819b77df.')
            return 1

    staged = {}
    notes = []
    for name, edits in PLAN:
        with open(name, 'rb') as handle:
            data = handle.read()
        is_crlf = data.count(b'\r\n') > 0
        content = data
        for old, new in edits:
            old_b = old.encode('utf-8')
            new_b = new.encode('utf-8')
            if non_ascii(new_b):
                print('ERROR: this patch would insert non-ASCII bytes into '
                      '%s. Nothing written.' % name)
                return 1
            if is_crlf:
                old_b = old_b.replace(b'\n', b'\r\n')
                new_b = new_b.replace(b'\n', b'\r\n')
            count = content.count(old_b)
            if count != 1:
                print('ANCHOR FAIL: %s -- expected 1 match, found %d for:'
                      % (name, count))
                print('   %s' % old.splitlines()[0][:70])
                print('Nothing written.')
                return 1
            content = content.replace(old_b, new_b)
        left = non_ascii(content)
        if left:
            notes.append('note: %s still holds %d non-ASCII byte(s) this '
                         'patch did not reach' % (name, len(left)))
        staged[name] = content

    written = 0
    for name, edits in PLAN:
        with open(name, 'wb') as handle:
            handle.write(staged[name])
        written += len(staged[name])
        print('ok  %s (%d edits)' % (name, len(edits)))

    for note in notes:
        print(note)
    print('patch applied (%d bytes)' % written)
    print('')
    print('Next: python maintenance_run.py -- the last four lines should')
    print('      read "11 of 11 gating checkers passed", then the two')
    print('      report-only tools with their own numbers.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
