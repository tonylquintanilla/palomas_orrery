# HANDOFF: Shell Consolidation -- Consolidated Ledger + Go-Forward Plan (v19)

**Date:** May 31, 2026
**Session model:** Claude Opus 4.8
**Supersedes:** v18 -- single running ledger (carries the full v18 ledger forward)
**Type:** Go-forward re-scoping + ledger update. NO code changed this session
(planning only). Deltas: May 29 round Mode-5 PASS recorded; D-ARTEMIS dissolved
into N6; note-composition refactor promoted to N10; Artemis console check
captured as N11 (standalone diagnostic); item 19 moved to Phase 5; Phase 2
shrunk to 49+53; animation (21/51) re-scoped to a three-objective track;
Phase 5 reorganized into three buckets; dead-code sweep marked deferred.
**Integrator:** Tony Quintanilla

> **This is the one document to follow.** v18 is now superseded and retired --
> do not carry it forward. Its full ledger lives below, carried forward intact
> (nothing renumbered). This session changed no code: it re-scoped the
> go-forward plan after a design conversation with Tony. The ledger rule still
> holds: nothing renumbered; new items appended (N10, N11 added this session).

---

## Why this handoff exists

The shell-consolidation track ran across ~19 handoffs (c2, c3, c4, d1,
d2, d2_v2, d3_1 v1-v12, stage_3 v14-v15). Item numbering was rebased
twice (c4: 1-22 -> D1: 1-41 -> D2: 42-54 -> D3.1: 55-61), then v8-v15
dropped the numbered table entirely for a "Stage 1-4" framing. Items
leaked at the seams -- most importantly the 4 Tier-1 provenance items
(D1 items 36-39) and a handful of small orphaned bugs.

The v16 session read all 19 handoffs end to end and rebuilt ONE
authoritative ledger. v18 continues it: provenance Phase 1 was executed
and its results folded in, and v17 + the Phase-1 addendum were absorbed
here so there is again exactly one document to follow. From here forward,
**this file is the running ledger.** New items get appended with the next
free number; nothing gets renumbered. (Protocol lesson, v3.24 re-issue:
handoff numbers rebased across versions is a drop source -- one running
ledger beats per-handoff renumbering.)

---

## THIS SESSION (May 31) -- Go-Forward Re-Scoping (planning only, no code)

A design conversation with Tony reorganized the go-forward plan. No code
touched; the ledger below is updated to match. Deltas:

- **May 29 border-refinement + osculating-marker round: Mode-5 PASS,
  recorded.** Tony's annotated test protocol confirms it: smoke clean,
  osculating marker now renders on every comet tested, all 7 border
  reversions read red, all 3 additions read white, custom-geometry inline
  borders correct, zero regression. Observations were superimposition cases
  only (ikeya_seki osculating/keplerian crosses overlapping + coma marker
  buried; 3I/ATLAS anti-tail/mini-jet overlapping) -- they fold into N8
  (parked). Round closes clean; nothing new opened. (N1 was already DONE in
  the ledger; this is the visual-verification close of that round.)
- **D-ARTEMIS dissolved as a standalone round -> folded into N6.** The
  Artemis preset rewrite is now a DOWNSTREAM step of the generator refactor:
  fix the studio encounter-export generator first, then re-enter both Artemis
  presets THROUGH it, annotating per-field sourcing as the data goes in.
  Items 37/38 stay claim-stripped (Tier-1 already compliant); the redo is now
  N6 work, not its own round.
- **N6 keystone RESOLVED.** The open design question v18 posed -- "does the
  generator emit encounter-event entries OR stay full-mission-only?" -- is
  answered: **both.** The generator gets EXTENDED to emit the encounter-event
  form (per-event `note` / `dist_km` / `date_source` + a `resolution_note`
  field) ALONGSIDE the full-mission form it already produces. This is now a
  build, not a fork to decide.
- **Note-composition structural refactor PROMOTED to N10** (was buried in the
  D-ARTEMIS prose as "structural follow-on"). Renderer composes the display
  note from resolved values + a template, so numbers can never be stored as
  stale prose again. It is the structural CURE for the fused-provenance
  disease that made Artemis a mess; it sits behind the same structured
  per-field data N6's extended generator would emit.
- **Artemis "does the Horizons override fire?" console check captured as N11**
  -- a STANDALONE DIAGNOSTIC, kept SEPARATE from D-URANUS per Tony. Possible
  live render bug (swallowed exception -> Apr-7 placeholder rendering for
  weeks), independent of the N6 refactor. Captured so it cannot float and get
  lost before N6 (which may be weeks out).
- **Item 19 (GUI axis/dtick) moved Phase 2 -> Phase 5.** It is a GUI rendering
  FEATURE with a Gallery-Studio-parity argument, not a known-shape mechanical
  edit. Bundles with the orrery-GUI-controls work (20/N5), same file, same
  xvfb gate.
- **Phase 2 shrinks to 49 + 53** -- both genuinely small leaf edits. This is
  the immediate "get it off the books" session.
- **Animation (21/51) re-scoped to a three-objective architecture track**
  (see ledger): not "wait until needed." It is real, multi-session work.
- **Phase 5 reorganized into three buckets** (completes/equips, additive-
  editorial, architecture) -- see the rewritten FEATURE section and Go-Forward
  Plan.
