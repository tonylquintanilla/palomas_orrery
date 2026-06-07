# Handoff: Lucy L4 Trojan Targets Implementation

**Date:** January 27, 2026  
**Previous Session:** Patroclus-Menoetius binary orbit implementation  
**Next Task:** Implement all remaining Lucy Trojan targets (Eurybates-Queta, Polymele-Shaun, Orus, Leucus)

---

## Context

We successfully implemented the Patroclus-Menoetius binary Trojan system with:
- Barycenter-centered visualization
- Analytical orbits from Brozović et al. 2024 parameters
- Phase alignment using Horizons reference vectors
- Sub-day temporal resolution for Lucy flyby (March 3, 2033)

Now we want to complete the full set of Lucy Trojan targets using the same patterns.

---

## Lucy Mission Trojan Targets - Complete List

### L4 Trojans (Leading) - TO BE IMPLEMENTED
| Target | Type | Flyby Date | Priority |
|--------|------|------------|----------|
| **Eurybates + Queta** | Binary | Aug 12, 2027 | HIGH - binary |
| **Polymele + Shaun** | Binary | Sep 15, 2027 | HIGH - binary |
| **Leucus** | Single | Apr 18, 2028 | Medium |
| **Orus** | Single | Nov 11, 2028 | Medium |

### L5 Trojans (Trailing) - DONE
| Target | Type | Flyby Date | Status |
|--------|------|------------|--------|
| **Patroclus-Menoetius** | Binary | Mar 3, 2033 | ✅ IMPLEMENTED |

---

## Implementation Plan

### Phase 1: Binary Systems (Barycenter Mode)

#### 1. Eurybates-Queta

**Known Parameters (need to verify with papers):**
| Parameter | Value | Source |
|-----------|-------|--------|
| Eurybates diameter | ~64 km | Lucy mission |
| Queta diameter | ~1.2 km | HST 2020 discovery |
| Separation | ~2,350 km | Noll et al. 2020 |
| Orbital period | ~82 days | Estimated |
| Mass ratio | Very small (~0.001?) | Queta is tiny |

**Horizons IDs to look up:**
- Eurybates: `3548` or search "Eurybates"
- Queta: Likely `3548 I` or similar satellite designation
- Barycenter: May need special ID like Patroclus

**Note:** Because Queta is so small (~1 km vs 64 km), this is NOT a true binary like Patroclus-Menoetius. The barycenter will be well inside Eurybates. But barycenter mode still shows the orbital mechanics correctly.

#### 2. Polymele-Shaun

**Known Parameters:**
| Parameter | Value | Source |
|-----------|-------|--------|
| Polymele diameter | ~21 km | Lucy mission |
| Shaun diameter | ~5 km | Discovered via occultation 2022! |
| Separation | ~200 km | Occultation data |
| Orbital period | Unknown | Need to research |

**Note:** Shaun was discovered by stellar occultation in March 2022 - a surprise satellite! May not be in Horizons yet.

**Horizons IDs to look up:**
- Polymele: `15094`
- Shaun: May not exist in Horizons (like MK2 situation)

### Phase 2: Single Trojans (Simple Implementation)

#### 3. Leucus

| Parameter | Value |
|-----------|-------|
| Diameter | ~40 km |
| Type | D-type asteroid |
| Rotation | Very slow (~446 hours!) |
| Horizons ID | `11351` |

**Implementation:** Standard heliocentric orbit, no special barycenter handling needed.

#### 4. Orus  

| Parameter | Value |
|-----------|-------|
| Diameter | ~51 km |
| Type | D-type asteroid |
| Horizons ID | `21900` |

**Implementation:** Standard heliocentric orbit, no special barycenter handling needed.

---

## Key Lessons from Patroclus-Menoetius

### What Worked
1. **Hybrid data approach:** Physical params from papers + orbital plane from Horizons
2. **Phase reference method:** Use Horizons XYZ vectors at known epoch to establish orbital phase
3. **Nearly circular orbit handling:** For e < 0.01, periapsis is undefined - show "Keplerian Position" instead

### Horizons Quirks
- Osculating elements for barycenter-centered queries return NaN for a, e, ω, Tp
- But inclination (i) and node (Ω) ARE returned correctly
- Vector queries (XYZ positions) work perfectly

