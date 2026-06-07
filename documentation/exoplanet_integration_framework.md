# Exoplanet System Integration Framework
## Conceptual Design for Paloma's Orrery

**Created:** October 21, 2025  
**Updated:** October 21, 2025 (Framework Solidified)  
**Purpose:** Integrate exoplanetary systems into the existing orrery visualization architecture

---

## Key Decisions Summary

### ✅ **Finalized Architectural Decisions**

1. **GUI Location:** Integrated into main `palomas_orrery.py` (not separate window)
   
2. **Data Strategy:** Start with hardcoded parameters (Phase 1), add API later (Phase 2)
   - Mirrors successful Solar System development approach
   - Faster MVP, predictable testing
   
3. **Binary Star Systems:** Hybrid approach
   - Functional: Barycenter at (0, 0, 0) for planet calculations
   - Visual: Both stars shown as orbiting objects for education
   - Stars treated like "special planets" with their own orbits
   
4. **Coordinate System:** Independent local frames (NOT connected to Solar System ecliptic)
   - Each system has own coordinate frame
   - XY = sky plane (perpendicular to line of sight)
   - Z = toward Earth
   - No "exoplanet ecliptic" - each system stands alone
   
5. **Time System:** UTC throughout (no TDB needed since independent from Horizons)

6. **View Default:** XY plane (face-on), user rotates as desired
   - Same pattern as `plot_objects()` default view

7. **Implementation Sequence:**
   - Phase 1: TRAPPIST-1 → TOI-1338 → Proxima Cen (hardcoded)
   - Phase 2: NASA Archive API + 7 more systems
   - Phase 3: Advanced features (habitable zones, comparisons)
   - Phase 4: Integration with stellar visualization

---

## Executive Summary

This framework proposes integrating exoplanetary systems into Paloma's Orrery by creating a new class of objects with their own host stars as central bodies, while reusing the existing visualization architecture. The implementation will enable users to visualize confirmed exoplanet systems with accurate orbital mechanics, leveraging NASA Exoplanet Archive data.

---

## 1. Architecture Overview

### 1.1 Core Design Principles

1. **Reuse existing visualization pipeline** - `plot_objects()` and `animate_objects()` already support arbitrary central bodies
2. **Extend object model** - Add new object type: `'exoplanet'` with associated `'host_star'`
3. **Parallel data structure** - Create separate exoplanet catalogs that integrate seamlessly with existing objects list
4. **Modular implementation** - Keep exoplanet code in dedicated modules for maintainability

### 1.2 Key Architectural Components

```
┌─────────────────────────────────────────────────────────────┐
│                   PALOMA'S ORRERY GUI                       │
│  (palomas_orrery.py or new exoplanet_orrery_gui.py)       │
└──────────────────┬──────────────────────────────────────────┘
                   │
      ┌────────────┴────────────┐
      │                         │
┌─────▼──────────┐    ┌────────▼────────────┐
│ Solar System   │    │ Exoplanet Systems   │
│ Objects List   │    │ Objects List        │
│ (existing)     │    │ (new)               │
└─────┬──────────┘    └────────┬────────────┘
      │                        │
      └────────┬───────────────┘
               │
    ┌──────────▼──────────────┐
    │  UNIFIED VISUALIZATION  │
    │  - plot_objects()       │
    │  - animate_objects()    │
    │  - plot_idealized_orbits│
    └──────────┬──────────────┘
               │
    ┌──────────▼──────────────┐
    │  DATA SOURCES           │
    │  - JPL Horizons (solar) │
    │  - NASA Exo Archive     │
    │  - SIMBAD (stars)       │
    └─────────────────────────┘
```

---

## 2. Data Structure Design

### 2.1 Exoplanet Object Structure

Extend the existing object dictionary format:

```python
{
    'name': 'Kepler-16 b',              # Exoplanet name
    'id': 'kepler16b',                   # Unique identifier
    'var': kepler16b_var,                # Tkinter variable
    'color': color_map('exoplanet'),     # Visualization color
    'symbol': 'circle',                   # Plot symbol
    'object_type': 'exoplanet',          # NEW TYPE
    'id_type': 'exoplanet',              # NEW ID TYPE
    
    # Exoplanet-specific fields
    'host_star': 'Kepler-16',            # Parent star name
    'host_star_id': 'kepler16',          # Star unique ID
    'host_ra': 19.1651,                  # Right ascension (deg)
    'host_dec': 51.7662,                 # Declination (deg)
    'host_distance': 60.0,               # Distance (pc)
    
    # Orbital parameters (from NASA Exoplanet Archive)
    'semi_major_axis_au': 0.7048,        # Semi-major axis
    'eccentricity': 0.0069,              # Eccentricity
    'inclination_deg': 90.0322,          # Inclination
    'period_days': 228.776,              # Orbital period
    'omega_deg': 0.0,                    # Argument of periastron
    'Omega_deg': 0.0,                    # Long. of ascending node
    
    # Physical parameters
    'mass_jupiter': 0.333,               # Mass in Jupiter masses
    'radius_jupiter': 0.7538,            # Radius in Jupiter radii
    'discovery_method': 'Transit',       # Discovery method
    'discovery_year': 2011,              # Year discovered
    
    'mission_info': 'Circumbinary planet...',
    'mission_url': 'https://exoplanetarchive.ipac.caltech.edu/...'
}
```