- **Dead-code sweep (Phase 3): marked DEFERRED.** Stays fully documented in
  the ledger (deferring dead code is safe precisely because it is dead -- the
  documentation is what keeps it safe).

**Near-term order agreed:** (1) Phase 2 = items 49 + 53 (start here);
(2) D-URANUS as its own render-gated session; (3) architecture/creative design
sessions scheduled after, unhurried. N11 (Artemis console check) is its own
observation, NOT bundled into D-URANUS.

---

## PHASE 1 EXECUTED (the May 30 session -- provenance verification)

The Go-Forward Plan's step 1 (factual verification, items 36-39 + tilt sign)
was run. web_search sourcing (fetched) + Gemini Mode 7 cross-check on the
contested claims. Outcome and ledger impact:

- **Item 36 (Neptune) -- CLOSED.** `# Source:` comment added directly above
  `magnetosphere_text` (within the 30-line scanner lookback; the existing
  citation sat ~134 lines away, outside the window, plus an in-string
  "Source:" the scanner does not count). Verified in the uploaded file
  (1719 -> 1722 lines). Values were already correct (47 deg, 0.55 R_N).
  Audit regenerated May 31 confirms Neptune dropped out of Tier-1.
- **Items 37, 38 (Artemis II) -- RE-SCOPED to D-ARTEMIS (below); interim
  strip COMPLETE.** Not a citation fix. The dict fuses fetched + recalled
  data behind a misleading source stamp; the right fix is a preset redo from
  traceable sources. Interim: BOTH `note` strings (lunar flyby L237 and
  reentry L265) were claim-stripped -- numbers removed -- to clear the Tier-1
  findings honestly without papering a citation over recalled prose. The
  lunar note cleared first; the reentry note was stripped in a follow-up and
  was the final Tier-1 close. Real content still pending the redo.
- **Item 39 (Uranus) -- CLOSED.** `# Source:` comment applied at L514-517,
  above the magnetosphere `description` (verified in uploaded file). Cleared
  Uranus from Tier-1. The 59/60 VALUE decision is separate and still open
  (displayed string still reads "60 degrees") -> D-URANUS U1.
- **N2-orphan (Uranus tilt sign) -- EXPANDED into D-URANUS (U2).** Render-
  gated, not literature. Magnitude verified (59-60); sign is a code-
  convention question only a render settles.

Key discovery (now a convention, see bottom): the audit flags by NUMERIC
token, and "sourced for a human" is not "sourced for the scanner" -- the
`# Source:` comment must sit within lookback and in the right form.

Tier-1 trajectory: 4 -> Neptune closed -> Uranus citation applied -> both
Artemis notes claim-stripped -> **Tier-1 = 0, confirmed in the May 31 audit.**
Provenance Phase 1 goal (drive Tier-1 to zero) is MET. Note the zero rests
partly on interim claim-strips (Artemis), not full sourcing -- the D-ARTEMIS
redo replaces stripped prose with traceable content but does not change the
Tier-1 count (stripped notes are already compliant).

---

## THE HEADLINE: where the refactor actually stands

**The strategic migration is COMPLETE.** All 13 bodies (Mercury, Venus,
Earth, Moon, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Eris,
Planet 9, Sun) route through the unified config-driven dispatch
(`SHELL_CONFIGS` / `CUSTOM_SHELLS` -> `create_celestial_body_visualization`
-> `build_sphere_shell` -> `create_info_marker`). Zero bodies remain on
the old `create_planet_visualization()` / `create_sun_visualization()`
paths.

Migration timeline (all DONE and deployed):
- C1-C3: Mercury through Jupiter (May 16)
- **C4: Saturn, Uranus, Neptune (May 18)**
- **D1: Sun + asteroid-belt separation (May 19)**
- **D2: sun_position wiring, Earth/Jupiter tilts, Neptune Option C (May 20-22, deployed)**
- D3.1: hovertext/legendgroup sweep + dispatch-path factory fix (May 22-23)
- D3.1 Stage 2: Mars info marker, Neptune ring/arc, MAPS comet cluster (May 26)
- Stage 3 Phase 1: info-marker factory re-pipe (Option A border control) + osculating marker fix (May 29)

**Posture correction:** the project is no longer "mid-refactor." It is
in **cleanup-and-close**. What remains is (a) provenance debt, (b) a
scatter of small orphaned bugs, (c) structural dead-code honesty, and
(d) optional feature work. Any handoff or memory that says "resume C4"
or "Phases B-D are the strategic line" is stale -- that work is done.

---

## Reconciled Deferred-Items Ledger (canonical)

Numbering follows D1 (the authority, items 1-41), extended by D2
(42-54) and D3.1 (55-61). Stage-era items that were never numbered are
assigned N1-N9 here. (v18 prose said "N1-N10" but never defined an N10 row --
a small leak; corrected here.) N10-N11 are added this session (May 31).
Status as of May 31, 2026.

### DONE (closed -- for the record, do not re-do)

