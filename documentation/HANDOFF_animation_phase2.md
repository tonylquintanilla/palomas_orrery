# HANDOFF -- Animation Refactor 21/51, Phase 2 (June 10, 2026)

Built on: orrery repo HEAD 3f03c122d85dc4bbeccf69d74faeb5893c914152 (verified
via git ls-remote at session start; matches the SHA Tony supplied; Phase 1
edits confirmed present at this base).
Deliverables: palomas_orrery.py (patched), phase2_diff.txt (review diff vs
HEAD). No other files touched.

Implements the four approved steps (2a-2d) from the June-10 design decisions,
including the params-flag resolution. All decision points honored: canon =
add_celestial_object; helpers in-file near add_celestial_object; offset-Sun
and non-center shells untouched (Phase 3 fence).

## What changed (10 diff hunks, net -36 lines: ~210 duplicated lines removed,
~174 helper lines added)

NEW HELPERS (inserted after add_celestial_object, ~L1862-2035):
- get_planet_shell_vars_map() [2d] -- replaces THREE per-pipeline dict copies
  (planet_shells_config + planet_shell_vars in static, animation_shell_config
  in animate). New shelled bodies are added once, here.
- resolve_shell_sun_position() [2b] -- the one sun-position producer.
  Static passes positions.get('Sun'); animate passes the frame-1 entry.
  Fallback Horizons fetch when the Sun checkbox is off, as before.
- add_center_body_marker() [2a] -- the canonical center marker. Routes
  through add_celestial_object (full hover, RA/Dec, CENTER_MARKER_SIZE);
  transparent center colors suppress the legend entry (preserves the old
  explicit-block barycenter behavior).
- add_center_body_shells() [2c] -- the one center-shell dispatch (Sun branch
  + belts + planet branch + Auto shell scaling). log_prefix parameterizes
  the console tag: '' (static, silent as before), '[ANIMATION] ' (animate,
  matching the test-protocol console lines).

SIGNATURE EXTENSION (~L1786-1858): add_celestial_object gains optional
params=None (osculating elements for hover; defaults to module
planetary_params -- behavior-preserving for any external caller) and
show_legend=True. The ONE existing call site (static object loop, ~L5064)
now passes params=active_planetary_params -- so ALL static markers' hover,
center included, now uses fresh osculating elements (the params-flag
resolution; previously they silently used the stale module dict).

STATIC plot_objects:
- Dispatch region (~4663-4684): sun-position block + Sun/planet shell
  branches collapse to resolve_shell_sun_position + add_center_body_shells.
  _sun_pos_tuple keeps its name (the comet-tails section reuses it).
  axis_range return is LIVE here (Auto shell scaling preserved).
- Explicit center-marker block DELETED (~4686, breadcrumb comment left).
  The object loop is the static canon. ** This kills ledger N3 ** (two
  origin markers when body checked + centered + no shells).

ANIMATE animate_objects:
- Phase-1 sun-position block (~6211) collapses to resolve_shell_sun_position
  (same semantics, one producer). Phase 1's frame-fence and first-frame-sync
  edits are UNTOUCHED (verified intact post-edit).
- Dispatch (~6229) collapses to add_center_body_shells. The returned
  axis_range is intentionally UNUSED and annotated: get_animation_axis_range
  recomputes it unconditionally downstream, so the shell auto-scale was
  ALREADY dead in animate (new ledger note below). Behavior preserved, not
  silently fixed.
- add_center_body_marker call placed BEFORE the fence (~6239), unconditional.
  ** This kills O6(a) ** (no center marker with shells on) ** and O5 **
  (bare hover) -- animate's center marker is now pixel-identical in
  mechanism to static's.
- Explicit center-marker block DELETED; animation_shell_config DELETED.

## Verification done (Claude-side)

- py_compile clean; ASCII-only; LF; 10 hunks all in intended regions;
  Phase-1 fence + sync code verified intact.
- FULL module execution under xvfb (GUI built end-to-end, mainloop
  suppressed, clean shutdown) -- this is the startup test and more.
- LIVE-DISPATCH tests inside the real module namespace (real tk vars, real
  builders; only the two network calls patched):
  T1 shared map: 12 bodies, live tk.IntVars.
  T2 sun producer: Sun-center, passthrough, and fetch-fallback branches.
  T3 EQUIVALENCE: add_center_body_shells output is trace-for-trace
     IDENTICAL (names + coordinates) to the direct create_planet_visualization
     call it replaced (Earth + magnetosphere, 16 traces); Auto axis_range
     returned correctly.
  T4 Sun-center branch: sphere shell + main belt dispatch (10 traces).
  T5 center marker: origin, CENTER_MARKER_SIZE, full 359-char hover (not
     bare name), transparency suppresses legend.
