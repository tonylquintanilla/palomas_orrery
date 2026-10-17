"""
van_allen_belt_sampler.py - Earth's two radiation belts as dots scattered
at random along dipole field lines, thickest at each belt's measured peak.

Tony's rulings of 2026-10-16 and 2026-10-17 (L-330): both belts are drawn
curved along the field lines (option A), as a density field, with the dots
scattered at random ("Yes, random. And it shows the density better too.");
the inner belt stays curved ("it reads okay"). Random dots are a stored
drawing (L-434, option A of 2026-10-11): the orrery places them once, from
a fixed seed, and the website draws the dots it is given.

THE FIELD LINES. A dipole field line is r = r0 cos^2(lat), where r0 is
where the line crosses the magnetic equator; written in Earth radii,
r0 is McIlwain's L, and the line meets the ground where cos^2(lat) = 1/L.
Source: Koskinen, H. E. J. and Kilpua, E. K. J. (2022), "Physics of
Earth's Radiation Belts: Theory and Observations", Springer, Astronomy
and Astrophysics Library, open access, doi:10.1007/978-3-030-82167-8 --
chapter 1, "Radiation Belts and Their Environment", sec. 1.2.1 "The
Dipole Field": the field line r = r0 cos^2(lambda), L = r0/R_E, and the
footpoint lambda_e = arccos(1/sqrt(L)).
Access: open, https://link.springer.com/chapter/10.1007/978-3-030-82167-8_1
Read: sec. 1.2.1, through the chapter page, 2026-10-17, Claude Opus 5.5.
The equation numbers did not come through the reader, so the locator is
the section.

WHAT IS MEASURED (every number is a row in constants_new.py, never typed
here): each belt's inner and outer edge at the equator, and its peak.

WHAT IS DRAWN BY CHOICE (said in the hover):
- the field is a dipole at Earth's centre lined up with the SPIN axis, the
  daily average of the tilted magnetic field (L-231); the instrument turns
  the dots to Earth's pole;
- each belt stops at the ground (r >= 1 Earth radius), which the relation
  gives by itself: every field line ends at its footpoint;
- the fade. A dot's weight is f(L) x g(s): f is 1 at the served peak and
  falls in a straight line to the edge weight at each served edge; s is the
  dot's latitude as a share of its field line's footpoint latitude, and
  g = 1 - s^2. Drawn to show the shape, not measured.

HOW THE DOTS ARE PLACED. Dots per unit volume follow the weight. Each
sample is L picked evenly between the belt's edges, s evenly in -1 to 1,
and the longitude evenly round the axis; it is kept with a chance
proportional to the weight times the volume it stands for,
dV ~ L^2 cos^7(lat) dL dlat dlon with dlat = (footpoint latitude) ds.
The settings (drawn_van_allen_belts' defaults) are rendering choices,
not measurements.

Coordinates are in Earth radii in Earth's body frame: z along the spin
axis, x and y in the equatorial plane. Each dot also carries its weight,
so both instruments shade it the same way.

Key functions:
    drawn_van_allen_belts() - the dots as drawn, with the settings below
    check() - the checks below, as a list of failures

THE CHECKS (check() returns what fails; test_drawings_export.py plants a
fault in each):
- every dot lies on a field line between its belt's two edge rows;
- no dot is below the ground;
- at the equator, each belt's dots are thicker in the slice holding its
  peak than in the slices at its two edges, by a third or more.

Run it to print the counts and the checks:
    python van_allen_belt_sampler.py

Consumed by: earth_visualization_shells.py (the belts), export_drawings.py,
             test_drawings_export.py

Role: computation
Domain: orrery

Module created: October 17, 2026 with Anthropic's Claude Opus 5.5 (L-330)
"""
import math
import sys

import numpy as np

# One home for each belt's rows: (name, inner edge, peak, outer edge).
BELT_ROWS = (
    ('inner', 'EARTH_VAN_ALLEN_INNER_BELT_INNER_EDGE',
     'EARTH_VAN_ALLEN_INNER_RADII', 'EARTH_VAN_ALLEN_INNER_BELT_OUTER_EDGE'),
    ('outer', 'EARTH_VAN_ALLEN_OUTER_BELT_INNER_EDGE',
     'EARTH_VAN_ALLEN_OUTER_RADII', 'EARTH_VAN_ALLEN_OUTER_BELT_OUTER_EDGE'),
)
ROW_NAMES = tuple(name for belt in BELT_ROWS for name in belt[1:])

def rows_from_store():
    """The rows this module reads, from constants_new.py, as a dict."""
    import constants_new
    return {name: float(getattr(constants_new, name)) for name in ROW_NAMES}


def belts(rows):
    """[(name, inner, peak, outer)] in Earth radii, from the rows."""
    return [(name, rows[a], rows[p], rows[b]) for name, a, p, b in BELT_ROWS]


def foot_lat(L):
    """Latitude (radians) where the field line of shell L meets r = 1."""
    return math.acos(1.0 / math.sqrt(L))


def weight(L, lat, inner, peak, outer, edge_weight):
    """The declared fade, 0 to 1: straight lines across the belt from the
    peak to edge_weight at each edge, times 1 - s^2 up the field line."""
    if L <= peak:
        t = (L - inner) / (peak - inner)
    else:
        t = (outer - L) / (outer - peak)
    across = edge_weight + (1.0 - edge_weight) * max(0.0, min(1.0, t))
    s = abs(lat) / foot_lat(L)
    return across * max(0.0, 1.0 - s * s)


