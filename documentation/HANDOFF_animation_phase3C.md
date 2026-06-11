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

Module updated: June 2026 with Anthropic's Claude Fable 5