| # | Item | Closed by |
|--:|------|-----------|
| 1 | Sun config extraction | D1 |
| 4 | sun_position wiring (static) | D2 |
| 10 | Double sun direction indicator | D2 |
| 11 | Earth/Jupiter magnetic_tilt_deg | D2 |
| 12 | Neptune magnetic poles -> diamond (Option C) | D2 |
| 14 | Neptune debug print | D1 |
| 15 | Neptune function-local imports | D1 |
| 16 | Venus hover text | C1 |
| 25/42 | Mars (induced) magnetosphere info marker | D3.1 Stage 2 (2B, v11) |
| 27 | Saturn/Uranus/Neptune hover \n -> <br> | D1 |
| 29 | Sun call-site switchover | D1 |
| 31 | hover_text_sun_and_corona Tkinter format | D1 |
| 32 | Sun custom info marker borders | D1 |
| 33 | Sun photosphere mesh3d | D1 |
| 34 | Photosphere hover truncation | D1 |
| 35 | corona_from_distance retired | D1 |
| 43 | Uranus magnetosphere hover truncation | D3.1 Batch 5 |
| 44 | Neptune magnetosphere hover truncation | D3.1 Batch 5 |
| 45 | Neptune radiation hover labelling | D3.1 sweep |
| 46 | Neptune FAC hover labelling | D3.1 sweep |
| 47a | Neptune arc markers superimposed | D3.1 Stage 2 (2C, v11) |
| 47b | Neptune Lassell+Arago superimposed | D3.1 Stage 2 (2C, v11) |
| 48 | Mercury sodium tail sun_position wiring | D3.1 Stage 2 (2A.5, v11) |
| 50 | Sun direction indicator per-body legendgroup+label | D3.1 (Sun Direction fix, v9) |
| 54 | Hovertext/legendgroup sweep | D3.1 (v4-v8) |
| 55 | Solar shell naming "Sun: X" | D3.1 Batch 1 |
| 56 | Crust/cloud legendgroup fix | D3.1 Batch 4 |
| 57 | Neptune magnetosphere double-leader | D3.1 Batch 2 |
| 58 | MAPS placeholder legendgroups | D3.1 Batch 2 |
| 59 | Deprecate create_neptune_magnetic_poles orphan | D3.1 Batch 3 |
| 60 | Moon Hill Sphere "Moon:" prefix | D3.1 Batch 3 |
| N1 | idealized_orbits.py line ~7331 "color not defined" (osculating marker) | Stage 3 (v15) |
| 36 | Provenance Tier-1: Neptune display string citation | Phase 1 (v18, May 30) |
| 39 | Provenance Tier-1: Uranus display string citation | Phase 1 (v18, May 30) |

### OPEN -- PRIORITY (real bugs + provenance, several orphaned in rebase)

Grouped by the KIND of work, because the kind sets the effort level
(see "Effort Calibration" below). Factual-verification items first
(fetched-not-recalled risk), then purely mechanical edits.

**Factual verification (Phase 1) -- claims that must be sourced against
an authority before asserting. The edit is trivial; the verification is
the work.**

**Factual verification (Phase 1) -- EXECUTED this session (v18). Status
updated; see PHASE 1 EXECUTED above and the D-ARTEMIS / D-URANUS rounds below.**

| # | Item | File / locus | Status |
|--:|------|--------------|--------|
| 36 | Provenance Tier-1: Neptune display string | neptune_visualization_shells.py | **CLOSED** (v18) -- citation applied + verified. |
| 37 | Provenance Tier-1: spacecraft display string | spacecraft_encounters.py line 237 | **FOLDED -> N6** (was D-ARTEMIS). note claim-stripped interim (Tier-1 compliant); preset redo is now downstream of the N6 generator refactor. |
| 38 | Provenance Tier-1: spacecraft display string | spacecraft_encounters.py line 268 | **FOLDED -> N6** (was D-ARTEMIS). Same. |
| 39 | Provenance Tier-1: Uranus display string | uranus_visualization_shells.py L514-517 | **CLOSED** (v18) -- `# Source:` comment applied above the magnetosphere `description`, verified in uploaded file. (59/60 VALUE decision still open -> D-URANUS U1; displayed string still reads 60.) |
| N2-orphan | Uranus magnetic tilt SIGN verification | uranus (60 deg) | **EXPANDED -> D-URANUS U2.** Magnitude verified; sign is render-gated. |

**Mechanical edits (Phase 2) -- no verification trap; shape is known.
START HERE (the immediate "off the books" session).**

| # | Item | File / locus | Notes |
|--:|------|--------------|-------|
| 49 | Earth fly-to-Sun distance hardcoded 0.15 AU | (Gap B, D2) | Geometry bug; never closed. Lives in `palomas_orrery.py` -> inherits the xvfb pre-test gate. |
| 53 | Neptune magnetic center marker convention | neptune | Should be `square-open`, not `diamond` (marker symbol convention). Clean leaf. |

(Item 19, formerly here, moved to Phase 5 -- it is a GUI rendering feature,
not a known-shape edit. See FEATURE section.)

**Standalone diagnostic (render-gated, no code) -- do NOT bundle.**

| # | Item | File / locus | Notes |
|--:|------|--------------|-------|
| N11 | Artemis II lunar-flyby: does the Horizons override actually fire? | render + console | **[DIAGNOSTIC]** Render the Artemis II lunar flyby, watch console for `[RESOLVE] Deriving Moon closest approach...` + `[HypOsc] Using spacecraft encounter epoch`. Present -> override fires, date/dist are pipeline-sourced. Absent -> override silently failed (swallowed exception, L1462), the Apr-7 placeholder is rendering -- a live render bug to fix BEFORE the N6 redo means anything. ~2 min, pure observation. Kept SEPARATE from D-URANUS per Tony's call. Captured here so it cannot float (it would otherwise sit unseen until N6, possibly weeks out). Detail: see D-ARTEMIS-now-N6 round below ("CRITICAL UNKNOWN"). |

