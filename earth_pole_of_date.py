"""
earth_pole_of_date.py - Earth's rotation pole and tilt for the date of a plot.

Earth's axis is not fixed. It slowly circles over thousands of years
(precession) and nods slightly (nutation), and the plane of Earth's orbit
moves too. So the direction the orrery draws for Earth's axis, and the tilt
it prints, belong to a date. This module fetches both for the date of the
plot from JPL Horizons, keeps them in a small cache, and falls back to the
frame's own axis when Horizons cannot be reached.

WHAT IS FETCHED, AND WHY THESE TWO

    1. Earth's north pole direction on the date: Horizons observer quantity
       32 ("N.Pole-RA N.Pole-DC") for target 399, Earth itself. Horizons
       returns its right ascension and declination in the ICRF, from its
       high-precision Earth model. astroquery names the two columns
       NPole_RA and NPole_DEC.
    2. The orbit of the Earth-Moon barycenter on the same date: osculating
       elements for Horizons target 3 about the Sun, against the ecliptic
       of J2000. Not Earth's own orbit (target 399). The Horizons manual
       says osculating elements of 399 about the Sun carry short-period
       oscillations from Earth's motion about the Earth-Moon barycenter,
       and the ecliptic that Earth's tilt is measured against is the
       barycenter's orbit plane (Tony's ruling, 2026-09-23, build manifest
       rev 3 section 0).

    The observer for the pole query is the Sun, not the geocenter, because
    an observer table of Earth seen from Earth's own center is not a
    meaningful request. The light time from the Sun, about eight minutes,
    shifts the pole by far less than anything drawn: the manifest measured
    the pole about 0.15 degrees from the year-2000 axis after 26 years,
    and eight minutes is a few ten-millionths of that span.

HOW THE TILT IS COMPUTED

    tilt_of_date_deg() turns the fetched pole from the ICRF into the
    drawing's frame (the ecliptic of J2000) by the frame's defining angle,
    EARTH_OBLIQUITY_J2000_DEG in constants_new.py. It turns the barycenter's
    inclination and node into the pole of its orbit in the same frame. The
    tilt is the angle between the two directions. Nothing here types a
    tilt, a rate or a textbook formula. The value includes Earth's nod at
    that instant, so it is not the smoothed mean value a textbook gives.
    ERFA, the IAU's SOFA routines as astropy ships them, is the independent
    check: test_earth_pole_of_date.py tests this geometry against ERFA's
    true obliquity of date offline, and earth_pole_live_check.py tests the
    fetched values against it live.

WHAT HAPPENS WHEN HORIZONS CANNOT BE REACHED

    The pole is the fallback pair in constants_new.py,
    EARTH_POLE_RA_J2000_DEG and EARTH_POLE_DEC_J2000_DEG: the frame's own
    axis, which is Earth's mean pole of the year 2000. No tilt is printed.
    The axis hover says which of the two the drawing shows and why
    (Graceful Fallback, protocol Part 2).

HOW IT IS USED

    palomas_orrery.py calls set_scene_date() just before it builds the
    center-body shells, in both the static plot and the animation (the
    animation uses its first frame's date). create_planet_transformation_
    matrix('Earth') in idealized_orbits.py then asks pole_of_scene_date()
    for the pole, and build_rotation_axis_traces() in
    planet_visualization_utilities.py asks tilt_hover_text() for the line
    it prints. With no scene date set -- a caller outside those two
    pipelines -- the fallback is used and nothing is fetched.

THE CACHE

    data/earth_pole_cache.json, keyed by the date at 0h UT, holds each
    fetched pole and barycenter orbit with its source block. A date already
    in the cache is not fetched again. Nothing in it is ever typed by hand.
    Delete the file to force fresh fetches.

RUN COMMAND

    Not run by itself. earth_pole_live_check.py, beside it, is the script
    you run to see a real fetch and the checks against it.

Role: data
Domain: orrery

Module created: September 23, 2026 with Anthropic's Claude Opus 5.5
(L-322 Stage D, patch D3: Earth's pole of date and tilt of date, fetched
from Horizons, from build manifest rev 3 sections 0 and 4.4)
Module updated: September 23, 2026 with Anthropic's Claude Opus 5.5
(L-322 Stage D, patch D4: the hover names the Earth-Moon barycenter,
the gravitational center of the Earth-Moon system, where it said the
Earth-Moon orbit; and the paragraph on the
independent check named the mean formula where the tests use ERFA's
true obliquity)
"""

import json
import math
import os
from datetime import datetime, timezone

from constants_new import (
    EARTH_OBLIQUITY_J2000_DEG,
    EARTH_POLE_DEC_J2000_DEG,
    EARTH_POLE_RA_J2000_DEG,
)

CACHE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          'data', 'earth_pole_cache.json')

