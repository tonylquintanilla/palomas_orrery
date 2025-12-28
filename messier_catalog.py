# messier_catalog.py

messier_catalog = {
    'M1': {
        'name': 'Crab Nebula',
        'type': 'Supernova Remnant',
        'vmag': 8.4,
        'distance_ly': 6500,
        'ra': '05h34m31.94s',
        'dec': '+22 deg00 arcmin52.2 arcsec',
        'notes': 'Remnant of supernova observed in 1054 AD. Contains a pulsar.',
    },
    'M8': {
        'name': 'Lagoon Nebula',
        'type': 'Emission Nebula',
        'vmag': 6.0,
        'distance_ly': 5200,
        'ra': '18h03m37s',
        'dec': '-24 deg23 arcmin12 arcsec',
        'notes': 'Contains many young stars. Active star formation region.',
    },
    'M16': {
        'name': 'Eagle Nebula',
        'type': 'Emission Nebula',
        'vmag': 6.0,
        'distance_ly': 7000,
        'ra': '18h18m48s',
        'dec': '-13 deg47 arcmin00 arcsec',
        'notes': 'Famous for the "Pillars of Creation" imaged by Hubble.',
    },
    'M17': {
        'name': 'Omega Nebula',
        'type': 'Emission Nebula',
        'vmag': 6.0,
        'distance_ly': 5500,
        'ra': '18h20m26s',
        'dec': '-16 deg10 arcmin36 arcsec',
        'notes': 'Also known as Swan Nebula. Active star formation region.',
    },
    'M20': {
        'name': 'Trifid Nebula',
        'type': 'Emission/Reflection Nebula',
        'vmag': 6.3,
        'distance_ly': 5200,
        'ra': '18h02m23s',
        'dec': '-23 deg01 arcmin48 arcsec',
        'notes': 'Combination of emission and reflection nebula divided by dark dust lanes.',
    },
    'M27': {
        'name': 'Dumbbell Nebula',
        'type': 'Planetary Nebula',
        'vmag': 7.5,
        'distance_ly': 1360,
        'ra': '19h59m36.3s',
        'dec': '+22 deg43 arcmin16 arcsec',
        'notes': 'First planetary nebula ever discovered.',
    },
    'M42': {
        'name': 'Orion Nebula',
        'type': 'Emission Nebula',
        'vmag': 4.0,
        'distance_ly': 1344,
        'ra': '05h35m17.3s',
        'dec': '-05 deg23 arcmin28 arcsec',
        'notes': 'Brightest diffuse nebula in the sky. Contains the Trapezium Cluster.',
    },
    'M43': {
        'name': 'De Mairan\'s Nebula',
        'type': 'HII Region',
        'vmag': 9.0,
        'distance_ly': 1600,
        'ra': '05h35m31.3s',
        'dec': '-05 deg16 arcmin03 arcsec',
        'notes': 'Part of the Orion Nebula complex.',
    },
    'M57': {
        'name': 'Ring Nebula',
        'type': 'Planetary Nebula',
        'vmag': 8.8,
        'distance_ly': 2300,
        'ra': '18h53m35.1s',
        'dec': '+33 deg01 arcmin45 arcsec',
        'notes': 'Classic example of a planetary nebula.',
    },
    'M76': {
        'name': 'Little Dumbbell Nebula',
        'type': 'Planetary Nebula',
        'vmag': 10.1,
        'distance_ly': 3400,
        'ra': '01h42m19.9s',
        'dec': '+51 deg34 arcmin31 arcsec',
        'notes': 'Also known as Cork Nebula or Butterfly Nebula.',
    },
    'M78': {
        'name': 'Messier 78',
        'type': 'Reflection Nebula',
        'vmag': 8.3,
        'distance_ly': 1600,
        'ra': '05h46m45.8s',
        'dec': '+00 deg04 arcmin48 arcsec',
        'notes': 'Brightest reflection nebula in the sky.',
    },
    'M97': {
        'name': 'Owl Nebula',
        'type': 'Planetary Nebula',
        'vmag': 9.9,
        'distance_ly': 2600,
        'ra': '11h14m47.7s',
        'dec': '+55 deg01 arcmin09 arcsec',
        'notes': 'Resembles an owl\'s face with large dark eyes.',
    }
}

