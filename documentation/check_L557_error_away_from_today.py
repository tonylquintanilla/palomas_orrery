"""check_L557_error_away_from_today.py -- is a box's error away from today right?

L-557 (the error away from today). A record of a test, not a nightly check.
Written November 25, 2026 with Anthropic's Claude Fable 5.2, in the
coordinating session that held the talk on L-556 (a date to choose in the
rooms). First run on gallery b2d9eaa66ed33ec93fc2bbcbdc5b85d5b872e043.

WHAT IT ASKS. The website prints a Sun-centred body's distance to the digits
its drift allows: drift = distance x error_rate_deg_per_day x days from the
orbit's date (distanceLine, gallery/solar_system_figures.js). The rate is the
night's one measurement: the miss at delta_days = min(period / 8, 30) either
side of the orbit's date, divided by delta_days (measure_trust,
tools/gallery_cache_builder.py). So away from today the box rests on a
straight line. This test holds that line to what really happened.

HOW. The website's repository keeps every night's served orbits in the
history of data/solar-system/coverage_index.json. For each earlier night:
take that night's orbit for a body, work out by two-body motion where it puts
the body at TONIGHT's orbit date, and compare with tonight's orbit at its own
date, which is JPL's place for that date. The angle between the two, seen
from the Sun, is the real miss; the old night's rate times the days between
is what a box would have claimed.

WHAT TELLS US IT WORKS. At a body's own delta_days the real miss must equal
the night's own sample, since it is the same question asked of JPL. The run
prints that comparison first and exits 1 if no body reproduces it.

WHAT IT CANNOT JUDGE. A comet with e close to 1: the simple solver here is
not built for it, and JPL may revise such an orbit between nights. Those are
named in the output and left out of the counts.

RUN. From the website's folder, which must hold its full history:
    python <path to this file>            every Sun-centred body
    python <path to this file> earth      named bodies only
It reads git history only. It writes nothing and asks JPL nothing.
"""
import json
import math
import subprocess
import sys

F = 'data/solar-system/coverage_index.json'
AU_KM = 149597870.7      # only to print kilometres; the test is on angles
NEAR_PARABOLA = 0.98     # e above this: not judged, and named


def load(rev):
    return json.loads(subprocess.check_output(
        ['git', 'show', '%s:%s' % (rev, F)], stderr=subprocess.DEVNULL))


def objects(index):
    o = index.get('objects') or {}
    return o if isinstance(o, dict) else dict((x.get('slug'), x) for x in o)


def place(osc, t_jd):
    a, e = osc['a_au'], osc['e']
    i, node, peri = (math.radians(osc[k])
                     for k in ('i_deg', 'node_deg', 'peri_deg'))
    m = math.radians(osc['M0_deg']
                     + osc['n_deg_per_day'] * (t_jd - osc['epoch_jd']))
    big_e = m
    for _ in range(80):
        big_e -= (big_e - e * math.sin(big_e) - m) / (1 - e * math.cos(big_e))
    xp = a * (math.cos(big_e) - e)
    yp = a * math.sqrt(1 - e * e) * math.sin(big_e)
    co, so = math.cos(node), math.sin(node)
    cw, sw = math.cos(peri), math.sin(peri)
    ci, si = math.cos(i), math.sin(i)
    return ((co * cw - so * sw * ci) * xp + (-co * sw - so * cw * ci) * yp,
            (so * cw + co * sw * ci) * xp + (-so * sw + co * cw * ci) * yp,
            (sw * si) * xp + (cw * si) * yp)


def angle_deg(u, v):
    dot = sum(p * q for p, q in zip(u, v))
    cr = (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2],
          u[0] * v[1] - u[1] * v[0])
    return math.degrees(math.atan2(math.sqrt(sum(c * c for c in cr)), dot))


def usable(o):
    t = (o or {}).get('trust') or {}
    osc = (o or {}).get('osculating') or {}
    return (o is not None and o.get('canonical_frame') == 'heliocentric'
            and t.get('error_rate_deg_per_day') and t.get('delta_days')
            and osc.get('n_deg_per_day') and osc.get('e') is not None)


