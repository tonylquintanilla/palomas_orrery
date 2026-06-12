# HANDOFF -- Animation Refactor 21/51, Phase 3 Session C (June 11, 2026)

Built on: orrery repo HEAD 0ce1e26a0a878c9bfa080e58d2aa114756530d14 (verified;
matches the SHA Tony supplied; Session B at this base).
Deliverables (6 patched files + docs): palomas_orrery.py, shell_configs.py,
comet_visualization_shells.py, shared_utilities.py,
uranus_visualization_shells.py, neptune_visualization_shells.py,
ANIMATION_TEST_PROTOCOL_v4.md, six diff files vs HEAD.

Scope per the GO: the five engine items + the one-line auto-scale (Tony's
call: in Session C, since the infrastructure exists; everything else
scaling lives in item 19; no "Session D" framing).

## What changed

1. BARYCENTER SUN-DIRECTION FIX (B3-bonus). Root cause was a sentinel
   conflation: (0,0,0) means "skip rotation" to shell-orientation code but
   reads as a literal position to the indicator. The engine now has its own
   Sun contract: positions_over_time['Sun'] -> engine-fetched Sun trajectory
   when the checkbox is off (one Horizons call per frame, announced) ->
   SUPPRESSION with a console note when the fetch fails. The engine never
   points at a placeholder position. Bonus: with the fetched trajectory,
   non-center indicators track the REAL Sun per frame even when the Sun
   checkbox is off -- the frozen-orientation caveat for that case is gone.

2. CONSOLE SPAM (O13a). Engine rebuilds run under stdout redirection;
   builder messages ("Sun direction indicator: Using shell radius...",
   "[COMET VIZ] ...") print once at allocation as the per-element record.
   No builder files touched for this.

3. COMET TAILS PER FRAME, OPT-IN. New Animation Settings checkbox
   ("Animate comet tails (rebuild each frame)"), default OFF per O1.
   - build_comet_tail_traces: a CAPTURE SHIM -- runs the existing 240-line
     fig-mutating builder on a private figure and returns its traces.
     Faithful by construction (live-verified trace-for-trace at 0.5 and
     8.0 AU); the hairy builder is unchanged.
   - VARIABLE-COUNT handling (live-measured: counts are 9/7/5/6 across
     distances and NON-monotonic): allocation probes every frame's count
     (quiet) and allocates the max; every rebuild pads to the slot count
     with invisible dummies; exceeding the allocation fails LOUD (max-probe
     missed a case). Design rule 2(a) implemented as padding -- zero
     builder changes.
   - MAPS excluded from per-frame mode (date-gated disintegration +
     fig-coupled ghost tail stay frame-1), disclosed in the tooltip.

4. SODIUM TAIL as engine customer. CUSTOM_SHELLS tag (14 per_frame tags
   now) + CHECKBOX GATING in collect: an element with its own checkbox
   (mercury_sodium_tail) animates only when THAT box is on; axis/cone
   keep the any-shell-checked trigger. Greyed placeholders SKIP elements
   the engine animates -- no "(static plots only)" lie next to a live tail.

5. HOVER DISCLOSURE (the D.Movement bow-shock remainder). Uranus + Neptune
   bow-shock hovers gain: "Conic-section MODEL: standoff distance is
   sourced; the flank shape is schematic (eccentricity 1.05, illustrative).
   In animations the shock is fixed at the animation start." Anchored
   byte-replaces with count asserts; Source lines and AU/km values
   untouched. The indicator hover (ONE central site, shared_utilities)
   gains the center-frozen / non-center-tracking line.

6. ONE-LINE AUTO-SCALE. Under Auto, after get_animation_axis_range, the
   cube becomes the LARGER of orbital and center-shell extents -- never
   shell extent alone (a naive wiring would have imported the Finding-1
   photosphere collapse into animations). _shell_axis_range is non-None
   only under Auto with shells, so manual scale is never overridden. The
   2c "intentionally unused" annotation is updated; the section-G
   dead-auto-scale question CLOSES.

## Verification done (Claude-side)

- py_compile clean (all 6); ASCII-only in all edit regions (3 pre-existing
  em-dash lines in comet_visualization_shells MAPS strings noted below);
  LF; diffs confined (388 diff lines across 6 files); sed swap on a
  throwaway copy.
- LIVE tests in the real module namespace under xvfb:
  T1 shim equivalence: trace-for-trace identical to the fig path at 0.5
     and 8.0 AU.
  T2 gating: comet spec appears only with the opt-in; sodium requires ITS
     checkbox; axis rides any-checked.
  T3 max-probe: a synthetic comet sweeping 8.0 -> 0.5 AU (crossing every
     threshold) allocates 9 slots = max over the NON-monotonic per-frame
     counts [6,6,5,4,9,9].
  T4 padding holds at every frame.
  T5 barycenter fix, geometrically: with sun trajectory None, sun-needing
     elements suppressed (note printed) while the axis survives; with a
     real trajectory, the indicator's first segment points at the REAL Sun
     (cosine > 0.999), not the origin.
  T6 quiet rebuild: zero stdout.
  T7 placeholder skip: engine-animated sodium has NO static-only entry;
     magnetosphere still placeheld.
