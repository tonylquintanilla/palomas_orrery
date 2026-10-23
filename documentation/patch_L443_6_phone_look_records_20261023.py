r"""patch_L443_6_phone_look_records_20261023.py -- the records of Tony's
phone look of slice 1: L-472 (the view fix), L-473 (groups open
unticked), L-474 (See more on top) and L-475 (the About link), new;
L-443 and L-470 updated; Where We Are says the look is done.

RUN COMMAND
    python patch_L443_6_phone_look_records_20261023.py

Save it in the ORRERY repository's root folder
(C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\),
open it in VS Code and click Run. Then move it to documentation/,
commit and push. No maintenance run is needed; the next one adds the
four new items to the ledger's index.

Built on orrery ee4e333176f6fb0de69c371926557b789a121a79 at
https://github.com/tonylquintanilla/palomas_orrery (branch main), with
gallery 25e4d24228a191622df68b447f519782162977ea at
https://github.com/tonylquintanilla/tonyquintanilla.github.io read for
the signals. Final as delivered: nothing will replace it.

WHAT IT CHANGES (records only; no code)
    LEDGER_CONSOLIDATED.md      header stamp; L-472 to L-475, new; L-443,
                                the phone look done and a new Gap; L-470,
                                the Gonggong discussion still owed
    documentation/WHERE_WE_ARE.md  by section: header, box, the road's
                                stage 10-11, Signals, Waiting on you,
                                Where the details are; the marks reset.
                                The run-record zone is not touched

Each file is checked only at the lines this patch edits, so notes you
have added elsewhere do not stop it.

SUCCESS prints one "ok" line per file, then "patch applied".
FAILURE prints one FAILURE line, and NOTHING is written; undo is
Discard Changes in GitHub Desktop.

Written October 23, 2026 with Anthropic's Claude Opus 5.5.

Role: devtool
Domain: dev_tools
"""

import os
import sys

