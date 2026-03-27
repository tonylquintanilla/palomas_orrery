"""
Paloma's Orrery: Coral Bleaching Scenario Definitions
Provides fetch function + SCENARIOS list for the earth_system_generator engine.
Data Source: NOAA Coral Reef Watch (ERDDAP API) - Degree Heating Weeks (DHW)

DHW is the metric of reef mortality: accumulated thermal stress above the
bleaching threshold (1C above max monthly mean SST), measured in C-weeks.
  4 DHW = Warning (bleaching likely)
  8 DHW = Significant bleaching and some mortality
 12 DHW = Severe mass bleaching and widespread mortality

Fetch logic adapted from biosphere_coral_generator.py (Gemini POC).
"""
import os
import csv
import requests


def fetch_noaa_coral(scenario, data_dir, status_callback=None):
    """Fetches Degree Heating Week data from NOAA Coral Reef Watch ERDDAP.

    Populates scenario['lats'], scenario['lons'], scenario['values'] in place.

    Resolution order:
    1. Local CSV cache in data/ (from prior fetch or manual download)
    2. NOAA ERDDAP primary (coastwatch.noaa.gov)
    3. NOAA ERDDAP Pacific mirror (coastwatch.pfeg.noaa.gov)
    4. PacIOOS Hawaii mirror (pae-paha.pacioos.hawaii.edu)

    Local CSV files can use either -180/180 or 0/360 longitude and
    either 'degree_heating_week' or 'CRW_DHW' as the variable name.
    Longitudes are normalized to -180/180 on load.

    Args:
        scenario: dict with 'date', 'lat_bounds', 'lon_bounds' keys
        data_dir: path to data/ directory for CSV cache
        status_callback: optional callable(str) for progress updates
    """
    name = scenario['name']
    date = scenario['date']
    scenario_id = scenario['scenario_id']
    lat_min, lat_max = scenario['lat_bounds']
    lon_min, lon_max = scenario['lon_bounds']

    # 1. CHECK LOCAL CSV CACHE
    cache_file = os.path.join(data_dir, f"{scenario_id}_dhw.csv")
    if os.path.exists(cache_file):
        print(f"Loading cached DHW data from {cache_file}...")
        if status_callback:
            status_callback(f"Loading cached data for {name}...")
        csv_text = open(cache_file, 'r').read()
        _parse_dhw_csv(csv_text, scenario)
        if scenario['values']:
            print(f"Loaded {len(scenario['values'])} points from cache.")
            return

    # 2. TRY ERDDAP SERVERS
    servers = [
        ("coastwatch.noaa.gov", "noaacrwdhwDaily", "degree_heating_week", "NOAA Primary"),
        ("coastwatch.pfeg.noaa.gov", "NOAA_DHW", "degree_heating_week", "NOAA Pacific"),
        ("pae-paha.pacioos.hawaii.edu", "dhw_5km", "CRW_DHW", "PacIOOS Hawaii"),
    ]

    response = None
    for host, dataset_id, var_name, label in servers:
        if status_callback:
            status_callback(f"Fetching DHW from {label}...")
        print(f"Trying {label}: {host}/{dataset_id}...")

        # PacIOOS uses 0-360 longitude
        if 'pacioos' in host:
            qlon_min = lon_min % 360
            qlon_max = lon_max % 360
        else:
            qlon_min, qlon_max = lon_min, lon_max

        url = (f"https://{host}/erddap/griddap/{dataset_id}.csv?"
               f"{var_name}[({date}T12:00:00Z):1:({date}T12:00:00Z)]"
               f"[({lat_max}):1:({lat_min})][({qlon_min}):1:({qlon_max})]")

        try:
            response = requests.get(url, timeout=60)
            if response.status_code == 200:
                print(f"Success from {label}.")
                # Cache the raw CSV for future use
                with open(cache_file, 'w') as f:
                    f.write(response.text)
                print(f"Cached to {cache_file}")
                break
            else:
                print(f"{label} returned HTTP {response.status_code}, trying next...")
                response = None
        except requests.exceptions.RequestException as e:
            print(f"{label} failed: {e}")
            response = None

    if response is None or response.status_code != 200:
        msg = ("All ERDDAP servers unavailable.\n\n"
               "You can manually download the data:\n"
               "1. Visit https://pae-paha.pacioos.hawaii.edu/erddap/griddap/dhw_5km.html\n"
               "2. Select CRW_DHW, set date/lat/lon bounds\n"
               f"3. Save the CSV as: data/{scenario_id}_dhw.csv\n"
               "4. Run again -- the local file will be used automatically.")
        raise Exception(msg)

    _parse_dhw_csv(response.text, scenario)
    print(f"Retrieved {len(scenario['values'])} marine data points for {name}.")

    if status_callback:
        status_callback(f"Retrieved {len(scenario['values'])} points")


