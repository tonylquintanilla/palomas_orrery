"""
sun_corona_sampler.py - the Sun's corona as dots that thin out with
distance, from the Sun's surface to the Alfven surface.

Tony's rulings of 2026-10-19 (L-410, with L-131): the inner and outer
corona spheres become ONE plasma fade, following the measured electron
density from the Sun's surface out to the Alfven surface, which stays
drawn as it is ("Confirmed as recommended"). Each dot's PLACE shows how
dense the gas is; its BRIGHTNESS shows how much sunlight reaches it,
which falls with the square of distance from the Sun ("Yes confirmed",
the same rule as the dust cloud's). A stored drawing: placed once here,
drawn as given by both instruments (the rule L-434 set for the Hills
cloud). Sources and rulings:
documentation/SOURCES_L410_sun_corona_dust_20261019.md.

THE PROFILE. Mann, Warmuth, Vocks and Rouillard (2023), A&A 679, A64,
Sect. 3: an isothermal Parker solar wind, eq. 9,

    v'^2 - ln(v'^2) = 4 ln(r') + 4 / r' - 3,  v' = v / v_c,  r' = r / r_c,

with v_c = (k T / (mu m_p))^(1/2) and r_c = G M_sun / (2 v_c^2), on the
accelerating branch (v' < 1 inside r_c, v' > 1 beyond); and eq. 10,
r^2 N_e v = C_e, so N_e = C_e / (r^2 v). Every number is a row in
constants_new.py, never typed here: T, mu and C_e are the article's
(CORONA_MODEL_*), k and m_p are CODATA 2022's, G M_sun is IAU's. The
density worked out this way lies 0.9 to 1.6 percent above the article's
Table 8 at every one of its 2,491 distances, 1 to 250 solar radii (the
row CORONA_MODEL_TEMPERATURE_K records the comparison).

WHAT IS DRAWN BY CHOICE (said in the website's drawing note, 1e):
- the model's long-term average, drawn the same in every direction: the
  real corona is shaped by the Sun's magnetic field, and the streamer
  belt, drawn with it, shows its brightest part;
- the dots start at the Sun's surface, one solar radius (the unit), and
  stop at the Alfven surface (ALFVEN_SURFACE_RADII), where the gas
  becomes the solar wind;
- only the SHAPE of the thinning is drawn, never a density: dots per
  unit volume follow N_e(r), so the count in each shell of thickness dr
  follows N_e(r) r^2 dr.

HOW THE DOTS ARE PLACED. Each dot's distance is drawn from N_e(r) r^2 by
inverting its cumulative sum on a fine grid; its direction is uniform on
the sphere. Each dot carries a weight from 0 to 1 for its brightness:
the logarithm of the sunlight at its distance, which falls as 1 / r^2,
scaled between the Alfven surface (0) and the surface (1). The seed, the
dot count and the grid are rendering settings (drawn_corona's defaults),
not measurements.

Coordinates are in solar radii, centred on the Sun. The drawing is
round, so no frame turn changes it.

Key functions:
    drawn_corona() - the dots as drawn, with the settings below
    density() - N_e(r) from the rows, electrons per cubic centimetre
    check_dots() - the checks below, as a list of failures

THE CHECKS (check_dots() returns what fails; test_drawings_export.py
plants a fault in each):
- every dot lies between the surface and the Alfven surface;
- the dots follow the profile: in shells between the two, each shell's
  count is the profile's share within a tolerance that allows for chance
  (four standard deviations, or 15 percent, whichever is larger);
- each dot's weight is the one its distance gives, to the file's
  rounding.

Run it to print the counts and the checks:
    python sun_corona_sampler.py

Consumed by: solar_visualization_shells.py (the corona), export_drawings.py,
             test_drawings_export.py

Role: computation
Domain: orrery

Module created: October 19, 2026 with Anthropic's Claude Opus 5.5 (L-410)
"""
import math
import sys

import numpy as np

# One home for the rows this drawing reads.
ROW_NAMES = (
    'CORONA_MODEL_TEMPERATURE_K',
    'CORONA_MODEL_MEAN_MOLECULAR_WEIGHT',
    'CORONA_MODEL_ELECTRON_FLUX_PER_S',
    'BOLTZMANN_CONSTANT_J_PER_K',
    'PROTON_MASS_KG',
    'GM_SUN_SI',
    'SUN_RADIUS_KM',
    'ALFVEN_SURFACE_RADII',
)


