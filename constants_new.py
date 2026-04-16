"""
constants_new.py - Verified numeric constants for Paloma's Orrery.

Single source of truth for all physical constants, orbital periods,
body radii, and color mappings. Every propagating constant has a
source citation and verification date. Derived values are computed
from primary constants -- never hardcoded independently.

Import from this module. Do not redefine these values locally.
See provenance_scanner.py for audit, module_atlas.py for consumers.

Verification process (April 2026):
    1. Claude sourced constants from IAU resolutions and NASA fact sheets
    2. Google Gemini reviewed all values against authoritative sources
    3. Gemini caught two errors Claude introduced during verification:
       - Arrokoth radius: 0.0088 km (8.8 m!) -> 9.95 km (actual mean)
       - Parker closest approach: 8.86 R_sun (surface altitude)
         -> 9.86 R_sun (from Sun center, consistent with shell radii);
         perihelion number corrected from 21 to 22
    4. Tony integrated corrections and made final decisions

Revised 2026-04-16 by Anthropic's Claude Opus 4.6 and Google Gemini:
    - CENTER_BODY_RADII convention changed from volumetric mean to
      hybrid (equatorial for major planets, volumetric for small
      bodies). Rationale: shell modules scale by R_body as a unit
      of measure (e.g. 5.9 R_J for Io torus), and planetary-science
      literature cites these fractions against equatorial radii.
      Volumetric mean introduced silent ~2.3% position errors.
    - Parker Solar Probe closest approach: 8.86 -> 9.86 R_sun was
      correctly applied; this revision does not affect Parker.    

Lesson: Verification by the same AI that generated the value is not
verification. Cross-AI review (Mode 7) is load-bearing for facts.

Module updated: April 2026 with Anthropic's Claude Opus 4.6
Reviewed: April 2026 by Google Gemini (Mode 7 cross-verification)
"""

import numpy as np
from datetime import datetime, timedelta


# ============================================================
# FUNDAMENTAL CONSTANTS (IAU-defined, exact)
# ============================================================

KM_PER_AU = 149597870.7
# Source: IAU 2012 Resolution B2 -- exact definition
# Ref: https://syrte.obspm.fr/IAU_resolutions/Res_IAU2012_B2.pdf
# Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/fact_notes.html
# Verified: 2026-04-15
# Note: 1 AU = 149,597,870,700 m exactly. We use km (divide by 1000).

SUN_RADIUS_KM = 695700.0
# Source: IAU 2015 Resolution B3 -- nominal solar radius
# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)
# Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html
# Verified: 2026-04-15
# Note: This is the IAU nominal value (conversion constant), not a
# measurement. The measured photospheric radius is ~696,340 km
# (Haberreiter et al. 2008). Use nominal for all calculations.

EARTH_EQUATORIAL_RADIUS_KM = 6378.137
# Source: IAU 2015 Resolution B3 -- nominal terrestrial equatorial radius
# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)
# Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
# Verified: 2026-04-15

EARTH_POLAR_RADIUS_KM = 6356.752
# Source: IAU 2015 Resolution B3 -- nominal terrestrial polar radius
# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)
# Verified: 2026-04-15

JUPITER_EQUATORIAL_RADIUS_KM = 71492.0
# Source: IAU 2015 Resolution B3 -- nominal jovian equatorial radius
# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)
# Verified: 2026-04-15

JUPITER_POLAR_RADIUS_KM = 66854.0
# Source: IAU 2015 Resolution B3 -- nominal jovian polar radius
# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)
# Verified: 2026-04-15

SPEED_OF_LIGHT_KM_S = 299792.458
# Source: NIST/SI exact definition
# Ref: https://physics.nist.gov/cgi-bin/cuu/Value?c
# Verified: 2026-04-15


# ============================================================
# DERIVED CONSTANTS (computed from primaries above)
# ============================================================
# Do not hardcode these values. They are computed to ensure
# consistency with the IAU primary definitions.

SOLAR_RADIUS_AU = SUN_RADIUS_KM / KM_PER_AU
# Derived: 695700 / 149597870.7 = 0.004650467...
# Previous hardcoded value was 0.00465047 (consistent to 6 sig figs)

