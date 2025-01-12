# messier_catalog.py

messier_catalog = {
    'M1': {
        'name': 'Crab Nebula',
        'type': 'Supernova Remnant',
        'vmag': 8.4,
        'distance_ly': 6500,
        'ra': '05h34m31.94s',
        'dec': '+22°00′52.2″',
        'notes': 'Remnant of supernova observed in 1054 AD. Contains a pulsar.',
    },
    'M8': {
        'name': 'Lagoon Nebula',
        'type': 'Emission Nebula',
        'vmag': 6.0,
        'distance_ly': 5200,
        'ra': '18h03m37s',
        'dec': '-24°23′12″',
        'notes': 'Contains many young stars. Active star formation region.',
    },
    'M16': {
        'name': 'Eagle Nebula',
        'type': 'Emission Nebula',
        'vmag': 6.0,
        'distance_ly': 7000,
        'ra': '18h18m48s',
        'dec': '-13°47′00″',
        'notes': 'Famous for the "Pillars of Creation" imaged by Hubble.',
    },
    'M17': {
        'name': 'Omega Nebula',
        'type': 'Emission Nebula',
        'vmag': 6.0,
        'distance_ly': 5500,
        'ra': '18h20m26s',
        'dec': '-16°10′36″',
        'notes': 'Also known as Swan Nebula. Active star formation region.',
    },
    'M20': {
        'name': 'Trifid Nebula',
        'type': 'Emission/Reflection Nebula',
        'vmag': 6.3,
        'distance_ly': 5200,
        'ra': '18h02m23s',
        'dec': '-23°01′48″',
        'notes': 'Combination of emission and reflection nebula divided by dark dust lanes.',
    },
    'M27': {
        'name': 'Dumbbell Nebula',
        'type': 'Planetary Nebula',
        'vmag': 7.5,
        'distance_ly': 1360,
        'ra': '19h59m36.3s',
        'dec': '+22°43′16″',
        'notes': 'First planetary nebula ever discovered.',
    },
    'M42': {
        'name': 'Orion Nebula',
        'type': 'Emission Nebula',
        'vmag': 4.0,
        'distance_ly': 1344,
        'ra': '05h35m17.3s',
        'dec': '-05°23′28″',
        'notes': 'Brightest diffuse nebula in the sky. Contains the Trapezium Cluster.',
    },
    'M43': {
        'name': 'De Mairan\'s Nebula',
        'type': 'HII Region',
        'vmag': 9.0,
        'distance_ly': 1600,
        'ra': '05h35m31.3s',
        'dec': '-05°16′03″',
        'notes': 'Part of the Orion Nebula complex.',
    },
    'M57': {
        'name': 'Ring Nebula',
        'type': 'Planetary Nebula',
        'vmag': 8.8,
        'distance_ly': 2300,
        'ra': '18h53m35.1s',
        'dec': '+33°01′45″',
        'notes': 'Classic example of a planetary nebula.',
    },
    'M76': {
        'name': 'Little Dumbbell Nebula',
        'type': 'Planetary Nebula',
        'vmag': 10.1,
        'distance_ly': 3400,
        'ra': '01h42m19.9s',
        'dec': '+51°34′31″',
        'notes': 'Also known as Cork Nebula or Butterfly Nebula.',
    },
    'M78': {
        'name': 'Messier 78',
        'type': 'Reflection Nebula',
        'vmag': 8.3,
        'distance_ly': 1600,
        'ra': '05h46m45.8s',
        'dec': '+00°04′48″',
        'notes': 'Brightest reflection nebula in the sky.',
    },
    'M97': {
        'name': 'Owl Nebula',
        'type': 'Planetary Nebula',
        'vmag': 9.9,
        'distance_ly': 2600,
        'ra': '11h14m47.7s',
        'dec': '+55°01′09″',
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
        'dec': '-32°15′12″',
        'notes': 'Contains about 80 stars. Resembles a butterfly.',
    },
    'M7': {
        'name': 'Ptolemy Cluster',
        'type': 'Open Cluster',
        'vmag': 3.3,
        'distance_ly': 980,
        'ra': '17h53m51.2s',
        'dec': '-34°47′34″',
        'notes': 'Visible to naked eye. Known to Ptolemy in 130 AD.',
    },
    'M11': {
        'name': 'Wild Duck Cluster',
        'type': 'Open Cluster',
        'vmag': 5.8,
        'distance_ly': 6200,
        'ra': '18h51m05s',
        'dec': '-06°16′12″',
        'notes': 'Rich, compact cluster. Contains about 3000 stars.',
    },
    'M44': {
        'name': 'Beehive Cluster',
        'type': 'Open Cluster',
        'vmag': 3.7,
        'distance_ly': 577,
        'ra': '08h40m6.0s',
        'dec': '+19°59′00″',
        'notes': 'Open cluste in Cancer.',
    },
    'M45': {
        'name': 'Pleiades',
        'type': 'Open Cluster',
        'vmag': 1.6,
        'distance_ly': 440,
        'ra': '03h47m0s',
        'dec': '+24°07′00″',
        'notes': 'Open cluste in Taurus.',
    },
}

def get_nebulae():
    """Return all nebulae from the catalog."""
    return {k: v for k, v in messier_catalog.items() 
            if 'Nebula' in v['type'] or 'HII Region' in v['type']}

def get_star_clusters():
    """Return all star clusters."""
    return star_cluster_catalog

def get_visible_objects(mag_limit):
    """Return all objects brighter than the given magnitude."""
    visible = {}
    # Check main catalog
    for m_id, obj in messier_catalog.items():
        if obj['vmag'] <= mag_limit:
            visible[m_id] = obj
    # Check star clusters
    for m_id, obj in star_cluster_catalog.items():
        if obj['vmag'] <= mag_limit:
            visible[m_id] = obj
    return visible

def get_object_info(messier_id):
    """Get detailed information about a specific object."""
    if messier_id in messier_catalog:
        return messier_catalog[messier_id]
    elif messier_id in star_cluster_catalog:
        return star_cluster_catalog[messier_id]
    return None