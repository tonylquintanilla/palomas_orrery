# GALLERY BUILD HANDOFF v0.1 -- gallery_cache_builder.py (as-built)

Tony Quintanilla, PE | Claude | July 9, 2026

**Type:** BUILD (session record). The as-built companion to the executable
contract GALLERY_BUILDER_MANIFEST v2. Records what was built, the deltas from
the manifest that grounding surfaced, and -- load-bearing -- the LIVE gate that
is still pending because it cannot run in the build container.
**Base:** orrery HEAD `4e2629c` (copy sources) | gallery HEAD `4b086a6` (deploy
target). SHA round trip re-confirmed this session. The initial local build
committed at gallery `a2b7435` was never pushed; the L-109-remediated build is
re-pushed by Tony (gallery SHA pending); the docs landed at orrery `ca5c052`.
**Remediation (L-109, July 10):** Fable 5 adversarial review -> Pass 1 (A-1
crash-recovery / archive-loss seam, A-2 exit code, A-7, A-8, A-11) + Pass 2 (A-3
last-good serve, A-4 id_type, A-5 CAP;, A-9 #T, A-10, B-3 parity fields) +
spacecraft fetch REDESIGN (authoritative start + coarse/windows/Douglas-Peucker,
dissolving A-6). Offline suite 47 -> 63 checks, 0 failures.
**Remediation Pass 4 (L-110, GPT competitive cross-check):** N1 whole-generation
atomic swap (staging sibling renamed as one unit; a crash leaves a COMPLETE old
or new generation, one prior retained as rollback); N2 verified push
(committed_local vs pushed_remote; a silent push failure no longer reads as
published -- the a2b7435 failure mode); N3 object-set continuity + first-build
minimum-count floor; N4/N6 #B3 conversion-consistency replaces the absolute #U
threshold and retires the phantom B3 claim; N5 structured solution-TP outcomes
(operational failure serves last-good, not a silent today-anchor). Offline suite
63 -> 68 checks, 0 failures.
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

## Open items and deferred work (as of Pass 4, July 10 2026)

Captured so nothing floats loose. None of these block the first live dry-run;
the operability set (Pass 5) should land before the job runs UNATTENDED. Items
are drawn from Tony's questions and the un-actioned remainder of both reviews
(Fable 5 / L-109, GPT 5.5 / L-110).

### Operability -- Pass 5 (highest value: makes the unattended job legible)

- **Deployment model (DECIDED July 10).** Automatic FETCH, manual PUSH. Task
  Scheduler runs the builder nightly WITHOUT `--commit`: it fetches, validates,
  swaps the new generation into the LOCAL tree, and writes the summary. Tony reads
  the summary and pushes by hand. This keeps commit authority with Tony (the
  standing rule) and makes N2 push-verification advisory -- Tony is the eyes-on
  confirm that already caught the a2b7435 miss. The summary is the handoff between
  the overnight run and the morning push.
- **New-object onboarding (Tony Q1).** A nightly only refreshes recent dates and
  copies the archive forward; a newly-added config object has nothing to copy
  forward, so it needs a ONE-TIME backfill. `--first-build` re-backfills
  EVERYTHING (wasteful); `--dry-run --object` writes nothing. Add a `--add-object
  <slug>` mode: backfill just the new object (365d arc / full flown arc) into the
  existing generation, then nightlies maintain it. Interacts correctly with N3 --
  a new object appearing is allowed; an existing one vanishing aborts.
- **Gap-aware catch-up (CORRECTNESS -- do before unattended).** The nightly
  currently fetches a FIXED trailing window `[today - freeze, today]` anchored to
  TODAY, so if the builder is dark longer than `freeze` (machine off, travel) the
  gap days are SILENTLY skipped -- a hole in the archive. Fix: anchor the refresh
  window to the ARCHIVE's last date, `[last_archived_date - refine_overlap,
  today]`, so a run fills whatever gap exists and self-heals an outage. The small
  backward `refine_overlap` only re-fetches recently-refined spacecraft points
  (planets/moons are stable); it is NOT a stopping point -- the fetch continues
  from wherever the archive ends. Missed PUSHES are harmless (increments
  accumulate locally, commits queue, one push catches GitHub up); missed RUNS are
  the case this fixes.
- **Run summary (Tony Q2).** A `_health.md` written EVERY run: status (swapped /
  aborted), per-object result, the warning list, the COMMITS-PENDING-PUSH count,
  and an explicit PUSH / DO-NOT-PUSH verdict. NO email or phone notification --
  the summary file is the mechanism (Tony's call). Likely-contamination sets the
  verdict to DO-NOT-PUSH rather than the builder refusing, since the push is manual.

### Correctness / hardening -- deferred

- **N7 time-scale / date-key (UTC-only, DST-immune).** Make the builder's date
  arithmetic wholly UTC-INTERNAL -- fetch epochs, date keys, and the 'today'
  anchor all in UTC -- so neither the 69 s `utc_to_tdb` approximation nor a DST
  shift can misassign a date key near midnight (same boundary bug: one ~a minute
  wide, one an hour wide twice a year). Local time then matters ONLY for when the
  scheduler fires. Verify the boundary at the live gate.
- **N8 as_of_today exactness.** `#T` catches gross staleness (48 h); add an
  explicit today-key check + carry the DATE on the served point + a `stale` flag
  so the browser need not infer it and a clipped trailing edge is visible.
