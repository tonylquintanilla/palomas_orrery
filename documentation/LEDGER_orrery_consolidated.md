# LEDGER -- Orrery Refactor / Movement Track (Consolidated, Running)

Tony Quintanilla, PE | Claude | June 7, 2026 (last updated June 13, 2026)
Base SHA at consolidation: `76c330e` (76c330ea4dbe6bc667fba2ffb5baa1a65ae56d22)
Current verified base: `a69c3a7` (a69c3a79466e5e3f02589eaee13031800d08be73)
Chain since consolidation: 76c330e -> 730b2bf (June-8 fixes) -> 7977a11
(animation Phase 1) -> 3f03c12 -> 191cf36 (Phase 2) -> 8438a85 (Phase 3 GO)
-> a9f0ec4 (Session A) -> e5fd86d (Session B) -> 0ce1e26 -> 7b71c29
(Session C) -> d9460e2 (provenance scan) -> 02cce78 (ledger) -> d05f0f1 (Session C
test results: NOT YET CONFIRMED, 3 blocking bugs -> fix pass C2
delivered June 11, render-gated on protocol v4.1).
Phase 4 render-gate session (June 13): `5e83c1e` -> `a69c3a7` -- camera-tracking
live fix (JS relayout), element-extent window sizing, per-frame grid fix, center
reticle suppression under tracking, and the hyperbolic osculating `color` fix;
all `[render-confirmed Mode 5]` by Tony on live Mercury data.
Reticle + docs pushed -> `33aac7` family -> `33aac56` (current base).

ROADMAP (June 13, Tony's call): active batch is items 1/3/5 --
(1) cube-residual cleanup [ATTEMPTED + RENDER-FALSIFIED + REVERTED this
session: frames-data-only did NOT fix the swing (JS relayout overridden by
Plotly per-frame autorange); pushed 373298d then reverted to restore
frame.layout; refined diagnosis in the camera-tracking residual, deferred
to a dedicated session]; (3) 3D axis control (dtick + range) in
orrery GUI + Studio, machinery warm now (`_calculate_grid_dtick`,
`traces_extent_from_center`); (5) palate-cleansers: near-parabolic apoapsis
false-precision (Envelope candidate), stale O2/O3 console wording, 4
apsidal_markers.py em-dashes, AND the remaining dipole cones (see set below).
DEDICATED (not a cleanup folder): the plot_objects/animate_objects DIVERGENCE
AUDIT -- map both pipelines, three-bucket catalog (shared / intentionally
divergent / accidentally divergent = drift), optional parity smoke test;
its own focused session, map-first-decide-second. The FULL function merge
stays OFF the list (chokepoints already earned most of its value; high blast
radius). RESERVE: IPC food-insecurity build (API key not yet arrived, Tony
waiting a few days) and the Gallery/Studio track (section H) as the
mission-flavored option if IPC keeps waiting.
Introduced by: HANDOFF v28. Supersedes the in-handoff ledgers embedded in
v23 (canonical body), v24, v25, v26, v27.

THE RUNNING LEDGER. From here forward this is the single authoritative backlog
for the orrery refactor / Movement chain. Future handoffs UPDATE THIS FILE IN
PLACE and reference it; they do NOT re-embed a fresh copy. That is the cure for
the rebase-leak failure this consolidation had to repair (items that lived only
"by reference" in v24-v27 and silently fell out of view). Numbering is preserved
from the D1/D2/D3.1/N-series authority; nothing is renumbered.

## Provenance of this ledger

The chain runs back to ~April 15, 2026 (the provenance audit). v23 already
absorbed that earlier history into its canonical "Reconciled Deferred-Items
Ledger" (D1 items 1-41, D2 42-54, D3.1 55-61, stage items N1-N14, U-items,
Phase buckets). This file carries v23's body forward and reconciles it against
the v24 -> v27 Movement work and against the live code at HEAD.

## Verification convention (honesty about this ledger's own claims)

A handoff is a claim; the code is closer to fact. Each status carries a tag:

- `[verified @SHA]` -- checked against the live repo code in the named session.
- `[per chain; not re-verified]` -- carried from a handoff's prose; status is
  as the handoff stated, NOT re-confirmed against HEAD this session.
- `[render-gated]` -- correctness is a Mode-5 judgment, not settleable here.
- `[render-confirmed Mode 5]` -- Tony's eyes passed it on live data.

Items with no tag are administrative (tracks, actions) rather than code claims.

---

## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; cross-referenced)

- **Food Insecurity (REOPENED, active).** Earth System track, not the orrery
  refactor. Design locked: HANDOFF_food_insecurity_design_v1.md +
  MANIFEST_food_insecurity_sudan_first_cut.md (Sudan first cut, IPC KML vector
  polygons / approach B, folders-per-period, transcribe-not-synthesize stance).
  Status: awaiting IPC Public API key (request submitted; CC BY-NC-SA 3.0 IGO
  terms reviewed and compatible with the non-commercial educational use).
  Build base will be HEAD at build time (design base was de12f56). RELEASE-DRIFT
  CORRECTION to fold in at build: the current Sudan release is Feb-May 2026
  Current + projections to Jan 2027, and names NO current Famine areas -- so the
  manifest's section-10 El Fasher/Kadugli Phase-5 spot-check (Sept 2025 picture)
  must be rewritten to the current classification.
