#!/usr/bin/env python3
"""
patch_L027_1_panel_colour_20261006.py -- ORRERY repo. Restores the
desktop orrery's panel colour as one name that every system knows, so
its window opens on Linux and macOS as well as Windows (L-027), and
takes the colour swap out of the pre-test (agentic-pre-test 1.3).

Built on orrery 51436054 at
https://github.com/tonylquintanilla/palomas_orrery PLUS
patch_L420_2_galactic_plane_and_centre_20261006.py and
patch_L420_3_session_close_20261006.py, which must run FIRST: this one
edits lines those two write. (gallery ed48d078 not read or changed.)

WHY
    palomas_orrery.py set the background of its panels and buttons to
    SystemButtonFace at 23 places. That colour name exists only on
    Windows; on Linux Tk stops at the first one and the window never
    opens. Tony replaced it with gray90 on 2026-01-09 and tested on all
    three systems; commit ec333df of 2026-06-12 swapped it back by
    mistake. The full account is on L-027.

HOW TO RUN IT
    After the two L-420 patches have run, save this file in the ORRERY
    repo ROOT, open it in VS Code and click Run. Then follow the NEXT
    steps it prints.

WHAT CHANGES
    palomas_orrery.py   PANEL_BG = 'gray90' defined just after the root
        window; the 23 'SystemButtonFace' become PANEL_BG; a docstring
        stamp. Nothing else in the file changes.
    skills/agentic-pre-test/SKILL.md   1.3: the headless test runs an
        unedited copy; the throwaway rule's founding case corrected.
    PROJECT_INSTRUCTIONS.md   v3.83: header, anchor, entry; v3.80
        moves down.
    documentation/PROJECT_INSTRUCTIONS_HISTORY.md   receives v3.80.
    LEDGER_CONSOLIDATED.md and documentation/HANDOFF_L420_galactic_plane_
        20261006.md   a few lines each, matched ONLY at those lines, so
        your notes anywhere else in them never stop this patch.

TESTED on a copy of 51436054 with both L-420 patches run first: every
edit landed; the orrery's window started headless on Linux with no
colour swap; orrery_maintenance_run.py passed every checker, Reset
completeness included; a second run refused and wrote nothing.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 6, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

REPO = "orrery"
ROOT_MARKERS = ("palomas_orrery.py", "LEDGER_CONSOLIDATED.md")
ZONED = {"PROJECT_INSTRUCTIONS.md": ("<!-- SKILL-MANIFEST:START",
                                     "<!-- SKILL-MANIFEST:END -->")}
NEXT = ["1. Run orrery_maintenance_run.py. Every checker should pass,",
        "   Reset completeness included; Skill manifest rewrites the",
        "   agentic-pre-test row in PROJECT_INSTRUCTIONS.md to 1.3.",
        "2. Open the orrery and look at the panels: a shade darker grey.",
        "3. Move this script into documentation/, commit and push.",
        "4. Reinstall agentic-pre-test in Settings > Skills, and replace",
        "   the Project's instructions with PROJECT_INSTRUCTIONS.md (v3.83)."]

BASE = {
    'PROJECT_INSTRUCTIONS.md': '882a697670d8eae49f9543c3fbbfc0ca',
    'documentation/PROJECT_INSTRUCTIONS_HISTORY.md': '30cb2b9dad20e6f269df26235edee6ee',
    'palomas_orrery.py': '75f2cd7a802b577fccddd5e3c96e796a',
    'skills/agentic-pre-test/SKILL.md': '52dcf98e01ae8fd733b448404b5c4849',
}

ANCHOR_ONLY = ('LEDGER_CONSOLIDATED.md', 'documentation/HANDOFF_L420_galactic_plane_20261006.md')

EDITS = {
  'palomas_orrery.py': [
    ('docstring stamp',
      'A*, which star_sphere_builder.py now draws. Words approved by Tony,\n2026-10-06.)\n',
      "A*, which star_sphere_builder.py now draws. Words approved by Tony,\n2026-10-06.)\nModule updated: October 6, 2026 with Anthropic's Claude Opus 5.5 (L-027:\nthe panels' background is one name, PANEL_BG = 'gray90', in place of\nthe Windows-only SystemButtonFace at 23 sites, so the window opens on\nLinux and macOS as well. Tony's colour of January 2026, restored.)\n",
      1),
    ('PANEL_BG defined after the root window',
      'root.title("Paloma\'s Orrery -- Updated: January 26, 2026")\n',
      'root.title("Paloma\'s Orrery -- Updated: January 26, 2026")\n\n# The background of the control panels, frames and buttons: one name\n# for every site (L-027). gray90 is a colour name Tk knows on Windows,\n# macOS and Linux alike. The Windows-only name SystemButtonFace stops\n# Tk on Linux with "unknown color name", so the window never opens.\n# gray90 was Tony\'s fix of 2026-01-09, tested then on all three\n# systems; a test colour swap undid it on 2026-06-12, and L-027\n# restored it here on 2026-10-06.\nPANEL_BG = \'gray90\'\n',
      1),
    ('the 23 SystemButtonFace sites use PANEL_BG',
      "'SystemButtonFace'",
      'PANEL_BG',
      23),
  ],
  'skills/agentic-pre-test/SKILL.md': [
    ('description: the throwaway rule, unnamed',
      'Covers py_compile, the xvfb headless GUI run, the SystemButtonFace throwaway-copy rule, and the live-dispatch smoke test.',
      'Covers py_compile, the xvfb headless GUI run, the throwaway-copy rule, and the live-dispatch smoke test.',
      1),
    ('v1.3 entry',
      'Skill version: 1.2 | Cut from palomas_orrery @ 3398970 | 2026-08-05\n',
      "Skill version: 1.3 | 2026-10-06, with Anthropic's Claude Opus 5.5, at\npalomas_orrery @ 51436054. v1.3 (L-027) drops the colour swap from the\nStandard Test. palomas_orrery.py now names its panel colour once,\nPANEL_BG = 'gray90', which Tk knows on every system, so the headless\nrun needs no edit to the copy, and it now fails if a Windows-only\ncolour name comes back. The throwaway rule stays, with its true\nfounding case.\nEarlier: 1.2 | Cut from palomas_orrery @ 3398970 | 2026-08-05\n",
      1),
    ('Standard Test without the swap',
      'cp palomas_orrery.py _pretest_throwaway.py\nsed -i "s/SystemButtonFace/gray90/g" _pretest_throwaway.py\ntimeout 30 xvfb-run -a python3 _pretest_throwaway.py 2>&1 | head -50\nrm _pretest_throwaway.py\n```\n',
      'cp palomas_orrery.py _pretest_throwaway.py\ntimeout 30 xvfb-run -a python3 _pretest_throwaway.py 2>&1 | head -50\nrm _pretest_throwaway.py\n```\n\nThe copy is run as it is, with no edit. The orrery is cross-platform\n(Tony, 2026-10-06: "We should not have any windows only\nrequirements."), so if this run stops with `unknown color name`, or\nwith any error naming something only one system has, that is a\nfinding in the deliverable. Fix it there and report it. Never edit\nthe copy to get past such an error: that turns a check that found the\nbug into one that cannot.\n',
      1),
    ('the throwaway section, with its true founding case',
      "## [CRITICAL] Swap on a THROWAWAY copy; never restore-in-place\n\nThe SystemButtonFace<->gray90 sed round trip is NOT idempotent:\npalomas_orrery.py contains many SystemButtonFace literals and 0 native\ngray90, so the test swap yields gray90 literals indistinguishable from\nNATIVE gray90 -- which DOES exist in sibling GUI files\n(star_visualization_gui.py has 5, earth_system_visualization_gui.py has 3\nat the time of writing). A gray90->SystemButtonFace restore therefore\ncannot tell converted from legitimate values; run it on the wrong file, or\nafter the counts drift, and it silently corrupts the deliverable. Test on a\ncopy, discard the copy; the deliverable is never edited by the pre-test.\n(Caught June 9, 2026; practice every session since.)\n\nBackground: SystemButtonFace is a Tk color name that resolves on Windows\nbut not Linux/macOS. The sed swap is a test workaround, not a fix; the\nreal fix (out of pre-test scope) is a hex literal ('#F0F0F0'), platform\ndetection, or ttk styling.\n\n",
      '## [CRITICAL] The pre-test never edits the deliverable\n\nAnything a test changes in code to make it run headless (a mainloop\npatched to a no-op, a network call stubbed) is changed on a throwaway\ncopy, and the copy is discarded. Never undo a test change in place on\nthe deliverable: an undo cannot tell the values the test put there\nfrom the ones that were there already.\n\nThe founding case, as the file history shows it (corrected\n2026-10-06, L-027). Tony\'s commit dff2d03 of 2026-01-09,\n"cross-platform refactor", replaced every SystemButtonFace in\npalomas_orrery.py with gray90, and he tested the orrery on Linux and\nmacOS while it held. The pre-test swapped SystemButtonFace to gray90\non a copy so the file would run headless, and swapping back\nafterwards, in place, was the known risk: on 2026-06-09 L-003\nrecorded the rule against it. On 2026-06-12 commit ec333df, "animation\nrefactor phase 4", changed all 26 gray90 in the file to\nSystemButtonFace: exactly that restore, on the real file. From then on\nthe damaged file was read as the original. L-027 opened on 2026-06-18\ncalling SystemButtonFace the starting state, and this skill at 1.1\n(L-115, 2026-07-12) rewrote this paragraph to fit the damaged file.\nThe orrery could not open its window on Linux for four\nmonths.\n\nThe swap also hid the bug. Every headless run passed, because the\ntest removed from the copy the one thing that stopped Linux. A test\nworkaround that edits the thing under test can leave the test unable\nto fail on exactly what it edited -- the resident gate A Check That\nCannot Fail Is Not Passing, from the other side.\n\nSince L-027 the colour is one name, PANEL_BG = \'gray90\', defined just\nafter the root window, so no swap is needed and a future one would\nhave a single line to change.\n\n',
      1),
  ],
  'PROJECT_INSTRUCTIONS.md': [
    ('header stamp',
      'Tony Quintanilla, PE | Claude | v3.82 | October 5, 2026\n',
      'Tony Quintanilla, PE | Claude | v3.83 | October 6, 2026\n',
      1),
    ('SHA anchor',
      'Cut from d9f47a87 at https://github.com/tonylquintanilla/palomas_orrery\n',
      'Cut from 51436054 at https://github.com/tonylquintanilla/palomas_orrery\n',
      1),
    ('v3.83 entry',
      'v3.82 (October 5, 2026): No rule changed in this document. ONE\n',
      'v3.83 (October 6, 2026): No rule changed in this document. ONE\nskill bump, one version (L-027): agentic-pre-test 1.2 -> 1.3. THE\nPRE-TEST RUNS THE FILE AS IT IS.\n\nWHAT PROMPTED IT. A session reported that the maintenance run\'s Reset\ncompleteness check fails in the sandbox because it needs a screen\ncolour only Windows has. Tony: "We should not have any windows only\nrequirements. This is a cross platform project." The file history\nshowed it was a regression, not the starting state: Tony\'s commit of\n2026-01-09 had replaced the Windows-only Tk colour name\nSystemButtonFace with gray90, and commit ec333df of 2026-06-12 swapped\nall 26 back -- the reverse of the pre-test\'s own colour swap, applied\nto the real file. Since then the orrery\'s window could not open on\nLinux, and every headless run passed because the test swapped the\ncolour out of its copy first.\n\nWHAT CHANGED. patch_L027_1 names the colour once in palomas_orrery.py,\nPANEL_BG = \'gray90\', at all 23 sites. agentic-pre-test 1.3 drops the\nswap: the headless run uses an unedited copy, and an error naming\nsomething only one system has is a finding to fix, never to swap past.\nIts throwaway rule keeps its place, with the founding case as the\nhistory shows it. Tony, on the colour: "Confirmed as recommended. And\nshould we improve the skill also?"\n\nTHE OBLIGATION TRAVELS. A reinstall during a session is not visible to\nthat session. The next session confirms its loaded copy reads\nagentic-pre-test 1.3 before any pre-test.\n\nThe header stamp and the SHA anchor move with this entry.\n\nVersion history: v3.80 moves down to\ndocumentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\nresident.\n\nv3.82 (October 5, 2026): No rule changed in this document. ONE\n',
      1),
    ('v3.80 moves down',
      'v3.80 (October 4, 2026): No rule changed in this document. ONE\nskill bump, one version (L-415): safe-file-editing 1.11 -> 1.12. A\nPATCH WRITES LF AND SAYS SO.\n\nWHAT PROMPTED IT. A ledger patch\'s test notes said a CRLF copy of the\nledger kept its CRLF. Tony: "why do we leave windows line endings\nuncorrected. I thought the rule was to convert to lf when found and\nreport." The skill said both: Fix In Passing lists CRLF as a violation\nto fix, while Line Endings Are Not Content and Compare Content, Not\nBytes said to write each file back in the style found, because\nflipping the endings shows every line changed.\n\nWHAT THE TEST SHOWED. Under `* text=auto eol=lf`, which both repos\ncarry, that reason is false: a CRLF working copy shows as modified with\nnothing inside it, and writing it LF clears the mark. The reason holds\nonly for a file committed CRLF before the rule existed; 22 such files\nremain, named on L-133.\n\nWHAT THE SKILL NOW SAYS. A patch writes LF and reports a file that\narrived CRLF. A file committed CRLF keeps its endings, is named, and\nwaits for L-133\'s one-commit sweep. Patches and generators now follow\nthe same convention.\n\nTHE OBLIGATION TRAVELS. This session loaded 1.11. The next session\nconfirms its loaded copy reads safe-file-editing 1.12 before any patch\nwork.\n\nThe header stamp and the SHA anchor move with this entry.\n\nVersion history: v3.77 moves down to\ndocumentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\nresident.\n\n',
      '',
      1),
  ],
  'documentation/PROJECT_INSTRUCTIONS_HISTORY.md': [
    ('receives v3.80',
      '================================================================\nPART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37\n',
      'v3.80 (October 4, 2026): No rule changed in this document. ONE\nskill bump, one version (L-415): safe-file-editing 1.11 -> 1.12. A\nPATCH WRITES LF AND SAYS SO.\n\nWHAT PROMPTED IT. A ledger patch\'s test notes said a CRLF copy of the\nledger kept its CRLF. Tony: "why do we leave windows line endings\nuncorrected. I thought the rule was to convert to lf when found and\nreport." The skill said both: Fix In Passing lists CRLF as a violation\nto fix, while Line Endings Are Not Content and Compare Content, Not\nBytes said to write each file back in the style found, because\nflipping the endings shows every line changed.\n\nWHAT THE TEST SHOWED. Under `* text=auto eol=lf`, which both repos\ncarry, that reason is false: a CRLF working copy shows as modified with\nnothing inside it, and writing it LF clears the mark. The reason holds\nonly for a file committed CRLF before the rule existed; 22 such files\nremain, named on L-133.\n\nWHAT THE SKILL NOW SAYS. A patch writes LF and reports a file that\narrived CRLF. A file committed CRLF keeps its endings, is named, and\nwaits for L-133\'s one-commit sweep. Patches and generators now follow\nthe same convention.\n\nTHE OBLIGATION TRAVELS. This session loaded 1.11. The next session\nconfirms its loaded copy reads safe-file-editing 1.12 before any patch\nwork.\n\nThe header stamp and the SHA anchor move with this entry.\n\nVersion history: v3.77 moves down to\ndocumentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\nresident.\n\n(Moved down from the resident protocol on 2026-10-06 when\nv3.83 made a fourth entry.)\n\n================================================================\nPART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37\n',
      1),
  ],
  'LEDGER_CONSOLIDATED.md': [
    ('header stamp',
      "(L-420 built: the galactic plane, its poles and Sgr A* in the orrery;\nSgr A*'s position sourced), built on 51436054.\n",
      "(L-420 built: the galactic plane, its poles and Sgr A* in the orrery;\nSgr A*'s position sourced), built on 51436054.\nModule updated: October 6, 2026 with Anthropic's Claude Opus 5.5\n(L-027 built: the panel colour restored as PANEL_BG = 'gray90';\nagentic-pre-test 1.3, protocol v3.83), built on patch_L420_3's tree\nover 51436054.\n",
      1),
    ('L-027 date',
      '<!-- L:027 status:OPEN upd:2026-06-18 section:D.Structural flag: rice:3/2/75/2 -->\n',
      '<!-- L:027 status:OPEN upd:2026-10-06 section:D.Structural flag: rice:3/2/75/2 -->\n',
      1),
    ('L-027 corrected and built',
      '**Gap:** choose replacement strategy, then sweep. Design decision before\nbuild. Moderate scope (26 sites); low functional risk (cosmetic only).\n',
      '- **Corrected and built, 2026-10-06.** The two lines above were wrong.\n  Not cosmetic: on Linux, Tk stops with `unknown color name\n  "SystemButtonFace"` at the first panel, so the window never opens\n  (checked in the sandbox). And not the starting state. Tony\'s commit\n  dff2d03 of 2026-01-09, "cross-platform refactor", had replaced all\n  22 with `gray90`, and he tested the orrery on Linux and macOS while\n  it held. Commit ec333df of 2026-06-12, "animation refactor phase 4",\n  changed all 26 `gray90` to `SystemButtonFace`: the reverse of the\n  pre-test\'s colour swap, on the real file, three days after L-003\n  recorded the rule against it. This item (2026-06-18) and\n  agentic-pre-test 1.1 (L-115, 2026-07-12) then read the damaged file\n  as the original. The pre-test\'s swap also hid it: every headless run\n  passed because the test removed the colour from its copy first.\n  Tony, 2026-10-06: "We should not have any windows only requirements.\n  This is a cross platform project."; "I did test palomas_orrery.py in\n  both Linux and MacOS but maybe six months ago so it is very stale.";\n  on restoring gray90 as one name, "Confirmed as recommended. And\n  should we improve the skill also?"\n  `patch_L027_1_panel_colour_20261006.py`: palomas_orrery.py defines\n  `PANEL_BG = \'gray90\'` after the root window and uses it at the 23\n  sites; agentic-pre-test 1.3 runs the headless test on an unedited\n  copy and records the founding case as the history shows it;\n  protocol v3.83.\n**Gap:** Tony runs the patch and the maintenance run, looks at the\npanels on Windows (back to the grey of January to June, a shade\ndarker than Windows\' own), and reinstalls agentic-pre-test; the next\nsession confirms its loaded copy reads 1.3. A run on a Mac would\nsettle the last system; macOS has not been tried since Tony\'s test.\n**Ref:** commits dff2d03, ec333df; L-003; L-115; L-026;\n`skills/agentic-pre-test/SKILL.md`.\n',
      1),
  ],
  'documentation/HANDOFF_L420_galactic_plane_20261006.md': [
    ('L-027 section',
      '## Tony-actions\n',
      '## Later the same session: L-027, the panel colour\n\n- Tony asked why the maintenance run\'s Reset completeness check fails\n  in the sandbox: "We should not have any windows only requirements.\n  This is a cross platform project."\n- Found: palomas_orrery.py set its panels to `SystemButtonFace`, a\n  colour name only Windows knows, at 23 sites. On Linux the window\n  never opens. The file history shows Tony\'s January fix (`gray90`)\n  was swapped back on 2026-06-12 by commit ec333df, and later records\n  read the damaged file as the original. Full account on L-027.\n- Built: `patch_L027_1_panel_colour_20261006.py`. `PANEL_BG = \'gray90\'`\n  defined once, used at the 23 sites; agentic-pre-test 1.3 drops the\n  colour swap from the headless test; protocol v3.83, with v3.80\n  moved to the history file.\n- Verified on a copy with both L-420 patches run first: the window\n  starts headless with no swap; the maintenance run passes every\n  checker, Reset completeness included, for the first time in the\n  sandbox; the skill headers check passes; a second run refuses.\n- Obligation: agentic-pre-test went to 1.3 at the commit Tony makes;\n  this session loaded 1.2; the next session confirms its loaded copy\n  reads 1.3 before any pre-test.\n- Running beside the other sessions: this patch also edits\n  PROJECT_INSTRUCTIONS.md. If another session lands a v3.83 first,\n  this patch refuses at the header line and writes nothing; it then\n  needs rebuilding on the new protocol.\n\n## Tony-actions\n',
      1),
    ('L-027 Where We Are lines',
      '- Road: not a stage of its own; an orrery item done between stages.\n- Details: L-420.\n',
      '- Road: not a stage of its own; an orrery item done between stages.\n- Details: L-420.\n- Changed: the desktop orrery opens on Linux and macOS again. Its\n  panels use one grey, gray90, that every system knows (L-027).\n- Needs Tony: a look at the panels on Windows, a shade darker than\n  before; and, when convenient, a run on a Mac.\n',
      1),
    ('L-027 Tony-actions',
      '5. Plot with Star Background, Celestial Grid and Labels on, and look:\n   the violet colour, the marker sizes, where the labels sit.\n',
      "5. Plot with Star Background, Celestial Grid and Labels on, and look:\n   the violet colour, the marker sizes, where the labels sit.\n6. After steps 1 and 2, run `patch_L027_1_panel_colour_20261006.py`\n   the same way, then the maintenance run again. Every checker should\n   pass.\n7. Look at the panels: a shade darker grey than before, the grey of\n   January to June.\n8. Move the script into `documentation/`, commit and push with the\n   others.\n9. Reinstall agentic-pre-test in Settings > Skills, and replace the\n   Project's instructions with PROJECT_INSTRUCTIONS.md (v3.83).\n",
      1),
    ('L-027 next session',
      "- Close L-420 on Tony's look, or adjust what he names.\n- Nothing else is opened by this session.\n",
      "- Close L-420 on Tony's look, or adjust what he names.\n- Close L-027 on Tony's run and look; confirm agentic-pre-test 1.3\n  loaded.\n- Nothing else is opened by this session.\n",
      1),
  ],
}


def md5(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def read_lf(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    return raw.decode("utf-8").replace("\r\n", "\n"), b"\r\n" in raw


def outside_zone(path, text):
    if path not in ZONED:
        return text
    start, end = ZONED[path]
    a = text.index(start)
    b = text.index(end) + len(end)
    return text[:a] + text[b:]


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the repo ROOT, not from "
                         "documentation/. NOTHING was written.")
    for marker in ROOT_MARKERS:
        if not os.path.isfile(marker):
            raise SystemExit("ERROR: %s is not here, so this is not the %s "
                             "root. NOTHING was written." % (marker, REPO))
    results = []
    for path in sorted(EDITS):
        if not os.path.isfile(path):
            raise SystemExit("ERROR: %s is not here. Run patch_L420_3 first. "
                             "NOTHING was written." % path)
        text, was_crlf = read_lf(path)
        if path not in ANCHOR_ONLY and md5(outside_zone(path, text)) != BASE[path]:
            raise SystemExit(
                "ERROR: %s is not the file this patch was built against\n"
                "       (51436054 after patch_L420_2 and patch_L420_3), or\n"
                "       this patch has already run. Have both L-420 patches\n"
                "       run? (Line endings are excluded, so they are not the\n"
                "       cause.) NOTHING was written." % path)
        done = []
        for label, old, new, want in EDITS[path]:
            found = text.count(old)
            if found != want:
                hint = (" Has patch_L420_3 run? Or has this patch already run?"
                        if path in ANCHOR_ONLY else "")
                raise SystemExit("ANCHOR FAIL (%s): expected %d match(es) in "
                                 "%s, found %d.%s NOTHING was written."
                                 % (label, want, path, found, hint))
            text = text.replace(old, new)
            done.append(label)
        results.append((path, text, done, was_crlf))
    for path, text, done, was_crlf in results:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in done:
            print("ok  %-48s %s" % (path, label))
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % path)
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    for line in NEXT:
        print("  " + line)


if __name__ == "__main__":
    main()
