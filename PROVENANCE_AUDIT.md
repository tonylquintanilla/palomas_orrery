# Paloma's Orrery -- Provenance Audit

Generated: April 15, 2026
Files scanned: 100
Total findings: 5029
Constants: 87 | Dict values: 3591 | String claims: 1351

---

## Risk Matrix: Vulnerability x Criticality

**Vulnerability** (how likely to be wrong):
- 1 = Fetched (authoritative pipeline)
- 2 = Sourced (has citation)
- 3 = Stale (may have changed)
- 4 = Recalled (LLM training data, no citation)

**Criticality** (impact if wrong):
- 1 = Cosmetic (colors, labels)
- 2 = Internal (used but not displayed)
- 3 = Load-bearing (drives geometry)
- 4 = Public-facing (hover text, gallery)
- 5 = Propagating (imported by other modules)

**Score = V x C** | Action thresholds:
- 16-20: FIX NOW
- 10-15: FIX NEXT SESSION
- 5-9: ADD SOURCE WHEN TOUCHED
- 1-4: NO ACTION NEEDED

---

## Priority Summary

| Tier | Score | Action | Count |
|------|-------|--------|------:|
| 1 | 16-20 | FIX NOW | 2497 |
| 2 | 10-15 | FIX NEXT SESSION | 1397 |
| 3 | 5-9 | ADD SOURCE WHEN TOUCHED | 1134 |
| 4 | 1-4 | NO ACTION NEEDED | 1 |

---

## INCONSISTENCIES (Same concept, different values)

These are the highest-risk findings: the same physical
concept has different numeric values in different files.

### KM_PER_AU

**Values found:** 149597870.7, 149600000.0
**Files:** close_approach_data.py, constants_new.py, planet_visualization.py, sgr_a_star_data.py

- `close_approach_data.py:50` -- `AU_TO_KM = 149597870.7`
- `constants_new.py:23` -- `KM_PER_AU = 149597870.7`
- `planet_visualization.py:278` -- `KM_PER_AU = 149597870.7`
- `sgr_a_star_data.py:140` -- `AU_TO_KM = 149600000.0`

**Action:** Determine correct value with citation. Consolidate to single source of truth in constants_new.py. Replace duplicates with imports.

---

## DUPLICATES (Same value, multiple files)

These constants have consistent values but are defined
in multiple files instead of imported from one source.

- **CORE_AU** = 0.00093 -- in constants_new.py, planet_visualization.py, planet_visualization_utilities.py
- **RADIATIVE_ZONE_AU** = 0.00325 -- in constants_new.py, planet_visualization.py, planet_visualization_utilities.py
- **SOLAR_RADIUS** = 0.00465 -- in constants_new.py, planet_visualization.py, planet_visualization_utilities.py
- **CHROMOSPHERE_RADII** = 1.5 -- in constants_new.py, planet_visualization.py, planet_visualization_utilities.py
- **INNER_CORONA_RADII** = 3 -- in constants_new.py, planet_visualization.py, planet_visualization_utilities.py
- **OUTER_CORONA_RADII** = 50 -- in constants_new.py, planet_visualization.py, planet_visualization_utilities.py
- **TERMINATION_SHOCK_AU** = 94 -- in constants_new.py, planet_visualization.py, planet_visualization_utilities.py
- **HELIOPAUSE_RADII** = 26449 -- in constants_new.py, planet_visualization.py, planet_visualization_utilities.py
- **INNER_LIMIT_OORT_CLOUD_AU** = 2000 -- in constants_new.py, planet_visualization.py, planet_visualization_utilities.py
- **INNER_OORT_CLOUD_AU** = 20000 -- in constants_new.py, planet_visualization.py, planet_visualization_utilities.py
- **OUTER_OORT_CLOUD_AU** = 100000 -- in constants_new.py, planet_visualization.py, planet_visualization_utilities.py
- **GRAVITATIONAL_INFLUENCE_AU** = 126000 -- in constants_new.py, planet_visualization.py, planet_visualization_utilities.py
- **flattened_analysis['temp_le_zero']** = 0 -- in hr_diagram_apparent_magnitude.py, hr_diagram_distance.py, planetarium_apparent_magnitude.py, planetarium_distance.py
- **flattened_analysis['missing_lum']** = 0 -- in planetarium_apparent_magnitude.py, planetarium_distance.py
- **result['confirmed']** = 0 -- in save_utils.py, social_media_export.py

**Action:** Consolidate to constants_new.py and import.

---

## Tier 1: FIX NOW (Score 16-20)

### apsidal_markers.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 1786 | ENCOUNTER_THRESHOLD_AU | 0.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |

### asteroid_belt_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 64 | claim: 11.86 years | 11.86 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 114 | claim: 4 AU | 4 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 116 | claim: 3.2 AU | 3.2 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 117 | claim: 940 km | 940 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 120 | claim: 2.7 AU | 2.7 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 151 | claim: 2.7 AU | 2.7 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 198 | claim: 3.2 AU | 3.2 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 200 | claim: 2.7 AU | 2.7 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 236 | claim: 5 AU | 5 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 239 | claim: 3.97 AU | 3.97 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 257 | claim: 120 degrees | 120 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 259 | claim: 0 deg | 0 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 259 | claim: 120 deg | 120 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 259 | claim: 240 deg | 240 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 270 | claim: 17 degree | 17 degree | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 290 | claim: 3.97 AU | 3.97 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 292 | claim: 120 deg | 120 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 328 | claim: 6 AU | 6 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 330 | claim: 60 deg | 60 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 332 | claim: 5.2 AU | 5.2 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 334 | claim: 250 km | 250 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 351 | claim: 60 degrees | 60 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 363 | claim: 23 degree | 23 degree | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 384 | claim: 60 deg | 60 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 422 | claim: 60 deg | 60 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 424 | claim: 5.2 AU | 5.2 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 443 | claim: 60 degrees | 60 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 455 | claim: 23 degree | 23 degree | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 476 | claim: 60 deg | 60 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |

### catalog_selection.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 36 | counts['hip_bright_count'] | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 37 | counts['hip_mid_count'] | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 38 | counts['gaia_mid_count'] | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 39 | counts['gaia_faint_count'] | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 40 | counts['total_stars'] | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 41 | counts['plottable_count'] | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 42 | counts['missing_temp_only'] | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 43 | counts['missing_lum_only'] | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |

### celestial_objects.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 34 | claim: 27.32 days | 27.32 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 39 | claim: 27.32 days | 27.32 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 47 | claim: 27.32 days | 27.32 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 66 | claim: 64 km | 64 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 66 | claim: 1 km | 1 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 88 | claim: 113 km | 113 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 88 | claim: 4.28 days | 4.28 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 96 | claim: 104 km | 104 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 96 | claim: 4.28 days | 4.28 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 102 | claim: 21 km | 21 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 102 | claim: 5 km | 5 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 108 | claim: 40 km | 40 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 108 | claim: 446 hours | 446 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 114 | claim: 51 km | 51 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 135 | claim: 800 AU | 800 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 151 | claim: 6.39 days | 6.39 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 157 | claim: 6.39 days | 6.39 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 175 | claim: 49 days | 49 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 175 | claim: 18 days | 18 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 183 | claim: 49 days | 49 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 183 | claim: 18 days | 18 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 183 | claim: 3.9 hours | 3.9 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 191 | claim: 15.79 days | 15.79 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 198 | claim: 15.79 days | 15.79 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 210 | claim: 312 km | 312 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 210 | claim: 615 km | 615 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 215 | claim: 25.22 days | 25.22 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 222 | claim: 25.22 days | 25.22 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 250 | claim: 9.54 days | 9.54 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 258 | claim: 9.54 days | 9.54 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 262 | claim: 7 km | 7 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 262 | claim: 090 km | 090 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 270 | claim: 12.44 days | 12.44 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 281 | claim: 81 k | 81 k | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 436 | claim: 4 km | 4 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 478 | claim: 5.37 years | 5.37 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 478 | claim: 9 km | 9 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 479 | claim: 1.42 AU | 1.42 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 487 | claim: 8.252 years | 8.252 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 487 | claim: 2.6 km | 2.6 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 488 | claim: 1.18 AU | 1.18 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 490 | claim: 1.18 AU | 1.18 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 495 | claim: 5.5 years | 5.5 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 496 | claim: 1.41 AU | 1.41 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 553 | claim: 0.56 AU | 0.56 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 610 | claim: 0.33 AU | 0.33 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 616 | claim: 8 days | 8 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 621 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 630 | claim: 8 days | 8 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 646 | claim: 33 days | 33 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 888 | claim: 7.08 hours | 7.08 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 893 | claim: 7.15 hours | 7.15 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 898 | claim: 11.95 hours | 11.95 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 903 | claim: 16.20 hours | 16.20 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1023 | claim: 12.317 hours | 12.317 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1028 | claim: 22.159 hours | 22.159 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1083 | claim: 15.79 days | 15.79 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1083 | claim: 700 km | 700 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1090 | claim: 25.22 days | 25.22 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1090 | claim: 100 km | 100 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1097 | claim: 9.54 days | 9.54 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1097 | claim: 440 km | 440 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1104 | claim: 12.44 days | 12.44 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1104 | claim: 170 km | 170 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1111 | claim: 49 days | 49 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1111 | claim: 310 km | 310 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1117 | claim: 18 days | 18 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1117 | claim: 170 km | 170 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1123 | claim: 18.023 days | 18.023 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1123 | claim: 250 km | 250 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1124 | claim: 175 km | 175 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1129 | claim: 40.5 light-years | 40.5 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1133 | claim: 40.5 light-years | 40.5 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1141 | claim: 1.5 day | 1.5 day | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1141 | claim: 400 K | 400 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1149 | claim: 2.4 day | 2.4 day | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1157 | claim: 4.0 day | 4.0 day | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1165 | claim: 6.1 day | 6.1 day | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1173 | claim: 9.2 day | 9.2 day | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1181 | claim: 12.4 day | 12.4 day | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1189 | claim: 18.8 day | 18.8 day | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1189 | claim: 173 K | 173 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1192 | claim: 292 light-years | 292 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1208 | claim: 14.6 days | 14.6 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1227 | claim: 4.24 light-years | 4.24 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1231 | claim: 4.24 light-years | 4.24 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1239 | claim: 11.2 day | 11.2 day | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |

### close_approach_data.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 50 | AU_TO_KM | 149597870.7 | 4 | 5 | **20** | No source citation (recalled) | Data constant imported by 1 modules |

### comet_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 13 | claim: 8.33 R_sun | 8.33 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 29 | claim: 8 km | 8 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 30 | claim: 60 km | 60 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 31 | claim: 5 km | 5 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 32 | claim: 2 km | 2 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 33 | claim: 5 km | 5 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 34 | claim: 5 km | 5 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 35 | claim: 4 km | 4 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 36 | claim: 3 km | 3 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 37 | claim: 8 km | 8 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 38 | claim: 10 km | 10 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 40 | claim: 2.6 km | 2.6 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 41 | claim: 3 km | 3 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 42 | claim: 9 km | 9 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 68 | claim: 76 years | 76 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 140 | claim: 175.1 deg | 175.1 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 144 | claim: 5 km | 5 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 144 | claim: 0.0023 AU | 0.0023 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 153 | claim: 175 deg | 175 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 165 | claim: 1.356 AU | 1.356 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 166 | claim: 1.8 AU | 1.8 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 167 | claim: 0.69 deg | 0.69 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 168 | claim: 58 km | 58 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 174 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 174 | claim: 20 deg | 20 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 188 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 190 | claim: 0.358 AU | 0.358 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 197 | claim: 6 AU | 6 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 199 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 202 | claim: 120 deg | 120 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 212 | claim: 000 year | 000 year | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 222 | claim: 10 deg | 10 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 225 | claim: 1.232 R_sun | 1.232 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 228 | claim: 6 hours | 6 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 244 | claim: 1 AU | 1 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 252 | claim: 8.25 year | 8.25 year | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 253 | claim: 2.6 km | 2.6 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 263 | claim: 5.5 year | 5.5 year | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 274 | claim: 5.37 year | 5.37 year | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 275 | claim: 9 km | 9 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 422 | claim: 100 km | 100 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 424 | claim: 400 kg | 400 kg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 424 | claim: 3.45 solar radii | 3.45 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 425 | claim: 165 km | 165 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 434 | claim: 100 km | 100 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 442 | claim: 3.45 R_sun | 3.45 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 442 | claim: 0.016 AU | 0.016 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 447 | claim: 6 hours | 6 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 453 | claim: 18.8 R_sun | 18.8 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 453 | claim: 0.087 AU | 0.087 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 453 | claim: 6.0 R_sun | 6.0 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 453 | claim: 0.028 AU | 0.028 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 458 | claim: 6.0 R_sun | 6.0 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 458 | claim: 0.028 AU | 0.028 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 459 | claim: 3.45 R_sun | 3.45 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 459 | claim: 0.016 AU | 0.016 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 460 | claim: 3.0 R_sun | 3.0 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 460 | claim: 0.014 AU | 0.014 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 462 | claim: 8.3 R_sun | 8.3 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 462 | claim: 0.039 AU | 0.039 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 466 | claim: 3.45 R_sun | 3.45 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 466 | claim: 0.016 AU | 0.016 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 470 | claim: 1.2 R_sun | 1.2 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 471 | claim: 8.33 R_sun | 8.33 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 476 | claim: 1.23 R_sun | 1.23 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 476 | claim: 0.006 AU | 0.006 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 476 | claim: 556 km | 556 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 477 | claim: 40 hours | 40 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 477 | claim: 28 R_sun | 28 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 477 | claim: 0.132 AU | 0.132 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 483 | claim: 0.006 AU | 0.006 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 483 | claim: 1.23 R_sun | 1.23 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 483 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 484 | claim: 663 years | 663 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 527 | claim: 0.039 AU | 0.039 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 528 | claim: 0.132 AU | 0.132 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 617 | claim: 40 hours | 40 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 618 | claim: 8.33 R_sun | 8.33 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 618 | claim: 0.039 AU | 0.039 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 619 | claim: 6 R_sun | 6 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 619 | claim: 0.028 AU | 0.028 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 620 | claim: 3.45 R_sun | 3.45 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 620 | claim: 0.016 AU | 0.016 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 620 | claim: 3.0 R_sun | 3.0 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 620 | claim: 0.014 AU | 0.014 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 621 | claim: 1.23 R_sun | 1.23 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 621 | claim: 0.006 AU | 0.006 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 621 | claim: 556 km | 556 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 622 | claim: 29 R_sun | 29 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 622 | claim: 0.132 AU | 0.132 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 832 | claim: 15 degree | 15 degree | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 970 | claim: 5 degree | 5 degree | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1215 | claim: 120 deg | 120 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1282 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1381 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1382 | claim: 8 km | 8 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1384 | claim: 0.586 AU | 0.586 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1392 | claim: 60 km | 60 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1401 | claim: 0.295 AU | 0.295 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1410 | claim: 0.10 AU | 0.10 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1421 | claim: 0.197 AU | 0.197 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1428 | claim: 0.008 AU | 0.008 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1428 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1444 | claim: 5 AU | 5 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1445 | claim: 4 AU | 4 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1446 | claim: 3 AU | 3 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |

