"""
test_position_digits.py - the orrery's body hover prints each distance and
speed to the digits JPL's errors earn, and proof that this check can fail.

The body hover (visualization_utils.format_detailed_hover_text, which the
static plot, the animation and the social export all use) once printed
ten decimal places of an AU and ten figures of a kilometre for every body
(L-401). Since build 1 it prints by the error position_accuracy.py works
out. This file builds the hover for a fixed set of bodies and centres,
offline, and judges every distance and speed line against errors it works
out ITSELF: from the rows in constants_new.py read by name, from the
fixture's own 3-sigma figures, and from the stated floors. It shares no
arithmetic with position_accuracy.py, so a fault there shows here.

It first plants a fault for each thing it must catch, and requires the
right finding, by name:

    planted                                      must be caught as
    Jupiter's row read ten times finer           PLANET FINER THAN ITS ROW
    a missing sigma turned into a tiny one       SMALL BODY WITHOUT SIGMA NOT IN THE NO-ERROR STATE
    the kilometer floor moved to meters          NO-ERROR BODY FINER THAN THE FLOOR
    the light-time line left out                 LINE DROPPED
    a typed sky value put back                   TYPED SKY VALUE
    the speed's error divided by a thousand      SPEED FINER THAN ITS DISTANCE
    fetch_position's 2xr call removed            DISPATCH
    the 2xr columns read by position             2XR READ BY POSITION
    a no-error body ignoring its centre's error  NO-ERROR BODY IGNORES ITS CENTRE
    a zero sigma taken as a figure               ZERO SIGMA TAKEN AS A FIGURE
    the Voyagers' data-sheet figures dropped     SPACECRAFT DATA-SHEET FIGURE IGNORED
    the surface line dropped for a giant planet  SURFACE LINE DROPPED
    the small-body database named for a planet   DATABASE MENTIONED FOR A PLANET OR MOON
    another body's period printed as the body's  TARGET WORDS DROPPED
    JPL's "n.a." said as not included            JPL'S NONE SAID AS NOT INCLUDED
    a failed question said as JPL stating none   A FAILED QUESTION SAID AS JPL STATING NONE

The last five go beyond the brief's six. The first two prove the static
plot still asks for a small body's uncertainty and reads Horizons'
columns by name, against an answer recorded from JPL; the last two come
from a cold review of the build (2026-10-12), with its other cases: a
pair must print the same digits from either end, and every listed
object is hovered from the Sun, Earth and Neptune. The fifth comes
from Tony's ruling of the same day (option A): a spacecraft whose
Horizons data sheet states a predicted pointing angle (the Voyagers)
prints by that angle at its distance from Earth. The twelfth comes from
Tony's look at build 1 (2026-10-12): every centre with a radius gets the
surface line, measured from one radius, the Sun and the giant planets
included; and the period sentence does not name JPL's small-body
database for a planet or a moon, which it does not hold.

Then it judges the real code. The last line starts "POSITION DIGITS:",
which the maintenance run quotes, and says what was compared and how many
hovers were examined.

Run (VS Code Run button, or):
    python test_position_digits.py

Never contacts Horizons. Live behaviour is the patch's live check and
Tony's look.

Role: devtool
Domain: dev_tools

Module created: October 12, 2026 with Anthropic's Claude Opus 5.5 (L-401,
build 1).
Module updated: October 12, 2026 with Anthropic's Claude Opus 5.5 (L-401,
Tony's look: the surface line for every centre with a radius, and the
period sentence's database clause for asteroids and comets only, each
with a planted fault).
Module updated: October 15, 2026 with Anthropic's Claude Opus 5.5 (L-445,
Earth's period: a period asked of another body says whose it is, in the
hover and the parameters window, and a body's own period does not; the
fourteenth planted fault drops those words.)
Module updated: October 29, 2026 with Anthropic's Claude Opus 5.5 (L-399,
L-484: a small body whose 2xr answer has no figure, "n.a." in JPL's
column, says JPL states no accuracy, and one whose question failed or was
never asked says the figure is not included here: Bennu both ways, and
Encke's zero sigma now reads as JPL stating none. Two planted faults, one
for each sentence said in the other's place.)
"""
import math
import os
import re
import sys
from contextlib import contextmanager

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import constants_new as cn
import celestial_coordinates
import position_accuracy as pa
from celestial_objects import OBJECT_DEFINITIONS
from orbital_elements import parent_planets
from visualization_utils import format_detailed_hover_text
import orbital_period

# ============================================================================
# THE CHECKER'S OWN ARITHMETIC (shares nothing with position_accuracy.py)
# ============================================================================

# The checker's own copies of the two stated floors, as half-units, kept
# apart from position_accuracy.py on purpose so a fault there shows here.
FLOOR_KM = 0.5
# Source: documentation/DESIGN_L401_distance_digits_rulings_20261011.md,
# Source+: section 4, item 4 -- whole kilometers; half of one is the error.
SPEED_FLOOR_KM_S = 0.0005
# Source: documentation/HANDOFF_L401_distance_build1_brief_20261011.md,
# Source+: section 2 -- one meter per second; half of it is the error.
DAY_S = cn.S_PER_DAY


def place_for(err):
    """The Report test, written out: the power of ten whose half-unit is
    nearest err on a log scale, a tie going to the coarser."""
    best = None
    for p in range(-20, 21):
        d = abs(math.log10(0.5 * 10.0 ** p) - math.log10(err))
        if best is None or d < best[0] - 1e-12 or (abs(d - best[0]) <= 1e-12 and p > best[1]):
            best = (d, p)
    return best[1]


def expected_place(value, err):
    p = place_for(err)
    if value:
        top = int(math.floor(math.log10(abs(value))))
        p = min(p, top)
    return p


def printed_place(s):
    s = s.replace(',', '')
    if '.' in s:
        return -len(s.split('.')[1])
    stripped = s.lstrip('-')
    return len(stripped) - len(stripped.rstrip('0')) if stripped.strip('0') else 0


def matches(s, value, p):
    """Does the printed string s carry value at place p, no finer, no coarser?"""
    t = s.replace(',', '')
    try:
        got = float(t)
    except ValueError:
        return False
    if p < 0:
        if '.' not in t or len(t.split('.')[1]) != -p:
            return False
        return abs(got - round(value, -p)) <= 0.5 * 10.0 ** p + 1e-9 * abs(value)
    if '.' in t:
        return False
    want = round(value / 10.0 ** p) * 10.0 ** p
    return abs(got - want) <= 1e-6 * max(1.0, abs(want))


