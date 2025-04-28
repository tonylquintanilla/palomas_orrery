# idealized_orbits.py

import numpy as np
import math
import plotly.graph_objs as go

planetary_params = {
    # Semi-major axis: This is one-half of the longest diameter of the elliptical orbit. It's essentially the average 
    # of the periapsis (closest point to Saturn) and apoapsis (farthest point from Saturn) distances.
    # IDs are NAIF IDs used by Horizons. The acronym NAIF stands for the Navigation and Ancillary Information Facility. 
    # It is a group at NASA's Jet Propulsion Laboratory (JPL) that is responsible for developing and supporting the SPICE 
    # (Spacecraft, Planet, Instrument, C-matrix, Events) information system. SPICE is used extensively by NASA and the 
    # international space science community for mission planning and the analysis of scientific observations from space missions. 
    # The NAIF IDs are numerical identifiers assigned to various celestial bodies, spacecraft, and instruments within the SPICE system. 
    # These IDs provide a consistent and unambiguous way to refer to these objects in SPICE data files (kernels) and software.

    'Mercury': {
        'a': 0.387098,  # semi-major axis in AU
        'e': 0.205630,  # eccentricity
        'i': 7.005,     # inclination in degrees
        'omega': 29.124, # argument of perihelion in degrees
        'Omega': 48.331  # longitude of ascending node in degrees
    },
    'Venus': {
        'a': 0.723332,
        'e': 0.006772,
        'i': 3.39471,
        'omega': 54.884,
        'Omega': 76.680
    },
    'Earth': {
        'a': 1.000000,
        'e': 0.016710,
        'i': 0.00005,
        'omega': 114.207,
        'Omega': -11.26064
    },
    'Mars': {
        'a': 1.523679,
        'e': 0.093400,
        'i': 1.850,
        'omega': 286.502,
        'Omega': 49.558
    },
    'Jupiter': {
        'a': 5.204267,
        'e': 0.048498,
        'i': 1.303,
        'omega': 273.867,
        'Omega': 100.464
    },
    'Saturn': {
        'a': 9.582486,
        'e': 0.054150,
        'i': 2.485,
        'omega': 339.392,
        'Omega': 113.665
    },
    'Uranus': {
        'a': 19.191263,
        'e': 0.047318,
        'i': 0.773,
        'omega': 96.998857,
        'Omega': 74.006
    },
    'Neptune': {
        'a': 30.068963,
        'e': 0.008678,
        'i': 1.770,
        'omega': 276.336,
        'Omega': 131.784
    },
    'Pluto': {
        'a': 39.482117,
        'e': 0.248808,
        'i': 17.16,
        'omega': 113.834,
        'Omega': 110.299
    },

    'Planet 9': {
    'a': 400,          # Semi-major axis in AU (estimates range from 400-800 AU)
    'e': 0.6,          # Eccentricity (estimates range from 0.2-0.7)
    'i': 20,           # Inclination in degrees (estimates range from 15-25 degrees)
    'L': 238,          # Mean longitude at epoch in degrees
    'omega': 150,      # Argument of perihelion in degrees
    'Omega': 90        # Longitude of ascending node in degrees
},
    
    # Dwarf Planets
    'Ceres': {
        'a': 2.7675,
        'e': 0.076,
        'i': 10.593,
        'omega': 73.597,
        'Omega': 80.393
    },
    'Haumea': {
        'a': 43.13,
        'e': 0.191,
        'i': 28.20,
        'omega': 240.20,
        'Omega': 122.10
    },
    'Makemake': {   # 136472 Makemake (2005 FY9); Epoch 2018-Jan-10
        'a': 45.6923640352447,                    # A
        'e': .1551157031828145,                   # EC
        'i': 28.98446068551257,                   # IN
        'omega': 295.7568523219785,               # W
        'Omega': 79.60732027458391                # OM
    },
    'Eris': {
        'a': 67.78,
        'e': 0.441,
        'i': 44.03,
        'omega': 150.977,
        'Omega': 35.873
    },
    'Quaoar': {
        'a': 43.325,
        'e': 0.0392,
        'i': 8.34,
        'omega': 157.631,
        'Omega': 188.809
    },
    'Sedna': {  # 90377 Sedna (2003 VB12); Epoch 2018-May-16
        'a': 481.3036019474312,         # A
        'e': .8418992747337005,         # EC
        'i': 11.92926934569724,         # IN
        'omega': 311.5908685997484,     # W
        'Omega': 144.4059276991507      # OM
    },
    'Gonggong': {  # 225088 Gonggong (2007 OR10); Epoch 2017-Sep-25
        'a': 67.15612088312527,     # A, semi-major axis in AU
        'e': .5057697166633393,   # EC, eccentricity
        'i': 30.86452616352285,     # IN, inclination in degrees
        'omega': 207.2059900430104, # W, argument of perihelion in degrees
        'Omega': 336.8262717815297  # OM, longitude of ascending node in degrees
    },

    'Orcus': {
        'a': 39.419,     # semi-major axis in AU
        'e': 0.226701,   # eccentricity
        'i': 20.573,     # inclination in degrees
        'omega': 72.400,  # argument of perihelion in degrees
        'Omega': 268.457  # longitude of ascending node in degrees
    },

    'Ixion': {
        'a': 39.648,     # semi-major axis in AU
        'e': 0.242419,   # eccentricity
        'i': 19.636,     # inclination in degrees
        'omega': 300.273, # argument of perihelion in degrees
        'Omega': 71.031   # longitude of ascending node in degrees
    },

    'MS4': {  # 307261 (2002 MS4); Epoch 2018-May-29
        'a': 41.9417204244255,     # A, semi-major axis in AU
        'e': .1397251099240261,   # EC, eccentricity
        'i': 17.66789460477087,     # IN, inclination in degrees
        'omega': 214.0813053057189, # W, argument of perihelion in degrees
        'Omega': 215.9040968620575  # OM, longitude of ascending node in degrees
    },

    'Varuna': {
        'a': 42.947,     # semi-major axis in AU
        'e': 0.051739,   # eccentricity
        'i': 17.200,     # inclination in degrees
        'omega': 97.286,  # argument of perihelion in degrees
        'Omega': 97.286   # longitude of ascending node in degrees
    },

    'GV9': {  # 90568 (2004 GV9); Epoch 2017-11-1   
        'a': 42.26253681484609,     # A, semi-major axis in AU
        'e': .08206106683377956,   # EC, eccentricity
        'i': 21.93322237277237,     # IN, inclination in degrees
        'omega': 295.190819856158, # W, argument of perihelion in degrees
        'Omega': 250.6628794038891  # OM, longitude of ascending node in degrees
    },

    'Arrokoth': {                  # Epoch 2017-12-14, heliocentric
        'a': 44.44519963724322,   # A, semi-major axis in AU
        'e': .03868645692376498,   # EC, eccentricity
        'i': 2.45301305206896,      # IN, inclination in degrees
        'omega': 176.1507602341478, # W, argument of perihelion in degrees
        'Omega': 158.939446659904   # OM, longitude of ascending node in degrees
    },

    # Asteroids
    'Vesta': {
        'a': 2.3617,
        'e': 0.089,
        'i': 7.155,
        'omega': 151.216,
        'Omega': 103.851
    },

    'Bennu': {
        'a': 1.126391,    # semi-major axis in AU
        'e': 0.203745,    # eccentricity
        'i': 6.035,       # inclination in degrees
        'omega': 66.223,  # argument of perihelion in degrees
        'Omega': 2.061    # longitude of ascending node in degrees
    },

    'Šteins': {
        'a': 2.363,      # semi-major axis in AU
        'e': 0.146,      # eccentricity
        'i': 9.944,      # inclination in degrees
        'omega': 250.97,  # argument of perihelion in degrees
        'Omega': 55.39    # longitude of ascending node in degrees
    },

    'Lutetia': {                  # Epoch 2017-10-12, heliocentric
        'a': 2.434591597038037,   # Horizons: A, semi-major axis in AU
        'e': .1644174522633922,   # Horizons: EC, eccentricity
        'i': 3.063715677953934,      # Horizons: IN, inclination in degrees
        'omega': 249.980528664283, # Horizons: W, argument of perihelion in degrees
        'Omega': 80.87713180326485   # Horizons: OM, longitude of ascending node in degrees
    },

    'Apophis': {
        'a': 0.922583,   # semi-major axis in AU
        'e': 0.191481,   # eccentricity
        'i': 3.331,      # inclination in degrees
        'omega': 126.394, # argument of perihelion in degrees
        'Omega': 204.061  # longitude of ascending node in degrees
    },  

    'Eros': {
        'a': 1.458040,   # semi-major axis in AU
        'e': 0.222868,   # eccentricity
        'i': 10.829,     # inclination in degrees
        'omega': 178.817, # argument of perihelion in degrees
        'Omega': 304.435  # longitude of ascending node in degrees
    },

    'Ryugu': {
        'a': 1.189562,   # semi-major axis in AU
        'e': 0.190349,   # eccentricity
        'i': 5.884,      # inclination in degrees
        'omega': 211.421, # argument of perihelion in degrees
        'Omega': 251.617  # longitude of ascending node in degrees
    },

    'Itokawa': {
        'a': 1.324163,   # semi-major axis in AU
        'e': 0.280164,   # eccentricity
        'i': 1.622,      # inclination in degrees
        'omega': 162.767, # argument of perihelion in degrees
        'Omega': 69.095   # longitude of ascending node in degrees
    },

    '2024 YR4': {                  # Epoch 2025-1-25, heliocentric, solution date 2025-3-18
        'a': 2.51634929076732,   # Horizons: A, semi-major axis in AU
        'e': .6616057837023791,   # Horizons: EC, eccentricity
        'i': 3.408279909719115,      # Horizons: IN, inclination in degrees
        'omega': 134.3644319410849, # Horizons: W, argument of perihelion in degrees
        'Omega': 271.3676930913076   # Horizons: OM, longitude of ascending node in degrees
    },

    '2024 PT5': {                  # Epoch 2024-10-20, heliocentric
        'a': 1.012228628670663,   # Horizons: A, semi-major axis in AU
        'e': .02141074038624791,   # Horizons: EC, eccentricity
        'i': 1.518377382131216,      # Horizons: IN, inclination in degrees
        'omega': 116.8074860094156, # Horizons: W, argument of perihelion in degrees
        'Omega': 305.1069316209851   # Horizons: OM, longitude of ascending node in degrees
    },

    '2024 DW': {                  # Epoch 2024-2-19, heliocentric; solution date 2024-2-23
        'a': 2.421098478271158,   # Horizons: A, semi-major axis in AU
        'e': .6939958024514898,   # Horizons: EC, eccentricity
        'i': .9861902430422796,      # Horizons: IN, inclination in degrees
        'omega': 244.5179261214832, # Horizons: W, argument of perihelion in degrees
        'Omega': 335.4879825233473   # Horizons: OM, longitude of ascending node in degrees
    },

    # Comets
    'Churyumov': {                  # Epoch 2015-10-10, heliocentric (500@10) and geocentric (500)
        'a': 3.462249489765068,   # Horizons: A, semi-major axis in AU
        'e': .6409081306555051,   # Horizons: EC, eccentricity
        'i': 7.040294906760007,      # Horizons: IN, inclination in degrees
        'omega': 12.79824973415729, # Horizons: W, argument of perihelion in degrees
        'Omega': 50.13557380441372   # Horizons: OM, longitude of ascending node in degrees
    },

    'Halley_geocentric': {         # Epoch 2017-10-13, geocentric -- not accurate for our plot
        'a': 3.170639037258039,   # Horizons: A, semi-major axis in AU
        'e': .1433170784128717,   # Horizons: EC, eccentricity
        'i': 3.449227641924809,      # Horizons: IN, inclination in degrees
        'omega': 188.324777427583, # Horizons: W, argument of perihelion in degrees
        'Omega': 95.24615579501011   # Horizons: OM, longitude of ascending node in degrees
    },

    'Halley': {                  # Epoch 2068-02-21, heliocentric
        'a': 17.93003431157555,   # Horizons: A, semi-major axis in AU
        'e': .9679221169240834,   # Horizons: EC, eccentricity
        'i': 162.1951462980701,      # Horizons: IN, inclination in degrees
        'omega': 112.2128395742619, # Horizons: W, argument of perihelion in degrees
        'Omega': 59.07198712310091   # Horizons: OM, longitude of ascending node in degrees
    },

    'Ikeya-Seki': {                  # Epoch 1965-10-7, heliocentric, (C/1965 S1-A)
        'a': 91.59999999999813,   # Horizons: A, semi-major axis in AU
        'e': .999915,   # Horizons: EC, eccentricity
        'i': 141.8642,      # Horizons: IN, inclination in degrees
        'omega': 69.04859999999999, # Horizons: W, argument of perihelion in degrees
        'Omega': 346.9947   # Horizons: OM, longitude of ascending node in degrees
    },

    # Satellites

    'Moon': {            # 301; Revised 7-31-2013, geocentric; source: https://ssd.jpl.nasa.gov/horizons/app.html#/
#        'a': 384400,   # Horizons: A, semi-major axis in AU
        'a': 0.002570,   # Horizons: A, semi-major axis in AU; 384400 km or 0.00257 au
        'e': 0.0549,   # Horizons: EC, eccentricity; 0.05490 was 0.0554
        'i': 5.145,      # Horizons: IN, inclination in degrees; 5.145 deg was 5.16
        'omega': 318.15, # Horizons: W, argument of perihelion in degrees
        'Omega': 125.08   # Horizons: OM, longitude of ascending node in degrees
    },

    # Mars' Moons

    'Phobos': {             # 401; Revised: Sep 28, 2012
#        'a': 9400,       # semi-major axis in km, 9.3772(10^3)
        'a': 0.000062682,       # semi-major axis in AU, 0.000062682
#        'a_parent': 2.76,      # semi-major axis in Mars radii
        'e': 0.0151,           # eccentricity
        'i': 1.082,            # inclination to Mars' equator in degrees
        'omega': 216.3,      # argument of perihelion in degrees
        'Omega': 169.2        # longitude of ascending node in degrees
    },

    'Deimos': {             # 402; Revised: Sep 28, 2012
#        'a': 23500,       # semi-major axis in km; 23.4632(10^3)
        'a': 0.00015683,       # semi-major axis in AU; 0.00015683
#        'a_parent': 6.92,      # semi-major axis in Mars radii
        'e': 0.00033,          # eccentricity
        'i': 1.791,            # inclination to Mars' equator in degrees
        'omega': 0,      # argument of perihelion in degrees
        'Omega': 54.4       # longitude of ascending node in degrees
    },

    # Jupiter's Galilean Moons
    'Io': {
#        'a': 421800,         # semi-major axis in km
        'a': 0.002819,         # semi-major axis in AU
    #    'a_parent': 5.90,      # semi-major axis in Jupiter radii
        'e': 0.0041,           # eccentricity
        'i': 0.05,             # inclination to Jupiter's equator in degrees
        'omega': 49.1,       # argument of perihelion in degrees
        'Omega': 0.0        # longitude of ascending node in degrees
    },

    'Europa': {
#        'a': 671100,         # semi-major axis in km
        'a': 0.004486,         # semi-major axis in AU
    #    'a_parent': 9.40,      # semi-major axis in Jupiter radii
        'e': 0.0094,           # eccentricity
        'i': 0.471,            # inclination to Jupiter's equator in degrees
        'omega': 45.0,       # argument of perihelion in degrees
        'Omega': 184.0       # longitude of ascending node in degrees
    },

    'Ganymede': {
#        'a': 1070400,         # semi-major axis in km
        'a': 0.007155,         # semi-major axis in AU
    #    'a_parent': 14.99,     # semi-major axis in Jupiter radii
        'e': 0.0013,           # eccentricity
        'i': 0.204,            # inclination to Jupiter's equator in degrees
        'omega': 198.3,      # argument of perihelion in degrees
        'Omega': 58.5        # longitude of ascending node in degrees
    },

    'Callisto': {
#        'a': 1882700,         # semi-major axis in km
        'a': 0.012585,         # semi-major axis in AU
    #    'a_parent': 26.37,     # semi-major axis in Jupiter radii
        'e': 0.0074,           # eccentricity
        'i': 0.205,            # inclination to Jupiter's equator in degrees
        'omega': 43.8,       # argument of perihelion in degrees
        'Omega': 309.1       # longitude of ascending node in degrees
    },

# Jupiter's Inner Moons associated with ring system
    'Metis': {
        'a': 0.000856,         # semi-major axis in AU (128,000 km)
    #    'a_parent': 1.79,      # semi-major axis in Jupiter radii
        'e': 0.0002,           # eccentricity (nearly circular)
        'i': 0.06,             # inclination to Jupiter's equator in degrees
        'omega': 16.63,        # argument of perihelion in degrees
        'Omega': 68.9          # longitude of ascending node in degrees
    },

    'Adrastea': {
        'a': 0.000864,         # semi-major axis in AU (129,000 km)
    #    'a_parent': 1.81,      # semi-major axis in Jupiter radii
        'e': 0.0015,           # eccentricity
        'i': 0.03,             # inclination to Jupiter's equator in degrees
        'omega': 234.0,        # argument of perihelion in degrees
        'Omega': 33.5          # longitude of ascending node in degrees
    },

    'Amalthea': {
        'a': 0.001217,         # semi-major axis in AU (182,000 km)
    #    'a_parent': 2.54,      # semi-major axis in Jupiter radii
        'e': 0.0032,           # eccentricity
        'i': 0.374,            # inclination to Jupiter's equator in degrees
        'omega': 155.87,       # argument of perihelion in degrees
        'Omega': 108.05        # longitude of ascending node in degrees
    },

    'Thebe': {
        'a': 0.001514,         # semi-major axis in AU (226,000 km)
    #    'a_parent': 3.11,      # semi-major axis in Jupiter radii
        'e': 0.0175,           # eccentricity
        'i': 1.076,            # inclination to Jupiter's equator in degrees
        'omega': 234.57,       # argument of perihelion in degrees
        'Omega': 237.33        # longitude of ascending node in degrees
    },

    # Saturn's Major and Ring Moons

    'Pan': {              # Revised: Oct 03, 2018; 618
#        'a': 133584,         # semi-major axis in km 133.584(10^3)
        'a': 0.0008930,         # semi-major axis in AU
#        'a_parent': ,      # semi-major axis in Saturn radii
        'e': 0,           # eccentricity not defined in Horizons; 0 in https://ssd.jpl.nasa.gov/sats/elem/
        'i': 0,            # inclination to Saturn's equator in degrees not defined in Horizons; 0 in https://ssd.jpl.nasa.gov/sats/elem/
        'omega': 0,      # argument of perihelion in degrees; laplace; 0 in https://ssd.jpl.nasa.gov/sats/elem/
        'Omega': 0       # longitude of ascending node in degrees; 0 in https://ssd.jpl.nasa.gov/sats/elem/
    },

    'Daphnis': {              # Revised: Aug 08, 2019; 635
#        'a': 136500,         # semi-major axis in km 136500 in https://ssd.jpl.nasa.gov/sats/elem/
        'a': 0.0009124,         # semi-major axis in AU
#        'a_parent': ,      # semi-major axis in Saturn radii
        'e': 0,           # eccentricity not defined in Horizons; 0 in https://ssd.jpl.nasa.gov/sats/elem/
        'i': 0,            # inclination to Saturn's equator in degrees not defined in Horizons; 0 in https://ssd.jpl.nasa.gov/sats/elem/
        'omega': 0,      # argument of perihelion in degrees; laplace; 0 in https://ssd.jpl.nasa.gov/sats/elem/
        'Omega': 0       # longitude of ascending node in degrees; 0 in https://ssd.jpl.nasa.gov/sats/elem/
    },

    'Prometheus': {              # Revised: Oct 03, 2018; 616
#        'a': 139350,         # semi-major axis in km 139.35 (10^3) in https://ssd.jpl.nasa.gov/horizons/app.html#/
        'a': 0.0009315,         # semi-major axis in AU; Orbital period 0.612986 d
#        'a_parent': ,      # semi-major axis in Saturn radii
        'e': 0.0024,           # eccentricity in https://ssd.jpl.nasa.gov/horizons/app.html#/
        'i': 0,            # inclination to Saturn's equator in degrees in Horizons; in https://ssd.jpl.nasa.gov/horizons/app.html#/
        'omega': 341.9,      # argument of perihelion in degrees; laplace; in https://ssd.jpl.nasa.gov/sats/elem/
        'Omega': 0       # longitude of ascending node in degrees; 0 in https://ssd.jpl.nasa.gov/sats/elem/
    },

    'Pandora': {              # Revised: Oct 03, 2018; 617
#        'a': 141700,         # semi-major axis in km 141.70 (10^3) in https://ssd.jpl.nasa.gov/horizons/app.html#/
        'a': 0.0009472,         # semi-major axis in AU; Orbital period 0.628804 d
#        'a_parent': ,      # semi-major axis in Saturn radii
        'e': 0.0042,           # eccentricity in https://ssd.jpl.nasa.gov/horizons/app.html#/
        'i': 0,            # inclination to Saturn's equator in degrees in Horizons; in https://ssd.jpl.nasa.gov/horizons/app.html#/
        'omega': 217.9,      # argument of perihelion in degrees; laplace; in https://ssd.jpl.nasa.gov/sats/elem/
        'Omega': 0       # longitude of ascending node in degrees; 0 in https://ssd.jpl.nasa.gov/sats/elem/
    },

    'Mimas': {              # revised 1-26-2022; 601
#        'a': 185540,         # semi-major axis in km
        'a': 0.001242,         # semi-major axis in AU
#        'a_parent': 3.08,      # semi-major axis in Saturn radii
        'e': 0.0196,           # eccentricity
        'i': 1.572,            # inclination to Saturn's equator in degrees
        'omega': 160.4,      # argument of perihelion in degrees; laplace
        'Omega': 66.2       # longitude of ascending node in degrees
    },

    'Enceladus': {          # 602
#        'a': 238400,         # semi-major axis in km
        'a': 0.001587,         # semi-major axis in AU
#        'a_parent': 3.95,      # semi-major axis in Saturn radii
        'e': 0.0047,           # eccentricity
        'i': 0.009,            # inclination to Saturn's equator in degrees
        'omega': 119.5,      # argument of perihelion in degrees
        'Omega': 0.0       # longitude of ascending node in degrees
    },

    'Tethys': {             # 603
#        'a': 295000,         # semi-major axis in km
        'a': 0.001970,         # semi-major axis in AU
#        'a_parent': 4.89,      # semi-major axis in Saturn radii
        'e': 0.001,           # eccentricity
        'i': 1.091,            # inclination to Saturn's equator in degrees
        'omega': 335.3,      # argument of perihelion in degrees
        'Omega': 273.0       # longitude of ascending node in degrees
    },

    'Dione': {              # 604
#        'a': 377700,         # semi-major axis in km
        'a': 0.002525,         # semi-major axis in AU
#        'a_parent': 6.26,      # semi-major axis in Saturn radii
        'e': 0.0022,           # eccentricity
        'i': 0.0,            # inclination to Saturn's equator in degrees
        'omega': 116.0,      # argument of perihelion in degrees
        'Omega': 0.0       # longitude of ascending node in degrees
    },

    'Rhea': {               # 605
#        'a': 527200,         # semi-major axis in km
        'a': 0.003524,         # semi-major axis in AU
#        'a_parent': 8.74,      # semi-major axis in Saturn radii
        'e': 0.0010,           # eccentricity
        'i': 0.333,            # inclination to Saturn's equator in degrees
        'omega': 44.3,      # argument of perihelion in degrees
        'Omega': 133.7       # longitude of ascending node in degrees
    },

    'Titan': {              # 606
#        'a': 1221900,         # semi-major axis in km
        'a': 0.008168,         # semi-major axis in AU
#        'a_parent': 20.27,     # semi-major axis in Saturn radii
        'e': 0.0288,           # eccentricity
        'i': 0.306,            # inclination to Saturn's equator in degrees
        'omega': 78.3,      # argument of perihelion in degrees
        'Omega': 78.6        # longitude of ascending node in degrees
    },

    'Hyperion': {              # 607; Revised: Jan 26, 2022; Orbital period 21.28 d
#        'a': 1500933,         # semi-major axis in km; 1500.933(10^3); https://ssd.jpl.nasa.gov/horizons/app.html#/
        'a': 0.010033,         # semi-major axis in AU
#        'a_parent': ,     # semi-major axis in Saturn radii
        'e': 0.0232,           # eccentricity; https://ssd.jpl.nasa.gov/horizons/app.html#/
        'i': 0.615,            # inclination to Saturn's equator in degrees; https://ssd.jpl.nasa.gov/horizons/app.html#/
        'omega': 214.0,      # argument of perihelion in degrees; https://ssd.jpl.nasa.gov/sats/elem/
        'Omega': 87.1        # longitude of ascending node in degrees; https://ssd.jpl.nasa.gov/sats/elem/
    },

    'Iapetus': {              # 608; Revised: Jan 26, 2022; Orbital period 79.33 d
#        'a': 3560840,         # semi-major axis in km; 3560.84 (10^3); https://ssd.jpl.nasa.gov/horizons/app.html#/
        'a': 0.02380,         # semi-major axis in AU
#        'a_parent': ,     # semi-major axis in Saturn radii
        'e': 0.0283,           # eccentricity; https://ssd.jpl.nasa.gov/horizons/app.html#/
        'i': 7.489,            # inclination to Saturn's equator in degrees; https://ssd.jpl.nasa.gov/horizons/app.html#/
        'omega': 254.5,      # argument of perihelion in degrees; https://ssd.jpl.nasa.gov/sats/elem/
        'Omega': 86.5        # longitude of ascending node in degrees; https://ssd.jpl.nasa.gov/sats/elem/
    },

    'Phoebe': {             # 609
#        'a': 12929400,          # semi-major axis in km
        'a': 0.08650,          # semi-major axis in AU
#        'a_parent': 214.7,     # semi-major axis in Saturn radii
        'e': 0.1635,           # eccentricity
        'i': 175.2,            # inclination to Saturn's equator in degrees (retrograde)
        'omega': 240.3,      # argument of perihelion in degrees
        'Omega': 192.7        # longitude of ascending node in degrees
    },

    # Uranus's Major Moons
    'Miranda': {            # 705
#        'a': 129900,         # semi-major axis in km
        'a': 0.000868,         # semi-major axis in AU
#        'a_parent': 5.0,       # semi-major axis in Uranus radii
        'e': 0.0013,           # eccentricity
        'i': 4.338,            # inclination to Uranus's equator in degrees
        'omega': 155.6,       # argument of perihelion in degrees
        'Omega': 100.6       # longitude of ascending node in degrees
    },

    'Ariel': {              # 701
#        'a': 190900,         # semi-major axis in km
        'a': 0.001276,         # semi-major axis in AU
#        'a_parent': 7.35,      # semi-major axis in Uranus radii
        'e': 0.0012,           # eccentricity
        'i': 0.0,            # inclination to Uranus's equator in degrees
        'omega': 83.3,      # argument of perihelion in degrees
        'Omega': 0.0        # longitude of ascending node in degrees
    },

    'Umbriel': {            # 702
#        'a': 266000,         # semi-major axis in km
        'a': 0.001778,         # semi-major axis in AU
#        'a_parent': 10.23,     # semi-major axis in Uranus radii
        'e': 0.0039,           # eccentricity
        'i': 0.1,            # inclination to Uranus's equator in degrees
        'omega': 157.5,       # argument of perihelion in degrees
        'Omega': 195.5        # longitude of ascending node in degrees
    },

    'Titania': {            # 703
#        'a': 436300,         # semi-major axis in km
        'a': 0.002914,         # semi-major axis in AU
#        'a_parent': 16.77,     # semi-major axis in Uranus radii
        'e': 0.001,           # eccentricity
        'i': 0.1,            # inclination to Uranus's equator in degrees
        'omega': 202.0,      # argument of perihelion in degrees
        'Omega': 26.4        # longitude of ascending node in degrees
    },

    'Oberon': {             # 704
#       'a': 583400,         # semi-major axis in km
        'a': 0.003907,         # semi-major axis in AU
#        'a_parent': 22.47,     # semi-major axis in Uranus radii
        'e': 0.0008,           # eccentricity
        'i': 0.058,            # inclination to Uranus's equator in degrees
        'omega': 182.4,      # argument of perihelion in degrees
        'Omega': 30.5       # longitude of ascending node in degrees
    },

    # Neptune's Major Moon
    'Triton': {             # 801
#        'a': 354800,         # semi-major axis in km
        'a': 0.002371,         # semi-major axis in AU
#        'a_parent': 14.33,     # semi-major axis in Neptune radii
        'e': 0.000016,         # eccentricity (nearly circular)
        'i': 157.3,          # inclination to Neptune's equator in degrees (retrograde)
        'omega': 0.0,       # argument of perihelion in degrees
        'Omega': 178.1       # longitude of ascending node in degrees
    },

    # Pluto's Moons
    'Charon': {             # 901
#        'a': 19600,         # semi-major axis in km
        'a': 0.000127,         # semi-major axis in AU
#        'a_parent': 16.4,      # semi-major axis in Pluto radii
        'e': 0.0002,           # eccentricity (nearly circular)
        'i': 0.001,            # inclination to Pluto's equator in degrees
        'omega': 0.0,      # argument of perihelion in degrees
        'Omega': 0.0       # longitude of ascending node in degrees
    },

    'Nix': {                # 902
#        'a': 49300,         # semi-major axis in km
        'a': 0.000242,         # semi-major axis in AU
#        'a_parent': 31.3,      # semi-major axis in Pluto radii
        'e': 0.015,           # eccentricity
        'i': 0.0,            # inclination to Pluto's equator in degrees
        'omega': 31.4,      # argument of perihelion in degrees
        'Omega': 0.0         # longitude of ascending node in degrees
    },

    'Hydra': {              # 903; revised 4-3-2024; Fit to post New Horizons encounter and Gaia data through 2023.
#        'a': 65200,         # semi-major axis in km
        'a': 0.0004358,         # semi-major axis in AU; 0.00043583
#        'a_parent': 83.9,     # semi-major axis in Pluto radii
        'e': 0.009,           # eccentricity
        'i': 0.3,            # inclination to Pluto's equator in degrees
        'omega': 139.3,      # argument of perihelion in degrees
        'Omega': 114.3       # longitude of ascending node in degrees
    },

    # Eris's Moon
    #'Dysnomia': {
#        'a': 0.000364,         # semi-major axis in AU
    #    'a': 0.000364,         # semi-major axis in AU
#        'a_parent': 36.2,      # semi-major axis in Eris radii (estimate)
    #    'e': 0.0062,           # eccentricity
    #    'i': 78.29,            # inclination in degrees (to the ecliptic)
    #    'omega': 139.65,       # argument of perihelion in degrees
    #    'Omega': 29.43         # longitude of ascending node in degrees
    #},

} 

