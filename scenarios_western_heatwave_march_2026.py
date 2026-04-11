"""
Paloma's Orrery: Western North America Heat Dome - March 2026
Scenario Module: Parameterized Timeline Snapshots

ARCHITECTURE:
-------------
Nine dated snapshots tell the complete story of a 1-in-500-year heat event:

  March 14 - "The Spark"        : NWS issues first Extreme Heat Watches (CSI 2)
  March 17 - "The Pivot"        : Heat dome locks in, anomaly jumps to dangerous (CSI 3)
  March 18 - "Records Fall"     : Phoenix earliest 100+F, Las Vegas shatters March record (CSI 4)
  March 20 - "The Peak"         : Martinez Lake 112F, Yuma 109F, national records (CSI 5)
  March 21 - "Eastward Surge"   : 14 states break all-time March records (CSI 5)
  March 22 - "The Crest"        : Pulse 1 crests at Mississippi Valley; 1500+ records (CSI 5)
  March 25 - "Round Two"        : Pulse 2 rebuilds; Denver breaks own record again (CSI 5)
  March 26 - "Pulse 2 Crests"   : OK 106F, TX 108F, KS 104F; 17 state records (CSI 5)
  March 30 - "The Reach"        : Chicago 81F; dome touches Great Lakes; event ends (CSI 4)

Each snapshot uses a shared parameterized fetch function. The date drives:
  - Anomaly magnitude (builds from 15F to 32F over the arc)
  - Spatial extent (starts AZ/CA, expands to full Western US)
  - Station record pins (accumulate as records fall)
  - Climate attribution index (CSI escalates 2 -> 5)

DATA SOURCES:
  - Primary: ERA5 reanalysis via CDS API (available ~5 days behind real time)
  - Cache: Local CSV files (auto-generated on first successful ERA5 fetch)
  - Fallback: Realistic synthetic grid seeded with confirmed station records
  - Station records: NWS SCAC, NOAA, WWA rapid attribution (March 20, 2026)

NARRATIVE FOCUS: Air Temperature Anomaly (degrees F above historical normal).
WHY: Low humidity across the Southwest means wet-bulb underestimates danger.
The story is the 25-32F early-season anomaly, not the absolute temperature.

USAGE:
  from scenarios_western_heatwave_march_2026 import SCENARIOS
  from earth_system_generator import run_scenario

  # Generate single snapshot
  run_scenario(SCENARIOS[2])  # March 18

  # Generate all 5
  for scenario in SCENARIOS:
      run_scenario(scenario)
"""

import os
import csv
import math
import numpy as np
from scipy.ndimage import gaussian_filter
from datetime import datetime


# ====================================================================
#                    THRESHOLD CONFIGURATION
# ====================================================================
# Air Temperature Anomaly (degrees F above historical March normal)
# Bands: (threshold_value, kml_color_aabbggrr, label)

WESTERN_HEATWAVE_THRESHOLDS = {
    'legend_title': 'Air Temp Anomaly (F above normal)',
    'unit_label': 'Anomaly (F)',
    'colorbar_title': 'Anomaly (F)',
    'colorscale': 'RdYlBu_r',
    'cmin': 0,
    'cmax': 35,
    'contour_levels_start': 0,
    'contour_levels_stop': 35,
    'contour_levels_step': 2,
    'contour_cmap': 'inferno_r',
    'height_multiplier': 100000,
    'height_base_subtract': True,
    'spike_stride': 200,
    'pop_radius_divisor': 100000,
    'legend_style': 'continuous',

    # Normal -> Warm -> Hot -> Extreme -> Record-Shattering
    'bands': [
        (0,            '80008000', 'Normal'),
        (10,           '80FFFF00', 'Warm'),
        (20,           '8000FFFF', 'Hot'),
        (25,           '800000FF', 'Extreme'),
        (30,           '80FF00FF', 'Record-Shattering'),
        (float('inf'), '800000FF', 'Beyond Scale'),
    ]
}


# ====================================================================
#                   POPULATION CENTERS
# ====================================================================

WESTERN_POPULATIONS = [
    {'name': 'Phoenix, AZ',        'lat': 33.4484, 'lon': -112.0742, 'pop': 1700000},
    {'name': 'Las Vegas, NV',      'lat': 36.1699, 'lon': -115.1398, 'pop':  650000},
    {'name': 'Los Angeles, CA',    'lat': 34.0522, 'lon': -118.2437, 'pop': 3900000},
    {'name': 'Palm Springs, CA',   'lat': 33.8303, 'lon': -116.5453, 'pop':   47500},
    {'name': 'Thermal, CA',        'lat': 33.2353, 'lon': -115.6064, 'pop':    2700},
    {'name': 'Denver, CO',         'lat': 39.7392, 'lon': -104.9903, 'pop':  715000},
    {'name': 'Salt Lake City, UT', 'lat': 40.7608, 'lon': -111.8910, 'pop':  200000},
    {'name': 'Albuquerque, NM',    'lat': 35.0844, 'lon': -106.6504, 'pop':  565000},
    {'name': 'Kansas City, MO',    'lat': 39.0997, 'lon': -94.5786,  'pop':  508000},
    {'name': 'Oklahoma City, OK',  'lat': 35.4676, 'lon': -97.5164,  'pop':  700000},
    {'name': 'Lubbock, TX',        'lat': 33.5779, 'lon': -101.8552, 'pop':  265000},
    {'name': 'St. Louis, MO',     'lat': 38.6270, 'lon': -90.1994,  'pop':  300000},
]


# ====================================================================
#              RECORD-BREAKING STATION PINS (by date)
# ====================================================================
# Each station has a 'first_date' -- the date it first appears in the
# visualization. Stations accumulate as the event progresses.

