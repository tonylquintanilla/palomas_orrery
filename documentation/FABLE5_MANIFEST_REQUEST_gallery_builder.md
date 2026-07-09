# MANIFEST REQUEST -- Gallery Builder (for Claude Fable 5)

**From:** Tony (carrying the converged design from Opus 4.8)
**Attached:** GALLERY_DATA_SOURCE_HANDOFF.md v0.3 (the converged design -- the
source of truth for this manifest).
**Mode:** Collegial Mode 7 -- you author the build manifest; Opus convergence-
reviews it, Tony builds from it. This is a SPEC, not implementation: describe
steps, schemas, gates, and invariants precisely enough to build against -- do
NOT write the builder's code.

--------------------------------------------------------------------
GROUND RULES
--------------------------------------------------------------------
- FETCHED-NOT-RECALLED. The handoff's code claims are Opus-verified at orrery
  HEAD `cde22c5` / gallery HEAD `4b086a6`. Re-check HEAD first (`git ls-remote`)
  -- the ghost-purge commit may have moved orrery HEAD past `cde22c5`; use the
  live SHA. Confirm anything load-bearing you build on; if a claim can't be
  sourced, say "unsourced" rather than filling from memory.
- STAY IN FIRST-BUILD SCOPE (below). The net-new tracks (L-101..L-105) are
  DEFERRED -- the manifest names them as out-of-scope, does not spec them.
- Follow the house manifest format: see PHASE1B_BUILD_MANIFEST_v4.md as the
  format precedent (Type, Base, Pre-build gates, Steps, Invariants, Interface,
  Post-build gate, What-to-verify, Lineage, credit line).
- This builder is STANDALONE in the GALLERY repo (astroquery, no orrery import).
  The derive/serve half is COPIED WITH PROVENANCE COMMENTS from
  export_orbit_cache.py (the v4 schema, epoch parser, JD, center-slug map,
  invariants) -- reused, not re-derived; ledger the deliberate duplication.

--------------------------------------------------------------------
WHAT THE MANIFEST MUST SPECIFY (first build)
--------------------------------------------------------------------
Target: a nightly, standalone gallery-cache builder in the gallery repo that
fetches fresh from Horizons with the correct center per object, validates on
write, and derives the served files. Sections the manifest needs:

1. **Object-list config** (new gallery-repo data file, the single authority the
   builder AND the coverage index derive from). Specify the schema:
   `{slug, name, horizons_id, category, canonical_center, orbit_type,
   trace_policy, features[]}` + per-object optional overrides (Tp for comets,
   max_distance for hyperbolics, spacecraft `{start,end}`, event windows) +
   `schema_version` + attribution string. Seed = the 9-object tranche.

2. **Fetch, per object** (astroquery jplhorizons):
   - osculating elements in the canonical center (at TODAY for most; at **Tp**
     for comets, matching `_add_perihelion_osculating_orbit`);
   - the **as-of-today** position vector (one `{t,x,y,z}`);
   - **spacecraft only:** the full-arc daily position trace, span = launch+1d ->
     min(mission end, Horizons horizon 2029-12-12), fetched in CHUNKS (~75
     epochs/query -- Horizons rejects near ~100) and stitched.
   - Cadence daily. NO general position trace for non-spacecraft (conic + today-
     point). NO preset fetching (preset slot exists, unpopulated; Apophis null).

3. **Guard v2 on write** (per-object band): accept a relative-frame point iff
   `|r| <= k * a*(1+e)` (k ~ 1.5-2); flag/reject heliocentric-scale points in a
   relative frame. Specify k, and that it replaces the global 0.5 AU `#F`.

4. **Nightly atomicity** (spec the exact sequence): build to STAGING -> run the
   full validation suite there (invariants + Guard v2 + the B3 magnitude check)
   EVERY night -> atomic swap -> SINGLE commit (none on failure) -> per-object
   failure isolation (keep last-good, stale `retrieved` stamp) -> git as
   rollback -> >5%-shrink pre-commit block -> repo size tripwire (~800 MB).

5. **Refresh-window semantics** (provisional leading edge): nightly overwrite
   `[today-7d, today+horizon]`; freeze points older than 7 days. Raw archive
   grows (append the frozen past); served window is a DERIVE parameter. Spell
   out how a re-fetch reconciles with already-stored dates (overwrite by date).

6. **Served outputs** (v4 schema, carried): `coverage_index.json` (per object:
   osculating elements + `orbit_type` + `center` + `as_of_today` point +
   `positions` ref for spacecraft + null `event_link` slot + null `presets`
   slot) + `positions/<slug>.json` (spacecraft arcs, km/JD) + `feature_configs.
   json` (best-effort, Phase 2 prep) + a per-run BUILD MANIFEST record
   (run id, window, objects, guard results, failures). Top-level `attribution`,
   `generated`, `schema_version`.

7. **Deployment**: desktop Task Scheduler now (Action later); PAT hygiene (fine-
   grained, gallery-repo only, `contents:write`, credential store); idempotent
   self-healing runs (window computed from today).

8. **First build STEP 0**: confirm the contaminated ghosts are purged from the
   orrery repo (data/solar-system/, _export_out/) and gitignored -- verify at
   live HEAD before the first gallery build.

--------------------------------------------------------------------
EXPLICITLY OUT OF SCOPE (name as deferred, do NOT spec)
--------------------------------------------------------------------
L-101 osculating-history fan; L-102 spacecraft thinning; L-103 hyperbolic
browser branch; L-104 preset generator; L-105 merge_orbit_data desktop guard;
L-100 shells interactive-vs-gallery split. The manifest leaves clean interfaces
(the null event_link/preset slots, the config's override fields) so these plug
in later without rework -- but specs none of them.

--------------------------------------------------------------------
DECISIONS TO NAIL (don't leave vague)
--------------------------------------------------------------------
- Object-list config exact field set + one worked example row (a spacecraft and
  a comet, since they carry the override fields).
- Chunk size constant (~75) and the stitch/dedup rule.
- Guard v2 k value and the reject-vs-flag behavior.
- The atomicity sequence as an ordered, testable checklist.
- `--dry-run` (fetch one object, validate, write nothing) as the builder's
  descendant of Stage 2's `--preflight-only`, and the nightly validation gate.

--------------------------------------------------------------------
DELIVERABLE
--------------------------------------------------------------------
The build manifest as a carried document (house format), scoped to the first
build, with the deferred tracks named. Flag any decision you had to make that
the handoff left open, and any spot where the handoff and the live code
disagree. Opus will convergence-review before Tony builds; if you hit a genuine
fork, present it rather than guessing.
