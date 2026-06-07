# HANDOFF: Shell Consolidation Stage 3 -- Phase 1 Landed + Border Refinement (v15)

**Date:** May 29, 2026
**Session model:** Claude Opus 4.8
**Supersedes:** v14 (dispatch discovery -- still correct; this builds on it)
**Predecessor of record:** v14

---

## READ THIS FIRST: what landed this session

Two things closed out this session, both tested and verified by Tony's eyes:

1. **The Phase 1 info-marker factory re-pipe is COMPLETE and tested.**
   The test protocol from v14's plan was run. Both CRITICAL sections
   (smoke + hover) passed; the no-change regression passed. The border
   refinement decisions below came out of that test pass.

2. **The perihelion osculating info marker is FIXED.** It had never
   rendered since March 10 (a NameError on an undefined `color` was
   silently swallowed by the caller's try/except, leaving the arc with
   no marker). It now renders -- verified across hyperbolic (3I/ATLAS),
   moderate-elliptical (Halley), and near-parabolic (MAPS) comets.

The v14 dispatch map is confirmed live: changing `info_border` in
SHELL_CONFIGS now changes the render. Option A (factory `border_color`
param + per-config `info_border` key) is in place and working. The
dead-code trap v14 named is closed for the active path.

---

## Files changed this session (all in outputs, all verified)

All four: compile clean (`py_compile`), ASCII-only, LF endings, and
diffed against the upload base to confirm no drift.

### `shell_configs.py` -- border roster now 18 white-border sites

**7 reversions** (removed `info_border: 'white'` -> factory default red):
- Mercury inner_core, Venus core, Earth inner_core, Mars inner_core
  -- all pale peach rgb(255,180,140)
- Uranus core, Neptune core -- golden-yellow rgb(255,215,0)
- Sun Streamer Belt -- golden-orange rgb(255,200,80) (was Tony's flagged
  May 29 error; reverted)

