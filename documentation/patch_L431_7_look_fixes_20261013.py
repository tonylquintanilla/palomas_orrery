"""patch_L431_7_look_fixes_20261013.py -- L-431 (orbital periods from
JPL), after build 2's look: the three things Tony's saved plot showed,
fixed, and the records closed on the look he accepted.

Built on orrery 87a54704ab2cba6d3fbfa5cbb4c3adb698a53a02 at
https://github.com/tonylquintanilla/palomas_orrery ("v3.93").
The gallery is not touched.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\;
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\.
Written October 13, 2026 with Anthropic's Claude Opus 5.5.
Record: documentation/HANDOFF_L431_build2_look_fixes_20261013.md
(created by this patch).

HOW TO RUN
    From the orrery repo's ROOT folder: open this file in VS Code and
    press Run, or from a terminal in that folder:
        python patch_L431_7_look_fixes_20261013.py
    Success prints one "ok" line per edit, then "patch applied", then
    the three fixes by name. It asks nothing and fetches nothing.

WHAT IT CHANGES
    idealized_orbits.py: the perihelion osculating orbit's hover (Encke's
      white arc) carries the accuracy sentence under its distances; the
      perturbation block says when it compares the Sun-centred elements
      while the drawn orbit is around another centre (Sedna).
    orbital_period.py: drawn_aphelion_distance(), how far a drawn
      ellipse moved to another centre reaches from the plot's centre.
    palomas_orrery.py: calculate_axis_range_from_orbits, shared by the
      static plot and the animation, sizes the frame from it.
    test_orbit_markers.py: three judges and three planted faults for
      the above, twelve in all.
    palomas_orrery_dashboard.py: Orbit Markers' description says twelve.
    LEDGER_CONSOLIDATED.md: L-431 and L-401, the look accepted and the
      fixes; the stamp. documentation/WHERE_WE_ARE.md, by section, never
      below the run-record marker.
    Created: the handoff.
    Every edited module's docstring stamp moves with it. No skill and no
    protocol version changes.

SAFETY
    Each file is checked only at the lines this patch edits: every anchor
    must match exactly once, and no edit lands below the run-record
    marker, so your notes cannot make it refuse. A file this patch
    creates must not exist yet. If any check fails, NOTHING is written.
    A file found with Windows line endings is matched after turning them
    into LF and written back LF, and the patch says so. Undo after a run
    is Discard Changes in GitHub Desktop, and delete the created file.
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
MARKER = '--- Your run record below this line'

EDITS = [
    ('orbital_period.py', 'line 63: _is_small_body counts a pinned record number',
     '_is_small_body counts a pinned record number as a small body whatever\nits id_type, so C/2025_K1 is asked of the Small-Body Database.)\n"""\n\n',
     '_is_small_body counts a pinned record number as a small body whatever\nits id_type, so C/2025_K1 is asked of the Small-Body Database.)\nModule updated: October 13, 2026 with Anthropic\'s Claude Opus 5.5 (L-431,\nafter build 2\'s look: drawn_aphelion_distance(), how far a drawn ellipse\nmoved to another centre reaches from the plot\'s centre, so the frame is\nsized from the orbit as drawn.)\n"""\n\n'),
    ('orbital_period.py', 'line 846: def drawn_aphelion_distance(obj_name, center',
     '\n\ndef carried_error_days(period, periods=1.0):\n    """The error a date carries from the period it was worked out from:\n',
     '\n\ndef drawn_aphelion_distance(obj_name, center_object_name, params, cache=None):\n    """\n    How far the drawn ellipse\'s aphelion is from the plot\'s centre, in AU,\n    when drawing_orbit draws the body around another centre (Sedna, around\n    the solar system\'s barycentre); None when the fetched elements are\n    drawn as they are, so the caller keeps its own a(1+e).\n\n    The plot\'s frame is sized from this (palomas_orrery.py,\n    calculate_axis_range_from_orbits): sized from the Sun-centred a(1+e),\n    Sedna\'s frame reached well past the end of its drawn ellipse (found\n    at build 2\'s look, 2026-10-13; the figures are in the handoff).\n    """\n    o = drawing_orbit(obj_name, center_object_name, params, cache=cache)\n    el = o[\'elements\']\n    if el is params or not _elements_usable(el):\n        return None\n    far = dict(el)\n    far[\'TA\'] = 180.0\n    x, y, z = position_from_elements(far)\n    dx, dy, dz = o[\'offset_au\']\n    return math.sqrt((x + dx) ** 2 + (y + dy) ** 2 + (z + dz) ** 2)\n\n\ndef carried_error_days(period, periods=1.0):\n    """The error a date carries from the period it was worked out from:\n'),
    ('idealized_orbits.py', 'line 47: Horizons as given, and every distance or spe',
     "Horizons as given, and every distance or speed it computes by the body\nhover's rule and formatter (position_accuracy).)\n\nRole: computation\n",
     "Horizons as given, and every distance or speed it computes by the body\nhover's rule and formatter (position_accuracy).)\nModule updated: October 13, 2026 with Anthropic's Claude Opus 5.5 (L-431,\nafter build 2's look: the perihelion osculating orbit's hover carries the\naccuracy sentence under its distances, as every other marker's does; and\nwhere the drawn orbit is around another centre (Sedna), the perturbation\nblock says it compares the Sun-centred elements with the mean ones and\nprints them, so its Delta-a is not read against the drawn a.)\n\nRole: computation\n"),
    ('idealized_orbits.py', 'line 219: return perturbation_notes.get(obj_name, defa',
     '    \n    return perturbation_notes.get(obj_name, default_note)\ndef get_mean_vs_osculating_assessment(obj_name, osc_params, mean_params, acc=None):\n    """\n    Compare osculating vs mean orbital elements and return perturbation assessment HTML.\n',
     '    \n    return perturbation_notes.get(obj_name, default_note)\ndef get_mean_vs_osculating_assessment(obj_name, osc_params, mean_params, acc=None,\n                                      compared_around=None):\n    """\n    Compare osculating vs mean orbital elements and return perturbation assessment HTML.\n'),
    ('idealized_orbits.py', 'line 233: osc_params (dict): Current osculating parame',
     '        osc_params (dict): Current osculating parameters (a, e, i, omega, Omega)\n        mean_params (dict): Mean parameters from orbital_elements.py\n    \n    Returns:\n',
     "        osc_params (dict): Current osculating parameters (a, e, i, omega, Omega)\n        mean_params (dict): Mean parameters from orbital_elements.py\n        compared_around (str): the centre's words, given when the drawn\n            orbit is around another centre than osc_params (L-431 build 2:\n            Sedna is drawn around the solar system's center of mass, and\n            compared around the Sun, where the mean elements are). The\n            block then names the centre and prints the elements it\n            compared, so its deltas are not read against the drawn ones.\n    \n    Returns:\n"),
    ('idealized_orbits.py', "line 289: epoch_str = mean_params.get('epoch', 'N/A')",
     '    epoch_str = mean_params.get(\'epoch\', \'N/A\')\n    \n    assessment = (\n        f"<br><br><b>Perturbation (osculating vs mean):</b>"\n        f"<br>Delta-e: {delta_e:+.8f} ({qual_e})"\n        f"{delta_a_text}"\n',
     '    epoch_str = mean_params.get(\'epoch\', \'N/A\')\n    \n    # FIXED (L-431, after build 2\'s look): when the drawn orbit is around\n    # another centre, say which elements were compared, so "+58.56 AU"\n    # is not read against the drawn a.\n    if compared_around:\n        heading = (f"<br><br><b>Perturbation (osculating vs mean, both around "\n                   f"{compared_around}):</b>"\n                   f"<br>Osculating around {compared_around}: a={_pa.as_given(osc_a)} AU, "\n                   f"e={_pa.as_given(osc_e)}")\n    else:\n        heading = f"<br><br><b>Perturbation (osculating vs mean):</b>"\n    assessment = (\n        f"{heading}"\n        f"<br>Delta-e: {delta_e:+.8f} ({qual_e})"\n        f"{delta_a_text}"\n'),
    ('idealized_orbits.py', "line 5478: 'period': {'days': None, 'err_days': None, '",
     "                          'period': {'days': None, 'err_days': None, 'kind': 'none',\n                                     'center': None, 'label': None, 'record': None}}\n            if _orbit['elements'] is not params:\n                params = dict(_orbit['elements'])\n",
     "                          'period': {'days': None, 'err_days': None, 'kind': 'none',\n                                     'center': None, 'label': None, 'record': None}}\n            # The mean elements are around the Sun, so the comparison stays\n            # there; when the drawn orbit is not, the comparison says so.\n            _compared_around = 'the Sun' if _orbit['elements'] is not params else None\n            if _orbit['elements'] is not params:\n                params = dict(_orbit['elements'])\n"),
    ('idealized_orbits.py', 'line 5862: f"i={_pa.as_given(i)} deg"',
     '                f"i={_pa.as_given(i)} deg"\n                f"{get_planet_perturbation_note(obj_name)}"\n                f"{get_mean_vs_osculating_assessment(obj_name, planetary_params[obj_name], ORIGINAL_planetary_params.get(obj_name, {}), _acc)}"\n            )\n            fig.add_trace(\n',
     '                f"i={_pa.as_given(i)} deg"\n                f"{get_planet_perturbation_note(obj_name)}"\n                f"{get_mean_vs_osculating_assessment(obj_name, planetary_params[obj_name], ORIGINAL_planetary_params.get(obj_name, {}), _acc, _compared_around)}"\n            )\n            fig.add_trace(\n'),
    ('idealized_orbits.py', 'line 7501: f"q = {_pa.km_text(_pa.accuracy_for(obj_name',
     '        f"q = {_pa.km_text(_pa.accuracy_for(obj_name, \'Sun\'), q_osc * KM_PER_AU)} (perihelion distance)<br>"\n        f"i = {_pa.as_given(i_osc)} deg"\n        f"{pert_note}"\n    )\n',
     '        f"q = {_pa.km_text(_pa.accuracy_for(obj_name, \'Sun\'), q_osc * KM_PER_AU)} (perihelion distance)<br>"\n        f"i = {_pa.as_given(i_osc)} deg"\n        # FIXED (L-401, after build 2\'s look): the distances above are\n        # printed by the digits rule, so the hover says which figure they\n        # are rounded to, as every other marker\'s does.\n        f"{_accuracy_tail(_pa.accuracy_for(obj_name, \'Sun\'))}"\n        f"{pert_note}"\n    )\n'),
    ('palomas_orrery.py', "line 88: body's position record travels with its posi",
     'body\'s position record travels with its position to the orbit drawing,\nso an orbit\'s markers print the body\'s digits (L-401\'s second slice).)\n\n"""\n',
     'body\'s position record travels with its position to the orbit drawing,\nso an orbit\'s markers print the body\'s digits (L-401\'s second slice).)\nModule updated: October 13, 2026 with Anthropic\'s Claude Opus 5.5 (L-431,\nafter build 2\'s look: calculate_axis_range_from_orbits sizes the frame\nfrom each ellipse as drawn, so Sedna\'s, drawn around the solar system\'s\ncenter of mass, frames to its 937 au far end, not the 1,004 au of its\nSun-centred elements. Both the static plot and the animation use it.)\n\n"""\n'),
    ('palomas_orrery.py', 'line 836: else:',
     '                else:\n                    aphelion = a * (1 + e)\n                    max_distances.append(abs(aphelion))  # Use abs to handle any edge cases\n                    print(f"{obj_name}: Elliptical orbit - a={a:.6f} AU, e={e:.4f}, aphelion={aphelion:.6f} AU", flush=True)\n            \n        else:\n',
     '                else:\n                    aphelion = a * (1 + e)\n                    print(f"{obj_name}: Elliptical orbit - a={a:.6f} AU, e={e:.4f}, aphelion={aphelion:.6f} AU", flush=True)\n                    # FIXED (L-431, after build 2\'s look): the frame is sized\n                    # from the ellipse as DRAWN. Sedna is drawn around the\n                    # solar system\'s center of mass, so its far end is 937 au\n                    # from the Sun, not the 1,004 of the Sun-centred elements.\n                    try:\n                        from orbital_period import drawn_aphelion_distance\n                        _drawn_far = drawn_aphelion_distance(obj_name, center_object_name, params)\n                    except Exception as _ex:\n                        print(f"[L-431 orbit] ERROR: could not size {obj_name} from its drawn "\n                              f"orbit ({_ex}); using the fetched elements", flush=True)\n                        _drawn_far = None\n                    if _drawn_far is not None:\n                        aphelion = _drawn_far\n                        print(f"{obj_name}: drawn around another centre; its drawn aphelion is "\n                              f"{aphelion:.6f} AU from the Sun", flush=True)\n                    max_distances.append(abs(aphelion))  # Use abs to handle any edge cases\n            \n        else:\n'),
    ('test_orbit_markers.py', 'line 38: the parameters window dated from a barycentr',
     "    the parameters window dated from a barycentre    PARAMETERS WINDOW PERIOD FROM ANOTHER CENTRE\n      view's period\n\nThe first four are the brief's (documentation/\n",
     "    the parameters window dated from a barycentre    PARAMETERS WINDOW PERIOD FROM ANOTHER CENTRE\n      view's period\n    the perihelion osculating orbit's hover without  DISTANCES WITHOUT THEIR ACCURACY SENTENCE\n      its accuracy sentence\n    Sedna's perturbation block not naming the        PERTURBATION COMPARED WITHOUT ITS CENTRE\n      centre it compared around\n    the plot's frame sized from the Sun-centred      FRAME SIZED FROM ANOTHER ORBIT\n      orbit while Sedna is drawn around the\n      barycentre\n\nThe first four are the brief's (documentation/\n"),
    ('test_orbit_markers.py', "line 50: next two cover the moons' marker path and th",
     "next two cover the moons' marker path and the map's one home; the last\nthree come from a cold review of the build (2026-10-12), which showed the\nfirst draft of this file could not fail on them. It also runs a record\nsaved before build 2 (Sedna stays around the Sun and says why) and the\nKeplerian position half a year after its epoch, where the period shows.\n",
     "next two cover the moons' marker path and the map's one home; the last\nthree come from a cold review of the build (2026-10-12), which showed the\nfirst draft of this file could not fail on them; the three after them\ncome from Tony's look at build 2 (2026-10-13), where the saved plot showed\neach one. It also runs a record\nsaved before build 2 (Sedna stays around the Sun and says why) and the\nKeplerian position half a year after its epoch, where the period shows.\n"),
    ('test_orbit_markers.py', 'line 80: Module created: October 12, 2026 with Anthro',
     'Module created: October 12, 2026 with Anthropic\'s Claude Opus 5.5 (L-431,\nbuild 2, with L-401\'s second slice).\n"""\nimport contextlib\n',
     'Module created: October 12, 2026 with Anthropic\'s Claude Opus 5.5 (L-431,\nbuild 2, with L-401\'s second slice).\nModule updated: October 13, 2026 with Anthropic\'s Claude Opus 5.5 (L-431,\nafter build 2\'s look: three judges and three planted faults for what the\nsaved plot showed -- the perihelion osculating orbit\'s accuracy sentence,\nSedna\'s perturbation block naming its centre, and the frame sized from\nthe drawn orbit. A whole number\'s trailing zeros are no longer called\ncoarse, since its place cannot be read from the print.)\n"""\nimport contextlib\n'),
    ('test_orbit_markers.py', 'line 111: from celestial_objects import OBJECT_DEFINIT',
     'from celestial_objects import OBJECT_DEFINITIONS\nfrom orbital_elements import parent_planets\n\n# ============================================================================\n',
     'from celestial_objects import OBJECT_DEFINITIONS\nfrom orbital_elements import parent_planets\nfrom orbital_elements import planetary_params as MEAN_ELEMENTS\n\n# ============================================================================\n'),
    ('test_orbit_markers.py', "line 438: findings.append(('DISTANCE FINER THAN ITS ER",
     "                findings.append(('DISTANCE FINER THAN ITS ERROR', '%s %s: %s %s printed to 1e%d, '\n                                 'its error earns 1e%d' % (body, where, val, unit, got, want)))\n            elif got > want:\n                findings.append(('DISTANCE COARSER THAN ITS ERROR', '%s %s: %s %s printed to 1e%d, '\n",
     "                findings.append(('DISTANCE FINER THAN ITS ERROR', '%s %s: %s %s printed to 1e%d, '\n                                 'its error earns 1e%d' % (body, where, val, unit, got, want)))\n            elif got > want and '.' not in val:\n                # A whole number's trailing zeros may be digits it earned:\n                # 50,654,699.7 km to the whole kilometer is 50,654,700.\n                # Its place cannot be read from the print, so it is not\n                # called coarse.\n                pass\n            elif got > want:\n                findings.append(('DISTANCE COARSER THAN ITS ERROR', '%s %s: %s %s printed to 1e%d, '\n"),
    ('test_orbit_markers.py', 'line 731: def judge_comparison(fig, findings, counts):',
     '\n\ndef run_checks(io_mod=None, ap_mod=None, pv_mod=None, orrery_source=None):\n    import idealized_orbits\n',
     '\n\ndef judge_comparison(fig, findings, counts):\n    """The perturbation block compares the Sun-centred osculating elements\n    with the mean ones, which are around the Sun. Where the drawn orbit is\n    around another centre (Sedna), the block must say so and print the\n    elements it compared, and its Delta-a must be their difference\n    (worked out here); where it is not, it must not claim a centre."""\n    mean_a = MEAN_ELEMENTS[\'Sedna\'][\'a\']\n    for body in (\'Sedna\', \'Mercury\', \'Encke\'):\n        tr = traces(fig, body)\n        info = tr[\'info\'].text[0] if \'info\' in tr else \'\'\n        if \'Perturbation (osculating vs mean\' not in info:\n            continue\n        counts[\'comparisons\'] += 1\n        named = \'both around the Sun\' in info\n        if body != \'Sedna\':\n            if named:\n                findings.append((\'PERTURBATION COMPARED WITHOUT ITS CENTRE\',\n                                 \'%s is drawn around the Sun and its block names a centre\' % body))\n            continue\n        if not named or (\'Osculating around the Sun: a=%r AU\' % SEDNA[\'a\']) not in info:\n            findings.append((\'PERTURBATION COMPARED WITHOUT ITS CENTRE\',\n                             \'Sedna is drawn around the barycentre (a=%r) and its block does not \'\n                             \'say it compares the Sun-centred a=%r\' % (SEDNA_BARY[\'a\'], SEDNA[\'a\'])))\n        m = re.search(r\'Delta-a: \\+?(%s) AU\' % NUM, info)\n        if not m or abs(float(m.group(1)) - (SEDNA[\'a\'] - mean_a)) > 0.01:\n            findings.append((\'PERTURBATION COMPARED WITHOUT ITS CENTRE\',\n                             \'Sedna Delta-a %s is not the Sun-centred a minus the mean a (%.2f)\'\n                             % (m.group(1) if m else \'missing\', SEDNA[\'a\'] - mean_a)))\n\n\ndef judge_periosc(io_mod, findings, counts):\n    """The perihelion osculating orbit (Encke\'s white arc) prints its\n    distances by the digits rule, so it says which figure they are\n    rounded to. Run offline: its perihelion time and its elements at that\n    time are the recorded ones."""\n    from constants_new import color_map\n    info = next(o for o in OBJECT_DEFINITIONS if o[\'name\'] == \'Encke\')\n    old_tp = osculating_cache_manager.resolve_tp\n    old_fetch = osculating_cache_manager.fetch_osculating_elements\n    osculating_cache_manager.resolve_tp = lambda name, obj_info=None: (ENCKE[\'TP\'], \'fixture\')\n    osculating_cache_manager.fetch_osculating_elements = lambda **kw: {\'elements\': dict(ENCKE)}\n    fig = go.Figure()\n    try:\n        with contextlib.redirect_stdout(io.StringIO()):\n            io_mod.plot_perihelion_osculating_orbit(fig, \'Encke\', info, color_map, PLOT_DATE, True)\n    finally:\n        osculating_cache_manager.resolve_tp = old_tp\n        osculating_cache_manager.fetch_osculating_elements = old_fetch\n    texts = [t.text if isinstance(t.text, str) else t.text[0]\n             for t in fig.data if t.text is not None and \'Osculating Orbit\' in str(t.text)]\n    if not texts:\n        findings.append((\'MARKER MISSING\', "Encke\'s perihelion osculating orbit has no hover"))\n        return\n    text = texts[0]\n    counts[\'periosc\'] += 1\n    judge_digits(\'Encke\', text, FLOOR_KM, findings, counts, \'perihelion osculating orbit\')\n    if re.search(r\'%s km\' % NUM, text) and \'shown to the whole kilometer\' not in text:\n        findings.append((\'DISTANCES WITHOUT THEIR ACCURACY SENTENCE\',\n                         "Encke\'s perihelion osculating orbit prints distances to the whole "\n                         \'kilometer and does not say why\'))\n\n\ndef _axis_range_function(orrery_source):\n    """palomas_orrery.calculate_axis_range_from_orbits, compiled alone from\n    the source, so the frame is judged without opening the orrery\'s\n    window."""\n    import ast\n    tree = ast.parse(orrery_source)\n    fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef)\n              and n.name == \'calculate_axis_range_from_orbits\')\n    ns = {}\n    exec(compile(ast.Module(body=[fn], type_ignores=[]), \'palomas_orrery.py\', \'exec\'), ns)\n    return ns[\'calculate_axis_range_from_orbits\']\n\n\ndef judge_frame(findings, counts, orrery_source=None):\n    """The plot\'s frame is sized from the ellipses as drawn: Sedna\'s far end\n    is its barycentre aphelion moved by the barycentre\'s place (worked out\n    here), times the 1.1 margin the orrery gives beyond 100 au."""\n    if orrery_source is None:\n        with open(os.path.join(HERE, \'palomas_orrery.py\'), encoding=\'utf-8\') as f:\n            orrery_source = f.read()\n    fn = _axis_range_function(orrery_source)\n    el, off = DRAWN[\'Sedna\']\n    far = math.sqrt(sum((a + b) ** 2 for a, b in zip(at_anomaly(el, 180.0), off)))\n    with cache_is(fixture_cache()), contextlib.redirect_stdout(io.StringIO()):\n        rng = fn([{\'name\': \'Sedna\'}], {}, {\'Sedna\': dict(SEDNA)}, parent_planets, \'Sun\')\n    counts[\'frames\'] += 1\n    if abs(rng[1] - 1.1 * far) > 1e-6 * far:\n        findings.append((\'FRAME SIZED FROM ANOTHER ORBIT\',\n                         "the frame reaches %.2f au; Sedna\'s drawn ellipse ends %.2f au from the "\n                         \'Sun, so it should reach %.2f\' % (rng[1], far, 1.1 * far)))\n    # A body drawn as fetched keeps a(1+e).\n    with cache_is(fixture_cache()), contextlib.redirect_stdout(io.StringIO()):\n        rng = fn([{\'name\': \'Mercury\'}], {}, {\'Mercury\': dict(MERCURY)}, parent_planets, \'Sun\')\n    want = 1.3 * MERCURY[\'a\'] * (1 + MERCURY[\'e\'])\n    counts[\'frames\'] += 1\n    if abs(rng[1] - want) > 1e-9:\n        findings.append((\'FRAME SIZED FROM ANOTHER ORBIT\',\n                         "Mercury\'s frame reaches %.6f au, want %.6f" % (rng[1], want)))\n\n\ndef run_checks(io_mod=None, ap_mod=None, pv_mod=None, orrery_source=None):\n    import idealized_orbits\n'),
    ('test_orbit_markers.py', 'line 843: findings = []',
     "    findings = []\n    counts = {'bodies': 0, 'points': 0, 'markers': 0, 'numbers': 0, 'dates': 0,\n              'elements': 0, 'moon': 0, 'sources': 0, 'kpos': 0, 'window': 0}\n    fig = draw_sun_view(io_mod, fixture_cache(), ap_mod=planted_ap)\n    judge_sun_view(fig, findings, counts)\n    judge_actual_markers(fig, findings, counts)\n    judge_kepler_position(io_mod, findings, counts)\n",
     "    findings = []\n    counts = {'bodies': 0, 'points': 0, 'markers': 0, 'numbers': 0, 'dates': 0,\n              'elements': 0, 'moon': 0, 'sources': 0, 'kpos': 0, 'window': 0,\n              'comparisons': 0, 'periosc': 0, 'frames': 0}\n    fig = draw_sun_view(io_mod, fixture_cache(), ap_mod=planted_ap)\n    judge_sun_view(fig, findings, counts)\n    judge_comparison(fig, findings, counts)\n    judge_periosc(io_mod, findings, counts)\n    judge_frame(findings, counts, orrery_source)\n    judge_actual_markers(fig, findings, counts)\n    judge_kepler_position(io_mod, findings, counts)\n"),
    ('test_orbit_markers.py', 'line 902: "                center_name=center_object,"',
     '      "                center_name=center_object,"),\n     \'PARAMETERS WINDOW PERIOD FROM ANOTHER CENTRE\'),\n]\n\n',
     '      "                center_name=center_object,"),\n     \'PARAMETERS WINDOW PERIOD FROM ANOTHER CENTRE\'),\n    ("the perihelion osculating orbit\'s hover without its accuracy sentence",\n     (\'idealized_orbits\', "        f\\"{_accuracy_tail(_pa.accuracy_for(obj_name, \'Sun\'))}\\"\\n", ""),\n     \'DISTANCES WITHOUT THEIR ACCURACY SENTENCE\'),\n    ("Sedna\'s perturbation block not naming the centre it compared around",\n     (\'idealized_orbits\', "_acc, _compared_around)}\\"", "_acc)}\\""),\n     \'PERTURBATION COMPARED WITHOUT ITS CENTRE\'),\n    ("the frame sized from the Sun-centred orbit",\n     (\'palomas_orrery\', "                        aphelion = _drawn_far\\n",\n      "                        pass\\n"),\n     \'FRAME SIZED FROM ANOTHER ORBIT\'),\n]\n\n'),
    ('test_orbit_markers.py', 'line 923: def _orrery_planted(old, new):',
     '\n\ndef main():\n    problems = []\n',
     "\n\ndef _orrery_planted(old, new):\n    with open(os.path.join(HERE, 'palomas_orrery.py'), encoding='utf-8') as f:\n        src = f.read()\n    n = src.count(old)\n    if n != 1:\n        raise RuntimeError('PLANT ANCHOR: %r found %d times in palomas_orrery' % (old[:60], n))\n    return src.replace(old, new)\n\n\ndef main():\n    problems = []\n"),
    ('test_orbit_markers.py', "line 939: if plant == 'orrery':",
     "            if plant == 'orrery':\n                kw['orrery_source'] = _orrery_with_copy()\n            else:\n                module, old, new = plant\n",
     "            if plant == 'orrery':\n                kw['orrery_source'] = _orrery_with_copy()\n            elif plant[0] == 'palomas_orrery':\n                kw['orrery_source'] = _orrery_planted(plant[1], plant[2])\n            else:\n                module, old, new = plant\n"),
    ('test_orbit_markers.py', "line 972: 'year on against the drawn elements\\' period",
     "          'year on against the drawn elements\\' period; a pre-build-2 record\\'s drawing '\n          'and dates; the parameters window\\'s apsis dates against Earth\\'s own period; '\n          'the Moon\\'s arc against its fetched period; and the dispatch in palomas_orrery.py')\n    print('examined: Mercury, Encke and Sedna from the Sun (ellipse, orbit hover, periapsis, '\n          'apoapsis, actual perihelion, Keplerian position); Sedna with a pre-build-2 record; '\n          'Earth in the orbital parameters window; the Moon from Earth; Io\\'s perijove and '\n          'apojove from Jupiter; palomas_orrery.py and idealized_orbits.py')\n    if problems:\n        print('ORBIT MARKERS: FAIL -- %d problem(s)' % len(problems))\n",
     "          'year on against the drawn elements\\' period; a pre-build-2 record\\'s drawing '\n          'and dates; the parameters window\\'s apsis dates against Earth\\'s own period; '\n          'the Moon\\'s arc against its fetched period; Sedna\\'s perturbation block against '\n          'the Sun-centred a minus the mean a; Encke\\'s perihelion osculating orbit against the '\n          'whole-kilometer floor and its sentence; the frame against Sedna\\'s drawn far end; '\n          'and the dispatch in palomas_orrery.py')\n    print('examined: Mercury, Encke and Sedna from the Sun (ellipse, orbit hover, periapsis, '\n          'apoapsis, actual perihelion, Keplerian position); Sedna with a pre-build-2 record; '\n          'Earth in the orbital parameters window; the Moon from Earth; Io\\'s perijove and '\n          'apojove from Jupiter; Encke\\'s perihelion osculating orbit; the frame for Sedna and '\n          'for Mercury; palomas_orrery.py and idealized_orbits.py')\n    if problems:\n        print('ORBIT MARKERS: FAIL -- %d problem(s)' % len(problems))\n"),
    ('test_orbit_markers.py', "line 987: 'drawn points on their period\\'s centre; %d ",
     "          'drawn points on their period\\'s centre; %d markers, %d dates, %d printed distances '\n          'against their errors; %d elements as given; %d Keplerian positions half a year '\n          'on; %d parameters-window date pairs; %d Moon arcs; %d sources read'\n          % (len(PLANTS), len(PLANTS), counts['bodies'], counts['points'], counts['markers'],\n             counts['dates'], counts['numbers'], counts['elements'], counts['kpos'],\n             counts['window'], counts['moon'], counts['sources']))\n    return 0\n\n",
     "          'drawn points on their period\\'s centre; %d markers, %d dates, %d printed distances '\n          'against their errors; %d elements as given; %d Keplerian positions half a year '\n          'on; %d parameters-window date pairs; %d Moon arcs; %d perturbation blocks; '\n          '%d perihelion osculating orbits; %d frames; %d sources read'\n          % (len(PLANTS), len(PLANTS), counts['bodies'], counts['points'], counts['markers'],\n             counts['dates'], counts['numbers'], counts['elements'], counts['kpos'],\n             counts['window'], counts['moon'], counts['comparisons'], counts['periosc'],\n             counts['frames'], counts['sources']))\n    return 0\n\n"),
    ('palomas_orrery_dashboard.py', 'line 192: after Test Orbit Cache, which is its alphabe',
     'after Test Orbit Cache, which is its alphabetical place once the other\nlabels lose the word.\n"""\n\n',
     'after Test Orbit Cache, which is its alphabetical place once the other\nlabels lose the word.\nOctober 13, 2026 with Anthropic\'s Claude Opus 5.5 (L-431, after build 2\'s\nlook): Orbit Markers\' description counts twelve planted faults, not nine.\n"""\n\n'),
    ('palomas_orrery_dashboard.py', 'line 1247: "its distances to the digits JPL\'s errors ea',
     '         "its distances to the digits JPL\'s errors earn. Runs the real orbit "\n         "drawing offline on recorded inputs and judges it with arithmetic of "\n         "its own. Nine faults are planted first, each in a copy of the real "\n         "code, and each must be caught by name. "\n         "Ends on \\"ORBIT MARKERS: PASS\\" (L-431, L-401).",\n',
     '         "its distances to the digits JPL\'s errors earn. Runs the real orbit "\n         "drawing offline on recorded inputs and judges it with arithmetic of "\n         "its own. Twelve faults are planted first, each in a copy of the real "\n         "code, and each must be caught by name. "\n         "Ends on \\"ORBIT MARKERS: PASS\\" (L-431, L-401).",\n'),
    ('LEDGER_CONSOLIDATED.md', 'line 375: Module updated: October 13, 2026 with Anthro',
     "opened from Tony's question on Settled), built on c9722520.\nReview and RICE update Tony 6-21-2026\n",
     "opened from Tony's question on Settled), built on c9722520.\nModule updated: October 13, 2026 with Anthropic's Claude Opus 5.5\n(L-431 build 2 accepted at Tony's look, with L-401's second slice; the\nthree findings read from his saved plot fixed), built on 87a54704.\nReview and RICE update Tony 6-21-2026\n"),
    ('LEDGER_CONSOLIDATED.md', 'line 1493: <!-- L:431 status:OPEN upd:2026-10-13 sectio',
     '<!-- L:431 status:OPEN upd:2026-10-12 section:A flag: rice: -->\n',
     '<!-- L:431 status:OPEN upd:2026-10-13 section:A flag: rice: -->\n'),
    ('LEDGER_CONSOLIDATED.md', "line 1700: - **2026-10-13, build 2 accepted at Tony's l",
     "  fetch them.\n**Gap:** three builds, in order (the record's section 3):\n",
     '  fetch them.\n- **2026-10-13, build 2 accepted at Tony\'s look** (pushed at 6bb8ef6f;\n  his run record `documentation/WHERE_WE_ARE_10-12-26_2212_run_record.md`,\n  at 87a54704). The patch ran clean; the live check asked JPL and\n  printed Sedna\'s aphelion in 7771 "Uncertain by about 930 days" beside\n  the typed table\'s 7776; the maintenance run passed 25 of 25 with the\n  gate path at 0 and the whole tree at 280, as predicted. His verdicts\n  on the look, in his words: Sedna "correct."; Encke and Mercury\n  "correct"; Venus\'s typed line "yes"; every marker\'s lines "yes"; the\n  ellipse, the centre line, the dates, the Kepler sentence and the\n  digits "correct". In chat: "bottom line: looks good."\n- **Three findings read from his saved plot** (Claude read\n  `solar_system_20261013_0829.html` and the console), fixed in\n  `patch_L431_7_look_fixes_20261013.py`, each with a planted fault in\n  `test_orbit_markers.py` (now twelve):\n  - Encke\'s perihelion osculating orbit printed its distances by the\n    digits rule without the sentence saying which figure they are\n    rounded to (L-401\'s slice; the one hover build 2 missed).\n  - Sedna\'s orbit hover showed the drawn a (506.44 au, around the\n    center of mass) above a perturbation block that compared the\n    Sun-centred a (539.87 au) with the mean, so "+58.56 AU (12.2%)"\n    read as the drawn orbit\'s. The block now says "both around the Sun"\n    and prints the elements it compared.\n  - The plot\'s frame was sized from the Sun-centred aphelion, 1,004\n    au, so it reached 1,104 au around a drawn ellipse ending at 937.\n    `calculate_axis_range_from_orbits`, which the static plot and the\n    animation share, now reads the drawn far end\n    (`orbital_period.drawn_aphelion_distance`): 1,030 au.\n**Gap:** three builds, in order (the record\'s section 3):\n'),
    ('LEDGER_CONSOLIDATED.md', 'line 1732: the fetched period: BUILT (2026-10-12) and A',
     "   the fetched period: BUILT (2026-10-12); waits for Tony's run, the\n   live check and his look (Mode 5).\n",
     "   the fetched period: BUILT (2026-10-12) and ACCEPTED at Tony's look\n   (2026-10-13). The three findings from his saved plot are fixed in\n   patch_L431_7, which waits for his run.\n"),
    ('LEDGER_CONSOLIDATED.md', 'line 1741: `documentation/HANDOFF_L431_period_build1_20',
     '`documentation/HANDOFF_L431_period_build1_20261011.md`; `orbital_period.py`;\n',
     '`documentation/HANDOFF_L431_period_build1_20261011.md`;\n`documentation/HANDOFF_L431_build2_orbits_markers_20261012.md`;\n`documentation/HANDOFF_L431_build2_look_fixes_20261013.md`; `orbital_period.py`;\n'),
    ('LEDGER_CONSOLIDATED.md', 'line 2233: <!-- L:401 status:OPEN upd:2026-10-13 sectio',
     '<!-- L:401 status:OPEN upd:2026-10-12 section:A flag: rice: -->\n',
     '<!-- L:401 status:OPEN upd:2026-10-13 section:A flag: rice: -->\n'),
    ('LEDGER_CONSOLIDATED.md', 'line 2486: - **2026-10-13, the second slice accepted** ',
     "**Gap:** Builds 1 and 2 are built; build 2 waits for Tony's look with\nL-431's. Left, build 3: the fly-to buttons, the parameters window, the\n",
     '- **2026-10-13, the second slice accepted** at Tony\'s look with\n  L-431\'s build 2 ("the distances\' digits. -- correct"). The perihelion\n  osculating orbit\'s hover now carries the accuracy sentence it lacked\n  (patch_L431_7; L-431 records it).\n**Gap:** Builds 1 and 2 are built and accepted. Left, build 3: the fly-to buttons, the parameters window, the\n'),
    ('documentation/WHERE_WE_ARE.md', 'line 4: Last updated: October 13, 2026: L-431 build ',
     "Last updated: October 12, 2026, night: L-431 build 2 built, with L-401's.\n- Written at orrery c9722520 and gallery f9453dd.\n",
     'Last updated: October 13, 2026: L-431 build 2 accepted at your look; three fixes.\n- Written at orrery 87a54704 and gallery 924977a3.\n'),
    ('documentation/WHERE_WE_ARE.md', 'line 10: > - Your look at the drawn orbits and marker',
     "> - Each orbit is drawn around its period's center (Sedna's around the\n>   center of mass, smaller); markers dated from JPL's period; every\n>   orbit and marker hover by the body hover's digits rule.\n> - Your Settled question: 3 of 12 lines are in a skill; L-435 (the\n>   rulings held only here) carries the rest.\n",
     '> - Your look at the drawn orbits and markers: accepted ("bottom line:\n>   looks good").\n> - Three fixes from your saved plot: Encke\'s white arc\'s accuracy line;\n>   Sedna\'s perturbation lines say "around the Sun"; the frame fits\n>   Sedna\'s drawn orbit (1,030 au, not 1,104).\n'),
    ('documentation/WHERE_WE_ARE.md', "line 16: > **Do next:** *L-431's website build, and t",
     "> **Do next:** *your look at build 2; then L-431's website build, and\n> the four briefed sessions beside it, in your order.*\n",
     "> **Do next:** *L-431's website build, and the four briefed sessions\n> beside it, in your order.*\n"),
    ('documentation/WHERE_WE_ARE.md', 'line 20: > - *Run patch_L431_7 and the maintenance ru',
     "> - *Run patch_L431_6 and the maintenance run; do the look (the\n>   handoff's section 7); reinstall horizons-orbital-mechanics 1.4;\n>   the Project's instructions to v3.93; push.*\n",
     '> - *Run patch_L431_7 and the maintenance run (25 of 25, Orbit markers\n>   12 of 12); move the patch into documentation/; push. No look\n>   needed.*\n'),
    ('documentation/WHERE_WE_ARE.md', 'line 30: 5.   [NOW]   *L-401 (the distance digits): b',
     "  5.   [NOW]   *L-401 (the distance digits): build 2 built with L-431's;\n               your look; build 3 later. Then Earth's remaining items.*\n",
     "  5.   [NOW]   *L-401 (the distance digits): builds 1 and 2 accepted;\n               build 3 later. Then Earth's remaining items.*\n"),
    ('documentation/WHERE_WE_ARE.md', 'line 37: 6a.  [NOW]   *Orbital periods from JPL: buil',
     '  6a.  [NOW]   *Orbital periods from JPL: build 2 done, the drawn orbits\n               and markers, waiting for your look; the website next.*\n',
     '  6a.  [NOW]   *Orbital periods from JPL: builds 1 and 2 accepted, the\n               hovers, the drawn orbits and markers; the website next.*\n'),
    ('documentation/WHERE_WE_ARE.md', 'line 91: - Last cache build: 20261013T132123Z, ok, no',
     '- Last cache build: 20261012T183311Z, ok, no retry (gallery f9453dd).\n',
     '- Last cache build: 20261013T132123Z, ok, no retry (gallery 924977a3).\n'),
    ('documentation/WHERE_WE_ARE.md', 'line 93: 87a54704 (your run of 2026-10-12). Whole tre',
     "  c9722520 (your run of 2026-10-12). Whole tree: 288; this patch takes\n  it to 280 (measured in the sandbox).\n- This page's date and the ledger's newest stamp: both Oct 12. Agree.\n",
     "  87a54704 (your run of 2026-10-12). Whole tree: 280, as build 2\n  predicted.\n- This page's date and the ledger's newest stamp: both Oct 13. Agree.\n"),
    ('documentation/WHERE_WE_ARE.md', 'line 97: ## Waiting on you',
     '## Waiting on you  **>> UPDATED THIS SESSION**\n',
     '## Waiting on you\n'),
    ('documentation/WHERE_WE_ARE.md', 'line 102: numbers that are not distances have no digit',
     '  numbers that are not distances have no digits rule. << new\n',
     '  numbers that are not distances have no digits rule.\n'),
    ('documentation/WHERE_WE_ARE.md', 'line 118: - Orbital periods: rulings `DESIGN_L431_..._',
     '- Orbital periods: rulings `DESIGN_L431_..._rulings_20261011.md`; build 2,\n  your look: `HANDOFF_L431_build2_orbits_markers_20261012.md` section 7\n',
     "- Orbital periods: rulings `DESIGN_L431_..._rulings_20261011.md`; build 2's\n  look and fixes `HANDOFF_L431_build2_look_fixes_20261013.md`\n"),
]

