# D3.1 Sweep -- Testing Protocol (v3, post-dispatch-path-fix)

**Date:** May 23, 2026
**Tester:** Tony Quintanilla
**Mode:** Mode 5 (visual verification -- Tony leads)
**Files changed:** 15 `*_visualization_shells.py` + `orrery_rendering.py`
+ `shared_utilities.py`

---

## What changed since v2

During Tony's Mode 5 visual test of Render 1 (Mercury), inconsistent
Rule 2 header application was observed. Investigation revealed that
standard interior shells for ALL 12 bodies render through a unified
config-driven dispatch (`build_sphere_shell` in `orrery_rendering.py`,
fed by `SHELL_CONFIGS` in `shell_configs.py`) that the original D3.1
inventory never saw.

A structural fix was applied to `build_sphere_shell` and
`create_sun_direction_indicator` -- two single-block edits that bring
83 sphere-shell pairs across 13 bodies into Rule 2 compliance.

**Status:** Both smoke tests pass. Mercury's interior shells now lead
with their legend labels. The Mode 5 visual protocol below now
includes a double-header advisory for 14 shells across 6 bodies where
the legend label header sits above a prose lead-in that also names
the shell (intentional, evaluate for ugliness).

---

## Pre-test: Drop files into working directory

Copy these into `palomas_orrery_for_github/`. Overwrite existing.

| File | From | Notes |
|------|------|-------|
| 15 `*_visualization_shells.py` | May 22 sweep + May 23 Earth fix | Per-body files |
| `orrery_rendering.py` | **NEW (May 23 PM)** | Dispatch-path fix |
| `shared_utilities.py` | **NEW (May 23 PM)** | Sun direction indicator fix |

Confirm no import errors on launch before starting visual checks.

---

## What the sweep changed (what you're verifying)

1. **Rule 2 prepend:** Every info marker hover now starts with its
   legend label as a header, separated by a blank line (`<br><br>`)
   from the description body. This applies to:
   - Per-body custom geometry (magnetospheres, rings, radiation
     belts, LEO/GEO) via the original sweep
   - Standard interior shells (core, mantle, crust, atmosphere,
     hill_sphere) via the May 23 PM dispatch-path fix
   - Sun direction indicator at non-origin positions

2. **Newline normalization:** All `\n` in hover strings replaced with
   `<br>` (per-body files).

3. **Legendgroup wiring:** Solar labels renamed to `"Sun: X"`,
   Neptune diamond hidden from legend, comet placeholders get
   explicit legendgroups, crust/cloud surface traces linked to their
   info markers, Moon Hill Sphere renamed.

---

## Test structure

Eight representative renders. Each tests a different batch or pattern.
For each render, check the four verification criteria. Stop and note
any anomaly -- don't fix in place.

### The four checks (apply to every render)

| # | Check | What to look for |
|---|-------|------------------|
| A | **Header present** | Hover starts with the legend label (e.g., "Mercury: Magnetosphere") |
| B | **Blank line gap** | Visible blank line between header and description body |
| C | **No literal `\n`** | No truncated or garbled text where `\n` was |
| D | **Legend toggle** | Clicking the legend entry hides BOTH the geometry AND the info marker cross |

---

## Mode 5 Note: Double-Header Survey

The dispatch-path fix (May 23 PM) introduces 14 shells where the
legend label header sits above a prose lead-in that also names the
shell. Structurally correct but visually redundant. Evaluate during
the relevant render and mark verdict.

| Body | Shell | Render where seen |
|------|-------|-------------------|
| Mercury | inner_core | Render 1 |
| Mercury | outer_core | Render 1 |
| Mercury | mantle | Render 1 |
| Mercury | atmosphere | Render 1 |
| Mercury | hill_sphere | Render 1 |
| Eris | mantle | (separate render if available) |
| Eris | atmosphere | (separate render if available) |
| Jupiter | metallic_hydrogen | Render 3 |
| Jupiter | molecular_hydrogen | Render 3 |
| Mars | mantle | (separate render if available) |
| Mars | upper_atmosphere | (separate render if available) |
| Moon | outer_core | Render 7 |
| Pluto | haze_layer | (separate render if available) |
| Pluto | atmosphere | (separate render if available) |

