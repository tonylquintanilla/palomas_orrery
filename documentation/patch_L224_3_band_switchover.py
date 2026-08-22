"""
patch_L224_3_band_switchover.py

L-224 build, patch 2 of 2. THIS IS THE ONE THAT CHANGES THE RENDER.

Eight files, one all-or-nothing transaction. Nothing is written unless
every anchor in every file matches exactly once.

WHAT IT DOES
  1. constants_new.py -- STREAMER_BELT_RADII = 6.0 becomes
     HELMET_CUSP_RADII = 4.0, sourced to Suess & Nerney (2004),
     Adv. Space Res. 33:668-675. The rename is the substance: 6.0 was an
     unsourced drawing choice sitting above the closed helmet and inside
     the open stalk, representing neither (L-210). 4.0 is the top of the
     helmet range the paper states, and it is a CUSP, not an outer edge.
  2. shell_configs.py -- 'streamer_belt' moves from SHELL_CONFIGS (the
     sphere builder) to CUSTOM_SHELLS['Sun'] (the band builder added in
     patch 1). This is the dispatch move; the rest is consequence.
  3. solar_visualization_shells.py -- the dead sphere function and the
     hover string that fed only it are DELETED, the tooltip is rewritten
     for the band, and the builder switches to the renamed constant.
  4. comet_visualization_shells.py -- rename, plus the typed
     "~6.0 R_sun, ~0.028 AU" and its typed verdict become computed.
  5-8. planet_visualization_utilities.py, planet_visualization.py,
     palomas_orrery.py (checkbox label), test_constants_provenance.py.

WHY THE CONSTANT COULD BE RENAMED SAFELY
  Measured, not assumed: the suite's ordering assertion holds at 4.0 --
  3.0 < 3.45 < 4.0 < 19.7 < 50 -- and all 15 provenance tests pass with
  the value substituted. Verified in the sandbox before delivery.

ONE THING DELIBERATELY NOT FIXED
  The MAPS disintegration radius. The repo carries 8.33 R_sun with only a
  "Verified via Gemini fact-check" leg. The figure is PLAUSIBLE -- from
  8.33 R_sun to a 1.23 R_sun perihelion is about four hours at these
  speeds, matching the NASA/LASCO statement that the nucleus was
  destroyed several hours before closest approach -- but plausible is
  not sourced -- so 8.33 cannot be a disintegration
  radius. That is L-225, not this patch. What this patch does is make
  the comparison COMPUTED, so both lines report correctly for whatever
  radius a real source eventually confirms, instead of typing one.

HOW TO RUN
  Save into the repo ROOT, open in VS Code, click Run. Then:
      python test_constants_provenance.py
      python -m py_compile palomas_orrery.py
  Then run the orrery, tick "-- Streamer Belt", and look at it. That is
  the Mode 5 gate and it is yours.

  If the render is wrong, revert with GitHub Desktop before pushing.

PERMANENT vs DISPOSABLE
  Disposable. Archive to documentation/ once run.

Built on 96707590ba445c58066787aef03299174a8f158b at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written August 22, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

FP = {'comet_visualization_shells.py': 'c1068d7ddedabee90ae43ac535881b9b',
 'constants_new.py': 'e2c2bf056551ff53410222224c10cb7b',
 'palomas_orrery.py': 'a22003eadeea738218b25b6617442d5e',
 'planet_visualization.py': '8088a87174dad4c0f31013bc288fd5ff',
 'planet_visualization_utilities.py': '8aaaf0c21543ef847693befdcd193d58',
 'shell_configs.py': '5a456c12f14cf19f2a6f09d34c5ac0af',
 'solar_visualization_shells.py': 'ffcbc60fa98af2998b0bc0a04f09b6f3',
 'test_constants_provenance.py': 'c1cdf6bc258a98eb92e7f8223cae51e8'}

EDITS = [
 ('comet_visualization_shells.py',
  'ghost-tail shadow constant computed',
  '        "inbound through Streamer Belt (6 R_sun, 0.028 AU),<br>"',
  '        f"inbound through the streamer band, past its helmet cusp<br>"\n'
  '        f"({HELMET_CUSP_RADII} R_sun, {HELMET_CUSP_RADII * SOLAR_RADIUS_AU:.3f} AU),<br>"'),('constants_new.py',
  'constant renamed and revalued',
  '# New shells (added April 2026)\n'
  'STREAMER_BELT_RADII = 6.0\n'
  "# ASSUMPTION -- NO VERIFIED SOURCE (Tony's ruling, 2026-08-20, L-210).\n"
  '# Note: 6.0 R_sun is a VISUALIZATION BOUNDARY carried as a working\n'
  '#   assumption, not a sourced value. It is not a physical edge:\n'
  '#   streamer-belt structure continues beyond whatever radius is\n'
  '#   drawn. The value is unchanged from what this row has always\n'
  '#   rendered; what changed is that the file now says we cannot show\n'
  '#   where it came from. Retire this note by citing a work that\n'
  '#   states a helmet-streamer radial extent, with a locatable\n'
  '#   position in the text -- then the value follows the source\n'
  '#   rather than the source being fitted to the value.\n',
  '# New shells (added April 2026); renamed and resourced 2026-08-22 '
  '(L-224)\n'
  'HELMET_CUSP_RADII = 4.0\n'
  '# Source: Suess & Nerney (2004), Adv. Space Res. 33:668-675, bibcode\n'
  '#   2004AdSpR..33..668S -- "the closed field regions, or helmets, '
  'reach\n'
  '#   no higher than 2-4 solar radii". 4.0 is the TOP of that stated\n'
  '#   range, chosen so the drawn cusp does not understate the helmet.\n'
  '# Note: this is the CUSP -- where the closed loops open -- not an '
  'outer\n'
  '#   edge of the streamer belt. The belt has no outer edge: above the\n'
  '#   cusp an open stalk continues into the slow solar wind. The '
  'renderer\n'
  '#   draws the transition and dissolves the stalk rather than stopping\n'
  '#   it (L-224, solar_visualization_shells.create_sun_streamer_band).\n'
  "# Note: the source STATES 2-4 as established background; the paper's "
  'own\n'
  '#   result is an analytic stagnation-flow model. Correctly cited, but '
  'do\n'
  "#   not read 2-4 as this paper's measurement. Modelled, so the "
  'rendered\n'
  '#   pinch is drawn soft rather than sharp.\n'
  '# Corrected: 2026-08-22 -- was STREAMER_BELT_RADII = 6.0, an unsourced\n'
  '#   visualization assumption sitting above the helmet and inside the\n'
  '#   stalk, representing neither (L-210). The rename is the substance:\n'
  '#   a constant named for the belt while holding the helmet cusp is the\n'
  '#   name-meaning drift that produced the citation failure it replaces.\n'
  '# Record: '
  'documentation/SOURCE_suess_nerney_2004_helmet_extent_20260821.md\n'),
 ('constants_new.py',
  'L-210 review-note header',
  "# Review-note: this row's entire citation stack was removed on\n"
  '#   2026-08-20 after an independent nine-source read.',
  "# Review-note: this row's entire citation stack was removed on\n"
  '#   2026-08-20 after an independent nine-source read, when it was\n'
  '#   STREAMER_BELT_RADII = 6.0. Kept because the removals still stand\n'
  '#   and the reasoning is why this row is now cited to a different work\n'
  '#   for a different quantity.'),
 ('constants_new.py',
  'L-210 Resolved line',
  'constants_new.py::STREAMER_BELT_RADII -- value held, unsupported '
  'citation removed, 4-6 R_sun range withdrawn (L-210)',
  'constants_new.py::HELMET_CUSP_RADII (as STREAMER_BELT_RADII) -- value '
  'held, unsupported citation removed, 4-6 R_sun range withdrawn (L-210); '
  'renamed and resourced 2026-08-22 (L-224)'),
 ('constants_new.py',
  'L-209 rehoming cross-ref',
  '# Also+: Rehomed here 2026-08-21 from STREAMER_BELT_RADII, where it had '
  'been',
  '# Also+: Rehomed here 2026-08-21 from HELMET_CUSP_RADII (then named\n'
  '# Also+: STREAMER_BELT_RADII), where it had been'),
 ('planet_visualization_utilities.py',
  'import rename',
  '    STREAMER_BELT_RADII, ROCHE_LIMIT_RADII, ALFVEN_SURFACE_RADII,',
  '    HELMET_CUSP_RADII, ROCHE_LIMIT_RADII, ALFVEN_SURFACE_RADII,'),
 ('planet_visualization.py',
  'import rename',
  '    STREAMER_BELT_RADII, ROCHE_LIMIT_RADII, ALFVEN_SURFACE_RADII,',
  '    HELMET_CUSP_RADII, ROCHE_LIMIT_RADII, ALFVEN_SURFACE_RADII,'),
 ('planet_visualization.py',
  'drop dead-function import',
  '                                        '
  'create_sun_streamer_belt_shell,\n',
  ''),
 ('test_constants_provenance.py',
  'test import rename',
  '    STREAMER_BELT_RADII,\n',
  '    HELMET_CUSP_RADII,\n'),
 ('test_constants_provenance.py',
  'ordering assertions',
  '    assert CHROMOSPHERE_PHYSICAL_RADII < INNER_CORONA_RADII < '
  'ROCHE_LIMIT_RADII < STREAMER_BELT_RADII, \\\n'
  '        "Solar atmosphere shell ordering violated (chromo -> inner '
  'corona -> roche -> streamer)"\n'
  '    assert STREAMER_BELT_RADII < ALFVEN_SURFACE_RADII < '
  'OUTER_CORONA_RADII, \\\n'
  '        "Solar atmosphere shell ordering violated (streamer -> alfven '
  '-> outer corona)"',
  '    assert CHROMOSPHERE_PHYSICAL_RADII < INNER_CORONA_RADII < '
  'ROCHE_LIMIT_RADII < HELMET_CUSP_RADII, \\\n'
  '        "Solar atmosphere shell ordering violated (chromo -> inner '
  'corona -> roche -> helmet cusp)"\n'
  '    assert HELMET_CUSP_RADII < ALFVEN_SURFACE_RADII < '
  'OUTER_CORONA_RADII, \\\n'
  '        "Solar atmosphere shell ordering violated (helmet cusp -> '
  'alfven -> outer corona)"'),
 ('palomas_orrery.py',
  'checkbox label',
  '    text="-- Streamer Belt (Visible Corona)", '
  'variable=sun_streamer_belt_var)',
  '    text="-- Streamer Belt", variable=sun_streamer_belt_var)'),
 ('comet_visualization_shells.py',
  'comet import rename',
  '    ALFVEN_SURFACE_RADII, STREAMER_BELT_RADII)',
  '    ALFVEN_SURFACE_RADII, HELMET_CUSP_RADII)'),
 ('comet_visualization_shells.py',
  'comet layer line',
  '        f"Layer: between Alfven Surface (~{ALFVEN_SURFACE_RADII} R_sun, '
  '"\n'
  '        f"~{ALFVEN_SURFACE_RADII * SOLAR_RADIUS_AU:.3f} AU) and '
  'Streamer Belt "\n'
  '        f"(~{STREAMER_BELT_RADII} R_sun, ~{STREAMER_BELT_RADII * '
  'SOLAR_RADIUS_AU:.3f} AU)<br>"',
  '        f"Layer: between the Alfven Surface (~{ALFVEN_SURFACE_RADII} '
  'R_sun, "\n'
  '        f"~{ALFVEN_SURFACE_RADII * SOLAR_RADIUS_AU:.3f} AU) and the '
  'helmet cusp "\n'
  '        f"(~{HELMET_CUSP_RADII} R_sun, ~{HELMET_CUSP_RADII * '
  'SOLAR_RADIUS_AU:.3f} AU)<br>"'),
 ('comet_visualization_shells.py',
  'comet helmet status computed, not typed',
  '        f"Inside Streamer Belt (~6.0 R_sun, ~0.028 AU): NO -- died '
  'before reaching it<br>"',
  '        # L-224: was a typed "~6.0 R_sun, ~0.028 AU" plus a typed '
  'verdict,\n'
  '        # both of which would have gone stale silently when the '
  'constant\n'
  '        # moved. Computed from the constant now. No Shadow Constants.\n'
  '        f"Inside the helmet cusp (~{HELMET_CUSP_RADII} R_sun, "\n'
  '        f"~{HELMET_CUSP_RADII * SOLAR_RADIUS_AU:.3f} AU): '
  '{helmet_status}<br>"'),
 ('comet_visualization_shells.py',
  'comet helmet status computation',
  '    # Roche status -- disintegration was OUTSIDE the Roche limit\n'
  '    inside_roche = r_km < ROCHE_KM',
  '    # L-224: helmet-cusp status, computed the same way as roche_status\n'
  '    # below rather than typed. NOTE: the disintegration radius this is\n'
  "    # evaluated against is itself under review (L-225) -- the repo's\n"
  '    # 8.33 R_sun does not agree with a perihelion of 1.23 R_sun. This\n'
  '    # line will report correctly for whatever position is passed; it '
  'is\n'
  '    # the INPUT that is in question, not the comparison.\n'
  '    HELMET_CUSP_KM = HELMET_CUSP_RADII * SUN_RADIUS_KM\n'
  '    inside_helmet = r_km < HELMET_CUSP_KM\n'
  '    helmet_status = (\n'
  '        f"YES -- {HELMET_CUSP_KM - r_km:,.0f} km inside"\n'
  '        if inside_helmet else\n'
  '        f"NO -- {r_km - HELMET_CUSP_KM:,.0f} km outside"\n'
  '    )\n'
  '\n'
  '    # Roche status -- disintegration was OUTSIDE the Roche limit\n'
  '    inside_roche = r_km < ROCHE_KM'),
 ('solar_visualization_shells.py',
  'shells import rename',
  '                                            INNER_CORONA_RADII, '
  'OUTER_CORONA_RADII, STREAMER_BELT_RADII,',
  '                                            INNER_CORONA_RADII, '
  'OUTER_CORONA_RADII, HELMET_CUSP_RADII,'),
 ('solar_visualization_shells.py',
  'termination-shock source line',
  '# Source+: TERMINATION_SHOCK_AU=94, STREAMER_BELT_RADII=6 in '
  'constants_new.py',
  '# Source+: TERMINATION_SHOCK_AU=94 in constants_new.py'),
 ('solar_visualization_shells.py',
  'builder uses the renamed constant',
  '    cusp_rs = float(STREAMER_BELT_RADII)   # patch 2: -> '
  'HELMET_CUSP_RADII = 4.0',
  '    cusp_rs = float(HELMET_CUSP_RADII)     # the cusp, not an outer '
  'edge'),
 ('solar_visualization_shells.py',
  'builder header comment',
  '# Source: constants_new.py HELMET_CUSP_RADII (STREAMER_BELT_RADII '
  'until\n'
  '# patch 2) -- the cusp, not an outer edge.',
  '# Source: constants_new.py HELMET_CUSP_RADII -- the cusp, not an edge.'),
 ('solar_visualization_shells.py',
  'builder wiring note now true',
  "# Wired via CUSTOM_SHELLS['Sun']['streamer_belt'] in patch 2. Until "
  'then\n'
  '# nothing calls this and the render is unchanged.',
  "# Wired via CUSTOM_SHELLS['Sun']['streamer_belt']. This is the live "
  'path.'),
 ('solar_visualization_shells.py',
  'tooltip source header',
  '# Source: constants_new.py STREAMER_BELT_RADII=6.0 -- a VISUALIZATION\n'
  '#   ASSUMPTION with no verified source (L-210). Ranges quoted below:\n'
  '#   Suess & Nerney 2004, Adv. Space Res. 33:668 (helmets below 2-4\n'
  '#   R_sun; streamers to many R_sun); Suess & Nerney 2005, Solar Wind\n'
  '#   11 / SOHO 16 (boundaries and stalks studied 2-10 R_sun);\n'
  '#   Decraemer et al. 2019, ApJ 883:152 (stalk as a plasma slab around\n'
  '#   a current sheet). See documentation/worksheets/\n'
  '#   worksheet_gemini-3-1-pro_streamer_extent_20260820.md\n'
  'streamer_belt_info = (',
  '# Source: constants_new.py HELMET_CUSP_RADII=4.0 -- Suess & Nerney '
  '2004,\n'
  '#   Adv. Space Res. 33:668-675, helmets reach no higher than 2-4 '
  'R_sun.\n'
  '#   Further ranges quoted below: Suess & Nerney 2005, Solar Wind 11 /\n'
  '#   SOHO 16 (boundaries and stalks studied 2-10 R_sun); Decraemer et '
  'al.\n'
  '#   2019, ApJ 883:152 (stalk as a plasma slab around a current sheet).\n'
  '#   See documentation/worksheets/\n'
  '#   worksheet_gemini-3-1-pro_streamer_extent_20260820.md and\n'
  '#   documentation/SOURCE_suess_nerney_2004_helmet_extent_20260821.md\n'
  '# L-191 note: this string reaches a Tk tooltip and carries literal '
  '<br>.\n'
  '#   Left as-is deliberately -- it is one of 58 such strings and the '
  'sweep\n'
  "#   is L-191's, not this item's. Fixing one out of step would hide it.\n"
  'streamer_belt_info = ('),
 ('solar_visualization_shells.py',
  'tooltip body -- the band, not a sphere',
  '    "IT HAS NO SINGLE OUTER RADIUS, and this shell is drawn at one '
  'anyway.<br>"\n'
  '    "A streamer is two structures stacked. The HELMET, a dome of '
  'closed<br>"\n'
  '    "magnetic loops, reaches no higher than 2-4 R_sun. Above its cusp '
  'the<br>"\n'
  '    "field opens and the solar wind draws it out into a STALK -- a '
  'thin<br>"\n'
  '    "current sheet reaching many solar radii, studied between 2 and '
  '10.<br>"\n'
  '    "This shell sits at 6.0 R_sun: above the helmet, inside the stalk, '
  'and<br>"\n'
  '    "not a boundary anybody has measured. It is a drawing choice.<br>"\n'
  '    "(Suess & Nerney 2004, Adv. Space Res. 33:668; 2005, Solar Wind '
  '11.)<br><br>"',
  '    "IT HAS NO SINGLE OUTER RADIUS, and since 2026-08-22 it is no '
  'longer<br>"\n'
  '    "drawn as if it did. A streamer is two structures stacked. The '
  'HELMET,<br>"\n'
  '    "a dome of closed magnetic loops, reaches no higher than 2-4 '
  'R_sun.<br>"\n'
  '    "Above its cusp the field opens and the solar wind draws it out '
  'into a<br>"\n'
  '    "STALK -- a thin current sheet reaching many solar radii, '
  'studied<br>"\n'
  '    "between 2 and 10. The band drawn here is ONE object with both: '
  'wide<br>"\n'
  '    "and dense at the base, pinching at the cusp at 4.0 R_sun where '
  'the<br>"\n'
  '    "loops open, then thinning and dissolving across the Alfven '
  'surface.<br>"\n'
  '    "It has no drawn outer edge, because there is no edge to '
  'draw.<br>"\n'
  '    "(Suess & Nerney 2004, Adv. Space Res. 33:668; 2005, Solar Wind '
  '11.)<br><br>"'),
 ('solar_visualization_shells.py',
  'delete streamer_belt_info_hover',
  'streamer_belt_info_hover = (\n'
  '    "Sun: Streamer Belt / Visible Corona:<br><br>"\n'
  '\n'
  '    "The brightest, most structured region of the visible solar corona. '
  'It has<br>"\n'
  '    "NO single outer radius: the closed helmet stays below 2-4 R_sun '
  'and its<br>"\n'
  '    "open stalk reaches many R_sun (Suess & Nerney 2004). This shell is '
  'drawn<br>"\n'
  '    "at 6.0 R_sun -- above the first, inside the second, and a drawing '
  'choice<br>"\n'
  '    "rather than a measured boundary. The eclipse edge divides two '
  'flow<br>"\n'
  '    "regimes, not plasma from vacuum. This is the corona that<br>"\n'
  '    "observers see during total solar eclipses as a pearly white halo '
  'around the Sun.<br><br>"\n'
  '\n'
  '    "Three components of white-light corona:<br>"\n'
  '    "* K-corona (kontinuierlich): Sunlight scattered off free '
  'electrons. Dominates within 2-3 R_sun.<br>"\n'
  '    "  Spectrum is continuous -- electrons move too fast to preserve '
  'absorption lines.<br>"\n'
  '    "* F-corona (Fraunhofer): Sunlight scattered off dust. Shows '
  'Fraunhofer absorption lines.<br>"\n'
  '    "  Dominates beyond ~3 R_sun, extends to ~15 R_sun. Has an oval '
  'shape.<br>"\n'
  '    "* E-corona (emission): Line emission from ionized Fe, Ni, Ca. '
  'Visible to ~2 R_sun.<br><br>"\n'
  '\n'
  '    "* Helmet streamers: closed loops below 2-4 R_sun, then a stalk '
  'reaching<br>"\n'
  '    "  many R_sun. Source of slow solar wind.<br>"\n'
  '    "* Temperature: ~1-2 million K<br><br>"\n'
  '    "MAPS C/2026 A1 context:<br>"\n'
  '    "MAPS was detected in SOHO/LASCO C3 (~33 R_sun field) from April 2, '
  '2026.<br>"\n'
  '    "It passed through this visible streamer belt on April 3-4 before '
  'perihelion."\n'
  ')\n'
  '\n',
  '# streamer_belt_info_hover was DELETED 2026-08-22 (L-224). It fed only\n'
  '# create_sun_streamer_belt_shell, which was dead code; the live band\n'
  '# builder composes its own hover from the constants. Deleted rather '
  'than\n'
  '# annotated: it demonstrates the sphere pattern this item exists to\n'
  '# retire, and a worked example of the wrong shape one screen from the\n'
  '# right one is a trap, not a reference.\n'
  '\n'),
 ('solar_visualization_shells.py',
  'delete the dead sphere function',
  'def create_sun_streamer_belt_shell():\n'
  '    """\n'
  '    Visible white-light corona / helmet streamer belt, drawn at 6.0 '
  'R_sun.\n'
  '    That radius is a VISUALIZATION ASSUMPTION, not a measured boundary\n'
  '    (L-210). The structure has two parts and no single outer radius: '
  'the\n'
  '    closed helmet stays below 2-4 R_sun and its open stalk reaches '
  'many\n'
  '    R_sun (Suess & Nerney 2004, Adv. Space Res. 33:668). 6.0 sits '
  'above\n'
  '    the first and inside the second.\n'
  '    This is the corona seen during total solar eclipses. Distinct from '
  'the\n'
  '    Alfven surface (plasma boundary) and the extended F-corona '
  '(dust-scattered).\n'
  '    """\n'
  '    x, y, z = create_sphere_points(STREAMER_BELT_RADII * '
  'SOLAR_RADIUS_AU, n_points=20)\n'
  '    r_info = STREAMER_BELT_RADII * SOLAR_RADIUS_AU * 1.05\n'
  '\n'
  '    shell_trace = go.Scatter3d(\n'
  '        x=x, y=y, z=z,\n'
  "        mode='markers',\n"
  "        marker=dict(size=3.0, color='rgb(255, 200, 80)', "
  'opacity=0.45),\n'
  "        name='Sun: Streamer Belt (Visible Corona)',\n"
  "        legendgroup='Sun: Streamer Belt (Visible Corona)',\n"
  "        hoverinfo='skip',\n"
  '        showlegend=True\n'
  '    )\n'
  '    # Phase 1 re-pipe (May 28, 2026): factory-routed.\n'
  '    info_trace = create_info_marker(\n'
  '        0, 0, r_info,\n'
  "        'rgb(255, 200, 80)',\n"
  '        f"Sun: Streamer Belt (Visible '
  'Corona)<br><br>{streamer_belt_info_hover}",\n'
  "        'Sun: Streamer Belt (Visible Corona)'\n"
  '    )\n'
  '    return [shell_trace, info_trace]\n',
  '# create_sun_streamer_belt_shell was DELETED 2026-08-22 (L-224). It '
  'was\n'
  '# defined here, imported once by planet_visualization.py, and never\n'
  "# called: the sphere it drew came from SHELL_CONFIGS['Sun']\n"
  "# ['streamer_belt'] via build_sphere_shell. Its replacement is\n"
  '# create_sun_streamer_band below, wired through CUSTOM_SHELLS.\n'),
 ('shell_configs.py',
  'registry import rename',
  '    STREAMER_BELT_RADII, ROCHE_LIMIT_RADII, ALFVEN_SURFACE_RADII,',
  '    ROCHE_LIMIT_RADII, ALFVEN_SURFACE_RADII,'),
 ('shell_configs.py',
  'drop the dead hover-string import',
  '    inner_corona_info_hover, streamer_belt_info_hover,\n',
  '    inner_corona_info_hover,\n'),
 ('shell_configs.py',
  'remove the sphere entry from SHELL_CONFIGS',
  "        'streamer_belt': {\n"
  "            'name': 'Streamer Belt (Visible Corona)',\n"
  "            'radius_au': STREAMER_BELT_RADII * SOLAR_RADIUS_AU,\n"
  "            'color': 'rgb(255, 200, 80)',\n"
  "            'opacity': 0.45,\n"
  "            'n_points': 20,\n"
  "            'marker_size': 3.0,\n"
  "            'hover_text': streamer_belt_info_hover,\n"
  "            'tooltip': streamer_belt_info,\n"
  '        },\n'
  '\n',
  "        # 'streamer_belt' MOVED to CUSTOM_SHELLS['Sun'] on 2026-08-22\n"
  '        # (L-224). It is no longer a sphere: helmet streamers form '
  'only\n'
  '        # over the magnetic neutral line, so a full sphere asserted '
  'them\n'
  '        # over the poles, where coronal holes are instead. Its radius '
  'was\n'
  '        # also a drawing choice with nothing under it (L-210). It is '
  'now\n'
  '        # a warped band pinching at the helmet cusp and dissolving '
  'across\n'
  '        # the Alfven surface. Do not re-add a sphere entry here.\n'
  '\n'),
 ('shell_configs.py',
  "add the band to CUSTOM_SHELLS['Sun']",
  "    'Sun': {\n"
  '\n'
  "        'rotation_axis': {\n"
  "            'per_frame': True,  # 21/51 Phase 3: engine-animatable "
  'primitive\n'
  "            'builder': "
  "'planet_visualization_utilities.build_rotation_axis_traces',",
  "    'Sun': {\n"
  '\n'
  "        'streamer_belt': {\n"
  "            'builder': "
  "'solar_visualization_shells.create_sun_streamer_band',\n"
  "            'tooltip': streamer_belt_info,\n"
  '        },\n'
  '\n'
  "        'rotation_axis': {\n"
  "            'per_frame': True,  # 21/51 Phase 3: engine-animatable "
  'primitive\n'
  "            'builder': "
  "'planet_visualization_utilities.build_rotation_axis_traces',")]