# Star Clusters
star_cluster_catalog = {
    'M6': {
        'name': 'Butterfly Cluster',
        'type': 'Open Cluster',
        'vmag': 4.2,
        'distance_ly': 1600,
        'ra': '17h40m20.8s',
        'dec': '-32 deg15 arcmin12 arcsec',
        'notes': 'Contains about 80 stars. Resembles a butterfly.',
    },
    'M7': {
        'name': 'Ptolemy Cluster',
        'type': 'Open Cluster',
        'vmag': 3.3,
        'distance_ly': 980,
        'ra': '17h53m51.2s',
        'dec': '-34 deg47 arcmin34 arcsec',
        'notes': 'Visible to naked eye. Known to Ptolemy in 130 AD.',
    },
    'M11': {
        'name': 'Wild Duck Cluster',
        'type': 'Open Cluster',
        'vmag': 5.8,
        'distance_ly': 6200,
        'ra': '18h51m05s',
        'dec': '-06 deg16 arcmin12 arcsec',
        'notes': 'Rich, compact cluster. Contains about 3000 stars.',
    },
    'M44': {
        'name': 'Beehive Cluster',
        'type': 'Open Cluster',
        'vmag': 3.7,
        'distance_ly': 577,
        'ra': '08h40m6.0s',
        'dec': '+19 deg59 arcmin00 arcsec',
        'notes': 'Open cluster in Cancer.',
    },
    'M45': {
        'name': 'Pleiades',
        'type': 'Open Cluster',
        'vmag': 1.6,
        'distance_ly': 440,
        'ra': '03h47m0s',
        'dec': '+24 deg07 arcmin00 arcsec',
        'notes': 'Open cluste in Taurus.',
    },
}

# Additional bright galactic objects (vmag <= 9.0)

bright_planetaries = {
    'NGC 7293': {
        'name': 'Helix Nebula',
        'type': 'Planetary Nebula',
        'vmag': 7.6,
        'distance_ly': 650,
        'ra': '22h29m38.6s',
        'dec': '-20 deg50 arcmin14 arcsec',
        'notes': 'Nearest bright planetary nebula to Earth. Appears as a large, ring-like structure.',
    },
    'NGC 3242': {
        'name': 'Ghost of Jupiter',
        'type': 'Planetary Nebula',
        'vmag': 8.6,
        'distance_ly': 1400,
        'ra': '10h24m46.1s',
        'dec': '-18 deg38 arcmin33 arcsec',
        'notes': 'Appears similar in size to Jupiter through a telescope. Shows a distinctive blue-green color.',
    },
    'NGC 2392': {
        'name': 'Eskimo Nebula',
        'type': 'Planetary Nebula',
        'vmag': 9.0,
        'distance_ly': 2870,
        'ra': '07h29m10.8s',
        'dec': '+20 deg54 arcmin42.5 arcsec',
        'notes': 'Distinctive appearance resembling a face surrounded by a fur parka hood.',
    },
}

bright_open_clusters = {
    'NGC 752': {
        'name': 'Caldwell 28',
        'type': 'Open Cluster',
        'vmag': 5.7,
        'distance_ly': 1300,
        'ra': '01h57m41s',
        'dec': '+37 deg47 arcmin06 arcsec',
        'notes': 'One of the oldest known open clusters, estimated age of 1.6 billion years.',
    },
    'NGC 2451': {
        'name': 'NGC 2451A',
        'type': 'Open Cluster',
        'vmag': 2.8,
        'distance_ly': 850,
        'ra': '07h45m15s',
        'dec': '-37 deg58 arcmin03 arcsec',
        'notes': 'One of the brightest open clusters in the sky, visible to naked eye.',
    },
    'NGC 2477': {
        'name': 'Caldwell 71',
        'type': 'Open Cluster',
        'vmag': 5.8,
        'distance_ly': 4300,
        'ra': '07h52m10s',
        'dec': '-38 deg31 arcmin48 arcsec',
        'notes': 'Rich open cluster containing thousands of stars, sometimes called the Southern Beehive.',
    },
}

bright_nebulae = {
    'NGC 2264': {
        'name': 'Cone Nebula',
        'type': 'Emission/Reflection Nebula',
        'vmag': 3.9,
        'distance_ly': 2700,
        'ra': '06h41m06s',
        'dec': '+09 deg53 arcmin00 arcsec',
        'notes': 'Part of the Christmas Tree Cluster, includes distinctive cone-shaped dark nebula.',
    },
    'IC 2944': {
        'name': 'Lambda Centauri Nebula',
        'type': 'Emission Nebula',
        'vmag': 4.5,
        'distance_ly': 6500,
        'ra': '11h36m16s',
        'dec': '-63 deg02 arcmin00 arcsec',
        'notes': 'Contains distinctive dark globules known as Thackeray\'s Globules.',
    },
    'IC 405': {
        'name': 'Flaming Star Nebula',
        'type': 'Emission/Reflection Nebula',
        'vmag': 6.0,
        'distance_ly': 1500,
        'ra': '05h16m12s',
        'dec': '+34 deg16 arcmin00 arcsec',
        'notes': 'Illuminated by the hot star AE Aurigae, appears reddish in photographs.',
    },
    'X Sgr A*': {
        'name': 'Sagittarius A*',
        'type': 'Supermassive Black Hole',
        'vmag': 0,                           # Apparent visual magnitude is not applicable to black holes
        'distance_ly': 26000,                 # Distance to the Galactic Center
        'ra': '17h 45m 40.04s',
        'dec': '-29 deg 00 arcmin 28.1 arcsec',
        'notes': 'Supermassive black hole at the center of the Milky Way galaxy.',
    },
    'X Stephenson 2-18': {
        'name': 'Stephenson 2-18',
        'type': 'Red Supergiant',
        'vmag': 0,                          # Apparent visual magnitude is difficult to determine precisely and varies
        'distance_ly': 18900,               # Distance estimates vary
        'ra': '18h 39m 11s',
        'dec': '-05 deg 57 arcmin 31 arcsec',
        'notes': 'One of the largest known stars, a red supergiant in the constellation Scutum.',
    },

}