If any look ugly, the fix is a content edit to the relevant
`hover_text` field in `shell_configs.py` to remove the redundant
prefix from the prose. This is content judgment, not structural.

---

## Render 1: Mercury (dispatch-path fix verification + Pattern A)

**Special note:** This was the render where Tony first noticed the
inconsistent header application. The May 23 PM dispatch-path fix
should now resolve it. Mercury's crust specifically -- which Tony
flagged as "does not have a label and has to be interpreted" --
should now lead with `"Mercury: Crust<br><br>..."`.

**Setup:** Render Mercury. Set manual scale to at least 0.002 AU.

**Hover targets (split by code path):**

*Dispatch-path shells (NEW in v3 -- via build_sphere_shell):*
- Inner Core info marker
- Outer Core info marker
- Mantle info marker
- **Crust info marker (the original complaint -- verify it now has a header)**
- Exosphere (atmosphere) info marker
- Hill Sphere info marker

*Per-body custom-geometry shells (already verified in v1/v2):*
- Sodium Tail info marker -- checkbox does not trigger sun direction indicator
- Magnetosphere info marker -- checkbox does not trigger sun direction indicator
- Bow Shock info marker

**Specific concerns:**
- All 6 dispatch-path shells should now lead with `"Mercury: <Name>"`
  as a header.
- 5 of the 6 dispatch-path shells have double-header prose lead-ins.
  Evaluate each for visual ugliness (see Double-Header Survey above).
- Mercury had `\n` in its config-dict description strings (`_info`
  tuples at the top of the file) that feed GUI tooltips, not Plotly
  hover -- verify Plotly hovers are clean regardless.

**Check A/B/C/D on each hover target.** -- correct. shortened the magnetosphere description so that it fits in the info box. note that like venus and earth, when rendered alone the magnetosphere shell does not trigger a "Sun Direction" indicator, but the hill sphere does trigger it alone; i did not test each shell separately. this seems to be a general pattern and should be checked. 

-- Venus test: all pass. Legacy issue: the magnetosphere and upper atmosphere descriptions exceed the maximum size of the info box. this was also the case for mercury's magnetosphere, but i edited it to reduce its size. is there a better solution? this should be solved in this session if possible because it will affects the info dictionary (earth's magnetosphere) if we carry this change back to the github repo. i also tested the venus magnetosphere selection separately and like earth it does not trigger a "Sun Direction" indicator along with the magnetosphere and bow shock shells. but if i add the venus hill sphere then the sun direction indicator is triggered.  

---

## Render 2: Earth (Batch 4 + Batch 5 -- runtime-fixed May 23 AM + dispatch fix May 23 PM)

**Status note:**
- May 23 AM: per-body Earth file fixed (custom geometries: magnetosphere,
  LEO, GEO, Hill Sphere via CUSTOM_SHELLS dispatch)
- May 23 PM: dispatch-path fix covers Earth's interior shells (inner core,
  outer core, lower mantle, upper mantle, crust, atmosphere, upper
  atmosphere) via build_sphere_shell

Note: the per-body Earth interior shell builders (`create_earth_inner_core_shell`,
etc.) still exist with correct prepends, but the active dispatch is
now SHELL_CONFIGS-driven. Both code paths produce the same hover.

**Setup:** Render Earth. Set manual scale to at least 0.001 AU for
inner shells.

**Hover targets (all should have Rule 2 headers):** -- all correct
- Any interior shell (core, mantle, crust) -- via dispatch path
- LEO shell info marker -- via custom-geometry path -- checkbox does not trigger sun direction indicator
- Geostationary Belt info marker -- via custom-geometry path -- checkbox does not trigger sun direction indicator
- Hill Sphere info marker -- via custom-geometry path
- Magnetosphere info marker (4 markers: magnetosphere, bow shock,
  inner Van Allen, outer Van Allen) -- via custom-geometry path -- checkbox does not trigger sun direction indicator

**Specific concerns:**
- Crust shell legend entry should toggle BOTH the Mesh3d surface AND
  the cross info marker (Batch 4 linkage). -- correct
