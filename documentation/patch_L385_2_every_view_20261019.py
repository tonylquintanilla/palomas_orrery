#!/usr/bin/env python3
"""
patch_L385_2_every_view_20261019.py -- the orrery's opening views
(L-385), part 2: every view, still and animated, opens on the farthest
thing drawn, shell or orbit, plus 20 percent.

Built on orrery 6e0cfacd0b6aa42cb09b0ca765be94e68aab6f70 at
https://github.com/tonylquintanilla/palomas_orrery ("L455 earth
numbers") WITH patch_L385_1_opening_views_20261019.py applied, which you
ran this morning. The website is not touched (gallery 4fc320fa at
https://github.com/tonylquintanilla/tonyquintanilla.github.io).
Tony's orrery folder:
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
Written October 19, 2026 with Anthropic's Claude Opus 5.5.

RUN COMMAND

    python patch_L385_2_every_view_20261019.py

    Saved in the ORRERY folder above. Open it in VS Code and click Run.
    It takes no arguments and asks no questions.

WHAT IT DOES, all or nothing. palomas_orrery.py must be as patch 1 left
it, and test_orbit_markers.py as it is at 6e0cfacd:

    palomas_orrery.py      one margin, 20 percent, at every scale (it was
                           50, 30, 20 or 10 percent); the still plot takes
                           the larger of the shells and the orbits, as the
                           animation does; with nothing orbiting, the
                           shells alone size the view, not the 1 AU
                           default; a moon counts only when it is plotted;
                           the animation's Sun arrow is clamped to the
                           view it opens on
    test_orbit_markers.py  its frame check expects the one margin

If either file differs from what this was built against, it refuses
and writes nothing.

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
FINGERPRINTS = {'palomas_orrery.py': '96b1e8c0cf39dc2e5c70de914fe89cd2', 'test_orbit_markers.py': 'e91f712fa7b962f6f8741e3f007b2749'}
RESULTS = {'palomas_orrery.py': '009ebe038d99c280ce8b308ebbaf283f', 'test_orbit_markers.py': '907635284b634ba934cfb5df96242cf4'}

EDITS = {
    'palomas_orrery.py': [
        ('the Auto view of a center body opens on its farthest shell drawn plus 20\npercent, read from the dispatch\'s fig._body_shell_reach_au; the Sun\'s\nasteroid belts count as shells drawn. Tony\'s rule, 2026-10-18.)\n\n"""\n',
         'the Auto view of a center body opens on its farthest shell drawn plus 20\npercent, read from the dispatch\'s fig._body_shell_reach_au; the Sun\'s\nasteroid belts count as shells drawn. Tony\'s rule, 2026-10-18. Then\nevery view, still and animated, opens on the farthest thing drawn, shell\nor orbit, with that one margin at every scale; with nothing orbiting,\nthe shells alone size the view, not the 1 AU default, and the\nanimation\'s Sun arrow is clamped to that view. Tony, 2026-10-19.)\n\n"""\n'),
        ('\ndef calculate_axis_range_from_orbits(selected_objects, positions, planetary_params, \n                                    parent_planets, center_object_name):\n    """\n    Calculate appropriate axis range based on orbital parameters.\n    Uses semi-major axis data when available, falls back to position data.\n    \n    Parameters:\n        selected_objects: List of selected object dictionaries\n        positions: Dictionary of current object positions  \n        planetary_params: Dictionary from idealized_orbits.py containing orbital parameters\n        parent_planets: Dictionary mapping planets to their moons\n        center_object_name: Name of the center object\n    \n    Returns:\n        list: [min_range, max_range] for axis scaling\n    """\n\n    # Special case: Pluto-Charon Barycenter centered view\n',
         '\ndef calculate_axis_range_from_orbits(selected_objects, positions, planetary_params, \n                                    parent_planets, center_object_name,\n                                    none_if_empty=False):\n    """\n    Calculate appropriate axis range based on orbital parameters.\n    Uses semi-major axis data when available, falls back to position data.\n\n    L-385 (Tony, 2026-10-19, "confirmed as recommended"): every view opens\n    on the farthest thing drawn plus 20 percent, in the still plot and the\n    animation alike. So the margin is one setting, view_margin, where it\n    was 1.5, 1.3, 1.2 or 1.1 by scale, and 1.5 for a barycentre\'s\n    children. With none_if_empty=True the function returns None when\n    nothing orbits, so a caller with shells drawn sizes the view from the\n    shells alone instead of from the 1 AU default.\n    \n    Parameters:\n        selected_objects: List of selected object dictionaries\n        positions: Dictionary of current object positions  \n        planetary_params: Dictionary from idealized_orbits.py containing orbital parameters\n        parent_planets: Dictionary mapping planets to their moons\n        center_object_name: Name of the center object\n    \n    Returns:\n        list: [min_range, max_range] for axis scaling, or None when\n        none_if_empty is True and no orbit was found\n    """\n    # A rendering setting: it frames the drawing and moves nothing in it\n    # (L-385). Written here because test_orbit_markers.py compiles this\n    # function on its own.\n    view_margin = 1.2\n\n    # Special case: Pluto-Charon Barycenter centered view\n'),
        ('        if not has_non_children:\n            child_distances = []\n            for child_name in children:\n                if child_name in planetary_params:\n                    child_params = planetary_params[child_name]\n                    child_a = child_params.get(\'a\', 0)\n                    child_e = child_params.get(\'e\', 0)\n                    if child_a > 0:\n                        child_apoapsis = child_a * (1 + child_e)\n                        child_distances.append(child_apoapsis)\n                        print(f"[SCALING] {center_object_name} child \'{child_name}\': a={child_a:.6f} AU, apoapsis={child_apoapsis:.6f} AU", flush=True)\n            \n            if child_distances:\n                max_range = max(child_distances) * 1.5  # 1.5x buffer for comfortable viewing\n                print(f"[SCALING] {center_object_name} mode: using range +/-{max_range:.6f} AU (based on children\'s orbits)", flush=True)\n                return [-max_range, max_range]\n',
         '        if not has_non_children:\n            child_distances = []\n            # L-385 (2026-10-19): only the children that are plotted. Every\n            # child used to count, so Earth with only its crust ticked\n            # opened on the Moon\'s orbit, which was not drawn.\n            for child_name in [c for c in children if c in selected_names]:\n                if child_name in planetary_params:\n                    child_params = planetary_params[child_name]\n                    child_a = child_params.get(\'a\', 0)\n                    child_e = child_params.get(\'e\', 0)\n                    if child_a > 0:\n                        child_apoapsis = child_a * (1 + child_e)\n                        child_distances.append(child_apoapsis)\n                        print(f"[SCALING] {center_object_name} child \'{child_name}\': a={child_a:.6f} AU, apoapsis={child_apoapsis:.6f} AU", flush=True)\n            \n            if child_distances:\n                max_range = max(child_distances) * view_margin  # L-385: was 1.5\n                print(f"[SCALING] {center_object_name} mode: using range +/-{max_range:.6f} AU (based on children\'s orbits)", flush=True)\n                return [-max_range, max_range]\n'),
        ('        max_range = max(max_distances)\n        \n        # Add appropriate buffer based on the scale\n        if max_range < 0.1:  # Very small systems (satellite systems)\n            buffer_factor = 1.5\n        elif max_range < 10:  # Inner solar system\n            buffer_factor = 1.3\n        elif max_range < 100:  # Outer solar system\n            buffer_factor = 1.2\n        else:  # Very distant objects\n            buffer_factor = 1.1\n            \n        max_range_with_buffer = max_range * buffer_factor\n        axis_range = [-max_range_with_buffer, max_range_with_buffer]\n        \n        print(f"\\nAutomatic scaling calculation:", flush=True)\n        print(f"  Maximum orbital distance: {max_range:.6f} AU", flush=True)\n        print(f"  Buffer factor: {buffer_factor}", flush=True)\n        print(f"  Final axis range: +/-{max_range_with_buffer:.6f} AU", flush=True)\n        \n        return axis_range\n    else:\n        # Fallback to default range if no orbital data available\n        print("No orbital data available, using default range", flush=True)\n        return [-1, 1]\n',
         '        max_range = max(max_distances)\n        \n        # L-385: one margin at every scale. It was 1.5 below 0.1 AU, 1.3\n        # below 10 AU, 1.2 below 100 AU and 1.1 beyond.\n        buffer_factor = view_margin\n\n        max_range_with_buffer = max_range * buffer_factor\n        axis_range = [-max_range_with_buffer, max_range_with_buffer]\n        \n        print(f"\\nAutomatic scaling calculation:", flush=True)\n        print(f"  Maximum orbital distance: {max_range:.6f} AU", flush=True)\n        print(f"  Buffer factor: {buffer_factor}", flush=True)\n        print(f"  Final axis range: +/-{max_range_with_buffer:.6f} AU", flush=True)\n        \n        return axis_range\n    else:\n        # Fallback to default range if no orbital data available\n        if none_if_empty:\n            print("No orbital data available; the view is sized by what else is drawn", flush=True)\n            return None\n        print("No orbital data available, using default range", flush=True)\n        return [-1, 1]\n'),
        ('            return [-1, 1]\n        \ndef get_animation_axis_range(scale_var, custom_scale_entry, objects, planetary_params, parent_planets, center_object_name):\n    """\n    Get axis range for animations using the same logic as static plots.\n    This ensures consistency between plot_objects() and animate_objects().\n    """\n    if scale_var.get() == \'Auto\':\n        # Use the same orbital-based scaling as plot_objects()\n        selected_objects = [obj for obj in objects if obj[\'var\'].get() == 1]\n        \n        return calculate_axis_range_from_orbits(\n            selected_objects, {}, planetary_params, \n            parent_planets, center_object_name\n        )\n    else:\n',
         '            return [-1, 1]\n        \ndef get_animation_axis_range(scale_var, custom_scale_entry, objects, planetary_params, parent_planets, center_object_name,\n                             none_if_empty=False):\n    """\n    Get axis range for animations using the same logic as static plots.\n    This ensures consistency between plot_objects() and animate_objects().\n    none_if_empty (L-385): passed through; None when nothing orbits.\n    """\n    if scale_var.get() == \'Auto\':\n        # Use the same orbital-based scaling as plot_objects()\n        selected_objects = [obj for obj in objects if obj[\'var\'].get() == 1]\n        \n        return calculate_axis_range_from_orbits(\n            selected_objects, {}, planetary_params, \n            parent_planets, center_object_name,\n            none_if_empty=none_if_empty\n        )\n    else:\n'),
        ("        # planet path). L-322 Stage D, patch D4: was 2x the outermost\n        # sphere shell only.\n        if scale_value == 'Auto':\n            shell_r = _auto_center_half_range(fig, 'Sun')\n            if shell_r > 0:\n                axis_range = [-shell_r, shell_r]\n        # Asteroid belts: standalone geometry, not part of unified shell\n",
         "        # planet path). L-322 Stage D, patch D4: was 2x the outermost\n        # sphere shell only.\n        # L-385 (2026-10-19): the larger of the shells and the orbits\n        # already in axis_range, so a plotted planet stays in view.\n        if scale_value == 'Auto':\n            shell_r = _auto_center_half_range(fig, 'Sun')\n            if shell_r > 0:\n                if axis_range is not None:\n                    shell_r = max(shell_r, abs(axis_range[1]))\n                axis_range = [-shell_r, shell_r]\n        # Asteroid belts: standalone geometry, not part of unified shell\n"),
        ('                shell_r = _auto_center_half_range(fig, center_object_name)\n                if shell_r > 0:\n                    axis_range = [-shell_r, shell_r]\n\n',
         '                shell_r = _auto_center_half_range(fig, center_object_name)\n                if shell_r > 0:\n                    # L-385: the larger of the shells and the orbits.\n                    if axis_range is not None:\n                        shell_r = max(shell_r, abs(axis_range[1]))\n                    axis_range = [-shell_r, shell_r]\n\n'),
        ('\n\ndef _animate_axis_range_hint(center_object_name):\n    """(Phase 4, O12) The animation\'s axis range, computed from the same\n    inputs the downstream computation uses (a pure function of GUI state\n    and selections), so the sun-direction indicator can be clamped to the\n    visible cube at allocation time -- the animate pipeline otherwise\n    derives its range from ORBITAL extent, which can be smaller than the\n    indicator\'s shell-scaled length (the O12 clip). None on any failure;\n    the clamp is then simply skipped."""\n    try:\n        return get_animation_axis_range(scale_var, custom_scale_entry,\n                                        objects, planetary_params,\n                                        parent_planets, center_object_name)\n    except Exception:\n        return None\n',
         '\n\ndef _animate_axis_range_hint(center_object_name, center_shell_range=None):\n    """(Phase 4, O12) The animation\'s axis range, computed from the same\n    inputs the downstream computation uses (a pure function of GUI state\n    and selections), so the sun-direction indicator can be clamped to the\n    visible cube at allocation time -- the animate pipeline otherwise\n    derives its range from ORBITAL extent, which can be smaller than the\n    indicator\'s shell-scaled length (the O12 clip). None on any failure;\n    the clamp is then simply skipped.\n\n    L-385 (2026-10-19): the hint is the view the animation will open on,\n    the larger of the orbits and the center body\'s shells\n    (center_shell_range, from add_center_body_shells), so the arrow is\n    clamped inside the view that is actually drawn. With nothing orbiting\n    it was the 1 AU default, which let the arrow run past a shells-only\n    view."""\n    try:\n        _orbit = get_animation_axis_range(scale_var, custom_scale_entry,\n                                          objects, planetary_params,\n                                          parent_planets, center_object_name,\n                                          none_if_empty=True)\n        if center_shell_range is not None:\n            _half = abs(center_shell_range[1])\n            if _orbit is not None:\n                _half = max(_half, abs(_orbit[1]))\n            return [-_half, _half]\n        return _orbit if _orbit is not None else [-1, 1]\n    except Exception:\n        return None\n'),
        ('\ndef collect_perframe_elements(center_object_name, candidate_body_names,\n                              center_shell_radius_au=None):\n    """(Phase 3) Element specs for engine-animatable primitives.\n\n',
         '\ndef collect_perframe_elements(center_object_name, candidate_body_names,\n                              center_shell_radius_au=None,\n                              center_shell_range=None):\n    """(Phase 3) Element specs for engine-animatable primitives.\n\n'),
        ('    # (Phase 4, O12) One range hint for every indicator spec this call\n    # produces -- the clamp input for create_sun_direction_indicator.\n    _range_hint = _animate_axis_range_hint(center_object_name)\n    planet_map = get_planet_shell_vars_map()\n    for body in candidate_body_names:\n',
         '    # (Phase 4, O12) One range hint for every indicator spec this call\n    # produces -- the clamp input for create_sun_direction_indicator.\n    _range_hint = _animate_axis_range_hint(center_object_name,\n                                           center_shell_range)  # L-385\n    planet_map = get_planet_shell_vars_map()\n    for body in candidate_body_names:\n'),
        ("                selected_objects = [obj for obj in objects if obj['var'].get() == 1]\n\n                axis_range = calculate_axis_range_from_orbits(\n            #        selected_objects, positions, planetary_params, \n                    selected_objects, positions, active_planetary_params,\n\n                    parent_planets, center_object_name\n    )\n\n",
         "                selected_objects = [obj for obj in objects if obj['var'].get() == 1]\n\n                # L-385: None when nothing orbits, so the shells alone can\n                # size the view; the 1 AU default is applied after them.\n                axis_range = calculate_axis_range_from_orbits(\n            #        selected_objects, positions, planetary_params, \n                    selected_objects, positions, active_planetary_params,\n\n                    parent_planets, center_object_name, none_if_empty=True\n    )\n\n"),
        ('                get_planet_shell_vars_map(), _sun_pos_tuple,\n                scale_var.get(), axis_range)\n\n            # (2a) The explicit center-marker block that lived here was REMOVED.\n',
         '                get_planet_shell_vars_map(), _sun_pos_tuple,\n                scale_var.get(), axis_range)\n            if axis_range is None:\n                # L-385: nothing orbits and no shell is drawn.\n                print("No orbit or shell to size the view; using default range", flush=True)\n                axis_range = [-1, 1]\n\n            # (2a) The explicit center-marker block that lived here was REMOVED.\n'),
        ("                center_object_name, list(positions_over_time.keys()),\n                center_shell_radius_au=getattr(\n                    fig, '_shell_outermost_radius_au', None))\n            _engine_sun_traj = positions_over_time.get('Sun')\n            if (_engine_sun_traj is None\n",
         "                center_object_name, list(positions_over_time.keys()),\n                center_shell_radius_au=getattr(\n                    fig, '_shell_outermost_radius_au', None),\n                center_shell_range=_shell_axis_range)  # L-385\n            _engine_sun_traj = positions_over_time.get('Sun')\n            if (_engine_sun_traj is None\n"),
        ('            #            scale_var, custom_scale_entry, objects, planetary_params, \n                        scale_var, custom_scale_entry, objects, active_planetary_params,\n                        parent_planets, center_object_name\n                    )\n            else:\n                axis_range = get_animation_axis_range(\n            #        scale_var, custom_scale_entry, objects, planetary_params, \n                    scale_var, custom_scale_entry, objects, active_planetary_params,\n                    parent_planets, center_object_name\n                )\n\n            # (Session C) Auto scale honors center-shell extent: the cube must\n            # hold BOTH the orbital extent and the shells -- the larger of the\n            # two, never shell extent alone (that is the Finding-1 photosphere\n            # collapse). _shell_axis_range is non-None only under Auto with\n            # center shells rendered (add_center_body_shells); manual scale is\n            # therefore never overridden here.\n            if _shell_axis_range is not None and axis_range is not None:\n                _half = max(abs(axis_range[1]), abs(_shell_axis_range[1]))\n                axis_range = [-_half, _half]\n\n            # Manual grid spacing (dtick) override -- item 19.3. Blank/0 -> None\n',
         '            #            scale_var, custom_scale_entry, objects, planetary_params, \n                        scale_var, custom_scale_entry, objects, active_planetary_params,\n                        parent_planets, center_object_name, none_if_empty=True\n                    )\n            else:\n                axis_range = get_animation_axis_range(\n            #        scale_var, custom_scale_entry, objects, planetary_params, \n                    scale_var, custom_scale_entry, objects, active_planetary_params,\n                    parent_planets, center_object_name, none_if_empty=True\n                )\n\n            # (Session C) Auto scale honors center-shell extent: the cube must\n            # hold BOTH the orbital extent and the shells -- the larger of the\n            # two, never shell extent alone (that is the Finding-1 photosphere\n            # collapse). _shell_axis_range is non-None only under Auto with\n            # center shells rendered (add_center_body_shells); manual scale is\n            # therefore never overridden here.\n            if _shell_axis_range is not None and axis_range is not None:\n                _half = max(abs(axis_range[1]), abs(_shell_axis_range[1]))\n                axis_range = [-_half, _half]\n            elif axis_range is None:\n                # L-385 (2026-10-19): nothing orbits. The shells alone size\n                # the view, where the 1 AU default used to win; with no\n                # shells either, the default stays.\n                axis_range = (list(_shell_axis_range) if _shell_axis_range is not None\n                              else [-1, 1])\n\n            # Manual grid spacing (dtick) override -- item 19.3. Blank/0 -> None\n'),
    ],
    'test_orbit_markers.py': [
        ('at all while its orbit is drawn around the barycentre; the judge and its\nplanted fault say so, and Mercury must keep its comparison.)\n"""\nimport contextlib\n',
         'at all while its orbit is drawn around the barycentre; the judge and its\nplanted fault say so, and Mercury must keep its comparison.)\nModule updated: October 19, 2026 with Anthropic\'s Claude Opus 5.5 (L-385:\nthe frame judge expects the one margin every view now opens with, 1.2,\nfor Sedna and for Mercury alike.)\n"""\nimport contextlib\n'),
        ('    """The plot\'s frame is sized from the ellipses as drawn: Sedna\'s far end\n    is its barycentre aphelion moved by the barycentre\'s place (worked out\n    here), times the 1.1 margin the orrery gives beyond 100 au."""\n    if orrery_source is None:\n        with open(os.path.join(HERE, \'palomas_orrery.py\'), encoding=\'utf-8\') as f:\n            orrery_source = f.read()\n    fn = _axis_range_function(orrery_source)\n    el, off = DRAWN[\'Sedna\']\n    far = math.sqrt(sum((a + b) ** 2 for a, b in zip(at_anomaly(el, 180.0), off)))\n    with cache_is(fixture_cache()), contextlib.redirect_stdout(io.StringIO()):\n        rng = fn([{\'name\': \'Sedna\'}], {}, {\'Sedna\': dict(SEDNA)}, parent_planets, \'Sun\')\n    counts[\'frames\'] += 1\n    if abs(rng[1] - 1.1 * far) > 1e-6 * far:\n        findings.append((\'FRAME SIZED FROM ANOTHER ORBIT\',\n                         "the frame reaches %.2f au; Sedna\'s drawn ellipse ends %.2f au from the "\n                         \'Sun, so it should reach %.2f\' % (rng[1], far, 1.1 * far)))\n    # A body drawn as fetched keeps a(1+e).\n    with cache_is(fixture_cache()), contextlib.redirect_stdout(io.StringIO()):\n        rng = fn([{\'name\': \'Mercury\'}], {}, {\'Mercury\': dict(MERCURY)}, parent_planets, \'Sun\')\n    want = 1.3 * MERCURY[\'a\'] * (1 + MERCURY[\'e\'])\n    counts[\'frames\'] += 1\n    if abs(rng[1] - want) > 1e-9:\n',
         '    """The plot\'s frame is sized from the ellipses as drawn: Sedna\'s far end\n    is its barycentre aphelion moved by the barycentre\'s place (worked out\n    here), times the view\'s margin, 1.2 at every scale since L-385\n    (2026-10-19; it was 1.1 beyond 100 au and 1.3 below 10 au)."""\n    margin = 1.2\n    if orrery_source is None:\n        with open(os.path.join(HERE, \'palomas_orrery.py\'), encoding=\'utf-8\') as f:\n            orrery_source = f.read()\n    fn = _axis_range_function(orrery_source)\n    el, off = DRAWN[\'Sedna\']\n    far = math.sqrt(sum((a + b) ** 2 for a, b in zip(at_anomaly(el, 180.0), off)))\n    with cache_is(fixture_cache()), contextlib.redirect_stdout(io.StringIO()):\n        rng = fn([{\'name\': \'Sedna\'}], {}, {\'Sedna\': dict(SEDNA)}, parent_planets, \'Sun\')\n    counts[\'frames\'] += 1\n    if abs(rng[1] - margin * far) > 1e-6 * far:\n        findings.append((\'FRAME SIZED FROM ANOTHER ORBIT\',\n                         "the frame reaches %.2f au; Sedna\'s drawn ellipse ends %.2f au from the "\n                         \'Sun, so it should reach %.2f\' % (rng[1], far, margin * far)))\n    # A body drawn as fetched keeps a(1+e).\n    with cache_is(fixture_cache()), contextlib.redirect_stdout(io.StringIO()):\n        rng = fn([{\'name\': \'Mercury\'}], {}, {\'Mercury\': dict(MERCURY)}, parent_planets, \'Sun\')\n    want = margin * MERCURY[\'a\'] * (1 + MERCURY[\'e\'])\n    counts[\'frames\'] += 1\n    if abs(rng[1] - want) > 1e-9:\n'),
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
                                   'was built against that commit with patch 1 applied.' % (rel, SHA))
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
        print('ok  %s  (%d edits; docstring stamp for October 19, 2026 extended or added)'
              % (rel, len(EDITS[rel])))
        if crlf[rel]:
            print('note: %s was CRLF in the working copy; written LF' % rel)
    print('patch applied (2 files).')
    print('Next: plot the Sun with only the photosphere and Earth ticked as an object,')
    print('Auto scale. Then the same as an animation. Undo is Discard Changes in GitHub Desktop.')


if __name__ == '__main__':
    main()
