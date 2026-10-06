#!/usr/bin/env python3
"""
patch_L420_2_galactic_plane_and_centre_20261006.py -- ORRERY repo. L-420: the galactic plane in the
Celestial Grid, and the galactic centre in the Star Background.

Built on orrery 51436054330aefd6be2a7efd93ebd58f06c4a2d2
at https://github.com/tonylquintanilla/palomas_orrery
(gallery ed48d078ceb639f5f98f13f4c6abc129f722c566
at https://github.com/tonylquintanilla/tonyquintanilla.github.io;
not touched).

The first of two patches. patch_L420_3 records the session (ledger, Where
We Are, handoff) and runs after this one.

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code and click Run. The same as:
        python patch_L420_2_galactic_plane_and_centre_20261006.py
    Then run patch_L420_3 the same way, then orrery_maintenance_run.py,
    which rewrites data/constants_export.json with the four new rows.

WHAT YOU SEE AFTER IT
    Celestial Grid on: a violet circle, the galactic plane, beside the
    amber ecliptic and the teal equator, and two violet crosses labelled
    NGP and SGP, the galactic poles. With Labels on, they read
        North Galactic Pole (NGP)
        Perpendicular to the disk of our galaxy
    (and the same for the south).
    Star Background on: a violet dot labelled "Sgr A*". Its hover reads
        Sagittarius A*
        The black hole at the centre of our galaxy
        Its direction from the Sun, among the stars
    Both "Ecliptic Coordinates (J2000)" boxes gain the line
        Violet circle: Galactic plane, the disk of the Milky Way
        (NGP, SGP its poles)
    Fixed in passing: with Labels on, the celestial and ecliptic pole
    hovers now show their full names ("North Celestial Pole (NCP)"),
    which the code meant to show and did not.

WHAT CHANGES
    constants_new.py        four rows: Sgr A*'s right ascension and
                            declination in arcseconds (exact as printed),
                            read from Liu, Zhu and Hu, arXiv:1110.6268,
                            eq. (8), the VLBA position of Reid and
                            Brunthaler (2004); and, derived, in degrees.
    star_sphere_builder.py  build_galactic_grid(); the galactic plane,
                            NGP and SGP in the grid; Sgr A* in the Star
                            Background; the pole hover fix.
    palomas_orrery.py       both coordinate boxes; the Celestial Sphere,
                            Star Background, Celestial Grid and Labels
                            tooltips.
    The saved star file, star_data/star_sphere_vmag35.json, is NOT
    rebuilt: the new parts are computed from constants_new.py when the
    plot is drawn.

PERMANENT, though this script is thrown away: the four rows, the new
function and the new traces.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 6, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

REPO = "orrery"
ROOT_MARKERS = ["palomas_orrery.py", "constants_new.py", "LEDGER_CONSOLIDATED.md"]

BASE = {'constants_new.py': '55efa7b95533039ea93569574cd5cb32',
 'palomas_orrery.py': 'f717b633d9be319092d34dafc49c85b0',
 'star_sphere_builder.py': '6a16edece7e1eec91af4c86c069e85c1'}

EDITS = {'constants_new.py': [('docstring stamp (L-420)',
                       '2026-09-28 crust ruling as the ruling itself; the '
                       "LEO outer edge's\n"
                       "stale note is corrected. L-292: the geocorona row's "
                       'note says the\n'
                       'orrery now draws it. No value changes.)\n'
                       '"""\n',
                       '2026-09-28 crust ruling as the ruling itself; the '
                       "LEO outer edge's\n"
                       "stale note is corrected. L-292: the geocorona row's "
                       'note says the\n'
                       'orrery now draws it. No value changes.)\n'
                       "Module updated: October 6, 2026 with Anthropic's "
                       'Claude Opus 5.5\n'
                       "(L-420: Sgr A*'s position on the sky, "
                       'SGR_A_STAR_RA_ICRS_ARCSEC and\n'
                       'SGR_A_STAR_DEC_ICRS_ARCSEC, read from Liu, Zhu and '
                       'Hu, arXiv:1110.6268,\n'
                       'eq. (8), with their degree rows derived. The Star '
                       'Background marks it\n'
                       'as the direction of the galactic centre.)\n'
                       '"""\n'),
                      ('Sgr A* position rows',
                       '# Figures: exact -- both inputs are exact.\n'
                       '# Note: drawn, never printed, so it carries no print '
                       'count.\n'
                       '\n'
                       '# The pole directions of the bodies the orrery draws '
                       'with an axis, as ICRF\n',
                       '# Figures: exact -- both inputs are exact.\n'
                       '# Note: drawn, never printed, so it carries no print '
                       'count.\n'
                       '\n'
                       'SGR_A_STAR_RA_ICRS_ARCSEC = 959100.6\n'
                       '# Unit: arcsec\n'
                       '# Status: measured V_SOURCED 2026-10-06\n'
                       '# Figures: 9 -- the source prints 17h 45m 40.0400s, '
                       'to a ten-thousandth\n'
                       '# Figures+: of a second of time, and the two '
                       'trailing zeros are printed\n'
                       '# Figures+: digits within that resolution, so they '
                       'count. Times 15, an\n'
                       '# Figures+: exact conversion, that is 959,100.600 '
                       'arcseconds.\n'
                       '# Read: eq. (8), sec. 3.2, of the document named in '
                       'the Source line, read\n'
                       '# Read+: as the ar5iv HTML rendering, 2026-10-06, '
                       'Claude Opus 5.5.\n'
                       '# Source: Liu, Zhu and Hu, "Constructing a Galactic '
                       'coordinate system\n'
                       '# Source+: based on near-infrared and radio '
                       'catalogs", arXiv:1110.6268,\n'
                       '# Source+: sec. 3.2, eq. (8) -- the absolute '
                       'position of Sgr A*, referred\n'
                       '# Source+: to the ICRS, derived by Reid and '
                       'Brunthaler from Very Long\n'
                       '# Source+: Baseline Array measurements: alpha = 17h '
                       '45m 40.0400s,\n'
                       '# Source+: delta = -29 deg 00\' 28.138". The layer '
                       'below: Reid, M. J. and\n'
                       '# Source+: Brunthaler, A. 2004, ApJ 616, 872.\n'
                       '# Ref: https://ar5iv.arxiv.org/html/1110.6268\n'
                       '# Note: added 2026-10-06 (L-420), the direction of '
                       'the galactic centre\n'
                       "# Note+: in the Star Background. The same paper's "
                       'eq. (7) gives the point\n'
                       '# Note+: the frame defines as galactic longitude '
                       'zero, 17h 45m 37.1991s,\n'
                       '# Note+: -28 deg 56\' 10.221"; it lies on the plane '
                       'of\n'
                       '# Note+: GALACTIC_NORTH_POLE_RA_J2000_DEG to a '
                       'hundred-millionth of a\n'
                       '# Note+: degree, checked 2026-10-06, and Sgr A* sits '
                       '0.05 degrees from\n'
                       '# Note+: it, far below anything the drawing shows. '
                       'The ICRS and the\n'
                       '# Note+: J2000 frame the orrery draws in differ by a '
                       'few hundredths of an\n'
                       '# Note+: arcsecond, also far below it.\n'
                       '\n'
                       'SGR_A_STAR_DEC_ICRS_ARCSEC = -104428.138\n'
                       '# Unit: arcsec\n'
                       '# Status: measured V_SOURCED 2026-10-06\n'
                       "# Figures: 9 -- the source prints -29 deg 00' "
                       '28.138", to a thousandth\n'
                       '# Figures+: of an arcsecond, which is exactly '
                       '-104,428.138 arcseconds.\n'
                       '# Read: as SGR_A_STAR_RA_ICRS_ARCSEC, 2026-10-06, '
                       'Claude Opus 5.5.\n'
                       '# Source: as SGR_A_STAR_RA_ICRS_ARCSEC.\n'
                       '# Ref: https://ar5iv.arxiv.org/html/1110.6268\n'
                       '# Note: stored in arcseconds because that is exact; '
                       'in degrees it does\n'
                       '# Note+: not end. Its companion is '
                       'SGR_A_STAR_RA_ICRS_ARCSEC. The paper\n'
                       '# Note+: prints no error bar for either.\n'
                       '\n'
                       'SGR_A_STAR_RA_ICRS_DEG = SGR_A_STAR_RA_ICRS_ARCSEC / '
                       'ARCSEC_PER_DEG\n'
                       "# Derived: Sgr A*'s right ascension in degrees, "
                       '959100.6 / 3600\n'
                       "# Derived+: = 266.416833, to the row's nine figures\n"
                       '# Unit: deg\n'
                       '# Status: derived 2026-10-06 -- inherits '
                       'SGR_A_STAR_RA_ICRS_ARCSEC,\n'
                       '# Status+: ARCSEC_PER_DEG\n'
                       '# Figures: 9 -- set by SGR_A_STAR_RA_ICRS_ARCSEC '
                       '(959100.6, 9); the\n'
                       '# Figures+: divisor is exact.\n'
                       '# Note: drawn, never printed, so it carries no print '
                       'count.\n'
                       '\n'
                       'SGR_A_STAR_DEC_ICRS_DEG = SGR_A_STAR_DEC_ICRS_ARCSEC '
                       '/ ARCSEC_PER_DEG\n'
                       "# Derived: Sgr A*'s declination in degrees, "
                       '-104428.138 / 3600\n'
                       "# Derived+: = -29.0078161, to the row's nine "
                       'figures\n'
                       '# Unit: deg\n'
                       '# Status: derived 2026-10-06 -- inherits '
                       'SGR_A_STAR_DEC_ICRS_ARCSEC,\n'
                       '# Status+: ARCSEC_PER_DEG\n'
                       '# Figures: 9 -- set by SGR_A_STAR_DEC_ICRS_ARCSEC '
                       '(-104428.138, 9); the\n'
                       '# Figures+: divisor is exact.\n'
                       '# Note: drawn, never printed, so it carries no print '
                       'count.\n'
                       '\n'
                       '# The pole directions of the bodies the orrery draws '
                       'with an axis, as ICRF\n')],
 'palomas_orrery.py': [('docstring stamp (L-420)',
                        "equator is tilted by Earth's axial tilt instead of "
                        'typing it (L-369).\n'
                        'Words approved by Tony, 2026-10-05.)\n',
                        "equator is tilted by Earth's axial tilt instead of "
                        'typing it (L-369).\n'
                        'Words approved by Tony, 2026-10-05.)\n'
                        "Module updated: October 6, 2026 with Anthropic's "
                        'Claude Opus 5.5 (L-420:\n'
                        'both "Ecliptic Coordinates (J2000)" boxes name the '
                        "galactic plane's\n"
                        'violet circle, and the Celestial Sphere, Star '
                        'Background, Celestial Grid\n'
                        'and Labels tooltips name the galactic plane, its '
                        'poles and Sagittarius\n'
                        'A*, which star_sphere_builder.py now draws. Words '
                        'approved by Tony,\n'
                        '2026-10-06.)\n'),
                       ('static plot box: violet circle line',
                        '                            + "<b>Teal circle:</b> '
                        'Celestial equator, tilted from the ecliptic by '
                        "Earth's axial tilt<br>(Earth's rotation-axis hover "
                        'gives the angle for this date)<br><br>"\n',
                        '                            + "<b>Teal circle:</b> '
                        'Celestial equator, tilted from the ecliptic by '
                        "Earth's axial tilt<br>(Earth's rotation-axis hover "
                        'gives the angle for this date)<br><br>"\n'
                        '\n'
                        '                            + "<b>Violet '
                        'circle:</b> Galactic plane, the disk of the Milky '
                        'Way (NGP, SGP its poles)<br><br>"\n'),
                       ('animation box: violet circle line',
                        '                            "<b>Teal circle:</b> '
                        'Celestial equator, tilted from the ecliptic by '
                        "Earth's axial tilt<br>(Earth's rotation-axis hover "
                        'gives the angle for this date)<br><br>"\n',
                        '                            "<b>Teal circle:</b> '
                        'Celestial equator, tilted from the ecliptic by '
                        "Earth's axial tilt<br>(Earth's rotation-axis hover "
                        'gives the angle for this date)<br><br>"\n'
                        '                            "<b>Violet circle:</b> '
                        'Galactic plane, the disk of the Milky Way (NGP, SGP '
                        'its poles)<br><br>"\n'),
                       ('Celestial Sphere tooltip',
                        '    "the celestial equator (tilted by Earth\'s '
                        'axial tilt), and coordinate poles.\\n\\n"\n',
                        '    "the celestial equator (tilted by Earth\'s '
                        'axial tilt), the galactic plane\\n"\n'
                        '    "(the disk of the Milky Way), and coordinate '
                        'poles.\\n\\n"\n'),
                       ('Star Background tooltip',
                        '    "Stars are at their real RA/Dec sky positions '
                        '(ecliptic frame).")\n',
                        '    "Stars are at their real RA/Dec sky positions '
                        '(ecliptic frame).\\n"\n'
                        '    "Also marks Sagittarius A* (Sgr A*), the black '
                        'hole at the\\n"\n'
                        '    "centre of our galaxy.")\n'),
                       ('Celestial Grid tooltip',
                        '    "- Celestial and ecliptic poles, vernal equinox '
                        'marker\\n\\n"\n',
                        '    "- Galactic plane (violet), the disk of the '
                        'Milky Way\\n"\n'
                        '    "- Celestial, ecliptic and galactic poles, '
                        'vernal equinox marker\\n\\n"\n'),
                       ('Labels tooltip',
                        '    "- Full pole names (North/South '
                        'Celestial/Ecliptic Pole)\\n\\n"\n',
                        '    "- Full pole names (North/South '
                        'Celestial/Ecliptic/Galactic Pole)\\n\\n"\n')],
 'star_sphere_builder.py': [('docstring stamp (L-420)',
                             "frame's defining angle, where it was typed as "
                             'a shorter copy. The\n'
                             'saved star file does not need rebuilding.)\n',
                             "frame's defining angle, where it was typed as "
                             'a shorter copy. The\n'
                             'saved star file does not need rebuilding.)\n'
                             '\n'
                             'Module updated: October 6, 2026 with '
                             "Anthropic's Claude Opus 5.5 (L-420:\n"
                             'the Celestial Grid draws the galactic plane, a '
                             'violet circle, and marks\n'
                             'the north and south galactic poles NGP and '
                             'SGP; the Star Background\n'
                             'marks Sagittarius A*, the direction of the '
                             'galactic centre. Both are\n'
                             'computed when the plot is drawn, by '
                             'build_galactic_grid() and from the\n'
                             'Sgr A* rows, out of constants_new.py, so the '
                             'saved star file does not\n'
                             'need rebuilding. Fixed in passing: with Labels '
                             'on, the celestial and\n'
                             'ecliptic pole hovers showed the short label, '
                             '"NCP", where the full name\n'
                             'was meant. Words approved by Tony, '
                             '2026-10-06.)\n'),
                            ('import the galactic rows',
                             'from constants_new import '
                             'EARTH_OBLIQUITY_J2000_DEG\n'
                             '\n'
                             '# Zodiac sign',
                             'from constants_new import '
                             'EARTH_OBLIQUITY_J2000_DEG\n'
                             "# L-420: the galactic plane's pole, and the "
                             "galactic centre's direction.\n"
                             'from constants_new import '
                             '(GALACTIC_NORTH_POLE_RA_J2000_DEG,\n'
                             '                           '
                             'GALACTIC_NORTH_POLE_DEC_J2000_DEG,\n'
                             '                           '
                             'SGR_A_STAR_RA_ICRS_DEG, '
                             'SGR_A_STAR_DEC_ICRS_DEG)\n'
                             '\n'
                             '# Zodiac sign'),
                            ('build_galactic_grid()',
                             '_star_sphere_cache = None\n',
                             '_star_sphere_cache = None\n'
                             '\n'
                             '\n'
                             'def '
                             'build_galactic_grid(n_points=CIRCLE_POINTS):\n'
                             '    """\n'
                             '    The galactic plane and its two poles, as '
                             'unit vectors in the ecliptic\n'
                             '    frame (L-420, 2026-10-06).\n'
                             '\n'
                             '    Computed from constants_new.py when the '
                             'plot is drawn, not stored in\n'
                             '    the saved star file, so the file needs no '
                             'rebuilding and the drawing\n'
                             '    cannot fall behind the rows.\n'
                             '\n'
                             '    The plane is the great circle whose pole '
                             'is the north galactic pole\n'
                             "    of J2000, the same pole the Sun's galactic "
                             'tide is drawn about\n'
                             '    '
                             '(solar_visualization_shells.create_sun_galactic_tide). '
                             'The circle\n'
                             '    starts where it crosses the ecliptic; the '
                             'starting point means\n'
                             '    nothing else, because the circle carries '
                             'no ticks.\n'
                             '\n'
                             "    Returns a dict: 'galactic_plane' (n_points "
                             '[x, y, z] lists),\n'
                             "    'galactic_north_pole' and "
                             "'galactic_south_pole' ([x, y, z]).\n"
                             '    """\n'
                             '    ngp = '
                             'np.array(equatorial_to_ecliptic_unit_vector(\n'
                             '        GALACTIC_NORTH_POLE_RA_J2000_DEG, '
                             'GALACTIC_NORTH_POLE_DEC_J2000_DEG))\n'
                             '    # Two directions in the plane: where it '
                             'meets the ecliptic, and the\n'
                             '    # direction 90 degrees on from that.\n'
                             '    u = np.cross([0.0, 0.0, 1.0], ngp)\n'
                             '    u = u / np.linalg.norm(u)\n'
                             '    v = np.cross(ngp, u)\n'
                             '    angles = np.linspace(0, 2 * np.pi, '
                             'n_points, endpoint=False)\n'
                             '    plane = [[float(np.cos(a) * u[i] + '
                             'np.sin(a) * v[i]) for i in range(3)]\n'
                             '             for a in angles]\n'
                             '    return {\n'
                             "        'galactic_plane': plane,\n"
                             "        'galactic_north_pole': [float(c) for c "
                             'in ngp],\n'
                             "        'galactic_south_pole': [float(-c) for "
                             'c in ngp],\n'
                             '    }\n'),
                            ('Sgr A* marker in the Star Background',
                             '                hoverinfo=hover_info,\n'
                             '                showlegend=False,\n'
                             "                name='_star_background'\n"
                             '            ))\n',
                             '                hoverinfo=hover_info,\n'
                             '                showlegend=False,\n'
                             "                name='_star_background'\n"
                             '            ))\n'
                             '\n'
                             '        # Sagittarius A*, the direction of the '
                             'galactic centre (L-420).\n'
                             '        # A celestial object, so a circle; '
                             'always labelled and hoverable,\n'
                             '        # unlike the stars, so a visitor can '
                             'find it. Position from the\n'
                             "        # store's Sgr A* rows "
                             '(constants_new.py).\n'
                             '        gx, gy, gz = '
                             'equatorial_to_ecliptic_unit_vector(\n'
                             '            SGR_A_STAR_RA_ICRS_DEG, '
                             'SGR_A_STAR_DEC_ICRS_DEG)\n'
                             "        sgra_hover = ('Sagittarius A*<br>'\n"
                             "                      'The black hole at the "
                             "centre of our galaxy<br>'\n"
                             "                      'Its direction from the "
                             "Sun, among the stars')\n"
                             '        fig.add_trace(go.Scatter3d(\n'
                             '            x=[gx * R], y=[gy * R], z=[gz * '
                             'R],\n'
                             "            mode='markers+text',\n"
                             '            marker=dict(size=4, '
                             "color='rgba(205, 165, 255, 0.95)',\n"
                             "                        symbol='circle'),\n"
                             "            text=['Sgr A*'],\n"
                             "            textfont=dict(color='rgba(205, "
                             "165, 255, 0.75)', size=9),\n"
                             "            textposition='top center',\n"
                             '            customdata=[sgra_hover],\n'
                             '            '
                             "hovertemplate='%{customdata}<extra></extra>',\n"
                             '            showlegend=False,\n'
                             "            name='_sgr_a_star'\n"
                             '        ))\n'),
                            ('galactic plane circle',
                             "            hoverinfo='skip',\n"
                             '            showlegend=False,\n'
                             "            name='_prime_meridian'\n"
                             '        ))\n',
                             "            hoverinfo='skip',\n"
                             '            showlegend=False,\n'
                             "            name='_prime_meridian'\n"
                             '        ))\n'
                             '\n'
                             '    # Galactic plane (violet), computed from '
                             "the store's galactic pole\n"
                             '    # when the plot is drawn (L-420). No '
                             'ticks; the NGP and SGP markers\n'
                             '    # below carry its words.\n'
                             '    galactic = build_galactic_grid()\n'
                             "    gal_pts = galactic['galactic_plane']\n"
                             '    gal_closed = gal_pts + [gal_pts[0]]\n'
                             '    fig.add_trace(go.Scatter3d(\n'
                             '        x=[p[0] * R for p in gal_closed],\n'
                             '        y=[p[1] * R for p in gal_closed],\n'
                             '        z=[p[2] * R for p in gal_closed],\n'
                             "        mode='lines',\n"
                             "        line=dict(color='rgba(175, 135, 235, "
                             "0.40)', width=1.5),\n"
                             "        hoverinfo='skip',\n"
                             '        showlegend=False,\n'
                             "        name='_galactic_plane'\n"
                             '    ))\n'),
                            ('NGP and SGP markers',
                             '            hoverinfo=epole_hinfo,\n'
                             '            showlegend=False,\n'
                             "            name='_ecliptic_poles'\n"
                             '        ))\n',
                             '            hoverinfo=epole_hinfo,\n'
                             '            showlegend=False,\n'
                             "            name='_ecliptic_poles'\n"
                             '        ))\n'
                             '\n'
                             '    # Galactic poles (L-420), drawn as the '
                             'celestial and ecliptic poles are\n'
                             "    ngp = galactic['galactic_north_pole']\n"
                             "    sgp = galactic['galactic_south_pole']\n"
                             '    gpole_hover = None\n'
                             "    gpole_hinfo = 'skip'\n"
                             '    gpole_tpl = None\n'
                             '    if show_labels:\n'
                             "        gpole_hover = ['North Galactic Pole "
                             "(NGP)<br>'\n"
                             "                       'Perpendicular to the "
                             "disk of our galaxy',\n"
                             "                       'South Galactic Pole "
                             "(SGP)<br>'\n"
                             "                       'Perpendicular to the "
                             "disk of our galaxy']\n"
                             '        gpole_hinfo = None\n'
                             '        gpole_tpl = '
                             "'%{customdata}<extra></extra>'\n"
                             '    fig.add_trace(go.Scatter3d(\n'
                             '        x=[ngp[0] * R, sgp[0] * R],\n'
                             '        y=[ngp[1] * R, sgp[1] * R],\n'
                             '        z=[ngp[2] * R, sgp[2] * R],\n'
                             "        mode='markers+text',\n"
                             "        marker=dict(size=4, color='rgba(175, "
                             "135, 235, 0.6)',\n"
                             "                    symbol='cross'),\n"
                             "        text=['NGP', 'SGP'],\n"
                             "        textfont=dict(color='rgba(175, 135, "
                             "235, 0.5)', size=8),\n"
                             "        textposition='top center',\n"
                             '        customdata=gpole_hover,\n'
                             '        hovertemplate=gpole_tpl,\n'
                             '        hoverinfo=gpole_hinfo,\n'
                             '        showlegend=False,\n'
                             "        name='_galactic_poles'\n"
                             '    ))\n'),
                            ('celestial pole hover shows the full name (in '
                             'passing)',
                             '            pole_tpl = '
                             "'%{text}<extra></extra>'\n",
                             '            pole_tpl = '
                             "'%{customdata}<extra></extra>'\n"),
                            ('ecliptic pole hover shows the full name (in '
                             'passing)',
                             '            epole_tpl = '
                             "'%{text}<extra></extra>'\n",
                             '            epole_tpl = '
                             "'%{customdata}<extra></extra>'\n")]}


