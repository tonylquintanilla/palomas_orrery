#!/usr/bin/env python3
"""
patch_L413_1_ledger_sweep_and_earth_list_20261004.py -- ORRERY repo.
Closes the ledger-sweep session of 2026-10-04: Earth's list (L-413),
the scanner finding (L-414), seven closes, and safe-file-editing 1.12
with protocol v3.80 (L-415, line endings).

Built on orrery 41c1ca7a175992248dad9cc3237686beab032f82
at https://github.com/tonylquintanilla/palomas_orrery
(gallery e7ef96eb07fbdede9a270965d216511eb4949043 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io was read,
not changed; there is no gallery patch this session).

This replaces the first build of the same name, made on cbde99dc, which
never ran. If that copy is still in the repo root, let this one
overwrite it.

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code and click Run. Then run orrery_maintenance_run.py
    the same way: every gating check should pass. Its Ledger index step
    moves the seven closed items into the closed section, and its Skill
    manifest step writes safe-file-editing 1.12 into the protocol; both
    are expected. Then move this script into documentation/, commit,
    push. Then reinstall safe-file-editing in Settings > Skills from
    skills/safe-file-editing/SKILL.md, and replace the Project's
    instructions with PROJECT_INSTRUCTIONS.md (v3.80).

WHAT CHANGES
    LEDGER_CONSOLIDATED.md
        Opens L-413 (Earth's list, in Tony's order), L-414 (the
        scanner's 15-line window and declared rows) and L-415 (line
        endings). Closes L-409, L-407, L-350, L-406, L-305, L-234 and
        L-383 (folded into L-181), each with its evidence and its loose
        ends re-homed (L-305's aberration to L-314; L-234's dipole cone
        to L-375). Corrects L-228, L-408, L-412, L-216, L-363 (with
        Tony's GO-arrow ruling), L-411, L-136, L-300, L-396, L-351,
        L-314, L-181, L-292, L-369, L-375, L-367, L-330; names L-133's 22
        files; moves L-131 and L-128 to section A; L-308 to DEFERRED;
        moves the date on L-386 and L-241; stamps the header. Matched by
        its lines, not the whole file, so your notes elsewhere in it do
        not stop this patch.
    skills/safe-file-editing/SKILL.md   1.11 -> 1.12: a patch writes LF
        and reports; a file committed CRLF keeps its endings and waits
        for L-133's sweep.
    PROJECT_INSTRUCTIONS.md             v3.80: header, anchor, the
        version entry; v3.77 moves down.
    documentation/PROJECT_INSTRUCTIONS_HISTORY.md   receives v3.77.
    documentation/WHERE_WE_ARE.md       rewritten, as at every session's
        end. Your notes on it are carried into the ledger first. Checked
        whole: if it changed since 41c1ca7a the patch stops rather than
        lose your words.
    documentation/HANDOFF_L413_ledger_sweep_and_earth_list_20261004.md  new.

LINE ENDINGS (safe-file-editing 1.12, which this patch installs and
follows): every file is written LF, the repos' convention. A file that
arrived CRLF in your working copy is named in a "note:" line. All six
files here are committed LF, so none is the exception.

PERMANENT, though this script is thrown away: the ledger entries, the
skill, the protocol entry, the page, the handoff.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 4, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

REPO = "orrery"
ROOT_MARKERS = ("palomas_orrery.py", "LEDGER_CONSOLIDATED.md")
BUILT_ON = "41c1ca7a"
ANCHOR_ONLY = ("LEDGER_CONSOLIDATED.md",)
ZONED = {"PROJECT_INSTRUCTIONS.md": ("<!-- SKILL-MANIFEST:START",
                                     "<!-- SKILL-MANIFEST:END -->")}
NEXT = ["1. Run orrery_maintenance_run.py. Every gating check passes; the",
        "   Ledger index step moves seven closed items to section C, and",
        "   the Skill manifest step writes 1.12 into the protocol.",
        "2. Move this script into documentation/; commit and push.",
        "3. Reinstall safe-file-editing (Settings > Skills) from",
        "   skills/safe-file-editing/SKILL.md, and replace the Project's",
        "   instructions with PROJECT_INSTRUCTIONS.md (v3.80)."]

BASE = {'PROJECT_INSTRUCTIONS.md': '71de7141228336c1f9cd5c323917f378',
 'documentation/PROJECT_INSTRUCTIONS_HISTORY.md': '9bb462a4fd2e6d96b557c8e4c8efdcc7',
 'skills/safe-file-editing/SKILL.md': '41350cb96059ddbeceef9c8db8416e2d'}

EDITS = {'LEDGER_CONSOLIDATED.md': [('L-409: status line',
                             '<!-- L:409 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice: -->',
                             '<!-- L:409 status:DONE upd:2026-10-04 '
                             'section:C flag: rice: -->',
                             1),
                            ('L-409: closed on the sidebar check',
                             "**Gap:** after both pushes, each repository's "
                             'GitHub page should say\n'
                             '"MIT license" in its sidebar -- the one check '
                             'that the recognition\n'
                             'worked. **Tony-action (do):** look at both.\n',
                             "- **2026-10-04, CLOSED.** Both repositories' "
                             'GitHub pages say "MIT\n'
                             '  license" in the sidebar: read from '
                             'github.com by the Claude Fable 5.1\n'
                             '  ledger sweep of 2026-10-04\n'
                             '  '
                             '(`documentation/LEDGER_SWEEP_review_20261004.md`), '
                             "and Tony's page\n"
                             "  says the same. The Gap's one check has "
                             'passed.\n'
                             '**Gap:** none.\n',
                             1),
                            ('L-407: status line',
                             '<!-- L:407 status:OPEN upd:2026-10-02 '
                             'section:A flag: rice: -->',
                             '<!-- L:407 status:DONE upd:2026-10-04 '
                             'section:C flag: rice: -->',
                             1),
                            ('L-407: closed on the load check',
                             '**Gap:** Tony reinstalls interactive-exhibit, '
                             'earth-system-pipeline and\n'
                             'provenance-discipline and replaces the '
                             "Project's instructions with\n"
                             'v3.79. The next session confirms its loaded '
                             'copies read 1.10, 1.2 and\n'
                             "2.25, and that provenance-discipline's "
                             'description runs past "adding\n'
                             'or reviewing", then closes this item.\n',
                             '- **2026-10-04, CLOSED.** The Fable 5.1 ledger '
                             'sweep of 2026-10-04\n'
                             '  loaded provenance-discipline 2.25, '
                             'earth-system-pipeline 1.2 and\n'
                             '  interactive-exhibit 1.10; '
                             "provenance-discipline's description runs to\n"
                             '  "Do not use for projects other than '
                             'Paloma\'s Orrery", past the old\n'
                             '  cut. The resident protocol is v3.79. The '
                             'L-371 handoff\'s "no load to\n'
                             '  confirm next session" was true of that '
                             "session's own skills; this\n"
                             '  obligation from 2026-10-02 was the one still '
                             'open.\n'
                             '**Gap:** none.\n',
                             1),
                            ('L-350: status line',
                             '<!-- L:350 status:OPEN upd:2026-09-28 '
                             'section:A flag: rice: -->',
                             '<!-- L:350 status:DONE upd:2026-10-04 '
                             'section:C flag: rice: -->',
                             1),
                            ('L-350: closed, the hover prints it',
                             '**Gap:** Decide whether the magnetotail hover '
                             'should print it; if not, stop serving it.\n',
                             '- **2026-10-04, CLOSED: the premise is gone.** '
                             "The website's\n"
                             '  magnetotail hover prints the observed '
                             'extent: "The drawing stops at\n'
                             '  220 Earth radii, which is how far the '
                             'spacecraft went, not where the\n'
                             '  tail ends." (`gallery/feature_renderers.js`, '
                             'read from\n'
                             '  `tl.observed_extent` with its served figure '
                             'count) [verified @\n'
                             '  gallery e7ef96eb]. Added by L-322 Stage D '
                             'gallery patch 3, after this\n'
                             '  item was written. Found by the Fable 5.1 '
                             'ledger sweep; confirmed by\n'
                             '  the Opus 5.5 session the same day. Not '
                             'checked: whether that hover is\n'
                             "  still inside the hover budget's ceiling; the "
                             'budget suite gates that\n'
                             '  on every run.\n'
                             '**Gap:** none.\n',
                             1),
                            ('L-406: status line',
                             '<!-- L:406 status:OPEN upd:2026-10-02 '
                             'section:A flag: rice: -->',
                             '<!-- L:406 status:DONE upd:2026-10-04 '
                             'section:C flag: rice: -->',
                             1),
                            ("L-406: closed, the look is L-408's",
                             '**Gap:** The look, on the phone and in the '
                             'orrery (Mode 5), waits on\n'
                             "L-408's ring as its reference.\n",
                             '- **2026-10-04, CLOSED.** Built and pushed on '
                             'both sides. Its one open\n'
                             "  step, the look at the tide's X, is L-408's "
                             'purpose and is recorded\n'
                             '  there (Fable 5.1 ledger sweep, 2026-10-04).\n'
                             '**Gap:** none here; the look is in L-408.\n',
                             1),
                            ('L-305: status line',
                             '<!-- L:305 status:OPEN upd:2026-09-16 '
                             'section:A flag: rice:4/4/60/4 -->',
                             '<!-- L:305 status:DONE upd:2026-10-04 '
                             'section:C flag: rice:4/4/60/4 -->',
                             1),
                            ('L-305: closed, loose ends re-homed',
                             '**Ref:** L-291, L-292, L-298 (the '
                             'orrery-vs-exhibit gap, made concrete),',
                             '**Note (2026-10-04) -- CLOSED, read against '
                             'the code** [verified @\n'
                             'orrery cbde99dc, gallery e7ef96eb]. Items (4) '
                             'to (8) have landed.\n'
                             "The orrery draws Shue's magnetopause and "
                             "Jelinek's bow shock from the\n"
                             'store (`earth_visualization_shells.py`, '
                             '`_shue_radius`,\n'
                             '`_shue_flaring`; L-322 Stage D patch D8), and '
                             '`magnetic_tilt_deg=11` is\n'
                             'gone from its call. The website draws the same '
                             'two surfaces and the\n'
                             'Slavin tail from served rows; the '
                             "magnetotail's old `base_radii` and\n"
                             '`end_radii` are retired; the i panel\'s "not '
                             'drawn yet" paragraph is\n'
                             "gone. The 2026-09-15 handoff's three interface "
                             'items were settled\n'
                             "later: the drawer row by L-318 round 3 (Tony's "
                             'five rulings of\n'
                             '2026-09-15, which withdrew the one-target '
                             'row), the navigation cross by\n'
                             'L-316 round 4, and the i-panel text by item '
                             '(7). Both instruments were\n'
                             "The website's surfaces were seen by Tony on "
                             'the phone (2026-09-16, "all\n'
                             'look good"); the orrery\'s D8 drawing went '
                             "through Stage D's own\n"
                             'checks.\n'
                             'Loose ends, each re-homed (A Closing Item '
                             'Re-homes Its Loose Ends):\n'
                             '- **The aberration, never decided and never '
                             'built.** The\n'
                             '  Tony-action (decide) above -- apply the 4.3 '
                             'degrees at the declared\n'
                             '  400 km/s, or draw un-aberrated and say so -- '
                             'has no ruling, and\n'
                             '  neither instrument applies it or says it '
                             'does not ("aberrat" appears\n'
                             '  in neither renderer). Moved to L-314, '
                             'because the angle is set by the\n'
                             "  solar wind's speed, which L-314 makes live.\n"
                             '- L-350 pointed here; it closed the same day '
                             '(its hover prints the\n'
                             '  observed extent).\n'
                             '- The four Earth rows the scanner scores Tier '
                             '1 (the mean radius and\n'
                             '  the three declared solar wind conditions) '
                             "are not this item's: see\n"
                             '  L-414.\n'
                             '**Gap:** none.\n'
                             '**Ref:** L-291, L-292, L-298 (the '
                             'orrery-vs-exhibit gap, made concrete),',
                             1),
                            ('L-234: status line',
                             '<!-- L:234 status:OPEN upd:2026-08-25 '
                             'section:A flag: rice:4/5/90/3 -->',
                             '<!-- L:234 status:DONE upd:2026-10-04 '
                             'section:C flag: rice:4/5/90/3 -->',
                             1),
                            ('L-234: closed, the Earth half is served',
                             '**Ref:** HANDOFF 2026-08-25 (orrery '
                             '`4ad78a01`, gallery `64201783` ->',
                             '**Note (2026-10-04) -- CLOSED: the Earth half '
                             'is served** [verified @\n'
                             'gallery e7ef96eb, `data/objects_config.json`]. '
                             "Earth's feature groups:\n"
                             'earth_interior (inner core, outer core, lower '
                             'mantle, upper mantle,\n'
                             'crust), earth_atmosphere, earth_exosphere (the '
                             'geocorona),\n'
                             'earth_orbital_zones (LEO), '
                             'earth_geostationary, earth_magnetosphere\n'
                             '(magnetopause, bow shock, magnetotail), '
                             'van_allen_belts, hill_sphere,\n'
                             'and orientation (the pole and rotation period, '
                             'from which the room\n'
                             'draws the rotation axis). The Fable 5.1 sweep '
                             'listed the Hill sphere as\n'
                             'missing; it is its own group.\n'
                             'One loose end, re-homed: **the dipole cone is '
                             'not drawn on the\n'
                             'website**, and no ruling against it was found. '
                             'It depends on a\n'
                             'rotation phase the website does not model, the '
                             'same question L-375\n'
                             "asks of the dipole's offset, so it goes to "
                             'L-375.\n'
                             'The RICE (decide) above lapses with the item.\n'
                             '**Gap:** none.\n'
                             '**Ref:** HANDOFF 2026-08-25 (orrery '
                             '`4ad78a01`, gallery `64201783` ->',
                             1),
                            ('L-383: status line',
                             '<!-- L:383 status:OPEN upd:2026-09-28 '
                             'section:A flag: rice: -->',
                             '<!-- L:383 status:DONE upd:2026-10-04 '
                             'section:C flag: rice: -->',
                             1),
                            ('L-383: folded into L-181',
                             "**Gap:** Bring the copy into line when L-349's "
                             'wording is ruled, or retire the copy.\n',
                             '- **2026-10-04, CLOSED by folding into '
                             "L-181.** The magnetosphere's\n"
                             "  `tooltip` sits in `CUSTOM_SHELLS['Earth']` "
                             'in `shell_configs.py`, and\n'
                             '  no code reads a config `tooltip` field: '
                             'checkbox tooltips come from\n'
                             '  the `<body>_<suffix>_info` variables through '
                             '`tooltips_dict`\n'
                             '  (`celestial_objects.build_shell_checkboxes`) '
                             '[verified @ cbde99dc].\n'
                             '  orrery-coding-conventions already names all '
                             '124 such fields dead\n'
                             "  data, says delete-or-wire is L-181's "
                             'decision, and says to keep each\n'
                             '  in agreement with its live twin until then. '
                             'So this copy is one of\n'
                             "  L-181's 124, not an item of its own. When "
                             "L-349's wording is ruled,\n"
                             '  the build that carries it keeps this copy in '
                             'step, as the skill says.\n'
                             '**Gap:** none here; L-181 (d).\n',
                             1),
                            ('L-228: status line',
                             '<!-- L:228 status:OPEN upd:2026-10-04 '
                             'section:A flag:Tony rice:2/3/60/2 -->',
                             '<!-- L:228 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice:2/3/60/2 -->',
                             1),
                            ('L-228: the (do) struck',
                             '- **Tony-action (do):** the source read. '
                             'Claude cannot clear this by\n'
                             '  reasoning about it, and guessing here is the '
                             'failure this week was\n'
                             '  spent on.\n',
                             '- ~~Tony-action (do): the source read.~~ '
                             'Struck 2026-10-04: the note\n'
                             '  above it (2026-10-04) has Claude do the read '
                             'by web, and the two\n'
                             '  disagreed (Fable 5.1 ledger sweep). The flag '
                             'that put "[Tony]" on the\n'
                             '  index row goes with it; the RICE (decide) '
                             'below stays.\n',
                             1),
                            ('L-408: status line',
                             '<!-- L:408 status:OPEN upd:2026-10-03 '
                             'section:A flag: rice: -->',
                             '<!-- L:408 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice: -->',
                             1),
                            ('L-408: the Gap made current',
                             "**Gap:** Build it next session, with the Sun's "
                             'distance cards (L-371):\n'
                             'gallery first; whether the orrery gets the '
                             'same toggle is asked then.\n',
                             '- **2026-10-04:** not built with L-371, as the '
                             'Gap had planned; it is\n'
                             "  the Sun slice's eighth item (L-412). It also "
                             'carries the look at the\n'
                             "  galactic tide's X that L-406 handed over "
                             'when it closed: turn until\n'
                             '  the ring is edge-on.\n'
                             "**Gap:** the Sun slice's eighth item (L-412): "
                             'gallery first; whether\n'
                             'the orrery gets the same toggle is asked then; '
                             "then the tide's look.\n",
                             1),
                            ('L-412: status line',
                             '<!-- L:412 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice: -->',
                             '<!-- L:412 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice: -->',
                             1),
                            ("L-412: Earth's list first",
                             '**Gap:** work down the list.\n'
                             "**Ref:** L-371 (the slice's numbers); the "
                             'handles above.\n',
                             "- **2026-10-04, Tony's notes on Where We Are "
                             'and the order he\n'
                             "  confirmed that evening.** Earth's old items "
                             'go FIRST (L-413), then\n'
                             '  this list resumes at item 3. After it: the '
                             "gallery's checks as a\n"
                             '  short ordered list, before the swap (L-363), '
                             'because one of them\n'
                             '  (L-367) is that no checker boots a new room, '
                             'and the swap changes the\n'
                             '  front door. Tony also asked for ledger '
                             'cleanup to be a standing step\n'
                             '  in the road, room by room under The Braid '
                             'and Cluster the Tail by\n'
                             '  Files Touched (ledger-and-session-records); '
                             'L-413 is the first.\n'
                             '- **Raised by the Fable 5.1 ledger sweep, for '
                             'Tony one at a time:**\n'
                             '  (a) whether an item inside an ordered list '
                             'like this one needs a RICE\n'
                             "  score, since the plan's sequencing outranks "
                             'the score (L-221) -- all\n'
                             '  67 unscored live items are L-343 onward; (b) '
                             'the scores it proposes\n'
                             '  (L-131 and L-128 at 3/3/70/2; L-216 lowered '
                             'or DEFERRED; L-228, L-241,\n'
                             '  L-292 confirmed; L-252 re-scored).\n'
                             '**Gap:** after L-413, work down the list from '
                             'item 3.\n'
                             "**Ref:** L-371 (the slice's numbers); the "
                             'handles above; L-413;\n'
                             '`documentation/LEDGER_SWEEP_review_20261004.md`.\n',
                             1),
                            ('L-216: the stray folder deleted',
                             '  - **Tony-action (do):** delete it, with '
                             'OneDrive paused, as before.\n',
                             '  - **Tony-action (do) -- DONE 2026-10-04** '
                             "(Tony's note on Where We\n"
                             '    Are): deleted.\n',
                             1),
                            ('L-363: status line',
                             '<!-- L:363 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice: -->',
                             '<!-- L:363 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice: -->',
                             1),
                            ('L-363: lobby checker re-homed',
                             "  - No gating checker reads `index.html`'s "
                             'lobby code; the maintenance\n'
                             "    run's 23 passes cover everything else. "
                             'Recorded, not chased.\n',
                             "  - No gating checker reads `index.html`'s "
                             'lobby code; the maintenance\n'
                             "    run's 23 passes cover everything else. "
                             'Recorded, not chased.\n'
                             '    Re-homed to L-367 on 2026-10-04, with the '
                             'rooms no checker boots.\n',
                             1),
                            ('L-363: two decides struck, GO arrow ruled, Gap '
                             'rewritten',
                             '- **Tony-action (decide), at Half 2:** whether '
                             'ticking a drawer row\n'
                             '  also opens it (design question 13).\n'
                             '- **Tony-action (decide), at Half 2:** Apophis '
                             'is drawn today but has\n'
                             '  no place in the ten-row drawer: one row '
                             'under "See more" until the\n'
                             '  near-Earth asteroids round, or out of Half 2 '
                             'until then.\n',
                             '- ~~Tony-action (decide), at Half 2: whether '
                             'ticking a drawer row\n'
                             '  also opens it (design question 13).~~ '
                             'Settled at the design talk of\n'
                             '  2026-09-30 and built.\n'
                             '- ~~Tony-action (decide), at Half 2: Apophis '
                             'is drawn today but has\n'
                             '  no place in the ten-row drawer.~~ Settled: '
                             'one row under "See more",\n'
                             '  built.\n'
                             "- **Tony's ruling, 2026-10-04 (his note on "
                             'Where We Are), on the\n'
                             "  arrow from GO's text box to its body:** "
                             '"the problem with this last\n'
                             '  time is that it moved the text box from the '
                             'center. the text box\n'
                             '  needs to remain in the center. if not '
                             "possible, don't implement the\n"
                             '  arrow." So the arrow may not amend L-318\'s '
                             'mid-view ruling, which the\n'
                             '  2026-10-02 note had allowed for.\n',
                             1),
                            ('L-363: Gap',
                             '**Gap (2026-09-29):** Half 2 as section 4 of '
                             '`documentation/HANDOFF_L363_three_strands_integrated_20260929.md` '
                             'sets it out, from step 1 (step 0 was this '
                             'entry): a short design round, the five planets '
                             "and one cache rebuild, the drawer, Tony's Mode "
                             "5. The swap after the Sun's slice closes.\n",
                             '**Gap (2026-09-29; SUPERSEDED 2026-10-04):** '
                             'Half 2 as section 4 of '
                             '`documentation/HANDOFF_L363_three_strands_integrated_20260929.md` '
                             'sets it out. All of it is built.\n'
                             '**Gap (2026-10-04):** (a) the swap: a bare '
                             '`interactive.html` link\n'
                             'opens this room and the Explorer gets its own '
                             "address, after the Sun's\n"
                             "slice and the gallery's checks (L-412); (b) "
                             "the arrival block's\n"
                             '`_declared` sentence still says the view fits '
                             '"1.1 times the largest\n'
                             'distance" where the rule is 1.2 [verified @ '
                             'gallery e7ef96eb,\n'
                             '`data/objects_config.json`] -- listed as a '
                             'small fix on 2026-10-02, it\n'
                             'did not ride patch_L363_14; (c) the '
                             'design-talk items: the highlighted\n'
                             "row at the top of the list, and GO's arrow "
                             'only if the text box stays\n'
                             'centred; (d) whether the editor edits the '
                             "rows' own words, re-homed\n"
                             'from L-404.\n',
                             1),
                            ('L-411: status line',
                             '<!-- L:411 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice: -->',
                             '<!-- L:411 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice: -->',
                             1),
                            ('L-411: the credit line',
                             "**Gap:** the Sun slice's fifth item (L-412), "
                             'straight after L-228.\n',
                             '- **2026-10-04, one more instance, and it is '
                             "Claude's own.** The\n"
                             '  credit line at the top of '
                             '`solar_visualization_shells.py` names\n'
                             '  94.01 AU, 121 AU and 0.65 parsecs in prose, '
                             'and the scanner reads the\n'
                             '  module docstring as a display string with '
                             'eight uncited claims\n'
                             '  (`PROVENANCE_AUDIT.md`, line 1) [verified @ '
                             'cbde99dc]. Written by the\n'
                             '  L-371 session, which caught the same mistake '
                             'in\n'
                             '  `comet_visualization_shells.py` and missed '
                             'it here. The other six\n'
                             '  Tier-1 findings in that file are the '
                             'date-sensitive hovers this item\n'
                             '  already holds.\n'
                             "**Gap:** the Sun slice's fifth item (L-412), "
                             'straight after L-228.\n',
                             1),
                            ('L-136: status line',
                             '<!-- L:136 status:OPEN upd:2026-07-17 '
                             'section:D.Feature-B flag: rice:2/2/50/2 -->',
                             '<!-- L:136 status:OPEN upd:2026-10-04 '
                             'section:D.Feature-B flag: rice:2/2/50/2 -->',
                             1),
                            ('L-136: scattered disk vs fuzzy boundaries',
                             '  icy bodies belongs with the Kuiper belt in '
                             'the Solar System room.\n'
                             '**Gap:** not scoped -- design conversation '
                             'needed.\n'
                             '**Ref:** to_do_ideas.md (pre-ledger, '
                             '4/18/26).\n',
                             '  icy bodies belongs with the Kuiper belt in '
                             'the Solar System room.\n'
                             "- **2026-10-04, Tony's question on Where We "
                             'Are:** is this the fuzzy\n'
                             '  boundary idea? No. This item is a population '
                             'to draw as a region;\n'
                             '  L-410 is a way of drawing any edge known '
                             'only as a range. They meet\n'
                             "  in one place: the scattered disk's edges are "
                             'themselves ranges, so\n'
                             "  when this is designed, L-410's drawing rule "
                             'applies to it.\n'
                             '**Gap:** not scoped -- design conversation '
                             'needed.\n'
                             '**Ref:** to_do_ideas.md (pre-ledger, 4/18/26); '
                             'L-363 (the Solar System\n'
                             'room); L-410.\n',
                             1),
                            ('L-300: status line',
                             '<!-- L:300 status:OPEN upd:2026-09-07 '
                             'section:A flag: rice:3/3/90/1 -->',
                             '<!-- L:300 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice:3/3/90/1 -->',
                             1),
                            ('L-300: path corrected, placed',
                             '**Gap:** one small patch to '
                             '`gallery_maintenance_run.py` registering the\n'
                             'checker; then a run to confirm it appears in '
                             'the CHECKERS list with its\n'
                             'verdict line. Not yet written.\n'
                             '**Ref:** L-268, gallery '
                             '`tools/sweep_collapsed_features.py`,\n'
                             '`gallery_maintenance_run.py`.\n',
                             '- **2026-10-04.** The script is in the '
                             "gallery's ROOT folder, not\n"
                             "  `tools/` as the Ref said; the new row's "
                             'working folder is ".".\n'
                             '  Run on gallery e7ef96eb: exit 0, "33 stored '
                             'as themselves, 16\n'
                             '  collapsed, 0 unclassified" -- Earth\'s two '
                             "belts, Jupiter's three belts\n"
                             "  and four rings, Saturn's seven rings. So "
                             'registering it cannot turn\n'
                             "  the run red today. **Placed by Tony's order "
                             "of 2026-10-04 in Earth's\n"
                             '  website patch (L-413),** which ends with a '
                             'gallery maintenance run\n'
                             "  anyway; it adds the runner's file to that "
                             'patch.\n'
                             '**Gap:** one small patch to '
                             '`gallery_maintenance_run.py` registering the\n'
                             'checker; then a run to confirm it appears in '
                             'the CHECKERS list with its\n'
                             "verdict line. Rides L-413's website patch.\n"
                             '**Ref:** L-268, gallery '
                             '`sweep_collapsed_features.py` (root folder),\n'
                             '`gallery_maintenance_run.py`; L-413.\n',
                             1),
                            ('L-396: status line',
                             '<!-- L:396 status:OPEN upd:2026-10-01 '
                             'section:A flag: rice: -->',
                             '<!-- L:396 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice: -->',
                             1),
                            ('L-396: the stamp the check would read',
                             '**Gap:** the check above, or a ruling that the '
                             'skill rule is enough.\n',
                             '- **2026-10-04, before the check is built** '
                             '(Fable 5.1 ledger sweep):\n'
                             "  the ledger's header stamps lagged by three "
                             'sessions -- the last one\n'
                             "  was the lobby-card session's at a841ab6e, "
                             'and the L-406/L-407 pushes,\n'
                             '  the L-371 patches and the L-371 close added '
                             'none. A check comparing\n'
                             "  the page's date with the newest stamp would "
                             'then pass on a stale\n'
                             '  page. Either every ledger patch stamps the '
                             'header (patch_L413_1 does),\n'
                             '  or the check reads the newest `upd` field '
                             'instead.\n'
                             '**Gap:** the check above, or a ruling that the '
                             'skill rule is enough.\n',
                             1),
                            ('L-351: status line',
                             '<!-- L:351 status:OPEN upd:2026-09-28 '
                             'section:A flag: rice: -->',
                             '<!-- L:351 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice: -->',
                             1),
                            ('L-351: the one place for owed skill sentences',
                             "**Gap:** Each lands with its store's next "
                             'bump.\n'
                             '**Ref:** skills/interactive-exhibit/SKILL.md; '
                             'skills/ledger-and-session-records/SKILL.md; '
                             'PROJECT_INSTRUCTIONS.md.\n',
                             '- **2026-10-04: this item becomes the one '
                             'place** for what each skill\n'
                             '  is owed at its next version, so a session '
                             'bumping a skill reads one\n'
                             '  block, not five (Fable 5.1 ledger sweep; '
                             'method). Pointers by source\n'
                             '  handle; the sentence itself is in that '
                             'item:\n'
                             '  - gallery-cache-builder: the `[SWAP]` line, '
                             'the run order and the\n'
                             '    empty "(N)" folders (L-216).\n'
                             "  - provenance-discipline: the range rule's "
                             'example names a removed\n'
                             '    range row; a patch\'s "what the run should '
                             'say" predicts the\n'
                             "    scanner's CHANGE, not its total (both "
                             'L-371); the conversion marker\n'
                             "    and the widening (L-390); the scanner's "
                             'window and declared rows\n'
                             '    (L-414, if the fix is method there).\n'
                             "  - gallery-pipeline: the wide card's four "
                             "fields and the picture's\n"
                             '    tool (L-363).\n'
                             '  - ledger-and-session-records: a patch checks '
                             'files Tony annotates by\n'
                             '    the lines it edits, never by a whole-file '
                             'fingerprint (Tony,\n'
                             "    2026-10-03); and Tony's "
                             'documentation-folder practice (above).\n'
                             '  - interactive-exhibit and the protocol: as '
                             'above.\n'
                             "**Gap:** Each lands with its store's next "
                             'bump.\n'
                             '**Ref:** skills/interactive-exhibit/SKILL.md; '
                             'skills/ledger-and-session-records/SKILL.md; '
                             'PROJECT_INSTRUCTIONS.md; L-216, L-363, L-371, '
                             'L-390, L-414.\n',
                             1),
                            ('L-314: status line',
                             '<!-- L:314 status:OPEN upd:2026-09-12 '
                             'section:A flag: rice:3/3/60/4 -->',
                             '<!-- L:314 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice:3/3/60/4 -->',
                             1),
                            ('L-314: carries the aberration',
                             '**Gap:** the whole item; sequenced after L-305 '
                             'closes.\n',
                             '- **2026-10-04, re-homed from L-305 at its '
                             'close: the aberration.**\n'
                             '  Both fits are defined in aberrated frames: '
                             'because Earth moves along\n'
                             '  its orbit, the solar wind arrives slightly '
                             'from the side, and the\n'
                             '  nose turns by atan(v_orbit / v_sw), about '
                             '4.3 degrees at the declared\n'
                             '  400 km/s. Neither instrument applies it or '
                             'says it does not.\n'
                             '  **Tony-action (decide):** apply it, or draw '
                             'un-aberrated and say so\n'
                             '  in the hover. Here because the angle follows '
                             "the solar wind's speed.\n"
                             '**Gap:** the whole item, now that L-305 has '
                             'closed (2026-10-04); and\n'
                             "the aberration decision above. On Earth's list "
                             '(L-413), design talks.\n',
                             1),
                            ('L-181: status line',
                             '<!-- L:181 status:OPEN upd:2026-09-12 '
                             'section:A flag: rice:5/5/70/5 -->',
                             '<!-- L:181 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice:5/5/70/5 -->',
                             1),
                            ('L-181: L-383 folded in',
                             '(d) decide on the 124 dead tooltip fields. '
                             "L-184's build path cannot be\n"
                             'defined until this settles.\n',
                             '(d) decide on the 124 dead tooltip fields. '
                             "L-184's build path cannot be\n"
                             'defined until this settles. (2026-10-04: '
                             'L-383, the Earth\n'
                             "magnetosphere's tooltip copy, is folded in "
                             'here as one of the 124.)\n',
                             1),
                            ('L-292: status line',
                             '<!-- L:292 status:OPEN upd:2026-09-08 '
                             'section:A flag: rice:3/3/75/2 -->',
                             '<!-- L:292 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice:3/3/75/2 -->',
                             1),
                            ('L-292: the orrery half stands',
                             "**Gap:** the orrery's exosphere/geocorona "
                             'shell in\n'
                             "`SHELL_CONFIGS['Earth']` at "
                             '`EARTH_GEOCORONA_RADII`; the other two\n'
                             'when a build already has the file open.\n',
                             '- **2026-10-04, the orrery half is still '
                             'unbuilt** [verified @\n'
                             "  cbde99dc]: Earth's shells in "
                             '`shell_configs.py` are Inner Core, Outer\n'
                             '  Core, Lower Mantle, Upper Mantle, Crust, '
                             'Lower Atmosphere, Upper\n'
                             '  Atmosphere and Hill Sphere; the geocorona is '
                             'a sentence inside the\n'
                             "  Upper Atmosphere hover. The L-371 handoff's "
                             '"an exosphere shell\n'
                             '  naming the geocorona now exists" is the '
                             "website's row. Earth's list,\n"
                             '  item 1 (L-413).\n'
                             "**Gap:** the orrery's exosphere/geocorona "
                             'shell in\n'
                             "`SHELL_CONFIGS['Earth']` at "
                             '`EARTH_GEOCORONA_RADII`; the other two\n'
                             'when a build already has the file open. '
                             "L-413's orrery patch.\n",
                             1),
                            ('L-369: status line',
                             '<!-- L:369 status:OPEN upd:2026-09-28 '
                             'section:A flag: rice: -->',
                             '<!-- L:369 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice: -->',
                             1),
                            ('L-369: line numbers at HEAD',
                             '**Gap:** Point each at the store row; the '
                             'visitor text says "about 23.4" from the row.\n',
                             '- **2026-10-04, all five still typed** '
                             '[verified @ cbde99dc]:\n'
                             '  `palomas_orrery.py` lines 5842, 8073 and '
                             '8891; `star_sphere_builder.py`\n'
                             '  line 46; `coordinate_system_guide.py` line '
                             "441. Earth's list, item 2\n"
                             '  (L-413).\n'
                             '**Gap:** Point each at the store row; the '
                             'visitor text says "about 23.4" from the row.\n',
                             1),
                            ('L-131: status line',
                             '<!-- L:131 status:OPEN upd:2026-07-17 '
                             'section:D.Feature-B flag: rice:2/2/50/2 -->',
                             '<!-- L:131 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice:2/2/50/2 -->',
                             1),
                            ('L-131: in the active slice',
                             '**Gap:** not scoped -- design conversation '
                             'needed (extent, density\n'
                             'profile, data source), with L-410.\n',
                             '- **2026-10-04:** moved to section A; it is '
                             "the Sun slice's ninth\n"
                             '  item, with L-410 (L-412). Its July score was '
                             'set as a loose idea; a\n'
                             '  re-score is among the questions L-412 '
                             'records.\n'
                             '**Gap:** not scoped -- design conversation '
                             'needed (extent, density\n'
                             'profile, data source), with L-410.\n',
                             1),
                            ('L-128: status line',
                             '<!-- L:128 status:OPEN upd:2026-07-17 '
                             'section:D.Feature-B flag: rice:2/2/50/2 -->',
                             '<!-- L:128 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice:2/2/50/2 -->',
                             1),
                            ('L-386: status line',
                             '<!-- L:386 status:OPEN upd:2026-09-28 '
                             'section:A flag: rice: -->',
                             '<!-- L:386 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice: -->',
                             1),
                            ('L-241: status line',
                             '<!-- L:241 status:OPEN upd:2026-08-25 '
                             'section:A flag: rice:2/2/95/1 -->',
                             '<!-- L:241 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice:2/2/95/1 -->',
                             1),
                            ('L-308: status line',
                             '<!-- L:308 status:OPEN upd:2026-09-08 '
                             'section:A flag: rice:2/3/60/3 -->',
                             '<!-- L:308 status:DEFERRED upd:2026-10-04 '
                             'section:A flag: rice:2/3/60/3 -->',
                             1),
                            ('L-308: DEFERRED with its trigger',
                             '**Gap:** none until the trigger fires. Not a '
                             'design decision awaiting\n'
                             'Tony; an option with a stated condition.\n',
                             '**Gap:** none until the trigger fires. Not a '
                             'design decision awaiting\n'
                             'Tony; an option with a stated condition. '
                             '(2026-10-04: status OPEN ->\n'
                             'DEFERRED, so the index stops showing it as a '
                             'gap; the trigger above is\n'
                             'unchanged.)\n',
                             1),
                            ('L-375: status line',
                             '<!-- L:375 status:OPEN upd:2026-09-28 '
                             'section:A flag: rice: -->',
                             '<!-- L:375 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice: -->',
                             1),
                            ('L-375: the dipole cone on the website',
                             '**Gap:** Read the source; then decide how, or '
                             'whether, to show an offset that depends on a '
                             'rotation phase the orrery does not model.\n',
                             '- **2026-10-04, re-homed from L-234 at its '
                             'close:** the website does\n'
                             '  not draw the dipole cone at all; the orrery '
                             'does, as the swept\n'
                             '  envelope of every azimuth. No ruling against '
                             'drawing it on the\n'
                             '  website was found. Same question as the '
                             'offset: what to show when\n'
                             '  the instant depends on a rotation phase '
                             'neither instrument models.\n'
                             "  Earth's list, design talks (L-413).\n"
                             '**Gap:** Read the source; then decide how, or '
                             'whether, to show an offset that depends on a '
                             'rotation phase the orrery does not model; and '
                             'whether the website draws the cone.\n',
                             1),
                            ('L-367: status line',
                             '<!-- L:367 status:OPEN upd:2026-09-29 '
                             'section:A flag: rice: -->',
                             '<!-- L:367 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice: -->',
                             1),
                            ('L-367: lobby code re-homed',
                             '**Gap:** A check that lists `EXHIBITS` and '
                             'fails on a room no checker boots, or one smoke '
                             'that boots every room.\n',
                             '- **2026-10-04, re-homed from L-363:** no '
                             'gating checker reads\n'
                             "  `index.html`'s lobby code either (recorded "
                             'at the lobby card,\n'
                             '  2026-10-04). And this item is why the '
                             "gallery's checks come before\n"
                             "  the swap in Tony's order of 2026-10-04 "
                             '(L-412): the swap changes the\n'
                             '  front door.\n'
                             '**Gap:** A check that lists `EXHIBITS` and '
                             'fails on a room no checker boots, or one smoke '
                             'that boots every room; and something that '
                             'reads the lobby code.\n',
                             1),
                            ('L-330: status line',
                             '<!-- L:330 status:OPEN upd:2026-09-15 '
                             'section:A flag: rice:3/3/60/3 -->',
                             '<!-- L:330 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice:3/3/60/3 -->',
                             1),
                            ('L-330: unblocked',
                             '**Gap:** build L-231 first. Then a design '
                             'round on this, then a decision,\n'
                             'then both instruments in one pass.\n',
                             '- **2026-10-04:** L-231 is built for Earth '
                             '(its Gap now holds only\n'
                             "  Jupiter's belts), so this item's "
                             'prerequisite is met. First of\n'
                             "  Earth's design talks (L-413).\n"
                             '**Gap:** a design round, then a decision, then '
                             'both instruments in one\n'
                             'pass.\n',
                             1),
                            ('L-413 and L-414: opened',
                             "#### [L-412] The Sun's slice: the order Tony "
                             "confirmed (the Sun's slice)\n",
                             "#### [L-413] Earth's list: the old Earth "
                             'items, in the order Tony confirmed (Earth '
                             'room)\n'
                             '<!-- L:413 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice: -->\n'
                             '- **Confirmed by Tony, 2026-10-04,** after a '
                             'sweep of the open items\n'
                             '  that touch the Earth room, read against the '
                             'code at orrery cbde99dc\n'
                             '  and gallery e7ef96eb, and checked against '
                             'the Claude Fable 5.1 ledger\n'
                             '  sweep of the same day\n'
                             '  '
                             '(`documentation/LEDGER_SWEEP_review_20261004.md`). '
                             'It goes BEFORE the\n'
                             "  Sun slice's item 3 (L-412). It is the first "
                             'of the room-by-room\n'
                             '  ledger cleanups Tony asked for: items '
                             'grouped by the files the work\n'
                             '  opens, and only what the room shows is in '
                             'scope.\n'
                             "- **First, Tony's ruling:** L-349, the inner "
                             'belt\'s "where the measured\n'
                             '  particle flux peaks". Once ruled, its '
                             'wording rides both patches\n'
                             '  below.\n'
                             '- **The orrery patch** (`shell_configs.py`, '
                             '`constants_new.py`,\n'
                             '  `palomas_orrery.py`, '
                             '`star_sphere_builder.py`,\n'
                             '  `coordinate_system_guide.py`, '
                             '`earth_visualization_shells.py`):\n'
                             "  1. L-292, the orrery's geocorona shell at "
                             '`EARTH_GEOCORONA_RADII`. The\n'
                             "     GPS shell and Earth's Roche limit stay "
                             'parked in it.\n'
                             "  2. L-369, Earth's obliquity typed in five "
                             'places.\n'
                             '  3. L-389, the atmosphere shells measured '
                             'from the equatorial radius\n'
                             '     while the crust is drawn at the mean '
                             'radius, worked by\n'
                             "     provenance-discipline's rules.\n"
                             "  4. L-349's wording on the orrery side (and "
                             'the dead tooltip copy kept\n'
                             '     in step, L-181).\n'
                             "  Then Tony's look on screen (Mode 5).\n"
                             '- **The website patch** '
                             '(`gallery/feature_renderers.js`,\n'
                             '  `documentation/payload_earth_scene.json` and '
                             'the smoke suites that\n'
                             '  read it, `gallery_maintenance_run.py`):\n'
                             "  1. L-349's wording on the website.\n"
                             '  2. L-379, re-record the saved Earth scene '
                             'from the current cache; the\n'
                             '     overlays retire.\n'
                             '  3. L-300, register '
                             '`sweep_collapsed_features.py` in the '
                             'maintenance\n'
                             '     run (it passes today: 0 unclassified).\n'
                             "  Then Tony's look on the phone.\n"
                             "- **Tony's look, no build:** L-382, the "
                             "magnetosphere's cost per\n"
                             '  orrery animation frame, whenever he next '
                             'runs an Earth animation.\n'
                             '- **Design talks, in this order,** interleaved '
                             "with the Sun's list\n"
                             '  rather than blocking it:\n'
                             "  1. L-330, the belts' shape (unblocked: L-231 "
                             'is done for Earth).\n'
                             '  2. L-356 and L-375 together, IGRF-14 and the '
                             "dipole's offset, since\n"
                             '     both change the same field rows; L-375 '
                             'also carries whether the\n'
                             '     website draws the dipole cone (re-homed '
                             'from L-234).\n'
                             "  3. L-321, the orrery's Earth hover strings "
                             'into the cross-check.\n'
                             '  4. L-314, live solar wind, now carrying the '
                             'aberration decision\n'
                             '     (re-homed from L-305).\n'
                             '  5. L-297 and L-294, the Lagrange points and '
                             "Earth's heliocentric\n"
                             "     view, after Tony's ruling on the Explorer "
                             'room.\n'
                             '  6. L-374 and L-061, precession over time and '
                             'the seasonal roll:\n'
                             '     recorded ideas.\n'
                             '- **What the reading changed, against the '
                             "L-371 handoff's sweep:**\n"
                             '  L-305 closed (only the aberration was left, '
                             'now on L-314); L-350\n'
                             '  closed (the hover prints it); L-234 closed '
                             '(the Earth half is\n'
                             '  served); L-383 folded into L-181 (dead '
                             "data); L-231 is Jupiter's\n"
                             '  only; L-292 is still open in the orrery; '
                             'L-369 is five places, not\n'
                             '  four.\n'
                             '- **Not on this list:** the four Earth rows '
                             'the scanner scores Tier 1,\n'
                             '  which are a scanner question (L-414); L-001, '
                             'L-060 (the Earth System\n'
                             '  climate track), L-157, L-173, L-186, L-252 '
                             '(the cross-check\n'
                             '  programme), L-177 (Mercury), L-347, L-348, '
                             'L-360, L-367 (general\n'
                             '  checks).\n'
                             "**Gap:** Tony's ruling on L-349, then the "
                             'orrery patch, the website\n'
                             'patch, and the design talks in the order '
                             'above.\n'
                             "**Ref:** L-412 (the Sun's list, which resumes "
                             'after this); the handles\n'
                             'above; '
                             '`documentation/HANDOFF_L413_ledger_sweep_and_earth_list_20261004.md`.\n'
                             '\n'
                             '#### [L-414] The scanner misses a Source line '
                             'past its window, and scores declared rows as '
                             'uncited (provenance tooling)\n'
                             '<!-- L:414 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice: -->\n'
                             '- **Found 2026-10-04,** checking why '
                             '`constants_new.py` went from 0 to\n'
                             '  4 Tier-1 findings between mid-August and '
                             'now. The four rows are not\n'
                             '  uncited.\n'
                             '  - `EARTH_MEAN_RADIUS_KM` carries `# Source: '
                             'NASA Planetary Fact\n'
                             '    Sheet, Earth` -- 16 lines below the '
                             'assignment, after a Figures\n'
                             '    block that grew on 2026-09-19. The '
                             "scanner's constant context looks\n"
                             '    15 lines ahead (`get_context_block(..., '
                             'lookback=30,\n'
                             '    lookahead=15)`). Tested at cbde99dc: at 15 '
                             'the Source line is not\n'
                             '    in the context, at 16 it is.\n'
                             '  - `EARTH_SOLAR_WIND_PRESSURE_NPA`, `_BZ_NT` '
                             'and `_SPEED_KM_S` each\n'
                             '    carry `# Status: declared pending` and a '
                             '`# Declared:` reason (the\n'
                             "    speed's reason says plainly it is not yet "
                             'written). The scanner\n'
                             '    does not count a declared status as '
                             'provenance, and its name rules\n'
                             '    call them MEASURED.\n'
                             '- So the count rose for a reason that is not '
                             'about provenance -- A\n'
                             '  Check That Cannot Fail Is Not Passing, from '
                             'the other side: a check\n'
                             '  that fails on a cited row costs trust in '
                             'every finding.\n'
                             "- **Method, not Tony's:** whether to move "
                             'Source lines up, widen the\n'
                             '  window to the attached comment run, or teach '
                             'the scanner the declared\n'
                             "  status is provenance-discipline's to settle. "
                             'L-351 points here for\n'
                             "  that skill's next version.\n"
                             "**Gap:** the fix, by provenance-discipline's "
                             "method; then the scanner's\n"
                             'count for `constants_new.py` should name these '
                             'four as gone.\n'
                             '**Ref:** `provenance_scanner.py`; '
                             '`constants_new.py`;\n'
                             '`PROVENANCE_AUDIT.md`; L-305; L-314; L-351.\n'
                             '\n'
                             "#### [L-412] The Sun's slice: the order Tony "
                             "confirmed (the Sun's slice)\n",
                             1),
                            ('header stamp',
                             'd4b408e6; L-216: the stray folder again), '
                             'built on a841ab6e.\n',
                             'd4b408e6; L-216: the stray folder again), '
                             'built on a841ab6e.\n'
                             'Module updated: October 4, 2026 with '
                             "Anthropic's Claude Opus 5.5\n"
                             "(ledger sweep and Earth's list: L-413, L-414 "
                             'and L-415 opened; L-409,\n'
                             'L-407, L-350, L-406, L-305, L-234 closed; '
                             'L-383 folded into L-181;\n'
                             'safe-file-editing 1.12; with the Claude Fable '
                             '5.1 sweep of the same\n'
                             'day), built on 41c1ca7a. The three sessions '
                             'before this one added no\n'
                             'stamp; this one does not restate them.\n',
                             1),
                            ('L-415: opened',
                             "#### [L-413] Earth's list: the old Earth "
                             'items, in the order Tony confirmed (Earth '
                             'room)\n',
                             '#### [L-415] A patch writes LF and reports: '
                             'safe-file-editing 1.12 (skills)\n'
                             '<!-- L:415 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice: -->\n'
                             '- **Asked 2026-10-04** by Tony, after '
                             "patch_L413_1's test notes said a\n"
                             '  CRLF copy of the ledger kept its CRLF: "why '
                             'do we leave windows line\n'
                             '  endings uncorrected. I thought the rule was '
                             'to convert to lf when\n'
                             '  found and report." He was right about the '
                             'rule: LF is the standard\n'
                             "  (L-026, L-133), and safe-file-editing's Fix "
                             'In Passing lists "CRLF\n'
                             '  where the repo is LF" as a violation to fix. '
                             'Two other sections of\n'
                             '  the same skill, Line Endings Are Not Content '
                             'and Compare Content, Not\n'
                             '  Bytes, said to write each file back in the '
                             'style found, and that is\n'
                             '  what the patch followed. The skill disagreed '
                             'with itself.\n'
                             "- **The preserve rule's reason, tested.** It "
                             "said flipping a file's\n"
                             '  endings shows every line changed in a git '
                             'GUI. On a scratch repo with\n'
                             '  `* text=auto eol=lf`, the setting both of '
                             "this project's repos have\n"
                             '  [verified @ orrery 41c1ca7a, gallery '
                             'e7ef96eb]: a CRLF working copy\n'
                             '  shows as modified with an empty diff, and '
                             'writing it back LF clears\n'
                             '  the mark. The reason holds only for a file '
                             'whose COMMITTED copy is\n'
                             '  CRLF.\n'
                             '- **Tony\'s word, 2026-10-04:** "Yes", to '
                             'bumping the skill now under A\n'
                             '  Wrong Sentence in a Skill: Bump Now, or '
                             'Carry It -- a session\n'
                             '  following the old sentences writes CRLF '
                             'back.\n'
                             '- **Built in patch_L413_1:** safe-file-editing '
                             '1.11 -> 1.12 (a patch\n'
                             '  writes LF and reports; a file committed CRLF '
                             'keeps its endings, is\n'
                             "  named, and waits for L-133's sweep); "
                             'protocol v3.80. The patch itself\n'
                             '  follows the new rule.\n'
                             '- **The committed-CRLF files, measured** (`git '
                             'ls-files --eol`,\n'
                             '  `i/crlf`, at 41c1ca7a), 22: .gitignore, '
                             'catalog_selection.py, create_cache_backups.py, '
                             'data_acquisition.py, '
                             'data_acquisition_distance.py, '
                             'data_processing.py, formatting_utils.py, '
                             'hr_diagram_apparent_magnitude.py, '
                             'hr_diagram_distance.py, '
                             'messier_object_data_handler.py, '
                             'object_type_analyzer.py, '
                             'planetarium_apparent_magnitude.py, '
                             'planetarium_distance.py, report_manager.py, '
                             'shutdown_handler.py, star_notes.py, '
                             'star_properties.py, stellar_data_patches.py, '
                             'stellar_parameters.py, visualization_2d.py, '
                             'visualization_3d.py, visualization_core.py. '
                             "These are L-133's.\n"
                             '**Gap:** Tony reinstalls safe-file-editing '
                             '(Settings > Skills) and\n'
                             "replaces the Project's instructions with "
                             'v3.80. The next session\n'
                             'confirms its loaded copy reads 1.12 before any '
                             'patch work, then closes\n'
                             'this item.\n'
                             '**Ref:** skills/safe-file-editing/SKILL.md; '
                             'PROJECT_INSTRUCTIONS.md;\n'
                             'L-026; L-133; L-351.\n'
                             '\n'
                             "#### [L-413] Earth's list: the old Earth "
                             'items, in the order Tony confirmed (Earth '
                             'room)\n',
                             1),
                            ('L-133: status line',
                             '<!-- L:133 status:OPEN upd:2026-07-17 '
                             'section:D.Structural flag: rice:2/2/50/2 -->',
                             '<!-- L:133 status:OPEN upd:2026-10-04 '
                             'section:D.Structural flag: rice:2/2/50/2 -->',
                             1),
                            ('L-133: the 22 files named',
                             '**Gap:** narrower now -- a one-time sweep of '
                             'files already CRLF in the\n'
                             'repo from before this rule existed (the '
                             ".gitattributes fix doesn't\n"
                             "retroactively touch files it hasn't seen "
                             're-added).\n',
                             '- **2026-10-04, measured** (`git ls-files '
                             '--eol` at 41c1ca7a): 22\n'
                             '  files are still committed CRLF -- '
                             '.gitignore, catalog_selection.py, '
                             'create_cache_backups.py, data_acquisition.py, '
                             'data_acquisition_distance.py, '
                             'data_processing.py, formatting_utils.py, '
                             'hr_diagram_apparent_magnitude.py, '
                             'hr_diagram_distance.py, '
                             'messier_object_data_handler.py, '
                             'object_type_analyzer.py, '
                             'planetarium_apparent_magnitude.py, '
                             'planetarium_distance.py, report_manager.py, '
                             'shutdown_handler.py, star_notes.py, '
                             'star_properties.py, stellar_data_patches.py, '
                             'stellar_parameters.py, visualization_2d.py, '
                             'visualization_3d.py, visualization_core.py. '
                             'safe-file-editing 1.12 (L-415)\n'
                             '  makes a patch keep their endings and name '
                             'them here, so the sweep\n'
                             '  stays one commit of its own, as L-026 was.\n'
                             '**Gap:** narrower now -- a one-time sweep of '
                             'the 22 files above,\n'
                             'already CRLF in the repo from before this rule '
                             'existed (the\n'
                             ".gitattributes fix doesn't retroactively touch "
                             "files it hasn't seen\n"
                             're-added). One commit, nothing else in it.\n',
                             1)],
 'PROJECT_INSTRUCTIONS.md': [('header and anchor',
                              'Tony Quintanilla, PE | Claude | v3.79 | '
                              'October 2, 2026\n'
                              '\n'
                              'Cut from 0a5eea0b at '
                              'https://github.com/tonylquintanilla/palomas_orrery\n',
                              'Tony Quintanilla, PE | Claude | v3.80 | '
                              'October 4, 2026\n'
                              '\n'
                              'Cut from 41c1ca7a at '
                              'https://github.com/tonylquintanilla/palomas_orrery\n',
                              1),
                             ('v3.80 entry',
                              'v3.79 (October 2, 2026): No rule changed in '
                              'this document. TWO\n',
                              'v3.80 (October 4, 2026): No rule changed in '
                              'this document. ONE\n'
                              'skill bump, one version (L-415): '
                              'safe-file-editing 1.11 -> 1.12. A\n'
                              'PATCH WRITES LF AND SAYS SO.\n'
                              '\n'
                              "WHAT PROMPTED IT. A ledger patch's test notes "
                              'said a CRLF copy of the\n'
                              'ledger kept its CRLF. Tony: "why do we leave '
                              'windows line endings\n'
                              'uncorrected. I thought the rule was to '
                              'convert to lf when found and\n'
                              'report." The skill said both: Fix In Passing '
                              'lists CRLF as a violation\n'
                              'to fix, while Line Endings Are Not Content '
                              'and Compare Content, Not\n'
                              'Bytes said to write each file back in the '
                              'style found, because\n'
                              'flipping the endings shows every line '
                              'changed.\n'
                              '\n'
                              'WHAT THE TEST SHOWED. Under `* text=auto '
                              'eol=lf`, which both repos\n'
                              'carry, that reason is false: a CRLF working '
                              'copy shows as modified with\n'
                              'nothing inside it, and writing it LF clears '
                              'the mark. The reason holds\n'
                              'only for a file committed CRLF before the '
                              'rule existed; 22 such files\n'
                              'remain, named on L-133.\n'
                              '\n'
                              'WHAT THE SKILL NOW SAYS. A patch writes LF '
                              'and reports a file that\n'
                              'arrived CRLF. A file committed CRLF keeps its '
                              'endings, is named, and\n'
                              "waits for L-133's one-commit sweep. Patches "
                              'and generators now follow\n'
                              'the same convention.\n'
                              '\n'
                              'THE OBLIGATION TRAVELS. This session loaded '
                              '1.11. The next session\n'
                              'confirms its loaded copy reads '
                              'safe-file-editing 1.12 before any patch\n'
                              'work.\n'
                              '\n'
                              'The header stamp and the SHA anchor move with '
                              'this entry.\n'
                              '\n'
                              'Version history: v3.77 moves down to\n'
                              'documentation/PROJECT_INSTRUCTIONS_HISTORY.md '
                              'PART 1 to keep three\n'
                              'resident.\n'
                              '\n'
                              'v3.79 (October 2, 2026): No rule changed in '
                              'this document. TWO\n',
                              1),
                             ('v3.77 moved down',
                              'v3.77 (October 2, 2026): No rule changed in '
                              'this document. TWO\n'
                              'skill bumps, one version each, for one '
                              'session (L-405):\n'
                              'interactive-exhibit 1.8 -> 1.9 and '
                              'ledger-and-session-records 1.13 ->\n'
                              "1.14. THE SKILLS CATCH UP WITH THE SESSION'S "
                              'TWO BUILDS.\n'
                              '\n'
                              'WHAT PROMPTED IT. The session made the '
                              'Exhibit Store Editor list every\n'
                              'room (L-404) and built the Solar System '
                              "room's drawer (L-363 step 3b).\n"
                              'Tony then asked to sort what the session did '
                              'into method already in\n'
                              'the skills, method that needed a skill, and '
                              'drawing decisions and\n'
                              'judgement -- and, the review done, to "take '
                              'care of the skills now and\n'
                              'the numbers in the next session."\n'
                              '\n'
                              'WHAT THE SKILLS NOW SAY. interactive-exhibit '
                              'corrects its sentence that\n'
                              'every reader of objects_config.json ignores '
                              'the "rooms" section; says\n'
                              'what the store writer may change in a room '
                              'that is not one body, and\n'
                              'that the editor lists rooms from both places '
                              'a room can live; records\n'
                              "the Solar System room's drawer as the shared "
                              'drawer with four\n'
                              "additions, and Tony's framing ruling of "
                              '2026-10-02 -- where each body\n'
                              'is now, plus 20%; and gives step 4 the '
                              'headless test recipe, now filed\n'
                              "in the gallery's tools/headless/. "
                              'ledger-and-session-records gains A\n'
                              'Wrong Sentence in a Skill: Bump Now, or Carry '
                              'It. The test is what a\n'
                              'session would do if it followed the sentence: '
                              'something wrong means\n'
                              'correct it now, nothing different means carry '
                              'it on the ledger to the\n'
                              'next version.\n'
                              '\n'
                              'JUDGEMENT KEPT OUT OF THE SKILLS. Five calls '
                              'Claude made inside the\n'
                              'drawer build were put to Tony as his, and he '
                              'confirmed them. They are\n'
                              'recorded as his rulings on L-363, not written '
                              'as method.\n'
                              '\n'
                              'THE OBLIGATION TRAVELS. This session loaded '
                              '1.8 and 1.13. The next\n'
                              'session confirms its loaded copies read '
                              'interactive-exhibit 1.9 and\n'
                              'ledger-and-session-records 1.14 before any '
                              'exhibit, ledger, handoff or\n'
                              'session-record work.\n'
                              '\n'
                              'The header stamp and the SHA anchor move with '
                              'this entry.\n'
                              '\n'
                              'Version history: v3.74 moves down to\n'
                              'documentation/PROJECT_INSTRUCTIONS_HISTORY.md '
                              'PART 1 to keep three\n'
                              'resident.\n'
                              '\n',
                              '',
                              1)],
 'documentation/PROJECT_INSTRUCTIONS_HISTORY.md': [('v3.77 received',
                                                    '\n'
                                                    '================================================================\n'
                                                    'PART 2 -- LESSONS '
                                                    'REMOVED FROM THE '
                                                    'PROTOCOL AT v3.37\n',
                                                    '\n'
                                                    'v3.77 (October 2, '
                                                    '2026): No rule changed '
                                                    'in this document. TWO\n'
                                                    'skill bumps, one '
                                                    'version each, for one '
                                                    'session (L-405):\n'
                                                    'interactive-exhibit 1.8 '
                                                    '-> 1.9 and '
                                                    'ledger-and-session-records '
                                                    '1.13 ->\n'
                                                    '1.14. THE SKILLS CATCH '
                                                    "UP WITH THE SESSION'S "
                                                    'TWO BUILDS.\n'
                                                    '\n'
                                                    'WHAT PROMPTED IT. The '
                                                    'session made the '
                                                    'Exhibit Store Editor '
                                                    'list every\n'
                                                    'room (L-404) and built '
                                                    "the Solar System room's "
                                                    'drawer (L-363 step '
                                                    '3b).\n'
                                                    'Tony then asked to sort '
                                                    'what the session did '
                                                    'into method already in\n'
                                                    'the skills, method that '
                                                    'needed a skill, and '
                                                    'drawing decisions and\n'
                                                    'judgement -- and, the '
                                                    'review done, to "take '
                                                    'care of the skills now '
                                                    'and\n'
                                                    'the numbers in the next '
                                                    'session."\n'
                                                    '\n'
                                                    'WHAT THE SKILLS NOW '
                                                    'SAY. '
                                                    'interactive-exhibit '
                                                    'corrects its sentence '
                                                    'that\n'
                                                    'every reader of '
                                                    'objects_config.json '
                                                    'ignores the "rooms" '
                                                    'section; says\n'
                                                    'what the store writer '
                                                    'may change in a room '
                                                    'that is not one body, '
                                                    'and\n'
                                                    'that the editor lists '
                                                    'rooms from both places '
                                                    'a room can live; '
                                                    'records\n'
                                                    "the Solar System room's "
                                                    'drawer as the shared '
                                                    'drawer with four\n'
                                                    "additions, and Tony's "
                                                    'framing ruling of '
                                                    '2026-10-02 -- where '
                                                    'each body\n'
                                                    'is now, plus 20%; and '
                                                    'gives step 4 the '
                                                    'headless test recipe, '
                                                    'now filed\n'
                                                    "in the gallery's "
                                                    'tools/headless/. '
                                                    'ledger-and-session-records '
                                                    'gains A\n'
                                                    'Wrong Sentence in a '
                                                    'Skill: Bump Now, or '
                                                    'Carry It. The test is '
                                                    'what a\n'
                                                    'session would do if it '
                                                    'followed the sentence: '
                                                    'something wrong means\n'
                                                    'correct it now, nothing '
                                                    'different means carry '
                                                    'it on the ledger to '
                                                    'the\n'
                                                    'next version.\n'
                                                    '\n'
                                                    'JUDGEMENT KEPT OUT OF '
                                                    'THE SKILLS. Five calls '
                                                    'Claude made inside the\n'
                                                    'drawer build were put '
                                                    'to Tony as his, and he '
                                                    'confirmed them. They '
                                                    'are\n'
                                                    'recorded as his rulings '
                                                    'on L-363, not written '
                                                    'as method.\n'
                                                    '\n'
                                                    'THE OBLIGATION TRAVELS. '
                                                    'This session loaded 1.8 '
                                                    'and 1.13. The next\n'
                                                    'session confirms its '
                                                    'loaded copies read '
                                                    'interactive-exhibit 1.9 '
                                                    'and\n'
                                                    'ledger-and-session-records '
                                                    '1.14 before any '
                                                    'exhibit, ledger, '
                                                    'handoff or\n'
                                                    'session-record work.\n'
                                                    '\n'
                                                    'The header stamp and '
                                                    'the SHA anchor move '
                                                    'with this entry.\n'
                                                    '\n'
                                                    'Version history: v3.74 '
                                                    'moves down to\n'
                                                    'documentation/PROJECT_INSTRUCTIONS_HISTORY.md '
                                                    'PART 1 to keep three\n'
                                                    'resident.\n'
                                                    '\n'
                                                    '(Moved down from the '
                                                    'resident protocol on '
                                                    '2026-10-04 when\n'
                                                    'v3.80 made a fourth '
                                                    'entry.)\n'
                                                    '\n'
                                                    '================================================================\n'
                                                    'PART 2 -- LESSONS '
                                                    'REMOVED FROM THE '
                                                    'PROTOCOL AT v3.37\n',
                                                    1)],
 'skills/safe-file-editing/SKILL.md': [('version line',
                                        'Skill version: 1.11 | Cut from '
                                        'palomas_orrery @ 1fa413d9 (v1.11),\n'
                                        'earlier @ ccd1ac96 (v1.10), '
                                        'bfa9de2f (v1.9),\n',
                                        'Skill version: 1.12 | Cut from '
                                        'palomas_orrery @ 41c1ca7a (v1.12),\n'
                                        'earlier @ 1fa413d9 (v1.11), '
                                        'ccd1ac96 (v1.10), bfa9de2f '
                                        '(v1.9),\n',
                                        1),
                                       ('date and v1.12 paragraph',
                                        'bdaaa0c (v1.1) | August 29, 2026, '
                                        "with Anthropic's Claude Opus 5\n"
                                        'v1.11 (L-315) adds',
                                        'bdaaa0c (v1.1) | October 4, 2026, '
                                        "with Anthropic's Claude Opus 5.5\n"
                                        '(v1.12); August 29, 2026, with '
                                        "Anthropic's Claude Opus 5 (v1.11)\n"
                                        'v1.12 (L-415) makes the skill agree '
                                        'with itself about line endings.\n'
                                        'Fix In Passing listed "CRLF where '
                                        'the repo is LF" as a violation to\n'
                                        'fix, while Line Endings Are Not '
                                        'Content and Compare Content, Not '
                                        'Bytes\n'
                                        'told a patch to write each file '
                                        'back in the style it found. Tony '
                                        'asked\n'
                                        'why a patch was leaving Windows '
                                        'line endings in place: "I thought '
                                        'the\n'
                                        'rule was to convert to lf when '
                                        'found and report." The preserve '
                                        "rule's\n"
                                        'reason -- that flipping the endings '
                                        'shows every line changed -- was\n'
                                        'tested on 2026-10-04 and is false '
                                        'wherever the repo normalizes\n'
                                        '(`* text=auto eol=lf`, both of this '
                                        "project's repos): a CRLF working\n"
                                        'copy shows as modified with nothing '
                                        'inside it, and writing it LF '
                                        'clears\n'
                                        'that mark. It holds only for a file '
                                        'whose COMMITTED copy is CRLF. So a\n'
                                        'patch now writes LF and reports, '
                                        'except for those files.\n'
                                        'v1.11 (L-315) adds',
                                        1),
                                       ('Line Endings: write LF, except '
                                        'committed CRLF',
                                        "**Translate anchors to the file's "
                                        'own convention.** Anchors are '
                                        'written\n'
                                        'LF; a CRLF file matches none of '
                                        'them and the patch aborts on a file '
                                        'it\n'
                                        'could have edited safely. Detect '
                                        'per file and convert both sides:\n'
                                        '\n'
                                        '```python\n'
                                        "is_crlf = data.count(b'\\r\\n') > "
                                        '0\n'
                                        'if is_crlf:\n'
                                        "    old = old.replace(b'\\n', "
                                        "b'\\r\\n')\n"
                                        "    new = new.replace(b'\\n', "
                                        "b'\\r\\n')\n"
                                        '```\n'
                                        '\n'
                                        'Preserve what the file already uses '
                                        'rather than converting it. The '
                                        'patch\n'
                                        'is there to make one change, not to '
                                        'also silently restyle 11,000 '
                                        'lines.\n',
                                        '**Normalize, match, and write LF.** '
                                        'Anchors are written LF; a CRLF\n'
                                        'file matches none of them and the '
                                        'patch aborts on a file it could '
                                        'have\n'
                                        'edited safely. So read the file, '
                                        'turn CRLF into LF, match the LF '
                                        'anchors\n'
                                        'against that, and write the result '
                                        'as LF:\n'
                                        '\n'
                                        '```python\n'
                                        "raw = open(path, 'rb').read()\n"
                                        "was_crlf = b'\\r\\n' in raw\n"
                                        "text = raw.replace(b'\\r\\n', "
                                        "b'\\n')\n"
                                        '# ... edits against LF anchors ...\n'
                                        'open(path, '
                                        "'wb').write(text)          # LF, "
                                        "the repo's convention\n"
                                        'if was_crlf:\n'
                                        "    print('note: %s was CRLF in the "
                                        "working copy; written LF' % path)\n"
                                        '```\n'
                                        '\n'
                                        'This is Fix In Passing applied to '
                                        'line endings, and it is the '
                                        'default\n'
                                        '(1.12). In a repo with `* text=auto '
                                        "eol=lf` -- both of this project's "
                                        '--\n'
                                        'git stores LF whatever the working '
                                        'copy holds. A CRLF working copy\n'
                                        'therefore shows in GitHub Desktop '
                                        'as modified with no change inside '
                                        'it,\n'
                                        'and writing it LF clears that false '
                                        'mark rather than creating a diff.\n'
                                        'Tested 2026-10-04 on a scratch '
                                        'repository with the same setting.\n'
                                        '\n'
                                        '**The exception: a file whose '
                                        'COMMITTED copy is CRLF.** Some '
                                        'files went\n'
                                        'in before the normalizing rule '
                                        'existed, and git still holds them '
                                        'CRLF\n'
                                        '(`git ls-files --eol` shows '
                                        '`i/crlf`). Writing one of those LF '
                                        'changes\n'
                                        'the ending of every line in the '
                                        'commit, which buries the edit that\n'
                                        'matters. The patch author checks at '
                                        'build time, from the repo pull;\n'
                                        'for such a file the patch keeps '
                                        'CRLF, says so, and names the file '
                                        'as\n'
                                        'one for the one-time sweep, done as '
                                        'a commit of its own. In this '
                                        'project\n'
                                        'that sweep is L-133. The test is '
                                        'the committed copy, never the '
                                        'working\n'
                                        'copy -- a CRLF working copy alone '
                                        'is not this case.\n',
                                        1),
                                       ('Guard section: patches and '
                                        'generators agree',
                                        '**The asymmetry with Line Endings '
                                        'Are Not Content is deliberate.** A\n'
                                        'PATCH preserves what the file '
                                        'already uses, because it is there '
                                        'to make\n'
                                        'one change and not to restyle '
                                        '11,000 lines. A GENERATOR that '
                                        'rewrites the\n'
                                        "whole file holds the repo's "
                                        'convention, because rewriting the '
                                        'file IS the\n'
                                        'job. Do not "fix" either one to '
                                        'match the other.\n',
                                        '**Patches and generators now agree '
                                        "(1.12).** Both write the repo's\n"
                                        'convention, LF. The earlier wording '
                                        'called it a deliberate asymmetry,\n'
                                        'with patches preserving what they '
                                        'found; that rested on the\n'
                                        'every-line-changed claim Line '
                                        'Endings Are Not Content now '
                                        'corrects. The\n'
                                        'one exception, a file committed '
                                        "CRLF, is the patch author's to "
                                        'spot\n'
                                        'there.\n',
                                        1),
                                       ('Compare Content: write LF',
                                        'write each file back in the '
                                        'line-ending style you found it '
                                        'in.\n',
                                        'write it back as LF (1.12; the one '
                                        'exception is in Line Endings Are\n'
                                        'Not Content).\n',
                                        1),
                                       ('Compare Content: code',
                                        'final = out.replace(b"\\n", '
                                        'b"\\r\\n") if was_crlf else out\n',
                                        'final = out                       # '
                                        'LF; report was_crlf, never hide '
                                        'it\n',
                                        1),
                                       ('Compare Content: the corrected '
                                        'paragraph',
                                        '**Preserve the style on write.** '
                                        "Flipping a 700 KB file's line\n"
                                        'endings shows in a git GUI as every '
                                        'line changed, which buries the\n'
                                        'eight edits that actually matter. '
                                        'This half is not cosmetic: a diff\n'
                                        'nobody can read is a diff nobody '
                                        'reviews.\n',
                                        '**Write LF, and say so (corrected '
                                        '1.12).** This paragraph used to '
                                        'say\n'
                                        '"preserve the style on write", '
                                        "because flipping a 700 KB file's "
                                        'line\n'
                                        'endings would show every line '
                                        'changed and bury the eight edits '
                                        'that\n'
                                        'matter. Under `* text=auto eol=lf` '
                                        'that does not happen: git compares\n'
                                        'normalized content, so the edits '
                                        'are all a reviewer sees. It does\n'
                                        'happen for a file COMMITTED CRLF, '
                                        'which is why that one case keeps '
                                        'its\n'
                                        'endings until its own sweep. A diff '
                                        'nobody can read is still a diff\n'
                                        'nobody reviews; the rule now '
                                        'protects that where it is actually '
                                        'at\n'
                                        'risk.\n',
                                        1)]}

WHOLE_FILES = {'documentation/WHERE_WE_ARE.md': (['6104feabc31a900097c65846cd126af7'],
                                   '<!-- Doc-Kind: hand | Where the project '
                                   'is and where it is going, in plain '
                                   'words. One file, rewritten in place; '
                                   'read it at the end of every session. '
                                   '-->\n'
                                   '# Where We Are\n'
                                   '\n'
                                   'Last updated: October 4, 2026, end of '
                                   "the day's third session.\n"
                                   '- Written at orrery 41c1ca7a and gallery '
                                   'e7ef96eb.\n'
                                   '- This session was a ledger sweep: no '
                                   'code changed. A Fable session\n'
                                   '  ran its own sweep beside it, and both '
                                   'were checked against the code.\n'
                                   '\n'
                                   '> **READ THIS FIRST**\n'
                                   '>\n'
                                   '> **Changed this session:**\n'
                                   "> - Earth's old items are now one "
                                   'ordered list, in the order you\n'
                                   '>   confirmed. They come before the rest '
                                   "of the Sun's list.\n"
                                   '> - Seven ledger items closed because '
                                   'their work was already done: the\n'
                                   '>   licenses, the skill-header check, '
                                   'the galactic tide, the\n'
                                   ">   magnetotail's length, Earth's "
                                   'magnetosphere model, Earth in the\n'
                                   ">   website's builder, and the "
                                   "magnetosphere's unused tooltip copy.\n"
                                   '> - The four Earth numbers the scanner '
                                   'calls uncited are cited. The\n'
                                   '>   scanner looks one line short of one '
                                   "source, and doesn't count a\n"
                                   '>   written "declared" reason. That is '
                                   'now its own item.\n'
                                   '> - Your notes on this page are in the '
                                   'ledger, so they survive this\n'
                                   '>   rewrite.\n'
                                   '> - Patches now convert Windows line '
                                   'endings to the standard LF and say\n'
                                   '>   so, as you remembered the rule. The '
                                   'patch skill had said both.\n'
                                   '>\n'
                                   '> **Do next:**\n'
                                   "> - *Your ruling on the inner belt's "
                                   "wording, then Earth's orrery\n"
                                   '>   patch.*\n'
                                   '>\n'
                                   '> **Needs you now:**\n'
                                   '> - *Run the ledger patch, then the '
                                   'maintenance run, and push.*\n'
                                   '> - *Reinstall the patch skill and '
                                   "update the Project's instructions.*\n"
                                   '\n'
                                   'How to read the marks:\n'
                                   '- *Italic* lines are the must-reads.\n'
                                   '- **>> UPDATED THIS SESSION** beside a '
                                   'heading means that section\n'
                                   '  changed in the latest session.\n'
                                   '- "<< new this session" beside a road '
                                   'stage marks a change to the road.\n'
                                   '- Sections without a mark are as they '
                                   'were.\n'
                                   '- The marks are cleared and reset at '
                                   "every session's update, so they\n"
                                   '  always mean "new since you last read '
                                   'this."\n'
                                   '\n'
                                   '## The goal\n'
                                   '\n'
                                   "- Paloma's Orrery on the web.\n"
                                   '- The website does what the desktop '
                                   'orrery does, in the browser, from\n'
                                   '  data fetched from JPL each night, so a '
                                   'visitor never waits on JPL.\n'
                                   '- Anyone can open it, with nothing to '
                                   'install.\n'
                                   '- Built from the same code and the same '
                                   'checked numbers as the desktop\n'
                                   '  orrery.\n'
                                   '- The one real limit: the browser can '
                                   'show only the dates the saved\n'
                                   '  data covers.\n'
                                   '- Saved data covering one orbit of each '
                                   'body is enough, as you decided.\n'
                                   '- Within that range, a visitor will be '
                                   'able to choose a date, and\n'
                                   '  perhaps play time forward.\n'
                                   '\n'
                                   '## The road  **>> UPDATED THIS '
                                   'SESSION**\n'
                                   '\n'
                                   "  1. [done]   The Sun's room is live on "
                                   'the website.\n'
                                   "  2. [done]   Earth's room is live, with "
                                   'every number traced to its source.\n'
                                   '  3. [done]   The numbers come from one '
                                   'place: the orrery feeds the\n'
                                   '              website, and nothing is '
                                   'typed twice.\n'
                                   '  4. [done]   The Solar System room '
                                   'becomes a second way in: all the\n'
                                   '              planets, a drawer to pick '
                                   'them, and a way into each\n'
                                   "              body's own room.\n"
                                   "  5. [NOW]    *Earth's old items are "
                                   'finished, in the order you\n'
                                   '              confirmed.* << new this '
                                   'session: the first of the\n'
                                   '              room-by-room ledger '
                                   "cleanups you asked for. Each room's\n"
                                   '              old items are grouped by '
                                   'the files the work opens, and\n'
                                   '              only what the room shows '
                                   'is in scope.\n'
                                   "  6. [next]   The Sun's numbers get the "
                                   "same checking Earth's got: the\n"
                                   "              Sun's list, from its "
                                   'opening view. << moved this session:\n'
                                   "              after Earth's list. The "
                                   'distance cards are done.\n'
                                   "  7. [next]   The website's checks get a "
                                   'short list of their own, so a\n'
                                   '              new room or a moved front '
                                   "door can't break unnoticed.\n"
                                   '              << new this session.\n'
                                   '  8. [next]   A bare interactive.html '
                                   'link opens the Solar System room,\n'
                                   '              and the Explorer gets its '
                                   "own address. The lobby's wide\n"
                                   '              Solar System card, its '
                                   'first half, is done.\n'
                                   "  9. [later]  The rest of the orrery's "
                                   'objects come to the website --\n'
                                   '              dwarf planets, asteroids, '
                                   'moons -- through the same\n'
                                   '              connection that now '
                                   "carries the room's eleven bodies,\n"
                                   '              checked against JPL '
                                   'Horizons.\n'
                                   ' 10. [later]  Encounters: comets and '
                                   'spacecraft shown at the dates\n'
                                   '              that matter.\n'
                                   ' 11. [later]  The planets get their '
                                   'details -- layers, rings, magnetic\n'
                                   '              fields -- Jupiter and '
                                   'Saturn first.\n'
                                   ' 12. [goal]   The website does what the '
                                   'desktop orrery does, from data\n'
                                   '              fetched from JPL each '
                                   'night, with a date to choose and\n'
                                   '              time to play within the '
                                   'range the data covers.\n'
                                   '\n'
                                   '## Right now  **>> UPDATED THIS '
                                   'SESSION**\n'
                                   '\n'
                                   "- Earth's magnetosphere is drawn from "
                                   'published models in both the\n'
                                   '  orrery and the website.\n'
                                   '  - One question was never answered: '
                                   'because Earth moves along its\n'
                                   '    orbit, the solar wind hits it '
                                   'slightly from the side, so the nose\n'
                                   '    should turn about 4 degrees. Neither '
                                   'drawing does, and neither says\n'
                                   '    so. It now waits with live solar '
                                   'wind, which sets that angle.\n'
                                   "- The website draws Earth's geocorona, "
                                   'its faint hydrogen halo. The\n'
                                   '  orrery only mentions it in a hover; '
                                   "drawing it is Earth's list, item 1.\n"
                                   "- The website's magnetotail hover "
                                   'already prints the 220 Earth radii\n'
                                   '  the spacecraft reached.\n'
                                   "- The website does not draw Earth's "
                                   'magnetic dipole cone; the orrery\n'
                                   '  does. Whether the website should is '
                                   'now a design question.\n'
                                   '- On the Sun: the distance cards are '
                                   'built on both sites, and the\n'
                                   '  Roche limit is drawn at 3.45 solar '
                                   'radii, described as "about 3".\n'
                                   '- The ledger holds 241 open items after '
                                   'the seven closes.\n'
                                   '\n'
                                   '## The next three steps  **>> UPDATED '
                                   'THIS SESSION**\n'
                                   '\n'
                                   "1. *Your ruling on the inner belt's "
                                   'wording.*\n'
                                   '   - It says "where the measured '
                                   'particle flux peaks".\n'
                                   '   - Once you rule, the new wording '
                                   'travels in both patches below.\n'
                                   "2. Earth's orrery patch, then your look "
                                   'on the screen.\n'
                                   '   - The geocorona drawn as its own '
                                   'shell.\n'
                                   "   - Earth's tilt read from the stored "
                                   'number in five places.\n'
                                   '   - The atmosphere shells measured from '
                                   'the same radius as the crust.\n'
                                   "3. Earth's website patch, then your look "
                                   'on the phone.\n'
                                   "   - The inner belt's wording.\n"
                                   '   - The saved Earth test scene '
                                   "re-recorded from today's data.\n"
                                   '   - The collapsed-features check added '
                                   'to the maintenance run. It\n'
                                   '     passes today, so it cannot block a '
                                   'push.\n'
                                   '\n'
                                   '## Waiting on you  **>> UPDATED THIS '
                                   'SESSION**\n'
                                   '\n'
                                   'Now:\n'
                                   '- Run the ledger patch, then '
                                   'orrery_maintenance_run.py, and push.\n'
                                   '- Reinstall safe-file-editing in '
                                   'Settings > Skills, and replace the\n'
                                   "  Project's instructions with "
                                   'PROJECT_INSTRUCTIONS.md, now v3.80.\n'
                                   '- Later, not urgent: 22 older files are '
                                   'still stored with Windows line\n'
                                   '  endings. Converting them is one commit '
                                   'of its own, whenever you like.\n'
                                   '\n'
                                   'At the next design talk:\n'
                                   '- The fuzzy outer corona, designed '
                                   'together with the dust cloud.\n'
                                   '- Moving the highlighted row to the top '
                                   'of the list.\n'
                                   "- GO's arrow, only if the text box stays "
                                   'in the centre, as you ruled.\n'
                                   "  If it can't, no arrow.\n"
                                   "- Earth's design talks, the belts' shape "
                                   'first.\n'
                                   '\n'
                                   'Decisions from the Fable sweep, one at a '
                                   "time when you're ready:\n"
                                   '- Whether items inside an ordered list '
                                   'need RICE scores at all.\n'
                                   '- A handful of scores it proposes.\n'
                                   '\n'
                                   'Not urgent, in your order:\n'
                                   "1. The full check of the orrery's object "
                                   'list against JPL Horizons.\n'
                                   '2. Whether the editor should also edit '
                                   'the words on the Solar System\n'
                                   "   room's rows.\n"
                                   '3. Choosing a date, and animation.\n'
                                   '4. The scattered disk, with the Kuiper '
                                   'belt in the Solar System room.\n'
                                   '   It is not the fuzzy boundary idea: '
                                   'the disk is a population of icy\n'
                                   '   bodies, the fuzzy boundary is a way '
                                   'of drawing an edge. When the\n'
                                   '   disk is designed, its edges would '
                                   'likely be drawn that way.\n'
                                   '\n'
                                   '## Where the details are  **>> UPDATED '
                                   'THIS SESSION**\n'
                                   '\n'
                                   '- Every item, done and open: '
                                   '`LEDGER_CONSOLIDATED.md`\n'
                                   "  - This session: L-413 (Earth's list), "
                                   "L-414 (the scanner's window),\n"
                                   '    L-415 (line endings), L-133 (the 22 '
                                   'older files).\n'
                                   '    Closed: L-409, L-407, L-350, L-406, '
                                   'L-305, L-234, L-383.\n'
                                   "  - The Sun's list: L-412.\n"
                                   '- The reasoning behind the order:\n'
                                   '  '
                                   '`documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`\n'
                                   '- The latest session records:\n'
                                   '  '
                                   '`documentation/HANDOFF_L413_ledger_sweep_and_earth_list_20261004.md`,\n'
                                   "  and Fable's sweep, "
                                   '`documentation/LEDGER_SWEEP_review_20261004.md`\n')}

NEW_FILES = {'documentation/HANDOFF_L413_ledger_sweep_and_earth_list_20261004.md': '<!-- '
                                                                       'Doc-Kind: '
                                                                       'hand '
                                                                       '| '
                                                                       'Session '
                                                                       'record: '
                                                                       'the '
                                                                       'ledger '
                                                                       'sweep '
                                                                       'of '
                                                                       '2026-10-04 '
                                                                       'and '
                                                                       "Earth's "
                                                                       'list '
                                                                       '(L-413). '
                                                                       '-->\n'
                                                                       '# '
                                                                       'Handoff: '
                                                                       'the '
                                                                       'ledger '
                                                                       'sweep '
                                                                       'and '
                                                                       "Earth's "
                                                                       'list '
                                                                       '(L-413)\n'
                                                                       '\n'
                                                                       'Built '
                                                                       'on '
                                                                       'orrery '
                                                                       '41c1ca7a175992248dad9cc3237686beab032f82 '
                                                                       'at\n'
                                                                       'https://github.com/tonylquintanilla/palomas_orrery '
                                                                       '(read '
                                                                       'first '
                                                                       'at\n'
                                                                       'cbde99dc; '
                                                                       '41c1ca7a '
                                                                       'is '
                                                                       "Tony's "
                                                                       'push '
                                                                       'of '
                                                                       'his '
                                                                       'notes '
                                                                       'and '
                                                                       "Fable's "
                                                                       'sweep, '
                                                                       'with\n'
                                                                       'the '
                                                                       'ledger '
                                                                       'unchanged), '
                                                                       'and '
                                                                       'gallery\n'
                                                                       'e7ef96eb07fbdede9a270965d216511eb4949043 '
                                                                       'at\n'
                                                                       'https://github.com/tonylquintanilla/tonyquintanilla.github.io '
                                                                       '(read\n'
                                                                       'only; '
                                                                       'nothing '
                                                                       'in '
                                                                       'the '
                                                                       'gallery '
                                                                       'changes). '
                                                                       'Pushed '
                                                                       'at: '
                                                                       "Tony's "
                                                                       'push '
                                                                       'of\n'
                                                                       'patch_L413_1.\n'
                                                                       '\n'
                                                                       '- '
                                                                       'Type: '
                                                                       'DOCUMENTATION '
                                                                       '(ledger, '
                                                                       'one '
                                                                       'skill, '
                                                                       'the '
                                                                       'protocol; '
                                                                       'zero '
                                                                       'code).\n'
                                                                       '- '
                                                                       'Supersedes: '
                                                                       '`documentation/HANDOFF_L371_distance_cards_session_20261004.md`\n'
                                                                       '  as '
                                                                       'the '
                                                                       'latest '
                                                                       'record.\n'
                                                                       '- '
                                                                       'Companion: '
                                                                       '`documentation/LEDGER_SWEEP_review_20261004.md`, '
                                                                       'a\n'
                                                                       '  '
                                                                       'Claude '
                                                                       'Fable '
                                                                       '5.1 '
                                                                       'sweep '
                                                                       'of '
                                                                       'the '
                                                                       'same '
                                                                       'ledger '
                                                                       'the '
                                                                       'same '
                                                                       'evening, '
                                                                       'carried\n'
                                                                       '  in '
                                                                       'and '
                                                                       'pushed '
                                                                       'by '
                                                                       'Tony '
                                                                       'at '
                                                                       '41c1ca7a.\n'
                                                                       '- '
                                                                       'Skills '
                                                                       'loaded: '
                                                                       'ledger-and-session-records '
                                                                       '1.14, '
                                                                       'safe-file-editing\n'
                                                                       '  '
                                                                       '1.11. '
                                                                       'Both '
                                                                       'matched '
                                                                       'the '
                                                                       'manifest. '
                                                                       'safe-file-editing '
                                                                       'went '
                                                                       'to '
                                                                       '1.12 '
                                                                       'in\n'
                                                                       '  '
                                                                       'this '
                                                                       'session '
                                                                       '(L-415), '
                                                                       'so '
                                                                       'the '
                                                                       'next '
                                                                       'session '
                                                                       'confirms '
                                                                       'its '
                                                                       'loaded '
                                                                       'copy\n'
                                                                       '  '
                                                                       'reads '
                                                                       '1.12 '
                                                                       'before '
                                                                       'any '
                                                                       'patch '
                                                                       'work.\n'
                                                                       '\n'
                                                                       '## '
                                                                       'What '
                                                                       'was '
                                                                       'done '
                                                                       '[verified '
                                                                       '@ '
                                                                       'orrery '
                                                                       'cbde99dc, '
                                                                       'gallery '
                                                                       'e7ef96eb]\n'
                                                                       '\n'
                                                                       '1. '
                                                                       'Confirmed '
                                                                       'the '
                                                                       'L-371 '
                                                                       'close '
                                                                       'patches '
                                                                       'landed '
                                                                       '(orrery '
                                                                       'cbde99dc, '
                                                                       'gallery\n'
                                                                       '   '
                                                                       'e7ef96eb; '
                                                                       'maintenance '
                                                                       'run '
                                                                       '20 '
                                                                       'of '
                                                                       '20) '
                                                                       'and '
                                                                       'that '
                                                                       'the '
                                                                       'uploaded '
                                                                       'handoffs\n'
                                                                       '   '
                                                                       'match '
                                                                       'the '
                                                                       'repo '
                                                                       'apart '
                                                                       'from '
                                                                       "Tony's "
                                                                       'run '
                                                                       'notes.\n'
                                                                       '2. '
                                                                       'Read '
                                                                       'the '
                                                                       'Earth '
                                                                       'items '
                                                                       'the '
                                                                       'L-371 '
                                                                       'handoff '
                                                                       'named '
                                                                       'against '
                                                                       'the '
                                                                       'code, '
                                                                       'then\n'
                                                                       '   '
                                                                       'checked '
                                                                       'the '
                                                                       'Fable '
                                                                       "sweep's "
                                                                       'claims '
                                                                       'where '
                                                                       'they '
                                                                       'were '
                                                                       'cheap '
                                                                       'to '
                                                                       'check.\n'
                                                                       '3. '
                                                                       'Wrote '
                                                                       "Earth's "
                                                                       'list '
                                                                       'as '
                                                                       'L-413 '
                                                                       'in '
                                                                       'the '
                                                                       'order '
                                                                       'Tony '
                                                                       'confirmed, '
                                                                       'opened\n'
                                                                       '   '
                                                                       'L-414 '
                                                                       'for '
                                                                       'the '
                                                                       'scanner '
                                                                       'finding, '
                                                                       'closed '
                                                                       'seven '
                                                                       'items, '
                                                                       'corrected '
                                                                       'the\n'
                                                                       '   '
                                                                       'rest, '
                                                                       'and '
                                                                       'rewrote '
                                                                       'Where '
                                                                       'We '
                                                                       'Are.\n'
                                                                       '4. '
                                                                       'On '
                                                                       "Tony's "
                                                                       'question '
                                                                       'why '
                                                                       'a '
                                                                       'patch '
                                                                       'kept '
                                                                       'Windows '
                                                                       'line '
                                                                       'endings, '
                                                                       'found '
                                                                       'the\n'
                                                                       '   '
                                                                       'skill '
                                                                       'disagreeing '
                                                                       'with '
                                                                       'itself, '
                                                                       'tested '
                                                                       'its '
                                                                       'reason, '
                                                                       'and '
                                                                       'bumped\n'
                                                                       '   '
                                                                       'safe-file-editing '
                                                                       'to '
                                                                       '1.12 '
                                                                       'with '
                                                                       'protocol '
                                                                       'v3.80 '
                                                                       '(L-415). '
                                                                       'Counted '
                                                                       'the\n'
                                                                       '   '
                                                                       '22 '
                                                                       'files '
                                                                       'still '
                                                                       'committed '
                                                                       'CRLF '
                                                                       'onto '
                                                                       'L-133.\n'
                                                                       '\n'
                                                                       '## '
                                                                       "Tony's "
                                                                       'rulings '
                                                                       'and '
                                                                       'confirmations\n'
                                                                       '\n'
                                                                       '- '
                                                                       'The '
                                                                       'order '
                                                                       'of '
                                                                       'the '
                                                                       'backlog: '
                                                                       "Earth's "
                                                                       'list '
                                                                       'first '
                                                                       '(L-413), '
                                                                       'then '
                                                                       'the '
                                                                       "Sun's\n"
                                                                       '  '
                                                                       'list '
                                                                       'from '
                                                                       'item '
                                                                       '3 '
                                                                       '(L-412), '
                                                                       'then '
                                                                       'the '
                                                                       "gallery's "
                                                                       'checks '
                                                                       'as a '
                                                                       'short '
                                                                       'list,\n'
                                                                       '  '
                                                                       'then '
                                                                       'the '
                                                                       'swap '
                                                                       '(L-363). '
                                                                       'The '
                                                                       'checks '
                                                                       'precede '
                                                                       'the '
                                                                       'swap '
                                                                       'because '
                                                                       'one '
                                                                       'of\n'
                                                                       '  '
                                                                       'them '
                                                                       '(L-367) '
                                                                       'is '
                                                                       'that '
                                                                       'no '
                                                                       'checker '
                                                                       'boots '
                                                                       'a '
                                                                       'new '
                                                                       'room.\n'
                                                                       '- '
                                                                       'Ledger '
                                                                       'cleanup '
                                                                       'becomes '
                                                                       'a '
                                                                       'standing '
                                                                       'step '
                                                                       'in '
                                                                       'the '
                                                                       'road, '
                                                                       'room '
                                                                       'by '
                                                                       'room,\n'
                                                                       '  '
                                                                       'under '
                                                                       'The '
                                                                       'Braid '
                                                                       'and '
                                                                       'Cluster '
                                                                       'the '
                                                                       'Tail '
                                                                       'by '
                                                                       'Files '
                                                                       'Touched.\n'
                                                                       '- '
                                                                       'L-300 '
                                                                       'rides '
                                                                       "Earth's "
                                                                       'website '
                                                                       'patch.\n'
                                                                       '- '
                                                                       'safe-file-editing: '
                                                                       'bump '
                                                                       'now, '
                                                                       'so a '
                                                                       'patch '
                                                                       'writes '
                                                                       'LF '
                                                                       'and '
                                                                       'reports '
                                                                       '(L-415).\n'
                                                                       '- '
                                                                       "GO's "
                                                                       'arrow: '
                                                                       '"the '
                                                                       'text '
                                                                       'box '
                                                                       'needs '
                                                                       'to '
                                                                       'remain '
                                                                       'in '
                                                                       'the '
                                                                       'center. '
                                                                       'if '
                                                                       'not\n'
                                                                       '  '
                                                                       'possible, '
                                                                       "don't "
                                                                       'implement '
                                                                       'the '
                                                                       'arrow." '
                                                                       '(L-363)\n'
                                                                       '- '
                                                                       'The '
                                                                       'close '
                                                                       'patches '
                                                                       'and '
                                                                       'the '
                                                                       'stray '
                                                                       'folder: '
                                                                       'done '
                                                                       '(L-216).\n'
                                                                       '\n'
                                                                       '## '
                                                                       'Closed, '
                                                                       'each '
                                                                       'with '
                                                                       'its '
                                                                       'evidence '
                                                                       'in '
                                                                       'its '
                                                                       'block\n'
                                                                       '\n'
                                                                       '- '
                                                                       'L-409 '
                                                                       '(both '
                                                                       'GitHub '
                                                                       'sidebars '
                                                                       'say '
                                                                       '"MIT '
                                                                       'license"; '
                                                                       "Fable's "
                                                                       'read).\n'
                                                                       '- '
                                                                       'L-407 '
                                                                       "(Fable's "
                                                                       'session '
                                                                       'loaded '
                                                                       '1.10, '
                                                                       '1.2 '
                                                                       'and '
                                                                       '2.25).\n'
                                                                       '- '
                                                                       'L-350 '
                                                                       '(the '
                                                                       'magnetotail '
                                                                       'hover '
                                                                       'prints '
                                                                       'the '
                                                                       '220 '
                                                                       'Earth '
                                                                       'radii).\n'
                                                                       '- '
                                                                       'L-406 '
                                                                       '(built; '
                                                                       'its '
                                                                       'look '
                                                                       'is '
                                                                       "L-408's "
                                                                       'purpose).\n'
                                                                       '- '
                                                                       'L-305 '
                                                                       '(both '
                                                                       'instruments '
                                                                       'draw '
                                                                       'Shue '
                                                                       'and '
                                                                       'Jelinek; '
                                                                       'the '
                                                                       'aberration\n'
                                                                       '  '
                                                                       'decision '
                                                                       're-homed '
                                                                       'to '
                                                                       'L-314).\n'
                                                                       '- '
                                                                       'L-234 '
                                                                       "(Earth's "
                                                                       'half '
                                                                       'served; '
                                                                       'the '
                                                                       "website's "
                                                                       'missing '
                                                                       'dipole '
                                                                       'cone\n'
                                                                       '  '
                                                                       're-homed '
                                                                       'to '
                                                                       'L-375).\n'
                                                                       '- '
                                                                       'L-383 '
                                                                       '(dead '
                                                                       'data; '
                                                                       'folded '
                                                                       'into '
                                                                       "L-181's "
                                                                       '124 '
                                                                       'tooltip '
                                                                       'fields).\n'
                                                                       '\n'
                                                                       '## '
                                                                       'Discrepancies '
                                                                       'surfaced\n'
                                                                       '\n'
                                                                       '- '
                                                                       'The '
                                                                       'L-371 '
                                                                       'handoff '
                                                                       'said '
                                                                       'an '
                                                                       'exosphere '
                                                                       'shell '
                                                                       'naming '
                                                                       'the '
                                                                       'geocorona '
                                                                       'exists\n'
                                                                       '  in '
                                                                       'the '
                                                                       'orrery. '
                                                                       'It '
                                                                       'is '
                                                                       'the '
                                                                       "website's "
                                                                       'row; '
                                                                       'the '
                                                                       'orrery '
                                                                       'shell '
                                                                       'is '
                                                                       'unbuilt\n'
                                                                       '  '
                                                                       '(L-292). '
                                                                       'Fable '
                                                                       'found '
                                                                       'the '
                                                                       'same.\n'
                                                                       '- '
                                                                       "L-369's "
                                                                       'obliquity '
                                                                       'is '
                                                                       'typed '
                                                                       'in '
                                                                       'five '
                                                                       'places, '
                                                                       'not '
                                                                       'the '
                                                                       'four '
                                                                       'the '
                                                                       'L-371\n'
                                                                       '  '
                                                                       'sweep '
                                                                       'said.\n'
                                                                       '- '
                                                                       'The '
                                                                       "scanner's "
                                                                       'four '
                                                                       'new '
                                                                       'Tier-1 '
                                                                       'findings '
                                                                       'in '
                                                                       '`constants_new.py` '
                                                                       'are\n'
                                                                       '  '
                                                                       'cited '
                                                                       'rows: '
                                                                       'one '
                                                                       'Source '
                                                                       'line '
                                                                       'sits '
                                                                       '16 '
                                                                       'lines '
                                                                       'down '
                                                                       'against '
                                                                       'a '
                                                                       '15-line\n'
                                                                       '  '
                                                                       'window '
                                                                       '(tested), '
                                                                       'and '
                                                                       'three '
                                                                       'rows '
                                                                       'carry '
                                                                       'declared '
                                                                       'reasons '
                                                                       'the '
                                                                       'scanner\n'
                                                                       '  '
                                                                       'does '
                                                                       'not '
                                                                       'credit '
                                                                       '(L-414). '
                                                                       'The '
                                                                       'previous '
                                                                       "session's "
                                                                       'summary '
                                                                       'to '
                                                                       'Tony\n'
                                                                       '  '
                                                                       'called '
                                                                       'them '
                                                                       'rows '
                                                                       'with '
                                                                       'no '
                                                                       'readable '
                                                                       'source '
                                                                       'line; '
                                                                       'that '
                                                                       'was '
                                                                       'half '
                                                                       'right.\n'
                                                                       '- '
                                                                       "Fable's "
                                                                       'sweep '
                                                                       'listed '
                                                                       "Earth's "
                                                                       'Hill '
                                                                       'sphere '
                                                                       'as '
                                                                       'unserved; '
                                                                       'it '
                                                                       'is '
                                                                       'served '
                                                                       'as\n'
                                                                       '  '
                                                                       'its '
                                                                       'own '
                                                                       'group. '
                                                                       'Fable '
                                                                       'read '
                                                                       'L-383 '
                                                                       'as '
                                                                       'waiting '
                                                                       'on '
                                                                       'L-349; '
                                                                       'it '
                                                                       'is '
                                                                       'dead '
                                                                       'data,\n'
                                                                       '  '
                                                                       "L-181's.\n"
                                                                       '- '
                                                                       'Fable '
                                                                       'missed '
                                                                       'the '
                                                                       'aberration '
                                                                       'decision '
                                                                       'inside '
                                                                       'L-305; '
                                                                       'it '
                                                                       'is '
                                                                       'now '
                                                                       'on\n'
                                                                       '  '
                                                                       'L-314.\n'
                                                                       '- In '
                                                                       'this '
                                                                       'conversation '
                                                                       'Claude '
                                                                       'first '
                                                                       'said '
                                                                       'L-300 '
                                                                       'fits '
                                                                       'the '
                                                                       'website '
                                                                       'patch\n'
                                                                       '  '
                                                                       'because '
                                                                       'that '
                                                                       'patch '
                                                                       '"already '
                                                                       'opens '
                                                                       'the '
                                                                       'run". '
                                                                       'It '
                                                                       'does '
                                                                       'not; '
                                                                       'L-300 '
                                                                       'adds\n'
                                                                       '  '
                                                                       'the '
                                                                       "runner's "
                                                                       'file '
                                                                       'to '
                                                                       'it. '
                                                                       'Corrected '
                                                                       'to '
                                                                       'Tony '
                                                                       'in '
                                                                       'the '
                                                                       'same '
                                                                       'conversation.\n'
                                                                       '- '
                                                                       'The '
                                                                       'first '
                                                                       'build '
                                                                       'of '
                                                                       'this '
                                                                       'patch, '
                                                                       'on '
                                                                       'cbde99dc, '
                                                                       'never '
                                                                       'ran: '
                                                                       'Tony '
                                                                       'pushed\n'
                                                                       '  '
                                                                       'his '
                                                                       'notes '
                                                                       'and '
                                                                       "Fable's "
                                                                       'sweep '
                                                                       'first '
                                                                       '(41c1ca7a), '
                                                                       'so '
                                                                       'it '
                                                                       'would '
                                                                       'have\n'
                                                                       '  '
                                                                       'refused '
                                                                       'on '
                                                                       'the '
                                                                       'sweep '
                                                                       'file '
                                                                       'already '
                                                                       'existing. '
                                                                       'This '
                                                                       'build '
                                                                       'is '
                                                                       'the '
                                                                       'same\n'
                                                                       '  '
                                                                       'ledger '
                                                                       'work '
                                                                       'on '
                                                                       '41c1ca7a, '
                                                                       'without '
                                                                       'that '
                                                                       'file, '
                                                                       'plus '
                                                                       'L-415.\n'
                                                                       '- '
                                                                       'The '
                                                                       "ledger's "
                                                                       'header '
                                                                       'stamps '
                                                                       'had '
                                                                       'lagged '
                                                                       'three '
                                                                       'sessions; '
                                                                       'this '
                                                                       'patch\n'
                                                                       '  '
                                                                       'stamps '
                                                                       'it '
                                                                       'and '
                                                                       'says '
                                                                       'so '
                                                                       'on '
                                                                       'L-396.\n'
                                                                       '- '
                                                                       'L-068 '
                                                                       'was '
                                                                       'left '
                                                                       'OPEN: '
                                                                       'it '
                                                                       'is '
                                                                       'an '
                                                                       'umbrella '
                                                                       'whose '
                                                                       '"none '
                                                                       'of '
                                                                       'its '
                                                                       'own" '
                                                                       'Gap '
                                                                       'is\n'
                                                                       '  '
                                                                       'accurate. '
                                                                       'L-308 '
                                                                       'moved '
                                                                       'to '
                                                                       'DEFERRED.\n'
                                                                       '\n'
                                                                       '## '
                                                                       'Tony-actions, '
                                                                       'rolled '
                                                                       'up\n'
                                                                       '\n'
                                                                       '- '
                                                                       '(do) '
                                                                       'Run '
                                                                       'patch_L413_1 '
                                                                       'from '
                                                                       'the '
                                                                       'orrery '
                                                                       'root, '
                                                                       'then\n'
                                                                       '  '
                                                                       'orrery_maintenance_run.py '
                                                                       '(every '
                                                                       'gating '
                                                                       'check '
                                                                       'passes; '
                                                                       'its '
                                                                       'Ledger\n'
                                                                       '  '
                                                                       'index '
                                                                       'step '
                                                                       'moves '
                                                                       'the '
                                                                       'seven '
                                                                       'closed '
                                                                       'items '
                                                                       'into '
                                                                       'the '
                                                                       'closed '
                                                                       'section, '
                                                                       'and\n'
                                                                       '  '
                                                                       'its '
                                                                       'Skill '
                                                                       'manifest '
                                                                       'step '
                                                                       'writes '
                                                                       '1.12 '
                                                                       'into '
                                                                       'the '
                                                                       'protocol), '
                                                                       'move '
                                                                       'the\n'
                                                                       '  '
                                                                       'script '
                                                                       'into '
                                                                       'documentation/, '
                                                                       'commit '
                                                                       'and '
                                                                       'push.\n'
                                                                       '- '
                                                                       '(do) '
                                                                       'Reinstall '
                                                                       'safe-file-editing '
                                                                       '(Settings '
                                                                       '> '
                                                                       'Skills) '
                                                                       'from\n'
                                                                       '  '
                                                                       'skills/safe-file-editing/SKILL.md, '
                                                                       'and '
                                                                       'replace '
                                                                       'the '
                                                                       "Project's\n"
                                                                       '  '
                                                                       'instructions '
                                                                       'with '
                                                                       'PROJECT_INSTRUCTIONS.md '
                                                                       'v3.80.\n'
                                                                       '- '
                                                                       '(decide) '
                                                                       'L-349, '
                                                                       'the '
                                                                       'inner '
                                                                       "belt's "
                                                                       'wording: '
                                                                       'the '
                                                                       'first '
                                                                       'step '
                                                                       'of '
                                                                       'L-413.\n'
                                                                       '- '
                                                                       '(decide) '
                                                                       'From '
                                                                       'the '
                                                                       'Fable '
                                                                       'sweep, '
                                                                       'one '
                                                                       'at a '
                                                                       'time '
                                                                       '(L-412): '
                                                                       'whether '
                                                                       'items\n'
                                                                       '  '
                                                                       'inside '
                                                                       'an '
                                                                       'ordered '
                                                                       'list '
                                                                       'need '
                                                                       'RICE '
                                                                       'scores; '
                                                                       'the '
                                                                       'scores '
                                                                       'it '
                                                                       'proposes.\n'
                                                                       '- '
                                                                       '(decide) '
                                                                       "L-314's "
                                                                       'aberration, '
                                                                       'at '
                                                                       'its '
                                                                       'design '
                                                                       'talk.\n'
                                                                       '\n'
                                                                       '## '
                                                                       'Next '
                                                                       'session\n'
                                                                       '\n'
                                                                       'First '
                                                                       'confirm '
                                                                       'the '
                                                                       'loaded '
                                                                       'safe-file-editing '
                                                                       'reads '
                                                                       '1.12 '
                                                                       '(L-415). '
                                                                       'Then\n'
                                                                       'start '
                                                                       'L-413: '
                                                                       'put '
                                                                       "L-349's "
                                                                       'wording '
                                                                       'question '
                                                                       'to '
                                                                       'Tony '
                                                                       'with '
                                                                       'the '
                                                                       'row '
                                                                       'read\n'
                                                                       'first, '
                                                                       'then '
                                                                       'build '
                                                                       'the '
                                                                       'orrery '
                                                                       'patch '
                                                                       '(load '
                                                                       'agentic-pre-test,\n'
                                                                       'orrery-coding-conventions '
                                                                       'and '
                                                                       'provenance-discipline; '
                                                                       'the '
                                                                       'geocorona\n'
                                                                       'shell '
                                                                       'is a '
                                                                       'new '
                                                                       'visual '
                                                                       'element). '
                                                                       'Beside '
                                                                       'it, '
                                                                       'L-414 '
                                                                       'is '
                                                                       'method '
                                                                       'for\n'
                                                                       'provenance-discipline '
                                                                       'and '
                                                                       'can '
                                                                       'ride '
                                                                       'whichever '
                                                                       'patch '
                                                                       'next '
                                                                       'opens '
                                                                       'the\n'
                                                                       'scanner.\n'
                                                                       '\n'
                                                                       'Session '
                                                                       'written '
                                                                       'October '
                                                                       '2026 '
                                                                       'with '
                                                                       "Anthropic's "
                                                                       'Claude '
                                                                       'Opus '
                                                                       '5.5.\n'}


def fingerprint(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def outside_zone(path, text):
    if path not in ZONED:
        return text
    start, end = ZONED[path]
    a = text.index(start)
    b = text.index(end) + len(end)
    return text[:a] + text[b:]


def read_lf(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    return raw.decode("utf-8").replace("\r\n", "\n"), b"\r\n" in raw


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the repo ROOT, not from "
                         "documentation/. NOTHING was written.")
    for marker in ROOT_MARKERS:
        if not os.path.isfile(marker):
            raise SystemExit("ERROR: %s is not here, so this is not the %s "
                             "root. NOTHING was written." % (marker, REPO))
    for path in NEW_FILES:
        if os.path.exists(path):
            raise SystemExit("ERROR: %s already exists. If this patch already "
                             "ran, it has nothing left to do. NOTHING was "
                             "written." % path)
    results = []
    for path in sorted(WHOLE_FILES):
        text, was_crlf = read_lf(path)
        wants, content = WHOLE_FILES[path]
        if fingerprint(text) not in wants:
            raise SystemExit(
                "ERROR: %s has changed since %s -- perhaps your notes. This\n"
                "       patch rewrites it whole and would lose them, so it\n"
                "       stops. Send the file to Claude. NOTHING was written."
                % (path, BUILT_ON))
        results.append((path, content, ["rewritten whole"], was_crlf))
    for path in sorted(EDITS):
        text, was_crlf = read_lf(path)
        if path not in ANCHOR_ONLY:
            got = fingerprint(outside_zone(path, text))
            if got != BASE[path]:
                raise SystemExit(
                    "ERROR: %s is not the file this patch was built against.\n"
                    "       expected %s, found %s. It has changed since\n"
                    "       %s, or this patch has already run.\n"
                    "       (Line endings are excluded, so they are not the cause.)\n"
                    "       NOTHING was written." % (path, BASE[path], got, BUILT_ON))
        done = []
        for label, old, new, want in EDITS[path]:
            found = text.count(old)
            if found != want:
                raise SystemExit("ANCHOR FAIL (%s): expected %d match(es) in "
                                 "%s, found %d. NOTHING was written."
                                 % (label, want, path, found))
            text = text.replace(old, new)
            done.append(label)
        bad = sum(1 for ch in text if ord(ch) > 127)
        if bad:
            raise SystemExit("ERROR: %s would hold %d non-ASCII character(s). "
                             "NOTHING was written." % (path, bad))
        results.append((path, text, done, was_crlf))
    for path, text, done, was_crlf in results:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in done:
            print("ok  %-30s %s" % (path, label))
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % path)
    for path in sorted(NEW_FILES):
        with open(path, "wb") as handle:
            handle.write(NEW_FILES[path].encode("utf-8"))
        print("ok  %-30s created" % path)
    print("")
    print("Stamps updated: the ledger's header (October 4, built on 41c1ca7a);")
    print("safe-file-editing's version line, cut-from list, date and v1.12")
    print("paragraph; the protocol's header, anchor and v3.80 entry; Where We")
    print("Are's date and SHAs.")
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    for line in NEXT:
        print("  " + line)


if __name__ == "__main__":
    main()
