# idealized_orbits.py

import numpy as np
import math
import plotly.graph_objs as go
import traceback  # Add this import
from datetime import datetime, timedelta
from constants_new import color_map, KNOWN_ORBITAL_PERIODS
from apsidal_markers import add_perihelion_marker, add_apohelion_marker

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
    'Earth': {              #  2025-Jul-06
        'a': 1.000000,
        'e': 0.016710,
        'i': 0.00005,
        'omega': 114.207,
        'Omega': -11.26064,
        'epoch': '2025-7-6',
        'perihelion_dates': [
        '2026-01-03',  # Following perihelion
        ],
        'aphelion_dates': [
        '2026-07-06',  # Following aphelion
        ]
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
        'a': 600,          # Semi-major axis in AU (updated to match 500-700 AU range from IRAS/AKARI study)
        'e': 0.30,         # Eccentricity (slightly adjusted to align with 280-1120 AU perihelion/aphelion range)
        'i': 6,            # Inclination in degrees (2025 estimate: 6°)
        'L': 238,          # Mean longitude at epoch in degrees (unchanged)
        'omega': 150,      # Argument of perihelion in degrees (unchanged)
        'Omega': 90        # Longitude of ascending node in degrees (unchanged)
    },
    
    # Dwarf Planets

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

    'GV9': {  # 90568 (2004 GV9); Epoch 2017-11-1   
        'a': 42.26253681484609,     # A, semi-major axis in AU
        'e': .08206106683377956,   # EC, eccentricity
        'i': 21.93322237277237,     # IN, inclination in degrees
        'omega': 295.190819856158, # W, argument of perihelion in degrees
        'Omega': 250.6628794038891  # OM, longitude of ascending node in degrees
    },

    'Varuna': {
        'a': 42.947,     # semi-major axis in AU
        'e': 0.051739,   # eccentricity
        'i': 17.200,     # inclination in degrees
        'omega': 97.286,  # argument of perihelion in degrees
        'Omega': 97.286   # longitude of ascending node in degrees
    },

    'Haumea': {
        'a': 43.13,
        'e': 0.191,
        'i': 28.20,
        'omega': 240.20,
        'Omega': 122.10
    },

    'Quaoar': {
        'a': 43.325,
        'e': 0.0392,
        'i': 8.34,
        'omega': 157.631,
        'Omega': 188.809
    },

    'Arrokoth': {                  # Epoch 2017-12-14, heliocentric
        'a': 44.44519963724322,   # A, semi-major axis in AU
        'e': .03868645692376498,   # EC, eccentricity
        'i': 2.45301305206896,      # IN, inclination in degrees
        'omega': 176.1507602341478, # W, argument of perihelion in degrees
        'Omega': 158.939446659904   # OM, longitude of ascending node in degrees
    },

    'Makemake': {   # 136472 Makemake (2005 FY9); Epoch 2018-Jan-10
        'a': 45.6923640352447,                    # A
        'e': .1551157031828145,                   # EC
        'i': 28.98446068551257,                   # IN
        'omega': 295.7568523219785,               # W
        'Omega': 79.60732027458391                # OM
    },

    'Gonggong': {  # 225088 Gonggong (2007 OR10); Epoch 2017-Sep-25
        'a': 67.15612088312527,     # A, semi-major axis in AU
        'e': .5057697166633393,   # EC, eccentricity
        'i': 30.86452616352285,     # IN, inclination in degrees
        'omega': 207.2059900430104, # W, argument of perihelion in degrees
        'Omega': 336.8262717815297  # OM, longitude of ascending node in degrees
    },    

    'Eris': {
        'a': 67.78,
        'e': 0.441,
        'i': 44.03,
        'omega': 150.977,
        'Omega': 35.873
    },

    'Sedna': {  # 90377 Sedna (2003 VB12); Epoch 2018-May-16
        'a': 481.3036019474312,         # A
        'e': .8418992747337005,         # EC
        'i': 11.92926934569724,         # IN
        'omega': 311.5908685997484,     # W
        'Omega': 144.4059276991507      # OM
    },

    '2017 OF201': {  # Epoch 2012-Jan-22.00
        'a': 911.3212633626483,         # A
        'e': .95044195853967,         # EC
        'i': 16.20068039109616,         # IN
        'omega': 338.23502348994,     # W
        'Omega': 328.5637374192406      # OM
    },

    # Asteroids

    'Apophis': {
        'a': 0.922583,   # Horizons: A, semi-major axis in AU
        'e': 0.191481,   # Horizons: EC, eccentricity
        'i': 3.331,      # inclination in degrees
        'omega': 126.394, # argument of perihelion in degrees
        'Omega': 204.061  # longitude of ascending node in degrees
    },  

    'Kamo oalewa': {     # 469219 Kamo`oalewa (2016 HO3)      2025-Jul-05 08:35:28        
        'a': 1.00102447694204,   # Horizons: A, semi-major axis in AU
        'e': .1040534310625292,   # Horizons: EC, eccentricity
        'i': 7.773894173631178,      # Horizons: IN, inclination in degrees
        'omega': 307.0951007739783, # Horizons: W, argument of perihelion in degrees
        'Omega': 66.43991583004482   # Horizons: OM, longitude of ascending node in degrees
    }, 

    '2024 PT5': {                  # Epoch 2024-10-20, heliocentric
        'a': 1.012228628670663,   # Horizons: A, semi-major axis in AU
        'e': .02141074038624791,   # Horizons: EC, eccentricity
        'i': 1.518377382131216,      # Horizons: IN, inclination in degrees
        'omega': 116.8074860094156, # Horizons: W, argument of perihelion in degrees
        'Omega': 305.1069316209851   # Horizons: OM, longitude of ascending node in degrees
    },

    'Bennu': {
        'a': 1.126391,    # semi-major axis in AU
        'e': 0.203745,    # eccentricity
        'i': 6.035,       # inclination in degrees
        'omega': 66.223,  # argument of perihelion in degrees
        'Omega': 2.061    # longitude of ascending node in degrees
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

    'Eros': {
        'a': 1.458040,   # semi-major axis in AU
        'e': 0.222868,   # eccentricity
        'i': 10.829,     # inclination in degrees
        'omega': 178.817, # argument of perihelion in degrees
        'Omega': 304.435  # longitude of ascending node in degrees
    },

    '2023 JF': {        # (2023 JF)  EPOCH=  2460073.5 ! 2023-May-09.00 (TDB)
        'a': 1.680153966583222,   # A - semi-major axis in AU
        'e': .409819444019783,   # EC - eccentricity
        'i': 3.1489028778487,     # IN - inclination in degrees
        'omega': 199.537622506113, # W - argument of perihelion in degrees
        'Omega': 50.09327122563936  # OM - longitude of ascending node in degrees
    },

    'Dinkinesh': {      # 152830 Dinkinesh (1999 VD57)
        'a': 2.191622877873451,   # A - semi-major axis in AU
        'e': .1121269945294693,   # EC - eccentricity
        'i': 2.093523142255687,     # IN - inclination in degrees
        'omega': 66.78467710309617, # W - argument of perihelion in degrees
        'Omega': 21.38248704730461  # OM - longitude of ascending node in degrees
    },    

    'Vesta': {
        'a': 2.3617,
        'e': 0.089,
        'i': 7.155,
        'omega': 151.216,
        'Omega': 103.851
    },

    'Šteins': {
        'a': 2.363,      # semi-major axis in AU
        'e': 0.146,      # eccentricity
        'i': 9.944,      # inclination in degrees
        'omega': 250.97,  # argument of perihelion in degrees
        'Omega': 55.39    # longitude of ascending node in degrees
    },

    'Donaldjohanson': {     # 52246 Donaldjohanson (1981 EQ5)
        'a': 2.383273486221501,      # A - semi-major axis in AU
        'e': .1874831199365464,      # EC - eccentricity
        'i': 4.423903983190933,      # IN - inclination in degrees
        'omega': 212.9285580998883,  # W - argument of perihelion in degrees
        'Omega': 262.7951724145965     # OM - longitude of ascending node in degrees
    },

    '2024 DW': {                  # 50613029 (2024 DW) 2025-Jul-05 10:27:18; Soln.date: 2024-Feb-23
        'a': 2.421098478271158,   # Horizons: A, semi-major axis in AU
        'e': .6939958024514898,   # Horizons: EC, eccentricity
        'i': .9861902430422796,      # Horizons: IN, inclination in degrees
        'omega': 244.5179261214832, # Horizons: W, argument of perihelion in degrees
        'Omega': 335.4879825233473,   # Horizons: OM, longitude of ascending node in degrees
        'epoch': '2024-02-19'  # Horizons: epoch
    },

    'Lutetia': {                  # Epoch 2017-10-12, heliocentric
        'a': 2.434591597038037,   # Horizons: A, semi-major axis in AU
        'e': .1644174522633922,   # Horizons: EC, eccentricity
        'i': 3.063715677953934,      # Horizons: IN, inclination in degrees
        'omega': 249.980528664283, # Horizons: W, argument of perihelion in degrees
        'Omega': 80.87713180326485   # Horizons: OM, longitude of ascending node in degrees
    },

    '2024 YR4': {                  # Epoch 2025-1-30, heliocentric, solution date 2025-6-3
        'a': 2.516308070047454,   # Horizons: A, semi-major axis in AU
        'e': .6615999301423001,   # Horizons: EC, eccentricity
        'i': 3.408259321981154,      # Horizons: IN, inclination in degrees
        'omega': 134.3644983455991, # Horizons: W, argument of perihelion in degrees
        'Omega': 271.3674693540159   # Horizons: OM, longitude of ascending node in degrees
    },

    'Ceres': {
        'a': 2.7675,
        'e': 0.076,
        'i': 10.593,
        'omega': 73.597,
        'Omega': 80.393
    },

    # Trojan Asteroids

     'Orus': {                  # 21900 Orus (1999 VQ10)
        'a': 5.12481038867513,   # Horizons: A, semi-major axis in AU
        'e': .03658969107145676,   # Horizons: EC, eccentricity
        'i': 8.468402951870347,      # Horizons: IN, inclination in degrees
        'omega': 179.5712820784224, # Horizons: W, argument of perihelion in degrees
        'Omega': 258.5587182277959   # Horizons: OM, longitude of ascending node in degrees
    }, 

     'Polymele': {                  # 15094 Polymele (1999 WB2)
        'a': 5.183610039255559,   # Horizons: A, semi-major axis in AU
        'e': .09688597854047172,   # Horizons: EC, eccentricity
        'i': 12.98094196026331,      # Horizons: IN, inclination in degrees
        'omega': 5.149831531818331, # Horizons: W, argument of perihelion in degrees
        'Omega': 50.31413377311653   # Horizons: OM, longitude of ascending node in degrees
    }, 

     'Eurybates': {                  # 3548 Eurybates (1973 SO)
        'a': 5.209549873585049,   # Horizons: A, semi-major axis in AU
        'e': .0911999243850036,   # Horizons: EC, eccentricity
        'i': 8.054169046592317,      # Horizons: IN, inclination in degrees
        'omega': 27.83332476783044, # Horizons: W, argument of perihelion in degrees
        'Omega': 43.54011293260102   # Horizons: OM, longitude of ascending node in degrees
    },  

     'Patroclus': {                  # 617 Patroclus (A906 UL) 
        'a': 5.212775153315913,   # Horizons: A, semi-major axis in AU
        'e': .1394751015199425,   # Horizons: EC, eccentricity
        'i': 22.05719746380513,      # Horizons: IN, inclination in degrees
        'omega': 307.9473518701323, # Horizons: W, argument of perihelion in degrees
        'Omega': 44.34955228487597   # Horizons: OM, longitude of ascending node in degrees
    }, 

     'Leucus': {                  # 11351 Leucus (1997 TS25)
        'a': 5.2899315120334,   # Horizons: A, semi-major axis in AU
        'e': .06389742479789216,   # Horizons: EC, eccentricity
        'i': 11.55528566945522,      # Horizons: IN, inclination in degrees
        'omega': 160.4023262565797, # Horizons: W, argument of perihelion in degrees
        'Omega': 251.0747114724082   # Horizons: OM, longitude of ascending node in degrees
    },  

    # Comets with closed elliptical orbits; object type 'orbital'
    
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

    'NEOWISE': {                  # 2020-Jul-06.0000000, heliocentric, NEOWISE (C/2020 F3) 
        'a': 358.4679565529321,   # Horizons: A, semi-major axis in AU
        'e': .9991780262531292,   # Horizons: EC, eccentricity
        'i': 128.9375027594809,      # Horizons: IN, inclination in degrees
        'omega': 37.2786584481257, # Horizons: W, argument of perihelion in degrees
        'Omega': 61.01042818536988   # Horizons: OM, longitude of ascending node in degrees
    },    

    # Comets with parabolic trajectories, object type 'trajectory'

     'C/2025_K1': {                  # ATLAS (C/2025 K1)            2025-Jul-11 21:59:05 
        # Rec #:90004909 (+COV) Soln.date: 2025-Jul-10_13:42:09      # obs: 563 (93 days)
        'a': -1328.874007526048,   # Horizons: A, semi-major axis in AU
        'e': 1.000251464554613,   # Horizons: EC, eccentricity
        'i': 147.864867556013,      # Horizons: IN, inclination in degrees
        'omega': 271.0285208159306, # Horizons: W, argument of perihelion in degrees
        'Omega': 97.55648983040697   # Horizons: OM, longitude of ascending node in degrees
    },   

    # Interstellar objects; hyperbolic trajectories, object type 'trajectory'

     '3I/ATLAS': {                  # 2025-Jul-01, heliocentric, ATLAS (C/2025 N1) 90004916
         # Ephemeris / WWW_USER Fri Jul 11 12:19:05 2025 Pasadena, USA      / Horizons
        'a': -.2636282119444073,   # Horizons: A, semi-major axis in AU
        'e': 6.151136010582101,   # Horizons: EC, eccentricity
        'i': 175.113183893991,      # Horizons: IN, inclination in degrees
        'omega': 127.9882324877828, # Horizons: W, argument of perihelion in degrees
        'Omega': 322.1637461140604   # Horizons: OM, longitude of ascending node in degrees
    },    

    # Satellites

    'Moon': {            # 301; Revised 7-31-2013, geocentric; source: https://ssd.jpl.nasa.gov/horizons/app.html#/
#        'a': 384400,   # Horizons: A, semi-major axis in AU
        'a': 0.002570,   # Horizons: A, semi-major axis in AU; 384400 km or 0.00257 au
        'e': 0.05490,   # Horizons: EC, eccentricity; 0.05490 was 0.0554
        'i': 5.145,      # Horizons: IN, inclination in degrees; 5.145 deg was 5.16
        'omega': 318.15, # Horizons: W, argument of perihelion in degrees
        'Omega': 125.08,   # Horizons: OM, longitude of ascending node in degrees
        'epoch': '2013-07-31'
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

    'Phoebe': {             # 609;  Revised: Jan 26, 2022 Phoebe / (Saturn) 609; Orbital period = 550.31 d
#        'a': 12947780,          # semi-major axis in km; Semi-major axis, a (km)= 12947.78(10^3) 
        'a': 0.08655,          # semi-major axis in AU
#        'a_parent': 214.7,     # semi-major axis in Saturn radii
        'e': 0.1635,           # eccentricity
        'i': 175.986,            # inclination to Saturn's equator in degrees (retrograde)
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

     'Portia': {             # 712
#       'a': 66100,         # semi-major axis in km
        'a': 0.0004419,         # semi-major axis in AU
#        'a_parent': ,     # semi-major axis in Uranus radii
        'e': 0.000,           # eccentricity
        'i': 0.0,            # inclination to Uranus's equator in degrees
        'omega': 0,      # argument of perihelion in degrees
        'Omega': 0       # longitude of ascending node in degrees
    },   

     'Mab': {             # 726
#       'a': 97700,         # semi-major axis in km
        'a': 0.0006531,         # semi-major axis in AU
#        'a_parent': ,     # semi-major axis in Uranus radii
        'e': 0.003,           # eccentricity
        'i': 0.1,            # inclination to Uranus's equator in degrees
        'omega': 237.9,      # argument of perihelion in degrees
        'Omega': 188.2       # longitude of ascending node in degrees
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

    'Despina': {             # 805
#        'a': 52500,         # semi-major axis in km
        'a': 0.0003509,         # semi-major axis in AU
#        'a_parent': ,     # semi-major axis in Neptune radii
        'e': 0.000,         # eccentricity (nearly circular)
        'i': 0.0,          # inclination to Neptune's equator in degrees (retrograde)
        'omega': 0.0,       # argument of perihelion in degrees
        'Omega': 0.0       # longitude of ascending node in degrees
    },

    'Galatea': {             # 806
#        'a': 62000,         # semi-major axis in km
        'a': 0.0004144,         # semi-major axis in AU
#        'a_parent': ,     # semi-major axis in Neptune radii
        'e': 0.000,         # eccentricity (nearly circular)
        'i': 0.0,          # inclination to Neptune's equator in degrees (retrograde)
        'omega': 0.0,       # argument of perihelion in degrees
        'Omega': 0.0       # longitude of ascending node in degrees
    },

    # Pluto's Moons
    'Charon': {             # 901; revised 4/3/2024 post-New Horizons
#        'a': 19600,         # semi-major axis in km
        'a': 0.00013102,         # semi-major axis in AU
#        'a_parent': 16.4,      # semi-major axis in Pluto radii
        'e': 0.000,           # eccentricity (nearly circular)
        'i': 0.0,            # inclination to Pluto's equator in degrees
        'omega': 0.0,      # argument of perihelion in degrees
        'Omega': 0.0       # longitude of ascending node in degrees
    },

    'Styx': {              # 905; revised 4-3-2024; Fit to post New Horizons encounter and Gaia data through 2023.
#        'a': 43200,         # semi-major axis in km
        'a': 0.00028877,         # semi-major axis in AU; 0.00043583
#        'a_parent': ,     # semi-major axis in Pluto radii
        'e': 0.025,           # eccentricity
        'i': 0.0,            # inclination to Pluto's equator in degrees
        'omega': 322.5,      # argument of perihelion in degrees
        'Omega': 0.0       # longitude of ascending node in degrees
    },    

    'Nix': {                # 902; revised 4/3/2024 post-New Horizons
#        'a': 49300,         # semi-major axis in km
        'a': 0.00032955,         # semi-major axis in AU
#        'a_parent': 31.3,      # semi-major axis in Pluto radii
        'e': 0.025,           # eccentricity
        'i': 0.0,            # inclination to Pluto's equator in degrees
        'omega': 31.4,      # argument of perihelion in degrees
        'Omega': 0.0         # longitude of ascending node in degrees
    },
    'Kerberos': {              # 904; revised 4-3-2024; Fit to post New Horizons encounter and Gaia data through 2023.
#        'a': 58300,         # semi-major axis in km
        'a': 0.00038971,         # semi-major axis in AU; 0.00043583
#        'a_parent': ,     # semi-major axis in Pluto radii
        'e': 0.010,           # eccentricity
        'i': 0.4,            # inclination to Pluto's equator in degrees
        'omega': 32.1,      # argument of perihelion in degrees
        'Omega': 314.3       # longitude of ascending node in degrees
    },   

    'Hydra': {              # 903; revised 4-3-2024; Fit to post New Horizons encounter and Gaia data through 2023.
#        'a': 65200,         # semi-major axis in km
        'a': 0.00043584,         # semi-major axis in AU; 0.00043583
#        'a_parent': 83.9,     # semi-major axis in Pluto radii
        'e': 0.009,           # eccentricity
        'i': 0.3,            # inclination to Pluto's equator in degrees
        'omega': 139.3,      # argument of perihelion in degrees
        'Omega': 114.3       # longitude of ascending node in degrees
    },

    # Eris's Moon
    'Dysnomia': {
#        'a': 0.000364,         # semi-major axis in km
        'a': 0.000364,         # semi-major axis in AU
#        'a_parent': 36.2,      # semi-major axis in Eris radii (estimate)
        'e': 0.0062,           # eccentricity
        'i': 78.29,            # inclination in degrees (to the ecliptic)
        'omega': 139.65,       # argument of perihelion in degrees
        'Omega': 29.43         # longitude of ascending node in degrees
    },

} 

parent_planets = {
    'Earth': ['Moon'],
    'Mars': ['Phobos', 'Deimos'],
    'Jupiter': ['Io', 'Europa', 'Ganymede', 'Callisto', 'Metis', 'Adrastea', 'Amalthea', 'Thebe'],
    'Saturn': ['Titan', 'Enceladus', 'Rhea', 'Dione', 'Tethys', 'Mimas', 'Iapetus', 'Phoebe', 'Pan', 'Daphnis', 'Prometheus',
               'Pandora', 'Hyperion'],
    'Uranus': ['Miranda', 'Ariel', 'Umbriel', 'Titania', 'Oberon', 'Portia', 'Mab'],
    'Neptune': ['Triton', 'Despina', 'Galatea'],
    'Pluto': ['Charon', 'Styx', 'Nix', 'Kerberos', 'Hydra'],
    'Eris': ['Dysnomia']
}

# Dictionary of planet tilts (degrees)
planet_tilts = {
    'Earth': 0,         # 23.44 tilt not needed, moon already defined in ecliptic frame
    'Mars': 25.19,      # Mars axial tilt
    'Jupiter': 3.13,    # Jupiter axial tilt
    'Saturn': -26.73,   # Saturn axial tilt (negative works better)
    'Uranus': 97.77,    # Uranus axial tilt
    'Neptune': 28.32,   # Neptune axial tilt (28.32) 
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

def plot_hyperbolic_orbit(obj_name, params, color, fig, date=None):
    """
    Plot a hyperbolic orbit for interstellar objects or comets with e > 1.
    Enhanced version that handles high eccentricity cases.
    """
    try:
        a = params.get('a', 0)  # Semi-major axis (negative for hyperbolic orbits)
        e = params.get('e', 0)  # Eccentricity (> 1 for hyperbolic orbits)
        i = params.get('i', 0)  # Inclination in degrees
        omega = params.get('omega', 0)  # Argument of perihelion in degrees
        Omega = params.get('Omega', 0)  # Longitude of ascending node in degrees
        
        # For hyperbolic orbits, a is negative and e > 1
        if e <= 1:
            print(f"Warning: {obj_name} has e={e}, not a hyperbolic orbit")
            return False
            
        # Calculate perihelion distance
        q = abs(a) * (e - 1)  # Perihelion distance for hyperbolic orbit
        
        # Determine a reasonable maximum distance to plot
        # For high eccentricity, limit the visible range
        if e > 10:
            max_distance = min(50, q * 20)  # Very narrow trajectory
        elif e > 5:
            max_distance = min(100, q * 30)  # Narrow trajectory
        else:
            max_distance = 200  # Standard range for moderate eccentricity
        
        # For hyperbolic orbits, the true anomaly range where the object is bound
        # to the solar system is limited by the asymptotic true anomaly
        theta_inf = np.arccos(-1/e)  # Asymptotic true anomaly
        
        # Special handling for high eccentricity
        if e > 5:
            # Calculate angle where r = max_distance
            cos_theta_max = ((abs(a) * (e**2 - 1) / max_distance) - 1) / e
            
            if -1 <= cos_theta_max <= 1:
                theta_visible = np.arccos(cos_theta_max)
                theta_limit = min(theta_inf - 0.01, theta_visible)
            else:
                # Very extreme case
                theta_limit = min(theta_inf - 0.01, np.pi/6)  # Max 30 degrees
            
            margin = 0.01  # Small margin for extreme cases
            num_points = 1000  # More points for smoother curve
        else:
            theta_limit = theta_inf
            margin = 0.1  # Standard margin
            num_points = 500
        
        # Create array of true anomaly values
        theta = np.linspace(-theta_limit + margin, theta_limit - margin, num_points)
        
        # Calculate radius for each true anomaly using hyperbolic orbit equation
        r = abs(a) * (e**2 - 1) / (1 + e * np.cos(theta))
        
        # Filter points within reasonable range
        valid_points = (r > 0) & (r <= max_distance)
        
        # Check if we have enough valid points
        if np.sum(valid_points) < 20:
            # Focus on perihelion region for extreme cases
            print(f"Note: {obj_name} has extreme eccentricity (e={e:.2f}), showing perihelion region only")
            theta_narrow = np.linspace(-0.1, 0.1, 100)
            r_narrow = abs(a) * (e**2 - 1) / (1 + e * np.cos(theta_narrow))
            valid_narrow = (r_narrow > 0) & (r_narrow <= max_distance * 1.5)
            
            if np.sum(valid_narrow) > 5:
                theta = theta_narrow[valid_narrow]
                r = r_narrow[valid_narrow]
                valid_points = np.ones_like(r, dtype=bool)
            else:
                print(f"Warning: Unable to plot meaningful trajectory for {obj_name} with e={e:.2f}")
                return False
        
        theta = theta[valid_points]
        r = r[valid_points]
        
        # Convert to Cartesian coordinates in orbital plane
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)
        
        # Convert angles to radians
        i_rad = np.radians(i)
        omega_rad = np.radians(omega)
        Omega_rad = np.radians(Omega)
        
        # Apply orbital element rotations
        # 1. Rotate by argument of perihelion (omega) around z-axis
        x1 = x_orbit * np.cos(omega_rad) - y_orbit * np.sin(omega_rad)
        y1 = x_orbit * np.sin(omega_rad) + y_orbit * np.cos(omega_rad)
        z1 = z_orbit
        
        # 2. Rotate by inclination (i) around x-axis
        x2 = x1
        y2 = y1 * np.cos(i_rad) - z1 * np.sin(i_rad)
        z2 = y1 * np.sin(i_rad) + z1 * np.cos(i_rad)
        
        # 3. Rotate by longitude of ascending node (Omega) around z-axis
        x_final = x2 * np.cos(Omega_rad) - y2 * np.sin(Omega_rad)
        y_final = x2 * np.sin(Omega_rad) + y2 * np.cos(Omega_rad)
        z_final = z2
        
        # Create hover text with eccentricity warning for extreme cases
        if e > 10:
            hover_text = f"{obj_name} Hyperbolic Orbit<br>EXTREME eccentricity: e={e:.2f}<br>Perihelion: q={q:.3f} AU<br>Nearly straight-line trajectory"
        elif e > 5:
            hover_text = f"{obj_name} Hyperbolic Orbit<br>High eccentricity: e={e:.2f}<br>Perihelion: q={q:.3f} AU<br>Very narrow trajectory"
        else:
            hover_text = f"{obj_name} Hyperbolic Orbit<br>Eccentricity: e={e:.2f}<br>Perihelion: q={q:.3f} AU"
        
        # Add the trace to the figure
        fig.add_trace(go.Scatter3d(
            x=x_final,
            y=y_final,
            z=z_final,
            mode='lines',
            line=dict(
                color=color,
                width=2,
                dash='dot'  # Dotted line for hyperbolic orbits
            ),
            name=f"{obj_name} orbit",
            hovertemplate=hover_text + '<extra></extra>',
            showlegend=True
        ))
        
        # Add perihelion marker
        fig.add_trace(go.Scatter3d(
            x=[x_final[len(x_final)//2]],  # Middle point (closest to perihelion)
            y=[y_final[len(y_final)//2]],
            z=[z_final[len(z_final)//2]],
            mode='markers',
            marker=dict(
                size=6,
                color='red',
                symbol='diamond'
            ),
            name=f"{obj_name} perihelion",
            hovertemplate=f"{obj_name} Perihelion<br>Distance: {q:.3f} AU<extra></extra>",
            showlegend=False
        ))
        
        print(f"Successfully plotted hyperbolic orbit for {obj_name}: e={e:.2f}, q={q:.3f} AU")
        return True
        
    except Exception as e:
        print(f"Error plotting hyperbolic orbit for {obj_name}: {str(e)}")
        return False

# this function adjusts the orbital elements for phobos and deimos based on perturbations
def calculate_mars_satellite_elements(date, satellite_name):
    """
    Calculate time-varying orbital elements for Mars satellites
    Similar to your Moon implementation but with Mars-specific perturbations
    """
    # Calculate days since revision date of ephemeris for Phobos and Deimos
    base_epoch = datetime(2025, 6, 2, 0, 0, 0)

    # Calculate days since the base epoch (NOT J2000!)
    d = (date - base_epoch).days
    
    # Base elements
    if satellite_name == 'Phobos':
        a_base = 0.000062682  # AU
        e_base = 0.0151
        i_base = 1.082
        omega_base = 216.3
        Omega_base = 169.2
        
        # Mars J2-induced precession rates (much faster than Moon)
        omega_rate = 27.0 / 365.25  # degrees/day (apsidal precession)
        Omega_rate = -158.0 / 365.25  # degrees/day (node regression)
        
        # Tidal acceleration (Phobos spiraling inward)
        # Semi-major axis decreases by ~1.8 cm/year
        a_secular = -1.8e-5 / 149597870.7 / 365.25 * d  # AU change
        
    elif satellite_name == 'Deimos':
        a_base = 0.0001568
        e_base = 0.00033
        i_base = 1.791
        omega_base = 0.0
        Omega_base = 54.4
        
        # Slower precession rates for more distant Deimos
        omega_rate = 0.84 / 365.25  # degrees/day
        Omega_rate = -7.6 / 365.25  # degrees/day
        
        # Minimal tidal effects
        a_secular = 0
    
    # Apply secular changes
    omega = (omega_base + omega_rate * d) % 360.0
    Omega = (Omega_base + Omega_rate * d) % 360.0
    a = a_base + a_secular
    
    # Could add periodic perturbations like you do for Moon
    # Solar perturbations, Mars librations, etc.
    
    return {
        'a': a,
        'e': e_base,  # Could add eccentricity variations
        'i': i_base,  # Could add inclination oscillations
        'omega': omega,
        'Omega': Omega
    }
    
def test_mars_rotations(satellite_name, planetary_params, color, fig=None):     # test function only
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

def plot_mars_satellite_orbit(satellite_name, planetary_params, color, fig=None):       # test function only
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

def test_uranus_equatorial_transformations(satellite_name, planetary_params, color, fig=None):
    """Test transformations assuming orbital elements are in Uranus's equatorial plane"""
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
        
        # Standard orbital element rotation sequence - this gives us the orbit in Uranus's equatorial plane
        x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, Omega_rad, 'z')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, omega_rad, 'z')
        
        # Now transform from Uranus's equatorial frame to ecliptic frame
        # Get Uranus's pole orientation
        uranus_pole = planet_poles['Uranus']
        ra_pole = np.radians(uranus_pole['ra'])
        dec_pole = np.radians(uranus_pole['dec'])
        
        # Calculate pole vector
        sin_dec = np.sin(dec_pole)
        cos_dec = np.cos(dec_pole)
        sin_ra = np.sin(ra_pole)
        cos_ra = np.cos(ra_pole)
        
        # Pole vector
        x_pole = cos_dec * cos_ra
        y_pole = cos_dec * sin_ra
        z_pole = sin_dec
        
        # Normalize the pole vector
        pole_norm = np.sqrt(x_pole**2 + y_pole**2 + z_pole**2)
        x_pole /= pole_norm
        y_pole /= pole_norm
        z_pole /= pole_norm
        
        print(f"Uranus pole vector: [{x_pole:.4f}, {y_pole:.4f}, {z_pole:.4f}]")
        
        # Transform from equatorial to ecliptic
        # Step 1: First rotation to get the pole's projection onto the XY plane aligned with the X-axis
        phi = np.arctan2(y_pole, x_pole)
        x_rot1, y_rot1, z_rot1 = rotate_points(x_temp, y_temp, z_temp, -phi, 'z')  # Note the negative sign
        
        # Step 2: Second rotation to align the pole with the Z-axis
        theta = np.arccos(z_pole)
        x_rot2, y_rot2, z_rot2 = rotate_points(x_rot1, y_rot1, z_rot1, -theta, 'y')  # Note the negative sign
        
        # Step 3: Third rotation to fix the orientation
        x_final, y_final, z_final = rotate_points(x_rot2, y_rot2, z_rot2, phi, 'z')
        
        # Add trace to figure
        fig.add_trace(
            go.Scatter3d(
                x=x_final,
                y=y_final,
                z=z_final,
                mode='lines',
                line=dict(dash='solid', width=2, color=color),
                name=f"{satellite_name} Equatorial Transform",
                text=[f"{satellite_name} Equatorial Transform"] * len(x_final),
                customdata=[f"{satellite_name} Equatorial Transform"] * len(x_final),
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
        
        return fig
        
    except Exception as e:
        print(f"Error in test_uranus_equatorial_transformations: {e}")
        traceback.print_exc()
        return fig

def test_uranus_rotation_combinations(satellite_name, planetary_params, color, fig=None):
    """Test multiple rotation combinations for Uranus satellites systematically"""
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
        
        # Styles for different combinations
        styles = ["solid", "dash", "dot", "dashdot", "longdash", "longdashdot"]
        
        # Uranus's axial tilt value
        tilt = planet_tilts['Uranus']  # 97.77 degrees
        tilt_rad = np.radians(tilt)
        neg_tilt_rad = np.radians(-tilt)
        
        # Test combinations
        combinations = [
            {"name": "X+", "axis": 'x', "angle": tilt_rad},
            {"name": "X-", "axis": 'x', "angle": neg_tilt_rad},
            {"name": "Y+", "axis": 'y', "angle": tilt_rad},
            {"name": "Y-", "axis": 'y', "angle": neg_tilt_rad},
            {"name": "Z+", "axis": 'z', "angle": tilt_rad},
            {"name": "Z-", "axis": 'z', "angle": neg_tilt_rad},
            # Try some composite rotations
            {"name": "X+Y+", "rotations": [
                {"axis": 'x', "angle": tilt_rad},
                {"axis": 'y', "angle": tilt_rad}
            ]},
            {"name": "X+Z+", "rotations": [
                {"axis": 'x', "angle": tilt_rad},
                {"axis": 'z', "angle": tilt_rad}
            ]},
            {"name": "90X", "axis": 'x', "angle": np.radians(90)},
            {"name": "90Y", "axis": 'y', "angle": np.radians(90)}
        ]
        
        # Plot each combination
        for idx, combo in enumerate(combinations):
            x_rotated, y_rotated, z_rotated = x_temp.copy(), y_temp.copy(), z_temp.copy()
            
            if "rotations" in combo:
                # Apply multiple rotations in sequence
                for rot in combo["rotations"]:
                    x_rotated, y_rotated, z_rotated = rotate_points(
                        x_rotated, y_rotated, z_rotated, 
                        rot["angle"], rot["axis"]
                    )
            else:
                # Apply single rotation
                x_rotated, y_rotated, z_rotated = rotate_points(
                    x_rotated, y_rotated, z_rotated, 
                    combo["angle"], combo["axis"]
                )
            
            # Add trace to figure
            style = styles[idx % len(styles)]
            
            fig.add_trace(
                go.Scatter3d(
                    x=x_rotated,
                    y=y_rotated,
                    z=z_rotated,
                    mode='lines',
                    line=dict(dash=style, width=1, color=color),
                    name=f"{satellite_name} {combo['name']}",
                    text=[f"{satellite_name} {combo['name']}"] * len(x_rotated),
                    customdata=[f"{satellite_name} {combo['name']}"] * len(x_rotated),
                    hovertemplate='%{text}<extra></extra>',
                    showlegend=True
                )
            )
        
        return fig
        
    except Exception as e:
        print(f"Error in test_uranus_rotation_combinations: {e}")
        traceback.print_exc()
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

def debug_mars_moons(satellites_data, parent_planets):          # test function only
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

def compare_transformation_methods(fig, satellites_data, parent_planets):       # test function only
    """Plot orbits with different transformation methods for comparison"""
    
    # Plot Mars moons with all transformation methods
    for moon in parent_planets.get('Mars', []):
        if moon in satellites_data:
            for method in ["none", "simple", "complex"]:
                plot_satellite_orbit(
                    moon, 
                    satellites_data[moon],
                    'Mars',
                    color_map('Mars'),  # Call the function with planet name
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
                    color_map('Jupiter'),  # Changed brackets [] to parentheses ()
                    fig,
                    debug=True,
                    transform_method=method
                )
    
    return fig

def test_mars_negative_tilt(fig, satellites_data):          # test function only
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

def plot_satellite_orbit(satellite_name, planetary_params, parent_planet, color, fig=None, 
                         date=None, days_to_plot=None, current_position=None):
    """
    Plot the idealized orbit of a satellite around its parent planet.
    
    Parameters:
        satellite_name (str): Name of the satellite
        planetary_params (dict): Dictionary containing orbital parameters for all objects
        parent_planet (str): Name of the parent planet
        color (str): Color to use for the orbit line
        fig (plotly.graph_objects.Figure): Existing figure to add the orbit to
        date (datetime): Date for the calculation
        days_to_plot (float): Number of days to plot
        current_position (dict): Current position with 'x', 'y', 'z' keys
        
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
        
        # Calculate angular range based on days_to_plot
        if days_to_plot is not None and days_to_plot > 0:
            # Get the satellite's orbital period
            if 'orbital_period_days' in orbital_params:
                period_days = orbital_params['orbital_period_days']
            else:
                # Use KNOWN_ORBITAL_PERIODS from constants_new.py
                from constants_new import KNOWN_ORBITAL_PERIODS
                
                if satellite_name in KNOWN_ORBITAL_PERIODS:
                    period_value = KNOWN_ORBITAL_PERIODS[satellite_name]

                    if period_value is None:
                        # Handle hyperbolic/parabolic objects - use Kepler's law
                        period_days = 365.25 * np.sqrt(abs(a)**3) if a else 365.25

                    else:
                        # Already in days
                        period_days = period_value
                else:
                    # Fallback for unknown satellites
                    print(f"  Warning: No known period for {satellite_name}, using default")
                    period_days = 10  # Default fallback
            
            orbital_fraction = days_to_plot / period_days
            max_angle = 2 * np.pi * orbital_fraction
            
            # Generate orbit points only for the requested time range
            num_points = max(30, int(360 * min(orbital_fraction, 1.0)))  # At least 30 points
            theta = np.linspace(0, max_angle, num_points)
            print(f"  Plotting {days_to_plot} days = {orbital_fraction:.2f} orbits (period: {period_days:.3f} days)")
        else:
            # Full orbit
            theta = np.linspace(0, 2*np.pi, 360)  # 360 points for smoothness

        # Generate ellipse in orbital plane
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
        
        # Transformation from a planet's equatorial frame to ecliptic frame:
        # 
        # This solution follows an important pattern we discovered across multiple planetary systems:
        # - For Mars satellites: Y-axis rotation of 25.19° (Mars's axial tilt) aligns orbits properly
        # - For Uranus satellites: Matching X and Y rotations of 97.77° (Uranus's axial tilt) creates proper alignment
        #
        # General principle: When satellite orbital elements are defined in a planet's equatorial reference frame
        # (as documented by JPL), the transformation to the ecliptic frame must incorporate the planet's axial tilt
        # in a manner that reflects the planet's specific orientation in space.
        #
        # For planets with moderate axial tilts (Mars), a single rotation may suffice.
        # For planets with extreme axial tilts (Uranus), compound rotations around multiple axes are required.
        #
        # This transformation correctly maps from the satellite's native reference frame (the planet's equator)
        # to the ecliptic reference frame used in our visualization.

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

            # Transform from Mars equatorial to ecliptic coordinates
            # Using Mars' axial tilt. Note: A small (~10-20°) offset remains
            # between ideal and actual orbits, likely due to JPL's specific
            # convention for defining the ascending node reference.

            #Different reference conventions: JPL might use a slightly different convention for defining the ascending node that 
            # we haven't identified         
            # Small systematic errors: The ~10-20° offset might be inherent to how the orbital elements are defined
            # Time-dependent effects: Small variations in Mars' orientation that aren't captured in a static transformation

            # Your time-varying elements are working correctly:
            # Ω change: -157.9° per year (matches expected -158°)
            # ω change: 27.0° per year (matches expected +27°)
            #This confirms the precession calculations are accurate.

            if date is not None:
                # Override static orbital elements with time-varying ones
                orbital_params = calculate_mars_satellite_elements(date, satellite_name)
                print(f"Using time-varying elements for {satellite_name} at {date}")
                
                # Re-extract the updated orbital elements
                a = orbital_params.get('a', 0)
                e = orbital_params.get('e', 0)
                i = orbital_params.get('i', 0)
                omega = orbital_params.get('omega', 0)
                Omega = orbital_params.get('Omega', 0)
                
                # Regenerate the orbit with new elements
                theta = np.linspace(0, 2*np.pi, 360)
                r = a * (1 - e**2) / (1 + e * np.cos(theta))
                
                x_orbit = r * np.cos(theta)
                y_orbit = r * np.sin(theta)
                z_orbit = np.zeros_like(theta)
                
                # Convert updated angles to radians
                i_rad = np.radians(i)
                omega_rad = np.radians(omega)
                Omega_rad = np.radians(Omega)
                
                # Apply standard orbital rotations with updated elements
                x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, Omega_rad, 'z')
                x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
                x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, omega_rad, 'z')

            # The Y-rotation of 25.19° suggests the node reference is already 
            # aligned with the ecliptic in some way. However, there's still
            # a visible offset in your plot.
            
            # Try this refined approach: -- not used because it does not resolve the discrepancy
            # 1. First apply a small Z-rotation to account for the remaining offset
    #        z_adjustment = np.radians(15)  # Tune this based on the visual offset. 
    #        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, z_adjustment, 'z')
            
            # 2. Then apply the Mars tilt

            mars_y_rotation = np.radians(25.19)
            x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, mars_y_rotation, 'y')
            print(f"Transformation applied: Mars with Y-axis rotation of 25.19°")   

    #        z_adjustment = np.radians(10)  # Shift the z adjustment after the y adjustment -- does not improve the discrepancy
    #        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, z_adjustment, 'z') 
            
        elif parent_planet == 'Jupiter':
            # Use simple tilt for Jupiter (which works well)
            if 'Jupiter' in planet_tilts:
                tilt_rad = np.radians(planet_tilts['Jupiter'])
                x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, tilt_rad, 'x')
                print(f"Transformation applied: Jupiter with tilt={planet_tilts['Jupiter']}°")
            else:
                x_final, y_final, z_final = x_temp, y_temp, z_temp
                print("No transformation applied for Jupiter (missing tilt data)")

        elif parent_planet == 'Saturn':
            if satellite_name == 'Phoebe':
                # Special transformation for Phoebe - irregular retrograde satellite
                # From JPL Horizons header: "mean values with respect to local Laplace plane"
                
                # Transform from Laplace plane to ecliptic:
                # 1. First align with Saturn's orbital plane
                saturn_orbit_inc = np.radians(2.485)  # Saturn's orbital inclination
                saturn_orbit_node = np.radians(113.665)  # Saturn's ascending node
                
                # 2. Apply a partial rotation between Saturn's equator and orbital plane
                # Phoebe is far enough that Laplace plane is tilted from equatorial plane
                laplace_tilt = np.radians(17.0)  # Increased from 15° based on residuals
                
                # 3. Additional node alignment correction
                # Based on the Y-component difference in normals, we need a Z rotation
                node_correction = np.radians(-30.0)  # Empirical adjustment
                
                # Apply transformations in sequence:
                # a) Rotate from Laplace plane toward Saturn's orbital plane
                x_rot1, y_rot1, z_rot1 = rotate_points(x_temp, y_temp, z_temp, -laplace_tilt, 'x')
                
                # b) Apply node correction to align ascending nodes
                x_rot2, y_rot2, z_rot2 = rotate_points(x_rot1, y_rot1, z_rot1, node_correction, 'z')
                
                # c) Transform to ecliptic using Saturn's orbital elements
                x_rot3, y_rot3, z_rot3 = rotate_points(x_rot2, y_rot2, z_rot2, -saturn_orbit_node, 'z')
                x_final, y_final, z_final = rotate_points(x_rot3, y_rot3, z_rot3, -saturn_orbit_inc, 'x')
                
                print(f"Transformation applied: Phoebe from Laplace plane to ecliptic (enhanced)")

            # ADD THE FOLLOWING ELSE BLOCK:
            else:
                # Apply a general transformation for all other Saturnian moons
                # This uses Saturn's axial tilt, similar to how Jupiter's moons are handled.
                if 'Saturn' in planet_tilts:
                    tilt_rad = np.radians(planet_tilts['Saturn'])
                    x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, tilt_rad, 'x')
                    print(f"Transformation applied: {satellite_name} with Saturn's tilt={planet_tilts['Saturn']}°")
                else:
                    # Fallback if tilt data is missing
                    x_final, y_final, z_final = x_temp, y_temp, z_temp

        elif parent_planet == 'Uranus':
            # Transformation from Uranus's equatorial frame to ecliptic frame:
            # 
            # The orbital elements in JPL Horizons are defined relative to Uranus's
            # equatorial plane (per JPL documentation), requiring a transformation
            # to the ecliptic reference frame used in our visualization.
            #
            # Our optimal transformation uses two sequential rotations:
            # 1. First rotation (X+): 105° rotation around the X-axis
            # 2. Second rotation (Y+): 105° rotation around the Y-axis
            #
            # This compound rotation of 105° (rather than Uranus's nominal axial tilt of 97.77°)
            # was determined through empirical testing to provide the best alignment between
            # idealized and actual satellite orbits. The 7° difference may account for:
            #   - Reference frame subtleties not captured in simple transformations
            #   - Uranus's magnetic field orientation (which is offset from its rotation axis)
            #   - The combined effect of Uranus's obliquity and orbital inclination
            #   - Possible reference epoch differences
            #
            # This solution follows a pattern we discovered across planetary systems:
            # - For Mars: Y-axis rotation of ~25° (Mars's axial tilt) aligns satellite orbits
            # - For Uranus: Matching X and Y rotations of 105° creates optimal alignment
            #
            # The need for dual-axis rotation reflects Uranus's unique 3D orientation
            # in space, where its equatorial plane is nearly perpendicular to its orbital plane.

            uranus_tilt = 105  # uranus tilt is 97.77 degrees            
            
            # First apply rotation around x-axis
            x_rot1, y_rot1, z_rot1 = rotate_points(x_temp, y_temp, z_temp, np.radians(uranus_tilt), 'x')
            
            # Then apply rotation around y-axis with the same angle
            x_final, y_final, z_final = rotate_points(x_rot1, y_rot1, z_rot1, np.radians(uranus_tilt), 'y')
            
            print(f"Transformation applied: Uranus with X and Y rotations of {uranus_tilt}°")
            
            # This transformation was determined by testing and provides the best visual alignment
            # between the ideal orbits and the actual orbits of Uranian satellites

        elif parent_planet == 'Neptune':
            if satellite_name == 'Triton':
                # Special transformation for Triton, Neptune's largest moon
                # Triton's orbital elements are defined relative to Neptune's equatorial plane
                # To transform to ecliptic coordinates, we use Neptune's pole orientation
                
                # Step 1: Rotate around z-axis by Neptune's pole Right Ascension
                # This aligns the x-axis with the line of nodes (intersection of Neptune's equator and the ecliptic)
                ra_pole = np.radians(planet_poles['Neptune']['ra'])
                x_rot1, y_rot1, z_rot1 = rotate_points(x_temp, y_temp, z_temp, ra_pole, 'z')
                
                # Step 2: Rotate around x-axis by (90° - Neptune's pole Declination)
                # This tilts the orbital plane to match Neptune's equatorial tilt relative to the ecliptic
                dec_pole = np.radians(90 - planet_poles['Neptune']['dec'])
                x_rot2, y_rot2, z_rot2 = rotate_points(x_rot1, y_rot1, z_rot1, dec_pole, 'x')
                
                # Step 3: Fine-tuning with a 3° z-axis rotation
                # This small adjustment compensates for reference frame differences between
                # Neptune's pole coordinates and Triton's orbital elements
                x_final, y_final, z_final = rotate_points(x_rot2, y_rot2, z_rot2, np.radians(3), 'z')
                
                print(f"Transformation applied: Triton with Neptune pole orientation + 3° z-axis adjustment")
            else:
                # Standard transformation for other Neptune satellites
                tilt_rad = np.radians(planet_tilts['Neptune'])
                x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, tilt_rad, 'x')

        elif parent_planet == 'Pluto':
            # Special case for Pluto's satellites
            # Apply the optimized transformation: X-Tilt->Y-Tilt->Z-105
            
            # Get Pluto's axial tilt
            pluto_tilt = planet_tilts.get('Pluto', -122.53)
            pluto_tilt_rad = np.radians(pluto_tilt)
            
            # 1. X-axis rotation by Pluto's tilt
            x_rotated, y_rotated, z_rotated = rotate_points(x_temp, y_temp, z_temp, pluto_tilt_rad, 'x')
            # 2. Y-axis rotation by Pluto's tilt
            x_rotated, y_rotated, z_rotated = rotate_points(x_rotated, y_rotated, z_rotated, pluto_tilt_rad, 'y')
            # 3. Z-axis rotation by -105 degrees
            z_angle = np.radians(-105)
            x_final, y_final, z_final = rotate_points(x_rotated, y_rotated, z_rotated, z_angle, 'z')
            
            print(f"Transformation applied: Pluto X-Tilt->Y-Tilt->Z-105")

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

        # Add markers at key points
        # Get semi-major axis in km for distance calculations        
        # Convert semi-major axis from AU to km
        a_km = a * 149597870.7  # 1 AU = 149,597,870.7 km
        
        # Find periapsis (closest approach to parent)
        periapsis_idx = np.argmin(r)
        
        # Prepare orbital parameters for apsidal markers
        orbital_params = planetary_params[satellite_name]
        
        # Add periapsis marker with proper date calculation
        add_perihelion_marker(
            fig,
            x_final[periapsis_idx],
            y_final[periapsis_idx],
            z_final[periapsis_idx],
            satellite_name,
            a,
            e,
            date if date else datetime.now(),
            current_position,
            orbital_params,
            lambda x: color,  # Simple color function
            q=r[periapsis_idx]  # Pass the periapsis distance
        )

        # Find apoapsis (farthest point from parent)
        apoapsis_idx = np.argmax(r)
        
        # Add apoapsis marker with proper date calculation
        add_apohelion_marker(
            fig,
            x_final[apoapsis_idx],
            y_final[apoapsis_idx],
            z_final[apoapsis_idx],
            satellite_name,
            a,
            e,
            date if date else datetime.now(),
            current_position,
            orbital_params,
            lambda x: color  # Simple color function
        )
        
        return fig
    
    except Exception as e:
        print(f"Error plotting {satellite_name} orbit: {e}")
        return fig

# Add this function to idealized_orbits.py

def calculate_moon_orbital_elements(date):
    """
    Calculate Moon's orbital elements for a specific date
    Using time-varying mean elements with major perturbations
    
    Parameters:
        date (datetime): Date for which to calculate elements
        
    Returns:
        dict: Dictionary containing orbital elements {a, e, i, omega, Omega}
    """
    # Calculate Julian centuries since J2000.0
    j2000 = datetime(2000, 1, 1, 12, 0, 0)  # J2000.0 epoch
    T = (date - j2000).total_seconds() / (36525.0 * 86400.0)  # Julian centuries
    
    # Mean orbital elements with secular variations
    # These values are from JPL and are relative to the ecliptic
    a = 0.002570  # AU (384,400 km) - relatively stable
    
    # Base eccentricity with secular variation
    e_base = 0.0549  # Mean eccentricity
    
    # Inclination to ecliptic (not Earth's equator!)
    i = 5.145  # degrees - mean inclination to ecliptic
    
    # Node regression (retrograde motion)
    # The Moon's node completes one cycle in about 18.6 years
    Omega = 125.08 - 0.0529538083 * (date - j2000).days  # degrees/day
    
    # Apsidal precession
    # The Moon's line of apsides completes one cycle in about 8.85 years  
    omega = 318.15 + 0.1643573223 * (date - j2000).days  # degrees/day
    
    # Calculate perturbations for more accuracy
    # Days since J2000
    d = (date - j2000).days
    
    # Mean anomalies
    M_moon = (134.963 + 13.064993 * d) % 360  # Moon's mean anomaly
    M_sun = (357.529 + 0.98560028 * d) % 360   # Sun's mean anomaly
    D = (297.850 + 12.190749 * d) % 360        # Mean elongation
    
    # Convert to radians
    M_moon_rad = np.radians(M_moon)
    M_sun_rad = np.radians(M_sun)
    D_rad = np.radians(D)
    
    # Apply perturbations to eccentricity
    # Evection (largest perturbation)
    e_evection = 0.01098 * np.cos(2*D_rad - M_moon_rad)
    e = e_base + e_evection
    
    # Ensure physical bounds
    e = max(0.026, min(e, 0.077))
    
    # Normalize angles
    omega = omega % 360.0
    Omega = Omega % 360.0
    
    return {
        'a': a,
        'e': e,
        'i': i,
        'omega': omega,
        'Omega': Omega
    }

def plot_moon_ideal_orbit(fig, date, center_object_name='Earth', color=None, days_to_plot=None, current_position=None):
    """
    Plot the Moon's idealized orbit with time-varying elements and perturbations
    
    Parameters:
        fig: Plotly figure object
        date: datetime object for the calculation epoch
        center_object_name: Name of the central body (should be 'Earth' for Moon)
        color: Color for the orbit line
        days_to_plot: Number of days to plot
        current_position: Dict with 'x', 'y', 'z' keys for current position
    """
    # Get time-varying orbital elements
    elements = calculate_moon_orbital_elements(date)
    
    # Extract elements
    a = elements['a']
    e = elements['e']
    i = elements['i']
    omega = elements['omega']
    Omega = elements['Omega']
    
    print(f"\nMoon orbital elements for {date.strftime('%Y-%m-%d')}:")
    print(f"  a = {a:.6f} AU")
    print(f"  e = {e:.4f}")
    print(f"  i = {i:.2f}°")
    print(f"  ω = {omega:.2f}°")
    print(f"  Ω = {Omega:.2f}°")
    
    # Calculate angular range based on days_to_plot
    if days_to_plot is not None and days_to_plot > 0:
        # Get Moon's orbital period from constants
        moon_period_days = KNOWN_ORBITAL_PERIODS.get('Moon', 27.321661)
        orbital_fraction = days_to_plot / moon_period_days
        max_angle = 2 * np.pi * orbital_fraction
        
    else:
        # Default to one complete orbit
        max_angle = 2 * np.pi
        orbital_fraction = 1.0
    
    # Generate the orbit points
    # Always use enough points for smooth display
    if orbital_fraction < 1:
        num_points = max(180, int(360 * orbital_fraction))  # At least 180 points
    else:
        # For multiple orbits, ensure at least 360 points per orbit
        num_points = int(360 * max(1, orbital_fraction))
        # Cap at a reasonable maximum to avoid performance issues
        num_points = min(num_points, 7200)  # Max ~20 points per degree for 360 degrees
    
    theta = np.linspace(0, max_angle, num_points)
    
    # Calculate radius for each point
    r = a * (1 - e**2) / (1 + e * np.cos(theta))
    
    # Convert to Cartesian coordinates in orbital plane
    x_orbit = r * np.cos(theta)
    y_orbit = r * np.sin(theta)
    z_orbit = np.zeros_like(theta)
    
    # Apply orbital element rotations - matching the standard sequence
    # Convert angles to radians
    i_rad = np.radians(i)
    omega_rad = np.radians(omega)
    Omega_rad = np.radians(Omega)
    
    # Use the same rotation sequence as in the main orbit plotting
    # 1. Rotate by argument of periapsis (ω) around z-axis
    x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, omega_rad, 'z')
    # 2. Rotate by inclination (i) around x-axis
    x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
    # 3. Rotate by longitude of ascending node (Ω) around z-axis
    x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, Omega_rad, 'z')
    
    # Create hover text with date information
    date_str = date.strftime('%Y-%m-%d %H:%M UTC')
    hover_text = f"Moon Ideal Orbit<br>Date: {date_str}<br>e: {e:.4f}<br>i: {i:.2f}°"
    
    # Use default Moon color if not specified
    if color is None:
        from constants_new import color_map
        color = color_map('Moon')
    
    # Add trace to figure
    fig.add_trace(
        go.Scatter3d(
            x=x_final,
            y=y_final,
            z=z_final,
            mode='lines',
            line=dict(dash='dot', width=2, color=color),
            name="Moon Ideal Orbit",
            text=[hover_text] * len(x_final),
            customdata=[hover_text] * len(x_final),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    )
    
    # Add markers at key points
    # Perigee (closest approach)
    perigee_idx = np.argmin(np.sqrt(x_final**2 + y_final**2 + z_final**2))
    
    # Prepare orbital parameters for apsidal markers
    orbital_params = {
        'a': a,
        'e': e,
        'i': i,
        'omega': omega,
        'Omega': Omega
    }
    
    # Debug print to verify position
    if current_position:
        print(f"Moon current position: x={current_position['x']:.6f}, y={current_position['y']:.6f}, z={current_position['z']:.6f} AU")
    else:
        print("Warning: No current position for Moon")

    # Add perigee marker with proper date calculation
    add_perihelion_marker(
        fig,
        x_final[perigee_idx],
        y_final[perigee_idx],
        z_final[perigee_idx],
        'Moon',  # obj_name
        a,
        e,
        date,
        current_position,
        orbital_params,
        color_map if color is None else lambda x: color,  # Use provided color or color_map
        q=r[perigee_idx]  # Pass the perigee distance
    )

    """
    fig.add_trace(
        go.Scatter3d(
            x=[x_final[perigee_idx]],
            y=[y_final[perigee_idx]],
            z=[z_final[perigee_idx]],
            mode='markers',
            marker=dict(
                size=5,
                color=color,
                symbol='square-open'
            ),
            name=f"Moon Perigee",
            text=[f"Moon Perigee<br>Date: {date.strftime('%Y-%m-%d %H:%M UTC')}<br>Distance: {r[perigee_idx]:.6f} AU"],
            customdata=[f"Moon Perigee"],
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    )
    """
    
    # Apogee (farthest approach)
    apogee_idx = np.argmax(np.sqrt(x_final**2 + y_final**2 + z_final**2))
    
    # Add apogee marker with proper date calculation
    add_apohelion_marker(
        fig,
        x_final[apogee_idx],
        y_final[apogee_idx],
        z_final[apogee_idx],
        'Moon',  # obj_name
        a,
        e,
        date,
        current_position,
        orbital_params,
        color_map if color is None else lambda x: color  # Use provided color or color_map
    )

    print(f"  Generated {num_points} points for {orbital_fraction:.1f} orbits")

    return fig

def generate_hyperbolic_orbit_points(a, e, i, omega, Omega, rotate_points, max_distance=100):
    """
    Generate points for a hyperbolic orbit trajectory.
    Enhanced to handle very high eccentricity cases.
    
    Parameters:
        a: Semi-major axis (negative for hyperbolic orbits)
        e: Eccentricity (> 1 for hyperbolic orbits)
        i: Inclination in degrees
        omega: Argument of perihelion in degrees
        Omega: Longitude of ascending node in degrees
        rotate_points: Function to rotate points
        max_distance: Maximum distance from Sun to plot (AU)
    
    Returns:
        tuple: (x_final, y_final, z_final, q) where q is perihelion distance
    """
    # Calculate perihelion distance
    q = abs(a) * (e - 1)
    
    # For hyperbolic orbits, the true anomaly range is limited
    theta_inf = np.arccos(-1/e)  # Asymptotic true anomaly
    
    # For very high eccentricity, we need special handling
    if e > 5:
        # High eccentricity: focus on the visible region
        # Calculate the true anomaly where r = max_distance
        # r = a(e^2 - 1) / (1 + e*cos(theta))
        # Solving for theta: cos(theta) = (a(e^2 - 1)/r - 1) / e
        
        cos_theta_max = ((abs(a) * (e**2 - 1) / max_distance) - 1) / e
        
        if cos_theta_max >= -1 and cos_theta_max <= 1:
            theta_visible = np.arccos(cos_theta_max)
            # Use the smaller angle
            theta_limit = min(theta_inf - 0.01, theta_visible)
        else:
            # Very extreme case - just show near perihelion
            theta_limit = min(theta_inf - 0.01, np.pi/4)  # Max 45 degrees
        
        # Use more points for smoother curve
        num_points = 1000
    else:
        # Standard approach for moderate eccentricity
        theta_limit = theta_inf - 0.1  # Use 0.1 radian margin
        num_points = 500
    
    # Create array of true anomaly values
    theta = np.linspace(-theta_limit, theta_limit, num_points)
    
    # Calculate radius for each true anomaly
    r = abs(a) * (e**2 - 1) / (1 + e * np.cos(theta))
    
    # Filter out points that are too far from the Sun
    valid_mask = (r > 0) & (r <= max_distance)
    
    # Check if we have enough valid points
    if np.sum(valid_mask) < 50:
        # If too few points, focus on perihelion region
        if e > 10:
            # For extremely high eccentricity, use very small angle range
            theta_perihelion = np.linspace(-0.05, 0.05, 200)  # ±2.9 degrees
        else:
            # For high eccentricity, use small angle range
            theta_perihelion = np.linspace(-np.pi/6, np.pi/6, 500)  # ±30 degrees
        
        r_perihelion = abs(a) * (e**2 - 1) / (1 + e * np.cos(theta_perihelion))
        valid_perihelion = (r_perihelion > 0) & (r_perihelion <= max_distance * 1.5)
        
        if np.sum(valid_perihelion) > 10:
            theta = theta_perihelion[valid_perihelion]
            r = r_perihelion[valid_perihelion]
        else:
            # Last resort: just create a small arc at perihelion
            print(f"Warning: Extremely high eccentricity (e={e:.2f}), showing minimal trajectory")
            theta = np.linspace(-0.01, 0.01, 20)
            r = abs(a) * (e**2 - 1) / (1 + e * np.cos(theta))
    else:
        theta = theta[valid_mask]
        r = r[valid_mask]
    
    # Convert to Cartesian coordinates in orbital plane
    x_orbit = r * np.cos(theta)
    y_orbit = r * np.sin(theta)
    z_orbit = np.zeros_like(theta)
    
    # Convert angles to radians
    i_rad = np.radians(i)
    omega_rad = np.radians(omega)
    Omega_rad = np.radians(Omega)
    
    # Apply orbital element rotations
    x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, omega_rad, 'z')
    x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
    x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, Omega_rad, 'z')
    
    return x_final, y_final, z_final, q

def plot_idealized_orbits(fig, objects_to_plot, center_id='Sun', objects=None, 
                          planetary_params=None, parent_planets=None, color_map=None, 
                          date=None, days_to_plot=None, current_positions=None, fetch_position=None):
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
        date (datetime): Date for time-varying orbital elements (used for Moon)
        
    Returns:
        plotly.graph_objects.Figure: Figure with idealized orbits added
    """
    # Create name to object mapping
    obj_dict = {obj['name']: obj for obj in objects} if objects else {}

    # If current_positions not provided, try to extract from objects parameter
    if current_positions is None and objects is not None:
        current_positions = {}
        for obj in objects:
            if hasattr(obj, 'name') and hasattr(obj, 'x') and hasattr(obj, 'y') and hasattr(obj, 'z'):
                current_positions[obj.name] = {
                    'x': obj.x,
                    'y': obj.y, 
                    'z': obj.z
                }

    # Track skipped objects by category
    skipped = {
        'satellites': [],
        'comets': [],
        'missions': [],
        'no_params': [],
        'invalid_orbit': []
    }

    plotted = []

    # If days_to_plot not provided, try to get from GUI
    if days_to_plot is None:
#        try:
#            days_to_plot = int(days_to_plot_entry.get())
#        except:
        days_to_plot = 365  # Default fallback

    # Add date parameter default
    if date is None:
        from datetime import datetime
        date = datetime.now()

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
        from constants_new import color_map       

    # In the section where we plot satellites of the center object:
    if center_id != 'Sun':
        # Get list of moons for this center
        moons = parent_planets.get(center_id, [])
        
        # Filter objects_to_plot to only include moons of this center
        objects_to_plot = [obj for obj in objects_to_plot if obj in moons]
        
        # For each satellite of the center object
        for moon_name in objects_to_plot:
            # Find the object in the objects list
            moon_info = next((obj for obj in objects if obj['name'] == moon_name), None)
            if moon_info is None:
                continue
            
            # Special handling for Earth's Moon with time-varying elements
            if moon_name == 'Moon' and center_id == 'Earth':
                # Get Moon's current position from current_positions
                moon_current_pos = current_positions.get('Moon') if current_positions else None

                fig = plot_moon_ideal_orbit(fig, date, center_id, color_map(moon_name), days_to_plot,
                                            current_position=moon_current_pos)
            else:
                # Use the standard satellite plotting function for other moons
                # Get satellite's current position
                satellite_current_pos = current_positions.get(moon_name) if current_positions else None

                fig = plot_satellite_orbit(
                    moon_name, 
                    planetary_params,
                    center_id, 
                    color_map(moon_name), 
                    fig,
                    date=date,
                    days_to_plot=days_to_plot,
                    current_position=satellite_current_pos
                )
            
            plotted.append(moon_name)
    
    # If center is the Sun, plot orbits for selected heliocentric objects
    else:
        for obj_name in objects_to_plot:
            # Find the object in the objects list
            obj_info = next((obj for obj in objects if obj['name'] == obj_name), None)
            # Get current position for this object
            current_pos = current_positions.get(obj_name) if current_positions else None
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
    #        if a < 0.0001:
    #           continue

            e = params.get('e', 0)
            i = params.get('i', 0)
            omega = params.get('omega', 0)
            Omega = params.get('Omega', 0)

            # Add this debug line
            print(f"\n[DEBUG] Processing {obj_name}")
            print(f"[DEBUG] params keys: {params.keys()}")            

# Check if this is a hyperbolic orbit (e > 1)
            if e > 1:
                try:
                    x_final, y_final, z_final, q = generate_hyperbolic_orbit_points(a, e, i, omega, Omega, rotate_points)
                    
                    epoch_str = ""
                    if 'epoch' in params:
                        epoch_str = f" (Epoch: {params['epoch']})"

                    fig.add_trace(
                        go.Scatter3d(
                            x=x_final,
                            y=y_final,
                            z=z_final,
                            mode='lines',
                            line=dict(dash='dot', width=1, color=color_map(obj_name)),
                            name=f"{obj_name} Ideal Orbit{epoch_str}",
                            text=[f"{obj_name} Hyperbolic Orbit<br>eccentricity, e={e:.5f}<br>periapsis distance, q={q:.5f} AU"] * len(x_final),
                            customdata=[f"{obj_name} Ideal Orbit"] * len(x_final),
                            hovertemplate='%{text}<extra></extra>',
                            showlegend=True                    
                        )
                    )
                    
                    # Calculate perihelion position explicitly at theta=0
                    r_perihelion = abs(a) * (e**2 - 1) / (1 + e)  # At theta=0, cos(0)=1
                    x_peri = r_perihelion
                    y_peri = 0.0
                    z_peri = 0.0
                    
                    # Convert angles to radians for rotation
                    i_rad = np.radians(i)
                    omega_rad = np.radians(omega)
                    Omega_rad = np.radians(Omega)
                    
                    # Apply the same rotations as the orbit
                    x_temp, y_temp, z_temp = rotate_points([x_peri], [y_peri], [z_peri], omega_rad, 'z')
                    x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
                    x_peri_final, y_peri_final, z_peri_final = rotate_points(x_temp, y_temp, z_temp, Omega_rad, 'z')

                    # NEW CODE - Use the apsidal_markers module:
                    # Get current position for this object
                    current_pos = current_positions.get(obj_name) if current_positions else None
                    
                    # Add perihelion marker with proper date calculation
                    add_perihelion_marker(
                        fig, 
                        x_peri_final[0],  # Note: x_peri_final is a list, so we take [0]
                        y_peri_final[0],  # Same for y
                        z_peri_final[0],  # Same for z
                        obj_name, 
                        a, 
                        e, 
                        date, 
                        current_pos,
                        params,  # Pass the full params dict
                        color_map, 
                        q=q  # Pass the perihelion distance we already calculated
                    )

                    plotted.append(obj_name)

                    print(f"Plotted hyperbolic orbit for {obj_name}: e={e:.5f}, q={q:.5f} AU")
                    
                except Exception as err:
                    print(f"Error plotting hyperbolic orbit for {obj_name}: {err}")
                    skipped['error'].append(obj_name)
                
                continue  # Skip to next object, don't run elliptical orbit code
            
            # For elliptical orbits (e <= 1), continue with existing code:
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

            # ADD THIS CODE to check for epoch
            epoch_str = ""
            if 'epoch' in params:
                epoch_str = f" (Epoch: {params['epoch']})"

            fig.add_trace(
                go.Scatter3d(
                    x=x_final,
                    y=y_final,
                    z=z_final,
                    mode='lines',
                    line=dict(dash='dot', width=1, color=color_map(obj_name)),
                    name=f"{obj_name} Ideal Orbit{epoch_str}",  # MODIFIED LINE - added {epoch_str}
                    text=[f"{obj_name} Ideal Orbit"] * len(x_final),
                    customdata=[f"{obj_name} Ideal Orbit"] * len(x_final),
                    hovertemplate='%{text}<extra></extra>',
                    showlegend=True                    
                )
            )

            perihelion_idx = np.argmin(np.abs(theta))  # Index closest to theta=0

            # NEW CODE - Use the apsidal_markers module:
            # Get current position for this object
            current_pos = current_positions.get(obj_name) if current_positions else None
            
            # Add perihelion marker with proper date calculation
            add_perihelion_marker(
                fig,
                x_final[perihelion_idx],   # x coordinate at perihelion
                y_final[perihelion_idx],   # y coordinate at perihelion
                z_final[perihelion_idx],   # z coordinate at perihelion
                obj_name, 
                a, 
                e, 
                date, 
                current_pos,              # Current position of the object
                params,                   # Full orbital parameters
                color_map                 # Color mapping function
            )

            # Apohelion (farthest point from Sun)
            apohelion_idx = np.argmin(np.abs(theta - np.pi))  # Index closest to theta=π
            
            # NEW CODE - Use the apsidal_markers module:
            # Add apohelion marker with proper date calculation
            add_apohelion_marker(
                fig,
                x_final[apohelion_idx],    # x coordinate at apohelion
                y_final[apohelion_idx],    # y coordinate at apohelion
                z_final[apohelion_idx],    # z coordinate at apohelion
                obj_name,
                a,
                e,
                date,
                current_pos,               # Current position of the object
                params,                    # Full orbital parameters
                color_map                  # Color mapping function
            )

            # ADD THE ACTUAL APSIDAL MARKERS CODE HERE (moved from hyperbolic section)
            # After adding ideal markers, add actual apsidal markers if dates are provided
            if 'perihelion_dates' in params or 'aphelion_dates' in params:
                print(f"\n[DEBUG] Found apsidal dates for {obj_name}")
                print(f"  Perihelion dates: {params.get('perihelion_dates', [])}")
                print(f"  Aphelion dates: {params.get('aphelion_dates', [])}")
                
                # Get the object ID for fetching positions
                obj_id = None
                id_type = None
                for obj in objects:
                    if obj['name'] == obj_name:
                        obj_id = obj['id']
                        id_type = obj.get('id_type', None)
                        break
                
                if obj_id:
                    # Import the functions we need
                    from apsidal_markers import fetch_positions_for_apsidal_dates, add_actual_apsidal_markers

                    # Use the passed fetch_position
                    if fetch_position is None:
                        print("ERROR: fetch_position not provided to plot_idealized_orbits")
                        continue

                    # Fetch positions for the apsidal dates
                    positions_dict = fetch_positions_for_apsidal_dates(
                        obj_id=obj_id,
                        params=params,
                        date_range=(date - timedelta(days=365), date + timedelta(days=365)),
                        center_id=center_id,
                        id_type=id_type,
                        is_satellite=(obj_name in parent_planets.get(center_id, [])),
                        fetch_position=fetch_position
                    )
                    
                    print(f"  Fetched positions: {len(positions_dict)} dates")
                    
                    # Add the actual markers
                    add_actual_apsidal_markers(
                        fig=fig,
                        obj_name=obj_name,
                        params=params,
                        date_range=(date - timedelta(days=365), date + timedelta(days=365)),
                        positions_dict=positions_dict,
                        color_map=color_map,
                        center_body=center_id,
                        is_satellite=(obj_name in parent_planets.get(center_id, []))
                    )
                    print(f"  Added actual apsidal markers for {obj_name}")

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

def test_triton_rotations(satellite_name, planetary_params, color, fig=None):
    """Test multiple rotation combinations for Triton's orbit"""
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
        
        # Neptune's axial tilt is 28.32 degrees
        neptune_tilt = 28.32
        
        # Test combinations
        combinations = [
            {"name": "Standard", "rotations": []},
            {"name": "X+", "rotations": [{"axis": 'x', "angle": np.radians(neptune_tilt)}]},
            {"name": "X-", "rotations": [{"axis": 'x', "angle": np.radians(-neptune_tilt)}]},
            {"name": "Y+", "rotations": [{"axis": 'y', "angle": np.radians(neptune_tilt)}]},
            {"name": "Y-", "rotations": [{"axis": 'y', "angle": np.radians(-neptune_tilt)}]},
            {"name": "Z+", "rotations": [{"axis": 'z', "angle": np.radians(neptune_tilt)}]},
            {"name": "Z-", "rotations": [{"axis": 'z', "angle": np.radians(-neptune_tilt)}]},
            
            # Compound rotations like what worked for Uranus
            {"name": "X+Y+", "rotations": [
                {"axis": 'x', "angle": np.radians(neptune_tilt)}, 
                {"axis": 'y', "angle": np.radians(neptune_tilt)}
            ]},
            {"name": "X+Y-", "rotations": [
                {"axis": 'x', "angle": np.radians(neptune_tilt)}, 
                {"axis": 'y', "angle": np.radians(-neptune_tilt)}
            ]},
            {"name": "X-Y+", "rotations": [
                {"axis": 'x', "angle": np.radians(-neptune_tilt)}, 
                {"axis": 'y', "angle": np.radians(neptune_tilt)}
            ]},
            {"name": "X-Y-", "rotations": [
                {"axis": 'x', "angle": np.radians(-neptune_tilt)}, 
                {"axis": 'y', "angle": np.radians(-neptune_tilt)}
            ]},
            
            # Try 90-degree rotations
            {"name": "X+90", "rotations": [{"axis": 'x', "angle": np.radians(90)}]},
            {"name": "Y+90", "rotations": [{"axis": 'y', "angle": np.radians(90)}]},
            {"name": "Z+90", "rotations": [{"axis": 'z', "angle": np.radians(90)}]},
            
            # Compound rotations with 90 degrees
            {"name": "X+90_Y+", "rotations": [
                {"axis": 'x', "angle": np.radians(90)}, 
                {"axis": 'y', "angle": np.radians(neptune_tilt)}
            ]},
            {"name": "X+_Y+90", "rotations": [
                {"axis": 'x', "angle": np.radians(neptune_tilt)}, 
                {"axis": 'y', "angle": np.radians(90)}
            ]},
            
            # Try a different approach with pole-based transformation using Neptune's pole
            {"name": "Neptune Pole", "rotations": [
                {"axis": 'z', "angle": np.radians(planet_poles['Neptune']['ra'])},
                {"axis": 'x', "angle": np.radians(90 - planet_poles['Neptune']['dec'])}
            ]},

            # Add these to your combinations list
            {"name": "Retrograde", "rotations": [
                {"axis": 'z', "angle": np.radians(planet_poles['Neptune']['ra'])},
                {"axis": 'x', "angle": np.radians(90 - planet_poles['Neptune']['dec'])},
                {"axis": 'z', "angle": np.radians(180)}
            ]},
            {"name": "Complex", "rotations": [
                {"axis": 'z', "angle": np.radians(planet_poles['Neptune']['ra'])},
                {"axis": 'y', "angle": np.radians(90 - planet_poles['Neptune']['dec'])},
                {"axis": 'x', "angle": np.radians(30)}
            ]}

        ]
        
        # Define line styles and colors for each rotation
        styles = ["solid", "dash", "dot", "dashdot", "longdash", "longdashdot"]
        
        # Apply each rotation combination
        for idx, combo in enumerate(combinations):
            x_rotated, y_rotated, z_rotated = x_temp.copy(), y_temp.copy(), z_temp.copy()
            
            for rot in combo["rotations"]:
                x_rotated, y_rotated, z_rotated = rotate_points(
                    x_rotated, y_rotated, z_rotated, 
                    rot["angle"], rot["axis"]
                )
            
            # Add trace with unique style
            style = styles[idx % len(styles)]
            
            fig.add_trace(
                go.Scatter3d(
                    x=x_rotated,
                    y=y_rotated,
                    z=z_rotated,
                    mode='lines',
                    line=dict(dash=style, width=1, color=color),
                    name=f"{satellite_name} {combo['name']}",
                    text=[f"{satellite_name} {combo['name']}"] * len(x_rotated),
                    customdata=[f"{satellite_name} {combo['name']}"] * len(x_rotated),
                    hovertemplate='%{text}<extra></extra>',
                    showlegend=True
                )
            )
        
        return fig
        
    except Exception as e:
        print(f"Error in test_triton_rotations: {e}")
        traceback.print_exc()  # This will print the full stack trace for better debugging
        return fig
    
def test_pluto_moon_rotations(satellite_name, planetary_params, color, fig=None):
#def test_pluto_moon_xyz_rotations(satellite_name, planetary_params, color, fig=None):
    """
    Fine-tuned testing of XYZ rotation combinations for Pluto's moons.
    This function focuses on variations of X, Y, and Z rotations with different angles.
    
    Parameters:
        satellite_name (str): Name of the satellite (Charon, Styx, Nix, Kerberos or Hydra)
        planetary_params (dict): Dictionary containing orbital parameters
        color (str): Color to use for the orbit lines
        fig (plotly.graph_objects.Figure): Existing figure to add the orbit to
        
    Returns:
        plotly.graph_objects.Figure: Figure with various test orbits added
    """
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
        
        print(f"Testing fine-tuned XYZ rotations for {satellite_name} orbit around Pluto")
        print(f"Orbital elements: a={a}, e={e}, i={i}°, ω={omega}°, Ω={Omega}°")
        
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
        
        # Pluto's axial tilt value
        pluto_tilt = planet_tilts.get('Pluto', -122.53)
        pluto_tilt_rad = np.radians(pluto_tilt)
        
        # Create a list of angles to test
        # We'll focus on different angles around Pluto's tilt and other relevant values
        # Using a mix of fixed angles and variations of Pluto's tilt
        x_angles = [-180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180]
        y_angles = [-180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180]
        z_angles = [-180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180]
        
        # Define specific combinations to test
        combinations = []
        
        # Base combination that was close
        combinations.append({
            "name": "XYZ-Tilt-Base",
            "rotations": [
                {"axis": 'x', "angle": pluto_tilt_rad},
                {"axis": 'y', "angle": pluto_tilt_rad},
                {"axis": 'z', "angle": pluto_tilt_rad}
            ]
        })
        
        # Variations around the base XYZ-Tilt rotation
        # Adjust X rotation
        for angle in [-135, -125, -115, -110, -105, -100, -95, -90]:
            combinations.append({
                "name": f"X{angle}->Y-Tilt->Z-Tilt",
                "rotations": [
                    {"axis": 'x', "angle": np.radians(angle)},
                    {"axis": 'y', "angle": pluto_tilt_rad},
                    {"axis": 'z', "angle": pluto_tilt_rad}
                ]
            })
        
        # Adjust Y rotation
        for angle in [-135, -125, -115, -110, -105, -100, -95, -90]:
            combinations.append({
                "name": f"X-Tilt->Y{angle}->Z-Tilt",
                "rotations": [
                    {"axis": 'x', "angle": pluto_tilt_rad},
                    {"axis": 'y', "angle": np.radians(angle)},
                    {"axis": 'z', "angle": pluto_tilt_rad}
                ]
            })
        
        # Adjust Z rotation
        for angle in [-135, -125, -115, -110, -105, -100, -95, -90]:
            combinations.append({
                "name": f"X-Tilt->Y-Tilt->Z{angle}",
                "rotations": [
                    {"axis": 'x', "angle": pluto_tilt_rad},
                    {"axis": 'y', "angle": pluto_tilt_rad},
                    {"axis": 'z', "angle": np.radians(angle)}
                ]
            })
        
        # Try different rotation orders
        combinations.append({
            "name": "YXZ-Tilt",
            "rotations": [
                {"axis": 'y', "angle": pluto_tilt_rad},
                {"axis": 'x', "angle": pluto_tilt_rad},
                {"axis": 'z', "angle": pluto_tilt_rad}
            ]
        })
        
        combinations.append({
            "name": "ZXY-Tilt",
            "rotations": [
                {"axis": 'z', "angle": pluto_tilt_rad},
                {"axis": 'x', "angle": pluto_tilt_rad},
                {"axis": 'y', "angle": pluto_tilt_rad}
            ]
        })
        
        # Try modified combinations with 90-degree rotations and Pluto's tilt
        combinations.append({
            "name": "X-90->Y-Tilt->Z-Tilt",
            "rotations": [
                {"axis": 'x', "angle": np.radians(-90)},
                {"axis": 'y', "angle": pluto_tilt_rad},
                {"axis": 'z', "angle": pluto_tilt_rad}
            ]
        })
        
        combinations.append({
            "name": "X-Tilt->Y-90->Z-Tilt",
            "rotations": [
                {"axis": 'x', "angle": pluto_tilt_rad},
                {"axis": 'y', "angle": np.radians(-90)},
                {"axis": 'z', "angle": pluto_tilt_rad}
            ]
        })
        
        combinations.append({
            "name": "X-Tilt->Y-Tilt->Z-90",
            "rotations": [
                {"axis": 'x', "angle": pluto_tilt_rad},
                {"axis": 'y', "angle": pluto_tilt_rad},
                {"axis": 'z', "angle": np.radians(-90)}
            ]
        })
        
        # Adding some specific combinations that might work well
        combinations.append({
            "name": "X-110->Y-115->Z-105",
            "rotations": [
                {"axis": 'x', "angle": np.radians(-110)},
                {"axis": 'y', "angle": np.radians(-115)},
                {"axis": 'z', "angle": np.radians(-105)}
            ]
        })
        
        combinations.append({
            "name": "X-115->Y-115->Z-115",
            "rotations": [
                {"axis": 'x', "angle": np.radians(-115)},
                {"axis": 'y', "angle": np.radians(-115)},
                {"axis": 'z', "angle": np.radians(-115)}
            ]
        })
        
        combinations.append({
            "name": "X-120->Y-120->Z-120",
            "rotations": [
                {"axis": 'x', "angle": np.radians(-120)},
                {"axis": 'y', "angle": np.radians(-120)},
                {"axis": 'z', "angle": np.radians(-120)}
            ]
        })
        
        # Fine-tuning around a specific zone
        for x_angle in [-122, -123]:
            for y_angle in [-122, -123]:
                for z_angle in [-122, -123]:
                    combinations.append({
                        "name": f"X{x_angle}->Y{y_angle}->Z{z_angle}",
                        "rotations": [
                            {"axis": 'x', "angle": np.radians(x_angle)},
                            {"axis": 'y', "angle": np.radians(y_angle)},
                            {"axis": 'z', "angle": np.radians(z_angle)}
                        ]
                    })
        
        # Define line styles for different combinations
        styles = ["solid", "dash", "dot", "dashdot", "longdash", "longdashdot", "solid", "dash", "dot"]
        
        # Apply each rotation combination
        for idx, combo in enumerate(combinations):
            x_rotated, y_rotated, z_rotated = x_temp.copy(), y_temp.copy(), z_temp.copy()
            
            for rot in combo["rotations"]:
                x_rotated, y_rotated, z_rotated = rotate_points(
                    x_rotated, y_rotated, z_rotated, 
                    rot["angle"], rot["axis"]
                )
            
            # Add trace with unique style
            style = styles[idx % len(styles)]
            
            fig.add_trace(
                go.Scatter3d(
                    x=x_rotated,
                    y=y_rotated,
                    z=z_rotated,
                    mode='lines',
                    line=dict(dash=style, width=1, color=color),
                    name=f"{satellite_name} {combo['name']}",
                    text=[f"{satellite_name} {combo['name']}"] * len(x_rotated),
                    customdata=[f"{satellite_name} {combo['name']}"] * len(x_rotated),
                    hovertemplate='%{text}<extra></extra>',
                    showlegend=True
                )
            )
        
        return fig
        
    except Exception as e:
        print(f"Error in test_pluto_moon_xyz_rotations: {e}")
        traceback.print_exc()
        return fig

def very_fine_pluto_rotations(satellite_name, planetary_params, color, fig=None, 
                             x_range=(-125, -115), 
                             y_range=(-125, -115), 
                             z_range=(-125, -115),
                             step=1):
    """
    Extremely fine-grained testing of XYZ rotation combinations for Pluto's moons.
    Tests all combinations within specified ranges with the given step size.
    
    Parameters:
        satellite_name (str): Name of the satellite (Charon, Styx, Nix, Kerberos or Hydra)
        planetary_params (dict): Dictionary containing orbital parameters
        color (str): Color to use for the orbit lines
        fig (plotly.graph_objects.Figure): Existing figure to add the orbit to
        x_range (tuple): Range of X rotation angles to test in degrees (min, max)
        y_range (tuple): Range of Y rotation angles to test in degrees (min, max)
        z_range (tuple): Range of Z rotation angles to test in degrees (min, max)
        step (int): Step size between angles in degrees
        
    Returns:
        plotly.graph_objects.Figure: Figure with various test orbits added
    """
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
        
        print(f"Testing very fine XYZ rotations for {satellite_name} orbit around Pluto")
        print(f"X range: {x_range}, Y range: {y_range}, Z range: {z_range}, Step: {step}")
        
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
        
        # Create angle ranges
        x_angles = range(x_range[0], x_range[1] + 1, step)
        y_angles = range(y_range[0], y_range[1] + 1, step)
        z_angles = range(z_range[0], z_range[1] + 1, step)
        
        # To limit the number of combinations, we'll only test a few combinations
        # where all three angles are the same or very similar
        combinations = []
        
        # Same angle for all three rotations
        for angle in range(max(x_range[0], y_range[0], z_range[0]), 
                           min(x_range[1], y_range[1], z_range[1]) + 1, 
                           step):
            combinations.append({
                "name": f"X{angle}->Y{angle}->Z{angle}",
                "rotations": [
                    {"axis": 'x', "angle": np.radians(angle)},
                    {"axis": 'y', "angle": np.radians(angle)},
                    {"axis": 'z', "angle": np.radians(angle)}
                ]
            })
        
        # Fixed X, varying Y and Z
        for x_angle in [x_range[0], (x_range[0] + x_range[1]) // 2, x_range[1]]:
            for y_angle in y_angles:
                for z_angle in z_angles:
                    if abs(y_angle - z_angle) <= step:  # Only when Y and Z are similar
                        combinations.append({
                            "name": f"X{x_angle}->Y{y_angle}->Z{z_angle}",
                            "rotations": [
                                {"axis": 'x', "angle": np.radians(x_angle)},
                                {"axis": 'y', "angle": np.radians(y_angle)},
                                {"axis": 'z', "angle": np.radians(z_angle)}
                            ]
                        })
        
        # Define line styles for different combinations
        styles = ["solid", "dash", "dot", "dashdot", "longdash", "longdashdot", "solid", "dash", "dot"]
        
        # Apply each rotation combination
        for idx, combo in enumerate(combinations):
            x_rotated, y_rotated, z_rotated = x_temp.copy(), y_temp.copy(), z_temp.copy()
            
            for rot in combo["rotations"]:
                x_rotated, y_rotated, z_rotated = rotate_points(
                    x_rotated, y_rotated, z_rotated, 
                    rot["angle"], rot["axis"]
                )
            
            # Add trace with unique style
            style = styles[idx % len(styles)]
            
            fig.add_trace(
                go.Scatter3d(
                    x=x_rotated,
                    y=y_rotated,
                    z=z_rotated,
                    mode='lines',
                    line=dict(dash=style, width=1, color=color),
                    name=f"{satellite_name} {combo['name']}",
                    text=[f"{satellite_name} {combo['name']}"] * len(x_rotated),
                    customdata=[f"{satellite_name} {combo['name']}"] * len(x_rotated),
                    hovertemplate='%{text}<extra></extra>',
                    showlegend=True
                )
            )
        
        return fig
        
    except Exception as e:
        print(f"Error in very_fine_pluto_rotations: {e}")
        traceback.print_exc()
        return fig

def pluto_system_final_transform(satellite_name, planetary_params, color, fig=None, transform=None):
    """
    Apply a specific optimal transformation to Pluto's moons' orbits.
    
    Parameters:
        satellite_name (str): Name of the satellite (Charon, Styx, Nix, Kerberos or Hydra)
        planetary_params (dict): Dictionary containing orbital parameters
        color (str): Color to use for the orbit lines
        fig (plotly.graph_objects.Figure): Existing figure to add the orbit to
        transform (dict, optional): Specific transformation to apply, with structure:
            {
                "x_angle": angle in degrees,
                "y_angle": angle in degrees,
                "z_angle": angle in degrees,
                "order": list of axes in order of rotation, e.g. ['x', 'y', 'z']
            }
            
    Returns:
        plotly.graph_objects.Figure: Figure with the finalized orbit
    """
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
        
        # Default transformation if none provided
        if transform is None:
            transform = {
                "x_angle": -120,
                "y_angle": -120,
                "z_angle": -120,
                "order": ['x', 'y', 'z']
            }
        
        print(f"Applying final transformation to {satellite_name} orbit around Pluto")
        print(f"Transformation: X={transform['x_angle']}°, Y={transform['y_angle']}°, Z={transform['z_angle']}°, Order={transform['order']}")
        
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
        
        # Apply the custom transformation
        x_rotated, y_rotated, z_rotated = x_temp.copy(), y_temp.copy(), z_temp.copy()
        
        # Convert transformation angles to radians
        x_angle_rad = np.radians(transform['x_angle'])
        y_angle_rad = np.radians(transform['y_angle'])
        z_angle_rad = np.radians(transform['z_angle'])
        
        # Apply rotations in specified order
        for axis in transform['order']:
            if axis == 'x':
                x_rotated, y_rotated, z_rotated = rotate_points(
                    x_rotated, y_rotated, z_rotated, x_angle_rad, 'x'
                )
            elif axis == 'y':
                x_rotated, y_rotated, z_rotated = rotate_points(
                    x_rotated, y_rotated, z_rotated, y_angle_rad, 'y'
                )
            elif axis == 'z':
                x_rotated, y_rotated, z_rotated = rotate_points(
                    x_rotated, y_rotated, z_rotated, z_angle_rad, 'z'
                )
        
        # Add the finalized orbit trace
        fig.add_trace(
            go.Scatter3d(
                x=x_rotated,
                y=y_rotated,
                z=z_rotated,
                mode='lines',
                line=dict(width=2, color=color),
                name=f"{satellite_name} Final",
                text=[f"{satellite_name} Final Orbit"] * len(x_rotated),
                customdata=[f"{satellite_name} Final Orbit"] * len(x_rotated),
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
        
        return fig
    
    except Exception as e:
        print(f"Error in pluto_system_final_transform: {e}")
        traceback.print_exc()
        return fig
    
from datetime import datetime

date1 = datetime(2025, 6, 17)
date2 = datetime(2026, 6, 17)

print("=== TESTING TIME-VARYING ELEMENTS ===")
elements1 = calculate_mars_satellite_elements(date1, 'Phobos')
elements2 = calculate_mars_satellite_elements(date2, 'Phobos')

# Handle angle wraparound for Omega change
omega_change = elements2['omega'] - elements1['omega']
Omega_change = elements2['Omega'] - elements1['Omega']

# Fix Omega wraparound
if Omega_change > 180:
    Omega_change -= 360
elif Omega_change < -180:
    Omega_change += 360

print(f"Phobos Ω change over 1 year: {Omega_change:.1f}° (expected: ~-158°)")
print(f"Phobos ω change over 1 year: {omega_change:.1f}° (expected: ~+27°)")

# Also print the actual values for debugging
print(f"\nDebug info:")
print(f"Start: Ω={elements1['Omega']:.1f}°, ω={elements1['omega']:.1f}°")
print(f"End:   Ω={elements2['Omega']:.1f}°, ω={elements2['omega']:.1f}°")

# Test different epochs
epochs = [
    datetime(2025, 6, 17),   # Start of data
    datetime(2026, 6, 17),   # Middle of data  
    datetime(2027, 6, 17),   # End of data
    datetime(2000, 1, 1, 12) # J2000.0
]

for epoch in epochs:
    elements = calculate_mars_satellite_elements(epoch, 'Phobos')
    print(f"Epoch {epoch}: Ω={elements['Omega']:.1f}°, ω={elements['omega']:.1f}°")

def calculate_phoebe_correction_from_normals():
    """
    Calculate the optimal rotation to align ideal orbit with actual orbit
    based on their normal vectors.
    """
    # Normal vectors from your output
    n_actual = np.array([0.1242, 0.0025, 0.9922])
    n_ideal = np.array([0.1814, -0.1036, 0.9779])
    
    # Calculate rotation axis and angle
    rotation_axis = np.cross(n_ideal, n_actual)
    rotation_axis = rotation_axis / np.linalg.norm(rotation_axis)
    
    cos_angle = np.dot(n_ideal, n_actual)
    angle = np.arccos(np.clip(cos_angle, -1, 1))
    
    print(f"Rotation axis: {rotation_axis}")
    print(f"Rotation angle: {np.degrees(angle):.2f}°")
    
    # Decompose into X, Y, Z rotations
    # This is approximate but gives us insight
    x_component = np.arcsin(rotation_axis[0]) * angle
    y_component = np.arcsin(rotation_axis[1]) * angle  
    z_component = np.arcsin(rotation_axis[2]) * angle
    
    print(f"Approximate decomposition:")
    print(f"  X rotation: {np.degrees(x_component):.2f}°")
    print(f"  Y rotation: {np.degrees(y_component):.2f}°")
    print(f"  Z rotation: {np.degrees(z_component):.2f}°")
    
    return rotation_axis, angle