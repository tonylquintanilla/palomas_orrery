# GALLERY DATA-SOURCE HANDOFF v0.2 -- fetch-fresh rebuild (converged)

Tony Quintanilla, PE | Claude | July 8, 2026

**Type:** DESIGN SESSION (zero code). v0.2 = v0.1 + Fable 5 broad-first review
integrated (Opus 4.6 designed, Fable 5 reviewed + verified against HEAD, Opus
convergence, Tony integrates). Converge, then manifest, then build.
**Base:** orrery HEAD `cde22c5` | gallery HEAD `4b086a6` (SHA round trip this
session; the v0.1 base `d4c37cf` was 13 commits behind -- the delta is the
committed Stage 2 record).
**Supersedes:** the "read the legacy orrery cache" INPUT model of Stage 2
(manifest v4 S2). Everything else in v4 carries forward (see "What carries").
**Ledger:** L-098.

================================================================
THE PIVOT
================================================================
Stop reading the legacy desktop cache to feed the gallery. Build a clean,
purpose-built gallery cache by fetching fresh from Horizons with the correct
center per object, stored in the GALLERY repo, refreshed by a nightly batch.
The legacy `orbit_paths.json` stays exactly as it is, for the desktop orrery.

Why (structural, not just the Charon bug): the desktop draws orbits from
osculating elements and fetches fresh points only for the current view, so
historical-trace corruption is invisible there. The gallery SERVES the raw
traces, so it is exposed to exactly the data the desktop is immune to. The
Charon/Pluto contamination (heliocentric points under a barycenter key, from a
fetch before the `@9` override) is one instance; `merge_orbit_data` merges by
date with no frame check, so the extent across 1501 accreted entries is
unknowable.

**Why rebuild rather than audit (the guarantee, stated correctly -- Fable):**
this is a cost asymmetry, not epistemic surrender. A magnitude audit can only
certify the magnitude-detectable contamination class; same-magnitude
wrong-center points (Pluto body vs barycenter differ by ~0.00013 AU) are
invisible to any magnitude check and could sit anywhere the blind merge
touched. Only PROVENANCE excludes them. A fresh fetch with an explicit center
per object buys the stronger guarantee for less work than the weaker audit --
and it removes a legacy-pair-to-gallery translation layer entirely.
**Honesty note:** "contamination can't enter by construction" is a property of
the EXPLICIT-CENTER FETCH. The `#F` magnitude guard is defense against gross
regressions only; it cannot catch the same-magnitude wrong-center class. Do not
credit the guard with the guarantee.

================================================================
DECIDED (Tony) + RATIFIED (Fable)
================================================================
- FETCH-FRESH, not validate-or-refetch. [ratified -- stronger guarantee, less
  work, removes a translation layer]
- NIGHTLY BATCH refresh. [ratified]
- Cache in the GALLERY repo (new file), NOT the orrery -- repos separate-clean.
  [ratified]
- Historical depth ~1 year to start. [ratified; window semantics amended below]
- Osculating fetched FRESH too (one provenance chain for the whole cache).
  [ratified -- cost trivial]