### Code Pattern for Binary Systems
```python
BINARY_PARAMS = {
    'separation_km': 692.5,
    'period_days': 4.283,
    'mass_fraction_primary': 0.7798,
    'mass_fraction_secondary': 0.2202,
    'eccentricity': 0.004,
    'inclination_ecliptic': 152.53,    # From Horizons
    'Omega_ecliptic': 324.12,          # From Horizons
}

PHASE_REFERENCE = {
    'jd_epoch': 2463659.5,
    'primary_x_km': 104.24,
    'primary_y_km': -109.12,
    'primary_z_km': 14.35,
}
```

---

## Implementation Steps for Each Binary

### Step 1: Research & Data Gathering
1. Find published orbital parameters (separation, period, mass ratio)
2. Look up Horizons IDs for primary, secondary, and barycenter
3. Query Horizons for orbital plane (i, Ω) - may return NaN for other elements
4. Query Horizons for XYZ vectors at reference epoch

### Step 2: orbital_elements.py
```python
# Add entries like:
'Eurybates': {
    'a': ..., 'e': ..., 'i': ...,  # Heliocentric elements
    'center_body': 'Eurybates-Queta Barycenter',
    'horizons_id': '...',
    'center_horizons_id': '...',  # Barycenter ID
    ...
}
```

### Step 3: idealized_orbits.py
```python
EURYBATES_BARYCENTER_ORBITERS = ['Eurybates', 'Queta']

def plot_eurybates_barycenter_orbit(fig, object_name, date, color, ...):
    # Same pattern as plot_patroclus_barycenter_orbit()
    ...
```

### Step 4: Handler in plot_idealized_orbits()
```python
elif center_id == 'Eurybates-Queta Barycenter':
    if object_name in EURYBATES_BARYCENTER_ORBITERS:
        return plot_eurybates_barycenter_orbit(...)
```

### Step 5: Test & Validate
- Verify analytical orbits match Horizons positions
- Test flyby visualization at appropriate date
- Check sub-day resolution works

---

## Files to Modify

| File | Changes |
|------|---------|
| `orbital_elements.py` | Add Eurybates, Queta, Polymele, Shaun, Leucus, Orus entries |
| `idealized_orbits.py` | Add binary orbit functions for Eurybates-Queta, Polymele-Shaun |
| `ORBITAL_MECHANICS_README.md` | Document all Lucy targets |

---

## Potential Challenges

### 1. Shaun (Polymele's moon)
- Discovered 2022 via stellar occultation
- May NOT be in Horizons yet (like MK2)
- May need pure analytical orbit from published elements

### 2. Queta
- Very small (~1 km) so mass ratio is extreme
- Barycenter is essentially at Eurybates center
- Still worth implementing for completeness

### 3. Orbital Parameters
- Less well-characterized than Patroclus-Menoetius
- May need to search recent papers (2022-2025)
- Lucy team has been refining parameters pre-encounter

---

## Lucy Flybys Timeline (Complete)

```
2021-10-16  Launch
2022-10-16  Earth gravity assist #1
2025-04-20  Earth gravity assist #2
2027-08-12  EURYBATES + QUETA (L4 binary) ← TO IMPLEMENT
2027-09-15  POLYMELE + SHAUN (L4 binary)  ← TO IMPLEMENT  
2028-04-18  LEUCUS (L4 single)            ← TO IMPLEMENT
2028-11-11  ORUS (L4 single)              ← TO IMPLEMENT
2031-04-26  Earth gravity assist #3
2033-03-03  PATROCLUS-MENOETIUS (L5 binary) ✅ DONE
```

---

## Research Links

- NASA Lucy Mission: https://lucy.swri.edu/
- Lucy target list: https://lucy.swri.edu/mission/targets.html
- Noll et al. 2020 (Queta discovery): Search ADS/arXiv
- Polymele occultation (Shaun discovery): Lucy team 2022 announcement

---

## Summary: Priority Order

1. **Eurybates-Queta** - First Lucy encounter, binary, likely in Horizons
2. **Polymele-Shaun** - Binary, Shaun may need analytical fallback
3. **Leucus** - Simple single asteroid
4. **Orus** - Simple single asteroid

---

**End of Handoff**
