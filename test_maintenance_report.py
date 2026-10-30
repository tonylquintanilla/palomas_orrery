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
summary to its last line, in four versions -- as printed (no file
rose), with one file risen (the shape provenance_history.console_lines
prints), with the run-history lines missing, and with one file risen
and Windows line endings, as the scanner's output reaches the runner on
Tony's machine. The output passes through the runner's real run_tool(),
with only the process call replaced, so the way the runner reads a
tool's output is tested too. It judges the printed summary with reading
of its own, sharing no code with the runner's.

Why the fourth (2026-10-14). The first three were all written with
plain line endings, and all passed. On Tony's machine every line the
scanner prints ends in a carriage return as well, and with a file risen
the summary said "Tier-1 rise: NOT READ" (his run record of 2026-10-13):
the reader's pattern stopped at the carriage return. A check fed only
the sandbox's line endings could not fail on that.

It first plants a fault for each thing it must catch, each put into a
copy of the real orrery_maintenance_run.py at the line it would live in,
and requires the right finding, by name:

    planted                                          must be caught as
    the summary no longer prints the rise lines      RISE LINE NOT PRINTED
    a risen file counted but not named               RISEN FILE NOT NAMED
    missing run-history lines passed over in         MISSING RISE NOT ANNOUNCED
      silence
    Windows line endings kept as they came           RISE NOT READ FROM
                                                     WINDOWS OUTPUT

And the night's gate (L-485), night_gate() and write_night_record() of
the real runner, run in a throwaway folder on eight cases: a clean
night, a failed night checker, a tool that could not reach JPL
(reported, not red: Tony's ruling R4), a tool that crashed, a file
changed outside the allow-list, a non-ASCII byte in an allowed file, a
night row no table carries, and the record a clean night writes. Six
faults are planted for it, each caught by name:

    a failed night checker let through               FAILED CHECKER PASSED
    an outage made red                               OUTAGE MADE RED
    a crashed night tool let through                 CRASHED TOOL PASSED
    the allow-list not applied                       OUTSIDE NOT REFUSED
    the ASCII test not applied                       NON-ASCII NOT REFUSED
    a night row no table carries dropped silently    UNKNOWN ROW DROPPED
                                                     SILENTLY

And the switch a night fired by hand may carry, --ask-everything
(L-485, 2026-10-30): with it the Horizons check runs with --all, without
it as by day, with its own time limit, longer than the runner's, since
it saves only at its end; and no other row of the night differs. Three
faults are planted for it, the switch in each direction and the limit:

    the switch dropped                               ASK EVERYTHING DROPPED
    the switch always on                             ASK EVERYTHING ALWAYS ON
    the time limit left off                          ASK EVERYTHING CUT SHORT

The last line starts "MAINTENANCE REPORT:", which the maintenance run
quotes, and says what was compared and how many things were examined.

Run (VS Code Run button, or):
    python test_maintenance_report.py

Runs nothing else and contacts nothing; the night's cases write only
to a throwaway folder.

Role: devtool
Domain: dev_tools

Module created: October 13, 2026 with Anthropic's Claude Opus 5.5 (L-269,
patch_L269_5_risen_files_20261013.py).
Module updated: October 14, 2026 with Anthropic's Claude Opus 5.5 (L-269,
patch_L269_6_windows_output_20261014.py: the summaries pass through the
runner's real run_tool(); a fourth summary, one file risen with Windows
line endings, and a fourth planted fault, the runner's line-ending fix
taken out.)
Module updated: October 30, 2026 with Anthropic's Claude Opus 5.5 (L-485,
the nightly run: the night's gate and record, eight cases and six planted
faults.)
Module updated: October 30, 2026 with Anthropic's Claude Opus 5.5 (L-485,
"ask JPL for everything": the night's rows with and without
--ask-everything and the Horizons check's time limit, two cases and
three planted faults.)
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