def row(name):
    return 0.5 * getattr(cn, name)


# ============================================================================
# THE FIXTURES: bodies, centres, positions, and what each must print by
# ============================================================================

def _od(r_au, v_km_s, sigma=None, missing=False, ra_sigma=None, earth_au=None,
        na=False):
    v = v_km_s * DAY_S / cn.KM_PER_AU
    d = {'x': r_au, 'y': 0.0, 'z': 0.0, 'vx': 0.0, 'vy': v, 'vz': 0.0,
         'velocity': v, 'ra': 123.4567, 'dec': -12.3456,
         'ra_3sigma': ra_sigma, 'dec_3sigma': ra_sigma}
    if sigma:
        d['position_uncertainty'] = {'range_3sigma_km': sigma[0],
                                     'speed_3sigma_km_s': sigma[1],
                                     'key': {'body': 'fixture'}}
    if missing:
        d['position_uncertainty'] = {'missing': 'fixture: no 2xr columns',
                                     'key': {'body': 'fixture'}}
    if na:
        # JPL answered; its uncertainty column read "n.a." (L-399, L-484):
        # uncertainty_record() writes the figure fields as None.
        d['position_uncertainty'] = {'range_3sigma_km': None,
                                     'speed_3sigma_km_s': None,
                                     'key': {'body': 'fixture'}}
    if earth_au is not None:
        d['earth_distance_au'] = earth_au
    return d


def sheet_err_km(name, earth_au):
    """The checker's own conversion of a Voyager's data-sheet angle: the
    larger of RA and DEC, from the rows by name, at its distance from Earth."""
    n = name.split()[-1]
    arcsec = max(getattr(cn, 'VOYAGER_%s_POINTING_RA_2030_ARCSEC' % n),
                 getattr(cn, 'VOYAGER_%s_POINTING_DEC_2030_ARCSEC' % n))
    return math.radians(arcsec / 3600.0) * earth_au * cn.KM_PER_AU


# (name, centre, obj_data, state, distance error, speed rule)
#   distance error: ('row', NAME) | ('sigma', km) | ('floor',)
#   speed rule:     'relative' | ('sigma', km/s) | 'floor' | 'floor_or_relative'
FIXTURES = [
    ('Mercury', 'Sun', _od(0.3871, 47.36), 'published',
     ('row', 'DE430_TERRESTRIAL_POSITION_PLACE_KM'), 'relative'),
    ('Jupiter', 'Sun', _od(5.2034, 13.07), 'published',
     ('row', 'DE430_JUPITER_SATURN_POSITION_PLACE_KM'), 'relative'),
    ('Neptune', 'Sun', _od(29.91, 5.43), 'published',
     ('row', 'DE430_URANUS_NEPTUNE_PLUTO_POSITION_PLACE_KM'), 'relative'),
    ('Mars', 'Earth', _od(0.5214, 15.2), 'published',
     ('row', 'DE430_TERRESTRIAL_POSITION_PLACE_KM'), 'relative'),
    ('Moon', 'Earth', _od(0.002570, 1.022), 'published',
     ('row', 'DE430_MOON_POSITION_PLACE_KM'), 'relative'),
    ('Sun', 'Jupiter', _od(5.2034, 13.07), 'published',
     ('row', 'DE430_JUPITER_SATURN_POSITION_PLACE_KM'), 'relative'),
    ('Sedna', 'Sun', _od(85.13, 4.30, sigma=(257820.0, 2.5476e-4), ra_sigma=0.41),
     'computed', ('sigma', 257820.0), ('sigma', 2.5476e-4)),
    ('Encke', 'Sun', _od(2.0108, 33.17, sigma=(1012.3, 1.3e-5), ra_sigma=0.9),
     'computed', ('sigma', 1012.3), ('sigma', 1.3e-5)),
    ('Sedna', 'Sun', _od(85.13, 4.30, missing=True), 'none', ('floor',), 'floor'),
    ('Io', 'Jupiter', _od(0.0028189, 17.33), 'none', ('floor',), 'floor'),
    ('Io', 'Sun', _od(5.2001, 12.9), 'floor',
     ('row', 'DE430_JUPITER_SATURN_POSITION_PLACE_KM'), 'floor_or_relative'),
    # Voyager 1 and 2: JPL's data sheets state a predicted pointing angle
    # (Tony's option A, 2026-10-12); with no distance from Earth fetched (the
    # animation) the figure is not included.
    ('Voyager 1', 'Sun', _od(170.22, 16.9, earth_au=170.9), 'sheet',
     ('sheet', 'Voyager 1', 170.9), 'relative'),
    ('Voyager 1', 'Sun', _od(170.22, 16.9), 'none', ('floor',), 'floor'),
    ('EM-L1', 'Earth', _od(0.002186, 0.85), 'none', ('floor',), 'floor'),
    ('Pluto', 'Pluto-Charon Barycenter', _od(1.4e-5, 0.02), 'none', ('floor',), 'floor'),
    # From the cold review of 2026-10-12: a no-error body seen from a centre
    # with a larger error takes that error as a floor; a small body's own
    # figure governing a floor case keeps the computed words; the
    # Earth-Moon system; a small-body record listed by id_type 'id'; a
    # system record fetched where JPL states the small body's figure; a
    # zero sigma.
    ('Voyager 2', 'Neptune', _od(114.3, 15.3, earth_au=144.6), 'sheet',
     ('sheet', 'Voyager 2', 144.6), 'relative'),
    ('EM-L1', 'Neptune', _od(29.9, 5.4), 'floor',
     ('row', 'DE430_URANUS_NEPTUNE_PLUTO_POSITION_PLACE_KM'), 'floor_or_relative'),
    ('Sedna', 'Neptune', _od(55.2, 6.1, missing=True), 'floor',
     ('row', 'DE430_URANUS_NEPTUNE_PLUTO_POSITION_PLACE_KM'), 'floor_or_relative'),
    ('Sedna', 'Io', _od(80.4, 12.0, sigma=(257820.0, 2.5476e-4)), 'floor',
     ('sigma', 257820.0), 'sigma_or_floor'),
    ('Earth', 'Earth-Moon Barycenter', _od(3.1e-5, 0.012), 'published',
     ('row', 'DE430_MOON_POSITION_PLACE_KM'), 'relative'),
    ('C/2025_K1', 'Sun', _od(3.2, 22.0, missing=True), 'none', ('floor',), 'floor'),
    ('Makemake', 'Earth', _od(52.6, 30.1), 'none', ('floor',), 'floor'),
    ('Encke', 'Sun', _od(2.0108, 33.17, sigma=(0.0, 0.0)), 'none', ('floor',), 'floor'),
    # L-399, L-484 (2026-10-29): JPL's 2xr answer for Bennu with "n.a." in
    # its uncertainty column, and Bennu with no record (never asked).
    ('Bennu', 'Sun', _od(1.13, 28.0, na=True), 'none', ('floor',), 'floor'),
    ('Bennu', 'Sun', _od(1.13, 28.0), 'none', ('floor',), 'floor'),
]

