# MAPS Disintegration Module Handoff
## Paloma's Orrery | April 9-10, 2026 | Claude Sonnet 4.6

---

## Session Summary

Comet MAPS (C/2026 A1) disintegrated at ~08:15 UTC April 4, 2026,
approximately 6 hours before perihelion, inside the solar corona.
Two sessions built the complete visualization and storytelling
infrastructure to document and display that event -- from the first
provisional 6AC4721 tracking through the ghost comet outbound arc,
with corrected physics, ghost tail animation, solar shell redesign,
and file size optimization.

"An experimental probe into the solar atmosphere." -- Tony
"Sad news Claude. Per Gemini, comet MAPS is no more." -- Tony, opening session 1

---

## Accomplishments

### 1. MAPS Disintegration Marker
**File: `comet_visualization_shells.py`**

New function `create_maps_disintegration_marker(position_au)`:
- Green diamond `rgb(80, 200, 120)` at the disintegration position
- Always rendered regardless of current date -- fixed historical event
- Hover card: position, distance from photosphere, solar layer
  identification, Roche limit status (with full non-absolute
  explanation), destruction mechanisms, ghost tail summary,
  363 AD lineage

Position: `_compute_maps_disintegration_position()` fetches from
Horizons at 2026-04-04 08:15 UTC (`@10` center). Falls back to
Barker's equation (perihelion-epoch elements) if Horizons unavailable.

**Bug fixed**: `r_solar_radii` and `ROCHE_KM` were undefined in
the hover f-string. Add after `dist_photosphere_au`:
```python
r_solar_radii = r_km / SUN_RADIUS_KM
ROCHE_KM = ROCHE_LIMIT_KM
```

**Key lesson**: January MPEC elements (omega=87.97, Omega=9.28)
differ from perihelion-epoch Horizons elements (omega=86.33,
Omega=7.87) by ~1.4-1.6 degrees -- enough to visibly offset the
marker from the trajectory at perihelion scale. Always fetch from
Horizons for markers that must sit on the plotted trace.

### 2. Corrected Disintegration Physics
**Critical correction made during session:**

Initial hover text incorrectly stated disintegration was inside the
Streamer Belt / Roche limit. Barker's equation confirms:

- Disintegration: **8.33 R_sun (0.039 AU)** -- between Alfven
  surface and Streamer Belt, OUTSIDE all inner shells
- Streamer Belt: 6.0 R_sun (0.028 AU) -- crossed by debris only
- Roche Limit: 3.45 R_sun (0.016 AU) -- crossed by debris only
- Inner K-corona: 3.0 R_sun (0.014 AU) -- crossed by debris only
- Perihelion: 1.23 R_sun (0.006 AU) -- debris only

**The corrected story**: MAPS was destroyed in the outer corona
by thermal ablation and rotational spin-up. Tidal forces never
acted on the nucleus -- it died before reaching the Roche limit.

**Roche limit is NOT absolute**: Tensile strength allows survival
inside it. Ikeya-Seki (~5 km, seen by Tony as a child in 1965)
survived at 1.66 R_sun (0.008 AU). Great Comet of 1843 survived
at 1.19 R_sun (0.006 AU). Size and structural coherence are
decisive. MAPS at 400 m had neither.

**Parker comparison corrected**: Parker Solar Probe closest approach
is 8.8 R_sun (0.041 AU). MAPS disintegrated at 8.33 R_sun (0.039 AU)
-- just inside Parker's record. The debris reached 1.23 R_sun.
The intact nucleus never beat Parker.

**Fallback dt_days fix** in `_compute_maps_disintegration_position()`:
```python
# BEFORE (accidentally correct but fragile):
dt_days = (2461135.0997 - 0.25) - params['TP']
# AFTER (explicit):
dt_days = -0.2548   # 6h 7min before perihelion
```

### 3. Ghost Tail Arc
**File: `comet_visualization_shells.py`**

New function `create_maps_ghost_tail_trace(fig=None)`:

Represents the debris cloud trajectory from disintegration
(8.33 R_sun, 0.039 AU, April 4 08:15) through perihelion and
outbound to SOHO/LASCO last detection (~29 R_sun, 0.132 AU,
April 6 01:00 UTC). Total: ~40 hours.