CREATED = {
    'documentation/HANDOFF_L431_build2_look_fixes_20261013.md': '<!-- Doc-Kind: hand | Session record: Tony\'s look at L-431 build 2 accepted, and the three findings from his saved plot fixed in patch_L431_7. -->\n# L-431 build 2: the look, and three fixes from the saved plot\n\nBuilt on orrery 87a54704ab2cba6d3fbfa5cbb4c3adb698a53a02 at\nhttps://github.com/tonylquintanilla/palomas_orrery (main); gallery\n924977a3 at https://github.com/tonylquintanilla/tonyquintanilla.github.io,\nnot touched.\nTony\'s local folders: orrery\n`C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\`;\ngallery `C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\`.\nWritten October 13, 2026 with Anthropic\'s Claude Opus 5.5. Follows\n`HANDOFF_L431_build2_orbits_markers_20261012.md` (the build).\n\n## 1. The look: accepted\n\nTony ran patch_L431_6, the live check and the maintenance run, did the\nlook in the build handoff\'s section 7, and pushed (6bb8ef6f, then\n87a54704 with his run record and the v3.93 copy). His record is\n`documentation/WHERE_WE_ARE_10-12-26_2212_run_record.md`. His verdicts,\none per line of the look: "correct.", "correct", "yes", "yes",\n"correct"; the reinstall "done". In chat: "bottom line: looks good."\n\nWhat the run showed, against what the build handoff predicted:\n- The live check: Sedna drawn around the solar system\'s center of mass,\n  a = 506.44 au; aphelion 7771-02-06 "Uncertain by about 930 days";\n  the typed table\'s 7776. Encke\'s aphelion 2028-10-05 (the typed table\n  has none). Mercury\'s aphelion a minute from the typed table\'s.\n- The maintenance run: 25 of 25 gating checkers; Orbit markers 9 of 9\n  planted faults; the gate path 0 Tier-1; the whole tree 280, the 288 to\n  280 the patch predicted.\n- The plot: Sedna\'s drawn aphelion 936.69 au; Venus (No to its update\n  box) shows "From a typed period: typed value, not fetched from JPL."\n\n## 2. Three findings from the saved plot, fixed\n\nClaude read the plot Tony saved\n(`palomas_orrery_images/solar_system_20261013_0829.html`, staged from his\ncomputer) and his console. Three things the build missed, all fixed in\n`patch_L431_7_look_fixes_20261013.py`, none needing a ruling:\n\n1. **Encke\'s perihelion osculating orbit** (the white arc) printed its\n   distances by the digits rule but not the sentence saying which figure\n   they are rounded to. Every other marker carries it. Now it does\n   (`idealized_orbits.plot_perihelion_osculating_orbit`).\n2. **Sedna\'s perturbation block.** The orbit hover\'s top lines show the\n   drawn elements, around the center of mass (a = 506.44 au). The block\n   below compared the Sun-centred elements (a = 539.87 au) with the mean\n   ones, which are around the Sun -- right, by horizons-orbital-mechanics\n   1.4 -- but did not say so, so "+58.56 AU (12.2%)" read as the drawn\n   orbit\'s. The block now reads "Perturbation (osculating vs mean, both\n   around the Sun)" and prints the Sun-centred a and e it compared\n   (`get_mean_vs_osculating_assessment`, new `compared_around`).\n3. **The frame.** `palomas_orrery.calculate_axis_range_from_orbits`,\n   which the static plot and the animation share, sized the frame from\n   the Sun-centred a(1+e), 1,004 au, so it reached 1,104 au around an\n   ellipse that ends at 937. It now asks\n   `orbital_period.drawn_aphelion_distance` for the drawn far end where\n   the orbit is drawn around another centre: 1,030 au. The animation\'s\n   earlier range hint (for clamping the Sun-direction arrow) still reads\n   the mean elements, 975 au; the frame it draws uses the fetched ones.\n   Left as it was.\n\nEach has a planted fault in `test_orbit_markers.py`, now twelve, each\ncaught by name:\n\n    planted                                          caught as\n    the perihelion osculating orbit\'s hover without  DISTANCES WITHOUT THEIR ACCURACY SENTENCE\n      its accuracy sentence\n    Sedna\'s perturbation block not naming the        PERTURBATION COMPARED WITHOUT ITS CENTRE\n      centre it compared around\n    the frame sized from the Sun-centred orbit       FRAME SIZED FROM ANOTHER ORBIT\n\nThe checker runs the perihelion osculating orbit offline on Encke\'s\nrecorded elements, and compiles `calculate_axis_range_from_orbits` alone\nfrom palomas_orrery.py\'s source, so the frame is judged without opening\nthe orrery\'s window. One correction to the checker itself: a whole\nnumber\'s trailing zeros are no longer called coarse, since its place\ncannot be read from the print (50,654,699.7 km to the whole kilometer\nis 50,654,700).\n\n## 3. Tested\n\n- `test_orbit_markers.py`: 12 of 12 planted faults caught; then a clean\n  pass. `test_position_digits.py`: 13 of 13.\n- The window opens headless from a throwaway copy.\n- Plot and Animate through the real dispatch (Sedna, Encke, Mercury from\n  the Sun): the frame is +/-1,030 au in both, from Sedna\'s drawn far end\n  of 936.71 au.\n- The maintenance run on a clean clone with the patch applied: see the\n  patch\'s NEXT lines for what to expect.\n\n## 4. Still open (unchanged by this session)\n\n- L-431 build 3, the website: the export carries each period and the\n  elements around its centre; every room draws and prints them.\n- L-401 build 3: the fly-to buttons, the parameters window, the\n  animation\'s 2xr; then the encounter slice.\n- At the design talk (on your page): a model with no stated accuracy\n  (the Moon\'s analytical orbit) and numbers that are not distances.\n\n## 5. For Tony\n\n- (do) Run `patch_L431_7_look_fixes_20261013.py` from the orrery folder\n  (VS Code, Run).\n- (do) Run `orrery_maintenance_run.py`: 25 of 25, "Orbit markers" with\n  12 of 12.\n- (do) Move the patch script into `documentation/`; commit and push.\n- No look is needed: the three fixes are words in two hovers and the\n  frame\'s size, each judged by the checker. If you want to see them,\n  plot Sedna and Encke from the Sun: the frame ends near 1,030 au, and\n  Sedna\'s orbit hover says "both around the Sun".\n\nNothing here bumps a skill or the protocol. The next session confirms\nits loaded horizons-orbital-mechanics reads 1.4 before Horizons work\n(this session loaded 1.3, and was the one that bumped it).\n',
}

