"""patch_L269_5_risen_files_20261013.py -- L-269 (a report names
its items): the maintenance run's summary names, under the provenance
scanner's verdict, every file whose Tier-1 rose since the scanner's
previous run. Redelivered on top of L-437, which already prints the
whole-tree split; patch_L269_1_scanner_breakdown_20261013.py is
superseded and is deleted.

Built on orrery ab9668145700d7f83d22206fd6c26a70864fd4dd at
https://github.com/tonylquintanilla/palomas_orrery ("L431 close").
The gallery is not touched.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\;
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\.
Written October 13, 2026 with Anthropic's Claude Opus 5.5.
Record: documentation/HANDOFF_L269_risen_files_20261013.md
(created by this patch).

HOW TO RUN
    From the orrery repo's ROOT folder: open this file in VS Code and
    press Run, or from a terminal in that folder:
        python patch_L269_5_risen_files_20261013.py
    Success prints one "ok" line per edit, then "patch applied". It asks
    nothing and fetches nothing.

WHAT IT CHANGES
    orrery_maintenance_run.py: scanner_risen_lines(); the summary names
      the risen files under the scanner's verdict, or says none rose, or
      says NOT READ; CHECKERS gains Maintenance report (L-269); GATING
      AND REPORT-ONLY no longer names a count, which had fallen behind.
    palomas_orrery_dashboard.py: the "Maintenance Report" button.
    Created: test_maintenance_report.py; the handoff.
    LEDGER_CONSOLIDATED.md (L-269, the stamp); documentation/
      WHERE_WE_ARE.md, by section, never below the run-record marker.
    No skill or protocol version changes.

SAFETY
    Each file is checked only at the lines this patch edits: every anchor
    must match exactly once, and no edit lands below the run-record
    marker, so your notes cannot make it refuse. A file this patch
    creates must not exist yet. If any check fails, NOTHING is written.
    A file found with Windows line endings is matched after turning them
    into LF and written back LF, and the patch says so. Undo after a run
    is Discard Changes in GitHub Desktop, and delete the created files.
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
MARKER = '--- Your run record below this line'

EDITS = [
    ('orrery_maintenance_run.py', 'line 88: GATING AND REPORT-ONLY',
     "GATING AND REPORT-ONLY\n----------------------\nTwenty-five checkers are pass/fail: a problem makes them exit non-zero.\nTwo are REPORT-ONLY -- worksheet_checker.py and provenance_scanner.py\nexit 0 whatever they find, and exit 1 only when they could not run.\nThey are marked in the CHECKERS table, and the summary counts the\ngating twenty-five in its headline and quotes the two report-only verdicts\nunderneath.\n\nThe block quotes each tool's own note rather than restating it. A\n",
     "GATING AND REPORT-ONLY\n----------------------\nEvery checker is pass/fail unless the CHECKERS table marks it\nREPORT-ONLY: a problem makes it exit non-zero. Two are REPORT-ONLY --\nworksheet_checker.py and provenance_scanner.py exit 0 whatever they find,\nand exit 1 only when they could not run. The summary counts the gating\ncheckers in its headline, from the table itself, and quotes the two\nreport-only verdicts underneath. (This paragraph named the count until\n2026-10-13; three sessions added rows that day and it fell behind, so\nthe number now lives only where the run counts it.)\n\nUnder the scanner's verdict the summary also names every file whose\nTier-1 rose since the scanner's previous run, read from the scanner's\nown output; when it cannot read that, it says so (L-269).\n\nThe block quotes each tool's own note rather than restating it. A\n"),
    ('orrery_maintenance_run.py', 'line 197: the dashboard-labels and L-425 patches also ',
     'the dashboard-labels and L-425 patches also add rows beside this one,\nand the patch that runs last restates it.)\n"""\n\nimport hashlib\nimport os\nimport subprocess\nimport sys\n',
     'the dashboard-labels and L-425 patches also add rows beside this one,\nand the patch that runs last restates it.)\nModule updated: October 13, 2026 with Anthropic\'s Claude Opus 5.5 (L-269,\npatch_L269_5_risen_files_20261013.py, Tony\'s run record of the same\nday: the summary names, under the scanner\'s verdict, each file whose\nTier-1 rose since the scanner\'s previous run, read from the scanner\'s\noutput by scanner_risen_lines(), and says NOT READ when it cannot. The\nwhole-tree split is L-437\'s and is not repeated. CHECKERS gains\nMaintenance report (L-269), test_maintenance_report.py, three faults\nplanted in copies of this file, each caught by name. GATING AND\nREPORT-ONLY no longer names a count: the headline counts from the\ntable, and the paragraph\'s number had fallen behind.)\n"""\n\nimport hashlib\nimport os\nimport re\nimport subprocess\nimport sys\n'),
    ('orrery_maintenance_run.py', 'line 354: # the run history; six faults planted, each ',
     '    # the run history; six faults planted, each caught by name.\n    (\'Domain Split\', [\'test_domain_split.py\'], \'DOMAIN SPLIT:\'),\n    # A fourth field marks a tool REPORT-ONLY: it exits 0 whatever it\n    # finds, so "passed" says only that it ran. Exactly two are, and\n',
     '    # the run history; six faults planted, each caught by name.\n    (\'Domain Split\', [\'test_domain_split.py\'], \'DOMAIN SPLIT:\'),\n    # L-269, 2026-10-13: this runner\'s summary names each file whose\n    # Tier-1 rose since the scanner\'s previous run; three faults planted\n    # first in copies of this file, each caught by name.\n    (\'Maintenance report (L-269)\', [\'test_maintenance_report.py\'],\n     \'MAINTENANCE REPORT:\'),\n    # A fourth field marks a tool REPORT-ONLY: it exits 0 whatever it\n    # finds, so "passed" says only that it ran. Exactly two are, and\n'),
    ('orrery_maintenance_run.py', 'line 564: NOTE_WIDTH = 44',
     "NOTE_WIDTH = 44\nNOTE_INDENT = 37        # matches '  %-25s %6.1fs  ' below\n\n\n",
     'NOTE_WIDTH = 44\nNOTE_INDENT = 37        # matches \'  %-25s %6.1fs  \' below\n\n\ndef scanner_risen_lines(output):\n    """\n    The files whose Tier-1 rose since the scanner\'s previous run, read\n    from its own run-history lines (L-269). The summary otherwise quotes\n    the GATE PATH line and the whole-tree split (L-437) and nothing\n    else, so a rise printed only on the scanner\'s screen, which this\n    runner captures and does not show. Read, never recomputed, so it\n    cannot drift from what the scanner printed; what cannot be read is\n    said, not dropped.\n    """\n    if re.search(r"no file\'s Tier-1 count rose", output):\n        return ["No file\'s Tier-1 count rose since the previous run."]\n    r = re.search(r\'Tier-1 ROSE in (\\d+) file\\(s\\):[ \\t]*\\n((?:[ \\t]+\\S+[ \\t]+\\d+ -> \\d+.*\\n?)*)\',\n                  output)\n    if r:\n        lines = [\'Tier-1 rose since the previous run in %s file(s):\' % r.group(1)]\n        for fname, before, after in re.findall(r\'(\\S+)[ \\t]+(\\d+) -> (\\d+)\', r.group(2)):\n            lines.append(\'- %s: %s -> %s\' % (fname, before, after))\n        return lines\n    if \'first recorded run\' in output:\n        return [\'Tier-1 rise: first recorded run, nothing to compare with.\']\n    return [\'Tier-1 rise: NOT READ -- the scanner printed neither \'\n            \'"no file\\\'s Tier-1 count rose" nor "Tier-1 ROSE in"\']\n\n\n'),
    ('orrery_maintenance_run.py', 'line 810: for row in report_only:',
     "        for row in report_only:\n            print('    %-27s %s' % (row[0], row[3]))\n    print('=' * 70)\n\n",
     "        for row in report_only:\n            print('    %-27s %s' % (row[0], row[3]))\n            # L-269: under the scanner's verdict, each file whose Tier-1\n            # rose since its previous run, read from its own output.\n            if row[0] == 'Provenance scanner' and row[1] is not None:\n                for line in scanner_risen_lines(row[4]):\n                    for piece in wrapped(line, 62):\n                        print('      ' + piece)\n    print('=' * 70)\n\n"),
    ('palomas_orrery_dashboard.py', 'line 199: button is named what the run prints). It sit',
     'button is named what the run prints). It sits before Drawings Export,\nits alphabetical place once the labels lose "Test".\n"""\n\n',
     'button is named what the run prints). It sits before Drawings Export,\nits alphabetical place once the labels lose "Test".\nOctober 13, 2026 with Anthropic\'s Claude Opus 5.5 (L-269): Maintenance\nReport under the orrery\'s checkers, in the same patch as its checker\ntest_maintenance_report.py, with the same name as its maintenance-run\nrow. It sits before Test Objects Export, its alphabetical place once\nthe labels lose "Test".\n"""\n\n'),
    ('palomas_orrery_dashboard.py', 'line 1238: "tilt pushed to 60 degrees) and each must be',
     '         "tilt pushed to 60 degrees) and each must be caught, then the real "\n         "rows must pass. Ends on \\"HILLS CLOUD: PASS\\" (L-421).",\n         SCRIPT_DIR,\n         True,\n',
     '         "tilt pushed to 60 degrees) and each must be caught, then the real "\n         "rows must pass. Ends on \\"HILLS CLOUD: PASS\\" (L-421).",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Maintenance Report",\n         "test_maintenance_report.py",\n         "Check that the maintenance run\'s summary names, under the "\n         "provenance scanner\'s verdict, every file whose Tier-1 count rose "\n         "since the scanner\'s previous run, and says so when it cannot read "\n         "that. Runs the run\'s real summary on recorded scanner output. Three "\n         "faults are planted first, each in a copy of the real code, and each "\n         "must be caught by name. "\n         "Ends on \\"MAINTENANCE REPORT: PASS\\" (L-269).",\n         SCRIPT_DIR,\n         True,\n'),
    ('LEDGER_CONSOLIDATED.md', 'line 398: Module updated: October 13, 2026 with Anthro',
     'build 3 briefed), built on 869b8c22.\nReview and RICE update Tony 6-21-2026\n',
     "build 3 briefed), built on 869b8c22.\nModule updated: October 13, 2026 with Anthropic's Claude Opus 5.5\n(L-269: the maintenance run's summary names the files whose Tier-1\nrose), built on ab96681.\nReview and RICE update Tony 6-21-2026\n"),
    ('LEDGER_CONSOLIDATED.md', 'line 8547: <!-- L:269 status:OPEN upd:2026-10-13 sectio',
     '<!-- L:269 status:OPEN upd:2026-08-30 section:A flag: rice:5/4/90/3 -->\n',
     '<!-- L:269 status:OPEN upd:2026-10-13 section:A flag: rice:5/4/90/3 -->\n'),
    ('LEDGER_CONSOLIDATED.md', 'line 8715: - **2026-10-13, redelivered as `patch_L269_5',
     '  has twenty-six gating checkers since L-437.\n\n',
     '  has twenty-six gating checkers since L-437.\n- **2026-10-13, redelivered as `patch_L269_5_risen_files_20261013.py`**,\n  cut on ab96681 after L-431\'s close, as the coordination session\n  ordered ("drop the breakdown half, keep the half that names each file\n  whose count rose, one patch, planted faults shown caught"). Tony\'s\n  request that started it, in his run record: "i was expecting the\n  module class breakdown." L-437 answered the breakdown; this answers\n  the rest. Under the scanner\'s verdict the summary now names each file\n  whose Tier-1 rose since the scanner\'s previous run, read from its own\n  run-history lines, or says that none rose, or says NOT READ.\n  `scanner_risen_lines()` in `orrery_maintenance_run.py`; new checker\n  `test_maintenance_report.py`, "Maintenance report (L-269)" in the run\n  and "Maintenance Report" on the dashboard, three faults planted in\n  copies of the runner, each caught by name. GATING AND REPORT-ONLY no\n  longer names a count: the headline counts from the table, and three\n  sessions adding rows on one day left the typed number behind. The old\n  `patch_L269_1_scanner_breakdown_20261013.py` in the root folder is\n  superseded and is deleted, not filed: its name repeats an older\n  patch\'s in documentation/.\n\n'),
    ('documentation/WHERE_WE_ARE.md', 'line 4: Last updated: October 13, 2026, night: the m',
     "Last updated: October 13, 2026, night: orbital periods' build 2 closed.\n- Written at orrery 869b8c22 and gallery 924977a3.\n",
     'Last updated: October 13, 2026, night: the maintenance run names risen files.\n- Written at orrery ab96681 and gallery 924977a3.\n'),
    ('documentation/WHERE_WE_ARE.md', "line 11: > - The maintenance run's summary names any ",
     '>   at your look and closed; all four fixes from your plot are in.\n>\n',
     ">   at your look and closed; all four fixes from your plot are in.\n> - The maintenance run's summary names any file whose count of\n>   problems to fix now (Tier-1) rose since the last run.\n>\n"),
    ('documentation/WHERE_WE_ARE.md', 'line 19: > - *Run patch_L269_5 and the maintenance ru',
     '> - *Run patch_L431_9 and the maintenance run; move the patch into\n>   documentation/; push.*\n',
     '> - *Run patch_L269_5 and the maintenance run; delete the old\n>   patch_L269_1; move the new one and patch_L431_9 into documentation/;\n>   push.*\n'),
]

