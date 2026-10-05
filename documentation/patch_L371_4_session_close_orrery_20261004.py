#!/usr/bin/env python3
"""
patch_L371_4_session_close_orrery_20261004.py -- ORRERY repo. Closes the
session of 2026-10-04: L-371's distance cards built, the Sun's slice
ordered.

Built on orrery d7f2a59440b49461a742a301777a67dc9bf49097
at https://github.com/tonylquintanilla/palomas_orrery
(gallery ac81e7ce6257cfd6811df7d031f94ac3109d480c at
https://github.com/tonylquintanilla/tonyquintanilla.github.io; its own
small close patch, patch_L371_5, runs after this one).

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code and click Run. Then run orrery_maintenance_run.py
    the same way: every gating check should pass. Its Ledger index step
    moves the four closed items into the closed section; that is
    expected. Then move this script into documentation/, commit, push.

WHAT CHANGES
    LEDGER_CONSOLIDATED.md
        L-371 records the build, Tony's two rulings and what was found;
        L-385, L-386, L-228, L-241, L-131, L-136, L-128 gain their place
        in the Sun's slice; L-209, L-224, L-227 and L-229 close;
        L-363 gains the drawer-fix patch the other session ran after its
        records. L-410 (fuzzy boundaries), L-411 (typed numbers in the
        Sun's hovers) and L-412 (the Sun's slice, in Tony's order) open --
        numbered past the other session's L-409, the licenses. The ledger is
        matched by its lines, not by the whole file, so your notes in it
        elsewhere do not stop this patch.
    documentation/WHERE_WE_ARE.md       rewritten, as at every session's
        end. Your notes on it (one orbit is enough; notes must not fail
        a patch) are folded in, and so is the lobby-card session's page:
        this one covers both sessions. It is the one file checked whole:
        if it changed since d7f2a594 the patch stops rather than lose
        your words.
    documentation/HANDOFF_L371_distance_cards_session_20261004.md  new.
    Ten orrery files: this session's dates. Rows and credit lines were
        stamped 2026-10-03 / October 3; the work was 2026-10-04. Lines
        recording your rulings of 2026-10-03 (ruling A, your approved
        notes, the Hill radius correction) keep that date. Comments
        only; no value or hover changes.

PERMANENT, though this script is thrown away: the ledger entries, the
page, the handoff, the corrected dates.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 4, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

REPO = "orrery"
ROOT_MARKERS = ("palomas_orrery.py",)
BUILT_ON = "d7f2a594"
ANCHOR_ONLY = ("LEDGER_CONSOLIDATED.md",)
NEXT = ["1. Run orrery_maintenance_run.py. Every gating check passes.",
        "2. Move this script into documentation/; commit and push.",
        "3. Then the gallery's small close patch, patch_L371_5."]

BASE = {'LEDGER_CONSOLIDATED.md': '890af99b8f713aa3c037ecae5448b60b',
 'comet_visualization_shells.py': '6aa9f48e70552227f7ab3521fc3e9bb1',
 'constants_new.py': '4b08bfb51a80655170787c7f2af6cbea',
 'constants_rows.py': '209a3e44c7657c3ca3a1732dfceadba2',
 'constants_tokens.py': 'b9a6a9b6f5fd5f35b10f47a4f6413dd9',
 'exact_rows_report.py': '8cdd670a478ee06137d0c9aac99ccebf',
 'palomas_orrery.py': '67b68c853ceb3eb62123032af5b3924a',
 'shell_configs.py': '8dd87e52bc76829bed01bce9b8cfdc24',
 'solar_visualization_shells.py': '978fbef4ff90178438546542ec7d7133',
 'test_constants_provenance.py': 'e1eaa854e061f61c192f2dd39dde06d0',
 'test_worksheet_checker.py': '5f5860bb0874b23d641ebff6f0b2d301'}

EDITS = {'LEDGER_CONSOLIDATED.md': [('L-371: status date',
                             '<!-- L:371 status:OPEN upd:2026-10-03 section:A flag: rice: -->',
                             '<!-- L:371 status:OPEN upd:2026-10-04 section:A flag: rice: -->',
                             1),
                            ('L-371: the distance cards, built; the new Gap',
                             "**Gap:** Build the distance cards as the handoff's section 3 says: "
                             'the\n'
                             "orrery rows (with L-386's two re-homes, the Heliopause to 121 AU "
                             'and\n'
                             'Gravitational Influence to 0.65 pc), the orrery hovers by count, '
                             'then\n'
                             "the gallery's notes, mirror and cache. Then the fifteen eyeballed "
                             'shape\n'
                             'numbers, one drawing at a time.\n',
                             '- **2026-10-04, the distance cards BUILT** [verified @ orrery '
                             'e38b86ad,\n'
                             '  gallery ba688199]. Three patches: patch_L371_1 (orrery rows, the '
                             'pc\n'
                             '  token, `constants_rows.row_text()`, the orrery hovers by count, '
                             'three\n'
                             '  relation tests, exact_rows_report seeing `row_text()`), '
                             'patch_L371_2\n'
                             "  (ROCHE_LIMIT_DRAWN_RADII), patch_L371_3 (gallery links, Tony's "
                             'notes\n'
                             '  with their numbers from served range rows, `drawn_radius`, a far\n'
                             '  shell\'s "Radius: <n> AU", the re-recorded hover fixture). Orrery '
                             '20\n'
                             '  of 20, gallery 23 of 23 after the cache rebuild; Tony approved '
                             'both\n'
                             '  wording files and confirmed on the phone. Sources re-opened\n'
                             '  2026-10-04: Stone et al. 2005 (94.01 AU), Gurnett et al. 2013 p. '
                             '1489\n'
                             '  (121 AU; the 121.6 the old comment attributed to it is not in the\n'
                             "  paper), NASA's Oort Cloud facts page, Portegies Zwart et al. 2021\n"
                             '  (0.65 pc in the captions of Figs. 2 and 3 and sec. 5 -- not Fig. '
                             '4,\n'
                             '  as the previous handoff said; and sec. 2.2 for the 20,000 AU '
                             'edge,\n'
                             "  because Duncan, Quinn and Tremaine's abstract does not print it),\n"
                             '  Kasper et al. 2021 (19.7; its Table 1 says 19.8). The outer '
                             "corona's\n"
                             '  Mann et al. (2004) citation could not be found and is removed.\n'
                             "- **Tony's rulings this session.** (1) The Roche limit, known to "
                             'one\n'
                             "  figure, is DRAWN at its formula's full 3.45 on both sites, option "
                             'B,\n'
                             "  because at 3 it would sit on the inner corona's line; which is\n"
                             '  further out is not known. An interim until L-410. (2) The '
                             'leading-1\n'
                             '  shortcut is NOT adopted: the uncertainty test of 2026-09-28 is '
                             'the\n'
                             '  rule, and it prints 100,000 AU as 10,000,000,000,000 km and 3 '
                             'solar\n'
                             '  radii as 0.01 AU. Tony: "I don\'t want to violate my own rule!"\n'
                             '- **Found, recorded, not fixed.** (a) EXACT_ROWS_PRINTED.md lists '
                             '11\n'
                             '  gallery pointers to exact Sun rows as NOT FOLLOWED -- the cusp, '
                             'the\n'
                             '  corona, the Oort edges, the drawn Roche row, the galactic pole. '
                             'The\n'
                             '  website does print them by the served count, but the check cannot\n'
                             '  confirm it until each has a PRINTS or DRAWN entry in\n'
                             "  exact_rows_report.py. (b) The typed numbers left in the Sun's "
                             'hovers\n'
                             "  are L-411. (c) This session's rows and credit lines were first\n"
                             '  stamped 2026-10-03; the work was 2026-10-04. The close patches\n'
                             '  correct them; the patch file names keep 20261003.\n'
                             "- **Carried to the skills' next versions.** provenance-discipline\n"
                             '  cites GRAVITATIONAL_INFLUENCE_AU and its _RANGE_AU row as the '
                             'worked\n'
                             '  example of When the Source Gives a Range; the range row is gone, '
                             'so\n'
                             '  the example now belongs to the Oort edges or the helmet cusp. A\n'
                             '  session following the old sentence looks for a row that does not\n'
                             '  exist and finds the right rule nearby, so it is carried, not '
                             'bumped.\n'
                             '  And for any patch\'s "what the run should say": predict the\n'
                             "  scanner's CHANGE, not its total (this machine and Tony's differ "
                             'by\n'
                             '  one), and expect the patch script itself to be scanned while it '
                             'sits\n'
                             '  in the root folder.\n'
                             '**Gap:** (1) PRINTS or DRAWN entries for the 11 not-followed '
                             'pointers.\n'
                             '(2) The fifteen eyeballed shape numbers, one drawing at a time. The\n'
                             "rest of the Sun's slice is ordered on L-412.\n",
                             1),
                            ('L-371: refs',
                             '**Ref:** gallery `data/objects_config.json`; gallery '
                             '`gallery/feature_renderers.js`; L-322 Gap (3); L-345.\n',
                             '**Ref:** gallery `data/objects_config.json`; gallery '
                             '`gallery/feature_renderers.js`; L-322 Gap (3); L-345;\n'
                             '`documentation/HANDOFF_L371_distance_cards_session_20261004.md`; '
                             'L-386, L-410, L-411, L-412.\n',
                             1),
                            ('L-209: DONE',
                             '<!-- L:209 status:OPEN upd:2026-08-21 section:A flag: rice:3/3/85/1 '
                             '-->',
                             '<!-- L:209 status:DONE upd:2026-10-04 section:C flag: rice:3/3/85/1 '
                             '-->',
                             1),
                            ('L-209: item 2 closed',
                             '2. **MODE 5, unchanged and still outstanding.** The Alfven shell '
                             'should\n'
                             '   render one solar radius larger than before, still nested inside '
                             'the\n'
                             "   50 R_sun outer corona. Tony's eyes on a plot, not a build.\n",
                             '2. **MODE 5 -- DONE 2026-10-04.** The Alfven shell should\n'
                             '   render one solar radius larger than before, still nested inside '
                             'the\n'
                             "   50 R_sun outer corona. Tony's eyes on a plot, not a build. Tony "
                             'on\n'
                             '   the phone, ?exhibit=sun, after patch_L371_3: "yes, 0.092 au '
                             'inside\n'
                             '   0.23 au", and "Beautiful." Nothing re-homed: item 1 was '
                             'discharged\n'
                             '   on 2026-08-21.\n',
                             1),
                            ('L-224: DONE',
                             '<!-- L:224 status:OPEN upd:2026-08-22 section:A flag: rice:3/3/85/2 '
                             '-->',
                             '<!-- L:224 status:DONE upd:2026-10-04 section:C flag: rice:3/3/85/2 '
                             '-->',
                             1),
                            ('L-224: closing note',
                             '**Gap:** build it. The design is settled and sourced; nothing is\n',
                             '- **Closed 2026-10-04** [verified @ orrery e38b86ad]: the band is\n'
                             '  `create_sun_streamer_band` in `solar_visualization_shells.py`,\n'
                             '  STREAMER_BELT_RADII is retired, and the cusp is '
                             'HELMET_CUSP_RADII,\n'
                             '  now the top of a two-row range (L-371). Nothing left in this item\n'
                             '  to re-home.\n'
                             '**Gap:** none. (Was: build it. The design is settled and sourced; '
                             'nothing is\n',
                             1),
                            ('L-229: DONE',
                             '<!-- L:229 status:OPEN upd:2026-08-23 section:A flag: rice:3/4/95/1 '
                             '-->',
                             '<!-- L:229 status:DONE upd:2026-10-04 section:C flag: rice:3/4/95/1 '
                             '-->',
                             1),
                            ('L-229: closing note, its citation re-homed',
                             '- **Ref:** '
                             '`solar_visualization_shells.py::create_sun_streamer_band`;\n'
                             '  `planet_visualization_utilities.py::create_streamer_band_shape` '
                             'and\n',
                             '- **Closed 2026-10-04** [verified @ orrery e38b86ad]: the band is\n'
                             "  turned into the Sun's equatorial frame by\n"
                             "  `create_planet_transformation_matrix('Sun')`, and Tony saw it "
                             'lean\n'
                             "  with the axis. Its one loose end, a citation for the belt's\n"
                             '  orientation (or leave it declared), is re-homed to L-228: the '
                             'same\n'
                             '  module and the same kind of source read.\n'
                             '- **Ref:** '
                             '`solar_visualization_shells.py::create_sun_streamer_band`;\n'
                             '  `planet_visualization_utilities.py::create_streamer_band_shape` '
                             'and\n',
                             1),
                            ('L-227: DONE',
                             '<!-- L:227 status:OPEN upd:2026-08-23 section:A flag: rice:2/2/95/1 '
                             '-->',
                             '<!-- L:227 status:DONE upd:2026-10-04 section:C flag: rice:2/2/95/1 '
                             '-->',
                             1),
                            ('L-227: closing note',
                             '- **Ref:** '
                             '`solar_visualization_shells.py::create_sun_streamer_band_shell`;\n'
                             '  `skills/orrery-coding-conventions/SKILL.md` v1.5; L-224 (the '
                             'build\n',
                             "- **Closed 2026-10-04** [verified @ orrery e38b86ad]: the band's "
                             'hover\n'
                             '  wraps at about sixty characters a line. Its Tony-actions are\n'
                             '  overtaken: orrery-coding-conventions has since reached 1.9 and '
                             'been\n'
                             '  reinstalled several times. Nothing re-homed.\n'
                             '- **Ref:** '
                             '`solar_visualization_shells.py::create_sun_streamer_band_shell`;\n'
                             '  `skills/orrery-coding-conventions/SKILL.md` v1.5; L-224 (the '
                             'build\n',
                             1),
                            ('L-228: date',
                             '<!-- L:228 status:OPEN upd:2026-08-23 section:A flag:Tony '
                             'rice:2/3/60/2 -->',
                             '<!-- L:228 status:OPEN upd:2026-10-04 section:A flag:Tony '
                             'rice:2/3/60/2 -->',
                             1),
                            ("L-228: the Sun slice's fourth item; Claude reads the source",
                             '- **Tony-action (do):** the source read. Claude cannot clear this '
                             'by\n',
                             "- **2026-10-04: the Sun slice's fourth item (L-412).** Claude does "
                             'the\n'
                             '  read of Cranmer et al. (2007) itself, by web, and brings the '
                             'result\n'
                             "  and any wording change to Tony. Also carries L-229's loose end: a\n"
                             "  citation for the streamer belt's orientation about the solar\n"
                             '  equator, or the drawing stays declared.\n'
                             '- **Tony-action (do):** the source read. Claude cannot clear this '
                             'by\n',
                             1),
                            ('L-385: date',
                             '<!-- L:385 status:OPEN upd:2026-09-30 section:A flag: rice: -->',
                             '<!-- L:385 status:OPEN upd:2026-10-04 section:A flag: rice: -->',
                             1),
                            ('L-385: not the one line it was said to be',
                             "**Gap:** Tony's decision above; if shorter, one change to "
                             '`half_len_frac` for the Sun.\n',
                             "- **2026-10-04: not one line.** Planned for this session's close "
                             'and\n'
                             "  held back. `half_len_frac` is the rotation axis's length; at 1.1 "
                             'the\n'
                             '  axis barely clears the photosphere, and the opening width is then\n'
                             '  set by whichever shells are on -- the inner corona alone is 3 '
                             'solar\n'
                             '  radii. "Photosphere + 10%" needs the autoscale and the default '
                             'shells\n'
                             "  read together, and a Mode 5 look. The Sun slice's third item "
                             '(L-412).\n'
                             "**Gap:** read the Sun's autoscale with its default shells; propose "
                             'how\n'
                             "the view opens at photosphere + 10% and what the axis does; Tony's "
                             'eye.\n',
                             1),
                            ('L-386: progress',
                             "**Gap:** The Sun's slice.\n"
                             '**Ref:** `constants_new.py`; gallery `data/objects_config.json`; '
                             'L-345; L-371; L-322.\n',
                             '- **2026-10-04, two re-homed (L-371):** HELIOPAUSE_AU (121, '
                             'Gurnett)\n'
                             '  with HELIOPAUSE_RADII its conversion, and '
                             'GRAVITATIONAL_INFLUENCE_PC\n'
                             '  (0.65, Portegies Zwart) with GRAVITATIONAL_INFLUENCE_AU its\n'
                             '  conversion; KM_PER_PARSEC and the pc token added for it. The Oort\n'
                             "  edges and the termination shock were already in their sources' "
                             'unit.\n'
                             "**Gap:** the core, the radiative zone and the photosphere's AU row\n"
                             '(CORE_AU, RADIATIVE_ZONE_AU, SOLAR_RADIUS_AU), still unexported: '
                             'the\n'
                             "Sun slice's seventh item (L-412).\n"
                             '**Ref:** `constants_new.py`; gallery `data/objects_config.json`; '
                             'L-345; L-371; L-322.\n',
                             1),
                            ('L-241: folds into the fuzzy-boundary design',
                             '**Gap:** minor. Fold into the next touch of either instrument.\n',
                             '- **2026-10-04:** folds into L-410. A fuzzy torus changes what the\n'
                             '  hover should describe, so the wording waits for that design (the\n'
                             "  Sun slice's sixth item, L-412).\n"
                             '**Gap:** minor. Fold into the next touch of either instrument.\n',
                             1),
                            ('L-131: into the Sun slice with the fuzzy outer corona',
                             '- **Cross-ref:** groups with L-128, L-136.\n'
                             '**Gap:** not scoped -- design conversation needed (extent, density\n'
                             'profile, data source).\n',
                             '- **Cross-ref:** groups with L-128, L-136.\n'
                             "- **2026-10-04, into the Sun's slice (Tony), designed with L-410.**\n"
                             "  The outer corona's faint glow is sunlight scattered by this same\n"
                             "  dust, so the outer corona's fuzzy edge may be where the drawing\n"
                             '  hands over to the dust cloud rather than fading into nothing. The\n'
                             "  cloud is flattened toward the planets' plane: a thick disk, not a\n"
                             '  sphere. Tony: this "conforms to our braid principle and grouping '
                             'of\n'
                             '  thematic content". The Sun slice\'s ninth item (L-412).\n'
                             '**Gap:** not scoped -- design conversation needed (extent, density\n'
                             'profile, data source), with L-410.\n',
                             1),
                            ('L-136: belongs with the Kuiper belt',
                             '- **Cross-ref:** groups with L-128, L-131.\n'
                             '**Gap:** not scoped -- design conversation needed.\n'
                             '**Ref:** to_do_ideas.md (pre-ledger, 4/18/26).\n',
                             '- **Cross-ref:** groups with L-128, L-131.\n'
                             "- **2026-10-04 (Tony):** not the Sun's slice. A population of "
                             'distant\n'
                             '  icy bodies belongs with the Kuiper belt in the Solar System room.\n'
                             '**Gap:** not scoped -- design conversation needed.\n'
                             '**Ref:** to_do_ideas.md (pre-ledger, 4/18/26).\n',
                             1),
                            ("L-128: the Sun slice's tenth item",
                             'sublimation distances, single vs. multi-shell, data source).\n'
                             '**Ref:** to_do_ideas.md (pre-ledger, 4/16/26).\n',
                             'sublimation distances, single vs. multi-shell, data source).\n'
                             "- **2026-10-04 (Tony):** in the Sun's slice, its tenth item "
                             '(L-412):\n'
                             '  a design talk after the dust cloud, since both are about what '
                             'fills\n'
                             '  the space around the Sun.\n'
                             '**Ref:** to_do_ideas.md (pre-ledger, 4/16/26).\n',
                             1),
                            ('L-363: the drawer fixes and Home, run and phone-checked',
                             '  - Unchanged: the swap (design section 7) -- a bare '
                             '`interactive.html`\n'
                             '    link opening this room, the Explorer at its own address -- '
                             'after\n'
                             "    the Sun's slice, per option C of 2026-09-29.\n",
                             '  - Unchanged: the swap (design section 7) -- a bare '
                             '`interactive.html`\n'
                             '    link opening this room, the Explorer at its own address -- '
                             'after\n'
                             "    the Sun's slice, per option C of 2026-09-29.\n"
                             "- **2026-10-04, the drawer's small fixes and Home, built** by the\n"
                             '  lobby-card session after its records patch: gallery\n'
                             "  `patch_L363_14_gallery_drawer_fixes_20261004.py` (the i panel's\n"
                             "  bullet lists and Home line; sideways, an opened row's Enter "
                             'button\n'
                             "  on the name's line; Home backing out to hold every ticked body).\n"
                             '  Pushed by gallery ac81e7ce. Tony on the phone and the desktop:\n'
                             '  "correct" [render-gated, Tony; recorded from his run record by '
                             'the\n'
                             "  L-371 session's close, which found it unrecorded here].\n",
                             1),
                            ('L-410, L-411, L-412 after L-408',
                             '**Ref:** L-406, L-265; gallery `gallery/feature_renderers.js`,\n'
                             '`data/objects_config.json`.\n',
                             '**Ref:** L-406, L-265; gallery `gallery/feature_renderers.js`,\n'
                             '`data/objects_config.json`.\n'
                             '\n'
                             '\n'
                             '#### [L-410] Fuzzy boundaries for edges known only as ranges, the '
                             "outer corona first (orrery + gallery, the Sun's slice)\n"
                             '<!-- L:410 status:OPEN upd:2026-10-04 section:A flag: rice: -->\n'
                             "- **Tony's idea, 2026-10-04**, deciding where the Roche limit is "
                             'drawn:\n'
                             '  "What if we draw fuzzy boundaries instead of shells". It is Show '
                             'the\n'
                             '  Envelope of the Unknowable as a drawing.\n'
                             '- **Where it fits.** An edge given as a sourced range becomes a '
                             'band\n'
                             '  that fades between the two rows: the inner corona (2-3 solar '
                             'radii),\n'
                             "  each Oort edge (L-371's range rows). An edge with no edge at all "
                             '--\n'
                             '  the outer corona -- fades by a declared rate, said on its card, '
                             'as\n'
                             '  the streamer band already does. A single measured crossing (the\n'
                             '  termination shock, the heliopause) stays a sharp shell.\n'
                             '- **The Roche limit needs a source first:** a published range of '
                             'comet\n'
                             "  densities. The 2.7 to 4.3 solar radii in the session's chat was\n"
                             '  arithmetic on a guessed factor of two, not a source.\n'
                             '- **Order (Tony, 2026-10-04):** the outer corona first, designed '
                             'WITH\n'
                             '  the dust cloud (L-131), since its glow is that dust. It is the\n'
                             '  simplest shape and the website already has the fading machinery. '
                             'The\n'
                             '  Oort edges are the biggest payoff after it. Written twice -- '
                             'Python\n'
                             '  and JavaScript -- and checked on the phone.\n'
                             '- **Until then:** the Roche limit stays drawn at 3.45 (L-371, option '
                             'B),\n'
                             "  and L-241's torus wording waits for this design.\n"
                             "**Gap:** a design talk before any build. The Sun slice's ninth item\n"
                             '(L-412).\n'
                             '**Ref:** L-131, L-241, L-371; `solar_visualization_shells.py`\n'
                             '(`create_sun_streamer_band`, the fade to follow); gallery\n'
                             '`gallery/feature_renderers.js`.\n'
                             '\n'
                             '\n'
                             "#### [L-411] The typed numbers left in the Sun's hovers (orrery + "
                             "gallery, the Sun's slice)\n"
                             '<!-- L:411 status:OPEN upd:2026-10-04 section:A flag: rice: -->\n'
                             "- **Recorded 2026-10-04** while building L-371. The orrery's Sun\n"
                             "  hovers, and some of the gallery's served words, still type "
                             'numbers\n'
                             '  that no row holds. One row per CLASS (The Braid); the instances '
                             'live\n'
                             "  in the code. The kinds, by example: Voyager 2's 84 AU crossing "
                             '(83.4 in\n'
                             '  Gurnett et al. 2013, p. 1489); Sedna\'s 936 AU; "75 to 100 AU" for '
                             'the\n'
                             "  termination shock; the Alfven surface's latitude ranges (that part "
                             'is\n'
                             '  L-228); the 15 R_sun field of view; temperatures.\n'
                             '- **One statement that is out of date, not a number:** the '
                             'heliopause\n'
                             '  hover says both Voyagers are still in the heliosheath; Voyager 2\n'
                             '  crossed the heliopause in 2018.\n'
                             '- **Method:** source it or remove it, one number at a time, under '
                             'the\n'
                             '  Fetched vs Recalled rule; wording changes go to Tony.\n'
                             "**Gap:** the Sun slice's fifth item (L-412), straight after L-228.\n"
                             '**Ref:** `solar_visualization_shells.py`, '
                             '`comet_visualization_shells.py`;\n'
                             'gallery `data/objects_config.json`; L-228, L-371.\n'
                             '\n'
                             '\n'
                             "#### [L-412] The Sun's slice: the order Tony confirmed (the Sun's "
                             'slice)\n'
                             '<!-- L:412 status:OPEN upd:2026-10-04 section:A flag: rice: -->\n'
                             '- **Confirmed by Tony, 2026-10-04**, after a sweep of the open items '
                             'that\n'
                             '  touch the Sun room. Smallest and most settled first:\n'
                             '  1. L-209, the Alfven surface look -- DONE 2026-10-04.\n'
                             '  2. L-224, L-229, L-227, the streamer band -- DONE 2026-10-04.\n'
                             "  3. L-385, the orrery's opening view of the Sun (not one line; see "
                             'it).\n'
                             "  4. L-228, the Alfven surface's latitude ranges, with L-229's\n"
                             '     orientation citation.\n'
                             "  5. L-411, the other typed numbers in the Sun's hovers.\n"
                             "  6. L-241, the Hills cloud hover, inside L-410's design.\n"
                             '  7. L-386, the core, radiative zone and photosphere rows.\n'
                             '  8. L-408, the Galactic Plane toggle.\n'
                             '  9. L-410 with L-131: the fuzzy outer corona and the dust cloud.\n'
                             '  10. L-128, the comet ice lines.\n'
                             "- Beside the list, L-371's own Gap: the exact-rows entries and the\n"
                             '  fifteen eyeballed shape numbers.\n'
                             '- **Not this slice:** L-136, the scattered disk, goes to the Solar\n'
                             '  System room with the Kuiper belt; L-234 (the Sun in the '
                             'assembler),\n'
                             '  L-239 (seeding the Oort builders), L-314 (live solar wind) and '
                             'L-331\n'
                             '  (Earth and Moon wording) stay where they are.\n'
                             '**Gap:** work down the list.\n'
                             "**Ref:** L-371 (the slice's numbers); the handles above.\n",
                             1)],
 'comet_visualization_shells.py': [('date: 2026-10-03 -> 2026-10-04',
                                    "Module updated: October 3, 2026 with Anthropic's Claude Opus "
                                    '5.5 (L-371:\n',
                                    "Module updated: October 4, 2026 with Anthropic's Claude Opus "
                                    '5.5 (L-371:\n',
                                    1)],
 'constants_new.py': [('date: 2026-10-03 -> 2026-10-04',
                       "# Status: measured V_CROSS_CHECKED 2026-10-03 -- belongs to no body's "
                       'slice;\n',
                       "# Status: measured V_CROSS_CHECKED 2026-10-04 -- belongs to no body's "
                       'slice;\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Read+: arXiv:1605.09788, 2026-10-03, Claude Opus 5.5\n',
                       '# Read+: arXiv:1605.09788, 2026-10-04, Claude Opus 5.5\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Note: moved here from the galactic-centre block on 2026-10-03 (L-371),\n',
                       '# Note: moved here from the galactic-centre block on 2026-10-04 (L-371),\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Conversion+: token in constants_tokens.py (L-371, 2026-10-03).\n',
                       '# Conversion+: token in constants_tokens.py (L-371, 2026-10-04).\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Status: declared 2026-10-03 -- a boundary chosen for the drawing, '
                       'L-371\n',
                       '# Status: declared 2026-10-04 -- a boundary chosen for the drawing, '
                       'L-371\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Review-note: the citation this row carried until 2026-10-03 could not\n',
                       '# Review-note: the citation this row carried until 2026-10-04 could not\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# drawn cusp is an expression over them (L-371, 2026-10-03).\n',
                       '# drawn cusp is an expression over them (L-371, 2026-10-04).\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Status: measured V_SOURCED 2026-10-03 -- abstract, open\n',
                       '# Status: measured V_SOURCED 2026-10-04 -- abstract, open\n',
                       3),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Status: declared 2026-10-03 -- the top of the range held in the two\n',
                       '# Status: declared 2026-10-04 -- the top of the range held in the two\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Declared+: the helmet. Until 2026-10-03 it was typed 4.0 with the\n',
                       '# Declared+: the helmet. Until 2026-10-04 it was typed 4.0 with the\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Status: declared 2026-10-03 -- where the shell is drawn, L-371\n',
                       '# Status: declared 2026-10-04 -- where the shell is drawn, L-371\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Declared+: 2026-10-03, option B: an interim, until edges known only as\n',
                       '# Declared+: 2026-10-04, option B: an interim, until edges known only as\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Status: measured V_SOURCED 2026-10-03 -- open full text\n',
                       '# Status: measured V_SOURCED 2026-10-04 -- open full text\n',
                       4),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Read+: 2026-10-03, Claude Opus 5.5. Table 1 of the same paper lists\n',
                       '# Read+: 2026-10-04, Claude Opus 5.5. Table 1 of the same paper lists\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Access+: (2026-10-03).\n',
                       '# Access+: (2026-10-04).\n',
                       4),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Read: abstract, Stone et al. (2005), at NASA ADS, 2026-10-03, Claude\n',
                       '# Read: abstract, Stone et al. (2005), at NASA ADS, 2026-10-04, Claude\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Corrected: 2026-10-03 (L-371) -- was 94, two figures where the source\n',
                       '# Corrected: 2026-10-04 (L-371) -- was 94, two figures where the source\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Cross-check retired: 2026-10-03 -- the Claude and GPT legs of '
                       '2026-08-02\n',
                       '# Cross-check retired: 2026-10-04 -- the Claude and GPT legs of '
                       '2026-08-02\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Read+: space.physics.uiowa.edu, 2026-10-03, Claude Opus 5.5\n',
                       '# Read+: space.physics.uiowa.edu, 2026-10-04, Claude Opus 5.5\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Note+: until 2026-10-03 is not in it.\n',
                       '# Note+: until 2026-10-04 is not in it.\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Cross-check retired: 2026-10-03 -- the Claude and GPT legs of '
                       '2026-08-02,\n',
                       '# Cross-check retired: 2026-10-04 -- the Claude and GPT legs of '
                       '2026-08-02,\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Note+: 2026-10-03 it was its own row, typed 26148 from 121.6 AU.\n',
                       '# Note+: 2026-10-04 it was its own row, typed 26148 from 121.6 AU.\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# --- the two edges of the Oort cloud, each a range (L-371, 2026-10-03) '
                       '---\n',
                       '# --- the two edges of the Oort cloud, each a range (L-371, 2026-10-04) '
                       '---\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Status: measured V_SOURCED 2026-10-03 -- open page\n',
                       '# Status: measured V_SOURCED 2026-10-04 -- open page\n',
                       4),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Read+: outer edges, 2026-10-03, Claude Opus 5.5\n',
                       '# Read+: outer edges, 2026-10-04, Claude Opus 5.5\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Read: as OORT_CLOUD_INNER_EDGE_LOW_AU, 2026-10-03, Claude Opus 5.5.\n',
                       '# Read: as OORT_CLOUD_INNER_EDGE_LOW_AU, 2026-10-04, Claude Opus 5.5.\n',
                       3),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Status: declared 2026-10-03 -- the low end of the range held in the '
                       'two\n',
                       '# Status: declared 2026-10-04 -- the low end of the range held in the '
                       'two\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Corrected: 2026-10-03 (L-371) -- was typed 2000, citing Hills (1981) '
                       'and\n',
                       '# Corrected: 2026-10-04 (L-371) -- was typed 2000, citing Hills (1981) '
                       'and\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Read+: 2026-10-03, Claude Opus 5.5\n',
                       '# Read+: 2026-10-04, Claude Opus 5.5\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Access: open full text, https://arxiv.org/html/2105.12816v2 '
                       '(2026-10-03).\n',
                       '# Access: open full text, https://arxiv.org/html/2105.12816v2 '
                       '(2026-10-04).\n',
                       2),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Corrected: 2026-10-03 (L-371) -- cited Hills (1981), which does not\n',
                       '# Corrected: 2026-10-04 (L-371) -- cited Hills (1981), which does not\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Status: declared 2026-10-03 -- the high end of the range held in the '
                       'two\n',
                       '# Status: declared 2026-10-04 -- the high end of the range held in the '
                       'two\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Corrected: 2026-10-03 (L-371) -- was typed 100000, citing Oort (1950)\n',
                       '# Corrected: 2026-10-04 (L-371) -- was typed 100000, citing Oort (1950)\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       "# --- the Sun's gravitational reach (L-371, 2026-10-03) ---\n",
                       "# --- the Sun's gravitational reach (L-371, 2026-10-04) ---\n",
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Read+: Zwart et al. (2021), arXiv:2105.12816v2, 2026-10-03, Claude Opus '
                       '5.5\n',
                       '# Read+: Zwart et al. (2021), arXiv:2105.12816v2, 2026-10-04, Claude Opus '
                       '5.5\n',
                       1),
                      ('date: 2026-10-03 -> 2026-10-04',
                       '# Note+: 2026-10-03 it was typed 150000, the midpoint of an unsourced\n',
                       '# Note+: 2026-10-04 it was typed 150000, the midpoint of an unsourced\n',
                       1)],
 'constants_rows.py': [('date: 2026-10-03 -> 2026-10-04',
                        "Module updated: October 3, 2026 with Anthropic's Claude Opus 5.5\n",
                        "Module updated: October 4, 2026 with Anthropic's Claude Opus 5.5\n",
                        1),
                       ('date: 2026-10-03 -> 2026-10-04',
                        '    of a width being chosen for it. L-371, 2026-10-03.\n',
                        '    of a width being chosen for it. L-371, 2026-10-04.\n',
                        1)],
 'constants_tokens.py': [('date: 2026-10-03 -> 2026-10-04',
                          "    # L-371 (2026-10-03): the Sun's gravitational reach is published\n",
                          "    # L-371 (2026-10-04): the Sun's gravitational reach is published\n",
                          1)],
 'exact_rows_report.py': [('date: 2026-10-03 -> 2026-10-04',
                           "Module updated: October 3, 2026 with Anthropic's Claude Opus 5.5\n",
                           "Module updated: October 4, 2026 with Anthropic's Claude Opus 5.5\n",
                           1)],
 'palomas_orrery.py': [('date: 2026-10-03 -> 2026-10-04',
                        "Module updated: October 3, 2026 with Anthropic's Claude Opus 5.5 "
                        '(L-371:\n',
                        "Module updated: October 4, 2026 with Anthropic's Claude Opus 5.5 "
                        '(L-371:\n',
                        1),
                       ('date: 2026-10-03 -> 2026-10-04',
                        "# Source+: Since 2026-10-03 (L-371) the row is the Sun's Hill radius in\n",
                        "# Source+: Since 2026-10-04 (L-371) the row is the Sun's Hill radius in\n",
                        1)],
 'shell_configs.py': [('date: 2026-10-03 -> 2026-10-04',
                       "Module updated: October 3, 2026 with Anthropic's Claude Opus 5.5 (L-371:\n",
                       "Module updated: October 4, 2026 with Anthropic's Claude Opus 5.5 (L-371:\n",
                       1)],
 'solar_visualization_shells.py': [('date: 2026-10-03 -> 2026-10-04',
                                    "Module updated: October 3, 2026 with Anthropic's Claude Opus "
                                    '5.5\n',
                                    "Module updated: October 4, 2026 with Anthropic's Claude Opus "
                                    '5.5\n',
                                    1),
                                   ('date: 2026-10-03 -> 2026-10-04',
                                    '# row gives it (L-371, 2026-10-03). A hover names these, '
                                    'never a typed\n',
                                    '# row gives it (L-371, 2026-10-04). A hover names these, '
                                    'never a typed\n',
                                    1)],
 'test_constants_provenance.py': [('date: 2026-10-03 -> 2026-10-04',
                                   "Module updated: October 3, 2026 with Anthropic's Claude Opus "
                                   '5.5\n',
                                   "Module updated: October 4, 2026 with Anthropic's Claude Opus "
                                   '5.5\n',
                                   1),
                                  ('date: 2026-10-03 -> 2026-10-04',
                                   '    """L-371, Tony\'s option B (2026-10-03): the drawn row '
                                   'equals the\n',
                                   '    """L-371, Tony\'s option B (2026-10-04): the drawn row '
                                   'equals the\n',
                                   1)],
 'test_worksheet_checker.py': [('date: 2026-10-03 -> 2026-10-04',
                                "Module updated: October 3, 2026 with Anthropic's Claude Opus 5.5 "
                                '(L-371:\n',
                                "Module updated: October 4, 2026 with Anthropic's Claude Opus 5.5 "
                                '(L-371:\n',
                                1),
                               ('date: 2026-10-03 -> 2026-10-04',
                                '# HELIOPAUSE_RADII was the fourth until 2026-10-03 (L-371): it '
                                'became a\n',
                                '# HELIOPAUSE_RADII was the fourth until 2026-10-04 (L-371): it '
                                'became a\n',
                                1)]}