### OPEN -- STRUCTURAL CLEANUP (Phase 3 dead-code / honest shell files)

| # | Item | Locus | Notes |
|--:|------|-------|-------|
| 2 | Asteroid belt migration decision | asteroid_belt_*_shells.py | Belts are direct calls (Sun-centered). Decide: CUSTOM_SHELLS vs documented exception. |
| 3 | Retire create_planet_visualization() frame | planet_visualization.py | Body blocks gone after C4; verify the frame + dead path can be deleted. |
| 5 | _info import cleanup | ~89+87 imports, 2 files | |
| 6 | Archive dead shell functions | per v9 table below | The Phase 3 "honest shell files" sweep. |
| 7 | Tooltip rewiring globals() -> config fields | celestial_objects.py path | |
| 8 | Dead create_sun_direction_indicator imports | 5 modules | v14 removed ~10; verify remainder. |
| 13 | Neptune ring info marker rotation | neptune | Likely subsumed by 47a/47b (2C); VERIFY then close. |
| 26 | CUSTOM_SHELLS tooltip verification (Mode 7) | Sun customs | Low -- D1 used source strings (zero composed). |
| 28 | Neptune superimposed info markers | neptune | Likely subsumed by 2C; VERIFY then close. |
| 40 | Asteroid belt hover -> single info marker | 4 belt builders | Predate the 141-conversion refactor. |
| N2 | Saturn/Uranus ring marker placement | saturn line 1171, uranus 1061-1062 | Same bug as Neptune 2C; markers at (r,0,0) not riding rotated ring. Single-line each. |
| N3 | Center-body marker edge case (no shells) | palomas_orrery.py 4558-4617 | Two markers at origin when body checked + centered + no shells. |
| N4 | Planet 9 single sphere n=50 | planet9_visualization_shells.py line 261 | Should be 20/25 convention. |
| N7 | Planetary shell info-marker standard sweep | *_visualization_shells.py | REFRAMED: per v14/v15 the sphere-shell inline markers are DEAD CODE; the factory + per-config `info_border` (Option A) already controls them. This item now reduces to custom-geometry inline markers only. Mostly obsolete -- do not edit sphere-shell inline dicts. |
| 9 | palomas_orrery_helpers.py CRLF -> LF | helpers | Platform/encoding (see protocol Platform Neutrality). |
| 61 | Platform Neutrality (SystemButtonFace) | palomas_orrery.py | Now also a protocol [QUALITY] convention. Real fix: hex literal / platform detect / ttk. |

**v9 dead-code detail (the "Archive dead shell functions" target):**
- 10 dormant sphere-shell builder calls (sun_direction blocks in
  `*_upper_atmosphere_shell` / `*_hill_sphere_shell`): venus 497/798,
  earth 605/1146, mars 576/925, jupiter 509/826, saturn 592/965.
  (Mercury/Uranus/Neptune already cleaned; Moon never affected.)
- Asteroid belt 4 dead calls: asteroid_belt lines 231, 327, 427, 523.
- Sun Roche duplicate: `CUSTOM_SHELLS['Sun']['roche_limit']` (shadowed
  by SHELL_CONFIGS, dead) + `create_sun_roche_limit_shell` (uncalled).
- Inert sphere-shell inline marker conversions from earlier sessions
  (compile clean, never rendered -- the v14 "fiction" edits).
- KEEP: comet sun-direction calls (lines 1523, 1949 -- they fire and
  are useful).

### OPEN -- COSMETIC POLISH (bundle when convenient)

| # | Item | Notes |
|--:|------|-------|
| 17 | GEO info marker position | +X side of ring; could move to spoke. |
| 18 | Uranus gossamer ring barely visible | Mode 5 when desired. |
| 41 | Sun legend ordering | Trace-add order vs shell size. DO NOT fix manually -- needs ordered dispatch iteration. |

### OPEN -- FEATURE / PHASE 5 (separate scoped sessions)

Phase 5 is not one phase. Tony's organizing seam is *what the work does to
the rendering*, and priority falls out of it. Three buckets:

**Bucket A -- Completes / equips the standard rendering (higher priority,
near-term):**

| # | Item | Notes |
|--:|------|-------|
| 24 | Gas giant bow shocks (Jupiter/Saturn +) | **Higher priority -- completes the standard geometry.** New paraboloid geometry; standoff distance + shape are Mode 7 / Gemini territory. Co-toggle design. |
| 23 | Earth ionosphere shell | Completes the structure (like bow shocks). Also an on-ramp to deeper editorial detail -- see Bucket B. |
| 19 | Manual axis dtick + range in orrery GUI | **Higher priority -- general rendering flexibility, not a specific object.** Gallery Studio has it; GUI does not (3D Axis Control Convention parity). `palomas_orrery.py` GUI -> xvfb gate. Bundles with 20/N5 (orrery-GUI-controls). |
| 20/N5 | Shell Resolution GUI control | The ENABLER for Bucket B, not a peer item -- every shell added makes this lever matter more. Two knobs (sphere/ring) + exemptions. Bundle with HTML export mode (same file-size lever) and with 19. |

**Bucket B -- Adds editorial content (truly additive, open-ended direction):**