parent_planets = {
    'Earth': ['Moon'],
    'Mars': ['Phobos', 'Deimos'],
    'Jupiter': ['Io', 'Europa', 'Ganymede', 'Callisto', 'Metis', 'Adrastea', 'Amalthea', 'Thebe'],
    'Saturn': ['Titan', 'Enceladus', 'Rhea', 'Dione', 'Tethys', 'Mimas', 'Iapetus', 'Phoebe', 'Pan', 'Daphnis', 'Prometheus',
               'Pandora', 'Hyperion'],
    'Uranus': ['Miranda', 'Ariel', 'Umbriel', 'Titania', 'Oberon'],
    'Neptune': ['Triton'],
    'Pluto': ['Charon', 'Nix', 'Hydra'],
    'Eris': ['Dysnomia']
}

# Dictionary of planet tilts (degrees)
planet_tilts = {
    'Earth': 0,         # 23.44 tilt not needed, moon already defined in ecliptic frame
    'Mars': 25.19,      # Mars axial tilt
    'Jupiter': 3.13,    # Jupiter axial tilt
    'Saturn': -26.73,   # Saturn axial tilt (negative works better)
    'Uranus': 97.77,    # Uranus axial tilt
    'Neptune': 28.32,   # Neptune axial tilt
    'Pluto': -122.53    # Pluto axial tilt (negative works better)
}

