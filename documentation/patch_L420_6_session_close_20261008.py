#!/usr/bin/env python3
"""
patch_L420_6_session_close_20261008.py -- ORRERY repo. Closes the
session that built L-420 (the galactic plane in the orrery) and L-027
(the panel colour). Records only: no code changes.

Built on orrery 1ba72f7f at
https://github.com/tonylquintanilla/palomas_orrery (gallery ab66aba0
read for the swap log, not changed). Tony's latest run record read:
documentation/WHERE_WE_ARE_10-7-26_0832_run_record.md.

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT, open it in VS Code and click
    Run. Then follow the NEXT steps it prints.

WHAT CHANGES
    LEDGER_CONSOLIDATED.md
        a header stamp; L-027 (the panel colour) closed; L-422 (the
        ledger skill at 1.17) confirmed and closed. Both closes rest on
        the skill copies this conversation loads, read on 2026-10-08
        after its environment was rebuilt: agentic-pre-test reads 1.3
        and ledger-and-session-records reads 1.17, byte for byte the
        repo's copies.
    documentation/WHERE_WE_ARE.md
        edited BY SECTION at each section's own lines (the 1.17 rule):
        the header, the box, the road's marks, Settled, Signals,
        Waiting on you, Where the details are. Nothing below the
        run-record marker is touched.
    documentation/HANDOFF_L420_galactic_plane_20261006.md
        a closing section and its Next session list.

Each edit is matched only at its own lines, so your notes anywhere else
never stop this patch. If another session has already changed one of
those lines, the patch refuses and writes nothing.

TESTED on a copy of 1ba72f7f: every edit landed; ledger_index.py moved
L-027 and L-422 to the closed table; orrery_maintenance_run.py passed
every gating checker; the page stands at fewer than 130 lines above
its marker; a second run refused and wrote nothing.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 8, 2026 with Anthropic's Claude Opus 5.5.
"""

import os

ROOT_MARKERS = ("palomas_orrery.py", "LEDGER_CONSOLIDATED.md")
NEXT = ["1. Move this script into documentation/ first.",
        "2. Run orrery_maintenance_run.py; the ledger index moves L-027",
        "   and L-422 to the closed table.",
        "3. Commit and push."]

LEDGER = "LEDGER_CONSOLIDATED.md"
PAGE = "documentation/WHERE_WE_ARE.md"
HANDOFF = "documentation/HANDOFF_L420_galactic_plane_20261006.md"

