"""
test_orbit_markers.py - each orbit is drawn around its period's centre,
each marker's date comes from the period JPL gave, and every orbit and
marker hover prints by the errors JPL states; and proof that this check
can fail.

L-431's second build (the drawn ellipse and the markers) carried L-401's
second slice (their hovers' digits). This file runs the real drawing,
idealized_orbits.plot_idealized_orbits, the function the static plot and
the animation both call, offline, for Mercury, Encke and Sedna seen from
the Sun, on recorded inputs, and judges what it drew with arithmetic of
its own: its own rotation of the elements, its own offset of the
barycentre, its own Report test, its own Julian-date arithmetic. It
shares no code with orbital_period.py or position_accuracy.py, so a
fault there shows here. It also runs the Moon's orbit, a moon's markers
(Io's, seen from Jupiter), and reads the dispatch in palomas_orrery.py.

It first plants a fault for each thing it must catch, each put into a
copy of the real source at the line it would live in, and requires the
right finding, by name:

    planted                                          must be caught as
    a marker dated from the typed period             MARKER DATED FROM THE TYPED PERIOD
      while a fetched record exists
    an ellipse drawn around the Sun while the        ELLIPSE NOT AROUND THE PERIOD'S CENTRE
      record names the barycentre
    an orbit hover printing a distance to ten        DISTANCE FINER THAN ITS ERROR
      decimals
    the Moon's typed period used when a fetched      MOON'S TYPED PERIOD USED
      period exists
    a moon's marker dated from the typed period      MARKER DATED FROM THE TYPED PERIOD
    the view-to-centre block copied back into        DISPATCH
      palomas_orrery.py
    the Keplerian position's period left to          KEPLERIAN POSITION FROM ANOTHER PERIOD
      Kepler's law
    an apsis marker printed by today's error,        DISTANCE FINER THAN ITS ERROR
      not its own date's
    the parameters window dated from a barycentre    PARAMETERS WINDOW PERIOD FROM ANOTHER CENTRE
      view's period
    the perihelion osculating orbit's hover without  DISTANCES WITHOUT THEIR ACCURACY SENTENCE
      its accuracy sentence
    Sedna's perturbation block not naming the        PERTURBATION COMPARED WITHOUT ITS CENTRE
      centre it compared around
    the plot's frame sized from the Sun-centred      FRAME SIZED FROM ANOTHER ORBIT
      orbit while Sedna is drawn around the
      barycentre

The first four are the brief's (documentation/
HANDOFF_L431_build2_orbits_markers_brief_20261012.md, section 4); the
next two cover the moons' marker path and the map's one home; the last
three come from a cold review of the build (2026-10-12), which showed the
first draft of this file could not fail on them; the three after them
come from Tony's look at build 2 (2026-10-13), where the saved plot showed
each one. It also runs a record
saved before build 2 (Sedna stays around the Sun and says why) and the
Keplerian position half a year after its epoch, where the period shows.

The inputs are recorded, not fetched. Mercury's, Encke's, Sedna's and
Io's elements and period records are JPL's answers as saved in
data/osculating_cache.json on 2026-10-12 (at orrery c9722520). Sedna's
elements around the solar system's barycentre are a SANDBOX FIXTURE, not
JPL's: worked out on 2026-10-12 from its cached Sun-centred elements and
the Sun's barycentric state in astropy's built-in ephemeris, offline.
Their a, 506.45 au, agrees with the rulings record's "about 506 au", and
their period, 4,160,226 days, with JPL's 4,160,096; the live run on
Tony's machine draws from JPL's own. The Moon's 27.0-day record is a
fixture too, chosen to differ from the typed table.

The last line starts "ORBIT MARKERS:", which the maintenance run quotes,
and says what was compared and how many things were examined.

Run (VS Code Run button, or):
    python test_orbit_markers.py

Never contacts Horizons.

Role: devtool
Domain: dev_tools

Module created: October 12, 2026 with Anthropic's Claude Opus 5.5 (L-431,
build 2, with L-401's second slice).
Module updated: October 13, 2026 with Anthropic's Claude Opus 5.5 (L-431,
after build 2's look: three judges and three planted faults for what the
saved plot showed -- the perihelion osculating orbit's accuracy sentence,
Sedna's perturbation block naming its centre, and the frame sized from
the drawn orbit. A whole number's trailing zeros are no longer called
coarse, since its place cannot be read from the print.)
"""
import contextlib
import copy
import io
import math
import os
import re
import sys
import types
import warnings
from datetime import datetime, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

warnings.filterwarnings('ignore')   # ERFA's "dubious year" for far dates

import plotly.graph_objects as go

import constants_new as cn
import orbital_period
import osculating_cache_manager
from celestial_objects import OBJECT_DEFINITIONS
from orbital_elements import parent_planets
from orbital_elements import planetary_params as MEAN_ELEMENTS

# ============================================================================
# THE RECORDED INPUTS (see the docstring for where each comes from)
# ============================================================================

PLOT_DATE = datetime(2026, 10, 12)
EPOCH = '2026-10-12 00:01 osc.'

MERCURY = {'a': 0.3870973829982185, 'e': 0.2056387447714802, 'i': 7.003372107877269,
           'omega': 29.20131193894946, 'Omega': 48.29727562895222, 'epoch': EPOCH,
           'TP': 2461354.853725812, 'MA': 239.8768490224104, 'TA': 222.1149278972467}
ENCKE = {'a': 2.217733604200496, 'e': 0.8473190141121133, 'i': 11.34776503248648,
         'omega': 187.2878283735506, 'Omega': 334.0190533905403, 'epoch': EPOCH,
         'TP': 2461446.72851751, 'MA': 323.822186585531, 'TA': 215.1239258277475}
SEDNA = {'a': 539.9028380449447, 'e': 0.8589239330257514, 'i': 11.92504808967517,
         'omega': 311.1460209612461, 'Omega': 144.515501575658, 'epoch': EPOCH,
         'TP': 2479295.630885726, 'MA': 358.5881717038998, 'TA': 325.6820662877274}
# The sandbox fixture: Sedna around the solar system's barycentre, same date.
SEDNA_BARY = {'a': 506.4534387518173, 'e': 0.8495586985395576, 'i': 11.928524341481102,
              'omega': 311.2846996213294, 'Omega': 144.4015765433012, 'epoch': EPOCH,
              'TP': 2479347.7582696793, 'MA': 358.4404663054393, 'TA': 325.65386551141864,
              'q': 76.19151445493986}
