"""
earth_exosphere_sampler.py - Earth's hydrogen exosphere, the geocorona, as
dots that thin out with distance, from 3 to 100 Earth radii.

Tony's rulings of 2026-10-17 (L-410): a boundary is drawn fuzzy only where
nature thins out with no edge, and Earth's hydrogen is that case. Designed
the same day ("I agree. As recommended"): dots from 3 Earth radii, where
the measured profile starts, to the 100 Earth radii detection floor of
EARTH_GEOCORONA_RADII; thinning by Zoennchen et al. (2022)'s day-side
profile to 15 Earth radii and with its measured fall beyond; drawn round;
a stored drawing, placed once here and drawn as given by the website (the
rule L-434 set for the Hills cloud). The seven rows were approved on
2026-10-17 ("read and approved"); their quotations and locators are in
documentation/SOURCES_earth_fade_20261017.md and on each row.

THE PROFILE. Every number is a row in constants_new.py, never typed here.
- From EARTH_EXOSPHERE_H_FIT_INNER_RADII to EARTH_EXOSPHERE_H_FIT_OUTER_RADII
  (3 to 15 Earth radii): Zoennchen et al. (2022), Ann. Geophys. 40:271,
  sec. 6, eq. 7, n(r) = C (r + a)^-p atoms per cubic centimetre, r in
  Earth radii from Earth's centre (C, a and p are the three _FIT_ rows).
- Beyond, to EARTH_GEOCORONA_RADII (100): the same paper's eq. 9 fall,
  n proportional to r^-q (EARTH_EXOSPHERE_H_OUTER_EXPONENT), started from
  eq. 7's value at 15 Earth radii so the profile has no step. The paper
  fits it between 9 and 15 Earth radii; carrying it out to 100 is a
  drawing choice, and the hover says so.

WHAT IS DRAWN BY CHOICE (said in the hover):
- the dots start at 3 Earth radii, where the measurements start, although
  the hydrogen continues inward to the top of the upper atmosphere;
- they stop at 100 Earth radii, where instruments lose the glow
  (Baliukin et al. 2019), not where the hydrogen ends;
- round: the profile is the day side's, and the hydrogen is measured
  denser near the Sun-Earth line on both the day and night sides
  (Zoennchen et al. 2024), which the drawing does not show;
- only the SHAPE of the thinning is drawn, never a density: dots per unit
  volume follow n(r), so the count in each shell of thickness dr follows
  n(r) r^2 dr.

HOW THE DOTS ARE PLACED. Each dot's distance is drawn from n(r) r^2 by
inverting its cumulative sum on a fine grid; its direction is uniform on
the sphere. Each dot carries a weight from 0 to 1, the logarithm of the
density at its distance scaled between the density at 100 (0) and at 3
Earth radii (1), so both instruments shade it the same way. The seed, the
dot count and the grid are rendering settings (drawn_exosphere's
defaults), not measurements.

Coordinates are in Earth radii, centred on Earth, in Earth's body frame
(z along the spin axis). The drawing is round, so the frame changes
nothing a visitor sees; it is named so the website turns it like the
belts.

Key functions:
    drawn_exosphere() - the dots as drawn, with the settings below
    density() - n(r) from the rows, atoms per cubic centimetre
    check_dots() - the checks below, as a list of failures

THE CHECKS (check_dots() returns what fails; test_drawings_export.py
plants a fault in each):
- every dot lies between the inner row and EARTH_GEOCORONA_RADII;
- the dots follow the profile: in five shells between the rows, each
  shell's count is the profile's share within a tolerance that allows for
  chance (four standard deviations, or 15 percent, whichever is larger);
- the weights fall outward: each dot's weight is the one its distance
  gives, to the file's rounding.

Run it to print the counts and the checks:
    python earth_exosphere_sampler.py

Consumed by: earth_visualization_shells.py (the exosphere), export_drawings.py,
             test_drawings_export.py

Role: computation
Domain: orrery

Module created: October 17, 2026 with Anthropic's Claude Opus 5.5 (L-410)
"""
import math
import sys

import numpy as np

# One home for the rows this drawing reads.
ROW_NAMES = (
    'EARTH_EXOSPHERE_H_FIT_INNER_RADII',
    'EARTH_EXOSPHERE_H_FIT_OUTER_RADII',
    'EARTH_EXOSPHERE_H_FIT_COEFF_CM3',
    'EARTH_EXOSPHERE_H_FIT_OFFSET_RADII',
    'EARTH_EXOSPHERE_H_FIT_EXPONENT',
    'EARTH_EXOSPHERE_H_OUTER_EXPONENT',
    'EARTH_GEOCORONA_RADII',
)


def rows_from_store():
    """The rows this module reads, from constants_new.py, as a dict."""
    import constants_new
    return {name: float(getattr(constants_new, name)) for name in ROW_NAMES}


