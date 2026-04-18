# Paloma's Orrery -- Provenance Audit

Generated: April 18, 2026
Files scanned: 102
Total findings: 541
Constants: 62 | Dicts: 30 | Display strings: 449

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
- 10-15: FIX NEXT SESSION
- 5-9: ADD SOURCE WHEN TOUCHED
- 1-4: NO ACTION NEEDED

---

## Priority Summary

| Tier | Score | Action | Count |
|------|-------|--------|------:|
| 1 | 16-20 | FIX NOW | 16 |
| 2 | 10-15 | FIX NEXT SESSION | 158 |
| 3 | 5-9 | ADD SOURCE WHEN TOUCHED | 352 |
| 4 | 1-4 | NO ACTION NEEDED | 15 |

---

## INCONSISTENCIES

None detected. No same-concept constants with differing 
values found across files.

Note: this does NOT rule out silent shadowing (a local 
dict with different name but overlapping keys). That 
pattern is the April 16 bug family; shadow detection 
is planned for a future session.

---

## DUPLICATES (Same value, multiple files)

Consistent values defined in multiple places rather 
than imported from one source. Consolidation candidates.

- **SPEED_OF_LIGHT_KM_S** = 299792.458 -- in constants_new.py, sgr_a_star_data.py

**Action:** Consolidate to constants_new.py and import.

---

## Tier 1: FIX NOW (Score 16-20)

### asteroid_belt_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 218 | string | display string @ line 218 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### comet_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1282 | string | display string @ line 1282 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### earth_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 649 | string | display string @ line 649 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### jupiter_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### neptune_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 647 | string | display string @ line 647 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 679 | string | display string @ line 679 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 903 | string | display string @ line 903 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### sgr_a_star_data.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 657 | string | display string @ line 657 | (2 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 664 | string | display string @ line 664 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### solar_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1237 | string | display string @ line 1237 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1270 | string | display string @ line 1270 | (5 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1497 | string | display string @ line 1497 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1621 | string | display string @ line 1621 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1672 | string | display string @ line 1672 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |
| 1712 | string | display string @ line 1712 | (1 claim) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

### star_notes.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (4 claims) | 4 | 4 | **16** | No source citation (recalled) | Public-facing display string (hover/INFO) |

---

## Tier 2: FIX NEXT SESSION (Score 10-15)

### apsidal_markers.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1796 | constant | ENCOUNTER_THRESHOLD_AU | 0.5 | 4 | 3 | **12** | No source citation (recalled) | Numeric constant in computation module |

### celestial_objects.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 620 | string | display string @ line 620 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 639 | string | display string @ line 639 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 655 | string | display string @ line 655 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 662 | string | display string @ line 662 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |

### comet_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 34 | dict | COMET_NUCLEUS_SIZES[...] | (16 entries) | 4 | 3 | **12** | No source citation (recalled) | Geometry dict in rendering/shells module |
| 323 | string | display string @ line 323 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1125 | string | display string @ line 1125 | (3 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 1517 | dict | COMET_FEATURE_THRESHOLDS[...] | (3 entries) | 4 | 3 | **12** | No source citation (recalled) | Imported by 1 module(s) |

### constants_new.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 47 | constant | KM_PER_AU | 149597870.7 | 2 | 5 | **10** | Has source citation | Imported by 9 modules |
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
| 241 | dict | CENTER_BODY_RADII[...] | (17 entries) | 2 | 5 | **10** | Has source citation | Imported by 8 modules |
| 262 | dict | KNOWN_ORBITAL_PERIODS[...] | (132 entries) | 2 | 5 | **10** | Has source citation | Imported by 8 modules |

### earth_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 868 | string | display string @ line 868 | (6 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 882 | string | display string @ line 882 | (7 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 934 | string | display string @ line 934 | (5 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |

### eris_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 417 | string | display string @ line 417 | (5 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |

### info_dictionary.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
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
| 634 | string | display string @ line 634 | (9 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 657 | string | display string @ line 657 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 686 | string | display string @ line 686 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 699 | string | display string @ line 699 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 719 | string | display string @ line 719 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 722 | string | display string @ line 722 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 726 | string | display string @ line 726 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 728 | string | display string @ line 728 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 733 | string | display string @ line 733 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 739 | string | display string @ line 739 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 743 | string | display string @ line 743 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 747 | string | display string @ line 747 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 752 | string | display string @ line 752 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 809 | string | display string @ line 809 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 830 | string | display string @ line 830 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 843 | string | display string @ line 843 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 846 | string | display string @ line 846 | (11 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 875 | string | display string @ line 875 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 879 | string | display string @ line 879 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 882 | string | display string @ line 882 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 885 | string | display string @ line 885 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 888 | string | display string @ line 888 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 892 | string | display string @ line 892 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 897 | string | display string @ line 897 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 900 | string | display string @ line 900 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 927 | string | display string @ line 927 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 935 | string | display string @ line 935 | (5 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 943 | string | display string @ line 943 | (8 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 975 | string | display string @ line 975 | (5 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 990 | string | display string @ line 990 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1116 | string | display string @ line 1116 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1133 | string | display string @ line 1133 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1136 | string | display string @ line 1136 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1153 | string | display string @ line 1153 | (5 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1173 | string | display string @ line 1173 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1290 | string | display string @ line 1290 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1300 | string | display string @ line 1300 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1304 | string | display string @ line 1304 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1334 | string | display string @ line 1334 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1348 | string | display string @ line 1348 | (4 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1386 | string | display string @ line 1386 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1426 | string | display string @ line 1426 | (11 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1445 | string | display string @ line 1445 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1476 | string | display string @ line 1476 | (7 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1525 | string | display string @ line 1525 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1529 | string | display string @ line 1529 | (4 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1556 | string | display string @ line 1556 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1560 | string | display string @ line 1560 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1600 | string | display string @ line 1600 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1658 | string | display string @ line 1658 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1662 | string | display string @ line 1662 | (18 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1775 | string | display string @ line 1775 | (7 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1827 | string | display string @ line 1827 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1831 | string | display string @ line 1831 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1838 | string | display string @ line 1838 | (6 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1865 | string | display string @ line 1865 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1875 | string | display string @ line 1875 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1886 | string | display string @ line 1886 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1898 | string | display string @ line 1898 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 1909 | string | display string @ line 1909 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2007 | string | display string @ line 2007 | (4 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2022 | string | display string @ line 2022 | (5 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2040 | string | display string @ line 2040 | (4 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2052 | string | display string @ line 2052 | (27 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2097 | string | display string @ line 2097 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2116 | string | display string @ line 2116 | (7 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 2140 | string | display string @ line 2140 | (1 claim) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 2143 | string | display string @ line 2143 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2144 | string | display string @ line 2144 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2145 | string | display string @ line 2145 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2146 | string | display string @ line 2146 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2147 | string | display string @ line 2147 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2148 | string | display string @ line 2148 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2149 | string | display string @ line 2149 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2150 | string | display string @ line 2150 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2154 | string | display string @ line 2154 | (8 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 2181 | string | display string @ line 2181 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 104 | dict | object_type_mapping[...] | (79 entries) | 2 | 5 | **10** | Has source citation | Imported by 6 modules |
| 240 | dict | class_mapping[...] | (14 entries) | 2 | 5 | **10** | Has source citation | Imported by 5 modules |

### mercury_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 586 | string | display string @ line 586 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |

### module_atlas.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 43 | dict | ROLE_MAP[...] | (94 entries) | 4 | 3 | **12** | No source citation (recalled) | Imported by 1 module(s) |

### orbital_elements.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1420 | dict | planet_tilts[...] | (7 entries) | 4 | 3 | **12** | No source citation (recalled) | Imported by 1 module(s) |

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
| 249 | string | display string @ line 249 | (8 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 270 | string | display string @ line 270 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 303 | string | display string @ line 303 | (6 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 875 | string | display string @ line 875 | (19 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 899 | string | display string @ line 899 | (5 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 934 | string | display string @ line 934 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 939 | string | display string @ line 939 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 945 | string | display string @ line 945 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 951 | string | display string @ line 951 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 956 | string | display string @ line 956 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 961 | string | display string @ line 961 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |

### spacecraft_encounters.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 112 | string | display string @ line 112 | (5 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 204 | string | display string @ line 204 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 213 | string | display string @ line 213 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 235 | string | display string @ line 235 | (2 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 266 | string | display string @ line 266 | (5 claims) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |

### star_notes.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 21 | dict | unique_notes[...] | (553 entries) | 3 | 5 | **15** | Sourced but potentially stale | Imported by 5 modules |
| 320 | string | display string @ line 320 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 347 | string | display string @ line 347 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 400 | string | display string @ line 400 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 427 | string | display string @ line 427 | (2 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 480 | string | display string @ line 480 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 741 | string | display string @ line 741 | (1 claim) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |
| 756 | string | display string @ line 756 | (1 claim) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 769 | string | display string @ line 769 | (1 claim) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 782 | string | display string @ line 782 | (1 claim) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 795 | string | display string @ line 795 | (1 claim) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 808 | string | display string @ line 808 | (1 claim) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 835 | string | display string @ line 835 | (1 claim) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 897 | string | display string @ line 897 | (1 claim) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 926 | string | display string @ line 926 | (1 claim) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 973 | string | display string @ line 973 | (1 claim) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 1031 | string | display string @ line 1031 | (3 claims) | 3 | 4 | **12** | Sourced but potentially stale | Public-facing display string (hover/INFO) |

### star_sphere_builder.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 493 | dict | CONSTELLATION_NAMES[...] | (88 entries) | 4 | 3 | **12** | No source citation (recalled) | Geometry dict in rendering module |

### uranus_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 534 | string | display string @ line 534 | (1 claim) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |
| 563 | string | display string @ line 563 | (1 claim) | 3 | 4 | **12** | No source, contains date-sensitive claims | Public-facing display string (hover/INFO) |

---

## Tier 3: ADD SOURCE WHEN TOUCHED (Score 5-9)

### add_docstrings.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 31 | dict | DOCSTRINGS[...] | (42 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### asteroid_belt_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 79 | string | display string @ line 79 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 134 | string | display string @ line 134 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 259 | string | display string @ line 259 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 314 | string | display string @ line 314 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 356 | string | display string @ line 356 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 411 | string | display string @ line 411 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 453 | string | display string @ line 453 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 508 | string | display string @ line 508 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

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
| 446 | string | display string @ line 446 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 500 | string | display string @ line 500 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 563 | string | display string @ line 563 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 902 | string | display string @ line 902 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 907 | string | display string @ line 907 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 912 | string | display string @ line 912 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 917 | string | display string @ line 917 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1037 | string | display string @ line 1037 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1042 | string | display string @ line 1042 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1097 | string | display string @ line 1097 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1104 | string | display string @ line 1104 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1111 | string | display string @ line 1111 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1118 | string | display string @ line 1118 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1125 | string | display string @ line 1125 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1131 | string | display string @ line 1131 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1137 | string | display string @ line 1137 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1147 | string | display string @ line 1147 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1155 | string | display string @ line 1155 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1163 | string | display string @ line 1163 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1171 | string | display string @ line 1171 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1179 | string | display string @ line 1179 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1187 | string | display string @ line 1187 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1195 | string | display string @ line 1195 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1203 | string | display string @ line 1203 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1222 | string | display string @ line 1222 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1245 | string | display string @ line 1245 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1253 | string | display string @ line 1253 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### close_approach_data.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### comet_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 82 | string | display string @ line 82 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 198 | string | display string @ line 198 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 224 | string | display string @ line 224 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 245 | string | display string @ line 245 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 272 | string | display string @ line 272 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 283 | string | display string @ line 283 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 294 | string | display string @ line 294 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 510 | string | display string @ line 510 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 516 | string | display string @ line 516 | (8 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 523 | string | display string @ line 523 | (16 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 683 | string | display string @ line 683 | (14 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1451 | string | display string @ line 1451 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1461 | string | display string @ line 1461 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1471 | string | display string @ line 1471 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1480 | string | display string @ line 1480 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1489 | string | display string @ line 1489 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1499 | string | display string @ line 1499 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1449 | dict | comet_visualization_info[...] | (6 entries) | 2 | 3 | **6** | Has source citation | Geometry dict in rendering/shells module |

### constants_new.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 54 | constant | SUN_RADIUS_KM | 695700.0 | 2 | 3 | **6** | Has source citation | Imported by 2 module(s) |
| 63 | constant | EARTH_EQUATORIAL_RADIUS_KM | 6378.137 | 2 | 3 | **6** | Has source citation | Imported by 1 module(s) |
| 69 | constant | EARTH_POLAR_RADIUS_KM | 6356.752 | 2 | 3 | **6** | Has source citation | Imported by 1 module(s) |
| 74 | constant | JUPITER_EQUATORIAL_RADIUS_KM | 71492.0 | 2 | 3 | **6** | Has source citation | Imported by 1 module(s) |
| 79 | constant | JUPITER_POLAR_RADIUS_KM | 66854.0 | 2 | 3 | **6** | Has source citation | Imported by 1 module(s) |
| 84 | constant | SPEED_OF_LIGHT_KM_S | 299792.458 | 2 | 3 | **6** | Has source citation | Imported by 1 module(s) |
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
| 28 | string | display string @ line 28 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 44 | string | display string @ line 44 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 86 | string | display string @ line 86 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 102 | string | display string @ line 102 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 144 | string | display string @ line 144 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 159 | string | display string @ line 159 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 200 | string | display string @ line 200 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 215 | string | display string @ line 215 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 256 | string | display string @ line 256 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 271 | string | display string @ line 271 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 415 | string | display string @ line 415 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 431 | string | display string @ line 431 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 473 | string | display string @ line 473 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 489 | string | display string @ line 489 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 539 | string | display string @ line 539 | (7 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 594 | string | display string @ line 594 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 681 | string | display string @ line 681 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 683 | string | display string @ line 683 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 761 | string | display string @ line 761 | (11 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 781 | string | display string @ line 781 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 834 | string | display string @ line 834 | (11 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 969 | string | display string @ line 969 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 992 | string | display string @ line 992 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### eris_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 46 | string | display string @ line 46 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 168 | string | display string @ line 168 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 434 | string | display string @ line 434 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### info_dictionary.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 259 | dict | INFO[...] | (181 entries) | 3 | 3 | **9** | Sourced but potentially stale | Imported by 2 module(s) |
| 1 | string | display string @ line 1 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 35 | string | display string @ line 35 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 499 | string | display string @ line 499 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 515 | string | display string @ line 515 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 524 | string | display string @ line 524 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 557 | string | display string @ line 557 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 591 | string | display string @ line 591 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 605 | string | display string @ line 605 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 619 | string | display string @ line 619 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 769 | string | display string @ line 769 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 904 | string | display string @ line 904 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 909 | string | display string @ line 909 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 913 | string | display string @ line 913 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 923 | string | display string @ line 923 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1011 | string | display string @ line 1011 | (8 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1034 | string | display string @ line 1034 | (7 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1053 | string | display string @ line 1053 | (6 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1070 | string | display string @ line 1070 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1080 | string | display string @ line 1080 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1083 | string | display string @ line 1083 | (7 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1090 | string | display string @ line 1090 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1098 | string | display string @ line 1098 | (8 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1225 | string | display string @ line 1225 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1229 | string | display string @ line 1229 | (6 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1734 | string | display string @ line 1734 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1918 | string | display string @ line 1918 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1958 | string | display string @ line 1958 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1988 | string | display string @ line 1988 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 2191 | string | display string @ line 2191 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 2201 | string | display string @ line 2201 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 2202 | string | display string @ line 2202 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 2203 | string | display string @ line 2203 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### jupiter_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 68 | string | display string @ line 68 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 84 | string | display string @ line 84 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 125 | string | display string @ line 125 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 140 | string | display string @ line 140 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 181 | string | display string @ line 181 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 197 | string | display string @ line 197 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 239 | string | display string @ line 239 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 257 | string | display string @ line 257 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 402 | string | display string @ line 402 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 420 | string | display string @ line 420 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 610 | string | display string @ line 610 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 706 | string | display string @ line 706 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 720 | string | display string @ line 720 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 818 | string | display string @ line 818 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 833 | string | display string @ line 833 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 848 | string | display string @ line 848 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 862 | string | display string @ line 862 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 926 | string | display string @ line 926 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### mars_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 447 | string | display string @ line 447 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 468 | string | display string @ line 468 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 522 | string | display string @ line 522 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 633 | string | display string @ line 633 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 757 | string | display string @ line 757 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### mercury_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 80 | string | display string @ line 80 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 93 | string | display string @ line 93 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 185 | string | display string @ line 185 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 201 | string | display string @ line 201 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 343 | string | display string @ line 343 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 419 | string | display string @ line 419 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 541 | string | display string @ line 541 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 714 | string | display string @ line 714 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### module_atlas.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 177 | dict | ROLE_DESCRIPTIONS[...] | (12 entries) | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### moon_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 42 | string | display string @ line 42 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 96 | string | display string @ line 96 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 142 | string | display string @ line 142 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 163 | string | display string @ line 163 | (8 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 469 | string | display string @ line 469 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### neptune_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 90 | string | display string @ line 90 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 109 | string | display string @ line 109 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 160 | string | display string @ line 160 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 424 | string | display string @ line 424 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 526 | string | display string @ line 526 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 836 | string | display string @ line 836 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 858 | string | display string @ line 858 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 880 | string | display string @ line 880 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1193 | string | display string @ line 1193 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1226 | string | display string @ line 1226 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1256 | string | display string @ line 1256 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1286 | string | display string @ line 1286 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1316 | string | display string @ line 1316 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1346 | string | display string @ line 1346 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1379 | string | display string @ line 1379 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1411 | string | display string @ line 1411 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1443 | string | display string @ line 1443 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1475 | string | display string @ line 1475 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1507 | string | display string @ line 1507 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1537 | string | display string @ line 1537 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1693 | string | display string @ line 1693 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1713 | string | display string @ line 1713 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

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
| 2920 | constant | BUTTON_WIDTH | 14 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### palomas_orrery_dashboard.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 36 | constant | WINDOW_WIDTH | 960 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 37 | constant | WINDOW_HEIGHT | 720 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### planet9_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 29 | string | display string @ line 29 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 49 | string | display string @ line 49 | (8 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 212 | string | display string @ line 212 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 232 | string | display string @ line 232 | (11 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### pluto_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 27 | string | display string @ line 27 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 44 | string | display string @ line 44 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 100 | string | display string @ line 100 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 117 | string | display string @ line 117 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 166 | string | display string @ line 166 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 339 | string | display string @ line 339 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 360 | string | display string @ line 360 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 425 | string | display string @ line 425 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 446 | string | display string @ line 446 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 511 | string | display string @ line 511 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 532 | string | display string @ line 532 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### provenance_scanner.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 86 | constant | V_FETCHED | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 87 | constant | V_SOURCED | 2 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 88 | constant | V_STALE | 3 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 89 | constant | V_RECALLED | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 92 | constant | C_COSMETIC | 1 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 93 | constant | C_INTERNAL | 2 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 94 | constant | C_LOADBEARING | 3 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 95 | constant | C_PUBLIC | 4 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |
| 96 | constant | C_PROPAGATING | 5 | 4 | 2 | **8** | No source citation (recalled) | Internal use (not imported externally) |

### saturn_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 79 | string | display string @ line 79 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 151 | string | display string @ line 151 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 259 | string | display string @ line 259 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 280 | string | display string @ line 280 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 490 | string | display string @ line 490 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 707 | string | display string @ line 707 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 887 | string | display string @ line 887 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 907 | string | display string @ line 907 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1172 | string | display string @ line 1172 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

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
| 475 | string | display string @ line 475 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 496 | string | display string @ line 496 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 148 | constant | G_CONST | 6.6743e-11 | 2 | 3 | **6** | Has source citation | Numeric constant in data module |
| 149 | constant | SPEED_OF_LIGHT | 299792458.0 | 2 | 3 | **6** | Has source citation | Numeric constant in data module |
| 150 | constant | SPEED_OF_LIGHT_KM_S | 299792.458 | 2 | 3 | **6** | Has source citation | Numeric constant in data module |
| 151 | constant | SOLAR_MASS_KG | 1.989e+30 | 2 | 3 | **6** | Has source citation | Numeric constant in data module |
| 162 | constant | PARSEC_TO_AU | 206265.0 | 2 | 3 | **6** | Has source citation | Numeric constant in data module |
| 163 | constant | YEAR_TO_SECONDS | 365.25 * 24 * 3600 | 2 | 3 | **6** | Has source citation | Numeric constant in data module |
| 169 | constant | SGR_A_MASS_SOLAR | 4154000.0 | 2 | 3 | **6** | Has source citation | Imported by 2 module(s) |
| 171 | constant | SGR_A_DISTANCE_PC | 8178.0 | 2 | 3 | **6** | Has source citation | Numeric constant in data module |
| 172 | constant | SGR_A_DISTANCE_LY | 26670.0 | 2 | 3 | **6** | Has source citation | Numeric constant in data module |

### solar_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 45 | string | display string @ line 45 | (7 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 72 | string | display string @ line 72 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 90 | string | display string @ line 90 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 106 | string | display string @ line 106 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 122 | string | display string @ line 122 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 148 | string | display string @ line 148 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 174 | string | display string @ line 174 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 200 | string | display string @ line 200 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 234 | string | display string @ line 234 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 333 | string | display string @ line 333 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 367 | string | display string @ line 367 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 430 | string | display string @ line 430 | (6 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 454 | string | display string @ line 454 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 472 | string | display string @ line 472 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 487 | string | display string @ line 487 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 503 | string | display string @ line 503 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 536 | string | display string @ line 536 | (4 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 550 | string | display string @ line 550 | (7 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 573 | string | display string @ line 573 | (8 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 595 | string | display string @ line 595 | (7 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 619 | string | display string @ line 619 | (17 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 649 | string | display string @ line 649 | (14 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 676 | string | display string @ line 676 | (6 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 705 | string | display string @ line 705 | (6 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 729 | string | display string @ line 729 | (7 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 753 | string | display string @ line 753 | (6 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 782 | string | display string @ line 782 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 815 | string | display string @ line 815 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1306 | string | display string @ line 1306 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1760 | string | display string @ line 1760 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### spacecraft_encounters.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 65 | constant | AU_KM | 149597870.7 | 3 | 3 | **9** | Sourced but potentially stale | Numeric constant in data module |
| 1 | string | display string @ line 1 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 141 | string | display string @ line 141 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 167 | string | display string @ line 167 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1396 | string | display string @ line 1396 | (7 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1412 | string | display string @ line 1412 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### star_notes.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 24 | string | display string @ line 24 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 71 | string | display string @ line 71 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 125 | string | display string @ line 125 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 169 | string | display string @ line 169 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 216 | string | display string @ line 216 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 234 | string | display string @ line 234 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 248 | string | display string @ line 248 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 287 | string | display string @ line 287 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 552 | string | display string @ line 552 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 569 | string | display string @ line 569 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 623 | string | display string @ line 623 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 648 | string | display string @ line 648 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 689 | string | display string @ line 689 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1050 | string | display string @ line 1050 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1126 | string | display string @ line 1126 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1196 | string | display string @ line 1196 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### uranus_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 36 | string | display string @ line 36 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 53 | string | display string @ line 53 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 111 | string | display string @ line 111 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 158 | string | display string @ line 158 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 178 | string | display string @ line 178 | (8 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 343 | string | display string @ line 343 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 362 | string | display string @ line 362 | (9 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 425 | string | display string @ line 425 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 480 | string | display string @ line 480 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 736 | string | display string @ line 736 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 780 | string | display string @ line 780 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 797 | string | display string @ line 797 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 815 | string | display string @ line 815 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 833 | string | display string @ line 833 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 852 | string | display string @ line 852 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 875 | string | display string @ line 875 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 893 | string | display string @ line 893 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 913 | string | display string @ line 913 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 933 | string | display string @ line 933 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 955 | string | display string @ line 955 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 991 | string | display string @ line 991 | (5 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1094 | string | display string @ line 1094 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 1114 | string | display string @ line 1114 | (3 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

### venus_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 1 | string | display string @ line 1 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 29 | string | display string @ line 29 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 46 | string | display string @ line 46 | (2 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 372 | string | display string @ line 372 | (12 claims) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 457 | string | display string @ line 457 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 506 | string | display string @ line 506 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |
| 665 | string | display string @ line 665 | (1 claim) | 2 | 4 | **8** | Has source citation | Public-facing display string (hover/INFO) |

---

## Tier 4: NO ACTION NEEDED (Score 1-4)

### asteroid_belt_visualization_shells.py

| Line | Kind | Name | Size/Value | V | C | Score | Vulnerability | Criticality |
|-----:|------|------|------------|--:|--:|------:|---------------|-------------|
| 110 | constant | MAIN_BELT_INNER | 2.2 | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |
| 111 | constant | MAIN_BELT_OUTER | 3.2 | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |
| 112 | constant | MAIN_BELT_PEAK | 2.7 | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |
| 114 | constant | HILDA_DISTANCE | 3.97 | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |
| 115 | constant | TROJAN_DISTANCE | 5.2 | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |

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
| 177 | dict | SECTION_SYMBOLS[...] | (4 entries) | 2 | 2 | **4** | Has source citation | Internal use (not imported externally) |

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
