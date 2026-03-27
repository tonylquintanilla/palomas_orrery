"""
Paloma's Orrery: Heatwave Scenario Definitions
Provides fetch function + SCENARIOS list for the earth_system_generator engine.
Data Source: ERA5 via Open-Meteo Archive API
"""
import os
import json
import math
import time
import requests


def fetch_era5_heatwave(scenario, data_dir, status_callback=None):
    """Fetches historic wet-bulb data from ERA5 via Open-Meteo Archive API.
    
    Populates scenario['lats'], scenario['lons'], scenario['values'] in place.
    Uses a persistent JSON cache in data_dir to avoid redundant API calls.
    
    Args:
        scenario: dict with 'lat_range', 'lon_range', 'date' keys
        data_dir: path to data/ directory for cache file
        status_callback: optional callable(str) for progress updates
    """
    cache_file = os.path.join(data_dir, 'weather_cache.json')
    cache = {}
    if os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            try:
                cache = json.load(f)
            except:
                pass

    lat_range = scenario['lat_range']
    lon_range = scenario['lon_range']
    date = scenario['date']

    lats, lons, values = [], [], []
    total_points = len(lat_range) * len(lon_range)
    processed = 0

    for lat in lat_range:
        for lon in lon_range:
            processed += 1
            if processed % 10 == 0 and status_callback:
                status_callback(f"Fetching ERA5 Grid: {processed}/{total_points}")

            cache_key = f"{lat}_{lon}_{date}"
            if cache_key in cache:
                lats.append(lat)
                lons.append(lon)
                values.append(cache[cache_key])
                continue

            url = (f"https://archive-api.open-meteo.com/v1/archive?"
                   f"latitude={lat}&longitude={lon}"
                   f"&start_date={date}&end_date={date}"
                   f"&hourly=temperature_2m,relative_humidity_2m")
            try:
                response = requests.get(url)
                data = response.json()
                if 'hourly' in data:
                    temps = data['hourly']['temperature_2m']
                    humids = data['hourly']['relative_humidity_2m']

                    max_wb = -999
                    for t, h in zip(temps, humids):
                        if t is not None and h is not None:
                            wb = (t * math.atan(0.151977 * math.sqrt(h + 8.313659)) +
                                  math.atan(t + h) - math.atan(h - 1.676331) +
                                  0.00391838 * math.pow(h, 1.5) * math.atan(0.023101 * h) -
                                  4.686035)
                            if wb > max_wb:
                                max_wb = wb

                    lats.append(lat)
                    lons.append(lon)
                    values.append(max_wb)
                    cache[cache_key] = max_wb
                    time.sleep(0.1)
            except Exception as e:
                print(f"Error fetching {lat},{lon}: {e}")

    with open(cache_file, 'w') as f:
        json.dump(cache, f)

    scenario['lats'] = lats
    scenario['lons'] = lons
    scenario['values'] = values


# ==========================================
#     HEATWAVE THRESHOLD CONFIGURATION
# ==========================================
HEATWAVE_THRESHOLDS = {
    'unit_label': 'Wet Bulb Temperature',
    'min_display': 20,
    'spike_floor': None,  # Uses focus_val_min from each scenario
    'bands': [
        (26.0, 'ff00a5ff', 'Moderate Risk (ISO)'),
        (31.0, 'ff0000ff', 'High Risk (Carter/Foster)'),
        (35.0, 'ff00008b', 'Biological Breach (Vecellio)'),
        (float('inf'), 'ff000000', 'Theoretical Limit (Raymond)'),
    ],
    'height_base_subtract': True,  # height = (val - focus_val_min) * multiplier
    'height_multiplier': 50000,
    'colorscale': 'YlOrRd',
    'cmin': 20,
    'cmax': 38,
    'colorbar_title': 'Wet Bulb C',
    'contour_levels_start': 20,
    'contour_levels_stop': 38,
    'contour_levels_step': 1,
    'contour_cmap': 'inferno_r',
    'pop_radius_divisor': 250000,
    'legend_style': 'continuous',
}