### 2.2 Host Star Object Structure

```python
{
    'name': 'Kepler-16 A/B',            # Binary system or single star
    'id': 'kepler16_star',              # Star identifier
    'var': kepler16_star_var,           # Tkinter variable
    'color': color_map('star'),         # Star color
    'symbol': 'star',                   # Plot symbol
    'object_type': 'exo_host_star',     # NEW TYPE
    'id_type': 'host_star',             # NEW ID TYPE
    
    # Stellar parameters
    'spectral_type': 'K0V + M5V',       # Spectral classification
    'stellar_mass_solar': 0.6897 + 0.2026,  # Combined mass
    'stellar_radius_solar': 0.6489 + 0.2261, # Combined radius
    'effective_temp_k': 4450,           # Temperature
    'ra': 19.1651,                      # Right ascension
    'dec': 51.7662,                     # Declination
    'distance_pc': 60.0,                # Distance from Earth
    
    'mission_info': 'Host star of...',
    'mission_url': 'http://simbad.u-strasbg.fr/simbad/...'
}
```

---

## 3. Data Acquisition

### 3.1 NASA Exoplanet Archive Integration

**Create new module:** `exoplanet_data_acquisition.py`

```python
def fetch_exoplanet_systems(selection_criteria):
    """
    Fetch exoplanet data from NASA Exoplanet Archive
    
    Parameters:
        selection_criteria: dict with keys like:
            - 'max_distance_pc': Maximum distance from Earth
            - 'min_planets': Minimum number of planets in system
            - 'discovery_method': ['Transit', 'Radial Velocity', etc.]
            - 'has_mass': True/False - require mass measurement
            - 'confirmed_only': True/False
    
    Returns:
        Dictionary of exoplanet systems with orbital parameters
    """
    # Use NASA Exoplanet Archive TAP service
    # URL: https://exoplanetarchive.ipac.caltech.edu/TAP/
    pass

def calculate_exoplanet_positions(exoplanet, date, host_star_position):
    """
    Calculate 3D position of exoplanet at given date
    
    Uses Keplerian orbital elements, similar to idealized_orbits.py
    but centered on the host star instead of the Sun
    """
    pass
```

### 3.2 Data Sources

1. **NASA Exoplanet Archive** (primary)
   - TAP service: https://exoplanetarchive.ipac.caltech.edu/TAP/
   - Planetary Systems Composite Data table
   - Contains: orbital parameters, physical properties, discovery info

2. **SIMBAD** (stellar properties)
   - Already integrated in `simbad_manager.py`
   - Use for detailed stellar characteristics

3. **Gaia** (stellar positions/distances)
   - Already integrated in `data_acquisition.py`
   - Use for accurate stellar coordinates

---

## 4. Visualization Implementation

### 4.1 Integration with Existing Pipeline

**Key insight:** The existing `plot_objects()` and `animate_objects()` functions already support arbitrary central objects!

```python
# Current architecture supports this:
center_object_name = center_object_var.get()  # Can be anything!
center_id = center_object_info['id']

# For exoplanets:
center_object_name = 'Kepler-16 A/B'  # The host star
center_id = 'kepler16_star'
```

### 4.2 Binary Star Visualization Strategy (Hybrid Approach)

**For systems like TOI-1338 (binary stars):**

**Approach:** Treat binary system as single barycentric center with optional stellar visualization

1. **Functional center:** Barycenter at (0, 0, 0)
   - Planets orbit the combined gravitational center
   - Simplified calculation: `center_position = (0, 0, 0)`

2. **Visual representation:** Both stars shown orbiting barycenter
   - Stars treated as special "planet-like" objects
   - Each star has its own orbital parameters around barycenter
   - Educational interest: shows binary dynamics
   - Optional toggle: "Show stellar orbits"

**Implementation:**
```python
def create_binary_system_objects(star1_mass, star2_mass, 
                                 binary_period, binary_separation):
    """
    Create orbital parameters for both stars around barycenter
    
    Returns:
        star1_orbit_params: dict with a, e, i, period for star 1
        star2_orbit_params: dict with a, e, i, period for star 2
    """
    total_mass = star1_mass + star2_mass
    
    # Semi-major axes (from center of mass)
    a1 = binary_separation * (star2_mass / total_mass)
    a2 = binary_separation * (star1_mass / total_mass)
    
    # Both stars have same period and phase (180° apart)
    return {
        'star1': {'a': a1, 'e': 0.0, 'period': binary_period, 'phase': 0.0},
        'star2': {'a': a2, 'e': 0.0, 'period': binary_period, 'phase': 180.0}
    }
```