- NOT tested in-container: the auto-scale max() under live animation
  (3-line wiring; C6 covers), Horizons-backed runs, render quality.

## Ledger-ready updates

- 21/51 Session C DELIVERED `[render-gated on protocol v4]`. On pass, the
  Phase 3 CORE TRACK (A/B/C) is COMPLETE: engine + axis/cone/indicator +
  sodium + opt-in comet tails + disclosures + auto-scale line.
- D.Movement bow-shock disclosure remainder: CLOSED (U+N hovers carry the
  conic + freeze disclosure; the Phase-1 orientation-freeze rider and the
  frame-1 rider are folded into the same lines). `[render-gated C5]`
- Section G dead-auto-scale question: CLOSED (max(orbital, shell) under
  Auto; Finding-1 inverse asserted in C6).
- B3-bonus barycenter bug: FIXED `[render-gated C1]`. Lesson for the
  archive: a fallback value is a CONTRACT -- (0,0,0) was a rotation-skip
  sentinel for one consumer and literal data to another; reusing a
  fallback without checking each consumer's semantics is how a sentinel
  becomes a physics bug. Suppression beats fabrication (envelope
  principle, geometric form).
- O13a console spam: FIXED engine-side (stdout redirection at rebuild);
  no builder edits.
- ITEM 19 fixture list (per Tony's framing call) now carries: photosphere
  auto-scale collapse (static), Sun-Direction indicator cube truncation,
  Fly-To zoom limit vs shell extent, Sun-orbit-around-center buffer,
  camera tracking across frames (mechanism note: go.Frame(layout=...) can
  carry scene.camera per frame -- implementable in existing machinery,
  needs a user-interaction toggle), plus O16's incoming auto-scale
  observations.
- Remaining riders (unchanged): resolution-sweep follow-on (gate 5(b)
  Mode-5 quality at reduced density; 5(a) bytes already passed);
  measure_animation_html.py file-browser dialog; D.Cosmetic ASCII note --
  3 pre-existing em-dash lines in comet_visualization_shells.py MAPS
  strings (L257/505/519) violate the ASCII-only convention; joins the
  next touch of that file.

## Session C Test Results (June 11, 2026 -- Tony, Mode 5)

Tested at HEAD d9460e22cd41b9da344930bbbac53dba8ed63d7c, pushed as
02cce781dda18cc099a676b682d908b4f6fb556f. Six items verified on Windows,
Python 3.13.

### C1 -- Barycenter fix
- PASS (Earth-centered). Console prints "Sun checkbox off -- fetching
  Sun trajectory..." Earth's Sun Direction indicator points at the Sun
  and tracks it across frames. Verified by comparison with Sun-checked
  run. Sun-centered verification limited by Fly To zoom (known item 49).

### C2 -- Comet tails per frame (Ikeya-Seki perihelion)
- ISSUES FOUND. Opt-in checked, hourly frames starting 10/20/1965 04:24
  (one day before perihelion). File size 2426 KB with opt-in.
  (a) FRAME-1 DOUBLING: Original frame-1 traces remain visible alongside
      per-frame rebuilt traces. Nucleus and Sun Direction indicator appear
      twice -- both the frame-1 original and the engine rebuild. Legend
      entries double. The engine is adding traces alongside existing ones
      instead of replacing them.
  (b) PERIHELION BEHAVIOR MISMATCH: No tail visible at perihelion in
      animation, but static plot (same dates, Go button) shows tail at
      perihelion (see uploaded screenshot). The capture shim may not be
      equivalent to the static builder at all distance thresholds, or
      the variable-count padding has edge cases at threshold crossings.
  (c) SUN DIRECTION INDICATOR DISAPPEARS: Present at 04:24, moves at
      05:24, absent from 18:24 onward. May be related to the per-frame
      engine's sun-direction suppression logic at close approach.
  (d) Opt-in UNCHECKED: frame-1 tails only (regression correct).
  (e) Fly To flies only to frame 1 (known item 49).

### C3 -- Sodium tail rides Mercury
- PASS. Tail rides Mercury per frame pointing anti-sunward. No greyed
  "static plots only" entry. Other Mercury shells greyed correctly.

### C4 -- Console spam
- See output. Builder messages appear to print once at allocation (the
  heavy output makes visual confirmation difficult -- same disclosure
  class as O2/O3).

### C5 -- Hover disclosures
- PASS. Uranus-centered bow-shock hover shows conic-model note + freeze
  line. Sun-centered sun-direction indicator hover correct. Same Fly To
  zoom limitations as previous sessions.

### C6 -- Auto-scale
- PARTIAL PASS with findings.
  (a) Sun-centered, inner planets + corona, Auto: cube holds orbits
      correctly (orbital extent wins). PASS.
  (b) Solar shell hovertext uses <br> instead of \n for line breaks.
      Cosmetic issue.
  (c) Sodium tail tracks the Sun correctly in Sun-centered view.
  (d) MERCURY-CENTERED BUG: Sun Direction indicator and sodium tail do
      NOT track the Sun when Mercury is the center body. Same class as
      the barycenter bug -- the engine's Sun trajectory resolution may
      not cover the case where a non-barycenter planet is centered and
      the Sun checkbox is off. The barycenter fix resolved the
      barycenter case but this planet-centered case may have been missed.

### C7 -- Regression
- B1-style Uranus run unchanged. No-shells animation matches Phase 1/2.
  Static plots with U/N magnetosphere render unchanged except new hover
  lines.

### Observation Log v4 (O14-O17)

O14 -- Comet tail visual quality: The threshold crossings produce
discontinuous behavior -- tail disappears at perihelion, coma appears
then disappears. The static builder produces a richer perihelion render.
The variable-count handling may be losing features at threshold
boundaries. Worth investigating whether the capture shim's distance-
based feature activation matches the static builder's.

O15 -- Sodium tail at 500 particles per frame: acceptable quality.

O16 -- Auto-scale max() behavior: Sun-centered correct. Mercury-centered
sun-tracking bug found (C6d).

O17 -- Free-form:
(a) Frame-1 trace doubling (C2a) is the most significant visual defect.
(b) Mercury-centered sun-tracking (C6d) is a real physics bug.
(c) Solar shell hovertext <br> vs \n (C6b) is cosmetic.

### Session C Disposition

Session C NOT YET CONFIRMED. Three issues require attention before the
Phase 3 core track can close:

1. FRAME-1 DOUBLING (C2a): Per-frame engine adds traces alongside
   frame-1 originals instead of replacing them. Visual and legend
   duplicates. Needs a fix.
2. PERIHELION BEHAVIOR MISMATCH (C2b): Animation comet tail differs
   from static at perihelion. May be a capture shim equivalence issue
   or a threshold-boundary edge case.
3. MERCURY-CENTERED SUN TRACKING (C6d): Sun Direction indicator and
   sodium tail don't track Sun when Mercury is center. Same bug class
   as the barycenter fix, different trigger.

Items 1 and 3 are likely small fixes (the doubling is probably a missed
cleanup of frame-1 traces when the engine allocates; the Mercury case
is likely the Sun trajectory fetch not triggering for planet centers).
Item 2 may require deeper investigation of the capture shim's distance
thresholds vs the static builder.

### New Ledger Items (promote from handoffs)

- **Directional arrow camera controls for 3D Plotly**: Currently
  available in Gallery Studio for 2D (D-pad pan arrows) but not for
  Plotly 3D. Would enable precise camera positioning without mouse,
  improving shell-scale visual verification. Add to item 19's
  comprehensive review. (First mentioned in Phase 3B handoff L183.)
- **Camera tracking across animation frames**: Plotly frames can carry
  layout updates including scene.camera (go.Frame(layout=...)). A
  camera-follows-body toggle would close the B1/B2 verification gap at
  outer-planet scales. Needs user-interaction toggle (frame-driven
  camera fights user orbit/zoom). Tooling session, item 19 adjacent.
  (First mentioned in Fable 5's Session C scope response.)
- **Solar shell hovertext uses `<br>` instead of `\n`**: Cosmetic issue
  found in C6 testing. D.Cosmetic class.
- **`[KEPLERIAN POS] Could not parse epoch date` with "osc." suffix**:
  Appears in EVERY console run for every planet. The epoch date parser
  cannot handle the "osc." suffix appended to osculating element epoch
  strings (e.g., "2026-06-10 12:32 osc."). Silently prevents Keplerian
  position calculation for every body with osculating elements. Pre-
  existing, not a regression from any Phase. Functional gap — the parser
  should strip or handle the suffix. D.Priority or D.Structural class.

### V4 Gate Blocking Items (for Fable 5 fix pass)

Three bugs must be resolved before the Phase 3 core track can close:

1. **C2a — Frame-1 trace doubling**: Per-frame engine adds comet traces
   alongside existing frame-1 comet traces instead of replacing them.
   Creates visual and legend duplicates (nucleus, sun direction indicator
   appear twice). D.Priority.

2. **C2b — Perihelion behavior mismatch**: Animation comet tail behavior
   at perihelion differs from static plot (no tail at perihelion in
   animation; static shows tail). May be a capture shim equivalence issue
   at distance-threshold boundaries, or variable-count padding edge case.
   D.Priority.

3. **C6d — Mercury-centered Sun tracking**: Sun Direction indicator and
   sodium tail do not track the Sun when Mercury is the center body and
   the Sun checkbox is off. Same bug class as the B3-bonus barycenter fix
   (sentinel conflation) but the Session C fix apparently did not cover
   non-barycenter planet centers. D.Priority.

Module updated: June 2026 with Anthropic's Claude Fable 5 + Claude Sonnet 4.6