TITLE = 'L-443 phone look records'
FILES = [
    {"path": 'LEDGER_CONSOLIDATED.md', "edits": [
        (b"d7195704 with the day's patches.\nReview and RICE update Tony 6-21-2026\n",
         b"d7195704 with the day's patches.\nModule updated: October 23, 2026 with Anthropic's Claude Opus 5.5 (the\nrecords of Tony's phone look of slice 1: L-472 new, the view fix;\nL-473, L-474 and L-475 new, the three drawer and panel changes; L-443\nand L-470 updated), built on ee4e333 and gallery 25e4d24.\nReview and RICE update Tony 6-21-2026\n"),
        (b'\n#### [L-471] A delivered patch is final (safe-file-editing, next version)\n',
         b'\n#### [L-475] The About link at the bottom of every room\'s i panel (gallery, the rooms\' shared chrome)\n<!-- L:475 status:OPEN upd:2026-10-23 section:A flag: rice: -->\n- **Found 2026-10-22, Tony\'s phone look of slice 1 (L-443 (the objects\n  to the website)), checklist item 2**\n  (`documentation/WHERE_WE_ARE_10-22-26_2027_run_record.md`). Tony: "i\n  cannot find the link to the "about" page that one accesses by tapping\n  the i button on the front page, the lobby. this should be on every\n  info panel at the bottom."\n- **What the code says, read at gallery b93072eb (not run).** The About\n  card is the lobby\'s: index.html\'s `.about-overlay`, opened by its\n  `.footer-about-btn`. interactive.html has no link to it. The lobby\'s\n  address routes (`#room=`) open rooms, not the card, so the link needs\n  an address that opens it.\n- An edit to the rooms\' shared i panel, so one line serves every room\n  (interactive-exhibit, One chrome, many rooms); every room is a Mode 5\n  target.\n**Gap:** an address that opens the About card; the link at the bottom\nof the i panel; Tony\'s look on the phone.\n**Ref:** L-443; L-458 (report a problem: another line for the same\npanel); gallery `index.html`, `interactive.html` (`renderSunInfo`).\n\n#### [L-474] See more / See fewer at the top of the Solar System room\'s drawer (gallery, the drawer)\n<!-- L:474 status:OPEN upd:2026-10-23 section:A flag: rice: -->\n- **Found 2026-10-22, after Tony\'s phone look of slice 1.** His note of\n  that night, as Claude worded it in the run record\n  (`documentation/WHERE_WE_ARE_10-22-26_2027_run_record.md`): "Move See\n  more / See fewer to the top of the drawer, where it\'s easier to find."\n- Today the button sits between the ticked rows and the rest\n  (interactive.html near line 4873, read at gallery b93072eb).\n- Mode 5: Claude builds it, Tony judges it on the phone.\n**Gap:** the build, with L-472 (the view fix) or before it (Tony\'s\ncall); Tony\'s look.\n**Ref:** L-443; gallery `interactive.html` (`renderSunDrawer`),\n`gallery/solar_system_drawer.js`.\n\n#### [L-473] A group in the Solar System room\'s drawer opens with its bodies unticked (gallery, the drawer)\n<!-- L:473 status:OPEN upd:2026-10-23 section:A flag: rice: -->\n- **Found 2026-10-22, Tony\'s phone look of slice 1, checklist item 4**\n  (`documentation/WHERE_WE_ARE_10-22-26_2027_run_record.md`). Tony: "i\n  think that when we open a group the specific checkboxes should be off\n  not on by default. let the user select the bodies to plot. if they\n  want all they can do that from the none/all button. the same should\n  apply to all groups, just as we ask the user to tap see more to see\n  all the special groups."\n- **What the code says, read at gallery b93072eb (not run).** `ssFold`\n  only folds the group and redraws the drawer; the comment above\n  `ssGroupTick` says a group\'s name "folds it open or shut, and moves\n  nothing." A group\'s bodies are ticked only from its row\'s box (the\n  `.pick` span) or its "All / none in <label>" button. So either the\n  tap landed on the box rather than the name, or the phone ticks on\n  folding in a way the code reading does not show.\n**Gap:** settle which on the phone before any code. If the tap target\nis the cause, the fix may be the row\'s layout rather than its logic.\nThen the build, with L-472 (the view fix) or before it (Tony\'s call).\n**Ref:** L-443; gallery `interactive.html` (`ssFold`, `ssGroupTick`),\n`gallery/solar_system_drawer.js`; interactive-exhibit 1.21, Groups fold\nopen.\n\n#### [L-472] The Solar System room\'s view: a far body drawn in the wrong place when zoomed in (gallery, the Solar System room)\n<!-- L:472 status:OPEN upd:2026-10-23 section:A flag: rice: -->\n- **Found 2026-10-22, Tony\'s phone look of slice 1 (L-443 (the objects\n  to the website)), checklist item 9**\n  (`documentation/WHERE_WE_ARE_10-22-26_2027_run_record.md`). Tony: "the\n  orbit of Halley does not look correct. for "now" halley is near its\n  apohelion but the render makes it look like it is near perihelion\n  approaching the orbit of mars. that\'s not right for today\'s date."\n  His screenshot was at a 1 AU grid. Halley was 35.01 AU from the Sun\n  (coverage_index.json, the Oct 22 build). The session that night found\n  the position right whenever the box holds Halley, as it does with\n  Neptune\'s orbit drawn, and wrong only when the box is smaller than\n  Halley\'s distance.\n- **The rule, as recorded that night,** in Claude\'s words in the run\n  record, from Tony\'s notes: "Always size the view to the farthest\n  orbit of anything ticked, so a far body is never drawn outside the\n  box." Claude then proposed a second part: "zooming moves the camera\n  closer and never shrinks the box below what it has to hold." The\n  second part is Claude\'s proposal; the design talk confirms or changes\n  it.\n- **What the code says, read at gallery b93072eb (not run).** Ticking\n  already frames on the farthest body ticked: `ssTick` and\n  `ssGroupTick` in interactive.html end in `sunApplyVisibility(true,\n  sunOutermostShown())`, and the room\'s row carries `frameOnPosition:\n  true, frameMargin: 1.2`. The zoom buttons are the other half:\n  `navFrameZoom` shrinks the axis range by 1.6 a tap, floored at 1e-5\n  AU, with nothing to stop it below a ticked body\'s distance.\n  `gallery/far_lines.js` (L-463 (the pink band)) cuts a LINE whose far\n  point lies more than 20 half-widths out, because a phone\'s graphics\n  chip draws such points in the wrong place; its header says "Markers\n  are not touched." Halley\'s marker at 35 AU in a 1 AU box is 35\n  half-widths out. The likeliest cause is L-463\'s failure again, for a\n  marker: a hypothesis for the phone test, not a finding.\n- **Two rulings to reconcile before code.** Tony\'s ruling of\n  2026-09-03, in `navFrameZoom`\'s comment: "+/- step the FRAME, not the\n  camera", so the Sun room\'s shells stay readable across six decades.\n  The rule above has the Solar System room\'s zoom move the camera.\n  Three shapes for the talk, none recommended (the brief, sec. 4): A,\n  per room, a floor under the Solar System room\'s zoom-in; B, frame\n  zoom down to that floor, then the camera; C, a far marker treated as\n  far_lines.js treats a far line, the HUD counting ticked bodies out of\n  view.\n- **The phone test before any code,** whichever shape wins: tick Halley\n  with Neptune drawn and confirm it sits at 35 AU; zoom in by the\n  buttons to a 1 AU grid and watch where Halley\'s marker goes, and\n  whether the visible part of its orbit is the perihelion end cut at\n  the box. The three cases Claude listed that night: tick a far body\n  without Go To; Go To Halley, then zoom in on Earth step by step; zoom\n  in very far with a far body ticked and watch whether its dot jumps.\n**Gap:** the design talk (which shape, and whether the rule is per\nroom), the phone test, then the build. Slice 2 of L-443 waits behind\nit, since slice 2 adds the far bodies this bug mis-draws.\n**Ref:** L-443; L-463; `documentation/HANDOFF_L443_view_and_drawer_brief_20261023.md`,\nsecs. 3 and 4; gallery `interactive.html` (`navFrameZoom`, `ssTick`,\n`ssGroupTick`), `gallery/far_lines.js`.\n\n#### [L-471] A delivered patch is final (safe-file-editing, next version)\n'),
        (b'<!-- L:470 status:OPEN upd:2026-10-22 section:A flag: rice: -->',
         b'<!-- L:470 status:OPEN upd:2026-10-23 section:A flag: rice: -->'),
        (b'**Gap (replaces the one below, 2026-10-22, evening):** the Gonggong test,\n',
         b'- **2026-10-23: the discussion is still owed.** Tony\'s phone-look note\n  of 2026-10-22, "Gonggong skipped but needs discussion", stands on\n  Where We Are\'s design-talk list. Not part of the view fix\n  (`documentation/HANDOFF_L443_view_and_drawer_brief_20261023.md`,\n  sec. 3, item 5).\n**Gap (replaces the one below, 2026-10-22, evening):** the Gonggong test,\n'),
        (b"**Gap (replaces the one below, 2026-10-22, 22:50):** Tony's phone look\n(the handoff, sec. 10); then slice 2, the spacecraft and the\nopen-path comets.\n",
         b'- **2026-10-22, night: Tony\'s phone look done.** His answers are in\n  `documentation/WHERE_WE_ARE_10-22-26_2027_run_record.md`. Items 1,\n  3, 5, 6, 7, 8 and 10 a plain yes. Item 9 found Halley drawn in the\n  wrong place when zoomed in: L-472 (the view fix). Item 4: a group\n  should open with its bodies unticked, L-473. Item 2: the About link\n  missing from the i panels, L-475. A later note: See more / See\n  fewer at the top of the drawer, L-474. And "Gonggong skipped but\n  needs discussion", on L-470.\n**Gap (replaces the one below, 2026-10-23):** the view fix first\n(L-472), with the three drawer and panel changes (L-473, L-474,\nL-475); then slice 2, the spacecraft and the open-path comets.\n**Gap (superseded above):** Tony\'s phone look\n(the handoff, sec. 10); then slice 2, the spacecraft and the\nopen-path comets.\n'),
    ]},
    {"path": 'documentation/WHERE_WE_ARE.md', "edits": [
        (b'Last updated: October 22, 2026, late evening: slice 1 is live, 50\nbodies in folding groups.\n- Written at orrery f10e859 and gallery b93072e, with patch 5.\n',
         b'Last updated: October 23, 2026: your phone look is done; the view fix\ncomes before slice 2.\n- Written at orrery ee4e333 and gallery 25e4d24, with patch 6.\n'),
        (b"> - Slice 1 of L-443 (the objects to the website) is live: 50 bodies,\n>   in six groups that fold open in the drawer.\n> - The website's check caught one wrong figure count, 2025 PN7's\n>   period; the fix is the orrery's, in patch 4.\n> - The method for choosing JPL's records is in a skill now.\n>\n> **Do next:** *your phone look (the handoff, sec. 10); then slice 2,\n> the spacecraft and the comets on open paths.*\n>\n> **Needs you now:**\n> - *(do) Your phone look (the handoff, sec. 10).*\n",
         b'> - Your phone look is done. Halley is drawn in the wrong place when\n>   the view is zoomed in (L-472 (the view fix)); that is fixed\n>   before slice 2.\n> - Three smaller changes: L-473 (groups open unticked), L-474 (See\n>   more on top), L-475 (the About link in every i panel).\n>\n> **Do next:** *the view design talk: how the zoom buttons work in\n> the Solar System room; then one test on your phone.*\n>\n> **Needs you now:**\n> - *(do) Run patch 6, then commit and push.*\n'),
        (b"- A citation's web address goes on its own Source line. Links checked\n  every 30 days. Problem reports through the guest book's form. (Oct 20)\n",
         b''),
        (b'## Deferred  **>> UPDATED THIS SESSION**\n',
         b'## Deferred\n'),
        (b" 10-11.[NOW]   *The orrery's objects come to the website (L-443 (the\n               objects to the website)): slice 1, 50 bodies, built Oct 22;\n               next, slice 2, the spacecraft and the comets on open paths;\n               then the moons.* The bare link opens the room. << moved this session\n",
         b" 10-11.[NOW]   *The orrery's objects come to the website (L-443 (the\n               objects to the website)): slice 1, 50 bodies, live Oct 22;\n               the view fix first; then slice 2, the spacecraft and the\n               comets on open paths; then the moons.* << moved this session\n"),
        (b'- Last cache build: 20261023T032713Z, ok, first try (gallery\n  b93072e).\n',
         b'- Last cache build: 20261023T165105Z, ok, first try (gallery\n  25e4d24).\n'),
        (b"- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md after the\n  day's orrery patches).",
         b'- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md at orrery\n  ee4e333).'),
        (b"- This page's date and the ledger's newest stamp: both Oct 22. Agree.\n",
         b"- This page's date and the ledger's newest stamp: both Oct 23. Agree.\n"),
        (b'At the next design talk:\n- "Gonggong skipped but needs discussion"',
         b'At the next design talk:\n- *The view fix (L-472 (the view fix)): which of three shapes, and\n  whether the zoom rule differs by room (the brief, sec. 4).*\n- Whether the three smaller changes go with it, or first.\n- "Gonggong skipped but needs discussion"'),
        (b'- *Next: `HANDOFF_L443_slice1_build_20261022.md`, sec. 9.*\n',
         b'- *Next: `HANDOFF_L443_view_and_drawer_brief_20261023.md`, sec. 4.*\n- Your phone look: `WHERE_WE_ARE_10-22-26_2027_run_record.md`\n'),
        (b'- Drawn ends: `DISCOVERY_drawn_ends_20261021.md`; drawer: gallery `DRAWER_ORDER_L460_*`\n',
         b''),
    ]},
]


