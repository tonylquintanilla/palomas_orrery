# Phase D2 Testing Protocol

**Tester:** Tony Quintanilla
**Date:** May 21, 2026
**Scope:** sun_position threading, magnetic tilt activation,
Neptune diamond marker, double indicator removal

**Reviewed by:** Opus 4.7 (Mode 7). Line 6194 NameError caught
and reverted before testing. Animation wiring deferred to D3.

**Round 1 findings:** Sun checkbox dependency -- _sun_pos_tuple
fell back to (0,0,0) when Sun checkbox was off because positions
dict only contains toggled-on objects. Fix: independent Sun fetch
at lines 4500-4506. Round 2 retests sections 2-4 with Sun off.

---

## 0. Pre-flight

### 0.0 Compile check [CRITICAL] -- by Claude; passed

```
python3 -m py_compile palomas_orrery.py
python3 -m py_compile shared_utilities.py
python3 -m py_compile planet_visualization.py
python3 -m py_compile shell_configs.py
python3 -m py_compile earth_visualization_shells.py
python3 -m py_compile mercury_visualization_shells.py
python3 -m py_compile venus_visualization_shells.py
python3 -m py_compile mars_visualization_shells.py
python3 -m py_compile jupiter_visualization_shells.py
python3 -m py_compile saturn_visualization_shells.py
python3 -m py_compile neptune_visualization_shells.py
python3 -m py_compile uranus_visualization_shells.py
python3 -m py_compile orrery_rendering.py
```

All 13 must pass. Stop on any failure.

### 0.1 Import verification -- by Claude and Tony; passed

```
grep "from orrery_rendering import rotate_to_sunward" earth_visualization_shells.py
```

Must return a match. If not, snippet 3c was not applied.

### 0.2 Verify line 6194 revert -- by Claude; passed

```
grep -n "create_planet_visualization.*sun_position" palomas_orrery.py
```

Should show sun_position on static paths (~4543, ~4636, ~4649) but
**NOT** on the animation center-body path (~6193). If line ~6193
still has sun_position, the NameError is live.

### 0.3 Verify Sun fetch fix (lines 4500-4506) -- by Claude; passed

```
grep -n "fetch_position.*10.*center_id" palomas_orrery.py
```

Should return a line in the _sun_pos_tuple computation block. This
is the fix for the Sun-checkbox-off bug found in Round 1.

### 0.4 Deploy and smoke -- done

1. Copy all modified files into your sandbox (not clean repo yet).
2. Launch `palomas_orrery_dashboard.py`.
3. Confirm the GUI opens without errors in the console.

**If the GUI fails to launch, stop here and report the error.**

---

## 1. Regression gate (Sun-centered baseline)

D2 should not change Sun-centered behavior. sun_position defaults
to (0,0,0) everywhere in this view, preserving old behavior exactly.

### 1.1 Sun-centered static, all shells

- [ ] Center: Sun. Enable all planet shells. Generate static.
- [ ] Mercury shells: unchanged from pre-D2 -- sun-centered correct; mercury-center sun orientation is correct for all shell except the sodium tail, which is oriented away from -x
- [ ] Venus shells: unchanged from pre-D2 -- sun-centered correct; venus-centered correct
- [ ] Earth shells: unchanged from pre-D2 -- sun-centered correct; earth-centered correct but the automatic flyto the sun was set to 0.15 au, which is too small to include the outer corona; 
- [ ] Mars shells: unchanged from pre-D2 -- sun-centered correct and mars-centered correct except that the induced magnetosphere does not have a hovertext and marker
- [ ] Jupiter shells: unchanged from pre-D2 -- sun-centered correct and jupiter-centered correct except they do not have a bow shock shell or selection option in the gui
- [ ] Saturn shells: unchanged from pre-D2 -- sun-centered and saturn-centered are correct and do not have a bow shock shell
- [ ] Uranus shells: unchanged from pre-D2 -- sun-centered and uranus-centered are correct and magnetosphere hovertext is truncated likely missing carriage return and no bow shock shell
- [ ] Nepturn shells: unchanged from pre-D2 -- sun-centered magnetosphere hovertext is truncated, the radiation hovertext are not clearly labelled to connect them to the legend, the arc markers are superimposed and cannot be distinguished, the lassel and arago ring markers are superimposed, the field-aligned current hovertext are not clearly labelled to connect to the legend
- [ ] Pluto shells: unchanged from pre-D2 -- sun-centered, pluto-center and bary-center shells render correctly
- [ ] Eris shells: unchanged from pre-D2 -- sun-centered and eris-centered shells render correctly
- [ ] Any outer planet shells: unchanged from pre-D2
- [ ] Sun shells (sphere + custom): unchanged from D1 -- all shells render correctly

### 1.2 Sun-centered animation smoke

