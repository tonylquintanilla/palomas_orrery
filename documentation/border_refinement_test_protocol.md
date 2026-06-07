# Test Protocol -- Border Refinement + Osculating Marker Fix

**Date:** _______________
**Tester:** Tony
**Build:** Border refinement (groups 1-3) + osculating marker fix (group 4), finalized May 29, 2026
**Scope:** 4 files. `shell_configs.py` (7 reversions to red, 3 additions to white), `asteroid_belt_visualization_shells.py` (2 Trojan borders to white), `mars_visualization_shells.py` (1 crustal-field border to white), `idealized_orbits.py` (perihelion osculating marker: NameError fix + placement + size).

**Convention this round refines:** The two-standards boundary is now a *spectrum* rule with both ends pinned. White border holds on saturated mid-warm fills (bright/burnt orange, the pink-reds, dense reds). It reverts to **red** on the two ends of the warm ramp: pale peach `rgb(255,180,140)` and golden-yellow `rgb(255,215,0)` -- both lose the white cross to the fill. The category is "warm fills that compete with a red border," and the peach/golden ends don't.

**Roster after this round:** 18 SHELL_CONFIGS sites carry `info_border: 'white'` (was 17 going in; net +1 from Roche, +2 Mars mantle/crust, -2 of the original peach/golden being among the 7 reversions... see Section 3 for the exact post-round roster).

---

## Section 0 -- Smoke Test [CRITICAL] -- pass / fail

Estimated time: 5 min

Catches: import/syntax failure in any of the 4 changed files. `idealized_orbits.py` and `shell_configs.py` are imported at startup -- a syntax error in either prevents launch entirely. The osculating fix added `np.argmin` / `np.nonzero` logic; a scope error (`r_full`, `q_osc` not defined) would surface only when a comet perihelion view is plotted, so that view is part of this smoke test.

- [ ] Launch `palomas_orrery.py` -- correct
- [ ] GUI opens with no `ImportError` / `SyntaxError` -- correct
- [ ] Console clean on startup -- correct
- [ ] Sun-centered default view renders -- correct
- [ ] Earth-centered view renders (touched: inner_core reverted) -- correct
- [ ] Mars-centered view renders (touched: mantle, crust, crustal fields) -- correct
- [ ] A comet perihelion view renders via **Go: Perihelion** (touched: osculating marker) -- no `[PeriOsc] Error...` in console -- correct

**Result:** &nbsp;&nbsp; [ ] PASS &nbsp;&nbsp; [ ] FAIL

**Notes:**
```


```

---

## Section 1 -- Osculating Marker Now Renders [CRITICAL] -- pass / fail

Estimated time: 15 min

Catches: the headline of group 4. The perihelion osculating info marker referenced an undefined `color` (NameError), so it was silently dropped and **had never rendered** -- the arc appeared with no marker. The fix defines `color = 'white'` and the marker should now appear. This is also where a placement bug (on perihelion instead of near it) or a hover-unwrap bug would show.

**Setup:** Press **Go: Perihelion** on a comet (the button sets center=Sun, apsidal markers on, scale q*4 -- the trigger conditions for Capability D). Test one hyperbolic and one elliptical comet to exercise both conic branches.

| Comet | Conic | Marker present? | Near perihelion, NOT on it? | Hover shows osculating text? | PASS | FAIL | Notes |
|---|---|:---:|:---:|:---:|:---:|:---:|---|
| 3I/ATLAS | hyperbolic | [ ] | [ ] | [ ] | [ ] | [ ] | | -- same as ikeka seki except that keplerian and osculating orbit info markers are not superimposed. anti-tail and mini ject info markers are superimposed.
| Halley (1986) | elliptical (moderate) | [ ] | [ ] | [ ] | [ ] | [ ] | | -- the keplerian and osculating orbit info markers are close but not superimposed. the coma doesa not completely hide the info marker. 
| MAPS (C/2026 A1) | near-parabolic elliptical | [ ] | [ ] | [ ] | [ ] | [ ] | | -- correct
ikeya_seki: the osculating and keplerian orbit info markers are superimposed. the coma info marker is hidden within the coma and difficult to discern. 

