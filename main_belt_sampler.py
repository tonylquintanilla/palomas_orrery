"""
main_belt_sampler.py - the main asteroid belt as a cloud of dots placed
at random inside the belt's spread, measured from JPL's own orbits.

Tony's ruling of 2026-10-28 (L-443), "form B": JPL's edges for the class,
and the spread measured from its orbits; the dots placed at random inside
that spread, in distance and in height, stored once like the Hills cloud.
Not a snapshot of real asteroids on one date, "because the orrery and the
website both show any date and a snapshot is wrong on every day but one."
The hover says the cloud shows the belt's extent measured from JPL's
main-belt orbits, not individual bodies.

WHERE THE NUMBERS COME FROM (every one a row in constants_new.py):
- The class. JPL's Small-Body Database calls an asteroid MBA, a
  main-belt asteroid, when its semi-major axis lies between
  MAIN_BELT_A_INNER_AU and MAIN_BELT_A_OUTER_AU and its perihelion is
  beyond MAIN_BELT_Q_MIN_AU (JPL's "SBDB Filter Parameters" page).
- The sample. Every MBA with absolute magnitude H no fainter than
  MAIN_BELT_SAMPLE_H_MAX, as JPL's SBDB Query API returned them on
  2026-10-28: MAIN_BELT_SAMPLE_ORBITS orbits, of MAIN_BELT_JPL_COUNT MBAs
  in all. The answer is kept, unchanged, in
  documentation/worksheets/main_belt_jpl_mba_h13_20261028.json. The cut is
  a drawing choice: it keeps the cloud near the size the orrery drew
  before, and the brighter asteroids are roughly the larger ones.
- The spread. measure() follows each orbit through one whole turn,
  720 points evenly in time (measure's default), and pools the points of every
  orbit: so the spread is where these asteroids spend their time, on no
  particular date. Three tables, each at every 5th percentile and at
  every one in the first and last five (PERCENTILES):
  MAIN_BELT_DISTANCE_PERCENTILES_AU (distance from the Sun),
  MAIN_BELT_LATITUDE_PERCENTILES_DEG (angle above or below the ecliptic,
  either side) and MAIN_BELT_HEIGHT_PERCENTILES_AU (distance above or
  below the ecliptic, either side). The 0th and 100th distance are the
  nearest perihelion and the farthest aphelion among the orbits, the
  100th latitude the largest inclination, exactly.

HOW THE DOTS ARE PLACED (drawn_main_belt):
- a distance, drawn from the distance table: a share chosen evenly from
  0 to 1, and the distance at that share, in a straight line between the
  table's two percentiles either side;
- a latitude, drawn from the latitude table the same way, above or below
  the ecliptic with even chances;
- a longitude, evenly around the Sun.
Distance and latitude are drawn apart, so the drawing does not keep how
the two go together in the real orbits. The check below holds the dots'
heights to the measured height table, which is what that would upset.
The seed and the dot count are rendering settings (drawn_main_belt's
defaults), not measurements.

THE CHECKS (check_dots() and check_rows() return what fails;
test_drawings_export.py plants a fault in each before judging the file):
- the ends: every dot between the 0th and 100th distance, the drawing's
  two ends, each a row;
- the distance: in each band between two of the distance table's
  percentiles the dots hold that band's share, within four standard
  deviations or 15 percent;
- the latitude: the same, band by band, for the latitude table;
- the height: the shares of dots within the 50th and 90th height are
  50 and 90 percent, within the same tolerance;
- the rows (check_rows): the kept answer holds MAIN_BELT_SAMPLE_ORBITS
  orbits, each one an MBA by the class rows and within the H cut, and
  measuring it again gives the three tables in the store, to their
  rounding.

Coordinates are in AU, centred on the Sun, in the ecliptic and equinox of
J2000, the orrery's drawing frame (the frame of JPL's elements).

Key functions:
    measure() - the three spread tables, from the kept answer
    drawn_main_belt() - the dots as drawn, with the settings below
    check_dots() - the four dot checks above, as a list of failures
    check_rows() - the rows against the kept answer
    hover_text() - the visitor's words, every number from the rows

Run it to print the tables, the counts and the checks:
    python main_belt_sampler.py

Consumed by: asteroid_belt_visualization_shells.py
             (create_main_asteroid_belt), export_drawings.py,
             test_drawings_export.py

Role: computation
Domain: orrery

Module created: October 28, 2026 with Anthropic's Claude Opus 5.5 (L-443,
the drawn main-belt cloud, the orrery half)
"""
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
WORKSHEET = os.path.join(HERE, "documentation", "worksheets",
                         "main_belt_jpl_mba_h13_20261028.json")