- **Protocol -> Skills refactor (process/tooling, not orrery code).** v27 idea:
  split the trigger-fired PROCEDURE layer (docstring standard, agentic pre-test,
  provenance-scanner mechanics, single-info-marker pattern, Horizons center rules,
  bottom-up / binary-mode editing) into Anthropic skills, keep the resident
  JUDGMENT layer (modes, criticality philosophy, Foundation, "when unsure ask",
  double-helix) in context. CAUTION: CRITICAL gates (SHA round trip,
  verify-execution, enumerate-uploads) must fire reliably -> stay resident or keep
  a one-line resident pointer; only QUALITY/PRACTICE mechanics are safe spin-offs.
  Its own sketch-first session: design which skills + triggers before building.
- **Protocol amendment candidates (for v3.29; from the animation refactor):**
  - The xvfb SystemButtonFace<->gray90 sed round trip is NOT idempotent on files
    that natively contain gray90 (palomas_orrery.py has 26 native gray90
    literals). Rule: run the swap on a THROWAWAY copy only; never
    restore-in-place on the deliverable. (Caught June 9; applied as practice
    in every session since.)
  - Full-module exec under xvfb with tk mainloop suppressed enables LIVE-dispatch
    tests inside the real module namespace (real tk vars, real builders, network
    calls patched). Used as the standard verification gate for Sessions
    Phase 2 through 3C; candidate for the Agentic Pre-Test section.
  - `grep -c` exits 1 when the count is 0, silently BREAKING an `&&` chain --
    a downstream verification command can simply never run while the output
    looks complete. Rule: never put `grep -c` mid-chain with `&&`; run
    verification greps standalone or with `;`. (Caught June 10 -- one residual
    check did not execute until re-run standalone.)

## PENDING ACTION (Tony-side)

- **Apply the C2 fix pass (2 files) and run ANIMATION_TEST_PROTOCOL_v4_1**
  (the focused retest of C2/C6d + regression), append results to the 3C
  handoff, push. On pass: the Phase 3 CORE TRACK (Sessions A/B/C + fix
  pass) is COMPLETE -- move the marked render-gated items below into
  section C and update 21/51. (v4 first run, June 11: C1/C3/C5/C7 PASS,
  C4 pass-with-caveat, C2/C6 blocked by the three bugs below -- all
  three root-caused and fixed in pass C2.)
- **Commit protocol v3.28 (or v3.29 with the candidates above) to the repo
  root.** `[per chain; not re-verified June 11]`
- (CLEARED June 11) Phase 2, Session A, Session B, and Session C are all AT
  HEAD (chain above); no code push outstanding.

---

## B. STRATEGIC STATUS

**The shell-consolidation refactor is COMPLETE** (per v23 headline; all 13 bodies
route through SHELL_CONFIGS / CUSTOM_SHELLS -> create_celestial_body_visualization
-> build_sphere_shell -> create_info_marker). The project is in
cleanup-and-close, not mid-refactor. (June 11: the create_planet_visualization
wrapper is now RETIRED -- zero pipeline callers; see section C.)

**Animation refactor (21/51): CORE TRACK DELIVERED, final gate pending.**
- Phase 1 (frame fence + sun threading + first-frame sync) -- DONE
  `[render-confirmed Mode 5 @7977a11, June 10]`. 88-94% file reductions.
- Phase 2 (scene-assembly consolidation 2a-2d) -- DONE
  `[render-confirmed Mode 5, June 10-11]`. Closed N3 + O5 + O6(a); two fixes
  shipped during testing (incl. osculating labeling, idealized_orbits)
  `[per chain]`.
- Phase 2.5 (wrapper retirement, 3 sites) -- DONE
  `[render-confirmed Mode 5 via Session A gate, June 10]`.
- Phase 3 Session A (design doc + 3a + budget harness) -- DONE
  `[render-confirmed Mode 5, June 10]`. Rebuild-as-universal adopted;
  gate 5(a) bytes PASSED at measured reduction.
- Phase 3 Session B (per-frame engine + axis/cone/indicator + greyed-legend
  disclosure) -- CONDITIONALLY render-confirmed June 11: engine allocates,
  rebuilds, budget-reports correctly; riding behavior visually confirmed at
  planet-centered scale; solar-system-scale visual confirmation blocked by a
  TOOLING gap (camera tracking; item 19), not an engine defect.
- Phase 3 Session C (barycenter Sun fix, console-spam fix, opt-in per-frame
  comet tails, sodium tail, U+N bow-shock disclosure, one-line auto-scale) --
  DELIVERED and PUSHED @7b71c29, `[render-gated on protocol v4]`.

**Movement 1 (bow shocks + magnetosphere nest) COMPLETE** (v24). `[per chain]`

**Movement 2 (pole-frame consumers) COMPLETE pending one gate:** rotation-axis
primitive (11 bodies, v26) and dipole cones (Uranus/Neptune, v27) done; the
v27 "animation gap" resolved -- center bodies confirmed O4 (June 10), and
NON-center bodies now animate via the Phase-3 engine (Session B). The
bow-shock hover disclosure remainder was delivered in Session C
`[render-gated C5]`.

**N15 ring-plane migration COMPLETE** (v25). `[per chain]`
**Analytical moon-orbit retirement DONE** (v25). `[per chain]`
**Provenance Tier-1 = 0** -- RE-CONFIRMED June 11 post-campaign
`[verified @d9460e2: PROVENANCE_AUDIT.md, 109 files scanned, 497 findings,
Tier-1 FIX NOW = 0]`. The clean mark held through the entire animation
refactor.

---

## C. RECONCILED LEDGER -- DONE (closed; for the record, do not re-do)

