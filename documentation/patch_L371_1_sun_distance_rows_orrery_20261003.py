#!/usr/bin/env python3
"""
patch_L371_1_sun_distance_rows_orrery_20261003.py -- ORRERY repo. The first of
two patches for L-371's distance cards: the Sun's distance rows, and the
orrery hovers that print them.

Built on orrery 17ef66607cbe63ac5ed7bdbff15397fbe546ae42
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 52659e04 at https://github.com/tonylquintanilla/tonyquintanilla.github.io;
not touched by this patch -- patch_L371_2 is the gallery's half).

BEFORE YOU RUN IT: read L371_orrery_hover_changes_for_approval_20261003.md,
which lists every hover line this patch changes, old beside new. Run this
only once you have approved those words.

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code and click Run. The same as:
        python patch_L371_1_sun_distance_rows_orrery_20261003.py
    Then run orrery_maintenance_run.py the same way. It rebuilds
    data/constants_export.json, which the gallery reads.

WHAT THE MAINTENANCE RUN SHOULD SAY
    21 of 22 checkers pass. ONE fails, and it is expected:
        Constants change -- FAILED
    It fails because six rows changed from a typed number to a formula
    and one row was removed, and this checker cannot read those shapes.
    It names exactly these, and nothing else should appear:
        "value unreadable": HELMET_CUSP_RADII, GRAVITATIONAL_INFLUENCE_AU,
        HELIOPAUSE_RADII, INNER_LIMIT_OORT_CLOUD_AU, OUTER_OORT_CLOUD_AU,
        PARSEC_TO_AU (PARSEC_TO_AU moved up the file; its value is the same)
        "not understood": the removed GRAVITATIONAL_INFLUENCE_RANGE_AU
    Each was checked by hand in the session. Once you commit, the same
    checker reads "No changes to constants_new.py since HEAD".
    If any OTHER checker fails, or Constants change names anything else,
    stop and bring it back. The provenance scanner should still report
    296 Tier-1 findings and "No file's Tier-1 count rose."

    Then move this script into documentation/, commit and push. The
    gallery patch runs only after this push.

WHAT CHANGES
    constants_new.py
        The termination shock is 94.01 AU (Stone et al. 2005) and the
        heliopause 121 AU (Gurnett et al. 2013), each with its source,
        its figure count and the date it was read. HELIOPAUSE_RADII is
        now the same distance converted, not typed.
        The Oort cloud's two edges are each a range of two rows (NASA),
        drawn at 2,000 and 100,000 AU as Tony ruled. The inner cloud's
        edge, 20,000 AU, is re-cited to Portegies Zwart et al. (2021).
        Gravitational Influence is the Sun's Hill radius, 0.65 parsecs
        (Portegies Zwart et al. 2021); the unsourced 100,000-200,000 AU
        range row is removed. GRAVITATIONAL_INFLUENCE_AU is that radius
        in AU, computed.
        The helmet cusp's 2-4 solar radii is two rows; the cusp is drawn
        at the top. The Alfven surface, inner and outer corona and Roche
        limit gain their units and figure counts. The outer corona's
        citation, which could not be found saying 50 solar radii, is
        removed and the value declared a drawing choice.
        PARSEC_TO_AU moves up beside KM_PER_AU, gains its unit and read
        line, and KM_PER_PARSEC is added.
    constants_tokens.py     a "pc" unit, defined by KM_PER_PARSEC. Every
                            length in the export now also has a parsec
                            value; no existing value changes.
    constants_rows.py       row_text(): prints any row at its count, in
                            its own unit or another.
    solar_visualization_shells.py, comet_visualization_shells.py,
    palomas_orrery.py       every hover line that states one of these
                            distances prints it from its row. The words
                            are in the approval file.
    planet_visualization_utilities.py   no longer imports the range row.
    test_constants_provenance.py        three relation tests, no pinned
                                        values (24 tests, was 21).
    test_worksheet_checker.py   HELIOPAUSE_RADII leaves a pin: its old
                                cross-checks retired with the 121.6 AU
                                they had certified.
    exact_rows_report.py    the check also sees prints through row_text().
                            Without this it could not see those lines.

PERMANENT, though this script is thrown away: the rows, the pc unit,
row_text(), the hover wording, the tests and the widened check.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 3, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

BASE = {'comet_visualization_shells.py': '92cf79d6cede84ad851196add18ff620',
 'constants_new.py': '031ae425d9e28f0dea6272d4266869b6',
 'constants_rows.py': '46dde0aface09eff1c03753cb82fbe27',
 'constants_tokens.py': '4c03c91854749b6437db1219f83d585c',
 'exact_rows_report.py': '1484d09e023ac36444794101bf56908e',
 'palomas_orrery.py': 'f505496fe28a473ccc93ff5f7c5d7f37',
 'planet_visualization_utilities.py': 'ec6d2a5304b9a90ce20ba0ae1ba9bbdb',
 'solar_visualization_shells.py': '6b7c238a74fe21d36e09e3c8e7b1ef2f',
 'test_constants_provenance.py': '6818edd242c5d50661e84ec78248b840',
 'test_worksheet_checker.py': 'fde62035e95d0482ec78ebf281a17e39'}

EDITS = {'comet_visualization_shells.py': [('docstring: credit line',
                                    "Module updated: May 2026 with Anthropic's Claude Opus 4.7\n",
                                    "Module updated: October 3, 2026 with Anthropic's Claude Opus "
                                    '5.5 (L-371:\n'
                                    'the MAPS hovers print the helmet cusp, the Roche limit and '
                                    'the inner\n'
                                    'corona from their rows at their counts, through '
                                    'constants_rows.row_text(),\n'
                                    'where they printed widths of their own or typed copies of the '
                                    'rows.)\n'
                                    "Module updated: May 2026 with Anthropic's Claude Opus 4.7\n",
                                    1),
                                   ('import row_text',
                                    '    ALFVEN_SURFACE_RADII, HELMET_CUSP_RADII)\n',
                                    '    ALFVEN_SURFACE_RADII, HELMET_CUSP_RADII)\n'
                                    "# L-371: the Sun's distance rows printed at their counts.\n"
                                    'from constants_rows import row_text\n',
                                    1),
                                   ('disintegration hover: the helmet cusp in the layer line',
                                    '        f"(~{HELMET_CUSP_RADII} R_sun, ~{HELMET_CUSP_RADII * '
                                    'SOLAR_RADIUS_AU:.3f} AU)<br>"\n',
                                    '        f"(~{row_text(\'HELMET_CUSP_RADII\')} R_sun, '
                                    '~{row_text(\'HELMET_CUSP_RADII\', \'au\')} AU)<br>"\n',
                                    1),
                                   ('disintegration hover: inside the helmet cusp',
                                    '        f"Inside the helmet cusp (~{HELMET_CUSP_RADII} R_sun, '
                                    '"\n'
                                    '        f"~{HELMET_CUSP_RADII * SOLAR_RADIUS_AU:.3f} AU): '
                                    '{helmet_status}<br>"\n',
                                    '        f"Inside the helmet cusp '
                                    '(~{row_text(\'HELMET_CUSP_RADII\')} R_sun, "\n'
                                    '        f"~{row_text(\'HELMET_CUSP_RADII\', \'au\')} AU): '
                                    '{helmet_status}<br>"\n',
                                    1),
                                   ('disintegration hover: the Roche limit and inner corona from '
                                    'their rows',
                                    '        f"Inside Roche limit (~3.45 R_sun, ~0.016 AU): '
                                    '{roche_status}<br>"\n'
                                    '        f"Inside Inner K-corona (~3.0 R_sun, ~0.014 AU): '
                                    'NO<br>"\n',
                                    '        f"Inside Roche limit '
                                    "(~{row_text('ROCHE_LIMIT_RADII')} R_sun, "
                                    "~{row_text('ROCHE_LIMIT_RADII', 'au')} AU): "
                                    '{roche_status}<br>"\n'
                                    '        f"Inside Inner K-corona '
                                    "(~{row_text('INNER_CORONA_RADII')} R_sun, "
                                    '~{row_text(\'INNER_CORONA_RADII\', \'au\')} AU): NO<br>"\n',
                                    1),
                                   ('disintegration hover: the Roche note',
                                    '        f"Note: Tidal disruption requires being inside the '
                                    'Roche limit (~3.45 R_sun, ~0.016 AU). MAPS never reached it '
                                    'intact.<br>"\n',
                                    '        f"Note: Tidal disruption requires being inside the '
                                    "Roche limit (~{row_text('ROCHE_LIMIT_RADII')} R_sun, "
                                    "~{row_text('ROCHE_LIMIT_RADII', 'au')} AU). MAPS never "
                                    'reached it intact.<br>"\n',
                                    1),
                                   ('ghost tail hover: the cusp, Roche limit and inner corona from '
                                    'their rows',
                                    '        f"({HELMET_CUSP_RADII} R_sun, {HELMET_CUSP_RADII * '
                                    'SOLAR_RADIUS_AU:.3f} AU),<br>"\n'
                                    '        "Roche limit (3.45 R_sun, 0.016 AU), inner K-corona '
                                    '(3.0 R_sun, 0.014 AU),<br>"\n',
                                    '        f"({row_text(\'HELMET_CUSP_RADII\')} R_sun, '
                                    '{row_text(\'HELMET_CUSP_RADII\', \'au\')} AU),<br>"\n'
                                    '        f"Roche limit (about '
                                    "{row_text('ROCHE_LIMIT_RADII')} R_sun, "
                                    "{row_text('ROCHE_LIMIT_RADII', 'au')} AU), inner K-corona "
                                    "({row_text('INNER_CORONA_RADII')} R_sun, "
                                    '{row_text(\'INNER_CORONA_RADII\', \'au\')} AU),<br>"\n',
                                    1)],
 'constants_new.py': [('the Sun: termination shock, heliopause, Oort edges, gravitational reach',
                       'TERMINATION_SHOCK_AU = 94\n'
                       '# Source: Stone et al. (2005), Science 309:2017\n'
                       '# See: Voyager 1 crossed at 94 AU (Dec 2004)\n'
                       '# Also: Voyager 2 crossed at 84 AU (Aug 2007) -- asymmetric\n'
                       '# Cross-checked: Claude 2026-08-02 -- Stone et al. '
                       '(worksheet_claude_constants_new.md)\n'
                       '# Cross-checked: GPT 2026-08-02 -- Stone et al. '
                       '(constants_new_citation_verification_gpt.md)\n'
                       '\n'
                       'HELIOPAUSE_RADII = 26148\n'
                       '# Note: This is in solar radii, not AU. 121.6 AU * 149597870.7 / 695700 = '
                       '26148 R_sun\n'
                       '# Source: Gurnett et al. (2013), Science 341:1489\n'
                       '# See: Voyager 1 crossed heliopause at ~121.6 AU (Aug 2012)\n'
                       '# Corrected: 2026-08-02 -- 26449 -> 26148 (prior comment used 123 AU;\n'
                       '#   Gurnett source says 121.6 AU; both checkers independently found the '
                       'error)\n'
                       '# Cross-checked: Claude 2026-08-02 -- Gurnett et al. '
                       '(worksheet_claude_constants_new.md)\n'
                       '# Cross-checked: GPT 2026-08-02 -- Gurnett et al. '
                       '(constants_new_citation_verification_gpt.md)\n'
                       '\n'
                       '# Oort Cloud and gravitational influence (in AU)\n'
                       'INNER_LIMIT_OORT_CLOUD_AU = 2000\n'
                       '# Source: Hills (1981); Oort (1950) -- inner edge estimate\n'
                       '# Note: Highly uncertain; ranges 2000-5000 AU in literature\n'
                       '\n'
                       'INNER_OORT_CLOUD_AU = 20000\n'
                       '# Source: Hills (1981) -- outer edge of inner (Hills) cloud\n'
                       '# Note: Boundary between inner and outer Oort cloud is uncertain\n'
                       '\n'
                       'OUTER_OORT_CLOUD_AU = 100000\n'
                       '# Source: Oort (1950); Weissman (1996)\n'
                       '# Note: Estimated outer boundary, ~0.5 parsec\n'
                       '\n'
                       'GRAVITATIONAL_INFLUENCE_AU = 150000\n'
                       '# Source: Approximate Hill sphere of Sun in Milky Way (model-dependent)\n'
                       '# Source+: Estimates range 100,000-200,000 AU in the literature;\n'
                       "# Source+: depends on assumed enclosed galactic mass and Sun's orbital "
                       'distance.\n'
                       '# Source+: ~2.4 light-years. Visualization boundary, not a measured '
                       'value.\n'
                       '# Corrected: 2026-08-02 -- 126000 -> 150000 (prior value unsourced;\n'
                       '#   150000 AU is a round midpoint of the published range)\n'
                       '# Confirmed 2026-08-07 (Tony, L-179): 150000 stands, chosen as the\n'
                       '#   midpoint of the published range below. Display text must carry\n'
                       '#   the RANGE, not present the midpoint as a measurement.\n'
                       '\n'
                       'GRAVITATIONAL_INFLUENCE_RANGE_AU = (100000, 200000)\n'
                       '# Source: spread of published Sun-in-Galaxy Hill sphere estimates;\n'
                       '# Source+: model-dependent, varying with assumed enclosed galactic mass\n'
                       "# Source+: and the Sun's galactocentric distance.\n"
                       '# Note: 100,000-200,000 AU = 1.6-3.2 light-years. Stored as DATA rather\n'
                       '#       than prose so display strings can interpolate the envelope\n'
                       '#       instead of restating the midpoint alone (L-179, 2026-08-07).\n'
                       '\n',
                       'TERMINATION_SHOCK_AU = 94.01\n'
                       '# Unit: au\n'
                       '# Status: measured V_SOURCED 2026-10-03 -- abstract, open\n'
                       '# Figures: 4 -- the source prints 94.01.\n'
                       '# Read: abstract, Stone et al. (2005), at NASA ADS, 2026-10-03, Claude\n'
                       '# Read+: Opus 5.5\n'
                       '# Source: Stone, E. C., Cummings, A. C., McDonald, F. B., Heikkila, B. '
                       'C.,\n'
                       '# Source+: Lal, N. and Webber, W. R. (2005), "Voyager 1 explores the\n'
                       '# Source+: termination shock region and the heliosheath beyond", Science\n'
                       '# Source+: 309, 2017-2020, doi:10.1126/science.1117684 -- abstract: '
                       'Voyager\n'
                       '# Source+: 1 crossed the termination shock on 16 December 2004 at 94.01 '
                       'AU.\n'
                       '# Access: abstract, open,\n'
                       '# Access+: https://ui.adsabs.harvard.edu/abs/2005Sci...309.2017S/abstract\n'
                       '# Access+: (2026-10-03).\n'
                       "# Note: one spacecraft's crossing of a surface that is not round; it is\n"
                       '# Note+: drawn as a sphere at that distance. Voyager 2 crossed nearer the\n'
                       '# Note+: Sun, which is why the shape is called asymmetric.\n'
                       '# Corrected: 2026-10-03 (L-371) -- was 94, two figures where the source\n'
                       '# Corrected+: prints four.\n'
                       '# Cross-check retired: 2026-10-03 -- the Claude and GPT legs of '
                       '2026-08-02\n'
                       '# Cross-check retired+: checked the value 94; a check of the old value is\n'
                       '# Cross-check retired+: not a check of the new one.\n'
                       '\n'
                       'HELIOPAUSE_AU = 121\n'
                       '# Unit: au\n'
                       '# Status: measured V_SOURCED 2026-10-03 -- open full text\n'
                       '# Figures: 3 -- the source prints 121.\n'
                       "# Read: p. 1489, second column, Gurnett et al. (2013), the authors' copy "
                       'at\n'
                       '# Read+: space.physics.uiowa.edu, 2026-10-03, Claude Opus 5.5\n'
                       '# Source: Gurnett, D. A., Kurth, W. S., Burlaga, L. F. and Ness, N. F.\n'
                       '# Source+: (2013), "In situ observations of interstellar plasma with\n'
                       '# Source+: Voyager 1", Science 341, 1489-1492, '
                       'doi:10.1126/science.1241681\n'
                       '# Source+: -- p. 1489: the first sign of the heliopause came on 28 July '
                       '2012,\n'
                       '# Source+: at 121 AU; the last of five crossings was on 25 August 2012.\n'
                       '# Access: open full text,\n'
                       '# Access+: '
                       'https://space.physics.uiowa.edu/~dag/publications/2013_InSituObservationsOfInterstellarPlasmaWaveVoyager_Science.pdf\n'
                       '# Access+: (2026-10-03).\n'
                       "# Note: one spacecraft's crossing of a surface that is not round; it is\n"
                       '# Note+: drawn as a sphere at that distance. The paper gives no distance\n'
                       "# Note+: for 25 August. The 121.6 AU this file's comment attributed to it\n"
                       '# Note+: until 2026-10-03 is not in it.\n'
                       '# Note+: Stored in AU, the unit its source gives (L-386); '
                       'HELIOPAUSE_RADII\n'
                       '# Note+: below is the same distance in solar radii, computed.\n'
                       '# Cross-check retired: 2026-10-03 -- the Claude and GPT legs of '
                       '2026-08-02,\n'
                       '# Cross-check retired+: on HELIOPAUSE_RADII, certified 26148 from 121.6 '
                       'AU; a\n'
                       '# Cross-check retired+: check of the old value is not a check of the new '
                       'one.\n'
                       '\n'
                       'HELIOPAUSE_RADII = HELIOPAUSE_AU * KM_PER_AU / SUN_RADIUS_KM\n'
                       '# Unit: r_sun\n'
                       '# Conversion: of HELIOPAUSE_AU -- computed from that row, which carries '
                       'the\n'
                       '# Conversion+: source and the count; the export serves this value as that\n'
                       '# Conversion+: row\'s "in" (provenance-discipline 2.22, Rule 3; L-386).\n'
                       '# Note: kept under its old name for the code that reads it. Until\n'
                       '# Note+: 2026-10-03 it was its own row, typed 26148 from 121.6 AU.\n'
                       '\n'
                       '# Oort cloud and gravitational influence (in AU)\n'
                       '# --- the two edges of the Oort cloud, each a range (L-371, 2026-10-03) '
                       '---\n'
                       '# NASA gives both edges as ranges. Each range is two rows; the drawn edge\n'
                       '# is an expression over them with its reason on the row, and a display\n'
                       '# prints the range from the rows (provenance-discipline, When the Source\n'
                       "# Gives a Range). Tony's ruling of 2026-10-03: draw one end of each range\n"
                       '# and say so.\n'
                       '\n'
                       'OORT_CLOUD_INNER_EDGE_LOW_AU = 2000\n'
                       '# Unit: au\n'
                       '# Status: measured V_SOURCED 2026-10-03 -- open page\n'
                       '# Figures: 1 -- the source prints "2,000" as the low end of a range it\n'
                       '# Figures+: states to thousands; the trailing zeros are placeholders\n'
                       '# Figures+: (Rule 2).\n'
                       '# Read: "Oort Cloud Facts", NASA Science, the paragraph on the inner and\n'
                       '# Read+: outer edges, 2026-10-03, Claude Opus 5.5\n'
                       '# Source: NASA Science, "Oort Cloud Facts" -- the inner edge of the Oort\n'
                       '# Source+: cloud is thought to lie between 2,000 and 5,000 AU from the '
                       'Sun.\n'
                       '# Access: open, https://science.nasa.gov/solar-system/oort-cloud/facts\n'
                       '# Access+: (2026-10-03).\n'
                       '\n'
                       'OORT_CLOUD_INNER_EDGE_HIGH_AU = 5000\n'
                       '# Unit: au\n'
                       '# Status: measured V_SOURCED 2026-10-03 -- open page\n'
                       '# Figures: 1 -- the source prints "5,000", the high end of the same '
                       'range.\n'
                       '# Read: as OORT_CLOUD_INNER_EDGE_LOW_AU, 2026-10-03, Claude Opus 5.5.\n'
                       '# Source: as OORT_CLOUD_INNER_EDGE_LOW_AU.\n'
                       '# Access: as OORT_CLOUD_INNER_EDGE_LOW_AU.\n'
                       '\n'
                       'INNER_LIMIT_OORT_CLOUD_AU = OORT_CLOUD_INNER_EDGE_LOW_AU\n'
                       "# Derived: the low end of the inner edge's range = 2000\n"
                       '# Unit: au\n'
                       '# Status: declared 2026-10-03 -- the low end of the range held in the two\n'
                       '# Status+: rows above, L-371\n'
                       '# Figures: exact -- prints 1, the digits of the value its rule gives\n'
                       '# Figures+: (2000); declared construction: equal to\n'
                       '# Figures+: OORT_CLOUD_INNER_EDGE_LOW_AU\n'
                       '# Declared: the inner edge is drawn at the near end of its range, and the\n'
                       '# Declared+: outer edge at the far end, so the cloud is drawn at the '
                       'widest\n'
                       '# Declared+: reach its sources allow. The pick is ours (Tony, 2026-10-03,\n'
                       '# Declared+: ruling A); the hover says the range and the end drawn.\n'
                       '# Corrected: 2026-10-03 (L-371) -- was typed 2000, citing Hills (1981) '
                       'and\n'
                       "# Corrected+: Oort (1950), which do not print it (Hills' abstract read\n"
                       '# Corrected+: 2026-10-02).\n'
                       '\n'
                       'INNER_OORT_CLOUD_AU = 20000\n'
                       '# Unit: au\n'
                       '# Status: measured V_SOURCED 2026-10-03 -- open full text\n'
                       '# Figures: 1 -- the source prints "20 000" as a bound, to tens of '
                       'thousands.\n'
                       '# Read: sec. 2.2, Portegies Zwart et al. (2021), arXiv:2105.12816v2,\n'
                       '# Read+: 2026-10-03, Claude Opus 5.5\n'
                       '# Source: Portegies Zwart, S., Torres, S., Cai, M. X. and Brown, A. G. A.\n'
                       '# Source+: (2021), "Oort cloud Ecology II: the chronology of the '
                       'formation\n'
                       '# Source+: of the Oort cloud", A&A 652, A144, '
                       'doi:10.1051/0004-6361/202040096\n'
                       '# Source+: -- sec. 2.2: the Hills cloud lies between the outer edge of '
                       'the\n'
                       '# Source+: parking zone and the inner edge of the Oort cloud, at about\n'
                       '# Source+: 20,000 au or less.\n'
                       '# Access: open full text, https://arxiv.org/html/2105.12816v2 '
                       '(2026-10-03).\n'
                       '# Note: the boundary between the inner (Hills) cloud and the outer cloud,\n'
                       '# Note+: and an uncertain one: the paper says what defines the transition\n'
                       '# Note+: remains unclear (sec. 2.3).\n'
                       '# Corrected: 2026-10-03 (L-371) -- cited Hills (1981), which does not\n'
                       '# Corrected+: print it.\n'
                       '\n'
                       'OORT_CLOUD_OUTER_EDGE_LOW_AU = 10000\n'
                       '# Unit: au\n'
                       '# Status: measured V_SOURCED 2026-10-03 -- open page\n'
                       '# Figures: 1 -- the source prints "10,000", the low end of a range it\n'
                       '# Figures+: states to tens of thousands.\n'
                       '# Read: as OORT_CLOUD_INNER_EDGE_LOW_AU, 2026-10-03, Claude Opus 5.5.\n'
                       '# Source: NASA Science, "Oort Cloud Facts" -- the outer edge of the Oort\n'
                       '# Source+: cloud is thought to lie between 10,000 and 100,000 AU from the '
                       'Sun.\n'
                       '# Access: as OORT_CLOUD_INNER_EDGE_LOW_AU.\n'
                       '\n'
                       'OORT_CLOUD_OUTER_EDGE_HIGH_AU = 100000\n'
                       '# Unit: au\n'
                       '# Status: measured V_SOURCED 2026-10-03 -- open page\n'
                       '# Figures: 1 -- the source prints "100,000", the high end of the same '
                       'range.\n'
                       '# Read: as OORT_CLOUD_INNER_EDGE_LOW_AU, 2026-10-03, Claude Opus 5.5.\n'
                       '# Source: as OORT_CLOUD_OUTER_EDGE_LOW_AU.\n'
                       '# Access: as OORT_CLOUD_INNER_EDGE_LOW_AU.\n'
                       '\n'
                       'OUTER_OORT_CLOUD_AU = OORT_CLOUD_OUTER_EDGE_HIGH_AU\n'
                       "# Derived: the high end of the outer edge's range = 100000\n"
                       '# Unit: au\n'
                       '# Status: declared 2026-10-03 -- the high end of the range held in the '
                       'two\n'
                       '# Status+: rows above, L-371\n'
                       '# Figures: exact -- prints 1, the digits of the value its rule gives\n'
                       '# Figures+: (100000); declared construction: equal to\n'
                       '# Figures+: OORT_CLOUD_OUTER_EDGE_HIGH_AU\n'
                       '# Declared: the far end of the range, for the reason on\n'
                       '# Declared+: INNER_LIMIT_OORT_CLOUD_AU: the cloud is drawn at the widest\n'
                       '# Declared+: reach its sources allow (Tony, 2026-10-03, ruling A).\n'
                       '# Corrected: 2026-10-03 (L-371) -- was typed 100000, citing Oort (1950)\n'
                       '# Corrected+: and Weissman (1996); Oort (1950) does not print it.\n'
                       '\n'
                       "# --- the Sun's gravitational reach (L-371, 2026-10-03) ---\n"
                       '\n'
                       'GRAVITATIONAL_INFLUENCE_PC = 0.65\n'
                       '# Unit: pc\n'
                       '# Status: measured V_SOURCED 2026-10-03 -- open full text\n'
                       '# Figures: 2 -- the source prints 0.65.\n'
                       '# Read: sec. 2.3, the captions of Figs. 2 and 3, and sec. 5, Portegies\n'
                       '# Read+: Zwart et al. (2021), arXiv:2105.12816v2, 2026-10-03, Claude Opus '
                       '5.5\n'
                       '# Source: Portegies Zwart et al. (2021), A&A 652, A144,\n'
                       '# Source+: doi:10.1051/0004-6361/202040096 -- the Hill radius of the Sun '
                       'in\n'
                       '# Source+: the Galactic potential is about 0.65 pc (Fig. 2 and Fig. 3\n'
                       '# Source+: captions; sec. 5); the outer limit of the Oort cloud is taken '
                       'to\n'
                       '# Source+: coincide with it (sec. 2.3).\n'
                       '# Access: open full text, https://arxiv.org/html/2105.12816v2 '
                       '(2026-10-03).\n'
                       "# Note: CALCULATED, not measured: where the galaxy's tidal pull overtakes\n"
                       "# Note+: the Sun's gravity, worked out from a model of the galaxy (the\n"
                       "# Note+: paper's Table 4). It is a published value, which is what\n"
                       '# Note+: "measured" means in the status line. The Hill surface is not a\n'
                       '# Note+: sphere; it is drawn as one at this radius.\n'
                       '# Note+: TRAP: Fig. 3 also gives an inner edge of the Oort cloud near\n'
                       "# Note+: 0.21 pc. That is a different definition -- where the galaxy's "
                       'tide\n'
                       "# Note+: starts to matter in their model -- and is not NASA's inner edge.\n"
                       '# Note+: Do not mix the two.\n'
                       '\n'
                       'GRAVITATIONAL_INFLUENCE_AU = GRAVITATIONAL_INFLUENCE_PC * KM_PER_PARSEC / '
                       'KM_PER_AU\n'
                       '# Unit: au\n'
                       '# Conversion: of GRAVITATIONAL_INFLUENCE_PC -- computed from that row, '
                       'which\n'
                       '# Conversion+: carries the source and the count; the export serves this\n'
                       '# Conversion+: value as that row\'s "in" (provenance-discipline 2.22, Rule '
                       '3).\n'
                       '# Note: kept under its old name for the code that reads it. Until\n'
                       '# Note+: 2026-10-03 it was typed 150000, the midpoint of an unsourced\n'
                       '# Note+: 100,000-200,000 AU range; the range row went with it (L-371,\n'
                       "# Note+: Tony's correction of 2026-10-03: a Hill radius is calculated, "
                       'not\n'
                       '# Note+: chosen).\n'
                       '\n',
                       1),
                      ('PARSEC_TO_AU moved out of the galactic-centre block',
                       'PARSEC_TO_AU = 206264.806247096\n'
                       '# Note: DEFINED, not measured. One parsec is the distance at which one\n'
                       '# Note+: astronomical unit subtends one arcsecond, so the value is\n'
                       '# Note+: exactly 648000/pi au and no source publishes it as a\n'
                       '# Note+: measurement.\n'
                       '# Derived: 648000 / pi = 206264.80624709636...\n'
                       '# Derived+: Previous hardcoded value was 206265.0 (consistent to 6 sig\n'
                       '# Derived+: figs; relative error 9.39e-07). The trailing .0 asserted a\n'
                       '# Derived+: tenth-of-an-au precision the number did not have -- the\n'
                       '# Derived+: true fourth decimal is 8, not 0.\n'
                       '# Source: IAU 2015 Resolution B2; the exact relation is restated in\n'
                       '# Source+: Prsa et al. (2016), AJ 152, 41,\n'
                       '# Source+: doi:10.3847/0004-6256/152/2/41.\n'
                       '# Cross-checked: Claude 2026-08-25 -- IAU 2015 B2 '
                       '(worksheet_claude-opus-5_L247_sgr_a_constants_20260825.md)\n'
                       '# Cross-checked: GPT 2026-08-25 -- IAU 2015 B2 '
                       '(worksheet_gpt-5.6-sol_L247_sgr_a_constants_20260825.md)\n'
                       '# Cross-checked: Gemini 2026-08-25 -- IAU 2015 B2 '
                       '(worksheet_gemini-2.5-pro_L247_sgr_a_constants_20260825.md)\n'
                       '# Resolved: worksheet_gpt-5.6-sol_L247_sgr_a_constants_20260825.md '
                       'constants_new.py::PARSEC_TO_AU -- rounded 206265.0 replaced by the exact '
                       'IAU definition 648000/pi (L-247)\n'
                       '# Note: written as a literal rather than as 648000.0/math.pi, following\n'
                       '# Note+: SPEED_OF_LIGHT_KM_S, which is equally exact by definition and\n'
                       '# Note+: equally written out. A math.pi expression would also be\n'
                       "# Note+: unreadable to constants_change_report.py's DERIVED case, which\n"
                       '# Note+: accepts only names tracked in this file.\n'
                       '# Note: this value carries the whole star pipeline once L-248 lands.\n'
                       '# Note+: PARSEC_TO_AU / AU_PER_LIGHT_YEAR is 3.2615637772 with the\n'
                       '# Note+: exact parsec and was 3.2615668 with the rounded one; the\n'
                       '# Note+: literal 3.26156 that L-248 sweeps is closer to the first.\n'
                       '\n',
                       '',
                       1),
                      ('PARSEC_TO_AU and KM_PER_PARSEC beside KM_PER_AU',
                       '# Note: 1 AU = 149,597,870,700 m exactly. We use km (divide by 1000).\n\n',
                       '# Note: 1 AU = 149,597,870,700 m exactly. We use km (divide by 1000).\n'
                       '\n'
                       'PARSEC_TO_AU = 206264.806247096\n'
                       '# Unit: au\n'
                       "# Status: measured V_CROSS_CHECKED 2026-10-03 -- belongs to no body's "
                       'slice;\n'
                       "# Status+: visited with the Sun's because the Sun's gravitational reach "
                       'is\n'
                       '# Status+: stated in parsecs (L-371).\n'
                       '# Figures: exact -- the notes to IAU 2015 Resolution B2 define one parsec\n'
                       '# Figures+: as exactly 648000/pi au; the literal carries 15 figures of '
                       'that\n'
                       '# Figures+: irrational number.\n'
                       "# Read: sec. 5 and the appendix's item 2, Prsa et al. (2016), AJ 152, 41,\n"
                       '# Read+: arXiv:1605.09788, 2026-10-03, Claude Opus 5.5\n'
                       '# Note: DEFINED, not measured. One parsec is the distance at which one\n'
                       '# Note+: astronomical unit subtends one arcsecond, so the value is\n'
                       '# Note+: exactly 648000/pi au and no source publishes it as a\n'
                       '# Note+: measurement.\n'
                       '# Derived: 648000 / pi = 206264.80624709636...\n'
                       '# Derived+: Previous hardcoded value was 206265.0 (consistent to 6 sig\n'
                       '# Derived+: figs; relative error 9.39e-07). The trailing .0 asserted a\n'
                       '# Derived+: tenth-of-an-au precision the number did not have -- the\n'
                       '# Derived+: true fourth decimal is 8, not 0.\n'
                       '# Source: IAU 2015 Resolution B2; the exact relation is restated in\n'
                       '# Source+: Prsa et al. (2016), AJ 152, 41,\n'
                       '# Source+: doi:10.3847/0004-6256/152/2/41.\n'
                       '# Cross-checked: Claude 2026-08-25 -- IAU 2015 B2 '
                       '(worksheet_claude-opus-5_L247_sgr_a_constants_20260825.md)\n'
                       '# Cross-checked: GPT 2026-08-25 -- IAU 2015 B2 '
                       '(worksheet_gpt-5.6-sol_L247_sgr_a_constants_20260825.md)\n'
                       '# Cross-checked: Gemini 2026-08-25 -- IAU 2015 B2 '
                       '(worksheet_gemini-2.5-pro_L247_sgr_a_constants_20260825.md)\n'
                       '# Resolved: worksheet_gpt-5.6-sol_L247_sgr_a_constants_20260825.md '
                       'constants_new.py::PARSEC_TO_AU -- rounded 206265.0 replaced by the exact '
                       'IAU definition 648000/pi (L-247)\n'
                       '# Note: written as a literal rather than as 648000.0/math.pi, following\n'
                       '# Note+: SPEED_OF_LIGHT_KM_S, which is equally exact by definition and\n'
                       '# Note+: equally written out. A math.pi expression would also be\n'
                       "# Note+: unreadable to constants_change_report.py's DERIVED case, which\n"
                       '# Note+: accepts only names tracked in this file.\n'
                       '# Note: this value carries the whole star pipeline once L-248 lands.\n'
                       '# Note+: PARSEC_TO_AU / AU_PER_LIGHT_YEAR is 3.2615637772 with the\n'
                       '# Note+: exact parsec and was 3.2615668 with the rounded one; the\n'
                       '# Note+: literal 3.26156 that L-248 sweeps is closer to the first.\n'
                       '# Note: moved here from the galactic-centre block on 2026-10-03 (L-371),\n'
                       "# Note+: so that KM_PER_PARSEC below and the Sun's rows can use it.\n"
                       '\n'
                       'KM_PER_PARSEC = PARSEC_TO_AU * KM_PER_AU\n'
                       '# Unit: km\n'
                       '# Conversion: of PARSEC_TO_AU -- computed from that row, which carries '
                       'the\n'
                       '# Conversion+: source and the count. This is the row that defines the '
                       '"pc"\n'
                       '# Conversion+: token in constants_tokens.py (L-371, 2026-10-03).\n'
                       '\n',
                       1),
                      ('INNER_CORONA_RADII: unit and print count',
                       'INNER_CORONA_RADII = 3\n',
                       'INNER_CORONA_RADII = 3\n'
                       '# Unit: r_sun\n'
                       '# Figures: exact -- prints 1. A declared convention is exact for\n'
                       '# Figures+: counting (Rule 2); it prints the digit it was chosen with.\n',
                       1),
                      ('OUTER_CORONA_RADII: declared, the citation removed',
                       'OUTER_CORONA_RADII = 50\n'
                       '# Source: Mann et al. (2004), A&A 414:1127\n'
                       '# See: Various; F-corona envelope extends to ~50 R_sun\n'
                       '# Note: Visualization boundary for F-corona envelope; not a sharp physical '
                       'edge\n',
                       'OUTER_CORONA_RADII = 50\n'
                       '# Unit: r_sun\n'
                       '# Status: declared 2026-10-03 -- a boundary chosen for the drawing, L-371\n'
                       '# Figures: exact -- prints 2, the digits it was chosen with (50).\n'
                       '# Declared: the faint outer corona, sunlight scattered by dust, has no\n'
                       '# Declared+: sharp edge. The shell marks a reach chosen so the drawing\n'
                       '# Declared+: shows that faint envelope; nothing is measured at 50.\n'
                       '# Review-note: the citation this row carried until 2026-10-03 could not\n'
                       '# Review-note+: be found saying this. It is recorded on L-371 and\n'
                       '# Review-note+: deliberately not restated here.\n',
                       1),
                      ('HELMET_CUSP_RADII: the 2-4 range as two rows, the cusp drawn at the top',
                       '# New shells (added April 2026); renamed and resourced 2026-08-22 (L-224)\n'
                       'HELMET_CUSP_RADII = 4.0\n',
                       '# New shells (added April 2026); renamed and resourced 2026-08-22 (L-224)\n'
                       "# The helmets' 2-4 solar radii is a range, so it is two rows and the\n"
                       '# drawn cusp is an expression over them (L-371, 2026-10-03).\n'
                       'HELMET_CUSP_LOW_RADII = 2\n'
                       '# Unit: r_sun\n'
                       '# Status: measured V_SOURCED 2026-10-03 -- abstract, open\n'
                       '# Figures: 1 -- the source prints "2-4".\n'
                       '# Read: abstract, Suess and Nerney (2004), at NASA ADS, 2026-08-21, Tony\n'
                       '# Read+: Quintanilla; record:\n'
                       '# Read+: documentation/SOURCE_suess_nerney_2004_helmet_extent_20260821.md\n'
                       '# Source: Suess & Nerney (2004), Adv. Space Res. 33:668-675, bibcode\n'
                       '# Source+: 2004AdSpR..33..668S -- the closed field regions, or helmets,\n'
                       '# Source+: reach no higher than 2-4 solar radii. This row is the low end.\n'
                       '# Access: abstract, open,\n'
                       '# Access+: https://ui.adsabs.harvard.edu/abs/2004AdSpR..33..668S/abstract\n'
                       '# Access+: (2026-08-21).\n'
                       '\n'
                       'HELMET_CUSP_HIGH_RADII = 4\n'
                       '# Unit: r_sun\n'
                       '# Status: measured V_SOURCED 2026-10-03 -- abstract, open\n'
                       '# Figures: 1 -- the source prints "2-4".\n'
                       '# Read: as HELMET_CUSP_LOW_RADII, 2026-08-21, Tony Quintanilla.\n'
                       '# Source: as HELMET_CUSP_LOW_RADII. This row is the high end.\n'
                       '# Access: as HELMET_CUSP_LOW_RADII.\n'
                       '\n'
                       'HELMET_CUSP_RADII = HELMET_CUSP_HIGH_RADII\n'
                       "# Derived: the top of the helmets' range = 4\n"
                       '# Unit: r_sun\n'
                       '# Status: declared 2026-10-03 -- the top of the range held in the two\n'
                       '# Status+: rows above, L-371\n'
                       '# Figures: exact -- prints 1, the digits of the value its rule gives\n'
                       '# Figures+: (4); declared construction: equal to HELMET_CUSP_HIGH_RADII\n'
                       '# Declared: the top of the range, so the drawn cusp does not understate\n'
                       '# Declared+: the helmet. Until 2026-10-03 it was typed 4.0 with the\n'
                       '# Declared+: range in the Source line below.\n',
                       1),
                      ('ROCHE_LIMIT_RADII: unit and figure count',
                       'ROCHE_LIMIT_RADII = 3.45\n',
                       'ROCHE_LIMIT_RADII = 3.45\n'
                       '# Unit: r_sun\n'
                       '# Figures: 1 -- set by the comet density it is worked out from, "~500"\n'
                       '# Figures+: kg/m3, one figure (Rule 3; a cube root does not magnify it).\n'
                       '# Note: its inputs are typed in the Calculation lines below, not rows;\n'
                       '# Note+: sourcing the comet density is recorded on L-371. Drawn at the\n'
                       '# Note+: full 3.45, printed at one figure.\n',
                       1),
                      ('ALFVEN_SURFACE_RADII: unit, status, figures, read',
                       'ALFVEN_SURFACE_RADII = 19.7\n',
                       'ALFVEN_SURFACE_RADII = 19.7\n'
                       '# Unit: r_sun\n'
                       '# Status: measured V_SOURCED 2026-10-03 -- open full text\n'
                       '# Figures: 3 -- the source prints 19.7.\n'
                       '# Read: p. 255101-1, Kasper et al. (2021), the APS article page,\n'
                       '# Read+: 2026-10-03, Claude Opus 5.5. Table 1 of the same paper lists\n'
                       "# Read+: the interval's start as 19.8; the text's 19.7 is kept.\n"
                       '# Access: open, https://doi.org/10.1103/PhysRevLett.127.255101\n'
                       '# Access+: (2026-10-03).\n',
                       1)],
 'constants_rows.py': [('docstring: row_text',
                        'conversion_shape() finds every row shaped like one, conversion_problem()\n'
                        'is the one check of a marked one, and conversion_text() prints one at\n'
                        'the count its source row gives it.)\n'
                        '"""\n',
                        'conversion_shape() finds every row shaped like one, conversion_problem()\n'
                        'is the one check of a marked one, and conversion_text() prints one at\n'
                        'the count its source row gives it.)\n'
                        "Module updated: October 3, 2026 with Anthropic's Claude Opus 5.5\n"
                        "(L-371, the Sun's distance cards: row_text() prints any row at the\n"
                        'count its row gives it, in its own unit or in another unit of its\n'
                        'dimension, so an orrery hover need not choose a width. It is the\n'
                        'general form of exact_text() and conversion_text(), and computes\n'
                        'through the same conversions() the export serves.)\n'
                        '"""\n',
                        1),
                       ('row_text(): any row at its count, in any unit of its dimension',
                        '    if not isinstance(entry["figures"], int):\n'
                        '        raise ValueError("%s: its source row declares no count" % name)\n'
                        '    return format_prints(entry["value"], entry["figures"], grouping)\n',
                        '    if not isinstance(entry["figures"], int):\n'
                        '        raise ValueError("%s: its source row declares no count" % name)\n'
                        '    return format_prints(entry["value"], entry["figures"], grouping)\n'
                        '\n'
                        '\n'
                        '_ROW_TEXT_CACHE = {}\n'
                        '\n'
                        '\n'
                        'def row_text(name, unit=None, grouping=False, project_dir=None):\n'
                        '    """Row `name` as text, at the count its row gives it.\n'
                        '\n'
                        "    In the row's own unit by default, or in `unit`, another token of\n"
                        "    the same dimension ('km', 'au', 'r_sun', 'pc'), computed by\n"
                        '    conversions() exactly as the export serves it -- so the orrery and\n'
                        '    the gallery print the same digits. A measured or derived row prints\n'
                        "    at its '# Figures:' count; an exact row at its print count. A row\n"
                        '    with neither raises ValueError where the display is built, instead\n'
                        '    of a width being chosen for it. L-371, 2026-10-03.\n'
                        '\n'
                        '    The store is read once per process and kept, because a hover module\n'
                        '    calls this many times at import.\n'
                        '    """\n'
                        '    project_dir = project_dir or '
                        'os.path.dirname(os.path.abspath(__file__))\n'
                        '    cached = _ROW_TEXT_CACHE.get(project_dir)\n'
                        '    if cached is None:\n'
                        '        from constants_tokens import TOKENS\n'
                        '        _text, _rows, by_name = read_store(project_dir)\n'
                        '        values = load_values(project_dir)\n'
                        '        units = dict((n, r.unit) for n, r in by_name.items())\n'
                        '        cached = (by_name, values, units, TOKENS)\n'
                        '        _ROW_TEXT_CACHE[project_dir] = cached\n'
                        '    by_name, values, units, tokens = cached\n'
                        '    row = by_name[name]\n'
                        '    if unit is None or unit == row.unit:\n'
                        '        entry = {"value": values[name], "figures": row.figures,\n'
                        '                 "prints": row.prints}\n'
                        '    else:\n'
                        '        entries, problem = conversions(row, values[name], values, units,\n'
                        '                                       tokens)\n'
                        '        if problem or not entries or unit not in entries:\n'
                        '            raise ValueError("%s gives no value in %r (%s)"\n'
                        '                             % (name, unit, problem))\n'
                        '        entry = entries[unit]\n'
                        '    if entry["figures"] == "exact":\n'
                        '        if entry["prints"] is None:\n'
                        '            raise ValueError("%s is exact and states no print count; add '
                        '"\n'
                        '                             "\'prints N\' after \'exact --\'" % name)\n'
                        '        return format_prints(entry["value"], entry["prints"], grouping)\n'
                        '    if not isinstance(entry["figures"], int):\n'
                        '        raise ValueError("%s declares no figure count" % name)\n'
                        '    return format_prints(entry["value"], entry["figures"], grouping)\n',
                        1)],
 'constants_tokens.py': [('the pc token, defined by KM_PER_PARSEC',
                          '    "r_sun": {\n'
                          '        "dimension": "km",\n'
                          '        "defining_constant": "SUN_RADIUS_KM",\n'
                          '        "meaning": "solar radii, IAU nominal",\n'
                          '    },\n',
                          '    "r_sun": {\n'
                          '        "dimension": "km",\n'
                          '        "defining_constant": "SUN_RADIUS_KM",\n'
                          '        "meaning": "solar radii, IAU nominal",\n'
                          '    },\n'
                          "    # L-371 (2026-10-03): the Sun's gravitational reach is published\n"
                          '    # in parsecs, so its row is stored in parsecs and every length\n'
                          '    # now also converts into them.\n'
                          '    "pc": {\n'
                          '        "dimension": "km",\n'
                          '        "defining_constant": "KM_PER_PARSEC",\n'
                          '        "meaning": "parsecs, exactly 648000/pi au (IAU 2015 B2)",\n'
                          '    },\n',
                          1)],
 'exact_rows_report.py': [('docstring: row_text prints by the count too',
                           'serves it as "prints", orrery displays print through\n'
                           'constants_rows.exact_text(), and the gallery prints by the served\n',
                           'serves it as "prints", orrery displays print through\n'
                           'constants_rows.exact_text() or constants_rows.row_text(), and the\n'
                           'gallery prints by the served\n',
                           1),
                          ('docstring: the failing form',
                           '    - an orrery line prints an exact row any way but exact_text() -- '
                           'a\n',
                           '    - an orrery line prints an exact row any way but exact_text() or\n'
                           '      row_text() -- a\n',
                           1),
                          ('docstring: the orrery half',
                           'exact_text, _declared, _whole_figures or _with_uncertainty, after %,\n'
                           'or inside str(...) or format(...). Only exact_text prints by the '
                           'count.\n',
                           'exact_text, row_text, _declared, _whole_figures or _with_uncertainty,\n'
                           'after %, or inside str(...) or format(...). Only exact_text and\n'
                           'row_text print by the count.\n',
                           1),
                          ('docstring: credit line',
                           'kilometres per solar radius.)\n"""\n',
                           'kilometres per solar radius.)\n'
                           "Module updated: October 3, 2026 with Anthropic's Claude Opus 5.5\n"
                           '(L-371: the orrery search also finds constants_rows.row_text(), which\n'
                           'prints a row by its count in any unit. Without it a hover printing an\n'
                           'exact row through row_text() was not counted as a print at all, so '
                           'the\n'
                           'check could not see it -- found when the patched tree reported fewer\n'
                           'printed rows than before.)\n'
                           '"""\n',
                           1),
                          ('the orrery print pattern finds row_text',
                           '        + r\'|exact_text\\(\\s*[\\\'"]%s[\\\'"]\' % n\n',
                           '        + r\'|exact_text\\(\\s*[\\\'"]%s[\\\'"]\' % n\n'
                           '        + r\'|row_text\\(\\s*[\\\'"]%s[\\\'"]\' % n\n',
                           1),
                          ('by_count docstring',
                           '    own: every printing form but exact_text() is one. A name passed '
                           'to\n',
                           '    own: every printing form but exact_text() and row_text() is one. '
                           'A\n'
                           '    name passed to\n',
                           1),
                          ('report text',
                           "        'line prints it through `exact_text()`, and the gallery serves "
                           "'\n",
                           "        'line prints it through `exact_text()` or `row_text()`, and "
                           "the '\n"
                           "        'gallery serves '\n",
                           1),
                          ('verdict text',
                           "          'state a count; %d orrery lines print through exact_text(); "
                           "%s'\n",
                           "          'state a count; %d orrery lines print through exact_text() "
                           "or '\n"
                           "          'row_text(); %s'\n",
                           1)],
 'palomas_orrery.py': [('docstring: credit line',
                        'longer cut off with its hover marker, and the Sun direction arrow is\n'
                        "fitted inside the cube. Tony's ruling, 2026-09-23.)\n",
                        'longer cut off with its hover marker, and the Sun direction arrow is\n'
                        "fitted inside the cube. Tony's ruling, 2026-09-23.)\n"
                        "Module updated: October 3, 2026 with Anthropic's Claude Opus 5.5 (L-371:\n"
                        "the manual-scale tooltip prints the Sun's distances from their rows at\n"
                        'their counts -- the termination shock at 94.01 AU, the heliopause at\n'
                        "121 AU where it typed 126, and the gravitational reach as the Sun's\n"
                        'Hill radius, 134,000 AU, where it printed every digit.)\n',
                        1),
                       ('import row_text',
                        'from info_dictionary import INFO\n',
                        "# L-371: the Sun's distances printed from their rows at their counts.\n"
                        'from constants_rows import row_text\n'
                        'from info_dictionary import INFO\n',
                        1),
                       ('manual-scale tooltip: termination shock and heliopause from their rows',
                        '"with a mean distance of 526 AU\\n* Planet 9, use 360 AU for full '
                        'orbit\\n* Solar Wind Termination Shock: 94 AU\\n* Heliopause (edge of the '
                        'Sun\'s influence): 126 AU\\n* Voyager 1: currently over 165 AU\\n" \n',
                        'f"with a mean distance of 526 AU\\n* Planet 9, use 360 AU for full '
                        'orbit\\n* Solar Wind Termination Shock: '
                        "{row_text('TERMINATION_SHOCK_AU')} AU\\n* Heliopause (edge of the Sun's "
                        "influence): {row_text('HELIOPAUSE_AU')} AU\\n* Voyager 1: currently over "
                        '165 AU\\n" \n',
                        1),
                       ('manual-scale tooltip: the Oort edges from their rows',
                        '"* Inner Limit of Oort Cloud: 2,000 AU\\n* Outer Limit of Oort Cloud: '
                        '100,000 AU\\n"\n',
                        'f"* Inner Limit of Oort Cloud: {row_text(\'INNER_LIMIT_OORT_CLOUD_AU\', '
                        'grouping=True)} AU\\n* Outer Limit of Oort Cloud: '
                        '{row_text(\'OUTER_OORT_CLOUD_AU\', grouping=True)} AU\\n"\n',
                        1),
                       ('manual-scale tooltip: the gravitational reach at its count',
                        '# Source+: literal with no link to the store until 2026-08-07 (L-179).\n'
                        'f"* Extent of Solar Gravitational Influence (Hill Sphere): "\n'
                        'f"{GRAVITATIONAL_INFLUENCE_AU:,.0f} AU\\n* Proxima Centauri: 268,585 '
                        'AU")\n',
                        '# Source+: literal with no link to the store until 2026-08-07 (L-179).\n'
                        "# Source+: Since 2026-10-03 (L-371) the row is the Sun's Hill radius in\n"
                        '# Source+: parsecs, GRAVITATIONAL_INFLUENCE_PC, printed here in AU at its '
                        'count.\n'
                        'f"* Extent of Solar Gravitational Influence (Hill Sphere): "\n'
                        'f"{row_text(\'GRAVITATIONAL_INFLUENCE_PC\', \'au\', grouping=True)} '
                        'AU\\n* Proxima Centauri: 268,585 AU")\n',
                        1)],
 'planet_visualization_utilities.py': [('import: the unsourced range row is gone (L-371)',
                                        '    GRAVITATIONAL_INFLUENCE_AU, '
                                        'GRAVITATIONAL_INFLUENCE_RANGE_AU,\n'
                                        ')\n',
                                        '    GRAVITATIONAL_INFLUENCE_AU,\n)\n',
                                        1)],
 'solar_visualization_shells.py': [('docstring: credit line',
                                    "Module updated: October 2, 2026 with Anthropic's Claude Opus "
                                    '5.5\n',
                                    "Module updated: October 3, 2026 with Anthropic's Claude Opus "
                                    '5.5\n'
                                    "(L-371, the Sun's distance cards: every hover line that "
                                    'states one of\n'
                                    "the Sun's distance rows prints it from the row, at the count "
                                    'its row\n'
                                    'gives it, through constants_rows.row_text() -- the '
                                    'termination shock\n'
                                    "at 94.01 AU, the heliopause at 121 AU, the Oort cloud's edges "
                                    'with\n'
                                    "their ranges, the gravitational reach as the Sun's Hill "
                                    'radius, 0.65\n'
                                    'parsecs, and the corona, helmet cusp and Roche limit by their '
                                    'counts.\n'
                                    'The unsourced 100,000-200,000 AU range is gone with its row. '
                                    'Wording\n'
                                    'changes approved by Tony are listed in the session handoff.)\n'
                                    '\n'
                                    "Module updated: October 2, 2026 with Anthropic's Claude Opus "
                                    '5.5\n',
                                    1),
                                   ('imports: the range row is gone; row_text',
                                    '                                            '
                                    'GRAVITATIONAL_INFLUENCE_AU, '
                                    'GRAVITATIONAL_INFLUENCE_RANGE_AU,\n',
                                    '                                            '
                                    'GRAVITATIONAL_INFLUENCE_AU,\n',
                                    1),
                                   ('imports: row_text',
                                    'from constants_rows import figures_of, exact_text, '
                                    'format_prints, conversion_text\n',
                                    'from constants_rows import figures_of, exact_text, '
                                    'format_prints, conversion_text\n'
                                    '# L-371: every Sun distance row prints at its own count, in '
                                    'any unit.\n'
                                    'from constants_rows import row_text\n',
                                    1),
                                   ('the gravitational sentence, and the shared distance texts',
                                    '# Source: GRAVITATIONAL_INFLUENCE_AU and '
                                    'GRAVITATIONAL_INFLUENCE_RANGE_AU\n'
                                    '# Source+: in constants_new.py -- approximate Hill sphere of '
                                    'the Sun in the\n'
                                    '# Source+: Milky Way, model-dependent. Published estimates '
                                    'span\n'
                                    '# Source+: 100,000-200,000 AU; the visualization draws the '
                                    '150,000 AU\n'
                                    "# Source+: midpoint (Tony's ruling, 2026-08-07). Light-year "
                                    'figures derive\n'
                                    '# Source+: from AU_PER_LIGHT_YEAR. NASA Solar System '
                                    'Exploration.\n'
                                    'GRAVITATIONAL_INFLUENCE_SENTENCE = (\n'
                                    '    f"The Sun\'s gravitational influence extends to roughly '
                                    '"\n'
                                    '    f"{GRAVITATIONAL_INFLUENCE_AU / AU_PER_LIGHT_YEAR:.1f} '
                                    'light-years "\n'
                                    '    f"(~{GRAVITATIONAL_INFLUENCE_AU:,.0f} AU).<br>"\n'
                                    '    f"Published estimates range "\n'
                                    '    f"{GRAVITATIONAL_INFLUENCE_RANGE_AU[0]:,.0f}-"\n'
                                    '    f"{GRAVITATIONAL_INFLUENCE_RANGE_AU[1]:,.0f} AU "\n'
                                    '    f"({GRAVITATIONAL_INFLUENCE_RANGE_AU[0] / '
                                    'AU_PER_LIGHT_YEAR:.1f}-"\n'
                                    '    f"{GRAVITATIONAL_INFLUENCE_RANGE_AU[1] / '
                                    'AU_PER_LIGHT_YEAR:.1f} "\n'
                                    '    f"light-years); this visualization draws the midpoint."\n'
                                    ')\n'
                                    '\n',
                                    "# The Sun's distances as text, each printed from its row at "
                                    'the count the\n'
                                    '# row gives it (L-371, 2026-10-03). A hover names these, '
                                    'never a typed\n'
                                    '# figure, so the words cannot drift from the drawing or from '
                                    'the store.\n'
                                    "_OORT_INNER_EDGE = row_text('INNER_LIMIT_OORT_CLOUD_AU', "
                                    'grouping=True)\n'
                                    "_OORT_HILLS_EDGE = row_text('INNER_OORT_CLOUD_AU', "
                                    'grouping=True)\n'
                                    "_OORT_OUTER_EDGE = row_text('OUTER_OORT_CLOUD_AU', "
                                    'grouping=True)\n'
                                    "_HELIOPAUSE = row_text('HELIOPAUSE_AU')\n"
                                    "_TERMINATION_SHOCK = row_text('TERMINATION_SHOCK_AU')\n"
                                    "# Tony's approved notes for the two ranged edges, "
                                    '2026-10-03.\n'
                                    'OORT_INNER_EDGE_NOTE = (\n'
                                    '    f"Thought to lie between "\n'
                                    '    f"{row_text(\'OORT_CLOUD_INNER_EDGE_LOW_AU\', '
                                    'grouping=True)} and "\n'
                                    '    f"{row_text(\'OORT_CLOUD_INNER_EDGE_HIGH_AU\', '
                                    'grouping=True)} AU; "\n'
                                    '    f"drawn at {_OORT_INNER_EDGE}."\n'
                                    ')\n'
                                    'OORT_OUTER_EDGE_NOTE = (\n'
                                    '    f"Thought to lie between "\n'
                                    '    f"{row_text(\'OORT_CLOUD_OUTER_EDGE_LOW_AU\', '
                                    'grouping=True)} and "\n'
                                    '    f"{row_text(\'OORT_CLOUD_OUTER_EDGE_HIGH_AU\', '
                                    'grouping=True)} AU; "\n'
                                    '    f"drawn at {_OORT_OUTER_EDGE}."\n'
                                    ')\n'
                                    '\n'
                                    '# Source: GRAVITATIONAL_INFLUENCE_PC in constants_new.py -- '
                                    "the Sun's\n"
                                    '# Source+: Hill radius in the galaxy, Portegies Zwart et al. '
                                    '(2021). The\n'
                                    '# Source+: AU and light-year figures are computed from it and '
                                    'printed at\n'
                                    "# Source+: its two figures. Words: Tony's approved note of "
                                    '2026-10-03.\n'
                                    'GRAVITATIONAL_INFLUENCE_SENTENCE = (\n'
                                    '    "The Sun\'s Hill radius in the galaxy, calculated where '
                                    'the galaxy\'s<br>"\n'
                                    '    "tidal pull overtakes the Sun\'s gravity: about "\n'
                                    '    f"{row_text(\'GRAVITATIONAL_INFLUENCE_PC\')} '
                                    'parsecs<br>"\n'
                                    '    f"({row_text(\'GRAVITATIONAL_INFLUENCE_PC\', \'au\', '
                                    'grouping=True)} AU, "\n'
                                    '    f"about {format_prints(GRAVITATIONAL_INFLUENCE_AU / '
                                    "AU_PER_LIGHT_YEAR, figures_of('GRAVITATIONAL_INFLUENCE_PC'))} "
                                    '"\n'
                                    '    "light-years). Calculated, not measured."\n'
                                    ')\n'
                                    '\n',
                                    1),
                                   ('gravitational: the heliopause from its row',
                                    '            "The Solar System\\\'s extent is actually defined '
                                    'in multiple ways. The Heliopause (120-123 AU):<br>" \n',
                                    '            f"The Solar System\\\'s extent is actually '
                                    'defined in multiple ways. The Heliopause ({_HELIOPAUSE} '
                                    'AU):<br>" \n',
                                    2),
                                   ('gravitational: the Oort edges from their rows',
                                    '            "Oort Cloud (2,000-20,000 AU), and the Outer Oort '
                                    'Cloud (20,000-100,000 AU).<br><br>" \n',
                                    '            f"Oort Cloud '
                                    '({_OORT_INNER_EDGE}-{_OORT_HILLS_EDGE} AU), and the Outer '
                                    'Oort Cloud ({_OORT_HILLS_EDGE}-{_OORT_OUTER_EDGE} '
                                    'AU).<br><br>" \n',
                                    2),
                                   ("Oort shells: the cloud's span from its rows (tooltip and "
                                    'hover, x6)',
                                    '            "Solar System at distances ranging from '
                                    'approximately 2,000 AU to 100,000 AU from the Sun.',
                                    '            f"Solar System at distances ranging from '
                                    'approximately {_OORT_INNER_EDGE} AU to {_OORT_OUTER_EDGE} AU '
                                    'from the Sun.',
                                    6),
                                   ('Oort shells: the Hills cloud from its rows (x4)',
                                    '            "Inner Oort Cloud (Hills Cloud): Extends from '
                                    'about 2,000 AU to 20,000 AU. More tightly bound to '
                                    'the<br>" \n',
                                    '            f"Inner Oort Cloud (Hills Cloud): Extends from '
                                    'about {_OORT_INNER_EDGE} AU to {_OORT_HILLS_EDGE} AU. More '
                                    'tightly bound to the<br>" \n',
                                    4),
                                   ("outer Oort: the edge drawn and its range, Tony's note (x2)",
                                    '            "Oort Cloud\'s Outer Edge: At 100,000 AU, it\'s '
                                    'about 1.58 light-years from the Sun, placing it just<br>" \n'
                                    '            "beyond the nearest star systems and marking the '
                                    'boundary between the Solar System and interstellar '
                                    'space.<br><br>" \n',
                                    '            "Oort Cloud\'s Outer Edge:<br>" \n'
                                    '            f"{OORT_OUTER_EDGE_NOTE}<br>" \n'
                                    '            f"At {_OORT_OUTER_EDGE} AU it is about '
                                    '{format_prints(OUTER_OORT_CLOUD_AU / AU_PER_LIGHT_YEAR, 1)} '
                                    'light-years from the Sun, marking the boundary<br>" \n'
                                    '            "between the Solar System and interstellar '
                                    'space.<br><br>" \n',
                                    2),
                                   ("inner limit: Tony's note under the title (x2)",
                                    '            "Oort Cloud: Inner Limit:<br><br>"\n',
                                    '            "Oort Cloud: Inner Limit:<br><br>"\n'
                                    '            f"{OORT_INNER_EDGE_NOTE}<br><br>"\n',
                                    2),
                                   ('torus, clumps, tide tooltips: the Hills cloud from its rows '
                                    '(x3)',
                                    '            "* Hills Cloud (Inner Oort): 2,000-20,000 AU, '
                                    'disk-like/toroidal<br>"\n',
                                    '            f"* Hills Cloud (Inner Oort): '
                                    '{_OORT_INNER_EDGE}-{_OORT_HILLS_EDGE} AU, '
                                    'disk-like/toroidal<br>"\n',
                                    3),
                                   ('torus, clumps, tide tooltips: the outer cloud from its rows '
                                    '(x3)',
                                    '            "* Outer Oort Cloud: 20,000-100,000+ AU, roughly '
                                    'spherical but clumpy<br>" \n',
                                    '            f"* Outer Oort Cloud: '
                                    '{_OORT_HILLS_EDGE}-{_OORT_OUTER_EDGE}+ AU, roughly spherical '
                                    'but clumpy<br>" \n',
                                    3),
                                   ('torus hover: its span from the rows',
                                    "        '2,000-20,000 AU<br>'\n",
                                    "        f'{_OORT_INNER_EDGE}-{_OORT_HILLS_EDGE} AU<br>'\n",
                                    1),
                                   ('clumps hover: its span from the rows',
                                    "        '20,000-100,000+ AU<br>'\n",
                                    "        f'{_OORT_HILLS_EDGE}-{_OORT_OUTER_EDGE}+ AU<br>'\n",
                                    1),
                                   ("heliopause: Voyager 1's crossing from the row (x2)",
                                    '            "at ~123 AU. This is considered the end of the '
                                    "Sun's influence and the start of interstellar "
                                    'space.<br><br>" \n',
                                    '            f"at {_HELIOPAUSE} AU. This is considered the end '
                                    "of the Sun's influence and the start of interstellar "
                                    'space.<br><br>" \n',
                                    2),
                                   ('heliopause: where the heliosheath lies, from the two rows '
                                    '(x2)',
                                    '            "* The heliosheath extends from ~120 to 150 AU at '
                                    'the Heliopause.<br>"\n',
                                    '            f"* The heliosheath lies between the termination '
                                    'shock ({_TERMINATION_SHOCK} AU) and the heliopause<br>"\n'
                                    '            f"  ({_HELIOPAUSE} AU), on Voyager 1\'s '
                                    'path.<br>"\n',
                                    2),
                                   ("termination shock: Voyager 1's crossing from the row (x2)",
                                    '            "Voyager 1 encountered the Termination Shock at '
                                    '94 AU, while Voyager 2 at 84 AU.<br>"\n',
                                    '            f"Voyager 1 encountered the Termination Shock at '
                                    '{_TERMINATION_SHOCK} AU, while Voyager 2 at 84 AU.<br>"\n',
                                    2),
                                   ("outer corona tooltip: the radius from its row, and Tony's "
                                    'note',
                                    '    "This shell marks the extended outer solar corona at ~50 '
                                    'solar radii (~0.23 AU).<br>"\n',
                                    '    f"This shell marks the extended outer solar corona at '
                                    "{row_text('OUTER_CORONA_RADII')} solar radii "
                                    '({row_text(\'OUTER_CORONA_RADII\', \'au\')} AU).<br>"\n'
                                    '    "A boundary chosen for the drawing; the faint outer '
                                    'corona has no sharp edge.<br>"\n',
                                    1),
                                   ("outer corona tooltip: the shell's radius from its row",
                                    '    "* This 50 R_sun shell represents the faint, extended '
                                    'F-corona envelope.<br><br>"\n',
                                    '    f"* This {row_text(\'OUTER_CORONA_RADII\')} R_sun shell '
                                    'represents the faint, extended F-corona envelope.<br><br>"\n',
                                    1),
                                   ("outer corona hover: the radius from its row, and Tony's note",
                                    '    "Extended outer solar corona at ~50 solar radii (~0.23 '
                                    'AU).<br>"\n',
                                    '    f"Extended outer solar corona at '
                                    "{row_text('OUTER_CORONA_RADII')} solar radii "
                                    '({row_text(\'OUTER_CORONA_RADII\', \'au\')} AU).<br>"\n'
                                    '    "A boundary chosen for the drawing; the faint outer '
                                    'corona has no sharp edge.<br>"\n',
                                    1),
                                   ('outer corona hover: the streamer belt as it is drawn now',
                                    '    "* Visible streamer belt: drawn at 6.0 R_sun, an '
                                    'approximation<br>"\n'
                                    '    "  (see Streamer Belt shell)<br>"\n',
                                    '    f"* Streamer belt: the helmets pinch at '
                                    "{row_text('HELMET_CUSP_RADII')} R_sun, and the stalk fades "
                                    'out<br>"\n'
                                    '    "  across the Alfven surface (see Streamer Belt '
                                    'shell)<br>"\n',
                                    1),
                                   ("outer corona hover: the F-corona's span from the rows",
                                    '    "* F-corona (dust-scattered): 3-50+ R_sun -- this '
                                    'shell\'s extent<br><br>"\n',
                                    '    f"* F-corona (dust-scattered): '
                                    "{row_text('INNER_CORONA_RADII')}-{row_text('OUTER_CORONA_RADII')}+ "
                                    'R_sun -- this shell\'s extent<br><br>"\n',
                                    1),
                                   ('inner corona: the drawn radius from its row (tooltip and '
                                    'hover)',
                                    '"* Solar Inner Corona (extends to 2-3 solar radii, ~0.014 '
                                    'AU)<br>"\n',
                                    'f"* Solar Inner Corona (extends to 2-3 solar radii; drawn at '
                                    "{row_text('INNER_CORONA_RADII')}, about "
                                    '{row_text(\'INNER_CORONA_RADII\', \'au\')} AU)<br>"\n',
                                    2),
                                   ('inner corona hover: the Roche limit at its count',
                                    '    "* The fluid Roche limit for comets (~3.45 R_sun) lies '
                                    'just outside this shell.<br>"\n',
                                    '    f"* The fluid Roche limit for comets (about '
                                    "{row_text('ROCHE_LIMIT_RADII')} R_sun) lies just outside this "
                                    'shell.<br>"\n',
                                    1),
                                   ('Roche tooltip: the result at its count',
                                    '    "Result: ~3.45 solar radii = ~2,400,165 km from Sun '
                                    'center<br>"\n'
                                    '    "  = ~1,704,465 km from photosphere (~0.0114 '
                                    'AU)<br><br>"\n',
                                    '    f"Result: about {row_text(\'ROCHE_LIMIT_RADII\')} solar '
                                    "radii, about {row_text('ROCHE_LIMIT_RADII', 'km', "
                                    'grouping=True)} km from the Sun\'s center<br>"\n'
                                    '    f"  ({row_text(\'ROCHE_LIMIT_RADII\', \'au\')} AU). The '
                                    'comet density is known to one figure, so the result is '
                                    'too.<br><br>"\n',
                                    1),
                                   ('Roche tooltip: MAPS passage at the count',
                                    '    "* The debris swept THROUGH the Roche limit (3.45 R_sun, '
                                    '0.016 AU) to perihelion<br>"\n',
                                    '    f"* The debris swept THROUGH the Roche limit (about '
                                    "{row_text('ROCHE_LIMIT_RADII')} R_sun, "
                                    "{row_text('ROCHE_LIMIT_RADII', 'au')} AU) to "
                                    'perihelion<br>"\n',
                                    1),
                                   ('Roche hover: the result at its count',
                                    '    "Result: ~3.45 R_sun (~0.016 AU) from Sun '
                                    'center<br><br>"\n',
                                    '    f"Result: about {row_text(\'ROCHE_LIMIT_RADII\')} R_sun '
                                    "({row_text('ROCHE_LIMIT_RADII', 'au')} AU) from Sun "
                                    'center;<br>"\n'
                                    '    "the comet density is known to one figure, so the result '
                                    'is too.<br><br>"\n',
                                    1),
                                   ("streamer tooltip: the helmets' range from the rows",
                                    '    "a dome of closed magnetic loops, reaches no higher than '
                                    '2-4 R_sun.<br>"\n',
                                    '    f"a dome of closed magnetic loops, reaches no higher than '
                                    "{row_text('HELMET_CUSP_LOW_RADII')}-{row_text('HELMET_CUSP_HIGH_RADII')} "
                                    'R_sun.<br>"\n',
                                    1),
                                   ('streamer tooltip: the cusp from its row',
                                    '    "and dense at the base, pinching at the cusp at 4.0 R_sun '
                                    'where the<br>"\n',
                                    '    f"and dense at the base, pinching at the cusp at '
                                    '{row_text(\'HELMET_CUSP_RADII\')} R_sun where the<br>"\n',
                                    1),
                                   ("streamer tooltip: the helmets' range again",
                                    '    "  helmet stays below 2-4 R_sun; its stalk continues far '
                                    'beyond.<br>"\n',
                                    '    f"  helmet stays below '
                                    "{row_text('HELMET_CUSP_LOW_RADII')}-{row_text('HELMET_CUSP_HIGH_RADII')} "
                                    'R_sun; its stalk continues far beyond.<br>"\n',
                                    1),
                                   ('streamer band: cusp and fade in km and AU from the rows',
                                    '    cusp_km, cusp_au = _km_au(cusp_rs)\n'
                                    '    fade_km, fade_au = _km_au(fade_rs)\n',
                                    '    # L-371: the cusp and the fade print from their rows, at '
                                    'their counts.\n',
                                    1),
                                   ('streamer band: the cusp line',
                                    '        f"higher than 2-4 R_sun, and the band pinches at '
                                    '{cusp_rs:.1f} R_sun<br>"\n'
                                    '        f"({cusp_km:,.0f} km, {cusp_au:.6f} AU) where they '
                                    'open.<br>"\n',
                                    '        f"higher than '
                                    "{row_text('HELMET_CUSP_LOW_RADII')}-{row_text('HELMET_CUSP_HIGH_RADII')} "
                                    'R_sun, and the band pinches at '
                                    '{row_text(\'HELMET_CUSP_RADII\')} R_sun<br>"\n'
                                    '        f"({row_text(\'HELMET_CUSP_RADII\', \'km\', '
                                    "grouping=True)} km, {row_text('HELMET_CUSP_RADII', 'au')} AU) "
                                    'where they open.<br>"\n',
                                    1),
                                   ('streamer band: the fade line',
                                    '        f"past the Alfven surface at {fade_rs:.1f} '
                                    'R_sun<br>"\n',
                                    '        f"past the Alfven surface at '
                                    '{row_text(\'ALFVEN_SURFACE_RADII\')} R_sun<br>"\n',
                                    1),
                                   ('streamer band: the fade in km and AU',
                                    '        f"({fade_km:,.0f} km, {fade_au:.6f} AU), where the '
                                    'corona becomes<br>"\n',
                                    '        f"({row_text(\'ALFVEN_SURFACE_RADII\', \'km\', '
                                    "grouping=True)} km, {row_text('ALFVEN_SURFACE_RADII', 'au')} "
                                    'AU), where the corona becomes<br>"\n',
                                    1),
                                   ('Sun marker hover and tooltip: the Roche limit at its count '
                                    '(x2)',
                                    "    '* Roche Limit: 3.45 R_sun -- tidal disruption threshold "
                                    "for comets<br>'\n",
                                    "    f'* Roche Limit: about {row_text('ROCHE_LIMIT_RADII')} "
                                    "R_sun -- tidal disruption threshold for comets<br>'\n",
                                    2),
                                   ('Sun marker hover and tooltip: the streamer belt as drawn now '
                                    '(x2)',
                                    "    '* Streamer Belt (Visible Corona): drawn at 6.0 R_sun, "
                                    "approximate<br>'\n",
                                    "    f'* Streamer Belt (Visible Corona): helmets pinch at "
                                    "{row_text('HELMET_CUSP_RADII')} R_sun, the stalk fades "
                                    "beyond<br>'\n",
                                    2),
                                   ('Sun marker hover and tooltip: the outer corona from its row '
                                    '(x2)',
                                    "    '* Extended Corona (F-corona): ~50 R_sun -- faint "
                                    "dust-scattered envelope<br><br>'\n",
                                    "    f'* Extended Corona (F-corona): "
                                    "{row_text('OUTER_CORONA_RADII')} R_sun, a boundary chosen for "
                                    "the drawing<br><br>'\n",
                                    2),
                                   ('galactic tide hover: its span from the rows, at their counts',
                                    "        f'From {INNER_OORT_CLOUD_AU:,} to "
                                    "{OUTER_OORT_CLOUD_AU:,} AU<br>'\n",
                                    "        f'From {_OORT_HILLS_EDGE} to {_OORT_OUTER_EDGE} "
                                    "AU<br>'\n",
                                    1)],
 'test_constants_provenance.py': [('docstring: credit line',
                                   'never makes them stale)\n\nRole: devtool\n',
                                   'never makes them stale)\n'
                                   "Module updated: October 3, 2026 with Anthropic's Claude Opus "
                                   '5.5\n'
                                   "(L-371: three relation tests for the Sun's distances -- each "
                                   'ranged\n'
                                   'edge is drawn at an end of its range, the heliopause and the\n'
                                   "gravitational reach are converted from their sources' units "
                                   'rather\n'
                                   'than typed twice, and the unsourced range row stays gone. '
                                   'Still no\n'
                                   'pinned values.)\n'
                                   '\n'
                                   'Role: devtool\n',
                                   1),
                                  ('import: the new rows; the range row is gone',
                                   '    GRAVITATIONAL_INFLUENCE_RANGE_AU,\n',
                                   "    # L-371: the Sun's ranged edges, and the rows in their "
                                   "sources' units\n"
                                   '    OORT_CLOUD_INNER_EDGE_LOW_AU,\n'
                                   '    OORT_CLOUD_INNER_EDGE_HIGH_AU,\n'
                                   '    OORT_CLOUD_OUTER_EDGE_LOW_AU,\n'
                                   '    OORT_CLOUD_OUTER_EDGE_HIGH_AU,\n'
                                   '    HELMET_CUSP_LOW_RADII,\n'
                                   '    HELMET_CUSP_HIGH_RADII,\n'
                                   '    HELIOPAUSE_AU,\n'
                                   '    GRAVITATIONAL_INFLUENCE_PC,\n'
                                   '    PARSEC_TO_AU,\n'
                                   '    KM_PER_PARSEC,\n'
                                   '    KM_PER_AU,\n'
                                   '    SUN_RADIUS_KM,\n',
                                   1),
                                  ("Section 4: three relation tests for the Sun's distances",
                                   '    assert INNER_LIMIT_OORT_CLOUD_AU < INNER_OORT_CLOUD_AU < '
                                   'OUTER_OORT_CLOUD_AU < GRAVITATIONAL_INFLUENCE_AU, \\\n'
                                   '        "Oort cloud shell ordering violated"\n',
                                   '    assert INNER_LIMIT_OORT_CLOUD_AU < INNER_OORT_CLOUD_AU < '
                                   'OUTER_OORT_CLOUD_AU < GRAVITATIONAL_INFLUENCE_AU, \\\n'
                                   '        "Oort cloud shell ordering violated"\n'
                                   '\n'
                                   '\n'
                                   'def test_sun_ranged_edges_drawn_at_an_end():\n'
                                   '    """L-371: each ranged edge is drawn at the end its row '
                                   'states.\n'
                                   '\n'
                                   "    The Oort cloud's inner edge at the near end of its range "
                                   'and its\n'
                                   "    outer edge at the far end (Tony's ruling A, 2026-10-03), "
                                   'and the\n'
                                   '    helmet cusp at the top of 2-4 solar radii.\n'
                                   '    """\n'
                                   '    assert OORT_CLOUD_INNER_EDGE_LOW_AU < '
                                   'OORT_CLOUD_INNER_EDGE_HIGH_AU\n'
                                   '    assert INNER_LIMIT_OORT_CLOUD_AU == '
                                   'OORT_CLOUD_INNER_EDGE_LOW_AU, \\\n'
                                   '        "the inner edge is not drawn at the near end of its '
                                   'range"\n'
                                   '    assert OORT_CLOUD_OUTER_EDGE_LOW_AU < '
                                   'OORT_CLOUD_OUTER_EDGE_HIGH_AU\n'
                                   '    assert OUTER_OORT_CLOUD_AU == '
                                   'OORT_CLOUD_OUTER_EDGE_HIGH_AU, \\\n'
                                   '        "the outer edge is not drawn at the far end of its '
                                   'range"\n'
                                   '    assert HELMET_CUSP_LOW_RADII < HELMET_CUSP_HIGH_RADII\n'
                                   '    assert HELMET_CUSP_RADII == HELMET_CUSP_HIGH_RADII, \\\n'
                                   '        "the helmet cusp is not drawn at the top of its '
                                   'range"\n'
                                   '\n'
                                   '\n'
                                   'def test_sun_distances_converted_not_typed():\n'
                                   '    """L-371 / L-386: one distance, one row, in its source\'s '
                                   'unit.\n'
                                   '\n'
                                   '    The heliopause is stored in AU and the gravitational reach '
                                   'in\n'
                                   '    parsecs; the solar-radii and AU names are computed from '
                                   'them.\n'
                                   '    """\n'
                                   '    rel = 1e-12\n'
                                   '    expect = HELIOPAUSE_AU * KM_PER_AU / SUN_RADIUS_KM\n'
                                   '    assert abs(HELIOPAUSE_RADII - expect) <= rel * expect, \\\n'
                                   '        f"HELIOPAUSE_RADII {HELIOPAUSE_RADII} is not '
                                   'HELIOPAUSE_AU converted ({expect})"\n'
                                   '    expect = PARSEC_TO_AU * KM_PER_AU\n'
                                   '    assert abs(KM_PER_PARSEC - expect) <= rel * expect, \\\n'
                                   '        f"KM_PER_PARSEC {KM_PER_PARSEC} is not PARSEC_TO_AU in '
                                   'km ({expect})"\n'
                                   '    expect = GRAVITATIONAL_INFLUENCE_PC * PARSEC_TO_AU\n'
                                   '    assert abs(GRAVITATIONAL_INFLUENCE_AU - expect) <= rel * '
                                   'expect, \\\n'
                                   '        f"GRAVITATIONAL_INFLUENCE_AU '
                                   '{GRAVITATIONAL_INFLUENCE_AU} is not the parsec row in AU '
                                   '({expect})"\n'
                                   '\n'
                                   '\n'
                                   'def test_unsourced_gravitational_range_stays_gone():\n'
                                   '    """L-371: the 100,000-200,000 AU range had no source and '
                                   'went with\n'
                                   '    the midpoint drawn from it. A row of that name coming back '
                                   'would\n'
                                   '    put an unsourced range back in front of a visitor."""\n'
                                   '    import constants_new\n'
                                   '    assert not hasattr(constants_new, '
                                   '"GRAVITATIONAL_INFLUENCE_RANGE_AU"), \\\n'
                                   '        "GRAVITATIONAL_INFLUENCE_RANGE_AU is back in '
                                   'constants_new.py"\n',
                                   1)],
 'test_worksheet_checker.py': [('docstring: credit line',
                                "Module updated: August 18, 2026 with Anthropic's Claude Opus 5 "
                                '(L-207).\n',
                                "Module updated: August 18, 2026 with Anthropic's Claude Opus 5 "
                                '(L-207).\n'
                                "Module updated: October 3, 2026 with Anthropic's Claude Opus 5.5 "
                                '(L-371:\n'
                                'HELIOPAUSE_RADII leaves the live-corpus movement pin. Its two '
                                'cross-check\n'
                                'legs retired with the value they checked, so no claim attaches to '
                                'it.)\n',
                                1),
                               ('the live-corpus pin: HELIOPAUSE_RADII retired from it',
                                '# All four moved after their worksheets ran, and all four sit in\n'
                                '# worksheets whose only verdict column asks about the CITATION. '
                                'So the\n'
                                '# tool cannot say whether the movement was a correction or a '
                                'defect,\n'
                                '# and says so. Before 2026-08-15 it called all eight rows '
                                'DRIFTED,\n'
                                '# which asserted the strongest of the three readings on no '
                                'evidence.\n'
                                "UNCHECKED_MOVE_CONSTANTS = ('HELIOPAUSE_RADII', "
                                "'BENNU_RADIUS_KM',\n"
                                "                            'HAUMEA_RADIUS_KM', "
                                "'ARROKOTH_RADIUS_KM')\n",
                                '# All three moved after their worksheets ran, and all three sit '
                                'in\n'
                                '# worksheets whose only verdict column asks about the CITATION. '
                                'So the\n'
                                '# tool cannot say whether the movement was a correction or a '
                                'defect,\n'
                                '# and says so. Before 2026-08-15 it called all eight rows '
                                'DRIFTED,\n'
                                '# which asserted the strongest of the three readings on no '
                                'evidence.\n'
                                '# HELIOPAUSE_RADII was the fourth until 2026-10-03 (L-371): it '
                                'became a\n'
                                '# conversion of HELIOPAUSE_AU, read from Gurnett et al. (2013) as '
                                '121 AU,\n'
                                '# and its Cross-checked legs of 2026-08-02 retired with the 121.6 '
                                'AU they\n'
                                '# had certified, which the paper does not print. With no '
                                'annotation on\n'
                                '# the row there is no claim for the checker to see move.\n'
                                "UNCHECKED_MOVE_CONSTANTS = ('BENNU_RADIUS_KM',\n"
                                "                            'HAUMEA_RADIUS_KM', "
                                "'ARROKOTH_RADIUS_KM')\n",
                                1)]}


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
                "       17ef6660, or this patch has already run.\n"
                "       (Line endings are excluded, so they are not the cause.)\n"
                "       NOTHING was written." % (path, BASE[path], got))
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
            print("ok  %-34s %s" % (path, label))
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    print("  1. Run orrery_maintenance_run.py (VS Code, Run). Expect 21 of 22;")
    print("     Constants change fails naming the six rows and the removed")
    print("     range row listed at the top of this script, and nothing else.")
    print("  2. Move this script into documentation/; commit and push.")
    print("  3. Then the gallery patch, patch_L371_2.")


if __name__ == "__main__":
    main()