# What a Python program's print() puts on a pipe on Windows: every line
# ends in a carriage return and a newline.
WINDOWS = '\r\n'

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
    # Kept before summary_of() swaps the suite for one row: the switch's
    # cases read the night's real rows (L-485).
    mod.REAL_TABLES = (mod.GENERATORS, mod.CHECKERS)
    return mod


class _Completed(object):
    """What subprocess.run() hands back: the exit code and the bytes."""
    def __init__(self, stdout):
        self.returncode = 0
        self.stdout = stdout


def summary_of(mod, scanner_output, line_end='\n'):
    """What main() prints when its suite is the scanner alone and the
    scanner printed scanner_output, each line ending in line_end.
    The output reaches main() through the runner's own run_tool(); only
    the process call inside it is replaced. Nothing is run or written."""
    mod.GENERATORS = []
    mod.CHECKERS = [('Provenance scanner', ['provenance_scanner.py'],
                     ('GATE PATH:', 'Whole tree, Tier-1:'), True)]
    raw = scanner_output.replace('\n', line_end).encode('utf-8')
    real = mod.subprocess
    mod.subprocess = types.SimpleNamespace(
        run=lambda *args, **kwargs: _Completed(raw),
        DEVNULL=real.DEVNULL, PIPE=real.PIPE, STDOUT=real.STDOUT,
        TimeoutExpired=real.TimeoutExpired)
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

    s = summary_of(mod, WITH_RISE, line_end=WINDOWS)
    counts['summaries'] += 1
    flat = ' '.join(s.split())
    for fname, before, after in RISEN:
        counts['risen'] += 1
        if ('%s: %d -> %d' % (fname, before, after)) not in flat:
            findings.append(('RISE NOT READ FROM WINDOWS OUTPUT', 'with Windows '
                             'line endings the summary does not name %s, %d -> %d'
                             % (fname, before, after)))
    judge_night(mod, findings, counts)


# ============================================================================
# THE NIGHT'S GATE (L-485)
# ============================================================================
#
# The night run commits only on a clean night (Tony's ruling R1), and an
# outage is reported, not red (R4). night_gate() decides it; these cases
# call the runner's real night_gate() and write_night_record() in a
# throwaway folder, with git's list of changed files given, and judge
# the answer with reading of their own.

def _row(label, rc, note, is_checker):
    return (label, rc, 0.0, note, '', is_checker)


