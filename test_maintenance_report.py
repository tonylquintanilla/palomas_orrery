"""
test_maintenance_report.py - the maintenance run's summary names every
file whose Tier-1 rose since the scanner's previous run; and proof that
this check can fail.

L-269 (a report names its items). Tony's run record of 2026-10-13: "i
was expecting the module class breakdown." L-437 put the whole-tree
split on the scanner's row; the files whose Tier-1 rose still printed
only on the scanner's own screen, which the maintenance run captures and
does not show. A session had told Tony to expect "Tier-1 rose" in
patch_L436_1 while it sat in the root folder; that line never reached
him.

This file runs the runner's real main() with its suite replaced by one
row, the scanner, whose output is RECORDED here rather than run: the
scanner's console at orrery ab96681 (2026-10-13), from its priority
summary to its last line, in three versions -- as printed (no file
rose), with one file risen (the shape provenance_history.console_lines
prints), and with the run-history lines missing. It judges the printed
summary with reading of its own, sharing no code with the runner's.

It first plants a fault for each thing it must catch, each put into a
copy of the real orrery_maintenance_run.py at the line it would live in,
and requires the right finding, by name:

    planted                                          must be caught as
    the summary no longer prints the rise lines      RISE LINE NOT PRINTED
    a risen file counted but not named               RISEN FILE NOT NAMED
    missing run-history lines passed over in         MISSING RISE NOT ANNOUNCED
      silence

The last line starts "MAINTENANCE REPORT:", which the maintenance run
quotes, and says what was compared and how many things were examined.

Run (VS Code Run button, or):
    python test_maintenance_report.py

Runs nothing else and contacts nothing.

Role: devtool
Domain: dev_tools

Module created: October 13, 2026 with Anthropic's Claude Opus 5.5 (L-269,
patch_L269_5_risen_files_20261013.py).
"""
import contextlib
import io
import os
import sys
import types

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

# ============================================================================
# THE RECORDED SCANNER OUTPUT (orrery ab96681, 2026-10-13)
# ============================================================================

AS_PRINTED = "Priority summary:\n  Tier 1 (16-20):   280 findings -- FIX NOW\n      earth_science     149\n      orrery            116\n      stars              13\n      utilities           2\n  Tier 2 (10-15):   684 findings -- REVIEW\n      orrery            567\n      earth_science      75\n      stars              41\n      unclassified        1\n  Tier 3 (5-9):   145 findings -- LOW PRIORITY\n      dev_tools          84\n      orrery             53\n      stars               6\n      earth_science       2\n  Tier 4 (1-4):     6 findings -- LOWEST PRIORITY\n      orrery              3\n      stars               3\n\nRun history (data/provenance_history.json):\n  previous run 20261014T034203Z (under an hour earlier, HEAD 869b8c2)\n  delta   total +0   T1 +0   T2 +0   T3 +0   T4 +0\n  no file's Tier-1 count rose.\n  Tier-1 by domain: orrery 116, Earth System 149, stars 13, utilities 2\n  no domain's Tier-1 count moved.\n  gate path: the same 0 Tier-1 finding(s) by name as the previous run.\n\n======================================================================\n  GATE PATH: 0 TIER-1 -- the push gate holds\n\n  Examined: 102 of 127 exported rows (constants_export.json),\n  25 more computed from other rows, whose inputs are scored;\n  0 display string(s) in 13 served object(s) (objects_export.json).\n\n  Whole tree, Tier-1: 280: orrery 116, Earth System 149, stars 13, utilities 2.\n  Informational; the gate is the GATE PATH line above.\n  Nothing here sets the exit code.\n======================================================================\n"

RISEN = [('patch_L436_1_idea_20261013.py', 0, 1)]
WITH_RISE = AS_PRINTED.replace(
    "  no file's Tier-1 count rose.\n",
    "  Tier-1 ROSE in 1 file(s):\n"
    "      patch_L436_1_idea_20261013.py                0 -> 1  (+1)\n")
NO_HISTORY = AS_PRINTED[:AS_PRINTED.index('Run history')] + \
    AS_PRINTED[AS_PRINTED.index('====='):]

# ============================================================================
# RUNNING THE REAL SUMMARY
# ============================================================================

def load(old=None, new=None):
    """The runner, real or with one line changed. The anchor must be found
    exactly once, or the plant fails loudly rather than testing nothing."""
    path = os.path.join(HERE, 'orrery_maintenance_run.py')
    with open(path, encoding='utf-8') as f:
        src = f.read()
    if old is not None:
        n = src.count(old)
        if n != 1:
            raise RuntimeError('PLANT ANCHOR: %r found %d times' % (old[:60], n))
        src = src.replace(old, new)
    mod = types.ModuleType('orrery_maintenance_run_under_test')
    mod.__file__ = path
    exec(compile(src, path, 'exec'), mod.__dict__)
    return mod


