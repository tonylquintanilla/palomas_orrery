"""
orbital_period.py - A body's orbital period from JPL, printed to the digits its errors earn.

Fetches each body's sidereal orbital period (Horizons' PR) with its
osculating elements, picks the centre it is steadiest around (the Sun or
the solar system's barycentre, its centre of mass), measures how much it
moves in a year, reads JPL's stated uncertainty of the orbit fit (the
Small-Body Database's sigma) where the body has one, and prints the
period by the larger of those two errors. Ledger L-431, build 1 of 3;
rulings in documentation/DESIGN_L431_orbital_periods_rulings_20261011.md.

The fallback order for SHOWING a period (Tony's ruling 5):
    1. a fresh fetch, saved in the orbit cache (data/osculating_cache.json)
       under the entry's 'period' key, with its centre, date and error;
    2. the last fetched period saved there, which is the same record
       carried forward when a later fetch could not get one;
    3. the typed table KNOWN_ORBITAL_PERIODS (constants_new.py), printed
       as typed with the note "typed value, not fetched from JPL".
The cache's 'elements' are not changed by any of this, so the drawn
ellipse and the perihelion and aphelion markers do not move (build 2).

Key functions:
    build_period_record() - Horizons + SBDB queries -> the cache's period record
    resolve_display_period() - the fallback order, for one body and one view
    period_hover_lines() - the hover's period lines, <br>-joined
    period_panel_text() - one short line for the orbital parameters window
    report_exponent() - the Report test's place for an error

Consumed by: osculating_cache_manager.fetch_osculating_elements (writes),
visualization_utils.format_detailed_hover_text, orbital_param_viz.py and
palomas_orrery.py (read).

Role: computation
Domain: orrery

Module updated: October 11, 2026 with Anthropic's Claude Opus 5.5 (L-431,
new module).
"""

import math
import os
import re
from datetime import datetime

from constants_new import D_PER_JULIAN_YEAR

# Horizons prints PR as 9.999E+99 for an open orbit (read 2026-10-11 on
# C/2025 N1 through the chat's web-fetch tool). Anything this large is
# that placeholder, not a period.
OPEN_ORBIT_PLACEHOLDER_FLOOR = 1e90

# The two centres of the two-centre test (ruling 2), in Horizons' location
# form, as orbit_data_manager.query_horizons_elements passes them.
CENTRE_SUN = '@sun'
CENTRE_BARYCENTRE = '@0'
HELIOCENTRIC_FORMS = ('@sun', '@10', 'sun', '10')

SBDB_API_URL = 'https://ssd-api.jpl.nasa.gov/sbdb.api'

# The view centres that make palomas_orrery.py fetch an object's elements
# around another centre. A COPY of the block that sets
# osculating_center_body in palomas_orrery.py (search for
# "osculating_center_body = '@9'"). Build 2 edits that path and folds this
# copy into one home there (L-431). The pre-test checks the two agree.
VIEW_TO_OSCULATING_CENTRE = {
    'Pluto-Charon Barycenter': '@9',
    'Pluto': '@999',
    'Orcus-Vanth Barycenter': '@20090482',
    'Orcus': '@920090482',
    'Patroclus-Menoetius Barycenter': '@20000617',
    'Earth-Moon Barycenter': '@3',
    'Earth': '@399',
}

# What the hover calls each centre. Words, not values.
CENTRE_LABELS = {
    'sun': 'the Sun',
    '10': 'the Sun',
    '0': "the solar system's center of mass",
    'ssb': "the solar system's center of mass",
    '3': 'the Earth-Moon center of mass',
    '9': 'the Pluto-Charon center of mass',
    '20090482': 'the Orcus-Vanth center of mass',
    '20000617': 'the Patroclus-Menoetius center of mass',
    '20136199': 'the Eris-Dysnomia center of mass',
    '20136108': "the Haumea system's center of mass",
    '20136472': "the Makemake system's center of mass",
    '20225088': "the Gonggong system's center of mass",
    '920050000': 'Quaoar',
    '920090482': 'Orcus',
    '199': 'Mercury', '299': 'Venus', '399': 'Earth', '499': 'Mars',
    '599': 'Jupiter', '699': 'Saturn', '799': 'Uranus', '899': 'Neptune',
    '999': 'Pluto',
}


