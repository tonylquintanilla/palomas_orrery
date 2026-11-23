"""
patch_L539_3_skills_bump.py -- the one skills bump, protocol v3.145:
five skills gain the rules three builds listed on the ledger and wrote
into no skill. L-539 (every entry checked), L-541 (a plan's clock),
L-529 (guided encounters), L-545 (checks that wait to be remembered)
and L-550 (a website check's dashboard button).

Built on 849bf462 at https://github.com/tonylquintanilla/palomas_orrery
(branch main), with gallery e6af10ea at
https://github.com/tonylquintanilla/tonyquintanilla.github.io read for
the code. Written by the coordinating session (Claude Fable 5.2) under
safe-file-editing 1.14 and ledger-and-session-records 1.23, from
documentation/HANDOFF_coordinator_20261122_bump_notes.md and the
ledger.

Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\

RUN COMMAND
    This file is in the orrery folder (palomas_orrery_for_github). Open
    it in VS Code and click Run:

        python patch_L539_3_skills_bump.py

    Success: one "ok" line per edit, "patch applied", then four tools,
    each printing "ok": skills_index.py, ledger_index.py,
    skills_index.py --check and doc_index.py --caps.
    Failure: an "ERROR:" or "ANCHOR FAIL" line, and NOTHING is written.
    Undo after a success: Discard Changes in GitHub Desktop.
    Once it has run, move it to the documentation folder.

WHY
    By the records skill's binding rule a skill bump travels as four
    steps in one commit: the SKILL.md, skills_index.py, a protocol
    version entry, and the commit. One bump for all five, so the
    skills are reinstalled once, before the next website build.

WHAT IT CHANGES (68 edits, 10 files; no code)
    skills/horizons-orbital-mechanics/SKILL.md, 1.19 -> 1.20. The
        entries the website does not serve (horizons_unserved.py);
        JPL's dates on JPL's clock; astroquery's fall-through to the
        asteroids. Three corrections: Orcus's and Patroclus's
        barycentre numbers, a sixth skip list, the astroquery version.
        904 lines, its cap.
    skills/gallery-cache-builder/SKILL.md, 1.20 -> 1.21. The Clock
        Block and Its Witness, new; an encounter's package under
        Sibling directory semantics. One sentence gone out of date is
        corrected: the website's second night run exists. 944, its cap.
    skills/gallery-assembler/SKILL.md, 1.4 -> 1.5. One seam between
        the visitor's clock and JPL's, new. 307, its cap.
    skills/interactive-exhibit/SKILL.md, 1.44 -> 1.45. A visitor reads
        UTC, new; under Phone first, a session that changes the page
        runs the walks, and who adds a new row's dashboard button.
        738, its cap.
    skills/safe-file-editing/SKILL.md, 1.14 -> 1.15. A mark outside
        ASCII is typed as its escape and the bytes are read; a placed
        file is read back. 763 of 765.
    documentation/SKILL_HISTORIES.md: receives, word for word, each
        skill's oldest version entry and the passages that moved so
        each skill stayed at its cap; a new section for
        gallery-assembler.
    PROJECT_INSTRUCTIONS.md: the v3.145 entry, the header's version,
        date and SHA; v3.142 moves down. skills_index.py then rewrites
        the manifest's five rows and the read plans. 1394, its cap.
    documentation/PROJECT_INSTRUCTIONS_HISTORY.md: receives v3.142.
    LEDGER_CONSOLIDATED.md: L-539, L-541, L-529, L-545 and L-550, the
        skill text written; L-548, a note. No status changes.
    documentation/WHERE_WE_ARE.md: the header line, "Do next", and one
        line of "Needs you now" replaced (start this session -> the
        reinstall and the paste). 130 lines above the marker, its cap.
        Nothing below the marker is touched.

AFTER IT RUNS
    1. (do) Move this file, and patch_L539_1 and patch_L539_2 if they
       are still beside it, into the documentation folder.
    2. (do) Commit and push the orrery, not while a night is running.
    3. (do) Reinstall five skills (Plugins, in the claude.ai sidebar):
       horizons-orbital-mechanics, gallery-assembler,
       interactive-exhibit, gallery-cache-builder, safe-file-editing.
    4. (do) Paste PROJECT_INSTRUCTIONS.md into the Project's
       instructions on claude.ai.

Tested on a fresh copy of the orrery at 849bf462: every edit applied,
the four tools passed, each skill ended at or under its cap, and a
second run refused and wrote nothing.

Written November 22, 2026 with Anthropic's Claude Fable 5.2.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

EDITS = [('skills/safe-file-editing/SKILL.md',
  'Skill version: 1.14 | 2026-10-25, with',
  "Skill version: 1.15 | 2026-11-22, with Anthropic's Claude Fable 5.2, at\n"
  'palomas_orrery @ 849bf462. v1.15 (L-529, guided encounters, and the\n'
  'coordinating session of 2026-11-22) adds two rules. A MARK OUTSIDE\n'
  'ASCII IS TYPED AS ITS ESCAPE, AND THE BYTES ARE READ AFTER THE EDIT,\n'
  'under Unicode-Safe Editing; and A PLACED FILE IS READ BACK, under A\n'
  'Delivered Patch Is Final. To stay at the cap, the 1.12 entry moved out.\n'
  'Earlier: 1.14 | 2026-10-25, with'),
 ('skills/safe-file-editing/SKILL.md',
  'Earlier: 1.12 | Cut from palomas_orrery @ 41c1ca7a (v1.12),\n'
  'earlier @ 1fa413d9 (v1.11), ccd1ac96 (v1.10), bfa9de2f (v1.9),\n'
  'earlier @ 6d12ecac (v1.8), d424c459 (v1.7), ef3bd13 (v1.6),\n'
  '50438c6 (v1.5), a872205 (v1.4), 1ba20c3 (v1.3), 3398970 (v1.2),\n'
  "bdaaa0c (v1.1) | October 4, 2026, with Anthropic's Claude Opus 5.5\n"
  "(v1.12); August 29, 2026, with Anthropic's Claude Opus 5 (v1.11)\n"
  'v1.12 (L-415) makes the skill agree with itself about line endings.\n'
  'Fix In Passing listed "CRLF where the repo is LF" as a violation to\n'
  'fix, while Line Endings Are Not Content and Compare Content, Not Bytes\n'
  'told a patch to write each file back in the style it found. Tony asked\n'
  'why a patch was leaving Windows line endings in place: "I thought the\n'
  'rule was to convert to lf when found and report." The preserve rule\'s\n'
  'reason -- that flipping the endings shows every line changed -- was\n'
  'tested on 2026-10-04 and is false wherever the repo normalizes\n'
  "(`* text=auto eol=lf`, both of this project's repos): a CRLF working\n"
  'copy shows as modified with nothing inside it, and writing it LF clears\n'
  'that mark. It holds only for a file whose COMMITTED copy is CRLF. So a\n'
  'patch now writes LF and reports, except for those files.\n'
  'v1.11 (L-315) adds A Guard Must Not Fence What a Generator Rewrites,\n'
  'earned when three chained ledger patches all refused: each was\n'
  "fingerprinted against the previous one's raw output, while every one of\n"
  'them told the operator to run `ledger_index.py` next -- which rewrites\n'
  'the zone they were hashing.\n'
  'Older entries are in documentation/SKILL_HISTORIES.md, moved there\n'
  'on 2026-10-05 (L-418).\n',
  'Older entries are in documentation/SKILL_HISTORIES.md, moved there\n'
  'on 2026-10-05 (L-418) and 2026-11-22 (L-529).\n'),
 ('skills/safe-file-editing/SKILL.md',
  '| Uncertain                  | Python binary mode (always safe)|\n',
  '| Uncertain                  | Python binary mode (always safe)|\n'
  '\n'
  'A MARK OUTSIDE ASCII IS TYPED AS ITS ESCAPE, AND THE BYTES ARE READ\n'
  'AFTER THE EDIT (v1.15, L-529). In a file kept ASCII, such a mark is\n'
  'written as its `\\u` escape, as the file writes its others. Then read\n'
  "the file's bytes for anything above 0x7F: on 2026-11-20 an edit tool\n"
  'wrote raw characters where escapes had been typed (the website\n'
  "page's Play and Pause marks, an ellipsis, a walk's arrow), and only\n"
  'the bytes showed it.\n'),
 ('skills/safe-file-editing/SKILL.md',
  'refuse when it sees a document you gave to me as an artifact?")\n',
  'refuse when it sees a document you gave to me as an artifact?")\n'
  '\n'
  "**A placed file is read back** (v1.15). A file placed in the person's\n"
  'folder from a linked session is read back, its size at least, before\n'
  'they are told it is there. On 2026-11-22 a prompt file changed and\n'
  'placed again arrived with its first content under a new date; the\n'
  'size, 1,666 bytes where 1,987 were sent, showed it, and a second\n'
  'placement seconds later landed.\n'),
 ('documentation/SKILL_HISTORIES.md',
  '\n## orrery-coding-conventions\n',
  '\n'
  'Earlier: 1.12 | Cut from palomas_orrery @ 41c1ca7a (v1.12),\n'
  'earlier @ 1fa413d9 (v1.11), ccd1ac96 (v1.10), bfa9de2f (v1.9),\n'
  'earlier @ 6d12ecac (v1.8), d424c459 (v1.7), ef3bd13 (v1.6),\n'
  '50438c6 (v1.5), a872205 (v1.4), 1ba20c3 (v1.3), 3398970 (v1.2),\n'
  "bdaaa0c (v1.1) | October 4, 2026, with Anthropic's Claude Opus 5.5\n"
  "(v1.12); August 29, 2026, with Anthropic's Claude Opus 5 (v1.11)\n"
  'v1.12 (L-415) makes the skill agree with itself about line endings.\n'
  'Fix In Passing listed "CRLF where the repo is LF" as a violation to\n'
  'fix, while Line Endings Are Not Content and Compare Content, Not Bytes\n'
  'told a patch to write each file back in the style it found. Tony asked\n'
  'why a patch was leaving Windows line endings in place: "I thought the\n'
  'rule was to convert to lf when found and report." The preserve rule\'s\n'
  'reason -- that flipping the endings shows every line changed -- was\n'
  'tested on 2026-10-04 and is false wherever the repo normalizes\n'
  "(`* text=auto eol=lf`, both of this project's repos): a CRLF working\n"
  'copy shows as modified with nothing inside it, and writing it LF clears\n'
  'that mark. It holds only for a file whose COMMITTED copy is CRLF. So a\n'
  'patch now writes LF and reports, except for those files.\n'
  'v1.11 (L-315) adds A Guard Must Not Fence What a Generator Rewrites,\n'
  'earned when three chained ledger patches all refused: each was\n'
  "fingerprinted against the previous one's raw output, while every one of\n"
  'them told the operator to run `ledger_index.py` next -- which rewrites\n'
  'the zone they were hashing.\n'
  '(Moved down 2026-11-22, when 1.15 made a fourth entry.)\n'
  '\n'
  '## orrery-coding-conventions\n'),
 ('skills/gallery-assembler/SKILL.md',
  'fires_when: render_orbits.py, resolver.py, cache_reader.py, propagation '
  'math,',
  'fires_when: render_orbits.py, resolver.py, cache_reader.py, the seam '
  "between UTC and JPL's clock, propagation math,"),
 ('skills/gallery-assembler/SKILL.md',
  'Skill version: 1.4 | Cut from orrery @ b3ce81f8 and gallery @ cea21af1\n'
  '(v1.4), earlier @ 159c5a2c (v1.3), @ 5b3fb6b4 (v1.2),\n'
  '@ f83a3abc72c5516e6dc2ad264be53ce95b68cf38 (v1.1) | 2026-11-10\n',
  'Skill version: 1.5 | Cut from orrery @ 849bf462 and gallery @ e6af10ea\n'
  '(v1.5), earlier @ b3ce81f8 and cea21af1 (v1.4), @ 159c5a2c (v1.3) |\n'
  "2026-11-22, with Anthropic's Claude Fable 5.2\n"
  "v1.5 (L-541, a plan's clock) adds One seam between the visitor's clock\n"
  "and JPL's: resolver.py adds the served difference once and nothing\n"
  'downstream converts again. Written by the coordinating session from\n'
  "L-541's notes and the gallery at e6af10ea. To stay at the cap, the\n"
  'v1.2 entry and five passages moved to '
  'documentation/SKILL_HISTORIES.md.\n'),
 ('skills/gallery-assembler/SKILL.md',
  'v1.2 (L-279) adds Mode 5 as Measurement and the Plotly event-handler\n'
  'field note, both earned by the 2026-09-02 Sun exhibit hang: eight reads\n'
  'to attribute a two-line bug, and three wrong readings on the way, every\n'
  'one of them from inferring the test conditions instead of stating them.\n',
  ''),
 ('skills/gallery-assembler/SKILL.md',
  'assembler. (Encke is the known exception -- in objects_config.json for\n'
  'M1/M2 testing ahead of the orrery; confirmed absent from\n'
  'celestial_objects.py as of July 20, 2026. Closing that gap doubles as a\n'
  'live test of the porting pipeline.)\n',
  'assembler.\n'),
 ('skills/gallery-assembler/SKILL.md',
  'to include it. (Known stale docs: cache_reader.py AND resolver.py both '
  'still say\n'
  'served_window is "currently null at HEAD... tracked with F1" -- pre-M2,\n'
  "no longer true; fix next time you're in that file.)\n",
  'to include it.\n'),
 ('skills/gallery-assembler/SKILL.md',
  'the render is right":\n'
  'Pluto/Charon and Moon/Io/Titan are both, as of July 20 2026, in the state '
  'of\n'
  '"data plumbing partially tested, render never attempted."\n',
  'the render is right".\n'),
 ('skills/gallery-assembler/SKILL.md',
  'Two hypotheses died before this one was found, and both are worth\n'
  'keeping because neither was unreasonable. Hover hit-testing was blamed\n'
  'first -- `Plotly.Fx.unhover` was tested directly and changed nothing.\n'
  'Trace size was blamed second, on the ~65,000 argument limit -- the\n'
  'largest trace in that scene is 4,332 points and the one that hung is '
  '400.\n'
  '\n',
  ''),
 ('skills/gallery-assembler/SKILL.md',
  'within 400 ms of it. (L-302, gallery `700b426d`.)\n'
  '\n'
  'Live example: gallery `700b426d`, `index.html`.\n',
  'within 400 ms of it. (L-302, gallery `700b426d`, `index.html`.)\n'),
 ('skills/gallery-assembler/SKILL.md',
  '## Golden artifact process\n',
  "## One seam between the visitor's clock and JPL's (v1.5, L-541)\n"
  '\n'
  "A served `jd`, an orbit's date and a plan's moment are on JPL's clock\n"
  '(TDB); the minute a room is asked for is UTC. `resolver.py` is the one\n'
  'place they meet: it checks the UTC minute against the served window,\n'
  'which the builder makes on UTC, then adds the served difference\n'
  '(`coverage_index.json`, `clock.tdb_minus_utc_s`) once. The context\n'
  'carries both (`asked_utc_jd`, `resolved_epoch_jd`), and the drivers\n'
  'hand the page `moment_utc_jd` and `moment_tdb_jd`; the old `epoch_jd`\n'
  'and `epochJd` are gone. Nothing downstream converts again. With no\n'
  "clock block the room draws as before and warns. The gallery run's Room\n"
  "clock row holds it against JPL's places. Detail: the gallery's\n"
  "`INTERACTIVE_AS_BUILT.md`, The rooms' clock.\n"
  '\n'
  '## Golden artifact process\n'),
 ('documentation/SKILL_HISTORIES.md',
  '- social_media_export.py is mostly superseded by Studio; its\n'
  '  _parse_hover_html() survives as a shared utility.\n',
  '- social_media_export.py is mostly superseded by Studio; its\n'
  '  _parse_hover_html() survives as a shared utility.\n'
  '\n'
  '## gallery-assembler\n'
  '\n'
  'Moved here on 2026-11-22 (L-541), when 1.5 added One seam between the\n'
  "visitor's clock and JPL's and the skill stood at its cap. The v1.2\n"
  'entry:\n'
  '\n'
  'v1.2 (L-279) adds Mode 5 as Measurement and the Plotly event-handler\n'
  'field note, both earned by the 2026-09-02 Sun exhibit hang: eight reads\n'
  'to attribute a two-line bug, and three wrong readings on the way, every\n'
  'one of them from inferring the test conditions instead of stating them.\n'
  '(Moved down 2026-11-22, when 1.5 made a fourth entry.)\n'
  '\n'
  'Five passages, word for word. The first three had gone out of date:\n'
  'Encke is in celestial_objects.py since 2026-10-10 (L-395), the two\n'
  'docstrings were corrected, and moons are drawn in the root since\n'
  '2026-11-10 (L-515).\n'
  '- From The boundary this skill exists to protect, after the Rule:\n'
  '(Encke is the known exception -- in objects_config.json for\n'
  'M1/M2 testing ahead of the orrery; confirmed absent from\n'
  'celestial_objects.py as of July 20, 2026. Closing that gap doubles as a\n'
  'live test of the porting pipeline.)\n'
  '- From The three core modules, cache_reader.py:\n'
  '(Known stale docs: cache_reader.py AND resolver.py both still say\n'
  'served_window is "currently null at HEAD... tracked with F1" -- pre-M2,\n'
  "no longer true; fix next time you're in that file.)\n"
  "- From Layered gate, distinct from gallery-cache-builder's:\n"
  'Pluto/Charon and Moon/Io/Titan are both, as of July 20 2026, in the state '
  'of\n'
  '"data plumbing partially tested, render never attempted."\n'
  '- From Field note: never mutate a plot from inside a Plotly event\n'
  '  handler:\n'
  'Two hypotheses died before this one was found, and both are worth\n'
  'keeping because neither was unreasonable. Hover hit-testing was blamed\n'
  'first -- `Plotly.Fx.unhover` was tested directly and changed nothing.\n'
  'Trace size was blamed second, on the ~65,000 argument limit -- the\n'
  'largest trace in that scene is 4,332 points and the one that hung is '
  '400.\n'
  '- The last line of Field note: a plotly_click bubbles as a DOM click,\n'
  '  folded into the line above it:\n'
  'Live example: gallery `700b426d`, `index.html`.\n'),
 ('skills/interactive-exhibit/SKILL.md',
  "a card's fold beside a row (Scenes, Encounters, Links)\n---\n",
  "a card's fold beside a row (Scenes, Encounters, Links); a date a visitor "
  "reads (UTC); a page change's walks\n"
  '---\n'),
 ('skills/interactive-exhibit/SKILL.md',
  'Skill version: 1.44 | 2026-11-21, with',
  "Skill version: 1.45 | 2026-11-22, with Anthropic's Claude Fable 5.2, at\n"
  'palomas_orrery @ 849bf462 and gallery @ e6af10ea. v1.45 (L-541, L-545,\n'
  "L-550) adds A VISITOR READS UTC; JPL'S DATES ARE ON JPL'S CLOCK and,\n"
  'under Phone first, A SESSION THAT CHANGES THE PAGE RUNS THE WALKS, with\n'
  "who adds a new row's dashboard button; written from the ledger and the\n"
  'gallery at e6af10ea. The 1.42 entry and two passages moved out.\n'
  'Earlier: 1.44 | 2026-11-21, with'),
 ('skills/interactive-exhibit/SKILL.md',
  "Earlier: 1.42 | 2026-11-12, with Anthropic's Claude Opus 5.5, at\n"
  "palomas_orrery @ af8e1bdf and gallery @ 001d5046 (the session's bases;\n"
  "Tony's checkpoint pushes since, to gallery ae0d7ac0). v1.42 (L-527, a\n"
  "first visit's guide) adds two rules. A GUIDE ASKS FOR ONE ACTION AND\n"
  'WAITS FOR IT: its cards give instructions only, so it adds no claim to\n'
  "source; a card ends only on its own action, told by the page's own\n"
  'functions, never on a timer; a camera move it makes is worked out from\n'
  'what is drawn; its steps, words, setting and sums are\n'
  "gallery/first_guide.js, held by the gallery run's First guide row and\n"
  'walked by tools/headless/walk_first_guide.js. And A ROOM IS BUILT AND\n'
  "TESTED UPRIGHT (Tony's ruling of 2026-11-12, 13:18 and 13:44): held\n"
  'sideways a room shows one line asking for the phone upright, and the\n'
  'phone look and the walks are upright. Seven field notes of September\n'
  '(L-278, L-282, L-289, L-334), each held by a rule above them or by the\n'
  "writer's own suite, moved to documentation/SKILL_HISTORIES.md.\n",
  ''),
 ('skills/interactive-exhibit/SKILL.md',
  '2026-11-19 (L-297) and 2026-11-21 (L-529).\n',
  '2026-11-19 (L-297), 2026-11-21 (L-529) and 2026-11-22 (L-541).\n'),
 ('skills/interactive-exhibit/SKILL.md',
  '  - An encounter is a package played in a room of its own [QUALITY]\n',
  '  - An encounter is a package played in a room of its own [QUALITY]\n'
  "  - A visitor reads UTC; JPL's dates are on JPL's clock [QUALITY]\n"),
 ('skills/interactive-exhibit/SKILL.md',
  'Before 2026-09-18 a shell was found by the END of its legend group name,\n'
  'which was a second reading of the label formula the renderers build. Two\n'
  'readings of one formula is how they come to disagree. There is one way\n'
  'of matching now; do not add a second.\n',
  'A shell is matched one way, by its key; do not add a second.\n'),
 ('skills/interactive-exhibit/SKILL.md',
  'they check only the line and the pause. A saved picture, Earth\n'
  "Science's above all, may still be landscape; a room is not.\n",
  'they check only the line and the pause. A saved picture, Earth\n'
  "Science's above all, may still be landscape; a room is not.\n"
  '\n'
  'A SESSION THAT CHANGES THE PAGE RUNS THE WALKS (v1.45, L-545; Tony,\n'
  '2026-11-21: "should this be method?"). After a change to\n'
  '`interactive.html` or a script it loads, before the closing report:\n'
  '`tools/headless/walk_solar_system_drawer.js` and `walk_scene_moment.js`\n'
  '(jsdom 24.1.3 from npm, in a scratch folder), each count and any red\n'
  'check by name; and the gallery run on a copy holding only what a push\n'
  'carries (L-543). On Nov 21 a walk caught a day one day early that 53\n'
  'green rows had passed. A NEW GALLERY-RUN ROW NEEDS A DASHBOARD BUTTON\n'
  'in the orrery, which a website session may not edit: the brief says\n'
  'who adds it, and the closing report names it as owed (L-550).\n'),
 ('skills/interactive-exhibit/SKILL.md',
  '### The touch path is not the mouse path [QUALITY]\n',
  "### A visitor reads UTC; JPL's dates are on JPL's clock [QUALITY]\n"
  'v1.45, L-541 (Tony, 2026-11-21: "Yes"). Every date a visitor reads is\n'
  "UTC, and the date line is the visitor's own minute. A served `jd`, an\n"
  "orbit's date and a plan's moment are on JPL's clock (TDB), about 69 s\n"
  'ahead. The assembler converts once (gallery-assembler, One seam) and\n'
  'hands the page `moment_utc_jd` to print and `moment_tdb_jd` for lookups\n'
  'and drift; no page subtracts one from the other. A day printed from a\n'
  "JPL date is taken back to UTC first (`planDay`); a served point's is\n"
  'then read at the nearest minute (`SolarSystemFigures.servedDay`),\n'
  "since daily points are asked 9 s before UTC midnight. Only a body's\n"
  "source line names JPL's clock.\n"
  '\n'
  '### The touch path is not the mouse path [QUALITY]\n'),
 ('skills/interactive-exhibit/SKILL.md',
  "- 2026-09-18, L-334: a check that could not fail. The writer's suite\n"
  '  asserted that refusing `value` produced a message MENTIONING "value"\n'
  '  -- and "value" is in the path, so emptying the refusal list left the\n'
  '  suite green. It now asserts the reason. Found by emptying the list on\n'
  '  purpose, which is the only way that class of hole is ever found.\n'
  '- 2026-09-18, L-334: the stamp check had a blind spot of its own. It\n'
  "  built Earth's features without the Sun direction, so the magnetopause\n"
  "  and the bow shock drew nothing and two of Earth's sixteen shells were\n"
  '  never examined. A check that examines less than it appears to is the\n'
  '  same failure as a check that cannot fail.\n'
  "- 2026-09-06, L-288: Studio authors the exhibit's card; the card is a\n"
  '  placard with an Interactive tag and needs no picture (the lobby\n'
  '  settled that on the phone).\n',
  'Three notes of September (L-334, L-288) are in the histories.\n'),
 ('skills/interactive-exhibit/SKILL.md',
  '1.0 to 1.43: documentation/SKILL_HISTORIES.md, under '
  'interactive-exhibit.\n'
  '1.44 was written on 2026-11-21 by the coordinating session for L-529\n'
  "and L-540, from the repo's copy of 1.43; a session that loads the\n"
  "account's copy confirms it reads 1.44 before exhibit work.\n",
  '1.0 to 1.44: documentation/SKILL_HISTORIES.md, under '
  'interactive-exhibit.\n'
  '1.45 was written on 2026-11-22 by the coordinating session for L-541,\n'
  "L-545 and L-550, from the repo's copy of 1.44; a session that loads the\n"
  "account's copy confirms it reads 1.45 before exhibit work.\n"),
 ('documentation/SKILL_HISTORIES.md',
  '\n## safe-file-editing\n',
  '\n'
  "Earlier: 1.42 | 2026-11-12, with Anthropic's Claude Opus 5.5, at\n"
  "palomas_orrery @ af8e1bdf and gallery @ 001d5046 (the session's bases;\n"
  "Tony's checkpoint pushes since, to gallery ae0d7ac0). v1.42 (L-527, a\n"
  "first visit's guide) adds two rules. A GUIDE ASKS FOR ONE ACTION AND\n"
  'WAITS FOR IT: its cards give instructions only, so it adds no claim to\n'
  "source; a card ends only on its own action, told by the page's own\n"
  'functions, never on a timer; a camera move it makes is worked out from\n'
  'what is drawn; its steps, words, setting and sums are\n'
  "gallery/first_guide.js, held by the gallery run's First guide row and\n"
  'walked by tools/headless/walk_first_guide.js. And A ROOM IS BUILT AND\n'
  "TESTED UPRIGHT (Tony's ruling of 2026-11-12, 13:18 and 13:44): held\n"
  'sideways a room shows one line asking for the phone upright, and the\n'
  'phone look and the walks are upright. Seven field notes of September\n'
  '(L-278, L-282, L-289, L-334), each held by a rule above them or by the\n'
  "writer's own suite, moved to documentation/SKILL_HISTORIES.md.\n"
  '(Moved down 2026-11-22, when 1.45 made a fourth entry.)\n'
  '\n'
  'Moved 2026-11-22 (L-541), to keep the skill at its cap, word for word.\n'
  'From A shell trace carries its key:\n'
  'Before 2026-09-18 a shell was found by the END of its legend group name,\n'
  'which was a second reading of the label formula the renderers build. Two\n'
  'readings of one formula is how they come to disagree. There is one way\n'
  'of matching now; do not add a second.\n'
  'The three field notes:\n'
  "- 2026-09-18, L-334: a check that could not fail. The writer's suite\n"
  '  asserted that refusing `value` produced a message MENTIONING "value"\n'
  '  -- and "value" is in the path, so emptying the refusal list left the\n'
  '  suite green. It now asserts the reason. Found by emptying the list on\n'
  '  purpose, which is the only way that class of hole is ever found.\n'
  '- 2026-09-18, L-334: the stamp check had a blind spot of its own. It\n'
  "  built Earth's features without the Sun direction, so the magnetopause\n"
  "  and the bow shock drew nothing and two of Earth's sixteen shells were\n"
  '  never examined. A check that examines less than it appears to is the\n'
  '  same failure as a check that cannot fail.\n'
  "- 2026-09-06, L-288: Studio authors the exhibit's card; the card is a\n"
  '  placard with an Interactive tag and needs no picture (the lobby\n'
  '  settled that on the phone).\n'
  'The 1.44 install, from Install and verify (its copy was confirmed\n'
  'loaded on 2026-11-22):\n'
  '1.44 was written on 2026-11-21 by the coordinating session for L-529\n'
  "and L-540, from the repo's copy of 1.43; a session that loads the\n"
  "account's copy confirms it reads 1.44 before exhibit work.\n"
  '\n'
  '## safe-file-editing\n'),
 ('skills/gallery-cache-builder/SKILL.md',
  "a Lagrange point served as a point (serving_shape 'point')\n---\n",
  "a Lagrange point served as a point (serving_shape 'point'), the clock "
  "block and its witness, an encounter's package\n"
  '---\n'),
 ('skills/gallery-cache-builder/SKILL.md',
  'Skill version: 1.20 | 2026-11-19, with',
  "Skill version: 1.21 | 2026-11-22, with Anthropic's Claude Fable 5.2, at\n"
  'palomas_orrery @ 849bf462 and gallery @ e6af10ea. v1.21 (L-541, a\n'
  "plan's clock; L-529, guided encounters) adds The Clock Block and Its\n"
  "Witness and, under Sibling directory semantics, an encounter's package.\n"
  "Riding it: the website's second night run exists. Written by the\n"
  'coordinating session from the ledger and the builder at e6af10ea. The\n'
  '1.18 entry and five passages of history moved out to stay at the cap.\n'
  'Earlier: 1.20 | 2026-11-19, with'),
 ('skills/gallery-cache-builder/SKILL.md',
  "Earlier: 1.18 | 2026-11-05, with Anthropic's Claude Opus 5.5, at\n"
  'palomas_orrery @ fb0a8dce and gallery @ 3660993e. v1.18 (L-507, more\n'
  "voyages, with L-510's carried sentences). A Comet on an Open Path Is a\n"
  "Path Body gains the mirror's side change across e = 1 and the offline\n"
  "suite's comparison with the export by name, with a stand-in orbit for a\n"
  'body newly drawn as one (gallery 3660993); the onboarding section says\n'
  "a comet that changes side needs none. The mirror's INSERTED list gains\n"
  "an ended mission's `mission_end`, `end_note` and `cutoff_note`, and An\n"
  "Ended Mission's Last Day gains the case where the path stops before the\n"
  'mission ended (Akatsuki, cut on the last day fitted to tracking). Read '
  "from the gallery's mirror, its suites and builder at\n"
  "3660993e and this session's edits before it was written.\n",
  ''),
 ('skills/gallery-cache-builder/SKILL.md',
  '2026-11-05 (L-507), 2026-11-11 (L-525) and 2026-11-19 (L-297).\n',
  '2026-11-05 (L-507), 2026-11-11 (L-525), 2026-11-19 (L-297) and\n'
  '2026-11-22 (L-541).\n'),
 ('skills/gallery-cache-builder/SKILL.md',
  '- A Lagrange Point Is Served as a Point [QUALITY]\n',
  '- A Lagrange Point Is Served as a Point [QUALITY]\n'
  '- The Clock Block and Its Witness [QUALITY]\n'),
 ('skills/gallery-cache-builder/SKILL.md',
  '  every future run; the sweep reaps the quarantine later.\n',
  '  every future run; the sweep reaps the quarantine later.\n'
  "- data/encounters/ is not the builder's (v1.21, L-529): an encounter's\n"
  '  package is written by hand by `tools/encounter_fetch.py`; the night\n'
  '  never runs, swaps or commits it, and the sibling check knows the\n'
  '  folder by name (interactive-exhibit, An encounter is a package).\n'),
 ('skills/gallery-cache-builder/SKILL.md',
  '  stand-in orbit, named when used. Piece C of C/2025 K1 went to an\n'
  '  orbit this way on 2026-11-05 (by hand that day, gallery e5352a86; the\n'
  '  mirror does it since).\n',
  '  stand-in orbit, named when used.\n'),
 ('skills/gallery-cache-builder/SKILL.md',
  "## A Small Body's Own Uncertainty Is Served [QUALITY]\n",
  '## The Clock Block and Its Witness [QUALITY]\n'
  '\n'
  "v1.21, L-541. A served `jd` is on JPL's clock (TDB) and a visitor's\n"
  'minute is UTC, so each build serves the difference in the index.\n'
  '- THE CLOCK BLOCK (`build_clock`, "clock"). JPL is asked its TDB-UT (a\n'
  '  vectors query for Mercury; the Horizons manual: "After 1962, UT means\n'
  '  UTC") at the window\'s first and last minute and the build\'s own;\n'
  '  astropy works out TDB minus UTC at the same minutes. The build stops,\n'
  '  by name, when JPL does not answer or names another body, when the two\n'
  "  differ by more than 0.001 s, or when JPL's moves by more than 0.004 s\n"
  "  across the window (a leap second inside it). Served: JPL's at the\n"
  "  build's minute, 69.1829 s on 2026-11-22.\n"
  "- THE WITNESS (`build_witness`). Each build serves JPL's places of\n"
  '  Mercury (from its orbit) and 3I/ATLAS (from served points) at its own\n'
  "  minute; the gallery run's Room clock row compares the room's places\n"
  '  with them. A witness does not share its clock with what it tests.\n'
  "- OPEN ON L-541: daily points are asked at 00:01:00 on JPL's clock, 9 s\n"
  '  before UTC midnight; keys and plan windows read as UTC.\n'
  '\n'
  "## A Small Body's Own Uncertainty Is Served [QUALITY]\n"),
 ('skills/gallery-cache-builder/SKILL.md',
  '  queued jobs may be dropped." On 2026-11-01 the website\'s 08:17 run\n'
  "  started at 15:15 UTC, 6 h 58 min late, and the orrery's 07:17 run at\n"
  '  14:17, 7 h 0 min late (6 h 22 min on 2026-10-31). A dropped night is\n'
  "  caught the same day by a second scheduled line: the orrery's at 11:17\n"
  '  UTC since 2026-11-01 (its `.github/workflows/nightly.yml`); the\n'
  "  website's at 12:17 comes with its next gallery session, and until\n"
  '  then its workflow carries the 08:17 line alone. A second firing is\n'
  '  harmless: the concurrency group queues it, and a clean second run\n'
  '  commits only its night record. The times stay (no reschedule): the\n'
  "  lag is GitHub's, not the clock's.\n",
  '  queued jobs may be dropped." Both nights started about seven hours\n'
  '  late on 2026-11-01. A dropped night is caught the same day by a\n'
  "  second scheduled line: the orrery's at 11:17 UTC, the website's at\n"
  '  12:17 (each `.github/workflows/nightly.yml`). A second firing is\n'
  '  harmless: the concurrency group queues it, and a clean second run\n'
  '  commits only its night record. The times stay (no reschedule): the\n'
  "  lag is GitHub's, not the clock's.\n"),
 ('skills/gallery-cache-builder/SKILL.md',
  'Apart from the pulls and the records, a step that reports a problem\n'
  "does not stop the next: the guest book's problems still do not stop the\n"
  'build. Nothing in\n'
  'the Daily Run commits or pushes. The Horizons\n'
  'check was its step 2 from 2026-10-10 to 2026-10-14 and moved into the\n'
  "orrery's maintenance run beside the objects export (L-395; Tony,\n"
  '2026-10-12: "the orrery stores and serves the data not the other way\n'
  'around"). The gallery\'s "Horizons confirmations" row still reads the\n'
  'dates JPL confirmed each object, from the pulled export, offline, and\n'
  'goes red, naming the objects, on the day a confirmation turns 30 days\n'
  "old: the cure is the orrery's maintenance run, then the push, then the\n"
  'pull here. `python daily_run.py --check` lists the steps and fails if a\n'
  'script is missing; the maintenance run runs it.\n',
  'Apart from the pulls and the records, a step that reports a problem\n'
  "does not stop the next: the guest book's problems still do not stop the\n"
  "build. Nothing in the Daily Run commits or pushes. The gallery's\n"
  '"Horizons confirmations" row still reads the dates JPL confirmed each\n'
  'object, from the pulled export, offline, and goes red, naming the\n'
  'objects, on the day a confirmation turns 30 days old: the cure is the\n'
  "orrery's maintenance run, then the push, then the pull here. `python\n"
  'daily_run.py --check` lists the steps and fails if a script is missing;\n'
  'the maintenance run runs it.\n'),
 ('skills/gallery-cache-builder/SKILL.md',
  "Learned 2026-11-01 (v1.16, L-484, with L-485). The orrery's export\n"
  "changed one served number on purpose -- Earth's inner Van Allen belt,\n"
  "9,600 km to 10,000 km, by the export's rounding fix of 2026-10-31 --\n"
  "and the website's night refused every cache built on it until a\n"
  "gallery session moved two pins: the website's run 2 (by hand, 14:24\n"
  'UTC) and run 3 (scheduled, 15:15 UTC) were red, "1 of 36 gating\n'
  'checkers FAILED: Display figures", and committed nothing, as designed.\n'
  "The renderers were right. Two of the website's CHECKS still held the\n"
  'old number.\n',
  "Learned 2026-11-01 (v1.16, L-484, L-485): the orrery's export moved one\n"
  "served number on purpose (Earth's inner Van Allen belt, 9,600 km to\n"
  "10,000 km) and two of the website's CHECKS still held the old one.\n"),
 ('skills/gallery-cache-builder/SKILL.md',
  '  gallery session after the ruler build, recorded on L-485.\n'
  '\n'
  "Origin: created for L-098 (Phase 1b) from Fable 5's 2026-07-12 Mode 7 "
  'review;\n'
  'every code fact verified against gallery HEAD 8e060677 / orrery HEAD '
  'e83fe9ce\n'
  "with Anthropic's Claude Opus 4.8.\n",
  '  gallery session after the ruler build, recorded on L-485.\n'),
 ('documentation/SKILL_HISTORIES.md',
  '\n## horizons-orbital-mechanics\n',
  '\n'
  "Earlier: 1.18 | 2026-11-05, with Anthropic's Claude Opus 5.5, at\n"
  'palomas_orrery @ fb0a8dce and gallery @ 3660993e. v1.18 (L-507, more\n'
  "voyages, with L-510's carried sentences). A Comet on an Open Path Is a\n"
  "Path Body gains the mirror's side change across e = 1 and the offline\n"
  "suite's comparison with the export by name, with a stand-in orbit for a\n"
  'body newly drawn as one (gallery 3660993); the onboarding section says\n'
  "a comet that changes side needs none. The mirror's INSERTED list gains\n"
  "an ended mission's `mission_end`, `end_note` and `cutoff_note`, and An\n"
  "Ended Mission's Last Day gains the case where the path stops before the\n"
  'mission ended (Akatsuki, cut on the last day fitted to tracking). Read '
  "from the gallery's mirror, its suites and builder at\n"
  "3660993e and this session's edits before it was written.\n"
  '(Moved down 2026-11-22, when 1.21 made a fourth entry.)\n'
  '\n'
  'Moved 2026-11-22 (L-541), to keep the skill at its cap, word for word:\n'
  '- From A Spacecraft Is Fetched by Its Plan, the end of A COMET ON AN\n'
  '  OPEN PATH IS A PATH BODY:\n'
  '  Piece C of C/2025 K1 went to an\n'
  '  orbit this way on 2026-11-05 (by hand that day, gallery e5352a86; the\n'
  '  mirror does it since).\n'
  '- From THE MORNING DOES NOT WAIT FOR THE NIGHT. Its last clause had\n'
  "  gone out of date: the website's workflow carries the 12:17 line,\n"
  '  read at gallery e6af10ea.\n'
  "  On 2026-11-01 the website's 08:17 run\n"
  "  started at 15:15 UTC, 6 h 58 min late, and the orrery's 07:17 run at\n"
  '  14:17, 7 h 0 min late (6 h 22 min on 2026-10-31). A dropped night is\n'
  "  caught the same day by a second scheduled line: the orrery's at 11:17\n"
  '  UTC since 2026-11-01 (its `.github/workflows/nightly.yml`); the\n'
  "  website's at 12:17 comes with its next gallery session, and until\n"
  '  then its workflow carries the 08:17 line alone.\n'
  "- From the end of The Daily Run's Steps:\n"
  'The Horizons\n'
  'check was its step 2 from 2026-10-10 to 2026-10-14 and moved into the\n'
  "orrery's maintenance run beside the objects export (L-395; Tony,\n"
  '2026-10-12: "the orrery stores and serves the data not the other way\n'
  'around").\n'
  '- The opening of A Served Number That Changes on Purpose:\n'
  "Learned 2026-11-01 (v1.16, L-484, with L-485). The orrery's export\n"
  "changed one served number on purpose -- Earth's inner Van Allen belt,\n"
  "9,600 km to 10,000 km, by the export's rounding fix of 2026-10-31 --\n"
  "and the website's night refused every cache built on it until a\n"
  "gallery session moved two pins: the website's run 2 (by hand, 14:24\n"
  'UTC) and run 3 (scheduled, 15:15 UTC) were red, "1 of 36 gating\n'
  'checkers FAILED: Display figures", and committed nothing, as designed.\n'
  "The renderers were right. Two of the website's CHECKS still held the\n"
  'old number.\n'
  "- The skill's last lines:\n"
  "Origin: created for L-098 (Phase 1b) from Fable 5's 2026-07-12 Mode 7 "
  'review;\n'
  'every code fact verified against gallery HEAD 8e060677 / orrery HEAD '
  'e83fe9ce\n'
  "with Anthropic's Claude Opus 4.8.\n"
  '\n'
  '## horizons-orbital-mechanics\n'),
 ('skills/horizons-orbital-mechanics/SKILL.md',
  'data/small_body_solutions.json)\n---\n',
  'data/small_body_solutions.json), an entry the website does not serve '
  "(horizons_unserved.py), JPL's dates on JPL's clock\n"
  '---\n'),
 ('skills/horizons-orbital-mechanics/SKILL.md',
  'Skill version: 1.19 | 2026-11-18, with',
  "Skill version: 1.20 | 2026-11-22, with Anthropic's Claude Fable 5.2, at\n"
  'palomas_orrery @ 849bf462 and gallery @ e6af10ea. v1.20 (L-539, every\n'
  "entry checked; L-541, a plan's clock). Where the Check Lives gains the\n"
  'entries the website does not serve (horizons_unserved.py); The Clock Is\n'
  "Read as UTC gains JPL's dates on JPL's clock. Three corrections: two\n"
  "barycentre numbers, a sixth skip list, astroquery's fall-through. From\n"
  'the ledger and the code at 849bf462; the 1.17 entry and five passages\n'
  'moved out.\n'
  'Earlier: 1.19 | 2026-11-18, with'),
 ('skills/horizons-orbital-mechanics/SKILL.md',
  "Earlier: 1.17 | 2026-11-04, evening, with Anthropic's Claude Opus\n"
  '5.5, at palomas_orrery @ 79018c0c and gallery @ 5abca2c6. v1.17 (L-512,\n'
  "part 1 and slice a's part A1). The orrery's plot decides path or orbit\n"
  "from the e of a body's typed elements when JPL's database has no record,\n"
  'and says so (A Named Failure, below). data/orbit_paths.json is retired\n'
  '(Tony\'s ruling 0 of 2026-11-04: "a heavy file that is wrong and nobody\n'
  'reads is a bad breadcrumb leading nowhere"), so the L-470 paragraph no\n'
  'longer sends a session to compare saved paths there, and the skip lists\n'
  'are five. Under Query Mechanics: every astroquery call in the repository\n'
  "now asks fresh, checked on Python's parser (test_orbit_cache.\n"
  'TestFreshCalls), where nine had not. Read from the code at 79018c0c and\n'
  "the session's own edits before it was written.\n",
  ''),
 ('skills/horizons-orbital-mechanics/SKILL.md',
  '(L-476), 2026-11-04 (L-510), 2026-11-04 (L-512), 2026-11-05 (L-507)\n'
  'and 2026-11-18 (L-533).\n',
  '(L-476), 2026-11-04 (L-510), 2026-11-04 (L-512), 2026-11-05 (L-507),\n'
  '2026-11-18 (L-533) and 2026-11-22 (L-539).\n'),
 ('skills/horizons-orbital-mechanics/SKILL.md',
  'The system-barycentre numbers for\n'
  "  Orcus (20090482) and Patroclus (20000617) are found in BOTH of JPL's\n"
  '  indexes, which the Horizons check reads as a wrong id_type (Checking\n'
  '  an Entry Against JPL, below); the small-body records 2004 DW and\n'
  '  A906 UL are found in one. Whether the drawing says "shared centre" is\n'
  "  the barycenter rule's, in orrery-coding-conventions.\n",
  'The system-barycentre numbers for\n'
  '  Orcus (20090482) and Patroclus (20000617) are major bodies, "asteroid\n'
  '  barycenter" (JPL, 2026-11-22). The small-body index finds each body\n'
  '  with that number as its SPKID, but its primary designation (2004 DW,\n'
  '  A906 UL) is not the number and the check keeps a small-body match by\n'
  '  designation, so neither is found in both (corrected v1.20, L-539).\n'
  '  Whether the drawing says "shared centre" is the barycenter rule\'s,\n'
  '  in orrery-coding-conventions.\n'),
 ('skills/horizons-orbital-mechanics/SKILL.md',
  'do not\n'
  '  judge from the name. Piece C of C/2025 K1, e 0.999994 and class COM,\n'
  '  is served as an orbit by the orrery since 2026-11-04, and drawn as one\n'
  '  by the website since 2026-11-05 (gallery e5352a86, L-510, its entry\n'
  "  made Hale-Bopp's: availability analytic, frame heliocentric); since\n"
  '  gallery 3660993 the objects mirror makes such a change by itself. The\n'
  '  open difference L-484 (the two agree) carried for it is closed by that\n'
  '  (v1.18; it had said "an open difference on L-484").\n',
  'do not\n  judge from the name.\n'),
 ('skills/horizons-orbital-mechanics/SKILL.md',
  '  Horizons returned nothing. A sixth, SKIP_HORIZONS_TRAJECTORY, guarded\n'
  "  only the saved-path file's writer and went with it (L-512, "
  '2026-11-04).\n'
  '  period_fetch.py copies the pre-fetch list as SKIP_NAMES. A name goes '
  'on\n'
  '  a list with a comment naming the record that failed, the centre it\n'
  '  failed around, and the date. Gonggong (id 920225088, its body-centre\n'
  '  record; helio_id 2007 OR10) was on all six from 2026-02-04 (commit\n'
  '  c60572d) with no such comment, and came off every list on 2026-10-23\n'
  "  (L-470): no failure on record. The lists' own comment speaks only for\n"
  '  the moons.\n',
  '  Horizons returned nothing. idealized_orbits.py has one more,\n'
  '  ANALYTICAL_ONLY_SATELLITES, written twice, with its own id for\n'
  '  Xiangliu, 92250881 (v1.20; L-549).\n'
  '  period_fetch.py copies the pre-fetch list as SKIP_NAMES. A name goes '
  'on\n'
  '  a list with a comment naming the record that failed, the centre it\n'
  '  failed around, and the date.\n'),
 ('skills/horizons-orbital-mechanics/SKILL.md',
  '- A STORE KEYED BY NAME DOES NOT NOTICE A NEW RECORD (L-470, L-512).\n'
  "  The orrery's path cache, data/orbit_paths.json on Tony's machine, was\n"
  "  keyed by name and centre, so when an entry's id changed, a path saved\n"
  '  under the old id was still served under the name (the C/2025 K1 patch\n'
  '  compared it and found it was the comet, within 0.024 AU of piece B on\n'
  '  320 dates). That file is retired since 2026-11-04 (L-512, ruling 0):\n'
  "  nothing in the app reads or writes it, and it filed JPL's points under\n"
  "  evenly spread dates, up to a month from JPL's own. So after an id\n"
  '  change there is no saved path to compare. A store of paths keeps each\n'
  "  body's JPL record number with them and holds, by name, a path whose\n"
  "  record differs from the entry's today (L-512, ruling 3, for the\n"
  '  positions record of its slice c; not built on 2026-11-04).\n',
  '- A STORE KEYED BY NAME DOES NOT NOTICE A NEW RECORD (L-470, L-512). A\n'
  "  store of paths keeps each body's JPL record number with them and\n"
  "  holds, by name, a path whose record differs from the entry's today\n"
  '  (L-512, ruling 3, for the positions record of its slice c; not built\n'
  "  on 2026-11-04). The orrery's old path cache, keyed by name and\n"
  '  centre, is retired (L-512, ruling 0).\n'),
 ('skills/horizons-orbital-mechanics/SKILL.md',
  "  JPL's 1.074 km/s around Earth, read 2026-10-30 02:00 UTC).\n",
  "  JPL's 1.074 km/s around Earth, read 2026-10-30 02:00 UTC).\n"
  "- JPL'S DATES ARE ON JPL'S CLOCK (v1.20, L-541, L-529). `datetime_jd`\n"
  "  is JDTDB, an elements epoch is on JPL's clock, a path plan's moments\n"
  '  are TDB; a page prints one as UTC only after converting it. The\n'
  "  difference is JPL's own TDB-UT, 69.183 s in November 2026 (69.184 s is\n"
  "  TT's figure, 32.184 + 37, a brief's mistake), and an old date has an\n"
  '  old one: 42.185 s on 4 March 1972, 56.182 s on 20 October 1989. Open\n'
  "  on L-541: the orrery's whole-second 69 (`utc_to_tdb`, `TDB_OFFSET`).\n"),
 ('skills/horizons-orbital-mechanics/SKILL.md',
  "Moved 2026-10-14 from the website's Daily Run into the orrery (Tony,\n"
  '2026-10-12: "the orrery stores and serves the data not the other way\n'
  'around"). The move\'s brief is\n'
  'documentation/HANDOFF_L395_horizons_check_move_brief_20261012.md; the\n'
  "build's record, documentation/HANDOFF_L431_build3_website_20261014.md.\n"
  '\n',
  ''),
 ('skills/horizons-orbital-mechanics/SKILL.md',
  '- The thirteen identity confirmations of 2026-10-10 were carried over\n'
  '  with their dates, so the move asked JPL nothing. The offline tests run\n'
  "  on JPL's recorded answers,\n"
  '  `documentation/worksheets/horizons_answers_L395.json`. Its identity\n'
  "  answers are JPL's own; its elements and data-sheet answers were\n"
  "  written in JPL's format by the build, which could not reach JPL, and\n"
  '  the file says so for each, so the first live run is the real test of\n'
  '  the parsing. The same file freezes the inputs the test runs on (the\n'
  '  three cache entries, the carried confirmations, the seeded sheets):\n'
  '  a test that read the live records would fail on the day the check\n'
  '  first worked.\n',
  '- THE ENTRIES THE WEBSITE DOES NOT SERVE (v1.20, L-539;\n'
  '  `horizons_unserved.py`, run by the check after the served ones) are\n'
  '  each held to the NAME and the KIND JPL gives its id, both stored in\n'
  '  `data/horizons_unserved_confirmations.json`, which the export does not\n'
  '  read. Which entries are asked is a rule read from the list and the\n'
  '  code, never a list of names: an entry that fits no side, or two with\n'
  '  one name, fails the run, and a skip written inline in the fetch code\n'
  '  is copied in the check and held to the code by a test. A planets-first\n'
  '  id found only among the asteroids FALLS THROUGH and fails by name\n'
  '  (3013, the L3 case). "JPL has no object for this id" is an answer\n'
  '  only when both indexes find nothing and the main service refuses the\n'
  '  id; anything else is a blind spot and fails. A first answer waits on\n'
  "  Tony's look: a session sets the mark from his words (`--mark <name>\n"
  "  --by <his run record>`), a name equal to JPL's marks itself, a\n"
  '  no-object answer never does. Asked again from day 20, ten a run, red\n'
  "  at day 30; never answered or differing, at once. The night's title\n"
  '  starts JPL DIFFERS or NEW JPL NAME.\n'
  "- The offline tests run on JPL's recorded answers, frozen with their\n"
  '  inputs: `documentation/worksheets/horizons_answers_L395.json` and,\n'
  '  for the unserved entries, `horizons_answers_L539.json`.\n'),
 ('skills/horizons-orbital-mechanics/SKILL.md',
  "- Cache structure: cache[name]['elements'] (nested dict) -- the elements\n"
  '  live one level down.\n',
  "- Cache structure: cache[name]['elements'] (nested dict) -- the elements\n"
  '  live one level down.\n'
  '- ASTROQUERY ASKS THE MAJOR BODIES FIRST AND FALLS THROUGH (v1.20,\n'
  "  L-539). id_type 'majorbody', 'id' and a blank all send the bare id;\n"
  '  JPL looks among the planets, moons and spacecraft and, finding none,\n'
  '  among the asteroids: two L3 entries drew asteroids 3013 and 33. Read\n'
  "  in 0.4.9.post1 (Tony's machine; requirements.txt asks >=0.4.6; this\n"
  "  skill's other notes name 0.4.11), whose own warning calls 'majorbody'\n"
  '  and \'id\' deprecated for None, "the same functionality" (L-548).\n'),
 ('documentation/SKILL_HISTORIES.md',
  '\n## earth-system-pipeline\n',
  '\n'
  "Earlier: 1.17 | 2026-11-04, evening, with Anthropic's Claude Opus\n"
  '5.5, at palomas_orrery @ 79018c0c and gallery @ 5abca2c6. v1.17 (L-512,\n'
  "part 1 and slice a's part A1). The orrery's plot decides path or orbit\n"
  "from the e of a body's typed elements when JPL's database has no record,\n"
  'and says so (A Named Failure, below). data/orbit_paths.json is retired\n'
  '(Tony\'s ruling 0 of 2026-11-04: "a heavy file that is wrong and nobody\n'
  'reads is a bad breadcrumb leading nowhere"), so the L-470 paragraph no\n'
  'longer sends a session to compare saved paths there, and the skip lists\n'
  'are five. Under Query Mechanics: every astroquery call in the repository\n'
  "now asks fresh, checked on Python's parser (test_orbit_cache.\n"
  'TestFreshCalls), where nine had not. Read from the code at 79018c0c and\n'
  "the session's own edits before it was written.\n"
  '(Moved down 2026-11-22, when 1.20 made a fourth entry.)\n'
  '\n'
  'Moved 2026-11-22 (L-539), to keep the skill at its cap, word for word:\n'
  '- From Which Record Serves a Body, AN OPEN ORBIT IS NOT AN ELLIPSE:\n'
  '  Piece C of C/2025 K1, e 0.999994 and class COM,\n'
  '  is served as an orbit by the orrery since 2026-11-04, and drawn as one\n'
  '  by the website since 2026-11-05 (gallery e5352a86, L-510, its entry\n'
  "  made Hale-Bopp's: availability analytic, frame heliocentric); since\n"
  '  gallery 3660993 the objects mirror makes such a change by itself. The\n'
  '  open difference L-484 (the two agree) carried for it is closed by that\n'
  '  (v1.18; it had said "an open difference on L-484").\n'
  '- From A SKIP NAMES WHAT FAILED, two passages:\n'
  '  A sixth, SKIP_HORIZONS_TRAJECTORY, guarded\n'
  "  only the saved-path file's writer and went with it (L-512, "
  '2026-11-04).\n'
  '  Gonggong (id 920225088, its body-centre\n'
  '  record; helio_id 2007 OR10) was on all six from 2026-02-04 (commit\n'
  '  c60572d) with no such comment, and came off every list on 2026-10-23\n'
  "  (L-470): no failure on record. The lists' own comment speaks only for\n"
  '  the moons.\n'
  '- From A STORE KEYED BY NAME DOES NOT NOTICE A NEW RECORD:\n'
  "  The orrery's path cache, data/orbit_paths.json on Tony's machine, was\n"
  "  keyed by name and centre, so when an entry's id changed, a path saved\n"
  '  under the old id was still served under the name (the C/2025 K1 patch\n'
  '  compared it and found it was the comet, within 0.024 AU of piece B on\n'
  '  320 dates). That file is retired since 2026-11-04 (L-512, ruling 0):\n'
  "  nothing in the app reads or writes it, and it filed JPL's points under\n"
  "  evenly spread dates, up to a month from JPL's own. So after an id\n"
  '  change there is no saved path to compare.\n'
  '- The opening of Where the Check Lives, and What It Compares:\n'
  "Moved 2026-10-14 from the website's Daily Run into the orrery (Tony,\n"
  '2026-10-12: "the orrery stores and serves the data not the other way\n'
  'around"). The move\'s brief is\n'
  'documentation/HANDOFF_L395_horizons_check_move_brief_20261012.md; the\n'
  "build's record, documentation/HANDOFF_L431_build3_website_20261014.md.\n"
  '- Its last bullet:\n'
  '- The thirteen identity confirmations of 2026-10-10 were carried over\n'
  '  with their dates, so the move asked JPL nothing. The offline tests run\n'
  "  on JPL's recorded answers,\n"
  '  `documentation/worksheets/horizons_answers_L395.json`. Its identity\n'
  "  answers are JPL's own; its elements and data-sheet answers were\n"
  "  written in JPL's format by the build, which could not reach JPL, and\n"
  '  the file says so for each, so the first live run is the real test of\n'
  '  the parsing. The same file freezes the inputs the test runs on (the\n'
  '  three cache entries, the carried confirmations, the seeded sheets):\n'
  '  a test that read the live records would fail on the day the check\n'
  '  first worked.\n'
  "- Corrected in 1.20, as it stood, from A TNO'S SMALL-BODY RECORD IS THE\n"
  "  PAIR'S CENTRE:\n"
  '  The system-barycentre numbers for\n'
  "  Orcus (20090482) and Patroclus (20000617) are found in BOTH of JPL's\n"
  '  indexes, which the Horizons check reads as a wrong id_type (Checking\n'
  '  an Entry Against JPL, below); the small-body records 2004 DW and\n'
  '  A906 UL are found in one. Whether the drawing says "shared centre" is\n'
  "  the barycenter rule's, in orrery-coding-conventions.\n"
  '\n'
  '## earth-system-pipeline\n'),
 ('PROJECT_INSTRUCTIONS.md',
  'Tony Quintanilla, PE | Claude | v3.144 | November 21, 2026\n',
  'Tony Quintanilla, PE | Claude | v3.145 | November 22, 2026\n'),
 ('PROJECT_INSTRUCTIONS.md',
  'Cut from bd70f584 at https://github.com/tonylquintanilla/palomas_orrery\n',
  'Cut from 849bf462 at '
  'https://github.com/tonylquintanilla/palomas_orrery\n'),
 ('PROJECT_INSTRUCTIONS.md',
  'v3.144 (November 21, 2026): No rule changed in this document. TWO\n',
  'v3.145 (November 22, 2026): No rule changed in this document. FIVE\n'
  "skill bumps in one, by the records skill's binding rule, from L-539\n"
  "(every entry checked), L-541 (a plan's clock), L-529 (guided\n"
  "encounters), L-545 (the walks) and L-550 (a new check's button).\n"
  '\n'
  'WHAT PROMPTED IT. Three builds by Claude Opus 5.5 in Claude Code listed\n'
  'their rules on the ledger and wrote no skill: the encounter (Nov 20),\n'
  "the rooms' clock (Nov 21), every entry checked against JPL (Nov 22).\n"
  'The coordinating session (Claude Fable 5.2) wrote the five from those\n'
  'notes and the code at orrery 849bf462 and gallery e6af10ea.\n'
  '\n'
  'WHAT CHANGED. horizons-orbital-mechanics 1.19 -> 1.20: the entries the\n'
  "website does not serve are held to JPL's name and kind; JPL's dates\n"
  "are on JPL's clock; three corrections. gallery-cache-builder 1.20 ->\n"
  "1.21: the clock block and its witness; an encounter's package.\n"
  "gallery-assembler 1.4 -> 1.5: one seam between the visitor's clock and\n"
  "JPL's. interactive-exhibit 1.44 -> 1.45: a visitor reads UTC; a page\n"
  "change runs the walks; who adds a new row's dashboard button.\n"
  'safe-file-editing 1.14 -> 1.15: a mark outside ASCII is typed as its\n'
  'escape and the bytes read; a placed file is read back. Each stayed at\n'
  'its cap by moving text, word for word, to SKILL_HISTORIES.md.\n'
  '\n'
  "THE OBLIGATION TRAVELS. Written from the repo's copies, as the manifest\n"
  'expected. Tony reinstalls all five (Plugins, in the claude.ai sidebar)\n'
  'and pastes this version into the Project; the next session that loads\n'
  'each from the account confirms 1.20, 1.21, 1.5, 1.45 or 1.15 first.\n'
  '\n'
  'The header stamp and the SHA anchor move with this entry.\n'
  '\n'
  'Version history: v3.142 moves down to\n'
  'documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\n'
  'resident.\n'
  '\n'
  'v3.144 (November 21, 2026): No rule changed in this document. TWO\n'),
 ('PROJECT_INSTRUCTIONS.md',
  'v3.142 (November 18, 2026): No rule changed in this document. ONE\n'
  "skill bump: horizons-orbital-mechanics 1.18 -> 1.19 (L-533, ESCAPADE's\n"
  "path), by the records skill's binding rule, on the brief's section 8\n"
  '(documentation/COORD_L533_escapade_path_brief_20261118.md: "The rule\n'
  'then goes into horizons-orbital-mechanics ... it is method from then\n'
  'on") and Tony\'s ruling of Nov 18 on the loiter: "Approved, with one\n'
  'tightening", then "the loiter ends at its flyby". A CRAFT RIDING NEAR A\n'
  'LAGRANGE POINT.\n'
  '\n'
  'WHAT PROMPTED IT. The Claude Code session of Nov 18 (Claude Opus 5.5),\n'
  "through the python_work door, built ESCAPADE's path on orrery 00c89ef0\n"
  "and gallery 1d3090bc, from Tony's prompt and the brief, in three parts\n"
  'with a report and his go-ahead after each.\n'
  '\n'
  'WHAT CHANGED. horizons-orbital-mechanics: THE LOITER, under How a\n'
  "Path's Events Are Found. A Lagrange point has no mass, so the orbiter\n"
  "rule cannot see a craft riding near one; ESCAPADE's year near L2 gave a\n"
  'false flyby of Earth and passes of the Sun. Sixty days or more within\n'
  "twice Earth's Hill sphere is one event at the point nearer on most\n"
  'days, ending at the flyby that ends it; inside it a pass of Earth is\n'
  'that flyby only when the path leaves within 15 days. To stay at the cap\n'
  "of 904 lines, the 1.16 entry and two passages of history (Galileo's and\n"
  "Cassini's first plans; the twelve's keying) moved to\n"
  'documentation/SKILL_HISTORIES.md.\n'
  '\n'
  'THE OBLIGATION TRAVELS. This session read horizons-orbital-mechanics\n'
  "1.18 from the repo's copy, as a Code session does, as the manifest\n"
  'expected. Tony reinstalls it (Settings > Skills) and pastes this\n'
  "version into the Project's instructions on claude.ai; the next session\n"
  'that loads it from the account confirms its copy reads 1.19 before\n'
  'Horizons work.\n'
  '\n'
  'The header stamp and the SHA anchor move with this entry.\n'
  '\n'
  'Version history: v3.139 moves down to\n'
  'documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\n'
  'resident.\n'
  '\n',
  ''),
 ('documentation/PROJECT_INSTRUCTIONS_HISTORY.md',
  '(Moved down from the resident protocol on 2026-11-21, when\n'
  'v3.144 made a fourth entry.)\n',
  '(Moved down from the resident protocol on 2026-11-21, when\n'
  'v3.144 made a fourth entry.)\n'
  '\n'
  'v3.142 (November 18, 2026): No rule changed in this document. ONE\n'
  "skill bump: horizons-orbital-mechanics 1.18 -> 1.19 (L-533, ESCAPADE's\n"
  "path), by the records skill's binding rule, on the brief's section 8\n"
  '(documentation/COORD_L533_escapade_path_brief_20261118.md: "The rule\n'
  'then goes into horizons-orbital-mechanics ... it is method from then\n'
  'on") and Tony\'s ruling of Nov 18 on the loiter: "Approved, with one\n'
  'tightening", then "the loiter ends at its flyby". A CRAFT RIDING NEAR A\n'
  'LAGRANGE POINT.\n'
  '\n'
  'WHAT PROMPTED IT. The Claude Code session of Nov 18 (Claude Opus 5.5),\n'
  "through the python_work door, built ESCAPADE's path on orrery 00c89ef0\n"
  "and gallery 1d3090bc, from Tony's prompt and the brief, in three parts\n"
  'with a report and his go-ahead after each.\n'
  '\n'
  'WHAT CHANGED. horizons-orbital-mechanics: THE LOITER, under How a\n'
  "Path's Events Are Found. A Lagrange point has no mass, so the orbiter\n"
  "rule cannot see a craft riding near one; ESCAPADE's year near L2 gave a\n"
  'false flyby of Earth and passes of the Sun. Sixty days or more within\n'
  "twice Earth's Hill sphere is one event at the point nearer on most\n"
  'days, ending at the flyby that ends it; inside it a pass of Earth is\n'
  'that flyby only when the path leaves within 15 days. To stay at the cap\n'
  "of 904 lines, the 1.16 entry and two passages of history (Galileo's and\n"
  "Cassini's first plans; the twelve's keying) moved to\n"
  'documentation/SKILL_HISTORIES.md.\n'
  '\n'
  'THE OBLIGATION TRAVELS. This session read horizons-orbital-mechanics\n'
  "1.18 from the repo's copy, as a Code session does, as the manifest\n"
  'expected. Tony reinstalls it (Settings > Skills) and pastes this\n'
  "version into the Project's instructions on claude.ai; the next session\n"
  'that loads it from the account confirms its copy reads 1.19 before\n'
  'Horizons work.\n'
  '\n'
  'The header stamp and the SHA anchor move with this entry.\n'
  '\n'
  'Version history: v3.139 moves down to\n'
  'documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\n'
  'resident.\n'
  '\n'
  '(Moved down from the resident protocol on 2026-11-22, when\n'
  'v3.145 made a fourth entry.)\n'),
 ('LEDGER_CONSOLIDATED.md',
  "**Gap:** the coordinating session's skill bump (the text above); the\n"
  "first night on GitHub after Tony's push,",
  '**Note:** THE SKILL TEXT IS WRITTEN (2026-11-22, the coordinating '
  'session, Claude Fable 5.2; protocol\n'
  'v3.145, patch_L539_3_skills_bump.py):\n'
  'horizons-orbital-mechanics 1.20 carries the eight rules above (Where\n'
  'the Check Lives, THE ENTRIES THE WEBSITE DOES NOT SERVE; Query\n'
  'Mechanics, the fall-through and the astroquery version) and the two\n'
  "corrections owed, with a third: idealized_orbits.py's own skip list.\n"
  '- **Tony-action (do):** reinstall five skills (Plugins, in the\n'
  '  claude.ai sidebar): horizons-orbital-mechanics, gallery-assembler,\n'
  '  interactive-exhibit, gallery-cache-builder, safe-file-editing; and\n'
  "  paste PROJECT_INSTRUCTIONS.md, v3.145, into the Project's\n"
  '  instructions.\n'
  '**Gap:** the next session confirms its loaded copies read 1.20, 1.21,\n'
  '1.5, 1.45 and 1.15; the\n'
  "first night on GitHub after Tony's push,"),
 ('LEDGER_CONSOLIDATED.md',
  '`utc_to_tdb` and `TDB_OFFSET`, which could read the served\n'
  "figure's way (JPL's TDB-UT); and the skill text\n"
  '(horizons-orbital-mechanics, gallery-assembler, interactive-exhibit,\n'
  "gallery-cache-builder), named in the build's closing report; the\n"
  'builder asks',
  '`utc_to_tdb` and `TDB_OFFSET`, which could read the served\n'
  "figure's way (JPL's TDB-UT); the skill text is written (2026-11-22, the "
  'coordinating session, Claude Fable 5.2; protocol\n'
  'v3.145, patch_L539_3_skills_bump.py):\n'
  'horizons-orbital-mechanics 1.20, gallery-assembler 1.5,\n'
  'interactive-exhibit 1.45 and gallery-cache-builder 1.21; the\n'
  'builder asks'),
 ('LEDGER_CONSOLIDATED.md',
  'Three of them also belong\n'
  "elsewhere and wait for those skills' next versions: the plan's clock,\n"
  "horizons-orbital-mechanics, with L-541 (a plan's clock); the escape\n"
  'rule, safe-file-editing, with L-471 (a delivered patch is final); the\n'
  "package's place and the night, gallery-cache-builder.\n",
  'Three of them also belonged\n'
  'elsewhere and are there since v3.145 (2026-11-22,\n'
  "patch_L539_3_skills_bump.py): the plan's clock,\n"
  'horizons-orbital-mechanics 1.20; the escape rule, safe-file-editing\n'
  "1.15; the package's place and the night, gallery-cache-builder 1.21.\n"),
 ('LEDGER_CONSOLIDATED.md',
  '<!-- L:545 status:OPEN upd:2026-11-21 section:A',
  '<!-- L:545 status:OPEN upd:2026-11-22 section:A'),
 ('LEDGER_CONSOLIDATED.md',
  '<!-- L:529 status:OPEN upd:2026-11-21 section:A',
  '<!-- L:529 status:OPEN upd:2026-11-22 section:A'),
 ('LEDGER_CONSOLIDATED.md',
  "**Gap:** the skill text, at interactive-exhibit's next version. Two\n"
  'rulings for Tony:',
  '**Gap:** the skill text is written (interactive-exhibit 1.45, Phone\n'
  "first; v3.145, 2026-11-22), the session's half only. Two\n"
  'rulings for Tony:'),
 ('LEDGER_CONSOLIDATED.md',
  '**Gap:** the rule, with the skills bump (v3.145): a brief for a website\n'
  'build that adds a gallery-run row says who adds the button, and the\n'
  "build's closing report names the button as owed. interactive-exhibit is\n"
  'its home.\n',
  '**Note:** THE RULE IS WRITTEN (2026-11-22, the coordinating session, '
  'Claude Fable 5.2; protocol\n'
  'v3.145, patch_L539_3_skills_bump.py):\n'
  'interactive-exhibit 1.45, the last sentences of Phone first: a brief\n'
  'for a website build that adds a gallery-run row says who adds the\n'
  "button, and the build's closing report names the button as owed.\n"
  '**Gap:** none of its own; it closes at the next close after a session\n'
  'has loaded interactive-exhibit 1.45 from the account.\n'),
 ('LEDGER_CONSOLIDATED.md',
  '**Gap:** a ruling: one default in every reader, or the list writing',
  '**Note:** (2026-11-22, the coordinating session, Claude Fable 5.2; '
  'protocol\n'
  "v3.145, patch_L539_3_skills_bump.py) astroquery's own\n"
  'warning, in Tony\'s output of Nov 22, says \'majorbody\' and \'id\' "are\n'
  'deprecated and replaced with ``None``, which has the same\n'
  'functionality": one more reason the default matters\n'
  '(horizons-orbital-mechanics 1.20, Query Mechanics).\n'
  '**Gap:** a ruling: one default in every reader, or the list writing'),
 ('documentation/WHERE_WE_ARE.md',
  "Last updated: November 22, 2026: the coordinating session's close. Every "
  'entry the orrery asks JPL for is checked against JPL; the skills bump is '
  "the next session's first job (Claude Fable 5.2).\n"
  '- Written on orrery 97a8b733 and gallery e6af10ea, both pushed;',
  'Last updated: November 22, 2026, evening: the skills bump, v3.145, is '
  'written; you reinstall five skills and paste the protocol (Claude Fable '
  '5.2).\n'
  '- Written on orrery 849bf462 and gallery e6af10ea, both pushed;'),
 ('documentation/WHERE_WE_ARE.md',
  '*The next coordinating session writes the one skills bump (v3.145) first, '
  'from `documentation/HANDOFF_coordinator_20261122_bump_notes.md`; then '
  'L-544 (L4 and L5 tie); then',
  '*The skills bump (v3.145) is written, Nov 22. Next, once you have '
  'reinstalled: L-544 (L4 and L5 tie), in the website; then'),
 ('documentation/WHERE_WE_ARE.md',
  '> - *(do) Start the next coordinating session with '
  '`documentation/PROMPT_coordinator_start_20261122_3.md`, pasted from below '
  'its line. The website builds wait for its skills bump.*\n',
  '> - *(do) Reinstall five skills (Plugins, in the claude.ai sidebar): '
  'horizons-orbital-mechanics, gallery-assembler, interactive-exhibit, '
  'gallery-cache-builder, safe-file-editing. Then paste '
  "`PROJECT_INSTRUCTIONS.md`, now v3.145, into the Project's instructions. "
  'The website builds wait for this (L-539 (every entry checked), L-541 (a '
  "plan's clock)).*\n")]


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
                  "Otherwise the file moved since this was built: tell "
                  "the session. NOTHING was written."
                  % (name, c, old[:70]))
            sys.exit(1)
        staged[name][0] = text.replace(o, n)
        print("ok   %s: %s" % (name, (old.strip().splitlines()
                                      or ['(end)'])[0][:52]))
    for name, (text, was_crlf) in staged.items():
        with open(os.path.join(HERE, *name.split('/')), 'wb') as f:
            f.write(text)
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % name)
    print("patch applied (%d edits, %d files)" % (len(EDITS), len(staged)))
    print("stamps updated: five skills' version lines, the protocol's "
          "header (v3.145, 849bf462), Where We Are's header")
    for tool in (["skills_index.py"], ["ledger_index.py"],
                 ["skills_index.py", "--check"], ["doc_index.py", "--caps"]):
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
    print("Do next: move this file (and patch_L539_1, patch_L539_2 if")
    print("still here) into documentation; commit and push the orrery;")
    print("reinstall five skills (horizons-orbital-mechanics,")
    print("gallery-assembler, interactive-exhibit, gallery-cache-builder,")
    print("safe-file-editing); paste PROJECT_INSTRUCTIONS.md into the")
    print("Project.")


if __name__ == '__main__':
    main()
