# Phase 1 Test Protocol — Info Marker Factory Re-pipe

**Date:** _______________  
**Tester:** Tony  
**Build:** Phase 1 deliverables, finalized May 29, 2026  
**Scope:** 37 inline info markers re-piped to `create_info_marker()` factory across 7 files + 22 SHELL_CONFIGS sites with `info_border: 'white'` under the two-standards convention

**Two-standards convention:** Factory default is `border_color='red'` for non-reddish shells (gives the cross contrast against blue/green/gray dot fields). Reddish/orange/golden fills get `border_color='white'` — applied either at the inline factory call (CUSTOM_SHELLS sites: Van Allen inner belt, Roche Limit, MAPS ghost tail) or via the `info_border: 'white'` key in SHELL_CONFIGS (22 sphere shells, see Section 4).

---

## Section 0 — Smoke Test [CRITICAL] -- pass

Estimated time: 5 min

Catches: import failure on the 5 new `from orrery_rendering import create_info_marker` lines (asteroid_belt / earth / moon / solar / comet). Also catches the magnetosphere signature regression that surfaced May 28 — Earth-centered plots should render rather than crash on `TypeError: sun_position`.

- [ ] Launch `palomas_orrery.py`
- [ ] GUI opens with no `ImportError`
- [ ] Console shows no errors on startup
- [ ] Sun-centered default view renders successfully
- [ ] **Earth-centered view renders without `TypeError: got an unexpected keyword argument 'sun_position'`** (this was the May 28 crash; fixed by reverting `earth_visualization_shells.py` to your upload as base)

**Result:** &nbsp;&nbsp; [ ] PASS &nbsp;&nbsp; [ ] FAIL

**Notes:**

```


```

---

## Section 1 — Hover-Text Sanity [CRITICAL] -- pass

Estimated time: 10 min

Catches: the riskiest class of bug — `text=variable[0]` unwraps where the factory call passes a single-element list field. If the unwrap is wrong, hover shows empty / undefined / a bracketed list literal.

**Setup:** Earth-centered, scale ~0.05 AU, enable Magnetosphere + Bow Shock + Van Allen Belts.

| Marker | Expected hover content | PASS | FAIL | Notes |
|---|---|:---:|:---:|---|
| Earth: Magnetosphere | Multi-line text about Earth's magnetic field structure | [ ] | [ ] | |
| Earth: Bow Shock | Multi-line text about the bow shock boundary | [ ] | [ ] | |
| Van Allen Inner Belt | Text describing inner belt | [ ] | [ ] | |
| Van Allen Outer Belt | Text describing outer belt | [ ] | [ ] | |
| Hill Sphere (newly factory-routed) | Multi-line text about Earth's Hill Sphere | [ ] | [ ] | |

**Result:** &nbsp;&nbsp; [ ] PASS &nbsp;&nbsp; [ ] FAIL -- pass

**Notes:**

```


```

---

## Section 2 — Visual Changes Phase 1 Introduces [QUALITY]

Estimated time: 20 min

These are the deliberate visual changes. Verify each category renders as expected.

### 2.A — Earth pale/light structures: default red border, size 8 -- pass

**Setup:** Earth-centered, ~0.1 AU. -- all correct

These were already factory-routed in your live code with the factory default red border. Mode 5 testing previously marked them acceptable. Confirming no regression.

| Marker | Fill color | Expected | PASS | FAIL | Notes |
|---|---|---|:---:|:---:|---|
| Magnetosphere | bluish rgb(180,180,255) | Red border, size 8 | [ ] | [ ] | |
| Bow Shock | warm pale rgb(255,200,150) | Red border, size 8 | [ ] | [ ] | |
| LEO | pale yellow rgb(255,248,220) | Red border, size 8 | [ ] | [ ] | |
| GEO | pale blue rgb(220,220,255) | Red border, size 8 | [ ] | [ ] | |
| Hill Sphere (newly converted) | green rgb(0,255,0) | Red border, size 8 | [ ] | [ ] | |

