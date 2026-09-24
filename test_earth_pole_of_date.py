"""
test_earth_pole_of_date.py - offline checks of Earth's pole and tilt of date.

WHAT THIS CHECKS, and what it cannot

    It never contacts Horizons. It checks the geometry, the fallback, the
    cache and the hover words of earth_pole_of_date.py, and that the
    orrery's pole transform really uses the pole of date for Earth. Whether
    Horizons returns what the module expects is checked by
    earth_pole_live_check.py, which does fetch.

    1. The worked case in the build manifest (rev 3, section 0): the
       fetched pole of 2026-Jan-01, 0.71450 / 89.85464, against the orbit
       the cache served on 2026-09-23, gives 23.43598 degrees.
    2. The geometry against ERFA, the IAU's SOFA routines as astropy ships
       them (pyerfa). For three dates, ERFA's own true pole of date
       (eraPnm06a) and its ecliptic of date (eraEcm06) are fed through this
       module's conversions, and the tilt must equal ERFA's true obliquity
       of date, the IAU 2006 mean obliquity (eraObl06) plus the nutation in
       obliquity (eraNut06a), to 0.001 arcseconds. This tests the code's
       geometry with an independent implementation of the same physics; it
       is not a test of Horizons.
    3. With a fetch that fails, the drawn pole is the fallback pair in
       constants_new.py, no tilt is given, and the reason is recorded.
    4. A fetched date is written to the cache and read back without a
       second fetch.
    5. The hover line prints the tilt at seven figures with its date, and
       on fallback says why no tilt is shown.
    6. create_planet_transformation_matrix('Earth') in idealized_orbits.py
       draws the pole of the scene's date, and the frame's axis when there
       is none.

RUN COMMAND

    Open in VS Code and click Run. The orrery maintenance run also runs it,
    as "Earth pole of date".

Role: test
Domain: orrery

Module created: September 23, 2026 with Anthropic's Claude Opus 5.5
(L-322 Stage D, patch D3)
"""

import math
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import earth_pole_of_date as epd                     # noqa: E402
from constants_new import (                           # noqa: E402
    EARTH_POLE_RA_J2000_DEG, EARTH_POLE_DEC_J2000_DEG)

RESULTS = []


def check(name, ok, detail):
    RESULTS.append((name, ok, detail))
    print('  %-4s %-44s %s' % ('ok' if ok else 'FAIL', name, detail))


def test_worked_case():
    got = epd.tilt_of_date_deg(0.71450, 89.85464,
                               0.005556904467098324, 176.69335175006)
    want = 23.43598
    check('worked case (manifest rev 3 section 0)',
          abs(got - want) < 0.5e-5,
          'computed %.8f deg, manifest reports %.5f' % (got, want))


def _erfa_inputs(jd):
    import erfa
    cip = erfa.pnm06a(jd, 0.0)[2]
    ecl = erfa.ecm06(jd, 0.0)[2]
    ra = math.degrees(math.atan2(cip[1], cip[0])) % 360.0
    dec = math.degrees(math.asin(cip[2]))
    n = epd.icrf_to_ecliptic_j2000(tuple(float(v) for v in ecl))
    incl = math.degrees(math.acos(n[2]))
    node = math.degrees(math.atan2(n[0], -n[1])) % 360.0
    _dpsi, deps = erfa.nut06a(jd, 0.0)
    true_obl = math.degrees(erfa.obl06(jd, 0.0) + deps)
    return ra, dec, incl, node, true_obl


def test_against_erfa():
    try:
        import erfa                                    # noqa: F401
    except ImportError:
        check('geometry against ERFA', False,
              'pyerfa is not installed, so this check could not run')
        return
    for label, jd in (('2000-01-01.5', 2451545.0),
                      ('2026-09-23', 2461306.5),
                      ('2100-01-01', 2488070.0)):
        ra, dec, incl, node, want = _erfa_inputs(jd)
        got = epd.tilt_of_date_deg(ra, dec, incl, node)
        diff = abs(got - want) * 3600.0
        check('geometry against ERFA, %s' % label, diff < 0.001,
              'tilt %.9f, ERFA true obliquity %.9f, differ %.2g arcsec'
              % (got, want, diff))


def _fake_ok(calls):
    def pole(jd):
        calls.append(('pole', jd))
        return 0.71450, 89.85464

    def orbit(jd):
        calls.append(('orbit', jd))
        return 0.005556904467098324, 176.69335175006
    return pole, orbit


def _fail(jd):
    raise RuntimeError('no network in this test')