# Dictionary of planet pole directions (J2000)
planet_poles = {
    'Mars': {'ra': 317.68, 'dec': 52.89},
    'Jupiter': {'ra': 268.05, 'dec': 64.49},
    'Saturn': {'ra': 40.58, 'dec': 83.54},
    'Uranus': {'ra': 257.43, 'dec': -15.10},
    'Neptune': {'ra': 299.36, 'dec': 43.46},
    'Pluto': {'ra': 132.99, 'dec': -6.16}
}

def plot_mars_satellite_orbit_refined(satellite_name, planetary_params, color, fig=None):
    """Further refined approach for Mars satellites"""
    if fig is None:
        fig = go.Figure()
    
    try:
        # Get orbital parameters
        if satellite_name not in planetary_params:
            print(f"Error: No orbital parameters found for {satellite_name}")
            return fig
            
        orbital_params = planetary_params[satellite_name]
        
        # Extract orbital elements
        a = orbital_params.get('a', 0)
        e = orbital_params.get('e', 0)
        i = orbital_params.get('i', 0)
        omega = orbital_params.get('omega', 0)
        Omega = orbital_params.get('Omega', 0)
        
        # Generate ellipse in orbital plane
        theta = np.linspace(0, 2*np.pi, 360)
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)

        # Convert angles to radians
        i_rad = np.radians(i)
        omega_rad = np.radians(omega)
        Omega_rad = np.radians(Omega)

        # Standard orbital element rotation sequence
        x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, Omega_rad, 'z')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, omega_rad, 'z')
        
        # Mars' orbit inclination to the ecliptic
        mars_inclination = np.radians(1.85)
        
        # Mars' longitude of ascending node
        mars_node = np.radians(49.58)
        
        # Apply Mars' orbital plane orientation
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, mars_node, 'z')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, mars_inclination, 'x')
        
        # Mars' axial tilt relative to its orbital plane
        mars_axial_tilt = np.radians(25.19)
        
        # Apply Mars' axial tilt
        x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, mars_axial_tilt, 'x')
        
        # Add the refined orbit trace to the figure
        fig.add_trace(
            go.Scatter3d(
                x=x_final,
                y=y_final,
                z=z_final,
                mode='lines',
                line=dict(dash='dashdot', width=2, color=color),
                name=f"{satellite_name} Refined Orbit",
                text=[f"{satellite_name} Refined Orbit"] * len(x_final),
                customdata=[f"{satellite_name} Refined Orbit"] * len(x_final),
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
        
        return fig
    
    except Exception as e:
        print(f"Error plotting refined Mars satellite {satellite_name}: {e}")
        return fig
    
def test_mars_rotations(satellite_name, planetary_params, color, fig=None):
    """Test multiple rotation combinations to find the best alignment"""
    if fig is None:
        fig = go.Figure()
    
    try:
        # Get orbital parameters
        if satellite_name not in planetary_params:
            print(f"Error: No orbital parameters found for {satellite_name}")
            return fig
            
        orbital_params = planetary_params[satellite_name]
        
        # Extract orbital elements
        a = orbital_params.get('a', 0)
        e = orbital_params.get('e', 0)
        i = orbital_params.get('i', 0)
        omega = orbital_params.get('omega', 0)
        Omega = orbital_params.get('Omega', 0)
        
        # Generate ellipse in orbital plane
        theta = np.linspace(0, 2*np.pi, 360)
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)

        # Convert angles to radians
        i_rad = np.radians(i)
        omega_rad = np.radians(omega)
        Omega_rad = np.radians(Omega)

        # Test several different rotation combinations
        rotations = [
            {"name": "Basic", "z1": Omega_rad, "x": i_rad, "z2": omega_rad, "extra": None},
            {"name": "Mars Tilt +", "z1": Omega_rad, "x": i_rad, "z2": omega_rad, 
             "extra": {"axis": 'x', "angle": np.radians(25.19)}},
            {"name": "Mars Tilt -", "z1": Omega_rad, "x": i_rad, "z2": omega_rad, 
             "extra": {"axis": 'x', "angle": np.radians(-25.19)}},
            {"name": "Mars Y", "z1": Omega_rad, "x": i_rad, "z2": omega_rad, 
             "extra": {"axis": 'y', "angle": np.radians(35.4)}},
            {"name": "Mars Z", "z1": Omega_rad, "x": i_rad, "z2": omega_rad, 
             "extra": {"axis": 'z', "angle": np.radians(49.58)}},
            {"name": "Y+Z", "z1": Omega_rad, "x": i_rad, "z2": omega_rad, 
             "extra": [{"axis": 'y', "angle": np.radians(35.4)}, 
                     {"axis": 'z', "angle": np.radians(49.58)}]},
            {"name": "Z+X", "z1": Omega_rad, "x": i_rad, "z2": omega_rad, 
             "extra": [{"axis": 'z', "angle": np.radians(49.58)}, 
                     {"axis": 'x', "angle": np.radians(25.19)}]},
        ]
        
        # Define line styles for each rotation
        styles = ["solid", "dash", "dot", "dashdot", "longdash", "longdashdot", "longdashdotdot"]
        
        # Apply each rotation combination
        for idx, rot in enumerate(rotations):
            # Apply standard orbital element rotations
            x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, rot["z1"], 'z')
            x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, rot["x"], 'x')
            x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, rot["z2"], 'z')
            
            # Apply extra rotations if specified
            if rot["extra"]:
                if isinstance(rot["extra"], list):
                    # Apply multiple extra rotations
                    for extra_rot in rot["extra"]:
                        x_temp, y_temp, z_temp = rotate_points(
                            x_temp, y_temp, z_temp, 
                            extra_rot["angle"], extra_rot["axis"]
                        )
                else:
                    # Apply single extra rotation
                    x_temp, y_temp, z_temp = rotate_points(
                        x_temp, y_temp, z_temp, 
                        rot["extra"]["angle"], rot["extra"]["axis"]
                    )
            
            # Add trace to figure
            line_style = styles[idx % len(styles)]
            
            fig.add_trace(
                go.Scatter3d(
                    x=x_temp,
                    y=y_temp,
                    z=z_temp,
                    mode='lines',
                    line=dict(dash=line_style, width=1, color=color),
                    name=f"{satellite_name} {rot['name']}",
                    text=[f"{satellite_name} {rot['name']} Rotation"] * len(x_temp),
                    customdata=[f"{satellite_name} {rot['name']} Rotation"] * len(x_temp),
                    hovertemplate='%{text}<extra></extra>',
                    showlegend=True
                )
            )
        
        return fig
    
    except Exception as e:
        print(f"Error testing Mars rotations for {satellite_name}: {e}")
        return fig