**Advantages:**
- ✅ Barycenter makes planet calculations simple
- ✅ Stellar orbits add educational value
- ✅ Can toggle stellar motion on/off
- ✅ Reuses existing planet orbit rendering code
- ✅ Scales to triple star systems (e.g., Alpha Centauri if we add planets there)

### 4.3 Position Calculation Strategy

Two approaches:

#### Option A: Extend `fetch_trajectory()` 
```python
# In palomas_orrery_helpers.py
def fetch_trajectory(object_id, dates_list, center_id='Sun', id_type=None):
    if id_type == 'exoplanet':
        # Calculate positions using Keplerian elements
        # relative to host star coordinates
        return calculate_exoplanet_trajectory(object_id, dates_list, center_id)
    else:
        # Existing JPL Horizons code
        ...
```

#### Option B: Extend `plot_idealized_orbits()` (Recommended)
```python
# In idealized_orbits.py or new exoplanet_orbits.py
def plot_exoplanet_orbits(fig, exoplanet_objects, date, center_position):
    """
    Plot exoplanet orbits using Keplerian elements
    
    Similar to existing planetary orbit plotting but:
    - Uses host star as center instead of Sun
    - Scales appropriately (typically < 10 AU)
    - Handles binary star systems
    """
    pass
```

### 4.4 Coordinate System Considerations

**Key Decision:** Exoplanet systems are **independent coordinate frames**, NOT connected to Solar System ecliptic

**Approach:**
1. **Local coordinate system** for each exoplanet system
   - Origin: Host star barycenter
   - XY plane: Sky plane (perpendicular to line of sight from Earth)
   - Z axis: Points toward Earth (line of sight)
   - NO attempt to align with Solar System ecliptic or First Point of Aries

2. **Default view:** XY plane (face-on, same as `plot_objects` default)
   - User can rotate view as desired
   - Natural orientation for transiting systems

3. **Stellar positioning in space** (for context, not visualization)
   - Convert (RA, Dec, Distance) → (X_gal, Y_gal, Z_gal) in galactic coords
   - Used only if showing multiple exoplanet systems together
   - Or in stellar visualization module with "this star has planets" marker

**No "exoplanet ecliptic" equivalent:**
- Each system is isolated in its own local frame
- First Point of Aries is Earth-centric concept (vernal equinox)
- Exoplanet orbital planes are arbitrary relative to our ecliptic
- Connection to Earth viewing geometry is through RA/Dec of host star only

**Implementation:**
```python
def create_exoplanet_coordinate_frame(host_star_ra, host_star_dec):
    """
    Create local coordinate system for exoplanet system
    
    Returns:
        Local frame with Z toward Earth, XY as sky plane
        NO connection to Solar System ecliptic
    """
    # Sky plane coordinate system
    # X-axis: Arbitrary direction in sky plane (e.g., toward celestial north)
    # Y-axis: Perpendicular in sky plane
    # Z-axis: Line of sight to Earth (positive = toward observer)
    
    # For visualization: Origin at (0,0,0) = host star barycenter
    # User rotates as desired from default XY view
    pass
```

**Connection to Solar System (future Phase 4):**
```python
# Only in star_visualization_gui.py context:
def show_exoplanet_host_in_stellar_map(host_star):
    """
    Place host star in 3D stellar neighborhood map
    
    Uses (RA, Dec, Distance) to position star in galactic frame
    Adds marker: "This star has X planets"
    User can click to open exoplanet system view
    """
    pass
```

### 4.5 Orbit Calculation (Keplerian Elements)

**Standard Keplerian orbit in orbital plane:**

```python
def calculate_keplerian_orbit(a, e, i, omega, Omega, period, date, num_points=360):
    """
    Calculate 3D orbit from Keplerian elements in local sky-plane frame
    
    Parameters:
        a: semi-major axis (AU)
        e: eccentricity
        i: inclination (degrees) - angle between orbital plane and sky plane
        omega: argument of periastron (degrees)
        Omega: longitude of ascending node (degrees) - orientation in sky plane
        period: orbital period (days)
        date: observation date (for mean anomaly calculation)
        num_points: number of points along orbit
    
    Returns:
        x, y, z: arrays of positions in local coordinate frame
    """
    # Calculate mean anomaly from epoch
    M = (2 * np.pi / period) * days_since_epoch
    
    # Solve Kepler's equation for eccentric anomaly E
    E = solve_kepler(M, e)
    
    # True anomaly
    nu = 2 * np.arctan2(np.sqrt(1+e) * np.sin(E/2), 
                         np.sqrt(1-e) * np.cos(E/2))
    
    # Distance from focus
    r = a * (1 - e**2) / (1 + e * np.cos(nu))
    
    # Position in orbital plane (perifocal frame)
    x_orb = r * np.cos(nu)
    y_orb = r * np.sin(nu)
    z_orb = 0
    
    # Rotate to sky plane using standard rotation sequence
    # Same as idealized_orbits.py for Solar System
    x, y, z = rotate_orbit_to_skyplane(x_orb, y_orb, z_orb, 
                                        i, omega, Omega)
    
    return x, y, z
```

