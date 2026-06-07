# D2 Manifest: sun_position Threading

**Session:** May 20, 2026
**Executor:** Anthropic's Claude Opus 4.6
**Integrator:** Tony Quintanilla

---

## Layer 1: shared_utilities.py (COMPLETE FILE)

Delivered separately as `/mnt/user-data/outputs/shared_utilities.py`.

Changes:
- `sun_position=(0, 0, 0)` parameter added (second param, after center_position)
- Direction computed from center_position toward sun_position (was: toward origin)
- Distance is body-to-Sun (was: body-to-origin)
- Suppression: body at Sun position OR object_type=='Sun'
- Hover text: removed "Sun is at the origin" claim; added AU+km convention
- Docstring updated for Phase D2
- Credit line: May 2026 with Anthropic's Claude Opus 4.6

Backward compatibility: all existing callers pass center_position only;
sun_position defaults to (0,0,0) which preserves the old "toward origin"
behavior exactly. No caller breaks.

---

## Layer 2: planet_visualization.py (TARGETED SNIPPETS)

### Snippet 2a: create_celestial_body_visualization signature + dispatch

**BEFORE** (lines 314-316):
```python
def create_celestial_body_visualization(fig, body_name, shell_vars, animate=False, frames=None,
                                        center_position=(0, 0, 0),
                                        object_type=None, center_object=None):
```

**AFTER:**
```python
def create_celestial_body_visualization(fig, body_name, shell_vars, animate=False, frames=None,
                                        center_position=(0, 0, 0), sun_position=(0, 0, 0),
                                        object_type=None, center_object=None):
```

### Snippet 2b: custom builder dispatch (sun_position threading)

**BEFORE** (lines 385-392):
```python
        elif shell_name in customs:
            custom = customs[shell_name]
            module_path, func_name = custom['builder'].rsplit('.', 1)
            mod = importlib.import_module(module_path)
            builder = getattr(mod, func_name)
            traces = builder(center_position)
            for t in traces:
                fig.add_trace(t)
```

**AFTER:**
```python
        elif shell_name in customs:
            custom = customs[shell_name]
            module_path, func_name = custom['builder'].rsplit('.', 1)
            mod = importlib.import_module(module_path)
            builder = getattr(mod, func_name)
            # Phase D2: pass sun_position to magnetosphere builders
            if custom.get('needs_sun_position'):
                traces = builder(center_position, sun_position=sun_position)
            else:
                traces = builder(center_position)
            for t in traces:
                fig.add_trace(t)
```

### Snippet 2c: sun direction indicator (sun_position pass-through)

**BEFORE** (lines 401-408):
```python
    if outermost_radius_au > 0:
        indicator_traces = create_sun_direction_indicator(
            center_position=center_position,
            shell_radius=outermost_radius_au,
            object_type=object_type if object_type is not None else body_name,
            center_object=center_object,
        )
        for t in indicator_traces:
```

**AFTER:**
```python
    if outermost_radius_au > 0:
        indicator_traces = create_sun_direction_indicator(
            center_position=center_position,
            sun_position=sun_position,
            shell_radius=outermost_radius_au,
            object_type=object_type if object_type is not None else body_name,
            center_object=center_object,
        )
        for t in indicator_traces:
```

### Snippet 2d: create_planet_visualization signature

**BEFORE** (line 425):
```python
def create_planet_visualization(fig, planet_name, shell_vars, animate=False, frames=None, center_position=(0, 0, 0)):
```

**AFTER:**
```python
def create_planet_visualization(fig, planet_name, shell_vars, animate=False, frames=None, center_position=(0, 0, 0), sun_position=(0, 0, 0)):
```

### Snippet 2e: sun_position threading through all create_celestial_body_visualization calls

Every `return create_celestial_body_visualization(` call inside
`create_planet_visualization` needs `sun_position=sun_position` added.
There are 12 bodies (Mercury through Planet 9). Same change for all.

**Pattern -- add one line to each call:**

