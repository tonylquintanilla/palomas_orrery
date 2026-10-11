"""
hills_cloud_sampler.py - the Hills cloud (the inner Oort cloud) as dots
along orbits, following Nesvorny et al. (2025), Fig. 3.

The paper finds the inner Oort cloud a slightly warped disk, tilted about
30 degrees to the ecliptic and nearly upright to the galaxy's plane, with
two spiral arms (arXiv:2502.11252v1, sec. 1, p. 3). This module draws it
the way the paper explains it: each dot is a body on an orbit, and the
tilt and the arms come out of where the orbits lie, not from a shape laid
on by hand. Tony's ruling of 2026-10-10: "follow the paper. Draw following
figure 3 and describe following the text. And cite everything."

HOW THE DOTS ARE PLACED (every number is a row in constants_new.py):
- Each orbit's plane is picked where Fig. 3's dots are: a cell of the
  reading HILLS_CLOUD_PLANES_READ, chosen with a chance in proportion to its
  count, then a point evenly inside it (galactic nodal longitude and
  galactic inclination).
- Its argument of perihelion is picked evenly in one of the two bands the
  Fig. 2 caption gives (the two arms), half the orbits in each.
- Its far end (aphelion) is picked evenly between the cloud's inner edge
  (INNER_LIMIT_OORT_CLOUD_AU) and the near end of the band
  (INNER_OORT_DISK_OUTER_AU), and across the band with a chance falling
  evenly to nothing at its far end (INNER_OORT_CLOUD_AU): so the disk is
  full to the band and thins out across it, from the orbit sample alone.
- Every orbit has the eccentricity HILLS_CLOUD_ECCENTRICITY, a declared
  pick. Dots go along each orbit evenly in TIME, so they gather at the
  far ends, where a body spends most of its time, and that is where the
  arms show. Dots near an orbit's near end can fall inside the cloud's
  inner edge, as a real body on that orbit would.
- The galactic angles are turned into the drawing's frame, the ecliptic
  of J2000, by the matrix pole_frames.create_pole_transformation_matrix
  builds about the north galactic pole (the rows the galactic tide is
  drawn about), after turning the paper's longitudes so that the
  ecliptic's ascending node sits at ECLIPTIC_NODE_GALACTIC_LON_DEG.

THE CHECKS (check() returns what fails; test_hills_cloud_sampler.py runs
it and shows each check failing on a planted fault):
- The frame: Sgr A*, from its rows, must fall within a degree of galactic
  longitude 0 and latitude 0, where the frame puts the galaxy's centre.
- The reading: most of Fig. 3's dots must fall inside the ranges its
  caption gives, as the caption says they do.
- The tilt: the plane through the dots must lie within 10 degrees of
  HILLS_CLOUD_TILT_DEG, the paper's "about 30". The tilt is printed, never
  set.

Pure Python and numpy: no Plotly, no Tk. The gallery's builder computes
served geometry in Python too, so this module can be carried there; which
way the gallery takes it is the gallery session's decision.

Key functions:
    sample_hills_cloud() - the dots, in AU, in the drawing frame
    describe() - what a sample looks like: counts, tilt, arms
    check() - the three checks above, as a list of failures

Run it to print the description and the checks:
    python hills_cloud_sampler.py

Consumed by: solar_visualization_shells.py (create_sun_hills_cloud_torus),
             test_hills_cloud_sampler.py

Role: computation
Domain: orrery

Module updated: October 10, 2026 with Anthropic's Claude Opus 5.5 (L-421)
"""
import math

import numpy as np

from pole_frames import create_pole_transformation_matrix

ROW_NAMES = (
    'INNER_LIMIT_OORT_CLOUD_AU', 'INNER_OORT_DISK_OUTER_AU',
    'INNER_OORT_CLOUD_AU', 'HILLS_CLOUD_TILT_DEG',
    'ECLIPTIC_NODE_GALACTIC_LON_DEG',
    'HILLS_CLOUD_PERI_ARG_BAND1_LOW_DEG', 'HILLS_CLOUD_PERI_ARG_BAND1_HIGH_DEG',
    'HILLS_CLOUD_PERI_ARG_BAND2_LOW_DEG', 'HILLS_CLOUD_PERI_ARG_BAND2_HIGH_DEG',
    'HILLS_CLOUD_NODE_LOW_DEG', 'HILLS_CLOUD_NODE_HIGH_DEG',
    'HILLS_CLOUD_INCL_GAL_LOW_DEG', 'HILLS_CLOUD_INCL_GAL_HIGH_DEG',
    'HILLS_CLOUD_PLANES_NODE_CELL_DEG', 'HILLS_CLOUD_PLANES_INCL_CELL_DEG',
    'HILLS_CLOUD_PLANES_READ', 'HILLS_CLOUD_ECCENTRICITY',
    'GALACTIC_NORTH_POLE_RA_J2000_DEG', 'GALACTIC_NORTH_POLE_DEC_J2000_DEG',
    'SGR_A_STAR_RA_ICRS_DEG', 'SGR_A_STAR_DEC_ICRS_DEG',
    'EARTH_OBLIQUITY_J2000_DEG',
)