| # | Item | Notes |
|--:|------|-------|
| 22 | Satellite internal structure shells | Truly additive. Phase E creative / Mode 7. |
| -- | Deeper-detail direction (Tony, May 31) | Not a finite item: stratosphere, troposphere, finer corona shells, solar magnetic storms, etc. 20/N5 is the on-ramp. NOTE: solar magnetic storms are time-varying -> lean on the animation track (Bucket C); that one straddles B and C. |

**Bucket C -- Architecture (each its own unhurried design session, design-
before-code):**

| # | Item | Notes |
|--:|------|-------|
| N6 | Studio editor review + encounter-event generator + Artemis redo | The data/provenance cluster. **Keystone RESOLVED (May 31): generator emits BOTH full-mission AND encounter-event forms** -- extend it to emit the event form (per-event note/dist_km/date_source + `resolution_note`) alongside the full-mission form. Then re-enter both Artemis presets through it with per-field sourcing (folds items 37/38). Also covers info-card routing, _studio patterns, fly-to, portrait/mobile. Highest leverage in Phase 5: pays down the one real correctness debt + removes a future class of provenance bugs. Zero-code design session FIRST. |
| N10 | Note-composition structural refactor | **Promoted this session** (was D-ARTEMIS "structural follow-on" prose). Renderer composes the encounter display note from resolved values + a template, so numbers can never be stored as stale prose again. The structural CURE for the fused-provenance disease. Sits behind N6's structured per-field data. Its own design session; do NOT fold into a redo under time pressure. |
| 21/51 | Animation track (three objectives) | **Re-scoped this session** from "wait until needed." Three objectives: (1) make non-center-body shells render in the animate path; (2) reduce animation-plot memory overhead; (3) consolidate animate with static plots for maintainability (the parallel-pipeline divergence). Architecture-and-design first; multi-session. |

### PARKED (Tony's explicit call to leave as-is)

| # | Item | Notes |
|--:|------|-------|
| N8 | Comet info-marker superposition cluster | Geometric, understood. Before any work: hover ikeya_seki, read labels, then design. |
| N9 | Codebase-wide white -> red orbit-marker switch | Keplerian/mean/actual info crosses. Deliberate whole-orrery visual change; not now. (Osculating marker intentionally stays white.) |

---

## DEFERRED ROUNDS (detailed -- absorbed from v17, May 30)

Two Phase-1 items grew past a citation fix into scoped rounds. Full detail
here so v17 can retire. Both are render-gated and file-gated -- new sessions,
current files uploaded.

### D-ARTEMIS -- Artemis II preset redo (ABSORBED into N6, May 31; re-scopes items 37, 38)

> **STATUS (v19):** D-ARTEMIS is no longer a standalone round. The redo is now
> a downstream step of N6 (Bucket C): fix the encounter-event generator first,
> then re-enter the presets through it. The keystone is RESOLVED -- the
> generator emits BOTH full-mission and encounter-event forms (extend it to the
> event form). The detail below is retained as the redo spec for the N6
> session. The "CRITICAL UNKNOWN" console check is tracked separately as N11
> (a standalone diagnostic, run independently of N6).

File: spacecraft_encounters.py, 'Artemis II' dict (3 entries: Earth departure,
lunar closest approach, reentry/splashdown). Authored entirely by Claude 4.6
(Apr 2, pre-flight); provenance untraceable.

WHY REDO, NOT PATCH -- the dict fuses three provenance classes behind one
misleading `'source':'NASA/JSC'` / `'date_source':'horizons'` stamp:
  - FETCHED (pipeline): position geometry from Horizons. For the lunar entry
    (date_source='horizons'), the override in palomas_orrery.py (~L1426)
    replaces dict date + dist_km with values resolve_encounter_time() derives
    from the trajectory. So dict date '2026-04-07' and dist_km 8900 are DEAD
    PLACEHOLDERS -- editing them is cosmetic.
  - RECALLED (Claude, pre-flight): every `note` string -- TCB times, "Apr 7
    23:06", FBC "11 km", "Apr 11" splashdown, records, CubeSats. None fetched,
    none overridden. This is what the audit flagged (L237/L268). Interim:
    claim-stripped to clear the audit; real content pending.
  - AUTHORITATIVE (as-entered, NOT overridden): the two
    date_source='authoritative' entries (departure, reentry). date + dist_km
    are live -- reentry '2026-04-11' / dist_km 6493 are real, date wrong (Apr 10).

CRITICAL UNKNOWN, resolve FIRST (render-in-the-loop): does the Horizons
override actually FIRE for the lunar entry? Override keys on
date_source=='horizons' (L1426) but resolve_encounter_time()'s docstring says
it activates on 'derive_from_horizons':True (spacecraft_encounters.py L589) --
the dict has NEITHER, only date_source='horizons'. The override sits in a
try/except that swallows failures (L1462), prints [HypOsc] on success.
  RENDER, WATCH CONSOLE. See "[RESOLVE] Deriving Moon closest approach for
  -1024..." + "[HypOsc] Using spacecraft encounter epoch" -> override fires,
  date/dist pipeline-sourced. DON'T see them -> override silently failed, the
  Apr-7 placeholder renders, date_source tag is decorative = a renderer bug to
  fix before any redo means anything. Single most informative step.