def main():
    originals = {}
    for path in FP:
        if not os.path.exists(path):
            print("ERROR: %s not found. Run this from the repo root." % path)
            sys.exit(1)
        with open(path, "rb") as f:
            originals[path] = f.read()
        got = hashlib.md5(originals[path].replace(b"\r\n", b"\n")).hexdigest()
        if got != FP[path]:
            print("ERROR: BASE MOVED on %s" % path)
            print("  expected %s" % FP[path])
            print("  found    %s" % got)
            print("  Nothing was written to any file.")
            sys.exit(1)
    print("base ok: %d files fingerprinted" % len(FP))

    for path, label, old, new in EDITS:
        bad = [c for c in new if ord(c) > 127]
        if bad:
            print("ERROR: edit '%s' would insert %d non-ASCII char(s)."
                  % (label, len(bad)))
            sys.exit(1)
    print("note: all inserted text is ASCII")

    results = dict(originals)
    for path, label, old, new in EDITS:
        data = results[path]
        crlf = b"\r\n" in data
        o = old.encode("ascii"); n = new.encode("ascii")
        if crlf:
            o = o.replace(b"\n", b"\r\n"); n = n.replace(b"\n", b"\r\n")
        c = data.count(o)
        if c != 1:
            print("ANCHOR FAIL in %s -- '%s': expected 1 match, found %d."
                  % (path, label, c))
            print("  Nothing was written to any file.")
            sys.exit(1)
        results[path] = data.replace(o, n)
        print("ok   %-34s %s" % (path, label))

    for path, data in results.items():
        if data != originals[path]:
            with open(path, "wb") as f:
                f.write(data)
            print("wrote %s (%d bytes, was %d)"
                  % (path, len(data), len(originals[path])))

    print("")
    print("verification, read back from disk:")
    fails = [0]

    def ck(desc, ok):
        if not ok:
            fails[0] += 1
        print("  %s  %s" % ("PASS" if ok else "FAIL", desc))

    def rd(p):
        with open(p, "rb") as f:
            return f.read().replace(b"\r\n", b"\n")

    c = rd("constants_new.py"); g = rd("shell_configs.py")
    s = rd("solar_visualization_shells.py"); m = rd("comet_visualization_shells.py")

    ck("constant renamed and revalued",
       b"\nHELMET_CUSP_RADII = 4.0\n" in c)
    ck("old constant name gone from constants_new.py definitions",
       b"\nSTREAMER_BELT_RADII = " not in c)
    ck("constant now carries a Source leg",
       b"# Source: Suess & Nerney (2004), Adv. Space Res. 33:668-675" in c)
    ck("no live code still imports the old name",
       all(b"STREAMER_BELT_RADII" not in rd(p) for p in
           ("shell_configs.py", "comet_visualization_shells.py",
            "planet_visualization_utilities.py", "planet_visualization.py",
            "solar_visualization_shells.py", "test_constants_provenance.py")))
    ck("band wired into CUSTOM_SHELLS",
       b"'builder': 'solar_visualization_shells.create_sun_streamer_band'" in g)
    ck("sphere entry gone from SHELL_CONFIGS",
       b"'name': 'Streamer Belt (Visible Corona)'," not in g)
    ck("dead sphere function deleted",
       b"def create_sun_streamer_belt_shell():" not in s)
    ck("its hover string deleted with it",
       b"streamer_belt_info_hover = (" not in s)
    ck("no dangling reference to either",
       b"create_sun_streamer_belt_shell," not in rd("planet_visualization.py")
       and b"streamer_belt_info_hover" not in g)
    ck("tooltip survives -- checkbox and CUSTOM_SHELLS both use it",
       b"streamer_belt_info = (" in s
       and b"'tooltip': streamer_belt_info," in g)
    ck("both comet shadow constants gone from DISPLAYED strings",
       not any(b"0.028 AU" in ln for ln in m.split(b"\n")
               if b'f"' in ln or b'"inbound' in ln))
    ck("comet status is computed",
       b"helmet_status = (" in m)

    import py_compile
    for p in FP:
        try:
            py_compile.compile(p, doraise=True)
        except Exception as exc:
            ck("%s compiles" % p, False)
            print("       %s" % exc)
        else:
            ck("%s compiles" % p, True)

    if fails[0]:
        print("")
        print("ERROR: %d check(s) failed AFTER writing. Revert all eight "
              "files in GitHub Desktop and report this." % fails[0])
        sys.exit(1)

    print("")
    print("The render HAS changed. Run the orrery, tick '-- Streamer Belt',")
    print("and judge it. Mode 5 is yours -- especially the fade profile,")
    print("which is a parameter in STREAMER_BAND_DEFAULTS, not a rewrite.")


if __name__ == "__main__":
    main()
