# ORBITAL_MECHANICS_README v1.8 Update

## Documentation Changes for Trajectory Visualization Consistency

**Date:** December 25, 2025  
**Version:** 1.8 (Trajectory Two-Layer System & Marker Color Consistency)

---

## 1. UPDATE HEADER

**Replace:**
```
**Last Updated:** December 23, 2025 (v1.7 - Center Object Refactoring, center_id Pattern & Fly-To Camera)  
```

**With:**
```
**Last Updated:** December 25, 2025 (v1.8 - Trajectory Two-Layer System & Marker Color Consistency)  
```

---

## 2. ADD NEW SECTION TO PART II (After Section 18 "Fly-To Camera Feature")

### Insert new section:

```markdown
---

## 19. Trajectory Two-Layer Visualization System

### The Problem

Spacecraft missions (like Juno at Jupiter) have two relevant time scales:
1. **Full Mission** - The entire trajectory from launch to end of mission (years)
2. **Plotted Period** - The specific dates selected in the GUI (days/weeks)

Previously, these were confusingly labeled and styled inconsistently between static and animated plots.

### The Solution: Two Distinct Traces

Both static and animated plots now show two separate, toggleable traces:

| Trace | Color | Purpose |
|-------|-------|---------|
| **Full Mission** | Base color (e.g., cyan for Juno) | Shows complete mission trajectory |
| **Plotted Period** | Yellow | Highlights the GUI-selected date range |

### Visual Consistency

The key insight: **Both plots should look the same**, with the only difference being animation.

| Element | Static Plot | Animated Plot |
|---------|-------------|---------------|
| Full Mission trace | Base color, solid | Base color, solid |
| Full Mission marker | Base color | Base color |
| Plotted Period trace | Yellow, solid | Yellow, solid |
| Plotted Period marker | Yellow | Yellow |

### Implementation Details

#### plot_actual_orbits() - Shared Function

Added `trajectory_marker_color` parameter to control trace and marker colors:

```python
def plot_actual_orbits(fig, planets_to_plot, dates_lists, center_id='Sun', 
                       show_lines=True, center_object_name='Sun', 
                       show_closest_approach=False, trajectory_marker_color=None):
    
    # Determine trace color for trajectory objects
    obj_type = obj_info.get('object_type', 'orbital')
    trace_color = trajectory_marker_color if (obj_type == 'trajectory' and trajectory_marker_color) else color_map(planet)
    
    # Labels depend on context
    if obj_type == 'trajectory':
        if trajectory_marker_color:  # Called from animate_objects with yellow
            legend_name = f"{planet} Plotted Period"
        else:  # Called from plot_objects without color
            legend_name = f"{planet} Full Mission"
```

#### plot_objects() - Static Plots

1. Calls `plot_actual_orbits()` without `trajectory_marker_color` -> Full Mission (base color)
2. Adds separate yellow Plotted Period trace and marker

```python
# Full Mission via plot_actual_orbits (base color)
plot_actual_orbits(fig, selected_planets, dates_lists, ...)

# Plotted Period overlay (yellow)
for obj in trajectory_objects:
    # Fetch trajectory for GUI date range
    fig.add_trace(go.Scatter3d(
        ...,
        line=dict(color='yellow', width=2),
        name=f"{obj_name} Plotted Period"
    ))
    
    # Yellow closest approach marker
    add_closest_approach_marker(..., marker_color='yellow')
```

#### animate_objects() - Animated Plots

1. Full Mission section adds trace AND marker (base color)
2. Calls `plot_actual_orbits()` with `trajectory_marker_color='yellow'` -> Plotted Period

```python
# Full Mission trace (base color)
fig.add_trace(go.Scatter3d(
    ...,
    line=dict(color=base_color, width=2),
    name=f"{obj_name} Full Mission"
))

# Full Mission closest approach marker (base color)
add_closest_approach_marker(..., marker_color=base_color)

# Plotted Period via plot_actual_orbits (yellow)
plot_actual_orbits(..., trajectory_marker_color='yellow')
```

### add_closest_approach_marker() Enhancement

Added optional `marker_color` parameter:

```python
def add_closest_approach_marker(fig, positions_dict, obj_name, center_body, 
                                 color_map, date_range=None, marker_color=None):
    ...
    marker=dict(
        size=8,
        color=marker_color if marker_color else color_map(obj_name),
        symbol='square-open'
    )
