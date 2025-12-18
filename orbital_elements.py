"""
orbital_elements.py

Standalone data module containing orbital element dictionaries.
NO IMPORTS - Pure data only to avoid circular dependencies.

This module provides:
- planetary_params: Orbital elements for all solar system objects
- parent_planets: Mapping of parent bodies to their satellites
- planet_tilts: Axial tilt data for planets

Part of Paloma's Orrery
Created: November 18, 2025 (Extracted from idealized_orbits.py to fix import chain)
"""

planetary_params = {
        #   Standard J2000 mean orbital elements for all planets. These are indeed in the ecliptic frame.
        #   Source: NASA Planetary Fact Sheets: https://nssdc.gsfc.nasa.gov/planetary/factsheet/
        #   JPL Approximate Positions: https://ssd.jpl.nasa.gov/planets/approx_pos.html
        #   Here are the updated values with J2000.0 mean elements. 

    # Saturn satellites
#    'Atlas': 0.602,        # 14.45 hours
#    'Epimetheus': 0.694,   # 16.66 hours
#    'Janus': 0.695,        # 16.68 hours

    # Uranus satellites
#    'Puck': 0.762,         # 18.29 hours
# new uranus satellite found by Webb number 29
  
    # Neptune satellites  
#    'Proteus': 1.122,      # 26.93 hours
#    'Larissa': 0.555,      # 13.32 hours
#    'Naiad': 0.294,        # 7.06 hours
    
    # Asteroids
#    'Pallas': 1685.37,     # 4.614 * 365.25
#    'Juno': 1591.93,       # 4.358 * 365.25  
#    'Hygiea': 2041.88,     # 5.592 * 365.25
#    'Psyche': 1825.01,     # 4.997 * 365.25
#    'Phaethon': 523.42,    # 1.43 * 365.25
    
    # Near-Earth asteroids
#    '2025 KV': 695.85,     # 1.91 * 365.25
    
    # Comets (converted from years to days where applicable)
#    'ISON': 230970.00,     # 632.3 * 365.25 (pre-disruption)
        
'Mercury': {    
        'a': 0.3870976430975001,
        'e': 0.2056464328427787,
        'i': 7.003437180750216,
        'omega': 29.19879045729881,
        'Omega': 48.29886557533597,
        'epoch': '2025-11-19 osc.',
        'TP': 2461002.976715519,
        #     'Mercury': 87.969,  days    
    },
    
    'Venus': {  
        'a': 0.72333566,
        'e': 0.00677672,
        'i': 3.39467605,
        'omega': 54.852,  # Corrected:
        'Omega': 76.67984255,
        'epoch': '2024-08-03',  # Date of perihelion passage
        'TP': 2460522.892,      # Time of perihelion - 2024-Aug-03
        #     'Venus': 224.701, 
    },
    
# Aten type near earth asteroids, a < 1.0 AU AND aphelion (Q) > 0.983 AU (Earth's perihelion) → cross Earth's orbit from inside

    'Apophis': {
        'a': 0.922583,   # Horizons: A, semi-major axis in AU
        'e': 0.191481,   # Horizons: EC, eccentricity
        'i': 3.331,      # inclination in degrees
        'omega': 126.394, # argument of perihelion in degrees
        'Omega': 204.061,  # longitude of ascending node in degrees;  
        'epoch': '2025-08-12',
        'TP': 2460719.3535595234   # 2025-Feb-12.8536 TDB (IAWN/Horizons)
        #  PER     'Apophis': 323.60,     # 0.89 * 365.25
        # aphelion (Q) = a * (1 + e) = 1.099 AU
    }, 

    'Earth': {  
        'a': 1.00000261,
        'e': 0.01671123,
        'i': 0.00001531,       # Nearly zero in ecliptic frame
        'omega': 102.93768193,  # Corrected from your 114.207
        'Omega': 0.0,          # Undefined for Earth in ecliptic, set to 0
        'epoch': '2025-01-03',  # Date of perihelion passage
        'TP': 2460677.413,      # Time of perihelion - 2025-Jan-03
        #     'Earth': 365.256,
    },
    
# Langrange points do not have orbital parameters, EM-L1 to EM-L5 and L1 to L5, but maybe could
# space missions do not have orbital parameters

    # Apollos: a > 1.0 AU, Perihelion < 1.017 AU, → cross Earth's orbit from outside

    '2024 DW': {                  # 50613029 (2024 DW) 2025-Jul-05 10:27:18; Soln.date: 2024-Feb-23
        'a': 2.421098478271158,   # Horizons: A, semi-major axis in AU
        'e': .6939958024514898,   # Horizons: EC, eccentricity
        'i': .9861902430422796,      # Horizons: IN, inclination in degrees
        'omega': 244.5179261214832, # Horizons: W, argument of perihelion in degrees
        'Omega': 335.4879825233473,   # Horizons: OM, longitude of ascending node in degrees;  
        'epoch': '2024-02-19'  # Horizons: epoch
        # need period
        # perihelion (q) = a * (1 - e) = 0.741
    },

    '2025 PY1': {                         # osculating elements for 2460862.500000000 = A.D. 2025-Jul-06 00:00:00.0000 TDB
        'a': 1.078452460125784,         # Horizons: A, semi-major axis in AU
        'e': .2233327947850885,         # Horizons: EC, eccentricity
        'i': 4.573408702272091,         # Horizons: IN, inclination in degrees
        'omega': 267.1185311148099,     # Horizons: W, argument of perihelion in degrees
        'Omega': 145.4731476162657,     # Horizons: OM, longitude of ascending node in degrees
        'epoch': '2025-8-18',            # osculating date: 2460862.500000000 = A.D. 2025-Jul-06 00:00:00.0000 TDB
        'TP': 2460976.5756525602,     # 2025-10-28 1:48:56
        'Tapo': 2461185.0875000,              # 2026-05-24 14:06      
        # 409.072695,    # PER= 1.00631 julian years
        # perihelion (q) = a * (1 - e) = 0.838
    },

    '2024 YR4': {                  # Epoch 2025-1-30, heliocentric, solution date 2025-6-3
        'a': 2.516308070047454,   # Horizons: A, semi-major axis in AU
        'e': .6615999301423001,   # Horizons: EC, eccentricity
        'i': 3.408259321981154,      # Horizons: IN, inclination in degrees
        'omega': 134.3644983455991, # Horizons: W, argument of perihelion in degrees
        'Omega': 271.3674693540159,   # Horizons: OM, longitude of ascending node in degrees;  
        'epoch': '2025-08-12',
        'TP': 2462115.7385         # 2028-Dec-10 (TheSkyLive)
        #     '2024 YR4': 922.84,    # 2.53 * 365.25
        # perihelion (q) = a * (1 - e) = 0.851
    },

    '2025 PN7': {                  # Rec #:50615430 (+COV) Soln.date: 2025-Aug-31_07:21:10 # obs: 27 (2013-2025) mean elements
        'a': 1.004188800489803,         # Horizons: A, semi-major axis in AU
        'e': .1071782474710749,         # Horizons: EC, eccentricity
        'i': 1.984028877925589,         # Horizons: IN, inclination in degrees
        'omega': 82.04919713631394,     # Horizons: W, argument of perihelion in degrees
        'Omega': 113.0180181480993,     # Horizons: OM, longitude of ascending node in degrees
        'epoch': '2023-Jul-06.00',            # osculating date: 2460131.5
        'TP': 2460048.1958280094,     # 2023-Apr-13.6958280094
        #    'Tapo':       
        # PER= 1.00631 julian years 367.5547275 d
        # perihelion (q) = a * (1 - e) = 0.896
    },

    'Bennu': {
        'a': 1.126391,    # semi-major axis in AU
        'e': 0.203745,    # eccentricity
        'i': 6.035,       # inclination in degrees
        'omega': 66.223,  # argument of perihelion in degrees
        'Omega': 2.061    # longitude of ascending node in degrees
        # PER    'Bennu': 436.65,       # 1.20 * 365.25
        # perihelion (q) = a * (1 - e) =  0.897
    },

    'Kamo oalewa': {     # 469219 Kamo`oalewa (2016 HO3)      2025-Jul-05 08:35:28        
        'a': 1.00102447694204,   # Horizons: A, semi-major axis in AU
        'e': .1040534310625292,   # Horizons: EC, eccentricity
        'i': 7.773894173631178,      # Horizons: IN, inclination in degrees
        'omega': 307.0951007739783, # Horizons: W, argument of perihelion in degrees
        'Omega': 66.43991583004482   # Horizons: OM, longitude of ascending node in degrees
        # need period
        # perihelion (q) = a * (1 - e) = 0.897 
    },     

    'Itokawa': {
        'a': 1.324163,   # semi-major axis in AU
        'e': 0.280164,   # eccentricity
        'i': 1.622,      # inclination in degrees
        'omega': 162.767, # argument of perihelion in degrees
        'Omega': 69.095   # longitude of ascending node in degrees
        # PER: 556.38,     # 1.52 * 365.25
        # perihelion (q) = a * (1 - e) = 0.953
    },

    'Ryugu': {
        'a': 1.189562,   # semi-major axis in AU
        'e': 0.190349,   # eccentricity
        'i': 5.884,      # inclination in degrees
        'omega': 211.421, # argument of perihelion in degrees
        'Omega': 251.617,  # longitude of ascending node in degrees;  
        'epoch': '2025-08-12',
        'TP': 2460643.5508         # 2024-Nov-29 (TheSkyLive)
        # PER: 473.98,       # 1.30 * 365.25
        # perihelion (q) = a * (1 - e) = 0.963
    },

    '2024 PT5': {                  # Epoch 2024-10-20, heliocentric
        'a': 1.012228628670663,   # Horizons: A, semi-major axis in AU
        'e': .02141074038624791,   # Horizons: EC, eccentricity
        'i': 1.518377382131216,      # Horizons: IN, inclination in degrees
        'omega': 116.8074860094156, # Horizons: W, argument of perihelion in degrees
        'Omega': 305.1069316209851   # Horizons: OM, longitude of ascending node in degrees;  
        # PER: 368.75,    # 1.01 * 365.25
        # perihelion (q) = a * (1 - e) = 0.990
    },

    '2023 JF': {        # (2023 JF)  EPOCH=  2460073.5 ! 2023-May-09.00 (TDB)
        'a': 1.680153966583222,   # A - semi-major axis in AU
        'e': .409819444019783,   # EC - eccentricity
        'i': 3.1489028778487,     # IN - inclination in degrees
        'omega': 199.537622506113, # W - argument of perihelion in degrees
        'Omega': 50.09327122563936  # OM - longitude of ascending node in degrees
        # PER     '2023 JF': 493.37,     # 1.35 * 365.25
        # perihelion (q) = a * (1 - e) = 0.992
    },

    # Amor type near Earth asteroids; Perihelion > 1.017 AU and < 1.3 AU → approach but don't cross Earth's orbit

    'Eros': {
        'a': 1.458040,   # semi-major axis in AU
        'e': 0.222868,   # eccentricity
        'i': 10.829,     # inclination in degrees
        'omega': 178.817, # argument of perihelion in degrees
        'Omega': 304.435,  # longitude of ascending node in degrees;  
        'epoch': '2025-08-12',
        'TP': 2460445.7223         # 2024-May-15 (TheSkyLive)
        # PER: 642.63,        # 1.76 * 365.25
        # perihelion (q) = a * (1 - e) = 1.133
    },

    'Mars': {
        'a': 1.52371034,
        'e': 0.09339410,
        'i': 1.84969142,
        'omega': 286.502,    # Corrected
        'Omega': 49.55953891,
        'epoch': '2024-10-05',  # Date of perihelion passage
        'TP': 2460587.648,      # Time of perihelion - 2024-Oct-05
        #     'Mars': 686.980,  
    },
    
    'Dinkinesh': {      # 152830 Dinkinesh (1999 VD57)
        'a': 2.191622877873451,   # A - semi-major axis in AU
        'e': .1121269945294693,   # EC - eccentricity
        'i': 2.093523142255687,     # IN - inclination in degrees
        'omega': 66.78467710309617, # W - argument of perihelion in degrees
        'Omega': 21.38248704730461  # OM - longitude of ascending node in degrees
        #     'Dinkinesh': 1387.50,  # 3.80 * 365.25
    },    

    'Vesta': {
        'a': 2.3617,
        'e': 0.089,
        'i': 7.155,
        'omega': 151.216,
        'Omega': 103.851,
        'epoch': '2025-08-12',
        'TP': 2460902.9691         # 2025-Aug-15 (TheSkyLive)
        #     'Vesta': 1325.75,      # 3.63 * 365.25
    },

    'Steins': {
        'a': 2.363,      # semi-major axis in AU
        'e': 0.146,      # eccentricity
        'i': 9.944,      # inclination in degrees
        'omega': 250.97,  # argument of perihelion in degrees
        'Omega': 55.39    # longitude of ascending node in degrees
        #     'Šteins': 1327.41,     # 3.64 * 365.25
    },

    'Donaldjohanson': {     # 52246 Donaldjohanson (1981 EQ5)
        'a': 2.383273486221501,      # A - semi-major axis in AU
        'e': .1874831199365464,      # EC - eccentricity
        'i': 4.423903983190933,      # IN - inclination in degrees
        'omega': 212.9285580998883,  # W - argument of perihelion in degrees
        'Omega': 262.7951724145965     # OM - longitude of ascending node in degrees;  
        #     'Donaldjohanson': 1446.04, # 3.96 * 365.25
    },



    'Lutetia': {                  # Epoch 2017-10-12, heliocentric
        'a': 2.434591597038037,   # Horizons: A, semi-major axis in AU
        'e': .1644174522633922,   # Horizons: EC, eccentricity
        'i': 3.063715677953934,      # Horizons: IN, inclination in degrees
        'omega': 249.980528664283, # Horizons: W, argument of perihelion in degrees
        'Omega': 80.87713180326485   # Horizons: OM, longitude of ascending node in degrees
        #     'Lutetia': 1321.00,    # 3.62 * 365.25
    },



    'Ceres': {
        'a': 2.7675,
        'e': 0.076,
        'i': 10.593,
        'omega': 73.597,
        'Omega': 80.393,
        'epoch': '2025-08-12',
        'TP': 2461601.4340         # 2027-Jul-14 (TheSkyLive)
        #     'Ceres': 1680.15,      # 4.6 * 365.25
    },

    # Trojan Asteroids

     'Orus': {                  # 21900 Orus (1999 VQ10)
        'a': 5.12481038867513,   # Horizons: A, semi-major axis in AU
        'e': .03658969107145676,   # Horizons: EC, eccentricity
        'i': 8.468402951870347,      # Horizons: IN, inclination in degrees
        'omega': 179.5712820784224, # Horizons: W, argument of perihelion in degrees
        'Omega': 258.5587182277959   # Horizons: OM, longitude of ascending node in degrees;  
        #     'Orus': 4274.32,       # 11.71 * 365.25
    }, 

     'Polymele': {                  # 15094 Polymele (1999 WB2)
        'a': 5.183610039255559,   # Horizons: A, semi-major axis in AU
        'e': .09688597854047172,   # Horizons: EC, eccentricity
        'i': 12.98094196026331,      # Horizons: IN, inclination in degrees
        'omega': 5.149831531818331, # Horizons: W, argument of perihelion in degrees
        'Omega': 50.31413377311653   # Horizons: OM, longitude of ascending node in degrees
        #     'Polymele': 4319.33,   # 11.83 * 365.25
    }, 

    'Jupiter': {
        'a': 5.20288700,
        'e': 0.04838624,
        'i': 1.30439695,
        'omega': 273.867,      # This one was already correct!
        'Omega': 100.47390909,
        'epoch': '2023-01-21',  # Date of perihelion passage
        'TP': 2459993.180,      # Time of perihelion - 2023-Jan-21
        #     'Jupiter': 4332.589,  
    },
    
     'Eurybates': {                  # 3548 Eurybates (1973 SO)
        'a': 5.209549873585049,   # Horizons: A, semi-major axis in AU
        'e': .0911999243850036,   # Horizons: EC, eccentricity
        'i': 8.054169046592317,      # Horizons: IN, inclination in degrees
        'omega': 27.83332476783044, # Horizons: W, argument of perihelion in degrees
        'Omega': 43.54011293260102   # Horizons: OM, longitude of ascending node in degrees
        #     'Eurybates': 4333.71,  # 11.87 * 365.25
    },  

     'Patroclus': {                  # 617 Patroclus (A906 UL) 
        'a': 5.212775153315913,   # Horizons: A, semi-major axis in AU
        'e': .1394751015199425,   # Horizons: EC, eccentricity
        'i': 22.05719746380513,      # Horizons: IN, inclination in degrees
        'omega': 307.9473518701323, # Horizons: W, argument of perihelion in degrees
        'Omega': 44.34955228487597   # Horizons: OM, longitude of ascending node in degrees
        #     'Patroclus': 4336.36,  # 11.88 * 365.25
    }, 

     'Leucus': {                  # 11351 Leucus (1997 TS25)
        'a': 5.2899315120334,   # Horizons: A, semi-major axis in AU
        'e': .06389742479789216,   # Horizons: EC, eccentricity
        'i': 11.55528566945522,      # Horizons: IN, inclination in degrees
        'omega': 160.4023262565797, # Horizons: W, argument of perihelion in degrees
        'Omega': 251.0747114724082   # Horizons: OM, longitude of ascending node in degrees;  
        #     'Leucus': 4352.24,     # 11.92 * 365.25
    },  

    # Comets with closed elliptical orbits; object type 'orbital'
    
    'Churyumov': {                          # 67P/Churyumov-Gerasimenko
        'a': 3.462249489765068,             # Horizons: A, semi-major axis in AU
        'e': .6409081306555051,             # Horizons: EC, eccentricity
        'i': 7.040294906760007,             # Horizons: IN, inclination in degrees
        'omega': 12.79824973415729,         # Horizons: W, argument of perihelion in degrees
        'Omega': 50.13557380441372,         # Horizons: OM, longitude of ascending node in degrees
        'epoch': '2015-10-10',              # EPOCH=  2457305.5 ! 2015-Oct-10.0000000 (TDB)         
        'TP': 2457247.5886578634,           # TP= 2015-Aug-13.0886578634
    #    'Tapo': ,                          # needed for actual aphelion date
                                            # PER= 6.4423711636744 jy =  2353.076068 days 
    },

    'Saturn': {
        'a': 9.53667594,
        'e': 0.05386179,
        'i': 2.48599187,
        'omega': 339.392,      # This one was already correct!
        'Omega': 113.66242448,
        'epoch': '2003-06-27',  # Date of perihelion passage
        'TP': 2452815.907,      # Time of perihelion - 2003-Jun-27
        #     'Saturn': 10759.22,  
    },
    
    'Chariklo': {                       # 10199 Chariklo (1997 CU26)
        'a': 15.82593058868572,         # A
        'e': .1719500347024694,         # EC
        'i': 23.37854062415448,         # IN
        'omega': 242.9893479383809,     # W
        'Omega': 300.4194578295845,     # OM 
        'epoch': '2017-12-4',           # EPOCH=  2458091.5 ! 2017-Dec-04.00 (TDB)
        'TP': 2453044.2465350656,       # Time of perihelion - 2004-Feb-08.7465350656
                                        # PER= 62.95962 jy = 22996.00121 days           
    },

    'Halley': {                         # Rec #:90000030; 1P/Halley; Soln.date: 2024-Apr-16_14:38:13; data arc: 1835-08-21 to 1994-01-11
        'a': 17.85950919,               # Horizons: A, semi-major axis in AU
        'e': 0.9678338727,              # Horizons: EC, eccentricity
        'i': 162.1475927,               # Horizons: IN, inclination in degrees; Retrograde, i > 90. 
        'omega': 112.497549,            # Horizons: W, argument of perihelion in degrees
        'Omega': 59.59944738,           # Horizons: OM, longitude of ascending node in degrees
        'epoch': '2025-7-6',            # osculating date: 2460862.500000000 = A.D. 2025-Jul-06 00:00:00.0000 TDB
        'TP': 2474058.277997814585,     # 2061-08-21 18:40:19 
        'Tapo': 2460856.0,              # 2025-06-29 12:00:00       
        #     'Halley': 27731.29226,    # PER=75.924140333742 julian year * 365.25 = 27731.29226
    },

    'Uranus': {
        'a': 19.18916464,
        'e': 0.04725744,
        'i': 0.77263783,
        'omega': 96.998857,    # This one was already correct!
        'Omega': 74.01692503,
        'epoch': '2050-08-20',  # Date of perihelion passage
        'TP': 2470213.857,      # Time of perihelion - 2050-Aug-20
        #     'Uranus': 30688.5,    
    },
    
    'Neptune': {
        'a': 30.06992276,
        'e': 0.00859048,
        'i': 1.77004347,
        'omega': 276.340,      
        'Omega': 131.78422574,
        'epoch': '2042-09-04',  # Date of perihelion passage
        'TP': 2468182.079,      # Time of perihelion - 2042-Sep-04
        #     'Neptune': 60189.0,  
    },
        
    # Dwarf Planets

    'Orcus': {                      # 90482 Orcus (2004 DW)
        'a': 39.39498513874738,                # A - semi-major axis in AU
        'e': .220173694129795,                 # EC - eccentricity
        'i': 20.58296889775066,                # IN - inclination in degrees
        'omega': 72.38143133086857,            # W - argument of perihelion in degrees
        'Omega': 268.7202801899987,            # OM - longitude of ascending node in degrees; 
        'epoch': '2017-09-26',                 # 2017-Sep-26.00 for ephemeris
        'TP': 2413410.1091600764,              # Time of perihelion - 1895-Aug-04.6091600764        
        # Period: 90314.9912925 days, 247.26897 julian years * 365.25
    },

    'Pluto': {
        'a': 39.48211675,
        'e': 0.24882730,
        'i': 17.14001206,
        'omega': 113.834,      # Close to correct (should be 113.76)
        'Omega': 110.30393684,
        'epoch': '1989-12-12',  # Date of perihelion passage
        'TP': 2447891.824,      # Time of perihelion - 1989-Dec-12
        #     'Pluto': 90560.0, 
    },

    'Ixion': {                          # 28978 Ixion (2001 KX76) 
        'a': 39.66337068351097,         # A - semi-major axis in AU
        'e': .2418414354067134,         # EC - eccentricity
        'i': 19.58703444758994,         # IN - inclination in degrees
        'omega': 298.8358378061579,     # W - argument of perihelion in degrees
        'Omega': 70.99623775199329,     # OM - longitude of ascending node in degrees
        'epoch': '2017-09-7',           # EPOCH=  2458003.5 ! 2017-Sep-07.00 (TDB) 
        'TP': 2477290.5810889825,       # TP= 2070-Jun-28.0810889825        
        # period —  PER= 249.80011
    },

    'Mani': {                           # 307261 Mani (2002 MS4) 
        'a': 41.96777641127755,         # A, semi-major axis in AU
        'e': .1393970721853619,         # EC, eccentricity
        'i': 17.6693032832701,          # IN, inclination in degrees
        'omega': 213.7989882449192,     # W, argument of perihelion in degrees
        'Omega': 215.9145112848788,     # OM, longitude of ascending node in degrees; 
        'epoch': '2018-09-17',          # EPOCH=  2458378.5 ! 2018-Sep-17.00 (TDB) 
        'TP': 2496542.2060495983,       # TP= 2123-Mar-14.7060495983 
                                        # period — PER= 271.88306 jy = 99305.28767
    },

    'GV9': {                            # 90568 (2004 GV9)   
        'a': 42.26218206953708,         # A, semi-major axis in AU
        'e': .08176903225395735,        # EC, eccentricity
        'i': 21.92860124861248,         # IN, inclination in degrees
        'omega': 295.464267897557,      # W, argument of perihelion in degrees
        'Omega': 250.6682664772548,     # OM, longitude of ascending node in degrees;
        'epoch': '2018-3-9',            # EPOCH=  2458186.5 ! 2018-Mar-09.00 (TDB)
        'TP': 2448321.5580008202,       # TP= 1991-Mar-06.0580008202
                                        # period — PER= 274.74897 jy = 100352.0613 days
    },

    'Varuna': {
        'a': 42.947,     # semi-major axis in AU
        'e': 0.051739,   # eccentricity
        'i': 17.200,     # inclination in degrees
        'omega': 97.286,  # argument of perihelion in degrees
        'Omega': 97.286   # longitude of ascending node in degrees
        # period — 102799.14 days (epoch 2025-08-12)
    },

    'Haumea': {
        'a': 43.13,
        'e': 0.191,
        'i': 28.20,
        'omega': 240.20,
        'Omega': 122.10,
        'epoch': '2025-08-12',
        'TP': 2500289.4542         # Next perihelion JD (2133-06-16 TDB)
        #     'Haumea': 103731.00,   # 284.0 * 365.25
    },

    'Quaoar': {
        'a': 43.325,
        'e': 0.0392,
        'i': 8.34,
        'omega': 157.631,
        'Omega': 188.809        # 
        #     'Quaoar': 105192.00,   # 288.0 * 365.25
    },

    'Arrokoth': {                  # Epoch 2017-12-14, heliocentric
        'a': 44.44519963724322,   # A, semi-major axis in AU
        'e': .03868645692376498,   # EC, eccentricity
        'i': 2.45301305206896,      # IN, inclination in degrees
        'omega': 176.1507602341478, # W, argument of perihelion in degrees
        'Omega': 158.939446659904   # OM, longitude of ascending node in degrees
        # period — 108224.98 days (epoch 2025-08-12)
    },

    'Makemake': {   # 136472 Makemake (2005 FY9); Epoch 2018-Jan-10
        'a': 45.6923640352447,                    # A
        'e': .1551157031828145,                   # EC
        'i': 28.98446068551257,                   # IN
        'omega': 295.7568523219785,               # W
        'Omega': 79.60732027458391,                # OM
        'epoch': '2025-08-12',       # solution date      
        'TP': 2520030.5498         # Next perihelion JD (2187-07-05 TDB)
        #     'Makemake': 111766.50, # 306.0 * 365.25
    },

    'Gonggong': {  # 225088 Gonggong (2007 OR10); Epoch 2017-Sep-25
        'a': 67.15612088312527,     # A, semi-major axis in AU
        'e': .5057697166633393,   # EC, eccentricity
        'i': 30.86452616352285,     # IN, inclination in degrees
        'omega': 207.2059900430104, # W, argument of perihelion in degrees
        'Omega': 336.8262717815297  # OM, longitude of ascending node in degrees; 
        # period — 201010.45 days (epoch 2025-08-12)
    },    

    'Eris': {
        'a': 67.78,
        'e': 0.441,
        'i': 44.03,
        'omega': 150.977,
        'Omega': 35.873
        #     'Eris': 203809.50,     # 558.0 * 365.25
    },

    'Ikeya-Seki': {                  # Epoch 1965-10-7, heliocentric, (C/1965 S1-A)
        'a': 91.59999999999813,   # Horizons: A, semi-major axis in AU
        'e': .999915,   # Horizons: EC, eccentricity
        'i': 141.8642,      # Horizons: IN, inclination in degrees; retrograde > 90
        'omega': 69.04859999999999, # Horizons: W, argument of perihelion in degrees
        'Omega': 346.9947   # Horizons: OM, longitude of ascending node in degrees;  
        #     'Ikeya-Seki': 319800.00, # 876.0 * 365.25 (estimate)
    },

    'Lemmon': {                  # JPL/HORIZONS                 Lemmon (C/2025 A6)            2025-Oct-04 14:37:27 
        # data arc: 2024-11-12 to 2025-10-03
        'a': 122.0093217668137,   # Horizons: A, semi-major axis in AU
        'e': .9956568328248036,   # Horizons: EC, eccentricity
        'i': 143.6632748988036,      # Horizons: IN, inclination in degrees; retrograde > 90
        'omega': 132.9672366055109, # Horizons: W, argument of perihelion in degrees
        'Omega': 108.0976178317535,   # Horizons: OM, longitude of ascending node in degrees
        'epoch': '2025-Aug-10',
        'TP': 2460988.0373512669  # 2025-Nov-08.5373512669
        # PER= 1347.7139437075 jy = 492252.5179 days (see orbital parameters calcs)
    },

    'Hale-Bopp': {                          # Hale-Bopp (C/1995 O1)   
        'a': 177.4333839117583,             # Horizons: A, semi-major axis in AU
        'e': .9949810027633206,             # Horizons: EC, eccentricity
        'i': 89.28759424740302,             # Horizons: IN, inclination in degrees
        'omega': 130.4146670659176,         # Horizons: W, argument of perihelion in degrees
        'Omega': 282.7334213961641,        # Horizons: OM, longitude of ascending node in degrees;  
        'epoch': '2022-9-15',               # EPOCH=  2459837.5 ! 2022-Sep-15.0000000 (TDB)
        'TP': 2450537.1349071441,           # 1997-Mar-29.6349071441 
    #    'Tapo': ,                          # needed       
                                            # PER= 2363.5304681429 jy = 863279.5035
    },  

    'Ammonite': {              #  2023 KQ14; Soln.date: 2025-Apr-29_21:35:00
        'a': 250.0679474237761,         # A
        'e': .7370249039390946,         # EC
        'i': 10.99528818274681,         # IN
        'omega': 199.2155526048832,     # W
        'Omega': 72.0885184764268,      # OM
        'epoch': '2025-4-29',
        'TP': 2474830.256515193265  # Time of perihelion (JD)  
        #     'Ammonite': 1444383.67 ,     # PER 3954.53339 Julian years 
    },

    'NEOWISE': {                  # 2020-Jul-06.0000000, heliocentric, NEOWISE (C/2020 F3) 
        'a': 358.4679565529321,   # Horizons: A, semi-major axis in AU
        'e': .9991780262531292,   # Horizons: EC, eccentricity
        'i': 128.9375027594809,      # Horizons: IN, inclination in degrees; retrograde > 90
        'omega': 37.2786584481257, # Horizons: W, argument of perihelion in degrees
        'Omega': 61.01042818536988,   # Horizons: OM, longitude of ascending node in degrees
        # need period
    }, 

    'Sedna': {  # 90377 Sedna (2003 VB12); Epoch 2018-May-16
        'a': 481.3036019474312,         # A
        'e': .8418992747337005,         # EC
        'i': 11.92926934569724,         # IN
        'omega': 311.5908685997484,     # W
        'Omega': 144.4059276991507,      # OM
        'epoch': '2025-08-12', 
        'TP': 2479072.5781         # Next perihelion JD (2075-05-15 TDB)       
        #     'Sedna': 4163850.00,   # 11400.0 * 365.25
    },

    'Planet 9': {
        'a': 600,          # Semi-major axis in AU (updated to match 500-700 AU range from IRAS/AKARI study)
        'e': 0.30,         # Eccentricity (slightly adjusted to align with 280-1120 AU perihelion/aphelion range)
        'i': 6,            # Inclination in degrees (2025 estimate: 6°)
        'L': 238,          # Mean longitude at epoch in degrees (unchanged)
        'omega': 150,      # Argument of perihelion in degrees (unchanged)
        'Omega': 90        # Longitude of ascending node in degrees (unchanged)        
        #     'Planet 9': 3652500.00, # ~10000 * 365.25 (estimated)
    },

    'SWAN': {                  # SWAN (C/2025 R2)  Rec #:90004920 (+COV) Soln.date: 2025-Sep-15_12:40:16  
        # data arc: 2025-08-13 to 2025-09-14   obs: 83 (32 days
        'a': 798.2574580972854,   # Horizons: A, semi-major axis in AU
        'e': .9993692862141036,   # Horizons: EC, eccentricity
        'i': 4.470167090495599,      # Horizons: IN, inclination in degrees
        'omega': 307.7690351733913, # Horizons: W, argument of perihelion in degrees
        'Omega': 335.6745583920674,   # Horizons: OM, longitude of ascending node in degrees
        'epoch': '2025-09-13',
        'TP': 2460931.1155318194  # 2025-Sep-12.6155318194
        # PER= 22553.953438133 jy = 8237831.493 days
    }, 

    '2017 OF201': {  # Epoch 2012-Jan-22.00
        'a': 911.3212633626483,         # A
        'e': .95044195853967,         # EC
        'i': 16.20068039109616,         # IN
        'omega': 338.23502348994,     # W
        'Omega': 328.5637374192406      # OM 
        # period — 10048413.07 days (epoch 2025-08-12)
    },

    'Leleakuhonua': {                   #  541132 Leleakuhonua (2015 TG387) ; Soln.date: 2025-Jul-02_03:47:19
        'a': 1062.136603634751,         # A
        'e': .9390574940805684,         # EC
        'i': 11.66948508856894,         # IN
        'omega': 118.4456730982617,     # W
        'Omega': 300.9623405298694,     # OM  
        'epoch': '2017-7-10',           # EPOCH=  2457944.5 ! 2017-Jul-10.00 (TDB)
        'TP': 2480393.5636051819        # TP= 2078-Dec-26.0636051819
        #     'Leleakuhonua': 12643548.84594,  # Orbital period in days;  34616.15016 julian years x 365.25
    },    

    'Hyakutake': {                          # Hyakutake (C/1996 B2)    
        'a': 2124.755444396066,             # Horizons: A, semi-major axis in AU
        'e': .9998916470450124,             # Horizons: EC, eccentricity
        'i': 124.9220493922234,             # Horizons: IN, inclination in degrees; retrograde > 90
        'omega': 130.1751209780967,         # Horizons: W, argument of perihelion in degrees
        'Omega': 188.045131992156,          # Horizons: OM, longitude of ascending node in degrees;  
        'epoch': '1996-3-15',               # EPOCH=  2450157.5 ! 1996-Mar-15.0000000 (TDB)
        'TP': 2450204.8941449965,           # TP= 1996-May-01.3941449965 
    #    'Tapo': ,                          # needed       
                                            # PER= 97942.599927659 jy = 35773534.62 days
    },

    # Comets with hyperbolic trajectories, object type 'trajectory'

    'West': {                  # West (C/1975 V1-A) 
        'a': -12220.2703313635,   # Horizons: A, semi-major axis in AU; hyperbolic/parabolic
        'e': 1.000016087612074,   # Horizons: EC, eccentricity
        'i': 43.07404350452942,      # Horizons: IN, inclination in degrees
        'omega': 358.4317208087168, # Horizons: W, argument of perihelion in degrees
        'Omega': 118.9175346769632,   # Horizons: OM, longitude of ascending node in degrees
        'epoch': 2021-4-15,     # Rec #:90002073 (+COV) Soln.date: 2021-Apr-15_23:29:24  
        'TP': 2442833.7219778746    # 1976-Feb-25.2219778746
        # period None; hyperbolic/parabolic; after ejection from the solar system
    }, 

    'McNaught': {                       # McNaught (C/2006 P1) 
        'a': -9074.061068728695,        # Horizons: A, semi-major axis in AU; hyperbolic/parabolic
        'e': 1.000018815882278,         # Horizons: EC, eccentricity
        'i': 77.83700054890942,         # Horizons: IN, inclination in degrees
        'omega': 155.9749681149126,     # Horizons: W, argument of perihelion in degrees
        'Omega': 267.4148026435385,     # Horizons: OM, longitude of ascending node in degrees; 
        'epoch': 2006-11-26,            # EPOCH=  2454065.5 ! 2006-Nov-26.0000000 (TDB)  
        'TP': 2454113.2988436329        # TP= 2007-Jan-12.7988436329
                                        # period None; hyperbolic/parabolic
    }, 

    'ATLAS': {                  # ATLAS (C/2024 G3)             
        # Rec #:90004845 (+COV) Soln.date: 2025-Apr-11_14:44:56    # obs: 299 (2024-2025)
        'a': -7606.45306976526,   # Horizons: A, semi-major axis in AU
        'e': 1.000012291218472,   # Horizons: EC, eccentricity
        'i': 116.8510954925091,      # Horizons: IN, inclination in degrees; retrograde > 90
        'omega': 108.1253732077035, # Horizons: W, argument of perihelion in degrees
        'Omega': 220.3320911080488,   # Horizons: OM, longitude of ascending node in degrees
        'epoch': '2024-Jun-19',
        'TP': 2460688.9243240277  # 2025-Jan-13.4243240277
    },

    'Tsuchinshan': {                    # Tsuchinshan-ATLAS (C/2023 A3)      2025-Oct-04 19:42:29             
        # Rec #:90004783 (+COV) Soln.date: 2025-Oct-03_14:42:16   # obs: 7228 (2022-2025)
        'a': -4088.071955049762,         # Horizons: A, semi-major axis in AU; hyperbolic; PER= 9.999999E99
        'e': 1.0000957494372,         # Horizons: EC, eccentricity
        'i': 139.1121557652439,         # Horizons: IN, inclination in degrees; retrograde > 90
        'omega': 308.491702255918,     # Horizons: W, argument of perihelion in degrees
        'Omega': 21.55947211343556,     # Horizons: OM, longitude of ascending node in degrees
        'epoch': '2024-May-16',
        'TP': 2460581.2407992561        # 2024-Sep-27.7407992561
    },

    'C/2025_K1': {                  # ATLAS (C/2025 K1)            2025-Jul-11 21:59:05 
        # Rec #:90004909 (+COV) Soln.date: 2025-Jul-10_13:42:09      # obs: 563 (93 days)
        'a': -1328.874007526048,   # Horizons: A, semi-major axis in AU
        'e': 1.000251464554613,   # Horizons: EC, eccentricity
        'i': 147.864867556013,      # Horizons: IN, inclination in degrees; retrograde > 90
        'omega': 271.0285208159306, # Horizons: W, argument of perihelion in degrees
        'Omega': 97.55648983040697,   # Horizons: OM, longitude of ascending node in degrees
        #     'C/2025_K1': 1e99,     # Parabolic comet - effectively infinite period
        # Next perihelion per current solutions is 2025-10-08; add JD+epoch.
        'epoch': '2025-10-08',
        'TP': 2460955.5  # 2025-10-08 00:00 UTC; replace with Horizons Tp for exact instant
        # 'C/2025_K1': 1e99,
    },

    'Borisov': {                  # Borisov (C/2025 V1)           2025-Nov-11 16:37:03 
        # Rec #:90004928 (+COV) Soln.date: 2025-Nov-05_13:13:07        # obs: 99 (7 days)
        'a': -48.28030957635523,   # Horizons: A, semi-major axis in AU
        'e': 1.009582732034413,   # Horizons: EC, eccentricity
        'i': 112.7242744491862,      # Horizons: IN, inclination in degrees; retrograde > 90
        'omega': 47.54446487656067, # Horizons: W, argument of perihelion in degrees
        'Omega': 91.89902555608872,   # Horizons: OM, longitude of ascending node in degrees
        #     'C/2025_V1': 1e99,     # Parabolic comet - effectively infinite period
        # Next perihelion per current solutions is 2025-Nov-16.5303735598; add JD+epoch.
        'epoch': '2025-11-03',
        'TP': 2460996.0303735598  # 2025-Nov-16.5303735598 UTC; replace with Horizons Tp for exact instant
    },

    # Interstellar objects; hyperbolic trajectories, object type 'trajectory'

    '1I/Oumuamua': {                   # 1I/'Oumuamua (A/2017 U1) 
        'a': -1.27234500742808,         # Horizons: A, semi-major axis in AU; Hyperbolic orbit
        'e': 1.201133796102373,         # Horizons: EC, eccentricity
        'i': 122.7417062847286,         # Horizons: IN, inclination in degrees; retrograde > 90
        'omega': 241.8105360304898,     # Horizons: W, argument of perihelion in degrees
        'Omega': 24.59690955523242,     # Horizons: OM, longitude of ascending node in degrees
        'epoch': '2017-11-23',          # EPOCH=  2458080.5 ! 2017-Nov-23.00 (TDB)
        'TP': 2458006.0073213754,       # Perihelion: 2017-Sep-09.5073213754
                                        # Hyperbolic orbit
    }, 

    '2I/Borisov': {                    # Borisov (C/2019 Q4) 
        'a': -.8514922551937886,        # Horizons: A, semi-major axis in AU; Hyperbolic orbit
        'e': 3.356475782676596,         # Horizons: EC, eccentricity
        'i': 44.05264247909138,         # Horizons: IN, inclination in degrees
        'omega': 209.1236864378081,     # Horizons: W, argument of perihelion in degrees
        'Omega': 308.1477292269942,     # Horizons: OM, longitude of ascending node in degrees;
        'epoch': '2020-1-5',            # EPOCH=  2458853.5 ! 2020-Jan-05.0000000 (TDB) 
        'TP': 2458826.052845906,        # Perihelion: 2019-Dec-08.5528459060
                                        # Hyperbolic orbit
    },

    '3I/ATLAS': {                      # heliocentric, ATLAS (C/2025 N1) 
        # 2025-Nov-17 00:00:00.0000 TDB   data arc: 2025-05-15 to 2025-11-13     Soln.date: 2025-Nov-13_12:56:43
        'a': -2.63886128382535E-01,        # Horizons: A, semi-major axis in AU; Hyperbolic orbit
        'e': 6.140504247361179E+00,         # Horizons: EC, eccentricity
        'i': 1.751131164859007E+02,         # Horizons: IN, inclination in degrees; retrograde > 90
        'omega': 1.279946584112738E+02,     # Horizons: W, argument of perihelion in degrees
        'Omega': 3.221578351010177E+02,     # Horizons: OM, longitude of ascending node in degrees;  
        'epoch': '2025-11-17',            # EPOCH=  2461001.5 ! 2025-Nov-17.0000000 (TDB)
        'TP': 2460977.974321826361,       # Time of perihelion (JD) 
        #     '3I/ATLAS': 1e99,         # Interstellar object - effectively infinite period
    },    

    # Satellites

    'Moon': {   # button; 301; Revised 7-31-2013, geocentric; source: https://ssd.jpl.nasa.gov/horizons/app.html#/
#        'a': 384400,   # Horizons: A, semi-major axis in AU
        'a': 0.002570,   # Horizons: A, semi-major axis in AU; 384400 km or 0.00257 au
        'e': 0.05490,   # Horizons: EC, eccentricity; 0.05490 was 0.0554
        'i': 5.145,      # Horizons: IN, inclination in degrees; 5.145 deg was 5.16
        'omega': 318.15, # Horizons: W, argument of perihelion in degrees
        'Omega': 125.08,   # Horizons: OM, longitude of ascending node in degrees
        'epoch': '2013-07-31'
        #     'Moon': 27.321582,
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
        #     'Phobos': 0.319,       # Verified from JPL
    },

    'Deimos': {             # 402; Revised: Sep 28, 2012
#        'a': 23500,       # semi-major axis in km; 23.4632(10^3)
        'a': 0.00015683,       # semi-major axis in AU; 0.00015683
#        'a_parent': 6.92,      # semi-major axis in Mars radii
        'e': 0.00033,          # eccentricity
        'i': 1.791,            # inclination to Mars' equator in degrees
        'omega': 0,      # argument of perihelion in degrees
        'Omega': 54.4       # longitude of ascending node in degrees
        #     'Deimos': 1.263,       # Verified from JPL
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
        #     'Io': 1.769,           # 42.456 hours
    },

    'Europa': {
#        'a': 671100,         # semi-major axis in km
        'a': 0.004486,         # semi-major axis in AU
    #    'a_parent': 9.40,      # semi-major axis in Jupiter radii
        'e': 0.0094,           # eccentricity
        'i': 0.471,            # inclination to Jupiter's equator in degrees
        'omega': 45.0,       # argument of perihelion in degrees
        'Omega': 184.0       # longitude of ascending node in degrees;  
        #     'Europa': 3.551,       # 85.224 hours
    },

    'Ganymede': {
#        'a': 1070400,         # semi-major axis in km
        'a': 0.007155,         # semi-major axis in AU
    #    'a_parent': 14.99,     # semi-major axis in Jupiter radii
        'e': 0.0013,           # eccentricity
        'i': 0.204,            # inclination to Jupiter's equator in degrees
        'omega': 198.3,      # argument of perihelion in degrees
        'Omega': 58.5        # longitude of ascending node in degrees
        #     'Ganymede': 7.155,     # 171.72 hours
    },

    'Callisto': {
#        'a': 1882700,         # semi-major axis in km
        'a': 0.012585,         # semi-major axis in AU
    #    'a_parent': 26.37,     # semi-major axis in Jupiter radii
        'e': 0.0074,           # eccentricity
        'i': 0.205,            # inclination to Jupiter's equator in degrees
        'omega': 43.8,       # argument of perihelion in degrees
        'Omega': 309.1       # longitude of ascending node in degrees;  
        #     'Callisto': 16.689,    # 400.536 hours
    },

# Jupiter's Inner Moons associated with ring system
    'Metis': {
        'a': 0.000856,         # semi-major axis in AU (128,000 km)
    #    'a_parent': 1.79,      # semi-major axis in Jupiter radii
        'e': 0.0002,           # eccentricity (nearly circular)
        'i': 0.06,             # inclination to Jupiter's equator in degrees
        'omega': 16.63,        # argument of perihelion in degrees
        'Omega': 68.9          # longitude of ascending node in degrees
        #     'Metis': 0.295,        # 7.08 hours
    },

    'Adrastea': {
        'a': 0.000864,         # semi-major axis in AU (129,000 km)
    #    'a_parent': 1.81,      # semi-major axis in Jupiter radii
        'e': 0.0015,           # eccentricity
        'i': 0.03,             # inclination to Jupiter's equator in degrees
        'omega': 234.0,        # argument of perihelion in degrees
        'Omega': 33.5          # longitude of ascending node in degrees
        #     'Adrastea': 0.298,     # 7.15 hours
    },

    'Amalthea': {
        'a': 0.001217,         # semi-major axis in AU (182,000 km)
    #    'a_parent': 2.54,      # semi-major axis in Jupiter radii
        'e': 0.0032,           # eccentricity
        'i': 0.374,            # inclination to Jupiter's equator in degrees
        'omega': 155.87,       # argument of perihelion in degrees
        'Omega': 108.05        # longitude of ascending node in degrees
        #     'Amalthea': 0.498,     # 11.95 hours
    },

    'Thebe': {
        'a': 0.001514,         # semi-major axis in AU (226,000 km)
    #    'a_parent': 3.11,      # semi-major axis in Jupiter radii
        'e': 0.0175,           # eccentricity
        'i': 1.076,            # inclination to Jupiter's equator in degrees
        'omega': 234.57,       # argument of perihelion in degrees
        'Omega': 237.33        # longitude of ascending node in degrees;  
        #     'Thebe': 0.675,        # 16.20 hours
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
        #     'Pan': 0.575,          # 13.80 hours
    },

    'Daphnis': {              # Revised: Aug 08, 2019; 635
#        'a': 136500,         # semi-major axis in km 136500 in https://ssd.jpl.nasa.gov/sats/elem/
        'a': 0.0009124,         # semi-major axis in AU
#        'a_parent': ,      # semi-major axis in Saturn radii
        'e': 0,           # eccentricity not defined in Horizons; 0 in https://ssd.jpl.nasa.gov/sats/elem/
        'i': 0,            # inclination to Saturn's equator in degrees not defined in Horizons; 0 in https://ssd.jpl.nasa.gov/sats/elem/
        'omega': 0,      # argument of perihelion in degrees; laplace; 0 in https://ssd.jpl.nasa.gov/sats/elem/
        'Omega': 0       # longitude of ascending node in degrees; 0 in https://ssd.jpl.nasa.gov/sats/elem/
        #     'Daphnis': 0.594,      # 14.26 hours
    },

    'Prometheus': {              # Revised: Oct 03, 2018; 616
#        'a': 139350,         # semi-major axis in km 139.35 (10^3) in https://ssd.jpl.nasa.gov/horizons/app.html#/
        'a': 0.0009315,         # semi-major axis in AU; Orbital period 0.612986 d
#        'a_parent': ,      # semi-major axis in Saturn radii
        'e': 0.0024,           # eccentricity in https://ssd.jpl.nasa.gov/horizons/app.html#/
        'i': 0,            # inclination to Saturn's equator in degrees in Horizons; in https://ssd.jpl.nasa.gov/horizons/app.html#/
        'omega': 341.9,      # argument of perihelion in degrees; laplace; in https://ssd.jpl.nasa.gov/sats/elem/
        'Omega': 0       # longitude of ascending node in degrees; 0 in https://ssd.jpl.nasa.gov/sats/elem/
        #     'Prometheus': 0.616,   # 14.78 hours
    },

    'Pandora': {              # Revised: Oct 03, 2018; 617
#        'a': 141700,         # semi-major axis in km 141.70 (10^3) in https://ssd.jpl.nasa.gov/horizons/app.html#/
        'a': 0.0009472,         # semi-major axis in AU; Orbital period 0.628804 d
#        'a_parent': ,      # semi-major axis in Saturn radii
        'e': 0.0042,           # eccentricity in https://ssd.jpl.nasa.gov/horizons/app.html#/
        'i': 0,            # inclination to Saturn's equator in degrees in Horizons; in https://ssd.jpl.nasa.gov/horizons/app.html#/
        'omega': 217.9,      # argument of perihelion in degrees; laplace; in https://ssd.jpl.nasa.gov/sats/elem/
        'Omega': 0       # longitude of ascending node in degrees; 0 in https://ssd.jpl.nasa.gov/sats/elem/
        #     'Pandora': 0.631,      # 15.14 hours
    },

    'Mimas': {              # revised 1-26-2022; 601
#        'a': 185540,         # semi-major axis in km
        'a': 0.001242,         # semi-major axis in AU
#        'a_parent': 3.08,      # semi-major axis in Saturn radii
        'e': 0.0196,           # eccentricity
        'i': 1.572,            # inclination to Saturn's equator in degrees
        'omega': 160.4,      # argument of perihelion in degrees; laplace
        'Omega': 66.2       # longitude of ascending node in degrees
        #     'Mimas': 0.942,        # 22.61 hours
    },

    'Enceladus': {          # 602
#        'a': 238400,         # semi-major axis in km
        'a': 0.001587,         # semi-major axis in AU
#        'a_parent': 3.95,      # semi-major axis in Saturn radii
        'e': 0.0047,           # eccentricity
        'i': 0.009,            # inclination to Saturn's equator in degrees
        'omega': 119.5,      # argument of perihelion in degrees
        'Omega': 0.0       # longitude of ascending node in degrees
        #     'Enceladus': 1.370,    # 32.88 hours
    },

    'Tethys': {             # 603
#        'a': 295000,         # semi-major axis in km
        'a': 0.001970,         # semi-major axis in AU
#        'a_parent': 4.89,      # semi-major axis in Saturn radii
        'e': 0.001,           # eccentricity
        'i': 1.091,            # inclination to Saturn's equator in degrees
        'omega': 335.3,      # argument of perihelion in degrees
        'Omega': 273.0       # longitude of ascending node in degrees;  
        #     'Tethys': 1.888,       # 45.31 hours
    },

    'Dione': {              # 604
#        'a': 377700,         # semi-major axis in km
        'a': 0.002525,         # semi-major axis in AU
#        'a_parent': 6.26,      # semi-major axis in Saturn radii
        'e': 0.0022,           # eccentricity
        'i': 0.0,            # inclination to Saturn's equator in degrees
        'omega': 116.0,      # argument of perihelion in degrees
        'Omega': 0.0       # longitude of ascending node in degrees
        #     'Dione': 2.737,        # 65.69 hours
    },

    'Rhea': {               # 605
#        'a': 527200,         # semi-major axis in km
        'a': 0.003524,         # semi-major axis in AU
#        'a_parent': 8.74,      # semi-major axis in Saturn radii
        'e': 0.0010,           # eccentricity
        'i': 0.333,            # inclination to Saturn's equator in degrees
        'omega': 44.3,      # argument of perihelion in degrees
        'Omega': 133.7       # longitude of ascending node in degrees
        #     'Rhea': 4.518,         # 108.43 hours
    },

    'Titan': {              # 606
#        'a': 1221900,         # semi-major axis in km
        'a': 0.008168,         # semi-major axis in AU
#        'a_parent': 20.27,     # semi-major axis in Saturn radii
        'e': 0.0288,           # eccentricity
        'i': 0.306,            # inclination to Saturn's equator in degrees
        'omega': 78.3,      # argument of perihelion in degrees
        'Omega': 78.6        # longitude of ascending node in degrees
        #     'Titan': 15.945,       # 382.68 hours
    },

    'Hyperion': {              # 607; Revised: Jan 26, 2022; Orbital period 21.28 d
#        'a': 1500933,         # semi-major axis in km; 1500.933(10^3); https://ssd.jpl.nasa.gov/horizons/app.html#/
        'a': 0.010033,         # semi-major axis in AU
#        'a_parent': ,     # semi-major axis in Saturn radii
        'e': 0.0232,           # eccentricity; https://ssd.jpl.nasa.gov/horizons/app.html#/
        'i': 0.615,            # inclination to Saturn's equator in degrees; https://ssd.jpl.nasa.gov/horizons/app.html#/
        'omega': 214.0,      # argument of perihelion in degrees; https://ssd.jpl.nasa.gov/sats/elem/
        'Omega': 87.1        # longitude of ascending node in degrees; https://ssd.jpl.nasa.gov/sats/elem/
        #     'Hyperion': 21.277,    # 510.65 hours
    },

    'Iapetus': {              # 608; Revised: Jan 26, 2022; Orbital period 79.33 d
#        'a': 3560840,         # semi-major axis in km; 3560.84 (10^3); https://ssd.jpl.nasa.gov/horizons/app.html#/
        'a': 0.02380,         # semi-major axis in AU
#        'a_parent': ,     # semi-major axis in Saturn radii
        'e': 0.0283,           # eccentricity; https://ssd.jpl.nasa.gov/horizons/app.html#/
        'i': 7.489,            # inclination to Saturn's equator in degrees; https://ssd.jpl.nasa.gov/horizons/app.html#/
        'omega': 254.5,      # argument of perihelion in degrees; https://ssd.jpl.nasa.gov/sats/elem/
        'Omega': 86.5        # longitude of ascending node in degrees; https://ssd.jpl.nasa.gov/sats/elem/
        #     'Iapetus': 79.331,     # 1903.94 hours
    },

    'Phoebe': {             # 609;  Revised: Jan 26, 2022 Phoebe / (Saturn) 609; Orbital period = 550.31 d
#        'a': 12947780,          # semi-major axis in km; Semi-major axis, a (km)= 12947.78(10^3) 
        'a': 0.08655,          # semi-major axis in AU
#        'a_parent': 214.7,     # semi-major axis in Saturn radii
        'e': 0.1635,           # eccentricity
        'i': 175.986,            # inclination to Saturn's equator in degrees; retrograde > 90
        'omega': 240.3,      # argument of perihelion in degrees
        'Omega': 192.7        # longitude of ascending node in degrees;  
        #     'Phoebe': 550.56,      # 1.51 years
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
        #     'Miranda': 1.413,      # 33.91 hours
    },

    'Ariel': {              # 701
#        'a': 190900,         # semi-major axis in km
        'a': 0.001276,         # semi-major axis in AU
#        'a_parent': 7.35,      # semi-major axis in Uranus radii
        'e': 0.0012,           # eccentricity
        'i': 0.0,            # inclination to Uranus's equator in degrees
        'omega': 83.3,      # argument of perihelion in degrees
        'Omega': 0.0        # longitude of ascending node in degrees
        #     'Ariel': 2.520,        # 60.48 hours
    },

    'Umbriel': {            # 702
#        'a': 266000,         # semi-major axis in km
        'a': 0.001778,         # semi-major axis in AU
#        'a_parent': 10.23,     # semi-major axis in Uranus radii
        'e': 0.0039,           # eccentricity
        'i': 0.1,            # inclination to Uranus's equator in degrees
        'omega': 157.5,       # argument of perihelion in degrees
        'Omega': 195.5        # longitude of ascending node in degrees;   
        #     'Umbriel': 4.144,      # 99.46 hours
    },

    'Titania': {            # 703
#        'a': 436300,         # semi-major axis in km
        'a': 0.002914,         # semi-major axis in AU
#        'a_parent': 16.77,     # semi-major axis in Uranus radii
        'e': 0.001,           # eccentricity
        'i': 0.1,            # inclination to Uranus's equator in degrees
        'omega': 202.0,      # argument of perihelion in degrees
        'Omega': 26.4        # longitude of ascending node in degrees
        #     'Titania': 8.706,      # 208.94 hours
    },

    'Oberon': {             # 704
#       'a': 583400,         # semi-major axis in km
        'a': 0.003907,         # semi-major axis in AU
#        'a_parent': 22.47,     # semi-major axis in Uranus radii
        'e': 0.0008,           # eccentricity
        'i': 0.058,            # inclination to Uranus's equator in degrees
        'omega': 182.4,      # argument of perihelion in degrees
        'Omega': 30.5       # longitude of ascending node in degrees
        #     'Oberon': 13.463,      # 323.11 hours
    },

     'Portia': {             # 712
#       'a': 66100,         # semi-major axis in km
        'a': 0.0004419,         # semi-major axis in AU
#        'a_parent': ,     # semi-major axis in Uranus radii
        'e': 0.000,           # eccentricity
        'i': 0.0,            # inclination to Uranus's equator in degrees
        'omega': 0,      # argument of perihelion in degrees
        'Omega': 0       # longitude of ascending node in degrees
        #     'Portia': 0.513,       # 12.31 hours
    },   

     'Mab': {             # 726
#       'a': 97700,         # semi-major axis in km
        'a': 0.0006531,         # semi-major axis in AU
#        'a_parent': ,     # semi-major axis in Uranus radii
        'e': 0.003,           # eccentricity
        'i': 0.1,            # inclination to Uranus's equator in degrees
        'omega': 237.9,      # argument of perihelion in degrees
        'Omega': 188.2       # longitude of ascending node in degrees;  
        #     'Mab': 0.923,          # 22.15 hours
    },    

    # Neptune's Major Moon
    'Triton': {             # 801
#        'a': 354800,         # semi-major axis in km
        'a': 0.002371,         # semi-major axis in AU
#        'a_parent': 14.33,     # semi-major axis in Neptune radii
        'e': 0.000016,         # eccentricity (nearly circular)
        'i': 157.3,          # inclination to Neptune's equator in degrees; retrograde > 90
        'omega': 0.0,       # argument of perihelion in degrees
        'Omega': 178.1       # longitude of ascending node in degrees
        #     'Triton': 5.877,       # 141.05 hours (retrograde)
    },

    'Despina': {             # 805
#        'a': 52500,         # semi-major axis in km
        'a': 0.0003509,         # semi-major axis in AU
#        'a_parent': ,     # semi-major axis in Neptune radii
        'e': 0.000,         # eccentricity (nearly circular)
        'i': 0.0,          # inclination to Neptune's equator in degrees
        'omega': 0.0,       # argument of perihelion in degrees
        'Omega': 0.0       # longitude of ascending node in degrees
        #     'Despina': 0.335,      # 8.04 hours
    },

    'Galatea': {             # 806
#        'a': 62000,         # semi-major axis in km
        'a': 0.0004144,         # semi-major axis in AU
#        'a_parent': ,     # semi-major axis in Neptune radii
        'e': 0.000,         # eccentricity (nearly circular)
        'i': 0.0,          # inclination to Neptune's equator in degrees
        'omega': 0.0,       # argument of perihelion in degrees
        'Omega': 0.0       # longitude of ascending node in degrees
        #     'Galatea': 0.429,      # 10.30 hours
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
        #     'Charon': 6.387,       # 153.29 hours
    },

    'Styx': {              # 905; revised 4-3-2024; Fit to post New Horizons encounter and Gaia data through 2023.
#        'a': 43200,         # semi-major axis in km
        'a': 0.00028877,         # semi-major axis in AU; 0.00043583
#        'a_parent': ,     # semi-major axis in Pluto radii
        'e': 0.025,           # eccentricity
        'i': 0.0,            # inclination to Pluto's equator in degrees
        'omega': 322.5,      # argument of perihelion in degrees
        'Omega': 0.0       # longitude of ascending node in degrees
        #     'Styx': 20.162,        # 483.89 hours
    },    

    'Nix': {                # 902; revised 4/3/2024 post-New Horizons
#        'a': 49300,         # semi-major axis in km
        'a': 0.00032955,         # semi-major axis in AU
#        'a_parent': 31.3,      # semi-major axis in Pluto radii
        'e': 0.025,           # eccentricity
        'i': 0.0,            # inclination to Pluto's equator in degrees
        'omega': 31.4,      # argument of perihelion in degrees
        'Omega': 0.0         # longitude of ascending node in degrees
        #     'Nix': 24.856,         # 596.54 hours
    },
    'Kerberos': {              # 904; revised 4-3-2024; Fit to post New Horizons encounter and Gaia data through 2023.
#        'a': 58300,         # semi-major axis in km
        'a': 0.00038971,         # semi-major axis in AU; 0.00043583
#        'a_parent': ,     # semi-major axis in Pluto radii
        'e': 0.010,           # eccentricity
        'i': 0.4,            # inclination to Pluto's equator in degrees
        'omega': 32.1,      # argument of perihelion in degrees
        'Omega': 314.3       # longitude of ascending node in degrees;  
        #     'Kerberos': 32.168,    # 772.03 hours
    },   

    'Hydra': {              # 903; revised 4-3-2024; Fit to post New Horizons encounter and Gaia data through 2023.
#        'a': 65200,         # semi-major axis in km
        'a': 0.00043584,         # semi-major axis in AU; 0.00043583
#        'a_parent': 83.9,     # semi-major axis in Pluto radii
        'e': 0.009,           # eccentricity
        'i': 0.3,            # inclination to Pluto's equator in degrees
        'omega': 139.3,      # argument of perihelion in degrees
        'Omega': 114.3       # longitude of ascending node in degrees
        #     'Hydra': 38.202,       # 916.85 hours
    },

    # Eris's Moon
#    'Dysnomia': {
#        'a': 0.000364,         # semi-major axis in km
#        'a': 0.000364,         # semi-major axis in AU
#        'a_parent': 36.2,      # semi-major axis in Eris radii (estimate)
#        'e': 0.0062,           # eccentricity
#        'i': 78.29,            # inclination in degrees (to the ecliptic)
#        'omega': 139.65,       # argument of perihelion in degrees
#        'Omega': 29.43         # longitude of ascending node in degrees
        #     'Dysnomia': 15.786,    # 378.86 hours
#    },

    'Dysnomia': {
        'a': 0.000249,         # semi-major axis in AU (37,300 km)
        'e': 0.0062,           # eccentricity
        'i': 78.29,            # inclination in degrees (to Eris heliocentric orbit)
        'omega': 139.65,       # argument of periapsis in degrees
        'Omega': 29.43,        # longitude of ascending node in degrees
        'orbital_period_days': 15.786,  # 378.86 hours
    },    

    # Haumea's Moons
    "Hi'iaka": {
        'a': 0.0003246,        # semi-major axis in AU (~49,500 km)
        'e': 0.0513,           # eccentricity
        'i': 126.356,          # inclination in degrees (to ecliptic)
        'omega': 154.1,        # argument of periapsis in degrees
        'Omega': 206.766,      # longitude of ascending node in degrees
        'orbital_period_days': 49.12,
    },

    'Namaka': {
        'a': 0.0001652,        # semi-major axis in AU (~25,657 km)
        'e': 0.249,            # eccentricity (highly elliptical)
        'i': 113.013,          # inclination in degrees (to ecliptic)
        'omega': 178.9,        # argument of periapsis in degrees
        'Omega': 205.016,      # longitude of ascending node in degrees
        'orbital_period_days': 18.28,
        # Note: Namaka's orbit is non-Keplerian due to Hi'iaka perturbations
    },

# Makemake's Moon
    'MK2': {
        'a': 0.0001487,        # semi-major axis in AU (22,250 km ± 780 km)
        'e': 0.0,              # eccentricity (best fit is circular)
        'i': 74.0,             # inclination to ecliptic in degrees (63°-87° range, uncertain)
        'omega': 0.0,          # argument of periapsis (undefined for circular orbit)
        'Omega': 0.0,          # longitude of ascending node (unknown - edge-on to Earth)
        'orbital_period_days': 18.023,  # ± 0.017 days
        # Source: arXiv:2509.05880 (Sept 2025) - preliminary Hubble analysis
        # Note: Orbit is edge-on to Earth (83.7° ± 1.0° relative to line of sight)
        # JPL Horizons has no satellite ephemeris for MK2 as of late 2025
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
    'Pluto-Charon Barycenter': ['Pluto', 'Charon', 'Styx', 'Nix', 'Kerberos', 'Hydra'],  # Binary planet mode
    'Eris': ['Dysnomia'],
    'Haumea': ["Hi'iaka", 'Namaka'],
    'Makemake': ['MK2']
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