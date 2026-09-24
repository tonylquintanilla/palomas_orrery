"""patch_L322_D_4_orrery_autoscale_and_live_check_20260923.py -- L-322 Stage D, patch D4.

RUN COMMAND

    Save this file in the ROOT of the palomas_orrery repository, open it in
    VS Code and click Run. It refuses to run from documentation/, and
    before patch D3. After it has run, MOVE it into documentation/.

WHAT IT CHANGES, and what stays

    Six files, all or nothing.

    palomas_orrery.py      the Auto scale for a center body fits every
                           feature the shell dispatch draws, not only the
                           sphere shells (Tony's ruling, 2026-09-23: "auto
                           scale should show any rendered feature"). With
                           Earth's crust alone, the cube grows from about
                           0.000085 AU to about 0.00016 AU, so the axis and
                           dipole cone tips, and their hover markers, are
                           inside it. Both the static plot and the
                           animation go through this one function. Nothing
                           that fitted before gets smaller.
    earth_pole_live_check.py   PASS and FAIL are judged against ERFA's TRUE
                           obliquity with a 1-arcsecond allowance, where D3
                           judged against the smoothed mean with 10. The
                           mean is still printed, for information.
    planet_visualization.py  records how far the features drawn for a body
                           reach, leaving out the Sun direction indicator.
                           The indicator only points, has a 0.001 AU
                           minimum length and is clamped to whatever cube
                           it is drawn in; fitting the cube to it would
                           make Earth a speck (0.0012 AU across instead of
                           0.00016). Instead, under Auto, the arrow is
                           fitted inside the cube, so its tip and hover
                           marker are drawn too.
    shared_utilities.py    the Sun direction arrow can be told to fit a
                           given cube even below its 0.001 AU minimum. Off
                           by default, so every other caller is unchanged.
    earth_pole_of_date.py  Earth's axis hover names the Earth-Moon
                           barycenter, the gravitational center of the
                           Earth-Moon system, where it said "the
                           Earth-Moon orbit" (Tony, 2026-09-23); and one
                           docstring paragraph corrected.
    palomas_orrery_dashboard.py  two buttons: Earth Pole Live Check under
                           Tools and Caches, and Test Earth Pole of Date
                           among the checkers under the maintenance run.

    What moves on screen: with the scale on Auto and a center body whose
    axis, cone, magnetosphere or tail reaches past its outermost sphere
    shell, the cube is larger than before and the whole feature shows.

    Nothing in the gallery repository is touched.

Built on orrery 0ab14d864e90843df7ec72d054db82b1f21bfadf
at https://github.com/tonylquintanilla/palomas_orrery. (Its six files
are unchanged since 1319e496, where the first issue of this patch was
built; this issue replaces that one, which was never run.)

Written September 23, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os
import sys

EDITS = [
    ('palomas_orrery.py', '2deb63f343d57b031b06b59f49be49c9', 'f505496fe28a473ccc93ff5f7c5d7f37', [
        ("Stage D, patch D3: both pipelines tell earth_pole_of_date.py the plot's\ndate before building the center-body shells, so Earth's axis is drawn\nfor that date; the animation uses its first frame's date).\n",
         "Stage D, patch D3: both pipelines tell earth_pole_of_date.py the plot's\ndate before building the center-body shells, so Earth's axis is drawn\nfor that date; the animation uses its first frame's date).\nModule updated: September 23, 2026 with Anthropic's Claude Opus 5.5 (L-322\nStage D, patch D4: the Auto scale for a center body now fits every\nfeature the shell dispatch draws, not only the sphere shells, so a\nrotation axis or dipole cone that reaches past the outermost shell is no\nlonger cut off with its hover marker, and the Sun direction arrow is\nfitted inside the cube. Tony's ruling, 2026-09-23.)\n"),
        ('from planet_visualization import (              # the greyed out imports are created in runtime with celestial_objects.py\n    create_celestial_body_visualization,\n',
         'from planet_visualization import (              # the greyed out imports are created in runtime with celestial_objects.py\n    create_celestial_body_visualization,\n    auto_cube_half_width,   # L-322 Stage D, patch D4: one Auto-cube rule\n'),
        ('def add_center_body_shells(fig, center_object_name, sun_shell_vars_map,\n',
         'def _auto_center_half_range(fig, body_name):\n    """Half-width of the Auto cube for a center body, in AU (0.0 if unknown).\n\n    Tony\'s ruling, 2026-09-23: Auto scale shows every rendered feature.\n    Until then Auto sized the cube to twice the outermost SPHERE shell\n    only, so anything drawn past it -- a rotation axis three body radii\n    long, a dipole cone, a magnetotail -- ran out of the cube, and Plotly\n    does not draw what falls outside the axis ranges. The hover markers at\n    the axis and cone tips disappeared with them (Earth with only its crust\n    shown: cube 0.000085 AU, tips at about 0.000117 AU).\n\n    Now the cube is the larger of two sizes. Twice the outermost sphere\n    shell, as before, so nothing that fitted gets smaller. And 1.2 times\n    the farthest vertex of every feature the shell dispatch drew for this\n    body, which create_celestial_body_visualization records in\n    fig._body_feature_extent_au; 1.2 is Fly To\'s own margin. The Sun\n    direction indicator is not counted: it only points, and it is clamped\n    to whatever cube it is drawn in. Both factors are rendering settings:\n    they set how much empty space frames the drawing, not where anything\n    is.\n    """\n    shell_r = getattr(fig, \'_shell_outermost_radius_au\', 0.0) or 0.0\n    extents = getattr(fig, \'_body_feature_extent_au\', None) or {}\n    return auto_cube_half_width(shell_r, extents.get(body_name, 0.0))\n\n\ndef add_center_body_shells(fig, center_object_name, sun_shell_vars_map,\n'),
        ("        # Auto-scale axis to shell radius (same as planet path)\n        if hasattr(fig, '_shell_outermost_radius_au') and scale_value == 'Auto':\n            shell_r = fig._shell_outermost_radius_au * 2\n            axis_range = [-shell_r, shell_r]\n",
         "        # Auto-scale the cube to fit every rendered feature (same as the\n        # planet path). L-322 Stage D, patch D4: was 2x the outermost\n        # sphere shell only.\n        if scale_value == 'Auto':\n            shell_r = _auto_center_half_range(fig, 'Sun')\n            if shell_r > 0:\n                axis_range = [-shell_r, shell_r]\n"),
        ("            # Auto-scale axis to shell radius for migrated bodies\n            if hasattr(fig, '_shell_outermost_radius_au') and scale_value == 'Auto':\n                shell_r = fig._shell_outermost_radius_au * 2\n                axis_range = [-shell_r, shell_r]\n",
         "            # Auto-scale the cube to fit every rendered feature for\n            # migrated bodies. L-322 Stage D, patch D4: was 2x the\n            # outermost sphere shell only, which cut off Earth's axis and\n            # dipole cone with their hover markers.\n            if scale_value == 'Auto':\n                shell_r = _auto_center_half_range(fig, center_object_name)\n                if shell_r > 0:\n                    axis_range = [-shell_r, shell_r]\n"),
    ]),
    ('earth_pole_of_date.py', '60fe43a37e13a6dc331183e172ae7a6c', 'c7d7362f754364e60b2318beb1f463d1', [
        ("    tilt, a rate or a textbook formula. The value includes Earth's nod at\n    that instant, so it is not the smoothed mean value a textbook gives;\n    test_earth_pole_of_date.py compares it with the IAU 2006 mean formula\n    (through ERFA, the library astropy already uses) only as an independent\n    check.\n",
         "    tilt, a rate or a textbook formula. The value includes Earth's nod at\n    that instant, so it is not the smoothed mean value a textbook gives.\n    ERFA, the IAU's SOFA routines as astropy ships them, is the independent\n    check: test_earth_pole_of_date.py tests this geometry against ERFA's\n    true obliquity of date offline, and earth_pole_live_check.py tests the\n    fetched values against it live.\n"),
        ("Module created: September 23, 2026 with Anthropic's Claude Opus 5.5\n(L-322 Stage D, patch D3: Earth's pole of date and tilt of date, fetched\nfrom Horizons, from build manifest rev 3 sections 0 and 4.4)\n",
         "Module created: September 23, 2026 with Anthropic's Claude Opus 5.5\n(L-322 Stage D, patch D3: Earth's pole of date and tilt of date, fetched\nfrom Horizons, from build manifest rev 3 sections 0 and 4.4)\nModule updated: September 23, 2026 with Anthropic's Claude Opus 5.5\n(L-322 Stage D, patch D4: the hover names the Earth-Moon barycenter,\nthe gravitational center of the Earth-Moon system, where it said the\nEarth-Moon orbit; and the paragraph on the\nindependent check named the mean formula where the tests use ERFA's\ntrue obliquity)\n"),
        ("    return ('%.*g deg on %s,<br>measured against the Earth-Moon orbit that '\n            'day (JPL Horizons).<br>It includes Earth\\'s small nod, so it '\n",
         '    # L-322 Stage D, patch D4, Tony\'s wording of 2026-09-23: the orbit is\n    # the Earth-Moon BARYCENTER\'s, the gravitational center of the\n    # Earth-Moon system. "Earth-Moon orbit" could be read as the Moon\'s\n    # orbit around Earth, a different plane about five degrees away.\n    return (\'%.*g deg on %s,<br>measured against the orbit of the \'\n            \'Earth-Moon barycenter,<br>the gravitational center of the \'\n            \'Earth-Moon system,<br>around the Sun that day (JPL Horizons).\'\n            \'<br>It includes Earth\\\'s small nod, so it \'\n'),
    ]),
    ('earth_pole_live_check.py', 'd656ad97b38979a41105d1d4ca2ebac0', '88d07ffed46dc47d34f1550e5d6ee5bf', [
        ("      - the IAU 2006 mean obliquity and the true obliquity of the same\n        date, from ERFA (the SOFA routines astropy ships), and how far the\n        tilt is from each, in arcseconds.\n    The build manifest (rev 3, section 5) allows about 10 arcseconds\n    against the MEAN value, because the fetched pole carries Earth's nod.\n    Each date reports PASS or FAIL on that allowance.\n",
         "      - the true obliquity of the same date from ERFA (the SOFA routines\n        astropy ships), which includes Earth's nod as the fetched pole\n        does, and how far the tilt is from it, in arcseconds. Each date\n        reports PASS or FAIL on that difference.\n      - the IAU 2006 mean obliquity, the smoothed textbook value, for\n        information only. It differs from the tilt by Earth's nod on the\n        day (8.46 arcseconds on 2026-09-24), so it cannot be a tight test.\n    Patch D3 tested against the mean with a 10-arcsecond allowance; on\n    2026-09-24 today's nod used 8.46 of it, so a pass said little. Patch\n    D4 tests against the true value instead (Tony, 2026-09-23).\n"),
        ("Module created: September 23, 2026 with Anthropic's Claude Opus 5.5\n(L-322 Stage D, patch D3)\n",
         "Module created: September 23, 2026 with Anthropic's Claude Opus 5.5\n(L-322 Stage D, patch D3)\nModule updated: September 23, 2026 with Anthropic's Claude Opus 5.5\n(L-322 Stage D, patch D4: PASS and FAIL judged against ERFA's true\nobliquity with a 1-arcsecond allowance, where D3 judged against the\nmean with 10; the mean is still printed)\n"),
        ("# Source: build manifest L-322 Stage D rev 3, section 5 -- the declared\n# allowance against the smoothed IAU 2006 value, about 10 arcseconds,\n# because the fetched pole carries Earth's nod (nutation). A test\n# allowance, not a measurement.\nALLOWANCE_ARCSEC = 10.0\n",
         "# Source: declared 2026-09-23, L-322 Stage D patch D4 -- a test allowance,\n# not a measurement. Tony's live run of 2026-09-24 put the fetched tilt\n# within 0.25 arcseconds of ERFA's true obliquity on all five dates, 2000\n# to 2100. What is left comes from two known differences: Horizons uses\n# the IAU 1976/1980 precession and nutation (Horizons manual, Reference\n# Frames), ERFA the IAU 2006/2000A models; and the barycenter's\n# osculating orbit plane is not quite the mean ecliptic. One arcsecond is\n# four times the largest difference seen, and an eighth of the 8.46\n# arcseconds of nod the same run measured on 2026-09-24, so a pass\n# means the tilt tracks the nod.\nALLOWANCE_ARCSEC = 1.0\n"),
        ('        ok = abs(d_mean) <= ALLOWANCE_ARCSEC\n',
         '        ok = abs(d_true) <= ALLOWANCE_ARCSEC\n'),
        ("        print('            ERFA mean %.7f (tilt minus mean %+.2f arcsec, %s)'\n              % (mean, d_mean, 'PASS' if ok else 'FAIL'))\n        print('            ERFA true %.7f (tilt minus true %+.2f arcsec)'\n              % (true, d_true))\n",
         "        print('            ERFA true %.7f (tilt minus true %+.2f arcsec, %s)'\n              % (true, d_true, 'PASS' if ok else 'FAIL'))\n        print('            ERFA mean %.7f (tilt minus mean %+.2f arcsec, '\n              'information only: the difference is Earth\\'s nod)'\n              % (mean, d_mean))\n"),
        ("    print('EARTH POLE LIVE CHECK: every date within %.0f arcseconds of the '\n          'IAU 2006 mean. Copy this whole output into the chat.'\n          % ALLOWANCE_ARCSEC)\n",
         "    print('EARTH POLE LIVE CHECK: every date within %.0f arcsecond of '\n          'ERFA\\'s true obliquity. Copy this whole output into the chat.'\n          % ALLOWANCE_ARCSEC)\n"),
    ]),
    ('palomas_orrery_dashboard.py', '028c6047a9bbab6d8619bd2163973254', '5cf8f142befa083f19a89d3763f1871e', [
        ('-- and Gallery Builder Offline Tests no longer carries a check count,\nwhich went stale the day after it was written.\n"""\n',
         '-- and Gallery Builder Offline Tests no longer carries a check count,\nwhich went stale the day after it was written.\nSeptember 23, 2026 with Anthropic\'s Claude Opus 5.5 (L-322 Stage D, patch\nD4), on Tony\'s request: added Earth Pole Live Check to Tools and Caches,\nthe script that fetches Earth\'s pole and orbit from Horizons and checks\nthe tilt against ERFA; and Test Earth Pole of Date to the checkers under\nthe maintenance runner, which patch D3 put in the runner with no button\nhere. Both in alphabetical place.\n"""\n'),
        ('        ("Test Orbit Cache",\n         "test_orbit_cache.py",\n',
         '        ("Test Earth Pole of Date",\n         "test_earth_pole_of_date.py",\n         "Offline checks of Earth\'s pole and tilt of the plot\'s date: the "\n         "build manifest\'s worked case, the geometry against ERFA\'s true "\n         "obliquity for 2000, 2026 and 2100, the fall-back to the frame\'s "\n         "year-2000 axis when Horizons cannot be reached, the cache, the "\n         "hover words, and that Earth\'s axis really uses the pole of date. "\n         "Never contacts Horizons; Earth Pole Live Check does.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Orbit Cache",\n         "test_orbit_cache.py",\n'),
        ('        ("Export Orbit Cache",\n',
         '        ("Earth Pole Live Check",\n         "earth_pole_live_check.py",\n         "Fetch Earth\'s pole and the orbit of the Earth-Moon barycenter from "\n         "Horizons for five "\n         "dates, 2000 to 2100, and check the tilt of date against ERFA\'s "\n         "true obliquity (1 arcsecond allowance), then measure the monthly "\n         "wobble of Earth\'s own orbit. Needs the internet, takes a minute or "\n         "two, writes nothing. Run after any change to earth_pole_of_date.py "\n         "or when Horizons may have changed; paste its output into the chat.",\n         SCRIPT_DIR,\n         True),\n        ("Export Orbit Cache",\n'),
    ]),
    ('planet_visualization.py', '54aeeffa05f41b0df56c98ae994419fe', 'bb045416d469b8edba836343b90a8972', [
        ('outermost_radius_au, body_name passed for distinct multi-body indicators)\n\nRole: rendering\n',
         "outermost_radius_au, body_name passed for distinct multi-body indicators)\nModule updated: September 23, 2026 with Anthropic's Claude Opus 5.5\n(L-322 Stage D, patch D4: records fig._body_feature_extent_au, the reach\nof everything the dispatch drew for a body EXCEPT the Sun direction\nindicator, for the Auto scale in palomas_orrery.py)\n\nRole: rendering\n"),
        ('def create_celestial_body_visualization(fig, body_name, shell_vars, animate=False, frames=None,\n',
         'def auto_cube_half_width(shell_outermost_au, feature_extent_au):\n    """Half-width, in AU, of the Auto cube for a center body.\n\n    L-322 Stage D, patch D4, on Tony\'s ruling of 2026-09-23 that the Auto\n    scale shows every rendered feature. The larger of two sizes: twice the\n    outermost sphere shell, which is what Auto used before, so nothing that\n    fitted gets smaller; and 1.2 times the farthest vertex of every feature\n    the dispatch drew for the body except the Sun direction indicator (see\n    fig._body_feature_extent_au below). 1.2 is Fly To\'s own margin. Both\n    factors are rendering settings: they frame the drawing and move\n    nothing in it. One rule, used by the indicator here and by the axis\n    ranges in palomas_orrery.py.\n    """\n    return max(2.0 * (shell_outermost_au or 0.0),\n               1.2 * (feature_extent_au or 0.0))\n\n\ndef create_celestial_body_visualization(fig, body_name, shell_vars, animate=False, frames=None,\n'),
        ('    # ONE sun direction indicator per body (replaces ~50 per-shell calls).\n',
         '    # L-322 Stage D, patch D4: the reach of every feature drawn so far --\n    # shells, magnetosphere, belts, rotation axis, dipole cone -- before\n    # the Sun direction indicator is added. The Auto scale fits this\n    # (Tony, 2026-09-23: Auto shows every rendered feature). The indicator\n    # is left out on purpose: it only points, it has a 0.001 AU minimum\n    # length and it is clamped to whatever cube it is drawn in, so fitting\n    # the cube to it would shrink Earth to a speck (0.0012 AU against\n    # 0.00016 AU with the crust alone) and it shows either way.\n    try:\n        from shared_utilities import traces_extent_from_center\n        _feat_ext = traces_extent_from_center(\n            list(fig.data)[_dispatch_start_idx:], center_position)\n        if _feat_ext > 0:\n            if not hasattr(fig, \'_body_feature_extent_au\'):\n                fig._body_feature_extent_au = {}\n            if _feat_ext > fig._body_feature_extent_au.get(body_name, 0.0):\n                fig._body_feature_extent_au[body_name] = _feat_ext\n    except Exception as _feat_err:\n        print(f"[DISPATCH] feature-extent record skipped for {body_name}: "\n              f"{_feat_err}", flush=True)\n\n    # ONE sun direction indicator per body (replaces ~50 per-shell calls).\n'),
        ('        indicator_traces = create_sun_direction_indicator(\n            center_position=center_position,\n            sun_position=sun_position,\n            axis_range=axis_range,\n            shell_radius=outermost_radius_au,\n            object_type=object_type if object_type is not None else body_name,\n            center_object=center_object,\n            body_name=body_name,\n        )\n',
         "        # L-322 Stage D, patch D4: under Auto (axis_range is None) for the\n        # center body, the cube is already known here -- it is\n        # auto_cube_half_width() of what was just drawn -- so the arrow is\n        # fitted inside it, and its hover marker at the tip is drawn. Before\n        # this, the arrow's 0.001 AU minimum carried the tip outside a small\n        # body's cube, and Plotly does not draw what falls outside.\n        _ind_range, _ind_fit = axis_range, False\n        if axis_range is None and center_object == body_name:\n            _half = auto_cube_half_width(\n                outermost_radius_au,\n                getattr(fig, '_body_feature_extent_au', {}).get(body_name, 0.0))\n            if _half > 0:\n                _ind_range, _ind_fit = [-_half, _half], True\n        indicator_traces = create_sun_direction_indicator(\n            center_position=center_position,\n            sun_position=sun_position,\n            axis_range=_ind_range,\n            shell_radius=outermost_radius_au,\n            object_type=object_type if object_type is not None else body_name,\n            center_object=center_object,\n            body_name=body_name,\n            fit_to_range=_ind_fit,\n        )\n"),
    ]),
    ('shared_utilities.py', 'f4ee040ceb9c904200d65dbc580ca2d6', '502398900110ce8e71b629dc89bb6597', [
        ('                Anthropic\'s Claude Opus 4.7 (D3.1 follow-up: body_name parameter\n                for distinct multi-body Sun Direction indicators)\n"""\n',
         '                Anthropic\'s Claude Opus 4.7 (D3.1 follow-up: body_name parameter\n                for distinct multi-body Sun Direction indicators)\nModule updated: September 23, 2026 with Anthropic\'s Claude Opus 5.5\n(L-322 Stage D, patch D4: create_sun_direction_indicator takes\nfit_to_range; when True the arrow is shortened to fit the given cube even\nbelow its 0.001 AU minimum. Default False keeps every other caller as it\nwas.)\n"""\n'),
        ('                              object_type=None, center_object=None,\n                              body_name=None):\n',
         '                              object_type=None, center_object=None,\n                              body_name=None, fit_to_range=False):\n'),
        ('        body_name (str): Optional body name for body-prefixed legend label.\n                         When provided, legend reads "{body_name}: Sun Direction".\n    """\n',
         '        body_name (str): Optional body name for body-prefixed legend label.\n                         When provided, legend reads "{body_name}: Sun Direction".\n        fit_to_range (bool): L-322 Stage D, patch D4. True when axis_range\n                         is the Auto cube fitted to the drawing: the arrow\n                         then always ends inside it, below the 0.001 AU\n                         minimum if need be, so its tip and hover marker\n                         are drawn. False (default) keeps the minimum.\n    """\n'),
        ('                plot_scale = max(min_scale, 0.95 * _t_exit)\n',
         '                plot_scale = (0.95 * _t_exit if fit_to_range\n                              else max(min_scale, 0.95 * _t_exit))\n'),
    ]),
]

