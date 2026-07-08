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
        warnings: 4 feature-slug warnings are EXPECTED and harmless
                  (SHELL_CONFIGS is keyed by shell component, not by these
                  feature slugs -- Phase 2 rework). 2 center-label warnings
                  on pluto/charon need triage -- see B1a.
      Result: PASS (core). 8 position files (earth, jupiter, saturn, moon,
      titan, pluto, charon, voyager_1); io/apophis osculating-only; voyager
      trajectory-only; invariants #2,#3,#5,#6,#8,#C PASS. Wrote to _export_out/
      (scratch default; gallery untouched). Warnings: 2 center-label (pluto,
      charon -> B1a) + 4 feature (Phase 2, expected). [verified, primary]
      NOTE if `moon` or `titan` is MISSING from the file list AND a warning
      says `position pair 'Moon_Earth' missing` (or 'Titan_Saturn'): that is an
      exact-string mismatch, NOT a failure -- the object shipped osculating-
      only. Fix the key in TEST_OBJECTS (see B4) and re-run. A center mismatch,
      by contrast, RAISES (loud, aborts) -- that is a real failure to
      investigate.

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

--- B1a. Center-mismatch warning triage (added July 8) ----------
  Fired: `pluto`/`charon: position center 'Sun' != stored_center
  pluto_barycenter`. This is a WARNING, not the loud RAISE of a true center
  mismatch (#C PASSED). Cause: the cache's metadata `center_body` for the
  barycenter pairs is written by several orbit_data_manager paths, some
  defaulting to 'Sun' -- an UNRELIABLE label, NOT proof of the data's frame.
  The served files use the correct center (pluto_barycenter, from the tranche
  definition). The MAGNITUDE in B3 is the decider, not the label:
    - charon/pluto |r| km-scale (~1.7e4 / ~2.1e3 km) -> data is barycenter-
      relative; label is stale; export is CORRECT. Follow-up: Claude swaps the
      cross-check off the unreliable center_body field so it stops false-
      alarming (the 2 warnings then disappear).
    - |r| AU-scale (~5e9 km ~ 35 AU) -> heliocentric data under a barycenter
      key: a REAL frame problem. STOP -- do not deploy; fix the source.
  Action: proceed to B2, then let B3 settle it; carry B3's verdict here.
  Result: STOP branch confirmed by B3. charon/pluto traces are frame-
  CONTAMINATED: heliocentric points (~35 AU) for 2025-11-24..2027-01-31, then
  barycentric (correct) for 2027-02-01..2027-06-10 -- a clean split at
  2027-02-01 (434 helio + 130 bary of 564). Root cause: the cache pairs
  `Charon_/Pluto_Pluto-Charon Barycenter` mix frames (NOT an export bug; the
  center_body='Sun' warning was a true signal). Export hardened v4.1 (#F guard)
  to DROP contaminated traces to osculating-only. Cache source must be repaired
  before charon/pluto traces can deploy.

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
      [x] voyager_1: osculating null, positions present.
      Result: PASS. Verified against the ACTUAL coverage_index.json:
      schema_version "1.0"; scene_features present; model osculating-primary /
      not-used; all 10 objects carry the 12 v0.6 fields; pluto+charon
      stored_center pluto_barycenter, barycenter-relative, osc.center
      pluto_barycenter; moon earth, titan saturn; io+apophis positions null +
      osculating present; voyager_1 osculating null + positions present.
      (Index STRUCTURE is correct; the data problem is in the position DATA,
      caught in B3.)

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
  Command (Windows cmd-safe -- no % ; forward slashes are fine; run per object):
    python -c "import json;p=json.load(open('_export_out/positions/charon.json'))['data'];print('charon |r| km =',(p['x'][0]**2+p['y'][0]**2+p['z'][0]**2)**0.5)"
    (repeat with pluto, moon, titan). Expected order: charon ~1.7e4,
    pluto ~2.1e3, moon ~3.8e5, titan ~1.2e6. AU-scale (~5e9) = frame problem.
      Result: MIXED -- 2 PASS, 2 FAIL (all files km + JD, no decimation).
        moon  PASS: |r| 356,708 .. 406,683 km, center earth, 1245 pts.
        titan PASS: |r| 1,186,730 .. 1,256,999 km, center saturn, 736 pts.
        charon FAIL: |r| 17,461 .. 5.34e9 km  (first pt 5.30e9 = 35 AU).
        pluto  FAIL: |r| 2,131 .. 5.34e9 km   (first pt 5.30e9 = 35 AU).
      charon/pluto are frame-CONTAMINATED (see B1a) -> STOP. Re-export with the
      v4.1 #F guard drops them to osculating-only (6 position files ship: earth,
      jupiter, saturn, moon, titan, voyager_1). Repair the cache, then re-run.

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
  - B2: coverage index v0.6-shaped (PASS).
  - B3: every position file km + JD. moon/titan traces PASS. charon/pluto
    traces are frame-contaminated -> the #F guard ships them osculating-only,
    which reproduces the correct desktop barycenter render (B8). ACCEPTED for
    the tranche; no repair needed to sign off.
  - B4: Moon_Earth + Titan_Saturn confirmed (or keys corrected and re-run).
  - B5: Mode 5 verdict recorded (Tony's eyes; hexagonal Charon/Pluto accepted
    or the trace deferred).
  - B6: provenance Tier-1 = 0 on the new module; ROLE_MAP entry added.
  - B7: deployed, pushed, round trip renders; SHA recorded.

--- B8. Contaminated barycenter TRACE -- RESOLVED for the tranche ---
  The barycenter cache pairs `Charon_/Pluto_Pluto-Charon Barycenter` mix frames
  in their historical data_points: pre-2027-02-01 heliocentric (~35 AU),
  2027-02-01 onward barycentric (correct). BUT this does not block the tranche.
  Evidence (desktop re-plot of the Pluto-Charon Barycenter system, July 8
  17:02): the render is CORRECT -- Pluto 2131.6 km, Charon 17,463.9 km from the
  barycenter -- because the desktop draws the orbit from the @9 OSCULATING
  elements ([BARYCENTER MODE] Charon@9), not from the trace. Those values match
  the export's osculating blocks EXACTLY (pluto a_au 1.42e-5 -> 2131 km; charon
  1.167e-4 -> 17,464 km). The re-plot smart-fetched 28 clean days but did NOT
  purge the old heliocentric span, so the #F guard still drops the pluto/charon
  TRACE to osculating-only -- which reproduces the same correct barycentric
  ellipse in the browser. The chunky, contaminated 6.4-pt trace is no loss.
  RESOLUTION: pluto/charon ship osculating-only for the tranche. No cache
  repair required for Stage 2 sign-off.
  Verify: re-run the export -> pluto/charon appear under "osculating-only" with
  the FRAME CONTAMINATION warning; 6 position files ship (earth, jupiter,
  saturn, moon, titan, voyager_1); coverage_index osculating.center =
  pluto_barycenter for both.
    [ ] re-export shows pluto/charon osculating-only
    [ ] coverage_index osculating a matches desktop (2131 / 17,464 km)
  DEFERRED (only if the actual-position trace is later wanted -- it is chunky
  at 6.4 pts/orbit anyway): purge the pre-2027-02-01 points and re-plot the
  system over the full span (the desktop @9 fetch stores clean data), or
  delete + re-fetch the pairs. Check the OTHER barycenter systems
  (Orcus/Eris/Haumea, Styx/Nix/Kerberos/Hydra) for the same mix. Ledger: L-098.

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
