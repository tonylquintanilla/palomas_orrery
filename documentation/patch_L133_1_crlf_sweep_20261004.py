#!/usr/bin/env python3
"""
patch_L133_1_crlf_sweep_20261004.py -- ORRERY repo. L-133: the 22 files
still committed with Windows (CRLF) line endings, written LF.

Built on orrery 41c1ca7a175992248dad9cc3237686beab032f82
at https://github.com/tonylquintanilla/palomas_orrery, AFTER
patch_L413_1_ledger_sweep_and_earth_list_20261004.py has run (it writes
the L-133 entry this patch closes). Run patch_L413_1 first, and commit
and push it; this patch refuses until that patch's handoff exists.

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code and click Run. Then run orrery_maintenance_run.py
    the same way: every gating check should pass. Move this script into
    documentation/, then commit and push ON ITS OWN, not together with
    other work.

WHAT YOU WILL SEE IN GITHUB DESKTOP
    The 22 files below show EVERY line changed. That is the line
    endings, and it is the point of this commit: git stored them CRLF
    from before the repo's LF rule, so converting them is a whole-file
    change, once. After this push, no committed orrery file is CRLF.

WHAT CHANGES
    22 files, line endings only, each first checked to hold exactly the
        content committed at 41c1ca7a (line endings aside):
        .gitignore, catalog_selection.py, create_cache_backups.py, data_acquisition.py, data_acquisition_distance.py, data_processing.py, formatting_utils.py, hr_diagram_apparent_magnitude.py, hr_diagram_distance.py, messier_object_data_handler.py, object_type_analyzer.py, planetarium_apparent_magnitude.py, planetarium_distance.py, report_manager.py, shutdown_handler.py, star_notes.py, star_properties.py, stellar_data_patches.py, stellar_parameters.py, visualization_2d.py, visualization_3d.py, visualization_core.py.
    One fix in passing, named in the output: two pairs of curly quotes
        in a comment at star_properties.py line 63 become plain quotes.
    LEDGER_CONSOLIDATED.md        L-133 closed; L-415 notes it; header stamp.
    documentation/WHERE_WE_ARE.md three lines.
    documentation/HANDOFF_L413_ledger_sweep_and_earth_list_20261004.md
                                  the step recorded. These three are
        matched by their lines, so your notes in them do not stop this
        patch.

PERMANENT, though this script is thrown away: the 22 files' LF endings.

SUCCESS looks like: one "ok" line per file or edit, "All 21 Python files
compile", then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 4, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

REPO = "orrery"
ROOT_MARKERS = ("palomas_orrery.py", "LEDGER_CONSOLIDATED.md")
BUILT_ON = "41c1ca7a"
NEEDS = "documentation/HANDOFF_L413_ledger_sweep_and_earth_list_20261004.md"
NEXT = ["1. Run orrery_maintenance_run.py. Every gating check passes.",
        "2. Move this script into documentation/; commit and push on its",
        "   own. Every line of the 22 files shows as changed: expected."]

SWEEP = {'.gitignore': '583057640c9d9749e6404980e297807a',
 'catalog_selection.py': '91df709bbb08cf6789c3611af92b5efe',
 'create_cache_backups.py': '5c575c699c596174d1fe09e98d276503',
 'data_acquisition.py': '080111ee548fe7fc568779aaaeea8be3',
 'data_acquisition_distance.py': '2155c4f9c46ff318a67b2a6a22869a3f',
 'data_processing.py': '2d1482af780f9ecc81c551b3a376228b',
 'formatting_utils.py': 'bebe26cddeaafe8863f0a3a3651f12f0',
 'hr_diagram_apparent_magnitude.py': '674ea2899202ad9699112dddc7f8d8a3',
 'hr_diagram_distance.py': 'fad5518456baa5489d288e31881e4920',
 'messier_object_data_handler.py': 'e2b89c20c4c6b19940eedb5b0a6ce9d6',
 'object_type_analyzer.py': 'a730f8ba37a5a20e8c633dbd4c798dbf',
 'planetarium_apparent_magnitude.py': 'ac7401ffbfb3bc892d968987d0a7fa43',
 'planetarium_distance.py': 'a070a0e76d308eed8e65c886cb083218',
 'report_manager.py': 'd45940fe0a2c273418d6963faa4865e1',
 'shutdown_handler.py': '6c9283324f9184c6988bd2bc10b5d969',
 'star_notes.py': '7b4715c7de1185dc1dcc3fc44e121a30',
 'star_properties.py': 'dec47dfcd378a6d2db20b9f812b069f8',
 'stellar_data_patches.py': '65c8353656962e2621ad333a32a19595',
 'stellar_parameters.py': 'b5c6b2c763c07e254be25f132d1b15fe',
 'visualization_2d.py': '0b62ea91506eb187ac3e39835e21eb0c',
 'visualization_3d.py': '5badc588d55d830722bcf40c4a4a7772',
 'visualization_core.py': '6c37e0317a75b8aef7e7a64464dfaffa'}

EDITS = {'LEDGER_CONSOLIDATED.md': [('L-133: status line',
                             '<!-- L:133 status:OPEN upd:2026-10-04 '
                             'section:D.Structural flag: rice:2/2/50/2 -->',
                             '<!-- L:133 status:DONE upd:2026-10-04 '
                             'section:C flag: rice:2/2/50/2 -->',
                             1),
                            ('L-133: done',
                             '**Gap:** narrower now -- a one-time sweep of '
                             'the 22 files above,\n'
                             'already CRLF in the repo from before this rule '
                             'existed (the\n'
                             ".gitattributes fix doesn't retroactively touch "
                             "files it hasn't seen\n"
                             're-added). One commit, nothing else in it.\n',
                             "- **2026-10-04, DONE on Tony's word** "
                             '("Let\'s take care of L133 now\n'
                             '  and take this off the backlog"): '
                             '`patch_L133_1_crlf_sweep_20261004.py`\n'
                             '  wrote all 22 files LF, each first checked to '
                             'hold the content\n'
                             '  committed at 41c1ca7a. Only line endings '
                             'changed, with one exception\n'
                             '  fixed in passing under the same harness and '
                             "named in the patch's\n"
                             '  output: two pairs of curly quotes in a '
                             'comment at `star_properties.py`\n'
                             '  line 63 became plain quotes. All 21 Python '
                             'files compile. Committed\n'
                             '  on its own, apart from this entry, Where We '
                             'Are and the handoff.\n'
                             '  - The check that it worked: `git ls-files '
                             '--eol` shows `i/lf` for\n'
                             '    all 22 after the push, so no committed '
                             'file in the orrery is CRLF.\n'
                             '    Claude reads it from a fresh clone at the '
                             "next session's pull.\n"
                             '**Gap:** none.\n',
                             1),
                            ('L-415: L-133 done the same session',
                             "visualization_core.py. These are L-133's.\n",
                             "visualization_core.py. These are L-133's.\n"
                             "- **2026-10-04: L-133's sweep done the same "
                             'session**\n'
                             "  (`patch_L133_1`), so 1.12's exception for "
                             'committed-CRLF files has\n'
                             '  no instance left in the orrery. It stays in '
                             'the skill: the gallery\n'
                             '  repo, or a file added from elsewhere, can '
                             'still meet it.\n',
                             1),
                            ('header stamp',
                             'stamp; this one does not restate them.\n',
                             'stamp; this one does not restate them.\n'
                             'Module updated: October 4, 2026 with '
                             "Anthropic's Claude Opus 5.5\n"
                             '(L-133 closed: the 22 committed-CRLF files '
                             'written LF by\n'
                             "patch_L133_1), built on patch_L413_1's tree "
                             'over 41c1ca7a.\n',
                             1)],
 'documentation/HANDOFF_L413_ledger_sweep_and_earth_list_20261004.md': [('item '
                                                                         '5',
                                                                         '   '
                                                                         'safe-file-editing '
                                                                         'to '
                                                                         '1.12 '
                                                                         'with '
                                                                         'protocol '
                                                                         'v3.80 '
                                                                         '(L-415). '
                                                                         'Counted '
                                                                         'the\n'
                                                                         '   '
                                                                         '22 '
                                                                         'files '
                                                                         'still '
                                                                         'committed '
                                                                         'CRLF '
                                                                         'onto '
                                                                         'L-133.\n',
                                                                         '   '
                                                                         'safe-file-editing '
                                                                         'to '
                                                                         '1.12 '
                                                                         'with '
                                                                         'protocol '
                                                                         'v3.80 '
                                                                         '(L-415). '
                                                                         'Counted '
                                                                         'the\n'
                                                                         '   '
                                                                         '22 '
                                                                         'files '
                                                                         'still '
                                                                         'committed '
                                                                         'CRLF '
                                                                         'onto '
                                                                         'L-133.\n'
                                                                         '5. '
                                                                         'On '
                                                                         "Tony's "
                                                                         'word, '
                                                                         'converted '
                                                                         'those '
                                                                         '22 '
                                                                         'files '
                                                                         'to '
                                                                         'LF '
                                                                         'in '
                                                                         'patch_L133_1,\n'
                                                                         '   '
                                                                         'its '
                                                                         'own '
                                                                         'commit, '
                                                                         'and '
                                                                         'closed '
                                                                         'L-133. '
                                                                         'One '
                                                                         'fix '
                                                                         'in '
                                                                         'passing: '
                                                                         'two '
                                                                         'pairs '
                                                                         'of\n'
                                                                         '   '
                                                                         'curly '
                                                                         'quotes '
                                                                         'in '
                                                                         'a '
                                                                         'comment '
                                                                         'in '
                                                                         'star_properties.py.\n',
                                                                         1),
                                                                        ('tony-actions',
                                                                         '- '
                                                                         '(do) '
                                                                         'Reinstall '
                                                                         'safe-file-editing '
                                                                         '(Settings '
                                                                         '> '
                                                                         'Skills) '
                                                                         'from',
                                                                         '- '
                                                                         '(do) '
                                                                         'After '
                                                                         'patch_L413_1 '
                                                                         'is '
                                                                         'committed '
                                                                         'and '
                                                                         'pushed: '
                                                                         'run\n'
                                                                         '  '
                                                                         'patch_L133_1 '
                                                                         'from '
                                                                         'the '
                                                                         'orrery '
                                                                         'root, '
                                                                         'then '
                                                                         'orrery_maintenance_run.py,\n'
                                                                         '  '
                                                                         'move '
                                                                         'the '
                                                                         'script '
                                                                         'into '
                                                                         'documentation/, '
                                                                         'and '
                                                                         'commit '
                                                                         'and '
                                                                         'push '
                                                                         'on '
                                                                         'its '
                                                                         'own.\n'
                                                                         '  '
                                                                         'GitHub '
                                                                         'Desktop '
                                                                         'shows '
                                                                         'every '
                                                                         'line '
                                                                         'of '
                                                                         'the '
                                                                         '22 '
                                                                         'files '
                                                                         'changed; '
                                                                         'that '
                                                                         'is\n'
                                                                         '  '
                                                                         'the '
                                                                         'line '
                                                                         'endings, '
                                                                         'and '
                                                                         'it '
                                                                         'is '
                                                                         'expected.\n'
                                                                         '- '
                                                                         '(do) '
                                                                         'Reinstall '
                                                                         'safe-file-editing '
                                                                         '(Settings '
                                                                         '> '
                                                                         'Skills) '
                                                                         'from',
                                                                         1)],
 'documentation/WHERE_WE_ARE.md': [('changed this session',
                                    '> - Patches now convert Windows line '
                                    'endings to the standard LF and say\n'
                                    '>   so, as you remembered the rule. The '
                                    'patch skill had said both.\n',
                                    '> - Patches now convert Windows line '
                                    'endings to the standard LF and say\n'
                                    '>   so, as you remembered the rule. The '
                                    'patch skill had said both.\n'
                                    '> - The 22 older files stored with '
                                    'Windows line endings are converted\n'
                                    '>   to LF, in a commit of their own. '
                                    'That item is off the backlog.\n',
                                    1),
                                   ('waiting on you: the 22 files done',
                                    '- Later, not urgent: 22 older files are '
                                    'still stored with Windows line\n'
                                    '  endings. Converting them is one '
                                    'commit of its own, whenever you like.\n',
                                    '',
                                    1),
                                   ('where the details are',
                                    'L-133 (the 22 older files).',
                                    'L-133 (the 22 older files, converted '
                                    'and closed).',
                                    1)],
 'star_properties.py': [('line 63 comment: two curly quote pairs made ASCII',
                         '\u201c [~]\u201d or \u201c[some text]\u201d',
                         '" [~]" or "[some text]"',
                         1)]}


def read_lf(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    return raw.replace(b"\r\n", b"\n"), b"\r\n" in raw


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the repo ROOT, not from "
                         "documentation/. NOTHING was written.")
    for marker in ROOT_MARKERS:
        if not os.path.isfile(marker):
            raise SystemExit("ERROR: %s is not here, so this is not the %s "
                             "root. NOTHING was written." % (marker, REPO))
    if not os.path.isfile(NEEDS):
        raise SystemExit("ERROR: patch_L413_1 has not run here yet (%s is\n"
                         "       missing). Run it first. NOTHING was written."
                         % NEEDS)
    out = {}
    notes = []
    for path in sorted(SWEEP):
        data, was_crlf = read_lf(path)
        got = hashlib.md5(data).hexdigest()
        if got != SWEEP[path]:
            raise SystemExit(
                "ERROR: %s is not the file committed at %s (line endings\n"
                "       aside): expected %s, found %s. It has been edited, or this\n"
                "       patch has already run.\n"
                "       NOTHING was written." % (path, BUILT_ON, SWEEP[path], got))
        out[path] = [data.decode("utf-8"), ["line endings: %s" % (
            "CRLF -> LF" if was_crlf else "already LF in your copy")]]
    for path in sorted(EDITS):
        if path not in out:
            data, was_crlf = read_lf(path)
            out[path] = [data.decode("utf-8"), []]
            if was_crlf:
                notes.append("note: %s was CRLF in the working copy; "
                             "written LF" % path)
        text = out[path][0]
        for label, old, new, want in EDITS[path]:
            found = text.count(old)
            if found != want:
                raise SystemExit("ANCHOR FAIL (%s): expected %d match(es) in "
                                 "%s, found %d. NOTHING was written."
                                 % (label, want, path, found))
            text = text.replace(old, new)
            out[path][1].append(label)
        out[path][0] = text
    for path in out:
        text = out[path][0]
        bad = sum(1 for ch in text if ord(ch) > 127)
        if bad:
            raise SystemExit("ERROR: %s would hold %d non-ASCII character(s). "
                             "NOTHING was written." % (path, bad))
        if "\r" in text:
            raise SystemExit("ERROR: %s would still hold a carriage return. "
                             "NOTHING was written." % path)
    for path in sorted(out):
        text, done = out[path]
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in done:
            print("ok  %-44s %s" % (path, label))
    for line in notes:
        print(line)
    failed = []
    count = 0
    for path in sorted(out):
        if path.endswith(".py"):
            count += 1
            try:
                compile(out[path][0], path, "exec")
            except SyntaxError as exc:
                failed.append("%s: line %s: %s" % (path, exc.lineno, exc.msg))
    print("")
    if failed:
        print("COMPILE FAILED after writing -- undo is Discard Changes:")
        for line in failed:
            print("  " + line)
        raise SystemExit(1)
    print("All %d Python files compile." % count)
    print("Stamps updated: the ledger's header (L-133 closed).")
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    for line in NEXT:
        print("  " + line)


if __name__ == "__main__":
    main()
