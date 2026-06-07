# Phase C2 Visual Verification Test Protocol

**For:** Tony Quintanilla
**Date:** May 16, 2026
**Files to deploy:** `shell_configs.py`, `earth_visualization_shells.py`, `planet_visualization.py`
**Backup first:** Copy the three files you're replacing. Revert if any test fails critically.

---

## Pre-test: Confirm deployment

1. Copy all three files into your working directory
2. Launch the orrery dashboard
3. Confirm it opens without errors

---

## Test 1: Earth sphere shells (heliocentric)

**Setup:** Default heliocentric view. Center: Sun. Select Earth.

| Step | Toggle on | Look for | Pass? |
|------|-----------|----------|-------|
| 1a | Inner Core only | Small orange-red sphere at 0.19 R_E. One cross (+) info marker at north pole. Hover shows inner core text. | |
| 1b | + Outer Core | Orange sphere wrapping inner core at 0.55 R_E. Own info marker. | |
| 1c | + Lower Mantle | Dark orange at 0.85 R_E. | |
| 1d | + Upper Mantle | Reddish at 0.98 R_E, just below crust. | |
| 1e | + Crust | Solid blue mesh3d sphere at 1.0 R_E. NOT dot grid -- solid surface. Color: ocean blue. | |
| 1f | + Atmosphere | Thin pale blue layer just outside crust (1.05 R_E). Legend says "Earth: Lower Atmosphere". | |
| 1g | + Upper Atmosphere | Slightly thicker blue layer (1.25 R_E). | |
| 1h | + Hill Sphere | Set manual scale >= 0.02 AU. Large green sparse sphere at 235 R_E. | |

**Key check:** Each shell has exactly ONE cross info marker. No duplicates. Hover text displays correctly on each.

---

## Test 2: Earth magnetosphere -- THE HEADLINE TEST

### 2a: Heliocentric view (regression -- should look the same as before)

**Setup:** Heliocentric view. Earth at its default position (~+X, ~1 AU from Sun).

| Toggle | Look for | Pass? |
|--------|----------|-------|
| Magnetosphere | Light blue dots (rgb(180,180,255)). Bow shock on Sun-facing side (-X). Magnetotail on +X side. Cross info marker with hover text. | |
| Bow Shock | Orange dots (rgb(255,200,150)). On Sun-facing side. Cross info marker. | |
| Inner Radiation Belt | Red toroidal ring at ~1.5 R_E around rotational axis. Cross info marker. | |
| Outer Radiation Belt | Blue toroidal ring at ~4.5 R_E. Cross info marker. | |

This view should look **identical** to pre-C2. Rotation is near-identity when Earth is at +X.

### 2b: Earth-centered flyto (the fix)

**Setup:** Switch center body to Earth. Flyto Earth.

| Check | Look for | Pass? |
|-------|----------|-------|
| Bow shock orientation | Bow shock should face TOWARD where the Sun is in this view. Before C2 it pointed along -X regardless. | |
| Magnetotail | Should extend AWAY from the Sun. | |
| Van Allen belts | Should wrap around Earth's rotational axis (+Z). NOT rotated with the bow shock. They stay put. | |

**This is the key behavioral change.** If the bow shock faces the Sun and the belts stay on the Z axis, C2 is working.

### 2c: Indicator check

| Check | Look for | Pass? |
|-------|----------|-------|
| Sun direction indicator count | ONE indicator total, regardless of which shells are toggled on. | |
| Toggle magnetosphere only | Still one indicator. | |
| Toggle all shells + magnetosphere + LEO + GEO | Still one indicator. | |

If you see two indicators, the per-shell call wasn't fully removed. Flag it.

---

## Test 3: LEO and GEO

**Setup:** Earth-centered. Set manual scale to 0.003 AU.

| Shell | Look for | Pass? |
|-------|----------|-------|
| LEO | Spherical scatter of warm-white dots (300 points) between 1.03-1.31 R_E. Denser near Starlink altitude (~550 km). Cross info marker at north pole. Hover text mentions ISS, Starlink, debris counts. | |
| GEO | Ring of cool silver-white dots (240 points) in equatorial plane at 6.62 R_E. Cross info marker on +X side of ring. Hover text mentions Apophis 2029 flyby. | |
| Both together | LEO shell clearly inside GEO ring. Spatial relationship is obvious. | |

---

## Test 4: Regression -- other migrated bodies

Quick spot-check. Each should render the same as before C2.

| Body | Center it, toggle a few shells | Pass? |
|------|-------------------------------|-------|
| Mercury | Shells + magnetosphere render | |
| Moon | Shells render | |
| Venus | Shells + magnetosphere render, bow shock faces Sun | |
| Mars | Shells + magnetosphere + crustal fields render. Crustal fields NOT rotated (southern hemisphere, purple dots) | |
| Pluto | Shells render, mesh3d crust | |
| Eris | Shells render | |
| Planet 9 | Shells render | |

---

## Test 5: Regression -- non-migrated bodies

These still use the old dispatch path. Verify they still work.

| Body | Shells render? | Pass? |
|------|---------------|-------|
| Jupiter | | |
| Saturn | | |
| Uranus | | |
| Neptune | | |

---

## Test 6: Animation regression

Per C1 handoff item 13:

| Test | Expected behavior | Pass? |
|------|-------------------|-------|
| Heliocentric animated plot with Earth shells on | Shells do NOT display (orbital trace animates, no shells at body position) | |
| Earth-centered animated plot | All shells render as static geometry at origin. Orbiting bodies animate around them. | |

---

## Test 7: GUI tooltip regression

Hover the mouse over each of these 11 Earth shell checkboxes in the GUI panel. Each should show a tooltip.

| Checkbox | Tooltip appears? |
|----------|-----------------|
| Inner Core | |
| Outer Core | |
| Lower Mantle | |
| Upper Mantle | |
| Crust | |
| Atmosphere | |
| Upper Atmosphere | |
| Magnetosphere | |
| Hill Sphere | |
| LEO | |
| Geostationary Belt | |

---

## Results summary

| Test | Result |
|------|--------|
| 1: Earth sphere shells | |
| 2a: Magnetosphere heliocentric (regression) | |
| 2b: Magnetosphere flyto (the fix) | |
| 2c: Indicator count | |
| 3: LEO + GEO | |
| 4: Other migrated bodies | |
| 5: Non-migrated bodies | |
| 6: Animation regression | |
| 7: GUI tooltips | |

**If all pass:** Phase C2 is verified. Write handoff.
**If any fail:** Note which test, what you see vs expected. We debug before proceeding.

---

*Paloma's Orrery | Phase C2 test protocol*
*Module updated: May 2026 with Anthropic's Claude Opus 4.6*
