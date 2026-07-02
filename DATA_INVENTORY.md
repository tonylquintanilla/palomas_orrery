# Data Inventory (local, gitignored -- CURRENT state)

Repo copies stale/absent; this reflects the live local stores.

## By extension

| ext | count | total | biggest | newest |
|---|---|---|---|---|
| .vot | 4 | 295.1 MB | gaia_data_magnitude.vot (284.4 MB) | 2025-11-07 |
| .nc | 18 | 161.1 MB | era5_clim_march_day22.nc (27.4 MB) | 2026-04-07 |
| .csv | 15 | 34.9 MB | 3773_v3_niskin_hot001_yr01_to_hot348_yr35.csv (30.8 MB) | 2026-04-07 |
| .pkl | 2 | 33.6 MB | star_properties_magnitude.pkl (31.1 MB) | 2025-09-16 |
| .png | 157 | 14.6 MB | 2026-03-21_heatmap_western_heatwave_march_21.png (807.0 KB) | 2026-06-30 |
| .kmz | 39 | 14.4 MB | western_heatwave_march_21_blockbuster.kmz (904.7 KB) | 2026-06-30 |
| .html | 39 | 9.2 MB | western_heatwave_march_26_teaser.html (1.4 MB) | 2026-06-30 |
| .pdf | 1 | 7.1 MB | IPC_Sudan_Acute_Food_Insecurity_Feb2026_Jan2027_Special_Report.pdf (7.1 MB) | 2026-06-22 |
| .json | 48 | 2.9 MB | orbit_paths.json (740.1 KB) | 2026-06-30 |
| .kml | 114 | 1.3 MB | 2015-05-24_spikes_india_pak_2015.kml (107.5 KB) | 2026-06-29 |
| .geojson | 1 | 700.6 KB | IPC_SD_A_87143417_2026-06-22.geojson (700.6 KB) | 2026-06-22 |
| .backup | 4 | 424.3 KB | co2_mauna_loa_monthly.json.backup (177.4 KB) | 2026-06-23 |
| .backup_old | 1 | 40.0 KB | orbit_paths.json.backup_old (40.0 KB) | 2026-06-23 |
| .bak1 | 1 | 1.6 KB | close_approach_cache.json.bak1 (1.6 KB) | 2026-04-16 |
| .bak2 | 1 | 924.0 B | close_approach_cache.json.bak2 (924.0 B) | 2026-03-13 |

## orbit_paths.json

- entries: 3, formats: {'data_points': 3}
- points/entry: min 366, max 14851, total 15664
- sample 'Sun_Sun':
```
{
  "data_points": {
    "2026-04-03": {
      "x": 0.0,
      "y": 0.0,
      "z": 0.0
    },
    "2026-04-04": {
      "x": 0.0,
      "y": 0.0,
      "z": 0.0
    },
    "2026-04-05": {
      "x": 0.0,
      "y": 0.0,
      "z": 0.0
    },
    "2026-04-06": {
      "x": 0.0,
      "y": 0.0,
      "z": 0.0
    },
    "2026-04-07": {
      "x": 0.0,
      "y": 0.0,
      "z": 0.0
    },
    "1985-08-09": {
      "x": 0.0,
      "y": 0.0,
      "z": 0.0
    },
    "1985-08-10": {
      "x": 0.0,
      "y": 0.0,
      "z": 0.0
    },
    "1985-08-11": {
      "x": 0.0,
      "y": 0.0,
      "z": 0.0
    },
    "1985-08-12": {
      "x": 0.0,
      "y": 0.0,
      "z": 0.0
    },
    "1985-08-13": {
      "x": 0.0,
      "y": 0.0,
      "z": 0.0
    },
    "1985-08-14": {
      "x": 0.0,
   
```

## star_properties_magnitude.pkl

- object type: dict
- dict keys (first 20): ['unique_ids', 'star_names', 'spectral_types', 'V_magnitudes', 'B_magnitudes', 'object_types', 'is_messier', 'distance_ly', 'distance_pc', 'notes', 'Temperature', 'Luminosity', 'Abs_Mag', 'RA_ICRS', 'DE_ICRS', 'ra_str', 'dec_str', 'Stellar_Class', 'Object_Type_Desc', 'Source_Catalog']