NEW_FILES = []


def content(raw):
    """LF-normalised bytes: line endings are not content."""
    return raw.replace(b"\r\n", b"\n")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    if os.path.basename(here) == "documentation":
        print("ERROR: run this from the repository ROOT, not from "
              "documentation/. Move it up one level, run it, then move it "
              "back. NOTHING was written.")
        return 1
    store = os.path.join(here, "constants_new.py")
    if not os.path.exists(store):
        print("ERROR: constants_new.py is not beside this script, so this "
              "is not the orrery root. NOTHING was written.")
        return 1
    with open(store, "rb") as handle:
        pass
    if not os.path.exists(os.path.join(here, "earth_pole_of_date.py")):
        print("ERROR: patch D3 has not been applied (earth_pole_of_date.py "
              "is missing). NOTHING was written.")
        return 1

    planned = []
    problems = []
    notes = []
    already = 0
    for name, base_fp, want_fp, hunks in EDITS:
        path = os.path.join(here, name)
        if not os.path.exists(path):
            problems.append("%s: not found" % name)
            continue
        with open(path, "rb") as handle:
            raw = handle.read()
        is_crlf = b"\r\n" in raw
        body = content(raw)
        actual = hashlib.md5(body).hexdigest()
        if actual == want_fp:
            problems.append("%s: already carries this patch's result -- a "
                            "second run" % name)
            already += 1
            continue
        if actual != base_fp:
            problems.append("%s: BASE MOVED. Expected %s, found %s"
                            % (name, base_fp[:12], actual[:12]))
            continue
        if is_crlf:
            notes.append("%s: the working copy is CRLF; written back CRLF"
                         % name)
        text = body.decode("utf-8")
        for index, (old, new) in enumerate(hunks, 1):
            found = text.count(old)
            if found != 1:
                problems.append("%s: ANCHOR FAIL, edit %d of %d matched %d "
                                "times" % (name, index, len(hunks), found))
                break
            if any(ord(ch) > 127 for ch in new):
                problems.append("%s: edit %d inserts a non-ASCII character"
                                % (name, index))
                break
            text = text.replace(old, new)
        else:
            out = text.encode("utf-8")
            if hashlib.md5(out).hexdigest() != want_fp:
                problems.append("%s: the result is not the file this patch "
                                "was built to produce" % name)
                continue
            planned.append((path, out.replace(b"\n", b"\r\n") if is_crlf
                            else out, name, "%d edit(s)" % len(hunks)))
    for name, want_fp, text in NEW_FILES:
        path = os.path.join(here, name)
        data = text.encode("utf-8")
        if hashlib.md5(data).hexdigest() != want_fp:
            problems.append("%s: the text in this patch is damaged" % name)
            continue
        if os.path.exists(path):
            with open(path, "rb") as handle:
                if hashlib.md5(content(handle.read())).hexdigest() == want_fp:
                    problems.append("%s: already exists with this patch's "
                                    "content -- a second run" % name)
                else:
                    problems.append("%s: already exists with OTHER content; "
                                    "this patch will not overwrite it" % name)
            continue
        planned.append((path, data, name, "new file"))

    if problems:
        print("FAILURE -- NOTHING was written:")
        for line in problems:
            print("  " + line)
        print("")
        print("Undo is Discard Changes in GitHub Desktop.")
        return 1

    for path, data, name, what in planned:
        with open(path, "wb") as handle:
            handle.write(data)
        print("ok  %-36s %s" % (name, what))
    for line in notes:
        print("note: " + line)
    print("")
    print("patch applied (%d file(s))" % len(planned))
    print("")
    print("DO THESE, IN THIS ORDER:")
    print("  1. Plot Earth as the center, scale on Auto, crust and axis "
          "shown, for today. The whole axis and cone should be inside the "
          "cube, and hovering the tip of the yellow axis should show its "
          "hover without changing the scale.")
    print("  2. Run Earth Pole Live Check from the dashboard (Tools and "
          "Caches). Every date should PASS against ERFA's true obliquity. "
          "Paste its output into the chat.")
    print("  3. Run the orrery maintenance run.")
    print("  4. Commit and push, including data/earth_pole_cache.json if "
          "GitHub Desktop lists it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