CREATED = {
    'test_maintenance_report.py': '"""\ntest_maintenance_report.py - the maintenance run\'s summary names every\nfile whose Tier-1 rose since the scanner\'s previous run; and proof that\nthis check can fail.\n\nL-269 (a report names its items). Tony\'s run record of 2026-10-13: "i\nwas expecting the module class breakdown." L-437 put the whole-tree\nsplit on the scanner\'s row; the files whose Tier-1 rose still printed\nonly on the scanner\'s own screen, which the maintenance run captures and\ndoes not show. A session had told Tony to expect "Tier-1 rose" in\npatch_L436_1 while it sat in the root folder; that line never reached\nhim.\n\nThis file runs the runner\'s real main() with its suite replaced by one\nrow, the scanner, whose output is RECORDED here rather than run: the\nscanner\'s console at orrery ab96681 (2026-10-13), from its priority\nsummary to its last line, in three versions -- as printed (no file\nrose), with one file risen (the shape provenance_history.console_lines\nprints), and with the run-history lines missing. It judges the printed\nsummary with reading of its own, sharing no code with the runner\'s.\n\nIt first plants a fault for each thing it must catch, each put into a\ncopy of the real orrery_maintenance_run.py at the line it would live in,\nand requires the right finding, by name:\n\n    planted                                          must be caught as\n    the summary no longer prints the rise lines      RISE LINE NOT PRINTED\n    a risen file counted but not named               RISEN FILE NOT NAMED\n    missing run-history lines passed over in         MISSING RISE NOT ANNOUNCED\n      silence\n\nThe last line starts "MAINTENANCE REPORT:", which the maintenance run\nquotes, and says what was compared and how many things were examined.\n\nRun (VS Code Run button, or):\n    python test_maintenance_report.py\n\nRuns nothing else and contacts nothing.\n\nRole: devtool\nDomain: dev_tools\n\nModule created: October 13, 2026 with Anthropic\'s Claude Opus 5.5 (L-269,\npatch_L269_5_risen_files_20261013.py).\n"""\nimport contextlib\nimport io\nimport os\nimport sys\nimport types\n\nHERE = os.path.dirname(os.path.abspath(__file__))\nif HERE not in sys.path:\n    sys.path.insert(0, HERE)\n\n# ============================================================================\n# THE RECORDED SCANNER OUTPUT (orrery ab96681, 2026-10-13)\n# ============================================================================\n\nAS_PRINTED = "Priority summary:\\n  Tier 1 (16-20):   280 findings -- FIX NOW\\n      earth_science     149\\n      orrery            116\\n      stars              13\\n      utilities           2\\n  Tier 2 (10-15):   684 findings -- REVIEW\\n      orrery            567\\n      earth_science      75\\n      stars              41\\n      unclassified        1\\n  Tier 3 (5-9):   145 findings -- LOW PRIORITY\\n      dev_tools          84\\n      orrery             53\\n      stars               6\\n      earth_science       2\\n  Tier 4 (1-4):     6 findings -- LOWEST PRIORITY\\n      orrery              3\\n      stars               3\\n\\nRun history (data/provenance_history.json):\\n  previous run 20261014T034203Z (under an hour earlier, HEAD 869b8c2)\\n  delta   total +0   T1 +0   T2 +0   T3 +0   T4 +0\\n  no file\'s Tier-1 count rose.\\n  Tier-1 by domain: orrery 116, Earth System 149, stars 13, utilities 2\\n  no domain\'s Tier-1 count moved.\\n  gate path: the same 0 Tier-1 finding(s) by name as the previous run.\\n\\n======================================================================\\n  GATE PATH: 0 TIER-1 -- the push gate holds\\n\\n  Examined: 102 of 127 exported rows (constants_export.json),\\n  25 more computed from other rows, whose inputs are scored;\\n  0 display string(s) in 13 served object(s) (objects_export.json).\\n\\n  Whole tree, Tier-1: 280: orrery 116, Earth System 149, stars 13, utilities 2.\\n  Informational; the gate is the GATE PATH line above.\\n  Nothing here sets the exit code.\\n======================================================================\\n"\n\nRISEN = [(\'patch_L436_1_idea_20261013.py\', 0, 1)]\nWITH_RISE = AS_PRINTED.replace(\n    "  no file\'s Tier-1 count rose.\\n",\n    "  Tier-1 ROSE in 1 file(s):\\n"\n    "      patch_L436_1_idea_20261013.py                0 -> 1  (+1)\\n")\nNO_HISTORY = AS_PRINTED[:AS_PRINTED.index(\'Run history\')] + \\\n    AS_PRINTED[AS_PRINTED.index(\'=====\'):]\n\n# ============================================================================\n# RUNNING THE REAL SUMMARY\n# ============================================================================\n\ndef load(old=None, new=None):\n    """The runner, real or with one line changed. The anchor must be found\n    exactly once, or the plant fails loudly rather than testing nothing."""\n    path = os.path.join(HERE, \'orrery_maintenance_run.py\')\n    with open(path, encoding=\'utf-8\') as f:\n        src = f.read()\n    if old is not None:\n        n = src.count(old)\n        if n != 1:\n            raise RuntimeError(\'PLANT ANCHOR: %r found %d times\' % (old[:60], n))\n        src = src.replace(old, new)\n    mod = types.ModuleType(\'orrery_maintenance_run_under_test\')\n    mod.__file__ = path\n    exec(compile(src, path, \'exec\'), mod.__dict__)\n    return mod\n\n\ndef summary_of(mod, scanner_output):\n    """What main() prints when its suite is the scanner alone and the\n    scanner printed scanner_output. Nothing is run or written."""\n    mod.GENERATORS = []\n    mod.CHECKERS = [(\'Provenance scanner\', [\'provenance_scanner.py\'],\n                     (\'GATE PATH:\', \'Whole tree, Tier-1:\'), True)]\n    mod.run_tool = lambda project_dir, argv_tail: (0, scanner_output, 0.1)\n    mod.tree_snapshot = lambda project_dir: {}\n    mod.print_files_written = lambda before, after: None\n    mod.staleness_report = lambda project_dir: []\n    here = os.getcwd()\n    buf = io.StringIO()\n    try:\n        with contextlib.redirect_stdout(buf):\n            mod.main()\n    finally:\n        os.chdir(here)\n    text = buf.getvalue()\n    # Only the summary block: from the gating headline to its closing rule.\n    start = text.index(\'gating checkers passed\')\n    return text[start:text.index(\'=\' * 70, start)]\n\n\n# ============================================================================\n# THE JUDGES\n# ============================================================================\n\ndef judge(mod, findings, counts):\n    s = summary_of(mod, AS_PRINTED)\n    counts[\'summaries\'] += 1\n    flat = \' \'.join(s.split())\n    if "No file\'s Tier-1 count rose since the previous run" not in flat:\n        findings.append((\'RISE LINE NOT PRINTED\', \'the summary does not say that no \'\n                         "file\'s Tier-1 rose, which the scanner printed"))\n\n    s = summary_of(mod, WITH_RISE)\n    counts[\'summaries\'] += 1\n    flat = \' \'.join(s.split())\n    if \'Tier-1 rose since the previous run in %d file(s)\' % len(RISEN) not in flat:\n        findings.append((\'RISE LINE NOT PRINTED\', \'the summary does not say that %d \'\n                         "file\'s Tier-1 rose" % len(RISEN)))\n    for fname, before, after in RISEN:\n        counts[\'risen\'] += 1\n        if (\'%s: %d -> %d\' % (fname, before, after)) not in flat:\n            findings.append((\'RISEN FILE NOT NAMED\', \'the summary does not name %s, \'\n                             \'%d -> %d\' % (fname, before, after)))\n\n    s = summary_of(mod, NO_HISTORY)\n    counts[\'summaries\'] += 1\n    flat = \' \'.join(s.split())\n    if \'Tier-1 rise: NOT READ\' not in flat:\n        findings.append((\'MISSING RISE NOT ANNOUNCED\', \'the scanner printed no run \'\n                         \'history and the runner did not say so\'))\n\n\nPLANTS = [\n    (\'the summary no longer prints the rise lines\',\n     (\'                for line in scanner_risen_lines(row[4]):\\n\',\n      \'                for line in []:\\n\'),\n     \'RISE LINE NOT PRINTED\'),\n    (\'a risen file counted but not named\',\n     ("            lines.append(\'- %s: %s -> %s\' % (fname, before, after))\\n",\n      \'            pass\\n\'),\n     \'RISEN FILE NOT NAMED\'),\n    (\'missing run-history lines passed over in silence\',\n     ("    return [\'Tier-1 rise: NOT READ -- the scanner printed neither \'\\n",\n      "    return []\\n    return [\'Tier-1 rise: NOT READ -- the scanner printed neither \'\\n"),\n     \'MISSING RISE NOT ANNOUNCED\'),\n]\n\n\ndef main():\n    problems = []\n    for label, (old, new), expected in PLANTS:\n        findings, counts = [], {\'summaries\': 0, \'risen\': 0}\n        try:\n            judge(load(old, new), findings, counts)\n        except RuntimeError as ex:\n            print(\'planted: %-52s COULD NOT BE PLANTED: %s\' % (label, ex))\n            problems.append(\'plant failed: %s\' % label)\n            continue\n        hits = [d for c, d in findings if c == expected]\n        if hits:\n            print(\'planted: %-52s caught as %s (%s)\' % (label, expected, hits[0]))\n        else:\n            print(\'planted: %-52s NOT CAUGHT; findings: %s\'\n                  % (label, sorted(set(c for c, _ in findings)) or \'none\'))\n            problems.append(\'planted fault not caught: %s\' % label)\n\n    findings, counts = [], {\'summaries\': 0, \'risen\': 0}\n    judge(load(), findings, counts)\n    for cls, detail in findings:\n        print(\'FAIL: %s -- %s\' % (cls, detail))\n        problems.append(\'%s -- %s\' % (cls, detail))\n    print("compared: the maintenance run\'s printed summary against the scanner output "\n          "recorded here -- the sentence that no file rose, the risen file by name with "\n          "its before and after, and the sentence when the run history is missing")\n    print(\'examined: three summaries (as printed at ab96681, with one file risen, with \'\n          \'no run history) from the real main() of orrery_maintenance_run.py\')\n    if problems:\n        print(\'MAINTENANCE REPORT: FAIL -- %d problem(s)\' % len(problems))\n        return 1\n    print(\'MAINTENANCE REPORT: PASS -- %d of %d planted faults caught by name; %d summaries; \'\n          \'%d risen file(s) named\' % (len(PLANTS), len(PLANTS), counts[\'summaries\'],\n                                      counts[\'risen\']))\n    return 0\n\n\nif __name__ == \'__main__\':\n    sys.exit(main())\n',
    'documentation/HANDOFF_L269_risen_files_20261013.md': '<!-- Doc-Kind: hand | Session record: the maintenance run\'s summary names every file whose Tier-1 rose since the scanner\'s previous run (L-269), redelivered on top of L-437. -->\n# The maintenance run names the files whose Tier-1 rose (L-269)\n\nBuilt on orrery ab96681 ("L431 close") at\nhttps://github.com/tonylquintanilla/palomas_orrery (main). The gallery\nis not touched.\nTony\'s local folders: orrery\n`C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\`;\ngallery `C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\`.\nWritten October 13, 2026 with Anthropic\'s Claude Opus 5.5.\nPatch: `patch_L269_5_risen_files_20261013.py`.\n\n## 1. Why, and why a second patch\n\nTony\'s run record of 2026-10-13: "i was expecting the module class\nbreakdown." The maintenance run\'s summary quoted only the scanner\'s\nGATE PATH line, so two things printed only on the scanner\'s own screen:\nthe whole-tree Tier-1 by kind of code, and the files whose Tier-1 rose\nsince the scanner\'s previous run.\n\nThe first patch, `patch_L269_1_scanner_breakdown_20261013.py`, did both\nand was built on 70202e3b. L-437 (the Tier-1 total split by domain) ran\nfirst and put the split on the scanner\'s row, so the first patch\nrefuses and would repeat the split if re-anchored. The coordination\nsession ordered the redelivery: "drop the breakdown half, keep the half\nthat names each file whose count rose, one patch, planted faults shown\ncaught." It is also deleted, not filed: its name repeats\n`documentation/patch_L269_1_ledger_blocks_and_protocol_v3_49.py`.\n\n## 2. What changed\n\nUnder the scanner\'s verdict in the summary, read from the scanner\'s own\nrun-history lines:\n\n    Provenance scanner          0 TIER-1 -- the push gate holds; Whole\n                                tree, Tier-1: 280: orrery 116, ...\n      No file\'s Tier-1 count rose since the previous run.\n\nor, when a file rose,\n\n      Tier-1 rose since the previous run in 1 file(s):\n      - patch_L436_1_idea_20261013.py: 0 -> 1\n\nIf the scanner printed no run history, the line says NOT READ.\n\nNew checker `test_maintenance_report.py`, "Maintenance report (L-269)"\nin the run and "Maintenance Report" on the dashboard. It runs the\nrunner\'s real main() on the scanner\'s output recorded at ab96681, in\nthree versions, after three planted faults are each caught by name:\n\n    planted                                          caught as\n    the summary no longer prints the rise lines      RISE LINE NOT PRINTED\n    a risen file counted but not named               RISEN FILE NOT NAMED\n    missing run-history lines passed over in         MISSING RISE NOT ANNOUNCED\n      silence\n\nGATING AND REPORT-ONLY in the runner\'s docstring no longer names a\ncount. It read twenty-five while the run had twenty-six; three sessions\nadded rows on 2026-10-13, and the headline already counts from the\ntable.\n\n## 3. Tested\n\n- The checker: 3 of 3 planted faults caught, then a clean pass.\n- The maintenance run on a clean clone of ab96681 with the patch\n  applied: every gating checker passed, and the rise line printed under\n  the scanner\'s.\n- The patch on a clean clone gives these files byte for byte; a second\n  run refuses; on a copy with Windows line endings and a note added, it\n  writes LF and keeps the note.\n\n## 4. For Tony\n\n- (do) Delete `patch_L269_1_scanner_breakdown_20261013.py` from the root\n  folder; it is superseded.\n- (do) Run `patch_L269_5_risen_files_20261013.py` (VS Code, Run), then\n  `orrery_maintenance_run.py`.\n- (do) Move it, and `patch_L431_9_close_20261013.py`, into\n  `documentation/`; commit and push.\n\nIf the dashboard session\'s patch lands after this one, its parity check\nmay ask for a one-line description for the Maintenance Report button;\nthat session said it would.\n\nNo skill or protocol version changes.\n',
}

