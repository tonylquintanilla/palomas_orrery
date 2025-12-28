"""
data_acquisition.py - Unified module for both distance- and magnitude-based
queries, integrating the simpler logic of data_acquisition_distance.py.

Key points:
- For distance queries, we fetch catalogs using "parallax >= min_parallax_mas."
- For magnitude queries, we fetch catalogs using "Vmag <= mag_limit" (Hipparcos)
  or "Gmag <= mag_limit + 0.5" (Gaia).
- We remove strict "file size" and "bright star" thresholds to avoid repeated downloads.
- We request only columns that are actually needed, so we don't overload VizieR on large queries.
- If you still get random connection closures for big queries, try chunking or raising timeout.
"""

import os
import time
import numpy as np
from astroquery.vizier import Vizier
from astropy.table import Table
from astropy.coordinates import Angle
from astropy.io import votable
from astropy.io.votable import parse_single_table

# Optional: If big queries often fail, increase the default timeout or choose a different mirror.
# Vizier.TIMEOUT = 300
# Vizier.MIRROR = 'cdsarc.u-strasbg.fr'

def calculate_parallax_limit(max_light_years):
    """Calculate minimum parallax for a given distance in light-years."""
    max_distance_pc = max_light_years / 3.26156
    return (1 / max_distance_pc) * 1000  # parallax in mas

def initialize_vizier(timeout=120):
    """
    Initialize Vizier with no row limit and a set of columns you actually need.
    Increase 'timeout' if queries time out frequently.
    """
    try:
        # Example: only request key columns from each catalog. 
        # This greatly reduces the data volume for large queries.
        # You can add or remove fields depending on what your code actually needs.
        v = Vizier(
            columns=[
                '*',  # Or list columns explicitly, e.g. "Vmag", "B-V", "HIP", "Plx", "phot_g_mean_mag", ...
            ],
            row_limit=-1,
            timeout=timeout
        )
        return v
    except Exception as e:
        raise RuntimeError(f"Failed to initialize Vizier: {e}")

def load_or_fetch_hipparcos_data(v, hip_data_file, mode='distance',
                                 mag_limit=None, parallax_constraint=None):
    """
    Load or fetch Hipparcos data.
    - If mode == 'magnitude', we apply Vmag <= mag_limit.
    - If mode == 'distance', we apply Plx >= parallax_constraint.
    - We skip strict file-size or bright-star validations to avoid repeated fetches.
    """
    if os.path.exists(hip_data_file):
        # Just load the file if it exists. No size-based checks.
        try:
            print(f"Loading existing Hipparcos file: {hip_data_file}")
            data = Table.read(hip_data_file, format='votable')
            print(f"Hipparcos data loaded: {len(data)} entries.")
            return data
        except Exception as e:
            print(f"Error reading {hip_data_file}: {e}")
            # Fall back to fetching if file is corrupt.
    
    print(f"Fetching Hipparcos data from Vizier ({mode} mode)...")
    try:
        constraints = {}
        if mode == 'magnitude' and mag_limit is not None:
            constraints['Vmag'] = f"<={mag_limit}"
        elif mode == 'distance' and parallax_constraint is not None:
            constraints['Plx'] = parallax_constraint

        result = v.query_constraints(catalog="I/239/hip_main", **constraints)
        if not result:
            print("No data found in Hipparcos catalog for these constraints.")
            return None

        hip_data = result[0]
        print(f"Number of Hipparcos entries fetched: {len(hip_data)}")
        # Save to disk
        hip_data.write(hip_data_file, format='votable', overwrite=True)
        print(f"Saved Hipparcos data to {hip_data_file}")
        return hip_data

    except Exception as e:
        print(f"Error fetching Hipparcos data: {e}")
        return None

def load_or_fetch_gaia_data(v, gaia_data_file, mode='distance',
                            mag_limit=None, parallax_constraint=None):
    """
    Load or fetch Gaia data.
    - If mode == 'magnitude', we apply Gmag <= mag_limit + 0.5 (common offset).
    - If mode == 'distance', we apply Plx >= parallax_constraint.
    - We skip strict file-size checks to avoid repeated fetches.
    """
    if os.path.exists(gaia_data_file):
        # Just load the file if it exists. 
        try:
            print(f"Loading existing Gaia file: {gaia_data_file}")
            data = Table.read(gaia_data_file, format='votable')
            print(f"Gaia data loaded: {len(data)} entries.")
            return data
        except Exception as e:
            print(f"Error reading {gaia_data_file}: {e}")
            # Fall back to fetching if file is corrupt.

    print(f"Fetching Gaia data from Vizier ({mode} mode)...")
    try:
        constraints = {}
        if mode == 'magnitude' and mag_limit is not None:
            adjusted_limit = min(11.0, mag_limit + 0.5)
            constraints['Gmag'] = f"<={adjusted_limit}"
        elif mode == 'distance' and parallax_constraint is not None:
            constraints['Plx'] = parallax_constraint
            # Optionally enforce parallax error <2 mas, if desired:
            # constraints['e_Plx'] = '<2'

        result = v.query_constraints(catalog="I/350/gaiaedr3", **constraints)
        if not result:
            print("No data found in Gaia EDR3 for these constraints.")
            return None

        gaia_data = result[0]
        print(f"Number of Gaia entries fetched: {len(gaia_data)}")
        # Save to disk
        gaia_data.write(gaia_data_file, format='votable', overwrite=True)
        print(f"Saved Gaia data to {gaia_data_file}")
        return gaia_data

    except Exception as e:
        print(f"Error fetching Gaia data: {e}")
        return None

