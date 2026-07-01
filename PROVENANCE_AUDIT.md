# Paloma's Orrery -- Provenance Audit

Generated: June 30, 2026
Files scanned: 115
Total findings: 666
Constants: 69 | Dicts: 34 | Display strings: 563

Unit of provenance: the smallest thing with a coherent source citation. A dict with one block-level `# Source:` comment is ONE unit; all its entries inherit that citation. A hover string with co-referring numbers is ONE unit.

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
| 1 | 16-20 | FIX NOW | 104 |
| 2 | 10-15 | ALL ACCEPTED RESIDUALS -- see note below | 153 |
| 3 | 5-9 | ALREADY CITED OR LOW RISK -- no action required | 391 |
| 4 | 1-4 | NO ACTION NEEDED | 18 |

**Tier 2 note (April 2026 audit):** All Tier-2 findings are documented
accepted residuals -- cited constants, V_STALE staleness flags on verified
strings, or known scanner limitations. No action required unless a new
uncited entry appears. See Accepted Residuals block below for details.

---

## COVERAGE GAPS -- needs role classification

These modules are classified `'other'` in module_atlas.py's ROLE_MAP (unrecognized, not deliberately excluded) and contain string content that looks claim-shaped. They are NOT scanned for narrative citations -- role-driven inclusion only covers data / scenario / rendering / rendering-shells / computation. Add each to ROLE_MAP with its real role (or to narrative_files as a manual override) so it stops being invisible.

| Module | Claim-shaped strings |
|--------|----------------------:|
| `shell_configs.py` | 91 |
| `food_insecurity_generator.py` | 1 |
| `orrery_rendering.py` | 1 |
| `smoke_rotation_axis.py` | 1 |

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
| 1200 | string | display string @ line 1200 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1202 | string | display string @ line 1202 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1204 | string | display string @ line 1204 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### celestial_coordinates.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 438 | string | display string @ line 438 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 447 | string | display string @ line 447 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 449 | string | display string @ line 449 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### coordinate_system_guide.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 116 | string | display string @ line 116 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 149 | string | display string @ line 149 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### data_acquisition.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 199 | string | display string @ line 199 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### earth_system_generator.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 696 | string | display string @ line 696 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 741 | string | display string @ line 741 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### energy_imbalance.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 532 | string | display string @ line 532 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### exoplanet_coordinates.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 86 | string | display string @ line 86 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 125 | string | display string @ line 125 | (5 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 299 | string | display string @ line 299 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 307 | string | display string @ line 307 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### exoplanet_orbits.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 288 | string | display string @ line 288 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### fetch_paleoclimate_data.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 149 | string | display string @ line 149 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### hr_diagram_distance.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 217 | string | display string @ line 217 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### idealized_orbits.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 121 | string | display string @ line 121 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 136 | string | display string @ line 136 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 164 | string | display string @ line 164 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 178 | string | display string @ line 178 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1403 | string | display string @ line 1403 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1462 | string | display string @ line 1462 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1473 | string | display string @ line 1473 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1586 | string | display string @ line 1586 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2382 | string | display string @ line 2382 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2428 | string | display string @ line 2428 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2450 | string | display string @ line 2450 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2476 | string | display string @ line 2476 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2509 | string | display string @ line 2509 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2683 | string | display string @ line 2683 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2807 | string | display string @ line 2807 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2929 | string | display string @ line 2929 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 3624 | string | display string @ line 3624 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 3827 | string | display string @ line 3827 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4296 | string | display string @ line 4296 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4563 | string | display string @ line 4563 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4585 | string | display string @ line 4585 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4649 | string | display string @ line 4649 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 4683 | string | display string @ line 4683 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 5909 | string | display string @ line 5909 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### object_type_analyzer.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 652 | string | display string @ line 652 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### paleoclimate_dual_scale.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 902 | string | display string @ line 902 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1047 | string | display string @ line 1047 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### paleoclimate_human_origins_full.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 200 | string | display string @ line 200 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 220 | string | display string @ line 220 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 362 | string | display string @ line 362 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1363 | string | display string @ line 1363 | (9 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1410 | string | display string @ line 1410 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1440 | string | display string @ line 1440 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1618 | string | display string @ line 1618 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1638 | string | display string @ line 1638 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1658 | string | display string @ line 1658 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### paleoclimate_visualization.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 129 | string | display string @ line 129 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 420 | string | display string @ line 420 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 454 | string | display string @ line 454 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### paleoclimate_visualization_full.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 188 | string | display string @ line 188 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 934 | string | display string @ line 934 | (9 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 981 | string | display string @ line 981 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1011 | string | display string @ line 1011 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1189 | string | display string @ line 1189 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1209 | string | display string @ line 1209 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1229 | string | display string @ line 1229 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### paleoclimate_wet_bulb_full.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 119 | string | display string @ line 119 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 127 | string | display string @ line 127 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 161 | string | display string @ line 161 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 250 | string | display string @ line 250 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 472 | string | display string @ line 472 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1758 | string | display string @ line 1758 | (9 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1805 | string | display string @ line 1805 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1835 | string | display string @ line 1835 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2013 | string | display string @ line 2013 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2033 | string | display string @ line 2033 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 2053 | string | display string @ line 2053 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### planet_visualization_utilities.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 436 | string | display string @ line 436 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 678 | string | display string @ line 678 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 680 | string | display string @ line 680 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 685 | string | display string @ line 685 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 689 | string | display string @ line 689 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 697 | string | display string @ line 697 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 705 | string | display string @ line 705 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### planetarium_distance.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 228 | string | display string @ line 228 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### plot_data_report_widget.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 277 | string | display string @ line 277 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### scenarios_coral_bleaching.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 61 | string | display string @ line 61 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### scenarios_western_heatwave_march_2026.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 917 | string | display string @ line 917 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1161 | string | display string @ line 1161 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1271 | string | display string @ line 1271 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### sgr_a_grand_tour.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 563 | string | display string @ line 563 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 575 | string | display string @ line 575 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 587 | string | display string @ line 587 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 599 | string | display string @ line 599 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 621 | string | display string @ line 621 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 631 | string | display string @ line 631 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### sgr_a_visualization_core.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 151 | string | display string @ line 151 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 259 | string | display string @ line 259 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 328 | string | display string @ line 328 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 381 | string | display string @ line 381 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### sgr_a_visualization_precession.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 298 | string | display string @ line 298 | (3 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 439 | string | display string @ line 439 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### visualization_utils.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 339 | string | display string @ line 339 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