### constants_new.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 19 | DEFAULT_MARKER_SIZE | 7 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 21 | CENTER_MARKER_SIZE | 10 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 22 | LIGHT_MINUTES_PER_AU | 8.3167 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 23 | KM_PER_AU | 149597870.7 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 26 | CORE_AU | 0.00093 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 27 | RADIATIVE_ZONE_AU | 0.00325 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 28 | SOLAR_RADIUS_AU | 0.00465047 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 31 | CHROMOSPHERE_RADII | 1.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 32 | INNER_CORONA_RADII | 3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 33 | OUTER_CORONA_RADII | 50 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 36 | TERMINATION_SHOCK_AU | 94 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 37 | HELIOPAUSE_RADII | 26449 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 40 | INNER_LIMIT_OORT_CLOUD_AU | 2000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 41 | INNER_OORT_CLOUD_AU | 20000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 42 | OUTER_OORT_CLOUD_AU | 100000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 43 | GRAVITATIONAL_INFLUENCE_AU | 126000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 46 | PARKER_CLOSEST_RADII | 8.2 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 55 | CENTER_BODY_RADII['Sun'] | 696340 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 56 | CENTER_BODY_RADII['Mercury'] | 2440 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 57 | CENTER_BODY_RADII['Venus'] | 6052 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 63 | CENTER_BODY_RADII['Uranus'] | 25362 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 64 | CENTER_BODY_RADII['Neptune'] | 24622 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 65 | CENTER_BODY_RADII['Pluto'] | 1188 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 66 | CENTER_BODY_RADII['Bennu'] | 0.262 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 67 | CENTER_BODY_RADII['Eris'] | 1163 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 68 | CENTER_BODY_RADII['Haumea'] | 816 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 69 | CENTER_BODY_RADII['Makemake'] | 715 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 70 | CENTER_BODY_RADII['Arrokoth'] | 0.0088 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 71 | CENTER_BODY_RADII['Planet 9'] | 24000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 76 | KNOWN_ORBITAL_PERIODS['Mercury'] | 87.969 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 77 | KNOWN_ORBITAL_PERIODS['Venus'] | 224.701 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 78 | KNOWN_ORBITAL_PERIODS['Earth'] | 365.256 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 79 | KNOWN_ORBITAL_PERIODS['Mars'] | 686.98 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 80 | KNOWN_ORBITAL_PERIODS['Jupiter'] | 4332.589 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 81 | KNOWN_ORBITAL_PERIODS['Saturn'] | 10759.22 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 82 | KNOWN_ORBITAL_PERIODS['Uranus'] | 30688.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 83 | KNOWN_ORBITAL_PERIODS['Neptune'] | 60189.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 86 | KNOWN_ORBITAL_PERIODS['Moon'] | 27.321582 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 93 | KNOWN_ORBITAL_PERIODS['Io'] | 1.769 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 94 | KNOWN_ORBITAL_PERIODS['Europa'] | 3.551 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 95 | KNOWN_ORBITAL_PERIODS['Ganymede'] | 7.155 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 96 | KNOWN_ORBITAL_PERIODS['Callisto'] | 16.689 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 97 | KNOWN_ORBITAL_PERIODS['Metis'] | 0.295 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 98 | KNOWN_ORBITAL_PERIODS['Adrastea'] | 0.298 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 99 | KNOWN_ORBITAL_PERIODS['Amalthea'] | 0.498 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 100 | KNOWN_ORBITAL_PERIODS['Thebe'] | 0.675 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 103 | KNOWN_ORBITAL_PERIODS['Mimas'] | 0.942 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 104 | KNOWN_ORBITAL_PERIODS['Enceladus'] | 1.37 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 105 | KNOWN_ORBITAL_PERIODS['Tethys'] | 1.888 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 106 | KNOWN_ORBITAL_PERIODS['Dione'] | 2.737 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 107 | KNOWN_ORBITAL_PERIODS['Rhea'] | 4.518 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 108 | KNOWN_ORBITAL_PERIODS['Titan'] | 15.945 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 109 | KNOWN_ORBITAL_PERIODS['Hyperion'] | 21.277 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 110 | KNOWN_ORBITAL_PERIODS['Iapetus'] | 79.331 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 111 | KNOWN_ORBITAL_PERIODS['Phoebe'] | 550.56 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 112 | KNOWN_ORBITAL_PERIODS['Pan'] | 0.575 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 113 | KNOWN_ORBITAL_PERIODS['Daphnis'] | 0.594 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 114 | KNOWN_ORBITAL_PERIODS['Atlas'] | 0.602 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 115 | KNOWN_ORBITAL_PERIODS['Prometheus'] | 0.616 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 116 | KNOWN_ORBITAL_PERIODS['Pandora'] | 0.631 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 117 | KNOWN_ORBITAL_PERIODS['Epimetheus'] | 0.694 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 118 | KNOWN_ORBITAL_PERIODS['Janus'] | 0.695 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 121 | KNOWN_ORBITAL_PERIODS['Miranda'] | 1.413 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 122 | KNOWN_ORBITAL_PERIODS['Ariel'] | 2.52 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 123 | KNOWN_ORBITAL_PERIODS['Umbriel'] | 4.144 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 124 | KNOWN_ORBITAL_PERIODS['Titania'] | 8.706 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 125 | KNOWN_ORBITAL_PERIODS['Oberon'] | 13.463 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 126 | KNOWN_ORBITAL_PERIODS['Puck'] | 0.762 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 127 | KNOWN_ORBITAL_PERIODS['Portia'] | 0.513 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 128 | KNOWN_ORBITAL_PERIODS['Mab'] | 0.923 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 131 | KNOWN_ORBITAL_PERIODS['Triton'] | 5.877 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 132 | KNOWN_ORBITAL_PERIODS['Despina'] | 0.335 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 133 | KNOWN_ORBITAL_PERIODS['Galatea'] | 0.429 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 134 | KNOWN_ORBITAL_PERIODS['Proteus'] | 1.122 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 135 | KNOWN_ORBITAL_PERIODS['Larissa'] | 0.555 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 136 | KNOWN_ORBITAL_PERIODS['Naiad'] | 0.294 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 139 | KNOWN_ORBITAL_PERIODS['Charon'] | 6.387 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 140 | KNOWN_ORBITAL_PERIODS['Styx'] | 20.162 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 141 | KNOWN_ORBITAL_PERIODS['Nix'] | 24.856 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 142 | KNOWN_ORBITAL_PERIODS['Kerberos'] | 32.168 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 143 | KNOWN_ORBITAL_PERIODS['Hydra'] | 38.202 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 146 | KNOWN_ORBITAL_PERIODS['Dysnomia'] | 15.786 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 158 | KNOWN_ORBITAL_PERIODS['Hi'iaka'] | 49.12 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 159 | KNOWN_ORBITAL_PERIODS['Namaka'] | 18.28 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 165 | KNOWN_ORBITAL_PERIODS['Pluto'] | 90560.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 166 | KNOWN_ORBITAL_PERIODS['Ceres'] | 1680.15 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 167 | KNOWN_ORBITAL_PERIODS['Eris'] | 203809.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 168 | KNOWN_ORBITAL_PERIODS['Haumea'] | 103731.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 169 | KNOWN_ORBITAL_PERIODS['Makemake'] | 111766.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 170 | KNOWN_ORBITAL_PERIODS['Quaoar'] | 105192.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 171 | KNOWN_ORBITAL_PERIODS['Orcus'] | 90314.9912925 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 172 | KNOWN_ORBITAL_PERIODS['Ixion'] | 91239.49018 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 173 | KNOWN_ORBITAL_PERIODS['Mani'] | 99305.28767 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 174 | KNOWN_ORBITAL_PERIODS['GV9'] | 100352.0613 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 175 | KNOWN_ORBITAL_PERIODS['Varuna'] | 102799.14 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 176 | KNOWN_ORBITAL_PERIODS['Arrokoth'] | 108224.98 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 177 | KNOWN_ORBITAL_PERIODS['Gonggong'] | 201010.45 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 178 | KNOWN_ORBITAL_PERIODS['2017 OF201'] | 10048413.07 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 181 | KNOWN_ORBITAL_PERIODS['Ammonite'] | 1444383.67 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 182 | KNOWN_ORBITAL_PERIODS['Sedna'] | 4163850.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 183 | KNOWN_ORBITAL_PERIODS['Leleakuhonua'] | 12643548.84594 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 186 | KNOWN_ORBITAL_PERIODS['Chariklo'] | 22996.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 189 | KNOWN_ORBITAL_PERIODS['Vesta'] | 1325.75 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 190 | KNOWN_ORBITAL_PERIODS['Pallas'] | 1685.37 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 191 | KNOWN_ORBITAL_PERIODS['Juno'] | 1591.93 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 192 | KNOWN_ORBITAL_PERIODS['Hygiea'] | 2041.88 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 193 | KNOWN_ORBITAL_PERIODS['Psyche'] | 1825.01 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 194 | KNOWN_ORBITAL_PERIODS['Eros'] | 642.63 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 195 | KNOWN_ORBITAL_PERIODS['Itokawa'] | 556.38 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 196 | KNOWN_ORBITAL_PERIODS['Ryugu'] | 473.98 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 197 | KNOWN_ORBITAL_PERIODS['Bennu'] | 436.65 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 198 | KNOWN_ORBITAL_PERIODS['Apophis'] | 323.6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 199 | KNOWN_ORBITAL_PERIODS['Phaethon'] | 523.42 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 200 | KNOWN_ORBITAL_PERIODS['Dinkinesh'] | 1387.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 201 | KNOWN_ORBITAL_PERIODS['Donaldjohanson'] | 1446.04 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 202 | KNOWN_ORBITAL_PERIODS['Steins'] | 1327.41 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 203 | KNOWN_ORBITAL_PERIODS['Lutetia'] | 1321.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 206 | KNOWN_ORBITAL_PERIODS['Orus'] | 4274.32 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 207 | KNOWN_ORBITAL_PERIODS['Polymele'] | 4319.33 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 208 | KNOWN_ORBITAL_PERIODS['Eurybates'] | 4333.71 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 209 | KNOWN_ORBITAL_PERIODS['Patroclus'] | 4336.36 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 210 | KNOWN_ORBITAL_PERIODS['Menoetius'] | 4336.36 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 211 | KNOWN_ORBITAL_PERIODS['Leucus'] | 4352.24 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 214 | KNOWN_ORBITAL_PERIODS['2024 YR4'] | 922.84 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 215 | KNOWN_ORBITAL_PERIODS['2025 PN7'] | 367.5547275 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 216 | KNOWN_ORBITAL_PERIODS['2024 PT5'] | 368.75 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 217 | KNOWN_ORBITAL_PERIODS['2025 PY1'] | 409.072695 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 218 | KNOWN_ORBITAL_PERIODS['2023 JF'] | 493.37 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 219 | KNOWN_ORBITAL_PERIODS['2025 KV'] | 695.85 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 222 | KNOWN_ORBITAL_PERIODS['Halley'] | 27731.29226 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 223 | KNOWN_ORBITAL_PERIODS['Hyakutake'] | 35773534.62 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 224 | KNOWN_ORBITAL_PERIODS['Hale-Bopp'] | 863279.5035 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 225 | KNOWN_ORBITAL_PERIODS['Ikeya-Seki'] | 319800.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 226 | KNOWN_ORBITAL_PERIODS['ISON'] | 230970.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 227 | KNOWN_ORBITAL_PERIODS['SWAN'] | 8237831.493 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 228 | KNOWN_ORBITAL_PERIODS['6AC4721'] | 311232 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 229 | KNOWN_ORBITAL_PERIODS['MAPS'] | 418226.4926 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 230 | KNOWN_ORBITAL_PERIODS['Lemmon'] | 492252.5179 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 231 | KNOWN_ORBITAL_PERIODS['Schaumasse'] | 3014.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 232 | KNOWN_ORBITAL_PERIODS['Howell'] | 2009.4 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 233 | KNOWN_ORBITAL_PERIODS['Tempel 2'] | 1961.8 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 251 | KNOWN_ORBITAL_PERIODS['Planet 9'] | 3652500.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2543 | 'x' | 0.2 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2544 | 'y' | 5.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2549 | 'x' | 0.66 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2550 | 'y' | 5.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2555 | 'x' | 0.22 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2556 | 'y' | 3.7 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2561 | 'x' | 0.857 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2562 | 'y' | 3.7 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2567 | 'x' | 0.96 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2568 | 'y' | 3.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2573 | 'x' | 0.25 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2574 | 'y' | 2.25 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2579 | 'x' | 0.83 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2580 | 'y' | 2.25 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2585 | 'x' | 0.2 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2586 | 'y' | 1.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2591 | 'x' | 0.75 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2592 | 'y' | 1.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2597 | 'x' | 0.4 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2598 | 'y' | 0.2 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2599 | 'rotation' | 15 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2604 | 'x' | 0.77 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2605 | 'y' | -1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2610 | 'x' | 0.4 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 2611 | 'y' | -4.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 14 modules |
| 26 | claim: 0.2 Solar radii | 0.2 Solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 27 | claim: 0.7 Solar radii | 0.7 Solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 31 | claim: 1.5 solar radii | 1.5 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 32 | claim: 3 solar radii | 3 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 33 | claim: 50 solar radii | 50 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 37 | claim: 123 AU | 123 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 46 | claim: 0.41 AU | 0.41 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 46 | claim: 8.2 solar radii | 8.2 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 68 | claim: 537 km | 537 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 71 | claim: 10 Earth masses | 10 Earth masses | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 93 | claim: 42.456 hours | 42.456 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 94 | claim: 85.224 hours | 85.224 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 95 | claim: 171.72 hours | 171.72 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 96 | claim: 400.536 hours | 400.536 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 97 | claim: 7.08 hours | 7.08 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 98 | claim: 7.15 hours | 7.15 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 99 | claim: 11.95 hours | 11.95 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 100 | claim: 16.20 hours | 16.20 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 103 | claim: 22.61 hours | 22.61 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 104 | claim: 32.88 hours | 32.88 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 105 | claim: 45.31 hours | 45.31 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 106 | claim: 65.69 hours | 65.69 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 107 | claim: 108.43 hours | 108.43 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 108 | claim: 382.68 hours | 382.68 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 109 | claim: 510.65 hours | 510.65 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 110 | claim: 1903.94 hours | 1903.94 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 111 | claim: 1.51 years | 1.51 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 112 | claim: 13.80 hours | 13.80 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 113 | claim: 14.26 hours | 14.26 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 114 | claim: 14.45 hours | 14.45 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 115 | claim: 14.78 hours | 14.78 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 116 | claim: 15.14 hours | 15.14 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 117 | claim: 16.66 hours | 16.66 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 118 | claim: 16.68 hours | 16.68 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 121 | claim: 33.91 hours | 33.91 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 122 | claim: 60.48 hours | 60.48 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 123 | claim: 99.46 hours | 99.46 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 124 | claim: 208.94 hours | 208.94 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 125 | claim: 323.11 hours | 323.11 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 126 | claim: 18.29 hours | 18.29 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 127 | claim: 12.31 hours | 12.31 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 128 | claim: 22.15 hours | 22.15 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 131 | claim: 141.05 hours | 141.05 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 132 | claim: 8.04 hours | 8.04 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 133 | claim: 10.30 hours | 10.30 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 134 | claim: 26.93 hours | 26.93 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 135 | claim: 13.32 hours | 13.32 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 136 | claim: 7.06 hours | 7.06 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 139 | claim: 153.29 hours | 153.29 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 140 | claim: 483.89 hours | 483.89 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 141 | claim: 596.54 hours | 596.54 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 142 | claim: 772.03 hours | 772.03 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 143 | claim: 916.85 hours | 916.85 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 146 | claim: 378.86 hours | 378.86 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 158 | claim: 49 days | 49 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 159 | claim: 18 days | 18 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 186 | claim: 22996.00121 days | 22996.00121 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 228 | claim: 852.1 years | 852.1 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 229 | claim: 1145.041732 years | 1145.041732 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 231 | claim: 8.252 years | 8.252 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 231 | claim: 3014.1 days | 3014.1 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 232 | claim: 5.5 years | 5.5 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 232 | claim: 2009.375 days | 2009.375 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 233 | claim: 5.37 years | 5.37 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 233 | claim: 1961.4 days | 1961.4 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 423 | claim: 100 light-years | 100 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 428 | claim: 650 km | 650 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 438 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 475 | claim: 6000 K | 6000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 676 | claim: 0.2 AU | 0.2 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 678 | claim: 0.002 AU | 0.002 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 683 | claim: 0.01 AU | 0.01 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 689 | claim: 0.02 AU | 0.02 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 693 | claim: 5.145 deg | 5.145 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 694 | claim: 28.545 deg | 28.545 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 694 | claim: 23.4 deg | 23.4 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 731 | claim: 003 AU | 003 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 735 | claim: 670 km | 670 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 736 | claim: 700 km | 700 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 737 | claim: 670 km | 670 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 737 | claim: 0.0000312 AU | 0.0000312 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 738 | claim: 730 km | 730 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 738 | claim: 0.00254 AU | 0.00254 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 739 | claim: 27.32 days | 27.32 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 782 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 813 | claim: 322 km | 322 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 814 | claim: 400 km | 400 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 815 | claim: 092 km | 092 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 827 | claim: 0.851 AU | 0.851 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 827 | claim: 4.181 AU | 4.181 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 828 | claim: 2.53 years | 2.53 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 833 | claim: 0.851 AU | 0.851 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 836 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 838 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 841 | claim: 487 km | 487 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 842 | claim: 945 km | 945 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 855 | claim: 0.741 AU | 0.741 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 855 | claim: 4.101 AU | 4.101 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 879 | claim: 345000 km | 345000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 879 | claim: 327000 km | 327000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 880 | claim: 61400 km | 61400 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 880 | claim: 58100 km | 58100 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 887 | claim: 475000 km | 475000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 888 | claim: 449600 km | 449600 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 889 | claim: 68300 km | 68300 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 889 | claim: 64600 km | 64600 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 903 | claim: 60 degrees | 60 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 904 | claim: 407000 km | 407000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 904 | claim: 385000 km | 385000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 911 | claim: 60 degrees | 60 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 912 | claim: 407000 km | 407000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 912 | claim: 385000 km | 385000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 948 | claim: 180 degrees | 180 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 976 | claim: 60 degrees | 60 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 976 | claim: 1 au | 1 au | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 989 | claim: 60 degrees | 60 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 990 | claim: 1 AU | 1 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 999 | claim: 0.01 AU | 0.01 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1012 | claim: 0.005 AU | 0.005 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1016 | claim: 1.0 AU | 1.0 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1017 | claim: 0.746 AU | 0.746 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1018 | claim: 1.099 AU | 1.099 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1018 | claim: 323.6 days | 323.6 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1019 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1022 | claim: 100 years | 100 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1024 | claim: 600 km | 600 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1025 | claim: 200 km | 200 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1040 | claim: 4.3 hours | 4.3 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1064 | claim: 8.2 km | 8.2 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1066 | claim: 1.133 AU | 1.133 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1066 | claim: 1.783 AU | 1.783 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1090 | claim: 52.7 hours | 52.7 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1095 | claim: 4 km | 4 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1099 | claim: 64 km | 64 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1099 | claim: 1 km | 1 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1101 | claim: 0.000005 AU | 0.000005 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1104 | claim: 0.000005 AU | 0.000005 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1109 | claim: 0.000005 AU | 0.000005 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1115 | claim: 40 km | 40 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1115 | claim: 446 hours | 446 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1118 | claim: 51 km | 51 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1121 | claim: 34 km | 34 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1126 | claim: 0.5 AU | 0.5 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1143 | claim: 0.5 AU | 0.5 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1202 | claim: 1 AU | 1 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1214 | claim: 0005 AU | 0005 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1217 | claim: 0005 AU | 0005 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1218 | claim: 0.1 AU | 0.1 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1222 | claim: 248 years | 248 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1223 | claim: 49 AU | 49 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1224 | claim: 30 AU | 30 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1225 | claim: 180 deg | 180 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1238 | claim: 035 km | 035 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1238 | claim: 188 km | 188 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1239 | claim: 100 km | 100 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1240 | claim: 500 km | 500 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1240 | claim: 6.387 days | 6.387 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1245 | claim: 0005 AU | 0005 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1247 | claim: 6.387 days | 6.387 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1247 | claim: 596 km | 596 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1249 | claim: 0005 AU | 0005 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1252 | claim: 0005 AU | 0005 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1255 | claim: 0005 AU | 0005 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1258 | claim: 0005 AU | 0005 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1262 | claim: 0.0006 AU | 0.0006 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1263 | claim: 0.000002 AU | 0.000002 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1267 | claim: 0.0006 AU | 0.0006 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1268 | claim: 49 days | 49 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1268 | claim: 310 km | 310 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1270 | claim: 0.0006 AU | 0.0006 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1271 | claim: 18 days | 18 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1271 | claim: 170 km | 170 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1274 | claim: 18.0 days | 18.0 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1274 | claim: 250 km | 250 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1275 | claim: 175 km | 175 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1278 | claim: 0.0003 AU | 0.0003 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1281 | claim: 0.0003 AU | 0.0003 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1284 | claim: 0.1 AU | 0.1 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1290 | claim: 0.0003 AU | 0.0003 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1291 | claim: 15.79 days | 15.79 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1291 | claim: 700 km | 700 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1293 | claim: 0.0002 AU | 0.0002 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1295 | claim: 1090 km | 1090 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1298 | claim: 286 years | 286 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1301 | claim: 0.0002 AU | 0.0002 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1304 | claim: 12.4 days | 12.4 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1304 | claim: 300 km | 300 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1304 | claim: 170 km | 170 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1311 | claim: 250.07 AU | 250.07 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1312 | claim: 65.76 AU | 65.76 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1312 | claim: 434.37 AU | 434.37 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1314 | claim: 10.99 degrees | 10.99 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1332 | claim: 76 AU | 76 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1332 | claim: 500 AU | 500 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1333 | claim: 80 AU | 80 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1334 | claim: 260 AU | 260 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1341 | claim: 526 AU | 526 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1342 | claim: 76 AU | 76 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1343 | claim: 936 AU | 936 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1347 | claim: 400 years | 400 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1351 | claim: 83.3 AU | 83.3 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1354 | claim: 2000 AU | 2000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1355 | claim: 090 AU | 090 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1375 | claim: 00008 AU | 00008 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1376 | claim: 1500 AU | 1500 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1379 | claim: 180 deg | 180 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1381 | claim: 48 AU | 48 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1381 | claim: 30 AU | 30 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1382 | claim: 247 years | 247 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1385 | claim: 230 km | 230 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1393 | claim: 910 km | 910 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1397 | claim: 00008 AU | 00008 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1401 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1402 | claim: 770 km | 770 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1403 | claim: 230 km | 230 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1404 | claim: 9.54 days | 9.54 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1406 | claim: 90 deg | 90 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1413 | claim: 443 km | 443 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1415 | claim: 00008 AU | 00008 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1419 | claim: 230 km | 230 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1420 | claim: 230 km | 230 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1421 | claim: 770 km | 770 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1422 | claim: 9.54 days | 9.54 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1423 | claim: 90 deg | 90 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1432 | claim: 1500 AU | 1500 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1442 | claim: 0.0003 AU | 0.0003 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1444 | claim: 0.0003 AU | 0.0003 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1445 | claim: 1230 km | 1230 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1445 | claim: 30.9 deg | 30.9 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1448 | claim: 22 hours | 22 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1449 | claim: 52.7 AU | 52.7 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1449 | claim: 550 years | 550 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1451 | claim: 0.0003 AU | 0.0003 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1454 | claim: 25.22 days | 25.22 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1454 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1454 | claim: 100 km | 100 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1455 | claim: 83 deg | 83 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1459 | claim: 17 Earth masses | 17 Earth masses | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1459 | claim: 700 AU | 700 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1460 | claim: 23 years | 23 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1461 | claim: 1120 AU | 1120 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1465 | claim: 23 years | 23 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1466 | claim: 8 AU | 8 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1467 | claim: 800 AU | 800 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1472 | claim: 800 AU | 800 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1475 | claim: 170 AU | 170 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1478 | claim: 165.2 AU | 165.2 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1491 | claim: 150 AU | 150 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1494 | claim: 15 AU | 15 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1501 | claim: 13 years | 13 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1511 | claim: 70 AU | 70 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1512 | claim: 0.0003 AU | 0.0003 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1518 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1519 | claim: 6 km | 6 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1523 | claim: 3537.7 km | 3537.7 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1530 | claim: 70 AU | 70 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1531 | claim: 0.0003 AU | 0.0003 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1532 | claim: 0.00003 AU | 0.00003 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1539 | claim: 36 km | 36 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1553 | claim: 3537.7 km | 3537.7 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1584 | claim: 6 AU | 6 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1588 | claim: 0.01 AU | 0.01 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1608 | claim: 2.5 hours | 2.5 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1635 | claim: 21.5 hours | 21.5 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1644 | claim: 2.5 days | 2.5 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1646 | claim: 2660 km | 2660 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1647 | claim: 24 km | 24 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1649 | claim: 140 AU | 140 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1654 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1658 | claim: 116 AU | 116 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1661 | claim: 5 AU | 5 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1677 | claim: 7.5 hours | 7.5 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1680 | claim: 3.5 years | 3.5 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1705 | claim: 2 AU | 2 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1706 | claim: 0.00003 AU | 0.00003 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1714 | claim: 592 km | 592 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1728 | claim: 0.0000000026 AU | 0.0000000026 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1742 | claim: 2 AU | 2 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1783 | claim: 0.00465 AU | 0.00465 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1784 | claim: 3 solar radii | 3 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1784 | claim: 0.01 AU | 0.01 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1785 | claim: 8.8 solar radii | 8.8 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1785 | claim: 0.041 AU | 0.041 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1786 | claim: 50 solar radii | 50 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1786 | claim: 0.2 AU | 0.2 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1787 | claim: 0.387 AU | 0.387 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1788 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1794 | claim: 8.8 solar radii | 8.8 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1795 | claim: 12 hours | 12 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1799 | claim: 6 AU | 6 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1829 | claim: 1.5 AU | 1.5 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1853 | claim: 0.00001829 AU | 0.00001829 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1853 | claim: 0.00001829 AU | 0.00001829 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1853 | claim: 736 km | 736 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1878 | claim: 1.5 AU | 1.5 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1881 | claim: 1.5 AU | 1.5 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1885 | claim: 0.28 au | 0.28 au | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1885 | claim: 60 solar radii | 60 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1885 | claim: 1.2 au | 1.2 au | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1926 | claim: 3396.19 km | 3396.19 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1928 | claim: 45.0 km | 45.0 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1968 | claim: 32 minutes | 32 minutes | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2008 | claim: 4.5 years | 4.5 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2012 | claim: 0.003 AU | 0.003 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2021 | claim: 000 kg | 000 kg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2021 | claim: 400 kg | 400 kg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2022 | claim: 000 kg | 000 kg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2024 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2024 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2033 | claim: 185 km | 185 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2034 | claim: 377 km | 377 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2054 | claim: 171 km | 171 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2063 | claim: 122 km | 122 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2063 | claim: 10.8 km | 10.8 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2064 | claim: 11 km | 11 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2065 | claim: 7.6 km | 7.6 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2066 | claim: 2.9 km | 2.9 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2074 | claim: 5 hours | 5 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2077 | claim: 14 hours | 14 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2079 | claim: 53 years | 53 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2088 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2093 | claim: 880 years | 880 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2123 | claim: 76 years | 76 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2127 | claim: 74.42 years | 74.42 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2127 | claim: 79.25 years | 79.25 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2132 | claim: 18 degrees | 18 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2151 | claim: 0.42 AU | 0.42 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2170 | claim: 0.09 AU | 0.09 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2175 | claim: 360 AU | 360 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2179 | claim: 40 AU | 40 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2189 | claim: 0.33 AU | 0.33 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2191 | claim: 0.40 AU | 0.40 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2193 | claim: 147.864867556013 degrees | 147.864867556013 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2194 | claim: 8 days | 8 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2194 | claim: 0.33 AU | 0.33 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2210 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2214 | claim: 8 days | 8 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2214 | claim: 0.33 AU | 0.33 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2235 | claim: 33 days | 33 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2236 | claim: 0.336 AU | 0.336 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2244 | claim: 50 AU | 50 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2257 | claim: 0.39 AU | 0.39 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2258 | claim: 25 years | 25 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2260 | claim: 0.47 AU | 0.47 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2268 | claim: 4.1 km | 4.1 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2272 | claim: 6.44 years | 6.44 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2273 | claim: 6.44 years | 6.44 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2274 | claim: 3.22 years | 3.22 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2312 | claim: 68 km | 68 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2330 | claim: 5 AU | 5 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2335 | claim: 200 years | 200 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2338 | claim: 0.09 AU | 0.09 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2349 | claim: 1500 AU | 1500 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2353 | claim: 2 degrees | 2 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2356 | claim: 0.26 AU | 0.26 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2364 | claim: 1500 AU | 1500 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2367 | claim: 2 degrees | 2 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2370 | claim: 0.26 AU | 0.26 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2376 | claim: 200 AU | 200 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2387 | claim: 200 AU | 200 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2391 | claim: 81 days | 81 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2400 | claim: 100 AU | 100 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2406 | claim: 33 R_sun | 33 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2406 | claim: 0.153 AU | 0.153 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2408 | claim: 18.8 R_sun | 18.8 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2408 | claim: 0.087 AU | 0.087 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2411 | claim: 8.33 R_sun | 8.33 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2411 | claim: 0.039 AU | 0.039 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2416 | claim: 1.23 R_sun | 1.23 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2417 | claim: 0.006 AU | 0.006 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2417 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2417 | claim: 556 km | 556 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2418 | claim: 6 R_sun | 6 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2418 | claim: 0.028 AU | 0.028 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2418 | claim: 3.45 R_sun | 3.45 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2418 | claim: 0.016 AU | 0.016 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2419 | claim: 3.0 R_sun | 3.0 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2419 | claim: 0.014 AU | 0.014 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2422 | claim: 40 hours | 40 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2423 | claim: 28 R_sun | 28 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2423 | claim: 0.132 AU | 0.132 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2425 | claim: 1.23 solar radii | 1.23 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2426 | claim: 8.8 R_sun | 8.8 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2426 | claim: 0.041 AU | 0.041 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2426 | claim: 8.33 R_sun | 8.33 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2427 | claim: 0.039 AU | 0.039 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2432 | claim: 250 AU | 250 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2451 | claim: 0.56 AU | 0.56 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2451 | claim: 0.19 AU | 0.19 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2455 | claim: 0.566 AU | 0.566 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2456 | claim: 1.01 AU | 1.01 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2460 | claim: 7 AU | 7 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2475 | claim: 9 km | 9 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2478 | claim: 40.5 ly | 40.5 ly | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2479 | claim: 1.5 day | 1.5 day | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2479 | claim: 400 K | 400 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2480 | claim: 2.4 day | 2.4 day | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2481 | claim: 4.0 day | 4.0 day | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2482 | claim: 6.1 days | 6.1 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2483 | claim: 9.2 day | 9.2 day | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2484 | claim: 12.4 day | 12.4 day | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2485 | claim: 18.8 day | 18.8 day | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2485 | claim: 173 K | 173 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2489 | claim: 292 ly | 292 ly | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2490 | claim: 0.35 AU | 0.35 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2493 | claim: 14.6 days | 14.6 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2500 | claim: 14.6 days | 14.6 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2501 | claim: 19.95 deg | 19.95 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2507 | claim: 0.461 AU | 0.461 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2508 | claim: 0.76 AU | 0.76 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2509 | claim: 0.352 AU | 0.352 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2516 | claim: 11.3 Earth masses | 11.3 Earth masses | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2519 | claim: 95.2 days | 95.2 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2520 | claim: 0.461 AU | 0.461 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2526 | claim: 75.4 Earth masses | 75.4 Earth masses | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2529 | claim: 215.5 days | 215.5 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2530 | claim: 0.794 AU | 0.794 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2533 | claim: 4.24 ly | 4.24 ly | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2534 | claim: 11.2 day | 11.2 day | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 2535 | claim: 5.1 days | 5.1 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |

### earth_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 26 | claim: 220 km | 220 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 42 | claim: 220 km | 220 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 81 | claim: 500 km | 500 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 97 | claim: 500 km | 500 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 136 | claim: 900 km | 900 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 151 | claim: 900 km | 900 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 190 | claim: 660 km | 660 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 205 | claim: 660 km | 660 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 243 | claim: 10 km | 10 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 243 | claim: 50 km | 50 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 260 | claim: 10 km | 10 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 260 | claim: 50 km | 50 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 399 | claim: 12 km | 12 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 400 | claim: 50 km | 50 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 414 | claim: 12 km | 12 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 415 | claim: 50 km | 50 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 453 | claim: 50 km | 50 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 453 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 469 | claim: 50 km | 50 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 469 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 516 | claim: 0.01 AU | 0.01 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 518 | claim: 10 Earth radii | 10 Earth radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 523 | claim: 15 Earth radii | 15 Earth radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 527 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 527 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 529 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 529 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 571 | claim: 10 Earth radii | 10 Earth radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 627 | claim: 15 Earth radii | 15 Earth radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 657 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 657 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 659 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 659 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 733 | claim: 0.003 AU | 0.003 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 734 | claim: 200 km | 200 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 734 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 735 | claim: 1.31 Earth radii | 1.31 Earth radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 738 | claim: 120 minutes | 120 minutes | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 738 | claim: 6 minutes | 6 minutes | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 740 | claim: 400 km | 400 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 740 | claim: 51.6 deg | 51.6 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 741 | claim: 550 km | 550 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 742 | claim: 540 km | 540 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 748 | claim: 786 km | 786 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 756 | claim: 200 km | 200 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 756 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 756 | claim: 1.31 Earth radii | 1.31 Earth radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 759 | claim: 550 km | 550 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 774 | claim: 200 km | 200 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 775 | claim: 2000 km | 2000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 776 | claim: 550 km | 550 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 792 | claim: 150 km | 150 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 804 | claim: 200 km | 200 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 804 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 805 | claim: 571 km | 571 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 805 | claim: 371 km | 371 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 805 | claim: 1.31 Earth radii | 1.31 Earth radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 807 | claim: 120 minutes | 120 minutes | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 807 | claim: 6 minutes | 6 minutes | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 809 | claim: 550 km | 550 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 809 | claim: 400 km | 400 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 809 | claim: 540 km | 540 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 812 | claim: 164 km | 164 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 837 | claim: 0.003 AU | 0.003 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 838 | claim: 164 km | 164 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 839 | claim: 786 km | 786 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 852 | claim: 164 km | 164 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 857 | claim: 0.1 deg | 0.1 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 861 | claim: 164 km | 164 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 861 | claim: 6.62 Earth radii | 6.62 Earth radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 862 | claim: 786 km | 786 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 863 | claim: 013 km | 013 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 863 | claim: 151 km | 151 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 877 | claim: 0.1 deg | 0.1 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 888 | claim: 0.0002 AU | 0.0002 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 888 | claim: 30 km | 30 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 892 | claim: 0.1 deg | 0.1 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 893 | claim: 0.05 Earth radii | 0.05 Earth radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 902 | claim: 786 km | 786 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 903 | claim: 164 km | 164 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 903 | claim: 6.62 Earth radii | 6.62 Earth radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 907 | claim: 013 km | 013 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 908 | claim: 150 km | 150 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 934 | claim: 0.02 AU | 0.02 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 935 | claim: 235 Earth radii | 235 Earth radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 941 | claim: 235 Earth radii | 235 Earth radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 957 | claim: 235 Earth radii | 235 Earth radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |

### eris_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 33 | claim: 875 K | 875 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 62 | claim: 875 K | 875 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 156 | claim: 0.005 AU | 0.005 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 401 | claim: 0.1 AU | 0.1 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 419 | claim: 0.05 AU | 0.05 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |

### exoplanet_stellar_properties.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 563 | trappist1_star['mass_solar'] | 0.0898 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 564 | trappist1_star['radius_solar'] | 0.1192 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 565 | trappist1_star['teff_k'] | 2566 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 566 | trappist1_star['luminosity_solar'] | 0.000525 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 567 | trappist1_star['distance_pc'] | 12.43 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 585 | proxima_star['mass_solar'] | 0.1221 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 586 | proxima_star['radius_solar'] | 0.1542 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 587 | proxima_star['teff_k'] | 3042 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 588 | proxima_star['distance_pc'] | 1.3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |

### exoplanet_systems.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 41 | TRAPPIST1_SYSTEM['discovery_year'] | 2017 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 42 | TRAPPIST1_SYSTEM['distance_pc'] | 12.43 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 43 | TRAPPIST1_SYSTEM['distance_ly'] | 40.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 55 | 'is_binary' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 58 | 'ra' | 346.62201667 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 59 | 'dec' | -5.04138889 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 60 | 'distance_pc' | 12.43 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 63 | 'pmra' | 922.88 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 64 | 'pmdec' | -469.24 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 69 | 'mass_solar' | 0.0898 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 70 | 'radius_solar' | 0.1192 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 71 | 'teff_k' | 2566 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 72 | 'luminosity_solar' | 0.000525 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 73 | 'age_gyr' | 7.6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 76 | 'habitable_zone_inner_au' | 0.025 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 77 | 'habitable_zone_outer_au' | 0.05 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 91 | 'period_days' | 1.51087081 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 92 | 'semi_major_axis_au' | 0.01154 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 93 | 'eccentricity' | 0.00622 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 94 | 'inclination_deg' | 89.728 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 95 | 'omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 96 | 'Omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 100 | 'mass_earth' | 1.374 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 101 | 'radius_earth' | 1.116 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 102 | 'density_earth' | 0.98 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 103 | 'equilibrium_temp_k' | 400 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 104 | 'insolation_earth' | 4.25 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 108 | 'discovery_year' | 2016 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 110 | 'in_habitable_zone' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 113 | 'e_assumed' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 114 | 'i_assumed' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 115 | 'omega_assumed' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 126 | 'period_days' | 2.42182151 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 127 | 'semi_major_axis_au' | 0.0158 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 128 | 'eccentricity' | 0.00654 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 129 | 'inclination_deg' | 89.778 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 130 | 'omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 131 | 'Omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 134 | 'mass_earth' | 1.308 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 135 | 'radius_earth' | 1.097 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 136 | 'density_earth' | 1.05 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 137 | 'equilibrium_temp_k' | 342 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 138 | 'insolation_earth' | 2.27 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 141 | 'discovery_year' | 2016 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 143 | 'in_habitable_zone' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 145 | 'e_assumed' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 146 | 'i_assumed' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 147 | 'omega_assumed' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 158 | 'period_days' | 4.04961 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 159 | 'semi_major_axis_au' | 0.02227 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 160 | 'eccentricity' | 0.00837 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 161 | 'inclination_deg' | 89.896 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 162 | 'omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 163 | 'Omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 166 | 'mass_earth' | 0.388 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 167 | 'radius_earth' | 0.788 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 168 | 'density_earth' | 0.72 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 169 | 'equilibrium_temp_k' | 288 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 170 | 'insolation_earth' | 1.15 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 173 | 'discovery_year' | 2016 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 175 | 'in_habitable_zone' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 177 | 'e_assumed' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 178 | 'i_assumed' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 179 | 'omega_assumed' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 190 | 'period_days' | 6.09965 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 191 | 'semi_major_axis_au' | 0.02925 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 192 | 'eccentricity' | 0.0051 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 193 | 'inclination_deg' | 89.793 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 194 | 'omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 195 | 'Omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 198 | 'mass_earth' | 0.692 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 199 | 'radius_earth' | 0.92 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 200 | 'density_earth' | 0.93 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 201 | 'equilibrium_temp_k' | 251 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 202 | 'insolation_earth' | 0.66 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 205 | 'discovery_year' | 2017 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 207 | 'in_habitable_zone' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 209 | 'e_assumed' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 210 | 'i_assumed' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 211 | 'omega_assumed' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 222 | 'period_days' | 9.20669 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 223 | 'semi_major_axis_au' | 0.03849 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 224 | 'eccentricity' | 0.01007 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 225 | 'inclination_deg' | 89.74 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 226 | 'omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 227 | 'Omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 230 | 'mass_earth' | 1.039 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 231 | 'radius_earth' | 1.045 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 232 | 'density_earth' | 0.93 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 233 | 'equilibrium_temp_k' | 219 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 234 | 'insolation_earth' | 0.38 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 237 | 'discovery_year' | 2017 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 239 | 'in_habitable_zone' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 241 | 'e_assumed' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 242 | 'i_assumed' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 243 | 'omega_assumed' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 254 | 'period_days' | 12.35294 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 255 | 'semi_major_axis_au' | 0.04683 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 256 | 'eccentricity' | 0.00208 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 257 | 'inclination_deg' | 89.721 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 258 | 'omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 259 | 'Omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 262 | 'mass_earth' | 1.321 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 263 | 'radius_earth' | 1.129 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 264 | 'density_earth' | 0.92 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 265 | 'equilibrium_temp_k' | 199 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 266 | 'insolation_earth' | 0.26 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 269 | 'discovery_year' | 2017 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 271 | 'in_habitable_zone' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 273 | 'e_assumed' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 274 | 'i_assumed' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 275 | 'omega_assumed' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 286 | 'period_days' | 18.76712 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 287 | 'semi_major_axis_au' | 0.06189 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 288 | 'eccentricity' | 0.00567 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 289 | 'inclination_deg' | 89.796 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 290 | 'omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 291 | 'Omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 294 | 'mass_earth' | 0.326 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 295 | 'radius_earth' | 0.755 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 296 | 'density_earth' | 0.66 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 297 | 'equilibrium_temp_k' | 173 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 298 | 'insolation_earth' | 0.16 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 301 | 'discovery_year' | 2017 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 303 | 'in_habitable_zone' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 305 | 'e_assumed' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 306 | 'i_assumed' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 307 | 'omega_assumed' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 327 | TOI1338_SYSTEM['discovery_year'] | 2020 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 328 | TOI1338_SYSTEM['distance_pc'] | 396 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 329 | TOI1338_SYSTEM['distance_ly'] | 1292 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 342 | 'is_binary' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 345 | 'ra' | 56.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 346 | 'dec' | -59.8 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 347 | 'distance_pc' | 396 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 350 | 'pmra' | 5.2 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 351 | 'pmdec' | -2.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 355 | 'binary_period_days' | 14.6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 356 | 'binary_separation_au' | 0.088 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 357 | 'binary_eccentricity' | 0.16 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 358 | 'binary_inclination_deg' | 89.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 359 | 'binary_Omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 366 | 'mass_solar' | 1.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 367 | 'radius_solar' | 1.44 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 368 | 'teff_k' | 6100 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 369 | 'luminosity_solar' | 2.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 377 | 'mass_solar' | 0.3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 378 | 'radius_solar' | 0.29 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 379 | 'teff_k' | 3450 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 380 | 'luminosity_solar' | 0.015 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 384 | 'total_mass_solar' | 1.4 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 385 | 'combined_luminosity_solar' | 2.015 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 388 | 'habitable_zone_inner_au' | 1.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 389 | 'habitable_zone_outer_au' | 1.6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 403 | 'period_days' | 95.196 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 404 | 'semi_major_axis_au' | 0.4607 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 405 | 'eccentricity' | 0.09 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 406 | 'inclination_deg' | 89.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 407 | 'omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 408 | 'Omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 412 | 'mass_jupiter' | 0.107 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 413 | 'mass_earth' | 22.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 414 | 'radius_jupiter' | 0.635 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 415 | 'radius_earth' | 6.9 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 416 | 'density_earth' | 0.15 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 417 | 'equilibrium_temp_k' | 250 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 418 | 'insolation_earth' | 0.22 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 422 | 'discovery_year' | 2020 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 425 | 'in_habitable_zone' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 428 | 'e_assumed' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 429 | 'i_assumed' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 430 | 'omega_assumed' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 442 | 'period_days' | 215.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 443 | 'semi_major_axis_au' | 0.76 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 444 | 'eccentricity' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 445 | 'inclination_deg' | 89.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 446 | 'omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 447 | 'Omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 451 | 'mass_earth' | 65.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 452 | 'radius_earth' | 11.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 453 | 'density_earth' | 0.2 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 454 | 'equilibrium_temp_k' | 180 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 455 | 'insolation_earth' | 0.08 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 459 | 'discovery_year' | 2023 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 461 | 'in_habitable_zone' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 464 | 'e_assumed' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 465 | 'i_assumed' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 466 | 'omega_assumed' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 486 | PROXIMA_SYSTEM['discovery_year'] | 2016 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 487 | PROXIMA_SYSTEM['distance_pc'] | 1.3012 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 488 | PROXIMA_SYSTEM['distance_ly'] | 4.244 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 501 | 'is_binary' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 504 | 'ra' | 217.42894167 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 505 | 'dec' | -62.67948333 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 506 | 'distance_pc' | 1.3012 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 509 | 'pmra' | 3853.92 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 510 | 'pmdec' | -768.34 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 515 | 'mass_solar' | 0.1221 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 516 | 'radius_solar' | 0.1542 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 517 | 'teff_k' | 3042 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 518 | 'luminosity_solar' | 0.00155 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 519 | 'age_gyr' | 4.85 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 522 | 'habitable_zone_inner_au' | 0.023 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 523 | 'habitable_zone_outer_au' | 0.054 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 537 | 'period_days' | 11.18427 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 538 | 'semi_major_axis_au' | 0.04856 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 539 | 'eccentricity' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 540 | 'inclination_deg' | 60.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 541 | 'omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 542 | 'Omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 546 | 'mass_earth' | 1.27 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 547 | 'radius_earth' | 1.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 548 | 'density_earth' | 1.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 549 | 'equilibrium_temp_k' | 234 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 550 | 'insolation_earth' | 0.65 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 554 | 'discovery_year' | 2016 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 556 | 'in_habitable_zone' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 559 | 'e_assumed' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 560 | 'i_assumed' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 561 | 'omega_assumed' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 573 | 'period_days' | 5.122 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 574 | 'semi_major_axis_au' | 0.029 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 575 | 'eccentricity' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 576 | 'inclination_deg' | 60.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 577 | 'omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 578 | 'Omega_deg' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 582 | 'mass_earth' | 0.26 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 583 | 'radius_earth' | 0.81 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 584 | 'density_earth' | 0.9 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 585 | 'equilibrium_temp_k' | 330 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 586 | 'insolation_earth' | 1.9 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 590 | 'discovery_year' | 2022 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 592 | 'in_habitable_zone' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 595 | 'e_assumed' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 596 | 'i_assumed' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 597 | 'omega_assumed' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 33 | claim: 12.43 pc | 12.43 pc | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 59 | claim: 05 deg | 05 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 70 | claim: 0.0013 solar radii | 0.0013 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 71 | claim: 26 K | 26 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 320 | claim: 396 pc | 396 pc | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 412 | claim: 22 Earth masses | 22 Earth masses | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 478 | claim: 1.30 pc | 1.30 pc | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 478 | claim: 4.24 ly | 4.24 ly | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 505 | claim: 62 deg | 62 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |

### idealized_orbits.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 51 | 'ra' | 317.68 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 51 | 'dec' | 52.89 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 52 | 'ra' | 268.05 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 52 | 'dec' | 64.49 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 53 | 'ra' | 40.58 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 53 | 'dec' | 83.54 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 54 | 'ra' | 257.43 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 54 | 'dec' | -15.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 55 | 'ra' | 299.36 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 55 | 'dec' | 43.46 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 56 | 'ra' | 132.99 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 56 | 'dec' | -6.16 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 1711 | BINARY_PARAMS['separation_au'] | 0.000131 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 1712 | BINARY_PARAMS['period_days'] | 6.387 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 1713 | BINARY_PARAMS['mass_ratio'] | 0.122 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 1714 | BINARY_PARAMS['eccentricity'] | 0.0002 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 1716 | BINARY_PARAMS['inclination_ecliptic'] | 119.6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 1717 | BINARY_PARAMS['Omega_ecliptic'] | 223.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 1718 | BINARY_PARAMS['omega'] | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2483 | BINARY_PARAMS['separation_au'] | 6.01e-05 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2484 | BINARY_PARAMS['period_days'] | 9.54 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2485 | BINARY_PARAMS['mass_ratio'] | 0.16 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2486 | BINARY_PARAMS['eccentricity'] | 0.007 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2489 | BINARY_PARAMS['inclination_ecliptic'] | 83.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2490 | BINARY_PARAMS['Omega_ecliptic'] | 216.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2492 | BINARY_PARAMS['omega'] | 65.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2764 | BINARY_PARAMS['separation_km'] | 24021 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2765 | BINARY_PARAMS['separation_au'] | 0.0001606 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2766 | BINARY_PARAMS['period_days'] | 25.22 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2767 | BINARY_PARAMS['eccentricity'] | 0.29 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2768 | BINARY_PARAMS['inclination_ecliptic'] | 83.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2769 | BINARY_PARAMS['Omega_ecliptic'] | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2770 | BINARY_PARAMS['omega'] | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2962 | BINARY_PARAMS['separation_km'] | 692.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2964 | BINARY_PARAMS['period_days'] | 4.28268 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2965 | BINARY_PARAMS['mass_fraction_patroclus'] | 0.7798 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2966 | BINARY_PARAMS['mass_fraction_menoetius'] | 0.2202 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2967 | BINARY_PARAMS['eccentricity'] | 0.004 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2969 | BINARY_PARAMS['inclination_ecliptic'] | 152.53 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2970 | BINARY_PARAMS['Omega_ecliptic'] | 324.12 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2971 | BINARY_PARAMS['omega'] | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2977 | PHASE_REFERENCE['jd_epoch'] | 2463659.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2978 | PHASE_REFERENCE['patroclus_x_km'] | 104.2448 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2979 | PHASE_REFERENCE['patroclus_y_km'] | -109.1216 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 2980 | PHASE_REFERENCE['patroclus_z_km'] | 14.3532 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 4268 | BINARY_PARAMS['separation_au'] | 0.00257 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 4269 | BINARY_PARAMS['period_days'] | 27.321582 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 4270 | BINARY_PARAMS['mass_ratio'] | 0.0123 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 4271 | BINARY_PARAMS['eccentricity'] | 0.0549 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 4273 | BINARY_PARAMS['inclination_ecliptic'] | 5.145 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 4274 | BINARY_PARAMS['Omega_ecliptic'] | 125.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 4275 | BINARY_PARAMS['omega'] | 318.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 6571 | transform['x_angle'] | -120 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 6572 | transform['y_angle'] | -120 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 6573 | transform['z_angle'] | -120 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |

### jupiter_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 66 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 66 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 74 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 81 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 81 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 120 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 128 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 135 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 175 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 175 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 183 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 191 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 191 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 227 | claim: 0.005 AU | 0.005 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 232 | claim: 120 K | 120 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 233 | claim: 200 K | 200 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 250 | claim: 120 K | 120 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 251 | claim: 200 K | 200 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 393 | claim: 200 K | 200 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 393 | claim: 1000 K | 1000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 410 | claim: 200 K | 200 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 410 | claim: 1000 K | 1000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 595 | claim: 0.005 AU | 0.005 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 688 | claim: 0.5 AU | 0.5 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 690 | claim: 0.25 AU | 0.25 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 702 | claim: 0.5 AU | 0.5 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 799 | claim: 500 km | 500 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 799 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 800 | claim: 300 km | 300 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 814 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 815 | claim: 500 km | 500 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 829 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 829 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 843 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 843 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 845 | claim: 600 km | 600 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 904 | claim: 0.4 AU | 0.4 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |

### mars_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 444 | claim: 200 km | 200 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 465 | claim: 200 km | 200 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 515 | claim: 0.005 AU | 0.005 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 626 | claim: 15 Earth radii | 15 Earth radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 744 | claim: 0.01 AU | 0.01 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |

### mercury_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 76 | claim: 1074 km | 1074 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 89 | claim: 1074 km | 1074 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 177 | claim: 0.002 AU | 0.002 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 180 | claim: 35 km | 35 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 196 | claim: 35 km | 35 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 333 | claim: 0.002 AU | 0.002 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 407 | claim: 0.002 AU | 0.002 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 408 | claim: 1.0 AU | 1.0 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 459 | claim: 10 degrees | 10 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 527 | claim: 0.002 AU | 0.002 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 585 | claim: 2440 km | 2440 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 698 | claim: 0.003 AU | 0.003 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |

### messier_catalog.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 17 | 'vmag' | 8.4 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 18 | 'distance_ly' | 6500 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 26 | 'vmag' | 6.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 27 | 'distance_ly' | 5200 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 35 | 'vmag' | 6.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 36 | 'distance_ly' | 7000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 44 | 'vmag' | 6.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 45 | 'distance_ly' | 5500 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 53 | 'vmag' | 6.3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 54 | 'distance_ly' | 5200 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 62 | 'vmag' | 7.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 63 | 'distance_ly' | 1360 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 71 | 'vmag' | 4.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 72 | 'distance_ly' | 1344 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 80 | 'vmag' | 9.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 81 | 'distance_ly' | 1600 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 89 | 'vmag' | 8.8 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 90 | 'distance_ly' | 2300 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 98 | 'vmag' | 10.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 99 | 'distance_ly' | 3400 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 107 | 'vmag' | 8.3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 108 | 'distance_ly' | 1600 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 116 | 'vmag' | 9.9 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 117 | 'distance_ly' | 2600 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 129 | 'vmag' | 4.2 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 130 | 'distance_ly' | 1600 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 138 | 'vmag' | 3.3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 139 | 'distance_ly' | 980 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 147 | 'vmag' | 5.8 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 148 | 'distance_ly' | 6200 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 156 | 'vmag' | 3.7 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 157 | 'distance_ly' | 577 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 165 | 'vmag' | 1.6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 166 | 'distance_ly' | 440 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 179 | 'vmag' | 7.6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 180 | 'distance_ly' | 650 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 188 | 'vmag' | 8.6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 189 | 'distance_ly' | 1400 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 197 | 'vmag' | 9.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 198 | 'distance_ly' | 2870 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 209 | 'vmag' | 5.7 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 210 | 'distance_ly' | 1300 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 218 | 'vmag' | 2.8 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 219 | 'distance_ly' | 850 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 227 | 'vmag' | 5.8 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 228 | 'distance_ly' | 4300 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 239 | 'vmag' | 3.9 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 240 | 'distance_ly' | 2700 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 248 | 'vmag' | 4.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 249 | 'distance_ly' | 6500 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 257 | 'vmag' | 6.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 258 | 'distance_ly' | 1500 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 266 | 'vmag' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 267 | 'distance_ly' | 26000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 275 | 'vmag' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 276 | 'distance_ly' | 18900 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 388 | stats['total_objects'] | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 391 | '<=4.0' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 392 | '4.1-6.0' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 393 | '6.1-9.0' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 394 | '>9.0' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 397 | 'Messier' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 398 | 'Star Clusters' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 399 | 'Planetaries' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 400 | 'Open Clusters' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 401 | 'Nebulae' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |

### moon_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 30 | claim: 1700 K | 1700 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 37 | claim: 1700 K | 1700 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 91 | claim: 1300 K | 1300 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 91 | claim: 1600 K | 1600 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 91 | claim: 1500 K | 1500 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 136 | claim: 200 km | 200 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 154 | claim: 200 km | 200 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 157 | claim: 1573 K | 1573 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 157 | claim: 1743 K | 1743 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 158 | claim: 623 K | 623 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 158 | claim: 823 K | 823 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 159 | claim: 798 K | 798 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 164 | claim: 1677.4 km | 1677.4 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 164 | claim: 1737.4 km | 1737.4 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 452 | claim: 0.001 AU | 0.001 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |

### neptune_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 5 | claim: 47 degrees | 47 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 80 | claim: 15 Earth masses | 15 Earth masses | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 91 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 96 | claim: 15 Earth masses | 15 Earth masses | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 104 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 105 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 144 | claim: 0.005 AU | 0.005 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 404 | claim: 0.2 AU | 0.2 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 408 | claim: 47 degrees | 47 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 504 | claim: 47 deg | 47 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 509 | claim: 47 deg | 47 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 628 | claim: 47 degrees | 47 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 657 | claim: 47 deg | 47 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 822 | claim: 47 deg | 47 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 844 | claim: 47 deg | 47 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 866 | claim: 47 deg | 47 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 889 | claim: 47 deg | 47 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 905 | claim: 47 degrees | 47 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1083 | claim: 23 deg | 23 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1181 | claim: 28.32 deg | 28.32 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1182 | claim: 98 deg | 98 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1186 | claim: 299.36 deg | 299.36 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1186 | claim: 43.46 deg | 43.46 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1202 | claim: 900 km | 900 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1204 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1231 | claim: 200 km | 200 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1233 | claim: 110 km | 110 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1260 | claim: 600 km | 600 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1263 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1289 | claim: 600 km | 600 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1291 | claim: 100 km | 100 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1317 | claim: 930 km | 930 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1319 | claim: 50 km | 50 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1350 | claim: 930 km | 930 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1351 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1351 | claim: 4 deg | 4 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1381 | claim: 930 km | 930 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1382 | claim: 100 km | 100 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1382 | claim: 4.5 deg | 4.5 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1412 | claim: 930 km | 930 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1413 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1413 | claim: 4.2 deg | 4.2 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1443 | claim: 930 km | 930 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1444 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1444 | claim: 4 deg | 4 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1474 | claim: 930 km | 930 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1475 | claim: 200 km | 200 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1475 | claim: 9 deg | 9 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1503 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1526 | claim: 28.32 degrees | 28.32 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1591 | claim: 299.36 deg | 299.36 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1591 | claim: 43.46 deg | 43.46 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1597 | claim: 90 deg | 90 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1602 | claim: 25 deg | 25 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1611 | claim: 32 deg | 32 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1615 | claim: 34 deg | 34 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1657 | claim: 1.0 AU | 1.0 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1676 | claim: 0.3 AU | 0.3 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |

### object_type_analyzer.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 179 | 'Peculiar/Special Objects' | 1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 180 | 'Young Stellar Objects' | 2 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 181 | 'Binary/Multiple Systems' | 3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 182 | 'Variable Stars' | 4 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 183 | 'Evolved Stars' | 5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 184 | 'Normal Stars' | 6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 185 | 'Unknown' | 7 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 198 | 'WolfRayet*' | 10 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 199 | 'SN*' | 10 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 200 | 'Pulsar' | 10 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 201 | 'BlueStraggler' | 9 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 202 | 'Symbiotic*' | 8 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 203 | 'XrayBin' | 8 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 204 | 'Be*' | 7 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 205 | 'CataclyV*' | 7 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 206 | 'YSO' | 6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 207 | 'Cepheid' | 6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 208 | 'RRLyr' | 6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 263 | results['total_count'] | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 264 | results['typed_count'] | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 269 | results['diversity_score'] | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 270 | results['shannon_entropy'] | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 271 | results['simpson_index'] | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 562 | 'total' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 725 | 'total_count' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 726 | 'typed_count' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 731 | 'diversity_score' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |

### orbit_data_manager.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 34 | DEFAULT_DAYS_AHEAD | 730 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 35 | MAX_DATA_AGE_DAYS | 90 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 395 | 'converted_from_old_format' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 589 | 'converted_from_legacy' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1060 | 'x' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1061 | 'y' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1062 | 'z' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1063 | 'range' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1394 | stats['total_points'] | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1397 | stats['file_size_mb'] | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |

### orbital_elements.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 50 | 'a' | 0.3870976430975001 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 51 | 'e' | 0.2056464328427787 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 52 | 'i' | 7.003437180750216 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 61 | 'a' | 0.72333566 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 62 | 'e' | 0.00677672 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 63 | 'i' | 3.39467605 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 86 | 'a' | 1.00000261 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 87 | 'e' | 0.01671123 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 88 | 'i' | 1.531e-05 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 148 | 'a' | 1.126391 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 149 | 'e' | 0.203745 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 150 | 'i' | 6.035 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 151 | 'omega' | 66.223 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 152 | 'Omega' | 2.061 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 158 | 'a' | 1.189562 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 159 | 'e' | 0.190349 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 160 | 'i' | 5.884 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 170 | 'a' | 1.324163 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 171 | 'e' | 0.280164 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 172 | 'i' | 1.622 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 173 | 'omega' | 162.767 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 174 | 'Omega' | 69.095 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 180 | 'a' | 1.680153966583222 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 181 | 'e' | 0.409819444019783 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 182 | 'i' | 3.1489028778487 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 183 | 'omega' | 199.537622506113 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 184 | 'Omega' | 50.09327122563936 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 215 | 'a' | 1.45804 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 216 | 'e' | 0.222868 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 217 | 'i' | 10.829 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 227 | 'a' | 1.52371034 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 228 | 'e' | 0.0933941 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 229 | 'i' | 1.84969142 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 238 | 'a' | 2.191622877873451 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 239 | 'e' | 0.1121269945294693 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 240 | 'i' | 2.093523142255687 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 241 | 'omega' | 66.78467710309617 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 242 | 'Omega' | 21.38248704730461 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 247 | 'a' | 2.3617 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 248 | 'e' | 0.089 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 249 | 'i' | 7.155 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 258 | 'a' | 2.363 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 259 | 'e' | 0.146 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 260 | 'i' | 9.944 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 261 | 'omega' | 250.97 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 262 | 'Omega' | 55.39 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 267 | 'a' | 2.383273486221501 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 268 | 'e' | 0.1874831199365464 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 269 | 'i' | 4.423903983190933 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 270 | 'omega' | 212.9285580998883 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 271 | 'Omega' | 262.7951724145965 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 285 | 'a' | 2.7675 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 286 | 'e' | 0.076 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 287 | 'i' | 10.593 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 316 | 'a' | 5.202887 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 317 | 'e' | 0.04838624 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 318 | 'i' | 1.30439695 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 319 | 'omega' | 273.867 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 320 | 'Omega' | 100.47390909 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 322 | 'TP' | 2459993.18 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 353 | 'a' | 5.212775041416492 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 354 | 'e' | 0.1394751648774633 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 355 | 'i' | 22.05719641611838 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 356 | 'omega' | 307.9473718922942 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 357 | 'Omega' | 44.3495507311498 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 359 | 'TP' | 2460486.237046778 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 387 | 'a' | 9.53667594 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 388 | 'e' | 0.05386179 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 389 | 'i' | 2.48599187 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 390 | 'omega' | 339.392 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 391 | 'Omega' | 113.66242448 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 393 | 'TP' | 2452815.907 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 398 | 'a' | 15.82593058868572 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 399 | 'e' | 0.1719500347024694 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 400 | 'i' | 23.37854062415448 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 401 | 'omega' | 242.9893479383809 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 402 | 'Omega' | 300.4194578295845 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 404 | 'TP' | 2453044.2465350656 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 421 | 'a' | 19.18916464 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 422 | 'e' | 0.04725744 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 423 | 'i' | 0.77263783 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 424 | 'omega' | 96.998857 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 425 | 'Omega' | 74.01692503 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 427 | 'TP' | 2470213.857 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 432 | 'a' | 30.06992276 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 433 | 'e' | 0.00859048 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 434 | 'i' | 1.77004347 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 435 | 'omega' | 276.34 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 436 | 'Omega' | 131.78422574 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 438 | 'TP' | 2468182.079 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 445 | 'a' | 39.39498513874738 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 446 | 'e' | 0.220173694129795 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 447 | 'i' | 20.58296889775066 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 448 | 'omega' | 72.38143133086857 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 449 | 'Omega' | 268.7202801899987 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 451 | 'TP' | 2413410.1091600764 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 456 | 'a' | 39.48211675 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 457 | 'e' | 0.2488273 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 458 | 'i' | 17.14001206 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 459 | 'omega' | 113.834 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 460 | 'Omega' | 110.30393684 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 462 | 'TP' | 2447891.824 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 467 | 'a' | 39.66337068351097 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 468 | 'e' | 0.2418414354067134 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 469 | 'i' | 19.58703444758994 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 470 | 'omega' | 298.8358378061579 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 471 | 'Omega' | 70.99623775199329 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 473 | 'TP' | 2477290.5810889825 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 478 | 'a' | 41.96777641127755 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 479 | 'e' | 0.1393970721853619 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 480 | 'i' | 17.6693032832701 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 481 | 'omega' | 213.7989882449192 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 482 | 'Omega' | 215.9145112848788 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 484 | 'TP' | 2496542.2060495983 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 489 | 'a' | 42.26218206953708 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 490 | 'e' | 0.08176903225395735 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 491 | 'i' | 21.92860124861248 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 492 | 'omega' | 295.464267897557 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 493 | 'Omega' | 250.6682664772548 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 495 | 'TP' | 2448321.55800082 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 500 | 'a' | 42.947 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 501 | 'e' | 0.051739 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 502 | 'i' | 17.2 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 509 | 'a' | 43.13 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 510 | 'e' | 0.191 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 511 | 'i' | 28.2 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 520 | 'a' | 43.325 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 521 | 'e' | 0.0392 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 522 | 'i' | 8.34 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 523 | 'omega' | 157.631 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 524 | 'Omega' | 188.809 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 529 | 'a' | 44.44519963724322 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 530 | 'e' | 0.03868645692376498 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 531 | 'i' | 2.45301305206896 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 538 | 'a' | 45.6923640352447 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 539 | 'e' | 0.1551157031828145 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 540 | 'i' | 28.98446068551257 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 549 | 'a' | 67.15612088312527 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 550 | 'e' | 0.5057697166633393 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 551 | 'i' | 30.86452616352285 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 558 | 'a' | 67.78 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 559 | 'e' | 0.441 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 560 | 'i' | 44.03 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 561 | 'omega' | 150.977 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 562 | 'Omega' | 35.873 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 628 | 'i' | 10.99528818274681 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 646 | 'a' | 481.3036019474312 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 647 | 'e' | 0.8418992747337005 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 648 | 'i' | 11.92926934569724 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 657 | 'a' | 600 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 658 | 'e' | 0.3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 659 | 'i' | 6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 660 | 'L' | 238 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 661 | 'omega' | 150 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 662 | 'Omega' | 90 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 679 | 'a' | 911.3212633626483 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 680 | 'e' | 0.95044195853967 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 681 | 'i' | 16.20068039109616 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 690 | 'i' | 11.66948508856894 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 691 | 'omega' | 118.4456730982617 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 692 | 'Omega' | 300.9623405298694 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 694 | 'TP' | 2480393.563605182 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 858 | 'a' | 6.2682e-05 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 860 | 'e' | 0.0151 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 861 | 'i' | 1.082 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 869 | 'a' | 0.00015683 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 871 | 'e' | 0.00033 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 872 | 'i' | 1.791 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 881 | 'a' | 0.002819 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 883 | 'e' | 0.0041 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 884 | 'i' | 0.05 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 885 | 'omega' | 49.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 886 | 'Omega' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 892 | 'a' | 0.004486 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 894 | 'e' | 0.0094 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 895 | 'i' | 0.471 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 896 | 'omega' | 45.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 897 | 'Omega' | 184.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 903 | 'a' | 0.007155 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 905 | 'e' | 0.0013 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 906 | 'i' | 0.204 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 907 | 'omega' | 198.3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 908 | 'Omega' | 58.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 914 | 'a' | 0.012585 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 916 | 'e' | 0.0074 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 917 | 'i' | 0.205 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 918 | 'omega' | 43.8 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 919 | 'Omega' | 309.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 925 | 'a' | 0.000856 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 927 | 'e' | 0.0002 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 928 | 'i' | 0.06 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 929 | 'omega' | 16.63 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 930 | 'Omega' | 68.9 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 935 | 'a' | 0.000864 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 937 | 'e' | 0.0015 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 938 | 'i' | 0.03 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 939 | 'omega' | 234.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 940 | 'Omega' | 33.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 945 | 'a' | 0.001217 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 947 | 'e' | 0.0032 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 948 | 'i' | 0.374 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 949 | 'omega' | 155.87 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 950 | 'Omega' | 108.05 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 955 | 'a' | 0.001514 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 957 | 'e' | 0.0175 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 958 | 'i' | 1.076 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 959 | 'omega' | 234.57 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 960 | 'Omega' | 237.33 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 969 | 'a' | 4.63e-06 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 970 | 'e' | 0.004 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 971 | 'i' | 106.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 974 | 'omega' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 975 | 'Omega' | 235.3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 976 | 'orbital_period_days' | 4.28268 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 985 | 'a' | 4.63e-06 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 986 | 'e' | 0.004 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 987 | 'i' | 106.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 988 | 'omega' | 180.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 989 | 'Omega' | 235.3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 990 | 'orbital_period_days' | 4.28268 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 998 | 'a' | 0.000893 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1000 | 'e' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1001 | 'i' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1002 | 'omega' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1003 | 'Omega' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1009 | 'a' | 0.0009124 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1011 | 'e' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1012 | 'i' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1013 | 'omega' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1014 | 'Omega' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1020 | 'a' | 0.0009315 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1022 | 'e' | 0.0024 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1023 | 'i' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1024 | 'omega' | 341.9 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1025 | 'Omega' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1031 | 'a' | 0.0009472 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1033 | 'e' | 0.0042 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1034 | 'i' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1035 | 'omega' | 217.9 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1036 | 'Omega' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1042 | 'a' | 0.001242 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1044 | 'e' | 0.0196 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1045 | 'i' | 1.572 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1046 | 'omega' | 160.4 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1047 | 'Omega' | 66.2 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1053 | 'a' | 0.001587 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1055 | 'e' | 0.0047 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1056 | 'i' | 0.009 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1057 | 'omega' | 119.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1058 | 'Omega' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1064 | 'a' | 0.00197 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1066 | 'e' | 0.001 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1067 | 'i' | 1.091 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1068 | 'omega' | 335.3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1069 | 'Omega' | 273.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1075 | 'a' | 0.002525 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1077 | 'e' | 0.0022 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1078 | 'i' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1079 | 'omega' | 116.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1080 | 'Omega' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1086 | 'a' | 0.003524 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1088 | 'e' | 0.001 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1089 | 'i' | 0.333 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1090 | 'omega' | 44.3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1091 | 'Omega' | 133.7 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1097 | 'a' | 0.008168 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1099 | 'e' | 0.0288 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1100 | 'i' | 0.306 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1101 | 'omega' | 78.3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1102 | 'Omega' | 78.6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1108 | 'a' | 0.010033 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1110 | 'e' | 0.0232 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1111 | 'i' | 0.615 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1112 | 'omega' | 214.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1113 | 'Omega' | 87.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1119 | 'a' | 0.0238 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1121 | 'e' | 0.0283 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1122 | 'i' | 7.489 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1123 | 'omega' | 254.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1124 | 'Omega' | 86.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1130 | 'a' | 0.08655 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1132 | 'e' | 0.1635 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1133 | 'i' | 175.986 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1134 | 'omega' | 240.3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1135 | 'Omega' | 192.7 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1142 | 'a' | 0.000868 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1144 | 'e' | 0.0013 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1145 | 'i' | 4.338 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1146 | 'omega' | 155.6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1147 | 'Omega' | 100.6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1153 | 'a' | 0.001276 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1155 | 'e' | 0.0012 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1156 | 'i' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1157 | 'omega' | 83.3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1158 | 'Omega' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1164 | 'a' | 0.001778 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1166 | 'e' | 0.0039 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1167 | 'i' | 0.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1168 | 'omega' | 157.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1169 | 'Omega' | 195.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1175 | 'a' | 0.002914 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1177 | 'e' | 0.001 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1178 | 'i' | 0.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1179 | 'omega' | 202.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1180 | 'Omega' | 26.4 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1186 | 'a' | 0.003907 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1188 | 'e' | 0.0008 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1189 | 'i' | 0.058 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1190 | 'omega' | 182.4 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1191 | 'Omega' | 30.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1197 | 'a' | 0.0004419 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1199 | 'e' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1200 | 'i' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1201 | 'omega' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1202 | 'Omega' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1208 | 'a' | 0.0006531 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1210 | 'e' | 0.003 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1211 | 'i' | 0.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1212 | 'omega' | 237.9 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1213 | 'Omega' | 188.2 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1220 | 'a' | 0.002371 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1222 | 'e' | 1.6e-05 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1223 | 'i' | 157.3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1224 | 'omega' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1225 | 'Omega' | 178.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1231 | 'a' | 0.0003509 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1233 | 'e' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1234 | 'i' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1235 | 'omega' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1236 | 'Omega' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1242 | 'a' | 0.0004144 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1244 | 'e' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1245 | 'i' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1246 | 'omega' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1247 | 'Omega' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1254 | 'a' | 0.00013102 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1256 | 'e' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1257 | 'i' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1258 | 'omega' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1259 | 'Omega' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1265 | 'a' | 0.00028877 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1267 | 'e' | 0.025 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1268 | 'i' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1269 | 'omega' | 322.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1270 | 'Omega' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1276 | 'a' | 0.00032955 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1278 | 'e' | 0.025 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1279 | 'i' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1280 | 'omega' | 31.4 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1281 | 'Omega' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1286 | 'a' | 0.00038971 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1288 | 'e' | 0.01 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1289 | 'i' | 0.4 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1290 | 'omega' | 32.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1291 | 'Omega' | 314.3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1297 | 'a' | 0.00043584 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1299 | 'e' | 0.009 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1300 | 'i' | 0.3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1301 | 'omega' | 139.3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1302 | 'Omega' | 114.3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1319 | 'a' | 0.000249 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1320 | 'e' | 0.0062 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1321 | 'i' | 78.29 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1322 | 'omega' | 139.65 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1323 | 'Omega' | 29.43 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1324 | 'orbital_period_days' | 15.786 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1329 | 'a' | 0.0001606 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1330 | 'e' | 0.29 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1331 | 'i' | 83.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1332 | 'omega' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1333 | 'Omega' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1334 | 'orbital_period_days' | 25.22 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1340 | 'a' | 6.02e-05 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1341 | 'e' | 0.007 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1342 | 'i' | 90.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1343 | 'omega' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1344 | 'Omega' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1345 | 'orbital_period_days' | 9.54 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1355 | 'Omega' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1356 | 'orbital_period_days' | 12.4 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1362 | 'a' | 0.0003246 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1363 | 'e' | 0.0513 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1364 | 'i' | 126.356 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1365 | 'omega' | 154.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1366 | 'Omega' | 206.766 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1367 | 'orbital_period_days' | 49.12 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1371 | 'a' | 0.0001652 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1372 | 'e' | 0.249 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1373 | 'i' | 113.013 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1374 | 'omega' | 178.9 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1375 | 'Omega' | 205.016 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1376 | 'orbital_period_days' | 18.28 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1381 | 'a' | 0.0001487 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1382 | 'e' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1383 | 'i' | 83.7 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1384 | 'omega' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1385 | 'Omega' | 0.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1386 | 'orbital_period_days' | 18.023 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1421 | planet_tilts['Earth'] | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1422 | planet_tilts['Mars'] | 25.19 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1423 | planet_tilts['Jupiter'] | 3.13 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1424 | planet_tilts['Saturn'] | -26.73 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1425 | planet_tilts['Uranus'] | 97.77 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1426 | planet_tilts['Neptune'] | 28.32 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 1427 | planet_tilts['Pluto'] | -122.53 | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |

### osculating_cache_manager.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 82 | REFRESH_INTERVALS['Mercury'] | 7 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 83 | REFRESH_INTERVALS['Moon'] | 1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 84 | REFRESH_INTERVALS['C/2025 N1'] | 1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 85 | REFRESH_INTERVALS['3I/ATLAS'] | 1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 89 | REFRESH_INTERVALS['pattern:C/'] | 1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 90 | REFRESH_INTERVALS['pattern:P/'] | 1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 91 | REFRESH_INTERVALS['pattern:I/'] | 1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 92 | REFRESH_INTERVALS['pattern:2025'] | 7 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 93 | REFRESH_INTERVALS['pattern:2024'] | 7 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 97 | REFRESH_INTERVALS['type:satellite'] | 7 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 98 | REFRESH_INTERVALS['type:orbital'] | 7 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 99 | REFRESH_INTERVALS['type:trajectory'] | 30 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 100 | REFRESH_INTERVALS['type:lagrange_point'] | 90 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 103 | REFRESH_INTERVALS['default'] | 30 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 329 | 'exists' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 332 | 'is_fresh' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 341 | 'exists' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 344 | 'is_fresh' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 352 | 'exists' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |

### planet9_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 21 | claim: 0.005 AU | 0.005 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 23 | claim: 4 Earth radii | 4 Earth radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 24 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 40 | claim: 4 Earth radii | 4 Earth radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 41 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 47 | claim: 4 Earth radii | 4 Earth radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 50 | claim: 4 Earth radii | 4 Earth radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 54 | claim: 4 Earth radii | 4 Earth radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 54 | claim: 3.7 Earth radii | 3.7 Earth radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 55 | claim: 10 Earth masses | 10 Earth masses | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 57 | claim: 4 Earth radii | 4 Earth radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 197 | claim: 8 AU | 8 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 197 | claim: 800 AU | 800 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 201 | claim: 7.6 AU | 7.6 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 213 | claim: 8 AU | 8 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 213 | claim: 800 AU | 800 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 215 | claim: 7.6 AU | 7.6 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 216 | claim: 7.6 AU | 7.6 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 217 | claim: 600 AU | 600 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 217 | claim: 700 AU | 700 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 222 | claim: 280 AU | 280 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 222 | claim: 1120 AU | 1120 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 232 | claim: 600 AU | 600 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 236 | claim: 420 AU | 420 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |

### planet_visualization_utilities.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 21 | SOLAR_RADIUS_AU | 0.00465047 | 4 | 5 | **20** | No source citation (recalled) | Imported by 15 modules |
| 22 | CORE_AU | 0.00093 | 4 | 5 | **20** | No source citation (recalled) | Imported by 15 modules |
| 23 | RADIATIVE_ZONE_AU | 0.00325 | 4 | 5 | **20** | No source citation (recalled) | Imported by 15 modules |
| 24 | CHROMOSPHERE_RADII | 1.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 15 modules |
| 25 | INNER_CORONA_RADII | 3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 15 modules |
| 26 | OUTER_CORONA_RADII | 50 | 4 | 5 | **20** | No source citation (recalled) | Imported by 15 modules |
| 27 | STREAMER_BELT_RADII | 6.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 15 modules |
| 28 | ROCHE_LIMIT_RADII | 3.45 | 4 | 5 | **20** | No source citation (recalled) | Imported by 15 modules |
| 30 | ALFVEN_SURFACE_RADII | 18.8 | 4 | 5 | **20** | No source citation (recalled) | Imported by 15 modules |
| 31 | TERMINATION_SHOCK_AU | 94 | 4 | 5 | **20** | No source citation (recalled) | Imported by 15 modules |
| 32 | HELIOPAUSE_RADII | 26449 | 4 | 5 | **20** | No source citation (recalled) | Imported by 15 modules |
| 33 | INNER_LIMIT_OORT_CLOUD_AU | 2000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 15 modules |
| 34 | INNER_OORT_CLOUD_AU | 20000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 15 modules |
| 35 | OUTER_OORT_CLOUD_AU | 100000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 15 modules |
| 36 | GRAVITATIONAL_INFLUENCE_AU | 126000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 15 modules |

### pluto_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 23 | claim: 1700 km | 1700 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 37 | claim: 1700 km | 1700 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 49 | claim: 1000 K | 1000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 53 | claim: 40 K | 40 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 93 | claim: 180 km | 180 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 107 | claim: 180 km | 180 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 152 | claim: 0.005 AU | 0.005 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 326 | claim: 200 km | 200 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 344 | claim: 200 km | 200 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 354 | claim: 200 km | 200 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 366 | claim: 200 km | 200 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 408 | claim: 200 km | 200 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 426 | claim: 200 km | 200 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 431 | claim: 1188 km | 1188 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 433 | claim: 1700 km | 1700 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 438 | claim: 200 km | 200 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 485 | claim: 0.1 AU | 0.1 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 489 | claim: 0.04 AU | 0.04 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 504 | claim: 0.05 AU | 0.05 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 506 | claim: 0.04 AU | 0.04 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |

### saturn_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 65 | layer_info['radius_fraction'] | 0.6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 67 | layer_info['opacity'] | 1.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 135 | layer_info['radius_fraction'] | 0.9 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 137 | layer_info['opacity'] | 0.9 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 196 | layer_info['radius_fraction'] | 0.99 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 198 | layer_info['opacity'] | 0.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 260 | layer_info['radius_fraction'] | 1.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 262 | layer_info['opacity'] | 1.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 468 | layer_info['radius_fraction'] | 1.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 470 | layer_info['opacity'] | 0.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 571 | params['sunward_distance'] | 22 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 574 | params['equatorial_radius'] | 45 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 575 | params['polar_radius'] | 35 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 578 | params['tail_length'] | 500 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 579 | params['tail_base_radius'] | 75 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 580 | params['tail_end_radius'] | 100 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 879 | layer_info['radius_fraction'] | 1120 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 881 | layer_info['opacity'] | 0.3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 970 | 'inner_radius_km' | 66900 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 971 | 'outer_radius_km' | 74500 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 972 | 'thickness_km' | 10 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 974 | 'opacity' | 0.4 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 985 | 'inner_radius_km' | 74658 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 986 | 'outer_radius_km' | 92000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 987 | 'thickness_km' | 10 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 989 | 'opacity' | 0.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 1000 | 'inner_radius_km' | 92000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 1001 | 'outer_radius_km' | 117500 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 1002 | 'thickness_km' | 10 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 1004 | 'opacity' | 0.8 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 1015 | 'inner_radius_km' | 122340 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 1016 | 'outer_radius_km' | 136800 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 1017 | 'thickness_km' | 30 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 1019 | 'opacity' | 0.7 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 1032 | 'inner_radius_km' | 140210 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 1033 | 'outer_radius_km' | 140420 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 1034 | 'thickness_km' | 1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 1036 | 'opacity' | 0.3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 1047 | 'inner_radius_km' | 166000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 1048 | 'outer_radius_km' | 175000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 1049 | 'thickness_km' | 100 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 1051 | 'opacity' | 0.2 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 1062 | 'inner_radius_km' | 180000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 1063 | 'outer_radius_km' | 480000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 1064 | 'thickness_km' | 1000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 1066 | 'opacity' | 0.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 66 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 80 | claim: 17 Earth masses | 17 Earth masses | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 81 | claim: 55 Earth masses | 55 Earth masses | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 85 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 136 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 146 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 246 | claim: 0.005 AU | 0.005 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 303 | claim: 200 km | 200 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 517 | claim: 300 km | 300 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 641 | claim: 26.73 degrees | 26.73 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 695 | claim: 100 kg | 100 kg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 781 | claim: 26.73 degrees | 26.73 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 866 | claim: 0.6 AU | 0.6 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 884 | claim: 0.3 AU | 0.3 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1147 | claim: 0.2 AU | 0.2 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |

### save_utils.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 105 | 'displayModeBar' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 18 modules |
| 257 | result['confirmed'] | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 18 modules |

### sgr_a_star_data.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 40 | B_STAR_TEMPERATURES['O'] | 35000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 41 | B_STAR_TEMPERATURES['B0'] | 30000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 42 | B_STAR_TEMPERATURES['B1'] | 25400 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 43 | B_STAR_TEMPERATURES['B2'] | 22000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 44 | B_STAR_TEMPERATURES['B3'] | 18700 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 45 | B_STAR_TEMPERATURES['B5'] | 15400 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 46 | B_STAR_TEMPERATURES['B7'] | 13000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 47 | B_STAR_TEMPERATURES['B8'] | 11400 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 48 | B_STAR_TEMPERATURES['B9'] | 10500 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 49 | B_STAR_TEMPERATURES['B'] | 20000 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 135 | G_CONST | 6.6743e-11 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 136 | SPEED_OF_LIGHT | 299792458.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 137 | SPEED_OF_LIGHT_KM_S | 299792.458 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 138 | SOLAR_MASS_KG | 1.989e+30 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 139 | AU_TO_METERS | 149600000000.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 140 | AU_TO_KM | 149600000.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 141 | PARSEC_TO_AU | 206265.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 148 | SGR_A_MASS_SOLAR | 4154000.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 150 | SGR_A_DISTANCE_PC | 8178.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 151 | SGR_A_DISTANCE_LY | 26670.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 185 | 'a_au' | 1031.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 186 | 'e' | 0.8843 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 187 | 'period_yrs' | 16.05 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 188 | 't_periapsis' | 2018.38 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 189 | 'arg_periapsis_deg' | 66.13 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 190 | 'inclination_deg' | 134.18 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 191 | 'asc_node_deg' | 228.07 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 194 | 'mass_solar' | 14.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 200 | 'a_au' | 740.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 201 | 'e' | 0.976 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 202 | 'period_yrs' | 9.9 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 203 | 't_periapsis' | 2003.33 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 204 | 'arg_periapsis_deg' | 42.6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 205 | 'inclination_deg' | 72.8 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 206 | 'asc_node_deg' | 122.6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 209 | 'mass_solar' | 6.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 215 | 'a_au' | 572.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 216 | 'e' | 0.768 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 217 | 'period_yrs' | 7.6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 218 | 't_periapsis' | 2013.4 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 219 | 'arg_periapsis_deg' | 120.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 220 | 'inclination_deg' | 110.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 221 | 'asc_node_deg' | 100.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 224 | 'mass_solar' | 2.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 230 | 'a_au' | 520.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 231 | 'e' | 0.985 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 232 | 'period_yrs' | 12.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 233 | 't_periapsis' | 2017.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 234 | 'arg_periapsis_deg' | 130.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 235 | 'inclination_deg' | 120.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 236 | 'asc_node_deg' | 90.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 239 | 'mass_solar' | 2.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 631 | 'date' | 2018.38 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 638 | 'date' | 2020.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 645 | 'date' | 2020.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 652 | 'date' | 2020.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 5 modules |
| 84 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 135 | claim: 3 kg | 3 kg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 139 | claim: 1 AU | 1 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 140 | claim: 1 AU | 1 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 158 | claim: 0.08 AU | 0.08 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 462 | claim: 0.2 degrees | 0.2 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 479 | claim: 120 AU | 120 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 633 | claim: 120 AU | 120 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 640 | claim: 27 years | 27 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |

### simbad_manager.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 685 | 'total_pkl_entries' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 6 modules |
| 686 | 'total_vot_entries' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 6 modules |
| 977 | props['is_messier'] | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 6 modules |
| 1020 | 'is_messier' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 6 modules |
| 1031 | 'is_messier' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 6 modules |

### solar_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 33 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 37 | claim: 123 AU | 123 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 40 | claim: 936 AU | 936 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 41 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 41 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 42 | claim: 2 light-years | 2 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 42 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 61 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 61 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 65 | claim: 200 years | 200 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 67 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 67 | claim: 1.58 light-years | 1.58 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 78 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 78 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 81 | claim: 200 years | 200 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 83 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 83 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 92 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 92 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 95 | claim: 200 years | 200 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 97 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 97 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 108 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 114 | claim: 1 km | 1 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 132 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 138 | claim: 1 km | 1 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 156 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 162 | claim: 1 km | 1 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 199 | claim: 123 AU | 123 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 201 | claim: 150 AU | 150 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 202 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 209 | claim: 100 AU | 100 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 215 | claim: 94 AU | 94 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 215 | claim: 84 AU | 84 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 216 | claim: 200 km | 200 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 222 | claim: 50 solar radii | 50 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 222 | claim: 0.23 AU | 0.23 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 226 | claim: 6 R_sun | 6 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 227 | claim: 20 R_sun | 20 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 228 | claim: 18.8 R_sun | 18.8 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 230 | claim: 50 R_sun | 50 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 264 | claim: 3 solar radii | 3 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 264 | claim: 0.014 AU | 0.014 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 292 | claim: 1.5 Solar radii | 1.5 Solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 292 | claim: 0.0070 AU | 0.0070 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 293 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 293 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 302 | claim: 1 Solar radii | 1 Solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 302 | claim: 0.00465 AU | 0.00465 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 303 | claim: 500 K | 500 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 332 | claim: 0.7 solar radii | 0.7 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 332 | claim: 0.00325 AU | 0.00325 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 392 | claim: 123 AU | 123 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 395 | claim: 936 AU | 936 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 396 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 396 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 397 | claim: 2 light-years | 2 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 397 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 416 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 416 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 420 | claim: 200 years | 200 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 422 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 422 | claim: 1.58 light-years | 1.58 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 433 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 433 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 436 | claim: 200 years | 200 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 438 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 438 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 447 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 447 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 450 | claim: 200 years | 200 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 452 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 452 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 482 | claim: 123 AU | 123 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 484 | claim: 150 AU | 150 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 485 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 492 | claim: 100 AU | 100 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 498 | claim: 94 AU | 94 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 498 | claim: 84 AU | 84 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 499 | claim: 200 km | 200 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 505 | claim: 50 solar radii | 50 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 505 | claim: 0.23 AU | 0.23 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 509 | claim: 6 R_sun | 6 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 510 | claim: 20 R_sun | 20 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 511 | claim: 18.8 R_sun | 18.8 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 516 | claim: 8.8 R_sun | 8.8 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 519 | claim: 33 R_sun | 33 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 527 | claim: 6 solar radii | 6 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 531 | claim: 3 R_sun | 3 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 534 | claim: 3 R_sun | 3 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 534 | claim: 15 R_sun | 15 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 535 | claim: 2 R_sun | 2 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 537 | claim: 6 R_sun | 6 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 540 | claim: 0.15 AU | 0.15 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 540 | claim: 33 R_sun | 33 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 548 | claim: 6 solar radii | 6 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 552 | claim: 3 R_sun | 3 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 555 | claim: 3 R_sun | 3 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 555 | claim: 15 R_sun | 15 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 556 | claim: 2 R_sun | 2 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 558 | claim: 6 R_sun | 6 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 561 | claim: 33 R_sun | 33 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 572 | claim: 408 kg | 408 kg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 572 | claim: 500 kg | 500 kg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 573 | claim: 3.45 solar radii | 3.45 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 573 | claim: 165 km | 165 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 574 | claim: 465 km | 465 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 574 | claim: 0.0114 AU | 0.0114 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 580 | claim: 5 km | 5 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 580 | claim: 1.66 R_sun | 1.66 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 580 | claim: 0.008 AU | 0.008 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 581 | claim: 1.19 R_sun | 1.19 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 581 | claim: 0.006 AU | 0.006 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 582 | claim: 1.2 R_sun | 1.2 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 587 | claim: 8.33 R_sun | 8.33 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 587 | claim: 0.039 AU | 0.039 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 590 | claim: 3.45 R_sun | 3.45 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 590 | claim: 0.016 AU | 0.016 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 591 | claim: 1.23 R_sun | 1.23 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 601 | claim: 408 kg | 408 kg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 601 | claim: 500 kg | 500 kg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 602 | claim: 3.45 R_sun | 3.45 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 602 | claim: 0.016 AU | 0.016 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 607 | claim: 5 km | 5 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 607 | claim: 1.66 R_sun | 1.66 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 607 | claim: 0.008 AU | 0.008 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 608 | claim: 1.19 R_sun | 1.19 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 608 | claim: 0.006 AU | 0.006 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 609 | claim: 1.2 R_sun | 1.2 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 613 | claim: 8.33 R_sun | 8.33 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 613 | claim: 0.039 AU | 0.039 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 615 | claim: 1.23 R_sun | 1.23 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 615 | claim: 0.006 AU | 0.006 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 626 | claim: 20 solar radii | 20 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 627 | claim: 18.8 R_sun | 18.8 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 628 | claim: 5 hours | 5 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 630 | claim: 15 R_sun | 15 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 630 | claim: 19 R_sun | 19 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 640 | claim: 20 hours | 20 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 653 | claim: 18.8 R_sun | 18.8 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 654 | claim: 5 hours | 5 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 656 | claim: 15 R_sun | 15 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 656 | claim: 19 R_sun | 19 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 660 | claim: 800 km | 800 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 664 | claim: 20 hours | 20 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 674 | claim: 3 solar radii | 3 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 677 | claim: 2.3 R_sun | 2.3 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 677 | claim: 3 R_sun | 3 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 683 | claim: 3.45 R_sun | 3.45 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 685 | claim: 1.23 R_sun | 1.23 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 688 | claim: 3 solar radii | 3 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 688 | claim: 0.014 AU | 0.014 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 716 | claim: 1.5 Solar radii | 1.5 Solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 716 | claim: 0.0070 AU | 0.0070 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 717 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 717 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 726 | claim: 1 Solar radii | 1 Solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 726 | claim: 0.00465 AU | 0.00465 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 727 | claim: 500 K | 500 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 756 | claim: 0.7 solar radii | 0.7 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 756 | claim: 0.00325 AU | 0.00325 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 816 | claim: 3 R_sun | 3 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 817 | claim: 3.45 R_sun | 3.45 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 818 | claim: 6 R_sun | 6 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 819 | claim: 18.8 R_sun | 18.8 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 821 | claim: 50 R_sun | 50 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 822 | claim: 8.8 R_sun | 8.8 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 828 | claim: 18.8 R_sun | 18.8 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 828 | claim: 0.087 AU | 0.087 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 829 | claim: 8.33 R_sun | 8.33 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 829 | claim: 0.039 AU | 0.039 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 831 | claim: 1.23 R_sun | 1.23 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 831 | claim: 0.006 AU | 0.006 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 832 | claim: 40 hours | 40 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 833 | claim: 8.8 R_sun | 8.8 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 833 | claim: 0.041 AU | 0.041 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 834 | claim: 8.33 R_sun | 8.33 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 834 | claim: 0.039 AU | 0.039 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 847 | claim: 5778 K | 5778 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 847 | claim: 500 degrees | 500 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 847 | claim: 000 degrees | 000 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 863 | claim: 0 pc | 0 pc | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 863 | claim: 0 ly | 0 ly | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 872 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 873 | claim: 0.00465 AU | 0.00465 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 873 | claim: 1.0 R_sun | 1.0 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 878 | claim: 3 solar radii | 3 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 878 | claim: 0.014 AU | 0.014 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 879 | claim: 3.45 R_sun | 3.45 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 883 | claim: 3.45 solar radii | 3.45 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 883 | claim: 0.016 AU | 0.016 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 890 | claim: 6 solar radii | 6 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 894 | claim: 18.8 R_sun | 18.8 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 900 | claim: 50 solar radii | 50 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 900 | claim: 0.23 AU | 0.23 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1159 | claim: 6 solar radii | 6 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1190 | claim: 3.45 solar radii | 3.45 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1190 | claim: 0.016 AU | 0.016 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1192 | claim: 500 kg | 500 kg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1195 | claim: 8.33 R_sun | 8.33 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1195 | claim: 0.039 AU | 0.039 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1224 | claim: 18.8 solar radii | 18.8 solar radii | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1225 | claim: 0.087 AU | 0.087 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1405 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1526 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1572 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1612 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1662 | claim: 000 AU | 000 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1669 | claim: 1 km | 1 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |

### spacecraft_encounters.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 59 | AU_KM | 149597870.7 | 4 | 5 | **20** | No source citation (recalled) | Data constant imported by 1 modules |
| 59 | claim: 1 AU | 1 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 99 | claim: 0.01541 AU | 0.01541 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 103 | claim: 16.26 km | 16.26 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 104 | claim: 43 km | 43 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 106 | claim: 19 km | 19 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 107 | claim: 4 km | 4 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 108 | claim: 23 km | 23 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 125 | claim: 472 km | 472 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 126 | claim: 0.0000834 AU | 0.0000834 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 130 | claim: 472 km | 472 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 131 | claim: 13.78 km | 13.78 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 132 | claim: 800 km | 800 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 152 | claim: 0.0000236 AU | 0.0000236 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 156 | claim: 43.4 AU | 43.4 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 189 | claim: 0.000470 AU | 0.000470 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 194 | claim: 185 km | 185 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 195 | claim: 377 km | 377 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 221 | claim: 0.0000595 AU | 0.0000595 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 224 | claim: 53 years | 53 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 229 | claim: 3 minutes | 3 minutes | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 231 | claim: 171 km | 171 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 251 | claim: 0.0000434 AU | 0.0000434 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 259 | claim: 122 km | 122 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 260 | claim: 10.8 km | 10.8 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 261 | claim: 11 km | 11 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 261 | claim: 7.6 km | 7.6 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 262 | claim: 2.9 km | 2.9 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 474 | claim: 10 minutes | 10 minutes | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 807 | claim: 7 days | 7 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1353 | claim: 7 days | 7 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1353 | claim: 365 days | 365 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1388 | claim: 4 days | 4 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1389 | claim: 8.33 R_sun | 8.33 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1390 | claim: 29 R_sun | 29 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1391 | claim: 0.023 AU | 0.023 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1397 | claim: 8.33 R_sun | 8.33 R_sun | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1397 | claim: 0.039 AU | 0.039 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |

### star_notes.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 19 | claim: 97 light-years | 97 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 63 | claim: 8.9 hours | 8.9 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 118 | claim: 37 light-years | 37 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 123 | claim: 778 K | 778 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 163 | claim: 310 light-years | 310 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 216 | claim: 790 K | 790 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 228 | claim: 4.37 light-years | 4.37 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 230 | claim: 80 years | 80 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 243 | claim: 525 light-years | 525 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 283 | claim: 50 years | 50 years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 284 | claim: 8.6 light-years | 8.6 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 340 | claim: 11.46 light-years | 11.46 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 394 | claim: 88 light-years | 88 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 478 | claim: 144 light-years | 144 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 556 | claim: 51 light-years | 51 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 568 | claim: 590 days | 590 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 615 | claim: 79 light-years | 79 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 618 | claim: 15.9 hours | 15.9 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 639 | claim: 2.7 days | 2.7 days | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 676 | claim: 25 light-years | 25 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 679 | claim: 12.5 hours | 12.5 hours | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 777 | claim: 900 light-years | 900 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 784 | claim: 000 light-years | 000 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 808 | claim: 817 light-years | 817 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 884 | claim: 25 light-years | 25 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1015 | claim: 65 light-years | 65 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1019 | claim: 778 K | 778 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1114 | claim: 250 light-years | 250 light-years | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |

### star_properties.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 279 | 'is_messier' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 290 | 'is_messier' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 312 | 'is_messier' | True | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 324 | 'is_messier' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |
| 335 | 'is_messier' | False | 4 | 5 | **20** | No source citation (recalled) | Imported by 4 modules |

### stellar_parameters.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 253 | 'O' | -6.4 | 4 | 5 | **20** | No source citation (recalled) | Imported by 8 modules |
| 253 | 'B' | -6.0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 8 modules |
| 253 | 'A' | -5.8 | 4 | 5 | **20** | No source citation (recalled) | Imported by 8 modules |
| 254 | 'F' | -5.6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 8 modules |
| 254 | 'G' | -5.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 8 modules |
| 254 | 'K' | -4.6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 8 modules |
| 254 | 'M' | -4.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 8 modules |
| 257 | 'O' | -5.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 8 modules |
| 257 | 'B' | -4.8 | 4 | 5 | **20** | No source citation (recalled) | Imported by 8 modules |
| 257 | 'A' | -4.3 | 4 | 5 | **20** | No source citation (recalled) | Imported by 8 modules |
| 258 | 'F' | -3.9 | 4 | 5 | **20** | No source citation (recalled) | Imported by 8 modules |
| 258 | 'G' | -3.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 8 modules |
| 258 | 'K' | -3.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 8 modules |
| 258 | 'M' | -2.6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 8 modules |
| 261 | 'O' | -4.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 8 modules |
| 261 | 'B' | -3.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 8 modules |
| 261 | 'A' | -2.8 | 4 | 5 | **20** | No source citation (recalled) | Imported by 8 modules |
| 262 | 'F' | -2.4 | 4 | 5 | **20** | No source citation (recalled) | Imported by 8 modules |
| 262 | 'G' | -2.1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 8 modules |
| 262 | 'K' | -1.6 | 4 | 5 | **20** | No source citation (recalled) | Imported by 8 modules |
| 262 | 'M' | -1.2 | 4 | 5 | **20** | No source citation (recalled) | Imported by 8 modules |

### uranus_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 5 | claim: 59 degrees | 59 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 27 | claim: 5255 K | 5255 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 35 | claim: 5255 K | 5255 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 41 | claim: 5255 K | 5255 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 90 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 100 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 100 | claim: 000 K | 000 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 139 | claim: 0.005 AU | 0.005 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 143 | claim: 320 K | 320 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 143 | claim: 53 K | 53 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 162 | claim: 320 K | 320 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 162 | claim: 53 K | 53 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 167 | claim: 559 km | 559 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 172 | claim: 50 km | 50 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 182 | claim: 559 km | 559 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 182 | claim: 50 km | 50 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 184 | claim: 609 km | 609 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 184 | claim: 559 km | 559 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 351 | claim: 559 km | 559 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 352 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 352 | claim: 559 km | 559 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 352 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 353 | claim: 559 km | 559 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 353 | claim: 559 km | 559 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 354 | claim: 559 km | 559 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 355 | claim: 559 km | 559 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 401 | claim: 0.2 AU | 0.2 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 405 | claim: 60 degrees | 60 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 457 | claim: 60 degrees | 60 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 579 | claim: 97.77 degrees | 97.77 degrees | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 724 | claim: 97.77 deg | 97.77 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 727 | claim: 105 deg | 105 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 727 | claim: 105 deg | 105 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 736 | claim: 105 deg | 105 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 736 | claim: 97.77 deg | 97.77 deg | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 755 | claim: 2 km | 2 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 766 | claim: 7 km | 7 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 771 | claim: 7 km | 7 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 788 | claim: 3 km | 3 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 800 | claim: 10 km | 10 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 805 | claim: 10 km | 10 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 818 | claim: 11 km | 11 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 824 | claim: 11 km | 11 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 842 | claim: 2 km | 2 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 855 | claim: 4 km | 4 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 861 | claim: 4 km | 4 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 874 | claim: 7 km | 7 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 880 | claim: 7 km | 7 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 893 | claim: 100 km | 100 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 899 | claim: 100 km | 100 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 913 | claim: 12000 km | 12000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 919 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 921 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 921 | claim: 700 km | 700 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 922 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 922 | claim: 700 km | 700 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 947 | claim: 17000 km | 17000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 953 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 955 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 955 | claim: 700 km | 700 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 956 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 956 | claim: 700 km | 700 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1053 | claim: 0.6 AU | 0.6 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1057 | claim: 7 km | 7 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1058 | claim: 360 km | 360 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1072 | claim: 0.6 AU | 0.6 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1074 | claim: 7 km | 7 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 1075 | claim: 360 km | 360 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |

### venus_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 23 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 38 | claim: 000 km | 000 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 363 | claim: 70 km | 70 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 365 | claim: 60 km | 60 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 365 | claim: 100 km | 100 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 368 | claim: 100 km | 100 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 369 | claim: 100 km | 100 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 371 | claim: 300 K | 300 K | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 372 | claim: 120 km | 120 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 375 | claim: 200 km | 200 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 377 | claim: 120 km | 120 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 379 | claim: 140 km | 140 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 384 | claim: 120 km | 120 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 385 | claim: 500 km | 500 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 444 | claim: 0.005 AU | 0.005 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 522 | claim: 120 km | 120 km | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |
| 648 | claim: 0.01 AU | 0.01 AU | 4 | 4 | **16** | No source citation (recalled) | In display string (hover text / INFO) |

### visualization_utils.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 120 | 'x' | 0.001 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 120 | 'y' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 120 | 'z' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 121 | 'x' | 1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 121 | 'y' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 121 | 'z' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 122 | 'x' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 122 | 'y' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 122 | 'z' | 1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 210 | 'x' | 0.001 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 210 | 'y' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 210 | 'z' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 211 | 'x' | 1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 211 | 'y' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 211 | 'z' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 212 | 'x' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 212 | 'y' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 212 | 'z' | 1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 269 | 'x' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 269 | 'y' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 269 | 'z' | 1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 422 | 'x' | 1.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 422 | 'y' | 1.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 422 | 'z' | 1.2 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 423 | 'x' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 423 | 'y' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 423 | 'z' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 424 | 'x' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 424 | 'y' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 424 | 'z' | 1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 436 | 'x' | 1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 436 | 'y' | 1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 436 | 'z' | 1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 485 | 'x' | 1.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 485 | 'y' | 1.5 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 485 | 'z' | 1.2 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 486 | 'x' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 486 | 'y' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 486 | 'z' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 487 | 'x' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 487 | 'y' | 0 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 487 | 'z' | 1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 499 | 'x' | 1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 499 | 'y' | 1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |
| 499 | 'z' | 1 | 4 | 5 | **20** | No source citation (recalled) | Imported by 3 modules |

---

## Tier 2: FIX NEXT SESSION (Score 10-15)

