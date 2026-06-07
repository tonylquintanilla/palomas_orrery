# Item 29: Sun Call Site Switchover -- Implementation Manifest

**Date:** May 19, 2026
**Prepared by:** Anthropic's Claude Opus 4.6
**Scope:** Replace `create_sun_visualization()` and `create_sun_corona_from_distance()`
with unified dispatch. Retire both functions. Remove `corona_from_distance` checkbox.
**Files:** `palomas_orrery.py` (7 snippets), `planet_visualization.py` (3 snippets)
**Apply order:** Bottom-up within each file (highest line numbers first)

---

## palomas_orrery.py -- 7 snippets

Apply in this order: 7, 6, 5, 4, 3, 2, 1

---

### Snippet 7 -- Remove corona_from_distance checkbox + tooltip (lines 7924-7937)

**DELETE** these 14 lines:

```python
sun_corona_from_distance_checkbutton = tk.Checkbutton(
    shell_options_frame, 
    text="---> Enable visible solar structures from a non-solar center", 
    variable=sun_corona_from_distance_var
)
sun_corona_from_distance_checkbutton.pack(anchor='w')

CreateToolTip(
    sun_corona_from_distance_checkbutton, 
    "Enables visualization of Sun's visible atmosphere from non-Sun-centered views (Earth, Mars, etc.). "
    "Check the Sun plus the individual shell boxes (Photosphere, Chromosphere, Inner Corona, Outer Corona) to select which "
    "layers to display. Useful for visualizing the Sun's 'glare zone' and understanding observational challenges "
    "for objects near the Sun. Note: Only works when viewing from another center object, not from the Sun itself."
)
```

---

### Snippet 6 -- Animation center-body switchover (lines 6149-6152)

**BEFORE:**

```python
            if center_object_name == 'Sun' and any(var.get() == 1 for var in sun_shell_vars.values()):
                fig = create_sun_visualization(fig, sun_shell_vars)
                center_shells_added = True
                print(f"[ANIMATION] Added Sun shells ({len(fig.data)} static traces)", flush=True)
```

**AFTER:**

```python
            if center_object_name == 'Sun' and any(var.get() == 1 for var in sun_shell_vars.values()):
                fig = create_celestial_body_visualization(
                    fig, 'Sun', sun_shell_vars,
                    center_position=(0, 0, 0),
                    object_type='Sun',
                    center_object='Sun',
                )
                center_shells_added = True
                # Auto-scale axis to shell radius (same as planet path)
                if hasattr(fig, '_shell_outermost_radius_au') and scale_var.get() == 'Auto':
                    shell_r = fig._shell_outermost_radius_au * 2
                    axis_range = [-shell_r, shell_r]
                # Asteroid belts: standalone geometry, not part of unified shell dispatch
                if sun_shell_vars.get('main_belt') and sun_shell_vars['main_belt'].get() == 1:
                    for t in create_main_asteroid_belt():
                        fig.add_trace(t)
                if sun_shell_vars.get('hildas') and sun_shell_vars['hildas'].get() == 1:
                    for t in create_hilda_group():
                        fig.add_trace(t)
                if sun_shell_vars.get('trojans_greeks') and sun_shell_vars['trojans_greeks'].get() == 1:
                    for t in create_jupiter_trojans_greeks(jupiter_angle=0):
                        fig.add_trace(t)
                if sun_shell_vars.get('trojans_trojans') and sun_shell_vars['trojans_trojans'].get() == 1:
                    for t in create_jupiter_trojans_trojans(jupiter_angle=0):
                        fig.add_trace(t)
                print(f"[ANIMATION] Added Sun shells ({len(fig.data)} static traces)", flush=True)
```

---

### Snippet 5 -- Replace corona_from_distance with unified off-center Sun (lines 4644-4653)

**BEFORE:**

```python
            # NEW: Add Sun corona when viewing from non-Sun center
            if center_object_name != 'Sun':
                if sun_shell_vars.get('corona_from_distance') and sun_shell_vars['corona_from_distance'].get() == 1:
                    # Get Sun's position relative to current center
                    if 'Sun' in positions and positions['Sun'] is not None:
                        sun_pos_dict = positions['Sun']
                        # Extract x, y, z from dictionary
                        sun_position = (sun_pos_dict['x'], sun_pos_dict['y'], sun_pos_dict['z'])
                        print(f"\nAdding Sun corona layers at position {sun_position}", flush=True)
                        fig = create_sun_corona_from_distance(fig, sun_shell_vars, sun_position)
```

**AFTER:**

