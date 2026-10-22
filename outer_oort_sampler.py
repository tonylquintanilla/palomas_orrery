"""
outer_oort_sampler.py - the outer Oort cloud as a thin scatter of loose
dots with clumps among them, placed once from a seed, between the rows'
edges.

The outer Oort cloud is a rough sphere of icy bodies at the very edge of
the Sun's reach. That it is lumpy is expected from passing stars; where
the lumps are is not known, and no survey has resolved one. So the
drawing is a choice: loose dots through the whole cloud, thin where it
begins and full from where the inner cloud's band ends, and 15 clumps of
50 to 200 dots placed at random among them, to show the cloud is not
smooth. Until 2026-10-22 the orrery placed the clumps afresh on every
plot and the website placed its own (L-239). Now the cloud is a stored
drawing, as the Hills cloud is (Tony's rulings of 2026-10-20, talk 5,
"Confirmed", L-434): placed once here, from a fixed seed, drawn as given
by the orrery window and by the website.

WHY THE LOOSE DOTS (Tony's choice, 2026-10-22). Fifteen clumps alone
never reach where the cloud's row says it begins: placed at random in a
cloud drawn thin at its near end, the nearest landed more than twice as
far out as the row's INNER_OORT_DISK_OUTER_AU. The loose dots fill the cloud as its rows
describe it, so the drawing begins near its row, as the galactic tide's
does, and the clumps are the denser lumps within it.

HOW THE DOTS ARE PLACED (every distance is a row in constants_new.py):
- The band. A distance is picked evenly between where the outer cloud
  begins, INNER_OORT_DISK_OUTER_AU, and its outer edge,
  OUTER_OORT_CLOUD_AU, and kept with the band's chance (band_keep):
  nothing at the near end, rising evenly to all of them by
  INNER_OORT_CLOUD_AU, the band the Hills cloud thins out across.
- A loose dot is placed at such a distance, in a random direction.
- A clump's centre is placed the same way. Its dots are scattered about
  the centre, out to the clump's size, gathered toward the middle (a
  beta distribution), and each is kept only if it lies between the two
  edges, and then with the band's chance at its own distance.
- So no dot lies nearer than INNER_OORT_DISK_OUTER_AU or farther than
  OUTER_OORT_CLOUD_AU, and the cloud is thin at its near end, as its row
  says ("drawn beginning here, thin").
- The number of loose dots, the clumps' count, dots and sizes, the beta
  shape and the seed are drawing choices, not measurements (drawn_cloud's
  defaults). The clumps' settings are the earlier unseeded drawing's,
  unchanged.

WHERE THE NEAREST DOT FALLS. Nothing is kept at INNER_OORT_DISK_OUTER_AU
itself and everything by INNER_OORT_CLOUD_AU, so the nearest dot falls
in that band, by chance, a little past its near end, and never nearer.
main() prints where.

THE CHECKS (check_dots() returns what fails; test_drawings_export.py
plants a fault):
- every dot lies between INNER_OORT_DISK_OUTER_AU and OUTER_OORT_CLOUD_AU,
  to the stored file's rounding (whole AU).

Pure Python and numpy: no Plotly, no Tk.

Key functions:
    band_keep() - the chance of keeping a dot at a distance (the band)
    drawn_cloud() - the dots as drawn, with the settings above
    check_dots() - the check above, as a list of failures

Run it to print where the dots fall and the check:
    python outer_oort_sampler.py

Consumed by: solar_visualization_shells.py (create_sun_outer_oort_clumpy),
             galactic_tide_sampler.py (band_keep), export_drawings.py,
             test_drawings_export.py

Role: computation
Domain: orrery

Module created: October 22, 2026 with Anthropic's Claude Opus 5.5 (L-434,
with L-239: the outer cloud placed once from a seed, its clumps by the
rule of solar_visualization_shells.create_sun_outer_oort_clumpy, with
loose dots through the band on Tony's choice of 2026-10-22; band_keep
moved here from that file's _outer_cloud_keep, unchanged)
"""
import math
import sys

import numpy as np

ROW_NAMES = (
    'INNER_OORT_DISK_OUTER_AU', 'INNER_OORT_CLOUD_AU', 'OUTER_OORT_CLOUD_AU',
)


def rows_from_store():
    """The rows this module reads, from constants_new.py, as a dict."""
    import constants_new
    return {name: getattr(constants_new, name) for name in ROW_NAMES}


def band_keep(distance, rows):
    """Chance of keeping a dot of the round outer cloud at `distance` AU
    (L-421, 2026-10-10): nothing at the band's near end,
    INNER_OORT_DISK_OUTER_AU, rising evenly to all of them at its far end,
    INNER_OORT_CLOUD_AU, and all of them beyond. The Hills cloud thins out
    across the same band, so the two overlap inside it (Tony's ruling of
    2026-10-09, a fuzzy boundary). Moved here unchanged from
    solar_visualization_shells._outer_cloud_keep (L-434)."""
    near = float(rows['INNER_OORT_DISK_OUTER_AU'])
    far = float(rows['INNER_OORT_CLOUD_AU'])
    return np.clip((np.asarray(distance, dtype=float) - near) / (far - near),
                   0.0, 1.0)


def _band_distance(rng, rows):
    """One distance in the band: evenly between the two edges, kept with
    band_keep's chance."""
    lo = float(rows['INNER_OORT_DISK_OUTER_AU'])
    hi = float(rows['OUTER_OORT_CLOUD_AU'])
    r = rng.uniform(lo, hi)
    while rng.random() >= band_keep(r, rows):
        r = rng.uniform(lo, hi)
    return r


