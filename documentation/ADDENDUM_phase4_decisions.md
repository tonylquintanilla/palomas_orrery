# ADDENDUM -- Phase 4 Brief: Review Decisions

Tony Quintanilla, PE | Claude Fable 5 review | June 12, 2026
Companion to: HANDOFF_animation_phase4_brief.md (at bd008ee)
Review chain: brief built on 988d0f8; reviewed at HEAD bd008ee
(remote HEAD verified matching; all code anchors in the brief
spot-verified byte-accurate against the live tree).

## Decisions (Tony, June 12, 2026)

1. MAPS DEFERRED. Per the review's sequencing analysis, MAPS
   per-frame wiring drops from the Phase 4 session to a future
   MAPS maintenance session (consistent with the 3C2 disposition).
   Phase 4 primary scope is now: per-frame magnetosphere, camera
   tracking, Sun Direction clamp, plus the completion riders.

2. "PER-FRAME ELEMENTS" UI GROUPING APPROVED. The magnetosphere
   opt-in goes into a labeled group in the animation settings
   panel alongside the existing comet-tail and sodium-tail
   toggles, rather than accreting as a standalone checkbox.
   Pairs with the resolution-management ambition: one
   perframe_resolution_scale concept, not scattered per-body flags.

3. PRECISION-ROUNDING MEASURED FIRST. Before committing to
   resolution parameters (belt n_points, bow shock n_phi/n_theta,
   envelope density), run measure_perframe_elements.py with
   coordinate rounding (4-5 significant digits) applied to the
   per-frame arrays. The rounding lever is orthogonal to and
   multiplies with resolution reduction; its measured savings may
   change where the resolution knobs need to land (including
   whether Jupiter needs any special handling at all). Measurement
   gates parameter selection -- this REORDERS the session start.

## Amendments to the brief (from the review)

A. Rotation-vs-rebuild (brief's open question, Feature 1): CLOSED
   as a byte-savings dead end. Plotly frames carry trace data, not
   transforms; rotated coordinates serialize at the same size as
   rebuilt ones. Rotation saves CPU only. Byte levers are: fewer
   points (resolution), fewer frames, and coordinate precision
   (decision 3). Do not spend session cycles here.

B. Jupiter: no special-case exclusion in code. Run Jupiter through
   the same reduced path (resolution + rounding), measure, and let
   Gate 5(b) -- Tony's Mode-5 judgment -- choose between reduced
   per-frame and frame-1-frozen-with-disclosure. A per-body
   carve-out is a parallel pipeline in miniature.

C. Camera tracking: build the NATIVE version this session --
   go.Frame(layout=dict(scene=dict(camera=...))) behind a toggle.
   The JS post-processing track-and-orbit design (frame-transition
   events + Plotly.relayout on camera.center, preserving the
   user's eye offset) is recorded as a designed follow-on, not
   attempted cold. Ledger item.

D. De-risk check BEFORE building camera tracking: manually Fly To
   Mercury at shell scale in a full-system STATIC plot and confirm
   render quality (precision artifacts, near-plane clipping,
   perspective at extreme zoom ratios inside an AU-scale cube).
   If it's ugly, the feature needs aspectmode/range thinking
   (item 19) before the per-frame work, not after.

E. Fly To shell-aware distance consumes the existing producer
   fig._shell_outermost_radius_au -- do not recompute extent.
   One producer, two consumers.

F. Frozen-element hover disclosure follows the Envelope house
   style: say what is frozen and why ("orientation from frame 1;
   per-frame tracking not yet implemented for non-center bodies"),
   not just that a limitation exists.

## Captured for the MAPS deferral (so nothing floats)

- TWO exclusion sites match the literal string 'MAPS':
  palomas_orrery.py L2209 (engine comet collection) and L7269
  (frame-1 skip block). They must change in lockstep when MAPS is
  wired in, or the C2a doubling / dead-slot disease returns.
  Grep both sites again at implementation time.
- Clean partition for the eventual wiring: engine owns ONLY the
  pre-disintegration active-comet traces (standard builder,
  date-gated); after the disintegration date those slots pad to
  explicit-invisible dummies (sticky-visible fix makes this safe,
  and the vanishing tail is correct physics -- an educational
  moment, not a workaround). Ghost tail + disintegration marker
  stay static frame-1.
- Ghost-tail design call recorded: static is the default. The only
  physically honest animated alternative is a GROWING debris arc
  (leading edge advancing along the Barker trajectory past the
  disintegration date). Deferred, not forgotten.

Module updated: June 2026 with Anthropic's Claude Fable 5