Mercury (line 453-459) -- add after `center_position=center_position,`:
```python
            sun_position=sun_position,
```

Repeat for Venus (465-471), Earth (478-484), Moon (492-498),
Mars (504-510), Jupiter (517-523), Saturn (530-536), Uranus (541-547),
Neptune (552-558), Pluto (563-569), Eris (574-580), Planet 9 (585-591).

Each call gets `sun_position=sun_position,` inserted after
`center_position=center_position,`.

### Snippet 2f: docstring update for create_celestial_body_visualization

In the Parameters block (after line 344), add:

```
        sun_position (tuple): (x, y, z) AU position of the Sun. Default (0,0,0)
                              is correct for heliocentric views. Body-centered
                              views pass actual Sun offset. Phase D2.
```

---

## Layer 2.5: shell_configs.py (TARGETED SNIPPETS)

Add `'needs_sun_position': True,` to all 8 magnetosphere custom entries.

**Pattern for each entry -- add one line after `'builder':` line:**

```python
            'needs_sun_position': True,
```

Lines to modify (add after the `'builder':` line at each):
- Mercury magnetosphere: after line 2085
- Venus magnetosphere: after line 2104
- Mars magnetosphere: after line 2127
- Earth magnetosphere: after line 2152
- Jupiter magnetosphere: after line 2223
- Saturn magnetosphere: after line 2295
- Uranus magnetosphere: after line 2382
- Neptune magnetosphere: after line 2443

---

## Layer 3: Magnetosphere builder sun_position wiring

### 3a: mercury_visualization_shells.py

**Signature BEFORE** (line 214):
```python
def create_mercury_magnetosphere_shell(center_position=(0, 0, 0)):
```

**Signature AFTER:**
```python
def create_mercury_magnetosphere_shell(center_position=(0, 0, 0), sun_position=(0, 0, 0)):
```

**Magnetosphere rotate_to_sunward BEFORE** (line 257):
```python
    x, y, z = rotate_to_sunward(x, y, z, center_position=center_position)
```

**AFTER:**
```python
    x, y, z = rotate_to_sunward(x, y, z, center_position=center_position, sun_position=sun_position)
```

**Bow shock rotate_to_sunward BEFORE** (lines 353-355):
```python
    bow_shock_x, bow_shock_y, bow_shock_z = rotate_to_sunward(
        bow_shock_x, bow_shock_y, bow_shock_z, center_position=center_position
    )
```

**AFTER:**
```python
    bow_shock_x, bow_shock_y, bow_shock_z = rotate_to_sunward(
        bow_shock_x, bow_shock_y, bow_shock_z, center_position=center_position, sun_position=sun_position
    )
```

### 3b: venus_visualization_shells.py

**Signature BEFORE** (line 515):
```python
def create_venus_magnetosphere_shell(center_position=(0, 0, 0)):
```

**Signature AFTER:**
```python
def create_venus_magnetosphere_shell(center_position=(0, 0, 0), sun_position=(0, 0, 0)):
```

**Magnetosphere rotate_to_sunward BEFORE** (line 552):
```python
    x, y, z = rotate_to_sunward(x, y, z, center_position=center_position)
```

**AFTER:**
```python
    x, y, z = rotate_to_sunward(x, y, z, center_position=center_position, sun_position=sun_position)
```

**Bow shock rotate_to_sunward BEFORE** (lines 681-683):
```python
    bow_shock_x, bow_shock_y, bow_shock_z = rotate_to_sunward(
        bow_shock_x, bow_shock_y, bow_shock_z, center_position=center_position
    )
```

**AFTER:**
```python
    bow_shock_x, bow_shock_y, bow_shock_z = rotate_to_sunward(
        bow_shock_x, bow_shock_y, bow_shock_z, center_position=center_position, sun_position=sun_position
    )
```

### 3c: earth_visualization_shells.py (LARGEST CHANGE -- item 4 + item 11)