RECORD_STATIONS = {
    # --- March 14: First watches issued, early anomalies ---
    'Phoenix_AZ_early': {
        'lat': 33.4484, 'lon': -112.0742,
        'air_temp_f': 95.0, 'normal_high_f': 78.0, 'anomaly': 17.0,
        'first_date': '2026-03-14',
        'note': 'NWS issues first Extreme Heat Watch'
    },
    'Yuma_AZ_early': {
        'lat': 32.6549, 'lon': -114.6196,
        'air_temp_f': 98.0, 'normal_high_f': 82.0, 'anomaly': 16.0,
        'first_date': '2026-03-14',
        'note': 'Already tracking 15+ above normal'
    },
    'Palm_Springs_CA': {
        'lat': 33.8303, 'lon': -116.5453,
        'air_temp_f': 96.0, 'normal_high_f': 80.0, 'anomaly': 16.0,
        'first_date': '2026-03-14',
        'note': 'Coachella Valley heating up early'
    },

    # --- March 17: Heat dome locks in ---
    'Las_Vegas_NV_early': {
        'lat': 36.1699, 'lon': -115.1398,
        'air_temp_f': 92.0, 'normal_high_f': 70.0, 'anomaly': 22.0,
        'first_date': '2026-03-17',
        'note': 'Heat dome compressing over Great Basin'
    },
    'Thermal_CA': {
        'lat': 33.6353, 'lon': -116.1064,
        'air_temp_f': 100.0, 'normal_high_f': 82.0, 'anomaly': 18.0,
        'first_date': '2026-03-17',
        'note': 'First triple digits in Salton Sea basin'
    },
    'Tucson_AZ': {
        'lat': 32.2226, 'lon': -110.9747,
        'air_temp_f': 97.0, 'normal_high_f': 76.0, 'anomaly': 21.0,
        'first_date': '2026-03-17',
        'note': 'Southern AZ corridor heating'
    },

    # --- March 18: Records start falling ---
    'Phoenix_AZ_record': {
        'lat': 33.4484, 'lon': -112.0742,
        'air_temp_f': 101.0, 'normal_high_f': 78.0, 'anomaly': 23.0,
        'first_date': '2026-03-18',
        'note': 'Earliest 100+ day EVER recorded in Phoenix'
    },
    'Las_Vegas_NV_record': {
        'lat': 36.1699, 'lon': -115.1398,
        'air_temp_f': 94.0, 'normal_high_f': 70.0, 'anomaly': 24.0,
        'first_date': '2026-03-18',
        'note': 'Shatters all-time March high'
    },
    'Death_Valley_CA': {
        'lat': 36.4616, 'lon': -116.8666,
        'air_temp_f': 108.0, 'normal_high_f': 86.0, 'anomaly': 22.0,
        'first_date': '2026-03-18',
        'note': 'Earliest 105+ in Death Valley'
    },

    # --- March 20: Peak / national records ---
    'Yuma_AZ_record': {
        'lat': 32.6549, 'lon': -114.6196,
        'air_temp_f': 109.0, 'normal_high_f': 82.0, 'anomaly': 27.0,
        'first_date': '2026-03-20',
        'note': 'Broke 1954 record of 108F'
    },
    'Martinez_Lake_AZ': {
        'lat': 32.7167, 'lon': -114.3333,
        'air_temp_f': 112.0, 'normal_high_f': 80.0, 'anomaly': 32.0,
        'first_date': '2026-03-20',
        'note': 'Pending NWS validation - potential national record'
    },
    'Phoenix_AZ_peak': {
        'lat': 33.4484, 'lon': -112.0742,
        'air_temp_f': 105.0, 'normal_high_f': 78.0, 'anomaly': 27.0,
        'first_date': '2026-03-20',
        'note': 'Earliest 105F on record'
    },

    # --- March 21: Eastward expansion + Plains records ---
    'Denver_CO': {
        'lat': 39.7392, 'lon': -104.9903,
        'air_temp_f': 86.0, 'normal_high_f': 55.0, 'anomaly': 31.0,
        'first_date': '2026-03-21',
        'note': 'New all-time March record (broke 84F from 1971)'
    },
    'Salt_Lake_City_UT': {
        'lat': 40.7608, 'lon': -111.8910,
        'air_temp_f': 78.0, 'normal_high_f': 53.0, 'anomaly': 25.0,
        'first_date': '2026-03-21',
        'note': 'Inland reach of heat dome'
    },
    'Albuquerque_NM': {
        'lat': 35.0844, 'lon': -106.6504,
        'air_temp_f': 91.0, 'normal_high_f': 63.0, 'anomaly': 28.0,
        'first_date': '2026-03-21',
        'note': 'New all-time March record for NM'
    },
    'Burlington_CO': {
        'lat': 39.3058, 'lon': -102.2694,
        'air_temp_f': 96.0, 'normal_high_f': 57.0, 'anomaly': 39.0,
        'first_date': '2026-03-21',
        'note': 'CO state March record (ties 1907)'
    },
    'Phillipsburg_KS': {
        'lat': 39.7561, 'lon': -99.3240,
        'air_temp_f': 101.0, 'normal_high_f': 57.0, 'anomaly': 44.0,
        'first_date': '2026-03-21',
        'note': 'KS state March record; 101F in March'
    },
    'Hitchcock_IA': {
        'lat': 41.2247, 'lon': -95.8152,
        'air_temp_f': 97.0, 'normal_high_f': 53.0, 'anomaly': 44.0,
        'first_date': '2026-03-21',
        'note': 'IA state March record (broke 92F from 1986)'
    },
    'Cambridge_NE': {
        'lat': 40.2819, 'lon': -100.1665,
        'air_temp_f': 99.0, 'normal_high_f': 56.0, 'anomaly': 43.0,
        'first_date': '2026-03-21',
        'note': 'NE state March record (broke 98F from 1907)'
    },
    'Vermilion_SD': {
        'lat': 42.7794, 'lon': -96.9292,
        'air_temp_f': 97.0, 'normal_high_f': 51.0, 'anomaly': 46.0,
        'first_date': '2026-03-21',
        'note': 'SD state March record (broke 96F from 1943)'
    },
    'Luverne_MN': {
        'lat': 43.6536, 'lon': -96.2128,
        'air_temp_f': 88.0, 'normal_high_f': 45.0, 'anomaly': 43.0,
        'first_date': '2026-03-21',
        'note': 'MN state March record (ties 88F from 1910)'
    },
    'Harrisonville_MO': {
        'lat': 38.6533, 'lon': -94.3488,
        'air_temp_f': 97.0, 'normal_high_f': 58.0, 'anomaly': 39.0,
        'first_date': '2026-03-21',
        'note': 'MO state March record (broke 95F set day before)'
    },
    'Carlsbad_NM': {
        'lat': 32.4207, 'lon': -104.2288,
        'air_temp_f': 100.0, 'normal_high_f': 75.0, 'anomaly': 25.0,
        'first_date': '2026-03-21',
        'note': 'NM state March record (broke 99F set day before)'
    },

    # --- March 22: Pulse 1 consolidation ---
    'St_Louis_MO': {
        'lat': 38.6270, 'lon': -90.1994,
        'air_temp_f': 88.0, 'normal_high_f': 56.0, 'anomaly': 32.0,
        'first_date': '2026-03-22',
        'note': 'Daily March record; heat reaches Mississippi Valley'
    },
    'Springfield_MO': {
        'lat': 37.2089, 'lon': -93.2923,
        'air_temp_f': 90.0, 'normal_high_f': 57.0, 'anomaly': 33.0,
        'first_date': '2026-03-22',
        'note': 'NWS Record Event Report issued'
    },
    'Kansas_City_MO': {
        'lat': 39.0997, 'lon': -94.5786,
        'air_temp_f': 92.0, 'normal_high_f': 56.0, 'anomaly': 36.0,
        'first_date': '2026-03-22',
        'note': 'All-time March record for Kansas City'
    },
    'North_Platte_NE': {
        'lat': 41.1403, 'lon': -100.7601,
        'air_temp_f': 92.0, 'normal_high_f': 53.0, 'anomaly': 39.0,
        'first_date': '2026-03-22',
        'note': 'All-time March record; 78F swing from Mar 16 low'
    },

    # --- March 25: Pulse 2 ---
    'Denver_CO_pulse2': {
        'lat': 39.7392, 'lon': -104.9903,
        'air_temp_f': 87.0, 'normal_high_f': 57.0, 'anomaly': 30.0,
        'first_date': '2026-03-25',
        'note': 'Breaks own all-time March record AGAIN (87F > 86F from Mar 21)'
    },
    'Lubbock_TX': {
        'lat': 33.5779, 'lon': -101.8552,
        'air_temp_f': 100.0, 'normal_high_f': 67.0, 'anomaly': 33.0,
        'first_date': '2026-03-25',
        'note': 'Pulse 2 reaches Texas; forecast 100F'
    },
    'Las_Vegas_NV_pulse2': {
        'lat': 36.1699, 'lon': -115.1398,
        'air_temp_f': 98.0, 'normal_high_f': 71.0, 'anomaly': 27.0,
        'first_date': '2026-03-25',
        'note': 'Breaks own all-time March record AGAIN (98F > 97F from Mar 20)'
    },
    'Albuquerque_NM_pulse2': {
        'lat': 35.0844, 'lon': -106.6504,
        'air_temp_f': 94.0, 'normal_high_f': 63.0, 'anomaly': 31.0,
        'first_date': '2026-03-25',
        'note': 'Breaks own all-time March record AGAIN (94F > 91F from Mar 21)'
    },

    # --- March 26: Pulse 2 crests ---
    'Beaver_OK': {
        'lat': 36.8164, 'lon': -100.5198,
        'air_temp_f': 106.0, 'normal_high_f': 65.0, 'anomaly': 41.0,
        'first_date': '2026-03-26',
        'note': 'OK state March record (broke 104F at Frederick, 1971)'
    },
    'Rio_Grande_City_TX': {
        'lat': 26.3797, 'lon': -98.8203,
        'air_temp_f': 108.0, 'normal_high_f': 82.0, 'anomaly': 26.0,
        'first_date': '2026-03-26',
        'note': 'Ties TX all-time March record (108F, 1954 and 1902)'
    },
    'Ashland_KS': {
        'lat': 37.1886, 'lon': -99.7654,
        'air_temp_f': 104.0, 'normal_high_f': 62.0, 'anomaly': 42.0,
        'first_date': '2026-03-26',
        'note': 'KS state March record AGAIN (104F > 101F from Mar 21)'
    },
    'Carlsbad_NM_pulse2': {
        'lat': 32.4207, 'lon': -104.2288,
        'air_temp_f': 103.0, 'normal_high_f': 75.0, 'anomaly': 28.0,
        'first_date': '2026-03-26',
        'note': 'NM state March record AGAIN (103F > 100F Mar 21 > 99F Mar 20)'
    },
    'Morrisonville_IL': {
        'lat': 39.4200, 'lon': -89.4562,
        'air_temp_f': 94.0, 'normal_high_f': 55.0, 'anomaly': 39.0,
        'first_date': '2026-03-26',
        'note': 'IL state March record tied (94F, matches Harrisburg 1929)'
    },

    # --- March 30: Final eastward reach ---
    'Chicago_IL': {
        'lat': 41.9742, 'lon': -87.9073,
        'air_temp_f': 81.0, 'normal_high_f': 49.0, 'anomaly': 32.0,
        'first_date': '2026-03-30',
        'note': 'Daily March 30 record (broke 79F from 1986); heat dome reaches Great Lakes'
    },
}


# ====================================================================
#            DATE-PARAMETERIZED SNAPSHOT CONFIGURATION
# ====================================================================
# Each snapshot defines how the heat field evolves on that date.
# The fetch function reads these parameters to build the grid.

