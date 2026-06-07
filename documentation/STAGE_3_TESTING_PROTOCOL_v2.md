# Stage 3 + Cleanup Round -- Testing Protocol (v2)

**Date:** May 27, 2026
**Tester:** Tony Quintanilla
**Mode:** Mode 5 (visual verification -- Tony leads)
**Files changed:** 14 from Stage 3 sweep, plus thread-1 cleanup
re-updates 4 of those (earth, eris, planet9, pluto). One additional
fix: Earth magnetosphere `sun_position` parameter (thread 2).

**Supersedes:** STAGE_3_TESTING_PROTOCOL_v1.md. v1 Scenario C was
based on a partial picture; this version rewrites C and adds D for
the dispatch-level findings that the cleanup round surfaced.

---

## What changed (full session summary)

| Change | Count |
|------|-------|
| Info-marker style conversion | 73 |
| Info-marker red-on-red preserves | 8 |
| Ring marker geometry fixes | 2 (Saturn, Uranus) |
| Per-shell `sun_direction` calls deleted (duplicates) | 20 (14 v9 + 6 thread-1) |
| Dead `create_sun_direction_indicator` imports removed | 10 |
| Pre-existing dispatch TypeError fixed | 1 (Earth magnetosphere `sun_position` kwarg) |
| `n_points=50 -> 25` normalization | 1 (Planet 9 hill sphere) |
| `create_info_marker` migration-intent docstring | 1 (orrery_rendering.py) |

Container-side gates passed: `py_compile` on every edited file,
import test on every edited module, functional execution of every
marker-producing function and every preserved exception, ring
marker position uniqueness (7/7 Saturn, 11/11 Uranus), and the new
duplicate-indicator check (exactly 1 indicator per affected body in
heliocentric view, 0 in body-centered view).

This protocol is the Mode 5 gate that compile + execute cannot
perform: visual contrast judgment on the new red-border standard,
ring marker placement on the rings, and confirmation that the
dispatch-level findings render correctly.

---

## What's new in v2 (vs v1)

1. **Scenario C is rewritten.** v1 asked "verify the v9 zero-
   behavior-change claim by confirming nothing visibly changed."
   v2 asks "verify the *correct* new state: exactly one Sun
   Direction indicator per body, where there were previously two
   (Eris, Planet 9, Pluto) or zero (Earth magnetosphere, due to a
   pre-existing TypeError).
2. **Scenario D is new.** Earth magnetosphere specifically -- it
   was crashing before, so this protocol's job is to confirm it
   now renders at all.
3. **Affected file list under Scenario C is corrected.** v1
   listed the 6 bodies that had v9-deleted calls (asteroid_belt,
   earth, jupiter, mars, saturn, venus). v2 lists ALL 9 bodies
   whose dispatch produces the dispatch-level indicator: those
   6 plus eris, planet9, pluto.

---

## Test structure

Five scenarios. A and B unchanged from v1. C rewritten. D new.
E and F (optional) preserved as the v1 D and E.

- **Scenario A** -- Representative breadth pass on info markers.
- **Scenario B** -- Ring marker fix (Saturn, Uranus).
- **Scenario C** -- Sun Direction indicator: ONE per body, body-
  prefixed, correctly suppressed at body-centered view.
- **Scenario D** -- Earth magnetosphere renders at all (pre-existing
  bug fix verification).
- **Scenario E** -- Planet 9 hill sphere n_points normalization
  (optional, low-risk).
- **Scenario F** -- `create_info_marker` docstring (optional,
  source-read only).

---

# Scenario A -- Representative breadth pass on info markers

(Unchanged from v1. Reproduced here so this file is self-contained.)

**Setup:** Plot each of the 6 bodies in heliocentric view with all
shells visible. -- general comment: i initiated the red outline for shells that were grey, or blue or green in the black background. however, in contrast with red or redish shells the red outlines are difficult to discern. maybe we should consider two standards, going back to a white outline in contrast to redish shells. 