### 2.B — Van Allen loop: per-belt borders (two-standards) -- pass

**Setup:** Earth-centered, narrow scale (~0.001 AU range). -- all correct

Per your May 29 decision: inner reddish belt gets white border, outer blue belt gets red border. The "acceptable" annotation on uniform red was right, but the per-belt treatment is better.

| Marker | Fill color | Expected border | PASS | FAIL | Notes |
|---|---|---|:---:|:---:|---|
| Inner Radiation Belt | reddish rgb(255,100,100) | **white** cross | [ ] | [ ] | |
| Outer Radiation Belt | blue rgb(100,200,255) | **red** cross | [ ] | [ ] | |

Watch for: the per-belt distinction should look intentional, not inconsistent. If it reads as a deliberate convention (warm fills get white, cool fills get red), the two-standards convention is working visually.

### 2.C — Solar gray-border sites: gray → red border, four with size 6→8

**Setup:** Sun-centered, vary scale per site. 

| Marker | Scale | Fill | Expected | PASS | FAIL | Notes |
|---|---|---|---|:---:|:---:|---|
| Outer Oort Cloud | ~100,000 AU | white | Red border, size 8 | [ ] | [ ] | | -- pass
| Inner Oort Cloud | ~10,000 AU | white | Red border, size 8 | [ ] | [ ] | | -- pass
| Inner Limit of Oort | ~1,000 AU | white | Red border, size 8 | [ ] | [ ] | | -- pass
| Termination Shock | ~150 AU | pale blue rgb(240,244,255) | Red border, size 8 | [ ] | [ ] | | -- pass
| Photosphere | ~0.01 AU | cream rgb(255,244,214) | Red border, size 8 | [ ] | [ ] | | -- pass

Watch for: pale Oort fills losing the cross to the dot field. If unreadable → keep gray per-site via `border_color='gray'`, one-line edit each.

-- asteroid belts: main belt and hildas: keep red border. two trojan belts change to white border for better contrast. 

### 2.D — Sun Streamer Belt: SHELL_CONFIGS white border (Category B addition, May 29)

**Setup:** Sun-centered, ~0.05 AU.

| Marker | Fill | Expected border | PASS | FAIL | Notes |
|---|---|---|:---:|:---:|---|
| Streamer Belt (Visible Corona) | golden-orange rgb(255,200,80) | **white** cross | [ ] | [ ] | | -- my error. please switch back to red border. 

### 2.E — Reddish CUSTOM_SHELLS factory calls: white border preserved

| Marker | Setup | Fill | Expected border | PASS | FAIL | Notes |
|---|---|---|---|:---:|:---:|---|
| Roche Limit (Comets) | Sun ~0.01 AU | dense red rgb(200,60,60) | **white** cross | [ ] | [ ] | | -- this shell marker has a red border, switch to white.
| MAPS Ghost Tail | MAPS comet view | reddish rgb(255,80,80) | **white** cross | [ ] | [ ] | | -- the ghost tail is white, which is correct. changes: the mean orbit, which is normally toggled off, the keplerian orbit, actual orbit seems to have the original white border style, please switch to new red style. the perihelion osculating orbit seems to be an exception: i plotted out to 8 au and there is no marker rendered at all; a marker should be rendered somewhere near perihelion (not on it) and it should also be in the new red style.

**Result for Section 2:** &nbsp;&nbsp; [ ] PASS &nbsp;&nbsp; [ ] FAIL

**Section 2 notes:**

```




```

---

## Section 3 — No-Change Regression [QUALITY]

Estimated time: 10 min

These sites were already at factory standard before Phase 1. Pure code routing, no visual change expected.

