# LEDGER -- Orrery Refactor / Movement Track (Consolidated, Running)

Tony Quintanilla, PE | Claude | June 7, 2026 (last updated June 8, 2026)
Base SHA at consolidation: `76c330e` (76c330ea4dbe6bc667fba2ffb5baa1a65ae56d22)
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

- `[verified @76c330e]` -- checked against the live repo code this session.
- `[per chain; not re-verified]` -- carried from a handoff's prose; status is
  as the handoff stated, NOT re-confirmed against HEAD this session.
- `[render-gated]` -- correctness is a Mode-5 judgment, not settleable here.

Items with no tag are administrative (tracks, actions) rather than code claims.

---

## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; cross-referenced)

- **Food Insecurity (REOPENED, active).** Earth System track, not the orrery
  refactor. Design locked: HANDOFF_food_insecurity_design_v1.md +
  MANIFEST_food_insecurity_sudan_first_cut.md (Sudan first cut, IPC KML vector
  polygons / approach B, folders-per-period, transcribe-not-synthesize stance).
  Status: awaiting IPC Public API key (request submitted; CC BY-NC-SA 3.0 IGO
  terms reviewed and compatible with the non-commercial educational use).
  Build base will be HEAD at build time (design base was de12f56; current HEAD
  76c330e). RELEASE-DRIFT CORRECTION to fold in at build: the current Sudan
  release is Feb-May 2026 Current + projections to Jan 2027, and names NO current
  Famine areas -- so the manifest's section-10 El Fasher/Kadugli Phase-5
  spot-check (Sept 2025 picture) must be rewritten to the current classification.
- **Protocol -> Skills refactor (process/tooling, not orrery code).** v27 idea:
  split the trigger-fired PROCEDURE layer (docstring standard, agentic pre-test,
  provenance-scanner mechanics, single-info-marker pattern, Horizons center rules,
  bottom-up / binary-mode editing) into Anthropic skills, keep the resident
  JUDGMENT layer (modes, criticality philosophy, Foundation, "when unsure ask",
  double-helix) in context. CAUTION: CRITICAL gates (SHA round trip,
  verify-execution, enumerate-uploads) must fire reliably -> stay resident or keep
  a one-line resident pointer; only QUALITY/PRACTICE mechanics are safe spin-offs.
  Its own sketch-first session: design which skills + triggers before building.

## PENDING ACTION (Tony-side)

- **Commit protocol v3.28 to the repo root.** v3.28 exists in the working copy /
  project instructions but has NOT been pushed (Tony confirmed: no new files
  pushed to root yet). Until pushed, the doc and its version stamp have not
  travelled together; the repo root still carries the prior protocol file.
- **Push the June-8 cleanup fixes** (working-copy done, verified, not yet pushed):
  `palomas_orrery.py` (center-dropdown Sun dedup) and `shell_configs.py`
  (duplicate-`'Sun'`-key block deleted + live Sun header revised). On push, the new
  HEAD becomes the next base; carry the new SHA in the next handoff.

---

## B. STRATEGIC STATUS

**The shell-consolidation refactor is COMPLETE** (per v23 headline; all 13 bodies
route through SHELL_CONFIGS / CUSTOM_SHELLS -> create_celestial_body_visualization
-> build_sphere_shell -> create_info_marker; zero bodies on the old
create_planet_visualization / create_sun_visualization paths). The project is in
cleanup-and-close, not mid-refactor.

**Movement 1 (bow shocks + magnetosphere nest) COMPLETE** (v24): one shared
conic-section create_bow_shock_shape; all 8 bodies; magnetopause nest corrected
on the Earth-scaled bodies (Mercury/Venus/Mars/Jupiter/Uranus). `[per chain]`

**Movement 2 (pole-frame consumers) IN PROGRESS:**
- Rotation-axis primitive -- DONE across 11 bodies (v26). Static render confirmed
  Sun/Mercury/Earth. `[per chain]`
- Dipole cone -- DONE for Uranus (60 deg, Ness 1986) + Neptune (47 deg, Ness 1989)
  (v27). Static render confirmed. `[per chain]`