**Primary path**: Extracts x,y,z from the perihelion osculating
orbit trace already in `fig` (name contains 'Perihelion Osc. Orbit'
and 'MAPS'). Filters by distance: inbound side where r <= 8.33 R_sun,
outbound side where r <= 29 R_sun. Guarantees ghost lies precisely
on the osculating curve with no segmentation artifacts.

**Fallback**: Analytical Barker arc (same elements as marker
function) if osculating trace not found in fig.

**Visual**: `n-1` short line segments with per-segment opacity
fade, power 1.8 curve: 0.85 at disintegration to 0.04 at dispersal.

**Critical**: `legendgroup='maps_ghost_tail'` on ALL segment traces.
Without this, only the first segment (showlegend=True) responds to
legend clicks -- the remaining 38 segments stay visible permanently.

**Call site** in `add_comet_tails_to_figure()`:
```python
dis_pos = _compute_maps_disintegration_position()
if dis_pos is not None:
    for tr in create_maps_disintegration_marker(dis_pos, comet_name):
        fig.add_trace(tr)
for tr in create_maps_ghost_tail_trace(fig):   # always called; pass fig
    fig.add_trace(tr)
```

### 4. Date-Gated Disintegration Logic
**File: `comet_visualization_shells.py`**

`add_comet_tails_to_figure()` accepts `current_date=None`:
- Pre-disintegration: full comet -- nucleus, coma, dust tail, ion tail
- Post-disintegration: headless ghost -- tails renamed "Remains",
  scaled by `post_disintegration_dust_scale=0.55` / `ion_scale=0.35`;
  gray legend entry "Nucleus (disintegrated April 4, 2026)"

Activity formula fix: standard `(q/r)^1.5` fails at q=0.005729 AU.
Override key `perihelion_distance_au_activity=0.30` in
`HISTORICAL_TAIL_DATA['MAPS']` for formula only; true orbital
perihelion unchanged for all physics calculations.

### 5. Two Preset Buttons
**Files: `palomas_orrery.py`, `spacecraft_encounters.py`**

MAPS `create_comet_checkbutton` call replaced with custom two-button block:

