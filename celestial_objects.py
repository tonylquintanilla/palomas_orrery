"""
Paloma's Orrery - Celestial Objects Data Module

This module contains all celestial object definitions separated from the GUI code.
The data-only structure allows the GUI (palomas_orrery.py) to remain cleaner.

Usage in palomas_orrery.py:
    from celestial_objects import OBJECT_DEFINITIONS, build_objects_list
    objects = build_objects_list(OBJECT_DEFINITIONS, vars_dict, color_map)
"""

from datetime import datetime


OBJECT_DEFINITIONS = [
    # Existing Celestial Objects
    {'name': 'Sun', 'id': '10', 'var_name': 'sun_var', 'color_key': 'Sun', 'symbol': 'circle', 'object_type': 'fixed', 
    'id_type': None, 
    'mission_info': 'Horizons: 10. NASA: "The Sun\'s gravity holds the solar system together, keeping everything in its orbit. "', 
    'mission_url': 'https://science.nasa.gov/sun/'},

    {'name': 'Mercury', 'id': '199', 'var_name': 'mercury_var', 'color_key': 'Mercury', 'symbol': 'circle', 'object_type': 'orbital', 
    'id_type': None, 
    'mission_info': 'Horizons: 199. NASA: "Mercury is the smallest planet in our solar system and the nearest to the Sun."', 
    'mission_url': 'https://science.nasa.gov/mercury/'},

    {'name': 'Venus', 'id': '299', 'var_name': 'venus_var', 'color_key': 'Venus', 'symbol': 'circle', 'object_type': 'orbital', 
    'id_type': None, 
    'mission_info': 'Horizons: 299. NASA: "Venus is the second planet from the Sun, and the sixth largest planet. It\'s the hottest planet in our solar system."', 
    'mission_url': 'https://science.nasa.gov/venus/'},

    {'name': 'Earth', 'id': '399', 'var_name': 'earth_var', 'color_key': 'Earth', 'symbol': 'circle', 'object_type': 'orbital', 
    'id_type': None, 
    'mission_info': 'Horizons: 399. Earth orbital period: 27.32 days.', 
     'mission_url': 'https://science.nasa.gov/earth/', 'mission_info': 'Our home planet.'},

    {'name': 'Moon', 'id': '301', 'var_name': 'moon_var', 'color_key': 'Moon', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 301. Earth orbital period: 27.32 days.', 
     'mission_url': 'https://science.nasa.gov/moon/', 'mission_info': 'NASA: "The Moon rotates exactly once each time it orbits our planet."'},

    # Earth-Moon Barycenter - highest mass ratio of any PLANET-moon system (1.23%)
    # Barycenter is INSIDE Earth (~4,670 km from center, ~1,700 km below surface)
    # JPL Horizons ID: 3 (Earth-Moon system barycenter)
    {'name': 'Earth-Moon Barycenter', 'id': '3', 'var_name': 'earth_moon_barycenter_var',
     'color_key': 'Earth', 'symbol': 'square-open', 'object_type': 'barycenter',
     'mission_info': 'Center of mass for the Earth-Moon system. Period: 27.32 days. Highest mass ratio (1.23%) of any planet-moon system!'},

    {'name': 'Mars', 'id': '499', 'var_name': 'mars_var', 'color_key': 'Mars', 'symbol': 'circle', 'object_type': 'orbital', 
    'id_type': None, 
    'mission_info': 'Horizons: 499. NASA: "Mars is one of the easiest planets to spot in the night sky -- it looks like a bright red point of light."', 
    'mission_url': 'https://science.nasa.gov/?search=mars'},

    {'name': 'Jupiter', 'id': '599', 'var_name': 'jupiter_var', 'color_key': 'Jupiter', 'symbol': 'circle', 'object_type': 'orbital', 
    'id_type': None, 
    'mission_info': 'Horizons: 599. NASA: "Jupiter is the largest and oldest planet in our solar system."', 
    'mission_url': 'https://science.nasa.gov/?search=Jupiter'},

    # Trojan Asteroids
    # Lucy L4 Trojan Targets (Leading Jupiter Trojans)
    # All have center_id to enable asteroid-centered flyby visualization
    
    {'name': 'Eurybates', 'id': '1973 SO', 'var_name': 'eurybates_var', 'color_key': 'Eurybates', 'symbol': 'circle-open', 'object_type': 'orbital', 
    'id_type': 'smallbody',
    'center_id': '920003548',  # Numeric ID for use as Horizons center (3548 Eurybates)
    'mission_info': 'Lucy flyby: Aug 12, 2027. D~64 km, C-type. Has satellite Queta (~1 km). First C-type Trojan to be visited.', 
    'mission_url': 'https://lucy.swri.edu/Eurybates.html'},

    # Patroclus-Menoetius Binary System (Lucy Mission target - flyby March 2, 2033)
    # Source: JPL Horizons satellite solution (JPL#82), Brozovic et al. 2024 (AJ 167:104)
    # Binary parameters: a=692.5 km, P=4.283 days, mass ratio ~78%/22%, density 0.88 g/cm3
    
    {'name': 'Patroclus-Menoetius Barycenter', 'id': '20000617', 'var_name': 'patroclus_barycenter_var',
     'color_key': 'Patroclus', 'symbol': 'square-open', 'object_type': 'barycenter',
     'id_type': 'majorbody',
     'start_date': datetime(2000, 1, 1, 12, 0), 'end_date': datetime(2050, 12, 1, 0, 0),
     'mission_info': 'Center of mass for Patroclus-Menoetius binary Trojan system. Lucy flyby: March 3, 2033.',
     'mission_info': 'System barycenter. First known binary Jupiter Trojan. Evidence suggests primordial formation ~4.5 Gyr ago.',
     'mission_url': 'https://lucy.swri.edu/targets/Patroclus-Menoetius.html'},

    {'name': 'Patroclus', 'id': '920000617', 'var_name': 'patroclus_var', 'color_key': 'Patroclus', 
     'symbol': 'circle-open', 'object_type': 'orbital',  # Changed to satellite - orbits barycenter
     'id_type': 'majorbody',
     'helio_id': 'A906 UL',           # For Sun-centered plots (smallbody solution)
     'helio_id_type': 'smallbody',
     'center_id': '920000617',  # Patroclus body center (for Lucy trajectory)
     'start_date': datetime(2000, 1, 1, 12, 0), 'end_date': datetime(2050, 12, 1, 0, 0),
     'mission_info': 'Primary body of binary Trojan. D=113 km. Binary period: 4.28 days. Lucy flyby: March 3, 2033.',
     'mission_url': 'https://lucy.swri.edu/targets/Patroclus-Menoetius.html'},

    {'name': 'Menoetius', 'id': '120000617', 'var_name': 'menoetius_var', 'color_key': 'Menoetius', 
     'symbol': 'circle-open', 'object_type': 'orbital',
     'id_type': 'majorbody',
     'center_id': '120000617',  # Menoetius body center (for Lucy trajectory)
     'start_date': datetime(2000, 1, 1, 12, 0), 'end_date': datetime(2050, 12, 1, 0, 0),
     'mission_info': 'Secondary body of binary Trojan. D=104 km. Binary period: 4.28 days. Named for Patroclus\'s father.',
     'mission_url': 'https://lucy.swri.edu/targets/Patroclus-Menoetius.html'},   

    {'name': 'Polymele', 'id': '1999 WB2', 'var_name': 'polymele_var', 'color_key': 'Polymele', 'symbol': 'circle-open', 'object_type': 'orbital', 
    'id_type': 'smallbody',
    'center_id': '920015094',  # Numeric ID for use as Horizons center (15094 Polymele)
    'mission_info': 'Lucy flyby: Sep 15, 2027. D~21 km, P-type. Has satellite Shaun (~5 km, discovered 2022 via occultation).', 
    'mission_url': 'https://lucy.swri.edu/Polymele.html'},

    {'name': 'Leucus', 'id': '1997 TS25', 'var_name': 'leucus_var', 'color_key': 'Leucus', 'symbol': 'circle-open', 'object_type': 'orbital', 
    'id_type': 'smallbody',
    'center_id': '20011351',  # Numeric ID for use as Horizons center (11351 Leucus)
    'mission_info': 'Lucy flyby: Apr 18, 2028. D~40 km, D-type. Extremely slow rotator (~446 hours). Dark, primitive surface.', 
    'mission_url': 'https://lucy.swri.edu/Leucus.html'},

    {'name': 'Orus', 'id': '1999 VQ10', 'var_name': 'orus_var', 'color_key': 'Orus', 'symbol': 'circle-open', 'object_type': 'orbital', 
    'id_type': 'smallbody',
    'center_id': '20021900',  # Numeric ID for use as Horizons center (21900 Orus)
    'mission_info': 'Lucy flyby: Nov 11, 2028. D~51 km, D-type. Last L4 Trojan visit before heading to L5.', 
    'mission_url': 'https://lucy.swri.edu/Orus.html'},

    {'name': 'Saturn', 'id': '699', 'var_name': 'saturn_var', 'color_key': 'Saturn', 'symbol': 'circle', 'object_type': 'orbital', 
    'id_type': None, 
    'mission_info': 'Horizons: 699. NASA: "Saturn is the sixth planet from the Sun and the second largest planet in our solar system."', 
    'mission_url': 'https://science.nasa.gov/saturn/'},

    {'name': 'Uranus', 'id': '799', 'var_name': 'uranus_var', 'color_key': 'Uranus', 'symbol': 'circle', 'object_type': 'orbital', 
    'id_type': None, 
    'mission_info': 'Horizons: 799. NASA: "Uranus is the seventh planet from the Sun, and the third largest planet in our solar system -- about four times wider than Earth."', 
    'mission_url': 'https://science.nasa.gov/uranus/'},

    {'name': 'Neptune', 'id': '899', 'var_name': 'neptune_var', 'color_key': 'Neptune', 'symbol': 'circle', 'object_type': 'orbital', 
    'id_type': None, 
    'mission_info': 'Horizons: 899. NASA: "Dark, cold and whipped by supersonic winds, giant Neptune is the eighth and most distant major planet orbiting our Sun."', 
    'mission_url': 'https://science.nasa.gov/neptune/'},

    {'name': 'Planet 9', 'id': 'planet9_placeholder', 'var_name': 'planet9_var', 'color_key': 'orbital', 
    'symbol': 'circle', 'object_type': 'hypothetical', 
    'id_type': None, 
    'mission_info': 'Hypothetical planet with estimated mass of 5-10 Earths at ~400-800 AU. Not yet directly observed. Visualization is our estimate and not from JPL Horizons.',
    'mission_url': 'https://en.wikipedia.org/wiki/Planet_Nine'},

# Centaurs asteroids

    {'name': 'Chariklo', 'id': '1997 CU26', 'var_name': 'chariklo_var', 'color_key': 'Chariklo', 'symbol': 'circle-open', 'object_type': 'orbital', 
    'id_type': 'smallbody', 
    'mission_info': 'Horizons: 1997 CU26. Large Centaur. Retrograde (left-handed) orbit.', 
    'mission_url': 'https://science.nasa.gov/solar-system/asteroids/10199-chariklo/'},

# Dwarf planets

# Original Pluto (keep as-is)
    {'name': 'Pluto', 'id': '999', 'var_name': 'pluto_var', 
     'color_key': 'Pluto', 'symbol': 'circle', 'object_type': 'orbital', 
     'id_type': None, 
     'mission_info': 'Horizons: 999. Dwarf planet in the Kuiper Belt. Barycentric period: 6.39 days (orbits Pluto-Charon center of mass with Charon).', 
     'mission_url': 'https://science.nasa.gov/dwarf-planets/pluto/'},

    # NEW: Pluto-Charon Barycenter
    {'name': 'Pluto-Charon Barycenter', 'id': '9', 'var_name': 'pluto_barycenter_var', 
     'color_key': 'Pluto', 'symbol': 'square-open', 'object_type': 'barycenter',
     'mission_info': 'Center of mass for Pluto-Charon binary planet system. System period: 6.39 days.'},

    {'name': 'Ceres', 'id': 'A801 AA', 'var_name': 'ceres_var', 'color_key': 'Ceres', 'symbol': 'circle', 'object_type': 'orbital', 
    'id_type': 'smallbody', 
    'center_id': '2000001',  # Numeric ID for use as Horizons center    
    'mission_info': 'Horizons: A801 AA. NASA: "Ceres was the first object discovered in the main asteroid belt. Dawn spacecraft orbited Ceres from 2015 to 2018."', 
    'mission_url': 'https://science.nasa.gov/mission/dawn/science/ceres/'},

#    {'name': 'Haumea', 'id': '2003 EL61', 'var_name': 'haumea_var', 'color_key': 'Haumea', 'symbol': 'circle', 'object_type': 'orbital', 
#    'id_type': 'smallbody', 
#    'mission_info': 'Horizons: 2003 EL61. Haumea is an oval-shaped dwarf planet that is one of the fastest rotating large objects in our solar system.', 
#    'mission_url': 'https://science.nasa.gov/dwarf-planets/haumea/'},

    # Haumea System (136108 Haumea) - has 2 moons
    # Pattern: Barycenter 20XXXXXX, Primary 920XXXXXX, First moon 120XXXXXX, Second moon 220XXXXXX
#    {'name': 'Haumea System Barycenter', 'id': '20136108', 'var_name': 'haumea_barycenter_var',
#     'color_key': 'Haumea', 'symbol': 'square-open', 'object_type': 'barycenter',
#     'id_type': 'majorbody',
#     'mission_info': 'Center of mass for Haumea triple system. Moon periods: Hi\'iaka 49 days, Namaka 18 days.'},

    {'name': 'Haumea', 'id': '920136108', 'var_name': 'haumea_var', 
    'color_key': 'Haumea', 'symbol': 'circle', 'object_type': 'orbital', 
    'id_type': 'majorbody',
    'helio_id': '2003 EL61',  # For Sun-centered plots (smallbody solution)
    'helio_id_type': 'smallbody',
    'center_id': '920136108',  # Haumea body center (for centered views)
    'mission_info': 'Horizons: 136108 Haumea. Egg-shaped dwarf planet with rings. Moon periods: Hi\'iaka 49 days, Namaka 18 days. Rotation: 3.9 hours.', 
    'mission_url': 'https://science.nasa.gov/dwarf-planets/haumea/'},    

    # Eris-Dysnomia Binary System (136199 Eris)
    # Pattern: Barycenter 20XXXXXX, Primary 920XXXXXX, Secondary 120XXXXXX
#    {'name': 'Eris-Dysnomia Barycenter', 'id': '20136199', 'var_name': 'eris_barycenter_var',
#     'color_key': 'Eris', 'symbol': 'square-open', 'object_type': 'barycenter',
#     'id_type': 'majorbody',
#     'mission_info': 'Center of mass for Eris-Dysnomia system. Binary period: 15.79 days.'},

    {'name': 'Eris', 'id': '920136199', 'var_name': 'eris_var', 'color_key': 'Eris', 'symbol': 'circle', 'object_type': 'orbital', 
    'id_type': 'majorbody',
    'helio_id': '2003 UB313',  # For Sun-centered plots (smallbody solution)
    'helio_id_type': 'smallbody',
    'center_id': '920136199',  # Eris body center (for centered views)
    'mission_info': 'Horizons: 136199 Eris. Most massive dwarf planet (27% more than Pluto). Binary period with Dysnomia: 15.79 days.', 
    'mission_url': 'https://science.nasa.gov/dwarf-planets/eris/'},

#    {'name': 'Eris/Dysnomia', 'id': '20136199', 'var_name': 'eris2_var', 'color_key': 'Eris', 'symbol': 'circle', 'object_type': 'satellite', 
    # 20136199 satellite solution (required for Eris centered plots) 
#    'id_type': 'smallbody', 
#    'mission_info': 'Eris is a dwarf planet about the same size as Pluto, but it\'s three times farther from the Sun.', 
#    'mission_url': 'https://science.nasa.gov/dwarf-planets/eris/'},

    # Gonggong-Xiangliu Binary System (225088 Gonggong)
    # Pattern: Barycenter 20XXXXXX, Primary 920XXXXXX, Secondary 120XXXXXX
    # NOTE: Gonggong-Xiangliu Barycenter removed - mass ratio ~0.013 means barycenter is
    # only ~312 km from Gonggong's center (inside the ~615 km body). Not visually meaningful.
    # Use Gonggong-centered mode instead (Xiangliu orbiting Gonggong).
    # {'name': 'Gonggong-Xiangliu Barycenter', 'id': '20225088', 'var_name': 'gonggong_barycenter_var',
    #  'color_key': 'Gonggong', 'symbol': 'square-open', 'object_type': 'barycenter',
    #  'id_type': 'majorbody',
    #  'mission_info': 'Center of mass for Gonggong-Xiangliu system. Binary period: 25.22 days.'},

    {'name': 'Gonggong', 'id': '920225088', 'var_name': 'gonggong_var', 'color_key': 'Gonggong', 'symbol': 'circle', 'object_type': 'orbital', 
    'id_type': 'majorbody',
    'helio_id': '2007 OR10',  # For Sun-centered plots (smallbody solution)
    'helio_id_type': 'smallbody',
    'center_id': '920225088',  # Gonggong body center (for centered views)
    'mission_info': 'Horizons: 225088 Gonggong. Dwarf planet with highly inclined orbit. Binary period with Xiangliu: 25.22 days.', 
    'mission_url': 'https://en.wikipedia.org/wiki/Gonggong_(dwarf_planet)'},

    {'name': 'Makemake', 'id': '20136472', 'var_name': 'makemake_var', 'color_key': 'Makemake', 'symbol': 'circle', 'object_type': 'orbital', 
    'id_type': 'majorbody',
    'helio_id': '2005 FY9',  # For Sun-centered plots; 
    'mission_info': 'Horizons: 2005 FY9. Makemake is a dwarf planet slightly smaller than Pluto, and is the second-brightest object in the Kuiper Belt.', 
    'mission_url': 'https://science.nasa.gov/dwarf-planets/makemake/'},

#    Note: JPL has no satellite ephemeris for Makemake yet (MK2 discovered 2015)
#    {'name': 'Makemake', 'id': '20136472', 'var_name': 'makemake_var', 'color_key': 'Makemake', 'symbol': 'circle', 'object_type': 'orbital', 
#    'id_type': 'majorbody',
#    'helio_id': '2005 FY9',  # For Sun-centered plots
#    'mission_info': 'Horizons: 136472 Makemake. Second-brightest Kuiper Belt object. Has one known moon (MK2).', 
#    'mission_url': 'https://science.nasa.gov/dwarf-planets/makemake/'},    

    {'name': 'Mani', 'id': '2002 MS4', 'var_name': 'ms4_var', 'color_key': 'MS4', 'symbol': 'circle', 'object_type': 'orbital', 
    'id_type': 'smallbody', 
    'mission_info': 'Horizons: 2002 MS4. One of the largest unnumbered Kuiper Belt Objects with no known moons.', 
    'mission_url': 'https://www.minorplanetcenter.net/db_search/show_object?object_id=2002+MS4'},

    {'name': 'Orcus', 'id': '920090482', 'var_name': 'orcus_var', 'color_key': 'Orcus', 'symbol': 'circle', 'object_type': 'orbital', 
    'center_id': '920090482', # PRIMARY body ID for use as Horizons center (not small body designation)
    'helio_id': '2004 DW',
    'helio_id_type': 'smallbody',
#    {'name': 'Orcus', 'id': '2004 DW', 'var_name': 'orcus_var', 'color_key': 'Orcus', 'symbol': 'circle', 'object_type': 'orbital', 
#    'id_type': 'smallbody', 
#    'center_id': '2090482', # Numeric ID for use as Horizons center; Orcus's moon Vanth
    'mission_info': 'Horizons: 90482 Orcus. Dwarf planet with moon Vanth. Binary period: 9.54 days. Highest mass ratio (~16%) of any known binary.', 
    'mission_url': 'https://en.wikipedia.org/wiki/Orcus_(dwarf_planet)'},

    # NEW: Orcus-Vanth Barycenter - HIGHEST mass ratio binary system in the solar system!
    {
#    'name': 'Orcus-Vanth Barycenter', 'id': '2090482', 'var_name': 'orcus_barycenter_var', 
    'name': 'Orcus-Vanth Barycenter', 'id': '20090482', 'var_name': 'orcus_barycenter_var',
     'color_key': 'Orcus', 'symbol': 'square-open', 'object_type': 'barycenter',
     'mission_info': 'Center of mass for Orcus-Vanth binary system. Binary period: 9.54 days. Highest mass ratio (16%)!'},

    # Quaoar (50000 Quaoar)
    # NOTE: Quaoar-Weywot Barycenter removed - mass ratio ~0.004 means barycenter is
    # only ~7 km from Quaoar's center (inside the 1,090 km body). Not visually meaningful.
    # Use Quaoar-centered mode instead (Weywot orbiting Quaoar).

    {'name': 'Quaoar', 'id': '920050000', 'var_name': 'quaoar_var', 'color_key': 'Quaoar', 'symbol': 'circle', 'object_type': 'orbital', 
    'id_type': 'majorbody',
    'helio_id': '2002 LM60',  # For Sun-centered plots (smallbody solution)
    'helio_id_type': 'smallbody',
    'center_id': '920050000',  # Quaoar body center (for centered views)
    'mission_info': 'Horizons: 50000 Quaoar. Kuiper Belt dwarf planet with ring system (discovered 2023). Binary period with Weywot: 12.44 days.', 
    'mission_url': 'https://solarsystem.nasa.gov/planets/dwarf-planets/quaoar/in-depth/'},

    {'name': 'Sedna', 'id': '2003 VB12', 'var_name': 'sedna_var', 'color_key': 'Sedna', 'symbol': 'circle', 'object_type': 'orbital', 
    'id_type': 'smallbody', 
    'mission_info': 'Horizons: 2003 VB12. A distant trans-Neptunian dwarf planet with an extremely long orbit.', 
    'mission_url': 'https://solarsystem.nasa.gov/planets/dwarf-planets/sedna/in-depth/'},

    {'name': 'Leleakuhonua', 'id': '2015 TG387', 'var_name': 'leleakuhonua_var', 'color_key': 'Leleakuhonua', 'symbol': 'circle', 'object_type': 'orbital', 
    'id_type': 'smallbody', 
    'mission_info': 'Horizons: 2015 TG387. A distant trans-Neptunian dwarf planet with an extremely long orbit.', 
    'mission_url': 'https://en.wikipedia.org/wiki/541132_Lele%C4%81k%C5%ABhonua'},

    {'name': '2017 OF201', 'id': '2017 OF201', 'var_name': 'of201_var', 'color_key': '2017 OF201', 'symbol': 'circle', 'object_type': 'orbital', 
    'id_type': 'smallbody', 
    'mission_info': 'Horizons: 2017 OF201. A extreme trans-Neptunian object with an extremely long orbit.', 
    'mission_url': 'https://en.wikipedia.org/wiki/2017_OF201#:~:text=2017%20OF201%20is%20an,have%20a%20directly%20estimated%20size.'},

    # Lagrange Points
    # Earth-Moon Lagrange Points
    {'name': 'EM-L1', 'id': '3011', 'var_name': 'eml1_var', 'color_key': 'EM-L1', 'symbol': 'square-open', 'object_type': 'lagrange_point',    
    'id_type': 'id', 'start_date': datetime(1900, 1, 1), 'end_date': datetime(2050, 12, 31), 
    'mission_info': 'Horizons: 3011. Earth-Moon Lagrange-1 point is where the Earth\'s gravitational field counters the Moon\'s',
    'mission_url': 'http://hyperphysics.phy-astr.gsu.edu/hbase/Mechanics/lagpt.html'},  

    {'name': 'EM-L2', 'id': '3012', 'var_name': 'eml2_var', 'color_key': 'EM-L2', 'symbol': 'square-open', 'object_type': 'lagrange_point',   
    'id_type': 'id', 'start_date': datetime(1900, 1, 1), 'end_date': datetime(2050, 12, 31), 
    'mission_info': 'Horizons: 3012. Earth-Moon Lagrange-1 point is where the Earth\'s gravitational field counters the Moon\'s',
    'mission_url': 'http://hyperphysics.phy-astr.gsu.edu/hbase/Mechanics/lagpt.html'}, 

    {'name': 'EM-L3', 'id': '3013', 'var_name': 'eml3_var', 'color_key': 'EM-L3', 'symbol': 'square-open', 'object_type': 'lagrange_point',   
    'id_type': 'id', 'start_date': datetime(1900, 1, 1), 'end_date': datetime(2050, 12, 31), 
    'mission_info': 'Horizons: 3013. Earth-Moon Lagrange-1 point is where the Earth\'s gravitational field counters the Moon\'s',
    'mission_url': 'http://hyperphysics.phy-astr.gsu.edu/hbase/Mechanics/lagpt.html'},

    {'name': 'EM-L4', 'id': '3014', 'var_name': 'eml4_var', 'color_key': 'EM-L4', 'symbol': 'square-open', 'object_type': 'lagrange_point',    
    'id_type': 'id', 'start_date': datetime(1900, 1, 1), 'end_date': datetime(2050, 12, 31), 
    'mission_info': 'Horizons: 3014. Earth-Moon Lagrange-1 point is where the Earth\'s gravitational field counters the Moon\'s',
    'mission_url': 'http://hyperphysics.phy-astr.gsu.edu/hbase/Mechanics/lagpt.html'},

    {'name': 'EM-L5', 'id': '3015', 'var_name': 'eml5_var', 'color_key': 'EM-L5', 'symbol': 'square-open', 'object_type': 'lagrange_point',    
    'id_type': 'id', 'start_date': datetime(1900, 1, 1), 'end_date': datetime(2050, 12, 31), 
    'mission_info': 'Horizons: 3015. Earth-Moon Lagrange-1 point is where the Earth\'s gravitational field counters the Moon\'s',
    'mission_url': 'http://hyperphysics.phy-astr.gsu.edu/hbase/Mechanics/lagpt.html'},    

    # Sun-Earth-Moon-Barycenter Lagrange Points
    {'name': 'L1', 'id': '31', 'var_name': 'l1_var', 'color_key': 'L1', 'symbol': 'square-open', 'object_type': 'lagrange_point',    # SEMB-L1 31
    'id_type': 'id', 'start_date': datetime(1900, 1, 1), 'end_date': datetime(2050, 12, 31), 
    'mission_info': 'Horizons: 31. The Sun & Earth-Moon Barycenter Lagrange-1 point is where the Earth\'s gravitational field counters the Sun\'s',
    'mission_url': 'https://science.nasa.gov/resource/what-is-a-lagrange-point/#:~:text=The%20L2%20point%20of%20the,regular%20course%20and%20altitude%20corrections.'},    

    {'name': 'L2', 'id': '32', 'var_name': 'l2_var', 'color_key': 'L2', 'symbol': 'square-open', 'object_type': 'lagrange_point',    # SEMB-L2 32
    'id_type': 'id', 'start_date': datetime(1900, 1, 1), 'end_date': datetime(2050, 12, 31), 
    'mission_info': 'Horizons: 32. The Sun & Earth-Moon Barycenter Lagrange-2 point is where the Earth\'s gravitational field counters the Sun\'s',
    'mission_url': 'https://science.nasa.gov/resource/what-is-a-lagrange-point/#:~:text=The%20L2%20point%20of%20the,regular%20course%20and%20altitude%20corrections.'},    

    {'name': 'L3', 'id': '33', 'var_name': 'l3_var', 'color_key': 'L3', 'symbol': 'square-open', 'object_type': 'lagrange_point',    # SEMB-L3 33
    'id_type': 'id', 'start_date': datetime(1900, 1, 1), 'end_date': datetime(2050, 12, 31), 
    'mission_info': 'Horizons: 33. The Sun & Earth-Moon Barycenter Lagrange-3 point is where the Earth\'s gravitational field counters the Sun\'s',
    'mission_url': 'https://science.nasa.gov/resource/what-is-a-lagrange-point/#:~:text=The%20L2%20point%20of%20the,regular%20course%20and%20altitude%20corrections.'},    

    {'name': 'L4', 'id': '34', 'var_name': 'l4_var', 'color_key': 'L4', 'symbol': 'square-open', 'object_type': 'lagrange_point',    # SEMB-L4 34
    'id_type': 'id', 'start_date': datetime(1900, 1, 1), 'end_date': datetime(2050, 12, 31), 
    'mission_info': 'Horizons: 34. The Sun & Earth-Moon Barycenter Lagrange-4 point is where the Earth\'s gravitational field counters the Sun\'s',
    'mission_url': 'https://science.nasa.gov/resource/what-is-a-lagrange-point/#:~:text=The%20L2%20point%20of%20the,regular%20course%20and%20altitude%20corrections.'},    

    {'name': 'L5', 'id': '35', 'var_name': 'l5_var', 'color_key': 'L5', 'symbol': 'square-open', 'object_type': 'lagrange_point',    # SEMB-L5 35
    'id_type': 'id', 'start_date': datetime(1900, 1, 1), 'end_date': datetime(2050, 12, 31), 
    'mission_info': 'Horizons: 35. The Sun & Earth-Moon Barycenter Lagrange-5 point is where the Earth\'s gravitational field counters the Sun\'s',
    'mission_url': 'https://science.nasa.gov/resource/what-is-a-lagrange-point/#:~:text=The%20L2%20point%20of%20the,regular%20course%20and%20altitude%20corrections.'},    

    # Near-Earth Asteroids
    {'name': 'Kamo oalewa', 'id': '2016 HO3', 'var_name': 'kamooalewa_var', 'color_key': 'Kamo oalewa', 'symbol': 'circle-open', 'object_type': 'orbital',
    'id_type': 'smallbody', 'start_date': datetime(1962, 1, 21), 'end_date': datetime(2032, 12, 31), 
    # EOP coverage    : DATA-BASED 1962-JAN-20 TO 2025-JUL-04. PREDICTS-> 2025-SEP-29
    'mission_info': 'Horizons: 2016 HO3. Kamo\'oalewa is a very small, elongated asteroid belonging to the Apollo group of near-Earth objects.', 
    'mission_url': 'https://www.jpl.nasa.gov/news/small-asteroid-is-earths-constant-companion/'},

    {'name': '2025 PN7', 'id': '2025 PN7', 'var_name': 'pn7_var', 'color_key': '2025 PN7', 'symbol': 'circle-open', 'object_type': 'orbital',
    'id_type': 'smallbody', 
    # 'start_date': datetime(2024, 8, 2), 'end_date': datetime(2032, 12, 31),   # full date range
    'mission_info': '2025 PN7 is a small near-Earth asteroid and the most recently discovered quasi-satellite of Earth.',
    'mission_url': 'https://en.wikipedia.org/wiki/2025_PN7'},

    {'name': '2024 PT5', 'id': '2024 PT5', 'var_name': 'pt5_var', 'color_key': '2024 PT5', 'symbol': 'circle-open', 'object_type': 'orbital',
    'id_type': 'smallbody', 'start_date': datetime(2024, 8, 2), 'end_date': datetime(2032, 12, 31), 
    'mission_info': 'Horizons: 2024 PT5. Closest approach to Earth 8-9-2024.',
    'mission_url': 'https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=2024%20PT5'},

    {'name': '2025 PY1', 'id': '2025 PY1', 'var_name': 'py1_var', 'color_key': '2025 PY1', 'symbol': 'circle-open', 'object_type': 'orbital',
    'id_type': 'smallbody', 
#    'start_date': datetime(2024, 8, 2), 'end_date': datetime(2032, 12, 31), 
    'mission_info': 'Horizons: 2025 PY1. Near-Earth asteroid.',
    'mission_url': 'https://www.jpl.nasa.gov/asteroid-watch/next-five-approaches/'},    

    {'name': '2023 JF', 'id': '2023 JF', 'var_name': 'asteroid2023jf_var', 'color_key': '2023 JF', 'symbol': 'circle-open', 'object_type': 'orbital', 
    'id_type': 'smallbody', 'start_date': datetime(1962, 1, 20), 'end_date': datetime(2025, 10, 4),
    # EOP coverage    : DATA-BASED 1962-JAN-20 TO 2025-JUL-09. PREDICTS-> 2025-OCT-04
    'mission_info': 'Horizons: 2023 JF. Asteroid 2023 JF flew past Earth on May 9, 2023.', 
    'mission_url': 'https://www.nasa.gov/solar-system/near-earth-object-observations-program/#:~:text=The%20NEO%20Observations%20Program%20sponsors,the%20sky%20to%20determine%20their'},

    {'name': '2024 DW', 'id': '2024 DW', 'var_name': 'asteroid_dw_var', 'color_key': '2024 DW', 'symbol': 'circle-open', 'object_type': 'orbital',
    'id_type': 'smallbody', 'start_date': datetime(2024, 2, 19), 'end_date': datetime(2032, 12, 31), 
    'mission_info': 'Horizons: 2024 DW. Closest approach to Earth 2-22-2024 approximately 5 UTC. Keplerian orbit perturbation from Jupiter.',
    'mission_url': 'https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=2024%20DW'},

    {'name': '2024 YR4', 'id': '2024 YR4', 'var_name': 'yr4_var', 'color_key': '2024 YR4', 'symbol': 'circle-open', 'object_type': 'orbital',
    'id_type': 'smallbody', 'start_date': datetime(2024, 12, 24), 'end_date': datetime(2032, 12, 31), 
    'mission_info': 'Closest approach to Earth 12-25-2024 4:46 UTC.',
    'mission_url': 'https://science.nasa.gov/solar-system/asteroids/2024-yr4/'},

    # Main Belt Asteroids
    {'name': 'Apophis', 'id': '2004 MN4', 'var_name': 'apophis_var', 'color_key': 'Apophis', 'symbol': 'circle-open', 'object_type': 'orbital',
    'id_type': 'smallbody', 
    'center_id': '2099942',  # Numeric ID for use as Horizons center
    'mission_info': 'Horizons: 2004 MN4. A near-Earth asteroid that will make a close approach in 2029. Future OSIRIS-APEX target', 
    'mission_url': 'https://cneos.jpl.nasa.gov/apophis/'},

    {'name': 'Bennu', 'id': '1999 RQ36', 'var_name': 'bennu_var', 'color_key': 'Bennu', 'symbol': 'circle-open', 'object_type': 'orbital', 
    'id_type': 'smallbody', 
    'center_id': '2101955',  # Numeric ID for use as Horizons center
    'mission_info': 'Horizons: 1999 RQ36. Studied by NASA\'s OSIRIS-REx mission.', 
    'mission_url': 'https://science.nasa.gov/solar-system/asteroids/101955-bennu/'},

#    {'name': 'Bennu/OSIRIS', 'id': '2101955', 'var_name': 'bennu2_var', 'color_key': 'Bennu', 'symbol': 'circle-open', 'object_type': 'orbital', 
#    'id_type': 'smallbody', # Bennu as a center object
#    'mission_info': 'Studied by NASA\'s OSIRIS-REx mission.', 
#    'mission_url': 'https://science.nasa.gov/solar-system/asteroids/101955-bennu/'},

    {'name': 'Eros', 'id': 'A898 PA', 'var_name': 'eros_var', 'color_key': 'Eros', 'symbol': 'circle-open', 'object_type': 'orbital', 
    'id_type': 'smallbody',
    'center_id': '2000433',  # Numeric ID for use as Horizons center 
    'mission_info': 'Horizons: A898 PA. First asteroid to be orbited and landed on by NASA\'s NEAR Shoemaker spacecraft in 2000-2001.', 
    'mission_url': 'https://science.nasa.gov/solar-system/asteroids/433-eros/'},

    {'name': 'Dinkinesh', 'id': '1999 VD57', 'var_name': 'dinkinesh_var', 'color_key': 'Dinkinesh', 'symbol': 'circle-open', 'object_type': 'orbital', 
    'id_type': 'smallbody',
    'center_id': '20152830',  # Numeric ID for use as Horizons center
    'mission_info': 'Horizons: 1999 VD57. Dinkinesh was visited by the mission Lucy.', 
    'mission_url': 'https://science.nasa.gov/solar-system/asteroids/dinkinesh/'},

    {'name': 'Itokawa', 'id': '1998 SF36', 'var_name': 'itokawa_var', 'color_key': 'Itokawa', 'symbol': 'circle-open', 'object_type': 'orbital', 
    'id_type': 'smallbody',
    'center_id': '2025143',  # Numeric ID for use as Horizons center 
    'mission_info': 'Horizons: 1998 SF36. First asteroid from which samples were returned to Earth by JAXA\'s Hayabusa mission in 2010.', 
    'mission_url': 'https://en.wikipedia.org/wiki/25143_Itokawa'},

    {'name': 'Lutetia', 'id': 'A852 VA', 'var_name': 'lutetia_var', 'color_key': 'Lutetia', 'symbol': 'circle-open', 'object_type': 'orbital', 
    'id_type': 'smallbody', 
    'mission_info': 'Horizons: A852 VA. Studied by European Space Agency\'s Rosetta mission.', 
    'mission_url': 'https://www.nasa.gov/image-article/asteroid-lutetia/'},

    {'name': 'Ryugu', 'id': '1999 JU3', 'var_name': 'ryugu_var', 'color_key': 'Ryugu', 'symbol': 'circle-open', 'object_type': 'orbital', 
    'id_type': 'smallbody',
    'center_id': '2162173',  # Numeric ID for use as Horizons center  
    'mission_info': 'Horizons: 1999 JU3. Target of JAXA\'s Hayabusa2 mission which returned samples to Earth in 2020.', 
    'mission_url': 'https://en.wikipedia.org/wiki/162173_Ryugu'},

    {'name': 'Steins', 'id': '1969 VC', 'var_name': 'steins_var', 'color_key': 'Steins', 'symbol': 'circle-open', 'object_type': 'orbital', 
     'id_type': 'smallbody',
     'mission_info': 'Horizons: 1969 VC. Visited by European Space Agency\'s Rosetta spacecraft.', 
     'mission_url': 'https://www.esa.int/Science_Exploration/Space_Science/Rosetta'},

    {'name': 'Donaldjohanson', 'id': '1981 EQ5', 'var_name': 'donaldjohanson_var', 'color_key': 'Donaldjohanson', 'symbol': 'circle-open', 'object_type': 'orbital', 
     'id_type': 'smallbody',
     'center_id': '20052246',  # Numeric ID for use as Horizons center (52246 Donaldjohanson)
     'mission_info': 'Lucy flyby: Apr 20, 2025. D~4 km, C-type. Named for paleoanthropologist who discovered "Lucy" fossil.', 
     'mission_url': 'https://science.nasa.gov/solar-system/asteroids/donaldjohanson/'},

    {'name': 'Vesta', 'id': 'A807 FA', 'var_name': 'vesta_var', 'color_key': 'Vesta', 'symbol': 'circle-open', 'object_type': 'orbital', 
    'id_type': 'smallbody',
    'center_id': '2000004',  # Numeric ID for use as Horizons center 
    'mission_info': 'Horizons: A807 FA. One of the largest objects in the asteroid belt, visited by NASA\'s Dawn mission.', 
    'mission_url': 'https://dawn.jpl.nasa.gov/'},

    # Kuiper Belt Objects or Trans-Neptunian Objects (TNOs)

    {'name': 'Arrokoth', 'id': '2014 MU69', 'var_name': 'arrokoth_var', 'color_key': 'Arrokoth', 'symbol': 'circle-open', 'object_type': 'orbital', 
    'id_type': 'smallbody',
    'center_id': '2486958', 
    'mission_info': 'Horizons: 2014 MU69. Arrokoth flyby from New Horizons on January 1, 2019.', 
    'mission_url': 'https://science.nasa.gov/resource/arrokoth-2014-mu69-in-3d/'},

    {'name': 'Ixion', 'id': '2001 KX76', 'var_name': 'ixion_var', 'color_key': 'Ixion', 'symbol': 'circle-open', 'object_type': 'orbital', 
    'id_type': 'smallbody', 
    'mission_info': 'Horizons: 2001 KX76. A large Kuiper Belt object without a known moon.', 
    'mission_url': 'https://en.wikipedia.org/wiki/28978_Ixion'},

    {'name': 'GV9', 'id': '2004 GV9', 'var_name': 'gv9_var', 'color_key': 'GV9', 'symbol': 'circle-open', 'object_type': 'orbital', 
    'id_type': 'smallbody', 
    'mission_info': 'Horizons: 2004 GV9. A binary Kuiper Belt Object providing precise mass measurements through its moon.', 
    'mission_url': 'https://en.wikipedia.org/wiki/(90568)_2004_GV9'},

    {'name': 'Varuna', 'id': '2000 WR106', 'var_name': 'varuna_var', 'color_key': 'Varuna', 'symbol': 'circle-open', 'object_type': 'orbital', 
    'id_type': 'smallbody', 
    'mission_info': 'Horizons: 2000 WR106. A significant Kuiper Belt Object with a rapid rotation period.', 
    'mission_url': 'https://en.wikipedia.org/wiki/20000_Varuna'},

    {'name': 'Ammonite', 'id': '2023 KQ14', 'var_name': 'ammonite_var', 'color_key': 'Ammonite', 'symbol': 'circle-open', 'object_type': 'orbital', 
    # 136199 primary (required for Sun centered plots)
    'id_type': 'smallbody', 
    'mission_info': 'Horizons: 2023 KQ14. Ammonite is classified as a sednoid, after Sedna.', 
    'mission_url': 'https://en.wikipedia.org/wiki/2023_KQ14'},     

    # Comets

    {'name': 'Churyumov', 'id': '90000699', 'var_name': 'comet_Churyumov_Gerasimenko_var', 'color_key': 'Churyumov', # 67P/Churyumov-Gerasimenko
    'symbol': 'diamond', 'object_type': 'orbital', 'id_type': 'smallbody', 
    #'start_date': datetime(2008, 6, 2), 'end_date': datetime(2023, 4, 25), 
    # data arc: 2008-06-01 to 2023-04-26; Epoch: 2015-Oct-10; 67P; previously rec 90000704; record number needed to fetch Horizons data.
    'mission_info': 'Horizons: 67P. 67P/Churyumov-Gerasimenko is the comet visited by the Rosetta spacecraft, August 2014 through September 2016.', 
    'mission_url': 'https://science.nasa.gov/solar-system/comets/67p-churyumov-gerasimenko/'},

    {'name': 'Hale-Bopp', 'id': 'C/1995 O1', 'var_name': 'comet_hale_bopp_var', 'color_key': 'Hale-Bopp', 'symbol': 'diamond', 
    'object_type': 'orbital', 'id_type': 'smallbody', 'start_date': datetime(1993, 4, 28), 'end_date': datetime(2022, 7, 9),
    # data arc: 1993-04-27 to 2022-07-09 
    'mission_info': 'Horizons: C/1995 O1. Visible to the naked eye for a record 18 months.', 
    'mission_url': 'https://science.nasa.gov/solar-system/comets/c-1995-o1-hale-bopp/'},

    {'name': 'Halley', 'id': '90000030', 'var_name': 'comet_halley_var', 'color_key': 'Halley', 'symbol': 'diamond',
    'object_type': 'orbital', 'id_type': 'smallbody', 
    #'start_date': datetime(1900, 1, 1), 'end_date': datetime(1994, 1, 11), 
    # data arc: 1835-08-21 to 1994-01-11; 1P/Halley requires the record number to fetch position data for the 1986 apparition.
    'mission_info': 'Horizons: 1P/Halley. Retrograde. Most famous comet, returned in 1986 and will return in 2061. Retrograde (left-handed) orbit.', 
    'mission_url': 'https://sites.google.com/view/tony-quintanilla/comets/halley-1986'},

    {'name': 'Hyakutake', 'id': 'C/1996 B2', 'var_name': 'comet_hyakutake_var', 'color_key': 'Hyakutake', 'symbol': 'diamond', 
    'object_type': 'orbital', 'id_type': 'smallbody', 
    #'start_date': datetime(1996, 1, 2), 'end_date': datetime(1996, 11, 1),
    # data arc: 1996-01-01 to 1996-11-02 
    'mission_info': 'Horizons: C/1996 B2. Retrograde. Passed very close to Earth in 1996. Retrograde (left-handed) orbit.', 
    'mission_url': 'https://science.nasa.gov/mission/ulysses/'},

    {'name': 'Lemmon', 'id': 'C/2025 A6', 'var_name': 'comet_lemmon_var', 'color_key': 'Lemmon', 'symbol': 'diamond', 
    'object_type': 'orbital', 'id_type': 'smallbody', 
    # 'start_date': datetime(2024, 11, 12), 'end_date': datetime(2029, 12, 31), # all dates are valid in Horizons
    #  data arc: 2024-11-12 to 2025-10-03
    # PREDICTS-> 2025-DEC-29    Rec #:90004893 (+COV) Soln.date: 2025-Oct-03_14:42:16    # obs: 758 (2024-2025)
    'mission_info': 'Horizons: C/2025 A6. Retrograde. In Fall 2025, Comet Lemmon is brightening and moving into morning northern skies.', 
    'mission_url': 'https://apod.nasa.gov/apod/ap250930.html'},      

    {'name': 'Ikeya-Seki', 'id': 'C/1965 S1-A', 'var_name': 'comet_ikeya_seki_var', 'color_key': 'Ikeya-Seki', 'symbol': 'diamond', 
    'object_type': 'orbital', 'id_type': 'smallbody', 
    #'start_date': datetime(1965, 9, 22), 'end_date': datetime(1966, 1, 14), 
    'mission_info': 'Horizons: C/1965 S1-A. Retrograde. One of the brightest comets of the 20th century. Retrograde (left-handed) orbit.', 
    'mission_url': 'https://sites.google.com/view/tony-quintanilla/comets/ikeya-seki-1965'},

    {'name': 'NEOWISE', 'id': 'C/2020 F3', 'var_name': 'comet_neowise_var', 'color_key': 'NEOWISE', 'symbol': 'diamond', # C/2020 F3
    'object_type': 'orbital', 'id_type': 'smallbody', 
    #'start_date': datetime(2020, 3, 28), 'end_date': datetime(2021, 6, 1), 
    'mission_info': 'Horizons: C/2020 F3. Retrograde. Brightest comet visible from the Northern Hemisphere in decades. Retrograde (left-handed) orbit.', 
    'mission_url': 'https://www.nasa.gov/missions/neowise/nasas-neowise-celebrates-10-years-plans-end-of-mission/'},

    {'name': 'SWAN', 'id': 'C/2025 R2', 'var_name': 'comet_c2025r2_var', 'color_key': 'SWAN', 'symbol': 'diamond', 
    'object_type': 'orbital', 'id_type': 'smallbody', 
    #'start_date': datetime(2025, 8, 14), 'end_date': datetime(2025, 9, 14),
    # data arc: data arc: 2025-08-13 to 2025-09-14;  EOP coverage    : DATA-BASED 1962-JAN-20 TO 2025-SEP-19. PREDICTS-> 2025-DEC-15
    'mission_info': 'Horizons: C/2025 R2 (SWAN). This is a non-periodic comet that was discovered on September 11, 2025.', 
    'mission_url': 'https://en.wikipedia.org/wiki/C/2025_R2_(SWAN)'},     

    {'name': '6AC4721', 'id': 'none', 'var_name': 'comet_6ac4721_var', 'color_key': '6AC4721', 'symbol': 'diamond',    # C/2026 A1 in Horizons
    'object_type': 'orbital', 'id_type': 'smallbody', 
    #'start_date': datetime(2026, 1, 13), 'end_date': datetime(2026, 1, 19),
    'mission_info': 'Kreutz sungrazer found at an unusually large distance from the Sun. Discovered by the 6AC4721 survey.',  
    'mission_url': 'https://en.wikipedia.org/wiki/C/2026_A1_(MAPS)'},      

    {'name': 'MAPS', 'id': 'C/2026 A1', 'var_name': 'comet_c2026a1_var', 'color_key': 'MAPS', 'symbol': 'diamond',    # C/2026 A1 in Horizons
    'object_type': 'orbital', 'id_type': 'smallbody', 
    'mission_info': 'Kreutz sungrazer comet discovered on 13 January 2026 from the AMACS1 Observatory in the Atacama Desert, Chile.', 
    'mission_url': 'https://en.wikipedia.org/wiki/C/2026_A1_(MAPS)'},      


# Interstellar and hyperbolic objects

# Hyperbolic solar

    {'name': 'West', 'id': 'C/1975 V1', 'var_name': 'comet_west_var', 'color_key': 'Comet West', 'symbol': 'diamond', 
    'object_type': 'trajectory', 'id_type': 'smallbody', 'start_date': datetime(1975, 11, 6), 'end_date': datetime(1976, 6, 1), 
    'mission_info': 'Horizons: C/1975 V1. Hyperbolic. Notable for its bright and impressive tail.', 
    'mission_url': 'https://en.wikipedia.org/wiki/Comet_West'},

    {'name': 'McNaught', 'id': 'C/2006 P1', 'var_name': 'comet_mcnaught_var', 'color_key': 'McNaught', 'symbol': 'diamond', 
    'object_type': 'trajectory', 'id_type': 'smallbody', 'start_date': datetime(2006, 8, 8), 'end_date': datetime(2007, 7, 10), 
    # data arc: 2006-08-07 to 2007-07-11
    'mission_info': 'Horizons: C/2006 P1. Hyperbolic. Known as the Great Comet of 2007. Retrograde (left-handed) orbit.', 
    'mission_url': 'https://science.nasa.gov/solar-system/comets/'},  

     {'name': 'Tsuchinshan', 'id': 'C/2023 A3', 'var_name': 'comet_tsuchinshan_atlas_var', 'color_key': 'Tsuchinsh', 
    'symbol': 'diamond', 'object_type': 'orbital', 'id_type': 'smallbody', # check object type should be 'trajectory'
    'start_date': datetime(2023, 1, 10), 'end_date': datetime(2029, 12, 31), 
    'mission_info': 'Horizons: C/2023 A3. Retrograde. Hyperbolic. Tsuchinshan-ATLAS is a new comet discovered in 2023, expected to become bright in 2024.', 
    'mission_url': 'https://en.wikipedia.org/wiki/C/2023_A3_(Tsuchinshan-ATLAS)'},      

    {'name': 'ATLAS', 'id': 'C/2024 G3', 'var_name': 'comet_atlas_var', 'color_key': 'ATLAS', 'symbol': 'diamond', 
    'object_type': 'orbital', 'id_type': 'smallbody', # check object type should be 'trajectory'
    # 'start_date': datetime(2024, 6, 18), 'end_date': datetime(2029, 12, 31), # all dates are valid in Horizons
    # EOP coverage    : DATA-BASED 1962-JAN-20 TO 2025-OCT-03. PREDICTS-> 2025-DEC-29
    # data arc: 2024-04-05 to 2025-01-01
    'mission_info': 'Horizons: C/2024 G3. Retrograde. Hyperbolic. The Great Comet of 2025. Comet C/2024 G3 (ATLAS) created quite a buzz in the Southern Hemisphere!', 
    'mission_url': 'https://en.wikipedia.org/wiki/C/2024_G3_(ATLAS)'},

    {'name': 'C/2025_K1', 'id': 'C/2025 K1', 'var_name': 'comet_2025k1_var', 'color_key': 'C/2025_K1', 'symbol': 'diamond', 
    # ATLAS (C/2025 K1) 2025-Jul-11 21:59:05; data arc: 2025-04-08 to 2025-07-10
    'object_type': 'trajectory', 'id_type': 'smallbody', 
    # 'start_date': datetime(2025, 4, 8), 'end_date': datetime(2025, 7, 10), 
    'mission_info': 'Horizons: C/2025 K1. Retrograde. Hyperbolic. A notable comet for observation in late 2025. Retrograde (left-handed) orbit.', 
    'mission_url': 'https://theskylive.com/c2025k1-info'}, 

    {'name': 'PANSTARRS', 'id': 'C/2025 R3', 'var_name': 'comet_c2025r3_var', 'color_key': 'PANSTARRS', 'symbol': 'diamond',     # PANSTARRS (C/2025 R3)
    'object_type': 'trajectory', 'id_type': 'smallbody', 
    'mission_info': 'Horizons: C/2025 R3 (PANSTARRS). Retrograde. Hyperbolic. This is a non-periodic comet that was discovered on September 8, 2025.', 
    'mission_url': 'https://www.space.com/astronomy/comets/will-comet-c-2025-r3-panstarrs-be-the-great-comet-of-2026'},

    {'name': 'Borisov', 'id': 'C/2025 V1', 'var_name': 'comet_2025v1_var', 'color_key': 'Borisov', 'symbol': 'diamond', 
    # Borisov (C/2025 V1) 2025-Nov-11 16:37:03; data arc: 2025-10-29 to 2025-11-05
    'object_type': 'trajectory', 'id_type': 'smallbody', 
    # 'start_date': datetime(2025, 4, 8), 'end_date': datetime(2025, 7, 10), 
    'mission_info': 'Horizons: C/2025 V1. Retrograde. Hyperbolic. Discovered 11-2-2025. Most likely originated from the Oort Cloud.', 
    'mission_url': 'https://theskylive.com/planetarium?obj=c2025v1'},

# Hyperbolic and interstellar

    {'name': '1I/Oumuamua', 'id': 'A/2017 U1', 'var_name': 'oumuamua_var', 'color_key': '1I/Oumuamua', 'symbol': 'diamond', 
    'object_type': 'trajectory', 'id_type': 'smallbody', 'start_date': datetime(2017, 10, 15), 'end_date': datetime(2018, 1, 1),
    # data arc from 2017 October 14 to 2018 January 2 
    'mission_info': 'Horizons: A/2017 U1. Retrograde. Hyperbolic. First known interstellar object detected passing through<br>' 
    'the Solar System. Retrograde (left-handed) orbit.', 
    'mission_url': 'https://www.jpl.nasa.gov/news/solar-systems-first-interstellar-visitor-dazzles-scientists/'},

    {'name': '2I/Borisov', 'id': 'C/2019 Q4', 'var_name': 'comet_borisov_var', 'color_key': '2I/Borisov', 'symbol': 'diamond', 
    'object_type': 'trajectory', 'id_type': 'smallbody', 'start_date': datetime(2019, 2, 25), 'end_date': datetime(2020, 9, 29), 
    # data arc: 2019-02-24 to 2020-09-30
    'mission_info': 'Horizons: C/2019 Q4. Hyperbolic. The second interstellar object detected, after \'1I/Oumuamua.', 
    'mission_url': 'https://science.nasa.gov/solar-system/comets/2i-borisov/'},

    {'name': '3I/ATLAS', 'id': 'C/2025 N1', 'var_name': 'atlas3i_var', 'color_key': '3I/ATLAS', 'symbol': 'diamond', 
    # JPL/HORIZONS                  ATLAS (C/2025 N1)            2025-Oct-28 14:32:30
    'object_type': 'trajectory', 'id_type': 'smallbody', 
    'start_date': datetime(2025, 5, 15), 'end_date': datetime(2032, 12, 31),
    # data arc: 2025-05-15 to 2025-09-21
    'mission_info': 'Horizons: C/2025 N1. Retrograde. Hyperbolic. Third known interstellar object detected passing through<br>'  
    'the Solar System. Retrograde (left-handed) orbit.', 
    'mission_url': 'https://science.nasa.gov/blogs/planetary-defense/2025/07/02/nasa-discovers-interstellar-comet-moving-through-solar-system/'},

    # NASA Missions -- start date moved up by one day to avoid fetching errors, and default end date is 2025-01-01

    # Apollo 11 S-IVB (Spacecraft) -399110 Time Specification: Start=1969-07-16:40 UT , Stop=1969-07-28 00:06, Step=1 (hours) Revised: Mar 22, 2016  
    {'name': 'Apollo 11 S-IVB', 'id': '-399110', 'var_name': 'apollo11sivb_var', 'color_key': 'Apollo 11 S-IVB', 'symbol': 'diamond-open', 
    'object_type': 'trajectory', 'id_type': 'id', 'is_mission': True, 'start_date': datetime(1969, 7, 16), 'end_date': datetime(1969, 7, 28), # splashdown 07-24 16:50
    'mission_url': 'https://www.nasa.gov/mission/apollo-11/', 
    'mission_info': 'Horizons: -399110. This is the last and most powerful stage of the Saturn V rocket that propelled the Apollo 11 mission towards the Moon.'},

    {'name': 'Pioneer 10', 'id': '-23', 'var_name': 'pioneer10_var', 'color_key': 'Pioneer 10', 'symbol': 'diamond-open', 
    'object_type': 'trajectory', 'id_type': 'id', 'is_mission': True, 'start_date': datetime(1972, 3, 4), 'end_date': datetime(2002, 3, 3), 
    # No ephemeris for target "Pioneer 10 (spacecraft)" prior to A.D. 1972-MAR-03 02:04:00.0000 UT
    # No ephemeris for target "Pioneer 10 (spacecraft)" after A.D. 2050-JAN-01 00:08:50.8161 UT
    'mission_url': 'https://www.nasa.gov/centers/ames/missions/archive/pioneer.html', 
    'mission_info': 'Horizons: -23. First spacecraft to travel through the asteroid belt and make direct observations of Jupiter.'},

    {'name': 'Pioneer 11', 'id': '-24', 'var_name': 'pioneer11_var', 'color_key': 'Pioneer 11', 'symbol': 'diamond-open', 
    'object_type': 'trajectory', 'id_type': 'id', 'is_mission': True, 'start_date': datetime(1973, 4, 7), 'end_date': datetime(1995, 9, 29),
    # No ephemeris for target "Pioneer 11 (spacecraft)" prior to A.D. 1973-APR-06 02:25:00.0000 UT
    # Science operations and daily telemetry ceased on September 30, 1995 
    'mission_url': 'https://www.nasa.gov/centers/ames/missions/archive/pioneer.html', 
    'mission_info': 'Horizons: -24. First spacecraft to encounter Saturn and study its rings.'},

    {'name': 'Voyager 1', 'id': '-31', 'var_name': 'voyager1_var', 'color_key': 'Voyager 1', 'symbol': 'diamond-open', 
    'object_type': 'trajectory', 'id_type': 'id', 'is_mission': True, 'start_date': datetime(1977, 9, 6), 'end_date': datetime(2029, 12, 31), 
    'mission_url': 'https://voyager.jpl.nasa.gov/mission/', 
    'mission_info': 'Horizons: -31. Launched in 1977, Voyager 1 is the farthest spacecraft from Earth.'},

    {'name': 'Voyager 2', 'id': '-32', 'var_name': 'voyager2_var', 'color_key': 'Voyager 2', 'symbol': 'diamond-open', 
    'object_type': 'trajectory', 'id_type': 'id', 'is_mission': True, 'start_date': datetime(1977, 8, 21), 'end_date': datetime(2029, 12, 31), 
    'mission_url': 'https://voyager.jpl.nasa.gov/mission/', 
    'mission_info': 'Horizons: -32. Launched in 1977, Voyager 2 explored all four giant planets.'},

    {'name': 'Galileo', 'id': '-77', 'var_name': 'galileo_var', 'color_key': 'Galileo', 'symbol': 'diamond-open', 'object_type': 'trajectory', 
    'id_type': 'id', 'is_mission': True, 'start_date': datetime(1989, 10, 20), 'end_date': datetime(2003, 9, 29),
    # No ephemeris for target "Galileo (spacecraft)" prior to A.D. 1989-OCT-19 01:28:37.0780 UT
    # No ephemeris for target "Galileo (spacecraft)" after A.D. 2003-SEP-30 11:58:55.8177 UT
    'mission_url': 'https://solarsystem.nasa.gov/missions/galileo/overview/', 
    'mission_info': 'Horizons: -77. Galileo studied Jupiter and its moons from 1995 to 2003.'},

    {'name': 'SOHO', 'id': '-21', 'var_name': 'soho_var', 'color_key': 'SOHO', 
    'symbol': 'diamond-open', 'object_type': 'trajectory', 'id_type': 'id', 'is_mission': True, 'start_date': datetime(1995, 12, 3), 'end_date': datetime(2025, 9, 28), 
    # No ephemeris for target "SOHO (spacecraft)" after A.D. 2025-SEP-29 23:50:00.0000 UT
    'mission_info': 'Horizons: -21. The Solar and Heliospheric Observatory observes the Sun and heliosphere from the L1 Lagrange point.', 
    'mission_url': 'https://sohowww.nascom.nasa.gov/'},    

    {'name': 'Cassini', 'id': '-82', 'var_name': 'cassini_var', 'color_key': 'Cassini', 'symbol': 'diamond-open', 
     'object_type': 'trajectory', 'id_type': 'id', 'is_mission': True, 'start_date': datetime(1997, 10, 16), 'end_date': datetime(2017, 9, 14), 
     # No ephemeris for target "Cassini (spacecraft)" after A.D. 2017-SEP-15 11:56:50.8176 UT
     'mission_url': 'https://solarsystem.nasa.gov/missions/cassini/overview/', 
     'mission_info': 'Horizons: -82. Cassini-Huygens studied Saturn and its moons from 2004 to 2017.'},

    {'name': 'Rosetta', 'id': '-226', 'var_name': 'rosetta_var', 'color_key': 'Rosetta', 'symbol': 'diamond-open', 'object_type': 'trajectory', 
    'id_type': 'id', 'is_mission': True, 'start_date': datetime(2004, 3, 3), 'end_date': datetime(2016, 10, 4),
    # No ephemeris for target "Rosetta (spacecraft)" prior to A.D. 2004-MAR-02 09:25:55.8146 UT
    # No ephemeris for target "Rosetta (spacecraft)" after A.D. 2016-OCT-04 23:59:59.9997 UT
    'mission_url': 'https://rosetta.esa.int/', 
    'mission_info': 'Horizons: -226. European Space Agency mission to study Comet 67P/Churyumov-Gerasimenko.'},

    {'name': 'New Horizons', 'id': '-98', 'var_name': 'new_horizons_var', 'color_key': 'New Horizons', 'symbol': 'diamond-open', 
    'object_type': 'trajectory', 'id_type': 'id', 'is_mission': True, 'start_date': datetime(2006, 1, 20), 'end_date': datetime(2029, 12, 31), 
    # No ephemeris for target "New Horizons (spacecraft)" prior to A.D. 2006-JAN-19 19:50:13.1460 UT
    # No ephemeris for target "New Horizons (spacecraft)" after A.D. 2030-JAN-01 11:58:50.8161 UT
    'mission_url': 'https://www.nasa.gov/mission_pages/newhorizons/main/index.html', 
    'mission_info': 'Horizons: -98. New Horizons flew past Pluto in 2015 and continues into the Kuiper Belt.'},

    {'name': 'Akatsuki', 'id': '-5', 'var_name': 'akatsuki_var', 'color_key': 'Akatsuki', 'symbol': 'diamond-open',
    # Akatsuki / VCO / Planet-C (spacecraft)           -5 
    'object_type': 'trajectory', 'id_type': 'id', 'is_mission': True, 'start_date': datetime(2010, 5, 22), 'end_date': datetime(2025, 8, 22), 
    # No ephemeris for target "Planet-C (spacecraft)" prior to A.D. 2010-MAY-21 00:51:00.0000 UT
    # No ephemeris for target "Planet-C (spacecraft)" after A.D. 2025-AUG-23 23:58:50.8172 UT
    'mission_info': 'Horizons: -5. JAXA mission to study the atmospheric circulation of Venus', 
    'mission_url': 'https://en.wikipedia.org/wiki/Akatsuki_(spacecraft)'},

    {'name': 'Juno', 'id': '-61', 'var_name': 'juno_var', 'color_key': 'Juno', 'symbol': 'diamond-open', 'object_type': 'trajectory', 
    'id_type': 'id', 'is_mission': True, 'start_date': datetime(2011, 8, 6), 'end_date': datetime(2028, 9, 30), 
    # No ephemeris for target "Juno (spacecraft)" prior to A.D. 2011-AUG-05 17:18:06.0000 UT
    # No ephemeris for target "Juno (spacecraft)" after A.D. 2028-SEP-30 23:58:50.8177 UT
    'mission_url': 'https://www.nasa.gov/mission_pages/juno/main/index.html', 
    'mission_info': 'Horizons: -61. Juno studies Jupiter\'s atmosphere and magnetosphere.'},

    {'name': 'Gaia', 'id': '-139479', 'var_name': 'gaia_var', 'color_key': 'Gaia', 'symbol': 'diamond-open', 'object_type': 'trajectory', 
    'id_type': 'id', 'is_mission': True, 'start_date': datetime(2013, 12, 20), 'end_date': datetime(2025, 3, 28),    # end of mission 2025-3-28
    # No ephemeris for target "Gaia (spacecraft)" prior to A.D. 2013-DEC-19 09:54:19.5774 UT
    #   ORB1_20250414_000001                            2013-Dec-19   2125-Mar-28 
    'mission_info': 'Horizons: -139479. European Space Agency mission at L2 mapping the Milky Way.', 
    'mission_url': 'https://www.cosmos.esa.int/web/gaia'},

    {'name': 'Hayabusa2', 'id': '-37', 'var_name': 'hayabusa2_var', 'color_key': 'Hayabusa2', 'symbol': 'diamond-open', 
    'object_type': 'trajectory', 'id_type': 'id', 'is_mission': True, 'start_date': datetime(2014, 12, 4), 'end_date': datetime(2025, 10, 29), 
    # No ephemeris for target "Hayabusa 2 (spacecraft)" prior to A.D. 2014-DEC-03 06:13:46.0000 UT
    # No ephemeris for target "Hayabusa 2 (spacecraft)" after A.D. 2025-OCT-30 23:58:50.8175 UT
    'mission_info': 'Horizons: -37. JAXA mission that returned samples from Ryugu.', 
    'mission_url': 'https://hayabusa2.jaxa.jp/en/'},

    {'name': 'OSIRISREx', 'id': '-64', 'var_name': 'osiris_rex_var', 'color_key': 'OSIRIS', 'symbol': 'diamond-open', 
    'object_type': 'trajectory', 'id_type': 'id', 'is_mission': True, 'start_date': datetime(2016, 9, 9), 'end_date': datetime(2023, 9, 24), 
    'mission_url': 'https://science.nasa.gov/mission/osiris-rex/', 
    'mission_info': 'Horizons: -64. OSIRIS-REx is NASA\'s mission to collect samples from asteroid Bennu.'},

    {'name': 'OSIRISAPE', 'id': '-64', 'var_name': 'osiris_apex_var', 'color_key': 'OSIRIS', 'symbol': 'diamond-open', 
    'object_type': 'trajectory', 'id_type': 'id', 'is_mission': True, 'start_date': datetime(2023, 9, 24), 'end_date': datetime(2030, 3, 1),
    # No ephemeris for target "OSIRIS-REx (spacecraft)" after A.D. 2030-MAR-01 19:58:50.8146 UT 
    'mission_url': 'https://science.nasa.gov/category/missions/osiris-apex/', 
    'mission_info': 'Horizons: -64. OSIRIS-APEX is NASA\'s mission to study asteroid Apophis.'},

    {'name': 'Parker', 'id': '-96', 'var_name': 'parker_solar_probe_var', 'color_key': 'Parker Solar Probe', 
    'symbol': 'diamond-open', 'object_type': 'trajectory', 'id_type': 'id', 'is_mission': True, 'start_date': datetime(2018, 8, 13), 'end_date': datetime(2029, 1, 31), 
    # No ephemeris for target "Parker Solar Probe (spacecraft)" after A.D. 2029-FEB-01 00:00:00.0000 UT
    'mission_url': 'https://www.nasa.gov/content/goddard/parker-solar-probe', 
    'mission_info': 'Horizons: -96. The Parker Solar Probe mission is to study the outer corona of the Sun.'},

    {'name': 'MarsRover', 'id': '-168', 'var_name': 'perse_var', 'color_key': 'MarsRover', 'symbol': 'diamond-open', # Perseverance
    'object_type': 'trajectory', 'id_type': 'id', 'is_mission': True, 'start_date': datetime(2020, 7, 31), 'end_date': datetime(2026, 2, 19),    # end ephemeris
    # No ephemeris for target "Mars2020 (spacecraft)" after A.D. 2026-FEB-18 23:58:50.8148 UT
    'mission_info': 'Horizons: -168. The Perseverance Rover is NASA\'s Mars rover and Ingenuity helicopter.<br><br>'
    '<b>HISTORIC MILESTONE - December 8, 2025:</b> First AI-planned drive on another planet! Engineers at NASA JPL used Claude <br>'
    'to plot a 400-meter route across the Martian surface. This was planned through conversation, not code.<br><br>'
    'Note: The elevation values shown (-4200m) differ from published scientific values for Jezero Crater (-2600m) due to different <br>'
    'Mars reference systems. JPL Horizons uses one elevation datum, while scientific publications often use the MOLA reference areoid.',
    'mission_url': 'mars_milestone.html'},  # Local HTML milestone graphic (contains link to NASA)

    {'name': 'Lucy', 'id': '-49', 'var_name': 'lucy_var', 'color_key': 'Lucy', 'symbol': 'diamond-open', 'object_type': 'trajectory', 
    'id_type': 'id', 'is_mission': True, 'start_date': datetime(2021, 10, 17), 'end_date': datetime(2033, 4, 2), 
    # 2021-10-16 10:33:08.283 (min. for current target body)
    # 2033-04-02 17:27:41.343 (max. for current target body)
    'mission_info': 'Horizons: -49. Exploring Trojan asteroids around Jupiter.', 
    'mission_url': 'https://www.nasa.gov/lucy'},

    {'name': 'DART', 'id': '-135', 'var_name': 'dart_var', 'color_key': 'DART', 'symbol': 'diamond-open', 'object_type': 'trajectory', 
    'id_type': 'id', 'is_mission': True, 'start_date': datetime(2021, 11, 25), 'end_date': datetime(2022, 9, 26), 
    # No ephemeris for target "DART (spacecraft)" prior to A.D. 2021-NOV-24 07:16:43.8171 UT
    # Impact: 26-Sep-2022 23:14:24.183  UTC (actual)
    'mission_info': 'Horizons: -135. NASA\'s mission to test asteroid deflection.', 
    'mission_url': 'https://www.nasa.gov/dart'},

    {'name': 'JamesWebb', 'id': '-170', 'var_name': 'jwst_var', 'color_key': 'JamesWebb', 
    'symbol': 'diamond-open', 'object_type': 'trajectory', 'id_type': 'id', 'is_mission': True, 'start_date': datetime(2021, 12, 26), 'end_date': datetime(2030, 8, 18), 
    # 2021-12-25 13:01:09.184 (min. for current target body)
    # 2030-08-18 00:01:09.183 (max. for current target body)
    'mission_url': 'https://science.nasa.gov/mission/webb/', 
    'mission_info': 'Horizons: -170. The James Webb Space Telescope is NASA\'s flagship infrared space telescope.'},

    {'name': 'JUICE', 'id': '-28', 'var_name': 'juice_var', 'color_key': 'JUICE', 'symbol': 'diamond-open', 
    'object_type': 'trajectory', 'id_type': 'id', 'is_mission': True, 'start_date': datetime(2023, 4, 15), 'end_date': datetime(2031, 7, 21), 
    # 2023-04-14 12:43:26.843 (min. for current target body)
    # 2031-07-21 06:31:30.022 (max. for current target body)
    'mission_url': 'https://www.esa.int/esearch?q=juice', 
    'mission_info': 'Horizons: -28. JUICE (Jupiter Icy Moons Explorer) is an ESA mission to study Jupiter and its moons.'},

    {'name': 'Clipper', 'id': '-159', 'var_name': 'europa_clipper_var', 'color_key': 'Clipper', 'symbol': 'diamond-open', 
    'object_type': 'trajectory', 'id_type': 'id', 'is_mission': True, 'start_date': datetime(2024, 10, 15), 'end_date': datetime(2031, 2, 7), 
    # 2024-10-14 16:15:03.712 (min. for current target body)
    # 2031-02-07 18:17:27.695 (max. for current target body)
    # No ephemeris for target "Europa Clipper (spacecraft)" after A.D. 2031-FEB-07 18:16:18.5105 UT
    'mission_url': 'https://europa.nasa.gov/', 
    'mission_info': 'Horizons: -159. Europa Clipper will conduct detailed reconnaissance of Jupiter\'s moon Europa.'},

    {'name': 'BepiColombo', 'id': '-121', 'var_name': 'bepicolombo_var', 'color_key': 'BepiColombo', 'symbol': 'diamond-open', 
    # 'id': '-121', 2018-080A
    'object_type': 'trajectory', 'id_type': 'id', 'is_mission': True,
    'start_date': datetime(2018, 10, 21), 'end_date': datetime(2027, 4, 7), 
    # 2018-10-20 02:13:28.719 (min. for current target body)
    # 2027-04-07 00:01:09.186 (max. for current target body)
    # No ephemeris for target "BepiColombo (Spacecraft)" after A.D. 2027-APR-06 23:59:59.9998 UT
    'mission_url': 'https://sci.esa.int/web/bepicolombo', 
    'mission_info': 'Horizons: -121. BepiColombo is the joint ESA/JAXA mission to study Mercury, arriving in 2025.'},

    {'name': 'SolO', 'id': '-144', 'var_name': 'solarorbiter_var', 'color_key': 'SolO', 'symbol': 'diamond-open', 
    'object_type': 'trajectory', 'id_type': 'id', 'is_mission': True, 'start_date': datetime(2020, 2, 11), 'end_date': datetime(2030, 11, 20),
    # 2020-02-10 04:56:58.855 (min. for current target body)
    # 2030-11-20 04:03:15.162 (max. for current target body)
    # No ephemeris for target "Solar Orbiter (spacecraft)" after A.D. 2030-NOV-20 04:02:05.9789 UT 
    'mission_url': 'https://en.wikipedia.org/wiki/Solar_Orbiter', 
    'mission_info': 'Horizons: -144. Solar Orbiter ("SolO"), an ESA/NASA solar probe mission'},
        
    # --- Adding New Moons ---

    # Mars' Moons
    {'name': 'Phobos', 'id': '401', 'var_name': 'phobos_var', 'color_key': 'Phobos', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 401. Mars orbital period: 0.32 Earth days.', 
     'mission_url': 'https://science.nasa.gov/resource/martian-moon-phobos/'},

    {'name': 'Deimos', 'id': '402', 'var_name': 'deimos_var', 'color_key': 'Deimos', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 402. Mars orbital period: 1.26 Earth days. Retrogade.', 
     'mission_url': 'https://science.nasa.gov/mars/moons/deimos/'},

# Jupiter's Inner Ring Moons (Amalthea Group)
    {'name': 'Metis', 'id': '516', 'var_name': 'metis_var', 'color_key': 'Metis', 'symbol': 'circle', 'object_type': 'satellite',
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 516. Jupiter orbital period: 0.295 Earth days (7.08 hours).', 
     'mission_url': 'https://science.nasa.gov/jupiter/jupiter-moons/'},

    {'name': 'Adrastea', 'id': '515', 'var_name': 'adrastea_var', 'color_key': 'Adrastea', 'symbol': 'circle', 'object_type': 'satellite',
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 515. Jupiter orbital period: 0.298 Earth days (7.15 hours).', 
     'mission_url': 'https://science.nasa.gov/jupiter/jupiter-moons/'},

    {'name': 'Amalthea', 'id': '505', 'var_name': 'amalthea_var', 'color_key': 'Amalthea', 'symbol': 'circle', 'object_type': 'satellite',
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 505. Jupiter orbital period: 0.498 Earth days (11.95 hours).', 
     'mission_url': 'https://science.nasa.gov/jupiter/jupiter-moons/'},

    {'name': 'Thebe', 'id': '514', 'var_name': 'thebe_var', 'color_key': 'Thebe', 'symbol': 'circle', 'object_type': 'satellite',
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 514. Jupiter orbital period: 0.675 Earth days (16.20 hours).', 
     'mission_url': 'https://science.nasa.gov/jupiter/jupiter-moons/'},

    # Jupiter's Galilean Moons
    {'name': 'Io', 'id': '501', 'var_name': 'io_var', 'color_key': 'Io', 'symbol': 'circle', 'object_type': 'satellite', # instead of 501 use 59901?
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 501. Jupiter orbital period: 1.77 Earth days.', 
     'mission_url': 'https://science.nasa.gov/jupiter/jupiter-moons/io/'},

    {'name': 'Europa', 'id': '502', 'var_name': 'europa_var', 'color_key': 'Europa', 'symbol': 'circle', 'object_type': 'satellite',  # instead of id 502 use 59902?
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 502. Jupiter orbital period: 3.55 Earth days.', 
     'mission_url': 'https://science.nasa.gov/jupiter/jupiter-moons/europa/'},

    {'name': 'Ganymede', 'id': '503', 'var_name': 'ganymede_var', 'color_key': 'Ganymede', 'symbol': 'circle', 'object_type': 'satellite', # instead of 503 use 59903?
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 503. Jupiter orbital period: 7.15 Earth days.', 
     'mission_url': 'https://science.nasa.gov/jupiter/jupiter-moons/ganymede/'},

    {'name': 'Callisto', 'id': '504', 'var_name': 'callisto_var', 'color_key': 'Callisto', 'symbol': 'circle', 'object_type': 'satellite', # instead of 504 use 59904?
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 504. Jupiter orbital period: 16.69 Earth days.', 
     'mission_url': 'https://science.nasa.gov/jupiter/jupiter-moons/callisto/'},

    # Saturn's Major Moons

    {'name': 'Pan', 'id': '618', 'var_name': 'pan_var', 'color_key': 'Pan', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 618. Saturn orbital period: 0.58 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/pan/'},

    {'name': 'Daphnis', 'id': '635', 'var_name': 'daphnis_var', 'color_key': 'Daphnis', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 635. Saturn orbital period: 0.58 Earth days. No Horizons ephemeris after 1-16-2018.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/daphnis/'},

    {'name': 'Prometheus', 'id': '616', 'var_name': 'prometheus_var', 'color_key': 'Prometheus', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 616. Saturn orbital period: 0.61 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/prometheus/'},

    {'name': 'Pandora', 'id': '617', 'var_name': 'pandora_var', 'color_key': 'Pandora', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 617. Saturn orbital period: 0.63 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/pandora/'},

    {'name': 'Mimas', 'id': '601', 'var_name': 'mimas_var', 'color_key': 'Mimas', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 601. Saturn orbital period: 0.94 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/mimas/'},

    {'name': 'Enceladus', 'id': '602', 'var_name': 'enceladus_var', 'color_key': 'Enceladus', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 602. Saturn orbital period: 1.37 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/enceladus/'},

    {'name': 'Tethys', 'id': '603', 'var_name': 'tethys_var', 'color_key': 'Tethys', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons 603. Saturn orbital period: 1.89 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/tethys/'},

    {'name': 'Dione', 'id': '604', 'var_name': 'dione_var', 'color_key': 'Dione', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 604. Saturn orbital period: 2.74 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/dione/'},

    {'name': 'Rhea', 'id': '605', 'var_name': 'rhea_var', 'color_key': 'Rhea', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 605. Saturn orbital period: 4.52 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/rhea/'},

    {'name': 'Titan', 'id': '606', 'var_name': 'titan_var', 'color_key': 'Titan', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 606. Saturn orbital period: 15.95 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/titan/'},

    {'name': 'Hyperion', 'id': '607', 'var_name': 'hyperion_var', 'color_key': 'Hyperion', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 607. Saturn orbital period: 21 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/hyperion/'},

    {'name': 'Iapetus', 'id': '608', 'var_name': 'iapetus_var', 'color_key': 'Iapetus', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 608. Saturn orbital period: 79.33 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/iapetus/'},

    {'name': 'Phoebe', 'id': '609', 'var_name': 'phoebe_var', 'color_key': 'Phoebe', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 609. Retrograde. Saturn orbital period: 550.56 Earth days. Retrograde (left-handed) orbit.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/phoebe/'},

    # Uranus's Major Moons

    {'name': 'Ariel', 'id': '701', 'var_name': 'ariel_var', 'color_key': 'Ariel', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 701. Uranus orbital period: 2.52 Earth days.', 
     'mission_url': 'https://science.nasa.gov/uranus/moons/ariel/'},

    {'name': 'Umbriel', 'id': '702', 'var_name': 'umbriel_var', 'color_key': 'Umbriel', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 702. Uranus orbital period: 4.14 Earth days.', 
     'mission_url': 'https://science.nasa.gov/uranus/moons/umbriel/'},

    {'name': 'Titania', 'id': '703', 'var_name': 'titania_var', 'color_key': 'Titania', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 703. Uranus orbital period: 8.71 Earth days.', 
     'mission_url': 'https://science.nasa.gov/uranus/moons/titania/'},

    {'name': 'Oberon', 'id': '704', 'var_name': 'oberon_var', 'color_key': 'Oberon', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 704. Uranus orbital period: 13.46 Earth days.', 
     'mission_url': 'https://science.nasa.gov/uranus/moons/oberon/'},

    {'name': 'Miranda', 'id': '705', 'var_name': 'miranda_var', 'color_key': 'Miranda', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 705. Uranus orbital period: 1.41 Earth days.',
     'mission_url': 'https://science.nasa.gov/uranus/moons/miranda/'},   

    {'name': 'Portia', 'id': '712', 'var_name': 'portia_var', 'color_key': 'Portia', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 712. Uranus orbital period: 0.513196 Earth days or 12.317 hours.',
     'mission_url': 'https://science.nasa.gov/uranus/moons/portia/'}, 

    {'name': 'Mab', 'id': '726', 'var_name': 'mab_var', 'color_key': 'Mab', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 726. Uranus orbital period: 0.923293 Earth days or 22.159 hours.',
     'mission_url': 'https://science.nasa.gov/uranus/moons/mab/'},             

    # Neptune's Major Moons
    {'name': 'Triton', 'id': '801', 'var_name': 'triton_var', 'color_key': 'Triton', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 801. Retrograde. Neptune orbital period: 5.88 Earth days. Retrograde (left-handed) orbit.', 
     'mission_url': 'https://science.nasa.gov/neptune/moons/triton/'},

    {'name': 'Despina', 'id': '805', 'var_name': 'despina_var', 'color_key': 'Despina', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 805. Neptune orbital period: 0.334656 Earth days. Retrograde (left-handed) orbit.', 
     'mission_url': 'https://science.nasa.gov/neptune/moons/despina/'},

    {'name': 'Galatea', 'id': '806', 'var_name': 'galatea_var', 'color_key': 'Galatea', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 806. Neptune orbital period: 0.428744 Earth days. Retrograde (left-handed) orbit.', 
     'mission_url': 'https://science.nasa.gov/neptune/moons/galatea/'},

    # Pluto's Moon
    {'name': 'Charon', 'id': '901', 'var_name': 'charon_var', 'color_key': 'Charon', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 901. Pluto orbital period: 6.39 Earth days.', 
     'mission_url': 'https://science.nasa.gov/dwarf-planets/pluto/moons/charon/'},

    {'name': 'Styx', 'id': '905', 'var_name': 'styx_var', 'color_key': 'Styx', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 905. Pluto orbital period: 20.16 Earth days.', 
     'mission_url': 'https://science.nasa.gov/dwarf-planets/pluto/moons/styx/'},     

    {'name': 'Nix', 'id': '902', 'var_name': 'nix_var', 'color_key': 'Nix', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 902. Pluto orbital period: 24.86 Earth days.', 
     'mission_url': 'https://science.nasa.gov/dwarf-planets/pluto/moons/nix/'},

    {'name': 'Kerberos', 'id': '904', 'var_name': 'kerberos_var', 'color_key': 'Kerberos', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 904. Pluto orbital period: 32.17 Earth days.', 
     'mission_url': 'https://science.nasa.gov/dwarf-planets/pluto/moons/kerberos/'},

    {'name': 'Hydra', 'id': '903', 'var_name': 'hydra_var', 'color_key': 'Hydra', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Horizons: 903. Pluto orbital period: 38.20 Earth days.', 
     'mission_url': 'https://science.nasa.gov/dwarf-planets/pluto/moons/hydra/'},

    # Eris's Moon
#    {'name': 'Dysnomia', 'id': '120136199', 'var_name': 'dysnomia_var', 'color_key': 'Dysnomia', 'symbol': 'circle', 'object_type': 'satellite', 
#     'id_type': 'majorbody', 
#     'mission_info': 'Eris orbital period: 15.79 Earth days.', 
#     'mission_url': 'https://science.nasa.gov/resource/hubble-view-of-eris-and-dysnomia/'},

    # Eris's Moon
    {'name': 'Dysnomia', 'id': '120136199', 'var_name': 'dysnomia_var', 'color_key': 'Dysnomia', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody',
     'center_id': '120136199',  # Dysnomia body center (following 120XXXXXX pattern)
     'mission_info': 'Eris\'s moon. Period: 15.79 days. Both tidally locked. Diameter ~700 km.', 
     'mission_url': 'https://science.nasa.gov/resource/hubble-view-of-eris-and-dysnomia/'},

    # Gonggong's Moon
    {'name': 'Xiangliu', 'id': '120225088', 'var_name': 'xiangliu_var', 'color_key': 'Xiangliu', 'symbol': 'circle', 'object_type': 'satellite',
     'id_type': 'majorbody',
     'center_id': '120225088',  # Xiangliu body center (following 120XXXXXX pattern)
     'mission_info': 'Gonggong\'s moon. Period: 25.22 days. Diameter ~100 km.', 
     'mission_url': 'https://en.wikipedia.org/wiki/Xiangliu_(moon)'},

    # Orcus's Moon
    {'name': 'Vanth', 'id': '120090482', 'var_name': 'vanth_var', 'color_key': 'Van', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody',
     'center_id': '120090482',  # Vanth body center (following 120XXXXXX pattern)
     'mission_info': 'Orcus\'s moon. Period: 9.54 days. Diameter ~440 km. Highest mass ratio (~16%) of any known binary system.', 
     'mission_url': 'https://en.wikipedia.org/wiki/Vanth_(moon)'},

    # Quaoar's Moon
    {'name': 'Weywot', 'id': '120050000', 'var_name': 'weywot_var', 'color_key': 'Weywot', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody',
     'center_id': '120050000',  # Weywot body center (following 120XXXXXX pattern)
     'mission_info': 'Quaoar\'s moon. Period: 12.44 days. Diameter ~170 km.', 
     'mission_url': 'https://en.wikipedia.org/wiki/Weywot'},    

    # Haumea's Moons
    {'name': "Hi'iaka", 'id': '120136108', 'var_name': 'hiiaka_var', 'color_key': "Hi'iaka", 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody',
     'center_id': '120136108',  # Hi'iaka body center (following 120XXXXXX pattern)
     'mission_info': 'Haumea\'s outer moon. Period: 49 days. Diameter ~310 km. Named for Hawaiian goddess of childbirth.', 
     'mission_url': 'https://science.nasa.gov/dwarf-planets/haumea/'},

    {'name': 'Namaka', 'id': '220136108', 'var_name': 'namaka_var', 'color_key': 'Namaka', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody',
     'center_id': '220136108',  # Namaka body center (220XXXXXX pattern for second moon)
     'mission_info': 'Haumea\'s inner moon. Period: 18 days. Diameter ~170 km. Eccentric orbit perturbed by Hi\'iaka.', 
     'mission_url': 'https://science.nasa.gov/dwarf-planets/haumea/'},

    # Makemake's Moon
    {'name': 'MK2', 'id': '120136472', 'var_name': 'mk2_var', 'color_key': 'MK2', 'symbol': 'circle', 'object_type': 'satellite', 
     'id_type': 'majorbody', 
     'mission_info': 'Makemake\'s moon (S/2015 (136472) 1). Discovered 2015 by Hubble. Period: 18.023 days. Distance: ~22,250 km. Orbit edge-on to Earth.<br>' 
     'Very dark surface (~4% reflectivity), diameter ~175 km. No JPL ephemeris available - orbit from 2025 Hubble analysis.', 
     'mission_url': 'https://science.nasa.gov/dwarf-planets/makemake/'},

# ============== EXOPLANET SYSTEMS ==============
    
    # TRAPPIST-1 System (40.5 light-years)
    {'name': 'TRAPPIST-1', 'id': 'trappist1_star', 'var_name': 'trappist1_star_var',
     'color': 'rgba(0,0,0,0)', 'symbol': 'circle', 'object_type': 'exo_host_star',
     'id_type': 'host_star', 'system_id': 'trappist1',
     'mission_info': 'M8V red dwarf at 40.5 light-years hosting 7 Earth-sized planets, 3 in habitable zone.',
     'mission_url': 'https://exoplanets.nasa.gov/trappist1/'},
    
    {'name': 'TRAPPIST-1 b', 'id': 'trappist1b', 'var_name': 'trappist1b_var',
     'color': 'lightblue', 'symbol': 'circle', 'object_type': 'exoplanet',
     'id_type': 'exoplanet', 'system_id': 'trappist1',
     'semi_major_axis_au': 0.01154, 'period_days': 1.51087,
     'in_habitable_zone': False,
     'mission_info': 'Innermost planet, 1.5 day period. Too hot for liquid water (400 K).',
     'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7913/trappist-1-b/'},
    
    {'name': 'TRAPPIST-1 c', 'id': 'trappist1c', 'var_name': 'trappist1c_var',
     'color': 'lightblue', 'symbol': 'circle', 'object_type': 'exoplanet',
     'id_type': 'exoplanet', 'system_id': 'trappist1',
     'semi_major_axis_au': 0.01580, 'period_days': 2.42182,
     'in_habitable_zone': False,
     'mission_info': '2.4 day period. JWST observations show no significant atmosphere.',
     'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7914/trappist-1-c/'},
    
    {'name': 'TRAPPIST-1 d', 'id': 'trappist1d', 'var_name': 'trappist1d_var',
     'color': 'green', 'symbol': 'circle', 'object_type': 'exoplanet',
     'id_type': 'exoplanet', 'system_id': 'trappist1',
     'semi_major_axis_au': 0.02227, 'period_days': 4.04961,
     'in_habitable_zone': True,
     'mission_info': '* IN HABITABLE ZONE * Inner edge, 4.0 day period. May have water.',
     'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7915/trappist-1-d/'},
    
    {'name': 'TRAPPIST-1 e', 'id': 'trappist1e', 'var_name': 'trappist1e_var',
     'color': 'green', 'symbol': 'circle', 'object_type': 'exoplanet',
     'id_type': 'exoplanet', 'system_id': 'trappist1',
     'semi_major_axis_au': 0.02925, 'period_days': 6.09965,
     'in_habitable_zone': True,
     'mission_info': '* IN HABITABLE ZONE * PRIME CANDIDATE! Most likely to have liquid water. 6.1 day period.',
     'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7916/trappist-1-e/'},
    
    {'name': 'TRAPPIST-1 f', 'id': 'trappist1f', 'var_name': 'trappist1f_var',
     'color': 'green', 'symbol': 'circle', 'object_type': 'exoplanet',
     'id_type': 'exoplanet', 'system_id': 'trappist1',
     'semi_major_axis_au': 0.03849, 'period_days': 9.20669,
     'in_habitable_zone': True,
     'mission_info': '* IN HABITABLE ZONE * 9.2 day period. May have significant water content.',
     'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7917/trappist-1-f/'},
    
    {'name': 'TRAPPIST-1 g', 'id': 'trappist1g', 'var_name': 'trappist1g_var',
     'color': 'green', 'symbol': 'circle', 'object_type': 'exoplanet',
     'id_type': 'exoplanet', 'system_id': 'trappist1',
     'semi_major_axis_au': 0.04683, 'period_days': 12.35294,
     'in_habitable_zone': True,
     'mission_info': '* IN HABITABLE ZONE * Outer edge, 12.4 day period. May have subsurface ocean.',
     'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7918/trappist-1-g/'},
    
    {'name': 'TRAPPIST-1 h', 'id': 'trappist1h', 'var_name': 'trappist1h_var',
     'color': 'lightblue', 'symbol': 'circle', 'object_type': 'exoplanet',
     'id_type': 'exoplanet', 'system_id': 'trappist1',
     'semi_major_axis_au': 0.06189, 'period_days': 18.76712,
     'in_habitable_zone': False,
     'mission_info': 'Outermost planet, 18.8 day period. Too cold for liquid water (173 K).',
     'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7919/trappist-1-h/'},
    
    # TOI-1338 System (1,292 light-years, Binary + Circumbinary)
    {'name': 'TOI-1338 A/B', 'id': 'toi1338_barycenter', 'var_name': 'toi1338_barycenter_var',
     'color': 'white', 'symbol': 'square-open', 'object_type': 'exo_barycenter',
     'id_type': 'barycenter', 'system_id': 'toi1338',
     'mission_info': 'Binary system barycenter (center of mass). Both stars orbit this point.',
     'mission_url': 'https://exoplanets.nasa.gov/news/1644/discovery-alert-first-planet-found-by-tess/'},
    
    {'name': 'TOI-1338 A (G-type)', 'id': 'toi1338_starA', 'var_name': 'toi1338_starA_var',
     'color': 'yellow', 'symbol': 'circle', 'object_type': 'exo_binary_star',
     'id_type': 'binary_star_a', 'system_id': 'toi1338',
     'mission_info': 'Primary star in binary system. G-type, 1.1 solar masses, like our Sun.',
     'mission_url': 'https://exoplanets.nasa.gov/news/1644/discovery-alert-first-planet-found-by-tess/'},
    
    {'name': 'TOI-1338 B (M-type)', 'id': 'toi1338_starB', 'var_name': 'toi1338_starB_var',
     'color': 'orange', 'symbol': 'circle', 'object_type': 'exo_binary_star',
     'id_type': 'binary_star_b', 'system_id': 'toi1338',
     'mission_info': 'Secondary star in binary. M-type red dwarf, 0.3 solar masses. Binary period: 14.6 days.',
     'mission_url': 'https://exoplanets.nasa.gov/news/1644/discovery-alert-first-planet-found-by-tess/'},
    
    {'name': 'TOI-1338 b', 'id': 'toi1338b', 'var_name': 'toi1338b_var',
     'color': 'lightblue', 'symbol': 'circle', 'object_type': 'exoplanet',
     'id_type': 'exoplanet', 'system_id': 'toi1338',
     'semi_major_axis_au': 0.4607, 'period_days': 95.196,
     'in_habitable_zone': False,
     'mission_info': 'Neptune-sized circumbinary planet. Discovered by Wolf Cukier (17-year-old TESS intern)!',
     'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/8452/toi-1338-b/'},
    
    {'name': 'TOI-1338 c', 'id': 'toi1338c', 'var_name': 'toi1338c_var',
     'color': 'lightblue', 'symbol': 'circle', 'object_type': 'exoplanet',
     'id_type': 'exoplanet', 'system_id': 'toi1338',
     'semi_major_axis_au': 0.76, 'period_days': 215.5,
     'in_habitable_zone': False,
     'mission_info': 'Jupiter-mass circumbinary planet. Confirmed 2023. Only second known multi-planet circumbinary system.',
     'mission_url': 'https://arxiv.org/abs/2305.16894'},
    
    # Proxima Centauri System (4.24 light-years - NEAREST!)
    {'name': 'Proxima Centauri', 'id': 'proxima_star', 'var_name': 'proxima_star_var',
     'color': 'rgba(0,0,0,0)', 'symbol': 'circle', 'object_type': 'exo_host_star',
     'id_type': 'host_star', 'system_id': 'proxima',
     'mission_info': 'NEAREST star to the Sun! M5.5V red dwarf at 4.24 light-years. Part of Alpha Centauri system.',
     'mission_url': 'https://exoplanets.nasa.gov/proxima-b/'},
    
    {'name': 'Proxima Centauri b', 'id': 'proximab', 'var_name': 'proximab_var',
     'color': 'green', 'symbol': 'circle', 'object_type': 'exoplanet',
     'id_type': 'exoplanet', 'system_id': 'proxima',
     'semi_major_axis_au': 0.04856, 'period_days': 11.18427,
     'in_habitable_zone': True,
     'mission_info': '* IN HABITABLE ZONE * NEAREST EXOPLANET! 11.2 day period. Stellar flares may challenge habitability.',
     'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7167/proxima-centauri-b/'},
    
    {'name': 'Proxima Centauri d', 'id': 'proximad', 'var_name': 'proximad_var',
     'color': 'lightblue', 'symbol': 'circle', 'object_type': 'exoplanet',
     'id_type': 'exoplanet', 'system_id': 'proxima',
     'semi_major_axis_au': 0.029, 'period_days': 5.122,
     'in_habitable_zone': False,
     'mission_info': 'Sub-Earth mass planet (0.26 Mearth). Lightest planet detected by radial velocity method.',
     'mission_url': 'https://www.eso.org/public/news/eso2202/'},

]


def build_objects_list(definitions, vars_dict, color_map_func):
    """
    Build the runtime objects list from definitions.
    
    Args:
        definitions: OBJECT_DEFINITIONS list
        vars_dict: Dictionary mapping var_name strings to tk.IntVar instances
        color_map_func: The color_map function from constants_new
    
    Returns:
        List of object dictionaries with 'var' and 'color' resolved
    """
    objects = []
    for defn in definitions:
        obj = defn.copy()
        
        # Resolve var reference
        var_name = obj.pop('var_name', None)
        if var_name and var_name in vars_dict:
            obj['var'] = vars_dict[var_name]
        
        # Resolve color
        color_key = obj.pop('color_key', obj.get('name', 'default'))
        obj['color'] = color_map_func(color_key)
        
        objects.append(obj)
    
    return objects


def get_all_var_names():
    """Return list of all var_name strings needed for IntVar creation."""
    return [d.get('var_name') for d in OBJECT_DEFINITIONS if d.get('var_name')]


# =============================================================================
# SHELL DEFINITIONS FOR PLANETARY CHECKBOXES (Phase 2)
# =============================================================================
# Each body maps to a list of shells. Each shell has:
#   - var_suffix: the part after {body}_ in the var name (e.g., 'inner_core' for 'mercury_inner_core_var')
#   - label: the checkbox text (e.g., '-- Inner Core')
#   - tooltip_var: the variable name for the tooltip info (defaults to {body}_{var_suffix}_info)
#
# NOTE: Sun is excluded - it has a complex multi-section structure that's better left as-is.
# NOTE: Earth is excluded - it has a special "Earth System Visualization" checkbox with 
#       custom formatting, color, and callback that requires manual handling.

SHELL_DEFINITIONS = {
    'Mercury': [
        {'var_suffix': 'inner_core', 'label': '-- Inner Core'},
        {'var_suffix': 'outer_core', 'label': '-- Outer Core'},
        {'var_suffix': 'mantle', 'label': '-- Mantle'},
        {'var_suffix': 'crust', 'label': '-- Crust'},
        {'var_suffix': 'atmosphere', 'label': '-- Exosphere'},
        {'var_suffix': 'sodium_tail', 'label': '-- Sodium Tail'},
        {'var_suffix': 'magnetosphere', 'label': '-- Magnetosphere'},
        {'var_suffix': 'hill_sphere', 'label': '-- Hill Sphere'},
    ],
    'Venus': [
        {'var_suffix': 'core', 'label': '-- Core'},
        {'var_suffix': 'mantle', 'label': '-- Mantle'},
        {'var_suffix': 'crust', 'label': '-- Crust'},
        {'var_suffix': 'atmosphere', 'label': '-- Atmosphere'},
        {'var_suffix': 'upper_atmosphere', 'label': '-- Upper Atmosphere'},
        {'var_suffix': 'magnetosphere', 'label': '-- Magnetosphere'},
        {'var_suffix': 'hill_sphere', 'label': '-- Hill Sphere'},
    ],
    # Earth excluded - has special "Earth System Visualization" checkbox
    'Moon': [
        {'var_suffix': 'inner_core', 'label': '-- Inner Core'},
        {'var_suffix': 'outer_core', 'label': '-- Outer Core'},
        {'var_suffix': 'mantle', 'label': '-- Mantle'},
        {'var_suffix': 'crust', 'label': '-- Crust'},
        {'var_suffix': 'exosphere', 'label': '-- Exosphere'},
        {'var_suffix': 'hill_sphere', 'label': '-- Hill Sphere'},
    ],
    'Mars': [
        {'var_suffix': 'inner_core', 'label': '-- Inner Core'},
        {'var_suffix': 'outer_core', 'label': '-- Outer Core'},
        {'var_suffix': 'mantle', 'label': '-- Mantle'},
        {'var_suffix': 'crust', 'label': '-- Crust'},
        {'var_suffix': 'atmosphere', 'label': '-- Atmosphere'},
        {'var_suffix': 'upper_atmosphere', 'label': '-- Upper Atmosphere'},
        {'var_suffix': 'magnetosphere', 'label': '-- Magnetosphere'},
        {'var_suffix': 'hill_sphere', 'label': '-- Hill Sphere'},
    ],
    'Jupiter': [
        {'var_suffix': 'core', 'label': '-- Core'},
        {'var_suffix': 'metallic_hydrogen', 'label': '-- Metallic Hydrogen Layer'},
        {'var_suffix': 'molecular_hydrogen', 'label': '-- Molecular Hydrogen Layer'},
        {'var_suffix': 'cloud_layer', 'label': '-- Cloud Layer'},
        {'var_suffix': 'upper_atmosphere', 'label': '-- Upper Atmosphere'},
        {'var_suffix': 'ring_system', 'label': '-- Ring System'},
        {'var_suffix': 'radiation_belts', 'label': '-- Radiation Belts'},
        {'var_suffix': 'io_plasma_torus', 'label': '-- Io Plasma Torus'},
        {'var_suffix': 'magnetosphere', 'label': '-- Magnetosphere'},
        {'var_suffix': 'hill_sphere', 'label': '-- Hill Sphere'},
    ],
    'Saturn': [
        {'var_suffix': 'core', 'label': '-- Core'},
        {'var_suffix': 'metallic_hydrogen', 'label': '-- Metallic Hydrogen Layer'},
        {'var_suffix': 'molecular_hydrogen', 'label': '-- Molecular Hydrogen Layer'},
        {'var_suffix': 'cloud_layer', 'label': '-- Cloud Layer'},
        {'var_suffix': 'upper_atmosphere', 'label': '-- Upper Atmosphere'},
        {'var_suffix': 'ring_system', 'label': '-- Ring System'},
        {'var_suffix': 'radiation_belts', 'label': '-- Radiation Belts'},
        {'var_suffix': 'enceladus_plasma_torus', 'label': '-- Enceladus Plasma Torus'},
        {'var_suffix': 'magnetosphere', 'label': '-- Magnetosphere'},
        {'var_suffix': 'hill_sphere', 'label': '-- Hill Sphere'},
    ],
    'Uranus': [
        {'var_suffix': 'core', 'label': '-- Core'},
        {'var_suffix': 'mantle', 'label': '-- Mantle'},
        {'var_suffix': 'cloud_layer', 'label': '-- Cloud Layer'},
        {'var_suffix': 'upper_atmosphere', 'label': '-- Upper Atmosphere'},
        {'var_suffix': 'ring_system', 'label': '-- Ring System'},
        {'var_suffix': 'radiation_belts', 'label': '-- Radiation Belts'},
        {'var_suffix': 'magnetosphere', 'label': '-- Magnetosphere'},
        {'var_suffix': 'hill_sphere', 'label': '-- Hill Sphere'},
    ],
    'Neptune': [
        {'var_suffix': 'core', 'label': '-- Core'},
        {'var_suffix': 'mantle', 'label': '-- Mantle'},
        {'var_suffix': 'cloud_layer', 'label': '-- Cloud Layer'},
        {'var_suffix': 'upper_atmosphere', 'label': '-- Upper Atmosphere'},
        {'var_suffix': 'ring_system', 'label': '-- Ring System'},
        {'var_suffix': 'radiation_belts', 'label': '-- Radiation Belts'},
        {'var_suffix': 'magnetosphere', 'label': '-- Magnetosphere'},
        {'var_suffix': 'hill_sphere', 'label': '-- Hill Sphere'},
    ],
    'Pluto': [
        {'var_suffix': 'core', 'label': '-- Core'},
        {'var_suffix': 'mantle', 'label': '-- Mantle'},
        {'var_suffix': 'crust', 'label': '-- Crust'},
        {'var_suffix': 'haze_layer', 'label': '-- Haze Layer'},
        {'var_suffix': 'atmosphere', 'label': '-- Atmosphere'},
        {'var_suffix': 'hill_sphere', 'label': '-- Hill Sphere'},
    ],
    'Eris': [
        {'var_suffix': 'core', 'label': '-- Core'},
        {'var_suffix': 'mantle', 'label': '-- Mantle'},
        {'var_suffix': 'crust', 'label': '-- Crust'},
        {'var_suffix': 'atmosphere', 'label': '-- Atmosphere'},
        {'var_suffix': 'hill_sphere', 'label': '-- Hill Sphere'},
    ],
    'Planet 9': [
        {'var_suffix': 'surface', 'label': '-- Surface'},
        {'var_suffix': 'hill_sphere', 'label': '-- Hill Sphere'},
    ],
}


def get_shell_var_names():
    """Return list of all shell var_name strings needed for IntVar creation."""
    var_names = []
    for body, shells in SHELL_DEFINITIONS.items():
        body_prefix = body.lower().replace(' ', '')  # 'Planet 9' -> 'planet9'
        for shell in shells:
            var_names.append(f"{body_prefix}_{shell['var_suffix']}_var")
    return var_names


def get_shell_tooltip_names():
    """Return list of all shell tooltip info variable names."""
    tooltip_names = []
    for body, shells in SHELL_DEFINITIONS.items():
        body_prefix = body.lower().replace(' ', '')
        for shell in shells:
            tooltip_names.append(f"{body_prefix}_{shell['var_suffix']}_info")
    return tooltip_names


def build_shell_checkboxes(body_name, parent_frame, vars_dict, tooltips_dict, tk_module, CreateToolTip):
    """
    Build shell checkboxes for a single body.
    
    Args:
        body_name: Name of the body (e.g., 'Mercury', 'Venus')
        parent_frame: The parent tk.Frame (usually celestial_frame)
        vars_dict: Dictionary mapping var_name strings to tk.IntVar instances
        tooltips_dict: Dictionary mapping tooltip_name strings to info text
        tk_module: The tkinter module (pass tk)
        CreateToolTip: The CreateToolTip class
    
    Returns:
        The shell_options_frame created, or None if body has no shells
    """
    if body_name not in SHELL_DEFINITIONS:
        return None
    
    shells = SHELL_DEFINITIONS[body_name]
    body_prefix = body_name.lower().replace(' ', '')
    
    # Create indented frame for shell options
    shell_frame = tk_module.Frame(parent_frame)
    shell_frame.pack(padx=(20, 0), anchor='w')
    
    # Create checkboxes for each shell
    for shell in shells:
        var_name = f"{body_prefix}_{shell['var_suffix']}_var"
        tooltip_name = f"{body_prefix}_{shell['var_suffix']}_info"
        
        var = vars_dict.get(var_name)
        tooltip_text = tooltips_dict.get(tooltip_name, "No information available")
        
        if var is not None:
            cb = tk_module.Checkbutton(shell_frame, text=shell['label'], variable=var)
            cb.pack(anchor='w')
            CreateToolTip(cb, tooltip_text)
    
    return shell_frame
