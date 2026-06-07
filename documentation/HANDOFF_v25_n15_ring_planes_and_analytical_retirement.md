# HANDOFF v25 -- N15 Ring-Plane Migration + Analytical-Orbit Retirement + UI fixes

**Date:** June 4, 2026
**Session model:** Claude Opus 4.8
**Supersedes:** v24 -- single running ledger; v24's bow-shock / magnetosphere track
and the v23 shell-consolidation D-track carried forward by reference (Section 8).
Nothing renumbered.
**Type:** CODE CHANGED, TESTED, PUSHED -- round trip complete. Seven files edited;
all compile, ASCII-clean, LF; live-dispatch smoke ALL PASS; Tony Mode-5 render PASS
on every body; provenance re-run PASS; committed and pushed; project knowledge
auto-synced from GitHub.
**Built on:** GitHub repo HEAD `d33eb0c` (branch main).
**Pushed at (new HEAD):** `7140b9c03c4df132b188d24c32ceb32fa8d7e7be` -- next session's
base. Verified against remote: all seven changes present, LF-clean.
**Integrator:** Tony Quintanilla

> **One document for the N15 ring-plane / analytical-orbit track.** Two earlier
> tracks remain authoritative by reference and were untouched this session: v24
> (bow shocks + magnetosphere nest, Movement 1; Movement 2 dipole cone still
> queued) and the v23 shell-consolidation D-track. This session did three things:
> small UI fixes, the N15 ring-plane migration, and the retirement of the legacy
> analytical moon-orbit pipeline for Jupiter and Mars.

---

## 1. WHAT THIS SESSION DID

**UI fixes (3 files), confirmed by render.**
- Mercury sodium-tail info marker was anchored at tail_distance=0 = planet center,
  occluded by the body when Mercury is selected. Moved down the anti-sunward tail
  axis (3.0 R_M, a Mode-5 knob), per the single-info-marker convention.
- Venus magnetosphere hover and Venus upper-atmosphere hover were essay-length
  walls overflowing the hover window on both axes. Condensed to ~7-8 short lines
  each, sourced numbers preserved. DISPATCH CATCH: the upper-atmosphere hover is a
  sphere shell, so its live hover_text lives in `shell_configs.py` (SHELL_CONFIGS
  Venus upper_atmosphere), NOT the inline `description` in venus.py (dead code for
  sphere shells). Editing venus.py there would have changed nothing -- the v3.24
  trap, avoided by mapping the dispatch first.

**N15 ring-plane migration (3 files) -- the main work.** All ring systems now
orient by the IAU pole vector via `orient_to_planet_pole`, replacing hardcoded
axial-tilt rotations. Validated 0.000 deg to the pole by the new smoke test, and
PASS on Tony's Mode-5 render against each body's ring-plane moons.
- Jupiter rings: had NO rotation (~2.2 deg off); now oriented. Ring info marker
  also moved onto the ring (was placed independently on +X).
- Saturn rings + Enceladus plasma torus + radiation belts: all three shared the
  hardcoded -26.73 deg X-tilt (~5 deg off, right magnitude / wrong node); all
  migrated.
- Neptune rings: retired the empirical 32 deg X + 34 deg Z fudge (8.57 deg off).
- Uranus was already migrated in v23 (0.0 deg) -- regression anchor only, unchanged.

**Analytical moon-orbit retirement (1 file: idealized_orbits.py).** Removed the
dual-orbit analytical pipeline (`plot_satellite_orbit` call) from the live dispatch
for Jupiter and Mars moons. All major-planet moon systems are now OSCULATING-ONLY
(+ actual), consistent across Mercury..Neptune. Rationale: the analytical path used
hardcoded single-axis tilt fudges (Jupiter 3.13 deg, Mars 25.19 deg Y, both found
empirically) that never aligned exactly with the actual orbit -- a frame artifact,
not perturbation. Osculating elements are already ecliptic and track the actual
path. Render-confirmed: Jupiter eyeballs perfectly; Mars render is clean and
coplanar (the "beautiful" image).

**Discovery (no change made).** Heliocentric "mean orbits" (`add_mean_orbit_trace`)
ARE implemented and wired (elliptical + hyperbolic Keplerian paths, gated on the
object being in `planetary_params`), but each trace is added with
`visible='legendonly'` -- present in the legend, hidden until toggled. That is why
they were "not seen." They apply to heliocentric objects only; moons never call
`add_mean_orbit_trace`. Left as-is (legend-only is a reasonable anti-clutter
default).

---

## 2. N15 OFFSET TABLE (current-code vs IAU pole, pre-migration; method validated)

    Body      Old ring orientation               Offset    After
    Uranus    orient_to_planet_pole (v23)         0.0 deg   unchanged (anchor)
    Neptune   hardcoded Rx(32) + Rz(34)           8.57 deg  -> 0.000
    Saturn    hardcoded Rx(-26.73) (tilt only)    4.99 deg  -> 0.000
    Jupiter   no rotation                         2.22 deg  -> 0.000

