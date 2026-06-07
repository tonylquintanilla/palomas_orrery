# Exoplanet Implementation Quick Start Guide
## Solidified Framework - Ready to Build

**Date:** October 21, 2025  
**Status:** Framework complete, ready for Phase 1 implementation

---

## Core Decisions (Finalized)

### 1. Architecture Pattern
- **Reuse existing pipeline:** `plot_objects()` and `animate_objects()` already support arbitrary central objects
- **Minimal code surgery:** Add new object types, not new rendering logic
- **Proven approach:** Mirrors how Solar System was built (hardcoded → API)

### 2. Data Strategy (Phase 1)
```
HARDCODE FIRST → TEST → THEN ADD API
```

**Why hardcode?**
- ✅ Faster MVP (2-3 weeks vs. 4-6 weeks)
- ✅ Predictable testing (no network failures)
- ✅ Focus on visualization bugs, not data parsing
- ✅ Matches Solar System development pattern

**What to hardcode:**
- TRAPPIST-1 (7 planets, single star)
- TOI-1338 (2 planets, binary stars)
- Proxima Centauri (1 planet, high proper motion)

### 3. Binary Stars (TOI-1338)
**Hybrid Approach:**

```python
# Functional: Barycenter simplifies planet calculations
center_position = (0, 0, 0)  # All planets orbit this point

# Visual: Show both stars as orbiting objects
star_A = {
    'object_type': 'exo_host_star',
    'orbit_around': 'barycenter',
    'semi_major_axis_au': 0.015,  # From center of mass
    'period_days': 14.6,
    'phase_offset': 0.0
}

star_B = {
    'object_type': 'exo_host_star',
    'orbit_around': 'barycenter',
    'semi_major_axis_au': 0.045,  # From center of mass
    'period_days': 14.6,
    'phase_offset': 180.0  # Opposite side
}
```

**Advantages:**
- Planets calculations stay simple (circular barycenter)
- Users see binary dynamics (educational)
- Reuses existing orbit rendering code
- Optional toggle for stellar orbits

### 4. Coordinate System
**Independent Local Frames - NOT connected to Solar System**

```
Each exoplanet system:
  Origin: Host star barycenter at (0, 0, 0)
  XY plane: Sky plane (perpendicular to Earth line of sight)
  Z axis: Toward Earth
  
Default view: XY plane (face-on)
User rotates: Same as plot_objects() behavior
```

**No "exoplanet ecliptic":**
- First Point of Aries is Earth-centric (vernal equinox)
- Exoplanet orbital planes are arbitrary relative to our ecliptic
- Each system stands alone in its own frame

**Connection to Solar System only via:**
- Host star (RA, Dec, Distance) for context
- In Phase 4: stellar visualization can show "this star has planets"

### 5. Time System
**Use UTC throughout**

```python
# Simple approach (no TDB needed):
from datetime import datetime, timezone

def calculate_exoplanet_position(planet, date_utc):
    """
    No need for TDB because:
    - Not mixing with JPL Horizons (separate systems)
    - Orbital elements are epoch-independent
    - Proper motion uses years, not precise scales
    """
    # Ensure UTC
    if date_utc.tzinfo is None:
        date_utc = date_utc.replace(tzinfo=timezone.utc)
    
    # Calculate position using Keplerian elements
    ...
```

### 6. GUI Integration
**Add section to existing palomas_orrery.py**

```python
# After spacecraft section, before stellar visualization button

exoplanet_frame = tk.LabelFrame(
    scrollable_frame,
    text="Exoplanetary Systems 🌍🌠",
    bg='#000033', 
    fg='white'
)

# System selection
system_var = tk.StringVar(value='Select System')
system_dropdown = ttk.Combobox(
    exoplanet_frame,
    textvariable=system_var,
    values=['TRAPPIST-1', 'TOI-1338', 'Proxima Centauri'],
    state='readonly'
)

# When system selected, populate planet checkboxes
def on_system_selected(event):
    system_name = system_var.get()
    populate_exoplanet_checkboxes(system_name, exoplanet_frame)
```

---