================================================================
ARCHITECTURE (converged)
================================================================
A standalone builder in the gallery repo (astroquery, no orrery import):

  reads the OBJECT-LIST CONFIG (the single authority; below)
   -> per object: fetch osculating elements + daily position vectors in the
      object's canonical center, with Guard v2 validation ON WRITE
   -> writes to a STAGING dir, runs the full validation suite there
   -> atomic swap -> clean RAW gallery cache (grows) + DERIVED served files
      (coverage_index.json + positions/*.json, v4 schema, window = derive param)
   -> single commit + push (none on failure)
  run nightly (scheduler detail: desktop now, Action later)

--- Choice 1: intermediate raw cache -- RATIFIED (a) ---
Builder writes a clean raw gallery cache (full-fidelity fetched vectors); a
derive step writes the served files from it. The raw archive is the
preservation asset. **This is also the mechanism that dissolves choice 3's
git-growth tension (Fable): archive depth is a property of the raw cache;
served depth is a DERIVE PARAMETER.** The raw archive can hold ten years while
the browser downloads two. Decide the split now.

--- Choice 2: desktop scheduler now, Action later -- RATIFIED (i) + 3 reqs ---
- **Idempotent, self-healing runs.** The window is computed from *today* at run
  time, so a missed night heals on the next run with no special-casing. State
  this as a design property.
- **Probe Actions early.** One manual workflow-dispatch Horizons fetch from a
  GitHub runner this month, to learn whether Horizons-from-CI is viable before
  the migration is needed (fact, not hope).
- **PAT hygiene.** The scheduled task needs push creds: a fine-grained PAT
  scoped to the gallery repo only, `contents:write`, in the Windows credential
  store, never in the script.

--- Choice 3: daily cadence -- RATIFIED; archive semantics AMENDED ---
- **Cadence:** daily, gallery-wide. Fast moons stay osculating-only; sub-daily
  is the deferred time-keyed follow-on. [ratified]
- **Leading edge is PROVISIONAL (Fable -- the biggest missing piece).** Points
  beyond today are PREDICTIONS; Horizons solutions update (materially for
  comets/NEOs). A strict never-overwrite archive would freeze stale predictions
  into the record. Rule: nightly RE-FETCH AND OVERWRITE `[today - 7d, today +
  horizon]`; only points older than 7 days are archival-frozen. Append-only for
  the deep past, refresh for the near-past+future.
- **Raw/served split** (choice 1): raw grows forever; served window is a derive
  parameter (start = full raw window; bound it when it matters).
- **Git growth: quantified -- fine, with a tripwire (Fable).** ~sub-KB packed
  delta per object-day; tens of MB/year even at 100 objects -- decades of
  headroom at tranche scale. The binding constraint is the gallery repo's
  existing 474 MB vs ~1 GB Pages guidance, NOT this pipeline. So: accept; add a
  repo-size check to the nightly run (alert ~800 MB); document the escape hatch
  (split to a data repo -- same-origin serving survives under the custom
  domain). Do NOT use LFS or history squashes now (complexity for a decade-away
  problem). Fixed commit message: `data: nightly YYYY-MM-DD` (greppable).

--- Choice 4: object-list config -- RATIFIED + PROMOTED ---
Make it the SINGLE AUTHORITY both the builder and the coverage index derive
from: `{slug, name, horizons_id, category, canonical center, features}` plus
per-object optional overrides (cadence, preset event windows), a
`schema_version`, and the attribution string. Start = the 9-object tranche
(promoted v4 TEST_OBJECTS), grow to a curated catalog.

================================================================
GUARD v2 -- per-object band (Fable; replaces the global 0.5 AU at scale)
================================================================
Fetched evidence: real bound moons cross 0.5 AU (Neso apoapsis 0.572 AU from
Neptune, July 2025; S/2021 N 1 ~0.50-0.51 AU). A global 0.5 AU threshold
FALSE-REJECTS real irregular moons at catalog scale while still passing
same-magnitude contamination. Fix uses what the v4 model already fetches
(osculating is PRIMARY, so the expected geometry is in hand):
  accept a relative-frame trace point iff  |r| <= k * a*(1+e)   (k ~ 1.5-2,
  perturbation slack), and flag any relative-frame trace whose magnitude
  approaches the parent's heliocentric distance.
For the 9-object tranche, `#F` at 0.5 AU is fine as-is. **Gate CATALOG GROWTH
on Guard v2**, and say so in the object-list config docs.

================================================================
NIGHTLY ATOMICITY (Fable -- the pattern the manifest must specify)
================================================================
1. Build everything to a STAGING directory.
2. Run the full validation suite there -- invariants + Guard v2 + the B3
   magnitude check that caught the original contamination -- EVERY NIGHT, not
   just at build time.
3. Atomic swap into place; SINGLE commit; NO commit on any failure.
4. Per-object failure isolation: one object erroring keeps its last-good data
   (its stale `retrieved` stamp makes that visible in the index); never aborts
   the batch.
5. Git itself is the rollback (previous nightly commit = backup). Import the
   desktop's >5%-shrink block as a pre-commit gate.
6. STALENESS VISIBLE WITHOUT ALERT INFRA: the exhibit already fetches
   `coverage_index.json` -- display "data as of <generated>". A dead nightly
   job then shows itself to every visitor (and to Tony). Cheapest monitoring
   that exists.

================================================================
STANDALONE BUILDER -- with copy discipline (Fable)
================================================================
Standalone is right (the desktop fetch path is entangled with the machinery
being escaped: tkinter callbacks, date-only keys, the blind merge). But the
hard-won specifics must be COPIED WITH PROVENANCE COMMENTS, not re-derived:
the `utc_to_tdb` TDB-boundary fix, `id_type` handling, the `@`-center override
syntax. Ledger the deliberate duplication ("two fetch paths exist by design;
sync-on-change") so the parallel-pipeline anti-pattern is a managed exception,
not an accident. Cross-repo import would couple deployment and break the
Actions future -- a documented copy is the honest form.

================================================================
ALSO FOLD IN (Fable, missing from v0.1)
================================================================
- **Mixed-version reads:** nightly updates + CDN caching can pair a fresh index
  with stale position files. Mitigation: exhibit appends `?v=<generated>` to
  position-file fetches and tolerates a missing file gracefully. (Pages CDN TTL
  is short -- verify before relying on it. Correctness nicety, not a crisis.)
- **Per-run build manifest:** commit a small record per run (run id, window,
  objects fetched, guard results, failures). The nightly log becomes the
  provenance trail; partial failures become visible in history.
- **Attribution field:** top-level `attribution: "Data: JPL/NASA Horizons"` in
  the coverage index (Horizons data is US-gov public domain -- courtesy/policy).
- **Builder testing:** `--dry-run` (fetch one object, validate, write nothing)
  as the descendant of Stage 2's `--preflight-only`; promote the B2/B3 protocol
  from build-time test to NIGHTLY GATE.

================================================================
FIRST BUILD STEP -- purge the committed contaminated ghosts (Fable, verified)
================================================================
Confirmed at orrery HEAD `cde22c5`: `data/solar-system/` AND `_export_out/` are
tracked, contain pre-guard `charon.json`/`pluto.json` with 35.70 AU points
declared `barycenter-relative`, and neither path is gitignored. This is the
protocol's stale-store failure class under the very path name the gallery will
use. BEFORE anything else: `git rm -r` both from the orrery repo and gitignore
the exporter output path. (Immediate; not deferred to the build session.)

================================================================
WHAT CARRIES FORWARD FROM STAGE 2 (only the SOURCE changes)
================================================================
- v4 osculating-primary model; coverage-index + position-file schema
  (v0.6-reconciled, field-verified); invariants #2/#3/#5/#6/#8/#C; center-slug
  map; epoch parser (HH:MM); JD convention; KM_PER_AU.
- `export_orbit_cache.py`'s derive/serve half is reused in the builder; its
  "read the legacy cache" input is retired.
- **Carry-forward TAGS (Fable -- so lessons don't float away):**
  - The `np.interp` containment/clamp hazard (retired invariant #4's lesson)
    RETURNS the day Phase 2 wide-view composition returns -- tag the deferral.
  - Stage 2's pre-flight discipline is CARRIED into the builder's `--dry-run`,
    not silently reinvented.

================================================================
RISKS (updated) -- ranked by cost to discover AFTER the build (Fable)
================================================================
1. Frozen stale predictions (no leading-edge refresh) -- FIXED by choice 3
   amendment above.
2. Silent nightly death -- FIXED by the "data as of" display.
3. Committed contaminated ghosts at orrery HEAD -- FIXED by the first build
   step (immediate).
4. `#F` false-rejects at catalog growth -- FIXED by Guard v2 gate.
5. Mixed-version CDN reads -- mitigated by `?v=<generated>`.
6. PAT scope/storage -- mitigated by PAT hygiene.

================================================================
NEXT
================================================================
1. Tony: purge the orrery-repo ghosts now (immediate action, above).
2. Manifest: the standalone builder (config-driven fetch + Guard v2-on-write +
   staging/validate/atomic-swap + derive served files + per-run manifest +
   nightly wiring), the object-list config schema, the refresh-window
   semantics.
3. Narrow Fable second round (offered): after this convergence, Fable re-checks
   ONLY the nightly-atomicity section and the refresh-window semantics -- where
   the remaining hidden failure modes live. Everything else converged this
   round.
4. Build (separate session): builder pre-tested; first full build over the
   window; Guard v2 verified; commit gallery cache + served files; schedule
   nightly.
5. The contamination question closes itself: the gallery never reads the legacy
   cache; every object comes out clean by construction (explicit-center fetch).

Ledger L-098 delta: SHA cde22c5; ghost cleanup (first build step); Fable review
integrated (raw/served split, provisional leading edge, Guard v2 gate,
atomicity pattern, standalone copy discipline, missing-considerations,
carry-forward tags). Sibling candidate: `merge_orbit_data` source-side frame
guard for the DESKTOP cache (would have prevented the original contamination;
low priority). Sibling candidate: the standalone/desktop fetch duplication as a
managed sync-on-change exception.

---

v0.1 written July 2026 with Anthropic's Claude Opus 4.8.
v0.2 convergence (Fable 5 review integrated) July 2026 with Anthropic's Claude
Opus 4.8. Review: FABLE5_REVIEW_gallery_data_source_pivot.md.
