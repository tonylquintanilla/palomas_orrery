# HANDOFF: Shell Consolidation -- Consolidated Ledger + Go-Forward Plan (v18)

**Date:** May 30, 2026
**Session model:** Claude Opus 4.8
**Supersedes:** v16 AND v17 (and the Phase-1 addendum) -- single running ledger
**Type:** Provenance Phase 1 executed + ledger update. Code changed: Neptune
citation applied (item 36 closed). Two items re-scoped to deferred rounds.
**Integrator:** Tony Quintanilla

> **This is the one document to follow.** v17 (Provenance Phase 1) and the
> Phase-1 addendum are now ABSORBED here and retired -- do not carry them
> forward. Their detail lives below: item 36 closed, 37/38 re-scoped to
> D-ARTEMIS, 39 ready-to-apply, the Uranus tilt sign expanded into the
> D-URANUS round, and new studio-generator findings folded into N6. The
> ledger rule still holds: nothing renumbered; new items appended.

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

## PHASE 1 EXECUTED (this session, May 30 -- provenance verification)

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
assigned N1-N10 here for the first time. Status as of May 29, 2026.

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
| 37 | Provenance Tier-1: spacecraft display string | spacecraft_encounters.py line 237 | **RE-SCOPED -> D-ARTEMIS.** note claim-stripped interim to clear audit; preset redo pending. |
| 38 | Provenance Tier-1: spacecraft display string | spacecraft_encounters.py line 268 | **RE-SCOPED -> D-ARTEMIS.** Same. |
| 39 | Provenance Tier-1: Uranus display string | uranus_visualization_shells.py L514-517 | **CLOSED** (v18) -- `# Source:` comment applied above the magnetosphere `description`, verified in uploaded file. (59/60 VALUE decision still open -> D-URANUS U1; displayed string still reads 60.) |
| N2-orphan | Uranus magnetic tilt SIGN verification | uranus (60 deg) | **EXPANDED -> D-URANUS U2.** Magnitude verified; sign is render-gated. |

**Mechanical edits (Phase 2) -- no verification trap; shape is known.**

| # | Item | File / locus | Notes |
|--:|------|--------------|-------|
| 49 | Earth fly-to-Sun distance hardcoded 0.15 AU | (Gap B, D2) | Geometry bug; never closed. |
| 53 | Neptune magnetic center marker convention | neptune | Should be `square-open`, not `diamond` (marker symbol convention). |
| 19 | Manual axis dtick in orrery GUI | palomas_orrery.py GUI | Tony feature request; ties to 3D Axis Control Convention. Gallery Studio has it; GUI does not. Mode 1 snippets. |

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

### OPEN -- FEATURE / PHASE E (separate scoped sessions)

| # | Item | Notes |
|--:|------|-------|
| 20/N5 | Shell Resolution GUI control | Two knobs (sphere/ring) + exemptions. Bundle with HTML export mode (same file-size lever). |
| 21/51 | Animation: non-center body shells do not render | Larger animation-path work. |
| 22 | Satellite internal structure shells | Phase E creative / Mode 7. |
| 23 | Earth ionosphere shell | Phase E editorial. |
| 24 | Gas giant bow shocks (Jupiter/Saturn +) | New paraboloid geometry; co-toggle design. |
| N6 | Studio editor comprehensive review | Info-card routing, _studio patterns, fly-to, portrait/mobile. Own scoped audit session. |

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

### D-ARTEMIS -- Artemis II preset redo (re-scopes items 37, 38)
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

STUDIO GENERATOR GAPS (verified this session -- folds into N6; read before any
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

STRUCTURAL FOLLOW-ON (separate, larger -- its own design session): renderer
composes encounter notes from resolved values + a narrative template, so
numbers can never be stored as stale prose again. The "unify the pipeline,
make the seam structural" move. Do NOT fold into the redo under time pressure.

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

Recommended order. Each is independently shippable; do not bundle a
verification task with a structural task (Separate the Problems).

1. **Provenance Phase 1 -- COMPLETE this session. Tier-1 = 0 (May 31 audit).**
   Neptune + Uranus citations applied and verified; both Artemis notes claim-
   stripped (interim). Nothing remains to drive Tier-1 down. The two tails are
   scoped rounds, NOT provenance work: **D-ARTEMIS** (preset redo -- render-in-
   the-loop, fetch mission narrative; replaces stripped prose with traceable
   content) and **D-URANUS** (U1 59/60 value decision + U2 tilt sign + U3
   105-deg fudge + U4 comments; the 39 citation is already done). Both new
   sessions; both render-gated. **Precondition unchanged:** confirm uploaded
   copies of uranus/spacecraft_encounters are current before editing.

2. **Mechanical small-bug batch.** Items 49 (Earth fly-to 0.15 AU),
   53 (Neptune marker square-open), 19 (manual axis dtick GUI). No
   verification trap left in this batch once the tilt sign moved to
   Phase 1. One targeted Mode 1 session.

3. **Dead-code / honest-shell-files sweep.** Items 3, 5, 6, 7, 8,
   2/40, 13, 26, 28, N2, N3, N4 + the v9 dead-code detail.
   Leverage-preserving, no visual change, deferrable but well-scoped.
   IMPORTANT: do NOT touch sphere-shell inline markers (N7 -- dead
   code; factory owns them). Grep-confirm every deletion is truly
   unreached; smoke-test on the LIVE dispatch.

4. **Cosmetic polish + platform.** Items 17, 18, 41 (do-not-fix-
   manually), 9, 61. Bundle.

5. **Features, one session each.** Items 20/N5, 21/51, 22, 23, 24, N6.

6. **Parked:** N8, N9 -- leave until Tony reopens.

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

## Lessons folded into project instructions this session (v3.24 re-issue)

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
