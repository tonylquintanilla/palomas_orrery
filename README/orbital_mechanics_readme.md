# ORBITAL_MECHANICS_README v1.9 Update

## Documentation Changes for Trajectory Visualization & Animation Shells

**Date:** December 25, 2025  
**Version:** 1.9 (Trajectory Two-Layer System, Marker Color Consistency & Static Shells in Animations)

---

## 1. UPDATE HEADER

**Replace:**
```
**Last Updated:** December 23, 2025 (v1.7 - Center Object Refactoring, center_id Pattern & Fly-To Camera)  
```

**With:**
```
**Last Updated:** December 25, 2025 (v1.9 - Trajectory Two-Layer System & Static Animation Shells)  
```

---

## 2. ADD NEW SECTIONS TO PART II (After Section 18 "Fly-To Camera Feature")

### Insert new sections:

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

#### animate_objects() - Animated Plots

1. Full Mission section adds trace AND marker (base color)
2. Calls `plot_actual_orbits()` with `trajectory_marker_color='yellow'` -> Plotted Period

### add_closest_approach_marker() Enhancement

Added optional `marker_color` parameter:

```python
def add_closest_approach_marker(fig, positions_dict, obj_name, center_body, 
                                 color_map, date_range=None, marker_color=None):
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
- Juno Full Mission Closest Plotted Point (cyan square)
- Juno Plotted Period (yellow line) - just July 5-6, 2016
- Juno Plotted Period Closest Plotted Point (yellow square)
- Juno (cyan diamond) - current position marker

### For Paloma

*"When we look at Juno visiting Jupiter, we show TWO paths - the cyan line shows Juno's WHOLE journey from Earth to Jupiter and all the orbits it will do. The yellow line shows just the days we picked to look at closely. Each path has its own 'closest point' marker in matching colors!"*

---

## 20. Static Shells in Animations: Memory Optimization

### The Problem

Shell visualizations (planet interiors, rings, radiation belts, magnetospheres) create many Plotly traces with complex geometry. Previously, animations excluded shells entirely because duplicating this geometry across N frames caused memory explosion.

This meant animated plots looked stripped down compared to static plots - no Jupiter rings, no radiation belts, no atmospheric layers.

### The Solution: Static vs Dynamic Trace Separation

Plotly's `Frame` object has an optional `traces` parameter that specifies WHICH traces the frame updates. Traces not listed remain static.

**Architecture:**
```
Figure.data:
  [0] Jupiter Cloud Layer        <- STATIC (index < static_trace_count)
  [1] Jupiter Upper Atmosphere   <- STATIC
  [2] Jupiter Rings              <- STATIC
  ...
  [14] Jupiter Magnetosphere     <- STATIC
  [15] Juno Full Mission         <- DYNAMIC (index >= static_trace_count)
  [16] Juno position             <- DYNAMIC
  [17] Metis position            <- DYNAMIC
  ...

Frame: data=[only dynamic traces], traces=[15, 16, 17, ...]
```

### Implementation

#### 1. Add shells immediately after figure creation

```python
fig = go.Figure()

# Add static center shells (same logic as plot_objects)
if center_object_name == 'Sun' and any(var.get() == 1 for var in sun_shell_vars.values()):
    fig = create_sun_visualization(fig, sun_shell_vars)
elif center_object_name in animation_shell_config:
    shell_vars = animation_shell_config[center_object_name]
    if any(var.get() == 1 for var in shell_vars.values()):
        fig = create_planet_visualization(fig, center_object_name, shell_vars)

# Track boundary between static and dynamic
static_trace_count = len(fig.data)
```

#### 2. Frame creation with selective updates

```python
dynamic_trace_indices = list(range(static_trace_count, len(fig.data)))

def to_frame_idx(absolute_idx):
    """Convert absolute fig.data index to frame_data index."""
    if absolute_idx >= static_trace_count:
        return absolute_idx - static_trace_count
    return None  # Static trace, not in frame_data

for i in range(N):
    # Only copy dynamic traces
    frame_data = [copy.deepcopy(fig.data[idx]) for idx in dynamic_trace_indices]
    
    # Update positions using frame indices...
    
    frames.append(go.Frame(
        data=frame_data,
        traces=dynamic_trace_indices,  # Only update these
        name=frame_name
    ))
```

#### 3. Index mapping throughout

Every `frame_data[trace_idx]` became `frame_data[to_frame_idx(trace_idx)]` with None checks.

### Debug Output

```
[ANIMATION] Added Jupiter shells (15 static traces)
[ANIMATION] Static traces: 0-14 (15 traces)
[ANIMATION] Dynamic traces: 15-30 (16 traces)
```

### Memory Savings

For 25-frame animation with Jupiter shells:

| Approach | Traces per Frame | Total Trace Data |
|----------|------------------|------------------|
| Old (all traces) | 31 | 31 x 25 = 775 |
| New (dynamic only) | 16 | 16 x 25 + 15 = 415 |

**45% reduction** in trace data, and shell geometry (the expensive part) is only stored once.

### Edge Cases Handled

| Case | Handling |
|------|----------|
| No shells selected | `static_trace_count = 0`, all traces dynamic |
| Exoplanet mode | Solar system shells skipped, works normally |
| Mesh3d debug print | Use `getattr(trace, 'mode', 'N/A')` - Mesh3d has no mode |
| Slider sync | Index mapping applied to initial frame sync |

### For Paloma

*"Before, when we made Jupiter movies, we couldn't show Jupiter's rings and clouds because the computer had to remember them 25 times - once for each picture in the movie! Now we're smarter - we tell the computer 'Jupiter stays still, so just remember it once.' That lets us show all of Jupiter's beautiful details while Juno flies around it!"*

---
```