REDO METHOD (new session): (1) render, confirm [RESOLVE]/[HypOsc]; (2) lunar
geometry/date/dist from pipeline; (3) departure + reentry (authoritative) from
render or fetched NASA solution -- NOT auto-overridden; (4) event chronology
(TCB/RTCB, separation, parachutes, CubeSats, records) FETCHED from NASA post-
mission report via web_search + Gemini -- Horizons carries no narrative;
(5) rewrite notes with PER-FIELD provenance, no fused stamp; (6) re-scan.
Confirmed values for the rewrite: launch Apr 1, flyby/max-dist BOTH Apr 6
(~23:07 UTC), splashdown Apr 10; max dist ~406,771 km; closest lunar approach
~6,545 km; Apollo 13 record 400,171 km; FBC 26,500 ft (~8 km), drogues
25,000 ft, mains 9,500 ft, entry interface ~122 km, reentry ~11.2 km/s.
NOT adopted from Gemini (fetched beats recalled): "58.6 explicit in Ness 1986"
(abstract says 60); the skip-vs-direct reentry-speed story (unsourced); offset
0.33 (primary says 0.3).

STUDIO GENERATOR GAPS (verified in the v18 session -- folds into N6; read before any
studio update): the studio encounter-export generator CANNOT regenerate this
dict. Confirmed in gallery_studio.py:
  - Generator emits a FULL-MISSION form (center, select_also, start/end_date,
    plot_scale_au, fetch_step, label -- one block per spacecraft).
  - Artemis II uses the HAND-AUTHORED ENCOUNTER-EVENT form (discrete events,
    each with note/dist_km/date/date_source/resolution_note). Different shape.
  - resolution_note is hand-authored ONLY -- generator never emits it (zero
    occurrences in gallery_studio.py); only New Horizons + Artemis II carry it.
    (resolution_note = plot-FIDELITY transparency, not mission fact. The lunar
    entry's resolution_note holds the one genuinely-sourced string in the dict
    -- the real OEM filename Orion_OEM_20260401_0335.V0.1 -- PRESERVE it.)
  - CONSEQUENCE: "redo from pipeline" is NOT click-export-replace. Pipeline
    supplies NUMBERS; event STRUCTURE + resolution_note are hand-built.
  - FEATURE GAP for the N6 studio review: if the generator should ever produce
    encounter-event entries, it needs (a) per-event note/dist_km/date_source
    and (b) a resolution_note field. Decide deliberately: extend generator to
    the event form, OR keep event entries hand-authored and let the generator
    own only full-mission tracks. Do not let a redo silently assume coverage.

STRUCTURAL FOLLOW-ON -- **now tracked as N10 (promoted to the ledger, v19).**
Separate, larger, its own design session: renderer composes encounter notes
from resolved values + a narrative template, so numbers can never be stored as
stale prose again. The "unify the pipeline, make the seam structural" move. Do
NOT fold into the redo under time pressure.

### D-URANUS -- Uranus rendering cleanup (one session, render-in-the-loop)
File: uranus_visualization_shells.py (+ orrery_rendering.py for U2). Includes
item 39 (citation) and N2-orphan (tilt sign). Render the full Uranian system
FIRST; U2/U3 resolve by eye. (Related cosmetic items already in ledger: 18
gossamer ring visibility, N2 ring marker placement.)

39 (citation) -- **DONE (v18):** the `# Source:` comment below was applied at
L514-517, above `description = (`, and cleared Uranus from Tier-1. Recorded
here for the round's completeness; no action remains on the citation itself.
The 59/60 VALUE decision (U1) is what's still open in this round.
    # Source: Ness et al. (1986) Science 233:85 -- Voyager 2 magnetometer.
    # Dipole-vs-rotation tilt: abstract states 60 deg; refined value commonly
    # cited ~59 deg (58.6 deg). Dipole offset 0.3 R_U (~1/3 radius). Axial tilt
    # 97.77 deg (NASA Uranus fact sheet). Sidereal rotation ~17.24 h (17h 14m).

U1 -- 59/60 inconsistency (code says both). 59 deg: L5 docstring, L440/L547
#Source, L555 inline. 60 deg: L446 hover ("nearly 60" -- hedged, OK), L459
docstring, **L503 magnetic_tilt_deg=60 (LOAD-BEARING, drives geometry)**, L515
hover. Sourced truth: refined ~59 (58.6); "nearly 60" is outreach rounding.
Recommended: L503 -> 59 (source of truth), update L459 docstring, soften L515
to "nearly 60 degrees" (match L446); 59-deg comments then correct. Keeping 60
everywhere also defensible -- pick ONE; current state (neither) is the bug.

U2 -- magnetosphere tilt SIGN (render check). Magnitude verified (59-60). Sign
= lean direction, set in rotate_to_sunward() Step 1 (orrery_rendering.py ~L232):
+tilt leans dipole +Y, -tilt -Y in the YZ plane. CAVEAT: absolute azimuth is
rotation-phase-dependent (~17h, no epoch phase tracked) -> partly conventional.
Physically checkable: (1) magnetotail trails ANTI-sunward; (2) dipole ~59-60
deg off the ROTATION axis; (3) lean consistent with drawn poles. Render: Uranus
body-centered (799), magnetosphere + poles on, Sun identifiable; camera straight
DOWN THE X AXIS (tilt is in YZ plane -> face-on, zero foreshortening), up =
rotation axis. Tail sunward -> sunward-rotation bug (not sign). Tail correct but
dipole mirrors -> flip L503 negative; magnitude stays. NOTE: magnetosphere path
is INDEPENDENT of the 105-deg fudge (U3) -- separate transforms.