# What each fixture's sentences must say, and must not, beyond its state:
# a sentence check by substring alone cannot see a false sentence.
WORDS = {
    ('Sedna', 'Io'): (["JPL's uncertainty for Sedna's position",
                       "JPL states no accuracy for Io's orbit around Jupiter"],
                      ['published accuracy', 'may be larger']),
    # Tony, 2026-10-12: an unstated error is not called a large one; then,
    # on Fable's reading of the Voyager 2 data sheet, option A: the sheet's
    # angle, converted at the distance from Earth, said to be ours.
    ('Voyager 2', 'Neptune'): (["predicted sky-position uncertainty",
                                "for Voyager 2 in 2030, 4.718 arcseconds",
                                "JPL states none for the distance itself",
                                "so this conversion is ours"],
                               ['may be larger', 'JPL states no accuracy']),
    ('Voyager 1', 'Sun'): ([], ['JPL states no accuracy']),
    ('EM-L1', 'Neptune'): (["published accuracy for", "Neptune's orbit",
                            "JPL states no accuracy for EM-L1's position"],
                           ['may be larger']),
    ('Sedna', 'Neptune'): (["JPL's figure for Sedna's position is not included here",
                            "may be larger"],
                           ["JPL states no accuracy for Sedna"]),
    ('Earth', 'Earth-Moon Barycenter'): (["the Moon's orbit around Earth"],
                                         ['JPL states no accuracy']),
    ('C/2025_K1', 'Sun'): (["is not included here"], ['JPL states no accuracy']),
    ('Makemake', 'Earth'): (["is not included here"], ['JPL states no accuracy']),
    ('Io', 'Sun'): (["JPL states no accuracy for Io's orbit around Jupiter"],
                    ['may be larger']),
}

SENTENCES = {
    'published': "published accuracy for",
    'computed': "on this date, at three standard deviations",
    'floor': "These distances are",
    'sheet': "predicted sky-position uncertainty",
}
NONE_WORDS = {
    'not_fetched': "JPL's uncertainty for this position is not included here",
    'unstated': "JPL states no accuracy for this position",
}
SPEED_WORDS = {
    'relative': "same relative precision as the distance",
    'sigma': "JPL's uncertainty in its velocity",
    'floor': "JPL states no uncertainty for this body's speed",
    'not_fetched': "JPL's uncertainty for this body's speed is not included here",
}


def _hover(name, centre, obj_data):
    full, _mini, _note = format_detailed_hover_text(
        dict(obj_data), name, centre, OBJECT_DEFINITIONS, {}, parent_planets,
        cn.CENTER_BODY_RADII, cn.KM_PER_AU, cn.LIGHT_MINUTES_PER_AU,
        cn.KNOWN_ORBITAL_PERIODS)
    return full.split('<br>')


def _find(lines, pattern):
    for ln in lines:
        m = re.match(pattern, ln)
        if m:
            return m
    return None