def centre_label(location, parent_name=None):
    """The hover's words for a Horizons centre such as '@sun' or '@599'."""
    key = str(location or '').lstrip('@').lower()
    if key in CENTRE_LABELS:
        return CENTRE_LABELS[key]
    if parent_name:
        return parent_name
    return 'Horizons center %s' % key


def _is_heliocentric(location):
    return str(location or '').lower() in HELIOCENTRIC_FORMS


# ============================================================================
# THE DIGITS RULE (ruling 3; provenance-discipline, The ceiling, Report)
# ============================================================================

def report_exponent(err):
    """
    The Report test's place for an error: the power of ten p whose implied
    half-width, half of 10**p, is closest to err on a log scale; a tie goes
    to the coarser place. Returns p (0 = whole units, -2 = hundredths).
    """
    x = math.log10(2.0 * err)
    return int(math.floor(x + 0.5))


def format_by_error(value, err):
    """
    value printed to the place its error earns, never fewer than one
    figure. Thousands separators from 10,000 up, as the rulings record's
    section 5 table prints them.
    """
    if value is None:
        return None
    if err is None or not (err > 0):
        # No error to round by: keep ten figures and let the caller say so.
        err = abs(value) * 1e-10 if value else 1e-10
    p = report_exponent(err)
    if value != 0:
        top = int(math.floor(math.log10(abs(value))))
        if p > top:
            p = top                  # never fewer than one figure
    if p >= 0:
        unit = 10 ** p
        r = int(round(value / unit)) * unit
        return ('{:,}'.format(r) if abs(r) >= 10000 else str(r))
    places = -p
    s = '%.*f' % (places, value)
    if abs(value) >= 10000:
        whole, _, frac = s.partition('.')
        s = '{:,}'.format(int(whole)) + ('.' + frac if frac else '')
    return s


# ============================================================================
# FETCHING (Horizons and the Small-Body Database)
# ============================================================================

def query_period_pair(horizons_id, id_type, date_str, location):
    """
    One Horizons elements query, two epochs: the plot date and a Julian
    year later (a year earlier if the later date is refused). Returns
    {'p1', 'p2', 'step_days', 'e', 'targetname'}; a period is None for an
    open orbit (PR printed as the 9.999E+99 placeholder).
    astroquery's elements() asks for OUT_UNITS AU-D and names PR 'P', in
    days (astroquery 0.4.11, jplhorizons/__init__.py, elem_columns).
    """
    from astroquery.jplhorizons import Horizons
    from astropy.time import Time

    jd = Time(date_str).jd
    last_error = None
    for step in (D_PER_JULIAN_YEAR, -D_PER_JULIAN_YEAR):
        try:
            obj = Horizons(id=horizons_id, id_type=id_type, location=location,
                           epochs=[jd, jd + step])
            el = obj.elements()
            if len(el) < 2:
                raise ValueError('Horizons returned %d rows, not 2' % len(el))
            if 'P' not in el.colnames:
                raise KeyError('no period column P in %s' % (el.colnames,))

            def _p(row):
                v = float(row['P'])
                return None if (not math.isfinite(v) or abs(v) >= OPEN_ORBIT_PLACEHOLDER_FLOOR) else v

            e_val = float(el[0]['e']) if 'e' in el.colnames else None
            p1, p2 = _p(el[0]), _p(el[1])
            if e_val is not None and e_val >= 1.0:
                p1 = p2 = None
            return {
                'p1': p1, 'p2': p2, 'step_days': step, 'e': e_val,
                'targetname': str(el[0]['targetname']) if 'targetname' in el.colnames else None,
            }
        except Exception as ex:          # try the other side of the year
            last_error = ex
    raise last_error


