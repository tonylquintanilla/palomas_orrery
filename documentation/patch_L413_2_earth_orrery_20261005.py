#!/usr/bin/env python3
"""
patch_L413_2_earth_orrery_20261005.py -- ORRERY repo. Earth's list
(L-413), the orrery patch: the geocorona shell, Earth's tilt in words,
the atmosphere and LEO notes, and the inner belt's words.

Built on orrery 72e3b55805c29f1f08a583864bd815a47e7434c6
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 624aa94557e16956b2fe022a467936ae2ccf3406 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io was read,
not changed; the website's half is a separate gallery patch, built
after this one is pushed).

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code and click Run. The same as:
        python patch_L413_2_earth_orrery_20261005.py
    Then follow the numbered NEXT steps it prints. Move it into
    documentation/ BEFORE the maintenance run, as step 1 says.

WHAT A VISITOR OF THE ORRERY SEES AFTER IT
    Under Earth, a new checkbox "-- Exosphere (Geocorona)" draws a faint
    shell at 100 Earth radii, in the website's colour and faintness. Its
    hover and its tooltip read, in the words you approved on 2026-10-05:
        Exosphere / Geocorona: a faint halo of hydrogen gas around Earth,
        the outermost trace of the atmosphere. The exosphere has no top;
        it simply thins into space. Its hydrogen glows faintly in
        ultraviolet light, a halo called the geocorona. The shell is drawn
        at 100 Earth radii, about 600,000 km (0.004 AU), where that glow
        has been detected. That is not where the atmosphere ends, and it
        reaches beyond the Moon's orbit. Zoom out past the Moon to see it.
        Source: Baliukin et al. (2019), J. Geophys. Res. Space Physics
        124:861.
    The Upper Atmosphere checkbox tooltip shows the same words as that
    shell's hover (it gave a different top for the layer; the shell is
    drawn to the 600 km thermopause).
    The two coordinate hovers say "Teal circle: Celestial equator, tilted
    from the ecliptic by Earth's axial tilt (Earth's rotation-axis hover
    gives the angle for this date)"; the Celestial Sphere tooltip says
    "tilted by Earth's axial tilt"; the coordinate guide says "Earth's
    equator is tilted relative to it by Earth's axial tilt, which causes
    the seasons". None types the angle any more (L-369).
    The inner belt's hover says "the brighter ring is near the measured
    proton flux peak, 1.5 Earth radii from Earth's centre"; the
    magnetosphere checkbox's tooltip says "drawn near their measured flux
    peak" (L-349).
    Nothing else on screen changes. Every Earth shell hover other than
    the new one was compared before and after, and is identical.

WHAT CHANGES
    earth_visualization_shells.py   earth_geocorona_info (new); the upper
        atmosphere's tooltip text; the inner belt's words.
    shell_configs.py    SHELL_CONFIGS['Earth']['geocorona'] (new); the
        upper atmosphere reads its words from the module string; the
        inner belt line of the magnetosphere tooltip.
    palomas_orrery.py   the checkbox, its variable, its place in
        earth_shell_vars (so Reset clears it), its import; three strings.
    star_sphere_builder.py   reads EARTH_OBLIQUITY_J2000_DEG from
        constants_new.py where it typed its own shorter copy. The saved
        star file does not need rebuilding: the two differ by about a
        hundred-thousandth of a degree.
    coordinate_system_guide.py   one table cell.
    constants_new.py    notes only, no value: the atmosphere tops and the
        LEO edges say why each is the equatorial radius plus its altitude
        (your reading of 2026-10-05, L-389); the frame note no longer
        reads a consequence of the 2026-09-28 crust ruling as the ruling;
        the LEO outer edge's stale note is corrected; the geocorona row
        says the orrery now draws it.
    Each file gets its credit line.

TESTED in a sandbox on a throwaway copy of 72e3b55: every file compiles;
the orrery opens headless and draws the new shell on the live path with
its checkbox and tooltip; orrery_maintenance_run.py passed 20 of 20
gating checkers, Reset completeness included; data/constants_export.json
changed only in its fingerprint, no value; the provenance scanner's
Tier-1 findings were the same 296, compared file by file.

LINE ENDINGS (safe-file-editing 1.12): every file is written LF. A file
that arrived CRLF in your working copy is named in a "note:" line. All
six are committed LF, so none is the exception.

PERMANENT, though this script is thrown away: the shell, the checkbox,
the words, the notes.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 5, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

REPO = "orrery"
ROOT_MARKERS = ("palomas_orrery.py", "LEDGER_CONSOLIDATED.md")
BUILT_ON = "72e3b55"
NEXT = ["1. Move this script into documentation/ FIRST. While it sits in",
        "   the root folder the provenance scanner counts it as findings.",
        "2. Run orrery_maintenance_run.py (VS Code, Run). Expect every",
        "   gating checker to pass and the scanner to read 296. The",
        "   Constants export step rewrites data/constants_export.json:",
        "   its fingerprint moves because of the notes; no value moves.",
        "3. Open the orrery and look (Mode 5): Earth with Exosphere",
        "   (Geocorona) ticked, zoomed out past the Moon; its hover; the",
        "   Upper Atmosphere tooltip; the coordinate hover's teal line;",
        "   the inner belt's hover (tick Magnetosphere).",
        "4. Commit and push.",
        "5. Then the gallery patch, which Claude builds after the push."]

BASE = {
    'constants_new.py': 'fbc605315425f9747ed2e1bb353060d3',
    'coordinate_system_guide.py': '434af6a5a9a3025ba7bd8a6450203c7e',
    'earth_visualization_shells.py': 'a861aa0e48d519fea52c3b68c5a9cec3',
    'palomas_orrery.py': '0c4a4582ed731d75f2e0df9c3335dc94',
    'shell_configs.py': 'e980a1215146e48798bf61512a916290',
    'star_sphere_builder.py': '585113c745ea21803e10aec96301ed8a',
}

EDITS = {
  'constants_new.py': [
    ('frame note: what Tony ruled on 2026-09-28',
      ('# therefore draws each boundary at its correct ABSOLUTE radius. Since\n'
      "# patch D20 (L-345, Tony's ruling of 2026-09-28) the crust is drawn at\n"
      '# the mean radius as well, EARTH_MEAN_RADIUS_KM over the equatorial\n'
      "# radius, so a boundary's depth below the DRAWN surface is its textbook\n"
      '# depth. Until then'),
      ('# therefore draws each boundary at its correct ABSOLUTE radius. Since\n'
      "# patch D20 (L-345, Tony's ruling of 2026-09-28) the crust is drawn at\n"
      '# the mean radius, EARTH_MEAN_RADIUS_KM over the equatorial radius,\n'
      '# because Earth is drawn as a sphere and a sphere at the mean radius\n'
      '# stays nearest sea level everywhere. The equatorial radius stays the\n'
      '# standard Earth radius. One consequence follows, and it is not a rule\n'
      "# of Tony's: an interior boundary's depth below the drawn crust is now\n"
      '# its textbook depth. Heights above the crust are NOT mirrored. The\n'
      '# atmosphere tops and the low Earth orbit edges are the equatorial\n'
      '# radius plus their altitude, so each sits further above the drawn\n'
      '# crust than its altitude, by the difference between the two radii.\n'
      '# That is the cost of drawing Earth as a sphere, not an error (Tony,\n'
      '# 2026-10-05, L-389; this note had read the consequence as the ruling\n'
      '# and was corrected the same day). Until then'),
      1),
    ('LEO inner edge: why the equatorial radius',
      ('# Figures: 8 -- set by EARTH_EQUATORIAL_RADIUS_KM\n'
      'EARTH_LEO_OUTER_KM ='),
      ('# Figures: 8 -- set by EARTH_EQUATORIAL_RADIUS_KM\n'
      '# Note: the altitude is added to the EQUATORIAL radius, the standard\n'
      '# Note+: Earth radius, on purpose (Tony, 2026-10-05, L-389). The crust is\n'
      '# Note+: drawn at the mean radius only because Earth is drawn as a\n'
      '# Note+: sphere, so this edge sits further above the drawn crust than\n'
      '# Note+: its altitude, by the difference between the two radii. See the\n'
      '# Note+: frame note above the interior boundaries.\n'
      'EARTH_LEO_OUTER_KM ='),
      1),
    ('LEO outer edge: stale note replaced',
      ("# Note: the orrery's LEO shell types 6571 and 8371 km, which is 6371 + the\n"
      '# Note+: altitude -- the mean radius, not the equatorial one the shell is\n'
      '# Note+: drawn against. Seven km, below the drawn resolution, but the\n'
      '# Note+: hover text quotes those numbers. Follow-on with the migration.\n'),
      ('# Note: the altitude is added to the EQUATORIAL radius, as on the row\n'
      '# Note+: above (Tony, 2026-10-05, L-389). Corrected in passing the same\n'
      "# Note+: day: this note said the LEO shell's hover typed its distances\n"
      '# Note+: from the mean radius; the hover has read this row since L-291.\n'),
      1),
    ('stratopause: why the equatorial radius',
      "# Note: the top of the lower atmosphere, measured from Earth's centre.\n",
      ("# Note: the top of the lower atmosphere, measured from Earth's centre.\n"
      '# Note+: The altitude is added to the EQUATORIAL radius, the standard\n'
      '# Note+: Earth radius, on purpose (Tony, 2026-10-05, L-389). The crust is\n'
      '# Note+: drawn at the mean radius only because Earth is drawn as a\n'
      '# Note+: sphere, so this top sits further above the drawn crust than its\n'
      '# Note+: altitude, by the difference between the two radii. That is the\n'
      "# Note+: sphere's cost, not an error.\n"),
      1),
    ('thermopause: why the equatorial radius',
      "# Note: the top of the upper atmosphere, measured from Earth's centre.\n",
      ("# Note: the top of the upper atmosphere, measured from Earth's centre.\n"
      '# Note+: The altitude is added to the EQUATORIAL radius, as on the\n'
      '# Note+: stratopause row above (Tony, 2026-10-05, L-389).\n'),
      1),
    ('geocorona row: the orrery now draws it',
      ('# Note+: boundary. The shell is drawn at the sourced floor and its hover\n'
      "# Note+: says so. It encloses the Moon's orbit at about 60 radii.\n"),
      ('# Note+: boundary. The shell is drawn at the sourced floor and its hover\n'
      "# Note+: says so. It encloses the Moon's orbit at about 60 radii.\n"
      '# Note+: The orrery draws it as its own shell since 2026-10-05\n'
      "# Note+: (SHELL_CONFIGS['Earth']['geocorona'], L-292), as the website\n"
      '# Note+: has since L-291.\n'),
      1),
    ('docstring credit',
      ('note now say the crust is drawn at the mean radius.)\n'
      '"""'),
      ('note now say the crust is drawn at the mean radius.)\n'
      "Module updated: October 5, 2026 with Anthropic's Claude Opus 5.5\n"
      '(L-389: notes on the two atmosphere tops and the two LEO edges say why\n'
      "each is the equatorial radius plus its altitude, Tony's reading of\n"
      '2026-10-05; the frame note no longer reads a consequence of the\n'
      "2026-09-28 crust ruling as the ruling itself; the LEO outer edge's\n"
      "stale note is corrected. L-292: the geocorona row's note says the\n"
      'orrery now draws it. No value changes.)\n'
      '"""'),
      1),
  ],
  'coordinate_system_guide.py': [
    ('the tilt in words (L-369)',
      "Earth's equator is tilted 23.4\xb0 relative to it (causes seasons)",
      "Earth's equator is tilted relative to it by Earth's axial tilt, which causes the seasons",
      1),
    ('docstring credit',
      ('Role: computation\n'
      'Domain: orrery\n'
      '"""'),
      ("Module updated: October 5, 2026 with Anthropic's Claude Opus 5.5 (L-369:\n"
      "the misconception table says Earth's equator is tilted by Earth's axial\n"
      'tilt, where it typed the angle. Words approved by Tony.)\n'
      '\n'
      'Role: computation\n'
      'Domain: orrery\n'
      '"""'),
      1),
  ],
  'earth_visualization_shells.py': [
    ('imports: the atmosphere rows and row_text',
      ('    EARTH_HILL_SPHERE_KM, EARTH_HILL_SPHERE_RADII,\n'
      ')\n'
      'from orrery_rendering import rotate_to_sunward, create_info_marker\n'
      'import constants_new as _store\n'
      'from constants_rows import figures_of, uncertainty_of, exact_text\n'),
      ('    EARTH_HILL_SPHERE_KM, EARTH_HILL_SPHERE_RADII,\n'
      "    # 2026-10-05: the upper atmosphere's tooltip reads the same rows as\n"
      '    # its hover (it typed a different top for the layer), and the\n'
      '    # geocorona gets a shell.\n'
      '    EARTH_STRATOPAUSE_ALTITUDE_KM, EARTH_THERMOPAUSE_ALTITUDE_KM,\n'
      '    EARTH_GEOCORONA_RADII,\n'
      ')\n'
      'from orrery_rendering import rotate_to_sunward, create_info_marker\n'
      'import constants_new as _store\n'
      'from constants_rows import figures_of, uncertainty_of, exact_text, row_text\n'),
      1),
    ("upper atmosphere tooltip: the hover's words; geocorona info added",
      ('# Source: NOAA, NASA Earth Fact Sheet\n'
      '# Verified: April 2026 via Gemini fact-check\n'
      'earth_upper_atmosphere_info = (\n'
      '            "The upper atmosphere extends from 50 km to about 1,000 km altitude. It includes\\n"\n'
      '            "the mesosphere where meteors burn up, the thermosphere where the aurora occurs and\\n"\n'
      '            "the International Space Station orbits, and the exosphere which gradually transitions\\n"\n'
      '            "to space. In the thermosphere, temperatures can reach 2,000 degC (3,600 degF), though the\\n"\n'
      '            "gas is so thin that it would feel cold to human skin."\n'
      ')\n'
      '\n'),
      ('# Source: NOAA, NASA Earth Fact Sheet\n'
      '# Verified: April 2026 via Gemini fact-check\n'
      "# 2026-10-05: the checkbox tooltip shows the plot hover's words, so the\n"
      '# two cannot disagree again; it had typed a different top for the layer\n'
      '# from the one the shell is drawn to. shell_configs.py now derives the\n'
      "# hover from this string. The altitudes and the geocorona's floor are\n"
      '# read from constants_new.py, where each row carries its own source.\n'
      'earth_upper_atmosphere_info = (\n'
      '            f"The upper atmosphere is drawn from the stratopause ({EARTH_STRATOPAUSE_ALTITUDE_KM:,.0f} km) to the\\n"\n'
      '            f"thermopause, about {EARTH_THERMOPAUSE_ALTITUDE_KM:,.0f} km up (NOAA JetStream; NASA). It includes\\n"\n'
      '            "the mesosphere where meteors burn up and the thermosphere where the aurora occurs and\\n"\n'
      '            "the International Space Station orbits. In the thermosphere, temperatures can reach\\n"\n'
      '            "2,000 degC (3,600 degF), though the gas is so thin that it would feel cold to human skin.\\n"\n'
      '            "Above the thermopause the exosphere thins into space with no boundary; its hydrogen\\n"\n'
      '            f"halo, the geocorona, is detected past {EARTH_GEOCORONA_RADII:.0f} Earth radii."\n'
      ')\n'
      '\n'
      "# L-292 (2026-10-05): Earth's exosphere, drawn as its own shell at the\n"
      "# geocorona's detection floor. Tony approved these words on 2026-10-05;\n"
      '# Source: every figure below is read from EARTH_GEOCORONA_RADII in\n'
      "# Source+: constants_new.py, and the words follow that row's source,\n"
      '# Source+: Baliukin et al. (2019), J. Geophys. Res. Space Physics 124,\n'
      '# Source+: 861-885, doi:10.1029/2018JA026136 -- its title (Lyman-alpha,\n'
      '# Source+: the ultraviolet glow) and abstract (detected to at least 100\n'
      '# Source+: Earth radii, encompassing the orbit of the Moon).\n'
      "# they follow the website's for the same shell. One string for the\n"
      '# checkbox tooltip and the plot hover (shell_configs.py derives <br>).\n'
      'earth_geocorona_info = (\n'
      '            "Exosphere / Geocorona: a faint halo of hydrogen gas around Earth, the outermost\\n"\n'
      '            "trace of the atmosphere. The exosphere has no top; it simply thins into space.\\n"\n'
      '            "Its hydrogen glows faintly in ultraviolet light, a halo called the geocorona.\\n"\n'
      '            f"The shell is drawn at {row_text(\'EARTH_GEOCORONA_RADII\')} Earth radii, "\n'
      '            f"about {row_text(\'EARTH_GEOCORONA_RADII\', \'km\', grouping=True)} km "\n'
      '            f"({row_text(\'EARTH_GEOCORONA_RADII\', \'au\')} AU), where that\\n"\n'
      '            "glow has been detected. That is not where the atmosphere ends, and it reaches\\n"\n'
      '            "beyond the Moon\'s orbit. Zoom out past the Moon to see it.\\n"\n'
      '            "Source: Baliukin et al. (2019), J. Geophys. Res. Space Physics 124:861."\n'
      ')\n'
      '\n'),
      1),
    ('inner belt words (L-349, Tony 2026-10-05)',
      ('        f"ring is the flux peak, {EARTH_VAN_ALLEN_INNER_RADII:g} Earth radii from Earth\'s centre, about<br>"\n'
      '        f"{_km_above_surface(EARTH_VAN_ALLEN_INNER_RADII, 2):,} km above the surface at the equator.<br>"\n'),
      ('        f"ring is near the measured proton flux peak, {EARTH_VAN_ALLEN_INNER_RADII:g} Earth radii from<br>"\n'
      '        f"Earth\'s centre, about {_km_above_surface(EARTH_VAN_ALLEN_INNER_RADII, 2):,} km above the surface at the equator.<br>"\n'),
      1),
    ('docstring credit',
      ('    The text shown does not change.\n'
      "Module updated: September 27, 2026 with Anthropic's Claude Opus 5.5\n"
      '"""'),
      ('    The text shown does not change.\n'
      "Module updated: September 27, 2026 with Anthropic's Claude Opus 5.5\n"
      "October 5, 2026 (L-413's orrery patch, Opus 5.5): earth_geocorona_info,\n"
      "    the words for Earth's new exosphere shell (L-292), printing the\n"
      '    geocorona row at its count in Earth radii, km and AU; the upper\n'
      "    atmosphere's tooltip shows its hover's words, where it typed a\n"
      '    different top for the layer; the inner belt says it is drawn near\n'
      '    the measured proton flux peak (L-349). Words approved by Tony.\n'
      "Module updated: October 5, 2026 with Anthropic's Claude Opus 5.5\n"
      '"""'),
      1),
  ],
  'palomas_orrery.py': [
    ('import the geocorona tooltip',
      ('from constants_new import (\n'
      '    DEFAULT_MARKER_SIZE,\n'),
      ("# L-292 (2026-10-05): the tooltip for Earth's exosphere checkbox.\n"
      'from earth_visualization_shells import earth_geocorona_info\n'
      '\n'
      'from constants_new import (\n'
      '    DEFAULT_MARKER_SIZE,\n'),
      1),
    ('geocorona var',
      'earth_upper_atmosphere_var = tk.IntVar(value=0)\n',
      ('earth_upper_atmosphere_var = tk.IntVar(value=0)\n'
      '# Earth exosphere / geocorona shell (L-292)\n'
      'earth_geocorona_var = tk.IntVar(value=0)\n'),
      1),
    ('geocorona in earth_shell_vars',
      ("    'earth_upper_atmosphere': earth_upper_atmosphere_var,\n"
      "    'earth_leo': earth_leo_var,\n"),
      ("    'earth_upper_atmosphere': earth_upper_atmosphere_var,\n"
      "    'earth_geocorona': earth_geocorona_var,\n"
      "    'earth_leo': earth_leo_var,\n"),
      1),
    ('geocorona checkbox',
      'CreateToolTip(earth_upper_atmosphere_checkbutton, earth_upper_atmosphere_info)\n',
      ('CreateToolTip(earth_upper_atmosphere_checkbutton, earth_upper_atmosphere_info)\n'
      '\n'
      '# Earth exosphere / geocorona shell (L-292, 2026-10-05)\n'
      'earth_geocorona_checkbutton = tk.Checkbutton(earth_shell_options_frame, text="-- Exosphere (Geocorona)", variable=earth_geocorona_var)\n'
      "earth_geocorona_checkbutton.pack(anchor='w')\n"
      'CreateToolTip(earth_geocorona_checkbutton, earth_geocorona_info)\n'),
      1),
    ('two plot hovers: the tilt in words (L-369)',
      '<b>Teal circle:</b> Celestial equator (tilted 23.4&deg;)<br><br>',
      "<b>Teal circle:</b> Celestial equator, tilted from the ecliptic by Earth's axial tilt<br>(Earth's rotation-axis hover gives the angle for this date)<br><br>",
      2),
    ('Celestial Sphere tooltip: the tilt in words (L-369)',
      'the celestial equator (tilted 23.4 deg), and coordinate poles.',
      "the celestial equator (tilted by Earth's axial tilt), and coordinate poles.",
      1),
    ('docstring credit',
      'Hill radius, 134,000 AU, where it printed every digit.)\n',
      ('Hill radius, 134,000 AU, where it printed every digit.)\n'
      "Module updated: October 5, 2026 with Anthropic's Claude Opus 5.5 (L-413's\n"
      'orrery patch: Earth\'s "-- Exosphere (Geocorona)" checkbox (L-292); the\n'
      'two coordinate hovers and the Celestial Sphere tooltip say the celestial\n'
      "equator is tilted by Earth's axial tilt instead of typing it (L-369).\n"
      'Words approved by Tony, 2026-10-05.)\n'),
      1),
  ],
  'shell_configs.py': [
    ('import the two Earth info strings',
      ('from earth_visualization_shells import (\n'
      '    earth_inner_core_info, earth_outer_core_info,\n'
      '    earth_lower_mantle_info, earth_upper_mantle_info,\n'
      ')\n'),
      ('from earth_visualization_shells import (\n'
      '    earth_inner_core_info, earth_outer_core_info,\n'
      '    earth_lower_mantle_info, earth_upper_mantle_info,\n'
      '    # 2026-10-05: one string each for the tooltip and the hover.\n'
      '    earth_upper_atmosphere_info, earth_geocorona_info,\n'
      ')\n'),
      1),
    ('upper atmosphere hover from its info string; geocorona shell added',
      ("            'marker_size': 2.0,\n"
      "            'hover_text': (\n"
      '                f"The upper atmosphere is drawn from the stratopause ({EARTH_STRATOPAUSE_ALTITUDE_KM:,.0f} km) to the<br>"\n'
      '                f"thermopause, about {EARTH_THERMOPAUSE_ALTITUDE_KM:,.0f} km up (NOAA JetStream; NASA). It includes<br>"\n'
      '                "the mesosphere where meteors burn up and the thermosphere where the aurora occurs and<br>"\n'
      '                "the International Space Station orbits. In the thermosphere, temperatures can reach<br>"\n'
      '                "2,000 degC (3,600 degF), though the gas is so thin that it would feel cold to human skin.<br>"\n'
      '                "Above the thermopause the exosphere thins into space with no boundary; its hydrogen<br>"\n'
      '                f"halo, the geocorona, is detected past {EARTH_GEOCORONA_RADII:.0f} Earth radii."\n'
      '            ),\n'
      "            'tooltip': (\n"
      '                f"The upper atmosphere is drawn from the stratopause ({EARTH_STRATOPAUSE_ALTITUDE_KM:,.0f} km) to the\\n"\n'
      '                f"thermopause, about {EARTH_THERMOPAUSE_ALTITUDE_KM:,.0f} km up (NOAA JetStream; NASA). It includes\\n"\n'
      '                "the mesosphere where meteors burn up and the thermosphere where the aurora occurs and\\n"\n'
      '                "the International Space Station orbits. In the thermosphere, temperatures can reach\\n"\n'
      '                "2,000 degC (3,600 degF), though the gas is so thin that it would feel cold to human skin.\\n"\n'
      '                "Above the thermopause the exosphere thins into space with no boundary; its hydrogen\\n"\n'
      '                f"halo, the geocorona, is detected past {EARTH_GEOCORONA_RADII:.0f} Earth radii."\n'
      '            ),\n'
      '        },\n'),
      ("            'marker_size': 2.0,\n"
      '            # 2026-10-05: the same words as before, now held once in\n'
      '            # earth_visualization_shells.py, where the checkbox tooltip\n'
      '            # reads them too.\n'
      "            'hover_text': earth_upper_atmosphere_info.replace('\\n', '<br>'),\n"
      "            'tooltip': earth_upper_atmosphere_info,\n"
      '        },\n'
      '\n'
      "        # L-292 (2026-10-05): the exosphere, drawn at the geocorona's\n"
      '        # detection floor, as the website draws it since L-291. Colour,\n'
      '        # opacity, point count and marker size are rendering settings and\n'
      "        # match the website's. A fuzzy edge in place of this sharp shell\n"
      '        # is a candidate for L-410 (Tony, 2026-10-05).\n'
      "        'geocorona': {\n"
      "            'name': 'Exosphere (Geocorona)',\n"
      "            'radius_fraction': EARTH_GEOCORONA_RADII,  # the sourced detection floor\n"
      "            'color': 'rgb(200, 200, 255)',\n"
      "            'opacity': 0.15,\n"
      "            'n_points': 20,\n"
      "            'marker_size': 3.0,\n"
      "            'hover_text': earth_geocorona_info.replace('\\n', '<br>'),\n"
      "            'tooltip': earth_geocorona_info,\n"
      '        },\n'),
      1),
    ('inner belt words in the magnetosphere tooltip (L-349)',
      '                f"Inner Van Allen Belt: trapped protons, drawn at the flux peak {EARTH_VAN_ALLEN_INNER_RADII:g} Earth radii out\\n"\n',
      '                f"Inner Van Allen Belt: trapped protons, drawn near their measured flux peak, {EARTH_VAN_ALLEN_INNER_RADII:g} Earth radii out\\n"\n',
      1),
    ('docstring credit',
      ('    describes that day.)\n'
      '"""'),
      ('    describes that day.)\n'
      "Module updated: October 5, 2026 with Anthropic's Claude Opus 5.5 (L-413's\n"
      "    orrery patch: Earth gains its exosphere shell, 'geocorona', drawn at\n"
      "    EARTH_GEOCORONA_RADII (L-292); the upper atmosphere's hover and\n"
      '    tooltip come from earth_upper_atmosphere_info, the same words; the\n'
      '    magnetosphere tooltip\'s inner belt line says "near their measured\n'
      '    flux peak" (L-349). Words approved by Tony, 2026-10-05.)\n'
      '"""'),
      1),
  ],
  'star_sphere_builder.py': [
    ('the frame angle from the store (L-369)',
      ("# Earth's axial tilt (obliquity of the ecliptic), J2000\n"
      'OBLIQUITY_DEG = 23.4393\n'),
      ('# The angle between the celestial equator and the ecliptic of J2000, the\n'
      '# frame every star and grid circle here is drawn in. It was typed here,\n'
      "# a shadow copy of the store's row (L-369, 2026-10-05). The row is the\n"
      "# frame's defining angle, not Earth's tilt on any date; the two differ\n"
      '# by far less than anything drawn here can show.\n'
      'from constants_new import EARTH_OBLIQUITY_J2000_DEG\n'),
      1),
    ('its uses',
      'OBLIQUITY_DEG',
      'EARTH_OBLIQUITY_J2000_DEG',
      7),
    ('docstring credit',
      ('Role: rendering\n'
      'Domain: stars\n'
      '"""'),
      ("Module updated: October 5, 2026 with Anthropic's Claude Opus 5.5 (L-369:\n"
      'the obliquity is read from constants_new.EARTH_OBLIQUITY_J2000_DEG, the\n'
      "frame's defining angle, where it was typed as a shorter copy. The\n"
      'saved star file does not need rebuilding.)\n'
      '\n'
      'Role: rendering\n'
      'Domain: stars\n'
      '"""'),
      1),
  ],
}


