"""
patch_L510_4_L507_session_close_20261105.py -- records for the
coordinating session of Nov 5, afternoon (road stage 13's quick wins).
Records, the ended missions' brief, and two dashboard descriptions.

Built on orrery ca4dceea55243e20e75689263ef31b996c8b1a3c at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 3660993e736641f1d1412bf9ed58244d419307dc at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read live
on Nov 5, 2026, 15:12 Chicago. Written by the coordinating session
(Claude Opus 5.5), under ledger-and-session-records 1.22 and
safe-file-editing 1.14. Tony's run record for the session:
documentation/WHERE_WE_ARE_11-5-26_1458_run_record.md.

Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
and gallery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\

WHAT IT CHANGES (four files)

    documentation/COORD_L507_historical_missions_more_voyages_brief_20261105.md
      NEW: the brief for the Code session that draws Pioneer 10, Pioneer
      11, Rosetta, DART and Akatsuki on the website, with your ruling of
      Nov 5, 15:17 (a craft that flew on stops on its mission's last
      day, and its words say it still flies, untracked).

    LEDGER_CONSOLIDATED.md
      - L-510 (the typed fields stop deciding): a dated note -- the
        objects mirror follows the e rule by itself (website 3660993),
        what was verified, the drawer row it leaves for a person, the two
        skill sentences carried -- and a new Gap.
      - L-507 (historical missions): a dated note -- your two rulings of
        Nov 5 (Apollo 11's S-IVB to slice 2; option A) and the brief --
        a new Gap, and its date stamp to 2026-11-05.
      Then it runs ledger_index.py, which rebuilds the index rows.

    documentation/WHERE_WE_ARE.md, by section: the header, the box, the
    road (stage 12 folded into the done line, stage 13 moved on), a
    Settled line (your ruling), two Deferred lines, the Signals' cache
    build read from the swap log at gallery 3660993, and Where the
    details are; the old marks cleared. Nothing below the run-record
    marker.

    palomas_orrery_dashboard.py: the Objects Mirror Check's and Objects
    Mirror Suite's descriptions say the mirror now follows a body
    across e = 1 (you asked for the tool on the dashboard; both its
    buttons were already there), and its "Module updated" line. Then it
    runs test_dashboard_parity.py.

    Each edit is checked only at the text it replaces, so your notes
    elsewhere never stop it. A file that already holds the result is
    accepted and reported.

RUN COMMAND

    Save this file in the orrery's root folder
    (palomas_orrery_for_github), open it in VS Code and click Run.
    (python patch_L510_4_L507_session_close_20261105.py)

    Success: one "ok" line per edit, the index tool's last lines, the
    dashboard check's "DASHBOARD PARITY: PASS" line, then "patch
    applied". Failure: one ERROR or ANCHOR FAIL line, and nothing is
    written. Undo is Discard Changes in GitHub Desktop.

Written November 5, 2026 with Anthropic's Claude Opus 5.5.
"""

import os
import subprocess
import sys

LEDGER = "LEDGER_CONSOLIDATED.md"
PAGE = os.path.join("documentation", "WHERE_WE_ARE.md")
DASH = "palomas_orrery_dashboard.py"
BRIEF = os.path.join(
    "documentation",
    "COORD_L507_historical_missions_more_voyages_brief_20261105.md")
MARKER = b"--- Your run record below this line"