# One home for the rows this drawing reads.
ROW_NAMES = (
    'MAIN_BELT_A_INNER_AU',
    'MAIN_BELT_A_OUTER_AU',
    'MAIN_BELT_Q_MIN_AU',
    'MAIN_BELT_SAMPLE_H_MAX',
    'MAIN_BELT_SAMPLE_ORBITS',
    'MAIN_BELT_JPL_COUNT',
    'MAIN_BELT_DISTANCE_PERCENTILES_AU',
    'MAIN_BELT_LATITUDE_PERCENTILES_DEG',
    'MAIN_BELT_HEIGHT_PERCENTILES_AU',
    'KM_PER_AU',
)
TABLES = ('MAIN_BELT_DISTANCE_PERCENTILES_AU',
          'MAIN_BELT_LATITUDE_PERCENTILES_DEG',
          'MAIN_BELT_HEIGHT_PERCENTILES_AU')

# The percentiles each table holds, as the store keys them: every 5th,
# and every one in the first and last five, where the spread's tails
# stretch out (the top 5 percent of distances runs from about 3.5 to
# 4.3 AU), so the straight lines between them do not overfill a tail.
PERCENTILES = (0, 1, 2, 3, 4) + tuple(range(5, 96, 5)) + (96, 97, 98, 99,
                                                           100)



def rows_from_store():
    """The rows this module reads, from constants_new.py, as a dict. A
    table stays a dict keyed by percentile, as the store writes it."""
    import constants_new
    rows = {}
    for name in ROW_NAMES:
        value = getattr(constants_new, name)
        rows[name] = (dict((str(k), float(v)) for k, v in value.items())
                      if isinstance(value, dict) else float(value))
    return rows


def _table(rows, name):
    """(shares 0..1, values) for one table, in percentile order."""
    t = rows[name]
    return (np.array([p / 100.0 for p in PERCENTILES]),
            np.array([t[str(p)] for p in PERCENTILES]))


def load_orbits(path=WORKSHEET):
    """The kept answer: (the file as read, a dict of float arrays by
    field)."""
    with open(path, "r", encoding="utf-8") as handle:
        sheet = json.load(handle)
    fields = sheet["fields"]
    cols = {}
    for k, name in enumerate(fields):
        if name == "spkid":
            continue
        cols[name] = np.array([float(row[k]) for row in sheet["data"]])
    return sheet, cols


def _kepler(m, e):
    """Eccentric anomaly for mean anomaly m (radians), Newton's method."""
    ecc = m.copy()
    for _ in range(60):
        ecc = ecc - (ecc - e * np.sin(ecc) - m) / (1.0 - e * np.cos(ecc))
    return ecc


def orbit_points(cols, steps=720):
    """(distance, height) in AU of every orbit at `steps` points evenly
    in time through one turn, each an array of orbits x steps. The node
    does not enter: neither distance nor height depends on it."""
    a = cols["a"][:, None]
    e = cols["e"][:, None]
    inc = np.radians(cols["i"])[:, None]
    peri = np.radians(cols["w"])[:, None]
    m = 2.0 * math.pi * (np.arange(steps) + 0.5) / steps
    m = np.broadcast_to(m, (len(cols["a"]), steps))
    ecc = _kepler(m, np.broadcast_to(e, m.shape))
    nu = 2.0 * np.arctan2(np.sqrt(1.0 + e) * np.sin(ecc / 2.0),
                          np.sqrt(1.0 - e) * np.cos(ecc / 2.0))
    r = a * (1.0 - e * np.cos(ecc))
    z = r * np.sin(peri + nu) * np.sin(inc)
    return r, z


