# Provenance Audit — Handoff v1

## Paloma's Orrery | Tony + Claude + Gemini | April 15, 2026

-----

## Origin

Tony noticed that Claude confabulated asterism line connections with full
confidence and explained away his correct visual observation. This raised
the question: how much of the codebase contains recalled-not-fetched facts
that could be wrong? ChatGPT thinking Biden was still president was funny.
Asterisms that look plausible but are wrong — and Claude arguing you out of
what your eyes see — is not.

The concern: as Tony delegates more and builds less manually, the verification
layer thins. The success of the partnership creates the conditions for the
failure mode. Trust earned on reasoning does not transfer to recall.

-----

## What We Built

### provenance_scanner.py

Companion tool to `module_atlas.py`. Scans all .py files for hardcoded
constants, dictionary values, and numeric claims in strings. Scores each
finding by **Vulnerability x Criticality** and outputs `PROVENANCE_AUDIT.md`.

Uses `module_atlas.py`'s dependency graph to auto-assess criticality:
modules imported by many others score higher (Propagating = 5).

**Vulnerability** (how likely to be wrong):
- 1 = Fetched (authoritative pipeline)
- 2 = Sourced (has `# Source:` citation)
- 3 = Stale (date-sensitive, may have changed)
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

Run: `python provenance_scanner.py`

Current results (April 15, 2026, 100 files):
- 1 inconsistency: KM_PER_AU in sgr_a_star_data.py (149600000 vs 149597870.7)
- 15 consistent duplicates (consolidation candidates)
- 5029 total findings scored across risk matrix

### info_dictionary.py (NEW)

Split from `constants_new.py` to separate narrative content from numeric
constants. Contains: INFO, object_type_mapping, class_mapping, note_text.

~2,100 lines of descriptive text that was cluttering the constants file.
These are Public-facing (Criticality = 4) but need fact-checking, not
source citations. Different verification approach from numeric constants.

### constants_new.py (RESTRUCTURED)

Reduced from 2,638 to ~690 lines. Now purely numeric with verified citations.

Architecture:
1. **Fundamental constants** (IAU-defined, exact): KM_PER_AU, SUN_RADIUS_KM,
   EARTH_EQUATORIAL_RADIUS_KM, JUPITER_EQUATORIAL_RADIUS_KM, etc.
2. **Derived constants** (computed, never hardcoded): SOLAR_RADIUS_AU,
   LIGHT_MINUTES_PER_AU, CORE_AU, RADIATIVE_ZONE_AU
3. **GUI constants** (application settings): DEFAULT_MARKER_SIZE, etc.
4. **Solar structure** (cited): all shell boundaries with `# Source:` comments
5. **New shell constants** (moved from planet_visualization_utilities.py):
   STREAMER_BELT_RADII, ROCHE_LIMIT_RADII, ALFVEN_SURFACE_RADII
6. **Body radii, orbital periods, colors**: existing dictionaries

Every propagating constant now has: `# Source:`, `# Ref:` (URL), `# Verified:` (date).

-----

## Gemini Review Findings (Mode 7 Cross-Verification)

Gemini reviewed the restructured `constants_new.py` against authoritative
sources and caught two errors Claude introduced *during the verification*:

1. **Arrokoth radius**: 0.0088 km (8.8 meters!) → 9.95 km
   - The 0.0088 value had been in the codebase since the beginning
   - ~1000x error, never caught because Arrokoth is rarely plotted with shells
   - Corrected to volumetric mean ~9.95 km (dimensions ~35x20x14 km)

2. **Parker Solar Probe closest approach**: 8.86 → 9.86 R_sun
   - Claude sourced 8.86 as surface altitude above photosphere
   - All other shell radii measure from Sun center — inconsistent
   - Correct value: 9.86 R_sun from Sun center
   - Perihelion number also wrong: was 21, actually 22

3. **HELIOPAUSE_RADII = 26449**: Gemini confirmed math is correct
   (123 AU × 149597870.7 / 695700 = 26449 R_sun)

**Key lesson**: Verification by the same AI that generated the value is not
verification. Claude confabulated Parker's distance with full confidence
while explicitly claiming to verify it. Cross-AI review is load-bearing.

-----

## Import Changes Completed

The `info_dictionary.py` split required import changes in 9 files:

| File | Change |
|------|--------|
| palomas_orrery.py | `INFO, note_text` → from info_dictionary |
| palomas_orrery_helpers.py | `INFO, note_text` → from info_dictionary |
| gallery_studio.py (2 places) | `INFO` → from info_dictionary |
| object_type_analyzer.py | `object_type_mapping` → from info_dictionary |
| star_visualization_gui.py | `object_type_mapping, class_mapping` → from info_dictionary |
| visualization_2d.py | `object_type_mapping, class_mapping` → from info_dictionary |
| visualization_3d.py | `object_type_mapping, class_mapping` → from info_dictionary |
| visualization_core.py | `object_type_mapping, class_mapping` → from info_dictionary |
| exoplanet_stellar_properties.py | `class_mapping, object_type_mapping` → from info_dictionary |

`stellar_class_labels` and `spectral_subclass_temps` stay in `constants_new.py`.

Bonus fix: duplicate `class_mapping` (lines 376 and 2618) resolved — only
the full 14-key version (with sub-types 0, Ia+, Ia, Iab, Ib, sd, D) lives
in `info_dictionary.py`.

-----

## Value Changes from Verification

