# ANIMATION TEST PROTOCOL v1 -- 21/51 Phase 1 (Frame Fence + Sun Threading)

Tony Quintanilla, PE | Claude | June 9, 2026
Patch base: orrery repo HEAD 730b2bf | Patched file: palomas_orrery.py
Companion tool: measure_animation_html.py

PURPOSE. Verify the two Phase 1 fixes in the live render (Mode 5), quantify
the frame-payload reduction on real exports, and systematically capture the
animation render issues you have seen or will see (ledger item 21/51
objective 4) so Phase 2/3 design starts from observed fact, not code reading.

THE TWO FIXES UNDER TEST
1. Frame fence: animation frames now carry ONLY the traces the frame loop
   updates (object/barycenter markers). Orbit paths, idealized orbits,
   trajectory layers, comet tails, and the center marker are no longer
   serialized into every frame. Render must be IDENTICAL except file size.
2. Sun threading: the animate shell dispatch now receives the frame-1 Sun
   position. Two visible consequences in planet-centered animations with
   magnetosphere shells: (a) the magnetotail orients anti-sunward instead of
   defaulting unrotated; (b) the Sun Direction indicator now renders (it was
   silently suppressed before -- the zero sun-vector read as "body at Sun").

================================================================
PHASE 0 -- BASELINE CAPTURE (run BEFORE replacing palomas_orrery.py)
================================================================

Using the CURRENT build (HEAD 730b2bf, unpatched), run and SAVE the HTML for:

  B1. Sun-centered, Mercury through Mars checked, actual orbits on,
      ~30 frames (e.g. 30 days, Day step). No shells.
  B2. Sun-centered, same objects, with a few solar shells checked
      (e.g. corona shells). Same frame count.
  B3. Earth-centered, Moon checked, Earth magnetosphere shell checked,
      ~30 frames.

Keep the three baseline HTML files. Record for each: the console
[ANIMATION] lines, and file size. No visual checks needed yet.

================================================================
PHASE 1 -- PATCHED VERIFICATION
================================================================

Replace palomas_orrery.py with the patched file. Re-run B1/B2/B3 with the
SAME settings (same dates if practical) and save as P1/P2/P3.

Console check (every run):
  [ ] New line appears: "[ANIMATION] Frame-updated traces: N; constant
      traces excluded from frames: M" with M > 0 whenever orbits are on.

Measurement (every pair):
  python measure_animation_html.py B1.html P1.html   (repeat for 2, 3)
  [ ] "Traces carried in frames" on P-files lists ONLY moving bodies
      (no orbit_*, no shell names, no center marker).
  [ ] Frames payload drops sharply; total file size drops accordingly.
      Record the before/after MB for the ledger.

Mode-5 visual checks, P1 (pure fence test):
  [ ] Slider scrub: planet markers move smoothly along their orbits.
  [ ] Orbit path lines persist, static and correct, during playback.
  [ ] First displayed frame matches slider position 0 (no jump on first
      scrub -- this exercises the rewritten first-frame sync mapping).
  [ ] Legend toggles still work for both orbits and markers.
  [ ] Hover on a moving marker shows full hover text; hover on an orbit
      line unchanged.
  [ ] Play/pause behaves; frame names (dates) shown correctly.

Mode-5 visual checks, P2 (static shells + fence):
  [ ] Solar shells render and stay put during playback.
  [ ] Planets animate over/through the shells exactly as before.

Mode-5 visual checks, P3 (sun threading -- the Edit A test):
  [ ] Magnetotail points AWAY from the Sun's frame-1 position. (Turn the
      Sun checkbox on to see the Sun marker; the tail should point opposite
      it at the first frame.)
  [ ] NEW: "Earth: Sun Direction" indicator renders (cross marker + line
      toward the Sun). This is new behavior -- it was suppressed before.
  [ ] Known honest limitation, confirm and accept: the magnetosphere
      orientation is FROZEN at frame 1 while the Sun marker moves over the
      animation span. (Hover disclosure of this freeze is deferred to the
      bow-shock sourced-vs-schematic disclosure sweep -- ledger.)
  [ ] Moon animates correctly around the static Earth shells.

Regression (static pipeline untouched, but verify):
  [ ] One static plot, any config you know well -- render identical to
      pre-patch. (No edits landed in plot_objects; this is the cheap
      confirmation that nothing leaked.)

================================================================
PHASE 2 -- ITEM-4 OBSERVATION LOG (captures what the code reading found,
plus whatever your eyes find)
================================================================

These are NOT pass/fail -- they are structured observations to seed the
Phase 2/3 design. Log what you see; add anything not listed.

  O1. Comet animation (e.g. a comet over its perihelion window):
      EXPECTED DEFECT: the tail renders at the frame-1 position only and
      the comet walks away from it. Confirm; note how bad it looks at
      your typical spans. (Candidate Phase 3 tier-2 element.)
  O2. Planet-centered animation with SUN shells checked:
      EXPECTED NO-OP: checking Sun shells does nothing when the center is
      a planet (the animate path has no offset-Sun branch). Confirm.
      (Phase 3 scope: moving-body shells.)
  O3. Non-center planet shells in animation (e.g. Sun-centered, Earth
      magnetosphere checked): EXPECTED NO-OP today. Confirm. (Phase 3.)
  O4. Rotation axis / dipole cone in a Uranus- or Neptune-centered
      animation: these are body-triggered and the center body's shells DO
      dispatch, so the axis + cone SHOULD render statically at center if
      any shell is checked. Confirm whether they appear. (This refines the
      v27 "animation gap" record: code reading says the gap is for
      NON-center bodies only.)
  O5. Center-body hover: the animate center marker hover is a bare name
      (static builds it from the INFO encyclopedia). Cosmetic divergence;
      note if it bothers you. (Phase 2 consolidation absorbs it.)
  O6. Anything else: jumps, ghosts, legend oddities, wrong scales,
      satellite behavior, trajectory-layer behavior in animations.
      Free-form log -- this is the Mode-5 ground truth Phase 2/3 needs.

================================================================
RECORD FOR THE LEDGER / NEXT HANDOFF
================================================================
- B/P file sizes and frames-payload numbers (the measured reduction).
- Pass/fail on the P1/P2/P3 checklists.
- The O1-O6 observation log.
- New HEAD SHA after pushing the patched file.

Module updated: June 2026 with Anthropic's Claude Fable 5