def rows_from_store():
    """The rows this module reads, from constants_new.py, as a dict."""
    import constants_new
    return {name: getattr(constants_new, name) for name in ROW_NAMES}


def galactic_matrix(rows):
    """3x3 matrix: a vector in galactic coordinates (x toward longitude 0,
    z toward the north galactic pole) into the drawing frame.

    The pole matrix's x axis is the ascending node of the galactic equator
    on the ecliptic, where the ecliptic's own ascending node on the
    galactic plane sits at longitude 180. So a galactic longitude l is
    longitude l - (node - 180) in that matrix's frame.
    """
    pole = np.asarray(create_pole_transformation_matrix(
        rows['GALACTIC_NORTH_POLE_RA_J2000_DEG'],
        rows['GALACTIC_NORTH_POLE_DEC_J2000_DEG']), dtype=float)
    turn = math.radians(rows['ECLIPTIC_NODE_GALACTIC_LON_DEG'] - 180.0)
    c, s = math.cos(turn), math.sin(turn)
    spin = np.array([[c, s, 0.0], [-s, c, 0.0], [0.0, 0.0, 1.0]])
    return pole @ spin


def _cells(rows):
    keys, counts = [], []
    for key, count in rows['HILLS_CLOUD_PLANES_READ'].items():
        node, incl = (float(part) for part in key.split(','))
        keys.append((node, incl))
        counts.append(float(count))
    counts = np.array(counts)
    return keys, counts / counts.sum()


def _aphelia(n, inner, near, far, rng):
    """Evenly from inner to near, then a chance falling evenly to nothing
    at far: inverse of the cumulative share of that shape."""
    flat = near - inner
    ramp = (far - near) / 2.0
    u = rng.random(n) * (flat + ramp)
    v = np.maximum(u - flat, 0.0)
    return np.where(u < flat, inner + u,
                    far - np.sqrt(np.maximum((far - near) ** 2
                                             - 2.0 * v * (far - near), 0.0)))


def _eccentric_anomaly(mean_anomaly, e):
    big_e = mean_anomaly + e * np.sin(mean_anomaly)
    for _ in range(50):
        big_e = big_e - ((big_e - e * np.sin(big_e) - mean_anomaly)
                         / (1.0 - e * np.cos(big_e)))
    return big_e


def sample_hills_cloud(n_orbits, points_per_orbit, rows=None, seed=None):
    """The dots: n_orbits orbits, points_per_orbit dots on each. How many
    is a rendering setting, so the drawing code that calls this passes it
    (create_sun_hills_cloud_torus draws 600 x 6 = 3,600, the torus's
    count). Returns a dict: x, y, z (AU, drawing frame, one entry per
    dot), and per orbit: node_deg, incl_deg, peri_arg_deg, aphelion_au,
    band (1 or 2), normal (3 x n, unit, drawing frame)."""
    rows = rows_from_store() if rows is None else rows
    rng = np.random.default_rng(seed)
    keys, weights = _cells(rows)
    node_cell = rows['HILLS_CLOUD_PLANES_NODE_CELL_DEG']
    incl_cell = rows['HILLS_CLOUD_PLANES_INCL_CELL_DEG']
    pick = rng.choice(len(keys), size=n_orbits, p=weights)
    node = np.array([keys[k][0] for k in pick]) + rng.uniform(0, node_cell, n_orbits)
    incl = np.array([keys[k][1] for k in pick]) + rng.uniform(0, incl_cell, n_orbits)

    band = np.where(rng.random(n_orbits) < 0.5, 1, 2)
    lo = np.where(band == 1, rows['HILLS_CLOUD_PERI_ARG_BAND1_LOW_DEG'],
                  rows['HILLS_CLOUD_PERI_ARG_BAND2_LOW_DEG'])
    hi = np.where(band == 1, rows['HILLS_CLOUD_PERI_ARG_BAND1_HIGH_DEG'],
                  rows['HILLS_CLOUD_PERI_ARG_BAND2_HIGH_DEG'])
    peri = lo + rng.random(n_orbits) * (hi - lo)

    e = float(rows['HILLS_CLOUD_ECCENTRICITY'])
    aphelion = _aphelia(n_orbits, float(rows['INNER_LIMIT_OORT_CLOUD_AU']),
                        float(rows['INNER_OORT_DISK_OUTER_AU']),
                        float(rows['INNER_OORT_CLOUD_AU']), rng)
    a = aphelion / (1.0 + e)

    mean_anomaly = rng.uniform(0, 2 * np.pi, (n_orbits, points_per_orbit))
    big_e = _eccentric_anomaly(mean_anomaly, e)
    in_x = a[:, None] * (np.cos(big_e) - e)
    in_y = a[:, None] * math.sqrt(1.0 - e * e) * np.sin(big_e)

    om, w, i = np.radians(node), np.radians(peri), np.radians(incl)
    co, so, cw, sw, ci, si = (np.cos(om), np.sin(om), np.cos(w), np.sin(w),
                              np.cos(i), np.sin(i))
    p_vec = np.array([co * cw - so * sw * ci, so * cw + co * sw * ci, sw * si])
    q_vec = np.array([-co * sw - so * cw * ci, -so * sw + co * cw * ci, cw * si])
    normal = np.array([so * si, -co * si, ci])
    galactic = (p_vec[:, :, None] * in_x[None] + q_vec[:, :, None] * in_y[None])
    m = galactic_matrix(rows)
    x, y, z = m @ galactic.reshape(3, -1)
    return {'x': x, 'y': y, 'z': z, 'node_deg': node, 'incl_deg': incl,
            'peri_arg_deg': peri, 'aphelion_au': aphelion, 'band': band,
            'normal': m @ normal, 'aphelion_dir': m @ (-p_vec)}