**Advantages of this approach:**
- ✅ Reuses existing rotation mathematics from `idealized_orbits.py`
- ✅ Natural orientation (XY = sky plane, Z = line of sight)
- ✅ User familiar with rotation controls
- ✅ No artificial connection to Solar System ecliptic
---

## 5. GUI Design Options

### Option A: Integrated GUI (Recommended for MVP)

**Pros:**
- Single interface
- Easy comparison between solar system and exoplanets
- Reuse all existing controls

**Cons:**
- GUI could become cluttered
- Different data sources/behaviors may confuse users

**Implementation:**
```python
# In palomas_orrery.py

# Add new section after spacecraft
exoplanet_frame = tk.LabelFrame(scrollable_frame, 
                                text="Exoplanetary Systems",
                                bg='#000033', fg='white')

# Add system selection dropdown
system_var = tk.StringVar(value='Select System')
system_menu = ttk.Combobox(exoplanet_frame, 
                           textvariable=system_var,
                           values=['TRAPPIST-1', 'Kepler-16', 
                                   'Proxima Centauri', ...])

# Populate planets when system selected
def on_system_selected(event):
    system = system_var.get()
    populate_exoplanets(system, exoplanet_frame)
```

### Option B: Separate GUI

**Pros:**
- Cleaner separation of concerns
- Can optimize UI for exoplanet-specific features
- Easier to maintain

**Cons:**
- Code duplication
- User must launch separate window
- May feel disconnected from main orrery

**Implementation:**
```python
# New file: exoplanet_orrery_gui.py

class ExoplanetOrreryGUI:
    """
    Separate GUI for exoplanet visualization
    Inherits core plotting from palomas_orrery architecture
    """
    def __init__(self):
        # Create new window
        self.root = tk.Tk()
        self.root.title("Exoplanet Systems - Paloma's Orrery")
        
        # Import and reuse visualization functions
        from palomas_orrery_helpers import plot_objects, animate_objects
        
        # Custom exoplanet controls
        ...
```

### Recommendation: **Start with Option A (Integrated)**

Rationale:
- Faster to implement
- Better user experience (everything in one place)
- Can always split later if GUI becomes unwieldy
- Maintains consistency with existing architecture

---

## 6. Featured Exoplanet Systems

### 6.1 Selection Criteria for Initial Implementation

**Scientific Interest:**
1. **TRAPPIST-1** - 7 terrestrial planets, 3 in habitable zone
2. **Kepler-16** - Circumbinary "Tatooine" planet
3. **Proxima Centauri** - Nearest exoplanet, potentially habitable
4. **51 Pegasi** - First exoplanet around sun-like star (historical)
5. **HD 209458** - First transiting exoplanet
6. **Kepler-452** - "Earth's cousin" in habitable zone

**Diversity of Systems:**
- Single star vs. binary systems
- Hot Jupiters vs. terrestrial planets
- Tight orbits (< 0.1 AU) vs. wide orbits (> 1 AU)
- Various discovery methods (transit, RV, direct imaging)

### 6.2 Data Completeness Requirements

For visualization, require:
- ✅ Orbital period
- ✅ Semi-major axis OR period (can derive other)
- ✅ Stellar distance (for positioning in space)
- ✅ Host star RA/Dec
- ⚠️ Eccentricity (default to 0 if unknown)
- ⚠️ Inclination (default to 90° for transiting planets)
- ⚠️ Argument of periastron (default to 0° if unknown)

---

## 7. Implementation Phases

### Phase 1: Core Infrastructure (MVP)
**Goal:** Visualize 2 exoplanet systems (single star + binary star) in main GUI

**Approach:** Following the successful pattern from initial Paloma's Orrery development:
1. Start with **hardcoded parameters** and Keplerian calculations
2. Get visualization working and tested
3. Later add live data fetching from NASA Archive

**Rationale for Hardcoding First:**
- ✅ **Faster MVP** - No API integration complexity upfront
- ✅ **Predictable testing** - Known good values, no network failures
- ✅ **Focus on visualization** - Solve coordinate transforms and rendering first
- ✅ **Proven approach** - Matches how solar system implementation evolved
- ⚠️ **Con: Manual updates** - Must manually update if catalog values improve
- ⚠️ **Con: Limited scope** - Only a few hand-picked systems initially

**Tasks:**