def span(rows):
    """(inner, outer) of the drawing, in Earth radii."""
    return (rows['EARTH_EXOSPHERE_H_FIT_INNER_RADII'],
            rows['EARTH_GEOCORONA_RADII'])


def density(r, rows):
    """n(r), atoms per cubic centimetre, r in Earth radii (eq. 7 to the
    fit's outer row, then eq. 9's fall from eq. 7's value there)."""
    c = rows['EARTH_EXOSPHERE_H_FIT_COEFF_CM3']
    a = rows['EARTH_EXOSPHERE_H_FIT_OFFSET_RADII']
    p = rows['EARTH_EXOSPHERE_H_FIT_EXPONENT']
    join = rows['EARTH_EXOSPHERE_H_FIT_OUTER_RADII']
    if r <= join:
        return c * (r + a) ** -p
    q = rows['EARTH_EXOSPHERE_H_OUTER_EXPONENT']
    return c * (join + a) ** -p * (join / r) ** q


def weight(r, rows):
    """0 at the outer edge, 1 at the inner, by the log of the density."""
    inner, outer = span(rows)
    top = math.log(density(inner, rows))
    bottom = math.log(density(outer, rows))
    if top <= bottom:
        return 1.0      # a profile that does not fall: nothing to shade
    w = (math.log(density(r, rows)) - bottom) / (top - bottom)
    return max(0.0, min(1.0, w))


def _cdf(rows, grid):
    """The radii and the cumulative share of dots inside each, from
    n(r) r^2 on a grid of `grid` steps."""
    inner, outer = span(rows)
    r = np.linspace(inner, outer, grid + 1)
    f = np.array([density(x, rows) * x * x for x in r])
    steps = 0.5 * (f[1:] + f[:-1]) * np.diff(r)
    cum = np.concatenate([[0.0], np.cumsum(steps)])
    return r, cum / cum[-1]


def share_between(lo, hi, rows, grid=20000):
    """The profile's share of the dots between radii lo and hi."""
    r, cum = _cdf(rows, grid)
    return float(np.interp(hi, r, cum) - np.interp(lo, r, cum))


def drawn_exosphere(rows=None, seed=410, dots=1500, grid=20000):
    """The exosphere as drawn: {'x', 'y', 'z', 'w', 'settings'}, lists in
    Earth radii and weights 0 to 1.

    The defaults ARE the drawing's settings, in this one place, as the
    belts' sampler keeps its own: the seed, the dot count and the grid
    the distances are drawn from. Rendering settings, not measurements
    (provenance-discipline, Three Kinds of Drawing Number)."""
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


# Five shells between the rows for the profile check: edges in Earth
# radii, the inner and outer rows added at run time. Few enough that
# chance does not move the answer at 1,500 dots.
CHECK_EDGES = (5.0, 10.0, 20.0, 50.0)


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
        failures.append("%d dot(s) lie outside %g to %g Earth radii, e.g. "
                        "at %.2f" % (len(off), inner, outer, off[0]))
    edges = [inner] + [e for e in CHECK_EDGES if inner < e < outer] + [outer]
    for lo, hi in zip(edges[:-1], edges[1:]):
        got = sum(1 for r in radii if lo <= r < hi or (hi == outer and r == hi))
        want = n * share_between(lo, hi, rows)
        allow = max(4.0 * math.sqrt(want), 0.15 * want)
        if abs(got - want) > allow:
            failures.append("the dots do not follow the profile: %d between "
                            "%g and %g Earth radii, where it gives %.0f "
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
    return check_dots(drawn_exosphere(rows, seed), rows)


def main():
    rows = rows_from_store()
    dots = drawn_exosphere(rows)
    inner, outer = span(rows)
    radii = [math.sqrt(x * x + y * y + z * z)
             for x, y, z in zip(dots['x'], dots['y'], dots['z'])]
    print("exosphere: %d dots from %g to %g Earth radii; density %.3g at "
          "%g, %.3g at %g, %.3g at %g atoms per cubic centimetre"
          % (len(radii), inner, outer, density(inner, rows), inner,
             density(rows['EARTH_EXOSPHERE_H_FIT_OUTER_RADII'], rows),
             rows['EARTH_EXOSPHERE_H_FIT_OUTER_RADII'],
             density(outer, rows), outer))
    edges = [inner] + list(CHECK_EDGES) + [outer]
    for lo, hi in zip(edges[:-1], edges[1:]):
        print("  %5g to %5g Earth radii: %4d dots"
              % (lo, hi, sum(1 for r in radii if lo <= r < hi)))
    failures = check_dots(dots, rows)
    for line in failures:
        print("FAIL: " + line)
    print("EXOSPHERE: %s" % ("all checks pass" if not failures
                             else "%d check(s) FAILED" % len(failures)))
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
