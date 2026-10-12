"""
position_accuracy.py - How well JPL knows a plotted position, and the hover's
distances and speeds printed to the digits that knowledge earns.

The orrery's body hover printed every distance to ten decimal places of an
AU and ten figures of a kilometre, whatever JPL knows (L-401). This module
works out, for one body seen from one centre on one date, the error the
numbers carry, and formats each unit by it. Rulings:
documentation/DESIGN_L401_distance_digits_rulings_20261011.md and
documentation/HANDOFF_L401_distance_build1_brief_20261011.md.

WHERE EACH ERROR COMES FROM (one place; the hover reads only this)
    planet or Pluto   JPL's published accuracy for its orbit, the three
                      DE430 rows in constants_new.py (Folkner et al. 2014),
                      used as half a unit of each row's place
    the Moon          its own DE430 row, "known to submeter accuracy"
    a small body      JPL's own uncertainty for that date, from the same
                      Horizons vector query that returns the position,
                      VEC_TABLE='2xr', times three (3-sigma); fetched by
                      fetch_small_body_state() below
    anything else     "no stated error", its own state, never a tiny
                      invented number: a moon seen from its planet, a
                      spacecraft, a Lagrange point, a barycentre
    The plot's centre joins by the larger of the two errors (Tony,
    2026-10-01) when the body has an error of its own; a body with none
    keeps none, whatever the centre. A moon seen from the Sun uses its planet's row as a
    floor: a lower bound, said so in words. The Sun adds nothing on
    either side, since a planet's accuracy is that of its orbit about
    the Sun; seen from a spacecraft or a barycentre it has none.

HOW THE DIGITS ARE CHOSEN
    Each unit (AU, kilometers, light time, AU/day, km/hr, km/s) is placed
    by its own Report test (provenance-discipline 2.28, The ceiling,
    Report): the power of ten whose half-unit is nearest the error on a
    log scale, a tie to the coarser. A distance is never finer than whole
    kilometers, the stated floor. A speed with a stated distance error
    keeps the distance's relative precision ("Reading 1", Tony,
    2026-10-11); a small body's speed uses JPL's three velocity
    uncertainties combined, times three; a speed with no stated error is
    printed to one meter per second with a plain sentence (ruled
    2026-10-11). Never fewer than one figure; plain numbers, no
    scientific notation.

Key functions:
    resolve_accuracy() - the error state for one body, centre and date
    distance_speed_lines() - the hover's distance and speed lines, with
        the sentence that says which kind of figure they are
    fetch_small_body_state() - a small body's position with its 2xr
        uncertainties, by a direct call to the Horizons API

Consumed by: visualization_utils.format_detailed_hover_text (the static
plot, the animation and the social export) and palomas_orrery.fetch_position;
checked by test_position_digits.py.

Role: computation
Domain: orrery

Module created: October 12, 2026 with Anthropic's Claude Opus 5.5 (L-401,
build 1, the body hover).
"""

import math
import re

from constants_new import (
    KM_PER_AU,
    LIGHT_MINUTES_PER_AU,
    SPEED_OF_LIGHT_KM_S,
    S_PER_HOUR,
    S_PER_DAY,
    DE430_TERRESTRIAL_POSITION_PLACE_KM,
    DE430_JUPITER_SATURN_POSITION_PLACE_KM,
    DE430_URANUS_NEPTUNE_PLUTO_POSITION_PLACE_KM,
    DE430_MOON_POSITION_PLACE_KM,
    VOYAGER_1_POINTING_RA_2030_ARCSEC,
    VOYAGER_1_POINTING_DEC_2030_ARCSEC,
    VOYAGER_2_POINTING_RA_2030_ARCSEC,
    VOYAGER_2_POINTING_DEC_2030_ARCSEC,
    ARCSEC_PER_DEG,
    DEG_PER_RAD,
)
from orbital_period import report_exponent, format_by_error, _is_small_body

# ============================================================================
# THE ROWS, THE LEVEL AND THE FLOORS
# ============================================================================