U3 -- 105-deg axial-tilt fudge (Tony: legacy, pre-osculating-orbits). THREE
sites use uranus_tilt=105 instead of nominal 97.77: L629, L759 (docstring),
L1010 (inline "best fit empirically"). Docstring L759: "empirically determined
to match satellite orbit alignment" -- a best-fit to MEAN-parameter moons, from
before the moons moved to osculating orbits. The reference 105 was fitted to has
changed -> alignment UNKNOWN until rendered. L772 "equatorial-to-ecliptic" note
reads as post-hoc rationale. Options: (1) derive tilt from IAU pole orientation
(RA/Dec -> ecliptic), same frame the osculating moons resolve in -- most correct,
geometry refactor; (2) re-fit the fudge -- cheap, re-arms the magic-number trap,
RESIST; (3) render first, decide nothing -- still aligns -> docs-only, off ->
evidence for Option 1. Recommended: 3 -> 1 if off.

U4 -- copy-paste "Saturn" comments (cosmetic): L651 "around Saturn's rotational
axis", L769 "Saturn's ring parameters" -- cloned from Saturn module. Fix while
in the file for U3.

Sequence: render full system -> judge U2 (sign) + U3 (105 alignment) by eye ->
apply U1 (pick one value, propagate) + 39 citation -> derive (Opt 1) if U3 off
-> fix U4 -> re-render -> smoke-test if hover data changed -> re-scan.

---

## Go-Forward Plan (next session entry point)

Order agreed with Tony May 31. Each is independently shippable; do not bundle
a verification task with a structural task (Separate the Problems).

**NEXT:**

1. **Phase 2 -- mechanical batch: items 49 + 53. START HERE.** The immediate
   "off the books" session. 53 (Neptune marker -> square-open) is a clean leaf;
   49 (Earth fly-to 0.15 AU) lives in `palomas_orrery.py` -> xvfb pre-test gate.
   One targeted Mode 1 session. (Item 19 left this batch -> Phase 5.)

2. **D-URANUS -- its own render-gated session.** U1 (pick 59 OR 60 and
   propagate; current bug is the code says both, L503 load-bearing), U2 (tilt
   sign -- face-on render down the X axis), U3 (105-deg fudge -- render first,
   decide nothing), U4 (copy-paste "Saturn" comments). The 39 citation is done.
   **Precondition:** confirm the uploaded `uranus_visualization_shells.py` is
   current at session start (verify-against-handoff). Render-in-the-loop.

**STANDALONE (run whenever, independently -- do NOT bundle into D-URANUS):**

- **N11 -- Artemis lunar-flyby console check.** ~2 min observation; tells us
  whether N6 inherits a live render bug. Separate from everything per Tony.

**SCHEDULED AFTER (unhurried, design-before-code):**

3. **Phase 5, Bucket A (completes/equips).** Items 24 (gas-giant bow shocks --
   higher priority, Mode 7), 23 (ionosphere), 19 (GUI axis control), 20/N5
   (shell-resolution enabler + HTML export lever). 19 + 20/N5 bundle (same
   file, xvfb gate). Bow shocks is the high-morale, pure-upside creative thread
   that also completes the standard geometry.

4. **Phase 5, Bucket C (architecture -- highest leverage, fresh sessions).**
   N6 (encounter-event generator + Artemis redo; keystone resolved -> build),
   N10 (note-composition refactor), 21/51 (animation three-objective track).
   Each gets a zero-code design session first. N6 pays down the one real
   correctness debt -- schedule it as a deliberate next design conversation,
   not a rush after Uranus.

5. **Phase 5, Bucket B (additive editorial).** Item 22 (satellite interiors)
   and the deeper-detail direction (stratosphere/troposphere/finer corona/
   solar storms). 20/N5 is the on-ramp; solar storms lean on the animation
   track.

**DEFERRED (documented, safe to leave):**

6. **Dead-code / honest-shell-files sweep.** Items 3, 5, 6, 7, 8, 2/40, 13,
   26, 28, N2, N3, N4 + the v9 dead-code detail. Low reward, high deliberation
   (the project's highest-trap zone -- burned twice editing/deleting the wrong
   thing). Deferring is safe because the code is dead AND documented here.
   When done: do NOT touch sphere-shell inline markers (N7 -- factory owns
   them); grep-confirm every deletion is unreached; smoke-test on the LIVE
   dispatch.

7. **Cosmetic polish + platform.** Items 17, 18, 41 (do-not-fix-manually), 9,
   61. Low priority, worth keeping. The only real decision is the
   SystemButtonFace fix (hex vs platform-detect vs ttk).

**PARKED:** N8, N9 -- leave until Tony reopens.

---

## Effort Calibration (model + thinking level per phase)

Governing principle: this project's expensive failures were NOT from
insufficient horsepower on hard problems -- they were confident
execution on an unverified base (the dead-code sweep, the "resume C4"
error, the partial review). So **thinking level tracks verification
risk and blast radius, not raw difficulty.** Spend thinking in
proportion to how INVISIBLE a wrong answer would be. A one-line edit
to a shared factory (83 render paths) deserves more deliberation than
a 50-line leaf edit.

