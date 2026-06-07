# Phase C4 Testing Protocol

**Tester:** Tony Quintanilla
**Date:** May 18, 2026
**Files to deploy:** 6 files from this session's output

---

## 0. Deploy and Smoke

1. Copy all 6 files into your sandbox (not clean repo yet).
2. Launch `palomas_orrery_dashboard.py`.
3. Confirm the GUI opens without errors in the console.
4. Confirm Saturn / Uranus / Neptune checkboxes still appear
   in the shell panel (labels unchanged).

**If the GUI fails to launch, stop here and report the error.**

---

## 1. Saturn (most similar to Jupiter -- establishes pattern)

### 1.1 Sphere shells (heliocentric, centered on Saturn)

- [ ] Core visible, gold-white color
- [ ] Metallic hydrogen layer surrounds core
- [ ] Molecular hydrogen layer surrounds metallic
- [ ] Cloud layer solid mesh3d (opaque surface)
- [ ] Upper atmosphere translucent shell outside cloud
- [ ] Hill sphere visible at manual scale >= 0.6 AU

### 1.2 Ring system

- [ ] All 7 ring components render (D, C, B, A, F, G, E)
- [ ] Rings lie in Saturn's equatorial plane (tilted ~27 deg from ecliptic)
- [ ] Each ring has its own info marker (cross symbol, hover shows ring-specific text)
- [ ] **CRITICAL: Ring tooltip text references Saturn** (not Jupiter/Metis/Adrastea).
      Hover over ring info markers and read the text. This was a copy-paste
      bug from Jupiter -- confirm it's fixed.
- [ ] Rings toggle on/off via GUI checkbox

### 1.3 Magnetosphere

- [ ] Renders as blue-purple particle cloud
- [ ] **Heliocentric view: tail points AWAY from Sun** (sunward rotation working)
- [ ] **Flyto Saturn: tail still away from Sun direction**
- [ ] Info marker (cross) present with hover text
- [ ] No bow shock (expected -- same as Jupiter, deferred item 16)

### 1.4 Enceladus plasma torus

- [ ] Donut shape centered on Saturn
- [ ] NOT rotated (equatorial, gravity-anchored)
- [ ] Info marker with hover text

### 1.5 Radiation belts

- [ ] 6 belt components render (A-Ring to Mimas, Mimas to Enceladus, etc.)
- [ ] Each belt has its own info marker
- [ ] Belts NOT rotated by sunward rotation (axis-anchored)
- [ ] **Watch for position change**: the double-offset bug fix may have
      moved belts to a different (physically correct) position vs prior
      renders. Note if they look different.

### 1.6 Sun direction indicator

- [ ] ONE indicator per render (not 6 per-shell indicators like before)
- [ ] Indicator appears when any shell with `has_sun_indicator` is on

### 1.7 Animation

- [ ] Heliocentric animation: shells not displayed (expected behavior)
- [ ] Saturn-centered animation: static shells, moons orbit

### 1.8 GUI tooltips

- [ ] All 10 Saturn checkboxes have tooltips (hover over checkbox label)

---

## 2. Uranus

### 2.1 Sphere shells (heliocentric, centered on Uranus)

- [ ] Core (gold), mantle (orange), cloud layer (light blue mesh3d)
- [ ] Upper atmosphere, hill sphere at manual scale >= 0.6 AU

### 2.2 Magnetosphere -- THE BIG ONE

- [ ] Renders as light blue particle cloud
- [ ] **Heliocentric: tail away from Sun** (sunward rotation)
- [ ] **Flyto Uranus: tail still away from Sun**
- [ ] **Visible asymmetry from magnetic_tilt_deg=60**: the magnetosphere
      shape should look tilted/asymmetric compared to Saturn's.
      This is the first real use of the magnetic tilt parameter.
- [ ] **INFO MARKER PRESENT** (this is NEW -- Uranus source had no info
      marker before C4). Cross symbol with hover text mentioning
      "60 degrees" and "Ness et al."
- [ ] If the tilt direction looks wrong (dipole tilted the wrong way),
      note it -- we can flip the sign with a one-character change.

### 2.3 Radiation belts

- [ ] 2 belt components (Inner, Outer)
- [ ] Each has info marker
- [ ] NOT rotated by sunward rotation
- [ ] **Position may have changed** from dead-code cleanup (same as
      Saturn 1.5 note). The pre-C4 code applied center offset twice;
      now it's applied once after tilt. Belts should be in the
      physically correct position.