def plot_mars_satellite_orbit(satellite_name, planetary_params, color, fig=None):
    """Special function just for Mars satellites with a different rotation sequence"""
    if fig is None:
        fig = go.Figure()
    
    try:
        # Get the orbital parameters for this specific satellite
        if satellite_name not in planetary_params:
            print(f"Error: No orbital parameters found for {satellite_name}")
            return fig
            
        orbital_params = planetary_params[satellite_name]
        
        # Extract orbital elements
        a = orbital_params.get('a', 0)  # Semi-major axis in AU
        e = orbital_params.get('e', 0)  # Eccentricity
        i = orbital_params.get('i', 0)  # Inclination in degrees
        omega = orbital_params.get('omega', 0)  # Argument of periapsis in degrees
        Omega = orbital_params.get('Omega', 0)  # Longitude of ascending node in degrees
        
        print(f"\nPlotting Mars satellite: {satellite_name}")
        print(f"Orbital elements: a={a}, e={e}, i={i}°, ω={omega}°, Ω={Omega}°")
        
        # Generate ellipse in orbital plane
        theta = np.linspace(0, 2*np.pi, 360)  # 360 points for smoothness
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)

        # Convert angles to radians
        i_rad = np.radians(i)
        omega_rad = np.radians(omega)
        Omega_rad = np.radians(Omega)
        
        # APPROACH 1: Alternative rotation sequence
        # First rotate the orbital plane to align with Mars' equator
        x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, omega_rad, 'z')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, Omega_rad, 'z')
        
        # Then apply a special Mars transformation
        # This assumes Mars' axial tilt AND orbit orientation
        mars_tilt = np.radians(25.19)
        mars_node = np.radians(49.58)  # Mars' ascending node
        
        # First rotate by Mars' node
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, mars_node, 'z')
        # Then by Mars' tilt
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, mars_tilt, 'x')
        # Then back by Mars' node
        x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, -mars_node, 'z')
        
        print(f"Applied special Mars transformation sequence")
        
        # Create hover text for the orbit
        hover_text = f"{satellite_name} Ideal Orbit around Mars"
        
        # Add the orbit trace to the figure
        fig.add_trace(
            go.Scatter3d(
                x=x_final,
                y=y_final,
                z=z_final,
                mode='lines',
                line=dict(dash='dot', width=1, color=color),
                name=f"{satellite_name} Ideal Orbit",
                text=[hover_text] * len(x_final),
                customdata=[hover_text] * len(x_final),
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
        
        # APPROACH 2: Try a direct pole-based transformation
        x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, omega_rad, 'z')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, Omega_rad, 'z')
        
        # Mars' north pole direction (J2000)
        ra_pole = np.radians(317.68)
        dec_pole = np.radians(52.89)
        
        # Calculate Mars' pole vector
        sin_dec = np.sin(dec_pole)
        cos_dec = np.cos(dec_pole)
        sin_ra = np.sin(ra_pole)
        cos_ra = np.cos(ra_pole)
        
        # Mars' north pole vector
        x_pole = cos_dec * cos_ra
        y_pole = cos_dec * sin_ra
        z_pole = sin_dec
        
        # Calculate rotation angle and axis to align z-axis with Mars' pole
        z_axis = np.array([0, 0, 1])
        rotation_axis = np.cross(z_axis, [x_pole, y_pole, z_pole])
        rotation_axis = rotation_axis / np.linalg.norm(rotation_axis)
        
        dot_product = np.dot(z_axis, [x_pole, y_pole, z_pole])
        rotation_angle = np.arccos(dot_product)
        
        # Apply the rotation - custom rotation around an arbitrary axis
        # This is a bit more complex - might need to use a rotation matrix
        # For now, we'll use a simplified approach
        
        # Add a second trace with a different style for comparison
        fig.add_trace(
            go.Scatter3d(
                x=x_temp,  # Just using the standard rotation for now
                y=y_temp, 
                z=z_temp,
                mode='lines',
                line=dict(dash='solid', width=1, color=color),
                name=f"{satellite_name} Alt Orbit",
                text=[f"{satellite_name} Alternative Orbit"] * len(x_temp),
                customdata=[f"{satellite_name} Alternative Orbit"] * len(x_temp),
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
        
        return fig
    
    except Exception as e:
        print(f"Error plotting Mars satellite {satellite_name}: {e}")
        return fig

def debug_planet_transformation(planet_name):
    """Print detailed information about the transformation for a specific planet"""
    print(f"\n==== DEBUG: {planet_name} Transformation ====")
    
    # Get the planet's axial tilt
    tilt = planet_tilts.get(planet_name, 0)
    print(f"Axial tilt: {tilt} degrees")
    
    # Simple tilt matrix
    tilt_rad = np.radians(tilt)
    simple_matrix = np.array([
        [1, 0, 0],
        [0, np.cos(tilt_rad), -np.sin(tilt_rad)],
        [0, np.sin(tilt_rad), np.cos(tilt_rad)]
    ])
    print("\nSimple tilt matrix:")
    print(simple_matrix)
    
    # If we have pole data, calculate the complex matrix
    if planet_name in planet_poles:
        pole = planet_poles[planet_name]
        ra_pole = np.radians(pole['ra'])
        dec_pole = np.radians(pole['dec'])
        
        print(f"\nPole direction: RA = {pole['ra']}°, Dec = {pole['dec']}°")
        
        # Calculate pole vector
        sin_dec = np.sin(dec_pole)
        cos_dec = np.cos(dec_pole)
        sin_ra = np.sin(ra_pole)
        cos_ra = np.cos(ra_pole)
        
        x_pole = cos_dec * cos_ra
        y_pole = cos_dec * sin_ra
        z_pole = sin_dec
        
        print(f"Pole vector: [{x_pole:.4f}, {y_pole:.4f}, {z_pole:.4f}]")
        
        # Calculate node vector
        node_denom = np.sqrt(x_pole**2 + y_pole**2)
        if node_denom > 0:
            x_node = -y_pole / node_denom
            y_node = x_pole / node_denom
            z_node = 0
            
            print(f"Node vector: [{x_node:.4f}, {y_node:.4f}, {z_node:.4f}]")
            
            # Create basis vectors
            z_basis = np.array([x_pole, y_pole, z_pole])
            x_basis = np.array([x_node, y_node, z_node])
            y_basis = np.cross(z_basis, x_basis)
            
            print(f"X basis: [{x_basis[0]:.4f}, {x_basis[1]:.4f}, {x_basis[2]:.4f}]")
            print(f"Y basis: [{y_basis[0]:.4f}, {y_basis[1]:.4f}, {y_basis[2]:.4f}]")
            print(f"Z basis: [{z_basis[0]:.4f}, {z_basis[1]:.4f}, {z_basis[2]:.4f}]")
            
            # Construct transformation matrix
            complex_matrix = np.vstack((x_basis, y_basis, z_basis)).T
            print("\nComplex transformation matrix:")
            print(complex_matrix)
            
            # Calculate the angle between simple and complex transformations
            # by comparing the transformed z-axis
            z_axis = np.array([0, 0, 1])
            simple_z = np.dot(simple_matrix, z_axis)
            complex_z = np.dot(complex_matrix, z_axis)
            
            dot_product = np.dot(simple_z, complex_z)
            angle = np.arccos(min(1, max(-1, dot_product))) * 180 / np.pi
            
            print(f"\nAngle between simple and complex transformations: {angle:.2f}°")
        else:
            print("Cannot calculate node vector (pole is directly aligned with Z-axis)")

def debug_mars_moons(satellites_data, parent_planets):
    """Special debug function for Mars and its moons"""
    print("\n==== MARS SYSTEM DEBUG ====")
    
    # Print Mars' axial tilt and pole direction
    debug_planet_transformation('Mars')
    
    # Print orbital elements for Mars' moons
    mars_moons = parent_planets.get('Mars', [])
    for moon in mars_moons:
        if moon in satellites_data:
            params = satellites_data[moon]
            print(f"\n{moon} orbital elements:")
            for key, value in params.items():
                print(f"  {key}: {value}")
    
    # Test if the moons' inclinations are relative to:
    # 1. Mars' equator
    # 2. Mars' orbital plane
    # 3. The ecliptic
    print("\nInclination references analysis:")
    
    # Mars' axial tilt to the ecliptic
    mars_tilt = np.radians(planet_tilts['Mars'])
    
    for moon in mars_moons:
        if moon in satellites_data:
            params = satellites_data[moon]
            i = params.get('i', 0)
            i_rad = np.radians(i)
            
            # If inclination is relative to Mars' equator,
            # then the true inclination to the ecliptic would be:
            i_to_ecliptic = np.arccos(np.cos(i_rad) * np.cos(mars_tilt) - 
                                       np.sin(i_rad) * np.sin(mars_tilt)) * 180/np.pi
            
            # If inclination is relative to the ecliptic,
            # then the true inclination to Mars' equator would be:
            i_to_equator = np.arccos(np.cos(i_rad) * np.cos(mars_tilt) + 
                                      np.sin(i_rad) * np.sin(mars_tilt)) * 180/np.pi
            
            print(f"\n{moon}:")
            print(f"  Stated inclination: {i}°")
            print(f"  If relative to Mars' equator, inclination to ecliptic would be ~{i_to_ecliptic:.2f}°")
            print(f"  If relative to ecliptic, inclination to Mars' equator would be ~{i_to_equator:.2f}°")

def compare_transformation_methods(fig, satellites_data, parent_planets):
    """Plot orbits with different transformation methods for comparison"""
    # Colors for different systems
    colors = {
        'Mars': 'red',
        'Jupiter': 'orange'
    }
    
    # Plot Mars moons with all transformation methods
    for moon in parent_planets.get('Mars', []):
        if moon in satellites_data:
            for method in ["none", "simple", "complex"]:
                plot_satellite_orbit(
                    moon, 
                    satellites_data[moon],
                    'Mars',
                    colors['Mars'],
                    fig,
                    debug=True,
                    transform_method=method
                )
    
    # Plot Jupiter moons with all transformation methods
    for moon in ['Io', 'Europa', 'Ganymede', 'Callisto']:  # Just the main moons
        if moon in satellites_data:
            for method in ["none", "simple", "complex"]:
                plot_satellite_orbit(
                    moon, 
                    satellites_data[moon],
                    'Jupiter',
                    colors['Jupiter'],
                    fig,
                    debug=True,
                    transform_method=method
                )
    
    return fig

def test_mars_negative_tilt(fig, satellites_data):
    """Test hypothesis that Mars needs a negative tilt application"""
    
    # Mars moons
    for moon in ['Phobos', 'Deimos']:
        if moon in satellites_data:
            # Extract orbital elements
            params = satellites_data[moon]
            a = params.get('a', 0)
            e = params.get('e', 0)
            i = params.get('i', 0)
            omega = params.get('omega', 0)
            Omega = params.get('Omega', 0)
            
            # Standard orbital transformation
            theta = np.linspace(0, 2*np.pi, 360)
            r = a * (1 - e**2) / (1 + e * np.cos(theta))
            
            x_orbit = r * np.cos(theta)
            y_orbit = r * np.sin(theta)
            z_orbit = np.zeros_like(theta)
            
            i_rad = np.radians(i)
            omega_rad = np.radians(omega)
            Omega_rad = np.radians(Omega)
            
            # Standard rotation sequence
            x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, Omega_rad, 'z')
            x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
            x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, omega_rad, 'z')
            
            # Try NEGATIVE tilt for Mars
            tilt_rad = np.radians(-planet_tilts['Mars'])
            x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, tilt_rad, 'x')
            
            # Add to figure
            fig.add_trace(
                go.Scatter3d(
                    x=x_final,
                    y=y_final,
                    z=z_final,
                    mode='lines',
                    line=dict(dash='solid', width=2, color='purple'),
                    name=f"{moon} (Negative Tilt Test)",
                    text=[f"{moon} with negative tilt test"] * len(x_final),
                    hovertemplate='%{text}<extra></extra>',
                    showlegend=True
                )
            )
    
    return fig

