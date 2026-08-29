"""maintenance_run.py -- L-188. One command, the whole maintenance suite.

RUN COMMAND
-----------
Open this file in VS Code and click Run. It takes no arguments.

    python maintenance_run.py

Run it after any edit session and before a push.

WHAT IT DOES
------------
Runs the four GENERATORS, then the CHECKERS, and prints one summary at
the end. Nothing stops on a failure -- every tool runs every time, so a
single pass shows the whole picture rather than the first problem in it.

The staleness report comes FIRST, before anything else runs. That
ordering is load-bearing: this runner runs provenance_scanner.py, so
asking afterwards whether the scanner is overdue would always read
fresh and the check could never fire. It is read off
data/provenance_history.json at the top, describing the state you
arrived in.

GENERATORS rewrite a file and are safe to run every time; running one
when nothing changed is a no-op. This runner REGENERATES by default
rather than offering a check-only mode, on Tony's ruling of 2026-08-12:
"a regenerate step may be missed." A tool that reports a stale atlas
without fixing it has only added a step. The output files are
fingerprinted before and after, so the summary says which ones actually
moved -- that is the regenerate-then-read-back half, and it is there
because generated documents went stale four separate times in one
evening while nothing noticed.

CHECKERS report a problem and inform the push call. They run last so
their verdict is the last thing on screen.

Constants change runs first among them: it reads the git diff for
constants_new.py and reports any value that moved without its provenance
moving too. It replaced 55 hand-pinned literals on 2026-08-12 and stores
no numbers of its own.

The worksheet checker sits just above the scanner. It opens the worksheet
each cross-check annotation names and reports whether that worksheet
records the check the annotation claims. It is REPORT-ONLY: it exits 0
whatever it finds, and exits 1 only when it could not run. Its one
summary line carries a denominator, so the number moves when something
moves; findings go to WORKSHEET_CHECK.md.

The scanner stays LAST deliberately. Its Tier-1 count is the number the
push call turns on, and a report-only tool printing after it pushes that
number up the screen.

WHAT IS DELIBERATELY NOT HERE
-----------------------------
dep_trace.py takes a module name and answers a question BEFORE an edit.
Different job, stays out (L-188, 2026-08-07).

add_docstrings.py modifies SOURCE CODE rather than a generated
document. Nothing in an automatic routine should edit code.

measure_animation_html.py needs a file argument.

Gallery-repo tools live in the other repo and are not reached from here.

OUTPUT
------
One line per tool while it runs, then a summary table. A tool that fails
gets its full output printed under the table, so the console stays
readable when everything passes and tells you what happened when it does
not. Nothing is written to a log file: the console output is the
artifact, and it is short enough to copy.

GATING AND REPORT-ONLY
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
could not run, which is a failure and not a finding.

Role: devtool
Domain: dev_tools

Module created: August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import subprocess
import sys
import time

# ============================================================
# THE SUITE
# ============================================================

# (label, argv-tail, output files to fingerprint)
GENERATORS = [
    ('Ledger index',    ['ledger_index.py'],
     ['LEDGER_CONSOLIDATED.md']),
    ('Skill manifest',  ['skills_index.py', 'PROJECT_INSTRUCTIONS.md'],
     ['PROJECT_INSTRUCTIONS.md']),
    ('Module atlas',    ['module_atlas.py'],
     ['MODULE_ATLAS.md', 'MODULE_INDEX.md']),
    ('Data inventory',  ['data_inventory.py'],
     ['DATA_INVENTORY.md']),
]

# (label, argv-tail, verdict hint)
#
# The verdict hint names a substring; the first output line containing it
# becomes the summary note. Without one the last meaningful line is used,
# which is the right answer for a test file that ends in a pass/fail
# summary. The scanner needs a hint because it ends on an advisory banner
# rather than its verdict, and its Tier-1 count is the number the push
# call actually turns on.
CHECKERS = [
    ('Constants change', ['constants_change_report.py'], None),
    ('Constants relations', ['test_constants_provenance.py'], None),
    ('Cross-check annotations', ['test_cross_checked.py'], None),
    ('Citation inheritance', ['test_citation_inheritance.py'], None),
    ('Scanner recognition 1d/1e', ['test_provenance_1d.py'], None),
    ('Reset completeness', ['test_reset_completeness.py'],
     'RESET COMPLETENESS:'),
    ('Orbit cache', ['test_orbit_cache.py'], None),
    # A fourth field marks a tool REPORT-ONLY: it exits 0 whatever it
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
]

TOOL_TIMEOUT_SECONDS = 900


# ============================================================
# HELPERS
# ============================================================

def snapshot(path):
    """(mtime_ns, content hash) for a file, or (None, None) if absent.

    TWO facts, deliberately, because a generator can change one
    without the other. skills_index.py rewrites its manifest zone on
    every run whether or not the bytes move: the mtime advances, the
    hash does not. Windows Explorer shows the first and this runner
    used to report only the second, so a file could look new on disk
    while the screen said 'unchanged' and neither was wrong.

    The distinction is operational, not cosmetic. A real change to
    PROJECT_INSTRUCTIONS.md has to be re-uploaded to the Claude UI;
    a rewrite with identical bytes does not.

    The hash is LF-normalized because a CRLF working copy is not a
    content change -- the same reason the patch scripts fingerprint
    this way.
    """
    if not os.path.exists(path):
        return (None, None)
    mtime = os.stat(path).st_mtime_ns
    with open(path, 'rb') as handle:
        digest = hashlib.md5(
            handle.read().replace(b'\r\n', b'\n')).hexdigest()
    return (mtime, digest)


# ============================================================
# WHAT THE RUN WROTE (L-212)
# ============================================================
#
# The generators declare their outputs and their rows name them. The
# checkers declare nothing, and they write five artifacts between
# them, so a run could rewrite WORKSHEET_CHECK.md, the routing file,
# the citation prompt, PROVENANCE_AUDIT.md and the history file with
# nothing on screen saying so. Tony asked for the missing names.
#
# MEASURED, NOT DECLARED. The obvious fix is an output list per
# checker, matching the generators. That is a second store of a fact
# the tools already own, and it drifts in one direction only: the next
# artifact added is invisible again, and nothing fails to report it.
# Snapshotting the tree instead means a file written by a tool nobody
# declared still appears.
#
# The cost was measured before the design was chosen. A stat walk over
# 1,329 files is about 0.01 s; hashing everything at or under the size
# limit is about 0.13 s. Two snapshots cost roughly a third of a
# second against a run of 100 seconds or more.
#
# THE BLIND SPOT ANNOUNCES ITSELF. Fourteen files exceed the limit --
# bulk climate and ocean data, 218 MB of it -- and are compared by
# size and mtime rather than content, so a same-size edit to one of
# them would be reported as touched rather than written. The summary
# prints that count every run rather than hiding it.

# Files larger than this are compared by size and mtime, not content.
HASH_LIMIT_BYTES = 2 * 1024 * 1024

# Not part of the working tree for this purpose. .git is git's own
# business, __pycache__ is a build product of running the suite at all,
# and a virtualenv is not project state.
SKIP_DIRS = ('.git', '__pycache__', '.venv', 'venv', '.pytest_cache',
             'node_modules')


def tree_snapshot(project_dir):
    """{relative path: (mtime_ns, size, hash or None)} for the tree.

    The hash is LF-normalized, like every other fingerprint in this
    project, because a CRLF working copy is not a content change.
    """
    seen = {}
    for root, dirs, files in os.walk(project_dir):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            path = os.path.join(root, name)
            try:
                stat = os.stat(path)
            except OSError:
                continue
            digest = None
            if stat.st_size <= HASH_LIMIT_BYTES:
                try:
                    with open(path, 'rb') as handle:
                        digest = hashlib.md5(
                            handle.read().replace(b'\r\n', b'\n')
                        ).hexdigest()
                except OSError:
                    digest = None
            key = os.path.relpath(path, project_dir).replace(os.sep, '/')
            seen[key] = (stat.st_mtime_ns, stat.st_size, digest)
    return seen


def tree_diff(before, after):
    """(written, created, removed, touched, unhashed).

    `written` changed content. `touched` was rewritten with identical
    bytes, which matters operationally: a real change to
    PROJECT_INSTRUCTIONS.md has to be re-uploaded to the Claude UI and
    an identical rewrite does not. `unhashed` counts files too large to
    compare by content, so the reader knows what the answer does not
    cover.
    """
    written, created, removed, touched = [], [], [], []
    unhashed = 0
    for path, now in sorted(after.items()):
        if now[2] is None:
            unhashed += 1
        was = before.get(path)
        if was is None:
            created.append(path)
            continue
        if now[2] is not None and was[2] is not None:
            if now[2] != was[2]:
                written.append(path)
            elif now[0] != was[0]:
                touched.append(path)
        elif now[1] != was[1]:
            written.append(path)
        elif now[0] != was[0]:
            touched.append(path)
    for path in sorted(before):
        if path not in after:
            removed.append(path)
    return written, created, removed, touched, unhashed


def print_files_written(before, after):
    """Name every file the run changed. Printed on every run."""
    written, created, removed, touched, unhashed = tree_diff(
        before, after)

    print()
    print('FILES WRITTEN THIS RUN')
    print('-' * 70)
    # Success carries evidence: the count of files EXAMINED, not just
    # the count changed. "Nothing written" and "nothing looked at" are
    # the same sentence otherwise.
    print('  %d file(s) examined, %d written, %d created, %d removed, '
          '%d rewritten identically'
          % (len(after), len(written), len(created), len(removed),
             len(touched)))
    for label, paths in (('written', written), ('created', created),
                         ('removed', removed)):
        for path in paths:
            print('    %-9s %s' % (label, path))
    if touched:
        print('    rewritten with identical bytes, no action needed:')
        for path in touched:
            print('      %s' % path)
    if unhashed:
        print('    %d file(s) over %d MB compared by size and mtime '
              'only' % (unhashed, HASH_LIMIT_BYTES // (1024 * 1024)))
    if not (written or created or removed):
        print('    nothing changed on disk')


def last_meaningful_line(text):
    """The last non-blank, non-rule line -- a tool's verdict, usually."""
    for line in reversed((text or '').splitlines()):
        stripped = line.strip()
        if stripped and stripped.strip('=-_ '):
            return stripped
    return ''