| Body | Mode 5 flag layers | Preserved layers |
|------|--------------------|------------------|
| **Earth** | inner core orange-red, lower mantle reddish-brown, upper mantle reddish-brown | **radiation belt (1 of 2 in loop)** | -- correct. the contrast is acceptable.
| **Mars** | inner core orange-red, mantle reddish-brown | **crust (Mars red)** | -- acceptable
| **Jupiter** | Amalthea ring `rgb(180, 120, 100)` | none | -- acceptable
| **Moon** | inner core red-orange | **outer core (charcoal red)** | -- the contrast with the outer core is challenging. the cross cannot be seen except on edge. l
| **Pluto** | none | **core, mantle** | -- both are difficult to read in the redish background. 
| **Sun** | none | **Roche limit** | -- acceptable 
-- Eris: both core and mantle markers are difficult to read

**Generic checks (apply to every shell in every render):**

| # | Check | What to look for | Pass [ ] |
|---|-------|------------------|:--------:|
| A1 | Info marker presence | One cross marker per shell at the "top" position | [ ] | -- yes
| A2 | Info marker size | Visibly larger than before (size 8 vs old size 6) | [ ] | -- yes
| A3 | Info marker border | Red outline (not white) on all standardized markers | [ ] | -- see above note on two standards; red for blue-green-yellow; white for red-orange
| A4 | Info marker hover | Hover card shows shell name + full description | [ ] | -- yes
| A5 | Geometry trace toggle | Toggling a shell hides BOTH the geometry AND its info marker | [ ] | -- yes
| A6 | Marker visible against fill | Red border visible against the marker's own fill color | [ ] | -- see above

**Mode 5 specific checks:**

| # | Check | Pass [ ] |
|---|-------|:--------:|
| AE1 | Earth inner_core (orange-red) -- red border reads cleanly | [ ] | -- acceptable
| AE2 | Earth lower_mantle (reddish-brown) -- red border reads cleanly | [ ] | -- acceptable
| AE3 | Earth upper_mantle (reddish-brown) -- red border reads cleanly | [ ] | -- acceptable 
| AE4 | **Earth radiation belts** -- both belts use OLD style (loop-shared marker dict; size 6, white border) | [ ] | -- acceptable
| AM1 | Mars inner_core (orange-red) -- red border reads cleanly | [ ] | -- acceptable
| AM2 | Mars mantle (reddish-brown) -- red border reads cleanly | [ ] | -- acceptable
| AM3 | **Mars crust (Mars red)** -- OLD style, white border on Mars red | [ ] | -- acceptable 
| AJ1 | Jupiter Amalthea ring (reddish-brown) -- red border reads cleanly | [ ] | -- are you thinking about the main ring? in both cases, they are acceptable
| AMo1 | Moon inner_core (red-orange) -- red border reads cleanly | [ ] | -- acceptable
| AMo2 | **Moon outer_core (charcoal red)** -- OLD style | [ ] | -- not readable. use white border. 
| AP1 | **Pluto core** -- OLD style | [ ] | -- difficult to read
| AP2 | **Pluto mantle** -- OLD style | [ ] | -- difficult to read
| AS1 | **Sun Roche limit** -- OLD style; closest case to true red | [ ] | -- acceptable only because the density of dots is less than the center planetary shells. 

---

# Scenario B -- Ring marker fix verification

(Unchanged from v1. Reproduced for completeness.)

## B1 -- Saturn

**Setup:** Plot Saturn with ring system enabled. Tilt view to
inspect the ring plane.

| # | Check | Pass [ ] |
|---|-------|:--------:|
| B1.1 | Each ring's info marker at distinct radial distance, not stacked | [ ] | -- yes
| B1.2 | Each marker sits on or at outer edge of its own ring | [ ] | -- yes
| B1.3 | Tilt preserved (markers in ring plane, not horizontal) | [ ] | -- yes
| B1.4 | Each marker hovers its own ring (no cross-contamination) | [ ] | -- yes
| B1.5 | Per-ring legend toggle hides trace + marker | [ ] | -- y3w

## B2 -- Uranus

**Setup:** Plot Uranus with ring system enabled.

| # | Check | Pass [ ] |
|---|-------|:--------:|
| B2.1 | 11 ring markers at 11 distinct positions | [ ] | -- yes
| B2.2 | Each marker on its own ring | [ ] | -- yes
| B2.3 | Extreme tilt preserved (rings nearly perpendicular to ecliptic) | [ ] | -- yes
| B2.4 | Per-ring hover correctness | [ ] | -- yes
| B2.5 | Per-ring legend toggle | [ ] | -- yes