LEDGER_EDITS = [
    ('L-510: the Nov 5 afternoon note and new Gap',
     b"**Gap (replaces the one below, 2026-11-05):** the road's quick win: the\nobjects mirror follows the e rule by itself",
     b'- **2026-11-05, afternoon: THE MIRROR FOLLOWS THE RULE BY ITSELF** (the\n  coordinating session of Nov 5 from 13:07, Claude Opus 5.5; Tony\'s run\n  record `WHERE_WE_ARE_11-5-26_1458_run_record.md`). The website\'s\n  `patch_L510_3_mirror_follows_e_rule.py`, pushed 3660993 and read back\n  on GitHub:\n  - The objects mirror (`tools/mirror_objects.py`) follows a body\n    across e = 1 both ways. To an orbit: it removes `path` and\n    `open_path`, sets availability analytic, frame heliocentric,\n    trace none, and inserts the export\'s period. To a path: the\n    reverse, removing the period. It rewrites the entry\'s note with\n    the day (a person\'s own note kept after it) and prints every\n    change. It still refuses a side change over an entry whose three\n    fields were set by hand.\n  - The builder\'s offline test: a stand-in orbit for a body newly\n    drawn as one, named when used; the open-path count (13) replaced\n    by a comparison with the export, by name; an end-to-end build of\n    a config the mirror has flipped (West to an orbit, Hale-Bopp to a\n    path).\n  - Verified on Tony\'s machine: "MIRROR OBJECTS SUITE: pass", "PASS\n    (511 checks, 0 failures)". The session saw each new check fail on\n    its planted fault; the mirror as it stood before reproduced Nov\n    4\'s refusal word for word. The website\'s maintenance run in the\n    session\'s workspace read "36 of 36 gating checkers passed" (its\n    five pulls could not reach GitHub from there).\n  - Not done, recorded: the mirror does not move a flipped body\'s\n    drawer row. The drawer groups by JPL\'s class (interactive-\n    exhibit), which the export does not carry, so the change line\n    names the row\'s group for a person to check.\n  - Tony asked for the tool on the dashboard: both its buttons were\n    already there (Objects Mirror Check, Objects Mirror Suite); this\n    session\'s records patch rewrites their descriptions to say so.\n  - Two skill sentences carried to the next bumps of their skills,\n    named in the ended missions\' brief (L-507, section 6):\n    gallery-cache-builder\'s open-path bullet and onboarding section\n    gain the mirror\'s side change and the offline test\'s comparison;\n    horizons-orbital-mechanics\' "an open difference on L-484" for\n    piece C\'s website drawing is read against L-484 and corrected.\n**Gap (replaces the one below, 2026-11-05, afternoon):** Tony\'s Mode 5\nlook (Sun-centred: Tsuchinshan, Wierzchos, ATLAS each drawn as\n3I/ATLAS is; 3I/ATLAS unchanged; Halley still its ellipse); then part\n2\'s brief and build (Deferred on Where We Are, Nov 5). The drawer row\nof a body that changes side waits until JPL\'s class reaches the\nexport.\n**Gap (superseded above, 2026-11-05, afternoon; replaced the one below, 2026-11-05):** the road\'s quick win: the\nobjects mirror follows the e rule by itself'),
    ('L-507: the Nov 5 note and new Gap',
     b'**Gap (replaces the one below, 2026-11-03, morning):** slice 2 waits\nbeside L-402 and L-489',
     b'- **2026-11-05: the next voyages, ruled and briefed** (the coordinating\n  session of Nov 5, Claude Opus 5.5; Tony\'s run record\n  `WHERE_WE_ARE_11-5-26_1458_run_record.md`), road stage 13\'s second\n  quick win.\n  - Tony, Nov 5, 13:27: a Claude Code session from a brief; and\n    "Apollo in slice 2": Apollo 11\'s S-IVB goes with the encounters.\n    JPL\'s span for it, as `celestial_objects.py` line 912 records it,\n    is 1969-07-16 to 1969-07-28, near Earth and the Moon.\n  - Tony, Nov 5, 15:17, on a craft that flew on after its mission\n    ended (the Pioneers; Akatsuki), choosing option A: "A. but\n    indicate the craft is still flying but not tracked." The path\n    stops on the day the mission ended, the marker where it was that\n    day, and the words say it still flies and no one tracks it.\n    Option B, declined: on to JPL\'s last day, dashed after the end.\n  - The brief, for Pioneer 10, Pioneer 11, Rosetta, DART and\n    Akatsuki:\n    `documentation/COORD_L507_historical_missions_more_voyages_brief_20261105.md`.\n    It carries L-476\'s note above (Pioneer 10 in the desktop orrery)\n    as a stop point, and the two skill sentences from L-510.\n**Gap (replaces the one below, 2026-11-05):** the more-voyages Claude\nCode session from its brief, both repositories; then Tony\'s phone look\nand the desktop orrery\'s Pioneer 10. Slice 2 (the encounters: Artemis\nII and Apollo 11\'s S-IVB) waits beside L-402 and L-489 (compositions).\nThe drawer walk\'s three older failures, to an item of their own or\nL-423 (the website\'s checks).\n**Gap (superseded above, 2026-11-05; replaced the one below, 2026-11-03, morning):** slice 2 waits\nbeside L-402 and L-489'),
    ('L-507: date stamp',
     b'<!-- L:507 status:OPEN upd:2026-11-03 section:A flag: rice: -->',
     b'<!-- L:507 status:OPEN upd:2026-11-05 section:A flag: rice: -->'),
]