SNAPSHOT_CONFIGS = {
    '2026-03-14': {
        'label': 'The Spark',
        'csi_level': 2,
        'csi_description': '2x more likely due to climate change',
        'baseline_center_anomaly': 12.0,   # Peak of baseline Gaussian
        'baseline_spread': 4.0,            # Spatial extent (degrees)
        'baseline_center_lat': 33.5,       # AZ/CA border
        'baseline_center_lon': -114.0,
        'max_anomaly_clip': 22.0,
        'grid_lat_range': (30.0, 42.0),
        'grid_lon_range': (-125.0, -104.0),
        'grid_resolution': 0.5,
    },
    '2026-03-17': {
        'label': 'The Pivot',
        'csi_level': 3,
        'csi_description': '3x more likely due to climate change',
        'baseline_center_anomaly': 16.0,
        'baseline_spread': 5.0,
        'baseline_center_lat': 34.0,
        'baseline_center_lon': -114.5,
        'max_anomaly_clip': 26.0,
        'grid_lat_range': (30.0, 42.0),
        'grid_lon_range': (-125.0, -104.0),
        'grid_resolution': 0.5,
    },
    '2026-03-18': {
        'label': 'Records Fall',
        'csi_level': 4,
        'csi_description': '4x more likely due to climate change',
        'baseline_center_anomaly': 18.0,
        'baseline_spread': 5.5,
        'baseline_center_lat': 34.0,
        'baseline_center_lon': -114.0,
        'max_anomaly_clip': 28.0,
        'grid_lat_range': (30.0, 42.0),
        'grid_lon_range': (-125.0, -104.0),
        'grid_resolution': 0.5,
    },
    '2026-03-20': {
        'label': 'The Peak',
        'csi_level': 5,
        'csi_description': '5x more likely due to climate change',
        'baseline_center_anomaly': 22.0,
        'baseline_spread': 6.0,
        'baseline_center_lat': 33.5,
        'baseline_center_lon': -114.0,
        'max_anomaly_clip': 35.0,
        'grid_lat_range': (30.0, 42.0),
        'grid_lon_range': (-125.0, -104.0),
        'grid_resolution': 0.5,
    },
    '2026-03-21': {
        'label': 'Eastward Surge',
        'csi_level': 5,
        'csi_description': '5x more likely due to climate change',
        'baseline_center_anomaly': 20.0,
        'baseline_spread': 7.0,            # Wider: dome expanding east
        'baseline_center_lat': 36.0,       # Shifted north/east for Plains
        'baseline_center_lon': -108.0,
        'max_anomaly_clip': 48.0,          # SD: 46F anomaly
        'grid_lat_range': (25.0, 50.0),    # Mexico to Canada
        'grid_lon_range': (-125.0, -88.0), # Pacific to Mississippi Valley
        'grid_resolution': 0.5,
    },
    '2026-03-22': {
        'label': 'The Crest',
        'csi_level': 5,
        'csi_description': '5x more likely due to climate change',
        'baseline_center_anomaly': 18.0,   # SW slightly moderated
        'baseline_spread': 8.0,            # Very wide: 14 states
        'baseline_center_lat': 37.0,       # Centered on Plains
        'baseline_center_lon': -105.0,
        'max_anomaly_clip': 42.0,
        'grid_lat_range': (25.0, 50.0),
        'grid_lon_range': (-125.0, -65.0),  # Pacific to Atlantic
        'grid_resolution': 0.5,
    },
    '2026-03-25': {
        'label': 'Round Two',
        'csi_level': 5,
        'csi_description': '5x more likely due to climate change',
        'baseline_center_anomaly': 20.0,   # Ridge rebuilds
        'baseline_spread': 7.5,
        'baseline_center_lat': 35.5,       # Centered on SW + southern Plains
        'baseline_center_lon': -108.0,
        'max_anomaly_clip': 35.0,
        'grid_lat_range': (25.0, 50.0),
        'grid_lon_range': (-125.0, -65.0),  # Pacific to Atlantic
        'grid_resolution': 0.5,
    },
    '2026-03-26': {
        'label': 'Pulse 2 Crests',
        'csi_level': 5,
        'csi_description': '5x more likely due to climate change',
        'baseline_center_anomaly': 22.0,   # Southern Plains peak
        'baseline_spread': 8.0,            # Very wide
        'baseline_center_lat': 34.0,       # Shifted south for OK/TX
        'baseline_center_lon': -102.0,
        'max_anomaly_clip': 45.0,
        'grid_lat_range': (25.0, 50.0),
        'grid_lon_range': (-125.0, -65.0),  # Pacific to Atlantic
        'grid_resolution': 0.5,
    },
    '2026-03-30': {
        'label': 'The Reach',
        'csi_level': 4,
        'csi_description': '4x more likely due to climate change',
        'baseline_center_anomaly': 14.0,   # Dome weakening
        'baseline_spread': 9.0,            # Very wide but diffuse
        'baseline_center_lat': 38.0,       # Shifted northeast
        'baseline_center_lon': -95.0,      # Centered on Plains/Midwest
        'max_anomaly_clip': 35.0,
        'grid_lat_range': (25.0, 50.0),
        'grid_lon_range': (-125.0, -65.0),  # Pacific to Atlantic
        'grid_resolution': 0.5,
    },
}


# ====================================================================
#                   SHARED FETCH FUNCTION
# ====================================================================