---

# Scenario C -- Sun Direction indicator: ONE per body (REWRITTEN)

This scenario replaces v1's Scenario C. The previous version was
asking the wrong question.

**The dispatch landscape:**

Every body except the Sun now flows through the unified dispatch
in `planet_visualization.create_celestial_body_visualization`. The
dispatch fires ONE Sun Direction indicator per body at its post-loop
step, scaled to the outermost active shell radius, with the
indicator labeled with the body name (e.g. `'Earth: Sun Direction'`,
`'Pluto: Sun Direction'`).

Before this session, several bodies had per-shell `sun_traces`
calls inside the shell builders themselves. These were duplicates
of the dispatch's post-loop indicator. The cleanup deleted all
of them (20 calls across 11 files). Net effect for the user:

- **9 affected bodies** (asteroid_belt, earth, jupiter, mars,
  saturn, venus from v9; plus eris, planet9, pluto from thread-1)
  now show **exactly one** Sun Direction indicator instead of two.
- Body-centered views correctly suppress the indicator (the body
  is at origin, the Sun is at origin, no meaningful direction).

**The container-side check has already proven exactly-one-indicator
for Earth, Eris, Planet 9, Pluto.** This Mode 5 check is the visual
confirmation that the indicator actually renders correctly.

## C1 -- Heliocentric view: exactly one indicator per body

**Setup:** Plot each of the 9 affected bodies in heliocentric view
with all shells visible. For each body, look in the legend for
entries containing "Sun Direction".

The 9 bodies: **asteroid_belt, earth, eris, jupiter, mars,
planet9, pluto, saturn, venus**.

| # | Check | What to look for | Pass [ ] |
|---|-------|------------------|:--------:|
| C1.1 | Asteroid belt has exactly one indicator | Legend entry `Sun Direction` or `Main Belt: Sun Direction` (label depends on body_name parameter) -- not two | [ ] | -- no. there is no sun direction indicator and that is right because the asteroid belts are heliocentric like sun shells
| C1.2 | Earth has exactly one indicator | `Earth: Sun Direction` -- not also a bare `Sun Direction` | [ ] | -- correct
| C1.3 | Eris has exactly one indicator | `Eris: Sun Direction` -- not two | [ ] | -- correct
| C1.4 | Jupiter has exactly one indicator | `Jupiter: Sun Direction` -- not two | [ ] | -- correct
| C1.5 | Mars has exactly one indicator | `Mars: Sun Direction` -- not two | [ ] | -- correct
| C1.6 | Planet 9 has exactly one indicator | `Planet 9: Sun Direction` -- not two | [ ] | -- correct; note that Planet 9 cannot be selected as a central object
| C1.7 | Pluto has exactly one indicator | `Pluto: Sun Direction` -- not two | [ ] | -- correct
| C1.8 | Saturn has exactly one indicator | `Saturn: Sun Direction` -- not two | [ ] | -- correct
| C1.9 | Venus has exactly one indicator | `Venus: Sun Direction` -- not two | [ ] | -- correct

## C2 -- Indicator points sunward

| # | Check | What to look for | Pass [ ] |
|---|-------|------------------|:--------:|
| C2.1 | Indicator arrow direction | From the body toward the Sun (at origin in heliocentric view) | [ ] |
| C2.2 | Indicator length scales with body | Sized to ~115% of the body's outermost active shell radius. Inner planets have short indicators; Planet 9 has a long one | [ ] |
| C2.3 | Indicator toggle | Clicking the legend entry hides the indicator. Doesn't affect any shell traces | [ ] |

## C3 -- Body-centered view: indicator is suppressed

**Setup:** Plot Earth (or Mars, or Pluto -- any of the 9) in
body-centered view (set Earth as the center body).

| # | Check | What to look for | Pass [ ] |
|---|-------|------------------|:--------:|
| C3.1 | No Sun Direction indicator in legend | The legend should NOT contain `Earth: Sun Direction` (or whichever body is centered) -- the dispatch suppresses the indicator when body is at origin | [ ] | -- this would be a regression. the actual plot does show the sun direction indicator in earth center view. we implemented this in a previous session. 
| C3.2 | Console shows suppression message | If you have stdout visible, you'll see `Sun direction indicator: Suppressed (body at Sun position)`. This is not required to see in the GUI, but if it's there, that's correct | [ ] |