Earth's magnetosphere currently does NOT call rotate_to_sunward(). It
generates geometry at origin and offsets by center_position without
rotating. This means the bow shock always points -X regardless of where
the Sun is. D2 adds rotate_to_sunward to both magnetosphere and bow shock.

**Signature BEFORE** (line 632):
```python
def create_earth_magnetosphere_shell(center_position=(0, 0, 0)):
```

**Signature AFTER:**
```python
def create_earth_magnetosphere_shell(center_position=(0, 0, 0), sun_position=(0, 0, 0)):
```

**Magnetosphere geometry BEFORE** (lines 660-669):
```python
    # Create magnetosphere main shape
    x, y, z = create_magnetosphere_shape(params)
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # 1. Add the main magnetosphere structure
    x = np.array(x) + center_x
    y = np.array(y) + center_y
    z = np.array(z) + center_z
```

**AFTER:**
```python
    # Create magnetosphere main shape (generated with -X as sunward)
    x, y, z = create_magnetosphere_shape(params)
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # 1. Add the main magnetosphere structure
    # Phase D2: rotate to face actual Sun direction with magnetic tilt.
    # Earth's magnetic dipole is tilted ~11 deg from its rotation axis.
    x, y, z = np.array(x), np.array(y), np.array(z)
    x, y, z = rotate_to_sunward(
        x, y, z, center_position=center_position,
        sun_position=sun_position, magnetic_tilt_deg=11,
    )
    x = x + center_x
    y = y + center_y
    z = z + center_z
```

**Bow shock geometry BEFORE** (lines 735-738):
```python
    # Apply center position offset
    bow_shock_x = np.array(bow_shock_x) + center_x
    bow_shock_y = np.array(bow_shock_y) + center_y
    bow_shock_z = np.array(bow_shock_z) + center_z
```

**AFTER:**
```python
    # Phase D2: rotate bow shock to face actual Sun direction.
    # Bow shock is a solar wind feature -- no magnetic tilt applied.
    bow_shock_x = np.array(bow_shock_x)
    bow_shock_y = np.array(bow_shock_y)
    bow_shock_z = np.array(bow_shock_z)
    bow_shock_x, bow_shock_y, bow_shock_z = rotate_to_sunward(
        bow_shock_x, bow_shock_y, bow_shock_z,
        center_position=center_position, sun_position=sun_position,
    )
    bow_shock_x = bow_shock_x + center_x
    bow_shock_y = bow_shock_y + center_y
    bow_shock_z = bow_shock_z + center_z
```

**IMPORT ADDITION REQUIRED.** Earth module does NOT import
rotate_to_sunward. Add this import at line 20 (after the existing
`planet_visualization_utilities` import):

```python
from orrery_rendering import rotate_to_sunward
```

The existing line 21 (`from shared_utilities import create_sun_direction_indicator`)
stays unchanged.

### 3d: mars_visualization_shells.py

**Signature BEFORE** (line 598):
```python
def create_mars_magnetosphere_shell(center_position=(0, 0, 0)):
```

**Signature AFTER:**
```python
def create_mars_magnetosphere_shell(center_position=(0, 0, 0), sun_position=(0, 0, 0)):
```

**Magnetosphere rotate_to_sunward BEFORE** (line 630):
```python
    x, y, z = rotate_to_sunward(x, y, z, center_position=center_position)
```

**AFTER:**
```python
    x, y, z = rotate_to_sunward(x, y, z, center_position=center_position, sun_position=sun_position)
```

**Bow shock rotate_to_sunward BEFORE** (lines 701-703):
```python
    bow_shock_x, bow_shock_y, bow_shock_z = rotate_to_sunward(
        bow_shock_x, bow_shock_y, bow_shock_z, center_position=center_position
    )
```

**AFTER:**
```python
    bow_shock_x, bow_shock_y, bow_shock_z = rotate_to_sunward(
        bow_shock_x, bow_shock_y, bow_shock_z, center_position=center_position, sun_position=sun_position
    )
```

### 3e: jupiter_visualization_shells.py (item 4 + item 11)

