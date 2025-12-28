"""
Paleoclimate Data Fetcher for Paloma's Orrery
Fetches and caches paleoclimate proxy data from authoritative sources

Data Preservation is Climate Action
"""

import requests
import json
import os
from datetime import datetime
import hashlib

# Data file paths
# PALEO_DATA_DIR = 'paleoclimate_data' # refactoring the data structure
PALEO_DATA_DIR = 'data'
LR04_CACHE = os.path.join(PALEO_DATA_DIR, 'lr04_benthic_stack.json')
EPICA_CO2_CACHE = os.path.join(PALEO_DATA_DIR, 'epica_co2_800kyr.json')
EPICA_TEMP_CACHE = os.path.join(PALEO_DATA_DIR, 'epica_temp_800kyr.json')

# Data source URLs
LR04_URL = 'https://www.ncei.noaa.gov/pub/data/paleo/contributions_by_author/lisiecki2005/lisiecki2005-d18o-stack-noaa.txt'
EPICA_CO2_URL = 'https://www.ncei.noaa.gov/pub/data/paleo/icecore/antarctica/epica_domec/edc-co2-2008.txt'

#def ensure_data_dir():
#    """Create data directory if it doesn't exist"""
#    if not os.path.exists(PALEO_DATA_DIR):
#        os.makedirs(PALEO_DATA_DIR)
#        print(f"Created directory: {PALEO_DATA_DIR}")

def ensure_data_dir():
    """Create data directory if it doesn't exist"""
    if not os.path.exists(PALEO_DATA_DIR):
        os.makedirs(PALEO_DATA_DIR)

def fetch_lr04_data():
    """
    Fetch LR04 benthic stack data (5.3 Ma - present)
    Benthic delta18O is proxy for ice volume and deep ocean temperature
    """
    print("\n" + "="*70)
    print("FETCHING LR04 BENTHIC STACK")
    print("="*70)
    
    try:
        response = requests.get(LR04_URL, timeout=30)
        response.raise_for_status()
        
        # Parse the tab-delimited data
        lines = response.text.split('\n')
        data_started = False
        records = []
        
        for line in lines:
            if line.startswith('age_calkaBP'):
                data_started = True
                continue
            
            if data_started and line.strip():
                parts = line.strip().split('\t')
                if len(parts) >= 3:
                    try:
                        age_ka = float(parts[0])
                        d18o = float(parts[1])
                        error = float(parts[2])
                        records.append({
                            'age_ka_bp': age_ka,
                            'd18o_permil': d18o,
                            'd18o_error': error
                        })
                    except ValueError:
                        continue
        
        # Create cached data structure
        cache_data = {
            'metadata': {
                'source': 'Lisiecki & Raymo (2005)',
                'doi': '10.1029/2004PA001071',
                'citation': 'Lisiecki, L.E. and M.E. Raymo. 2005. A Pliocene-Pleistocene stack of 57 globally distributed benthic D18O records. Paleoceanography, 20, PA1003.',
                'data_url': LR04_URL,
                'description': 'LR04 benthic delta18O stack - proxy for ice volume and deep ocean temperature',
                'time_range': '5.3 Ma to present',
                'downloaded': datetime.now().isoformat(),
                'record_count': len(records)
            },
            'data': records
        }
        
        # Save to cache
        with open(LR04_CACHE, 'w') as f:
            json.dump(cache_data, f, indent=2)
        
        print(f"[OK] Downloaded {len(records):,} records")
        print(f"[OK] Time range: {records[0]['age_ka_bp']:.1f} ka BP to {records[-1]['age_ka_bp']:.1f} ka BP")
        print(f"[OK] Cached to: {LR04_CACHE}")
        
        return True
        
    except Exception as e:
        print(f"[FAIL] Error fetching LR04 data: {e}")
        return False

def fetch_epica_co2_data():
    """
    Fetch EPICA Dome C CO2 data (800 ka - present)
    """
    print("\n" + "="*70)
    print("FETCHING EPICA DOME C CO2 DATA")
    print("="*70)
    
    try:
        response = requests.get(EPICA_CO2_URL, timeout=30)
        response.raise_for_status()
        
        # Parse the data
        lines = response.text.split('\n')
        data_started = False
        records = []
        
        for line in lines:
            # Skip comments
            if line.startswith('#'):
                continue
            
            # Look for data header
            if 'Age' in line or 'age' in line:
                data_started = True
                continue
            
            if data_started and line.strip():
                parts = line.strip().split()
                if len(parts) >= 2:
                    try:
                        # Format varies, but typically: age_yr_BP  CO2_ppmv
                        age_yr = float(parts[0])
                        co2_ppm = float(parts[1])
                        records.append({
                            'age_yr_bp': age_yr,
                            'co2_ppm': co2_ppm
                        })
                    except ValueError:
                        continue
        
        if records:
            cache_data = {
                'metadata': {
                    'source': 'Luthi et al. (2008)',
                    'doi': '10.1038/nature06949',
                    'citation': 'Luthi, D., et al. 2008. High-resolution carbon dioxide concentration record 650,000-800,000 years before present. Nature, Vol. 453, pp. 379-382.',
                    'data_url': EPICA_CO2_URL,
                    'description': 'EPICA Dome C ice core 800,000-year CO2 record',
                    'time_range': '800 ka to present',
                    'downloaded': datetime.now().isoformat(),
                    'record_count': len(records)
                },
                'data': records
            }
            
            with open(EPICA_CO2_CACHE, 'w') as f:
                json.dump(cache_data, f, indent=2)
            
            print(f"[OK] Downloaded {len(records):,} records")
            print(f"[OK] Cached to: {EPICA_CO2_CACHE}")
            return True
        else:
            print("[FAIL] No data records found")
            return False
            
    except Exception as e:
        print(f"[FAIL] Error fetching EPICA CO2 data: {e}")
        print("  Note: URL may need adjustment or data may require manual download")
        return False

def main():
    """Fetch all paleoclimate datasets"""
    ensure_data_dir()
    
    print("\n" + "="*70)
    print("PALEOCLIMATE DATA FETCHER")
    print("For Paloma's Orrery - Data Preservation is Climate Action")
    print("="*70)
    
    results = {
        'LR04 Stack': fetch_lr04_data(),
        'EPICA CO2': fetch_epica_co2_data()
    }
    
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    for name, success in results.items():
        status = "[OK] SUCCESS" if success else "[FAIL] FAILED"
        print(f"{name}: {status}")
    
    print("\nNext steps:")
    print("1. Check cached files in:", PALEO_DATA_DIR)
    print("2. Manual data may be needed for deep Cenozoic (66 Ma)")
    print("3. Temperature proxies may need conversion from delta18O")

if __name__ == '__main__':
    main()