def test_fallback_and_cache(tmp):
    from datetime import datetime
    day = datetime(2026, 1, 1)
    path = os.path.join(tmp, 'cache.json')
    got = epd.resolve(day, cache_path=path, fetch_pole_fn=_fail,
                      fetch_orbit_fn=_fail)
    check('fallback draws the frame axis',
          got['status'] == 'fallback'
          and got['ra_deg'] == EARTH_POLE_RA_J2000_DEG
          and got['dec_deg'] == EARTH_POLE_DEC_J2000_DEG
          and got['tilt_deg'] is None,
          'status %s, pole %s / %s, tilt %s'
          % (got['status'], got['ra_deg'], got['dec_deg'], got['tilt_deg']))
    check('fallback records why', got['reason'] == 'Horizons could not be '
          'reached', 'reason: %r' % got['reason'])
    check('fallback writes no cache', not os.path.exists(path),
          'cache file present: %s' % os.path.exists(path))
    calls = []
    pole, orbit = _fake_ok(calls)
    got = epd.resolve(day, cache_path=path, fetch_pole_fn=pole,
                      fetch_orbit_fn=orbit)
    check('first fetch is fetched and cached',
          got['status'] == 'fetched' and os.path.exists(path)
          and len(calls) == 2,
          'status %s, %d fetch call(s), cache written: %s'
          % (got['status'], len(calls), os.path.exists(path)))
    again = epd.resolve(day, cache_path=path, fetch_pole_fn=_fail,
                        fetch_orbit_fn=_fail)
    check('second read comes from the cache',
          again['status'] == 'cached' and again['tilt_deg'] == got['tilt_deg'],
          'status %s, tilt %s' % (again['status'], again['tilt_deg']))
    check('cache keeps both source blocks',
          (again['pole_source'] or {}).get('query_target') == '399'
          and (again['orbit_source'] or {}).get('query_target') == '3',
          'pole target %s, orbit target %s'
          % ((again['pole_source'] or {}).get('query_target'),
             (again['orbit_source'] or {}).get('query_target')))


def test_hover_and_transform():
    from datetime import datetime
    import idealized_orbits
    saved = dict(epd._memo), epd._scene['date']
    try:
        fetched = {'ra_deg': 0.71450, 'dec_deg': 89.85464,
                   'tilt_deg': 23.435979372358, 'day': '2026-01-01',
                   'status': 'fetched', 'reason': None,
                   'pole_source': None, 'orbit_source': None}
        epd.set_scene_date(datetime(2026, 1, 1))
        epd._memo.clear()
        epd._memo['2026-01-01'] = fetched
        text = epd.tilt_hover_text()
        check('hover prints the tilt at seven figures with its date',
              text.startswith('23.43598 deg on 2026-01-01'), text[:48])
        m = idealized_orbits.create_planet_transformation_matrix('Earth')
        want = epd.icrf_to_ecliptic_j2000(epd.unit_from_ra_dec(0.71450,
                                                               89.85464))
        col = [float(m[k][2]) for k in range(3)]
        err = max(abs(a - b) for a, b in zip(col, want))
        check('the Earth transform draws the pole of date', err < 1e-12,
              'largest difference %.2g' % err)
        epd.set_scene_date(None)
        epd._memo.clear()
        text = epd.tilt_hover_text()
        check('hover on fallback says why',
              text.startswith('not shown: no plot date was given'), text[:48])
        m = idealized_orbits.create_planet_transformation_matrix('Earth')
        want = epd.icrf_to_ecliptic_j2000(epd.unit_from_ra_dec(
            EARTH_POLE_RA_J2000_DEG, EARTH_POLE_DEC_J2000_DEG))
        col = [float(m[k][2]) for k in range(3)]
        err = max(abs(a - b) for a, b in zip(col, want))
        check('with no date the Earth transform draws the frame axis',
              err < 1e-12, 'largest difference %.2g' % err)
    finally:
        epd._memo.clear()
        epd._memo.update(saved[0])
        epd._scene['date'] = saved[1]


def main():
    print('=' * 70)
    print('EARTH POLE OF DATE -- offline checks (no Horizons contact)')
    print('=' * 70)
    tmp = tempfile.mkdtemp(prefix='earth_pole_test_')
    try:
        test_worked_case()
        test_against_erfa()
        test_fallback_and_cache(tmp)
        test_hover_and_transform()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    failed = [name for name, ok, _d in RESULTS if not ok]
    print('')
    if failed:
        print('EARTH POLE OF DATE: %d of %d checks FAILED: %s'
              % (len(failed), len(RESULTS), ', '.join(failed)))
        return 1
    print('EARTH POLE OF DATE: all %d checks passed (geometry, ERFA, '
          'fallback, cache, hover, transform).' % len(RESULTS))
    return 0


if __name__ == '__main__':
    sys.exit(main())