- Earth's three known double-headers from the May 23 AM fix (Crust,
  LEO, GEO) -- evaluate ugliness. Note Crust's double-header now has
  TWO sources: the AM fix in `earth_visualization_shells.py` AND the
  PM dispatch-path fix from `build_sphere_shell` (but only one is
  active -- the dispatch path). -- correct and acceptable

**Check A/B/C/D on each hover target.** -- pass

-- special note: i tested the earth-moon system with the barycenter as the center object and all the moon shells but only the magnetosphere shell selected for earth. the moon shells all are rendered with their hovertext correctly. however for earth only the following shells are rendered: magnetosphere, bow shock, and the two radiation belts. importantly, earth's sun direction indicator does not render. however, then i replotted adding earth's hill sphere and then earth's sun direction indicator does plot. however, and this is minor, the two sun direction indicators are not distinguished in the legend, both are labelled "Sun Direction" and they are grouped so that they both toggle on and off together not separately. the same labelling standard should be used for the sun direction indicators as for other shells, namely "Earth: Sun Direction" and "Moon: Sun Direction" and they should toggle independently. 

-- Mars test: all correct except that the "Mars: Induced Magnetosphere" is missing its info marker. this may be a D2 error that was missed. like mercury, venus and earth, selecting the "Magnestosphere" checkbox alone does not trigger a "Sun Direction" indicator. however, selecting "Hill Sphere" or "Upper Atmosphere" alone does. I did not check each shell separately. this seems to be an issue isolated to the Magentosphere rendering code. 

---

## Render 3: Jupiter (Batch 5 Pattern C loops + dispatch fix)

**Setup:** Render Jupiter.

**Hover targets:**

*Dispatch-path shells:* -- render correctly
- Core info marker
- Metallic Hydrogen info marker (double-header watch)
- Molecular Hydrogen info marker (double-header watch)
- Cloud Layer info marker
- Upper Atmosphere info marker

*Custom-geometry shells:* -- render correctly except as noted
- Magnetosphere info marker -- magnetosphere still needs a bow shock shell and selecting the checkboxes for magnetosphere, plasma torus, radiation belts and ring system do not trigger a sun direction indicator
- Io Plasma Torus info marker
- Any radiation belt info marker (3 belts, loop-generated)
- Any ring info marker (4 rings, loop-generated)

**Specific concern:** Radiation belts and rings are loop-generated -- render correctly
(Pattern C). The per-body sweep used `belt_names[i]` and
`f"Jupiter: {ring_info['name']}"`. Verify each belt/ring info marker
matches its corresponding legend entry.

**Check A/B/C/D on each hover target.**

-- Saturn test: -- correctly rendered except: magnetosphere needs bow shock; and selecting the checkboxes for magnetosphere, plasma torus, radiation belts and ring system do not trigger the sun direction indicator. 

-- Uranus test: -- correctly rendered except: magnetosphere hovertext is truncated; selecting the checkboxes for magnetosphere, radiation belts and ring system do not trigger sun direction indicator

---

## Render 4: Neptune (Batch 2 + Batch 5, items 44-46 + dispatch fix)

**Setup:** Render Neptune.

**Hover targets:** -- correctly rendered except as noted
- Any interior shell -- via dispatch path
- Magnetosphere info marker (item 44, was truncating, now fixed) -- does not trigger sun direction indicator; hovertext is truncated
- Magnetic Field Center diamond marker (Batch 2 -- should NOT appear
  as separate legend entry but should be hoverable in the plot) -- correct
- Any radiation belt info marker (item 45) -- does not trigger sun direction indicator
- Any FAC info marker (item 46)
- Any ring/arc info marker -- ring hovertext markers are superimposted; arc and adams ring hovertext markers are superimposed; do not trigger sun direction indicator

**Specific concerns:** -- correctly rendered except as noted
- Magnetosphere legend toggle should hide envelope geometry, diamond
  marker, AND magnetosphere info marker cross. -- hovertext is truncated; 
- The diamond should be invisible in the legend sidebar but visible
  and hoverable in the plot.

**Check A/B/C/D on each hover target.**

-- Pluto test: correctly rendered

-- Eris test: correctly rendered

---