POLE_QUERY = {'target': '399', 'observer': '@sun', 'quantity': '32'}
ORBIT_QUERY = {'target': '3', 'center': '@sun', 'refplane': 'ecliptic'}

# The tilt prints at seven significant figures. There is no stated
# uncertainty on a Horizons pole, so Rule 3's counting fallback decides:
# Horizons prints the pole's declination to five decimal places of a
# degree (89.85464, seven figures), and the tilt is set by that input.
TILT_FIGURES = 7

_scene = {'date': None}
_memo = {}


def set_scene_date(date_obj):
    """Record the date the next plot is drawn for (a datetime, UTC)."""
    _scene['date'] = date_obj


def scene_date():
    return _scene['date']


def _day_key(date_obj):
    return date_obj.strftime('%Y-%m-%d')


def _julian_day_0h(date_obj):
    """Julian day at 0h UT of the date's calendar day."""
    d = datetime(date_obj.year, date_obj.month, date_obj.day)
    epoch = datetime(2000, 1, 1, 12)
    return 2451545.0 + (d - epoch).total_seconds() / 86400.0


def _now_iso():
    return datetime.now(timezone.utc).isoformat()


# ----------------------------------------------------------------------
# Geometry. Pure functions, no network; the tests call these directly.
# ----------------------------------------------------------------------

def unit_from_ra_dec(ra_deg, dec_deg):
    ra, dec = math.radians(ra_deg), math.radians(dec_deg)
    return (math.cos(dec) * math.cos(ra),
            math.cos(dec) * math.sin(ra),
            math.sin(dec))


def icrf_to_ecliptic_j2000(vec, frame_obliquity_deg=EARTH_OBLIQUITY_J2000_DEG):
    """Rotate an ICRF direction about the x-axis into the ecliptic of J2000.

    The same rotation idealized_orbits.py applies to every pole, by the
    frame's defining angle (84381.448 arcseconds, the Horizons manual).
    """
    x, y, z = vec
    e = math.radians(frame_obliquity_deg)
    return (x,
            y * math.cos(e) + z * math.sin(e),
            -y * math.sin(e) + z * math.cos(e))


def orbit_pole_ecliptic(incl_deg, node_deg):
    """The unit normal of an orbit with this inclination and node,
    in the frame the elements are given against."""
    i, o = math.radians(incl_deg), math.radians(node_deg)
    return (math.sin(i) * math.sin(o),
            -math.sin(i) * math.cos(o),
            math.cos(i))


def angle_between_deg(a, b):
    dot = sum(p * q for p, q in zip(a, b))
    na = math.sqrt(sum(p * p for p in a))
    nb = math.sqrt(sum(q * q for q in b))
    cosang = max(-1.0, min(1.0, dot / (na * nb)))
    return math.degrees(math.acos(cosang))


def tilt_of_date_deg(pole_ra_deg, pole_dec_deg, orbit_incl_deg,
                     orbit_node_deg,
                     frame_obliquity_deg=EARTH_OBLIQUITY_J2000_DEG):
    """Angle between Earth's pole and the barycenter's orbit pole."""
    pole = icrf_to_ecliptic_j2000(unit_from_ra_dec(pole_ra_deg, pole_dec_deg),
                                  frame_obliquity_deg)
    return angle_between_deg(pole, orbit_pole_ecliptic(orbit_incl_deg,
                                                       orbit_node_deg))


# ----------------------------------------------------------------------
# Fetching. astroquery is imported only when a fetch happens.
# ----------------------------------------------------------------------

def fetch_pole(jd):
    """(ra_deg, dec_deg) of Earth's north pole on JD `jd` (UT), ICRF."""
    from astroquery.jplhorizons import Horizons
    obj = Horizons(id=POLE_QUERY['target'], location=POLE_QUERY['observer'],
                   epochs=jd)
    table = obj.ephemerides(quantities=POLE_QUERY['quantity'])
    return float(table['NPole_RA'][0]), float(table['NPole_DEC'][0])


def fetch_orbit(jd):
    """(inclination_deg, node_deg) of the Earth-Moon barycenter's orbit.

    Element epochs are read by Horizons as TDB, the pole's as UT; the same
    Julian day is passed to both. The two time scales differ by about a
    minute, over which neither direction moves by anything drawn.
    """
    from astroquery.jplhorizons import Horizons
    obj = Horizons(id=ORBIT_QUERY['target'], location=ORBIT_QUERY['center'],
                   epochs=jd)
    table = obj.elements(refplane=ORBIT_QUERY['refplane'])
    return float(table['incl'][0]), float(table['Omega'][0])


