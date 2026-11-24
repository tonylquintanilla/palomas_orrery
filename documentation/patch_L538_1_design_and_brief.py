"""
patch_L538_1_design_and_brief.py -- the records of the coordinating
session of Nov 23, 2026, night: step 3 of L-522 (document caps)
confirmed from GitHub, the design of L-538 (the orbiters' printed
error) with Tony's ruling, and the brief for its build.

Built on 2634031c19ff78e591ebbdc1d724ff4f0d494484 at
https://github.com/tonylquintanilla/palomas_orrery (branch main), with
gallery 9e7bb99ffb77799759abe5a3e6d6dc556853da8e at
https://github.com/tonylquintanilla/tonyquintanilla.github.io read for
its served cache, its builder and its night record. Written by the
coordinating session (Claude Fable 5.2) under safe-file-editing 1.15
and ledger-and-session-records 1.24, the copies this session loaded and
compared with the repository's.

Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\

RUN COMMAND
    This file is in the orrery folder (palomas_orrery_for_github). Open
    it in VS Code and click Run:

        python patch_L538_1_design_and_brief.py

    Success: one "ok" line per edit, "patch applied", "wrote" for the
    brief, then two tools, each printing "ok": ledger_index.py and
    doc_index.py --caps.
    Failure: an "ERROR:" or "ANCHOR FAIL" line, and NOTHING is written.
    Undo after a success: Discard Changes in GitHub Desktop.
    Once it has run, move it to the documentation folder.

WHAT IT CHANGES (no code, no skill, no protocol)
    LEDGER_CONSOLIDATED.md
        L-538 (the orbiters' printed error): what the served cache
        shows, Tony's ruling of Nov 23 in his words, the design, a new
        Gap, the brief named.
        L-522 (document caps): step 3 confirmed by the closing
        handoff's four checks; the paste and the three reinstalls
        marked done by that comparison.
    documentation/WHERE_WE_ARE.md, above the marker only: the header,
        the three "Changed" lines, "Do next", one "Needs you now" line
        removed (the paste and the reinstalls, confirmed), the road's
        lines d and b, one Settled line, one Signals line, one line
        added under Waiting on you, Where the details are. The same
        count of lines above the marker as before, 130.
    documentation/COORD_L538_orbiters_brief_20261123.md: new, the brief
        for one Claude Code session in the website repository.

Permanent: the records and the brief. This script is one-shot.

Written November 23, 2026 with Anthropic's Claude Fable 5.2.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

EDITS = [('documentation/WHERE_WE_ARE.md',
  "Last updated: November 23, 2026, evening: the close of the protocol's "
  'reduction, step 3 of L-522 (document caps). The protocol is v4.0, 795 '
  'lines (Claude Opus 5.5, in Claude Code).\n'
  '- Written on orrery 0a024d9f and gallery 9e7bb99f, both pushed; the '
  'nights since, read green in your run record.\n',
  'Last updated: November 23, 2026, night: step 3 of L-522 (document caps) '
  "confirmed from GitHub, and the design of L-538 (the orbiters' printed "
  'error) with its brief (Claude Fable 5.2, the coordinating session).\n'
  '- Written on orrery 2634031c and gallery 9e7bb99f, both pushed; both last '
  "nights read clean from their own records (the orrery's of Nov 23, 22:44 "
  "UTC; the website's of Nov 24, 00:02 UTC, 59 rows).\n"),
 ('documentation/WHERE_WE_ARE.md',
  '> - The protocol is shorter: 1,394 lines became 795, the text you '
  'ratified ("ratified. thanks."). Nothing was lost: each old line is in the '
  'protocol, in the history file, or at the end of PROJECT_ORIGIN.md, and a '
  'script found every one. Closed with it: L-199 (protocol length), L-230 (a '
  "skill change's protocol entry), L-499 (kinds of session).\n"
  '> - A skill change no longer makes a new protocol version, so it no '
  'longer asks you to paste the protocol. The table of skills is its own '
  'file now, `skills/SKILL_MANIFEST.md`.\n'
  '> - Three skills changed. The records skill: no protocol entry for a '
  'skill change, and your run-record zone is never emptied. The coding '
  "conventions: six places position data reaches a viewer, the website's own "
  "the sixth. The pre-test: it reads the program's real result, which the "
  'old line hid.\n',
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
  'million.\n'),
 ('documentation/WHERE_WE_ARE.md',
  "> **Do next:** *L-538 (the orbiters' printed error); then every path",
  "> **Do next:** *L-538 (the orbiters' printed error): start a Claude Code "
  'session with its brief, '
  '`documentation/COORD_L538_orbiters_brief_20261123.md`; it stops after its '
  'Part A report, which goes to the coordinating session before any edit. '
  'Then every path'),
 ('documentation/WHERE_WE_ARE.md',
  "> - *(do) Paste PROJECT_INSTRUCTIONS.md, v4.0, into the Project's "
  'instructions on claude.ai (the number is yours to change first), and '
  'reinstall ledger-and-session-records, orrery-coding-conventions and '
  'agentic-pre-test (Plugins, in the claude.ai sidebar). The next session '
  'with a shell checks the three. The handoff is '
  '`documentation/HANDOFF_document_upkeep_20261123_close.md`; the '
  'coordinating session starts with '
  '`documentation/PROMPT_coordinator_start_20261123_1.md`, pasted from below '
  'its line.*\n',
  ''),
 ('documentation/WHERE_WE_ARE.md',
  'built Nov 23 as v4.0 << moved this session;',
  'built Nov 23 as v4.0 and confirmed that night;'),
 ('documentation/WHERE_WE_ARE.md',
  "then the orbiters' hourly points, L-538 (the orbiters' printed error);",
  "then the orbiters' fine points, L-538 (the orbiters' printed error), "
  'designed Nov 23, its brief written << moved this session;'),
 ('documentation/WHERE_WE_ARE.md',
  '- A craft orbiting a planet gets the real fix, hourly points near today, '
  "and no stopgap (Nov 19; L-538 (the orbiters' printed error)).\n",
  '- A craft orbiting a planet gets the real fix and no stopgap: a point a '
  'day across the date window, a point an hour apart around today, and finer '
  'points where the check finds that too coarse (Nov 19 and 23; L-538 (the '
  "orbiters' printed error)).\n"),
 ('documentation/WHERE_WE_ARE.md',
  '## Deferred  **>> UPDATED THIS SESSION**\n',
  '## Deferred\n'),
 ('documentation/WHERE_WE_ARE.md',
  '- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md, '
  "generated Nov 23 by this session's run, on 0a024d9f).\n",
  '- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md, '
  'generated Nov 23, read at 2634031c).\n'),
 ('documentation/WHERE_WE_ARE.md',
  '## Waiting on you\n',
  '## Waiting on you  **>> UPDATED THIS SESSION**\n'),
 ('documentation/WHERE_WE_ARE.md',
  '- Where the four small builds from the decisions of Nov 22 sit in the '
  "order. Until you say: after the protocol's reduction, at the gaps between "
  'builds (the road, line b).\n',
  '- Where the four small builds from the decisions of Nov 22 sit in the '
  "order. Until you say: after the protocol's reduction, at the gaps between "
  'builds (the road, line b).\n'
  '- Three things on the document track never put to you, before step 4 of '
  'L-522 (document caps): the stamping rule (safe-file-editing, "Stamp What '
  'You Change"), which refills the header stamps step 4 empties; a cap for '
  "the website's `INTERACTIVE_AS_BUILT.md`; and a split for "
  'gallery-cache-builder and horizons-orbital-mechanics, both at their caps, '
  "the first due more text after L-538's build.\n"),
 ('documentation/WHERE_WE_ARE.md',
  '- This round: L-539 (every entry checked), its brief '
  '`COORD_L539_every_entry_brief_20261122.md`, the list you scanned '
  '`CHECK_L539_every_entry_names_20261122.md`, the check '
  "`horizons_unserved.py`. The clock: L-541 (a plan's clock). The encounter: "
  'L-529 (guided encounters), `DESIGN_encounters_20261120.md`. The tie: '
  "L-544 (L4 and L5 tie), `patch_L544_1_tie_break.py` in the website's "
  'documentation.\n',
  '- This round: L-539 (every entry checked), its brief '
  '`COORD_L539_every_entry_brief_20261122.md`, the list you scanned '
  '`CHECK_L539_every_entry_names_20261122.md`, the check '
  "`horizons_unserved.py`. The clock: L-541 (a plan's clock). The encounter: "
  'L-529 (guided encounters), `DESIGN_encounters_20261120.md`. The tie: '
  "L-544 (L4 and L5 tie), `patch_L544_1_tie_break.py` in the website's "
  "documentation. The orbiters: L-538 (the orbiters' printed error), its "
  'brief `COORD_L538_orbiters_brief_20261123.md`.\n'),
 ('LEDGER_CONSOLIDATED.md',
  '<!-- L:538 status:OPEN upd:2026-11-22 section:A flag: rice: -->',
  '<!-- L:538 status:OPEN upd:2026-11-23 section:A flag: rice: -->'),
 ('LEDGER_CONSOLIDATED.md',
  '**Gap:** the build, soon (Tony, Nov 19): finer points near today for a\n'
  'craft inside a capture; until then those boxes print up to about one\n'
  'place finer than earned.\n'
  "**Ref:** L-297 (the curve's error, Tony's ruling of Nov 19); gallery\n"
  '`tools/test_curve_error.py` (run with every kind to measure);\n'
  'provenance-discipline, A Computed Position Prints What Its Errors Earn.\n',
  '**Note:** (2026-11-23, night, the coordinating session, Claude Fable\n'
  "5.2, on orrery 2634031c and gallery 9e7bb99f) DESIGNED, AND TONY'S\n"
  'RULING. Read from the served cache built 2026-11-24T00:01 UTC:\n'
  "- Two craft are inside a capture in the date window, by their plans'\n"
  '  arrivals: Juno, and BepiColombo, which arrived at Mercury on\n'
  "  2026-11-21 18:48 by JPL's path, after the measure of Nov 19 above.\n"
  "- Juno's points are not a week apart, as this item says. Of its 32\n"
  '  served points inside the window (JD 2461280.53 to 2461456.47), 28\n'
  "  are the nightly tail's days and the other four stand 3 to 49 days\n"
  '  from their neighbours: the backbone is thinned at 0.02 AU, and\n'
  "  Juno's loop around Jupiter is thinned away.\n"
  "- A visitor can show any day in the window (the page's date input), so\n"
  '  hourly points near today alone would leave every other day as it is.\n'
  '- The measure, each served point in the window held out, with the\n'
  '  figure the box prints: Juno 6 of 32 missed by more than the figure,\n'
  '  worst 3.9 times it (JD 2461393.5, miss 4,780,840 km, figure\n'
  '  1,234,320 km), the largest miss 8,292,035 km against 3,775,987 km\n'
  '  (JD 2461442.5), and three inside the daily tail (JD 2461357.5 to\n'
  '  2461359.5, up to 2.3 times); BepiColombo 1 of 294, 6.8 times (JD\n'
  '  2461408.5).\n'
  'Tony, 23:24, to "Shall I go ahead with L-538\'s design?": "Yes". Tony,\n'
  '23:38, to "Do you approve daily points across the whole date window\n'
  'plus hourly around today, rather than hourly around today alone?":\n'
  '"What is your recommendation?" The session\'s answer: "Daily points\n'
  'across the whole date window, plus hourly points around today", and\n'
  'with it one rule: "when the night check finds an hour too coarse for\n'
  'a craft, the builder halves the step for that craft, down to a floor,\n'
  'and comes to you only if the floor still fails. That is method, so it\n'
  'would go in the skill and not to you each time." Tony, 23:39: "Yes".\n'
  'So the shape is a recommendation he accepted, and the finer-step rule\n'
  'is method, owed to gallery-cache-builder.\n'
  'The brief applies the finer-step rule to the daily part as well as to\n'
  'the hourly band, since a day was too coarse on three days of the\n'
  'tail. That is the session\'s reading, told to Tony after his "Yes", and\n'
  'not his words.\n'
  'The proof is the gallery run\'s "Curve error" row, widened to every\n'
  'craft inside a capture: red, by name, when a figure is smaller than\n'
  "its miss. The orrery's code is not touched; the arrival is already in\n"
  'the plan it sends.\n'
  "NOT CHECKED: that BepiColombo's loop around Mercury shortens to a few\n"
  'hours in the coming months. The session said it from memory; the\n'
  "brief's Part A measures it from JPL's own points.\n"
  '**Gap:** the build, by the brief, in one Claude Code session in the\n'
  'website repository. Its Part A (the map, the measure against JPL, its\n'
  'proposal) returns to a coordinating session before any edit. Then the\n'
  'skill text for gallery-cache-builder, which stands at its cap. Until\n'
  'the build, those boxes claim less error than they have.\n'
  "**Ref:** L-297 (the curve's error, Tony's ruling of Nov 19); gallery\n"
  '`tools/test_curve_error.py` (run with every kind to measure);\n'
  'provenance-discipline, A Computed Position Prints What Its Errors Earn;\n'
  'the brief, `documentation/COORD_L538_orbiters_brief_20261123.md`,\n'
  'placed by `patch_L538_1_design_and_brief.py`.\n'),
 ('LEDGER_CONSOLIDATED.md',
  '- CARRIED by this step, each for the place named (the brief\'s "Not in\n',
  '- **Step 3 confirmed, 2026-11-23, night** (the coordinating session,\n'
  '  Claude Fable 5.2, from GitHub: orrery 2634031c, Tony\'s commit "L522\n'
  '  documents", above 0a024d9f; gallery 9e7bb99f). The closing handoff\'s\n'
  '  four checks:\n'
  "  - The twelve installed skills equal the repository's copies at\n"
  '    HEAD, the text below the header byte for byte;\n'
  "    gallery-cache-builder's header differs by a line wrap, 2 bytes.\n"
  '    ledger-and-session-records reads 1.24, orrery-coding-conventions\n'
  '    1.14, agentic-pre-test 1.4. That comparison clears the three\n'
  '    reinstalls.\n'
  "  - The Project's resident protocol reads v4.0 on its third line. It\n"
  "    was not compared with the repository's file beyond that line.\n"
  "  - Part 3 is on GitHub with the four corrections in it: the door's\n"
  "    line struck, the two old Tony-actions marked overtaken, L-012's\n"
  '    line 4907, the closing handoff named here and on Where We Are.\n'
  '  - `HANDOFF_document_upkeep_20261123_close.md` is whole on GitHub,\n'
  '    158 lines, 8,172 bytes, and equal line for line to the copy Tony\n'
  '    attached.\n'
  '  Three things on the carried list above were still not put to Tony,\n'
  '  and now stand on Where We Are under Waiting on you: the stamping\n'
  "  rule, a cap for the website's `INTERACTIVE_AS_BUILT.md`, and a split\n"
  '  for gallery-cache-builder and horizons-orbital-mechanics.\n'
  '- CARRIED by this step, each for the place named (the brief\'s "Not in\n'),
 ('LEDGER_CONSOLIDATED.md',
  'session with a shell compares the installed skills with the\n'
  'repository before it works; that comparison clears the three.\n',
  'session with a shell compares the installed skills with the\n'
  'repository before it works; that comparison clears the three.\n'
  'DONE, 2026-11-23, night: the paste and the three reinstalls, by the\n'
  'comparison recorded under "Step 3 confirmed" above.\n')]

BRIEF_PATH = 'documentation/COORD_L538_orbiters_brief_20261123.md'

BRIEF_TEXT = (
    '<!-- Doc-Kind: hand | Brief for one Claude Code session in the website repository: a craft orbiting a planet is served points fine enough that its box never claims a smaller error than its real miss, on every date the date box offers (L-538). -->\n'
    "# Brief: the orbiters' printed error (L-538)\n"
    '\n'
    'Built on gallery 9e7bb99ffb77799759abe5a3e6d6dc556853da8e at\n'
    'https://github.com/tonylquintanilla/tonyquintanilla.github.io and\n'
    'orrery 2634031c19ff78e591ebbdc1d724ff4f0d494484 at\n'
    'https://github.com/tonylquintanilla/palomas_orrery (branch main).\n'
    'Written November 23, 2026 by the coordinating session (Claude Fable\n'
    '5.2) for ONE Claude Code session in the WEBSITE repository. The orrery\n'
    'is touched only for the closing records.\n'
    '\n'
    "Tony's local folders: orrery\n"
    'C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\\n'
    'gallery\n'
    'C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\\n'
    '\n'
    "Read before building, and say back which you read, with each skill's\n"
    "version line: the website's CLAUDE.md and the files it points to; the\n"
    'skills `gallery-cache-builder` (A Spacecraft Is Fetched by Its Plan; A\n'
    'Lagrange Point Is Served as a Point; A Served Number That Changes on\n'
    'Purpose; Every Question Is Asked of JPL, Fresh; the three-layer gate),\n'
    '`gallery-assembler` (the golden artifact process),\n'
    "`horizons-orbital-mechanics` (How a Path's Events Are Found, with the\n"
    'orbiter rule), `provenance-discipline` (A Computed Position Prints\n'
    'What Its Errors Earn), `orrery-coding-conventions` (the six consumers\n'
    'of position data), `agentic-pre-test`, `safe-file-editing` and\n'
    '`ledger-and-session-records` (the closing records). Then this brief,\n'
    "and L-538 (the orbiters' printed error) and L-297 (the Lagrange\n"
    'points) in LEDGER_CONSOLIDATED.md.\n'
    '\n'
    '## 1. The rulings\n'
    '\n'
    'Tony, November 19, 2026 (L-538): no stopgap. A coarser figure in those\n'
    'boxes until the fix was offered and not taken; "Yes" to the real fix,\n'
    'soon.\n'
    '\n'
    "Tony, November 23, 2026, 23:38, to the coordinating session's question\n"
    'whether the fix is daily points across the whole date window plus\n'
    'hourly points around today, or hourly points around today alone: "What\n'
    'is your recommendation?" The recommendation given: "Daily points\n'
    'across the whole date window, plus hourly points around today", with\n'
    'one rule as method, in the session\'s words: "when the night check\n'
    'finds an hour too coarse for a craft, the builder halves the step for\n'
    'that craft, down to a floor, and comes to you only if the floor still\n'
    'fails." Tony, 23:39: "Yes".\n'
    '\n'
    'One thing in section 3 goes past those words and is the coordinating\n'
    'session\'s reading, told to Tony after his "Yes": the same finer-step\n'
    'rule is applied to the daily part, not only to the hourly band,\n'
    'because the measurement in section 2 says a day will be too coarse on\n'
    'some days.\n'
    '\n'
    '## 2. What was found at gallery 9e7bb99f (read it; do not trust this list)\n'
    '\n'
    'Read from the served cache built 2026-11-24T00:01 UTC\n'
    '(`data/solar-system/`), `data/objects_config.json`,\n'
    '`tools/gallery_cache_builder.py`, `tools/test_curve_error.py` and\n'
    '`gallery/assembler/render_spacecraft.py`.\n'
    '\n'
    '- WHO IS IN A CAPTURE. Eight plans carry an arrival that stays, none a\n'
    '  departure: Juno (Jupiter, 2016-07-05), BepiColombo (Mercury,\n'
    '  2026-11-21 18:48, 3,073.0 km), Clipper (Jupiter, 2030-04-11),\n'
    '  ESCAPADE-Blue and ESCAPADE-Gold (Mars, 2027-09-09 and 2027-09-07),\n'
    '  and three ended missions, Galileo, Cassini and Akatsuki. So two are\n'
    "  in a capture inside today's date window: Juno and BepiColombo.\n"
    "  BepiColombo's arrival is two days old; L-538's figures of Nov 19 for\n"
    '  it were taken before it.\n'
    "- THE DATE WINDOW. `coverage_index.json`'s served_window, JD 2461280.53\n"
    '  to 2461456.47, about 176 days. `interactive.html` has a date input\n'
    '  (`id="date-input"`), so a visitor can show any day in it.\n'
    "- JUNO'S POINTS ARE NOT A WEEK APART. L-538 says so; the file says\n"
    '  otherwise. Of its 289 served points, 32 lie in the window: a daily\n'
    '  run of 28, JD 2461342.5 to 2461369.5 (the nightly tail, kept until\n'
    '  the plan is made again), and four single points. With the two just\n'
    '  outside the window the single points stand at 2461274.5, 2461323.5,\n'
    '  2461372.5, 2461393.5, 2461442.5 and 2461456.5: gaps of 49, 19, 3, 21,\n'
    '  49 and 14 days. The 7-day backbone is thinned at 0.02 AU\n'
    "  (`douglas_peucker`, `fetch_path_by_plan`), and Juno's loop around\n"
    '  Jupiter is small enough to be thinned away.\n'
    '- THE MISS, MEASURED. Each served point in the window held out and\n'
    '  worked out from the rest by `position_at` with the figure the box\n'
    "  prints (curve=False), as `tools/test_curve_error.py`'s `held_out`\n"
    '  does. Juno, 6 of 32 missed by more than the figure:\n'
    '    JD 2461393.5  miss 4,780,840 km  figure 1,234,320 km  (3.9)\n'
    '    JD 2461323.5  miss 4,409,146 km  figure 1,590,655 km  (2.8)\n'
    '    JD 2461357.5  miss   385,224 km  figure   170,258 km  (2.3)\n'
    '    JD 2461442.5  miss 8,292,035 km  figure 3,775,987 km  (2.2)\n'
    '    JD 2461358.5  miss   584,820 km  figure   467,098 km  (1.3)\n'
    '    JD 2461359.5  miss   602,788 km  figure   491,989 km  (1.2)\n'
    '  The three of JD 2461357.5 to 2461359.5 are inside the daily run, so\n'
    '  a point a day, held out, was too coarse on those days. BepiColombo, 1\n'
    '  of 294: JD 2461408.5, miss 5,780 km, figure 847 km (6.8). Holding a\n'
    '  point out doubles the spacing around it, so each is harder than a\n'
    '  real minute; it is the measure L-538 and L-297 use.\n'
    "- HOW A PATH'S POINTS ARE KEPT. `points.update(new)` in the spacecraft\n"
    '  branch (near line 1499): the saved points keep every tail day until\n'
    '  the plan is made again, when they are cleared and the whole path is\n'
    '  fetched (`fetch_path_by_plan`), the tail merged after the thinning.\n'
    '  An hourly band merged the same way would pile up, 24 points a day,\n'
    '  until the next plan.\n'
    '- THE WINDOW IS KNOWN LATE. A Lagrange point is fetched last, once the\n'
    '  window is known (`point_window`, `process_point`), and never takes\n'
    '  part in it. A path body is fetched before that and has no window.\n'
    "- THE PATTERN TO FOLLOW is the Lagrange points' (`POINT_*`,\n"
    '  `point_near_span`, `process_point`, the served `point` block with its\n'
    "  `near`, the validator's `point_problems`): a day apart across the\n"
    '  window and a day past each edge, an hour apart from yesterday 00:00\n'
    '  UTC to the end of the day after tomorrow.\n'
    '- WHERE THE ERROR IS MADE AND READ. `render_spacecraft.position_at`\n'
    '  makes it (the room runs this Python in the page); it reaches the box\n'
    '  as `interp_err_km`, read at three places in `interactive.html` and in\n'
    "  `gallery/solar_system_figures.js`. `CURVE_KINDS` keeps the curve's\n"
    "  figure off for spacecraft, by Tony's ruling of Nov 19.\n"
    "- THE CHECK. `tools/test_curve_error.py` is the gallery run's gating\n"
    '  row "Curve error". It holds only the Lagrange points and the comets\n'
    '  on open paths: 3,035 points across 21 files on this cache, worst miss\n'
    '  0.54 of the figure. `kinds()` already names spacecraft; `main` does\n'
    '  not hold them.\n'
    '\n'
    '## 3. What to build\n'
    '\n'
    "The outcomes, which are Tony's ruling:\n"
    '1. For a craft inside a capture, on every day the date box offers, the\n'
    "   box's error is never smaller than the real miss, as the held-out\n"
    '   measure finds it.\n'
    '2. Such a craft is served a point a day across the whole date window,\n'
    '   unthinned, and a point an hour apart from yesterday to the day after\n'
    '   tomorrow.\n'
    '3. Where a day or an hour is too coarse, the builder asks a finer step\n'
    '   there, down to a floor. Only a craft that still fails at the floor\n'
    '   comes to Tony, by name.\n'
    '4. No stopgap and no typed figure. The error stays worked out from\n'
    '   served points.\n'
    '5. Nothing else moves. Every other served file (a craft not in a\n'
    '   capture, a comet, a Lagrange point, every orbit) is compared before\n'
    '   and after, by name, with only what a night moves moved.\n'
    '\n'
    'How, which is yours to propose in Part A. These are the coordinating\n'
    "session's starting points, not rulings:\n"
    '- WHO IS IN A CAPTURE is read from the plan the entry already carries\n'
    '  (an arrival, and no departure before the day asked), never a typed\n'
    '  list of names. The build prints who it found, by name, and the body\n'
    '  each is captured by. A craft whose arrival falls inside the window\n'
    "  gets the fine points from its arrival on. An ended mission's span\n"
    '  ended before the window, so it gets none; say what the room shows for\n'
    '  one and confirm no box works out a figure between its old points.\n'
    '- THE FINER STEP is found by the measure itself: hold out each new\n'
    '  point, and where the miss is larger than the figure ask that stretch\n'
    "  again at a finer step, until none is. Propose the steps (the plan's\n"
    '  own events use 1h, 30m, 5m, 1m), the floor, and a limit on points and\n'
    '  on questions to JPL for one craft in one night. A craft that reaches\n'
    "  the limit is named and fails as the builder's other named failures\n"
    '  do; say which (served last-good, or held).\n'
    "- YESTERDAY'S HOURS. Say what the saved points keep once a day has left\n"
    '  the hourly band, and once it has left the window, so neither the\n'
    '  served file nor the raw archive grows by 24 points a day.\n'
    '- THE ORDER. The fine points need the window, which is known after the\n'
    '  path bodies are fetched today. Say where the fetch goes, and show a\n'
    '  capture craft cannot narrow the window.\n'
    "- THE SERVED BLOCK. A capture craft's served entry says what it was\n"
    '  served by (the step, the window, the hourly band, the finer\n'
    "  stretches), as a point's `point` block does, so the validator can\n"
    '  refuse a missing day or hour by name.\n'
    '- THE CHECK IS WIDENED, not copied: "Curve error" holds every capture\n'
    '  craft, with the figure its box prints, across the window. Its line\n'
    '  names the craft held and how many points. A capture craft with no\n'
    '  fine points is a failure, not a skip.\n'
    "- THE FIGURE. Keep the chord figure for spacecraft. Report the curve's\n"
    "  figure beside it on the new points. If only the curve's holds, do not\n"
    "  switch: that is Tony's ruling of Nov 19 to revisit, and it is the one\n"
    '  question of your Part A report.\n'
    '\n'
    "PART A, no edits. Map every place a path's points are fetched, merged,\n"
    'thinned, gated (the shrink gate, the sanity bound, Guard), validated,\n'
    'served and read, in the builder, the room and the checks, and name the\n'
    'six consumers of position data with what each reads of a path. Then\n'
    'measure, live against JPL, for Juno and BepiColombo: a point a day\n'
    'across the window and an hour apart in the band; each held out; the\n'
    'days and hours that fail, by date; the finer steps that cure them; the\n'
    "points, bytes, questions and seconds it costs. Measure BepiColombo's\n"
    "loop around Mercury from JPL's own points at the start, the middle and\n"
    'the end of its span (to 2027-04-10): the time between two nearest\n'
    'approaches. The coordinating session expects it to shorten to a few\n'
    'hours, from memory, not checked; the floor has to stand for that day.\n'
    'Then your proposal for each starting point above. Stop with that\n'
    'report. Tony carries it to the coordinating session.\n'
    '\n'
    'PART B, after the go-ahead. The builder, the validator, the offline\n'
    'suite and the widened check. Each new check is shown able to fail, by\n'
    'a planted fault caught by name: a capture craft missing a day in the\n'
    'window; missing an hour in the band; a figure smaller than its miss; a\n'
    'craft with an arrival and no departure that the build did not treat as\n'
    'captured; a craft past its departure treated as captured; a craft at\n'
    "the limit; yesterday's hours still served. `agentic-pre-test` before\n"
    'any file is called done. Stop with a report and wait for the go-ahead.\n'
    '\n'
    'PART C. A whole build on a throwaway copy, the served files compared\n'
    'before and after by name (outcome 5). `gallery_maintenance_run.py`\n'
    'whole, read green from its output, the rows that could not run named.\n'
    'What Tony looks at on his phone, written before he looks: the Solar\n'
    "System room, Juno's box and BepiColombo's box, today and on one other\n"
    'day in the window, with what each read before and what it should read\n'
    'now. His look is the gate. Then the closing records and the report.\n'
    '\n'
    'NOT IN THIS SESSION.\n'
    '- Any skill file. List on L-538 the rules you learned, in plain\n'
    '  sentences, and name in the report what `gallery-cache-builder` should\n'
    '  say. It stands at its cap, 944 of 944 lines, and its split has not\n'
    '  been put to Tony; the coordinating session writes the bump.\n'
    "- The box's words, and which figure it prints.\n"
    "- The orrery's code, and `path_plan.py`. If the plan lacks something\n"
    '  the build needs, stop and say what.\n'
    '- Every path to its last day (L-533 (ESCAPADE)), the next build, its\n'
    "  own. The clock items left open on L-541 (a plan's clock).\n"
    '- A wider date window. Days outside it, for an ended mission or any\n'
    '  other, are noted on L-538 if you find a box that can show one.\n'
    '\n'
    '## 4. Delivery\n'
    '\n'
    '- Work in the website repository, through the python_work door. Record\n'
    '  both bases (`git rev-parse HEAD`, `git ls-remote origin HEAD`, each\n'
    '  repository). A night commits under data/ every day, so a base may be\n'
    '  a descendant of the ones above; stop only if a file named in section\n'
    '  2 is not as described, and name what moved.\n'
    "- Edit the files in Tony's working copy, ASCII and LF, each change\n"
    '  stamped where it is made. Tony commits and pushes. Nothing is pushed\n'
    '  by the session.\n'
    '- The closing records go to the orrery: L-538 on\n'
    "  `LEDGER_CONSOLIDATED.md`, Where We Are edited by section, the run's\n"
    "  tools after them. Tony's run order names the two repositories apart.\n"
    "- After Tony's push, the website's next night is the proof on GitHub's\n"
    '  machine. Say in the report what its "Curve error" row should read,\n'
    '  with the craft named.\n'
    '\n'
    '## 5. The report\n'
    '\n'
    'Plain words, in this order: what was built, file by file; who is in a\n'
    'capture, by name; the measure before and after, with the worst day\n'
    'named for each craft; the cost (points, bytes, questions, seconds);\n'
    "the served files compared; the gallery run's rows by name; what Tony\n"
    'looks at on his phone; what Tony does next; the skill text owed;\n'
    'anything this brief got wrong. It opens with the anchor line: built on\n'
    '<base SHA> at each repository\'s URL; ready at <new SHA or "not\n'
    'pushed">. It ends with the session\'s token count as Claude Code\'s\n'
    '/cost prints it (Token Economy).\n'
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
    bpath = os.path.join(HERE, *BRIEF_PATH.split('/'))
    bbytes = ''.join(BRIEF_TEXT).encode('ascii')
    write_brief = True
    if os.path.exists(bpath):
        with open(bpath, 'rb') as f:
            have = f.read().replace(b'\r\n', b'\n')
        if have == bbytes:
            write_brief = False
        else:
            print("ERROR: %s already exists and differs from the one this "
                  "patch places. Likely a copy saved by hand: delete it and "
                  "run again. NOTHING was written." % BRIEF_PATH)
            sys.exit(1)
    for name, (text, was_crlf) in staged.items():
        with open(os.path.join(HERE, *name.split('/')), 'wb') as f:
            f.write(text)
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % name)
    print("patch applied (%d edits, %d files)" % (len(EDITS), len(staged)))
    if write_brief:
        with open(bpath, 'wb') as f:
            f.write(bbytes)
        print("wrote %s (%d bytes)" % (BRIEF_PATH, len(bbytes)))
    else:
        print("already there, identical: %s" % BRIEF_PATH)
    print("stamps updated: Where We Are's header (2634031c, 9e7bb99f); "
          "L-538's date (2026-11-23)")
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
    print("the orrery. Then start a Claude Code session with the brief,")
    print("documentation/COORD_L538_orbiters_brief_20261123.md. It stops")
    print("after its Part A report; bring that to the coordinating session.")


if __name__ == '__main__':
    main()