def plane_tilt_deg(x, y, z):
    """Tilt to the ecliptic of the plane through the dots: the plane whose
    normal is the direction they spread least along."""
    pts = np.vstack([x, y, z])
    moment = pts @ pts.T / pts.shape[1]
    _values, vectors = np.linalg.eigh(moment)
    normal = vectors[:, 0]
    return math.degrees(math.acos(min(1.0, abs(normal[2]))))


def sgr_a_galactic(rows):
    """Sgr A*'s galactic longitude and latitude in the frame
    galactic_matrix builds, from its ICRF rows; longitude wrapped to
    -180..180. Both are checked: a wrong pole can put the longitude near
    0 by chance, as swapping the pole's RA and Dec does, but not the
    latitude too."""
    ra = math.radians(rows['SGR_A_STAR_RA_ICRS_DEG'])
    dec = math.radians(rows['SGR_A_STAR_DEC_ICRS_DEG'])
    eq = np.array([math.cos(dec) * math.cos(ra), math.cos(dec) * math.sin(ra),
                   math.sin(dec)])
    eps = math.radians(rows['EARTH_OBLIQUITY_J2000_DEG'])
    ecl = np.array([eq[0], eq[1] * math.cos(eps) + eq[2] * math.sin(eps),
                    -eq[1] * math.sin(eps) + eq[2] * math.cos(eps)])
    gal = galactic_matrix(rows).T @ ecl
    lon = math.degrees(math.atan2(gal[1], gal[0]))
    lat = math.degrees(math.asin(max(-1.0, min(1.0, gal[2]))))
    return (lon + 180.0) % 360.0 - 180.0, lat


def caption_share(rows):
    """Share of Fig. 3's dots, as read, inside its caption's ranges."""
    total = inside = 0.0
    n_cell = rows['HILLS_CLOUD_PLANES_NODE_CELL_DEG']
    i_cell = rows['HILLS_CLOUD_PLANES_INCL_CELL_DEG']
    for key, count in rows['HILLS_CLOUD_PLANES_READ'].items():
        node, incl = (float(part) for part in key.split(','))
        total += count
        if (rows['HILLS_CLOUD_NODE_LOW_DEG'] <= node
                and node + n_cell <= rows['HILLS_CLOUD_NODE_HIGH_DEG']
                and rows['HILLS_CLOUD_INCL_GAL_LOW_DEG'] <= incl
                and incl + i_cell <= rows['HILLS_CLOUD_INCL_GAL_HIGH_DEG']):
            inside += count
    return inside / total


def _lon_lat(vec):
    vec = vec / np.linalg.norm(vec)
    return (math.degrees(math.atan2(vec[1], vec[0])) % 360.0,
            math.degrees(math.asin(max(-1.0, min(1.0, vec[2])))))


