"""
galactic_tide_sampler.py - where the galaxy's tide sends comets in from:
dots in the outer Oort cloud about the galaxy's pole, placed once from a
seed, sparse at the galaxy's plane and at its poles, thickest halfway.

The drawing was solar_visualization_shells.create_sun_galactic_tide's
own, drawn afresh on every plot (L-406, L-420, L-421). Now it is a
stored drawing, as the Hills cloud is (Tony's rulings of 2026-10-20,
talks 2 and 5, L-434): placed once here, drawn as given by the orrery
window and by the website, so the phone shows the orrery's own dots.
The pink double cone is NOT stored: it is a few served numbers and a
formula, so each instrument works it out from the rows.

HOW THE DOTS ARE PLACED (every distance and the pole is a row in
constants_new.py):
- The plane. Dots are placed about the north galactic pole of J2000,
  GALACTIC_NORTH_POLE_RA_J2000_DEG and _DEC_J2000_DEG, and turned into
  the drawing's frame, the ecliptic of J2000, by
  pole_frames.create_pole_transformation_matrix, as a planet's pole is.
- The density. Dots per piece of sky go as |sin b cos b|, b the galactic
  latitude: none at the plane or the poles, most halfway between, where
  sin b equals cos b. Drawing sin b evenly gives every piece of sky the
  same chance; keeping a draw with probability |sin 2b| (at most 1,
  halfway) makes the count go as |sin b cos b|. The sources are in the comments beside the code.
- The distance. Evenly in distance from INNER_OORT_DISK_OUTER_AU to
  OUTER_OORT_CLOUD_AU, kept with the outer cloud's band chance
  (outer_oort_sampler.band_keep): thin at the near end, full by
  INNER_OORT_CLOUD_AU.
- Each dot stands for the far end of an orbit. Where any real comet is,
  is not known and is not claimed.
- The count (Tony's look of 2026-10-06) and the seed are drawing
  choices, not measurements (drawn_tide's defaults).

THE CHECKS (check_dots() returns what fails; test_drawings_export.py
plants a fault in each):
- the edges: every dot between INNER_OORT_DISK_OUTER_AU and
  OUTER_OORT_CLOUD_AU, to the stored file's rounding (whole AU);
- the band: the dots in four distance shells follow the band's rule;
- the tilt: each dot's galactic latitude is worked out about the pole
  as its rows give it, by a second construction (the pole's RA and Dec
  turned to the ecliptic by the obliquity row, not the matrix above),
  and the dots in five latitude shells must follow |sin b cos b|. Dots
  drawn about a pole tilted away from the rows' fill the shells near
  the plane and the poles, and fail.
Each shell's allowance is the check's own setting (_allow): four
standard deviations of chance, or a fixed share of the expected count,
whichever is larger.

Pure Python and numpy: no Plotly, no Tk.

Key functions:
    drawn_tide() - the dots as drawn, with the settings above
    pole_vector() - the galactic pole in the drawing frame, from its rows
    check_dots() - the three checks above, as a list of failures

Run it to print where the dots fall and the checks:
    python galactic_tide_sampler.py

Consumed by: solar_visualization_shells.py (create_sun_galactic_tide),
             export_drawings.py, test_drawings_export.py

Role: computation
Domain: orrery

Module created: October 22, 2026 with Anthropic's Claude Opus 5.5 (L-434,
with L-239: the tide's dots placed once from a seed, by the rule of
solar_visualization_shells.create_sun_galactic_tide, which now draws
them from here)
"""
import math
import sys

import numpy as np

from outer_oort_sampler import band_keep
from pole_frames import create_pole_transformation_matrix

ROW_NAMES = (
    'INNER_OORT_DISK_OUTER_AU', 'INNER_OORT_CLOUD_AU', 'OUTER_OORT_CLOUD_AU',
    'GALACTIC_NORTH_POLE_RA_J2000_DEG', 'GALACTIC_NORTH_POLE_DEC_J2000_DEG',
    'EARTH_OBLIQUITY_J2000_DEG',
)

# The check's distance shells (AU) are the rows' own edges, and two
# points between them chosen to split each part (a rendering of the
# check, not a claim); its latitude shells are in |sin b|.
CHECK_SIN_B_EDGES = (0.0, 0.2, 0.4, 0.6, 0.8, 1.0)


def rows_from_store():
    """The rows this module reads, from constants_new.py, as a dict."""
    import constants_new
    return {name: getattr(constants_new, name) for name in ROW_NAMES}