def judge_fixture(fx, findings, counts):
    name, centre, od, state, derr, srule = fx
    tag = '%s from %s' % (name, centre)
    acc = pa.resolve_accuracy(name, centre, od, OBJECT_DEFINITIONS, parent_planets)
    if acc['state'] != state:
        pu = od.get('position_uncertainty') or {}
        if state == 'none' and pu.get('missing'):
            findings.append(('SMALL BODY WITHOUT SIGMA NOT IN THE NO-ERROR STATE',
                             '%s: state %r, expected none' % (tag, acc['state'])))
        elif state == 'sheet':
            findings.append(('SPACECRAFT DATA-SHEET FIGURE IGNORED',
                             '%s: state %r, expected the data sheet\'s figure' % (tag, acc['state'])))
        elif state == 'none' and pu.get('range_3sigma_km') == 0.0:
            findings.append(('ZERO SIGMA TAKEN AS A FIGURE',
                             '%s: state %r, expected none' % (tag, acc['state'])))
        elif state == 'floor' and acc['state'] == 'none':
            findings.append(('NO-ERROR BODY IGNORES ITS CENTRE',
                             '%s: state none, expected the centre as a floor' % tag))
        else:
            findings.append(('WRONG STATE', '%s: state %r, expected %r'
                             % (tag, acc['state'], state)))
    lines = _hover(name, centre, od)
    counts['hovers'] += 1
    text = '\n'.join(lines)

    # The error this fixture must print by, worked out here.
    if derr[0] == 'row':
        err_km = max(row(derr[1]), FLOOR_KM)
        governs = 'row' if row(derr[1]) >= FLOOR_KM else 'floor'
    elif derr[0] == 'sigma':
        err_km = max(derr[1], FLOOR_KM)
        governs = 'sigma' if derr[1] >= FLOOR_KM else 'floor'
    elif derr[0] == 'sheet':
        err_km = max(sheet_err_km(derr[1], derr[2]), FLOOR_KM)
        governs = 'sheet'
    else:
        err_km, governs = FLOOR_KM, 'floor'
    dist_au = math.sqrt(od['x'] ** 2 + od['y'] ** 2 + od['z'] ** 2)
    dist_km = dist_au * cn.KM_PER_AU
    lm = dist_au * cn.LIGHT_MINUTES_PER_AU
    err_au = err_km / cn.KM_PER_AU
    err_lm = err_au * cn.LIGHT_MINUTES_PER_AU

    distance_lines = [
        ('AU', r'Distance from Center: ([-\d,.]+) AU$', dist_au, err_au),
        ('kilometers', r'Distance: ([-\d,.]+) kilometers$', dist_km, err_km),
    ]
    if lm < 60:
        distance_lines.append(('light-minutes', r'Distance: ([-\d,.]+) light-minutes$', lm, err_lm))
    else:
        distance_lines.append(('light-hours', r'Distance: ([-\d,.]+) light-hours$',
                               lm / 60, err_lm / 60))
    # Every centre with a radius gets the surface line, measured from one
    # radius: the solid surface, or the 1-bar level of a giant planet and
    # the Sun's photosphere (Tony's ruling, restated 2026-10-12, L-401).
    radius = cn.CENTER_BODY_RADII.get(centre)
    if radius:
        distance_lines.append(('surface', r'Distance to Center Surface: ([-\d,.]+)',
                               dist_km - radius, err_km))
    elif _find(lines, r'Distance to Center Surface'):
        findings.append(('SURFACE LINE WITHOUT A RADIUS', '%s: %s has no radius in '
                         'CENTER_BODY_RADII' % (tag, centre)))

    for unit, pat, value, err in distance_lines:
        m = _find(lines, pat)
        if not m:
            if unit == 'surface':
                findings.append(('SURFACE LINE DROPPED', '%s: no surface line, though '
                                 '%s has a radius' % (tag, centre)))
            else:
                findings.append(('LINE DROPPED', '%s: no %s line' % (tag, unit)))
            continue
        counts['lines'] += 1
        p = expected_place(value, err)
        if not matches(m.group(1), value, p):
            got = printed_place(m.group(1))
            if got < p and state == 'none':
                cls = 'NO-ERROR BODY FINER THAN THE FLOOR'
            elif got < p and governs == 'row':
                cls = 'PLANET FINER THAN ITS ROW'
            elif got < p and governs == 'sheet':
                cls = 'SPACECRAFT FINER THAN ITS DATA SHEET'
            elif got < p and governs == 'floor':
                cls = 'FINER THAN THE FLOOR'
            elif got < p:
                cls = 'FINER THAN ITS SIGMA'
            else:
                cls = 'WRONG DIGITS'
            findings.append((cls, '%s, %s line: printed %s, expected the 10^%d place'
                             % (tag, unit, m.group(1), p)))

    # The speed, by the rule this fixture names.
    speed_km_s = od['velocity'] * cn.KM_PER_AU / DAY_S
    if srule == 'relative':
        v_err = speed_km_s * err_km / dist_km
    elif srule == 'floor':
        v_err = SPEED_FLOOR_KM_S
    elif srule == 'floor_or_relative':
        v_err = max(SPEED_FLOOR_KM_S, speed_km_s * err_km / dist_km)
    elif srule == 'sigma_or_floor':
        v_err = max(SPEED_FLOOR_KM_S, 2.5476e-4)
    else:
        v_err = srule[1]
    speed_lines = [
        ('AU/day', r'Velocity: ([-\d,.]+) AU/day$', od['velocity'],
         v_err * DAY_S / cn.KM_PER_AU),
        ('km/hr', r'Velocity: ([-\d,.]+) km/hr', speed_km_s * 3600, v_err * 3600),
        ('km/sec', r'Velocity: .* km/hr \(([-\d,.]+) km/sec\)$', speed_km_s, v_err),
    ]
    for unit, pat, value, err in speed_lines:
        m = _find(lines, pat)
        if not m:
            findings.append(('LINE DROPPED', '%s: no speed line in %s' % (tag, unit)))
            continue
        counts['lines'] += 1
        p = expected_place(value, err)
        if not matches(m.group(1), value, p):
            got = printed_place(m.group(1))
            cls = ('SPEED FINER THAN ITS DISTANCE' if got < p and srule == 'relative'
                   else 'SPEED FINER THAN ITS ERROR' if got < p
                   else 'WRONG SPEED DIGITS')
            findings.append((cls, '%s, speed in %s: printed %s, expected the 10^%d place'
                             % (tag, unit, m.group(1), p)))

    # The sentences: which kind of figure, in words.
    if state == 'none':
        pu = od.get('position_uncertainty')
        # JPL answered with no figure ("n.a.", or zero): JPL states none.
        # A failed question ('missing'), or none asked for a small body,
        # is the figure not included here (L-399, L-484).
        jpl_none = (isinstance(pu, dict) and 'range_3sigma_km' in pu
                    and 'missing' not in pu)
        if jpl_none:
            reason = 'unstated'
        else:
            reason = ('not_fetched' if (pu
                                        or (name, centre) in (('Makemake', 'Earth'),
                                                              ('Bennu', 'Sun'))
                                        or name in ('Voyager 1', 'Voyager 2'))
                      else 'unstated')
        if NONE_WORDS[reason] not in text:
            if jpl_none:
                cls = "JPL'S NONE SAID AS NOT INCLUDED"
            elif (reason == 'not_fetched' and isinstance(pu, dict) and pu.get('missing')
                  and NONE_WORDS['unstated'] in text):
                cls = 'A FAILED QUESTION SAID AS JPL STATING NONE'
            elif reason == 'not_fetched':
                cls = 'SMALL BODY WITHOUT SIGMA NOT IN THE NO-ERROR STATE'
            else:
                cls = 'LINE DROPPED'
            findings.append((cls, '%s: the no-error sentence is missing' % tag))
        want = SPEED_WORDS['not_fetched' if reason == 'not_fetched' else 'floor']
    else:
        if SENTENCES[state] not in text:
            findings.append(('LINE DROPPED', '%s: the %s sentence is missing' % (tag, state)))
        want = None if srule in ('floor_or_relative', 'sigma_or_floor') else SPEED_WORDS[
            srule if isinstance(srule, str) else 'sigma']
    if want and want not in text:
        findings.append(('LINE DROPPED', '%s: the speed sentence is missing' % tag))
    must, mustnot = WORDS.get((name, centre), ([], []))
    flat = ' '.join(text.split())
    for w in must:
        if w not in flat:
            findings.append(('FALSE OR MISSING WORDS', '%s: lacks "%s"' % (tag, w)))
    for w in mustnot:
        if w in flat:
            findings.append(('FALSE OR MISSING WORDS', '%s: says "%s"' % (tag, w)))

    # The sky position (Tony's look, 2026-10-12, option B): one heading, the
    # two coordinates, one uncertainty line -- JPL's fetched figure, or
    # plain words; never a typed value.
    if 'Sky position seen from Earth:' not in lines:
        findings.append(('WRONG SKY NOTE', '%s: no "Sky position seen from Earth:" heading'
                         % tag))
    note = [ln for ln in lines if ln.strip().startswith('Uncertainty:')]
    if len(note) != 1:
        findings.append(('LINE DROPPED', '%s: %d sky-position uncertainty lines, expected 1'
                         % (tag, len(note))))
    else:
        counts['lines'] += 1
        if od.get('ra_3sigma') is None:
            if '+/-' in note[0] or note[0].strip() != 'Uncertainty: none given by JPL with this position':
                findings.append(('TYPED SKY VALUE', '%s: %s' % (tag, note[0].strip())))
        elif not note[0].strip().endswith('(JPL, 3-sigma)'):
            findings.append(('WRONG SKY NOTE', '%s: %s' % (tag, note[0].strip())))
    if any('(apparent' in ln for ln in lines):
        findings.append(('WRONG SKY NOTE', '%s: the old note in parentheses is back' % tag))