PAGE_EDITS = [
    ("the page's header",
     b"Last updated: November 5, 2026, noon: the coordinating session (Opus) closed; the website's night green again.\n- Written at orrery 620b9149 and gallery e605f56, read live.\n",
     b"Last updated: November 5, 2026, afternoon: the coordinating session (Opus) for stage 13's quick wins.\n- Written at orrery ca4dceea and gallery 3660993, read live.\n"),
    ("the page's box",
     b"> **Changed since you last read this:**\n> - The website's nights stopped on Nov 4 and 5 over piece C of comet\n>   C/2025 K1, which the orrery now draws as an orbit. Two website\n>   patches fix it; the first is pushed (e5352a86).\n> - By your ruling, the website follows the orrery's rule: path or\n>   orbit by the e in JPL's database.\n> - The road turns to the symbols, with the moons sooner.\n> - The website's night went green on Nov 5 (e605f56), piece C an orbit.\n>\n> **Do next:** *the quick wins, starting with the copying tool\n> following the e rule by itself (stage 13).*\n",
     b"> **Changed since you last read this:**\n> - The copying tool now follows the e rule by itself, both ways\n>   (website 3660993). A comet that crosses e = 1 no longer stops a\n>   night. It leaves the body's drawer row for a person, and says so.\n> - The ended missions, your ruling: a craft that flew on stops on the\n>   day its mission ended, and the words say it still flies, untracked.\n>\n> **Do next:** *the Code session for the ended missions, from its brief\n> `COORD_L507_historical_missions_more_voyages_brief_20261105.md`.*\n"),
    ('the road: the done stages',
     b"  1-11.[done]  Through Nov 4: the three rooms, the objects, the Sun's and\n               Earth's slices, historical missions' slice 1, the paths by\n               the plan (L-476), path or orbit by e (L-510), A1 and A2\n               of JPL's fallbacks (L-512).\n 12.   [done]  A green website night, Nov 5 (e605f56). << moved this session\n",
     b"  1-12.[done]  Through Nov 5: the three rooms, the objects, the Sun's and\n               Earth's slices, historical missions' slice 1, the paths by\n               the plan (L-476), path or orbit by e (L-510), A1 and A2\n               of JPL's fallbacks (L-512), a green website night.\n"),
    ('the road: stage 13',
     b" 13.   [NOW]   *Quick wins:* the copying tool follows the e rule by itself\n               (L-510 (the typed fields stop deciding)); the ended\n               missions Pioneer 10 and 11, Rosetta, DART, Akatsuki and\n               Apollo 11's S-IVB (L-507 (historical missions)). << new this session\n",
     b' 13.   [NOW]   *Quick wins:* the copying tool follows the e rule, done\n               Nov 5 (L-510 (the typed fields stop deciding)); now the\n               ended missions Pioneer 10 and 11, Rosetta, DART and\n               Akatsuki (L-507 (historical missions)). << moved this session\n'),
    ("the road: stage 14's mark",
     b"and uncertainty; the Pluto row's drawing and name, your ruling. << new this session\n",
     b"and uncertainty; the Pluto row's drawing and name, your ruling.\n"),
    ("the road: stage 15's mark",
     b'Charon and Pluto come to standard in their rooms. << new this session\n',
     b'Charon and Pluto come to standard in their rooms.\n'),
    ("Settled: the ended missions' ruling",
     b'once a skill or the protocol carries it (trimmed Nov 3, night).\n',
     b"once a skill or the protocol carries it (trimmed Nov 3, night).\n- A craft that flew on: path stops on its mission's last day; words say still flying, untracked (Nov 5).\n"),
    ('Settled: the saved-path line, now carried by horizons 1.17',
     b'- No saved-path file (July copy kept outside); an outage is met by propagation and a record (Nov 4).\n',
     b''),
    ("Deferred: Apollo 11's S-IVB with slice 2",
     b'- L-489 (compositions), with L-486 and L-488 under it: Artemis II in\n  the Earth room first, with slice 2 (L-507 (historical missions)).\n',
     b"- L-489 (compositions), with L-486 and L-488 under it: Artemis II in\n  the Earth room first, with slice 2 (L-507 (historical missions));\n  Apollo 11's S-IVB with them (Nov 5).\n- A body crossing e = 1: its drawer row waits for JPL's class (L-510 (the typed fields), Nov 5).\n"),
    ('Signals: the cache build',
     b'- Last cache build: 20261105T181207Z, ok, no retry (swap log at gallery\n  e605f56).\n',
     b'- Last cache build: 20261105T200309Z, ok, no retry (swap log at gallery\n  3660993).\n'),
    ('Waiting on you: its mark',
     b'## Waiting on you  **>> UPDATED THIS SESSION**\n',
     b'## Waiting on you\n'),
    ('Where the details are: this session',
     b"- This session: your run record `WHERE_WE_ARE_11-4-26_2321_run_record.md`;\n  the website's `patch_L510_1_piece_c_orbit_website.py` and\n  `patch_L510_2_orbit_body_drops_future_points.py`.\n",
     b"- This session: your run record `WHERE_WE_ARE_11-5-26_1458_run_record.md`;\n  the website's `patch_L510_3_mirror_follows_e_rule.py`; the brief\n  `COORD_L507_historical_missions_more_voyages_brief_20261105.md`.\n"),
]