LIGHT_MINUTES_PER_AU = KM_PER_AU / SPEED_OF_LIGHT_KM_S / 60.0
# Derived: 149597870.7 / 299792.458 / 60 = 8.31675...
# Previous hardcoded value was 8.3167 (consistent to 5 sig figs)


# ============================================================
# GUI CONSTANTS (application settings, not physical)
# ============================================================

DEFAULT_MARKER_SIZE = 7
HORIZONS_MAX_DATE = datetime(2199, 12, 29, 0, 0, 0)
CENTER_MARKER_SIZE = 10  # For central objects like the Sun


# ============================================================
# SOLAR STRUCTURE (in AU unless noted)
# ============================================================
# Interior boundaries are approximate; based on standard solar models.
# Source: Carroll & Ostlie, "Introduction to Modern Astrophysics" (2017)
# Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html
# Verified: 2026-04-15

CORE_AU = 0.2 * SOLAR_RADIUS_AU
# Derived: core extends to ~0.2 solar radii
# Source: Standard solar model (Bahcall et al.)

RADIATIVE_ZONE_AU = 0.7 * SOLAR_RADIUS_AU
# Derived: radiative zone extends to ~0.7 solar radii
# Source: Standard solar model

# Solar atmosphere (in solar radii)
CHROMOSPHERE_RADII = 1.5
# Source: Carroll & Ostlie (2017), Ch. 11
# Note: Chromosphere extends from photosphere (~1.0) to ~1.5 R_sun
# Verified: 2026-04-15

INNER_CORONA_RADII = 3
# Source: Golub & Pasachoff, "The Solar Corona" (2010)
# Note: Inner (K-)corona extends to 2-3 R_sun
# Verified: 2026-04-15

OUTER_CORONA_RADII = 50
# Source: Various; F-corona envelope extends to ~50 R_sun
# Ref: Mann et al. (2004), A&A 414:1127
# Verified: 2026-04-15

# New shells (added April 2026)
STREAMER_BELT_RADII = 6.0
# Source: Eclipse observations; helmet streamers extend 4-6 R_sun
# Ref: Golub & Pasachoff (2010); DeForest et al. (2018)
# Verified: 2026-04-15

ROCHE_LIMIT_RADII = 3.45
# Source: Fluid Roche limit formula: d = 2.44 * R * (rho_sun/rho_comet)^(1/3)
# Calculation: 2.44 * 1.0 * (1408/500)^(1/3) = 3.45 R_sun
# Using rho_sun = 1408 kg/m3, rho_comet ~ 500 kg/m3
# Ref: Murray & Dermott, "Solar System Dynamics" (1999), Sec. 4.6
# Verified: 2026-04-15
# Note: Roche limit is NOT absolute; tensile strength allows survival
# inside it. Ikeya-Seki survived at 1.66 R_sun.

ALFVEN_SURFACE_RADII = 18.8
# Source: Parker Solar Probe first crossing, April 28, 2021
# Ref: Kasper et al. (2021), Phys. Rev. Lett. 127:255101
# Also: https://www.nasa.gov/feature/goddard/2021/nasa-enters-the-solar-atmosphere
# Verified: 2026-04-15
# Note: Varies 10-20 R_sun with solar activity; 18.8 is the measured crossing


# ============================================================
# HELIOSPHERE BOUNDARIES (in AU)
# ============================================================

TERMINATION_SHOCK_AU = 94
# Source: Voyager 1 crossed at 94 AU (Dec 2004)
# Ref: Stone et al. (2005), Science 309:2017
# Also: Voyager 2 crossed at 84 AU (Aug 2007) -- asymmetric
# Verified: 2026-04-15

HELIOPAUSE_RADII = 26449
# Note: This is in solar radii, not AU. ~123 AU = 123 * 149597870.7 / 695700 = 26449 R_sun
# Source: Voyager 1 crossed heliopause at ~121.6 AU (Aug 2012)
# Ref: Gurnett et al. (2013), Science 341:1489
# Verified: 2026-04-15
# Gemini confirmed: conversion math is correct (123 AU -> 26449 R_sun)
# TODO: Consider renaming to HELIOPAUSE_AU = 123 for clarity

# Oort Cloud and gravitational influence (in AU)
INNER_LIMIT_OORT_CLOUD_AU = 2000
# Source: Hills (1981); Oort (1950) -- inner edge estimate
# Note: Highly uncertain; ranges 2000-5000 AU in literature

