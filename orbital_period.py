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
The cache's 'elements' are not changed by any of this.

Since build 2 the period also sets what is DRAWN (ruling 7). The period
record keeps the elements Horizons gave around the period's own centre,
and drawing_orbit() hands the drawing those elements, so the ellipse is
taken around the same centre as the period: Sedna's around the solar
system's barycentre, Mercury's and Encke's around the Sun. The markers'
dates are worked out from the period that belongs to the drawn elements,
by the same fallback order, and a date carries the period's error.

Key functions:
    build_period_record() - Horizons + SBDB queries -> the cache's period record
    resolve_display_period() - the fallback order, for one body and one view
    drawing_orbit() - the elements to draw, their centre, and their period
    period_for_computation() - the period a marker's date is worked out from
    osculating_centre_for_view() - the one home of the view-to-centre map
    period_hover_lines() - the hover's period lines, <br>-joined
    period_panel_text() - one short line for the orbital parameters window
    report_exponent() - the Report test's place for an error

Consumed by: osculating_cache_manager.fetch_osculating_elements (writes),
visualization_utils.format_detailed_hover_text, orbital_param_viz.py,
palomas_orrery.py, idealized_orbits.py and apsidal_markers.py (read).

Role: computation
Domain: orrery

Module updated: October 11, 2026 with Anthropic's Claude Opus 5.5 (L-431,
new module).
Module updated: October 12, 2026 with Anthropic's Claude Opus 5.5 (L-401,
build 1: the hover's sentence "JPL lists no orbit uncertainty for this
body", false of JPL for a planet, now says what is true: JPL's small-body
database has no entry for the body, or why it gave no uncertainty.
report_exponent and format_by_error are now also used by
position_accuracy.py.)
Module updated: October 12, 2026 with Anthropic's Claude Opus 5.5 (L-401,
Tony's look: a planet or a moon, which JPL's small-body database does not
hold, no longer mentions it; the clause stays for an asteroid or comet
whose lookup gave no uncertainty.)
Module updated: October 12, 2026 with Anthropic's Claude Opus 5.5 (L-431,
build 2: the period record keeps the chosen centre's elements, and
drawing_orbit() and period_for_computation() hand them, with their
period, to the drawing and the markers; VIEW_TO_OSCULATING_CENTRE is the
one home of the view-to-centre map, which palomas_orrery.py now reads;
_is_small_body counts a pinned record number as a small body whatever
its id_type, so C/2025_K1 is asked of the Small-Body Database.)
Module updated: October 13, 2026 with Anthropic's Claude Opus 5.5 (L-431,
after build 2's look: drawn_aphelion_distance(), how far a drawn ellipse
moved to another centre reaches from the plot's centre, so the frame is
sized from the orbit as drawn.)
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
# around another centre. The ONE home of this map (L-431, build 2): both
# of palomas_orrery.py's plot paths, the static plot and the animation,
# read it through osculating_centre_for_view(), and so does the hover.
# Until build 2 the animation kept its own copy, which lacked Orcus.
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


def osculating_centre_for_view(center_object_name):
    """The Horizons centre a view fetches its system's elements around,
    such as '@9' for the Pluto-Charon barycentre, or None for the default
    (the Sun, or the centre Horizons picks for a moon)."""
    return VIEW_TO_OSCULATING_CENTRE.get(center_object_name)


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
                'elements': _elements_from_row(el[0], date_str),
            }
        except Exception as ex:          # try the other side of the year
            last_error = ex
    raise last_error


# The element columns kept from the period query's first row, under the
# names the orbit cache uses (orbit_data_manager.query_horizons_elements
# reads the same columns). astroquery 0.4.11 asks for AU-D units.
ELEMENT_COLUMNS = (
    ('a', ('a',)), ('e', ('e',)), ('i', ('incl',)), ('omega', ('w',)),
    ('Omega', ('Omega',)), ('TP', ('Tp_jd',)), ('MA', ('M',)),
    ('TA', ('nu',)), ('q', ('q',)),
)