def _m_per_km():
    """Metres in a kilometre: a unit conversion, exact by definition."""
    return 1000.0


def _cm_per_m():
    """Centimetres in a metre: a unit conversion, exact by definition."""
    return 100.0


def rows_from_store():
    """The rows this module reads, from constants_new.py, as a dict."""
    import constants_new
    return {name: float(getattr(constants_new, name)) for name in ROW_NAMES}


def span(rows):
    """(inner, outer) of the drawing, in solar radii. The inner end is the
    Sun's surface, one solar radius: the drawing's own unit, so a
    definition, not a measurement."""
    return (1.0, rows['ALFVEN_SURFACE_RADII'])


def _critical(rows):
    """(v_c in m/s, r_c in solar radii) of Mann et al.'s Parker wind."""
    k = rows['BOLTZMANN_CONSTANT_J_PER_K']
    m_p = rows['PROTON_MASS_KG']
    v_c = math.sqrt(k * rows['CORONA_MODEL_TEMPERATURE_K']
                    / (rows['CORONA_MODEL_MEAN_MOLECULAR_WEIGHT'] * m_p))
    r_c_m = rows['GM_SUN_SI'] / (2.0 * v_c * v_c)
    return v_c, r_c_m / (rows['SUN_RADIUS_KM'] * _m_per_km())


def _v_prime(rp):
    """v / v_c on the accelerating branch of eq. 9, at r' = r / r_c."""
    if abs(rp - 1.0) < 1e-12:
        return 1.0
    rhs = 4.0 * math.log(rp) + 4.0 / rp - 3.0

    def f(u):
        return u * u - math.log(u * u) - rhs
    lo, hi = (1e-12, 1.0) if rp < 1.0 else (1.0, 1e3)
    for _ in range(200):                      # bisection: f falls then rises
        mid = 0.5 * (lo + hi)
        if (f(mid) > 0) == (rp < 1.0):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def wind_speed(r, rows):
    """The model's solar wind speed at r solar radii, in km/s."""
    v_c, r_c = _critical(rows)
    return v_c * _v_prime(r / r_c) / _m_per_km()


def density(r, rows):
    """N_e(r), electrons per cubic centimetre, r in solar radii (eq. 10:
    N_e = C_e / (r^2 v))."""
    v_c, r_c = _critical(rows)
    v_cm_s = v_c * _v_prime(r / r_c) * _cm_per_m()
    r_cm = r * rows['SUN_RADIUS_KM'] * _m_per_km() * _cm_per_m()
    return rows['CORONA_MODEL_ELECTRON_FLUX_PER_S'] / (r_cm * r_cm * v_cm_s)


def weight(r, rows):
    """0 at the Alfven surface, 1 at the Sun's surface, by the log of the
    sunlight reaching distance r, which falls as 1 / r^2."""
    inner, outer = span(rows)
    w = 1.0 - math.log(r / inner) / math.log(outer / inner)
    return max(0.0, min(1.0, w))


def _cdf(rows, grid):
    """The radii and the cumulative share of dots inside each, from
    N_e(r) r^2 on a grid of `grid` steps, finer near the surface where
    the density falls fastest."""
    inner, outer = span(rows)
    r = inner * (outer / inner) ** np.linspace(0.0, 1.0, grid + 1)
    f = np.array([density(x, rows) * x * x for x in r])
    steps = 0.5 * (f[1:] + f[:-1]) * np.diff(r)
    cum = np.concatenate([[0.0], np.cumsum(steps)])
    return r, cum / cum[-1]


def share_between(lo, hi, rows, grid=4000):
    """The profile's share of the dots between radii lo and hi."""
    r, cum = _cdf(rows, grid)
    return float(np.interp(hi, r, cum) - np.interp(lo, r, cum))