## Phase 1 Implementation Plan (2-3 Weeks)

### Week 1: Core Infrastructure

**Day 1-2:** Data structures
```python
# Create exoplanet_systems.py
TRAPPIST1_SYSTEM = {
    'host_star': {...},  # RA, Dec, distance, spectral type
    'planets': [
        {'name': 'TRAPPIST-1 b', 'period_days': 1.51, ...},
        # ... 7 planets total
    ]
}

TOI1338_SYSTEM = {
    'host_star': {
        'is_binary': True,
        'star_A': {...},
        'star_B': {...},
        'binary_period_days': 14.6,
        'binary_separation_au': 0.06
    },
    'planets': [
        {'name': 'TOI-1338 b', 'period_days': 95.2, ...},
        {'name': 'TOI-1338 c', 'period_days': 215.5, ...}
    ]
}
```

**Day 3-4:** Orbit calculations
```python
# Create exoplanet_orbits.py

def calculate_keplerian_orbit(a, e, i, omega, Omega, period, date):
    """
    Same math as idealized_orbits.py
    Returns x, y, z in local sky-plane frame
    """
    # Solve Kepler's equation
    # Calculate true anomaly
    # Apply rotations: Ω, i, ω
    return x, y, z

def plot_exoplanet_orbits(fig, exo_objects, date):
    """
    Main plotting function - called from plot_objects()
    """
    for planet in exo_objects:
        if planet['object_type'] != 'exoplanet':
            continue
        
        x, y, z = calculate_keplerian_orbit(...)
        
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='lines',
            name=planet['name'],
            ...
        ))
    
    return fig
```

**Day 5:** Binary star handling
```python
# In exoplanet_orbits.py

def create_binary_orbits(star_A_mass, star_B_mass, separation, period):
    """
    Calculate stellar orbits around barycenter
    """
    total_mass = star_A_mass + star_B_mass
    a_A = separation * (star_B_mass / total_mass)
    a_B = separation * (star_A_mass / total_mass)
    
    return {
        'star_A': {'a': a_A, 'e': 0.0, 'period': period, 'phase': 0},
        'star_B': {'a': a_B, 'e': 0.0, 'period': period, 'phase': 180}
    }
```

### Week 2: GUI Integration

**Day 6-7:** Add to objects list
```python
# In palomas_orrery.py

# Add after spacecraft section
trappist1b_var = tk.IntVar(value=0)
# ... (7 planets)
toi1338b_var = tk.IntVar(value=0)
toi1338c_var = tk.IntVar(value=0)
toi1338_starA_var = tk.IntVar(value=0)
toi1338_starB_var = tk.IntVar(value=0)

objects.extend([
    # TRAPPIST-1 system
    {'name': 'TRAPPIST-1 (star)', 'id': 'trappist1_star', 
     'var': trappist1_star_var, 'object_type': 'exo_host_star', ...},
    {'name': 'TRAPPIST-1 b', 'id': 'trappist1b', 
     'var': trappist1b_var, 'object_type': 'exoplanet',
     'host_star': 'trappist1_star', 'semi_major_axis_au': 0.01154, ...},
    # ... other planets
    
    # TOI-1338 system
    {'name': 'TOI-1338 A', 'id': 'toi1338_starA', ...},
    {'name': 'TOI-1338 B', 'id': 'toi1338_starB', ...},
    {'name': 'TOI-1338 b', 'id': 'toi1338b', 
     'object_type': 'exoplanet', 'host_star': 'toi1338_barycenter', ...},
])
```

**Day 8-9:** GUI controls
```python
# Create exoplanet section with system dropdown
# When system selected, enable relevant planet checkboxes
# Add info labels showing system distance, number of planets
```

**Day 10:** Integration with plot_objects()
```python
# In plot_objects() function, after idealized orbits:

# Plot exoplanet orbits
exo_objects = [obj for obj in selected_objects 
               if obj['object_type'] == 'exoplanet']
if exo_objects:
    fig = plot_exoplanet_orbits(fig, exo_objects, current_date)

# Plot host stars
host_stars = [obj for obj in selected_objects 
              if obj['object_type'] == 'exo_host_star']
# Add star markers at (0,0,0) or binary positions
```