DASH_EDITS = [
    ("Objects Mirror Check's description",
     b'        "Objects mirror writes them. Also refuses a Solar System drawer row "\n        "with no key in the export. GATES the gallery runner.",\n',
     b'        "Objects mirror writes them. Also refuses a Solar System drawer row "\n        "with no key in the export. A body the orrery has moved across e = "\n        "1 (a path become an orbit, or back) shows here as the side change "\n        "the mirror makes by itself, its drawer row named for a person "\n        "(L-510). GATES the gallery runner.",\n'),
    ("Objects Mirror Suite's description",
     b'        "without an object, a null over held words -- then reads the real "\n        "config. GATES the gallery runner.",\n',
     b'        "without an object, a null over held words, a body moved across e "\n        "= 1 both ways with three planted faults (L-510) -- then reads the "\n        "real config. GATES the gallery runner.",\n'),
    ("the dashboard's stamp",
     b"(L-510: the Path Or Orbit Suite's button and line; the Period Fetch's\nline names its 30-day refresh of each small body's e).\n",
     b"(L-510: the Path Or Orbit Suite's button and line; the Period Fetch's\nline names its 30-day refresh of each small body's e).\nModule updated: November 5, 2026 with Anthropic's Claude Opus 5.5\n(L-510: the Objects Mirror Check's and Suite's descriptions say the\nwebsite's objects mirror follows a body across e = 1 by itself).\n"),
]

