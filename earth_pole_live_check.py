"""
earth_pole_live_check.py - fetch Earth's pole and orbit from Horizons and
check the tilt of date against an independent calculation.

WHY THIS EXISTS

    test_earth_pole_of_date.py never contacts Horizons, so it cannot show
    that Horizons answers the two queries the way earth_pole_of_date.py
    expects. This script does contact it, and it is the first live test of
    those queries. It writes nothing: no cache, no file.

WHAT IT PRINTS

    For five dates (2000-01-01, the first of this month, today, 2050-01-01
    and 2100-01-01):
      - the pole Horizons returns (quantity 32, target 399);
      - the tilt against the Earth-Moon barycenter's orbit (target 3), the
        value the orrery prints;
      - the true obliquity of the same date from ERFA (the SOFA routines
        astropy ships), which includes Earth's nod as the fetched pole
        does, and how far the tilt is from it, in arcseconds. Each date
        reports PASS or FAIL on that difference.
      - the IAU 2006 mean obliquity, the smoothed textbook value, for
        information only. It differs from the tilt by Earth's nod on the
        day (8.46 arcseconds on 2026-09-24), so it cannot be a tight test.
    Patch D3 tested against the mean with a 10-arcsecond allowance; on
    2026-09-24 today's nod used 8.46 of it, so a pass said little. Patch
    D4 tests against the true value instead (Tony, 2026-09-23).

    Then, for eight dates a few days apart across one month, the tilt
    measured against Earth's own orbit (target 399) beside the tilt
    against the barycenter's. The spread of the difference is the monthly
    wobble the manifest estimated at about 8 arcseconds from recalled
    round figures; this replaces that estimate with a measured number.

RUN COMMAND

    Open this file in VS Code and click Run. It needs an internet
    connection and takes a minute or two, because it asks Horizons about
    thirty questions. If a query fails, it says which one and carries on.

Role: diagnostic
Domain: orrery

Module created: September 23, 2026 with Anthropic's Claude Opus 5.5
(L-322 Stage D, patch D3)
Module updated: September 23, 2026 with Anthropic's Claude Opus 5.5
(L-322 Stage D, patch D4: PASS and FAIL judged against ERFA's true
obliquity with a 1-arcsecond allowance, where D3 judged against the
mean with 10; the mean is still printed)
"""

import math
import sys
from datetime import datetime, timedelta, timezone

import earth_pole_of_date as epd

# Source: declared 2026-09-23, L-322 Stage D patch D4 -- a test allowance,
# not a measurement. Tony's live run of 2026-09-24 put the fetched tilt
# within 0.25 arcseconds of ERFA's true obliquity on all five dates, 2000
# to 2100. What is left comes from two known differences: Horizons uses
# the IAU 1976/1980 precession and nutation (Horizons manual, Reference
# Frames), ERFA the IAU 2006/2000A models; and the barycenter's
# osculating orbit plane is not quite the mean ecliptic. One arcsecond is
# four times the largest difference seen, and an eighth of the 8.46
# arcseconds of nod the same run measured on 2026-09-24, so a pass
# means the tilt tracks the nod.
ALLOWANCE_ARCSEC = 1.0


def _earth_orbit(jd):
    from astroquery.jplhorizons import Horizons
    table = Horizons(id='399', location='@sun', epochs=jd).elements(
        refplane='ecliptic')
    return float(table['incl'][0]), float(table['Omega'][0])


def _erfa(jd):
    import erfa
    mean = math.degrees(erfa.obl06(jd, 0.0))
    _dpsi, deps = erfa.nut06a(jd, 0.0)
    return mean, mean + math.degrees(deps)


def main():
    today = datetime.now(timezone.utc).replace(tzinfo=None)
    dates = [datetime(2000, 1, 1), datetime(today.year, today.month, 1),
             datetime(today.year, today.month, today.day),
             datetime(2050, 1, 1), datetime(2100, 1, 1)]
    print('=' * 70)
    print('EARTH POLE LIVE CHECK -- JPL Horizons, compared with ERFA')
    print('=' * 70)
    failures = 0
    for d in dates:
        jd = epd._julian_day_0h(d)
        try:
            ra, dec = epd.fetch_pole(jd)
            incl, node = epd.fetch_orbit(jd)
        except Exception as exc:                          # noqa: BLE001
            print('%s  FETCH FAILED: %s' % (d.date(), exc))
            failures += 1
            continue
        tilt = epd.tilt_of_date_deg(ra, dec, incl, node)
        mean, true = _erfa(jd)
        d_mean = (tilt - mean) * 3600.0
        d_true = (tilt - true) * 3600.0
        ok = abs(d_true) <= ALLOWANCE_ARCSEC
        failures += 0 if ok else 1
        print('%s  pole %.5f / %.5f   tilt %.7f deg' % (d.date(), ra, dec,
                                                         tilt))
        print('            ERFA true %.7f (tilt minus true %+.2f arcsec, %s)'
              % (true, d_true, 'PASS' if ok else 'FAIL'))
        print('            ERFA mean %.7f (tilt minus mean %+.2f arcsec, '
              'information only: the difference is Earth\'s nod)'
              % (mean, d_mean))
    print('')
    print('Monthly wobble: tilt against Earth\'s own orbit minus tilt '
          'against the barycenter\'s')
    start = datetime(today.year, today.month, 1)
    diffs = []
    for k in range(8):
        d = start + timedelta(days=4 * k)
        jd = epd._julian_day_0h(d)
        try:
            ra, dec = epd.fetch_pole(jd)
            bi, bn = epd.fetch_orbit(jd)
            ei, en = _earth_orbit(jd)
        except Exception as exc:                          # noqa: BLE001
            print('  %s  FETCH FAILED: %s' % (d.date(), exc))
            continue
        diff = (epd.tilt_of_date_deg(ra, dec, ei, en)
                - epd.tilt_of_date_deg(ra, dec, bi, bn)) * 3600.0
        diffs.append(diff)
        print('  %s  %+.2f arcsec' % (d.date(), diff))
    if diffs:
        print('  spread over the month: %.2f arcsec (largest minus smallest)'
              % (max(diffs) - min(diffs)))
    print('')
    if failures:
        print('EARTH POLE LIVE CHECK: %d date(s) FAILED or could not be '
              'fetched. Copy this whole output into the chat.' % failures)
        return 1
    print('EARTH POLE LIVE CHECK: every date within %.0f arcsecond of '
          'ERFA\'s true obliquity. Copy this whole output into the chat.'
          % ALLOWANCE_ARCSEC)
    return 0


if __name__ == '__main__':
    sys.exit(main())
