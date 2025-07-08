"""
create_ephemeris_database.py - Create satellite_ephemerides.json from multiple sources

This script combines:
1. Orbital parameters from idealized_orbits.py
2. Updated data from JPL Horizons ephemeris files (when available)
3. A framework for adding more satellites as you download their ephemerides
"""

import json
import os
import re
from datetime import datetime
from typing import Dict, Optional

def parse_horizons_header(filename: str) -> Dict:
    """
    Parse orbital elements from JPL Horizons ephemeris file header.
    
    Returns dict with orbital elements found in the file.
    """
    orbital_data = {}
    
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        # Find the satellite data section
        # Look for patterns like "Semi-major axis, a (km) = 9.3772(10^3)"
        
        # Semi-major axis
        sma_match = re.search(r'Semi-major axis.*?=\s*([\d.]+)\s*\(10\^3\)', content)
        if not sma_match:
            sma_match = re.search(r'Semi-major axis.*?=\s*([\d.]+)', content)
        if sma_match:
            value = float(sma_match.group(1))
            # Check if it needs to be multiplied by 1000 (if in 10^3 km)
            if '(10^3)' in content[sma_match.start():sma_match.end() + 20]:
                value *= 1000
            orbital_data['semi_major_axis_km'] = value
            
        # Eccentricity
        ecc_match = re.search(r'Eccentricity.*?=\s*([\d.]+)', content)
        if ecc_match:
            orbital_data['eccentricity'] = float(ecc_match.group(1))
            
        # Inclination
        inc_match = re.search(r'Inclination.*?\(deg\).*?=\s*([\d.]+)', content)
        if inc_match:
            orbital_data['inclination_deg'] = float(inc_match.group(1))
            
        # Orbital period
        period_match = re.search(r'Orbital period.*?=\s*([\d.]+)\s*d', content)
        if period_match:
            orbital_data['orbital_period_days'] = float(period_match.group(1))
            
        # Physical properties
        radius_match = re.search(r'Radius.*?=\s*([\d.]+)\s*x\s*([\d.]+)\s*x\s*([\d.]+)', content)
        if radius_match:
            orbital_data['radius_km'] = {
                'x': float(radius_match.group(1)),
                'y': float(radius_match.group(2)),
                'z': float(radius_match.group(3))
            }
            
        # Density
        density_match = re.search(r'Density.*?=\s*([\d.]+)', content)
        if density_match:
            orbital_data['density_g_cm3'] = float(density_match.group(1))
            
        # Mass
        mass_match = re.search(r'Mass.*?=\s*([\d.]+).*?\(10\^(\d+)', content)
        if mass_match:
            base = float(mass_match.group(1))
            exponent = int(mass_match.group(2))
            orbital_data['mass_kg'] = base * (10 ** exponent)
            
        print(f"Parsed {filename}: found {len(orbital_data)} parameters")
        
    except FileNotFoundError:
        print(f"Warning: {filename} not found")
        
    return orbital_data


def get_idealized_orbits_data() -> Dict:
    """
    Import orbital parameters from idealized_orbits.py if available.
    """
    try:
        from idealized_orbits import planetary_params
        print(f"Loaded orbital parameters for {len(planetary_params)} objects from idealized_orbits.py")
        return planetary_params
    except ImportError:
        print("Warning: Could not import idealized_orbits.py")
        return {}