def sample_belt(n, inner, peak, outer, edge_weight, rng):
    """n dots for one belt: lists x, y, z (Earth radii) and w."""
    # The kept-chance's bound: weight <= 1, L^2 <= outer^2, cos^7 <= 1,
    # footpoint latitude <= that of the outer edge.
    top = outer * outer * foot_lat(outer)
    x, y, z, w = [], [], [], []
    while len(x) < n:
        L = rng.uniform(inner, outer)
        s = rng.uniform(-1.0, 1.0)
        lat = s * foot_lat(L)
        wt = weight(L, lat, inner, peak, outer, edge_weight)
        keep = wt * L * L * math.cos(lat) ** 7 * foot_lat(L)
        lon = rng.uniform(0.0, 2.0 * math.pi)
        if rng.uniform(0.0, top) > keep:
            continue
        r = L * math.cos(lat) ** 2
        rho = r * math.cos(lat)
        x.append(rho * math.cos(lon))
        y.append(rho * math.sin(lon))
        z.append(r * math.sin(lat))
        w.append(wt)
    return x, y, z, w


def drawn_van_allen_belts(rows=None, seed=330, dots_inner=1200,
                          dots_outer=2000, edge_weight=0.2):
    """Both belts as drawn: {'inner': {...}, 'outer': {...}, 'settings'},
    each belt holding lists x, y, z (Earth radii) and w (0 to 1).

    The defaults ARE the drawing's settings, in this one place, as
    hills_cloud_sampler.drawn_hills_cloud() keeps its own: the seed, the
    dots in each belt, and the weight at the belts' edges. Rendering
    settings, not measurements (provenance-discipline, Three Kinds of
    Drawing Number). Tony looked at 1,200 and 2,000 dots on his phone on
    2026-10-17."""
    rows = rows_from_store() if rows is None else rows
    rng = np.random.default_rng(seed)
    counts = {'inner': dots_inner, 'outer': dots_outer}
    out = {'settings': {'edge_weight': edge_weight,
                        'dots_inner': dots_inner,
                        'dots_outer': dots_outer, 'seed': seed}}
    for name, inner, peak, outer in belts(rows):
        x, y, z, w = sample_belt(counts[name], inner, peak, outer,
                                 edge_weight, rng)
        out[name] = {'x': x, 'y': y, 'z': z, 'w': w}
    return out


def shell_of(x, y, z):
    """The L of the field line through a dot (Earth radii)."""
    r = math.sqrt(x * x + y * y + z * z)
    cos_lat = math.sqrt(x * x + y * y) / r
    return r / (cos_lat * cos_lat)


def check_dots(dots, rows, slack=0.02):
    """Failures for a set of drawn dots, as sentences. slack allows for
    the rounding of the stored file's coordinates (export_drawings.py)."""
    failures = []
    for name, inner, peak, outer in belts(rows):
        belt = dots[name]
        pts = list(zip(belt['x'], belt['y'], belt['z']))
        shells = [shell_of(*p) for p in pts]
        off = [L for L in shells if L < inner - slack or L > outer + slack]
        if off:
            failures.append("%s belt: %d dot(s) lie off the field lines "
                            "between its edges (%g to %g), e.g. L = %.2f"
                            % (name, len(off), inner, outer, off[0]))
        under = [p for p in pts
                 if math.sqrt(p[0] ** 2 + p[1] ** 2 + p[2] ** 2) < 1 - slack]
        if under:
            failures.append("%s belt: %d dot(s) below the ground"
                            % (name, len(under)))
        # The equator's densest slice: dots within three tenths of the
        # footpoint latitude of the equator, counted in six slices across
        # the belt (few enough that chance does not move the answer).
        width = (outer - inner) / 6.0
        counts = [0] * 6
        for p, L in zip(pts, shells):
            r = math.sqrt(p[0] ** 2 + p[1] ** 2 + p[2] ** 2)
            lat = math.asin(p[2] / r)
            if abs(lat) <= 0.3 * foot_lat(max(L, 1.0001)):
                k = min(5, max(0, int((L - inner) / width)))
                counts[k] += 1
        # Per unit volume: a slice's volume goes as L^2 times the band's
        # latitude width, which is a share of the footpoint latitude.
        mids = [inner + (k + 0.5) * width for k in range(6)]
        dens = [c / (m * m * foot_lat(m)) for c, m in zip(counts, mids)]
        k = min(5, max(0, int((peak - inner) / width)))
        ends = [dens[0], dens[5]]
        if not all(dens[k] > 1.3 * e for e in ends):
            failures.append("%s belt: at the equator the dots are not "
                            "thickest at the peak %g: per unit volume, the "
                            "slice holding it has %.3g against %.3g and %.3g "
                            "at the two edges" % (name, peak, dens[k],
                                                   ends[0], ends[1]))
    return failures


def check(rows=None, seed=330):
    rows = rows_from_store() if rows is None else rows
    return check_dots(drawn_van_allen_belts(rows, seed), rows)


def main():
    rows = rows_from_store()
    dots = drawn_van_allen_belts(rows)
    for name, inner, peak, outer in belts(rows):
        print("%s belt: %d dots, edges %g to %g Earth radii, peak %g, "
              "reaching the ground at %.1f to %.1f degrees latitude"
              % (name, len(dots[name]['x']), inner, outer, peak,
                 math.degrees(foot_lat(inner)), math.degrees(foot_lat(outer))))
    failures = check_dots(dots, rows)
    for line in failures:
        print("FAIL: " + line)
    print("VAN ALLEN BELTS: %s" % ("all checks pass" if not failures
                                   else "%d check(s) FAILED" % len(failures)))
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