BRIEF_TEXT = b'<!-- Doc-Kind: hand | Brief for a Claude Code session (build): historical missions, more voyages (L-507) -- Pioneer 10, Pioneer 11, Rosetta, DART and Akatsuki drawn in the Solar System room as Galileo and Cassini are, each path stopping on the day its mission ended, and a craft that flies on said to be flying and untracked; across both repositories. -->\n# Brief: historical missions, more voyages (L-507)\n\nTony Quintanilla, PE | Claude Opus 5.5 (coordinating session) | November 5, 2026, afternoon, Chicago\n\nBuilt on orrery ca4dceea55243e20e75689263ef31b996c8b1a3c at\nhttps://github.com/tonylquintanilla/palomas_orrery and gallery\n3660993e736641f1d1412bf9ed58244d419307dc at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io, both read\nlive on Nov 5, 2026, 15:12 Chicago. The orrery commit that carries this\nbrief is the coordinating session\'s records patch on top of ca4dceea.\n\nTony\'s local folders: orrery\n`C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\`,\ngallery `C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\`.\n\nType: BRIEF for one Claude Code session, opened through the python_work\ndoor, working in both folders: the orrery first, then the website. Opus,\nhigh effort (path plans and served dates, by `METHOD_MODEL_EFFORT.md`).\nIts report ends with its token count as Claude Code prints it (the\nprotocol\'s Token Economy).\n\nThe machinery is slice 1\'s, built Nov 2 and 3 for Galileo and Cassini:\nread L-507\'s body and\n`documentation/COORD_L507_gallery_historical_missions_slice1_brief_20261102.md`\nfirst. This brief says only what differs.\n\n## 1. Why, in two sentences\n\nRoad stage 13 on Where We Are, the quick wins, second part: the ended\nmissions the orrery already lists, drawn on the website (Tony\'s order of\nNov 5; the instrument, a Code session from this brief, his go-ahead of\nNov 5, 13:27). Apollo 11\'s S-IVB is not in this build: it goes with\nslice 2, the encounters (Tony, Nov 5, 13:27: "Apollo in slice 2").\n\n## 2. The rulings\n\nSlice 1\'s stand (L-507): a served positions file by the mission\'s path\nplan, drawn whole and solid by `render_spacecraft.py`; the marker at the\npath\'s last served point; the box opens "This mission ended on <date>.\nThe marker is where it was that day."; the Historical missions group;\nthe dates sentence on every spacecraft\'s box. Galileo\'s ruling, "Yes\nstop at impact" (Nov 2), stops a path on its `mission_end` where JPL\nruns past it.\n\nNew, for a craft that flew on after its mission ended (Tony, Nov 5,\n15:17 Chicago, choosing option A of the coordinating session\'s question):\n"A. but indicate the craft is still flying but not tracked."\n- So the path stops on the day the mission ended, as Galileo\'s does,\n  and the marker sits where the craft was that day.\n- And the words say the craft is still flying and no one tracks it. The\n  wording is drafted and waits for his "Approved" (section 5).\n- Option B, declined: the path running on to JPL\'s last day, dashed\n  after the mission\'s end.\n\n## 3. What is already found, at the two SHAs above\n\nEvery line was read from the code. Re-read before building.\n\nThe orrery, `celestial_objects.py` (all `\'object_type\': \'trajectory\'`,\n`\'is_mission\': True`, symbol diamond-open; none has a \'key\', a\n\'horizons_name\' or a \'mission_end\', so none is exported or planned):\n\n| Entry | Line | id | start / typed end | JPL\'s ends, as the entry\'s comments record them | mission_url |\n|---|---|---|---|---|---|\n| Pioneer 10 | 918 | -23 | 1972-03-04 / 2002-03-03 | none before 1972-MAR-03 02:04; none after 2050-JAN-01 00:08 | NASA Ames archive page |\n| Pioneer 11 | 925 | -24 | 1973-04-07 / 1995-09-29 | none before 1973-APR-06 02:25; "Science operations and daily telemetry ceased on September 30, 1995" (no JPL end recorded) | the same NASA page |\n| Rosetta | 976 | -226 | 2004-03-03 / 2016-10-04 | none before 2004-MAR-02 09:25; none after 2016-OCT-04 23:59 | rosetta.esa.int |\n| Akatsuki | 990 | -5 | 2010-05-22 / 2025-08-22 | none before 2010-MAY-21 00:51; none after 2025-AUG-23 23:58 | Wikipedia (not the agency\'s page) |\n| DART | 1053 | -135 | 2021-11-25 / 2022-09-26 | none before 2021-NOV-24 07:16; "Impact: 26-Sep-2022 23:14:24.183 UTC (actual)" | nasa.gov/dart |\n\n- The comments are older readings, not today\'s JPL. Read JPL again.\n- `path_plan.py` takes a plan\'s span from JPL\'s first and last day, or\n  to `mission_end` where it is set (line 481), and adds `mission_end` to\n  a plan\'s inputs only where it is set (line 739).\n- L-507\'s note received from L-476 (Nov 3, evening): in the DESKTOP\n  orrery, Pioneer 10 has no plan, its line stops at its typed end\n  (79.8 AU) while its marker is at today\'s position (142.2 AU). See\n  step 1\'s stop point.\n\nThe website:\n- `interactive.html` line ~2804 writes the ended opening from the\n  path\'s last served day; ~2839 notes `mission_end`. The ended branch of\n  `render_spacecraft.py` and `fetch_path_last_day` in the builder are\n  slice 1\'s and serve these five unchanged.\n- The objects mirror copies `REPLACED = ("name", "horizons_id",\n  "id_type")` and `INSERTED = ("description", "info_url", "period",\n  "path", "open_path", "horizons_name")` (`tools/mirror_objects.py`).\n  Nothing that says a craft flies on reaches the room today.\n- The mirror follows a body across e = 1 by itself since 3660993 (L-510);\n  that does not touch spacecraft.\n\n## 4. The work, in order\n\n1. ORRERY, the five entries. A \'key\' each (`pioneer_10`, `pioneer_11`,\n   `rosetta`, `dart`, `akatsuki`, the website\'s slugs) and JPL\'s exact\n   \'horizons_name\', read from JPL (horizons-orbital-mechanics, Which\n   Record Serves a Body). Then each one\'s `mission_end` by that skill\'s\n   method (An Ended Mission Ends on Its mission_end): JPL\'s last day and\n   the mission\'s end as the AGENCY\'S OWN PAGE states it (NASA for the\n   Pioneers and DART, ESA for Rosetta, JAXA for Akatsuki), side by side,\n   the page quoted on the entry.\n   - Within a day: the page\'s date, as for Galileo and Cassini.\n   - JPL runs past the page\'s end (an impact, or a craft that flew on):\n     the page\'s date. Galileo\'s ruling and Tony\'s of Nov 5 cover both.\n   - STOP and bring Tony one question, the two dates and their sources,\n     when: the page\'s end is AFTER JPL\'s last day (no point to put the\n     marker on); no agency page states an end (Akatsuki\'s link today is\n     Wikipedia); or a page gives two dates (last contact and a declared\n     end) and does not say which is the mission\'s end.\n2. ORRERY, "still flying". For each craft that flew on, a field on its\n   entry saying so, cited to a page that says the craft still flies (or\n   still orbits). No page saying so: no field and no sentence, and the\n   gap named (remove and note it). The field\'s name and its road to the\n   room are the session\'s, as `mission_end`\'s and `open_path`\'s were:\n   the export, the mirror\'s INSERTED list (with a case in\n   `tools/test_mirror_objects.py`), the config, the room.\n3. ORRERY, the plans: `path_plan.py` for the five, each plan\'s span and\n   events printed and read. Akatsuki is a Venus orbiter (the orbiter\n   rule, an arrival). Then the orrery\'s maintenance run, which exports\n   them; Tier-1 0 on the gate path.\n   - STOP POINT, L-476\'s note: plot Pioneer 10 Sun-centred in the\n     desktop orrery after the change and report what the line and the\n     marker show. If the marker still sits at today\'s predicted place\n     beyond the line\'s end, bring Tony that one question; the ruling\n     says the marker is where it was on its last day.\n4. THE WORDS (section 5), before any is written into the room.\n5. WEBSITE, in the same round as the export\'s new keys (a key in the\n   export with no website entry stops the mirror, and the night with\n   it; horizons-orbital-mechanics, KEYING): the five entries in\n   `data/objects_config.json` (the mirror fills the rest), their rows in\n   the Historical missions group, colours in `presentation.py`\n   (method, recorded in the words file), the box\'s still-flying\n   sentence, and companions by the plans (read them, do not type them).\n6. CACHE: a hand build, so Tony sees them before the night. The\n   Pioneers\' spans run decades; read each positions file\'s size and say\n   it (render size is watched).\n7. CHECKS: the figures check\'s part 7 and the drawer walk\'s section 20\n   gain the still-flying case; the mirror suite the new field; each\n   shown failing once on a planted fault. Both maintenance runs green,\n   read from their output.\n8. PUSH ORDER, in the run order: orrery and website the same evening,\n   orrery first, both before the next night (08:17 UTC).\n\n## 5. The words, Tony\'s before they are written\n\nDraft in `documentation/WORDS_L507_more_voyages_20261105.md` (slice 1\'s\n`WORDS_L507_historical_missions_20261102.md` is the shape) and wait for\nhis "Approved". Plain words, one sentence to a bullet:\n- the still-flying sentence, after the ended opening, for each craft\n  whose page says it flies on (gist: "It is still flying, but no one has\n  tracked it since."), with its source;\n- each of the five\'s description;\n- each `mission_end` with the sentence of the page it comes from;\n- the colours (method, recorded).\nEverything else in the box is slice 1\'s and unchanged.\n\n## 6. The rules it runs under\n\nRead each before the work it governs; open the first report with each\nversion line read, against the manifest: horizons-orbital-mechanics 1.17\n(Which Record Serves a Body; An Ended Mission Ends on Its mission_end;\nthe orbiter rule; KEYING); gallery-cache-builder 1.17 (A Spacecraft Is\nFetched by Its Plan, its last-day fetch); interactive-exhibit 1.30 (the\nspacecraft bullet, the drawer, companions); gallery-assembler 1.3;\norrery-coding-conventions 1.13 (Marker Symbol Convention);\nprovenance-discipline 2.36 (a served date prints what its source\nearns); safe-file-editing 1.14; agentic-pre-test 1.3;\nledger-and-session-records 1.22.\n\nCorrections that ride this session\'s bumps (one session, one bump; each\ncarried here from the coordinating session of Nov 5, L-510 and L-507):\n- horizons-orbital-mechanics: An Ended Mission Ends on Its mission_end\n  says "NASA\'s own mission page"; it becomes the agency\'s own page, and\n  gains Tony\'s ruling of Nov 5 for a craft that flew on. Under Which\n  Record Serves a Body, AN OPEN ORBIT IS NOT AN ELLIPSE calls piece C\'s\n  website drawing "an open difference on L-484": read L-484 and correct\n  the sentence to its state.\n- gallery-cache-builder: the mirror now follows a body across e = 1\n  (`tools/mirror_objects.py`, WHEN A BODY CHANGES SIDE, gallery\n  3660993), and the builder\'s offline test compares its comets on open\n  paths with the export by name and gives a stand-in orbit to a body\n  newly drawn as one; the bullet A COMET ON AN OPEN PATH IS A PATH BODY\n  and the onboarding section say so. Plus the new field in INSERTED.\n- interactive-exhibit: the spacecraft bullet gains the still-flying\n  sentence.\nEach bump follows ledger-and-session-records\' four steps in one commit,\nwith the protocol\'s version-history entry (v3.127).\n\n## 7. Done when\n\n- The five are served, drawn whole and solid, each marker on its\n  mission\'s last day, with the approved words; a craft that flew on says\n  so, where a page supports it.\n- Both maintenance runs pass, read from their output; Tier-1 0 on the\n  gate path; each new check case shown failing once.\n- Tony\'s run order ends with his phone look: the five ticked from\n  Historical missions, their boxes and companions; and the desktop\n  orrery\'s Pioneer 10, Sun-centred.\n\n## 8. Records, in the same session\n\n- L-507: what was built, verified against claimed; slice 2 (the\n  encounters, Apollo 11\'s S-IVB and Artemis II) untouched.\n- L-510: the two carried corrections, closed in the bumps.\n- Where We Are, by section: stage 13\'s line, the box, Signals read from\n  files; nothing below the run-record marker.\n- The report: files changed with their edit counts, the token count,\n  Tony\'s run order, the Tony-action rollup, one question at most.\n\nWritten November 5, 2026 with Anthropic\'s Claude Opus 5.5.\n'