def _direction(rng):
    """A direction as the clumps have always been placed: a longitude
    evenly, and a latitude evenly in angle."""
    theta = rng.uniform(0.0, 2.0 * math.pi)
    phi = rng.uniform(-math.pi / 2.0, math.pi / 2.0)
    return (math.cos(phi) * math.cos(theta), math.cos(phi) * math.sin(theta),
            math.sin(phi))


def sample_cloud(rows, seed, n_loose, n_clumps, points_min, points_max,
                 clump_size_min, clump_size_max, beta_a, beta_b):
    """The dots, in AU, centred on the Sun, as lists x, y, z: the loose
    dots first, then the clumps'. The clumps' rule is
    create_sun_outer_oort_clumpy's of 2026-10-10, drawn from one seeded
    generator instead of numpy's shared one."""
    rng = np.random.default_rng(seed)
    lo = float(rows['INNER_OORT_DISK_OUTER_AU'])
    hi = float(rows['OUTER_OORT_CLOUD_AU'])
    xs, ys, zs = [], [], []
    for _ in range(n_loose):
        r = _band_distance(rng, rows)
        ux, uy, uz = _direction(rng)
        xs.append(r * ux)
        ys.append(r * uy)
        zs.append(r * uz)
    for _ in range(n_clumps):
        centre = _band_distance(rng, rows)
        ux, uy, uz = _direction(rng)
        cx, cy, cz = centre * ux, centre * uy, centre * uz
        count = int(rng.integers(points_min, points_max))
        size = rng.uniform(clump_size_min, clump_size_max)
        for _ in range(count):
            r = size * rng.beta(beta_a, beta_b)
            vx, vy, vz = _direction(rng)
            x, y, z = cx + r * vx, cy + r * vy, cz + r * vz
            d = math.sqrt(x * x + y * y + z * z)
            if lo <= d <= hi and rng.random() < band_keep(d, rows):
                xs.append(x)
                ys.append(y)
                zs.append(z)
    return {'x': xs, 'y': ys, 'z': zs}


def drawn_cloud(rows=None, n_loose=1000, n_clumps=15, points_min=50,
                points_max=200, clump_size_min=5000, clump_size_max=15000,
                beta_a=2, beta_b=5, seed=434):
    """The outer cloud as drawn, in the orrery window and on the website,
    from a fixed seed, so every plot and the exported file hold the same
    dots. The settings are drawing choices, not measurements, written
    only here: 1,000 loose dots, fewer than the clumps hold, enough to show the cloud's extent without hiding the clumps (a
    look for Tony to judge); the clumps' count, dots and sizes (AU) and
    the beta shape are the earlier drawing's, unchanged; the seed is the
    ledger handle that made it fixed, as the Hills cloud's is its own.
    Every caller takes the defaults. The returned dict also carries them,
    as 'settings'."""
    rows = rows_from_store() if rows is None else rows
    settings = {'n_loose': n_loose, 'n_clumps': n_clumps,
                'points_min': points_min, 'points_max': points_max,
                'clump_size_min': clump_size_min,
                'clump_size_max': clump_size_max, 'beta_a': beta_a,
                'beta_b': beta_b, 'seed': seed}
    dots = sample_cloud(rows, **settings)
    dots['settings'] = settings
    return dots


def radii(dots):
    return [math.sqrt(x * x + y * y + z * z)
            for x, y, z in zip(dots['x'], dots['y'], dots['z'])]


def check_dots(dots, rows, slack_au=1.0):
    """Failures for a set of drawn dots, as sentences. slack_au allows for
    the stored file's rounding of each coordinate to the whole AU, which
    moves a dot's distance by under one AU."""
    failures = []
    lo = float(rows['INNER_OORT_DISK_OUTER_AU'])
    hi = float(rows['OUTER_OORT_CLOUD_AU'])
    rr = radii(dots)
    if not rr:
        return ['no dots to check']
    inside = [r for r in rr if r < lo - slack_au]
    beyond = [r for r in rr if r > hi + slack_au]
    if inside:
        failures.append("%d dot(s) lie inside %g AU, where the outer cloud's "
                        "row says it begins; the nearest at %.0f AU"
                        % (len(inside), lo, min(inside)))
    if beyond:
        failures.append("%d dot(s) lie beyond %g AU, the cloud's outer edge; "
                        "the farthest at %.0f AU" % (len(beyond), hi,
                                                     max(beyond)))
    return failures


def main():
    rows = rows_from_store()
    dots = drawn_cloud(rows)
    rr = radii(dots)
    s = dots['settings']
    print("outer Oort cloud: %d dots, %d loose and %d in %d clumps, seed %d"
          % (len(rr), s['n_loose'], len(rr) - s['n_loose'], s['n_clumps'],
             s['seed']))
    print("  nearest dot %.0f AU (drawn thin from %s AU, full by %s AU); "
          "farthest %.0f AU (outer edge %s AU)"
          % (min(rr), rows['INNER_OORT_DISK_OUTER_AU'],
             rows['INNER_OORT_CLOUD_AU'], max(rr),
             rows['OUTER_OORT_CLOUD_AU']))
    print("  nearest clump dot %.0f AU" % min(rr[s['n_loose']:]))
    failures = check_dots(dots, rows)
    for line in failures:
        print("FAIL: " + line)
    print("OUTER OORT CLOUD: %s" % ("all checks pass" if not failures
                                    else "%d check(s) FAILED" % len(failures)))
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