IO = {'a': 0.002821167458629801, 'e': 0.004720541664878496, 'i': 2.227967621835635,
      'omega': 30.85957784755919, 'Omega': 338.4034057952332,
      'epoch': '2026-10-12 20:44 osc.', 'TP': 2461326.51905351,
      'MA': 328.4664327440004, 'TA': 328.1820966498049}
EARTH = {'a': 0.9991609075089946, 'e': 0.01725633817381888, 'i': 0.004535327342978969,
         'omega': 267.8647017501623, 'Omega': 193.2423453182036,
         'epoch': '2023-05-07 00:39 osc.', 'TP': 2459946.723188862,
         'MA': 123.1628451926368, 'TA': 124.7986552457518}
MOON = {'a': 0.002558396788810978, 'e': 0.03209237574578062, 'i': 5.155171595436955,
        'omega': 121.4654664966015, 'Omega': 328.7159764475099,
        'epoch': '2026-10-06 12:51 osc.', 'TP': 2461316.380380294,
        'MA': 48.54132410988097, 'TA': 51.37133411535093}


def _rec(days, err, centre, epoch, sbdb=None, elements=None):
    r = {'days': days, 'open_orbit': False, 'center': centre, 'epoch': epoch,
         'fetched': '2026-10-12', 'error_days': err,
         'error_from': 'sigma' if sbdb else 'year_change',
         'sbdb_sigma_days': sbdb,
         'sbdb_status': 'SBDB sigma' if sbdb else 'not a small body; SBDB not asked'}
    if elements is not None:
        r['elements'] = elements
    return r


def fixture_cache():
    """The orbit cache the drawing reads, as data/osculating_cache.json held
    it on 2026-10-12, with Sedna's barycentre elements and the Moon's
    record added as fixtures."""
    def entry(el, centre, period):
        return {'elements': dict(el), 'metadata': {'center_body': centre}, 'period': period}
    return {
        'Mercury': entry(MERCURY, '@sun', _rec(87.96881539014642, 0.0003637054403924367,
                                                '@sun', '2026-10-12 00:01')),
        'Encke': entry(ENCKE, '@sun', _rec(1206.31990119054, 0.14979585173000487,
                                            '@sun', '2026-10-12 00:01', sbdb=0.0006574)),
        'Sedna': entry(SEDNA, '@sun', _rec(4160095.730593757, 1864.0, '@0',
                                            '2026-10-12 00:01', sbdb=1864.0,
                                            elements=dict(SEDNA_BARY))),
        'Io': entry(IO, '@599', _rec(1.771422283426844, 3.3145577758020295e-05,
                                      '@599', '2026-10-12 20:44')),
        'Moon@399': entry(MOON, '@399', _rec(27.0, 0.001, '@399', '2026-10-06 12:51')),
        # Earth around the Sun, and a period around the Earth-Moon
        # barycentre as a plot from that view saves it (fixture figures)
        'Earth': entry(EARTH, '@sun', _rec(365.2600, 0.0001, '@sun', '2023-05-07 00:39')),
        'Earth@3': entry({'a': 0.0000312, 'epoch': '2026-10-12 00:01 osc.'}, '@3',
                         _rec(27.3217, 0.001, '@3', '2026-10-12 00:01')),
        'Charon@9': {'elements': {'a': 0.000130, 'epoch': 'fixture'}, 'metadata': {}},
        'Charon': {'elements': {'a': 39.0, 'epoch': 'fixture'}, 'metadata': {}},
    }


# The bodies' own uncertainties, as the static plot carries them in each
# position record. Sedna's: three times R_s, 85,939.995 km, read 2026-10-12
# (the L-401 rulings record, section 4). Encke's: three times R_s from the
# 2xr answer test_position_digits.py records (2.25639403e-06 au).
SEDNA_SIGMA_KM = 3 * 85939.995
ENCKE_SIGMA_KM = 3 * 2.25639403e-06 * cn.KM_PER_AU
# Mercury's: half a unit of JPL's published place for the terrestrial
# planets (the DE430 row, read by name).
MERCURY_ERR_KM = 0.5 * cn.DE430_TERRESTRIAL_POSITION_PLACE_KM
FLOOR_KM = 0.5   # whole kilometers; half of one is the error

# A position JPL gives for an apsis date carries its own uncertainty for
# that date; these fixture figures differ from today's on purpose, so a
# marker printed by today's error shows (L-401: keyed by body, centre and
# date).
APSIS_SIGMA_KM = {'Sedna': 600000.0, 'Encke': 3000.0}
KPOS_DATE = datetime(2027, 4, 12)    # half a year after the elements' epoch

BODY_ERR_KM = {'Mercury': MERCURY_ERR_KM, 'Encke': ENCKE_SIGMA_KM, 'Sedna': SEDNA_SIGMA_KM,
               'Io': FLOOR_KM}
TYPED = cn.KNOWN_ORBITAL_PERIODS


def position_record(name):
    d = {'x': 1.0, 'y': 0.0, 'z': 0.0}
    if name == 'Sedna':
        d['position_uncertainty'] = {'range_3sigma_km': SEDNA_SIGMA_KM, 'speed_3sigma_km_s': 2.5e-4}
    if name == 'Encke':
        d['position_uncertainty'] = {'range_3sigma_km': ENCKE_SIGMA_KM, 'speed_3sigma_km_s': 1.3e-5}
    return d


# ============================================================================
# THE CHECKER'S OWN ARITHMETIC
# ============================================================================

def place_for(err):
    """The Report test, written out: the power of ten whose half-unit is
    nearest err on a log scale, a tie going to the coarser."""
    best = None
    for p in range(-20, 21):
        d = abs(math.log10(0.5 * 10.0 ** p) - math.log10(err))
        if best is None or d < best[0] - 1e-12 or (abs(d - best[0]) <= 1e-12 and p > best[1]):
            best = (d, p)
    return best[1]


def printed_place(s):
    s = s.replace(',', '').lstrip('+-')
    if '.' in s:
        return -len(s.split('.')[1])
    return len(s) - len(s.rstrip('0')) if s.strip('0') else 0


def expected_place(value, err):
    p = place_for(err)
    if value:
        p = min(p, int(math.floor(math.log10(abs(value)))))
    return p


def rot(el):
    """The orbit's rotation, omega about z, i about x, Omega about z, as a
    3x3 list of rows."""
    def rz(t):
        c, s = math.cos(t), math.sin(t)
        return [[c, -s, 0], [s, c, 0], [0, 0, 1]]

    def rx(t):
        c, s = math.cos(t), math.sin(t)
        return [[1, 0, 0], [0, c, -s], [0, s, c]]

    def mul(a, b):
        return [[sum(a[r][k] * b[k][col] for k in range(3)) for col in range(3)] for r in range(3)]
    return mul(mul(rz(math.radians(el['Omega'])), rx(math.radians(el['i']))),
               rz(math.radians(el['omega'])))