- Remaining Movement-2 items: see D.Movement below.

**N15 ring-plane migration COMPLETE** (v25): all ring systems + Saturn torus +
belts orient by IAU pole via orient_to_planet_pole. `[per chain]`

**Analytical moon-orbit retirement DONE** (v25): Jupiter + Mars analytical path
removed from live dispatch; all major-planet moons osculating-only. `[per chain]`

**Provenance Tier-1 = 0** achieved (v18). `[per chain]`

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
N2-orphan Uranus dipole SIGN closed by convention (comment at load-bearing site).

Closed SINCE v23 (Movement chain + verified):
- **24 Bow shocks (all 8, incl. ice giants)** -- DONE, Movement 1 (v24). `[per chain]`
- **Magnetosphere nest sizing** (Mercury full rescale, Venus, Mars, Jupiter,
  Uranus) -- DONE (v24). `[per chain]`
- **U3 Uranus belt/ring 105-deg fudge** -- RETIRED; belts (L732) and rings
  (L1097) now orient via orient_to_planet_pole. `[verified @76c330e]`
  (NOTE: the June-1 erratum recorded this as "NOT STARTED / still live"; that text
  is SUPERSEDED. Do not re-open from the erratum.)
- **N15 ring-plane migration** (Jupiter / Saturn+torus+belts / Neptune; Uranus was
  the v23 anchor) -- DONE (v25). `[per chain]`
- **Analytical moon-orbit retirement** (Jupiter, Mars) -- DONE (v25). `[per chain]`
- **Rotation-axis primitive** (11 bodies) -- DONE (v26). `[per chain]`
- **N13 dipole rotation sweep-cone** -- DONE as the v27 dipole cone (Uranus 60 /
  Neptune 47). `[per chain]` This closes the v23 Bucket-B N13 item.
- **N12 planet N/S pole markers** -- DONE (Tony-confirmed, June 7). Closes the
  v23 Bucket-B N12 item.
- **Double 'Sun' in the center-object dropdown** -- DONE (render-confirmed Mode 5,
  June 8). NOT a duplicate dict key: update_center_dropdown (palomas_orrery.py
  ~L9292) built `new_options = ['Sun'] + ordered_centers`, and 'Sun' also enters
  ordered_centers (numeric Horizons ID passes can_be_horizons_center; it is the
  default center, so the keep-the-shadowed-center logic retains it) -- so it listed
  twice in every selection. Fix:
  `new_options = ['Sun'] + [name for name in ordered_centers if name != 'Sun']`.
  `[render-confirmed Mode 5; working copy, pending push]`
- **Duplicate 'Sun' key in CUSTOM_SHELLS** (shell_configs.py, L2642/L2823) -- DONE
  (verified @working-copy, June 8). Confirmed real via AST (two top-level 'Sun' keys;
  last wins). Dormant, NOT a live render bug: the dropped L2642 block was a stale
  sphere-shell duplicate of SHELL_CONFIGS['Sun'] (same 15 keys, served via the sphere
  path); the surviving L2823 block holds the correct custom geometry (rotation_axis,
  hills_cloud_torus, outer_oort_clumpy, galactic_tide). Fix: deleted the dead
  L2631-2811 block (its comment header + the sphere-shell copy) and revised the live
  SHELL_CONFIGS['Sun'] header (dropped stale "not yet invoked" / "stays alive" /
  "switchover" notes; Source/Verified provenance preserved verbatim). Verified in the
  uploaded copy: one 'Sun' key, 4 custom sub-keys, SHELL_CONFIGS['Sun'] intact at 15,
  py_compile clean, ASCII, one provenance copy. (The prior entry's line numbers were
  correct but never named the file -- it is shell_configs.py, not palomas_orrery.py.)
  `[verified @working-copy; pending push]`

---

## D. RECONCILED LEDGER -- OPEN

### D.Movement -- Movement-track open items (restored from v24-v27)