def scan_sources(findings, sky_source=None, orrery_source=None):
    """The typed table must not be back in the code, and fetch_position must
    still make the 2xr call for small bodies and the hover callers stay three."""
    if sky_source is None:
        with open(os.path.join(HERE, 'celestial_coordinates.py'), encoding='utf-8') as f:
            sky_source = f.read()
    code = '\n'.join(ln for ln in sky_source.split('\n') if not ln.lstrip().startswith('#'))
    if re.search(r'MAJOR_BODY_UNCERTAINTIES\s*(=|\[)', code) or ', typical"' in code:
        findings.append(('TYPED SKY VALUE', 'celestial_coordinates.py holds a typed '
                         'uncertainty table or a "typical" fallback'))
    if orrery_source is None:
        with open(os.path.join(HERE, 'palomas_orrery.py'), encoding='utf-8') as f:
            orrery_source = f.read()
    m = re.search(r'\ndef fetch_position\(.*?\n(?=def )', orrery_source, re.S)
    body = m.group(0) if m else ''
    if 'fetch_small_body_state(' not in body:
        findings.append(('DISPATCH', 'fetch_position no longer fetches a small body '
                         'with its 2xr uncertainty'))
    calls = len(re.findall(r'=\s*format_detailed_hover_text\(', orrery_source))
    if calls != 3:
        findings.append(('DISPATCH', 'palomas_orrery.py calls format_detailed_hover_text '
                         '%d times, expected 3 (static plot, animation start, frames)' % calls))


# Horizons' answer for 2P/Encke (record 90000091) from the Sun at JD
# 2461325.5 with VEC_TABLE='2xr' and OUT_UNITS='AU-D', the header and the
# data line as read 2026-10-12 through the chat's web-fetch tool.
RECORDED_2XR_HEADER = (
    '            JDTDB,            Calendar Date (TDB),                      X,'
    '                      Y,                      Z,                     VX,'
    '                     VY,                     VZ,             X_s,'
    '             Y_s,             Z_s,            VX_s,            VY_s,'
    '            VZ_s,             R_s,             T_s,             N_s,'
    '            VR_s,            VT_s,            VN_s,')
RECORDED_2XR_DATA = (
    '2461325.500000000, A.D. 2026-Oct-12 00:00:00.0000,  1.942725296484269E+00,'
    '  5.522246602639908E-01,  2.704195947645857E-01, -1.203972263020625E-02,'
    '  3.443839821663160E-03, -4.371888997361478E-04,  2.12131568E-06,'
    '  7.25420125E-07,  4.93573275E-07,  1.24183900E-08,  2.35613571E-09,'
    '  2.08273117E-09,  2.25639403E-06,  3.14493101E-07,  2.82151047E-07,'
    '  1.18004525E-08,  4.59717385E-09,  1.92895507E-09,')
RECORDED_R_S_AU = 2.25639403E-06
RECORDED_V_S_AU_D = (1.18004525E-08, 4.59717385E-09, 1.92895507E-09)


def _answer(header, data):
    return ('Target body name: 2P/Encke\n' + header + '\n$$SOE\n' + data
            + '\n$$EOE\n')


def _swap_columns(header, data, a, b):
    hs, ds = header.split(','), data.split(',')
    names = [h.strip() for h in hs]
    i, j = names.index(a), names.index(b)
    hs[i], hs[j] = hs[j], hs[i]
    ds[i], ds[j] = ds[j], ds[i]
    return ','.join(hs), ','.join(ds)


def check_2xr_reading(findings, counts):
    """The 2xr answer is read by column name: the recorded answer, the same
    answer with R_s and X_s swapped, and one whose R_s is "n.a."."""
    want_km = 3 * RECORDED_R_S_AU * cn.KM_PER_AU
    want_v = 3 * math.sqrt(sum(x * x for x in RECORDED_V_S_AU_D)) * cn.KM_PER_AU / DAY_S
    cases = [('as recorded', RECORDED_2XR_HEADER, RECORDED_2XR_DATA),
             ('R_s and X_s swapped',) + _swap_columns(RECORDED_2XR_HEADER,
                                                       RECORDED_2XR_DATA, 'R_s', 'X_s')]
    for label, h, d in cases:
        counts['answers'] += 1
        try:
            row = pa.parse_vectors_2xr(_answer(h, d))[0]
            rec = pa.uncertainty_record(row, '90000091', '@10', 2461325.5)
        except Exception as ex:
            findings.append(('2XR READ BY POSITION', '%s: %s' % (label, ex)))
            continue
        if (rec['range_3sigma_km'] is None or abs(rec['range_3sigma_km'] - want_km) > 1e-6 * want_km
                or rec['speed_3sigma_km_s'] is None
                or abs(rec['speed_3sigma_km_s'] - want_v) > 1e-6 * want_v):
            findings.append(('2XR READ BY POSITION', '%s: 3-sigma range %s km, speed %s km/s; '
                             'expected %.1f km, %.3g km/s' % (label, rec['range_3sigma_km'],
                                                              rec['speed_3sigma_km_s'],
                                                              want_km, want_v)))
    counts['answers'] += 1
    names = [x.strip() for x in RECORDED_2XR_HEADER.split(',')]
    toks = RECORDED_2XR_DATA.split(',')
    toks[names.index('R_s')] = '  n.a.'
    try:
        row = pa.parse_vectors_2xr(_answer(RECORDED_2XR_HEADER, ','.join(toks)))[0]
        rec = pa.uncertainty_record(row, '90000091', '@10', 2461325.5)
        od = _od(2.0108, 33.17)
        od['position_uncertainty'] = rec
        acc = pa.resolve_accuracy('Encke', 'Sun', od, OBJECT_DEFINITIONS, parent_planets)
        if acc['state'] != 'none':
            findings.append(('SMALL BODY WITHOUT SIGMA NOT IN THE NO-ERROR STATE',
                             'Encke with R_s "n.a.": state %r' % acc['state']))
    except Exception as ex:
        findings.append(('2XR READ BY POSITION', 'R_s "n.a.": %s' % ex))