def apply(m, v):
    return [sum(m[r][k] * v[k] for k in range(3)) for r in range(3)]


def at_anomaly(el, nu_deg):
    nu = math.radians(nu_deg)
    r = el['a'] * (1 - el['e'] ** 2) / (1 + el['e'] * math.cos(nu))
    return apply(rot(el), [r * math.cos(nu), r * math.sin(nu), 0.0])


def off_ellipse(el, offset, pt):
    """How far a point lies off the ellipse el moved by offset, relative to
    its distance: the point taken back into the orbit's plane, its radius
    compared with the conic's at its own angle."""
    m = rot(el)
    v = [pt[k] - offset[k] for k in range(3)]
    back = [sum(m[k][r] * v[k] for k in range(3)) for r in range(3)]   # transpose
    r = math.sqrt(sum(x * x for x in back))
    if r == 0:
        return 1.0
    th = math.atan2(back[1], back[0])
    want = el['a'] * (1 - el['e'] ** 2) / (1 + el['e'] * math.cos(th))
    return abs(r - want) / r + abs(back[2]) / r


def jd_to_dt(jd):
    return datetime(2000, 1, 1, 12) + timedelta(days=jd - 2451545.0)


# The barycentre's place seen from the Sun: Sedna's position from both
# element sets at the one date (the checker's own sum).
SEDNA_OFFSET = [h - b for h, b in zip(at_anomaly(SEDNA, SEDNA['TA']),
                                      at_anomaly(SEDNA_BARY, SEDNA_BARY['TA']))]
DRAWN = {'Mercury': (MERCURY, [0.0, 0.0, 0.0]), 'Encke': (ENCKE, [0.0, 0.0, 0.0]),
         'Sedna': (SEDNA_BARY, SEDNA_OFFSET)}
FETCHED_DAYS = {'Mercury': 87.96881539014642, 'Encke': 1206.31990119054,
                'Sedna': 4160095.730593757}
FETCHED_ERR = {'Mercury': 0.0003637054403924367, 'Encke': 0.14979585173000487,
               'Sedna': 1864.0}


# ============================================================================
# RUNNING THE REAL CODE
# ============================================================================

@contextlib.contextmanager
def cache_is(cache):
    old_op = orbital_period._load_cache_quietly
    old_oc = osculating_cache_manager.load_cache
    orbital_period._load_cache_quietly = lambda: cache
    osculating_cache_manager.load_cache = lambda: cache
    try:
        yield
    finally:
        orbital_period._load_cache_quietly = old_op
        osculating_cache_manager.load_cache = old_oc


def load_planted(module_name, old, new):
    """A copy of a real module with one line changed, executed as a module
    of its own. The anchor must be found exactly once, or the plant fails
    loudly rather than testing nothing."""
    path = os.path.join(HERE, module_name + '.py')
    with open(path, encoding='utf-8') as f:
        src = f.read()
    n = src.count(old)
    if n != 1:
        raise RuntimeError('PLANT ANCHOR: %r found %d times in %s' % (old[:60], n, module_name))
    mod = types.ModuleType(module_name + '_planted')
    mod.__file__ = path
    code = compile(src.replace(old, new), path, 'exec')
    # idealized_orbits.py rewraps sys.stdout as UTF-8 when it loads. A
    # second load would wrap the console's buffer again, and the wrapper
    # it drops would close it; so the copy loads against a throwaway one.
    real = sys.stdout
    sys.stdout = io.TextIOWrapper(io.BytesIO(), encoding='utf-8')
    try:
        exec(code, mod.__dict__)
    finally:
        sys.stdout = real
    return mod


def apsis_fetch(obj_id, date_obj, center_id=None, id_type=None, **kw):
    """The position JPL would give at an apsis date: a fixture point with
    the fixture uncertainty for that date."""
    name = {'199': 'Mercury', '90000091': 'Encke', '2003 VB12': 'Sedna'}.get(str(obj_id))
    if name is None:
        return None
    d = {'x': 0.6 if name == 'Mercury' else 3.0 if name == 'Encke' else 80.0,
         'y': 0.1, 'z': 0.0}
    if name in APSIS_SIGMA_KM:
        d['position_uncertainty'] = {'range_3sigma_km': APSIS_SIGMA_KM[name]}
    return d


@contextlib.contextmanager
def module_is(name, mod):
    """A planted copy stands in for a module that the drawing imports
    inside its functions, for the length of one run."""
    real = sys.modules.get(name)
    if mod is not None:
        sys.modules[name] = mod
    try:
        yield
    finally:
        if real is not None:
            sys.modules[name] = real


def draw_sun_view(io_mod, cache, date=PLOT_DATE, ap_mod=None):
    from constants_new import color_map
    params = {'Mercury': dict(MERCURY), 'Encke': dict(ENCKE), 'Sedna': dict(SEDNA)}
    cur = {k: {'x': 0.0, 'y': 0.0, 'z': 0.0, 'record': position_record(k)} for k in params}
    fig = go.Figure()
    with cache_is(cache), module_is('apsidal_markers', ap_mod), \
            contextlib.redirect_stdout(io.StringIO()):
        io_mod.plot_idealized_orbits(
            fig, list(params), center_id='Sun', objects=OBJECT_DEFINITIONS,
            planetary_params=params, parent_planets=parent_planets, color_map=color_map,
            date=date, current_positions=cur, fetch_position=apsis_fetch,
            show_apsidal_markers=True)
    return fig


def traces(fig, body):
    out = {}
    for t in fig.data:
        tag = (t.customdata[0] if t.customdata is not None and len(t.customdata) else '') or ''
        name = t.name or ''
        if not (name.startswith(body + ' ') or tag.startswith(body + ' ')):
            continue
        if t.mode == 'lines' and 'Keplerian Orbit' in name:
            out['ellipse'] = t
        elif tag == body + ' Keplerian Orbit':
            out['info'] = t
        elif name == body + ' Keplerian Periapsis':
            out['peri'] = t
        elif name == body + ' Keplerian Apoapsis':
            out['apo'] = t
        elif name.startswith(body + ' Keplerian Position'):
            out['kpos'] = t
        elif name.startswith(body + ' Keplerian Perihelion ('):
            out['actual_peri'] = t
    return out


# ============================================================================
# THE JUDGES
# ============================================================================

NUM = r'[+-]?[0-9][0-9,]*(?:\.[0-9]+)?'