## C4 -- Centering on the Sun

**Setup:** Plot solar shells with Sun as center body.

| # | Check | What to look for | Pass [ ] |
|---|-------|------------------|:--------:|
| C4.1 | No Sun Direction indicator on Sun shells | The dispatch's post-loop indicator is suppressed for the Sun (object_type='Sun' triggers early return). No `Sun: Sun Direction` entry | [ ] | -- correct

## What this scenario is NOT testing

- **Comet sun direction indicators.** The 3 comet-internal
  `sun_traces` calls are LIVE (not duplicates) -- comets receive
  their actual ephemeris position from `add_comet_tails_to_figure`,
  not via the unified dispatch. Comet indicators are tested in
  Stage 2D protocol, not here.

---

# Scenario D -- Earth magnetosphere renders (NEW)

**Why this scenario exists:** during the cleanup round audit, a
pre-existing bug surfaced. `create_earth_magnetosphere_shell` was
registered in CUSTOM_SHELLS with `needs_sun_position: True`, but
the function signature didn't accept that kwarg. Every attempt to
render Earth's magnetosphere through the unified dispatch raised
`TypeError: create_earth_magnetosphere_shell() got an unexpected
keyword argument 'sun_position'`.

This bug predates this session. The other 8 magnetosphere builders
(Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, plus
Mercury sodium tail) all had the correct signature; Earth was
the lone anomaly.

Thread 2 fix: added `sun_position=(0, 0, 0)` to the Earth
magnetosphere signature. The body of the function doesn't yet use
the parameter (the magnetosphere is rendered in body-frame coords
and re-oriented sunward by the rendering layer), but the signature
now matches the dispatch contract.

**Setup:** Plot Earth in heliocentric view with magnetosphere
shell selected.

| # | Check | What to look for | Pass [ ] |
|---|-------|------------------|:--------:|
| D1 | Earth magnetosphere renders | The magnetosphere shape is visible -- teardrop body with bow shock toward the Sun, magnetotail away from the Sun. Before this fix, the plot would crash or the shell would silently not render | [ ] | -- correct
| D2 | Bow shock visible | The compressed sunward boundary is rendered as a separate trace | [ ] | -- correct
| D3 | Magnetotail visible | The extended anti-sunward tail is rendered | [ ] | -- correct
| D4 | Both Van Allen belts visible | Inner belt (`rgb(255, 100, 100)`, reddish) and outer belt (`rgb(100, 200, 255)`, blue), both with OLD-style info markers per the radiation belt loop preserve | [ ] | -- acceptable
| D5 | Single Sun Direction indicator | Exactly one `Earth: Sun Direction` (no duplicate from the now-deleted per-shell call). This is C1.2 from above, restated | [ ] | -- correct
| D6 | No console TypeError | If you have stdout visible, no `TypeError: ... got an unexpected keyword argument 'sun_position'` message. If you don't have stdout visible, D1 passing covers it | [ ] |

---

# Scenario E (optional) -- Planet 9 hill sphere n_points

(v1 Scenario D, renumbered.)

`n_points` was normalized from 50 to 25 on Planet 9 hill sphere.
The shell will look very slightly less smooth.

| # | Check | Pass [ ] |
|---|-------|:--------:|
| E1 | Planet 9 hill sphere still recognizable as a sphere | [ ] | -- yes
| E2 | Geometry still renders, info marker still present | [ ] | -- yes

---

# Scenario F (optional) -- create_info_marker docstring

(v1 Scenario E, renumbered.)

| # | Check | Pass [ ] |
|---|-------|:--------:|
| F1 | Docstring describes accomplished state | [ ] |
| F2 | Module list accurate (13 modules) | [ ] |
| F3 | Exception rule documented | [ ] |

---

## Results template

