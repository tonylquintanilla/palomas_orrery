"""
patch_L539_1_close_record.py -- the close of the coordinating session of
Nov 22, 2026: the ledger, Where We Are, the working notes for the skills
bump, and the starting prompt for the next coordinating session.

Built on 97a8b733 at https://github.com/tonylquintanilla/palomas_orrery
(branch main), with gallery e6af10ea at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.

Tony, 2026-11-22, 14:47: "i will be away from my computer. i have pulled
and pushed the repos. the nightly runs and builds are all green today.
please proceed. i will complete the mode 5 later."

RUN COMMAND
    This file is in the orrery folder (palomas_orrery_for_github). Open
    it in VS Code and click Run:

        python patch_L539_1_close_record.py

    Success: "ok" lines for the edits, two "new" lines, "patch applied",
    then "ok" for ledger_index.py and the document-caps check.
    Failure: an "ERROR:" or "ANCHOR FAIL" line, and NOTHING is written.
    Undo after a success: Discard Changes in GitHub Desktop, and delete
    the two new documents.
    Once it has run, move it to the documentation folder.

What it changes:
    LEDGER_CONSOLIDATED.md:
        L-539 (every entry checked): the coordinating session's review,
            Tony's push, his look in the window so far, and what is left
            of it.
        L-541 (a plan's clock): the skill text is still owed, and where
            its notes are.
        L-544 (L4 and L5 tie) and L-538 (the orbiters' printed error):
            the order, on Tony's word of Nov 22.
        L-550, new: a website check added by a website session leaves
            the orrery's dashboard check red.
    documentation/WHERE_WE_ARE.md, seven lines, each in place: the
        header, Do next, two lines of Needs you now, the road's cleanup
        line, and a stale line under Deferred.
    New: documentation/HANDOFF_coordinator_20261122_bump_notes.md and
        documentation/PROMPT_coordinator_start_20261122_3.md.

No code, no skill and no data file is touched. Each file is checked only
at the lines edited, so Tony's notes elsewhere in them are kept.

Written November 22, 2026 with Anthropic's Claude Fable 5.2.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

NEW_FILES = [('documentation/HANDOFF_coordinator_20261122_bump_notes.md',
  '<!-- Doc-Kind: hand | The working notes for the one skills bump, v3.145, '
  'handed from the coordinating session of Nov 22, 2026 to the next one: what '
  'each of five skills gains, what was checked, and what is still to choose. '
  '-->\n'
  '# Handoff: the skills bump (v3.145), working notes\n'
  '\n'
  'Built on orrery 97a8b733 at '
  'https://github.com/tonylquintanilla/palomas_orrery\n'
  '(branch main) and gallery e6af10ea at\n'
  'https://github.com/tonylquintanilla/tonyquintanilla.github.io. Written\n'
  'Nov 22, 2026 by the coordinating session of that day (Claude Fable 5.2).\n'
  '\n'
  "Tony's local folders: orrery\n"
  'C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\\n'
  'gallery\n'
  'C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\\n'
  '\n'
  'Type: DOCUMENTATION. A handoff is a claim: check each line below\n'
  'against the code at HEAD before it goes into a skill.\n'
  '\n'
  '## What this is\n'
  '\n'
  'One bump, five skills, one round of reinstalls for Tony, before the next\n'
  'website build. The rules were gathered and checked against the code on\n'
  'Nov 22; three skills have draft text below; two do not. Nothing in\n'
  'skills/ or PROJECT_INSTRUCTIONS.md has changed since 531c6826, so every\n'
  'line number below is good at 97a8b733.\n'
  '\n'
  "Checked Nov 22: all twelve installed skills read the manifest's\n"
  'versions, and the five below match the repo byte for byte\n'
  '(gallery-cache-builder differs only by a wrapped fires_when line). So\n'
  "v3.143's and v3.144's obligations are discharged: interactive-exhibit\n"
  '1.44, gallery-pipeline 1.3, gallery-cache-builder 1.20,\n'
  'provenance-discipline 2.37.\n'
  '\n'
  "The patch's model is documentation/patch_L529_3_skills_and_protocol.py:\n"
  'a list of (file, old, new), each old matching once; then\n'
  'skills_index.py, ledger_index.py, skills_index.py --check and\n'
  'doc_index.py --caps.\n'
  '\n'
  '## Each skill is at its cap\n'
  '\n'
  'Lines now, cap, and the oldest version entry that moves word for word\n'
  'to documentation/SKILL_HISTORIES.md:\n'
  '\n'
  '- safe-file-editing: 1.14 to 1.15; 765 of 765; the 1.12 block, lines\n'
  '  27-49 (23 lines). Room enough; nothing else moves.\n'
  '- gallery-assembler: 1.4 to 1.5; 307 of 307; the v1.2 note in its\n'
  '  header (4 lines). About 10 more lines of room to find. It has no\n'
  '  section yet in SKILL_HISTORIES.md.\n'
  '- interactive-exhibit: 1.44 to 1.45; 738 of 738; the 1.42 entry, lines\n'
  '  29-43 (15 lines). The three field notes, lines 714-726, can move, one\n'
  '  line staying under the heading. That gives about 17 lines.\n'
  '- gallery-cache-builder: 1.20 to 1.21; 942 of 944; the 1.18 entry,\n'
  '  lines 25-35 (11 lines). About 16 more lines to find; read lines\n'
  '  430-522, 728-773 and 791-799 for history that can move.\n'
  '- horizons-orbital-mechanics: 1.19 to 1.20; 904 of 904; the 1.17 entry,\n'
  "  lines 36-47 (12 lines). About 20 more lines plus L-539's; read lines\n"
  '  601-794 and 104-190.\n'
  '\n'
  'Few passages in these four are plain history any more; the earlier\n'
  'bumps moved the easy ones. Choosing what moves needs the passages\n'
  'read, not skimmed.\n'
  '\n'
  '## safe-file-editing 1.15 (draft)\n'
  '\n'
  'Under Unicode-Safe Editing, after the table:\n'
  '\n'
  '    A MARK OUTSIDE ASCII IS TYPED AS ITS ESCAPE, AND THE BYTES ARE READ\n'
  '    AFTER THE EDIT (v1.15, L-529). In a file kept ASCII, such a mark is\n'
  '    written as its `\\u` escape, as the file writes its others. Then read\n'
  "    the file's bytes for anything above 0x7F: on 2026-11-20 an edit tool\n"
  '    wrote raw characters where escapes had been typed (the website\n'
  "    page's Play and Pause marks, an ellipsis, a walk's arrow), and only\n"
  '    the bytes showed it.\n'
  '\n'
  'Under A Delivered Patch Is Final, after its Origin paragraph:\n'
  '\n'
  "    A PLACED FILE IS READ BACK (v1.15). A file placed in Tony's folder\n"
  '    from a linked session is read back, its size at least, before he is\n'
  '    told it is there. On 2026-11-22 a prompt file changed and placed\n'
  '    again arrived with its first content under a new date; the size,\n'
  '    1,666 bytes where 1,987 were sent, showed it, and a second placement\n'
  '    seconds later landed.\n'
  '\n'
  '## gallery-assembler 1.5 (draft)\n'
  '\n'
  "Keep it short; the website's INTERACTIVE_AS_BUILT.md, The rooms' clock,\n"
  'holds the detail. A new section after Trust / served_window system:\n'
  '\n'
  "    ## One seam between the visitor's clock and JPL's (v1.5, L-541)\n"
  '\n'
  "    A served `jd`, an orbit's date and a plan's moment are on JPL's\n"
  '    clock (TDB); the minute a room is asked for is UTC. `resolver.py`\n'
  '    is the one place they meet: it checks the UTC minute against the\n'
  '    served window, which the builder makes on UTC, then adds the served\n'
  '    difference (`coverage_index.json`, `clock.tdb_minus_utc_s`) once.\n'
  '    The context carries both dates, and the drivers hand the page\n'
  '    `moment_utc_jd` and `moment_tdb_jd`; `epoch_jd` and `epochJd` are\n'
  '    gone. Nothing downstream converts again. With no clock block the\n'
  "    room draws as before and warns. The gallery run's Room clock row\n"
  "    holds it against JPL's places.\n"
  '\n'
  '## interactive-exhibit 1.45 (draft; about 17 lines of room)\n'
  '\n'
  'A new section after An encounter is a package:\n'
  '\n'
  "    ### A visitor reads UTC; JPL's dates are on JPL's clock [QUALITY]\n"
  '    v1.45, L-541 (Tony, 2026-11-21: "Yes"). Every date a visitor reads\n'
  "    is UTC, and the date line is the visitor's own minute. A served\n"
  "    `jd`, an orbit's date and a plan's moment are on JPL's clock (TDB),\n"
  '    about 69 s ahead. The assembler converts once (gallery-assembler,\n'
  '    One seam) and hands the page `moment_utc_jd` to print and\n'
  '    `moment_tdb_jd` for lookups and drift; no page subtracts one from\n'
  '    the other. A day printed from a JPL date is taken back to UTC\n'
  "    first; from a served point's date it is read at the nearest minute\n"
  "    (`SolarSystemFigures.servedDay`), a plan's moment as it stands.\n"
  "    Only a body's source line names JPL's clock.\n"
  '\n'
  'A paragraph at the end of Phone first, and the conditions are stated:\n'
  '\n'
  '    A SESSION THAT CHANGES THE PAGE RUNS THE WALKS (v1.45, L-545; Tony,\n'
  '    2026-11-21: "should this be method?"). After a change to\n'
  '    `interactive.html` or a script it loads, before the closing report:\n'
  '    `tools/headless/walk_solar_system_drawer.js` and\n'
  '    `walk_scene_moment.js` (jsdom 24.1.3 from npm, in a scratch\n'
  '    folder), each count and any red check by name; and the gallery run\n'
  '    on a copy holding only what a push carries (L-543). On Nov 21 a\n'
  '    walk caught a day one day early that 53 green rows had passed.\n'
  '\n'
  'Two more for this skill, not drafted:\n'
  "- A new gallery-run row needs a button in the orrery's dashboard, and a\n"
  '  website session may not edit the orrery. The brief says who adds it\n'
  '  (L-550). Three times in three days: Encounters, Link cards, Room\n'
  '  clock.\n'
  "- The second half of the walks paragraph is the session's half of\n"
  "  L-543 (green on Tony's computer, red on GitHub). Whether Tony does it\n"
  '  before every push of his own is not ruled; do not write it as his.\n'
  '\n'
  '## gallery-cache-builder 1.21 (not drafted; facts checked)\n'
  '\n'
  'From L-541, in tools/gallery_cache_builder.py (`build_clock`) and\n'
  'data/solar-system/coverage_index.json ("clock" and "witness"):\n'
  '- THE CLOCK BLOCK. `build_clock` asks JPL its TDB-UT (a vectors query\n'
  "  for Mercury, id 199; astroquery's delta_T; the Horizons manual:\n"
  '  "After 1962, UT means UTC") at the window\'s first and last minute and\n'
  "  the build's own, works out astropy's TDB minus UTC at the same\n"
  '  minutes, and stops the build by name if the two differ by more than\n'
  "  0.001 s or JPL's moves by more than 0.004 s across the window (a leap\n"
  '  second inside it). Served on Nov 22: 69.182891 s, figure_from jpl.\n'
  "- THE WITNESS. Each build serves JPL's places of Mercury (from its\n"
  '  orbit) and 3I/ATLAS (from served points) at its own minute; the Room\n'
  '  clock row compares places. A witness does not share its clock with\n'
  '  what it tests: astropy and JPL each check the other.\n'
  "- OPEN ON L-541, one line: daily points are asked at 00:01:00 on JPL's\n"
  '  clock, 9 s before UTC midnight; keys and plan windows read as UTC.\n'
  'From L-529, one rule waits for this skill, in the ledger\'s words "the\n'
  'package\'s place and the night": an encounter\'s package lives under\n'
  'data/encounters/, written by hand with its own tool; the night never\n'
  'runs, swaps or commits it, and the sibling check knows the folder by\n'
  'name. interactive-exhibit 1.44 already carries the encounter: read\n'
  'what it says before repeating any of it.\n'
  '\n'
  '## horizons-orbital-mechanics 1.20 (not drafted; facts checked)\n'
  '\n'
  'Under The Clock Is Read as UTC (L-504), line 281:\n'
  "- JPL'S DATES ARE ON JPL'S CLOCK (L-541, L-529). datetime_jd is JDTDB;\n"
  "  an elements epoch is read on JPL's clock; a path plan's moments are\n"
  '  TDB. A page prints one as UTC only after converting it.\n'
  "- THE DIFFERENCE IS JPL'S OWN TDB-UT, 69.183 s in Nov 2026. 69.184 s is\n"
  "  TT's figure (32.184 + 37) and was a brief's mistake. The orrery's\n"
  '  whole-second 69 (`utc_to_tdb`, `TDB_OFFSET`) is open on L-541.\n'
  '- AN OLD DATE HAS AN OLD DIFFERENCE: 42.185 s on 4 March 1972, 56.182 s\n'
  '  on 20 October 1989 (astropy, 2026-11-21; L-541).\n'
  'From L-539 (every entry checked): its own list of rules and skill text\n'
  "is on the ledger item, under the build's record. Read it there. Three\n"
  'corrections it found in this skill:\n'
  '- Line 117 says Orcus (20090482) and Patroclus (20000617) are found in\n'
  "  BOTH of JPL's lists; on Nov 22 the session found 20000617 only among\n"
  "  the major bodies. Correct it from L-539's live answers for both.\n"
  '- Line 146 names FIVE skip lists in palomas_orrery.py;\n'
  '  idealized_orbits.py has another, ANALYTICAL_ONLY_SATELLITES, and its\n'
  '  own id for Xiangliu, 92250881 (L-549).\n'
  "- astroquery: the skill says 0.4.11; Tony's machine has 0.4.9;\n"
  "  requirements.txt asks >=0.4.6. In it 'majorbody', 'id' and a blank\n"
  '  all search the major bodies first and FALL THROUGH to the asteroids\n'
  '  when nothing matches, which is how the two L3 entries drew asteroids.\n'
  "  Tony's own output of Nov 22 carries astroquery's warning that\n"
  '  \'majorbody\' and \'id\' "are deprecated and replaced with ``None``,\n'
  '  which has the same functionality". That bears on L-548 too.\n'
  "New in the check, for the skill's Horizons-check section:\n"
  'horizons_unserved.py; data/horizons_unserved_confirmations.json; the\n'
  'answer "JPL has no object for this id", stored, waiting on Tony\'s look,\n'
  'then held; the mark ("looked"), set by a session\'s one command from\n'
  "Tony's words or by itself when the entry's name equals JPL's; due from\n"
  "day 20, ten a night, red at day 30; the night's title flags JPL DIFFERS\n"
  'and NEW JPL NAME.\n'
  '\n'
  '## The protocol\n'
  '\n'
  'A v3.145 entry; v3.142 moves down to PROJECT_INSTRUCTIONS_HISTORY.md,\n'
  'PART 1. The obligation travels: Tony reinstalls five skills and pastes\n'
  'the protocol; the session after confirms each loaded copy.\n'
  '\n'
  "Session record written November 2026 with Anthropic's Claude Fable 5.2.\n"),
 ('documentation/PROMPT_coordinator_start_20261122_3.md',
  '<!-- Doc-Kind: hand | A starting prompt for the next coordinating session, '
  'written at the close of the one before it. -->\n'
  '# Starting prompt: the next coordinating session\n'
  '\n'
  'Built on orrery 97a8b733 at\n'
  'https://github.com/tonylquintanilla/palomas_orrery (branch main) and\n'
  'gallery e6af10ea at\n'
  'https://github.com/tonylquintanilla/tonyquintanilla.github.io, with\n'
  'patch_L539_1_close_record.py on top. Written Nov 22, 2026 by the\n'
  'coordinating session of that day (Claude Fable 5.2).\n'
  '\n'
  "Tony's local folders: orrery\n"
  'C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\\n'
  'gallery\n'
  'C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\\n'
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
  '   v3.144 (no skill was bumped), the ledger carries L-547 to L-550, and\n'
  '   documentation/HANDOFF_coordinator_20261122_bump_notes.md exists. If\n'
  '   not, the close patch was not run or not pushed; say so before\n'
  '   anything else.\n'
  "2. Read documentation/WHERE_WE_ARE.md, then Tony's newest run-record\n"
  '   copy (documentation/WHERE_WE_ARE_*_run_record.md) for his notes. On\n'
  "   Nov 22 he had answered lines 1 to 7 of a look in the orrery's window\n"
  '   and left lines 8 to 14: one animation with a Lagrange point ticked,\n'
  "   and what Haumea's two moons draw.\n"
  '3. Read the night records in BOTH repositories. The orrery: its Horizons\n'
  '   check row reads NOTHING DUE until Nov 25, when 90 served identities\n'
  '   renew together, about 7 minutes of a 15-minute limit; a title that\n'
  '   starts JPL DIFFERS or NEW JPL NAME is the first thing to tell Tony.\n'
  "   NOAA's next El Nino update is expected 10 December 2026. The website:\n"
  '   59 rows, Room clock among them.\n'
  '\n'
  'Where things stand:\n'
  '\n'
  '- Every entry the orrery asks JPL for is checked against JPL (L-539),\n'
  '  built Nov 22 by one Code session in four parts, pushed at 142287c1.\n'
  "  56 entries the website does not serve are held to JPL's name and kind;\n"
  '  JPL has no object for four of them (L-549, for a talk with Tony).\n'
  '- The Lagrange points no longer ask JPL for elements or close\n'
  "  approaches (L-512's two leftover asks). Tony's eyes confirmed the\n"
  '  still picture on Nov 22.\n'
  '- The skills bump was NOT written. Its rules are gathered and checked,\n'
  '  three of five skills are drafted, in the handoff named above.\n'
  '\n'
  'Next, in this order:\n'
  '\n'
  '- The one skills bump, v3.145, FIRST, before any website build:\n'
  '  horizons-orbital-mechanics, gallery-assembler, interactive-exhibit,\n'
  '  gallery-cache-builder and safe-file-editing, from the handoff and from\n'
  "  L-539's own list of rules on the ledger. Each skill is at its cap, and\n"
  '  choosing what moves to SKILL_HISTORIES.md needs the passages read.\n'
  '  Tony then reinstalls five skills and pastes the protocol.\n'
  "- L-544 (L4 and L5 tie), in the website, AHEAD of L-538 (the orbiters'\n"
  '  printed error): Tony, Nov 22, "Confirmed as recommended including\n'
  '  your final thought". A walk that is red for a known reason at some\n'
  '  minutes teaches a session to wave a red through.\n'
  "- Then L-538, then the encounter's slice 2, its talk first (L-529).\n"
  "- Waiting on Tony, on Where We Are: L-543 (the gallery's checks from a\n"
  '  push copy before his own pushes), L-545 (whether the walks join the\n'
  '  gallery run), L-548 (a missing id_type), and at a talk L-549 (the\n'
  '  four moons).\n'
  '- Open on L-541, for an orrery session and a builder session: the\n'
  '  builder asks daily points 9 seconds before UTC midnight; its keys and\n'
  "  plan windows are read as UTC; the orrery's whole-second 69.\n"
  '\n'
  'Lessons from the last session worth carrying:\n'
  '\n'
  '- Running a Code session beside a writing job did not overlap. Each of\n'
  '  its reports needed a full turn of review, so the writing job waited.\n'
  '  Plan one at a time.\n'
  "- A check proves itself on real data. The new check's first run found\n"
  '  four ids JPL has no object for, two of them answered in February and\n'
  '  withdrawn since. The brief had not imagined that answer; the ruling\n'
  '  for it was made in the middle of Part C.\n'
  "- A coordinating session's own ruling can be wrong an hour later. It\n"
  '  ruled two moons onto a skip list "if they fail as MK2 does"; the\n'
  "  trace showed they are drawn from JPL's cached elements, and the\n"
  '  ruling was withdrawn before anything was edited. A Part that traces\n'
  '  and edits nothing paid for itself again.\n'
  '- Read a placed file back. A changed file placed a second time arrived\n'
  '  with its first content under a new date; its size showed it.\n'
  "- Laying a Code session's files from Tony's folder over a fresh copy of\n"
  '  the pushed commit, and running its suites there, checked each report\n'
  '  in a few minutes.\n'
  '- Searching past chats for a Code report cost much and found little.\n'
  "  The ledger's record of the build and the code were enough.\n"
  '- A look-in-the-window checklist must use the orrery\'s own words. "L1\n'
  '  as its marker alone" is the website\'s rule; the desktop draws a\n'
  '  point\'s path. Tony: "L1 has an orbit too. not a problem. what is the\n'
  '  issue?"\n'
  "- A website build that adds a check leaves the orrery's dashboard\n"
  '  check red, because a website session may not edit the orrery, and the\n'
  "  orrery's night skips that check (L-550). A brief that adds a website\n"
  '  check says who adds the button.\n'
  '\n'
  'Ask Tony one thing to begin: whether he has finished the look in the\n'
  "orrery's window, lines 8 to 14.\n")]

EDITS = [('LEDGER_CONSOLIDATED.md',
  "**Gap:** the coordinating session's skill bump (the text above); the",
  "**Note:** THE COORDINATING SESSION'S REVIEW AND THE CLOSE, Nov 22, 2026\n"
  '(Claude Fable 5.2). Each report of the Code session was read against\n'
  "Tony's disk: its files laid over a fresh copy of the pushed orrery,\n"
  'where the two suites read 40 and 121 after Part B and 46 and 127 at the\n'
  'close; the export in his folder was byte for byte the pushed one; the\n'
  'eight skipped names are the eight Lagrange-point entries in all three\n'
  "copies of the list. Three rulings were the coordinating session's, as\n"
  "method. A first answer waits on Tony's look, and an entry whose own name\n"
  'equals JPL\'s marks itself. "JPL has no object for this id" is an answer,\n'
  "stored and then held. And Hi'iaka and Namaka were first ruled onto the\n"
  'pre-fetch\'s skip list "if they fail exactly as MK2 does", then kept off\n'
  'it within the hour, when the trace showed their orbits are drawn from\n'
  "JPL's elements of Feb 2 (L-549 (four moons JPL cannot place)). Tony\n"
  'pushed the work at 142287c1 (merge 97a8b733) and wrote, 14:47: "i have\n'
  'pulled and pushed the repos. the nightly runs and builds are all green\n'
  'today. please proceed. i will complete the mode 5 later." Both nights of\n'
  'Nov 22 read clean on GitHub: orrery 60d0f157, and website e6af10ea with\n'
  '59 rows.\n'
  "- TONY'S LOOK IN THE WINDOW, Nov 22, partly done (his run record copy\n"
  '  documentation/WHERE_WE_ARE_11-22-26_1315_run_record.md). The two new\n'
  '  dashboard buttons ran and ended PASS. With the Moon and Earth-Moon L1\n'
  '  ticked around Earth, and with Earth and Earth-Sun L2 around the Sun,\n'
  '  the panel read "[PRE-FETCH] Checking osculating elements for 1\n'
  '  objects": two ticked, one asked, and no "Required masses not defined".\n'
  '  The checklist\'s line 4 was wrong: it said "L1 as its marker alone",\n'
  "  which is the website's rule; the orrery draws a point's path from\n"
  '  JPL\'s positions, as it did before. Tony: "L1 has an orbit too. not a\n'
  '  problem. what is the issue?"\n'
  "- **Tony-action (do):** the checklist's lines 8 to 14, in that run\n"
  '  record: one short animation with the Moon and Earth-Moon L1 ticked,\n'
  "  which no session ran; then Haumea with Hi'iaka and Namaka, a look for\n"
  "  L-549's talk.\n"
  '- THE SKILL TEXT was not written this session; it is the next\n'
  "  coordinating session's first job, from\n"
  '  documentation/HANDOFF_coordinator_20261122_bump_notes.md and the list\n'
  "  above (L-541 (a plan's clock) says why).\n"
  "**Gap:** the coordinating session's skill bump (the text above); the"),
 ('LEDGER_CONSOLIDATED.md',
  "- **Tony-action (do):** commit and push this session's work before\n"
  "  running the coordinating session's patch, so the two are not mixed\n"
  '  in one commit.',
  "- Done Nov 22: Tony committed and pushed this session's work at\n"
  "  142287c1, before the coordinating session's patch, so the two were not\n"
  '  mixed in one commit.'),
 ('LEDGER_CONSOLIDATED.md',
  "**Gap:** the rooms' clock is live. Still open here: the builder's keys",
  '**Note:** THE SKILL TEXT IS STILL OWED, Nov 22, 2026 (the coordinating\n'
  "session, Claude Fable 5.2). It was to be written while L-539's Code\n"
  'session ran (Tony, Nov 22, 10:13, to that order: "Confirmed as\n'
  'recommended including your final thought"). Every report of that session\n'
  'needed a turn of review, and the text was not finished. What each of the\n'
  "four skills should say, checked against the website's code at 5a7c96f8,\n"
  'is in documentation/HANDOFF_coordinator_20261122_bump_notes.md, with\n'
  "safe-file-editing as a fifth (L-529's escape rule) and the rules L-539\n"
  "(every entry checked) lists. It is the next coordinating session's first\n"
  'job: one bump, v3.145, before the next website build.\n'
  "**Gap:** the rooms' clock is live. Still open here: the builder's keys"),
 ('LEDGER_CONSOLIDATED.md',
  '<!-- L:541 status:OPEN upd:2026-11-21 section:A flag: rice: -->',
  '<!-- L:541 status:OPEN upd:2026-11-22 section:A flag: rice: -->'),
 ('LEDGER_CONSOLIDATED.md',
  "**Gap:** a tie-break in the drawer's order where two distances agree to",
  '**Note:** ORDER, Nov 22, 2026. The coordinating session proposed that\n'
  "this item go ahead of L-538 (the orbiters' printed error): L-538's\n"
  'session must run both walks (L-545 (checks that wait to be remembered)),\n'
  'and a walk that is red for a known reason at some minutes teaches a\n'
  'session to wave a red through. Tony, 10:13: "Confirmed as recommended\n'
  'including your final thought". It follows the skills bump (v3.145).\n'
  "**Gap:** a tie-break in the drawer's order where two distances agree to"),
 ('LEDGER_CONSOLIDATED.md',
  '<!-- L:544 status:OPEN upd:2026-11-21 section:A flag: rice: -->',
  '<!-- L:544 status:OPEN upd:2026-11-22 section:A flag: rice: -->'),
 ('LEDGER_CONSOLIDATED.md',
  '**Gap:** the build, soon (Tony, Nov 19): finer points near today for a',
  '**Note:** ORDER, Nov 22, 2026: after the skills bump (v3.145) and after\n'
  "L-544 (L4 and L5 tie), by Tony's word of that day, recorded on L-544.\n"
  '**Gap:** the build, soon (Tony, Nov 19): finer points near today for a'),
 ('LEDGER_CONSOLIDATED.md',
  '<!-- L:538 status:OPEN upd:2026-11-19 section:A flag: rice: -->',
  '<!-- L:538 status:OPEN upd:2026-11-22 section:A flag: rice: -->'),
 ('LEDGER_CONSOLIDATED.md',
  '#### [L-540] A reel on a Featured card, beside a link into the room on its '
  'scene (gallery; the Links fold built Nov 21, a card that plays video an '
  'idea)',
  '#### [L-550] A website check added by a website session leaves the '
  "orrery's dashboard check red (method; for the skills bump)\n"
  '<!-- L:550 status:OPEN upd:2026-11-22 section:A flag: rice: -->\n'
  "- FOUND Nov 22, 2026 by L-539's Code session (Claude Opus 5.5): the\n"
  '  orrery\'s Dashboard parity check failed on "Link cards" and "Room\n'
  '  clock", two rows the website\'s builds of Nov 21 added to the gallery\n'
  '  run with no button in `palomas_orrery_dashboard.py`. The Encounters\n'
  '  row did the same on Nov 20 (Tony then: "Yes, add the button"). Three\n'
  '  times in three days.\n'
  '- WHY IT RECURS. A website session may not edit the orrery; its brief\n'
  "  says so. The orrery's night skips Dashboard parity, so nothing shows\n"
  '  the red until the next whole maintenance run by hand.\n'
  "- DONE Nov 22: the two buttons, in L-539's session, on the coordinating\n"
  '  session\'s go-ahead, which Tony pasted; "PASS -- 10 of 10 planted\n'
  '  faults caught; 116 steps matched to their buttons", and both ran to\n'
  "  PASS under Tony's hand.\n"
  '**Gap:** the rule, with the skills bump (v3.145): a brief for a website\n'
  'build that adds a gallery-run row says who adds the button, and the\n'
  "build's closing report names the button as owed. interactive-exhibit is\n"
  'its home.\n'
  '**Ref:** L-539 (every entry checked); L-529 (guided encounters: the\n'
  "Encounters button); L-541 (a plan's clock: the Room clock row); L-540 (a\n"
  'reel: the Link cards row); `palomas_orrery_dashboard.py`;\n'
  'documentation/HANDOFF_coordinator_20261122_bump_notes.md.\n'
  '\n'
  '#### [L-540] A reel on a Featured card, beside a link into the room on its '
  'scene (gallery; the Links fold built Nov 21, a card that plays video an '
  'idea)'),
 ('documentation/WHERE_WE_ARE.md',
  'Last updated: November 22, 2026: every entry the orrery asks JPL for is '
  'now checked against JPL (Claude Code, Claude Opus 5.5, for the '
  'coordinating session).',
  "Last updated: November 22, 2026: the coordinating session's close. Every "
  'entry the orrery asks JPL for is checked against JPL; the skills bump is '
  "the next session's first job (Claude Fable 5.2)."),
 ('documentation/WHERE_WE_ARE.md',
  "- Written on orrery f58581d5 with this session's work on your disk, not "
  'pushed; gallery 5a7c96f8, untouched.',
  '- Written on orrery 97a8b733 and gallery e6af10ea, both pushed; both '
  'nights of Nov 22 clean.'),
 ('documentation/WHERE_WE_ARE.md',
  '> **Do next:** *The coordinating session writes the skill text this check '
  "and the clock's build owe; then the orbiters' hourly points, L-538 (the "
  "orbiters' printed error); then the encounter's slice 2, its talk first "
  '(L-529 (guided encounters)).*',
  '> **Do next:** *The next coordinating session writes the one skills bump '
  '(v3.145) first, from '
  '`documentation/HANDOFF_coordinator_20261122_bump_notes.md`; then L-544 (L4 '
  "and L5 tie), ahead of L-538 (the orbiters' printed error) by your word of "
  "Nov 22; then the encounter's slice 2, its talk first (L-529 (guided "
  'encounters)).*'),
 ('documentation/WHERE_WE_ARE.md',
  '> - *(do) The reel: if its place is not pushed yet, commit it in the '
  'website, then Pull origin, then Push origin. Then on your phone look for '
  "Links in Earth's fold, between Encounters and Saved pictures, and tap the "
  'reel (L-540 (a reel on a Featured card)).*',
  "> - *(do) Finish the look in the orrery's window, lines 8 to 14 of the "
  'checklist in your run record `WHERE_WE_ARE_11-22-26_1315_run_record.md`: '
  'one short animation with the Moon and Earth-Moon L1 ticked, with no '
  '"Required masses not defined" in the panel; then Haumea with Hi\'iaka and '
  'Namaka, for our talk (L-539 (every entry checked), L-549 (four moons JPL '
  'cannot place)).*'),
 ('documentation/WHERE_WE_ARE.md',
  "> - *(do) Commit and push this session's orrery work first; only then run "
  "the coordinating session's patch, in a commit of its own (L-539 (every "
  'entry checked)).*',
  '> - *(do) Start the next coordinating session with '
  '`documentation/PROMPT_coordinator_start_20261122_3.md`, pasted from below '
  'its line. The website builds wait for its skills bump.*'),
 ('documentation/WHERE_WE_ARE.md',
  "  b.   [beside] This round's cleanup, each ruled Nov 19, in the order set "
  'Nov 21: every entry checked against JPL, L-539 (every entry checked), '
  "built Nov 22; then the orbiters' hourly points, L-538 (the orbiters' "
  'printed error); then every path to its last day, L-533 (ESCAPADE); the '
  "period's swing in its sentence, L-536 (a moon's yearly change); the 24 in "
  'goldenrod, L-432 (the default goldenrod), at your desk.  << moved this '
  'session',
  "  b.   [beside] This round's cleanup, each ruled Nov 19, in the order set "
  'Nov 21: every entry checked against JPL, L-539 (every entry checked), '
  'built Nov 22; then the L4 and L5 tie, L-544 (L4 and L5 tie), put ahead on '
  "Nov 22; then the orbiters' hourly points, L-538 (the orbiters' printed "
  "error); then every path to its last day, L-533 (ESCAPADE); the period's "
  "swing in its sentence, L-536 (a moon's yearly change); the 24 in "
  'goldenrod, L-432 (the default goldenrod), at your desk.  << moved this '
  'session'),
 ('documentation/WHERE_WE_ARE.md',
  '- L-490 (the legacy list); L-499 (kinds of session); L-471 (a delivered '
  "patch is final), for safe-file-editing's next version.",
  '- L-490 (the legacy list); L-499 (kinds of session).')]


def main():
    for rel, text in NEW_FILES:
        path = os.path.join(HERE, *rel.split('/'))
        if os.path.exists(path):
            with open(path, 'rb') as f:
                have = f.read().replace(b'\r\n', b'\n')
            if have != text.encode('ascii'):
                print("ERROR: %s already exists and differs from this patch's "
                      "copy. Delete it and run again. NOTHING was written."
                      % rel)
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
                  "it has not, the file is not the one pushed at 97a8b733: "
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
          "the orrery. Suggested summary: L539 close record")


if __name__ == '__main__':
    main()
