# GALLERY BUILD HANDOFF v0.1 -- gallery_cache_builder.py (as-built)

Tony Quintanilla, PE | Claude | July 9, 2026

**Type:** BUILD (session record). The as-built companion to the executable
contract GALLERY_BUILDER_MANIFEST v2. Records what was built, the deltas from
the manifest that grounding surfaced, and -- load-bearing -- the LIVE gate that
is still pending because it cannot run in the build container.
**Base:** orrery HEAD `4e2629c` (copy sources) | gallery HEAD `4b086a6` (deploy
target). SHA round trip re-confirmed this session. Pushed at `<fill after your
commit>` -- update the chain when the files land.
**Companion:** GALLERY_BUILDER_MANIFEST v2 (contract); GALLERY_DATA_SOURCE_
HANDOFF v0.4 (design). **Ledger:** L-098 (parent); L-107 (copy-provenance sync
register); L-108 (master-plan drift).

================================================================
WHAT WAS BUILT (verified vs claimed)
================================================================
Three files, written and OFFLINE-verified in one warm-context session
(continuation of the v2/v0.4 convergence):
- `tools/gallery_cache_builder.py` -- the standalone nightly builder (~806 lines).
- `data/solar-system/objects_config.json` -- the 11-row seed (single authority).
- `tools/test_gallery_cache_builder_offline.py` -- offline mocked-Horizons suite.
Plus a 3-line `.gitignore` add (in-tree ignored `data/solar-system/.staging/` +
`data/solar-system/backup/`, matching the orrery's own `data/` layout).

VERIFIED (in the build container): `py_compile` clean; the offline suite passes
47 checks / 0 failures; all three files ASCII-clean; every copied specific
carries a provenance comment to orrery `4e2629c`.
NOT VERIFIED here (by nature -- see the live gate): anything touching JPL
Horizons. The container has no network route to `ssd.jpl.nasa.gov`, so the
offline suite MOCKS the fetch layer. It proves the pipeline LOGIC, not the fetch.

================================================================
AS-BUILT DELTAS FROM MANIFEST v2 (what grounding changed; carry these)
================================================================
Reading the real orrery code at HEAD (not the manifest's summaries) surfaced
four places where the as-built differs from or sharpens the manifest. None
change the design; all make it correct.

1. **Served schema is the FULL v0.6 shape, not manifest S6's shorthand.** S6
   sketched a lean object (elements + orbit_type + anchor + as_of_today + ...).
   The schema the browser actually consumes (export_orbit_cache.py at HEAD) is
   richer: per object `name, horizons_id, category, availability, parent,
   stored_center, canonical_frame, trajectory_of, osculating{center, epoch_jd,
   a_au, e, i_deg, node_deg, peri_deg, M0_deg, source}, positions{file, start,
   end, n_points, size_kb}, presets, features`; index adds `serving_base
   (as generator/attribution), feature_configs, scene_features, model`. The
   builder emits that exact shape (schema PARITY) PLUS the conic additions
   (`orbit_type`, `as_of_today` km, comet `Tp_jd`/`solution_Tp_jd`/
   `max_distance_au`, `event_link`, top-level `attribution`/`served_window`).
   No renames, no drops -- the browser contract is unchanged.

2. **`trace_policy` is MODEL-derived, not carried from TEST_OBJECTS.** The
   desktop TEST_OBJECTS `trace_policy` field carries `serve`/`none` -- the
   RETIRED Stage-2 relative-trace vocabulary (Earth/Titan/etc. are `serve`
   there). The builder's `trace_policy` is a different axis (`none`/`full-arc`)
   and under the conic model is derived: every non-spacecraft is `none` (conic +
   as-of-today), only voyager_1 is `full-arc`. Copying the desktop field
   verbatim would have mis-tagged seven objects. Manifest S2's "carried verbatim
   from TEST_OBJECTS" holds for ids/centers, NOT trace_policy.

3. **Comet Tp resolver ADAPTED to Path-2-only + nightly re-resolve.** The desktop
   `resolve_tp` (osculating_cache_manager.py:566) is a four-path hierarchy whose
   Paths 1/3/4 lean on the orrery osculating cache. The standalone builder shares
   no cache, so its comet path collapses to Path 2: live `fetch_solution_tp`
   (solution TP LOCATES perihelion) -> fetch osculating elements AT that epoch ->
   serve the element set's OWN osculating TP as the converged anchor (residual
   `solution_TP - converged_osc_TP` = the non-grav/outgassing shift, both served).
   Re-resolved nightly so a republished JPL solution is picked up. The provenance
   comment names the dropped paths. Verified against the desktop LEAF
   (idealized_orbits.py:7089): the leaf reads `osc_tp_at_perihelion =
   elements.get('TP')` and computes exactly this residual -- the correction in
   F4 is faithful.

4. **A coarse `#U` unit-sanity ABORT was added.** Manifest S6's `#V` re-applied
   the Guard band to served numbers. Since F8 made the Guard a MONITOR (warn),
   the band-on-served became warn too -- but a KM_PER_AU/derive conversion bug is
   a BUILDER bug that should still ABORT. So `#U` (served |r| must be km-scale,
   not AU-scale) is a distinct structural abort; the narrow contamination band
   stays a warn. Validation split as-built: structural invariants (#2,#3,#5,#6,
   #8,#C,#T,#W,#U) + shrink gate ABORT; Guard v2 + B3 WARN.

================================================================
WHAT THE OFFLINE SUITE VERIFIED (47 checks)
================================================================
first-build -> derive -> structural validation -> atomic swap across all 11
objects; full v0.6 schema parity + the conic additions; `as_of_today` km-scale;
spacecraft positions-with-no-osculating; comet `Tp_jd`+`solution_Tp_jd`;
pluto/charon on `pluto_barycenter`; the elements JSONL history + per-run
manifest; a nightly re-run leaving the frozen past byte-for-byte stable and
passing the shrink gate; and -- the F8 teeth -- the Guard MONITOR warning-and-
KEEPING a 35.7 AU point (tagged `likely-contamination`) instead of rejecting it,
plus the spacecraft `|r|>200 AU` sanity warning.

================================================================
PENDING LIVE GATE (Tony's hardware -- the authoritative render)
================================================================
The offline pass is NOT live verification. Run in manifest S10 order:
1. `--dry-run --object voyager_1` -- confirm the ephemeris START is discovered
   from Horizons (not launch+1) and NO future is fetched.
2. `--dry-run --object encke` -- confirm the solution-Tp two-role resolution
   runs, the `2P` apparition disambiguation picks the current record, and the
   served `Tp_jd` MATCHES the desktop `resolve_tp` result (Mode 5 -- a valid-
   looking conic is not proof the epoch is right).
3. Inject one out-of-band point; confirm the Guard BANNER fires loudly (not a
   silent accept, not a reject).
4. Confirm the backup action + `.gitignore` entry exist BEFORE the first build
   (L-106 precondition).
5. First full build; spot-check `raw/vectors/charon.json` magnitudes; confirm
   `coverage_index.json` (attribution, served_window, as_of_today km,
   pluto/charon centers).
6. Schedule `--nightly` + the separate backup action; probe GitHub Actions.
Treat the first `--dry-run` as the ground truth; the offline pass and the code
reading are a sound draft, not a rendered fact.

================================================================
DOCUMENTATION STATUS
================================================================
- Ledger L-098 advanced (build done, offline-verified; live gate next); Ref +
  spawned-items updated. L-107 opened (copy-provenance sync register -- the
  managed exception to the parallel-pipeline anti-pattern). L-108 opened.
- Manifest v2 gets a one-line as-built pointer to this handoff (S2/S6 deltas).
- MASTER PLAN (MASTER_PLAN_INTERACTIVE_GALLERY.md v10) is STALE on Phase 1b and
  NOT edited this session: section-5 Deliverable #1 + section-3a still say the
  export script "reads desktop caches" (the pre-pivot model the v0.4 fetch-fresh
  design retired), and the Status line says v0.3 while the changelog says v0.4.
  The drift is pivot-driven, not build-driven; captured as L-108 for a focused
  v10 -> v11 pass (Tony's roadmap call), not folded silently into this close-out.

---

BUILD handoff v0.1 written July 2026 with Anthropic's Claude Opus 4.8; built +
offline-verified this session. Companion: GALLERY_BUILDER_MANIFEST v2.
