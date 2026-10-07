#!/usr/bin/env python3
"""
patch_L420_4_circle_hovers_and_tide_20261006.py -- ORRERY repo. Tony's
look at L-420, built: each coordinate circle says what it is in a hover
cross, the coordinate boxes keep only the axes, and the galactic tide is
drawn brighter with a faint cone that shows its shape from the side.

Built on orrery fbd223ee at
https://github.com/tonylquintanilla/palomas_orrery (gallery ed48d078
not read or changed).

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT, open it in VS Code and click
    Run. Then follow the NEXT steps it prints.

WHAT CHANGES
    star_sphere_builder.py   one hover cross on each of the ecliptic, the
        celestial equator and the galactic plane, with the words you
        approved; build_galactic_grid() also returns where the galactic
        plane's cross sits; a docstring stamp.
    palomas_orrery.py   both "Ecliptic Coordinates (J2000)" boxes drop
        the three circle lines and point to the crosses; a docstring
        stamp.
    solar_visualization_shells.py   the galactic tide: 5,000 points,
        twice the size and opacity, a faint double cone where its
        strength peaks, one new hover line; a docstring stamp.
    LEDGER_CONSOLIDATED.md and documentation/HANDOFF_L420_galactic_plane_
        20261006.md   a few lines each, matched ONLY at those lines, so
        your notes anywhere else in them never stop this patch.

TESTED on a copy of fbd223ee: every edit landed; the orrery's window
started headless with no edit; the circles and the tide were built
through the same functions the plot and the animation call, and their
traces read back; orrery_maintenance_run.py passed all 20 gating
checkers, the scanner's Tier-1 findings the same 296; a second run
refused and wrote nothing.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 6, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

REPO = "orrery"
ROOT_MARKERS = ("palomas_orrery.py", "LEDGER_CONSOLIDATED.md")
ZONED = {}
NEXT = ["1. Run orrery_maintenance_run.py; the gating checkers pass.",
        "2. Move this script into documentation/, commit and push.",
        "3. Your look: plot the Sun with Galactic Tide, Celestial Grid and",
        "   Star Background on. Turn until the violet circle is edge-on and",
        "   look at the tide and its cone; hover the circles' three crosses."]

BASE = {
    'palomas_orrery.py': 'cb5452d96305beb2e718a9bee85e6da1',
    'solar_visualization_shells.py': 'dd8e73189603f53d630992d507808b13',
    'star_sphere_builder.py': 'a3a8c44ba44be9d712909c35d64468f0',
}

ANCHOR_ONLY = ('LEDGER_CONSOLIDATED.md', 'documentation/HANDOFF_L420_galactic_plane_20261006.md')

EDITS = {
  'palomas_orrery.py': [
    ('docstring stamp (L-420, the box)',
      "Linux and macOS as well. Tony's colour of January 2026, restored.)\n",
      'Linux and macOS as well. Tony\'s colour of January 2026, restored.)\nModule updated: October 6, 2026 with Anthropic\'s Claude Opus 5.5 (L-420,\nafter Tony\'s look: both "Ecliptic Coordinates (J2000)" boxes keep the\naxes and drop the three circle lines, which move to a hover cross on\neach circle in star_sphere_builder.py. Words approved by Tony,\n2026-10-06.)\n',
      1),
    ('static plot box: circle lines move to hovers',
      '                            + "<b>XY plane:</b> Ecliptic (amber circle)<br>"\n                            + ("<i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(For exoplanets: sky plane, perpendicular to line of sight)</i><br><br>" \n                            if is_exoplanet_mode else "")\n\n                            + "<b>Teal circle:</b> Celestial equator, tilted from the ecliptic by Earth\'s axial tilt<br>(Earth\'s rotation-axis hover gives the angle for this date)<br><br>"\n\n                            + "<b>Violet circle:</b> Galactic plane, the disk of the Milky Way (NGP, SGP its poles)<br><br>"\n\n                            + "<i>Enable Celestial Grid to see coordinate circles</i>"\n',
      '                            + "<b>XY plane:</b> Ecliptic<br>"\n                            + ("<i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(For exoplanets: sky plane, perpendicular to line of sight)</i><br><br>" \n                            if is_exoplanet_mode else "<br>")\n\n                            # L-420: the circles\' own lines moved to a hover cross on\n                            # each circle (star_sphere_builder.py). Tony, 2026-10-06.\n                            + "<i>Enable Celestial Grid to see the coordinate circles;<br>hover the + on each circle to see what it is</i>"\n',
      1),
    ('animation box: circle lines move to hovers',
      '                            "<b>XY plane:</b> Ecliptic (amber circle)<br>"\n                            "<b>Teal circle:</b> Celestial equator, tilted from the ecliptic by Earth\'s axial tilt<br>(Earth\'s rotation-axis hover gives the angle for this date)<br><br>"\n                            "<b>Violet circle:</b> Galactic plane, the disk of the Milky Way (NGP, SGP its poles)<br><br>"\n                            "<i>Enable Celestial Grid to see coordinate circles</i>" if not is_exoplanet_mode\n',
      '                            "<b>XY plane:</b> Ecliptic<br><br>"\n                            "<i>Enable Celestial Grid to see the coordinate circles;<br>hover the + on each circle to see what it is</i>" if not is_exoplanet_mode\n',
      1),
  ],
  'star_sphere_builder.py': [
    ('docstring stamp (L-420, the circle hovers)',
      'was meant. Words approved by Tony, 2026-10-06.)\n\nRole: rendering\n',
      "was meant. Words approved by Tony, 2026-10-06.)\n\nModule updated: October 6, 2026 with Anthropic's Claude Opus 5.5 (L-420,\nafter Tony's look: each of the three circles, the ecliptic, the\ncelestial equator and the galactic plane, carries one hover cross\nthat says what it is, whenever the Celestial Grid is on. The words\nmove here from the coordinate box in palomas_orrery.py. Words\napproved by Tony, 2026-10-06.)\n\nRole: rendering\n",
      1),
    ("the circles' cross places and words",
      'def build_galactic_grid(n_points=CIRCLE_POINTS):\n',
      "# Where each circle's hover cross sits along its circle, in degrees\n# (L-420, after Tony's look of 2026-10-06). Rendering settings, an\n# angular marker step, not facts about the sky: each is placed far\n# from where the other two circles cross it, and off the ticks, so the\n# cross reads as its own marker.\nECLIPTIC_INFO_MARKER_LON = 142.5   # ecliptic longitude\nEQUATOR_INFO_MARKER_RA = 52.5      # right ascension, in degrees\nGALACTIC_INFO_MARKER_LON = 110.0   # galactic longitude\n\n# What each circle is, for its hover cross. Words approved by Tony,\n# 2026-10-06; until then they sat in the coordinate box at the plot's\n# left (palomas_orrery.py).\nCIRCLE_INFO_ECLIPTIC = (\n    'Ecliptic (amber circle)<br>'\n    'The plane of Earth\\'s orbit around the Sun,<br>'\n    'and the plot\\'s XY plane')\nCIRCLE_INFO_EQUATOR = (\n    'Celestial equator (teal circle)<br>'\n    'Earth\\'s equator carried out onto the sky<br>'\n    'Tilted from the ecliptic by Earth\\'s axial tilt;<br>'\n    'Earth\\'s rotation-axis hover gives the angle for this date')\nCIRCLE_INFO_GALACTIC = (\n    'Galactic plane (violet circle)<br>'\n    'The disk of the Milky Way, seen from the Sun<br>'\n    'Its poles are marked NGP and SGP')\n\n\ndef build_galactic_grid(n_points=CIRCLE_POINTS):\n",
      1),
    ('build_galactic_grid docstring: the info point',
      '    Returns a dict: \'galactic_plane\' (n_points [x, y, z] lists),\n    \'galactic_north_pole\' and \'galactic_south_pole\' ([x, y, z]).\n    """\n',
      '    Returns a dict: \'galactic_plane\' (n_points [x, y, z] lists),\n    \'galactic_north_pole\' and \'galactic_south_pole\' ([x, y, z]), and\n    \'galactic_plane_info\' ([x, y, z]), where the plane\'s hover cross\n    sits: galactic longitude GALACTIC_INFO_MARKER_LON, counted\n    from the direction of Sagittarius A* (the SGR_A_STAR rows).\n    """\n',
      1),
    ('build_galactic_grid returns the info point',
      "    return {\n        'galactic_plane': plane,\n        'galactic_north_pole': [float(c) for c in ngp],\n        'galactic_south_pole': [float(-c) for c in ngp],\n    }\n",
      "    # The hover cross's place on the plane (L-420): Sgr A*'s direction\n    # laid into the plane gives longitude zero.\n    sgr = np.array(equatorial_to_ecliptic_unit_vector(\n        SGR_A_STAR_RA_ICRS_DEG, SGR_A_STAR_DEC_ICRS_DEG))\n    l0 = sgr - np.dot(sgr, ngp) * ngp\n    l0 = l0 / np.linalg.norm(l0)\n    l90 = np.cross(ngp, l0)\n    lon = np.radians(GALACTIC_INFO_MARKER_LON)\n    info = np.cos(lon) * l0 + np.sin(lon) * l90\n    return {\n        'galactic_plane': plane,\n        'galactic_north_pole': [float(c) for c in ngp],\n        'galactic_south_pole': [float(-c) for c in ngp],\n        'galactic_plane_info': [float(c) for c in info],\n    }\n",
      1),
    ('one hover cross per circle',
      '    # ---- Tick markers (always visible when grid is on) ----\n',
      "    # ---- One hover cross per circle (L-420, 2026-10-06) ----\n    # The circles themselves skip hover; each carries one cross, in the\n    # circle's own colour, through the orrery's info-marker factory.\n    # Shown whenever the grid is on, not only with Labels, since it\n    # replaces the coordinate box's lines. Amber is a saturated warm\n    # fill, so its outline is white; teal and violet keep red.\n    from orrery_rendering import create_info_marker\n    ecl_info = ecliptic_longitude_to_unit_vector(ECLIPTIC_INFO_MARKER_LON)\n    eq_info = equatorial_to_ecliptic_unit_vector(EQUATOR_INFO_MARKER_RA, 0.0)\n    gal_info = galactic['galactic_plane_info']\n    for point, colour, border, words, label in (\n            (ecl_info, 'rgb(239, 159, 39)', 'white', CIRCLE_INFO_ECLIPTIC,\n             '_ecliptic_info'),\n            (eq_info, 'rgb(93, 202, 165)', 'red', CIRCLE_INFO_EQUATOR,\n             '_celestial_equator_info'),\n            (gal_info, 'rgb(175, 135, 235)', 'red', CIRCLE_INFO_GALACTIC,\n             '_galactic_plane_info')):\n        cross = create_info_marker(\n            float(point[0]) * R, float(point[1]) * R, float(point[2]) * R,\n            colour, words, label, border_color=border)\n        cross.name = label\n        fig.add_trace(cross)\n\n    # ---- Tick markers (always visible when grid is on) ----\n",
      1),
  ],
  'solar_visualization_shells.py': [
    ('docstring stamp (L-420, the tide)',
      "Module updated: October 4, 2026 with Anthropic's Claude Opus 5.5\n(L-371, the Sun's distance cards:",
      "Module updated: October 6, 2026 with Anthropic's Claude Opus 5.5\n(L-420, after Tony's look: the galactic tide is drawn brighter, with\n5,000 points, and with a faint double cone where the tide's\nstrength peaks, halfway between the galaxy's plane and its poles,\nso its shape reads from the side as an hourglass. One hover line\nnames the cone. Words approved by Tony, 2026-10-06.)\n\nModule updated: October 4, 2026 with Anthropic's Claude Opus 5.5\n(L-371, the Sun's distance cards:",
      1),
    ('tide: 5,000 points by default',
      'def create_sun_galactic_tide(center_position=(0, 0, 0), n_points=2000):\n',
      'def create_sun_galactic_tide(center_position=(0, 0, 0), n_points=5000):\n',
      1),
    ('tide docstring: the cone',
      '    - Each point stands for the far end of an orbit. Where any real comet\n      is, is not known and is not claimed.\n',
      "    - Each point stands for the far end of an orbit. Where any real comet\n      is, is not known and is not claimed.\n    - The cone (L-420, Tony's choice of 2026-10-06). A faint double cone\n      through the Sun, at the galactic latitude where |sin b cos b| is\n      largest, between the same two edges. It marks where the density\n      above peaks, so the shape reads from the side as an hourglass.\n      It is not a surface any comet is on.\n",
      1),
    ('tide docstring: the point count',
      '    - n_points: Number of random points (default: 2000), a rendering\n      setting.\n',
      "    - n_points: Number of random points (default: 5000, up from 2000\n      after Tony's look of 2026-10-06), a rendering setting.\n",
      1),
    ('tide hover: the cone line',
      "        'Tilted to the galaxy\\'s plane, thickest halfway to its poles<br>'\n",
      "        'Tilted to the galaxy\\'s plane, thickest halfway to its poles<br>'\n        'The pink cone marks that halfway line, where the tide<br>'\n        'changes comets\\' orbits the most<br>'\n",
      1),
    ('tide points: brighter',
      "        marker=dict(size=0.8, color='rgb(255, 182, 193)', opacity=0.2, symbol='circle'),\n",
      "        # Size and opacity doubled, and two and a half times the points,\n        # after Tony's look of 2026-10-06: the tide was too faint to read.\n        marker=dict(size=1.6, color='rgb(255, 182, 193)', opacity=0.45, symbol='circle'),\n",
      1),
    ('tide: the cone',
      '    r_info = OUTER_OORT_CLOUD_AU * 1.05\n    # Phase 1 re-pipe (May 28, 2026): factory-routed.\n',
      "    # The cone (L-420, 2026-10-06). |sin b cos b| is largest where\n    # sin b equals cos b, so at b = arctan(1), north and south. Each half\n    # is a band of triangles between the two edges the points use,\n    # turned by the same matrix M. Faint, no hover: the tide's info\n    # marker carries its words. It toggles with the tide.\n    b_peak = np.arctan(1.0)\n    n_around = 72                      # a rendering setting\n    phi = np.linspace(0, 2 * np.pi, n_around, endpoint=False)\n    cone_traces = []\n    for sign in (1.0, -1.0):\n        b = sign * b_peak\n        ring = np.concatenate([\n            np.vstack([edge * np.cos(b) * np.cos(phi),\n                       edge * np.cos(b) * np.sin(phi),\n                       edge * np.sin(b) * np.ones(n_around)])\n            for edge in (INNER_OORT_CLOUD_AU, OUTER_OORT_CLOUD_AU)], axis=1)\n        cx, cy, cz = M @ ring\n        nxt = (np.arange(n_around) + 1) % n_around\n        here = np.arange(n_around)\n        cone_traces.append(go.Mesh3d(\n            x=cx, y=cy, z=cz,\n            i=np.concatenate([here, nxt]),\n            j=np.concatenate([nxt, n_around + nxt]),\n            k=np.concatenate([n_around + here, n_around + here]),\n            color='rgb(255, 182, 193)',\n            opacity=0.12,\n            flatshading=True,\n            hoverinfo='skip',\n            name='Sun: Galactic Tide Region',\n            legendgroup='Sun: Galactic Tide Region',\n            showlegend=False))\n\n    r_info = OUTER_OORT_CLOUD_AU * 1.05\n    # Phase 1 re-pipe (May 28, 2026): factory-routed.\n",
      1),
    ('tide returns the cone',
      "        customdata='Galactic Tide Region'\n    )\n    return [shell_trace, info_trace]\n",
      "        customdata='Galactic Tide Region'\n    )\n    return [shell_trace] + cone_traces + [info_trace]\n",
      1),
  ],
  'LEDGER_CONSOLIDATED.md': [
    ('header stamp',
      "Tony's runs; Tony's look at L-420 recorded), built on e7073fce.\n",
      "Tony's runs; Tony's look at L-420 recorded), built on e7073fce.\nModule updated: October 6, 2026 with Anthropic's Claude Opus 5.5\n(L-420 after Tony's look: the circles' hovers, the brighter tide and\nits cone; L-408 told the orrery has them), built on fbd223ee.\n",
      1),
    ('L-420 after the look',
      "**Gap:** Tony's two requests above, then close. (Was: Tony's runs and\nlook.)\n",
      '- **The tide\'s X.** A brighter tide alone would not show an X: seen\n  from the side, the layers at 45 degrees flatten into two lobes with\n  an empty strip along the plane, which a sketch showed. Tony chose\n  "brighter plus cone": 5,000 points, twice the size and twice the\n  opacity, and a faint double cone between the Oort cloud\'s two edges\n  at the latitude where |sin b cos b| peaks, computed as arctan(1),\n  not typed. From the side it reads as an hourglass. One hover line\n  names it.\n- **The point count, held down.** 10,000 points was built first, about\n  0.34 MB in a saved plot against 0.07 MB at 2,000. Tony: "i don\'t\n  want to regress into memory heavy renders. We worked hard to reduce\n  memory overhead a few months ago."; then "I could not discern the X\n  at All before even faulty. Let\'s try 5000". 5,000 adds about\n  0.17 MB, only when the tide is on, and once per plot: the animation\n  does not copy shells into its frames. The cone adds about 0.02 MB.\n- **The circles\' words move to the circles.** One hover cross per\n  circle, through create_info_marker, in its circle\'s colour (amber\n  outlined white, teal and violet red), shown whenever the grid is on,\n  each placed far from the other two circles\' crossings. Both\n  coordinate boxes keep the axes and point to the crosses.\n- **Words approved by Tony, 2026-10-06 ("Confirmed").** Tide hover,\n  new line: "The pink cone marks that halfway line, where the tide /\n  changes comets\' orbits the most". Ecliptic: "Ecliptic (amber\n  circle) / The plane of Earth\'s orbit around the Sun, / and the\n  plot\'s XY plane". Equator: "Celestial equator (teal circle) /\n  Earth\'s equator carried out onto the sky / Tilted from the ecliptic\n  by Earth\'s axial tilt; / Earth\'s rotation-axis hover gives the angle\n  for this date". Galactic plane: "Galactic plane (violet circle) / The\n  disk of the Milky Way, seen from the Sun / Its poles are marked NGP\n  and SGP". Box: "XY plane: Ecliptic" and "Enable Celestial Grid to\n  see the coordinate circles; hover the + on each circle to see what\n  it is".\n  `patch_L420_4_circle_hovers_and_tide_20261006.py`.\n- **The phone.** Tony: "galactic plane and Sag A* are shown in\n  celestial coordinates, but only in the orrery, not in phone. so\n  that\'s a design decision." Recorded on L-408; nothing on the\n  website changed.\n- **298 in Tony\'s run, 296 at the push.** The scanner counted two\n  patch scripts\' fingerprint tables while they sat in the repo root;\n  the pushed tree e7073fce scans 296, the same list as before.\n**Gap:** Tony runs patch_L420_4 and the maintenance run, pushes, and\nlooks (Mode 5): the tide from the side with the violet circle edge-on,\nthe cone\'s faintness, the three crosses\' places and colours. Then\nclose.\n',
      1),
    ('L-408 date',
      '<!-- L:408 status:OPEN upd:2026-10-04 section:A flag: rice: -->\n',
      '<!-- L:408 status:OPEN upd:2026-10-06 section:A flag: rice: -->\n',
      1),
    ('L-408: the orrery has the plane',
      "**Gap:** the Sun slice's eighth item (L-412): gallery first; whether\nthe orrery gets the same toggle is asked then; then the tide's look.\n",
      '- **2026-10-06: the orrery has them now.** L-420 draws the galactic\n  plane, its poles NGP and SGP, and Sagittarius A* in the orrery\'s\n  Celestial Grid and Star Background, and, after Tony\'s look, a\n  brighter tide with a cone where its strength peaks. Tony: "galactic\n  plane and Sag A* are shown in celestial coordinates, but only in the\n  orrery, not in phone. so that\'s a design decision." The orrery half\n  of the toggle question below is answered; the tide\'s look is being\n  made there (L-420).\n**Gap:** the Sun slice\'s eighth item (L-412): Tony\'s design decision\non whether the phone draws the galactic plane, Sgr A*, and the tide\'s\ncone and brightness; then the gallery build.\n',
      1),
    ('L-027: run and pushed',
      "**Gap:** Tony runs the patch and the maintenance run, looks at the\npanels on Windows (back to the grey of January to June, a shade\ndarker than Windows' own), and reinstalls agentic-pre-test; the next\nsession confirms its loaded copy reads 1.3. A run on a Mac would\nsettle the last system; macOS has not been tried since Tony's test.\n",
      "- **Run, pushed at e7073fce and reinstalled, 2026-10-06** (Tony's run\n  record).\n**Gap:** Tony's look at the panels on Windows (back to the grey of\nJanuary to June, a shade darker than Windows' own); the next session\nconfirms its loaded copy of agentic-pre-test reads 1.3. A run on a\nMac would settle the last system; macOS has not been tried since\nTony's test.\n",
      1),
  ],
  'documentation/HANDOFF_L420_galactic_plane_20261006.md': [
    ('after the look: section',
      '## Tony-actions\n',
      '## After Tony\'s look: the circles\' hovers, the brighter tide\n\n- Pushed at e7073fce. Tony\'s look: "looks great", with two notes --\n  the galactic tide is very faint and its X cannot be made out, and\n  the circles\' descriptions should move from the box to hover\n  markers on the circles.\n- Found: a brighter tide alone shows two lobes, not an X. Tony chose\n  a brighter tide plus a faint double cone where its strength peaks.\n- Built: `patch_L420_4_circle_hovers_and_tide_20261006.py`, on\n  e7073fce. The words Tony approved are on L-420.\n- Tony noted the phone shows none of this; that design decision is\n  recorded on L-408.\n\n## Tony-actions\n',
      1),
    ('after the look: Where We Are lines',
      '- Needs Tony: a look at the panels on Windows, a shade darker than\n  before; and, when convenient, a run on a Mac.\n',
      '- Needs Tony: a look at the panels on Windows, a shade darker than\n  before; and, when convenient, a run on a Mac.\n- Changed: each coordinate circle says what it is in a hover cross,\n  and the galactic tide is brighter, with a cone showing its shape.\n- Needs Tony: a look at the tide from the side, and a design decision\n  on whether the phone gets the galactic plane, Sgr A* and the cone\n  (L-408).\n',
      1),
    ('after the look: Tony-actions',
      "9. Reinstall agentic-pre-test in Settings > Skills, and replace the\n   Project's instructions with PROJECT_INSTRUCTIONS.md (v3.83).\n",
      "9. Reinstall agentic-pre-test in Settings > Skills, and replace the\n   Project's instructions with PROJECT_INSTRUCTIONS.md (v3.83).\n10. Run `patch_L420_4_circle_hovers_and_tide_20261006.py`, then the\n    maintenance run; move the script into `documentation/`, commit\n    and push.\n11. Plot the Sun with Galactic Tide, Celestial Grid and Star\n    Background on. Turn until the violet circle is edge-on, and look\n    at the tide and its cone; hover the three circles' crosses.\n",
      1),
    ('after the look: next session',
      "- Close L-420 on Tony's look, or adjust what he names.\n",
      "- Close L-420 on Tony's look at patch_L420_4, or adjust what he\n  names.\n",
      1),
  ],
}