def line_containing(text, hint):
    """First line carrying `hint`, or '' if none does."""
    for line in (text or '').splitlines():
        if hint in line:
            return line.strip()
    return ''


NOTE_WIDTH = 44
NOTE_INDENT = 37        # matches '  %-25s %6.1fs  ' below


def wrapped(text, width=NOTE_WIDTH):
    """The whole sentence across as many lines as it needs.

    A verdict is the one line of a tool's output anybody reads, so it
    does not get an ellipsis. A single token longer than the width --
    a file path, usually -- overhangs rather than being cut in half.
    """
    lines = []
    current = ''
    for word in (text or '').split():
        candidate = word if not current else current + ' ' + word
        if len(candidate) > width and current:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines or ['']


def print_row(label, seconds, note):
    """One tool's row: label, elapsed, and its verdict in full."""
    lines = wrapped(note)
    print('  %-25s %6.1fs  %s' % (label, seconds, lines[0]))
    for extra in lines[1:]:
        print(' ' * NOTE_INDENT + extra)


def fit(text, width=44):
    """Trim to width on a word boundary rather than mid-word."""
    text = ' '.join((text or '').split())
    if len(text) <= width:
        return text
    cut = text[:width - 3]
    if ' ' in cut:
        cut = cut[:cut.rfind(' ')]
    return cut + '...'


