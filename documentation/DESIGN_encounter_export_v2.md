# Encounter Export Redesign
**Design Document | v1.0 | May 6, 2026**
**Tony Quintanilla with Anthropic's Claude Opus 4.6**

## Problem Statement

The Gallery Studio encounter exporter produces incorrect encounter dicts.
The Psyche Mars flyby/Phobos flyby exports (May 2026) required manual
correction of center body, distance, and date format -- and even after
manual correction, the Go button failed because the exported date format
('2026-5-15 9:28') silently breaks all downstream date parsers.

The Go button plotted the right objects at the right center at the right
scale -- but at the wrong time (today's date instead of the encounter date).

## Design Principle

**The preview IS the test of the extraction.** The user sees exactly what the
encounter dict will produce before committing. Every extraction error is
visible in the preview as a wrong plot, not as a wrong text label.

WYSIWYG: What You See Is What You Get.

## Pipeline

```
1. Generate plot in Orrery, save as HTML
2. Import HTML into Gallery Studio
3. Enter Orrery Preset mode (strips post-production, enables encounter export)
4. Open Export Encounter dialog
5. PREVIEW: renders what the extraction produces
   - Temp HTML using same render path as Go button
   - Shows extraction limitations (e.g., static-only for now)
   - User validates visually
6. If preview looks right, generate outputs:
   a. Python dict for spacecraft_encounters.py
   b. Optional HTML export of preview (identical to Go button output)
7. Paste dict into spacecraft_encounters.py
8. Go button produces same plot as preview
9. (Future) Address gaps between original HTML and Go button output
```

Key contract: steps 5, 6b, and 8 all produce the same plot from the same
parameter set. The preview is the Go button running ahead of time.

## Parameter Set

### Render Parameters (drive preview and Go button)

| Parameter      | Source                        | Notes                                |
|----------------|-------------------------------|--------------------------------------|
| center body    | Extracted from traces         | Body at (0,0,0) in position data     |
| select_also    | Extracted from visible traces | Deduplicated, spacecraft excluded    |
| date window    | From Orrery (start/end dates) | Parsed from title or Orrery state    |
| plot_scale_au  | From Orrery, editable in Studio | Studio axis range control          |

### Extracted Science Data (from closest plotted point marker)

| Parameter       | Source                         | Notes                              |
|-----------------|--------------------------------|------------------------------------|
| encounter date  | Closest plotted point date     | Format: YYYY-MM-DD HH:MM:SS       |
| dist_km         | Center-to-center distance      | From closest plotted point marker  |
| dist_surface_km | Surface distance if radius known | dist_km minus body radius        |

### Manual Metadata (user enters in dialog)

| Parameter   | Widget   | Default       | Notes                          |
|-------------|----------|---------------|--------------------------------|
| target      | Entry    | (suggestion)  | Mission target, informational  |
| label       | Entry    | (empty)       | Display label                  |
| date_source | Dropdown | 'horizons'    | horizons / authoritative / planning |
| v_kms       | Entry    | (empty)       | Manual entry for now           |
| status      | Dropdown | 'completed'   | completed / ongoing / planned / canceled |
| source      | Entry    | 'NASA/JPL'    | Data attribution               |
| note        | Text     | (empty)       | Must support paste entry       |

## Bugs Diagnosed

### Bug 1: Center Detection Failure
**Location**: `gallery_studio.py`, `_extract_encounter_data()`, lines 5085-5100
**Symptom**: Center defaults to 'Sun' on Mars/Phobos-centered plots.
**Root cause**: Regex looks for "around X" / "centered on X" in title.
Orrery titles ("Paloma's Orrery - Animation Over Below Dates") never match.
Fallback checks if 'Sun' is in visible traces, otherwise no center set.
`_generate_encounter_code()` at line 5276 defaults: `extracted.get('center', 'Sun')`.
**Fix**: Detect center body from trace position data (body at origin) or
pass center body name from Orrery state.

### Bug 2: Animation First-Frame Grab
**Location**: `gallery_studio.py`, `_extract_encounter_data()`, lines 5133-5155
**Symptom**: Distance off by factor of ~4,300x (4,970,995 km vs 1,151 km).
**Root cause**: Loop finds first "Closest Plotted Point" trace and breaks.
Animations have N frames x M closest-point traces. First frame is typically
the farthest, not the closest approach.
Phobos flyby HTML: 64 frames, Frame 0 = 4,970,995 km, Frame 1 = 1,151 km.
**Fix**: Use the Orrery's already-computed closest approach (argmin in
`add_closest_approach_marker()`, apsidal_markers.py line 1470). Pass through
rather than re-derive.

### Bug 3: Distance Semantics
**Location**: Hover text uses "Distance from center" (apsidal_markers.py line 1508).
**Current state**: Hover text shows both center distance and surface distance
when radius is known. Extractor grabs first km match (center-to-center).
**Fix**: Extract both values. Report dist_km as center-to-center (consistent
with Horizons and existing NH/Artemis entries). Report dist_surface_km
separately when body radius is available.