# Which published row each body points at. Names, not values: the values
# live in constants_new.py with their sources.
PUBLISHED_ROW_NAMES = {
    'Mercury': 'DE430_TERRESTRIAL_POSITION_PLACE_KM',
    'Venus': 'DE430_TERRESTRIAL_POSITION_PLACE_KM',
    'Earth': 'DE430_TERRESTRIAL_POSITION_PLACE_KM',
    'Mars': 'DE430_TERRESTRIAL_POSITION_PLACE_KM',
    'Jupiter': 'DE430_JUPITER_SATURN_POSITION_PLACE_KM',
    'Saturn': 'DE430_JUPITER_SATURN_POSITION_PLACE_KM',
    'Uranus': 'DE430_URANUS_NEPTUNE_PLUTO_POSITION_PLACE_KM',
    'Neptune': 'DE430_URANUS_NEPTUNE_PLUTO_POSITION_PLACE_KM',
    'Pluto': 'DE430_URANUS_NEPTUNE_PLUTO_POSITION_PLACE_KM',
}
MOON_ROW_NAME = 'DE430_MOON_POSITION_PLACE_KM'

ROW_VALUES = {
    'DE430_TERRESTRIAL_POSITION_PLACE_KM': DE430_TERRESTRIAL_POSITION_PLACE_KM,
    'DE430_JUPITER_SATURN_POSITION_PLACE_KM': DE430_JUPITER_SATURN_POSITION_PLACE_KM,
    'DE430_URANUS_NEPTUNE_PLUTO_POSITION_PLACE_KM': DE430_URANUS_NEPTUNE_PLUTO_POSITION_PLACE_KM,
    'DE430_MOON_POSITION_PLACE_KM': DE430_MOON_POSITION_PLACE_KM,
    'VOYAGER_1_POINTING_RA_2030_ARCSEC': VOYAGER_1_POINTING_RA_2030_ARCSEC,
    'VOYAGER_1_POINTING_DEC_2030_ARCSEC': VOYAGER_1_POINTING_DEC_2030_ARCSEC,
    'VOYAGER_2_POINTING_RA_2030_ARCSEC': VOYAGER_2_POINTING_RA_2030_ARCSEC,
    'VOYAGER_2_POINTING_DEC_2030_ARCSEC': VOYAGER_2_POINTING_DEC_2030_ARCSEC,
}

# Spacecraft whose own Horizons data sheet states a trajectory
# uncertainty: the Voyagers, as a predicted pointing uncertainty seen from
# Earth for 2030, an angle (the survey of all 26 sheets, 2026-10-12). The
# hover converts the larger of RA and DEC at the spacecraft's distance from
# Earth, and says the conversion is ours (Tony, 2026-10-12, option A).
SPACECRAFT_SHEET_ROWS = {
    'Voyager 1': ('VOYAGER_1_POINTING_RA_2030_ARCSEC', 'VOYAGER_1_POINTING_DEC_2030_ARCSEC'),
    'Voyager 2': ('VOYAGER_2_POINTING_RA_2030_ARCSEC', 'VOYAGER_2_POINTING_DEC_2030_ARCSEC'),
}
SHEET_FIGURES = 4   # the sheets print four figures (the rows' # Figures: lines)

# These four are display rules, not measurements. Each is cited to the
# ruling it comes from.

HALF_UNIT = 0.5
# Source: provenance-discipline 2.28, An Accuracy Stated in Words Is
# Source+: Stored as the Place It Reports To -- a row stores the place its
# Source+: words report to, and "the display uses half a unit of the
# Source+: place" as the source's error.

SIGMA_MULTIPLE = 3
# Source: documentation/DESIGN_L401_distance_digits_rulings_20261011.md,
# Source+: section 4, item 5 -- "The level is 3-sigma". Horizons' 2xr
# Source+: columns are 1-sigma (the vector table's own column notes, read
# Source+: 2026-10-12), so every figure kept is three times that, and
# Source+: every field name says so.

DISTANCE_FLOOR_EXPONENT_KM = 0
# Source: documentation/DESIGN_L401_distance_digits_rulings_20261011.md,
# Source+: section 4, item 4 -- no stated error prints "to whole
# Source+: kilometres, the website's floor"; never finer for any body
# Source+: (provenance-discipline 2.28, A Computed Position Prints What
# Source+: Its Errors Earn). The exponent of ten in kilometers.