EDITS = {
  LEDGER: [
    ("header stamp",
     ("rule landed; L-396's check gains the cap), built on 8653ef1b, after\n"
      "the day's five patches.\n"),
     ("rule landed; L-396's check gains the cap), built on 8653ef1b, after\n"
      "the day's five patches.\n"
      "Module updated: October 8, 2026 with Anthropic's Claude Opus 5.5\n"
      "(L-027 and L-422 closed on the loaded skill copies; Where We Are\n"
      "edited by section at the L-420 session's close), built on 1ba72f7f.\n")),
    ("L-027 status",
     "<!-- L:027 status:OPEN upd:2026-10-07 section:D.Structural flag: rice:3/2/75/2 -->\n",
     "<!-- L:027 status:DONE upd:2026-10-08 section:C flag: rice:3/2/75/2 -->\n"),
    ("L-027 closed",
     ("**Gap:** a later session confirms its loaded copy of agentic-pre-test\n"
      "reads 1.3, then closes this item. The session that bumped it loaded\n"
      "1.2 and cannot see the reinstall.\n"),
     ("- **Closed 2026-10-08.** The loaded copy of agentic-pre-test reads\n"
      "  1.3. It was read from the skills this conversation loads, after its\n"
      "  environment was rebuilt on 2026-10-08, and it is byte for byte the\n"
      "  repo's `skills/agentic-pre-test/SKILL.md` at 1ba72f7f. The bytes\n"
      "  were the check, not the word that the skill was reinstalled. Tony's\n"
      "  verdict on the panels, from\n"
      "  `documentation/WHERE_WE_ARE_10-7-26_0832_run_record.md`:\n"
      "  \"-- confirmed.\"\n"
      "**Gap:** none. (Was: a later session confirms its loaded copy of\n"
      "agentic-pre-test reads 1.3.)\n")),
    ("L-422 status",
     "<!-- L:422 status:OPEN upd:2026-10-07 section:A flag: rice: -->\n",
     "<!-- L:422 status:DONE upd:2026-10-08 section:C flag: rice: -->\n"),
    ("L-422 confirmed and closed",
     ("**Gap:** the loaded-copy confirmation above; then CLOSE. The check\n"
      "(date and cap) is L-396's to build, not this item's.\n"),
     ("- **Confirmed and closed, 2026-10-08,** by the L-420 (galactic plane)\n"
      "  session. The loaded copy of ledger-and-session-records reads 1.17,\n"
      "  byte for byte the repo's at 1ba72f7f, read from the skills this\n"
      "  conversation loads after its environment was rebuilt. That\n"
      "  session's close then edited Where We Are by section under it.\n"
      "  Tony's reinstall and v3.85, from\n"
      "  `documentation/WHERE_WE_ARE_10-7-26_0832_run_record.md`: \"-- done\".\n"
      "**Gap:** none. The check (date and cap) is L-396's to build, not\n"
      "this item's. (Was: the loaded-copy confirmation; then close.)\n")),
  ],
  PAGE: [
    ("header",
     ("Last updated: October 7, 2026, end of the Fable ledger sweep.\n"
      "- Written at orrery 8653ef1b and gallery 4cfeca27, after the day's five\n"
      "  patches and before your run of this closing one.\n"),
     ("Last updated: October 8, 2026, end of the galactic plane session.\n"
      "- Written at orrery 1ba72f7f and gallery ab66aba0, before your run of\n"
      "  this closing patch.\n")),
    ("box: changed",
     ("> **Changed since you last read this:**\n"
      "> - This page has a new shape, the one you confirmed: each fact once,\n"
      ">   this box is the page, and the end of the page is yours. Paste your\n"
      ">   run record below the marker at the bottom, as you do.\n"
      "> - The Horizons check is designed, in one session with its own file.\n"
      ">   What it checks, what counts as agreement, where it runs: settled.\n"
      ">   The build is next.\n"
      "> - The Earth System work is ordered: central, but behind the orrery\n"
      ">   website; the gallery cards stand in meanwhile. The 2026 heat-dome\n"
      ">   items close, because the event is over.\n"
      "> - The daily hand run stands: four checks, first thing, no automating\n"
      ">   for now. Daily Run pauses OneDrive for 24 hours, not 2.\n"
      "> - The swap log proves the retry fix: two of your hand builds needed a\n"
      ">   second attempt and both succeeded. \"Took 2 attempts\" is normal.\n"
      "> - Items inside an ordered list need no RICE score; the rest keep it.\n"
      ">   That rule, and this page's rules, are in the ledger skill, now 1.17.\n"),
     ("> **Changed since you last read this:**\n"
      "> - The galactic plane work in the desktop orrery is finished, and you\n"
      ">   found it correct: the violet circle with its poles, Sagittarius A*,\n"
      ">   a hover cross on each coordinate circle, and a brighter galactic\n"
      ">   tide with its cone.\n"
      "> - The orrery's panels use one grey, gray90, on every system. You\n"
      ">   confirmed it, and L-027 (the panel colour) is closed.\n"
      "> - L-422 (the ledger skill at 1.17) is closed: the skill copy this\n"
      ">   session loads reads 1.17, and this page was edited under it.\n")),
    ("box: needs you now",
     ("> - *Run orrery_maintenance_run.py and push. Reinstall the ledger skill\n"
      ">   (1.17) and replace the Project's instructions with v3.85.*\n"),
     "> - *Run this closing patch, then orrery_maintenance_run.py, and push.*\n"),
    ("road: heading mark cleared",
     "## The road  **>> UPDATED THIS SESSION**\n",
     "## The road\n"),
    ("road: stage 8 mark cleared",
     "               Designed; build next. << moved this session\n",
     "               Designed; build next.\n"),
    ("settled: two rulings",
     "Standing rulings. A line leaves after a few weeks, once it is habit.\n",
     ("Standing rulings. A line leaves after a few weeks, once it is habit.\n"
      "- The galactic tide keeps its cone, to show its pull as physics. (Oct 7)\n"
      "- No colour or other name that only one system knows. The panels'\n"
      "  grey is one name, gray90. (Oct 6)\n")),
    ("signals",
     ("- Last cache build: 20261007T143110Z, ok, one attempt. Last retry: the\n"
      "  Oct 6 18:20 hand build, two attempts, ok.\n"
      "- Tier-1 findings, whole tree: 296, unchanged since Oct 6. No tool yet\n"
      "  prints the number on the gate path alone; that is owed on the\n"
      "  provenance-discipline bump.\n"
      "- This page's date and the ledger's newest stamp: both Oct 7. Agree.\n"),
     ("- Last cache build: 20261008T013323Z, ok, one attempt. Last retry: the\n"
      "  Oct 6 18:20 hand build, two attempts, ok.\n"
      "- Tier-1 findings, whole tree: 296, unchanged since Oct 6. No tool yet\n"
      "  prints the number on the gate path alone; that is owed on the\n"
      "  provenance-discipline bump.\n"
      "- This page's date and the ledger's newest stamp: both Oct 8. Agree.\n")),
    ("waiting: design talk, the phone's galactic plane",
     "- Earth's design talks, the belts' shape first.\n",
     ("- Earth's design talks, the belts' shape first.\n"
      "- Whether the phone's Sun room gets the galactic plane, its poles,\n"
      "  Sgr A* and the tide's cone: L-408 (the galactic plane on the phone).\n"
      "  You: \"awaits the design talk.\" (Oct 7)\n")),
    ("waiting: L-027 decision done",
     "- L-027 (the panel colour) closes once its confirming patch has run.\n",
     ""),
    ("details: Fable sweep named",
     "- Every item: `LEDGER_CONSOLIDATED.md`. This session: L-422 (the ledger\n",
     "- Every item: `LEDGER_CONSOLIDATED.md`. The Fable sweep: L-422 (the ledger\n"),
    ("details: records",
     ("- This session's record:\n"
      "  `documentation/HANDOFF_L422_fable_sweep_close_20261007.md`\n"),
     ("- The Fable sweep's record:\n"
      "  `documentation/HANDOFF_L422_fable_sweep_close_20261007.md`\n"
      "- The galactic plane and the panel colour, both closed: L-420 (the\n"
      "  galactic plane), L-027 (the panel colour);\n"
      "  `documentation/HANDOFF_L420_galactic_plane_20261006.md`\n")),
  ],
  HANDOFF: [
    ("session closed",
     ("## Next session\n"
      "\n"
      "- L-420 closed 2026-10-07.\n"
      "- Confirm the loaded agentic-pre-test reads 1.3, then close L-027;\n"
      "  Tony confirmed the panels 2026-10-07.\n"
      "- Nothing else is opened by this session.\n"),
     ("## Session closed, 2026-10-08\n"
      "\n"
      "- Pushes, in order: e7073fce (L-420 and L-027 built), 12693a53 (the\n"
      "  circles' hovers and the tide), 8c457b7d (L-420 closed), 3f4c01e2\n"
      "  (the panels confirmed). Tony's verdicts are in\n"
      "  `documentation/WHERE_WE_ARE_10-7-26_0832_run_record.md`.\n"
      "- L-027 (the panel colour) closed by\n"
      "  `patch_L420_6_session_close_20261008.py`. This conversation's\n"
      "  environment was rebuilt on 2026-10-08, and the skill copies it\n"
      "  loads then read agentic-pre-test 1.3 and\n"
      "  ledger-and-session-records 1.17, byte for byte the repo's at\n"
      "  1ba72f7f. That discharges both travelling obligations, and L-422\n"
      "  (the ledger skill at 1.17) closes on the same read.\n"
      "- Where We Are edited by section under 1.17: the box, Settled,\n"
      "  Signals, Waiting on you and the details; nothing below the marker.\n"
      "- Lesson: twice this session a patch was built on a commit the repo\n"
      "  had moved past while other sessions pushed. The guards refused and\n"
      "  nothing broke, but the fix is to read the repo's head just before\n"
      "  handing over any patch, which the later patches did.\n"
      "\n"
      "## Next session\n"
      "\n"
      "- L-420 (the galactic plane) closed 2026-10-07; L-027 (the panel\n"
      "  colour) and L-422 (the ledger skill at 1.17) closed 2026-10-08.\n"
      "- The phone's galactic plane waits for the design talk, on L-408\n"
      "  (the galactic plane on the phone).\n"
      "- Nothing else is opened by this session.\n")),
  ],
}