**Signature BEFORE** (line 516):
```python
def create_jupiter_magnetosphere(center_position=(0, 0, 0)):
```

**Signature AFTER:**
```python
def create_jupiter_magnetosphere(center_position=(0, 0, 0), sun_position=(0, 0, 0)):
```

**rotate_to_sunward BEFORE** (line 545):
```python
    x, y, z = rotate_to_sunward(x, y, z, center_position=center_position)
```

**AFTER:**
```python
    # Phase D2: sun_position + magnetic tilt. Jupiter's magnetic dipole
    # is tilted ~10 deg from its rotation axis.
    x, y, z = rotate_to_sunward(
        x, y, z, center_position=center_position,
        sun_position=sun_position, magnetic_tilt_deg=10,
    )
```

### 3f: saturn_visualization_shells.py

**Signature BEFORE** (line 599):
```python
def create_saturn_magnetosphere(center_position=(0, 0, 0)):
```

**Signature AFTER:**
```python
def create_saturn_magnetosphere(center_position=(0, 0, 0), sun_position=(0, 0, 0)):
```

**rotate_to_sunward BEFORE** (line 630):
```python
    x, y, z = rotate_to_sunward(x, y, z, center_position=center_position)
```

**AFTER:**
```python
    x, y, z = rotate_to_sunward(x, y, z, center_position=center_position, sun_position=sun_position)
```

### 3g: neptune_visualization_shells.py (item 12 Option C)

No signature change needed (already has sun_position).

**Item 12: Replace magnetic poles call block with single diamond marker.**

**BEFORE** (lines 595-623):
```python
    # Add magnetic poles and axis visualization - with error handling
    # Phase C4: create_neptune_magnetic_poles call site UNCHANGED (bounded scope).
    # The 4 pole/axis traces stay in Neptune's body frame; they do NOT track
    # the sunward direction. Phase D fixes via sun_position extension.
    try:
        mag_poles_traces = create_neptune_magnetic_poles(center_position, offset_distance, magnetic_tilt, azimuthal_angle)
        if mag_poles_traces and len(mag_poles_traces) > 0:
            for trace in mag_poles_traces:
                traces.append(trace)
        else:
            print("Warning: create_neptune_magnetic_poles returned empty traces")
    except Exception as e:
        print(f"Error in magnetic poles visualization: {e}")
        # Create a simple fallback trace for the magnetic center
        fallback_trace = go.Scatter3d(
            x=[center_x + 0.2 * offset_distance],
            y=[center_y + 0.1 * offset_distance],
            z=[center_z + 0.5 * offset_distance],
            mode='markers',
            marker=dict(
                size=10,
                color='yellow',
                symbol='diamond'
            ),
            name='Neptune: Magnetic Field Center (fallback)',
            showlegend=True
        )
        traces.append(fallback_trace)
```

**AFTER:**
```python
    # Phase D2 (item 12, Option C): single diamond marker for the offset
    # magnetic center. The magnetosphere shape communicates the 47-deg tilt
    # and asymmetric geometry; the axis line and pole markers removed to
    # reduce legend clutter. The offset is the one insight the shape alone
    # cannot show -- Neptune's magnetic dipole center is displaced 0.55 radii
    # from the planet center (Voyager 2, 1989).
    mag_center_x = center_x + 0.2 * offset_distance
    mag_center_y = center_y + 0.1 * offset_distance
    mag_center_z = center_z + 0.5 * offset_distance
    traces.append(go.Scatter3d(
        x=[mag_center_x], y=[mag_center_y], z=[mag_center_z],
        mode='markers',
        marker=dict(size=8, color='yellow', symbol='diamond',
                    line=dict(color='orange', width=2)),
        name='Neptune: Magnetic Field Center',
        legendgroup='Neptune: Magnetosphere',
        text=["Neptune's magnetic field center is offset ~0.55 radii from the<br>"
              "planet center (Voyager 2, 1989). Combined with the 47-degree<br>"
              "tilt between magnetic and rotation axes, this creates the most<br>"
              "asymmetric magnetosphere in the solar system."],
        hovertemplate='%{text}<extra></extra>',
        showlegend=True
    ))
```