- [ ] Center: Sun. Enable Earth shells. Click Animate (5 frames). -- sun shells render when animated with planets but planet shells do not render.
- [ ] Runs without errors in console -- correct
- [ ] mercury shells render when mercury is the center and animated but not when sun-centered
- [ ] venus shells render when venus is the center and animated but when not when sun-centered 
- [ ] earth shells render when center is the center and animated but not when sun-centered or moon-centered and animated, and when moon-centered moon shells render
- [ ] Mars shells render when mercury is the center and animated but not when sun-centered and animated
- [ ] Jupiter shells render when mercury is the center and animated but not when sun-centered and animated
- [ ] Saturn shells render when mercury is the center and animated but not when sun-centered and animated
- [ ] Uranus shells render when mercury is the center and animated but not when sun-centered and animated
- [ ] neptune shells render when mercury is the center and animated but not when sun-centered and animated
- [ ] pluto shells render when pluto is the center and animated but not when sun-centered or barycentered and animated
- [ ] eris shells shells render when eris is the center and animated but not when sun-centered and animated

**If anything looks different from pre-D2 in a Sun-centered view, stop.**

---

## 2. Sun direction indicator (item 10)

### 2.1 Indicator with Sun checkbox OFF

- [ ] Center: Earth. Sun checkbox OFF. Enable any Earth shell. -- correct
      Generate static.
- [ ] ONE yellow dashed arrow pointing from origin toward Sun -- correct and when the moon shells are enabled the moon has a separate correly pointed indicator, but the two sun direction indicators toggle on and off together not separately
- [ ] Hover cross marker at arrow tip: shows
      "Distance to Sun: X.XXXX AU (XXX,XXX,XXX km)" -- correct

### 2.2 Indicator with Sun checkbox ON (regression)

- [ ] Center: Earth. Sun checkbox ON. Enable Earth + Sun shells. -- correct as noted above
      Generate static.
- [ ] ONE yellow dashed arrow on Earth (not two) -- correct
- [ ] Sun shells render at Sun's offset position -- correct
- [ ] NO yellow arrow on the Sun body (suppressed) -- correct

### 2.3 Moon indicator

- [ ] Center: Earth. Enable Moon shells + Earth shells. -- correct
      Generate static.
- [ ] Moon gets its own Sun Direction arrow pointing toward Sun -- correct, but toggles with the Earth's when plotted
- [ ] Moon arrow direction matches Earth arrow direction -- not parallel but both are directed towards the sun
      (both point toward the same Sun position)
- [ ] Two "Sun Direction" legend entries (one per body) -- correct, but they are both labelled "Sun Direction" 

### 2.4 Indicator on other planets (Sun checkbox OFF)

- [ ] Center: Jupiter. Sun OFF. Enable any Jupiter shell. Generate static. -- correct
- [ ] ONE yellow dashed arrow pointing toward Sun -- correct
- [ ] Center: Mars. Sun OFF. Enable any Mars shell. Generate static. -- correct as noted above
- [ ] ONE yellow dashed arrow pointing toward Sun -- correct

---

## 3. Magnetosphere sunward rotation (item 4)

The bow shock should point toward the Sun's offset position, not
along the default -X axis. **All tests with Sun checkbox OFF** to
verify the independent fetch works. -- correct

### 3.1 Earth-centered (Sun OFF)

- [ ] Center: Earth. Sun checkbox OFF. Enable magnetosphere +
      bow shock. Generate static. -- correct
- [ ] Bow shock faces toward Sun's offset position in the plot -- correct
- [ ] Magnetosphere tail extends away from Sun -- correct
- [ ] Compare against pre-D2 screenshot if available

### 3.2 Earth-centered (Sun ON, regression)

- [ ] Center: Earth. Sun checkbox ON. Enable magnetosphere +
      bow shock + Sun shells. Generate static. -- correct
- [ ] Same rotation as 3.1 (confirms both paths produce
      the same sun_position) -- correct

### 3.3 Jupiter-centered (Sun OFF)

- [ ] Center: Jupiter. Sun OFF. Enable magnetosphere.
      Generate static. -- correct
- [ ] Bow shock faces toward Sun's offset position -- correct

### 3.4 Mars-centered (Sun OFF)

- [ ] Center: Mars. Sun OFF. Enable magnetosphere + bow shock.
      Generate static. -- correct as noted above
- [ ] Bow shock faces toward Sun -- correct

### 3.5 Saturn-centered (Sun OFF)