```
Scenario A -- Breadth pass (info markers):
  Generic checks
    A1 Info marker presence:                   [ ]
    A2 Info marker size visibly larger:        [ ]
    A3 Red border on standardized markers:     [ ]
    A4 Hover card no regression:               [ ]
    A5 Legend toggle hides both:               [ ]
    A6 Marker visible against fill (general):  [ ]
  Body-specific (Mode 5 contrast judgment)
    AE1 Earth inner_core red border:           [ ]
    AE2 Earth lower_mantle red border:         [ ]
    AE3 Earth upper_mantle red border:         [ ]
    AE4 Earth radiation belts preserved OLD:   [ ]
    AM1 Mars inner_core red border:            [ ]
    AM2 Mars mantle red border:                [ ]
    AM3 Mars crust preserved OLD:              [ ]
    AJ1 Jupiter Amalthea ring red border:      [ ]
    AMo1 Moon inner_core red border:           [ ]
    AMo2 Moon outer_core preserved OLD:        [ ]
    AP1 Pluto core preserved OLD:              [ ]
    AP2 Pluto mantle preserved OLD:            [ ]
    AS1 Sun Roche limit preserved OLD:         [ ]

Scenario B -- Ring marker fix:
  Saturn (B1)
    B1.1 Distinct positions on rings:          [ ]
    B1.2 Markers on the rings:                 [ ]
    B1.3 Tilt preserved:                       [ ]
    B1.4 Per-ring hover correctness:           [ ]
    B1.5 Legend toggle:                        [ ]
  Uranus (B2)
    B2.1 Distinct positions on rings:          [ ]
    B2.2 Markers on the rings:                 [ ]
    B2.3 Extreme tilt preserved:               [ ]
    B2.4 Per-ring hover correctness:           [ ]
    B2.5 Legend toggle:                        [ ]

Scenario C -- Sun Direction: ONE per body
  Heliocentric (C1)
    C1.1 Asteroid belt: one indicator:         [ ]
    C1.2 Earth: one indicator:                 [ ]
    C1.3 Eris: one indicator:                  [ ]
    C1.4 Jupiter: one indicator:               [ ]
    C1.5 Mars: one indicator:                  [ ]
    C1.6 Planet 9: one indicator:              [ ]
    C1.7 Pluto: one indicator:                 [ ]
    C1.8 Saturn: one indicator:                [ ]
    C1.9 Venus: one indicator:                 [ ]
  Indicator quality (C2)
    C2.1 Arrow points sunward:                 [ ]
    C2.2 Length scales with body:              [ ]
    C2.3 Toggle hides only indicator:          [ ]
  Body-centered suppression (C3)
    C3.1 No Sun Direction in legend:           [ ]
    C3.2 Console suppression message:          [ ] (optional)
  Sun-centered (C4)
    C4.1 No Sun Direction on Sun shells:       [ ]

Scenario D -- Earth magnetosphere renders:
    D1 Magnetosphere shape visible:            [ ]
    D2 Bow shock visible:                      [ ]
    D3 Magnetotail visible:                    [ ]
    D4 Both Van Allen belts visible:           [ ]
    D5 Single Sun Direction indicator:         [ ]
    D6 No console TypeError:                   [ ]

Scenario E (optional) -- Planet 9 n_points:
    E1 Hill sphere still recognizable:         [ ]
    E2 Geometry + info marker render:          [ ]

Scenario F (optional) -- Docstring:
    F1 Migration-intent paragraph present:     [ ]
    F2 Module list accurate:                   [ ]
    F3 Exception rule documented:              [ ]

Notes / anomalies / Mode 5 reversal candidates:
```

---

## After testing

**If all checks pass:**

1. Stage 3 sweep + cleanup round are complete. 14 files ready to deploy:
   - 13 `*_visualization_shells.py` (asteroid_belt, earth*, eris*,
     jupiter, mars, moon, neptune, planet9*, pluto*, saturn, solar,
     uranus, venus). Files marked `*` are from thread-1 cleanup
     re-update.
   - `orrery_rendering.py` (migration-intent docstring).
2. Suggested commit message:
   `Stage 3 sweep + cleanup round (D3.1 v13): 73 marker conversions,
   8 preserves, 2 ring fixes, 20 duplicate sun_direction calls
   removed (14 v9 + 6 thread-1), 10 dead imports removed, Earth
   magnetosphere TypeError fixed, n_points normalization, docstring
   update.`
