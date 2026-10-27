<!-- Doc-Kind: generated | The provenance audit: every numeric claim scored against its citation, rebuilt by provenance_scanner.py on each run. Do not hand-edit. -->
# Paloma's Orrery -- Provenance Audit

Generated: October 27, 2026
Files scanned: 168
Total findings: 1189
Constants: 287 | Dicts: 69 | Display strings: 833

Unit of provenance: the smallest thing with a coherent source citation. A dict with one block-level `# Source:` comment is ONE unit; all its entries inherit that citation. A hover string with co-referring numbers is ONE unit.

**Color values are excluded from this audit.** RGB/color fields are never scored as claims (see _make_dict_unit), and a dict's block `# Source:` citation should never be read as covering that dict's `color` field(s), even when it covers everything else in the same unit. This does not mean color choices have no basis at all -- some are loosely informed by real imagery or composition data -- but color selection across this codebase is inconsistent in method: sometimes evidence-informed, sometimes chosen purely for visual contrast or distinction, sometimes arbitrary. Treat every color value as a developer/AI judgment call, not a measured or verified quantity, regardless of what citation sits nearby. (Tony's call, July 16, 2026; a low-priority wishlist item for a real, systematic color-accuracy pass is tracked at LEDGER_CONSOLIDATED.md L-124.)

---

## Run History

The last 6 recorded scanner runs, newest first. Written by provenance_history.py and tracked in git: when an audit was taken, and against which commit, is itself provenance.

A run is expected every 1 day(s). Nothing here affects the exit code -- the delta informs the push call, it does not make it.

| Run (UTC) | HEAD | Files | Total | T1 | T1 by domain | T2 | T3 | T4 | Gate T1 |
|-----------|------|------:|------:|---:|--------------|---:|---:|---:|--------:|
| 20261027T145449Z | `8d334e7` | 168 | 1189 | 276 | orrery 112, Earth System 149, stars 13, utilities 2 | 731 | 176 | 6 | 0 |
| 20261027T012531Z | `8f4173c` | 168 | 1189 | 276 | orrery 112, Earth System 149, stars 13, utilities 2 | 731 | 176 | 6 | 0 |
| 20261026T213028Z | `140db0a` | 168 | 1189 | 276 | orrery 112, Earth System 149, stars 13, utilities 2 | 731 | 176 | 6 | 0 |
| 20261026T200107Z | `5398439` | 170 | 1191 | 277 | orrery 112, Earth System 149, stars 13, utilities 2, unclassified 1 | 731 | 177 | 6 | 0 |
| 20261026T143725Z | `288e83f` | 168 | 1178 | 276 | orrery 112, Earth System 149, stars 13, utilities 2 | 724 | 172 | 6 | 0 |
| 20261026T012932Z | `d80aed3` | 169 | 1179 | 277 | orrery 112, Earth System 149, stars 13, utilities 2, unclassified 1 | 724 | 172 | 6 | 0 |

Change since the previous run: total +0, Tier-1 +0.

No file's Tier-1 count rose.

---

## Risk Matrix: Vulnerability x Criticality

**Vulnerability** (how likely to be wrong):
- 1 = Fetched (authoritative pipeline)
- 2 = Sourced (has citation)
- 3 = Stale (may have changed)
- 4 = Recalled (LLM training data, no citation)

**Criticality** (impact if wrong):
- 1 = Cosmetic (colors, labels)
- 2 = Internal (used but not imported elsewhere)
- 3 = Load-bearing (drives geometry) or imported 1-2x
- 4 = Public-facing (hover text, gallery)
- 5 = Propagating (imported by 3+ modules)

**Score = V x C** | Action thresholds:
- 16-20: FIX NOW
- 10-15: REVIEW
- 5-9: LOW PRIORITY
- 1-4: LOWEST PRIORITY

---

## Priority Summary

| Tier | Score | Action | Count |
|------|-------|--------|------:|
| 1 | 16-20 | FIX NOW | 276 |
| 2 | 10-15 | REVIEW | 731 |
| 3 | 5-9 | LOW PRIORITY | 176 |
| 4 | 1-4 | LOWEST PRIORITY | 6 |

**Whole tree, Tier-1: 276: orrery 112, Earth System 149, stars 13, utilities 2.** By each file's docstring `Domain:` tag; Findings by File Type below has every tier and every domain. The push gate is the Gate Path section, not this total.

**Tier 2 note (April 2026 audit):** All Tier-2 findings are documented
accepted residuals -- cited constants, V_STALE staleness flags on verified
strings, or known scanner limitations. No action required unless a new
uncited entry appears. See Accepted Residuals block below for details.

---

## Gate Path: Tier-1 on What Leaves the Orrery

The push gate is Tier-1 = 0 on the active build path, and it binds at export. This section reads the path from `data/constants_export.json` (the constants_new.py rows the website is served) and `data/objects_export.json` (the celestial_objects.py entries it serves), and names every Tier-1 finding on it.

**GATE PATH: 0 TIER-1 -- the push gate holds.**

Examined: 184 of 215 exported rows; 31 more are computed from other rows, whose inputs are scored where they are typed; 6 display string(s) in 89 served object(s). The whole tree's Tier-1 count is 276: orrery 112, Earth System 149, stars 13, utilities 2; most of them are off this path.

Exported rows computed from other rows (31): `CHROMOSPHERE_TOP_KM`, `CORONA_BASE_KM`, `DEG_PER_RAD`, `EARTH_BOW_SHOCK_STANDOFF_RADII`, `EARTH_DIPOLE_TILT_DEG`, `EARTH_DIPOLE_TILT_RATE_DEG_PER_YEAR`, `EARTH_GEOSTATIONARY_RADIUS_KM`, `EARTH_HILL_SPHERE_KM`, `EARTH_LEO_INNER_KM`, `EARTH_LEO_INNER_PERIOD_MIN`, `EARTH_LEO_OUTER_KM`, `EARTH_LEO_OUTER_PERIOD_MIN`, `EARTH_LOWER_MANTLE_KM`, `EARTH_MAGNETOPAUSE_STANDOFF_RADII`, `EARTH_MAGNETOTAIL_DRAWN_END_RADII`, `EARTH_MAGNETOTAIL_DRAWN_RADIUS_RADII`, `EARTH_OBLIQUITY_J2000_DEG`, `EARTH_SIDEREAL_ROTATION_PERIOD_H`, `EARTH_STRATOPAUSE_RADIUS_KM`, `EARTH_THERMOPAUSE_RADIUS_KM`, `EARTH_VAN_ALLEN_OUTER_RADII`, `GALACTIC_NORTH_POLE_DEC_J2000_DEG`, `HELMET_CUSP_RADII`, `INNER_LIMIT_OORT_CLOUD_AU`, `OUTER_OORT_CLOUD_AU`, `PARKER_CLOSEST_KM`, `ROCHE_LIMIT_DRAWN_RADII`, `SGR_A_STAR_DEC_ICRS_DEG`, `SGR_A_STAR_RA_ICRS_DEG`, `SUN_EQUATOR_TILT_DEG`, `SUN_SIDEREAL_ROTATION_PERIOD_D`.

---

## Declared Rows (28)

Rows whose own comment block says `# Status: declared` and gives the reason, on a `# Declared:` line or after `--` on the Status line. A declared value is a choice with its reason written down, not a measurement missing its source, so it is not scored and never counts as Tier-1. Listed by name so the set stays visible; `declared pending` rows are backlog and carry a ledger handle (provenance-discipline, Measured Is the Goal).

| File | Line | Row | Status | Reason on |
|------|-----:|-----|--------|-----------|
| `constants_new.py` | 697 | `S_PER_HOUR` | Status: declared 2026-09-23 -- an exact unit conversion, seconds in one | Status line |
| `constants_new.py` | 720 | `S_PER_DAY` | Status: declared 2026-10-12 -- an exact unit conversion, seconds in one | Status line |
| `constants_new.py` | 739 | `S_PER_MINUTE` | Status: declared 2026-10-18 -- an exact unit conversion, seconds in one | Status line |
| `constants_new.py` | 759 | `D_PER_JULIAN_YEAR` | Status: declared 2026-10-11 -- an exact unit conversion, days in one | Status line |
| `constants_new.py` | 789 | `EARTH_POLE_RA_J2000_DEG` | Status: declared 2026-09-23 -- a frame definition, the FALLBACK only | Declared line |
| `constants_new.py` | 826 | `EARTH_POLE_DEC_J2000_DEG` | Status: declared 2026-09-23 -- a frame definition, the FALLBACK only | Declared line |
| `constants_new.py` | 838 | `ARCSEC_PER_DEG` | Status: declared 2026-09-23 -- an exact unit conversion, arcseconds in | Status line |
| `constants_new.py` | 857 | `EARTH_OBLIQUITY_J2000_ARCSEC` | Status: declared 2026-09-23 -- a frame definition, not a measurement | Declared line |
| `constants_new.py` | 895 | `GALACTIC_NORTH_POLE_RA_J2000_DEG` | Status: declared 2026-10-02 -- a frame definition, not a measurement | Declared line |
| `constants_new.py` | 941 | `GALACTIC_NORTH_POLE_DEC_J2000_ARCSEC` | Status: declared 2026-10-02 -- a frame definition, not a measurement | Declared line |
| `constants_new.py` | 2034 | `DEG_PER_TURN` | Status: declared 2026-10-22 -- an exact unit conversion, degrees in one | Status line |
| `constants_new.py` | 2279 | `EARTH_SOLAR_WIND_PRESSURE_NPA` | Status: declared pending 2026-09-12 -- L-314 | Declared line |
| `constants_new.py` | 2297 | `EARTH_SOLAR_WIND_BZ_NT` | Status: declared pending 2026-09-12 -- L-314 | Declared line |
| `constants_new.py` | 2309 | `EARTH_SOLAR_WIND_SPEED_KM_S` | Status: declared pending 2026-09-12 -- L-314 | Declared line |
| `constants_new.py` | 2478 | `EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG` | Status: declared 2026-09-14 -- a drawing limit, not an edge | Declared line |
| `constants_new.py` | 2573 | `EARTH_BOW_SHOCK_CUT_ANGLE_DEG` | Status: declared 2026-09-21 -- a drawing limit, not an edge | Declared line |
| `constants_new.py` | 3344 | `INNER_CORONA_RADII` | Status: declared 2026-08-29 -- a stated CONVENTION, not a | Status line |
| `constants_new.py` | 3373 | `OUTER_CORONA_RADII` | Status: declared 2026-10-04 -- a boundary chosen for the drawing, L-371 | Declared line |
| `constants_new.py` | 3816 | `ZODIACAL_DUST_OUTER_AU` | Status: declared 2026-10-19 -- the drawing stops where the COBE model | Status line |
| `constants_new.py` | 4303 | `HILLS_CLOUD_PLANES_NODE_CELL_DEG` | Status: declared 2026-10-10 -- the width of a cell in the reading of | Declared line |
| `constants_new.py` | 4313 | `HILLS_CLOUD_PLANES_INCL_CELL_DEG` | Status: declared 2026-10-10 -- the height of a cell in the reading of | Declared line |
| `constants_new.py` | 4320 | `HILLS_CLOUD_PLANES_READ` | Status: declared 2026-10-10 -- a reading of the paper's Fig. 3, which | Declared line |
| `constants_new.py` | 4558 | `HILLS_CLOUD_ECCENTRICITY` | Status: declared 2026-10-10 -- chosen for the picture; the paper shows | Declared line |
| `constants_new.py` | 5286 | `DE430_TERRESTRIAL_POSITION_PLACE_KM` | Status: declared 2026-10-01 -- the reporting place of the source's | Declared line |
| `constants_new.py` | 5314 | `DE430_JUPITER_SATURN_POSITION_PLACE_KM` | Status: declared 2026-10-01 -- the reporting place of the source's | Declared line |
| `constants_new.py` | 5338 | `DE430_URANUS_NEPTUNE_PLUTO_POSITION_PLACE_KM` | Status: declared 2026-10-01 -- the reporting place of the source's | Declared line |
| `constants_new.py` | 5365 | `DE430_MOON_POSITION_PLACE_KM` | Status: declared 2026-10-12 -- the reporting place of the source's | Declared line |
| `constants_new.py` | 5693 | `M3_PER_KM3` | Status: declared 2026-09-19 -- an exact unit conversion, 1 km^3 = 1e9 m^3. | Status line |

---

## Findings by File

Quick-reference counts before the per-tier detail below. Same data, grouped the other way: every file that has at least one finding, with its count in each tier.

| File | Domain | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Total |
|------|--------|-------:|-------:|-------:|-------:|------:|
| `constants_new.py` | orrery | 1 | 174 | 4 | 2 | 181 |
| `info_dictionary.py` | orrery | 2 | 125 | 2 | 0 | 129 |
| `shell_configs.py` | orrery | 35 | 72 | 0 | 0 | 107 |
| `paleoclimate_wet_bulb_full.py` | earth_science | 44 | 22 | 0 | 0 | 66 |
| `paleoclimate_human_origins_full.py` | earth_science | 40 | 6 | 0 | 0 | 46 |
| `star_notes.py` | stars | 1 | 37 | 0 | 0 | 38 |
| `idealized_orbits.py` | orrery | 24 | 12 | 0 | 0 | 36 |
| `celestial_objects.py` | orrery | 0 | 35 | 0 | 0 | 35 |
| `paleoclimate_visualization_full.py` | earth_science | 28 | 6 | 0 | 0 | 34 |
| `neptune_visualization_shells.py` | orrery | 0 | 28 | 0 | 0 | 28 |
| `comet_visualization_shells.py` | orrery | 4 | 22 | 0 | 0 | 26 |
| `uranus_visualization_shells.py` | orrery | 1 | 24 | 0 | 0 | 25 |
| `earth_visualization_shells.py` | earth_science | 0 | 19 | 0 | 0 | 19 |
| `jupiter_visualization_shells.py` | orrery | 0 | 19 | 0 | 0 | 19 |
| `planet_visualization_utilities.py` | orrery | 4 | 12 | 1 | 0 | 17 |
| `solar_visualization_shells.py` | orrery | 2 | 15 | 0 | 0 | 17 |
| `path_plan.py` | dev_tools | 0 | 0 | 16 | 0 | 16 |
| `provenance_scanner.py` | dev_tools | 0 | 0 | 16 | 0 | 16 |
| `venus_visualization_shells.py` | orrery | 3 | 4 | 6 | 0 | 13 |
| `scenarios_heatwaves.py` | earth_science | 3 | 9 | 0 | 0 | 12 |
| `test_orbit_markers.py` | dev_tools | 0 | 0 | 12 | 0 | 12 |
| `scenarios_western_heatwave_march_2026.py` | earth_science | 10 | 1 | 0 | 0 | 11 |
| `sgr_a_grand_tour.py` | orrery | 8 | 0 | 3 | 0 | 11 |
| `mars_visualization_shells.py` | orrery | 4 | 3 | 4 | 0 | 11 |
| `mercury_visualization_shells.py` | orrery | 1 | 5 | 5 | 0 | 11 |
| `moon_visualization_shells.py` | orrery | 3 | 4 | 4 | 0 | 11 |
| `paleoclimate_dual_scale.py` | earth_science | 10 | 1 | 0 | 0 | 11 |
| `pluto_visualization_shells.py` | orrery | 0 | 0 | 11 | 0 | 11 |
| `saturn_visualization_shells.py` | orrery | 1 | 9 | 0 | 0 | 10 |
| `food_insecurity_generator.py` | earth_science | 5 | 2 | 2 | 0 | 9 |
| `skills_index.py` | dev_tools | 0 | 0 | 9 | 0 | 9 |
| `eris_visualization_shells.py` | orrery | 2 | 4 | 2 | 0 | 8 |
| `asteroid_belt_visualization_shells.py` | orrery | 0 | 7 | 0 | 0 | 7 |
| `spacecraft_encounters.py` | orrery | 0 | 7 | 0 | 0 | 7 |
| `star_sphere_builder.py` | stars | 0 | 1 | 3 | 3 | 7 |
| `sgr_a_star_data.py` | orrery | 3 | 3 | 0 | 0 | 6 |
| `paleoclimate_visualization.py` | earth_science | 6 | 0 | 0 | 0 | 6 |
| `position_accuracy.py` | orrery | 0 | 5 | 1 | 0 | 6 |
| `test_position_digits.py` | dev_tools | 0 | 0 | 6 | 0 | 6 |
| `exoplanet_coordinates.py` | stars | 5 | 0 | 0 | 0 | 5 |
| `earth_pole_of_date.py` | orrery | 0 | 5 | 0 | 0 | 5 |
| `fetch_climate_data.py` | earth_science | 0 | 5 | 0 | 0 | 5 |
| `planet9_visualization_shells.py` | orrery | 0 | 5 | 0 | 0 | 5 |
| `worksheet_checker.py` | dev_tools | 0 | 0 | 5 | 0 | 5 |
| `coordinate_system_guide.py` | orrery | 2 | 2 | 0 | 0 | 4 |
| `sgr_a_visualization_precession.py` | orrery | 4 | 0 | 0 | 0 | 4 |
| `orbital_period.py` | orrery | 0 | 3 | 0 | 1 | 4 |
| `orrery_maintenance_run.py` | dev_tools | 0 | 0 | 4 | 0 | 4 |
| `palomas_orrery_dashboard.py` | orrery | 0 | 0 | 4 | 0 | 4 |
| `provenance_history.py` | dev_tools | 0 | 0 | 4 | 0 | 4 |
| `test_path_plan.py` | dev_tools | 0 | 0 | 4 | 0 | 4 |
| `horizons_check.py` | dev_tools | 0 | 0 | 4 | 0 | 4 |
| `object_type_analyzer.py` | orrery | 3 | 0 | 0 | 0 | 3 |
| `orrery_rendering.py` | orrery | 2 | 1 | 0 | 0 | 3 |
| `scenarios_coral_bleaching.py` | earth_science | 1 | 2 | 0 | 0 | 3 |
| `sgr_a_visualization_core.py` | orrery | 1 | 2 | 0 | 0 | 3 |
| `visualization_3d.py` | stars | 0 | 3 | 0 | 0 | 3 |
| `dep_trace.py` | dev_tools | 0 | 0 | 3 | 0 | 3 |
| `doc_index.py` | dev_tools | 0 | 0 | 3 | 0 | 3 |
| `ledger_index.py` | dev_tools | 0 | 0 | 3 | 0 | 3 |
| `measure_perframe_elements.py` | dev_tools | 0 | 0 | 3 | 0 | 3 |
| `module_atlas.py` | dev_tools | 0 | 0 | 3 | 0 | 3 |
| `palomas_orrery.py` | orrery | 0 | 0 | 3 | 0 | 3 |
| `exoplanet_systems.py` | stars | 0 | 0 | 3 | 0 | 3 |
| `energy_imbalance.py` | earth_science | 1 | 1 | 0 | 0 | 2 |
| `plot_data_report_widget.py` | utilities | 2 | 0 | 0 | 0 | 2 |
| `sgr_a_visualization_animation.py` | orrery | 1 | 0 | 1 | 0 | 2 |
| `apsidal_markers.py` | orrery | 0 | 2 | 0 | 0 | 2 |
| `close_approach_data.py` | orrery | 0 | 1 | 1 | 0 | 2 |
| `export_objects.py` | dev_tools | 0 | 0 | 2 | 0 | 2 |
| `orbit_data_manager.py` | orrery | 0 | 0 | 2 | 0 | 2 |
| `test_dashboard_parity.py` | dev_tools | 0 | 0 | 2 | 0 | 2 |
| `worksheet_request_builder.py` | dev_tools | 0 | 0 | 2 | 0 | 2 |
| `orbital_elements.py` | orrery | 1 | 0 | 0 | 0 | 1 |
| `data_acquisition.py` | stars | 1 | 0 | 0 | 0 | 1 |
| `exoplanet_orbits.py` | stars | 1 | 0 | 0 | 0 | 1 |
| `fetch_paleoclimate_data.py` | earth_science | 1 | 0 | 0 | 0 | 1 |
| `hr_diagram_distance.py` | stars | 1 | 0 | 0 | 0 | 1 |
| `messier_catalog.py` | stars | 1 | 0 | 0 | 0 | 1 |
| `planetarium_distance.py` | stars | 1 | 0 | 0 | 0 | 1 |
| `visualization_core.py` | stars | 1 | 0 | 0 | 0 | 1 |
| `visualization_utils.py` | stars | 1 | 0 | 0 | 0 | 1 |
| `earth_pole_live_check.py` | orrery | 0 | 1 | 0 | 0 | 1 |
| `celestial_coordinates.py` | orrery | 0 | 1 | 0 | 0 | 1 |
| `earth_exosphere_sampler.py` | orrery | 0 | 1 | 0 | 0 | 1 |
| `hills_cloud_sampler.py` | orrery | 0 | 1 | 0 | 0 | 1 |
| `sun_corona_sampler.py` | orrery | 0 | 1 | 0 | 0 | 1 |
| `zodiacal_dust_sampler.py` | orrery | 0 | 1 | 0 | 0 | 1 |
| `add_docstrings.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |
| `data_inventory.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |
| `export_drawings.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |
| `osculating_cache_manager.py` | orrery | 0 | 0 | 1 | 0 | 1 |
| `test_dimensions.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |
| `test_domain_split.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |
| `test_objects_export.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |
| `test_period_fetch.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |
| `test_reset_completeness.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |
| `worksheet_key_aliases.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |
| `worksheet_keys.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |
| `export_constants.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |
| `export_orbit_cache.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |

---

## Findings by File Type

Same data again, grouped by subject-matter domain rather than by individual file -- orrery, earth science, gallery, stars, utilities, dev tools. Domain is a report-only grouping, read from each module's own docstring `Domain:` tag (classify_domain(), through module_atlas.py's reader); it does not affect which files get scanned or scored. The Tier 1 column sums to the whole-tree split in the Priority Summary.