- [ ] Center: Saturn. Sun OFF. Enable magnetosphere. Generate static. -- correct
- [ ] Bow shock faces toward Sun -- no bow shock is plotted or in the legend in either sun or saturn centered views
- [ ] No magnetic tilt applied (Saturn's dipole nearly aligned) -- correct

### 3.6 Non-center planet with shells

- [ ] Center: Sun. Select Earth orbit on. Enable Earth shells
      including magnetosphere. Generate static. -- correct
- [ ] Earth magnetosphere rendered at Earth's offset position -- correct
- [ ] Bow shock faces back toward Sun (at origin) -- correct

---

## 4. Magnetic tilt activation (item 11)

Earth 11 deg and Jupiter 10 deg magnetic tilt now active. Tilt
produces slight asymmetry in the magnetosphere envelope relative
to the bow shock direction. Bow shock should NOT show tilt
(it is a solar wind feature, not magnetic). -- correct but the 11 degree earth magnetosphere tilt is difficult to discern visually

### 4.1 Earth magnetic tilt

- [ ] Center: Earth. Enable magnetosphere + bow shock. Generate static. -- correct
- [ ] Magnetosphere envelope shows slight asymmetry (11-deg tilt) -- correct; see above note
- [ ] Bow shock is symmetric about the Sun direction (no tilt) -- correct
- [ ] The two features visibly differ in their orientation -- correct; see above note

### 4.2 Jupiter magnetic tilt

- [ ] Center: Jupiter. Enable magnetosphere. Generate static. -- correct but no bow shock trace
- [ ] Magnetosphere envelope shows slight asymmetry (10-deg tilt) -- tilt is likely correct not discernible angle

### 4.3 Uranus unchanged

- [ ] Center: Uranus. Enable magnetosphere. Generate static.
- [ ] 60-deg tilt still renders correctly (pre-existing, not new) -- see image
- [ ] Bow shock now receives sun_position from dispatch (new wiring) -- no bow shock is rendering or in legend
- [ ] Tilt character unchanged from pre-D2

---

## 5. Neptune diamond marker (item 12, Option C)

Old magnetic axis line + 2 pole markers (4 traces) replaced by
a single diamond marker showing the offset magnetic center.

### 5.1 Diamond marker present

- [ ] Center: Neptune. Enable magnetosphere. Generate static.
- [ ] ONE yellow diamond marker labeled "Neptune: Magnetic Field Center"
- [ ] Diamond visible near the planet body

### 5.2 Old traces removed

- [ ] NO magnetic axis line visible
- [ ] NO pole markers visible (were yellow dots at north/south poles)
- [ ] Legend: 1 entry for magnetic center, not 4

### 5.3 Hover and legend behavior

- [ ] Hover the diamond: shows text about 0.55-radii offset,
      47-degree tilt, Voyager 2 1989
- [ ] Toggle magnetosphere off in legend: diamond also disappears
      (legendgroup linkage)

---

## 6. Animation paths (smoke only -- full wiring is D3)

D2 reverted line 6194 to avoid NameError. Animation uses default
sun_position=(0,0,0). Magnetospheres in animated frames will
NOT rotate to face Sun -- that is expected and deferred to D3.

- [ ] Center: Earth. Enable magnetosphere. Click Animate (5 frames).
      Runs without NameError. Shells render (rotation not expected). -- see above
- [ ] Center: Jupiter. Enable magnetosphere. Click Animate (5 frames).
      Runs without errors. -- see above

---

## 7. After testing

If all checks pass:
1. Copy files from sandbox to clean repo
2. Run `provenance_scanner.py` (expect 0 Tier-1 on touched files)
3. Deploy to GitHub
4. Report results for handoff document update

If issues found:
- Note which check failed and what you see
- Screenshot if visual
- We diagnose before proceeding to D3

---

## Files modified in D2

| File | Change type |
|------|-------------|
| shared_utilities.py | Complete file |
| planet_visualization.py | Targeted snippets (2a-2f) |
| shell_configs.py | 8 x needs_sun_position flag |
| earth_visualization_shells.py | Snippet 3c (largest change) |
| mercury_visualization_shells.py | Snippet 3a |
| venus_visualization_shells.py | Snippet 3b |
| mars_visualization_shells.py | Snippet 3d |
| jupiter_visualization_shells.py | Snippet 3e |
| saturn_visualization_shells.py | Snippet 3f |
| neptune_visualization_shells.py | Snippet 3g |
| uranus_visualization_shells.py | Signature only |
| orrery_rendering.py | rotate_to_sunward signature |
| palomas_orrery.py | Snippets 4a, 4c-4g + two fixes + revert + Sun fetch fix |

## Items resolved by D2

| Item | Description |
|-----:|-------------|
| 4 | sun_position threaded through all 3 layers (static only) |
| 10 | Double sun direction indicator removed |
| 11 | Earth 11-deg, Jupiter 10-deg magnetic tilt activated |
| 12 | Neptune: single diamond marker (Option C) |

## Bugs found and fixed during testing

| Bug | Root cause | Fix |
|-----|-----------|-----|
| Line 6194 NameError | Animation path referenced _sun_pos_tuple before definition | Reverted to no sun_position (D3 scope) |
| Sun-checkbox-off: no rotation/indicator | positions dict only has toggled-on objects; _sun_pos_tuple fell back to (0,0,0) | Independent Sun fetch at lines 4500-4506 |

## Deferred to D3

- Animation path sun_position wiring (frame-by-frame Sun position)
- Manifest snippet 4b numbering clarification
- Snippet 4e comment rewording (suppression mechanism)