```python
            # Add Sun shells when viewing from non-Sun center (unified dispatch)
            if center_object_name != 'Sun':
                if any(var.get() == 1 for var in sun_shell_vars.values()):
                    if 'Sun' in positions and positions['Sun'] is not None:
                        sun_pos_dict = positions['Sun']
                        sun_position = (sun_pos_dict['x'], sun_pos_dict['y'], sun_pos_dict['z'])
                        print(f"\nAdding Sun shells at offset position {sun_position}", flush=True)
                        fig = create_celestial_body_visualization(
                            fig, 'Sun', sun_shell_vars,
                            center_position=sun_position,
                            object_type='Sun',
                            center_object=center_object_name,
                        )
```

**Note:** Asteroid belt vars in `sun_shell_vars` may fire the `any()` True, but
the unified dispatch silently skips keys not in SHELL_CONFIGS or CUSTOM_SHELLS.
Belts only make geometric sense Sun-centered. Harmless no-op.

---

### Snippet 4 -- Static center-body switchover (lines 4509-4511)

**BEFORE:**

```python
            if center_object_name == 'Sun' and any(var.get() == 1 for var in sun_shell_vars.values()):
                fig = create_sun_visualization(fig, sun_shell_vars)
                center_shells_added = True
```

**AFTER:**

```python
            if center_object_name == 'Sun' and any(var.get() == 1 for var in sun_shell_vars.values()):
                fig = create_celestial_body_visualization(
                    fig, 'Sun', sun_shell_vars,
                    center_position=(0, 0, 0),
                    object_type='Sun',
                    center_object='Sun',
                )
                center_shells_added = True
                # Auto-scale axis to shell radius (same as planet path)
                if hasattr(fig, '_shell_outermost_radius_au') and scale_var.get() == 'Auto':
                    shell_r = fig._shell_outermost_radius_au * 2
                    axis_range = [-shell_r, shell_r]
                # Asteroid belts: standalone geometry, not part of unified shell dispatch
                if sun_shell_vars.get('main_belt') and sun_shell_vars['main_belt'].get() == 1:
                    for t in create_main_asteroid_belt():
                        fig.add_trace(t)
                if sun_shell_vars.get('hildas') and sun_shell_vars['hildas'].get() == 1:
                    for t in create_hilda_group():
                        fig.add_trace(t)
                if sun_shell_vars.get('trojans_greeks') and sun_shell_vars['trojans_greeks'].get() == 1:
                    for t in create_jupiter_trojans_greeks(jupiter_angle=0):
                        fig.add_trace(t)
                if sun_shell_vars.get('trojans_trojans') and sun_shell_vars['trojans_trojans'].get() == 1:
                    for t in create_jupiter_trojans_trojans(jupiter_angle=0):
                        fig.add_trace(t)
```

---

### Snippet 3 -- Remove corona_from_distance from sun_shell_vars (line 2511)

**DELETE** this line (plus the blank line after it):

```python
    'corona_from_distance': sun_corona_from_distance_var,  # NEW
```

---

### Snippet 2 -- Remove corona_from_distance var definition (line 1997)

**DELETE** this line:

```python
sun_corona_from_distance_var = tk.IntVar(value=0)  # NEW: Special checkbox for non-Sun-centered corona
```

---

### Snippet 1 -- Remove dead imports (lines 104-105)

**DELETE** these 2 lines:

```python
    create_sun_visualization,
    create_sun_corona_from_distance,
```

---

## planet_visualization.py -- 3 snippets

Apply in this order: C, B, A

---

### Snippet C -- Retire create_sun_corona_from_distance() (lines 413-531)

**REPLACE** the entire function (lines 413-531) with:

```python
def create_sun_corona_from_distance(fig, sun_shell_vars, sun_position):
    """RETIRED: Off-center Sun rendering migrated to unified dispatch (May 2026).

    Sun shells now render at any center via create_celestial_body_visualization()
    with center_position parameter. No special checkbox needed.

    Module updated: May 2026 with Anthropic's Claude Opus 4.6
    """
    raise NotImplementedError(
        "create_sun_corona_from_distance() retired May 2026. "
        "Use create_celestial_body_visualization(fig, 'Sun', ..., "
        "center_position=sun_position) instead."
    )
```

---

### Snippet B -- Retire create_sun_visualization() (lines 299-411)

**REPLACE** the entire function (lines 299-411) with:

