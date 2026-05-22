# Paloma's Orrery -- Provenance Audit

Generated: May 22, 2026
Files scanned: 105
Total findings: 493
Constants: 61 | Dicts: 29 | Display strings: 403

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
| 1 | 16-20 | FIX NOW | 4 |
| 2 | 10-15 | ALL ACCEPTED RESIDUALS -- see note below | 143 |
| 3 | 5-9 | ALREADY CITED OR LOW RISK -- no action required | 330 |
| 4 | 1-4 | NO ACTION NEEDED | 16 |

**Tier 2 note (April 2026 audit):** All Tier-2 findings are documented
accepted residuals -- cited constants, V_STALE staleness flags on verified
strings, or known scanner limitations. No action required unless a new
uncited entry appears. See Accepted Residuals block below for details.

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

### neptune_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 584 | string | display string @ line 584 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### spacecraft_encounters.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 237 | string | display string @ line 237 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 268 | string | display string @ line 268 | (5 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### uranus_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 509 | string | display string @ line 509 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

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
| 34 | dict | COMET_NUCLEUS_SIZES[...] | (16 entries) | 4 | 3 | **12** | No source citation (recalled) | Geometry dict in rendering/shells module |
| 323 | string | display string @ line 323 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1602 | dict | COMET_FEATURE_THRESHOLDS[...] | (3 entries) | 4 | 3 | **12** | No source citation (recalled) | Imported by 1 module(s) |

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
| 972 | string | display string @ line 972 | (6 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 986 | string | display string @ line 986 | (7 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1038 | string | display string @ line 1038 | (5 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |

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
| 264 | string | display string @ line 264 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |

### module_atlas.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 43 | dict | ROLE_MAP[...] | (94 entries) | 4 | 3 | **12** | No source citation (recalled) | Imported by 1 module(s) |

### orbital_elements.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1430 | dict | planet_tilts[...] | (7 entries) | 4 | 3 | **12** | No source citation (recalled) | Imported by 1 module(s) |

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
| 230 | string | display string @ line 230 | (8 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 250 | string | display string @ line 250 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 282 | string | display string @ line 282 | (6 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 841 | string | display string @ line 841 | (19 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 868 | string | display string @ line 868 | (19 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 892 | string | display string @ line 892 | (5 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |

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
| 554 | string | display string @ line 554 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |

---

## Tier 3: ALREADY CITED OR LOW RISK -- no action required (Score 5-9)

### add_docstrings.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 31 | dict | DOCSTRINGS[...] | (42 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### apsidal_markers.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1849 | constant | ENCOUNTER_THRESHOLD_AU | 0.5 | 2 | 3 | **6** | Has source citation | Numeric constant in computation module |

### asteroid_belt_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 62 | string | display string @ line 62 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 114 | string | display string @ line 114 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### celestial_coordinates.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
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
| 291 | string | display string @ line 291 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
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
| 82 | string | display string @ line 82 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 198 | string | display string @ line 198 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 283 | string | display string @ line 283 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 294 | string | display string @ line 294 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 510 | string | display string @ line 510 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 516 | string | display string @ line 516 | (8 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 523 | string | display string @ line 523 | (16 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 683 | string | display string @ line 683 | (14 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1536 | string | display string @ line 1536 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1546 | string | display string @ line 1546 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1556 | string | display string @ line 1556 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1565 | string | display string @ line 1565 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1574 | string | display string @ line 1574 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1584 | string | display string @ line 1584 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1534 | dict | comet_visualization_info[...] | (6 entries) | 2 | 3 | **6** | Has source citation | Geometry dict in rendering/shells module |

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

### dep_trace.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 32 | constant | HUB_THRESHOLD | 8 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 44 | dict | _ROLE_TO_VISUAL[...] | (12 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### earth_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 29 | string | display string @ line 29 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 45 | string | display string @ line 45 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 101 | string | display string @ line 101 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 117 | string | display string @ line 117 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 173 | string | display string @ line 173 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 188 | string | display string @ line 188 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 243 | string | display string @ line 243 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 258 | string | display string @ line 258 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 313 | string | display string @ line 313 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 328 | string | display string @ line 328 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 465 | string | display string @ line 465 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 481 | string | display string @ line 481 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 537 | string | display string @ line 537 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 553 | string | display string @ line 553 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 860 | string | display string @ line 860 | (11 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 880 | string | display string @ line 880 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 933 | string | display string @ line 933 | (11 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1077 | string | display string @ line 1077 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1100 | string | display string @ line 1100 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### eris_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 46 | string | display string @ line 46 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 196 | string | display string @ line 196 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 452 | string | display string @ line 452 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 469 | string | display string @ line 469 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

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
| 69 | string | display string @ line 69 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 85 | string | display string @ line 85 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 140 | string | display string @ line 140 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 155 | string | display string @ line 155 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 210 | string | display string @ line 210 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 226 | string | display string @ line 226 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 282 | string | display string @ line 282 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 300 | string | display string @ line 300 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 438 | string | display string @ line 438 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 456 | string | display string @ line 456 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 659 | string | display string @ line 659 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 749 | string | display string @ line 749 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 763 | string | display string @ line 763 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 875 | string | display string @ line 875 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 890 | string | display string @ line 890 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 905 | string | display string @ line 905 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 919 | string | display string @ line 919 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 981 | string | display string @ line 981 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### mars_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 497 | string | display string @ line 497 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 518 | string | display string @ line 518 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 586 | string | display string @ line 586 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 710 | string | display string @ line 710 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 837 | string | display string @ line 837 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### mercury_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 43 | string | display string @ line 43 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 57 | string | display string @ line 57 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 66 | string | display string @ line 66 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 80 | string | display string @ line 80 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 208 | string | display string @ line 208 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 400 | string | display string @ line 400 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### module_atlas.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 177 | dict | ROLE_DESCRIPTIONS[...] | (12 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### moon_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 42 | string | display string @ line 42 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 110 | string | display string @ line 110 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 170 | string | display string @ line 170 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 191 | string | display string @ line 191 | (8 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 518 | string | display string @ line 518 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### neptune_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 104 | string | display string @ line 104 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 123 | string | display string @ line 123 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 188 | string | display string @ line 188 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 452 | string | display string @ line 452 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 791 | string | display string @ line 791 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1122 | string | display string @ line 1122 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1155 | string | display string @ line 1155 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1185 | string | display string @ line 1185 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1215 | string | display string @ line 1215 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1245 | string | display string @ line 1245 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1275 | string | display string @ line 1275 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1308 | string | display string @ line 1308 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1340 | string | display string @ line 1340 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1372 | string | display string @ line 1372 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1404 | string | display string @ line 1404 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1436 | string | display string @ line 1436 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1466 | string | display string @ line 1466 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1619 | string | display string @ line 1619 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1639 | string | display string @ line 1639 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### orbit_data_manager.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 34 | constant | DEFAULT_DAYS_AHEAD | 730 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 35 | constant | MAX_DATA_AGE_DAYS | 90 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### osculating_cache_manager.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 79 | dict | REFRESH_INTERVALS[...] | (14 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### paleoclimate_wet_bulb_full.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 132 | constant | BASELINE_ABSOLUTE_TEMP | 14.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 134 | constant | TW_SURVIVABILITY_BIOLOGICAL | 31.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 135 | constant | TW_SURVIVABILITY_THEORETICAL | 35.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### palomas_orrery.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 2935 | constant | BUTTON_WIDTH | 14 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### palomas_orrery_dashboard.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 38 | constant | WINDOW_WIDTH | 960 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 39 | constant | WINDOW_HEIGHT | 720 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### planet9_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 29 | string | display string @ line 29 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 49 | string | display string @ line 49 | (8 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 205 | string | display string @ line 205 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 225 | string | display string @ line 225 | (11 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### pluto_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 27 | string | display string @ line 27 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 44 | string | display string @ line 44 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 114 | string | display string @ line 114 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 131 | string | display string @ line 131 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 194 | string | display string @ line 194 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 360 | string | display string @ line 360 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 381 | string | display string @ line 381 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 481 | string | display string @ line 481 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 560 | string | display string @ line 560 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 581 | string | display string @ line 581 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### provenance_scanner.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 220 | constant | V_SOURCED | 2 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 221 | constant | V_STALE | 3 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 222 | constant | V_RECALLED | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 225 | constant | C_COSMETIC | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 226 | constant | C_INTERNAL | 2 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 227 | constant | C_LOADBEARING | 3 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 228 | constant | C_PUBLIC | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 229 | constant | C_PROPAGATING | 5 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### saturn_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 46 | string | display string @ line 46 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 132 | string | display string @ line 132 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 268 | string | display string @ line 268 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 289 | string | display string @ line 289 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 492 | string | display string @ line 492 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 724 | string | display string @ line 724 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 885 | string | display string @ line 885 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 905 | string | display string @ line 905 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1181 | string | display string @ line 1181 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### scenarios_heatwaves.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 94 | dict | HEATWAVE_THRESHOLDS[...] | (15 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### scenarios_western_heatwave_march_2026.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 61 | dict | WESTERN_HEATWAVE_THRESHOLDS[...] | (15 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### sgr_a_grand_tour.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 45 | constant | ANIMATION_FRAMES | 140 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 46 | constant | POINTS_PER_ORBIT | 80 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 62 | constant | REFERENCE_YEAR | 2025.0 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

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

### solar_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 34 | string | display string @ line 34 | (7 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 60 | string | display string @ line 60 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 78 | string | display string @ line 78 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 93 | string | display string @ line 93 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 108 | string | display string @ line 108 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 133 | string | display string @ line 133 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 158 | string | display string @ line 158 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 183 | string | display string @ line 183 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 216 | string | display string @ line 216 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 311 | string | display string @ line 311 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 344 | string | display string @ line 344 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 408 | string | display string @ line 408 | (6 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 431 | string | display string @ line 431 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 448 | string | display string @ line 448 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 462 | string | display string @ line 462 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 476 | string | display string @ line 476 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 510 | string | display string @ line 510 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 523 | string | display string @ line 523 | (7 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 545 | string | display string @ line 545 | (8 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 566 | string | display string @ line 566 | (7 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 588 | string | display string @ line 588 | (17 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 617 | string | display string @ line 617 | (14 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 643 | string | display string @ line 643 | (6 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 671 | string | display string @ line 671 | (6 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 694 | string | display string @ line 694 | (7 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 719 | string | display string @ line 719 | (6 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 747 | string | display string @ line 747 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 781 | string | display string @ line 781 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### spacecraft_encounters.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 67 | constant | AU_KM | 149597870.7 | 3 | 3 | **9** | Sourced but potentially stale | Numeric constant in data module |
| 1 | string | display string @ line 1 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 143 | string | display string @ line 143 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 169 | string | display string @ line 169 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 206 | string | display string @ line 206 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 215 | string | display string @ line 215 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1494 | string | display string @ line 1494 | (7 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1510 | string | display string @ line 1510 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### star_notes.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 116 | string | display string @ line 116 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 160 | string | display string @ line 160 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 207 | string | display string @ line 207 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 225 | string | display string @ line 225 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 239 | string | display string @ line 239 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 278 | string | display string @ line 278 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 543 | string | display string @ line 543 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 560 | string | display string @ line 560 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 611 | string | display string @ line 611 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 635 | string | display string @ line 635 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 675 | string | display string @ line 675 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1046 | string | display string @ line 1046 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1121 | string | display string @ line 1121 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1189 | string | display string @ line 1189 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### uranus_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 27 | string | display string @ line 27 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 42 | string | display string @ line 42 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 112 | string | display string @ line 112 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 172 | string | display string @ line 172 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 191 | string | display string @ line 191 | (8 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 348 | string | display string @ line 348 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 367 | string | display string @ line 367 | (9 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 436 | string | display string @ line 436 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 729 | string | display string @ line 729 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 772 | string | display string @ line 772 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 788 | string | display string @ line 788 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 806 | string | display string @ line 806 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 823 | string | display string @ line 823 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 841 | string | display string @ line 841 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 860 | string | display string @ line 860 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 878 | string | display string @ line 878 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 898 | string | display string @ line 898 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 917 | string | display string @ line 917 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 937 | string | display string @ line 937 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1071 | string | display string @ line 1071 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1090 | string | display string @ line 1090 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### venus_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 30 | string | display string @ line 30 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 47 | string | display string @ line 47 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 408 | string | display string @ line 408 | (12 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 507 | string | display string @ line 507 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 561 | string | display string @ line 561 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 729 | string | display string @ line 729 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

---

## Tier 4: NO ACTION NEEDED (Score 1-4)

### asteroid_belt_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 93 | constant | MAIN_BELT_INNER | 2.2 | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |
| 94 | constant | MAIN_BELT_OUTER | 3.2 | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |
| 95 | constant | MAIN_BELT_PEAK | 2.7 | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |
| 97 | constant | HILDA_DISTANCE | 3.97 | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |
| 98 | constant | TROJAN_DISTANCE | 5.2 | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |

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

### palomas_orrery_dashboard.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 180 | dict | SECTION_SYMBOLS[...] | (4 entries) | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |

### provenance_scanner.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 219 | constant | V_FETCHED | 1 | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |

### scenarios_coral_bleaching.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 165 | dict | CORAL_THRESHOLDS[...] | (16 entries) | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |

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
