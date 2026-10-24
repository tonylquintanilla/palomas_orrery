r"""patch_L472_2_records_20261023.py -- the records of the view design
talk: L-472 (nothing drawn wrong; Tony's ruling, the count line; built),
L-474 and L-475 (built), L-473 (parked), L-443's Gap, and Where We Are.

RUN COMMAND
    python patch_L472_2_records_20261023.py

Save it in the ORRERY repository's root folder
(C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\),
open it in VS Code and click Run. Then move it to documentation/,
commit and push. No maintenance run is needed.

It is patch 2 of 2. Patch 1, patch_L472_1_view_drawer_panel_20261023.py,
is the website's; the two can run in either order.

Built on orrery b90d895a4ef1cdc31daec7a20fef8c34369fa24c at
https://github.com/tonylquintanilla/palomas_orrery (branch main), with
gallery 25e4d24228a191622df68b447f519782162977ea at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Final as
delivered: nothing will replace it.

WHAT IT CHANGES (records only; no code)
    LEDGER_CONSOLIDATED.md      header stamp; L-472, the day's test, the
                                ruling and the build; L-474 and L-475,
                                built; L-473, PARKED on Tony's word; L-443,
                                its Gap
    documentation/WHERE_WE_ARE.md  by section: header, box, the road's
                                stage 10-11, Settled (the day's ruling in,
                                the Oct 21 line out for the length cap),
                                Waiting on you, Where the details are; the
                                marks reset. The run-record zone is not
                                touched

Each file is checked only at the lines this patch edits.

SUCCESS prints one "ok" line per file, then "patch applied".
FAILURE prints one FAILURE line, and NOTHING is written; undo is
Discard Changes in GitHub Desktop.

Written October 23, 2026 with Anthropic's Claude Opus 5.5.

Role: devtool
Domain: dev_tools
"""

import os
import sys

