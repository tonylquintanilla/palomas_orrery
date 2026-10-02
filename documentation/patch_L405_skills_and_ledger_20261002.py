#!/usr/bin/env python3
"""
patch_L405_skills_and_ledger_20261002.py -- ORRERY repo.
Two skills catch up with this session's builds (L-405): the room skill
goes to 1.9 and the ledger skill to 1.14, and the protocol records them
as v3.77. And the session is recorded: the Exhibit Store Editor fix
(L-404), the Solar System room's drawer (L-363 step 3b), and Tony's page,
documentation/WHERE_WE_ARE.md.

This REPLACES both earlier orrery patches of this session,
patch_L404_ledger_20261001.py and patch_L404_L363_ledger_20261002.py.
Neither was run. Delete them.

Run: save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
open it in VS Code and click Run. The same as: python
patch_L405_skills_and_ledger_20261002.py

A patch is run from its repository's ROOT and filed in documentation/
AFTER it has run. This script refuses to run from documentation/.

Built on orrery b3cfc780676596fd2b1469af280ea5308a184a46
at https://github.com/tonylquintanilla/palomas_orrery
(gallery cfc534903792925ea7433e352c6a49ac894e6d08
at https://github.com/tonylquintanilla/tonyquintanilla.github.io;
not touched by this patch -- its own patch is
patch_L404_1_rooms_in_store_editor_20261001.py)

WHAT IT DOES.

  LEDGER_CONSOLIDATED.md          New L-404: the cause, what was built,
                                  how it was checked, and its Gap. New
                                  L-405: the skill text owed. On L-363,
                                  the step 3b note and Tony's
                                  confirmations. A header stamp. The index is rebuilt by
                                  the maintenance run, so this patch's
                                  guard does not look inside it.
  skills/interactive-exhibit/SKILL.md          1.8 -> 1.9
  skills/ledger-and-session-records/SKILL.md   1.13 -> 1.14
  PROJECT_INSTRUCTIONS.md         v3.77: header, cut-from SHA, the
                                  entry; v3.74 moves down
  documentation/PROJECT_INSTRUCTIONS_HISTORY.md   receives v3.74
  documentation/WHERE_WE_ARE.md   rewritten for this session.

Everything is written or nothing is.

SUCCESS looks like: one "ok" line per edit and per file, then "patch
applied". FAILURE looks like one ERROR: or ANCHOR FAIL: line, and
NOTHING is written. Undo is Discard Changes in GitHub Desktop.

Written October 2, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

SPEC = {'BASE': {'LEDGER_CONSOLIDATED.md': '25b9e9de1f39af364caa54c11cddf294',
          'PROJECT_INSTRUCTIONS.md': '4547b496d5244cfddf1c51dbaccdc12b',
          'documentation/PROJECT_INSTRUCTIONS_HISTORY.md': '7df1cf9676e4386fe1060103a30813f3',
          'documentation/WHERE_WE_ARE.md': '72cb92f2ae8300f07c6384823b7428de',
          'skills/interactive-exhibit/SKILL.md': 'bb5f572e69ab0abf5bbf2594e23f7a83',
          'skills/ledger-and-session-records/SKILL.md': 'bf5df249875dfa2a1f4bbe08cd18c4bf'},
 'EDITS': {'LEDGER_CONSOLIDATED.md': [('(L-398 done; L-401 and L-402 opened; L-363 note; a '
                                       'dashboard button for\n'
                                       'the Solar System figures check), built on c12994d2.\n',
                                       '(L-398 done; L-401 and L-402 opened; L-363 note; a '
                                       'dashboard button for\n'
                                       'the Solar System figures check), built on c12994d2.\n'
                                       "Module updated: October 2, 2026 with Anthropic's Claude "
                                       'Opus 5.5\n'
                                       '(L-404 opened: the Exhibit Store Editor lists every room, '
                                       'and can set\n'
                                       "the Solar System room's opening view; L-363 step 3b built, "
                                       'the drawer;\n'
                                       'L-405 opened and built: interactive-exhibit 1.9,\n'
                                       'ledger-and-session-records 1.14, protocol v3.77), built on '
                                       'b3cfc780.\n',
                                       'header stamp'),
                                      ('## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; '
                                       'cross-referenced)\n'
                                       '\n'
                                       '#### [L-403]',
                                       '## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; '
                                       'cross-referenced)\n'
                                       '\n'
                                       '#### [L-405] Skill text owed from the editor fix and the '
                                       'drawer build (skills)\n'
                                       '<!-- L:405 status:OPEN upd:2026-10-02 section:A flag: '
                                       'rice: -->\n'
                                       "- **From Tony's review of 2026-10-02**, sorting the "
                                       'session into method\n'
                                       '  already in the skills, method needing a skill, and his '
                                       'own drawing\n'
                                       '  decisions. Method that needs writing down, so the next '
                                       'session does\n'
                                       '  not have to rediscover or ask it:\n'
                                       '  - **interactive-exhibit:** (a) the sentence saying every '
                                       'reader of\n'
                                       '    data/objects_config.json ignores "rooms" is wrong -- '
                                       'the store\n'
                                       '    writer, the editor, their suites and '
                                       'tools/mirror_objects.py read\n'
                                       '    it (L-404, L-395); (b) what is editable in a '
                                       'rooms-section room --\n'
                                       "    its arrival's `drawn` and `highlight`, each a drawer "
                                       'row other than\n'
                                       "    the Sun -- and that the editor's room list is read "
                                       'from both places\n'
                                       '    a room can live (L-404); (c) the body drawer as shared '
                                       'chrome: the\n'
                                       "    Sun's fixed row, opened rows, See more, Home's tick "
                                       'order, rows\n'
                                       '    found by the group they name, and the room parameters\n'
                                       "    `frameOnPosition` / `frameMargin` with Tony's 20% "
                                       '(L-363 step 3b);\n'
                                       "    (d) the headless test recipe -- the room's real driver "
                                       'run in\n'
                                       '    CPython on the served cache, the real page booted in '
                                       'jsdom with a\n'
                                       '    stand-in Plotly, and the other rooms driven the same '
                                       'way before and\n'
                                       '    after a shared-chrome change, compared row by row. The '
                                       'harness\n'
                                       "    lives only in a session's scratch space today; whether "
                                       'it is filed\n'
                                       '    in the repo, marked as Claude-only, is part of this '
                                       'item.\n'
                                       '  - **ledger-and-session-records:** when a wrong sentence '
                                       'in a skill\n'
                                       '    earns a version bump, and when it is carried on the '
                                       'ledger to the\n'
                                       '    next bump instead. L-404 chose the second for one '
                                       'sentence; the\n'
                                       '    question recurs, so the skill should answer it.\n'
                                       '- **Built the same session, at Tony\'s word** ("I would '
                                       'rather take care\n'
                                       '  of the skills now and the numbers in the next '
                                       'session"):\n'
                                       '  interactive-exhibit 1.9 carries (a) to (d); '
                                       'ledger-and-session-records\n'
                                       '  1.14 carries the bump threshold as A Wrong Sentence in a '
                                       'Skill: Bump\n'
                                       '  Now, or Carry It; protocol v3.77 records both. The '
                                       'harness is filed in\n'
                                       "  the gallery's tools/headless/ by patch_L363_9 (four "
                                       'files, Claude-only,\n'
                                       "  not run by the maintenance run). The bump rule's wording "
                                       "is Claude's,\n"
                                       '  shown to Tony in the session.\n'
                                       '**Gap:** The next session confirms its loaded copies read\n'
                                       'interactive-exhibit 1.9 and ledger-and-session-records '
                                       '1.14, then\n'
                                       'closes this item.\n'
                                       '**Ref:** L-404; L-363; L-395; L-338; '
                                       'skills/interactive-exhibit/SKILL.md;\n'
                                       'skills/ledger-and-session-records/SKILL.md.\n'
                                       '\n'
                                       '#### [L-404] The Exhibit Store Editor did not list the '
                                       'Solar System room (gallery, tooling)\n'
                                       '<!-- L:404 status:OPEN upd:2026-10-01 section:A flag: '
                                       'rice: -->\n'
                                       "- **Tony's question, 2026-10-01**: he went to the editor "
                                       'to make the\n'
                                       '  Solar System room open on the inner planets, and its '
                                       'room list held\n'
                                       '  only Sun and Earth. "shouldn\'t all interactive rooms be '
                                       'available in\n'
                                       '  the drop down menu as they are created?" Yes.\n'
                                       '- **Cause** [read at gallery cfc53490]. '
                                       '`exhibit_store_editor.rooms()`\n'
                                       '  and `store_writer.editable_paths()` both found a room by '
                                       'one test: an\n'
                                       '  entry in `objects` carrying an arrival block. The Solar '
                                       'System room\n'
                                       "  is not one body, so its settings went into the config's "
                                       'top-level\n'
                                       '  "rooms" section on 2026-09-30 (L-392). Neither tool was '
                                       'taught to look\n'
                                       '  there. Built under L-334, before a second place for '
                                       'rooms existed.\n'
                                       '- **Built** (gallery '
                                       'patch_L404_1_rooms_in_store_editor_20261001.py, on\n'
                                       '  cfc53490). `store_writer.room_ids()` is the one room '
                                       'list, from both\n'
                                       '  places a room can live, so the next room added to either '
                                       'appears with\n'
                                       '  nothing else to change. The writer may change a '
                                       "rooms-section room's\n"
                                       '  `drawn` and `highlight`; each must name a drawer row '
                                       'other than the\n'
                                       '  Sun, which is always drawn. Nothing else in the section '
                                       'is writable.\n'
                                       '  The editor ticks the room\'s bodies, adds a "Highlighted '
                                       'row" picker,\n'
                                       "  and says in the form that the rows' own words are not "
                                       'edited there.\n'
                                       '- **Checks**. Writer suite check 9 (289 checks) and editor '
                                       'suite check\n'
                                       "  10 (269; 314 with the window walk). The editor's check "
                                       'works out the\n'
                                       '  expected room list from the raw JSON rather than asking '
                                       'the editor,\n'
                                       '  so it cannot agree by sharing the code. Proved able to '
                                       'fail: with\n'
                                       '  room_ids() cut back to the body rooms, both suites '
                                       'named\n'
                                       '  solar-system as missing; with the Sun let through as a '
                                       'tick, five\n'
                                       "  checks named it. Tony's own path was run in a real "
                                       'window headless:\n'
                                       '  pick solar-system, tick Mercury, Venus and Mars, Save -- '
                                       'one line of\n'
                                       '  data/objects_config.json changed, `"drawn": ["mercury", '
                                       '"venus",\n'
                                       '  "earth", "mars"]`. That save was made on a scratch copy '
                                       'only.\n'
                                       '- **Not in this build**, recorded rather than chased (The '
                                       'Braid): the\n'
                                       "  editor does not edit the Solar System room's row words "
                                       '(`label`,\n'
                                       '  `about`, `source_note`). Today a change to them comes as '
                                       'a patch.\n'
                                       '- **The Correction Does Not Travel**: interactive-exhibit '
                                       '1.8 says the\n'
                                       '  cache builder, the assembler and every check read only '
                                       '"objects" and\n'
                                       '  ignore the rooms section. The store writer and both '
                                       'suites now read\n'
                                       '  it (and tools/mirror_objects.py already read its rows '
                                       'under L-395).\n'
                                       "  That sentence is corrected at the skill's next version, "
                                       'carried on\n'
                                       '  L-405; no bump was made for one sentence.\n'
                                       '- **Skills this session**: interactive-exhibit 1.8 and\n'
                                       '  provenance-discipline 2.24 loaded as the manifest '
                                       'expects, which\n'
                                       '  discharges the obligation v3.76 carried. Also loaded and '
                                       'matching:\n'
                                       '  safe-file-editing 1.11, agentic-pre-test 1.2,\n'
                                       '  ledger-and-session-records 1.13.\n'
                                       '**Gap:**\n'
                                       '- Tony-action (do): gallery -- run the patch; in the '
                                       'editor pick\n'
                                       '  solar-system, tick Mercury, Venus and Mars, Save; run\n'
                                       '  gallery_maintenance_run.py; commit and push. The opening '
                                       'view needs\n'
                                       '  only the push, no cache rebuild.\n'
                                       '- Tony-action (do): orrery -- run '
                                       'patch_L405_skills_and_ledger_20261002.py and\n'
                                       '  orrery_maintenance_run.py; commit and push.\n'
                                       '- Closes when the room opens on the inner planets on the '
                                       'site. The\n'
                                       '  skill sentence above already lives on L-405.\n'
                                       '**Ref:** tools/store_writer.py, '
                                       'tools/exhibit_store_editor.py and their\n'
                                       'two suites (gallery); L-334 (the editor), L-392 (the rooms '
                                       'section),\n'
                                       'L-363 (the room), L-395.\n'
                                       '\n'
                                       '#### [L-403]',
                                       'L-405 and L-404 opened'),
                                      ('<!-- L:363 status:OPEN upd:2026-10-01 section:A flag: '
                                       'rice: -->\n'
                                       "- **2026-10-01, the front door decided, and the panel's "
                                       'words.**',
                                       '<!-- L:363 status:OPEN upd:2026-10-02 section:A flag: '
                                       'rice: -->\n'
                                       '- **2026-10-02, step 3b built: the drawer.** Gallery\n'
                                       '  patch_L363_9_room_step3b_drawer_20261002.py, on '
                                       'cfc53490, not yet run\n'
                                       "  or seen on a phone. Built from the design's sections 3 "
                                       'and 4 and\n'
                                       "  Tony's answers of 2026-09-30, with no new ruling:\n"
                                       "  - The Sun's row has no tick box and no GO; it still "
                                       'highlights and\n'
                                       '    opens. All / none leaves it alone.\n'
                                       '  - A name tap highlights its row and opens it; a second '
                                       'tap closes it.\n'
                                       '    An open row links "Enter the Sun room" or "Enter the '
                                       'Earth room", or\n'
                                       '    says "No room or cards yet". Whether a body has a room '
                                       'is read from\n'
                                       "    the page's EXHIBITS table, so the next room lights its "
                                       'row by itself.\n'
                                       '  - Ticking draws a body, highlights and opens its row, '
                                       'and frames\n'
                                       '    everything drawn. Apophis waits under See more / See '
                                       'fewer; a ticked\n'
                                       '    row never hides.\n'
                                       '  - A tap on a body in the picture highlights its row and '
                                       'moves nothing\n'
                                       '    (design 3.5). In step 3a it framed the body; GO still '
                                       'does.\n'
                                       '  - Home: the last body ticked that is still ticked, '
                                       'opening angle,\n'
                                       '    drawer closed, frame holding everything drawn, falling '
                                       'back through\n'
                                       '    the tick order (tab only). With nothing ticked it puts '
                                       'back what the\n'
                                       '    room OPENS ON, served -- the design\'s "ticks Earth '
                                       'again" was written\n'
                                       '    when the room opened on Earth alone, and L-404 made '
                                       'that a setting.\n'
                                       '  - **Framing, Tony\'s ruling of 2026-10-02: "B but with a '
                                       'buffer of\n'
                                       '    20%".** The room frames on how far each body is from '
                                       'the Sun now,\n'
                                       '    not on its whole orbit (design 4.1 and 4.2): the '
                                       'farthest body\n'
                                       '    ticked, times 1.2. The opening view and Home follow '
                                       'the same rule; GO\n'
                                       '    frames the one body the same way. Part of a stretched '
                                       'orbit may run\n'
                                       '    past the box and is cut off at its edge (Plotly 2.35.2 '
                                       'clips a 3D\n'
                                       '    scene to its axis ranges, read from the bundle) until '
                                       'the visitor\n'
                                       "    zooms out. Today's frames, whole orbit at 10% against "
                                       'now at 20%:\n'
                                       '    Pluto 49.6 to 42.7 AU and Apophis 1.18 to 1.02 AU, '
                                       'tighter; every\n'
                                       '    planet slightly wider, by 2% (Saturn) to 9% (Mercury, '
                                       'Venus). The Sun and Earth rooms keep\n'
                                       '    framing whole shapes at 10%. In step 3a ticking framed '
                                       'whole orbits.\n'
                                       "    The choice was put to Tony with today's numbers, after "
                                       'Claude\n'
                                       '    corrected its own first summary: the two framings '
                                       'differ not only\n'
                                       '    for stretched orbits but wherever a body sits toward a '
                                       'corner of the\n'
                                       '    square box -- Jupiter, by about a third, under the '
                                       'tightest rule,\n'
                                       '    which was offered and ruled out.\n'
                                       '  - **Five calls Claude made inside the build, confirmed '
                                       'by Tony on\n'
                                       '    2026-10-02 ("Confirmed as recommended"):** a tap on a '
                                       'body in the\n'
                                       '    picture does not move the view; tapping a name does '
                                       'not move the\n'
                                       '    view, only GO does; Home with nothing ticked puts back '
                                       "the room's\n"
                                       "    served opening, not Earth alone; the Sun's row has no "
                                       'GO; the\n'
                                       "    room's opening frame follows the 20% rule alone, "
                                       "without step 3a's\n"
                                       '    1.2 AU minimum (Mercury alone would open at 0.56 AU).\n'
                                       "  - The info panel's two paragraphs rewritten to say this. "
                                       'Tony to\n'
                                       '    approve the words before Mode 5 (interactive-exhibit, '
                                       'hover text is\n'
                                       '    written for the visitor).\n'
                                       '  - Logic in gallery/solar_system_drawer.js (L-338), '
                                       'checked by\n'
                                       '    documentation/smoke_solar_system_drawer.js, a new '
                                       'gating checker\n'
                                       '    whose self-test breaks it three ways; the file joins '
                                       'SERVED_FILES.\n'
                                       '  - Tested here [sandbox]: the page booted in jsdom with a '
                                       'stand-in\n'
                                       "    Plotly on the REAL driver payload (the room's driver "
                                       'run in CPython\n'
                                       '    on the served cache): 53 checks walking the drawer, '
                                       'failing as\n'
                                       '    expected on the unpatched page and on a broken frame '
                                       'rule. The Sun\n'
                                       '    and Earth rooms driven the same way before and after: '
                                       'identical\n'
                                       '    rows, ticks, focus, All / none and Home through every '
                                       'row. The walk\n'
                                       "    checks each frame against the body's distance worked "
                                       'out on its own,\n'
                                       '    and fails 7 ways if the room frames whole orbits '
                                       'again. All\n'
                                       '    gating checkers pass but Pole of date, which needs '
                                       'pyerfa the\n'
                                       "    sandbox lacks. No WebGL and no phone: Tony's Mode 5 is "
                                       'the test.\n'
                                       "- **2026-10-01, the front door decided, and the panel's "
                                       'words.**',
                                       'L-363 step 3b note')],
           'PROJECT_INSTRUCTIONS.md': [('Tony Quintanilla, PE | Claude | v3.76 | October 1, 2026',
                                        'Tony Quintanilla, PE | Claude | v3.77 | October 2, 2026',
                                        'header v3.77'),
                                       ('Cut from feb5e369 at '
                                        'https://github.com/tonylquintanilla/palomas_orrery',
                                        'Cut from b3cfc780 at '
                                        'https://github.com/tonylquintanilla/palomas_orrery',
                                        'cut from b3cfc780'),
                                       ('v3.76 (October 1, 2026): No rule changed in this '
                                        'document. TWO',
                                        'v3.77 (October 2, 2026): No rule changed in this '
                                        'document. TWO\n'
                                        'skill bumps, one version each, for one session (L-405):\n'
                                        'interactive-exhibit 1.8 -> 1.9 and '
                                        'ledger-and-session-records 1.13 ->\n'
                                        "1.14. THE SKILLS CATCH UP WITH THE SESSION'S TWO BUILDS.\n"
                                        '\n'
                                        'WHAT PROMPTED IT. The session made the Exhibit Store '
                                        'Editor list every\n'
                                        "room (L-404) and built the Solar System room's drawer "
                                        '(L-363 step 3b).\n'
                                        'Tony then asked to sort what the session did into method '
                                        'already in\n'
                                        'the skills, method that needed a skill, and drawing '
                                        'decisions and\n'
                                        'judgement -- and, the review done, to "take care of the '
                                        'skills now and\n'
                                        'the numbers in the next session."\n'
                                        '\n'
                                        'WHAT THE SKILLS NOW SAY. interactive-exhibit corrects its '
                                        'sentence that\n'
                                        'every reader of objects_config.json ignores the "rooms" '
                                        'section; says\n'
                                        'what the store writer may change in a room that is not '
                                        'one body, and\n'
                                        'that the editor lists rooms from both places a room can '
                                        'live; records\n'
                                        "the Solar System room's drawer as the shared drawer with "
                                        'four\n'
                                        "additions, and Tony's framing ruling of 2026-10-02 -- "
                                        'where each body\n'
                                        'is now, plus 20%; and gives step 4 the headless test '
                                        'recipe, now filed\n'
                                        "in the gallery's tools/headless/. "
                                        'ledger-and-session-records gains A\n'
                                        'Wrong Sentence in a Skill: Bump Now, or Carry It. The '
                                        'test is what a\n'
                                        'session would do if it followed the sentence: something '
                                        'wrong means\n'
                                        'correct it now, nothing different means carry it on the '
                                        'ledger to the\n'
                                        'next version.\n'
                                        '\n'
                                        'JUDGEMENT KEPT OUT OF THE SKILLS. Five calls Claude made '
                                        'inside the\n'
                                        'drawer build were put to Tony as his, and he confirmed '
                                        'them. They are\n'
                                        'recorded as his rulings on L-363, not written as method.\n'
                                        '\n'
                                        'THE OBLIGATION TRAVELS. This session loaded 1.8 and 1.13. '
                                        'The next\n'
                                        'session confirms its loaded copies read '
                                        'interactive-exhibit 1.9 and\n'
                                        'ledger-and-session-records 1.14 before any exhibit, '
                                        'ledger, handoff or\n'
                                        'session-record work.\n'
                                        '\n'
                                        'The header stamp and the SHA anchor move with this '
                                        'entry.\n'
                                        '\n'
                                        'Version history: v3.74 moves down to\n'
                                        'documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to '
                                        'keep three\n'
                                        'resident.\n'
                                        '\n'
                                        'v3.76 (October 1, 2026): No rule changed in this '
                                        'document. TWO',
                                        'version history: v3.77 entry'),
                                       ('v3.74 (September 30, 2026): No rule changed in this '
                                        'document. ONE\n'
                                        'skill bump, ledger-and-session-records 1.12 -> 1.13 '
                                        "(L-396). TONY'S\n"
                                        'PAGE: WHERE WE ARE.\n'
                                        '\n'
                                        'WHAT PROMPTED IT. Tony, 2026-09-30: "i struggle to keep '
                                        'the big\n'
                                        "picture. it's the old dilemma of loosing the forest for "
                                        'the trees."\n'
                                        "The master plan's summary and critical path had been "
                                        'tried for that\n'
                                        'and had not really helped: both are written for the work, '
                                        'and both\n'
                                        'move only at design builds. He asked for one running '
                                        'document he can\n'
                                        'read at the end of every turn and every session, '
                                        'practical both to\n'
                                        'write and to read. Then he asked for the parts changed '
                                        'this session\n'
                                        'and the immediate next steps to be marked, because '
                                        '"attention is a\n'
                                        'human limitation", and for bullets in place of '
                                        'paragraphs.\n'
                                        '\n'
                                        'WHAT THE SKILL NOW SAYS. The Document Stack gains Where '
                                        'We Are:\n'
                                        'documentation/WHERE_WE_ARE.md, one file rewritten in '
                                        'place and\n'
                                        "updated inside every session's ledger patch. It has a "
                                        'fixed shape: a\n'
                                        'Read This First box, the road from start to goal, right '
                                        'now, the next\n'
                                        "three steps, and what waits on Tony. This session's "
                                        'changes are\n'
                                        'marked, the must-reads are in italics, and the marks are '
                                        'cleared at\n'
                                        'each update. And a turn that changes the picture ends '
                                        'with two or\n'
                                        'three bullets under "Where this leaves us". Nothing '
                                        'checks the page\n'
                                        'yet; the candidate check is recorded on L-396.\n'
                                        '\n'
                                        'THE SAME SESSION (2026-09-29 and 30) brought three '
                                        'strands of work\n'
                                        "together and recorded Tony's order of work: the Solar "
                                        "System room's\n"
                                        "second half first, then the Sun's numbers, then the room "
                                        'becomes the\n'
                                        "website's home page. After that, the orrery's other "
                                        'objects come to\n'
                                        'the website from its own object list, checked against JPL '
                                        'Horizons\n'
                                        '(L-363, L-395; master plan v35).\n'
                                        '\n'
                                        'THE OBLIGATION TRAVELS. This session loaded 1.12. The '
                                        'next session\n'
                                        'confirms its loaded copy reads 1.13 before any ledger, '
                                        'handoff or\n'
                                        'session-record work -- which every session does at its '
                                        'end.\n'
                                        '\n'
                                        'The header stamp and the SHA anchor move with this '
                                        'entry.\n'
                                        '\n'
                                        'Version history: v3.71 moves down to\n'
                                        'documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to '
                                        'keep three\n'
                                        'resident.\n'
                                        '\n',
                                        '',
                                        'version history: v3.74 moved down')],
           'documentation/PROJECT_INSTRUCTIONS_HISTORY.md': [('================================================================\n'
                                                              'PART 2 -- LESSONS REMOVED FROM THE '
                                                              'PROTOCOL AT v3.37',
                                                              'v3.74 (September 30, 2026): No rule '
                                                              'changed in this document. ONE\n'
                                                              'skill bump, '
                                                              'ledger-and-session-records 1.12 -> '
                                                              "1.13 (L-396). TONY'S\n"
                                                              'PAGE: WHERE WE ARE.\n'
                                                              '\n'
                                                              'WHAT PROMPTED IT. Tony, 2026-09-30: '
                                                              '"i struggle to keep the big\n'
                                                              "picture. it's the old dilemma of "
                                                              'loosing the forest for the trees."\n'
                                                              "The master plan's summary and "
                                                              'critical path had been tried for '
                                                              'that\n'
                                                              'and had not really helped: both are '
                                                              'written for the work, and both\n'
                                                              'move only at design builds. He '
                                                              'asked for one running document he '
                                                              'can\n'
                                                              'read at the end of every turn and '
                                                              'every session, practical both to\n'
                                                              'write and to read. Then he asked '
                                                              'for the parts changed this session\n'
                                                              'and the immediate next steps to be '
                                                              'marked, because "attention is a\n'
                                                              'human limitation", and for bullets '
                                                              'in place of paragraphs.\n'
                                                              '\n'
                                                              'WHAT THE SKILL NOW SAYS. The '
                                                              'Document Stack gains Where We Are:\n'
                                                              'documentation/WHERE_WE_ARE.md, one '
                                                              'file rewritten in place and\n'
                                                              "updated inside every session's "
                                                              'ledger patch. It has a fixed shape: '
                                                              'a\n'
                                                              'Read This First box, the road from '
                                                              'start to goal, right now, the next\n'
                                                              'three steps, and what waits on '
                                                              "Tony. This session's changes are\n"
                                                              'marked, the must-reads are in '
                                                              'italics, and the marks are cleared '
                                                              'at\n'
                                                              'each update. And a turn that '
                                                              'changes the picture ends with two '
                                                              'or\n'
                                                              'three bullets under "Where this '
                                                              'leaves us". Nothing checks the '
                                                              'page\n'
                                                              'yet; the candidate check is '
                                                              'recorded on L-396.\n'
                                                              '\n'
                                                              'THE SAME SESSION (2026-09-29 and '
                                                              '30) brought three strands of work\n'
                                                              "together and recorded Tony's order "
                                                              "of work: the Solar System room's\n"
                                                              "second half first, then the Sun's "
                                                              'numbers, then the room becomes the\n'
                                                              "website's home page. After that, "
                                                              "the orrery's other objects come to\n"
                                                              'the website from its own object '
                                                              'list, checked against JPL Horizons\n'
                                                              '(L-363, L-395; master plan v35).\n'
                                                              '\n'
                                                              'THE OBLIGATION TRAVELS. This '
                                                              'session loaded 1.12. The next '
                                                              'session\n'
                                                              'confirms its loaded copy reads 1.13 '
                                                              'before any ledger, handoff or\n'
                                                              'session-record work -- which every '
                                                              'session does at its end.\n'
                                                              '\n'
                                                              'The header stamp and the SHA anchor '
                                                              'move with this entry.\n'
                                                              '\n'
                                                              'Version history: v3.71 moves down '
                                                              'to\n'
                                                              'documentation/PROJECT_INSTRUCTIONS_HISTORY.md '
                                                              'PART 1 to keep three\n'
                                                              'resident.\n'
                                                              '\n'
                                                              '(Moved down from the resident '
                                                              'protocol on 2026-10-02 when\n'
                                                              'v3.77 made a fourth entry.)\n'
                                                              '\n'
                                                              '================================================================\n'
                                                              'PART 2 -- LESSONS REMOVED FROM THE '
                                                              'PROTOCOL AT v3.37',
                                                              'PART 1: v3.74 received')],
           'skills/interactive-exhibit/SKILL.md': [('Skill version: 1.8 | 2026-10-01, with '
                                                    "Anthropic's Claude Opus 5.5, from\n"
                                                    'orrery @ feb5e369 and gallery @ 43993b49.',
                                                    'Skill version: 1.9 | 2026-10-02, with '
                                                    "Anthropic's Claude Opus 5.5, from\n"
                                                    'orrery @ b3cfc780 and gallery @ cfc53490, '
                                                    'with gallery patches\n'
                                                    'patch_L404_1_rooms_in_store_editor_20261001.py '
                                                    'and\n'
                                                    'patch_L363_9_room_step3b_drawer_20261002.py. '
                                                    'v1.9 (L-405) writes down\n'
                                                    'what two builds of one session taught, sorted '
                                                    "on Tony's review of\n"
                                                    '2026-10-02 into method rather than judgement. '
                                                    'The sentence saying every\n'
                                                    'reader of data/objects_config.json ignores '
                                                    '"rooms" was wrong and is\n'
                                                    'corrected. The store writer may change a '
                                                    "rooms-section room's `drawn`\n"
                                                    'and `highlight`, and the editor lists rooms '
                                                    'from both places a room can\n'
                                                    "live (L-404). The Solar System room's drawer "
                                                    'is recorded as shared\n'
                                                    "chrome with four additions, with Tony's "
                                                    'framing ruling -- where a body\n'
                                                    'is now, plus 20% (L-363 step 3b). And step 4 '
                                                    'gains the headless recipe:\n'
                                                    "a room's real driver in CPython, the real "
                                                    'page in jsdom with a stand-in\n'
                                                    'Plotly, and the other rooms compared before '
                                                    'and after (tools/headless/).\n'
                                                    "Earlier: 1.8 | 2026-10-01, with Anthropic's "
                                                    'Claude Opus 5.5, from\n'
                                                    'orrery @ feb5e369 and gallery @ 43993b49.',
                                                    'version line 1.8 -> 1.9, with the v1.9 '
                                                    'paragraph'),
                                                   ('change reaches a visitor on the push alone. '
                                                    'The cache builder, the\n'
                                                    'assembler and every check read only '
                                                    '`"objects"` and ignore it -- checked\n'
                                                    'before the section was added, and the reason '
                                                    'it could be added without\n'
                                                    'touching them.\n',
                                                    'change reaches a visitor on the push alone. '
                                                    'The cache builder and the\n'
                                                    'assembler read only `"objects"` and ignore it '
                                                    '-- checked before the\n'
                                                    'section was added, and the reason it could be '
                                                    'added without touching\n'
                                                    'them. Other readers have joined since, so do '
                                                    'not repeat the older claim\n'
                                                    'that EVERY reader ignores it: '
                                                    '`tools/mirror_objects.py` reads its rows\n'
                                                    '(v1.8, L-395), and `tools/store_writer.py`, '
                                                    '`tools/exhibit_store_editor.py`\n'
                                                    'and their two suites read it (v1.9, L-404).\n'
                                                    '\n'
                                                    'WHAT MAY BE EDITED IN A ROOMS-SECTION ROOM '
                                                    "(v1.9, L-404): its arrival's\n"
                                                    '`drawn` and `highlight`, through the store '
                                                    'writer, and nothing else in\n'
                                                    'the section. Each must name a drawer row '
                                                    'other than the Sun, which is\n'
                                                    'the fixed centre and always drawn; the writer '
                                                    'refuses anything else,\n'
                                                    'because the page would warn about it and '
                                                    "highlight nothing. The editor's\n"
                                                    'room list is `store_writer.room_ids()`: the '
                                                    'body rooms by slug, then the\n'
                                                    "section's rooms by key, so a room added in "
                                                    'EITHER place appears with\n'
                                                    'nothing else to change. Until 2026-10-01 the '
                                                    'list read only `objects`,\n'
                                                    'and the Solar System room, built the day '
                                                    'before, could not be chosen at\n'
                                                    "all -- found by Tony at the editor. A row's "
                                                    'own words (`label`, `about`,\n'
                                                    '`source_note`) are not in the allow list; a '
                                                    'change to them comes as a\n'
                                                    'patch, and whether the editor should take '
                                                    "them is Tony's question.\n",
                                                    'rooms section: the wrong sentence corrected; '
                                                    'what is editable there'),
                                                   ('### A shell trace carries its key [CRITICAL]',
                                                    "### The Solar System room's drawer: bodies, "
                                                    'not shells [QUALITY]\n'
                                                    'v1.9, L-363 step 3b. It is the SAME drawer as '
                                                    "the Sun's and Earth's --\n"
                                                    'One chrome, many rooms -- with four things '
                                                    'added for a room whose rows\n'
                                                    'are bodies. A room gets them by handing '
                                                    '`drawer` (its served rows and\n'
                                                    'opening) back from its `compose`; the page '
                                                    'then sets `ssDrawer`, and the\n'
                                                    '`ss*` functions above `buildSunDrawer` do the '
                                                    'work. In the Sun and Earth\n'
                                                    'rooms `ssDrawer` is null and every branch '
                                                    'that asks is skipped. Each\n'
                                                    'decision is made in '
                                                    '`gallery/solar_system_drawer.js`, checked by\n'
                                                    '`documentation/smoke_solar_system_drawer.js` '
                                                    '(a gating checker that\n'
                                                    'breaks the file three ways first); the page '
                                                    'only touches the DOM and\n'
                                                    'Plotly.\n'
                                                    '\n'
                                                    "- **The Sun's row is fixed**: no tick box, no "
                                                    'GO, never unticked by All\n'
                                                    '  / none. It still highlights and opens. The '
                                                    "Sun's trace group is\n"
                                                    "  `center` (the assembler's centre marker), "
                                                    'not its slug.\n'
                                                    '- **A row opens.** Tapping a name highlights '
                                                    'the row and opens it; a\n'
                                                    '  second tap closes it. Ticking a body opens '
                                                    'its row too (Tony,\n'
                                                    '  2026-09-30). An open row links "Enter the '
                                                    '<name> room" where the\n'
                                                    "  row's slug is a key in `EXHIBITS`, and says "
                                                    '"No room or cards yet"\n'
                                                    "  where it is not -- read from the page's own "
                                                    'table, so the next room\n'
                                                    '  lights its row by itself.\n'
                                                    '- **See more / See fewer** for rows served '
                                                    '`see_more`. A ticked row\n'
                                                    '  never hides; the button is not offered when '
                                                    'nothing is behind it.\n'
                                                    '- **Home remembers the tick order**, for the '
                                                    'open tab only: the last\n'
                                                    '  body ticked that is still ticked, at the '
                                                    'opening angle, drawer closed,\n'
                                                    '  falling back through the order. With '
                                                    'nothing ticked it puts back the\n'
                                                    "  room's SERVED opening -- the one time Home "
                                                    'changes what is drawn.\n'
                                                    '- **Selecting moves nothing.** A tap on a '
                                                    'body in the picture\n'
                                                    '  highlights its row and opens its hover; a '
                                                    'name tap highlights and\n'
                                                    '  opens the row. Only GO moves the view. '
                                                    "(These, the Sun's missing GO,\n"
                                                    "  Home's served opening and the opening frame "
                                                    "below were Claude's calls\n"
                                                    '  inside the build; Tony confirmed all five '
                                                    'on 2026-10-02.)\n'
                                                    '- **Rows are found by the group they name** '
                                                    '(`data-k`), never by their\n'
                                                    '  place in the list: opened rows and the See '
                                                    'more button sit between\n'
                                                    '  them. `renderSunDrawer` does this for every '
                                                    'room.\n'
                                                    '\n'
                                                    '**FRAMING, Tony\'s ruling of 2026-10-02** ("B '
                                                    'but with a buffer of\n'
                                                    '20%"): the room frames on how far each body '
                                                    'is from the Sun NOW, not\n'
                                                    'on its whole orbit, and the farthest body '
                                                    'ticked sets the frame. Two\n'
                                                    "parameters on the room's `EXHIBITS` row carry "
                                                    'it, `frameOnPosition:\n'
                                                    'true` and `frameMargin: 1.2`; '
                                                    '`sunGroupRadius` then returns the\n'
                                                    "position marker's distance "
                                                    '(`sunPositionRadius`) and `sunFrameMargin()`\n'
                                                    'the 20%. The opening view, Home and GO follow '
                                                    'the same rule, and the\n'
                                                    'opening has no 1.2 AU minimum. The Sun and '
                                                    'Earth rooms keep framing\n'
                                                    'whole shapes at 10%. Part of a stretched '
                                                    'orbit runs past the box and is\n'
                                                    'CUT OFF at its edge until the visitor zooms '
                                                    'out: gl-plot3d clips each\n'
                                                    'trace to the axis ranges (`clipToBounds`, on '
                                                    'by default, read from the\n'
                                                    'Plotly 2.35.2 bundle). Put to Tony with each '
                                                    "body's numbers, after a\n"
                                                    'first summary that said the two framings '
                                                    'differ only for stretched\n'
                                                    'orbits -- wrong: in a square box they also '
                                                    'differ wherever a body sits\n'
                                                    'toward a corner, by about a third for Jupiter '
                                                    'under the tightest rule.\n'
                                                    '\n'
                                                    '### A shell trace carries its key [CRITICAL]',
                                                    "new rule: the Solar System room's drawer, and "
                                                    'its framing'),
                                                   ('WHAT THE WRITER MAY TOUCH IS AN ALLOW LIST '
                                                    'BUILT BY READING THE CONFIG,\n'
                                                    'not a list of exceptions -- 204 paths at '
                                                    'gallery `d9d7a48f`: a served\n'
                                                    "shell's six words, a belt's parallel words, "
                                                    'and `drawn` and `moon`.',
                                                    'WHAT THE WRITER MAY TOUCH IS AN ALLOW LIST '
                                                    'BUILT BY READING THE CONFIG,\n'
                                                    'not a list of exceptions -- 204 paths at '
                                                    'gallery `d9d7a48f`: a served\n'
                                                    "shell's six words, a belt's parallel words, "
                                                    'and `drawn` and `moon`; and\n'
                                                    "since v1.9 a rooms-section room's `drawn` and "
                                                    '`highlight` (above).',
                                                    'writer allow list: the rooms section joins '
                                                    'it'),
                                                   ('   room, add it to this suite before trusting '
                                                    'its green.\n'
                                                    '5. Push;',
                                                    '   room, add it to this suite before trusting '
                                                    'its green.\n'
                                                    '\n'
                                                    '   **THE HEADLESS RECIPE** (v1.9, L-405; '
                                                    'first used for L-363 step 3b).\n'
                                                    '   The stand-in scene above, made concrete, '
                                                    'in `tools/headless/` in the\n'
                                                    '   gallery repo. Claude-only: Tony never runs '
                                                    'it and the maintenance run\n'
                                                    '   does not. jsdom is not in the gallery; '
                                                    '`npm install jsdom@24` in a\n'
                                                    '   scratch folder and run with '
                                                    '`NODE_PATH=<scratch>/node_modules`.\n'
                                                    '   - `run_room_driver.py <DRIVER> <EPOCH> '
                                                    "<out.json>` runs a room's REAL\n"
                                                    '     driver in plain CPython on the served '
                                                    'cache. The driver is ordinary\n'
                                                    '     Python over `gallery/assembler/`; only '
                                                    'Pyodide is missing.\n'
                                                    '   - `page_harness.js` boots the REAL '
                                                    '`interactive.html` in jsdom with\n'
                                                    '     the real gallery files, that payload, '
                                                    'and a stand-in Plotly that\n'
                                                    '     records restyles and relayouts. It '
                                                    "measures the chrome's MECHANISM\n"
                                                    '     -- rows, ticks, focus, frames, Home -- '
                                                    'and nothing a visitor sees.\n'
                                                    '   - `compare_rooms.js <before> <after> '
                                                    '<room> <payload>`: when SHARED\n'
                                                    '     chrome changes, drive every other room '
                                                    'the same way in the old and\n'
                                                    "     the new copy -- every row's box in turn, "
                                                    'All / none, Home -- and\n'
                                                    '     require the two to be identical. "Both '
                                                    'rooms are Mode 5 targets"\n'
                                                    '     (One chrome, many rooms) still holds; '
                                                    'this makes the first pass\n'
                                                    '     cheap and exact.\n'
                                                    '   - A walk per room '
                                                    '(`walk_solar_system_drawer.js`) checks each '
                                                    'step\n'
                                                    '     against values worked out in the walk '
                                                    "itself, not by the page's own\n"
                                                    '     helpers, and is run once against a '
                                                    'deliberately broken copy to show\n'
                                                    '     it can fail. It fixes its own opening, '
                                                    'so a change to what the room\n'
                                                    '     opens on does not break it.\n'
                                                    "   The page's CDN scripts are refused by the "
                                                    "harness's loader, which\n"
                                                    '   serves the stand-in Plotly instead. Say in '
                                                    'the handoff what was run\n'
                                                    '   this way and that the phone has not seen '
                                                    'it.\n'
                                                    '5. Push;',
                                                    'step 4: the headless recipe'),
                                                   ('its loaded copy reads 1.3 before exhibit '
                                                    'work.',
                                                    'its loaded copy reads 1.3 before exhibit '
                                                    'work. 1.9 was cut in the\n'
                                                    'session that wrote it, which loaded 1.8; the '
                                                    'next session confirms its\n'
                                                    'loaded copy reads 1.9 before exhibit work.',
                                                    'install: 1.9 obligation'),
                                                   ('meta.shell_key and the trace stamp; editing '
                                                    'the served words with store_writer or '
                                                    'exhibit_store_editor; carding an exhibit in '
                                                    'Studio\n'
                                                    '---',
                                                    'meta.shell_key and the trace stamp; editing '
                                                    'the served words with store_writer or '
                                                    "exhibit_store_editor; the Solar System room's "
                                                    "drawer, See more, Home's order and its "
                                                    'framing; testing a room headlessly '
                                                    '(tools/headless); carding an exhibit in '
                                                    'Studio\n'
                                                    '---',
                                                    'fires_when: the body drawer and the headless '
                                                    'recipe')],
           'skills/ledger-and-session-records/SKILL.md': [('Skill version: 1.13 | Cut from '
                                                           'palomas_orrery @ 5db8bbe0 (v1.13),\n'
                                                           'earlier @ 2a7d26b9 (v1.12),',
                                                           'Skill version: 1.14 | Cut from '
                                                           'palomas_orrery @ b3cfc780 (v1.14),\n'
                                                           'earlier @ 5db8bbe0 (v1.13), @ 2a7d26b9 '
                                                           '(v1.12),',
                                                           'version line 1.13 -> 1.14'),
                                                          ('the must-reads in italics. Tony, '
                                                           '2026-09-30: "i struggle to keep the\n'
                                                           "big picture. it's the old dilemma of "
                                                           'loosing the forest for the trees."\n',
                                                           'the must-reads in italics. Tony, '
                                                           '2026-09-30: "i struggle to keep the\n'
                                                           "big picture. it's the old dilemma of "
                                                           'loosing the forest for the trees."\n'
                                                           'v1.14 (L-405; 2026-10-02, with '
                                                           "Anthropic's Claude Opus 5.5) adds A "
                                                           'Wrong\n'
                                                           'Sentence in a Skill: Bump Now, or '
                                                           'Carry It, under the change log. A\n'
                                                           'session had to decide it for itself on '
                                                           "2026-10-01 (L-404); Tony's review\n"
                                                           'of 2026-10-02 sorted it as method, so '
                                                           'the skill answers it now.\n',
                                                           'v1.14 paragraph in the header'),
                                                          ('**Step 3 is the one that stops '
                                                           "firing** (Tony's observation,",
                                                           '**A WRONG SENTENCE IN A SKILL: BUMP '
                                                           'NOW, OR CARRY IT [QUALITY].**\n'
                                                           '(v1.14, L-405.) A skill loads every '
                                                           'session and is followed without\n'
                                                           'being noticed, so the test is what a '
                                                           'session would DO if it followed the\n'
                                                           'wrong sentence as written.\n'
                                                           '\n'
                                                           '- **It would do something wrong** -- '
                                                           'edit the wrong file, skip or trust\n'
                                                           '  the wrong check, write a wrong '
                                                           'number, tell Tony something false.\n'
                                                           '  Correct it in THIS session. If the '
                                                           'session is not otherwise bumping\n'
                                                           '  that skill, this is a bump of its '
                                                           'own: one wrong instruction is\n'
                                                           '  enough to earn one.\n'
                                                           '- **It would do nothing different** -- '
                                                           'the sentence is a description\n'
                                                           '  that has gone out of date, a count '
                                                           'or a list that has grown, a claim\n'
                                                           '  no step depends on. Carry it on a '
                                                           "ledger item for the skill's next\n"
                                                           '  version, name it in the patch output '
                                                           '(The Correction Does Not\n'
                                                           '  Travel), and correct it then. The '
                                                           'ceremony of a bump -- a protocol\n'
                                                           '  entry, a manifest run, a reinstall '
                                                           '-- is not spent on a sentence no\n'
                                                           '  one acts on.\n'
                                                           '- **If the session is already bumping '
                                                           'that skill**, any wrong sentence\n'
                                                           '  in it rides that bump, whichever '
                                                           'kind it is. One Session, One Bump.\n'
                                                           '\n'
                                                           'When it is unclear which of the first '
                                                           'two a sentence is, treat it as\n'
                                                           'the first. The worked case: '
                                                           'interactive-exhibit 1.8 said every '
                                                           'reader of\n'
                                                           '`data/objects_config.json` ignores its '
                                                           '`"rooms"` section. A session\n'
                                                           'following it would at worst have '
                                                           'looked in fewer places for a reader,\n'
                                                           'so on 2026-10-01 it was carried (L-404 '
                                                           'to L-405), and corrected at 1.9.\n'
                                                           '\n'
                                                           '**Step 3 is the one that stops '
                                                           "firing** (Tony's observation,",
                                                           'new rule: a wrong sentence in a skill, '
                                                           'bump now or carry it')]},
 'REPLACE': {'documentation/WHERE_WE_ARE.md': '<!-- Doc-Kind: hand | Where the project is and '
                                              'where it is going, in plain words. One file, '
                                              'rewritten in place; read it at the end of every '
                                              'session. -->\n'
                                              '# Where We Are\n'
                                              '\n'
                                              'Last updated: October 2, 2026\n'
                                              '- Written at orrery b3cfc780 and gallery cfc53490, '
                                              "plus this session's\n"
                                              '  two patches.\n'
                                              '\n'
                                              '> **READ THIS FIRST**\n'
                                              '>\n'
                                              '> **Changed this session:**\n'
                                              '> - The Exhibit Store Editor now lists every room, '
                                              'the Solar System\n'
                                              '>   room included, and can set what it opens on.\n'
                                              "> - The Solar System room's drawer is built: See "
                                              'more, rows that open\n'
                                              '>   with a way into the Sun and Earth rooms, and '
                                              'Home remembering what\n'
                                              '>   you ticked. Not yet on the website.\n'
                                              '> - Your ruling: the room frames where each body is '
                                              'now, plus 20%,\n'
                                              '>   not its whole orbit. You also confirmed five '
                                              'smaller calls I had\n'
                                              '>   made in the build.\n'
                                              '> - The two skills are updated for this work, with '
                                              'a new rule on when\n'
                                              '>   a skill gets a new version.\n'
                                              "> - The last session's two skill reinstalls are "
                                              'confirmed.\n'
                                              '>\n'
                                              '> **Do next:**\n'
                                              '> - *You check the drawer on your phone, then the '
                                              'desktop.*\n'
                                              '>\n'
                                              '> **Needs you now:**\n'
                                              "> - *Read the room's two new info paragraphs and "
                                              'say if they are right.*\n'
                                              '> - *At your machine: two gallery patches, the '
                                              'editor ticks, one orrery\n'
                                              '>   patch, then reinstall two skills and the '
                                              "Project's instructions.\n"
                                              '>   Each patch prints what to do next.*\n'
                                              '\n'
                                              'How to read the marks:\n'
                                              '- *Italic* lines are the must-reads.\n'
                                              '- **>> UPDATED THIS SESSION** beside a heading '
                                              'means that section\n'
                                              '  changed in the latest session.\n'
                                              '- "<< new this session" beside a road stage marks a '
                                              'change to the road.\n'
                                              '- Sections without a mark are as they were.\n'
                                              '- The marks are cleared and reset at every '
                                              "session's update, so they\n"
                                              '  always mean "new since you last read this."\n'
                                              '\n'
                                              '## The goal\n'
                                              '\n'
                                              "- Paloma's Orrery on the web.\n"
                                              '- The website does what the desktop orrery does, in '
                                              'the browser, from\n'
                                              '  data fetched from JPL each night, so a visitor '
                                              'never waits on JPL.\n'
                                              '- Anyone can open it, with nothing to install.\n'
                                              '- Built from the same code and the same checked '
                                              'numbers as the desktop\n'
                                              '  orrery.\n'
                                              '- The one real limit: the browser can show only the '
                                              'dates the saved\n'
                                              '  data covers.\n'
                                              '- Within that range, a visitor will be able to '
                                              'choose a date, and\n'
                                              '  perhaps play time forward.\n'
                                              '\n'
                                              '## The road\n'
                                              '\n'
                                              "  1. [done]   The Sun's room is live on the "
                                              'website.\n'
                                              "  2. [done]   Earth's room is live, with every "
                                              'number traced to its source.\n'
                                              '  3. [done]   The numbers come from one place: the '
                                              'orrery feeds the\n'
                                              '              website, and nothing is typed twice.\n'
                                              '  4. [NOW]    *The Solar System room becomes a '
                                              'second way in: all the\n'
                                              '              planets, a drawer to pick them, and a '
                                              'way into each\n'
                                              "              body's own room.*\n"
                                              "  5. [next]   The Sun's numbers get the same "
                                              "checking Earth's got.\n"
                                              "  6. [next]   The Solar System room's card becomes "
                                              'the top featured\n'
                                              '              card in the lobby. A bare '
                                              'interactive.html link opens\n'
                                              '              the Solar System room, and the '
                                              'Explorer gets its own\n'
                                              '              address.\n'
                                              "  7. [later]  The rest of the orrery's objects come "
                                              'to the website --\n'
                                              '              dwarf planets, asteroids, moons -- '
                                              'through the same\n'
                                              '              connection that now carries the '
                                              "room's eleven bodies,\n"
                                              '              checked against JPL Horizons.\n'
                                              '  8. [later]  Encounters: comets and spacecraft '
                                              'shown at the dates\n'
                                              '              that matter.\n'
                                              '  9. [later]  The planets get their details -- '
                                              'layers, rings, magnetic\n'
                                              '              fields -- Jupiter and Saturn first.\n'
                                              ' 10. [goal]   The website does what the desktop '
                                              'orrery does, from data\n'
                                              '              fetched from JPL each night, with a '
                                              'date to choose and\n'
                                              '              time to play within the range the '
                                              'data covers.\n'
                                              '\n'
                                              '## Right now  **>> UPDATED THIS SESSION**\n'
                                              '\n'
                                              '- The Solar System room shows the Sun, all eight '
                                              'planets, Pluto and\n'
                                              '  the asteroid Apophis, where they are when you '
                                              'open it.\n'
                                              '- It opens on Earth alone until you tick more in '
                                              'the editor.\n'
                                              "- The drawer's new behaviours are built and tested "
                                              'here, not yet on\n'
                                              "  the website: See more, rows that open, the Sun's "
                                              'row that cannot be\n'
                                              '  unticked, a tap on a body finding its row, and '
                                              'Home remembering.\n'
                                              '- The room will frame where each body is now, plus '
                                              "20%. Pluto's orbit\n"
                                              '  runs past the edge until you zoom out.\n'
                                              "- Each body's info panel shows a description and a "
                                              'NASA link.\n'
                                              "- Those words and links come from the orrery's own "
                                              'object list. The\n'
                                              '  website keeps copies, written by a tool, and a '
                                              'check fails if anyone\n'
                                              '  edits them by hand.\n'
                                              '- The editor can set what any room opens on. It '
                                              'cannot yet change the\n'
                                              "  words on the Solar System room's rows, such as "
                                              "Pluto's sentence.\n"
                                              "- The rest of the orrery's objects are not "
                                              'connected yet.\n'
                                              '\n'
                                              '## The next three steps  **>> UPDATED THIS '
                                              'SESSION**\n'
                                              '\n'
                                              '1. *You check the drawer on your phone, then the '
                                              'desktop.*\n'
                                              '   - Tick and untick bodies, open rows, See more, '
                                              'Enter the Sun room,\n'
                                              '     tap a body in the picture, and Home.\n'
                                              '2. Whatever your phone shows gets fixed.\n'
                                              "3. The Sun's numbers get the same checking Earth's "
                                              'got.\n'
                                              '\n'
                                              '## Waiting on you  **>> UPDATED THIS SESSION**\n'
                                              '\n'
                                              'Now:\n'
                                              "- *The room's two new info paragraphs: right, or "
                                              'reword?*\n'
                                              '- *Gallery: run the two patches, in either order. '
                                              'Then open the editor,\n'
                                              '  pick solar-system, tick Mercury, Venus and Mars, '
                                              'Save. Then the\n'
                                              '  maintenance run, commit and push.*\n'
                                              '  - Nothing needs a cache rebuild.\n'
                                              '- *Orrery: run the skills-and-ledger patch, then '
                                              'the maintenance run,\n'
                                              '  commit and push. Then reinstall '
                                              'interactive-exhibit and\n'
                                              '  ledger-and-session-records in Settings > Skills, '
                                              'and replace the\n'
                                              "  Project's instructions with the new "
                                              'PROJECT_INSTRUCTIONS.md.*\n'
                                              '\n'
                                              'At the next design talk:\n'
                                              '- Nothing new.\n'
                                              '\n'
                                              'Not urgent:\n'
                                              '- Choosing a date, and animation, your idea of '
                                              'October 1.\n'
                                              '  - The range would follow only the bodies you '
                                              'tick.\n'
                                              '  - Talked through once the drawer is built.\n'
                                              "- The full check of the orrery's object list "
                                              'against JPL Horizons.\n'
                                              '  - Its first run lists what disagrees; simple '
                                              'errors get fixed and\n'
                                              '    listed, the rest come to you.\n'
                                              '- Whether the editor should also edit the words on '
                                              'the Solar System\n'
                                              "  room's rows, such as Pluto's sentence.\n"
                                              '  - Today a change to them comes as a patch from a '
                                              'session.\n'
                                              '\n'
                                              '## Where the details are  **>> UPDATED THIS '
                                              'SESSION**\n'
                                              '\n'
                                              '- Every item, done and open: '
                                              '`LEDGER_CONSOLIDATED.md`\n'
                                              '  - This session: L-404, L-405 and L-363.\n'
                                              '- The reasoning behind the order:\n'
                                              '  '
                                              '`documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`\n'
                                              '- The latest session record: L-404 and the newest '
                                              'note on L-363, in the\n'
                                              '  ledger. This session wrote no separate '
                                              'handoff.\n'}}


def fingerprint(path, raw):
    """The content, line endings aside. For the ledger and the protocol,
    the content OUTSIDE the zone a generator rewrites (ledger_index.py's
    index; skills_index.py's manifest)."""
    lf = raw.replace(b"\r\n", b"\n")
    if path == "LEDGER_CONSOLIDATED.md":
        a = lf.index(b"<!-- INDEX:START")
        b = lf.index(b"<!-- INDEX:END -->") + len(b"<!-- INDEX:END -->")
        lf = lf[:a] + lf[b:]
    if path == "PROJECT_INSTRUCTIONS.md":
        a = lf.index(b"<!-- SKILL-MANIFEST:START")
        b = lf.index(b"<!-- SKILL-MANIFEST:END -->") + len(b"<!-- SKILL-MANIFEST:END -->")
        lf = lf[:a] + lf[b:]
    return hashlib.md5(lf).hexdigest()


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the ORRERY repo ROOT, next to "
                         "palomas_orrery.py -- not from documentation/. "
                         "NOTHING was written.")
    if not os.path.isfile("palomas_orrery.py"):
        raise SystemExit("ERROR: palomas_orrery.py is not here, so this is "
                         "not the orrery root. NOTHING was written.")
    raws = {}
    for path in list(SPEC['EDITS']) + list(SPEC['REPLACE']):
        with open(path, "rb") as handle:
            raws[path] = handle.read()
        got = fingerprint(path, raws[path])
        if got != SPEC['BASE'][path]:
            raise SystemExit(
                "ERROR: %s is not the file this patch was built against.\n"
                "       expected %s, found %s.\n"
                "       (Line endings are excluded, so they are not the cause.)\n"
                "       NOTHING was written. Undo is Discard Changes in\n"
                "       GitHub Desktop." % (path, SPEC['BASE'][path], got))

    results = []
    for path, edits in sorted(SPEC['EDITS'].items()):
        raw = raws[path]
        nl = "\r\n" if raw.count(b"\r\n") > 0 else "\n"
        text = raw.decode("utf-8")
        before = sum(1 for ch in text if ord(ch) > 127)
        done = []
        for old, new, label in edits:
            o = old.replace("\n", nl)
            n = new.replace("\n", nl)
            count = text.count(o)
            if count != 1:
                raise SystemExit("ANCHOR FAIL (%s): expected 1 match in %s, "
                                 "found %d. NOTHING was written."
                                 % (label, path, count))
            text = text.replace(o, n)
            done.append(label)
        if sum(1 for ch in text if ord(ch) > 127) > before:
            raise SystemExit("ERROR: %s would hold new non-ASCII text. "
                             "NOTHING was written." % path)
        results.append((path, text.encode("utf-8"), done))
    for path, content in sorted(SPEC['REPLACE'].items()):
        nl = "\r\n" if raws[path].count(b"\r\n") > 0 else "\n"
        results.append((path, content.replace("\n", nl).encode("ascii"),
                        ["rewritten"]))

    for path, data, done in results:
        with open(path, "wb") as handle:
            handle.write(data)
        for label in done:
            print("ok  %-34s %s" % (path, label))

    print("")
    print("Stamps updated: interactive-exhibit 1.9, ledger-and-session-records")
    print("1.14, the protocol's header (v3.77, cut from b3cfc780), the")
    print("ledger's header, Where We Are's date.")
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    print("  1. python orrery_maintenance_run.py -- it rebuilds the ledger's")
    print("     index and the protocol's skill manifest (1.8 -> 1.9,")
    print("     1.13 -> 1.14).")
    print("  2. Move this script into documentation/; commit and push.")
    print("  3. Reinstall interactive-exhibit and ledger-and-session-records")
    print("     from skills/ in Settings > Skills.")
    print("  4. Replace the Project's instructions in claude.ai with the new")
    print("     PROJECT_INSTRUCTIONS.md.")


if __name__ == "__main__":
    main()
