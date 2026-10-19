#!/usr/bin/env python3
"""
patch_L385_1_opening_views_20261019.py -- the orrery's opening views
(L-385), the first of the Sun's drawings (L-412). Every center body's
Auto view opens on its farthest shell drawn plus 20 percent; the
center body's rotation axis and dipole cone are drawn to end just past
that shell; low orbit and the other custom shells count as shells; the
Sun's asteroid belts count as shells.

Built on orrery 6e0cfacd0b6aa42cb09b0ca765be94e68aab6f70 at
https://github.com/tonylquintanilla/palomas_orrery ("L455 earth
numbers"). The website is not touched (gallery 4fc320fa at
https://github.com/tonylquintanilla/tonyquintanilla.github.io).
Tony's orrery folder:
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
Written October 19, 2026 with Anthropic's Claude Opus 5.5.

RUN COMMAND

    python patch_L385_1_opening_views_20261019.py

    Saved in the ORRERY folder above. Open it in VS Code and click Run.
    It takes no arguments and asks no questions.

WHAT IT DOES, all or nothing. The three files must match 6e0cfacd
exactly (line endings aside):

    planet_visualization.py            the Auto rule: the farthest shell
                                       drawn plus 20 percent; the center
                                       body's axis and cone end just past
                                       it; a custom shell's reach is
                                       measured from what it draws
    planet_visualization_utilities.py  the axis and cone builders take a
                                       length limit, never longer than
                                       their set length
    palomas_orrery.py                  the static plot and the animation
                                       read the new rule; the asteroid
                                       belts count as shells drawn

If any file differs from what this was built against, it refuses and
writes nothing.

WHAT IT PRINTS

    Success: one "ok" line per file, then "patch applied".
    Failure: one ERROR or ANCHOR FAIL line and "NOTHING was written."

Undo is Discard Changes in GitHub Desktop.

Role: dev_tools
Domain: dev_tools
"""

import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SHA = '6e0cfacd'
FINGERPRINTS = {'palomas_orrery.py': '8418f771bb0486a843407fb6c64c15f1', 'planet_visualization.py': 'bb045416d469b8edba836343b90a8972', 'planet_visualization_utilities.py': 'a86e49f8709235674690b3bab51af625'}
RESULTS = {'palomas_orrery.py': '96b1e8c0cf39dc2e5c70de914fe89cd2', 'planet_visualization.py': 'a6539f49631578416d330770e41c6391', 'planet_visualization_utilities.py': '6664a97490b1c43e53d64fa64f0301be'}