TITLE = 'L-472 records'
FILES = [
    {"path": 'LEDGER_CONSOLIDATED.md', "edits": [
        (b'L-473, L-474 and L-475 new, the three drawer and panel changes; L-443\nand L-470 updated), built on ee4e333 and gallery 25e4d24.\nReview and RICE update Tony 6-21-2026\n\n',
         b"L-473, L-474 and L-475 new, the three drawer and panel changes; L-443\nand L-470 updated), built on ee4e333 and gallery 25e4d24.\nModule updated: October 23, 2026, afternoon, with Anthropic's Claude Opus\n5.5 (the view design talk: L-472, nothing drawn wrong, Tony's ruling the\ncount line, built with L-474 and L-475 in gallery patch_L472_1; L-473\nparked; L-443's Gap), built on b90d895 and gallery 25e4d24.\nReview and RICE update Tony 6-21-2026\n\n"),
        (b"  (interactive-exhibit, One chrome, many rooms); every room is a Mode 5\n  target.\n**Gap:** an address that opens the About card; the link at the bottom\nof the i panel; Tony's look on the phone.\n**Ref:** L-443; L-458 (report a problem: another line for the same\n",
         b'  (interactive-exhibit, One chrome, many rooms); every room is a Mode 5\n  target.\n- **2026-10-23: built,** words approved ("yes, please"): the last line\n  of every room\'s i panel, the Explorer\'s too, reads "About Paloma\'s\n  Orrery" and links to index.html#about, which opens the lobby with\n  its About card showing; closing the card goes back to the lobby\'s\n  own address. Gallery `patch_L472_1_view_drawer_panel_20261023.py`;\n  `mountAboutLink` in interactive.html. The Sun and Earth rooms were\n  driven headlessly in the old page and the new: identical but for the\n  panel\'s 21 added characters.\n**Gap (replaces the one below, 2026-10-23):** Tony\'s runs and push of\npatch_L472_1, then his look on the phone.\n**Gap (superseded above):** an address that opens the About card; the link at the bottom\nof the i panel; Tony\'s look on the phone.\n**Ref:** L-443; L-458 (report a problem: another line for the same\n'),
        (b"  (interactive.html near line 4873, read at gallery b93072eb).\n- Mode 5: Claude builds it, Tony judges it on the phone.\n**Gap:** the build, with L-472 (the view fix) or before it (Tony's\ncall); Tony's look.\n**Ref:** L-443; gallery `interactive.html` (`renderSunDrawer`),\n",
         b'  (interactive.html near line 4873, read at gallery b93072eb).\n- Mode 5: Claude builds it, Tony judges it on the phone.\n- **2026-10-23: built,** riding with L-472 by Tony\'s word ("yes,\n  please"): See more / See fewer is the first item of the room\'s\n  drawer list (`ssAddSeeMore`). Gallery\n  `patch_L472_1_view_drawer_panel_20261023.py`.\n**Gap (replaces the one below, 2026-10-23):** Tony\'s runs and push,\nthen his look on the phone.\n**Gap (superseded above):** the build, with L-472 (the view fix) or before it (Tony\'s\ncall); Tony\'s look.\n**Ref:** L-443; gallery `interactive.html` (`renderSunDrawer`),\n'),
        (b'\n#### [L-473] A group in the Solar System room\'s drawer opens with its bodies unticked (gallery, the drawer)\n<!-- L:473 status:OPEN upd:2026-10-23 section:A flag: rice: -->\n- **Found 2026-10-22, Tony\'s phone look of slice 1, checklist item 4**\n  (`documentation/WHERE_WE_ARE_10-22-26_2027_run_record.md`). Tony: "i\n',
         b'\n#### [L-473] A group in the Solar System room\'s drawer opens with its bodies unticked (gallery, the drawer)\n<!-- L:473 status:PARKED upd:2026-10-23 section:A flag: rice: -->\n- **Found 2026-10-22, Tony\'s phone look of slice 1, checklist item 4**\n  (`documentation/WHERE_WE_ARE_10-22-26_2027_run_record.md`). Tony: "i\n'),
        (b"  tap landed on the box rather than the name, or the phone ticks on\n  folding in a way the code reading does not show.\n**Gap:** settle which on the phone before any code. If the tap target\nis the cause, the fix may be the row's layout rather than its logic.\nThen the build, with L-472 (the view fix) or before it (Tony's call).\n",
         b'  tap landed on the box rather than the name, or the phone ticks on\n  folding in a way the code reading does not show.\n- **2026-10-23: the drawer already does this.** Asked whether, at the\n  day\'s test, all 13 comet boxes were empty until he ticked Halley,\n  Tony: "yes". So the tap of Oct 22 most likely landed on the group\n  row\'s box. Tony: "let\'s let this go for now. if the problem recurs,\n  we can address it." Parked; nothing built.\n**Gap (replaces the one below, 2026-10-23):** none while parked. If it\nhappens again, the row\'s box and name made harder to confuse.\n**Gap (superseded above):** settle which on the phone before any code. If the tap target\nis the cause, the fix may be the row\'s layout rather than its logic.\nThen the build, with L-472 (the view fix) or before it (Tony\'s call).\n'),
        (b'  without Go To; Go To Halley, then zoom in on Earth step by step; zoom\n  in very far with a far body ticked and watch whether its dot jumps.\n**Gap:** the design talk (which shape, and whether the rule is per\nroom), the phone test, then the build. Slice 2 of L-443 waits behind\nit, since slice 2 adds the far bodies this bug mis-draws.\n',
         b'  without Go To; Go To Halley, then zoom in on Earth step by step; zoom\n  in very far with a far body ticked and watch whether its dot jumps.\n- **2026-10-23: nothing is drawn wrong.** Tony\'s test of the day\n  (`documentation/WHERE_WE_ARE_10-23-26_1402_run_record.md`): zoomed to\n  a 1 AU grid, the Halley-coloured mark near the inner planets hovers\n  "Halley\'s orbit": the orbit\'s info cross, which render_orbits.build_orbit_traces\n  puts at sweep index 10, ten degrees past perihelion, 0.58 AU from the\n  Sun. Halley itself, 35 AU out, was outside the box. On the desktop:\n  "exactly the same", so the phone\'s graphics chip is not involved\n  (L-463\'s failure ruled out). The orbit\'s near end and its cross,\n  correctly drawn inside a zoomed box, read as the body.\n- **Tony\'s ruling, 2026-10-23.** Offered A (say what is outside), B (the\n  box always holds what is ticked) and C (frame zoom to that floor,\n  then the camera), Claude leaning A: "actually i\'m leaning to, do\n  nothing. with this solution, we could have many objects outside the\n  view and this could get complicated." Offered a line that counts and\n  never names: "The count line. good solution." So zooming stays a\n  cutout in every room, the Sept 3 frame-zoom ruling stands, and the\n  Oct 22 rule\'s second part (Claude\'s proposal, zoom moving the camera)\n  is not adopted.\n- **Built 2026-10-23,** words approved ("yes, please"): in the Solar\n  System room, a line above the grid chip, "1 ticked body is outside\n  this view" or "N ticked bodies are outside this view", hidden at\n  zero, updated at the end of every frame change (`ssOutsideUpdate`,\n  from `sunHudUpdate`); a body is outside when its marker is past the\n  box on any axis (`SolarSystemDrawer.outsideCount`). Gallery\n  `patch_L472_1_view_drawer_panel_20261023.py`, with L-474 and L-475.\n  Checked: the drawer check\'s section 5 with a sixth planted fault; the\n  headless walk\'s sections 16 to 18 (91 checks), each new check shown\n  red on a broken copy; the Sun and Earth rooms identical but for the\n  i panel\'s new line; the offline maintenance run, 35 of 35 gating\n  checkers on a copy (its five pulls could not reach GitHub\'s API from\n  the sandbox).\n- **Carried for interactive-exhibit\'s next version** (a description to\n  add, not a wrong sentence): the count line, See more at the top of\n  the drawer, and the About line with index.html#about.\n**Gap (replaces the one below, 2026-10-23):** Tony\'s runs and push of\npatch_L472_1, then his look on the phone; closes on his look.\n**Gap (superseded above):** the design talk (which shape, and whether the rule is per\nroom), the phone test, then the build. Slice 2 of L-443 waits behind\nit, since slice 2 adds the far bodies this bug mis-draws.\n'),
        (b'\n#### [L-443] The rest of the orrery\'s objects come to the website as plotted positions (gallery + orrery, objects)\n<!-- L:443 status:OPEN upd:2026-10-22 section:A flag: rice: -->\n- **Tony, 2026-10-13:** "I am anxious to add the symbols to the gallery\n  too so visitors can at least plot positions." And his note of\n',
         b'\n#### [L-443] The rest of the orrery\'s objects come to the website as plotted positions (gallery + orrery, objects)\n<!-- L:443 status:OPEN upd:2026-10-23 section:A flag: rice: -->\n- **Tony, 2026-10-13:** "I am anxious to add the symbols to the gallery\n  too so visitors can at least plot positions." And his note of\n'),
        (b'  fewer at the top of the drawer, L-474. And "Gonggong skipped but\n  needs discussion", on L-470.\n**Gap (replaces the one below, 2026-10-23):** the view fix first\n(L-472), with the three drawer and panel changes (L-473, L-474,\nL-475); then slice 2, the spacecraft and the open-path comets.\n',
         b'  fewer at the top of the drawer, L-474. And "Gonggong skipped but\n  needs discussion", on L-470.\n- **2026-10-23: the view talk done.** Nothing was drawn wrong; a count\n  line for ticked bodies outside the view, See more at the top and the\n  About line built in gallery patch_L472_1 (L-472, L-474, L-475);\n  L-473 parked, the drawer already opening groups unticked.\n**Gap (replaces the one below, 2026-10-23, afternoon):** Tony\'s runs of\npatch_L472_1 and his phone look; then slice 2, the spacecraft and the\nopen-path comets.\n**Gap (superseded above):** the view fix first\n(L-472), with the three drawer and panel changes (L-473, L-474,\nL-475); then slice 2, the spacecraft and the open-path comets.\n'),
    ]},
    {"path": 'documentation/WHERE_WE_ARE.md', "edits": [
        (b'# Where We Are\n\nLast updated: October 23, 2026: your phone look is done; the view fix\ncomes before slice 2.\n- Written at orrery ee4e333 and gallery 25e4d24, with patch 6.\n\n> **READ THIS FIRST**\n>\n> **Changed since you last read this:**\n> - Your phone look is done. Halley is drawn in the wrong place when\n>   the view is zoomed in (L-472 (the view fix)); that is fixed\n>   before slice 2.\n> - Three smaller changes: L-473 (groups open unticked), L-474 (See\n>   more on top), L-475 (the About link in every i panel).\n>\n> **Do next:** *the view design talk: how the zoom buttons work in\n> the Solar System room; then one test on your phone.*\n>\n> **Needs you now:**\n> - *(do) Run patch 6, then commit and push.*\n> - Two papers left to try (`READING_L456_tony_20261021.md`).\n\n',
         b"# Where We Are\n\nLast updated: October 23, 2026, afternoon: Halley was drawn right; a\ncount line, See more on top, the About line built.\n- Written at orrery b90d895 and gallery 25e4d24, with patches 1 and 2.\n\n> **READ THIS FIRST**\n>\n> **Changed since you last read this:**\n> - Halley was drawn right. Zoomed in, its orbit's near end and cross\n>   stay in view while Halley does not. A line now counts the ticked\n>   bodies outside the view (L-472 (the view fix)).\n> - Built with it: L-474 (See more on top), L-475 (the About link in\n>   every i panel). L-473 (groups open unticked) parked: they do.\n>\n> **Do next:** *your phone look of the three changes; then slice 2,\n> the spacecraft and the comets on open paths.*\n>\n> **Needs you now:**\n> - *(do) Patch 1 on the website and patch 2 on the orrery, the runs\n>   and pushes; then your phone look.*\n> - Two papers left to try (`READING_L456_tony_20261021.md`).\n\n"),
        (b" 10-11.[NOW]   *The orrery's objects come to the website (L-443 (the\n               objects to the website)): slice 1, 50 bodies, live Oct 22;\n               the view fix first; then slice 2, the spacecraft and the\n               comets on open paths; then the moons.* << moved this session\n 12.   [later] Encounters: comets and spacecraft at the dates that matter.\n 13.   [later] The inner planets' rooms (Mercury, Venus, Mars), from the\n",
         b" 10-11.[NOW]   *The orrery's objects come to the website (L-443 (the\n               objects to the website)): slice 1, 50 bodies, live Oct 22;\n               the view's count line built Oct 23; then slice 2, the\n               spacecraft and the comets on open paths; then the moons.*\n               << moved this session\n 12.   [later] Encounters: comets and spacecraft at the dates that matter.\n 13.   [later] The inner planets' rooms (Mercury, Venus, Mars), from the\n"),
        (b"  shell or orbit, plus 20%; the center body's axis and cone end just\n  past its farthest shell. Kelvin stays. (Oct 18-19)\n- Earth's dipole cone drawn, unticked. Agency pages read one layer\n  down. Report words approved. (Oct 21)\n- Drawer order: nearest part as drawn from sourced rows. Drawings end\n  where a row says, Earth too. (Oct 21)\n",
         b"  shell or orbit, plus 20%; the center body's axis and cone end just\n  past its farthest shell. Kelvin stays. (Oct 18-19)\n- Drawer order: nearest part as drawn from sourced rows. Drawings end\n  where a row says, Earth too. (Oct 21)\n"),
        (b"  its symbol. Every body fetched every build. Every comet drawn from\n  today's orbit. Open-path comets go with the spacecraft. (Oct 22)\n\n## Deferred\n",
         b"  its symbol. Every body fetched every build. Every comet drawn from\n  today's orbit. Open-path comets go with the spacecraft. (Oct 22)\n- Zooming in stays a cutout; one line counts the ticked bodies\n  outside the view, never names them. (Oct 23)\n\n## Deferred\n"),
        (b"- L-471 (a delivered patch is final): safe-file-editing's next version.\n\n## Signals  **>> UPDATED THIS SESSION**\n\nRead from files when this page was written, not typed from memory.\n",
         b"- L-471 (a delivered patch is final): safe-file-editing's next version.\n\n## Signals\n\nRead from files when this page was written, not typed from memory.\n"),
        (b'\nAt the next design talk:\n- *The view fix (L-472 (the view fix)): which of three shapes, and\n  whether the zoom rule differs by room (the brief, sec. 4).*\n- Whether the three smaller changes go with it, or first.\n- "Gonggong skipped but needs discussion" (your run record, Oct 22;\n  L-470 (entries the website cannot serve)).\n',
         b'\nAt the next design talk:\n- "Gonggong skipped but needs discussion" (your run record, Oct 22;\n  L-470 (entries the website cannot serve)).\n'),
        (b"\n- Every item: `LEDGER_CONSOLIDATED.md`.\n- *Next: `HANDOFF_L443_view_and_drawer_brief_20261023.md`, sec. 4.*\n- Your phone look: `WHERE_WE_ARE_10-22-26_2027_run_record.md`\n- The objects' rulings: `DESIGN_L443_objects_rulings_20261022.md`;\n  the words: `WORDS_L443_slice1_20261022.md`\n",
         b"\n- Every item: `LEDGER_CONSOLIDATED.md`.\n- *Next, after your look: slice 2, `HANDOFF_L443_slice1_build_20261022.md`.*\n- Today's test and rulings: `WHERE_WE_ARE_10-23-26_1402_run_record.md`\n- The objects' rulings: `DESIGN_L443_objects_rulings_20261022.md`;\n  the words: `WORDS_L443_slice1_20261022.md`\n"),
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
            fail("%s not found. Run this from the repository's root folder"
                 % f["path"])
        raw = open(path, "rb").read()
        crlf = b"\r\n" in raw
        lf = raw.replace(b"\r\n", b"\n")
        if all(lf.count(old) == 0 and lf.count(new) >= 1
               for old, new in f["edits"]):
            fail("%s already carries this patch's edits; it has run before"
                 % f["path"])
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
        plan.append((f, path, out, crlf))
    for f, path, out, crlf in plan:
        open(path, "wb").write(out)
        print("ok  %s (%d edits%s)" % (f["path"], len(f["edits"]),
              "; it was CRLF in the working copy, written LF" if crlf else ""))
    print("patch applied: %s (%d files)" % (TITLE, len(plan)))


if __name__ == "__main__":
    main()