NEXT = [
    "1. Run patch_L420_3_session_close_20261006.py the same way.",
    "2. Run orrery_maintenance_run.py. Constants export rewrites",
    "   data/constants_export.json: 105 rows exported, up from 101.",
    "3. Move both patch scripts into documentation/, commit and push.",
    "4. Your look: plot with Star Background, Celestial Grid and Labels on.",
]


def read_lf(path):
    raw = open(path, "rb").read()
    return raw.replace(b"\r\n", b"\n").decode("utf-8"), b"\r\n" in raw


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the repo ROOT, not from "
                         "documentation/. NOTHING was written.")
    for marker in ROOT_MARKERS:
        if not os.path.isfile(marker):
            raise SystemExit("ERROR: %s is not here, so this is not the %s "
                             "root. NOTHING was written." % (marker, REPO))
    writes = []
    for path in sorted(EDITS):
        text, was_crlf = read_lf(path)
        fp = hashlib.md5(text.encode("utf-8")).hexdigest()
        if fp != BASE[path]:
            if "SGR_A_STAR_RA_ICRS_ARCSEC" in text and path == "constants_new.py":
                raise SystemExit("ERROR: %s already carries the Sgr A* rows; "
                                 "this patch has run. NOTHING was written."
                                 % path)
            raise SystemExit("ERROR: %s is not the copy this patch was built "
                             "on (orrery 51436054); it has changed since. "
                             "NOTHING was written." % path)
        done = []
        for label, old, new in EDITS[path]:
            found = text.count(old)
            if found != 1:
                raise SystemExit("ANCHOR FAIL (%s): expected 1 match in %s, "
                                 "found %d. NOTHING was written."
                                 % (label, path, found))
            text = text.replace(old, new)
            done.append(label)
        if any(ord(ch) > 127 for ch in text):
            raise SystemExit("ERROR: %s would hold non-ASCII text. NOTHING "
                             "was written." % path)
        writes.append((path, text, done, was_crlf))
    for path, text, done, was_crlf in writes:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in done:
            print("ok  %-24s %s" % (path, label))
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % path)
    print("")
    print("stamps updated: the docstrings of constants_new.py, "
          "star_sphere_builder.py and palomas_orrery.py")
    print("patch applied (%d edits in %d files)"
          % (sum(len(w[2]) for w in writes), len(writes)))
    print("")
    print("NEXT:")
    for line in NEXT:
        print("  " + line)


if __name__ == "__main__":
    main()
