"""
Climate Cache Manager for Paloma's Orrery
Manages safe updates of climate data caches with validation and rollback.

Updated December 2025 - Fixed API calls to match fetch_climate_data.py
"""

import os
import json
import inspect

# Output file paths - now in data/ subdirectory
CO2_OUTPUT_FILE = "data/co2_mauna_loa_monthly.json"
TEMP_OUTPUT_FILE = "data/temperature_giss_monthly.json"
ICE_OUTPUT_FILE = "data/arctic_ice_extent_monthly.json"


def update_climate_data(status_callback=None):
    """
    Update all climate datasets by importing and calling fetch functions directly.
    Returns: (success, message, details)
    """
    def status(msg):
        if status_callback:
            status_callback(msg)
        print(msg)
    
    print("\n" + "="*70)
    print("CLIMATE DATA UPDATE")
    print("="*70)
    
    try:
        # Try to import the fetch module
        status("Attempting to import fetch_climate_data module...")
        import fetch_climate_data
        status("[OK] Successfully loaded fetch_climate_data module")
    except ImportError as e:
        error_msg = f"Could not import fetch_climate_data: {e}"
        status(f"[FAIL] {error_msg}")
        return False, error_msg, {}
    
    results = {
        'co2': {'success': False},
        'temperature': {'success': False},
        'ice': {'success': False}
    }
    
    # ========== FETCH CO2 DATA ==========
    print("\n" + "="*60)
    print("1. Fetching Mauna Loa CO2 monthly data...")
    print("="*60)
    
    try:
        status("Downloading CO2 data from NOAA...")
        
        # fetch_mauna_loa_co2 returns just records (not a tuple)
        co2_records = fetch_climate_data.fetch_mauna_loa_co2()
        
        if not co2_records:
            raise Exception("No CO2 data returned")
        
        status(f"[OK] Fetched {len(co2_records)} CO2 records")
        
        # save_cache expects: (filename, records, metadata_func)
        # Pass the function, not the result
        if fetch_climate_data.save_cache(CO2_OUTPUT_FILE, co2_records, fetch_climate_data.create_co2_metadata):
            latest = co2_records[-1]
            co2_value = latest.get('co2_ppm', latest.get('average', 0))
            status(f"[OK] CO2 updated: {co2_value:.2f} ppm")
            
            results['co2'] = {
                'success': True,
                'records': len(co2_records),
                'latest': co2_value
            }
        else:
            raise Exception("Failed to save CO2 data")
        
    except Exception as e:
        error_msg = str(e)
        status(f"[FAIL] CO2 fetch failed: {error_msg}")
        results['co2'] = {'success': False, 'error': error_msg}
    
    # ========== FETCH TEMPERATURE DATA ==========
    print("\n" + "="*60)
    print("2. Fetching NASA GISS temperature anomaly data...")
    print("="*60)
    
    try:
        status("Downloading temperature data from NASA GISS...")
        
        # fetch_nasa_giss_temperature returns (records, metadata) tuple
        temp_records, temp_metadata = fetch_climate_data.fetch_nasa_giss_temperature()
        
        if not temp_records:
            raise Exception("No temperature data returned")
        
        status(f"[OK] Fetched {len(temp_records)} temperature records")
        
        # For temperature, we already have metadata, so pass it as a lambda
        if fetch_climate_data.save_cache(TEMP_OUTPUT_FILE, temp_records, lambda r: temp_metadata):
            latest = temp_records[-1]
            temp_value = latest.get('anomaly_c', latest.get('anomaly_celsius', 0))
            status(f"[OK] Temperature updated: {temp_value:+.2f} deg C")
            
            results['temperature'] = {
                'success': True,
                'records': len(temp_records),
                'latest': temp_value
            }
        else:
            raise Exception("Failed to save temperature data")
        
    except Exception as e:
        error_msg = str(e)
        status(f"[FAIL] Temperature fetch failed: {error_msg}")
        results['temperature'] = {'success': False, 'error': error_msg}
    
    # ========== FETCH ARCTIC ICE DATA ==========
    print("\n" + "="*60)
    print("3. Fetching Arctic sea ice extent data...")
    print("="*60)
    
    try:
        status("Downloading Arctic ice data from NSIDC...")
        
        # Function is fetch_arctic_ice (not fetch_arctic_sea_ice)
        # Returns just records (like CO2)
        ice_records = fetch_climate_data.fetch_arctic_ice()
        
        if not ice_records:
            raise Exception("No ice data returned")
        
        status(f"[OK] Fetched {len(ice_records)} ice records")
        
        # Use create_ice_metadata function if it exists, otherwise create inline
        if hasattr(fetch_climate_data, 'create_ice_metadata'):
            metadata_func = fetch_climate_data.create_ice_metadata
        else:
            # Inline metadata function
            def metadata_func(records):
                return {
                    'source': 'NSIDC Sea Ice Index V4',
                    'url': 'https://nsidc.org/data/seaice_index',
                    'units': 'million km^2',
                    'records': len(records)
                }
        
        if fetch_climate_data.save_cache(ICE_OUTPUT_FILE, ice_records, metadata_func):
            latest = ice_records[-1]
            ice_value = latest.get('extent', latest.get('extent_million_km2', 0))
            status(f"[OK] Arctic ice updated: {ice_value:.2f} million km^2")
            
            results['ice'] = {
                'success': True,
                'records': len(ice_records),
                'latest': ice_value
            }
        else:
            raise Exception("Failed to save ice data")
        
    except Exception as e:
        error_msg = str(e)
        status(f"[FAIL] Arctic ice fetch failed: {error_msg}")
        results['ice'] = {'success': False, 'error': error_msg}
    
    # ========== SUMMARY ==========
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    success_count = sum(1 for r in results.values() if r.get('success', False))
    total_count = len(results)
    
    for dataset, result in results.items():
        status_str = '[OK]' if result.get('success', False) else '[FAIL]'
        print(f"{status_str} {dataset.upper()}: ", end='')
        if result.get('success'):
            print(f"SUCCESS")
            print(f"    Records: {result.get('records', 'N/A')}")
            print(f"    Latest: {result.get('latest', 'N/A')}")
        else:
            print(f"FAILED - {result.get('error', 'Unknown error')}")
    
    all_success = success_count == total_count
    
    if all_success:
        message = "All datasets updated successfully!"
        status(f"[OK] {message}")
    else:
        message = f"{success_count}/{total_count} datasets updated"
        status(f"[WARN] {message}")
    
    print(f"\nFinal result: {'SUCCESS' if all_success else 'PARTIAL'}")
    print(f"Message: {message}")
    
    return all_success, message, results


if __name__ == '__main__':
    success, message, details = update_climate_data()
    print(f"\nResult: {success}")
    print(f"Message: {message}")