From v23 DONE table (closed by D1/D2/D3.1/C1; `[per chain]`):
1 Sun config extraction; 4 sun_position wiring (static); 10 double sun direction
indicator; 11 Earth/Jupiter magnetic_tilt_deg; 12 Neptune poles -> square-open;
14 Neptune debug print; 15 Neptune function-local imports; 16 Venus hover text;
25/42 Mars magnetosphere info marker; 27 hover \n -> <br>; 29 Sun call-site
switchover; 31 sun/corona Tkinter format; 32 Sun marker borders; 33 photosphere
mesh3d; 34 photosphere hover truncation; 35 corona_from_distance retired; 43/44
Uranus/Neptune magnetosphere hover truncation; 45 Neptune radiation labelling;
46 Neptune FAC labelling; 47a/47b Neptune arc / Lassell+Arago superimposed;
48 Mercury sodium-tail sun_position; 50 sun-direction per-body legendgroup;
54 hovertext/legendgroup sweep; 55 solar shell naming; 56 crust/cloud
legendgroup; 57 Neptune double-leader; 58 MAPS placeholder legendgroups;
59 create_neptune_magnetic_poles orphan; 60 Moon Hill Sphere prefix;
N1 osculating-marker "color not defined"; 36/39 Neptune/Uranus provenance Tier-1
display strings; 53 Neptune magnetic-center marker -> square-open;
N2-orphan Uranus dipole SIGN closed by convention.

Closed SINCE v23 (Movement chain + verified):
- **24 Bow shocks (all 8)** -- DONE (v24). **Magnetosphere nest sizing** -- DONE
  (v24). **U3 Uranus 105-deg fudge** -- RETIRED `[verified @76c330e]`.
  **N15 ring-plane migration** -- DONE (v25). **Analytical moon-orbit
  retirement** -- DONE (v25). **Rotation-axis primitive** (11 bodies) -- DONE
  (v26). **N13 dipole sweep-cone** -- DONE (v27). **N12 pole markers** -- DONE
  (June 7). `[all per chain unless tagged]`
- **Double 'Sun' in the center dropdown** -- DONE `[verified @730b2bf, L9296]`.
- **Duplicate 'Sun' key in CUSTOM_SHELLS** -- DONE `[verified @730b2bf via AST]`.
  (Full root-cause narratives for both retained in the June-8 entry of the
  prior ledger edition; reachable in git history.)
- **21/51 PHASE 1** (frame fence + sun threading + first-frame sync) -- DONE
  `[render-confirmed Mode 5 @7977a11, June 10]`. P1 4818->271 KB (94.4%),
  P2 5133->593 KB (88.4%); Sun Direction indicator un-suppressed in
  animations; magnetotail oriented at frame 1. Companion artifacts in repo:
  measure_animation_html.py, ANIMATION_TEST_PROTOCOL (v4 current).
- **21/51 PHASE 2 (2a-2d)** -- DONE `[render-confirmed Mode 5, June 10-11]`.
  One canonical center-body marker (add_celestial_object via
  add_center_body_marker); explicit blocks deleted in BOTH pipelines; one
  sun-position producer (resolve_shell_sun_position); one center-shell
  dispatch (add_center_body_shells); one shell-vars map
  (get_planet_shell_vars_map, replaced three copies); osculating params
  threaded through marker hover. Net -36 lines. P2-7 correction recorded:
  barycenters render as open squares with full hover + legend, correct
  as-is (the transparency-suppression expectation in the checklist was
  wrong, not the code).
- **N3 center-marker double** + **O5 animate bare hover** + **O6(a) animate
  no-marker-with-shells** -- CLOSED by Phase 2a (one disease: two marker
  mechanisms in static, one in animate, no canon). `[render-confirmed]`
- **D.Structural 3: create_planet_visualization RETIRED** -- DONE
  `[render-confirmed via Session A gate, June 10]`. THREE call sites swapped
  to the unified dispatch (NOT one -- the prior "one-site" ledger claim was
  wrong; corrected by repo-wide grep June 10); non-center sites now pass the
  TRUE center_object (the wrapper's own promised Phase-D correction;
  live-characterized identical). Wrapper annotated dead; deletion rides
  D.Structural 6. helpers' dead import joins D.Structural 5/6.
- **21/51 Phase 3 SESSION A** (3a notices + retirement + design doc +
  measurement harness) -- DONE `[render-confirmed Mode 5, June 10]`.
  Rebuild-as-universal adopted (ANIMATION_ENGINE_DESIGN_v1.md); gate 5(a)
  bytes PASSED: reduced magnetosphere composite 62.4 KB/f -> 1.81 MB @29f
  (envelope un-reduced; ~1.4 MB after the create_magnetosphere_shape
  producer promotion). measure_perframe_elements.py in repo.