def fingerprint(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def read_lf(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    return raw.decode("utf-8").replace("\r\n", "\n"), b"\r\n" in raw


def non_ascii(text):
    return sum(1 for ch in text if ord(ch) > 127)


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the repo ROOT, not from "
                         "documentation/. NOTHING was written.")
    for marker in ROOT_MARKERS:
        if not os.path.isfile(marker):
            raise SystemExit("ERROR: %s is not here, so this is not the %s "
                             "root. NOTHING was written." % (marker, REPO))
    results = []
    for path in sorted(EDITS):
        text, was_crlf = read_lf(path)
        got = fingerprint(text)
        if got != BASE[path]:
            raise SystemExit(
                "ERROR: %s is not the file this patch was built against.\n"
                "       expected %s, found %s. It has changed since\n"
                "       %s, or this patch has already run.\n"
                "       (Line endings are excluded, so they are not the cause.)\n"
                "       NOTHING was written." % (path, BASE[path], got, BUILT_ON))
        before = non_ascii(text)
        done = []
        for label, old, new, want in EDITS[path]:
            found = text.count(old)
            if found != want:
                raise SystemExit("ANCHOR FAIL (%s): expected %d match(es) in "
                                 "%s, found %d. NOTHING was written."
                                 % (label, want, path, found))
            text = text.replace(old, new)
            done.append(label)
        if non_ascii(text) > before:
            raise SystemExit("ERROR: %s would gain non-ASCII characters. "
                             "NOTHING was written." % path)
        results.append((path, text, done, was_crlf))
    for path, text, done, was_crlf in results:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in done:
            print("ok  %-30s %s" % (path, label))
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % path)
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    for line in NEXT:
        print("  " + line)


if __name__ == "__main__":
    main()