- The sed display swap ran on a THROWAWAY copy only (Phase-1 lesson applied);
  the deliverable was never sed-touched.
- NOT verifiable in-container: live RA/Dec fetch inside the marker hover and
  full animation runs (Horizons unreachable). Mode-5 checklist below.

## Mode-5 checklist (Phase 2 render gate)

Static:
  [ ] Body checked + centered + NO shells: exactly ONE origin marker
      (N3 was the double -- confirm it is gone; legend shows one entry).
  [ ] Center marker hover unchanged from what you know (object-loop render).
  [ ] Sun-centered, no shells: single Sun marker, hover from the full
      formatter (the old hover_text_sun block is gone -- content may read
      slightly differently; judge).
  [ ] One shells-on static plot: unchanged vs pre-patch (T3 equivalence
      says identical; confirm by eye).
Animate:
  [ ] P3-style run (Earth center, magnetosphere, Moon): center marker NOW
      RENDERS with shells on (new pixels -- the O6a fix), full hover on it.
  [ ] Marker is constant across frames (not in trace_indices; console
      "Static shell traces" count includes it now -- one higher than before).
  [ ] Re-run one P1-style measurement: frames payload unchanged from
      Phase 1 numbers (fence untouched).
  [ ] Barycenter-centered animation (e.g. Pluto-Charon): transparent center
      suppresses the legend entry, marker behavior sane.
Cosmetic observation (pre-existing, now visible in animate too): the center
marker's hover includes "Distance to Center Surface: -6378 km (below mean
datum)" style lines -- the formatter treats the center like any object at
distance 0. Static has always shown this; animate now matches. If it grates,
it is a formatter polish item (ledger candidate), not a Phase 2 defect.

## Ledger-ready updates

- CLOSE (render-gated on the checklist above): N3 (center-marker edge case,
  double origin markers) -- root cause was two mechanisms; second mechanism
  removed. O5 and O6(a) (from the Phase-1 observation log) -- animate now
  uses the canonical marker.
- D.Structural 5 (_info import cleanup): hover_text_sun import (L208) is now
  UNUSED (its only consumer was the deleted static explicit block). Joins
  the existing import-cleanup sweep; deliberately not removed solo.
- NEW note (animate scaling): the shell auto-scale (axis_range from
  _shell_outermost_radius_au) is DEAD in animate -- get_animation_axis_range
  unconditionally recomputes axis_range downstream and does not read the
  shell radius. Pre-existing (Tony's P2/P3 render-approved the current
  scaling); now annotated at the call site. DECISION FOR LATER: should
  animation Auto scale consider shell extent? If yes, it is a one-line use
  of the helper's returned axis_range, gated on Mode-5.
- NEW cosmetic candidate: center-body hover "distance to own surface"
  lines (formatter treats center as object-at-zero). Pre-existing in static.
- 21/51: Phase 2 (2a-2d) DELIVERED, render-gated. Remaining in track:
  Phase 3 (non-center/offset-Sun/moving shells -- tier decision pending) and
  the comet-tail opt-in mode. D.Structural 3 (create_planet_visualization
  wrapper retirement) is NOT yet absorbed: the wrapper is still the live
  planet-branch entry inside add_center_body_shells; retiring it is now a
  ONE-SITE change (swap to create_celestial_body_visualization with
  center_object threading) -- a clean Phase 2.5 or Phase 3 rider.

## Next session

- Tony: run the Mode-5 checklist, push, carry the new SHA, apply ledger
  updates.
- Then: Phase 3 tier decision (the three-tier design from the Phase-1
  handoff), and optionally the wrapper-retirement rider (D.Structural 3).

## Phase 2 Test Results (June 10, 2026 -- Tony, Mode 5)

Tested at HEAD 6a0ac2808f3b167e3fa5bebe0bdd5ca16f063591. All four steps
verified on Windows, Python 3.13.

### P2-1 -- Static, N3 single-marker check
- PASS. One marker, one legend entry, full formatter hover. INFO icon works.

### P2-2 -- Static, Sun-centered, no shells
- PASS. Single Sun marker. Full formatter hover serves.

### P2-3 -- Static, shells-on regression
- PASS. Unchanged from pre-patch. Center marker present. Auto-scale correct.

### P2-4 -- Static, osculating hover spot-check
- FINDING. Keplerian Orbit hover said "averaged orbital elements" but orbits
  use osculating elements. Pre-existing labeling error in idealized_orbits.py
  get_planet_perturbation_note(). FIX APPLIED (Claude Sonnet, same session):
  10 instances corrected to "osculating (instantaneous) elements at epoch."