# ==========================================
#          SCENARIO DEFINITIONS
# ==========================================
SCENARIOS = [
    {
        'scenario_id': 'nyc_1948', 'name': 'New York City (Aug 1948)',
        'boundary_type': 'heatwave',
        'date': '1948-08-26',
        'lat_range': range(45, 37, -1), 'lon_range': range(-80, -70, 1),
        'focus_val_min': 24,
        'description': 'Historical Baseline (Pre-AC Era). 100F+ Temps.',
        'briefing': "THE PRE-COOLING ERA. A massive heatwave hit the Northeast US. In an era before widespread AC, New Yorkers slept on fire escapes. This serves as our 'Historical Baseline'--survivable by the young, lethal to the vulnerable.\n\nStation Records: NYC 29.5C, Philadelphia 28.7C.\nRegional Map Peak: ~26.0C.\n\nSOURCE: NOAA; NY Times Archives",
        'populations': [
            {"name": "New York City (Station: 29.5C)", "lat": 40.7128, "lon": -74.0060, "pop": 7800000},
            {"name": "Philadelphia (Station: 28.7C)", "lat": 39.9526, "lon": -75.1652, "pop": 2000000},
            {"name": "Boston", "lat": 42.3601, "lon": -71.0589, "pop": 800000},
            {"name": "Baltimore", "lat": 39.2904, "lon": -76.6122, "pop": 950000},
            {"name": "Washington DC", "lat": 38.9072, "lon": -77.0369, "pop": 800000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'st_louis_1954', 'name': 'Midwest Torch (July 1954)',
        'boundary_type': 'heatwave',
        'date': '1954-07-14',
        'lat_range': range(42, 34, -1), 'lon_range': range(-94, -86, 1),
        'focus_val_min': 26.0,
        'description': 'All-time state record (117F). Deaths outnumbered births.',
        'briefing': "THE MIDWEST TORCH. East St. Louis hit 47.2C (117F), a record that still stands today. The combination of extreme air temperature and river valley humidity created conditions that overwhelmed the era's limited infrastructure.\n\nStation Record: East St. Louis 117F (Air Temp).\nRegional Map Peak: ~30.0C (Wet Bulb Estimate).\n\nSOURCE: Illinois State Water Survey",
        'populations': [
            {"name": "East St. Louis (Record: 117F)", "lat": 38.6245, "lon": -90.1506, "pop": 800000},
            {"name": "St. Louis", "lat": 38.6270, "lon": -90.1994, "pop": 850000},
            {"name": "Springfield", "lat": 39.7817, "lon": -89.6501, "pop": 100000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'la_1955', 'name': "LA Inferno (Sept 1955)",
        'boundary_type': 'heatwave',
        'date': '1955-09-01',
        'lat_range': range(35, 32, -1), 'lon_range': range(-120, -116, 1),
        'focus_val_min': 22.0,
        'description': "The 'Forgotten Disaster'. 946 deaths. 110F.",
        'briefing': "THE COASTAL SURPRISE. A massive high-pressure ridge parked over the West Coast. Downtown LA hit 110F (43C), and temps stayed above 100F for a week. With almost no air conditioning in 1955, the mortality (946 deaths) exceeded most earthquakes, exposing the deadly 'adaptation gap' of coastal cities.\n\nStation Record: Los Angeles 110F (Air Temp).\nRegional Map Peak: ~26.5C (Wet Bulb).\n\nSOURCE: LA Almanac; WeatherBug",
        'populations': [
            {"name": "Los Angeles (Record: 110F)", "lat": 34.0522, "lon": -118.2437, "pop": 2200000},
            {"name": "Long Beach", "lat": 33.7701, "lon": -118.1937, "pop": 250000},
            {"name": "Santa Monica", "lat": 34.0195, "lon": -118.4912, "pop": 75000},
            {"name": "Anaheim", "lat": 33.8366, "lon": -117.9143, "pop": 30000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'st_louis_nyc_1966', 'name': 'The Heat Index Event (July 1966)',
        'boundary_type': 'heatwave',
        'date': '1966-07-12',
        'lat_range': range(42, 37, -1), 'lon_range': range(-91, -73, 2),
        'focus_val_min': 25.0,
        'description': 'The event that created the Heat Index metric.',
        'briefing': "THE ORIGIN STORY. A massive heat dome bridged the Midwest and East Coast simultaneously. The sheer misery of high humidity in St. Louis combined with urban heat in NYC caused mass mortality, forcing the NWS to invent the 'Heat Index' to explain why 95F felt like 105F.\n\nStation Records: St. Louis 106F, NYC 103F.\nRegional Map Peak: ~29.0C.\n\nSOURCE: National Weather Service",
        'populations': [
            {"name": "St. Louis", "lat": 38.6270, "lon": -90.1994, "pop": 700000},
            {"name": "New York City", "lat": 40.7128, "lon": -74.0060, "pop": 7800000},
            {"name": "Philadelphia", "lat": 39.9526, "lon": -75.1652, "pop": 2000000},
            {"name": "Cincinnati", "lat": 39.1031, "lon": -84.5120, "pop": 500000},
            {"name": "Indianapolis", "lat": 39.7684, "lon": -86.1581, "pop": 500000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'uk_1976', 'name': 'UK Heat Wave (June 1976)',
        'boundary_type': 'heatwave',
        'date': '1976-06-26',
        'lat_range': range(55, 48, -1), 'lon_range': range(-5, 5, 1),
        'focus_val_min': 18.0,
        'description': 'The Great Drought. Water rationing and 20% excess deaths.',
        'briefing': "THE DROUGHT TRAP. One of the driest summers in UK history. While absolute temperatures (35.9C) seem modest, the compound stress of drought led to 20% excess mortality.\n\nStation Record: London 21.5C.\nRegional Map Peak: ~20.0C.\n\nSOURCE: Met Office; ONS",
        'populations': [
            {"name": "London (Station: 21.5C)", "lat": 51.5074, "lon": -0.1278, "pop": 6800000},
            {"name": "Birmingham", "lat": 52.4862, "lon": -1.8904, "pop": 1000000},
            {"name": "Southampton", "lat": 50.9097, "lon": -1.4044, "pop": 200000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'us_1980', 'name': 'US Heat Wave (July 1980)',
        'boundary_type': 'heatwave',
        'date': '1980-07-15',
        'lat_range': range(40, 30, -2), 'lon_range': range(-98, -85, 2),
        'focus_val_min': 24.0,
        'description': "1,700+ deaths. The 'Billion Dollar' heat disaster.",
        'briefing': "THE RUNAWAY HIGH. A massive high-pressure ridge stalled over the central US. Memphis hit 108F (42C). It caused >1,700 deaths and $20 billion in agricultural losses.\n\nStation Records: Memphis 28.8C, Kansas City 28.5C.\nRegional Map Peak: ~28.0C.\n\nSOURCE: NOAA; Karl & Quayle (1981)",
        'populations': [
            {"name": "Memphis (Station: 28.8C)", "lat": 35.1495, "lon": -90.0490, "pop": 650000},
            {"name": "St. Louis", "lat": 38.6270, "lon": -90.1994, "pop": 450000},
            {"name": "Kansas City", "lat": 39.0997, "lon": -94.5786, "pop": 450000},
            {"name": "Dallas", "lat": 32.7767, "lon": -96.7970, "pop": 900000},
            {"name": "Jackson (MS)", "lat": 32.2988, "lon": -90.1848, "pop": 200000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'athens_1987', 'name': 'Athens Heat Wave (July 1987)',
        'boundary_type': 'heatwave',
        'date': '1987-07-27',
        'lat_range': range(41, 36, -1), 'lon_range': range(20, 26, 1),
        'focus_val_min': 23.0,
        'description': '1,300+ deaths. The Urban Heat Island wake-up call.',
        'briefing': "THE CONCRETE TRAP. A week-long heatwave turned Athens into a kiln. The concrete city retained heat overnight, denying physiological recovery. ~1,300 deaths forced a complete overhaul of Greek infrastructure.\n\nStation Record: Athens 25.7C.\nRegional Map Peak: ~24.0C.\n\nSOURCE: Metaxas et al. (1991)",
        'populations': [
            {"name": "Athens (Station: 25.7C)", "lat": 37.9838, "lon": 23.7275, "pop": 3000000},
            {"name": "Patras", "lat": 38.2466, "lon": 21.7346, "pop": 150000},
            {"name": "Thessaloniki", "lat": 40.6401, "lon": 22.9444, "pop": 800000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'chicago_1995', 'name': 'Chicago Heat Wave (July 1995)',
        'boundary_type': 'heatwave',
        'date': '1995-07-13',
        'lat_range': range(50, 30, -2), 'lon_range': range(-100, -80, 2),
        'focus_val_min': 24.0,
        'description': "The 'silent killer' event. High mortality at lower thresholds.",
        'briefing': "A TRAGEDY OF VULNERABILITY. Wet bulbs hovered in the 'Red Zone'. Lack of AC and the 'Urban Heat Island' effect proved fatal for the elderly. CDC records confirm 739 excess deaths in 5 days.\n\nStation Record: Chicago (Midway) 28.3C.\nRegional Map Peak: ~29.4C (Corn Belt Humidity Pool).\n\nSOURCE: CDC; Klinenberg (2002)",
        'populations': [
            {"name": "Chicago (Station: 28.3C)", "lat": 41.8781, "lon": -87.6298, "pop": 2700000},
            {"name": "Milwaukee", "lat": 43.0389, "lon": -87.9065, "pop": 570000},
            {"name": "Gary", "lat": 41.5934, "lon": -87.3464, "pop": 75000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'europe_2003', 'name': 'Europe (The Great Mortality - Aug 2003)',
        'boundary_type': 'heatwave',
        'date': '2003-08-10',
        'lat_range': range(53, 40, -2), 'lon_range': range(-5, 15, 2),
        'focus_val_min': 22.0,
        'description': 'The event that changed Europe. 70,000+ excess deaths.',
        'briefing': "VULNERABILITY VS EXPOSURE. With <2% AC adoption and aging demographics, this 'moderate' wet-bulb heat became the deadliest natural disaster in modern European history.\n\nStation Record: Rome 25.2C, Paris 24.1C.\nRegional Map Peak: ~25.7C.\n\nSOURCE: Robine et al. (2008); INSERM",
        'populations': [
            {"name": "Paris", "lat": 48.8566, "lon": 2.3522, "pop": 2100000},
            {"name": "London", "lat": 51.5074, "lon": -0.1278, "pop": 8900000},
            {"name": "Milan", "lat": 45.4642, "lon": 9.1900, "pop": 1350000},
            {"name": "Rome (Station: 25.2C)", "lat": 41.9028, "lon": 12.4964, "pop": 2800000},
            {"name": "Berlin", "lat": 52.5200, "lon": 13.4050, "pop": 3600000},
            {"name": "Amsterdam", "lat": 52.3676, "lon": 4.9041, "pop": 820000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'russia_2010', 'name': 'Russia Heat Wave (July 2010)',
        'boundary_type': 'heatwave',
        'date': '2010-07-29',
        'lat_range': range(64, 48, -2), 'lon_range': range(25, 55, 2),
        'focus_val_min': 20.0,
        'description': '55,000+ excess deaths. Smoke and stagnation.',
        'briefing': "THE CONTINENTAL TRAP. A 'blocking high' stalled over Russia. The sheer duration (weeks) + toxic smoke from peat fires caused 55,000 excess deaths, proving that 'safe' wet bulbs are lethal if sustained.\n\nStation Record: St. Petersburg 23.4C, Moscow 22.8C.\nRegional Map Peak: ~25.2C.\n\nSOURCE: Barriopedro et al. (2011)",
        'populations': [
            {"name": "Moscow", "lat": 55.7558, "lon": 37.6173, "pop": 11500000},
            {"name": "St. Petersburg (Station: 23.4C)", "lat": 59.9311, "lon": 30.3609, "pop": 5400000},
            {"name": "Nizhny Novgorod", "lat": 56.3269, "lon": 44.0059, "pop": 1250000},
            {"name": "Voronezh", "lat": 51.6755, "lon": 39.2089, "pop": 1000000},
            {"name": "Helsinki", "lat": 60.1699, "lon": 24.9384, "pop": 650000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'india_pak_2015', 'name': 'India/Pakistan (May 2015)',
        'boundary_type': 'heatwave',
        'date': '2015-05-24',
        'lat_range': range(36, 5, -2), 'lon_range': range(55, 96, 2),
        'focus_val_min': 24.0,
        'description': '3,500+ deaths. The prequel to the modern crisis.',
        'briefing': "THE MASS CASUALTY SIGNAL. Before the 2024 Heat Belt, this event killed ~3,500 people. Roads melted in Delhi. It established the lethal trend for South Asia: pre-monsoon heat + high humidity.\n\nStation Records: Bhubaneswar 29.2C, Dhaka 28.0C.\nRegional Map Peak: ~30.0C (Coastal Andhra Pradesh).\n\nSOURCE: IMD; CNN Reports",
        'populations': [
            {"name": "Karachi", "lat": 24.8607, "lon": 67.0011, "pop": 16000000},
            {"name": "Hyderabad (Pak)", "lat": 25.3960, "lon": 68.3578, "pop": 1700000},
            {"name": "New Delhi", "lat": 28.6139, "lon": 77.2090, "pop": 26000000},
            {"name": "Nagpur", "lat": 21.1458, "lon": 79.0882, "pop": 2400000},
            {"name": "Hyderabad (India)", "lat": 17.3850, "lon": 78.4867, "pop": 10000000},
            {"name": "Vijayawada", "lat": 16.5062, "lon": 80.6480, "pop": 1500000},
            {"name": "Ahmedabad", "lat": 23.0225, "lon": 72.5714, "pop": 8000000},
            {"name": "Bhubaneswar (Station: 29.2C)", "lat": 20.2961, "lon": 85.8245, "pop": 1100000},
            {"name": "Dhaka (Station: 28.0C)", "lat": 23.8103, "lon": 90.4125, "pop": 22000000},
            {"name": "Muscat", "lat": 23.5859, "lon": 58.4059, "pop": 1500000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'iran_2015', 'name': 'Iran Bandar Mahshahr (July 2015)',
        'boundary_type': 'heatwave',
        'date': '2015-07-31',
        'lat_range': range(34, 22, -1), 'lon_range': range(44, 58, 1),
        'focus_val_min': 24.0,
        'description': 'The Warning Shot. Heat Index 74C.',
        'briefing': "THE NEAR BREACH. Before 2024, this was the record holder. Bandar Mahshahr hit a Heat Index of 74C (165F). The map illustrates the 'Coastal Resolution Gap':\n\nStation Record: Bandar Mahshahr 34.6C (Near-Theoretical Limit).\nRegional Map Peak: ~31.5C (Grid Average).\n\nSOURCE: Pal & Eltahir (2016)",
        'populations': [
            {"name": "Bandar Mahshahr (Station: 34.6C)", "lat": 30.5583, "lon": 49.1983, "pop": 160000},
            {"name": "Ahvaz", "lat": 31.3183, "lon": 48.6706, "pop": 1100000},
            {"name": "Basra", "lat": 30.5081, "lon": 47.7835, "pop": 1300000},
            {"name": "Kuwait City", "lat": 29.3759, "lon": 47.9774, "pop": 3000000},
            {"name": "Doha", "lat": 25.2854, "lon": 51.5310, "pop": 650000},
            {"name": "Manama", "lat": 26.2285, "lon": 50.5860, "pop": 200000},
            {"name": "Dammam", "lat": 26.4207, "lon": 50.0888, "pop": 1200000},
            {"name": "Nasiriyah", "lat": 31.0580, "lon": 46.2573, "pop": 550000},
            {"name": "Liwa Oasis", "lat": 23.1323, "lon": 53.7966, "pop": 20000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'se_asia_2016', 'name': 'SE Asia Super El Nino (April 2016)',
        'boundary_type': 'heatwave',
        'date': '2016-04-12',
        'lat_range': range(25, 10, -2), 'lon_range': range(95, 110, 2),
        'focus_val_min': 24.0,
        'description': 'Super El Nino event. Records broken across Thailand/Laos.',
        'briefing': "THE EL NINO SPIKE. A powerful El Nino superimposed on global warming triggered the longest heatwave in 65 years. Thailand consumed record power; schools closed.\n\nStation Record: Bangkok 30.2C.\nRegional Map Peak: ~29.0C.\n\nSOURCE: WMO; Thai Met Dept",
        'populations': [
            {"name": "Bangkok", "lat": 13.7563, "lon": 100.5018, "pop": 10000000},
            {"name": "Chiang Mai", "lat": 18.7061, "lon": 98.9817, "pop": 1200000},
            {"name": "Vientiane", "lat": 17.9757, "lon": 102.6331, "pop": 950000},
            {"name": "Phnom Penh", "lat": 11.5564, "lon": 104.9282, "pop": 2100000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'japan_2018', 'name': 'Japan Heat Wave (July 2018)',
        'boundary_type': 'heatwave',
        'date': '2018-07-23',
        'lat_range': range(40, 32, -2), 'lon_range': range(130, 145, 2),
        'focus_val_min': 24.0,
        'description': "Declared a 'Natural Disaster'. 1,000+ deaths.",
        'briefing': "THE DEMOGRAPHIC TRAP. Kumagaya hit 41.1C air temp. Despite high-tech infrastructure, over 1,000 people died, highlighting the vulnerability of aging populations to wet-bulb stress.\n\nStation Record: Kumagaya 28.0C.\nRegional Map Peak: ~27.5C.\n\nSOURCE: JMA; Ibithaj et al. (2020)",
        'populations': [
            {"name": "Tokyo", "lat": 35.6762, "lon": 139.6503, "pop": 14000000},
            {"name": "Kumagaya (Station: 28.0C)", "lat": 36.1473, "lon": 139.3886, "pop": 200000},
            {"name": "Nagoya", "lat": 35.1815, "lon": 136.9066, "pop": 2300000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'europe_2019', 'name': 'Europe Heat Wave (July 2019)',
        'boundary_type': 'heatwave',
        'date': '2019-07-25',
        'lat_range': range(53, 42, -2), 'lon_range': range(0, 15, 2),
        'focus_val_min': 24.0,
        'description': 'Records shattered. France hits 46C.',
        'briefing': "THE ACCELERATION. Paris broke its all-time record. Unlike 2003, mortality was lower due to adaptation, but the *intensity* proved the climate had fundamentally shifted.\n\nStation Record: Paris 23.9C (Dry Heat Event).\nRegional Map Peak: ~24.5C.\n\nSOURCE: Meteo France; WWA",
        'populations': [
            {"name": "Paris", "lat": 48.8566, "lon": 2.3522, "pop": 2100000},
            {"name": "Brussels", "lat": 50.8503, "lon": 4.3517, "pop": 1200000},
            {"name": "Frankfurt", "lat": 50.1109, "lon": 8.6821, "pop": 750000},
            {"name": "Amsterdam", "lat": 52.3676, "lon": 4.9041, "pop": 820000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'siberia_2020', 'name': 'Siberia Arctic Breach (June 2020)',
        'boundary_type': 'heatwave',
        'date': '2020-06-20',
        'lat_range': range(72, 60, -2), 'lon_range': range(125, 145, 2),
        'focus_val_min': 18.0,
        'description': '38C (100F) in the Arctic Circle.',
        'briefing': "PLANETARY STATE SHIFT. Verkhoyansk hit 38C, the highest temperature ever recorded north of the Arctic Circle. While wet-bulb stress was low (dry heat), the *anomaly* was +18C above normal, triggering massive peat fires and permafrost melt.\n\nStation Record: Verkhoyansk 38.0C (Air).\nRegional Map Peak: ~23.0C (Wet Bulb).\n\nSOURCE: WMO; Copernicus",
        'populations': [
            {"name": "Verkhoyansk", "lat": 67.5447, "lon": 133.3850, "pop": 1300},
            {"name": "Yakutsk", "lat": 62.0397, "lon": 129.7422, "pop": 300000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'pnw_heat_dome', 'name': 'Pacific NW Heat Dome (June 2021)',
        'boundary_type': 'heatwave',
        'date': '2021-06-28',
        'lat_range': range(60, 40, -2), 'lon_range': range(-135, -110, 2),
        'focus_val_min': 24.0,
        'description': 'Extreme anomaly in high latitudes.',
        'briefing': "THE 1-IN-1000 YEAR EVENT. Lytton, BC broke records (49.6C). The rapid onset shocked the unacclimatized population. Combined death toll estimated at over 1,200.\n\nStation Record: Portland 27.3C.\nRegional Map Peak: ~26.0C.\n\nSOURCE: BC Coroners Service; CDC",
        'populations': [
            {"name": "Seattle", "lat": 47.6062, "lon": -122.3321, "pop": 737000},
            {"name": "Portland (Station: 27.3C)", "lat": 45.5152, "lon": -122.6784, "pop": 650000},
            {"name": "Vancouver", "lat": 49.2827, "lon": -123.1207, "pop": 675000},
            {"name": "Lytton", "lat": 50.2333, "lon": -121.5833, "pop": 250},
            {"name": "Salem", "lat": 44.9429, "lon": -123.0351, "pop": 175000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'china_2022', 'name': 'China Yangtze Basin (Aug 2022)',
        'boundary_type': 'heatwave',
        'date': '2022-08-20',
        'lat_range': range(34, 26, -2), 'lon_range': range(102, 123, 2),
        'focus_val_min': 24.0,
        'description': 'The 70-day mega-heatwave. Industrial shutdown.',
        'briefing': "SYSTEMIC FAILURE. The Yangtze river dried up, cutting hydropower to the very region needing AC. The event caused a massive industrial shutdown and reports of significant excess mortality.\n\nStation Record: Wuhan 29.5C.\nRegional Map Peak: ~30.0C.\n\nSOURCE: World Weather Attribution (WWA)",
        'populations': [
            {"name": "Wuhan (Station: 29.5C)", "lat": 30.5928, "lon": 114.3055, "pop": 11000000},
            {"name": "Chongqing", "lat": 29.5630, "lon": 106.5516, "pop": 15800000},
            {"name": "Nanjing", "lat": 32.0603, "lon": 118.7969, "pop": 8500000},
            {"name": "Shanghai", "lat": 31.2304, "lon": 121.4737, "pop": 26300000},
            {"name": "Chengdu", "lat": 30.5728, "lon": 104.0668, "pop": 16000000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'amazon_2023', 'name': "Amazon 'Boiling River' (Sept 2023)",
        'boundary_type': 'heatwave',
        'date': '2023-09-25',
        'lat_range': range(2, -10, -2), 'lon_range': range(-70, -55, 2),
        'focus_val_min': 24.0,
        'description': 'Ecological collapse. River temperatures hit 39C.',
        'briefing': "THE BIOSPHERE LIMIT. A severe drought heated the Rio Negro to 39C. Mortality was ecological: 150+ river dolphins boiled alive. Indigenous communities faced critical water shortages.\n\nStation Record: Tefe 28.5C.\nRegional Map Peak: ~27.9C.\n\nSOURCE: Mamiraua Institute",
        'populations': [
            {"name": "Manaus", "lat": -3.1190, "lon": -60.0217, "pop": 2200000},
            {"name": "Tefe", "lat": -3.3542, "lon": -64.7115, "pop": 60000},
            {"name": "Coari", "lat": -4.0849, "lon": -63.1417, "pop": 85000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'rio_2023', 'name': "Rio 'Heat Index 59' (Nov 2023)",
        'boundary_type': 'heatwave',
        'date': '2023-11-18',
        'lat_range': range(-20, -25, -1), 'lon_range': range(-45, -40, 1),
        'focus_val_min': 24.0,
        'description': "The 'Taylor Swift' heatwave. Heat Index 59.7C.",
        'briefing': "THE CULTURAL LIMIT. A massive humidity dome over Rio drove the Heat Index to 59.7C. The death of a fan at a major concert forced the industry to recognize heat as a mass-casualty threat.\n\nStation Record: Marambaia 29.5C.\nRegional Map Peak: ~28.5C.\n\nSOURCE: INMET; Local Authorities",
        'populations': [
            {"name": "Rio de Janeiro (Station: 29.5C)", "lat": -22.9068, "lon": -43.1729, "pop": 6700000},
            {"name": "Sao Paulo", "lat": -23.5505, "lon": -46.6333, "pop": 12300000},
            {"name": "Santos", "lat": -23.9618, "lon": -46.3322, "pop": 430000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'mali_2024', 'name': 'Mali/Sahel (April 2024)',
        'boundary_type': 'heatwave',
        'date': '2024-04-03',
        'lat_range': range(22, 4, -1), 'lon_range': range(-17, 10, 1),
        'focus_val_min': 24.0,
        'description': 'The forgotten heatwave. Temps hit 48.5C.',
        'briefing': "THE EQUATORIAL TRAP. Bamako, Mali saw temperatures of 48.5C. Gabriel Toure Hospital reported 102 deaths in just 4 days. Total regional excess mortality likely exceeded 3,000.\n\nStation Record: Kayes 28.9C.\nRegional Map Peak: ~28.6C.\n\nSOURCE: Gabriel Toure Hospital; WWA",
        'populations': [
            {"name": "Bamako", "lat": 12.6392, "lon": -8.0029, "pop": 2400000},
            {"name": "Kayes", "lat": 14.4469, "lon": -11.4445, "pop": 127000},
            {"name": "Segou", "lat": 13.4416, "lon": -6.2163, "pop": 130000},
            {"name": "Ouagadougou", "lat": 12.3714, "lon": -1.5197, "pop": 2500000},
            {"name": "Niamey", "lat": 13.5116, "lon": 2.1254, "pop": 1000000},
            {"name": "Kano", "lat": 12.0022, "lon": 8.5920, "pop": 4000000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'delhi_heat_wave', 'name': 'The Asian Heat Belt (Delhi/Gulf - May 2024)',
        'boundary_type': 'heatwave',
        'date': '2024-05-29',
        'lat_range': range(35, 5, -3), 'lon_range': range(40, 110, 3),
        'focus_val_min': 24.0,
        'description': 'A trans-national event affecting 1 Billion people.',
        'briefing': "THE INVISIBLE DISASTER. A 'Heat Belt' stretched 5,000km from Riyadh to Bangkok. This visualization reveals a continuous corridor of lethal wet-bulb potential overlaying the world's densest population centers.\n\nStation Record: Kolkata 31.6C (Biological Breach).\nRegional Map Peak: ~31.0C.\n\nSOURCE: IMD; WWA; Local Reports",
        'populations': [
            {"name": "Riyadh", "lat": 24.7136, "lon": 46.6753, "pop": 7600000},
            {"name": "Dubai", "lat": 25.2048, "lon": 55.2708, "pop": 3300000},
            {"name": "Kuwait City", "lat": 29.3759, "lon": 47.9774, "pop": 3100000},
            {"name": "Baghdad", "lat": 33.3152, "lon": 44.3661, "pop": 7100000},
            {"name": "Basra", "lat": 30.5081, "lon": 47.7835, "pop": 1300000},
            {"name": "Karachi", "lat": 24.8607, "lon": 67.0011, "pop": 16000000},
            {"name": "Lahore", "lat": 31.5204, "lon": 74.3587, "pop": 13000000},
            {"name": "Jacobabad", "lat": 28.2835, "lon": 68.4388, "pop": 200000},
            {"name": "New Delhi", "lat": 28.6139, "lon": 77.2090, "pop": 32000000},
            {"name": "Lucknow", "lat": 26.8467, "lon": 80.9462, "pop": 3800000},
            {"name": "Jaipur", "lat": 26.9124, "lon": 75.7873, "pop": 4000000},
            {"name": "Ahmedabad", "lat": 23.0225, "lon": 72.5714, "pop": 8200000},
            {"name": "Mumbai", "lat": 19.0760, "lon": 72.8777, "pop": 21000000},
            {"name": "Kolkata (Station: 31.6C)", "lat": 22.5726, "lon": 88.3639, "pop": 15000000},
            {"name": "Patna", "lat": 25.5941, "lon": 85.1376, "pop": 2500000},
            {"name": "Bhubaneswar", "lat": 20.2961, "lon": 85.8245, "pop": 1100000},
            {"name": "Dhaka", "lat": 23.8103, "lon": 90.4125, "pop": 22000000},
            {"name": "Chittagong", "lat": 22.3569, "lon": 91.7832, "pop": 5000000},
            {"name": "Yangon", "lat": 16.8409, "lon": 96.1735, "pop": 5500000},
            {"name": "Bangkok", "lat": 13.7563, "lon": 100.5018, "pop": 10700000},
            {"name": "Ho Chi Minh City", "lat": 10.8231, "lon": 106.6297, "pop": 9000000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'persian_gulf_2024', 'name': 'Persian Gulf (July 2024)',
        'boundary_type': 'heatwave',
        'date': '2024-07-17',
        'lat_range': range(35, 20, -2), 'lon_range': range(45, 60, 2),
        'focus_val_min': 24.0,
        'description': 'Breaching the theoretical limit.',
        'briefing': "THE BLACK SWAN. Stations recorded 35C Wet Bulb. Remarkably, mortality was minimal due to near-universal air conditioning. This illustrates the 'Adaptation Gap': money bought survival in a lethal environment.\n\nStation Record: Dubai 31.4C.\nRegional Map Peak: ~31.5C.\n\nSOURCE: NOAA; Raymond et al.",
        'populations': [
            {"name": "Dubai (Station: 31.4C)", "lat": 25.276987, "lon": 55.296249, "pop": 3300000},
            {"name": "Doha", "lat": 25.2854, "lon": 51.5310, "pop": 2300000},
            {"name": "Bandar Abbas", "lat": 27.1832, "lon": 56.2666, "pop": 526000},
            {"name": "Abu Dhabi", "lat": 24.4539, "lon": 54.3773, "pop": 1450000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'australia_heat_dome', 'name': 'Australia Heat Dome (Dec 2024)',
        'boundary_type': 'heatwave',
        'date': '2024-12-19',
        'lat_range': range(5, -60, -4), 'lon_range': range(-180, 180, 4),
        'focus_val_min': 24.0,
        'description': 'Peak heating in the Southern Hemisphere.',
        'briefing': "SOUTHERN HEMISPHERE MAX. While the Australian interior baked in extreme *dry* heat (45C+), the lethal *wet-bulb* peak shifted north into the tropical convergence zone. The humidity trap over Java created higher physiological stress than the Outback.\n\nStation Record: Jakarta 27.2C (Wet Bulb Peak).\nRegional Map Peak: ~25.5C (Northern Australia).\n\nSOURCE: BOM; Health Dept",
        'populations': [
            {"name": "Jakarta (Station: 27.2C)", "lat": -6.2088, "lon": 106.8456, "pop": 10500000},
            {"name": "Darwin", "lat": -12.4634, "lon": 130.8456, "pop": 150000},
            {"name": "Alice Springs", "lat": -23.6980, "lon": 133.8807, "pop": 26000},
            {"name": "Mount Isa", "lat": -20.7256, "lon": 139.4927, "pop": 18000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'pakistan_2025', 'name': 'Pakistan Heat Wave (June 2025)',
        'boundary_type': 'heatwave',
        'date': '2025-06-22',
        'lat_range': range(34, 23, -2), 'lon_range': range(66, 76, 2),
        'focus_val_min': 24.0,
        'description': "The 'Unlivable' Summer. Heat Index 55C+.",
        'briefing': "THE THERMODYNAMIC TRAP. Heat trough + Monsoon moisture. Local NGOs estimated 1,500+ excess deaths in Sindh province alone, as hospitals were overwhelmed by kidney failure cases.\n\nStation Record: Karachi 28.7C.\nRegional Map Peak: ~29.0C.\n\nSOURCE: NDMA; Edhi Foundation",
        'populations': [
            {"name": "Jacobabad", "lat": 28.2835, "lon": 68.4388, "pop": 200000},
            {"name": "Sibi", "lat": 29.5448, "lon": 67.8764, "pop": 115000},
            {"name": "Karachi (Station: 28.7C)", "lat": 24.8607, "lon": 67.0011, "pop": 14900000},
            {"name": "Sukkur", "lat": 27.7131, "lon": 68.8492, "pop": 500000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'us_grid_2025', 'name': 'US Grid-Stress Heat Dome (June 2025)',
        'boundary_type': 'heatwave',
        'date': '2025-06-25',
        'lat_range': range(45, 30, -2), 'lon_range': range(-95, -70, 2),
        'focus_val_min': 24.0,
        'description': 'Infrastructure failure event. 255 million affected.',
        'briefing': "THE GRID TRAP. A heat dome spanned from Chicago to Atlanta. Energy demand shattered records, forcing rolling blackouts. It proved that in a fully adapted society, the grid itself is the point of failure.\n\nStation Record: St. Louis 29.1C.\nRegional Map Peak: ~29.0C.\n\nSOURCE: NOAA; NERC",
        'populations': [
            {"name": "Chicago", "lat": 41.8781, "lon": -87.6298, "pop": 2700000},
            {"name": "Washington DC", "lat": 38.9072, "lon": -77.0369, "pop": 700000},
            {"name": "Atlanta", "lat": 33.7490, "lon": -84.3880, "pop": 500000},
            {"name": "New York City", "lat": 40.7128, "lon": -74.0060, "pop": 8000000},
            {"name": "St. Louis", "lat": 38.6270, "lon": -90.1994, "pop": 300000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
    {
        'scenario_id': 'amazon_drought_2025', 'name': 'Amazon Tipping Point Drought (Sept 2025)',
        'boundary_type': 'heatwave',
        'date': '2025-09-15',
        'lat_range': range(5, -15, -2), 'lon_range': range(-75, -50, 2),
        'focus_val_min': 24.0,
        'description': "Failure of the 'Flying Rivers'. Historic low water.",
        'briefing': "ECOLOGICAL COLLAPSE. Following the 2023 drought, 2025 pushed the basin past the tipping point. Major tributaries like the Madeira hit historic lows. The rainforest temporarily became a net carbon source.\n\nStation Record: Manaus 28.2C.\nRegional Map Peak: ~28.0C.\n\nSOURCE: INPE; MapBiomas",
        'populations': [
            {"name": "Manaus", "lat": -3.1190, "lon": -60.0217, "pop": 2200000},
            {"name": "Santarem", "lat": -2.4430, "lon": -54.7081, "pop": 300000},
            {"name": "Iquitos (Peru)", "lat": -3.7437, "lon": -73.2516, "pop": 480000},
            {"name": "Porto Velho", "lat": -8.7612, "lon": -63.9039, "pop": 540000}
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },
]