def _load_era5_csv_cache(scenario, cache_path, status_callback=None):
    """Load previously cached ERA5 anomaly CSV. Returns True if successful."""
    if not os.path.exists(cache_path):
        return False
    if status_callback:
        status_callback(f"Loading cached ERA5 for {scenario['date']}...")
    try:
        lats, lons, values = [], [], []
        with open(cache_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                lats.append(float(row['lat']))
                lons.append(float(row['lon']))
                values.append(float(row['anomaly_f']))
        if lats:
            scenario['lats'] = lats
            scenario['lons'] = lons
            scenario['values'] = values
            return True
    except Exception as e:
        print(f"ERA5 cache read failed: {e}")
    return False


def _save_era5_csv_cache(lats, lons, anomalies_f, cache_path):
    """Save ERA5 anomaly data as CSV for future runs."""
    os.makedirs(os.path.dirname(cache_path) or '.', exist_ok=True)
    with open(cache_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['lat', 'lon', 'anomaly_f'])
        for lat, lon, val in zip(lats, lons, anomalies_f):
            writer.writerow([f'{lat:.4f}', f'{lon:.4f}', f'{val:.2f}'])
    print(f"  ERA5 anomaly cache saved: {cache_path} ({len(lats)} points)")


def _fetch_era5_from_cds(scenario, data_dir, status_callback=None):
    """
    Fetch ERA5 daily max 2m temperature from Copernicus CDS API,
    compute anomaly against 1991-2020 March climatology, and cache
    the result as a CSV.

    Requirements:
      - pip install cdsapi netCDF4
      - CDS account with API key in ~/.cdsapirc
        (register free at https://cds.climate.copernicus.eu/)

    The climatology is cached separately and reused across dates.
    Each event date is fetched once and cached as CSV.

    Returns True if successful, False to fall back to synthetic.
    """
    # Guard: check dependencies
    try:
        import cdsapi
        import netCDF4
    except ImportError as e:
        print(f"  ERA5 CDS fetch skipped (missing package: {e})")
        print(f"  Install with: pip install cdsapi netCDF4")
        return False

    date_str = scenario['date']
    config = SNAPSHOT_CONFIGS.get(date_str)
    if not config:
        return False

    # Grid extent from snapshot config
    lat_min, lat_max = config['grid_lat_range']
    lon_min, lon_max = config['grid_lon_range']
    # CDS area format: [North, West, South, East]
    area = [lat_max, lon_min, lat_min, lon_max]

    # Parse date components
    year, month, day = date_str.split('-')
    day_of_month = int(day)

    if status_callback:
        status_callback(f"Fetching ERA5 from CDS for {date_str}...")

    try:
        client = cdsapi.Client(quiet=True)
    except Exception as e:
        print(f"  CDS API client init failed: {e}")
        print(f"  Check ~/.cdsapirc (see https://cds.climate.copernicus.eu/how-to-api)")
        return False

    # --- Step 1: Fetch the event day (daily max 2m temp) ---
    event_nc = os.path.join(data_dir, f"era5_raw_{date_str}.nc")
    if not os.path.exists(event_nc):
        if status_callback:
            status_callback(f"Downloading ERA5 daily max for {date_str}...")
        print(f"  Requesting ERA5 daily max 2m temp for {date_str}...")
        try:
            client.retrieve(
                'reanalysis-era5-single-levels',
                {
                    'product_type': ['reanalysis'],
                    'variable': ['2m_temperature'],
                    'year': [year],
                    'month': [month],
                    'day': [day],
                    # Request hourly data to compute daily max ourselves
                    'time': [f'{h:02d}:00' for h in range(24)],
                    'area': area,
                    'data_format': 'netcdf',
                },
                event_nc
            )
        except Exception as e:
            print(f"  CDS fetch failed for {date_str}: {e}")
            return False
    else:
        print(f"  Using cached ERA5 NetCDF: {event_nc}")

    # --- Step 2: Fetch or load March climatology (1991-2020) ---
    # One climatology file per day-of-month, reusable across years
    clim_nc = os.path.join(data_dir, f"era5_clim_march_day{day_of_month:02d}.nc")
    clim_years = [str(y) for y in range(1991, 2021)]

    if not os.path.exists(clim_nc):
        if status_callback:
            status_callback(f"Downloading March {day_of_month} climatology (1991-2020)...")
        print(f"  Requesting ERA5 climatology for March {day_of_month} (1991-2020)...")
        print(f"  (This is a one-time download; future runs use cache)")
        try:
            client.retrieve(
                'reanalysis-era5-single-levels',
                {
                    'product_type': ['reanalysis'],
                    'variable': ['2m_temperature'],
                    'year': clim_years,
                    'month': ['03'],
                    'day': [f'{day_of_month:02d}'],
                    'time': [f'{h:02d}:00' for h in range(24)],
                    'area': area,
                    'data_format': 'netcdf',
                },
                clim_nc
            )
        except Exception as e:
            print(f"  CDS climatology fetch failed: {e}")
            return False
    else:
        print(f"  Using cached climatology: {clim_nc}")

    # --- Step 3: Compute anomaly ---
    if status_callback:
        status_callback(f"Computing anomaly for {date_str}...")

    try:
        # Read event day: compute daily max from hourly data
        ds_event = netCDF4.Dataset(event_nc, 'r')
        t2m_event = ds_event.variables['t2m'][:]  # shape: (hours, lat, lon)
        lats_nc = ds_event.variables['latitude'][:]
        lons_nc = ds_event.variables['longitude'][:]
        ds_event.close()

        # Daily max across all hours (axis=0)
        tmax_event_k = np.max(t2m_event, axis=0)  # shape: (lat, lon), Kelvin

        # Read climatology: compute daily max for each year, then average
        ds_clim = netCDF4.Dataset(clim_nc, 'r')
        t2m_clim = ds_clim.variables['t2m'][:]  # shape: (years*24, lat, lon)
        ds_clim.close()

        n_years = len(clim_years)
        n_hours = 24
        # Reshape to (years, hours, lat, lon) and take max per year
        t2m_clim_reshaped = t2m_clim.reshape(n_years, n_hours,
                                              t2m_clim.shape[1],
                                              t2m_clim.shape[2])
        tmax_clim_per_year = np.max(t2m_clim_reshaped, axis=1)  # (years, lat, lon)
        tmax_clim_mean_k = np.mean(tmax_clim_per_year, axis=0)  # (lat, lon)

        # Anomaly in Fahrenheit: (Kelvin difference) * 9/5
        anomaly_k = tmax_event_k - tmax_clim_mean_k
        anomaly_f = anomaly_k * 9.0 / 5.0

        # Clip negative anomalies to 0 (we only care about heat)
        anomaly_f = np.clip(anomaly_f, 0, None)

        # Flatten to point cloud (engine contract)
        flat_lats = []
        flat_lons = []
        flat_vals = []
        for i in range(len(lats_nc)):
            for j in range(len(lons_nc)):
                flat_lats.append(float(lats_nc[i]))
                flat_lons.append(float(lons_nc[j]))
                flat_vals.append(float(anomaly_f[i, j]))

        # Populate scenario
        scenario['lats'] = flat_lats
        scenario['lons'] = flat_lons
        scenario['values'] = flat_vals

        # Cache as CSV for future runs (instant load next time)
        cache_path = os.path.join(data_dir, f"era5_western_{date_str}.csv")
        _save_era5_csv_cache(flat_lats, flat_lons, flat_vals, cache_path)

        if status_callback:
            status_callback(
                f"ERA5 loaded: {len(flat_lats)} points, "
                f"anomaly range {min(flat_vals):.1f}-{max(flat_vals):.1f}F"
            )

        return True

    except Exception as e:
        print(f"  ERA5 anomaly computation failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def _try_era5_fetch(scenario, data_dir, status_callback=None):
    """
    Attempt ERA5 reanalysis fetch for the scenario date.

    Three-tier strategy:
      1. Local CSV cache (instant -- from previous successful fetch)
      2. CDS API fetch (requires cdsapi + netCDF4 + ~/.cdsapirc)
      3. Return False -> caller falls back to synthetic grid

    ERA5T (near-real-time) data is available ~5 days behind real time.
    First fetch for a date downloads from CDS and caches as CSV.
    Subsequent runs load from CSV cache instantly.

    CDS account (free): https://cds.climate.copernicus.eu/
    API setup: https://cds.climate.copernicus.eu/how-to-api
    """
    date_str = scenario['date']
    cache_path = os.path.join(data_dir, f"era5_western_{date_str}.csv")

    # Tier 1: Local CSV cache (instant)
    if _load_era5_csv_cache(scenario, cache_path, status_callback):
        return True

    # Tier 2: CDS API fetch (downloads, computes anomaly, caches CSV)
    if _fetch_era5_from_cds(scenario, data_dir, status_callback):
        return True

    # Tier 3: Caller falls back to synthetic
    return False


def _build_synthetic_field(scenario, data_dir, status_callback=None):
    """
    Build realistic synthetic anomaly field for the given date.

    Uses date-parameterized configuration from SNAPSHOT_CONFIGS to produce
    a spatially coherent heat field with sharp peaks at confirmed stations
    and smooth Gaussian baseline.

    The synthetic field is designed to be visually and scientifically
    plausible -- seeded with real station observations and realistic
    spatial patterns -- while clearly labeled as preliminary.
    """
    date_str = scenario['date']
    config = SNAPSHOT_CONFIGS[date_str]

    if status_callback:
        status_callback(f"Building synthetic field for {date_str} ({config['label']})...")

    lat_min, lat_max = config['grid_lat_range']
    lon_min, lon_max = config['grid_lon_range']
    res = config['grid_resolution']

    lat_steps = int((lat_max - lat_min) / res) + 1
    lon_steps = int((lon_max - lon_min) / res) + 1
    lat_arr = np.linspace(lat_min, lat_max, lat_steps)
    lon_arr = np.linspace(lon_min, lon_max, lon_steps)
    lon_grid, lat_grid = np.meshgrid(lon_arr, lat_arr)

    # STEP 1: Gaussian baseline -- represents the heat dome shape
    center_lat = config['baseline_center_lat']
    center_lon = config['baseline_center_lon']
    spread = config['baseline_spread']
    peak_anomaly = config['baseline_center_anomaly']

    dist_sq = ((lat_grid - center_lat) ** 2 + (lon_grid - center_lon) ** 2)
    baseline = peak_anomaly * np.exp(-dist_sq / (2 * spread ** 2))

    # STEP 2: Add confirmed station spikes using RBF-style distance decay
    # Stations active on or before this date get pinned
    spike_field = np.zeros_like(baseline)

    active_stations = {
        sid: st for sid, st in RECORD_STATIONS.items()
        if st['first_date'] <= date_str
    }

    for sid, station in active_stations.items():
        st_lat = station['lat']
        st_lon = station['lon']
        st_anomaly = station['anomaly']

        # RBF: sharp peak at station, decays over ~1.5 degrees
        dist = np.sqrt((lat_grid - st_lat) ** 2 + (lon_grid - st_lon) ** 2)
        influence_radius = 1.5  # degrees
        spike = st_anomaly * np.exp(-(dist ** 2) / (2 * (influence_radius / 2.5) ** 2))
        spike_field = np.maximum(spike_field, spike)

    # STEP 3: Combine baseline + spikes (spikes add, not replace)
    anomaly_field = baseline + spike_field * 0.6  # Blend: spikes boost baseline
    anomaly_field = np.clip(anomaly_field, 0, config['max_anomaly_clip'])

    # STEP 4: Ensure station pin locations hit their exact anomaly values
    for sid, station in active_stations.items():
        st_lat = station['lat']
        st_lon = station['lon']
        st_anomaly = station['anomaly']
        # Find nearest grid cell and force exact value
        lat_idx = np.argmin(np.abs(lat_arr - st_lat))
        lon_idx = np.argmin(np.abs(lon_arr - st_lon))
        anomaly_field[lat_idx, lon_idx] = max(anomaly_field[lat_idx, lon_idx], st_anomaly)

    # STEP 5: Light Gaussian smooth to reduce grid artifacts
    anomaly_field = gaussian_filter(anomaly_field, sigma=0.8)

    # Re-pin stations after smoothing (smoothing dilutes the exact values)
    for sid, station in active_stations.items():
        lat_idx = np.argmin(np.abs(lat_arr - station['lat']))
        lon_idx = np.argmin(np.abs(lon_arr - station['lon']))
        anomaly_field[lat_idx, lon_idx] = max(
            anomaly_field[lat_idx, lon_idx], station['anomaly']
        )

    # STEP 6: Extract as point cloud (engine contract)
    lats = []
    lons = []
    values = []
    for i in range(lat_grid.shape[0]):
        for j in range(lat_grid.shape[1]):
            lats.append(float(lat_grid[i, j]))
            lons.append(float(lon_grid[i, j]))
            values.append(float(anomaly_field[i, j]))

    scenario['lats'] = lats
    scenario['lons'] = lons
    scenario['values'] = values

    n_active = len(active_stations)
    if status_callback:
        status_callback(
            f"Built {len(lats)} grid points, {n_active} station pins "
            f"({config['label']}, CSI {config['csi_level']})"
        )

    return True


def fetch_western_heatwave(scenario, data_dir, status_callback=None):
    """
    Shared fetch function for all Western Heatwave snapshots.

    Tries ERA5 reanalysis first (cached CSV or API), falls back to
    realistic synthetic grid seeded with confirmed station records.

    This is the function referenced by every scenario dict's 'fetch' key.
    """
    if status_callback:
        status_callback(f"Fetching data for {scenario['date']}...")

    # Try ERA5 first
    if _try_era5_fetch(scenario, data_dir, status_callback):
        print(f"  ERA5 data loaded for {scenario['date']}")
        return True

    # Fall back to synthetic
    print(f"  ERA5 not available for {scenario['date']}, using synthetic")
    return _build_synthetic_field(scenario, data_dir, status_callback)


# ====================================================================
#                 BRIEFING TEXT BUILDER
# ====================================================================

def _build_briefing(date_str, config):
    """Build the HTML briefing text for a snapshot's intel card."""
    label = config['label']
    csi = config['csi_level']
    csi_desc = config['csi_description']

    # Date-specific narrative details
    details = {
        '2026-03-14': (
            'NWS issues first Extreme Heat Watches for AZ/CA. '
            'High-pressure ridge beginning to stall. '
            'Temperatures 15-20F above March normals.'
        ),
        '2026-03-17': (
            'Heat dome locks in over Great Basin. Anomaly jumps from '
            '"warm spring" to "dangerous summer." Widespread warnings issued. '
            'System stops moving and starts compressing.'
        ),
        '2026-03-18': (
            'First major records fall. Phoenix: earliest 100+F day ever (101F). '
            'Las Vegas: 94F shatters all-time March high. '
            'Death Valley: earliest 105+F.'
        ),
        '2026-03-20': (
            'Absolute apex. Yuma 109F (broke 1954 record of 108F). '
            'Martinez Lake 112F (pending NWS validation). '
            'Phoenix earliest 105F on record. '
            'WWA: "virtually impossible" without climate change.'
        ),
        '2026-03-21': (
            'Heat dome expanding eastward. Denver 86F new all-time March record. '
            '14 states break all-time March records: AZ, CA, NV, UT, CO, WY, '
            'ID, NM, KS, NE, IA, SD, MN, MO. '
            'Kansas 101F, South Dakota 97F, Iowa 97F. '
            'Colorado snowpack at historic lows.'
        ),
        '2026-03-22': (
            'Pulse 1 crest. Heat dome footprint extends to Mississippi Valley. '
            'Kansas City 92F, North Platte NE 92F, Springfield MO 90F, '
            'St. Louis 88F. Over 1,500 records broken across the event. '
            'Brief cooldown Sunday before Pulse 2 rebuilds.'
        ),
        '2026-03-25': (
            'Pulse 2 arrives. Ridge rebuilds over southern Rockies. '
            'Denver 87F -- breaks its own all-time March record AGAIN. '
            'Las Vegas forecast 98F (new March record). '
            'Lubbock TX forecast 100F. 200+ daily records forecast nationwide. '
            'NWS: 42.5M people under CSI 3+ conditions.'
        ),
        '2026-03-26': (
            'Pulse 2 crests. Oklahoma 106F (new state March record). '
            'Texas ties all-time March record at 108F. '
            'Kansas 104F (broke its own record set 5 days ago). '
            'Illinois 94F (ties state March record from 1929). '
            '17 states with broken all-time March records. '
            'Event total: 17 state records, 1500+ station records.'
        ),
        '2026-03-30': (
            'The final reach. Heat dome touches Great Lakes before '
            'cold front arrives. Chicago 81F (daily March 30 record). '
            'March 2026 confirmed as warmest March on record for the US, '
            'beating 2012 by half a degree F. Warmest Nov-Mar on record. '
            '17 state records. One of six most astonishing weather events '
            'of the century (Yale Climate Connections).'
        ),
    }

    detail = details.get(date_str, '')

    briefing = (
        f'<b>Western Heat Dome: {date_str} - {label}</b><br>'
        f'<br>'
        f'{detail}<br>'
        f'<br>'
        f'<b>Attribution:</b><br>'
        f'Climate Shift Index: Level {csi} ({csi_desc})<br>'
        f'<br>'
        f'Pins mark confirmed record-breaking observations.<br>'
        f'<br>'        
        f'<i>Data: ERA5 reanalysis (if available) or preliminary synthetic.</i>'
    )
    return briefing


def _build_description(date_str, config):
    """Build the plain-text description for gallery metadata."""
    label = config['label']
    csi = config['csi_level']

    descriptions = {
        '2026-03-14': (
            f'Western Heat Dome March 14, 2026: {label}. '
            f'NWS issues first Extreme Heat Watches. '
            f'Temperatures 15-20F above normal across AZ/CA. '
            f'Climate Shift Index: Level {csi}.'
        ),
        '2026-03-17': (
            f'Western Heat Dome March 17, 2026: {label}. '
            f'Heat dome locks over Great Basin. Anomaly jumps to dangerous levels. '
            f'20-25F above normal. '
            f'Climate Shift Index: Level {csi}.'
        ),
        '2026-03-18': (
            f'Western Heat Dome March 18, 2026: {label}. '
            f'Phoenix earliest 100+F ever. Las Vegas shatters March record (94F). '
            f'Climate Shift Index: Level {csi}.'
        ),
        '2026-03-20': (
            f'Western Heat Dome March 20, 2026: {label}. '
            f'Yuma 109F (broke 1954 record). Martinez Lake 112F (pending NWS). '
            f'WWA: 1-in-500-year event, "virtually impossible" without climate change. '
            f'Climate Shift Index: Level {csi}.'
        ),
        '2026-03-21': (
            f'Western Heat Dome March 21, 2026: {label}. '
            f'14 states break all-time March records. '
            f'Kansas 101F, Iowa 97F, South Dakota 97F, Minnesota 88F. '
            f'Denver 86F new all-time March record. '
            f'Climate Shift Index: Level {csi}.'
        ),
        '2026-03-22': (
            f'Western Heat Dome March 22, 2026: {label}. '
            f'Pulse 1 crests. Heat extends to Mississippi Valley. '
            f'Kansas City 92F, Springfield MO 90F, St. Louis 88F. '
            f'Over 1,500 records broken across 14+ states. '
            f'Climate Shift Index: Level {csi}.'
        ),
        '2026-03-25': (
            f'Western Heat Dome March 25, 2026: {label}. '
            f'Pulse 2 rebuilds. Denver 87F breaks own all-time March record again. '
            f'Las Vegas 98F, Albuquerque 94F, Lubbock TX 100F. '
            f'200+ daily records forecast. 42.5M under CSI 3+. '
            f'Climate Shift Index: Level {csi}.'
        ),
        '2026-03-26': (
            f'Western Heat Dome March 26, 2026: {label}. '
            f'Oklahoma 106F, Texas 108F (ties all-time March), '
            f'Kansas 104F (broke own 5-day-old record). '
            f'Illinois 94F (ties 1929 state March record). '
            f'17 states with all-time March records broken. '
            f'Climate Shift Index: Level {csi}.'
        ),
        '2026-03-30': (
            f'Western Heat Dome March 30, 2026: {label}. '
            f'Final snapshot. Chicago 81F (daily March record). '
            f'Heat dome reaches Great Lakes before cold front ends event. '
            f'March 2026: warmest March on record (US), warmest Nov-Mar on record. '
            f'17 state records, 1500+ station records. '
            f'Climate Shift Index: Level {csi}.'
        ),
    }
    return descriptions.get(date_str, f'Western Heat Dome {date_str}: {label}. CSI {csi}.')


def _build_encyclopedia(date_str, config):
    """Build rich encyclopedia 'i' card content for a snapshot.

    Structured as: What Happened, Climate Attribution, Earth System
    Context (organized by planetary boundaries), Record-Breaking
    Stations (accumulated to date), Data & Sources.

    The Earth System Context connects the heat event to planetary
    boundaries: climate change, freshwater change, biosphere
    integrity, land system change, and novel entities. Each snapshot
    emphasizes different boundaries as the event escalates.
    """
    label = config['label']
    csi = config['csi_level']
    csi_desc = config['csi_description']

    # Build station list: only stations active on or before this date
    station_lines = []
    for sid, station in RECORD_STATIONS.items():
        if station['first_date'] <= date_str:
            name = sid.replace('_', ' ')
            # Clean up duplicate city entries (e.g., Phoenix_AZ_early -> Phoenix AZ early)
            note = station.get('note', '')
            line = f"{name}: {station['air_temp_f']:.0f}F (+{station['anomaly']:.0f}F)"
            if note:
                line += f" -- {note}"
            station_lines.append(line)
    stations_html = '<br>'.join(station_lines)

    entries = {
        '2026-03-14': (
            '<b>What Happened</b><br>'
            'The National Weather Service issued Extreme Heat Watches across '
            'Arizona and Southern California as a high-pressure ridge began '
            'stalling over the Great Basin. Temperatures climbed 15-20F above '
            'March normals -- warm enough to break daily records but not yet '
            'at crisis levels. The pattern suggested a prolonged event.'
            '<br><br>'

            '<b>Climate Attribution</b><br>'
            f'Climate Shift Index: Level {csi} ({csi_desc}). '
            'Temperatures at this stage sit outside the range of natural '
            'variability but within the expanding envelope of the warming '
            'climate. A CSI of 2 means this warmth was made at least twice '
            'as likely by anthropogenic forcing.'
            '<br><br>'

            '<b>Earth System Context</b><br>'
            '<i>Climate Change:</i> The high-pressure stall pattern is '
            'intensifying. Research links more persistent ridges to Arctic '
            'amplification -- as the pole-to-equator temperature gradient '
            'weakens, the jet stream meanders more slowly and weather '
            'patterns lock in place longer.<br><br>'
            '<i>Freshwater Change:</i> March is peak snowpack accumulation '
            'season in the Western US. The Sierra Nevada, Cascades, and '
            'Rockies are banking water as snow that will supply rivers, '
            'reservoirs, and agriculture through summer. Heat arriving now '
            'is the worst possible timing -- it converts accumulation to '
            'ablation at the moment the snowpack should be deepening.'
        ),

        '2026-03-17': (
            '<b>What Happened</b><br>'
            'The high-pressure ridge locked into place over the Great Basin, '
            'transitioning from a warm spell into a dangerous heat event. '
            'Anomalies jumped from 15-20F to 20-25F above March normals. '
            'The system stopped moving and began compressing -- subsiding '
            'air heated adiabatically as it descended, amplifying surface '
            'temperatures. NWS upgraded from Heat Watches to Warnings '
            'across the Southwest.'
            '<br><br>'

            '<b>Climate Attribution</b><br>'
            f'Climate Shift Index: Level {csi} ({csi_desc}). '
            'At CSI 3, the event is moving beyond what historical climate '
            'records would predict. It belongs to the new climate, not '
            'the old one.'
            '<br><br>'

            '<b>Earth System Context</b><br>'
            '<i>Climate Change:</i> The compression phase is characteristic '
            'of heat domes -- descending air suppresses cloud formation, '
            'creating a positive feedback: clear skies allow more solar '
            'heating, which strengthens the high pressure, which forces more '
            'descent. Once locked in, these systems resist displacement by '
            'approaching weather systems.<br><br>'
            '<i>Freshwater Change:</i> Snowmelt acceleration is now '
            'measurable. River gauge stations in Arizona and Southern '
            'California show unseasonable flow increases. The Colorado '
            'River basin, already in a 23-year megadrought, faces '
            'earlier-than-modeled drawdown.<br><br>'
            '<i>Biosphere Integrity:</i> Stone fruit and almond orchards in '
            "California's Central Valley face false-spring risk. Trees "
            'respond to sustained warmth by breaking dormancy and flowering. '
            'If freezing nights return (common through April), the blossoms '
            'die and the crop is lost. The economic window between "warm '
            'enough to bloom" and "safe from frost" is narrowing as spring '
            'heat events intensify.'
        ),

        '2026-03-18': (
            '<b>What Happened</b><br>'
            'Major records began falling across the region. Phoenix recorded '
            'its earliest-ever 100F+ day (101F), a milestone that had never '
            'occurred before April. Las Vegas hit 94F, shattering its all-time '
            'March record. Death Valley reached its earliest-ever 105F+. The '
            'anomaly crossed 25F above normal at multiple stations -- '
            'territory where infrastructure and human physiology face '
            'compounding stress.'
            '<br><br>'

            '<b>Climate Attribution</b><br>'
            f'Climate Shift Index: Level {csi} ({csi_desc}). '
            'At CSI 4, the event is strongly attributable -- it could occur '
            'naturally, but the probability has been so amplified by warming '
            'that the human fingerprint dominates.'
            '<br><br>'

            '<b>Earth System Context</b><br>'
            '<i>Climate Change:</i> The "earliest ever" records are the '
            'signature of seasonal boundary destabilization. It is not just '
            'that summers are hotter -- spring is arriving with summer '
            'intensity. Systems calibrated to historical norms (irrigation '
            'schedules, construction work rules, school outdoor policies) '
            'face conditions they were not designed for, months early.<br><br>'
            '<i>Land System Change:</i> Fuel moisture in desert scrub and '
            'chaparral is dropping rapidly. Fire agencies monitor "energy '
            'release component" (ERC) -- a measure of available fire energy. '
            'March ERC values approaching June levels means fire season is '
            'effectively starting two months early. The firefighting workforce '
            'and aerial tanker fleet are not yet deployed for the season.<br><br>'
            '<i>Biosphere Integrity:</i> Urban heat islands in Phoenix and '
            'Las Vegas compound the anomaly. Concrete and asphalt retain '
            'daytime heat, preventing nighttime cooling. When overnight lows '
            'stay above 80F, the human body cannot recover from daytime heat '
            'stress. This is the mechanism that kills: not peak temperature '
            'alone, but the absence of physiological recovery.'
        ),

        '2026-03-20': (
            '<b>What Happened</b><br>'
            'The event reached its absolute apex. Yuma AZ hit 109F, breaking '
            'a 1954 record that had stood for 72 years. Martinez Lake AZ '
            'reached 112F (pending NWS validation). Phoenix recorded its '
            'earliest-ever 105F day. The anomaly reached 30-33F above March '
            'normals at multiple stations -- a magnitude that redefines what '
            '"March weather" means in the Western US.'
            '<br><br>'

            '<b>Climate Attribution</b><br>'
            f'Climate Shift Index: Level {csi} (maximum). '
            'World Weather Attribution conducted a rapid analysis and '
            'classified this event as "virtually impossible" without '
            'human-induced climate change -- a 1-in-500-year event in the '
            'current climate that would not have occurred at all in a '
            'pre-industrial atmosphere. CSI 5 means the anthropogenic '
            'signal is not a contributing factor but the dominant cause.'
            '<br><br>'

            '<b>Earth System Context</b><br>'
            '<i>Climate Change:</i> The WWA finding -- "virtually impossible" '
            'without climate change -- places this event in the category of '
            'phenomena that exist only because the Earth system has been '
            'shifted. The 1954 Yuma record was set in a climate with ~315 ppm '
            'CO2. The 2026 record was set at ~427 ppm. The additional energy '
            'trapped by that difference is what made this event possible.<br><br>'
            '<i>Freshwater Change:</i> Denver recorded 85F, 30F above normal. '
            'The Rocky Mountain snowpack that supplies the Colorado, Platte, '
            'and Arkansas river systems is under direct assault. Snowpack '
            'provides 75% of Western water supply. Early melt does not just '
            'shift timing -- rapid melt overwhelms reservoirs, causes '
            'flooding, and the water that runs off in March is not available '
            'in August when demand peaks.<br><br>'
            '<i>Land System Change:</i> Wildfire preconditioning is now '
            'severe. The combination of early heat and wind desiccation has '
            'reduced fuel moisture across Southern California chaparral and '
            'Arizona grasslands to levels normally seen in late May. Any '
            'ignition source -- lightning, powerline, human -- would find '
            'receptive fuels.<br><br>'
            '<i>Novel Entities (Energy System Feedback):</i> Early-season AC '
            'demand is spiking across the Southwest grid. Utilities planned '
            'for spring maintenance outages on generation assets -- those '
            'outages are being cancelled. Peaking plants (typically gas-fired) '
            'are coming online months early, adding CO2 emissions that '
            'reinforce the warming that caused the event. This is the '
            'feedback loop: heat drives energy demand drives emissions drives '
            'heat.'
        ),

        '2026-03-21': (
            '<b>What Happened</b><br>'
            'The heat dome surged eastward, smashing all-time March records in '
            '14 states simultaneously -- the largest single-day count of state '
            'March records in recorded history. Kansas hit 101F at Phillipsburg. '
            'Iowa reached 97F at Hitchcock. Nebraska 99F. South Dakota 97F. '
            'Minnesota 88F. Denver set a new all-time March record at 86F. '
            'The geographic extent was staggering: from the Pacific Coast to '
            'the Mississippi River, a continuous zone of anomaly 25-46F above '
            'normal.'
            '<br><br>'

            '<b>Climate Attribution</b><br>'
            f'Climate Shift Index: Level {csi} (maximum). '
            "The WWA 1-in-500-year classification was confirmed. CSI 5 "
            'conditions now cover an area from the Pacific Coast to the Great '
            'Plains -- roughly 1,500 miles of continuous extreme anomaly. '
            'The 14-state simultaneous record is itself a metric of how '
            'climate change amplifies the spatial coherence of heat events.'
            '<br><br>'

            '<b>Earth System Context</b><br>'
            '<i>Climate Change:</i> The eastward surge demonstrates how heat '
            'domes interact with the broader atmospheric circulation. As the '
            'ridge expands, it displaces the jet stream northward, pulling '
            'subtropical air into regions that normally experience cool spring '
            'conditions. The Great Plains in late March should be transitioning '
            'from winter -- instead, they are experiencing midsummer heat.<br><br>'
            '<i>Freshwater Change:</i> Colorado snowpack has plunged to 40% of '
            'median -- the lowest value for late March in 41 years of '
            'recordkeeping. The South Platte Basin has dropped below its '
            'historic minimum. The Arkansas and Platte River headwaters are '
            'now in the anomaly zone. Municipal water systems in Denver and '
            'downstream communities depend on gradual spring melt.<br><br>'
            '<i>Biosphere Integrity:</i> The Great Plains expansion brings '
            'the heat dome over the winter wheat belt. Winter wheat is '
            'vernalizing (completing its cold requirement) in March. Sudden '
            'heat can force premature heading, reducing grain fill time and '
            'yield. The US winter wheat crop, planted across Kansas, Oklahoma, '
            'and Texas, provides ~25% of US wheat production.<br><br>'
            '<i>Land System Change:</i> Nebraska is fighting its largest '
            'wildfire in state history (Morrill County, 640K+ acres). The '
            'expanded heat footprint means fire preconditioning extends from '
            'California grasslands to Great Plains rangeland. Spring '
            'phenology is running 20-30 days ahead of normal across the '
            'Central Plains and Rockies.'
        ),

        '2026-03-22': (
            '<b>What Happened</b><br>'
            'Pulse 1 crested. The heat dome footprint reached the Mississippi '
            'Valley: Kansas City 92F, Springfield MO 90F, St. Louis 88F, '
            'North Platte NE 92F. The event consolidated as one of the most '
            'astounding global weather events of the century -- over 1,500 '
            'records broken since March 18. NWS Record Event Reports issued '
            'from offices spanning 14+ states. A brief Sunday cooldown '
            'followed, but forecast models showed the ridge rebuilding for '
            'Pulse 2 by midweek.'
            '<br><br>'

            '<b>Climate Attribution</b><br>'
            f'Climate Shift Index: Level {csi} (maximum). '
            'Climate Central analysis: from March 24-27, more than 42.5 million '
            'people will experience at least one day with maximum temperatures '
            'at CSI 3 or higher. The event physical area may rival or exceed '
            'the 2012 and 2021 historic heat waves.'
            '<br><br>'

            '<b>Earth System Context</b><br>'
            '<i>Climate Change:</i> In Chanute, Kansas, temperatures went from '
            'a record low of 13F on March 16 to a record high of 91F on '
            'March 20 -- a 78F swing in four days. This type of intra-week '
            'variance is a signature of jet stream disruption, where blocking '
            'patterns alternate between Arctic intrusions and subtropical '
            'surges with no transitional weather between them.<br><br>'
            '<i>Freshwater Change:</i> Sierra Nevada snowpack imagery shows '
            'dramatic mid-March snowmelt. Despite average precipitation, the '
            'intense heat is driving rapid snowmelt that reduces water '
            'availability for California summer. Denver declared Stage 1 '
            'drought restrictions as reservoir storage dropped 5% below '
            'average.<br><br>'
            '<i>Biosphere Integrity:</i> Spring leaf-out is running 20-30 days '
            'ahead of normal across the Central Plains and Rockies, and 30+ '
            'days early in parts of Montana. The National Phenology Network '
            'reports the earliest spring on record for many locations. Early '
            'leaf-out exposes new growth to late-season frost risk.<br><br>'
            '<i>Land System Change:</i> Over 400 people were treated for '
            'heat-related illness at an Arizona airshow during the event. '
            'The early-season timing catches public health infrastructure '
            'unprepared: cooling centers not yet open, outdoor workers not '
            'acclimatized, school athletic programs following spring rules '
            'rather than summer heat protocols.'
        ),

        '2026-03-25': (
            '<b>What Happened</b><br>'
            'Pulse 2 arrived as forecast. The high-pressure ridge rebuilt over '
            'the southern Rockies, driving a new surge of record heat. Denver '
            'hit 87F -- breaking its own all-time March record that was set '
            'just four days earlier (86F on March 21). Las Vegas forecast to '
            'reach 98F, breaking its own record of 97F from March 20. '
            'Lubbock TX forecast 100F. NWS forecasts 200+ daily record highs '
            'across 28 states from coast to coast.'
            '<br><br>'

            '<b>Climate Attribution</b><br>'
            f'Climate Shift Index: Level {csi} (maximum). '
            'Climate Central: 42.5 million people across the western US will '
            'experience at least one day this week with CSI 3+. The two-pulse '
            'structure -- record heat, brief cooldown, more record heat -- '
            'extends the duration of physiological and infrastructure stress '
            'beyond any single-event precedent for March.'
            '<br><br>'

            '<b>Earth System Context</b><br>'
            '<i>Climate Change:</i> Cities breaking their own freshly-set '
            'records within days is the signature of a climate regime where '
            'the ceiling keeps rising. Denver has now broken its all-time '
            'March record three times in one week (85F, 86F, 87F). The NWS '
            'describes the weather pattern as "horribly stagnant" -- a '
            'persistent ridge that has kept Colorado warm and dry for months. '
            'Winter 2025-26 was the warmest on record across the western '
            'and central US.<br><br>'
            '<i>Freshwater Change:</i> Colorado snowpack is at historic lows. '
            'In the southern part of the state, snowpack is at only 25% of '
            'normal. Denver declared Stage 1 drought restrictions. The '
            'mountain snowpack that remains is melting under conditions more '
            'typical of early June than late March.<br><br>'
            '<i>Land System Change:</i> The combination of heat and dry '
            'conditions is raising fire danger across Colorado despite '
            'relatively light winds. NWS Boulder issued near-critical fire '
            'weather conditions for March 25. Nebraska continues to fight '
            'its largest wildfire in state history.<br><br>'
            '<i>Novel Entities (Energy System Feedback):</i> The two-pulse '
            'structure creates a ratchet effect on energy infrastructure. '
            'Utilities that brought peaking plants online for Pulse 1 cannot '
            'take them offline during the brief cooldown because Pulse 2 is '
            'already forecast. The net result is extended fossil fuel '
            'generation during what should be a low-demand shoulder season.'
        ),

        '2026-03-26': (
            '<b>What Happened</b><br>'
            'Pulse 2 crested harder than Pulse 1 in the southern corridor. '
            'Oklahoma hit 106F at Beaver -- a new state March record, breaking '
            '104F from Frederick in 1971. Texas tied its all-time March record '
            'at 108F. Kansas broke its own record for the second time in five '
            'days: 104F at Ashland, up from 101F at Phillipsburg on March 21. '
            'Carlsbad NM hit 103F, its third consecutive March record (100F, '
            '102F, 103F). Illinois tied its state March record at 94F, '
            'confirming the heat dome had formally reached the Midwest. The '
            'total: 17 states with all-time March records broken, over 1,500 '
            'station records, and the warmest November-through-March period '
            'in recorded US history is now a foregone conclusion.'
            '<br><br>'

            '<b>The Meteorological Engine</b><br>'
            'The mechanism driving this event is an omega block -- a jet '
            'stream configuration shaped like the Greek letter omega. A '
            'massive upper-level ridge of high pressure sits at the center, '
            'flanked by low-pressure troughs on either side. The '
            'configuration is remarkably stable: the surrounding lows lock '
            'the central high in place, resisting the normal west-to-east '
            'progression of weather systems.<br><br>'
            'At the 500-millibar level (~18,000 feet), geopotential heights '
            'reached 3.5 to 4 standard deviations above normal -- the '
            'strongest mid-tropospheric ridge ever observed in the '
            'southwestern US in March. Subsiding air within the high '
            'compresses and heats adiabatically as it descends, suppressing '
            'cloud formation and allowing intense solar radiation to heat '
            'the surface unopposed. The dome acts as a lid: warm air rises '
            'but is forced back down by the high pressure above, creating '
            'a self-reinforcing feedback.<br><br>'
            'The two-pulse structure occurs because the omega block weakens '
            'slightly as shortwave troughs erode its edges (the brief '
            'Sunday March 23 cooldown), then re-strengthens as the ridge '
            'rebuilds. This is not two separate events -- it is one '
            'persistent blocking pattern with internal oscillation. The '
            'eastward creep of the heat reflects the ridge axis slowly '
            'migrating, pulling subtropical air into regions progressively '
            'further from the original center.'
            '<br><br>'

            '<b>Climate Attribution</b><br>'
            f'Climate Shift Index: Level {csi} (maximum). '
            'The omega block pattern itself is a natural feature of '
            'atmospheric dynamics -- blocking events have occurred throughout '
            'the observational record. What climate change contributes is '
            'the baseline: the atmosphere is 1.3C warmer than pre-industrial '
            'levels, so every blocking event starts from a higher floor. '
            'WWA estimated this event is 4.7-7.2F (2.6-4C) hotter than it '
            'would have been without anthropogenic warming. The blocking '
            'creates the pattern; the warming sets the magnitude. Both are '
            'necessary; neither alone is sufficient.'
            '<br><br>'

            '<b>Anomaly vs Records</b><br>'
            'The ERA5 anomaly field shows 25-34F above normal extending from '
            'the Pacific coast to the Appalachians -- a continental-scale '
            'event. Yet all-time March state records concentrate in the '
            'interior West and Plains. The distinction: anomaly measures '
            'departure from the local climatological normal for that date. '
            'A record requires exceeding the highest temperature ever '
            'observed in any March. The Southeast and Appalachia have a '
            'history of warm March days from subtropical air surges, so '
            'their existing March ceilings are already high. The interior '
            'West and Plains, normally cold in March, have lower ceilings '
            'to break. The anomaly tells you the whole continent is '
            'abnormally hot. The pins tell you where the heat exceeded '
            'anything ever measured.'
            '<br><br>'

            '<b>Earth System Context</b><br>'
            '<i>Climate Change:</i> CSI 5 covered approximately 3 million '
            'square kilometers (29% of the continental US) on March 20 -- '
            'the largest CSI 5 extent on record since the index began in '
            '1970. The event physical area may rival the 2012 Midwest heat '
            'wave and the 2021 Pacific Northwest heat dome, but spans a '
            'wider geographic range than either.<br><br>'
            '<i>Freshwater Change:</i> Snowpack across the West is at or '
            'near record lows for late March. Colorado snowpack is at 25% '
            'of normal in the south, 50% in the north. Water supply and '
            'hydropower impacts are expected through summer, especially '
            'across the Colorado River Basin.<br><br>'
            '<i>Land System Change:</i> The Morrill County fire in Nebraska '
            'burned over 640,000 acres -- the largest wildfire in state '
            'history. Fire preconditioning now extends from California to '
            'the Great Plains. Spring phenology is 20-30 days ahead of '
            'normal across the Central Plains.<br><br>'
            '<i>Novel Entities (Energy System Feedback):</i> The two-pulse '
            'ratchet forced utilities to maintain emergency generation '
            'throughout the event. The transition from La Nina to ENSO '
            'neutral, with signs of a developing strong El Nino, suggests '
            'the background warming trend will accelerate through 2026-27.'
        ),

        '2026-03-30': (
            '<b>What Happened</b><br>'
            'The heat dome made its final eastward reach. Chicago hit 81F '
            'at O\'Hare Airport, breaking the March 30 daily record of 79F '
            'set in 1986. Thunderstorms and a cold front followed, marking '
            'the meteorological end of the event that started in the Arizona '
            'desert sixteen days earlier. The omega block that had locked '
            'the jet stream in place since mid-March finally lost coherence '
            'as northern-stream disturbances broke through.'
            '<br><br>'

            '<b>The Final Tally</b><br>'
            'March 2026 was confirmed as the warmest March on record for the '
            'United States, beating the previous record (2012) by approximately '
            'half a degree Fahrenheit. Yale Climate Connections classified the '
            'event as one of the six most astonishing weather events of the '
            'century. The numbers: 17 states broke all-time March temperature '
            'records. Over 1,500 individual station records fell. The national '
            'March temperature record was broken on three consecutive days '
            '(March 18-20), reaching 112F. Some locations broke not just March '
            'but April records -- and in a few cases, May records. It was the '
            'warmest November-through-March period in recorded US history.'
            '<br><br>'

            '<b>Climate Attribution</b><br>'
            f'Climate Shift Index: Level {csi}. '
            'As the event concludes, the attribution picture is clear. '
            'World Weather Attribution: "virtually impossible without '
            'human-induced climate change." Climate change added 4.7-7.2F '
            'to temperatures. Daniel Swain (Weather West) noted that by '
            'statistical anomaly metrics, this event was comparable to the '
            'June 2021 Pacific Northwest heat dome -- but occurred three '
            'months earlier in the year, when the atmosphere has a '
            'thermodynamic disadvantage (shorter days, weaker sun, snow '
            'cover still present). The fact that it happened anyway, '
            '"despite all the seasonal factors working against it," is '
            'the measure of how much the baseline has shifted.'
            '<br><br>'

            '<b>Earth System Context</b><br>'
            '<i>Climate Change:</i> March 2026 was the warmest March on '
            'record for at least a third, and possibly half, of the '
            'continental United States. The warmth was not confined to the '
            'heat dome\'s footprint -- even the first half of March, before '
            'the extreme event began, was notably mild nationwide. Winter '
            '2025-26 was the warmest on record across the western and '
            'central US. The event sits atop a warming trend that is '
            'raising the floor for every subsequent extreme.<br><br>'
            '<i>Freshwater Change:</i> The cascading impacts will outlast '
            'the heat. Record-low snowpack means reduced summer streamflow, '
            'lower reservoir levels, and water shortages. Lake Mead and '
            'Lake Powell are at 30-year lows. The Colorado River Basin '
            'faces its most stressed water year in memory. Denver declared '
            'Stage 1 drought restrictions during the event.<br><br>'
            '<i>Land System Change:</i> Nationally, 13,658 wildfires have '
            'been recorded in 2026 through late March -- nearly double the '
            '10-year average. Over 1.4 million acres have burned -- triple '
            'the average. The traditional fire season has not yet begun. '
            'Nebraska\'s Morrill County fire (640,000+ acres) was the '
            'largest in state history.<br><br>'
            '<i>Biosphere Integrity:</i> Spring leaf-out ran 20-30 days '
            'ahead of normal across the Central Plains and Rockies, with '
            'some Montana locations 30+ days early. This phenological shift '
            'exposes new growth to late frost risk and disrupts pollinator '
            'synchronization. Winter wheat across the southern Plains faced '
            'heat stress during vernalization -- a critical yield-limiting '
            'period.<br><br>'
            '<i>Looking Forward:</i> A strong El Nino is developing for '
            '2026-27, which will add further warming to an already '
            'record-warm baseline. The impacts of March 2026 -- depleted '
            'snowpack, early fire preconditioning, stressed water systems, '
            'disrupted phenology -- are not endpoints. They are initial '
            'conditions for the summer ahead.'
        ),
    }

    body = entries.get(date_str, '')

    # Assemble: header + body + stations + sources
    encyclopedia = (
        f'<b>Western Heat Dome: {date_str} -- {label}</b>'
        '<br><br>'
        + body +
        '<br><br>'
        f'<b>Record-Breaking Stations (as of {date_str})</b><br>'
        + stations_html +
        '<br><br>'
        '<b>Data &amp; Sources</b><br>'
        'Visualizations utilize modified Copernicus Climate Change Service '
        '(C3S) information [2026]. Temperature anomalies derived from ERA5 '
        'hourly 2m temperature data (Hersbach et al., 2020), computed as '
        'daily maximum departure from 1991-2020 climatological baseline. '
        'Neither the European Commission nor ECMWF is responsible for any '
        'use that may be made of the information it contains.<br>'
        'Station records: NWS Preliminary Record Event Reports; NOAA '
        'National Centers for Environmental Information (NCEI).<br>'
        'Attribution: World Weather Attribution rapid analysis (March 20, '
        '2026); Climate Central Climate Shift Index (CSI).<br>'
        'Planetary boundaries: Rockstrom et al. (2009), '
        'Richardson et al. (2023).<br>'
        'Visualization engine: Paloma\'s Orrery Earth System Generator.'
    )
    return encyclopedia


# ====================================================================
#                      SCENARIO DEFINITIONS
# ====================================================================

def _make_scenario(date_str):
    """Factory: build a scenario dict for a given date."""
    config = SNAPSHOT_CONFIGS[date_str]
    day = date_str.split('-')[2]
    label = config['label']
    csi = config['csi_level']

    # Build pin_stations: confirmed observations active on or before this date
    pin_stations = []
    for sid, station in RECORD_STATIONS.items():
        if station['first_date'] <= date_str:
            pin_stations.append({
                'name': sid.replace('_', ' '),
                'lat': station['lat'],
                'lon': station['lon'],
                'anomaly': station['anomaly'],
                'air_temp_f': station['air_temp_f'],
                'note': station.get('note', ''),
            })

    return {
        'scenario_id': f'western_heatwave_march_{day}',
        'name': f'Western Heat Dome Mar {day} - {label}',
        'date': date_str,
        'boundary_type': 'HEAT',
        'fetch': fetch_western_heatwave,
        'thresholds': WESTERN_HEATWAVE_THRESHOLDS,
        'populations': WESTERN_POPULATIONS,
        'description': _build_description(date_str, config),
        'briefing': _build_briefing(date_str, config),
        'encyclopedia': _build_encyclopedia(date_str, config),
        'pin_stations': pin_stations,
        'csi_level': csi,
        'csi_description': config['csi_description'],
        'narrative_label': label,
        'lats': [],
        'lons': [],
        'values': [],
    }

# The nine snapshots, ordered chronologically
SCENARIOS = [
    _make_scenario('2026-03-14'),
    _make_scenario('2026-03-17'),
    _make_scenario('2026-03-18'),
    _make_scenario('2026-03-20'),
    _make_scenario('2026-03-21'),
    _make_scenario('2026-03-22'),
    _make_scenario('2026-03-25'),
    _make_scenario('2026-03-26'),
    _make_scenario('2026-03-30'),
]


# ====================================================================
#                    BATCH GENERATION
# ====================================================================

def generate_all(engine_module=None):
    """
    Generate all 5 snapshots through the engine pipeline.

    Usage:
        from scenarios_western_heatwave_march_2026 import generate_all
        generate_all()

    Or from command line:
        python scenarios_western_heatwave_march_2026.py --generate-all
    """
    if engine_module is None:
        try:
            import earth_system_generator as engine_module
        except ImportError:
            print("ERROR: earth_system_generator.py not found in path.")
            print("       Run from the project directory.")
            return

    print("=" * 60)
    print("WESTERN HEAT DOME MARCH 2026: Generating all 9 snapshots")
    print("=" * 60)

    for i, scenario in enumerate(SCENARIOS):
        print(f"\n--- [{i+1}/9] {scenario['name']} ---")
        print(f"    Date: {scenario['date']}")
        print(f"    CSI:  Level {scenario['csi_level']} ({scenario['csi_description']})")
        print(f"    Label: {scenario['narrative_label']}")
        try:
            engine_module.run_scenario(scenario)
            print(f"    [OK] Pipeline complete")
        except Exception as e:
            print(f"    [ERROR] {e}")

    print("\n" + "=" * 60)
    print("All snapshots generated. Check data/ for outputs.")
    print("=" * 60)


# ====================================================================
#                    VALIDATION / DIAGNOSTICS
# ====================================================================

def validate_snapshots():
    """
    Quick validation: build all 5 synthetic fields and report stats.
    Does NOT require the engine -- just tests the fetch/data layer.
    """
    print("Validating 9 snapshot data fields...\n")

    for scenario in SCENARIOS:
        date_str = scenario['date']
        config = SNAPSHOT_CONFIGS[date_str]
        label = config['label']
        csi = config['csi_level']

        # Build synthetic (always, for validation)
        _build_synthetic_field(scenario, 'data')

        n_pts = len(scenario['lats'])
        v_min = min(scenario['values']) if scenario['values'] else 0
        v_max = max(scenario['values']) if scenario['values'] else 0
        v_mean = sum(scenario['values']) / n_pts if n_pts else 0

        # Count active stations for this date
        n_stations = sum(
            1 for st in RECORD_STATIONS.values()
            if st['first_date'] <= date_str
        )

        print(f"  {date_str} | {label:16s} | CSI {csi} | "
              f"{n_pts:5d} pts | "
              f"range {v_min:5.1f}-{v_max:5.1f}F | "
              f"mean {v_mean:5.1f}F | "
              f"{n_stations} stations")

    print("\nValidation complete.")


# ====================================================================
#                        CLI ENTRY POINT
# ====================================================================

if __name__ == '__main__':
    import sys

    if '--generate-all' in sys.argv:
        generate_all()
    elif '--validate' in sys.argv:
        validate_snapshots()
    else:
        # Default: validate only (no engine dependency)
        validate_snapshots()