def drawn_corona(rows=None, seed=410, dots=2500, grid=4000):
    """The corona as drawn: {'x', 'y', 'z', 'w', 'settings'}, lists in
    solar radii and weights 0 to 1.

    The defaults ARE the drawing's settings, in this one place: the seed,
    the dot count and the grid the distances are drawn from. Rendering
    settings, not measurements (provenance-discipline, Three Kinds of
    Drawing Number)."""
    rows = rows_from_store() if rows is None else rows
    rng = np.random.default_rng(seed)
    r_grid, cum = _cdf(rows, grid)
    radii = np.interp(rng.uniform(0.0, 1.0, dots), cum, r_grid)
    cos_t = rng.uniform(-1.0, 1.0, dots)
    lon = rng.uniform(0.0, 2.0 * math.pi, dots)
    sin_t = np.sqrt(1.0 - cos_t * cos_t)
    x = (radii * sin_t * np.cos(lon)).tolist()
    y = (radii * sin_t * np.sin(lon)).tolist()
    z = (radii * cos_t).tolist()
    w = [weight(float(r), rows) for r in radii]
    return {'x': x, 'y': y, 'z': z, 'w': w,
            'settings': {'dots': dots, 'seed': seed, 'grid': grid}}


# Shells between the surface and the Alfven surface for the profile
# check, edges in solar radii, the two ends added at run time. Few
# enough that chance does not move the answer at 2,500 dots.
CHECK_EDGES = (1.1, 1.3, 2.0, 5.0)


def check_dots(dots, rows, slack=0.02, w_slack=0.011):
    """Failures for a set of drawn dots, as sentences. slack allows for
    the stored file's rounding of each coordinate, w_slack for a
    weight's."""
    failures = []
    inner, outer = span(rows)
    radii = [math.sqrt(x * x + y * y + z * z)
             for x, y, z in zip(dots['x'], dots['y'], dots['z'])]
    n = len(radii)
    off = [r for r in radii if r < inner - slack or r > outer + slack]
    if off:
        failures.append("%d dot(s) lie outside %g to %g solar radii, e.g. "
                        "at %.3f" % (len(off), inner, outer, off[0]))
    edges = [inner] + [e for e in CHECK_EDGES if inner < e < outer] + [outer]
    for lo, hi in zip(edges[:-1], edges[1:]):
        got = sum(1 for r in radii
                  if lo <= r < hi or (hi == outer and r >= hi))
        if lo == inner:
            got += sum(1 for r in radii if r < inner)   # rounding inside
        want = n * share_between(lo, hi, rows)
        allow = max(4.0 * math.sqrt(want), 0.15 * want)
        if abs(got - want) > allow:
            failures.append("the dots do not follow the profile: %d between "
                            "%g and %g solar radii, where it gives %.0f "
                            "(allowing %.0f)" % (got, lo, hi, want, allow))
    if 'w' in dots:
        wrong = [k for k, r in enumerate(radii)
                 if abs(dots['w'][k] - weight(min(max(r, inner), outer), rows))
                 > w_slack + 0.02]
        if wrong:
            failures.append("%d dot(s) carry a weight their distance does not "
                            "give, e.g. dot %d" % (len(wrong), wrong[0]))
    return failures


def check(rows=None, seed=410):
    rows = rows_from_store() if rows is None else rows
    return check_dots(drawn_corona(rows, seed), rows)


def main():
    rows = rows_from_store()
    dots = drawn_corona(rows)
    inner, outer = span(rows)
    v_c, r_c = _critical(rows)
    radii = [math.sqrt(x * x + y * y + z * z)
             for x, y, z in zip(dots['x'], dots['y'], dots['z'])]
    print("corona: %d dots from %g to %g solar radii; critical point at %.2f "
          "solar radii, %.1f km/s" % (len(radii), inner, outer, r_c,
                                      v_c / _m_per_km()))
    for r in (inner, 2.0, 5.0, 10.0, outer):
        print("  N_e at %5g solar radii: %.4g electrons per cubic centimetre, "
              "wind %.1f km/s" % (r, density(r, rows), wind_speed(r, rows)))
    edges = [inner] + list(CHECK_EDGES) + [outer]
    for lo, hi in zip(edges[:-1], edges[1:]):
        print("  %5g to %5g solar radii: %4d dots"
              % (lo, hi, sum(1 for r in radii if lo <= r < hi)))
    failures = check_dots(dots, rows)
    for line in failures:
        print("FAIL: " + line)
    print("CORONA: %s" % ("all checks pass" if not failures
                          else "%d check(s) FAILED" % len(failures)))
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