def debug_satellite_systems():
    fig = go.Figure()
    
    # Print transformation matrices
    debug_planet_transformation('Mars')
    debug_planet_transformation('Jupiter')
    
    # Special debug for Mars
    debug_mars_moons(planetary_params, parent_planets)
    
    # Compare transformation methods
    fig = compare_transformation_methods(fig, planetary_params, parent_planets)
    
    # Test negative tilt for Mars
    fig = test_mars_negative_tilt(fig, planetary_params)
    
    # Configure the layout
    fig.update_layout(
        title="Satellite System Transformation Debug",
        scene=dict(
            aspectmode='data'
        )
    )
    
    fig.show()

def rotate_points(x, y, z, angle, axis='z'):
    """
    Rotates points (x,y,z) about the given axis by 'angle' radians.
    Returns (xr, yr, zr) as numpy arrays.
    
    Parameters:
        x (array-like): x coordinates
        y (array-like): y coordinates
        z (array-like): z coordinates
        angle (float): rotation angle in radians
        axis (str): axis of rotation ('x', 'y', or 'z')
        
    Returns:
        tuple: (xr, yr, zr) rotated coordinates
    """
    # Convert inputs to numpy arrays if they aren't already
    x = np.array(x, copy=True)
    y = np.array(y, copy=True)
    z = np.array(z, copy=True)

    # Initialize rotated coordinates
    xr = x.copy()
    yr = y.copy()
    zr = z.copy()

    # Perform rotation based on specified axis
    if axis == 'z':
        # Rotate about z-axis
        xr = x * np.cos(angle) - y * np.sin(angle)
        yr = x * np.sin(angle) + y * np.cos(angle)
        # zr remains the same
    elif axis == 'x':
        # Rotate about x-axis
        yr = y * np.cos(angle) - z * np.sin(angle)
        zr = y * np.sin(angle) + z * np.cos(angle)
        # xr remains the same
    elif axis == 'y':
        # Rotate about y-axis
        zr = z * np.cos(angle) - x * np.sin(angle)
        xr = z * np.sin(angle) + x * np.cos(angle)
        # yr remains the same
    else:
        raise ValueError(f"Unknown rotation axis: {axis}. Use 'x', 'y', or 'z'.")

    return xr, yr, zr

