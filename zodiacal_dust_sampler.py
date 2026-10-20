"""
zodiacal_dust_sampler.py - the zodiacal dust cloud as dots: a flattened
cloud of dust around the Sun that thins with distance, from the edge of
the dust-free zone out to 5.2 AU.

Tony's rulings of 2026-10-19 (L-131, with L-410): the dust is its own
drawing, a stored cloud of dots following Kelsall et al. (1998)'s COBE
model. A dot's PLACE shows the dust's density; its BRIGHTNESS shows the
sunlight it receives, which falls with the square of distance ("Confirmed
as recommend"; the square, not the cube, "Confirmed"). The dots stop at
5.2 AU, where the model stops its sums ("Confirmed"). Near the Sun the
dust thins from about 19 solar radii and is gone by about 5 (Lamy et al.
2022). A stored drawing: placed once here, drawn as given by both
instruments (the rule L-434 set for the Hills cloud). Sources and
rulings: documentation/SOURCES_L410_sun_corona_dust_20261019.md.

THE MODEL. Kelsall et al. (1998), ApJ 508, 44, Sect. 4.2, the smooth
cloud: n = n0 R^-alpha f(zeta), eq. 6, with zeta = |Z_c / R| the height
over the cloud's middle plane divided by distance, and eq. 7,

    f(zeta) = exp(-beta g^gamma),  g = zeta^2 / (2 mu)  for zeta < mu,
                                   g = zeta - mu / 2    for zeta >= mu.

The middle plane is tilted i to the ecliptic, its ascending node at
Omega (eq. 5: Z_c = X sin Omega sin i - Y cos Omega sin i + Z cos i).
Every number is a row in constants_new.py: alpha, beta, gamma, mu, i and
Omega (Table 1), and the 5.2 AU cutoff; Lamy et al.'s 19 and 5 solar
radii; the solar radius and the AU. n0 is not needed: only the shape is
drawn.

Because zeta is |sin b|, b the latitude above the middle plane, the
density separates in spherical coordinates: a volume element is
R^2 dR d(sin b) d(longitude), so a dot's distance is drawn from
R^(2 - alpha) (times the thinning near the Sun, below), its sin b from
f(|sin b|), and its longitude around the middle plane uniformly.

WHAT IS DRAWN BY CHOICE:
- the cloud has no edge; the dots stop at ZODIACAL_DUST_OUTER_AU, where
  the COBE model stops adding up its light (said in the hover, 2c and
  2e);
- only the model's smooth cloud, not the narrow dust bands it also
  includes (said in 2e);
- the middle plane follows Kelsall's fit everywhere; near the Sun the
  real plane is warped (Lamy et al. 2022), which the drawing does not
  show (said in 2d);
- centred on the Sun: the model's small offset of the cloud's centre
  (Table 1, about 0.013 AU) is not drawn;
- THE THINNING NEAR THE SUN: between DUST_FREE_ZONE_RADII and
  DUST_DEPLETION_OUTER_RADII the density is multiplied by a factor that
  rises in a straight line from 0 at the inner edge to 1 at the outer.
  Lamy et al. give the two edges, not the shape between them, so the
  straight line is a drawing choice (taper() below);
- only the SHAPE is drawn, never a density.

THE BRIGHTNESS. Each dot carries a weight from 0 to 1: the logarithm of
the sunlight at its distance, which falls as 1 / R^2, scaled between the
outer edge (0) and the inner edge (1), as the corona's dots are. The
seed, the dot count and the grid are rendering settings (drawn_dust's
defaults), not measurements.

Coordinates are in AU, centred on the Sun, in the ecliptic frame the
orrery draws in (the model is computed in heliocentric ecliptic
coordinates, Sect. 4.2).

Key functions:
    drawn_dust() - the dots as drawn, with the settings below
    density_shape() - n / n0 at a point, from the rows
    check_dots() - the checks below, as a list of failures

THE CHECKS (check_dots() returns what fails; test_drawings_export.py
plants a fault in each):
- every dot lies between the inner and outer edges;
- the dots follow the radial profile: in shells between the edges, each
  shell's count is the profile's share within a tolerance that allows
  for chance (four standard deviations, or 15 percent, whichever is
  larger);
- the dots follow the vertical profile: the share of dots within
  sin b < 0.1 of the middle plane is the model's, within the same
  tolerance;
- each dot's weight is the one its distance gives, to the file's
  rounding.

Run it to print the counts and the checks:
    python zodiacal_dust_sampler.py

Consumed by: solar_visualization_shells.py (the dust cloud),
             export_drawings.py, test_drawings_export.py

Role: computation
Domain: orrery

Module created: October 19, 2026 with Anthropic's Claude Opus 5.5 (L-131)
"""
import math
import sys

