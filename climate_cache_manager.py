# climate_cache_manager.py
"""
Climate Data Cache Manager for Paloma's Orrery
Handles safe updates to climate data caches with atomic saves and validation.

Follows the same safety protocols as orbit_data_manager.py:
- Never overwrites large files with small data
- Creates backups before updates
- Validates data before saving
- Uses atomic file operations (temp file -> backup -> move)

Data preservation is climate action.
"""

import json
import os
import sys


# Output Files
CO2_OUTPUT_FILE = "co2_mauna_loa_monthly.json"
TEMP_OUTPUT_FILE = "temperature_giss_monthly.json"
ICE_OUTPUT_FILE = "arctic_ice_extent_monthly.json"

# Minimum acceptable file sizes (bytes)
MIN_CO2_SIZE = 30_000  # ~30 KB minimum
MIN_TEMP_SIZE = 60_000  # ~60 KB minimum
MIN_ICE_SIZE = 20_000   # ~20 KB minimum


def update_climate_data(status_callback=None):
    """
    Update climate data by directly calling fetch_climate_data functions.
    
    This avoids subprocess issues on Windows by importing and calling directly.
    
    Returns: (success, message, details)
    """
    print("\n" + "="*70)
    print("CLIMATE DATA UPDATE")
    print("="*70)
    print()
    
    if status_callback:
        status_callback("Fetching latest climate data...")
    
    # Import the fetch module
    try:
        print("Attempting to import fetch_climate_data module...")
        import fetch_climate_data
        print("✓ Successfully loaded fetch_climate_data module")
    except ImportError as e:
        error_msg = f"Could not import fetch_climate_data: {e}"
        print(f"✗ {error_msg}")
        return False, error_msg, None
    except Exception as e:
        error_msg = f"Error importing fetch_climate_data: {e}"
        print(f"✗ {error_msg}")
        import traceback
        traceback.print_exc()
        return False, error_msg, None
    
    # Track results
    results = {}
    
    # ========== FETCH CO2 DATA ==========
    print("\n" + "="*60)
    print("1. Fetching Mauna Loa CO₂ monthly data...")
    print("="*60)
    
    if status_callback:
        status_callback("Downloading CO₂ data from NOAA...")
    
    try:
        # Check if function accepts status_callback parameter
        import inspect
        sig = inspect.signature(fetch_climate_data.fetch_mauna_loa_co2)
        has_callback = 'status_callback' in sig.parameters
        
        if has_callback:
            co2_records, co2_metadata = fetch_climate_data.fetch_mauna_loa_co2(status_callback)
        else:
            co2_records, co2_metadata = fetch_climate_data.fetch_mauna_loa_co2()
        
        if not co2_records or not co2_metadata:
            raise Exception("No CO₂ data returned")
        
        if status_callback:
            status_callback("Validating and saving CO₂ data...")
        
        # Save using fetch_climate_data's save_cache function
        if fetch_climate_data.save_cache(CO2_OUTPUT_FILE, co2_records, co2_metadata):
            latest = co2_records[-1]
            print(f"✓ CO₂ updated: {latest['co2_ppm']:.2f} ppm")
            
            if status_callback:
                status_callback(f"✓ CO₂ updated: {latest['co2_ppm']:.2f} ppm")
            
            results['co2'] = {
                'success': True,
                'records': len(co2_records),
                'latest': latest['co2_ppm']
            }
        else:
            raise Exception("Failed to save CO₂ data")
        
    except Exception as e:
        print(f"✗ CO₂ fetch failed: {e}")
        import traceback
        traceback.print_exc()
        results['co2'] = {
            'success': False,
            'error': str(e)
        }
    
    # ========== FETCH TEMPERATURE DATA ==========
    print("\n" + "="*60)
    print("2. Fetching NASA GISS temperature anomaly data...")
    print("="*60)
    
    if status_callback:
        status_callback("Downloading temperature data from NASA GISS...")
    
    try:
        import inspect
        sig = inspect.signature(fetch_climate_data.fetch_nasa_giss_temperature)
        has_callback = 'status_callback' in sig.parameters
        
        if has_callback:
            temp_records, temp_metadata = fetch_climate_data.fetch_nasa_giss_temperature(status_callback)
        else:
            temp_records, temp_metadata = fetch_climate_data.fetch_nasa_giss_temperature()
        
        if not temp_records or not temp_metadata:
            raise Exception("No temperature data returned")
        
        if status_callback:
            status_callback("Validating and saving temperature data...")
        
        # Save using fetch_climate_data's save_cache function
        if fetch_climate_data.save_cache(TEMP_OUTPUT_FILE, temp_records, temp_metadata):
            latest = temp_records[-1]
            print(f"✓ Temperature updated: {latest['anomaly_c']:+.2f}°C")
            
            if status_callback:
                status_callback(f"✓ Temperature updated: {latest['anomaly_c']:+.2f}°C")
            
            results['temperature'] = {
                'success': True,
                'records': len(temp_records),
                'latest': latest['anomaly_c']
            }
        else:
            raise Exception("Failed to save temperature data")
        
    except Exception as e:
        print(f"✗ Temperature fetch failed: {e}")
        import traceback
        traceback.print_exc()
        results['temperature'] = {
            'success': False,
            'error': str(e)
        }
    
    # ========== FETCH ARCTIC ICE DATA ==========
    print("\n" + "="*60)
    print("3. Fetching Arctic sea ice extent data...")
    print("="*60)
    
    if status_callback:
        status_callback("Downloading Arctic ice data from NSIDC...")
    
    try:
        import inspect
        sig = inspect.signature(fetch_climate_data.fetch_arctic_sea_ice)
        has_callback = 'status_callback' in sig.parameters
        
        if has_callback:
            ice_records, ice_metadata = fetch_climate_data.fetch_arctic_sea_ice(status_callback)
        else:
            ice_records, ice_metadata = fetch_climate_data.fetch_arctic_sea_ice()
        
        if not ice_records or not ice_metadata:
            raise Exception("No Arctic ice data returned")
        
        if status_callback:
            status_callback("Validating and saving Arctic ice data...")
        
        # Save using fetch_climate_data's save_cache function
        if fetch_climate_data.save_cache(ICE_OUTPUT_FILE, ice_records, ice_metadata):
            latest = ice_records[-1]
            print(f"✓ Arctic ice updated: {latest['extent_million_km2']:.2f} million km²")
            
            if status_callback:
                status_callback(f"✓ Arctic ice updated: {latest['extent_million_km2']:.2f} million km²")
            
            results['ice'] = {
                'success': True,
                'records': len(ice_records),
                'latest': latest['extent_million_km2']
            }
        else:
            raise Exception("Failed to save Arctic ice data")
        
    except Exception as e:
        print(f"✗ Arctic ice fetch failed: {e}")
        import traceback
        traceback.print_exc()
        results['ice'] = {
            'success': False,
            'error': str(e)
        }
    
    # ========== SUMMARY ==========
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    success_count = sum(1 for r in results.values() if r.get('success', False))
    total_count = len(results)
    
    for dataset, result in results.items():
        status = '✅' if result.get('success', False) else '❌'
        print(f"{status} {dataset.upper()}: {'SUCCESS' if result.get('success', False) else 'FAILED'}")
        if result.get('success', False):
            print(f"    Records: {result.get('records', 'N/A')}")
            print(f"    Latest: {result.get('latest', 'N/A')}")
    
    print()
    
    if success_count == total_count:
        summary = (f"All datasets updated successfully! "
                  f"CO₂: {results['co2']['records']} records ({results['co2']['latest']:.2f} ppm), "
                  f"Temp: {results['temperature']['records']} records ({results['temperature']['latest']:+.2f}°C), "
                  f"Ice: {results['ice']['records']} records ({results['ice']['latest']:.2f} million km²)")
        print("✅ All datasets updated successfully!")
        return True, summary, results
    elif success_count > 0:
        summary = f"Partial update: {success_count}/{total_count} datasets updated successfully"
        print(f"⚠️  {summary}")
        return True, summary, results
    else:
        summary = "Update failed: No datasets were successfully updated"
        print(f"✗ {summary}")
        return False, summary, results


if __name__ == "__main__":
    """Test the update function"""
    success, message, details = update_climate_data()
    print(f"\nFinal result: {'SUCCESS' if success else 'FAILED'}")
    print(f"Message: {message}")
    
    if details:
        print("\nDetails:")
        for dataset, result in details.items():
            print(f"  {dataset}: {result}")
    
    sys.exit(0 if success else 1)
