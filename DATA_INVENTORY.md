# Data Inventory (local, gitignored -- CURRENT state)

Repo copies stale/absent; this reflects the live local stores.

## By extension

| ext | count | total | biggest | newest |
|---|---|---|---|---|
| .vot | 4 | 295.1 MB | gaia_data_magnitude.vot (284.4 MB) | 2026-02-08 |
| .csv | 34 | 258.4 MB | V-Dem-CY-Core-v16.csv (202.5 MB) | 2026-04-25 |
| .nc | 18 | 161.1 MB | era5_clim_march_day22.nc (27.4 MB) | 2026-04-07 |
| .json | 47 | 132.7 MB | orbit_paths.json (130.4 MB) | 2026-06-30 |
| .backup | 4 | 130.7 MB | orbit_paths.json.backup (130.4 MB) | 2026-06-17 |
| .backup_old | 1 | 130.4 MB | orbit_paths.json.backup_old (130.4 MB) | 2026-06-17 |
| .pkl | 2 | 33.6 MB | star_properties_magnitude.pkl (31.1 MB) | 2025-09-16 |
| .pdf | 6 | 18.0 MB | IPC_Sudan_Acute_Food_Insecurity_Feb2026_Jan2027_Special_Report.pdf (7.1 MB) | 2026-06-22 |
| .zip | 1 | 15.6 MB | V-Dem-CY-Core-v16_csv.zip (15.6 MB) | 2026-04-19 |
| .png | 158 | 14.6 MB | 2026-03-21_heatmap_western_heatwave_march_21.png (807.0 KB) | 2026-06-30 |
| .kmz | 40 | 14.4 MB | western_heatwave_march_21_blockbuster.kmz (904.7 KB) | 2026-06-30 |
| .html | 49 | 9.6 MB | western_heatwave_march_26_teaser.html (1.4 MB) | 2026-06-30 |
| .geojson | 2 | 1.4 MB | IPC_SD_A_87143417_2026-06-22.geojson (700.6 KB) | 2026-06-22 |
| .kml | 114 | 1.3 MB | 2015-05-24_spikes_india_pak_2015.kml (107.5 KB) | 2026-06-29 |
| .xlsx | 20 | 328.0 KB | FTS_Trends_in_reported_funding_Yemen_2026_216f2bd7-c844-479c-b360-a2bb0fa9528b_as_on_2026-04-24.xlsx (16.7 KB) | 2026-04-24 |
| .js | 1 | 200.3 KB | chart.umd.js (200.3 KB) | 2026-04-24 |
| .md | 9 | 82.9 KB | food_insecurity_handoff_v2_2.md (11.7 KB) | 2026-04-26 |
| .txt | 1 | 9.3 KB | WFP_HDX_SCHEMA_SAMPLE.txt (9.3 KB) | 2026-04-25 |
| .py | 1 | 6.5 KB | extract_vdem.py (6.5 KB) | 2026-04-19 |
| .bak1 | 1 | 2.1 KB | close_approach_cache.json.bak1 (2.1 KB) | 2026-06-10 |
| .bak2 | 1 | 1.8 KB | close_approach_cache.json.bak2 (1.8 KB) | 2026-05-02 |

## orbit_paths.json

- entries: 1501, formats: {'data_points': 1501}
- points/entry: min 2, max 24479, total 1515366
- sample 'Mercury_Sun':
```
{
  "data_points": {
    "2025-05-13": {
      "x": -0.2169951535023722,
      "y": -0.4081076696680744,
      "z": -0.01344832493890828
    },
    "2025-05-14": {
      "x": -0.1975096438844687,
      "y": -0.4193449084872911,
      "z": -0.016153887542039
    },
    "2025-05-15": {
      "x": -0.1774383424648234,
      "y": -0.4293386211334898,
      "z": -0.0188115560073015
    },
    "2025-05-16": {
      "x": -0.1568446119250048,
      "y": -0.43806841263644,
      "z": -0.02141385190001423
    },
    "2025-05-17": {
      "x": -0.135791625023607,
      "y": -0.4455156350468274,
      "z": -0.02395345697914293
    },
    "2025-05-18": {
      "x": -0.1143425039387085,
      "y": -0.4516632821135773,
      "z": -0.02642319180928893
    },
    "2025-05-19": {
      "x": -0.0925604659741
```

## star_properties_magnitude.pkl

- object type: dict
- dict keys (first 20): ['unique_ids', 'star_names', 'spectral_types', 'V_magnitudes', 'B_magnitudes', 'object_types', 'is_messier', 'distance_ly', 'distance_pc', 'notes', 'Temperature', 'Luminosity', 'Abs_Mag', 'RA_ICRS', 'DE_ICRS', 'ra_str', 'dec_str', 'Stellar_Class', 'Object_Type_Desc', 'Source_Catalog']