1. Create `exoplanet_systems.py` (NEW - hardcoded catalog)
   - Define TRAPPIST-1 system with all 7 planets
   - Define TOI-1338 binary system with 2 planets
   - Include orbital elements, physical properties, discovery metadata
   - Use same structure as will be returned by API later

2. Create `exoplanet_orbits.py` (NEW - Keplerian calculations)
   - Implement `calculate_keplerian_orbit()` for exoplanets
   - Implement `plot_exoplanet_orbits()` - analogous to `plot_idealized_orbits()`
   - Handle coordinate transformations (orbital plane → 3D space)
   - Support binary star barycentric orbits

3. Create `exoplanet_coordinates.py` (NEW - stellar positioning)
   - Implement `radec_to_cartesian()` - convert (RA, Dec, distance) → (X, Y, Z)
   - Implement `apply_proper_motion()` - correct stellar position for date
   - Implement `calculate_binary_barycenter()` - for binary systems
   - NO attempt to relate to Solar System ecliptic frame

4. Modify `palomas_orrery.py`
   - Add exoplanet objects to objects list (hardcoded from `exoplanet_systems.py`)
   - Add "Exoplanetary Systems" GUI section with system selection
   - Integrate `plot_exoplanet_orbits()` call alongside `plot_idealized_orbits()`
   - Add exoplanet branch to position fetching

5. Update `constants_new.py`
   - Add `color_map()` entries for exoplanets and host stars
   - Add `EXOPLANET_INFO` dictionary (similar to `INFO`)

6. Extend `palomas_orrery_helpers.py`
   - Add `id_type='exoplanet'` branch to `fetch_trajectory()`
   - Add `id_type='host_star'` branch for stellar positions

**Test Cases:**
- System 1: TRAPPIST-1 (7 planets, single M-dwarf star, <0.07 AU)
- System 2: TOI-1338 (2 planets, binary G+M stars, circumbinary at 0.46 AU)

**Deliverable:** Working visualization of both systems with proper framing and animation

### Phase 2: Live Data Integration
**Goal:** Add NASA Exoplanet Archive API fetching to expand system catalog

**Tasks:**
1. Create `exoplanet_data_acquisition.py`
   - Implement NASA Exoplanet Archive TAP queries
   - Parse Planetary Systems Composite table
   - Transform API response to match hardcoded structure
   - Cache fetched systems with timestamp

2. Add system discovery features
   - Filter by distance, discovery method, year
   - Search for systems by name
   - "Recently discovered" category
   - "Most planets" sorting

3. Update GUI with dynamic loading
   - System dropdown populated from cache + hardcoded favorites
   - Refresh button to fetch latest catalog
   - Status indicator showing cache age

4. Add 8-10 more systems (mix of API + hardcoded)
   - Proxima Centauri (nearest, proper motion test)
   - 51 Pegasi (historical first)
   - Kepler-452 ("Earth's cousin")
   - HD 209458 (first transit)
   - Kepler-90 (8 planets - most in one system)
   - LHS 1140 (habitable zone super-Earth)

**Deliverable:** 10+ exoplanet systems with hybrid data sourcing

### Phase 3: Enhanced Features
**Goal:** Advanced exoplanet visualization capabilities

**Tasks:**
1. Habitable zone visualization
   - Calculate and display habitable zone boundaries
   - Color-code planets by habitability metrics

2. Comparative planetology
   - Size/mass comparison with Solar System
   - Overlay Solar System for scale reference

3. Time-travel animation
   - Show planetary transits from Earth's perspective
   - Animate orbital resonances

4. Discovery timeline
   - Filter systems by discovery year
   - Show how field has evolved

**Deliverable:** Full-featured exoplanet visualization suite

### Phase 4: Integration with Stellar Visualization
**Goal:** Unified stellar + exoplanet view

**Tasks:**
1. Link `star_visualization_gui.py` with exoplanet data
2. Click star → see exoplanets (if any)
3. 3D view showing Earth, nearby stars, and their planets
4. Distance-based filtering (e.g., "all exoplanets within 100 ly")

**Deliverable:** Integrated stellar-exoplanet catalog

---

## 8. Technical Considerations

### 8.1 Proper Motion Correction

**Critical for nearby stars** (like Proxima Centauri with 3.85 arcsec/year proper motion)

```python
def apply_proper_motion(ra0, dec0, pmra, pmdec, epoch0, target_date):
    """
    Apply proper motion to stellar position
    
    Parameters:
        ra0, dec0: Initial position (degrees) at epoch0
        pmra, pmdec: Proper motion (mas/year)
        epoch0: Reference epoch (datetime)
        target_date: Target date (datetime)
    
    Returns:
        ra, dec: Corrected position at target_date
    """
    # Calculate elapsed time in years
    years_elapsed = (target_date - epoch0).total_seconds() / (365.25 * 86400)
    
    # Apply proper motion (convert mas/year to degrees)
    # Note: pmra is already corrected for cos(dec) in catalogs
    delta_ra = (pmra / 3600000) * years_elapsed
    delta_dec = (pmdec / 3600000) * years_elapsed
    
    ra = ra0 + delta_ra
    dec = dec0 + delta_dec
    
    return ra, dec
```