def plan(path, edits, top_only=False):
    if not os.path.isfile(path):
        print("ERROR: %s not found. Run this from the orrery's root folder "
              "(palomas_orrery_for_github). Nothing was written." % path)
        return False, None
    raw = open(path, "rb").read()
    text = raw.replace(b"\r\n", b"\n")
    if top_only:
        if text.count(MARKER) != 1:
            print("ERROR: the run-record marker is not on %s once. Nothing "
                  "was written." % path)
            return False, None
        top, marker, bottom = text.partition(MARKER)
    else:
        top, marker, bottom = text, b"", b""
    if all((top.count(new) == 1) if new else (top.count(old) == 0)
           for _, old, new in edits):
        print("already there, identical: %s" % path)
        return True, None
    for label, old, new in edits:
        n = top.count(old)
        if n != 1:
            print("ANCHOR FAIL: %s in %s -- expected its text once, found "
                  "%d. Nothing was written." % (label, path, n))
            return False, None
        top = top.replace(old, new)
        print("ok %s" % label)
    out = top + marker + bottom
    if any(c > 127 for c in top):
        print("ERROR: %s would hold non-ASCII bytes. Nothing was written."
              % path)
        return False, None
    if top_only and top.count(b"\n") > 130:
        print("ERROR: %s would stand over 130 lines above its marker. "
              "Nothing was written." % path)
        return False, None
    if b"\r\n" in raw:
        print("note: %s was CRLF in the working copy; written LF" % path)
    return True, out


