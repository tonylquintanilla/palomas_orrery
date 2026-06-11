# ANIMATION TEST PROTOCOL v4 -- 21/51 Through Phase 3 Session C

Tony Quintanilla, PE | Claude | June 11, 2026
Supersedes v3 (Session B gate -- CONDITIONALLY PASSED June 11).
Session C patch base: orrery repo HEAD 0ce1e26 | Patched (6 files):
palomas_orrery.py, shell_configs.py, comet_visualization_shells.py,
shared_utilities.py, uranus_visualization_shells.py,
neptune_visualization_shells.py

WHAT SESSION C ADDED
1. Barycenter Sun-Direction fix (B3-bonus): sun-direction elements use the
   REAL Sun -- positions_over_time, else an engine-fetched Sun trajectory
   (one Horizons call per frame when the Sun checkbox is off), else
   SUPPRESSED with a console note. (0,0,0) is never drawn toward.
2. Console-spam fix (O13a): engine rebuilds run with stdout suppressed;
   per-builder messages print once at allocation.
3. Comet tails per frame, OPT-IN: new checkbox in Animation Settings
   ("Animate comet tails (rebuild each frame)"), default OFF. Trace-
   returning core build_comet_tail_traces (capture shim; the 240-line
   builder unchanged). Variable-count handling: allocation probes every
   frame and pads to the maximum. MAPS excluded (frame-1 as before).
4. Mercury sodium tail: engine customer, gated on ITS OWN checkbox.
   Its greyed placeholder is skipped when engine-animated.
5. Hover disclosure: U+N bow-shock hovers gain the conic-model
   sourced-vs-schematic note + animation-freeze line (the D.Movement
   remainder); the sun-direction indicator hover gains the
   center-frozen/non-center-tracking line (one central site).
6. One-line auto-scale: under Auto, the animation cube is the LARGER of
   the orbital and center-shell extents -- never shell extent alone.

================================================================
SESSION C RENDER GATE
================================================================

C1. Barycenter fix (the B3-bonus regression test)
  Config: Earth-Moon Barycenter centered, Earth + Moon checked, Earth
  magnetosphere checked, SUN CHECKBOX OFF, ~29 frames.
  [ ] Console: "Sun checkbox off -- fetching Sun trajectory..." appears.
  [ ] Earth's Sun-Direction indicator points at the SUN (verify with a
      second run, Sun checkbox on, same dates -- direction matches), NOT
      at the barycenter/Moon, and tracks the real Sun across frames.
  [ ] If you can simulate a fetch failure (offline), the indicator is
      absent with the "suppressed -- Sun position unresolvable" note --
      optional check.

C2. Comet tails per frame (the headline)
  Config: a comet crossing its activity thresholds in the span (perihelion
  approach), Sun-centered, opt-in CHECKED, ~29 frames.
  [ ] Console: "Per-frame comet tails: <name> allocated N slots (max over
      29 frames)" and the engine budget line.
  [ ] Tail swings anti-sunward as the comet rounds perihelion; features
      (coma/tails) APPEAR as thresholds are crossed -- watch the legend
      entries update from "(inactive, >X AU)" to active names.
  [ ] No FATAL assert in console (padding held across thresholds).
  [ ] Same run, opt-in UNCHECKED: frame-1 tails as before (regression).
  [ ] MAPS animation with opt-in CHECKED: MAPS stays frame-1 (excluded);
      other comets in the same run animate.

C3. Sodium tail rides Mercury
  Config: Sun-centered, Mercury checked, Mercury SODIUM TAIL checked,
  opt-in state irrelevant.
  [ ] Sodium tail rides Mercury per frame, pointing anti-sunward.
  [ ] NO "Mercury: Sodium Tail (static plots only)" greyed entry (the
      engine animates it); other checked Mercury shells still greyed.
  [ ] Budget line includes the tail (~48 KB/frame at 500 particles).

C4. Console spam (O13a)
  [ ] Any engine run: "Sun direction indicator: Using shell radius..."
      and "[COMET VIZ]..." blocks print ONCE (allocation), not per frame.

C5. Hover disclosures
  [ ] Uranus-centered static or animation, magnetosphere on: bow-shock
      info marker hover shows the conic-model note + freeze line. Same
      for Neptune. AU/km values unchanged.
  [ ] Any sun-direction indicator hover: the center-frozen /
      non-center-tracking line reads correctly in both contexts.

C6. One-line auto-scale
  Config: Sun-centered animation, inner planets, full corona set, Auto.
  [ ] Cube holds the ORBITS (orbital extent wins over shell extent --
      the inverse of the Finding-1 collapse).
  Config: Mercury-centered animation, Mercury shells on, Auto, Moonless.
  [ ] Cube fits the shells when shell extent exceeds orbital extent.
  [ ] Manual scale: never overridden.

C7. Regression sweep
  [ ] B1-style run (Uranus riding primitives): unchanged from Session B.
  [ ] No-shells, no-opt-in animation: no engine lines, payload matches
      Phase 1/2.
  [ ] One static plot with U or N magnetosphere: renders unchanged except
      the new hover lines.

================================================================
OBSERVATION LOG v4 (continue numbering)
================================================================
  O14. Per-frame comet tails: visual quality through threshold crossings
       (legend churn as features activate -- acceptable or noisy?).
  O15. Sodium tail at 500 particles per frame: keep, or drop the count in
       per-frame mode (knob exists)?
  O16. Auto-scale max() behavior across your scale combinations -- feeds
       item 19's comprehensive review.
  O17. Free-form.

================================================================
RECORD FOR THE LEDGER
================================================================
- C1-C7 pass/fail; O14-O17; new HEAD after push.
- On pass: 21/51 Session C render-confirmed -- the Phase 3 core track
  (Sessions A/B/C) is COMPLETE. Remaining riders: resolution-sweep
  follow-on (gate 5b), item-19 scaling review (fixtures accumulated),
  camera-tracking tooling, measure-tool file browser.

Module updated: June 2026 with Anthropic's Claude Fable 5
