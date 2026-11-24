"""
patch_L538_2_partB_ruling_and_encounter.py -- the records of the
coordinating session's morning of Nov 24, 2026: the Part A report of
L-538 (the orbiters' printed error) read, Tony's ruling on BepiColombo,
the go-ahead for Part B, and BepiColombo's arrival at Mercury added to
the encounters of L-529 (guided encounters).

Built on 6a42ab3bc703bac58ad80d9b738c3cd546803d47 at
https://github.com/tonylquintanilla/palomas_orrery (branch main), with
gallery 9e7bb99ffb77799759abe5a3e6d6dc556853da8e at
https://github.com/tonylquintanilla/tonyquintanilla.github.io read for
its page's loader and its served features. Written by the coordinating
session (Claude Fable 5.2) under safe-file-editing 1.15 and
ledger-and-session-records 1.24. It runs after
patch_L538_1_design_and_brief.py, which is pushed.

Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\

RUN COMMAND
    This file is in the orrery folder (palomas_orrery_for_github). Open
    it in VS Code and click Run:

        python patch_L538_2_partB_ruling_and_encounter.py

    Success: one "ok" line per edit, "patch applied", "wrote" for the
    go-ahead, then two tools, each printing "ok": ledger_index.py and
    doc_index.py --caps.
    Failure: an "ERROR:" or "ANCHOR FAIL" line, and NOTHING is written.
    Undo after a success: Discard Changes in GitHub Desktop.
    Once it has run, move it to the documentation folder.

WHAT IT CHANGES (no code, no skill, no protocol)
    LEDGER_CONSOLIDATED.md
        L-538 (the orbiters' printed error): the Part A report, the
        session's wrong estimate of Nov 23, Tony's ruling of Nov 24 in
        his words, a new Gap, the report and the go-ahead named.
        L-529 (guided encounters): BepiColombo's arrival at Mercury as
        an encounter, Tony's words, what was read, what is open.
        L-533 (ESCAPADE): one line for its last-day build, the false
        "This mission ended".
    documentation/WHERE_WE_ARE.md, above the marker only: the header,
        the three "Changed" lines, "Do next", the road's line b, one
        Settled line, one Signals line, one line under Waiting on you
        made longer, Where the details are. No line added or removed.
    documentation/COORD_L538_partB_goahead_20261124.md: new, the answer
        to the Part A report and the go-ahead for Part B.

Permanent: the records and the go-ahead. This script is one-shot.

Written November 24, 2026 with Anthropic's Claude Fable 5.2.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

EDITS = [('documentation/WHERE_WE_ARE.md',
  'Last updated: November 23, 2026, night: step 3 of L-522 (document caps) '
  "confirmed from GitHub, and the design of L-538 (the orbiters' printed "
  'error) with its brief (Claude Fable 5.2, the coordinating session).\n'
  '- Written on orrery 2634031c and gallery 9e7bb99f, both pushed; both last '
  "nights read clean from their own records (the orrery's of Nov 23, 22:44 "
  "UTC; the website's of Nov 24, 00:02 UTC, 59 rows).\n",
  "Last updated: November 24, 2026, morning: L-538 (the orbiters' printed "
  "error), its Part A report read and its Part B ruled; BepiColombo's "
  'arrival at Mercury added to the encounters (Claude Fable 5.2, the '
  'coordinating session).\n'
  '- Written on orrery 6a42ab3b and gallery 9e7bb99f, both pushed; no night '
  'has run on either since the page was last written.\n'),
 ('documentation/WHERE_WE_ARE.md',
  "> - Step 3 is confirmed by comparison, not by anyone's word: all twelve "
  "of your installed skills equal the repository's copies, the Project's "
  'protocol reads v4.0, and Part 3 with its four corrections is on GitHub.\n'
  '> - L-538 (the orbiters\' printed error) has its design, on your "Yes" of '
  'Nov 23: a craft orbiting a planet is served a point a day across every '
  'date the date box offers and a point an hour apart around today, and '
  'finer points wherever the check finds that too coarse. Today that is Juno '
  "and BepiColombo, which reached Mercury on Nov 21 by JPL's path.\n"
  "> - The fault is larger than the ledger said. Juno's points are up to 49 "
  'days apart inside the date window, not a week. Tested point by point, its '
  'marker missed by up to 8.3 million km where the box claimed 3.8 '
  'million.\n',
  "> - L-538 (the orbiters' printed error): the Code session's first report "
  "is in. Juno's fix is cheap, 48 KB. BepiColombo's would have cost about 1 "
  'MB on every visit to the room, so you ruled (Nov 24): fine points around '
  'today, a point a day on the other days, and there a coarser, true figure '
  'in its box, never smaller than the reach of its loop around Mercury.\n'
  '> - The usual test was blind for BepiColombo: a point a day passed it '
  'while the box was wrong by up to twice its figure. The build adds a '
  "second test, against JPL's own points in between. The session's estimate "
  'of Nov 23, about 22 KB a craft, was wrong for BepiColombo by 30 times and '
  'more.\n'
  "> - BepiColombo's arrival at Mercury (Nov 21) is on the encounter list, "
  "with Mercury's features drawn, the Hill sphere above all (you, Nov 24; "
  'L-529 (guided encounters)). The website serves no Mercury features yet, '
  'so those come first.\n'),
 ('documentation/WHERE_WE_ARE.md',
  'start a Claude Code session with its brief, '
  '`documentation/COORD_L538_orbiters_brief_20261123.md`; it stops after its '
  'Part A report, which goes to the coordinating session before any edit. '
  'Then every path',
  'tell its Claude Code session to go ahead with Part B by '
  '`documentation/COORD_L538_partB_goahead_20261124.md`; it reports once '
  "more before it touches the room's code. Then every path"),
 ('documentation/WHERE_WE_ARE.md',
  'designed Nov 23, its brief written << moved this session;',
  'designed Nov 23, measured and its Part B ruled Nov 24 << moved this '
  'session;'),
 ('documentation/WHERE_WE_ARE.md',
  '- A craft orbiting a planet gets the real fix and no stopgap: a point a '
  'day across the date window, a point an hour apart around today, and finer '
  'points where the check finds that too coarse (Nov 19 and 23; L-538 (the '
  "orbiters' printed error)).\n",
  '- A craft orbiting a planet gets the real fix and no stopgap. Where its '
  'fine points across the date window stay small (Juno), it is served them. '
  'Where they do not (BepiColombo), fine points around today, a point a day '
  'elsewhere, and a coarser, true figure on the other days (Nov 19, 23 and '
  "24; L-538 (the orbiters' printed error)).\n"),
 ('documentation/WHERE_WE_ARE.md',
  "- This page's date and the ledger's newest stamp: both Nov 23. Agree.\n",
  "- This page's date and the ledger's newest stamp: both Nov 24. Agree.\n"),
 ('documentation/WHERE_WE_ARE.md',
  '- Where the four small builds from the decisions of Nov 22 sit in the '
  "order. Until you say: after the protocol's reduction, at the gaps between "
  'builds (the road, line b).\n',
  '- Where the four small builds from the decisions of Nov 22 sit in the '
  "order. Until you say: after the protocol's reduction, at the gaps between "
  "builds (the road, line b). And where BepiColombo's arrival at Mercury "
  'sits (L-529 (guided encounters)): the session recommends right after '
  "L-538 (the orbiters' printed error), ahead of the polish of ESCAPADE's "
  'slice 2.\n'),
 ('documentation/WHERE_WE_ARE.md',
  'its brief `COORD_L538_orbiters_brief_20261123.md`.\n',
  'its brief `COORD_L538_orbiters_brief_20261123.md`, the Part A report '
  '`REPORT_L538_partA_20261124.md`, the go-ahead '
  '`COORD_L538_partB_goahead_20261124.md`.\n'),
 ('LEDGER_CONSOLIDATED.md',
  '<!-- L:538 status:OPEN upd:2026-11-23 section:A flag: rice: -->',
  '<!-- L:538 status:OPEN upd:2026-11-24 section:A flag: rice: -->'),
 ('LEDGER_CONSOLIDATED.md',
  '**Gap:** the build, by the brief, in one Claude Code session in the\n'
  'website repository. Its Part A (the map, the measure against JPL, its\n'
  'proposal) returns to a coordinating session before any edit. Then the\n'
  'skill text for gallery-cache-builder, which stands at its cap. Until\n'
  'the build, those boxes claim less error than they have.\n',
  '**Note:** (2026-11-24, morning, the same coordinating session, Claude\n'
  'Fable 5.2, on orrery 6a42ab3b and gallery 9e7bb99f) PART A READ, AND\n'
  "TONY'S RULING ON BEPICOLOMBO.\n"
  '- Tony, 08:12, after the session told him the finer-step rule covers\n'
  '  the daily part: "yes". The session read it as accepting that and\n'
  '  said so; he did not say otherwise. `patch_L538_1_design_and_brief.py`\n'
  '  ran and is pushed at 6a42ab3b.\n'
  '- The Part A report, `documentation/REPORT_L538_partA_20261124.md`\n'
  "  (the Claude Code session, Claude Opus 5.5), read whole from Tony's\n"
  '  folder, 16,780 bytes, not yet on GitHub. Its figures are its own, not\n'
  '  checked here: Juno cured at 45 minutes on its six close passes of\n'
  '  Jupiter in the window, 636 points, about 48 KB; BepiColombo passes\n'
  '  the held-out test with a point a day while its box is wrong at 56 of\n'
  '  728 real minutes, by up to 2.0 times, so a second test is needed,\n'
  "  against JPL's own points between the served ones; with both tests it\n"
  '  settles at 15 minutes, 6,179 points and about 472 KB stretch by\n'
  '  stretch, about 9,700 points and 740 KB day by day; its loop around\n'
  '  Mercury is 28 hours just after arrival, 4.40 hours by 2027-01-20,\n'
  "  2.37 hours by 2027-04-06; the chord figure holds, the curve's does\n"
  '  not.\n'
  '- THE SESSION\'S ESTIMATE OF NOV 23 WAS WRONG: "about 270 more points\n'
  '  per craft, roughly 22 KB each". For BepiColombo the measured cost is\n'
  '  30 times that and more, and Tony\'s "Yes" of Nov 23 was given on it.\n'
  "- What the session added, by its own arithmetic from the report's\n"
  '  figures and by reading `interactive.html` at 9e7bb99f: the 740 KB is\n'
  "  today's size, and the fine span grows as the window moves, to about\n"
  "  13,400 points and 1.0 MB by mid-January, past the report's own limit\n"
  '  of 12,000 points about the end of December; and\n'
  "  `solarSystemPositionFiles` fetches every spacecraft's positions file\n"
  '  before the room draws, 42 files, 1,084 KB together.\n'
  "- Tony, 09:30, on the report's question (about 470 KB or about 740\n"
  '  KB): "I think it\'s okay. Comments?" The session\'s recommendation:\n'
  '  "Juno gets the full fix as measured. BepiColombo gets fine points\n'
  '  only for the few days around today, and a point a day elsewhere. On\n'
  '  the other days its box prints a coarser, true figure: an error no\n'
  '  smaller than the reach of its loop around Mercury, which the builder\n'
  '  measures from JPL each night. The same second test proves it. The\n'
  '  loop itself goes in the BepiColombo encounter you asked for this\n'
  '  morning, loaded only by a visitor who opens it." And: "This needs\n'
  '  your ruling, because on Nov 19 you declined a coarser figure as a\n'
  '  stopgap. I think this one is different: it is permanent and it is\n'
  '  true. But it is a coarser figure." Tony, 09:38: "I agree with your\n'
  '  recommendation. Fine points around today. And we should also draw\n'
  '  the Mercury features for this close encounter especially the hill\n'
  '  sphere."\n'
  '- SO RULED, Nov 24: for a craft whose loop is too short for fine\n'
  '  points across the window to stay small, fine points around today, a\n'
  '  point a day elsewhere, and outside the band a figure never smaller\n'
  '  than the reach of its loop. It sets aside the whole-window part of\n'
  '  the Nov 23 ruling for such a craft. It was put to him as a coarser\n'
  '  figure and as different from the stopgap he declined on Nov 19.\n'
  "- The session's reading, as method and not his words: which craft\n"
  '  gets which shape is decided by a measured size, not by a name.\n'
  '- The go-ahead for Part B:\n'
  '  `documentation/COORD_L538_partB_goahead_20261124.md`. It restates the\n'
  "  outcomes, asks for the floor's form and where it enters the room\n"
  "  before the room's code is touched, and carries four smaller things:\n"
  "  the limits measured before they are set, the check points' times\n"
  "  moved each night, how fresh JPL's path is, what a night commits.\n"
  '- Re-homed: "This mission ended" on days past the end of JPL\'s data,\n'
  "  to L-533 (ESCAPADE), every path to its last day. BepiColombo's loop\n"
  '  drawn, to L-529 (guided encounters).\n'
  '**Gap:** Part B, by the brief and the go-ahead, in the same Claude\n'
  'Code session: one more report, on the floor and the room, before the\n'
  "room's code is touched; then Part C and Tony's look on his phone. Then\n"
  'the skill text for gallery-cache-builder, which stands at its cap.\n'
  'Until the build, those boxes claim less error than they have.\n'),
 ('LEDGER_CONSOLIDATED.md',
  'placed by `patch_L538_1_design_and_brief.py`.\n',
  'placed by `patch_L538_1_design_and_brief.py`; the Part A report,\n'
  '`documentation/REPORT_L538_partA_20261124.md`; the go-ahead,\n'
  '`documentation/COORD_L538_partB_goahead_20261124.md`, placed by\n'
  '`patch_L538_2_partB_ruling_and_encounter.py`.\n'),
 ('LEDGER_CONSOLIDATED.md',
  '<!-- L:529 status:OPEN upd:2026-11-22 section:A flag: rice: -->',
  '<!-- L:529 status:OPEN upd:2026-11-24 section:A flag: rice: -->'),
 ('LEDGER_CONSOLIDATED.md',
  '**Gap:** slice 2, its talk first: the two close passes and how the\n',
  '**Note:** (2026-11-24, the coordinating session, Claude Fable 5.2, on\n'
  "orrery 6a42ab3b and gallery 9e7bb99f) BEPICOLOMBO'S ARRIVAL AT MERCURY,\n"
  'AN ENCOUNTER FOR THE LIST. Tony, 08:51: "bepi colombo just arrived at\n'
  'mercury. can we add this close encounter to the list? it may be a\n'
  'useful test of this architecture too." Tony, 09:38: "And we should\n'
  'also draw the Mercury features for this close encounter especially the\n'
  'hill sphere."\n'
  '- What happened, read on the web on Nov 24 and not from JPL: ESA\n'
  '  confirmed the capture into orbit of 2026-11-21; a software fault\n'
  '  ended the burn short of its planned 37 minutes; the burn was about\n'
  '  635 km above the surface (europeanspaceflight.com, "BepiColombo\n'
  '  Enters Orbit Around Mercury Despite Software Glitch"). ESA\'s\n'
  '  timeline: the two orbiters part on 9 to 10 December 2026, MPO\n'
  '  reaches its final orbit on 10 March 2027, science begins 6 April\n'
  '  2027 (esa.int, "BepiColombo arrival at Mercury timeline").\n'
  '- What the website holds: the plan of Nov 4 has the arrival at\n'
  "  2026-11-21 18:48, 3,073.0 km from Mercury's centre, staying. L-538's\n"
  "  Part A found JPL's answer of Nov 24 thousands of km from that plan's\n"
  '  points within a minute, and the loop 28 hours long just after\n'
  '  arrival, 3,062 to 55,341 km from the centre (its report; not checked\n'
  "  here). How recent JPL's path is, and whether it holds the orbit\n"
  "  after the short burn, is not read; L-538's Part B prints it.\n"
  "- Why it tests the architecture (the session's reading, told to\n"
  '  Tony): a new kind, an arrival that stays, where slice 1 was a pass;\n'
  "  a new body, the first row in Mercury's fold; and this item's own\n"
  '  open question, a measurement replacing a prediction, as a live case.\n'
  '- What Mercury has to draw: the orrery draws eight things for it\n'
  '  (`mercury_visualization_shells.py`: inner core, outer core, mantle,\n'
  '  crust, atmosphere, sodium tail, magnetosphere, Hill sphere). The\n'
  '  website serves none of them: `data/solar-system/feature_configs.json`\n'
  '  at 9e7bb99f holds features for the Sun (6), Earth (9), Jupiter (3)\n'
  '  and Saturn (2), an empty entry for Mercury, and a Hill sphere for\n'
  "  the Sun and for Earth alone. So this encounter needs Mercury's\n"
  '  features served first, the Hill sphere at least.\n'
  "- From L-538 (the orbiters' printed error), ruled the same morning:\n"
  "  BepiColombo's loop around Mercury is not served to the Solar System\n"
  '  room; its fine points belong to this package, loaded by the visitor\n'
  '  who opens it.\n'
  "- OPEN, for its talk: where an arrival's encounter ends (the capture,\n"
  "  the first loop, the orbiters' parting); which of the eight features;\n"
  "  whether it waits for JPL's path after the burn; and its place in the\n"
  '  order. The session asked whether right after L-538, ahead of slice\n'
  "  2's polish, as it recommends, or after slice 2: not yet answered.\n"
  "**Gap:** BepiColombo's arrival at Mercury as an encounter, its talk\n"
  "first, its place in the order Tony's to say (the note of 2026-11-24).\n"
  'Slice 2, its talk first: the two close passes and how the\n'),
 ('LEDGER_CONSOLIDATED.md',
  '<!-- L:533 status:OPEN upd:2026-11-23 section:A flag: rice: -->',
  '<!-- L:533 status:OPEN upd:2026-11-24 section:A flag: rice: -->'),
 ('LEDGER_CONSOLIDATED.md',
  "orbit insertion; the plan's 30-day remake shows it if JPL trims that.\n",
  "orbit insertion; the plan's 30-day remake shows it if JPL trims that.\n"
  "For the last-day build (2026-11-24, from L-538's Part A report, not\n"
  "checked by the coordinating session): past the end of JPL's data for a\n"
  'craft still flying, the box reads "This mission ended on ...", which\n'
  "is false. BepiColombo's data ends 2027-04-10, and the date window\n"
  'reaches that day about 2027-01-12.\n')]

DOC_PATH = 'documentation/COORD_L538_partB_goahead_20261124.md'

DOC_TEXT = (
    "<!-- Doc-Kind: hand | The coordinating session's answer to the Part A report of L-538 (the orbiters' printed error): Tony's ruling of Nov 24, what changes in the proposal, and the go-ahead for Part B. -->\n"
    "# Go-ahead for Part B: the orbiters' printed error (L-538)\n"
    '\n'
    'Built on orrery 6a42ab3bc703bac58ad80d9b738c3cd546803d47 at\n'
    'https://github.com/tonylquintanilla/palomas_orrery (branch main) and\n'
    'gallery 9e7bb99ffb77799759abe5a3e6d6dc556853da8e at\n'
    'https://github.com/tonylquintanilla/tonyquintanilla.github.io.\n'
    'Written November 24, 2026 by the coordinating session (Claude Fable\n'
    '5.2) for the Claude Code session that wrote\n'
    '`documentation/REPORT_L538_partA_20261124.md`. It amends\n'
    '`documentation/COORD_L538_orbiters_brief_20261123.md`; where the two\n'
    'differ, this one holds.\n'
    '\n'
    "Tony's local folders: orrery\n"
    'C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\\n'
    'gallery\n'
    'C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\\n'
    '\n'
    "The report was read whole from Tony's folder (16,780 bytes), not from\n"
    "its summary. Say back that you read this file, and L-538's note of\n"
    '2026-11-24 in the ledger.\n'
    '\n'
    '## 1. The ruling\n'
    '\n'
    'Your question was a BepiColombo file of about 470 KB or about 740 KB.\n'
    'Neither. What the coordinating session read and told Tony:\n'
    "- The 740 KB is today's size. The fine span starts at the arrival and\n"
    '  the window moves forward over it: 140 days at 96 points a day is\n'
    '  about 13,400 points, about 1.0 MB, by mid-January, and more if JPL\n'
    '  extends its data past 2027-04-10. That passes your own limit of\n'
    "  12,000 points about the end of December. (The session's arithmetic\n"
    '  from your figures; check it.)\n'
    '- Every visitor pays for it. `solarSystemPositionFiles` in\n'
    "  `interactive.html` fetches every spacecraft's positions file among\n"
    "  the room's rows before the room draws. The 42 files are 1,084 KB\n"
    '  together at gallery 9e7bb99f.\n'
    "- By April the loop is within 4,000 km of Mercury's centre. At the\n"
    "  room's scale the marker sits on Mercury either way.\n"
    '\n'
    'The session\'s recommendation, as put to Tony: "Juno gets the full fix\n'
    'as measured. BepiColombo gets fine points only for the few days around\n'
    'today, and a point a day elsewhere. On the other days its box prints a\n'
    'coarser, true figure: an error no smaller than the reach of its loop\n'
    'around Mercury, which the builder measures from JPL each night. The\n'
    'same second test proves it. The loop itself goes in the BepiColombo\n'
    'encounter you asked for this morning, loaded only by a visitor who\n'
    'opens it." And: "This needs your ruling, because on Nov 19 you declined\n'
    'a coarser figure as a stopgap. I think this one is different: it is\n'
    'permanent and it is true. But it is a coarser figure."\n'
    '\n'
    'Tony, November 24, 2026, 09:38: "I agree with your recommendation. Fine\n'
    'points around today."\n'
    '\n'
    '## 2. The outcomes, restated\n'
    '\n'
    'These replace outcomes 1 to 3 of the brief. Outcomes 4 and 5 stand.\n'
    '1. For a craft inside a capture, on every day the date box offers, the\n'
    "   box's error is never smaller than the real miss, by BOTH tests: its\n"
    "   served points held out, and JPL's own points between them. Your\n"
    '   correction to the brief is taken whole.\n'
    '2. A craft whose fine layer across the whole window stays small (Juno:\n'
    '   636 points) is served it as you proposed, day by day.\n'
    '3. A craft whose fine layer would not stay small (BepiColombo) is\n'
    '   served fine points in the band around today only, and a point a day\n'
    "   across the rest of the window. Outside the band its box's error is\n"
    '   never smaller than a floor: the reach of its loop around its planet.\n'
    '4. The floor is measured from JPL each night and served; never typed.\n'
    '\n'
    "## 3. What is yours to propose in Part B's report, before the room is touched\n"
    '\n'
    "The session's starting points, not rulings:\n"
    '- WHICH CRAFT GETS WHICH is decided by a measured size, never by a\n'
    "  name: a limit on a craft's fine points across the window, with the\n"
    '  band-only shape past it. Tony ruled on BepiColombo; that the same\n'
    "  rule sorts the next craft is the session's reading, as method.\n"
    "  Propose the limit, and show each capture craft's size for every week\n"
    "  from now to the end of its span, not today's alone.\n"
    '- THE BAND. Yesterday to the day after tomorrow, as ruled Nov 23,\n'
    '  refined by both tests as you measured (30 minutes today). Say whether\n'
    '  a visitor who opens the room late in a served night can fall outside\n'
    '  it.\n'
    "- THE FLOOR. Worked from a quantity with a name: the craft's distance\n"
    "  from its planet's centre, from JPL's points around that centre, over\n"
    '  the loops of that day. Propose the exact form (the farthest distance,\n'
    '  twice it, or what the geometry gives) and why. It is then TESTED\n'
    "  against JPL's check points. A floor fitted to the points that test it\n"
    '  cannot fail: the points it is worked from and the points that test it\n'
    '  are different points, and the report says which is which.\n'
    "- WHERE THE FLOOR ENTERS. Part A's map says the room is not touched;\n"
    '  now it is. `position_at` makes the error and three places in\n'
    '  `interactive.html` read it. Propose where the larger of the chord\n'
    '  figure and the floor is taken, so there is one place, and map every\n'
    '  reader again, the golden artifacts and the smoke suites included.\n'
    "- THE BOX'S WORDS do not change: the same sentence prints fewer digits.\n"
    '  If you think the box must say why, that is a question for Tony; put\n'
    '  it in the report and change nothing.\n'
    '\n'
    '## 4. Four smaller things\n'
    '\n'
    '- THE LIMITS (12,000 points, 60 questions) were set before the day by\n'
    '  day build was measured: Part A asked 557 questions stretch by\n'
    "  stretch and did not run the other. Measure a night's questions and\n"
    '  seconds for both craft, check points included, then set the limits\n'
    '  with room to spare.\n'
    "- THE CHECK POINTS' TIMES MOVE EACH NIGHT. A point every 37 minutes\n"
    '  from a fixed start meets a loop at the same few places whenever the\n'
    "  loop's period is a multiple of 37 minutes, and BepiColombo's passes\n"
    '  through several (148, 185, 222, 259 minutes) between January and\n'
    '  April. Shift the start each night by an amount worked from the date,\n'
    '  so a night can be run again, and print it in the record.\n'
    "- HOW FRESH JPL'S PATH IS. The served file's arrival, from the plan of\n"
    "  Nov 4, is thousands of km from JPL's answer of Nov 24, and ESA\n"
    '  reported the capture burn cut short. Print, for each capture craft,\n'
    "  what JPL's answer says of its own path's date or version, in the\n"
    "  build's record. Do not remake the plan; say whether its old events\n"
    "  inside the capture mislead the room's list.\n"
    '- WHAT A NIGHT COMMITS. The check points are saved and not served. Say\n'
    "  whether they are committed, and measure the nightly commit's growth\n"
    "  in Part C against the repository's size, as your own last thought\n"
    '  asks.\n'
    '\n'
    'NOT IN THIS BUILD, as before, and two more:\n'
    '- "This mission ended" on days past the end of JPL\'s data for a craft\n'
    '  still flying (BepiColombo past 2027-04-10, in the window from about\n'
    '  2027-01-12). It goes to L-533 (ESCAPADE), every path to its last\n'
    '  day, the next build. Your closing records add the line there.\n'
    "- BepiColombo's loop around Mercury, drawn. It belongs to an encounter\n"
    "  of its own, L-529 (guided encounters), with Mercury's features and\n"
    '  its Hill sphere (Tony, Nov 24).\n'
    '\n'
    '## 5. Go ahead\n'
    '\n'
    'Part B may start, in this order: the measure and the proposals of\n'
    "section 3 first, with no edit to the room's code, and a short report;\n"
    'the builder, the validator and the widened check may be built before\n'
    "that report where section 3 does not reach them (Juno's layer, the\n"
    "capture function, the served block, yesterday's hours). Read\n"
    '`safe-file-editing` and `ledger-and-session-records` whole before the\n'
    "first edit, as your report said you would. The brief's section 4\n"
    '(delivery) and section 5 (the report) stand.\n'
    '\n'
    "Written November 2026 with Anthropic's Claude Fable 5.2.\n"
)


def main():
    staged = {}
    for name, old, new in EDITS:
        path = os.path.join(HERE, *name.split('/'))
        if not os.path.exists(path):
            print("ERROR: %s not found next to this script. Is it in the "
                  "orrery folder? NOTHING was written." % name)
            sys.exit(1)
        if name not in staged:
            with open(path, 'rb') as f:
                raw = f.read()
            staged[name] = [raw.replace(b'\r\n', b'\n'), b'\r\n' in raw]
        text = staged[name][0]
        o, n = old.encode('ascii'), new.encode('ascii')
        c = text.count(o)
        if c != 1:
            print("ANCHOR FAIL: %s, expected 1 match, found %d: %r\n"
                  "If this patch already ran, there is nothing to do. "
                  "Otherwise the file moved since this was built: tell the "
                  "session. NOTHING was written." % (name, c, old[:70]))
            sys.exit(1)
        staged[name][0] = text.replace(o, n)
        print("ok   %s: %s" % (name, (old.strip().splitlines()
                                      or ['(end)'])[0][:52]))
    dpath = os.path.join(HERE, *DOC_PATH.split('/'))
    dbytes = ''.join(DOC_TEXT).encode('ascii')
    write_doc = True
    if os.path.exists(dpath):
        with open(dpath, 'rb') as f:
            have = f.read().replace(b'\r\n', b'\n')
        if have == dbytes:
            write_doc = False
        else:
            print("ERROR: %s already exists and differs from the one this "
                  "patch places. Likely a copy saved by hand: delete it and "
                  "run again. NOTHING was written." % DOC_PATH)
            sys.exit(1)
    for name, (text, was_crlf) in staged.items():
        with open(os.path.join(HERE, *name.split('/')), 'wb') as f:
            f.write(text)
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % name)
    print("patch applied (%d edits, %d files)" % (len(EDITS), len(staged)))
    if write_doc:
        with open(dpath, 'wb') as f:
            f.write(dbytes)
        print("wrote %s (%d bytes)" % (DOC_PATH, len(dbytes)))
    else:
        print("already there, identical: %s" % DOC_PATH)
    print("stamps updated: Where We Are's header (6a42ab3b, 9e7bb99f); the "
          "dates of L-538, L-529 and L-533 (2026-11-24)")
    for tool in (["ledger_index.py"], ["doc_index.py", "--caps"]):
        r = subprocess.run([sys.executable] + tool, cwd=HERE,
                           capture_output=True, text=True)
        if r.returncode != 0:
            print((r.stdout or '')[-1800:] + (r.stderr or '')[-800:])
            print("ERROR: %s exited %d. The edits above are written; "
                  "Discard Changes in GitHub Desktop undoes them. Tell "
                  "the session what it printed." % (' '.join(tool),
                                                    r.returncode))
            sys.exit(1)
        print("ok   %s" % ' '.join(tool))
    print("")
    print("Do next: move this file into documentation; commit and push")
    print("the orrery, the Part A report with it. Then tell the Claude Code")
    print("session: go ahead with Part B by")
    print("documentation/COORD_L538_partB_goahead_20261124.md.")

if __name__ == '__main__':
    main()
