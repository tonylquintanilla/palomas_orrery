"""patch_L322_D_3_orrery_pole_of_date_20260923.py -- L-322 Stage D, patch D3.

RUN COMMAND

    Run patch D2 (patch_L322_D_2_orrery_rows_and_poles_20260923.py) FIRST.
    This patch is built on the files D2 produces and refuses to run
    without them.

    Save this file in the ROOT of the palomas_orrery repository, open it in
    VS Code and click Run. It refuses to run from documentation/. After it
    has run, MOVE it into documentation/.

WHAT IT CHANGES, and what stays

    Three new files and four edited ones, all or nothing: if one anchor is
    missing, a file is not the version this was built against, or a new
    file already exists with other content, NOTHING is written.

    NEW earth_pole_of_date.py      fetches Earth's north pole for the
                                   plot's date (Horizons quantity 32,
                                   target 399) and the Earth-Moon
                                   barycenter's orbit (target 3), keeps
                                   them in data/earth_pole_cache.json,
                                   computes the tilt of date from the two,
                                   and falls back to the frame's year-2000
                                   axis when Horizons cannot be reached.
    NEW test_earth_pole_of_date.py offline checks: the manifest's worked
                                   case, the geometry against ERFA's true
                                   obliquity, fallback, cache, hover words
                                   and the Earth transform.
    NEW earth_pole_live_check.py   the script you run to see a real fetch,
                                   checked against ERFA, and the monthly
                                   wobble of Earth's own orbit measured.
    idealized_orbits.py            create_planet_transformation_matrix
                                   draws Earth's pole of date.
    planet_visualization_utilities.py  Earth's axis hover prints the tilt
                                   of date, or says why none is shown;
                                   the typed 23.44 deg goes.
    palomas_orrery.py              the static plot and the animation tell
                                   earth_pole_of_date.py the plot's date
                                   before the center-body shells are
                                   built. The social export reuses the
                                   last plotted figure, so it needs no
                                   change.
    orrery_maintenance_run.py      runs the new test as "Earth pole of
                                   date".

    What moves on screen: Earth's axis, the dipole cone hung on it and the
    radiation belts, by about 0.15 degrees for a 2026 date, because they
    now point along the pole of that date instead of the pole of 2000.

    Nothing in the gallery repository is touched.

WHAT IS PERMANENT AND WHAT IS NOT

    This script is disposable and aborts on a second run. The three new
    files and the edits are permanent. The cache file is data and is
    rewritten by the orrery whenever it fetches a new date.

Built on orrery bba21459bb5dae46d94cb650fd6ba4ab05ee0286 plus patch D2
at https://github.com/tonylquintanilla/palomas_orrery,
from documentation/BUILD_MANIFEST_L322_D_earth_pole_20260922.md rev 3
(the revision with the Earth-Moon barycenter ruling).

Written September 23, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os
import sys

EDITS = [
    ('idealized_orbits.py', '43ff9b435df77a51354d728065d70ec8', '5ed9b4c8a6cd967334008b47ba129c3e', [
        ("(L-322 Stage D: planet_poles moved to constants_new.py and imported\nhere; the rotation of a pole into the ecliptic frame reads\nEARTH_OBLIQUITY_J2000_DEG, the frame's defining angle, where it typed\n23.439291 labelled IAU 2006)\n",
         "(L-322 Stage D: planet_poles moved to constants_new.py and imported\nhere; the rotation of a pole into the ecliptic frame reads\nEARTH_OBLIQUITY_J2000_DEG, the frame's defining angle, where it typed\n23.439291 labelled IAU 2006)\nModule updated: September 23, 2026 with Anthropic's Claude Opus 5.5\n(L-322 Stage D, patch D3: create_planet_transformation_matrix('Earth')\ndraws Earth's pole of the plot's date from earth_pole_of_date.py, and\nthe frame's year-2000 axis when Horizons cannot be reached)\n"),
        ("    # Get pole direction\n    pole = planet_poles[planet_name]\n    ra_pole = np.radians(pole['ra'])\n",
         "    # Get pole direction\n    # L-322 Stage D (2026-09-23): Earth's pole is the pole of the plot's\n    # date, fetched from Horizons by earth_pole_of_date.py; with no date,\n    # or no connection, that module returns the fallback pair the\n    # planet_poles entry also holds. Every other body reads its entry.\n    if planet_name == 'Earth':\n        import earth_pole_of_date\n        pole = earth_pole_of_date.pole_of_scene_date()\n    else:\n        pole = planet_poles[planet_name]\n    ra_pole = np.radians(pole['ra'])\n"),
    ]),
    ('planet_visualization_utilities.py', '6d9628f2211c3982a6288d7b5523d5b5', 'bfb3c487ec26ef7a8e937b6aab156488', [
        ("Stage D: Earth's rotation period on the axis hover is the sidereal period\nrow in constants_new.py at its declared count, where it typed 23.93 h)\n",
         "Stage D: Earth's rotation period on the axis hover is the sidereal period\nrow in constants_new.py at its declared count, where it typed 23.93 h)\n\nModule updated: September 23, 2026 with Anthropic's Claude Opus 5.5 (L-322\nStage D, patch D3: Earth's axis hover prints the tilt of the plot's date,\nfrom earth_pole_of_date.py, where it typed a fixed tilt)\n"),
        ("    # count (seven figures), and says which turn it is. The tilt below is\n    # still typed; the pole-of-date patch replaces it with the tilt of the\n    # plot's date.\n",
         "    # count (seven figures), and says which turn it is. Earth's tilt is not\n    # typed here: build_rotation_axis_traces() asks earth_pole_of_date.py\n    # for the tilt of the plot's date when it builds the hover (L-322\n    # Stage D, patch D3), so obliquity_str is None for Earth.\n"),
        ("                'sense': 'prograde', 'obliquity_str': '23.44 deg',\n                'note': 'The familiar tilt that drives the seasons.',\n",
         "                'sense': 'prograde', 'obliquity_str': None,\n                'note': 'The familiar tilt that drives the seasons.',\n"),
        ('    # 4) single info marker at the north tip (hub of the spin ring)\n    hover = (',
         "    # 4) single info marker at the north tip (hub of the spin ring)\n    obliquity_text = info['obliquity_str']\n    if planet_name == 'Earth':\n        # L-322 Stage D, patch D3: the tilt of the plot's date, or why\n        # none is shown.\n        import earth_pole_of_date\n        obliquity_text = earth_pole_of_date.tilt_hover_text()\n    hover = ("),
        ("                      info['obliquity_str'], info['note'])\n",
         "                      obliquity_text, info['note'])\n"),
    ]),
    ('palomas_orrery.py', '8ce651c86def2687c77204a6542a1a19', '2deb63f343d57b031b06b59f49be49c9', [
        ('build_scene for a readable auto/manual grid).\n\n"""\n',
         'build_scene for a readable auto/manual grid).\nModule updated: September 23, 2026 with Anthropic\'s Claude Opus 5.5 (L-322\nStage D, patch D3: both pipelines tell earth_pole_of_date.py the plot\'s\ndate before building the center-body shells, so Earth\'s axis is drawn\nfor that date; the animation uses its first frame\'s date).\n\n"""\n'),
        ("            _sun_pos_tuple = resolve_shell_sun_position(\n                center_object_name, positions.get('Sun'), date_obj, center_id)\n",
         "            _sun_pos_tuple = resolve_shell_sun_position(\n                center_object_name, positions.get('Sun'), date_obj, center_id)\n            # L-322 Stage D, patch D3: Earth's axis and tilt are drawn for\n            # this date (earth_pole_of_date.py), set here for the shells.\n            import earth_pole_of_date\n            earth_pole_of_date.set_scene_date(date_obj)\n"),
        ('            _sun_pos_tuple = resolve_shell_sun_position(\n                center_object_name, _sun_entry, dates_list[0], center_id)\n',
         "            _sun_pos_tuple = resolve_shell_sun_position(\n                center_object_name, _sun_entry, dates_list[0], center_id)\n            # L-322 Stage D, patch D3: the animation draws Earth's axis and\n            # tilt for its first frame's date; the hover names that date.\n            import earth_pole_of_date\n            earth_pole_of_date.set_scene_date(dates_list[0])\n"),
    ]),
    ('orrery_maintenance_run.py', '89f321eddb6c0d3727a4e78b5b245a42', '996771288c061ef84814a6d9d5a2f706', [
        ('docstring had drifted to four generators and eleven gating checkers;\nthey are six and sixteen.)\n"""\n',
         'docstring had drifted to four generators and eleven gating checkers;\nthey are six and sixteen.)\nModule updated: September 23, 2026 with Anthropic\'s Claude Opus 5.5 (L-322\nStage D, patch D3: CHECKERS gains Earth pole of date,\ntest_earth_pole_of_date.py, which checks the pole-of-date geometry against\nERFA and the fallback without contacting Horizons.)\n"""\n'),
        ("    ('Orbit cache', ['test_orbit_cache.py'], None),\n",
         "    ('Orbit cache', ['test_orbit_cache.py'], None),\n    # Earth's pole and tilt of the plot's date: geometry against ERFA,\n    # fallback, cache, hover and the Earth transform, all offline.\n    # L-322 Stage D, patch D3.\n    ('Earth pole of date', ['test_earth_pole_of_date.py'],\n     'EARTH POLE OF DATE:'),\n"),
    ]),
]