Method validated by reproducing Tony's measured Neptune 8.57 deg with the exact
normals (0.296, -0.439, 0.848) vs (0.356, -0.307, 0.883). Smoke test confirms all
migrated structures (rings, Saturn torus, Saturn belts) land 0.000 deg on the pole.
Root cause was ONE pattern: a single hardcoded axial-tilt rotation reproduces tilt
magnitude but not the node (the pole's x-component), so it misplaces the plane.

---

## 3. REASONING TRAIL, TONY-CATCHES, LESSONS

The lineage worth recording (the throughline, not a list of deletions):
**normal-vector idea (early) -> hand-fit tilts (kept Mars/Jupiter because they
worked at low obliquity, dropped Saturn/Uranus/Neptune as unreliable) -> osculating
method (suggested by an earlier Claude) made the analytical curves redundant rather
than wrong -> N15 implements the normal-vector idea correctly as
orient_to_planet_pole -> analytical retired across the board, deferred for a proper
pole-transform revival.** Two years of the double helix, with the AI assistants
improving in the middle of it.

- DISPATCH BEFORE LEAVES (twice). Venus upper-atmosphere hover lives in
  shell_configs, not the venus.py inline description (dead for sphere shells).
  Neptune's ring tilt at line 1637 was confirmed inside the live builder (no
  intervening def) before editing -- the prior "wrong function" incident not
  repeated.
- SWEEP SIZING BY GREP. N15 started as "fix Neptune" but the grep found Saturn on
  the same pattern (~5 deg) and Jupiter (~2 deg), then found Saturn's torus + belts
  sharing the identical -26.73 tilt. Tony chose all four + torus/belt. "Don't let
  'just fix Neptune' win by default before the grep" held.
- COMPLETE FILES FROM A VERIFIED BASE. Tony asked for complete files (his pipeline
  replaces whole files). Done surgically: repo-HEAD bytes + only the agreed edits,
  each splice asserting one match, py_compile + diff to preserve localized review.
  Filename-retention bug (short names vs repo *_visualization_shells.py names)
  caught by Tony and fixed.
- PIPELINE CHANGE. Project knowledge now auto-syncs from the GitHub repo via the
  connector (no manual add/delete step). This kills the v3.26 failure class at the
  source: the stale-snapshot duplicate and the served ghost both came from the
  manual step. -> v3.27 (Section 9).
- SHA IS THE ANCHOR. Tony first pasted the base SHA (d33eb0c) as the post-push
  HEAD; an unchanged hash after a seven-file commit is impossible, so it was
  flagged and the real HEAD (7140b9c) read from the remote. The two-hash check did
  its job.
- LINE ENDINGS. GitHub noted an LF->CRLF change on idealized_orbits.py; the pushed
  repo copy was verified LF-clean (git normalized on commit). Repo convention holds;
  any CRLF is local-working-tree only.
- TETHYS / TRITON ARE EXPECTED PHYSICS, NOT BUGS. Neptune rings match Despina /
  Galatea but NOT Triton -- correct: Triton is retrograde (~157 deg), it SHOULD be
  off the ring plane. Saturn's Tethys reads ~1 deg off the others -- that is
  Tethys's real inclination; a frame error would tilt ALL moons together, a single
  moon off is its own inclination. The osculating hover shows the fetched value.

Quotable (for v3.27): **"Our work is not just right -- it's beautiful." -- Tony,
June 2026.** Marks the session where "Tony's eyes win" extended from correctness to
aesthetics -- the render that confirmed the frames were correct was the same one
that was lovely; they turned out to be the same thing.

---

## 4. DEFERRED / LEDGER