INNER_OORT_CLOUD_AU = 20000
# Source: Hills (1981) -- outer edge of inner (Hills) cloud
# Note: Boundary between inner and outer Oort cloud is uncertain

OUTER_OORT_CLOUD_AU = 100000
# Source: Oort (1950); Weissman (1996)
# Note: Estimated outer boundary, ~0.5 parsec

GRAVITATIONAL_INFLUENCE_AU = 126000
# Source: Approximate Hill sphere radius of Sun in Milky Way
# Note: ~2 light-years; depends on local stellar density
# Verified: 2026-04-15

# Spacecraft reference
PARKER_CLOSEST_RADII = 9.86
# Source: Parker Solar Probe perihelion 22, Dec 24, 2024
# Ref: https://parkersolarprobe.jhuapl.edu/The-Mission/index.php
# Verified: 2026-04-15
# Corrected: 2026-04-15 per Gemini review -- 8.86 was surface altitude,
#   9.86 is distance from Sun center (consistent with other shell radii).
#   Perihelion number corrected from 21 to 22.
# 9.86 R_sun = 6.86 million km = 0.0459 AU


# ============================================================
# CENTER BODY RADII (km)
# ============================================================
# Hybrid convention:
#   - Major planets (Earth through Neptune) + Sun + Pluto: equatorial
#     radius. Matches IAU 2015 nominal values and planetary-science
#     literature convention for "N radii" measurements (e.g. Io torus
#     at 5.9 R_J assumes equatorial = 71,492 km).
#   - Small bodies (Bennu, Eris, Haumea, Makemake, Arrokoth, Planet 9):
#     volumetric mean radius. "Equatorial" is not well-defined for
#     irregular or highly ellipsoidal bodies.
#   - Mercury, Venus, Moon: difference is sub-0.1%; volumetric retained.
#
# Sources:
#   IAU 2015 Resolution B3 (Prsa et al. 2016, AJ 152:41) for Sun,
#     Earth, Mars, Jupiter, Saturn, Uranus, Neptune nominal values.
#   NASA NSSDCA Planetary Fact Sheets for Mercury, Venus, Moon.
#   JPL Solar System Dynamics for dwarf planets / small bodies.
#   Nimmo et al. 2017 (Icarus) for Pluto.
# Ref: https://nssdc.gsfc.nasa.gov/planetary/factsheet/
# Ref: https://ssd.jpl.nasa.gov/planets/phys_par.html
# Verified: 2026-04-16 (equatorial convention adopted per downstream
#   usage analysis; prior volumetric values caused ~2.3% position error
#   for Jupiter-scaled shells like Io torus).

CENTER_BODY_RADII = {       # km (equatorial for major bodies, volumetric for small)
    'Sun':      695700,     # IAU 2015 nominal solar radius
    'Mercury':  2439.7,     # NASA Fact Sheet (volumetric mean; oblateness ~0.0009)
    'Venus':    6051.8,     # NASA Fact Sheet (volumetric mean; oblateness ~0)
    'Earth':    6378.137,   # IAU 2015 nominal equatorial (WGS-84; polar = 6356.752)
    'Moon':     1737.4,     # NASA Fact Sheet (volumetric mean; oblateness ~0.0012)
    'Mars':     3396.2,     # IAU 2015 nominal equatorial (volumetric = 3389.5)
    'Jupiter':  71492,      # IAU 2015 nominal equatorial (volumetric = 69911)
    'Saturn':   60268,      # IAU 2015 nominal equatorial (volumetric = 58232)
    'Uranus':   25559,      # IAU 2015 nominal equatorial (volumetric = 25362)
    'Neptune':  24764,      # IAU 2015 nominal equatorial (volumetric = 24622)
    'Pluto':    1188.3,     # New Horizons occultation (Nimmo et al. 2017)
    'Bennu':    0.262,      # Volumetric mean (top-shape asteroid, OSIRIS-REx)
    'Eris':     1163,       # Volumetric mean (Sicardy et al. 2011 occultation)
    'Haumea':   816,        # Volumetric mean (highly ellipsoidal: 1050x840x537 km)
    'Makemake': 715,        # Volumetric mean (Brown et al.)
    'Arrokoth': 9.95,       # Volumetric mean (~35x20x14 km bilobed shape)
                            # Corrected 2026-04-15 per Gemini review (was 0.0088 = 8.8 meters!)
    'Planet 9': 24000       # Model estimate (Batygin & Brown; 5-10 M_Earth assumption)
}