- **"Go: Perihelion Prediction"** -- existing dynamic preset, relabeled
- **"Go: Disintegration"** -- new fixed preset:
  - Window: April 3-7, 2026 | Scale: 0.023 AU (tight) or 0.06 AU
    (complete arc, Tony's preference for full ghost story)
  - Position marker at disintegration time (2026-04-04 08:15:00)
    via `_encounter_plot_date[0]`
  - Uses fixed `tp_date` string -- no extra Horizons fetch

New `get_comet_disintegration_preset()` in `spacecraft_encounters.py`.
New `_apply_comet_disintegration_preset()` in `palomas_orrery.py`.

### 6. Revised Solar Shell Architecture
**Files: `solar_visualization_shells.py`, `planet_visualization_utilities.py`,
`planet_visualization.py`, `palomas_orrery.py`**

Seven near-Sun shells (three new this session):

| Shell | Radius | AU | Color | Physical meaning |
|-------|--------|----|-------|-----------------|
| Inner Corona (K-corona) | 3.0 R_sun | 0.014 | Blue | Electron-scattered |
| Roche Limit (Comets) | 3.45 R_sun | 0.016 | Dark red | Tidal threshold (NOT absolute) |
| Streamer Belt (Visible) | 6.0 R_sun | 0.028 | Gold | Eclipse white-light corona |
| Alfven Surface | 18.8 R_sun | 0.087 | Cyan | True corona/solar wind boundary |
| Extended Corona (F-corona) | 50 R_sun | 0.232 | Dark blue | Dust-scattered envelope |

New constants in `planet_visualization_utilities.py`:
```python
STREAMER_BELT_RADII  = 6.0
ROCHE_LIMIT_RADII    = 3.45
ALFVEN_SURFACE_RADII = 18.8
```

`hover_text_sun_and_corona` wired to solar shells master checkbutton
tooltip -- hovering shows full MAPS coronal autopsy as motivation
for turning the shells on.

### 7. Solar Shell Two-Trace Pattern + File Size Optimization
**File: `solar_visualization_shells.py` (complete rewrite of all 15 shell functions)**

**Problem**: Gallery exports 30-70 MB. Root cause: hover text
serialized once per point. At n_points=60, 3600 points x ~600 char
hover = ~2.2 MB per shell x 15 shells = ~20 MB in hover text alone.

**Solution**: Two-trace structure for ALL 15 sphere shells:
1. Shell sphere -- `hoverinfo='skip'`, purely visual, no text stored
2. Single info marker -- `cross` symbol at `(0, 0, r*1.05)` (north
   pole, 5% above shell), carries full hover text exactly once

**n_points**: outer/boundary shells 20, inner sun shells 25.
**Marker visibility**: size=3.0-3.5, opacity=0.35-0.5 (up from
0.5-1.25 / 0.2-0.3 which were invisible at 400 points).
Photosphere/radiative/core unchanged (solid bodies at size 7-10).

**Result**: 45 MB to 5 MB confirmed (89% reduction).

Three particle-cloud functions (hills cloud torus, outer oort clumpy,
galactic tide) also updated with same pattern.

**Credit line added**: "Module updated: April 2026 with Anthropic's
Claude Sonnet 4.6" in the design pattern block comment.

### 8. `hover_text_sun_and_corona` Import + Wiring
Previously defined but never imported or used. Now:
- Added to import block in `palomas_orrery.py`
- Used as tooltip for the solar shells master checkbutton

### 9. Updated INFO Strings
**File: `constants_new.py`**

`MAPS` entry fully rewritten with corrected physics, coronal journey,
Parker comparison, Roche limit non-absolute explanation, and
provenance (tracked as 6AC4721 from near-discovery).
Credit: "Module updated: April 2026 with Anthropic's Claude Sonnet 4.6.
In memoriam C/2026 A1."

---

## Corrected MAPS Coronal Journey

| Event | Distance | AU | UTC |
|-------|----------|----|-----|
| Entered SOHO/LASCO C3 | ~33 R_sun | ~0.153 AU | April 2 |
| Crossed Alfven Surface | 18.8 R_sun | 0.087 AU | April 3 ~18:00 |
| **DISINTEGRATION** | **8.33 R_sun** | **0.039 AU** | **April 4 08:15** |
| Streamer Belt (debris) | 6.0 R_sun | 0.028 AU | April 4 ~10:00 |
| Roche Limit (debris) | 3.45 R_sun | 0.016 AU | April 4 ~12:00 |
| Inner K-corona (debris) | 3.0 R_sun | 0.014 AU | April 4 ~13:00 |
| Perihelion (debris) | 1.23 R_sun | 0.006 AU | April 4 14:22 |
| Ghost dispersed | ~29 R_sun | ~0.132 AU | April 6 ~01:00 |

Ghost tracked ~40 hours by SOHO/LASCO. No ground-based visibility.
The intact nucleus never reached the Streamer Belt, Roche limit,
inner K-corona, or perihelion. Only debris did.

---

## Open Issues

### Activity Visibility at Inbound Distances
`perihelion_distance_au_activity=0.30` gives reasonable activity
within 1 AU. At ~2 AU inbound (January), no visible structure --
physically correct but users may expect something.
A note in the GUI tooltip could help.

### Post-Disintegration Tail Colors
Ghost comet tails use same orange/blue as live comet. Pale/desaturated
version would better communicate "debris." Low priority.

---

## Files Modified

| File | Changes |
|------|---------|
| `comet_visualization_shells.py` | MAPS in HISTORICAL_TAIL_DATA; nucleus size 0.4 km; `create_maps_disintegration_marker()` with corrected physics; `_compute_maps_disintegration_position()` Horizons+Barker; `create_maps_ghost_tail_trace(fig)` with legendgroup; `add_comet_tails_to_figure()` date-gating + activity override; NameError fix (r_solar_radii, ROCHE_KM); dt_days fallback fix |
| `solar_visualization_shells.py` | Complete rewrite: two-trace pattern (hoverinfo=skip + cross info marker) on all 15 shell functions; n_points=20/25; size=3.0-3.5/opacity=0.35-0.5; three new shell functions + info strings; roche_limit_info non-absolute physics; hover_text_sun_and_corona corrected MAPS timeline; credit line |
| `planet_visualization_utilities.py` | STREAMER_BELT_RADII, ROCHE_LIMIT_RADII, ALFVEN_SURFACE_RADII; deleted stray lines |
| `planet_visualization.py` | Three new shell imports + render calls in both paths |
| `palomas_orrery.py` | Three new IntVars + shell_vars + toggle + checkbuttons; hover_text_sun_and_corona import + master tooltip; MAPS two-button GUI; `_apply_comet_disintegration_preset()`; animation worker date fix |
| `spacecraft_encounters.py` | `get_comet_disintegration_preset()` |
| `constants_new.py` | MAPS + 6AC4721 INFO entries rewritten |

---

## Conventions Established

**Ghost tail legendgroup**: all segment traces must share
`legendgroup='maps_ghost_tail'`. Non-negotiable. Without it,
only the first segment toggles in the legend.

**Solar shell two-trace pattern**: visual sphere (`hoverinfo='skip'`)
+ single cross info marker at `(0, 0, r*1.05)`. Apply to all new
shells. Hover text serialized once, not N^2 times.

**Shell n_points**: outer/boundary=20, inner sun=25.
Marker size=3.0-3.5, opacity=0.35-0.5 for visibility at 400 points.

**Roche limit is not absolute**: always document in hover text.
Include survival examples (Ikeya-Seki, Great Comet of 1843).

**AU alongside solar radii**: every solar radii citation must include
AU equivalent. Standing convention across all shell and comet text.

**Disintegration marker hover**: use `<br>` not `\n` (Plotly hover
is HTML). `depth_into_corona_km` is a dead variable -- remove.

**Comet disintegration events**: model as date-gated state change
via `disintegration_date` key in `HISTORICAL_TAIL_DATA`.

**Activity formula override**: use `perihelion_distance_au_activity`
key for extreme sungrazers where q < 0.01 AU breaks `(q/r)^1.5`.

---

## Quotables This Session

"Sad news Claude. Per Gemini, comet MAPS is no more."
-- Tony, opening the session

"It's like an experimental probe into the solar atmosphere."
-- Tony, on the MAPS coronal journey

"And remember we were tracking MAPS before it even got a Horizons ID!"
-- Tony, on 6AC4721 provenance

"I saw it as a child." -- Tony, on Ikeya-Seki (1965)

"Beautiful." -- Tony, on first ghost tail render

"Nice." -- Tony, on the disintegration preset view

"Looks great!" -- Tony, on the final shell visibility result

"Aww...you didn't give yourself credit Claude!"
-- Tony, after the solar shell rewrite

---

## Gallery Status

Two views confirmed working:
1. **Context view** (April 3-7, Mercury included, auto scale):
   MAPS in relation to the inner solar system, all solar shells
   visible and layered, ghost tail sweeping outbound in gold/green.
2. **Disintegration preset** (0.06 AU, MAPS + Sun):
   Shells nested around Sun, disintegration diamond on inbound arc,
   ghost tail threading through perihelion and outbound.
   File size: ~5 MB (down from ~45 MB, 89% reduction).

Portrait/mobile export not yet tested at new shell settings.

---

## The Double Helix at Work

Gemini provided the real-time observational report (SOHO coronagraph
data, disintegration timing, headless comet status). Claude provided
the implementation and physics framework. Tony carried the context,
caught the physics errors (disintegration geometry, Roche limit
non-absoluteness, \n vs <br>, missing credit lines), and pushed
toward the story.

The shells are the chapters. The ghost tail is the arc.
The cross markers are the access points.
The MAPS timeline in `hover_text_sun_and_corona` is the story.

---

*Module updated: April 2026 with Anthropic's Claude Sonnet 4.6.*
*In memoriam C/2026 A1 (MAPS) -- the accidental solar probe.*
*Data Preservation is Climate Action. Sharing is Astronomy Action.*
