"""patch_L269_1_scanner_breakdown_20261013.py -- L-269 (a report names
its items): the maintenance run's summary prints the provenance
scanner's whole-tree Tier-1 by kind of code, and names every file whose
Tier-1 rose since the previous run.

Built on orrery 70202e3bff79136fe6561aab60d42f57b193eda9 at
https://github.com/tonylquintanilla/palomas_orrery ("maintenance").
The gallery is not touched.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\;
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\.
Written October 13, 2026 with Anthropic's Claude Opus 5.5.
Record: documentation/HANDOFF_L269_maintenance_breakdown_20261013.md
(created by this patch).

HOW TO RUN
    From the orrery repo's ROOT folder: open this file in VS Code and
    press Run, or from a terminal in that folder:
        python patch_L269_1_scanner_breakdown_20261013.py
    Success prints one "ok" line per edit, then "patch applied". It asks
    nothing and fetches nothing.

WHAT IT CHANGES
    orrery_maintenance_run.py: scanner_breakdown_lines(); the summary
      prints the scanner's whole tree by kind of code and the risen files
      under its verdict, or says NOT READ; CHECKERS gains Maintenance
      report (L-269). Twenty-six gating checkers.
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
     "GATING AND REPORT-ONLY\n----------------------\nTwenty-six checkers are pass/fail: a problem makes them exit non-zero.\nTwo are REPORT-ONLY -- worksheet_checker.py and provenance_scanner.py\nexit 0 whatever they find, and exit 1 only when they could not run.\nThey are marked in the CHECKERS table, and the summary counts the\ngating twenty-six in its headline and quotes the two report-only verdicts\nunderneath. Under the scanner's verdict it also prints the whole tree's\nTier-1 by kind of code and names any file whose Tier-1 rose since the\nprevious run, both read from the scanner's own output (L-269).\n\nThe block quotes each tool's own note rather than restating it. A\n"),
    ('orrery_maintenance_run.py', 'line 181: distance, after nine faults planted in copie',
     'distance, after nine faults planted in copies of the real source are each\ncaught by name. Twenty-five gating checkers.)\n"""\n\nimport hashlib\nimport os\nimport subprocess\nimport sys\n',
     'distance, after nine faults planted in copies of the real source are each\ncaught by name. Twenty-five gating checkers.)\nModule updated: October 13, 2026 with Anthropic\'s Claude Opus 5.5 (L-269,\nTony\'s run record of the same day: "i was expecting the module class\nbreakdown." The summary quoted only the scanner\'s GATE PATH line, so the\nwhole tree\'s Tier-1 by kind of code, and the files whose Tier-1 rose,\nshowed only on the scanner\'s own screen. scanner_breakdown_lines() reads\nboth from the scanner\'s output and the summary prints them under its\nverdict, in both branches; when it cannot read them it says so. CHECKERS\ngains Maintenance report (L-269), test_maintenance_report.py, which runs\nthis file\'s summary on recorded scanner output after three planted\nfaults are each caught by name. Twenty-six gating checkers.)\n"""\n\nimport hashlib\nimport os\nimport re\nimport subprocess\nimport sys\n'),
    ('orrery_maintenance_run.py', "line 334: ('Orbit markers (L-431, L-401)', ['test_orbi",
     '    (\'Orbit markers (L-431, L-401)\', [\'test_orbit_markers.py\'],\n     \'ORBIT MARKERS:\'),\n    # A fourth field marks a tool REPORT-ONLY: it exits 0 whatever it\n    # finds, so "passed" says only that it ran. Exactly two are, and\n',
     '    (\'Orbit markers (L-431, L-401)\', [\'test_orbit_markers.py\'],\n     \'ORBIT MARKERS:\'),\n    # L-269, 2026-10-13: this runner\'s own summary prints the scanner\'s\n    # whole-tree Tier-1 by kind of code and names the files whose Tier-1\n    # rose; three faults planted first in copies of this file, each\n    # caught by name.\n    (\'Maintenance report (L-269)\', [\'test_maintenance_report.py\'],\n     \'MAINTENANCE REPORT:\'),\n    # A fourth field marks a tool REPORT-ONLY: it exits 0 whatever it\n    # finds, so "passed" says only that it ran. Exactly two are, and\n'),
    ('orrery_maintenance_run.py', 'line 544: def scanner_breakdown_lines(output):',
     '\n\ndef wrapped(text, width=NOTE_WIDTH):\n    """The whole sentence across as many lines as it needs.\n',
     '\n\ndef scanner_breakdown_lines(output):\n    """\n    The scanner\'s whole-tree Tier-1, by kind of code, and the files whose\n    Tier-1 rose since its previous run, read from its own output (L-269).\n\n    The summary otherwise quotes only the GATE PATH line, so a reader of\n    the summary saw neither: the breakdown and the risen files printed on\n    the scanner\'s screen, which this runner captures and does not show.\n    Both are read, never recomputed, so they cannot drift from what the\n    scanner printed. Anything that cannot be read is said, not dropped.\n    """\n    lines = []\n    m = re.search(r\'Tier 1 \\([^)]*\\):\\s*(\\d+) findings[^\\n]*\\n((?:[ \\t]{5,}\\S+[ \\t]+\\d+[ \\t]*\\n)*)\',\n                  output)\n    if m:\n        parts = re.findall(r\'(\\S+)[ \\t]+(\\d+)\', m.group(2))\n        split = \', \'.join(\'%s %s\' % (name, n) for name, n in parts)\n        lines.append(\'Whole tree, Tier-1: %s%s\' % (m.group(1),\n                                                   (\' -- \' + split) if split else \'\'))\n    else:\n        lines.append(\'Whole tree, Tier-1: NOT READ -- the scanner printed no \'\n                     \'"Tier 1 (...): N findings" line\')\n    if re.search(r"no file\'s Tier-1 count rose", output):\n        lines.append("No file\'s Tier-1 count rose since the previous run.")\n    else:\n        r = re.search(r\'Tier-1 ROSE in (\\d+) file\\(s\\):\\s*\\n((?:[ \\t]+\\S+[ \\t]+\\d+ -> \\d+.*\\n?)*)\',\n                      output)\n        if r:\n            risen = re.findall(r\'(\\S+)[ \\t]+(\\d+) -> (\\d+)\', r.group(2))\n            lines.append(\'Tier-1 rose since the previous run in %s file(s):\' % r.group(1))\n            for fname, before, after in risen:\n                lines.append(\'- %s: %s -> %s\' % (fname, before, after))\n        elif \'first recorded run\' in output:\n            lines.append(\'Tier-1 rise: first recorded run, nothing to compare with.\')\n        else:\n            lines.append(\'Tier-1 rise: NOT READ -- the scanner printed neither \'\n                         \'"no file\\\'s Tier-1 count rose" nor "Tier-1 ROSE in"\')\n    return lines\n\n\ndef wrapped(text, width=NOTE_WIDTH):\n    """The whole sentence across as many lines as it needs.\n'),
    ('orrery_maintenance_run.py', 'line 781: for row in report_only:',
     "        for row in report_only:\n            print('    %-27s %s' % (row[0], row[3]))\n    print('=' * 70)\n\n",
     "        for row in report_only:\n            print('    %-27s %s' % (row[0], row[3]))\n            # L-269: the scanner's whole tree by kind of code, and the\n            # files whose Tier-1 rose, under its verdict. Read from the\n            # scanner's own output, which the row above already holds.\n            if row[0] == 'Provenance scanner' and row[1] is not None:\n                for line in scanner_breakdown_lines(row[4]):\n                    for piece in wrapped(line, 62):\n                        print('      ' + piece)\n    print('=' * 70)\n\n"),
    ('palomas_orrery_dashboard.py', "line 194: October 13, 2026 with Anthropic's Claude Opu",
     'October 13, 2026 with Anthropic\'s Claude Opus 5.5 (L-431, after build 2\'s\nlook): Orbit Markers\' description counts twelve planted faults, not nine.\n"""\n\n',
     'October 13, 2026 with Anthropic\'s Claude Opus 5.5 (L-431, after build 2\'s\nlook): Orbit Markers\' description counts twelve planted faults, not nine.\nOctober 13, 2026 with Anthropic\'s Claude Opus 5.5 (L-269): Maintenance\nReport under the orrery\'s checkers, in the same patch as its checker, in\nalphabetical place once the other labels lose "Test".\n"""\n\n'),
    ('palomas_orrery_dashboard.py', 'line 1217: "tilt pushed to 60 degrees) and each must be',
     '         "tilt pushed to 60 degrees) and each must be caught, then the real "\n         "rows must pass. Ends on \\"HILLS CLOUD: PASS\\" (L-421).",\n         SCRIPT_DIR,\n         True,\n',
     '         "tilt pushed to 60 degrees) and each must be caught, then the real "\n         "rows must pass. Ends on \\"HILLS CLOUD: PASS\\" (L-421).",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Maintenance Report",\n         "test_maintenance_report.py",\n         "Check that the maintenance run\'s summary prints the provenance "\n         "scanner\'s whole-tree Tier-1 by kind of code, names every file whose "\n         "Tier-1 rose since the previous run, and says so when it cannot read "\n         "them. Runs the run\'s real summary on recorded scanner output. Three "\n         "faults are planted first, each in a copy of the real code, and each "\n         "must be caught by name. "\n         "Ends on \\"MAINTENANCE REPORT: PASS\\" (L-269).",\n         SCRIPT_DIR,\n         True,\n'),
    ('LEDGER_CONSOLIDATED.md', 'line 382: Module updated: October 13, 2026 with Anthro',
     'on 400a9615.\nReview and RICE update Tony 6-21-2026\n',
     "on 400a9615.\nModule updated: October 13, 2026 with Anthropic's Claude Opus 5.5\n(L-269: the maintenance run's summary prints the scanner's whole-tree\nTier-1 by kind of code and names the files whose Tier-1 rose), built on\n70202e3b.\nReview and RICE update Tony 6-21-2026\n"),
    ('LEDGER_CONSOLIDATED.md', 'line 8508: <!-- L:269 status:OPEN upd:2026-10-13 sectio',
     '<!-- L:269 status:OPEN upd:2026-08-30 section:A flag: rice:5/4/90/3 -->\n',
     '<!-- L:269 status:OPEN upd:2026-10-13 section:A flag: rice:5/4/90/3 -->\n'),
    ('LEDGER_CONSOLIDATED.md', "line 8658: - **2026-10-13, the maintenance run's summar",
     '  are touched -- as Tony proposed on 2026-08-30.\n- **Ref:** A Check That Cannot Fail Is Not Passing and The Braid,\n',
     '  are touched -- as Tony proposed on 2026-08-30.\n- **2026-10-13, the maintenance run\'s summary names the scanner\'s\n  classes and risen files** (Tony\'s run record\n  `documentation/WHERE_WE_ARE_10-12-26_2212_run_record.md`: "this is\n  what i read: Provenance scanner 0 TIER-1 -- the push gate holds. i was\n  expecting the module class breakdown."). Since L-414 (2026-10-09) the\n  summary quoted only the GATE PATH line; the scanner\'s priority summary\n  by kind of code and its "Tier-1 ROSE in" list printed only on the\n  scanner\'s own screen, which the runner captures and does not show. So\n  the rise a session told him to expect (patch_L436_1 in the root\n  folder) never reached him. `orrery_maintenance_run.py` now prints both\n  under the scanner\'s verdict, read from the scanner\'s output, and says\n  NOT READ when it cannot find them. New checker\n  `test_maintenance_report.py`, "Maintenance report (L-269)" in the run\n  and "Maintenance Report" on the dashboard: the real summary on\n  recorded scanner output, three faults planted first, each caught by\n  name. Twenty-six gating checkers.\n  `patch_L269_1_scanner_breakdown_20261013.py`.\n- **Ref:** A Check That Cannot Fail Is Not Passing and The Braid,\n'),
    ('documentation/WHERE_WE_ARE.md', 'line 4: Last updated: October 13, 2026, afternoon: t',
     'Last updated: October 13, 2026, afternoon: no perturbation lines for Sedna.\n- Written at orrery 400a9615 and gallery 924977a3.\n',
     'Last updated: October 13, 2026, afternoon: the maintenance run shows the breakdown.\n- Written at orrery 70202e3b and gallery 924977a3.\n'),
    ('documentation/WHERE_WE_ARE.md', "line 10: > - Orbital periods' part 2 accepted and its",
     '> - Your look at the drawn orbits and markers: accepted ("bottom line:\n>   looks good").\n> - Fixes from your saved plot: Encke\'s white arc\'s accuracy line; the\n>   frame fits Sedna (1,030 au, not 1,104); by your ruling, no\n>   perturbation lines for orbits drawn around the barycentre.\n',
     "> - Orbital periods' part 2 accepted and its four fixes in, pushed.\n> - The maintenance run's summary now shows the scanner's whole-tree\n>   count by kind of code, and names any file whose count rose.\n"),
    ('documentation/WHERE_WE_ARE.md', 'line 18: > - *Run patch_L269_1 and the maintenance ru',
     "> - *Run patch_L431_8 and the maintenance run (25 of 25); reinstall\n>   horizons-orbital-mechanics 1.5; the Project's instructions to\n>   v3.94; move both patches into documentation/; push.*\n",
     '> - *Run patch_L269_1 and the maintenance run (26 of 26); move the\n>   patch into documentation/; push.*\n'),
    ('documentation/WHERE_WE_ARE.md', "line 116: - The maintenance run's breakdown: `HANDOFF_",
     '  look and fixes `HANDOFF_L431_build2_look_fixes_20261013.md`\n- The distance digits: `DESIGN_L401_distance_digits_rulings_20261011.md`;\n',
     "  look and fixes `HANDOFF_L431_build2_look_fixes_20261013.md`\n- The maintenance run's breakdown: `HANDOFF_L269_maintenance_breakdown_20261013.md`\n- The distance digits: `DESIGN_L401_distance_digits_rulings_20261011.md`;\n"),
]