EDITS = {
    'palomas_orrery.py': [
        ('tooltip strings written with Plotly\'s <br> read as lines in the window\nuntil each body\'s strings are rewritten in the newline form.)\n\n"""\n',
         'tooltip strings written with Plotly\'s <br> read as lines in the window\nuntil each body\'s strings are rewritten in the newline form.)\nModule updated: October 19, 2026 with Anthropic\'s Claude Opus 5.5 (L-385:\nthe Auto view of a center body opens on its farthest shell drawn plus 20\npercent, read from the dispatch\'s fig._body_shell_reach_au; the Sun\'s\nasteroid belts count as shells drawn. Tony\'s rule, 2026-10-18.)\n\n"""\n'),
        ('    """Half-width of the Auto cube for a center body, in AU (0.0 if unknown).\n\n    Tony\'s ruling, 2026-09-23: Auto scale shows every rendered feature.\n    Until then Auto sized the cube to twice the outermost SPHERE shell\n',
         '    """Half-width of the Auto cube for a center body, in AU (0.0 if unknown).\n\n    L-385, 2026-10-19: the cube is the farthest shell drawn plus 20\n    percent (Tony, 2026-10-18), read from fig._body_shell_reach_au, which\n    the shell dispatch records; the rotation axis and dipole cone are\n    drawn to end inside it. auto_cube_half_width() holds the rule. The\n    D4 history below is kept for the record.\n\n    Tony\'s ruling, 2026-09-23: Auto scale shows every rendered feature.\n    Until then Auto sized the cube to twice the outermost SPHERE shell\n'),
        ('    is.\n    """\n    shell_r = getattr(fig, \'_shell_outermost_radius_au\', 0.0) or 0.0\n    extents = getattr(fig, \'_body_feature_extent_au\', None) or {}\n    return auto_cube_half_width(shell_r, extents.get(body_name, 0.0))\n\n\n',
         '    is.\n    """\n    reaches = getattr(fig, \'_body_shell_reach_au\', None) or {}\n    extents = getattr(fig, \'_body_feature_extent_au\', None) or {}\n    return auto_cube_half_width(reaches.get(body_name, 0.0),\n                                extents.get(body_name, 0.0))\n\n\n'),
        ("\n    if center_object_name == 'Sun' and any(var.get() == 1 for var in sun_shell_vars_map.values()):\n        fig = create_celestial_body_visualization(\n            fig, 'Sun', sun_shell_vars_map,\n            center_position=(0, 0, 0),\n            object_type='Sun',\n            center_object='Sun',\n            skip_elements=skip_elements,\n            animate=animate,\n            # (Phase 4, O12) Clamp input for the indicator. Auto passes\n            # None: the Auto range is widened to 2x shell extent AFTER\n",
         "\n    if center_object_name == 'Sun' and any(var.get() == 1 for var in sun_shell_vars_map.values()):\n        # L-385 (2026-10-19): the asteroid belts are built first, so their\n        # reach counts as a shell drawn -- for the opening view and for the\n        # Sun's axis length -- and added after the dispatch, as before.\n        # Until now a belt alone opened at the Sun's axis, 0.29 AU, inside\n        # the main belt's 2 AU.\n        _belt_traces = []\n        for _belt_key, _belt_fn in (\n                ('main_belt', lambda: create_main_asteroid_belt()),\n                ('hildas', lambda: create_hilda_group()),\n                ('trojans_greeks', lambda: create_jupiter_trojans_greeks(jupiter_angle=0)),\n                ('trojans_trojans', lambda: create_jupiter_trojans_trojans(jupiter_angle=0))):\n            if sun_shell_vars_map.get(_belt_key) and sun_shell_vars_map[_belt_key].get() == 1:\n                _belt_traces.extend(_belt_fn())\n        from shared_utilities import traces_extent_from_center\n        _belt_reach = traces_extent_from_center(_belt_traces, (0, 0, 0))\n        fig = create_celestial_body_visualization(\n            fig, 'Sun', sun_shell_vars_map,\n            center_position=(0, 0, 0),\n            object_type='Sun',\n            center_object='Sun',\n            skip_elements=skip_elements,\n            animate=animate,\n            extra_shell_reach_au=_belt_reach,\n            # (Phase 4, O12) Clamp input for the indicator. Auto passes\n            # None: the Auto range is widened to 2x shell extent AFTER\n"),
        ('            if shell_r > 0:\n                axis_range = [-shell_r, shell_r]\n        # Asteroid belts: standalone geometry, not part of unified shell dispatch\n        if sun_shell_vars_map.get(\'main_belt\') and sun_shell_vars_map[\'main_belt\'].get() == 1:\n            for t in create_main_asteroid_belt():\n                fig.add_trace(t)\n        if sun_shell_vars_map.get(\'hildas\') and sun_shell_vars_map[\'hildas\'].get() == 1:\n            for t in create_hilda_group():\n                fig.add_trace(t)\n        if sun_shell_vars_map.get(\'trojans_greeks\') and sun_shell_vars_map[\'trojans_greeks\'].get() == 1:\n            for t in create_jupiter_trojans_greeks(jupiter_angle=0):\n                fig.add_trace(t)\n        if sun_shell_vars_map.get(\'trojans_trojans\') and sun_shell_vars_map[\'trojans_trojans\'].get() == 1:\n            for t in create_jupiter_trojans_trojans(jupiter_angle=0):\n                fig.add_trace(t)\n        if log_prefix:\n            print(f"{log_prefix}Added Sun shells ({len(fig.data)} static traces)", flush=True)\n',
         '            if shell_r > 0:\n                axis_range = [-shell_r, shell_r]\n        # Asteroid belts: standalone geometry, not part of unified shell\n        # dispatch; built above (L-385), added here in the same order.\n        for t in _belt_traces:\n            fig.add_trace(t)\n        if log_prefix:\n            print(f"{log_prefix}Added Sun shells ({len(fig.data)} static traces)", flush=True)\n'),
    ],
    'planet_visualization.py': [
        ('of everything the dispatch drew for a body EXCEPT the Sun direction\nindicator, for the Auto scale in palomas_orrery.py)\n\nRole: rendering\n',
         "of everything the dispatch drew for a body EXCEPT the Sun direction\nindicator, for the Auto scale in palomas_orrery.py)\nModule updated: October 19, 2026 with Anthropic's Claude Opus 5.5\n(L-385: the Auto view opens on the farthest shell drawn plus a margin,\nrecorded per body in fig._body_shell_reach_au; the center body's rotation\naxis and dipole cone end just past that shell; low orbit and the other\ncustom shells count as shells. Tony's rulings, 2026-10-18 and 2026-10-19.)\n\nRole: rendering\n"),
        ('\n\ndef auto_cube_half_width(shell_outermost_au, feature_extent_au):\n    """Half-width, in AU, of the Auto cube for a center body.\n\n    L-322 Stage D, patch D4, on Tony\'s ruling of 2026-09-23 that the Auto\n',
         '\n\ndef auto_cube_half_width(shell_reach_au, feature_extent_au):\n    """Half-width, in AU, of the Auto cube for a center body.\n\n    L-385, on Tony\'s rule of 2026-10-18 for every view: the farthest shell\n    drawn plus a margin, and the line toward the Sun ignored unless it is\n    the only feature drawn. The farthest shell is a sphere shell\'s radius\n    or the reach of a custom shell\'s geometry (low orbit, a magnetosphere,\n    a belt). The rotation axis and dipole cone do not set it; the dispatch\n    shortens them to end inside it. Only when no shell has a reach does\n    the cube fall back to everything else drawn (feature_extent_au). The\n    Sun direction arrow never sets it; it is fitted inside.\n\n    The rule this replaced (D4) took the larger of twice the outermost\n    sphere shell and the margin times every feature, so the Sun\'s long\n    rotation axis set its opening view, and low orbit\'s fallback size set\n    Earth\'s. It is kept below, retired, as _auto_cube_half_width_d4.\n    """\n    # A rendering setting (Tony, 2026-10-18: "plus say 20%"): it frames\n    # the drawing and moves nothing in it, so it stays here, where it is\n    # used, not in constants_new.py.\n    view_margin = 1.2\n    if shell_reach_au and shell_reach_au > 0:\n        return view_margin * shell_reach_au\n    return view_margin * (feature_extent_au or 0.0)\n\n\ndef _auto_cube_half_width_d4(shell_outermost_au, feature_extent_au):\n    """RETIRED by L-385 (2026-10-19); no caller. The D4 rule, kept so the\n    change can be read against it.\n\n    L-322 Stage D, patch D4, on Tony\'s ruling of 2026-09-23 that the Auto\n'),
        ('                                        center_position=(0, 0, 0), sun_position=(0, 0, 0),\n                                        object_type=None, center_object=None,\n                                        skip_elements=None, axis_range=None):\n\n    """\n',
         '                                        center_position=(0, 0, 0), sun_position=(0, 0, 0),\n                                        object_type=None, center_object=None,\n                                        skip_elements=None, axis_range=None,\n                                        extra_shell_reach_au=0.0):\n\n    """\n'),
        ('                            is correct for heliocentric views. Body-centered\n                            views pass actual Sun offset. Phase D2.\n\n    Returns:\n',
         "                            is correct for heliocentric views. Body-centered\n                            views pass actual Sun offset. Phase D2.\n        extra_shell_reach_au (float): L-385. The reach of shells the caller\n                            draws itself, outside this dispatch (the Sun's\n                            asteroid belts), so they count as shells drawn.\n\n    Returns:\n"),
        ('\n    outermost_radius_au = 0.0\n    # D3.1 follow-up (May 2026, Bug 1): track whether any custom shell was\n    # rendered, so the Sun Direction indicator can fall back to a body-radius\n',
         "\n    outermost_radius_au = 0.0\n    # L-385: the farthest shell drawn, sphere or custom, measured from the\n    # geometry for a custom shell. Sets the opening view and the length of\n    # the center body's axis and cone.\n    shells_reach_au = max(0.0, extra_shell_reach_au or 0.0)\n    from shared_utilities import traces_extent_from_center\n    # D3.1 follow-up (May 2026, Bug 1): track whether any custom shell was\n    # rendered, so the Sun Direction indicator can fall back to a body-radius\n"),
        ("                shell_r = config['radius_fraction'] * body_r\n            outermost_radius_au = max(outermost_radius_au, shell_r)\n\n        elif shell_name in customs and shell_name not in ('rotation_axis', 'dipole_cone'):\n",
         "                shell_r = config['radius_fraction'] * body_r\n            outermost_radius_au = max(outermost_radius_au, shell_r)\n            shells_reach_au = max(shells_reach_au, shell_r)\n\n        elif shell_name in customs and shell_name not in ('rotation_axis', 'dipole_cone'):\n"),
        ('            for t in traces:\n                fig.add_trace(t)\n            # D3.1 follow-up (May 2026, Bug 1): mark that a custom shell was\n            # rendered, so the post-loop fallback can pick a sensible indicator\n',
         '            for t in traces:\n                fig.add_trace(t)\n            shells_reach_au = max(shells_reach_au,\n                                  traces_extent_from_center(list(traces),\n                                                            center_position))\n            # D3.1 follow-up (May 2026, Bug 1): mark that a custom shell was\n            # rendered, so the post-loop fallback can pick a sensible indicator\n'),
        ("    # pole line) and toggles as a unit, so the user can still hide it via the\n    # legend. Only the 11 bodies with a sourced spin pole have this entry.\n    if 'rotation_axis' in customs:\n        axis_custom = customs['rotation_axis']\n        axis_mod_path, axis_func = axis_custom['builder'].rsplit('.', 1)\n        axis_builder = getattr(importlib.import_module(axis_mod_path), axis_func)\n        for t in axis_builder(center_position, planet_name=body_name):\n            if animate:\n                _append_inertial_note(t)\n",
         '    # pole line) and toggles as a unit, so the user can still hide it via the\n    # legend. Only the 11 bodies with a sourced spin pole have this entry.\n    # L-385 (Tony, 2026-10-19, "Confirmed as recommended"): for the plot\'s\n    # center body the axis and the dipole cone end just past the farthest\n    # shell drawn, never longer than their half_len_frac, so their tips and\n    # hover markers sit inside the opening view. Other bodies keep their\n    # length, as the animation engine draws them. axis_reach is a rendering\n    # setting, chosen so the spin arrow at the tip also stays inside the\n    # view\'s margin (auto_cube_half_width).\n    axis_reach = 1.1\n    _axis_cap = None\n    if center_object == body_name and shells_reach_au > 0:\n        _axis_cap = axis_reach * shells_reach_au\n    if \'rotation_axis\' in customs:\n        axis_custom = customs[\'rotation_axis\']\n        axis_mod_path, axis_func = axis_custom[\'builder\'].rsplit(\'.\', 1)\n        axis_builder = getattr(importlib.import_module(axis_mod_path), axis_func)\n        for t in axis_builder(center_position, planet_name=body_name,\n                              max_half_len_au=_axis_cap):\n            if animate:\n                _append_inertial_note(t)\n'),
        ("        dc_mod_path, dc_func = dc_custom['builder'].rsplit('.', 1)\n        dc_builder = getattr(importlib.import_module(dc_mod_path), dc_func)\n        for t in dc_builder(center_position, planet_name=body_name):\n            if animate:\n                _append_inertial_note(t)\n",
         "        dc_mod_path, dc_func = dc_custom['builder'].rsplit('.', 1)\n        dc_builder = getattr(importlib.import_module(dc_mod_path), dc_func)\n        for t in dc_builder(center_position, planet_name=body_name,\n                            max_half_len_au=_axis_cap):\n            if animate:\n                _append_inertial_note(t)\n"),
        ('    # the cube to it would shrink Earth to a speck (0.0012 AU against\n    # 0.00016 AU with the crust alone) and it shows either way.\n    try:\n        from shared_utilities import traces_extent_from_center\n        _feat_ext = traces_extent_from_center(\n            list(fig.data)[_dispatch_start_idx:], center_position)\n',
         "    # the cube to it would shrink Earth to a speck (0.0012 AU against\n    # 0.00016 AU with the crust alone) and it shows either way.\n    if shells_reach_au > 0:\n        if not hasattr(fig, '_body_shell_reach_au'):\n            fig._body_shell_reach_au = {}\n        if shells_reach_au > fig._body_shell_reach_au.get(body_name, 0.0):\n            fig._body_shell_reach_au[body_name] = shells_reach_au\n    try:\n        _feat_ext = traces_extent_from_center(\n            list(fig.data)[_dispatch_start_idx:], center_position)\n"),
        ('    # create_earth_magnetosphere_shell). The fallback only triggers when no\n    # sphere shell was rendered AND at least one custom shell was rendered.\n    if outermost_radius_au == 0 and custom_rendered and body_name in CENTER_BODY_RADII:\n        body_r_au = CENTER_BODY_RADII[body_name] / KM_PER_AU\n        outermost_radius_au = 100.0 * body_r_au\n\n    if outermost_radius_au > 0 and not (skip_elements\n',
         "    # create_earth_magnetosphere_shell). The fallback only triggers when no\n    # sphere shell was rendered AND at least one custom shell was rendered.\n    # L-385 (2026-10-19): the fallback is now the custom shells' measured\n    # reach. The 100-body-radii guess set Earth's opening view to 200 Earth\n    # radii with low orbit alone, and drew the arrow 115 radii long.\n    if outermost_radius_au == 0 and custom_rendered:\n        outermost_radius_au = shells_reach_au\n\n    if outermost_radius_au > 0 and not (skip_elements\n"),
        ("        if axis_range is None and center_object == body_name:\n            _half = auto_cube_half_width(\n                outermost_radius_au,\n                getattr(fig, '_body_feature_extent_au', {}).get(body_name, 0.0))\n            if _half > 0:\n",
         "        if axis_range is None and center_object == body_name:\n            _half = auto_cube_half_width(\n                shells_reach_au,\n                getattr(fig, '_body_feature_extent_au', {}).get(body_name, 0.0))\n            if _half > 0:\n"),
        ('    # multi-body plot sizes each Fly To target correctly.\n    try:\n        from shared_utilities import traces_extent_from_center\n        _body_ext = traces_extent_from_center(\n            list(fig.data)[_dispatch_start_idx:], center_position)\n',
         '    # multi-body plot sizes each Fly To target correctly.\n    try:\n        _body_ext = traces_extent_from_center(\n            list(fig.data)[_dispatch_start_idx:], center_position)\n'),
    ],
    'planet_visualization_utilities.py': [
        ("create_streamer_band_shape -- helmet-and-stalk band geometry for the\nsolar streamer belt, per-point alpha so the stalk has no visible edge)\n\nModule updated: September 22, 2026 with Anthropic's Claude Opus 5 (L-322\n",
         "create_streamer_band_shape -- helmet-and-stalk band geometry for the\nsolar streamer belt, per-point alpha so the stalk has no visible edge)\n\nModule updated: October 19, 2026 with Anthropic's Claude Opus 5.5 (L-385:\nbuild_rotation_axis_traces and build_dipole_cone_traces take\nmax_half_len_au, so the center body's axis and cone end just past the\nfarthest shell drawn; never longer than half_len_frac. Tony's ruling,\n2026-10-19.)\n\nModule updated: September 22, 2026 with Anthropic's Claude Opus 5 (L-322\n"),
        ('\ndef build_rotation_axis_traces(center_position=(0, 0, 0), planet_name=None,\n                               sun_position=None):\n    """Build the rotation-axis primitive for one body.\n\n',
         '\ndef build_rotation_axis_traces(center_position=(0, 0, 0), planet_name=None,\n                               sun_position=None, max_half_len_au=None):\n    """Build the rotation-axis primitive for one body.\n\n'),
        ('    convention never surfaces. sun_position is accepted and ignored for\n    dispatch-signature uniformity.\n\n    Bodies with no sourced spin data return [] (no axis); the omission is noted\n',
         "    convention never surfaces. sun_position is accepted and ignored for\n    dispatch-signature uniformity.\n\n    max_half_len_au (L-385, 2026-10-19): when given, the axis is drawn no\n    longer than this, never longer than half_len_frac. The dispatch passes\n    it for the plot's center body so the axis ends just past the farthest\n    shell drawn and its tip marker stays inside the opening view. None\n    (the default, and every per-frame engine call) keeps half_len_frac.\n\n    Bodies with no sourced spin data return [] (no axis); the omission is noted\n"),
        ("    body_r_au = CENTER_BODY_RADII.get(planet_name, 0.0) / KM_PER_AU\n    half = info.get('half_len_frac', 2.0) * body_r_au\n    if half <= 0:\n        return []\n",
         "    body_r_au = CENTER_BODY_RADII.get(planet_name, 0.0) / KM_PER_AU\n    half = info.get('half_len_frac', 2.0) * body_r_au\n    if max_half_len_au is not None and max_half_len_au > 0:\n        half = min(half, max_half_len_au)   # L-385: shorter, never longer\n    if half <= 0:\n        return []\n"),
        ('\ndef build_dipole_cone_traces(center_position=(0, 0, 0), planet_name=None,\n                             sun_position=None):\n    """Build the magnetic dipole-cone primitive for one body (Movement 2).\n\n',
         '\ndef build_dipole_cone_traces(center_position=(0, 0, 0), planet_name=None,\n                             sun_position=None, max_half_len_au=None):\n    """Build the magnetic dipole-cone primitive for one body (Movement 2).\n\n'),
        ("    tilt (intentional omission, not a failure). sun_position is accepted and\n    ignored for dispatch-signature uniformity with the other shared builders.\n\n    Module updated: June 2026 with Anthropic's Claude Opus 4.8.\n",
         "    tilt (intentional omission, not a failure). sun_position is accepted and\n    ignored for dispatch-signature uniformity with the other shared builders.\n    max_half_len_au (L-385, 2026-10-19) caps the cone's length exactly as it\n    caps the rotation axis's, so the two stay the same length.\n\n    Module updated: June 2026 with Anthropic's Claude Opus 4.8.\n"),
        ("    body_r_au = CENTER_BODY_RADII.get(planet_name, 0.0) / KM_PER_AU\n    half = rot.get('half_len_frac', 2.5) * body_r_au\n    if half <= 0:\n        return []\n",
         "    body_r_au = CENTER_BODY_RADII.get(planet_name, 0.0) / KM_PER_AU\n    half = rot.get('half_len_frac', 2.5) * body_r_au\n    if max_half_len_au is not None and max_half_len_au > 0:\n        half = min(half, max_half_len_au)   # L-385: shorter, never longer\n    if half <= 0:\n        return []\n"),
    ],
}


