# enhanced_star_properties.py
"""
Enhanced star_properties.py with both incremental VizieR caching
and smart SIMBAD querying.
"""

import os
import pickle
import time
import re
from astroquery.simbad import Simbad
import numpy as np

# Import the enhanced managers
from simbad_manager import SimbadQueryManager, SimbadConfig
from incremental_cache_manager import SimbadCacheManager


def parse_magnitude(value):
    """Parse magnitude value from various formats."""
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    value_str = str(value)
    # Remove annotations like [~] or [some text]
    cleaned = re.sub(r"\[.*?\]", "", value_str).strip()
    try:
        return float(cleaned)
    except ValueError:
        return None


def load_existing_properties(properties_file):
    """
    Load existing star and Messier object properties from a file.
    Enhanced with cache validation and migration.
    """
    if os.path.exists(properties_file):
        print("Loading properties from local file...")
        try:
            with open(properties_file, 'rb') as f:
                data = pickle.load(f)
            
            # Check if this is the old format (lists) or new format (dict)
            if isinstance(data, dict) and 'unique_ids' in data:
                # Old format - convert to new format
                print("Migrating cache from old format to new format...")
                existing_properties = {}
                
                required_keys = {
                    'unique_ids', 'star_names', 'spectral_types', 
                    'V_magnitudes', 'B_magnitudes', 'object_types'
                }
                
                if not required_keys.issubset(data.keys()):
                    print("Error: Missing required keys in properties file.")
                    return {}
                
                # Convert list format to dictionary format
                for i in range(len(data['unique_ids'])):
                    uid = data['unique_ids'][i]
                    
                    props = {
                        'star_name': data['star_names'][i],
                        'spectral_type': data['spectral_types'][i],
                        'V_magnitude': data['V_magnitudes'][i],
                        'B_magnitude': data['B_magnitudes'][i],
                        'object_type': data['object_types'][i],
                    }
                    
                    # Add optional fields if present
                    if 'is_messier' in data:
                        props['is_messier'] = data['is_messier'][i]
                        if data['is_messier'][i]:
                            props['distance_ly'] = data.get('distance_ly', [None] * len(data['unique_ids']))[i]
                            props['notes'] = data.get('notes', [''] * len(data['unique_ids']))[i]
                    
                    existing_properties[uid] = props
                
                # Save in new format for next time
                save_properties_to_file(existing_properties, properties_file)
                print(f"Migrated {len(existing_properties)} objects to new format")
                
            elif isinstance(data, dict):
                # Already in new dictionary format
                existing_properties = data
            else:
                print("Unknown cache format, starting fresh")
                return {}
            
            # Report statistics
            messier_count = sum(1 for props in existing_properties.values() 
                              if props.get('is_messier', False))
            print(f"Loaded {len(existing_properties)} objects ({messier_count} Messier objects)")
            
            return existing_properties
            
        except Exception as e:
            print(f"Error loading properties from file: {e}")
            return {}
    else:
        print("No existing properties file found. Starting fresh.")
        return {}


def save_properties_to_file(properties, properties_file):
    """
    Save star properties to file in new dictionary format.
    This is more efficient for incremental updates.
    """
    try:
        with open(properties_file, 'wb') as f:
            pickle.dump(properties, f)
        print(f"Saved {len(properties)} properties to {properties_file}")
    except Exception as e:
        print(f"Error saving properties: {e}")


def generate_unique_ids(combined_data):
    """Generate unique identifiers for all stars consistently."""
    print("Generating unique identifiers...")
    unique_ids = []

    for row in combined_data:
        uid = None
        
        # First try HIP ID
        if 'HIP' in combined_data.colnames:
            hip = row['HIP']
            if not np.ma.is_masked(hip) and hip is not None:
                try:
                    uid = f"HIP {int(hip)}"
                except (TypeError, ValueError):
                    uid = None

        # Then try Gaia Source ID
        if uid is None and 'Source' in combined_data.colnames:
            source = row['Source']
            if not np.ma.is_masked(source) and source is not None:
                try:
                    uid = f"Gaia DR3 {int(source)}"
                except (TypeError, ValueError):
                    uid = None

        # Finally use coordinates as fallback
        if uid is None and 'RA_ICRS' in combined_data.colnames and 'DE_ICRS' in combined_data.colnames:
            ra = row['RA_ICRS']
            dec = row['DE_ICRS']
            if not np.ma.is_masked(ra) and not np.ma.is_masked(dec):
                uid = f"J{ra:.6f}{dec:+.6f}"

        unique_ids.append(uid)

    print(f"Generated {len([uid for uid in unique_ids if uid is not None])} unique identifiers")
    return unique_ids