---

## Tier 2: ALL ACCEPTED RESIDUALS -- see note below (Score 10-15)

### celestial_objects.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 628 | string | display string @ line 628 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 647 | string | display string @ line 647 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 663 | string | display string @ line 663 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 670 | string | display string @ line 670 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |

### comet_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 42 | dict | COMET_NUCLEUS_SIZES[...] | (16 entries) | 4 | 3 | **12** | No source citation (recalled) | Geometry dict in rendering/shells module |
| 331 | string | display string @ line 331 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1174 | string | display string @ line 1174 | (3 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 1595 | dict | COMET_FEATURE_THRESHOLDS[...] | (3 entries) | 4 | 3 | **12** | No source citation (recalled) | Imported by 1 module(s) |

### constants_new.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 47 | constant | KM_PER_AU | 149597870.7 | 2 | 5 | **10** | Has source citation | Imported by 10 modules |
| 131 | constant | CHROMOSPHERE_RADII | 1.5 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 136 | constant | INNER_CORONA_RADII | 3 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 141 | constant | OUTER_CORONA_RADII | 50 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 173 | constant | TERMINATION_SHOCK_AU | 94 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 179 | constant | HELIOPAUSE_RADII | 26449 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 188 | constant | INNER_LIMIT_OORT_CLOUD_AU | 2000 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 192 | constant | INNER_OORT_CLOUD_AU | 20000 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 196 | constant | OUTER_OORT_CLOUD_AU | 100000 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 200 | constant | GRAVITATIONAL_INFLUENCE_AU | 126000 | 2 | 5 | **10** | Has source citation | Imported by 4 modules |
| 206 | constant | PARKER_CLOSEST_RADII | 9.86 | 2 | 5 | **10** | Has source citation | Imported by 3 modules |
| 241 | dict | CENTER_BODY_RADII[...] | (18 entries) | 2 | 5 | **10** | Has source citation | Imported by 9 modules |
| 263 | dict | KNOWN_ORBITAL_PERIODS[...] | (133 entries) | 2 | 5 | **10** | Has source citation | Imported by 8 modules |

### earth_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 980 | string | display string @ line 980 | (6 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 994 | string | display string @ line 994 | (7 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1046 | string | display string @ line 1046 | (5 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |

### eris_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 459 | string | display string @ line 459 | (5 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |

### idealized_orbits.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 3580 | string | display string @ line 3580 | (1 claim) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 5813 | string | display string @ line 5813 | (1 claim) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |

### info_dictionary.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 259 | dict | INFO[...] | (183 entries) | 3 | 5 | **15** | Sourced but potentially stale | Imported by 3 modules |
| 283 | string | display string @ line 283 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 290 | string | display string @ line 290 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 297 | string | display string @ line 297 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 302 | string | display string @ line 302 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 340 | string | display string @ line 340 | (8 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 360 | string | display string @ line 360 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 380 | string | display string @ line 380 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 418 | string | display string @ line 418 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 437 | string | display string @ line 437 | (8 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 466 | string | display string @ line 466 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 489 | string | display string @ line 489 | (4 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 627 | string | display string @ line 627 | (10 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 657 | string | display string @ line 657 | (9 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 680 | string | display string @ line 680 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 709 | string | display string @ line 709 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 722 | string | display string @ line 722 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 742 | string | display string @ line 742 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 745 | string | display string @ line 745 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 749 | string | display string @ line 749 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 751 | string | display string @ line 751 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 762 | string | display string @ line 762 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 766 | string | display string @ line 766 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 770 | string | display string @ line 770 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 775 | string | display string @ line 775 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 832 | string | display string @ line 832 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 853 | string | display string @ line 853 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 866 | string | display string @ line 866 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 869 | string | display string @ line 869 | (11 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 898 | string | display string @ line 898 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 902 | string | display string @ line 902 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 905 | string | display string @ line 905 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 908 | string | display string @ line 908 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 911 | string | display string @ line 911 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 915 | string | display string @ line 915 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 920 | string | display string @ line 920 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 923 | string | display string @ line 923 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 950 | string | display string @ line 950 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 958 | string | display string @ line 958 | (5 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 966 | string | display string @ line 966 | (8 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 998 | string | display string @ line 998 | (5 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1013 | string | display string @ line 1013 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1139 | string | display string @ line 1139 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1156 | string | display string @ line 1156 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1159 | string | display string @ line 1159 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1176 | string | display string @ line 1176 | (5 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1196 | string | display string @ line 1196 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1313 | string | display string @ line 1313 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1323 | string | display string @ line 1323 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1327 | string | display string @ line 1327 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1357 | string | display string @ line 1357 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1370 | string | display string @ line 1370 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1387 | string | display string @ line 1387 | (4 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1425 | string | display string @ line 1425 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1465 | string | display string @ line 1465 | (11 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1484 | string | display string @ line 1484 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1515 | string | display string @ line 1515 | (7 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1564 | string | display string @ line 1564 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1568 | string | display string @ line 1568 | (4 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1595 | string | display string @ line 1595 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1599 | string | display string @ line 1599 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1639 | string | display string @ line 1639 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1697 | string | display string @ line 1697 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1701 | string | display string @ line 1701 | (18 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1814 | string | display string @ line 1814 | (7 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1866 | string | display string @ line 1866 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1870 | string | display string @ line 1870 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1877 | string | display string @ line 1877 | (6 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1904 | string | display string @ line 1904 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1914 | string | display string @ line 1914 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1925 | string | display string @ line 1925 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1937 | string | display string @ line 1937 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1948 | string | display string @ line 1948 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2092 | string | display string @ line 2092 | (27 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2137 | string | display string @ line 2137 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2156 | string | display string @ line 2156 | (7 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 2180 | string | display string @ line 2180 | (1 claim) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 2183 | string | display string @ line 2183 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2184 | string | display string @ line 2184 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2185 | string | display string @ line 2185 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2186 | string | display string @ line 2186 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2187 | string | display string @ line 2187 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2188 | string | display string @ line 2188 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2189 | string | display string @ line 2189 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2190 | string | display string @ line 2190 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2194 | string | display string @ line 2194 | (8 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2221 | string | display string @ line 2221 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 104 | dict | object_type_mapping[...] | (79 entries) | 2 | 5 | **10** | Has source citation | Imported by 6 modules |
| 240 | dict | class_mapping[...] | (14 entries) | 2 | 5 | **10** | Has source citation | Imported by 5 modules |

### mercury_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 289 | string | display string @ line 289 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |

### module_atlas.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 43 | dict | ROLE_MAP[...] | (94 entries) | 4 | 3 | **12** | No source citation (recalled) | Imported by 1 module(s) |

### neptune_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 683 | string | display string @ line 683 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |

### orbital_elements.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1430 | dict | planet_tilts[...] | (7 entries) | 4 | 3 | **12** | No source citation (recalled) | Imported by 1 module(s) |

### planet_visualization_utilities.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 532 | dict | ROTATION_AXIS_OMITTED[...] | (2 entries) | 4 | 3 | **12** | No source citation (recalled) | Imported by 1 module(s) |

### scenarios_western_heatwave_march_2026.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1223 | string | display string @ line 1223 | (3 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 1394 | string | display string @ line 1394 | (1 claim) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 1471 | string | display string @ line 1471 | (1 claim) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |

### sgr_a_grand_tour.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 54 | dict | ROSETTE_ORBIT_COUNTS[...] | (4 entries) | 4 | 3 | **12** | No source citation (recalled) | Geometry dict in rendering module |

### sgr_a_visualization_animation.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 24 | dict | ANIMATION_CONFIG[...] | (5 entries) | 4 | 3 | **12** | No source citation (recalled) | Geometry dict in rendering module |

### sgr_a_visualization_precession.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 30 | dict | S4714_ACCURACY_PATCH[...] | (1 entry) | 4 | 3 | **12** | No source citation (recalled) | Geometry dict in rendering module |

### solar_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 245 | string | display string @ line 245 | (8 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 265 | string | display string @ line 265 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 297 | string | display string @ line 297 | (6 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 856 | string | display string @ line 856 | (19 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 883 | string | display string @ line 883 | (19 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 907 | string | display string @ line 907 | (5 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |

### spacecraft_encounters.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 114 | string | display string @ line 114 | (5 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |

### star_notes.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 311 | string | display string @ line 311 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 338 | string | display string @ line 338 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 391 | string | display string @ line 391 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 418 | string | display string @ line 418 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 471 | string | display string @ line 471 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 728 | string | display string @ line 728 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 744 | string | display string @ line 744 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 758 | string | display string @ line 758 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 773 | string | display string @ line 773 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 788 | string | display string @ line 788 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 803 | string | display string @ line 803 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 830 | string | display string @ line 830 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 894 | string | display string @ line 894 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 925 | string | display string @ line 925 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 973 | string | display string @ line 973 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1029 | string | display string @ line 1029 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |

### star_sphere_builder.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 493 | dict | CONSTELLATION_NAMES[...] | (88 entries) | 4 | 3 | **12** | No source citation (recalled) | Geometry dict in rendering module |

### uranus_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 532 | string | display string @ line 532 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 625 | string | display string @ line 625 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |

---

## Tier 3: ALREADY CITED OR LOW RISK -- no action required (Score 5-9)

### add_docstrings.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 31 | dict | DOCSTRINGS[...] | (42 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### apsidal_markers.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1854 | constant | ENCOUNTER_THRESHOLD_AU | 0.5 | 2 | 3 | **6** | Has source citation | Numeric constant in computation module |

### asteroid_belt_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 77 | string | display string @ line 77 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 129 | string | display string @ line 129 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### celestial_coordinates.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 384 | string | display string @ line 384 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 451 | string | display string @ line 451 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 137 | dict | MAJOR_BODY_UNCERTAINTIES[...] | (206 entries) | 3 | 2 | **6** | Sourced but potentially stale | Internal use (not imported externally) |

### celestial_objects.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 44 | string | display string @ line 44 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 49 | string | display string @ line 49 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 57 | string | display string @ line 57 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 76 | string | display string @ line 76 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 98 | string | display string @ line 98 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 106 | string | display string @ line 106 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 112 | string | display string @ line 112 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 118 | string | display string @ line 118 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 124 | string | display string @ line 124 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 145 | string | display string @ line 145 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 161 | string | display string @ line 161 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 167 | string | display string @ line 167 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 193 | string | display string @ line 193 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 208 | string | display string @ line 208 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 232 | string | display string @ line 232 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 260 | string | display string @ line 260 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 268 | string | display string @ line 268 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 280 | string | display string @ line 280 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 291 | string | display string @ line 291 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 296 | string | display string @ line 296 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 329 | string | display string @ line 329 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 362 | string | display string @ line 362 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 379 | string | display string @ line 379 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 454 | string | display string @ line 454 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 508 | string | display string @ line 508 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 571 | string | display string @ line 571 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 917 | string | display string @ line 917 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 922 | string | display string @ line 922 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 927 | string | display string @ line 927 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 932 | string | display string @ line 932 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1052 | string | display string @ line 1052 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1057 | string | display string @ line 1057 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1112 | string | display string @ line 1112 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1119 | string | display string @ line 1119 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1126 | string | display string @ line 1126 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1133 | string | display string @ line 1133 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1140 | string | display string @ line 1140 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1146 | string | display string @ line 1146 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1152 | string | display string @ line 1152 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1162 | string | display string @ line 1162 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1170 | string | display string @ line 1170 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1178 | string | display string @ line 1178 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1186 | string | display string @ line 1186 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1194 | string | display string @ line 1194 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1202 | string | display string @ line 1202 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1210 | string | display string @ line 1210 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1218 | string | display string @ line 1218 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1237 | string | display string @ line 1237 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1260 | string | display string @ line 1260 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1268 | string | display string @ line 1268 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### close_approach_data.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### comet_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 90 | string | display string @ line 90 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 206 | string | display string @ line 206 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 232 | string | display string @ line 232 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 253 | string | display string @ line 253 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 280 | string | display string @ line 280 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 291 | string | display string @ line 291 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 302 | string | display string @ line 302 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 519 | string | display string @ line 519 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 525 | string | display string @ line 525 | (8 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 532 | string | display string @ line 532 | (16 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 698 | string | display string @ line 698 | (14 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1348 | string | display string @ line 1348 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1529 | string | display string @ line 1529 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1539 | string | display string @ line 1539 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1549 | string | display string @ line 1549 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1558 | string | display string @ line 1558 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1567 | string | display string @ line 1567 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1577 | string | display string @ line 1577 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1527 | dict | comet_visualization_info[...] | (6 entries) | 2 | 3 | **6** | Has source citation | Geometry dict in rendering/shells module |

### constants_new.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 54 | constant | SUN_RADIUS_KM | 695700.0 | 2 | 3 | **6** | Has source citation | Imported by 2 module(s) |
| 63 | constant | EARTH_EQUATORIAL_RADIUS_KM | 6378.137 | 2 | 3 | **6** | Has source citation | Imported by 1 module(s) |
| 69 | constant | EARTH_POLAR_RADIUS_KM | 6356.752 | 2 | 3 | **6** | Has source citation | Imported by 1 module(s) |
| 74 | constant | JUPITER_EQUATORIAL_RADIUS_KM | 71492.0 | 2 | 3 | **6** | Has source citation | Imported by 1 module(s) |
| 79 | constant | JUPITER_POLAR_RADIUS_KM | 66854.0 | 2 | 3 | **6** | Has source citation | Imported by 1 module(s) |
| 84 | constant | SPEED_OF_LIGHT_KM_S | 299792.458 | 2 | 3 | **6** | Has source citation | Imported by 2 module(s) |
| 109 | constant | DEFAULT_MARKER_SIZE | 7 | 2 | 3 | **6** | Has source citation | Imported by 2 module(s) |
| 111 | constant | CENTER_MARKER_SIZE | 10 | 2 | 3 | **6** | Has source citation | Imported by 2 module(s) |
| 147 | constant | STREAMER_BELT_RADII | 6.0 | 2 | 3 | **6** | Has source citation | Imported by 2 module(s) |
| 152 | constant | ROCHE_LIMIT_RADII | 3.45 | 2 | 3 | **6** | Has source citation | Imported by 2 module(s) |
| 161 | constant | ALFVEN_SURFACE_RADII | 18.8 | 2 | 3 | **6** | Has source citation | Imported by 2 module(s) |

### coordinate_system_guide.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 245 | string | display string @ line 245 | (9 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### dep_trace.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 32 | constant | HUB_THRESHOLD | 8 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 44 | dict | _ROLE_TO_VISUAL[...] | (12 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### earth_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 52 | string | display string @ line 52 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 68 | string | display string @ line 68 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 124 | string | display string @ line 124 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 140 | string | display string @ line 140 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 196 | string | display string @ line 196 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 211 | string | display string @ line 211 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 266 | string | display string @ line 266 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 281 | string | display string @ line 281 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 336 | string | display string @ line 336 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 351 | string | display string @ line 351 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 489 | string | display string @ line 489 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 505 | string | display string @ line 505 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 561 | string | display string @ line 561 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 577 | string | display string @ line 577 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 634 | string | display string @ line 634 | (7 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 698 | string | display string @ line 698 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 747 | string | display string @ line 747 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 785 | string | display string @ line 785 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 787 | string | display string @ line 787 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 867 | string | display string @ line 867 | (11 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 887 | string | display string @ line 887 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 940 | string | display string @ line 940 | (11 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1086 | string | display string @ line 1086 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1109 | string | display string @ line 1109 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### eris_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 53 | string | display string @ line 53 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 209 | string | display string @ line 209 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 476 | string | display string @ line 476 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### exoplanet_coordinates.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 33 | string | display string @ line 33 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### food_insecurity_generator.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 154 | string | display string @ line 154 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### idealized_orbits.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1512 | string | display string @ line 1512 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1625 | string | display string @ line 1625 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1768 | string | display string @ line 1768 | (8 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1835 | string | display string @ line 1835 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 2543 | string | display string @ line 2543 | (7 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 2707 | string | display string @ line 2707 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 2774 | string | display string @ line 2774 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 2840 | string | display string @ line 2840 | (6 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 3041 | string | display string @ line 3041 | (9 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 3695 | string | display string @ line 3695 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 3754 | string | display string @ line 3754 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 4401 | string | display string @ line 4401 | (11 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### info_dictionary.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 35 | string | display string @ line 35 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 499 | string | display string @ line 499 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 515 | string | display string @ line 515 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 524 | string | display string @ line 524 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 557 | string | display string @ line 557 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 591 | string | display string @ line 591 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 605 | string | display string @ line 605 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 619 | string | display string @ line 619 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 792 | string | display string @ line 792 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 927 | string | display string @ line 927 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 932 | string | display string @ line 932 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 936 | string | display string @ line 936 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 946 | string | display string @ line 946 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1034 | string | display string @ line 1034 | (8 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1057 | string | display string @ line 1057 | (7 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1076 | string | display string @ line 1076 | (6 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1093 | string | display string @ line 1093 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1103 | string | display string @ line 1103 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1106 | string | display string @ line 1106 | (7 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1113 | string | display string @ line 1113 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1121 | string | display string @ line 1121 | (8 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1248 | string | display string @ line 1248 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1252 | string | display string @ line 1252 | (6 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1773 | string | display string @ line 1773 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1957 | string | display string @ line 1957 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1997 | string | display string @ line 1997 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 2027 | string | display string @ line 2027 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 2046 | string | display string @ line 2046 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 2061 | string | display string @ line 2061 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 2080 | string | display string @ line 2080 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 2231 | string | display string @ line 2231 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 2241 | string | display string @ line 2241 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 2242 | string | display string @ line 2242 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 2243 | string | display string @ line 2243 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### jupiter_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 74 | string | display string @ line 74 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 90 | string | display string @ line 90 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 145 | string | display string @ line 145 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 160 | string | display string @ line 160 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 215 | string | display string @ line 215 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 231 | string | display string @ line 231 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 287 | string | display string @ line 287 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 305 | string | display string @ line 305 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 444 | string | display string @ line 444 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 462 | string | display string @ line 462 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 699 | string | display string @ line 699 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 789 | string | display string @ line 789 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 803 | string | display string @ line 803 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 907 | string | display string @ line 907 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 922 | string | display string @ line 922 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 937 | string | display string @ line 937 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 951 | string | display string @ line 951 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1019 | string | display string @ line 1019 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### ledger_index.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 75 | dict | SECTION_ALIASES[...] | (1 entry) | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 79 | dict | SECTION_TITLES[...] | (15 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### mars_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 514 | string | display string @ line 514 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 597 | string | display string @ line 597 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 709 | string | display string @ line 709 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 837 | string | display string @ line 837 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### measure_perframe_elements.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 38 | constant | KB | 1000.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 39 | constant | FRAMES_29 | 29 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 40 | constant | FRAMES_60 | 60 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### mercury_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 44 | string | display string @ line 44 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 58 | string | display string @ line 58 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 67 | string | display string @ line 67 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 81 | string | display string @ line 81 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 233 | string | display string @ line 233 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 398 | string | display string @ line 398 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### module_atlas.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 177 | dict | ROLE_DESCRIPTIONS[...] | (12 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### moon_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 53 | string | display string @ line 53 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 121 | string | display string @ line 121 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 208 | string | display string @ line 208 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 557 | string | display string @ line 557 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### neptune_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 110 | string | display string @ line 110 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 129 | string | display string @ line 129 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 194 | string | display string @ line 194 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 459 | string | display string @ line 459 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 594 | string | display string @ line 594 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 861 | string | display string @ line 861 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 883 | string | display string @ line 883 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 908 | string | display string @ line 908 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1194 | string | display string @ line 1194 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1227 | string | display string @ line 1227 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1257 | string | display string @ line 1257 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1287 | string | display string @ line 1287 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1317 | string | display string @ line 1317 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1347 | string | display string @ line 1347 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1380 | string | display string @ line 1380 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1412 | string | display string @ line 1412 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1444 | string | display string @ line 1444 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1476 | string | display string @ line 1476 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1508 | string | display string @ line 1508 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1538 | string | display string @ line 1538 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1680 | string | display string @ line 1680 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1700 | string | display string @ line 1700 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### object_type_analyzer.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 659 | string | display string @ line 659 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### orbit_data_manager.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 34 | constant | DEFAULT_DAYS_AHEAD | 730 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 35 | constant | MAX_DATA_AGE_DAYS | 90 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### osculating_cache_manager.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 79 | dict | REFRESH_INTERVALS[...] | (14 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### paleoclimate_human_origins_full.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 206 | string | display string @ line 206 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 228 | string | display string @ line 228 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### paleoclimate_wet_bulb_full.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 122 | string | display string @ line 122 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 132 | constant | BASELINE_ABSOLUTE_TEMP | 14.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 134 | constant | TW_SURVIVABILITY_BIOLOGICAL | 31.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 135 | constant | TW_SURVIVABILITY_THEORETICAL | 35.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 338 | string | display string @ line 338 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### palomas_orrery.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 2076 | constant | PERFRAME_INDICATOR_RADIUS_FACTOR | 100.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 2109 | constant | PERFRAME_COORD_DECIMALS | 7 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 3684 | constant | BUTTON_WIDTH | 14 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### palomas_orrery_dashboard.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 38 | constant | WINDOW_WIDTH | 960 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 39 | constant | WINDOW_HEIGHT | 720 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### planet9_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 35 | string | display string @ line 35 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 55 | string | display string @ line 55 | (8 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 212 | string | display string @ line 212 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 232 | string | display string @ line 232 | (11 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### planet_visualization_utilities.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 485 | string | display string @ line 485 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 489 | string | display string @ line 489 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 493 | string | display string @ line 493 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 497 | string | display string @ line 497 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 501 | string | display string @ line 501 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 505 | string | display string @ line 505 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 509 | string | display string @ line 509 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 513 | string | display string @ line 513 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 517 | string | display string @ line 517 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 521 | string | display string @ line 521 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 525 | string | display string @ line 525 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### pluto_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 33 | string | display string @ line 33 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 50 | string | display string @ line 50 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 123 | string | display string @ line 123 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 140 | string | display string @ line 140 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 206 | string | display string @ line 206 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 373 | string | display string @ line 373 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 394 | string | display string @ line 394 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 494 | string | display string @ line 494 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 566 | string | display string @ line 566 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 587 | string | display string @ line 587 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### provenance_scanner.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 224 | constant | V_FETCHED | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 225 | constant | V_SOURCED | 2 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 226 | constant | V_STALE | 3 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 227 | constant | V_RECALLED | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 230 | constant | C_COSMETIC | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 231 | constant | C_INTERNAL | 2 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 232 | constant | C_LOADBEARING | 3 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 233 | constant | C_PUBLIC | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 234 | constant | C_PROPAGATING | 5 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### saturn_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 53 | string | display string @ line 53 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 139 | string | display string @ line 139 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 275 | string | display string @ line 275 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 296 | string | display string @ line 296 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 500 | string | display string @ line 500 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 767 | string | display string @ line 767 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 929 | string | display string @ line 929 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 949 | string | display string @ line 949 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1222 | string | display string @ line 1222 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### scenarios_coral_bleaching.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 98 | string | display string @ line 98 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### scenarios_heatwaves.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 94 | dict | HEATWAVE_THRESHOLDS[...] | (15 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 256 | string | display string @ line 256 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 312 | string | display string @ line 312 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 359 | string | display string @ line 359 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 377 | string | display string @ line 377 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 428 | string | display string @ line 428 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 500 | string | display string @ line 500 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 520 | string | display string @ line 520 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### scenarios_western_heatwave_march_2026.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 61 | dict | WESTERN_HEATWAVE_THRESHOLDS[...] | (15 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 705 | string | display string @ line 705 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### sgr_a_grand_tour.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 45 | constant | ANIMATION_FRAMES | 140 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 46 | constant | POINTS_PER_ORBIT | 80 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 62 | constant | REFERENCE_YEAR | 2025.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 611 | string | display string @ line 611 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### sgr_a_star_data.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 52 | dict | B_STAR_TEMPERATURES[...] | (10 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 474 | string | display string @ line 474 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 495 | string | display string @ line 495 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 148 | constant | G_CONST | 6.6743e-11 | 2 | 3 | **6** | Has source citation | Numeric constant in data module |
| 149 | constant | SPEED_OF_LIGHT | 299792458.0 | 2 | 3 | **6** | Has source citation | Numeric constant in data module |
| 150 | constant | SOLAR_MASS_KG | 1.989e+30 | 2 | 3 | **6** | Has source citation | Numeric constant in data module |
| 161 | constant | PARSEC_TO_AU | 206265.0 | 2 | 3 | **6** | Has source citation | Numeric constant in data module |
| 162 | constant | YEAR_TO_SECONDS | 365.25 * 24 * 3600 | 2 | 3 | **6** | Has source citation | Numeric constant in data module |
| 168 | constant | SGR_A_MASS_SOLAR | 4154000.0 | 2 | 3 | **6** | Has source citation | Imported by 2 module(s) |
| 170 | constant | SGR_A_DISTANCE_PC | 8178.0 | 2 | 3 | **6** | Has source citation | Numeric constant in data module |
| 171 | constant | SGR_A_DISTANCE_LY | 26670.0 | 2 | 3 | **6** | Has source citation | Numeric constant in data module |

### sgr_a_visualization_precession.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 438 | string | display string @ line 438 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### smoke_dipole_cone.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 41 | constant | _TILT_EPS_DEG | 0.5 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### solar_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 49 | string | display string @ line 49 | (7 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 75 | string | display string @ line 75 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 93 | string | display string @ line 93 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 108 | string | display string @ line 108 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 123 | string | display string @ line 123 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 148 | string | display string @ line 148 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 173 | string | display string @ line 173 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 198 | string | display string @ line 198 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 231 | string | display string @ line 231 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 326 | string | display string @ line 326 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 359 | string | display string @ line 359 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 423 | string | display string @ line 423 | (6 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 538 | string | display string @ line 538 | (7 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 560 | string | display string @ line 560 | (8 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 603 | string | display string @ line 603 | (17 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 632 | string | display string @ line 632 | (14 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 658 | string | display string @ line 658 | (6 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 686 | string | display string @ line 686 | (6 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 709 | string | display string @ line 709 | (7 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### spacecraft_encounters.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 67 | constant | AU_KM | 149597870.7 | 3 | 3 | **9** | Sourced but potentially stale | Numeric constant in data module |
| 1 | string | display string @ line 1 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 143 | string | display string @ line 143 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 169 | string | display string @ line 169 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 213 | string | display string @ line 213 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1490 | string | display string @ line 1490 | (7 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1506 | string | display string @ line 1506 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### star_notes.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 116 | string | display string @ line 116 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 160 | string | display string @ line 160 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 207 | string | display string @ line 207 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 225 | string | display string @ line 225 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 239 | string | display string @ line 239 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 278 | string | display string @ line 278 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 507 | string | display string @ line 507 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 543 | string | display string @ line 543 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 560 | string | display string @ line 560 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 611 | string | display string @ line 611 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 635 | string | display string @ line 635 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 675 | string | display string @ line 675 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1046 | string | display string @ line 1046 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1121 | string | display string @ line 1121 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1189 | string | display string @ line 1189 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### star_sphere_builder.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 76 | string | display string @ line 76 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### test_reset_completeness.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 40 | dict | ENTRY_DEFAULTS[...] | (10 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### uranus_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 36 | string | display string @ line 36 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 51 | string | display string @ line 51 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 121 | string | display string @ line 121 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 181 | string | display string @ line 181 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 200 | string | display string @ line 200 | (8 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 358 | string | display string @ line 358 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 377 | string | display string @ line 377 | (9 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 446 | string | display string @ line 446 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 801 | string | display string @ line 801 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 845 | string | display string @ line 845 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 861 | string | display string @ line 861 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 879 | string | display string @ line 879 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 896 | string | display string @ line 896 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 914 | string | display string @ line 914 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 933 | string | display string @ line 933 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 951 | string | display string @ line 951 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 971 | string | display string @ line 971 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 990 | string | display string @ line 990 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1010 | string | display string @ line 1010 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1143 | string | display string @ line 1143 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1162 | string | display string @ line 1162 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### venus_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 38 | string | display string @ line 38 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 55 | string | display string @ line 55 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 417 | string | display string @ line 417 | (12 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 505 | string | display string @ line 505 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 649 | string | display string @ line 649 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### visualization_3d.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 722 | string | display string @ line 722 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 745 | string | display string @ line 745 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 782 | string | display string @ line 782 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

---

## Tier 4: NO ACTION NEEDED (Score 1-4)

### asteroid_belt_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 108 | constant | MAIN_BELT_INNER | 2.2 | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |
| 109 | constant | MAIN_BELT_OUTER | 3.2 | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |
| 110 | constant | MAIN_BELT_PEAK | 2.7 | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |
| 112 | constant | HILDA_DISTANCE | 3.97 | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |
| 113 | constant | TROJAN_DISTANCE | 5.2 | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |

### close_approach_data.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 65 | dict | CAD_BODY_NAMES[...] | (11 entries) | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |

### dep_trace.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 59 | dict | CATEGORY_COLORS[...] | (10 entries) | 4 | 1 | **4** | No source citation (recalled) | Cosmetic dictionary (CATEGORY_COLORS) |

### exoplanet_systems.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 38 | dict | TRAPPIST1_SYSTEM[...] | (6 entries) | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |
| 324 | dict | TOI1338_SYSTEM[...] | (6 entries) | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |
| 483 | dict | PROXIMA_SYSTEM[...] | (6 entries) | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |

### food_insecurity_generator.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 107 | constant | P5_DOT_MIN_SCALE | 0.5 | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |
| 108 | constant | P5_DOT_MAX_SCALE | 1.8 | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |

### palomas_orrery_dashboard.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 218 | dict | SECTION_SYMBOLS[...] | (4 entries) | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |

### scenarios_coral_bleaching.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 165 | dict | CORAL_THRESHOLDS[...] | (16 entries) | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |

### smoke_rotation_axis.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 40 | dict | OBLIQ[...] | (11 entries) | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |

### star_sphere_builder.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 29 | constant | VMAG_LIMIT | 3.5 | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |
| 43 | constant | OBLIQUITY_DEG | 23.4393 | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |
| 62 | constant | CIRCLE_POINTS | 120 | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |

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
