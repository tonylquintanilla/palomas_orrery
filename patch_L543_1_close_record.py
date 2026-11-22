"""
patch_L543_1_close_record.py -- the close of the coordinating session of
Nov 21, 2026 (afternoon and night): the ledger, Where We Are, and the
starting prompt for the next coordinating session.

Built on e8cc7f11 at https://github.com/tonylquintanilla/palomas_orrery
(branch main), with gallery 15eec699 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.

Tony, 2026-11-21, on "Shall I write the close now, as a patch for you to
run in the morning?": "-- yes" (his run record copy,
documentation/WHERE_WE_ARE_11-21-26_1515_run_record.md).

RUN COMMAND
    Save this file in the orrery folder (palomas_orrery_for_github), open
    it in VS Code and click Run:

        python patch_L543_1_close_record.py

    Success: "ok" lines for the edits, one "new" line, "patch applied",
    then "ok" for ledger_index.py and the document-caps check.
    Failure: an "ERROR:" or "ANCHOR FAIL" line, and NOTHING is written.
    Undo after a success: Discard Changes in GitHub Desktop, and delete
    the one new document.
    Once it has run, move it to the documentation folder.

What it changes:
    LEDGER_CONSOLIDATED.md:
        L-541 (a plan's clock): the coordinating session's review, Tony's
            tolerance question and its measurement, and that the rooms'
            clock is live (pushed, the night green, his phone look).
        L-529 (guided encounters): the two red nights of Nov 21, their
            cause and their fix.
        L-521 (the walk's red checks): its gate is met; it stays open
            for L-544.
        Four new items: L-543 (green on Tony's computer, red on GitHub),
            L-544 (L4 and L5 tie), L-545 (checks that wait to be
            remembered), L-546 (the dashboard does not open the as-built
            page).
    documentation/WHERE_WE_ARE.md, by section, above the run-record
        marker only: the date line, the box, the road's two lines,
        Settled, Signals, Waiting on you, Where the details are. The
        page stays at its cap of 130 lines. Nothing below the marker is
        read or changed.
    documentation/PROMPT_coordinator_start_20261122_2.md (new): the
        starting prompt for the next coordinating session.

No skill and no rule of the protocol changes; the skill text owed is
named on L-541 and L-545 for the next coordinating session.

Written November 21, 2026 with Anthropic's Claude Fable 5.2.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

NEW_FILES = [('documentation/PROMPT_coordinator_start_20261122_2.md',
  '<!-- Doc-Kind: hand | A starting prompt for the next coordinating '
  'session, written at the close of the one before it. -->\n'
  '# Starting prompt: the next coordinating session\n'
  '\n'
  'Built on orrery e8cc7f11 at\n'
  'https://github.com/tonylquintanilla/palomas_orrery (branch main) and\n'
  'gallery 15eec699 at\n'
  'https://github.com/tonylquintanilla/tonyquintanilla.github.io, with\n'
  'patch_L543_1_close_record.py on top. Written Nov 21, 2026, night, by\n'
  'the coordinating session of that day (Claude Fable 5.2).\n'
  '\n'
  'Paste everything below the line into a new chat in the Orrery Project.\n'
  '\n'
  '---\n'
  '\n'
  "You are the coordinating session for Paloma's Orrery. The Project\n"
  'instructions and the skills are resident; follow them.\n'
  '\n'
  'Start the usual way:\n'
  '\n'
  "1. Pull both repositories at HEAD and record the SHAs. The orrery's\n"
  "   HEAD should hold the last session's close: the protocol still reads\n"
  '   v3.144 (no skill was bumped), the ledger carries L-543 to L-546, and\n'
  "   L-541 (a plan's clock) says the rooms' clock is LIVE. If not, the\n"
  '   close patch was not run or not pushed; say so before anything else.\n'
  "2. Read documentation/WHERE_WE_ARE.md, then Tony's newest run-record\n"
  '   copy (documentation/WHERE_WE_ARE_*_run_record.md) for his notes.\n'
  '3. Read the night records in BOTH repositories. The website: a\n'
  '   "Nightly run" commit dated after Nov 21, 21:46 Chicago, with the\n'
  '   "Room clock" row PASS in data/nightly_run_record.json. That row is\n'
  "   new; it asks whether the room's places of Mercury and 3I/ATLAS match\n"
  "   JPL's at the build's UTC minute. If a night is red on it, or on the\n"
  "   builder's clock question, that is the first thing to tell Tony. The\n"
  '   orrery: its newest "Nightly run" title and its El Nino row; NOAA\'s\n'
  '   next update is expected 10 December 2026.\n'
  "4. Whether the reel's place is on GitHub: in "
  'gallery/gallery_metadata.json\n'
  '   the card escapade_reel should carry drawer_row "earth". It was on\n'
  "   Tony's disk, not pushed, when this was written.\n"
  '\n'
  'Where things stand:\n'
  '\n'
  "- The live rooms' clock is set right and live (L-541): a body is drawn\n"
  '  where JPL puts it at the UTC minute shown; until Nov 21 it was drawn\n'
  '  69 seconds behind. Built by one Code session in three parts, pushed\n'
  '  at gallery b817aca5, the night by hand green at 15eec699.\n'
  "- Two red website nights were found and fixed the same day (L-529's\n"
  '  note; the class is L-543).\n'
  "- Two decisions wait on Tony, on Where We Are: the gallery's checks\n"
  '  read from a push copy before every push (L-543), and whether the\n'
  '  walks join the gallery run, with the recorded Earth scene (L-545).\n'
  '\n'
  'Next, in the order Tony left to the coordinating session on Nov 21 ("in\n'
  'whatever order you believe works best"):\n'
  '\n'
  "- L-539 (every entry checked): the orrery's Horizons check over every\n"
  '  entry, from a one-time list Tony scans; its brief is not written. It\n'
  "  never touches the website. With it, L-512's two leftover asks, if\n"
  '  Tony agrees; that grouping was proposed, not ruled.\n'
  '- The skill text owed, as one bump (v3.145), before the next website\n'
  '  build: from L-541, horizons-orbital-mechanics, gallery-assembler,\n'
  "  interactive-exhibit and gallery-cache-builder (the build's closing\n"
  "  report names each; it is on L-541); from L-545, interactive-exhibit's\n"
  '  rule that a session changing the page runs both walks; and the three\n'
  '  L-529 left waiting. Each skill is at its cap.\n'
  "- L-538 (the orbiters' printed error), in the website, after the bump.\n"
  "- L-544 (L4 and L5 tie): a tie-break in the drawer's order; small, and\n"
  '  it turns a walk red at some minutes until it is done.\n'
  "- Then the encounter's slice 2, its talk first (L-529).\n"
  '- Open on L-541, for an orrery session and a builder session: the\n'
  '  builder asks daily points 9 seconds before UTC midnight; its keys and\n'
  "  plan windows are read as UTC; the orrery's whole-second 69.\n"
  '\n'
  'Lessons from the last session worth carrying:\n'
  '\n'
  '- A base is a fresh checkout of the pushed commit. An untouched copy of\n'
  "  Tony's folder is not what GitHub has: nine leftover folders made a\n"
  '  check green there and red at night. This sandbox can clone both\n'
  '  repositories and run gallery_maintenance_run.py --night on the clone\n'
  '  (pip install astropy astroquery; Scene cards needs a stand-in for\n'
  '  tkinter; the pulls and the builder cannot run here).\n'
  '- A session that changes the page runs the walks before its closing\n'
  '  report. On Nov 21 a one-day slip in three boxes passed 53 gallery\n'
  "  rows and the coordinating session's own re-run, and one walk caught\n"
  '  it, run only because it was asked for at the last minute.\n'
  '- A Part A that maps and changes no file pays for itself. It corrected\n'
  '  the brief on the served window before anything was built.\n'
  "- The linked computer lets this session read Tony's uncommitted files\n"
  '  (staged copies) and so check a Code report against his disk. It was\n'
  '  used to re-run the new check on his files before the push.\n'
  "- A build that rebuilds the cache on Tony's machine, the checks and his\n"
  '  push are one sitting, between two nights; read git ls-remote before\n'
  '  the build and before the push. Website nights are scheduled 08:17 and\n'
  '  12:17 UTC and have landed hours late.\n'
  '- A witness should not share its clock with what it tests. The build\n'
  "  proposed astropy alone; JPL's own TDB-UT (astroquery's delta_T) was\n"
  '  added so each checks the other.\n'
  '- Check a claim before telling Tony. The last session told him the red\n'
  '  nights "went unseen until you looked at the Actions tab" without\n'
  '  knowing how he learned of them; L-485 (a nightly run) records that\n'
  "  the dashboard's nightly line turns red a day after the last clean\n"
  "  run. It also wrote 69.184 s into a brief; that is TT's figure, and\n"
  "  JPL's clock gives 69.183 s.\n"
  '- Tony reads a report on his phone and carries it by paste. A go-ahead\n'
  '  he can paste, with its anchor line, worked every time.\n'
  '\n'
  "Ask Tony one thing to begin: L-539's brief first, or the skills bump\n"
  'first.\n')]

EDITS = [('LEDGER_CONSOLIDATED.md',
  "#### [L-541] A plan's moment is on JPL's clock (TDB), and some places "
  "read or print it as UTC (orrery + gallery; the rooms' clock built Nov 21, "
  "the builder's and the orrery's readings still open)\n",
  "#### [L-541] A plan's moment is on JPL's clock (TDB), and some places "
  "read or print it as UTC (orrery + gallery; the rooms' clock LIVE Nov 21, "
  "the builder's and the orrery's readings still open)\n"),
 ('LEDGER_CONSOLIDATED.md',
  "**Gap:** the rooms' clock is built and waits for Tony's push, the night\n"
  "by hand and his phone look. Still open here: the builder's keys\n",
  "- **THE COORDINATING SESSION'S REVIEW, AND TONY'S QUESTION, 2026-11-21**\n"
  "  (Claude Fable 5.2). Read on Tony's disk against 7d1e2e16 before the\n"
  "  push: `resolver.py`, `models.py`, `cache_reader.py` and the builder's\n"
  '  clock block. `documentation/smoke_room_clock.js` run on a clean\n'
  "  checkout with his files laid over it: PASS, with the build's own rows\n"
  '  (0.001 km and 0.026 km with the seam; 3,694 km and 4,088 km without).\n'
  '  Tony, 20:58: "are we asking JPL to match our numbers at a time\n'
  '  tolerance that invites a fail?" Measured by the build, by hand and not\n'
  "  in the build, at 6, 12, 18 and 24 hours after the date of Mercury's\n"
  "  served orbit: the box's error was at least 6.9 times the room's miss\n"
  '  at every hour (3I/ATLAS at 12 hours, 0.072 km against 0.5 km; Mercury\n'
  '  at 24 hours, 0.055 km against 0.5 km). The brief was wrong twice, both\n'
  '  found by the build: the served window is made on UTC, and 69.184 s is\n'
  "  TT's figure.\n"
  '- **LIVE, 2026-11-21.** Pushed at gallery b817aca5 (Tony, 21:40, '
  '"website\n'
  '  pushed. no pull."). The night run by hand, run 52, green at gallery\n'
  '  15eec699: six steps clean, all 59 rows PASS, Room clock among them;\n'
  "  the builder on GitHub's machine got 69.182891 s from JPL, astropy "
  '8.0.3\n'
  '  agreeing. Tony\'s phone look, on "the date line still reads UTC ...\n'
  '  Juno\'s box still says \'as far as 26 August 2028\'": "-- yes"\n'
  '  (`documentation/WHERE_WE_ARE_11-21-26_1515_run_record.md`).\n'
  "**Gap:** the rooms' clock is live. Still open here: the builder's keys\n"),
 ('LEDGER_CONSOLIDATED.md',
  "above, no day wrong). The walks' two reds are L-521's.\n"
  "**Tony-action (do):** commit the website's code and its rebuilt cache\n"
  'together and push in the same sitting; run the night by hand (Actions,\n'
  '"Nightly run", "Run workflow") and read it green; then the phone look.\n',
  "above, no day wrong). The walks' two reds are L-544 (L4 and L5 tie).\n"
  'The skill text is for the next coordinating session, as one bump.\n'),
 ('LEDGER_CONSOLIDATED.md',
  '**Gap:** slice 2, its talk first: the two close passes and how the\n'
  'visitor moves between the three views; escape speed beside the speed\n',
  "- **TWO NIGHTS WENT RED ON THIS BUILD'S AS-BUILT LINE, 2026-11-21** (the\n"
  '  coordinating session, Claude Fable 5.2). Tony, 14:50: "nightly runs 49\n'
  '  and 50 on the website failed exit code 1." The as-built section pushed\n'
  '  at f918d74 (Nov 20, 20:43) named `feature_configs.json` with no\n'
  '  folder; `tools/check_as_built_names.py` does not look for a bare file\n'
  "  name inside `data/solar-system/`, so on GitHub's copy the name was not\n"
  "  found. On Tony's computer the same check was green: nine folders a\n"
  '  build of Nov 19 left under `data/` (`.staging_solar-system_...`) each\n'
  '  held a file of that name, and the check read them. So the Nov 21\n'
  '  session\'s "52 of 52" was true of his disk and not of the push. Its\n'
  '  Picture folds red was real too, and was fixed at 828362fd. Measured on\n'
  '  a clean checkout of 81c6ff5d: As-built names red, 50 of 52 gating\n'
  '  rows green, Scene cards not runnable there. Fixed by\n'
  '  `patch_L529_4_as_built_names_night.py` in the website (the name with\n'
  '  its folder; the check leaves out `data/.staging_*`; its self-test\n'
  '  plants a file in each leftover place), pushed at 627acc3f; the night\n'
  '  run by hand green at 7d1e2e16, all 58 rows PASS. The class is L-543\n'
  "  (green on Tony's computer, red on GitHub).\n"
  '**Gap:** slice 2, its talk first: the two close passes and how the\n'
  'visitor moves between the three views; escape speed beside the speed\n'),
 ('LEDGER_CONSOLIDATED.md',
  '<!-- L:521 status:PENDING-GATE upd:2026-11-21 section:A flag: rice: -->\n',
  '<!-- L:521 status:OPEN upd:2026-11-21 section:A flag: rice: -->\n'),
 ('LEDGER_CONSOLIDATED.md',
  "**Gap:** Tony's push of the walk; then DONE, and the walk is the check\n"
  'that goes red when the drawer leaves its rules.\n',
  '**Gap:** the walk was pushed at gallery 81c6ff5d (Nov 21), so its gate\n'
  'is met. Not DONE: that evening one of its 368 checks, and one of\n'
  "`walk_scene_moment.js`'s 13, was red at some minutes and green at\n"
  'others, on the order of Earth-Moon L4 and L5, which is L-544 (L4 and\n'
  'L5 tie). When L-544 closes, this closes, and the walk is the check that\n'
  'goes red when the drawer leaves its rules.\n'),
 ('LEDGER_CONSOLIDATED.md',
  "#### [L-541] A plan's moment is on JPL's clock (TDB), and some places "
  "read or print it as UTC (orrery + gallery; the rooms' clock LIVE Nov 21, "
  "the builder's and the orrery's readings still open)\n",
  "#### [L-543] A check green on Tony's computer and red on GitHub: the "
  "gallery's checks are not read from what a push carries (gallery; "
  'recorded, a ruling asked)\n'
  '<!-- L:543 status:OPEN upd:2026-11-21 section:A flag: rice: -->\n'
  '- **Opened 2026-11-21** by the coordinating session (Claude Fable 5.2),\n'
  "  from two red website nights (L-529's note of that day). A check that\n"
  "  walks Tony's website folder also reads what git ignores there; "
  "GitHub's\n"
  '  copy holds none of it. The founding case: '
  '`tools/check_as_built_names.py`\n'
  '  read nine `data/.staging_solar-system_*` folders left by a build of\n'
  "  Nov 19, and passed on a name that GitHub's copy does not have.\n"
  "- That one check now leaves the builder's leftovers out\n"
  '  (`patch_L529_4_as_built_names_night.py`). The class is open: any other\n'
  '  check that walks `data/` or the folder can do the same. The nine\n'
  '  folders need nothing: the builder removes siblings older than three\n'
  '  days at its next run on that machine\n'
  '  (`documentation/check_cache_siblings.py`, its header).\n'
  '- WHAT WORKED TWICE ON NOV 21. The coordinating session ran\n'
  '  `gallery_maintenance_run.py --night` on a clean clone of the pushed\n'
  "  commit. L-541's Code session ran the whole gallery run in a throwaway\n"
  '  folder holding only the files `git ls-files --cached --others\n'
  '  --exclude-standard` lists, 53 of 53; its copy script lived in a\n'
  '  scratch folder and is not in the repository.\n'
  '- Tony, Nov 21, on "a gallery run on a fresh checkout before a push ...\n'
  '  is worth a ruling at the close": "-- okay"\n'
  '  (`documentation/WHERE_WE_ARE_11-21-26_1515_run_record.md`).\n'
  "**Gap:** Tony's ruling: whether the gallery run is read from a push copy\n"
  'before every website push. If yes: the copy script becomes a tool in\n'
  '`tools/`, the run gains a way to do it in one step, and the rule goes\n'
  'into the skill that covers testing a room.\n'
  "**Ref:** L-529 (guided encounters); L-541 (a plan's clock); L-423 (the\n"
  "website's checks); L-485 (a nightly run).\n"
  '\n'
  "#### [L-544] Earth-Moon L4 and L5 tie in the drawer's order, so which is "
  'listed first changes from minute to minute (gallery; recorded, not '
  'fixed)\n'
  '<!-- L:544 status:OPEN upd:2026-11-21 section:A flag: rice: -->\n'
  '- **Opened 2026-11-21** by the coordinating session (Claude Fable 5.2),\n'
  "  from L-541's Code session (Claude Opus 5.5), which found it with the\n"
  "  walks. Earth's fold lists its children nearest first (L-297). The two\n"
  '  points are each as far from Earth as the Moon is, and are served at\n'
  '  the same distance except in the 17th decimal place, so the order of\n'
  '  the two rows is not fixed.\n'
  '- WHAT IT DID. `tools/headless/walk_solar_system_drawer.js`: 368 of 368\n'
  '  at 02:58 and 03:22 UTC on Nov 22, 367 at a minute between ("earth\'s\n'
  '  moons are not right under its row, nearest first"); the untouched\n'
  '  7d1e2e16 failed the same check at 03:22. `walk_scene_moment.js`: 12 of\n'
  '  13 on the untouched 7d1e2e16 ("frozen: the drawer differs from the\n'
  '  plain opening (232 rows against 232)"), rows 100 and 101 trading\n'
  "  places between today and the window's last day. The same pair was the\n"
  "  one wrong verdict of eleven in L-521's repair.\n"
  '- NOT VERIFIED in a browser: whether a visitor sees the two rows trade\n'
  '  places between visits. The walks say the order differs between\n'
  '  minutes.\n'
  "**Gap:** a tie-break in the drawer's order where two distances agree to\n"
  'the digits a box prints (by name is the plain choice), in the page and\n'
  "in the gallery editor's tree, which lists the same order; then both\n"
  'walks green at every minute. Method, not a ruling. Small; a session\n'
  'that changes the page runs both walks (L-545).\n'
  "**Ref:** L-297 (the Lagrange points); L-521 (the walk's red checks);\n"
  "L-541 (a plan's clock).\n"
  '\n'
  '#### [L-545] Two checks of the page wait to be remembered: the walks, and '
  "the recorded Earth scene (gallery; the session's part is method, two "
  'rulings asked)\n'
  '<!-- L:545 status:OPEN upd:2026-11-21 section:A flag: rice: -->\n'
  '- **Opened 2026-11-21** by the coordinating session (Claude Fable 5.2).\n'
  "  THE WALKS load the page itself; the gallery run's rows test its\n"
  "  scripts and a recorded scene. On Nov 21 L-541's build left three boxes\n"
  "  printing a path's day one day early (Juno, West, Galileo). It passed\n"
  "  53 gallery rows on Tony's copy and on a push copy, and the\n"
  "  coordinating session's own run of the new check.\n"
  '  `walk_solar_system_drawer.js` caught it, run only because the\n'
  '  coordinating session asked for the walks before the commit. A session\n'
  '  does not run them unasked: they need jsdom (24.1.3, from npm, into a\n'
  '  scratch folder), and neither the gallery run nor the night runs them.\n'
  '- Tony, Nov 21, on "that should not depend on someone remembering":\n'
  '  "-- correct. should this be method?"\n'
  '  (`documentation/WHERE_WE_ARE_11-21-26_1515_run_record.md`). Yes. THE '
  'METHOD: a session that changes\n'
  '  `interactive.html` or a script it loads runs both walks before its\n'
  '  closing report, and reports each count and any red check by name. A\n'
  '  brief says so until interactive-exhibit does.\n'
  '- THE RECORDED EARTH SCENE (`documentation/payload_earth_scene.json`,\n'
  '  made by `tools/record_earth_scene.py`) is re-recorded only by hand.\n'
  '  Six checks read it. Re-recorded on Nov 21 for L-541, it brought in\n'
  "  Earth's period sentence, served since L-535, which Typed facts had\n"
  "  never read (the build's closing thought).\n"
  "**Gap:** the skill text, at interactive-exhibit's next version. Two\n"
  'rulings for Tony: whether the walks join the gallery run, which means\n'
  "the website keeps jsdom and the night's runner installs it; and when the\n"
  'recorded scene is re-recorded (at every cache build, or by a check that\n'
  'goes red when it is older than the page).\n'
  "**Ref:** L-541 (a plan's clock); L-521 (the walk's red checks); L-423\n"
  "(the website's checks); L-535.\n"
  '\n'
  "#### [L-546] Tony could not find INTERACTIVE_AS_BUILT.md: the dashboard's "
  'documents list does not open it (orrery, the dashboard; recorded)\n'
  '<!-- L:546 status:OPEN upd:2026-11-21 section:A flag: rice: -->\n'
  '- **Opened 2026-11-21** by the coordinating session (Claude Fable 5.2).\n'
  '  Tony, 15:02: "I can\'t find INTERACTIVE_AS_BUILT.md in my folders. it\n'
  '  should be in the orrery root if it is ia critical document". It is in\n'
  "  the website's root, beside the code it describes;\n"
  "  `tools/check_as_built_names.py` reads it there, and GitHub's night has\n"
  '  no orrery folder. Tony agreed it stays ("Yes", 15:08, to the patch\n'
  "  with the page staying in the website's root).\n"
  '- FOUND BY A SEARCH, NOT A RUN: `palomas_orrery_dashboard.py` names the\n'
  "  page once, in a check's description, and has no entry that opens it.\n"
  "**Gap:** a line in the dashboard's documents list that opens the\n"
  "website's `INTERACTIVE_AS_BUILT.md` from the sibling folder. A patch.\n"
  '**Ref:** L-522 (document caps); L-529 (guided encounters).\n'
  '\n'
  "#### [L-541] A plan's moment is on JPL's clock (TDB), and some places "
  "read or print it as UTC (orrery + gallery; the rooms' clock LIVE Nov 21, "
  "the builder's and the orrery's readings still open)\n"),
 ('documentation/WHERE_WE_ARE.md',
  'Last updated: November 21, 2026, afternoon: the Links fold built, the '
  'drawer walk brought up to date (Claude Code, Claude Opus 5.5), and the '
  'skills written for both builds (the coordinating session, Claude Fable '
  '5.2).\n'
  "- Written at orrery bd70f584 and gallery 828362fd, with this session's "
  'edits on your disk, not pushed.\n',
  'Last updated: November 21, 2026, night: two red website nights found and '
  "fixed, and the live rooms' clock set right (the coordinating session, "
  'Claude Fable 5.2; the clock built by Claude Code, Claude Opus 5.5).\n'
  '- Written at orrery e8cc7f11 and gallery 15eec699, both pushed; the '
  "reel's place was on your disk and not yet on GitHub.\n"),
 ('documentation/WHERE_WE_ARE.md',
  "> - A link card can now sit beside a body in the room's drawer, in a "
  "Links fold after that body's Encounters and before its Saved pictures; a "
  'tap opens it in a new tab. The gallery editor shows the same fold, and '
  'New Link Card asks which row; with no row the card goes to Storage. The '
  'Outside Links room is gone from the code (L-540 (a reel on a Featured '
  'card)).\n'
  "> - The pushed website's Picture folds check was red: it refused the "
  "reel's card for having no place in the drawer. A link card may now have "
  'none, and the whole gallery run is green, 52 of 52, run with nothing '
  'being edited.\n'
  '> - The drawer walk is green again, 368 checks: its eleven red checks '
  'each expected the page as it was before a deliberate change (the Lagrange '
  'points, the Encounters fold, and three older ones), so only the walk '
  "changed; three planted breaks each turn it red (L-521 (the walk's red "
  'checks)).\n',
  '> - Every live room now draws each body where JPL puts it at the UTC '
  'minute its date line shows. Until Nov 21 each was drawn where it was 69 '
  "seconds earlier: JPL's dates are on JPL's own clock, and nothing "
  'converted. No date you read changed. Each night now asks JPL where '
  'Mercury and 3I/ATLAS are and goes red if the room disagrees, the "Room '
  'clock" row (L-541 (a plan\'s clock)).\n'
  "> - Two website nights went red, Nov 21's runs 49 and 50, on one line of "
  'INTERACTIVE_AS_BUILT.md. It was green on your computer only because nine '
  'folders left by a build of Nov 19 hid it. Fixed and pushed the same '
  'afternoon; the nights are green again (L-529 (guided encounters), L-543 '
  '(green on your computer, red on GitHub)).\n'
  '> - A walk, which loads the page itself, caught what 53 green rows did '
  "not: three boxes printing a path's day one day early. It was fixed before "
  'the push. The walks are not in the gallery run; whether they join it is '
  'yours, under Waiting on you (L-545 (checks that wait to be '
  'remembered)).\n'),
 ('documentation/WHERE_WE_ARE.md',
  "> **Do next:** *Your push and the reel's place (below); then the "
  "encounter's slice 2, its talk first (L-529 (guided encounters)); beside "
  "it, this round's cleanup (the road, line b), whose briefs are not written "
  'yet.*\n',
  '> **Do next:** *The cleanup, in the order set Nov 21: every entry checked '
  'against JPL, L-539 (every entry checked), in the orrery, its brief not '
  "written yet; then the orbiters' hourly points, L-538 (the orbiters' "
  "printed error); then the encounter's slice 2, its talk first (L-529 "
  '(guided encounters)). The next coordinating session also writes the skill '
  "text the clock's build owes, before the next website build.*\n"),
 ('documentation/WHERE_WE_ARE.md',
  "> - *(do) Start the Code session for the rooms' clock: open Claude Code "
  'in python_work, Opus, high effort, and paste '
  '`documentation/PROMPT_code_L541_room_clock_20261121.md` from below its '
  'line. The live rooms draw every body 69 seconds behind the UTC minute '
  'shown; your ruling of Nov 21: "Yes", convert (L-541 (a plan\'s clock)). '
  'The two skills are reinstalled and v3.144 is pasted, confirmed Nov 21.*\n'
  '> - *(do) Push the website and then the orrery; then in the gallery '
  'editor select the reel (Solar System, Lobby only), Add place... Earth, '
  "Save All, push; then look on your phone: Earth's Links fold, its words, "
  'and the reel opening in a new tab (L-540 (a reel on a Featured card)).*\n',
  '> - *(do) The reel: if its place is not pushed yet, commit it in the '
  'website, then Pull origin, then Push origin. Then on your phone look for '
  "Links in Earth's fold, between Encounters and Saved pictures, and tap the "
  'reel (L-540 (a reel on a Featured card)).*\n'
  '> - *(do) Start the next coordinating session with '
  '`documentation/PROMPT_coordinator_start_20261122_2.md`, pasted from below '
  'its line.*\n'),
 ('documentation/WHERE_WE_ARE.md',
  "               and the first encounter, ESCAPADE's Earth flybys, Nov 20, "
  'on your phone look (L-529 (guided encounters)); then Uranus and Neptune. '
  'Io, Titan, Charon and Pluto come to standard in their folds.*\n',
  "               and the first encounter, ESCAPADE's Earth flybys, Nov 20, "
  "on your phone look (L-529 (guided encounters)); the live rooms' clock set "
  "right Nov 21 (L-541 (a plan's clock)); then Uranus and Neptune. Io, "
  'Titan, Charon and Pluto come to standard in their folds.*\n'),
 ('documentation/WHERE_WE_ARE.md',
  "  b.   [beside] This round's cleanup, each ruled Nov 19 (the order is "
  "yours): every path to its last day, L-533 (ESCAPADE); the orbiters' "
  "hourly points, L-538 (the orbiters' printed error); every entry checked "
  "against JPL, L-539 (every entry checked); the period's swing in its "
  "sentence, L-536 (a moon's yearly change); the 24 in goldenrod, L-432 (the "
  'default goldenrod), at your desk.\n',
  "  b.   [beside] This round's cleanup, each ruled Nov 19, in the order set "
  'Nov 21: every entry checked against JPL, L-539 (every entry checked); '
  "then the orbiters' hourly points, L-538 (the orbiters' printed error); "
  "then every path to its last day, L-533 (ESCAPADE); the period's swing in "
  "its sentence, L-536 (a moon's yearly change); the 24 in goldenrod, L-432 "
  '(the default goldenrod), at your desk.  << moved this session\n'),
 ('documentation/WHERE_WE_ARE.md',
  '## Settled\n'
  '\n'
  'Standing rulings; a line leaves once it is habit, or a skill carries '
  'it.\n',
  '## Settled  **>> UPDATED THIS SESSION**\n'
  '\n'
  'Standing rulings; a line leaves once it is habit, or a skill carries it.\n'
  "- A visitor reads UTC everywhere. The room adds JPL's clock difference "
  "before it looks up JPL's data; only a body's source line names JPL's "
  "clock, for the date of its orbit; a plan's moments print as UTC (Nov 21, "
  'your "Yes"; L-541 (a plan\'s clock)).\n'),
 ('documentation/WHERE_WE_ARE.md',
  '- The points are served a day apart, an hour apart from yesterday to the '
  "day after tomorrow; colours and name sides as built, Earth-Moon L1's name "
  'on the left; the pile-up in the Solar System view stays (Nov 19; L-297 '
  '(the Lagrange points)).\n'
  "- The curve's error is on for the Lagrange points and the open-path "
  'comets only, held by the daily "Curve error" check (Nov 19; L-297 (the '
  'Lagrange points)).\n',
  ''),
 ('documentation/WHERE_WE_ARE.md',
  '## Deferred  **>> UPDATED THIS SESSION**\n',
  '## Deferred\n'),
 ('documentation/WHERE_WE_ARE.md',
  '## Signals\n'
  '\n'
  'Read from files when this page was written, not typed from memory.\n'
  '- Last cache build: 20261120T202853Z, ok, no retry on the swap (the '
  "website's swap log at ae56a944, read Nov 20).\n"
  '- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md at '
  'orrery 1c0688ca, generated Nov 19, read Nov 20).\n'
  "- This page's date and the ledger's newest stamp: both Nov 21. Agree.\n",
  '## Signals  **>> UPDATED THIS SESSION**\n'
  '\n'
  'Read from files when this page was written, not typed from memory.\n'
  '- Last cache build: 20261122T034324Z, ok, no retry on the swap (the '
  "website's swap log at 15eec699, read Nov 21).\n"
  '- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md at '
  'orrery e8cc7f11, generated Nov 20, read Nov 21).\n'
  "- This page's date and the ledger's newest stamp: both Nov 21. Agree.\n"),
 ('documentation/WHERE_WE_ARE.md',
  '## Waiting on you\n'
  '\n'
  'Decisions, one at a time:\n'
  '- None open. The last day was ruled Nov 19: yes, each path asks for its '
  "span's last day (L-533 (ESCAPADE)).\n",
  '## Waiting on you  **>> UPDATED THIS SESSION**\n'
  '\n'
  'Decisions, one at a time:\n'
  "- Whether the gallery's checks are read from a copy holding only what a "
  "push carries, before every website push. Nov 21's red nights were green "
  'on your computer. Your "-- okay" was to raising it (L-543 (green on your '
  'computer, red on GitHub)).\n'
  '- Whether the two walks join the gallery run, which means the website '
  'keeps one more library; and when the recorded Earth scene is re-recorded. '
  'Your words, Nov 21: "should this be method?" The session\'s part is '
  'method now; these two are yours (L-545 (checks that wait to be '
  'remembered)).\n'),
 ('documentation/WHERE_WE_ARE.md',
  '- This round: L-529 (guided encounters), its brief '
  '`COORD_L529_encounter_escapade_earth_brief_20261120.md`, the design '
  "record `DESIGN_encounters_20261120.md`; the website's "
  '`INTERACTIVE_AS_BUILT.md`, Encounters; the tool '
  '`tools/encounter_fetch.py` and its package under `data/encounters/`.\n',
  "- This round: L-541 (a plan's clock), its brief "
  '`COORD_L541_room_clock_brief_20261121.md` and its survey '
  "`SURVEY_L541_clock_69s_20261121.md`; the website's "
  "`INTERACTIVE_AS_BUILT.md`, The rooms' clock; the check "
  '`documentation/smoke_room_clock.js`. The encounter: L-529 (guided '
  'encounters), `DESIGN_encounters_20261120.md`.\n')]


def main():
    for rel, text in NEW_FILES:
        path = os.path.join(HERE, *rel.split('/'))
        if os.path.exists(path):
            with open(path, 'rb') as f:
                have = f.read().replace(b'\\r\\n', b'\\n')
            if have != text.encode('ascii'):
                print("ERROR: %s already exists and differs from this patch's "
                      "copy (a copy saved from a download?). Delete it and run "
                      "again. NOTHING was written." % rel)
                sys.exit(1)
    staged = {}
    for name, old, new in EDITS:
        path = os.path.join(HERE, *name.split('/'))
        if not os.path.exists(path):
            print("ERROR: %s not found next to this script. Is the script "
                  "in the orrery folder (palomas_orrery_for_github)? "
                  "NOTHING was written." % name)
            sys.exit(1)
        if name not in staged:
            with open(path, 'rb') as f:
                raw = f.read()
            staged[name] = [raw.replace(b'\\r\\n', b'\\n'), b'\\r\\n' in raw]
        text = staged[name][0]
        o, n = old.encode('ascii'), new.encode('ascii')
        c = text.count(o)
        if c != 1:
            print("ANCHOR FAIL: %s, expected 1 match, found %d: %r\\n"
                  "If this patch already ran, there is nothing to do. If "
                  "it has not, the file is not the one pushed at e8cc7f11: "
                  "tell the session, and change nothing. NOTHING was "
                  "written." % (name, c, old[:70]))
            sys.exit(1)
        staged[name][0] = text.replace(o, n)
        print("ok   %s: %s" % (name, old.strip().splitlines()[0][:60]))
    for rel, text in NEW_FILES:
        path = os.path.join(HERE, *rel.split('/'))
        if os.path.exists(path):
            print("ok   %s: already there, identical" % rel)
            continue
        with open(path, 'wb') as f:
            f.write(text.encode('ascii'))
        print("new  %s" % rel)
    for name, (text, was_crlf) in staged.items():
        with open(os.path.join(HERE, *name.split('/')), 'wb') as f:
            f.write(text)
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % name)
    print("patch applied (%d new files, %d edits in %d files)"
          % (len(NEW_FILES), len(EDITS), len(staged)))
    for tool in (["ledger_index.py"], ["doc_index.py", "--caps"]):
        r = subprocess.run([sys.executable] + tool, cwd=HERE,
                           capture_output=True, text=True)
        if r.returncode != 0:
            print((r.stdout or '')[-1500:] + (r.stderr or '')[-800:])
            print("ERROR: %s exited %d. The edits above are written; "
                  "tell the session what it printed." % (' '.join(tool),
                                                        r.returncode))
            sys.exit(1)
        print("ok   %s" % ' '.join(tool))
    print("Next: move this patch to documentation, then commit and push "
          "the orrery.")


if __name__ == '__main__':
    main()