def query_simbad_for_star_properties(missing_ids, existing_properties, properties_file,
                                    use_incremental_cache=True, config=None):
    """
    Enhanced SIMBAD query function with incremental caching and rate limiting.
    
    Args:
        missing_ids: List of star IDs to query
        existing_properties: Dictionary of already known properties
        properties_file: File to save properties
        use_incremental_cache: Whether to use the SIMBAD cache manager
        config: Optional SimbadConfig instance
    """
    print(f"\nQuerying SIMBAD for {len(missing_ids)} missing star properties...")
    
    # Use SIMBAD cache manager if enabled
    if use_incremental_cache:
        simbad_cache = SimbadCacheManager()
        
        # Check what's already cached at the SIMBAD level
        cached_props, truly_missing_ids = simbad_cache.get_cached_objects(missing_ids)
        
        # Add cached properties to existing properties
        for obj_id, props in cached_props.items():
            existing_properties[obj_id] = props
        
        print(f"Retrieved {len(cached_props)} from SIMBAD cache, "
              f"{len(truly_missing_ids)} need fetching")
        
        # Update the list of IDs to query
        missing_ids = truly_missing_ids
    
    if not missing_ids:
        print("All properties found in cache!")
        return existing_properties
    
    # Load configuration or use defaults
    if config is None:
        config = SimbadConfig.load_from_file()
    
    print(f"Using rate limit: {config.queries_per_second:.1f} queries/second")
    print(f"Batch size: {config.batch_size} objects")
    
    try:
        # Create manager and query objects
        manager = SimbadQueryManager(config)
        
        # Query SIMBAD
        updated_properties = manager.query_objects(
            missing_ids,
            existing_properties,
            properties_file
        )
        
        # Update SIMBAD cache if enabled
        if use_incremental_cache:
            new_props = {
                obj_id: props 
                for obj_id, props in updated_properties.items()
                if obj_id in missing_ids
            }
            simbad_cache.update_cache(new_props)
        
        # Display statistics
        print(manager.stats.get_summary())
        
        # Save final properties
        save_properties_to_file(updated_properties, properties_file)
        
        return updated_properties
        
    except Exception as e:
        print(f"Error in SIMBAD query: {e}")
        return existing_properties


def assign_properties_to_data(combined_data, existing_properties, unique_ids):
    """
    Assign retrieved properties to the combined data.
    Enhanced with better error handling and reporting.
    """
    print(f"Assigning properties to {len(combined_data)} stars...")
    
    # Add new columns if they don't exist
    if 'star_name' not in combined_data.colnames:
        combined_data['star_name'] = [''] * len(combined_data)
    if 'spectral_type' not in combined_data.colnames:
        combined_data['spectral_type'] = [''] * len(combined_data)
    if 'object_type' not in combined_data.colnames:
        combined_data['object_type'] = [''] * len(combined_data)
    
    # Track assignment statistics
    assigned = 0
    missing = 0
    
    for i, uid in enumerate(unique_ids):
        if uid in existing_properties:
            props = existing_properties[uid]
            
            # Assign properties
            combined_data['star_name'][i] = props.get('star_name', '')
            combined_data['spectral_type'][i] = props.get('spectral_type', '')
            combined_data['object_type'][i] = props.get('object_type', '')
            
            # Update magnitudes if missing
            if 'V_magnitude' in props and props['V_magnitude'] is not None:
                if 'Vmag' in combined_data.colnames:
                    if np.ma.is_masked(combined_data['Vmag'][i]) or np.isnan(combined_data['Vmag'][i]):
                        combined_data['Vmag'][i] = props['V_magnitude']
            
            if 'B_magnitude' in props and props['B_magnitude'] is not None:
                if 'B-V' in combined_data.colnames and 'Vmag' in combined_data.colnames:
                    if not np.ma.is_masked(combined_data['Vmag'][i]):
                        combined_data['B-V'][i] = props['B_magnitude'] - combined_data['Vmag'][i]
            
            assigned += 1
        else:
            missing += 1
    
    print(f"Properties assigned: {assigned} stars have properties, {missing} missing")
    
    return combined_data


def create_custom_simbad():
    """
    Create custom SIMBAD instance using the enhanced manager.
    Maintains backward compatibility.
    """
    from simbad_manager import create_custom_simbad as create_simbad
    return create_simbad()


# Additional utility functions

def get_property_statistics(properties):
    """Get statistics about cached properties."""
    stats = {
        'total': len(properties),
        'with_spectral': 0,
        'with_vmag': 0,
        'with_bmag': 0,
        'messier': 0,
        'complete': 0
    }
    
    for props in properties.values():
        if props.get('spectral_type'):
            stats['with_spectral'] += 1
        if props.get('V_magnitude') is not None:
            stats['with_vmag'] += 1
        if props.get('B_magnitude') is not None:
            stats['with_bmag'] += 1
        if props.get('is_messier', False):
            stats['messier'] += 1
        
        # Check if all key properties are present
        if (props.get('star_name') and 
            props.get('spectral_type') and 
            props.get('V_magnitude') is not None):
            stats['complete'] += 1
    
    return stats


def cleanup_old_cache_files(directory=".", keep_latest=True):
    """
    Clean up old cache files to save disk space.
    
    Args:
        directory: Directory containing cache files
        keep_latest: If True, keep the most recent cache for each type
    """
    import glob
    from datetime import datetime
    
    cache_patterns = [
        "*_metadata.json",
        "hipparcos_*.vot",
        "gaia_*.vot",
        "star_properties_*.pkl"
    ]
    
    for pattern in cache_patterns:
        files = glob.glob(os.path.join(directory, pattern))
        
        if not files:
            continue
        
        if keep_latest and len(files) > 1:
            # Sort by modification time
            files.sort(key=lambda x: os.path.getmtime(x))
            
            # Keep the latest, delete the rest
            for old_file in files[:-1]:
                try:
                    os.remove(old_file)
                    print(f"Removed old cache file: {old_file}")
                except Exception as e:
                    print(f"Could not remove {old_file}: {e}")


# Testing
if __name__ == "__main__":
    # Test property loading and conversion
    test_file = "test_star_properties.pkl"
    
    # Test with a few star IDs
    test_ids = ["HIP 71683", "HIP 71681", "Gaia DR3 12345"]
    
    # Load existing properties
    props = load_existing_properties(test_file)
    print(f"\nLoaded {len(props)} existing properties")
    
    # Get statistics
    stats = get_property_statistics(props)
    print("\nProperty Statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # Find missing properties
    missing = [uid for uid in test_ids if uid not in props]
    
    if missing:
        # Query with enhanced caching
        props = query_simbad_for_star_properties(
            missing, props, test_file,
            use_incremental_cache=True
        )
    
    print(f"\nFinal: {len(props)} total properties")