```python
def create_sun_visualization(fig, sun_shell_vars, animate=False, frames=None):
    """RETIRED: Sun rendering migrated to unified dispatch (May 2026).

    Call sites in palomas_orrery.py now use create_celestial_body_visualization()
    directly. Asteroid belt geometry dispatched at call sites.

    Module updated: May 2026 with Anthropic's Claude Opus 4.6
    """
    raise NotImplementedError(
        "create_sun_visualization() retired May 2026. "
        "Use create_celestial_body_visualization(fig, 'Sun', ...) instead."
    )
```

---

### Snippet A -- Remove dead asteroid belt imports (lines 175-186)

**DELETE** these 12 lines:

```python
from asteroid_belt_visualization_shells import (
                                        create_main_asteroid_belt,
                                        create_hilda_group,
                                        create_jupiter_trojans_greeks,
                                        create_jupiter_trojans_trojans,
                                        main_belt_info,
                                        hilda_group_info,
                                        jupiter_trojans_greeks_info,
                                        jupiter_trojans_trojans_info,
                                        get_jupiter_angle_from_data,
                                        calculate_body_angle,
                                        estimate_jupiter_angle_from_date)
```

**Note:** These were only consumed by `create_sun_visualization()`. The same
4 creation functions are already imported directly in `palomas_orrery.py`
(lines 235-239). The info strings are imported via `shell_configs.py` for
the GUI tooltips. No consumer is lost.

---

## Mode 5 Visual Review Checklist

### Sun-centered static plot

- [ ] All 15 sphere shells render (Core through Gravitational Influence)
- [ ] 3 custom shells render (Hills Cloud Torus, Outer Oort Clumpy, Galactic Tide)
- [ ] Photosphere renders as mesh3d solid surface (not dot sphere)
- [ ] 6 legend names normalized:
  - `Sun: Termination Shock` (was: Solar Wind Termination Shock)
  - `Sun: Heliopause` (was: Solar Wind Heliopause)
  - `Sun: Inner Limit of Oort Cloud` (was: Inner Limit of Oort Cloud)
  - `Sun: Inner Oort Cloud` (was: Inner Oort Cloud)
  - `Sun: Outer Oort Cloud` (was: Outer Oort Cloud)
  - `Sun: Gravitational Influence` (was: Sun's Gravitational Influence)
- [ ] 4 asteroid belts still render (Main Belt, Hildas, Trojans Greeks, Trojans Trojans)
- [ ] No sun direction indicator on any Sun shell
- [ ] Axis auto-scales when shells selected + Auto scale mode

### Non-Sun-centered plot (Earth or Mars)

- [ ] Sun shells render at Sun's offset position (check any shell: Photosphere, Corona, etc.)
- [ ] `corona_from_distance` checkbox gone from GUI panel
- [ ] No special checkbox needed -- just check Sun + individual shell boxes

### Animation (Sun-centered)

- [ ] Sun shells render as static traces in animated plot
- [ ] Asteroid belts render in animated plot
- [ ] Animation frames play correctly (shells don't flicker or duplicate)

---

## What Changed (summary for handoff)

| Before | After |
|--------|-------|
| `create_sun_visualization()` renders Sun shells | `create_celestial_body_visualization()` renders Sun shells |
| `create_sun_corona_from_distance()` renders 7 shells off-center | Unified dispatch renders all 18 shells off-center |
| Special `corona_from_distance` checkbox | No special checkbox -- any Sun shell works from any center |
| No axis auto-scale for Sun | Auto-scale via `_shell_outermost_radius_au` |
| 6 non-conforming legend names | All 15 shells follow `"Sun: <X>"` pattern |
| Photosphere as scatter3d | Photosphere as mesh3d (item 33 goes live) |

## Capability Gains

1. **Universal off-center Sun rendering.** All 15 sphere + 3 custom shells
   render at the Sun's offset position from any center body. Previously only
   7 shells from a subset of centers.

2. **Axis auto-scaling.** Sun-centered plots auto-scale to outermost active
   shell radius, matching planet behavior.

3. **Consistent legend naming.** All Sun shells follow `"Sun: <X>"` convention.

4. **Single info markers.** Off-center Sun shells now use the single info
   marker pattern (inherited from SHELL_CONFIGS). Previously
   `corona_from_distance` used the old multi-hover pattern.

## Lines Changed

| File | Lines removed | Lines added | Net |
|------|-------------:|------------:|----:|
| `palomas_orrery.py` | ~24 | ~52 | +28 |
| `planet_visualization.py` | ~243 | ~24 | -219 |
| **Total** | ~267 | ~76 | **-191** |

---

*Module updated: May 2026 with Anthropic's Claude Opus 4.6*