def measure(cols, steps=720, au_places=3, deg_places=2):
    """The three spread tables from the orbits, keyed as the store keys
    them. The ends that can be had exactly are taken exactly: the 0th and
    100th distance are the nearest perihelion and the farthest aphelion,
    the 100th latitude the largest inclination.

    The defaults ARE the measurement's settings, in this one place: the
    points per orbit, evenly in time, and each table's rounding at rest,
    in decimal places of an AU and of a degree. Settings, not values; the
    rows' check measures again with the same ones."""
    r, z = orbit_points(cols, steps)
    r, z = r.ravel(), z.ravel()
    lat = np.degrees(np.arcsin(np.clip(np.abs(z) / r, 0.0, 1.0)))
    height = np.abs(z)
    a, e, inc = cols["a"], cols["e"], cols["i"]
    out = {}
    for name, values, places in (
            ('MAIN_BELT_DISTANCE_PERCENTILES_AU', r, au_places),
            ('MAIN_BELT_LATITUDE_PERCENTILES_DEG', lat, deg_places),
            ('MAIN_BELT_HEIGHT_PERCENTILES_AU', height, au_places)):
        cut = np.percentile(values, PERCENTILES)
        if name == 'MAIN_BELT_DISTANCE_PERCENTILES_AU':
            cut[0] = float(np.min(a * (1.0 - e)))
            cut[-1] = float(np.max(a * (1.0 + e)))
        elif name == 'MAIN_BELT_LATITUDE_PERCENTILES_DEG':
            cut[0] = 0.0
            cut[-1] = float(np.max(inc))
        else:
            cut[0] = 0.0
        out[name] = dict((str(p), round(float(v), places))
                         for p, v in zip(PERCENTILES, cut))
    return out


def span(rows):
    """(nearest, farthest) distance of the drawing, in AU: the 0th and
    100th distance."""
    t = rows['MAIN_BELT_DISTANCE_PERCENTILES_AU']
    return t['0'], t['100']


def drawn_main_belt(rows=None, seed=443, dots=6000):
    """The belt as drawn: {'x', 'y', 'z', 'settings'}, lists in AU.

    The defaults ARE the drawing's settings, in this one place: the seed
    and the dot count. Rendering settings, not measurements
    (provenance-discipline, Three Kinds of Drawing Number)."""
    rows = rows_from_store() if rows is None else rows
    rng = np.random.default_rng(seed)
    d_share, d_value = _table(rows, 'MAIN_BELT_DISTANCE_PERCENTILES_AU')
    l_share, l_value = _table(rows, 'MAIN_BELT_LATITUDE_PERCENTILES_DEG')
    radii = np.interp(rng.uniform(0.0, 1.0, dots), d_share, d_value)
    lat = np.radians(np.interp(rng.uniform(0.0, 1.0, dots), l_share, l_value))
    lat = np.where(rng.uniform(0.0, 1.0, dots) < 0.5, -lat, lat)
    lon = rng.uniform(0.0, 2.0 * math.pi, dots)
    x = radii * np.cos(lat) * np.cos(lon)
    y = radii * np.cos(lat) * np.sin(lon)
    z = radii * np.sin(lat)
    return {'x': [float(v) for v in x], 'y': [float(v) for v in y],
            'z': [float(v) for v in z],
            'settings': {'dots': dots, 'seed': seed}}


def _allow(want):
    return max(4.0 * math.sqrt(want), 0.15 * want)