NEW_FILES = {'documentation/HANDOFF_L371_distance_cards_session_20261004.md': '<!-- Doc-Kind: hand | Session '
                                                                  "record: L-371's distance cards "
                                                                  'built, the Sun slice ordered. '
                                                                  '-->\n'
                                                                  "# Handoff: the Sun's distance "
                                                                  'cards (L-371), and the Sun '
                                                                  'slice ordered\n'
                                                                  '\n'
                                                                  'Built on orrery '
                                                                  '17ef66607cbe63ac5ed7bdbff15397fbe546ae42 '
                                                                  'at\n'
                                                                  'https://github.com/tonylquintanilla/palomas_orrery; '
                                                                  'pushed through\n'
                                                                  'e38b86adb7d1b32696b759b3c8222f3742aa2bd4. '
                                                                  'Gallery\n'
                                                                  '52659e04 at '
                                                                  'https://github.com/tonylquintanilla/tonyquintanilla.github.io;\n'
                                                                  'pushed through '
                                                                  'ba68819937bae6089d104c9a370a0b84c8a87925 '
                                                                  '(the lobby\n'
                                                                  "card's separate session also "
                                                                  'pushed in between, at '
                                                                  'd4b408e6).\n'
                                                                  'The close patches below land '
                                                                  'after these, on orrery\n'
                                                                  'd7f2a59440b49461a742a301777a67dc9bf49097 '
                                                                  'and gallery\n'
                                                                  'ac81e7ce6257cfd6811df7d031f94ac3109d480c, '
                                                                  "where the lobby-card session's\n"
                                                                  'records and license patches had '
                                                                  'landed first.\n'
                                                                  '\n'
                                                                  '- Type: BUILD.\n'
                                                                  '- Supersedes: '
                                                                  '`documentation/HANDOFF_L406_L407_L371_session_20261003.md`\n'
                                                                  '  as the latest record. That '
                                                                  "file also holds this session's "
                                                                  'run records,\n'
                                                                  '  which Tony appended to it.\n'
                                                                  '- Session date: 2026-10-04. '
                                                                  '(Rows and credit lines were '
                                                                  'first stamped\n'
                                                                  '  2026-10-03 by mistake; the '
                                                                  'close patches correct them.)\n'
                                                                  '\n'
                                                                  '## What was done [verified @ '
                                                                  'orrery e38b86ad, gallery '
                                                                  'ba688199]\n'
                                                                  '\n'
                                                                  '1. **patch_L371_1 (orrery).** '
                                                                  "The Sun's distance rows, each "
                                                                  'with its\n'
                                                                  '   source opened this session, '
                                                                  'its figure count and its read '
                                                                  'line:\n'
                                                                  '   termination shock 94.01 AU '
                                                                  '(Stone et al. 2005), heliopause '
                                                                  '121 AU\n'
                                                                  '   (Gurnett et al. 2013, p. '
                                                                  "1489), the Oort cloud's two "
                                                                  'edges as range\n'
                                                                  "   rows (NASA's facts page) "
                                                                  'drawn at 2,000 and 100,000 AU, '
                                                                  'the inner\n'
                                                                  "   cloud's 20,000 AU (Portegies "
                                                                  'Zwart et al. 2021, sec. 2.2), '
                                                                  "the Sun's\n"
                                                                  '   Hill radius 0.65 pc (the '
                                                                  "same paper), the helmet cusp's "
                                                                  '2-4 as two\n'
                                                                  '   rows, the Alfven surface, '
                                                                  'corona and Roche limit with '
                                                                  'units and\n'
                                                                  '   counts. The unsourced '
                                                                  '100,000-200,000 AU row removed; '
                                                                  'the outer\n'
                                                                  "   corona's unfound citation "
                                                                  'removed. A pc token, '
                                                                  'KM_PER_PARSEC,\n'
                                                                  '   `constants_rows.row_text()`, '
                                                                  'every orrery hover line that '
                                                                  'states\n'
                                                                  '   these distances printed from '
                                                                  'its row, three relation tests, '
                                                                  'and\n'
                                                                  '   exact_rows_report.py made to '
                                                                  'see `row_text()`.\n'
                                                                  '2. **patch_L371_2 (orrery).** '
                                                                  "ROCHE_LIMIT_DRAWN_RADII, Tony's "
                                                                  'option B.\n'
                                                                  '3. **patch_L371_3 (gallery).** '
                                                                  "The Sun's links, Tony's notes "
                                                                  'with their\n'
                                                                  '   numbers from served range '
                                                                  'rows, `drawn_radius`, a far '
                                                                  "shell's\n"
                                                                  '   "Radius: <n> AU", served '
                                                                  'counts on the Oort shapes and '
                                                                  'the streamer\n'
                                                                  '   band, the Sun shells check, '
                                                                  'a re-recorded hover fixture.\n'
                                                                  '4. Runs: orrery 20 of 20; '
                                                                  'gallery 23 of 23 after '
                                                                  '`daily_run.py`. Tony\n'
                                                                  '   approved both wording files. '
                                                                  'On the phone: "Beautiful", and '
                                                                  'the\n'
                                                                  '   Alfven surface at 0.092 AU '
                                                                  'inside the outer corona at 0.23 '
                                                                  'AU.\n'
                                                                  '\n'
                                                                  "## Tony's rulings\n"
                                                                  '\n'
                                                                  '- The Roche limit is drawn at '
                                                                  '3.45 on both sites, described '
                                                                  'as "about\n'
                                                                  '  3": at 3 it would sit on the '
                                                                  'inner corona, and which is '
                                                                  'further out\n'
                                                                  '  is not known. An interim '
                                                                  'until fuzzy boundaries '
                                                                  '(L-410).\n'
                                                                  '- The leading-1 shortcut is not '
                                                                  'adopted. The uncertainty test '
                                                                  'of\n'
                                                                  '  2026-09-28 stands, so 100,000 '
                                                                  'AU prints as 10,000,000,000,000 '
                                                                  'km.\n'
                                                                  '  Tony: "I don\'t want to '
                                                                  'violate my own rule!"\n'
                                                                  '- Fuzzy boundaries are their '
                                                                  'own item, the outer corona '
                                                                  'first and\n'
                                                                  '  designed with the dust cloud '
                                                                  '(L-410, L-131). The dust cloud '
                                                                  'joins the\n'
                                                                  "  Sun's slice.\n"
                                                                  "- The Sun's slice is the "
                                                                  'ordered list on L-412. The '
                                                                  'scattered disk\n'
                                                                  '  (L-136) goes to the Solar '
                                                                  'System room.\n'
                                                                  '\n'
                                                                  '## Discrepancies surfaced\n'
                                                                  '\n'
                                                                  '- The orrery patch said the '
                                                                  'scanner would report 296 '
                                                                  'serious findings;\n'
                                                                  "  Tony's machine reported 297. "
                                                                  "Tony's tree was already at 297, "
                                                                  'and the\n'
                                                                  '  one new file flagged was the '
                                                                  'patch script itself in the root '
                                                                  'folder.\n'
                                                                  '  Carried on L-371 as method '
                                                                  'for the next skill version.\n'
                                                                  '- L-385 was offered as "one '
                                                                  'line" for this close and is '
                                                                  'not: the axis\n'
                                                                  '  length and the shells '
                                                                  'switched on both set the width. '
                                                                  'Recorded on\n'
                                                                  "  L-385; the Sun slice's next "
                                                                  'item.\n'
                                                                  '- EXACT_ROWS_PRINTED.md lists '
                                                                  '11 gallery pointers to exact '
                                                                  'Sun rows as\n'
                                                                  '  not followed. The site prints '
                                                                  'them by the served count, but '
                                                                  'the check\n'
                                                                  '  cannot yet confirm it. '
                                                                  "L-371's Gap.\n"
                                                                  '- The previous handoff cited '
                                                                  'Figs. 3 and 4 for the 0.65 pc; '
                                                                  'it is\n'
                                                                  '  Figs. 2 and 3. Duncan, Quinn '
                                                                  "and Tremaine's abstract does "
                                                                  'not print\n'
                                                                  '  20,000 AU, so the row cites '
                                                                  'Portegies Zwart sec. 2.2 '
                                                                  'instead.\n'
                                                                  '\n'
                                                                  '## Checked against the other '
                                                                  'session before closing\n'
                                                                  '\n'
                                                                  '- The lobby-card session had '
                                                                  'taken L-409 (the licenses), so '
                                                                  'this\n'
                                                                  "  session's new items are "
                                                                  'L-410, L-411 and L-412.\n'
                                                                  '- It had rewritten Where We '
                                                                  'Are; this close merges both '
                                                                  'sessions into\n'
                                                                  '  the page rather than '
                                                                  'replacing its words.\n'
                                                                  '- Its drawer-fix patch, '
                                                                  'patch_L363_14, ran after its '
                                                                  'records patch and\n'
                                                                  '  was not on the ledger; this '
                                                                  'close adds that note to L-363 '
                                                                  "from Tony's\n"
                                                                  '  run record.\n'
                                                                  '- No file this close edits had '
                                                                  'been touched by the other '
                                                                  'session\n'
                                                                  '  besides those two.\n'
                                                                  '\n'
                                                                  '## The close patches\n'
                                                                  '\n'
                                                                  '- '
                                                                  '`patch_L371_4_session_close_orrery_20261004.py`: '
                                                                  'the ledger (L-371,\n'
                                                                  '  L-385, L-386, L-228, L-241, '
                                                                  'L-131, L-136, L-128 and L-363 '
                                                                  'updated; L-209,\n'
                                                                  '  L-224, L-227, L-229 closed; '
                                                                  'L-410, L-411, L-412 opened), '
                                                                  'this\n'
                                                                  '  handoff, Where We Are, and '
                                                                  'the date corrections in ten '
                                                                  'orrery files.\n'
                                                                  '- '
                                                                  '`patch_L371_5_dates_gallery_20261004.py`: '
                                                                  'the date corrections in\n'
                                                                  "  three gallery files' "
                                                                  'comments. No hover or served '
                                                                  'value changes.\n'
                                                                  '\n'
                                                                  '## Tony-actions, rolled up\n'
                                                                  '\n'
                                                                  '- (do) Run the orrery close '
                                                                  'patch, then '
                                                                  'orrery_maintenance_run.py\n'
                                                                  '  (every gating check passes), '
                                                                  'move the script into '
                                                                  'documentation/,\n'
                                                                  '  commit and push.\n'
                                                                  '- (do) Run the gallery close '
                                                                  'patch, then '
                                                                  'gallery_maintenance_run.py\n'
                                                                  '  (23 of 23; no cache rebuild '
                                                                  'is needed, since no served '
                                                                  'value\n'
                                                                  '  changes), move the script '
                                                                  'into documentation/, commit and '
                                                                  'push.\n'
                                                                  '\n'
                                                                  '## Skills\n'
                                                                  '\n'
                                                                  '- No skill changed this '
                                                                  'session, so there is no load to '
                                                                  'confirm next\n'
                                                                  '  session.\n'
                                                                  '- Carried to the next versions '
                                                                  '(on L-371): '
                                                                  "provenance-discipline's\n"
                                                                  '  range-rule example names the '
                                                                  'removed range row; and a '
                                                                  "patch's\n"
                                                                  '  "what the run should say" '
                                                                  "should predict the scanner's "
                                                                  'change, not\n'
                                                                  '  its total.\n'
                                                                  '\n'
                                                                  '## Next session\n'
                                                                  '\n'
                                                                  "First, Earth's list (the "
                                                                  'section below). Then start at '
                                                                  'L-412 item 3,\n'
                                                                  "the orrery's opening view of "
                                                                  'the Sun (L-385):\n'
                                                                  "read the Sun's autoscale with "
                                                                  'its default shells and propose '
                                                                  'to Tony\n'
                                                                  'before building. Then item 4, '
                                                                  'L-228: Claude reads Cranmer et '
                                                                  'al. (2007)\n'
                                                                  'itself. Beside the list, '
                                                                  "L-371's own Gap.\n"
                                                                  '\n'
                                                                  "## Next session also: Earth's "
                                                                  'list, for a ledger update\n'
                                                                  '\n'
                                                                  'On 2026-10-04 Tony asked for '
                                                                  'the same sweep for Earth that '
                                                                  'L-412 is for\n'
                                                                  'the Sun, to be recorded on the '
                                                                  'ledger next session. Do it\n'
                                                                  'early: first read L-305 and '
                                                                  'L-292 against the code, so the '
                                                                  'list starts\n'
                                                                  'accurate, then write it as one '
                                                                  'ledger item in the shape of '
                                                                  'L-412.\n'
                                                                  '\n'
                                                                  'The sweep, as given to Tony:\n'
                                                                  '\n'
                                                                  '- **Possibly finished but still '
                                                                  'open; read first.**\n'
                                                                  '  - L-305, the magnetosphere on '
                                                                  'a sourced model: the Shue and '
                                                                  'Jelinek\n'
                                                                  '    shapes are in both '
                                                                  'instruments, but its open list '
                                                                  'is long.\n'
                                                                  '  - L-292, the shells the '
                                                                  'orrery does not draw: an '
                                                                  'exosphere shell\n'
                                                                  '    naming the geocorona now '
                                                                  'exists; the other two may not.\n'
                                                                  '  - L-383, the magnetosphere '
                                                                  'tooltip copy: if that '
                                                                  'SHELL_CONFIGS text\n'
                                                                  '    is never shown '
                                                                  '(orrery-coding-conventions '
                                                                  'calls the tooltip field\n'
                                                                  '    dead data), the copy goes.\n'
                                                                  '- **Small, the Earth room '
                                                                  'reaches them.**\n'
                                                                  "  - L-369, Earth's obliquity "
                                                                  'typed in four places outside '
                                                                  'the store.\n'
                                                                  "  - L-350, the magnetotail's "
                                                                  'observed extent served and '
                                                                  'shown nowhere:\n'
                                                                  '    Tony decides print it or '
                                                                  'stop serving it.\n'
                                                                  '  - L-349 then L-383, the inner '
                                                                  'belt\'s "where the measured '
                                                                  'particle\n'
                                                                  '    flux peaks": Tony\'s '
                                                                  'wording ruling, then the copy.\n'
                                                                  '  - L-389, the atmosphere '
                                                                  'shells from the equatorial '
                                                                  'radius against the\n'
                                                                  '    crust at the mean radius: '
                                                                  'Tony noted it "depends on the '
                                                                  'source".\n'
                                                                  '  - L-379, the recorded Earth '
                                                                  'scene payload, aging: recapture '
                                                                  'it.\n'
                                                                  "  - L-382, Tony's look at the "
                                                                  "magnetosphere's cost per "
                                                                  'animation frame.\n'
                                                                  '- **Design talks first.**\n'
                                                                  '  - L-231 then L-330, the belts '
                                                                  'tilted with the magnetic field, '
                                                                  'then\n'
                                                                  '    their shape.\n'
                                                                  '  - L-375, the eccentric dipole '
                                                                  'offset (depends on an '
                                                                  'unmodelled\n'
                                                                  '    rotation phase).\n'
                                                                  '  - L-356, IGRF-14 as a '
                                                                  're-sourcing of the coefficient '
                                                                  'rows.\n'
                                                                  "  - L-321, the orrery's 36 "
                                                                  'Earth hover strings into the '
                                                                  'provenance\n'
                                                                  '    braid.\n'
                                                                  '  - L-297 and L-294, the '
                                                                  "Lagrange points and Earth's "
                                                                  'heliocentric view,\n'
                                                                  "    behind Tony's ruling on the "
                                                                  'Explorer room.\n'
                                                                  '  - L-314 after L-305, live '
                                                                  'solar wind for the '
                                                                  'magnetosphere.\n'
                                                                  '  - L-374 and L-061, precession '
                                                                  'over time and the seasonal '
                                                                  'roll:\n'
                                                                  '    recorded ideas.\n'
                                                                  '- **Not the Earth room:** '
                                                                  'L-001, L-060 (the Earth System '
                                                                  'climate\n'
                                                                  '  track), L-157, L-173, L-186, '
                                                                  'L-252 (the cross-check '
                                                                  'programme), L-177\n'
                                                                  '  (Mercury), L-347, L-348, '
                                                                  'L-360, L-367 (general checks).\n'
                                                                  '\n'
                                                                  'Tony orders the list when it is '
                                                                  'put to him; the order above is '
                                                                  'the\n'
                                                                  "sweep's, not his.\n"
                                                                  '\n'
                                                                  'Session written October 2026 '
                                                                  "with Anthropic's Claude Opus "
                                                                  '5.5.\n'}