def describe(sample, rows=None):
    """What a sample looks like, as a dict, every figure computed."""
    rows = rows_from_store() if rows is None else rows
    incl_ecl = np.degrees(np.arccos(np.clip(sample['normal'][2], -1, 1)))
    incl_ecl = np.minimum(incl_ecl, 180.0 - incl_ecl)
    arms = {}
    for band in (1, 2):
        dirs = sample['aphelion_dir'][:, sample['band'] == band]
        arms[band] = _lon_lat(dirs.sum(axis=1))
    r = np.sqrt(sample['x'] ** 2 + sample['y'] ** 2 + sample['z'] ** 2)
    return {
        'orbits': int(sample['band'].size),
        'dots': int(sample['x'].size),
        'plane_tilt_deg': plane_tilt_deg(sample['x'], sample['y'], sample['z']),
        'orbit_tilt_mean_deg': float(incl_ecl.mean()),
        'orbit_tilt_spread_deg': float(incl_ecl.std()),
        'arm_1_lon_lat_deg': arms[1],
        'arm_2_lon_lat_deg': arms[2],
        'dots_inside_inner_edge': float((r < rows['INNER_LIMIT_OORT_CLOUD_AU']).mean()),
        'dots_beyond_band_near_end': float((r > rows['INNER_OORT_DISK_OUTER_AU']).mean()),
        'sgr_a_galactic_lon_lat_deg': sgr_a_galactic(rows),
        'fig3_share_in_caption': caption_share(rows),
    }


def check(rows=None, seed=421, frame_tolerance_deg=1.0, tilt_tolerance_deg=10.0):
    """The three checks, as a list of failure sentences (empty: all pass),
    and the description they were judged on, from 4,000 orbits so the
    tilt barely moves between runs. The two tolerances are the checks'
    own settings, not read from a source: a degree is well above how far
    the paper's rounded node row moves Sgr A* (main() prints where it
    falls), and the tilt tolerance holds the paper's "about" while still
    catching a frame or a reading gone wrong."""
    rows = rows_from_store() if rows is None else rows
    failures = []
    info = describe(sample_hills_cloud(4000, 6, rows, seed=seed), rows)
    lon, lat = info['sgr_a_galactic_lon_lat_deg']
    if abs(lon) > frame_tolerance_deg or abs(lat) > frame_tolerance_deg:
        failures.append('frame: Sgr A* falls at galactic longitude %.2f, '
                        'latitude %.2f deg, not within %.0f deg of 0, 0 -- '
                        'the pole rows or the node row are wrong'
                        % (lon, lat, frame_tolerance_deg))
    if info['fig3_share_in_caption'] <= 0.5:
        failures.append('reading: only %.0f%% of Fig. 3\'s dots, as read, fall '
                        'inside its caption\'s ranges; the caption says most '
                        'do -- the reading is misplaced'
                        % (100 * info['fig3_share_in_caption']))
    if abs(info['plane_tilt_deg'] - rows['HILLS_CLOUD_TILT_DEG']) > tilt_tolerance_deg:
        failures.append('tilt: the dots\' plane is tilted %.1f deg to the '
                        'ecliptic, not within %.0f deg of the paper\'s %s'
                        % (info['plane_tilt_deg'], tilt_tolerance_deg,
                           rows['HILLS_CLOUD_TILT_DEG']))
    return failures, info


def main():
    rows = rows_from_store()
    drawn = describe(sample_hills_cloud(600, 6, rows), rows)
    print('Hills cloud, as drawn: %d orbits, %d dots' % (drawn['orbits'], drawn['dots']))
    failures, info = check(rows)
    print('Judged on a larger sample (%d orbits, %d dots):' % (info['orbits'], info['dots']))
    print('  plane through the dots: tilted %.1f deg to the ecliptic '
          '(the paper: about %s)' % (info['plane_tilt_deg'], rows['HILLS_CLOUD_TILT_DEG']))
    print('  the orbits\' own tilts: mean %.1f deg, spread %.1f deg'
          % (info['orbit_tilt_mean_deg'], info['orbit_tilt_spread_deg']))
    for band in (1, 2):
        lon, lat = info['arm_%d_lon_lat_deg' % band]
        print('  arm %d (omega_G %s-%s deg): toward ecliptic longitude %.0f, '
              'latitude %.0f deg' % (
                  band, rows['HILLS_CLOUD_PERI_ARG_BAND%d_LOW_DEG' % band],
                  rows['HILLS_CLOUD_PERI_ARG_BAND%d_HIGH_DEG' % band], lon, lat))
    print('  dots inside the inner edge: %.0f%%; beyond the band\'s near end: %.0f%%'
          % (100 * info['dots_inside_inner_edge'], 100 * info['dots_beyond_band_near_end']))
    print('  frame: Sgr A* at galactic longitude %.2f, latitude %.2f deg'
          % info['sgr_a_galactic_lon_lat_deg'])
    print('  reading: %.0f%% of Fig. 3\'s dots inside its caption\'s ranges'
          % (100 * info['fig3_share_in_caption']))
    if failures:
        for line in failures:
            print('FAIL: ' + line)
        return 1
    print('PASS: frame, reading and tilt')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