3. Regenerate `MODULE_ATLAS.md` (15 files have credit-line updates:
   14 from the sweep + thread 1 + thread 2, plus
   `planet_visualization.py` if you want the thread-2 finding
   recorded there as well).
4. Run `provenance_scanner.py` -- no source citations touched, expect clean.
5. Write handoff v13 with three findings: the sweep itself, the
   cleanup round, and the Earth magnetosphere TypeError (the
   third one is a Lesson for the archive).
6. Next session entry: Stage 4 from v12 deferred list
   (`idealized_orbits.py:7331` color fix, center body no-shells
   edge case, Jupiter/Saturn bow shocks, Shell Resolution GUI,
   Studio editor comprehensive review).

**If any Mode 5 check (Scenario A) fails (warm-tone contrast):**

Same reversal recipe as v1 -- one line per site, swap marker dict
back to old style, add inline comment.

**If any Scenario B (ring) check fails:**

- Wrong plane: check that `x_final, y_final, z_final` is in scope
  at the marker call site.
- Single position regression: the `str_replace` didn't land.
  Check Saturn ~line 1170 and Uranus ~line 1060.

**If any Scenario C (sun direction) check fails:**

There are two structurally different failure modes:

- **Two indicators where there should be one (C1.X fails):** the
  thread-1 deletion didn't land for that body. Re-check that
  body's `*_visualization_shells.py` for any remaining
  `sun_traces = create_sun_direction_indicator(...)` call.
- **Zero indicators where there should be one:** the dispatch's
  post-loop indicator is broken. Check `planet_visualization.py`
  line 437 area for changes; check that the body is in
  CUSTOM_SHELLS or SHELL_CONFIGS and that `outermost_radius_au`
  is computed correctly.
- **Suppression failure (C3.1 fails -- indicator visible in
  body-centered view):** check `shared_utilities.py` line 70
  (the `dist < 1e-10` branch). This would be a regression in
  the suppression logic itself.

**If any Scenario D (Earth magnetosphere) check fails:**

D1 specifically -- if Earth magnetosphere doesn't render, the
thread-2 fix didn't land. Check that
`create_earth_magnetosphere_shell` signature in
`earth_visualization_shells.py` (around line 632) is:

```python
def create_earth_magnetosphere_shell(center_position=(0, 0, 0), sun_position=(0, 0, 0)):
```

Not:

```python
def create_earth_magnetosphere_shell(center_position=(0, 0, 0)):
```

---

## Lessons surfaced this session

For the handoff archive:

1. **"v9 was a convenience, not determinative" (Tony's framing,
   May 27 2026).** A handoff document is a working summary, not
   an authoritative scope boundary. The actual scope was always
   "all dormant calls." Treating v9's list as the scope led to
   stopping short; treating it as a starting point led to the
   complete cleanup.

2. **Verify universal-propagation claims with grep AND with
   end-to-end dispatch tracing.** The asteroid-belt finding (v12)
   was that v12's list was incomplete. The Earth-magnetosphere
   finding (this session) was that the function's signature didn't
   match the dispatch contract. Both kinds of mismatch hide until
   the dispatch is actually exercised; both are findable by tracing
   the call path from GUI through dispatch through builder.

3. **Pre-existing bugs surface from adjacent work.** The Earth
   magnetosphere TypeError predates this session and would have
   continued to predate any future session that didn't trace the
   dispatch end-to-end. The cleanup round wasn't designed to find
   bugs, but ended up exposing one. This is the value of working
   with one's hands inside the machine.

4. **Mode 5 protocol design must follow the actual code state,
   not the intended state.** v1 of this protocol asked the wrong
   question for Scenario C because it was written from the
   incomplete dispatch picture. The complete dispatch picture
   changed the question from "did v9's deletions break anything"
   to "is the dispatch producing exactly one indicator per body."

---

*"Tony's eyes win."*

*Module updated: May 27, 2026 with Anthropic's Claude Opus 4.7*
*(Stage 3 sweep + cleanup round test protocol v2: 73 conversions,*
*8 preserves, 2 ring fixes, 20 dormant deletions + 10 dead imports,*
*Earth magnetosphere TypeError fix, n_points normalization,*
*migration-intent docstring)*