CREATED = {
    'test_maintenance_report.py': '"""\ntest_maintenance_report.py - the maintenance run\'s summary prints the\nscanner\'s whole-tree Tier-1 by kind of code, and names every file whose\nTier-1 rose; and proof that this check can fail.\n\nL-269 (a report names its items). Tony\'s run record of 2026-10-13: "i\nwas expecting the module class breakdown." The summary of\norrery_maintenance_run.py quoted only the scanner\'s GATE PATH line, so\nthe breakdown and the risen files printed only on the scanner\'s own\nscreen, which the runner captures and does not show.\n\nThis file runs the runner\'s real main() with its suite replaced by one\nrow, the scanner, whose output is RECORDED here rather than run: the\nscanner\'s console at orrery 4da3d7cc (2026-10-13), trimmed to the lines\nthe summary reads, in three versions -- as printed (no file rose), with\none file risen (the shape provenance_history.console_lines prints), and\nwith the priority summary missing. It judges the printed summary with\nreading of its own, sharing no code with the runner\'s reader.\n\nIt first plants a fault for each thing it must catch, each put into a\ncopy of the real orrery_maintenance_run.py at the line it would live in,\nand requires the right finding, by name:\n\n    planted                                          must be caught as\n    the summary no longer prints the breakdown       BREAKDOWN NOT PRINTED\n    a risen file counted but not named               RISEN FILE NOT NAMED\n    a missing priority summary passed over in        MISSING BREAKDOWN NOT ANNOUNCED\n      silence\n\nThe last line starts "MAINTENANCE REPORT:", which the maintenance run\nquotes, and says what was compared and how many things were examined.\n\nRun (VS Code Run button, or):\n    python test_maintenance_report.py\n\nRuns nothing else and contacts nothing.\n\nRole: devtool\nDomain: dev_tools\n\nModule created: October 13, 2026 with Anthropic\'s Claude Opus 5.5 (L-269).\n"""\nimport contextlib\nimport io\nimport os\nimport sys\nimport types\n\nHERE = os.path.dirname(os.path.abspath(__file__))\nif HERE not in sys.path:\n    sys.path.insert(0, HERE)\n\n# ============================================================================\n# THE RECORDED SCANNER OUTPUT (orrery 4da3d7cc, 2026-10-13, trimmed)\n# ============================================================================\n\nCLASSES = [(\'earth_science\', 149), (\'orrery\', 118), (\'stars\', 12), (\'utilities\', 2)]\nWHOLE_TREE = 281\n\nAS_PRINTED = """Audit written to PROVENANCE_AUDIT.md\n  1114 findings across 153 files\n\nPriority summary:\n  Tier 1 (16-20):   281 findings -- FIX NOW\n      earth_science     149\n      orrery            118\n      stars              12\n      utilities           2\n  Tier 2 (10-15):   683 findings -- REVIEW\n      orrery            567\n      earth_science      75\n      stars              41\n  Tier 3 (5-9):   144 findings -- LOW PRIORITY\n      orrery             91\n      dev_tools          45\n      stars               6\n      earth_science       2\n  Tier 4 (1-4):     6 findings -- LOWEST PRIORITY\n      orrery              3\n      stars               3\n\nRun history (data/provenance_history.json):\n  previous run 20261013T174809Z (under an hour earlier, HEAD 400a961)\n  delta   total +0   T1 +0   T2 +0   T3 +0   T4 +0\n  no file\'s Tier-1 count rose.\n  gate path: the same 0 Tier-1 finding(s) by name as the previous run.\n\n======================================================================\n  GATE PATH: 0 TIER-1 -- the push gate holds\n\n  Whole tree: 281 Tier-1. Informational; the gate is the\n  GATE PATH line above. Nothing here sets the exit code.\n======================================================================\n"""\n\nRISEN = [(\'patch_L436_1_idea_20261013.py\', 0, 1)]\nWITH_RISE = AS_PRINTED.replace(\n    "  no file\'s Tier-1 count rose.\\n",\n    "  Tier-1 ROSE in 1 file(s):\\n"\n    "      patch_L436_1_idea_20261013.py                0 -> 1  (+1)\\n")\nNO_SUMMARY = AS_PRINTED[:AS_PRINTED.index(\'Priority summary:\')] + \\\n    AS_PRINTED[AS_PRINTED.index(\'Run history\'):]\n\n# ============================================================================\n# RUNNING THE REAL SUMMARY\n# ============================================================================\n\ndef load(old=None, new=None):\n    """The runner, real or with one line changed. The anchor must be found\n    exactly once, or the plant fails loudly rather than testing nothing."""\n    path = os.path.join(HERE, \'orrery_maintenance_run.py\')\n    with open(path, encoding=\'utf-8\') as f:\n        src = f.read()\n    if old is not None:\n        n = src.count(old)\n        if n != 1:\n            raise RuntimeError(\'PLANT ANCHOR: %r found %d times\' % (old[:60], n))\n        src = src.replace(old, new)\n    mod = types.ModuleType(\'orrery_maintenance_run_under_test\')\n    mod.__file__ = path\n    exec(compile(src, path, \'exec\'), mod.__dict__)\n    return mod\n\n\ndef summary_of(mod, scanner_output):\n    """What main() prints when its suite is the scanner alone and the\n    scanner printed scanner_output. Nothing is run or written."""\n    mod.GENERATORS = []\n    mod.CHECKERS = [(\'Provenance scanner\', [\'provenance_scanner.py\'], \'GATE PATH:\', True)]\n    mod.run_tool = lambda project_dir, argv_tail: (0, scanner_output, 0.1)\n    mod.tree_snapshot = lambda project_dir: {}\n    mod.print_files_written = lambda before, after: None\n    mod.staleness_report = lambda project_dir: []\n    here = os.getcwd()\n    buf = io.StringIO()\n    try:\n        with contextlib.redirect_stdout(buf):\n            mod.main()\n    finally:\n        os.chdir(here)\n    text = buf.getvalue()\n    # Only the summary block: from the gating headline to its closing rule.\n    start = text.index(\'gating checkers passed\')\n    return text[start:text.index(\'=\' * 70, start)]\n\n\n# ============================================================================\n# THE JUDGES\n# ============================================================================\n\ndef judge(mod, findings, counts):\n    s = summary_of(mod, AS_PRINTED)\n    counts[\'summaries\'] += 1\n    flat = \' \'.join(s.split())\n    if (\'Whole tree, Tier-1: %d\' % WHOLE_TREE) not in flat:\n        findings.append((\'BREAKDOWN NOT PRINTED\', \'the summary does not print the whole \'\n                         "tree\'s Tier-1, %d" % WHOLE_TREE))\n    for name, n in CLASSES:\n        counts[\'classes\'] += 1\n        if (\'%s %d\' % (name, n)) not in flat:\n            findings.append((\'BREAKDOWN NOT PRINTED\', \'the summary does not print %s %d\'\n                             % (name, n)))\n    if "No file\'s Tier-1 count rose" not in flat:\n        findings.append((\'RISEN FILE NOT NAMED\', \'the summary does not say that no \'\n                         "file\'s Tier-1 rose"))\n\n    s = summary_of(mod, WITH_RISE)\n    counts[\'summaries\'] += 1\n    flat = \' \'.join(s.split())\n    for fname, before, after in RISEN:\n        counts[\'risen\'] += 1\n        if (\'%s: %d -> %d\' % (fname, before, after)) not in flat:\n            findings.append((\'RISEN FILE NOT NAMED\', \'the summary does not name %s, \'\n                             \'%d -> %d\' % (fname, before, after)))\n\n    s = summary_of(mod, NO_SUMMARY)\n    counts[\'summaries\'] += 1\n    flat = \' \'.join(s.split())\n    if \'Whole tree, Tier-1: NOT READ\' not in flat:\n        findings.append((\'MISSING BREAKDOWN NOT ANNOUNCED\', \'the scanner printed no \'\n                         \'priority summary and the runner did not say so\'))\n\n\nPLANTS = [\n    (\'the summary no longer prints the breakdown\',\n     (\'                for line in scanner_breakdown_lines(row[4]):\\n\',\n      \'                for line in []:\\n\'),\n     \'BREAKDOWN NOT PRINTED\'),\n    (\'a risen file counted but not named\',\n     ("                lines.append(\'- %s: %s -> %s\' % (fname, before, after))\\n",\n      \'                pass\\n\'),\n     \'RISEN FILE NOT NAMED\'),\n    (\'a missing priority summary passed over in silence\',\n     ("        lines.append(\'Whole tree, Tier-1: NOT READ -- the scanner printed no \'\\n"\n      "                     \'\\"Tier 1 (...): N findings\\" line\')\\n",\n      \'        pass\\n\'),\n     \'MISSING BREAKDOWN NOT ANNOUNCED\'),\n]\n\n\ndef main():\n    problems = []\n    for label, (old, new), expected in PLANTS:\n        findings, counts = [], {\'summaries\': 0, \'classes\': 0, \'risen\': 0}\n        try:\n            judge(load(old, new), findings, counts)\n        except RuntimeError as ex:\n            print(\'planted: %-52s COULD NOT BE PLANTED: %s\' % (label, ex))\n            problems.append(\'plant failed: %s\' % label)\n            continue\n        hits = [d for c, d in findings if c == expected]\n        if hits:\n            print(\'planted: %-52s caught as %s (%s)\' % (label, expected, hits[0]))\n        else:\n            print(\'planted: %-52s NOT CAUGHT; findings: %s\'\n                  % (label, sorted(set(c for c, _ in findings)) or \'none\'))\n            problems.append(\'planted fault not caught: %s\' % label)\n\n    findings, counts = [], {\'summaries\': 0, \'classes\': 0, \'risen\': 0}\n    judge(load(), findings, counts)\n    for cls, detail in findings:\n        print(\'FAIL: %s -- %s\' % (cls, detail))\n        problems.append(\'%s -- %s\' % (cls, detail))\n    print("compared: the maintenance run\'s printed summary against the scanner output "\n          "recorded here -- the whole tree\'s Tier-1 and each kind of code\'s count, the "\n          "risen file by name with its before and after, and the sentence when the "\n          "breakdown is missing")\n    print(\'examined: three summaries (as printed at 4da3d7cc, with one file risen, with \'\n          \'no priority summary) from the real main() of orrery_maintenance_run.py\')\n    if problems:\n        print(\'MAINTENANCE REPORT: FAIL -- %d problem(s)\' % len(problems))\n        return 1\n    print(\'MAINTENANCE REPORT: PASS -- %d of %d planted faults caught by name; %d summaries; \'\n          \'%d kinds of code and the whole tree, %d; %d risen file(s) named\'\n          % (len(PLANTS), len(PLANTS), counts[\'summaries\'], counts[\'classes\'], WHOLE_TREE,\n             counts[\'risen\']))\n    return 0\n\n\nif __name__ == \'__main__\':\n    sys.exit(main())\n',
    'documentation/HANDOFF_L269_maintenance_breakdown_20261013.md': '<!-- Doc-Kind: hand | Session record: the maintenance run\'s summary prints the scanner\'s whole-tree Tier-1 by kind of code and names the files whose Tier-1 rose (L-269). -->\n# The maintenance run shows the scanner\'s breakdown (L-269)\n\nBuilt on orrery 70202e3bff79136fe6561aab60d42f57b193eda9 at\nhttps://github.com/tonylquintanilla/palomas_orrery (main). The gallery\nis not touched.\nTony\'s local folders: orrery\n`C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\`;\ngallery `C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\`.\nWritten October 13, 2026 with Anthropic\'s Claude Opus 5.5.\nPatch: `patch_L269_1_scanner_breakdown_20261013.py`.\n\n## 1. What prompted it\n\nTony\'s run record of 2026-10-13\n(`documentation/WHERE_WE_ARE_10-12-26_2212_run_record.md`): "this is\nwhat i read: Provenance scanner 0 TIER-1 -- the push gate holds. i was\nexpecting the module class breakdown."\n\nSince L-414 (2026-10-09) the maintenance run\'s summary quoted only the\nscanner\'s GATE PATH line. The scanner still prints its whole-tree\nTier-1 by kind of code, and the files whose Tier-1 rose since its last\nrun, but on its own screen, which the maintenance run captures and does\nnot show. A session had told Tony to expect "Tier-1 rose" in\npatch_L436_1 while it sat in the root folder; that line never reached\nhim.\n\n## 2. What changed\n\nUnder the scanner\'s verdict, the summary now prints, read from the\nscanner\'s own output and never worked out again:\n\n    Provenance scanner          0 TIER-1 -- the push gate holds\n      Whole tree, Tier-1: 281 -- earth_science 149, orrery 118, stars\n      12, utilities 2\n      No file\'s Tier-1 count rose since the previous run.\n\nand, when a file\'s Tier-1 rose,\n\n      Tier-1 rose since the previous run in 1 file(s):\n      - patch_L436_1_idea_20261013.py: 0 -> 1\n\nWhen the scanner\'s output lacks either part, the line says NOT READ\nrather than leaving it out (A Check That Cannot Fail Is Not Passing:\nmake the blind spot announce). Printed whether or not a checker failed.\n\nNew checker `test_maintenance_report.py`, "Maintenance report (L-269)"\nin the run and "Maintenance Report" on the dashboard. It runs the\nrunner\'s real main() with the scanner\'s output recorded at 4da3d7cc, in\nthree versions (as printed, one file risen, no priority summary), after\nthree planted faults are each caught by name:\n\n    planted                                          caught as\n    the summary no longer prints the breakdown       BREAKDOWN NOT PRINTED\n    a risen file counted but not named               RISEN FILE NOT NAMED\n    a missing priority summary passed over in        MISSING BREAKDOWN NOT ANNOUNCED\n      silence\n\nTwenty-six gating checkers.\n\n## 3. Tested\n\n- The checker: 3 of 3 planted faults caught, then a clean pass.\n- The maintenance run on a clean clone with the patch applied: 26 of 26\n  gating checkers, and the breakdown printed under the scanner\'s line.\n- The patch on a clean clone gives these files byte for byte; on a copy\n  with Windows line endings and a note added, it writes LF and keeps\n  the note.\n\n## 4. One correction\n\npatch_L436_1_idea_20261013.py is another session\'s patch (L-436, an\nidea about using the orrery away from this computer) and has NOT been\nrun: the ledger has no L-436 block. An earlier message in this session\ntold Tony to move it into documentation/ with the others. That was\nwrong; it waits in the root folder for its own run.\n\n## 5. For Tony\n\n- (do) Run `patch_L269_1_scanner_breakdown_20261013.py` (VS Code, Run),\n  then `orrery_maintenance_run.py`: 26 of 26, and the breakdown under\n  the scanner\'s line at the bottom.\n- (do) Move the patch into `documentation/`; commit and push.\n\nNo skill or protocol version changes.\n',
}

FIXES = [
    "The maintenance run's summary, under the scanner's verdict: the whole tree's Tier-1 "
    "by kind of code, and the name of any file whose Tier-1 rose since the previous run.",
    'If the scanner\'s output lacks either, the line says NOT READ instead of leaving it out.',
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
    print('  1. Run orrery_maintenance_run.py: expect 26 of 26 gating checkers, among them')
    print('     "Maintenance report" with 3 of 3 planted faults. At the bottom, under')
    print('     "Provenance scanner", you should now see a "Whole tree, Tier-1" line with')
    print('     the count for each kind of code, and a line about files whose count rose.')
    print('  2. Move this script into documentation/; commit and push.')
    print('  patch_L436_1_idea_20261013.py has not been run yet; it is another session\'s')
    print('  and waits for its own run. Leave it in the root folder until then.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