KNOWN_ORBITAL_PERIODS = {
    # Planets (converted from years to days)
    'Mercury': 87.969,      
    'Venus': 224.701,       
    'Earth': 365.256,       
    'Mars': 686.980,        
    'Jupiter': 4332.589,    
    'Saturn': 10759.22,   
    'Uranus': 30688.5,    
    'Neptune': 60189.0,   
    
    # Earth satellite
    'Moon': 27.321582,
    
    # Mars satellites
    'Phobos': 0.319,       # Verified from JPL
    'Deimos': 1.263,       # Verified from JPL
    
    # Jupiter satellites
    'Io': 1.769,           # 42.456 hours
    'Europa': 3.551,       # 85.224 hours
    'Ganymede': 7.155,     # 171.72 hours
    'Callisto': 16.689,    # 400.536 hours
    'Metis': 0.295,        # 7.08 hours
    'Adrastea': 0.298,     # 7.15 hours
    'Amalthea': 0.498,     # 11.95 hours
    'Thebe': 0.675,        # 16.20 hours
    
    # Saturn satellites
    'Mimas': 0.942,        # 22.61 hours
    'Enceladus': 1.370,    # 32.88 hours
    'Tethys': 1.888,       # 45.31 hours
    'Dione': 2.737,        # 65.69 hours
    'Rhea': 4.518,         # 108.43 hours
    'Titan': 15.945,       # 382.68 hours
    'Hyperion': 21.277,    # 510.65 hours
    'Iapetus': 79.331,     # 1903.94 hours
    'Phoebe': 550.56,      # 1.51 years
    'Pan': 0.575,          # 13.80 hours
    'Daphnis': 0.594,      # 14.26 hours
    'Atlas': 0.602,        # 14.45 hours
    'Prometheus': 0.616,   # 14.78 hours
    'Pandora': 0.631,      # 15.14 hours
    'Epimetheus': 0.694,   # 16.66 hours
    'Janus': 0.695,        # 16.68 hours
    
    # Uranus satellites
    'Miranda': 1.413,      # 33.91 hours
    'Ariel': 2.520,        # 60.48 hours
    'Umbriel': 4.144,      # 99.46 hours
    'Titania': 8.706,      # 208.94 hours
    'Oberon': 13.463,      # 323.11 hours
    'Puck': 0.762,         # 18.29 hours
    'Portia': 0.513,       # 12.31 hours
    'Mab': 0.923,          # 22.15 hours
    
    # Neptune satellites  
    'Triton': 5.877,       # 141.05 hours 
    'Despina': 0.335,      # 8.04 hours
    'Galatea': 0.429,      # 10.30 hours
    'Proteus': 1.122,      # 26.93 hours
    'Larissa': 0.555,      # 13.32 hours
    'Naiad': 0.294,        # 7.06 hours
    
    # Pluto satellites
    'Charon': 6.387,       # 153.29 hours
    'Styx': 20.162,        # 483.89 hours
    'Nix': 24.856,         # 596.54 hours
    'Kerberos': 32.168,    # 772.03 hours
    'Hydra': 38.202,       # 916.85 hours
        
    # Eris satellite
    'Dysnomia': 15.786,    # 378.86 hours
    
    # Gonggong satellite
    'Xiangliu': 25.22,      # Based on arXiv:2305.17175 (May 2023)

    # Orcus satellite
    'Vanth': 9.54,         # Based on arXiv:1509.01719 (Sept 2015)

    # Quaoar satellite
    'Weywot': 12.44,       # Based on arXiv:astro-ph/0405636 (May 2004)

    # Haumea satellites
    "Hi'iaka": 49.12,      # ~49 days
    'Namaka': 18.28,       # ~18 days (non-Keplerian due to Hi'iaka)
    
    # Makemake satellite
    'MK2': 18.0,           # Based on arXiv:2509.05880 (Sept 2025)
    
    # Dwarf planets and KBOs (converted from years to days)
    'Pluto': 90560.0,    
    'Ceres': 1680.15,      # 4.6 * 365.25
    'Eris': 203809.50,     # 558.0 * 365.25
    'Haumea': 103731.00,   # 284.0 * 365.25
    'Makemake': 111766.50, # 306.0 * 365.25
    'Quaoar': 105192.00,   # 288.0 * 365.25
    'Orcus': 90314.9912925,     # 247.26897 * 365.25; 247.26897
    'Ixion': 91239.49018,       # PER= 249.80011 jy
    'Mani': 99305.28767,        # PER= 271.88306 jy
    'GV9': 100352.0613,         # PER= 274.74897 jy
    'Varuna': 102799.14,
    'Arrokoth': 108224.98,
    'Gonggong': 201010.45,
    '2017 OF201': 10048413.07,

    # Sednoid Trans-Neptunian Objects
    'Ammonite': 1444383.67 ,     # PER 3954.53339 Julian years 
    'Sedna': 4163850.00,   # 11400.0 * 365.25
    'Leleakuhonua': 12643548.84594,  # Orbital period in days;  34616.15016 julian years x 365.25

    # Centaurs -- unstable objects between Jupiter and Neptune
    'Chariklo': 22996.00,         # PER= 62.95962 jy = 22996.00121 days 

    # Asteroids
    'Vesta': 1325.75,      # 3.63 * 365.25
    'Pallas': 1685.37,     # 4.614 * 365.25
    'Juno': 1591.93,       # 4.358 * 365.25  
    'Hygiea': 2041.88,     # 5.592 * 365.25
    'Psyche': 1825.01,     # 4.997 * 365.25
    'Eros': 642.63,        # 1.76 * 365.25
    'Itokawa': 556.38,     # 1.52 * 365.25
    'Ryugu': 473.98,       # 1.30 * 365.25
    'Bennu': 436.65,       # 1.20 * 365.25
    'Apophis': 323.60,     # 0.89 * 365.25
    'Phaethon': 523.42,    # 1.43 * 365.25
    'Dinkinesh': 1387.50,  # 3.80 * 365.25
    'Donaldjohanson': 1446.04, # 3.96 * 365.25
    'Steins': 1327.41,     # 3.64 * 365.25
    'Lutetia': 1321.00,    # 3.62 * 365.25
    
    # Trojan asteroids (Jupiter's L4 and L5)
    'Orus': 4274.32,       # 11.71 * 365.25
    'Polymele': 4319.33,   # 11.83 * 365.25
    'Eurybates': 4333.71,  # 11.87 * 365.25
    'Patroclus': 4336.36,  # 11.88 * 365.25
    'Menoetius': 4336.36,  # 11.88 * 365.25
    'Leucus': 4352.24,     # 11.92 * 365.25
    
    # Near-Earth asteroids
    '2024 YR4': 922.84,         # 2.53 * 365.25
    '2025 PN7': 367.5547275,    # 1.00631 * 365.25   
    '2024 PT5': 368.75,         # 1.01 * 365.25
    '2025 PY1': 409.072695,     # days from PER in julian years
    '2023 JF': 493.37,          # 1.35 * 365.25
    '2025 KV': 695.85,          # 1.91 * 365.25
    
    # Comets (converted from years to days where applicable)
    'Halley': 27731.29226,          # 75.92414033 * 365.25 = 27731.29226; EPOCH=  2439907.5 ! 1968-Feb-21.0000000
    'Hyakutake': 35773534.62,       # PER= 97942.599927659 jy
    'Hale-Bopp': 863279.5035,       # PER= 2363.5304681429 jy = 863279.5035
    'Ikeya-Seki': 319800.00,        # 876.0 * 365.25 (estimate)
    'ISON': 230970.00,              # 632.3 * 365.25 (pre-disruption)
    'SWAN': 8237831.493,            # PER= 22553.953438133 jy
    '6AC4721': 311232,              # Approximate period for sungrazer comet C/2026 A1. This is equivalent to roughly 852.1 years.
    'MAPS': 418226.4926,            # Approximate period for sungrazer comet C/2026 A1. This is equivalent to roughly 1145.041732 years.    
    'Lemmon': 492252.5179,          # PER= 1347.7139437075 jy    
    'Schaumasse': 3014.1,           # 8.252 years * 365.25 = 3014.1 days
    'Howell': 2009.4,              # ~5.5 years * 365.25 = 2009.375 days
    'Tempel 2': 1961.8,            # 5.37 years * 365.25 = 1961.4 days
  
    # For hyperbolic/parabolic objects, period is undefined
    'West': None,           # West (C/1975 V1-A);  Parabolic comet - effectively infinite period  
    'C/2025_K1': None,      # Hyperbolic comet - effectively infinite period
    'C/2025_K1-B': None,    # Hyperbolic fragment - escaping solar system
    'C/2025_K1-C': None,    # Technically ~13M year period, effectively infinite
    'C/2025_K1-D': None,    # Hyperbolic fragment - escaping solar system    
    'Borisov': None,        # Hyperbolic comet - effectively infinite period    
    'McNaught': None,       # Hyperbolic comet - effectively infinite period 
    'ATLAS': None,          # Hyperbolic comet -- infinite period   PER= 9.999999E99
    'PANSTARRS': None,      # PER= 9.999999E99 jy (hyperbolic)
    '3I/ATLAS': None,       # Interstellar hyperbolic object - effectively infinite period
    '1I/Oumuamua': None,    # Interstellar hyperbolic object - effectively infinite period  
    '2I/Borisov': None,     # Interstellar hyperbolic object - effectively infinite period
    'Wierzchos': None,      # Near-parabolic, outbound ~200,000 years; effectively open trajectory     
    
    # Hypothetical
    'Planet 9': 3652500.00, # ~10000 * 365.25 (estimated)
}