FIXES = [
    "The maintenance run's summary, under the scanner's verdict: each file whose Tier-1 "
    "rose since the scanner's previous run, by name with its before and after, or a "
    "line saying none rose.",
    'If the scanner printed no run history, the line says NOT READ instead of leaving it out.',
    'New checker test_maintenance_report.py, with three planted faults; its dashboard button '
    '"Maintenance Report".',
]


def apply():
    for f in CREATED:
        if os.path.exists(os.path.join(ROOT, f)):
            print('ERROR: %s already exists; this patch has run. NOTHING was written.' % f)
            return None
    texts, crlf, done = {}, set(), []
    for f, label, old, new in EDITS:
        path = os.path.join(ROOT, f)
        if f not in texts:
            if not os.path.exists(path):
                print('ERROR: %s not found in %s. NOTHING was written.' % (f, ROOT))
                return None
            raw = open(path, 'rb').read()
            if b'\r\n' in raw:
                crlf.add(f)
            texts[f] = raw.replace(b'\r\n', b'\n').decode('utf-8')
        t = texts[f]
        n = t.count(old)
        if n != 1:
            print('ANCHOR FAIL  %-45s %s (found %d times, expected 1). NOTHING was written.'
                  % (f, label, n))
            return None
        if MARKER in t and t.index(old) > t.index(MARKER):
            print('ANCHOR FAIL  %-45s %s lies below the run-record marker. NOTHING was written.'
                  % (f, label))
            return None
        texts[f] = t.replace(old, new)
        done.append((f, label))
    for f, label, old, new in EDITS:
        if any(ord(c) > 127 for c in new):
            print('ERROR: an edit to %s would add non-ASCII. NOTHING was written.' % f)
            return None
    for f, t in texts.items():
        with open(os.path.join(ROOT, f), 'w', encoding='utf-8', newline='') as h:
            h.write(t)
    for f, t in CREATED.items():
        with open(os.path.join(ROOT, f), 'w', encoding='utf-8', newline='') as h:
            h.write(t)
    for f, label in done:
        print('ok  %-45s %s' % (f, label))
    for f in CREATED:
        print('ok  %-45s created' % f)
    for f in sorted(crlf):
        print('note: %s was CRLF in the working copy; written LF' % f)
    print()
    print('patch applied (%d edits in %d files, %d file created)'
          % (len(done), len(texts), len(CREATED)))
    print('Stamps updated: the docstrings of both edited modules, the ledger.')
    print()
    print('What changed:')
    for line in FIXES:
        print('  - ' + line)
    return True


def main():
    if not apply():
        return 1
    print()
    print('NEXT:')
    print('  1. Delete patch_L269_1_scanner_breakdown_20261013.py from this folder; this')
    print('     patch replaces it.')
    print('  2. Run orrery_maintenance_run.py: expect every gating checker to pass, among')
    print('     them "Maintenance report" with 3 of 3 planted faults. At the bottom, under')
    print('     "Provenance scanner", a line now says whether any file\'s Tier-1 count rose.')
    print('  3. Move this script and patch_L431_9_close_20261013.py into documentation/;')
    print('     commit and push.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
