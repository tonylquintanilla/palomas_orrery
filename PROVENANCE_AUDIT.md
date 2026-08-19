# Paloma's Orrery -- Provenance Audit

Generated: August 19, 2026
Files scanned: 129
Total findings: 1027
Constants: 108 | Dicts: 39 | Display strings: 880

Unit of provenance: the smallest thing with a coherent source citation. A dict with one block-level `# Source:` comment is ONE unit; all its entries inherit that citation. A hover string with co-referring numbers is ONE unit.

**Color values are excluded from this audit.** RGB/color fields are never scored as claims (see _make_dict_unit), and a dict's block `# Source:` citation should never be read as covering that dict's `color` field(s), even when it covers everything else in the same unit. This does not mean color choices have no basis at all -- some are loosely informed by real imagery or composition data -- but color selection across this codebase is inconsistent in method: sometimes evidence-informed, sometimes chosen purely for visual contrast or distinction, sometimes arbitrary. Treat every color value as a developer/AI judgment call, not a measured or verified quantity, regardless of what citation sits nearby. (Tony's call, July 16, 2026; a low-priority wishlist item for a real, systematic color-accuracy pass is tracked at LEDGER_CONSOLIDATED.md L-124.)

---

## Run History

The last 6 recorded scanner runs, newest first. Written by provenance_history.py and tracked in git: when an audit was taken, and against which commit, is itself provenance.

A run is expected every 1 day(s). Nothing here affects the exit code -- the delta informs the push call, it does not make it.

| Run (UTC) | HEAD | Files | Total | T1 | T2 | T3 | T4 |
|-----------|------|------:|------:|---:|---:|---:|---:|
| 20260819T175306Z | `d2cb527` | 129 | 1027 | 289 | 621 | 115 | 2 |
| 20260819T174326Z | `d5814d3` | 128 | 1026 | 289 | 620 | 115 | 2 |
| 20260819T172341Z | `894f015` | 128 | 1025 | 289 | 620 | 114 | 2 |
| 20260819T025354Z | `eae95f5` | 128 | 1025 | 289 | 620 | 114 | 2 |
| 20260818T232216Z | `c5c0102` | 129 | 1027 | 289 | 622 | 114 | 2 |
| 20260818T213246Z | `731066f` | 129 | 1026 | 289 | 621 | 114 | 2 |

Change since the previous run: total +1, Tier-1 +0.

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
| 1 | 16-20 | FIX NOW | 289 |
| 2 | 10-15 | REVIEW | 621 |
| 3 | 5-9 | LOW PRIORITY | 115 |
| 4 | 1-4 | LOWEST PRIORITY | 2 |

**Tier 2 note (April 2026 audit):** All Tier-2 findings are documented
accepted residuals -- cited constants, V_STALE staleness flags on verified
strings, or known scanner limitations. No action required unless a new
uncited entry appears. See Accepted Residuals block below for details.

---

## Findings by File

Quick-reference counts before the per-tier detail below. Same data, grouped the other way: every file that has at least one finding, with its count in each tier.

| File | Domain | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Total |
|------|--------|-------:|-------:|-------:|-------:|------:|
| `info_dictionary.py` | orrery | 2 | 123 | 3 | 0 | 128 |
| `shell_configs.py` | orrery | 35 | 81 | 0 | 0 | 116 |
| `paleoclimate_wet_bulb_full.py` | earth_science | 44 | 22 | 0 | 0 | 66 |
| `celestial_objects.py` | orrery | 0 | 51 | 0 | 0 | 51 |
| `paleoclimate_human_origins_full.py` | earth_science | 40 | 6 | 0 | 0 | 46 |
| `idealized_orbits.py` | orrery | 29 | 12 | 0 | 0 | 41 |
| `constants_new.py` | orrery | 0 | 32 | 5 | 2 | 39 |
| `star_notes.py` | stars | 1 | 37 | 0 | 0 | 38 |
| `paleoclimate_visualization_full.py` | earth_science | 28 | 6 | 0 | 0 | 34 |
| `neptune_visualization_shells.py` | orrery | 0 | 28 | 0 | 0 | 28 |
| `earth_visualization_shells.py` | earth_science | 1 | 26 | 0 | 0 | 27 |
| `solar_visualization_shells.py` | orrery | 3 | 24 | 0 | 0 | 27 |
| `uranus_visualization_shells.py` | orrery | 1 | 24 | 0 | 0 | 25 |
| `comet_visualization_shells.py` | orrery | 4 | 20 | 0 | 0 | 24 |
| `planet_visualization_utilities.py` | orrery | 4 | 15 | 0 | 0 | 19 |
| `jupiter_visualization_shells.py` | orrery | 0 | 19 | 0 | 0 | 19 |
| `provenance_scanner.py` | dev_tools | 0 | 0 | 16 | 0 | 16 |
| `sgr_a_star_data.py` | orrery | 4 | 10 | 0 | 0 | 14 |
| `venus_visualization_shells.py` | orrery | 3 | 4 | 6 | 0 | 13 |
| `scenarios_heatwaves.py` | earth_science | 3 | 9 | 0 | 0 | 12 |
| `scenarios_western_heatwave_march_2026.py` | earth_science | 10 | 1 | 0 | 0 | 11 |
| `sgr_a_grand_tour.py` | orrery | 8 | 0 | 3 | 0 | 11 |
| `mars_visualization_shells.py` | orrery | 4 | 3 | 4 | 0 | 11 |
| `mercury_visualization_shells.py` | orrery | 1 | 5 | 5 | 0 | 11 |
| `moon_visualization_shells.py` | orrery | 3 | 4 | 4 | 0 | 11 |
| `paleoclimate_dual_scale.py` | earth_science | 10 | 1 | 0 | 0 | 11 |
| `pluto_visualization_shells.py` | orrery | 0 | 0 | 11 | 0 | 11 |
| `saturn_visualization_shells.py` | orrery | 1 | 9 | 0 | 0 | 10 |
| `food_insecurity_generator.py` | earth_science | 5 | 2 | 2 | 0 | 9 |
| `eris_visualization_shells.py` | orrery | 2 | 4 | 2 | 0 | 8 |
| `spacecraft_encounters.py` | orrery | 0 | 8 | 0 | 0 | 8 |
| `asteroid_belt_visualization_shells.py` | orrery | 0 | 7 | 0 | 0 | 7 |
| `celestial_coordinates.py` | orrery | 4 | 2 | 0 | 0 | 6 |
| `paleoclimate_visualization.py` | earth_science | 6 | 0 | 0 | 0 | 6 |
| `exoplanet_coordinates.py` | stars | 5 | 0 | 0 | 0 | 5 |
| `sgr_a_visualization_precession.py` | orrery | 4 | 0 | 1 | 0 | 5 |
| `star_sphere_builder.py` | stars | 0 | 2 | 3 | 0 | 5 |
| `fetch_climate_data.py` | earth_science | 0 | 5 | 0 | 0 | 5 |
| `planet9_visualization_shells.py` | orrery | 0 | 5 | 0 | 0 | 5 |
| `worksheet_checker.py` | orrery | 0 | 0 | 5 | 0 | 5 |
| `apsidal_markers.py` | orrery | 3 | 1 | 0 | 0 | 4 |
| `coordinate_system_guide.py` | orrery | 2 | 2 | 0 | 0 | 4 |
| `sgr_a_visualization_core.py` | orrery | 1 | 3 | 0 | 0 | 4 |
| `maintenance_run.py` | orrery | 0 | 0 | 4 | 0 | 4 |
| `palomas_orrery_dashboard.py` | orrery | 0 | 0 | 4 | 0 | 4 |
| `skills_index.py` | dev_tools | 0 | 0 | 4 | 0 | 4 |
| `object_type_analyzer.py` | orrery | 3 | 0 | 0 | 0 | 3 |
| `scenarios_coral_bleaching.py` | earth_science | 1 | 2 | 0 | 0 | 3 |
| `visualization_3d.py` | stars | 0 | 3 | 0 | 0 | 3 |
| `dep_trace.py` | dev_tools | 0 | 0 | 3 | 0 | 3 |
| `ledger_index.py` | dev_tools | 0 | 0 | 3 | 0 | 3 |
| `measure_perframe_elements.py` | dev_tools | 0 | 0 | 3 | 0 | 3 |
| `module_atlas.py` | dev_tools | 0 | 0 | 3 | 0 | 3 |
| `palomas_orrery.py` | orrery | 0 | 0 | 3 | 0 | 3 |
| `provenance_history.py` | dev_tools | 0 | 0 | 3 | 0 | 3 |
| `exoplanet_systems.py` | stars | 0 | 0 | 3 | 0 | 3 |
| `energy_imbalance.py` | earth_science | 1 | 1 | 0 | 0 | 2 |
| `plot_data_report_widget.py` | utilities | 2 | 0 | 0 | 0 | 2 |
| `sgr_a_visualization_animation.py` | orrery | 1 | 0 | 1 | 0 | 2 |
| `close_approach_data.py` | orrery | 0 | 1 | 1 | 0 | 2 |
| `orbit_data_manager.py` | orrery | 0 | 0 | 2 | 0 | 2 |
| `worksheet_request_builder.py` | orrery | 0 | 0 | 2 | 0 | 2 |
| `orbital_elements.py` | orrery | 1 | 0 | 0 | 0 | 1 |
| `data_acquisition.py` | orrery | 1 | 0 | 0 | 0 | 1 |
| `exoplanet_orbits.py` | stars | 1 | 0 | 0 | 0 | 1 |
| `fetch_paleoclimate_data.py` | earth_science | 1 | 0 | 0 | 0 | 1 |
| `hr_diagram_distance.py` | stars | 1 | 0 | 0 | 0 | 1 |
| `messier_catalog.py` | stars | 1 | 0 | 0 | 0 | 1 |
| `orrery_rendering.py` | orrery | 1 | 0 | 0 | 0 | 1 |
| `planetarium_distance.py` | stars | 1 | 0 | 0 | 0 | 1 |
| `visualization_core.py` | stars | 1 | 0 | 0 | 0 | 1 |
| `visualization_utils.py` | stars | 1 | 0 | 0 | 0 | 1 |
| `patch_L212_2_records.py` | orrery | 0 | 1 | 0 | 0 | 1 |
| `add_docstrings.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |
| `data_inventory.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |
| `osculating_cache_manager.py` | orrery | 0 | 0 | 1 | 0 | 1 |
| `test_reset_completeness.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |
| `worksheet_keys.py` | orrery | 0 | 0 | 1 | 0 | 1 |
| `export_orbit_cache.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |

---

## Findings by File Type

Same data again, grouped by subject-matter domain rather than by individual file -- orrery, earth science, gallery, stars, utilities, dev tools. Domain is a report-only grouping (see MODULE_DOMAIN_MAP / classify_domain()); it does not affect which files get scanned or scored.

| Domain | Files | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Total |
|--------|------:|-------:|-------:|-------:|-------:|------:|
| Orrery (solar system + orbital mechanics) | 43 | 125 | 498 | 68 | 2 | 693 |
| Earth System | 13 | 150 | 81 | 2 | 0 | 233 |
| Stars (stellar neighborhood) | 11 | 12 | 42 | 6 | 0 | 60 |
| Dev Tools (audit, diagnostics, one-shot scripts) | 11 | 0 | 0 | 39 | 0 | 39 |
| Utilities (cross-domain shared helpers) | 1 | 2 | 0 | 0 | 0 | 2 |
| Gallery | 0 | 0 | 0 | 0 | 0 | 0 |

**Domain coverage gap:** the following files have findings but no entry in `MODULE_DOMAIN_MAP` -- defaulted to `orrery` rather than guessed into a more specific bucket. Add each to `MODULE_DOMAIN_MAP` in provenance_scanner.py with its real domain so this stops silently defaulting:

- `maintenance_run.py`
- `patch_L212_2_records.py`
- `worksheet_checker.py`
- `worksheet_keys.py`
- `worksheet_request_builder.py`

---

## ORPHAN ANNOTATIONS -- diagnostic, no scoring effect

Cross-check annotations that touch no claim's own statement. They granted no credit. A citation may be inherited from a section header; an annotation may not, because it names one checker who verified one value.

Each of these was written for something. Either it belongs on a specific value -- move it down and the credit follows -- or it was meant to cover a group, which this codebase does not express. Nothing here is safe to delete without reading the worksheet it names.

| File | Line | Annotation |
|------|-----:|------------|
| `constants_new.py` | 145 | # Cross-checked: Gemini 2026-08-02 -- Carroll & Ostlie (worksheet_gemini_constants_remaining.md) |
| `constants_new.py` | 146 | # Cross-checked: GPT 2026-08-02 -- NASA Sun Fact Sheet (constants_new_citation_verification_gpt.md) |
| `constants_new.py` | 318 | # Cross-checked: Claude 2026-08-02 -- IAU B3 / Archinal / JPL SSD (worksheet_claude_constants_new.md) |
| `constants_new.py` | 319 | # Cross-checked: GPT 2026-08-02 -- IAU B3 / Archinal / JPL SSD (constants_new_citation_verification_gpt.md) |

---

## CITATION LEVEL MISMATCH -- diagnostic, no scoring effect

Citations in this codebase attach to a block. The resolver reads exactly one block per string: the narrowest one containing it. A citation written one level further out is invisible to it. Nothing below is mis-scored today -- the flat 60-line context window catches these independently, which is exactly why the mismatch is easy to miss. Move a few lines and it becomes a real gap with no warning.

### Shadowed strings

The string sits in a block with no citation, inside a block that has one. Fix by repeating a short citation above the inner block's key, as done for `ring_params` -- not by loosening the resolver, which would clear the L-173 gaps by accident.

| File | Line | Shadowed from | Its citation at |
|------|-----:|---------------|----------------:|
| `comet_visualization_shells.py` | 94 | `HISTORICAL_TAIL_DATA` | 81 |
| `comet_visualization_shells.py` | 210 | `HISTORICAL_TAIL_DATA` | 81 |
| `comet_visualization_shells.py` | 236 | `HISTORICAL_TAIL_DATA` | 81 |
| `comet_visualization_shells.py` | 295 | `HISTORICAL_TAIL_DATA` | 81 |
| `comet_visualization_shells.py` | 306 | `HISTORICAL_TAIL_DATA` | 81 |
| `comet_visualization_shells.py` | 335 | `HISTORICAL_TAIL_DATA` | 81 |
| `planet_visualization_utilities.py` | 503 | `PLANET_ROTATION` | 494 |
| `planet_visualization_utilities.py` | 507 | `PLANET_ROTATION` | 494 |
| `planet_visualization_utilities.py` | 511 | `PLANET_ROTATION` | 494 |
| `planet_visualization_utilities.py` | 515 | `PLANET_ROTATION` | 494 |
| `planet_visualization_utilities.py` | 519 | `PLANET_ROTATION` | 494 |
| `planet_visualization_utilities.py` | 523 | `PLANET_ROTATION` | 494 |
| `planet_visualization_utilities.py` | 527 | `PLANET_ROTATION` | 494 |
| `planet_visualization_utilities.py` | 531 | `PLANET_ROTATION` | 494 |
| `planet_visualization_utilities.py` | 535 | `PLANET_ROTATION` | 494 |
| `planet_visualization_utilities.py` | 539 | `PLANET_ROTATION` | 494 |
| `planet_visualization_utilities.py` | 543 | `PLANET_ROTATION` | 494 |

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
| 454 | string | display string @ line 454 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### comet_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 46 | dict | COMET_NUCLEUS_SIZES[...] | (16 entries) | 4 | 5 | **20** | No source citation (recalled) | MEASURED -- independently catalogued fact (name) |
| 1603 | dict | COMET_FEATURE_THRESHOLDS[...] | (3 entries) | 4 | 5 | **20** | No source citation (recalled) | MEASURED -- independently catalogued fact (name) |
| 1182 | string | display string @ line 1182 | (5 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 2011 | string | display string @ line 2011 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### coordinate_system_guide.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 119 | string | display string @ line 119 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 152 | string | display string @ line 152 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### data_acquisition.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 202 | string | display string @ line 202 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### earth_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 702 | string | display string @ line 702 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

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
| 36 | string | display string @ line 36 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
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
| 124 | string | display string @ line 124 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 139 | string | display string @ line 139 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 167 | string | display string @ line 167 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 181 | string | display string @ line 181 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1406 | string | display string @ line 1406 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1465 | string | display string @ line 1465 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1476 | string | display string @ line 1476 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1589 | string | display string @ line 1589 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1709 | string | display string @ line 1709 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2385 | string | display string @ line 2385 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2408 | string | display string @ line 2408 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2431 | string | display string @ line 2431 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2453 | string | display string @ line 2453 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2468 | string | display string @ line 2468 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2479 | string | display string @ line 2479 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2512 | string | display string @ line 2512 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2810 | string | display string @ line 2810 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2932 | string | display string @ line 2932 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 3583 | string | display string @ line 3583 | (1 claim) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 3627 | string | display string @ line 3627 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 3757 | string | display string @ line 3757 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 3830 | string | display string @ line 3830 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4299 | string | display string @ line 4299 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4566 | string | display string @ line 4566 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4588 | string | display string @ line 4588 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4652 | string | display string @ line 4652 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4686 | string | display string @ line 4686 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 5816 | string | display string @ line 5816 | (1 claim) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 5912 | string | display string @ line 5912 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### info_dictionary.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 2159 | string | display string @ line 2159 | (7 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 2183 | string | display string @ line 2183 | (1 claim) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |

### mars_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 284 | string | display string @ line 284 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 298 | string | display string @ line 298 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 441 | string | display string @ line 441 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 454 | string | display string @ line 454 | (5 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

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
| 237 | string | display string @ line 237 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

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
| 550 | dict | ROTATION_AXIS_OMITTED[...] | (2 entries) | 4 | 5 | **20** | No source citation (recalled) | UNDETERMINED -- could not be classified |
| 454 | string | display string @ line 454 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 696 | string | display string @ line 696 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 698 | string | display string @ line 698 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

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
| 65 | constant | REFERENCE_YEAR | 2025.0 | 4 | 5 | **20** | No source citation (recalled) | UNDETERMINED -- could not be classified |
| 566 | string | display string @ line 566 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 578 | string | display string @ line 578 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 590 | string | display string @ line 590 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 602 | string | display string @ line 602 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 614 | string | display string @ line 614 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 624 | string | display string @ line 624 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 634 | string | display string @ line 634 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### sgr_a_star_data.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 55 | dict | B_STAR_TEMPERATURES[...] | (10 entries) | 4 | 5 | **20** | No source citation (recalled) | MEASURED -- independently catalogued fact (name) |
| 1 | string | display string @ line 1 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 234 | string | display string @ line 234 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 264 | string | display string @ line 264 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### sgr_a_visualization_animation.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 361 | string | display string @ line 361 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### sgr_a_visualization_core.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 384 | string | display string @ line 384 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### sgr_a_visualization_precession.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 301 | string | display string @ line 301 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 441 | string | display string @ line 441 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 442 | string | display string @ line 442 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### shell_configs.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 537 | string | display string @ line 537 | (5 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 558 | string | display string @ line 558 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 574 | string | display string @ line 574 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 588 | string | display string @ line 588 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 603 | string | display string @ line 603 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 621 | string | display string @ line 621 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 638 | string | display string @ line 638 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 668 | string | display string @ line 668 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 687 | string | display string @ line 687 | (10 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 729 | string | display string @ line 729 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 737 | string | display string @ line 737 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 763 | string | display string @ line 763 | (5 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 811 | string | display string @ line 811 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 818 | string | display string @ line 818 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 835 | string | display string @ line 835 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 847 | string | display string @ line 847 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 863 | string | display string @ line 863 | (1 claim) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 906 | string | display string @ line 906 | (7 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 915 | string | display string @ line 915 | (7 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 939 | string | display string @ line 939 | (2 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 945 | string | display string @ line 945 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 984 | string | display string @ line 984 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 992 | string | display string @ line 992 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1007 | string | display string @ line 1007 | (5 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1017 | string | display string @ line 1017 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1034 | string | display string @ line 1034 | (6 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1045 | string | display string @ line 1045 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1061 | string | display string @ line 1061 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1070 | string | display string @ line 1070 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1197 | string | display string @ line 1197 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1208 | string | display string @ line 1208 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1222 | string | display string @ line 1222 | (5 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1236 | string | display string @ line 1236 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1249 | string | display string @ line 1249 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2137 | string | display string @ line 2137 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### solar_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 913 | string | display string @ line 913 | (20 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 940 | string | display string @ line 940 | (20 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 964 | string | display string @ line 964 | (12 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |

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
| 181 | string | display string @ line 181 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 196 | string | display string @ line 196 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 414 | string | display string @ line 414 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### visualization_core.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 150 | string | display string @ line 150 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### visualization_utils.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 342 | string | display string @ line 342 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

---

## Tier 2: REVIEW (Score 10-15)

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
| 132 | string | display string @ line 132 | (7 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### celestial_coordinates.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 140 | dict | MAJOR_BODY_UNCERTAINTIES[...] | (206 entries) | 3 | 5 | **15** | Cited, not cross-checked; date-sensitive | MEASURED -- independently catalogued fact (key) |
| 387 | string | display string @ line 387 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### celestial_objects.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 47 | string | display string @ line 47 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 52 | string | display string @ line 52 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 60 | string | display string @ line 60 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
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
| 211 | string | display string @ line 211 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 235 | string | display string @ line 235 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 263 | string | display string @ line 263 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 271 | string | display string @ line 271 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 283 | string | display string @ line 283 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 294 | string | display string @ line 294 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 457 | string | display string @ line 457 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 511 | string | display string @ line 511 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 574 | string | display string @ line 574 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 631 | string | display string @ line 631 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 650 | string | display string @ line 650 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 658 | string | display string @ line 658 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
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
| 1129 | string | display string @ line 1129 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1136 | string | display string @ line 1136 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1143 | string | display string @ line 1143 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1149 | string | display string @ line 1149 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1155 | string | display string @ line 1155 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
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
| 1535 | dict | comet_visualization_info[...] | (6 entries) | 3 | 5 | **15** | Cited, not independently cross-checked | UNDETERMINED -- could not be classified |
| 94 | string | display string @ line 94 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 210 | string | display string @ line 210 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 236 | string | display string @ line 236 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 257 | string | display string @ line 257 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 284 | string | display string @ line 284 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 295 | string | display string @ line 295 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 306 | string | display string @ line 306 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 335 | string | display string @ line 335 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 524 | string | display string @ line 524 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 530 | string | display string @ line 530 | (9 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 537 | string | display string @ line 537 | (17 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 706 | string | display string @ line 706 | (14 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1356 | string | display string @ line 1356 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1537 | string | display string @ line 1537 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1547 | string | display string @ line 1547 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1557 | string | display string @ line 1557 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1566 | string | display string @ line 1566 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1575 | string | display string @ line 1575 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1585 | string | display string @ line 1585 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### constants_new.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 175 | constant | CHROMOSPHERE_PHYSICAL_KM | 2000.0 | 3 | 5 | **15** | Cited; cross-check incomplete (1/2 models) | MEASURED -- independently catalogued fact (name) |
| 247 | constant | INNER_LIMIT_OORT_CLOUD_AU | 2000 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 251 | constant | INNER_OORT_CLOUD_AU | 20000 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 255 | constant | OUTER_OORT_CLOUD_AU | 100000 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 259 | constant | GRAVITATIONAL_INFLUENCE_AU | 150000 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 330 | constant | MERCURY_RADIUS_KM | 2439.7 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 333 | constant | VENUS_RADIUS_KM | 6051.8 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 348 | constant | PHOBOS_RADIUS_KM | 11.1 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 366 | constant | PLUTO_RADIUS_KM | 1188.3 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 376 | constant | ERIS_RADIUS_KM | 1163 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 387 | constant | MAKEMAKE_RADIUS_KM | 715 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 425 | dict | KNOWN_ORBITAL_PERIODS[...] | (133 entries) | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1 | string | display string @ line 1 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 186 | constant | INNER_CORONA_RADII | 3 | 3 | 4 | **12** | Cited; cross-check incomplete (1/2 models) | RELATIONAL -- defined against a tracked base (name) |
| 191 | constant | OUTER_CORONA_RADII | 50 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 399 | dict | CENTER_BODY_RADII[...] | (1 entry) | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 54 | constant | KM_PER_AU | 149597870.7 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 62 | constant | SUN_RADIUS_KM | 695700.0 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 72 | constant | EARTH_EQUATORIAL_RADIUS_KM | 6378.137 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 80 | constant | EARTH_POLAR_RADIUS_KM | 6356.752 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 86 | constant | JUPITER_EQUATORIAL_RADIUS_KM | 71492.0 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 92 | constant | JUPITER_POLAR_RADIUS_KM | 66854.0 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 98 | constant | SPEED_OF_LIGHT_KM_S | 299792.458 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED (inferred from role 'data') |
| 230 | constant | TERMINATION_SHOCK_AU | 94 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 336 | constant | MOON_RADIUS_KM | 1737.4 | 2 | 5 | **10** | Cross-checked by 3 models (Claude, GPT, Gemini) | MEASURED -- independently catalogued fact (name) |
| 343 | constant | MARS_RADIUS_KM | 3396.2 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 351 | constant | SATURN_RADIUS_KM | 60268 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 356 | constant | URANUS_RADIUS_KM | 25559 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 361 | constant | NEPTUNE_RADIUS_KM | 24764 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 369 | constant | BENNU_RADIUS_KM | 0.246 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 379 | constant | HAUMEA_RADIUS_KM | 715 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 390 | constant | ARROKOTH_RADIUS_KM | 9.1 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |

### coordinate_system_guide.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 248 | string | display string @ line 248 | (10 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 537 | string | display string @ line 537 | (10 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### earth_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 56 | string | display string @ line 56 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 72 | string | display string @ line 72 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 128 | string | display string @ line 128 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 144 | string | display string @ line 144 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 200 | string | display string @ line 200 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 215 | string | display string @ line 215 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 270 | string | display string @ line 270 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 285 | string | display string @ line 285 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 340 | string | display string @ line 340 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 355 | string | display string @ line 355 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 493 | string | display string @ line 493 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 509 | string | display string @ line 509 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 565 | string | display string @ line 565 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 581 | string | display string @ line 581 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 638 | string | display string @ line 638 | (7 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 751 | string | display string @ line 751 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 789 | string | display string @ line 789 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 791 | string | display string @ line 791 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 871 | string | display string @ line 871 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 891 | string | display string @ line 891 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 947 | string | display string @ line 947 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 987 | string | display string @ line 987 | (6 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1001 | string | display string @ line 1001 | (7 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1058 | string | display string @ line 1058 | (7 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1098 | string | display string @ line 1098 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1121 | string | display string @ line 1121 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

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

### idealized_orbits.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1515 | string | display string @ line 1515 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1628 | string | display string @ line 1628 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1771 | string | display string @ line 1771 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1838 | string | display string @ line 1838 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2546 | string | display string @ line 2546 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2686 | string | display string @ line 2686 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2710 | string | display string @ line 2710 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2777 | string | display string @ line 2777 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2843 | string | display string @ line 2843 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 3044 | string | display string @ line 3044 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 3698 | string | display string @ line 3698 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 4404 | string | display string @ line 4404 | (12 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### info_dictionary.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 38 | string | display string @ line 38 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 171 | string | display string @ line 171 | (1 claim) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 286 | string | display string @ line 286 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 293 | string | display string @ line 293 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 300 | string | display string @ line 300 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 305 | string | display string @ line 305 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 343 | string | display string @ line 343 | (12 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 363 | string | display string @ line 363 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 383 | string | display string @ line 383 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 421 | string | display string @ line 421 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 440 | string | display string @ line 440 | (10 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 469 | string | display string @ line 469 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 492 | string | display string @ line 492 | (6 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 502 | string | display string @ line 502 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 518 | string | display string @ line 518 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 527 | string | display string @ line 527 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 535 | string | display string @ line 535 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 549 | string | display string @ line 549 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 560 | string | display string @ line 560 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 594 | string | display string @ line 594 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 608 | string | display string @ line 608 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 622 | string | display string @ line 622 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 630 | string | display string @ line 630 | (12 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
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
| 872 | string | display string @ line 872 | (12 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 901 | string | display string @ line 901 | (5 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 905 | string | display string @ line 905 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 908 | string | display string @ line 908 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 911 | string | display string @ line 911 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 914 | string | display string @ line 914 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 918 | string | display string @ line 918 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 923 | string | display string @ line 923 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 926 | string | display string @ line 926 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 930 | string | display string @ line 930 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 935 | string | display string @ line 935 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 939 | string | display string @ line 939 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 949 | string | display string @ line 949 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 953 | string | display string @ line 953 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 961 | string | display string @ line 961 | (6 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 969 | string | display string @ line 969 | (10 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1001 | string | display string @ line 1001 | (6 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1016 | string | display string @ line 1016 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1024 | string | display string @ line 1024 | (4 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1037 | string | display string @ line 1037 | (10 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1060 | string | display string @ line 1060 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1079 | string | display string @ line 1079 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1096 | string | display string @ line 1096 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1106 | string | display string @ line 1106 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1109 | string | display string @ line 1109 | (7 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1116 | string | display string @ line 1116 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1124 | string | display string @ line 1124 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1142 | string | display string @ line 1142 | (4 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1159 | string | display string @ line 1159 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1162 | string | display string @ line 1162 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1179 | string | display string @ line 1179 | (5 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1199 | string | display string @ line 1199 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1251 | string | display string @ line 1251 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1255 | string | display string @ line 1255 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1316 | string | display string @ line 1316 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1326 | string | display string @ line 1326 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1330 | string | display string @ line 1330 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1360 | string | display string @ line 1360 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1373 | string | display string @ line 1373 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1390 | string | display string @ line 1390 | (4 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1428 | string | display string @ line 1428 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1468 | string | display string @ line 1468 | (12 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1487 | string | display string @ line 1487 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1518 | string | display string @ line 1518 | (9 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1567 | string | display string @ line 1567 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1571 | string | display string @ line 1571 | (4 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1598 | string | display string @ line 1598 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1602 | string | display string @ line 1602 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1642 | string | display string @ line 1642 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1700 | string | display string @ line 1700 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1704 | string | display string @ line 1704 | (19 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1776 | string | display string @ line 1776 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1817 | string | display string @ line 1817 | (14 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1869 | string | display string @ line 1869 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1873 | string | display string @ line 1873 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1880 | string | display string @ line 1880 | (7 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1907 | string | display string @ line 1907 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1917 | string | display string @ line 1917 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1928 | string | display string @ line 1928 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1940 | string | display string @ line 1940 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1951 | string | display string @ line 1951 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1960 | string | display string @ line 1960 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2000 | string | display string @ line 2000 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2030 | string | display string @ line 2030 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2049 | string | display string @ line 2049 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2064 | string | display string @ line 2064 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2083 | string | display string @ line 2083 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2095 | string | display string @ line 2095 | (28 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2140 | string | display string @ line 2140 | (4 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
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
| 537 | string | display string @ line 537 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 649 | string | display string @ line 649 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 866 | string | display string @ line 866 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

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

### patch_L212_2_records.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 54 | dict | BASE[...] | (2 entries) | 3 | 5 | **15** | Cited, not independently cross-checked | UNDETERMINED -- could not be classified |

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
| 503 | string | display string @ line 503 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 507 | string | display string @ line 507 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 511 | string | display string @ line 511 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 515 | string | display string @ line 515 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 519 | string | display string @ line 519 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 523 | string | display string @ line 523 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 527 | string | display string @ line 527 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 531 | string | display string @ line 531 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 535 | string | display string @ line 535 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 539 | string | display string @ line 539 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 543 | string | display string @ line 543 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 703 | string | display string @ line 703 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 707 | string | display string @ line 707 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 715 | string | display string @ line 715 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 723 | string | display string @ line 723 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

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

### sgr_a_visualization_core.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 154 | string | display string @ line 154 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 262 | string | display string @ line 262 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 331 | string | display string @ line 331 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### shell_configs.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 108 | string | display string @ line 108 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 113 | string | display string @ line 113 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 128 | string | display string @ line 128 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 132 | string | display string @ line 132 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 146 | string | display string @ line 146 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 150 | string | display string @ line 150 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 168 | string | display string @ line 168 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 173 | string | display string @ line 173 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 186 | string | display string @ line 186 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 230 | string | display string @ line 230 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 263 | string | display string @ line 263 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 269 | string | display string @ line 269 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 283 | string | display string @ line 283 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 293 | string | display string @ line 293 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 311 | string | display string @ line 311 | (9 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 332 | string | display string @ line 332 | (1 claim) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 350 | string | display string @ line 350 | (4 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 370 | string | display string @ line 370 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 385 | string | display string @ line 385 | (1 claim) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 417 | string | display string @ line 417 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 423 | string | display string @ line 423 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 452 | string | display string @ line 452 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 478 | string | display string @ line 478 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 495 | string | display string @ line 495 | (9 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 514 | string | display string @ line 514 | (3 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1261 | string | display string @ line 1261 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1282 | string | display string @ line 1282 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1305 | string | display string @ line 1305 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1330 | string | display string @ line 1330 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1337 | string | display string @ line 1337 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1354 | string | display string @ line 1354 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1361 | string | display string @ line 1361 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1378 | string | display string @ line 1378 | (5 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1384 | string | display string @ line 1384 | (5 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1400 | string | display string @ line 1400 | (5 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1406 | string | display string @ line 1406 | (5 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1421 | string | display string @ line 1421 | (6 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1429 | string | display string @ line 1429 | (6 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1444 | string | display string @ line 1444 | (11 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1451 | string | display string @ line 1451 | (11 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1467 | string | display string @ line 1467 | (4 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1474 | string | display string @ line 1474 | (4 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1490 | string | display string @ line 1490 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1499 | string | display string @ line 1499 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1523 | string | display string @ line 1523 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1529 | string | display string @ line 1529 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1545 | string | display string @ line 1545 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1551 | string | display string @ line 1551 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1566 | string | display string @ line 1566 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1573 | string | display string @ line 1573 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1589 | string | display string @ line 1589 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1598 | string | display string @ line 1598 | (3 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1616 | string | display string @ line 1616 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1623 | string | display string @ line 1623 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1640 | string | display string @ line 1640 | (4 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1650 | string | display string @ line 1650 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1920 | string | display string @ line 1920 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2123 | string | display string @ line 2123 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2153 | string | display string @ line 2153 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2186 | string | display string @ line 2186 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2223 | string | display string @ line 2223 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2261 | string | display string @ line 2261 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2277 | string | display string @ line 2277 | (7 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2296 | string | display string @ line 2296 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2319 | string | display string @ line 2319 | (6 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2361 | string | display string @ line 2361 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2377 | string | display string @ line 2377 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2392 | string | display string @ line 2392 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2405 | string | display string @ line 2405 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 2421 | string | display string @ line 2421 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2462 | string | display string @ line 2462 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2478 | string | display string @ line 2478 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2496 | string | display string @ line 2496 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2510 | string | display string @ line 2510 | (1 claim) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 2527 | string | display string @ line 2527 | (10 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2578 | string | display string @ line 2578 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2594 | string | display string @ line 2594 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2625 | string | display string @ line 2625 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2668 | string | display string @ line 2668 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2684 | string | display string @ line 2684 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2718 | string | display string @ line 2718 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### solar_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 97 | string | display string @ line 97 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 123 | string | display string @ line 123 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 141 | string | display string @ line 141 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 156 | string | display string @ line 156 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 171 | string | display string @ line 171 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 196 | string | display string @ line 196 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 225 | string | display string @ line 225 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 250 | string | display string @ line 250 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 283 | string | display string @ line 283 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 297 | string | display string @ line 297 | (9 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 317 | string | display string @ line 317 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 354 | string | display string @ line 354 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 377 | string | display string @ line 377 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 383 | string | display string @ line 383 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 416 | string | display string @ line 416 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 445 | string | display string @ line 445 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 480 | string | display string @ line 480 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 595 | string | display string @ line 595 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 617 | string | display string @ line 617 | (9 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 660 | string | display string @ line 660 | (18 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 689 | string | display string @ line 689 | (14 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 715 | string | display string @ line 715 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 743 | string | display string @ line 743 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 766 | string | display string @ line 766 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

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
| 46 | constant | OBLIQUITY_DEG | 23.4393 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 79 | string | display string @ line 79 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

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
| 356 | string | display string @ line 356 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 638 | string | display string @ line 638 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 707 | string | display string @ line 707 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### visualization_3d.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 725 | string | display string @ line 725 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 748 | string | display string @ line 748 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 785 | string | display string @ line 785 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

---

## Tier 3: LOW PRIORITY (Score 5-9)

### add_docstrings.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 118 | dict | DOCSTRINGS[...] | (42 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### close_approach_data.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 68 | dict | CAD_BODY_NAMES[...] | (11 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal use (name vocabulary) |

### constants_new.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 197 | constant | STREAMER_BELT_RADII | 6.0 | 2 | 4 | **8** | Cross-checked by 2 models (Gemini, GPT) | RELATIONAL -- defined against a tracked base (name) |
| 205 | constant | ROCHE_LIMIT_RADII | 3.45 | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | RELATIONAL -- defined against a tracked base (name) |
| 215 | constant | ALFVEN_SURFACE_RADII | 18.8 | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | RELATIONAL -- defined against a tracked base (name) |
| 237 | constant | HELIOPAUSE_RADII | 26148 | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | RELATIONAL -- defined against a tracked base (name) |
| 279 | constant | PARKER_CLOSEST_RADII | 9.86 | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | RELATIONAL -- defined against a tracked base (name) |

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

### maintenance_run.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 154 | constant | TOOL_TIMEOUT_SECONDS | 900 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 217 | constant | HASH_LIMIT_BYTES | 2 * 1024 * 1024 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 336 | constant | NOTE_WIDTH | 44 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 337 | constant | NOTE_INDENT | 37 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### mars_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 518 | string | display string @ line 518 | (1 claim) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 599 | string | display string @ line 599 | (3 claims) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 713 | string | display string @ line 713 | (2 claims) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 850 | string | display string @ line 850 | (3 claims) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |

### measure_perframe_elements.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 41 | constant | KB | 1000.0 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 42 | constant | FRAMES_29 | 29 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 43 | constant | FRAMES_60 | 60 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

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
| 103 | dict | ROLE_MAP[...] | (124 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 368 | dict | ROLE_DESCRIPTIONS[...] | (13 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 391 | dict | ROLE_SECTION_TITLES[...] | (13 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

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
| 39 | constant | DEFAULT_DAYS_AHEAD | 730 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'cache') |
| 40 | constant | MAX_DATA_AGE_DAYS | 90 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'cache') |

### osculating_cache_manager.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 82 | dict | REFRESH_INTERVALS[...] | (14 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'cache') |

### palomas_orrery.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 2079 | constant | PERFRAME_INDICATOR_RADIUS_FACTOR | 100.0 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |
| 2112 | constant | PERFRAME_COORD_DECIMALS | 7 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |
| 3687 | constant | BUTTON_WIDTH | 14 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |

### palomas_orrery_dashboard.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 66 | constant | WINDOW_WIDTH | 960 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |
| 67 | constant | WINDOW_HEIGHT | 720 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |
| 478 | constant | TOOLTIP_DELAY_MS | 400 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |
| 609 | dict | SECTION_SYMBOLS[...] | (4 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'gui') |

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

### provenance_history.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 45 | constant | SCHEMA_VERSION | 1 | 4 | 2 | **8** | No source citation; date-sensitive (recalled) | Internal (role 'devtool') |
| 50 | constant | MAX_RUNS | 6 | 4 | 2 | **8** | No source citation; date-sensitive (recalled) | Internal (role 'devtool') |
| 56 | constant | EXPECTED_CADENCE_DAYS | 1 | 4 | 2 | **8** | No source citation; date-sensitive (recalled) | Internal (role 'devtool') |

### provenance_scanner.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 327 | constant | V_FETCHED | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 328 | constant | V_CROSS_CHECKED | 2 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 337 | constant | V_SOURCED | 3 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 340 | constant | V_RECALLED | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 349 | constant | C_COSMETIC | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 350 | constant | C_INTERNAL | 2 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 351 | constant | C_LOADBEARING | 3 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 352 | constant | C_PUBLIC | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 353 | constant | C_PROPAGATING | 5 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 358 | constant | C_RELATIONAL | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 359 | constant | C_MEASURED | 5 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 364 | constant | C_UNDETERMINED | 5 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 465 | dict | DOMAIN_LABELS[...] | (6 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 474 | dict | MODULE_DOMAIN_MAP[...] | (101 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 1104 | constant | CITATION_LOOKBACK_BLOCK | 15 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |
| 1980 | constant | SHADOW_DERIVED_MIN_MAGNITUDE | 100.0 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |

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

### venus_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 43 | string | display string @ line 43 | (2 claims) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 62 | string | display string @ line 62 | (2 claims) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 339 | string | display string @ line 339 | (3 claims) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 437 | string | display string @ line 437 | (15 claims) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 528 | string | display string @ line 528 | (1 claim) | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | Public-facing display string (hover/INFO) |
| 681 | string | display string @ line 681 | (2 claims) | 2 | 4 | **8** | Cross-checked by 2 models (GPT, Claude) | Public-facing display string (hover/INFO) |

### worksheet_checker.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 419 | constant | HASH_CHARS | 8 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 651 | constant | MIN_PROSE_FRAGMENT | 24 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 842 | constant | QUOTE_LIMIT | 160 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 1001 | constant | INSTRUCTION_LOOKBACK | 30 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 1002 | constant | INSTRUCTION_LOOKAHEAD | 25 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### worksheet_keys.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 138 | constant | EXTRACTOR_VERSION | 2 | 4 | 2 | **8** | No source citation (recalled) | Internal use (name vocabulary) |

### worksheet_request_builder.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 123 | constant | CLAIM_EXCERPT | 90 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 316 | constant | HASH_CHARS | 8 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

---

## Tier 4: LOWEST PRIORITY (Score 1-4)

### constants_new.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 134 | constant | DEFAULT_MARKER_SIZE | 7 | 3 | 1 | **3** | Cited, not independently cross-checked | Cosmetic (name vocabulary) |
| 136 | constant | CENTER_MARKER_SIZE | 10 | 3 | 1 | **3** | Cited, not independently cross-checked | Cosmetic (name vocabulary) |

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