Expected per comet: one **white cross, size 8**, sitting on the osculating arc on the **outbound (post-perihelion) side**, at roughly twice the perihelion distance (`r ~ 2q`). At the Go:Perihelion default scale, 2q is well inside the view, so the cross should sit clearly off perihelion, not at the closest point. Hover shows the multi-line "Osculating Orbit" text (e, a, q in AU and km, perihelion velocity, and the non-grav shift if present) -- not empty, not a bracketed list literal.

Watch for:
- **No marker at all** -> the deployed `idealized_orbits.py` is not the fixed one (re-copy from outputs), OR `color` still undefined.
- **Marker exactly on perihelion** (the closest point of the arc) -> placement reverted to midpoint; Option B logic not applied.
- **Marker at the clip edge / far out** -> expected only if you zoomed in tighter than ~2q (arc clips before 2q, fallback uses the outermost point). At default Go:Perihelion scale it should be at ~2q, not the edge.
- **Empty / undefined hover** -> `text=[hover_text]` unwrap issue.

**Result:** &nbsp;&nbsp; [ ] PASS &nbsp;&nbsp; [ ] FAIL

**Notes:**
```


```

---

## Section 2 -- Border Reversions: white -> red [QUALITY]

Estimated time: 15 min

These 7 SHELL_CONFIGS sites had `info_border: 'white'` removed, so they fall back to the factory default **red** border. The peach and golden fills should now read better with red than they did with white (the white cross was washing out against them).

**Setup:** center on each body, scale to a fraction of body radius, enable the listed shell.

| Body | Shell | Fill RGB | Expected | PASS | FAIL | Notes |
|---|---|---|---|:---:|:---:|---|
| Mercury | inner_core | 255,180,140 (peach) | **red** cross | [ ] | [ ] | | -- correct
| Venus | core | 255,180,140 (peach) | **red** cross | [ ] | [ ] | | -- correct
| Earth | inner_core | 255,180,140 (peach) | **red** cross | [ ] | [ ] | | -- correct
| Mars | inner_core | 255,180,140 (peach) | **red** cross | [ ] | [ ] | | -- correct
| Uranus | core | 255,215,0 (golden) | **red** cross | [ ] | [ ] | | -- correct
| Neptune | core | 255,215,0 (golden) | **red** cross | [ ] | [ ] | | -- correct
| Sun | Streamer Belt (Visible Corona) | 255,200,80 (golden-orange) | **red** cross | [ ] | [ ] | | -- correct

Watch for: any of these still showing a **white** cross -> the `info_border` line wasn't removed, or the running file is a stale snapshot. Confirms the deployed `shell_configs.py` is current.

**Result:** &nbsp;&nbsp; [ ] PASS &nbsp;&nbsp; [ ] FAIL

**Notes:**
```


```

---

## Section 3 -- Border Additions: red -> white [QUALITY]

Estimated time: 10 min

Three sites gained `info_border: 'white'` (two Mars sphere shells + the Sun Roche Limit, which is a SHELL_CONFIGS sphere shell routed through the factory, not the comet file).

| Body | Shell | Fill RGB | Expected | PASS | FAIL | Notes |
|---|---|---|---|:---:|:---:|---|
| Mars | mantle | 205,85,85 (pink-red) | **white** cross | [ ] | [ ] | | -- correct
| Mars | crust | 188,39,50 (dense red) | **white** cross | [ ] | [ ] | | -- correct
| Sun | Roche Limit (Comets) | 200,60,60 (dense red) | **white** cross | [ ] | [ ] | | -- correct

Setup notes: Mars mantle/crust -- center Mars, enable the interior shells (toggle crust off to see mantle). Roche Limit -- Sun-centered, ~0.01 AU; it sits at ~3.45 solar radii.