def sbdb_search_string(horizons_id, targetname=None):
    """
    What to ask the Small-Body Database for. A pinned Horizons record
    number (9 followed by seven digits) is not something SBDB can find
    (horizons-orbital-mechanics 1.2, Checking an Entry Against JPL), so
    for one the name Horizons gave the record is used: '2P/Encke' -> '2P'.
    """
    hid = str(horizons_id).strip()
    if re.match(r'^9\d{7}$', hid) and targetname:
        name = targetname.strip()
        m = re.match(r'^(\d+[PI])/', name)
        if m:
            return m.group(1)
        m = re.search(r'\(([^()]+)\)\s*$', name)
        return m.group(1).strip() if m else name
    return hid


def fetch_sbdb_period_sigma(search):
    """
    JPL's stated 1-sigma of the sidereal orbital period, in days, from the
    Small-Body Database API (orbit.elements, name 'per'). Returns
    (sigma_days or None, status words, SBDB's full name or None).
    """
    import requests
    try:
        resp = requests.get(SBDB_API_URL, params={'sstr': search, 'full-prec': '1'},
                            timeout=30)
        data = resp.json()
    except Exception as ex:
        return None, 'SBDB not reached (%s)' % ex.__class__.__name__, None
    if 'list' in data:
        return None, 'SBDB found several matches for %r' % search, None
    if 'orbit' not in data:
        return None, 'SBDB has no entry for %r' % search, None
    fullname = (data.get('object') or {}).get('fullname')
    for el in data['orbit'].get('elements', []):
        if el.get('name') == 'per':
            try:
                return float(el.get('sigma')), 'SBDB sigma', fullname
            except (TypeError, ValueError):
                return None, 'SBDB gives no sigma for the period', fullname
    return None, 'SBDB gives no period (open orbit?)', fullname


def _is_small_body(horizons_id, id_type):
    if id_type in ('smallbody', 'designation', 'asteroid_name', 'comet_name'):
        return not str(horizons_id).startswith('-')
    return False


def build_period_record(horizons_id, id_type, date_str, location, previous=None,
                        elements_p_days=None):
    """
    The period record the orbit cache keeps beside an entry's elements.

    location is the centre the elements were fetched around. When it is the
    Sun -- the default for planets, asteroids and comets -- the two-centre
    test runs (ruling 2): the period around the Sun and around the solar
    system's barycentre, each at the plot date and a year later, and the
    centre whose period moved less is kept. Its choice is saved, so a later
    fetch asks only for the chosen centre. A later fetch whose chosen centre
    moved more than the other centre did when the choice was made runs the
    test again. Moons and the Pluto system keep the centre the orrery gives
    them (method 3) and are measured there alone.

    elements_p_days is the PR the elements fetch itself returned, around
    location at the same date. Where the chosen centre is that location,
    the two must agree, and the record says whether they did.

    Raises on a failed query; the caller keeps the previous record.
    """
    test = None
    chosen = location
    if _is_heliocentric(location):
        prev_test = (previous or {}).get('test') or {}
        prev_choice = (previous or {}).get('center')
        if prev_choice in (CENTRE_SUN, CENTRE_BARYCENTRE) and prev_test:
            chosen = prev_choice
        else:
            chosen = None
    if chosen is not None:
        pair = query_period_pair(horizons_id, id_type, date_str, chosen)
        if _is_heliocentric(location):
            other = CENTRE_BARYCENTRE if chosen == CENTRE_SUN else CENTRE_SUN
            other_change = prev_test.get(other)
            change = _change(pair)
            if change is not None and other_change is not None and change > other_change:
                print('  [L-431 period] %s: around %s it moved %.6g d this year, more than '
                      '%s did when chosen (%.6g d); running the two-centre test again'
                      % (horizons_id, chosen, change, other, other_change), flush=True)
                chosen = None
            else:
                test = prev_test
    if chosen is None:
        sun = query_period_pair(horizons_id, id_type, date_str, CENTRE_SUN)
        bary = query_period_pair(horizons_id, id_type, date_str, CENTRE_BARYCENTRE)
        c_sun, c_bary = _change(sun), _change(bary)
        test = {CENTRE_SUN: c_sun, CENTRE_BARYCENTRE: c_bary,
                'run': datetime.now().strftime('%Y-%m-%d')}
        if c_bary is not None and (c_sun is None or c_bary < c_sun):
            chosen, pair = CENTRE_BARYCENTRE, bary
        else:
            chosen, pair = CENTRE_SUN, sun
        print('  [L-431 period] %s: year change around the Sun %s d, around the '
              'barycentre %s d -> %s'
              % (horizons_id, _fmt(c_sun), _fmt(c_bary), chosen), flush=True)

    days = pair['p1']
    change = _change(pair)
    agrees = None
    if elements_p_days is not None and days is not None and (
            chosen == location or (_is_heliocentric(chosen) and _is_heliocentric(location))):
        agrees = abs(elements_p_days - days) <= 1e-9 * abs(days)
        print('  [L-431 period] %s: the elements fetch gave PR %.10g d, the period '
              'query %.10g d -- %s' % (horizons_id, elements_p_days, days,
                                       'agree' if agrees else 'DISAGREE'), flush=True)
    sigma, sigma_status, sbdb_name = None, 'not a small body; SBDB not asked', None
    if days is None:
        sigma_status = 'open orbit; SBDB not asked'
    elif _is_small_body(horizons_id, id_type):
        search = sbdb_search_string(horizons_id, pair.get('targetname'))
        sigma, sigma_status, sbdb_name = fetch_sbdb_period_sigma(search)
    errors = [x for x in (change, sigma) if x is not None]
    err = max(errors) if errors else None
    if err is None:
        governs = None
    elif sigma is not None and sigma >= (change or 0.0):
        governs = 'sigma'
    else:
        governs = 'year_change'

    return {
        'days': days,
        'open_orbit': days is None,
        'center': chosen,
        'epoch': date_str,
        'fetched': datetime.now().strftime('%Y-%m-%d'),
        'source': 'JPL Horizons PR (sidereal orbit period)',
        'year_change_days': change,
        'year_step_days': pair['step_days'],
        'sbdb_sigma_days': sigma,
        'sbdb_status': sigma_status,
        'sbdb_fullname': sbdb_name,
        'error_days': err,
        'error_from': governs,
        'test': test,
        'horizons_targetname': pair.get('targetname'),
        'agrees_with_elements_fetch': agrees,
    }