import numpy as np

# One home for the rows this drawing reads.
ROW_NAMES = (
    'ZODIACAL_DUST_DENSITY_EXPONENT',
    'ZODIACAL_DUST_BETA',
    'ZODIACAL_DUST_GAMMA',
    'ZODIACAL_DUST_MU',
    'ZODIACAL_DUST_TILT_DEG',
    'ZODIACAL_DUST_NODE_DEG',
    'ZODIACAL_DUST_OUTER_AU',
    'DUST_DEPLETION_OUTER_RADII',
    'DUST_FREE_ZONE_RADII',
    'SUN_RADIUS_KM',
    'KM_PER_AU',
)


def rows_from_store():
    """The rows this module reads, from constants_new.py, as a dict."""
    import constants_new
    return {name: float(getattr(constants_new, name)) for name in ROW_NAMES}


def _radii_au(rows):
    """One solar radius in AU."""
    return rows['SUN_RADIUS_KM'] / rows['KM_PER_AU']


def span(rows):
    """(inner, outer) of the drawing, in AU: the dust-free zone's edge to
    the model's cutoff."""
    return (rows['DUST_FREE_ZONE_RADII'] * _radii_au(rows),
            rows['ZODIACAL_DUST_OUTER_AU'])


def taper(r, rows):
    """The thinning near the Sun: 0 at the dust-free zone's edge, 1 at the
    depletion zone's outer border, a straight line between (a drawing
    choice; Lamy et al. give the edges, not the shape between)."""
    lo = rows['DUST_FREE_ZONE_RADII'] * _radii_au(rows)
    hi = rows['DUST_DEPLETION_OUTER_RADII'] * _radii_au(rows)
    return max(0.0, min(1.0, (r - lo) / (hi - lo)))


def vertical(zeta, rows):
    """Kelsall et al.'s f(zeta), eq. 7."""
    mu = rows['ZODIACAL_DUST_MU']
    if zeta < mu:
        g = zeta * zeta / (2.0 * mu)
    else:
        g = zeta - mu / 2.0
    return math.exp(-rows['ZODIACAL_DUST_BETA'] * g ** rows['ZODIACAL_DUST_GAMMA'])


def density_shape(r, sin_b, rows):
    """n / n0 at distance r AU and sin b above the middle plane."""
    return (r ** -rows['ZODIACAL_DUST_DENSITY_EXPONENT'] * taper(r, rows)
            * vertical(abs(sin_b), rows))


def weight(r, rows):
    """0 at the outer edge, 1 at the inner, by the log of the sunlight
    reaching distance r, which falls as 1 / r^2."""
    inner, outer = span(rows)
    w = 1.0 - math.log(r / inner) / math.log(outer / inner)
    return max(0.0, min(1.0, w))


