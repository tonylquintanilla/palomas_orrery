# PHASE 1B STAGE 2 TEST PROTOCOL -- export_orbit_cache.py v4

Tony Quintanilla, PE | Claude | July 8, 2026

Scope: verify the Stage 2 data-serving export end to end -- the v4
osculating-primary model (no subtraction), the v0.6-reconciled coverage index,
and the nine-object test tranche -- from a clean desktop run through the
gallery round trip. Ledger: L-098. Companions: PHASE1B_BUILD_MANIFEST_v4.md,
PHASE1B_MODEL_CORRECTION_HANDOFF.md, PHASE1B_DATA_SERVING_DESIGN_HANDOFF.md
v0.6.

Base: orrery HEAD `d4c37cf` | gallery HEAD `4b086a6`.
New file under test: `export_orbit_cache.py` (675 lines), placed in the orrery
repo root; reads `./data/orbit_paths.json` + `./data/osculating_cache.json`.

Division of labor (per the agentic-pre-test discipline): Claude covers Syntax
+ Runtime (Part A, done in the sandbox against the real osculating cache +
synthetic positions). Tony covers Desktop Runtime + Visual + Deploy (Part B,
against the PRIMARY cache; Mode 5 is Tony's eyes). A protocol result is
recorded, not assumed -- fill the Result blanks as you go.

Model under test (one line): the orbit ALWAYS renders from osculating
elements (matched to the object's center); the direct relative-frame position
trace is ADDITIVE, served only where daily cadence closes the orbit. No
subtraction anywhere.

================================================================
PART A -- SANDBOX PRE-TEST (Claude, DONE)
================================================================
Recorded results from the pre-delivery run. These are the syntax/runtime half;
they do not substitute for the desktop run on the primary (Part B).

  [x] A1. py_compile clean; ASCII-only; LF-only on the delivered copy.
  [x] A2. Unit tests: resolve_center_slug maps both @-id and NAME forms;
          epoch parser PRESERVES HH:MM (the v3 catch); J2000 -> JD 2451545.0
          exact; TA->M0 sane at perihelion.
  [x] A3. build_osculating_entry for all 9 osculating objects against the REAL
          osculating cache: every block builds and center-matches
          (osculating.center == stored_center). Spot values (a_au * KM_PER_AU):
          Pluto@9 ~2,127 km (barycenter wobble), Charon@9 ~17,460 km,
          Moon ~383,000 km, Io ~422,000 km, Titan ~1.22e6 km; Apophis
          epoch_jd 2462236.5 == 2029-04-10.
  [x] A4. Full export (real osculating + synthetic positions): 8 position
          files (earth, jupiter, saturn, moon, titan, pluto, charon,
          voyager_1); io + apophis osculating-only; voyager trajectory-only;
          invariants #2,#3,#5,#6,#8,#C PASS.
  [x] A5. coverage_index.json field shape matches design handoff v0.6
          field-for-field (per-object 12 fields; osculating 9; positions
          {file,start,end,step_hours,n_points,size_kb}; top-level
          scene_features; the one v4 addition is a `model` note block).
  [x] A6. Position file format matches v0.6 (object, center, frame, unit "km",
          epoch_type "JD", source{query_target,center,epoch,retrieved},
          data{t,x,y,z}).

================================================================
PART B -- DESKTOP RUNTIME + VISUAL (Tony, against the PRIMARY)
================================================================

--- B0. Pre-flight (Step 0) -- RUN July 8, 2026 -----------------
  [x] `python export_orbit_cache.py --preflight-only`
      Expected: 10 pairs present, daily cadence, AU units; osculating 9/9,
      8/9 HH:MM, 0 MA=None; Step 0-STOP verdicts Io UNUSABLE, Moon/Titan/
      Charon chunky.
      Result: PASS. 1501 pair keys; all 10 present @ 1.000 d/step, AU;
      osc 9/9, 8/9 HH:MM, 0 MA=None; verdicts as expected. `[verified, primary]`

Output: 

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>python export_orbit_cache.py --preflight-only
========================================================================
PHASE 1B PRE-FLIGHT (Step 0) -- read-only diagnostics
Cache dir: C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\data
========================================================================

orbit_paths.json: 1501 pair keys

--- 0a/0c/0e: presence, key format, cadence, units ---
  Earth_Sun         8527 pts | date-only    | 1.000 d/step | 2023-10-14 .. 2047-02-17 | center=Sun
       first-pt |r|=0.9977 -> AU
  Jupiter_Sun      10595 pts | date-only    | 1.000 d/step | 2025-05-13 .. 2054-05-16 | center=Sun
       first-pt |r|=5.117 -> AU
  Saturn_Sun       10597 pts | date-only    | 1.000 d/step | 2025-05-13 .. 2054-05-18 | center=Sun
       first-pt |r|=9.6 -> AU
  Pluto_Sun        14458 pts | date-only    | 1.000 d/step | 2025-05-13 .. 2064-12-12 | center=Sun
       first-pt |r|=35.24 -> AU
  Moon_Sun           759 pts | date-only    | 1.000 d/step | 2025-05-13 .. 2027-06-11 | center=Sun
       first-pt |r|=1.005 -> AU
  Io_Sun           10595 pts | date-only    | 1.000 d/step | 2025-05-13 .. 2054-05-16 | center=Sun
       first-pt |r|=5.114 -> AU
  Titan_Sun        10597 pts | date-only    | 1.000 d/step | 2025-05-13 .. 2054-05-18 | center=Sun
       first-pt |r|=9.6 -> AU
  Charon_Sun         751 pts | date-only    | 1.000 d/step | 2025-05-13 .. 2027-06-03 | center=Sun
       first-pt |r|=35.24 -> AU
  Voyager 1_Sun      751 pts | date-only    | 1.000 d/step | 2025-05-13 .. 2027-06-03 | center=Sun
       first-pt |r|=166.7 -> AU
  Apophis_Sun        751 pts | date-only    | 1.000 d/step | 2025-05-13 .. 2027-06-03 | center=Sun
       first-pt |r|=0.8776 -> AU

--- 0b: Pluto pair -- which Horizons target? ---
  Pluto_Sun center_body=Sun horizons_id=None

--- 0d: imports ---
  constants_new.KM_PER_AU: 149597870.7
  celestial_objects.OBJECT_DEFINITIONS: 182

--- 0f: osculating cache structure ---
  osculating entries: 115
  tranche osc keys present: 9/9
  epochs carrying HH:MM: 8/9
  entries with MA=None:  0/9

========================================================================
STEP 0-STOP: moon-cadence -- orbit ALWAYS ships (osculating);
the question is whether the direct position TRACE is added.
========================================================================
  Moon    : 1.000 d/step, period 27.322 d -> ~27.3 pts/orbit [trace chunky (Mode 5)]
  Io      : 1.000 d/step, period 1.769 d -> ~1.8 pts/orbit [trace UNUSABLE (osculating only)]
  Titan   : 1.000 d/step, period 15.945 d -> ~15.9 pts/orbit [trace chunky (Mode 5)]
  Charon  : 1.000 d/step, period 6.387 d -> ~6.4 pts/orbit [trace chunky (Mode 5)]
========================================================================

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>      

--- B1. Scratch export run ------------------------------------
  [ ] `python export_orbit_cache.py`   (writes to ./_export_out -- the SAFE
      default; does NOT touch the gallery)
      Expected summary:
        position files:  8  (earth, jupiter, saturn, moon, titan, pluto,
                             charon, voyager_1)
        osculating-only: io, apophis
        invariants #2,#3,#5,#6,#8,#C: PASS
        warnings: none  (on the desktop shell_configs loads, so
                        feature_configs.json is written too)
      Result: ____________________________________________
      NOTE if `moon` or `titan` is MISSING from the file list AND a warning
      says `position pair 'Moon_Earth' missing` (or 'Titan_Saturn'): that is an
      exact-string mismatch, NOT a failure -- the object shipped osculating-
      only. Fix the key in TEST_OBJECTS (see B4) and re-run. A center mismatch,
      by contrast, RAISES (loud, aborts) -- that is a real failure to
      investigate.

Output: 
 C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>python export_orbit_cache.py
Loading caches from C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\data
Asserting invariants...
  invariants #2,#3,#5,#6,#8,#C: PASS
  feature_configs.json: 0 feature(s)

Summary
  objects:          10
  position files:   8  (earth, jupiter, saturn, moon, titan, pluto, charon, voyager_1)
  osculating-only:  io, apophis
  coverage_index.json + feature_configs.json written
  warnings (6):
    - pluto: position center 'Sun' != stored_center pluto_barycenter
    - charon: position center 'Sun' != stored_center pluto_barycenter
    - feature 'atmosphere_shell' not in SHELL_CONFIGS
    - feature 'magnetosphere' not in SHELL_CONFIGS
    - feature 'ring_system' not in SHELL_CONFIGS
    - feature 'van_allen_belts' not in SHELL_CONFIGS

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>     

--- B2. Coverage index inspection ----------------------------
  [ ] Open `_export_out/coverage_index.json`.
      [ ] schema_version "1.0"; scene_features present; model block says
          orbit_source "osculating-primary", subtraction "not-used".
      [ ] Every object has the 12 v0.6 fields.
      [ ] pluto + charon: stored_center "pluto_barycenter",
          canonical_frame "barycenter-relative", osculating.center
          "pluto_barycenter" (center-match).
      [ ] moon: stored_center "earth"; titan: "saturn".
      [ ] io + apophis: positions null, osculating present.
      [ ] voyager_1: osculating null, positions present.
      Result: ____________________________________________

--- B3. Position file spot-checks (the manifest S7 checks) ----
  [ ] `_export_out/positions/charon.json`: center "pluto_barycenter",
      frame "barycenter-relative", unit "km", epoch_type "JD"; |r| of the
      first point is km-scale, order ~1.7e4 km (NOT ~0.0001 AU).
  [ ] `positions/moon.json`: center "earth"; |r| order ~3.8e5 km.
  [ ] `positions/titan.json`: center "saturn"; |r| order ~1.2e6 km.
  [ ] `positions/pluto.json`: center "pluto_barycenter"; |r| order ~2.1e3 km
      (Pluto's small wobble about the barycenter -- the mirror of Charon).
  [ ] Any file: `data.t` are JD floats (~2.46e6), not date strings; point
      count equals the cache cadence (no decimation -- there is no
      interpolation step).
      Result: ____________________________________________

--- B4. Exact pair-key confirmation --------------------------
  [ ] Confirm the served-pair strings the tranche assumes exist on the primary:
      `python -c "import json; c=json.load(open(r'data/orbit_paths.json'));
      print([k for k in ('Moon_Earth','Titan_Saturn') if k in c])"`
      Expected: both present -> `['Moon_Earth', 'Titan_Saturn']`.
      If either is absent, note the ACTUAL key and update TEST_OBJECTS
      (position_pair_key), then re-run B1.
      Result: ____________________________________________

--- B5. Mode 5 render (VISUAL GATE -- Tony's eyes) -----------
  Load the served tranche in the renderer / a Phase 2 test page. Tony's eyes
  are the ground truth here, not the file.
  [ ] Planets (Earth/Jupiter/Saturn) heliocentric orbits render; Voyager arc
      renders.
  [ ] Moon (~27 pts/orbit) and Titan (~16) traces read as clean orbits.
  [ ] Charon + Pluto about the barycenter: ~6.4-pt hexagons -- ACCEPTABLE or
      not is Tony's call. Circle around a common center (the binary dance),
      NOT offset by ~2000 km (that would signal a body-vs-barycenter frame
      error).
  [ ] Io: orbit renders from the osculating conic (smooth ellipse), no trace.
  [ ] No orbit sits in the wrong frame (a moon's ellipse and its trace overlay;
      if they diverge, suspect a center mismatch -- but #C should have caught
      it at export).
      Result / Mode 5 verdict: ____________________________________________

--- B6. Provenance gate --------------------------------------
  [ ] Add a ROLE_MAP entry for `export_orbit_cache.py` in module_atlas.py
      (role: devtool) so the coverage-gap check classifies it (L-078).
  [ ] Run provenance_scanner.py; confirm Tier-1 = 0 for the new module
      (it imports KNOWN_ORBITAL_PERIODS rather than embedding periods, and
      carries no recalled numeric display strings, so it should be clean).
      Result: Tier-1 = ______   (target 0)   ROLE_MAP added [ ]

--- B7. Deploy round trip ------------------------------------
  [ ] DEPLOY: `python export_orbit_cache.py --output-dir
      ../tonyquintanilla.github.io/data/solar-system/`  (or copy _export_out/
      across). Add `_export_out/` to the orrery .gitignore.
  [ ] Commit + push the gallery repo. Record the pushed SHA below.
  [ ] A test page fetches `coverage_index.json` + one position file + one
      osculating-only object (io) and renders both an ellipse (io) and an
      ellipse-plus-trace (titan). Same-repo = same origin, so no CORS.
      Result: gallery pushed SHA ____________  round trip OK [ ]

================================================================
PASS CRITERIA (all must hold for Stage 2 sign-off)
================================================================
  - B1 summary: 8 position files, io/apophis osculating-only, invariants PASS,
    no unexpected warnings.
  - B2/B3: coverage index v0.6-shaped; every position file km + JD; center-
    match holds for pluto/charon/moon/titan.
  - B4: Moon_Earth + Titan_Saturn confirmed (or keys corrected and re-run).
  - B5: Mode 5 verdict recorded (Tony's eyes; hexagonal Charon/Pluto accepted
    or the trace deferred).
  - B6: provenance Tier-1 = 0 on the new module; ROLE_MAP entry added.
  - B7: deployed, pushed, round trip renders; SHA recorded.

Deferred (tracked, NOT in this protocol): Pluto-Charon relative subsystem
(Styx/Nix/Kerberos/Hydra) + fine-cadence moon traces + the 29-pt barycenter
heliocentric coverage for Phase 2 wide-view composition. Full-catalog export
(--full-catalog is tranche-scoped in this build).

================================================================
RESULTS LOG / SIGN-OFF
================================================================
  Run date:            ____________
  Orrery HEAD at run:  ____________   (expect d4c37cf or later, source-clean)
  Export files written: ____________
  Invariants:          PASS / FAIL
  Mode 5 verdict:      ____________
  Provenance Tier-1:   ____________
  Gallery pushed SHA:  ____________
  Sign-off (Tony):     ____________

Protocol written July 2026 with Anthropic's Claude Opus 4.8.