def _read_cache(path):
    try:
        with open(path, 'r', encoding='utf-8') as handle:
            data = json.load(handle)
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def _write_cache(path, data):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        tmp = path + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as handle:
            json.dump(data, handle, indent=1, sort_keys=True)
        os.replace(tmp, path)
    except OSError as exc:
        print('[EARTH POLE] could not write %s: %s' % (path, exc), flush=True)


def resolve(date_obj, cache_path=None, fetch_pole_fn=None, fetch_orbit_fn=None):
    """Everything the drawing needs for `date_obj`, as one dict.

    Keys: ra_deg, dec_deg (the pole drawn), tilt_deg (None on fallback),
    day (YYYY-MM-DD), status ('fetched', 'cached' or 'fallback'), reason
    (words, on fallback), pole_source and orbit_source (source blocks).
    The fetch functions can be swapped in by the tests.
    """
    cache_path = cache_path or CACHE_PATH
    fetch_pole_fn = fetch_pole_fn or fetch_pole
    fetch_orbit_fn = fetch_orbit_fn or fetch_orbit
    fallback = {'ra_deg': EARTH_POLE_RA_J2000_DEG,
                'dec_deg': EARTH_POLE_DEC_J2000_DEG,
                'tilt_deg': None, 'day': None, 'status': 'fallback',
                'reason': 'no plot date was given', 'pole_source': None,
                'orbit_source': None}
    if date_obj is None:
        return fallback
    day = _day_key(date_obj)
    fallback['day'] = day
    cache = _read_cache(cache_path)
    entry = cache.get(day)
    status = 'cached'
    if not (isinstance(entry, dict) and 'pole' in entry and 'orbit' in entry):
        jd = _julian_day_0h(date_obj)
        try:
            ra, dec = fetch_pole_fn(jd)
            incl, node = fetch_orbit_fn(jd)
        except Exception as exc:                      # noqa: BLE001
            print('[EARTH POLE] Horizons fetch failed for %s: %s -- drawing '
                  'the frame\'s year-2000 axis instead' % (day, exc),
                  flush=True)
            fallback['reason'] = 'Horizons could not be reached'
            return fallback
        now = _now_iso()
        entry = {
            'pole': {'ra_deg': ra, 'dec_deg': dec},
            'orbit': {'incl_deg': incl, 'node_deg': node},
            'pole_source': {'query_target': POLE_QUERY['target'],
                            'observer': POLE_QUERY['observer'],
                            'quantity': POLE_QUERY['quantity'],
                            'epoch_jd_ut': jd, 'retrieved': now},
            'orbit_source': {'query_target': ORBIT_QUERY['target'],
                             'center': ORBIT_QUERY['center'],
                             'refplane': ORBIT_QUERY['refplane'],
                             'epoch_jd': jd, 'retrieved': now},
        }
        cache[day] = entry
        _write_cache(cache_path, cache)
        status = 'fetched'
    tilt = tilt_of_date_deg(entry['pole']['ra_deg'], entry['pole']['dec_deg'],
                            entry['orbit']['incl_deg'],
                            entry['orbit']['node_deg'])
    return {'ra_deg': entry['pole']['ra_deg'],
            'dec_deg': entry['pole']['dec_deg'],
            'tilt_deg': tilt, 'day': day, 'status': status, 'reason': None,
            'pole_source': entry.get('pole_source'),
            'orbit_source': entry.get('orbit_source')}


def _current():
    date_obj = _scene['date']
    key = _day_key(date_obj) if date_obj is not None else None
    if key not in _memo:
        _memo[key] = resolve(date_obj)
    return _memo[key]


def pole_of_scene_date():
    """{'ra': deg, 'dec': deg} of the pole to draw, in planet_poles' shape."""
    got = _current()
    return {'ra': got['ra_deg'], 'dec': got['dec_deg']}


def tilt_hover_text():
    """The Obliquity line of Earth's axis hover, in plain words."""
    got = _current()
    if got['tilt_deg'] is None:
        return ('not shown: %s,<br>so the axis drawn is the frame\'s axis, '
                'Earth\'s average pole of the year 2000' % got['reason'])
    # L-322 Stage D, patch D4, Tony's wording of 2026-09-23: the orbit is
    # the Earth-Moon BARYCENTER's, the gravitational center of the
    # Earth-Moon system. "Earth-Moon orbit" could be read as the Moon's
    # orbit around Earth, a different plane about five degrees away.
    return ('%.*g deg on %s,<br>measured against the orbit of the '
            'Earth-Moon barycenter,<br>the gravitational center of the '
            'Earth-Moon system,<br>around the Sun that day (JPL Horizons).'
            '<br>It includes Earth\'s small nod, so it '
            'differs slightly<br>from the smoothed textbook value. The axis '
            'also circles<br>slowly over thousands of years'
            % (TILT_FIGURES, got['tilt_deg'], got['day']))