SPEED_FLOOR_EXPONENT_KM_S = -3
# Source: documentation/HANDOFF_L401_distance_build1_brief_20261011.md,
# Source+: section 2, Tony's ruling of 2026-10-11 ("approved as
# Source+: recommended") -- one meter per second, printed as 0.001 km/s,
# Source+: for a speed with no stated error. The exponent of ten in km/s.

# Centres with no solid surface: the surface line is left out for them,
# all three reviewers agreeing (brief section 1). Words, not values.
NO_SOLID_SURFACE = {'Sun', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Planet 9'}

# The one local pair JPL states an accuracy for: the Moon's orbit about
# Earth (and so about the Earth-Moon barycentre).
EARTH_MOON_SYSTEM = {'Moon', 'Earth', 'Earth-Moon Barycenter'}


def _floor_err_km():
    return HALF_UNIT * 10.0 ** DISTANCE_FLOOR_EXPONENT_KM


def _speed_floor_err_km_s():
    return HALF_UNIT * 10.0 ** SPEED_FLOOR_EXPONENT_KM_S


def _row_err_km(row_name):
    return HALF_UNIT * ROW_VALUES[row_name]


# ============================================================================
# WHO IS WHAT
# ============================================================================

def _entry(name, objects):
    for o in objects or ():
        if o.get('name') == name:
            return o
    return None


def parent_of(name, parent_planets):
    """The body a satellite orbits, from parent_planets; a barycentre key is
    used only when no body key lists it."""
    found = None
    for key, members in (parent_planets or {}).items():
        if name in members:
            if 'Barycenter' not in key:
                return key
            found = found or key
    return found


def is_local_pair(a, b, parent_planets):
    pp = parent_planets or {}
    return a in pp.get(b, ()) or b in pp.get(a, ())


def is_small_body_fetch(object_id, id_type):
    """Is this a Horizons small-body target, which states its own
    uncertainty? orbital_period's test by id_type, plus a small-body
    record number (9 followed by seven digits), whatever its id_type: a
    comet pinned by record can be listed with id_type 'id'."""
    if object_id is None:
        return False
    if _is_small_body(object_id, id_type):
        return True
    return bool(re.match(r'^9\d{7}$', str(object_id).strip()))


def _finite_positive(x):
    try:
        x = float(x)
    except (TypeError, ValueError):
        return None
    return x if (math.isfinite(x) and x > 0) else None


def body_kind(name, center_name, objects, parent_planets, obj_data=None):
    """
    One of: 'sun', 'planet', 'moon' (Earth's), 'satellite', 'small_body',
    'small_body_other_record', 'not_from_jpl', 'unstated'.
    """
    if obj_data is not None and (obj_data.get('analytical_position')
                                 or obj_data.get('not_fetched_for_date')):
        return 'not_from_jpl'
    if name == 'Sun':
        return 'sun'
    if name in PUBLISHED_ROW_NAMES:
        return 'planet'
    if name == 'Moon':
        return 'moon'
    if name in SPACECRAFT_SHEET_ROWS:
        return 'spacecraft_sheet'
    entry = _entry(name, objects) or {}
    otype = entry.get('object_type')
    if otype in ('hypothetical', 'exoplanet', 'exo_host_star', 'exo_binary_star',
                 'exo_barycenter'):
        return 'not_from_jpl'
    if otype == 'satellite':
        return 'satellite'
    fetch_id, fetch_type = entry.get('id'), entry.get('id_type')
    if 'helio_id' in entry:
        if center_name == 'Sun':
            # palomas_orrery.py fetches these by their small-body solution
            # in a Sun-centred plot.
            fetch_id, fetch_type = entry['helio_id'], 'smallbody'
        elif is_small_body_fetch(entry['helio_id'], 'smallbody'):
            # From any other centre the system's record is fetched, which
            # carries no uncertainty; JPL states one for the small body.
            return 'small_body_other_record'
    if is_small_body_fetch(fetch_id, fetch_type):
        return 'small_body'
    return 'unstated'


def _gap(name, reason, what=None):
    """The words for a part with no figure, true to why it has none."""
    what = what or "%s's position" % name
    if reason == 'not_fetched':
        return "JPL's figure for %s is not included here" % what
    if reason == 'not_from_jpl':
        return 'no accuracy is stated for %s' % what
    # An unstated error is not a large one: a spacecraft is tracked by its
    # radio signal's travel time and a moon by its orbit fit, so nothing
    # here says the true uncertainty may be larger (Tony, 2026-10-12).
    return 'JPL states no accuracy for %s' % what


def _none_side(name, reason, what=None):
    return {'kind': 'none', 'name': name, 'reason': reason,
            'gap': _gap(name, reason, what)}


def _may_be_larger(sides):
    """Only a part JPL does give a figure for that is not included here,
    or a position not from JPL at all, can make the true uncertainty
    larger than the one printed; a part JPL simply states no figure for is
    not, by that alone, a large one."""
    return any(s.get('reason') in ('not_fetched', 'not_from_jpl') for s in sides)


def _side(name, role, center_name, obj_data, objects, parent_planets):
    """
    One side of the pair: the error that body's own position carries.
    kind: 'reference', 'published', 'computed', 'floor' or 'none'.
    """
    kind = body_kind(name, center_name, objects, parent_planets,
                     obj_data if role == 'body' else None)
    if kind == 'sun':
        # The Sun adds nothing on either side: a planet's published
        # accuracy is the accuracy of its orbit about the Sun, so the Sun
        # seen from Earth is as well known as Earth seen from the Sun. Seen
        # from a spacecraft or a barycentre the other side states nothing,
        # and the pair has no stated error.
        return {'kind': 'reference', 'name': name}
    if kind == 'planet':
        row = PUBLISHED_ROW_NAMES[name]
        return {'kind': 'published', 'name': name, 'err_km': _row_err_km(row),
                'row': row, 'who': name}
    if kind == 'moon':
        # About the Sun the Moon is Earth's orbit plus the Moon's about
        # Earth; both are published, and the larger governs.
        earth = _row_err_km(PUBLISHED_ROW_NAMES['Earth'])
        moon = _row_err_km(MOON_ROW_NAME)
        if earth >= moon:
            return {'kind': 'published', 'name': name, 'err_km': earth,
                    'row': PUBLISHED_ROW_NAMES['Earth'], 'who': 'Earth'}
        return {'kind': 'published', 'name': name, 'err_km': moon,
                'row': MOON_ROW_NAME, 'who': 'the Moon'}
    if kind == 'satellite':
        parent = parent_of(name, parent_planets)
        if parent in PUBLISHED_ROW_NAMES:
            row = PUBLISHED_ROW_NAMES[parent]
            return {'kind': 'floor', 'name': name, 'err_km': _row_err_km(row),
                    'row': row, 'who': parent,
                    'gap': _gap(name, 'unstated',
                                "%s's orbit around %s" % (name, parent))}
        return _none_side(name, 'unstated')
    if kind == 'small_body':
        sig = (obj_data or {}).get('position_uncertainty') if role == 'body' else None
        err = _finite_positive(sig.get('range_3sigma_km')) if sig else None
        if err is not None:
            return {'kind': 'computed', 'name': name, 'err_km': err,
                    'speed_err_km_s': _finite_positive(sig.get('speed_3sigma_km_s')),
                    'who': name}
        return _none_side(name, 'not_fetched')
    if kind == 'small_body_other_record':
        return _none_side(name, 'not_fetched')
    if kind == 'spacecraft_sheet':
        earth = _finite_positive((obj_data or {}).get('earth_distance_au')) if role == 'body' else None
        if earth is None:
            # Its distance from Earth was not fetched (the animation, or a
            # centre): the sheet's figure is not included here.
            return _none_side(name, 'not_fetched')
        ra, dec = (ROW_VALUES[r] for r in SPACECRAFT_SHEET_ROWS[name])
        arcsec = max(ra, dec)
        err = arcsec / ARCSEC_PER_DEG / DEG_PER_RAD * earth * KM_PER_AU
        return {'kind': 'sheet', 'name': name, 'err_km': err, 'who': name,
                'arcsec': arcsec}
    if kind == 'not_from_jpl':
        return _none_side(name, 'not_from_jpl')
    return _none_side(name, 'unstated')


def resolve_accuracy(obj_name, center_name, obj_data, objects, parent_planets):
    """
    The error state for one body seen from one centre, with the position
    record it was fetched in (so keyed by body, centre and date).

    Returns a dict:
        state         'published', 'computed', 'floor', 'none' or 'center'
        err_km        the governing distance error, before the floor
                      (None for 'none' and 'center')
        governs_kind  'published' or 'computed': what kind of figure governs
        reason        for 'none': 'unstated', 'not_fetched' or 'not_from_jpl'
        who           the body whose figure governs
        gap           for 'floor' and 'none': the words for the part with
                      no figure, true to why it has none
        speed_err_km_s  a small body's combined velocity 3-sigma, or None
        row           the constants_new.py row that governs, or None
    """
    if obj_name == center_name:
        return {'state': 'center', 'err_km': None}
    if is_local_pair(obj_name, center_name, parent_planets):
        pair = {obj_name, center_name}
        if len(pair) == 2 and pair <= EARTH_MOON_SYSTEM:
            # Inside the Earth-Moon system every distance is the Moon's
            # orbit about Earth, or a fixed share of it.
            return {'state': 'published', 'err_km': _row_err_km(MOON_ROW_NAME),
                    'governs_kind': 'published', 'row': MOON_ROW_NAME,
                    'who': 'the Moon',
                    'orbit_words': "the Moon's orbit around Earth"}
        moon = obj_name if obj_name in (parent_planets or {}).get(center_name, ()) else center_name
        host = center_name if moon == obj_name else obj_name
        return {'state': 'none', 'err_km': None, 'reason': 'unstated',
                'gap': _gap(moon, 'unstated', "%s's orbit around %s" % (moon, host))}

    b = _side(obj_name, 'body', center_name, obj_data, objects, parent_planets)
    c = _side(center_name, 'centre', center_name, None, objects, parent_planets)
    if b['kind'] == 'none':
        # The body's own position has no figure. A centre whose own error is
        # no larger than the kilometer floor changes nothing that prints, so
        # the pair has none (a spacecraft seen from Earth). A centre with a
        # larger error is a lower bound on the pair, by the larger-of-two
        # ruling, and governs as a floor (a spacecraft seen from Neptune).
        if c['kind'] in ('published', 'computed', 'floor') and c['err_km'] > _floor_err_km():
            gap_sides = [s for s in (b, c) if s.get('gap')]
            return {'state': 'floor', 'err_km': c['err_km'], 'who': c['who'],
                    'row': c.get('row'),
                    'governs_kind': 'computed' if c['kind'] == 'computed' else 'published',
                    'speed_err_km_s': None, 'published_sides': [c],
                    'gap': '; '.join(s['gap'] for s in gap_sides),
                    'may_be_larger': _may_be_larger(gap_sides)}
        return {'state': 'none', 'err_km': None, 'reason': b.get('reason'),
                'gap': b['gap']}
    sides = [s for s in (b, c) if s['kind'] != 'reference']
    numeric = [s for s in sides if s['kind'] in ('published', 'computed', 'floor', 'sheet')]
    nones = [s for s in sides if s['kind'] == 'none']
    gov = max(numeric, key=lambda s: s['err_km'])
    small = [s for s in numeric if s['kind'] == 'computed']
    out = {'err_km': gov['err_km'], 'who': gov['who'], 'row': gov.get('row'),
           'arcsec': gov.get('arcsec'),
           'governs_kind': gov['kind'] if gov['kind'] in ('computed', 'sheet') else 'published',
           'speed_err_km_s': small[0].get('speed_err_km_s') if small else None,
           'published_sides': [s for s in numeric if s['kind'] != 'computed']}
    gap_sides = nones + [s for s in numeric if s['kind'] == 'floor']
    if gap_sides:
        out['state'] = 'floor'
        out['gap'] = '; '.join(s['gap'] for s in gap_sides)
        out['may_be_larger'] = _may_be_larger(gap_sides)
    else:
        out['state'] = gov['kind']
    return out


# ============================================================================
# THE LINES
# ============================================================================

def _fmt(value, err):
    """value to the Report test's place for err, never fewer than one
    figure, plain digits. err is always positive here: the floors see to
    it, so format_by_error never falls back to ten figures."""
    return format_by_error(value, err)


def _finite(x):
    if isinstance(x, bool):
        return False
    try:
        return math.isfinite(float(x))
    except (TypeError, ValueError):
        return False


def speed_error_km_s(acc, distance_km, speed_km_s):
    """
    The speed's error and what set it: ('sigma', 'relative' or 'floor').
    """
    state = acc['state']
    if state in ('none', 'center') or speed_km_s is None:
        return _speed_floor_err_km_s(), 'floor'
    dist_err = max(acc['err_km'], _floor_err_km())
    candidates = []
    if distance_km and distance_km > 0:
        if acc.get('governs_kind') == 'computed' and state == 'computed':
            for s in acc.get('published_sides', ()):
                e = max(s['err_km'], _floor_err_km())
                candidates.append((speed_km_s * e / distance_km, 'relative'))
        else:
            candidates.append((speed_km_s * dist_err / distance_km, 'relative'))
        if acc.get('speed_err_km_s') is None and state == 'computed':
            # A small body whose velocity columns came back empty: its speed
            # keeps the distance's relative precision instead.
            candidates.append((speed_km_s * dist_err / distance_km, 'relative'))
    if acc.get('speed_err_km_s') is not None:
        candidates.append((acc['speed_err_km_s'], 'sigma'))
    if state == 'floor':
        candidates.append((_speed_floor_err_km_s(), 'floor'))
    if not candidates:
        return _speed_floor_err_km_s(), 'floor'
    return max(candidates, key=lambda t: t[0])


def _distance_sentence(acc):
    state = acc['state']
    if state == 'center':
        return ['This body is the center of the plot.']
    if state == 'none':
        reason = acc.get('reason')
        if reason == 'not_fetched':
            return ["JPL's uncertainty for this position is not included here,",
                    'so distances are shown to the whole kilometer.']
        if reason == 'not_from_jpl':
            return ['No accuracy is stated for this position,',
                    'so distances are shown to the whole kilometer.']
        return ['JPL states no accuracy for this position,',
                'so distances are shown to the whole kilometer.']
    computed = acc.get('governs_kind') == 'computed'
    finer = acc['err_km'] < _floor_err_km()
    orbit = acc.get('orbit_words') or "%s's orbit" % acc['who']
    if acc.get('governs_kind') == 'sheet':
        # JPL states the Voyagers' uncertainty as an angle seen from Earth,
        # predicted for 2030, and none for the distance; the conversion at
        # the spacecraft's distance from Earth is ours, and the words say so.
        km = float('%.2g' % acc['err_km'])
        lines = ["These distances are rounded to JPL's predicted sky-position uncertainty",
                 'for %s in 2030, %s arcseconds seen from Earth: about %s km'
                 % (acc['who'], '%.*g' % (SHEET_FIGURES, acc['arcsec']),
                    '{:,}'.format(int(km))),
                 'at its distance. JPL states none for the distance itself,',
                 'so this conversion is ours.']
    elif finer:
        lines = ['These distances are shown to the whole kilometer;',
                 ("JPL's uncertainty for %s's position on this date is finer."
                  % acc['who'] if computed
                  else "JPL's published accuracy for %s is finer." % orbit)]
    elif computed:
        lines = ["These distances are rounded to JPL's uncertainty for %s's position"
                 % acc['who'], 'on this date, at three standard deviations.']
    else:
        lines = ["These distances are rounded to JPL's published accuracy for",
                 '%s.' % orbit]
    if state == 'floor':
        lines[-1] = lines[-1].rstrip('.') + ';'
        gaps = acc['gap'].split('; ')
        if acc.get('may_be_larger'):
            lines += [g + ',' for g in gaps]
            lines.append('so the true uncertainty may be larger.')
        else:
            lines += [g + ';' for g in gaps[:-1]] + [gaps[-1] + '.']
    return lines


def _speed_sentence(acc, speed_from):
    state = acc['state']
    if state == 'center':
        return []
    if state == 'none':
        reason = acc.get('reason')
        if reason == 'not_fetched':
            return ["JPL's uncertainty for this body's speed is not included here."]
        if reason == 'not_from_jpl':
            return ['No uncertainty is stated for this speed.']
        return ["JPL states no uncertainty for this body's speed."]
    if speed_from == 'sigma':
        return ["The speed is rounded to JPL's uncertainty in its velocity."]
    if speed_from == 'floor':
        return ['Part of this speed has no stated uncertainty,',
                'so it is shown to the meter per second.']
    return ['The speed is rounded to the same relative precision as the distance.']


def distance_speed_lines(acc, distance_au, speed_au_per_day, center_name,
                         center_radius_km):
    """
    The hover's distance and speed lines, in order, each without <br>.
    Every unit is placed by its own Report test of the same error.
    """
    lines = []
    is_center = acc['state'] == 'center'
    err_km = _floor_err_km() if acc['state'] in ('none', 'center') else max(
        acc['err_km'], _floor_err_km())
    if _finite(distance_au):
        distance_au = float(distance_au)
        dist_km = distance_au * KM_PER_AU
        err_au = err_km / KM_PER_AU
        lines.append('Distance from Center: %s AU' % _fmt(distance_au, err_au))
        lines.append('Distance: %s kilometers' % _fmt(dist_km, err_km))
        # One light-time line: light-minutes under an hour, light-hours
        # above (brief section 1).
        lh_per_km = 1.0 / SPEED_OF_LIGHT_KM_S / S_PER_HOUR
        if dist_km * lh_per_km < 1:
            lines.append('Distance: %s light-minutes' % _fmt(
                distance_au * LIGHT_MINUTES_PER_AU, err_au * LIGHT_MINUTES_PER_AU))
        else:
            lines.append('Distance: %s light-hours' % _fmt(
                dist_km * lh_per_km, err_km * lh_per_km))
        if (not is_center and center_radius_km
                and center_name not in NO_SOLID_SURFACE):
            surf = dist_km - center_radius_km
            s = _fmt(surf, err_km)
            if surf < 0:
                s += ' (below mean datum)'
            lines.append('Distance to Center Surface: %s kilometers' % s)
    else:
        dist_km = None
        lines.append('Distance from Center: N/A AU')
        lines.append('Distance: N/A kilometers')
        lines.append('Distance: N/A light-minutes')

    speed_from = None
    if _finite(speed_au_per_day):
        km_s = float(speed_au_per_day) * KM_PER_AU / S_PER_DAY
        v_err, speed_from = speed_error_km_s(acc, dist_km, km_s)
        lines.append('Velocity: %s AU/day' % _fmt(
            float(speed_au_per_day), v_err * S_PER_DAY / KM_PER_AU))
        lines.append('Velocity: %s km/hr (%s km/sec)' % (
            _fmt(km_s * S_PER_HOUR, v_err * S_PER_HOUR), _fmt(km_s, v_err)))
    else:
        lines.append('Velocity: N/A AU/day')
        lines.append('Velocity: N/A km/hr (N/A km/sec)')
    lines += _distance_sentence(acc)
    if speed_from is not None:
        lines += _speed_sentence(acc, speed_from)
    return lines


# ============================================================================
# FETCHING A SMALL BODY'S UNCERTAINTY WITH ITS POSITION (Horizons, 2xr)
# ============================================================================

# Horizons' column names for the 2xr table, read by name and never by
# position (read live 2026-10-12 for 2P/Encke and 90377 Sedna through the
# chat's web-fetch tool). With OUT_UNITS='AU-D' the position columns are
# in AU and the velocity columns in AU/day, uncertainties included.
STATE_COLUMNS = ('X', 'Y', 'Z', 'VX', 'VY', 'VZ')
SIGMA_COLUMNS = ('R_s', 'VR_s', 'VT_s', 'VN_s')


def _num(tok):
    tok = tok.strip()
    if not tok or tok.lower().strip('.') in ('n.a', 'na'):
        return None
    try:
        return float(tok)
    except ValueError:
        return None


def parse_vectors_2xr(text):
    """
    The rows of a Horizons vector table, as dicts keyed by column name.
    Raises ValueError, quoting Horizons, when there is no data block.
    """
    lines = text.split('\n')
    try:
        soe = next(i for i, ln in enumerate(lines) if '$$SOE' in ln)
        eoe = next(i for i, ln in enumerate(lines) if '$$EOE' in ln)
    except StopIteration:
        snippet = ' | '.join(ln.strip() for ln in lines if ln.strip())[:400]
        raise ValueError('Horizons returned no vector table: %s' % snippet)
    header = None
    for ln in reversed(lines[:soe]):
        if 'JDTDB' in ln and ',' in ln:
            header = ln
            break
    if header is None:
        raise ValueError('Horizons vector table has no column header')
    names = [h.strip() for h in header.split(',')]
    if names and 'JDTDB' in names[0] and 'Calendar' in names[0]:
        names = ['JDTDB', 'Calendar Date (TDB)'] + names[1:]
    rows = []
    for ln in lines[soe + 1:eoe]:
        if not ln.strip() or 'Cut-off' in ln:
            continue
        toks = ln.split(',')
        row = {}
        for name, tok in zip(names, toks):
            if name:
                row[name] = tok.strip() if name.startswith('Calendar') else _num(tok)
        rows.append(row)
    missing = [c for c in STATE_COLUMNS if c not in names]
    if missing:
        raise ValueError('Horizons vector table lacks columns %s' % ', '.join(missing))
    return rows


def uncertainty_record(row, body_id, location, jd):
    """The hover's error record from one 2xr row, keyed by body, centre and
    date. Fields carry the sigma level in their names."""
    # A sigma of zero, or one that is not a number, is no figure.
    r_s = _finite_positive(row.get('R_s'))
    v = [row.get(c) for c in ('VR_s', 'VT_s', 'VN_s')]
    v = [x if (x is not None and math.isfinite(x) and x >= 0) else None for x in v]
    rec = {
        'source': "JPL Horizons vector table 2xr, 1-sigma columns times %d" % SIGMA_MULTIPLE,
        'key': {'body': str(body_id), 'center': str(location), 'jd': jd},
        'range_1sigma_au': r_s,
        'velocity_1sigma_rtn_au_per_day': v,
        'range_3sigma_km': (SIGMA_MULTIPLE * r_s * KM_PER_AU) if r_s is not None else None,
        'speed_3sigma_km_s': None,
    }
    if all(x is not None for x in v) and any(x > 0 for x in v):
        combined = math.sqrt(sum(x * x for x in v))
        rec['speed_3sigma_km_s'] = (SIGMA_MULTIPLE * combined * KM_PER_AU
                                    / (S_PER_DAY))
    return rec


def fetch_small_body_state(object_id, id_type, location, jd, timeout=60):
    """
    One Horizons vector query for a small body at one date, asking for the
    2xr table: the position and velocity, and their 1-sigma uncertainties,
    in the same answer. astroquery 0.4.11 sets no VEC_TABLE and cannot
    parse the extra columns, so the request is the payload astroquery
    builds, with VEC_TABLE added, sent directly. No extra query.

    Returns (state, uncertainty_record): state has x, y, z (AU), vx, vy,
    vz (AU/day), range (AU) and range_rate (AU/day). Raises on failure.
    """
    import requests
    from astroquery.jplhorizons import Horizons, conf
    h = Horizons(id=object_id, id_type=id_type, location=location, epochs=[jd])
    payload = h.vectors(get_query_payload=True)
    payload['VEC_TABLE'] = "'2xr'"
    payload['OBJ_DATA'] = 'NO'
    resp = requests.get(conf.horizons_server, params=payload, timeout=timeout)
    resp.raise_for_status()
    rows = parse_vectors_2xr(resp.text)
    if not rows:
        raise ValueError('Horizons returned an empty vector table')
    row = rows[0]
    x, y, z = row['X'], row['Y'], row['Z']
    vx, vy, vz = row['VX'], row['VY'], row['VZ']
    if None in (x, y, z, vx, vy, vz):
        raise ValueError('Horizons vector table has an empty state column')
    rng = math.sqrt(x * x + y * y + z * z)
    state = {'x': x, 'y': y, 'z': z, 'vx': vx, 'vy': vy, 'vz': vz,
             'range': rng,
             'range_rate': (x * vx + y * vy + z * vz) / rng if rng else 0.0}
    return state, uncertainty_record(row, object_id, location, jd)