def _radial_cdf(rows, grid):
    """The radii and the cumulative share of dots inside each, from
    r^(2 - alpha) times the taper, on a grid finer near the Sun."""
    inner, outer = span(rows)
    r = inner * (outer / inner) ** np.linspace(0.0, 1.0, grid + 1)
    alpha = rows['ZODIACAL_DUST_DENSITY_EXPONENT']
    f = np.array([x ** (2.0 - alpha) * taper(x, rows) for x in r])
    steps = 0.5 * (f[1:] + f[:-1]) * np.diff(r)
    cum = np.concatenate([[0.0], np.cumsum(steps)])
    return r, cum / cum[-1]


def _vertical_cdf(rows, grid):
    """sin b from -1 to 1 and the cumulative share of dots below each."""
    u = np.linspace(-1.0, 1.0, grid + 1)
    f = np.array([vertical(abs(x), rows) for x in u])
    steps = 0.5 * (f[1:] + f[:-1]) * np.diff(u)
    cum = np.concatenate([[0.0], np.cumsum(steps)])
    return u, cum / cum[-1]


def share_between(lo, hi, rows, grid=20000):
    """The radial profile's share of the dots between distances lo and hi."""
    r, cum = _radial_cdf(rows, grid)
    return float(np.interp(hi, r, cum) - np.interp(lo, r, cum))


def share_near_plane(limit, rows, grid=20000):
    """The vertical profile's share of the dots with |sin b| < limit."""
    u, cum = _vertical_cdf(rows, grid)
    return float(np.interp(limit, u, cum) - np.interp(-limit, u, cum))


def to_ecliptic(xm, ym, zm, rows):
    """Turn points from the cloud's middle-plane frame (z its pole, x
    toward its ascending node) to ecliptic coordinates: Rz(Omega) Rx(i),
    which carries the middle plane's pole to eq. 5's (sin Omega sin i,
    -cos Omega sin i, cos i)."""
    inc = math.radians(rows['ZODIACAL_DUST_TILT_DEG'])
    node = math.radians(rows['ZODIACAL_DUST_NODE_DEG'])
    y1 = ym * math.cos(inc) - zm * math.sin(inc)
    z1 = ym * math.sin(inc) + zm * math.cos(inc)
    x = xm * math.cos(node) - y1 * math.sin(node)
    y = xm * math.sin(node) + y1 * math.cos(node)
    return x, y, z1


def sin_b_of(x, y, z, rows):
    """sin b above the middle plane for an ecliptic point (eq. 5)."""
    inc = math.radians(rows['ZODIACAL_DUST_TILT_DEG'])
    node = math.radians(rows['ZODIACAL_DUST_NODE_DEG'])
    zc = (x * math.sin(node) * math.sin(inc) - y * math.cos(node) * math.sin(inc)
          + z * math.cos(inc))
    r = math.sqrt(x * x + y * y + z * z)
    return zc / r if r > 0 else 0.0


def drawn_dust(rows=None, seed=131, dots=3000, grid=20000):
    """The dust cloud as drawn: {'x', 'y', 'z', 'w', 'settings'}, lists in
    AU and weights 0 to 1.

    The defaults ARE the drawing's settings, in this one place: the seed,
    the dot count and the grid the distances are drawn from. Rendering
    settings, not measurements (provenance-discipline, Three Kinds of
    Drawing Number)."""
    rows = rows_from_store() if rows is None else rows
    rng = np.random.default_rng(seed)
    r_grid, r_cum = _radial_cdf(rows, grid)
    u_grid, u_cum = _vertical_cdf(rows, grid)
    radii = np.interp(rng.uniform(0.0, 1.0, dots), r_cum, r_grid)
    sin_b = np.interp(rng.uniform(0.0, 1.0, dots), u_cum, u_grid)
    lon = rng.uniform(0.0, 2.0 * math.pi, dots)
    cos_b = np.sqrt(np.clip(1.0 - sin_b * sin_b, 0.0, 1.0))
    xs, ys, zs, ws = [], [], [], []
    for r, sb, cb, lam in zip(radii, sin_b, cos_b, lon):
        x, y, z = to_ecliptic(r * cb * math.cos(lam), r * cb * math.sin(lam),
                              r * sb, rows)
        xs.append(x)
        ys.append(y)
        zs.append(z)
        ws.append(weight(float(r), rows))
    return {'x': xs, 'y': ys, 'z': zs, 'w': ws,
            'settings': {'dots': dots, 'seed': seed, 'grid': grid}}