def judge_digits(body, text, err_km, findings, counts, where):
    """Every distance printed in AU or km, outside an element line, must
    sit at the place its error earns; an element must print as given."""
    for line in text.split('<br>'):
        bare = re.sub(r'<[^>]+>', '', line).strip()
        if re.match(r'^(a|e|i)\s*=', bare):
            continue
        if not re.search(r'(Distance|q =|Q =|Delta-[aq])', bare):
            continue
        for val, unit in re.findall(r'(%s) (AU|km)\b' % NUM, bare):
            v = float(val.replace(',', ''))
            err = max(err_km, FLOOR_KM)
            if unit == 'AU':
                err = err / cn.KM_PER_AU
            want = expected_place(v, err)
            got = printed_place(val)
            counts['numbers'] += 1
            if got < want:
                findings.append(('DISTANCE FINER THAN ITS ERROR', '%s %s: %s %s printed to 1e%d, '
                                 'its error earns 1e%d' % (body, where, val, unit, got, want)))
            elif got > want and '.' not in val:
                # A whole number's trailing zeros may be digits it earned:
                # 50,654,699.7 km to the whole kilometer is 50,654,700.
                # Its place cannot be read from the print, so it is not
                # called coarse.
                pass
            elif got > want:
                findings.append(('DISTANCE COARSER THAN ITS ERROR', '%s %s: %s %s printed to 1e%d, '
                                 'its error earns 1e%d' % (body, where, val, unit, got, want)))


def judge_elements_as_given(body, text, el, findings, counts):
    m = re.search(r'a=(%s) AU, e=(%s),' % (NUM, NUM), text)
    if not m:
        findings.append(('ELEMENT NOT AS GIVEN', '%s orbit hover has no "a=..., e=..." line' % body))
        return
    counts['elements'] += 2
    for got, key in ((m.group(1), 'a'), (m.group(2), 'e')):
        if float(got) != el[key]:
            findings.append(('ELEMENT NOT AS GIVEN', '%s %s printed %s, given %r'
                             % (body, key, got, el[key])))


def hover_date(text):
    m = re.search(r'Date: (\d{4}-\d\d-\d\d \d\d:\d\d:\d\d)', text)
    return datetime.strptime(m.group(1), '%Y-%m-%d %H:%M:%S') if m else None


def judge_sun_view(fig, findings, counts):
    for body, (el, off) in DRAWN.items():
        tr = traces(fig, body)
        counts['bodies'] += 1
        e = tr.get('ellipse')
        if e is None:
            findings.append(('ELLIPSE MISSING', '%s drew no Keplerian orbit' % body))
            continue
        worst = max(off_ellipse(el, off, (x, y, z)) for x, y, z in zip(e.x, e.y, e.z))
        counts['points'] += len(e.x)
        if worst > 1e-9:
            findings.append(("ELLIPSE NOT AROUND THE PERIOD'S CENTRE",
                             '%s: the drawn points lie up to %.2g of their distance off '
                             'the ellipse around its period\'s centre' % (body, worst)))
        info = tr['info'].text[0] if 'info' in tr else ''
        want = ("the solar system's center of mass" if body == 'Sedna' else 'the Sun')
        if 'Drawn around %s.' % want not in info:
            findings.append(("ELLIPSE NOT AROUND THE PERIOD'S CENTRE",
                             '%s orbit hover does not name %s' % (body, want)))
        judge_elements_as_given(body, info, el, findings, counts)
        judge_digits(body, info, BODY_ERR_KM[body], findings, counts, 'orbit hover')
        for key, nu in (('peri', 0.0), ('apo', 180.0)):
            t = tr.get(key)
            if t is None:
                findings.append(('MARKER MISSING', '%s %s marker' % (body, key)))
                continue
            p = [t.x[0], t.y[0], t.z[0]]
            exp = [a + b for a, b in zip(at_anomaly(el, nu), off)]
            if math.dist(p, exp) > 1e-9 * max(1.0, el['a']):
                findings.append(('MARKER OFF ITS ORBIT', '%s %s marker %.3g au from where its '
                                 'drawn ellipse puts it' % (body, key, math.dist(p, exp))))
            judge_digits(body, t.text[0], BODY_ERR_KM[body], findings, counts, key + ' marker')
            counts['markers'] += 1
        # The dates: perihelion is the drawn elements' TP; aphelion is TP
        # plus half the fetched period, carrying half its error.
        peri, apo = tr.get('peri'), tr.get('apo')
        if peri is not None:
            got = hover_date(peri.text[0])
            if got is None or abs((got - jd_to_dt(el['TP'])).total_seconds()) > 2:
                findings.append(('MARKER DATE WRONG', '%s perihelion %s, the drawn elements give %s'
                                 % (body, got, jd_to_dt(el['TP']))))
            counts['dates'] += 1
        if apo is not None:
            got = hover_date(apo.text[0])
            want = jd_to_dt(el['TP'] + FETCHED_DAYS[body] / 2)
            typed = TYPED.get(body)
            counts['dates'] += 1
            if got is None:
                findings.append(('MARKER DATE WRONG', '%s aphelion has no date' % body))
            elif abs((got - want).total_seconds()) > 2:
                if typed and abs((got - jd_to_dt(el['TP'] + typed / 2)).total_seconds()) <= 2:
                    findings.append(('MARKER DATED FROM THE TYPED PERIOD',
                                     '%s aphelion %s is TP plus half the typed %s days; JPL '
                                     'gave %s' % (body, got, typed, FETCHED_DAYS[body])))
                else:
                    findings.append(('MARKER DATE WRONG', '%s aphelion %s, want %s'
                                     % (body, got, want)))
            carried = FETCHED_ERR[body] / 2
            said = 'Uncertain by about' in apo.text[0]
            if carried > 1 and not said:
                findings.append(('DATE UNCERTAINTY MISSING', '%s aphelion carries %.0f days and '
                                 'does not say so' % (body, carried)))
            if carried <= 1 and said:
                findings.append(('DATE UNCERTAINTY MISSING', '%s aphelion states an uncertainty '
                                 'under a day' % body))
        k = tr.get('kpos')
        if k is not None:
            judge_digits(body, k.text[0], BODY_ERR_KM[body], findings, counts, 'Keplerian position')
            # Its place is on the drawn ellipse.
            gap = off_ellipse(el, off, (k.x[0], k.y[0], k.z[0]))
            if gap > 1e-9:
                findings.append(('MARKER OFF ITS ORBIT', '%s Keplerian position %.2g off its '
                                 'drawn ellipse' % (body, gap)))
            counts['markers'] += 1