NEW_FILES = [
    ('earth_pole_of_date.py', '60fe43a37e13a6dc331183e172ae7a6c',
     '"""\nearth_pole_of_date.py - Earth\'s rotation pole and tilt for the date of a plot.\n\nEarth\'s axis is not fixed. It slowly circles over thousands of years\n(precession) and nods slightly (nutation), and the plane of Earth\'s orbit\nmoves too. So the direction the orrery draws for Earth\'s axis, and the tilt\nit prints, belong to a date. This module fetches both for the date of the\nplot from JPL Horizons, keeps them in a small cache, and falls back to the\nframe\'s own axis when Horizons cannot be reached.\n\nWHAT IS FETCHED, AND WHY THESE TWO\n\n    1. Earth\'s north pole direction on the date: Horizons observer quantity\n       32 ("N.Pole-RA N.Pole-DC") for target 399, Earth itself. Horizons\n       returns its right ascension and declination in the ICRF, from its\n       high-precision Earth model. astroquery names the two columns\n       NPole_RA and NPole_DEC.\n    2. The orbit of the Earth-Moon barycenter on the same date: osculating\n       elements for Horizons target 3 about the Sun, against the ecliptic\n       of J2000. Not Earth\'s own orbit (target 399). The Horizons manual\n       says osculating elements of 399 about the Sun carry short-period\n       oscillations from Earth\'s motion about the Earth-Moon barycenter,\n       and the ecliptic that Earth\'s tilt is measured against is the\n       barycenter\'s orbit plane (Tony\'s ruling, 2026-09-23, build manifest\n       rev 3 section 0).\n\n    The observer for the pole query is the Sun, not the geocenter, because\n    an observer table of Earth seen from Earth\'s own center is not a\n    meaningful request. The light time from the Sun, about eight minutes,\n    shifts the pole by far less than anything drawn: the manifest measured\n    the pole about 0.15 degrees from the year-2000 axis after 26 years,\n    and eight minutes is a few ten-millionths of that span.\n\nHOW THE TILT IS COMPUTED\n\n    tilt_of_date_deg() turns the fetched pole from the ICRF into the\n    drawing\'s frame (the ecliptic of J2000) by the frame\'s defining angle,\n    EARTH_OBLIQUITY_J2000_DEG in constants_new.py. It turns the barycenter\'s\n    inclination and node into the pole of its orbit in the same frame. The\n    tilt is the angle between the two directions. Nothing here types a\n    tilt, a rate or a textbook formula. The value includes Earth\'s nod at\n    that instant, so it is not the smoothed mean value a textbook gives;\n    test_earth_pole_of_date.py compares it with the IAU 2006 mean formula\n    (through ERFA, the library astropy already uses) only as an independent\n    check.\n\nWHAT HAPPENS WHEN HORIZONS CANNOT BE REACHED\n\n    The pole is the fallback pair in constants_new.py,\n    EARTH_POLE_RA_J2000_DEG and EARTH_POLE_DEC_J2000_DEG: the frame\'s own\n    axis, which is Earth\'s mean pole of the year 2000. No tilt is printed.\n    The axis hover says which of the two the drawing shows and why\n    (Graceful Fallback, protocol Part 2).\n\nHOW IT IS USED\n\n    palomas_orrery.py calls set_scene_date() just before it builds the\n    center-body shells, in both the static plot and the animation (the\n    animation uses its first frame\'s date). create_planet_transformation_\n    matrix(\'Earth\') in idealized_orbits.py then asks pole_of_scene_date()\n    for the pole, and build_rotation_axis_traces() in\n    planet_visualization_utilities.py asks tilt_hover_text() for the line\n    it prints. With no scene date set -- a caller outside those two\n    pipelines -- the fallback is used and nothing is fetched.\n\nTHE CACHE\n\n    data/earth_pole_cache.json, keyed by the date at 0h UT, holds each\n    fetched pole and barycenter orbit with its source block. A date already\n    in the cache is not fetched again. Nothing in it is ever typed by hand.\n    Delete the file to force fresh fetches.\n\nRUN COMMAND\n\n    Not run by itself. earth_pole_live_check.py, beside it, is the script\n    you run to see a real fetch and the checks against it.\n\nRole: data\nDomain: orrery\n\nModule created: September 23, 2026 with Anthropic\'s Claude Opus 5.5\n(L-322 Stage D, patch D3: Earth\'s pole of date and tilt of date, fetched\nfrom Horizons, from build manifest rev 3 sections 0 and 4.4)\n"""\n\nimport json\nimport math\nimport os\nfrom datetime import datetime, timezone\n\nfrom constants_new import (\n    EARTH_OBLIQUITY_J2000_DEG,\n    EARTH_POLE_DEC_J2000_DEG,\n    EARTH_POLE_RA_J2000_DEG,\n)\n\nCACHE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),\n                          \'data\', \'earth_pole_cache.json\')\n\nPOLE_QUERY = {\'target\': \'399\', \'observer\': \'@sun\', \'quantity\': \'32\'}\nORBIT_QUERY = {\'target\': \'3\', \'center\': \'@sun\', \'refplane\': \'ecliptic\'}\n\n# The tilt prints at seven significant figures. There is no stated\n# uncertainty on a Horizons pole, so Rule 3\'s counting fallback decides:\n# Horizons prints the pole\'s declination to five decimal places of a\n# degree (89.85464, seven figures), and the tilt is set by that input.\nTILT_FIGURES = 7\n\n_scene = {\'date\': None}\n_memo = {}\n\n\ndef set_scene_date(date_obj):\n    """Record the date the next plot is drawn for (a datetime, UTC)."""\n    _scene[\'date\'] = date_obj\n\n\ndef scene_date():\n    return _scene[\'date\']\n\n\ndef _day_key(date_obj):\n    return date_obj.strftime(\'%Y-%m-%d\')\n\n\ndef _julian_day_0h(date_obj):\n    """Julian day at 0h UT of the date\'s calendar day."""\n    d = datetime(date_obj.year, date_obj.month, date_obj.day)\n    epoch = datetime(2000, 1, 1, 12)\n    return 2451545.0 + (d - epoch).total_seconds() / 86400.0\n\n\ndef _now_iso():\n    return datetime.now(timezone.utc).isoformat()\n\n\n# ----------------------------------------------------------------------\n# Geometry. Pure functions, no network; the tests call these directly.\n# ----------------------------------------------------------------------\n\ndef unit_from_ra_dec(ra_deg, dec_deg):\n    ra, dec = math.radians(ra_deg), math.radians(dec_deg)\n    return (math.cos(dec) * math.cos(ra),\n            math.cos(dec) * math.sin(ra),\n            math.sin(dec))\n\n\ndef icrf_to_ecliptic_j2000(vec, frame_obliquity_deg=EARTH_OBLIQUITY_J2000_DEG):\n    """Rotate an ICRF direction about the x-axis into the ecliptic of J2000.\n\n    The same rotation idealized_orbits.py applies to every pole, by the\n    frame\'s defining angle (84381.448 arcseconds, the Horizons manual).\n    """\n    x, y, z = vec\n    e = math.radians(frame_obliquity_deg)\n    return (x,\n            y * math.cos(e) + z * math.sin(e),\n            -y * math.sin(e) + z * math.cos(e))\n\n\ndef orbit_pole_ecliptic(incl_deg, node_deg):\n    """The unit normal of an orbit with this inclination and node,\n    in the frame the elements are given against."""\n    i, o = math.radians(incl_deg), math.radians(node_deg)\n    return (math.sin(i) * math.sin(o),\n            -math.sin(i) * math.cos(o),\n            math.cos(i))\n\n\ndef angle_between_deg(a, b):\n    dot = sum(p * q for p, q in zip(a, b))\n    na = math.sqrt(sum(p * p for p in a))\n    nb = math.sqrt(sum(q * q for q in b))\n    cosang = max(-1.0, min(1.0, dot / (na * nb)))\n    return math.degrees(math.acos(cosang))\n\n\ndef tilt_of_date_deg(pole_ra_deg, pole_dec_deg, orbit_incl_deg,\n                     orbit_node_deg,\n                     frame_obliquity_deg=EARTH_OBLIQUITY_J2000_DEG):\n    """Angle between Earth\'s pole and the barycenter\'s orbit pole."""\n    pole = icrf_to_ecliptic_j2000(unit_from_ra_dec(pole_ra_deg, pole_dec_deg),\n                                  frame_obliquity_deg)\n    return angle_between_deg(pole, orbit_pole_ecliptic(orbit_incl_deg,\n                                                       orbit_node_deg))\n\n\n# ----------------------------------------------------------------------\n# Fetching. astroquery is imported only when a fetch happens.\n# ----------------------------------------------------------------------\n\ndef fetch_pole(jd):\n    """(ra_deg, dec_deg) of Earth\'s north pole on JD `jd` (UT), ICRF."""\n    from astroquery.jplhorizons import Horizons\n    obj = Horizons(id=POLE_QUERY[\'target\'], location=POLE_QUERY[\'observer\'],\n                   epochs=jd)\n    table = obj.ephemerides(quantities=POLE_QUERY[\'quantity\'])\n    return float(table[\'NPole_RA\'][0]), float(table[\'NPole_DEC\'][0])\n\n\ndef fetch_orbit(jd):\n    """(inclination_deg, node_deg) of the Earth-Moon barycenter\'s orbit.\n\n    Element epochs are read by Horizons as TDB, the pole\'s as UT; the same\n    Julian day is passed to both. The two time scales differ by about a\n    minute, over which neither direction moves by anything drawn.\n    """\n    from astroquery.jplhorizons import Horizons\n    obj = Horizons(id=ORBIT_QUERY[\'target\'], location=ORBIT_QUERY[\'center\'],\n                   epochs=jd)\n    table = obj.elements(refplane=ORBIT_QUERY[\'refplane\'])\n    return float(table[\'incl\'][0]), float(table[\'Omega\'][0])\n\n\ndef _read_cache(path):\n    try:\n        with open(path, \'r\', encoding=\'utf-8\') as handle:\n            data = json.load(handle)\n        return data if isinstance(data, dict) else {}\n    except (OSError, ValueError):\n        return {}\n\n\ndef _write_cache(path, data):\n    try:\n        os.makedirs(os.path.dirname(path), exist_ok=True)\n        tmp = path + \'.tmp\'\n        with open(tmp, \'w\', encoding=\'utf-8\') as handle:\n            json.dump(data, handle, indent=1, sort_keys=True)\n        os.replace(tmp, path)\n    except OSError as exc:\n        print(\'[EARTH POLE] could not write %s: %s\' % (path, exc), flush=True)\n\n\ndef resolve(date_obj, cache_path=None, fetch_pole_fn=None, fetch_orbit_fn=None):\n    """Everything the drawing needs for `date_obj`, as one dict.\n\n    Keys: ra_deg, dec_deg (the pole drawn), tilt_deg (None on fallback),\n    day (YYYY-MM-DD), status (\'fetched\', \'cached\' or \'fallback\'), reason\n    (words, on fallback), pole_source and orbit_source (source blocks).\n    The fetch functions can be swapped in by the tests.\n    """\n    cache_path = cache_path or CACHE_PATH\n    fetch_pole_fn = fetch_pole_fn or fetch_pole\n    fetch_orbit_fn = fetch_orbit_fn or fetch_orbit\n    fallback = {\'ra_deg\': EARTH_POLE_RA_J2000_DEG,\n                \'dec_deg\': EARTH_POLE_DEC_J2000_DEG,\n                \'tilt_deg\': None, \'day\': None, \'status\': \'fallback\',\n                \'reason\': \'no plot date was given\', \'pole_source\': None,\n                \'orbit_source\': None}\n    if date_obj is None:\n        return fallback\n    day = _day_key(date_obj)\n    fallback[\'day\'] = day\n    cache = _read_cache(cache_path)\n    entry = cache.get(day)\n    status = \'cached\'\n    if not (isinstance(entry, dict) and \'pole\' in entry and \'orbit\' in entry):\n        jd = _julian_day_0h(date_obj)\n        try:\n            ra, dec = fetch_pole_fn(jd)\n            incl, node = fetch_orbit_fn(jd)\n        except Exception as exc:                      # noqa: BLE001\n            print(\'[EARTH POLE] Horizons fetch failed for %s: %s -- drawing \'\n                  \'the frame\\\'s year-2000 axis instead\' % (day, exc),\n                  flush=True)\n            fallback[\'reason\'] = \'Horizons could not be reached\'\n            return fallback\n        now = _now_iso()\n        entry = {\n            \'pole\': {\'ra_deg\': ra, \'dec_deg\': dec},\n            \'orbit\': {\'incl_deg\': incl, \'node_deg\': node},\n            \'pole_source\': {\'query_target\': POLE_QUERY[\'target\'],\n                            \'observer\': POLE_QUERY[\'observer\'],\n                            \'quantity\': POLE_QUERY[\'quantity\'],\n                            \'epoch_jd_ut\': jd, \'retrieved\': now},\n            \'orbit_source\': {\'query_target\': ORBIT_QUERY[\'target\'],\n                             \'center\': ORBIT_QUERY[\'center\'],\n                             \'refplane\': ORBIT_QUERY[\'refplane\'],\n                             \'epoch_jd\': jd, \'retrieved\': now},\n        }\n        cache[day] = entry\n        _write_cache(cache_path, cache)\n        status = \'fetched\'\n    tilt = tilt_of_date_deg(entry[\'pole\'][\'ra_deg\'], entry[\'pole\'][\'dec_deg\'],\n                            entry[\'orbit\'][\'incl_deg\'],\n                            entry[\'orbit\'][\'node_deg\'])\n    return {\'ra_deg\': entry[\'pole\'][\'ra_deg\'],\n            \'dec_deg\': entry[\'pole\'][\'dec_deg\'],\n            \'tilt_deg\': tilt, \'day\': day, \'status\': status, \'reason\': None,\n            \'pole_source\': entry.get(\'pole_source\'),\n            \'orbit_source\': entry.get(\'orbit_source\')}\n\n\ndef _current():\n    date_obj = _scene[\'date\']\n    key = _day_key(date_obj) if date_obj is not None else None\n    if key not in _memo:\n        _memo[key] = resolve(date_obj)\n    return _memo[key]\n\n\ndef pole_of_scene_date():\n    """{\'ra\': deg, \'dec\': deg} of the pole to draw, in planet_poles\' shape."""\n    got = _current()\n    return {\'ra\': got[\'ra_deg\'], \'dec\': got[\'dec_deg\']}\n\n\ndef tilt_hover_text():\n    """The Obliquity line of Earth\'s axis hover, in plain words."""\n    got = _current()\n    if got[\'tilt_deg\'] is None:\n        return (\'not shown: %s,<br>so the axis drawn is the frame\\\'s axis, \'\n                \'Earth\\\'s average pole of the year 2000\' % got[\'reason\'])\n    return (\'%.*g deg on %s,<br>measured against the Earth-Moon orbit that \'\n            \'day (JPL Horizons).<br>It includes Earth\\\'s small nod, so it \'\n            \'differs slightly<br>from the smoothed textbook value. The axis \'\n            \'also circles<br>slowly over thousands of years\'\n            % (TILT_FIGURES, got[\'tilt_deg\'], got[\'day\']))\n'),
    ('test_earth_pole_of_date.py', '873903578d0d37246421fb92fb1585cf',
     '"""\ntest_earth_pole_of_date.py - offline checks of Earth\'s pole and tilt of date.\n\nWHAT THIS CHECKS, and what it cannot\n\n    It never contacts Horizons. It checks the geometry, the fallback, the\n    cache and the hover words of earth_pole_of_date.py, and that the\n    orrery\'s pole transform really uses the pole of date for Earth. Whether\n    Horizons returns what the module expects is checked by\n    earth_pole_live_check.py, which does fetch.\n\n    1. The worked case in the build manifest (rev 3, section 0): the\n       fetched pole of 2026-Jan-01, 0.71450 / 89.85464, against the orbit\n       the cache served on 2026-09-23, gives 23.43598 degrees.\n    2. The geometry against ERFA, the IAU\'s SOFA routines as astropy ships\n       them (pyerfa). For three dates, ERFA\'s own true pole of date\n       (eraPnm06a) and its ecliptic of date (eraEcm06) are fed through this\n       module\'s conversions, and the tilt must equal ERFA\'s true obliquity\n       of date, the IAU 2006 mean obliquity (eraObl06) plus the nutation in\n       obliquity (eraNut06a), to 0.001 arcseconds. This tests the code\'s\n       geometry with an independent implementation of the same physics; it\n       is not a test of Horizons.\n    3. With a fetch that fails, the drawn pole is the fallback pair in\n       constants_new.py, no tilt is given, and the reason is recorded.\n    4. A fetched date is written to the cache and read back without a\n       second fetch.\n    5. The hover line prints the tilt at seven figures with its date, and\n       on fallback says why no tilt is shown.\n    6. create_planet_transformation_matrix(\'Earth\') in idealized_orbits.py\n       draws the pole of the scene\'s date, and the frame\'s axis when there\n       is none.\n\nRUN COMMAND\n\n    Open in VS Code and click Run. The orrery maintenance run also runs it,\n    as "Earth pole of date".\n\nRole: test\nDomain: orrery\n\nModule created: September 23, 2026 with Anthropic\'s Claude Opus 5.5\n(L-322 Stage D, patch D3)\n"""\n\nimport math\nimport os\nimport shutil\nimport sys\nimport tempfile\n\nHERE = os.path.dirname(os.path.abspath(__file__))\nif HERE not in sys.path:\n    sys.path.insert(0, HERE)\n\nimport earth_pole_of_date as epd                     # noqa: E402\nfrom constants_new import (                           # noqa: E402\n    EARTH_POLE_RA_J2000_DEG, EARTH_POLE_DEC_J2000_DEG)\n\nRESULTS = []\n\n\ndef check(name, ok, detail):\n    RESULTS.append((name, ok, detail))\n    print(\'  %-4s %-44s %s\' % (\'ok\' if ok else \'FAIL\', name, detail))\n\n\ndef test_worked_case():\n    got = epd.tilt_of_date_deg(0.71450, 89.85464,\n                               0.005556904467098324, 176.69335175006)\n    want = 23.43598\n    check(\'worked case (manifest rev 3 section 0)\',\n          abs(got - want) < 0.5e-5,\n          \'computed %.8f deg, manifest reports %.5f\' % (got, want))\n\n\ndef _erfa_inputs(jd):\n    import erfa\n    cip = erfa.pnm06a(jd, 0.0)[2]\n    ecl = erfa.ecm06(jd, 0.0)[2]\n    ra = math.degrees(math.atan2(cip[1], cip[0])) % 360.0\n    dec = math.degrees(math.asin(cip[2]))\n    n = epd.icrf_to_ecliptic_j2000(tuple(float(v) for v in ecl))\n    incl = math.degrees(math.acos(n[2]))\n    node = math.degrees(math.atan2(n[0], -n[1])) % 360.0\n    _dpsi, deps = erfa.nut06a(jd, 0.0)\n    true_obl = math.degrees(erfa.obl06(jd, 0.0) + deps)\n    return ra, dec, incl, node, true_obl\n\n\ndef test_against_erfa():\n    try:\n        import erfa                                    # noqa: F401\n    except ImportError:\n        check(\'geometry against ERFA\', False,\n              \'pyerfa is not installed, so this check could not run\')\n        return\n    for label, jd in ((\'2000-01-01.5\', 2451545.0),\n                      (\'2026-09-23\', 2461306.5),\n                      (\'2100-01-01\', 2488070.0)):\n        ra, dec, incl, node, want = _erfa_inputs(jd)\n        got = epd.tilt_of_date_deg(ra, dec, incl, node)\n        diff = abs(got - want) * 3600.0\n        check(\'geometry against ERFA, %s\' % label, diff < 0.001,\n              \'tilt %.9f, ERFA true obliquity %.9f, differ %.2g arcsec\'\n              % (got, want, diff))\n\n\ndef _fake_ok(calls):\n    def pole(jd):\n        calls.append((\'pole\', jd))\n        return 0.71450, 89.85464\n\n    def orbit(jd):\n        calls.append((\'orbit\', jd))\n        return 0.005556904467098324, 176.69335175006\n    return pole, orbit\n\n\ndef _fail(jd):\n    raise RuntimeError(\'no network in this test\')\n\n\ndef test_fallback_and_cache(tmp):\n    from datetime import datetime\n    day = datetime(2026, 1, 1)\n    path = os.path.join(tmp, \'cache.json\')\n    got = epd.resolve(day, cache_path=path, fetch_pole_fn=_fail,\n                      fetch_orbit_fn=_fail)\n    check(\'fallback draws the frame axis\',\n          got[\'status\'] == \'fallback\'\n          and got[\'ra_deg\'] == EARTH_POLE_RA_J2000_DEG\n          and got[\'dec_deg\'] == EARTH_POLE_DEC_J2000_DEG\n          and got[\'tilt_deg\'] is None,\n          \'status %s, pole %s / %s, tilt %s\'\n          % (got[\'status\'], got[\'ra_deg\'], got[\'dec_deg\'], got[\'tilt_deg\']))\n    check(\'fallback records why\', got[\'reason\'] == \'Horizons could not be \'\n          \'reached\', \'reason: %r\' % got[\'reason\'])\n    check(\'fallback writes no cache\', not os.path.exists(path),\n          \'cache file present: %s\' % os.path.exists(path))\n    calls = []\n    pole, orbit = _fake_ok(calls)\n    got = epd.resolve(day, cache_path=path, fetch_pole_fn=pole,\n                      fetch_orbit_fn=orbit)\n    check(\'first fetch is fetched and cached\',\n          got[\'status\'] == \'fetched\' and os.path.exists(path)\n          and len(calls) == 2,\n          \'status %s, %d fetch call(s), cache written: %s\'\n          % (got[\'status\'], len(calls), os.path.exists(path)))\n    again = epd.resolve(day, cache_path=path, fetch_pole_fn=_fail,\n                        fetch_orbit_fn=_fail)\n    check(\'second read comes from the cache\',\n          again[\'status\'] == \'cached\' and again[\'tilt_deg\'] == got[\'tilt_deg\'],\n          \'status %s, tilt %s\' % (again[\'status\'], again[\'tilt_deg\']))\n    check(\'cache keeps both source blocks\',\n          (again[\'pole_source\'] or {}).get(\'query_target\') == \'399\'\n          and (again[\'orbit_source\'] or {}).get(\'query_target\') == \'3\',\n          \'pole target %s, orbit target %s\'\n          % ((again[\'pole_source\'] or {}).get(\'query_target\'),\n             (again[\'orbit_source\'] or {}).get(\'query_target\')))\n\n\ndef test_hover_and_transform():\n    from datetime import datetime\n    import idealized_orbits\n    saved = dict(epd._memo), epd._scene[\'date\']\n    try:\n        fetched = {\'ra_deg\': 0.71450, \'dec_deg\': 89.85464,\n                   \'tilt_deg\': 23.435979372358, \'day\': \'2026-01-01\',\n                   \'status\': \'fetched\', \'reason\': None,\n                   \'pole_source\': None, \'orbit_source\': None}\n        epd.set_scene_date(datetime(2026, 1, 1))\n        epd._memo.clear()\n        epd._memo[\'2026-01-01\'] = fetched\n        text = epd.tilt_hover_text()\n        check(\'hover prints the tilt at seven figures with its date\',\n              text.startswith(\'23.43598 deg on 2026-01-01\'), text[:48])\n        m = idealized_orbits.create_planet_transformation_matrix(\'Earth\')\n        want = epd.icrf_to_ecliptic_j2000(epd.unit_from_ra_dec(0.71450,\n                                                               89.85464))\n        col = [float(m[k][2]) for k in range(3)]\n        err = max(abs(a - b) for a, b in zip(col, want))\n        check(\'the Earth transform draws the pole of date\', err < 1e-12,\n              \'largest difference %.2g\' % err)\n        epd.set_scene_date(None)\n        epd._memo.clear()\n        text = epd.tilt_hover_text()\n        check(\'hover on fallback says why\',\n              text.startswith(\'not shown: no plot date was given\'), text[:48])\n        m = idealized_orbits.create_planet_transformation_matrix(\'Earth\')\n        want = epd.icrf_to_ecliptic_j2000(epd.unit_from_ra_dec(\n            EARTH_POLE_RA_J2000_DEG, EARTH_POLE_DEC_J2000_DEG))\n        col = [float(m[k][2]) for k in range(3)]\n        err = max(abs(a - b) for a, b in zip(col, want))\n        check(\'with no date the Earth transform draws the frame axis\',\n              err < 1e-12, \'largest difference %.2g\' % err)\n    finally:\n        epd._memo.clear()\n        epd._memo.update(saved[0])\n        epd._scene[\'date\'] = saved[1]\n\n\ndef main():\n    print(\'=\' * 70)\n    print(\'EARTH POLE OF DATE -- offline checks (no Horizons contact)\')\n    print(\'=\' * 70)\n    tmp = tempfile.mkdtemp(prefix=\'earth_pole_test_\')\n    try:\n        test_worked_case()\n        test_against_erfa()\n        test_fallback_and_cache(tmp)\n        test_hover_and_transform()\n    finally:\n        shutil.rmtree(tmp, ignore_errors=True)\n    failed = [name for name, ok, _d in RESULTS if not ok]\n    print(\'\')\n    if failed:\n        print(\'EARTH POLE OF DATE: %d of %d checks FAILED: %s\'\n              % (len(failed), len(RESULTS), \', \'.join(failed)))\n        return 1\n    print(\'EARTH POLE OF DATE: all %d checks passed (geometry, ERFA, \'\n          \'fallback, cache, hover, transform).\' % len(RESULTS))\n    return 0\n\n\nif __name__ == \'__main__\':\n    sys.exit(main())\n'),
    ('earth_pole_live_check.py', 'd656ad97b38979a41105d1d4ca2ebac0',
     '"""\nearth_pole_live_check.py - fetch Earth\'s pole and orbit from Horizons and\ncheck the tilt of date against an independent calculation.\n\nWHY THIS EXISTS\n\n    test_earth_pole_of_date.py never contacts Horizons, so it cannot show\n    that Horizons answers the two queries the way earth_pole_of_date.py\n    expects. This script does contact it, and it is the first live test of\n    those queries. It writes nothing: no cache, no file.\n\nWHAT IT PRINTS\n\n    For five dates (2000-01-01, the first of this month, today, 2050-01-01\n    and 2100-01-01):\n      - the pole Horizons returns (quantity 32, target 399);\n      - the tilt against the Earth-Moon barycenter\'s orbit (target 3), the\n        value the orrery prints;\n      - the IAU 2006 mean obliquity and the true obliquity of the same\n        date, from ERFA (the SOFA routines astropy ships), and how far the\n        tilt is from each, in arcseconds.\n    The build manifest (rev 3, section 5) allows about 10 arcseconds\n    against the MEAN value, because the fetched pole carries Earth\'s nod.\n    Each date reports PASS or FAIL on that allowance.\n\n    Then, for eight dates a few days apart across one month, the tilt\n    measured against Earth\'s own orbit (target 399) beside the tilt\n    against the barycenter\'s. The spread of the difference is the monthly\n    wobble the manifest estimated at about 8 arcseconds from recalled\n    round figures; this replaces that estimate with a measured number.\n\nRUN COMMAND\n\n    Open this file in VS Code and click Run. It needs an internet\n    connection and takes a minute or two, because it asks Horizons about\n    thirty questions. If a query fails, it says which one and carries on.\n\nRole: diagnostic\nDomain: orrery\n\nModule created: September 23, 2026 with Anthropic\'s Claude Opus 5.5\n(L-322 Stage D, patch D3)\n"""\n\nimport math\nimport sys\nfrom datetime import datetime, timedelta, timezone\n\nimport earth_pole_of_date as epd\n\n# Source: build manifest L-322 Stage D rev 3, section 5 -- the declared\n# allowance against the smoothed IAU 2006 value, about 10 arcseconds,\n# because the fetched pole carries Earth\'s nod (nutation). A test\n# allowance, not a measurement.\nALLOWANCE_ARCSEC = 10.0\n\n\ndef _earth_orbit(jd):\n    from astroquery.jplhorizons import Horizons\n    table = Horizons(id=\'399\', location=\'@sun\', epochs=jd).elements(\n        refplane=\'ecliptic\')\n    return float(table[\'incl\'][0]), float(table[\'Omega\'][0])\n\n\ndef _erfa(jd):\n    import erfa\n    mean = math.degrees(erfa.obl06(jd, 0.0))\n    _dpsi, deps = erfa.nut06a(jd, 0.0)\n    return mean, mean + math.degrees(deps)\n\n\ndef main():\n    today = datetime.now(timezone.utc).replace(tzinfo=None)\n    dates = [datetime(2000, 1, 1), datetime(today.year, today.month, 1),\n             datetime(today.year, today.month, today.day),\n             datetime(2050, 1, 1), datetime(2100, 1, 1)]\n    print(\'=\' * 70)\n    print(\'EARTH POLE LIVE CHECK -- JPL Horizons, compared with ERFA\')\n    print(\'=\' * 70)\n    failures = 0\n    for d in dates:\n        jd = epd._julian_day_0h(d)\n        try:\n            ra, dec = epd.fetch_pole(jd)\n            incl, node = epd.fetch_orbit(jd)\n        except Exception as exc:                          # noqa: BLE001\n            print(\'%s  FETCH FAILED: %s\' % (d.date(), exc))\n            failures += 1\n            continue\n        tilt = epd.tilt_of_date_deg(ra, dec, incl, node)\n        mean, true = _erfa(jd)\n        d_mean = (tilt - mean) * 3600.0\n        d_true = (tilt - true) * 3600.0\n        ok = abs(d_mean) <= ALLOWANCE_ARCSEC\n        failures += 0 if ok else 1\n        print(\'%s  pole %.5f / %.5f   tilt %.7f deg\' % (d.date(), ra, dec,\n                                                         tilt))\n        print(\'            ERFA mean %.7f (tilt minus mean %+.2f arcsec, %s)\'\n              % (mean, d_mean, \'PASS\' if ok else \'FAIL\'))\n        print(\'            ERFA true %.7f (tilt minus true %+.2f arcsec)\'\n              % (true, d_true))\n    print(\'\')\n    print(\'Monthly wobble: tilt against Earth\\\'s own orbit minus tilt \'\n          \'against the barycenter\\\'s\')\n    start = datetime(today.year, today.month, 1)\n    diffs = []\n    for k in range(8):\n        d = start + timedelta(days=4 * k)\n        jd = epd._julian_day_0h(d)\n        try:\n            ra, dec = epd.fetch_pole(jd)\n            bi, bn = epd.fetch_orbit(jd)\n            ei, en = _earth_orbit(jd)\n        except Exception as exc:                          # noqa: BLE001\n            print(\'  %s  FETCH FAILED: %s\' % (d.date(), exc))\n            continue\n        diff = (epd.tilt_of_date_deg(ra, dec, ei, en)\n                - epd.tilt_of_date_deg(ra, dec, bi, bn)) * 3600.0\n        diffs.append(diff)\n        print(\'  %s  %+.2f arcsec\' % (d.date(), diff))\n    if diffs:\n        print(\'  spread over the month: %.2f arcsec (largest minus smallest)\'\n              % (max(diffs) - min(diffs)))\n    print(\'\')\n    if failures:\n        print(\'EARTH POLE LIVE CHECK: %d date(s) FAILED or could not be \'\n              \'fetched. Copy this whole output into the chat.\' % failures)\n        return 1\n    print(\'EARTH POLE LIVE CHECK: every date within %.0f arcseconds of the \'\n          \'IAU 2006 mean. Copy this whole output into the chat.\'\n          % ALLOWANCE_ARCSEC)\n    return 0\n\n\nif __name__ == \'__main__\':\n    sys.exit(main())\n'),
]


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
        if b"EARTH_OBLIQUITY_J2000_DEG" not in handle.read():
            print("ERROR: patch D2 has not been applied (constants_new.py "
                  "has no EARTH_OBLIQUITY_J2000_DEG row). Run "
                  "patch_L322_D_2_orrery_rows_and_poles_20260923.py first. "
                  "NOTHING was written.")
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
    print("  1. Run earth_pole_live_check.py (open it in VS Code, click "
          "Run). It fetches from Horizons and needs the internet; it takes "
          "a minute or two. Copy its whole output into the chat. It is the "
          "first live test of the two new queries.")
    print("  2. Run the orrery maintenance run. The new line 'Earth pole "
          "of date' should pass. Constants change should be quiet: this "
          "patch does not touch constants_new.py.")
    print("  3. Plot Earth as the center with its axis shown, for today. "
          "Its hover should read 'Obliquity: 23.43... deg on <today>, "
          "measured against the Earth-Moon orbit that day'. The first plot "
          "of a new date fetches, so it is a little slower. The console "
          "prints a line starting [EARTH POLE] if the fetch failed.")
    print("  4. Commit and push, including data/earth_pole_cache.json.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