| Domain | Files | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Total |
|--------|------:|-------:|-------:|-------:|-------:|------:|
| Orrery (solar system + orbital mechanics) | 45 | 112 | 616 | 55 | 3 | 786 |
| Earth System | 13 | 149 | 74 | 2 | 0 | 225 |
| Dev Tools (audit, diagnostics, one-shot scripts) | 30 | 0 | 0 | 113 | 0 | 113 |
| Stars (stellar neighborhood) | 12 | 13 | 41 | 6 | 3 | 63 |
| Utilities (cross-domain shared helpers) | 1 | 2 | 0 | 0 | 0 | 2 |
| Gallery | 0 | 0 | 0 | 0 | 0 | 0 |
| Unclassified (no Domain: tag, or one outside the six) | 0 | 0 | 0 | 0 | 0 | 0 |

**Domain coverage:** all 101 files with findings declare a `Domain:` tag the report knows.

---

## SHADOW CONSTANTS -- [CRITICAL] convention violation

Local copies of values that are already defined and cited in `constants_new.py`. The number may be correct today; the problem is that it will not follow if the source value is ever corrected, and it sits outside the citation chain in the meantime.

Per provenance-discipline v1.3, No Shadow Constants [CRITICAL]: delete the local definition and import the real one, through the `planet_visualization_utilities` shim or directly. Do NOT add a `# Source:` comment to the local copy -- that cites-to-clear a structural problem instead of fixing it.

`direct` means the local name and value both match a cited constant. `derived` means the value is computed from pinned literals rather than from the imported names.

| File | Line | Name | Kind |
|------|-----:|------|------|
| `path_plan.py` | 244 | `BACKBONE_STEP_SECONDS` | derived |

---

## ORPHAN ANNOTATIONS -- diagnostic, no scoring effect

Cross-check annotations that touch no claim's own statement. They granted no credit. A citation may be inherited from a section header; an annotation may not, because it names one checker who verified one value.

Each of these was written for something. Either it belongs on a specific value -- move it down and the credit follows -- or it was meant to cover a group, which this codebase does not express. Nothing here is safe to delete without reading the worksheet it names.

| File | Line | Annotation |
|------|-----:|------------|
| `constants_new.py` | 3133 | # Cross-checked: Gemini 2026-08-02 -- Carroll & Ostlie (worksheet_gemini_constants_remaining.md) |
| `constants_new.py` | 3134 | # Cross-checked: GPT 2026-08-02 -- NASA Sun Fact Sheet (constants_new_citation_verification_gpt.md) |
| `constants_new.py` | 4672 | # Cross-checked: Claude 2026-08-02 -- IAU B3 / Archinal / JPL SSD (worksheet_claude_constants_new.md) |
| `constants_new.py` | 4673 | # Cross-checked: GPT 2026-08-02 -- IAU B3 / Archinal / JPL SSD (constants_new_citation_verification_gpt.md) |

---

## CITATION LEVEL MISMATCH -- diagnostic, no scoring effect