def create_satellite_ephemerides():
    """
    Create comprehensive satellite ephemeris database from all available sources.
    """
    
    # Initialize database structure
    database = {
        "metadata": {
            "version": "1.1",
            "created": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat(),
            "sources": {
                "idealized_orbits": "Local orbital parameters file",
                "jpl_horizons": "JPL Horizons ephemeris files"
            },
            "description": "Satellite orbital elements for refined orbit calculations",
            "units": {
                "distance": "kilometers",
                "angles": "degrees",
                "time": "days",
                "mass": "kilograms"
            }
        },
        "satellites": {}
    }
    
    # Step 1: Load data from idealized_orbits.py
    idealized_params = get_idealized_orbits_data()
    
    # Step 2: Convert idealized_orbits data to our format
    # Note: idealized_orbits.py uses AU, we need km
    AU_TO_KM = 149597870.7
    
    for sat_name, params in idealized_params.items():
        # Skip non-satellite objects
        if sat_name in ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 
                        'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Eris']:
            continue
            
        # Determine primary body
        primary = None
        if sat_name == 'Moon':
            primary = 'Earth'
        elif sat_name in ['Phobos', 'Deimos']:
            primary = 'Mars'
        elif sat_name in ['Io', 'Europa', 'Ganymede', 'Callisto']:
            primary = 'Jupiter'
        elif sat_name in ['Titan', 'Enceladus', 'Rhea', 'Dione', 'Tethys', 'Mimas', 'Phoebe']:
            primary = 'Saturn'
        elif sat_name in ['Miranda', 'Ariel', 'Umbriel', 'Titania', 'Oberon']:
            primary = 'Uranus'
        elif sat_name in ['Triton']:
            primary = 'Neptune'
        elif sat_name in ['Charon', 'Styx', 'Nix', 'Kerberos', 'Hydra']:
            primary = 'Pluto'
        elif sat_name == 'Dysnomia':
            primary = 'Eris'
            
        if primary:
            key = f"{primary.lower()}_{sat_name.lower()}"
            
            # Convert orbital elements
            orbital_elements = {}
            
            # Semi-major axis (convert from AU to km)
            if 'a' in params:
                orbital_elements['semi_major_axis_km'] = params['a'] * AU_TO_KM
                
            if 'e' in params:
                orbital_elements['eccentricity'] = params['e']
                
            if 'i' in params:
                orbital_elements['inclination_deg'] = params['i']
                
            if 'omega' in params:
                orbital_elements['argument_of_periapsis_deg'] = params['omega']
                
            if 'Omega' in params:
                orbital_elements['longitude_ascending_node_deg'] = params['Omega']
            
            database["satellites"][key] = {
                "name": sat_name,
                "primary": primary,
                "source": "idealized_orbits.py",
                "last_updated": datetime.now().isoformat(),
                "orbital_elements": orbital_elements
            }
    
    # Step 3: Update with Horizons data (more accurate)
    horizons_files = {
        'mars_phobos': 'horizons_phobos_heliocentric.txt',
        'mars_deimos': 'horizons_deimos_heliocentric.txt',
        'saturn_phoebe': 'horizons_phoebe_heliocentric.txt',
        # Add more as you download them:
        # 'jupiter_io': 'horizons_io.txt',
        # 'earth_moon': 'horizons_moon.txt',
        # etc.
    }
    
    for sat_key, filename in horizons_files.items():
        if os.path.exists(filename):
            print(f"\nProcessing Horizons file: {filename}")
            horizons_data = parse_horizons_header(filename)
            
            if horizons_data and sat_key in database["satellites"]:
                # Update with Horizons data (more accurate)
                sat_entry = database["satellites"][sat_key]
                
                # Update orbital elements
                for key, value in horizons_data.items():
                    if key in ['semi_major_axis_km', 'eccentricity', 'inclination_deg', 
                             'orbital_period_days']:
                        sat_entry["orbital_elements"][key] = value
                    elif key in ['radius_km', 'density_g_cm3', 'mass_kg']:
                        if "physical_properties" not in sat_entry:
                            sat_entry["physical_properties"] = {}
                        sat_entry["physical_properties"][key] = value
                
                sat_entry["source"] = "JPL Horizons (updated)"
                sat_entry["horizons_file"] = filename
                sat_entry["last_updated"] = datetime.now().isoformat()
                
                print(f"Updated {sat_key} with Horizons data")
        else:
            print(f"Horizons file not found: {filename}")
    
    # Step 4: Add any manual corrections or additional data
    # For example, adding specific values we know from the Horizons headers
    if "mars_phobos" in database["satellites"]:
        phobos = database["satellites"]["mars_phobos"]
        # From your Horizons file header
        phobos["orbital_elements"]["semi_major_axis_km"] = 9377.2
        phobos["orbital_elements"]["eccentricity"] = 0.0151
        phobos["orbital_elements"]["inclination_deg"] = 1.082
        phobos["orbital_elements"]["orbital_period_days"] = 0.319
        phobos["revision_date"] = "2025-06-02"
        
    if "mars_deimos" in database["satellites"]:
        deimos = database["satellites"]["mars_deimos"]
        # From your Horizons file header
        deimos["orbital_elements"]["semi_major_axis_km"] = 23463.2
        deimos["orbital_elements"]["eccentricity"] = 0.00033
        deimos["orbital_elements"]["inclination_deg"] = 1.791
        deimos["orbital_elements"]["orbital_period_days"] = 1.263
        deimos["revision_date"] = "2025-06-02"
    
    # Save to JSON file
    with open('satellite_ephemerides.json', 'w') as f:
        json.dump(database, f, indent=2)
    
    # Print summary
    print("\n" + "="*60)
    print("Created satellite_ephemerides.json")
    print(f"Total satellites: {len(database['satellites'])}")
    print("\nSatellites by source:")
    
    idealized_count = sum(1 for s in database['satellites'].values() 
                         if 'idealized' in s.get('source', ''))
    horizons_count = sum(1 for s in database['satellites'].values() 
                        if 'Horizons' in s.get('source', ''))
    
    print(f"  From idealized_orbits.py: {idealized_count}")
    print(f"  Updated with JPL Horizons: {horizons_count}")
    
    print("\nSatellites with refined data:")
    for key, sat in database['satellites'].items():
        if 'Horizons' in sat.get('source', ''):
            elements = sat['orbital_elements']
            print(f"\n{sat['name']} ({sat['primary']}):")
            print(f"  Semi-major axis: {elements.get('semi_major_axis_km', 'N/A'):,.1f} km")
            print(f"  Inclination: {elements.get('inclination_deg', 'N/A'):.3f}°")
            print(f"  Source: {sat['source']}")


def download_instructions():
    """Print instructions for downloading more ephemerides."""
    print("\n" + "="*60)
    print("To add more satellites:")
    print("1. Go to https://ssd.jpl.nasa.gov/horizons/")
    print("2. Select your satellite (e.g., 'Io')")
    print("3. Set:")
    print("   - Ephemeris Type: OBSERVER")
    print("   - Target Body: [Your satellite]")
    print("   - Observer Location: '@' + primary body code (e.g., '@599' for Jupiter)")
    print("   - Time Specification: Your date range")
    print("   - Table Settings: Default is fine")
    print("4. Download and save as 'horizons_[satellite]_heliocentric.txt'")
    print("5. Add to horizons_files dict in this script")
    print("6. Re-run this script")
    print("="*60)


if __name__ == "__main__":
    create_satellite_ephemerides()
    download_instructions()