def run_tool(project_dir, argv_tail):
    """Run one tool with this interpreter. Returns (rc, output, seconds)."""
    started = time.time()
    try:
        completed = subprocess.run(
            [sys.executable] + argv_tail,
            cwd=project_dir,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=TOOL_TIMEOUT_SECONDS)
        output = completed.stdout.decode('utf-8', 'replace')
        return completed.returncode, output, time.time() - started
    except subprocess.TimeoutExpired:
        return (None, 'TIMEOUT after %d seconds.' % TOOL_TIMEOUT_SECONDS,
                time.time() - started)
    except OSError as exc:
        return None, 'could not start: %s' % exc, time.time() - started


def staleness_report(project_dir):
    """L-189's check, called here because the scanner cannot call it.

    A scanner that is running is by definition not stale, so this has to
    be read before the suite touches anything.
    """
    lines = []
    try:
        import provenance_history
    except ImportError as exc:
        return ['Staleness check unavailable: %s' % exc]
    try:
        history = provenance_history.load_history(project_dir)
        lines.extend(provenance_history.overdue_lines(history))
    except Exception as exc:                          # noqa: BLE001
        lines.append('Staleness check failed to read the history: %s' % exc)
    return lines


# ============================================================
# MAIN
# ============================================================

def main():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)

    print('=' * 70)
    print('MAINTENANCE RUN -- generators, then checkers (L-188)')
    print('=' * 70)

    # Bracketed around the whole suite, so the report covers every
    # tool rather than the ones that happened to declare an output.
    tree_before = tree_snapshot(project_dir)

    # ---- staleness first, before the suite makes it fresh ------------
    for line in staleness_report(project_dir):
        print('  ' + line)
    print()

    # (label, rc, seconds, note, output, is_checker[, report_only])
    # Checker rows carry the seventh field; generator rows stop at six.
    # Read it with a length guard, never by unpacking a fixed width.
    results = []

    # ---- generators ---------------------------------------------------
    print('GENERATORS -- regenerate every time; a no-op when nothing moved')
    print('-' * 70)
    for label, argv_tail, outputs in GENERATORS:
        before = dict((path, snapshot(path)) for path in outputs)
        rc, output, seconds = run_tool(project_dir, argv_tail)
        after = dict((path, snapshot(path)) for path in outputs)
        moved = [path for path in outputs
                 if before[path][1] != after[path][1]]
        written = [path for path in outputs
                   if before[path][0] != after[path][0]]
        if rc is None:
            note = 'DID NOT RUN'
        elif rc != 0:
            note = 'exit %d' % rc
        elif moved:
            note = 'rewrote ' + ', '.join(moved)
        elif written:
            note = ('unchanged (%d of %d rewritten, content identical)'
                    % (len(written), len(outputs)))
        else:
            note = ('unchanged (%d checked, not written)'
                    % len(outputs))
        print_row(label, seconds, note)
        results.append((label, rc, seconds, note, output, False))
    print()

    # ---- checkers -----------------------------------------------------
    print('CHECKERS -- verdict informs the push call')
    print('-' * 70)
    for entry in CHECKERS:
        label, argv_tail, hint = entry[0], entry[1], entry[2]
        report_only = entry[3] if len(entry) > 3 else False
        rc, output, seconds = run_tool(project_dir, argv_tail)
        verdict = line_containing(output, hint) if hint else ''
        # The row already carries the label; a verdict that opens by
        # repeating the hint spends the column on it twice. Stripped only
        # when the hint is a genuine prefix, so a hint matched mid-line
        # (the scanner's 'TIER-1 FINDINGS') is left exactly as printed.
        if hint and verdict.startswith(hint):
            verdict = verdict[len(hint):].strip()
        if rc is None:
            note = 'DID NOT RUN'
        elif rc == 0:
            note = (verdict or last_meaningful_line(output)) or 'passed'
        else:
            note = 'FAILED (exit %d)' % rc
            if verdict:
                note += ' -- ' + fit(verdict, 30)
        print_row(label, seconds, note)
        results.append((label, rc, seconds, note, output, True,
                        report_only))
    print()

    # ---- summary ------------------------------------------------------
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
    print('=' * 70)

    # ---- what the run wrote (L-212) -----------------------------------
    # After the verdict block, because the verdict is what the push
    # call turns on. Printed whether or not anything changed: a run
    # that wrote nothing should say so rather than leaving the reader
    # to infer it from an absence.
    print_files_written(tree_before, tree_snapshot(project_dir))

    # ---- detail for failures only -------------------------------------
    # Indexed rather than unpacked: checker rows carry a seventh field
    # and generator rows do not, so a fixed-width unpack here raises on
    # the first checker row. It compiled cleanly and died on the run --
    # the compiler cannot see a tuple width.
    for row in results:
        label, rc, note, output = row[0], row[1], row[3], row[4]
        if rc == 0:
            continue
        print()
        print('-' * 70)
        print('%s -- %s' % (label, note))
        print('-' * 70)
        print(output.rstrip())

    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
