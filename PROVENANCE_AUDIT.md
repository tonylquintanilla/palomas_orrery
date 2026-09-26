<!-- Doc-Kind: generated | The provenance audit: every numeric claim scored against its citation, rebuilt by provenance_scanner.py on each run. Do not hand-edit. -->
# Paloma's Orrery -- Provenance Audit

Generated: September 25, 2026
Files scanned: 140
Total findings: 1083
Constants: 161 | Dicts: 44 | Display strings: 878

Unit of provenance: the smallest thing with a coherent source citation. A dict with one block-level `# Source:` comment is ONE unit; all its entries inherit that citation. A hover string with co-referring numbers is ONE unit.

**Color values are excluded from this audit.** RGB/color fields are never scored as claims (see _make_dict_unit), and a dict's block `# Source:` citation should never be read as covering that dict's `color` field(s), even when it covers everything else in the same unit. This does not mean color choices have no basis at all -- some are loosely informed by real imagery or composition data -- but color selection across this codebase is inconsistent in method: sometimes evidence-informed, sometimes chosen purely for visual contrast or distinction, sometimes arbitrary. Treat every color value as a developer/AI judgment call, not a measured or verified quantity, regardless of what citation sits nearby. (Tony's call, July 16, 2026; a low-priority wishlist item for a real, systematic color-accuracy pass is tracked at LEDGER_CONSOLIDATED.md L-124.)

---

## Run History

The last 6 recorded scanner runs, newest first. Written by provenance_history.py and tracked in git: when an audit was taken, and against which commit, is itself provenance.

A run is expected every 1 day(s). Nothing here affects the exit code -- the delta informs the push call, it does not make it.

| Run (UTC) | HEAD | Files | Total | T1 | T2 | T3 | T4 |
|-----------|------|------:|------:|---:|---:|---:|---:|
| 20260926T012448Z | `62e9385` | 140 | 1083 | 295 | 668 | 118 | 2 |
| 20260925T023903Z | `fb8d927` | 140 | 1080 | 295 | 665 | 118 | 2 |
| 20260924T174742Z | `50343e0` | 141 | 1080 | 295 | 665 | 118 | 2 |
| 20260924T034040Z | `0ab14d8` | 140 | 1081 | 293 | 668 | 118 | 2 |
| 20260924T013317Z | `8fffbe1` | 139 | 1081 | 293 | 668 | 118 | 2 |
| 20260924T012434Z | `bba2145` | 138 | 1076 | 293 | 663 | 118 | 2 |

Change since the previous run: total +3, Tier-1 +0.

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
| 1 | 16-20 | FIX NOW | 295 |
| 2 | 10-15 | REVIEW | 668 |
| 3 | 5-9 | LOW PRIORITY | 118 |
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
| `info_dictionary.py` | orrery | 2 | 125 | 2 | 0 | 129 |
| `shell_configs.py` | orrery | 35 | 76 | 0 | 0 | 111 |
| `constants_new.py` | orrery | 4 | 87 | 3 | 2 | 96 |
| `paleoclimate_wet_bulb_full.py` | earth_science | 44 | 22 | 0 | 0 | 66 |
| `celestial_objects.py` | orrery | 0 | 51 | 0 | 0 | 51 |
| `paleoclimate_human_origins_full.py` | earth_science | 40 | 6 | 0 | 0 | 46 |
| `idealized_orbits.py` | orrery | 29 | 12 | 0 | 0 | 41 |
| `star_notes.py` | stars | 1 | 37 | 0 | 0 | 38 |
| `solar_visualization_shells.py` | orrery | 6 | 29 | 0 | 0 | 35 |
| `paleoclimate_visualization_full.py` | earth_science | 28 | 6 | 0 | 0 | 34 |
| `neptune_visualization_shells.py` | orrery | 0 | 28 | 0 | 0 | 28 |
| `comet_visualization_shells.py` | orrery | 4 | 22 | 0 | 0 | 26 |
| `uranus_visualization_shells.py` | orrery | 1 | 24 | 0 | 0 | 25 |
| `earth_visualization_shells.py` | earth_science | 0 | 20 | 0 | 0 | 20 |
| `jupiter_visualization_shells.py` | orrery | 0 | 19 | 0 | 0 | 19 |
| `planet_visualization_utilities.py` | orrery | 4 | 12 | 1 | 0 | 17 |
| `provenance_scanner.py` | dev_tools | 0 | 0 | 16 | 0 | 16 |
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
| `asteroid_belt_visualization_shells.py` | orrery | 0 | 7 | 0 | 0 | 7 |
| `spacecraft_encounters.py` | orrery | 0 | 7 | 0 | 0 | 7 |
| `sgr_a_star_data.py` | orrery | 3 | 3 | 0 | 0 | 6 |
| `celestial_coordinates.py` | orrery | 4 | 2 | 0 | 0 | 6 |
| `paleoclimate_visualization.py` | earth_science | 6 | 0 | 0 | 0 | 6 |
| `exoplanet_coordinates.py` | stars | 5 | 0 | 0 | 0 | 5 |
| `earth_pole_of_date.py` | orrery | 0 | 5 | 0 | 0 | 5 |
| `star_sphere_builder.py` | stars | 0 | 2 | 3 | 0 | 5 |
| `fetch_climate_data.py` | earth_science | 0 | 5 | 0 | 0 | 5 |
| `planet9_visualization_shells.py` | orrery | 0 | 5 | 0 | 0 | 5 |
| `worksheet_checker.py` | orrery | 0 | 0 | 5 | 0 | 5 |
| `apsidal_markers.py` | orrery | 3 | 1 | 0 | 0 | 4 |
| `coordinate_system_guide.py` | orrery | 2 | 2 | 0 | 0 | 4 |
| `sgr_a_visualization_precession.py` | orrery | 4 | 0 | 0 | 0 | 4 |
| `orrery_maintenance_run.py` | orrery | 0 | 0 | 4 | 0 | 4 |
| `palomas_orrery_dashboard.py` | orrery | 0 | 0 | 4 | 0 | 4 |
| `skills_index.py` | dev_tools | 0 | 0 | 4 | 0 | 4 |
| `object_type_analyzer.py` | orrery | 3 | 0 | 0 | 0 | 3 |
| `orrery_rendering.py` | orrery | 2 | 1 | 0 | 0 | 3 |
| `scenarios_coral_bleaching.py` | earth_science | 1 | 2 | 0 | 0 | 3 |
| `sgr_a_visualization_core.py` | orrery | 1 | 2 | 0 | 0 | 3 |
| `visualization_3d.py` | stars | 0 | 3 | 0 | 0 | 3 |
| `dep_trace.py` | dev_tools | 0 | 0 | 3 | 0 | 3 |
| `doc_index.py` | orrery | 0 | 0 | 3 | 0 | 3 |
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
| `planetarium_distance.py` | stars | 1 | 0 | 0 | 0 | 1 |
| `visualization_core.py` | stars | 1 | 0 | 0 | 0 | 1 |
| `visualization_utils.py` | stars | 1 | 0 | 0 | 0 | 1 |
| `earth_pole_live_check.py` | orrery | 0 | 1 | 0 | 0 | 1 |
| `add_docstrings.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |
| `data_inventory.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |
| `export_constants.py` | orrery | 0 | 0 | 1 | 0 | 1 |
| `osculating_cache_manager.py` | orrery | 0 | 0 | 1 | 0 | 1 |
| `test_dimensions.py` | orrery | 0 | 0 | 1 | 0 | 1 |
| `test_reset_completeness.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |
| `worksheet_key_aliases.py` | orrery | 0 | 0 | 1 | 0 | 1 |
| `worksheet_keys.py` | orrery | 0 | 0 | 1 | 0 | 1 |
| `export_orbit_cache.py` | dev_tools | 0 | 0 | 1 | 0 | 1 |

---

## Findings by File Type

Same data again, grouped by subject-matter domain rather than by individual file -- orrery, earth science, gallery, stars, utilities, dev tools. Domain is a report-only grouping (see MODULE_DOMAIN_MAP / classify_domain()); it does not affect which files get scanned or scored.

| Domain | Files | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Total |
|--------|------:|-------:|-------:|-------:|-------:|------:|
| Orrery (solar system + orbital mechanics) | 48 | 132 | 551 | 71 | 2 | 756 |
| Earth System | 13 | 149 | 75 | 2 | 0 | 226 |
| Stars (stellar neighborhood) | 11 | 12 | 42 | 6 | 0 | 60 |
| Dev Tools (audit, diagnostics, one-shot scripts) | 11 | 0 | 0 | 39 | 0 | 39 |
| Utilities (cross-domain shared helpers) | 1 | 2 | 0 | 0 | 0 | 2 |
| Gallery | 0 | 0 | 0 | 0 | 0 | 0 |

**Domain coverage gap:** the following files have findings but no entry in `MODULE_DOMAIN_MAP` -- defaulted to `orrery` rather than guessed into a more specific bucket. Add each to `MODULE_DOMAIN_MAP` in provenance_scanner.py with its real domain so this stops silently defaulting:

- `doc_index.py`
- `earth_pole_live_check.py`
- `earth_pole_of_date.py`
- `export_constants.py`
- `orrery_maintenance_run.py`
- `test_dimensions.py`
- `worksheet_checker.py`
- `worksheet_key_aliases.py`
- `worksheet_keys.py`
- `worksheet_request_builder.py`

---

## CROSS-CHECK ANNOTATION ISSUES -- diagnostic, no scoring effect

Annotation lines the scanner saw but could not use. None of these changed a score. They are listed because an annotation that quietly does nothing is worse than one that is visibly wrong -- it reads as a completed cross-check to anyone skimming the source.

A qualifying annotation needs an ISO date and, after it, a parenthetical worksheet reference ending in `.md`, `.jsonl` or `.json`. Two of them, naming different checkers, on a claim that already has a citation, are what earns V2.

`Near line` is the first claim that saw the annotation, not the annotation's own line. The annotation sits within the citation lookback above it.

| File | Near line | Issue | Detail |
|------|----------:|-------|--------|
| `constants_new.py` | 217 | `unsourced_annotation` | annotation present, but the claim carries no citation |

---

## ORPHAN ANNOTATIONS -- diagnostic, no scoring effect

Cross-check annotations that touch no claim's own statement. They granted no credit. A citation may be inherited from a section header; an annotation may not, because it names one checker who verified one value.

Each of these was written for something. Either it belongs on a specific value -- move it down and the credit follows -- or it was meant to cover a group, which this codebase does not express. Nothing here is safe to delete without reading the worksheet it names.

| File | Line | Annotation |
|------|-----:|------------|
| `constants_new.py` | 1700 | # Cross-checked: Gemini 2026-08-02 -- Carroll & Ostlie (worksheet_gemini_constants_remaining.md) |
| `constants_new.py` | 1701 | # Cross-checked: GPT 2026-08-02 -- NASA Sun Fact Sheet (constants_new_citation_verification_gpt.md) |
| `constants_new.py` | 1992 | # Cross-checked: Claude 2026-08-02 -- IAU B3 / Archinal / JPL SSD (worksheet_claude_constants_new.md) |
| `constants_new.py` | 1993 | # Cross-checked: GPT 2026-08-02 -- IAU B3 / Archinal / JPL SSD (constants_new_citation_verification_gpt.md) |

---

## CITATION LEVEL MISMATCH -- diagnostic, no scoring effect

Citations in this codebase attach to a block. The resolver reads exactly one block per string: the narrowest one containing it. A citation written one level further out is invisible to it. Nothing below is mis-scored today -- the flat 60-line context window catches these independently, which is exactly why the mismatch is easy to miss. Move a few lines and it becomes a real gap with no warning.

### Shadowed strings

The string sits in a block with no citation, inside a block that has one. Fix by repeating a short citation above the inner block's key, as done for `ring_params` -- not by loosening the resolver, which would clear the L-173 gaps by accident.

| File | Line | Shadowed from | Its citation at |
|------|-----:|---------------|----------------:|
| `comet_visualization_shells.py` | 95 | `HISTORICAL_TAIL_DATA` | 82 |
| `comet_visualization_shells.py` | 211 | `HISTORICAL_TAIL_DATA` | 82 |
| `comet_visualization_shells.py` | 237 | `HISTORICAL_TAIL_DATA` | 82 |
| `comet_visualization_shells.py` | 296 | `HISTORICAL_TAIL_DATA` | 82 |
| `comet_visualization_shells.py` | 307 | `HISTORICAL_TAIL_DATA` | 82 |
| `comet_visualization_shells.py` | 336 | `HISTORICAL_TAIL_DATA` | 82 |
| `planet_visualization_utilities.py` | 539 | `PLANET_ROTATION` | 530 |
| `planet_visualization_utilities.py` | 543 | `PLANET_ROTATION` | 530 |
| `planet_visualization_utilities.py` | 547 | `PLANET_ROTATION` | 530 |
| `planet_visualization_utilities.py` | 562 | `PLANET_ROTATION` | 530 |
| `planet_visualization_utilities.py` | 566 | `PLANET_ROTATION` | 530 |
| `planet_visualization_utilities.py` | 570 | `PLANET_ROTATION` | 530 |
| `planet_visualization_utilities.py` | 574 | `PLANET_ROTATION` | 530 |
| `planet_visualization_utilities.py` | 578 | `PLANET_ROTATION` | 530 |
| `planet_visualization_utilities.py` | 582 | `PLANET_ROTATION` | 530 |
| `planet_visualization_utilities.py` | 586 | `PLANET_ROTATION` | 530 |

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
| 47 | dict | COMET_NUCLEUS_SIZES[...] | (16 entries) | 4 | 5 | **20** | No source citation (recalled) | MEASURED -- independently catalogued fact (name) |
| 1625 | dict | COMET_FEATURE_THRESHOLDS[...] | (3 entries) | 4 | 5 | **20** | No source citation (recalled) | MEASURED -- independently catalogued fact (name) |
| 1204 | string | display string @ line 1204 | (5 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 2033 | string | display string @ line 2033 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### constants_new.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 217 | constant | EARTH_MEAN_RADIUS_KM | 6371.0 | 4 | 5 | **20** | No source citation (recalled) | MEASURED -- independently catalogued fact (name) |
| 1071 | constant | EARTH_SOLAR_WIND_PRESSURE_NPA | 2.0 | 4 | 5 | **20** | No source citation (recalled) | MEASURED -- independently catalogued fact (name) |
| 1087 | constant | EARTH_SOLAR_WIND_BZ_NT | 0.0 | 4 | 5 | **20** | No source citation (recalled) | MEASURED (inferred from role 'data') |
| 1097 | constant | EARTH_SOLAR_WIND_SPEED_KM_S | 400.0 | 4 | 5 | **20** | No source citation (recalled) | MEASURED (inferred from role 'data') |

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
| 119 | string | display string @ line 119 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 134 | string | display string @ line 134 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 162 | string | display string @ line 162 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 176 | string | display string @ line 176 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1401 | string | display string @ line 1401 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1460 | string | display string @ line 1460 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1471 | string | display string @ line 1471 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1584 | string | display string @ line 1584 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1704 | string | display string @ line 1704 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2380 | string | display string @ line 2380 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2403 | string | display string @ line 2403 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2426 | string | display string @ line 2426 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2448 | string | display string @ line 2448 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2463 | string | display string @ line 2463 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2474 | string | display string @ line 2474 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2507 | string | display string @ line 2507 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2805 | string | display string @ line 2805 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2927 | string | display string @ line 2927 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 3590 | string | display string @ line 3590 | (1 claim) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 3634 | string | display string @ line 3634 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 3764 | string | display string @ line 3764 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 3837 | string | display string @ line 3837 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4306 | string | display string @ line 4306 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4573 | string | display string @ line 4573 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4595 | string | display string @ line 4595 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4659 | string | display string @ line 4659 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4693 | string | display string @ line 4693 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 5823 | string | display string @ line 5823 | (1 claim) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 5919 | string | display string @ line 5919 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### info_dictionary.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 2162 | string | display string @ line 2162 | (7 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 2186 | string | display string @ line 2186 | (1 claim) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |

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
| 593 | dict | ROTATION_AXIS_OMITTED[...] | (2 entries) | 4 | 5 | **20** | No source citation (recalled) | UNDETERMINED -- could not be classified |
| 490 | string | display string @ line 490 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 782 | string | display string @ line 782 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 784 | string | display string @ line 784 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

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
| 595 | string | display string @ line 595 | (5 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 616 | string | display string @ line 616 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 632 | string | display string @ line 632 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 646 | string | display string @ line 646 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 661 | string | display string @ line 661 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 679 | string | display string @ line 679 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 696 | string | display string @ line 696 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 726 | string | display string @ line 726 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 745 | string | display string @ line 745 | (10 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 787 | string | display string @ line 787 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 795 | string | display string @ line 795 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 821 | string | display string @ line 821 | (5 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 869 | string | display string @ line 869 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 876 | string | display string @ line 876 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 893 | string | display string @ line 893 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 905 | string | display string @ line 905 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 921 | string | display string @ line 921 | (1 claim) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 964 | string | display string @ line 964 | (7 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 973 | string | display string @ line 973 | (7 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 997 | string | display string @ line 997 | (2 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 1003 | string | display string @ line 1003 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1042 | string | display string @ line 1042 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1050 | string | display string @ line 1050 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1065 | string | display string @ line 1065 | (5 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1075 | string | display string @ line 1075 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1092 | string | display string @ line 1092 | (6 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1103 | string | display string @ line 1103 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1119 | string | display string @ line 1119 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1128 | string | display string @ line 1128 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1255 | string | display string @ line 1255 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1266 | string | display string @ line 1266 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1280 | string | display string @ line 1280 | (5 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1294 | string | display string @ line 1294 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1307 | string | display string @ line 1307 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2169 | string | display string @ line 2169 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### solar_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 938 | string | display string @ line 938 | (4 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 943 | string | display string @ line 943 | (4 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 952 | string | display string @ line 952 | (9 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 965 | string | display string @ line 965 | (4 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 979 | string | display string @ line 979 | (9 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |
| 989 | string | display string @ line 989 | (12 claims) | 4 | 4 | **16** | No source citation; date-sensitive (recalled) | Public-facing display string (hover/INFO) |

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
| 343 | string | display string @ line 343 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

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
| 1557 | dict | comet_visualization_info[...] | (6 entries) | 3 | 5 | **15** | Cited, not independently cross-checked | UNDETERMINED -- could not be classified |
| 95 | string | display string @ line 95 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 211 | string | display string @ line 211 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 237 | string | display string @ line 237 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 258 | string | display string @ line 258 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 285 | string | display string @ line 285 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 296 | string | display string @ line 296 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 307 | string | display string @ line 307 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 336 | string | display string @ line 336 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 539 | string | display string @ line 539 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 548 | string | display string @ line 548 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 557 | string | display string @ line 557 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 558 | string | display string @ line 558 | (17 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 727 | string | display string @ line 727 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 731 | string | display string @ line 731 | (9 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1378 | string | display string @ line 1378 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1559 | string | display string @ line 1559 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1569 | string | display string @ line 1569 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1579 | string | display string @ line 1579 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1588 | string | display string @ line 1588 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1597 | string | display string @ line 1597 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1607 | string | display string @ line 1607 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### constants_new.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 239 | constant | EARTH_INNER_CORE_KM | 1221.5 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 258 | constant | EARTH_OUTER_CORE_KM | 3480.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 286 | constant | EARTH_D660_DEPTH_KM | 660.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 336 | constant | EARTH_UPPER_MANTLE_KM | 6346.6 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 366 | constant | EARTH_GM_KM3_S2 | 398600.4418 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 384 | constant | EARTH_ROTATION_RATE_RAD_S | 7.292115e-05 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 426 | constant | S_PER_HOUR | 3600.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 458 | constant | EARTH_POLE_RA_J2000_DEG | 0.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 488 | constant | EARTH_POLE_DEC_J2000_DEG | 90.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 500 | constant | ARCSEC_PER_DEG | 3600.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 514 | constant | EARTH_OBLIQUITY_J2000_ARCSEC | 84381.448 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 581 | constant | EARTH_LEO_UPPER_ALTITUDE_KM | 2000.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 604 | constant | EARTH_LEO_LOWER_ALTITUDE_KM | 200.0 | 3 | 5 | **15** | Cited, not cross-checked; date-sensitive | MEASURED -- independently catalogued fact (name) |
| 642 | constant | EARTH_STRATOPAUSE_ALTITUDE_KM | 50.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 654 | constant | EARTH_THERMOPAUSE_ALTITUDE_KM | 600.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 723 | constant | EARTH_VAN_ALLEN_OUTER_BAND_LOW_L | 4.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 748 | constant | EARTH_VAN_ALLEN_OUTER_BAND_HIGH_L | 5.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 803 | constant | EARTH_VAN_ALLEN_INNER_BELT_INNER_EDGE | 1.1 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 828 | constant | EARTH_VAN_ALLEN_INNER_BELT_OUTER_EDGE | 2.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 846 | constant | EARTH_VAN_ALLEN_OUTER_BELT_INNER_EDGE | 3.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 871 | constant | EARTH_VAN_ALLEN_OUTER_BELT_OUTER_EDGE | 7.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 936 | constant | EARTH_IGRF13_G10_NT | -29404.8 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 954 | constant | EARTH_IGRF13_G11_NT | -1450.9 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 966 | constant | EARTH_IGRF13_H11_NT | 4652.5 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 978 | constant | EARTH_IGRF13_G10_SV_NT_PER_YEAR | 5.7 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 991 | constant | EARTH_IGRF13_G11_SV_NT_PER_YEAR | 7.4 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 1004 | constant | EARTH_IGRF13_H11_SV_NT_PER_YEAR | -25.9 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 1138 | constant | EARTH_MAGNETOPAUSE_SHUE_A3_PER_NT | 0.184 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 1148 | constant | EARTH_MAGNETOPAUSE_SHUE_A4_NT | 8.14 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 1158 | constant | EARTH_MAGNETOPAUSE_SHUE_A5 | 6.6 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 1173 | constant | EARTH_MAGNETOPAUSE_SHUE_A6 | 0.58 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 1186 | constant | EARTH_MAGNETOPAUSE_SHUE_A7_PER_NT | -0.007 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 1197 | constant | EARTH_MAGNETOPAUSE_SHUE_A8 | 0.024 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 1209 | constant | EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG | 120.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1261 | constant | EARTH_BOW_SHOCK_JELINEK_EPS | 6.55 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 1270 | constant | EARTH_BOW_SHOCK_JELINEK_LAMBDA | 1.17 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 1284 | constant | EARTH_BOW_SHOCK_CUT_ANGLE_DEG | 105.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1754 | constant | CHROMOSPHERE_PHYSICAL_KM | 2000.0 | 3 | 5 | **15** | Cited; cross-check incomplete (1/2 models) | MEASURED -- independently catalogued fact (name) |
| 1921 | constant | INNER_LIMIT_OORT_CLOUD_AU | 2000 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1925 | constant | INNER_OORT_CLOUD_AU | 20000 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1929 | constant | OUTER_OORT_CLOUD_AU | 100000 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1933 | constant | GRAVITATIONAL_INFLUENCE_AU | 150000 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 2004 | constant | MERCURY_RADIUS_KM | 2439.7 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 2007 | constant | VENUS_RADIUS_KM | 6051.8 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 2022 | constant | PHOBOS_RADIUS_KM | 11.1 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 2040 | constant | PLUTO_RADIUS_KM | 1188.3 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 2043 | constant | BENNU_RADIUS_KM | 0.24503 | 3 | 5 | **15** | Cited; cross-check incomplete (1/2 models) | MEASURED -- independently catalogued fact (name) |
| 2061 | constant | ERIS_RADIUS_KM | 1163 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 2087 | constant | MAKEMAKE_RADIUS_KM | 715 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 2125 | dict | KNOWN_ORBITAL_PERIODS[...] | (133 entries) | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 2634 | constant | M3_PER_KM3 | 1000000000.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED (inferred from role 'data') |
| 2730 | constant | SGR_A_MASS_SOLAR | 4297000.0 | 3 | 5 | **15** | Cited; cross-check incomplete (1/2 models) | MEASURED -- independently catalogued fact (name) |
| 2758 | constant | SGR_A_DISTANCE_PC | 8277.0 | 3 | 5 | **15** | Cited, not independently cross-checked | MEASURED -- independently catalogued fact (name) |
| 1 | string | display string @ line 1 | (7 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 692 | constant | EARTH_VAN_ALLEN_INNER_RADII | 1.5 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 1108 | constant | EARTH_MAGNETOPAUSE_SHUE_A1_RADII | 10.22 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 1128 | constant | EARTH_MAGNETOPAUSE_SHUE_A2_RADII | 1.29 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 1240 | constant | EARTH_BOW_SHOCK_JELINEK_R0_RADII | 15.02 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 1309 | constant | EARTH_MAGNETOPAUSE_SHUE_SCATTER_RADII | 1.23 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 1395 | constant | EARTH_BOW_SHOCK_JELINEK_SCATTER_RADII | 0.69 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 1465 | constant | EARTH_MAGNETOTAIL_OBSERVED_RADII | 220.0 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 1520 | constant | EARTH_MAGNETOTAIL_FLARE_END_RADII | 120.0 | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | RELATIONAL -- defined against a tracked base (name) |
| 1554 | constant | EARTH_MAGNETOTAIL_DIAMETER_RADII | 60.0 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 1622 | constant | EARTH_GEOCORONA_RADII | 100.0 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 1765 | constant | INNER_CORONA_RADII | 3 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 1790 | constant | OUTER_CORONA_RADII | 50 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 1796 | constant | HELMET_CUSP_RADII | 4.0 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 1854 | constant | ALFVEN_SURFACE_RADII | 19.7 | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 2099 | dict | CENTER_BODY_RADII[...] | (1 entry) | 3 | 4 | **12** | Cited, not independently cross-checked | RELATIONAL -- defined against a tracked base (name) |
| 130 | constant | KM_PER_AU | 149597870.7 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 145 | constant | SUN_RADIUS_KM | 695700.0 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 155 | constant | EARTH_EQUATORIAL_RADIUS_KM | 6378.1366 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 176 | constant | EARTH_POLAR_RADIUS_KM | 6356.752 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 1641 | constant | JUPITER_EQUATORIAL_RADIUS_KM | 71492.0 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 1647 | constant | JUPITER_POLAR_RADIUS_KM | 66854.0 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 1653 | constant | SPEED_OF_LIGHT_KM_S | 299792.458 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED (inferred from role 'data') |
| 1904 | constant | TERMINATION_SHOCK_AU | 94 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 2010 | constant | MOON_RADIUS_KM | 1737.4 | 2 | 5 | **10** | Cross-checked by 3 models (Claude, GPT, Gemini) | MEASURED -- independently catalogued fact (name) |
| 2017 | constant | MARS_RADIUS_KM | 3396.2 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 2025 | constant | SATURN_RADIUS_KM | 60268 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 2030 | constant | URANUS_RADIUS_KM | 25559 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 2035 | constant | NEPTUNE_RADIUS_KM | 24764 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 2064 | constant | HAUMEA_RADIUS_KM | 798 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 2090 | constant | ARROKOTH_RADIUS_KM | 9.1 | 2 | 5 | **10** | Cross-checked by 2 models (Claude, GPT) | MEASURED -- independently catalogued fact (name) |
| 2596 | constant | GRAVITATIONAL_CONSTANT_SI | 6.6743e-11 | 2 | 5 | **10** | Cross-checked by 3 models (Claude, GPT, Gemini) | MEASURED (inferred from role 'data') |
| 2618 | constant | GM_SUN_SI | 1.3271244e+20 | 2 | 5 | **10** | Cross-checked by 3 models (Claude, GPT, Gemini) | MEASURED (inferred from role 'data') |
| 2703 | constant | PARSEC_TO_AU | 206264.806247096 | 2 | 5 | **10** | Cross-checked by 3 models (Claude, GPT, Gemini) | MEASURED -- independently catalogued fact (name) |

### coordinate_system_guide.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 248 | string | display string @ line 248 | (10 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 537 | string | display string @ line 537 | (10 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

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
| 267 | string | display string @ line 267 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 344 | string | display string @ line 344 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 418 | string | display string @ line 418 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 493 | string | display string @ line 493 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 564 | string | display string @ line 564 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 586 | string | display string @ line 586 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 724 | string | display string @ line 724 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 747 | string | display string @ line 747 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 803 | string | display string @ line 803 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 826 | string | display string @ line 826 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 895 | string | display string @ line 895 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 950 | string | display string @ line 950 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1365 | string | display string @ line 1365 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1385 | string | display string @ line 1385 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1448 | string | display string @ line 1448 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1455 | string | display string @ line 1455 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1487 | string | display string @ line 1487 | (6 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1501 | string | display string @ line 1501 | (7 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1563 | string | display string @ line 1563 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1600 | string | display string @ line 1600 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

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
| 1510 | string | display string @ line 1510 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1623 | string | display string @ line 1623 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1766 | string | display string @ line 1766 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1833 | string | display string @ line 1833 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2541 | string | display string @ line 2541 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2681 | string | display string @ line 2681 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2705 | string | display string @ line 2705 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2772 | string | display string @ line 2772 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2838 | string | display string @ line 2838 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 3039 | string | display string @ line 3039 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 3705 | string | display string @ line 3705 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 4411 | string | display string @ line 4411 | (12 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### info_dictionary.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 265 | dict | INFO[...] | (182 entries) | 3 | 5 | **15** | Cited, not cross-checked; date-sensitive | MEASURED (inferred from role 'data') |
| 1 | string | display string @ line 1 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 41 | string | display string @ line 41 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 174 | string | display string @ line 174 | (1 claim) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 289 | string | display string @ line 289 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 296 | string | display string @ line 296 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 303 | string | display string @ line 303 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 308 | string | display string @ line 308 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 346 | string | display string @ line 346 | (12 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 366 | string | display string @ line 366 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 386 | string | display string @ line 386 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 424 | string | display string @ line 424 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 443 | string | display string @ line 443 | (10 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 472 | string | display string @ line 472 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 495 | string | display string @ line 495 | (6 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 505 | string | display string @ line 505 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 521 | string | display string @ line 521 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 530 | string | display string @ line 530 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 538 | string | display string @ line 538 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 552 | string | display string @ line 552 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 563 | string | display string @ line 563 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 597 | string | display string @ line 597 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 611 | string | display string @ line 611 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 625 | string | display string @ line 625 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 633 | string | display string @ line 633 | (12 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 663 | string | display string @ line 663 | (9 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 686 | string | display string @ line 686 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 715 | string | display string @ line 715 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 728 | string | display string @ line 728 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 748 | string | display string @ line 748 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 751 | string | display string @ line 751 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 755 | string | display string @ line 755 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 757 | string | display string @ line 757 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 768 | string | display string @ line 768 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 772 | string | display string @ line 772 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 776 | string | display string @ line 776 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 781 | string | display string @ line 781 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 798 | string | display string @ line 798 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 838 | string | display string @ line 838 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 859 | string | display string @ line 859 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 872 | string | display string @ line 872 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 875 | string | display string @ line 875 | (12 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 904 | string | display string @ line 904 | (5 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 908 | string | display string @ line 908 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 911 | string | display string @ line 911 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 914 | string | display string @ line 914 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 917 | string | display string @ line 917 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 921 | string | display string @ line 921 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 926 | string | display string @ line 926 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 929 | string | display string @ line 929 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 933 | string | display string @ line 933 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 938 | string | display string @ line 938 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 942 | string | display string @ line 942 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 952 | string | display string @ line 952 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 956 | string | display string @ line 956 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 964 | string | display string @ line 964 | (6 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 972 | string | display string @ line 972 | (10 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1004 | string | display string @ line 1004 | (6 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1019 | string | display string @ line 1019 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1027 | string | display string @ line 1027 | (4 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1040 | string | display string @ line 1040 | (10 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1063 | string | display string @ line 1063 | (11 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1082 | string | display string @ line 1082 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1099 | string | display string @ line 1099 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1109 | string | display string @ line 1109 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1112 | string | display string @ line 1112 | (7 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1119 | string | display string @ line 1119 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1127 | string | display string @ line 1127 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1145 | string | display string @ line 1145 | (4 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1162 | string | display string @ line 1162 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1165 | string | display string @ line 1165 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1182 | string | display string @ line 1182 | (5 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1202 | string | display string @ line 1202 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1254 | string | display string @ line 1254 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1258 | string | display string @ line 1258 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1319 | string | display string @ line 1319 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1329 | string | display string @ line 1329 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1333 | string | display string @ line 1333 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1363 | string | display string @ line 1363 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1376 | string | display string @ line 1376 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1393 | string | display string @ line 1393 | (4 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1431 | string | display string @ line 1431 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1471 | string | display string @ line 1471 | (12 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1490 | string | display string @ line 1490 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1521 | string | display string @ line 1521 | (9 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1570 | string | display string @ line 1570 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1574 | string | display string @ line 1574 | (4 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1601 | string | display string @ line 1601 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1605 | string | display string @ line 1605 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1645 | string | display string @ line 1645 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1703 | string | display string @ line 1703 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1707 | string | display string @ line 1707 | (19 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1779 | string | display string @ line 1779 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1820 | string | display string @ line 1820 | (14 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1872 | string | display string @ line 1872 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1876 | string | display string @ line 1876 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1883 | string | display string @ line 1883 | (7 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1910 | string | display string @ line 1910 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1920 | string | display string @ line 1920 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1931 | string | display string @ line 1931 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1943 | string | display string @ line 1943 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1954 | string | display string @ line 1954 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 1963 | string | display string @ line 1963 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2003 | string | display string @ line 2003 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2033 | string | display string @ line 2033 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2052 | string | display string @ line 2052 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2067 | string | display string @ line 2067 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2086 | string | display string @ line 2086 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2098 | string | display string @ line 2098 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2119 | string | display string @ line 2119 | (21 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2143 | string | display string @ line 2143 | (4 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2189 | string | display string @ line 2189 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2190 | string | display string @ line 2190 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2191 | string | display string @ line 2191 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2192 | string | display string @ line 2192 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2193 | string | display string @ line 2193 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2194 | string | display string @ line 2194 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2195 | string | display string @ line 2195 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2196 | string | display string @ line 2196 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2200 | string | display string @ line 2200 | (8 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2227 | string | display string @ line 2227 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2237 | string | display string @ line 2237 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2247 | string | display string @ line 2247 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2248 | string | display string @ line 2248 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2249 | string | display string @ line 2249 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

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
| 539 | string | display string @ line 539 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 543 | string | display string @ line 543 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 547 | string | display string @ line 547 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 562 | string | display string @ line 562 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 566 | string | display string @ line 566 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 570 | string | display string @ line 570 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 574 | string | display string @ line 574 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 578 | string | display string @ line 578 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 582 | string | display string @ line 582 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 586 | string | display string @ line 586 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 816 | string | display string @ line 816 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 824 | string | display string @ line 824 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

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
| 1 | string | display string @ line 1 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 166 | string | display string @ line 166 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 171 | string | display string @ line 171 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 186 | string | display string @ line 186 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 190 | string | display string @ line 190 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 204 | string | display string @ line 204 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 208 | string | display string @ line 208 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 226 | string | display string @ line 226 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 231 | string | display string @ line 231 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 244 | string | display string @ line 244 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 288 | string | display string @ line 288 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 321 | string | display string @ line 321 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 327 | string | display string @ line 327 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 341 | string | display string @ line 341 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 351 | string | display string @ line 351 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 369 | string | display string @ line 369 | (9 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 390 | string | display string @ line 390 | (1 claim) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 408 | string | display string @ line 408 | (4 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 428 | string | display string @ line 428 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 443 | string | display string @ line 443 | (1 claim) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 475 | string | display string @ line 475 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 481 | string | display string @ line 481 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 510 | string | display string @ line 510 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 536 | string | display string @ line 536 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 553 | string | display string @ line 553 | (9 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 572 | string | display string @ line 572 | (3 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1319 | string | display string @ line 1319 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1340 | string | display string @ line 1340 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1363 | string | display string @ line 1363 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1443 | string | display string @ line 1443 | (6 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1453 | string | display string @ line 1453 | (6 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1471 | string | display string @ line 1471 | (11 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1479 | string | display string @ line 1479 | (11 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1498 | string | display string @ line 1498 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1507 | string | display string @ line 1507 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1524 | string | display string @ line 1524 | (1 claim) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1534 | string | display string @ line 1534 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1558 | string | display string @ line 1558 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1564 | string | display string @ line 1564 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1580 | string | display string @ line 1580 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1586 | string | display string @ line 1586 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1601 | string | display string @ line 1601 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1608 | string | display string @ line 1608 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1624 | string | display string @ line 1624 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1633 | string | display string @ line 1633 | (3 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1651 | string | display string @ line 1651 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1658 | string | display string @ line 1658 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1675 | string | display string @ line 1675 | (4 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 1685 | string | display string @ line 1685 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1955 | string | display string @ line 1955 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2155 | string | display string @ line 2155 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2185 | string | display string @ line 2185 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2218 | string | display string @ line 2218 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2255 | string | display string @ line 2255 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2293 | string | display string @ line 2293 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2309 | string | display string @ line 2309 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2328 | string | display string @ line 2328 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2330 | string | display string @ line 2330 | (7 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2351 | string | display string @ line 2351 | (1 claim) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2353 | string | display string @ line 2353 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2393 | string | display string @ line 2393 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2409 | string | display string @ line 2409 | (2 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 2424 | string | display string @ line 2424 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2437 | string | display string @ line 2437 | (2 claims) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 2453 | string | display string @ line 2453 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2494 | string | display string @ line 2494 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2510 | string | display string @ line 2510 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2528 | string | display string @ line 2528 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2542 | string | display string @ line 2542 | (1 claim) | 3 | 4 | **12** | Cited via enclosing block citation | Public-facing display string (hover/INFO) |
| 2559 | string | display string @ line 2559 | (10 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2610 | string | display string @ line 2610 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2626 | string | display string @ line 2626 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2657 | string | display string @ line 2657 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2700 | string | display string @ line 2700 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2716 | string | display string @ line 2716 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 2750 | string | display string @ line 2750 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

### solar_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 105 | string | display string @ line 105 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 131 | string | display string @ line 131 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 149 | string | display string @ line 149 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 164 | string | display string @ line 164 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 179 | string | display string @ line 179 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 204 | string | display string @ line 204 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 233 | string | display string @ line 233 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 258 | string | display string @ line 258 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 291 | string | display string @ line 291 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 305 | string | display string @ line 305 | (4 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 314 | string | display string @ line 314 | (4 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 326 | string | display string @ line 326 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 363 | string | display string @ line 363 | (3 claims) | 3 | 4 | **12** | Cited, not cross-checked; date-sensitive | Public-facing display string (hover/INFO) |
| 386 | string | display string @ line 386 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 392 | string | display string @ line 392 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 425 | string | display string @ line 425 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 454 | string | display string @ line 454 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 489 | string | display string @ line 489 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 604 | string | display string @ line 604 | (4 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 613 | string | display string @ line 613 | (3 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 637 | string | display string @ line 637 | (10 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 681 | string | display string @ line 681 | (18 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 710 | string | display string @ line 710 | (14 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 738 | string | display string @ line 738 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 746 | string | display string @ line 746 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 773 | string | display string @ line 773 | (6 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 791 | string | display string @ line 791 | (8 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1705 | string | display string @ line 1705 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 1726 | string | display string @ line 1726 | (1 claim) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

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
| 415 | string | display string @ line 415 | (5 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 704 | string | display string @ line 704 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |
| 780 | string | display string @ line 780 | (2 claims) | 3 | 4 | **12** | Cited, not independently cross-checked | Public-facing display string (hover/INFO) |

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
| 64 | dict | CAD_BODY_NAMES[...] | (11 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal use (name vocabulary) |

### constants_new.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1844 | constant | ROCHE_LIMIT_RADII | 3.45 | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | RELATIONAL -- defined against a tracked base (name) |
| 1911 | constant | HELIOPAUSE_RADII | 26148 | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | RELATIONAL -- defined against a tracked base (name) |
| 1953 | constant | PARKER_CLOSEST_RADII | 9.86 | 2 | 4 | **8** | Cross-checked by 2 models (Claude, GPT) | RELATIONAL -- defined against a tracked base (name) |

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
| 81 | dict | KIND_LABEL[...] | (3 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 87 | dict | KIND_ORDER[...] | (4 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 90 | constant | TAG_SCAN_LINES | 40 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

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
| 125 | constant | SCHEMA | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

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
| 110 | dict | object_type_mapping[...] | (79 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal use (name vocabulary) |
| 246 | dict | class_mapping[...] | (14 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal use (name vocabulary) |

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
| 106 | dict | ROLE_MAP[...] | (134 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 381 | dict | ROLE_DESCRIPTIONS[...] | (13 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 404 | dict | ROLE_SECTION_TITLES[...] | (13 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

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

### orrery_maintenance_run.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 230 | constant | TOOL_TIMEOUT_SECONDS | 900 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 293 | constant | HASH_LIMIT_BYTES | 2 * 1024 * 1024 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 412 | constant | NOTE_WIDTH | 44 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 413 | constant | NOTE_INDENT | 37 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |

### osculating_cache_manager.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 82 | dict | REFRESH_INTERVALS[...] | (14 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'cache') |

### palomas_orrery.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 2123 | constant | PERFRAME_INDICATOR_RADIUS_FACTOR | 100.0 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |
| 2156 | constant | PERFRAME_COORD_DECIMALS | 7 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |
| 3752 | constant | BUTTON_WIDTH | 14 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |

### palomas_orrery_dashboard.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 154 | constant | WINDOW_WIDTH | 960 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |
| 155 | constant | WINDOW_HEIGHT | 720 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |
| 926 | constant | TOOLTIP_DELAY_MS | 400 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'gui') |
| 1057 | dict | SECTION_SYMBOLS[...] | (7 entries) | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'gui') |

### planet_visualization_utilities.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1039 | dict | STREAMER_BAND_DEFAULTS[...] | (20 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (name vocabulary) |

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
| 336 | constant | V_FETCHED | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 337 | constant | V_CROSS_CHECKED | 2 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 346 | constant | V_SOURCED | 3 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 349 | constant | V_RECALLED | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 358 | constant | C_COSMETIC | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 359 | constant | C_INTERNAL | 2 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 360 | constant | C_LOADBEARING | 3 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 361 | constant | C_PUBLIC | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 362 | constant | C_PROPAGATING | 5 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 367 | constant | C_RELATIONAL | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 368 | constant | C_MEASURED | 5 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 373 | constant | C_UNDETERMINED | 5 | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 474 | dict | DOMAIN_LABELS[...] | (6 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 483 | dict | MODULE_DOMAIN_MAP[...] | (101 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal (role 'devtool') |
| 1140 | constant | CITATION_LOOKBACK_BLOCK | 15 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |
| 2016 | constant | SHADOW_DERIVED_MIN_MAGNITUDE | 100.0 | 3 | 2 | **6** | Cited, not independently cross-checked | Internal (role 'devtool') |

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

### test_dimensions.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 125 | constant | REL_TOL | 1e-09 | 4 | 2 | **8** | No source citation; date-sensitive (recalled) | Internal (role 'devtool') |

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
| 1689 | constant | DEFAULT_MARKER_SIZE | 7 | 3 | 1 | **3** | Cited, not independently cross-checked | Cosmetic (name vocabulary) |
| 1691 | constant | CENTER_MARKER_SIZE | 10 | 3 | 1 | **3** | Cited, not independently cross-checked | Cosmetic (name vocabulary) |

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
