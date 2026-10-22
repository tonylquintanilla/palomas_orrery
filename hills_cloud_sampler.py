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
- Its far end (aphelion) is picked with a chance rising evenly from
  nothing at the cloud's inner edge (INNER_LIMIT_OORT_CLOUD_AU, the low
  end of the inner edge's range) to full at the range's high end
  (OORT_CLOUD_INNER_EDGE_HIGH_AU), even from there to the near end of the
  band (INNER_OORT_DISK_OUTER_AU), and falling evenly to nothing at the
  band's far end (INNER_OORT_CLOUD_AU): so the disk fills in across the
  inner edge's range, is full to the band and thins out across it.
  ADDED 2026-10-22 (L-434, Tony's ruling): the inner edge is uncertain,
  thought to lie between those two rows, and an uncertain edge is drawn
  as a cloud across its range; until then the disk was full from 2,000 AU
  and a sphere marked the edge.
- Every orbit has the eccentricity HILLS_CLOUD_ECCENTRICITY, a declared
  pick. Dots go along each orbit evenly in TIME, so they gather at the
  far ends, where a body spends most of its time, and that is where the
  arms show. Across the inner edge's range a dot is kept with the same
  rising chance at its own distance, drawn again along its orbit until
  kept, so the fill-in shows in the dots and not only in the orbits.
  They go only on the part of each orbit inside the cloud,
  no nearer the Sun than its inner edge (INNER_LIMIT_OORT_CLOUD_AU): the
  paper places the inner cloud by distance from the Sun (sec. 1, p. 2,
  the row INNER_OORT_DISK_OUTER_AU), so no dot is drawn closer in.
  FIXED 2026-10-21 (L-460): until then dots near an orbit's near end
  fell inside the edge, to 257 AU, which no row allowed; a drawing ends
  where a sourced row says it does (Tony, 2026-10-21).
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
- The edges: every dot between INNER_LIMIT_OORT_CLOUD_AU and
  INNER_OORT_CLOUD_AU (L-460).
- The fill-in: across the inner edge's range, from
  INNER_LIMIT_OORT_CLOUD_AU to OORT_CLOUD_INNER_EDGE_HIGH_AU, the dots in
  four equal shells must rise shell by shell (L-434). Drawn full from the
  low end, as before 2026-10-22, they fall instead.

Pure Python and numpy: no Plotly, no Tk. The gallery's builder computes
served geometry in Python too, so this module can be carried there; which
way the gallery takes it is the gallery session's decision.

THE DRAWING, ONE PLACE FOR ITS SETTINGS (L-421, 2026-10-11). The orrery
window and the website draw the same dots. drawn_hills_cloud() is the
drawing: 600 orbits of 6 dots, from a fixed seed, its settings written
once, as drawn_hills_cloud()'s defaults, so every plot shows the same
cloud. The orrery's
shell builder calls it, and export_drawings.py writes its dots to
data/drawings/hills_cloud.json, which the website pulls and draws (Tony's
ruling of 2026-10-11, option A: the website draws the orrery's dots, it
does not re-sample them). Before this the orrery drew fresh random dots
on every plot (L-239). The three settings are drawing choices, not
measurements.

Key functions:
    sample_hills_cloud() - the dots, in AU, in the drawing frame
    drawn_hills_cloud() - the dots as drawn, with the settings above
    describe() - what a sample looks like: counts, tilt, arms
    check() - the three checks above, as a list of failures

Run it to print the description and the checks:
    python hills_cloud_sampler.py

Consumed by: solar_visualization_shells.py (create_sun_hills_cloud_torus),
             export_drawings.py, test_drawings_export.py,
             test_hills_cloud_sampler.py

Role: computation
Domain: orrery

Module updated: October 10, 2026 with Anthropic's Claude Opus 5.5 (L-421)
Module updated: October 11, 2026 with Anthropic's Claude Opus 5.5 (L-421,
the website half: drawn_hills_cloud() and its three settings, so the
orrery and the website draw the same seeded dots)
Module updated: October 21, 2026 with Anthropic's Claude Opus 5.5 (L-460:
dots only on the part of each orbit inside the cloud's inner edge, still
evenly in time there; a fourth check, the edges, that every dot lies
between the inner edge and INNER_OORT_CLOUD_AU)
Module updated: October 22, 2026 with Anthropic's Claude Opus 5.5 (L-434,
Tony's ruling that an uncertain edge is drawn as a cloud across its
range: the disk fills in across the inner edge's range, from
INNER_LIMIT_OORT_CLOUD_AU to OORT_CLOUD_INNER_EDGE_HIGH_AU, in the
orbits' far ends and in the dots, fill_in(); the sphere that marked the
edge is gone. A fifth check, the fill-in.)
"""
import math

import numpy as np

from pole_frames import create_pole_transformation_matrix

ROW_NAMES = (
    'INNER_LIMIT_OORT_CLOUD_AU', 'OORT_CLOUD_INNER_EDGE_HIGH_AU',
    'INNER_OORT_DISK_OUTER_AU',
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


def _aphelia(n, inner, full, near, far, rng):
    """A chance rising evenly from nothing at inner to full at full, even
    to near, then falling evenly to nothing at far: inverse of the
    cumulative share of that trapezoid. L-434 (2026-10-22): the rise
    across the inner edge's range is new; with full == inner it is the
    earlier shape exactly."""
    rise = (full - inner) / 2.0
    flat = near - full
    fall = (far - near) / 2.0
    u = rng.random(n) * (rise + flat + fall)
    w = np.maximum(u - rise - flat, 0.0)
    up = inner + np.sqrt(np.maximum(2.0 * u * (full - inner), 0.0))
    mid = full + (u - rise)
    down = far - np.sqrt(np.maximum((far - near) ** 2
                                    - 2.0 * w * (far - near), 0.0))
    return np.where(u < rise, up, np.where(u < rise + flat, mid, down))


def fill_in(r, rows):
    """Chance of keeping a dot at distance r across the inner edge's
    range (L-434): nothing at INNER_LIMIT_OORT_CLOUD_AU, rising evenly to
    all of them at OORT_CLOUD_INNER_EDGE_HIGH_AU, and all of them beyond."""
    lo = float(rows['INNER_LIMIT_OORT_CLOUD_AU'])
    hi = float(rows['OORT_CLOUD_INNER_EDGE_HIGH_AU'])
    return np.clip((np.asarray(r, dtype=float) - lo) / (hi - lo), 0.0, 1.0)


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
                        float(rows['OORT_CLOUD_INNER_EDGE_HIGH_AU']),
                        float(rows['INNER_OORT_DISK_OUTER_AU']),
                        float(rows['INNER_OORT_CLOUD_AU']), rng)
    a = aphelion / (1.0 + e)

    # L-460: evenly in time, but only on the part of the orbit no nearer
    # the Sun than the cloud's inner edge. r = a (1 - e cos E) >= r_in
    # where cos E <= (1 - r_in / a) / e; E0 is where that starts, and the
    # mean anomaly M0 = E0 - e sin E0. A whole orbit outside the edge has
    # E0 = 0, so nothing changes for it.
    r_in = float(rows['INNER_LIMIT_OORT_CLOUD_AU'])
    big_e0 = np.arccos(np.clip((1.0 - r_in / a) / e, -1.0, 1.0))
    m0 = big_e0 - e * np.sin(big_e0)
    share = rng.uniform(0, 1, (n_orbits, points_per_orbit))
    mean_anomaly = m0[:, None] + share * (2 * np.pi - 2 * m0[:, None])
    big_e = _eccentric_anomaly(mean_anomaly, e)
    # L-434 (2026-10-22): across the inner edge's range a dot is kept with
    # fill_in's chance at its distance; one not kept is drawn again along
    # its own orbit, evenly in time on the same part, until kept, so the
    # count is unchanged. An orbit always reaches past the range's high
    # end or close to it, so this ends; the cap is a guard, never reached
    # in the drawing or the check.
    pending = np.ones(big_e.shape, dtype=bool)
    span_m = np.broadcast_to(2 * np.pi - 2 * m0[:, None], big_e.shape)
    start_m = np.broadcast_to(m0[:, None], big_e.shape)
    semi = np.broadcast_to(a[:, None], big_e.shape)
    for _ in range(100000):
        idx = np.nonzero(pending)
        r_now = semi[idx] * (1.0 - e * np.cos(big_e[idx]))
        kept = rng.random(r_now.shape) < fill_in(r_now, rows)
        pending[tuple(i[kept] for i in idx)] = False
        if not pending.any():
            break
        idx = np.nonzero(pending)
        mean_anomaly[idx] = start_m[idx] + rng.uniform(0, 1, idx[0].size) * span_m[idx]
        big_e[idx] = _eccentric_anomaly(mean_anomaly[idx], e)
    else:
        raise RuntimeError('hills cloud: dots could not be placed across the '
                           'inner edge\'s range')
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


def drawn_hills_cloud(rows=None, n_orbits=600, points_per_orbit=6, seed=421):
    """The Hills cloud as drawn, in the orrery window and on the website:
    sample_hills_cloud() with the drawing's settings, from a fixed seed,
    so every plot and the exported file hold the same dots. The three
    settings are drawing choices, not measurements, written only here,
    as this module keeps its other settings (check()'s seed and
    tolerances): 600 orbits of 6 dots is the old torus's count (render
    size), and the seed is any fixed number. Every caller takes the
    defaults. The returned dict also carries them, as 'settings'."""
    dots = sample_hills_cloud(n_orbits, points_per_orbit, rows, seed=seed)
    dots['settings'] = {'n_orbits': n_orbits,
                        'points_per_orbit': points_per_orbit, 'seed': seed}
    return dots


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


def edge_failures(sample, rows, slack_au=1.0):
    """The edges check: every dot between the cloud's inner edge
    (INNER_LIMIT_OORT_CLOUD_AU) and the far end of its band
    (INNER_OORT_CLOUD_AU). slack_au allows for the stored file's rounding
    of each coordinate to the whole AU (L-460)."""
    r = np.sqrt(np.asarray(sample['x']) ** 2 + np.asarray(sample['y']) ** 2
                + np.asarray(sample['z']) ** 2)
    lo = rows['INNER_LIMIT_OORT_CLOUD_AU'] - slack_au
    hi = rows['INNER_OORT_CLOUD_AU'] + slack_au
    out = []
    inside = r < lo
    beyond = r > hi
    if inside.any():
        out.append('edges: %d dot(s) inside the cloud\'s inner edge of %s AU, '
                   'the nearest at %.0f AU' % (int(inside.sum()),
                   rows['INNER_LIMIT_OORT_CLOUD_AU'], float(r.min())))
    if beyond.any():
        out.append('edges: %d dot(s) beyond %s AU, the farthest at %.0f AU'
                   % (int(beyond.sum()), rows['INNER_OORT_CLOUD_AU'],
                      float(r.max())))
    return out


def fill_in_failures(sample, rows):
    """The fill-in check (L-434): across the inner edge's range the dots
    in four equal shells rise shell by shell. A list of failure sentences,
    each starting "fill-in:"."""
    lo = float(rows['INNER_LIMIT_OORT_CLOUD_AU'])
    hi = float(rows['OORT_CLOUD_INNER_EDGE_HIGH_AU'])
    r = np.sqrt(np.asarray(sample['x']) ** 2 + np.asarray(sample['y']) ** 2
                + np.asarray(sample['z']) ** 2)
    counts, _edges = np.histogram(r, bins=np.linspace(lo, hi, 5))
    if not all(counts[k] < counts[k + 1] for k in range(len(counts) - 1)):
        return ['fill-in: the dots in four shells from %g to %g AU do not '
                'rise outward: %s' % (lo, hi, ', '.join(str(c) for c in counts))]
    return []


def check(rows=None, seed=421, frame_tolerance_deg=1.0, tilt_tolerance_deg=10.0):
    """The four checks, as a list of failure sentences (empty: all pass),
    and the description they were judged on, from 4,000 orbits so the
    tilt barely moves between runs. The two tolerances are the checks'
    own settings, not read from a source: a degree is well above how far
    the paper's rounded node row moves Sgr A* (main() prints where it
    falls), and the tilt tolerance holds the paper's "about" while still
    catching a frame or a reading gone wrong."""
    rows = rows_from_store() if rows is None else rows
    failures = []
    sample = sample_hills_cloud(4000, 6, rows, seed=seed)
    info = describe(sample, rows)
    failures += edge_failures(sample, rows)
    failures += edge_failures(drawn_hills_cloud(rows), rows)
    failures += fill_in_failures(sample, rows)
    failures += fill_in_failures(drawn_hills_cloud(rows), rows)
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
    drawn = describe(drawn_hills_cloud(rows), rows)
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
    print('PASS: frame, reading, tilt, edges and fill-in')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