- **N10 unit handling.** Prefer reading Astropy column UNITS over the
  `q > 10000` km/AU magnitude heuristic; keep the heuristic only as a logged
  compatibility fallback. Needs live column evidence.
- **Guard warning payload (Fable).** `emit_guard_warnings` should carry the
  fetch params (epoch window, id_type, center) the warning is about.
- **warnings_log surfacing (Fable).** The warnings list is printed only on the
  success path; on ABORT / dry-run it is not surfaced -- fold it into
  `_health.json` (Q2) so it survives every path.
- **Guard scan scope (Fable).** The guard re-scans the whole archive nightly (a
  frozen contaminated point warns forever; Voyager's full-arc sanity loop runs
  nightly). Consider scan-the-refresh-window; low priority.
- **Schema-shrink continuity (GPT).** N3 guards object-set membership; a
  finer gate on per-object schema fields / position references / center changes
  is still only partial (#C + #8). Low priority.

### Tests / fixtures

- **N11 real-response fixtures (GPT).** The offline suite mocks Horizons
  (pipeline logic). Add sanitized LIVE fixtures captured at the first dry-run for
  column names / units / masks, header parsing, target ambiguity, empty / clipped
  ranges, and center strings. Build the identity matrix (slug -> requested
  target / id_type / location -> returned name / center / frame) and abort
  first-build on mismatch.

### Cleanup / consistency

- **Dead code.** `_replace_file` is unused after the whole-directory swap (N1)
  retired the per-subtree promotion -- delete on the next pass.
- **Severity threshold.** Code / manifest say the outer guard tier fires at
  >= 10x; handoff v0.4 change 4 says ~30x -- reconcile to one number.
- **source.epoch type.** Builder emits a float JD where v0.6 used a string --
  note in the parity claim or align.
- **Scheduled-task working dir.** `git add` / `--config` / `--output-dir` assume
  CWD = repo root; the Task Scheduler job MUST set the working directory (or the
  config load fails before anything else).
- **DST-safe run time.** Schedule the nightly at a non-transition local time
  (~4 AM, clear of 1-3 AM local): in spring 2-3 AM local does not exist (a task
  there may not fire), in fall 1-2 AM local repeats (a task there may fire twice).
  A double-fire is otherwise harmless (gap-aware catch-up over an already-current
  archive, atomic swap, N3 clean), but avoiding the window is the clean fix. Pairs
  with the N7 UTC-only date handling.

### Live-gate open dependencies (resolve at the first --dry-run; see TESTING_PROTOCOL.md)

- Does 2P/Encke's Horizons header carry `TP=` in the expected decimal form?
  (else the conic degrades to today-anchored -- now a VISIBLE `not_present`, N5.)
- Does Horizons clip or ERROR on a pre-SPK spacecraft start? (authoritative
  `config.start` assumes a curated valid date; the error text guides a fix.)
- id_type / center identity matrix for `@sun`, `@9`, `@599`, spacecraft `-31`,
  and small-body designations -- abort first-build on target/center mismatch.
- `elements()` column names / units / masks per object class; record the
  astroquery version.
- Windows: schedule the backup action clear of the swap window (a file lock on
  `raw/` during the rename can fail the swap).

---

BUILD handoff v0.1 written July 2026 with Anthropic's Claude Opus 4.8; built +
offline-verified this session. Companion: GALLERY_BUILDER_MANIFEST v2.