def create_planet_transformation_matrix(planet_name):
    """
    Create a transformation matrix for a planet based on its pole direction.
    Transforms from planet's equatorial coordinates to ecliptic coordinates.
    
    Parameters:
        planet_name (str): Name of the planet
        
    Returns:
        numpy.ndarray: 3x3 transformation matrix
    """
    if planet_name not in planet_poles:
        # For planets without explicit pole directions, use the axial tilt
        if planet_name in planet_tilts:
            tilt_rad = np.radians(planet_tilts[planet_name])
            # Simple rotation matrix around the x-axis
            return np.array([
                [1, 0, 0],
                [0, np.cos(tilt_rad), -np.sin(tilt_rad)],
                [0, np.sin(tilt_rad), np.cos(tilt_rad)]
            ])
        return np.identity(3)  # Identity matrix if no data available
    
    # Get pole direction
    pole = planet_poles[planet_name]
    ra_pole = np.radians(pole['ra'])
    dec_pole = np.radians(pole['dec'])
    
    # Calculate the rotation matrix from planet's equatorial to ecliptic
    sin_dec = np.sin(dec_pole)
    cos_dec = np.cos(dec_pole)
    sin_ra = np.sin(ra_pole)
    cos_ra = np.cos(ra_pole)
    
    # Planet's north pole vector in ecliptic coordinates
    x_pole = cos_dec * cos_ra
    y_pole = cos_dec * sin_ra
    z_pole = sin_dec
    
    # Find the ascending node of planet's equator on the ecliptic
    # This is perpendicular to the pole and in the ecliptic plane
    x_node = -y_pole / np.sqrt(x_pole**2 + y_pole**2)
    y_node = x_pole / np.sqrt(x_pole**2 + y_pole**2)
    z_node = 0
    
    # Create orthogonal basis vectors
    x_basis = np.array([x_node, y_node, z_node])
    z_basis = np.array([x_pole, y_pole, z_pole])
    y_basis = np.cross(z_basis, x_basis)
    
    # Construct the transformation matrix
    transform_matrix = np.vstack((x_basis, y_basis, z_basis)).T
    
    return transform_matrix