WHOLE_FILES = {'documentation/WHERE_WE_ARE.md': ('aac6b0fef875d05840e9f5f40a87aa3a',
                                   '<!-- Doc-Kind: hand | Where the project is and where it is '
                                   'going, in plain words. One file, rewritten in place; read it '
                                   'at the end of every session. -->\n'
                                   '# Where We Are\n'
                                   '\n'
                                   "Last updated: October 4, 2026, end of both of today's "
                                   'sessions.\n'
                                   '- Written at orrery d7f2a594 and gallery ac81e7ce.\n'
                                   "- Two sessions ran today side by side: the Sun's distance "
                                   'cards, and\n'
                                   '  the lobby card. This page now covers both.\n'
                                   '\n'
                                   '> **READ THIS FIRST**\n'
                                   '>\n'
                                   '> **Changed this session:**\n'
                                   "> - The Sun's distance cards are built, on the website and in "
                                   'the\n'
                                   '>   orrery. Every distance now comes from a source that was '
                                   'opened and\n'
                                   '>   read, and prints at the figures that source supports.\n'
                                   '> - The heliopause is 121 AU, the termination shock 94.01 AU, '
                                   'and the\n'
                                   ">   Sun's gravitational reach is its Hill radius, 0.65 "
                                   'parsecs.\n'
                                   '> - The Roche limit is drawn at 3.45 solar radii and described '
                                   'as\n'
                                   '>   "about 3", so it doesn\'t sit on the inner corona.\n'
                                   "> - The Sun's remaining work is now one ordered list of ten "
                                   'items. The\n'
                                   '>   dust cloud joined it.\n'
                                   '> - From the other session: the lobby opens with a wide Solar '
                                   'System\n'
                                   ">   card; the drawer's small fixes and Home are built; both\n"
                                   '>   repositories now show "MIT license" on GitHub, and the '
                                   "website's\n"
                                   '>   content is under CC BY 4.0.\n'
                                   '>\n'
                                   '> **Do next:**\n'
                                   "> - *The Sun's list, from item 3: the orrery's opening view of "
                                   'the Sun,\n'
                                   ">   then the Alfven surface's unsourced ranges.*\n"
                                   '>\n'
                                   '> **Needs you now:**\n'
                                   '> - *Run the two small close patches and push.*\n'
                                   '\n'
                                   'How to read the marks:\n'
                                   '- *Italic* lines are the must-reads.\n'
                                   '- **>> UPDATED THIS SESSION** beside a heading means that '
                                   'section\n'
                                   '  changed in the latest session.\n'
                                   '- "<< new this session" beside a road stage marks a change to '
                                   'the road.\n'
                                   '- Sections without a mark are as they were.\n'
                                   "- The marks are cleared and reset at every session's update, "
                                   'so they\n'
                                   '  always mean "new since you last read this."\n'
                                   '\n'
                                   '## The goal  **>> UPDATED THIS SESSION**\n'
                                   '\n'
                                   "- Paloma's Orrery on the web.\n"
                                   '- The website does what the desktop orrery does, in the '
                                   'browser, from\n'
                                   '  data fetched from JPL each night, so a visitor never waits '
                                   'on JPL.\n'
                                   '- Anyone can open it, with nothing to install.\n'
                                   '- Built from the same code and the same checked numbers as the '
                                   'desktop\n'
                                   '  orrery.\n'
                                   '- The one real limit: the browser can show only the dates the '
                                   'saved\n'
                                   '  data covers.\n'
                                   '- Saved data covering one orbit of each body is enough, as you '
                                   'decided.\n'
                                   '- Within that range, a visitor will be able to choose a date, '
                                   'and\n'
                                   '  perhaps play time forward.\n'
                                   '\n'
                                   '## The road  **>> UPDATED THIS SESSION**\n'
                                   '\n'
                                   "  1. [done]   The Sun's room is live on the website.\n"
                                   "  2. [done]   Earth's room is live, with every number traced "
                                   'to its source.\n'
                                   '  3. [done]   The numbers come from one place: the orrery '
                                   'feeds the\n'
                                   '              website, and nothing is typed twice.\n'
                                   '  4. [done]   The Solar System room becomes a second way in: '
                                   'all the\n'
                                   '              planets, a drawer to pick them, and a way into '
                                   'each\n'
                                   "              body's own room. << new this session: the "
                                   "drawer's\n"
                                   '              small fixes and Home are built, and you checked '
                                   'them.\n'
                                   "  5. [NOW]    *The Sun's numbers get the same checking Earth's "
                                   'got.*\n'
                                   '              << new this session: the distance cards are '
                                   'done. Ten\n'
                                   '              items remain, in the order you confirmed.\n'
                                   '  6. [next]   A bare interactive.html link opens the Solar '
                                   'System room,\n'
                                   '              and the Explorer gets its own address, after the '
                                   "Sun's\n"
                                   '              list. << new this session: its first half, the '
                                   "lobby's\n"
                                   '              wide Solar System card, is done and on the '
                                   'website.\n'
                                   "  7. [later]  The rest of the orrery's objects come to the "
                                   'website --\n'
                                   '              dwarf planets, asteroids, moons -- through the '
                                   'same\n'
                                   "              connection that now carries the room's eleven "
                                   'bodies,\n'
                                   '              checked against JPL Horizons.\n'
                                   '  8. [later]  Encounters: comets and spacecraft shown at the '
                                   'dates\n'
                                   '              that matter.\n'
                                   '  9. [later]  The planets get their details -- layers, rings, '
                                   'magnetic\n'
                                   '              fields -- Jupiter and Saturn first.\n'
                                   ' 10. [goal]   The website does what the desktop orrery does, '
                                   'from data\n'
                                   '              fetched from JPL each night, with a date to '
                                   'choose and\n'
                                   '              time to play within the range the data covers.\n'
                                   '\n'
                                   '## Right now  **>> UPDATED THIS SESSION**\n'
                                   '\n'
                                   "- On the phone, the Sun's far shells say their radius in AU, "
                                   'then\n'
                                   '  their kilometres, at the figures their sources support.\n'
                                   "- Your notes print under the Oort cloud's two edges, "
                                   'Gravitational\n'
                                   '  Influence, the outer corona and the streamer belt. Their '
                                   'numbers come\n'
                                   '  from the stored rows, not typed into the words.\n'
                                   '- The Alfven surface sits inside the outer corona, as you '
                                   'checked.\n'
                                   "- The orrery's Sun hovers print the same numbers from the same "
                                   'rows.\n'
                                   '- The lobby opens with the wide Solar System card. Its picture '
                                   'shows\n'
                                   '  the planets at noon on October 4; the room itself always '
                                   'shows now.\n'
                                   "- In the Solar System room's drawer, an opened row fits with "
                                   'the phone\n'
                                   '  sideways, and Home backs out to keep every ticked body in '
                                   'view.\n'
                                   '- Some kilometre figures look coarse because their source '
                                   'gives one\n'
                                   '  figure: 100,000 AU prints as 10,000,000,000,000 km. That is '
                                   'the rule\n'
                                   '  you set on September 28, and you kept it.\n'
                                   '\n'
                                   '## The next three steps  **>> UPDATED THIS SESSION**\n'
                                   '\n'
                                   "1. *The orrery's opening view of the Sun.*\n"
                                   '   - You decided "photosphere plus 10%".\n'
                                   '   - It turned out to be more than one line: the axis length '
                                   'and the\n'
                                   '     shells that start switched on both set the width. '
                                   'Proposed to you\n'
                                   '     before it is built.\n'
                                   "2. The Alfven surface's three unsourced ranges.\n"
                                   '   - I read Cranmer et al. (2007). If it states them, they '
                                   'stay with a\n'
                                   '     citation; if not, all three go.\n'
                                   "   - The streamer belt's tilt with the Sun's equator gets the "
                                   'same\n'
                                   '     read.\n'
                                   "3. The other typed numbers in the Sun's hovers, one at a "
                                   'time.\n'
                                   "   - For example Voyager 2's 84 AU, and the heliopause hover "
                                   'saying\n'
                                   '     both Voyagers are still inside, which stopped being true '
                                   'in 2018.\n'
                                   '\n'
                                   '## Waiting on you  **>> UPDATED THIS SESSION**\n'
                                   '\n'
                                   'Now:\n'
                                   '- Run the two small close patches (orrery, then website) and '
                                   'push.\n'
                                   '- Delete the folder "data/solar-system (1)" in your gallery '
                                   'copy, with\n'
                                   '  OneDrive paused, as you did on October 1. Git ignores it, so '
                                   'it does\n'
                                   '  no harm meanwhile.\n'
                                   '\n'
                                   'At the next design talk:\n'
                                   '- The fuzzy outer corona, designed together with the dust '
                                   'cloud.\n'
                                   '- Moving the highlighted row to the top of the list.\n'
                                   "- An arrow from GO's text box to its body.\n"
                                   '\n'
                                   'Not urgent, in your order:\n'
                                   "1. The full check of the orrery's object list against JPL "
                                   'Horizons.\n'
                                   '2. Whether the editor should also edit the words on the Solar '
                                   'System\n'
                                   "   room's rows.\n"
                                   '3. Choosing a date, and animation.\n'
                                   '4. The scattered disk, with the Kuiper belt in the Solar '
                                   'System room.\n'
                                   '\n'
                                   '## Where the details are  **>> UPDATED THIS SESSION**\n'
                                   '\n'
                                   '- Every item, done and open: `LEDGER_CONSOLIDATED.md`\n'
                                   '  - The Sun session: L-371 (the distance cards), L-412 (the '
                                   "Sun's list\n"
                                   '    of ten), L-410 (fuzzy boundaries), L-411 (typed numbers), '
                                   'L-131\n'
                                   '    (the dust cloud). Closed: L-209, L-224, L-227, L-229.\n'
                                   '  - The lobby session: L-363 (the lobby card, the drawer fixes '
                                   'and\n'
                                   '    Home), L-409 (the licenses), L-216 (the stray folder).\n'
                                   '- The reasoning behind the order:\n'
                                   '  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`\n'
                                   '- The latest session records:\n'
                                   '  '
                                   '`documentation/HANDOFF_L371_distance_cards_session_20261004.md`, '
                                   'and\n'
                                   '  '
                                   '`documentation/HANDOFF_L363_lobby_card_session_20261004.md`\n')}