- **Mercury +0.2 R_M northward dipole offset** -- OPEN. v24 Movement-2 item
  (N-S asymmetry, large exposed southern cusp; Anderson 2011). Translate the
  magnetosphere + shock shell north 0.2 R_M; subsolar standoff stays 1.45.
  `[verified @76c330e]` -- confirmed ABSENT in mercury_visualization_shells.py
  (only the cosmetic tail-marker offset and the standard sunward-recenter exist).
  LEAK RECOVERED: present in v24's Movement-2 queue, dropped from v26/v27 ledgers.
- **Bow-shock / envelope honesty -- CLOSED BY REDESIGN, with one open remainder.**
  The geometric flank-poke "tilt enclosure" (v24 Movement-2) is RETIRED by Tony's
  decision (Q2, June 7): the chosen approach is the HOVER DISCLOSURE -- state what
  geometry is sourced from physics vs approximate/schematic, not re-shape the
  flank. Envelope hovers (Uranus + Neptune) carry this disclosure as of v27 (DONE).
  OPEN REMAINDER: the BOW-SHOCK hovers (Uranus 23.7 R_U, Neptune 34.9 R_N) cite
  their standoff but do NOT yet flag the conic-section approximation (v27 sec 4).
  Extend the same sourced-vs-schematic disclosure to the bow-shock hovers. `[per chain]`