FIXES = [
    "Encke's perihelion osculating orbit (the white arc): its hover now ends its distances "
    "with the sentence saying which figure they are rounded to.",
    "Sedna's orbit hover: the perturbation lines now read \"both around the Sun\" and print "
    "the Sun-centred a and e they compare, so \"+58.56 AU\" is not read against the drawn "
    "a of 506.44 au.",
    "The frame: sized from Sedna's drawn far end, 937 au from the Sun, so it reaches about "
    "1,030 au in the static plot and the animation, not 1,104.",
]


def apply():
    for f in CREATED:
        if os.path.exists(os.path.join(ROOT, f)):
            print('ERROR: %s already exists; this patch has run. NOTHING was written.' % f)
            return None
    texts, crlf, done = {}, set(), []
    for f, label, old, new in EDITS:
        path = os.path.join(ROOT, f)
        if f not in texts:
            if not os.path.exists(path):
                print('ERROR: %s not found in %s. NOTHING was written.' % (f, ROOT))
                return None
            raw = open(path, 'rb').read()
            if b'\r\n' in raw:
                crlf.add(f)
            texts[f] = raw.replace(b'\r\n', b'\n').decode('utf-8')
        t = texts[f]
        n = t.count(old)
        if n != 1:
            print('ANCHOR FAIL  %-45s %s (found %d times, expected 1). NOTHING was written.'
                  % (f, label, n))
            return None
        if MARKER in t and t.index(old) > t.index(MARKER):
            print('ANCHOR FAIL  %-45s %s lies below the run-record marker. NOTHING was written.'
                  % (f, label))
            return None
        texts[f] = t.replace(old, new)
        done.append((f, label))
    for f, label, old, new in EDITS:
        if any(ord(c) > 127 for c in new):
            print('ERROR: an edit to %s would add non-ASCII. NOTHING was written.' % f)
            return None
    for f, t in texts.items():
        with open(os.path.join(ROOT, f), 'w', encoding='utf-8', newline='') as h:
            h.write(t)
    for f, t in CREATED.items():
        with open(os.path.join(ROOT, f), 'w', encoding='utf-8', newline='') as h:
            h.write(t)
    for f, label in done:
        print('ok  %-45s %s' % (f, label))
    for f in CREATED:
        print('ok  %-45s created' % f)
    for f in sorted(crlf):
        print('note: %s was CRLF in the working copy; written LF' % f)
    print()
    print('patch applied (%d edits in %d files, %d file created)'
          % (len(done), len(texts), len(CREATED)))
    print('Stamps updated: the docstrings of every edited module, the ledger.')
    print()
    print('The three fixes from your saved plot:')
    for line in FIXES:
        print('  - ' + line)
    return True


def main():
    if not apply():
        return 1
    print()
    print('NEXT:')
    print('  1. Run orrery_maintenance_run.py: expect 25 of 25 gating checkers, "Orbit markers"')
    print('     with 12 of 12 planted faults, and "0 TIER-1 -- the push gate holds".')
    print('  2. Move this script into documentation/; commit and push.')
    print('  No look is needed. To see the fixes anyway: plot Sedna and Encke from the Sun;')
    print('  the frame ends near 1,030 au, and Sedna\'s orbit hover says "both around the Sun".')
    return 0


if __name__ == '__main__':
    sys.exit(main())