SYMMETRIC_PAIRS = [('Jupiter', 'Mars'), ('Sun', 'Jupiter'), ('Neptune', 'EM-L1'),
                   ('Io', 'Earth'), ('EM-L1', 'Uranus')]


def check_symmetry(findings, counts):
    """A from B and B from A are one distance with one error, so they must
    print the same digits (neither side a small body, whose figure is
    fetched for the body only)."""
    for a, b in SYMMETRIC_PAIRS:
        got = []
        for name, centre in ((a, b), (b, a)):
            lines = _hover(name, centre, _od(4.321, 10.0))
            m = _find(lines, r'Distance: ([-\d,.]+) kilometers$')
            got.append(m.group(1) if m else None)
        counts['pairs'] += 1
        if got[0] != got[1]:
            findings.append(('NOT SYMMETRIC', '%s from %s prints %s km, %s from %s prints %s km'
                             % (a, b, got[0], b, a, got[1])))


def _checker_small(entry, centre):
    """The checker's own reading of which entries are JPL small bodies."""
    if centre == 'Sun' and 'helio_id' in entry:
        return True
    oid, t = str(entry.get('id', '')), entry.get('id_type')
    if t in ('smallbody', 'designation', 'asteroid_name', 'comet_name') and not oid.startswith('-'):
        return True
    return bool(re.match(r'^9\d{7}$', oid))


def check_every_object(findings, counts):
    """Every entry in the object list, from the Sun, Earth and Neptune,
    with no fetched figure: a JPL small body must never be said to have no
    stated accuracy, and nothing may print finer than whole kilometers."""
    for o in OBJECT_DEFINITIONS:
        if o.get('object_type') in ('exoplanet', 'exo_host_star', 'exo_binary_star',
                                    'exo_barycenter', 'fixed'):
            continue
        for centre in ('Sun', 'Earth', 'Neptune'):
            if o['name'] == centre:
                continue
            small = _checker_small(o, centre) or (
                'helio_id' in o and o.get('object_type') != 'satellite')
            lines = _hover(o['name'], centre, _od(7.0, 9.0))
            counts['sweep'] += 1
            flat = ' '.join(' '.join(lines).split())
            if small and o.get('object_type') != 'satellite':
                for w in ('JPL states no accuracy for this position',
                          "JPL states no accuracy for %s's position" % o['name']):
                    if w in flat:
                        findings.append(('SMALL BODY SAID TO HAVE NO FIGURE',
                                         '%s from %s says "%s"' % (o['name'], centre, w)))
            m = _find(lines, r'Distance: ([-\d,.]+) kilometers$')
            if not m or '.' in m.group(1):
                findings.append(('FINER THAN THE FLOOR', '%s from %s: km line %s'
                                 % (o['name'], centre, m.group(1) if m else 'missing')))


def check_odd_inputs(findings, counts):
    """A speed of 'N/A' or not-a-number prints N/A with no speed sentence,
    and a distance of zero does not divide by it."""
    cases = [('Mercury', 'Sun', dict(_od(0.39, 47.0), velocity='N/A')),
             ('Mercury', 'Sun', dict(_od(0.39, 47.0), velocity=float('nan'))),
             ('Encke', 'Sun', dict(_od(0.0, 33.0), position_uncertainty={
                 'range_3sigma_km': 1012.0, 'speed_3sigma_km_s': None}))]
    for name, centre, od in cases:
        counts['odd'] += 1
        try:
            lines = _hover(name, centre, od)
        except Exception as ex:
            findings.append(('CRASH', '%s from %s, velocity %r: %s'
                             % (name, centre, od['velocity'], ex)))
            continue
        if not isinstance(od['velocity'], (int, float)) or od['velocity'] != od['velocity']:
            if 'Velocity: N/A AU/day' not in lines:
                findings.append(('WRONG SPEED DIGITS', '%s: speed not N/A' % name))
            if any('speed' in ln for ln in lines if not ln.startswith('Velocity')
                   and 'Orbital' not in ln):
                findings.append(('FALSE OR MISSING WORDS', '%s: a speed sentence with no speed'
                                 % name))


# The period sentence's database clause (Tony's look, 2026-10-12): a
# planet or a moon is not in JPL's small-body database and the hover does
# not mention it; an asteroid or comet whose lookup gave no uncertainty
# says why. (status saved by build_period_record, expect the clause)
PERIOD_CASES = [
    ('not a small body; SBDB not asked', False),
    ('open orbit; SBDB not asked', False),
    (None, False),
    ('SBDB not reached (ConnectionError)', True),
    ('SBDB gives no sigma for the period', True),
    ("SBDB has no entry for '2026 XY1'", True),
]