def check_dots(dots, rows, slack=0.0006):
    """Failures for a set of drawn dots, as sentences. slack allows for
    the stored file's rounding of each coordinate."""
    failures = []
    pts = np.array([dots['x'], dots['y'], dots['z']], dtype=float)
    r = np.sqrt((pts ** 2).sum(axis=0))
    n = len(r)
    if n == 0:
        return ["no dots"]
    near, far = span(rows)
    off = r[(r < near - slack) | (r > far + slack)]
    if len(off):
        failures.append("ends: %d dot(s) lie outside %g to %g AU, e.g. at "
                        "%.4f" % (len(off), near, far, off[0]))
    lat = np.degrees(np.arcsin(np.clip(np.abs(pts[2]) / r, 0.0, 1.0)))
    for name, values, what, unit in (
            ('MAIN_BELT_DISTANCE_PERCENTILES_AU', r, "distance", "AU"),
            ('MAIN_BELT_LATITUDE_PERCENTILES_DEG', lat, "latitude", "deg")):
        shares, cuts = _table(rows, name)
        for k in range(len(cuts) - 1):
            lo, hi = cuts[k], cuts[k + 1]
            last = k == len(cuts) - 2
            got = int(np.sum((values >= lo) & ((values <= hi) if last
                                               else (values < hi))))
            want = n * (shares[k + 1] - shares[k])
            if abs(got - want) > _allow(want):
                failures.append("%s: %d dots between %g and %g %s, where "
                                "the measured spread puts %.0f (allowing "
                                "%.0f)" % (what, got, lo, hi, unit, want,
                                           _allow(want)))
    heights = rows['MAIN_BELT_HEIGHT_PERCENTILES_AU']
    for p in ('50', '90'):
        got = int(np.sum(np.abs(pts[2]) <= heights[p] + slack))
        want = n * float(p) / 100.0
        if abs(got - want) > _allow(want):
            failures.append("height: %d dots within %g AU of the ecliptic, "
                            "where the measured spread puts %.0f (allowing "
                            "%.0f)" % (got, heights[p], want, _allow(want)))
    return failures


def check_rows(rows, path=WORKSHEET):
    """Failures for the rows against the kept answer, as sentences."""
    failures = []
    sheet, cols = load_orbits(path)
    count = len(cols["a"])
    if count != int(rows['MAIN_BELT_SAMPLE_ORBITS']) or count != sheet.get(
            "count"):
        failures.append("rows: the kept answer holds %d orbits, its count "
                        "says %s, the store %d" % (
                            count, sheet.get("count"),
                            int(rows['MAIN_BELT_SAMPLE_ORBITS'])))
    if sheet.get("all_mba_count") != int(rows['MAIN_BELT_JPL_COUNT']):
        failures.append("rows: the kept answer counts %s MBAs in all, the "
                        "store %d" % (sheet.get("all_mba_count"),
                                      int(rows['MAIN_BELT_JPL_COUNT'])))
    q = cols["a"] * (1.0 - cols["e"])
    bad = np.where((cols["a"] <= rows['MAIN_BELT_A_INNER_AU'])
                   | (cols["a"] >= rows['MAIN_BELT_A_OUTER_AU'] + 1e-9)
                   | (q <= rows['MAIN_BELT_Q_MIN_AU'])
                   | (cols["H"] > rows['MAIN_BELT_SAMPLE_H_MAX']))[0]
    if len(bad):
        k = int(bad[0])
        failures.append("rows: %d orbit(s) in the kept answer are not MBAs "
                        "within the H cut by the class rows, e.g. a %g, q "
                        "%.3f, H %g" % (len(bad), cols["a"][k], q[k],
                                        cols["H"][k]))
    again = measure(cols)
    for name in TABLES:
        moved = [p for p in again[name]
                 if abs(again[name][p] - rows[name].get(p, float('nan')))
                 > 1e-9 or p not in rows[name]]
        if moved or len(rows[name]) != len(again[name]):
            p = moved[0] if moved else "?"
            failures.append("rows: %s is not the kept answer's spread, e.g. "
                            "the %sth percentile: %s in the store, %s "
                            "measured" % (name, p, rows[name].get(p),
                                          again[name].get(p)))
    return failures


def check(rows=None):
    rows = rows_from_store() if rows is None else rows
    return check_rows(rows) + check_dots(drawn_main_belt(rows), rows)