| Phase | Model | Thinking | Where the effort goes |
|-------|-------|----------|-----------------------|
| 1 Factual verification | Opus 4.7/4.8 | High | Sourcing each claim, not editing. Epistemic, not architectural. Wrong-but-cited is worse than uncited. |
| 2 Mechanical bugs | Opus 4.6 | Medium | Almost none -- known shapes. |
| 3 Dead-code sweep | Opus 4.7/4.8 | High | Grep-confirm every deletion is unreached. Looks lowest-stakes, is highest-trap (the project has been burned twice deleting/editing the wrong thing). The LOTO "procedure that feels unnecessary right up until it isn't." |
| 4 Cosmetic/platform | Opus 4.6 / Haiku | Low-Medium | Only the platform-fix choice (hex vs detect vs ttk) needs a quick design call. |
| 5 Features | Opus 4.8 (design) -> 4.6 (impl) | High up front | Design conversation BEFORE building (iterate-design rule). Bow shocks / animation path may be Mode 7 candidates. Implementation can drop once design stabilizes. |

Cross-cutting:
- Anything touching `palomas_orrery.py` (item 19, dead calls living
  there) inherits the xvfb pre-test gate regardless of model -- that's
  procedural, not a thinking-level question.
- Model choice matters less than thinking-level choice on the
  mechanical phases. The failures were deliberation failures, not
  capability failures.
- Gemini Mode 7 is useful in specific contested or far-from-domain
  cases; it is NOT mandatory. Claude sourcing against authoritative
  references is proper grounding on its own.

---

## Verification posture for whatever comes next

Per protocol v3.24:
- Data-content edits (hover, legendgroup, marker) need a runtime
  smoke test against the LIVE dispatch (`build_sphere_shell` via
  SHELL_CONFIGS), not the per-body builders.
- Map the dispatch before editing leaves -- sphere-shell inline
  markers are dead code; custom geometry (magnetospheres, rings,
  belts) uses the inline path.
- Handoffs are claims; the render is fact. Smoke-test contradicts a
  handoff -> smoke-test wins.
- Enumerate the full uploads set before claiming a review.

---

## Lessons folded into project instructions in the v18 session (v3.24 re-issue)

- [CRITICAL] Enumerate uploads before claiming a review (the
  in-context subset is invisible to Tony and not authoritative).
- Floating items get lost; capture on first mention.
- Verify universal-propagation claims with grep, not narrative.
- Central factories need explicit migration intent.
- Testing iterates in dependency order (regression -> features ->
  animation).
- Smoke-test deferred pipelines for a KNOWN state.
- Handoff numbering rebased across versions is a drop source -- one
  running ledger.
- [NEW v18] Provenance scanner flags by NUMERIC token within a lookback
  window (30 lines for display strings). "Sourced for a human" != "sourced
  for the scanner": a `# Source:` comment must sit WITHIN lookback and in
  the `# Source:` form -- in-string "Source:" prose and distant comments do
  not count (item 36 root cause). Two honest ways to clear a finding: add a
  compliant `# Source:` comment, OR remove the numeric claims (claim-strip)
  when the data is recalled and not yet traceable (Artemis interim). Never
  paper a citation over recalled data.
- [NEW v18] A field's provenance tag is a CLAIM, not proof. `date_source:
  'horizons'` does not prove the Horizons override fired -- a swallowed
  exception can leave a placeholder rendering for weeks. Confirm at the
  render (console), not from the tag.
- [NEW v18] Studio generators and hand-authored dicts can be different
  STRUCTURES. The encounter export emits full-mission tracks, not encounter-
  event entries -- "regenerate from the tool" is not always available; check
  the output shape before assuming the generator covers a dict.

This session is itself the evidence: a prior review and the first
v3.24 edit were built on 9 of 19 uploaded handoffs, which produced a
"resume C4" recommendation for work finished 11 days earlier. The
full read corrected the record and recovered the dropped items.

---

## Credit

```
Go-forward re-scoping + ledger v19: Anthropic's Claude Opus 4.8 (May 31, 2026)
  -- no code changed; design conversation with Tony. Recorded May 29 round
     Mode-5 PASS; dissolved D-ARTEMIS into N6 (keystone resolved -> generator
     emits both forms); promoted note-composition refactor to N10; captured
     Artemis console check as N11; moved item 19 to Phase 5; shrank Phase 2 to
     49+53; re-scoped animation to a three-objective track; reorganized Phase 5
     into three buckets; marked dead-code sweep deferred; corrected the v18
     N-range leak.
Provenance Phase 1 + ledger v18: Anthropic's Claude Opus 4.8 (May 30, 2026)
  -- executed factual verification (items 36-39 + tilt sign), web_search
     sourcing + Gemini Mode 7 cross-check, Neptune citation applied, Artemis
     and Uranus re-scoped to deferred rounds; absorbed v17 + addendum into
     this single running ledger.
Consolidated ledger (v16): Anthropic's Claude Opus 4.8 (May 29, 2026)
  -- full read of 19 handoffs, numbering reconciliation, drop recovery,
     go-forward plan; no code changed.
Prior track credit preserved in v1-v15 (Opus 4.6 / 4.7 / 4.8, ~12 sessions).
Integrator: Tony Quintanilla -- carried context across every session,
  caught the dispatch dead-code, the 11-week-invisible marker, the
  partial-review gap, and (v18) the fused-provenance Artemis dict and the
  studio-generator structure mismatch.
```

---

*Paloma's Orrery | palomasorrery.com*

*"The in-context subset is invisible to Tony, and not authoritative --*
*enumerate the whole upload."*

*"One running ledger beats per-handoff renumbering."*

*"Three Claudes, one Tony, zero orchestration framework."*