def read(rel):
    path = os.path.join(ROOT, rel)
    with open(path, 'rb') as f:
        raw = f.read()
    was_crlf = b'\r\n' in raw
    return raw.replace(b'\r\n', b'\n').decode('utf-8'), was_crlf


def fingerprint(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def main():
    texts, crlf, out = {}, {}, {}
    try:
        for rel in FINGERPRINTS:
            if not os.path.exists(os.path.join(ROOT, rel)):
                raise RuntimeError('ERROR: %s not found beside this script. '
                                   'Save the script in the orrery folder.' % rel)
            texts[rel], crlf[rel] = read(rel)
            if fingerprint(texts[rel]) != FINGERPRINTS[rel]:
                raise RuntimeError('ERROR: %s is not the file at %s; this patch '
                                   'was built against that commit.' % (rel, SHA))
        for rel, edits in EDITS.items():
            s = texts[rel]
            for k, (old, new) in enumerate(reversed(edits), 1):
                n = s.count(old)
                if n != 1:
                    raise RuntimeError('ANCHOR FAIL: %s, edit %d from the bottom, '
                                       'found %d times' % (rel, k, n))
                s = s.replace(old, new)
            if fingerprint(s) != RESULTS[rel]:
                raise RuntimeError('ERROR: %s did not come out as tested.' % rel)
            if any(ord(ch) > 127 for ch in s):
                raise RuntimeError('ERROR: %s would hold non-ASCII text.' % rel)
            out[rel] = s
    except RuntimeError as e:
        print(e)
        print('NOTHING was written.')
        print('Undo is not needed. Discard Changes in GitHub Desktop restores '
              'any file you changed by hand.')
        sys.exit(1)
    for rel, s in out.items():
        with open(os.path.join(ROOT, rel), 'w', encoding='utf-8', newline='') as f:
            f.write(s)
        print('ok  %s  (%d edits; module docstring stamped October 19, 2026)'
              % (rel, len(EDITS[rel])))
        if crlf[rel]:
            print('note: %s was CRLF in the working copy; written LF' % rel)
    print('patch applied (3 files).')
    print('Next: open the orrery, center on the Sun, tick only the photosphere,')
    print('Auto scale, and plot. Then Earth. Undo is Discard Changes in GitHub Desktop.')


if __name__ == '__main__':
    main()