# Mapping of SIMBAD object types to full descriptions



# Function to map celestial objects to colors
def color_map(planet):
    colors = {
        'Sun': 'rgb(102, 187, 106)',      # chlorophyll green
    #    'Sun': 'rgb(255, 249, 240)',  # Slightly warm white to represent 6000K at the Sun's surface. The inner corona is 2M K.
        'Mercury': 'rgb(128, 128, 128)',   # Description: Dark Gray reflecting Mercury's rocky and heavily cratered surface.
        'Venus': 'rgb(255, 255, 224)',
        'Earth': 'rgb(0, 102, 204)',
        'Moon': 'rgb(211, 211, 211)',
        'Mars': 'rgb(188, 39, 50)',
        'Phobos': 'rgb(139, 0, 0)',
        'Deimos': 'rgb(105, 105, 105)',
        'Ceres': 'rgb(105, 105, 105)',

        'Jupiter': 'rgb(255, 165, 0)',
        'Io': 'rgb(255, 140, 0)',
        'Europa': 'rgb(173, 216, 230)',
        'Ganymede': 'rgb(150, 75, 0)',
        'Callisto': 'rgb(169, 169, 169)',
        'Metis': 'rgb(180, 120, 100)',    # Reddish-brown
        'Adrastea': 'rgb(190, 150, 130)',  # Light reddish-brown
        'Amalthea': 'rgb(200, 60, 50)',    # Red
        'Thebe': 'rgb(170, 110, 90)',       # Dark reddish-brown

        'Saturn': 'rgb(210, 180, 140)',
        'Titan': 'rgb(255, 215, 0)',
        'Enceladus': 'rgb(192, 192, 192)',
        'Rhea': 'rgb(211, 211, 211)',
        'Dione': 'rgb(255, 182, 193)',
        'Tethys': 'rgb(173, 216, 230)',
        'Mimas': 'rgb(105, 105, 105)',
        'Pan': 'rgb(180, 180, 180)',            # (Light Gray)
        'Daphnis': 'rgb(190, 190, 190)',        # (Slightly lighter gray)
        'Prometheus': 'rgb(170, 170, 170)',     # (Medium Gray)
        'Pandora': 'rgb(185, 185, 185)',        # (Light-Medium Gray)
        'Hyperion': 'rgb(160, 100, 80)',        # (Dark reddish-brown)
        'Iapetus': 'rgb(220, 220, 220)',        # Trailing Hemisphere: (220, 220, 220) (Light Gray/Whitish); 
                                                # Leading Hemisphere (Cassini Regio): (50, 50, 50) (Very dark gray/almost black) 
        'Phoebe': 'cyan',

        'Uranus': 'rgb(173, 216, 230)',
        'Titania': 'rgb(221, 160, 221)',         
        'Oberon': 'rgb(128, 0, 128)',
        'Umbriel': 'rgb(148, 0, 211)',    
        'Ariel': 'rgb(144, 238, 144)',
        'Miranda': 'rgb(0, 128, 0)',
        'Portia': 'rgb(150, 150, 150)',
        'Mab': 'rgb(100, 100, 120)',

        'Neptune': 'rgb(0, 0, 255)',
        'Triton': 'rgb(0, 255, 255)',
        'Despina': 'rgb(175, 175, 175)',
        'Galatea': 'rgb(175, 175, 175)',

        'Pluto': 'rgb(205, 92, 92)',
        'Charon': 'rgb(169, 169, 169)',
        'Styx': 'rgb(180, 180, 180)',
        'Nix': 'rgb(200, 200, 200)',  
        'Kerberos': 'rgb(170, 170, 170)',      
        'Hydra': 'rgb(190, 190, 190)', 

        'Planet 9': 'grey',  # grey
       
        'Voyager 1': 'white',
        'Voyager 2': 'gold',
        'Cassini': 'green',
        'New Horizons': 'cyan',
        'Arrokoth': 'red',
        'Juno': 'cyan',
        'Galileo': 'white',
        'Apollo 11 S-IVB': 'cyan', 
        'Artemis II': 'gold',       
        'Pioneer 10': 'red',
        'Pioneer 11': 'green',
        'Clipper': 'red',
        'JUICE': 'blue', 
        'OSIRIS': 'cyan',
        'Parker': 'white',
        'JWST': 'gold',
        'Rosetta': 'white',
        'BepiColombo': 'red',
        'SolO': 'red',
        'SOHO': 'green',
        'Akatsuki': 'cyan',
        'MarsRover': 'white',

        'EM-L1': 'cyan',        
        'EM-L2': 'white',
        'EM-L3': 'green',
        'EM-L4': 'gold',
        'EM-L5': 'red',
        'L1': 'cyan',        
        'L2': 'white',
        'L3': 'green',
        'L4': 'gold',
        'L5': 'red',

        'Kamo oalewa': 'cyan',
        '2025 PN7': 'gold',        
        '2024 PT5': 'red',
        '2025 PY1': 'white',
        '2023 JF': 'white',
        '2024 DW': 'gold',        
        '2024 YR4': 'green',

        'Apophis': 'red',
        'Vesta': 'cyan',
        'Bennu': 'white',
        'Lutetia': 'green',
        'Steins': 'red',  

        '1I/Oumuamua': 'gold',
        '3I/ATLAS': 'red',
        'Ikeya-Seki': 'green',
        'West': 'red',
        'Halley': 'cyan',
        'Hyakutake': 'white',
        'Hale-Bopp': 'gold',
        'McNaught': 'green',
        'NEOWISE': 'red',
        'C/2025_K1': 'cyan',
        'C/2025_K1-B': 'rgb(0, 200, 220)',          # Teal - darker cyan variant
        'C/2025_K1-C': 'rgb(255, 215, 0)',           # Gold - the bound fragment (special!)
        'C/2025_K1-D': 'rgb(100, 180, 255)',          # Sky blue - cooler variant        
        'Borisov': 'green',        
        'Tsuchinshan': 'cyan',
        'ATLAS': 'white',
        'Churyumov': 'gold',
        '2I/Borisov': 'red',
        'SWAN': 'gold',
        'PANSTARRS': 'green',
        '6AC4721': 'cyan',
        'MAPS': 'cyan',
        'Lemmon': 'green',  
        'Wierzchos': 'cyan',
        'Schaumasse': 'gold',
        'Howell': 'white',
        'Tempel 2': 'red',             

        'SOHO': 'white',
        'JamesWebb': 'gold',
        'Ryugu': 'gold',
        'Eros': 'green',
        'Dinkinesh': 'white',
        'Donaldjohanson': 'red',
        'Eurybates': 'green',
        'Patroclus': 'white',
        'Menoetius': 'red',
        'Leucus': 'gold',
        'Polymele': 'cyan',
        'Orus': 'pink',
        'Itokawa': 'red',
        'MarsRover': 'white',
        'DART': 'gold',
        'Lucy': 'green',
        'Gaia': 'red',
        'Hayabusa2': 'cyan',  
        'Quaoar': 'rgb(244, 164, 96)',
        'Dysnomia': 'white',
        'Xiangliu': 'rgb(210, 105, 30)',
        'Vanth': 'rgb(169, 169, 169)',
        'Weywot': 'rgb(205, 133, 63)',
        "Hi'iaka": 'rgb(200, 180, 220)',    # Light purple (Haumea family)
        'Namaka': 'rgb(180, 160, 200)',     # Slightly darker purple
        'MK2': 'rgb(80, 80, 80)',           # Very dark (low albedo)        
        'Chariklo': 'rgb(100, 50, 50)',
        'Orcus': 'rgb(0, 100, 0)',
        'Varuna': 'rgb(218, 165, 32)',
        'Ixion': 'rgb(218, 165, 32)',
        'GV9': 'rgb(128, 0, 128)',
        'Mani': 'rgb(255, 0, 0)',  
        'Gonggong': 'red',    
        'Haumea': 'rgb(128, 0, 128)',
        'Makemake': 'rgb(255, 192, 203)',
        'Eris': 'rgb(240, 240, 240)',
        'Ammonite': 'rgb(255, 0, 0)', 
        'Sedna': 'rgb(135, 206, 235)',
        'Leleakuhonua': 'cyan',
        '2017 OF201': 'rgb(150, 90, 60)',                       
    }
    return colors.get(planet, 'goldenrod')

