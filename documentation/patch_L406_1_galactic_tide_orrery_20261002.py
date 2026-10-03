#!/usr/bin/env python3
"""
patch_L406_1_galactic_tide_orrery_20261002.py -- ORRERY repo. The first of
two patches for L-406: the galactic tide is drawn in the galaxy's plane.

Built on orrery 5e42b00bdce82e895cc4b5a8d0aaa4d14283e9cb
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 0ffa451838dd5753710b3ec77d0d6f2f052f3d96
at https://github.com/tonylquintanilla/tonyquintanilla.github.io;
not touched by this patch -- patch_L406_2 is the gallery's half).

If patch_L405_handoff_20261002.py has already run, that is fine: it
touches neither file this patch fingerprints.

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code and click Run. The same as:
        python patch_L406_1_galactic_tide_orrery_20261002.py
    Then run orrery_maintenance_run.py the same way: it rebuilds the
    ledger's index, the skill manifest in PROJECT_INSTRUCTIONS.md, and
    data/constants_export.json, which the gallery reads. Then move this
    script into documentation/, commit and push. The gallery patch runs
    only after this push.

WHAT A VISITOR OF THE ORRERY SEES AFTER IT
    The Sun's "Galactic Tide Influence Oort" checkbox draws 2,000 points
    between 20,000 and 100,000 AU, tilted into the galaxy's plane (its
    pole sits about 60 degrees from the ecliptic's), sparse at that plane
    and at its poles and thickest halfway between. The hover reads, in
    Tony's approved words of 2026-10-02:
        Galactic Tide: sends comets in from the outer Oort cloud
        Tilted to the galaxy's plane, thickest halfway to its poles
        From 20,000 to 100,000 AU
        Where the comets really are is not known

WHAT CHANGES
    constants_new.py      three rows: the north galactic pole of J2000,
                          its right ascension in degrees, its declination
                          in arcseconds (exact) and, derived, in degrees.
                          Read from Liu, Zhu and Hu, arXiv:1110.6268,
                          eq. (2), Murray's 1989 Hipparcos standard.
    idealized_orbits.py   create_pole_transformation_matrix(ra, dec): the
                          planet matrix's arithmetic moved out unchanged
                          so the galactic pole can use it.
    solar_visualization_shells.py   create_sun_galactic_tide redrawn,
                          with its sources beside the code.
    skills/interactive-exhibit/SKILL.md   1.9 -> 1.10: Tony's rule for a
                          feature's info link (L-265), written down.
    PROJECT_INSTRUCTIONS.md   v3.78; v3.75 moves to
                          documentation/PROJECT_INSTRUCTIONS_HISTORY.md.
    LEDGER_CONSOLIDATED.md    L-406 opened; L-371 records the sort of
                          the 43; L-405 closed.

PERMANENT, though this script is thrown away: the three rows, the new
function, the redrawn tide, the skill text.

AFTER THE PUSH: reinstall interactive-exhibit (Settings > Skills) and
replace the Project's instructions with PROJECT_INSTRUCTIONS.md v3.78.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 2, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

BASE = {'LEDGER_CONSOLIDATED.md': 'a5a1f5a2ca793471712b8aca352d5454',
 'PROJECT_INSTRUCTIONS.md': '52ee15627e3e8bef73dbe620c572d66e',
 'constants_new.py': '929d9ac4cde63b7e03c7707d6544d6e7',
 'documentation/PROJECT_INSTRUCTIONS_HISTORY.md': '3401514d14d5f77b8a806b0e5e23b00b',
 'idealized_orbits.py': '5ed9b4c8a6cd967334008b47ba129c3e',
 'skills/interactive-exhibit/SKILL.md': 'a9377a6edd1b52f6de60084578638b6d',
 'solar_visualization_shells.py': '7353d5d69087145e822efed91644649a'}

EDITS = {'LEDGER_CONSOLIDATED.md': [('L-406 new item',
                             '#### [L-405] Skill text owed from the editor '
                             'fix and the drawer build (skills)\n'
                             '<!-- L:405 status:OPEN upd:2026-10-02 '
                             'section:A flag: rice: -->\n',
                             '#### [L-406] The galactic tide drawn in the '
                             "galaxy's plane (orrery + gallery, the Sun's "
                             'slice)\n'
                             '<!-- L:406 status:OPEN upd:2026-10-02 '
                             'section:A flag: rice: -->\n'
                             "- **Found 2026-10-02**, sorting the Sun room's "
                             '43 unlinked numbers\n'
                             "  (L-371). The galactic tide's words, on the "
                             'website and in the orrery,\n'
                             '  said its bodies are thinned near the '
                             "galaxy's plane. The drawing\n"
                             '  thinned them near the ecliptic, the plane of '
                             "Earth's orbit, and was\n"
                             "  densest at the ecliptic's poles. A code "
                             'comment in\n'
                             '  `gallery/feature_renderers.js` said the '
                             'hover admitted this; it did\n'
                             "  not. And the website's gating check\n"
                             '  `documentation/smoke_sun_shells.js` passed a '
                             'test named "tide is\n'
                             '  genuinely thinned at the galactic plane" '
                             'that measured the ecliptic:\n'
                             '  the check could not fail on the wrong '
                             'plane.\n'
                             "- **Tony's rulings, 2026-10-02.** Fix it now, "
                             'as a drawing choice made\n'
                             '  more correct ("this is the session to do any '
                             'fixing"). Draw it\n'
                             "  tilted into the galaxy's plane AND with the "
                             'pattern the source gives:\n'
                             "  sparse at the galaxy's plane and at its "
                             'poles, thickest halfway\n'
                             '  between. Draw it between the outer Oort '
                             "cloud's two stored edges,\n"
                             '  20,000 and 100,000 AU, instead of a typed '
                             '50,000 AU with a typed\n'
                             '  spread and cut-offs ("Confirmed as '
                             'recommended"). The words follow\n'
                             '  the discipline of the other features: the '
                             'drawing is a choice resting\n'
                             '  on the best information we can cite, the '
                             'hover is basic with any\n'
                             '  number cited, the info icon links to NASA or '
                             'Wikipedia. Old and new\n'
                             '  words were shown side by side and '
                             'confirmed.\n'
                             '- **Sources read 2026-10-02 by Claude Opus '
                             '5.5.** The pole: Liu, Zhu\n'
                             '  and Hu, arXiv:1110.6268, eq. (2), the J2000 '
                             'pole of Murray (1989),\n'
                             '  the Hipparcos standard. The pattern: '
                             'Delsemme (1987), A&A 187, 913,\n'
                             '  summary (aphelia avoid both galactic polar '
                             'caps and a strip along the\n'
                             '  galactic equator); Matese and Whitmire, '
                             'arXiv:1004.4584, sec. 2.2\n'
                             '  (the dominant tidal term goes as |sin B cos '
                             'B|, peaks near 45\n'
                             '  degrees). Dissent, said in the panel: '
                             'Higuchi (2020), arXiv:2008.04324\n'
                             '  (AJ 160, 134); Rickman et al. (2008) as '
                             'Matese and Whitmire report.\n'
                             '  The info link stays Wikipedia\'s "Galactic '
                             'tide", which meets the L-265\n'
                             '  rule.\n'
                             '- **Built 2026-10-02.** Orrery '
                             '`patch_L406_1_galactic_tide_orrery_20261002.py`:\n'
                             "  three rows in `constants_new.py` (the pole's "
                             'right ascension in\n'
                             '  degrees, its declination in arcseconds and, '
                             'derived, in degrees);\n'
                             '  '
                             '`idealized_orbits.create_pole_transformation_matrix(ra_deg, '
                             'dec_deg)`,\n'
                             "  the planet matrix's arithmetic moved out "
                             'unchanged (identical\n'
                             '  matrices for eight bodies, checked); the '
                             "orrery's tide redrawn;\n"
                             '  interactive-exhibit 1.10 with the link rule; '
                             'protocol v3.78. Gallery\n'
                             '  '
                             '`patch_L406_2_galactic_tide_gallery_20261002.py`: '
                             "the tide's entry\n"
                             '  in `data/objects_config.json`, its drawing '
                             'in\n'
                             '  `gallery/feature_renderers.js`, and the '
                             'corrected check. Retired: the\n'
                             '  0.5 asymmetry, the 0.3 spread and the 0.5 '
                             'and 1.5 cut-offs -- four of\n'
                             "  L-371's 19 eyeballed numbers -- and the "
                             'declared 50,000 AU distance.\n'
                             "- **Fixed in passing, reported:** the Sun's "
                             '`_comment` in\n'
                             '  `data/objects_config.json` said the custom '
                             'geometry is "NOT here";\n'
                             '  all four shapes have been there since '
                             'L-234.\n'
                             '**Gap:** Tony: run patch 1, run '
                             '`orrery_maintenance_run.py`, commit and\n'
                             'push the orrery; then patch 2, the cache '
                             'builder, and\n'
                             '`gallery_maintenance_run.py`, commit and push '
                             'the gallery; then look at\n'
                             'the tide on the phone (Mode 5). The next '
                             'session confirms its loaded\n'
                             'interactive-exhibit reads 1.10.\n'
                             '**Ref:** L-371; L-265; L-386; '
                             'skills/interactive-exhibit/SKILL.md;\n'
                             'orrery `solar_visualization_shells.py`, '
                             '`idealized_orbits.py`,\n'
                             '`constants_new.py`; gallery '
                             '`gallery/feature_renderers.js`,\n'
                             '`documentation/smoke_sun_shells.js`.\n'
                             '\n'
                             '#### [L-405] Skill text owed from the editor '
                             'fix and the drawer build (skills)\n'
                             '<!-- L:405 status:DONE upd:2026-10-02 '
                             'section:C flag: rice: -->\n'),
                            ('L-405 closed',
                             '**Gap:** The next session confirms its loaded '
                             'copies read\n'
                             'interactive-exhibit 1.9 and '
                             'ledger-and-session-records 1.14, then\n'
                             'closes this item.\n',
                             '- **Closed 2026-10-02, the next session.** Its '
                             'loaded copies read\n'
                             '  interactive-exhibit 1.9 and '
                             'ledger-and-session-records 1.14, matching\n'
                             '  the manifest. Nothing in the body is left '
                             'undone: the harness is\n'
                             '  filed, and the bump rule stands as pushed. '
                             'interactive-exhibit went\n'
                             '  on to 1.10 the same day (L-406).\n'
                             '**Gap:** None -- closed 2026-10-02.\n'),
                            ('L-371 sorted',
                             '  the same date.\n'
                             "**Gap:** The Sun's slice: sort the 43, give "
                             'each measured one a row and a count, and print '
                             'by the count.\n',
                             '  the same date.\n'
                             '- **Sorted 2026-10-02** (Claude Opus 5.5; the '
                             "test is the skill's --\n"
                             '  does changing the number move WHERE '
                             'something is drawn or only HOW\n'
                             '  it looks). The 43 are exactly the four '
                             "`drawing` blocks of the Sun's\n"
                             '  hand-built shapes: streamer belt 18, Hills '
                             'cloud torus 7, clumpy outer\n'
                             '  Oort 10, galactic tide 8. None is a '
                             'measurement, so none needs a row.\n'
                             '  Rendering settings, 22, stay where they are: '
                             "the streamer's four point\n"
                             '  counts, jitter, seed, brightness and two '
                             'marker sizes; and each Oort\n'
                             "  shape's point counts, seed, opacity and "
                             'marker size. Copies of linked\n'
                             "  rows, 2: the streamer's base radius (the "
                             'photosphere) and its outer\n'
                             '  radius, 20.0 typed where the orrery works '
                             'out 19.9955, past the\n'
                             '  Alfven surface where nothing shows. '
                             'Eyeballed shape numbers, 19, do\n'
                             "  not promote: the streamer's two widths, "
                             'helmet curve, stalk taper,\n'
                             "  fade curve, warp and lobe count; the torus's "
                             'thickness, flattening\n'
                             '  and 10% scatter (borderline: it pushes '
                             'points past the stated edges);\n'
                             "  the clumps' count, two sizes and two "
                             'concentration numbers; the\n'
                             "  tide's spread, two cut-offs and asymmetry.\n"
                             "- **The tide's four went on 2026-10-02 "
                             '(L-406)**, replaced by sourced\n'
                             '  rows and a sourced shape. Fifteen eyeballed '
                             'numbers remain in the\n'
                             '  streamer belt, the torus and the clumps, to '
                             'be taken one drawing at a\n'
                             '  time, each needing its own source hunt.\n'
                             "**Gap:** The Sun's slice, second half: the "
                             "numbers already linked -- L-386's rows stored "
                             'in another unit, and the radius lines that '
                             'print with no count. Then the fifteen '
                             'eyeballed shape numbers, one drawing at a '
                             'time.\n'),
                            ('L-371 date',
                             '<!-- L:371 status:OPEN upd:2026-09-29 '
                             'section:A flag: rice: -->',
                             '<!-- L:371 status:OPEN upd:2026-10-02 '
                             'section:A flag: rice: -->')],
 'PROJECT_INSTRUCTIONS.md': [('header v3.78',
                              'Tony Quintanilla, PE | Claude | v3.77 | '
                              'October 2, 2026\n'
                              '\n'
                              'Cut from b3cfc780 at',
                              'Tony Quintanilla, PE | Claude | v3.78 | '
                              'October 2, 2026\n'
                              '\n'
                              'Cut from 5e42b00b at'),
                             ('v3.78 entry; v3.75 moves down',
                              'that file. An entry lives in exactly one '
                              'place, never both.\n'
                              '\n'
                              'v3.77 (October 2, 2026):',
                              'that file. An entry lives in exactly one '
                              'place, never both.\n'
                              '\n'
                              'v3.78 (October 2, 2026): No rule changed in '
                              'this document. ONE\n'
                              'skill bump, one version (L-406): '
                              'interactive-exhibit 1.9 -> 1.10.\n'
                              "THE GALACTIC TIDE IS DRAWN IN THE GALAXY'S "
                              'PLANE.\n'
                              '\n'
                              "WHAT PROMPTED IT. Sorting the Sun room's 43 "
                              'unlinked numbers (L-371)\n'
                              "found the galactic tide's words saying its "
                              'bodies are thinned near the\n'
                              "galaxy's plane while the drawing thinned them "
                              "near the ecliptic. Tony's\n"
                              'ruling of 2026-10-02: fix it now, as a '
                              'drawing choice made more\n'
                              'correct. The source then showed the pattern '
                              'was wrong too: comets the\n'
                              "tide sends in avoid the galaxy's plane AND "
                              'its poles. Tony confirmed\n'
                              'drawing both, and drawing the tide between '
                              "the outer Oort cloud's two\n"
                              'stored edges instead of a typed 50,000 AU.\n'
                              '\n'
                              'WHAT THE SKILL NOW SAYS. Asked whether the '
                              "skills cover how a feature's\n"
                              'hover, info panel and drawing are written, '
                              'the answer was that the\n'
                              'hover and the drawing were covered and the '
                              "info link was not: Tony's\n"
                              'rule lived only on L-265. interactive-exhibit '
                              '1.10 writes it down -- a\n'
                              'NASA page where one is specific to the '
                              'feature, otherwise English\n'
                              'Wikipedia, the corona the one named '
                              'exception.\n'
                              '\n'
                              'THE BUILD. Orrery patch_L406_1 adds the '
                              'galactic pole of J2000 to\n'
                              'constants_new.py, gives the pole matrix its '
                              'own function, and redraws\n'
                              "the orrery's tide; gallery patch_L406_2 "
                              "redraws the website's tide in\n"
                              "Tony's approved words and corrects the check "
                              'that measured the\n'
                              "ecliptic under the galactic plane's name.\n"
                              '\n'
                              'THE OBLIGATION TRAVELS. This session loaded '
                              '1.9. The next session\n'
                              'confirms its loaded copy reads '
                              'interactive-exhibit 1.10 before any\n'
                              'exhibit work.\n'
                              '\n'
                              'The header stamp and the SHA anchor move with '
                              'this entry.\n'
                              '\n'
                              'Version history: v3.75 moves down to\n'
                              'documentation/PROJECT_INSTRUCTIONS_HISTORY.md '
                              'PART 1 to keep three\n'
                              'resident.\n'
                              '\n'
                              'v3.77 (October 2, 2026):'),
                             ('v3.75 leaves the resident three',
                              'v3.75 (October 1, 2026): No rule changed in '
                              'this document. TWO\n'
                              'skill bumps, one version each, for one build '
                              '(L-398):\n'
                              'provenance-discipline 2.22 -> 2.23 and '
                              'interactive-exhibit 1.6 -> 1.7.\n'
                              'A COMPUTED DISTANCE PRINTS WHAT ITS ERRORS '
                              'EARN.\n'
                              '\n'
                              "WHAT PROMPTED IT. Tony's question on "
                              '2026-10-01 about the Solar System\n'
                              'room: "does Horizons serve the distance to '
                              'pluto with 9 significant\n'
                              'digits?" It did not. The room\'s figures came '
                              'from how closely the page\n'
                              'reproduces Horizons, not from how well JPL '
                              'knows where the planet is,\n'
                              "and Pluto printed ten figures where JPL's own "
                              'report says several\n'
                              'thousand kilometres.\n'
                              '\n'
                              'WHAT THE SKILLS NOW SAY. '
                              'provenance-discipline gains A Computed\n'
                              'Position Prints What Its Errors Earn: a '
                              'distance worked out at display\n'
                              "time prints to the Report test's place for "
                              'the LARGER of the measured\n'
                              "drift and the source's own accuracy (Tony: "
                              '"use whichever is larger").\n'
                              'Its second half is the case the source '
                              'forced: an accuracy stated only\n'
                              'in words is stored as the place those words '
                              'report to, the place the\n'
                              'Report test gives for every value the words '
                              'can mean, the coarser where\n'
                              'they could mean two, and never as a number '
                              'the source does not print.\n'
                              "JPL's 2014 report gives 1 km, 100 km and "
                              '10,000 km for its three groups.\n'
                              'interactive-exhibit records the rooms section '
                              'of objects_config.json\n'
                              'and the words a drawer row may carry, the '
                              '"position_accuracy" link\n'
                              "and Tony's sentence for a body with none, and "
                              'the second file moved\n'
                              'out of interactive.html.\n'
                              '\n'
                              'ONE PLACE COARSER THAN THE PLAN. The session '
                              'plan said the place the\n'
                              'words name, thousands for "several thousand". '
                              'Every value those words\n'
                              'allow reports to ten-thousands, so that is '
                              'what the rule gives. Tony\n'
                              'confirmed it as recommended on 2026-10-01.\n'
                              '\n'
                              'THE BUILD. Orrery patch patch_L398_1 adds the '
                              'three rows to\n'
                              'constants_new.py; gallery patch patch_L398_2 '
                              'links nine bodies to them\n'
                              'and prints by them, with a new gating check.\n'
                              '\n'
                              'THE OBLIGATION TRAVELS. This session loaded '
                              '2.22 and 1.6. The next\n'
                              'session confirms its loaded copies read '
                              'provenance-discipline 2.23 and\n'
                              'interactive-exhibit 1.7 before any '
                              'provenance, constants_new.py or\n'
                              'exhibit work.\n'
                              '\n'
                              'The header stamp and the SHA anchor move with '
                              'this entry.\n'
                              '\n'
                              'Version history: v3.72 moves down to\n'
                              'documentation/PROJECT_INSTRUCTIONS_HISTORY.md '
                              'PART 1 to keep three\n'
                              'resident.\n'
                              '\n'
                              'Functional for Claude, readable for human, '
                              'signal preserved.',
                              'Functional for Claude, readable for human, '
                              'signal preserved.')],
 'constants_new.py': [('three galactic pole rows',
                       '# The pole directions of the bodies the orrery draws '
                       'with an axis, as ICRF\n',
                       'GALACTIC_NORTH_POLE_RA_J2000_DEG = 192.85948125\n'
                       '# Unit: deg\n'
                       '# Status: declared 2026-10-02 -- a frame definition, '
                       'not a measurement\n'
                       '# Figures: exact -- a frame definition; the source '
                       'prints it as\n'
                       '# Figures+: 12h 51m 26.2755s, which is exactly '
                       '192.85948125 degrees.\n'
                       '# Declared: the right ascension of the north '
                       'galactic pole of the year\n'
                       '# Declared+: 2000, the pole of the galactic '
                       'coordinate system defined by\n'
                       '# Declared+: the IAU in 1958 and carried to J2000 by '
                       "Murray's 1989\n"
                       '# Declared+: transformation, which the Hipparcos '
                       'team adopted as the\n'
                       '# Declared+: standard. It sets the plane the '
                       'galactic tide is drawn\n'
                       '# Declared+: about '
                       '(solar_visualization_shells.create_sun_galactic_tide\n'
                       "# Declared+: and the gallery's tide_field). The "
                       'source also reports that\n'
                       '# Declared+: the plane fitted to modern 2MASS and '
                       'radio catalogues is\n'
                       '# Declared+: inclined 0.4 to 0.6 degrees more than '
                       'this one, far below\n'
                       '# Declared+: anything the drawing shows.\n'
                       '# Read: eq. (2), sec. 1, of the document named in '
                       'the Source line,\n'
                       '# Read+: 2026-10-02, Claude Opus 5.5.\n'
                       '# Source: Liu, Zhu and Hu, "Constructing a Galactic '
                       'coordinate system\n'
                       '# Source+: based on near-infrared and radio '
                       'catalogs", arXiv:1110.6268,\n'
                       '# Source+: eq. (2) -- the north galactic pole at '
                       'J2000.0, alpha =\n'
                       "# Source+: 12h 51m 26.2755s, delta = +27 deg 07' "
                       '41.704", as derived by\n'
                       '# Source+: Murray (1989) and adopted by the '
                       'Hipparcos team as the\n'
                       '# Source+: standard transformation. The layer below: '
                       'Murray, C. A. 1989,\n'
                       '# Source+: A&A 218, 325; ESA 1997, The Hipparcos and '
                       'Tycho Catalogues,\n'
                       '# Source+: ESA SP-1200.\n'
                       '# Ref: https://arxiv.org/pdf/1110.6268\n'
                       '# Note: added 2026-10-02 (L-406). Until then the '
                       'galactic tide was drawn\n'
                       '# Note+: about the ecliptic while its words said the '
                       "galaxy's plane.\n"
                       '\n'
                       'GALACTIC_NORTH_POLE_DEC_J2000_ARCSEC = 97661.704\n'
                       '# Unit: arcsec\n'
                       '# Status: declared 2026-10-02 -- a frame definition, '
                       'not a measurement\n'
                       '# Figures: exact -- a frame definition; the source '
                       'prints it as\n'
                       '# Figures+: +27 deg 07\' 41.704", which is exactly '
                       '97,661.704 arcseconds.\n'
                       '# Declared: the declination of the north galactic '
                       'pole of the year 2000,\n'
                       '# Declared+: the companion of '
                       'GALACTIC_NORTH_POLE_RA_J2000_DEG. Stored in\n'
                       '# Declared+: arcseconds because that is exact; in '
                       'degrees it does not end.\n'
                       '# Read: as GALACTIC_NORTH_POLE_RA_J2000_DEG, '
                       '2026-10-02, Claude Opus 5.5.\n'
                       '# Source: as GALACTIC_NORTH_POLE_RA_J2000_DEG.\n'
                       '# Ref: https://arxiv.org/pdf/1110.6268\n'
                       '\n'
                       'GALACTIC_NORTH_POLE_DEC_J2000_DEG = '
                       'GALACTIC_NORTH_POLE_DEC_J2000_ARCSEC / '
                       'ARCSEC_PER_DEG\n'
                       "# Derived: the pole's declination in degrees, "
                       '97661.704 / 3600\n'
                       '# Derived+: = 27.128251111...\n'
                       '# Unit: deg\n'
                       '# Status: derived 2026-10-02 -- inherits '
                       'GALACTIC_NORTH_POLE_DEC_J2000_ARCSEC,\n'
                       '# Status+: ARCSEC_PER_DEG\n'
                       '# Figures: exact -- both inputs are exact.\n'
                       '# Note: drawn, never printed, so it carries no print '
                       'count.\n'
                       '\n'
                       '# The pole directions of the bodies the orrery draws '
                       'with an axis, as ICRF\n')],
 'documentation/PROJECT_INSTRUCTIONS_HISTORY.md': [('v3.75 arrives',
                                                    '(Moved down from the '
                                                    'resident protocol on '
                                                    '2026-10-02 when\n'
                                                    'v3.77 made a fourth '
                                                    'entry.)\n'
                                                    '\n'
                                                    '================================================================\n'
                                                    'PART 2 -- LESSONS '
                                                    'REMOVED',
                                                    '(Moved down from the '
                                                    'resident protocol on '
                                                    '2026-10-02 when\n'
                                                    'v3.77 made a fourth '
                                                    'entry.)\n'
                                                    '\n'
                                                    'v3.75 (October 1, '
                                                    '2026): No rule changed '
                                                    'in this document. TWO\n'
                                                    'skill bumps, one '
                                                    'version each, for one '
                                                    'build (L-398):\n'
                                                    'provenance-discipline '
                                                    '2.22 -> 2.23 and '
                                                    'interactive-exhibit 1.6 '
                                                    '-> 1.7.\n'
                                                    'A COMPUTED DISTANCE '
                                                    'PRINTS WHAT ITS ERRORS '
                                                    'EARN.\n'
                                                    '\n'
                                                    'WHAT PROMPTED IT. '
                                                    "Tony's question on "
                                                    '2026-10-01 about the '
                                                    'Solar System\n'
                                                    'room: "does Horizons '
                                                    'serve the distance to '
                                                    'pluto with 9 '
                                                    'significant\n'
                                                    'digits?" It did not. '
                                                    "The room's figures came "
                                                    'from how closely the '
                                                    'page\n'
                                                    'reproduces Horizons, '
                                                    'not from how well JPL '
                                                    'knows where the planet '
                                                    'is,\n'
                                                    'and Pluto printed ten '
                                                    "figures where JPL's own "
                                                    'report says several\n'
                                                    'thousand kilometres.\n'
                                                    '\n'
                                                    'WHAT THE SKILLS NOW '
                                                    'SAY. '
                                                    'provenance-discipline '
                                                    'gains A Computed\n'
                                                    'Position Prints What '
                                                    'Its Errors Earn: a '
                                                    'distance worked out at '
                                                    'display\n'
                                                    'time prints to the '
                                                    "Report test's place for "
                                                    'the LARGER of the '
                                                    'measured\n'
                                                    "drift and the source's "
                                                    'own accuracy (Tony: '
                                                    '"use whichever is '
                                                    'larger").\n'
                                                    'Its second half is the '
                                                    'case the source forced: '
                                                    'an accuracy stated '
                                                    'only\n'
                                                    'in words is stored as '
                                                    'the place those words '
                                                    'report to, the place '
                                                    'the\n'
                                                    'Report test gives for '
                                                    'every value the words '
                                                    'can mean, the coarser '
                                                    'where\n'
                                                    'they could mean two, '
                                                    'and never as a number '
                                                    'the source does not '
                                                    'print.\n'
                                                    "JPL's 2014 report gives "
                                                    '1 km, 100 km and 10,000 '
                                                    'km for its three '
                                                    'groups.\n'
                                                    'interactive-exhibit '
                                                    'records the rooms '
                                                    'section of '
                                                    'objects_config.json\n'
                                                    'and the words a drawer '
                                                    'row may carry, the '
                                                    '"position_accuracy" '
                                                    'link\n'
                                                    "and Tony's sentence for "
                                                    'a body with none, and '
                                                    'the second file moved\n'
                                                    'out of '
                                                    'interactive.html.\n'
                                                    '\n'
                                                    'ONE PLACE COARSER THAN '
                                                    'THE PLAN. The session '
                                                    'plan said the place '
                                                    'the\n'
                                                    'words name, thousands '
                                                    'for "several thousand". '
                                                    'Every value those '
                                                    'words\n'
                                                    'allow reports to '
                                                    'ten-thousands, so that '
                                                    'is what the rule gives. '
                                                    'Tony\n'
                                                    'confirmed it as '
                                                    'recommended on '
                                                    '2026-10-01.\n'
                                                    '\n'
                                                    'THE BUILD. Orrery patch '
                                                    'patch_L398_1 adds the '
                                                    'three rows to\n'
                                                    'constants_new.py; '
                                                    'gallery patch '
                                                    'patch_L398_2 links nine '
                                                    'bodies to them\n'
                                                    'and prints by them, '
                                                    'with a new gating '
                                                    'check.\n'
                                                    '\n'
                                                    'THE OBLIGATION TRAVELS. '
                                                    'This session loaded '
                                                    '2.22 and 1.6. The next\n'
                                                    'session confirms its '
                                                    'loaded copies read '
                                                    'provenance-discipline '
                                                    '2.23 and\n'
                                                    'interactive-exhibit 1.7 '
                                                    'before any provenance, '
                                                    'constants_new.py or\n'
                                                    'exhibit work.\n'
                                                    '\n'
                                                    'The header stamp and '
                                                    'the SHA anchor move '
                                                    'with this entry.\n'
                                                    '\n'
                                                    'Version history: v3.72 '
                                                    'moves down to\n'
                                                    'documentation/PROJECT_INSTRUCTIONS_HISTORY.md '
                                                    'PART 1 to keep three\n'
                                                    'resident.\n'
                                                    '\n'
                                                    '(Moved down from the '
                                                    'resident protocol on '
                                                    '2026-10-02 when\n'
                                                    'v3.78 made a fourth '
                                                    'entry.)\n'
                                                    '\n'
                                                    '================================================================\n'
                                                    'PART 2 -- LESSONS '
                                                    'REMOVED')],
 'idealized_orbits.py': [('stamp',
                          "the frame's year-2000 axis when Horizons cannot "
                          'be reached)\n',
                          "the frame's year-2000 axis when Horizons cannot "
                          'be reached)\n'
                          "Module updated: October 2, 2026 with Anthropic's "
                          'Claude Opus 5.5\n'
                          '(L-406: the pole-to-ecliptic matrix is '
                          'create_pole_transformation_matrix\n'
                          "(ra_deg, dec_deg), so a pole that is not a body's "
                          '-- the galactic pole\n'
                          'the galactic tide is drawn about -- uses the same '
                          'construction.\n'
                          'create_planet_transformation_matrix finds the '
                          "body's pole and calls it;\n"
                          'the arithmetic did not change)\n'),
                         ('extract create_pole_transformation_matrix',
                          'def '
                          'create_planet_transformation_matrix(planet_name):\n',
                          'def create_pole_transformation_matrix(ra_deg, '
                          'dec_deg):\n'
                          '    """\n'
                          '    The matrix that turns coordinates measured '
                          'about a pole into the\n'
                          "    drawing's frame, the ecliptic of J2000.\n"
                          '\n'
                          '    The pole is given as ICRF right ascension and '
                          'declination in degrees\n'
                          '    (equatorial, J2000). Its columns are the '
                          'basis vectors: x along the\n'
                          "    ascending node of the pole's equator on the "
                          'ecliptic, z along the\n'
                          '    pole, y completing a right-handed set. So '
                          'matrix @ [x, y, z] takes a\n'
                          '    point given about the pole into ecliptic '
                          'coordinates.\n'
                          '\n'
                          '    Moved out of '
                          'create_planet_transformation_matrix on '
                          '2026-10-02\n'
                          '    (L-406) unchanged, so that the galactic pole '
                          "can use it as a planet's\n"
                          '    pole does.\n'
                          '\n'
                          '    Module updated: October 2, 2026 with '
                          "Anthropic's Claude Opus 5.5\n"
                          '    """\n'
                          '    ra_pole = np.radians(ra_deg)\n'
                          '    dec_pole = np.radians(dec_deg)\n'
                          '\n'
                          '    sin_dec = np.sin(dec_pole)\n'
                          '    cos_dec = np.cos(dec_pole)\n'
                          '    sin_ra = np.sin(ra_pole)\n'
                          '    cos_ra = np.cos(ra_pole)\n'
                          '\n'
                          '    # The pole vector -- RA/Dec are EQUATORIAL '
                          '(J2000) coordinates.\n'
                          '    x_pole = cos_dec * cos_ra\n'
                          '    y_pole = cos_dec * sin_ra\n'
                          '    z_pole = sin_dec\n'
                          '\n'
                          '    # U3 fix (June 2026): the visualization frame '
                          'is ECLIPTIC (J2000), but the pole\n'
                          '    # above is in the EQUATORIAL frame. Rotate it '
                          'into ecliptic by the mean obliquity\n'
                          '    # before building the basis. Omitting this '
                          'left belts/rings ~23.4 deg off the\n'
                          '    # (ecliptic-native) moon orbits -- caught by '
                          "Tony's Mode-5 render, not the container test.\n"
                          '    # L-322 Stage D (2026-09-23): the angle '
                          'Horizons builds its ecliptic of\n'
                          '    # J2000 with, read from constants_new.py. It '
                          "is the frame's angle, the\n"
                          "    # IAU 1976 value, not Earth's tilt; the label "
                          '"IAU 2006" that stood\n'
                          '    # here named a standard whose value is '
                          '84381.406 arcseconds, not this.\n'
                          '    _OBLIQUITY = '
                          'np.radians(EARTH_OBLIQUITY_J2000_DEG)\n'
                          '    _ce, _se = np.cos(_OBLIQUITY), '
                          'np.sin(_OBLIQUITY)\n'
                          '    y_pole, z_pole = (y_pole * _ce + z_pole * '
                          '_se,\n'
                          '                      -y_pole * _se + z_pole * '
                          '_ce)\n'
                          '\n'
                          "    # Find the ascending node of the pole's "
                          'equator on the ecliptic\n'
                          '    # This is perpendicular to the pole and in '
                          'the ecliptic plane\n'
                          '    x_node = -y_pole / np.sqrt(x_pole**2 + '
                          'y_pole**2)\n'
                          '    y_node = x_pole / np.sqrt(x_pole**2 + '
                          'y_pole**2)\n'
                          '    z_node = 0\n'
                          '\n'
                          '    # Create orthogonal basis vectors\n'
                          '    x_basis = np.array([x_node, y_node, z_node])\n'
                          '    z_basis = np.array([x_pole, y_pole, z_pole])\n'
                          '    y_basis = np.cross(z_basis, x_basis)\n'
                          '\n'
                          '    # Construct the transformation matrix\n'
                          '    transform_matrix = np.vstack((x_basis, '
                          'y_basis, z_basis)).T\n'
                          '\n'
                          '    return transform_matrix\n'
                          '\n'
                          '\n'
                          'def '
                          'create_planet_transformation_matrix(planet_name):\n'),
                         ('planet matrix calls the pole matrix',
                          '        pole = planet_poles[planet_name]\n'
                          "    ra_pole = np.radians(pole['ra'])\n"
                          "    dec_pole = np.radians(pole['dec'])\n"
                          '    \n'
                          "    # Calculate the rotation matrix from planet's "
                          'equatorial to ecliptic\n'
                          '    sin_dec = np.sin(dec_pole)\n'
                          '    cos_dec = np.cos(dec_pole)\n'
                          '    sin_ra = np.sin(ra_pole)\n'
                          '    cos_ra = np.cos(ra_pole)\n'
                          '    \n'
                          "    # Planet's north pole vector -- RA/Dec are "
                          'EQUATORIAL (J2000) coordinates.\n'
                          '    x_pole = cos_dec * cos_ra\n'
                          '    y_pole = cos_dec * sin_ra\n'
                          '    z_pole = sin_dec\n'
                          '\n'
                          '    # U3 fix (June 2026): the visualization frame '
                          'is ECLIPTIC (J2000), but the pole\n'
                          '    # above is in the EQUATORIAL frame. Rotate it '
                          'into ecliptic by the mean obliquity\n'
                          '    # before building the basis. Omitting this '
                          'left belts/rings ~23.4 deg off the\n'
                          '    # (ecliptic-native) moon orbits -- caught by '
                          "Tony's Mode-5 render, not the container test.\n"
                          '    # L-322 Stage D (2026-09-23): the angle '
                          'Horizons builds its ecliptic of\n'
                          '    # J2000 with, read from constants_new.py. It '
                          "is the frame's angle, the\n"
                          "    # IAU 1976 value, not Earth's tilt; the label "
                          '"IAU 2006" that stood\n'
                          '    # here named a standard whose value is '
                          '84381.406 arcseconds, not this.\n'
                          '    _OBLIQUITY = '
                          'np.radians(EARTH_OBLIQUITY_J2000_DEG)\n'
                          '    _ce, _se = np.cos(_OBLIQUITY), '
                          'np.sin(_OBLIQUITY)\n'
                          '    y_pole, z_pole = (y_pole * _ce + z_pole * '
                          '_se,\n'
                          '                      -y_pole * _se + z_pole * '
                          '_ce)\n'
                          '\n'
                          "    # Find the ascending node of planet's equator "
                          'on the ecliptic\n'
                          '    # This is perpendicular to the pole and in '
                          'the ecliptic plane\n'
                          '    x_node = -y_pole / np.sqrt(x_pole**2 + '
                          'y_pole**2)\n'
                          '    y_node = x_pole / np.sqrt(x_pole**2 + '
                          'y_pole**2)\n'
                          '    z_node = 0\n'
                          '    \n'
                          '    # Create orthogonal basis vectors\n'
                          '    x_basis = np.array([x_node, y_node, z_node])\n'
                          '    z_basis = np.array([x_pole, y_pole, z_pole])\n'
                          '    y_basis = np.cross(z_basis, x_basis)\n'
                          '    \n'
                          '    # Construct the transformation matrix\n'
                          '    transform_matrix = np.vstack((x_basis, '
                          'y_basis, z_basis)).T\n'
                          '    \n'
                          '    return transform_matrix\n',
                          '        pole = planet_poles[planet_name]\n'
                          '    # L-406 (2026-10-02): the construction lives '
                          'in\n'
                          '    # create_pole_transformation_matrix above, '
                          'unchanged.\n'
                          '    return '
                          "create_pole_transformation_matrix(pole['ra'], "
                          "pole['dec'])\n")],
 'skills/interactive-exhibit/SKILL.md': [("fires_when: a feature's info link",
                                          'testing a room headlessly '
                                          '(tools/headless); carding an '
                                          'exhibit in Studio\n',
                                          'testing a room headlessly '
                                          '(tools/headless); carding an '
                                          'exhibit in Studio;\n'
                                          "choosing a feature's info link "
                                          '(NASA or Wikipedia)\n'),
                                         ('version 1.10',
                                          'Skill version: 1.9 | 2026-10-02, '
                                          "with Anthropic's Claude Opus 5.5, "
                                          'from\n'
                                          'orrery @ b3cfc780 and gallery @ '
                                          'cfc53490,',
                                          'Skill version: 1.10 | 2026-10-02, '
                                          "with Anthropic's Claude Opus 5.5, "
                                          'from\n'
                                          'orrery @ 5e42b00b and gallery @ '
                                          '0ffa4518. v1.10 (L-406) writes '
                                          'down\n'
                                          "Tony's rule for a feature's info "
                                          'link, which lived only on L-265: '
                                          'a\n'
                                          'NASA page where one is specific '
                                          'to the feature, otherwise '
                                          'English\n'
                                          'Wikipedia, with the corona the '
                                          'one named exception. Asked on\n'
                                          '2026-10-02, while the galactic '
                                          'tide was being redrawn, whether '
                                          'the\n'
                                          "skills covered how a feature's "
                                          'hover, info panel and drawing '
                                          'are\n'
                                          'written; the hover and the '
                                          'drawing were covered and the link '
                                          'was not.\n'
                                          'Earlier: 1.9 | 2026-10-02, with '
                                          "Anthropic's Claude Opus 5.5, "
                                          'from\n'
                                          'orrery @ b3cfc780 and gallery @ '
                                          'cfc53490,'),
                                         ("section: a feature's info link",
                                          'follow under '
                                          'orrery-coding-conventions 1.9 and '
                                          'L-321.)\n',
                                          'follow under '
                                          'orrery-coding-conventions 1.9 and '
                                          'L-321.)\n'
                                          '\n'
                                          "### A feature's info link: NASA "
                                          'if specific, else Wikipedia '
                                          '[QUALITY]\n'
                                          'Every drawn feature carries '
                                          'exactly one link, its `info_url` '
                                          'in\n'
                                          '`data/objects_config.json` '
                                          "(Earth's two belts carry the "
                                          'parallel list\n'
                                          '`info_urls`), and the i panel '
                                          'shows it as "Read more at NASA" '
                                          'or "Read\n'
                                          'more at Wikipedia". Tony\'s rule '
                                          'of 2026-09-02, until v1.10 only '
                                          'on the\n'
                                          'ledger (L-265):\n'
                                          '- A NASA page where one is '
                                          'SPECIFIC to the feature. A hub '
                                          'page about\n'
                                          '  the Sun, the atmosphere or the '
                                          'solar system in general does not\n'
                                          '  count.\n'
                                          "- Otherwise the feature's English "
                                          'Wikipedia article.\n'
                                          '- One exception, by his word: the '
                                          "corona shells take Wikipedia's "
                                          '"Solar\n'
                                          '  corona", because NASA\'s only '
                                          'corona page is Space Place, '
                                          'written for\n'
                                          '  children.\n'
                                          '- Every link is a URL a search or '
                                          'fetch returned live on the day it '
                                          'was\n'
                                          '  chosen. None is recalled.\n'
                                          'WHY A LINK AND NOT PROSE (Tony, '
                                          '2026-08-30): paragraphs written '
                                          'for the\n'
                                          'panel would be claims crossing to '
                                          'the website, where nothing '
                                          'scores\n'
                                          'them again. A link moves that '
                                          'burden to NASA or Wikipedia, who '
                                          'maintain\n'
                                          'the page. The words a room does '
                                          'serve -- `description`, `about`,\n'
                                          '`note` -- follow the hover rule '
                                          'above, and any number in them '
                                          'carries\n'
                                          'its source.\n'
                                          'A redrawn feature keeps its link '
                                          'while the page still describes '
                                          'what is\n'
                                          'drawn: the galactic tide kept '
                                          'Wikipedia\'s "Galactic tide" when '
                                          'it was\n'
                                          "redrawn in the galaxy's plane "
                                          '(L-406). Choosing the link is '
                                          'method and\n'
                                          'needs no ruling; whether a '
                                          'feature is drawn at all is '
                                          "Tony's.\n")],
 'solar_visualization_shells.py': [('stamp',
                                    'Module updated: September 28, 2026 with '
                                    "Anthropic's Claude Opus 5.5\n"
                                    '(L-345, patch D20:',
                                    'Module updated: October 2, 2026 with '
                                    "Anthropic's Claude Opus 5.5\n"
                                    '(L-406: the galactic tide is drawn '
                                    "tilted into the galaxy's plane, about\n"
                                    'the galactic pole of J2000 from '
                                    'constants_new.py, between the outer '
                                    'Oort\n'
                                    "cloud's two edges, with its density "
                                    "following the tide's strength --\n"
                                    "sparse at the galaxy's plane and poles, "
                                    'thickest halfway between. It had\n'
                                    'been drawn about the ecliptic, densest '
                                    'at the poles, at a typed 50,000\n'
                                    "AU, while its words said the galaxy's "
                                    "plane. Hover rewritten in Tony's\n"
                                    'approved words of 2026-10-02.)\n'
                                    '\n'
                                    'Module updated: September 28, 2026 with '
                                    "Anthropic's Claude Opus 5.5\n"
                                    '(L-345, patch D20:'),
                                   ('import the galactic pole rows',
                                    '# L-322 Stage D, patch D17: print rows '
                                    'by the counts their rows state.\n'
                                    'from constants_rows import figures_of, '
                                    'exact_text, format_prints, '
                                    'conversion_text\n',
                                    '# L-322 Stage D, patch D17: print rows '
                                    'by the counts their rows state.\n'
                                    'from constants_rows import figures_of, '
                                    'exact_text, format_prints, '
                                    'conversion_text\n'
                                    '# L-406: the pole the galactic tide is '
                                    'drawn about.\n'
                                    'from constants_new import '
                                    '(GALACTIC_NORTH_POLE_RA_J2000_DEG,\n'
                                    '                           '
                                    'GALACTIC_NORTH_POLE_DEC_J2000_DEG)\n'),
                                   ("galactic tide drawn in the galaxy's "
                                    'plane',
                                    'def '
                                    'create_sun_galactic_tide(center_position=(0, '
                                    '0, 0), radius=50000, n_points=2000):\n'
                                    '    """\n'
                                    '    Create Oort Cloud structure '
                                    'influenced by galactic tidal forces.\n'
                                    '    The galactic plane creates '
                                    'asymmetry in the distribution.\n'
                                    '    FIXED VERSION - Returns proper '
                                    'Plotly trace objects.\n'
                                    '\n'
                                    '    Parameters:\n'
                                    '    - center_position: Sun position '
                                    'tuple (default: (0, 0, 0)).\n'
                                    '      Accepted for interface uniformity '
                                    'with the unified dispatch\n'
                                    '      contract. Geometry translation '
                                    'deferred to switchover phase.\n'
                                    '    - radius: Typical distance in AU '
                                    '(default: 50000)\n'
                                    '    - n_points: Number of random points '
                                    '(default: 2000)\n'
                                    '    """\n'
                                    '    # Phase D1: center_position '
                                    'accepted for interface uniformity;\n'
                                    '    # geometry translation deferred to '
                                    'switchover phase.\n'
                                    '    r = np.random.normal(radius, '
                                    'radius*0.3, n_points)\n'
                                    '    r = np.clip(r, radius*0.5, '
                                    'radius*1.5)\n'
                                    '    \n'
                                    '    theta = np.random.uniform(0, '
                                    '2*np.pi, n_points)\n'
                                    '    \n'
                                    '    phi_weights = np.linspace(-np.pi/2, '
                                    'np.pi/2, 100)\n'
                                    '    weights = 1 + 0.5 * '
                                    'np.abs(np.sin(phi_weights))\n'
                                    '    phi = np.random.choice(phi_weights, '
                                    'n_points, p=weights/weights.sum())\n'
                                    '    \n'
                                    '    x = r * np.cos(phi) * '
                                    'np.cos(theta)\n'
                                    '    y = r * np.cos(phi) * '
                                    'np.sin(theta)\n'
                                    '    z = r * np.sin(phi)\n'
                                    '\n'
                                    '    tide_hover = (\n'
                                    "        'Galactic Tide Influenced "
                                    "Objects<br>'\n"
                                    "        'Asymmetric distribution due to "
                                    "Milky Way\\'s gravity<br>'\n"
                                    "        'Objects avoid galactic "
                                    "plane<br>'\n"
                                    "        '~50,000 AU typical distance'\n"
                                    '    )\n',
                                    'def '
                                    'create_sun_galactic_tide(center_position=(0, '
                                    '0, 0), n_points=2000):\n'
                                    '    """\n'
                                    "    Where the galaxy's tide sends "
                                    'comets in from: points in the outer '
                                    'Oort\n'
                                    "    cloud, tilted into the galaxy's "
                                    'plane, sparse at the plane and at the\n'
                                    '    galactic poles and thickest halfway '
                                    'between.\n'
                                    '\n'
                                    '    THE DRAWING IS A CHOICE RESTING ON '
                                    "WHAT CAN BE CITED (L-406, Tony's\n"
                                    '    rulings of 2026-10-02):\n'
                                    '    - The plane. Points are placed '
                                    'about the north galactic pole of '
                                    'J2000,\n'
                                    '      GALACTIC_NORTH_POLE_RA_J2000_DEG '
                                    '/ _DEC_J2000_DEG in constants_new.py,\n'
                                    "      and turned into the drawing's "
                                    "frame by the same matrix a planet's\n"
                                    '      pole uses '
                                    '(idealized_orbits.create_pole_transformation_matrix).\n'
                                    '    - The density. The number of points '
                                    'per piece of sky goes as\n'
                                    '      |sin b cos b|, b the galactic '
                                    'latitude: none at the plane or the\n'
                                    '      poles, most at 45 degrees. The '
                                    'sources are in the comments beside\n'
                                    '      the code that does it.\n'
                                    '    - The distance. Spread evenly from '
                                    'INNER_OORT_CLOUD_AU to\n'
                                    '      OUTER_OORT_CLOUD_AU, the outer '
                                    "cloud's two edges, the rows the\n"
                                    '      clumpy outer Oort cloud is drawn '
                                    'between. It replaces a typed\n'
                                    '      50,000 AU with a typed spread and '
                                    'cut-offs.\n'
                                    '    - Each point stands for the far end '
                                    'of an orbit. Where any real comet\n'
                                    '      is, is not known and is not '
                                    'claimed.\n'
                                    '\n'
                                    '    Parameters:\n'
                                    '    - center_position: Sun position '
                                    'tuple (default: (0, 0, 0)).\n'
                                    '      Accepted for interface uniformity '
                                    'with the unified dispatch\n'
                                    '      contract. Geometry translation '
                                    'deferred to switchover phase.\n'
                                    '    - n_points: Number of random points '
                                    '(default: 2000), a rendering\n'
                                    '      setting.\n'
                                    '    """\n'
                                    '    # Phase D1: center_position '
                                    'accepted for interface uniformity;\n'
                                    '    # geometry translation deferred to '
                                    'switchover phase.\n'
                                    '    from idealized_orbits import '
                                    'create_pole_transformation_matrix\n'
                                    '    M = '
                                    'np.asarray(create_pole_transformation_matrix(\n'
                                    '        '
                                    'GALACTIC_NORTH_POLE_RA_J2000_DEG, '
                                    'GALACTIC_NORTH_POLE_DEC_J2000_DEG),\n'
                                    '        dtype=float)\n'
                                    '\n'
                                    '    # Source: Matese and Whitmire, '
                                    '"Persistent Evidence of a Jovian Mass\n'
                                    '    #   Solar Companion in the Oort '
                                    'Cloud", arXiv:1004.4584, sec. 2.2 --\n'
                                    '    #   the dominant disk tidal term '
                                    'goes as |sin B cos B| (Matese et al.\n'
                                    '    #   1999), so if the tide '
                                    'dominates, the aphelia of new comets '
                                    'avoid\n'
                                    '    #   the galactic poles and equator '
                                    'and peak near B = +/-45 degrees.\n'
                                    '    # Source: Delsemme, "Galactic tides '
                                    'affect the Oort cloud: an\n'
                                    '    #   observational confirmation", '
                                    'A&A 187, 913 (1987), summary -- the\n'
                                    '    #   aphelia of 152 comets with '
                                    'periods over ten thousand years avoid\n'
                                    '    #   the two galactic polar caps and '
                                    'a strip along the galactic equator.\n'
                                    '    # Note: not everyone reads it this '
                                    'way. Higuchi, "Anisotropy of\n'
                                    '    #   Long-period Comets Explained by '
                                    'Their Formation Process",\n'
                                    '    #   arXiv:2008.04324 (AJ 160, 134), '
                                    'explains the same depletions by\n'
                                    '    #   comets gathering near the '
                                    'ecliptic and a second plane; and '
                                    'Rickman\n'
                                    '    #   et al. (2008), as Matese and '
                                    'Whitmire report, take the term to go\n'
                                    '    #   as |sin B|.\n'
                                    '    # Galactic latitude by rejection. '
                                    'Drawing sin(b) evenly gives every\n'
                                    '    # piece of sky the same chance; '
                                    'keeping a draw with probability\n'
                                    '    # |2 sin b cos b| = |sin 2b| (at '
                                    'most 1, at b = 45 degrees) makes the\n'
                                    '    # points per piece of sky go as '
                                    '|sin b cos b|.\n'
                                    '    sin_b = np.empty(0)\n'
                                    '    while sin_b.size < n_points:\n'
                                    '        u = np.random.uniform(-1.0, '
                                    '1.0, 2 * n_points)\n'
                                    '        keep = np.random.uniform(0.0, '
                                    '1.0, u.size) < 2.0 * np.abs(u) * '
                                    'np.sqrt(1.0 - u * u)\n'
                                    '        sin_b = np.concatenate([sin_b, '
                                    'u[keep]])\n'
                                    '    sin_b = sin_b[:n_points]\n'
                                    '    cos_b = np.sqrt(1.0 - sin_b * '
                                    'sin_b)\n'
                                    '    lon = np.random.uniform(0, 2 * '
                                    'np.pi, n_points)\n'
                                    '    r = '
                                    'np.random.uniform(INNER_OORT_CLOUD_AU, '
                                    'OUTER_OORT_CLOUD_AU, n_points)\n'
                                    '\n'
                                    '    galactic = np.vstack([r * cos_b * '
                                    'np.cos(lon),\n'
                                    '                          r * cos_b * '
                                    'np.sin(lon),\n'
                                    '                          r * sin_b])\n'
                                    '    x, y, z = M @ galactic\n'
                                    '\n'
                                    "    # Tony's approved words, 2026-10-02 "
                                    '(L-406). The distances are the\n'
                                    "    # rows', printed as the clumps' "
                                    'hover prints them.\n'
                                    '    tide_hover = (\n'
                                    "        'Galactic Tide: sends comets in "
                                    "from the outer Oort cloud<br>'\n"
                                    "        'Tilted to the galaxy\\'s "
                                    'plane, thickest halfway to its '
                                    "poles<br>'\n"
                                    "        f'From {INNER_OORT_CLOUD_AU:,} "
                                    "to {OUTER_OORT_CLOUD_AU:,} AU<br>'\n"
                                    "        'Where the comets really are is "
                                    "not known'\n"
                                    '    )\n'),
                                   ('tide info marker beyond the outer edge',
                                    '    r_info = radius * 1.5 * 1.05\n'
                                    '    # Phase 1 re-pipe (May 28, 2026): '
                                    'factory-routed.\n'
                                    '    info_trace = create_info_marker(\n'
                                    '        0, 0, r_info,\n'
                                    "        'rgb(255, 182, 193)',\n"
                                    '        f"Sun: Galactic Tide '
                                    'Region<br><br>{tide_hover}",',
                                    '    r_info = OUTER_OORT_CLOUD_AU * '
                                    '1.05\n'
                                    '    # Phase 1 re-pipe (May 28, 2026): '
                                    'factory-routed.\n'
                                    '    info_trace = create_info_marker(\n'
                                    '        0, 0, r_info,\n'
                                    "        'rgb(255, 182, 193)',\n"
                                    '        f"Sun: Galactic Tide '
                                    'Region<br><br>{tide_hover}",')]}