Note: `create_neptune_magnetic_poles()` function (lines 626-758) becomes
dead code after this change. Do NOT delete it in D2 -- track as deferred
item for D3 dead code cleanup (item 6 scope). The function is only called
from the block we just replaced.

### 3h: Uranus -- no change

Already has `sun_position` in signature. Dispatch now wires it via
`needs_sun_position: True`.

---

## Layer 4: palomas_orrery.py (MODE 1 SNIPPETS -- Tony applies)

### Snippet 4a: Move _sun_pos_tuple computation before shell rendering

Currently `_sun_pos_tuple` is computed at line ~5392 (comet tails section).
We need it earlier -- before shell rendering at line ~4500. The `positions`
dict is already populated at that point (it's filled during orbit plotting).

**ADD** between line 4498 (closing brace of planet_shells_config) and
line 4500 (the `center_shells_added = False` flag):

```python
            # Sun position tuple for shell rendering (sun_position threading, D2)
            # Reused later by comet tails section
            _sun_pos_data = positions.get('Sun')
            _sun_pos_tuple = (
                (_sun_pos_data['x'], _sun_pos_data['y'], _sun_pos_data['z'])
                if _sun_pos_data and 'x' in _sun_pos_data else (0, 0, 0)
            )
```

`positions` is populated during orbit plotting (line ~4449) BEFORE shell
rendering starts at line 4500. Safe to compute here. When Sun is center,
`positions.get('Sun')` returns None, giving `(0,0,0)` -- correct (Sun IS
at origin). When Sun is non-center, its offset position is captured.

### Snippet 4b: Sun-centered static path -- no change needed

When Sun is center (line 4505), `sun_position=(0,0,0)` is correct
(Sun is at origin). The default parameter value handles this.

### Snippet 4c: Non-center planet path -- add sun_position

**BEFORE** (lines 4641-4646):
```python
                            # Always add the planet shells
                            fig = create_planet_visualization(
                                fig,                            
                                planet_name,                    
                                planet_shell_vars[planet_name], 
                                center_position=planet_data['position']  # Use planet's position
                            )
```

**AFTER:**
```python
                            # Always add the planet shells
                            fig = create_planet_visualization(
                                fig,                            
                                planet_name,                    
                                planet_shell_vars[planet_name], 
                                center_position=planet_data['position'],
                                sun_position=_sun_pos_tuple
                            )
```

### Snippet 4d: Remove double sun direction indicator (item 10)

**DELETE** lines 4648-4659:
```python
                            # Only add sun direction indicator when Sun is not the center
                            if center_object_name != 'Sun':
                                print(f"Adding Sun direction indicator for {planet_name}", flush=True)
                                sun_direction_traces = create_sun_direction_indicator(
                                    center_position=planet_data['position'],
                                    axis_range=axis_range,  # Pass the axis_range parameter
                                    object_type=planet_name,
                                    center_object=center_object_name
                                )

                                for trace in sun_direction_traces:
                                    fig.add_trace(trace)
```

The unified dispatch in `create_celestial_body_visualization()` already
emits the indicator. This explicit call was producing a second copy.

### Snippet 4e: Off-center Sun path -- add sun_position

**BEFORE** (lines 4668-4673):
```python
                        fig = create_celestial_body_visualization(
                            fig, 'Sun', sun_shell_vars,
                            center_position=sun_position,
                            object_type='Sun',
                            center_object=center_object_name,
                        )
```

Note: the local variable `sun_position` (line 4666) conflicts with the
new parameter name. This is fine -- it's the same value. But for clarity:

**AFTER:**
```python
                        fig = create_celestial_body_visualization(
                            fig, 'Sun', sun_shell_vars,
                            center_position=sun_position,
                            sun_position=(0, 0, 0),  # Sun points at itself = suppressed
                            object_type='Sun',
                            center_object=center_object_name,
                        )
```

### Snippet 4f: Remove duplicate _sun_pos_tuple at comet tails

**BEFORE** (lines 5391-5396):
```python
            # Sun position for correct tail direction when center != Sun
            _sun_pos_data = positions.get('Sun')
            _sun_pos_tuple = (
                (_sun_pos_data['x'], _sun_pos_data['y'], _sun_pos_data['z'])
                if _sun_pos_data and 'x' in _sun_pos_data else (0, 0, 0)
            )
```

**AFTER:**
```python
            # _sun_pos_tuple already computed above (D2 shell rendering)
```

### Snippet 4g: Center-body planet path -- add sun_position

When the center body IS a planet (line 4535), it's at origin and the
Sun position is in `_sun_pos_tuple`. Currently calls
`create_planet_visualization` without sun_position.

**BEFORE** (line 4535):
```python
                    fig = create_planet_visualization(fig, center_object_name, shell_vars)
```

**AFTER:**
```python
                    fig = create_planet_visualization(fig, center_object_name, shell_vars, sun_position=_sun_pos_tuple)
```

---

## Summary: Application Order

Tony should apply changes in this order:

1. **shared_utilities.py** -- replace with delivered complete file
2. **shell_configs.py** -- add `'needs_sun_position': True,` to 8 entries
3. **planet_visualization.py** -- apply snippets 2a-2f
4. **earth_visualization_shells.py** -- check import, apply snippet 3c
5. **mercury_visualization_shells.py** -- apply snippet 3a
6. **venus_visualization_shells.py** -- apply snippet 3b
7. **mars_visualization_shells.py** -- apply snippet 3d
8. **jupiter_visualization_shells.py** -- apply snippet 3e
9. **saturn_visualization_shells.py** -- apply snippet 3f
10. **neptune_visualization_shells.py** -- apply snippet 3g
11. **palomas_orrery.py** -- apply snippets 4a, 4c, 4d, 4e, 4f, 4g

---

## Verification Checklist

| Test | Expected |
|------|----------|
| All modified files compile (`python3 -m py_compile`) | PASS |
| `shared_utilities.py`: indicator with sun_position=(0,0,0) matches old behavior | Same direction as before |
| `shared_utilities.py`: indicator with sun_position != origin points correctly | Arrow toward sun_position |
| `shell_configs.py`: 8 entries have `needs_sun_position: True` | 8 entries |
| Sun-centered plot: no indicator (suppressed at origin) | Unchanged |
| Earth-centered plot: indicator points toward Sun offset | Arrow toward Sun |
| Earth-centered plot: magnetosphere bow shock faces Sun | Bow shock rotated |
| Earth magnetosphere: 11-deg magnetic tilt visible | Slight asymmetry |
| Jupiter magnetosphere: 10-deg magnetic tilt visible | Slight asymmetry |
| Neptune: single diamond marker, no axis line or pole markers | 1 trace vs 4 |
| No double indicator on non-center planets | 1 indicator, not 2 |
| LF line endings: all files | PASS |
| ASCII encoding: all files | PASS |

### Mode 5 visual tests (Tony)

1. Sun-centered static: unchanged behavior (all shells, indicators suppressed)
2. Earth-centered static: bow shock should face Sun offset, ~11-deg tilt
3. Jupiter-centered static: bow shock should face Sun, ~10-deg tilt
4. Neptune-centered static: diamond marker present, no axis/poles
5. Any planet off-center from Sun: indicator arrow points toward Sun
6. Animation: unchanged (D2 does not wire animation path)

---

## Items Resolved

| Item | Status |
|-----:|--------|
| 4 | **DONE** -- sun_position threaded through all 3 layers |
| 10 | **DONE** -- double indicator removed (snippet 4d) |
| 11 | **DONE** -- Earth 11 deg, Jupiter 10 deg wired |
| 12 | **DONE (Option C)** -- single diamond marker, poles/axis removed |

---

## Credit

```
Module updated: May 2026 with Anthropic's Claude Opus 4.6
```