def hover_text(rows=None, br="<br>"):
    """The visitor's words for the cloud, every number read from a row.
    br is '<br>' for a Plotly hover and '\\n' for a Tk tooltip."""
    rows = rows_from_store() if rows is None else rows
    d = rows['MAIN_BELT_DISTANCE_PERCENTILES_AU']
    h = rows['MAIN_BELT_HEIGHT_PERCENTILES_AU']
    km_per_au = rows['KM_PER_AU']
    import constants_rows
    d_figs = constants_rows.figures_of('MAIN_BELT_DISTANCE_PERCENTILES_AU')
    h_figs = constants_rows.figures_of('MAIN_BELT_HEIGHT_PERCENTILES_AU')

    def au(v, figs):
        """v AU at the row's declared count, and its kilometres to the
        place that count's last digit carries (the Report test:
        provenance-discipline, references/figures.md, The ceiling)."""
        last = 10.0 ** (math.floor(math.log10(abs(v))) - figs + 1)
        place = 10.0 ** round(math.log10(last * km_per_au))
        mkm = round(v * km_per_au / place) * place / 1.0e6
        return "%s AU" % ("%.*g" % (figs, v)), "{:,.0f}".format(mkm)

    def far(v, figs):
        a, m = au(v, figs)
        return "%s (about %s million km)" % (a, m)
    lines = [
        "This cloud shows how far the main asteroid belt reaches, measured",
        "from %s of JPL's main-belt orbits. The dots are not asteroids:"
        % "{:,}".format(int(rows['MAIN_BELT_SAMPLE_ORBITS'])),
        "they are placed at random inside that measured spread, so the",
        "cloud is the same on every date.",
        "",
        "JPL classes an asteroid a Main-belt Asteroid (MBA) when its",
        "semi-major axis, its average distance from the Sun, is between",
        "%.1f and %.1f AU, and its perihelion, its nearest point to the Sun,"
        % (rows['MAIN_BELT_A_INNER_AU'], rows['MAIN_BELT_A_OUTER_AU']),
        "is beyond %g AU." % rows['MAIN_BELT_Q_MIN_AU'],
        "",
        "Following those orbits all the way round, the asteroids come as",
        "near as %s" % far(d['0'], d_figs),
        "and go as far as %s." % far(d['100'], d_figs),
        "Nine tenths of the time they are between %s and %s from"
        % (au(d['5'], d_figs)[0], au(d['95'], d_figs)[0]),
        "the Sun, and within %s" % far(h['90'], h_figs),
        "of the plane of Earth's orbit; half the time within",
        "%s." % far(h['50'], h_figs),
        "",
        "The %s are the brightest of JPL's %s main-belt asteroids,"
        % ("{:,}".format(int(rows['MAIN_BELT_SAMPLE_ORBITS'])),
           "{:,}".format(int(rows['MAIN_BELT_JPL_COUNT']))),
        "absolute magnitude %g or brighter, which are roughly the larger"
        % rows['MAIN_BELT_SAMPLE_H_MAX'],
        "ones. Which asteroids to measure was our choice, made to keep",
        "the cloud readable; it is not a measurement.",
    ]
    return br.join(lines)


def main():
    rows = rows_from_store()
    sheet, cols = load_orbits()
    print("main belt: %d orbits kept from JPL (asked %s), %d MBAs in all"
          % (len(cols["a"]), sheet.get("asked"), sheet.get("all_mba_count")))
    for name in TABLES:
        t = rows[name]
        print("  %s: 0th %s, 5th %s, 50th %s, 90th %s, 95th %s, 100th %s"
              % (name, t['0'], t['5'], t['50'], t['90'], t['95'], t['100']))
    dots = drawn_main_belt(rows)
    near, far = span(rows)
    print("drawn: %d dots between %g and %g AU" % (len(dots['x']), near, far))
    failures = check(rows)
    for line in failures:
        print("FAIL: " + line)
    print("MAIN BELT: %s" % ("all checks pass" if not failures
                             else "%d check(s) FAILED" % len(failures)))
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