**When to use:**
- ✅ Always for animation across years
- ✅ For stars within 100 pc (proper motion likely significant)
- ✅ When user sets date far from discovery epoch
- ⚠️ Optional for distant stars (>1000 pc) with small proper motion

### 8.2 Time System Consistency

**Decision:** Use consistent time scale throughout

**Approach:**
```python
from astropy.time import Time

def ensure_time_consistency(user_date):
    """
    Convert user input to standard time scale
    
    User provides: UTC datetime
    Internal calculations: Use UTC consistently
    Display: UTC
    
    No need for TDB since:
    - Not mixing with JPL Horizons (different systems)
    - Exoplanet orbital elements are epoch-independent
    - Proper motion uses years, not precise timescales
    """
    # Just ensure datetime is timezone-aware UTC
    if user_date.tzinfo is None:
        user_date = user_date.replace(tzinfo=timezone.utc)
    return user_date
```

**Rationale:**
- Exoplanet systems are **independent** from Solar System
- Not mixing Horizons ephemerides with exoplanet calculations
- Proper motion precision (mas/year) doesn't require TDB
- Simplify: UTC throughout for exoplanet code

### 8.3 Missing Data Defaults and Documentation

**Challenge:** Exoplanet orbits (< 10 AU) are much smaller than outer Solar System (> 30 AU)

**Solutions:**
1. **Separate scale mode** - Zoom to exoplanet system when selected
2. **Picture-in-picture** - Show exoplanet system in corner while viewing Solar System
3. **Scale indicator** - Always show scale bar in AU

### 8.3 Data Refresh Strategy

**NASA Exoplanet Archive updates frequently** (~monthly)

**Strategy:**
1. Cache exoplanet data with timestamp
2. Check for updates on startup (once per day)
3. Prompt user to refresh if cache > 30 days old
4. Store in `exoplanet_cache.json` similar to orbit cache

### 8.4 Performance Optimization

**Concern:** Calculating positions for hundreds of exoplanets

**Optimizations:**
1. **Lazy loading** - Only calculate positions for visible/selected planets
2. **Caching** - Store calculated trajectories like orbit_paths.json
3. **LOD (Level of Detail)** - Fewer points for distant/small planets
4. **Parallel processing** - Calculate multiple systems simultaneously

---

## 9. User Experience Enhancements

### 9.1 Discovery Annotations

Add tooltips showing:
- Discovery date and method
- Discovery team/telescope
- Significance (first of its kind, records, etc.)

### 9.2 Comparison Mode

Allow users to:
- Overlay Solar System planets for size comparison
- Show Earth's habitable zone over exoplanet systems
- Compare multiple exoplanet systems side-by-side

### 9.3 Educational Features

**Add to `star_notes.py` equivalent: `exoplanet_notes.py`**
- Explanations of discovery methods
- Habitability factors
- Links to papers and press releases

---

## 10. Future Extensions

### 10.1 Direct Imaging Visualization
- Show actual exoplanet images where available
- Overlay coronagraph masks
- Simulate what JWST/future telescopes will see

### 10.2 Atmospheric Characterization
- Display detected molecules (H₂O, CH₄, O₃)
- Show transmission spectra
- Color-code by atmospheric composition

### 10.3 Mission Planning
- Show observation windows for telescopes
- Calculate transit times
- Predict future transits

### 10.4 Citizen Science Integration
- Link to Planet Hunters
- Show user-discovered planets
- Display candidates awaiting confirmation

---

## 11. Technical Dependencies

### 11.1 New Dependencies
```python
# Add to requirements.txt
astroquery>=0.4.7  # For NASA Exoplanet Archive TAP
```

### 11.2 Data APIs
- **NASA Exoplanet Archive TAP:** https://exoplanetarchive.ipac.caltech.edu/TAP/
- **SIMBAD (already integrated):** http://simbad.u-strasbg.fr/simbad/
- **Gaia (already integrated):** https://gea.esac.esa.int/archive/

---

## 12. Testing Strategy

### 12.1 Unit Tests
- Test Keplerian orbit calculations
- Verify coordinate transformations
- Validate data parsing from NASA Archive

### 12.2 Integration Tests
- Test with all Phase 1 exoplanet systems
- Verify plots render correctly
- Check animation frame rates

### 12.3 Validation
- Compare calculated positions with published papers
- Cross-check with other exoplanet visualization tools
- Verify orbital periods match observations

---

## 13. Documentation Requirements

### 13.1 User Documentation
- Update `README.md` with exoplanet section
- Create tutorial: "Visualizing Exoplanet Systems"
- Add to website: screenshots and videos

### 13.2 Developer Documentation
- Document exoplanet data structures
- Explain coordinate transformation math
- Provide examples for adding new systems