def check_period_sentence(findings, counts):
    for status, want in PERIOD_CASES:
        rec = {'days': 87.9691, 'error_days': 0.001, 'error_from': 'year_change',
               'sbdb_sigma_days': None, 'sbdb_status': status, 'fetched': '2026-10-12'}
        text = orbital_period.period_hover_lines(
            {'kind': 'fetched', 'days': 87.9691, 'record': rec, 'label': 'the Sun'})
        has = 'small-body database' in text
        counts['period'] = counts.get('period', 0) + 1
        if has and not want:
            findings.append(('DATABASE MENTIONED FOR A PLANET OR MOON',
                             'status %r: %s' % (status, text.replace('<br>', ' / '))))
        elif want and not has:
            findings.append(('DATABASE REASON DROPPED',
                             'status %r: %s' % (status, text.replace('<br>', ' / '))))
    # L-445: a period asked of another body says whose it is, in the hover
    # and in the parameters window; a body's own period does not.
    for label in ('the Earth-Moon center of mass', None):
        rec = {'days': 365.2514, 'error_days': 0.0039, 'error_from': 'year_change',
               'sbdb_sigma_days': None, 'sbdb_status': 'not a small body; SBDB not asked',
               'fetched': '2026-10-15', 'target': '3' if label else '399',
               'target_label': label}
        resolved = {'kind': 'fetched', 'days': 365.2514, 'record': rec, 'label': 'the Sun'}
        hover = orbital_period.period_hover_lines(resolved)
        panel = orbital_period.period_panel_text(resolved)
        counts['period'] = counts.get('period', 0) + 2
        if label:
            if ('<br>For %s, around the Sun, from JPL Horizons' % label) not in hover \
                    or ('for %s, around the Sun' % label) not in panel:
                findings.append(('TARGET WORDS DROPPED',
                                 'a period asked of %s: %s | %s'
                                 % (label, hover.replace('<br>', ' / '), panel)))
        elif 'For ' in hover or ' for ' in panel:
            findings.append(('TARGET WORDS FOR THE BODY ITSELF',
                             "a body's own period: %s | %s"
                             % (hover.replace('<br>', ' / '), panel)))
        for line in hover.split('<br>'):
            if len(line) >= 98:
                findings.append(('PERIOD LINE TOO WIDE', '%d characters: %s'
                                 % (len(line), line)))


def run_checks(sky_source=None, orrery_source=None):
    findings = []
    counts = {'hovers': 0, 'lines': 0, 'answers': 0, 'pairs': 0, 'sweep': 0, 'odd': 0,
              'period': 0}
    for fx in FIXTURES:
        judge_fixture(fx, findings, counts)
    check_period_sentence(findings, counts)
    check_odd_inputs(findings, counts)
    check_symmetry(findings, counts)
    check_every_object(findings, counts)
    check_2xr_reading(findings, counts)
    scan_sources(findings, sky_source, orrery_source)
    return findings, counts


# ============================================================================
# THE PLANTED FAULTS
# ============================================================================

@contextmanager
def _patched(module, attr, value):
    old = getattr(module, attr)
    setattr(module, attr, value)
    try:
        yield
    finally:
        setattr(module, attr, old)


@contextmanager
def _row_finer():
    rv = dict(pa.ROW_VALUES)
    rv['DE430_JUPITER_SATURN_POSITION_PLACE_KM'] = rv['DE430_JUPITER_SATURN_POSITION_PLACE_KM'] / 10
    with _patched(pa, 'ROW_VALUES', rv):
        yield


@contextmanager
def _sigma_invented():
    real = pa._side

    def side(name, role, center_name, obj_data, objects, pp):
        s = real(name, role, center_name, obj_data, objects, pp)
        if s.get('reason') == 'not_fetched':
            return {'kind': 'computed', 'name': name, 'err_km': 1e-6,
                    'speed_err_km_s': 1e-9, 'who': name}
        return s
    with _patched(pa, '_side', side):
        yield


@contextmanager
def _floor_meters():
    with _patched(pa, 'DISTANCE_FLOOR_EXPONENT_KM', -3):
        yield


@contextmanager
def _line_dropped():
    real = pa.distance_speed_lines

    def lines(*a, **k):
        return [ln for ln in real(*a, **k) if 'light-' not in ln]
    with _patched(pa, 'distance_speed_lines', lines):
        yield


@contextmanager
def _typed_sky():
    real = celestial_coordinates.get_precision_note

    def note(obj_data, obj_name=None):
        got = real(obj_data, obj_name)
        return got if got else '+/-0.005 arcsec'
    with _patched(celestial_coordinates, 'get_precision_note', note):
        yield


@contextmanager
def _speed_finer():
    real = pa.speed_error_km_s

    def err(acc, distance_km, speed_km_s):
        e, why = real(acc, distance_km, speed_km_s)
        return e / 1000.0, why
    with _patched(pa, 'speed_error_km_s', err):
        yield


@contextmanager
def _read_by_position():
    """A parser that reads the 2xr columns at their recorded positions."""
    names = [x.strip() for x in RECORDED_2XR_HEADER.split(',')]
    at = {n: i for i, n in enumerate(names)}

    def parse(text):
        lines = text.split('\n')
        i = next(k for k, ln in enumerate(lines) if '$$SOE' in ln)
        toks = lines[i + 1].split(',')
        return [{n: pa._num(toks[at[n]]) for n in ('X', 'Y', 'Z', 'VX', 'VY', 'VZ',
                                                   'R_s', 'VR_s', 'VT_s', 'VN_s')}]
    with _patched(pa, 'parse_vectors_2xr', parse):
        yield


@contextmanager
def _body_none_ignores_centre():
    real = pa.resolve_accuracy

    def resolve(name, centre, od, objects, pp):
        acc = real(name, centre, od, objects, pp)
        b = pa._side(name, 'body', centre, od, objects, pp)
        if b['kind'] == 'none' and acc['state'] == 'floor':
            return {'state': 'none', 'err_km': None, 'reason': b['reason'], 'gap': b['gap']}
        return acc
    with _patched(pa, 'resolve_accuracy', resolve):
        yield