def _change(pair):
    if pair is None or pair['p1'] is None or pair['p2'] is None:
        return None
    return abs(pair['p2'] - pair['p1'])


def _fmt(x):
    return 'n/a' if x is None else '%.6g' % x


# ============================================================================
# READING (the fallback order, for showing)
# ============================================================================

class _CacheMemo:
    """The orbit cache as last read, and the file time it was read at."""
    mtime = None
    data = None


def _load_cache_quietly():
    """The orbit cache, re-read only when the file changes."""
    try:
        from osculating_cache_manager import CACHE_FILE
        mtime = os.path.getmtime(CACHE_FILE)
        if _CacheMemo.mtime != mtime:
            import json
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                _CacheMemo.data = json.load(f)
            _CacheMemo.mtime = mtime
        return _CacheMemo.data or {}
    except Exception:
        return {}


def _cache_entry_for(obj_name, center_object_name, cache, view_only=False):
    """
    The cache entry the hover's view would have fetched: the one keyed to
    the view's centre (e.g. 'Pluto@9') where it exists, else the plain one.
    view_only skips the plain one, for a caller whose typed value belongs
    to the view and must not be replaced by a period around another centre.
    """
    osc = VIEW_TO_OSCULATING_CENTRE.get(center_object_name)
    if osc:
        key = '%s@%s' % (obj_name, osc.lstrip('@'))
        if key in cache:
            return cache[key]
    if view_only:
        return None
    return cache.get(obj_name)


