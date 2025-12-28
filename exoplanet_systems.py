"""
exoplanet_systems.py - Hardcoded Exoplanet System Catalog

This module contains well-characterized exoplanet systems with complete
orbital parameters for visualization in Paloma's Orrery.

Data sources:
- NASA Exoplanet Archive: https://exoplanetarchive.ipac.caltech.edu/
- Published papers and discovery announcements
- SIMBAD for stellar properties

Phase 1 systems:
1. TRAPPIST-1: 7 terrestrial planets, 3 in habitable zone
2. TOI-1338: Circumbinary system, student discovery
3. Proxima Centauri: Nearest exoplanet, high proper motion

Created: October 21, 2025
Author: Tony Quintanilla with Claude AI
"""

from datetime import datetime, timezone

# Reference epochs for orbital calculations
J2000 = datetime(2000, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
TRAPPIST1_DISCOVERY_EPOCH = datetime(2017, 2, 22, tzinfo=timezone.utc)
TOI1338_DISCOVERY_EPOCH = datetime(2020, 1, 13, tzinfo=timezone.utc)
PROXIMA_DISCOVERY_EPOCH = datetime(2016, 8, 24, tzinfo=timezone.utc)

# ============================================================================
# TRAPPIST-1 SYSTEM
# ============================================================================
# Discovery: Gillon et al. 2017, Nature 542, 456-460
# Location: 12.43 pc in constellation Aquarius
# Spectral type: M8V ultracool red dwarf
# Notable: 3 planets in habitable zone (e, f, g)
# ============================================================================

TRAPPIST1_SYSTEM = {
    'system_name': 'TRAPPIST-1',
    'system_id': 'trappist1',
    'discovery_year': 2017,
    'distance_pc': 12.43,
    'distance_ly': 40.5,
    'constellation': 'Aquarius',
    'notable_features': [
        '7 terrestrial planets',
        '3 planets in habitable zone',
        'Orbital resonance chain',
        'Nearest 7-planet system'
    ],
    
    'host_star': {
        'name': 'TRAPPIST-1',
        'star_id': 'trappist1_star',
        'is_binary': False,
        
        # Position (J2000.0 epoch)
        'ra': 346.62201667,  # degrees (23h 06m 29.28s)
        'dec': -5.04138889,   # degrees (-05 deg 02' 29.0")
        'distance_pc': 12.43,
        
        # Proper motion (for animation across time)
        'pmra': 922.88,   # mas/year (includes cos(dec) factor)
        'pmdec': -469.24, # mas/year
        'epoch': J2000,
        
        # Stellar properties
        'spectral_type': 'M8V',
        'mass_solar': 0.0898,      # +/-0.0023 solar masses
        'radius_solar': 0.1192,     # +/-0.0013 solar radii
        'teff_k': 2566,             # +/-26 K
        'luminosity_solar': 0.000525,
        'age_gyr': 7.6,             # +/-2.2 Gyr
        
        # Habitable zone boundaries (conservative estimate)
        'habitable_zone_inner_au': 0.025,
        'habitable_zone_outer_au': 0.050,
        
        'mission_info': 'Ultra-cool red dwarf hosting 7 Earth-sized planets discovered by TRAPPIST telescope.',
        'mission_url': 'https://exoplanets.nasa.gov/trappist1/',
        'simbad_id': '2MASS J23062928-0502285'
    },
    
    'planets': [
        {
            'name': 'TRAPPIST-1 b',
            'planet_id': 'trappist1b',
            'letter': 'b',
            
            # Orbital elements
            'period_days': 1.51087081,       # +/-0.00000060
            'semi_major_axis_au': 0.01154,   # +/-0.00004
            'eccentricity': 0.00622,         # +/-0.00304
            'inclination_deg': 89.728,       # +/-0.087 (edge-on, transiting)
            'omega_deg': 0.0,                # Not well constrained, assume 0
            'Omega_deg': 0.0,                # Sky-plane orientation
            'epoch': TRAPPIST1_DISCOVERY_EPOCH,
            
            # Physical properties
            'mass_earth': 1.374,      # +/-0.069
            'radius_earth': 1.116,    # +/-0.014
            'density_earth': 0.98,    # Relative to Earth
            'equilibrium_temp_k': 400,
            'insolation_earth': 4.25, # Stellar flux relative to Earth
            
            # Discovery information
            'discovery_method': 'Transit',
            'discovery_year': 2016,
            'discovery_facility': 'TRAPPIST-South',
            'in_habitable_zone': False,
            
            # Data quality flags
            'e_assumed': False,  # Eccentricity measured
            'i_assumed': False,  # Inclination measured (transiting)
            'omega_assumed': True,  # Argument of periastron not constrained
            
            'mission_info': 'Innermost planet, receives 4x Earth\'s stellar flux. Too hot for liquid water.',
            'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7913/trappist-1-b/'
        },
        
        {
            'name': 'TRAPPIST-1 c',
            'planet_id': 'trappist1c',
            'letter': 'c',
            
            'period_days': 2.42182151,
            'semi_major_axis_au': 0.01580,
            'eccentricity': 0.00654,
            'inclination_deg': 89.778,
            'omega_deg': 0.0,
            'Omega_deg': 0.0,
            'epoch': TRAPPIST1_DISCOVERY_EPOCH,
            
            'mass_earth': 1.308,
            'radius_earth': 1.097,
            'density_earth': 1.05,
            'equilibrium_temp_k': 342,
            'insolation_earth': 2.27,
            
            'discovery_method': 'Transit',
            'discovery_year': 2016,
            'discovery_facility': 'TRAPPIST-South',
            'in_habitable_zone': False,
            
            'e_assumed': False,
            'i_assumed': False,
            'omega_assumed': True,
            
            'mission_info': 'Second planet, likely rocky with no significant atmosphere (JWST observations).',
            'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7914/trappist-1-c/'
        },
        
        {
            'name': 'TRAPPIST-1 d',
            'planet_id': 'trappist1d',
            'letter': 'd',
            
            'period_days': 4.04961,
            'semi_major_axis_au': 0.02227,
            'eccentricity': 0.00837,
            'inclination_deg': 89.896,
            'omega_deg': 0.0,
            'Omega_deg': 0.0,
            'epoch': TRAPPIST1_DISCOVERY_EPOCH,
            
            'mass_earth': 0.388,
            'radius_earth': 0.788,
            'density_earth': 0.72,
            'equilibrium_temp_k': 288,
            'insolation_earth': 1.15,
            
            'discovery_method': 'Transit',
            'discovery_year': 2016,
            'discovery_facility': 'TRAPPIST-South',
            'in_habitable_zone': True,  # At inner edge
            
            'e_assumed': False,
            'i_assumed': False,
            'omega_assumed': True,
            
            'mission_info': 'Smallest planet in system, at inner edge of habitable zone. May have water.',
            'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7915/trappist-1-d/'
        },
        
        {
            'name': 'TRAPPIST-1 e',
            'planet_id': 'trappist1e',
            'letter': 'e',
            
            'period_days': 6.09965,
            'semi_major_axis_au': 0.02925,
            'eccentricity': 0.00510,
            'inclination_deg': 89.793,
            'omega_deg': 0.0,
            'Omega_deg': 0.0,
            'epoch': TRAPPIST1_DISCOVERY_EPOCH,
            
            'mass_earth': 0.692,
            'radius_earth': 0.920,
            'density_earth': 0.93,
            'equilibrium_temp_k': 251,
            'insolation_earth': 0.66,
            
            'discovery_method': 'Transit',
            'discovery_year': 2017,
            'discovery_facility': 'Spitzer Space Telescope',
            'in_habitable_zone': True,  # Prime candidate!
            
            'e_assumed': False,
            'i_assumed': False,
            'omega_assumed': True,
            
            'mission_info': 'Most likely to have liquid water! Similar size to Earth, in optimal habitable zone.',
            'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7916/trappist-1-e/'
        },
        
        {
            'name': 'TRAPPIST-1 f',
            'planet_id': 'trappist1f',
            'letter': 'f',
            
            'period_days': 9.20669,
            'semi_major_axis_au': 0.03849,
            'eccentricity': 0.01007,
            'inclination_deg': 89.740,
            'omega_deg': 0.0,
            'Omega_deg': 0.0,
            'epoch': TRAPPIST1_DISCOVERY_EPOCH,
            
            'mass_earth': 1.039,
            'radius_earth': 1.045,
            'density_earth': 0.93,
            'equilibrium_temp_k': 219,
            'insolation_earth': 0.38,
            
            'discovery_method': 'Transit',
            'discovery_year': 2017,
            'discovery_facility': 'Spitzer Space Telescope',
            'in_habitable_zone': True,
            
            'e_assumed': False,
            'i_assumed': False,
            'omega_assumed': True,
            
            'mission_info': 'In habitable zone, may have significant water content. JWST target.',
            'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7917/trappist-1-f/'
        },
        
        {
            'name': 'TRAPPIST-1 g',
            'planet_id': 'trappist1g',
            'letter': 'g',
            
            'period_days': 12.35294,
            'semi_major_axis_au': 0.04683,
            'eccentricity': 0.00208,
            'inclination_deg': 89.721,
            'omega_deg': 0.0,
            'Omega_deg': 0.0,
            'epoch': TRAPPIST1_DISCOVERY_EPOCH,
            
            'mass_earth': 1.321,
            'radius_earth': 1.129,
            'density_earth': 0.92,
            'equilibrium_temp_k': 199,
            'insolation_earth': 0.26,
            
            'discovery_method': 'Transit',
            'discovery_year': 2017,
            'discovery_facility': 'Spitzer Space Telescope',
            'in_habitable_zone': True,  # Outer edge
            
            'e_assumed': False,
            'i_assumed': False,
            'omega_assumed': True,
            
            'mission_info': 'At outer edge of habitable zone, may have subsurface ocean.',
            'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7918/trappist-1-g/'
        },
        
        {
            'name': 'TRAPPIST-1 h',
            'planet_id': 'trappist1h',
            'letter': 'h',
            
            'period_days': 18.76712,
            'semi_major_axis_au': 0.06189,
            'eccentricity': 0.00567,
            'inclination_deg': 89.796,
            'omega_deg': 0.0,
            'Omega_deg': 0.0,
            'epoch': TRAPPIST1_DISCOVERY_EPOCH,
            
            'mass_earth': 0.326,
            'radius_earth': 0.755,
            'density_earth': 0.66,
            'equilibrium_temp_k': 173,
            'insolation_earth': 0.16,
            
            'discovery_method': 'Transit',
            'discovery_year': 2017,
            'discovery_facility': 'Spitzer Space Telescope',
            'in_habitable_zone': False,  # Too cold
            
            'e_assumed': False,
            'i_assumed': False,
            'omega_assumed': True,
            
            'mission_info': 'Outermost planet, likely too cold for liquid water. Low density suggests icy composition.',
            'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7919/trappist-1-h/'
        }
    ]
}

# ============================================================================
# TOI-1338 SYSTEM (Circumbinary)
# ============================================================================
# Discovery: Kostov et al. 2020, AJ 159, 253
# Discovered by: Wolf Cukier (17-year-old TESS intern)
# Location: ~396 pc in constellation Pictor
# Notable: First TESS circumbinary planet ("Real Tatooine")
# ============================================================================

TOI1338_SYSTEM = {
    'system_name': 'TOI-1338 / BEBOP-1',
    'system_id': 'toi1338',
    'discovery_year': 2020,
    'distance_pc': 396,
    'distance_ly': 1292,
    'constellation': 'Pictor',
    'notable_features': [
        'Circumbinary planet (orbits two stars)',
        'Discovered by high school student',
        'First TESS circumbinary discovery',
        'Multi-planet circumbinary system',
        '"Real Tatooine"'
    ],
    
    'host_star': {
        'name': 'TOI-1338 A/B',
        'star_id': 'toi1338_barycenter',
        'is_binary': True,
        
        # Binary system position (J2000.0 epoch)
        'ra': 56.5,      # degrees (approximate)
        'dec': -59.8,    # degrees (approximate)
        'distance_pc': 396,
        
        # Proper motion (small for distant system)
        'pmra': 5.2,     # mas/year
        'pmdec': -2.1,   # mas/year
        'epoch': J2000,
        
        # Binary orbit parameters
        'binary_period_days': 14.6,
        'binary_separation_au': 0.088,  # Semi-major axis of binary orbit
        'binary_eccentricity': 0.16,
        'binary_inclination_deg': 89.0,  # Same as planet inclination - coplanar system
        'binary_Omega_deg': 0.0,  # Longitude of ascending node        
        
        # Primary star (TOI-1338 A)
        'star_A': {
            'name': 'TOI-1338 A',
            'star_id': 'toi1338_starA',
            'spectral_type': 'G-type',  # Similar to Sun
            'mass_solar': 1.1,
            'radius_solar': 1.44,
            'teff_k': 6100,
            'luminosity_solar': 2.0
        },
        
        # Secondary star (TOI-1338 B)
        'star_B': {
            'name': 'TOI-1338 B',
            'star_id': 'toi1338_starB',
            'spectral_type': 'M-type',  # Red dwarf
            'mass_solar': 0.3,
            'radius_solar': 0.29,
            'teff_k': 3450,
            'luminosity_solar': 0.015
        },
        
        # Combined system properties
        'total_mass_solar': 1.4,
        'combined_luminosity_solar': 2.015,
        
        # Habitable zone (based on combined luminosity)
        'habitable_zone_inner_au': 1.0,
        'habitable_zone_outer_au': 1.6,
        
        'mission_info': 'Binary star system with circumbinary planets. First discovered by TESS.',
        'mission_url': 'https://exoplanets.nasa.gov/news/1644/discovery-alert-first-planet-found-by-tess/',
        'simbad_id': 'TIC 260128333'
    },
    
    'planets': [
        {
            'name': 'TOI-1338 b',
            'planet_id': 'toi1338b',
            'letter': 'b',
            
            # Orbital elements (around binary barycenter)
            'period_days': 95.196,           # +/-0.024
            'semi_major_axis_au': 0.4607,    # +/-0.0058
            'eccentricity': 0.09,            # +/-0.03
            'inclination_deg': 89.0,         # Nearly edge-on
            'omega_deg': 0.0,                # Not well constrained
            'Omega_deg': 0.0,
            'epoch': TOI1338_DISCOVERY_EPOCH,
            
            # Physical properties
            'mass_jupiter': 0.107,           # ~22 Earth masses (uncertain)
            'mass_earth': 22.0,              # Best estimate
            'radius_jupiter': 0.635,
            'radius_earth': 6.9,
            'density_earth': 0.15,           # Very low - suggests gas giant
            'equilibrium_temp_k': 250,
            'insolation_earth': 0.22,
            
            # Discovery information
            'discovery_method': 'Transit',
            'discovery_year': 2020,
            'discovery_facility': 'TESS',
            'discoverer': 'Wolf Cukier (17-year-old intern)',
            'in_habitable_zone': False,
            
            # Data quality
            'e_assumed': False,
            'i_assumed': False,
            'omega_assumed': True,
            
            'mission_info': 'Neptune-sized circumbinary planet discovered by high school intern Wolf Cukier. Transits are irregular due to binary stellar motion.',
            'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/8452/toi-1338-b/'
        },
        
        {
            'name': 'TOI-1338 c',
            'planet_id': 'toi1338c',
            'letter': 'c',
            
            # Orbital elements (confirmed 2023)
            'period_days': 215.5,            # +/-2.5
            'semi_major_axis_au': 0.76,      # Estimated
            'eccentricity': 0.0,             # Assumed circular
            'inclination_deg': 89.5,         # Assumed similar to b
            'omega_deg': 0.0,
            'Omega_deg': 0.0,
            'epoch': datetime(2023, 6, 1, tzinfo=timezone.utc),
            
            # Physical properties (estimated)
            'mass_earth': 65.0,              # Jupiter-like mass
            'radius_earth': 11.0,            # Estimated, not transiting
            'density_earth': 0.2,
            'equilibrium_temp_k': 180,
            'insolation_earth': 0.08,
            
            # Discovery information
            'discovery_method': 'Radial Velocity',
            'discovery_year': 2023,
            'discovery_facility': 'BEBOP survey',
            'in_habitable_zone': False,
            
            # Data quality
            'e_assumed': True,
            'i_assumed': True,
            'omega_assumed': True,
            
            'mission_info': 'Second planet in system, discovered via radial velocity. Makes this only the second known multi-planet circumbinary system.',
            'mission_url': 'https://arxiv.org/abs/2305.16894'
        }
    ]
}

# ============================================================================
# PROXIMA CENTAURI SYSTEM
# ============================================================================
# Discovery: Anglada-Escude et al. 2016, Nature 536, 437-440
# Location: 1.30 pc (4.24 ly) - NEAREST star system
# Spectral type: M5.5Ve red dwarf
# Notable: Nearest exoplanet, high proper motion, potentially habitable
# ============================================================================

PROXIMA_SYSTEM = {
    'system_name': 'Proxima Centauri',
    'system_id': 'proxima',
    'discovery_year': 2016,
    'distance_pc': 1.3012,
    'distance_ly': 4.244,
    'constellation': 'Centaurus',
    'notable_features': [
        'NEAREST exoplanet to Earth',
        'Part of Alpha Centauri system',
        'High proper motion (3.85 "/yr)',
        'Potentially habitable planet',
        'Multiple planets confirmed'
    ],
    
    'host_star': {
        'name': 'Proxima Centauri',
        'star_id': 'proxima_star',
        'is_binary': False,
        
        # Position (J2000.0 epoch)
        'ra': 217.42894167,  # degrees (14h 29m 42.95s)
        'dec': -62.67948333, # degrees (-62 deg 40' 46.14")
        'distance_pc': 1.3012,
        
        # Proper motion (VERY HIGH - nearest star)
        'pmra': 3853.92,     # mas/year (huge!)
        'pmdec': -768.34,    # mas/year
        'epoch': J2000,
        
        # Stellar properties
        'spectral_type': 'M5.5Ve',
        'mass_solar': 0.1221,
        'radius_solar': 0.1542,
        'teff_k': 3042,
        'luminosity_solar': 0.00155,
        'age_gyr': 4.85,
        
        # Habitable zone
        'habitable_zone_inner_au': 0.023,
        'habitable_zone_outer_au': 0.054,
        
        'mission_info': 'Nearest star to the Sun, red dwarf with at least 3 confirmed planets.',
        'mission_url': 'https://exoplanets.nasa.gov/proxima-b/',
        'simbad_id': 'V* V645 Cen'
    },
    
    'planets': [
        {
            'name': 'Proxima Centauri b',
            'planet_id': 'proximab',
            'letter': 'b',
            
            # Orbital elements
            'period_days': 11.18427,
            'semi_major_axis_au': 0.04856,
            'eccentricity': 0.0,              # Assumed circular
            'inclination_deg': 60.0,          # Estimated (not transiting)
            'omega_deg': 0.0,
            'Omega_deg': 0.0,
            'epoch': PROXIMA_DISCOVERY_EPOCH,
            
            # Physical properties
            'mass_earth': 1.27,               # Minimum mass (M sin i)
            'radius_earth': 1.1,              # Estimated
            'density_earth': 1.0,             # Assumed Earth-like
            'equilibrium_temp_k': 234,
            'insolation_earth': 0.65,
            
            # Discovery information
            'discovery_method': 'Radial Velocity',
            'discovery_year': 2016,
            'discovery_facility': 'ESO 3.6m + HARPS',
            'in_habitable_zone': True,        # Prime target!
            
            # Data quality
            'e_assumed': True,
            'i_assumed': True,
            'omega_assumed': True,
            
            'mission_info': 'Nearest exoplanet to Earth! In habitable zone but stellar flares may make habitability challenging.',
            'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7167/proxima-centauri-b/'
        },
        
        {
            'name': 'Proxima Centauri d',
            'planet_id': 'proximad',
            'letter': 'd',
            
            # Orbital elements (innermost, confirmed 2022)
            'period_days': 5.122,
            'semi_major_axis_au': 0.029,
            'eccentricity': 0.0,
            'inclination_deg': 60.0,
            'omega_deg': 0.0,
            'Omega_deg': 0.0,
            'epoch': datetime(2022, 2, 10, tzinfo=timezone.utc),
            
            # Physical properties
            'mass_earth': 0.26,              # Sub-Earth mass
            'radius_earth': 0.81,            # Estimated
            'density_earth': 0.9,
            'equilibrium_temp_k': 330,
            'insolation_earth': 1.9,
            
            # Discovery information
            'discovery_method': 'Radial Velocity',
            'discovery_year': 2022,
            'discovery_facility': 'VLT + ESPRESSO',
            'in_habitable_zone': False,
            
            # Data quality
            'e_assumed': True,
            'i_assumed': True,
            'omega_assumed': True,
            
            'mission_info': 'Lightest planet detected by radial velocity method. Too close to star for habitability.',
            'mission_url': 'https://www.eso.org/public/news/eso2202/'
        }
    ]
}

# ============================================================================
# CATALOG DICTIONARY - Easy access to all systems
# ============================================================================

EXOPLANET_CATALOG = {
    'trappist1': TRAPPIST1_SYSTEM,
    'toi1338': TOI1338_SYSTEM,
    'proxima': PROXIMA_SYSTEM
}

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_system(system_id):
    """
    Get exoplanet system by ID
    
    Parameters:
        system_id: str - System identifier ('trappist1', 'toi1338', 'proxima')
        
    Returns:
        dict: System data or None if not found
    """
    return EXOPLANET_CATALOG.get(system_id)

def get_all_systems():
    """Get list of all available system IDs"""
    return list(EXOPLANET_CATALOG.keys())

def get_system_summary(system_id):
    """
    Get quick summary of system for GUI display
    
    Returns:
        str: Human-readable summary
    """
    system = get_system(system_id)
    if not system:
        return "System not found"
    
    n_planets = len(system['planets'])
    distance = system['distance_ly']
    
    summary = f"{system['system_name']}: {n_planets} planet"
    if n_planets != 1:
        summary += "s"
    summary += f" at {distance:.1f} light-years"
    
    if system['host_star'].get('is_binary'):
        summary += " (binary star)"
    
    return summary

def get_planets_in_hz(system_id):
    """
    Get list of planets in habitable zone
    
    Returns:
        list: Planet names in HZ
    """
    system = get_system(system_id)
    if not system:
        return []
    
    return [p['name'] for p in system['planets'] if p.get('in_habitable_zone', False)]

if __name__ == "__main__":
    # Test the catalog
    print("Exoplanet Systems Catalog")
    print("=" * 60)
    
    for sys_id in get_all_systems():
        system = get_system(sys_id)
        print(f"\n{system['system_name']}")
        print(f"  Distance: {system['distance_ly']:.1f} light-years")
        print(f"  Planets: {len(system['planets'])}")
        
        hz_planets = get_planets_in_hz(sys_id)
        if hz_planets:
            print(f"  In HZ: {', '.join(hz_planets)}")
        
        for planet in system['planets']:
            hz_mark = " [HZ]" if planet.get('in_habitable_zone') else ""
            print(f"    * {planet['name']}: {planet['period_days']:.2f} days{hz_mark}")
