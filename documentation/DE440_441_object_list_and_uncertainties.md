# High-precision uncertainty values for solar system bodies
# Based on DE440/441 planetary ephemeris and mission data
# Values in arcseconds (3-sigma)
MAJOR_BODY_UNCERTAINTIES = {
    # ========== PLANETS ========== all done
    'Mercury': 0.005,
    'Venus': 0.003,
    'Mars': 0.002,
    'Jupiter': 0.05,
    'Saturn': 0.1,
    'Uranus': 0.3,
    'Neptune': 0.5,
    
    # ========== DWARF PLANETS ==========
    'Ceres': 0.01,      # Dawn mission
    'Pluto': 0.8,       # New Horizons
    'Eris': 5.0,
    'Makemake': 3.0,
    'Haumea': 2.0,
    'Gonggong': 5.0,    # 2007 OR10
    'Quaoar': 3.0,
    'Sedna': 10.0,
    'Orcus': 3.0,
    'Salacia': 5.0,     # need
    'Varuna': 5.0,
    'Ixion': 5.0,
    '2002 MS4': 8.0,    # Mani, done
    'Varda': 8.0,       # need
    
    # ========== EARTH'S MOON ========== done
    'Moon': 0.0001,     # Lunar laser ranging
    
    # ========== MARTIAN MOONS ========== done
    'Phobos': 0.01,
    'Deimos': 0.02,
    
    # ========== JOVIAN MOONS ==========
    'Io': 0.01,
    'Europa': 0.01,
    'Ganymede': 0.01,
    'Callisto': 0.01,
    'Amalthea': 0.05,
    'Himalia': 0.1,
    'Thebe': 0.05,
    'Metis': 0.05,
    'Adrastea': 0.05,
    'Pasiphae': 0.5,
    'Sinope': 0.5,
    'Lysithea': 0.5,
    'Carme': 0.5,
    'Ananke': 0.5,
    'Leda': 0.5,
    'Elara': 0.3,
    
    # ========== SATURNIAN MOONS ==========
    'Mimas': 0.05,
    'Enceladus': 0.05,
    'Tethys': 0.05,
    'Dione': 0.05,
    'Rhea': 0.05,
    'Titan': 0.05,
    'Hyperion': 0.1,
    'Iapetus': 0.1,
    'Phoebe': 0.2,
    'Janus': 0.05,
    'Epimetheus': 0.05,
    'Helene': 0.1,
    'Telesto': 0.1,
    'Calypso': 0.1,
    'Atlas': 0.05,
    'Prometheus': 0.05,
    'Pandora': 0.05,
    'Pan': 0.05,
    'Daphnis': 0.05,
    
    # ========== URANIAN MOONS ========== plus new number 29
    'Ariel': 0.3,
    'Umbriel': 0.3,
    'Titania': 0.3,
    'Oberon': 0.3,
    'Miranda': 0.3,
    'Puck': 0.5,
    'Cordelia': 0.5,
    'Ophelia': 0.5,
    'Bianca': 0.5,
    'Cressida': 0.5,
    'Desdemona': 0.5,
    'Juliet': 0.5,
    'Portia': 0.5,
    'Rosalind': 0.5,
    'Belinda': 0.5,
    
    # ========== NEPTUNIAN MOONS ==========
    'Triton': 0.5,
    'Nereid': 1.0,
    'Proteus': 0.8,
    'Larissa': 0.8,
    'Galatea': 0.8,
    'Despina': 0.8,
    'Thalassa': 0.8,
    'Naiad': 0.8,
    
    # ========== PLUTONIAN SYSTEM ========== done
    'Charon': 1.0,
    'Nix': 2.0,
    'Hydra': 2.0,
    'Kerberos': 3.0,
    'Styx': 3.0,
    
    # ========== MAIN BELT ASTEROIDS (DE440 perturbers) ==========
    'Vesta': 0.01,      # Dawn mission
    'Pallas': 0.05,
    'Juno': 0.1,
    'Hygiea': 0.2,
    'Davida': 0.2,
    'Interamnia': 0.3,
    'Europa (asteroid)': 0.3,  # 52 Europa
    'Eunomia': 0.2,
    'Psyche': 0.1,      # Upcoming mission
    'Euphrosyne': 0.3,
    'Cybele': 0.3,
    'Sylvia': 0.2,
    'Thisbe': 0.3,
    'Camilla': 0.3,
    'Herculina': 0.3,
    'Doris': 0.3,
    
    # ========== MISSION-VISITED ASTEROIDS ==========
    'Bennu': 0.001,     # OSIRIS-REx
    'Ryugu': 0.001,     # Hayabusa2
    'Eros': 0.001,      # NEAR Shoemaker
    'Itokawa': 0.001,   # Hayabusa
    'Mathilde': 0.01,   # NEAR flyby
    'Ida': 0.01,        # Galileo
    'Dactyl': 0.02,     # Ida's moon
    'Gaspra': 0.01,     # Galileo
    'Lutetia': 0.01,    # Rosetta
    'Steins': 0.01,     # Rosetta
    'Annefrank': 0.05,  # Stardust
    'Braille': 0.05,    # Deep Space 1
    'Toutatis': 0.001,  # Radar + Chang'e 2
    'Didymos': 0.01,    # DART impact
    'Dimorphos': 0.02,  # Didymos moon
    'Arrokoth': 1.0,    # New Horizons (2014 MU69); done
    
    # ========== NEAR-EARTH ASTEROIDS (Radar observed) ==========
    'Apophis': 0.001,
    '2005 YU55': 0.01,
    '1999 JM8': 0.01,
    '2004 BL86': 0.01,
    '2000 DP107': 0.01,
    '1998 KY26': 0.01,
    '2017 YE5': 0.01,
    '1999 KW4': 0.01,
    '2003 YT1': 0.01,
    '2014 HQ124': 0.01,
    '2014 JO25': 0.01,
    '2015 TB145': 0.01,
    
    # ========== TROJAN ASTEROIDS ==========
    'Patroclus': 1.0,   # Lucy target (binary)
    'Menoetius': 1.0,   # Patroclus companion
    'Eurybates': 1.0,   # Lucy target
    'Polymele': 1.0,    # Lucy target
    'Leucus': 1.0,      # Lucy target
    'Orus': 1.0,        # Lucy target
    'Donald Johanson': 1.0,  # Lucy target
    'Hektor': 0.5,      # Largest trojan
    'Agamemnon': 1.0,
    'Achilles': 1.0,
    'Nestor': 1.0,
    'Diomedes': 1.0,
    
    # ========== CENTAURS ==========
    'Chiron': 2.0,
    'Pholus': 5.0,
    'Nessus': 8.0,
    'Asbolus': 8.0,
    'Chariklo': 3.0,    # Has rings; done
    'Hylonome': 10.0,
    'Bienor': 10.0,
    'Amycus': 10.0,
    
    # ========== COMET NUCLEI ==========
    'Halley': 10.0,     # Currently distant
    'Encke': 1.0,       # Short period
    'Tempel 1': 0.5,    # Deep Impact
    'Wild 2': 0.01,     # Stardust
    'Borrelly': 0.01,   # Deep Space 1
    'Churyumov-Gerasimenko': 0.001,  # Rosetta (67P)
    '67P/Churyumov-Gerasimenko': 0.001,  # Alternative designation
    'Hartley 2': 0.01,  # EPOXI
    'Giacobini-Zinner': 1.0,  # ICE
    'Grigg-Skjellerup': 1.0,   # Giotto
    'Wirtanen': 0.5,    # Original Rosetta target
    'Schwassmann-Wachmann 3': 2.0,
    'Holmes': 5.0,
    'Hale-Bopp': 20.0,  # Currently very distant
    'Hyakutake': 15.0,
    'McNaught': 10.0,
    'ISON': 10.0,       # Destroyed
    'Lovejoy': 5.0,
    'NEOWISE': 3.0,
    'PanSTARRS': 5.0,
    'Borisov': 10.0,    # Interstellar
    
    # ========== SPACECRAFT (when tracked as objects) ==========
    'Voyager 1': 100.0,     # done
    'Voyager 2': 100.0,     # done
    'New Horizons': 10.0,   # done
    'Pioneer 10': 1000.0,   # Contact lost; done
    'Pioneer 11': 1000.0,   # Contact lost; done
    'Cassini': 0.1,         # When active; done
    'Juno': 0.01,           # Currently at Jupiter; done
    'Dawn': 0.01,           # Mission ended at Ceres
    'OSIRIS-REx': 0.01,
    'Hayabusa2': 0.01,
    'Parker Solar Probe': 0.001,
    'Solar Orbiter': 0.01,
    'BepiColombo': 0.01,
    'JUICE': 0.01,
    'Europa Clipper': 0.01,
    'Lucy': 0.01,
    'Psyche (spacecraft)': 0.01,
    'Dragonfly': 0.1,       # Future
    'Apollo 11'             # unknown uncertainty; done
    'SOHO'                  # unknown uncertainty; done
    
    # ========== SPECIAL OBJECTS ==========
    'Sun': 0.001,       # Barycenter position
    'Earth-Moon Barycenter': 0.0001,
    'Pluto-Charon Barycenter': 0.5,
    
    # ========== ARTIFICIAL SATELLITES (if tracking) ==========
    'ISS': 0.001,       # International Space Station
    'HST': 0.001,       # Hubble Space Telescope
    'JWST': 0.01,       # James Webb Space Telescope
    'Gaia': 0.001,
    'TESS': 0.001,
    'Spitzer': 0.01,
    'Kepler': 0.01,
    'WMAP': 0.1,
    'Planck': 0.1,
    
    # ========== METEOR SHOWER PARENTS ==========
    'Swift-Tuttle': 5.0,    # Perseids
    'Tempel-Tuttle': 3.0,   # Leonids
    'Thatcher': 10.0,       # Lyrids
    'Phaethon': 0.1,        # Geminids (asteroid)
}