---

## 3. ADD TO QUOTATIONS SECTION

**Add:**

```markdown
*"Both plots should look the same, with the only difference being animation."* - Dec 25, 2025 (trajectory consistency insight)
*"Each trace gets its own closest approach marker in matching colors."* - Dec 25, 2025
*"Static traces don't need to be in frames - that's the whole point!"* - Dec 25, 2025 (animation optimization)
*"Ha ha I just want to see Juno fly through that cloud layer!"* - Tony, Dec 25, 2025
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

New `trajectory_marker_color` parameter controls both trace color and marker color for trajectory objects.

### Files Modified

| File | Changes |
|------|---------|
| `apsidal_markers.py` | Added `marker_color` parameter |
| `palomas_orrery.py` | Added `trajectory_marker_color` parameter, Plotted Period sections |

---

## What's New in v1.9 (December 25, 2025)

### Static Shells in Animations

Center object shell visualizations now appear in animations without memory explosion.

**Key insight:** Plotly frames can specify which traces to update via the `traces` parameter. Static geometry (shells) doesn't need to be duplicated in every frame.

**Architecture:**
1. Shells added first (indices 0 to static_trace_count-1)
2. Dynamic objects added after (indices static_trace_count onwards)
3. Frames only contain and update dynamic traces
4. ~45% memory reduction for shell-heavy animations

### Implementation Pattern

```python
static_trace_count = len(fig.data)  # After adding shells
dynamic_trace_indices = list(range(static_trace_count, len(fig.data)))

frames.append(go.Frame(
    data=frame_data,  # Only dynamic traces
    traces=dynamic_trace_indices  # Which fig.data indices to update
))
```

### Index Mapping

Helper function converts absolute trace indices to frame indices:

```python
def to_frame_idx(absolute_idx):
    if absolute_idx >= static_trace_count:
        return absolute_idx - static_trace_count
    return None  # Static trace
```

### Bug Fix: Mesh3d Mode Attribute

Debug print failed on shell traces (Mesh3d) which don't have `mode` attribute:

```python
# Before (crashes on Mesh3d)
print(f"Trace {i}: {trace.name} (mode: {trace.mode})")

# After (safe for all trace types)
trace_mode = getattr(trace, 'mode', 'N/A')
print(f"Trace {i}: {trace.name} ({type(trace).__name__}, mode: {trace_mode})")
```

### Files Modified

| File | Changes |
|------|---------|
| `palomas_orrery.py` | Added shell support in `animate_objects()`, frame index mapping |

### Testing: Juno at Jupiter

Validated with Juno perijove animation (July 5, 2016):
- Jupiter shells visible (cloud layer, rings, radiation belts, magnetosphere)
- Juno trajectory animates through shell layers
- Memory usage acceptable for 25 frames
- All moon positions update correctly

### Lessons Documented

| Topic | Insight |
|-------|---------|
| Plotly frames | `traces` parameter enables selective updates |
| Memory optimization | Static geometry stored once, not per-frame |
| Index mapping | Absolute indices vs frame-relative indices |
| Trace attributes | Mesh3d lacks `mode`, use `getattr()` safely |

---

**Focus areas:** Performance optimization, visual parity between static/animated plots  
**Files modified:** `palomas_orrery.py`, `apsidal_markers.py`  
**Educational value:** Demonstrates Plotly animation optimization techniques  
**Quotable:** *"Static traces don't need to be in frames - that's the whole point!"*

---
```

---

## 5. UPDATE VERSION HISTORY

**Add entries:**

```markdown
| 1.8 | Dec 25, 2025 | Trajectory Two-Layer System & Marker Color Consistency |
| 1.9 | Dec 25, 2025 | Static Shells in Animations (Memory Optimization) |
```

---

## Summary of Changes

| Section | Action |
|---------|--------|
| Header | Update to v1.9, Dec 25, 2025 |
| Part II, Section 19 | Add "Trajectory Two-Layer Visualization System" |
| Part II, Section 20 | Add "Static Shells in Animations: Memory Optimization" |
| Quotations | Add trajectory and animation insights |
| What's New | Add v1.8 and v1.9 sections |
| Version History | Add v1.8 and v1.9 entries |

---

## Edge Cases Considered

For the animation shells feature, we verified:

1. **No shells selected** - `static_trace_count = 0`, all traces are dynamic, works normally
2. **Exoplanet mode** - Solar system shells aren't added, exoplanet animation works
3. **Center object without shell support** - Falls back to marker, no shells to add
4. **Mesh3d trace type** - Fixed debug print to use `getattr()` for missing `mode`
5. **Slider sync** - Index mapping applied when syncing initial frame data
6. **Binary stars** - Frame index mapping handles these correctly

---

*Document prepared by Claude for Tony's Paloma's Orrery project*  
*December 25, 2025 - Merry Christmas!*