def judge_night(mod, findings, counts):
    import json
    import shutil
    import tempfile
    tmp = tempfile.mkdtemp(prefix='night_gate_')
    try:
        os.makedirs(os.path.join(tmp, 'data'))
        gens = [('Objects export', ['export_objects.py'],
                 ['data/objects_export.json'])]
        with open(os.path.join(tmp, 'data', 'objects_export.json'),
                  'wb') as f:
            f.write(b'{"ascii": true}\n')
        clean = [_row('Objects export', 0, 'unchanged', False),
                 _row('Objects export check', 0, 'pass', True)]

        def gate(results, changed):
            counts['night'] += 1
            return mod.night_gate(tmp, results, gens, changed=changed)

        problems, reported, inside = gate(clean, ['data/objects_export.json'])
        if problems or inside != ['data/objects_export.json']:
            findings.append(('CLEAN NIGHT REFUSED', 'a clean night with an '
                             'allowed file changed gave %s' % problems))
        problems, _r, _i = gate(
            clean[:1] + [_row('Objects export check', 1, 'FAILED', True)], [])
        if not any('Objects export check' in s for s in problems):
            findings.append(('FAILED CHECKER PASSED', 'a failed night checker '
                             'did not stop the night'))
        problems, reported, _i = gate(
            [_row('Horizons check', 1, 'exit 1 -- UNREACHABLE -- JPL could '
                  'not be reached', False)] + clean[1:], [])
        if problems or reported != ['Horizons check']:
            findings.append(('OUTAGE MADE RED', 'a tool that could not reach '
                             'JPL gave %s, reported %s' % (problems, reported)))
        problems, _r, _i = gate(
            [_row('Path plan', 1, 'exit 1 -- no summary line printed',
                  False)] + clean[1:], [])
        if not any('Path plan' in s for s in problems):
            findings.append(('CRASHED TOOL PASSED', 'a night tool that exited '
                             '1 without UNREACHABLE did not stop the night'))
        problems, _r, _i = gate(clean, ['celestial_objects.py'])
        if not any('celestial_objects.py' in s for s in problems):
            findings.append(('OUTSIDE NOT REFUSED', 'a changed file outside the '
                             'allow-list did not stop the night'))
        with open(os.path.join(tmp, 'data', 'objects_export.json'),
                  'wb') as f:
            f.write(b'{"name": "Cr\xc3\xa8me"}\n')
        problems, _r, _i = gate(clean, ['data/objects_export.json'])
        if not any('non-ASCII' in s for s in problems):
            findings.append(('NON-ASCII NOT REFUSED', 'an allowed file with a '
                             'non-ASCII byte did not stop the night'))
        real_rows = mod.NIGHT_ROWS
        mod.NIGHT_ROWS = real_rows + ('No such row',)
        counts['night'] += 1
        try:
            mod.night_rows()
            findings.append(('UNKNOWN ROW DROPPED SILENTLY', 'a night row no '
                             'table carries was not named'))
        except ValueError as ex:
            if 'No such row' not in str(ex):
                findings.append(('UNKNOWN ROW DROPPED SILENTLY', str(ex)))
        finally:
            mod.NIGHT_ROWS = real_rows
        # The switch a night fired by hand may carry (L-485, 2026-10-30):
        # with it the Horizons check is asked with --all, without it as
        # by day, and nothing else about the night differs.
        swapped = (mod.GENERATORS, mod.CHECKERS)
        mod.GENERATORS, mod.CHECKERS = mod.REAL_TABLES
        try:
            off = mod.night_rows()
            on = mod.night_rows(ask_everything=True)
        finally:
            mod.GENERATORS, mod.CHECKERS = swapped
        counts['night'] += 2

        def horizons_args(gens_):
            return [r[1] for r in gens_ if r[0] == 'Horizons check']

        if horizons_args(on[0]) != [['horizons_check.py', '--all']]:
            findings.append(('ASK EVERYTHING DROPPED', 'with the switch the '
                             'Horizons check runs as %s' % horizons_args(on[0])))
        if horizons_args(off[0]) != [['horizons_check.py']]:
            findings.append(('ASK EVERYTHING ALWAYS ON', 'without the switch '
                             'the Horizons check runs as %s'
                             % horizons_args(off[0])))
        limits = [r[4] if len(r) > 4 else None
                  for r in on[0] if r[0] == 'Horizons check']
        if limits != [mod.ASK_EVERYTHING_SECONDS] or not (
                mod.ASK_EVERYTHING_SECONDS > mod.TOOL_TIMEOUT_SECONDS):
            findings.append(('ASK EVERYTHING CUT SHORT', 'with the switch the '
                             'Horizons check may take %s seconds, against the '
                             "runner's %d" % (limits, mod.TOOL_TIMEOUT_SECONDS)))
        rest_on = [r for r in on[0] if r[0] != 'Horizons check']
        rest_off = [r for r in off[0] if r[0] != 'Horizons check']
        if rest_on != rest_off or on[1:] != off[1:]:
            findings.append(('ASK EVERYTHING CHANGED MORE', 'the switch '
                             'changed a row other than the Horizons check'))
        mod.write_night_record(tmp, clean, [('Ledger index', 'a document')],
                               [])
        counts['night'] += 1
        raw = open(os.path.join(tmp, mod.NIGHT_RECORD), 'rb').read()
        body = json.loads(raw.decode('ascii'))
        if (any(b > 127 for b in raw) or b'\r' in raw
                or not body.get('clean_run_utc', '').endswith('+00:00')
                or [r['row'] for r in body['rows']] != [c[0] for c in clean]):
            findings.append(('RECORD WRONG', 'the night record is not ASCII and '
                             'LF, or lacks its UTC stamp or its rows'))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


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
    ('Windows line endings kept as they came',
     ("        output = output.replace('\\r\\n', '\\n')\n",
      "        pass\n"),
     'RISE NOT READ FROM WINDOWS OUTPUT'),
    # L-485, the night's gate
    ('a failed night checker let through',
     ("            problems.append('%s failed' % label)\n",
      "            pass\n"),
     'FAILED CHECKER PASSED'),
    ('an outage made red',
     ("        elif not is_checker and NIGHT_UNREACHABLE in note:\n",
      "        elif False:\n"),
     'OUTAGE MADE RED'),
    ('a crashed night tool let through',
     ("            problems.append('%s exited %d' % (label, rc))\n",
      "            pass\n"),
     'CRASHED TOOL PASSED'),
    ('the allow-list not applied',
     ("            problems.append('changed outside the allow-list: %s' % path)\n",
      "            pass\n"),
     'OUTSIDE NOT REFUSED'),
    ('the ASCII test not applied',
     ("        if bad:\n",
      "        if False:\n"),
     'NON-ASCII NOT REFUSED'),
    ('a night row no table carries dropped silently',
     ("    if unknown:\n        raise ValueError(",
      "    if False:\n        raise ValueError("),
     'UNKNOWN ROW DROPPED SILENTLY'),
    # L-485, the switch a night fired by hand may carry
    ('the ask-everything switch dropped',
     ("            if ask_everything and row[0] in ASK_EVERYTHING_ARGS:\n",
      "            if False:\n"),
     'ASK EVERYTHING DROPPED'),
    ('the ask-everything switch always on',
     ("            if ask_everything and row[0] in ASK_EVERYTHING_ARGS:\n",
      "            if row[0] in ASK_EVERYTHING_ARGS:\n"),
     'ASK EVERYTHING ALWAYS ON'),
    ('the ask-everything time limit left off',
     ("                       + (ASK_EVERYTHING_SECONDS,))\n",
      "                       )\n"),
     'ASK EVERYTHING CUT SHORT'),
]