### 13.3 Citations
- Cite NASA Exoplanet Archive in all outputs
- Credit discovery teams in tooltips
- Link to original discovery papers

---

## 14. Proof of Concept: TRAPPIST-1

### 14.1 System Parameters

**Host Star:** TRAPPIST-1 (2MASS J23062928-0502285)
- Spectral Type: M8V (ultracool red dwarf)
- Distance: 12.43 ± 0.03 pc
- RA: 23h 06m 29.283s
- Dec: -05° 02′ 28.5″

**Planets:** (innermost to outermost)
| Planet | Period (days) | a (AU) | e | i (deg) | Mass (M⊕) | Radius (R⊕) |
|--------|---------------|--------|---|---------|-----------|-------------|
| b | 1.51087 | 0.01154 | 0.00622 | 89.728 | 1.374 | 1.116 |
| c | 2.42182 | 0.01580 | 0.00654 | 89.778 | 1.308 | 1.097 |
| d | 4.04961 | 0.02227 | 0.00837 | 89.896 | 0.388 | 0.788 |
| e | 6.09965 | 0.02925 | 0.00510 | 89.793 | 0.692 | 0.920 |
| f | 9.20669 | 0.03849 | 0.01007 | 89.740 | 1.039 | 1.045 |
| g | 12.35294 | 0.04683 | 0.00208 | 89.721 | 1.321 | 1.129 |
| h | 18.76712 | 0.06189 | 0.00567 | 89.796 | 0.326 | 0.755 |

**Habitable Zone:** ~0.025-0.050 AU (e, f, g potentially habitable)

### 14.2 Visualization Goals

1. Show all 7 planets in synchronized orbits
2. Highlight habitable zone with translucent green torus
3. Animate over ~20 days to show orbital resonances
4. Scale comparison: overlay Earth orbit for perspective
5. Add note: "3 planets in habitable zone - water could exist"

### 14.3 Code Skeleton

```python
# In exoplanet_data_acquisition.py

TRAPPIST1_SYSTEM = {
    'host_star': {
        'name': 'TRAPPIST-1',
        'ra': 346.6220125,  # degrees
        'dec': -5.04125,     # degrees
        'distance_pc': 12.43,
        'spectral_type': 'M8V',
        'mass_solar': 0.0898,
        'radius_solar': 0.1192,
        'teff_k': 2566
    },
    'planets': [
        {
            'name': 'TRAPPIST-1 b',
            'period_days': 1.51087,
            'semi_major_axis_au': 0.01154,
            'eccentricity': 0.00622,
            'inclination_deg': 89.728,
            'mass_earth': 1.374,
            'radius_earth': 1.116,
            'equilibrium_temp_k': 400,
            'insolation_earth': 4.25
        },
        # ... (other 6 planets)
    ],
    'habitable_zone': {
        'inner_au': 0.025,
        'outer_au': 0.050
    }
}
```

---

## 15. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Data API changes | Medium | High | Cache data, monitor API |
| Performance issues with many planets | Medium | Medium | Implement LOD, caching |
| Coordinate transform errors | Low | High | Extensive testing, validation |
| User confusion (mixing solar + exo) | Medium | Low | Clear UI sections, tutorials |
| Incomplete exoplanet data | High | Medium | Handle missing values gracefully |

---

## 16. Success Metrics

**Phase 1 Success:**
- ✅ TRAPPIST-1 system renders correctly
- ✅ All 7 planets visible and labeled
- ✅ Animation runs smoothly (>20 fps)
- ✅ Orbital periods match observations (±1%)

**Long-term Success:**
- 10+ exoplanet systems visualized
- User feedback: "easy to understand"
- Educational adoption by teachers/planetariums
- Citation in academic papers

---

## 17. Questions for Review

1. **GUI location:** Integrated into main GUI or separate window?
   - **Recommendation:** Integrated (Option A)

2. **Coordinate system:** Observer perspective or 3D ecliptic?
   - **Recommendation:** Support both, default to observer perspective

3. **Data source priority:** NASA Archive only or multi-source?
   - **Recommendation:** NASA Archive primary, SIMBAD for stellar data

4. **Performance target:** Max number of simultaneous systems?
   - **Recommendation:** 5 systems, 50 planets total

5. **Update frequency:** Check for new exoplanets how often?
   - **Recommendation:** Monthly, user-configurable

---

## 18. Next Steps

### Immediate Actions (This Week)
1. ✅ Review this framework document
2. ⬜ Decide on GUI approach (integrated vs. separate)
3. ⬜ Create `exoplanet_data_acquisition.py` stub
4. ⬜ Fetch TRAPPIST-1 data from NASA Archive
5. ⬜ Test coordinate transformation with one planet

