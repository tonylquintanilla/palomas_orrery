"""
patch_L544_2_session_close.py -- the close of the coordinating session
of Nov 22 and 23, 2026 (the L4 and L5 tie; three decisions).

Built on b0eedeab at https://github.com/tonylquintanilla/palomas_orrery
(branch main), with gallery 326863a6 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io read for
its swap log and night record. Written by the coordinating session
(Claude Fable 5.2) under safe-file-editing 1.15 and
ledger-and-session-records 1.23, the copies this session loaded.

Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\

RUN COMMAND
    This file is in the orrery folder (palomas_orrery_for_github). Open
    it in VS Code and click Run:

        python patch_L544_2_session_close.py

    Success: one "ok" line per edit, "patch applied", "wrote" for the
    new prompt file, then two tools, each printing "ok": ledger_index.py
    and doc_index.py --caps.
    Failure: an "ERROR:" or "ANCHOR FAIL" line, and NOTHING is written.
    Undo after a success: Discard Changes in GitHub Desktop.
    Once it has run, move it to the documentation folder.

WHAT IT CHANGES (no code, no skill, no protocol)
    LEDGER_CONSOLIDATED.md
        L-544 (L4 and L5 tie): built, proved, pushed at gallery
        326863a6, Tony's phone look; DONE.
        L-533 (ESCAPADE): the last 7 days of a path keeps its own
        build, after L-538, in Tony's words.
        L-543 (green on your computer, red on GitHub): ruled; a small
        build left.
        L-545 (checks that wait to be remembered): ruled, the walks at
        night on GitHub only; the recorded scene goes to L-551.
        L-548 (a missing id_type): method, nothing guesses; its patch.
        L-550 (a website check's dashboard button): DONE, with the
        check of the five skills of v3.145.
        New: L-551 (no saved scenes) and L-552 (the kind of body).
    documentation/WHERE_WE_ARE.md, above the marker only: the header,
        the three "Changed" lines, "Do next", one "Needs you now" line,
        the road's lines d and b, Settled, Signals, Waiting on you,
        the design-talk list, Where the details are.
    documentation/PROMPT_coordinator_start_20261123_1.md: new, the next
        coordinating session's starting prompt.

Permanent: the records. This script is one-shot.

Written November 23, 2026 with Anthropic's Claude Fable 5.2.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

EDITS = [('LEDGER_CONSOLIDATED.md',
  '<!-- L:544 status:OPEN upd:2026-11-22 section:A flag: rice: -->',
  '<!-- L:544 status:DONE upd:2026-11-23 section:A flag: rice: -->'),
 ('LEDGER_CONSOLIDATED.md',
  "**Gap:** a tie-break in the drawer's order where two distances agree to\n"
  'the digits a box prints (by name is the plain choice), in the page and\n'
  "in the gallery editor's tree, which lists the same order; then both\n"
  'walks green at every minute. Method, not a ruling. Small; a session\n'
  'that changes the page runs both walks (L-545).\n',
  '**Note:** (2026-11-22, the coordinating session, Claude Fable 5.2)\n'
  'BUILT by `patch_L544_1_tie_break.py`, pushed at gallery 326863a6. Two\n'
  'children of a body whose distances differ by less than half a\n'
  'kilometre, the finest a text box prints (`TIE_KM`, held equal to\n'
  '`FINEST_KM`), are listed by name (`settleTies`, in\n'
  '`gallery/drawer_order.js`). The page set this order in TWO places: the\n'
  "root's fold when the room opens, and the planner once Earth's fold is\n"
  "drawn with its shells; one rule serves both. The gallery editor's tree\n"
  "needed no change: it lists a body's children in the config's order, L4\n"
  'then L5, never by distance, so the Gap\'s "which lists the same order"\n'
  'was wrong.\n'
  '- PROOF, on clean clones of e6af10ea, untouched and patched. Drawer\n'
  '  walk at 04:10 UTC Nov 23 (L5 the nearer): 367 of 368 before, 368 of\n'
  '  368 after; at 06:01 UTC (L4 the nearer): 368 of 368 after.\n'
  '  Scene-moment walk: 12 of 13 before, 13 of 13 after. Of the root\n'
  "  drawer's 133 rows, the only two that changed places were L4 and L5.\n"
  '  The Drawer order row gained a worked case with the two real\n'
  "  distances and a fourth planted fault. The gallery run's night pass\n"
  '  gave every row the same verdict on both copies; nine rows cannot run\n'
  "  in a session's sandbox and failed alike on both (the three pulls,\n"
  '  the two mirrors, Cache builder suite, Pole of date and its ERFA\n'
  '  check, Scene cards). No new row, so no dashboard button.\n'
  '- Tony\'s phone look, Earth\'s fold, L4 above L5: "-- yes"\n'
  '  (`documentation/WHERE_WE_ARE_11-22-26_2226_run_record.md`).\n'
  '- No website night had run on the new page when this was written\n'
  "  (Nov 23, 15:00 UTC). The next session reads the night's Drawer order\n"
  '  row for "self-test red four times".\n'
  "**Gap:** none. The walks' place in the night is L-545's.\n"),
 ('LEDGER_CONSOLIDATED.md',
  '<!-- L:533 status:OPEN upd:2026-11-21 section:A flag: rice: -->',
  '<!-- L:533 status:OPEN upd:2026-11-23 section:A flag: rice: -->'),
 ('LEDGER_CONSOLIDATED.md',
  "Nov 20). The box's last day: its build, as ruled Nov 19. The loops near L2, with\n",
  "Nov 20). The box's last day: its build, as ruled Nov 19, a build of\n"
  "its own straight after L-538 (the orbiters' printed error), not a part\n"
  'of it (Tony, 2026-11-22, 21:58, asked which: "Keep its own build"). The loops near L2, with\n'),
 ('LEDGER_CONSOLIDATED.md',
  '<!-- L:543 status:OPEN upd:2026-11-21 section:A flag: rice: -->',
  '<!-- L:543 status:OPEN upd:2026-11-23 section:A flag: rice: -->'),
 ('LEDGER_CONSOLIDATED.md',
  "**Gap:** Tony's ruling: whether the gallery run is read from a push copy\n"
  'before every website push. If yes: the copy script becomes a tool in\n'
  '`tools/`, the run gains a way to do it in one step, and the rule goes\n'
  'into the skill that covers testing a room.\n',
  '**Note:** (2026-11-22, the coordinating session, Claude Fable 5.2)\n'
  'RULED. Tony, 22:46, on "no, with the script added": "confirmed as\n'
  'recommended." He runs no push-copy check before his own website\n'
  'pushes; the night catches a fault of this kind in one of his. A\n'
  'session that changes the page already tests on a push copy\n'
  '(interactive-exhibit 1.45, Phone first). The reasons given him: most\n'
  "website pushes carry a session's work; a step to remember before every\n"
  'push is the weak kind of check; a red night writes nothing.\n'
  '**Gap:** a small build in the website: the copy script becomes a tool\n'
  "in `tools/`, so a Code session working in Tony's folder makes the push\n"
  'copy in one step. No dashboard button, no step for Tony.\n'),
 ('LEDGER_CONSOLIDATED.md',
  '<!-- L:545 status:OPEN upd:2026-11-22 section:A flag: rice: -->',
  '<!-- L:545 status:OPEN upd:2026-11-23 section:A flag: rice: -->'),
 ('LEDGER_CONSOLIDATED.md',
  '**Gap:** the skill text is written (interactive-exhibit 1.45, Phone\n'
  "first; v3.145, 2026-11-22), the session's half only. Two\n"
  'rulings for Tony: whether the walks join the gallery run, which means\n'
  "the website keeps jsdom and the night's runner installs it; and when the\n"
  'recorded scene is re-recorded (at every cache build, or by a check that\n'
  'goes red when it is older than the page).\n',
  '**Note:** (2026-11-22, the coordinating session, Claude Fable 5.2)\n'
  'RULED, both.\n'
  "- THE WALKS. Tony, 22:54, of three choices (a session's job only; at\n"
  '  night on GitHub only; everywhere, the website keeping the library):\n'
  '  "B". The night on GitHub installs jsdom at its fixed version in a\n'
  '  scratch folder and runs both walks; a failed walk makes the night\n'
  "  red; nothing is added to Tony's computer or to the website's files.\n"
  "  The night's workflow file was not read when he ruled, so the build\n"
  '  is not sized.\n'
  '- THE RECORDED SCENE is not re-recorded at all: L-551 (no saved\n'
  "  scenes), opened from Tony's answer. Ten checks read\n"
  '  `payload_earth_scene.json` on Nov 22, not six.\n'
  '**Gap:** the build of the walks at night, after step 3 of L-522\n'
  "(document caps); interactive-exhibit's rule on the walks then says the\n"
  'night runs them.\n'),
 ('LEDGER_CONSOLIDATED.md',
  '<!-- L:548 status:OPEN upd:2026-11-22 section:A flag: rice: -->',
  '<!-- L:548 status:OPEN upd:2026-11-23 section:A flag: rice: -->'),
 ('LEDGER_CONSOLIDATED.md',
  '**Gap:** a ruling: one default in every reader, or the list writing\n'
  'id_type on every entry; then a patch.\n',
  '**Note:** (2026-11-23, the coordinating session, Claude Fable 5.2)\n'
  "METHOD, on Tony's word. Neither default is safe: read as a small body,\n"
  "Pluto's 999 is the asteroid Zachia; read as a major body, an asteroid\n"
  'numbered 499 would be Mars. So nothing guesses. Every entry writes\n'
  'id_type, the four named above included; a reader that finds none\n'
  "leaves that one object out and names it; the night's check of every\n"
  'entry (L-539) fails on an entry without it. Tony, Nov 23, 08:28:\n'
  '"shouldn\'t we specify what kind of body it is? the objects list\n'
  'already has a field for that. that would disambiguate the id"; and at\n'
  '08:54, on this patch now and his idea to a design talk: "i\'ll follow\n'
  'your lead on this." His idea is L-552 (the kind of body).\n'
  '**Gap:** the patch, in the orrery: four lines in\n'
  '`celestial_objects.py`, the readers (`palomas_orrery.py`, the\n'
  "pre-fetch's two lines and the position fetch's two; `period_fetch.py`)\n"
  'and the check. All five consumers of position data are mapped first\n'
  "(the protocol's Check All Parallel Pipelines); `id_type` is on 68\n"
  'lines of `palomas_orrery.py`. Its rule goes into\n'
  'horizons-orbital-mechanics, so it follows step 3 of L-522 (document\n'
  'caps).\n'),
 ('LEDGER_CONSOLIDATED.md',
  '<!-- L:550 status:OPEN upd:2026-11-22 section:A flag: rice: -->',
  '<!-- L:550 status:DONE upd:2026-11-23 section:A flag: rice: -->'),
 ('LEDGER_CONSOLIDATED.md',
  '**Gap:** none of its own; it closes at the next close after a session\n'
  'has loaded interactive-exhibit 1.45 from the account.\n',
  '**Note:** (2026-11-22, the coordinating session, Claude Fable 5.2)\n'
  'interactive-exhibit loaded from the account and read whole; its\n'
  "version line reads 1.45, the manifest's. THE FIVE SKILLS OF v3.145,\n"
  "checked the same evening: the account's copies read 1.20, 1.21, 1.5,\n"
  '1.45 and 1.15. Two were loaded and read whole (interactive-exhibit,\n'
  'safe-file-editing); three were read at their version line only\n'
  '(horizons-orbital-mechanics, gallery-cache-builder,\n'
  "gallery-assembler). Four are byte for byte the repository's at\n"
  "675b1cfe; gallery-cache-builder's differs by one line break in its\n"
  "header's description, and no word.\n"
  '**Gap:** none. Closed.\n'),
 ('LEDGER_CONSOLIDATED.md',
  "#### [L-550] A website check added by a website session leaves the orrery's dashboard check red "
  '(method; for the skills bump)\n',
  "#### [L-551] No saved scenes: the gallery run makes every room's scene fresh at each run, and "
  'the saved copies go (gallery; ruled Nov 22, a list first)\n'
  '<!-- L:551 status:OPEN upd:2026-11-23 section:A flag: rice: -->\n'
  '- **Opened 2026-11-23** by the coordinating session (Claude Fable 5.2),\n'
  "  from L-545's second question. The session had proposed a fingerprint\n"
  '  on the saved Earth scene. Tony, Nov 22, 23:25: "wait, the earth room\n'
  '  is only the first of many. every planet will have one. then every\n'
  '  moon with rows. dwarf planets, etc. we need a method that will handle\n'
  '  all of them. how is the sun\'s room handled?"\n'
  "- HOW THE SUN'S IS HANDLED: nothing is saved. Each check builds the\n"
  "  Sun's room at every run from `data/objects_config.json` and the\n"
  "  page's own renderers. Earth's room has three things the page's\n"
  "  Python works out for a moment (the Sun's direction, the Moon's arc,\n"
  '  the pole of date), and a check cannot run that Python in a browser,\n'
  '  so its result was saved.\n'
  '- THREE SAVED COPIES at gallery 326863a6, in `documentation/`.\n'
  '  `payload_earth_scene.json`, read by ten checks: smoke_source_list,\n'
  '  smoke_arrival, smoke_typed_numbers, smoke_display_figures,\n'
  '  smoke_label_words, smoke_earth_geometry, smoke_drawer_order,\n'
  '  smoke_typed_facts, smoke_drawn_ends, smoke_hover_budget.\n'
  '  `payload_jupiter_saturn.json`, read by smoke_features, smoke_framing\n'
  '  and smoke_hover_budget. `payload_earth.json`, an older Earth copy,\n'
  '  read by smoke_features, smoke_hover_budget and two walks,\n'
  '  walk_drawer_order and walk_shell_reset. The last two copies carry no\n'
  '  date.\n'
  '- THE METHOD. Tony, Nov 22, 23:30: "Yes and we should remove obsolete\n'
  '  saved files." No saved copies. The page\'s Python for a room runs in\n'
  '  plain Python outside the browser (`tools/headless/run_room_driver.py`,\n'
  "  the standard library only; the Solar System room's 430 traces in 0.3\n"
  "  s on Nov 23). The gallery run makes each room's scene at the start of\n"
  "  every run, from the page's own code and the served data, and hands it\n"
  '  to the checks. A new planet or moon needs no new file; the run is the\n'
  "  same on Tony's computer and on GitHub; at night the checks read the\n"
  "  scene made from that night's data.\n"
  '**Gap:** FIRST A LIST, no code: each check and walk, which copy it\n'
  'reads, and whether it holds numbers fixed to that copy (those work\n'
  'their numbers out from the fresh scene instead). The list sizes the\n'
  'build. Then the build, after step 3 of L-522 (document caps): the\n'
  'three copies and `tools/record_earth_scene.py`, whose header still\n'
  'says four checks, are removed in it. Not known: which moment a fresh\n'
  'scene is made at, and whether one moment is enough.\n'
  '**Ref:** L-545 (checks that wait to be remembered); L-379 (the\n'
  'recorder); L-543; L-509 (obsolete code).\n'
  '\n'
  '#### [L-552] The kind of body: each entry says what it is, and how JPL is asked follows from it '
  "(orrery; Tony's idea, for a design talk)\n"
  '<!-- L:552 status:OPEN upd:2026-11-23 section:A flag: rice: -->\n'
  '- **Opened 2026-11-23** by the coordinating session (Claude Fable 5.2),\n'
  '  from Tony\'s question on L-548 (a missing id_type), 08:28: "shouldn\'t\n'
  '  we specify what kind of body it is? the objects list already has a\n'
  '  field for that. that would disambiguate the id".\n'
  '- WHAT THE LIST HAS, read at orrery b0eedeab, 184 entries in\n'
  '  `celestial_objects.py`. `object_type` says how a thing is drawn, not\n'
  '  what it is: fixed 1, orbital 68, satellite 46, barycenter 4,\n'
  '  hypothetical 1, lagrange_point 8, trajectory 40, and the exoplanet\n'
  '  systems\' four values, 16 entries. "orbital" holds Mercury to Pluto\n'
  "  (id_type None), 51 small bodies ('smallbody'), seven asked by JPL's\n"
  "  long ids ('majorbody': Patroclus, Menoetius, Haumea, Eris, Gonggong,\n"
  '  Makemake, Quaoar) and Orcus (none written). "trajectory" holds 29\n'
  "  spacecraft ('id'), 10 comets and interstellar objects ('smallbody')\n"
  "  and C/2025_K1 ('designation'). So `object_type` does not tell Mars,\n"
  '  499, from an asteroid numbered 499.\n'
  '- `id_type` DOES TWO JOBS. It tells astroquery how to read the id, and\n'
  "  the orrery's own code reads it as a kind: 'id' is taken for a\n"
  '  spacecraft (the close-approach passes), and the exoplanet entries\n'
  "  hold 'host_star', 'exoplanet', 'barycenter', 'binary_star_a' and\n"
  "  'binary_star_b', which JPL never sees. astroquery calls 'majorbody'\n"
  "  and 'id' deprecated, replaced by None (L-548's note).\n"
  '- THE IDEA: an entry says what the body is (planet, moon, dwarf planet,\n'
  '  asteroid, comet, spacecraft, barycentre, Lagrange point), and one\n'
  "  function works out how to ask JPL. The word can be JPL's own:\n"
  '  `horizons_unserved.py` records the kind JPL gives each id it checks\n'
  '  (L-539).\n'
  '- ONE LIMIT, not worked out: a small body is asked by its catalogue\n'
  "  number or by JPL's own long id (Haumea as 920136108, not 136108), so\n"
  '  the kind alone does not say how. Those entries need one more fact,\n'
  "  or a rule on the id's form.\n"
  '**Gap:** a design talk with Tony; then a list of all 184 entries, the\n'
  'kind of each and how it is asked today, before any code. `id_type` is\n'
  'on 68 lines of `palomas_orrery.py`; the session told Tony "about\n'
  'thirty places", from a list it had cut short. L-548\'s patch does not\n'
  'wait for this.\n'
  "**Ref:** L-548; L-539 (every entry checked); L-512 (the plot's data\n"
  'path); `celestial_objects.py`.\n'
  '\n'
  "#### [L-550] A website check added by a website session leaves the orrery's dashboard check red "
  '(method; for the skills bump)\n'),
 ('documentation/WHERE_WE_ARE.md',
  "Last updated: November 22, 2026, night: this coordinating session's close. The skills bump, "
  "v3.145, is pushed and you reinstalled; your look in the orrery's window is done (Claude Fable "
  '5.2).\n'
  '- Written on orrery 811cf44f and gallery e6af10ea, both pushed; both nights of Nov 22 clean.\n',
  "Last updated: November 23, 2026, morning: this coordinating session's close. Earth-Moon L4 is "
  'always above L5, live and looked at; your three waiting decisions are made (Claude Fable 5.2).\n'
  '- Written on orrery b0eedeab and gallery 326863a6, both pushed; both nights of Nov 22 clean; no '
  'night has run on the new page yet.\n'),
 ('documentation/WHERE_WE_ARE.md',
  '> - Five skills now carry the rules three builds had left on the ledger: protocol v3.145, '
  'pushed at 811cf44f. You reinstalled them and pasted the protocol; the next session checks that '
  "its copies are the new ones (L-539 (every entry checked), L-541 (a plan's clock)).\n"
  '> - Your look in the orrery\'s window is done. The animation with Earth-Moon L1 plays, your "-- '
  'yes". Its path is drawn from JPL\'s positions, as before; JPL is no longer asked for the '
  'numbers that describe an ellipse, which a point does not have (L-512 (fallbacks when JPL cannot '
  'answer)).\n'
  "> - Haumea's two moons, from your look: each orbit is drawn and says it is JPL's, of Feb 2, "
  'though JPL has since dropped both moons; the dates on its two end markers both show the day of '
  'the plot; neither moon has a marker of its own. Your "yes": that talk moves ahead of the '
  "encounter's slice 2 (L-549 (four moons JPL cannot place)).\n",
  "> - Earth-Moon L4 is always above L5 in Earth's fold: live at gallery 326863a6, your phone look "
  '"-- yes". Two rows closer than half a kilometre, the finest a box prints, are listed by name '
  '(L-544 (L4 and L5 tie), closed).\n'
  "> - The last 7 days of a path keeps its own build, straight after the orbiters' hourly points, "
  'your "Keep its own build" (L-533 (ESCAPADE), L-538 (the orbiters\' printed error)).\n'
  '> - Your three decisions. No new step before your own website pushes (L-543 (green on your '
  'computer, red on GitHub)). The two walks run at night on GitHub only, your "B" (L-545 (checks '
  "that wait to be remembered)). No saved scenes: every room's scene is made fresh at each run, "
  'your "Yes and we should remove obsolete saved files." (L-551 (no saved scenes)). A missing '
  'id_type is never guessed, and your idea of a kind of body goes to a design talk (L-548 (a '
  'missing id_type), L-552 (the kind of body)).\n'),
 ('documentation/WHERE_WE_ARE.md',
  '> **Do next:** *A new coordinating session first checks that its five skills are the new '
  "versions, then takes up L-544 (L4 and L5 tie), in the website; then the protocol's reduction, "
  "step 3 of L-522 (document caps), in its own Fable session; then L-538 (the orbiters' printed "
  'error); then the talk on L-549 (four moons JPL cannot place), put ahead on Nov 22, your "yes"; '
  "then the encounter's slice 2, its talk first (L-529 (guided encounters)).*\n",
  "> **Do next:** *The protocol's reduction, step 3 of L-522 (document caps), in its own Fable "
  "session; then L-538 (the orbiters' printed error); then every path to its last day, a build of "
  'its own (L-533 (ESCAPADE)); then the talk on L-549 (four moons JPL cannot place); then the '
  "encounter's slice 2, its talk first (L-529 (guided encounters)).*\n"),
 ('documentation/WHERE_WE_ARE.md',
  '> - *(do) Start the next coordinating session with '
  '`documentation/PROMPT_coordinator_start_20261122_4.md`, pasted from below its line. The website '
  'builds wait for its check of the skills.*\n',
  "> - *(do) Start the protocol's reduction in a new Fable session of its own, with "
  '`documentation/HANDOFF_document_upkeep_20261116.md` and L-522 (document caps). The coordinating '
  'session after it starts with `documentation/PROMPT_coordinator_start_20261123_1.md`, pasted '
  'from below its line.*\n'),
 ('documentation/WHERE_WE_ARE.md', '## The road\n', '## The road  **>> UPDATED THIS SESSION**\n'),
 ('documentation/WHERE_WE_ARE.md',
  '  d.   [beside] Document caps (L-522 (document caps)): steps 1 and 2\n'
  "               built Nov 10 and 11; step 3, the protocol's reduction, after L-544 and before "
  'L-538, in its own Fable session (your "Yes", Nov 22); step 4, the ledger\'s closed items moved '
  'out,\n'
  '               at the next gap between builds; then steps 5 and 6.\n'
  "  b.   [beside] This round's cleanup, each ruled Nov 19, in the order set Nov 21: every entry "
  'checked against JPL, L-539 (every entry checked), built Nov 22; then the L4 and L5 tie, L-544 '
  "(L4 and L5 tie), put ahead on Nov 22; then the orbiters' hourly points, L-538 (the orbiters' "
  "printed error); then every path to its last day, L-533 (ESCAPADE); the period's swing in its "
  "sentence, L-536 (a moon's yearly change); the 24 in goldenrod, L-432 (the default goldenrod), "
  'at your desk.\n',
  '  d.   [beside] Document caps (L-522 (document caps)): steps 1 and 2\n'
  "               built Nov 10 and 11; step 3, the protocol's reduction, is next, before L-538, in "
  'its own Fable session (your "Yes", Nov 22); step 4, the ledger\'s closed items moved out,\n'
  '               at the next gap between builds; then steps 5 and 6.\n'
  "  b.   [beside] This round's cleanup: every entry checked against JPL, L-539 (every entry "
  'checked), built Nov 22; the L4 and L5 tie, L-544 (L4 and L5 tie), built and closed Nov 22; then '
  "the orbiters' hourly points, L-538 (the orbiters' printed error); then every path to its last "
  "day, a build of its own, L-533 (ESCAPADE); the period's swing in its sentence, L-536 (a moon's "
  'yearly change); the 24 in goldenrod, L-432 (the default goldenrod), at your desk. Four small '
  'builds from the decisions of Nov 22, after step 3, at the gaps: the walks at night, L-545 '
  '(checks that wait to be remembered); no saved scenes, its list first, L-551 (no saved scenes); '
  'the push-copy script, L-543 (green on your computer, red on GitHub); no guessed id_type, L-548 '
  '(a missing id_type).  << moved this session\n'),
 ('documentation/WHERE_WE_ARE.md', '## Settled\n', '## Settled  **>> UPDATED THIS SESSION**\n'),
 ('documentation/WHERE_WE_ARE.md',
  "- A visitor reads UTC everywhere. The room adds JPL's clock difference before it looks up JPL's "
  "data; only a body's source line names JPL's clock, for the date of its orbit; a plan's moments "
  'print as UTC (Nov 21, your "Yes"; L-541 (a plan\'s clock)).\n',
  "- No saved scenes: the gallery's checks get every room's scene made fresh at each run, as the "
  "Sun's always was, and the saved copies are removed (Nov 22; L-551 (no saved scenes)).\n"
  '- The two walks run at night on GitHub only; a failed walk makes the night red; nothing is '
  'added to your computer (Nov 22; L-545 (checks that wait to be remembered)). You run no '
  'push-copy check before your own pushes; the night catches those (Nov 22; L-543 (green on your '
  'computer, red on GitHub)).\n'
  '- Nothing guesses a missing id_type: every entry writes it, and a reader that finds none leaves '
  'that object out and names it (Nov 23; L-548 (a missing id_type)).\n'),
 ('documentation/WHERE_WE_ARE.md',
  "- Every entry the orrery asks JPL for is held to JPL's name and kind for its id; an id JPL has "
  'no object for is recorded so, and a first answer waits on your look (Nov 19 and 22; L-539 '
  '(every entry checked)).\n',
  ''),
 ('documentation/WHERE_WE_ARE.md',
  "- Last cache build: 20261122T194726Z, ok, no retry on the swap (the website's swap log at "
  'e6af10ea, read Nov 22).\n'
  '- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md, generated Nov 22, read '
  'Nov 22 at 811cf44f).\n'
  "- This page's date and the ledger's newest stamp: both Nov 22. Agree.\n",
  "- Last cache build: 20261122T194726Z, ok, no retry on the swap (the website's swap log at "
  '326863a6, read Nov 23). No night has run since the push of Nov 22, 22:31.\n'
  '- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md, generated Nov 22, read '
  'Nov 23 at b0eedeab).\n'
  "- This page's date and the ledger's newest stamp: both Nov 23. Agree.\n"),
 ('documentation/WHERE_WE_ARE.md',
  "- Whether the gallery's checks are read from a copy holding only what a push carries, before "
  'every website push. Nov 21\'s red nights were green on your computer. Your "-- okay" was to '
  'raising it (L-543 (green on your computer, red on GitHub)).\n'
  '- Whether the two walks join the gallery run, which means the website keeps one more library; '
  'and when the recorded Earth scene is re-recorded. Your words, Nov 21: "should this be method?" '
  "The session's part is method now; these two are yours (L-545 (checks that wait to be "
  'remembered)).\n'
  '- Whether every entry writes its id_type, or every reader takes one default: the orbit '
  "pre-fetch reads a missing one as an asteroid's, and only one line keeps Pluto from being asked "
  'as asteroid 999 (L-548 (a missing id_type)).\n',
  '- Where the four small builds from the decisions of Nov 22 sit in the order. Until you say: '
  "after the protocol's reduction, at the gaps between builds (the road, line b).\n"),
 ('documentation/WHERE_WE_ARE.md',
  "- The four moons JPL cannot place: what Hi'iaka and Namaka should draw and say now that JPL has "
  'dropped them, and whether Vanth, which JPL answers again, comes off its skip lists. Ahead of '
  'the encounter\'s slice 2, your "yes". Your look: the orbits say JPL, of Feb 2; their end '
  "markers' dates both show the plot's day; neither moon has its own marker (Nov 22; L-549 (four "
  'moons JPL cannot place)).\n',
  "- The four moons JPL cannot place: what Hi'iaka and Namaka should draw and say now that JPL has "
  'dropped them, and whether Vanth, which JPL answers again, comes off its skip lists. Ahead of '
  'the encounter\'s slice 2, your "yes". Your look: the orbits say JPL, of Feb 2; their end '
  "markers' dates both show the plot's day; neither moon has its own marker (Nov 22; L-549 (four "
  'moons JPL cannot place)).\n'
  "- The kind of body: each entry in the orrery's list would say what it is (planet, moon, "
  'asteroid, comet, spacecraft), and how JPL is asked would follow from it. Your words: '
  '"shouldn\'t we specify what kind of body it is?" The list\'s object_type says how a thing is '
  'drawn, not what it is (Nov 23; L-552 (the kind of body)).\n'),
 ('documentation/WHERE_WE_ARE.md',
  '- This round: L-539 (every entry checked), its brief '
  '`COORD_L539_every_entry_brief_20261122.md`, the list you scanned '
  '`CHECK_L539_every_entry_names_20261122.md`, the check `horizons_unserved.py`. The clock: L-541 '
  "(a plan's clock). The encounter: L-529 (guided encounters), `DESIGN_encounters_20261120.md`.\n",
  '- This round: L-539 (every entry checked), its brief '
  '`COORD_L539_every_entry_brief_20261122.md`, the list you scanned '
  '`CHECK_L539_every_entry_names_20261122.md`, the check `horizons_unserved.py`. The clock: L-541 '
  "(a plan's clock). The encounter: L-529 (guided encounters), `DESIGN_encounters_20261120.md`. "
  "The tie: L-544 (L4 and L5 tie), `patch_L544_1_tie_break.py` in the website's documentation.\n")]

PROMPT_PATH = 'documentation/PROMPT_coordinator_start_20261123_1.md'
PROMPT_TEXT = ('<!-- Doc-Kind: hand | A starting prompt for the next coordinating session, written at the close '
 'of the one before it. -->\n'
 '# Starting prompt: the next coordinating session\n'
 '\n'
 'Built on orrery b0eedeab at\n'
 'https://github.com/tonylquintanilla/palomas_orrery (branch main) and\n'
 'gallery 326863a6 at\n'
 'https://github.com/tonylquintanilla/tonyquintanilla.github.io, with\n'
 'patch_L544_2_session_close.py on top. Written Nov 23, 2026 by the\n'
 'coordinating session of Nov 22 and 23 (Claude Fable 5.2).\n'
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
 "   HEAD should hold the last session's close: L-544 on the ledger reads\n"
 '   DONE, L-551 and L-552 exist, and\n'
 '   documentation/PROMPT_coordinator_start_20261123_1.md exists. If not,\n'
 '   patch_L544_2_session_close.py was not run or not pushed; say so\n'
 '   before anything else.\n'
 '2. THE FIRST CHECK. No website night had run on the changed page when\n'
 "   the last session closed. Read the website's night record: its Drawer\n"
 '   order row should end "self-test red four times". "three times" means\n'
 '   that night ran before the push of Nov 22 (326863a6). A red row is\n'
 '   the first thing to tell Tony.\n'
 "3. Ask Tony whether the protocol's reduction, step 3 of L-522 (document\n"
 '   caps), has run in its own session. If it has, the protocol and some\n'
 '   skills have moved: load what the work fires and compare each version\n'
 '   line with the manifest (Stale Skill = Stop). No skill was bumped by\n'
 '   the session that wrote this.\n'
 "4. Read documentation/WHERE_WE_ARE.md, then Tony's newest run-record\n"
 '   copy (documentation/WHERE_WE_ARE_*_run_record.md) for his notes.\n'
 '5. Read the night records in BOTH repositories. The orrery: its Horizons\n'
 '   check row reads NOTHING DUE until Nov 25, when 90 served identities\n'
 '   renew together, about 7 minutes of a 15-minute limit; a title that\n'
 '   starts JPL DIFFERS or NEW JPL NAME is the first thing to tell Tony.\n'
 "   NOAA's next El Nino update is expected 10 December 2026. The website:\n"
 '   59 rows.\n'
 '\n'
 'Where things stand:\n'
 '\n'
 "- L-544 (L4 and L5 tie) is built and closed: gallery 326863a6, Tony's\n"
 '  phone look "-- yes". Two children of a body nearer each other than\n'
 '  half a kilometre are listed by name (settleTies, in\n'
 '  gallery/drawer_order.js).\n'
 '- The last 7 days of a path (L-533) keeps its own build, straight after\n'
 '  L-538: Tony, Nov 22, "Keep its own build".\n'
 "- Three decisions of Nov 22 and 23, each on the ledger in Tony's words:\n"
 '  no push-copy step before his own website pushes (L-543); the two\n'
 '  walks run at night on GitHub only, a failed walk red (L-545); no\n'
 "  saved scenes, every room's scene made fresh at each run and the saved\n"
 '  copies removed (L-551); a missing id_type is never guessed (L-548),\n'
 '  and his idea, a kind of body on each entry, is for a design talk\n'
 '  (L-552).\n'
 '\n'
 'Next, in this order:\n'
 '\n'
 "- Step 3 of L-522, the protocol's reduction, in its own Fable session,\n"
 '  BEFORE any build: Tony starts it with\n'
 '  documentation/HANDOFF_document_upkeep_20261116.md and L-522. The\n'
 '  coordinating session writes it no brief. If Tony opens this session\n'
 '  before step 3 has run, say so, and take only work that touches no\n'
 "  skill at its cap: L-551's list (no code), or a talk (L-549, L-552).\n"
 "- Then L-538 (the orbiters' printed error); then L-533's last day, a\n"
 '  build of its own; then the talk on L-549 (the four moons); then the\n'
 "  encounter's slice 2, its talk first (L-529).\n"
 '- Four small builds, after step 3, at the gaps; where they sit in the\n'
 "  order waits on Tony. L-545: read the night's workflow file first and\n"
 '  size it. L-551: the list first, each check and walk, which saved copy\n'
 '  it reads, whether it holds numbers fixed to that copy. L-543: the\n'
 "  push-copy script into the website's tools folder. L-548: the patch,\n"
 '  with all five consumers of position data mapped first.\n'
 "- Step 4 of L-522, the ledger's closed items moved out by a tool, at\n"
 '  the next gap; steps 5 and 6 the same way.\n'
 '- Open on L-541, for an orrery session and a builder session: the\n'
 '  builder asks daily points 9 seconds before UTC midnight; its keys and\n'
 "  plan windows are read as UTC; the orrery's whole-second 69.\n"
 '\n'
 'Lessons from the last session worth carrying:\n'
 '\n'
 "- The ledger's Gap described the code wrongly: it said the gallery\n"
 "  editor's tree lists the drawer's order (it lists the config's), and\n"
 '  the page set the order in two places, not one. Read the code before\n'
 '  telling Tony where a change goes; the session told him "two places"\n'
 '  and had to correct it.\n'
 '- What proved the build: two clean clones of the pushed commit, one\n'
 '  untouched and one patched, the same driver minute for both; the walk\n'
 "  red before and green after; then the drawer's rows listed from both,\n"
 '  so "the only two rows that moved" was read, not argued. The driver\n'
 '  was scanned for a minute of each kind first.\n'
 "- Nine gallery-run rows cannot run in a session's sandbox (no GitHub\n"
 "  API, no Tk, no ERFA). Compare each row's verdict with the untouched\n"
 "  copy's, by name, and say which rows could not run.\n"
 "- Twice Tony's question widened a proposal that was too narrow: a\n"
 '  fingerprint for the Earth scene became no saved scenes for any room,\n'
 '  and a missing field became the kind of body. Before proposing a\n'
 '  mechanism for one room or one field, ask how the others are handled.\n'
 '- Twice a count given to Tony was wrong because a list was cut short\n'
 '  or copied from the ledger: "six checks" was ten; "about thirty\n'
 '  places" was 68 lines. Count from the file, whole.\n'
 "- After a night's pause, read both heads and both night records again\n"
 "  before the close. No night had run; the page's Signals say so.\n"
 '- Reading the placed patch back failed once ("hardlinked") and\n'
 '  succeeded 35 seconds later, as before.\n'
 '\n'
 "Ask Tony one thing to begin: whether the protocol's reduction, step 3\n"
 'of L-522, has run.\n')


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
    ppath = os.path.join(HERE, *PROMPT_PATH.split('/'))
    pbytes = PROMPT_TEXT.encode('ascii')
    write_prompt = True
    if os.path.exists(ppath):
        with open(ppath, 'rb') as f:
            have = f.read().replace(b'\r\n', b'\n')
        if have == pbytes:
            write_prompt = False
        else:
            print("ERROR: %s already exists and differs from the one this "
                  "patch places. Likely a copy saved by hand: delete it and "
                  "run again. NOTHING was written." % PROMPT_PATH)
            sys.exit(1)
    for name, (text, was_crlf) in staged.items():
        with open(os.path.join(HERE, *name.split('/')), 'wb') as f:
            f.write(text)
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % name)
    print("patch applied (%d edits, %d files)" % (len(EDITS), len(staged)))
    if write_prompt:
        with open(ppath, 'wb') as f:
            f.write(pbytes)
        print("wrote %s (%d bytes)" % (PROMPT_PATH, len(pbytes)))
    else:
        print("already there, identical: %s" % PROMPT_PATH)
    print("stamps updated: Where We Are's header (b0eedeab, 326863a6)")
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
    print("the orrery. The protocol's reduction is next, in its own")
    print("session; the coordinating session after it starts with")
    print("documentation/PROMPT_coordinator_start_20261123_1.md.")


if __name__ == '__main__':
    main()