- **21/51 Phase 3 SESSION B** (per-frame engine; axis + dipole cone +
  sun-direction indicator riding non-center bodies; greyed-legend
  disclosure) -- CONDITIONALLY render-confirmed June 11 @e5fd86d. Engine
  architecturally sound (allocation, rebuild, budget guardrail, stability
  assert all confirmed); riding visually confirmed at planet-centered scale
  (B3: Sun's axis rides the Sun marker); solar-system-scale visual gap is a
  TOOLING item (camera tracking -> item 19), not an engine defect.
  Greyed-legend (`visible='legendonly'` + legendrank + italic note)
  ACCEPTED (B4); click wart acceptable. 14 per_frame registry tags.

---

## D. RECONCILED LEDGER -- OPEN

### D.Movement -- Movement-track open items

- **Mercury +0.2 R_M northward dipole offset** -- OPEN. (Anderson 2011;
  v24 Movement-2 item.) `[verified absent @76c330e]`
- **Bow-shock hover disclosure remainder** -- DELIVERED Session C
  `[render-gated C5]`: U+N bow-shock hovers now carry the conic-model
  sourced-vs-schematic note + the animation-freeze line (this also closes
  the Phase-1 orientation-freeze disclosure rider and the frame-1-freeze
  rider -- one sweep, three siblings, as designed). MOVE TO C on the v4
  gate pass.
- **v24 sec5 precision batch** (low-risk): inner-four bow-shock hover km/AU
  `[verified @76c330e]` (also section E); Jupiter compressed/expanded MP
  toggle; Earth MP/BS citation upgrade; per-body shock eccentricity.
  `[per chain]`
- **Envelope -> dipole tie / season-derived roll** (Mode-7, conditional);
  **dipole offset DIRECTION** (Mode-7; apex stays centered until sourced);
  **REMAINING DIPOLE CONES** (verified set, June 13 @33aac56): the cone
  exists on Uranus + Neptune (done -- the dramatically tilted/offset
  dipoles, where the swept envelope matters most). Of the eight bodies
  with a magnetosphere, the candidates still WITHOUT a dipole_cone, on
  physics, are Earth, Jupiter, Mercury (genuine tilted/offset global
  dipoles -- Tony's named set) plus Saturn (MARGINAL: dipole aligned to
  <1 deg of the spin axis, so the swept cone is near-degenerate; earns the
  element only weakly). EXCLUDED on physics: Mars (crustal fields, no
  global dipole) and Venus (induced magnetosphere, no internal dynamo).
  PROVENANCE GATE unchanged: all dipole tilts are currently RECALLED and
  MUST be sourced before any PLANET_DIPOLE entry (Fetched-vs-Recalled) --
  show the envelope, but the tilt that SETS it must be cited, not
  remembered. **per-body half_len_frac tuning** (Mode-5 knobs).
  `[verified set @33aac56]`

### D.Priority -- real bugs

- **`[KEPLERIAN POS] Could not parse epoch date` with 'osc.' suffix**
  -- FIXED in Phase 4 (June 12) `[render-gated]`. The apsidal_markers
  chain gained the missing '%Y-%m-%d %H:%M' form (the suffix WAS being
  stripped; the HH:MM format was not in the chain). The fix uncovered
  the worse half: FOUR sites in palomas_orrery.py used the same broken
  chain with a SILENT J2000 fallback -- a wrong-position failure, not
  console noise. All four now route through _parse_osc_epoch (one
  producer, three formats) with a loud [EPOCH] note before any J2000
  fallback. Smoke-tested (all three Horizons forms + garbage -> None).
- FIXED in pass C2 (June 11, `[render-gated v4.1]`), three v4 blockers:
  * **C2a frame-1 comet doubling** -- the pre-existing frame-1 tail
    block AND the engine both added the comet's traces (incl. the
    builder's own Sun Direction). Fix: frame-1 block skips
    engine-owned comets (opt-in on, non-MAPS); the engine's
    allocation IS frame-1 content.
  * **C2b/C2c vanishing tail/indicator** -- STICKY-VISIBLE MERGE:
    Plotly applies frame traces as a MERGE; builders omit 'visible',
    so a slot once dummied to visible=False never reappeared. Tails
    filled previously-dummied slots exactly at perihelion; the
    indicator reshuffled into a dead slot when variable counts grew.
    Fix: EXPLICIT visible on every slot write (normalizer); the
    missing-position branch now writes explicit dummies + a console
    note (was a silent blanking). LESSON: frame updates are merges --
    any property a builder omits inherits the slot's history; padding
    slots with invisible dummies REQUIRES explicit visibility on
    every later write.
  * **C6d Mercury-centered Sun tracking** -- the engine excluded the
    center body entirely, but a centered body's SUN-DIRECTION
    elements must track the Sun moving around it; frame-1 freeze
    there is a physics lie. Fix: get_center_engine_elements() is the
    single source of truth -- the dispatch SKIPS that set
    (skip_elements threading, static unaffected, regression-tested
    identical) and the engine adds matching center_fixed specs
    (origin position, per-frame Sun). Inertial elements (axis, cone)
    correctly stay frozen. The B3-bonus barycenter Sun-Direction bug (indicator
  pointed at (0,0,0)/the barycenter when the Sun checkbox was off) was FIXED
  in Session C `[render-gated C1]`: the engine resolves a REAL Sun trajectory
  (fetching it when unchecked) and SUPPRESSES sun-direction elements when
  unresolvable -- it never points at a placeholder. Root cause for the
  archive: a fallback value is a CONTRACT -- (0,0,0) was a rotation-skip
  sentinel to shell-orientation code and literal position data to the
  indicator; reusing a fallback without checking each consumer's semantics
  is how a sentinel becomes a physics bug. Suppression beats fabrication.

### D.Structural -- dead-code / honest shell files (Phase 3)

`[per v23/v25 chain unless tagged]`
- 2 Asteroid belt migration decision.
- 5 _info import cleanup (~89+87 imports, 2 files) -- hover_text_sun import
  (L208) unused since Phase 2a; the helpers' create_planet_visualization
  import unused since Phase 2.5. Both join this sweep.
- 6 Archive dead shell functions (v9 detail in prior edition / git history);
  NOW ALSO: the retired create_planet_visualization body itself
  (annotated RETIRED June 10; delete here with grep-confirm).
- 7 Tooltip rewiring globals() -> config fields. 8 Dead
  create_sun_direction_indicator imports (verify remainder). 13 Neptune ring
  info-marker rotation (VERIFY+close). 26 CUSTOM_SHELLS tooltip verification.
  28 Neptune superimposed info markers (VERIFY+close). 40 Asteroid belt
  hover -> single info marker. N2 Saturn/Uranus ring marker placement.
  N4 Planet 9 sphere n=50 -> 20/25. N7 reduced to custom-geometry inline
  markers only. 9 palomas_orrery_helpers.py CRLF -> LF. 61 Platform
  Neutrality (SystemButtonFace).
- (NEW June 11) ASCII-convention violation, pre-existing: 3 em-dash lines in
  comet_visualization_shells.py MAPS strings (L257/505/519)
  `[verified @0ce1e26]`. Fix on next touch of that file (binary-mode).
- v25 D3 dead-code annotations + small-body analytical tail. `[per chain]`

### D.Cosmetic -- polish (bundle when convenient)

- 17 GEO info-marker position. 18 Uranus gossamer ring visibility.
  41 Sun legend ordering (ordered dispatch iteration; no manual fix).
  `[per chain]`
- Comet plotted-period trace visibility (line weight/color; O6b June 10).
- Center-body hover "Distance to Center Surface: -<radius> km (below mean
  datum)" (formatter treats center as object-at-zero; pre-existing; polish
  target is format_detailed_hover_text).