### celestial_coordinates.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 139 | MAJOR_BODY_UNCERTAINTIES['Mercury'] | 0.005 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 140 | MAJOR_BODY_UNCERTAINTIES['Venus'] | 0.003 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 141 | MAJOR_BODY_UNCERTAINTIES['Mars'] | 0.002 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 142 | MAJOR_BODY_UNCERTAINTIES['Jupiter'] | 0.05 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 143 | MAJOR_BODY_UNCERTAINTIES['Saturn'] | 0.1 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 144 | MAJOR_BODY_UNCERTAINTIES['Uranus'] | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 145 | MAJOR_BODY_UNCERTAINTIES['Neptune'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 148 | MAJOR_BODY_UNCERTAINTIES['Ceres'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 149 | MAJOR_BODY_UNCERTAINTIES['Pluto'] | 0.8 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 150 | MAJOR_BODY_UNCERTAINTIES['Eris'] | 5.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 151 | MAJOR_BODY_UNCERTAINTIES['Makemake'] | 3.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 152 | MAJOR_BODY_UNCERTAINTIES['Haumea'] | 2.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 153 | MAJOR_BODY_UNCERTAINTIES['Gonggong'] | 5.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 154 | MAJOR_BODY_UNCERTAINTIES['Quaoar'] | 3.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 155 | MAJOR_BODY_UNCERTAINTIES['Sedna'] | 10.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 156 | MAJOR_BODY_UNCERTAINTIES['Orcus'] | 3.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 157 | MAJOR_BODY_UNCERTAINTIES['Salacia'] | 5.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 158 | MAJOR_BODY_UNCERTAINTIES['Varuna'] | 5.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 159 | MAJOR_BODY_UNCERTAINTIES['Ixion'] | 5.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 160 | MAJOR_BODY_UNCERTAINTIES['2002 MS4'] | 8.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 161 | MAJOR_BODY_UNCERTAINTIES['Varda'] | 8.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 164 | MAJOR_BODY_UNCERTAINTIES['Moon'] | 0.0001 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 167 | MAJOR_BODY_UNCERTAINTIES['Phobos'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 168 | MAJOR_BODY_UNCERTAINTIES['Deimos'] | 0.02 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 171 | MAJOR_BODY_UNCERTAINTIES['Io'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 172 | MAJOR_BODY_UNCERTAINTIES['Europa'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 173 | MAJOR_BODY_UNCERTAINTIES['Ganymede'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 174 | MAJOR_BODY_UNCERTAINTIES['Callisto'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 175 | MAJOR_BODY_UNCERTAINTIES['Amalthea'] | 0.05 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 176 | MAJOR_BODY_UNCERTAINTIES['Himalia'] | 0.1 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 177 | MAJOR_BODY_UNCERTAINTIES['Thebe'] | 0.05 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 178 | MAJOR_BODY_UNCERTAINTIES['Metis'] | 0.05 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 179 | MAJOR_BODY_UNCERTAINTIES['Adrastea'] | 0.05 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 180 | MAJOR_BODY_UNCERTAINTIES['Pasiphae'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 181 | MAJOR_BODY_UNCERTAINTIES['Sinope'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 182 | MAJOR_BODY_UNCERTAINTIES['Lysithea'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 183 | MAJOR_BODY_UNCERTAINTIES['Carme'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 184 | MAJOR_BODY_UNCERTAINTIES['Ananke'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 185 | MAJOR_BODY_UNCERTAINTIES['Leda'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 186 | MAJOR_BODY_UNCERTAINTIES['Elara'] | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 189 | MAJOR_BODY_UNCERTAINTIES['Mimas'] | 0.05 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 190 | MAJOR_BODY_UNCERTAINTIES['Enceladus'] | 0.05 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 191 | MAJOR_BODY_UNCERTAINTIES['Tethys'] | 0.05 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 192 | MAJOR_BODY_UNCERTAINTIES['Dione'] | 0.05 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 193 | MAJOR_BODY_UNCERTAINTIES['Rhea'] | 0.05 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 194 | MAJOR_BODY_UNCERTAINTIES['Titan'] | 0.05 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 195 | MAJOR_BODY_UNCERTAINTIES['Hyperion'] | 0.1 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 196 | MAJOR_BODY_UNCERTAINTIES['Iapetus'] | 0.1 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 197 | MAJOR_BODY_UNCERTAINTIES['Phoebe'] | 0.2 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 198 | MAJOR_BODY_UNCERTAINTIES['Janus'] | 0.05 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 199 | MAJOR_BODY_UNCERTAINTIES['Epimetheus'] | 0.05 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 200 | MAJOR_BODY_UNCERTAINTIES['Helene'] | 0.1 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 201 | MAJOR_BODY_UNCERTAINTIES['Telesto'] | 0.1 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 202 | MAJOR_BODY_UNCERTAINTIES['Calypso'] | 0.1 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 203 | MAJOR_BODY_UNCERTAINTIES['Atlas'] | 0.05 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 204 | MAJOR_BODY_UNCERTAINTIES['Prometheus'] | 0.05 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 205 | MAJOR_BODY_UNCERTAINTIES['Pandora'] | 0.05 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 206 | MAJOR_BODY_UNCERTAINTIES['Pan'] | 0.05 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 207 | MAJOR_BODY_UNCERTAINTIES['Daphnis'] | 0.05 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 210 | MAJOR_BODY_UNCERTAINTIES['Ariel'] | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 211 | MAJOR_BODY_UNCERTAINTIES['Umbriel'] | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 212 | MAJOR_BODY_UNCERTAINTIES['Titania'] | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 213 | MAJOR_BODY_UNCERTAINTIES['Oberon'] | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 214 | MAJOR_BODY_UNCERTAINTIES['Miranda'] | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 215 | MAJOR_BODY_UNCERTAINTIES['Puck'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 216 | MAJOR_BODY_UNCERTAINTIES['Cordelia'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 217 | MAJOR_BODY_UNCERTAINTIES['Ophelia'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 218 | MAJOR_BODY_UNCERTAINTIES['Bianca'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 219 | MAJOR_BODY_UNCERTAINTIES['Cressida'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 220 | MAJOR_BODY_UNCERTAINTIES['Desdemona'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 221 | MAJOR_BODY_UNCERTAINTIES['Juliet'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 222 | MAJOR_BODY_UNCERTAINTIES['Portia'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 223 | MAJOR_BODY_UNCERTAINTIES['Rosalind'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 224 | MAJOR_BODY_UNCERTAINTIES['Belinda'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 227 | MAJOR_BODY_UNCERTAINTIES['Triton'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 228 | MAJOR_BODY_UNCERTAINTIES['Nereid'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 229 | MAJOR_BODY_UNCERTAINTIES['Proteus'] | 0.8 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 230 | MAJOR_BODY_UNCERTAINTIES['Larissa'] | 0.8 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 231 | MAJOR_BODY_UNCERTAINTIES['Galatea'] | 0.8 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 232 | MAJOR_BODY_UNCERTAINTIES['Despina'] | 0.8 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 233 | MAJOR_BODY_UNCERTAINTIES['Thalassa'] | 0.8 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 234 | MAJOR_BODY_UNCERTAINTIES['Naiad'] | 0.8 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 237 | MAJOR_BODY_UNCERTAINTIES['Charon'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 238 | MAJOR_BODY_UNCERTAINTIES['Nix'] | 2.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 239 | MAJOR_BODY_UNCERTAINTIES['Hydra'] | 2.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 240 | MAJOR_BODY_UNCERTAINTIES['Kerberos'] | 3.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 241 | MAJOR_BODY_UNCERTAINTIES['Styx'] | 3.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 244 | MAJOR_BODY_UNCERTAINTIES['Vesta'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 245 | MAJOR_BODY_UNCERTAINTIES['Pallas'] | 0.05 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 246 | MAJOR_BODY_UNCERTAINTIES['Juno'] | 0.1 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 247 | MAJOR_BODY_UNCERTAINTIES['Hygiea'] | 0.2 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 248 | MAJOR_BODY_UNCERTAINTIES['Davida'] | 0.2 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 249 | MAJOR_BODY_UNCERTAINTIES['Interamnia'] | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 255 | MAJOR_BODY_UNCERTAINTIES['Sylvia'] | 0.2 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 256 | MAJOR_BODY_UNCERTAINTIES['Thisbe'] | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 257 | MAJOR_BODY_UNCERTAINTIES['Camilla'] | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 258 | MAJOR_BODY_UNCERTAINTIES['Herculina'] | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 259 | MAJOR_BODY_UNCERTAINTIES['Doris'] | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 262 | MAJOR_BODY_UNCERTAINTIES['Bennu'] | 0.001 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 263 | MAJOR_BODY_UNCERTAINTIES['Ryugu'] | 0.001 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 264 | MAJOR_BODY_UNCERTAINTIES['Eros'] | 0.001 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 265 | MAJOR_BODY_UNCERTAINTIES['Itokawa'] | 0.001 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 266 | MAJOR_BODY_UNCERTAINTIES['Mathilde'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 267 | MAJOR_BODY_UNCERTAINTIES['Ida'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 268 | MAJOR_BODY_UNCERTAINTIES['Dactyl'] | 0.02 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 269 | MAJOR_BODY_UNCERTAINTIES['Gaspra'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 270 | MAJOR_BODY_UNCERTAINTIES['Lutetia'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 271 | MAJOR_BODY_UNCERTAINTIES['Steins'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 272 | MAJOR_BODY_UNCERTAINTIES['Annefrank'] | 0.05 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 273 | MAJOR_BODY_UNCERTAINTIES['Braille'] | 0.05 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 274 | MAJOR_BODY_UNCERTAINTIES['Toutatis'] | 0.001 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 275 | MAJOR_BODY_UNCERTAINTIES['Didymos'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 276 | MAJOR_BODY_UNCERTAINTIES['Dimorphos'] | 0.02 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 277 | MAJOR_BODY_UNCERTAINTIES['Arrokoth'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 280 | MAJOR_BODY_UNCERTAINTIES['Apophis'] | 0.001 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 281 | MAJOR_BODY_UNCERTAINTIES['2005 YU55'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 282 | MAJOR_BODY_UNCERTAINTIES['1999 JM8'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 283 | MAJOR_BODY_UNCERTAINTIES['2004 BL86'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 284 | MAJOR_BODY_UNCERTAINTIES['2000 DP107'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 285 | MAJOR_BODY_UNCERTAINTIES['1998 KY26'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 286 | MAJOR_BODY_UNCERTAINTIES['2017 YE5'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 287 | MAJOR_BODY_UNCERTAINTIES['1999 KW4'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 288 | MAJOR_BODY_UNCERTAINTIES['2003 YT1'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 289 | MAJOR_BODY_UNCERTAINTIES['2014 HQ124'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 290 | MAJOR_BODY_UNCERTAINTIES['2014 JO25'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 291 | MAJOR_BODY_UNCERTAINTIES['2015 TB145'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 294 | MAJOR_BODY_UNCERTAINTIES['Patroclus'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 295 | MAJOR_BODY_UNCERTAINTIES['Menoetius'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 296 | MAJOR_BODY_UNCERTAINTIES['Eurybates'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 297 | MAJOR_BODY_UNCERTAINTIES['Polymele'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 298 | MAJOR_BODY_UNCERTAINTIES['Leucus'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 299 | MAJOR_BODY_UNCERTAINTIES['Orus'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 300 | MAJOR_BODY_UNCERTAINTIES['Donald Johanso | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 301 | MAJOR_BODY_UNCERTAINTIES['Hektor'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 302 | MAJOR_BODY_UNCERTAINTIES['Agamemnon'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 303 | MAJOR_BODY_UNCERTAINTIES['Achilles'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 304 | MAJOR_BODY_UNCERTAINTIES['Nestor'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 305 | MAJOR_BODY_UNCERTAINTIES['Diomedes'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 308 | MAJOR_BODY_UNCERTAINTIES['Chiron'] | 2.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 309 | MAJOR_BODY_UNCERTAINTIES['Pholus'] | 5.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 310 | MAJOR_BODY_UNCERTAINTIES['Nessus'] | 8.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 311 | MAJOR_BODY_UNCERTAINTIES['Asbolus'] | 8.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 312 | MAJOR_BODY_UNCERTAINTIES['Chariklo'] | 3.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 313 | MAJOR_BODY_UNCERTAINTIES['Hylonome'] | 10.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 314 | MAJOR_BODY_UNCERTAINTIES['Bienor'] | 10.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 315 | MAJOR_BODY_UNCERTAINTIES['Amycus'] | 10.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 318 | MAJOR_BODY_UNCERTAINTIES['Halley'] | 10.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 319 | MAJOR_BODY_UNCERTAINTIES['Encke'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 320 | MAJOR_BODY_UNCERTAINTIES['Tempel 1'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 321 | MAJOR_BODY_UNCERTAINTIES['Wild 2'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 322 | MAJOR_BODY_UNCERTAINTIES['Borrelly'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 323 | MAJOR_BODY_UNCERTAINTIES['Churyumov-Gera | 0.001 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 324 | MAJOR_BODY_UNCERTAINTIES['67P/Churyumov- | 0.001 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 325 | MAJOR_BODY_UNCERTAINTIES['Hartley 2'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 326 | MAJOR_BODY_UNCERTAINTIES['Giacobini-Zinn | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 327 | MAJOR_BODY_UNCERTAINTIES['Grigg-Skjeller | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 328 | MAJOR_BODY_UNCERTAINTIES['Wirtanen'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 329 | MAJOR_BODY_UNCERTAINTIES['Schwassmann-Wa | 2.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 330 | MAJOR_BODY_UNCERTAINTIES['Holmes'] | 5.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 331 | MAJOR_BODY_UNCERTAINTIES['Hale-Bopp'] | 20.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 332 | MAJOR_BODY_UNCERTAINTIES['Hyakutake'] | 15.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 333 | MAJOR_BODY_UNCERTAINTIES['McNaught'] | 10.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 334 | MAJOR_BODY_UNCERTAINTIES['ISON'] | 10.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 335 | MAJOR_BODY_UNCERTAINTIES['Lovejoy'] | 5.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 336 | MAJOR_BODY_UNCERTAINTIES['NEOWISE'] | 3.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 337 | MAJOR_BODY_UNCERTAINTIES['PanSTARRS'] | 5.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 338 | MAJOR_BODY_UNCERTAINTIES['Borisov'] | 10.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 341 | MAJOR_BODY_UNCERTAINTIES['Voyager 1'] | 100.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 342 | MAJOR_BODY_UNCERTAINTIES['Voyager 2'] | 100.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 343 | MAJOR_BODY_UNCERTAINTIES['New Horizons'] | 10.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 344 | MAJOR_BODY_UNCERTAINTIES['Pioneer 10'] | 1000.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 345 | MAJOR_BODY_UNCERTAINTIES['Pioneer 11'] | 1000.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 346 | MAJOR_BODY_UNCERTAINTIES['Cassini'] | 0.1 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 347 | MAJOR_BODY_UNCERTAINTIES['Juno'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 348 | MAJOR_BODY_UNCERTAINTIES['Dawn'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 349 | MAJOR_BODY_UNCERTAINTIES['OSIRIS-REx'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 350 | MAJOR_BODY_UNCERTAINTIES['Hayabusa2'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 351 | MAJOR_BODY_UNCERTAINTIES['Parker Solar P | 0.001 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 352 | MAJOR_BODY_UNCERTAINTIES['Solar Orbiter' | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 353 | MAJOR_BODY_UNCERTAINTIES['BepiColombo'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 354 | MAJOR_BODY_UNCERTAINTIES['JUICE'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 355 | MAJOR_BODY_UNCERTAINTIES['Europa Clipper | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 356 | MAJOR_BODY_UNCERTAINTIES['Lucy'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 357 | MAJOR_BODY_UNCERTAINTIES['Psyche (spacec | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 358 | MAJOR_BODY_UNCERTAINTIES['Dragonfly'] | 0.1 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 361 | MAJOR_BODY_UNCERTAINTIES['Sun'] | 0.001 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 362 | MAJOR_BODY_UNCERTAINTIES['Earth-Moon Bar | 0.0001 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 363 | MAJOR_BODY_UNCERTAINTIES['Pluto-Charon B | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 366 | MAJOR_BODY_UNCERTAINTIES['ISS'] | 0.001 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 367 | MAJOR_BODY_UNCERTAINTIES['HST'] | 0.001 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 368 | MAJOR_BODY_UNCERTAINTIES['JWST'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 369 | MAJOR_BODY_UNCERTAINTIES['Gaia'] | 0.001 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 370 | MAJOR_BODY_UNCERTAINTIES['TESS'] | 0.001 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 371 | MAJOR_BODY_UNCERTAINTIES['Spitzer'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 372 | MAJOR_BODY_UNCERTAINTIES['Kepler'] | 0.01 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 373 | MAJOR_BODY_UNCERTAINTIES['WMAP'] | 0.1 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 374 | MAJOR_BODY_UNCERTAINTIES['Planck'] | 0.1 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 377 | MAJOR_BODY_UNCERTAINTIES['Swift-Tuttle'] | 5.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 378 | MAJOR_BODY_UNCERTAINTIES['Tempel-Tuttle' | 3.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 379 | MAJOR_BODY_UNCERTAINTIES['Thatcher'] | 10.0 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 380 | MAJOR_BODY_UNCERTAINTIES['Phaethon'] | 0.1 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |

### celestial_objects.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 551 | claim: 0.562 AU | 0.562 AU | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 551 | claim: 1.0 AU | 1.0 AU | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 643 | claim: 33 days | 33 days | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |

### comet_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 29 | COMET_NUCLEUS_SIZES['Halley'] | 15 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 30 | COMET_NUCLEUS_SIZES['Hale-Bopp'] | 60 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 31 | COMET_NUCLEUS_SIZES['NEOWISE'] | 5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 32 | COMET_NUCLEUS_SIZES['ISON'] | 2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 33 | COMET_NUCLEUS_SIZES['West'] | 5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 34 | COMET_NUCLEUS_SIZES['Ikeya-Seki'] | 5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 35 | COMET_NUCLEUS_SIZES['Hyakutake'] | 4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 36 | COMET_NUCLEUS_SIZES['Lemmon'] | 3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 37 | COMET_NUCLEUS_SIZES['3I/ATLAS'] | 8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 38 | COMET_NUCLEUS_SIZES['Wierzchos'] | 5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 39 | COMET_NUCLEUS_SIZES['MAPS'] | 0.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 40 | COMET_NUCLEUS_SIZES['Schaumasse'] | 3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 41 | COMET_NUCLEUS_SIZES['Howell'] | 3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 42 | COMET_NUCLEUS_SIZES['Tempel 2'] | 16 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 43 | COMET_NUCLEUS_SIZES['default'] | 5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 64 | 'max_dust_tail_length_mkm' | 10 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 65 | 'max_ion_tail_length_mkm' | 20 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 66 | 'peak_brightness_mag' | -0.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 67 | 'perihelion_distance_au' | 0.586 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 75 | 'max_dust_tail_length_mkm' | 40 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 76 | 'max_ion_tail_length_mkm' | 150 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 77 | 'peak_brightness_mag' | -1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 78 | 'perihelion_distance_au' | 0.914 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 85 | 'max_dust_tail_length_mkm' | 15 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 86 | 'max_ion_tail_length_mkm' | 25 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 87 | 'peak_brightness_mag' | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 88 | 'perihelion_distance_au' | 0.295 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 95 | 'max_dust_tail_length_mkm' | 30 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 96 | 'max_ion_tail_length_mkm' | 50 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 97 | 'peak_brightness_mag' | -3.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 98 | 'perihelion_distance_au' | 0.197 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 105 | 'max_dust_tail_length_mkm' | 25 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 106 | 'max_ion_tail_length_mkm' | 100 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 107 | 'peak_brightness_mag' | -10.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 108 | 'perihelion_distance_au' | 0.008 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 115 | 'max_dust_tail_length_mkm' | 20 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 116 | 'max_ion_tail_length_mkm' | 580 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 117 | 'peak_brightness_mag' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 118 | 'perihelion_distance_au' | 0.23 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 125 | 'max_dust_tail_length_mkm' | 8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 126 | 'max_ion_tail_length_mkm' | 15 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 127 | 'peak_brightness_mag' | 4.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 128 | 'perihelion_distance_au' | 0.53 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 138 | claim: 1.356 AU | 1.356 AU | 3 | 4 | **12** | Sourced but potentially stale | In display string (hover text / INFO) |
| 147 | claim: 129 days | 129 days | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 169 | claim: 5.6 km | 5.6 km | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 175 | claim: 7 deg | 7 deg | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 178 | claim: 0.358 AU | 0.358 AU | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 180 | 'max_dust_tail_length_mkm' | 12 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 181 | 'max_ion_tail_length_mkm' | 25 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 182 | 'peak_brightness_mag' | 9.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 183 | 'perihelion_distance_au' | 1.356 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 194 | 'hyperbolic' | True | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 195 | 'co2_rich' | True | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 196 | 'preliminary_data' | False | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 197 | 'max_active_distance_au' | 5.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 199 | 'anti_tail_length_km' | 400000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 201 | 'anti_tail_collimation' | 0.1 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 202 | 'jet_count' | 4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 206 | 'max_dust_tail_length_mkm' | 5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 207 | 'max_ion_tail_length_mkm' | 12 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 208 | 'peak_brightness_mag' | 6.8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 209 | 'perihelion_distance_au' | 0.562 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 217 | claim: 2 deg | 2 deg | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 222 | 'max_dust_tail_length_mkm' | 20 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 223 | 'max_ion_tail_length_mkm' | 12 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 224 | 'peak_brightness_mag' | -0.6 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 225 | 'perihelion_distance_au' | 0.005729 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 241 | 'post_disintegration_ion_scale' | 0.35 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 243 | 'perihelion_distance_au_activity' | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 244 | 'max_active_distance_au' | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 248 | 'max_dust_tail_length_mkm' | 2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 249 | 'max_ion_tail_length_mkm' | 5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 250 | 'peak_brightness_mag' | 9.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 251 | 'perihelion_distance_au' | 1.18 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 259 | 'max_dust_tail_length_mkm' | 2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 260 | 'max_ion_tail_length_mkm' | 4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 261 | 'peak_brightness_mag' | 10.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 262 | 'perihelion_distance_au' | 1.41 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 270 | 'max_dust_tail_length_mkm' | 3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 271 | 'max_ion_tail_length_mkm' | 6 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 272 | 'peak_brightness_mag' | 8.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 273 | 'perihelion_distance_au' | 1.42 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 281 | 'max_dust_tail_length_mkm' | 10 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 282 | 'max_ion_tail_length_mkm' | 20 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 283 | 'peak_brightness_mag' | 3.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 284 | 'perihelion_distance_au' | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1062 | claim: 120 deg | 120 deg | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 1064 | claim: 000 km | 000 km | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 1065 | claim: 20 deg | 20 deg | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 1444 | COMET_FEATURE_THRESHOLDS['coma'] | 5.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1445 | COMET_FEATURE_THRESHOLDS['dust_tail'] | 3.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1446 | COMET_FEATURE_THRESHOLDS['ion_tail'] | 2.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1526 | features_visible['nucleus'] | True | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1860 | params['a'] | 104.9899273 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1860 | params['e'] | 0.999945 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1861 | params['i'] | 144.49 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1861 | params['omega'] | 86.33 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1861 | params['Omega'] | 7.87 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1862 | params['TP'] | 2461135.0997 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |

### constants_new.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 757 | claim: 28 minutes | 28 minutes | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 787 | claim: 60 years | 60 years | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 787 | claim: 60 years | 60 years | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 1182 | claim: 0.5 AU | 0.5 AU | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 1305 | claim: 15 deg | 15 deg | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 1691 | claim: 5 AU | 5 AU | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 1697 | claim: 5.50 year | 5.50 year | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 1699 | claim: 25 km | 25 km | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 1854 | claim: 440 km | 440 km | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 1854 | claim: 296 km | 296 km | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 1855 | claim: 295 km | 295 km | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 1907 | claim: 1.5 AU | 1.5 AU | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 2216 | claim: 0.336 AU | 0.336 AU | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 2228 | claim: 0.334 AU | 0.334 AU | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 2237 | claim: 000 km | 000 km | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 2382 | claim: 6 hours | 6 hours | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 2383 | claim: 1.23 solar radii | 1.23 solar radii | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 2383 | claim: 000 km | 000 km | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 2436 | claim: 350 years | 350 years | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 2437 | claim: 150 years | 150 years | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 2464 | claim: 10 km | 10 km | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 58 | CENTER_BODY_RADII['Earth'] | 6371 | 2 | 5 | **10** | Has source citation | Imported by 14 modules |
| 59 | CENTER_BODY_RADII['Moon'] | 1737 | 2 | 5 | **10** | Has source citation | Imported by 14 modules |
| 60 | CENTER_BODY_RADII['Mars'] | 3396.2 | 2 | 5 | **10** | Has source citation | Imported by 14 modules |
| 61 | CENTER_BODY_RADII['Jupiter'] | 71492 | 2 | 5 | **10** | Has source citation | Imported by 14 modules |
| 62 | CENTER_BODY_RADII['Saturn'] | 58232 | 2 | 5 | **10** | Has source citation | Imported by 14 modules |
| 89 | KNOWN_ORBITAL_PERIODS['Phobos'] | 0.319 | 2 | 5 | **10** | Has source citation | Imported by 14 modules |
| 90 | KNOWN_ORBITAL_PERIODS['Deimos'] | 1.263 | 2 | 5 | **10** | Has source citation | Imported by 14 modules |
| 149 | KNOWN_ORBITAL_PERIODS['Xiangliu'] | 25.22 | 2 | 5 | **10** | Has source citation | Imported by 14 modules |
| 152 | KNOWN_ORBITAL_PERIODS['Vanth'] | 9.54 | 2 | 5 | **10** | Has source citation | Imported by 14 modules |
| 155 | KNOWN_ORBITAL_PERIODS['Weywot'] | 12.44 | 2 | 5 | **10** | Has source citation | Imported by 14 modules |
| 162 | KNOWN_ORBITAL_PERIODS['MK2'] | 18.0 | 2 | 5 | **10** | Has source citation | Imported by 14 modules |

### coordinate_system_guide.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 240 | 'responsive' | True | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 240 | 'displayModeBar' | True | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |

### earth_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 33 | layer_info['radius_fraction'] | 0.19 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 35 | layer_info['opacity'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 89 | layer_info['radius_fraction'] | 0.55 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 91 | layer_info['opacity'] | 0.8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 144 | layer_info['radius_fraction'] | 0.85 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 146 | layer_info['opacity'] | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 198 | layer_info['radius_fraction'] | 0.98 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 200 | layer_info['opacity'] | 0.6 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 252 | layer_info['radius_fraction'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 254 | layer_info['opacity'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 409 | layer_info['radius_fraction'] | 1.05 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 411 | layer_info['opacity'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 464 | layer_info['radius_fraction'] | 1.25 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 466 | layer_info['opacity'] | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 539 | params['sunward_distance'] | 10 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 542 | params['equatorial_radius'] | 12 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 543 | params['polar_radius'] | 10 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 546 | params['tail_length'] | 100 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 547 | params['tail_base_radius'] | 15 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 548 | params['tail_end_radius'] | 25 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 551 | params['inner_belt_distance'] | 1.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 552 | params['outer_belt_distance'] | 4.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 553 | params['belt_thickness'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 844 | claim: 013 km | 013 km | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 844 | claim: 150 km | 150 km | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 845 | claim: 000 km | 000 km | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |

### energy_imbalance.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 136 | 'secondary_y' | True | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 143 | 'start' | 2006.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 143 | 'end' | 2007.2 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 148 | 'start' | 2007.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 148 | 'end' | 2008.2 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 153 | 'start' | 2009.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 153 | 'end' | 2010.3 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 158 | 'start' | 2010.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 158 | 'end' | 2012.2 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 163 | 'start' | 2015.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 163 | 'end' | 2016.3 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 168 | 'start' | 2016.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 168 | 'end' | 2017.2 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 174 | 'start' | 2020.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 174 | 'end' | 2023.3 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 179 | 'start' | 2023.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 179 | 'end' | 2024.3 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 489 | 'x' | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 491 | 'size' | 18 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |

### eris_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 32 | layer_info['radius_fraction'] | 0.6 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 34 | layer_info['opacity'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 111 | layer_info['radius_fraction'] | 0.66 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 113 | layer_info['opacity'] | 0.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 167 | layer_info['radius_fraction'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 169 | layer_info['opacity'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 331 | layer_info['radius_fraction'] | 1.005 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 333 | layer_info['opacity'] | 0.1 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 414 | layer_info['radius_fraction'] | 6965 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 416 | layer_info['opacity'] | 0.25 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |

### exoplanet_orbits.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 276 | 'phase' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 282 | 'phase' | 180.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |

### fetch_climate_data.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 231 | 'pre_industrial_ph' | 8.2 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |
| 232 | 'current_decline' | 0.1 | 4 | 3 | **12** | No source citation (recalled) | Value in computation module |

### hr_diagram_apparent_magnitude.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 437 | flattened_analysis['temp_le_zero'] | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |

### hr_diagram_distance.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 448 | flattened_analysis['temp_le_zero'] | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |

### jupiter_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 73 | layer_info['radius_fraction'] | 0.1 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 75 | layer_info['opacity'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 127 | layer_info['radius_fraction'] | 0.8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 129 | layer_info['opacity'] | 0.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 182 | layer_info['radius_fraction'] | 0.97 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 184 | layer_info['opacity'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 240 | layer_info['radius_fraction'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 242 | layer_info['opacity'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 401 | layer_info['radius_fraction'] | 1.1 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 403 | layer_info['opacity'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 457 | params['sunward_distance'] | 50 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 460 | params['equatorial_radius'] | 100 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 461 | params['polar_radius'] | 80 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 464 | params['tail_length'] | 500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 465 | params['tail_base_radius'] | 150 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 466 | params['tail_end_radius'] | 200 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 697 | layer_info['radius_fraction'] | 740 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 699 | layer_info['opacity'] | 0.25 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 791 | 'inner_radius_km' | 122500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 792 | 'outer_radius_km' | 129000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 793 | 'thickness_km' | 30 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 795 | 'opacity' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 806 | 'inner_radius_km' | 100000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 807 | 'outer_radius_km' | 122500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 808 | 'thickness_km' | 12500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 810 | 'opacity' | 0.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 821 | 'inner_radius_km' | 129000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 822 | 'outer_radius_km' | 182000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 823 | 'thickness_km' | 2000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 825 | 'opacity' | 0.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 835 | 'inner_radius_km' | 129000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 836 | 'outer_radius_km' | 226000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 837 | 'thickness_km' | 8600 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 839 | 'opacity' | 0.15 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |

### mars_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 30 | layer_info['radius_fraction'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 32 | layer_info['opacity'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 108 | layer_info['radius_fraction'] | 0.8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 110 | layer_info['opacity'] | 0.8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 177 | layer_info['radius_fraction'] | 0.98 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 179 | layer_info['opacity'] | 0.6 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 232 | layer_info['radius_fraction'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 234 | layer_info['opacity'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 390 | layer_info['radius_fraction'] | 1.02 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 392 | layer_info['opacity'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 458 | layer_info['radius_fraction'] | 1.06 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 460 | layer_info['opacity'] | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 534 | params['sunward_distance'] | 1.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 537 | params['equatorial_radius'] | 2.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 538 | params['polar_radius'] | 1.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 541 | params['tail_length'] | 10.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 542 | params['tail_base_radius'] | 2.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 543 | params['tail_end_radius'] | 4.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 755 | layer_info['radius_fraction'] | 324.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 757 | layer_info['opacity'] | 0.15 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |

### mercury_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 32 | layer_info['radius_fraction'] | 0.41 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 34 | layer_info['opacity'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 83 | layer_info['radius_fraction'] | 0.85 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 85 | layer_info['opacity'] | 0.8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 134 | layer_info['radius_fraction'] | 0.98 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 136 | layer_info['opacity'] | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 188 | layer_info['radius_fraction'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 190 | layer_info['opacity'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 343 | layer_info['radius_fraction'] | 2.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 345 | layer_info['opacity'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 540 | params['sunward_distance'] | 10 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 543 | params['equatorial_radius'] | 12 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 544 | params['polar_radius'] | 10 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 547 | params['tail_length'] | 100 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 548 | params['tail_base_radius'] | 15 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 549 | params['tail_end_radius'] | 25 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |

### moon_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 29 | layer_info['radius_fraction'] | 0.1485 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 31 | layer_info['opacity'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 81 | layer_info['radius_fraction'] | 0.2083 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 83 | layer_info['opacity'] | 0.8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 143 | layer_info['radius_fraction'] | 0.85 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 145 | layer_info['opacity'] | 0.9655 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 217 | layer_info['radius_fraction'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 219 | layer_info['opacity'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 400 | layer_info['radius_fraction'] | 1.06 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 402 | layer_info['opacity'] | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |

### neptune_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 33 | layer_info['radius_fraction'] | 0.25 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 35 | layer_info['opacity'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 90 | layer_info['radius_fraction'] | 0.85 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 92 | layer_info['opacity'] | 0.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 161 | layer_info['radius_fraction'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 163 | layer_info['opacity'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 330 | layer_info['radius_fraction'] | 1.01 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 332 | layer_info['opacity'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 423 | params['sunward_distance'] | 34 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 426 | params['equatorial_radius'] | 40 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 427 | params['polar_radius'] | 25 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 430 | params['tail_length'] | 600 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 431 | params['tail_base_radius'] | 60 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 432 | params['tail_end_radius'] | 120 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 807 | 'distance' | 1.8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 808 | 'thickness' | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 810 | 'opacity' | 0.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 829 | 'distance' | 3.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 830 | 'thickness' | 0.6 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 832 | 'opacity' | 0.35 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 851 | 'distance' | 6.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 852 | 'thickness' | 0.8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 854 | 'opacity' | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 873 | 'distance' | 4.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 874 | 'thickness' | 0.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 876 | 'opacity' | 0.25 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 877 | 'variable_offset' | True | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1195 | 'inner_radius_km' | 41900 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1196 | 'outer_radius_km' | 42900 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1197 | 'thickness_km' | 15 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1199 | 'opacity' | 0.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1224 | 'inner_radius_km' | 53200 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1225 | 'outer_radius_km' | 53200 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1226 | 'thickness_km' | 110 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1228 | 'opacity' | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1253 | 'inner_radius_km' | 55400 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1254 | 'outer_radius_km' | 57600 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1255 | 'thickness_km' | 4000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1257 | 'opacity' | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1282 | 'inner_radius_km' | 57600 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1283 | 'outer_radius_km' | 57600 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1284 | 'thickness_km' | 100 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1286 | 'opacity' | 0.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1310 | 'inner_radius_km' | 62932 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1311 | 'outer_radius_km' | 62932 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1312 | 'thickness_km' | 50 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1314 | 'opacity' | 0.6 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1340 | 'inner_radius_km' | 62932 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1341 | 'outer_radius_km' | 62932 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1342 | 'thickness_km' | 50 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1343 | 'arc_length' | 4.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1344 | 'arc_center' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1346 | 'opacity' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1371 | 'inner_radius_km' | 62932 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1372 | 'outer_radius_km' | 62932 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1373 | 'thickness_km' | 50 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1374 | 'arc_length' | 4.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1375 | 'arc_center' | 8.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1377 | 'opacity' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1402 | 'inner_radius_km' | 62932 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1403 | 'outer_radius_km' | 62932 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1404 | 'thickness_km' | 50 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1405 | 'arc_length' | 4.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1406 | 'arc_center' | 14.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1408 | 'opacity' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1433 | 'inner_radius_km' | 62932 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1434 | 'outer_radius_km' | 62932 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1435 | 'thickness_km' | 50 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1436 | 'arc_length' | 4.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1437 | 'arc_center' | 22.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1439 | 'opacity' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1464 | 'inner_radius_km' | 62932 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1465 | 'outer_radius_km' | 62932 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1466 | 'thickness_km' | 50 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1467 | 'arc_length' | 9.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1468 | 'arc_center' | 40.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1470 | 'opacity' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1495 | 'inner_radius_km' | 67500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1496 | 'outer_radius_km' | 73000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1497 | 'thickness_km' | 2000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1499 | 'opacity' | 0.1 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1671 | layer_info['radius_fraction'] | 4685 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1673 | layer_info['opacity'] | 0.25 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |

### orbital_elements.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 53 | 'omega' | 29.19879045729881 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 54 | 'Omega' | 48.29886557533597 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 56 | 'TP' | 2461002.976715519 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 64 | 'omega' | 54.852 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 65 | 'Omega' | 76.67984255 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 67 | 'TP' | 2460522.892 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 77 | 'omega' | 126.394 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 78 | 'Omega' | 204.061 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 80 | 'TP' | 2460719.3535595234 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 89 | 'omega' | 102.93768193 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 90 | 'Omega' | 0.0 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 92 | 'TP' | 2460677.413 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 102 | 'a' | 1.00102447694204 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 103 | 'e' | 0.1040534310625292 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 112 | 'a' | 1.004188800489803 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 113 | 'e' | 0.1071782474710749 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 125 | 'a' | 1.012228628670663 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 126 | 'e' | 0.02141074038624791 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 135 | 'a' | 1.078452460125784 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 136 | 'e' | 0.2233327947850885 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 138 | 'omega' | 267.1185311148099 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 139 | 'Omega' | 145.4731476162657 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 141 | 'TP' | 2460976.57565256 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 142 | 'Tapo' | 2461185.0875 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 161 | 'omega' | 211.421 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 162 | 'Omega' | 251.617 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 164 | 'TP' | 2460643.5508 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 190 | 'a' | 2.421098478271158 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 191 | 'e' | 0.6939958024514898 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 193 | 'omega' | 244.5179261214832 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 194 | 'Omega' | 335.4879825233473 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 201 | 'a' | 2.516308070047454 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 202 | 'e' | 0.6615999301423001 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 204 | 'omega' | 134.3644983455991 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 205 | 'Omega' | 271.3674693540159 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 207 | 'TP' | 2462115.7385 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 218 | 'omega' | 178.817 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 219 | 'Omega' | 304.435 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 221 | 'TP' | 2460445.7223 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 230 | 'omega' | 286.502 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 231 | 'Omega' | 49.55953891 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 233 | 'TP' | 2460587.648 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 250 | 'omega' | 151.216 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 251 | 'Omega' | 103.851 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 253 | 'TP' | 2460902.9691 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 288 | 'omega' | 73.597 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 289 | 'Omega' | 80.393 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 291 | 'TP' | 2461601.434 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 409 | 'a' | 17.85950919 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 410 | 'e' | 0.9678338727 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 412 | 'omega' | 112.497549 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 413 | 'Omega' | 59.59944738 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 415 | 'TP' | 2474058.2779978146 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 416 | 'Tapo' | 2460856.0 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 503 | 'omega' | 97.286 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 504 | 'Omega' | 97.286 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 512 | 'omega' | 240.2 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 513 | 'Omega' | 122.1 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 515 | 'TP' | 2500289.4542 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 532 | 'omega' | 176.1507602341478 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 533 | 'Omega' | 158.939446659904 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 541 | 'omega' | 295.7568523219785 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 542 | 'Omega' | 79.60732027458391 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 544 | 'TP' | 2520030.5498 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 552 | 'omega' | 207.2059900430104 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 553 | 'Omega' | 336.8262717815297 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 576 | 'a' | 89.88 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 577 | 'e' | 0.99994 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 579 | 'omega' | 87.97 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 580 | 'Omega' | 9.28 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 581 | 'MA' | 359.907 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 583 | 'TP' | 2461134.92 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 589 | 'a' | 109.4482298572126 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 590 | 'e' | 0.9999501049489632 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 592 | 'omega' | 86.48357844330381 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 593 | 'Omega' | 7.887906287190159 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 596 | 'TP' | 2461135.0670770155 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 603 | 'a' | 122.0093217668137 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 604 | 'e' | 0.9956568328248036 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 606 | 'omega' | 132.9672366055109 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 607 | 'Omega' | 108.0976178317535 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 609 | 'TP' | 2460988.037351267 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 626 | 'a' | 250.0679474237761 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 627 | 'e' | 0.7370249039390946 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 629 | 'omega' | 199.2155526048832 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 630 | 'Omega' | 72.0885184764268 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 632 | 'TP' | 2474830.2565151933 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 649 | 'omega' | 311.5908685997484 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 650 | 'Omega' | 144.4059276991507 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 652 | 'TP' | 2479072.5781 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 668 | 'a' | 798.2574580972854 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 669 | 'e' | 0.9993692862141036 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 671 | 'omega' | 307.7690351733913 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 672 | 'Omega' | 335.6745583920674 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 674 | 'TP' | 2460931.1155318194 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 682 | 'omega' | 338.23502348994 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 683 | 'Omega' | 328.5637374192406 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 688 | 'a' | 1062.136603634751 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 689 | 'e' | 0.9390574940805684 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 737 | 'a' | -0.263886128382535 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 738 | 'e' | 6.140504247361179 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 740 | 'omega' | 127.9946584112738 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 741 | 'Omega' | 322.1578351010177 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 743 | 'TP' | 2460977.9743218264 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 749 | 'a' | -48.28030957635523 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 750 | 'e' | 1.009582732034413 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 753 | 'Omega' | 91.89902555608872 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 757 | 'TP' | 2460996.03037356 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 762 | 'a' | -1328.874007526048 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 763 | 'e' | 1.000251464554613 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 766 | 'Omega' | 97.55648983040697 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 770 | 'TP' | 2460955.5 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 776 | 'a' | -1517.905498054856 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 777 | 'e' | 1.000328480251838 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 779 | 'omega' | 162.226608108783 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 780 | 'Omega' | 38.69210120731782 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 782 | 'TP' | 2461150.396752224 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 788 | 'a' | -4088.071955049762 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 789 | 'e' | 1.0000957494372 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 791 | 'omega' | 308.491702255918 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 792 | 'Omega' | 21.55947211343556 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 794 | 'TP' | 2460581.240799256 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 799 | 'a' | -7606.45306976526 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 800 | 'e' | 1.000012291218472 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 802 | 'omega' | 108.1253732077035 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 803 | 'Omega' | 220.3320911080488 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 805 | 'TP' | 2460688.9243240277 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 820 | 'a' | -10594.89311322137 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 821 | 'e' | 1.000053413285714 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 823 | 'omega' | 243.6365239065296 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 824 | 'Omega' | 108.0828131320636 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 826 | 'TP' | 2461061.262214219 | 3 | 5 | **15** | Sourced but potentially stale | Imported by 4 modules |
| 1351 | 'a' | 8.89e-05 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 1352 | 'e' | 0.011 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 1353 | 'i' | 15.0 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 1354 | 'omega' | 0.0 | 3 | 5 | **15** | No source, contains date-sensitive claims | Imported by 4 modules |
| 74 | 'a' | 0.922583 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 75 | 'e' | 0.191481 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 76 | 'i' | 3.331 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 104 | 'i' | 7.773894173631178 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 105 | 'omega' | 307.0951007739783 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 106 | 'Omega' | 66.43991583004482 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 114 | 'i' | 1.984028877925589 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 115 | 'omega' | 82.04919713631394 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 116 | 'Omega' | 113.0180181480993 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 118 | 'TP' | 2460048.1958280094 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 127 | 'i' | 1.518377382131216 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 128 | 'omega' | 116.8074860094156 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 129 | 'Omega' | 305.1069316209851 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 137 | 'i' | 4.573408702272091 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 192 | 'i' | 0.9861902430422796 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 203 | 'i' | 3.408259321981154 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 276 | 'a' | 2.434591597038037 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 277 | 'e' | 0.1644174522633922 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 278 | 'i' | 3.063715677953934 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 279 | 'omega' | 249.980528664283 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 280 | 'Omega' | 80.87713180326485 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 298 | 'a' | 5.12481038867513 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 299 | 'e' | 0.03658969107145676 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 300 | 'i' | 8.468402951870347 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 301 | 'omega' | 179.5712820784224 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 302 | 'Omega' | 258.5587182277959 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 307 | 'a' | 5.183610039255559 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 308 | 'e' | 0.09688597854047172 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 309 | 'i' | 12.98094196026331 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 310 | 'omega' | 5.149831531818331 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 311 | 'Omega' | 50.31413377311653 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 327 | 'a' | 5.209549873585049 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 328 | 'e' | 0.0911999243850036 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 329 | 'i' | 8.054169046592317 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 330 | 'omega' | 27.83332476783044 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 331 | 'Omega' | 43.54011293260102 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 339 | 'a' | 5.212775041416492 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 340 | 'e' | 0.1394751648774633 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 341 | 'i' | 22.05719641611838 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 342 | 'omega' | 307.9473718922942 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 343 | 'Omega' | 44.3495507311498 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 345 | 'TP' | 2460486.237046778 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 364 | 'a' | 5.2899315120334 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 365 | 'e' | 0.06389742479789216 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 366 | 'i' | 11.55528566945522 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 367 | 'omega' | 160.4023262565797 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 368 | 'Omega' | 251.0747114724082 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 375 | 'a' | 3.462249489765068 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 376 | 'e' | 0.6409081306555051 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 377 | 'i' | 7.040294906760007 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 378 | 'omega' | 12.79824973415729 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 379 | 'Omega' | 50.13557380441372 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 381 | 'TP' | 2457247.5886578634 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 411 | 'i' | 162.1475927 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 567 | 'a' | 91.59999999999813 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 568 | 'e' | 0.999915 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 569 | 'i' | 141.8642 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 570 | 'omega' | 69.0486 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 571 | 'Omega' | 346.9947 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 578 | 'i' | 144.51 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 591 | 'i' | 144.5100163985513 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 605 | 'i' | 143.6632748988036 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 614 | 'a' | 177.4333839117583 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 615 | 'e' | 0.9949810027633206 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 616 | 'i' | 89.28759424740302 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 617 | 'omega' | 130.4146670659176 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 618 | 'Omega' | 282.7334213961641 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 620 | 'TP' | 2450537.134907144 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 637 | 'a' | 358.4679565529321 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 638 | 'e' | 0.9991780262531292 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 639 | 'i' | 128.9375027594809 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 640 | 'omega' | 37.2786584481257 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 641 | 'Omega' | 61.01042818536988 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 670 | 'i' | 4.470167090495599 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 699 | 'a' | 2124.755444396066 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 700 | 'e' | 0.9998916470450124 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 701 | 'i' | 124.9220493922234 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 702 | 'omega' | 130.1751209780967 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 703 | 'Omega' | 188.045131992156 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 705 | 'TP' | 2450204.8941449965 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 714 | 'a' | -0.8514922551937886 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 715 | 'e' | 3.356475782676596 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 716 | 'i' | 44.05264247909138 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 717 | 'omega' | 209.1236864378081 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 718 | 'Omega' | 308.1477292269942 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 720 | 'TP' | 2458826.052845906 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 725 | 'a' | -1.27234500742808 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 726 | 'e' | 1.201133796102373 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 727 | 'i' | 122.7417062847286 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 728 | 'omega' | 241.8105360304898 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 729 | 'Omega' | 24.59690955523242 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 731 | 'TP' | 2458006.0073213754 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 739 | 'i' | 175.1131164859007 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 751 | 'i' | 112.7242744491862 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 752 | 'omega' | 47.54446487656067 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 764 | 'i' | 147.864867556013 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 765 | 'omega' | 271.0285208159306 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 778 | 'i' | 124.7293449694749 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 790 | 'i' | 139.1121557652439 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 801 | 'i' | 116.8510954925091 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 809 | 'a' | -9074.061068728695 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 810 | 'e' | 1.000018815882278 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 811 | 'i' | 77.83700054890942 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 812 | 'omega' | 155.9749681149126 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 813 | 'Omega' | 267.4148026435385 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 815 | 'TP' | 2454113.298843633 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 822 | 'i' | 75.23843302846508 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 831 | 'a' | -12220.2703313635 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 832 | 'e' | 1.000016087612074 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 833 | 'i' | 43.07404350452942 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 834 | 'omega' | 358.4317208087168 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 835 | 'Omega' | 118.9175346769632 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 837 | 'TP' | 2442833.7219778746 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 845 | 'a' | 0.00257 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 846 | 'e' | 0.0549 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 847 | 'i' | 5.145 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 848 | 'omega' | 318.15 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 849 | 'Omega' | 125.08 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 862 | 'omega' | 216.3 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 863 | 'Omega' | 169.2 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 873 | 'omega' | 0 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 874 | 'Omega' | 54.4 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |

### paleoclimate_dual_scale.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 38 | 'start' | 4500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 38 | 'end' | 4000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 39 | 'start' | 4000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 39 | 'end' | 2500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 40 | 'start' | 2500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 40 | 'end' | 541 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 43 | 'start' | 541 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 43 | 'end' | 485.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 44 | 'start' | 485.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 44 | 'end' | 443.8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 45 | 'start' | 443.8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 45 | 'end' | 419.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 46 | 'start' | 419.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 46 | 'end' | 358.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 47 | 'start' | 358.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 47 | 'end' | 298.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 48 | 'start' | 298.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 48 | 'end' | 252.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 51 | 'start' | 252.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 51 | 'end' | 201.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 52 | 'start' | 201.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 52 | 'end' | 145.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 58 | 'start' | 33.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 58 | 'end' | 23.03 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 59 | 'start' | 23.03 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 59 | 'end' | 5.333 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 60 | 'start' | 5.333 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 60 | 'end' | 2.58 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 61 | 'start' | 2.58 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 61 | 'end' | 0.0117 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 170 | 'width' | 2.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 179 | 'width' | 2.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 188 | 'width' | 2.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 197 | 'width' | 2.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 206 | 'width' | 2.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 969 | 'x' | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 971 | 'size' | 18 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |

### paleoclimate_human_origins_full.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 34 | 'start' | 4500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 34 | 'end' | 4000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 35 | 'start' | 4000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 35 | 'end' | 2500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 36 | 'start' | 2500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 36 | 'end' | 541 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 39 | 'start' | 541 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 39 | 'end' | 485.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 40 | 'start' | 485.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 40 | 'end' | 443.8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 41 | 'start' | 443.8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 41 | 'end' | 419.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 42 | 'start' | 419.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 42 | 'end' | 358.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 43 | 'start' | 358.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 43 | 'end' | 298.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 44 | 'start' | 298.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 44 | 'end' | 252.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 47 | 'start' | 252.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 47 | 'end' | 201.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 48 | 'start' | 201.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 48 | 'end' | 145.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 54 | 'start' | 33.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 54 | 'end' | 23.03 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 55 | 'start' | 23.03 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 55 | 'end' | 5.333 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 56 | 'start' | 5.333 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 56 | 'end' | 2.58 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 57 | 'start' | 2.58 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 57 | 'end' | 0.0117 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 58 | 'start' | 0.0117 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 58 | 'end' | 1e-06 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 92 | 'age_ma' | 21 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 93 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 95 | 'age_ma' | 20.6 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 96 | 'y_offset' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 100 | 'age_ma' | 7.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 101 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 103 | 'age_ma' | 6.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 104 | 'y_offset' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 106 | 'age_ma' | 5.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 107 | 'y_offset' | 1.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 109 | 'age_ma' | 4.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 110 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 114 | 'age_ma' | 4.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 115 | 'y_offset' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 117 | 'age_ma' | 3.85 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 118 | 'y_offset' | 1.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 120 | 'age_ma' | 3.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 121 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 125 | 'age_ma' | 2.8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 126 | 'y_offset' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 128 | 'age_ma' | 2.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 129 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 131 | 'age_ma' | 1.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 132 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 134 | 'age_ma' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 135 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 137 | 'age_ma' | 0.43 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 138 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 140 | 'age_ma' | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 141 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 143 | 'age_ma' | 0.315 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 144 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 146 | 'age_ma' | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 147 | 'y_offset' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 151 | 'age_ma' | 0.19 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 152 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 154 | 'age_ma' | 0.067 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 155 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 163 | 'age_ma' | 2.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 164 | 'y_offset' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 166 | 'age_ma' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 167 | 'y_offset' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 169 | 'age_ma' | 1.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 170 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 172 | 'age_ma' | 1.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 173 | 'y_offset' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 177 | 'age_ma' | 0.28 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 178 | 'y_offset' | 1.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 180 | 'age_ma' | 0.15 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 181 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 199 | 'start_ma' | 0.014 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 199 | 'end_ma' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 201 | 'start_ma' | 0.029 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 201 | 'end_ma' | 0.014 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 203 | 'start_ma' | 0.057 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 203 | 'end_ma' | 0.029 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 205 | 'start_ma' | 0.071 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 205 | 'end_ma' | 0.057 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 209 | 'start_ma' | 0.13 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 209 | 'end_ma' | 0.071 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 211 | 'start_ma' | 0.13 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 211 | 'end_ma' | 0.115 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 215 | 'start_ma' | 0.191 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 215 | 'end_ma' | 0.13 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 217 | 'start_ma' | 0.243 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 217 | 'end_ma' | 0.191 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 219 | 'start_ma' | 0.424 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 219 | 'end_ma' | 0.374 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 221 | 'start_ma' | 0.478 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 221 | 'end_ma' | 0.424 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 227 | 'age_ma' | 0.074 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 229 | 'age_ma' | 0.125 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 231 | 'age_ma' | 0.009 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 500 | 'secondary_y' | True | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1242 | 'start' | 4500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1242 | 'end' | 541 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1243 | 'start' | 541 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1243 | 'end' | 252.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1244 | 'start' | 252.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1244 | 'end' | 66.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1245 | 'start' | 66.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1245 | 'end' | 1e-06 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 2010 | 'x' | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 2012 | 'size' | 18 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |

### paleoclimate_visualization.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 31 | 'start' | 4500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 31 | 'end' | 4000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 32 | 'start' | 4000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 32 | 'end' | 2500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 33 | 'start' | 2500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 33 | 'end' | 541 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 36 | 'start' | 541 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 36 | 'end' | 485.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 37 | 'start' | 485.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 37 | 'end' | 443.8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 38 | 'start' | 443.8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 38 | 'end' | 419.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 39 | 'start' | 419.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 39 | 'end' | 358.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 40 | 'start' | 358.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 40 | 'end' | 298.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 41 | 'start' | 298.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 41 | 'end' | 252.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 44 | 'start' | 252.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 44 | 'end' | 201.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 45 | 'start' | 201.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 45 | 'end' | 145.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 51 | 'start' | 33.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 51 | 'end' | 23.03 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 52 | 'start' | 23.03 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 52 | 'end' | 5.333 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 53 | 'start' | 5.333 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 53 | 'end' | 2.58 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 54 | 'start' | 2.58 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 54 | 'end' | 0.0117 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 55 | 'start' | 0.0117 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 55 | 'end' | 1e-06 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 241 | 'secondary_y' | True | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 379 | 'start' | 4500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 379 | 'end' | 541 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 380 | 'start' | 541 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 380 | 'end' | 252.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 381 | 'start' | 252.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 381 | 'end' | 66.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 382 | 'start' | 66.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 382 | 'end' | 1e-06 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 507 | 'x' | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 509 | 'size' | 18 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |

### paleoclimate_visualization_full.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 34 | 'start' | 4500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 34 | 'end' | 4000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 35 | 'start' | 4000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 35 | 'end' | 2500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 36 | 'start' | 2500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 36 | 'end' | 541 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 39 | 'start' | 541 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 39 | 'end' | 485.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 40 | 'start' | 485.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 40 | 'end' | 443.8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 41 | 'start' | 443.8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 41 | 'end' | 419.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 42 | 'start' | 419.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 42 | 'end' | 358.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 43 | 'start' | 358.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 43 | 'end' | 298.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 44 | 'start' | 298.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 44 | 'end' | 252.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 47 | 'start' | 252.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 47 | 'end' | 201.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 48 | 'start' | 201.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 48 | 'end' | 145.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 54 | 'start' | 33.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 54 | 'end' | 23.03 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 55 | 'start' | 23.03 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 55 | 'end' | 5.333 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 56 | 'start' | 5.333 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 56 | 'end' | 2.58 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 57 | 'start' | 2.58 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 57 | 'end' | 0.0117 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 58 | 'start' | 0.0117 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 58 | 'end' | 1e-06 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 326 | 'secondary_y' | True | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 813 | 'start' | 4500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 813 | 'end' | 541 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 814 | 'start' | 541 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 814 | 'end' | 252.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 815 | 'start' | 252.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 815 | 'end' | 66.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 816 | 'start' | 66.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 816 | 'end' | 1e-06 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1581 | 'x' | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1583 | 'size' | 18 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |

### paleoclimate_wet_bulb_full.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 33 | 'start' | 4500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 33 | 'end' | 4000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 34 | 'start' | 4000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 34 | 'end' | 2500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 35 | 'start' | 2500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 35 | 'end' | 541 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 38 | 'start' | 541 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 38 | 'end' | 485.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 39 | 'start' | 485.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 39 | 'end' | 443.8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 40 | 'start' | 443.8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 40 | 'end' | 419.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 41 | 'start' | 419.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 41 | 'end' | 358.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 42 | 'start' | 358.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 42 | 'end' | 298.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 43 | 'start' | 298.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 43 | 'end' | 252.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 46 | 'start' | 252.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 46 | 'end' | 201.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 47 | 'start' | 201.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 47 | 'end' | 145.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 53 | 'start' | 33.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 53 | 'end' | 23.03 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 54 | 'start' | 23.03 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 54 | 'end' | 5.333 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 55 | 'start' | 5.333 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 55 | 'end' | 2.58 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 56 | 'start' | 2.58 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 56 | 'end' | 0.0117 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 57 | 'start' | 0.0117 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 57 | 'end' | 1e-07 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 63 | 'age_ma' | 21 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 63 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 65 | 'age_ma' | 20.6 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 65 | 'y_offset' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 67 | 'age_ma' | 7.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 67 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 69 | 'age_ma' | 6.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 69 | 'y_offset' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 71 | 'age_ma' | 5.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 71 | 'y_offset' | 1.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 73 | 'age_ma' | 4.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 73 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 75 | 'age_ma' | 4.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 75 | 'y_offset' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 77 | 'age_ma' | 3.85 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 77 | 'y_offset' | 1.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 79 | 'age_ma' | 3.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 79 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 81 | 'age_ma' | 2.8 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 81 | 'y_offset' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 83 | 'age_ma' | 2.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 83 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 85 | 'age_ma' | 1.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 85 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 87 | 'age_ma' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 87 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 89 | 'age_ma' | 0.43 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 89 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 91 | 'age_ma' | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 91 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 93 | 'age_ma' | 0.315 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 93 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 95 | 'age_ma' | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 95 | 'y_offset' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 97 | 'age_ma' | 0.19 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 97 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 99 | 'age_ma' | 0.067 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 99 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 103 | 'age_ma' | 2.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 103 | 'y_offset' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 105 | 'age_ma' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 105 | 'y_offset' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 107 | 'age_ma' | 1.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 107 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 109 | 'age_ma' | 1.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 109 | 'y_offset' | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 111 | 'age_ma' | 0.28 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 111 | 'y_offset' | 1.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 113 | 'age_ma' | 0.15 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 113 | 'y_offset' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 119 | 'start_ma' | 0.014 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 119 | 'end_ma' | 0.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 120 | 'start_ma' | 0.029 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 120 | 'end_ma' | 0.014 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 121 | 'start_ma' | 0.057 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 121 | 'end_ma' | 0.029 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 122 | 'start_ma' | 0.071 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 122 | 'end_ma' | 0.057 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 123 | 'start_ma' | 0.13 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 123 | 'end_ma' | 0.071 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 124 | 'start_ma' | 0.13 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 124 | 'end_ma' | 0.115 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 125 | 'start_ma' | 0.191 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 125 | 'end_ma' | 0.13 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 126 | 'start_ma' | 0.243 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 126 | 'end_ma' | 0.191 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 127 | 'start_ma' | 0.424 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 127 | 'end_ma' | 0.374 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 128 | 'start_ma' | 0.478 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 128 | 'end_ma' | 0.424 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 142 | 'tw_celsius' | 30.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 148 | 'tw_celsius' | 29.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 154 | 'tw_celsius' | 30.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 160 | 'tw_celsius' | 26.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 167 | 'tw_celsius' | 29.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 174 | 'tw_celsius' | 21.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 180 | 'tw_celsius' | 29.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 186 | 'tw_celsius' | 25.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 193 | 'tw_celsius' | 28.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 199 | 'tw_celsius' | 25.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 205 | 'tw_celsius' | 23.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 212 | 'tw_celsius' | 29.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 218 | 'tw_celsius' | 34.6 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 224 | 'tw_celsius' | 30.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 230 | 'tw_celsius' | 28.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 236 | 'tw_celsius' | 23.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 242 | 'tw_celsius' | 22.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 249 | 'tw_celsius' | 27.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 255 | 'tw_celsius' | 29.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 261 | 'tw_celsius' | 28.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 267 | 'tw_celsius' | 29.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 337 | 'age_ma' | 0.074 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 339 | 'age_ma' | 0.125 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 341 | 'age_ma' | 0.009 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 684 | 'secondary_y' | True | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1244 | 'age_ma' | 5e-06 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1245 | 'age_ma' | 6e-06 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1246 | 'age_ma' | 1.6e-05 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1247 | 'age_ma' | 2.1e-05 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1248 | 'age_ma' | 2.6e-05 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1249 | 'age_ma' | 3.6e-05 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1637 | 'start' | 4500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1637 | 'end' | 541 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1638 | 'start' | 541 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1638 | 'end' | 252.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1639 | 'start' | 252.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1639 | 'end' | 66.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1640 | 'start' | 66.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 1640 | 'end' | 1e-07 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 2414 | 'x' | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 2416 | 'size' | 18 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |

### planet9_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 33 | layer_info['radius_fraction'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 35 | layer_info['opacity'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 208 | layer_info['radius_fraction'] | 48000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 210 | layer_info['opacity'] | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |

### planetarium_apparent_magnitude.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 374 | flattened_analysis['missing_lum'] | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 375 | flattened_analysis['temp_le_zero'] | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |

### planetarium_distance.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 416 | flattened_analysis['missing_lum'] | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 417 | flattened_analysis['temp_le_zero'] | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |

### pluto_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 31 | layer_info['radius_fraction'] | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 33 | layer_info['opacity'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 100 | layer_info['radius_fraction'] | 0.99 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 102 | layer_info['opacity'] | 0.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 164 | layer_info['radius_fraction'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 166 | layer_info['opacity'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 335 | layer_info['radius_fraction'] | 1.17 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 337 | layer_info['opacity'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 417 | layer_info['radius_fraction'] | 1.43 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 419 | layer_info['opacity'] | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 499 | layer_info['radius_fraction'] | 4685 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 501 | layer_info['opacity'] | 0.25 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |

### sgr_a_grand_tour.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 55 | ROSETTE_ORBIT_COUNTS['S2'] | 80 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 56 | ROSETTE_ORBIT_COUNTS['S62'] | 50 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 57 | ROSETTE_ORBIT_COUNTS['S4711'] | 60 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 58 | ROSETTE_ORBIT_COUNTS['S4714'] | 40 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 569 | 'duration' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 569 | 'redraw' | True | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 570 | 'duration' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 581 | 'duration' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 581 | 'redraw' | True | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 582 | 'duration' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 593 | 'duration' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 593 | 'redraw' | True | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 594 | 'duration' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 605 | 'duration' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 605 | 'redraw' | True | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 606 | 'duration' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 645 | 'scene.xaxis.autorange' | True | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 646 | 'scene.yaxis.autorange' | True | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 647 | 'scene.zaxis.autorange' | True | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |

### sgr_a_visualization_animation.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 25 | ANIMATION_CONFIG['num_frames'] | 180 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 26 | ANIMATION_CONFIG['frame_duration_ms'] | 30 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 27 | ANIMATION_CONFIG['star_marker_size'] | 10 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 28 | ANIMATION_CONFIG['show_velocity_trace'] | True | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 29 | ANIMATION_CONFIG['trail_length'] | 5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |

### sgr_a_visualization_precession.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 31 | S4714_ACCURACY_PATCH['a_au'] | 800.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 158 | orbit_counts['S2'] | 100 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 159 | orbit_counts['S62'] | 40 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 160 | orbit_counts['S4711'] | 80 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 161 | orbit_counts['S4714'] | 50 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |

### solar_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 233 | claim: 20 R_sun | 20 R_sun | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 234 | claim: 8.8 R_sun | 8.8 R_sun | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 827 | claim: 33 R_sun | 33 R_sun | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 827 | claim: 0.153 AU | 0.153 AU | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 1228 | claim: 20 hours | 20 hours | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |

### spacecraft_encounters.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 204 | claim: 14 hours | 14 hours | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 248 | claim: 122 km | 122 km | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 250 | claim: 122 km | 122 km | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 250 | claim: 6371 km | 6371 km | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |

### star_notes.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 324 | claim: 800 light-years | 800 light-years | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 428 | claim: 200 light-years | 200 light-years | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |
| 832 | claim: 340 light-years | 340 light-years | 3 | 4 | **12** | No source, contains date-sensitive claims | In display string (hover text / INFO) |

### uranus_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 34 | layer_info['radius_fraction'] | 0.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 36 | layer_info['opacity'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 89 | layer_info['radius_fraction'] | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 91 | layer_info['opacity'] | 0.9 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 153 | layer_info['radius_fraction'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 155 | layer_info['opacity'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 335 | layer_info['radius_fraction'] | 1.16 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 337 | layer_info['opacity'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 419 | params['sunward_distance'] | 21 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 422 | params['equatorial_radius'] | 27.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 423 | params['polar_radius'] | 17.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 426 | params['tail_length'] | 300 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 427 | params['tail_base_radius'] | 15 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 428 | params['tail_end_radius'] | 75 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 748 | 'inner_radius_km' | 41800 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 749 | 'outer_radius_km' | 41802 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 750 | 'thickness_km' | 2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 752 | 'opacity' | 0.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 764 | 'inner_radius_km' | 42200 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 765 | 'outer_radius_km' | 42207 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 766 | 'thickness_km' | 7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 768 | 'opacity' | 0.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 781 | 'inner_radius_km' | 42600 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 782 | 'outer_radius_km' | 42603 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 783 | 'thickness_km' | 3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 785 | 'opacity' | 0.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 798 | 'inner_radius_km' | 44700 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 799 | 'outer_radius_km' | 44710 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 800 | 'thickness_km' | 10 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 802 | 'opacity' | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 816 | 'inner_radius_km' | 45700 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 817 | 'outer_radius_km' | 45711 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 818 | 'thickness_km' | 11 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 820 | 'opacity' | 0.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 835 | 'inner_radius_km' | 47200 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 836 | 'outer_radius_km' | 47202 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 837 | 'thickness_km' | 2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 839 | 'opacity' | 0.2 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 853 | 'inner_radius_km' | 47600 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 854 | 'outer_radius_km' | 47604 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 855 | 'thickness_km' | 4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 857 | 'opacity' | 0.4 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 872 | 'inner_radius_km' | 48300 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 873 | 'outer_radius_km' | 48307 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 874 | 'thickness_km' | 7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 876 | 'opacity' | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 891 | 'inner_radius_km' | 51100 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 892 | 'outer_radius_km' | 51190 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 893 | 'thickness_km' | 60 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 895 | 'opacity' | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 911 | 'inner_radius_km' | 62000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 912 | 'outer_radius_km' | 97700 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 913 | 'thickness_km' | 9500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 915 | 'opacity' | 0.1 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 945 | 'inner_radius_km' | 86000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 946 | 'outer_radius_km' | 102000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 947 | 'thickness_km' | 16000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 949 | 'opacity' | 0.1 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1067 | layer_info['radius_fraction'] | 2770 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 1069 | layer_info['opacity'] | 0.25 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |

### venus_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 32 | layer_info['radius_fraction'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 34 | layer_info['opacity'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 85 | layer_info['radius_fraction'] | 0.98 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 87 | layer_info['opacity'] | 0.7 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 138 | layer_info['radius_fraction'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 140 | layer_info['opacity'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 297 | layer_info['radius_fraction'] | 1.01 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 299 | layer_info['opacity'] | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 356 | layer_info['radius_fraction'] | 1.08 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 358 | layer_info['opacity'] | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 459 | params['sunward_distance'] | 1.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 462 | params['equatorial_radius'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 463 | params['polar_radius'] | 1.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 466 | params['tail_length'] | 60 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 467 | params['tail_base_radius'] | 1.5 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |
| 468 | params['tail_end_radius'] | 30 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering/shells module |

### visualization_2d.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 312 | 'temp_min' | 30000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 312 | 'temp_max' | 50000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 313 | 'temp_min' | 10000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 313 | 'temp_max' | 30000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 314 | 'temp_min' | 7500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 314 | 'temp_max' | 10000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 315 | 'temp_min' | 6000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 315 | 'temp_max' | 7500 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 316 | 'temp_min' | 5200 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 316 | 'temp_max' | 6000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 317 | 'temp_min' | 3700 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 317 | 'temp_max' | 5200 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 318 | 'temp_min' | 2400 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 318 | 'temp_max' | 3700 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 319 | 'temp_min' | 1300 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 319 | 'temp_max' | 2400 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 418 | label_positions_paper['O'] | 0.08 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 419 | label_positions_paper['B'] | 0.3 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 420 | label_positions_paper['A'] | 0.485 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 421 | label_positions_paper['F'] | 0.555 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 422 | label_positions_paper['G'] | 0.6 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 423 | label_positions_paper['K'] | 0.67 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 424 | label_positions_paper['M'] | 0.77 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 425 | label_positions_paper['L'] | 0.92 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 562 | 'bv_matched' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 563 | 'bv_only' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 564 | 'spectral_type_hot' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 565 | 'spectral_type_cool' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 566 | 'spectral_type_only' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 567 | 'spectral_type_disagreement' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 568 | 'none' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |

### visualization_3d.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 433 | 'x' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 433 | 'y' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 433 | 'z' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 437 | 'x' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 437 | 'y' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 437 | 'z' | 1 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 496 | 'temp_min' | 1300 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 497 | 'temp_max' | 50000 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 498 | 'mag_min' | -1.44 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 499 | 'mag_max' | 9.0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 898 | 'x' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 898 | 'y' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 898 | 'z' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 902 | 'x' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 902 | 'y' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 902 | 'z' | 1 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 923 | 'x' | 0.001 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 923 | 'y' | 0.001 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 923 | 'z' | 0.001 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 924 | 'x' | 1 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 924 | 'y' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 924 | 'z' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 925 | 'x' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 925 | 'y' | 0 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 925 | 'z' | 1 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 968 | 'r' | 10 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |
| 968 | 't' | 10 | 4 | 3 | **12** | No source citation (recalled) | Geometry value in rendering module |

---

## Tier 3: ADD SOURCE WHEN TOUCHED (Score 5-9)

### asteroid_belt_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 93 | MAIN_BELT_INNER | 2.2 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 94 | MAIN_BELT_OUTER | 3.2 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 95 | MAIN_BELT_PEAK | 2.7 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 97 | HILDA_DISTANCE | 3.97 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 98 | TROJAN_DISTANCE | 5.2 | 4 | 2 | **8** | No source citation (recalled) | Internal use |

### celestial_coordinates.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 250 | MAJOR_BODY_UNCERTAINTIES['Europa (astero | 0.3 | 3 | 3 | **9** | No source, contains date-sensitive claims | Value in computation module |
| 251 | MAJOR_BODY_UNCERTAINTIES['Eunomia'] | 0.2 | 3 | 3 | **9** | No source, contains date-sensitive claims | Value in computation module |
| 252 | MAJOR_BODY_UNCERTAINTIES['Psyche'] | 0.1 | 3 | 3 | **9** | No source, contains date-sensitive claims | Value in computation module |
| 253 | MAJOR_BODY_UNCERTAINTIES['Euphrosyne'] | 0.3 | 3 | 3 | **9** | No source, contains date-sensitive claims | Value in computation module |
| 254 | MAJOR_BODY_UNCERTAINTIES['Cybele'] | 0.3 | 3 | 3 | **9** | No source, contains date-sensitive claims | Value in computation module |

### celestial_objects.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 43 | claim: 670 km | 670 km | 2 | 4 | **8** | Has source citation | In display string (hover text / INFO) |
| 43 | claim: 700 km | 700 km | 2 | 4 | **8** | Has source citation | In display string (hover text / INFO) |
| 71 | claim: 692.5 km | 692.5 km | 2 | 4 | **8** | Has source citation | In display string (hover text / INFO) |
| 71 | claim: 4.283 days | 4.283 days | 2 | 4 | **8** | Has source citation | In display string (hover text / INFO) |
| 71 | claim: 0.88 g/cm3 | 0.88 g/cm3 | 2 | 4 | **8** | Has source citation | In display string (hover text / INFO) |
| 690 | 'is_mission' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 695 | 'is_mission' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 702 | 'is_mission' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 709 | 'is_mission' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 714 | 'is_mission' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 719 | 'is_mission' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 732 | 'is_mission' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 738 | 'is_mission' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 745 | 'is_mission' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 760 | 'is_mission' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 781 | 'is_mission' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 786 | 'is_mission' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 792 | 'is_mission' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 808 | 'is_mission' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 815 | 'is_mission' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 822 | 'is_mission' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 829 | 'is_mission' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 845 | 'is_mission' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 854 | 'is_mission' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1139 | 'semi_major_axis_au' | 0.01154 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1139 | 'period_days' | 1.51087 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1140 | 'in_habitable_zone' | False | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1147 | 'semi_major_axis_au' | 0.0158 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1147 | 'period_days' | 2.42182 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1148 | 'in_habitable_zone' | False | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1155 | 'semi_major_axis_au' | 0.02227 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1155 | 'period_days' | 4.04961 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1156 | 'in_habitable_zone' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1163 | 'semi_major_axis_au' | 0.02925 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1163 | 'period_days' | 6.09965 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1164 | 'in_habitable_zone' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1171 | 'semi_major_axis_au' | 0.03849 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1171 | 'period_days' | 9.20669 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1172 | 'in_habitable_zone' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1179 | 'semi_major_axis_au' | 0.04683 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1179 | 'period_days' | 12.35294 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1180 | 'in_habitable_zone' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1187 | 'semi_major_axis_au' | 0.06189 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1187 | 'period_days' | 18.76712 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1188 | 'in_habitable_zone' | False | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1214 | 'semi_major_axis_au' | 0.4607 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1214 | 'period_days' | 95.196 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1215 | 'in_habitable_zone' | False | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1222 | 'semi_major_axis_au' | 0.76 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1222 | 'period_days' | 215.5 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1223 | 'in_habitable_zone' | False | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1237 | 'semi_major_axis_au' | 0.04856 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1237 | 'period_days' | 11.18427 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1238 | 'in_habitable_zone' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1245 | 'semi_major_axis_au' | 0.029 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1245 | 'period_days' | 5.122 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1246 | 'in_habitable_zone' | False | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 628 | 'show_tails' | False | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 636 | 'show_tails' | False | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 644 | 'show_tails' | False | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 726 | 'is_mission' | True | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 753 | 'is_mission' | True | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 767 | 'is_mission' | True | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 774 | 'is_mission' | True | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 798 | 'is_mission' | True | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 836 | 'is_mission' | True | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 866 | 'is_mission' | True | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |

### climate_cache_manager.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 43 | 'success' | False | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 44 | 'success' | False | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 45 | 'success' | False | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 72 | 'success' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 82 | 'success' | False | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 107 | 'success' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 117 | 'success' | False | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 155 | 'success' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 165 | 'success' | False | 4 | 2 | **8** | No source citation (recalled) | Internal use |

### close_approach_data.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 56 | CENTER_BODY_RADII_KM['Sun'] | 695700.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 57 | CENTER_BODY_RADII_KM['Mercury'] | 2439.7 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 58 | CENTER_BODY_RADII_KM['Venus'] | 6051.8 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 59 | CENTER_BODY_RADII_KM['Earth'] | 6371.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 60 | CENTER_BODY_RADII_KM['Moon'] | 1737.4 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 61 | CENTER_BODY_RADII_KM['Mars'] | 3389.5 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 62 | CENTER_BODY_RADII_KM['Jupiter'] | 69911.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 63 | CENTER_BODY_RADII_KM['Saturn'] | 58232.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 64 | CENTER_BODY_RADII_KM['Uranus'] | 25362.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 65 | CENTER_BODY_RADII_KM['Neptune'] | 24622.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 66 | CENTER_BODY_RADII_KM['Pluto'] | 1188.3 | 4 | 2 | **8** | No source citation (recalled) | Internal use |

### comet_visualization_shells.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 216 | 'dust_tail_count' | 3 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering/shells module |
| 218 | 'dust_tail_fan_angle' | 40 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering/shells module |
| 240 | 'post_disintegration_dust_scale' | 0.55 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering/shells module |

### convert_hot_ph_to_json.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 168 | 'pre_industrial_ph' | 8.2 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 169 | 'current_decline' | 0.1 | 4 | 2 | **8** | No source citation (recalled) | Internal use |

### dep_trace.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 32 | HUB_THRESHOLD | 8 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 322 | 'width' | 1.5 | 4 | 2 | **8** | No source citation (recalled) | Internal use |

### earth_system_visualization_gui.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 175 | 'x' | 0.5 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 177 | 'size' | 16 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 313 | 'x' | 0.5 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 315 | 'size' | 14 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 877 | 'x' | 0.5 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 879 | 'size' | 20 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1024 | 'x' | 0.5 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1026 | 'size' | 16 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1172 | SRC['CLIMATE_RF'] | 2.56 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1173 | SRC['CLIMATE_CO2'] | 1.44 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1174 | SRC['NOVEL'] | 1.8 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1175 | SRC['OZONE'] | 0.48 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1176 | SRC['AEROSOLS'] | 0.8 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1177 | SRC['OCEAN_ACID'] | 1.04 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1178 | SRC['FRESH_GREEN'] | 0.95 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1179 | SRC['FRESH_BLUE'] | 1.16 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1180 | SRC['LAND'] | 1.46 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1181 | SRC['BIO_FUNC'] | 2.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1182 | SRC['BIO_GEN'] | 1.6 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1183 | SRC['BIOGEO_P'] | 2.14 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1184 | SRC['BIOGEO_N'] | 2.82 | 4 | 2 | **8** | No source citation (recalled) | Internal use |

### paleoclimate_dual_scale.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 53 | 'start' | 145.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 53 | 'end' | 66.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 56 | 'start' | 66.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 56 | 'end' | 56.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 57 | 'start' | 56.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 57 | 'end' | 33.9 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |

### paleoclimate_human_origins_full.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 49 | 'start' | 145.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 49 | 'end' | 66.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 52 | 'start' | 66.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 52 | 'end' | 56.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 53 | 'start' | 56.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 53 | 'end' | 33.9 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |

### paleoclimate_visualization.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 46 | 'start' | 145.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 46 | 'end' | 66.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 49 | 'start' | 66.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 49 | 'end' | 56.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 50 | 'start' | 56.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 50 | 'end' | 33.9 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |

### paleoclimate_visualization_full.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 49 | 'start' | 145.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 49 | 'end' | 66.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 52 | 'start' | 66.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 52 | 'end' | 56.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 53 | 'start' | 56.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 53 | 'end' | 33.9 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |

### paleoclimate_wet_bulb_full.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 48 | 'start' | 145.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 48 | 'end' | 66.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 51 | 'start' | 66.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 51 | 'end' | 56.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 52 | 'start' | 56.0 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 52 | 'end' | 33.9 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 273 | 'tw_celsius' | 28.9 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 279 | 'tw_celsius' | 31.6 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 285 | 'tw_celsius' | 31.4 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 291 | 'tw_celsius' | 27.2 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 297 | 'tw_celsius' | 28.7 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 303 | 'tw_celsius' | 29.1 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 309 | 'tw_celsius' | 28.2 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 1241 | 'age_ma' | 2e-06 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 1242 | 'age_ma' | 3e-06 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 1243 | 'age_ma' | 4e-06 | 3 | 3 | **9** | No source, contains date-sensitive claims | Geometry value in rendering module |
| 132 | BASELINE_ABSOLUTE_TEMP | 14.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 134 | TW_SURVIVABILITY_BIOLOGICAL | 31.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 135 | TW_SURVIVABILITY_THEORETICAL | 35.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |

### palomas_orrery.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 541 | defaults['trajectory_points'] | 50 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 542 | defaults['orbital_points'] | 50 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 543 | defaults['satellite_days'] | 50 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 544 | defaults['satellite_points'] | 50 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 547 | defaults['days_to_plot'] | 365 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 869 | satellite_precession_rates['Phobos'] | 158.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 870 | satellite_precession_rates['Deimos'] | 2.7 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 873 | satellite_precession_rates['Metis'] | 28.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 874 | satellite_precession_rates['Adrastea'] | 24.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 875 | satellite_precession_rates['Amalthea'] | 7.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 876 | satellite_precession_rates['Thebe'] | 2.5 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 877 | satellite_precession_rates['Io'] | 0.7 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 878 | satellite_precession_rates['Europa'] | 0.04 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 879 | satellite_precession_rates['Ganymede'] | 0.002 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 880 | satellite_precession_rates['Callisto'] | 0.0001 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 883 | satellite_precession_rates['Pan'] | 52.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 884 | satellite_precession_rates['Daphnis'] | 48.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 885 | satellite_precession_rates['Atlas'] | 44.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 886 | satellite_precession_rates['Prometheus'] | 36.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 887 | satellite_precession_rates['Pandora'] | 32.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 888 | satellite_precession_rates['Mimas'] | 5.3 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 889 | satellite_precession_rates['Enceladus'] | 0.6 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 890 | satellite_precession_rates['Tethys'] | 0.05 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 891 | satellite_precession_rates['Dione'] | 0.009 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 892 | satellite_precession_rates['Rhea'] | 0.001 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 893 | satellite_precession_rates['Titan'] | 0.0001 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 896 | satellite_precession_rates['Cordelia'] | 16.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 897 | satellite_precession_rates['Ophelia'] | 12.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 898 | satellite_precession_rates['Bianca'] | 8.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 899 | satellite_precession_rates['Cressida'] | 4.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 900 | satellite_precession_rates['Portia'] | 15.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 901 | satellite_precession_rates['Mab'] | 8.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 902 | satellite_precession_rates['Miranda'] | 0.8 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 903 | satellite_precession_rates['Ariel'] | 0.03 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 904 | satellite_precession_rates['Umbriel'] | 0.01 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 905 | satellite_precession_rates['Titania'] | 0.002 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 906 | satellite_precession_rates['Oberon'] | 0.001 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 909 | satellite_precession_rates['Naiad'] | 24.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 910 | satellite_precession_rates['Thalassa'] | 18.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 911 | satellite_precession_rates['Despina'] | 14.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 912 | satellite_precession_rates['Galatea'] | 8.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 913 | satellite_precession_rates['Larissa'] | 2.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 914 | satellite_precession_rates['Proteus'] | 0.5 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 915 | satellite_precession_rates['Triton'] | 0.2 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 918 | satellite_precession_rates['Moon'] | 0.004 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 921 | satellite_precession_rates['Charon'] | 0.001 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 922 | satellite_precession_rates['Styx'] | 0.001 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 923 | satellite_precession_rates['Nix'] | 0.001 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 924 | satellite_precession_rates['Kerberos'] | 0.001 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 925 | satellite_precession_rates['Hydra'] | 0.001 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1154 | 'vx' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1155 | 'vy' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1156 | 'vz' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1157 | 'velocity' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 1687 | result['analytical_position'] | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 2920 | BUTTON_WIDTH | 14 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 3213 | 'x' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 3213 | 'y' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 3213 | 'z' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 4189 | obj_data['vx'] | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 4190 | obj_data['vy'] | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 4191 | obj_data['vz'] | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 4192 | obj_data['velocity'] | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 4205 | obj_data['x'] | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 4205 | obj_data['y'] | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 4205 | obj_data['z'] | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 4258 | obj_data['derived_from_vanth'] | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 4349 | obj_data['analytical_position'] | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 4630 | 'x' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 4630 | 'y' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 4630 | 'z' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 4689 | obj_data['x'] | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 4689 | obj_data['y'] | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 4689 | obj_data['z'] | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 4734 | obj_data['derived_from_vanth'] | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 5813 | 'x' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 5813 | 'y' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 5813 | 'z' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 5963 | 'x' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 5963 | 'y' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 5963 | 'z' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 5972 | 'x' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 5972 | 'y' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 5972 | 'z' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 6899 | 'duration' | 500 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 6899 | 'redraw' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 6900 | 'fromcurrent' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 6901 | 'duration' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 6904 | 'duration' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 6906 | 'duration' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 6919 | 'duration' | 500 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 6919 | 'redraw' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |

### palomas_orrery_dashboard.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 36 | WINDOW_WIDTH | 960 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 37 | WINDOW_HEIGHT | 720 | 4 | 2 | **8** | No source citation (recalled) | Internal use |

### palomas_orrery_helpers.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 761 | 'x' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 761 | 'y' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 761 | 'z' | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 762 | 'x' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 762 | 'y' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 762 | 'z' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 763 | 'x' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 763 | 'y' | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 763 | 'z' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |

### planet_visualization.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 265 | SOLAR_RADIUS_AU | 0.00465047 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 266 | CORE_AU | 0.00093 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 267 | RADIATIVE_ZONE_AU | 0.00325 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 268 | CHROMOSPHERE_RADII | 1.5 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 269 | INNER_CORONA_RADII | 3 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 270 | OUTER_CORONA_RADII | 50 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 271 | TERMINATION_SHOCK_AU | 94 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 272 | HELIOPAUSE_RADII | 26449 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 273 | INNER_LIMIT_OORT_CLOUD_AU | 2000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 274 | INNER_OORT_CLOUD_AU | 20000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 275 | OUTER_OORT_CLOUD_AU | 100000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 276 | GRAVITATIONAL_INFLUENCE_AU | 126000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 278 | KM_PER_AU | 149597870.7 | 4 | 2 | **8** | No source citation (recalled) | Internal use |

### provenance_scanner.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 44 | V_FETCHED | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 45 | V_SOURCED | 2 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 46 | V_STALE | 3 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 47 | V_RECALLED | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 54 | C_COSMETIC | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 55 | C_INTERNAL | 2 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 56 | C_LOADBEARING | 3 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 57 | C_PUBLIC | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 58 | C_PROPAGATING | 5 | 4 | 2 | **8** | No source citation (recalled) | Internal use |

### scenarios_coral_bleaching.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 167 | CORAL_THRESHOLDS['min_display'] | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 168 | CORAL_THRESHOLDS['spike_floor'] | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 175 | CORAL_THRESHOLDS['height_base_subtract'] | False | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 176 | CORAL_THRESHOLDS['height_multiplier'] | 1000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 178 | CORAL_THRESHOLDS['cmin'] | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 179 | CORAL_THRESHOLDS['cmax'] | 16 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 181 | CORAL_THRESHOLDS['contour_levels_start'] | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 182 | CORAL_THRESHOLDS['contour_levels_stop'] | 16 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 183 | CORAL_THRESHOLDS['contour_levels_step'] | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 185 | CORAL_THRESHOLDS['pop_radius_divisor'] | 50000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 186 | CORAL_THRESHOLDS['spike_stride'] | 200 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 202 | 'focus_val_min' | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 213 | 'lat' | 25.7617 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 213 | 'lon' | -80.1918 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 213 | 'pop' | 6100000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 214 | 'lat' | 24.5551 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 214 | 'lon' | -81.78 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 214 | 'pop' | 26000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 215 | 'lat' | 23.1136 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 215 | 'lon' | -82.3666 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 215 | 'pop' | 2100000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 216 | 'lat' | 25.0443 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 216 | 'lon' | -77.3504 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 216 | 'pop' | 275000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |

### scenarios_heatwaves.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 96 | HEATWAVE_THRESHOLDS['min_display'] | 20 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 104 | HEATWAVE_THRESHOLDS['height_base_subtrac | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 105 | HEATWAVE_THRESHOLDS['height_multiplier'] | 50000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 107 | HEATWAVE_THRESHOLDS['cmin'] | 20 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 108 | HEATWAVE_THRESHOLDS['cmax'] | 38 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 110 | HEATWAVE_THRESHOLDS['contour_levels_star | 20 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 111 | HEATWAVE_THRESHOLDS['contour_levels_stop | 38 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 112 | HEATWAVE_THRESHOLDS['contour_levels_step | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 114 | HEATWAVE_THRESHOLDS['pop_radius_divisor' | 250000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 128 | 'focus_val_min' | 24 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 132 | 'lat' | 40.7128 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 132 | 'lon' | -74.006 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 132 | 'pop' | 7800000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 133 | 'lat' | 39.9526 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 133 | 'lon' | -75.1652 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 133 | 'pop' | 2000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 134 | 'lat' | 42.3601 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 134 | 'lon' | -71.0589 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 134 | 'pop' | 800000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 135 | 'lat' | 39.2904 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 135 | 'lon' | -76.6122 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 135 | 'pop' | 950000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 136 | 'lat' | 38.9072 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 136 | 'lon' | -77.0369 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 136 | 'pop' | 800000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 147 | 'focus_val_min' | 26.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 151 | 'lat' | 38.6245 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 151 | 'lon' | -90.1506 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 151 | 'pop' | 800000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 152 | 'lat' | 38.627 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 152 | 'lon' | -90.1994 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 152 | 'pop' | 850000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 153 | 'lat' | 39.7817 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 153 | 'lon' | -89.6501 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 153 | 'pop' | 100000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 164 | 'focus_val_min' | 22.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 168 | 'lat' | 34.0522 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 168 | 'lon' | -118.2437 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 168 | 'pop' | 2200000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 169 | 'lat' | 33.7701 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 169 | 'lon' | -118.1937 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 169 | 'pop' | 250000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 170 | 'lat' | 34.0195 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 170 | 'lon' | -118.4912 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 170 | 'pop' | 75000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 171 | 'lat' | 33.8366 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 171 | 'lon' | -117.9143 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 171 | 'pop' | 30000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 182 | 'focus_val_min' | 25.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 186 | 'lat' | 38.627 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 186 | 'lon' | -90.1994 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 186 | 'pop' | 700000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 187 | 'lat' | 40.7128 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 187 | 'lon' | -74.006 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 187 | 'pop' | 7800000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 188 | 'lat' | 39.9526 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 188 | 'lon' | -75.1652 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 188 | 'pop' | 2000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 189 | 'lat' | 39.1031 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 189 | 'lon' | -84.512 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 189 | 'pop' | 500000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 190 | 'lat' | 39.7684 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 190 | 'lon' | -86.1581 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 190 | 'pop' | 500000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 201 | 'focus_val_min' | 18.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 205 | 'lat' | 51.5074 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 205 | 'lon' | -0.1278 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 205 | 'pop' | 6800000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 206 | 'lat' | 52.4862 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 206 | 'lon' | -1.8904 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 206 | 'pop' | 1000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 207 | 'lat' | 50.9097 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 207 | 'lon' | -1.4044 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 207 | 'pop' | 200000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 218 | 'focus_val_min' | 24.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 222 | 'lat' | 35.1495 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 222 | 'lon' | -90.049 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 222 | 'pop' | 650000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 223 | 'lat' | 38.627 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 223 | 'lon' | -90.1994 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 223 | 'pop' | 450000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 224 | 'lat' | 39.0997 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 224 | 'lon' | -94.5786 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 224 | 'pop' | 450000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 225 | 'lat' | 32.7767 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 225 | 'lon' | -96.797 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 225 | 'pop' | 900000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 226 | 'lat' | 32.2988 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 226 | 'lon' | -90.1848 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 226 | 'pop' | 200000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 237 | 'focus_val_min' | 23.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 241 | 'lat' | 37.9838 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 241 | 'lon' | 23.7275 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 241 | 'pop' | 3000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 242 | 'lat' | 38.2466 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 242 | 'lon' | 21.7346 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 242 | 'pop' | 150000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 243 | 'lat' | 40.6401 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 243 | 'lon' | 22.9444 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 243 | 'pop' | 800000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 254 | 'focus_val_min' | 24.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 258 | 'lat' | 41.8781 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 258 | 'lon' | -87.6298 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 258 | 'pop' | 2700000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 259 | 'lat' | 43.0389 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 259 | 'lon' | -87.9065 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 259 | 'pop' | 570000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 260 | 'lat' | 41.5934 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 260 | 'lon' | -87.3464 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 260 | 'pop' | 75000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 271 | 'focus_val_min' | 22.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 275 | 'lat' | 48.8566 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 275 | 'lon' | 2.3522 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 275 | 'pop' | 2100000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 276 | 'lat' | 51.5074 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 276 | 'lon' | -0.1278 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 276 | 'pop' | 8900000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 277 | 'lat' | 45.4642 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 277 | 'lon' | 9.19 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 277 | 'pop' | 1350000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 278 | 'lat' | 41.9028 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 278 | 'lon' | 12.4964 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 278 | 'pop' | 2800000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 279 | 'lat' | 52.52 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 279 | 'lon' | 13.405 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 279 | 'pop' | 3600000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 280 | 'lat' | 52.3676 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 280 | 'lon' | 4.9041 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 280 | 'pop' | 820000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 291 | 'focus_val_min' | 20.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 295 | 'lat' | 55.7558 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 295 | 'lon' | 37.6173 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 295 | 'pop' | 11500000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 296 | 'lat' | 59.9311 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 296 | 'lon' | 30.3609 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 296 | 'pop' | 5400000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 297 | 'lat' | 56.3269 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 297 | 'lon' | 44.0059 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 297 | 'pop' | 1250000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 298 | 'lat' | 51.6755 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 298 | 'lon' | 39.2089 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 298 | 'pop' | 1000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 299 | 'lat' | 60.1699 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 299 | 'lon' | 24.9384 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 299 | 'pop' | 650000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 310 | 'focus_val_min' | 24.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 314 | 'lat' | 24.8607 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 314 | 'lon' | 67.0011 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 314 | 'pop' | 16000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 315 | 'lat' | 25.396 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 315 | 'lon' | 68.3578 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 315 | 'pop' | 1700000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 316 | 'lat' | 28.6139 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 316 | 'lon' | 77.209 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 316 | 'pop' | 26000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 317 | 'lat' | 21.1458 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 317 | 'lon' | 79.0882 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 317 | 'pop' | 2400000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 318 | 'lat' | 17.385 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 318 | 'lon' | 78.4867 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 318 | 'pop' | 10000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 319 | 'lat' | 16.5062 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 319 | 'lon' | 80.648 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 319 | 'pop' | 1500000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 320 | 'lat' | 23.0225 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 320 | 'lon' | 72.5714 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 320 | 'pop' | 8000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 321 | 'lat' | 20.2961 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 321 | 'lon' | 85.8245 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 321 | 'pop' | 1100000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 322 | 'lat' | 23.8103 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 322 | 'lon' | 90.4125 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 322 | 'pop' | 22000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 323 | 'lat' | 23.5859 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 323 | 'lon' | 58.4059 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 323 | 'pop' | 1500000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 334 | 'focus_val_min' | 24.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 338 | 'lat' | 30.5583 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 338 | 'lon' | 49.1983 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 338 | 'pop' | 160000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 339 | 'lat' | 31.3183 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 339 | 'lon' | 48.6706 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 339 | 'pop' | 1100000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 340 | 'lat' | 30.5081 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 340 | 'lon' | 47.7835 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 340 | 'pop' | 1300000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 341 | 'lat' | 29.3759 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 341 | 'lon' | 47.9774 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 341 | 'pop' | 3000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 342 | 'lat' | 25.2854 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 342 | 'lon' | 51.531 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 342 | 'pop' | 650000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 343 | 'lat' | 26.2285 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 343 | 'lon' | 50.586 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 343 | 'pop' | 200000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 344 | 'lat' | 26.4207 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 344 | 'lon' | 50.0888 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 344 | 'pop' | 1200000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 345 | 'lat' | 31.058 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 345 | 'lon' | 46.2573 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 345 | 'pop' | 550000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 346 | 'lat' | 23.1323 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 346 | 'lon' | 53.7966 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 346 | 'pop' | 20000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 357 | 'focus_val_min' | 24.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 361 | 'lat' | 13.7563 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 361 | 'lon' | 100.5018 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 361 | 'pop' | 10000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 362 | 'lat' | 18.7061 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 362 | 'lon' | 98.9817 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 362 | 'pop' | 1200000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 363 | 'lat' | 17.9757 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 363 | 'lon' | 102.6331 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 363 | 'pop' | 950000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 364 | 'lat' | 11.5564 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 364 | 'lon' | 104.9282 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 364 | 'pop' | 2100000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 375 | 'focus_val_min' | 24.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 379 | 'lat' | 35.6762 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 379 | 'lon' | 139.6503 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 379 | 'pop' | 14000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 380 | 'lat' | 36.1473 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 380 | 'lon' | 139.3886 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 380 | 'pop' | 200000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 381 | 'lat' | 35.1815 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 381 | 'lon' | 136.9066 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 381 | 'pop' | 2300000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 392 | 'focus_val_min' | 24.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 396 | 'lat' | 48.8566 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 396 | 'lon' | 2.3522 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 396 | 'pop' | 2100000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 397 | 'lat' | 50.8503 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 397 | 'lon' | 4.3517 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 397 | 'pop' | 1200000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 398 | 'lat' | 50.1109 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 398 | 'lon' | 8.6821 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 398 | 'pop' | 750000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 399 | 'lat' | 52.3676 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 399 | 'lon' | 4.9041 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 399 | 'pop' | 820000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 410 | 'focus_val_min' | 18.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 414 | 'lat' | 67.5447 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 414 | 'lon' | 133.385 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 414 | 'pop' | 1300 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 415 | 'lat' | 62.0397 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 415 | 'lon' | 129.7422 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 415 | 'pop' | 300000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 426 | 'focus_val_min' | 24.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 430 | 'lat' | 47.6062 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 430 | 'lon' | -122.3321 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 430 | 'pop' | 737000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 431 | 'lat' | 45.5152 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 431 | 'lon' | -122.6784 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 431 | 'pop' | 650000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 432 | 'lat' | 49.2827 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 432 | 'lon' | -123.1207 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 432 | 'pop' | 675000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 433 | 'lat' | 50.2333 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 433 | 'lon' | -121.5833 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 433 | 'pop' | 250 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 434 | 'lat' | 44.9429 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 434 | 'lon' | -123.0351 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 434 | 'pop' | 175000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 445 | 'focus_val_min' | 24.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 449 | 'lat' | 30.5928 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 449 | 'lon' | 114.3055 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 449 | 'pop' | 11000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 450 | 'lat' | 29.563 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 450 | 'lon' | 106.5516 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 450 | 'pop' | 15800000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 451 | 'lat' | 32.0603 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 451 | 'lon' | 118.7969 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 451 | 'pop' | 8500000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 452 | 'lat' | 31.2304 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 452 | 'lon' | 121.4737 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 452 | 'pop' | 26300000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 453 | 'lat' | 30.5728 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 453 | 'lon' | 104.0668 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 453 | 'pop' | 16000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 464 | 'focus_val_min' | 24.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 468 | 'lat' | -3.119 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 468 | 'lon' | -60.0217 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 468 | 'pop' | 2200000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 469 | 'lat' | -3.3542 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 469 | 'lon' | -64.7115 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 469 | 'pop' | 60000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 470 | 'lat' | -4.0849 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 470 | 'lon' | -63.1417 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 470 | 'pop' | 85000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 481 | 'focus_val_min' | 24.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 485 | 'lat' | -22.9068 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 485 | 'lon' | -43.1729 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 485 | 'pop' | 6700000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 486 | 'lat' | -23.5505 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 486 | 'lon' | -46.6333 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 486 | 'pop' | 12300000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 487 | 'lat' | -23.9618 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 487 | 'lon' | -46.3322 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 487 | 'pop' | 430000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 502 | 'lat' | 12.6392 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 502 | 'lon' | -8.0029 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 502 | 'pop' | 2400000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 503 | 'lat' | 14.4469 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 503 | 'lon' | -11.4445 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 503 | 'pop' | 127000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 504 | 'lat' | 13.4416 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 504 | 'lon' | -6.2163 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 504 | 'pop' | 130000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 505 | 'lat' | 12.3714 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 505 | 'lon' | -1.5197 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 505 | 'pop' | 2500000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 506 | 'lat' | 13.5116 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 506 | 'lon' | 2.1254 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 506 | 'pop' | 1000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 507 | 'lat' | 12.0022 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 507 | 'lon' | 8.592 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 507 | 'pop' | 4000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 522 | 'lat' | 24.7136 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 522 | 'lon' | 46.6753 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 522 | 'pop' | 7600000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 523 | 'lat' | 25.2048 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 523 | 'lon' | 55.2708 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 523 | 'pop' | 3300000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 524 | 'lat' | 29.3759 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 524 | 'lon' | 47.9774 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 524 | 'pop' | 3100000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 525 | 'lat' | 33.3152 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 525 | 'lon' | 44.3661 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 525 | 'pop' | 7100000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 526 | 'lat' | 30.5081 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 526 | 'lon' | 47.7835 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 526 | 'pop' | 1300000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 527 | 'lat' | 24.8607 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 527 | 'lon' | 67.0011 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 527 | 'pop' | 16000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 528 | 'lat' | 31.5204 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 528 | 'lon' | 74.3587 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 528 | 'pop' | 13000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 529 | 'lat' | 28.2835 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 529 | 'lon' | 68.4388 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 529 | 'pop' | 200000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 530 | 'lat' | 28.6139 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 530 | 'lon' | 77.209 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 530 | 'pop' | 32000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 531 | 'lat' | 26.8467 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 531 | 'lon' | 80.9462 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 531 | 'pop' | 3800000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 532 | 'lat' | 26.9124 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 532 | 'lon' | 75.7873 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 532 | 'pop' | 4000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 533 | 'lat' | 23.0225 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 533 | 'lon' | 72.5714 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 533 | 'pop' | 8200000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 534 | 'lat' | 19.076 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 534 | 'lon' | 72.8777 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 534 | 'pop' | 21000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 535 | 'lat' | 22.5726 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 535 | 'lon' | 88.3639 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 535 | 'pop' | 15000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 536 | 'lat' | 25.5941 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 536 | 'lon' | 85.1376 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 536 | 'pop' | 2500000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 537 | 'lat' | 20.2961 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 537 | 'lon' | 85.8245 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 537 | 'pop' | 1100000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 538 | 'lat' | 23.8103 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 538 | 'lon' | 90.4125 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 538 | 'pop' | 22000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 539 | 'lat' | 22.3569 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 539 | 'lon' | 91.7832 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 539 | 'pop' | 5000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 540 | 'lat' | 16.8409 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 540 | 'lon' | 96.1735 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 540 | 'pop' | 5500000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 541 | 'lat' | 13.7563 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 541 | 'lon' | 100.5018 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 541 | 'pop' | 10700000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 542 | 'lat' | 10.8231 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 542 | 'lon' | 106.6297 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 542 | 'pop' | 9000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 557 | 'lat' | 25.276987 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 557 | 'lon' | 55.296249 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 557 | 'pop' | 3300000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 558 | 'lat' | 25.2854 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 558 | 'lon' | 51.531 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 558 | 'pop' | 2300000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 559 | 'lat' | 27.1832 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 559 | 'lon' | 56.2666 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 559 | 'pop' | 526000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 560 | 'lat' | 24.4539 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 560 | 'lon' | 54.3773 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 560 | 'pop' | 1450000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 575 | 'lat' | -6.2088 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 575 | 'lon' | 106.8456 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 575 | 'pop' | 10500000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 576 | 'lat' | -12.4634 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 576 | 'lon' | 130.8456 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 576 | 'pop' | 150000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 577 | 'lat' | -23.698 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 577 | 'lon' | 133.8807 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 577 | 'pop' | 26000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 578 | 'lat' | -20.7256 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 578 | 'lon' | 139.4927 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 578 | 'pop' | 18000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 593 | 'lat' | 28.2835 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 593 | 'lon' | 68.4388 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 593 | 'pop' | 200000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 594 | 'lat' | 29.5448 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 594 | 'lon' | 67.8764 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 594 | 'pop' | 115000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 595 | 'lat' | 24.8607 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 595 | 'lon' | 67.0011 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 595 | 'pop' | 14900000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 596 | 'lat' | 27.7131 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 596 | 'lon' | 68.8492 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 596 | 'pop' | 500000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 611 | 'lat' | 41.8781 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 611 | 'lon' | -87.6298 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 611 | 'pop' | 2700000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 612 | 'lat' | 38.9072 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 612 | 'lon' | -77.0369 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 612 | 'pop' | 700000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 613 | 'lat' | 33.749 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 613 | 'lon' | -84.388 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 613 | 'pop' | 500000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 614 | 'lat' | 40.7128 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 614 | 'lon' | -74.006 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 614 | 'pop' | 8000000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 615 | 'lat' | 38.627 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 615 | 'lon' | -90.1994 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 615 | 'pop' | 300000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 630 | 'lat' | -3.119 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 630 | 'lon' | -60.0217 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 630 | 'pop' | 2200000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 631 | 'lat' | -2.443 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 631 | 'lon' | -54.7081 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 631 | 'pop' | 300000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 632 | 'lat' | -3.7437 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 632 | 'lon' | -73.2516 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 632 | 'pop' | 480000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 633 | 'lat' | -8.7612 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 633 | 'lon' | -63.9039 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 633 | 'pop' | 540000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 498 | 'focus_val_min' | 24.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 518 | 'focus_val_min' | 24.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 553 | 'focus_val_min' | 24.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 571 | 'focus_val_min' | 24.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 589 | 'focus_val_min' | 24.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 607 | 'focus_val_min' | 24.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 626 | 'focus_val_min' | 24.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |

### scenarios_western_heatwave_march_2026.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 66 | WESTERN_HEATWAVE_THRESHOLDS['cmin'] | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 67 | WESTERN_HEATWAVE_THRESHOLDS['cmax'] | 35 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 68 | WESTERN_HEATWAVE_THRESHOLDS['contour_lev | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 69 | WESTERN_HEATWAVE_THRESHOLDS['contour_lev | 35 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 70 | WESTERN_HEATWAVE_THRESHOLDS['contour_lev | 2 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 72 | WESTERN_HEATWAVE_THRESHOLDS['height_mult | 100000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 73 | WESTERN_HEATWAVE_THRESHOLDS['height_base | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 74 | WESTERN_HEATWAVE_THRESHOLDS['spike_strid | 200 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 75 | WESTERN_HEATWAVE_THRESHOLDS['pop_radius_ | 100000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 95 | 'lat' | 33.4484 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 95 | 'lon' | -112.0742 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 95 | 'pop' | 1700000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 96 | 'lat' | 36.1699 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 96 | 'lon' | -115.1398 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 96 | 'pop' | 650000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 97 | 'lat' | 34.0522 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 97 | 'lon' | -118.2437 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 97 | 'pop' | 3900000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 98 | 'lat' | 33.8303 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 98 | 'lon' | -116.5453 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 98 | 'pop' | 47500 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 99 | 'lat' | 33.2353 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 99 | 'lon' | -115.6064 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 99 | 'pop' | 2700 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 100 | 'lat' | 39.7392 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 100 | 'lon' | -104.9903 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 100 | 'pop' | 715000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 101 | 'lat' | 40.7608 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 101 | 'lon' | -111.891 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 101 | 'pop' | 200000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 102 | 'lat' | 35.0844 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 102 | 'lon' | -106.6504 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 102 | 'pop' | 565000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 103 | 'lat' | 39.0997 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 103 | 'lon' | -94.5786 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 103 | 'pop' | 508000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 104 | 'lat' | 35.4676 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 104 | 'lon' | -97.5164 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 104 | 'pop' | 700000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 105 | 'lat' | 33.5779 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 105 | 'lon' | -101.8552 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 105 | 'pop' | 265000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 106 | 'lat' | 38.627 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 106 | 'lon' | -90.1994 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 106 | 'pop' | 300000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 370 | 'baseline_center_anomaly' | 12.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 371 | 'baseline_spread' | 4.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 372 | 'baseline_center_lat' | 33.5 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 373 | 'baseline_center_lon' | -114.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 374 | 'max_anomaly_clip' | 22.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 383 | 'baseline_center_anomaly' | 16.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 384 | 'baseline_spread' | 5.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 385 | 'baseline_center_lat' | 34.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 386 | 'baseline_center_lon' | -114.5 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 387 | 'max_anomaly_clip' | 26.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 396 | 'baseline_center_anomaly' | 18.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 397 | 'baseline_spread' | 5.5 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 398 | 'baseline_center_lat' | 34.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 399 | 'baseline_center_lon' | -114.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 400 | 'max_anomaly_clip' | 28.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 409 | 'baseline_center_anomaly' | 22.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 410 | 'baseline_spread' | 6.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 411 | 'baseline_center_lat' | 33.5 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 412 | 'baseline_center_lon' | -114.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 413 | 'max_anomaly_clip' | 35.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 422 | 'baseline_center_anomaly' | 20.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 423 | 'baseline_spread' | 7.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 424 | 'baseline_center_lat' | 36.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 425 | 'baseline_center_lon' | -108.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 426 | 'max_anomaly_clip' | 48.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 435 | 'baseline_center_anomaly' | 18.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 436 | 'baseline_spread' | 8.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 437 | 'baseline_center_lat' | 37.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 438 | 'baseline_center_lon' | -105.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 439 | 'max_anomaly_clip' | 42.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 448 | 'baseline_center_anomaly' | 20.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 449 | 'baseline_spread' | 7.5 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 450 | 'baseline_center_lat' | 35.5 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 451 | 'baseline_center_lon' | -108.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 452 | 'max_anomaly_clip' | 35.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 461 | 'baseline_center_anomaly' | 22.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 462 | 'baseline_spread' | 8.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 463 | 'baseline_center_lat' | 34.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 464 | 'baseline_center_lon' | -102.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 465 | 'max_anomaly_clip' | 45.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 474 | 'baseline_center_anomaly' | 14.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 475 | 'baseline_spread' | 9.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 476 | 'baseline_center_lat' | 38.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 477 | 'baseline_center_lon' | -95.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 478 | 'max_anomaly_clip' | 35.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 481 | 'grid_resolution' | 0.5 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 119 | 'lat' | 33.4484 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 119 | 'lon' | -112.0742 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 120 | 'air_temp_f' | 95.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 120 | 'normal_high_f' | 78.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 120 | 'anomaly' | 17.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 125 | 'lat' | 32.6549 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 125 | 'lon' | -114.6196 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 126 | 'air_temp_f' | 98.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 126 | 'normal_high_f' | 82.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 126 | 'anomaly' | 16.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 131 | 'lat' | 33.8303 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 131 | 'lon' | -116.5453 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 132 | 'air_temp_f' | 96.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 132 | 'normal_high_f' | 80.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 132 | 'anomaly' | 16.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 139 | 'lat' | 36.1699 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 139 | 'lon' | -115.1398 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 140 | 'air_temp_f' | 92.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 140 | 'normal_high_f' | 70.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 140 | 'anomaly' | 22.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 145 | 'lat' | 33.6353 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 145 | 'lon' | -116.1064 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 146 | 'air_temp_f' | 100.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 146 | 'normal_high_f' | 82.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 146 | 'anomaly' | 18.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 151 | 'lat' | 32.2226 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 151 | 'lon' | -110.9747 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 152 | 'air_temp_f' | 97.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 152 | 'normal_high_f' | 76.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 152 | 'anomaly' | 21.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 159 | 'lat' | 33.4484 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 159 | 'lon' | -112.0742 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 160 | 'air_temp_f' | 101.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 160 | 'normal_high_f' | 78.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 160 | 'anomaly' | 23.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 165 | 'lat' | 36.1699 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 165 | 'lon' | -115.1398 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 166 | 'air_temp_f' | 94.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 166 | 'normal_high_f' | 70.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 166 | 'anomaly' | 24.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 171 | 'lat' | 36.4616 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 171 | 'lon' | -116.8666 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 172 | 'air_temp_f' | 108.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 172 | 'normal_high_f' | 86.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 172 | 'anomaly' | 22.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 179 | 'lat' | 32.6549 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 179 | 'lon' | -114.6196 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 180 | 'air_temp_f' | 109.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 180 | 'normal_high_f' | 82.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 180 | 'anomaly' | 27.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 185 | 'lat' | 32.7167 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 185 | 'lon' | -114.3333 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 186 | 'air_temp_f' | 112.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 186 | 'normal_high_f' | 80.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 186 | 'anomaly' | 32.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 191 | 'lat' | 33.4484 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 191 | 'lon' | -112.0742 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 192 | 'air_temp_f' | 105.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 192 | 'normal_high_f' | 78.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 192 | 'anomaly' | 27.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 199 | 'lat' | 39.7392 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 199 | 'lon' | -104.9903 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 200 | 'air_temp_f' | 86.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 200 | 'normal_high_f' | 55.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 200 | 'anomaly' | 31.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 205 | 'lat' | 40.7608 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 205 | 'lon' | -111.891 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 206 | 'air_temp_f' | 78.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 206 | 'normal_high_f' | 53.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 206 | 'anomaly' | 25.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 211 | 'lat' | 35.0844 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 211 | 'lon' | -106.6504 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 212 | 'air_temp_f' | 91.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 212 | 'normal_high_f' | 63.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 212 | 'anomaly' | 28.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 217 | 'lat' | 39.3058 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 217 | 'lon' | -102.2694 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 218 | 'air_temp_f' | 96.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 218 | 'normal_high_f' | 57.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 218 | 'anomaly' | 39.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 223 | 'lat' | 39.7561 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 223 | 'lon' | -99.324 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 224 | 'air_temp_f' | 101.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 224 | 'normal_high_f' | 57.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 224 | 'anomaly' | 44.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 229 | 'lat' | 41.2247 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 229 | 'lon' | -95.8152 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 230 | 'air_temp_f' | 97.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 230 | 'normal_high_f' | 53.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 230 | 'anomaly' | 44.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 235 | 'lat' | 40.2819 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 235 | 'lon' | -100.1665 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 236 | 'air_temp_f' | 99.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 236 | 'normal_high_f' | 56.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 236 | 'anomaly' | 43.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 241 | 'lat' | 42.7794 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 241 | 'lon' | -96.9292 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 242 | 'air_temp_f' | 97.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 242 | 'normal_high_f' | 51.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 242 | 'anomaly' | 46.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 247 | 'lat' | 43.6536 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 247 | 'lon' | -96.2128 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 248 | 'air_temp_f' | 88.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 248 | 'normal_high_f' | 45.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 248 | 'anomaly' | 43.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 253 | 'lat' | 38.6533 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 253 | 'lon' | -94.3488 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 254 | 'air_temp_f' | 97.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 254 | 'normal_high_f' | 58.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 254 | 'anomaly' | 39.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 259 | 'lat' | 32.4207 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 259 | 'lon' | -104.2288 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 260 | 'air_temp_f' | 100.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 260 | 'normal_high_f' | 75.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 260 | 'anomaly' | 25.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 267 | 'lat' | 38.627 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 267 | 'lon' | -90.1994 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 268 | 'air_temp_f' | 88.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 268 | 'normal_high_f' | 56.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 268 | 'anomaly' | 32.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 273 | 'lat' | 37.2089 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 273 | 'lon' | -93.2923 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 274 | 'air_temp_f' | 90.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 274 | 'normal_high_f' | 57.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 274 | 'anomaly' | 33.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 279 | 'lat' | 39.0997 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 279 | 'lon' | -94.5786 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 280 | 'air_temp_f' | 92.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 280 | 'normal_high_f' | 56.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 280 | 'anomaly' | 36.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 285 | 'lat' | 41.1403 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 285 | 'lon' | -100.7601 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 286 | 'air_temp_f' | 92.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 286 | 'normal_high_f' | 53.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 286 | 'anomaly' | 39.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 293 | 'lat' | 39.7392 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 293 | 'lon' | -104.9903 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 294 | 'air_temp_f' | 87.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 294 | 'normal_high_f' | 57.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 294 | 'anomaly' | 30.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 299 | 'lat' | 33.5779 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 299 | 'lon' | -101.8552 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 300 | 'air_temp_f' | 100.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 300 | 'normal_high_f' | 67.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 300 | 'anomaly' | 33.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 305 | 'lat' | 36.1699 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 305 | 'lon' | -115.1398 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 306 | 'air_temp_f' | 98.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 306 | 'normal_high_f' | 71.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 306 | 'anomaly' | 27.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 311 | 'lat' | 35.0844 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 311 | 'lon' | -106.6504 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 312 | 'air_temp_f' | 94.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 312 | 'normal_high_f' | 63.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 312 | 'anomaly' | 31.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 319 | 'lat' | 36.8164 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 319 | 'lon' | -100.5198 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 320 | 'air_temp_f' | 106.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 320 | 'normal_high_f' | 65.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 320 | 'anomaly' | 41.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 325 | 'lat' | 26.3797 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 325 | 'lon' | -98.8203 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 326 | 'air_temp_f' | 108.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 326 | 'normal_high_f' | 82.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 326 | 'anomaly' | 26.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 331 | 'lat' | 37.1886 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 331 | 'lon' | -99.7654 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 332 | 'air_temp_f' | 104.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 332 | 'normal_high_f' | 62.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 332 | 'anomaly' | 42.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 337 | 'lat' | 32.4207 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 337 | 'lon' | -104.2288 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 338 | 'air_temp_f' | 103.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 338 | 'normal_high_f' | 75.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 338 | 'anomaly' | 28.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 343 | 'lat' | 39.42 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 343 | 'lon' | -89.4562 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 344 | 'air_temp_f' | 94.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 344 | 'normal_high_f' | 55.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 344 | 'anomaly' | 39.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 351 | 'lat' | 41.9742 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 351 | 'lon' | -87.9073 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 352 | 'air_temp_f' | 81.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 352 | 'normal_high_f' | 49.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 352 | 'anomaly' | 32.0 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 368 | 'csi_level' | 2 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 377 | 'grid_resolution' | 0.5 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 381 | 'csi_level' | 3 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 390 | 'grid_resolution' | 0.5 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 394 | 'csi_level' | 4 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 403 | 'grid_resolution' | 0.5 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 407 | 'csi_level' | 5 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 416 | 'grid_resolution' | 0.5 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 420 | 'csi_level' | 5 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 429 | 'grid_resolution' | 0.5 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 433 | 'csi_level' | 5 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 442 | 'grid_resolution' | 0.5 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 446 | 'csi_level' | 5 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 455 | 'grid_resolution' | 0.5 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 459 | 'csi_level' | 5 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 468 | 'grid_resolution' | 0.5 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 472 | 'csi_level' | 4 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |

### sgr_a_grand_tour.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 45 | ANIMATION_FRAMES | 140 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 46 | POINTS_PER_ORBIT | 80 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 62 | REFERENCE_YEAR | 2025.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |

### social_media_export.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 263 | 'size' | 11 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 285 | 'size' | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 299 | 'size' | 12 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 310 | 'l' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 310 | 'r' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 310 | 't' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 322 | 'size' | 16 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 848 | result['confirmed'] | False | 4 | 2 | **8** | No source citation (recalled) | Internal use |

### spacecraft_encounters.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 98 | 'dist_km' | 2305000 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 100 | 'v_kms' | 21.219 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 101 | 'v_helio_kms' | 23.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 115 | 'plot_days' | 120 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 116 | 'plot_scale_au' | 8.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 118 | 'plot_days_closeup' | 120 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 119 | 'plot_scale_au_closeup' | 0.1 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 125 | 'dist_km' | 12472 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 127 | 'v_kms' | 13.78 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 128 | 'v_helio_kms' | 14.52 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 141 | 'plot_days' | 28 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 142 | 'plot_scale_au' | 0.5 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 144 | 'plot_days_closeup' | 14 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 145 | 'plot_scale_au_closeup' | 0.002 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 151 | claim: 538.5 km | 538.5 km | 2 | 4 | **8** | Has source citation | In display string (hover text / INFO) |
| 153 | 'v_kms' | 14.43 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 154 | 'v_helio_kms' | 13.87 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 167 | 'plot_days' | 28 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 168 | 'plot_scale_au' | 0.5 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 170 | 'plot_days_closeup' | 3 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 171 | 'plot_scale_au_closeup' | 3e-05 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 209 | 'plot_days' | 2 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 210 | 'plot_scale_au' | 0.0005 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 212 | 'plot_days_closeup' | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 213 | 'plot_scale_au_closeup' | 0.0005 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 220 | 'dist_km' | 8900 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 240 | 'plot_days' | 10 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 241 | 'plot_scale_au' | 0.003 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 243 | 'plot_days_closeup' | 2 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 244 | 'plot_scale_au_closeup' | 0.0003 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 252 | 'v_kms' | 10.8 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 270 | 'plot_days' | 10 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 271 | 'plot_scale_au' | 0.003 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 273 | 'plot_days_closeup' | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 274 | 'plot_scale_au_closeup' | 0.0001 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 188 | 'dist_km' | 70377 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 250 | 'dist_km' | 6493 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 1402 | 'plot_scale_au' | 0.06 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |

### star_sphere_builder.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 29 | VMAG_LIMIT | 3.5 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 43 | OBLIQUITY_DEG | 23.4393 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 62 | CIRCLE_POINTS | 120 | 4 | 2 | **8** | No source citation (recalled) | Internal use |

### star_visualization_gui.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 112 | 'exists' | True | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 118 | 'exists' | False | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 119 | 'size_mb' | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |

### test_orbit_cache.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 52 | 'x' | 1.5 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 52 | 'y' | 0.2 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 52 | 'z' | 0.1 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 53 | 'x' | 1.51 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 53 | 'y' | 0.21 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 53 | 'z' | 0.11 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 54 | 'x' | 1.52 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 54 | 'y' | 0.22 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 54 | 'z' | 0.12 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 65 | 'x' | 5.2 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 65 | 'y' | 0.3 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 65 | 'z' | 0.15 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 66 | 'x' | 5.21 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 66 | 'y' | 0.31 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |
| 66 | 'z' | 0.16 | 3 | 2 | **6** | No source, contains date-sensitive claims | Internal use |

### vot_cache_manager.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 58 | 'limit' | 100.1 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 63 | 'limit' | 9.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 68 | 'limit' | 100.1 | 4 | 2 | **8** | No source citation (recalled) | Internal use |
| 73 | 'limit' | 9.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use |

---

## Tier 4: NO ACTION NEEDED (Score 1-4)

### spacecraft_encounters.py

| Line | Name | Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|-------|--:|--:|------:|---------------|-------------|
| 151 | 'dist_km' | 3538 | 2 | 2 | **4** | Has source citation | Internal use |

---

## How to Use This Audit

1. Start with INCONSISTENCIES -- these are confirmed problems
2. Work through Tier 1 (FIX NOW) findings
3. For each finding:
   a. Find the correct value from an authoritative source
   b. Update the value in constants_new.py
   c. Add `# Source: [citation]` comment
   d. Replace duplicates with imports
   e. Verify downstream behavior unchanged
4. Re-run this scanner to confirm fixes

Companion tools:
- module_atlas.py -- dependency graph for tracing propagation
- dep_trace.py -- fine-grained import tracing

---

*Generated by provenance_scanner.py -- Paloma's Orrery Developer Tools*