def sample_tide(rows, n_points, seed):
    """The dots, in AU, in the drawing frame, as arrays x, y, z."""
    rng = np.random.default_rng(seed)
    m = np.asarray(create_pole_transformation_matrix(
        rows['GALACTIC_NORTH_POLE_RA_J2000_DEG'],
        rows['GALACTIC_NORTH_POLE_DEC_J2000_DEG']), dtype=float)

    # Source: Matese and Whitmire, "Persistent Evidence of a Jovian Mass
    #   Solar Companion in the Oort Cloud", arXiv:1004.4584, sec. 2.2 --
    #   the dominant disk tidal term goes as |sin B cos B| (Matese et al.
    #   1999), so if the tide dominates, the aphelia of new comets avoid
    #   the galactic poles and equator and peak near B = +/-45 degrees.
    # Source: Delsemme, "Galactic tides affect the Oort cloud: an
    #   observational confirmation", A&A 187, 913 (1987), summary -- the
    #   aphelia of 152 comets with periods over ten thousand years avoid
    #   the two galactic polar caps and a strip along the galactic equator.
    # Note: not everyone reads it this way. Higuchi, "Anisotropy of
    #   Long-period Comets Explained by Their Formation Process",
    #   arXiv:2008.04324 (AJ 160, 134), explains the same depletions by
    #   comets gathering near the ecliptic and a second plane; and Rickman
    #   et al. (2008), as Matese and Whitmire report, take the term to go
    #   as |sin B|.
    # (Moved here with the drawing from create_sun_galactic_tide, L-434.)
    sin_b = np.empty(0)
    while sin_b.size < n_points:
        u = rng.uniform(-1.0, 1.0, 2 * n_points)
        keep = rng.uniform(0.0, 1.0, u.size) < 2.0 * np.abs(u) * np.sqrt(1.0 - u * u)
        sin_b = np.concatenate([sin_b, u[keep]])
    sin_b = sin_b[:n_points]
    cos_b = np.sqrt(1.0 - sin_b * sin_b)
    lon = rng.uniform(0.0, 2.0 * np.pi, n_points)

    lo = float(rows['INNER_OORT_DISK_OUTER_AU'])
    hi = float(rows['OUTER_OORT_CLOUD_AU'])
    r = np.empty(0)
    while r.size < n_points:
        draw = rng.uniform(lo, hi, 2 * n_points)
        r = np.concatenate([r, draw[rng.uniform(0.0, 1.0, draw.size)
                                    < band_keep(draw, rows)]])
    r = r[:n_points]

    galactic = np.vstack([r * cos_b * np.cos(lon),
                          r * cos_b * np.sin(lon),
                          r * sin_b])
    x, y, z = m @ galactic
    return {'x': x, 'y': y, 'z': z}


def drawn_tide(rows=None, n_points=5000, seed=434):
    """The tide as drawn, in the orrery window and on the website, from a
    fixed seed, so every plot and the exported file hold the same dots.
    The two settings are drawing choices, written only here: 5,000 dots
    after Tony's look of 2026-10-06, and the seed, the ledger handle that
    made it fixed. Every caller takes the defaults. The returned dict also
    carries them, as 'settings'."""
    rows = rows_from_store() if rows is None else rows
    dots = sample_tide(rows, n_points, seed)
    dots['settings'] = {'dots': n_points, 'seed': seed}
    return dots


def pole_vector(rows):
    """The north galactic pole as a unit vector in the drawing frame (the
    ecliptic of J2000), built from its RA and Dec rows and the obliquity
    row directly -- not by the matrix the dots are placed with, so the
    tilt check is a second construction, not the first one re-run."""
    ra = math.radians(rows['GALACTIC_NORTH_POLE_RA_J2000_DEG'])
    dec = math.radians(rows['GALACTIC_NORTH_POLE_DEC_J2000_DEG'])
    eq = (math.cos(dec) * math.cos(ra), math.cos(dec) * math.sin(ra),
          math.sin(dec))
    eps = math.radians(rows['EARTH_OBLIQUITY_J2000_DEG'])
    return np.array([eq[0],
                     eq[1] * math.cos(eps) + eq[2] * math.sin(eps),
                     -eq[1] * math.sin(eps) + eq[2] * math.cos(eps)])


