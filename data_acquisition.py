"""data_acquisition.py - Unified module for fetching stellar data based on magnitude or distance."""

import os
import time
import numpy as np
from astroquery.vizier import Vizier
from astropy.table import Table
from astropy.coordinates import Angle
from astropy.io.votable import parse_single_table

def format_file_size(size_bytes):
    """Format file size in human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"

class ProgressReporter:
    """Handle progress reporting for data operations."""
    
    @staticmethod
    def start_operation(operation, details=""):
        """Report start of an operation."""
        message = f"\n=== Starting {operation} ==="
        if details:
            message += f"\n{details}"
        print(message)
    
    @staticmethod
    def file_operation(operation, filename, file_size=None):
        """Report file operation progress."""
        if file_size is not None:
            size_str = format_file_size(file_size)
            print(f"{operation} {filename} ({size_str})...")
        else:
            print(f"{operation} {filename}...")
    
    @staticmethod
    def catalog_stats(catalog_name, total_stars, bright_stars=None, medium_stars=None, faint_stars=None):
        """Report catalog statistics."""
        print(f"\n{catalog_name} Statistics:")
        print(f"  Total stars: {total_stars:,}")
        if bright_stars is not None:
            print(f"  Bright stars (≤ 1.73): {bright_stars:,}")
        if medium_stars is not None:
            print(f"  Medium stars (1.73-4.0): {medium_stars:,}")
        if faint_stars is not None:
            print(f"  Faint stars (> 4.0): {faint_stars:,}")
    
    @staticmethod
    def complete_operation(operation, duration=None):
        """Report completion of an operation."""
        message = f"=== Completed {operation} ==="
        if duration is not None:
            message += f" in {duration:.1f} seconds"
        print(f"\n{message}\n")

def initialize_vizier():
    """Initialize Vizier with no row limit and all columns."""
    try:
        v = Vizier(columns=['*'], row_limit=-1)
        return v
    except Exception as e:
        raise RuntimeError(f"Failed to initialize Vizier: {e}")

def calculate_parallax_limit(max_light_years):
    """Calculate minimum parallax for given distance in light-years."""
    max_distance_pc = max_light_years / 3.26156
    min_parallax_mas = (1 / max_distance_pc) * 1000
    return min_parallax_mas

"""
Updates to data_acquisition.py focusing on validation and user confirmation.
Documentation and GitHub-specific items will be added later.
"""

def confirm_regeneration(file_path, mode):
    """Ask for user confirmation before regenerating files."""
    print(f"\nWARNING: {file_path} needs to be regenerated.")
    print("This process can take several hours.")
    response = input("Would you like to regenerate this file? (yes/no): ").lower()
    
    if response != 'yes':
        print("Regeneration cancelled.")
        return False, None
        
    response = input("Are you sure? This may take several hours. Type 'yes' to confirm: ").lower()
    if response != 'yes':
        print("Regeneration cancelled.")
        return False, None
        
    if mode == 'distance':
        while True:
            try:
                ly = float(input("Enter maximum distance in light-years (max 100): "))
                if 0 < ly <= 100:
                    return True, ly
                print("Please enter a value between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
    else:  # magnitude mode
        while True:
            try:
                mag = float(input("Enter maximum apparent magnitude (-1.44 to 9.0): "))
                if -1.44 <= mag <= 9.0:
                    return True, mag
                print("Please enter a value between -1.44 and 9.0.")
            except ValueError:
                print("Please enter a valid number.")

def validate_votable_file(file_path, catalog_type, mode):
    """Validate VOTable file content."""
    try:
        if not os.path.exists(file_path):
            return False
            
        file_size = os.path.getsize(file_path)
        
        # Define minimum expected sizes based on actual data
        if mode == 'magnitude':
            if catalog_type == 'hipparcos':
                min_size = 25 * 1024 * 1024  # 25MB (actual ~29.6MB)
                min_bright_stars = 30  # For Vmag ≤ 1.73
            else:  # gaia
                min_size = 250 * 1024 * 1024  # 250MB (actual ~284MB)
                min_bright_stars = 0  # Gaia doesn't have bright stars
        else:  # distance mode
            if catalog_type == 'hipparcos':
                min_size = 800 * 1024  # 800KB (actual ~897KB)
                min_bright_stars = 14  # For 100ly
            else:  # gaia
                min_size = 8 * 1024 * 1024  # 8MB (actual ~9.2MB)
                min_bright_stars = 0  # Gaia doesn't have bright stars
        
        if file_size < min_size:
            print(f"File size {format_file_size(file_size)} is smaller than expected minimum {format_file_size(min_size)}")
            return False
            
        # Check bright stars for Hipparcos
        if catalog_type == 'hipparcos':
            table = parse_single_table(file_path, pedantic=False)
            if 'Vmag' in table.array.dtype.names:
                bright_stars = np.sum(table.array['Vmag'] <= 1.73)
                if bright_stars < min_bright_stars:
                    print(f"Found only {bright_stars} bright stars, expected at least {min_bright_stars}")
                    return False
        
        return True
        
    except Exception as e:
        print(f"Error validating {file_path}: {e}")
        return False

def load_or_fetch_hipparcos_data(v, hip_data_file, mag_limit=None, parallax_constraint=None):
    """Load or fetch Hipparcos data with progress reporting."""
    progress = ProgressReporter()
    start_time = time.time()
    
    if os.path.exists(hip_data_file):
        if validate_votable_file(hip_data_file, 'hipparcos', 
                               'magnitude' if mag_limit else 'distance'):
            file_size = os.path.getsize(hip_data_file)
            progress.file_operation("Loading", hip_data_file, file_size)
            data = Table.read(hip_data_file, format='votable')
            progress.catalog_stats("Cached Hipparcos", len(data))
            return data
    
    progress.start_operation("Hipparcos data fetch", 
                           f"{'Magnitude' if mag_limit else 'Distance'} mode")
    try:
        constraints = {}
        if mag_limit is not None:
            constraints['Vmag'] = f"<={mag_limit}"
        elif parallax_constraint is not None:
            constraints['Plx'] = parallax_constraint
            
        print("Querying VizieR database...")
        result = v.query_constraints(catalog="I/239/hip_main", **constraints)
        
        if not result:
            print("No data found in Hipparcos catalog.")
            return None
            
        hip_data = result[0]
        
        if 'Vmag' in hip_data.colnames:
            bright_stars = np.sum(hip_data['Vmag'] <= 1.73)
            medium_stars = np.sum((hip_data['Vmag'] > 1.73) & (hip_data['Vmag'] <= 4.0))
            faint_stars = np.sum(hip_data['Vmag'] > 4.0)
            progress.catalog_stats("Fresh Hipparcos", len(hip_data), 
                                bright_stars, medium_stars, faint_stars)
        
        progress.file_operation("Saving", hip_data_file)
        hip_data.write(hip_data_file, format='votable', overwrite=True)
        saved_size = os.path.getsize(hip_data_file)
        print(f"Saved Hipparcos data ({format_file_size(saved_size)})")
        
        duration = time.time() - start_time
        progress.complete_operation("Hipparcos data fetch", duration)
        return hip_data
        
    except Exception as e:
        print(f"\nError fetching Hipparcos data: {e}")
        return None

def load_or_fetch_gaia_data(v, gaia_data_file, mag_limit=None, parallax_constraint=None):
    """Load or fetch Gaia data with progress reporting."""
    progress = ProgressReporter()
    start_time = time.time()
    
    if os.path.exists(gaia_data_file):
        if validate_votable_file(gaia_data_file, 'gaia', 
                               'magnitude' if mag_limit else 'distance'):
            file_size = os.path.getsize(gaia_data_file)
            progress.file_operation("Loading", gaia_data_file, file_size)
            data = Table.read(gaia_data_file, format='votable')
            progress.catalog_stats("Cached Gaia", len(data))
            return data
    
    progress.start_operation("Gaia data fetch", 
                           f"{'Magnitude' if mag_limit else 'Distance'} mode")
    try:
        constraints = {}
        if mag_limit is not None:
            adjusted_limit = min(11.0, mag_limit + 0.5)
            constraints['Gmag'] = f"<={adjusted_limit}"
        elif parallax_constraint is not None:
            constraints['Plx'] = parallax_constraint
            constraints['e_Plx'] = '<2'  # Parallax error < 2 mas
            
        print("Querying VizieR database...")
        result = v.query_constraints(catalog="I/350/gaiaedr3", **constraints)
        
        if not result:
            print("No data found in Gaia EDR3.")
            return None
            
        gaia_data = result[0]
        
        # Standardize column names
        if 'phot_g_mean_mag' in gaia_data.colnames:
            gaia_data['Gmag'] = gaia_data['phot_g_mean_mag']
        if 'phot_bp_mean_mag' in gaia_data.colnames and 'phot_rp_mean_mag' in gaia_data.colnames:
            gaia_data['BP-RP'] = gaia_data['phot_bp_mean_mag'] - gaia_data['phot_rp_mean_mag']
        
        # Calculate statistics
        if 'Gmag' in gaia_data.colnames:
            bright_stars = np.sum(gaia_data['Gmag'] <= 1.73)
            medium_stars = np.sum((gaia_data['Gmag'] > 1.73) & (gaia_data['Gmag'] <= 4.0))
            faint_stars = np.sum(gaia_data['Gmag'] > 4.0)
            progress.catalog_stats("Fresh Gaia", len(gaia_data), 
                                bright_stars, medium_stars, faint_stars)
        
        progress.file_operation("Saving", gaia_data_file)
        gaia_data.write(gaia_data_file, format='votable', overwrite=True)
        saved_size = os.path.getsize(gaia_data_file)
        print(f"Saved Gaia data ({format_file_size(saved_size)})")
        
        duration = time.time() - start_time
        progress.complete_operation("Gaia data fetch", duration)
        return gaia_data
        
    except Exception as e:
        print(f"\nError fetching Gaia data: {e}")
        return None

def estimate_vmag_from_gaia(gaia_data):
    """Convert Gaia G magnitudes to Johnson V magnitudes."""
    vmag = np.full(len(gaia_data), np.nan)
    
    if all(col in gaia_data.colnames for col in ['Gmag', 'BP-RP']):
        bp_rp = gaia_data['BP-RP']
        valid_mask = ~np.isnan(gaia_data['Gmag']) & ~np.isnan(bp_rp)
        vmag[valid_mask] = (gaia_data['Gmag'][valid_mask] - 
                         (-0.0257 - 0.0924*bp_rp[valid_mask] - 
                          0.1623*bp_rp[valid_mask]**2 + 
                          0.0090*bp_rp[valid_mask]**3))
    return vmag

def align_coordinate_systems(hip_data):
    """Align coordinate systems between catalogs."""
    if hip_data is None:
        return None
        
    try:
        if 'RA_ICRS' not in hip_data.colnames:
            if 'RAICRS' in hip_data.colnames:
                hip_data.rename_column('RAICRS', 'RA_ICRS')
            elif 'RAhms' in hip_data.colnames:
                ra_hms = hip_data['RAhms']
                hip_data['RA_ICRS'] = Angle(ra_hms, unit='hourangle').degree
        
        if 'DE_ICRS' not in hip_data.colnames:
            if 'DEICRS' in hip_data.colnames:
                hip_data.rename_column('DEICRS', 'DE_ICRS')
            elif 'DEdms' in hip_data.colnames:
                dec_dms = hip_data['DEdms']
                hip_data['DE_ICRS'] = Angle(dec_dms, unit='deg').degree
                
        return hip_data
    except Exception as e:
        raise RuntimeError(f"Error aligning coordinate systems: {e}")