def main():
    asked = sys.argv[1:]
    head = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode().strip()
    now = objects(load('HEAD'))
    slugs = sorted(s for s, o in now.items() if usable(o)
                   and (not asked or s in asked))
    not_judged = sorted(s for s in slugs
                        if now[s]['osculating']['e'] > NEAR_PARABOLA)
    slugs = [s for s in slugs if s not in not_judged]
    log = subprocess.check_output(
        ['git', 'log', '--format=%H %ad', '--date=short', '--', F]).decode()
    nights, seen = [], set()
    for line in log.split('\n'):
        if line and line.split()[1] not in seen:
            seen.add(line.split()[1])
            nights.append(line.split())
    rows = dict((s, []) for s in slugs)
    for sha, _day in nights:
        try:
            old = objects(load(sha))
        except Exception:
            continue
        for s in slugs:
            o = old.get(s)
            if not usable(o) or o['osculating']['e'] > NEAR_PARABOLA:
                continue
            t = now[s]['osculating']['epoch_jd']
            days = t - o['osculating']['epoch_jd']
            if days < 1:
                continue
            truth = place(now[s]['osculating'], t)
            real = angle_deg(truth, place(o['osculating'], t))
            line_deg = o['trust']['error_rate_deg_per_day'] * days
            km = math.radians(1) * math.sqrt(sum(c * c for c in truth)) * AU_KM
            rows[s].append({'days': days, 'real_km': real * km,
                            'line_km': line_deg * km,
                            'ratio': real / line_deg if line_deg else 0.0,
                            'tested': o['trust']['delta_days']})
    compared = sum(len(v) for v in rows.values())
    print('website at %s' % head)
    print('nights in the history: %d (%s to %s) | bodies examined: %d | '
          'comparisons: %d' % (len(nights), nights[-1][1], nights[0][1],
                               len(slugs), compared))
    print('not judged, e above %.2f (%d): %s'
          % (NEAR_PARABOLA, len(not_judged), ', '.join(not_judged) or 'none'))
    empty = sorted(s for s in slugs if not rows[s])
    print('no earlier night to compare (%d): %s'
          % (len(empty), ', '.join(empty) or 'none'))

    # 1. The test's own proof: at the tested distance it must agree.
    print('\n1. AT ITS OWN TESTED DISTANCE (real miss / the line; 1.00 is '
          'agreement)')
    proved = 0
    for s in slugs:
        at = [r for r in rows[s] if abs(r['days'] - r['tested']) <= 0.75]
        if at:
            r = at[0]
            ok = 0.9 <= r['ratio'] <= 1.1
            proved += ok
            if asked or s in ('mercury', 'venus', 'earth', 'mars', 'jupiter',
                              'saturn', 'uranus', 'neptune'):
                print('  %-10s %5.1f days: real %10.1f km, line %10.1f km '
                      '(%.2f)' % (s, r['days'], r['real_km'], r['line_km'],
                                  r['ratio']))
    print('  bodies within 10%% of agreement there: %d' % proved)

    def worst(band):
        out = []
        for s in slugs:
            rs = [r for r in rows[s] if band(r)]
            if rs:
                w = max(rs, key=lambda r: r['ratio'])
                out.append((w['ratio'], s, w, len(rs)))
        return sorted(out, reverse=True)

    def table(title, band, show_all=False):
        res = worst(band)
        over = [x for x in res if x[0] > 1.05]
        print('\n%s' % title)
        print('  bodies with a night in this band: %d | real miss over the '
              'line by more than 5%%: %d' % (len(res), len(over)))
        for ratio, s, w, n in (res if show_all else over):
            print('  %-20s tested to %4.1f d | worst at %5.0f d: real '
                  '%10.0f km, line %10.0f km (x%.1f) | %d nights'
                  % (s, w['tested'], w['days'], w['real_km'], w['line_km'],
                     ratio, n))

    table('2. INSIDE ITS TESTED DISTANCE',
          lambda r: r['days'] <= r['tested'] + 0.5)
    table('3. PAST ITS TESTED DISTANCE, TO 30 DAYS',
          lambda r: r['tested'] + 0.5 < r['days'] <= 30.5)
    table('4. FROM 30 TO 88 DAYS', lambda r: 30.5 < r['days'] <= 88.5)
    table('5. PAST 88 DAYS (every body with a night this far back)',
          lambda r: r['days'] > 88.5, show_all=True)
    sys.exit(0 if proved else 1)


if __name__ == '__main__':
    main()