Citations in this codebase attach to a block. The resolver reads exactly one block per string: the narrowest one containing it. A citation written one level further out is invisible to it. Nothing below is mis-scored today -- the flat 60-line context window catches these independently, which is exactly why the mismatch is easy to miss. Move a few lines and it becomes a real gap with no warning.

### Shadowed strings

The string sits in a block with no citation, inside a block that has one. Fix by repeating a short citation above the inner block's key, as done for `ring_params` -- not by loosening the resolver, which would clear the L-173 gaps by accident.

| File | Line | Shadowed from | Its citation at |
|------|-----:|---------------|----------------:|
| `comet_visualization_shells.py` | 128 | `HISTORICAL_TAIL_DATA` | 115 |
| `comet_visualization_shells.py` | 244 | `HISTORICAL_TAIL_DATA` | 115 |
| `comet_visualization_shells.py` | 270 | `HISTORICAL_TAIL_DATA` | 115 |
| `comet_visualization_shells.py` | 329 | `HISTORICAL_TAIL_DATA` | 115 |
| `comet_visualization_shells.py` | 340 | `HISTORICAL_TAIL_DATA` | 115 |
| `comet_visualization_shells.py` | 369 | `HISTORICAL_TAIL_DATA` | 115 |
| `planet_visualization_utilities.py` | 548 | `PLANET_ROTATION` | 539 |
| `planet_visualization_utilities.py` | 552 | `PLANET_ROTATION` | 539 |
| `planet_visualization_utilities.py` | 556 | `PLANET_ROTATION` | 539 |
| `planet_visualization_utilities.py` | 571 | `PLANET_ROTATION` | 539 |
| `planet_visualization_utilities.py` | 575 | `PLANET_ROTATION` | 539 |
| `planet_visualization_utilities.py` | 579 | `PLANET_ROTATION` | 539 |
| `planet_visualization_utilities.py` | 583 | `PLANET_ROTATION` | 539 |
| `planet_visualization_utilities.py` | 587 | `PLANET_ROTATION` | 539 |
| `planet_visualization_utilities.py` | 591 | `PLANET_ROTATION` | 539 |
| `planet_visualization_utilities.py` | 595 | `PLANET_ROTATION` | 539 |

---

## Accepted Residuals (data/provenance_exceptions.json)

The following findings are documented exceptions -- known false positives
or deliberately deferred items. They appear in lower tiers but require
no action unless the underlying file is being actively modified.

