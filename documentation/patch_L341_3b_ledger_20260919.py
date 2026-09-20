#!/usr/bin/env python3
"""
patch_L341_3b_ledger_20260919.py -- ORRERY repo.

Run: save this file in the ORRERY repo ROOT (next to
PROJECT_INSTRUCTIONS.md), open it in VS Code and click Run.  Or:
python patch_L341_3b_ledger_20260919.py

A patch is run from its repository's ROOT and filed in documentation/
AFTER it has run. This script refuses to run from documentation/.

Built on orrery 21065c5d95ecb22c79fa1f398644a30b73a9a5ed
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 2ead992b055054956816ddda3544e849e9789d9a
at https://github.com/tonylquintanilla/tonyquintanilla.github.io)

RE-CUT 2026-09-19. The first version of this script was cut against
LEDGER_CONSOLIDATED.md as it stands at 21065c5d. So was
patch_L342_3_skill_215_20260919.py, and only one of the two can go
first. THIS VERSION EXPECTS patch_L342_3 AND BOTH INDEX TOOLS TO HAVE
RUN ALREADY. Discard the earlier copy; running it now would refuse on
its fingerprint, which is the guard working.

L-341 has been cited in two patches and in the dashboard's own module
docstring since 2026-09-19, and has had no ledger block behind it. This
writes it, as DONE: the work shipped at 21065c5d and Tony accepted it at
the window.

WHAT IT DOES (one file, 1 anchored edit):

  LEDGER_CONSOLIDATED.md gains [L-341] in section C, immediately before
  [L-249], recording what was asked, what was built, the two things
  testing turned up, and TWO RULINGS that are the part worth keeping:

  - The dashboard is not where "what should I run now" gets answered.
    That is this conversation's job. Recorded as a decision, not as
    backlog, so that nobody builds it later thinking it was merely
    deferred.

  - The twenty checkers under the maintenance runner were NOT re-sorted
    by kind, although that would have shortened the longest group. The
    alphabetical arrangement with GENERATORS and CHECKERS labels is
    Tony's ruling of 2026-09-12, and a tidy-up that quietly overturns a
    prior ruling is worse than a group that stays long.

THE INDEX ZONE IS EXCLUDED FROM THE FINGERPRINT, because ledger_index.py
regenerates it and this patch's own steps tell Tony to run that tool.

SUCCESS looks like: one "ok" line, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.
"""

import hashlib
import os
import sys

LEDGER = "LEDGER_CONSOLIDATED.md"
BASE = "363d9657a8f856b56c0f758726e16a38"
ZONE = (b"<!-- INDEX:START", b"<!-- INDEX:END -->")


def fail(msg):
    print(msg)
    print("NOTHING was written. Undo is Discard Changes in GitHub Desktop.")
    sys.exit(1)


def fingerprint(raw):
    lf = raw.replace(b"\r\n", b"\n")
    try:
        a = lf.index(ZONE[0])
        b = lf.index(ZONE[1]) + len(ZONE[1])
    except ValueError:
        fail("ERROR: the INDEX zone markers are missing from " + LEDGER + ".")
    return hashlib.md5(lf[:a] + lf[b:]).hexdigest()


