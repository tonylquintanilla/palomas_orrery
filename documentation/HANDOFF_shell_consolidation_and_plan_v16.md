# HANDOFF: Shell Consolidation -- Consolidated Ledger + Go-Forward Plan (v16)

**Date:** May 29, 2026
**Session model:** Claude Opus 4.8
**Supersedes:** v15 (and the entire v1-v15 chain for ledger purposes)
**Type:** Big-picture planning + drop-recovery. No code changed this session.
**Integrator:** Tony Quintanilla

---

## Why this handoff exists

The shell-consolidation track ran across ~19 handoffs (c2, c3, c4, d1,
d2, d2_v2, d3_1 v1-v12, stage_3 v14-v15). Item numbering was rebased
twice (c4: 1-22 -> D1: 1-41 -> D2: 42-54 -> D3.1: 55-61), then v8-v15
dropped the numbered table entirely for a "Stage 1-4" framing. Items
leaked at the seams -- most importantly the 4 Tier-1 provenance items
(D1 items 36-39) and a handful of small orphaned bugs.

This session read all 19 handoffs end to end and rebuilt ONE
authoritative ledger. From here forward, **this file is the running
ledger.** New items get appended with the next free number; nothing
gets renumbered. (Protocol lesson, v3.24 re-issue: handoff numbers
rebased across versions is a drop source -- one running ledger beats
per-handoff renumbering.)

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

### OPEN -- PRIORITY (real bugs + provenance, several orphaned in rebase)

Grouped by the KIND of work, because the kind sets the effort level
(see "Effort Calibration" below). Factual-verification items first
(fetched-not-recalled risk), then purely mechanical edits.

**Factual verification (Phase 1) -- claims that must be sourced against
an authority before asserting. The edit is trivial; the verification is
the work.**

| # | Item | File / locus | Notes |
|--:|------|--------------|-------|
| 36 | Provenance Tier-1: Neptune display string | neptune_visualization_shells.py ~line 590 (was 584) | 1 claim, no citation. Logged D1 May 19, never closed. FIX NOW per project rubric. |
| 37 | Provenance Tier-1: spacecraft display string | spacecraft_encounters.py line 237 | 2 claims, no citation. Same. |
| 38 | Provenance Tier-1: spacecraft display string | spacecraft_encounters.py line 268 | 5 claims, no citation. Same. |
| 39 | Provenance Tier-1: Uranus display string | uranus_visualization_shells.py ~line 515 (was 509) | 2 claims, no citation. Same. |
| N2-orphan | Uranus magnetic tilt SIGN verification | uranus (60 deg) | Was c4 "item 26"; orphaned when D1 reused 26. A physics fact (dipole orientation vs rotation axis), not a code question -- belongs with provenance because the failure mode is a confident wrong answer invisible until the right render angle. Magnitude correct; sign unverified. One-char fix if wrong. |

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

## Go-Forward Plan (next session entry point)

Recommended order. Each is independently shippable; do not bundle a
verification task with a structural task (Separate the Problems).

1. **Factual verification: items 36-39 + Uranus tilt sign.** Highest by
   the project's own rubric (Tier-1, score 16, FIX NOW), public-facing
   hover strings, oldest open items (since May 19), plus the orphaned
   tilt sign (same KIND of work). Source each claim against an authority
   (NASA/JPL, peer-reviewed, primary mission docs) via web_search, add
   `# Source:` comments, re-run `provenance_scanner.py`, confirm Tier-1
   drops to 0, confirm the tilt sign against a render. Claude sources
   and drafts citations with the actual reference; Tony verifies and
   applies. web_search is sourcing (fetched, not recalled) -- it
   satisfies the convention on its own; Gemini Mode 7 is optional, for
   a specific claim that smells contested, not a gate every claim
   passes through. **Precondition:** the four files (neptune, uranus,
   spacecraft_encounters) were not in the last deploy set -- confirm
   the uploaded copies are current before editing, or upload fresh.

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

This session is itself the evidence: a prior review and the first
v3.24 edit were built on 9 of 19 uploaded handoffs, which produced a
"resume C4" recommendation for work finished 11 days earlier. The
full read corrected the record and recovered the dropped items.

---

## Credit

```
Consolidated ledger (v16): Anthropic's Claude Opus 4.8 (May 29, 2026)
  -- full read of 19 handoffs, numbering reconciliation, drop recovery,
     go-forward plan; no code changed.
Prior track credit preserved in v1-v15 (Opus 4.6 / 4.7 / 4.8, ~12 sessions).
Integrator: Tony Quintanilla -- carried context across every session,
  caught the dispatch dead-code, the 11-week-invisible marker, and the
  partial-review gap that prompted this consolidation.
```

---

*Paloma's Orrery | palomasorrery.com*

*"The in-context subset is invisible to Tony, and not authoritative --*
*enumerate the whole upload."*

*"One running ledger beats per-handoff renumbering."*

*"Three Claudes, one Tony, zero orchestration framework."*