- **v24 sec5 precision batch** (low-risk, not blocking):
  - **Inner-four bow-shock hover missing km/AU** -- OPEN. Mercury/Venus/Earth/Mars
    bow-shock hover reads "radii" only (e.g. Mercury L304/L364 "1.4 to 2.0 radii");
    giants got km/AU in v24. Standing Hover-Text-AU-Convention gap.
    `[verified @76c330e]` (Mercury checked; the other three inner bodies follow the
    same v24 pattern, `[per chain]`). See section E.
  - Jupiter compressed/expanded MP toggle (Joy 2002 bimodal ~63/~92; current single
    65 defensible). Feature, not a number. `[per chain]`
  - Earth MP/BS citation upgrade (Fairfield/Shue ~10 / ~14.6 over flat "15
    textbook"); nest unaffected. `[per chain]`
  - Per-body bow-shock eccentricity (e.g. Mercury 1.02); 1.05 illustrative is
    visually fine. Optional. `[per chain]`
- **Animation parallel-pipeline gap -- UNIFIED ITEM (see D.Architecture 21/51).**
  v27's "dipole cone + rotation axis do not render in animate frames" is the SAME
  architectural issue as v23 item 21/51 ("make non-center-body shells render in the
  animate path") and v25's animation deferral. ONE fix likely covers the
  body-triggered elements; map the animate dispatch before patching. Tracked once,
  under 21/51, not three times.
- **Envelope -> dipole tie / season-derived roll** (Mode-7). Conditional: only if a
  season-derived envelope roll is wanted; gated on a physics question (does the
  magnetopause asymmetry track the instantaneous dipole projection?). Otherwise the
  frozen still + v27 disclosure is the honest near-term state. `[per chain]`
- **Dipole offset DIRECTION** (Mode-7). Magnitude sourced (~0.3 R_U, ~0.55 R_N),
  direction not. Apex stays at center until sourced; do not fake direction. `[per chain]`
- **Other dipole bodies** -- Earth (~11 deg, the compass-vs-true-north anchor;
  worth a skinny cone), Jupiter (~10 deg, optional), Saturn (<1 deg, NO cone --
  hover NOTE only). ALL tilts/sense/poles currently RECALLED; MUST be sourced
  (primary literature / Mode-7) before any PLANET_DIPOLE entry. `[per chain]`
- **Per-body half_len_frac tuning** (rotation axis + cone share the scale) -- Mode-5
  knobs, not a bug. `[render-gated]`

### D.Priority -- real bugs

- (none currently open) The conflated "duplicate 'Sun'" item closed June 8 as TWO
  distinct fixes: the visible double-Sun was a center-dropdown assembly bug
  (palomas_orrery.py), and the CUSTOM_SHELLS duplicate key (shell_configs.py
  L2642/L2823) was a real but dormant dead-block. Both recorded in section C (DONE).
  Lesson: a duplicate dict key collapses to one on iteration, so it cannot by itself
  produce a doubled selector entry -- the symptom and the dict-key bug were separate.

### D.Structural -- dead-code / honest shell files (Phase 3)

`[all per v23 / v25 chain; not re-verified @HEAD this session]`
- 2 Asteroid belt migration decision (CUSTOM_SHELLS vs documented exception).
- 3 Retire create_planet_visualization() frame (verify dead path deletable).
- 5 _info import cleanup (~89+87 imports, 2 files).
- 6 Archive dead shell functions (the "honest shell files" sweep; v9 detail below).
- 7 Tooltip rewiring globals() -> config fields.
- 8 Dead create_sun_direction_indicator imports (v14 removed ~10; verify remainder).
- 13 Neptune ring info-marker rotation (likely subsumed by 47a/47b; VERIFY+close).
- 26 CUSTOM_SHELLS tooltip verification (Sun customs; low -- D1 used source strings).
- 28 Neptune superimposed info markers (likely subsumed by 2C; VERIFY+close).
- 40 Asteroid belt hover -> single info marker (4 belt builders).
- N2 Saturn/Uranus ring marker placement (saturn L1171, uranus L1061-1062; markers
  at (r,0,0) not riding the rotated ring; single-line each). Also the erratum's "N2
  ring marker placement -- unchanged" thread.
- N3 Center-body marker edge case (palomas_orrery.py 4558-4617; two origin markers
  when body checked + centered + no shells).
- N4 Planet 9 single sphere n=50 (should be 20/25 convention).
- N7 Planetary shell info-marker sweep -- MOSTLY OBSOLETE (sphere-shell inline
  markers are dead code; factory + per-config info_border already controls them).
  Reduces to custom-geometry inline markers only. Do NOT edit sphere-shell inline dicts.
- 9 palomas_orrery_helpers.py CRLF -> LF.
- 61 Platform Neutrality (SystemButtonFace -> hex literal / platform detect / ttk).
- **v25 D3 dead-code annotations** (annotate, do NOT remove yet): saturn
  rotate_points import now unused after N15; idealized_orbits.py analytical branches
  (Mars 25.19, Jupiter 3.13, Uranus 105 fudge squatting in plot_satellite_orbit) +
  calculate_jupiter/saturn_satellite_elements now effectively unused in live render.
- **v25 small-body analytical tail**: TNO_MOONS + Patroclus-Menoetius barycenter
  orbiters (~L5174) still call plot_satellite_orbit via the generic-parent path.
  Evaluate same-artifact before migrate-or-retire; rarely-plotted edge cases.

v9 dead-code detail (the "archive dead shell functions" target): 10 dormant
sun_direction blocks (venus 497/798, earth 605/1146, mars 576/925, jupiter 509/826,
saturn 592/965); asteroid belt 4 dead calls (231/327/427/523); Sun Roche duplicate
(CUSTOM_SHELLS['Sun']['roche_limit'] shadowed + create_sun_roche_limit_shell
uncalled); inert sphere-shell inline marker conversions. KEEP: comet sun-direction
calls (L1523/1949 -- they fire).

### D.Cosmetic -- polish (bundle when convenient) `[per chain]`

- 17 GEO info-marker position (+X side of ring; could move to spoke).
- 18 Uranus gossamer ring barely visible (Mode-5 when desired; also the erratum's
  cosmetic-18 thread).
- 41 Sun legend ordering (DO NOT fix manually -- needs ordered dispatch iteration).

### D.Feature -- Bucket A (completes/equips standard rendering; near-term) `[per chain]`

- 23 Earth ionosphere shell.
- 19 Plot-cube control parity (orrery GUI) -- JOINED / cross-repo (Tony, June 8).
  Gallery Studio has a full plot-cube control set; the orrery GUI does not.
  Implement the Studio set in the orrery GUI: scene_axis_range + scene_dtick
  (the original "manual axis range + dtick" core), scene_aspectmode
  (auto/cube/data/manual), scene_camera orientation (original/isometric/top/
  front/side), and show_axes / show_grid toggles. Studio side
  `[verified @2f40d9d]` (tools/gallery_studio.py DEFAULT_CONFIG ~L72-96; rendering
  ~L912-941); orrery GUI side is the open work. Design authority:
  3d_axis_control_handoff.md (website repo documentation/). 3D Axis Control
  Convention parity; xvfb gate. (Cross-ref
  Gallery section H.)
- 20/N5 Shell-resolution GUI control (enabler for Bucket B; bundle with HTML export
  mode and with 19).
- 49 Fly-to view scaling (the "0.15 AU" bug; visualization_utils.py
  add_fly_to_object_buttons; view box sized by distance-from-center not target size).
- View-window scaling design (49 + 19 + Studio parity): one shared
  view_window(target|region) -> (range, dtick) producer; zero-code design first.

### D.Feature -- Bucket B (editorial; open-ended) `[per chain]`

- 22 Satellite internal-structure shells (Phase E creative / Mode 7).
- N14 Miranda inclination-anomaly tooltip (i=4.232-4.34 deg to Uranus equator;
  3:1 Umbriel resonance hook; confirmed-correct in render). Small editorial; Tony's call.
- Deeper-detail direction (stratosphere, finer corona, solar storms -> straddles
  animation Bucket C). Not a finite item; 20/N5 is the on-ramp.

### D.Feature -- Bucket C (architecture; design-before-code) `[per chain]`

- N6 Studio editor review + encounter-event generator + Artemis redo (data/
  provenance cluster; folds items 37/38 spacecraft provenance and N11 Artemis
  lunar-flyby Horizons-override console check). UPDATED June 8: the generator
  EXISTS and emits both full-mission and encounter forms (gallery_studio.py
  _generate_encounter_code, ~L5352) -- N6's "design-first / emits both forms"
  keystone is DONE. Remaining work is a COUPLED refactor + redo, done together,
  and it SPANS TWO REPOS (Gallery Studio is a separate repo from the orrery):
    * Generator refactor [Gallery Studio repo, tools/gallery_studio.py @2f40d9d;
      `[verified @2f40d9d]` -- upload confirmed byte-identical to repo HEAD]:
      the generator does NOT emit four fields the Artemis presets carry --
      resolution_note, center_closeup, plot_days_closeup, plot_scale_au_closeup.
      Extend it to produce them.
    * Artemis preset redo [orrery repo, `[verified @730b2bf]`]: regenerate the
      'Artemis II' presets (spacecraft_encounters.py ~L196) through the refactored
      generator. They hold removed/unverified data (v_kms None; dates "pending
      re-derivation from NASA/JSC OEM"), so they need the generator's normalized +
      sourced output (dist_au from dist_km, date normalization, date_source/source).
    * Coupling (Tony, June 8): the generator must include items only in the presets,
      and the presets need information the generator produces -- one pass, not two.
      Because the halves live in DIFFERENT repos, the redo must coordinate a Gallery
      Studio change with an orrery-repo data change (two HEADs to track).
    * N11 (Artemis Moon-flyby, date_source 'horizons') rides with the redo: the
      Horizons-derived date is validated by the console check during regeneration.
    * Design authority: ENCOUNTER_EXPORT_HANDOFF_v3.md (the "v3.0" doc; Fork 1 /
      Fork 2, Orrery preset mode, post-production boundary) -- in the ORRERY repo
      documentation/ `[verified @730b2bf]`, NOT the website repo. Generator built
      Session 36b (May 2), refined Session 37 (May 4-5) -- per web_gallery_handoff.md
      (website repo documentation/; Gallery section H).
    * Refactor scope note: the four missing fields are a SECOND (close-up) view's
      parameters (center_closeup / plot_days_closeup / plot_scale_au_closeup) plus
      an editorial resolution_note -- not post-production cosmetics. Open design
      question the refactor inherits: how the Studio captures a second view in one
      export (Session 37 held "the figure is the source of truth for view
      parameters" for a single view). "Camera capture (not extracted)" is the
      sibling un-emitted field.
- N10 Note-composition structural refactor (renderer composes the encounter note
  from resolved values + template; structural cure for stale-prose numbers; sits
  behind N6).
- **21/51 Animation track (UNIFIED)** -- three objectives: (1) non-center-body /
  body-triggered shells render in the animate path (NOW EXPLICITLY INCLUDES the v27
  rotation-axis + dipole-cone animation gap); (2) reduce animation memory overhead;
  (3) consolidate animate with static (parallel-pipeline divergence). When deferring,
  smoke-test the animate pipeline to confirm a KNOWN state, not just no-error.
  Architecture-first; multi-session.

### D.Parked (Tony's explicit call to leave as-is) `[per chain]`

- N8 Comet info-marker superposition cluster (hover ikeya_seki + design before work).
- N9 Codebase-wide white -> red orbit-marker switch (deliberate whole-orrery change;
  osculating marker intentionally stays white).

### D.Loose end to reconcile `[per chain; not re-verified]`

- Uranus pole-value prose inconsistency (erratum): Dec -15.10 (planet_poles, the
  value v26's table uses) vs prose "RA 257.31 / -15.18" elsewhere (~0.1 deg).
  Reconcile the stray prose to the load-bearing value when next in the file.

---

## E. AU-CONVENTION COMPLIANCE CLUSTER (standing convention; one sweep)

The Hover-Text-AU-Convention (all distance hover text includes AU alongside km;
km/149597870.7) has known residual gaps. Group them into one sweep rather than
chasing singly:
- Inner-four bow-shock hover ("radii" only) -- `[verified @76c330e]` (Mercury).
- GEO altitude hover missing AU (standing-convention note; GEO ~0.000285 AU).
  `[per standing convention; not re-verified]`
- Any new hover added by Movement work -- confirm km+AU at add time.

---

## F. CONSOLIDATION LOG (what this pass repaired)

- RESTORED 2 leaked Movement-2 items (Mercury north offset; bow-shock honesty)
  that lived only "by reference" in v24 and were absent from v26/v27 ledgers.
- RESTORED the v24 sec5 precision batch (inner-four km/AU, Jupiter toggle, Earth
  citation, eccentricity), absent from v26/v27 ledgers.
- CORRECTED a stale "open": the June-1 erratum's Uranus 105-fudge "NOT STARTED" is
  DONE at HEAD (verified); not carried forward as open.
- UNIFIED three records of the animation issue (v23 21/51, v25 deferral, v27 gap)
  into one item (21/51).
- CLOSED N13 (v23 Bucket B) as the v27 dipole cone.
- CLOSED N12 (pole markers, Tony-confirmed June 7) and dropped the rotation-axis
  Mode-5 sweep as a non-issue (most confirmed, Tony June 7).
- RECORDED Q2 decision: flank-poke geometric enclosure closed-by-redesign; hover
  disclosure is the path; bow-shock-hover disclosure is the open remainder.
- MOVED Food Insecurity from v23 "on-the-horizon" backlog to an active separate
  track (Tony, June 7).
- VERIFIED against HEAD: 105-fudge (done), Mercury offset (absent/open), duplicate
  Sun key (L2642/L2823, open), inner-four bow-shock hover (radii-only, open).
  (UPDATE June 8: the duplicate Sun key is now CLOSED, and the visible double-Sun was
  traced to a separate center-dropdown bug -- both in section C.)
- (June 8) RECOVERED a leaked item into N6: the Gallery Studio preset-generator
  refactor + Artemis preset redo. It floated since June 1 (v21 erratum) with no
  handoff home ("flag it for whichever ledger" that never landed), so the v23->v28
  consolidation could not carry it -- it lived below the handoff layer. Now folded
  into N6 with verified specifics. Also recorded: Gallery Studio is a SEPARATE repo
  (HEAD 2f40d9d), distinct from the orrery repo (730b2bf) -- this coupled item
  spans both.

---

## G. OPEN QUESTIONS / TONY CALLS

- AU-convention sweep (section E): KEEP OPEN, revisit (Tony, June 7 -- origin not
  immediately recalled). Context for the revisit: the verified facts are that the
  inner-four bow-shock hover reads "radii" only at HEAD (Mercury L304/L364), and
  the GEO altitude hover lacks AU per the standing convention. Decide then whether
  to batch them as one pass.

(Resolved June 7: N12 pole markers -- done; rotation-axis Mode-5 sweep -- most
confirmed, not an issue. Both removed from the open list.)

---

## H. GALLERY / STUDIO TRACK (website repo; low-activity)

Added June 8 (Tony's call: carry the Gallery as a separate section in this one
ledger rather than a separate file -- it is much less active). This is the
website/Gallery-Studio track, a SEPARATE repo from the orrery app repo.

- **Repo source (recorded June 8 for future reference).**
  URL: https://github.com/tonylquintanilla/tonyquintanilla.github.io
  Owner `tonylquintanilla` (WITH the 'l', same as the orrery); repo name
  `tonyquintanilla.github.io` (NO 'l'). That owner/name split is exactly why the
  repo is easy to mis-locate -- pair them as written. Branch `main`. Public
  (clones / raw-fetches unauthenticated). HEAD verified this session == `2f40d9d`
  (matches the SHA Tony provided). Custom domain `palomasorrery.com` (CNAME).
  Studio file: `tools/gallery_studio.py` (NOT repo root). The uploaded
  gallery_studio.py this session was byte-IDENTICAL to that path @2f40d9d, so the
  Studio verification below is repo-grade.
- **Handoffs / design docs -- which repo holds what (both have a documentation/):**
  - WEBSITE repo `documentation/` `[verified @2f40d9d]`: `web_gallery_handoff.md`
    (last Studio handoff, Feb 5 -> May 5, 2026); `3d_axis_control_handoff.md`
    (design authority for the item-19 plot-cube parity).
  - ORRERY repo `documentation/` `[verified @730b2bf]`: the encounter-export design
    docs live HERE, not in the website repo -- `ENCOUNTER_EXPORT_HANDOFF_v3.md`
    (the "v3.0" authority for N6), plus _v2, DESIGN_encounter_export_v2, and the
    fix/test set.
- **No Studio running ledger yet** -- by design (Tony, June 8): stand one up only
  if/when Studio work resumes in volume. Until then these open items live here.

**Joined / cross-repo items (tracked in their orrery homes; cross-referenced):**
- **N6** -- encounter-preset generator (Studio repo) refactor + Artemis preset
  redo (orrery repo). See D.Feature Bucket C.
- **Item 19** -- plot-cube control parity: port the Studio plot-cube control set
  to the orrery GUI. See D.Feature Bucket A.

**Open Studio items (carried from the May-5 handoff; statuses checked @2f40d9d
where file-verifiable):**
- Encounter export: test with various mission types `[per handoff]`; camera
  capture -- still NOT extracted, confirmed `[verified @2f40d9d]` (sibling of the
  N6 second-view gap); link-icon end-to-end test `[per handoff]`.
- Content re-population: re-export ALL existing gallery content through the
  Studio (WYSIWYG refactor moved transforms into the Studio; index applies none).
  Not file-verifiable from a clone `[per handoff]`.
- Website chrome `[verified @2f40d9d]`: gallery-card thumbnails -- ABSENT (open);
  content pages About/Downloads/Contact -- ABSENT (only index.html exists, open);
  social link-preview og:image -- a meta tag IS present in index.html (per-card
  previews unconfirmed; treat as partial).

**Recently closed (verified this session @uploads/HEAD):**
- `_enter_orrery_mode()` reset to DEFAULT_CONFIG -- DONE (`[verified @2f40d9d]`,
  tools/gallery_studio.py ~L4775).
- `ongoing` added to spacecraft_encounters.py status comment -- DONE (verified, L60).

---

Module updated: June 2026 with Anthropic's Claude Opus 4.8