### Sprint 1 (Next 2 Weeks)
1. ⬜ Implement full TRAPPIST-1 system
2. ⬜ Add to objects list in palomas_orrery.py
3. ⬜ Create basic GUI controls
4. ⬜ Generate first exoplanet visualization
5. ⬜ Write unit tests for orbital calculations

### Sprint 2 (Weeks 3-4)
1. ⬜ Add 4 more exoplanet systems
2. ⬜ Implement system selection dropdown
3. ⬜ Add habitable zone visualization
4. ⬜ Create comparison with Solar System feature
5. ⬜ Update documentation

---

## 19. References

### Academic
- NASA Exoplanet Archive: https://exoplanetarchive.ipac.caltech.edu/
- Gillon et al. 2017 (TRAPPIST-1 discovery): Nature 542, 456-460
- Murray & Dermott (1999): Solar System Dynamics (orbital mechanics)

### Technical
- Astroquery Documentation: https://astroquery.readthedocs.io/
- Plotly 3D Scatter Plots: https://plotly.com/python/3d-scatter-plots/
- JPL Horizons Manual: https://ssd.jpl.nasa.gov/horizons/manual.html

### Educational
- NASA Exoplanet Exploration: https://exoplanets.nasa.gov/
- Eyes on Exoplanets: https://eyes.nasa.gov/apps/exo/
- Planet Hunters: https://www.zooniverse.org/projects/nora-dot-eisner/planet-hunters-tess

---

## Appendix A: Code Structure

```
palomas_orrery/
├── palomas_orrery.py              # Main GUI (add exoplanet section)
│
├── exoplanet_systems.py           # NEW: Hardcoded system catalog (Phase 1)
│   └── TRAPPIST1_SYSTEM           # 7 planets, single M-dwarf
│   └── TOI1338_SYSTEM             # 2 planets, binary G+M stars
│   └── PROXIMA_SYSTEM             # (Phase 1.5)
│
├── exoplanet_orbits.py            # NEW: Keplerian orbit calculations
│   └── plot_exoplanet_orbits()   # Main plotting function
│   └── calculate_keplerian_orbit() # Position calculation
│   └── create_binary_system_objects() # Binary star handling
│
├── exoplanet_coordinates.py       # NEW: Stellar positioning (NOT ecliptic)
│   └── create_local_frame()       # Local sky-plane coordinate system
│   └── apply_proper_motion()      # Stellar motion correction
│   └── calculate_binary_barycenter() # Binary system center
│
├── exoplanet_data_acquisition.py  # NEW: NASA Archive API (Phase 2)
│   └── fetch_exoplanet_systems()  # TAP queries
│   └── parse_exoplanet_data()     # Transform to standard format
│
├── exoplanet_visualization.py     # NEW: Advanced features (Phase 3)
│   └── plot_habitable_zone()      # HZ torus visualization
│   └── create_comparison_view()   # vs. Solar System
│
├── exoplanet_notes.py             # NEW: Educational content
│   └── DISCOVERY_METHODS          # Transit, RV, etc.
│   └── SYSTEM_STORIES             # Wolf Cukier, etc.
│
├── idealized_orbits.py            # Reference for rotation math
├── palomas_orrery_helpers.py      # Extend fetch_trajectory()
├── constants_new.py               # Add exoplanet colors/info
├── exoplanet_cache.json           # NEW: Cached API data (Phase 2)
└── README.md                      # Update with exoplanet section
```

**Module Dependencies:**
```
exoplanet_systems.py (no dependencies, pure data)
     ↓
exoplanet_orbits.py (uses numpy, copies rotation from idealized_orbits.py)
     ↓
exoplanet_coordinates.py (uses astropy for RA/Dec transforms)
     ↓
palomas_orrery.py (imports all above, integrates into GUI)
```

**Phase 2 adds:**
```
exoplanet_data_acquisition.py → exoplanet_cache.json → exoplanet_systems.py
```

---

## Appendix B: Example Queries

### NASA Exoplanet Archive TAP Query
```sql
SELECT 
    pl_name, hostname, 
    ra, dec, sy_dist,
    pl_orbper, pl_orbsmax, pl_orbeccen, pl_orbincl,
    pl_bmassj, pl_radj,
    disc_year, discoverymethod
FROM 
    ps  -- Planetary Systems Composite Parameters table
WHERE 
    sy_dist < 100  -- Within 100 parsecs
    AND pl_orbper IS NOT NULL  -- Must have orbital period
    AND default_flag = 1  -- Use default parameters
ORDER BY 
    sy_dist ASC
```

### SIMBAD Star Query (via astroquery)
```python
from astroquery.simbad import Simbad

custom_simbad = Simbad()
custom_simbad.add_votable_fields('sptype', 'flux(V)', 'plx', 'ids')

result = custom_simbad.query_object('TRAPPIST-1')
```

---

**Document Version:** 1.0  
**Last Updated:** October 21, 2025  
**Author:** AI Assistant (Claude) with Tony Quintanilla  
**Status:** Draft for Review