### P2-5 -- Animate, O6a/O5 headline (new pixels)
- PASS. Center marker renders with shells on. Full hover. Constant across
  frames. Static shell traces: 17 (one higher than Phase 1 P3). Magnetotail
  + Sun Direction unchanged.

### P2-6 -- Animate, no shells
- PASS. Full formatter hover (not bare name).

### P2-7 -- Animate, barycenter transparency
- TEST DESCRIPTION CORRECTED. Barycenters correctly render as open squares
  with full hover and legend entries (not transparent/suppressed as the
  checklist expected). Pluto-Charon Barycenter centered: open square, full
  hover, legend entry. Earth-Moon Barycenter in Earth-centered animation:
  same. Both CORRECT as rendered.

### P2-8 -- Frame-payload regression
- Deferred. Fence untouched; console counts match expectations.

### P2-9 -- Console lines
- PASS. "[ANIMATION] Added Earth shells (16 static traces)" prints from
  shared helper. Frame-updated/excluded counts print in expected form.

### Observation Log v2 (O7-O9)

O7 -- "Below mean datum" hover: acceptable and informative. No promotion.
O8 -- Sun hover (new full-formatter vs old custom): acceptable.
O9 -- Keplerian orbit hover labeling error found and fixed (P2-4).
      palomas_orrery.py docstring authorship updated.

### Additional Fixes (Claude Sonnet, June 10, 2026)

1. idealized_orbits.py: 10 instances of "averaged orbital elements" changed
   to "osculating (instantaneous) elements at epoch" in
   get_planet_perturbation_note(). Pre-existing factual error, not introduced
   by Phase 2. py_compile clean, ASCII-only. Credit line added.

2. palomas_orrery.py: docstring authorship updated to "June 10, 2026 with
   Anthropic's Claude Fable 5, Claude Sonnet 4.6, and Tony."

### Phase 2 Disposition

Phase 2 RENDER-CONFIRMED. N3, O5, O6(a) all resolved. No regressions.
P2-7 test description corrected (barycenters render correctly as-is).
Osculating hover labeling fixed separately (pre-existing, one file).

### Ledger-Ready Updates (apply to LEDGER_orrery_consolidated.md)

- Move N3, O5, O6(a) to section C (DONE).
- 21/51: Phase 2 RENDER-CONFIRMED. Phase 2.5 (wrapper retirement) and
  Phase 3 (tier decision) remain open.
- New DONE: osculating hover labeling fix (idealized_orbits.py, 10 text
  corrections in get_planet_perturbation_note).
- New DONE: palomas_orrery.py authorship update.
- Queued (section G): animation auto-scale-vs-shells decision; Phase 3
  tier decision; optional Phase 2.5 wrapper retirement.
- New SHA after push carries: Phase 2 helpers (6a0ac28 base) + osculating
  label fix + authorship update.

## Phase 3 Design Decisions (June 10, 2026 -- Tony + Claude Sonnet)

Tony reviewed Fable 5's Phase 3 scope proposal with Claude Sonnet's
interpretation assist. Five decision points addressed. Fable 5's opinion
sought on undetermined elements and open design questions before convergence.

### Decision 1: Tier 2 committed

YES. Tier 2 (per-frame re-emission of small primitives) is the committed
direction. Tiers 1 and 3 are not parked outright but reframed:

- Tier 1 (static-at-frame-1) remains the default for large geometry (sphere
  shells) -- this is how they already behave post-Phase-1. The honesty
  problem Fable 5 identified (Moon vs Uranus drift rates) is real and should
  be disclosed, not suppressed.
- Tier 3 (full shell re-emission) is reframed as "reduced-resolution
  per-frame re-emission" -- a measured follow-on to tier 2, not a separate
  tier. See Decision 5.

Explicit trace inventory for the per-frame engine:

PER-FRAME (small primitives, orientation/position-dependent):
  - Rotation axis lines (auto-triggered with center body shells, no checkbox)
  - Dipole cone
  - Sun direction indicator + line
  - Comet tails (opt-in mode, second engine customer)

FRAME-1-ONLY (large geometry, static after initial render):
  - All sphere shells (magnetosphere, bow shock, radiation belts, corona
    layers, photosphere mesh, core, etc.)
  - With reduced-resolution per-frame as a measured follow-on (Decision 5)

NOTE: The rotation axis is not checkbox-controlled -- it is automatically
added when the center body shell dispatch fires. This simplifies the
per-frame engine: it is always present when shells are on, no conditional
UI gating needed.

QUESTION FOR FABLE 5: Is this trace inventory complete? Are there other
small primitives or orientation-dependent elements that should be in the
per-frame category? What about the info markers that ride on shells --
should those move with a non-center body or stay at frame-1 position?

### Decision 2: Console notice for 3a