def _elements_from_row(row, date_str):
    """The osculating elements of one Horizons elements row, around the
    centre the query asked, at the plot date (L-431, build 2: the drawn
    ellipse is taken around the period's centre). None when a column is
    missing; the drawing then keeps the elements it already has."""
    out = {}
    names = getattr(row, 'colnames', ())
    for key, candidates in ELEMENT_COLUMNS:
        col = next((c for c in candidates if c in names), None)
        if col is None:
            if key == 'q':
                continue
            return None
        try:
            v = float(row[col])
        except (TypeError, ValueError):
            return None
        if not math.isfinite(v):
            return None
        out[key] = v
    out['epoch'] = '%s osc.' % date_str
    return out


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
    """An asteroid or comet, by its id_type, or by a pinned Horizons
    small-body record number (9 followed by seven digits), whatever its
    id_type: C/2025_K1 is listed as record 90004912 with id_type 'id'
    (L-431, build 2; found at L-401's review)."""
    if id_type in ('smallbody', 'designation', 'asteroid_name', 'comet_name'):
        return not str(horizons_id).startswith('-')
    return bool(re.match(r'^9\d{7}$', str(horizons_id).strip()))


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
        # L-431, build 2: the elements around the chosen centre at the plot
        # date, so the drawing can be taken around the period's centre;
        # and the period the elements fetch itself gave, around its own
        # centre, for the drawing that cannot be (drawing_orbit).
        'elements': pair.get('elements'),
        'elements_fetch_days': elements_p_days,
        'elements_fetch_center': location,
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


def _sbdb_words(status):
    """Why JPL's small-body database gave no period uncertainty, in true
    words, from the status build_period_record saved (L-401, build 1)."""
    status = status or ''
    if status.startswith('SBDB gives no sigma'):
        return "JPL's small-body database gives no uncertainty for this period."
    if status.startswith('SBDB not reached'):
        return "JPL's small-body database could not be reached when this was fetched."
    if status.startswith('SBDB gives no period'):
        return "JPL's small-body database gives no period for this body."
    if status.startswith('SBDB found several'):
        return "JPL's small-body database found more than one match for this body."
    return "JPL's small-body database has no entry for this body."


def _sbdb_asked(status):
    """True when the database was asked, which happens only for an
    asteroid or comet with a closed orbit (build_period_record). A record
    saved with no status is treated as not asked."""
    return bool(status) and not status.endswith('SBDB not asked')


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
    elif governs == 'year_change' and not _sbdb_asked(rec.get('sbdb_status')):
        # Tony's look at L-401 build 1 (2026-10-12): a planet or a moon is
        # not in JPL's small-body database, so the database is not
        # mentioned. Only the yearly change sets its digits.
        why = 'Rounded to how much the period changes in a year.'
    elif governs == 'year_change':
        # L-401 build 1: say what is true. An asteroid or comet whose
        # database lookup gave no uncertainty says why, in plain words.
        why = ('Rounded to how much the period changes in a year;<br>'
               + _sbdb_words(rec.get('sbdb_status')))
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


# ============================================================================
# COMPUTING WITH A PERIOD (L-431, build 2: the drawn ellipse and the markers)
# ============================================================================
#
# Ruling 7 (2026-10-11): the drawn ellipse is taken around the same centre
# as the period, and the perihelion and aphelion markers use the fetched
# period in the same fallback order. The period a marker's date is worked
# out from must belong to the elements that draw the orbit, or the date and
# the drawing describe two orbits; drawing_orbit() keeps the two together.

KIND_FETCHED = 'fetched'
KIND_TYPED = 'typed'
KIND_KEPLER = 'kepler'
KIND_NONE = 'none'

# The words a marker carries when its date did not come from JPL's period.
# "Typed value, not fetched from JPL" is the body hover's own (build 1,
# approved at its look); the Kepler sentence is new in build 2 and goes to
# Tony at its look.
TYPED_PERIOD_WORDS = 'From a typed period: typed value, not fetched from JPL.'
KEPLER_PERIOD_WORDS = ("From a period worked out from the orbit's size,<br>"
                       'not fetched from JPL.')


