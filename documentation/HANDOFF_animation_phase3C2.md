# HANDOFF -- Animation Refactor 21/51, Fix Pass C2 (June 11, 2026)

Built on: orrery repo HEAD d05f0f1d3e63287494bad93b7a8ccc1cddfa608d
(verified; the 3C handoff with Tony's v4 results at this base).
Deliverables (2 patched files + docs): palomas_orrery.py,
planet_visualization.py, ANIMATION_TEST_PROTOCOL_v4_1.md, the updated
LEDGER_orrery_consolidated.md, two diff files vs HEAD (245 diff lines).

All three v4 blockers are root-caused with reproduction -- none was
patched on a guess. The blocking trio turned out to be three DIFFERENT
diseases that happened to present together in the C2 run.

## Root cause 1 (C2b + C2c): the sticky-visible frame merge

The perihelion reproduction EXONERATED the engine math: a synthetic
sungrazer sweep (0.30 -> 0.008 -> 0.27 AU) through the engine's exact
rebuild path produces the full tail at perihelion (9 traces, 0.75 AU
extent). The bug is Plotly frame MECHANICS: frame traces are applied as a
MERGE onto the slot's current state, and builders omit 'visible' from
their JSON (verified: zero of the comet builder's 9 traces serialize a
visible property). So a slot once occupied by a visible=False padding
dummy NEVER REVIVED -- the omitted property inherited False forever.

That one mechanism explains both symptoms exactly: trace counts swing
(3 -> 9 -> 3) across the sweep, so the tails materialize into
previously-dummied slots precisely at perihelion (C2b: no tail at
perihelion, static fine), and the indicator reshuffles into a dead slot
the moment counts grow as the comet enters its activity window (C2c:
present 04:24, gone from 18:24 on). O14's "coma appears then disappears"
is the same slot shuffle.

FIX: `_normalize_perframe_visibility()` -- every trace written into a
frame slot carries an EXPLICIT visible (unset -> True; builder-set values
like 'legendonly' preserved), applied at allocation and at every rebuild.
The missing-position branch now writes explicit invisible dummies
(`_perframe_dummy_trace()`) instead of mutating copies -- same trap, same
fix -- and prints a one-shot console NOTE naming the body (it was a
silent blanking before; silent fallbacks are how render bugs hide).

LESSON (archive-grade): Plotly frame updates are merges -- any property a
builder omits inherits the slot's history. Padding slots with invisible
dummies REQUIRES explicit visibility on every subsequent write.

## Root cause 2 (C2a): two producers of one element

The pre-existing frame-1 comet-tail block in animate AND the engine's
allocation both added the comet's traces -- including the builder's OWN
Sun Direction trace, which is why the indicator doubled too. The engine's
allocation IS frame-1 content by design; the old block just didn't know.

FIX: the frame-1 block skips engine-owned comets (opt-in checked,
non-MAPS), with a console line saying so. MAPS still gets frame-1 tails
there (excluded from per-frame mode). Opt-in off: block runs exactly as
before (live truth-table tested).

## Root cause 3 (C6d): a coverage gap, not a trajectory bug

Your barycenter-class instinct pointed the right way, but the trigger
differed: the Sun-trajectory resolution was fine (C1 proved the fetch
works). The engine simply EXCLUDED the center body entirely -- and a
centered body's sun-direction elements must track the Sun moving around
it across frames even though the body sits at the origin. The frame-1
freeze there is a physics lie; the indicator hover even documented it as
a limitation. Now it's a capability instead.

FIX: `get_center_engine_elements(center)` is the SINGLE SOURCE OF TRUTH
for which center elements the engine owns (sun-direction-dependent only:
indicator + checkbox-gated sodium tail; inertial axis/cone correctly stay
frozen; Sun-centered returns empty). Two consumers of that one producer:
the animate dispatch call passes it as `skip_elements` (threaded through
add_center_body_shells -> create_celestial_body_visualization, default
None) so dispatch and engine never double; collect_perframe_elements adds
matching `center_fixed` specs (origin position every frame, per-frame
Sun). The center indicator's radius comes from the dispatch's rendered
outermost (fig._shell_outermost_radius_au) when available, else the
100x-body-radius fallback -- matching dispatch scaling.

## Verification done (Claude-side)

- py_compile clean (both files); ASCII-only; LF; 245 diff lines, hunks
  confined; transactional binary edits with count asserts (one anchored
  edit FAILED LOUD on a wrong count -- the Sun branch hardcodes
  center_object='Sun' -- and was redone with correct anchors; the
  all-or-nothing pattern caught it before any bytes were written).
- LIVE tests in the real module namespace under xvfb:
  T1 sticky-visible regression: full allocation + 24-frame rebuild
     replication through perihelion; EVERY slot write serializes an
     explicit visible; perihelion tail traces visible=True in JSON.
  T2 frame-1 skip truth table: fires only for opt-in + non-MAPS.
  T3 get_center_engine_elements: Sun center empty; sodium gated by its
     box; indicator rides any-checked.
  T4 C6d end-to-end: dispatch with skip_elements omits sodium +
     indicator (both present without it); engine center indicator at the
     origin tracks a MOVING Sun (cosine > 0.999 at a mid-sweep frame).
  T5 dispatch regression: skip_elements=None output IDENTICAL to the
     unpatched HEAD module (imported side by side) -- the static
     pipeline is provably untouched.
- NOT testable in-container: the live Plotly.js render of the merge fix
  (R1), Horizons-backed runs. Protocol v4.1 covers them.

## Ledger

Updated in this delivery (LEDGER_orrery_consolidated.md): header chain
through d05f0f1 + fix pass; pending action = apply 2 files, run v4.1;
D.Priority carries the three FIXED blockers with root causes + the
promoted 'osc.' epoch-parser gap (OPEN, pre-existing, every run);
D.Cosmetic gains the <br> hovertext item; item 19 gains the 3D arrow
camera controls and the C6a/O16 partial-pass record; F log gains the
fix-pass entry (reproduction-before-patch; the perihelion repro
exonerated the engine and convicted the frame merge).

## V4.1 Retest Results (June 12, 2026 -- Tony, Mode 5)

Tested at HEAD 39370bb3be99559aa5e8cd68bb8188d855dfc31e. Three fixes
verified on Windows, Python 3.13.

### R1 -- Ikeya-Seki perihelion rerun
- PASS. Truly beautiful. No doubled nucleus/indicator/legend. Tail
  PRESENT at perihelion matching the static render's character. Coma
  and tails appear as distance thresholds cross and persist while active.
  Sun Direction indicator present and tracking throughout. File size:
  181 KB without tails, 3215 KB with tails (worth it for the educational
  value). The tail swinging anti-sunward as the comet rounds perihelion
  is THE educational moment this engine was built to show.

### R2 -- Mercury-centered Sun tracking
- PASS. Perfect. Both Sun-on and Sun-off views synchronize. Sodium tail
  and Sun Direction indicator perfectly align. No doubled traces. Rotation
  axis fixed in center view (correct physics -- inertial orientation).
  Beautiful. Meets the "our work is not just right -- it's beautiful"
  criterion.

### R3 -- Regression
- Static Mercury-centered: PASS. Correct.
- B1-style Uranus (29 years, Sun-centered and Uranus-centered): PASS.
  Sun Direction indicator tracks in both views. In Uranus-centered view,
  only Sun Direction indicator tracks (rotation axis stays fixed --
  correct). NOTE: since non-center shell per-frame tracking is not yet
  implemented for all elements, the hover text for those elements should
  note this. Ledger item.
- MAPS animation with opt-in: GAP FOUND. Render with opt-in checked and
  unchecked is IDENTICAL. Only frame-1 tail shows, even before the comet
  reaches the disintegration point. The per-frame engine does not engage
  for MAPS. Root cause: MAPS has special disintegration-mode code paths
  ("headless ghost comet" / "pre-disintegration mode: active comet with
  coma") that bypass the standard comet tail builder. The opt-in checkbox
  likely does not reach the MAPS-specific branch. This is a scoped issue
  (the engine works for standard comets -- R1 proved it); the MAPS path
  needs its own wiring.

### Observation Log v4.1 (O18-O20)

O18 -- Perihelion render quality: excellent. The tail development through
threshold crossings is smooth and educational. The static-vs-animated
parity at perihelion is now confirmed.

O19 -- Center-body sodium/indicator motion: the Mercury test is a
showcase render. The tail swing and indicator alignment are precisely
synchronized. High educational value.

O20 -- Free-form:
(a) MAPS per-frame tails not engaging (see R3 above). Scoped to
    MAPS disintegration path, not systemic. Ledger item.
(b) Uranus-centered: non-tracking elements should carry hover text
    noting the limitation. Ledger item.

### V4.1 Retest Disposition

Phase 3 core track (Sessions A/B/C + fix pass) CONDITIONALLY CLOSED.
All three blocking bugs (C2a doubling, C2b/C2c sticky visible,
C6d Mercury Sun tracking) are RESOLVED. R1 and R2 are clean passes
with beautiful educational renders. One scoped gap remains: MAPS
disintegration-mode tails do not engage with the per-frame engine.
This is NOT a blocker for the core track -- it is a MAPS-specific
wiring issue that can ride a future MAPS maintenance session.

### New Ledger Items

- MAPS disintegration-mode per-frame tails: the opt-in checkbox does
  not reach MAPS's special ghost/pre-disintegration code path. Standard
  comets (Ikeya-Seki) work correctly. MAPS needs its own wiring.
- Non-center non-tracking elements: hover text should note which
  elements are per-frame tracked vs frame-1 frozen for non-center
  bodies in heliocentric animations.

Module updated: June 2026 with Anthropic's Claude Fable 5 + Claude Sonnet 4.6