- Solar shell hovertext uses '<br>' where '\n' renders (or vice versa;
  context-specific -- C6b finding, June 11). Fix in the affected
  formatter on next touch.
- O11 verdict June 11: greyed-legend display names derive correctly from
  checkbox keys -- NO item needed; recorded so it is not re-raised.

### D.Feature -- Bucket A (near-term)

- 23 Earth ionosphere shell. `[per chain]`
- **19 Plot-cube control parity + SCALING/CAMERA COMPREHENSIVE REVIEW** --
  JOINED / cross-repo. The original parity scope (scene_axis_range,
  scene_dtick, aspectmode, camera orientation, axes/grid toggles; Studio
  side `[verified @2f40d9d]`; design authority 3d_axis_control_handoff.md)
  PLUS, per Tony's June-11 framing call, the accumulated scaling/camera
  FIXTURE LIST (all scaling work lives here; no separate session track):
    * Photosphere auto-scale collapse (static Auto = shell extent alone,
      hiding orbits; Session-A Finding 1 concrete case).
    * Sun-Direction indicator clipped by cube range (Finding 1 / O12)
      -- FIXED in Phase 4 (June 12) `[render-gated]`: geometric clamp in
      create_sun_direction_indicator (ray-cube exit along the sun
      direction, 0.95 margin, min_scale floor wins); axis_range threaded
      through the unified dispatch (Manual scales only -- Auto widens to
      2x shell extent AFTER the dispatch, so the incoming range would
      over-clamp) and into both engine indicator specs via a
      collect-time range hint (the animate pipeline's orbital-derived
      Auto range CAN undercut the shell-scaled length -- the O12 case).
      No-range path byte-identical (smoke-tested).
    * Sun orbit around a planet center lacks cube buffer (O12).
    * Fly To zoom limit ignores shell extent (computed from orbital
      distance/marker size; planets stop too far out to see magnetosphere
      or belts; comets okay). (O13b, June 11.) RESOLVED (Phase 4 render-
      gate, June 13) `[render-confirmed Mode 5]`: window sizing replaced
      the body-radius multiple with the LARGEST ACTIVE element's MEASURED
      extent -- traces_extent_from_center() (shared_utilities) is the one
      producer; the static dispatch records fig._body_element_extent_au per
      body and the per-frame allocator records _perframe_body_extent, and
      BOTH the camera-tracking window and add_fly_to_object_buttons
      (new target_extents param) consume it. Sodium tail on -> window
      opens to ~0.20 AU to hold the whole 10,003-radii tail; tail off ->
      collapses to ~0.002 AU on the magnetosphere (Tony's call: largest
      active element sets the size). The empty-box Fly To is gone.
    * CAMERA TRACKING across animation frames -- IMPLEMENTED in Phase 4
      (June 12) and RENDER-CONFIRMED in the Phase 4 render-gate session
      (June 13) `[render-confirmed Mode 5]`. The view window translates
      with the body while the camera stays FREE (the user can orbit during
      playback). UI: 'Camera: track body across frames' combobox in the
      Per-frame elements group; requires redraw=True (already set).
      MECHANISM CHANGE (June 13 live fix): per-frame go.Frame(layout=...)
      scene ranges are UNRELIABLE for a 3D scene when the window is tiny
      relative to the body's offset from origin -- Plotly silently drops
      the per-frame range and autoranges the whole Sun-body span (the
      sodium-tail-off case: a 0.0045 AU cube 0.42 AU from origin swung to
      ~0.4 AU and went non-uniform; the body also rendered off-center and
      effectively invisible). FIX: save_utils._inject_camera_tracking
      injects a post_script that applies the body-centered window via
      Plotly.relayout on load (centers the body) and on every
      plotly_animatingframe (holds the window) -- the documented-reliable
      path for driving a 3D scene during animation; data stashed as
      fig._track_relayout_data keyed by frame date. Routes through
      _write_html so it reaches BOTH the browser-opened and the saved
      offline file (saved round trip render-confirmed). The frame.layout
      path is kept as a no-JS fallback; the relayout runs after the frame
      and wins. This IS the JS event-based follow-on the prior RESIDUAL
      parked (ADDENDUM_phase4 amendment C) -- now built.
      RESIDUAL (OPEN -- item 1 attempted June 13, RENDER-FALSIFIED, then
      REVERTED): dropping the scene from frame.layout (frames data-only, JS
      as sole per-frame window owner -- item 1) did NOT make the cube
      uniform. The render still showed the cube differing BY AXIS and
      swinging ~0.15-0.65 AU -- essentially unchanged. So the frame.layout/
      JS conflict was NOT the cause; the render caught the wrong diagnosis.
      Item 1 was pushed (373298d) then REVERTED (frame.layout restored),
      because it bought nothing and cost the large-window partial-hold plus
      the no-JS fallback -- the reverted 33aac56-equivalent behavior is the
      better baseline. REFINED DIAGNOSIS (next-session seed, NOT verified):
      Plotly re-autoranges the 3D scene per frame when frames carry data
      without an explicit range, overriding the JS relayout -- the cube
      differs by axis (autorange fits the asymmetric sodium tail per axis)
      and swings as the tail rotates. SUPPORTING EVIDENCE (console): track
      half-width 0.19612 AU (relayout target ~0.39 cube), but the swing's
      upper bound (~0.65) matches the static auto-scale "+/-0.606714 AU"
      full-orbit autorange -- the scene drifts toward the data-extent
      autorange. CENTERING still holds (relayout midpoint right); only
      SIZE/uniformity is uncontrolled. COSMETIC: Tony judged the wobble
      "not a visual problem"; load-bearing behavior (centering, shell-track,
      saved round trip, reticle) all render-confirmed. DEFERRED to a
      dedicated session with a repro that ACTUALLY RUNS in Tony's browser
      (prior two did not). Won't-fix (accept the wobble) is a legitimate
      close if autorange can't be cleanly suppressed during 3D frame
      animation.
      RETICLE (June 13) `[render-confirmed Mode 5]`: the center '<>' marker
      (a hand-aligned screen-space paper-coord annotation borrowed from the
      star viz, never pixel-exact) is suppressed under camera tracking via
      add_look_at_object_buttons(show_target_marker=_track_body is None) --
      at shell scale with one body there is nothing to disambiguate, and
      the eyeball error shows. Kept in all non-tracking and static views.
    * Directional arrow camera controls for Plotly 3D (Studio has 2D
      D-pad pan; no 3D equivalent) -- precise cameras without the
      mouse; aids shell-scale visual verification. (Promoted June 11.)
    * O16: auto-scale max() Sun-centered case PASSED (C6a, June 11);
      Mercury-centered case retests in v4.1 after the C6d fix.