def solve_kepler(m, e):
    big_e = m if e < 0.8 else math.pi
    for _ in range(100):
        big_e -= (big_e - e * math.sin(big_e) - m) / (1 - e * math.cos(big_e))
    return big_e


def judge_actual_markers(fig, findings, counts):
    """A marker on a position JPL gave for an apsis date prints by that
    position's own uncertainty, not by today's."""
    for body in ('Sedna', 'Encke', 'Mercury'):
        t = traces(fig, body).get('actual_peri')
        if t is None:
            findings.append(('MARKER MISSING', '%s actual perihelion marker' % body))
            continue
        err = APSIS_SIGMA_KM.get(body, MERCURY_ERR_KM)
        judge_digits(body, t.text[0], err, findings, counts, 'actual perihelion marker')
        counts['markers'] += 1


def judge_kepler_position(io_mod, findings, counts):
    """Half a year after the epoch the Keplerian position has moved by the
    period of the drawn elements: worked out here, Kepler's equation and
    all, and compared with where the marker sits."""
    fig = draw_sun_view(io_mod, fixture_cache(), date=KPOS_DATE)
    days = (KPOS_DATE - datetime(2026, 10, 12, 0, 1)).total_seconds() / cn.S_PER_DAY
    for body, (el, off) in DRAWN.items():
        k = traces(fig, body).get('kpos')
        counts['kpos'] += 1
        if k is None:
            findings.append(('MARKER MISSING', '%s Keplerian position' % body))
            continue
        m = math.radians(el['MA'] + 360.0 * days / FETCHED_DAYS[body]) % (2 * math.pi)
        big_e = solve_kepler(m, el['e'])
        nu = 2 * math.atan2(math.sqrt(1 + el['e']) * math.sin(big_e / 2),
                            math.sqrt(1 - el['e']) * math.cos(big_e / 2))
        want = [a + b for a, b in zip(at_anomaly(el, math.degrees(nu)), off)]
        gap = math.dist([k.x[0], k.y[0], k.z[0]], want)
        if gap > 1e-9 * max(1.0, el['a']):
            findings.append(('KEPLERIAN POSITION FROM ANOTHER PERIOD',
                             '%s Keplerian position %.3g au from where the drawn elements\' '
                             'period puts it %.0f days after the epoch' % (body, gap, days)))


def judge_old_record(io_mod, findings, counts):
    """A record saved before build 2 names the barycentre and holds no
    elements around it: Sedna stays drawn around the Sun, says so, and its
    aphelion is dated from the typed period, marked."""
    cache = fixture_cache()
    del cache['Sedna']['period']['elements']
    tr = traces(draw_sun_view(io_mod, cache), 'Sedna')
    counts['bodies'] += 1
    e = tr.get('ellipse')
    if e is None or max(off_ellipse(SEDNA, [0.0, 0.0, 0.0], p) for p in zip(e.x, e.y, e.z)) > 1e-9:
        findings.append(("ELLIPSE NOT AROUND THE PERIOD'S CENTRE",
                         'Sedna with a pre-build-2 record is not drawn around the Sun'))
    if 'Update the orbital elements' not in (tr['info'].text[0] if 'info' in tr else ''):
        findings.append(('NOTE MISSING', 'Sedna with a pre-build-2 record does not say why it '
                         'is drawn around the Sun'))
    apo = tr.get('apo')
    want = jd_to_dt(SEDNA['TP'] + TYPED['Sedna'] / 2)
    got = hover_date(apo.text[0]) if apo is not None else None
    counts['dates'] += 1
    if got is None or abs((got - want).total_seconds()) > 2 or 'typed' not in apo.text[0]:
        findings.append(('MARKER DATE WRONG', 'Sedna with a pre-build-2 record: aphelion %s, '
                         'want %s from the typed period, marked' % (got, want)))


def judge_window(pv_mod, findings, counts):
    """The orbital parameters window dates Earth's apsides from the period
    of the elements it draws (around the Sun), not from a period a plot
    from the Earth-Moon barycentre saved: its two dates lie half that
    period apart."""
    from orbital_elements import parent_planets as pp_map
    out = io.StringIO()
    with cache_is(fixture_cache()), contextlib.redirect_stdout(out):
        pv_mod.create_orbital_transformation_viz(
            go.Figure(), 'Earth', {'Earth': dict(EARTH)}, plot_date=PLOT_DATE,
            current_position={'x': 0.98, 'y': 0.17, 'z': 0.0}, center_object='Sun',
            parent_planets=pp_map)
    m = re.search(r'Calculated dates - Perihelion: (\S+ \S+), Aphelion: (\S+ \S+)', out.getvalue())
    counts['window'] += 1
    if not m:
        findings.append(('PARAMETERS WINDOW PERIOD FROM ANOTHER CENTRE',
                         'the window printed no apsis dates for Earth'))
        return
    peri, apo = (datetime.fromisoformat(x) for x in m.groups())
    half = abs((apo - peri).total_seconds()) / cn.S_PER_DAY
    # The fixture's fetched 365.2600 days differs from the typed 365.256, so
    # a window that fell back to the typed table shows here too.
    if abs(half - 365.2600 / 2) > 0.0005:
        findings.append(('PARAMETERS WINDOW PERIOD FROM ANOTHER CENTRE',
                         "Earth's perihelion and aphelion are %.4f days apart; its own "
                         'fetched period gives %.4f' % (half, 365.2600 / 2)))


def judge_moon(io_mod, findings, counts):
    """The Moon's arc is drawn for days_to_plot over its period: the
    fixture's fetched 27.0 days, not the typed table's."""
    fig = go.Figure()
    with cache_is(fixture_cache()), contextlib.redirect_stdout(io.StringIO()):
        io_mod.plot_moon_ideal_orbit(fig, PLOT_DATE, 'Earth', None, 365,
                                     current_position={'x': 0.0025, 'y': 0.0, 'z': 0.0},
                                     show_apsidal_markers=False, planetary_params=dict(MOON))
    arcs = [t for t in fig.data if t.mode == 'lines' and (t.name or '').startswith('Moon ')]
    want = min(int(360 * max(1.0, 365 / 27.0)), 7200)
    typed = min(int(360 * max(1.0, 365 / TYPED['Moon'])), 7200)
    counts['moon'] += len(arcs)
    if not arcs:
        findings.append(("MOON'S TYPED PERIOD USED", 'the Moon drew no orbit'))
    for t in arcs:
        n = len(t.x)
        if n == typed and n != want:
            findings.append(("MOON'S TYPED PERIOD USED", '%s drew %d points, the typed %s days\' '
                             'count; the fetched 27.0 days give %d' % (t.name, n, TYPED['Moon'], want)))
        elif n != want:
            findings.append(("MOON'S TYPED PERIOD USED", '%s drew %d points, want %d'
                             % (t.name, n, want)))