def _band_share(a, b, rows):
    """Share of the dots between a and b AU by the band's rule: the chance
    of a distance goes as band_keep, evenly in distance."""
    near = float(rows['INNER_OORT_DISK_OUTER_AU'])
    full = float(rows['INNER_OORT_CLOUD_AU'])
    far = float(rows['OUTER_OORT_CLOUD_AU'])

    def area(x):        # integral of band_keep from near to x
        x = min(max(x, near), far)
        if x <= full:
            return (x - near) ** 2 / (2.0 * (full - near))
        return (full - near) / 2.0 + (x - full)
    return (area(b) - area(a)) / area(far)


def _sin_b_share(t0, t1):
    """Share of the dots with t0 <= |sin b| < t1 when the count goes as
    |sin b cos b|: the cumulative share below t is 1 - (1 - t^2)^(3/2)."""
    def cum(t):
        return 1.0 - (1.0 - t * t) ** 1.5
    return cum(t1) - cum(t0)


def _allow(want):
    return max(4.0 * math.sqrt(want), 0.15 * want)


def check_dots(dots, rows, slack_au=1.0):
    """Failures for a set of drawn dots, as sentences. slack_au allows for
    the stored file's rounding of each coordinate to the whole AU."""
    failures = []
    xyz = np.vstack([np.asarray(dots['x'], dtype=float),
                     np.asarray(dots['y'], dtype=float),
                     np.asarray(dots['z'], dtype=float)])
    n = xyz.shape[1]
    if not n:
        return ['no dots to check']
    r = np.sqrt((xyz ** 2).sum(axis=0))
    near = float(rows['INNER_OORT_DISK_OUTER_AU'])
    full = float(rows['INNER_OORT_CLOUD_AU'])
    far = float(rows['OUTER_OORT_CLOUD_AU'])
    off = r[(r < near - slack_au) | (r > far + slack_au)]
    if off.size:
        failures.append("edges: %d dot(s) lie outside %g to %g AU, e.g. at "
                        "%.0f AU" % (off.size, near, far, off[0]))
    edges = (near, (near + full) / 2.0, full, (full + far) / 2.0, far)
    for a, b in zip(edges[:-1], edges[1:]):
        got = int(((r >= a) & (r < b)).sum())
        if a == near:
            got += int((r < near).sum())
        if b == far:
            got += int((r >= far).sum())
        want = n * _band_share(a, b, rows)
        if abs(got - want) > _allow(want):
            failures.append("band: %d dots between %.0f and %.0f AU, where "
                            "the band's rule gives %.0f (allowing %.0f)"
                            % (got, a, b, want, _allow(want)))
    sin_b = np.abs(pole_vector(rows) @ xyz) / np.where(r > 0, r, 1.0)
    for t0, t1 in zip(CHECK_SIN_B_EDGES[:-1], CHECK_SIN_B_EDGES[1:]):
        got = int(((sin_b >= t0) & ((sin_b < t1) | (t1 == 1.0))).sum())
        want = n * _sin_b_share(t0, t1)
        if abs(got - want) > _allow(want):
            failures.append("tilt: %d dots with |sin b| from %.1f to %.1f "
                            "about the galactic pole as its rows give it, "
                            "where |sin b cos b| gives %.0f (allowing %.0f)"
                            % (got, t0, t1, want, _allow(want)))
    return failures


def main():
    rows = rows_from_store()
    dots = drawn_tide(rows)
    r = np.sqrt(np.asarray(dots['x']) ** 2 + np.asarray(dots['y']) ** 2
                + np.asarray(dots['z']) ** 2)
    print("tide: %d dots, seed %d; nearest %.0f AU, farthest %.0f AU "
          "(thin from %s AU, full by %s AU, to %s AU)"
          % (r.size, dots['settings']['seed'], r.min(), r.max(),
             rows['INNER_OORT_DISK_OUTER_AU'], rows['INNER_OORT_CLOUD_AU'],
             rows['OUTER_OORT_CLOUD_AU']))
    pole = pole_vector(rows)
    m = np.asarray(create_pole_transformation_matrix(
        rows['GALACTIC_NORTH_POLE_RA_J2000_DEG'],
        rows['GALACTIC_NORTH_POLE_DEC_J2000_DEG']), dtype=float)
    print("  the pole two ways: %.6f deg apart (the matrix's z axis and the "
          "rows turned by the obliquity)"
          % math.degrees(math.acos(min(1.0, float(pole @ m[:, 2])))))
    failures = check_dots(dots, rows)
    for line in failures:
        print("FAIL: " + line)
    print("TIDE: %s" % ("all checks pass" if not failures
                        else "%d check(s) FAILED" % len(failures)))
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