Console notice for the O2/O3 no-ops, not UI greying. The greying-out
approach (similar to Gallery Studio's preset mode) has a fundamental
sequencing problem: checkboxes are selected BEFORE the animation button
is clicked, so there is no animation-context moment to grey them out.
A proper solution would require rethinking the flow:

  animation checkbox --> context-aware checkboxes --> animation button

This is significant GUI surgery that should not be designed before the
per-frame engine settles, because the engine determines which elements
are per-frame vs static vs unavailable -- and that fence may move as
the engine matures.

For now: console notice + disclosure in the rendered output (title or
annotation) indicating which elements are per-frame animated vs frame-1
frozen. The user sees everything they checked rendered; the disclosure
tells them which moves and which is frozen. Honest without restrictive.

QUESTION FOR FABLE 5: What is the right disclosure mechanism in the
rendered HTML? A subtitle annotation? A hover-accessible note? Something
in the legend? What have you seen work in Plotly for this kind of
per-element status disclosure without cluttering the visualization?

### Decision 3: Auto-scale through consolidated pipeline

Auto-scale should NOT be a standalone 3a one-line patch. It should ride
the consolidated pipeline in 3b, where the engine knows what is rendered
and the scale calculation accounts for it naturally. A one-line patch on
the current animate path risks being overwritten or creating a second
scaling mechanism when the pipeline consolidation lands.

QUESTION FOR FABLE 5: Does this change your 3a scope? If auto-scale
moves to 3b, what remains in 3a beyond the console notice and the
wrapper retirement?

### Decision 4: Comet tails in 3b first cut

YES. Include comet tails as the second customer of the per-frame engine.
This validates the engine's generality -- if it can handle both rotation
primitives (orientation-dependent, position-fixed) AND comet tails
(position-dependent, builder-generated), the architecture is proven.
If deferred, 3b ships as a single-customer engine and the generality
claim is untested.

QUESTION FOR FABLE 5: The current comet tail builder generates the tail
geometry from a position + anti-sunward direction. In the per-frame
engine, would the tail be rebuilt from scratch each frame (calling the
builder with the new position), or would the frame-1 tail geometry be
translated/rotated to the new position? The former is more honest
physically (tail direction changes as the comet moves relative to the
Sun); the latter is cheaper. What is your recommendation?

### Decision 5: Element fence -- first cut + measured follow-on

First cut = small primitives only: rotation axis, dipole cone, sun
direction indicator, comet tails. These are geometrically light and the
per-frame cost is known to be negligible.

Second cut = reduced-resolution sphere shells (bow shock, magnetosphere),
GATED on two measurements before committing:
  (a) Byte budget: Fable 5 measures what a 4x-reduced magnetosphere costs
      per frame and confirms 29 frames stays within the Phase-1 savings.
  (b) Render quality: Tony reviews the reduced-resolution shell in Mode 5
      and judges whether it serves educationally at the lower fidelity.

This is a tier 2 + tier 3 hybrid: frame 1 gets full-resolution shells,
subsequent frames get simplified versions. Architecturally this means the
shell builders need a "resolution mode" parameter -- real design work, but
it keeps the door open rather than parking tier 3 permanently.

Tony's instinct: anything pertaining to the planet or Sun's orientation
should move per-frame (rotation axis, comet tails, sun direction). Bow
shock and magnetosphere are desirable but the byte cost must be measured
first. The educational value of seeing the magnetotail sweep as Earth
orbits is high -- this is worth pursuing if the budget allows.

QUESTION FOR FABLE 5: What is your estimate of the design work for
resolution-mode shell builders? Is this a parameter addition to
build_sphere_shell (e.g., n_points=400 default, n_points=100 for
per-frame), or does it require a different builder architecture? And
for the magnetosphere specifically (CUSTOM_SHELLS, not sphere shells),
what would "reduced resolution" look like?

### Proposed 3a/3b split (for Fable 5's review)

3a (surgical, independently shippable):
  - O2/O3 console notices for non-center/offset-Sun shell no-ops
  - Phase 2.5 wrapper retirement (one site)
  - No auto-scale patch (deferred to 3b)

3b (the engine, multi-session, design-before-code):
  - Per-frame primitive registry and frame-loop extension
  - First customers: rotation axis + dipole cone + sun direction + info
    markers on non-center bodies
  - Second customer: comet tails (opt-in)
  - Auto-scale through consolidated pipeline
  - Measured follow-on: reduced-resolution shells if budget allows

QUESTION FOR FABLE 5: Does this split make sense? Is 3a worth shipping
independently, or should it just fold into 3b's first session? And what
is your estimate of the session count for 3b -- is this a two-session
or three-session effort?

Module updated: June 2026 with Anthropic's Claude Fable 5 + Claude Sonnet 4.6