### Bug 4: Date Format
**Location**: Exported encounter dicts.
**Symptom**: Psyche dates '2026-5-15 9:28' fail `strptime('%Y-%m-%d %H:%M:%S')`.
**Impact cascade**:
  1. `_calculate_encounter_resolution()` line 553: parse fails, returns None.
     No adaptive resolution (no curvature-derived fetch step).
  2. Fallback path in `get_encounter_preset()` line 756: same parse, also fails.
     Returns `start_date=None`, `end_date=None`.
  3. `_apply_mission_preset()` line 8369: skips date assignment (date_str is None).
     GUI keeps whatever dates were loaded. Go button plots wrong time window.
**Result**: Even with manually corrected center/distance, Go button plotted
May 6-June 3 2026 (today's default) instead of the May 15 encounter window.
**Fix**: Enforce YYYY-MM-DD HH:MM:SS format in generated code. Zero-pad
month/day/hour. Always include seconds.

### Bug 5: Animation Loss
**Location**: `_apply_mission_preset()`, line 8467.
**Symptom**: Encounter preset always produces static plot.
**Root cause**: Go button calls `plot_objects`, never `animate_objects`.
No animation parameters in encounter dict schema.
**Status**: Deferred to pipeline step 9. Preview shows what the extractor
CAN produce. If static only, preview shows static, user sees that limitation.

### Bug 6: Psyche Full Mission Empty Dates
**Location**: `SPACECRAFT_FULL_MISSION['Psyche']`.
**Symptom**: `start_date: ''` and `end_date: ''`.
**Fix**: Fill in dates. Psyche launched Oct 13, 2023; arrival August 2029.

## Why Hand-Authored Entries Work But Exports Don't

New Horizons and Artemis II entries were written directly into
`spacecraft_encounters.py` -- they never went through the Studio exporter.
Their dict values are clean (proper date format, correct centers).

The Psyche entries were the first real test of the encounter export pipeline.
Every exporter bug (center detection, distance extraction, date format)
manifested simultaneously.

The same center detection failure would occur on ANY Orrery plot loaded
into Studio -- it is not Mars-specific. The exporter has not been validated
against New Horizons or Artemis II plots.

## Existing Encounters Audit

| Spacecraft   | Encounter        | Center | dist_km      | Date Format | Dict Status |
|--------------|------------------|--------|--------------|-------------|-------------|
| New Horizons | Jupiter GA       | Sun    | 2,305,000    | OK          | Clean       |
| New Horizons | Pluto Flyby      | Sun    | 12,472 (sfc) | OK          | Clean       |
| New Horizons | Arrokoth Flyby   | Sun    | 3,538 (sfc)  | OK          | Clean       |
| Artemis II   | Earth Departure  | Earth  | 70,377       | OK          | Clean       |
| Artemis II   | Lunar Closest    | EMB    | 8,900 (sfc)  | OK          | Clean       |
| Artemis II   | Reentry          | Earth  | 6,493        | OK          | Clean       |
| Psyche       | Mars GA Static   | Mars*  | 8,009*       | BROKEN      | Manually fixed |
| Psyche       | Mars GA Animated | Mars*  | 8,009*       | BROKEN      | Manually fixed |
| Psyche       | Phobos Flyby     | Phobos*| 1,151*       | BROKEN      | Manually fixed |
| Psyche       | Full Mission     | Sun    | N/A          | EMPTY DATES | Incomplete  |

*Manually corrected by Tony. Exporter originally produced center='Sun'
and distances of 8,016,400 km / 4,970,995 km. Manual correction fixed
center and distance but the broken date format ('2026-5-15 9:28') silently
prevented the Go button from working -- dates fell through to GUI defaults.

## Distance Convention

Existing entries use both center-to-center and surface distances inconsistently:

| Entry              | dist_km label | Meaning                        |
|--------------------|---------------|--------------------------------|
| NH Jupiter GA      | 2,305,000     | Center-to-center (32 Jovian radii) |
| NH Pluto           | 12,472        | Surface ("12,472 km above the surface") |
| NH Arrokoth        | 3,538         | Surface (per JPL Horizons header) |
| Artemis II Moon    | 8,900         | Surface ("closest approach to lunar surface") |
| Artemis II Reentry | 6,493         | Center-to-center (122 km alt + 6371 km radius) |

Convention going forward: dist_km = center-to-center. dist_surface_km =
surface distance when body radius is known. Both values in the dict.
Hover text and notes should clarify which is which.

Note: NH Pluto (12,472 km) and Arrokoth (3,538 km) are labeled as surface
distances in their notes. These were hand-authored before the convention
was established. Consider adding dist_surface_km retroactively.

## Implementation Notes

- The preview renders a temp HTML using the same path as the Go button.
  This is the existing WYSIWYG architecture applied to encounter export.
- The HTML export produces a file identical to the preview.
- The encounter dict captures the parameters that reproduce the preview
  via the Go button.
- Current limitation: static plots only. Animation support is pipeline step 9.
- All date strings must be YYYY-MM-DD HH:MM:SS (zero-padded, with seconds).

## Related Files

| File                       | Role                                    |
|----------------------------|-----------------------------------------|
| gallery_studio.py          | Encounter export dialog and extraction  |
| spacecraft_encounters.py   | Encounter dict database and presets     |
| apsidal_markers.py         | Closest plotted point marker generation |
| palomas_orrery.py          | Go button (_apply_mission_preset)       |

## Version History

- v1.0 (May 6, 2026): Initial design from diagnostic session. Three Psyche
  encounter exports diagnosed, six bugs identified, pipeline redesigned
  around WYSIWYG preview as validation layer.