# Define positions for stellar class labels with different x positions and fonts
stellar_class_labels = [
        {
            'text': 'Supergiants', 
            'x': 0.2, 
            'y': 5.5,
            'font': dict(color='lightblue', size=14, family='Arial')
        },
        {
            'text': 'Supergiants', 
            'x': 0.66, 
            'y': 5.5,
            'font': dict(color='red', size=14, family='Arial')
        },
        {
            'text': 'Bright Giants', 
            'x': 0.22, 
            'y': 3.7,
            'font': dict(color='lightblue', size=14, family='Arial')
        },
        {
            'text': 'Bright Giants', 
            'x': 0.857, 
            'y': 3.7,
            'font': dict(color='red', size=14, family='Arial')
        },
        {
            'text': 'Carbon Stars', 
            'x': 0.96, 
            'y': 3.0,
            'font': dict(color='red', size=14, family='Arial')
        },
        {
            'text': 'Giants', 
            'x': 0.25, 
            'y': 2.25,
            'font': dict(color='lightblue', size=14, family='Arial')
        },
        {
            'text': 'Giants', 
            'x': 0.83, 
            'y': 2.25,
            'font': dict(color='red', size=14, family='Arial')
        },
        {
            'text': 'Subgiants', 
            'x': 0.2, 
            'y': 1.0,
            'font': dict(color='lightblue', size=14, family='Arial')
        },
        {
            'text': 'Subgiants', 
            'x': 0.75, 
            'y': 1.0,
            'font': dict(color='red', size=14, family='Arial')
        },
        {
            'text': 'Main Sequence', 
            'x': 0.4, 
            'y': 0.2, 
            'rotation': 15,
            'font': dict(color='white', size=20, family='Arial', weight='bold')  # Making this one bold as an example
        },
                {
            'text': 'Dwarfs', 
            'x': 0.77, 
            'y': -1,
            'font': dict(color='red', size=14, family='Arial')
        },
        {
            'text': 'White Dwarfs', 
            'x': 0.4, 
            'y': -4.5,
            'font': dict(color='white', size=14, family='Arial')
        }
    ]

spectral_subclass_temps = {
    'O': {0: 50000, 9: 30000},    # O0 to O9
    'B': {0: 30000, 9: 10000},    # B0 to B9
    'A': {0: 10000, 9: 7500},     # A0 to A9
    'F': {0: 7500, 9: 6000},      # F0 to F9
    'G': {0: 6000, 9: 5200},      # G0 to G9
    'K': {0: 5200, 9: 3700},      # K0 to K9
    'M': {0: 3700, 9: 2400},      # M0 to M9
    'L': {0: 2400, 9: 1300},      # L0 to L9
    'T': {0: 1300, 9: 600},       # T0 to T9 (optional)
}