## Render 5: Solar / Oort Cloud (Batch 1 renames + Batch 5 + dispatch fix)

**Setup:** Render the Sun. Various scales for different shells.

**Hover targets:** -- correctly rendered

*Dispatch-path shells (Sun has 15 in SHELL_CONFIGS!):*
- Sample 3-4 of these. Examples: "Sun: Heliopause", "Sun: Termination
  Shock", "Sun: Gravitational Influence", any Oort Cloud shell, Hills
  Cloud, Galactic Tide Region.

**Specific concerns:** -- correctly rendered
- All legend entries should read "Sun: X" (no "Solar Wind Heliopause",
  no "Sun's Gravitational Influence"). Batch 1 = 9 renames.
- Solar had 388 `\n` instances in config dicts -- verify hovers are
  clean.
- Config-dict descriptions still contain `\n` and feed GUI tooltips
  via `globals()`. That separate rendering path may render `<br>`
  literally -- if so, that's a known dual-path issue (config dicts
  for tooltips, Plotly hover_text for plots).

**Check A/B/C/D on a sample of 3-4 hover targets.**

---

## Render 6: MAPS Comet (Batch 2 legendgroups + Batch 5)

**Setup:** Render MAPS. Since MAPS disintegrated, you'll see
placeholder legend entries for inactive features.

**Hover targets:** -- seems correct except as noted
- Disintegration diamond marker -- minor issue: this is a position in space so the marker should be an open square not a filled diamond. otherwise correct.
- Ghost Tail info marker (cross on the debris arc) -- the trace is not visible superimposed to the orbital trace. maybe make it thicker? 
- Nucleus placeholder (if visible -- disintegrated)
- Any inactive placeholder ("MAPS: Coma (inactive, >X AU)", etc.) -- i plotted the comet on 4/5/26 and it clearly shows the comet structure except for the nucleus. i assume this is the remains of the comet, but the hovertext label or text is not clear on this point

**Specific concerns:** -- seems correct except as noted
- Each inactive placeholder should have an explicit `legendgroup`.
  Toggling one should NOT toggle others.
- Disintegration marker hover should start with "MAPS: Disintegration"
  header.
- Ghost Tail hover has an existing `<b>MAPS: Ghost Tail (debris arc)</b>`
  bold header. The Batch 5 prepend adds `MAPS: Ghost Tail (April 4-6)`
  above it -- two similar headers. Note if ugly.
- **Smoke test note:** Ghost Tail's legendgroup is snake_case
  (`maps_ghost_tail`) while the hover correctly uses the display name.
  Both smoke tests flag this as an R2 miss, but it is intentional.

-- i noticed a significant lag in updating the figure when toggling the legend elements.   

**Check A/B/C/D on each hover target.**

---

## Render 7: Moon (Batch 3 rename + Batch 5 + dispatch fix)

**Setup:** Render Moon. Set scale to ~0.001 AU.

**Hover targets:** -- correct except as noted in the earth test

*Dispatch-path shells:*
- Inner Core, Outer Core (double-header watch), Mantle, Crust,
  Exosphere

*Per-body shell:*
- Hill Sphere info marker -- legend should read "Moon: Hill Sphere"
  (was "Hill Sphere" before Batch 3)

**Specific concern:** The Batch 3 rename flowed into both `name=` and
`legendgroup=`. Verify the legend sidebar shows "Moon: Hill Sphere",
not "Hill Sphere".

**Check A/B/C/D.**

---

## Render 8: Asteroid Belt (Batch 5 -- category file)

**Setup:** Render with asteroid belt populations visible.

**Hover targets:** -- correct
- Main Asteroid Belt info marker
- Hilda Family info marker
- Jupiter Trojans (Greeks - L4) info marker

**Specific concern:** Category file -- no body prefix. The legend
label IS the population name ("Hilda Family", etc.). The prepend
should use that name as the header -- not "Asteroid Belt: Hilda Family". -- correct

**Check A/B/C/D.**

---

## Sun Direction Indicator (cross-render check)

**Specific to dispatch-path fix May 23 PM.** This indicator appears
on most renders that have shells. Pick any render with a body NOT at
the origin (e.g., a planet rendered from a heliocentric view) and
verify the Sun Direction info marker (at the arrow tip) leads with
`"Sun Direction<br><br>"` as a header. -- correct with exceptions as noted

