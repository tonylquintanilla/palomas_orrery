ADDENDUM to HANDOFF v23 -- Design-Session Narrative (Bow Shocks + Dipole Cone)
Tony Quintanilla, PE | Claude Opus 4.8 | June 2, 2026
Status: narrative notes to fold into v24 AFTER the build. Not a renumber of v23.
Companion to: MANIFEST_bow_shock_and_dipole_cone_v1.md (the build spec).

PURPOSE
This captures what the manifest does NOT: the reasoning trail, the Tony-catches,
and a few live flags that otherwise live only in the design conversation. The
manifest carries the DECISIONS (conic shape, sourced standoffs, item-24 reframe,
dipole/obliquity distinction). This carries the PROCESS -- the lesson layer the
protocol treats as a first-class output. When v24 is written after the build,
fold both the build results AND these narrative items in.

--------------------------------------------------------------------------------
1. THE REASONING TRAIL (decisions survive in the manifest; the path does not)
--------------------------------------------------------------------------------
- SHAPE arrived at by self-correction, not first instinct. Claude's progression
  was: (a) pure paraboloid -> (b) a HEURISTIC conic (an invented flank-gain
  factor) -> (c) the real conic-section model r = L/(1+e*cos a). The flip from
  (b) to (c) happened ONLY because Tony twice declined to accept the lean and
  said "do your own search / what is the evidence." The dedicated literature
  search returned the standard form and the fitted eccentricities, and showed
  the rigorous conic was actually FEWER lines than the heuristic AND sourceable.
  Lesson: Claude's first instinct was the unsourced fudge; the heuristic would
  have shipped into the handoff as "illustrative conic" with an invented
  parameter. Tony's push to source it caught it. This is Fetched-vs-Recalled
  applied to GEOMETRY, not just to numbers -- a recalled-style fudge vs. a cited
  model. The double-helix did exactly its job.

- ITEM 24 REFRAMED (handoff-is-a-claim / code-is-fact). v23 carried item 24 as
  "bow shock is custom geometry that must sit in the body-frame -> first
  consumer of orient_to_planet_pole." Reading the actual magnetosphere builders
  showed the shocks are built -X sunward then rotate_to_sunward(sun_position) --
  they are SUN-framed and consume sun_position, NOT the pole-vector producer.
  The bow shocks are self-contained and depend on no pole-frame work. The
  genuine first pole-frame consumer is the Uranus tilt cone (Movement 2), not
  the shock. The handoff premise was physically off; the code corrected it.

- GEMINI CROSS-CHECK was nearly run anchored, then corrected to blind. Claude's
  first draft of the Gemini prompt INCLUDED Claude's own numbers. Tony caught
  that this invites anchoring (Gemini pattern-matches "1.96, sounds right" and
  rubber-stamps) and collapses two independent opinions into one. The prompt was
  rewritten to ask for values de novo, no figures supplied. The blind pass then
  agreed on 7 of 8 independently and surfaced the conic-shape upgrade and the
  ice-giant dipole OFFSET (vertex displacement) -- findings an anchored check
  would likely have missed. Mode-7 lesson: a cross-check is only a cross-check
  if the second opinion is independent; supplying the answer key defeats it.

--------------------------------------------------------------------------------
2. TONY-CATCHES (attributable; the manifest flattens these into bare facts)
--------------------------------------------------------------------------------
- THE INNER-PLANET INVENTORY CORRECTION came from Tony's question. Claude's
  first scope pass covered only the four giants. Tony asked "what about the
  Mercury, Venus and Mars bow shocks?" -- which forced a verify-don't-assume
  sweep that found: (i) Mercury and Venus both carry a literal 15*radius
  standoff COPY-PASTED from Earth, ~8-10x too large; (ii) Mars was the only
  inner body correctly rescaled (1.5); (iii) the giants' tooltips DESCRIBE a bow
  shock that is not actually rendered. None of this was on Claude's radar before
  the question. The eight-copy duplication this exposed is what made the
  extract-the-shared-shape decision clearly correct rather than optional.

- THE EARTH SHAPE INCONSISTENCY was Tony's catch. Claude planned to keep Earth
  on the legacy paraboloid as a "regression anchor" while every other body got
  the cited conic. Tony asked "shouldn't we use the new standard model that's
  cited?" -- exposing that Claude was conflating two things: the anchor's job
  (prove the EXTRACTION is faithful -- a one-time test, already green) vs. the
  RENDER (should use the best cited model). Resolution: Earth renders the conic
  like everyone else; the paraboloid path survives only as the extraction
  regression test, not in the delivered figure. Tony's question retired an
  oddity ("Earth is special for test reasons") before it calcified.

- EARTH VALUE was Tony's judgment call, evidence-informed. Claude searched;
  the literature split into two correct camps (textbook ~15 vs. measured-nominal
  ~11-14 / Shue ~13.5). Tony chose 15 WITH a tooltip note of the range -- the
  honest presentation (a convention, not a precise fit).

--------------------------------------------------------------------------------
3. LIVE FLAGS (stated assumptions; low-risk but should be visible)
--------------------------------------------------------------------------------
- orrery_rendering.py (home of create_info_marker and rotate_to_sunward) was
  read from the /mnt/project SNAPSHOT this session, not a fresh upload. These
  are the stable v3.24 Stage-3 factories, unchanged by v22/v23 (which touched
  Uranus/Neptune frames and idealized_orbits.py). Signatures used:
    create_info_marker(x, y, z, color, text, legendgroup, customdata=None,
                       fill_color=None, border_color='red')
    rotate_to_sunward(px, py, pz, center_position, sun_position)
  Re-confirm against a fresh upload at build time if either is edited (we only
  CALL them, so risk is low).

- VERIFICATION ARTIFACTS were in the session container (/home/claude/) and are
  EPHEMERAL -- they vanish with the container. The re-runnable guarantee rests
  on the function copy EMBEDDED in the manifest, which was extracted and
  re-verified: compiles clean, anchor exact (0.0 diff on x/y/z over 900 points),
  conic nose pinned at -standoff, flank opens finite. The build session should
  re-run the anchor test from the manifest's embedded copy, not assume the
  container test persisted.

- CONIC FLARE is a Mode-5 watch item. At e=1.05 the conic flank is much wider
  than the legacy paraboloid (physically correct -- marginal hyperbola flares
  toward its Mach-cone asymptote). The new shocks WILL look more flared than the
  old paraboloids. The 0.92 asymptote-cap factor in create_bow_shock_shape is
  the knob if Tony's eyes find it too broad.

- DEAD-CODE ANNOTATION is a standing Tony instruction for the build: annotate
  (do not remove) any dead inline code encountered while editing -- e.g. the
  dead rotate_points import in uranus_visualization_shells.py. Removal is the
  deferred D3 sweep, not this work.

--------------------------------------------------------------------------------
4. ONE-LINE SUMMARY FOR THE v24 LESSON ARCHIVE
--------------------------------------------------------------------------------
"The first instinct was the unsourced fudge; sourcing it (at Tony's push) made
it simpler AND citable. Three of the session's load-bearing corrections -- the
inner-planet inventory, the Earth shape inconsistency, and the Gemini blind
check -- were Tony-catches against a too-narrow or too-quick first pass. The
manifest records what was decided; this records that the deciding was a
double-helix, not a monologue."