@contextmanager
def _surface_dropped_for_giants():
    """Build 1's first form: no surface line for the Sun or a giant planet."""
    real = pa.distance_speed_lines
    giants = {'Sun', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Planet 9'}

    def lines(acc, distance_au, speed_au_per_day, center_name, center_radius_km):
        out = real(acc, distance_au, speed_au_per_day, center_name, center_radius_km)
        if center_name in giants:
            out = [ln for ln in out if not ln.startswith('Distance to Center Surface')]
        return out
    with _patched(pa, 'distance_speed_lines', lines):
        yield


@contextmanager
def _database_for_planets():
    """Build 1's first form: every body told about the small-body database."""
    with _patched(orbital_period, '_sbdb_asked', lambda status: True):
        yield


@contextmanager
def _target_words_dropped():
    """L-445: Earth's period printed with no word of whose it is."""
    with _patched(orbital_period, 'target_words', lambda rec: ''):
        yield


@contextmanager
def _sheet_ignored():
    with _patched(pa, 'SPACECRAFT_SHEET_ROWS', {}):
        yield


@contextmanager
def _zero_sigma_kept():
    def finite(x):
        try:
            return float(x)
        except (TypeError, ValueError):
            return None
    with _patched(pa, '_finite_positive', finite):
        yield


@contextmanager
def _jpl_none_called_not_fetched():
    # The code before 2026-10-29: JPL's "n.a." said as not included here.
    real = pa._side

    def side(name, role, center_name, obj_data, objects, pp):
        s = real(name, role, center_name, obj_data, objects, pp)
        if s.get('reason') == 'unstated' and role == 'body' and isinstance(
                (obj_data or {}).get('position_uncertainty'), dict):
            return pa._none_side(name, 'not_fetched')
        return s
    with _patched(pa, '_side', side):
        yield


@contextmanager
def _failed_called_jpl_none():
    # The brief's first sketch: any record present, failed or not, read as
    # JPL stating none.
    real = pa._side

    def side(name, role, center_name, obj_data, objects, pp):
        s = real(name, role, center_name, obj_data, objects, pp)
        pu = (obj_data or {}).get('position_uncertainty') if role == 'body' else None
        if s.get('reason') == 'not_fetched' and isinstance(pu, dict) and pu.get('missing'):
            return pa._none_side(name, 'unstated')
        return s
    with _patched(pa, '_side', side):
        yield


def _sky_source_with_table():
    with open(os.path.join(HERE, 'celestial_coordinates.py'), encoding='utf-8') as f:
        src = f.read()
    return src + "\nMAJOR_BODY_UNCERTAINTIES = {'Mercury': 0.005}\n"


def _orrery_source_without_2xr():
    with open(os.path.join(HERE, 'palomas_orrery.py'), encoding='utf-8') as f:
        src = f.read()
    return src.replace('fetch_small_body_state(', 'fetch_small_body_state_REMOVED(')


PLANTS = [
    ("Jupiter's row read ten times finer", _row_finer, {}, 'PLANET FINER THAN ITS ROW'),
    ('a missing sigma turned into a tiny one', _sigma_invented, {},
     'SMALL BODY WITHOUT SIGMA NOT IN THE NO-ERROR STATE'),
    ('the kilometer floor moved to meters', _floor_meters, {},
     'NO-ERROR BODY FINER THAN THE FLOOR'),
    ('the light-time line left out', _line_dropped, {}, 'LINE DROPPED'),
    ('a typed sky value put back', _typed_sky,
     {'sky_source': 'table'}, 'TYPED SKY VALUE'),
    ("the speed's error divided by a thousand", _speed_finer, {},
     'SPEED FINER THAN ITS DISTANCE'),
    ("fetch_position's 2xr call removed", None, {'orrery_source': 'no2xr'}, 'DISPATCH'),
    ('the 2xr columns read by position', _read_by_position, {}, '2XR READ BY POSITION'),
    ("a no-error body ignoring its centre's error", _body_none_ignores_centre, {},
     'NO-ERROR BODY IGNORES ITS CENTRE'),
    ('a zero sigma taken as a figure', _zero_sigma_kept, {}, 'ZERO SIGMA TAKEN AS A FIGURE'),
    ("the Voyagers' data-sheet figures dropped", _sheet_ignored, {},
     'SPACECRAFT DATA-SHEET FIGURE IGNORED'),
    ('the surface line dropped for a giant planet', _surface_dropped_for_giants, {},
     'SURFACE LINE DROPPED'),
    ('the small-body database named for a planet', _database_for_planets, {},
     'DATABASE MENTIONED FOR A PLANET OR MOON'),
    ("a period asked of another body printed as the body's own", _target_words_dropped, {},
     'TARGET WORDS DROPPED'),
    ('JPL\'s "n.a." said as not included', _jpl_none_called_not_fetched, {},
     "JPL'S NONE SAID AS NOT INCLUDED"),
    ('a failed question said as JPL stating none', _failed_called_jpl_none, {},
     'A FAILED QUESTION SAID AS JPL STATING NONE'),
]


def main():
    problems = []
    for label, ctx, sources, expected in PLANTS:
        kw = {}
        if sources.get('sky_source') == 'table':
            kw['sky_source'] = _sky_source_with_table()
        if sources.get('orrery_source') == 'no2xr':
            kw['orrery_source'] = _orrery_source_without_2xr()
        if ctx is None:
            findings, _ = run_checks(**kw)
        else:
            with ctx():
                findings, _ = run_checks(**kw)
        hits = [d for c, d in findings if c == expected]
        if hits:
            print('planted: %-42s caught as %s (%s)' % (label, expected, hits[0]))
        else:
            print('planted: %-42s NOT CAUGHT; findings: %s'
                  % (label, sorted(set(c for c, _ in findings)) or 'none'))
            problems.append('planted fault not caught: %s' % label)

    findings, counts = run_checks()
    for cls, detail in findings:
        print('FAIL: %s -- %s' % (cls, detail))
        problems.append('%s -- %s' % (cls, detail))
    rows = sorted(set(fx[4][1] for fx in FIXTURES if fx[4][0] == 'row'))
    sigmas = ['%s from %s' % (fx[0], fx[1]) for fx in FIXTURES if fx[4][0] == 'sigma']
    print('compared: every distance line (AU, kilometers, light time, surface) and '
          'every speed line (AU/day, km/hr, km/sec), against errors worked out here from '
          '%s; the fixture 3-sigma figures for %s; and the stated floors (whole kilometers, '
          'one meter per second); plus the sky-position note, celestial_coordinates.py '
          'and the dispatch in palomas_orrery.py' % (', '.join(rows), ', '.join(sigmas)))
    print('examined: %s' % ', '.join(
        '%s from %s%s' % (fx[0], fx[1], ' (its 2xr missing)'
                          if fx[2].get('position_uncertainty', {}).get('missing') else '')
        for fx in FIXTURES))
    if problems:
        print('POSITION DIGITS: FAIL -- %d problem(s)' % len(problems))
        return 1
    print('POSITION DIGITS: PASS -- %d of %d planted faults caught by name; %d hovers '
          'examined, %d lines compared against their errors; %d pairs printed the same '
          'from either end; %d hovers of every listed object from the Sun, Earth and '
          'Neptune; %d recorded 2xr answers read by column name; %d period sentences'
          % (len(PLANTS), len(PLANTS), counts['hovers'], counts['lines'], counts['pairs'],
             counts['sweep'], counts['answers'], counts['period']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