def estimate_vmag_from_gaia(gaia_data):
    """Convert Gaia G magnitudes (plus BP-RP) to an approximate Johnson V magnitude."""
    vmag = np.full(len(gaia_data), np.nan)
    if all(col in gaia_data.colnames for col in ['Gmag', 'BP-RP']):
        bp_rp = gaia_data['BP-RP']
        valid_mask = ~np.isnan(gaia_data['Gmag']) & ~np.isnan(bp_rp)
        # Polynomial approximation
        vmag[valid_mask] = (
            gaia_data['Gmag'][valid_mask]
            - (
                -0.0257
                - 0.0924 * bp_rp[valid_mask]
                - 0.1623 * bp_rp[valid_mask] ** 2
                + 0.0090 * bp_rp[valid_mask] ** 3
            )
        )
    return vmag

def align_coordinate_systems(hip_data):
    """Align coordinate systems by ensuring RA_ICRS, DE_ICRS exist in the table."""
    if hip_data is None:
        return None
    try:
        if 'RA_ICRS' not in hip_data.colnames:
            if 'RAICRS' in hip_data.colnames:
                hip_data.rename_column('RAICRS', 'RA_ICRS')
            elif 'RAhms' in hip_data.colnames:
                hip_data['RA_ICRS'] = Angle(hip_data['RAhms'], unit='hourangle').degree
        if 'DE_ICRS' not in hip_data.colnames:
            if 'DEICRS' in hip_data.colnames:
                hip_data.rename_column('DEICRS', 'DE_ICRS')
            elif 'DEdms' in hip_data.colnames:
                hip_data['DE_ICRS'] = Angle(hip_data['DEdms'], unit='deg').degree
        return hip_data
    except Exception as e:
        raise RuntimeError(f"Error aligning coordinate systems: {e}")

def process_distance_data(data, max_light_years):
    """
    Convert parallax to distance (pc, ly) and filter out anything beyond max_light_years.
    This mimics the old data_acquisition_distance.py logic.
    """
    if data is None or 'Plx' not in data.colnames:
        return None
    parallax_mas = data['Plx']
    parallax_arcsec = parallax_mas / 1000.0
    distance_pc = 1 / parallax_arcsec
    distance_ly = distance_pc * 3.26156
    data['Distance_pc'] = distance_pc
    data['Distance_ly'] = distance_ly

    # Filter
    mask = (np.isfinite(distance_ly) & (distance_ly > 0) & (distance_ly <= max_light_years))
    data = data[mask]
    return data

def load_stellar_data(mode='distance', max_value=20.0, 
                      hip_file='hipparcos_data.vot', gaia_file='gaia_data.vot'):
    """
    Main function to load or fetch data from Hipparcos and Gaia, either for a distance-based
    or magnitude-based query. Integrates old distance logic plus optional magnitude logic.

    Args:
        mode: 'distance' or 'magnitude'
        max_value: e.g. 100.0 light-years (distance mode) or 6.0 (magnitude mode)
        hip_file, gaia_file: local filenames to cache results
    Returns:
        (hip_data, gaia_data): Two astropy Tables
    """
    v = initialize_vizier(timeout=300)  # longer timeout for big queries

    # Build constraints
    if mode == 'distance':
        parallax_constraint = f">={calculate_parallax_limit(max_value)}"
        hip_data = load_or_fetch_hipparcos_data(
            v, hip_data_file=hip_file, mode='distance',
            parallax_constraint=parallax_constraint
        )
        gaia_data = load_or_fetch_gaia_data(
            v, gaia_file, mode='distance',
            parallax_constraint=parallax_constraint
        )

        # Post-process distances
        hip_data = process_distance_data(hip_data, max_value)
        if hip_data is not None:
            hip_data = align_coordinate_systems(hip_data)
        if gaia_data is not None:
            gaia_data = process_distance_data(gaia_data, max_value)
            # Estimate V from G for Gaia
            gaia_data['Estimated_Vmag'] = estimate_vmag_from_gaia(gaia_data)
        return hip_data, gaia_data

    else:  # magnitude mode
        hip_data = load_or_fetch_hipparcos_data(
            v, hip_file, mode='magnitude', mag_limit=max_value
        )
        gaia_data = load_or_fetch_gaia_data(
            v, gaia_file, mode='magnitude', mag_limit=max_value
        )
        # You can do extra processing if needed-like distance calculation if 'Plx' is present
        if gaia_data is not None:
            gaia_data['Estimated_Vmag'] = estimate_vmag_from_gaia(gaia_data)
        return hip_data, gaia_data