| Group | Sites | Expected | PASS | FAIL |
|---|---|---|:---:|:---:|
| Hill Spheres | Mars, Moon, Venus | Identical to last week's gallery | [ ] | [ ] | -- correct
| Asteroid belt | Main Belt, Hilda, Trojan L4, Trojan L5 | Identical | [ ] | [ ] | -- see above notes
| Comet (active) | Coma, Dust Tail, Ion Tail, Anti-tail, Mini-jet | Identical | [ ] | [ ] | -- correct
| Sun: outer | Gravitational Influence, Heliopause, Hills Cloud Torus, Outer Oort (Clumpy), Galactic Tide Region | Identical | [ ] | [ ] | -- see above
| Sun: corona | Outer Corona, Inner Corona, Alfvén Surface, Chromosphere, Radiative Zone, Core | Identical | [ ] | [ ] | -- see above

Note: Streamer Belt removed from "Sun: corona" group above — it's now under Section 2.D as a visible change.

**Result:** &nbsp;&nbsp; [ ] PASS &nbsp;&nbsp; [ ] FAIL

Any visible difference → conversion bug (color literal typo, position arg reorder). Flag the site.

**Notes:**

```


```

---

## Section 4 — SHELL_CONFIGS white-border roster [QUALITY]

Estimated time: 15 min

22 sphere shells now use `info_border: 'white'` via SHELL_CONFIGS. Render each body centered, enable the listed shells, confirm white-border crosses on warm/reddish fills.

### 4.A — Dense-red shells (May 28, prior approval)

These were approved in your A/B test earlier this session. Spot-check to confirm no regression.

| Body | Shell | RGB | PASS | FAIL | Notes |
|---|---|---|:---:|:---:|---|
| Moon | outer_core | rgb(255,50,0) | [ ] | [ ] | | -- correct
| Pluto | core | rgb(255,56,0) | [ ] | [ ] | | -- correct
| Pluto | mantle | rgb(150,0,0) | [ ] | [ ] | | -- correct
| Eris | core | rgb(187,63,63) | [ ] | [ ] | | -- correct
| Eris | mantle | rgb(150,0,0) | [ ] | [ ] | | -- correct
eris: crust and atmosphere info markers are superimposted and cannot be discerned separately unless toggled. 

### 4.B — Inner shells, warm chromatic palette (May 29 additions)

The biggest visual change in this round — every inner-shell warm fill across the inner solar system and ice giants now gets a white-bordered cross.

**Setup tip:** for each body, center on it, scale to a fraction of body radius, enable inner shells.

| Body | Shell | RGB | PASS | FAIL | Notes |
|---|---|---|:---:|:---:|---|
| Mercury | inner_core | rgb(255,180,140) | [ ] | [ ] | | -- this color is an edge case; switch back to red
| Mercury | outer_core | rgb(255,140,0) | [ ] | [ ] | | -- correct
| Mercury | mantle | rgb(230,100,20) | [ ] | [ ] | | -- correct
| Moon | inner_core | rgb(255,100,0) | [ ] | [ ] | | -- correct
| Venus | core | rgb(255,180,140) | [ ] | [ ] | | -- this color is an edge case; switch back to red
| Venus | mantle | rgb(230,100,20) | [ ] | [ ] | | -- correct
| Earth | inner_core | rgb(255,180,140) | [ ] | [ ] | confirmed May 29 screenshot | -- this color is an edge case; switch back to red
| Earth | outer_core | rgb(255,140,0) | [ ] | [ ] | confirmed May 29 screenshot | -- correct
| Earth | lower_mantle | rgb(230,100,20) | [ ] | [ ] | confirmed May 29 screenshot | -- correct
| Earth | upper_mantle | rgb(205,85,85) | [ ] | [ ] | | -- correct
| Mars | inner_core | rgb(255,180,140) | [ ] | [ ] | | -- this color is an edge case; switch back to red
| Mars | outer_core | rgb(255,140,0) | [ ] | [ ] | | -- correct
| Uranus | core | rgb(255,215,0) | [ ] | [ ] | golden — borderline yellow | -- switch back to red
| Uranus | mantle | rgb(255,138,18) | [ ] | [ ] | | -- correct
| Neptune | core | rgb(255,215,0) | [ ] | [ ] | golden — borderline yellow | -- switch back to red
| Neptune | mantle | rgb(255,138,18) | [ ] | [ ] | | -- correct