def md5(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def read_lf(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    return raw.decode("utf-8").replace("\r\n", "\n"), b"\r\n" in raw


def outside_zone(path, text):
    if path not in ZONED:
        return text
    start, end = ZONED[path]
    a = text.index(start)
    b = text.index(end) + len(end)
    return text[:a] + text[b:]


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
        if not os.path.isfile(path):
            raise SystemExit("ERROR: %s is not here. "
                             "NOTHING was written." % path)
        text, was_crlf = read_lf(path)
        if path not in ANCHOR_ONLY and md5(outside_zone(path, text)) != BASE[path]:
            raise SystemExit(
                "ERROR: %s is not the file this patch was built against\n"
                "       (fbd223ee), or this patch has already run.\n"
                "       (Line endings are excluded, so they are not the cause.)\n"
                "       NOTHING was written." % path)
        done = []
        for label, old, new, want in EDITS[path]:
            found = text.count(old)
            if found != want:
                hint = (" Has this patch already run?"
                        if path in ANCHOR_ONLY else "")
                raise SystemExit("ANCHOR FAIL (%s): expected %d match(es) in "
                                 "%s, found %d.%s NOTHING was written."
                                 % (label, want, path, found, hint))
            text = text.replace(old, new)
            done.append(label)
        results.append((path, text, done, was_crlf))
    for path, text, done, was_crlf in results:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in done:
            print("ok  %-48s %s" % (path, label))
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
