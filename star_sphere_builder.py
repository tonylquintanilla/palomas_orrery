"""
star_sphere_builder.py - Build and render celestial sphere for Paloma's Orrery.

Two roles in one file:
  1. BUILDER (offline): Reads Hipparcos VOT + SIMBAD caches, produces
     star_data/star_sphere_vmag35.json. Run standalone: python star_sphere_builder.py
  2. RENDERER (runtime): Imported by palomas_orrery.py to add star background
     and celestial grid traces to Plotly 3D figures. Single function called by
     both plot_objects and animate_objects -- zero parallel-pipeline divergence.

Output:
    star_data/star_sphere_vmag35.json

No network access required -- reads only local cache files.

# Module created: April 2026 with Anthropic's Claude Opus 4.6
# Renderer added: April 13, 2026 with Anthropic's Claude Opus 4.6
# Part of Paloma's Orrery celestial sphere feature
"""

import os
import sys
import json
import pickle
import numpy as np

# ---- Configuration ----

VMAG_LIMIT = 3.5
OUTPUT_DIR = 'star_data'
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'star_sphere_vmag35.json')

# Hipparcos VOT cache -- same files used by planetarium_apparent_magnitude.py
HIP_VOT_CANDIDATES = [
    'hipparcos_data_magnitude.vot',
    'star_data/hipparcos_data_magnitude.vot',
]

# SIMBAD properties cache -- maps HIP IDs to star names/designations
PROPERTIES_PKL = 'star_data/star_properties_magnitude.pkl'

# Earth's axial tilt (obliquity of the ecliptic), J2000
OBLIQUITY_DEG = 23.4393

# Zodiac sign boundaries along the ecliptic, in ecliptic longitude (degrees)
ZODIAC_SIGNS = [
    (0,   'ARI', 'Aries'),
    (30,  'TAU', 'Taurus'),
    (60,  'GEM', 'Gemini'),
    (90,  'CAN', 'Cancer'),
    (120, 'LEO', 'Leo'),
    (150, 'VIR', 'Virgo'),
    (180, 'LIB', 'Libra'),
    (210, 'SCO', 'Scorpius'),
    (240, 'SAG', 'Sagittarius'),
    (270, 'CAP', 'Capricornus'),
    (300, 'AQR', 'Aquarius'),
    (330, 'PSC', 'Pisces'),
]

# Number of points to generate along each great circle
CIRCLE_POINTS = 120


# ---- Helper Functions ----

def find_hipparcos_vot():
    """Locate the Hipparcos VOT cache file."""
    for path in HIP_VOT_CANDIDATES:
        if os.path.exists(path):
            return path
    return None


def equatorial_to_ecliptic_unit_vector(ra_deg, dec_deg):
    """
    Convert equatorial RA/Dec (ICRS, degrees) to a unit vector in
    ecliptic coordinates (the orrery's native frame).

    Ecliptic frame:
      X -> vernal equinox direction (RA=0, Dec=0)
      Y -> ecliptic longitude 90 deg
      Z -> ecliptic north pole

    The rotation is about the X axis by the obliquity angle.
    """
    ra_rad = np.radians(ra_deg)
    dec_rad = np.radians(dec_deg)
    eps = np.radians(OBLIQUITY_DEG)

    # Equatorial unit vector
    eq_x = np.cos(dec_rad) * np.cos(ra_rad)
    eq_y = np.cos(dec_rad) * np.sin(ra_rad)
    eq_z = np.sin(dec_rad)

    # Rotate about X axis by +obliquity (equatorial -> ecliptic)
    ecl_x = eq_x
    ecl_y = eq_y * np.cos(eps) + eq_z * np.sin(eps)
    ecl_z = -eq_y * np.sin(eps) + eq_z * np.cos(eps)

    return float(ecl_x), float(ecl_y), float(ecl_z)


def ecliptic_longitude_to_unit_vector(lon_deg):
    """
    Convert ecliptic longitude (degrees) to unit vector in ecliptic frame.
    These points sit on the ecliptic plane (z=0).
    """
    lon_rad = np.radians(lon_deg)
    return float(np.cos(lon_rad)), float(np.sin(lon_rad)), 0.0


def generate_great_circle_ecliptic(n_points):
    """
    Generate points along the ecliptic great circle.
    In ecliptic coordinates, this is simply the XY plane (z=0).
    """
    angles = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
    points = []
    for a in angles:
        points.append([round(float(np.cos(a)), 6),
                        round(float(np.sin(a)), 6),
                        0.0])
    return points


def generate_great_circle_equator(n_points):
    """
    Generate points along the celestial equator in ecliptic coordinates.
    The celestial equator is tilted by -obliquity relative to the ecliptic.
    """
    eps = np.radians(OBLIQUITY_DEG)
    angles = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
    points = []
    for a in angles:
        # Equatorial circle in equatorial frame: (cos a, sin a, 0)
        eq_x = np.cos(a)
        eq_y = np.sin(a)
        eq_z = 0.0
        # Rotate to ecliptic frame
        ecl_x = eq_x
        ecl_y = eq_y * np.cos(eps) + eq_z * np.sin(eps)
        ecl_z = -eq_y * np.sin(eps) + eq_z * np.cos(eps)
        points.append([round(float(ecl_x), 6),
                        round(float(ecl_y), 6),
                        round(float(ecl_z), 6)])
    return points


