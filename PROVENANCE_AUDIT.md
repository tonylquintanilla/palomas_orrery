# Paloma's Orrery -- Provenance Audit

Generated: July 29, 2026
Files scanned: 118
Total findings: 781
Constants: 90 | Dicts: 38 | Display strings: 653

Unit of provenance: the smallest thing with a coherent source citation. A dict with one block-level `# Source:` comment is ONE unit; all its entries inherit that citation. A hover string with co-referring numbers is ONE unit.

**Color values are excluded from this audit.** RGB/color fields are never scored as claims (see _make_dict_unit), and a dict's block `# Source:` citation should never be read as covering that dict's `color` field(s), even when it covers everything else in the same unit. This does not mean color choices have no basis at all -- some are loosely informed by real imagery or composition data -- but color selection across this codebase is inconsistent in method: sometimes evidence-informed, sometimes chosen purely for visual contrast or distinction, sometimes arbitrary. Treat every color value as a developer/AI judgment call, not a measured or verified quantity, regardless of what citation sits nearby. (Tony's call, July 16, 2026; a low-priority wishlist item for a real, systematic color-accuracy pass is tracked at LEDGER_CONSOLIDATED.md L-124.)

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
- 10-15: ALL ACCEPTED RESIDUALS -- see note below
- 5-9: ALREADY CITED OR LOW RISK
- 1-4: NO ACTION NEEDED

---

## Priority Summary

| Tier | Score | Action | Count |
|------|-------|--------|------:|
| 1 | 16-20 | FIX NOW | 156 |
| 2 | 10-15 | ALL ACCEPTED RESIDUALS -- see note below | 563 |
| 3 | 5-9 | ALREADY CITED OR LOW RISK -- no action required | 60 |
| 4 | 1-4 | NO ACTION NEEDED | 2 |

**Tier 2 note (April 2026 audit):** All Tier-2 findings are documented
accepted residuals -- cited constants, V_STALE staleness flags on verified
strings, or known scanner limitations. No action required unless a new
uncited entry appears. See Accepted Residuals block below for details.

---

## Findings by File

Quick-reference counts before the per-tier detail below. Same data, grouped the other way: every file that has at least one finding, with its count in each tier.

| File | Domain | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Total |
|------|--------|-------:|-------:|-------:|-------:|------:|
| `info_dictionary.py` | orrery | 0 | 121 | 3 | 0 | 124 |
| `shell_configs.py` | orrery | 41 | 49 | 0 | 0 | 90 |
| `celestial_objects.py` | orrery | 0 | 54 | 0 | 0 | 54 |
| `constants_new.py` | orrery | 0 | 37 | 0 | 2 | 39 |
| `idealized_orbits.py` | orrery | 24 | 14 | 0 | 0 | 38 |
| `star_notes.py` | stars | 0 | 32 | 0 | 0 | 32 |
| `earth_visualization_shells.py` | earth_science | 0 | 27 | 0 | 0 | 27 |
| `solar_visualization_shells.py` | orrery | 0 | 25 | 0 | 0 | 25 |
| `neptune_visualization_shells.py` | orrery | 0 | 24 | 0 | 0 | 24 |
| `uranus_visualization_shells.py` | orrery | 0 | 24 | 0 | 0 | 24 |
| `comet_visualization_shells.py` | orrery | 2 | 21 | 0 | 0 | 23 |
| `planet_visualization_utilities.py` | orrery | 8 | 11 | 0 | 0 | 19 |
| `jupiter_visualization_shells.py` | orrery | 1 | 17 | 0 | 0 | 18 |
| `paleoclimate_wet_bulb_full.py` | earth_science | 14 | 2 | 0 | 0 | 16 |
| `provenance_scanner.py` | dev_tools | 0 | 0 | 14 | 0 | 14 |
| `sgr_a_grand_tour.py` | orrery | 7 | 1 | 3 | 0 | 11 |
| `sgr_a_star_data.py` | orrery | 1 | 10 | 0 | 0 | 11 |
| `paleoclimate_human_origins_full.py` | earth_science | 9 | 2 | 0 | 0 | 11 |
| `pluto_visualization_shells.py` | orrery | 0 | 10 | 0 | 0 | 10 |
| `scenarios_western_heatwave_march_2026.py` | earth_science | 5 | 4 | 0 | 0 | 9 |
| `saturn_visualization_shells.py` | orrery | 0 | 9 | 0 | 0 | 9 |
| `scenarios_heatwaves.py` | earth_science | 1 | 7 | 0 | 0 | 8 |
| `spacecraft_encounters.py` | orrery | 0 | 8 | 0 | 0 | 8 |
| `paleoclimate_visualization_full.py` | earth_science | 7 | 0 | 0 | 0 | 7 |
| `asteroid_belt_visualization_shells.py` | orrery | 0 | 7 | 0 | 0 | 7 |
| `mercury_visualization_shells.py` | orrery | 0 | 7 | 0 | 0 | 7 |
| `celestial_coordinates.py` | orrery | 3 | 3 | 0 | 0 | 6 |
| `venus_visualization_shells.py` | orrery | 0 | 6 | 0 | 0 | 6 |
| `exoplanet_coordinates.py` | stars | 4 | 1 | 0 | 0 | 5 |
| `sgr_a_visualization_precession.py` | orrery | 3 | 1 | 1 | 0 | 5 |
| `star_sphere_builder.py` | stars | 0 | 2 | 3 | 0 | 5 |
| `planet9_visualization_shells.py` | orrery | 0 | 5 | 0 | 0 | 5 |
| `apsidal_markers.py` | orrery | 3 | 1 | 0 | 0 | 4 |
| `sgr_a_visualization_core.py` | orrery | 4 | 0 | 0 | 0 | 4 |
| `eris_visualization_shells.py` | orrery | 0 | 4 | 0 | 0 | 4 |
| `mars_visualization_shells.py` | orrery | 0 | 4 | 0 | 0 | 4 |
| `moon_visualization_shells.py` | orrery | 0 | 4 | 0 | 0 | 4 |
| `skills_index.py` | dev_tools | 0 | 0 | 4 | 0 | 4 |
| `coordinate_system_guide.py` | orrery | 2 | 1 | 0 | 0 | 3 |
| `paleoclimate_visualization.py` | earth_science | 3 | 0 | 0 | 0 | 3 |
| `scenarios_coral_bleaching.py` | earth_science | 1 | 2 | 0 | 0 | 3 |
| `food_insecurity_generator.py` | earth_science | 0 | 1 | 2 | 0 | 3 |
| `visualization_3d.py` | stars | 0 | 3 | 0 | 0 | 3 |
| `dep_trace.py` | dev_tools | 0 | 0 | 3 | 0 | 3 |
| `ledger_index.py` | dev_tools | 0 | 0 | 3 | 0 | 3 |
| `measure_perframe_elements.py` | dev_tools | 0 | 0 | 3 | 0 | 3 |
| `module_atlas.py` | dev_tools | 0 | 0 | 3 | 0 | 3 |
| `palomas_orrery.py` | orrery | 0 | 0 | 3 | 0 | 3 |
| `palomas_orrery_dashboard.py` | orrery | 0 | 0 | 3 | 0 | 3 |
| `exoplanet_systems.py` | stars | 0 | 0 | 3 | 0 | 3 |
| `object_type_analyzer.py` | orrery | 1 | 1 | 0 | 0 | 2 |
| `paleoclimate_dual_scale.py` | earth_science | 2 | 0 | 0 | 0 | 2 |
| `close_approach_data.py` | orrery | 0 | 1 | 1 | 0 | 2 |
| `orbit_data_manager.py` | orrery | 0 | 0 | 2 | 0 | 2 |
| `orbital_elements.py` | orrery | 1 | 0 | 0 | 0 | 1 |
| `data_acquisition.py` | orrery | 1 | 0 | 0 | 0 | 1 |
| `energy_imbalance.py` | earth_science | 1 | 0 | 0 | 0 | 1 |
| `exoplanet_orbits.py` | stars | 1 | 0 | 0 | 0 | 1 |
| `fetch_paleoclimate_data.py` | earth_science | 1 | 0 | 0 | 0 | 1 |
| `hr_diagram_distance.py` | stars | 1 | 0 | 0 | 0 | 1 |
| `orrery_rendering.py` | orrery | 1 | 0 | 0 | 0 | 1 |
| `planetarium_distance.py` | stars | 1 | 0 | 0 | 0 | 1 |
| `plot_data_report_widget.py` | utilities | 1 | 0 | 0 | 0 | 1 |
| `visualization_utils.py` | stars | 1 | 0 | 0 | 0 | 1 |
| `add_docstrings.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |
| `data_inventory.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |
| `osculating_cache_manager.py` | orrery | 0 | 0 | 1 | 0 | 1 |
| `sgr_a_visualization_animation.py` | orrery | 0 | 0 | 1 | 0 | 1 |
| `test_reset_completeness.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |
| `export_orbit_cache.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |

---

## Findings by File Type

Same data again, grouped by subject-matter domain rather than by individual file -- orrery, earth science, gallery, stars, utilities, dev tools. Domain is a report-only grouping (see MODULE_DOMAIN_MAP / classify_domain()); it does not affect which files get scanned or scored.

| Domain | Files | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Total |
|--------|------:|-------:|-------:|-------:|-------:|------:|
| Orrery (solar system + orbital mechanics) | 38 | 103 | 480 | 18 | 2 | 603 |
| Earth System | 12 | 44 | 45 | 2 | 0 | 91 |
| Stars (stellar neighborhood) | 9 | 8 | 38 | 6 | 0 | 52 |
| Dev Tools (audit, diagnostics, one-shot scripts) | 10 | 0 | 0 | 34 | 0 | 34 |
| Utilities (cross-domain shared helpers) | 1 | 1 | 0 | 0 | 0 | 1 |
| Gallery | 0 | 0 | 0 | 0 | 0 | 0 |

**Domain coverage gap:** the following files have findings but no entry in `MODULE_DOMAIN_MAP` -- defaulted to `orrery` rather than guessed into a more specific bucket. Add each to `MODULE_DOMAIN_MAP` in provenance_scanner.py with its real domain so this stops silently defaulting:

- `orrery_rendering.py`
- `shell_configs.py`

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
  Nucleus sizes and feature thresholds drive shell rendering geometry. Low user-visible impact if slightly off. Deferred until comet shell refactor.

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

### apsidal_markers.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1203 | string | display string @ line 1203 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1205 | string | display string @ line 1205 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1207 | string | display string @ line 1207 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### celestial_coordinates.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 441 | string | display string @ line 441 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 450 | string | display string @ line 450 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 452 | string | display string @ line 452 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### comet_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 45 | dict | COMET_NUCLEUS_SIZES[...] | (16 entries) | 4 | 5 | **20** | No source citation (recalled) | MEASURED -- independently catalogued fact (name) |
| 1598 | dict | COMET_FEATURE_THRESHOLDS[...] | (3 entries) | 4 | 5 | **20** | No source citation (recalled) | MEASURED -- independently catalogued fact (name) |

### coordinate_system_guide.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 119 | string | display string @ line 119 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 152 | string | display string @ line 152 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### data_acquisition.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 202 | string | display string @ line 202 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### energy_imbalance.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 535 | string | display string @ line 535 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### exoplanet_coordinates.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 89 | string | display string @ line 89 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 128 | string | display string @ line 128 | (5 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 302 | string | display string @ line 302 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 310 | string | display string @ line 310 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### exoplanet_orbits.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 291 | string | display string @ line 291 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### fetch_paleoclimate_data.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 152 | string | display string @ line 152 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### hr_diagram_distance.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 220 | string | display string @ line 220 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### idealized_orbits.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 124 | string | display string @ line 124 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 139 | string | display string @ line 139 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 167 | string | display string @ line 167 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 181 | string | display string @ line 181 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1406 | string | display string @ line 1406 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1465 | string | display string @ line 1465 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1476 | string | display string @ line 1476 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1589 | string | display string @ line 1589 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2385 | string | display string @ line 2385 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2431 | string | display string @ line 2431 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2453 | string | display string @ line 2453 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2479 | string | display string @ line 2479 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2512 | string | display string @ line 2512 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2686 | string | display string @ line 2686 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2810 | string | display string @ line 2810 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2932 | string | display string @ line 2932 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 3627 | string | display string @ line 3627 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 3830 | string | display string @ line 3830 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4299 | string | display string @ line 4299 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4566 | string | display string @ line 4566 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4588 | string | display string @ line 4588 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4652 | string | display string @ line 4652 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4686 | string | display string @ line 4686 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 5912 | string | display string @ line 5912 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### jupiter_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 959 | string | display string @ line 959 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### object_type_analyzer.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 655 | string | display string @ line 655 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### orbital_elements.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1433 | dict | planet_tilts[...] | (7 entries) | 4 | 5 | **20** | No source citation (recalled) | MEASURED -- independently catalogued fact (name) |

### orrery_rendering.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 237 | string | display string @ line 237 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### paleoclimate_dual_scale.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 905 | string | display string @ line 905 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1050 | string | display string @ line 1050 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### paleoclimate_human_origins_full.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 203 | string | display string @ line 203 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 223 | string | display string @ line 223 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 365 | string | display string @ line 365 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1366 | string | display string @ line 1366 | (9 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1413 | string | display string @ line 1413 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1443 | string | display string @ line 1443 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1621 | string | display string @ line 1621 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1641 | string | display string @ line 1641 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1661 | string | display string @ line 1661 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### paleoclimate_visualization.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 132 | string | display string @ line 132 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 423 | string | display string @ line 423 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 457 | string | display string @ line 457 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### paleoclimate_visualization_full.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 191 | string | display string @ line 191 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 937 | string | display string @ line 937 | (9 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 984 | string | display string @ line 984 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1014 | string | display string @ line 1014 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1192 | string | display string @ line 1192 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1212 | string | display string @ line 1212 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1232 | string | display string @ line 1232 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### paleoclimate_wet_bulb_full.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 135 | constant | BASELINE_ABSOLUTE_TEMP | 14.0 | 4 | 5 | **20** | No source citation (recalled) | MEASURED -- independently catalogued fact (name) |
| 137 | constant | TW_SURVIVABILITY_BIOLOGICAL | 31.0 | 4 | 5 | **20** | No source citation (recalled) | UNDETERMINED -- could not be classified |
| 138 | constant | TW_SURVIVABILITY_THEORETICAL | 35.0 | 4 | 5 | **20** | No source citation (recalled) | UNDETERMINED -- could not be classified |
| 122 | string | display string @ line 122 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 130 | string | display string @ line 130 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 164 | string | display string @ line 164 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 253 | string | display string @ line 253 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 475 | string | display string @ line 475 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1761 | string | display string @ line 1761 | (9 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1808 | string | display string @ line 1808 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1838 | string | display string @ line 1838 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2016 | string | display string @ line 2016 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2036 | string | display string @ line 2036 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2056 | string | display string @ line 2056 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### planet_visualization_utilities.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 547 | dict | ROTATION_AXIS_OMITTED[...] | (2 entries) | 4 | 5 | **20** | No source citation (recalled) | UNDETERMINED -- could not be classified |
| 451 | string | display string @ line 451 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 693 | string | display string @ line 693 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 695 | string | display string @ line 695 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 700 | string | display string @ line 700 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 704 | string | display string @ line 704 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 712 | string | display string @ line 712 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 720 | string | display string @ line 720 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### planetarium_distance.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 231 | string | display string @ line 231 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### plot_data_report_widget.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 280 | string | display string @ line 280 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### scenarios_coral_bleaching.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 64 | string | display string @ line 64 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### scenarios_heatwaves.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 97 | dict | HEATWAVE_THRESHOLDS[...] | (15 entries) | 4 | 5 | **20** | No source citation (recalled) | MEASURED -- independently catalogued fact (name) |

### scenarios_western_heatwave_march_2026.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 64 | dict | WESTERN_HEATWAVE_THRESHOLDS[...] | (15 entries) | 4 | 5 | **20** | No source citation (recalled) | MEASURED -- independently catalogued fact (name) |
| 1 | string | display string @ line 1 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 920 | string | display string @ line 920 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1164 | string | display string @ line 1164 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1274 | string | display string @ line 1274 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### sgr_a_grand_tour.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 65 | constant | REFERENCE_YEAR | 2025.0 | 4 | 5 | **20** | No source citation (recalled) | UNDETERMINED -- could not be classified |
| 566 | string | display string @ line 566 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 578 | string | display string @ line 578 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 590 | string | display string @ line 590 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 602 | string | display string @ line 602 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 624 | string | display string @ line 624 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 634 | string | display string @ line 634 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### sgr_a_star_data.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 55 | dict | B_STAR_TEMPERATURES[...] | (10 entries) | 4 | 5 | **20** | No source citation (recalled) | MEASURED -- independently catalogued fact (name) |

### sgr_a_visualization_core.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 154 | string | display string @ line 154 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 262 | string | display string @ line 262 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 331 | string | display string @ line 331 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 384 | string | display string @ line 384 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### sgr_a_visualization_precession.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 301 | string | display string @ line 301 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 442 | string | display string @ line 442 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### shell_configs.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 162 | string | display string @ line 162 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 168 | string | display string @ line 168 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 305 | string | display string @ line 305 | (9 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 326 | string | display string @ line 326 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 344 | string | display string @ line 344 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 364 | string | display string @ line 364 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 508 | string | display string @ line 508 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 531 | string | display string @ line 531 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 552 | string | display string @ line 552 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 568 | string | display string @ line 568 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 582 | string | display string @ line 582 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 615 | string | display string @ line 615 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 632 | string | display string @ line 632 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 662 | string | display string @ line 662 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 681 | string | display string @ line 681 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 723 | string | display string @ line 723 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 731 | string | display string @ line 731 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 757 | string | display string @ line 757 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 841 | string | display string @ line 841 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 939 | string | display string @ line 939 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1024 | string | display string @ line 1024 | (5 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1060 | string | display string @ line 1060 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1239 | string | display string @ line 1239 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1251 | string | display string @ line 1251 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1374 | string | display string @ line 1374 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1390 | string | display string @ line 1390 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1396 | string | display string @ line 1396 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1434 | string | display string @ line 1434 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1441 | string | display string @ line 1441 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1457 | string | display string @ line 1457 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1464 | string | display string @ line 1464 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1480 | string | display string @ line 1480 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1563 | string | display string @ line 1563 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1579 | string | display string @ line 1579 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1588 | string | display string @ line 1588 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1606 | string | display string @ line 1606 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1613 | string | display string @ line 1613 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1630 | string | display string @ line 1630 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2127 | string | display string @ line 2127 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2395 | string | display string @ line 2395 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2500 | string | display string @ line 2500 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### visualization_utils.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 342 | string | display string @ line 342 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

---

## Tier 2: ALL ACCEPTED RESIDUALS -- see note below (Score 10-15)

### apsidal_markers.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1857 | constant | ENCOUNTER_THRESHOLD_AU | 0.5 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |

### asteroid_belt_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 111 | constant | MAIN_BELT_INNER | 2.2 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 112 | constant | MAIN_BELT_OUTER | 3.2 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 113 | constant | MAIN_BELT_PEAK | 2.7 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 115 | constant | HILDA_DISTANCE | 3.97 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 116 | constant | TROJAN_DISTANCE | 5.2 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 80 | string | display string @ line 80 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 132 | string | display string @ line 132 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### celestial_coordinates.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 140 | dict | MAJOR_BODY_UNCERTAINTIES[...] | (206 entries) | 3 | 5 | **15** | Cited, not cross-checked; date-sensitive | MEASURED -- independently catalogued fact (key) |
| 387 | string | display string @ line 387 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 454 | string | display string @ line 454 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### celestial_objects.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 47 | string | display string @ line 47 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 52 | string | display string @ line 52 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 60 | string | display string @ line 60 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 79 | string | display string @ line 79 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 101 | string | display string @ line 101 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 109 | string | display string @ line 109 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 115 | string | display string @ line 115 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 121 | string | display string @ line 121 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 127 | string | display string @ line 127 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 148 | string | display string @ line 148 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 164 | string | display string @ line 164 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 170 | string | display string @ line 170 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 196 | string | display string @ line 196 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 211 | string | display string @ line 211 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 235 | string | display string @ line 235 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 263 | string | display string @ line 263 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 271 | string | display string @ line 271 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 283 | string | display string @ line 283 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 294 | string | display string @ line 294 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 299 | string | display string @ line 299 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 332 | string | display string @ line 332 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 365 | string | display string @ line 365 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 382 | string | display string @ line 382 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 457 | string | display string @ line 457 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 511 | string | display string @ line 511 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 574 | string | display string @ line 574 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 631 | string | display string @ line 631 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 650 | string | display string @ line 650 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 666 | string | display string @ line 666 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 673 | string | display string @ line 673 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 920 | string | display string @ line 920 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 925 | string | display string @ line 925 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 930 | string | display string @ line 930 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 935 | string | display string @ line 935 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1055 | string | display string @ line 1055 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1060 | string | display string @ line 1060 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1115 | string | display string @ line 1115 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1122 | string | display string @ line 1122 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1129 | string | display string @ line 1129 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1136 | string | display string @ line 1136 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1143 | string | display string @ line 1143 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1149 | string | display string @ line 1149 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1155 | string | display string @ line 1155 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1165 | string | display string @ line 1165 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1173 | string | display string @ line 1173 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1181 | string | display string @ line 1181 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1189 | string | display string @ line 1189 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1197 | string | display string @ line 1197 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1205 | string | display string @ line 1205 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1213 | string | display string @ line 1213 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1221 | string | display string @ line 1221 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1240 | string | display string @ line 1240 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1263 | string | display string @ line 1263 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1271 | string | display string @ line 1271 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### close_approach_data.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### comet_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1530 | dict | comet_visualization_info[...] | (6 entries) | 3 | 5 | **15** | Cited, not independently cross-checked | UNDETERMINED -- could not be classified |
| 93 | string | display string @ line 93 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 209 | string | display string @ line 209 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 235 | string | display string @ line 235 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 256 | string | display string @ line 256 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 283 | string | display string @ line 283 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 294 | string | display string @ line 294 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 305 | string | display string @ line 305 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 334 | string | display string @ line 334 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 522 | string | display string @ line 522 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 528 | string | display string @ line 528 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 535 | string | display string @ line 535 | (16 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 701 | string | display string @ line 701 | (14 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1177 | string | display string @ line 1177 | (3 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 1351 | string | display string @ line 1351 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1532 | string | display string @ line 1532 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1542 | string | display string @ line 1542 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1552 | string | display string @ line 1552 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1561 | string | display string @ line 1561 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1570 | string | display string @ line 1570 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1580 | string | display string @ line 1580 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### constants_new.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 54 | constant | KM_PER_AU | 149597870.7 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 61 | constant | SUN_RADIUS_KM | 695700.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 70 | constant | EARTH_EQUATORIAL_RADIUS_KM | 6378.137 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 76 | constant | EARTH_POLAR_RADIUS_KM | 6356.752 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 81 | constant | JUPITER_EQUATORIAL_RADIUS_KM | 71492.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 86 | constant | JUPITER_POLAR_RADIUS_KM | 66854.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 91 | constant | SPEED_OF_LIGHT_KM_S | 299792.458 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 180 | constant | TERMINATION_SHOCK_AU | 94 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 195 | constant | INNER_LIMIT_OORT_CLOUD_AU | 2000 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 199 | constant | INNER_OORT_CLOUD_AU | 20000 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 203 | constant | OUTER_OORT_CLOUD_AU | 100000 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 207 | constant | GRAVITATIONAL_INFLUENCE_AU | 126000 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 257 | constant | MERCURY_RADIUS_KM | 2439.7 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 260 | constant | VENUS_RADIUS_KM | 6051.8 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 263 | constant | MOON_RADIUS_KM | 1737.4 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 266 | constant | MARS_RADIUS_KM | 3396.2 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 269 | constant | PHOBOS_RADIUS_KM | 11.1 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 272 | constant | SATURN_RADIUS_KM | 60268 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 275 | constant | URANUS_RADIUS_KM | 25559 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 278 | constant | NEPTUNE_RADIUS_KM | 24764 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 281 | constant | PLUTO_RADIUS_KM | 1188.3 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 284 | constant | BENNU_RADIUS_KM | 0.262 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 287 | constant | ERIS_RADIUS_KM | 1163 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 290 | constant | HAUMEA_RADIUS_KM | 816 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 293 | constant | MAKEMAKE_RADIUS_KM | 715 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 296 | constant | ARROKOTH_RADIUS_KM | 9.95 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 326 | dict | KNOWN_ORBITAL_PERIODS[...] | (133 entries) | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1 | string | display string @ line 1 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 138 | constant | CHROMOSPHERE_RADII | 1.5 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 143 | constant | INNER_CORONA_RADII | 3 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 148 | constant | OUTER_CORONA_RADII | 50 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 154 | constant | STREAMER_BELT_RADII | 6.0 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 159 | constant | ROCHE_LIMIT_RADII | 3.45 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 168 | constant | ALFVEN_SURFACE_RADII | 18.8 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 186 | constant | HELIOPAUSE_RADII | 26449 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 213 | constant | PARKER_CLOSEST_RADII | 9.86 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 300 | dict | CENTER_BODY_RADII[...] | (1 entry) | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |

### coordinate_system_guide.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 248 | string | display string @ line 248 | (9 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### earth_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 55 | string | display string @ line 55 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 71 | string | display string @ line 71 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 127 | string | display string @ line 127 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 143 | string | display string @ line 143 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 199 | string | display string @ line 199 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 214 | string | display string @ line 214 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 269 | string | display string @ line 269 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 284 | string | display string @ line 284 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 339 | string | display string @ line 339 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 354 | string | display string @ line 354 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 492 | string | display string @ line 492 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 508 | string | display string @ line 508 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 564 | string | display string @ line 564 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 580 | string | display string @ line 580 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 637 | string | display string @ line 637 | (7 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 701 | string | display string @ line 701 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 750 | string | display string @ line 750 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 788 | string | display string @ line 788 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 790 | string | display string @ line 790 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 870 | string | display string @ line 870 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 890 | string | display string @ line 890 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 943 | string | display string @ line 943 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 983 | string | display string @ line 983 | (6 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 997 | string | display string @ line 997 | (7 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1049 | string | display string @ line 1049 | (5 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1089 | string | display string @ line 1089 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1112 | string | display string @ line 1112 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### eris_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 56 | string | display string @ line 56 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 212 | string | display string @ line 212 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 462 | string | display string @ line 462 | (5 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 479 | string | display string @ line 479 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### exoplanet_coordinates.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 36 | string | display string @ line 36 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### food_insecurity_generator.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 157 | string | display string @ line 157 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### idealized_orbits.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1515 | string | display string @ line 1515 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1628 | string | display string @ line 1628 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1771 | string | display string @ line 1771 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1838 | string | display string @ line 1838 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2546 | string | display string @ line 2546 | (7 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2710 | string | display string @ line 2710 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2777 | string | display string @ line 2777 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2843 | string | display string @ line 2843 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 3044 | string | display string @ line 3044 | (9 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 3583 | string | display string @ line 3583 | (1 claim) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 3698 | string | display string @ line 3698 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 3757 | string | display string @ line 3757 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 4404 | string | display string @ line 4404 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 5816 | string | display string @ line 5816 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |

### info_dictionary.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 38 | string | display string @ line 38 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 286 | string | display string @ line 286 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 293 | string | display string @ line 293 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 300 | string | display string @ line 300 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 305 | string | display string @ line 305 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 343 | string | display string @ line 343 | (8 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 363 | string | display string @ line 363 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 383 | string | display string @ line 383 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 421 | string | display string @ line 421 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 440 | string | display string @ line 440 | (8 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 469 | string | display string @ line 469 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 492 | string | display string @ line 492 | (4 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 502 | string | display string @ line 502 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 518 | string | display string @ line 518 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 527 | string | display string @ line 527 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 560 | string | display string @ line 560 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 594 | string | display string @ line 594 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 608 | string | display string @ line 608 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 622 | string | display string @ line 622 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 630 | string | display string @ line 630 | (10 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 660 | string | display string @ line 660 | (9 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 683 | string | display string @ line 683 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 712 | string | display string @ line 712 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 725 | string | display string @ line 725 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 745 | string | display string @ line 745 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 748 | string | display string @ line 748 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 752 | string | display string @ line 752 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 754 | string | display string @ line 754 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 765 | string | display string @ line 765 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 769 | string | display string @ line 769 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 773 | string | display string @ line 773 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 778 | string | display string @ line 778 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 795 | string | display string @ line 795 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 835 | string | display string @ line 835 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 856 | string | display string @ line 856 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 869 | string | display string @ line 869 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 872 | string | display string @ line 872 | (11 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 901 | string | display string @ line 901 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 905 | string | display string @ line 905 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 908 | string | display string @ line 908 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 911 | string | display string @ line 911 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 914 | string | display string @ line 914 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 918 | string | display string @ line 918 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 923 | string | display string @ line 923 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 926 | string | display string @ line 926 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 930 | string | display string @ line 930 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 935 | string | display string @ line 935 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 939 | string | display string @ line 939 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 949 | string | display string @ line 949 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 953 | string | display string @ line 953 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 961 | string | display string @ line 961 | (5 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 969 | string | display string @ line 969 | (8 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1001 | string | display string @ line 1001 | (5 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1016 | string | display string @ line 1016 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1037 | string | display string @ line 1037 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1060 | string | display string @ line 1060 | (7 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1079 | string | display string @ line 1079 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1096 | string | display string @ line 1096 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1106 | string | display string @ line 1106 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1109 | string | display string @ line 1109 | (7 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1116 | string | display string @ line 1116 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1124 | string | display string @ line 1124 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1142 | string | display string @ line 1142 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1159 | string | display string @ line 1159 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1162 | string | display string @ line 1162 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1179 | string | display string @ line 1179 | (5 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1199 | string | display string @ line 1199 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1251 | string | display string @ line 1251 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1255 | string | display string @ line 1255 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1316 | string | display string @ line 1316 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1326 | string | display string @ line 1326 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1330 | string | display string @ line 1330 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1360 | string | display string @ line 1360 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1373 | string | display string @ line 1373 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1390 | string | display string @ line 1390 | (4 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1428 | string | display string @ line 1428 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1468 | string | display string @ line 1468 | (11 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1487 | string | display string @ line 1487 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1518 | string | display string @ line 1518 | (7 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1567 | string | display string @ line 1567 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1571 | string | display string @ line 1571 | (4 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1598 | string | display string @ line 1598 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1602 | string | display string @ line 1602 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1642 | string | display string @ line 1642 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1700 | string | display string @ line 1700 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1704 | string | display string @ line 1704 | (18 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1776 | string | display string @ line 1776 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1817 | string | display string @ line 1817 | (7 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1869 | string | display string @ line 1869 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1873 | string | display string @ line 1873 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1880 | string | display string @ line 1880 | (6 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1907 | string | display string @ line 1907 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1917 | string | display string @ line 1917 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1928 | string | display string @ line 1928 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1940 | string | display string @ line 1940 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1951 | string | display string @ line 1951 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1960 | string | display string @ line 1960 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2000 | string | display string @ line 2000 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2030 | string | display string @ line 2030 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2049 | string | display string @ line 2049 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2064 | string | display string @ line 2064 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2083 | string | display string @ line 2083 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2095 | string | display string @ line 2095 | (27 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2140 | string | display string @ line 2140 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2159 | string | display string @ line 2159 | (7 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 2183 | string | display string @ line 2183 | (1 claim) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 2186 | string | display string @ line 2186 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2187 | string | display string @ line 2187 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2188 | string | display string @ line 2188 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2189 | string | display string @ line 2189 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2190 | string | display string @ line 2190 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2191 | string | display string @ line 2191 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2192 | string | display string @ line 2192 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2193 | string | display string @ line 2193 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2197 | string | display string @ line 2197 | (8 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2224 | string | display string @ line 2224 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2234 | string | display string @ line 2234 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2244 | string | display string @ line 2244 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2245 | string | display string @ line 2245 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2246 | string | display string @ line 2246 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

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
| 702 | string | display string @ line 702 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 792 | string | display string @ line 792 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 806 | string | display string @ line 806 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 915 | string | display string @ line 915 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 930 | string | display string @ line 930 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 945 | string | display string @ line 945 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1027 | string | display string @ line 1027 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### mars_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 517 | string | display string @ line 517 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 600 | string | display string @ line 600 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 712 | string | display string @ line 712 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 840 | string | display string @ line 840 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### mercury_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 47 | string | display string @ line 47 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 61 | string | display string @ line 61 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 70 | string | display string @ line 70 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 84 | string | display string @ line 84 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 236 | string | display string @ line 236 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 292 | string | display string @ line 292 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 401 | string | display string @ line 401 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### moon_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 56 | string | display string @ line 56 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 124 | string | display string @ line 124 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 211 | string | display string @ line 211 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 560 | string | display string @ line 560 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### neptune_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 113 | string | display string @ line 113 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 132 | string | display string @ line 132 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 197 | string | display string @ line 197 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 462 | string | display string @ line 462 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 597 | string | display string @ line 597 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 686 | string | display string @ line 686 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 864 | string | display string @ line 864 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 886 | string | display string @ line 886 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 911 | string | display string @ line 911 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
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

### object_type_analyzer.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 662 | string | display string @ line 662 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### paleoclimate_human_origins_full.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 209 | string | display string @ line 209 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 231 | string | display string @ line 231 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### paleoclimate_wet_bulb_full.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 125 | string | display string @ line 125 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 341 | string | display string @ line 341 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

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
| 500 | string | display string @ line 500 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 504 | string | display string @ line 504 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 508 | string | display string @ line 508 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 512 | string | display string @ line 512 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 516 | string | display string @ line 516 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 520 | string | display string @ line 520 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 524 | string | display string @ line 524 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 528 | string | display string @ line 528 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 532 | string | display string @ line 532 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 536 | string | display string @ line 536 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 540 | string | display string @ line 540 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### pluto_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 36 | string | display string @ line 36 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 53 | string | display string @ line 53 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 126 | string | display string @ line 126 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 143 | string | display string @ line 143 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 209 | string | display string @ line 209 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 376 | string | display string @ line 376 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 397 | string | display string @ line 397 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 497 | string | display string @ line 497 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 569 | string | display string @ line 569 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 590 | string | display string @ line 590 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### saturn_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 56 | string | display string @ line 56 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 142 | string | display string @ line 142 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 278 | string | display string @ line 278 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 299 | string | display string @ line 299 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 503 | string | display string @ line 503 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 770 | string | display string @ line 770 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 932 | string | display string @ line 932 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 952 | string | display string @ line 952 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1231 | string | display string @ line 1231 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### scenarios_coral_bleaching.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 168 | dict | CORAL_THRESHOLDS[...] | (16 entries) | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 101 | string | display string @ line 101 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### scenarios_heatwaves.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 259 | string | display string @ line 259 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
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
| 1226 | string | display string @ line 1226 | (3 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 1397 | string | display string @ line 1397 | (1 claim) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 1474 | string | display string @ line 1474 | (1 claim) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |

### sgr_a_grand_tour.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 614 | string | display string @ line 614 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### sgr_a_star_data.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 151 | constant | G_CONST | 6.6743e-11 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 152 | constant | SPEED_OF_LIGHT | 299792458.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 153 | constant | SOLAR_MASS_KG | 1.989e+30 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 164 | constant | PARSEC_TO_AU | 206265.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 165 | constant | YEAR_TO_SECONDS | 365.25 * 24 * 3600 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 171 | constant | SGR_A_MASS_SOLAR | 4154000.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 173 | constant | SGR_A_DISTANCE_PC | 8178.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 174 | constant | SGR_A_DISTANCE_LY | 26670.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 477 | string | display string @ line 477 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 498 | string | display string @ line 498 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### sgr_a_visualization_precession.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 441 | string | display string @ line 441 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### shell_configs.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 125 | string | display string @ line 125 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 129 | string | display string @ line 129 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 226 | string | display string @ line 226 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 256 | string | display string @ line 256 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 276 | string | display string @ line 276 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 417 | string | display string @ line 417 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 446 | string | display string @ line 446 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 472 | string | display string @ line 472 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 489 | string | display string @ line 489 | (9 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 900 | string | display string @ line 900 | (5 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 909 | string | display string @ line 909 | (5 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 933 | string | display string @ line 933 | (2 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 1295 | string | display string @ line 1295 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1320 | string | display string @ line 1320 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1327 | string | display string @ line 1327 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1344 | string | display string @ line 1344 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1351 | string | display string @ line 1351 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1368 | string | display string @ line 1368 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1411 | string | display string @ line 1411 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1419 | string | display string @ line 1419 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1489 | string | display string @ line 1489 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1513 | string | display string @ line 1513 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1519 | string | display string @ line 1519 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1535 | string | display string @ line 1535 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1541 | string | display string @ line 1541 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1556 | string | display string @ line 1556 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1640 | string | display string @ line 1640 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2113 | string | display string @ line 2113 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2143 | string | display string @ line 2143 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2176 | string | display string @ line 2176 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2213 | string | display string @ line 2213 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2251 | string | display string @ line 2251 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2267 | string | display string @ line 2267 | (7 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2286 | string | display string @ line 2286 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2309 | string | display string @ line 2309 | (6 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2351 | string | display string @ line 2351 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2367 | string | display string @ line 2367 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2382 | string | display string @ line 2382 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2411 | string | display string @ line 2411 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2452 | string | display string @ line 2452 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2468 | string | display string @ line 2468 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2486 | string | display string @ line 2486 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2517 | string | display string @ line 2517 | (10 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2568 | string | display string @ line 2568 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2584 | string | display string @ line 2584 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2615 | string | display string @ line 2615 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2658 | string | display string @ line 2658 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2674 | string | display string @ line 2674 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2708 | string | display string @ line 2708 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### solar_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 52 | string | display string @ line 52 | (7 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 78 | string | display string @ line 78 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 96 | string | display string @ line 96 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 111 | string | display string @ line 111 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 126 | string | display string @ line 126 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 151 | string | display string @ line 151 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 176 | string | display string @ line 176 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 201 | string | display string @ line 201 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 234 | string | display string @ line 234 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 248 | string | display string @ line 248 | (8 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 268 | string | display string @ line 268 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 300 | string | display string @ line 300 | (6 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 329 | string | display string @ line 329 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 362 | string | display string @ line 362 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 426 | string | display string @ line 426 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 541 | string | display string @ line 541 | (7 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 563 | string | display string @ line 563 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 606 | string | display string @ line 606 | (17 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 635 | string | display string @ line 635 | (14 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 661 | string | display string @ line 661 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 689 | string | display string @ line 689 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 712 | string | display string @ line 712 | (7 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 859 | string | display string @ line 859 | (19 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 886 | string | display string @ line 886 | (19 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 910 | string | display string @ line 910 | (5 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |

### spacecraft_encounters.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 70 | constant | AU_KM | 149597870.7 | 3 | 5 | **15** | Cited, not cross-checked; date-sensitive | MEASURED -- independently catalogued fact (name) |
| 1 | string | display string @ line 1 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 117 | string | display string @ line 117 | (5 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 146 | string | display string @ line 146 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 172 | string | display string @ line 172 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 216 | string | display string @ line 216 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1493 | string | display string @ line 1493 | (7 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1509 | string | display string @ line 1509 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### star_notes.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 65 | string | display string @ line 65 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 119 | string | display string @ line 119 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 163 | string | display string @ line 163 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 210 | string | display string @ line 210 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 228 | string | display string @ line 228 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 242 | string | display string @ line 242 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 281 | string | display string @ line 281 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 314 | string | display string @ line 314 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 341 | string | display string @ line 341 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 394 | string | display string @ line 394 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 421 | string | display string @ line 421 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 474 | string | display string @ line 474 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 510 | string | display string @ line 510 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
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
| 897 | string | display string @ line 897 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 928 | string | display string @ line 928 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 976 | string | display string @ line 976 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1032 | string | display string @ line 1032 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1049 | string | display string @ line 1049 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1124 | string | display string @ line 1124 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1192 | string | display string @ line 1192 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### star_sphere_builder.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 46 | constant | OBLIQUITY_DEG | 23.4393 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 79 | string | display string @ line 79 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### uranus_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 39 | string | display string @ line 39 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 54 | string | display string @ line 54 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 124 | string | display string @ line 124 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 184 | string | display string @ line 184 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 203 | string | display string @ line 203 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 361 | string | display string @ line 361 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 380 | string | display string @ line 380 | (9 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 449 | string | display string @ line 449 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 535 | string | display string @ line 535 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 628 | string | display string @ line 628 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 804 | string | display string @ line 804 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 848 | string | display string @ line 848 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 864 | string | display string @ line 864 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 882 | string | display string @ line 882 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 899 | string | display string @ line 899 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 917 | string | display string @ line 917 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 936 | string | display string @ line 936 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 954 | string | display string @ line 954 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 974 | string | display string @ line 974 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 993 | string | display string @ line 993 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1013 | string | display string @ line 1013 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1146 | string | display string @ line 1146 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1165 | string | display string @ line 1165 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### venus_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 41 | string | display string @ line 41 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 58 | string | display string @ line 58 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 420 | string | display string @ line 420 | (12 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 508 | string | display string @ line 508 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 652 | string | display string @ line 652 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### visualization_3d.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 725 | string | display string @ line 725 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 748 | string | display string @ line 748 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 785 | string | display string @ line 785 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

---

## Tier 3: ALREADY CITED OR LOW RISK -- no action required (Score 5-9)

### add_docstrings.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 118 | dict | DOCSTRINGS[...] | (42 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### close_approach_data.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 68 | dict | CAD_BODY_NAMES[...] | (11 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal use (name vocabulary) |

### data_inventory.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 30 | constant | PAGES_CEILING_MB | 1024 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### dep_trace.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 40 | constant | HUB_THRESHOLD | 8 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 52 | dict | _ROLE_TO_VISUAL[...] | (12 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 67 | dict | CATEGORY_COLORS[...] | (10 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### exoplanet_systems.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 41 | dict | TRAPPIST1_SYSTEM[...] | (6 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal use (key vocabulary) |
| 327 | dict | TOI1338_SYSTEM[...] | (6 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal use (key vocabulary) |
| 486 | dict | PROXIMA_SYSTEM[...] | (6 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal use (key vocabulary) |

### export_orbit_cache.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 206 | dict | CENTER_SLUG_MAP[...] | (22 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |

### food_insecurity_generator.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 110 | constant | P5_DOT_MIN_SCALE | 0.5 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |
| 111 | constant | P5_DOT_MAX_SCALE | 1.8 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |

### info_dictionary.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 107 | dict | object_type_mapping[...] | (79 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal use (name vocabulary) |
| 243 | dict | class_mapping[...] | (14 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal use (name vocabulary) |
| 262 | dict | INFO[...] | (183 entries) | 3 | 2 | **6** | Cited, not cross-checked; date-sensitive | Internal use (key vocabulary) |

### ledger_index.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 170 | dict | SECTION_ALIASES[...] | (1 entry) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 174 | dict | SECTION_TITLES[...] | (26 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 482 | dict | ISSUE_TAGS[...] | (4 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### measure_perframe_elements.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 41 | constant | KB | 1000.0 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 42 | constant | FRAMES_29 | 29 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 43 | constant | FRAMES_60 | 60 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### module_atlas.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 97 | dict | ROLE_MAP[...] | (114 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 352 | dict | ROLE_DESCRIPTIONS[...] | (12 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 374 | dict | ROLE_SECTION_TITLES[...] | (12 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### orbit_data_manager.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 37 | constant | DEFAULT_DAYS_AHEAD | 730 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'cache') |
| 38 | constant | MAX_DATA_AGE_DAYS | 90 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'cache') |

### osculating_cache_manager.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 82 | dict | REFRESH_INTERVALS[...] | (14 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'cache') |

### palomas_orrery.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 2080 | constant | PERFRAME_INDICATOR_RADIUS_FACTOR | 100.0 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |
| 2113 | constant | PERFRAME_COORD_DECIMALS | 7 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |
| 3688 | constant | BUTTON_WIDTH | 14 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |

### palomas_orrery_dashboard.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 60 | constant | WINDOW_WIDTH | 960 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |
| 61 | constant | WINDOW_HEIGHT | 720 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |
| 336 | dict | SECTION_SYMBOLS[...] | (4 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'gui') |

### provenance_scanner.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 294 | constant | V_FETCHED | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 295 | constant | V_CROSS_CHECKED | 2 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 304 | constant | V_SOURCED | 3 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 307 | constant | V_RECALLED | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 316 | constant | C_COSMETIC | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 317 | constant | C_INTERNAL | 2 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 318 | constant | C_LOADBEARING | 3 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 319 | constant | C_PUBLIC | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 320 | constant | C_PROPAGATING | 5 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 325 | constant | C_RELATIONAL | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 326 | constant | C_MEASURED | 5 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 331 | constant | C_UNDETERMINED | 5 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 432 | dict | DOMAIN_LABELS[...] | (6 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 441 | dict | MODULE_DOMAIN_MAP[...] | (100 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### sgr_a_grand_tour.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 48 | constant | ANIMATION_FRAMES | 140 | 4 | 2 | **8** | No source citation (recalled) | Internal use (name vocabulary) |
| 49 | constant | POINTS_PER_ORBIT | 80 | 4 | 2 | **8** | No source citation (recalled) | Internal use (name vocabulary) |
| 57 | dict | ROSETTE_ORBIT_COUNTS[...] | (4 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (name vocabulary) |

### sgr_a_visualization_animation.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 27 | dict | ANIMATION_CONFIG[...] | (5 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (name vocabulary) |

### sgr_a_visualization_precession.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 33 | dict | S4714_ACCURACY_PATCH[...] | (1 entry) | 4 | 2 | **8** | No source citation (recalled) | Internal use (name vocabulary) |

### skills_index.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 94 | constant | NAME_COL_WIDTH | 29 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 95 | constant | VER_COL_WIDTH | 5 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 97 | constant | WRAP_WIDTH | 79 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 98 | constant | FALLBACK_TRUNC | 60 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### star_sphere_builder.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 496 | dict | CONSTELLATION_NAMES[...] | (88 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (name vocabulary) |
| 32 | constant | VMAG_LIMIT | 3.5 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal use (name vocabulary) |
| 65 | constant | CIRCLE_POINTS | 120 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal use (name vocabulary) |

### test_reset_completeness.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 43 | dict | ENTRY_DEFAULTS[...] | (10 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

---

## Tier 4: NO ACTION NEEDED (Score 1-4)

### constants_new.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 116 | constant | DEFAULT_MARKER_SIZE | 7 | 3 | 1 | **3** | Cited, not independently cross-checked | Cosmetic (name vocabulary) |
| 118 | constant | CENTER_MARKER_SIZE | 10 | 3 | 1 | **3** | Cited, not independently cross-checked | Cosmetic (name vocabulary) |

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