BLOCK = b"""#### [L-341] The dashboard: a search that names the group, and two rulings
<!-- L:341 status:DONE upd:2026-09-19 section:C flag: rice:3/3/95/1 -->
- **Opened and closed 2026-09-19.** Tony had just run
  `tools/pull_constants_export.py` from a terminal. The dashboard
  already carried a button for it -- Constants Export Pull -- and he
  had not found it. He asked whether the tool was on the dashboard and
  whether a search could be added to find the right button.
- **THE GROUPS WERE BADLY UNEVEN, measured rather than recalled:**
  Solar System 2, Earth System 5, Stars 1, Gallery & Web 22, Developer
  Tools 37. Sixty-seven buttons, and fifty-nine of them in two groups.
  They are now seven: Gallery -- checks and data 15, Gallery --
  authoring 8, Maintenance Run 25, Tools and Caches 11, and the three
  small ones untouched. `Gallery Cache Builder -- Manual Run` moved to
  the gallery group, where its `GALLERY_REPO_DIR` base always said it
  belonged. [verified @ `21065c5d`]
- **THE SEARCH DRAWS EACH MATCH UNDER ITS OWN GROUP HEADING**, rather
  than in one flat list, and that was Tony's choice between the two
  shapes offered. Finding the button is half the job; the other half is
  learning WHERE it lives, so that next time the search is not needed.
  A flat list answers the first question every time and never answers
  the second. A group with no match is not drawn, so the headings left
  on screen are themselves the answer.
- **IT RUNS ON DEMAND, NOT WHILE YOU TYPE** -- Tony's suggestion on
  seeing the first version: "add a Find button before the Clear button.
  that way the search function does not update with every character
  typed only at the end." Two reasons, and the second is his. A redraw
  destroys and rebuilds all sixty-odd cards, which is real work once
  per letter. And the groups shuffle and vanish under the cursor while
  a word is half typed, which is the opposite of a page you can scan.
  Enter does what Find does. What remains is a screen that can disagree
  with the box, so the status line says "press Find, or Enter" while
  they differ -- one short label, the only thing a keystroke touches.
- **TWO THINGS TESTING TURNED UP THAT READING DID NOT.**
  (1) Typing "stars" matched NOTHING. The Stars group exists, but its
  one button is called Star Visualization and no description carries
  the word. A group name now counts as a match and takes its whole
  group. Found by a behaviour test that happened to use that word.
  (2) Searching descriptions as well as names is broad: "export"
  matches 14 of the 67 buttons, because the descriptions in that file
  are long and specific. That breadth is the reason the search works at
  all -- it is how "Constants Export Pull" is findable from "export" --
  and the status line reports the count so the breadth is visible
  rather than surprising.
- **RULING: THE DASHBOARD IS NOT WHERE "WHAT SHOULD I RUN NOW" GETS
  ANSWERED.** A state-aware dashboard was offered as a fourth option --
  the window reading the current state and saying "the export is stale,
  run this". Tony: "the current state is the right question, but i am
  not sure that the dashboard is the place to answer it. ultimately
  this is our conversation." Recorded as a DECISION and not as backlog,
  so that a later session does not build it believing it was merely
  deferred. The question stays live; its home is the conversation.
- **RULING: THE TWENTY CHECKERS WERE NOT RE-SORTED**, although sorting
  them by kind would have cut the longest group from 25 to about 14.
  The alphabetical run with its GENERATORS and CHECKERS labels is
  Tony's own ruling of 2026-09-12, written into the file's comments: a
  sorted run of twenty buttons gives no clue where one kind stops and
  the other starts, and the two labels are what fixed that. Maintenance
  Run stays long on purpose, and reads as a runner with its contents
  indented under it rather than a flat list. A tidy-up that quietly
  overturns a prior ruling is worse than a group that stays long.
- **Tony at the window, 2026-09-19:** "perfect. good update."
- **Claude proposes, unratified:** the behaviour test that found the
  "stars" gap exists only in the session that wrote it. It drives the
  real widget under a virtual display and asserts that typing does not
  redraw, that Find and Enter do, that Clear restores, and that a group
  name matches; it was confirmed able to fail by putting the live-typing
  behaviour back on purpose. Nothing in the repository checks any of
  that now. Whether it earns a place among the checkers is Tony's call,
  and the argument against is that a GUI behaviour test is a new kind of
  thing for this runner to carry.
- **Ref:** `palomas_orrery_dashboard.py`;
  `documentation/patch_L341_1_dashboard_search_and_groups_20260919.py`;
  `documentation/patch_L341_2_dashboard_find_button_20260919.py`.

"""


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        fail("ERROR: this script is running from documentation/. Move it "
             "to the repository ROOT and run it there.")
    if not os.path.exists(LEDGER):
        fail("ERROR: " + LEDGER + " is not here. Run this from the ORRERY "
             "repo root.")

    with open(LEDGER, "rb") as handle:
        raw = handle.read()
    got = fingerprint(raw)
    if got != BASE:
        fail("ERROR: " + LEDGER + " is not the file this patch was cut "
             "against.\n  expected " + BASE + "\n  found    " + got +
             "\nIf the patch already ran, this is what a second run looks "
             "like: it refuses.")

    is_crlf = raw.count(b"\r\n") > 0
    anchor = b"#### [L-249]"
    if is_crlf:
        block = BLOCK.replace(b"\n", b"\r\n")
    else:
        block = BLOCK
    n = raw.count(anchor)
    if n != 1:
        fail("ANCHOR FAIL: expected exactly 1 '#### [L-249]' heading, "
             "found %d." % n)
    out = raw.replace(anchor, block + anchor)

    try:
        out.decode("ascii")
    except UnicodeDecodeError as exc:
        fail("ERROR: the result is not ASCII (%s)." % exc)

    with open(LEDGER, "wb") as handle:
        handle.write(out)

    print("  ok  LEDGER  [L-341] written into section C, before [L-249]")
    print("")
    print("      %-28s %7d -> %7d bytes" % (LEDGER, len(raw), len(out)))
    print("")
    print("patch applied (1 file, 1 edit)")
    print("")
    print("NOW, in order:")
    print("  1. Run ledger_index.py from this folder. It rebuilds the")
    print("     INDEX table. Expect the L-block count to go from 336 to")
    print("     337, and L-341 to appear as DONE in section C.")
    print("  2. Run the orrery maintenance run.")
    print("  3. Move this script into documentation/.")
    print("  4. Commit everything the run touched and push. Report the")
    print("     new SHA.")
    print("")
    print("Undo at any point is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