def judge_moon_markers(ap_mod, findings, counts):
    """Io's perijove and apojove, seen from Jupiter: TP plus whole periods,
    and half of one for the apojove, by JPL's 1.7714 days."""
    fig = go.Figure()
    pos = {'x': 0.0028, 'y': 0.0001, 'z': 0.0}
    with cache_is(fixture_cache()), contextlib.redirect_stdout(io.StringIO()):
        ap_mod.add_perihelion_marker(fig, 0.0028, 0, 0, 'Io', IO['a'], IO['e'], PLOT_DATE, pos,
                                     dict(IO), lambda n: 'red', center_body='Jupiter')
        ap_mod.add_apohelion_marker(fig, 0.0028, 0, 0, 'Io', IO['a'], IO['e'], PLOT_DATE, pos,
                                    dict(IO), lambda n: 'red', center_body='Jupiter')
    p = 1.771422283426844
    for t, half in zip(fig.data, (0.0, 0.5)):
        counts['dates'] += 1
        counts['markers'] += 1
        got = hover_date(t.text[0])
        jd = IO['TP'] + half * p
        while jd_to_dt(jd) < PLOT_DATE:
            jd += p
        typed_jd = IO['TP'] + half * TYPED['Io']
        while jd_to_dt(typed_jd) < PLOT_DATE:
            typed_jd += TYPED['Io']
        if got is None:
            findings.append(('MARKER DATE WRONG', '%s has no date' % t.name))
        elif abs((got - jd_to_dt(jd)).total_seconds()) > 2:
            if abs((got - jd_to_dt(typed_jd)).total_seconds()) <= 2:
                findings.append(('MARKER DATED FROM THE TYPED PERIOD', '%s %s steps by the '
                                 'typed %s days' % (t.name, got, TYPED['Io'])))
            else:
                findings.append(('MARKER DATE WRONG', '%s %s, want %s'
                                 % (t.name, got, jd_to_dt(jd))))
        judge_digits('Io', t.text[0], FLOOR_KM, findings, counts, t.name)
        if 'Accuracy: +/-' in t.text[0]:
            findings.append(('TYPED ACCURACY NOTE', '%s prints a typed accuracy' % t.name))


def judge_dispatch(findings, counts, orrery_source=None):
    if orrery_source is None:
        with open(os.path.join(HERE, 'palomas_orrery.py'), encoding='utf-8') as f:
            orrery_source = f.read()
    code = '\n'.join(ln for ln in orrery_source.split('\n') if not ln.lstrip().startswith('#'))
    calls = len(re.findall(r'\bplot_idealized_orbits\(', code)) - len(
        re.findall(r'def plot_idealized_orbits\(', code))
    if calls != 2:
        findings.append(('DISPATCH', 'palomas_orrery.py calls plot_idealized_orbits %d times, '
                         'expected 2 (static plot, animation)' % calls))
    copies = len(re.findall(r"osculating_center_body\s*=\s*'@", code))
    reads = code.count('osculating_center_body = osculating_centre_for_view(center_object_name)')
    if copies or reads != 2:
        findings.append(('DISPATCH', 'the view-to-centre map is not read from its one home: '
                         '%d typed copies, %d reads (want 0 and 2)' % (copies, reads)))
    if code.count("'record': pos_data") != 1 or code.count("'record': initial_pos") != 1:
        findings.append(('DISPATCH', 'a position record no longer travels with its position '
                         'to the orbit drawing'))
    with open(os.path.join(HERE, 'idealized_orbits.py'), encoding='utf-8') as f:
        if '_op.drawing_orbit(obj_name, center_id, params)' not in f.read():
            findings.append(('DISPATCH', 'plot_idealized_orbits no longer asks drawing_orbit '
                             'for the elements to draw'))
    counts['sources'] += 2
    # The record number is a small body; the declined update keeps the
    # view's own elements.
    if not orbital_period._is_small_body('90004912', 'id'):
        findings.append(('DISPATCH', "C/2025_K1's record 90004912 (id_type 'id') is not a small body"))
    with cache_is(fixture_cache()), contextlib.redirect_stdout(io.StringIO()):
        got = osculating_cache_manager.get_fallback_elements('Charon', '@9')
    if got.get('a') != 0.000130:
        findings.append(('DISPATCH', 'get_fallback_elements read Charon around the Sun for '
                         'the Pluto-Charon view'))


def judge_comparison(fig, findings, counts):
    """The perturbation block compares the Sun-centred osculating elements
    with the mean ones, which are around the Sun. Where the drawn orbit is
    around another centre (Sedna), the block must say so and print the
    elements it compared, and its Delta-a must be their difference
    (worked out here); where it is not, it must not claim a centre."""
    mean_a = MEAN_ELEMENTS['Sedna']['a']
    for body in ('Sedna', 'Mercury', 'Encke'):
        tr = traces(fig, body)
        info = tr['info'].text[0] if 'info' in tr else ''
        if 'Perturbation (osculating vs mean' not in info:
            continue
        counts['comparisons'] += 1
        named = 'both around the Sun' in info
        if body != 'Sedna':
            if named:
                findings.append(('PERTURBATION COMPARED WITHOUT ITS CENTRE',
                                 '%s is drawn around the Sun and its block names a centre' % body))
            continue
        if not named or ('Osculating around the Sun: a=%r AU' % SEDNA['a']) not in info:
            findings.append(('PERTURBATION COMPARED WITHOUT ITS CENTRE',
                             'Sedna is drawn around the barycentre (a=%r) and its block does not '
                             'say it compares the Sun-centred a=%r' % (SEDNA_BARY['a'], SEDNA['a'])))
        m = re.search(r'Delta-a: \+?(%s) AU' % NUM, info)
        if not m or abs(float(m.group(1)) - (SEDNA['a'] - mean_a)) > 0.01:
            findings.append(('PERTURBATION COMPARED WITHOUT ITS CENTRE',
                             'Sedna Delta-a %s is not the Sun-centred a minus the mean a (%.2f)'
                             % (m.group(1) if m else 'missing', SEDNA['a'] - mean_a)))


