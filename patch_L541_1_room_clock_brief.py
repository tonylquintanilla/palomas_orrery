"""
patch_L541_1_room_clock_brief.py -- places the brief, the starting prompt
and the survey for the Code session that sets the live rooms' clock, and
records the trace and Tony's ruling of Nov 21 on L-541 and on Where We
Are.

Built on ae9ec0f9 at https://github.com/tonylquintanilla/palomas_orrery
(branch main), with gallery 7d1e2e16 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.

Tony, 2026-11-21: 16:04, "i was thinking of L538 and L539 but your other
findings too. in whatever order you believe works best."; 16:18, "What
will we show visitors UTC converted from TDB, or TDB?"; 16:21, "Yes", to
convert.

RUN COMMAND
    Save this file in the orrery folder (palomas_orrery_for_github), open
    it in VS Code and click Run:

        python patch_L541_1_room_clock_brief.py

    Success: three "ok" lines for the edits, three "new" lines, "patch
    applied", then "ok" for ledger_index.py and the document-caps check.
    Failure: an "ERROR:" or "ANCHOR FAIL" line, and NOTHING is written.
    Undo after a success: Discard Changes in GitHub Desktop, and delete
    the three new documents.
    Once it has run, move it to the documentation folder.

What it changes:
    documentation/COORD_L541_room_clock_brief_20261121.md (new): the
        brief for one Claude Code session in the website.
    documentation/PROMPT_code_L541_room_clock_20261121.md (new): its
        starting prompt, to paste into Claude Code.
    documentation/SURVEY_L541_clock_69s_20261121.md (new): the
        measurement, 106 bodies, each one's 69 seconds of motion against
        the error its box prints with.
    LEDGER_CONSOLIDATED.md: on L-541, the wider question traced (yes),
        the sizes, that the 69 has no source, Tony's ruling, and the Gap
        rewritten; its title says the rooms' clock is ruled.
    documentation/WHERE_WE_ARE.md: in "Needs you now", the reinstall
        step, which is done, gives its place to starting the Code
        session. The page stays at its cap of 130 lines. The rest of the
        page is brought up to date by this session's close.

Written November 21, 2026 with Anthropic's Claude Fable 5.2.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

NEW_FILES = [('documentation/COORD_L541_room_clock_brief_20261121.md',
  '<!-- Doc-Kind: hand | Brief for one Claude Code session: the live rooms '
  "ask JPL's dates on JPL's clock, so a body is drawn where it is at the UTC "
  'minute shown (L-541). -->\n'
  "# Brief: the rooms' clock (L-541)\n"
  '\n'
  'Built on orrery ae9ec0f9 at '
  'https://github.com/tonylquintanilla/palomas_orrery\n'
  'and gallery 7d1e2e16 at\n'
  'https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch '
  'main\n'
  'for both). Written November 21, 2026 by the coordinating session (Claude\n'
  'Fable 5.2) for ONE Claude Code session in the WEBSITE repository.\n'
  '\n'
  "Read before building, and say back which you read: the website's\n"
  'CLAUDE.md and the files it points to; the skills `interactive-exhibit`\n'
  '(a room, its date line, the words and numbers it prints, testing a\n'
  'room), `gallery-assembler` (resolver.py, render_orbits.py, the served\n'
  'window), `gallery-cache-builder` (what the builder serves and the\n'
  "night's gate), `horizons-orbital-mechanics` (The Clock Is Read as UTC),\n"
  "`provenance-discipline` (a served number's source; a computed position\n"
  'prints what its errors earn), `safe-file-editing`, and\n'
  '`ledger-and-session-records` (the closing report). Then this brief;\n'
  "L-541 (a plan's clock) in the orrery's LEDGER_CONSOLIDATED.md, read\n"
  'whole; and documentation/SURVEY_L541_clock_69s_20261121.md.\n'
  '\n'
  '## 1. The ruling\n'
  '\n'
  "Tony, November 21, 2026, after the coordinating session traced L-541's\n"
  'wider question and reported that every body in a live room is drawn\n'
  'where it was 69 seconds before the minute its date line shows.\n'
  '\n'
  '16:18, his question: "What will we show visitors UTC converted from\n'
  'TDB, or TDB?" He was told: visitors see UTC; the date line is the\n'
  "visitor's own UTC minute and does not change; the room adds the\n"
  "difference before it looks up JPL's data; a body's source line keeps\n"
  "naming JPL's clock for the date of its orbit, as it does now, because\n"
  "it quotes the source; a path plan's moments, where a visitor reads\n"
  "them, print as UTC converted from JPL's clock, as the encounter already\n"
  'does. 16:21: "Yes".\n'
  '\n'
  'On the order of the cleanup, 16:04: "in whatever order you believe\n'
  'works best." The coordinating session put this first because it reaches\n'
  "every room, and before L-538 (the orbiters' printed error).\n"
  '\n'
  '## 2. What was found at gallery 7d1e2e16 (read it; do not trust this '
  'list)\n'
  '\n'
  "- THE DATES ARE JPL'S. `tools/gallery_cache_builder.py` stores, as each\n"
  "  point's `jd`, the `datetime_jd` JPL returns (its JDTDB column); an\n"
  "  orbit's `epoch_jd` is the Julian date Horizons was asked, which it\n"
  '  reads on its own clock; `as_of_today.t` reads 2461365.500694444 on\n'
  "  the Moon's record, which is 00:01:00 on JPL's clock.\n"
  '- THE MINUTE IS UTC. `gallery/scene_moment.js` (`askFor`) turns the\n'
  "  visitor's clock into an ISO minute; `interactive.html` hands it to\n"
  '  Pyodide as `EPOCH_ISO`, in three scene specs and once more as\n'
  '  `_jd = _iso_to_jd(EPOCH_ISO)`; `gallery/assembler/resolver.py`\n'
  '  (`_iso_to_jd`) makes `resolved_epoch_jd` from it as it stands.\n'
  '- NOTHING CONVERTS BETWEEN THEM. `render_orbits.propagate_marker`,\n'
  '  `render_spacecraft.position_at` and `compose_children` take that\n'
  "  Julian date against JPL's dates. So the room draws, at UTC minute M,\n"
  "  the place a body had at M on JPL's clock, which is 69.184 seconds\n"
  '  earlier.\n'
  '- THE DATE LINE SAYS UTC. `sceneMomentStamp(jd)` in `interactive.html`\n'
  '  prints the Julian date the driver returns (`epoch_jd`, `epochJd`)\n'
  '  with the word "UTC". `SolarSystemFigures.distanceLine` and `pastSpan`\n'
  "  subtract an orbit's `element_epoch_jd` (JPL's clock) from the same\n"
  "  number (UTC). `scene_moment.js` reads the served window's `end_jd`\n"
  '  to find the last minute it may ask for.\n'
  "- A PLAN'S DAY IS PRINTED AS WRITTEN. `gallery/solar_system_figures.js`\n"
  "  (`planDay` in `loiterLine`) prints a plan moment's day on JPL's\n"
  '  clock in a sentence whose other dates are UTC (L-541, PRINTED).\n'
  '- THE NUMBER HAS NO SOURCE. The 69 is whole seconds, typed in the\n'
  "  builder's `utc_to_tdb`, copied from the orrery's\n"
  "  `orbit_data_manager.py`; the orrery's `constants_new.py` has no row\n"
  '  for it. The figure is 69.184 s: TAI is 37 s ahead of UTC (IERS\n'
  '  Bulletin C 70 of 7 July 2025: "from 2017 January 1, 0h UTC, until\n'
  '  further notice : UTC-TAI = -37 s"), and Bulletin C 72 of 6 July 2026\n'
  '  says "NO leap second will be introduced at the end of December 2026"\n'
  "  (both read Nov 21, 2026 in the tz list's forwards of them; C 72's at\n"
  '  '
  'https://lists.iana.org/hyperkitty/list/tz@iana.org/thread/QXCI2R2IOCR6XHSWBBTYXXE4WT2LEY3R/\n'
  '  ; read the bulletin at IERS yourself before citing it). The 32.184 s\n'
  "  between TAI and JPL's clock is in the builder's own docstring and is\n"
  '  NOT sourced there; source it or let astropy carry it (below).\n'
  '- WHAT IT COSTS. The survey: at 22:00 UTC on Nov 21, for 56 of 106\n'
  '  served bodies the distance from the centre changes in 69.184 s by\n'
  '  more than the error its box prints with. Mercury prints to whole\n'
  '  kilometres and is about 640 km off.\n'
  '\n'
  '## 3. What to build\n'
  '\n'
  "The outcomes, which are Tony's ruling:\n"
  '1. A body is drawn where JPL puts it at the UTC minute the date line\n'
  '   shows, in every live room.\n'
  '2. No date a visitor reads changes its clock: the date line, the frozen\n'
  "   minute past the served window, and the shared link's minute stay\n"
  "   UTC. A body's source line keeps its words on JPL's clock.\n"
  '3. Where a room subtracts two dates (drift, the checked span), both are\n'
  '   on one clock.\n'
  "4. A plan's moment printed to a visitor is UTC, converted (the loiter\n"
  '   sentence; right today for ESCAPADE, and must stay right).\n'
  '5. The difference between the clocks is not typed in the page or the\n'
  '   assembler. It is served, with its source.\n'
  '6. A check that can fail holds outcome 1, every night.\n'
  '\n'
  'How, which is yours to propose in Part A; this is the coordinating\n'
  "session's starting point, not a ruling:\n"
  "- ONE SEAM. JPL's dates stay as served. The UTC minute becomes a date\n"
  "  on JPL's clock in one place, and what comes back to the page says\n"
  '  both: the UTC minute asked and the date used. Nothing downstream\n'
  '  converts again. Every place that prints a date from a Julian date\n'
  '  says which clock that number is on.\n'
  '- THE DIFFERENCE, SERVED. The builder has astropy, which carries the\n'
  "  leap seconds; it can work the difference out for the served window's\n"
  '  first and last minute, serve it with its source line, and fail\n'
  "  loudly if the two ends differ. Say if a row in the orrery's store is\n"
  "  the better home; that would be an orrery change, not this session's.\n"
  '- THE WITNESS. At each build the builder asks JPL where two bodies are\n'
  '  at one stated UTC minute inside the window, converting that minute\n'
  '  with astropy, and serves the answers. A checker in the night pass\n'
  '  works out the same two places the way the room does and compares,\n'
  '  each within the error its box prints. Choose bodies whose 69 seconds\n'
  '  of motion is far larger than that error (the survey ranks them): one\n'
  '  worked out from its orbit, one from served points. With the seam\n'
  "  taken out, the witness must go red by about the 69 seconds' motion,\n"
  '  and the checker shows that on a planted break every run.\n'
  '\n'
  'PART A, no edits. Map every place that makes, reads, subtracts or\n'
  'prints a moment or a Julian date in a live room: the page, the scripts\n'
  'under `gallery/`, the assembler under Pyodide, its tests and harness,\n'
  "`tools/headless`, and the gallery run's checks that use a moment\n"
  '(Scene moment, Scene address, Curve error, Solar System figures,\n'
  'Display figures, Arrival, Earth scene geometry, the walks). For each:\n'
  'the file and function, which clock the number is on, which clock the\n'
  'code assumes. Then your proposal for the seam, the served difference\n'
  "and the witness, and what the served window's last minute becomes (it\n"
  'moves by 69 seconds; a minute asked past the end must still be\n'
  'refused, and the last minute allowed must still be accepted). Stop\n'
  'with that report. Tony carries it to the coordinating session.\n'
  '\n'
  'PART B, after the go-ahead. The seam, the served difference, the date\n'
  'line and each printing site, the two subtractions, the loiter\n'
  'sentence. INTERACTIVE_AS_BUILT.md in the same commit, each file named\n'
  'with its folder.\n'
  '\n'
  'PART C. The witness and its checker; each existing check that moved,\n'
  'changed in the same way and for a stated reason; then the whole\n'
  "gallery run TWICE: on Tony's working copy, and in a throwaway folder\n"
  'holding only what a push would carry (the files `git ls-files --cached\n'
  '--others --exclude-standard` lists). Report the rows from the second.\n'
  'On Nov 20 and 21 two nights went red on a check that was green only on\n'
  "Tony's disk; documentation/patch_L529_4_as_built_names_night.py in the\n"
  'website tells it.\n'
  '\n'
  'NOT IN THIS SESSION.\n'
  "- The builder's keys (`Time(jd).datetime` read as UTC) and its reading\n"
  "  of a plan's windows as UTC, and the orrery's `path_drawing.py` and\n"
  '  `utc_to_tdb` (L-541, READ AS UTC): named in your report, not changed.\n'
  "- What `jd` means in a served file. An encounter's package and player.\n"
  '  Hourly points for an orbiter (L-538).\n'
  '- Any skill file. Name in the report what each of\n'
  '  `horizons-orbital-mechanics`, `gallery-assembler`,\n'
  '  `interactive-exhibit` and `gallery-cache-builder` should say.\n'
  '- The orrery repository.\n'
  '\n'
  '## 4. Delivery\n'
  '\n'
  '- Work in the website repository only, through the python_work door.\n'
  '  Record its base (`git rev-parse HEAD`, `git ls-remote origin HEAD`).\n'
  '  The night commits under data/ every day, so the base will be a\n'
  '  descendant of 7d1e2e16; stop only if a file named in section 2 is\n'
  '  not as described, and name what moved.\n'
  "- Edit the files in Tony's working copy, ASCII and LF, each change\n"
  '  stamped where it is made; Tony commits and pushes. Nothing is pushed\n'
  '  by the session.\n'
  "- After Tony's push he runs the night by hand (the website's Actions\n"
  '  tab, "Nightly run", "Run workflow") and reads it green before\n'
  '  anything else is built in the website. Say so in the report.\n'
  '- His phone look: the date line still reads UTC and nothing he can see\n'
  '  has moved. The evidence is the witness, so the report shows its two\n'
  '  rows, with the seam in and with it taken out.\n'
  '\n'
  '## 5. The report\n'
  '\n'
  'Plain words, in this order: what was built, file by file; the gallery\n'
  "run's rows by name with their results, from the throwaway folder; the\n"
  "witness's two rows both ways; what Tony does next (the push, the night\n"
  'by hand, the phone look); the skill text owed; what is left on L-541;\n'
  "anything this brief got wrong. It ends with the session's token count\n"
  "as Claude Code's /cost prints it (Token Economy), and opens with the\n"
  "anchor line: built on <base SHA> at the website's URL; ready at <new\n"
  'SHA or "not pushed">.\n'),
 ('documentation/PROMPT_code_L541_room_clock_20261121.md',
  '<!-- Doc-Kind: hand | The starting prompt for the Claude Code session '
  "that sets the rooms' clock (L-541), from its brief. -->\n"
  "# Starting prompt: the rooms' clock, the Code session\n"
  '\n'
  'Built on orrery ae9ec0f9 at '
  'https://github.com/tonylquintanilla/palomas_orrery\n'
  'and gallery 7d1e2e16 at\n'
  'https://github.com/tonylquintanilla/tonyquintanilla.github.io. Written\n'
  'Nov 21, 2026 by the coordinating session (Claude Fable 5.2).\n'
  '\n'
  'Open Claude Code in the python_work folder (the door), Opus, high\n'
  'effort, and paste everything below the line.\n'
  '\n'
  '---\n'
  '\n'
  'The work is in the website repository (tonyquintanilla.github.io).\n'
  'Follow its CLAUDE.md from its first step, and record its base.\n'
  '\n'
  'Your brief is documentation/COORD_L541_room_clock_brief_20261121.md in\n'
  'the orrery (palomas_orrery_for_github). Read it whole, then L-541 (a\n'
  "plan's clock) on the orrery's ledger and\n"
  'documentation/SURVEY_L541_clock_69s_20261121.md, and say back which\n'
  'rule files and skills you read.\n'
  '\n'
  'Work in three parts. Part A changes no file: the map and your\n'
  "proposal, as the brief's section 3 asks. Stop with that report; I\n"
  'carry it to the coordinating session and come back with a go-ahead.\n'
  'Part B: the build. Stop with a report and wait for my go-ahead.\n'
  'Part C: the witness, the checks, the gallery run both ways, and the\n'
  'closing report the brief asks for. Edit my working copy; I commit and\n'
  'push.\n'
  '\n'
  'Plain words in every report, one question at most.\n'),
 ('documentation/SURVEY_L541_clock_69s_20261121.md',
  '<!-- Doc-Kind: hand | A survey: how far each served body moves in 69.184 '
  'seconds, against the error its box prints with (L-541), measured once on '
  'Nov 21, 2026. -->\n'
  "# Survey: 69 seconds of motion against each box's printed error (L-541)\n"
  '\n'
  'Built on gallery 7d1e2e16 at\n'
  'https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch\n'
  'main), with orrery ae9ec0f9 at\n'
  'https://github.com/tonylquintanilla/palomas_orrery. Measured November\n'
  '21, 2026 by the coordinating session (Claude Fable 5.2). A record of\n'
  'one measurement; nothing reads this file.\n'
  '\n'
  '## What was asked\n'
  '\n'
  "L-541 (a plan's clock) carried a question marked not verified: whether\n"
  'the live rooms draw every body 69 seconds from the minute shown, and\n'
  'whether any box prints finer than that. The trace is on L-541. This is\n'
  'the second half: the sizes.\n'
  '\n'
  '## How it was measured\n'
  '\n'
  '- The moment: Julian date 2461366.4167, which is 22:00 UTC on\n'
  "  November 21, 2026, about 0.92 days after the served orbits' date.\n"
  '- A body worked out from its orbit (trust method two_body_rate_v1):\n'
  '  its place from `gallery/assembler/render_orbits.propagate_marker` at\n'
  '  that Julian date and at 69.184 seconds before it.\n'
  '- A body worked out from served points: its place from\n'
  '  `gallery/assembler/render_spacecraft.point_at`, the same two moments,\n'
  "  with the curve's error where the page uses it.\n"
  '- "moves km" is the distance between the two places. "dist chg km" is\n'
  '  the change in its distance from its centre, which is the figure a\n'
  '  box prints.\n'
  '- "error km" re-works the page\'s rule '
  '(`gallery/solar_system_figures.js`,\n'
  '  `distanceLine` and `pathDistanceLine`) in Python: the larger of the\n'
  "  drift, JPL's own figure (a small body's `range_3sigma_km`, or half a\n"
  "  unit of a planet's `position_accuracy` place) and one kilometre; for\n"
  "  served points, the larger of the working-out's error and one\n"
  '  kilometre. "prints to" is the place that error earns.\n'
  '- A row is marked where the distance changes by more than the error.\n'
  '\n'
  '## What it is not\n'
  '\n'
  "- Not the page's own code run in a browser: the rule was re-worked\n"
  '  here, so a row near the line could fall either side.\n'
  "- One moment. The drift grows through the day and a body's speed\n"
  '  toward its centre changes along its orbit, so the count is for that\n'
  '  hour.\n'
  "- A moon's row uses its distance from its planet.\n"
  '- Eight of 114 were not worked out: the Sun, and seven ended missions\n'
  '  whose served points stop before that day.\n'
  '\n'
  '## The result\n'
  '\n'
  '```\n'
  'examined 106 of 114; 8 not worked out\n'
  'distance changes in 69 s by MORE than the error its box prints with: 56\n'
  'body                   kind            moves km  dist chg km     error '
  'km  prints to  error from\n'
  'atlas_3i               comet             4088.5       4061.3          '
  '1.0          1  curve   <-- finer\n'
  'borisov_2i             comet             2271.4       2268.1          '
  '1.0          1  curve   <-- finer\n'
  'oumuamua               comet             1867.1       1866.9          '
  '1.0          1  curve   <-- finer\n'
  'panstarrs_2025_r3      comet             1551.6       1438.1          '
  '1.0          1  curve   <-- finer\n'
  'wierzchos              comet             1376.1       1286.7          '
  '1.0          1  curve   <-- finer\n'
  'borisov_2025_v1        comet             1293.0       1237.7          '
  '1.0          1  curve   <-- finer\n'
  'c2025_k1_d             comet             1225.0       1189.5          '
  '1.0          1  curve   <-- finer\n'
  'c2025_k1_b             comet             1223.3       1187.7          '
  '1.0          1  curve   <-- finer\n'
  'c2025_k1               comet             1215.9       1180.1          '
  '1.0          1  curve   <-- finer\n'
  'voyager_1              spacecraft        1170.4       1167.9          '
  '1.0          1  chord   <-- finer\n'
  'voyager_2              spacecraft        1056.0       1041.0          '
  '1.0          1  chord   <-- finer\n'
  'atlas_2024_g3          comet             1006.0       1000.4          '
  '1.0          1  curve   <-- finer\n'
  'tsuchinshan_atlas      comet              972.9        951.5          '
  '1.0          1  curve   <-- finer\n'
  'new_horizons           spacecraft         939.1        936.2          '
  '1.0          1  chord   <-- finer\n'
  'mercury                planet            3703.7        644.4          '
  '1.0          1  whole km   <-- finer\n'
  'mcnaught               comet              453.6        452.6          '
  '1.0          1  curve   <-- finer\n'
  'west                   comet              333.7        333.3          '
  '1.0          1  curve   <-- finer\n'
  'lutetia                asteroid          1541.1         94.8          '
  '2.9         10  JPL 2xr   <-- finer\n'
  'bennu                  asteroid          1610.0        138.4          '
  '4.9         10  drift   <-- finer\n'
  'semb_l2                lagrange_po       2106.9         24.1          '
  '1.0          1  curve   <-- finer\n'
  'semb_l4                lagrange_po       2085.8         23.8          '
  '1.0          1  curve   <-- finer\n'
  'semb_l5                lagrange_po       2085.8         23.8          '
  '1.0          1  curve   <-- finer\n'
  'semb_l1                lagrange_po       2065.0         23.6          '
  '1.0          1  curve   <-- finer\n'
  'itokawa                asteroid          1723.0        478.4         '
  '23.6        100  JPL 2xr   <-- finer\n'
  'steins                 asteroid          1486.1        156.7          '
  '8.6         10  drift   <-- finer\n'
  'eros                   asteroid          1380.1        108.7          '
  '6.5         10  JPL 2xr   <-- finer\n'
  'ikeya_seki             comet              243.9        243.9         '
  '14.9         10  drift   <-- finer\n'
  'tempel_2               comet             1815.9        695.1         '
  '53.4        100  JPL 2xr   <-- finer\n'
  'schaumasse             comet             1186.8        831.2         '
  '82.3        100  JPL 2xr   <-- finer\n'
  'ryugu                  asteroid          1558.4         36.2          '
  '4.3         10  JPL 2xr   <-- finer\n'
  'vesta                  asteroid          1265.0         87.3         '
  '12.9         10  drift   <-- finer\n'
  'mars                   planet            1571.7        112.4         '
  '17.2        100  drift   <-- finer\n'
  'orus                   asteroid           897.4         30.2          '
  '5.5         10  drift   <-- finer\n'
  'patroclus              asteroid           924.6        126.6         '
  '23.4        100  JPL 2xr   <-- finer\n'
  'em_l2                  lagrange_po         85.4          5.4          '
  '1.0          1  curve   <-- finer\n'
  'lucy                   spacecraft         599.0        320.6         '
  '62.3        100  chord   <-- finer\n'
  'donaldjohanson         asteroid          1108.2         37.8          '
  '7.4         10  JPL 2xr   <-- finer\n'
  'em_l5                  lagrange_po         73.1          4.6          '
  '1.0          1  curve   <-- finer\n'
  'em_l4                  lagrange_po         73.1          4.6          '
  '1.0          1  curve   <-- finer\n'
  'dinkinesh              asteroid          1401.4        157.6         '
  '36.0        100  JPL 2xr   <-- finer\n'
  'halley                 comet               69.7         31.0          '
  '7.2         10  drift   <-- finer\n'
  'em_l1                  lagrange_po         62.1          3.9          '
  '1.0          1  curve   <-- finer\n'
  'howell                 comet             1341.4        739.9        '
  '206.4       1000  JPL 2xr   <-- finer\n'
  'encke                  comet             1881.3       1563.3        '
  '461.6       1000  JPL 2xr   <-- finer\n'
  'psyche                 asteroid          1127.7        134.0         '
  '42.7        100  drift   <-- finer\n'
  'eurybates              asteroid           839.5         46.2         '
  '15.3         10  drift   <-- finer\n'
  'ceres                  dwarf_plane       1299.2         83.5         '
  '28.0        100  drift   <-- finer\n'
  'asteroid_2025_pn7      asteroid          1888.5        121.2         '
  '47.1        100  JPL 2xr   <-- finer\n'
  'venus                  planet            2432.3         13.4          '
  '5.3         10  drift   <-- finer\n'
  'churyumov              comet              865.8        537.8        '
  '246.1       1000  JPL 2xr   <-- finer\n'
  'kamo_oalewa            asteroid          2195.5        175.7         '
  '82.9        100  drift   <-- finer\n'
  'polymele               asteroid           826.7         28.2         '
  '15.3         10  drift   <-- finer\n'
  'asteroid_2024_pt5      asteroid          2040.5         30.8         '
  '17.3        100  JPL 2xr   <-- finer\n'
  'leucus                 asteroid           843.3         23.8         '
  '13.4         10  drift   <-- finer\n'
  'titan                  moon               378.7          8.5          '
  '6.5         10  drift   <-- finer\n'
  'psyche_spacecraft      spacecraft        1579.3        501.1        '
  '477.3       1000  chord   <-- finer\n'
  'jupiter                planet             883.1         37.3         '
  '50.0        100  JPL place\n'
  'saturn                 planet             675.6         36.2         '
  '50.0        100  JPL place\n'
  'lemmon                 comet             1258.0       1191.5       '
  '2127.9      10000  JPL 2xr\n'
  'europa_clipper         spacecraft        2567.7        600.6       '
  '2016.9      10000  chord\n'
  'asteroid_2025_py1      asteroid          2370.8        308.2       '
  '1088.3       1000  JPL 2xr\n'
  'parker_solar_probe     spacecraft        3224.4       2845.2      '
  '10854.3      10000  chord\n'
  'bepicolombo            spacecraft        3778.9        611.0       '
  '2390.0      10000  chord\n'
  'osiris_apex            spacecraft        2297.7        415.6       '
  '2030.2      10000  chord\n'
  'chariklo               asteroid           456.2         51.6        '
  '402.0       1000  JPL 2xr\n'
  'juice                  spacecraft        2688.9        273.5       '
  '2285.7      10000  chord\n'
  'apophis                asteroid          2603.9          0.7          '
  '5.7         10  drift\n'
  'solar_orbiter          spacecraft        1559.7        233.9       '
  '2152.1      10000  chord\n'
  'escapade_blue          spacecraft        2265.6        131.0       '
  '1704.6      10000  chord\n'
  'swan                   comet             1188.5       1134.0      '
  '14896.1      10000  JPL 2xr\n'
  'escapade_gold          spacecraft        2271.6        128.4       '
  '1710.1      10000  chord\n'
  'maps                   comet             1424.5       1423.5      '
  '22500.4     100000  JPL 2xr\n'
  'juno                   spacecraft         900.2         56.8       '
  '1507.0       1000  chord\n'
  'moon                   moon                73.0          4.7        '
  '143.0        100  drift\n'
  'earth                  planet            2085.2         24.4        '
  '850.5       1000  drift\n'
  'phobos                 moon               145.7          0.3         '
  '13.5         10  drift\n'
  'io                     moon              1194.3          3.5        '
  '179.0       1000  drift\n'
  'pluto_barycenter       dwarf_plane        361.0         83.3       '
  '5000.0      10000  JPL place\n'
  'neowise                comet              661.5        656.3      '
  '48839.4     100000  JPL 2xr\n'
  'hale_bopp              comet              376.9        372.9      '
  '33670.6     100000  JPL 2xr\n'
  'ixion                  asteroid           345.6         82.3       '
  '9361.3      10000  JPL 2xr\n'
  'c2025_k1_c             comet             1214.9       1179.1     '
  '142555.1     100000  JPL 2xr\n'
  'asteroid_2024_yr4      asteroid           586.6          1.1        '
  '236.0       1000  JPL 2xr\n'
  'goibniu                asteroid           332.8         21.3       '
  '4858.4      10000  JPL 2xr\n'
  'uranus                 planet             465.4         21.8       '
  '5000.0      10000  JPL place\n'
  'deimos                 moon                93.5          0.0          '
  '5.0         10  JPL place\n'
  'haumea                 dwarf_plane        268.7         31.9      '
  '12523.0      10000  JPL 2xr\n'
  'varuna                 asteroid           305.8         13.7       '
  '5847.6      10000  JPL 2xr\n'
  'mani                   asteroid           287.6         30.1      '
  '13020.3      10000  JPL 2xr\n'
  'quaoar                 asteroid           317.8         10.2       '
  '7430.3      10000  JPL 2xr\n'
  'orcus                  asteroid           263.1          8.4       '
  '8535.3      10000  JPL 2xr\n'
  'charon                 moon                13.8          0.0          '
  '1.0          1  whole km\n'
  'asteroid_2023_jf       asteroid          1241.0        377.7     '
  '606655.6    1000000  JPL 2xr\n'
  'neptune                planet             378.1          2.9       '
  '5000.0      10000  JPL place\n'
  'eris                   dwarf_plane        162.6         29.8      '
  '63834.0     100000  JPL 2xr\n'
  'makemake               dwarf_plane        260.6          5.9      '
  '13348.5      10000  JPL 2xr\n'
  'hyakutake              comet              392.2        391.3    '
  '1053256.9    1000000  JPL 2xr\n'
  'tno_2026_ed138         asteroid           284.6         29.0      '
  '81062.3     100000  JPL 2xr\n'
  'sedna                  asteroid           307.7         83.7     '
  '258024.0    1000000  JPL 2xr\n'
  'gonggong               asteroid           176.0         69.2     '
  '324491.3    1000000  JPL 2xr\n'
  'tno_2017_of201         asteroid           295.8        207.6    '
  '1038937.4    1000000  JPL 2xr\n'
  'leleakuhonua           asteroid           330.5        123.5    '
  '1019137.3    1000000  JPL 2xr\n'
  'asteroid_2024_dw       asteroid           852.2        508.0    '
  '4494695.5   10000000  JPL 2xr\n'
  'pluto                  dwarf_plane          1.7          0.0          '
  '1.0          1  whole km\n'
  'ammonite               asteroid           322.4         72.9    '
  '1565534.6    1000000  JPL 2xr\n'
  'arrokoth               asteroid           317.7          8.5    '
  '2952550.8   10000000  JPL 2xr\n'
  'NOT WORKED OUT:\n'
  '  not worked out here: 1 -- sun\n'
  '  outside its served span: 7 -- galileo, cassini, pioneer_10, pioneer_11, '
  'rosetta, akatsuki, dart\n'
  '```\n')]

EDITS = [('LEDGER_CONSOLIDATED.md',
  "#### [L-541] A plan's moment is on JPL's clock (TDB), and some places "
  'read or print it as UTC (orrery + gallery; recorded, not fixed)\n',
  "#### [L-541] A plan's moment is on JPL's clock (TDB), and some places "
  "read or print it as UTC (orrery + gallery; the rooms' clock ruled Nov 21, "
  'its brief written)\n'),
 ('LEDGER_CONSOLIDATED.md',
  '  changes: what the builder stamps, what the page asks for, and\n'
  "  whether any box prints finer than 69 seconds of its body's motion.\n"
  "**Gap:** a ruling on each: convert, or name JPL's clock where it is\n"
  'printed (L-504\'s rule prints an elements\' date "on JPL\'s ephemeris\n'
  'clock").\n'
  "**Ref:** L-529 (guided encounters); L-504 (the orrery's clock, UTC);\n"
  'L-533 (ESCAPADE); horizons-orbital-mechanics (The Clock Is Read as '
  'UTC).\n',
  '  changes: what the builder stamps, what the page asks for, and\n'
  "  whether any box prints finer than 69 seconds of its body's motion.\n"
  '- **TRACED, 2026-11-21: YES** (the coordinating session, Claude Fable\n'
  '  5.2, at gallery 7d1e2e16; by reading the code and the served index,\n'
  "  not by a render). The builder stores JPL's own Julian dates (each\n"
  "  point's `datetime_jd`, JPL's JDTDB; an orbit's `epoch_jd` as asked;\n"
  "  the Moon's `as_of_today.t` reads 2461365.500694444, 00:01:00 on\n"
  "  JPL's clock). The page hands the visitor's UTC minute to the\n"
  '  assembler (`EPOCH_ISO`; `resolver.py`, `_iso_to_jd`; once more in\n'
  '  `interactive.html`), and `propagate_marker` and `position_at` take\n'
  "  it against JPL's dates with no conversion. `sceneMomentStamp` prints\n"
  '  the same number with the word "UTC". So every body in a live room is\n'
  '  drawn where it was 69.184 seconds before the minute its date line\n'
  '  shows; the bodies are right relative to each other. The desktop\n'
  '  orrery was not traced.\n'
  '- THE SIZES (`documentation/SURVEY_L541_clock_69s_20261121.md`): at\n'
  '  22:00 UTC on Nov 21, for 56 of 106 served bodies the distance from\n'
  '  the centre changes in 69.184 s by more than the error its box prints\n'
  '  with: 20 comets, 18 asteroids, the 8 Lagrange points, 5 spacecraft\n'
  '  (Voyager 1 and 2, New Horizons, Lucy, Psyche), Mercury, Venus and\n'
  '  Mars, Ceres, and Titan. Mercury prints to whole kilometres and is\n'
  '  about 640 km off; Mars prints with a 17 km error and is 112 km off.\n'
  "  A re-working of the page's rule in Python at one moment, not the\n"
  "  page's own code; 8 of 114 not worked out (the Sun, and 7 ended\n"
  '  missions past their served points).\n'
  '- THE NUMBER HAS NO SOURCE. The 69 is whole seconds, typed in three\n'
  "  places: the builder's `utc_to_tdb`, the orrery's\n"
  '  `orbit_data_manager.py` (`utc_to_tdb`) and `path_drawing.py`\n'
  '  (`TDB_OFFSET`); `constants_new.py` has no row for it. The figure is\n'
  "  69.184 s: 37 s between TAI and UTC, and 32.184 s more to JPL's\n"
  '  clock. IERS Bulletin C 72 (6 July 2026): "NO leap second will be\n'
  '  introduced at the end of December 2026", so the 37 holds across the\n'
  "  served window; read 2026-11-21 in the tz list's forward of it, not\n"
  "  at IERS. The 32.184 s is in the builder's docstring and is not\n"
  '  sourced there.\n'
  '- **TONY\'S RULING, 2026-11-21.** 16:18: "What will we show visitors\n'
  '  UTC converted from TDB, or TDB?" He was told: visitors see UTC; the\n'
  "  date line is the visitor's own UTC minute and does not change; the\n"
  "  room adds the difference before it looks up JPL's data; a body's\n"
  "  source line keeps naming JPL's clock for the date of its orbit; a\n"
  "  plan's moments print as UTC converted from JPL's clock where a\n"
  '  visitor reads them. 16:21: "Yes". On the cleanup\'s order, 16:04: "in\n'
  '  whatever order you believe works best"; the coordinating session\'s\n'
  "  order is this item's rooms, then L-539 (every entry checked), then\n"
  "  L-538 (the orbiters' printed error), which refines an error smaller\n"
  "  than 69 seconds of an orbiter's motion.\n"
  "**Gap:** the rooms' clock, built by one Code session in the website\n"
  'from `documentation/COORD_L541_room_clock_brief_20261121.md`.\n'
  '**Tony-action (do):** start it with\n'
  '`documentation/PROMPT_code_L541_room_clock_20261121.md`. Outside that\n'
  "brief and still open here: the builder's keys and its reading of a\n"
  "plan's windows as UTC; the orrery's `path_drawing.py`; the whole-second\n"
  "69 in the orrery's `utc_to_tdb`; a sourced row for the difference, if\n"
  "the orrery's store is its home; and the skill text\n"
  '(horizons-orbital-mechanics, gallery-assembler, interactive-exhibit,\n'
  'gallery-cache-builder).\n'
  "**Ref:** L-529 (guided encounters); L-504 (the orrery's clock, UTC);\n"
  "L-533 (ESCAPADE); L-538 (the orbiters' printed error); L-539 (every\n"
  'entry checked); horizons-orbital-mechanics (The Clock Is Read as UTC);\n'
  '`documentation/COORD_L541_room_clock_brief_20261121.md`;\n'
  '`documentation/SURVEY_L541_clock_69s_20261121.md`.\n'),
 ('documentation/WHERE_WE_ARE.md',
  '> - *(do) Reinstall two skills, interactive-exhibit and gallery-pipeline '
  '(Plugins, in the claude.ai sidebar), and paste PROJECT_INSTRUCTIONS.md, '
  "now v3.144, into the Project's instructions (L-529 (guided encounters), "
  'L-540 (a reel on a Featured card)).*\n',
  "> - *(do) Start the Code session for the rooms' clock: open Claude Code "
  'in python_work, Opus, high effort, and paste '
  '`documentation/PROMPT_code_L541_room_clock_20261121.md` from below its '
  'line. The live rooms draw every body 69 seconds behind the UTC minute '
  'shown; your ruling of Nov 21: "Yes", convert (L-541 (a plan\'s clock)). '
  'The two skills are reinstalled and v3.144 is pasted, confirmed Nov '
  '21.*\n')]


def main():
    for rel, text in NEW_FILES:
        path = os.path.join(HERE, *rel.split('/'))
        if os.path.exists(path):
            with open(path, 'rb') as f:
                have = f.read().replace(b'\r\n', b'\n')
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
            staged[name] = [raw.replace(b'\r\n', b'\n'), b'\r\n' in raw]
        text = staged[name][0]
        o, n = old.encode('ascii'), new.encode('ascii')
        c = text.count(o)
        if c != 1:
            print("ANCHOR FAIL: %s, expected 1 match, found %d: %r\n"
                  "If this patch already ran, there is nothing to do. If "
                  "it has not, the file is not the one pushed at ae9ec0f9: "
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
    print("Next: commit and push the orrery; then start the Code session "
          "with documentation/PROMPT_code_L541_room_clock_20261121.md.")


if __name__ == '__main__':
    main()