def generate_great_circle_prime_meridian(n_points):
    """
    Generate points along the RA=0h / RA=12h great circle in ecliptic coordinates.
    This is the prime meridian of right ascension -- passes through the vernal
    equinox (RA=0h) and autumnal equinox (RA=12h) and both celestial poles.

    In equatorial coordinates this circle lies in the XZ plane (y=0).
    """
    eps = np.radians(OBLIQUITY_DEG)
    angles = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
    points = []
    for a in angles:
        # Circle in equatorial XZ plane: (cos a, 0, sin a)
        eq_x = np.cos(a)
        eq_y = 0.0
        eq_z = np.sin(a)
        # Rotate to ecliptic frame
        ecl_x = eq_x
        ecl_y = eq_y * np.cos(eps) + eq_z * np.sin(eps)
        ecl_z = -eq_y * np.sin(eps) + eq_z * np.cos(eps)
        points.append([round(float(ecl_x), 6),
                        round(float(ecl_y), 6),
                        round(float(ecl_z), 6)])
    return points


def load_simbad_names():
    """
    Load star designations from the SIMBAD properties cache.
    Returns dict mapping 'HIP NNNNN' -> star_name (e.g. '* alf Ori').
    """
    if not os.path.exists(PROPERTIES_PKL):
        print(f"  SIMBAD cache not found: {PROPERTIES_PKL}")
        print("  Stars will use HIP ID as designation.")
        return {}

    print(f"Loading SIMBAD properties from: {PROPERTIES_PKL}")
    with open(PROPERTIES_PKL, 'rb') as f:
        data = pickle.load(f)

    names = {}
    if isinstance(data, dict) and 'unique_ids' in data:
        uids = data['unique_ids']
        star_names = data.get('star_names', [])
        for i, uid in enumerate(uids):
            if i < len(star_names) and star_names[i]:
                names[uid] = str(star_names[i])
    elif isinstance(data, dict):
        for uid, props in data.items():
            if isinstance(props, dict) and 'star_name' in props:
                names[uid] = str(props['star_name'])

    print(f"  Loaded {len(names)} star designations.")
    return names


def build_star_data(vot_path, simbad_names):
    """
    Build the star array from Hipparcos VOT data.
    
    Returns (stars, hip_to_index) where:
      stars: list of [x, y, z, vmag, designation] arrays
      hip_to_index: dict mapping HIP number (int) to index in stars list
    Unit vectors are in ecliptic coordinates.
    """
    from astropy.table import Table

    print(f"\nLoading Hipparcos data from: {vot_path}")
    data = Table.read(vot_path, format='votable')
    print(f"  Total entries in VOT: {len(data)}")

    # Find RA/Dec columns
    ra_col = dec_col = None
    for c in ['RAICRS', 'RA_ICRS']:
        if c in data.colnames:
            ra_col = c
            break
    for c in ['DEICRS', 'DE_ICRS']:
        if c in data.colnames:
            dec_col = c
            break

    if ra_col is None or dec_col is None:
        print("ERROR: Cannot find RA/Dec columns.")
        print(f"  Available: {data.colnames}")
        return [], {}

    ra_deg = np.array(data[ra_col], dtype=float)
    dec_deg = np.array(data[dec_col], dtype=float)
    vmag = np.array(data['Vmag'], dtype=float)

    # HIP IDs for name lookup
    hip_ids = data['HIP'] if 'HIP' in data.colnames else None

    # Filter
    valid = np.isfinite(vmag) & np.isfinite(ra_deg) & np.isfinite(dec_deg) & (vmag <= VMAG_LIMIT)
    print(f"  Stars with vmag <= {VMAG_LIMIT}: {np.sum(valid)}")

    # Build stars with HIP tracking for constellation centroid lookup
    stars_with_hip = []  # (star_entry, hip_number_or_None)
    named_count = 0
    for i in range(len(data)):
        if not valid[i]:
            continue

        # Convert equatorial RA/Dec to ecliptic unit vector
        ux, uy, uz = equatorial_to_ecliptic_unit_vector(ra_deg[i], dec_deg[i])

        # Look up designation
        designation = ''
        hip_num = None
        if hip_ids is not None and not np.ma.is_masked(hip_ids[i]):
            hip_num = int(hip_ids[i])
            hip_key = f"HIP {hip_num}"
            if hip_key in simbad_names:
                designation = simbad_names[hip_key]
                named_count += 1
            else:
                designation = hip_key

        entry = [
            round(ux, 6),
            round(uy, 6),
            round(uz, 6),
            round(float(vmag[i]), 2),
            designation
        ]
        stars_with_hip.append((entry, hip_num))

    # Sort by vmag (brightest first)
    stars_with_hip.sort(key=lambda s: s[0][3])

    # Separate into stars list and HIP->index map
    stars = []
    hip_to_index = {}
    for idx, (entry, hip_num) in enumerate(stars_with_hip):
        stars.append(entry)
        if hip_num is not None:
            hip_to_index[hip_num] = idx

    print(f"  Stars with SIMBAD designations: {named_count}")
    print(f"  Stars with HIP-only fallback: {len(stars) - named_count}")
    print(f"  HIP-to-index map: {len(hip_to_index)} entries")

    return stars, hip_to_index