def judge_periosc(io_mod, findings, counts):
    """The perihelion osculating orbit (Encke's white arc) prints its
    distances by the digits rule, so it says which figure they are
    rounded to. Run offline: its perihelion time and its elements at that
    time are the recorded ones."""
    from constants_new import color_map
    info = next(o for o in OBJECT_DEFINITIONS if o['name'] == 'Encke')
    old_tp = osculating_cache_manager.resolve_tp
    old_fetch = osculating_cache_manager.fetch_osculating_elements
    osculating_cache_manager.resolve_tp = lambda name, obj_info=None: (ENCKE['TP'], 'fixture')
    osculating_cache_manager.fetch_osculating_elements = lambda **kw: {'elements': dict(ENCKE)}
    fig = go.Figure()
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            io_mod.plot_perihelion_osculating_orbit(fig, 'Encke', info, color_map, PLOT_DATE, True)
    finally:
        osculating_cache_manager.resolve_tp = old_tp
        osculating_cache_manager.fetch_osculating_elements = old_fetch
    texts = [t.text if isinstance(t.text, str) else t.text[0]
             for t in fig.data if t.text is not None and 'Osculating Orbit' in str(t.text)]
    if not texts:
        findings.append(('MARKER MISSING', "Encke's perihelion osculating orbit has no hover"))
        return
    text = texts[0]
    counts['periosc'] += 1
    judge_digits('Encke', text, FLOOR_KM, findings, counts, 'perihelion osculating orbit')
    if re.search(r'%s km' % NUM, text) and 'shown to the whole kilometer' not in text:
        findings.append(('DISTANCES WITHOUT THEIR ACCURACY SENTENCE',
                         "Encke's perihelion osculating orbit prints distances to the whole "
                         'kilometer and does not say why'))


def _axis_range_function(orrery_source):
    """palomas_orrery.calculate_axis_range_from_orbits, compiled alone from
    the source, so the frame is judged without opening the orrery's
    window."""
    import ast
    tree = ast.parse(orrery_source)
    fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef)
              and n.name == 'calculate_axis_range_from_orbits')
    ns = {}
    exec(compile(ast.Module(body=[fn], type_ignores=[]), 'palomas_orrery.py', 'exec'), ns)
    return ns['calculate_axis_range_from_orbits']


def judge_frame(findings, counts, orrery_source=None):
    """The plot's frame is sized from the ellipses as drawn: Sedna's far end
    is its barycentre aphelion moved by the barycentre's place (worked out
    here), times the 1.1 margin the orrery gives beyond 100 au."""
    if orrery_source is None:
        with open(os.path.join(HERE, 'palomas_orrery.py'), encoding='utf-8') as f:
            orrery_source = f.read()
    fn = _axis_range_function(orrery_source)
    el, off = DRAWN['Sedna']
    far = math.sqrt(sum((a + b) ** 2 for a, b in zip(at_anomaly(el, 180.0), off)))
    with cache_is(fixture_cache()), contextlib.redirect_stdout(io.StringIO()):
        rng = fn([{'name': 'Sedna'}], {}, {'Sedna': dict(SEDNA)}, parent_planets, 'Sun')
    counts['frames'] += 1
    if abs(rng[1] - 1.1 * far) > 1e-6 * far:
        findings.append(('FRAME SIZED FROM ANOTHER ORBIT',
                         "the frame reaches %.2f au; Sedna's drawn ellipse ends %.2f au from the "
                         'Sun, so it should reach %.2f' % (rng[1], far, 1.1 * far)))
    # A body drawn as fetched keeps a(1+e).
    with cache_is(fixture_cache()), contextlib.redirect_stdout(io.StringIO()):
        rng = fn([{'name': 'Mercury'}], {}, {'Mercury': dict(MERCURY)}, parent_planets, 'Sun')
    want = 1.3 * MERCURY['a'] * (1 + MERCURY['e'])
    counts['frames'] += 1
    if abs(rng[1] - want) > 1e-9:
        findings.append(('FRAME SIZED FROM ANOTHER ORBIT',
                         "Mercury's frame reaches %.6f au, want %.6f" % (rng[1], want)))


def run_checks(io_mod=None, ap_mod=None, pv_mod=None, orrery_source=None):
    import idealized_orbits
    import apsidal_markers
    import orbital_param_viz
    planted_ap = ap_mod
    io_mod = io_mod or idealized_orbits
    ap_mod = ap_mod or apsidal_markers
    pv_mod = pv_mod or orbital_param_viz
    findings = []
    counts = {'bodies': 0, 'points': 0, 'markers': 0, 'numbers': 0, 'dates': 0,
              'elements': 0, 'moon': 0, 'sources': 0, 'kpos': 0, 'window': 0,
              'comparisons': 0, 'periosc': 0, 'frames': 0}
    fig = draw_sun_view(io_mod, fixture_cache(), ap_mod=planted_ap)
    judge_sun_view(fig, findings, counts)
    judge_comparison(fig, findings, counts)
    judge_periosc(io_mod, findings, counts)
    judge_frame(findings, counts, orrery_source)
    judge_actual_markers(fig, findings, counts)
    judge_kepler_position(io_mod, findings, counts)
    judge_old_record(io_mod, findings, counts)
    judge_window(pv_mod, findings, counts)
    judge_moon(io_mod, findings, counts)
    judge_moon_markers(ap_mod, findings, counts)
    judge_dispatch(findings, counts, orrery_source)
    return findings, counts


# ============================================================================
# THE PLANTED FAULTS, each in a copy of the real source
# ============================================================================

