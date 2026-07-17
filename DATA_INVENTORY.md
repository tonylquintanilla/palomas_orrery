# Data Inventory (local, gitignored -- CURRENT state)

Repo copies stale/absent; this reflects the live local stores.

## Orrery Data -- By extension

| ext | count | total | biggest | newest |
|---|---|---|---|---|
| .vot | 4 | 295.1 MB | gaia_data_magnitude.vot (284.4 MB) | 2026-02-08 |
| .json | 49 | 262.3 MB | orbit_paths.json (130.4 MB) | 2026-07-16 |
| .nc | 18 | 161.1 MB | era5_clim_march_day22.nc (27.4 MB) | 2026-04-07 |
| .backup | 4 | 130.7 MB | orbit_paths.json.backup (130.4 MB) | 2026-06-17 |
| .backup_old | 1 | 130.4 MB | orbit_paths.json.backup_old (130.4 MB) | 2026-06-17 |
| .csv | 15 | 34.9 MB | 3773_v3_niskin_hot001_yr01_to_hot348_yr35.csv (30.8 MB) | 2026-04-07 |
| .pkl | 2 | 33.6 MB | star_properties_magnitude.pkl (31.1 MB) | 2025-09-16 |
| .png | 159 | 14.6 MB | 2026-03-21_heatmap_western_heatwave_march_21.png (807.0 KB) | 2026-06-30 |
| .kmz | 40 | 14.4 MB | western_heatwave_march_21_blockbuster.kmz (904.7 KB) | 2026-06-30 |
| .html | 40 | 9.5 MB | western_heatwave_march_26_teaser.html (1.4 MB) | 2026-06-30 |
| .pdf | 1 | 7.1 MB | IPC_Sudan_Acute_Food_Insecurity_Feb2026_Jan2027_Special_Report.pdf (7.1 MB) | 2026-06-22 |
| .kml | 114 | 1.3 MB | 2015-05-24_spikes_india_pak_2015.kml (107.5 KB) | 2026-06-29 |
| .geojson | 1 | 700.6 KB | IPC_SD_A_87143417_2026-06-22.geojson (700.6 KB) | 2026-06-22 |
| .bak1 | 1 | 2.1 KB | close_approach_cache.json.bak1 (2.1 KB) | 2026-06-10 |
| .bak2 | 1 | 1.8 KB | close_approach_cache.json.bak2 (1.8 KB) | 2026-05-02 |

## orbit_paths.json

- entries: 1501, formats: {'data_points': 1501}
- points/entry: min 2, max 24479, total 1515409
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

---

## Gallery Repo -- tonyquintanilla.github.io

Path: `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io`

**Total size:** 437.6 MB (358 files)

**GitHub Pages headroom:** 586 MB remaining of 1024 MB ceiling (42.7% used)

### By extension

| ext | count | total | biggest | newest |
|---|---|---|---|---|
| .json | 237 | 416.9 MB | current_comets_social_view_20260210_2331.json (32.2 MB) | 2026-07-16 |
| .kmz | 39 | 14.4 MB | western_heatwave_march_21_blockbuster.kmz (904.7 KB) | 2026-06-30 |
| .png | 1 | 5.1 MB | palomas_orrery_logo.png (5.1 MB) | 2025-11-27 |
| .py | 25 | 505.6 KB | gallery_studio.py (244.1 KB) | 2026-07-16 |
| .md | 9 | 366.4 KB | web_gallery_handoff.md (242.4 KB) | 2026-07-16 |
| .html | 5 | 184.7 KB | index.html (128.2 KB) | 2026-07-14 |
| .ico | 1 | 137.3 KB | favicon.ico (137.3 KB) | 2025-11-28 |
| .diff | 2 | 27.6 KB | gallery_cache_builder.py.diff (20.4 KB) | 2026-07-16 |
| .txt | 3 | 20.1 KB | horizons_results encke.txt (8.2 KB) | 2026-07-11 |
| .jsonl | 30 | 12.2 KB | encke.jsonl (632.0 B) | 2026-07-11 |
| .mermaid | 1 | 7.4 KB | gallery_navigation_flowchart.mermaid (7.4 KB) | 2026-03-08 |
| .patch | 1 | 7.0 KB | phaseb_studio.patch (7.0 KB) | 2026-06-16 |
| .url | 1 | 176.0 B | Paloma's Orrery - Interactive Astronomical Visualizations.url (176.0 B) | 2026-02-27 |
| (none) | 3 | 17.0 B | CNAME (17.0 B) | 2026-07-12 |

### Largest files (top 10)

| file | size | path |
|---|---|---|
| current_comets_social_view_20260210_2331.json | 32.2 MB | gallery\current_comets_social_view_20260210_2331.json |
| inner_planets_comets_solar_corona_20260207_1748.json | 30.5 MB | gallery\inner_planets_comets_solar_corona_20260207_1748.json |
| pluto_barycenter_social_view_20260211_0031.json | 25.2 MB | gallery\pluto_barycenter_social_view_20260211_0031.json |
| jupiter_system_social_view_20260211_0035.json | 21.9 MB | gallery\jupiter_system_social_view_20260211_0035.json |
| pluto_barycenter_system_20260208_1957.json | 17.7 MB | gallery\pluto_barycenter_system_20260208_1957.json |
| 3iatlas_jupiter_20260316_1222_mobile.json | 16.1 MB | gallery\3iatlas_jupiter_20260316_1222_mobile.json |
| artemis_moon_animation_20260406_mobile.json | 14.6 MB | gallery\artemis_moon_animation_20260406_mobile.json |
| mars_system_static_psyche_gravitational_assist_mobile.json | 14.1 MB | gallery\mars_system_static_psyche_gravitational_assist_mobile.json |
| 3iatlas_jupiter_20260316_1222.json | 11.9 MB | gallery\3iatlas_jupiter_20260316_1222.json |
| 16_psyche_20231014_animated_months_gallery.json | 11.7 MB | gallery\16_psyche_20231014_animated_months_gallery.json |

### gallery_metadata.json

- indexed entries: 148
- fields per entry: ['id', 'title', 'filename', 'category', 'category_label', 'description', 'size_kb', 'converted', 'mode', 'featured', 'subcategory', 'subcategory_label']
- categories: {'solar_system': 25, 'inner_planets': 10, 'climate': 76, 'outer_planets': 3, 'missions': 24, 'exoplanets': 3, 'stellar': 7}
- modes: {'landscape': 38, '(none)': 24, 'portrait': 58, 'both': 28}

---

## Headroom Summary

| repo | served size | ceiling | headroom | used |
|---|---|---|---|---|
| gallery | 437.6 MB | 1024 MB | 586 MB | 42.7% |
| orrery (gitignored data) | 1.1 GB | n/a (not served) | -- | -- |

Note: orrery data is local/gitignored. If orbit cache files are pushed to either repo for web serving, re-run this inventory to update headroom.
