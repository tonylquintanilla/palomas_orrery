# Spacecraft Encounter Infrastructure — Integration Guide

**Date:** March 11, 2026  
**Steps:** 4 (all included below)  
**Editing order:** Bottom-up within each file  

---

## File 1: `apsidal_markers.py`

### Step 2: Add small body apsidal terms (line ~46)

Insert into `APSIDAL_TERMINOLOGY` dict, after the Pluto entries:

```python
    'Bennu':      ('Peribennu', 'Apobennu'),
    'Ryugu':      ('Periryugu', 'Aporyugu'),
    'Arrokoth':   ('Periarrokoth', 'Apoarerokoth'),
    'Patroclus':  ('Peripatroclia', 'Apopatroclia'),
    'Apophis':    ('Periapophion', 'Apoapophion'),
    'Dinkinesh':  ('Peridinkinesh', 'Apodinkinesh'),
```

### Step 3: Append to END of file (after line 1756)

Append the entire contents of `step3_pairwise_encounter.py` (provided separately).

Contains:
- `ENCOUNTER_THRESHOLD_AU = 0.5`
- `compute_pairwise_encounter()` — finds closest approach between two position time series
- `add_encounter_marker()` — places white diamond-open marker with hover text

### Step 1: Modify `add_closest_approach_marker` (two changes)

**Change 1a — Signature (line 1363):**

```
OLD: def add_closest_approach_marker(fig, positions_dict, obj_name, center_body, color_map, date_range=None, marker_color=None):
NEW: def add_closest_approach_marker(fig, positions_dict, obj_name, center_body, color_map, date_range=None, marker_color=None, obj_info=None):
```

**Change 1b — After hover text (line 1461), add mission_info block:**

After:
```python
    hover_text = (
        f"<b>{obj_name} {label}</b><br>"
        f"Date: {date_str_formatted}<br>"
        f"Distance from center: {au_str}<br>"
        f"Distance from center: {km_str}"
    )
```

Add:
```python
    # Append mission context if available (spacecraft encounter infrastructure)
    if obj_info:
        mission_info = obj_info.get('mission_info', '')
        if mission_info:
            # Truncate long mission_info for hover — first 300 chars
            if len(mission_info) > 300:
                mission_info = mission_info[:297] + '...'
            hover_text += f"<br><br><i>{mission_info}</i>"
```

---

## File 2: `palomas_orrery.py`

### Step 4a: Add `_add_spacecraft_encounter_markers` function

Place AFTER `_add_perihelion_osculating_orbit` (after line ~1876).

Insert the entire contents of `step4_spacecraft_encounter_markers.py` (provided separately).

### Step 4b: Call the function at Pipeline 1 (around line 5271)

After the Capability D block (after `_add_perihelion_osculating_orbit`), add:

```python
            # ---- Spacecraft Encounter Markers (Mode 2: pairwise detection) --------
            # Only fires for Sun-centered plots where both objects are heliocentric
            if center_object_name == 'Sun' and show_closest_approach_var.get():
                _add_spacecraft_encounter_markers(
                    fig=fig,
                    selected_objects=selected_objects,
                    objects=objects,
                    dates_lists=dates_lists,
                    center_object_name=center_object_name,
                    center_id=center_id,
                    color_map=color_map,
                    show_closest_approach=show_closest_approach_var.get(),
                )
```

### Step 4c: Call the function at Pipeline 2 (around line 6451)

After the Capability D block in Pipeline 2, add:

```python
            # ---- Spacecraft Encounter Markers (Mode 2: pairwise detection) --------
            if center_object_name == 'Sun' and show_closest_approach_var.get():
                _add_spacecraft_encounter_markers(
                    fig=fig,
                    selected_objects=selected_object_names,
                    objects=objects,
                    dates_lists=dates_lists,
                    center_object_name=center_object_name,
                    center_id=center_id,
                    color_map=color_map,
                    show_closest_approach=show_closest_approach_var.get(),
                    positions_cache=positions_over_time,
                )
```

Note: Pipeline 2 passes `positions_cache=positions_over_time` to avoid redundant Horizons fetches (positions already fetched for animation).

### Step 1 callers: Pass obj_info to add_closest_approach_marker

**Line ~4861 (Plotted Period, Pipeline 1):**

Variable `obj` is the full dict at this scope (from `trajectory_objects` loop at line 4766).

```
OLD:                                    marker_color='yellow'  # Yellow for Plotted Period
                                )
NEW:                                    marker_color='yellow',  # Yellow for Plotted Period
                                    obj_info=obj
                                )
```

**Line ~6384 (Full Mission, Pipeline 2):**

Variable `obj_info` is already defined at line 6325.

```
OLD:                                    marker_color=base_color  # Use base color for Full Mission
                                )
NEW:                                    marker_color=base_color,  # Use base color for Full Mission
                                    obj_info=obj_info
                                )
```

---

## Summary of Changes

| File | Change | Type | Lines |
|------|--------|------|-------|
| `apsidal_markers.py` | Small body apsidal terms | Insert 6 lines at ~46 | Step 2 |
| `apsidal_markers.py` | `compute_pairwise_encounter()` + `add_encounter_marker()` | Append ~200 lines | Step 3 |
| `apsidal_markers.py` | `obj_info` param + mission_info hover | 2 targeted edits | Step 1 |
| `palomas_orrery.py` | `_add_spacecraft_encounter_markers()` function | Insert ~140 lines at ~1876 | Step 4a |
| `palomas_orrery.py` | Pipeline 1 call | Insert 10 lines at ~5271 | Step 4b |
| `palomas_orrery.py` | Pipeline 2 call | Insert 11 lines at ~6451 | Step 4c |
| `palomas_orrery.py` | Pass `obj_info` to 2 existing callers | 2 targeted edits | Step 1 |

**Total: ~370 new lines across 2 files + 4 targeted edits**

---

## Test Cases

| Spacecraft | Target | Center | Expected behavior |
|------------|--------|--------|-------------------|
| New Horizons | Pluto | Sun | Encounter marker ~12,472 km, diamond-open white |
| New Horizons | Arrokoth | Sun | Encounter marker ~3,500 km (if both in date range) |
| Juno | Jupiter | Sun | Encounter marker at Jupiter approach distance |
| Juno | Jupiter | Jupiter | Mode 1 (existing) — closest approach marker to center |
| Lucy | Dinkinesh | Sun | Encounter marker ~430 km (if in date range) |
| Voyager 1 | Saturn | Sun | Encounter marker ~124,000 km |

**Key verification:** 
- White diamond-open marker at spacecraft position
- Hover shows distance in AU and km, relative velocity in km/s
- Mission context from `mission_info` appears in hover
- Console log: `[ENCOUNTER] New Horizons -> Pluto: 12,472 km ...`
- Threshold: markers only appear if closest approach < 0.5 AU

---

## Architecture Notes

- **Mode 1** (spacecraft -> center body): Already handled by `add_closest_approach_marker` on center-relative positions. No change needed.
- **Mode 2** (spacecraft -> non-center target): This new capability. Requires both objects to be in the same coordinate frame (heliocentric).
- **Velocity source:** Horizons already returns vx/vy/vz in AU/day. Relative velocity computed directly from velocity vector differences — no position differencing needed.
- **No new API calls:** Uses existing trajectory data. The `positions_cache` parameter in Pipeline 2 avoids duplicate fetches.
- **Threshold:** 0.5 AU initial. Per-object overrides can be added to `celestial_objects.py` later if needed.