-- mercury: the sodium tail info marker will be hidden behind the Mercury object trace if it is enabled with Mercury as the center object because the marker is located at the center. 
-- mars: switch mantle, crust, and crustal magenetic fields to white.
-- jupiter: Metis and Adrastea analytical orbit markers are nearly superimposed.
-- saturn: correct

Watch for: Uranus / Neptune golden cores (rgb(255,215,0)). If the white cross looks indistinct against the golden fill rather than crisp, the golden case is the weakest test — falls between true orange and yellow. If it reads poorly, we revert those two to default red.

**Result:** &nbsp;&nbsp; [ ] PASS &nbsp;&nbsp; [ ] FAIL

**Notes:**

```




```

---

## Section 5 — Hover-Text AU Convention [PRACTICE]

Estimated time: as you go

Per protocol line 85, all distance hover text should include AU alongside km. Not a Phase 1 task, but flag anything spotted. -- no. the hover text for all includes km and earth radii, but not AU. in this near-earth context this is acceptable. however, this is something to note. the hill sphere radius of about 0.01 au can be estimated from the plot grid. 

| Marker | Has AU? | Notes |
|---|:---:|---|
| GEO altitude | [ ] yes [ ] no | |
| LEO altitude | [ ] yes [ ] no | |
| Hill Spheres | [ ] yes [ ] no | | 
| Other observations | | |

---

## Exit Decision

- [ ] **ALL PASS** → Phase 1 lands. Update handoff to v15 noting completion. Phase 2 (dead-code sphere shells) becomes next track.
- [ ] **Section 0 fails (Earth-centered crash)** → Do not merge. The reverted `earth_visualization_shells.py` isn't the one in the sandbox. Re-copy from outputs.
- [ ] **Section 1 (hover) fails** → Do not merge. Flag which site; variable unwrap needs investigation.
- [ ] **Section 2.B fails (Van Allen per-belt inconsistent)** → Revert to uniform red or uniform white in the loop.
- [ ] **Section 2.C fails (Oort / Photosphere red borders unreadable)** → Don't roll back. Add `border_color='gray'` to the 5 solar sites, one-line each.
- [ ] **Section 3 fails** → Find which site, compare factory call to original inline block. Localized fix.
- [ ] **Section 4.B fails (Uranus / Neptune golden cores)** → Remove `info_border: 'white'` from those two entries; revert to factory default red. Other 4.B sites unaffected.
- [ ] **Other** (describe below)

**Decision date:** _______________

**Final notes:**

```




```

---

**Estimated total:** ~65 min thorough pass (Section 4 is the time addition vs prior version), ~20 min fast smoke + Section 0/1/4.B sample.

---

## Lessons captured this session (for archive)

- **`/mnt/project/` staleness is per-file, not session-wide.** Six of seven uploaded files matched the snapshot byte-for-byte; only `earth_visualization_shells.py` had drifted. Active-edit files need direct upload; quiescent files sync fine. The earth file has earned "always upload" status — twice burned now (this incident + the prior March recovery).
- **Rule-based color scoring identifies candidates, not decisions.** The R≥180 reddish heuristic missed Pluto mantle (rgb(150,0,0) — deepest red in the inventory). Mode 5 visual verification produces decisions; rules produce starting lists.
- **The "two-standards" convention is a spectrum rule, not a binary one.** Started as "dense red gets white border" (May 28); generalized to "reddish/orange/golden warm chromatic fills get white border" (May 29) once Earth orange shells visually surfaced the same contrast issue. The category is "warm fills that compete with red borders for visual presence," not a specific RGB threshold.