def build_grid_data():
    """
    Build celestial grid data: ecliptic, equator, poles, zodiac labels.
    All positions are unit vectors in ecliptic coordinates.
    """
    print("\nBuilding celestial grid data...")

    grid = {}

    # Ecliptic great circle (z=0 plane in ecliptic coords)
    grid['ecliptic'] = generate_great_circle_ecliptic(CIRCLE_POINTS)

    # Celestial equator (tilted by obliquity)
    grid['equator'] = generate_great_circle_equator(CIRCLE_POINTS)

    # Prime meridian (RA=0h / RA=12h great circle)
    grid['prime_meridian'] = generate_great_circle_prime_meridian(CIRCLE_POINTS)

    # Ecliptic poles
    grid['ecliptic_north_pole'] = [0.0, 0.0, 1.0]
    grid['ecliptic_south_pole'] = [0.0, 0.0, -1.0]

    # Celestial poles (equatorial poles in ecliptic coordinates)
    eps = np.radians(OBLIQUITY_DEG)
    # North celestial pole: equatorial (0, 0, 1) -> ecliptic
    ncp_x = 0.0
    ncp_y = round(float(np.sin(eps)), 6)
    ncp_z = round(float(np.cos(eps)), 6)
    grid['celestial_north_pole'] = [ncp_x, ncp_y, ncp_z]
    grid['celestial_south_pole'] = [ncp_x, -ncp_y, -ncp_z]

    # Vernal equinox (RA=0, Dec=0 -> ecliptic X axis)
    grid['vernal_equinox'] = [1.0, 0.0, 0.0]

    # Zodiac labels: position + label + degrees
    zodiac_labels = []
    for lon_deg, abbr, full_name in ZODIAC_SIGNS:
        # Place label at the midpoint of each 30-degree segment
        mid_lon = lon_deg + 15
        ux, uy, uz = ecliptic_longitude_to_unit_vector(mid_lon)
        zodiac_labels.append({
            'x': round(ux, 6),
            'y': round(uy, 6),
            'z': round(uz, 6),
            'abbr': abbr,
            'name': full_name,
            'lon_deg': lon_deg,
        })
    grid['zodiac_labels'] = zodiac_labels

    # Degree markers along ecliptic (every 30 degrees at boundaries)
    # These are tick diamonds -- always visible when grid is on
    degree_markers = []
    for lon_deg in range(0, 360, 30):
        ux, uy, uz = ecliptic_longitude_to_unit_vector(lon_deg)
        degree_markers.append({
            'x': round(ux, 6),
            'y': round(uy, 6),
            'z': round(uz, 6),
            'deg': lon_deg,
            'label': f"{lon_deg}\u00b0",
        })
    grid['degree_markers'] = degree_markers

    # Equator tick markers (every 30 deg = every 2h of RA)
    # Tick diamonds along equator -- always visible when grid is on
    eps = np.radians(OBLIQUITY_DEG)
    equator_tick_markers = []
    for i in range(12):
        ra_deg = i * 30.0  # 0, 30, 60, ... 330 degrees
        ra_h = i * 2       # 0h, 2h, 4h, ... 22h
        ra_rad = np.radians(ra_deg)
        # Equatorial: (cos ra, sin ra, 0) -> rotate to ecliptic
        eq_x = np.cos(ra_rad)
        eq_y = np.sin(ra_rad)
        ecl_x = eq_x
        ecl_y = eq_y * np.cos(eps)
        ecl_z = -eq_y * np.sin(eps)
        equator_tick_markers.append({
            'x': round(float(ecl_x), 6),
            'y': round(float(ecl_y), 6),
            'z': round(float(ecl_z), 6),
            'label': f"{ra_h}h",
        })
    grid['equator_tick_markers'] = equator_tick_markers

    # Prime meridian tick markers (every 30 deg of declination arc)
    # The PM circle goes through RA=0h (VE), NCP, RA=12h, SCP
    # In equatorial frame: (cos dec, 0, sin dec) for RA=0h half,
    # continues through RA=12h half for negative dec visual continuity.
    # We place 12 ticks at 30-deg arc intervals around the full circle.
    pm_tick_markers = []
    for i in range(12):
        arc_deg = i * 30.0  # 0, 30, 60, ... 330 around the circle
        arc_rad = np.radians(arc_deg)
        # Circle in equatorial XZ plane: (cos a, 0, sin a)
        eq_x = np.cos(arc_rad)
        eq_z = np.sin(arc_rad)
        ecl_x = eq_x
        ecl_y = eq_z * np.sin(eps)
        ecl_z = eq_z * np.cos(eps)
        # Map arc position to Dec label:
        # arc 0=VE(0deg), 90=NCP(+90deg), 180=AE(0deg), 270=SCP(-90deg)
        if arc_deg <= 90:
            dec_val = arc_deg
        elif arc_deg <= 180:
            dec_val = 180 - arc_deg
        elif arc_deg <= 270:
            dec_val = -(arc_deg - 180)
        else:
            dec_val = -(360 - arc_deg)
        dec_int = int(round(dec_val))
        if dec_int > 0:
            label = f"+{dec_int}\u00b0"
        elif dec_int < 0:
            label = f"{dec_int}\u00b0"
        else:
            # 0 deg appears at VE (arc 0) and AE (arc 180)
            label = "0\u00b0" if arc_deg < 90 else "0\u00b0"
        pm_tick_markers.append({
            'x': round(float(ecl_x), 6),
            'y': round(float(ecl_y), 6),
            'z': round(float(ecl_z), 6),
            'label': label,
            'arc_deg': arc_deg,
        })
    grid['pm_tick_markers'] = pm_tick_markers

    # RA hour markers -- dense labels (hovertext when Labels checkbox is on)
    # Same positions as equator_tick_markers but with full hover info
    ra_hour_markers = []
    for i in range(12):
        ra_deg = i * 30.0
        ra_h = i * 2
        ra_rad = np.radians(ra_deg)
        eq_x = np.cos(ra_rad)
        eq_y = np.sin(ra_rad)
        ecl_x = eq_x
        ecl_y = eq_y * np.cos(eps)
        ecl_z = -eq_y * np.sin(eps)
        ra_hour_markers.append({
            'x': round(float(ecl_x), 6),
            'y': round(float(ecl_y), 6),
            'z': round(float(ecl_z), 6),
            'label': f"RA {ra_h}h",
            'ra_h': ra_h,
        })
    grid['ra_hour_markers'] = ra_hour_markers

    # Dec degree markers -- dense labels (hovertext when Labels checkbox is on)
    # 7 points on the prime meridian at Dec = 0, +/-30, +/-60, +/-90
    dec_degree_markers = []
    for dec_deg_val in [0, 30, 60, 90, -30, -60, -90]:
        dec_rad = np.radians(dec_deg_val)
        # On RA=0h meridian in equatorial: (cos dec, 0, sin dec)
        eq_x = np.cos(dec_rad)
        eq_z = np.sin(dec_rad)
        ecl_x = eq_x
        ecl_y = eq_z * np.sin(eps)
        ecl_z = eq_z * np.cos(eps)
        if dec_deg_val > 0:
            label = f"Dec +{dec_deg_val}\u00b0"
        elif dec_deg_val < 0:
            label = f"Dec {dec_deg_val}\u00b0"
        else:
            label = "Dec 0\u00b0 (VE)"
        dec_degree_markers.append({
            'x': round(float(ecl_x), 6),
            'y': round(float(ecl_y), 6),
            'z': round(float(ecl_z), 6),
            'label': label,
            'dec_deg': dec_deg_val,
        })
    grid['dec_degree_markers'] = dec_degree_markers

    print(f"  Ecliptic: {len(grid['ecliptic'])} points")
    print(f"  Equator: {len(grid['equator'])} points")
    print(f"  Prime meridian: {len(grid['prime_meridian'])} points")
    print(f"  Zodiac labels: {len(grid['zodiac_labels'])}")
    print(f"  Degree markers (ecliptic): {len(grid['degree_markers'])}")
    print(f"  Equator ticks: {len(grid['equator_tick_markers'])}")
    print(f"  PM ticks: {len(grid['pm_tick_markers'])}")
    print(f"  RA hour markers: {len(grid['ra_hour_markers'])}")
    print(f"  Dec degree markers: {len(grid['dec_degree_markers'])}")
    print(f"  Obliquity: {OBLIQUITY_DEG}\u00b0")

    return grid


