"""patch_L269_6_windows_output_20261014.py -- L-269: the maintenance
run's rise line reads the scanner's output on Windows.

Built on orrery fe000597d5282a93461d31065997254d5bf981ff at
https://github.com/tonylquintanilla/palomas_orrery ("L440 dashboard").
The gallery is not touched.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\;
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\.
Written October 14, 2026 with Anthropic's Claude Opus 5.5.
Record: section 5 of documentation/HANDOFF_L269_risen_files_20261013.md
(added by this patch).

HOW TO RUN
    From the orrery repo's ROOT folder: open this file in VS Code and
    press Run, or from a terminal in that folder:
        python patch_L269_6_windows_output_20261014.py
    Success prints one "ok" line per edit, then "patch applied". It asks
    nothing and fetches nothing. A second run finds its anchors gone and
    writes nothing.

WHAT IT CHANGES
    orrery_maintenance_run.py: run_tool() turns a tool's Windows line
      endings into plain ones before anything reads the output. With a
      file's Tier-1 risen, the summary had said "Tier-1 rise: NOT READ"
      on your machine (your run record of 2026-10-13).
    test_maintenance_report.py: its summaries pass through the real
      run_tool(); a fourth summary with Windows line endings and a
      fourth planted fault, the fix taken out.
    palomas_orrery_dashboard.py: the Maintenance Report card counts four
      planted faults.
    LEDGER_CONSOLIDATED.md (L-269, the stamp); the L-269 handoff, a new
      section 5. Nothing on your Where We Are page.
    No skill or protocol version changes.

SAFETY
    Each file is checked only at the lines this patch edits: every anchor
    must match exactly once, so your notes cannot make it refuse. If any
    check fails, NOTHING is written. A file found with Windows line
    endings is matched after turning them into LF and written back LF,
    and the patch says so. Undo after a run is Discard Changes in GitHub
    Desktop.

Role: patch
Domain: dev_tools
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

EDITS = [
    ('orrery_maintenance_run.py', "line 683: output = completed.stdout.decode('utf-8', 'replace",
     "            timeout=TOOL_TIMEOUT_SECONDS)\n        output = completed.stdout.decode('utf-8', 'replace')\n        return completed.returncode, output, time.time() - started\n",
     '            timeout=TOOL_TIMEOUT_SECONDS)\n        # L-269, 2026-10-14: a tool\'s lines come back as the system wrote\n        # them -- on Windows every one ends "\\r\\n" -- and every reader of\n        # the output below expects "\\n". Turned into "\\n" here, once, so\n        # no reader has to remember it. The case that showed it: with a\n        # file\'s Tier-1 risen, scanner_risen_lines() printed NOT READ on\n        # Tony\'s machine, because its pattern stopped at the "\\r".\n        output = completed.stdout.decode(\'utf-8\', \'replace\')\n        output = output.replace(\'\\r\\n\', \'\\n\')\n        return completed.returncode, output, time.time() - started\n'),
    ('orrery_maintenance_run.py', "line 363: # Tier-1 rose since the scanner's previous run; th",
     "    # Tier-1 rose since the scanner's previous run; three faults planted\n    # first in copies of this file, each caught by name.\n",
     "    # Tier-1 rose since the scanner's previous run; four faults planted\n    # first in copies of this file, each caught by name, one of them the\n    # scanner's output with Windows line endings (2026-10-14).\n"),
    ('orrery_maintenance_run.py', 'line 215: """',
     '28 gating checkers.)\n"""\n',
     '28 gating checkers.)\nModule updated: October 14, 2026 with Anthropic\'s Claude Opus 5.5 (L-269,\npatch_L269_6_windows_output_20261014.py: run_tool() turns a tool\'s\nWindows line endings into plain ones before anything reads its output.\nWith a file\'s Tier-1 risen, the summary\'s rise line had printed NOT READ\non Tony\'s machine (his run record of 2026-10-13), because the reader\'s\npattern stopped at the carriage return. Maintenance report now plants a fourth\nfault, the line-ending fix taken out, fed Windows output with a rise.)\n"""\n'),
    ('test_maintenance_report.py', 'line 187: "its before and after, and the sentence when the r',
     '          "its before and after, and the sentence when the run history is missing")\n    print(\'examined: three summaries (as printed at ab96681, with one file risen, with \'\n          \'no run history) from the real main() of orrery_maintenance_run.py\')\n',
     '          "its before and after, the sentence when the run history is missing, and the "\n          "risen file again when the output has Windows line endings")\n    print(\'examined: four summaries (as printed at ab96681, with one file risen, with \'\n          \'no run history, with one file risen and Windows line endings) from the real \'\n          \'main() and run_tool() of orrery_maintenance_run.py\')\n'),
    ('test_maintenance_report.py', 'line 159: ]',
     "     'MISSING RISE NOT ANNOUNCED'),\n]\n",
     '     \'MISSING RISE NOT ANNOUNCED\'),\n    (\'Windows line endings kept as they came\',\n     ("        output = output.replace(\'\\\\r\\\\n\', \'\\\\n\')\\n",\n      "        pass\\n"),\n     \'RISE NOT READ FROM WINDOWS OUTPUT\'),\n]\n'),
    ('test_maintenance_report.py', 'line 145: ',
     "                         'history and the runner did not say so'))\n\n\nPLANTS = [\n",
     "                         'history and the runner did not say so'))\n\n    s = summary_of(mod, WITH_RISE, line_end=WINDOWS)\n    counts['summaries'] += 1\n    flat = ' '.join(s.split())\n    for fname, before, after in RISEN:\n        counts['risen'] += 1\n        if ('%s: %d -> %d' % (fname, before, after)) not in flat:\n            findings.append(('RISE NOT READ FROM WINDOWS OUTPUT', 'with Windows '\n                             'line endings the summary does not name %s, %d -> %d'\n                             % (fname, before, after)))\n\n\nPLANTS = [\n"),
    ('test_maintenance_report.py', 'line 97: mod.run_tool = lambda project_dir, argv_tail: (0, ',
     '    mod.run_tool = lambda project_dir, argv_tail: (0, scanner_output, 0.1)\n',
     "    raw = scanner_output.replace('\\n', line_end).encode('utf-8')\n    real = mod.subprocess\n    mod.subprocess = types.SimpleNamespace(\n        run=lambda *args, **kwargs: _Completed(raw),\n        DEVNULL=real.DEVNULL, PIPE=real.PIPE, STDOUT=real.STDOUT,\n        TimeoutExpired=real.TimeoutExpired)\n"),
    ('test_maintenance_report.py', 'line 93: scanner printed scanner_output. Nothing is run or ',
     '    scanner printed scanner_output. Nothing is run or written."""\n',
     '    scanner printed scanner_output, each line ending in line_end.\n    The output reaches main() through the runner\'s own run_tool(); only\n    the process call inside it is replaced. Nothing is run or written."""\n'),
    ('test_maintenance_report.py', 'line 91: def summary_of(mod, scanner_output):',
     'def summary_of(mod, scanner_output):\n',
     'class _Completed(object):\n    """What subprocess.run() hands back: the exit code and the bytes."""\n    def __init__(self, stdout):\n        self.returncode = 0\n        self.stdout = stdout\n\n\ndef summary_of(mod, scanner_output, line_end=\'\\n\'):\n'),
    ('test_maintenance_report.py', 'line 70: # ================================================',
     "    AS_PRINTED[AS_PRINTED.index('====='):]\n\n# ============================================================================\n# RUNNING THE REAL SUMMARY\n",
     "    AS_PRINTED[AS_PRINTED.index('====='):]\n\n# What a Python program's print() puts on a pipe on Windows: every line\n# ends in a carriage return and a newline.\nWINDOWS = '\\r\\n'\n\n# ============================================================================\n# RUNNING THE REAL SUMMARY\n"),
    ('test_maintenance_report.py', 'line 45: """',
     'patch_L269_5_risen_files_20261013.py).\n"""\n',
     'patch_L269_5_risen_files_20261013.py).\nModule updated: October 14, 2026 with Anthropic\'s Claude Opus 5.5 (L-269,\npatch_L269_6_windows_output_20261014.py: the summaries pass through the\nrunner\'s real run_tool(); a fourth summary, one file risen with Windows\nline endings, and a fourth planted fault, the runner\'s line-ending fix\ntaken out.)\n"""\n'),
    ('test_maintenance_report.py', 'line 31: ',
     '      silence\n\n',
     '      silence\n    Windows line endings kept as they came           RISE NOT READ FROM\n                                                     WINDOWS OUTPUT\n\n'),
    ('test_maintenance_report.py', 'line 19: prints), and with the run-history lines missing. I',
     "prints), and with the run-history lines missing. It judges the printed\nsummary with reading of its own, sharing no code with the runner's.\n",
     'prints), with the run-history lines missing, and with one file risen\nand Windows line endings, as the scanner\'s output reaches the runner on\nTony\'s machine. The output passes through the runner\'s real run_tool(),\nwith only the process call replaced, so the way the runner reads a\ntool\'s output is tested too. It judges the printed summary with reading\nof its own, sharing no code with the runner\'s.\n\nWhy the fourth (2026-10-14). The first three were all written with\nplain line endings, and all passed. On Tony\'s machine every line the\nscanner prints ends in a carriage return as well, and with a file risen\nthe summary said "Tier-1 rise: NOT READ" (his run record of 2026-10-13):\nthe reader\'s pattern stopped at the carriage return. A check fed only\nthe sandbox\'s line endings could not fail on that.\n'),
    ('test_maintenance_report.py', 'line 17: summary to its last line, in three versions -- as ',
     'summary to its last line, in three versions -- as printed (no file\n',
     'summary to its last line, in four versions -- as printed (no file\n'),
    ('palomas_orrery_dashboard.py', 'line 1303: "that. Runs the run\'s real summary on recorded sca',
     '         "that. Runs the run\'s real summary on recorded scanner output. Three "\n',
     '         "that. Runs the run\'s real summary on recorded scanner output, once "\n         "with Windows line endings, as it reaches the run on Windows. Four "\n'),
    ('palomas_orrery_dashboard.py', 'line 237: """',
     'in a description is cut, only moved behind "+ more".\n"""\n',
     'in a description is cut, only moved behind "+ more".\nOctober 14, 2026 with Anthropic\'s Claude Opus 5.5 (L-269): Maintenance\nReport\'s description counts four planted faults, one of them the\nscanner\'s output with Windows line endings.\n"""\n'),
    ('LEDGER_CONSOLIDATED.md', 'line 8792: ',
     "  patch's in documentation/.\n\n",
     '  patch\'s in documentation/.\n- **2026-10-14, the rise line read Windows output**, by\n  `patch_L269_6_windows_output_20261014.py`, on fe00059. In Tony\'s run\n  record of 2026-10-13 the summary said "Tier-1 rise: NOT READ" on a run\n  where a file\'s Tier-1 had risen (whole tree 281, a patch script in the\n  root folder). The scanner had printed "Tier-1 ROSE in 1 file(s):", but\n  on Windows every line it prints ends in a carriage return as well, and\n  the reader\'s pattern stopped there. The "no file rose" sentence still\n  matched, so the line failed only when it had something to report, and\n  the checker passed because its recorded output had plain line endings.\n  Fixed at the one place the runner takes in a tool\'s output,\n  `run_tool()`, so every reader gets plain line endings.\n  `test_maintenance_report.py` now passes its summaries through the real\n  `run_tool()` and adds a fourth, one file risen with Windows line\n  endings, and a fourth planted fault, the fix taken out, caught as RISE\n  NOT READ FROM WINDOWS OUTPUT. Against the runner at fe00059 the new\n  check fails with that finding, which is the bug.\n\n'),
    ('LEDGER_CONSOLIDATED.md', 'line 409: Review and RICE update Tony 6-21-2026',
     'db63721d.\nReview and RICE update Tony 6-21-2026\n',
     "db63721d.\nModule updated: October 14, 2026 with Anthropic's Claude Opus 5.5\n(L-269: the maintenance run reads a tool's Windows line endings; the\nrise line no longer says NOT READ when a file rose), built on fe00059.\nReview and RICE update Tony 6-21-2026\n"),
    ('documentation/HANDOFF_L269_risen_files_20261013.md', 'line 86: No skill or protocol version changes.',
     'No skill or protocol version changes.\n',
     'No skill or protocol version changes.\n\n## 5. Afterwards: the rise line on Windows (2026-10-14)\n\nAdded by `patch_L269_6_windows_output_20261014.py`, built on fe00059 at\nhttps://github.com/tonylquintanilla/palomas_orrery ("L440 dashboard").\nWritten October 14, 2026 with Anthropic\'s Claude Opus 5.5, in the L-437\nsession, at Tony\'s request: "i think this patch is rather orphaned. can\nyou take care of this?"\n\nWhat went wrong. Tony\'s run record of 2026-10-13 shows the summary\nsaying "Tier-1 rise: NOT READ" on a run where a patch script in the root\nfolder had raised the whole tree to 281. The scanner had printed the\nrisen file. On Windows each line a program prints ends in a carriage\nreturn and a newline, and the pattern in `scanner_risen_lines()` that\nreads the risen-files list allowed only the newline. When no file rose\nit still read the sentence, so the fault showed only when there was\nsomething to report. The checker passed because its recorded output had\nplain line endings, the sandbox\'s.\n\nThe fix. `run_tool()` turns a tool\'s Windows line endings into plain\nones as it takes in the output, so every reader below it gets the same\ntext on every system. No reader changes.\n\nThe check. `test_maintenance_report.py` now passes each recorded output\nthrough the runner\'s real `run_tool()`, with only the process call\nreplaced, and adds a fourth summary: one file risen, Windows line\nendings. A fourth planted fault takes the fix out and must be caught as\nRISE NOT READ FROM WINDOWS OUTPUT. Run against the runner at fe00059,\nthe new check fails with exactly that finding.\n\nFor Tony:\n- (do) Run `patch_L269_6_windows_output_20261014.py` (VS Code, Run),\n  then `orrery_maintenance_run.py`: every gating checker passes, and\n  Maintenance report reads 4 of 4 planted faults caught. This patch adds\n  no Tier-1 finding of its own, so the line under the scanner\'s row\n  should read "No file\'s Tier-1 count rose since the previous run." The\n  next run where a file\'s count does rise is the fix seen on your\n  machine; until then the checker\'s Windows summary stands in for it.\n- Pre-tested on a clean clone of fe00059 with the patch applied: the\n  maintenance run passed 28 of 28 gating checkers; Maintenance report 4\n  of 4; Dashboard parity passed; a second run of the patch refuses.\n- (do) Move the patch into `documentation/`; commit and push.\n\nNo skill or protocol version changes.\n'),
]


def apply():
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
            if n == 0 and "replace('\\r\\n', '\\n')" in texts.get('orrery_maintenance_run.py', ''):
                print('It looks as though this patch has already run.')
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
    for f, label in done:
        print('ok  %-52s %s' % (f, label[:50]))
    for f in sorted(crlf):
        print('note: %s was CRLF in the working copy; written LF' % f)
    print()
    print('patch applied (%d edits in %d files)' % (len(done), len(texts)))
    print('Stamps updated: orrery_maintenance_run.py, test_maintenance_report.py,')
    print('palomas_orrery_dashboard.py, the ledger; the L-269 handoff gains section 5.')
    return True


def main():
    if not apply():
        return 1
    print()
    print('NEXT:')
    print('  1. Run orrery_maintenance_run.py. Every gating checker passes, and')
    print('     "Maintenance report (L-269)" reads 4 of 4 planted faults caught.')
    print('     Under the scanner\'s row: "No file\'s Tier-1 count rose since the')
    print('     previous run." The next run where a count does rise will name the')
    print('     file instead of saying NOT READ; the checker proves that case now.')
    print('  2. Move this script into documentation/; commit and push.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