### Week 3: Polish & Testing

**Day 11-12:** Proper motion (Proxima Cen)
```python
# Create exoplanet_coordinates.py

def apply_proper_motion(ra, dec, pmra, pmdec, epoch, target_date):
    """
    For nearby stars with high proper motion
    Proxima Cen: 3853.92 mas/yr in RA, -768.34 mas/yr in Dec
    """
    years = (target_date - epoch).total_seconds() / (365.25 * 86400)
    ra += (pmra / 3600000) * years  # mas/yr to deg
    dec += (pmdec / 3600000) * years
    return ra, dec
```

**Day 13:** Hover text with assumptions
```python
def format_exoplanet_hover(planet):
    text = f"<b>{planet['name']}</b><br>"
    text += f"Period: {planet['period_days']:.2f} days<br>"
    
    # Annotate defaults
    if planet.get('e_assumed'):
        text += f"Eccentricity: {planet['e']:.4f} (assumed circular)<br>"
    
    text += f"Discovery: {planet['discovery_method']} ({planet['discovery_year']})"
    return text
```

**Day 14-15:** Testing & validation
- Test TRAPPIST-1: 7 planets, periods match literature
- Test TOI-1338: binary orbits, circumbinary planet
- Test Proxima: proper motion across 50 years
- Test animation: frame rates, smooth motion
- Test axis framing: tight bounds for each system

---

## Code Snippets: Key Functions

### 1. Main Integration Point
```python
# In palomas_orrery.py, plot_objects() function

def plot_objects():
    # ... existing solar system code ...
    
    # NEW: Add exoplanet orbits
    selected_objects = [obj for obj in objects if obj['var'].get() == 1]
    exo_objects = [obj for obj in selected_objects 
                   if obj.get('object_type') == 'exoplanet']
    
    if exo_objects:
        from exoplanet_orbits import plot_exoplanet_orbits
        fig = plot_exoplanet_orbits(fig, exo_objects, current_date)
    
    # ... rest of plotting code ...
```

### 2. Keplerian Orbit Calculation
```python
# In exoplanet_orbits.py

def calculate_keplerian_orbit(a, e, i_deg, omega_deg, Omega_deg, 
                              period_days, epoch, date, num_points=360):
    """
    Calculate orbit in local sky-plane frame
    
    Uses same rotation sequence as idealized_orbits.py:
    1. Calculate position in perifocal frame (orbit plane)
    2. Rotate by ω (argument of periastron)
    3. Rotate by i (inclination)
    4. Rotate by Ω (longitude of ascending node)
    """
    import numpy as np
    
    # Mean anomaly
    days_since_epoch = (date - epoch).total_seconds() / 86400
    M = (2 * np.pi / period_days) * days_since_epoch
    
    # Solve Kepler's equation for E (eccentric anomaly)
    E = M
    for _ in range(10):  # Newton's method
        E = E - (E - e * np.sin(E) - M) / (1 - e * np.cos(E))
    
    # True anomaly
    nu = 2 * np.arctan2(
        np.sqrt(1 + e) * np.sin(E / 2),
        np.sqrt(1 - e) * np.cos(E / 2)
    )
    
    # Distance
    r = a * (1 - e**2) / (1 + e * np.cos(nu))
    
    # Position in orbital plane
    theta = np.linspace(0, 2*np.pi, num_points)
    x_orb = r * np.cos(theta)
    y_orb = r * np.sin(theta)
    z_orb = np.zeros_like(x_orb)
    
    # Apply rotations (reuse from idealized_orbits.py)
    from idealized_orbits import rotate_points
    x, y, z = rotate_points(x_orb, y_orb, z_orb, 
                            i_deg, omega_deg, Omega_deg)
    
    return x, y, z
```