def fail(msg):
    print("FAILURE: " + msg)
    print("NOTHING was written. Undo is Discard Changes in GitHub Desktop.")
    sys.exit(1)


def main():
    root = os.getcwd()
    plan = []
    for f in FILES:
        path = os.path.join(root, f["path"])
        if not os.path.exists(path):
            fail("%s not found. Run this from the orrery repository's root "
                 "folder" % f["path"])
        raw = open(path, "rb").read()
        crlf = b"\r\n" in raw
        lf = raw.replace(b"\r\n", b"\n")
        if all(lf.count(new) == 1 and lf.count(old) == 0
               for old, new in f["edits"]):
            fail("%s already carries this patch's edits; it has run "
                 "before" % f["path"])
        spots = []
        for k, (old, new) in enumerate(f["edits"]):
            n = lf.count(old)
            if n != 1:
                fail("ANCHOR FAIL in %s, edit %d: expected 1 match, found %d: %r"
                     % (f["path"], k + 1, n, old[:70]))
            spots.append((lf.index(old), old, new))
        spots.sort()
        out, last = b"", 0
        for i, old, new in spots:
            if i < last:
                fail("%s: two edits overlap" % f["path"])
            out += lf[last:i] + new
            last = i + len(old)
        out += lf[last:]
        try:
            out.decode("ascii")
        except UnicodeDecodeError:
            fail("%s would hold a non-ASCII byte after the edits" % f["path"])
        plan.append((f, path, out, crlf))
    for f, path, out, crlf in plan:
        open(path, "wb").write(out)
        print("ok  %s (%d edits%s)" % (f["path"], len(f["edits"]),
                                    "; it was CRLF in the working copy, written LF" if crlf else ""))
    print("patch applied: %s (%d files)" % (TITLE, len(plan)))


if __name__ == "__main__":
    main()