def _parse_dhw_csv(csv_text, scenario):
    """Parses ERDDAP CSV into scenario lats/lons/values.

    Handles both variable names (degree_heating_week, CRW_DHW) and
    both longitude conventions (-180/180 and 0/360).
    """
    reader = csv.reader(csv_text.splitlines())
    rows = list(reader)

    if len(rows) < 3:
        scenario['lats'] = []
        scenario['lons'] = []
        scenario['values'] = []
        return

    # Find DHW column index from header (row 0)
    header = rows[0]
    dhw_col = None
    for i, col in enumerate(header):
        if col.strip() in ('degree_heating_week', 'CRW_DHW'):
            dhw_col = i
            break
    if dhw_col is None:
        dhw_col = 3  # fallback to 4th column

    data_rows = rows[2:]  # skip header + units rows

    lats, lons, values = [], [], []
    for row in data_rows:
        if len(row) <= dhw_col or row[dhw_col] == 'NaN':
            continue
        lat = float(row[1])
        lon = float(row[2])
        dhw = float(row[dhw_col])

        # Normalize 0-360 longitude to -180/180
        if lon > 180:
            lon = lon - 360

        if dhw > 0:
            lats.append(lat)
            lons.append(lon)
            values.append(dhw)

    scenario['lats'] = lats
    scenario['lons'] = lons
    scenario['values'] = values


# ==========================================
#     CORAL BLEACHING THRESHOLD CONFIG
# ==========================================
CORAL_THRESHOLDS = {
    'unit_label': 'Degree Heating Weeks (DHW)',
    'min_display': 0,
    'spike_floor': 4,  # Only extrude dangerous heat (DHW >= 4)
    'bands': [
        (4,  'ff00a5ff', 'Warning'),
        (8,  'ff0000ff', 'Significant Bleaching'),
        (12, 'ff800080', 'Severe Mass Bleaching'),
        (float('inf'), 'ff000000', 'Systemic Mortality'),
    ],
    'height_base_subtract': False,  # height = dhw * multiplier (no offset)
    'height_multiplier': 1000,
    'colorscale': 'YlOrRd',
    'cmin': 0,
    'cmax': 16,
    'colorbar_title': 'DHW',
    'contour_levels_start': 0,
    'contour_levels_stop': 16,
    'contour_levels_step': 1,
    'contour_cmap': 'magma_r',
    'pop_radius_divisor': 50000,  # Coastal populations are smaller; bigger circles
    'spike_stride': 200,  # NOAA 5km grid is very dense; stride keeps full range, fewer pins
    'legend_style': 'continuous',
}


# ==========================================
#          SCENARIO DEFINITIONS
# ==========================================
SCENARIOS = [
    {
        'scenario_id': 'florida_coral_2023',
        'name': 'Florida & Cuba Mass Bleaching',
        'boundary_type': 'coral_bleaching',
        'date': '2023-08-25',
        'lat_bounds': (22.0, 27.0),
        'lon_bounds': (-84.0, -76.0),
        'focus_val_min': 4,
        'description': 'Peak thermal stress during the worst Caribbean bleaching event on record.',
        'briefing': "REEF EMERGENCY. August 2023: Sea surface temperatures off Florida shattered records. "
                    "Buoy readings at Manatee Bay hit 38.4C -- hot tub temperatures over living reef. "
                    "The Florida Reef Tract, third largest barrier reef system in the world, experienced "
                    "near-total bleaching. NOAA Coral Reef Watch recorded DHW values exceeding 16 in the "
                    "Florida Keys -- double the threshold for mass mortality.\n\n"
                    "The event extended across the entire Caribbean basin, devastating reefs from "
                    "Belize to the Bahamas.\n\n"
                    "SOURCE: NOAA Coral Reef Watch; FKNMS",
        'populations': [
            {'name': 'Miami Metro', 'lat': 25.7617, 'lon': -80.1918, 'pop': 6100000},
            {'name': 'Key West', 'lat': 24.5551, 'lon': -81.7800, 'pop': 26000},
            {'name': 'Havana', 'lat': 23.1136, 'lon': -82.3666, 'pop': 2100000},
            {'name': 'Nassau', 'lat': 25.0443, 'lon': -77.3504, 'pop': 275000},
        ],
        'thresholds': CORAL_THRESHOLDS,
        'fetch': fetch_noaa_coral,
        'lats': [], 'lons': [], 'values': [],
    },
]