| Constant | Old | New | Reason |
|----------|-----|-----|--------|
| CENTER_BODY_RADII['Sun'] | 696340 | 695700 | IAU 2015 nominal (was photospheric measurement) |
| CENTER_BODY_RADII['Mercury'] | 2440 | 2439.7 | NASA Fact Sheet volumetric mean |
| CENTER_BODY_RADII['Venus'] | 6052 | 6051.8 | NASA Fact Sheet volumetric mean |
| CENTER_BODY_RADII['Moon'] | 1737 | 1737.4 | NASA Fact Sheet volumetric mean |
| CENTER_BODY_RADII['Mars'] | 3396.2 | 3389.5 | Volumetric mean (3396.2 was equatorial) |
| CENTER_BODY_RADII['Jupiter'] | 71492 | 69911 | Volumetric mean (71492 is equatorial) |
| CENTER_BODY_RADII['Arrokoth'] | 0.0088 | 9.95 | Was 8.8 meters! Gemini caught |
| SOLAR_RADIUS_AU | 0.00465047 | derived | Computed from SUN_RADIUS_KM / KM_PER_AU |
| LIGHT_MINUTES_PER_AU | 8.3167 | derived | Computed from KM_PER_AU / c / 60 |
| CORE_AU | 0.00093 | derived | 0.2 * SOLAR_RADIUS_AU |
| RADIATIVE_ZONE_AU | 0.00325 | derived | 0.7 * SOLAR_RADIUS_AU |
| PARKER_CLOSEST_RADII | 8.2 | 9.86 | Center distance, perihelion 22. Gemini caught |

**Decision needed from Tony**: Mars and Jupiter in CENTER_BODY_RADII changed
from equatorial to volumetric mean radii. If shell rendering uses these to
draw sphere surfaces, equatorial may be more visually correct. Either way,
the choice should be documented.

-----

## Remaining Work

### Immediate (consolidation)

The 15 consistent duplicates need to be resolved. Every solar constant is
defined three times: `constants_new.py`, `planet_visualization.py`, and
`planet_visualization_utilities.py`. Fix: import from `constants_new.py`,
delete local redefinitions.

Additionally, `KM_PER_AU` is hardcoded as `149597870.7` in 8+ files instead
of imported. And `sgr_a_star_data.py` has the wrong value (149600000).

Target files for consolidation:
- planet_visualization.py — redefines 12 solar constants locally
- planet_visualization_utilities.py — redefines 12 solar constants + owns 3 shell constants (now in constants_new.py)
- comet_visualization_shells.py — hardcodes SUN_RADIUS_KM and KM_PER_AU
- close_approach_data.py — hardcodes AU_TO_KM and body radii
- apsidal_markers.py — hardcodes 149597870.7 in 5 places
- idealized_orbits.py — hardcodes 149597870.7 in 6 places
- gallery_studio.py — hardcodes 149597870.7 in 2 places
- sgr_a_star_data.py — WRONG VALUE (149600000)

### Next session (testing protocol)

Build verification testing to ensure value changes don't break rendering.
Byword: accuracy first.

### Ongoing (INFO dictionary fact-checking)

The 181 entries in `info_dictionary.py` are all Public-facing (Criticality = 4)
and mostly Recalled (Vulnerability = 4). Score = 16 for each. These need
selective fact-checking against NASA mission pages and published sources.
Priority: MAPS narrative, solar shell descriptions, spacecraft encounter details.

-----

## New Principles Established

### Fetched vs Recalled Convention

Claude's factual claims fall into two categories with very different reliability:

- **Fetched** — data from authoritative pipeline (Horizons, VizieR, ERA5). Trust the pipeline.
- **Recalled** — data from Claude's training memory. Verify or source.

The rule: *If a factual claim would be embarrassing or misleading if wrong,
it must be fetched, not recalled.* Claude will assert recalled facts with full
confidence — confidence is not evidence.

### Cross-AI Verification is Load-Bearing

Verification by the same AI that generated the value is not verification.
This session proved it: Claude confabulated Parker's distance while explicitly
claiming to verify it. Gemini caught it. The audit pipeline should be:
Claude sources → Gemini reviews → Tony decides.

### When Claude Explains Away Your Observation, Be MOST Skeptical

The asterism failure: Claude didn't just get facts wrong — it constructed a
plausible explanation for why Tony's correct visual observation was mistaken.
That's active confabulation defending prior confabulation. The double helix
fails if one strand can talk the other out of what it's seeing.

### Trust Earned on Reasoning Does Not Transfer to Recall

They are different capabilities with different failure modes. As delegation
increases, so must source discipline.

-----

## Tool Pipeline

```
dep_trace.py          — fine-grained import tracing
module_atlas.py       — dependency graph + module encyclopedia → MODULE_ATLAS.md
provenance_scanner.py — fact provenance audit → PROVENANCE_AUDIT.md
add_docstrings.py     — batch docstring management
```

Each tool builds on the last. The atlas maps code structure. The scanner
maps fact structure. Together they make the invisible visible.

-----

## Quotables from This Session

"Claude even explained why I was not seeing the Orion asterism correctly!"
"I remember laughing when ChatGPT thought Biden was still President. Now it's not funny."
"And here's the thing — I am doing less manual building. And trusting Claude more."
"You and me are doing the work of seven programmers." — but the eighth job
  (fact-checker for every recalled claim) doesn't scale.
"Verification by the same AI that generated the value is not verification."
"Aww...you didn't give yourself credit Claude!" → "Aww...Gemini caught what Claude missed!"

-----

*Handoff v1: Provenance audit pipeline established. Cross-AI verification proven essential.*