### 2.4 Ring system

- [ ] 11 rings render (6, 5, 4, Alpha, Beta, Eta, Gamma, Delta, Epsilon, Nu, Mu)
- [ ] Rings in Uranus's equatorial plane (~98 deg tilt -- nearly vertical)
- [ ] Each ring has info marker
- [ ] Gossamer ring (Nu/Mu) barely visible (pre-existing, deferred item 22)

### 2.5 Sun direction indicator

- [ ] ONE indicator per render

### 2.6 Animation + GUI

- [ ] Same animation behavior as Saturn
- [ ] All 8 Uranus checkboxes have tooltips

---

## 3. Neptune (most complex)

### 3.1 Sphere shells

- [ ] Core (gold), mantle (orange), cloud layer (blue mesh3d)
- [ ] Upper atmosphere, hill sphere at manual scale >= 1.0 AU

### 3.2 Magnetosphere

- [ ] Renders as blue particle cloud
- [ ] **Heliocentric: tail away from Sun** (sunward rotation)
- [ ] **Flyto Neptune: tail still away from Sun**
- [ ] Info marker present with hover text
- [ ] **Magnetic poles visible** (4 traces: center marker, axis line,
      north pole, south pole) -- these are from
      `create_neptune_magnetic_poles` which was NOT modified in C4
- [ ] **EXPECTED ISSUE: In heliocentric view, magnetic poles may drift
      off the rotated envelope.** The envelope rotates to face the Sun
      but the pole traces don't (bounded scope for C4). This is
      documented as Phase D item 6. Note the severity -- is it
      acceptable for now?

### 3.3 Radiation belts

- [ ] Multiple belt regions render (inner, outer, cusp)
- [ ] Field-aligned currents (FAC) render (dawn, dusk)
- [ ] Each has info marker
- [ ] **Info markers should sit ON the belt geometry** (not floating
      off-axis like before the bug fix)
- [ ] NOT rotated by sunward rotation

### 3.4 Ring system

- [ ] Main rings render (Galle, Le Verrier, Lassell, Arago, Adams)
- [ ] **Adams ring arcs visible** (Courage, Liberte, Egalite, Fraternite)
- [ ] Rings in Neptune's equatorial plane (~28 deg tilt)
- [ ] Each ring/arc has info marker

### 3.5 Sun direction indicator

- [ ] ONE indicator per render

### 3.6 Animation + GUI

- [ ] Same animation behavior as Saturn/Uranus
- [ ] All 8 Neptune checkboxes have tooltips

---

## 4. Regression checks

### 4.1 Prior bodies (quick spot-check)

- [ ] Jupiter: magnetosphere still rotates, rings/belts/torus unrotated
- [ ] Earth: magnetosphere still rotates
- [ ] Mercury: magnetosphere + bow shock still rotate
- [ ] Any one other body (Mars or Venus): quick visual sanity

### 4.2 Ring helper regression

- [ ] Saturn rings same shape as before C4
- [ ] Uranus rings same shape as before C4
- [ ] Neptune rings same shape as before C4

(The ring helper was promoted in C3 and is unchanged in C4.
This is a quick "nothing broke" check.)

---

## 5. Decision points during testing

These require your judgment call:

**5a. Uranus magnetic tilt direction (Section 2.2)**
If the dipole looks tilted the wrong way relative to Voyager-2-era
diagrams, we flip the sign: `magnetic_tilt_deg=60` becomes
`magnetic_tilt_deg=-60`. One-character change.

**5b. Belt position changes (Sections 1.5, 2.3)**
The double-offset fix moved Saturn and Uranus belts to physically
correct positions. If the visual change is jarring, note it --
but the physics is now correct.

**5c. Neptune pole drift (Section 3.2)**
How bad is the magnetic pole misalignment in heliocentric view?
If it's subtle, accept for C4. If it's distracting, we can
fast-track the Phase D fix for the pole helper.

---

## 6. After testing

If all checks pass:
1. Copy files from sandbox to clean repo
2. Run `provenance_scanner.py` (expect 0 Tier-1 on touched files)
3. Deploy to GitHub
4. Report results for handoff document

If issues found:
- Note which check failed and what you see
- Screenshot if visual
- We fix in this session or next

---

*"Visual verification catches physics errors code review misses."*