# ---- Constellation Data (Stellarium Western Sky Culture, GPLv2+) ----
# Each constellation maps to a list of line segments as HIP ID pairs.
# Stars not in the vmag 3.5 set are silently skipped at build time.
#
# Credit: Stellarium project (stellarium.org)
# Asterism data added: April 2026 with Anthropic's Claude Opus 4.6

CONSTELLATION_NAMES = {
    'AND': 'Andromeda', 'ANT': 'Antlia', 'APS': 'Apus',
    'AQR': 'Aquarius', 'AQL': 'Aquila', 'ARA': 'Ara',
    'ARI': 'Aries', 'AUR': 'Auriga', 'BOO': 'Bootes',
    'CAE': 'Caelum', 'CAM': 'Camelopardalis', 'CNC': 'Cancer',
    'CVN': 'Canes Venatici', 'CMA': 'Canis Major', 'CMI': 'Canis Minor',
    'CAP': 'Capricornus', 'CAR': 'Carina', 'CAS': 'Cassiopeia',
    'CEN': 'Centaurus', 'CEP': 'Cepheus', 'CET': 'Cetus',
    'CHA': 'Chamaeleon', 'CIR': 'Circinus', 'COL': 'Columba',
    'COM': 'Coma Berenices', 'CRA': 'Corona Australis', 'CRB': 'Corona Borealis',
    'CRV': 'Corvus', 'CRT': 'Crater', 'CRU': 'Crux',
    'CYG': 'Cygnus', 'DEL': 'Delphinus', 'DOR': 'Dorado',
    'DRA': 'Draco', 'EQU': 'Equuleus', 'ERI': 'Eridanus',
    'FOR': 'Fornax', 'GEM': 'Gemini', 'GRU': 'Grus',
    'HER': 'Hercules', 'HOR': 'Horologium', 'HYA': 'Hydra',
    'HYI': 'Hydrus', 'IND': 'Indus', 'LAC': 'Lacerta',
    'LEO': 'Leo', 'LMI': 'Leo Minor', 'LEP': 'Lepus',
    'LIB': 'Libra', 'LUP': 'Lupus', 'LYN': 'Lynx',
    'LYR': 'Lyra', 'MEN': 'Mensa', 'MIC': 'Microscopium',
    'MON': 'Monoceros', 'MUS': 'Musca', 'NOR': 'Norma',
    'OCT': 'Octans', 'OPH': 'Ophiuchus', 'ORI': 'Orion',
    'PAV': 'Pavo', 'PEG': 'Pegasus', 'PER': 'Perseus',
    'PHE': 'Phoenix', 'PIC': 'Pictor', 'PSC': 'Pisces',
    'PSA': 'Piscis Austrinus', 'PUP': 'Puppis', 'PYX': 'Pyxis',
    'RET': 'Reticulum', 'SGE': 'Sagitta', 'SGR': 'Sagittarius',
    'SCO': 'Scorpius', 'SCL': 'Sculptor', 'SCT': 'Scutum',
    'SER': 'Serpens', 'SEX': 'Sextans', 'TAU': 'Taurus',
    'TEL': 'Telescopium', 'TRI': 'Triangulum', 'TRA': 'Triangulum Australe',
    'TUC': 'Tucana', 'UMA': 'Ursa Major', 'UMI': 'Ursa Minor',
    'VEL': 'Vela', 'VIR': 'Virgo', 'VOL': 'Volans', 'VUL': 'Vulpecula',
}