def _strip_osc(epoch):
    return str(epoch or '').replace(' osc.', '').strip()


def _same_centre(a, b):
    """Two Horizons centre strings name the same centre ('@sun' and '@10',
    '@599' and '599')."""
    if a is None or b is None:
        return False
    if _is_heliocentric(a) and _is_heliocentric(b):
        return True
    return str(a).lstrip('@').lower() == str(b).lstrip('@').lower()


def _period(days, err, kind, center=None, record=None, parent_name=None):
    return {'days': days, 'err_days': err, 'kind': kind, 'center': center,
            'label': centre_label(center, parent_name) if center else None,
            'record': record}


def _orbits_the_sun(obj_name, center_object_name):
    """Around the Sun: a Sun-centred view (or none named) and a body that
    is not a moon or a member of a binary system (orbital_elements'
    parent_planets lists those). Only then may Kepler's law with the Sun's
    mass stand in for a period."""
    if center_object_name not in (None, 'Sun'):
        return False
    try:
        from orbital_elements import parent_planets
    except Exception:
        return True
    return not any(obj_name in members for members in parent_planets.values())


def _typed_or_kepler(obj_name, typed_table, a_au, heliocentric):
    """The last two steps of the fallback order, for computing: the typed
    table, marked; then, for an orbit around the Sun only, Kepler's third
    law from the orbit's size, marked. A moon gets neither: Kepler's law
    with the Sun's mass would be wrong for it."""
    if typed_table is None:
        from constants_new import KNOWN_ORBITAL_PERIODS as typed_table
    days = typed_table.get(obj_name) if obj_name else None
    if days is not None and math.isfinite(float(days)) and float(days) < OPEN_ORBIT_PLACEHOLDER_FLOOR:
        return _period(float(days), None, KIND_TYPED)
    if heliocentric and a_au is not None and a_au > 0:
        return _period(D_PER_JULIAN_YEAR * math.sqrt(a_au ** 3), None, KIND_KEPLER, CENTRE_SUN)
    return _period(None, None, KIND_NONE)


def period_for_computation(obj_name, center_object_name=None, a_au=None,
                           typed_table=None, cache=None, parent_name=None):
    """
    The period to WORK OUT a marker's date from, by the fallback order:
    the fetched record in the orbit cache (a fresh fetch writes it, so the
    last fetched record is the same step), then the typed table, marked,
    then Kepler's third law from a, marked, for an orbit around the Sun.

    For a view whose elements and period share one centre: a moon, the
    Pluto system, or any body whose record names the centre its elements
    were fetched around. drawing_orbit() is the caller for a Sun-centred
    view, where the two can differ.

    Returns {'days', 'err_days', 'kind', 'center', 'label', 'record'};
    kind is 'fetched', 'typed', 'kepler' or 'none'.
    """
    resolved = resolve_display_period(obj_name, center_object_name, parent_name,
                                      typed_table={}, cache=cache)
    rec = resolved.get('record')
    if resolved['kind'] == 'fetched' and rec.get('days') is not None:
        return _period(rec['days'], rec.get('error_days'), KIND_FETCHED,
                       rec.get('center'), rec, parent_name)
    if resolved['kind'] == 'fetched':
        return _period(None, None, KIND_NONE, rec.get('center'), rec, parent_name)
    return _typed_or_kepler(obj_name, typed_table, a_au,
                            _orbits_the_sun(obj_name, center_object_name))


def _rotate(x, y, z, angle, axis):
    """The rotation idealized_orbits.rotate_points applies, for one point."""
    c, s = math.cos(angle), math.sin(angle)
    if axis == 'z':
        return x * c - y * s, x * s + y * c, z
    return x, y * c - z * s, y * s + z * c