def summary_of(mod, scanner_output):
    """What main() prints when its suite is the scanner alone and the
    scanner printed scanner_output. Nothing is run or written."""
    mod.GENERATORS = []
    mod.CHECKERS = [('Provenance scanner', ['provenance_scanner.py'],
                     ('GATE PATH:', 'Whole tree, Tier-1:'), True)]
    mod.run_tool = lambda project_dir, argv_tail: (0, scanner_output, 0.1)
    mod.tree_snapshot = lambda project_dir: {}
    mod.print_files_written = lambda before, after: None
    mod.staleness_report = lambda project_dir: []
    here = os.getcwd()
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            mod.main()
    finally:
        os.chdir(here)
    text = buf.getvalue()
    # Only the summary block: from the gating headline to its closing rule.
    start = text.index('gating checkers passed')
    return text[start:text.index('=' * 70, start)]


# ============================================================================
# THE JUDGES
# ============================================================================

def judge(mod, findings, counts):
    s = summary_of(mod, AS_PRINTED)
    counts['summaries'] += 1
    flat = ' '.join(s.split())
    if "No file's Tier-1 count rose since the previous run" not in flat:
        findings.append(('RISE LINE NOT PRINTED', 'the summary does not say that no '
                         "file's Tier-1 rose, which the scanner printed"))

    s = summary_of(mod, WITH_RISE)
    counts['summaries'] += 1
    flat = ' '.join(s.split())
    if 'Tier-1 rose since the previous run in %d file(s)' % len(RISEN) not in flat:
        findings.append(('RISE LINE NOT PRINTED', 'the summary does not say that %d '
                         "file's Tier-1 rose" % len(RISEN)))
    for fname, before, after in RISEN:
        counts['risen'] += 1
        if ('%s: %d -> %d' % (fname, before, after)) not in flat:
            findings.append(('RISEN FILE NOT NAMED', 'the summary does not name %s, '
                             '%d -> %d' % (fname, before, after)))

    s = summary_of(mod, NO_HISTORY)
    counts['summaries'] += 1
    flat = ' '.join(s.split())
    if 'Tier-1 rise: NOT READ' not in flat:
        findings.append(('MISSING RISE NOT ANNOUNCED', 'the scanner printed no run '
                         'history and the runner did not say so'))


PLANTS = [
    ('the summary no longer prints the rise lines',
     ('                for line in scanner_risen_lines(row[4]):\n',
      '                for line in []:\n'),
     'RISE LINE NOT PRINTED'),
    ('a risen file counted but not named',
     ("            lines.append('- %s: %s -> %s' % (fname, before, after))\n",
      '            pass\n'),
     'RISEN FILE NOT NAMED'),
    ('missing run-history lines passed over in silence',
     ("    return ['Tier-1 rise: NOT READ -- the scanner printed neither '\n",
      "    return []\n    return ['Tier-1 rise: NOT READ -- the scanner printed neither '\n"),
     'MISSING RISE NOT ANNOUNCED'),
]


def main():
    problems = []
    for label, (old, new), expected in PLANTS:
        findings, counts = [], {'summaries': 0, 'risen': 0}
        try:
            judge(load(old, new), findings, counts)
        except RuntimeError as ex:
            print('planted: %-52s COULD NOT BE PLANTED: %s' % (label, ex))
            problems.append('plant failed: %s' % label)
            continue
        hits = [d for c, d in findings if c == expected]
        if hits:
            print('planted: %-52s caught as %s (%s)' % (label, expected, hits[0]))
        else:
            print('planted: %-52s NOT CAUGHT; findings: %s'
                  % (label, sorted(set(c for c, _ in findings)) or 'none'))
            problems.append('planted fault not caught: %s' % label)

    findings, counts = [], {'summaries': 0, 'risen': 0}
    judge(load(), findings, counts)
    for cls, detail in findings:
        print('FAIL: %s -- %s' % (cls, detail))
        problems.append('%s -- %s' % (cls, detail))
    print("compared: the maintenance run's printed summary against the scanner output "
          "recorded here -- the sentence that no file rose, the risen file by name with "
          "its before and after, and the sentence when the run history is missing")
    print('examined: three summaries (as printed at ab96681, with one file risen, with '
          'no run history) from the real main() of orrery_maintenance_run.py')
    if problems:
        print('MAINTENANCE REPORT: FAIL -- %d problem(s)' % len(problems))
        return 1
    print('MAINTENANCE REPORT: PASS -- %d of %d planted faults caught by name; %d summaries; '
          '%d risen file(s) named' % (len(PLANTS), len(PLANTS), counts['summaries'],
                                      counts['risen']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