PLANTS = [
    ('a marker dated from the typed period while a fetched record exists',
     ('idealized_orbits', "                        _p = _orbit['period']\n",
      "                        _p = {'days': KNOWN_ORBITAL_PERIODS.get(obj_name), 'err_days': None, "
      "'kind': 'typed'}\n"),
     'MARKER DATED FROM THE TYPED PERIOD'),
    ("an ellipse drawn around the Sun while the record names the barycentre",
     ('idealized_orbits', "            if _orbit['elements'] is not params:\n",
      "            _orbit = dict(_orbit, offset_au=(0.0, 0.0, 0.0), elements=params)\n"
      "            if _orbit['elements'] is not params:\n"),
     "ELLIPSE NOT AROUND THE PERIOD'S CENTRE"),
    ('an orbit hover printing a distance to ten decimals',
     ('idealized_orbits', "f\"<br>q = {_pa.distance_text(_acc, peri['q_or_Q'])}\"",
      "f\"<br>q = {peri['q_or_Q']:.10f} AU\""),
     'DISTANCE FINER THAN ITS ERROR'),
    ("the Moon's typed period used when a fetched period exists",
     ('idealized_orbits', "        moon_period_days = _p['days']\n",
      "        moon_period_days = KNOWN_ORBITAL_PERIODS.get('Moon', 27.321661)\n"),
     "MOON'S TYPED PERIOD USED"),
    ("a moon's marker dated from the typed period",
     ('apsidal_markers',
      "    period = get_orbital_period(obj_name, orbital_params.get('a', a), center_body)\n",
      "    period = {'days': KNOWN_ORBITAL_PERIODS.get(obj_name), 'err_days': None, "
      "'kind': _op.KIND_TYPED}\n"),
     'MARKER DATED FROM THE TYPED PERIOD'),
    ('the view-to-centre block copied back into palomas_orrery.py', 'orrery', 'DISPATCH'),
    ("the Keplerian position's period left to Kepler's law",
     ('idealized_orbits', "                        period_days=_orbit['period']['days'],\n",
      "                        period_days=None,\n"),
     'KEPLERIAN POSITION FROM ANOTHER PERIOD'),
    ("an apsis marker printed by today's error, not its own date's",
     ('apsidal_markers', "        acc = _pa.accuracy_for(obj_name, str(center_body), actual_pos)\n",
      "        acc = _pa.accuracy_for(obj_name, str(center_body))\n"),
     'DISTANCE FINER THAN ITS ERROR'),
    ("the parameters window dated from a barycentre view's period",
     ('orbital_param_viz', "                period_days=_own_period['days'],",
      "                center_name=center_object,"),
     'PARAMETERS WINDOW PERIOD FROM ANOTHER CENTRE'),
    ("the perihelion osculating orbit's hover without its accuracy sentence",
     ('idealized_orbits', "        f\"{_accuracy_tail(_pa.accuracy_for(obj_name, 'Sun'))}\"\n", ""),
     'DISTANCES WITHOUT THEIR ACCURACY SENTENCE'),
    ("Sedna's perturbation block not naming the centre it compared around",
     ('idealized_orbits', "_acc, _compared_around)}\"", "_acc)}\""),
     'PERTURBATION COMPARED WITHOUT ITS CENTRE'),
    ("the frame sized from the Sun-centred orbit",
     ('palomas_orrery', "                        aphelion = _drawn_far\n",
      "                        pass\n"),
     'FRAME SIZED FROM ANOTHER ORBIT'),
]


def _orrery_with_copy():
    with open(os.path.join(HERE, 'palomas_orrery.py'), encoding='utf-8') as f:
        src = f.read()
    old = 'osculating_center_body = osculating_centre_for_view(center_object_name)\n'
    return src.replace(old, "osculating_center_body = '@9' if center_object_name == "
                       "'Pluto-Charon Barycenter' else None\n", 1)


def _orrery_planted(old, new):
    with open(os.path.join(HERE, 'palomas_orrery.py'), encoding='utf-8') as f:
        src = f.read()
    n = src.count(old)
    if n != 1:
        raise RuntimeError('PLANT ANCHOR: %r found %d times in palomas_orrery' % (old[:60], n))
    return src.replace(old, new)


def main():
    problems = []
    for label, plant, expected in PLANTS:
        kw = {}
        try:
            if plant == 'orrery':
                kw['orrery_source'] = _orrery_with_copy()
            elif plant[0] == 'palomas_orrery':
                kw['orrery_source'] = _orrery_planted(plant[1], plant[2])
            else:
                module, old, new = plant
                key = {'idealized_orbits': 'io_mod', 'apsidal_markers': 'ap_mod',
                       'orbital_param_viz': 'pv_mod'}[module]
                kw[key] = load_planted(module, old, new)
            findings, _ = run_checks(**kw)
        except RuntimeError as ex:
            print('planted: %-58s COULD NOT BE PLANTED: %s' % (label, ex))
            problems.append('plant failed: %s' % label)
            continue
        hits = [d for c, d in findings if c == expected]
        if hits:
            print('planted: %-58s caught as %s (%s)' % (label, expected, hits[0]))
        else:
            print('planted: %-58s NOT CAUGHT; findings: %s'
                  % (label, sorted(set(c for c, _ in findings)) or 'none'))
            problems.append('planted fault not caught: %s' % label)

    findings, counts = run_checks()
    for cls, detail in findings:
        print('FAIL: %s -- %s' % (cls, detail))
        problems.append('%s -- %s' % (cls, detail))
    print('compared: each drawn ellipse, point by point, against the ellipse around its '
          "period's centre worked out here (Sedna's around the solar system's barycentre, "
          'moved by the barycentre\'s place seen from the Sun; Mercury\'s and Encke\'s around '
          'the Sun); each marker\'s place and date against the drawn elements and the fetched '
          'period; every distance against its body\'s error (DE430_TERRESTRIAL_POSITION_PLACE_KM '
          'for Mercury, the recorded 3-sigma figures for Encke and Sedna, the whole-kilometer '
          'floor for Io); the elements against the values given; the Keplerian position half a '
          'year on against the drawn elements\' period; a pre-build-2 record\'s drawing '
          'and dates; the parameters window\'s apsis dates against Earth\'s own period; '
          'the Moon\'s arc against its fetched period; Sedna\'s perturbation block against '
          'the Sun-centred a minus the mean a; Encke\'s perihelion osculating orbit against the '
          'whole-kilometer floor and its sentence; the frame against Sedna\'s drawn far end; '
          'and the dispatch in palomas_orrery.py')
    print('examined: Mercury, Encke and Sedna from the Sun (ellipse, orbit hover, periapsis, '
          'apoapsis, actual perihelion, Keplerian position); Sedna with a pre-build-2 record; '
          'Earth in the orbital parameters window; the Moon from Earth; Io\'s perijove and '
          'apojove from Jupiter; Encke\'s perihelion osculating orbit; the frame for Sedna and '
          'for Mercury; palomas_orrery.py and idealized_orbits.py')
    if problems:
        print('ORBIT MARKERS: FAIL -- %d problem(s)' % len(problems))
        return 1
    print('ORBIT MARKERS: PASS -- %d of %d planted faults caught by name; %d ellipses, %d '
          'drawn points on their period\'s centre; %d markers, %d dates, %d printed distances '
          'against their errors; %d elements as given; %d Keplerian positions half a year '
          'on; %d parameters-window date pairs; %d Moon arcs; %d perturbation blocks; '
          '%d perihelion osculating orbits; %d frames; %d sources read'
          % (len(PLANTS), len(PLANTS), counts['bodies'], counts['points'], counts['markers'],
             counts['dates'], counts['numbers'], counts['elements'], counts['kpos'],
             counts['window'], counts['moon'], counts['comparisons'], counts['periosc'],
             counts['frames'], counts['sources']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