def position_from_elements(el):
    """The body's position at its elements' epoch, from a, e, i, omega,
    Omega and the true anomaly TA, in the rotation order the orrery draws
    its ellipses in (omega about z, i about x, Omega about z). AU."""
    a, e, nu = el['a'], el['e'], math.radians(el['TA'])
    r = a * (1.0 - e * e) / (1.0 + e * math.cos(nu))
    x, y, z = r * math.cos(nu), r * math.sin(nu), 0.0
    x, y, z = _rotate(x, y, z, math.radians(el['omega']), 'z')
    x, y, z = _rotate(x, y, z, math.radians(el['i']), 'x')
    return _rotate(x, y, z, math.radians(el['Omega']), 'z')


def _elements_usable(el):
    """Every element position_from_elements needs is a finite number (the
    cache stores None for a column Horizons did not send)."""
    for k in ('a', 'e', 'i', 'omega', 'Omega', 'TA'):
        v = el.get(k)
        if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v):
            return False
    return el['e'] < 1.0


def period_for_elements(obj_name, params, cache=None, typed_table=None):
    """
    The period that belongs to the elements in hand, for a window that
    draws them as given (the orbital parameters window). The record is
    read under the plain key, the one a Sun-centred or a moon's own fetch
    writes; a view-keyed record (Earth@3, Pluto@9) is around another
    centre and never pairs with these elements. When the record's centre
    differs, the period the same elements fetch gave is used, then the
    typed table, marked.
    """
    return drawing_orbit(obj_name, None, params, cache=cache, typed_table=typed_table,
                         allow_move=False)['period']


def drawing_orbit(obj_name, center_object_name, params, cache=None,
                  typed_table=None, parent_name=None, allow_move=True):
    """
    The elements to DRAW a body's orbit with, the centre they are taken
    around, and the period that belongs to them (ruling 7).

    params are the elements the view fetched (planetary_params[obj_name]).
    When the body's period record names a different centre (Sedna's names
    the solar system's barycentre, while the plot asks around the Sun) and
    holds the elements Horizons gave around that centre at the same date,
    those are drawn, moved so their focus sits where that centre is: the
    body's position from both element sets at the one date gives where the
    barycentre is seen from the Sun, so the two ellipses meet at the body.

    Returns a dict:
        elements   a, e, i, omega, Omega, TP, MA, TA, epoch to draw from
        center     the Horizons centre they are around, or None if unknown
        label      the hover's words for that centre, or None
        offset_au  (dx, dy, dz): that centre seen from the plot's centre
        period     the period to compute with (as period_for_computation)
        note       None, or a sentence for the orbit's hover when the
                   period's centre could not be drawn

    allow_move=False keeps params as they are and returns the period that
    belongs to them (period_for_elements), for a window that draws the
    elements it was given.
    """
    out = {'elements': params, 'center': None, 'label': None,
           'offset_au': (0.0, 0.0, 0.0), 'note': None}
    a_au = (params or {}).get('a')
    if cache is None:
        cache = _load_cache_quietly()
    entry = _cache_entry_for(obj_name, center_object_name, cache) if obj_name else None
    entry = entry if isinstance(entry, dict) else {}
    rec = entry.get('period') if isinstance(entry.get('period'), dict) else None
    same_fetch = bool(entry.get('elements')) and params is not None and (
        _strip_osc(entry['elements'].get('epoch')) == _strip_osc(params.get('epoch')))
    params_centre = (entry.get('metadata') or {}).get('center_body', CENTRE_SUN) if same_fetch else None
    if params_centre:
        out['center'] = params_centre
        out['label'] = centre_label(params_centre, parent_name)

    if rec is None or 'days' not in rec:
        out['period'] = _typed_or_kepler(obj_name, typed_table, a_au,
                                         _orbits_the_sun(obj_name, center_object_name))
        return out
    if rec.get('days') is None:
        # An open orbit: nothing to time by a period.
        out['period'] = _period(None, None, KIND_NONE, rec.get('center'), rec, parent_name)
        return out
    fetched = _period(rec['days'], rec.get('error_days'), KIND_FETCHED,
                      rec.get('center'), rec, parent_name)
    sun_view = center_object_name in (None, 'Sun')
    if params_centre is None and sun_view and not _is_heliocentric(rec.get('center')):
        # Elements from somewhere other than this fetch, around the Sun,
        # and a period around another centre: they cannot be paired.
        out['period'] = _typed_or_kepler(obj_name, typed_table, a_au,
                                         _orbits_the_sun(obj_name, center_object_name))
        return out
    if params_centre is None or _same_centre(rec.get('center'), params_centre):
        # The record and the drawn elements share a centre (Mercury, Encke,
        # a moon), or the drawn elements are not this fetch's and the
        # record's centre is the view's.
        out['period'] = fetched
        return out
    el = rec.get('elements')
    if (allow_move and isinstance(el, dict)
            and _strip_osc(el.get('epoch')) == _strip_osc(params.get('epoch'))
            and _elements_usable(params) and _elements_usable(el)):
        hx, hy, hz = position_from_elements(params)
        bx, by, bz = position_from_elements(el)
        out.update({'elements': el, 'center': rec.get('center'),
                    'label': centre_label(rec.get('center'), parent_name),
                    'offset_au': (hx - bx, hy - by, hz - bz), 'period': fetched})
        return out
    # The record names another centre but holds no elements around it for
    # this date (a record saved before build 2): the drawing stays around
    # its own centre, and its markers use the period the elements fetch
    # gave around that centre, or the typed table, marked.
    out['note'] = ('Drawn around %s; the period above is around %s.<br>'
                   'Update the orbital elements to draw it around that center.'
                   % (out['label'], centre_label(rec.get('center'), parent_name)))
    own = rec.get('elements_fetch_days')
    if own is not None and _same_centre(rec.get('elements_fetch_center'), params_centre):
        out['period'] = _period(own, None, KIND_FETCHED, params_centre, None, parent_name)
    else:
        out['period'] = _typed_or_kepler(obj_name, typed_table, a_au,
                                         _orbits_the_sun(obj_name, center_object_name))
    return out