def main():
    problems = []
    for label, (old, new), expected in PLANTS:
        findings, counts = [], {'summaries': 0, 'risen': 0, 'night': 0}
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

    findings, counts = [], {'summaries': 0, 'risen': 0, 'night': 0}
    judge(load(), findings, counts)
    for cls, detail in findings:
        print('FAIL: %s -- %s' % (cls, detail))
        problems.append('%s -- %s' % (cls, detail))
    print("compared: the maintenance run's printed summary against the scanner output "
          "recorded here -- the sentence that no file rose, the risen file by name with "
          "its before and after, the sentence when the run history is missing, and the "
          "risen file again when the output has Windows line endings; and the "
          "night's gate (L-485) on clean, failed, unreached, crashed, outside "
          "the allow-list and non-ASCII nights, an unknown night row, the "
          "Horizons check's arguments with and without --ask-everything, and "
          "the night's record")
    print('examined: four summaries (as printed at ab96681, with one file risen, with '
          'no run history, with one file risen and Windows line endings) from the real '
          'main() and run_tool() of orrery_maintenance_run.py')
    if problems:
        print('MAINTENANCE REPORT: FAIL -- %d problem(s)' % len(problems))
        return 1
    print('MAINTENANCE REPORT: PASS -- %d of %d planted faults caught by name; %d summaries; '
          '%d risen file(s) named; %d night-gate cases' % (
              len(PLANTS), len(PLANTS), counts['summaries'], counts['risen'],
              counts['night']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
