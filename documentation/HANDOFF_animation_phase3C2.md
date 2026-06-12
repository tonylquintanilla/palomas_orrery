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

Module updated: June 2026 with Anthropic's Claude Fable 5