def drawn_aphelion_distance(obj_name, center_object_name, params, cache=None):
    """
    How far the drawn ellipse's aphelion is from the plot's centre, in AU,
    when drawing_orbit draws the body around another centre (Sedna, around
    the solar system's barycentre); None when the fetched elements are
    drawn as they are, so the caller keeps its own a(1+e).

    The plot's frame is sized from this (palomas_orrery.py,
    calculate_axis_range_from_orbits): sized from the Sun-centred a(1+e),
    Sedna's frame reached well past the end of its drawn ellipse (found
    at build 2's look, 2026-10-13; the figures are in the handoff).
    """
    o = drawing_orbit(obj_name, center_object_name, params, cache=cache)
    el = o['elements']
    if el is params or not _elements_usable(el):
        return None
    far = dict(el)
    far['TA'] = 180.0
    x, y, z = position_from_elements(far)
    dx, dy, dz = o['offset_au']
    return math.sqrt((x + dx) ** 2 + (y + dy) ** 2 + (z + dz) ** 2)


def carried_error_days(period, periods=1.0):
    """The error a date carries from the period it was worked out from:
    the period's error times the number of periods stepped (half of one
    for an aphelion after a perihelion). None when the period has none."""
    err = (period or {}).get('err_days')
    if err is None:
        return None
    return abs(periods) * err


def date_note_lines(period, carried_days):
    """The hover lines a computed date carries: where its period came from
    when that is not JPL's, and its uncertainty where that is more than a
    day (L-431 brief, section 2b). Each line without <br>."""
    lines = []
    kind = (period or {}).get('kind')
    if kind == KIND_TYPED:
        lines.append(TYPED_PERIOD_WORDS)
    elif kind == KIND_KEPLER:
        lines.extend(KEPLER_PERIOD_WORDS.split('<br>'))
    if carried_days is not None and carried_days > 1.0:
        v = float('%.2g' % carried_days)
        s = '{:,}'.format(int(round(v))) if v >= 10 else ('%g' % v)
        lines.append("Uncertain by about %s days, from the period's uncertainty." % s)
    return lines