- (June 14 DESIGN, no code) Orrery-side axis control (item 19.3) scoped +
    handed off: HANDOFF_item19_axis_control_orrery_v1.md, built on 1288b51 /
    gallery 2f40d9d. DECISION (a2): scene-dict extraction only (axes +
    aspectmode + camera + domain, verified byte-identical across the 5704/7940
    twins); layout envelope (title/annotation/legend/margin/footer) NOT merged
    -> divergence-audit seed (4 catalogued divergences in the handoff). Full
    function-body merge stays off the list. FINDING: _track_axis (7652) is
    already the complete, correct spec (range + autorange=False + dtick +
    styling); the two MAIN paths (5704/7940) under-specify (no dtick /
    autorange) -- THAT is the close-approach unreadability. Feature =
    generalize the track spec to the under-specified sites via
    build_scene_axes/build_scene, dtick from the SHARED
    visualization_utils._calculate_grid_dtick (provable Studio parity). Q2:
    auto-only first cut (auto dtick + non-Sun-center range autofit IF the
    existing range logic doesn't already fit extent); user GUI fields = fast
    follow. Q3 matrix: range never overrides S3(exoplanet)/S4(track); dtick
    lands on S1/S2 first; S4 already correct. Two-phase: P1 byte-identical
    extraction (Mode-5 zero-change gate), P2 turn on dtick+range (Apophis
    render gate). Confirm-at-impl: read get_improved_axis_range /
    get_animation_axis_range (range-autofit scope), _track_dtick source
    (parity routing), Studio round-trip (no double-apply).      
  20/N5 shell-resolution GUI control (enabler; its backend partially exists
  since Session A -- bow-shock conic already parameterized, sphere-shell
  n_points per-config; remaining: create_magnetosphere_shape promotion +
  per-body density literals). 49 Fly-to view scaling (folds into the
  fixture list above). View-window design (49 + 19 + Studio parity).
  `[per chain unless tagged]`

### D.Feature -- Bucket B (editorial; open-ended) `[per chain]`

- 22 Satellite internal-structure shells. N14 Miranda inclination tooltip.
  Deeper-detail direction (20/N5 is the on-ramp).

### D.Feature -- Bucket C (architecture; design-before-code)

- **N6** Studio encounter-generator refactor + Artemis preset redo (coupled,
  TWO repos; full verified specifics in the prior edition / git history;
  design authority ENCOUNTER_EXPORT_HANDOFF_v3.md, orrery repo). N11 rides.
  `[per chain + @2f40d9d/@730b2bf verifications]`
- **N10** Note-composition structural refactor (behind N6). `[per chain]`
- **21/51 Animation track -- CORE COMPLETE pending the v4 gate. Status
  June 11:**
  - Phases 1, 2, 2.5, 3A DONE; 3B conditionally confirmed (section C).
  - **PHASE 3 SESSION C -- DELIVERED + PUSHED @7b71c29,
    `[render-gated on ANIMATION_TEST_PROTOCOL_v4]`:** barycenter Sun fix
    (engine Sun contract: real trajectory / engine fetch / suppression --
    never a placeholder position); console-spam fix (O13a; quiet rebuilds,
    builder messages print once at allocation, zero builder edits); comet
    tails per frame as OPT-IN (Animation Settings checkbox, default off
    per O1; build_comet_tail_traces capture shim, the 240-line builder
    unchanged; VARIABLE-COUNT handling: per-frame max-probe + pad-to-max
    with invisible dummies -- live counts are non-monotonic, 9/7/5/6
    measured; MAPS excluded, disclosed); Mercury sodium tail as engine
    customer (checkbox-gated; its greyed placeholder skipped when live);
    U+N bow-shock hover disclosure (D.Movement remainder); one-line
    auto-scale (Auto cube = MAX of orbital and center-shell extents, never
    shell alone -- the Finding-1 inverse).
  - **ENGINE ARCHITECTURE (for the record):** rebuild-as-universal --
    builder(**frame_context) through the same dispatch convention as
    static; registry = 14 per_frame tags in CUSTOM_SHELLS + the indicator
    builtin; trace-count stability asserted loud, variable-count elements
    pad-to-max; engine Sun contract with suppression-over-fabrication;
    quiet rebuilds; live byte-budget guardrail (warn >150 KB/frame).
    Design authority: ANIMATION_ENGINE_DESIGN_v1.md (sec 8 footnote
    superseded by the greyed legend -- amend on next touch).
  - **REMAINING RIDERS after the v4 gate:**
    * Resolution-sweep follow-on: RESOLVED BY MEASUREMENT (Phase 4,
      June 12, ADDENDUM decision 3). The 7-decimal coordinate-rounding
      lever (PERFRAME_COORD_DECIMALS, applied at the build_perframe_traces
      chokepoint -- every engine element inherits it) roughly HALVES
      per-frame bytes: Earth magnetosphere FULL 133->68 KB/f, Jupiter
      FULL 79->43, sodium tail 46->31 (live-measured; decimal places are
      scale-safe at any heliocentric distance, unlike significant
      digits). Full-resolution geometry + rounding fits the per-body
      budget, so NO density reduction ships: gate 5(b) is moot in its
      original form (nothing reduced to judge), and the per-body density
      literal sweep is CLOSED AS NOT NEEDED (reopen only if multi-
      magnetosphere or 60-frame budgets bite in practice; all eight
      simultaneously measure 411 KB/f rounded -- the >150 guardrail
      warns correctly). create_magnetosphere_shape n-parameter promotion
      DONE (defaults byte-identical; doubles as 20/N5's backend).
    * measure_animation_html.py: add tkinter file-browser dialog (B5).
    * Camera tracking -> item 19 fixture list (above): IMPLEMENTED.
    * O14/O15 incoming from the v4 gate: comet-tail legend churn verdict;
      sodium particle count in per-frame mode (knob exists, 500 -> 250
      measured ~24.9 KB/f -- note rounding now takes 500 to ~31 KB/f,
      which may settle O15 without the knob).
  - Standing instruction kept: when deferring, smoke-test the animate
    pipeline to a KNOWN state.

### D.Parked (Tony's explicit call) `[per chain]`

- N8 Comet info-marker superposition cluster. N9 white -> red orbit-marker
  switch (osculating marker intentionally stays white).

### D.Loose end to reconcile `[per chain; not re-verified]`

- Uranus pole-value prose inconsistency (Dec -15.10 load-bearing vs stray
  prose -15.18; reconcile when next in the file).

---

## E. AU-CONVENTION COMPLIANCE CLUSTER (standing convention; one sweep)

- Inner-four bow-shock hover ("radii" only) `[verified @76c330e]`; GEO
  altitude hover missing AU `[per standing convention]`; confirm km+AU on
  any new hover at add time. (Session C's U+N bow-shock disclosure lines
  added no new numbers; existing km/AU values untouched.)

---

## F. CONSOLIDATION LOG (what each pass repaired)

- (June 7, v28 consolidation) RESTORED 2 leaked Movement-2 items + the v24
  sec5 batch; corrected the stale U3 "open"; UNIFIED the three animation
  records into 21/51; closed N13, N12; recorded Q2; moved Food Insecurity
  to a separate track; HEAD verifications. (Full detail: prior edition /
  git history.)
- (June 8) Recovered the N6 generator-refactor leak; recorded the two-repo
  coupling; Gallery section H stood up.
- (June 10) ANIMATION PASS 1: Phase 1 render-confirmed; Phase 2 delivered;
  PENDING June-8 items verified at HEAD and cleared; center-marker
  divergence root-caused (N3 + O5 + O6a = one disease); v27 axis/cone gap
  refined to non-center-only (O4); animate shell auto-scale found dead and
  annotated; new items from the O-log.
- (June 10, later) Phase 2 render-confirmed; Phase 3 GO (rebuild-universal
  directive); Session A delivered: the "one-site" wrapper claim CORRECTED
  by repo-wide grep (three sites); budget harness + gate 5(a) passed;
  grep -c chain-break lesson.
- (June 11, fix pass C2) v4 first run found 3 blockers; all root-caused
  with reproduction, not patched on guesses: the perihelion repro
  EXONERATED the engine math and convicted Plotly's frame-merge
  semantics (sticky visible); the doubling was two producers of one
  element (frame-1 block + engine); Mercury-centered was a coverage
  gap, not a trajectory bug (Tony's barycenter-class instinct pointed
  the way; the trigger differed). skip_elements threaded through the
  dispatch with a None-default regression test (HEAD-identical).
  Promoted: epoch-parser 'osc.' gap (D.Priority), <br> hovertext
  (D.Cosmetic), 3D arrow cameras (item 19).
- (June 11) Sessions B + C: engine delivered and conditionally confirmed
  (solar-system-scale visual gap identified as TOOLING -> item 19 with the
  go.Frame camera mechanism note); greyed-legend disclosure verified and
  accepted (supersedes the footnote; console notices demoted to dev
  diagnostics); B3-bonus barycenter bug root-caused (sentinel conflation:
  a fallback value is a CONTRACT) and fixed with
  suppression-over-fabrication; comet trace counts measured non-monotonic
  -> pad-to-max; capture-shim pattern adopted for the comet core (faithful
  by construction, hairy builder untouched); O13a spam fixed engine-side;
  scaling consolidated into item 19 per Tony's framing call (no separate
  track); section-G auto-scale and tier-decision questions CLOSED;
  provenance re-scan at d9460e2: Tier-1 = 0 held through the campaign.
- (June 14) Item 19.3 design session: SHA round trip verified (orrery 1288b51,
  gallery 2f40d9d); map-confirmed 4 scene sites (2 twins / 2 variants, prior
  3-site grep was stale); seam decision (a2) + Q2/Q3 settled; handoff drafted.
  No code. Divergence-audit seeded.
---

## G. OPEN QUESTIONS / TONY CALLS

- AU-convention sweep (section E): KEEP OPEN, revisit (Tony, June 7).
- **Gate 5(b)** RECAST (June 12); RENDER-CONFIRMED (June 13) `[render-
  confirmed Mode 5]`: full resolution ships, rounded. Tony's June-13 pass
  on live Mercury data confirmed (1) animated magnetosphere correct (tail
  anti-sunward across frames, no seam/flicker at d7 rounding); (2) camera
  tracking frames the active elements (element-extent window: tail opens
  it, magnetosphere tightens it); (3) tracked playback centers steadily on
  the body (cube-size wobble noted acceptable, see camera-tracking RESIDUAL);
  (4) indicator clamp renders sensibly; (5) inertial-note hover wording.
  Mercury-centered AND Sun-centered-track-Mercury both confirmed; saved-file
  round trip confirmed identical to live render.
- O14/O15 verdicts arrive with the v4 gate (comet legend churn; sodium
  particle count) -- record here if either becomes an item. O15 may be
  settled by rounding (500 particles now ~31 KB/f).
- **Phase 4 residuals** (June 12): O2/O3 console notice wording is
  slightly stale when magnetosphere opt-in is ON (the blanket "not yet
  rendered" remains true for sphere shells; engine prints its own
  allocation lines) -- amend on next touch. apsidal_markers.py carries
  4 PRE-EXISTING em-dashes (platform-neutrality flag, not Phase 4's).
  MAPS per-frame wiring DEFERRED per ADDENDUM_phase4 decision 1 (the
  two-site exclusion warning and partition design are captured there).

(CLOSED June 10-11: animation Auto-scale-vs-shells -- implemented as
max(orbital, shell) in Session C, render-gated C6. Phase 3 tier decision --
tier 2 adopted at the June-10 GO; tier 1 dropped; tier 3 = the resolution
follow-on behind gate 5(b).)

---

## H. GALLERY / STUDIO TRACK (website repo; low-activity)

(Unchanged this pass; carried verbatim from the June-10 edition.)

- **Repo source.** https://github.com/tonylquintanilla/tonyquintanilla.github.io
  -- owner WITH the 'l', repo name WITHOUT; branch main; public; HEAD
  verified June 8 == `2f40d9d`; custom domain palomasorrery.com; Studio file
  tools/gallery_studio.py (NOT root). Uploaded Studio byte-identical
  @2f40d9d.
- **Docs split:** WEBSITE repo documentation/ holds web_gallery_handoff.md +
  3d_axis_control_handoff.md `[verified @2f40d9d]`; ORRERY repo
  documentation/ holds the encounter-export design set incl.
  ENCOUNTER_EXPORT_HANDOFF_v3.md `[verified @730b2bf]`.
- **No Studio running ledger** by design (stand one up only if Studio work
  resumes in volume).
- **Joined items:** N6 (Bucket C) and item 19 (Bucket A) -- tracked in their
  orrery homes, cross-referenced here.
- **Open Studio items** (May-5 handoff; checked @2f40d9d where
  file-verifiable): encounter-export mission-type testing `[per handoff]`;
  camera capture NOT extracted `[verified]`; link-icon end-to-end test
  `[per handoff]`; content re-population through the Studio `[per handoff]`;
  gallery-card thumbnails ABSENT; About/Downloads/Contact pages ABSENT;
  og:image meta present (per-card previews unconfirmed).
- **Recently closed:** _enter_orrery_mode() DEFAULT_CONFIG reset
  `[verified @2f40d9d ~L4775]`; 'ongoing' status comment
  (spacecraft_encounters.py L60, verified).

---

Module updated: June 2026 with Anthropic's Claude Opus 4.8 + Claude Fable 5