Watch for: Roche still **red** -> the add landed in the wrong dict. (Reminder: `roche_limit` exists in both `SHELL_CONFIGS` and `CUSTOM_SHELLS`; the live render is the SHELL_CONFIGS one because the dispatch checks configs first. The CUSTOM_SHELLS duplicate is dead -- if Roche reads white, the live path is confirmed.)

**Result:** &nbsp;&nbsp; [ ] PASS &nbsp;&nbsp; [ ] FAIL

**Notes:**
```


```

---

## Section 4 -- Custom-geometry inline border changes [QUALITY]

Estimated time: 10 min

These are inline `create_info_marker(...)` calls inside live CUSTOM_SHELLS builders (not factory/config). Border changed to white; fill unchanged.

| Marker | Setup | Fill | Expected border | PASS | FAIL | Notes |
|---|---|---|---|:---:|:---:|---|
| Asteroid Trojan L4 (Greeks) | Sun-centered, ~6 AU | rgb(180,100,100) reddish | **white** cross | [ ] | [ ] | | -- correct
| Asteroid Trojan L5 (Trojans) | Sun-centered, ~6 AU | rgb(160,80,80) reddish | **white** cross | [ ] | [ ] | | -- correct
| Mars Crustal Magnetic Fields | Mars-centered, >=0.005 AU, magnetosphere on | rgb(255,100,255) magenta | **white** cross | [ ] | [ ] | | -- correct

Watch for: the per-belt distinction in the asteroid view should read as intentional -- both Trojan camps white, while Main Belt and Hilda stay red (see Section 5). For Mars, the crustal-field cross is white while the magnetosphere and bow-shock crosses from the same builder stay red.

**Result:** &nbsp;&nbsp; [ ] PASS &nbsp;&nbsp; [ ] FAIL

**Notes:**
```


```

---

## Section 5 -- No-Change Regression [QUALITY]

Estimated time: 15 min

Sites NOT touched this round. They should look identical to last week's gallery.

### 5.A -- Stayed red (should remain red)

| Marker | Setup | Expected | PASS | FAIL |
|---|---|---|:---:|:---:|
| Asteroid Main Belt | Sun ~3 AU | red cross (white fill) | [ ] | [ ] | -- correct
| Asteroid Hilda | Sun ~4 AU | red cross | [ ] | [ ] | -- correct
| Mars Magnetosphere | Mars >=0.005 AU | red cross | [ ] | [ ] | -- correct
| Mars Bow Shock | Mars >=0.005 AU | red cross | [ ] | [ ] | -- correct

### 5.B -- Stayed white (pre-existing white roster, 15 sites untouched)

Spot-check a sample; full list for reference. These had `info_border: 'white'` before this round and were not edited.

| Body | Shells (white border) | PASS | FAIL |
|---|---|:---:|:---:|
| Mercury | outer_core, mantle | [ ] | [ ] | -- correct
| Moon | inner_core, outer_core | [ ] | [ ] | -- correct
| Pluto | core, mantle | [ ] | [ ] | -- correct
| Eris | core, mantle | [ ] | [ ] | -- correct
| Venus | mantle | [ ] | [ ] | -- correct
| Mars | outer_core | [ ] | [ ] | -- correct
| Earth | outer_core, lower_mantle, upper_mantle | [ ] | [ ] | -- correct
| Uranus | mantle | [ ] | [ ] |  -- correct
| Neptune | mantle | [ ] | [ ] | -- correct

### 5.C -- Osculating arc + non-comet orbits unchanged

| Check | Expected | PASS | FAIL |
|---|---|:---:|:---:|
| Osculating **arc** (the white line itself) | Unchanged from before -- only the marker is new | [ ] | [ ] |
| Planet / asteroid orbit markers (Keplerian/mean/actual) | Unchanged -- still white (deliberately left as-is this round) | [ ] | [ ] |

**Result:** &nbsp;&nbsp; [ ] PASS &nbsp;&nbsp; [ ] FAIL