def build_centroid_data(stars, hip_to_index):
    """
    Build constellation centroid data: brightness-weighted centroid positions
    for each constellation that has at least one star in the vmag set.

    Used for constellation name labels. No line segment data.

    Returns dict: abbr -> {name, centroid, star_count}
    """
    print("\nBuilding constellation centroid data...")

    centroids = {}
    total_with_centroid = 0

    # Collect all HIP IDs per constellation from CONSTELLATION_NAMES
    # We check every star in our set to see if its Bayer designation
    # matches a constellation abbreviation
    # Actually simpler: iterate stars and check which constellations
    # have members via hip_to_index. But we don't have a constellation
    # membership map -- we only have CONSTELLATION_NAMES (abbr->full name).
    #
    # The SIMBAD designation format "* alf Ori"
    # contains the constellation abbreviation as the last 3 characters.
    # We can parse this to build constellation membership.

    # Build constellation -> star indices mapping from designations
    const_members = {}  # abbr -> list of star indices
    for idx, star in enumerate(stars):
        desig = star[4] if len(star) > 4 else ''
        if desig and desig.startswith('* '):
            # Parse "* alf Ori" -> "Ori" -> "ORI"
            parts = desig.split()
            if len(parts) >= 3:
                const_abbr = parts[-1].upper()
                # Map 3-letter abbreviation variants
                # Most SIMBAD abbrs match IAU, but check edge cases
                if const_abbr in CONSTELLATION_NAMES:
                    if const_abbr not in const_members:
                        const_members[const_abbr] = []
                    const_members[const_abbr].append(idx)

    for abbr, full_name in sorted(CONSTELLATION_NAMES.items()):
        member_indices = const_members.get(abbr, [])
        if not member_indices:
            continue

        # Compute brightness-weighted centroid
        wx_sum = wy_sum = wz_sum = w_sum = 0.0
        for idx in member_indices:
            s = stars[idx]
            weight = 10.0 ** (-0.4 * s[3])
            wx_sum += s[0] * weight
            wy_sum += s[1] * weight
            wz_sum += s[2] * weight
            w_sum += weight

        centroid = None
        if w_sum > 0:
            cx = wx_sum / w_sum
            cy = wy_sum / w_sum
            cz = wz_sum / w_sum
            mag = (cx**2 + cy**2 + cz**2) ** 0.5
            if mag > 1e-10:
                centroid = [round(cx/mag, 6), round(cy/mag, 6), round(cz/mag, 6)]

        if centroid:
            centroids[abbr] = {
                'name': full_name,
                'abbr': abbr,
                'centroid': centroid,
                'star_count': len(member_indices),
            }
            total_with_centroid += 1

    print(f"  Constellations with centroid: {total_with_centroid}")
    print(f"  Constellations skipped (no stars in set): "
          f"{len(CONSTELLATION_NAMES) - total_with_centroid}")

    return centroids