# Function to combine all catalogs
def get_all_bright_objects():
    """Combine all catalogs of bright galactic objects."""
    all_objects = {}
    catalogs = [
        bright_planetaries,
        bright_open_clusters,
        bright_nebulae
    ]
    
    for catalog in catalogs:
        all_objects.update(catalog)
    
    return all_objects

def get_objects_brighter_than(magnitude):
    """Return all objects brighter than the specified magnitude."""
    visible = {}
    # Check all catalogs
    catalogs = [
        messier_catalog,
        star_cluster_catalog,
        bright_planetaries,
        bright_open_clusters,
        bright_nebulae
    ]
    
    for catalog in catalogs:
        visible.update({k: v for k, v in catalog.items() if v['vmag'] <= magnitude})
    
    return visible

def get_objects_by_type(obj_type):
    """Return all objects of a specific type."""
    matching = {}
    catalogs = [
        messier_catalog,
        star_cluster_catalog,
        bright_planetaries,
        bright_open_clusters,
        bright_nebulae
    ]
    
    for catalog in catalogs:
        matching.update({k: v for k, v in catalog.items() 
                        if obj_type.lower() in v['type'].lower()})
    
    return matching

def get_nebulae():
    """Return all nebulae from both Messier and bright object catalogs."""
    nebulae = {}
    # Check Messier catalog
    nebulae.update({k: v for k, v in messier_catalog.items() 
                    if 'Nebula' in v['type'] or 'HII Region' in v['type']})
    # Add bright nebulae
    nebulae.update(bright_nebulae)
    # Add bright planetaries
    nebulae.update(bright_planetaries)
    return nebulae

def get_star_clusters():
    """Return all star clusters from both catalogs."""
    clusters = {}
    clusters.update(star_cluster_catalog)
    clusters.update(bright_open_clusters)
    return clusters

def get_visible_objects(mag_limit):
    """Return all objects brighter than the given magnitude."""
    visible = {}
    # Check all catalogs
    catalogs = [
        ('M', messier_catalog),
        ('SC', star_cluster_catalog),
        ('PN', bright_planetaries),
        ('OC', bright_open_clusters),
        ('NEB', bright_nebulae)
    ]
    
    for prefix, catalog in catalogs:
        for obj_id, obj in catalog.items():
            if obj['vmag'] <= mag_limit:
                visible[obj_id] = obj
    return visible

def get_object_info(obj_id):
    """Get detailed information about a specific object."""
    catalogs = [
        messier_catalog,
        star_cluster_catalog,
        bright_planetaries,
        bright_open_clusters,
        bright_nebulae
    ]
    
    for catalog in catalogs:
        if obj_id in catalog:
            return catalog[obj_id]
    return None

def get_catalog_statistics():
    """Return statistics about all catalogs."""
    stats = {
        'total_objects': 0,
        'by_type': {},
        'magnitude_ranges': {
            '<=4.0': 0,
            '4.1-6.0': 0,
            '6.1-9.0': 0,
            '>9.0': 0
        },
        'by_catalog': {
            'Messier': 0,
            'Star Clusters': 0,
            'Planetaries': 0,
            'Open Clusters': 0,
            'Nebulae': 0
        }
    }
    
    # Process all catalogs
    catalog_map = {
        messier_catalog: 'Messier',
        star_cluster_catalog: 'Star Clusters',
        bright_planetaries: 'Planetaries',
        bright_open_clusters: 'Open Clusters',
        bright_nebulae: 'Nebulae'
    }
    
    for catalog, catalog_name in catalog_map.items():
        for obj in catalog.values():
            stats['total_objects'] += 1
            stats['by_catalog'][catalog_name] += 1
            
            # Count by type
            obj_type = obj['type']
            stats['by_type'][obj_type] = stats['by_type'].get(obj_type, 0) + 1
            
            # Count by magnitude
            vmag = obj['vmag']
            if vmag <= 4.0:
                stats['magnitude_ranges']['<=4.0'] += 1
            elif vmag <= 6.0:
                stats['magnitude_ranges']['4.1-6.0'] += 1
            elif vmag <= 9.0:
                stats['magnitude_ranges']['6.1-9.0'] += 1
            else:
                stats['magnitude_ranges']['>9.0'] += 1
            
    return stats