Any difference here -> conversion bug (a color literal typo, a wrong dict entry, or a stale file). Flag the site.

**Notes:**
```


```

---

## Section 6 -- Known limitations / non-actions [PRACTICE]

Not failures -- behavior confirmed acceptable this round, logged so they aren't re-flagged.

- **Orbit marker color (Keplerian/mean/actual) left white.** The codebase-wide white->red orbit-marker switch is parked, not done. Expected to still be white.
- **Osculating marker border is white** (not red) per the May 29 decision; fill is also white. Single `color` variable governs line + marker fill; the marker outline is hardcoded white to match the other orbit functions.
- **Marker placement depends on plot scale.** Via Go:Perihelion the scale is q*4, so the marker sits at ~2q. On a manually-scaled view tighter than 2q, the marker falls back to the outermost arc point -- still near perihelion, by design.
- **Carried over from last round (not this round's work):** Eris crust/atmosphere markers superimposed; Mercury sodium-tail marker hidden behind the body when Mercury-centered; Jupiter Metis/Adrastea analytical orbit markers nearly superimposed. Position-clutter items, deferred.

---

## Exit Decision

- [ ] **ALL PASS** -> Round lands. Write handoff v15 noting completion; flag the dead `CUSTOM_SHELLS['Sun']['roche_limit']` + `create_sun_roche_limit_shell` as a Phase 2 dead-code cleanup candidate.
- [ ] **Section 0 fails** -> Do not merge. Syntax/import error; identify which of the 4 files and recompile.
- [ ] **Section 1 fails (osculating marker)** ->
  - No marker -> deployed `idealized_orbits.py` is stale; re-copy from outputs.
  - On perihelion -> placement logic not applied.
  - Bad hover -> variable unwrap; investigate `text=[hover_text]`.
- [ ] **Section 2 fails (a reversion still white)** -> stale `shell_configs.py`, or the `info_border` line wasn't removed. Localized.
- [ ] **Section 3 fails (Roche still red)** -> add landed in the dead CUSTOM_SHELLS entry instead of SHELL_CONFIGS, or stale file.
- [ ] **Section 4 fails (Trojan/crustal still red)** -> inline `border_color='white'` not applied; check the specific call.
- [ ] **Section 5 fails (regression)** -> compare the changed file against the original diff; find the unintended edit.
- [ ] **Uranus/Neptune golden cores look wrong even with red** -> the golden case was always the weakest; note for a future pass.
- [ ] **Other** (describe).

**Decision date:** _______________

**Final notes:**
```


```

---

**Estimated total:** ~70 min thorough; ~20 min fast pass (Sections 0, 1, and a Section 2/3 sample).

---

## Lessons captured this round (for archive)

- **A marker can be written and never render.** The osculating info marker existed in code since March 10 but referenced an undefined `color`; the NameError was swallowed by the caller's try/except, leaving the arc with no marker. "The code is there" is not "the code runs" -- same family as v14's dead-code lesson, but the inverse: live path, dead variable. The tell was Tony's eyes ("no marker at all"), not the code reading as correct.
- **Assign, don't hardcode, to stay in the pattern.** The fix could have hardcoded `color='white'` in the marker dict. Defining `color = 'white'` once and referencing it (line + marker fill) matches every other orbit function and makes a future restyle a one-line change. Tony's call, and the more correct one.
- **The two-standards rule has two pinned ends.** Not "warm fills get white" but "saturated mid-warm fills get white; pale peach and golden-yellow at the ends of the ramp revert to red." The boundary is contrast against a red border, not an RGB threshold.
- **A shell in two dicts is governed by dispatch order, not by which dict you edit.** Roche lives in both SHELL_CONFIGS and CUSTOM_SHELLS; the `if configs ... elif customs` order means SHELL_CONFIGS wins and the custom entry (plus its builder) is dead. Editing the live dict is correct only after confirming the dispatch -- the same trap v14 named.
