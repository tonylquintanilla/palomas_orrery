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

EXIT CODE
---------
0 when every checker passed, 1 when any failed. The generators do not
affect it -- a regenerated file is the normal case, not a problem.

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
    ('Provenance 1d/1e', ['test_provenance_1d.py'], None),
    ('Reset completeness', ['test_reset_completeness.py'], None),
    ('Orbit cache', ['test_orbit_cache.py'], None),
    ('Worksheet checker', ['worksheet_checker.py'], 'WORKSHEET CHECK:'),
    ('Worksheet checker tests', ['test_worksheet_checker.py'], None),
    ('Worksheet key round trip', ['test_worksheet_keys.py'], None),
    ('Extractor pins', ['test_extractor_pins.py'], None),
    ('Provenance scanner', ['provenance_scanner.py'], 'TIER-1 FINDINGS'),
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

    # ---- staleness first, before the suite makes it fresh ------------
    for line in staleness_report(project_dir):
        print('  ' + line)
    print()

    results = []      # (label, rc, seconds, note, output)

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
        print('  %-24s %6.1fs  %s' % (label, seconds, note))
        results.append((label, rc, seconds, note, output, False))
    print()

    # ---- checkers -----------------------------------------------------
    print('CHECKERS -- verdict informs the push call')
    print('-' * 70)
    for label, argv_tail, hint in CHECKERS:
        rc, output, seconds = run_tool(project_dir, argv_tail)
        verdict = line_containing(output, hint) if hint else ''
        if rc is None:
            note = 'DID NOT RUN'
        elif rc == 0:
            note = fit(verdict or last_meaningful_line(output)) or 'passed'
        else:
            note = 'FAILED (exit %d)' % rc
            if verdict:
                note += ' -- ' + fit(verdict, 30)
        print('  %-24s %6.1fs  %s' % (label, seconds, note))
        results.append((label, rc, seconds, note, output, True))
    print()

    # ---- summary ------------------------------------------------------
    failed = [row for row in results if row[5] and row[1] != 0]
    total = sum(row[2] for row in results)

    print('=' * 70)
    if failed:
        print('  %d of %d checkers FAILED -- %.1fs total'
              % (len(failed), len(CHECKERS), total))
        print('  ' + ', '.join(row[0] for row in failed))
    else:
        print('  All %d checkers passed -- %.1fs total' % (len(CHECKERS), total))
    print('=' * 70)

    # ---- detail for failures only -------------------------------------
    for label, rc, seconds, note, output, is_checker in results:
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