def build_json(vot_path):
    """Main build routine."""
    print("=" * 60)
    print("Star Sphere Builder - Paloma's Orrery")
    print("=" * 60)

    # Load SIMBAD names (optional -- falls back to HIP IDs)
    simbad_names = load_simbad_names()

    # Build star data
    stars, hip_to_index = build_star_data(vot_path, simbad_names)
    if not stars:
        print("ERROR: No stars produced. Aborting.")
        return False

    # Build grid data
    grid = build_grid_data()

    # Build constellation centroid data (for name labels)
    constellation_centroids = build_centroid_data(stars, hip_to_index)

    # Assemble output
    output = {
        'meta': {
            'vmag_limit': VMAG_LIMIT,
            'star_count': len(stars),
            'obliquity_deg': OBLIQUITY_DEG,
            'coordinate_frame': 'ecliptic_J2000',
            'source': 'Hipparcos via VizieR VOT cache',
            'format': '[x, y, z, vmag, designation]',
            'notes': 'Unit vectors in ecliptic coordinates. '
                     'Multiply by axis_range to scale at runtime. '
                     'Grid circles are also unit vectors.',
        },
        'stars': stars,
        'grid': grid,
        'constellations': constellation_centroids,
    }

    # Write JSON
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)

    file_size = os.path.getsize(OUTPUT_FILE)
    print(f"\n{'=' * 60}")
    print(f"Output: {OUTPUT_FILE}")
    print(f"  Stars: {len(stars)}")
    print(f"  Constellations with centroid: {len(constellation_centroids)}")
    print(f"  File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
    print(f"  Brightest: {stars[0][4]} (vmag {stars[0][3]})")
    print(f"  Faintest: {stars[-1][4]} (vmag {stars[-1][3]})")
    print(f"{'=' * 60}")

    return True


# ---- Runtime: Cache Loader + Renderer ----
# These functions are called by palomas_orrery.py at runtime.
# They lazy-import plotly so the builder can run standalone without it.
# Module updated: April 13, 2026 with Anthropic's Claude Opus 4.6

_star_sphere_cache = None


def load_star_sphere_data():
    """
    Load celestial sphere JSON data, caching in memory after first load.
    Returns dict with 'stars' and 'grid' keys, or None if file not found.
    """
    global _star_sphere_cache
    if _star_sphere_cache is not None:
        return _star_sphere_cache

    json_path = os.path.join('star_data', 'star_sphere_vmag35.json')
    if not os.path.exists(json_path):
        print(f"[STAR SPHERE] JSON not found: {json_path}", flush=True)
        print(f"[STAR SPHERE] Run star_sphere_builder.py to generate it.", flush=True)
        return None

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            _star_sphere_cache = json.load(f)
        star_count = len(_star_sphere_cache.get('stars', []))
        print(f"[STAR SPHERE] Loaded {star_count} stars from {json_path}", flush=True)
        return _star_sphere_cache
    except Exception as e:
        print(f"[STAR SPHERE] Error loading {json_path}: {e}", flush=True)
        return None


def add_celestial_sphere_traces(fig, axis_range, show_stars, show_names,
                                 show_grid, show_labels,
                                 show_constellation_names=False):
    """
    Add celestial sphere traces to a Plotly 3D figure.

    Called by both plot_objects and animate_objects in palomas_orrery.py.
    One function, zero parallel-pipeline divergence.

    Args:
        fig: plotly.graph_objects.Figure with a 3D scene
        axis_range: [min, max] AU range -- sphere radius = abs(max)
        show_stars: bool -- Star Background checkbox
        show_names: bool -- Star Names sub-checkbox
        show_grid: bool -- Celestial Grid checkbox
        show_labels: bool -- Labels sub-checkbox (dense hover labels)
        show_constellation_names: bool -- Constellation Names sub-checkbox
    """
    import plotly.graph_objects as go

    sphere_data = load_star_sphere_data()
    if sphere_data is None:
        return

    R = abs(axis_range[1])  # Sphere radius = axis range magnitude

    # ---- Star Background ----
    if show_stars:
        stars = sphere_data.get('stars', [])
        if stars:
            sx = [s[0] * R for s in stars]
            sy = [s[1] * R for s in stars]
            sz = [s[2] * R for s in stars]

            # Hover: show designation if star names enabled, skip otherwise
            if show_names:
                hover_texts = [s[4] if len(s) > 4 and s[4] else f'vmag {s[3]}'
                               for s in stars]
                hover_mode = '%{text}<extra></extra>'
                hover_info = None  # use hovertemplate
            else:
                hover_texts = None
                hover_mode = None
                hover_info = 'skip'

            fig.add_trace(go.Scatter3d(
                x=sx, y=sy, z=sz,
                mode='markers',
                marker=dict(
                    size=1.0,
                    color='rgba(180, 195, 230, 0.55)',
                    symbol='circle',
                ),
                text=hover_texts,
                hovertemplate=hover_mode,
                hoverinfo=hover_info,
                showlegend=False,
                name='_star_background'
            ))

    # ---- Celestial Grid ----
    if not show_grid:
        # Even without grid, constellation names may be active
        if show_constellation_names:
            consts = sphere_data.get('constellations', {})
            if consts:
                cx_list, cy_list, cz_list = [], [], []
                name_list = []
                for abbr, info in consts.items():
                    centroid = info.get('centroid')
                    if centroid:
                        cx_list.append(centroid[0] * R * 1.03)
                        cy_list.append(centroid[1] * R * 1.03)
                        cz_list.append(centroid[2] * R * 1.03)
                        name_list.append(info['name'])
                if cx_list:
                    fig.add_trace(go.Scatter3d(
                        x=cx_list, y=cy_list, z=cz_list,
                        mode='markers+text',
                        marker=dict(size=4, color='rgba(180, 195, 230, 0.6)',
                                    symbol='cross',
                                    line=dict(color='white', width=0.5)),
                        text=name_list,
                        textposition='top center',
                        textfont=dict(color='rgba(180, 195, 230, 0.45)', size=8),
                        hovertemplate='%{text}<extra></extra>',
                        showlegend=False,
                        name='_constellation_names',
                    ))
        return

    grid = sphere_data.get('grid', {})

    # Ecliptic great circle (amber)
    ecl_pts = grid.get('ecliptic', [])
    if ecl_pts:
        ecl_closed = ecl_pts + [ecl_pts[0]]
        fig.add_trace(go.Scatter3d(
            x=[p[0] * R for p in ecl_closed],
            y=[p[1] * R for p in ecl_closed],
            z=[p[2] * R for p in ecl_closed],
            mode='lines',
            line=dict(color='rgba(239, 159, 39, 0.45)', width=2),
            hoverinfo='skip',
            showlegend=False,
            name='_ecliptic'
        ))

    # Celestial equator (teal)
    eq_pts = grid.get('equator', [])
    if eq_pts:
        eq_closed = eq_pts + [eq_pts[0]]
        fig.add_trace(go.Scatter3d(
            x=[p[0] * R for p in eq_closed],
            y=[p[1] * R for p in eq_closed],
            z=[p[2] * R for p in eq_closed],
            mode='lines',
            line=dict(color='rgba(93, 202, 165, 0.35)', width=1.5),
            hoverinfo='skip',
            showlegend=False,
            name='_celestial_equator'
        ))

    # Prime meridian (gray)
    pm_pts = grid.get('prime_meridian', [])
    if pm_pts:
        pm_closed = pm_pts + [pm_pts[0]]
        fig.add_trace(go.Scatter3d(
            x=[p[0] * R for p in pm_closed],
            y=[p[1] * R for p in pm_closed],
            z=[p[2] * R for p in pm_closed],
            mode='lines',
            line=dict(color='rgba(180, 180, 180, 0.25)', width=1),
            hoverinfo='skip',
            showlegend=False,
            name='_prime_meridian'
        ))

    # ---- Tick markers (always visible when grid is on) ----
    # + markers at every 30 deg. When Labels is on, ticks carry hovertext.
    # Convention: + markers for non-structural positions signifying hovertext.

    # Ecliptic degree ticks (amber +)
    # Persistent text labels only at quarters: 0 deg, 90 deg, 180 deg, 270 deg
    deg_markers = grid.get('degree_markers', [])
    if deg_markers:
        ecl_quarter_degs = {0, 90, 180, 270}
        fig.add_trace(go.Scatter3d(
            x=[d['x'] * R for d in deg_markers],
            y=[d['y'] * R for d in deg_markers],
            z=[d['z'] * R for d in deg_markers],
            mode='markers+text',
            marker=dict(size=3, color='rgba(239, 159, 39, 0.6)',
                        symbol='cross'),
            text=[d.get('label', f"{d.get('deg', '')}")
                  if d.get('deg', -1) in ecl_quarter_degs else ''
                  for d in deg_markers],
            textfont=dict(color='rgba(239, 159, 39, 0.45)', size=8),
            textposition='top center',
            customdata=[d.get('label', f"{d.get('deg', '')}") for d in deg_markers] if show_labels else None,
            hovertemplate='%{customdata}<extra></extra>' if show_labels else None,
            hoverinfo=None if show_labels else 'skip',
            showlegend=False,
            name='_degree_markers'
        ))

    # Equator ticks (teal +)
    # Persistent text labels only at quarters: 0h, 6h, 12h, 18h
    eq_ticks = grid.get('equator_tick_markers', [])
    if eq_ticks:
        eq_quarter_hours = {'0h', '6h', '12h', '18h'}
        fig.add_trace(go.Scatter3d(
            x=[t['x'] * R for t in eq_ticks],
            y=[t['y'] * R for t in eq_ticks],
            z=[t['z'] * R for t in eq_ticks],
            mode='markers+text',
            marker=dict(size=3, color='rgba(93, 202, 165, 0.5)',
                        symbol='cross'),
            text=[t['label'] if t['label'] in eq_quarter_hours else ''
                  for t in eq_ticks],
            textfont=dict(color='rgba(93, 202, 165, 0.4)', size=8),
            textposition='top center',
            customdata=[t['label'] for t in eq_ticks] if show_labels else None,
            hovertemplate='%{customdata}<extra></extra>' if show_labels else None,
            hoverinfo=None if show_labels else 'skip',
            showlegend=False,
            name='_equator_ticks'
        ))

    # Prime meridian ticks (gray +)
    # Persistent text labels only at quarters: 0 deg (VE), +90 deg (NCP), 0 deg (AE), -90 deg (SCP)
    pm_ticks = grid.get('pm_tick_markers', [])
    if pm_ticks:
        pm_quarter_arcs = {0.0, 90.0, 180.0, 270.0}
        fig.add_trace(go.Scatter3d(
            x=[t['x'] * R for t in pm_ticks],
            y=[t['y'] * R for t in pm_ticks],
            z=[t['z'] * R for t in pm_ticks],
            mode='markers+text',
            marker=dict(size=2.5, color='rgba(180, 180, 180, 0.4)',
                        symbol='cross'),
            text=[t['label'] if t.get('arc_deg', -1) in pm_quarter_arcs else ''
                  for t in pm_ticks],
            textfont=dict(color='rgba(180, 180, 180, 0.35)', size=7),
            textposition='top center',
            customdata=[t['label'] for t in pm_ticks] if show_labels else None,
            hovertemplate='%{customdata}<extra></extra>' if show_labels else None,
            hoverinfo=None if show_labels else 'skip',
            showlegend=False,
            name='_pm_ticks'
        ))

    # ---- Fixed markers (always visible) ----

    # Vernal equinox
    ve = grid.get('vernal_equinox')
    if ve:
        fig.add_trace(go.Scatter3d(
            x=[ve[0] * R], y=[ve[1] * R], z=[ve[2] * R],
            mode='markers+text',
            marker=dict(size=6, color='rgba(239, 159, 39, 0.8)',
                        symbol='cross', line=dict(color='white', width=1)),
            text=['VE'],
            textfont=dict(color='rgba(239, 159, 39, 0.7)', size=9),
            textposition='top center',
            hoverinfo='skip',
            showlegend=False,
            name='_vernal_equinox'
        ))

    # Celestial poles (abbreviation always, full name on hover when dense)
    ncp = grid.get('celestial_north_pole')
    scp = grid.get('celestial_south_pole')
    if ncp and scp:
        pole_hover = None
        pole_hinfo = 'skip'
        pole_tpl = None
        if show_labels:
            pole_hover = ['North Celestial Pole (NCP)',
                          'South Celestial Pole (SCP)']
            pole_hinfo = None
            pole_tpl = '%{text}<extra></extra>'
        fig.add_trace(go.Scatter3d(
            x=[ncp[0] * R, scp[0] * R],
            y=[ncp[1] * R, scp[1] * R],
            z=[ncp[2] * R, scp[2] * R],
            mode='markers+text',
            marker=dict(size=5, color='rgba(93, 202, 165, 0.7)',
                        symbol='cross', line=dict(color='white', width=1)),
            text=['NCP', 'SCP'],
            textfont=dict(color='rgba(93, 202, 165, 0.6)', size=9),
            textposition='top center',
            customdata=pole_hover,
            hovertemplate=pole_tpl if show_labels else None,
            hoverinfo=pole_hinfo,
            showlegend=False,
            name='_celestial_poles'
        ))

    # Ecliptic poles
    enp = grid.get('ecliptic_north_pole')
    esp = grid.get('ecliptic_south_pole')
    if enp and esp:
        epole_hover = None
        epole_hinfo = 'skip'
        epole_tpl = None
        if show_labels:
            epole_hover = ['North Ecliptic Pole (NEP)',
                           'South Ecliptic Pole (SEP)']
            epole_hinfo = None
            epole_tpl = '%{text}<extra></extra>'
        fig.add_trace(go.Scatter3d(
            x=[enp[0] * R, esp[0] * R],
            y=[enp[1] * R, esp[1] * R],
            z=[enp[2] * R, esp[2] * R],
            mode='markers+text',
            marker=dict(size=4, color='rgba(239, 159, 39, 0.5)',
                        symbol='cross'),
            text=['NEP', 'SEP'],
            textfont=dict(color='rgba(239, 159, 39, 0.4)', size=8),
            textposition='top center',
            customdata=epole_hover,
            hovertemplate=epole_tpl if show_labels else None,
            hoverinfo=epole_hinfo,
            showlegend=False,
            name='_ecliptic_poles'
        ))

    # ---- Dense labels (only when Labels checkbox is on) ----
    if show_labels:
        # Zodiac constellation names along ecliptic (amber +, at midpoints 1.03R)
        # These need their own markers because they're at 15 deg, 45 deg, etc.
        # -- not at the 30 deg tick positions.
        zodiac = grid.get('zodiac_labels', [])
        if zodiac:
            fig.add_trace(go.Scatter3d(
                x=[z['x'] * R * 1.03 for z in zodiac],
                y=[z['y'] * R * 1.03 for z in zodiac],
                z=[z['z'] * R * 1.03 for z in zodiac],
                mode='markers',
                marker=dict(size=4, color='rgba(239, 159, 39, 0.4)',
                            symbol='cross'),
                text=[z['name'] for z in zodiac],
                hovertemplate='%{text}<extra></extra>',
                showlegend=False,
                name='_zodiac_labels'
            ))

    # RA hour and Dec degree labels are NOT separate traces --
    # the equator and PM tick markers carry this hovertext via customdata
    # when show_labels is on. No duplicate markers needed.

    # ---- Constellation names (persistent text at centroids) ----
    if show_constellation_names:
        consts = sphere_data.get('constellations', {})
        if consts:
            cx_list, cy_list, cz_list = [], [], []
            name_list = []
            for abbr, info in consts.items():
                centroid = info.get('centroid')
                if centroid:
                    # Place at 1.03R (slightly outside sphere, like zodiac labels)
                    cx_list.append(centroid[0] * R * 1.03)
                    cy_list.append(centroid[1] * R * 1.03)
                    cz_list.append(centroid[2] * R * 1.03)
                    name_list.append(info['name'])

            if cx_list:
                # Persistent text labels + cross marker for hover
                fig.add_trace(go.Scatter3d(
                    x=cx_list, y=cy_list, z=cz_list,
                    mode='markers+text',
                    marker=dict(size=4, color='rgba(180, 195, 230, 0.6)',
                                symbol='cross',
                                line=dict(color='white', width=0.5)),
                    text=name_list,
                    textposition='top center',
                    textfont=dict(color='rgba(180, 195, 230, 0.45)', size=8),
                    hovertemplate='%{text}<extra></extra>',
                    showlegend=False,
                    name='_constellation_names',
                ))


if __name__ == '__main__':
    vot_path = find_hipparcos_vot()
    if vot_path is None:
        print("ERROR: Hipparcos VOT cache not found.")
        print("Expected locations:")
        for p in HIP_VOT_CANDIDATES:
            print(f"  {p}")
        print("\nRun planetarium_apparent_magnitude.py first to generate the cache,")
        print("or place the VOT file in one of the above locations.")
        sys.exit(1)

    success = build_json(vot_path)
    sys.exit(0 if success else 1)