def plot_satellite_orbit(satellite_name, planetary_params, parent_planet, color, fig=None):
    """
    Plot the idealized orbit of a satellite around its parent planet.
    
    Parameters:
        satellite_name (str): Name of the satellite
        planetary_params (dict): Dictionary containing orbital parameters for all objects
        parent_planet (str): Name of the parent planet
        color (str): Color to use for the orbit line
        fig (plotly.graph_objects.Figure): Existing figure to add the orbit to
        
    Returns:
        plotly.graph_objects.Figure: Figure with the satellite orbit added
    """
    if fig is None:
        fig = go.Figure()
    
    try:
        # Get the orbital parameters for this specific satellite
        if satellite_name not in planetary_params:
            print(f"Error: No orbital parameters found for {satellite_name}")
            return fig
            
        orbital_params = planetary_params[satellite_name]
        
        # Extract orbital elements
        a = orbital_params.get('a', 0)  # Semi-major axis in AU
        e = orbital_params.get('e', 0)  # Eccentricity
        i = orbital_params.get('i', 0)  # Inclination in degrees
        omega = orbital_params.get('omega', 0)  # Argument of periapsis in degrees
        Omega = orbital_params.get('Omega', 0)  # Longitude of ascending node in degrees
        
        print(f"\nPlotting {satellite_name} orbit around {parent_planet}")
        print(f"Orbital elements: a={a}, e={e}, i={i}°, ω={omega}°, Ω={Omega}°")
        
        # Generate ellipse in orbital plane
        theta = np.linspace(0, 2*np.pi, 360)  # 360 points for smoothness
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)

        # Convert angles to radians
        i_rad = np.radians(i)
        omega_rad = np.radians(omega)
        Omega_rad = np.radians(Omega)

        # Standard orbital element rotation sequence
        # 1. Longitude of ascending node (Ω) around z-axis
        x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, Omega_rad, 'z')
        # 2. Inclination (i) around x-axis
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
        # 3. Argument of periapsis (ω) around z-axis
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, omega_rad, 'z')
        
        # Apply transformation based on the planet
        if parent_planet == 'Mars':
            # This 25° value is particularly interesting because it's very close to Mars' axial tilt of 25.19°. 
            # This suggests there might be a direct relationship between Mars' axial tilt and the reference frame used 
            # for defining its satellites' orbital elements. The fact that Deimos aligns better at 25° while Phobos aligns 
            # better at 26° could be related to: 1) Small differences in how each moon's orbital elements were measured or 
            # calculated. 2) The fact that Phobos orbits much closer to Mars and might be more affected by Mars' non-spherical 
            # gravity field 3) Possible time-dependent variations in the orbital planes. To put this discovery in context: we've 
            # essentially found that Mars' moons' orbital elements are defined in a reference frame that requires a Y-axis 
            # rotation approximately equal to Mars' axial tilt to align with the ecliptic reference frame used in your 
            # visualization. This makes intuitive sense astronomically, as it suggests the orbital elements are defined relative 
            # to Mars' equatorial plane.
            #
            # Using Mars' exact axial tilt (25.19°) as the Y-axis rotation value creates a perfect astronomical justification 
            # for the transformation. It strongly suggests that the orbital elements for Mars' satellites are indeed defined 
            # relative to Mars' equatorial plane, which makes sense from a planetary science perspective.
            #
            # "Reference Frame Note: The orbital elements for Mars' satellites (Phobos and Deimos) are provided relative to 
            # Mars' equatorial plane. When transforming these elements to ecliptic coordinates for visualization, a rotation 
            # of 25.19° around the Y-axis (equivalent to Mars' axial tilt) should be applied after the standard orbital element 
            # rotations."
            # 
            # A Y-axis rotation (not X) is needed because it represents a rotation around 
            # the ecliptic plane's normal axis, which correctly positions the orbital planes
            # of Phobos and Deimos relative to Mars' orbital plane.
            mars_y_rotation = np.radians(25.19)
            x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, mars_y_rotation, 'y')
            print(f"Transformation applied: Mars with Y-axis rotation of 25.19°")    # originally 35.4
            
        elif parent_planet == 'Jupiter':
            # Use simple tilt for Jupiter (which works well)
            if 'Jupiter' in planet_tilts:
                tilt_rad = np.radians(planet_tilts['Jupiter'])
                x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, tilt_rad, 'x')
                print(f"Transformation applied: Jupiter with tilt={planet_tilts['Jupiter']}°")
            else:
                x_final, y_final, z_final = x_temp, y_temp, z_temp
                print("No transformation applied for Jupiter (missing tilt data)")
            
        elif parent_planet in planet_tilts:
            # Use recorded tilt for other planets
            tilt_rad = np.radians(planet_tilts[parent_planet])
            x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, tilt_rad, 'x')
            print(f"Transformation applied: {parent_planet} with tilt={planet_tilts[parent_planet]}°")
            
        else:
            # No transformation for planets without tilt data
            x_final, y_final, z_final = x_temp, y_temp, z_temp
            print(f"No transformation applied for {parent_planet} (no tilt data available)")
        
        # Create hover text for the orbit
        hover_text = f"{satellite_name} Ideal Orbit around {parent_planet}"
        
        # Add the orbit trace to the figure
        fig.add_trace(
            go.Scatter3d(
                x=x_final,
                y=y_final,
                z=z_final,
                mode='lines',
                line=dict(dash='dot', width=1, color=color),
                name=f"{satellite_name} Ideal Orbit",
                text=[hover_text] * len(x_final),
                customdata=[hover_text] * len(x_final),
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
        
        return fig
    
    except Exception as e:
        print(f"Error plotting {satellite_name} orbit: {e}")
        return fig

def plot_idealized_orbits(fig, objects_to_plot, center_id='Sun', objects=None, planetary_params=None, parent_planets=None, color_map=None):
    """
    Plot idealized orbits for planets, dwarf planets, asteroids, KBOs, and moons.
    For non-Sun centers, only plots moons of that center body.
    
    Parameters:
        fig (plotly.graph_objects.Figure): The figure to add orbits to
        objects_to_plot (list): List of object names to potentially plot orbits for
        center_id (str): The central body ('Sun' or a planet name)
        objects (list): List of object dictionaries with metadata
        planetary_params (dict): Dictionary of orbital parameters for each object
        parent_planets (dict): Dictionary mapping parent planets to their satellites
        color_map (callable): Function to get color for an object by name
        
    Returns:
        plotly.graph_objects.Figure: Figure with idealized orbits added
    """
    # Track skipped objects by category
    skipped = {
        'satellites': [],
        'comets': [],
        'missions': [],
        'no_params': [],
        'invalid_orbit': []
    }

    plotted = []

    # If objects parameter is None, handle gracefully
    if objects is None:
        print("Warning: objects list is None, cannot determine object properties")
        return fig
        
    # If planetary_params is None, handle gracefully
    if planetary_params is None:
        print("Warning: planetary_params is None, cannot plot idealized orbits")
        return fig
        
    # If parent_planets is None, handle gracefully
    if parent_planets is None:
        print("Warning: parent_planets is None, cannot determine satellite relationships")
        return fig
        
    # If color_map is None, use a default function
    if color_map is None:
        def default_color_map(name):
            # Default colors for common objects
            colors = {
                'Mercury': 'gray',
                'Venus': 'orange',
                'Earth': 'blue',
                'Mars': 'red',
                'Jupiter': 'brown',
                'Saturn': 'gold',
                'Uranus': 'lightblue',
                'Neptune': 'darkblue',
                'Pluto': 'purple'
            }
            return colors.get(name, 'white')
        color_map = default_color_map

    # If center is not the Sun, we only want to plot moons of that center
    if center_id != 'Sun':
        # Get list of moons for this center
        moons = parent_planets.get(center_id, [])
        
        # Filter objects_to_plot to only include moons of this center
        objects_to_plot = [obj for obj in objects_to_plot if obj in moons]

        # For each satellite of the center object, use the standard function
        for moon_name in objects_to_plot:
            # Find the object in the objects list
            moon_info = next((obj for obj in objects if obj['name'] == moon_name), None)
            if moon_info is None:
                continue
                
            # Use the satellite plotting function with built-in planet-specific transformations
            fig = plot_satellite_orbit(
                moon_name, 
                planetary_params,
                center_id, 
                color_map(moon_name), 
                fig
            )
            
            plotted.append(moon_name)
    
    # If center is the Sun, plot orbits for selected heliocentric objects
    else:
        for obj_name in objects_to_plot:
            # Find the object in the objects list
            obj_info = next((obj for obj in objects if obj['name'] == obj_name), None)
            if obj_info is None:
                continue
                
            # Check each skip condition and record the reason
            if obj_name not in planetary_params:
                skipped['no_params'].append(obj_name)
                continue

            # Check if this is a satellite of another object (but not of the center)
            is_satellite_of_another = False
            for planet, moons in parent_planets.items():
                if obj_name in moons and planet != center_id:
                    is_satellite_of_another = True
                    break

            if is_satellite_of_another:
                # If we're centered on the Sun, skip satellites of other objects
                skipped['satellites'].append(obj_name)
                continue            

            elif obj_info.get('is_mission', False):
                skipped['missions'].append(obj_name)
                continue
            
            params = planetary_params[obj_name]
            a = params.get('a', 0)

            # Skip if semi-major axis is zero or very small
            if a < 0.0001:
                continue

            e = params.get('e', 0)
            i = params.get('i', 0)
            omega = params.get('omega', 0)
            Omega = params.get('Omega', 0)

            # Generate ellipse in orbital plane
            theta = np.linspace(0, 2*np.pi, 360)  # 360 points for smoothness
            r = a * (1 - e**2) / (1 + e * np.cos(theta))
            
            x_orbit = r * np.cos(theta)
            y_orbit = r * np.sin(theta)
            z_orbit = np.zeros_like(theta)

            # Convert angles to radians
            i_rad = np.radians(i)
            omega_rad = np.radians(omega)
            Omega_rad = np.radians(Omega)

            # Rotate ellipse by argument of periapsis (ω) around z-axis
            x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, omega_rad, 'z')
            # Then rotate by inclination (i) around x-axis
            x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
            # Then rotate by longitude of ascending node (Ω) around z-axis
            x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, Omega_rad, 'z')

            fig.add_trace(
                go.Scatter3d(
                    x=x_final,
                    y=y_final,
                    z=z_final,
                    mode='lines',
                    line=dict(dash='dot', width=1, color=color_map(obj_name)),
                    name=f"{obj_name} Ideal Orbit",
                    text=[f"{obj_name} Ideal Orbit"] * len(x_final),
                    customdata=[f"{obj_name} Ideal Orbit"] * len(x_final),
                    hovertemplate='%{text}<extra></extra>',
                    showlegend=True                    
                )
            )

            plotted.append(obj_name)

    # Print summary of plotted and skipped objects
    print("\nIdeal Orbit Summary:")
    print(f"Plotted ideal orbits for {len(plotted)} objects:")
    for obj in plotted:
        print(f"  - {obj}")

    print("\nSkipped ideal orbits for:")
    for category, objects_list in skipped.items():
        if objects_list:
            print(f"\n{category.capitalize()} ({len(objects_list)}):")
            for obj in objects_list:
                print(f"  - {obj}")

    return fig