### 3. Binary Star Orbits
```python
# In exoplanet_orbits.py

def add_binary_stars_to_plot(fig, system_data, date):
    """
    Add both stars orbiting barycenter
    """
    star_A = system_data['host_star']['star_A']
    star_B = system_data['host_star']['star_B']
    
    # Calculate masses and separation
    m_A = star_A['mass_solar']
    m_B = star_B['mass_solar']
    total_mass = m_A + m_B
    separation = system_data['host_star']['binary_separation_au']
    
    # Semi-major axes from barycenter
    a_A = separation * (m_B / total_mass)
    a_B = separation * (m_A / total_mass)
    
    # Calculate positions (simplified: circular, coplanar)
    period = system_data['host_star']['binary_period_days']
    angle = (2 * np.pi / period) * days_since_epoch
    
    # Star A
    x_A = a_A * np.cos(angle)
    y_A = a_A * np.sin(angle)
    
    # Star B (opposite side)
    x_B = -a_B * np.cos(angle)
    y_B = -a_B * np.sin(angle)
    
    # Add to plot
    fig.add_trace(go.Scatter3d(
        x=[x_A], y=[y_A], z=[0],
        mode='markers',
        marker=dict(size=8, color='yellow'),
        name='TOI-1338 A',
        ...
    ))
    
    fig.add_trace(go.Scatter3d(
        x=[x_B], y=[y_B], z=[0],
        mode='markers',
        marker=dict(size=5, color='orange'),
        name='TOI-1338 B',
        ...
    ))
    
    return fig
```

---

## Testing Checklist

### TRAPPIST-1
- [ ] All 7 planets visible
- [ ] Orbital periods match (1.51, 2.42, 4.05, 6.10, 9.21, 12.35, 18.77 days)
- [ ] Planets in habitable zone (e, f, g) labeled
- [ ] Tight axis framing (~0.074 AU)
- [ ] Animation shows orbital resonances
- [ ] Hover text shows discovery method (Transit, 2017)

### TOI-1338
- [ ] Both stars orbit barycenter
- [ ] Stars 180° apart (opposite sides)
- [ ] Period matches (14.6 days for stars)
- [ ] Planet b orbits at 0.46 AU with 95.2 day period
- [ ] Planet c orbits at larger distance
- [ ] Binary separation ~0.06 AU visible
- [ ] Hover shows "Wolf Cukier (TESS intern)" discoverer
- [ ] Circumbinary annotation present

### Proxima Centauri
- [ ] High proper motion applied (position shifts over decades)
- [ ] Planet at ~0.05 AU, period 11.2 days
- [ ] Annotation: "Nearest exoplanet system (4.24 ly)"
- [ ] Test animation from 2000 to 2050 (proper motion visible)

### General
- [ ] Axis range auto-calculates per system
- [ ] No blank space outside orbits
- [ ] Colors distinct from Solar System objects
- [ ] Missing parameters labeled in hover text
- [ ] Animation smooth (>20 fps)
- [ ] Can select/deselect individual planets

---

## Next Steps After Phase 1

### Phase 2: API Integration (Weeks 4-6)
1. Create `exoplanet_data_acquisition.py`
2. Query NASA Exoplanet Archive TAP service
3. Parse and cache system data
4. Add 7 more systems dynamically
5. Implement search/filter by distance, method, year

### Phase 3: Advanced Features (Weeks 7-9)
1. Habitable zone visualization (green torus)
2. Comparison with Solar System (overlay)
3. Size/mass comparison charts
4. Discovery timeline animation

### Phase 4: Stellar Integration (Weeks 10-12)
1. Link with `star_visualization_gui.py`
2. Click star → see exoplanets
3. 3D neighborhood with "has planets" markers
4. Filter: "All systems within 100 ly"

---

## Success Criteria

**Phase 1 is complete when:**
1. ✅ TRAPPIST-1 system visualizes correctly (7 planets)
2. ✅ TOI-1338 binary system works (2 stars + 2 planets)
3. ✅ Proxima Cen with proper motion across time
4. ✅ Animation is smooth and accurate
5. ✅ Code is clean, commented, and maintainable
6. ✅ Paloma can show friends "real Tatooine" in the orrery! 🌟🌟

---

**Ready to implement? Let's build Phase 1!** 🚀