**info_dictionary.py** (Tier 2) -- V_STALE false positives
  Tier-2 V_STALE findings are multi-line string continuation false positives. Citations exist at entry-key level (# Source: above dict key). Verified correct by Gemini fact-check April 2026. Not real gaps.

**spacecraft_encounters.py** (Tier 2) -- Inline source key not recognized
  Artemis II entries carry 'source': 'NASA/JSC' as a dict value. Scanner requires # Source: comment format. Verified correct. Future fix: extend SOURCE_PATTERNS to recognize dict-value citations.

**star_notes.py** (Tier 2) -- Large dict V_STALE
  553-entry stellar parameters dict. Verified against SIMBAD/Gaia DR3 April 2026. V_STALE flag reflects real staleness risk as catalogs improve. Review when adding new stars, not as standalone task.

**constants_new.py** (Tier 2) -- V_SOURCED x C_PROPAGATING (score 10)
  All Tier-2 items have source citations (V=2). Score 10 = cited constant imported by 3+ modules. Not errors -- these are the best-cited values in the codebase.

**comet_visualization_shells.py** (Tier 2) -- Rendering geometry dicts
  Feature thresholds drive shell rendering geometry. Low user-visible impact if slightly off. Deferred until comet shell refactor. (2026-10-26, L-491: COMET_NUCLEUS_SIZES left this entry; it was printed in hovers, not geometry, and is now sourced rows in constants_new.py.)

---

## INCONSISTENCIES

None detected. No same-concept constants with differing 
values found across files.

Note: this does NOT rule out silent shadowing (a local 
dict with different name but overlapping keys). That 
pattern is the April 16 bug family; shadow detection 
is planned for a future session.

---

## Tier 1: FIX NOW (Score 16-20)

### comet_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1658 | dict | COMET_FEATURE_THRESHOLDS[...] | (3 entries) | 4 | 5 | **20** | No source citation (recalled) | MEASURED -- independently catalogued fact (name) |
| 1 | string | display string @ line 1 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1239 | string | display string @ line 1239 | (5 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 2064 | string | display string @ line 2064 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### constants_new.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 4779 | dict | CENTER_BODY_RADII[...] | (1 entry) | 4 | 4 | **16** | No source citation (recalled) | RELATIONAL -- defined against a tracked base (name) |

### coordinate_system_guide.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 123 | string | display string @ line 123 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 156 | string | display string @ line 156 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### data_acquisition.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 202 | string | display string @ line 202 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### energy_imbalance.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 535 | string | display string @ line 535 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### eris_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 140 | string | display string @ line 140 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 157 | string | display string @ line 157 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### exoplanet_coordinates.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 41 | string | display string @ line 41 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 94 | string | display string @ line 94 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 133 | string | display string @ line 133 | (5 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 307 | string | display string @ line 307 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 315 | string | display string @ line 315 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### exoplanet_orbits.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 291 | string | display string @ line 291 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### fetch_paleoclimate_data.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 152 | string | display string @ line 152 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### food_insecurity_generator.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 315 | string | display string @ line 315 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 357 | string | display string @ line 357 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 404 | string | display string @ line 404 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 434 | string | display string @ line 434 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### hr_diagram_distance.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 220 | string | display string @ line 220 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### idealized_orbits.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 153 | string | display string @ line 153 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 168 | string | display string @ line 168 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 196 | string | display string @ line 196 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 210 | string | display string @ line 210 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1490 | string | display string @ line 1490 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1549 | string | display string @ line 1549 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1560 | string | display string @ line 1560 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1673 | string | display string @ line 1673 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1793 | string | display string @ line 1793 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2471 | string | display string @ line 2471 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2494 | string | display string @ line 2494 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2517 | string | display string @ line 2517 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2539 | string | display string @ line 2539 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2554 | string | display string @ line 2554 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2565 | string | display string @ line 2565 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2598 | string | display string @ line 2598 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2896 | string | display string @ line 2896 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 3018 | string | display string @ line 3018 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 3895 | string | display string @ line 3895 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4372 | string | display string @ line 4372 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4639 | string | display string @ line 4639 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4661 | string | display string @ line 4661 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4725 | string | display string @ line 4725 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4759 | string | display string @ line 4759 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### info_dictionary.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 2170 | string | display string @ line 2170 | (7 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 2196 | string | display string @ line 2196 | (1 claim) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |

### mars_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 338 | string | display string @ line 338 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 359 | string | display string @ line 359 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 502 | string | display string @ line 502 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 522 | string | display string @ line 522 | (5 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### mercury_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### messier_catalog.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 216 | string | display string @ line 216 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### moon_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 315 | string | display string @ line 315 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 337 | string | display string @ line 337 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 514 | string | display string @ line 514 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### object_type_analyzer.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 655 | string | display string @ line 655 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 662 | string | display string @ line 662 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 680 | string | display string @ line 680 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### orbital_elements.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1433 | dict | planet_tilts[...] | (7 entries) | 4 | 5 | **20** | No source citation (recalled) | MEASURED -- independently catalogued fact (name) |

### orrery_rendering.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 271 | string | display string @ line 271 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### paleoclimate_dual_scale.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 688 | string | display string @ line 688 | (6 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 717 | string | display string @ line 717 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 775 | string | display string @ line 775 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 804 | string | display string @ line 804 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 833 | string | display string @ line 833 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 862 | string | display string @ line 862 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 891 | string | display string @ line 891 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 905 | string | display string @ line 905 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 994 | string | display string @ line 994 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1050 | string | display string @ line 1050 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### paleoclimate_human_origins_full.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 142 | string | display string @ line 142 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 151 | string | display string @ line 151 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 171 | string | display string @ line 171 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 172 | string | display string @ line 172 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 174 | string | display string @ line 174 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 175 | string | display string @ line 175 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 177 | string | display string @ line 177 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 182 | string | display string @ line 182 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 203 | string | display string @ line 203 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 209 | string | display string @ line 209 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 223 | string | display string @ line 223 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 231 | string | display string @ line 231 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 239 | string | display string @ line 239 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 365 | string | display string @ line 365 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 433 | string | display string @ line 433 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 893 | string | display string @ line 893 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 952 | string | display string @ line 952 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 979 | string | display string @ line 979 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1063 | string | display string @ line 1063 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1119 | string | display string @ line 1119 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1147 | string | display string @ line 1147 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1175 | string | display string @ line 1175 | (6 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1366 | string | display string @ line 1366 | (9 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1413 | string | display string @ line 1413 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1443 | string | display string @ line 1443 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1484 | string | display string @ line 1484 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1563 | string | display string @ line 1563 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1621 | string | display string @ line 1621 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1641 | string | display string @ line 1641 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1661 | string | display string @ line 1661 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1687 | string | display string @ line 1687 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1712 | string | display string @ line 1712 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1733 | string | display string @ line 1733 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1756 | string | display string @ line 1756 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1779 | string | display string @ line 1779 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1802 | string | display string @ line 1802 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1850 | string | display string @ line 1850 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1908 | string | display string @ line 1908 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1937 | string | display string @ line 1937 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2012 | string | display string @ line 2012 | (1 claim) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |

### paleoclimate_visualization.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 62 | string | display string @ line 62 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 132 | string | display string @ line 132 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 200 | string | display string @ line 200 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 423 | string | display string @ line 423 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 457 | string | display string @ line 457 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 509 | string | display string @ line 509 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### paleoclimate_visualization_full.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 65 | string | display string @ line 65 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 191 | string | display string @ line 191 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 259 | string | display string @ line 259 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 496 | string | display string @ line 496 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 523 | string | display string @ line 523 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 550 | string | display string @ line 550 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 634 | string | display string @ line 634 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 690 | string | display string @ line 690 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 718 | string | display string @ line 718 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 746 | string | display string @ line 746 | (6 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 937 | string | display string @ line 937 | (9 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 984 | string | display string @ line 984 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1014 | string | display string @ line 1014 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1055 | string | display string @ line 1055 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1134 | string | display string @ line 1134 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1192 | string | display string @ line 1192 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1212 | string | display string @ line 1212 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1232 | string | display string @ line 1232 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1258 | string | display string @ line 1258 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1283 | string | display string @ line 1283 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1304 | string | display string @ line 1304 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1327 | string | display string @ line 1327 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1350 | string | display string @ line 1350 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1373 | string | display string @ line 1373 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1421 | string | display string @ line 1421 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1479 | string | display string @ line 1479 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1508 | string | display string @ line 1508 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1583 | string | display string @ line 1583 | (1 claim) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |

### paleoclimate_wet_bulb_full.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 93 | string | display string @ line 93 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 99 | string | display string @ line 99 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 109 | string | display string @ line 109 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 110 | string | display string @ line 110 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 111 | string | display string @ line 111 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 112 | string | display string @ line 112 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 113 | string | display string @ line 113 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 115 | string | display string @ line 115 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 122 | string | display string @ line 122 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 125 | string | display string @ line 125 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 222 | string | display string @ line 222 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 240 | string | display string @ line 240 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 246 | string | display string @ line 246 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 253 | string | display string @ line 253 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 271 | string | display string @ line 271 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 277 | string | display string @ line 277 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 341 | string | display string @ line 341 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 349 | string | display string @ line 349 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 475 | string | display string @ line 475 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 617 | string | display string @ line 617 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1131 | string | display string @ line 1131 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1329 | string | display string @ line 1329 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1347 | string | display string @ line 1347 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1374 | string | display string @ line 1374 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1458 | string | display string @ line 1458 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1514 | string | display string @ line 1514 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1542 | string | display string @ line 1542 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1570 | string | display string @ line 1570 | (6 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1761 | string | display string @ line 1761 | (9 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1808 | string | display string @ line 1808 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1838 | string | display string @ line 1838 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1879 | string | display string @ line 1879 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1958 | string | display string @ line 1958 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2016 | string | display string @ line 2016 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2036 | string | display string @ line 2036 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2056 | string | display string @ line 2056 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2082 | string | display string @ line 2082 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2107 | string | display string @ line 2107 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2128 | string | display string @ line 2128 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2151 | string | display string @ line 2151 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2174 | string | display string @ line 2174 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2197 | string | display string @ line 2197 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2332 | string | display string @ line 2332 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### planet_visualization_utilities.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 602 | dict | ROTATION_AXIS_OMITTED[...] | (2 entries) | 4 | 5 | **20** | No source citation (recalled) | UNDETERMINED -- could not be classified |
| 499 | string | display string @ line 499 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 799 | string | display string @ line 799 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 801 | string | display string @ line 801 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### planetarium_distance.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 231 | string | display string @ line 231 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### plot_data_report_widget.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 280 | string | display string @ line 280 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 414 | string | display string @ line 414 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### saturn_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 217 | string | display string @ line 217 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### scenarios_coral_bleaching.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 64 | string | display string @ line 64 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### scenarios_heatwaves.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 97 | dict | HEATWAVE_THRESHOLDS[...] | (15 entries) | 4 | 5 | **20** | No source citation (recalled) | MEASURED -- independently catalogued fact (name) |
| 205 | string | display string @ line 205 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 522 | string | display string @ line 522 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### scenarios_western_heatwave_march_2026.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 64 | dict | WESTERN_HEATWAVE_THRESHOLDS[...] | (15 entries) | 4 | 5 | **20** | No source citation (recalled) | MEASURED -- independently catalogued fact (name) |
| 1 | string | display string @ line 1 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 920 | string | display string @ line 920 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1164 | string | display string @ line 1164 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1174 | string | display string @ line 1174 | (1 claim) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 1226 | string | display string @ line 1226 | (5 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 1274 | string | display string @ line 1274 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1319 | string | display string @ line 1319 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1397 | string | display string @ line 1397 | (4 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 1474 | string | display string @ line 1474 | (1 claim) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |

### sgr_a_grand_tour.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 63 | constant | REFERENCE_YEAR | 2025.0 | 4 | 5 | **20** | No source citation (recalled) | UNDETERMINED -- could not be classified |
| 564 | string | display string @ line 564 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 576 | string | display string @ line 576 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 588 | string | display string @ line 588 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 600 | string | display string @ line 600 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 612 | string | display string @ line 612 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 622 | string | display string @ line 622 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 632 | string | display string @ line 632 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### sgr_a_star_data.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 61 | dict | B_STAR_TEMPERATURES[...] | (10 entries) | 4 | 5 | **20** | No source citation (recalled) | MEASURED -- independently catalogued fact (name) |
| 1 | string | display string @ line 1 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 226 | string | display string @ line 226 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### sgr_a_visualization_animation.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 361 | string | display string @ line 361 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### sgr_a_visualization_core.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 386 | string | display string @ line 386 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### sgr_a_visualization_precession.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 275 | string | display string @ line 275 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 415 | string | display string @ line 415 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 416 | string | display string @ line 416 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### shell_configs.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 638 | string | display string @ line 638 | (5 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 659 | string | display string @ line 659 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 675 | string | display string @ line 675 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 689 | string | display string @ line 689 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 704 | string | display string @ line 704 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 722 | string | display string @ line 722 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 739 | string | display string @ line 739 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 769 | string | display string @ line 769 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 788 | string | display string @ line 788 | (10 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 830 | string | display string @ line 830 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 838 | string | display string @ line 838 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 864 | string | display string @ line 864 | (5 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 912 | string | display string @ line 912 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 919 | string | display string @ line 919 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 936 | string | display string @ line 936 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 948 | string | display string @ line 948 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 964 | string | display string @ line 964 | (1 claim) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 1007 | string | display string @ line 1007 | (7 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 1016 | string | display string @ line 1016 | (7 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 1040 | string | display string @ line 1040 | (2 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 1046 | string | display string @ line 1046 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1085 | string | display string @ line 1085 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1093 | string | display string @ line 1093 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1108 | string | display string @ line 1108 | (5 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1118 | string | display string @ line 1118 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1135 | string | display string @ line 1135 | (6 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1146 | string | display string @ line 1146 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1162 | string | display string @ line 1162 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1171 | string | display string @ line 1171 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1298 | string | display string @ line 1298 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1309 | string | display string @ line 1309 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1323 | string | display string @ line 1323 | (5 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1337 | string | display string @ line 1337 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1350 | string | display string @ line 1350 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2169 | string | display string @ line 2169 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### solar_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 804 | string | display string @ line 804 | (12 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 1700 | string | display string @ line 1700 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### star_notes.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1260 | string | display string @ line 1260 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### uranus_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 936 | string | display string @ line 936 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### venus_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 226 | string | display string @ line 226 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 248 | string | display string @ line 248 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 473 | string | display string @ line 473 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### visualization_core.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 150 | string | display string @ line 150 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### visualization_utils.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 355 | string | display string @ line 355 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

---

## Tier 2: REVIEW (Score 10-15)

### apsidal_markers.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1835 | constant | ENCOUNTER_THRESHOLD_AU | 0.5 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1 | string | display string @ line 1 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### asteroid_belt_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 111 | constant | MAIN_BELT_INNER | 2.2 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 112 | constant | MAIN_BELT_OUTER | 3.2 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 113 | constant | MAIN_BELT_PEAK | 2.7 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 115 | constant | HILDA_DISTANCE | 3.97 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 116 | constant | TROJAN_DISTANCE | 5.2 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 80 | string | display string @ line 80 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 132 | string | display string @ line 132 | (7 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### celestial_coordinates.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 158 | string | display string @ line 158 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### celestial_objects.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 97 | string | display string @ line 97 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 145 | string | display string @ line 145 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 184 | string | display string @ line 184 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 200 | string | display string @ line 200 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 233 | string | display string @ line 233 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 300 | string | display string @ line 300 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 308 | string | display string @ line 308 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 331 | string | display string @ line 331 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 494 | string | display string @ line 494 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 679 | string | display string @ line 679 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 779 | string | display string @ line 779 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1062 | string | display string @ line 1062 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1067 | string | display string @ line 1067 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1072 | string | display string @ line 1072 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1077 | string | display string @ line 1077 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1197 | string | display string @ line 1197 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1202 | string | display string @ line 1202 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1257 | string | display string @ line 1257 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1264 | string | display string @ line 1264 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1271 | string | display string @ line 1271 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1278 | string | display string @ line 1278 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1285 | string | display string @ line 1285 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1291 | string | display string @ line 1291 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1297 | string | display string @ line 1297 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1307 | string | display string @ line 1307 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1315 | string | display string @ line 1315 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1323 | string | display string @ line 1323 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1331 | string | display string @ line 1331 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1339 | string | display string @ line 1339 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1347 | string | display string @ line 1347 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1355 | string | display string @ line 1355 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1363 | string | display string @ line 1363 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1382 | string | display string @ line 1382 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1405 | string | display string @ line 1405 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1413 | string | display string @ line 1413 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### close_approach_data.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### comet_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1590 | dict | comet_visualization_info[...] | (6 entries) | 3 | 5 | **15** | Cited, not independently cross-checked | UNDETERMINED -- could not be classified |
| 128 | string | display string @ line 128 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 244 | string | display string @ line 244 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 270 | string | display string @ line 270 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 291 | string | display string @ line 291 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 318 | string | display string @ line 318 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 329 | string | display string @ line 329 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 340 | string | display string @ line 340 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 369 | string | display string @ line 369 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 574 | string | display string @ line 574 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 583 | string | display string @ line 583 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 594 | string | display string @ line 594 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 600 | string | display string @ line 600 | (10 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 762 | string | display string @ line 762 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 767 | string | display string @ line 767 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1413 | string | display string @ line 1413 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1592 | string | display string @ line 1592 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1602 | string | display string @ line 1602 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1612 | string | display string @ line 1612 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1621 | string | display string @ line 1621 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1630 | string | display string @ line 1630 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1640 | string | display string @ line 1640 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### constants_new.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 414 | constant | EARTH_MEAN_RADIUS_KM | 6371.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 443 | constant | EARTH_INNER_CORE_KM | 1221.5 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 473 | constant | EARTH_OUTER_CORE_KM | 3480.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 511 | constant | EARTH_D660_DEPTH_KM | 660.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 573 | constant | EARTH_UPPER_MANTLE_KM | 6346.6 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 615 | constant | EARTH_GM_KM3_S2 | 398600.4418 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 637 | constant | EARTH_ROTATION_RATE_RAD_S | 7.292115e-05 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 962 | constant | SGR_A_STAR_RA_ICRS_ARCSEC | 959100.6 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 997 | constant | SGR_A_STAR_DEC_ICRS_ARCSEC | -104428.138 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 1034 | constant | SUN_POLE_RA_J2000_DEG | 286.13 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1053 | constant | SUN_POLE_DEC_J2000_DEG | 63.87 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1099 | constant | EARTH_LEO_UPPER_ALTITUDE_KM | 2000.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1131 | constant | EARTH_LEO_LOWER_ALTITUDE_KM | 180.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1188 | constant | EARTH_STRATOPAUSE_ALTITUDE_KM | 50.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1206 | constant | EARTH_THERMOPAUSE_ALTITUDE_KM | 600.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1285 | constant | EARTH_INNER_CORE_TEMPERATURE_K | 5600.0 | 3 | 5 | **15** | Cited, not cross-checked; date-sensitive | MEASURED -- independently catalogued fact (name) |
| 1308 | constant | EARTH_CRUST_OCEANIC_THICKNESS_KM | 5.0 | 3 | 5 | **15** | Cited, not cross-checked; date-sensitive | MEASURED -- independently catalogued fact (name) |
| 1321 | constant | EARTH_CRUST_CONTINENTAL_THICKNESS_KM | 30.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1331 | constant | EARTH_SURFACE_COLDEST_K | 184.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 1348 | constant | EARTH_SURFACE_HOTTEST_K | 329.8 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 1364 | constant | EARTH_TROPOPAUSE_ALTITUDE_KM | 12.0 | 3 | 5 | **15** | Cited, not cross-checked; date-sensitive | MEASURED -- independently catalogued fact (name) |
| 1380 | constant | EARTH_SURFACE_MEAN_TEMPERATURE_K | 290.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1397 | constant | EARTH_TROPOPAUSE_TEMPERATURE_K | 222.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1411 | constant | EARTH_THERMOSPHERE_TOP_TEMPERATURE_K | 2000.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1451 | constant | APOPHIS_2029_APPROACH_ALTITUDE_KM | 32000.0 | 3 | 5 | **15** | Cited, not cross-checked; date-sensitive | MEASURED -- independently catalogued fact (name) |
| 1469 | constant | EARTH_CORE_MANTLE_BOUNDARY_TEMPERATURE_K | 4100.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1492 | constant | EARTH_INNER_CORE_BOUNDARY_TEMPERATURE_K | 5580.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1512 | constant | EARTH_UPPER_MANTLE_TOP_TEMPERATURE_K | 1646.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1530 | constant | EARTH_UPPER_MANTLE_BASE_TEMPERATURE_K | 1994.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1543 | constant | EARTH_LOWER_MANTLE_TOP_TEMPERATURE_K | 1960.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1557 | constant | EARTH_ATMOSPHERE_MASS_BELOW_STRATOPAUSE_ | 99.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1574 | constant | EARTH_THERMOPAUSE_LOW_KM | 500.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1589 | constant | EARTH_THERMOPAUSE_HIGH_KM | 1000.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1623 | constant | MOON_SEMI_MAJOR_AXIS_KM | 384400.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1636 | constant | ISS_ALTITUDE_LOW_KM | 370.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1649 | constant | ISS_ALTITUDE_HIGH_KM | 460.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1658 | constant | ISS_INCLINATION_DEG | 51.6 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1667 | constant | HUBBLE_ALTITUDE_KM | 550.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1713 | constant | STARLINK_PEAK_ALTITUDE_KM | 550.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1781 | constant | EARTH_VAN_ALLEN_OUTER_BAND_LOW_L | 4.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 1813 | constant | EARTH_VAN_ALLEN_OUTER_BAND_HIGH_L | 5.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 1874 | constant | EARTH_VAN_ALLEN_INNER_BELT_INNER_EDGE | 1.1 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1900 | constant | EARTH_VAN_ALLEN_INNER_BELT_OUTER_EDGE | 2.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1925 | constant | EARTH_VAN_ALLEN_OUTER_BELT_INNER_EDGE | 3.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1953 | constant | EARTH_VAN_ALLEN_OUTER_BELT_OUTER_EDGE | 7.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 2052 | constant | SUN_ROTATION_RATE_DEG_PER_DAY | 14.1844 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 2112 | constant | EARTH_IGRF13_G10_NT | -29404.8 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 2134 | constant | EARTH_IGRF13_G11_NT | -1450.9 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 2150 | constant | EARTH_IGRF13_H11_NT | 4652.5 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 2166 | constant | EARTH_IGRF13_G10_SV_NT_PER_YEAR | 5.7 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 2183 | constant | EARTH_IGRF13_G11_SV_NT_PER_YEAR | 7.4 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 2200 | constant | EARTH_IGRF13_H11_SV_NT_PER_YEAR | -25.9 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 2364 | constant | EARTH_MAGNETOPAUSE_SHUE_A3_PER_NT | 0.184 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 2381 | constant | EARTH_MAGNETOPAUSE_SHUE_A4_NT | 8.14 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 2398 | constant | EARTH_MAGNETOPAUSE_SHUE_A5 | 6.6 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 2420 | constant | EARTH_MAGNETOPAUSE_SHUE_A6 | 0.58 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 2440 | constant | EARTH_MAGNETOPAUSE_SHUE_A7_PER_NT | -0.007 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 2459 | constant | EARTH_MAGNETOPAUSE_SHUE_A8 | 0.024 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 2537 | constant | EARTH_BOW_SHOCK_JELINEK_EPS | 6.55 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 2552 | constant | EARTH_BOW_SHOCK_JELINEK_LAMBDA | 1.17 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 2994 | constant | EARTH_EXOSPHERE_H_FIT_COEFF_CM3 | 370520.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 3017 | constant | EARTH_EXOSPHERE_H_FIT_EXPONENT | 3.67 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 3026 | constant | EARTH_EXOSPHERE_H_OUTER_EXPONENT | 3.02 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 3169 | constant | PHOTOSPHERE_THICKNESS_KM | 100 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 3180 | constant | PHOTOSPHERE_TEMPERATURE_K | 5700 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 3248 | constant | CHROMOSPHERE_PHYSICAL_KM | 2000.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 3300 | constant | CORONA_BASE_HEIGHT_KM | 3000.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 3658 | constant | CORONA_MODEL_TEMPERATURE_K | 1180000.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 3686 | constant | CORONA_MODEL_MEAN_MOLECULAR_WEIGHT | 0.57 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 3698 | constant | CORONA_MODEL_ELECTRON_FLUX_PER_S | 9.127e+34 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 3708 | constant | CORONA_TEMPERATURE_MAX_K | 2000000.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 3719 | constant | ZODIACAL_DUST_DENSITY_EXPONENT | 1.34 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 3736 | constant | ZODIACAL_DUST_BETA | 4.14 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 3752 | constant | ZODIACAL_DUST_GAMMA | 0.942 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 3767 | constant | ZODIACAL_DUST_MU | 0.189 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 3782 | constant | ZODIACAL_DUST_TILT_DEG | 2.03 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 3798 | constant | ZODIACAL_DUST_NODE_DEG | 77.7 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 3858 | constant | ZODIACAL_DUST_JFC_LOW_PERCENT | 85 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 3872 | constant | ZODIACAL_DUST_JFC_HIGH_PERCENT | 95 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 3879 | constant | ZODIACAL_DUST_ASTEROID_MAX_PERCENT | 10 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 3891 | constant | TERMINATION_SHOCK_AU | 94.01 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 3920 | constant | VOYAGER2_TERMINATION_SHOCK_AU | 83.6 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 3944 | constant | TERMINATION_SHOCK_RANGE_LOW_AU | 80 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 3961 | constant | TERMINATION_SHOCK_RANGE_HIGH_AU | 100 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 3970 | constant | VOYAGER2_TS_UPSTREAM_SPEED_KM_S | 321.01 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 3986 | constant | VOYAGER2_TS_DOWNSTREAM_SPEED_KM_S | 184.67 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 3997 | constant | HELIOPAUSE_AU | 121 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 4042 | constant | OORT_CLOUD_INNER_EDGE_LOW_AU | 2000 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 4059 | constant | OORT_CLOUD_INNER_EDGE_HIGH_AU | 5000 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 4083 | constant | INNER_OORT_CLOUD_AU | 20000 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 4109 | constant | OORT_CLOUD_OUTER_EDGE_LOW_AU | 10000 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 4121 | constant | OORT_CLOUD_OUTER_EDGE_HIGH_AU | 100000 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 4154 | constant | INNER_OORT_DISK_OUTER_AU | 10000 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 4177 | constant | HILLS_CLOUD_TILT_DEG | 30 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 4197 | constant | ECLIPTIC_NODE_GALACTIC_LON_DEG | 186 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 4217 | constant | HILLS_CLOUD_PERI_ARG_BAND1_LOW_DEG | 70 | 3 | 5 | **15** | Cited, not cross-checked; date-sensitive | MEASURED -- independently catalogued fact (name) |
| 4235 | constant | HILLS_CLOUD_PERI_ARG_BAND1_HIGH_DEG | 180 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 4243 | constant | HILLS_CLOUD_PERI_ARG_BAND2_LOW_DEG | 250 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 4251 | constant | HILLS_CLOUD_PERI_ARG_BAND2_HIGH_DEG | 360 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 4259 | constant | HILLS_CLOUD_NODE_LOW_DEG | 120 | 3 | 5 | **15** | Cited, not cross-checked; date-sensitive | MEASURED -- independently catalogued fact (name) |
| 4278 | constant | HILLS_CLOUD_NODE_HIGH_DEG | 180 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 4286 | constant | HILLS_CLOUD_INCL_GAL_LOW_DEG | 75 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 4294 | constant | HILLS_CLOUD_INCL_GAL_HIGH_DEG | 90 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 4574 | constant | GRAVITATIONAL_INFLUENCE_PC | 0.65 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 4612 | constant | PARKER_CLOSEST_ALTITUDE_KM | 6160000.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 4684 | constant | MERCURY_RADIUS_KM | 2439.7 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 4687 | constant | VENUS_RADIUS_KM | 6051.8 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 4702 | constant | PHOBOS_RADIUS_KM | 11.1 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 4720 | constant | PLUTO_RADIUS_KM | 1188.3 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 4723 | constant | BENNU_RADIUS_KM | 0.24503 | 3 | 5 | **15** | Cited; cross-check incomplete (1/2 models) | MEASURED -- independently catalogued fact (name) |
| 4741 | constant | ERIS_RADIUS_KM | 1163 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 4767 | constant | MAKEMAKE_RADIUS_KM | 715 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 4811 | dict | KNOWN_ORBITAL_PERIODS[...] | (133 entries) | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 5406 | constant | VOYAGER_1_POINTING_RA_2030_ARCSEC | 1.701 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 5420 | constant | VOYAGER_1_POINTING_DEC_2030_ARCSEC | 1.535 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 5431 | constant | VOYAGER_2_POINTING_RA_2030_ARCSEC | 4.718 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 5445 | constant | VOYAGER_2_POINTING_DEC_2030_ARCSEC | 3.715 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 5472 | constant | COMET_HALLEY_NUCLEUS_RADIUS_KM | 5.5 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 5488 | constant | COMET_HALE_BOPP_NUCLEUS_RADIUS_KM | 37 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 5506 | constant | COMET_IKEYA_SEKI_NUCLEUS_RADIUS_KM | 4.3 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 5522 | constant | COMET_HYAKUTAKE_NUCLEUS_RADIUS_KM | 2.4 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 5540 | constant | COMET_3I_ATLAS_NUCLEUS_RADIUS_KM | 1.3 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 5557 | constant | COMET_MAPS_NUCLEUS_DIAMETER_KM | 0.4 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 5575 | constant | COMET_SCHAUMASSE_NUCLEUS_DIAMETER_KM | 2.6 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 5588 | constant | COMET_HOWELL_NUCLEUS_DIAMETER_KM | 4.4 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 5602 | constant | COMET_TEMPEL_2_NUCLEUS_RADIUS_KM | 5.98 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 5672 | constant | BOLTZMANN_CONSTANT_J_PER_K | 1.380649e-23 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 5684 | constant | PROTON_MASS_KG | 1.67262192595e-27 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 5762 | constant | SGR_A_MASS_SOLAR | 4297000.0 | 3 | 5 | **15** | Cited; cross-check incomplete (1/2 models) | MEASURED -- independently catalogued fact (name) |
| 5790 | constant | SGR_A_DISTANCE_PC | 8277.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1 | string | display string @ line 1 | (12 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1601 | constant | EARTH_MAGNETOPAUSE_STORM_2005_RADII | 3.0 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 1746 | constant | EARTH_VAN_ALLEN_INNER_RADII | 1.5 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 2320 | constant | EARTH_MAGNETOPAUSE_SHUE_A1_RADII | 10.22 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 2347 | constant | EARTH_MAGNETOPAUSE_SHUE_A2_RADII | 1.29 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 2510 | constant | EARTH_BOW_SHOCK_JELINEK_R0_RADII | 15.02 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 2606 | constant | EARTH_MAGNETOPAUSE_SHUE_SCATTER_RADII | 1.23 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 2686 | constant | EARTH_BOW_SHOCK_JELINEK_SCATTER_RADII | 0.69 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 2755 | constant | EARTH_MAGNETOTAIL_OBSERVED_RADII | 220.0 | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | RELATIONAL -- defined against a tracked base (name) |
| 2814 | constant | EARTH_MAGNETOTAIL_FLARE_END_RADII | 120.0 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 2854 | constant | EARTH_MAGNETOTAIL_DIAMETER_RADII | 60.0 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 2928 | constant | EARTH_GEOCORONA_RADII | 100.0 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 2957 | constant | EARTH_EXOSPHERE_H_FIT_INNER_RADII | 3.0 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 2983 | constant | EARTH_EXOSPHERE_H_FIT_OUTER_RADII | 15.0 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 3008 | constant | EARTH_EXOSPHERE_H_FIT_OFFSET_RADII | 2.47 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 3047 | constant | EARTH_EXOSPHERE_H_AT_10_RADII_CM3 | 35.0 | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | RELATIONAL -- defined against a tracked base (name) |
| 3062 | constant | EARTH_EXOSPHERE_H_AT_RADII | 10.0 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 3136 | constant | CORE_RADII | 0.25 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 3194 | constant | RADIATIVE_ZONE_RADII | 0.713 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 3387 | constant | HELMET_CUSP_LOW_RADII | 2 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 3411 | constant | HELMET_CUSP_HIGH_RADII | 4 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 3535 | constant | ALFVEN_SURFACE_RADII | 19.7 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 3600 | constant | ALFVEN_SURFACE_RANGE_LOW_RADII | 10 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 3621 | constant | ALFVEN_SURFACE_RANGE_HIGH_RADII | 20 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 3631 | constant | ALFVEN_SURFACE_STREAMER_FLOOR_RADII | 15 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 3831 | constant | DUST_DEPLETION_OUTER_RADII | 19 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 3845 | constant | DUST_FREE_ZONE_RADII | 5 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 248 | constant | KM_PER_AU | 149597870.7 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 269 | constant | PARSEC_TO_AU | 206264.806247096 | 2 | 5 | **10** | Cross-checked by 3 models (Claude, GPT, Gemini) | MEASURED -- independently catalogued fact (name) |
| 313 | constant | SUN_RADIUS_KM | 695700.0 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 335 | constant | EARTH_EQUATORIAL_RADIUS_KM | 6378.1366 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 358 | constant | EARTH_POLAR_RADIUS_KM | 6356.752 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 3074 | constant | JUPITER_EQUATORIAL_RADIUS_KM | 71492.0 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 3080 | constant | JUPITER_POLAR_RADIUS_KM | 66854.0 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 3086 | constant | SPEED_OF_LIGHT_KM_S | 299792.458 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED (inferred from role 'data') |
| 4690 | constant | MOON_RADIUS_KM | 1737.4 | 2 | 5 | **10** | Cross-checked by 3 models (Claude, GPT, Gemini) | MEASURED -- independently catalogued fact (name) |
| 4697 | constant | MARS_RADIUS_KM | 3396.2 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 4705 | constant | SATURN_RADIUS_KM | 60268 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 4710 | constant | URANUS_RADIUS_KM | 25559 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 4715 | constant | NEPTUNE_RADIUS_KM | 24764 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 4744 | constant | HAUMEA_RADIUS_KM | 798 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 4770 | constant | ARROKOTH_RADIUS_KM | 9.1 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 5634 | constant | GRAVITATIONAL_CONSTANT_SI | 6.6743e-11 | 2 | 5 | **10** | Cross-checked by 3 models (Claude, GPT, Gemini) | MEASURED (inferred from role 'data') |
| 5656 | constant | GM_SUN_SI | 1.3271244e+20 | 2 | 5 | **10** | Cross-checked by 3 models (Claude, GPT, Gemini) | MEASURED (inferred from role 'data') |

### coordinate_system_guide.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 252 | string | display string @ line 252 | (10 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 541 | string | display string @ line 541 | (10 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### earth_exosphere_sampler.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### earth_pole_live_check.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 69 | constant | ALLOWANCE_ARCSEC | 1.0 | 3 | 5 | **15** | Cited, not independently cross-checked | UNDETERMINED -- could not be classified |

### earth_pole_of_date.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 107 | dict | POLE_QUERY[...] | (3 entries) | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 108 | dict | ORBIT_QUERY[...] | (3 entries) | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 114 | constant | TILT_FIGURES | 7 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 116 | dict | _scene[...] | (1 entry) | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 1 | string | display string @ line 1 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### earth_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 334 | string | display string @ line 334 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 411 | string | display string @ line 411 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 485 | string | display string @ line 485 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 560 | string | display string @ line 560 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 631 | string | display string @ line 631 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 653 | string | display string @ line 653 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 791 | string | display string @ line 791 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 814 | string | display string @ line 814 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 876 | string | display string @ line 876 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 942 | string | display string @ line 942 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1011 | string | display string @ line 1011 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1066 | string | display string @ line 1066 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1537 | string | display string @ line 1537 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1559 | string | display string @ line 1559 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1674 | string | display string @ line 1674 | (6 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1688 | string | display string @ line 1688 | (7 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1750 | string | display string @ line 1750 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1787 | string | display string @ line 1787 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### energy_imbalance.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 900 | string | display string @ line 900 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### eris_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 61 | string | display string @ line 61 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 234 | string | display string @ line 234 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 397 | string | display string @ line 397 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 495 | string | display string @ line 495 | (7 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### fetch_climate_data.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 237 | string | display string @ line 237 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 238 | string | display string @ line 238 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 612 | string | display string @ line 612 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 613 | string | display string @ line 613 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 615 | string | display string @ line 615 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### food_insecurity_generator.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 130 | string | display string @ line 130 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 157 | string | display string @ line 157 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### hills_cloud_sampler.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### idealized_orbits.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1599 | string | display string @ line 1599 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1712 | string | display string @ line 1712 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1855 | string | display string @ line 1855 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1922 | string | display string @ line 1922 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2632 | string | display string @ line 2632 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2772 | string | display string @ line 2772 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2796 | string | display string @ line 2796 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2863 | string | display string @ line 2863 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2929 | string | display string @ line 2929 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 3130 | string | display string @ line 3130 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 3763 | string | display string @ line 3763 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 4477 | string | display string @ line 4477 | (12 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### info_dictionary.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 274 | dict | INFO[...] | (183 entries) | 3 | 5 | **15** | Cited, not cross-checked; date-sensitive | MEASURED (inferred from role 'data') |
| 1 | string | display string @ line 1 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 50 | string | display string @ line 50 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 183 | string | display string @ line 183 | (1 claim) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 298 | string | display string @ line 298 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 305 | string | display string @ line 305 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 312 | string | display string @ line 312 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 317 | string | display string @ line 317 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 355 | string | display string @ line 355 | (12 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 375 | string | display string @ line 375 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 395 | string | display string @ line 395 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 433 | string | display string @ line 433 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 452 | string | display string @ line 452 | (10 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 481 | string | display string @ line 481 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 504 | string | display string @ line 504 | (6 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 514 | string | display string @ line 514 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 530 | string | display string @ line 530 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 539 | string | display string @ line 539 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 547 | string | display string @ line 547 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 561 | string | display string @ line 561 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 572 | string | display string @ line 572 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 606 | string | display string @ line 606 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 620 | string | display string @ line 620 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 634 | string | display string @ line 634 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 642 | string | display string @ line 642 | (12 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 672 | string | display string @ line 672 | (9 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 695 | string | display string @ line 695 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 724 | string | display string @ line 724 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 737 | string | display string @ line 737 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 757 | string | display string @ line 757 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 760 | string | display string @ line 760 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 764 | string | display string @ line 764 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 766 | string | display string @ line 766 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 777 | string | display string @ line 777 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 781 | string | display string @ line 781 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 785 | string | display string @ line 785 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 790 | string | display string @ line 790 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 807 | string | display string @ line 807 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 847 | string | display string @ line 847 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 868 | string | display string @ line 868 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 881 | string | display string @ line 881 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 884 | string | display string @ line 884 | (12 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 913 | string | display string @ line 913 | (5 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 917 | string | display string @ line 917 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 920 | string | display string @ line 920 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 923 | string | display string @ line 923 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 926 | string | display string @ line 926 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 930 | string | display string @ line 930 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 935 | string | display string @ line 935 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 938 | string | display string @ line 938 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 942 | string | display string @ line 942 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 947 | string | display string @ line 947 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 951 | string | display string @ line 951 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 961 | string | display string @ line 961 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 965 | string | display string @ line 965 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 973 | string | display string @ line 973 | (6 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 981 | string | display string @ line 981 | (10 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1013 | string | display string @ line 1013 | (6 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1028 | string | display string @ line 1028 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1036 | string | display string @ line 1036 | (4 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1049 | string | display string @ line 1049 | (10 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1072 | string | display string @ line 1072 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1091 | string | display string @ line 1091 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1108 | string | display string @ line 1108 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1118 | string | display string @ line 1118 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1121 | string | display string @ line 1121 | (7 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1128 | string | display string @ line 1128 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1136 | string | display string @ line 1136 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1154 | string | display string @ line 1154 | (4 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1171 | string | display string @ line 1171 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1174 | string | display string @ line 1174 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1191 | string | display string @ line 1191 | (5 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1211 | string | display string @ line 1211 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1263 | string | display string @ line 1263 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1267 | string | display string @ line 1267 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1328 | string | display string @ line 1328 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1338 | string | display string @ line 1338 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1342 | string | display string @ line 1342 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1372 | string | display string @ line 1372 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1385 | string | display string @ line 1385 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1402 | string | display string @ line 1402 | (4 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1440 | string | display string @ line 1440 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1480 | string | display string @ line 1480 | (12 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1499 | string | display string @ line 1499 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1530 | string | display string @ line 1530 | (9 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1579 | string | display string @ line 1579 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1583 | string | display string @ line 1583 | (4 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1610 | string | display string @ line 1610 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1614 | string | display string @ line 1614 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1654 | string | display string @ line 1654 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1712 | string | display string @ line 1712 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1716 | string | display string @ line 1716 | (19 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1788 | string | display string @ line 1788 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1829 | string | display string @ line 1829 | (14 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1881 | string | display string @ line 1881 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1885 | string | display string @ line 1885 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1894 | string | display string @ line 1894 | (4 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1921 | string | display string @ line 1921 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1930 | string | display string @ line 1930 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1940 | string | display string @ line 1940 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1951 | string | display string @ line 1951 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1962 | string | display string @ line 1962 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1971 | string | display string @ line 1971 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2011 | string | display string @ line 2011 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2041 | string | display string @ line 2041 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2060 | string | display string @ line 2060 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2075 | string | display string @ line 2075 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2094 | string | display string @ line 2094 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2106 | string | display string @ line 2106 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2127 | string | display string @ line 2127 | (21 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2151 | string | display string @ line 2151 | (4 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2199 | string | display string @ line 2199 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2200 | string | display string @ line 2200 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2201 | string | display string @ line 2201 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2202 | string | display string @ line 2202 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2203 | string | display string @ line 2203 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2204 | string | display string @ line 2204 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2205 | string | display string @ line 2205 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2206 | string | display string @ line 2206 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2210 | string | display string @ line 2210 | (8 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2237 | string | display string @ line 2237 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2247 | string | display string @ line 2247 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2257 | string | display string @ line 2257 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2258 | string | display string @ line 2258 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2259 | string | display string @ line 2259 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### jupiter_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 77 | string | display string @ line 77 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 93 | string | display string @ line 93 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 148 | string | display string @ line 148 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 163 | string | display string @ line 163 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 218 | string | display string @ line 218 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 234 | string | display string @ line 234 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 290 | string | display string @ line 290 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 308 | string | display string @ line 308 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 447 | string | display string @ line 447 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 465 | string | display string @ line 465 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 573 | string | display string @ line 573 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 702 | string | display string @ line 702 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 792 | string | display string @ line 792 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 806 | string | display string @ line 806 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 916 | string | display string @ line 916 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 932 | string | display string @ line 932 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 948 | string | display string @ line 948 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 963 | string | display string @ line 963 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1031 | string | display string @ line 1031 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### mars_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 612 | string | display string @ line 612 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 724 | string | display string @ line 724 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 946 | string | display string @ line 946 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### mercury_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 39 | string | display string @ line 39 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 59 | string | display string @ line 59 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 126 | string | display string @ line 126 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 310 | string | display string @ line 310 | (8 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 383 | string | display string @ line 383 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |

### moon_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 118 | string | display string @ line 118 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 249 | string | display string @ line 249 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 586 | string | display string @ line 586 | (3 claims) | 3 | 4 | **12** | Cited; cross-check incomplete (1/2 models) | Public-facing display string (hover/INFO) |
| 613 | string | display string @ line 613 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### neptune_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 40 | string | display string @ line 40 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 57 | string | display string @ line 57 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 113 | string | display string @ line 113 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 132 | string | display string @ line 132 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 197 | string | display string @ line 197 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 221 | string | display string @ line 221 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 462 | string | display string @ line 462 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 597 | string | display string @ line 597 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 631 | string | display string @ line 631 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 686 | string | display string @ line 686 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 864 | string | display string @ line 864 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 886 | string | display string @ line 886 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 911 | string | display string @ line 911 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1197 | string | display string @ line 1197 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1230 | string | display string @ line 1230 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1260 | string | display string @ line 1260 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1290 | string | display string @ line 1290 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1320 | string | display string @ line 1320 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1350 | string | display string @ line 1350 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1383 | string | display string @ line 1383 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1415 | string | display string @ line 1415 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1447 | string | display string @ line 1447 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1479 | string | display string @ line 1479 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1511 | string | display string @ line 1511 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1541 | string | display string @ line 1541 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1683 | string | display string @ line 1683 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1703 | string | display string @ line 1703 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### orbital_period.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 105 | constant | OPEN_ORBIT_PLACEHOLDER_FLOOR | 1e+90 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'computation') |
| 120 | dict | VIEW_TO_OSCULATING_CENTRE[...] | (7 entries) | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'computation') |
| 142 | dict | PERIOD_TARGETS[...] | (1 entry) | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |

### orrery_rendering.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 108 | string | display string @ line 108 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### paleoclimate_dual_scale.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 262 | string | display string @ line 262 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### paleoclimate_human_origins_full.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 603 | string | display string @ line 603 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 605 | string | display string @ line 605 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 620 | string | display string @ line 620 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 622 | string | display string @ line 622 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 637 | string | display string @ line 637 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 639 | string | display string @ line 639 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### paleoclimate_visualization_full.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 429 | string | display string @ line 429 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 431 | string | display string @ line 431 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 446 | string | display string @ line 446 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 448 | string | display string @ line 448 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 463 | string | display string @ line 463 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 465 | string | display string @ line 465 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### paleoclimate_wet_bulb_full.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 135 | constant | BASELINE_ABSOLUTE_TEMP | 14.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 137 | constant | TW_SURVIVABILITY_BIOLOGICAL | 31.0 | 3 | 5 | **15** | Cited, not independently cross-checked | UNDETERMINED -- could not be classified |
| 138 | constant | TW_SURVIVABILITY_THEORETICAL | 35.0 | 3 | 5 | **15** | Cited, not independently cross-checked | UNDETERMINED -- could not be classified |
| 130 | string | display string @ line 130 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 146 | string | display string @ line 146 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 152 | string | display string @ line 152 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 158 | string | display string @ line 158 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 164 | string | display string @ line 164 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 178 | string | display string @ line 178 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 184 | string | display string @ line 184 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 789 | string | display string @ line 789 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 791 | string | display string @ line 791 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 806 | string | display string @ line 806 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 808 | string | display string @ line 808 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 823 | string | display string @ line 823 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 825 | string | display string @ line 825 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1205 | string | display string @ line 1205 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1218 | string | display string @ line 1218 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2245 | string | display string @ line 2245 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2303 | string | display string @ line 2303 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2341 | string | display string @ line 2341 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2416 | string | display string @ line 2416 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### planet9_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 38 | string | display string @ line 38 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 58 | string | display string @ line 58 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 215 | string | display string @ line 215 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 235 | string | display string @ line 235 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### planet_visualization_utilities.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 548 | string | display string @ line 548 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 552 | string | display string @ line 552 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 556 | string | display string @ line 556 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 571 | string | display string @ line 571 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 575 | string | display string @ line 575 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 579 | string | display string @ line 579 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 583 | string | display string @ line 583 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 587 | string | display string @ line 587 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 591 | string | display string @ line 591 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 595 | string | display string @ line 595 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 833 | string | display string @ line 833 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 841 | string | display string @ line 841 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### position_accuracy.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 133 | constant | SHEET_FIGURES | 4 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'computation') |
| 138 | constant | HALF_UNIT | 0.5 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'computation') |
| 144 | constant | SIGMA_MULTIPLE | 3 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'computation') |
| 151 | constant | DISTANCE_FLOOR_EXPONENT_KM | 0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 158 | constant | SPEED_FLOOR_EXPONENT_KM_S | -3 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'computation') |

### saturn_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 56 | string | display string @ line 56 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 142 | string | display string @ line 142 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 278 | string | display string @ line 278 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 299 | string | display string @ line 299 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 503 | string | display string @ line 503 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 770 | string | display string @ line 770 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 932 | string | display string @ line 932 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 952 | string | display string @ line 952 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1231 | string | display string @ line 1231 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### scenarios_coral_bleaching.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 168 | dict | CORAL_THRESHOLDS[...] | (16 entries) | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 101 | string | display string @ line 101 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### scenarios_heatwaves.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 206 | string | display string @ line 206 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 259 | string | display string @ line 259 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 276 | string | display string @ line 276 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 315 | string | display string @ line 315 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 362 | string | display string @ line 362 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 380 | string | display string @ line 380 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 431 | string | display string @ line 431 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 503 | string | display string @ line 503 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 523 | string | display string @ line 523 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### scenarios_western_heatwave_march_2026.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 708 | string | display string @ line 708 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### sgr_a_star_data.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 278 | string | display string @ line 278 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 491 | string | display string @ line 491 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 512 | string | display string @ line 512 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### sgr_a_visualization_core.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 156 | string | display string @ line 156 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 264 | string | display string @ line 264 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### shell_configs.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 209 | string | display string @ line 209 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 214 | string | display string @ line 214 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 229 | string | display string @ line 229 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 233 | string | display string @ line 233 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 247 | string | display string @ line 247 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 251 | string | display string @ line 251 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 269 | string | display string @ line 269 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 274 | string | display string @ line 274 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 287 | string | display string @ line 287 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 331 | string | display string @ line 331 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 364 | string | display string @ line 364 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 370 | string | display string @ line 370 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 384 | string | display string @ line 384 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 394 | string | display string @ line 394 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 412 | string | display string @ line 412 | (9 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 433 | string | display string @ line 433 | (1 claim) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 451 | string | display string @ line 451 | (4 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 471 | string | display string @ line 471 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 486 | string | display string @ line 486 | (1 claim) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 518 | string | display string @ line 518 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 524 | string | display string @ line 524 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 553 | string | display string @ line 553 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 579 | string | display string @ line 579 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 596 | string | display string @ line 596 | (9 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 615 | string | display string @ line 615 | (3 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1362 | string | display string @ line 1362 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1383 | string | display string @ line 1383 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1406 | string | display string @ line 1406 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1491 | string | display string @ line 1491 | (6 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1506 | string | display string @ line 1506 | (6 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1529 | string | display string @ line 1529 | (11 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1537 | string | display string @ line 1537 | (11 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1573 | string | display string @ line 1573 | (1 claim) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1583 | string | display string @ line 1583 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1607 | string | display string @ line 1607 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1613 | string | display string @ line 1613 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1629 | string | display string @ line 1629 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1635 | string | display string @ line 1635 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1650 | string | display string @ line 1650 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1657 | string | display string @ line 1657 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1673 | string | display string @ line 1673 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1682 | string | display string @ line 1682 | (3 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1700 | string | display string @ line 1700 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1707 | string | display string @ line 1707 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1724 | string | display string @ line 1724 | (4 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1734 | string | display string @ line 1734 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2004 | string | display string @ line 2004 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2155 | string | display string @ line 2155 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2185 | string | display string @ line 2185 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2218 | string | display string @ line 2218 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2255 | string | display string @ line 2255 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2293 | string | display string @ line 2293 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2309 | string | display string @ line 2309 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2345 | string | display string @ line 2345 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2347 | string | display string @ line 2347 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2387 | string | display string @ line 2387 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2403 | string | display string @ line 2403 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2418 | string | display string @ line 2418 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2431 | string | display string @ line 2431 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 2447 | string | display string @ line 2447 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2488 | string | display string @ line 2488 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2504 | string | display string @ line 2504 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2522 | string | display string @ line 2522 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2536 | string | display string @ line 2536 | (1 claim) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 2553 | string | display string @ line 2553 | (10 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2604 | string | display string @ line 2604 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2620 | string | display string @ line 2620 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2651 | string | display string @ line 2651 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2694 | string | display string @ line 2694 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2710 | string | display string @ line 2710 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2744 | string | display string @ line 2744 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### solar_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 386 | string | display string @ line 386 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 462 | string | display string @ line 462 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 500 | string | display string @ line 500 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 523 | string | display string @ line 523 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 533 | string | display string @ line 533 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 595 | string | display string @ line 595 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 644 | string | display string @ line 644 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 652 | string | display string @ line 652 | (9 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 668 | string | display string @ line 668 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 696 | string | display string @ line 696 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 760 | string | display string @ line 760 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 766 | string | display string @ line 766 | (5 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 771 | string | display string @ line 771 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 794 | string | display string @ line 794 | (5 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |

### spacecraft_encounters.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 116 | string | display string @ line 116 | (5 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 145 | string | display string @ line 145 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 171 | string | display string @ line 171 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 215 | string | display string @ line 215 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1492 | string | display string @ line 1492 | (7 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1511 | string | display string @ line 1511 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### star_notes.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 65 | string | display string @ line 65 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 119 | string | display string @ line 119 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 163 | string | display string @ line 163 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 210 | string | display string @ line 210 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 228 | string | display string @ line 228 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 242 | string | display string @ line 242 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 281 | string | display string @ line 281 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 314 | string | display string @ line 314 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 341 | string | display string @ line 341 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 394 | string | display string @ line 394 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 421 | string | display string @ line 421 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 474 | string | display string @ line 474 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 494 | string | display string @ line 494 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 510 | string | display string @ line 510 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 522 | string | display string @ line 522 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 546 | string | display string @ line 546 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 563 | string | display string @ line 563 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 614 | string | display string @ line 614 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 638 | string | display string @ line 638 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 678 | string | display string @ line 678 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 731 | string | display string @ line 731 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 747 | string | display string @ line 747 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 761 | string | display string @ line 761 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 776 | string | display string @ line 776 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 791 | string | display string @ line 791 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 806 | string | display string @ line 806 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 833 | string | display string @ line 833 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 856 | string | display string @ line 856 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 897 | string | display string @ line 897 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 928 | string | display string @ line 928 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 976 | string | display string @ line 976 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1032 | string | display string @ line 1032 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1049 | string | display string @ line 1049 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1124 | string | display string @ line 1124 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1180 | string | display string @ line 1180 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1192 | string | display string @ line 1192 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1199 | string | display string @ line 1199 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### star_sphere_builder.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 109 | string | display string @ line 109 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### sun_corona_sampler.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### uranus_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 39 | string | display string @ line 39 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 54 | string | display string @ line 54 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 107 | string | display string @ line 107 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 124 | string | display string @ line 124 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 184 | string | display string @ line 184 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 203 | string | display string @ line 203 | (12 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 361 | string | display string @ line 361 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 380 | string | display string @ line 380 | (16 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 449 | string | display string @ line 449 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 535 | string | display string @ line 535 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 628 | string | display string @ line 628 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 804 | string | display string @ line 804 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 848 | string | display string @ line 848 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 864 | string | display string @ line 864 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 882 | string | display string @ line 882 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 899 | string | display string @ line 899 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 917 | string | display string @ line 917 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 954 | string | display string @ line 954 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 974 | string | display string @ line 974 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 993 | string | display string @ line 993 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1013 | string | display string @ line 1013 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1146 | string | display string @ line 1146 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1165 | string | display string @ line 1165 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### venus_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 415 | string | display string @ line 415 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 704 | string | display string @ line 704 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 780 | string | display string @ line 780 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### visualization_3d.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 725 | string | display string @ line 725 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 748 | string | display string @ line 748 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 785 | string | display string @ line 785 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### zodiacal_dust_sampler.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

---

## Tier 3: LOW PRIORITY (Score 5-9)

### add_docstrings.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 118 | dict | DOCSTRINGS[...] | (42 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### close_approach_data.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 64 | dict | CAD_BODY_NAMES[...] | (11 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal use (name vocabulary) |

### constants_new.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 3480 | constant | ROCHE_LIMIT_RADII | 3.45 | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | RELATIONAL -- defined against a tracked base (name) |
| 1682 | constant | SATELLITES_FUNCTIONING_COUNT | 15900.0 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal use (name vocabulary) |
| 1697 | constant | LEO_OBJECTS_TRACKED_COUNT | 28015.0 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal use (name vocabulary) |
| 1732 | constant | STARLINK_WORKING_COUNT | 11140.0 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal use (name vocabulary) |

### data_inventory.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 32 | constant | PAGES_CEILING_MB | 1024 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### dep_trace.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 40 | constant | HUB_THRESHOLD | 8 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 52 | dict | _ROLE_TO_VISUAL[...] | (12 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 67 | dict | CATEGORY_COLORS[...] | (10 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### doc_index.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 92 | dict | KIND_LABEL[...] | (3 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 98 | dict | KIND_ORDER[...] | (4 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 109 | constant | TAG_SCAN_LINES | 40 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### eris_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 218 | string | display string @ line 218 | (2 claims) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 478 | string | display string @ line 478 | (7 claims) | 2 | 4 | **8** | Cross-checked by 2 models (GPT, Gemini) | Public-facing display string (hover/INFO) |

### exoplanet_systems.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 41 | dict | TRAPPIST1_SYSTEM[...] | (6 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal use (key vocabulary) |
| 327 | dict | TOI1338_SYSTEM[...] | (6 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal use (key vocabulary) |
| 486 | dict | PROXIMA_SYSTEM[...] | (6 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal use (key vocabulary) |

### export_constants.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 204 | constant | SCHEMA | 7 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |

### export_drawings.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 118 | constant | SCHEMA | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### export_objects.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 262 | constant | SCHEMA | 3 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 263 | constant | CADENCE_DAYS | 30 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### export_orbit_cache.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 206 | dict | CENTER_SLUG_MAP[...] | (22 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |

### food_insecurity_generator.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 110 | constant | P5_DOT_MIN_SCALE | 0.5 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |
| 111 | constant | P5_DOT_MAX_SCALE | 1.8 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |

### horizons_check.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 178 | constant | PAUSE_SECONDS | 2.0 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |
| 179 | constant | TIMEOUT_SECONDS | 30 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |
| 182 | dict | INDEX_WORD[...] | (2 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |
| 184 | constant | OPEN_ORBIT_FLOOR | 1e+90 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |

### info_dictionary.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 119 | dict | object_type_mapping[...] | (79 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal use (name vocabulary) |
| 255 | dict | class_mapping[...] | (14 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal use (name vocabulary) |

### ledger_index.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 170 | dict | SECTION_ALIASES[...] | (1 entry) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 174 | dict | SECTION_TITLES[...] | (26 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 482 | dict | ISSUE_TAGS[...] | (4 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### mars_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 586 | string | display string @ line 586 | (1 claim) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 674 | string | display string @ line 674 | (3 claims) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 788 | string | display string @ line 788 | (2 claims) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 925 | string | display string @ line 925 | (3 claims) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |

### measure_perframe_elements.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 45 | constant | KB | 1000.0 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 46 | constant | FRAMES_29 | 29 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 47 | constant | FRAMES_60 | 60 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### mercury_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 49 | string | display string @ line 49 | (1 claim) | 2 | 4 | **8** | Cross-checked by 2 models (GPT, Gemini) | Public-facing display string (hover/INFO) |
| 71 | string | display string @ line 71 | (1 claim) | 2 | 4 | **8** | Cross-checked by 2 models (Gemini, GPT) | Public-facing display string (hover/INFO) |
| 97 | string | display string @ line 97 | (4 claims) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 254 | string | display string @ line 254 | (1 claim) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 424 | string | display string @ line 424 | (1 claim) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |

### module_atlas.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 106 | dict | ROLE_MAP[...] | (161 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 408 | dict | ROLE_DESCRIPTIONS[...] | (13 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 431 | dict | ROLE_SECTION_TITLES[...] | (13 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### moon_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 47 | string | display string @ line 47 | (1 claim) | 2 | 4 | **8** | Cross-checked by 2 models (GPT, Gemini) | Public-facing display string (hover/INFO) |
| 65 | string | display string @ line 65 | (1 claim) | 2 | 4 | **8** | Cross-checked by 2 models (GPT, Gemini) | Public-facing display string (hover/INFO) |
| 138 | string | display string @ line 138 | (1 claim) | 2 | 4 | **8** | Cross-checked by 2 models (GPT, Gemini) | Public-facing display string (hover/INFO) |
| 228 | string | display string @ line 228 | (1 claim) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |

### orbit_data_manager.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 44 | constant | DEFAULT_DAYS_AHEAD | 730 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'cache') |
| 45 | constant | MAX_DATA_AGE_DAYS | 90 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'cache') |

### orrery_maintenance_run.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 498 | constant | TOOL_TIMEOUT_SECONDS | 900 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 561 | constant | HASH_LIMIT_BYTES | 2 * 1024 * 1024 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 680 | constant | NOTE_WIDTH | 44 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 681 | constant | NOTE_INDENT | 37 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### osculating_cache_manager.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 98 | dict | REFRESH_INTERVALS[...] | (14 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'cache') |

### palomas_orrery.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 2345 | constant | PERFRAME_INDICATOR_RADIUS_FACTOR | 100.0 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |
| 2378 | constant | PERFRAME_COORD_DECIMALS | 7 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |
| 4010 | constant | BUTTON_WIDTH | 14 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |

### palomas_orrery_dashboard.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 360 | constant | WINDOW_WIDTH | 960 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |
| 361 | constant | WINDOW_HEIGHT | 720 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |
| 2459 | constant | TOOLTIP_DELAY_MS | 400 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |
| 2590 | dict | SECTION_SYMBOLS[...] | (8 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'gui') |

### path_plan.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 225 | constant | SCHEMA | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 229 | constant | RULE | 2 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 231 | dict | WORD[...] | (4 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 233 | constant | CADENCE_DAYS | 30 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 234 | constant | KEEP_PAST_DAYS | 30 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 235 | constant | OVERLAP_DAYS | 3 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 236 | constant | PAUSE_SECONDS | 1.0 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 239 | constant | TIME_LIMIT_SECONDS | 600 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 244 | constant | BACKBONE_STEP_SECONDS | 7 * 86400.0 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 245 | constant | THIN_TOL_AU | 0.02 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 257 | constant | DAY_S | 86400.0 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 316 | dict | PRIMARY[...] | (1 entry) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 902 | constant | COMET_BEFORE_PERIHELION_DAYS | 365 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 903 | constant | COMET_AFTER_TODAY_DAYS | 365 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 906 | constant | COMET_TP_SLACK_DAYS | 3 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 908 | constant | COMET_RULE | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### planet_visualization_utilities.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1060 | dict | STREAMER_BAND_DEFAULTS[...] | (20 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (name vocabulary) |

### pluto_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 41 | string | display string @ line 41 | (2 claims) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 61 | string | display string @ line 61 | (5 claims) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 136 | string | display string @ line 136 | (1 claim) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 155 | string | display string @ line 155 | (2 claims) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 227 | string | display string @ line 227 | (1 claim) | 2 | 4 | **8** | Cross-checked by 2 models (GPT, Gemini) | Public-facing display string (hover/INFO) |
| 250 | string | display string @ line 250 | (1 claim) | 2 | 4 | **8** | Cross-checked by 2 models (GPT, Gemini) | Public-facing display string (hover/INFO) |
| 400 | string | display string @ line 400 | (1 claim) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 423 | string | display string @ line 423 | (4 claims) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 535 | string | display string @ line 535 | (10 claims) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 614 | string | display string @ line 614 | (3 claims) | 2 | 4 | **8** | Cross-checked by 2 models (GPT, Claude) | Public-facing display string (hover/INFO) |
| 638 | string | display string @ line 638 | (3 claims) | 2 | 4 | **8** | Cross-checked by 2 models (GPT, Claude) | Public-facing display string (hover/INFO) |

### position_accuracy.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 100 | dict | PUBLISHED_ROW_NAMES[...] | (9 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (name vocabulary) |

### provenance_history.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 63 | constant | SCHEMA_VERSION | 1 | 4 | 2 | **8** | No source citation; date-sensitive (recalled) | Internal (role 'devtool') |
| 68 | constant | MAX_RUNS | 6 | 4 | 2 | **8** | No source citation; date-sensitive (recalled) | Internal (role 'devtool') |
| 74 | constant | EXPECTED_CADENCE_DAYS | 1 | 4 | 2 | **8** | No source citation; date-sensitive (recalled) | Internal (role 'devtool') |
| 361 | dict | DOMAIN_SHORT_NAMES[...] | (7 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### provenance_scanner.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 389 | constant | V_FETCHED | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 390 | constant | V_CROSS_CHECKED | 2 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 399 | constant | V_SOURCED | 3 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 402 | constant | V_RECALLED | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 403 | constant | V_DECLARED | 0 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 416 | constant | C_COSMETIC | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 417 | constant | C_INTERNAL | 2 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 418 | constant | C_LOADBEARING | 3 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 419 | constant | C_PUBLIC | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 420 | constant | C_PROPAGATING | 5 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 425 | constant | C_RELATIONAL | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 426 | constant | C_MEASURED | 5 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 431 | constant | C_UNDETERMINED | 5 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 528 | dict | DOMAIN_LABELS[...] | (6 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 1139 | constant | CITATION_LOOKBACK_BLOCK | 15 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |
| 2156 | constant | SHADOW_DERIVED_MIN_MAGNITUDE | 100.0 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |

### sgr_a_grand_tour.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 46 | constant | ANIMATION_FRAMES | 140 | 4 | 2 | **8** | No source citation (recalled) | Internal use (name vocabulary) |
| 47 | constant | POINTS_PER_ORBIT | 80 | 4 | 2 | **8** | No source citation (recalled) | Internal use (name vocabulary) |
| 55 | dict | ROSETTE_ORBIT_COUNTS[...] | (4 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (name vocabulary) |

### sgr_a_visualization_animation.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 27 | dict | ANIMATION_CONFIG[...] | (5 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (name vocabulary) |

### skills_index.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 153 | constant | NAME_COL_WIDTH | 29 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |
| 154 | constant | VER_COL_WIDTH | 5 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |
| 156 | constant | WRAP_WIDTH | 79 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |
| 157 | constant | FALLBACK_TRUNC | 60 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |
| 168 | constant | NAME_MAX_CHARS | 64 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |
| 171 | constant | DESCRIPTION_MAX_CHARS | 1024 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |
| 173 | constant | BODY_GUIDELINE_LINES | 500 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |
| 185 | constant | READ_PART_MAX_CHARS | 16000 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |
| 186 | constant | READ_PART_MAX_LINES | 2000 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |

### star_sphere_builder.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 95 | constant | CIRCLE_POINTS | 120 | 4 | 2 | **8** | No source citation (recalled) | Internal use (name vocabulary) |
| 526 | dict | CONSTELLATION_NAMES[...] | (88 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (name vocabulary) |
| 54 | constant | VMAG_LIMIT | 3.5 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal use (name vocabulary) |

### test_dashboard_parity.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 106 | constant | MAX_WORDS | 12 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 128 | dict | WRAPPERS[...] | (2 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### test_dimensions.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 125 | constant | REL_TOL | 1e-09 | 4 | 2 | **8** | No source citation; date-sensitive (recalled) | Internal (role 'devtool') |

### test_domain_split.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 104 | dict | NOTES[...] | (4 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### test_objects_export.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 105 | dict | SELF_TEST_RECORD[...] | (8 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### test_orbit_markers.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 131 | dict | MERCURY[...] | (8 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 134 | dict | ENCKE[...] | (8 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 137 | dict | SEDNA[...] | (8 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 141 | dict | SEDNA_BARY[...] | (9 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 145 | dict | IO[...] | (9 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 149 | dict | EARTH[...] | (9 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 153 | dict | MOON[...] | (9 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 201 | constant | SEDNA_SIGMA_KM | 3 * 85939.995 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 206 | constant | FLOOR_KM | 0.5 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 212 | dict | APSIS_SIGMA_KM[...] | (2 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 310 | dict | FETCHED_DAYS[...] | (3 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 312 | dict | FETCHED_ERR[...] | (3 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### test_path_plan.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 113 | constant | DAY | 86400.0 | 4 | 2 | **8** | No source citation; date-sensitive (recalled) | Internal (role 'devtool') |
| 133 | dict | FLYBY_A[...] | (3 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 135 | dict | FLYBY_B[...] | (3 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 152 | dict | CIRCLES[...] | (11 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### test_period_fetch.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 503 | dict | L445_FIELDS[...] | (2 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### test_position_digits.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 265 | dict | SENTENCES[...] | (4 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 271 | dict | NONE_WORDS[...] | (2 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 275 | dict | SPEED_WORDS[...] | (4 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 96 | constant | FLOOR_KM | 0.5 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |
| 99 | constant | SPEED_FLOOR_KM_S | 0.0005 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |
| 512 | constant | RECORDED_R_S_AU | 2.25639403e-06 | 3 | 2 | **6** | Cited, not cross-checked; date-sensitive | Internal (role 'devtool') |

### test_reset_completeness.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 43 | dict | ENTRY_DEFAULTS[...] | (10 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### venus_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 74 | string | display string @ line 74 | (2 claims) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 100 | string | display string @ line 100 | (2 claims) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 391 | string | display string @ line 391 | (3 claims) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 503 | string | display string @ line 503 | (15 claims) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 594 | string | display string @ line 594 | (1 claim) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 747 | string | display string @ line 747 | (2 claims) | 2 | 4 | **8** | Cross-checked by 2 models (GPT, Claude) | Public-facing display string (hover/INFO) |

### worksheet_checker.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 428 | constant | HASH_CHARS | 8 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 660 | constant | MIN_PROSE_FRAGMENT | 24 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 851 | constant | QUOTE_LIMIT | 160 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 1013 | constant | INSTRUCTION_LOOKBACK | 30 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 1014 | constant | INSTRUCTION_LOOKAHEAD | 25 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### worksheet_key_aliases.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 68 | dict | ALIASES[...] | (1 entry) | 4 | 2 | **8** | No source citation (recalled) | Internal use (name vocabulary) |

### worksheet_keys.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 141 | constant | EXTRACTOR_VERSION | 2 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### worksheet_request_builder.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 124 | constant | CLAIM_EXCERPT | 90 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 321 | constant | HASH_CHARS | 8 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

---

## Tier 4: LOWEST PRIORITY (Score 1-4)

### constants_new.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 3122 | constant | DEFAULT_MARKER_SIZE | 7 | 4 | 1 | **4** | No source citation (recalled) | Cosmetic (name vocabulary) |
| 3124 | constant | CENTER_MARKER_SIZE | 10 | 4 | 1 | **4** | No source citation (recalled) | Cosmetic (name vocabulary) |

### orbital_period.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 147 | dict | CENTRE_LABELS[...] | (23 entries) | 4 | 1 | **4** | No source citation (recalled) | Cosmetic (name vocabulary) |

### star_sphere_builder.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 709 | constant | ECLIPTIC_INFO_MARKER_LON | 142.5 | 4 | 1 | **4** | No source citation (recalled) | Cosmetic (name vocabulary) |
| 710 | constant | EQUATOR_INFO_MARKER_RA | 52.5 | 4 | 1 | **4** | No source citation (recalled) | Cosmetic (name vocabulary) |
| 711 | constant | GALACTIC_INFO_MARKER_LON | 110.0 | 4 | 1 | **4** | No source citation (recalled) | Cosmetic (name vocabulary) |

---

## How to Use This Audit

1. Start with INCONSISTENCIES -- these are confirmed problems.
2. Work through Tier 1 (FIX NOW) findings.
3. For each finding:
   a. Locate the correct value from an authoritative source.
   b. Update constants_new.py (or info_dictionary.py).
   c. Add a `# Source:` comment above the declaration.
   d. Replace local copies with imports.
   e. Verify downstream plots unchanged.
4. Re-run this scanner to confirm fixes.

Companion tools:
- module_atlas.py              -- dependency graph
- test_constants_provenance.py -- pin constants_new.py values
- dep_trace.py                 -- per-module import tracing

---

*Generated by provenance_scanner.py -- Paloma's Orrery Developer Tools*