**3 additions** (added `info_border: 'white'`):
- Mars mantle rgb(205,85,85) (pink-red)
- Mars crust rgb(188,39,50) (dense red)
- Sun Roche Limit (Comets) rgb(200,60,60) (dense red) -- this was
  initially MISFILED as a comet-file inline edit; it is actually a
  SHELL_CONFIGS sphere shell on the live factory path (see "Roche
  dispatch note" below).

Post-round roster: 18 sites with `info_border: 'white'`. Full list in
the test protocol Section 3/5.

### `asteroid_belt_visualization_shells.py` -- 2 inline border changes

- Trojan L4 (Greeks) and Trojan L5 (Trojans) info markers gained
  `border_color='white'` (reddish dot fields).
- Main Belt and Hilda left at factory red. Docstring breadcrumb added.
- These are live CUSTOM_SHELLS-builder inline calls (Path 2), not
  factory/config.

### `mars_visualization_shells.py` -- 1 inline border change

- Crustal Magnetic Fields info marker (magenta rgb(255,100,255)) gained
  `border_color='white'`. In the live `create_mars_magnetosphere_shell`
  builder (Path 2). Magnetosphere + bow-shock markers in the same
  builder stay factory red. Docstring breadcrumb added.

### `idealized_orbits.py` -- osculating marker fix (the headline)

In `plot_perihelion_osculating_orbit` (the ONLY function touched;
diffed to confirm). Four changes, all in the marker block:
- **Bug fix:** `color` was undefined -> `color = 'white'` defined once,
  referenced by both the line trace and the marker fill (house pattern;
  one place to restyle). This is what makes the marker render at all.
- **Placement:** was exactly on perihelion (`len//2`); now near
  perihelion -- first outbound point where `r >= 1.5*q` (with fallback
  to the outermost point if the view clips before 1.5q).
- **Size:** 6 -> 8 (matches the other orbit markers).
- **Border:** stays white (per Tony, May 29). Fill white, border white.
- Docstring breadcrumb added.

---

## The osculating marker: full story (for the record)

The marker code existed since March 10 but had a latent NameError:
`marker=dict(..., color=color, ...)` where `color` was never assigned
in the function (the parameter is `color_map`; the line trace hardcoded
`'white'`). At runtime the arc trace was added first, then the marker
line raised NameError, the caller's try/except caught it and printed
`[PeriOsc] Error...`, and the marker was dropped. Result: arc out to
8 AU, no marker -- exactly what Tony saw. The marker had never rendered
in ~11 weeks.

**Placement design (resolved conversationally):**
- Initial: Option B at 2q (first outbound point at twice perihelion
  distance). Physically meaningful, consistent across conic types.
- The 2q point landed visually near other near-perihelion markers on
  some comets (ikeya_seki tightest). A long design exchange explored
  whether to move it.
- **Resolved (Mode 5, Tony's call): 1.5q.** Keeps the marker in the
  interesting near-perihelion segment while sitting clearly off
  perihelion. Verified on the MAPS plot -- the osculating cross sits
  cleanly separated from the perihelion-box cluster.

**Important scope correction reached during that exchange:** the
"Keplerian orbit info cross" (`kep_info_idx = len(x_final) // 4` in
`plot_idealized_orbits`) is placed on the FULL Keplerian ellipse near
APHELION ("opposite perihelion for clarity"), and is GENERIC (every
object, planets included). It is NOT a near-perihelion marker and `q`
has no clean meaning for a general orbit -- so it cannot and should not
be moved to a "3q" basis. The only free, comet-scoped lever is the
osculating marker. The Keplerian and all other markers were left
untouched. (This corrects two wrong mental models built from the code
during the session -- the plot and Tony's eyes overrode them. Same
spirit as v14's Lesson 6.)

---

## Roche dispatch note (confirms v14, closes the question)

`roche_limit` exists in BOTH `SHELL_CONFIGS['Sun']` and
`CUSTOM_SHELLS['Sun']` (byte-identical, the custom one builderless).
The dispatch in `create_celestial_body_visualization` is
`if shell in configs ... elif shell in customs` -- SHELL_CONFIGS wins,
so the custom entry is permanently shadowed (dead). Also:
- `create_sun_visualization` is RETIRED (raises NotImplementedError;
  docstring redirects to the new dispatch).
- `create_sun_roche_limit_shell` (in solar_visualization_shells.py) is
  import-only, never called -- the only path that would reach it
  (`create_planet_shell_traces`'s `globals()` lookup) is itself never
  called. Dead, exactly as v14 found for the inline sphere-shell path.

So the live Roche fix is the one-line `info_border: 'white'` in
SHELL_CONFIGS. Confirmed white in the test (Section 3) -- which itself
re-verifies the SHELL_CONFIGS-wins dispatch empirically.

**Phase 2 dead-code candidate:** `CUSTOM_SHELLS['Sun']['roche_limit']`
(shadowed duplicate) + `create_sun_roche_limit_shell` (uncalled). Both
are the v14 "inert but misleading" category. Strip when the honest-
shell-files pass happens; no rush, no visual consequence either way.

---

## Convention refined this session: the two-standards spectrum

The "warm fills get white border" rule is now a spectrum rule with
BOTH ENDS PINNED:

- **White border** holds on saturated mid-warm fills: bright/burnt
  orange (255,140,0 / 230,100,20 / 255,138,18), the pink-reds
  (205,85,85), and dense reds (188,39,50 / 200,60,60 / the Pluto/Eris/
  Moon reds).
- **Reverts to red** at the two ends of the warm ramp: pale peach
  (255,180,140) and golden-yellow (255,215,0). Both lose the white
  cross to the fill -- peach is too light, golden is too close to
  yellow.

The category is "warm fills that compete with a red border for visual
presence" -- NOT an RGB threshold. The peach and golden ends don't
compete, so red reads better there. This is a Mode 5 spectrum
judgment; rules produce candidate lists, Tony's eyes produce the
boundary.

---

## Deferred: comet info-marker superposition cluster (NEW)

Fixing the osculating marker made it visible, which surfaced a
pre-existing neighbor-collision that was invisible while the marker
didn't render. These are POSITION-clutter items (fixed-position single
info markers landing near each other), not border or placement bugs.
Grouped as the next design item:

- **Osculating cross near other near-perihelion crosses** -- worst on
  ikeya_seki, fine on MAPS after 1.5q. The 1.5q move addressed the
  MAPS case; ikeya_seki is the tight one and may still want attention.
- **Coma info marker hidden inside the coma sphere** -- worst on
  ikeya_seki, partial on Halley, fine on 3I/ATLAS. Coma marker at a
  fixed position the coma can swallow at some scales.
- **Anti-tail and mini-jet markers superimposed** -- 3I/ATLAS.

**Before the design pass:** confirm which two markers actually collide
on ikeya_seki by HOVERING and reading the labels. This session
established the participants by reasoning, not observation -- and the
reasoning was wrong twice. Get the hover labels first, design second.

This joins the existing deferred position-clutter list: Eris crust/
atmosphere superimposed, Mercury sodium-tail marker hidden behind the
body when Mercury-centered, Jupiter Metis/Adrastea analytical orbit
markers nearly superimposed.

---

## Still parked (unchanged from before)

- **Codebase-wide white->red orbit-marker switch** (Keplerian / mean /
  actual orbit info markers). Tony's call this session: leave as-is.
  These are the last white-border holdouts among orbit markers; the
  switch is a deliberate visual change across the whole orrery, not
  done. The osculating marker is intentionally NOT part of this (it's
  white by Tony's May 29 decision).
- **Shell consolidation Phases B-D** (the larger track v12-v14 was
  about). Untouched this session.
- **Phase 2 dead-code sweep** (honest-shell-files): the inert sphere-
  shell inline marker conversions from earlier sessions, plus the
  Roche duplicate/uncalled function above.

---

## State of deliverables

Four files in outputs, ready to deploy:
- `shell_configs.py`
- `asteroid_belt_visualization_shells.py`
- `mars_visualization_shells.py`
- `idealized_orbits.py`

Plus the test protocol (`border_refinement_test_protocol.md`) -- run
and passed, results captured. Exit decision: ALL PASS.

All four pass the agentic pre-test gates: py_compile clean, zero
non-ASCII, LF preserved, diffed against upload base (changes contained
to the intended regions only). Tony has NOT yet done the Windows-side
visual confirm at deploy; the MAPS plot screenshot confirms the
osculating marker renders and separates correctly.

---

## Lessons for the Archive

(v14 Lessons 1-7 stand. Added:)

### Lesson 8 [CRITICAL]: A marker can be written and never render

The osculating info marker existed in code for ~11 weeks but referenced
an undefined variable; the NameError was swallowed by the caller's
try/except, so the arc rendered and the marker silently didn't. "The
code is there" is not "the code runs." This is the inverse of v14's
dead-code lesson: there it was a live function on a dead path; here
it's a dead variable on a live path. Both produce "looks converted /
looks coded but does nothing." The tell, again, was Tony's eyes ("no
marker at all"), not the code reading as correct. A swallowed exception
in a try/except is where a render bug hides -- check the console for
the caught-error print.

### Lesson 9 [QUALITY]: Assign, don't hardcode, to stay in the pattern

The fix could have hardcoded `color='white'` in the marker dict.
Defining `color = 'white'` once and referencing it (line + marker
fill) matches every other orbit function and makes a future restyle a
one-line change. Tony caught this and asked for the variable. The more
maintainable fix was also the one closer to the original author's
intent (the marker already said `color=color` -- the variable was just
never defined).

### Lesson 10 [QUALITY]: The plot overrides the code's apparent structure

Twice this session a mental model built from reading the code was wrong
about which markers were involved, and the plot (or Tony's correction)
overrode it. The Keplerian info cross turned out to be near-aphelion
and generic, not near-perihelion and comet-specific. When reasoning
about what a marker collides with, get the hover labels from the actual
plot before designing the fix -- don't theorize marker identities from
code alone. (Direct continuation of v14 Lesson 6: map the dispatch /
read the plot before editing the leaves.)

### Lesson 11 [PRACTICE]: Fixing an invisible thing surfaces its neighbors

The osculating marker collisions were always latent -- you can't see a
marker collide with its neighbor when it isn't rendering. Making it
visible revealed a clutter problem that predates this session. Worth
expecting: when you fix a "nothing renders" bug, budget for "now I can
see it's too close to its neighbors" as the immediate follow-on.

---

## Next-session opener (concrete)

1. Deploy the four files (Windows-side visual confirm if not yet done).
2. If picking up comet clutter: hover the overlapping markers on
   ikeya_seki, read the labels, THEN design the separation. Candidate
   approaches discussed: deliberately place colliding markers on
   opposite sides of perihelion, or different arc fractions -- but
   confirm participants first.
3. Phase 2 dead-code sweep if desired (Roche duplicate + uncalled
   function + the inert inline sphere-shell conversions from earlier
   sessions).
4. The larger shell-consolidation track (Phases B-D) remains the
   strategic line; this session was a border/marker refinement detour
   that closed out Phase 1 testing.

---

*"Tony's eyes win" -- again. This session they caught that a marker*
*had never rendered in 11 weeks, that 2q sat too close to its*
*neighbors, and that two of Claude's marker-identity models were*
*wrong. The plot is the ground truth; the code's apparent structure*
*is not.*

*Handoff written: May 29, 2026 with Anthropic's Claude Opus 4.8*