def read_lf(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    return raw.decode("utf-8").replace("\r\n", "\n"), b"\r\n" in raw


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the repo ROOT, not from "
                         "documentation/. NOTHING was written.")
    for marker in ROOT_MARKERS:
        if not os.path.isfile(marker):
            raise SystemExit("ERROR: %s is not here, so this is not the "
                             "orrery root. NOTHING was written." % marker)
    results = []
    for path in (LEDGER, PAGE, HANDOFF):
        if not os.path.isfile(path):
            raise SystemExit("ERROR: %s is not here. NOTHING was written." % path)
        text, crlf = read_lf(path)
        marker = "--- Your run record below this line"
        zone_before = text[text.find(marker):] if path == PAGE else None
        done = []
        for label, old, new in EDITS[path]:
            found = text.count(old)
            if found != 1:
                raise SystemExit("ANCHOR FAIL (%s): expected 1 match in %s, "
                                 "found %d. Has this patch already run, or has "
                                 "another session changed those lines? NOTHING "
                                 "was written." % (label, path, found))
            text = text.replace(old, new)
            done.append(label)
        if path == PAGE:
            if marker not in text or text[text.find(marker):] != zone_before:
                raise SystemExit("ERROR: the run-record zone would change. "
                                 "NOTHING was written.")
            above = text[:text.find(marker)].count("\n")
            if above > 130:
                raise SystemExit("ERROR: the page would stand at %d lines above "
                                 "its marker (cap 130). NOTHING was written."
                                 % above)
        results.append((path, text, done, crlf))
    for path, text, done, crlf in results:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        if crlf:
            print("note: %s was CRLF in the working copy; written LF" % path)
        for label in done:
            print("ok  %-56s %s" % (path, label))
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    for line in NEXT:
        print("  " + line)


if __name__ == "__main__":
    main()