def fingerprint(raw):
    return hashlib.md5(raw.replace(b"\r\n", b"\n")).hexdigest()


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the ORRERY repo ROOT, next to "
                         "palomas_orrery.py -- not from documentation/. "
                         "NOTHING was written.")
    if not os.path.isfile("palomas_orrery.py"):
        raise SystemExit("ERROR: palomas_orrery.py is not here, so this is "
                         "not the orrery root. NOTHING was written.")
    results = []
    for path in sorted(EDITS):
        with open(path, "rb") as handle:
            raw = handle.read()
        got = fingerprint(raw)
        if got != BASE[path]:
            raise SystemExit(
                "ERROR: %s is not the file this patch was built against.\n"
                "       expected %s, found %s. It has changed since\n"
                "       5e42b00b, or this patch has already run.\n"
                "       (Line endings are excluded, so they are not the cause.)\n"
                "       NOTHING was written." % (path, BASE[path], got))
        nl = "\r\n" if b"\r\n" in raw else "\n"
        text = raw.decode("utf-8").replace("\r\n", "\n")
        done = []
        for label, old, new in EDITS[path]:
            if text.count(old) != 1:
                raise SystemExit("ANCHOR FAIL (%s): expected 1 match in %s, "
                                 "found %d. NOTHING was written."
                                 % (label, path, text.count(old)))
            text = text.replace(old, new)
            done.append(label)
        results.append((path, text.replace("\n", nl), done))
    for path, text, done in results:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in done:
            print("ok  %-46s %s" % (path, label))
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    print("  1. Run orrery_maintenance_run.py (VS Code, Run). It rebuilds")
    print("     the ledger index, the skill manifest and")
    print("     data/constants_export.json. Expect 21 of 21 checkers.")
    print("  2. Move this script into documentation/; commit and push.")
    print("  3. Reinstall interactive-exhibit (1.10) and replace the")
    print("     Project's instructions with PROJECT_INSTRUCTIONS.md v3.78.")
    print("  4. Then the gallery patch, patch_L406_2.")


if __name__ == "__main__":
    main()