```

### Code Locations Modified

| File | Function/Location | Change |
|------|-------------------|--------|
| `apsidal_markers.py` | `add_closest_approach_marker()` | Added `marker_color` parameter |
| `palomas_orrery.py` | `plot_actual_orbits()` | Added `trajectory_marker_color` parameter |
| `palomas_orrery.py` | `plot_objects()` | Added yellow Plotted Period section |
| `palomas_orrery.py` | `animate_objects()` | Added Full Mission marker, yellow for Plotted Period |

### Example: Juno at Jupiter

When viewing Juno's arrival at Jupiter (July 5, 2016):

**Legend items:**
- Jupiter (orange circle)
- Juno Full Mission (cyan line) - entire 2011-2028 trajectory
- Juno Full Mission Closest Plotted Point (cyan square) - closest point in full mission
- Juno Plotted Period (yellow line) - just July 5-6, 2016
- Juno Plotted Period Closest Plotted Point (yellow square) - closest point in plotted dates
- Juno (cyan diamond) - current position marker

### For Paloma

*"When we look at Juno visiting Jupiter, we show TWO paths - the cyan line shows Juno's WHOLE journey from Earth to Jupiter and all the orbits it will do. The yellow line shows just the days we picked to look at closely. Each path has its own 'closest point' marker in matching colors, so you can see when Juno got closest during the whole mission (cyan square) versus when it got closest during just the days we're watching (yellow square)!"*

---
```

---

## 3. ADD TO QUOTATIONS SECTION

**Add:**

```markdown
*"Both plots should look the same, with the only difference being animation."* - Dec 25, 2025 (trajectory consistency insight)
*"Each trace gets its own closest approach marker in matching colors."* - Dec 25, 2025
```

---

## 4. ADD TO "WHAT'S NEW" SECTION

**Add after v1.7 section:**

```markdown
---

## What's New in v1.8 (December 25, 2025)

### Trajectory Two-Layer Visualization

Spacecraft mission trajectories now consistently show two separate, toggleable traces in both static and animated plots:

| Trace | Color | Shows |
|-------|-------|-------|
| Full Mission | Base color | Complete mission trajectory |
| Plotted Period | Yellow | GUI-selected date range |

**Key principle:** Both plot types should look identical; only animation differs.

### Closest Approach Marker Colors

Each trace now has its own closest approach marker in matching color:

- Full Mission trace -> Base color marker
- Plotted Period trace -> Yellow marker

**Enhancement:** `add_closest_approach_marker()` gained optional `marker_color` parameter.

### plot_actual_orbits() Enhancement

New `trajectory_marker_color` parameter controls both trace color and marker color for trajectory objects:

```python
plot_actual_orbits(..., trajectory_marker_color='yellow')  # Plotted Period
plot_actual_orbits(...)  # Full Mission (no color = base color)
```

### Files Modified

| File | Changes |
|------|---------|
| `apsidal_markers.py` | Added `marker_color` parameter to `add_closest_approach_marker()` |
| `palomas_orrery.py` | Added `trajectory_marker_color` to `plot_actual_orbits()` |
| `palomas_orrery.py` | Added Plotted Period section in `plot_objects()` |
| `palomas_orrery.py` | Added Full Mission marker in `animate_objects()` |

### Testing: Juno at Jupiter

Validated with Juno arrival visualization (July 5, 2016):
- Static plot: Full Mission (cyan) + Plotted Period (yellow) with matching markers
- Animated plot: Same traces and markers, animated over 25 frames

### Lessons Documented

| Topic | Insight |
|-------|---------|
| Visual consistency | Static and animated plots should show identical traces |
| Marker ownership | Each trace should have its own closest approach marker |
| Color semantics | Yellow = "what you're looking at now", base = "full context" |
| Parameter design | Single `trajectory_marker_color` controls both trace and marker |

---

**Focus areas:** Visual consistency, user experience  
**Files modified:** `palomas_orrery.py`, `apsidal_markers.py`  
**Educational value:** Demonstrates layered visualization for temporal context  
**Quotable:** *"Each trace gets its own closest approach marker in matching colors."*

---
```

---

## 5. UPDATE VERSION HISTORY

**Add entry:**

```markdown
| 1.8 | Dec 25, 2025 | Trajectory Two-Layer System & Marker Color Consistency |
```

---

## Summary of Changes

| Section | Action |
|---------|--------|
| Header | Update to v1.8, Dec 25, 2025 |
| Part II, Section 19 | Add "Trajectory Two-Layer Visualization System" |
| Quotations | Add trajectory consistency insights |
| What's New | Add v1.8 section |
| Version History | Add v1.8 entry |

---

*Document prepared by Claude for Tony's Paloma's Orrery project*  
*December 25, 2025*