def plan_brief():
    if os.path.exists(BRIEF):
        have = open(BRIEF, "rb").read().replace(b"\r\n", b"\n")
        if have == BRIEF_TEXT:
            print("already there, identical: %s" % BRIEF)
            return True, None
        print("ERROR: %s already exists and differs from this patch's "
              "copy. Most likely a copy saved from a download: delete it "
              "and run again. Nothing was written." % BRIEF)
        return False, None
    return True, BRIEF_TEXT


def main():
    if os.path.basename(os.getcwd()).lower() == "documentation":
        print("ERROR: run this from the orrery's root folder, not from "
              "documentation\\. Nothing was written.")
        return 1
    ok0, brief = plan_brief()
    if not ok0:
        return 1
    ok1, led = plan(LEDGER, LEDGER_EDITS)
    if not ok1:
        return 1
    ok2, page = plan(PAGE, PAGE_EDITS, top_only=True)
    if not ok2:
        return 1
    ok3, dash = plan(DASH, DASH_EDITS)
    if not ok3:
        return 1
    wrote = False
    for path, out, n in ((BRIEF, brief, 1), (LEDGER, led, len(LEDGER_EDITS)),
                         (PAGE, page, len(PAGE_EDITS)),
                         (DASH, dash, len(DASH_EDITS))):
        if out is None:
            continue
        with open(path, "wb") as f:
            f.write(out)
        wrote = True
        print("ok %s (%s)" % (path, "new" if path == BRIEF else
                               "%d edits" % n))
    for script, lines in (("ledger_index.py", 6),
                          ("test_dashboard_parity.py", 1)):
        if script == "ledger_index.py" and led is None:
            continue
        print("Running %s ..." % script)
        r = subprocess.run([sys.executable, script], capture_output=True,
                           text=True)
        for line in (r.stdout + r.stderr).strip().splitlines()[-lines:]:
            print("  " + line)
        if r.returncode != 0:
            print("ERROR: %s exited %d. The edits above are written; "
                  "Discard Changes in GitHub Desktop undoes them. Paste "
                  "these lines to the session." % (script, r.returncode))
            return 1
        print("ok %s" % script)
    print("patch applied" if wrote else "Nothing to do.")
    print("")
    print("Do next:")
    print("  1. (do) Move this file into documentation\\.")
    print("  2. (do) In GitHub Desktop (orrery): the change list shows the "
          "ledger, WHERE_WE_ARE.md, palomas_orrery_dashboard.py, the new "
          "brief and this file. Commit and push -- not while the website's "
          "night is running (08:17 UTC, 2:17 Chicago, often hours late).")
    print("  3. (do) Open the Code session for the ended missions through "
          "the python_work door, pointing it at the brief "
          "documentation\\COORD_L507_historical_missions_more_voyages_brief"
          "_20261105.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