def resolve_display_period(obj_name, center_object_name=None, parent_name=None,
                           typed_table=None, typed_override=None, cache=None):
    """
    The period to SHOW for one body in one view, by the fallback order.

    Returns a dict:
        kind     'fetched' | 'typed' | 'none'
        days     float, or None for an open orbit or nothing known
        record   the cache's period record (fetched only)
        label    the centre's words (fetched only)
    typed_override is a value the caller types for its own view (Pluto
    around the Pluto-Charon barycentre); it is printed as typed, with the
    note, when nothing was fetched.
    """
    if cache is None:
        cache = _load_cache_quietly()
    entry = (_cache_entry_for(obj_name, center_object_name, cache,
                              view_only=typed_override is not None)
             if obj_name else None)
    rec = (entry or {}).get('period') if isinstance(entry, dict) else None
    if isinstance(rec, dict) and ('days' in rec):
        return {'kind': 'fetched', 'days': rec.get('days'), 'record': rec,
                'label': centre_label(rec.get('center'), parent_name)}
    if typed_override is not None:
        return {'kind': 'typed', 'days': typed_override, 'record': None, 'label': None}
    if typed_table is not None and obj_name in typed_table:
        return {'kind': 'typed', 'days': typed_table[obj_name], 'record': None, 'label': None}
    return {'kind': 'none', 'days': None, 'record': None, 'label': None}


def _typed_strings(days):
    """A typed value as typed, and its years to the same figure count."""
    days_s = repr(float(days)) if not float(days).is_integer() else '%d' % days
    digits = len(re.sub(r'[^0-9]', '', days_s).lstrip('0')) or 1
    years = days / D_PER_JULIAN_YEAR
    years_s = '%.*g' % (digits, years)
    if 'e' in years_s:
        years_s = '%.*f' % (max(digits - 1 - int(math.floor(math.log10(abs(years)))), 0), years)
    return years_s, days_s


def period_hover_lines(resolved):
    """
    The hover's period lines, each ending in <br> except the last, every
    line under 98 characters (orrery-coding-conventions, Hover Line Width).
    The words are proposed by build 1 and Tony approves them at its look.
    """
    kind = resolved['kind']
    if kind == 'none':
        return 'Orbital period: N/A'
    if kind == 'typed':
        if resolved['days'] is None:
            return ('Orbital period: none (open orbit)<br>'
                    'Typed value, not fetched from JPL.')
        years_s, days_s = _typed_strings(resolved['days'])
        return ('Orbital period: %s years (%s days)<br>'
                'Typed value, not fetched from JPL.' % (years_s, days_s))
    rec = resolved['record']
    where = 'Around %s, from JPL Horizons, fetched %s.' % (resolved['label'], rec.get('fetched'))
    if rec.get('days') is None:
        return 'Orbital period: none (open orbit)<br>' + where
    err = rec.get('error_days')
    days_s = format_by_error(rec['days'], err)
    years_s = format_by_error(rec['days'] / D_PER_JULIAN_YEAR,
                              err / D_PER_JULIAN_YEAR if err else None)
    governs = rec.get('error_from')
    if governs == 'sigma':
        why = "Rounded to JPL's stated uncertainty in the orbit."
    elif governs == 'year_change' and rec.get('sbdb_sigma_days') is not None:
        why = 'Rounded to how much the period changes in a year.'
    elif governs == 'year_change':
        why = ('Rounded to how much the period changes in a year;<br>'
               'JPL lists no orbit uncertainty for this body.')
    else:
        why = 'No error was measured, so the digits are not rounded to one.'
    return ('Orbital period: %s years (%s days)<br>%s<br>%s'
            % (years_s, days_s, where, why))


def period_panel_text(resolved):
    """One short line for the orbital parameters window."""
    kind = resolved['kind']
    if kind == 'none':
        return '---'
    if resolved['days'] is None:
        return 'none (open orbit)' + (' - typed, not from JPL' if kind == 'typed' else '')
    if kind == 'typed':
        years_s, days_s = _typed_strings(resolved['days'])
        return '%s days (%s yr) - typed, not from JPL' % (days_s, years_s)
    rec = resolved['record']
    err = rec.get('error_days')
    days_s = format_by_error(rec['days'], err)
    years_s = format_by_error(rec['days'] / D_PER_JULIAN_YEAR,
                              err / D_PER_JULIAN_YEAR if err else None)
    return '%s days (%s yr), JPL, around %s' % (days_s, years_s, resolved['label'])