- **Analytical moon orbits via orient_to_planet_pole (deferred, OPTIONAL feature).**
  Now that the pole transform is validated, a CORRECT analytical orbit (unlike the
  retired hand-fit fudges) is feasible. **Saturn is the lead candidate**: prominent
  rings, many co-planar moons, and the scaffolding already half-exists
  (`calculate_saturn_satellite_elements`, currently gated off with limited data).
  The documented skip-reason for Saturn moons ("reference frame transformation
  complex, pole RA=40.58") is exactly what N15 solved. Per body: build orbit in
  parent-equatorial (Omega_z, i_x, omega_z), then orient_to_planet_pole to ecliptic.
  CAVEAT vs rings: an orbit carries node (Omega) and periapsis (omega), so the
  element FRAME / node convention must be verified per body -- the residual
  "complexity" beyond the pole tilt. Mars also needs an IAU pole ADDED to
  `planet_poles` (only `planet_tilts['Mars']` exists today). Render-gated. Frame as
  "worth it only if it adds something for Paloma," not as debt.
- **Small-body analytical tail (separate evaluation).** TNO_MOONS and the
  Patroclus-Menoetius barycenter orbiters (~line 5174) still call
  `plot_satellite_orbit` via the generic-parent path. Evaluate whether they show the
  same artifact before deciding to migrate or retire; rarely-plotted edge cases.
- **D3 dead-code (annotate, do NOT remove yet):**
  - `saturn_visualization_shells.py`: `rotate_points` import now unused after N15.
  - `idealized_orbits.py`: `plot_satellite_orbit`'s named-planet analytical branches
    (Mars 25.19, Jupiter 3.13, and the Uranus 105-deg fudge that U3 retired for
    rings but which still squats here) are reachable in the live render only via the
    small-body generic path + the `compare_transformation_methods` test function.
    `calculate_jupiter_satellite_elements` / `calculate_saturn_satellite_elements`
    are now effectively unused in the live render.

---

## 5. LIVE FLAGS / ASSUMPTIONS

- `orient_to_planet_pole` / `planet_poles` covers the four giants only. NOT Mars
  (just `planet_tilts['Mars']`). Adding Mars's IAU pole is the prerequisite for any
  Mars analytical revival.
- Heliocentric mean-orbit traces default to `visible='legendonly'` (line ~344 of
  idealized_orbits.py). One-line flip to `visible=True` if a visible default is ever
  wanted; treat as a deliberate decision, not a fix.
- N15 smoke proves rings sit ON the pole, not that the pole matches the MOONS;
  Horizons is unavailable in-container, so ring-vs-moon agreement is the Mode-5
  render gate (passed this session).
- Plotly Scatter3d ignores marker.line.width (#4118) -- contrast is via fill color.
  3D symbol palette is the 8-symbol set. (Standing facts.)

---

## 6. FILES + INTEGRATION

Built on repo HEAD `d33eb0c`; pushed at new HEAD `7140b9c`. All verified present
and LF-clean at the remote.

    mercury_visualization_shells.py   sodium-tail info marker offset off-center
    venus_visualization_shells.py     magnetosphere hover condensed
    shell_configs.py                  Venus upper-atmosphere hover_text condensed
    jupiter_visualization_shells.py   ring orient via pole + marker-on-ring
    saturn_visualization_shells.py    ring + torus + belt orient via pole
    neptune_visualization_shells.py   ring orient via pole (32/34 fudge retired)
    idealized_orbits.py               Jupiter + Mars analytical-orbit removal

New project artifacts (in repo / sandbox):
    smoke_ring_planes.py              live-dispatch ring-plane smoke (re-runnable)
    TEST_PROTOCOL_n15_ring_planes.md  4-layer protocol (all layers PASS this session)

---

## 7. CARRIED FORWARD (by reference; unchanged this session)

- **v24 bow-shock track:** Movement 1 (bow shocks for all 8 bodies + magnetosphere
  nest) complete and pushed. The sourced nest table (magnetopause / bow-shock
  standoffs) and Movement-1 deferred precision items stand.
- **Movement 2 (queued, next major work):** Uranus / Neptune dipole tilt cone +
  spin axis (the first real consumer of the pole-vector producer); Uranus/Neptune
  bow-shock tilt enclosure (Neptune flank poke is the known artifact); Mercury
  +0.2 R_M northward dipole offset. Note: the "rotation-axis arrows at the poles"
  idea and Movement 2's spin axis are the same primitive.
- **v23 shell-consolidation D-track:** U-items, provenance Phase 1 (Tier-1 = 0),
  dead-code D3 sweep, and the broader on-the-horizon backlog (Phase D sun_position
  threading, comet presets, Spacecraft Mission Explorer, Food Insecurity module,
  ERA5/Western Heatwave, gallery pipeline). None touched.

---

## 8. NEXT-SESSION PRIORITIES

1. Movement 2: the dipole tilt cone + spin axis (first pole-frame consumer),
   folding in the Uranus/Neptune tilt enclosure and the Mercury north offset.
2. Optional, if educational value justifies: the deferred analytical-via-pole
   feature, Saturn first (build on calculate_saturn_satellite_elements; add Mars
   pole if extending to Mars). Verify Omega/i frame per body; render-gated.
3. v3.27 protocol edit: record the pipeline change (project knowledge auto-syncs
   from GitHub; manual add/delete retired), add the "right and beautiful" quotable,
   and reaffirm SHA-as-anchor (the base-vs-HEAD catch this session).

Session-start: pull build targets from repo HEAD `7140b9c`, SHA-pin, build on
repo/upload only (v3.26). Run smoke_ring_planes.py from a clean dir.