def fingerprint(raw):
    return hashlib.md5(raw.replace(b"\r\n", b"\n")).hexdigest()


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
        with open(path, "rb") as handle:
            raw = handle.read()
        want, content = WHOLE_FILES[path]
        if fingerprint(raw) != want:
            raise SystemExit(
                "ERROR: %s has changed since %s -- perhaps your notes. This\n"
                "       patch rewrites it whole and would lose them, so it\n"
                "       stops. Send the file to Claude. NOTHING was written."
                % (path, BUILT_ON))
        nl = "\r\n" if b"\r\n" in raw else "\n"
        results.append((path, content.replace("\n", nl), ["rewritten whole"]))
    for path in sorted(EDITS):
        with open(path, "rb") as handle:
            raw = handle.read()
        got = fingerprint(raw)
        if path in ANCHOR_ONLY:
            pass
        elif got != BASE[path]:
            raise SystemExit(
                "ERROR: %s is not the file this patch was built against.\n"
                "       expected %s, found %s. It has changed since\n"
                "       %s, or this patch has already run.\n"
                "       (Line endings are excluded, so they are not the cause.)\n"
                "       NOTHING was written." % (path, BASE[path], got, BUILT_ON))
        nl = "\r\n" if b"\r\n" in raw else "\n"
        text = raw.decode("utf-8").replace("\r\n", "\n")
        done = []
        for label, old, new, want in EDITS[path]:
            found = text.count(old)
            if found != want:
                raise SystemExit("ANCHOR FAIL (%s): expected %d match(es) in "
                                 "%s, found %d. NOTHING was written."
                                 % (label, want, path, found))
            text = text.replace(old, new)
            done.append(label)
        results.append((path, text.replace("\n", nl), done))
    for path, text, done in results:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in done:
            print("ok  %-36s %s" % (path, label))
    for path in sorted(NEW_FILES):
        with open(path, "wb") as handle:
            handle.write(NEW_FILES[path].encode("utf-8"))
        print("ok  %-36s created" % path)
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    for line in NEXT:
        print("  " + line)


if __name__ == "__main__":
    main()