# Shells between the edges for the radial check, in AU, the two edges
# added at run time. The height band for the vertical check is
# check_dots's plane_band.
CHECK_EDGES = (0.5, 1.0, 2.0, 3.5)


def check_dots(dots, rows, slack=0.0006, w_slack=0.011, plane_band=0.1):
    """Failures for a set of drawn dots, as sentences. slack allows for
    the stored file's rounding of each coordinate, w_slack for a
    weight's."""
    failures = []
    inner, outer = span(rows)
    pts = list(zip(dots['x'], dots['y'], dots['z']))
    radii = [math.sqrt(x * x + y * y + z * z) for x, y, z in pts]
    n = len(radii)
    off = [r for r in radii if r < inner - slack or r > outer + slack]
    if off:
        failures.append("%d dot(s) lie outside %.4f to %g AU, e.g. at %.4f"
                        % (len(off), inner, outer, off[0]))
    edges = [inner] + [e for e in CHECK_EDGES if inner < e < outer] + [outer]
    for lo, hi in zip(edges[:-1], edges[1:]):
        got = sum(1 for r in radii
                  if lo <= r < hi or (hi == outer and r >= hi)
                  or (lo == inner and r < lo))
        want = n * share_between(lo, hi, rows)
        allow = max(4.0 * math.sqrt(want), 0.15 * want)
        if abs(got - want) > allow:
            failures.append("the dots do not follow the radial profile: %d "
                            "between %g and %g AU, where it gives %.0f "
                            "(allowing %.0f)" % (got, lo, hi, want, allow))
    near = sum(1 for x, y, z in pts if abs(sin_b_of(x, y, z, rows)) < plane_band)
    want = n * share_near_plane(plane_band, rows)
    allow = max(4.0 * math.sqrt(want), 0.15 * want)
    if abs(near - want) > allow:
        failures.append("the dots do not follow the vertical profile: %d "
                        "within sin b %g of the middle plane, where it gives "
                        "%.0f (allowing %.0f)" % (near, plane_band, want, allow))
    if 'w' in dots:
        wrong = [k for k, r in enumerate(radii)
                 if abs(dots['w'][k] - weight(min(max(r, inner), outer), rows))
                 > w_slack + 0.02]
        if wrong:
            failures.append("%d dot(s) carry a weight their distance does not "
                            "give, e.g. dot %d" % (len(wrong), wrong[0]))
    return failures


def check(rows=None, seed=131):
    rows = rows_from_store() if rows is None else rows
    return check_dots(drawn_dust(rows, seed), rows)


def main():
    rows = rows_from_store()
    dots = drawn_dust(rows)
    inner, outer = span(rows)
    radii = [math.sqrt(x * x + y * y + z * z)
             for x, y, z in zip(dots['x'], dots['y'], dots['z'])]
    band = 0.1
    print("zodiacal dust: %d dots from %.4f to %g AU; %.1f%% of them within "
          "sin b %g of the middle plane"
          % (len(radii), inner, outer,
             100.0 * share_near_plane(band, rows), band))
    edges = [inner] + list(CHECK_EDGES) + [outer]
    for lo, hi in zip(edges[:-1], edges[1:]):
        print("  %6.4f to %6.4f AU: %4d dots"
              % (lo, hi, sum(1 for r in radii if lo <= r < hi)))
    failures = check_dots(dots, rows)
    for line in failures:
        print("FAIL: " + line)
    print("ZODIACAL DUST: %s" % ("all checks pass" if not failures
                                 else "%d check(s) FAILED" % len(failures)))
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