**Check A/B/C only** (D not applicable -- the indicator does not have
its own legend entry in the standard config).

---

## Results template

```
Render 1 (Mercury):     A[ ] B[ ] C[ ] D[ ]  Notes:
  Crust now has header:    yes [ ]  no [ ]
  inner_core double-header:    looks OK [ ]  needs prose edit [ ]
  outer_core double-header:    looks OK [ ]  needs prose edit [ ]
  mantle double-header:        looks OK [ ]  needs prose edit [ ]
  atmosphere double-header:    looks OK [ ]  needs prose edit [ ]
  hill_sphere double-header:   looks OK [ ]  needs prose edit [ ]

Render 2 (Earth):        A[ ] B[ ] C[ ] D[ ]  Notes:
  Crust double-header:      looks OK [ ]  needs prose edit [ ]
  LEO double-header:        looks OK [ ]  needs prose edit [ ]
  GEO double-header:        looks OK [ ]  needs prose edit [ ]

Render 3 (Jupiter):      A[ ] B[ ] C[ ] D[ ]  Notes:
  metallic_hydrogen double-header:   looks OK [ ]  needs prose edit [ ]
  molecular_hydrogen double-header:  looks OK [ ]  needs prose edit [ ]

Render 4 (Neptune):      A[ ] B[ ] C[ ] D[ ]  Notes:
Render 5 (Solar):        A[ ] B[ ] C[ ] D[ ]  Notes:
Render 6 (MAPS):         A[ ] B[ ] C[ ] D[ ]  Notes:

Render 7 (Moon):         A[ ] B[ ] C[ ] D[ ]  Notes:
  outer_core double-header:   looks OK [ ]  needs prose edit [ ]

Render 8 (Asteroid):     A[ ] B[ ] C[ ] D[ ]  Notes:

Sun Direction marker:    A[ ] B[ ] C[ ]      Notes:
```

---

## Edge cases to watch for (not render-specific)

- **Double headers:** Some descriptions in `shell_configs.py` start
  with the shell name in prose (e.g., "Inner Core: Mercury has..."),
  and the dispatch-path fix prepends the legend label above. The
  Double-Header Survey above lists all 14 known cases. Other prose
  patterns may produce similar effects -- note any you spot. -- acceptable

- **Very long hovers:** Some hovers (Mercury magnetosphere, solar
  shells, Mercury exosphere with the sodium-tail prose) are extremely
  long. The prepended header should still be visible at the top
  without scrolling. If the hover box runs off-screen, note it. -- a few exceed the box boundaries. these can be either manually edited unless there is another option

- **Ghost Tail redundancy:** The ghost tail hover had an existing
  `<b>MAPS: Ghost Tail (debris arc)</b>` line. The prepend adds
  `MAPS: Ghost Tail (April 4-6)` above it. Two similar headers.

- **Sun GUI tooltips:** Solar `_info` strings feed BOTH Plotly hover
  (uses `<br>`) AND GUI tooltips via `globals()` (may render `<br>`
  literally). If GUI tooltips look wrong, the fix is a targeted
  revert on the config dicts only.

---

## After testing -- review and resolve before deploying

If all 8 renders pass A/B/C/D and double-header verdicts are recorded:
D3.1 is done. Deploy to GitHub.

If any check fails: note the render, check letter, and what you see.
Screenshot if possible. Fix in next session.

If a double-header looks ugly: note which shell, and we'll edit the
`hover_text` field in `shell_configs.py` to remove the redundant prose
prefix.

---

*"The script's Rule 2 check is a weak proxy. Real verification*
*is Mode 5 visual." -- D3.1 Mode 7 lesson, May 22*

*"Compile-only verification is the absence of a runtime test,*
*not a substitute for one." -- D3.1 runtime-fix lesson, May 23 mid*

*"We tested the trees while Plotly renders from the forest."*
*-- D3.1 dispatch-path lesson, May 23 PM*

*"Tony's eyes win. The inventory said clean, the smoke test said*
*clean, Mode 5 said no."*
