# GALLERY BUILDER BUILD MANIFEST v2 -- gallery_cache_builder.py

**Type:** BUILD MANIFEST (Mode 2 -- agentic, new standalone module, GALLERY repo)
**Author:** Claude Fable 5 (v1, per FABLE5_MANIFEST_REQUEST_gallery_builder.md);
Opus 4.8 convergence review + Tony ratification (v2).
**Design source:** GALLERY_DATA_SOURCE_HANDOFF v0.4 (the converged design as
amended this session; carries v0.3 by reference). Where this manifest and the
handoff disagree, the disagreement is FLAGGED in S0 -- nothing silently resolved.
**As-built:** the builder was built + offline-verified July 9 (see
GALLERY_BUILD_HANDOFF v0.1). Two spec deltas surfaced at build time and are
recorded there in full: the served schema is the FULL v0.6 shape, not S6's
shorthand (schema parity to export_orbit_cache.py's actual output); and S2's
`trace_policy` is MODEL-derived (none for every non-spacecraft, full-arc only
for spacecraft), NOT carried from TEST_OBJECTS's retired serve/none field.
**Base:** orrery HEAD `4e2629c` | gallery HEAD `4b086a6` -- both confirmed live
via `git ls-remote` (July 9, 2026). NOTE: v1 was authored on orrery `081ee18`;
the only commit between `081ee18` and `4e2629c` adds the manifest file itself
(`documentation/GALLERY_BUILDER_MANIFEST_v1.md`) -- ZERO source changed, so every
v1 code citation remains byte-valid. Re-resolve live HEADs at build session start;
do not hardcode.
**Pre-build gates:**
(1) GHOST PURGE -- **VERIFIED SATISFIED** (commit `9febac5` "remove obsolete
    cache", ancestor of HEAD): `git ls-tree -r HEAD` shows `data/solar-system/`
    and `_export_out/` absent from the orrery tree; `.gitignore` at HEAD covers
    both (lines 24-25). Request S8 closed; one-line re-confirm only if orrery
    HEAD has moved.
(2) Copy-source availability at orrery HEAD -- verified this session:
    `export_orbit_cache.py`, `orbit_data_manager.py` (utc_to_tdb,
    range-query pattern, shrink guard), `idealized_orbits.py`
    (plot_perihelion_osculating_orbit), and -- NEW in v2 --
    `osculating_cache_manager.py` (`fetch_solution_tp`:459, `resolve_tp`,
    `cache_solution_tp`) for the comet solution-Tp path (S3a, F4).
(3) BACKUP PRECONDITION (NEW, F9): the gallery-cache backup action and the
    `.gitignore` entry for the local backup path must both EXIST before the
    first build runs -- so the irreplaceable raw archive is never held
    un-backed-up, even for one night. Tracked as ledger L-106.
**Post-build gates:** provenance scan Tier-1 = 0 on the new module before push;
`--dry-run` clean on one object; first full build passes the STRUCTURAL
validation suite (schema/file/center invariants + shrink gate) before its commit.
Guard v2 and the B3 magnitude check are MONITORS (warn, not abort) per F8.

---

## S0. Flags -- forks, decisions, and corrections (review these first)

Each flag carries a STATUS: CORRECTED (factual fix to v1), RATIFIED (Tony
confirmed as drafted), RESOLVED (open fork now decided), CHANGED (design
altered from v1/v0.3), or NEW.

**F1 -- Chunking vs range query. [RATIFIED]** The *request*
(FABLE5_MANIFEST_REQUEST_gallery_builder.md, not v0.3) specifies spacecraft arcs
"fetched in CHUNKS (~75 epochs/query)." That limit is real but applies only to
**discrete epoch lists**; the house pattern is a Horizons **range query**
(`epochs={'start','stop','step'}`) -- `spacecraft_encounters.py` fetches an
entire mission window at 1h step in ONE call (the `Horizons(...)` call ~621,
`.vectors()` ~632), and `orbit_data_manager.py:680` confirms the range pattern.
This manifest specs range-query primary. SUPERSEDED by the L-109 spacecraft
redesign: the flown arc is a COARSE glide backbone (fetch_step, e.g. 7d) + daily
densification inside known flyby windows + Douglas-Peucker thin -- a coarse range
is ~2,600 points for Voyager, not ~17,900, so there is no giant single-range
query and no range-HALVING fallback is needed (A-6 dissolved). Authoritative
config.start replaces the Horizons start-probe. Densify KNOWN event windows
BEFORE thinning -- you cannot thin toward an epoch you never sampled. Also
landed with L-109: #T freshness invariant implemented; B-3 parity fields
(serving_base / scene_features / step_hours); A-3 failed-fetch serves last-good
conic with as_of_today nulled.

**F2 -- Perihelion function name. [CORRECTED]** v1 said
`_add_perihelion_osculating_orbit` is "No such symbol at HEAD." That is FALSE.
BOTH symbols exist: `_add_perihelion_osculating_orbit` (`palomas_orrery.py:1533`)
is the live DISPATCHER that v0.3 correctly named -- it loops selected objects and
imports+calls the leaf; `plot_perihelion_osculating_orbit`
(`idealized_orbits.py:7089`) is the LEAF that builds the conic. Copy the LEAF for
provenance; the dispatcher is its live caller (map the dispatch, don't just copy
the leaf blind). All comet-conic provenance comments cite the leaf.

**F3 -- Refresh-window semantics under the conic model. [RATIFIED]** Non-
spacecraft fetch NO future points -- the conic covers the future visually and the
as-of-today point is "you are here." `horizon = 0` for non-spacecraft: the nightly
vectors window is `[today-7d, today]` (8 daily points in one range query,
overwrite-by-date; dates older than `freeze_after_days` are frozen). The raw
archive still grows one frozen point per object per night -- the preservation
asset accreting. With F5's spacecraft change, NO object fetches a future point
anywhere in the nightly; the whole nightly is a small backward accretion plus a
frozen past.

**F4 -- Comet in the seed + comet Tp path. [RESOLVED + CORRECTED]** Encke JOINS
the seed (11 rows). The comet path is corrected to match the desktop's actual
two-role Tp resolution (v1's "elements at today -> read TP -> refetch" was a
single un-iterated step from far out and does NOT converge). See S3a. The Encke
dry-run is LOAD-BEARING: it is the only place the Tp path, the `2P`-apparition
disambiguation, and the presence of the header solution-TP are exercised -- and
it must be checked against the desktop `resolve_tp` result (Mode 5), because the
builder's own two-step produces a valid-looking conic even when the epoch is
wrong.

**F5 -- Spacecraft model: fetch-flown-once + append-today-nightly. [CHANGED --
Tony's design; supersedes v0.3]** v0.3 specced pre-fetching the FULL arc
(past + predicted future out to the ~2029 SPK horizon), write-once, with a manual
`--refresh-spacecraft`. REPLACED: at `--first-build`, fetch only the FLOWN arc
(ephemeris-start -> today) ONCE; thereafter the nightly appends today's single
point via 3b, exactly like every other object. Spacecraft stop being a nightly
special case. Rationale: (a) uniform nightly -- every object accretes one real
point/night; (b) no predictions served as fact; (c) a live daily endpoint, which
DISSOLVES the active-maneuver problem (a maneuvering craft's predicted future
would drift; a nightly-fetched endpoint never does) rather than deferring it;
(d) if the "where is it heading" projection is ever wanted, the browser
extrapolates the coast -- it is not stored. The served arc is slightly smaller
(no future block) and grows one point/day.

**F6 -- Osculating elements history retained in raw. [RATIFIED]** Elements are
fetched nightly (cheap). The raw cache appends each night's element set to a
per-object JSONL history (~100 bytes/object/night), making the deferred L-101
osculating-history fan buildable FROM THE ARCHIVE with zero refetching. Served
index carries the latest set only.

**F7 -- SPK-horizon date. [RESOLVED BY REMOVAL]** v1's unsourced "2029-12-12"
existed only to bound the pre-fetched FUTURE arc. F5 removes future fetching, so
there is no future end to source and the date is GONE from the config. The ONLY
ephemeris bound that still exists is the START, which is discovered from Horizons
(F5 / S3c), not from a constant. (Note for the record: 2029-12-12 did appear in
v0.3 point 4 and in the request, as an unsourced value -- v1's "not found in
v0.3" was imprecise; moot now.)

**F8 -- Guard v2 becomes a MONITOR, not a gate. [CHANGED -- supersedes both v0.3
and v1]** v0.3 hard-rejected the outer bound and flagged the reverse class; v1
promoted BOTH bounds to hard reject. v2 makes BOTH bounds WARN. Guard v2 is
explicitly defense-in-depth, NOT the primary guarantee -- provenance-by-
construction (explicit-center fetch) is (v0.3 honesty note). A backstop should
not veto a build and DISCARD data over what is most likely a transient Horizons
error; discarding also destroys the evidence needed to diagnose why the fetch
went wrong. Band `q/k <= |r| <= k*Q`, k = 2.0, still sets the WARNING threshold.
The requirement that makes warn safe rather than silent-accept: the warning must
be LOUD and DIAGNOSTIC and reach a channel Tony actually monitors (S4, S8) --
warn degrades to accept the instant the warning goes unread. Optional two-tier
severity: inner-bound trip = "review" (can be a real perturbation snapshot swing);
outer-bound trip at ~30x expected distance = "likely contamination" (the Charon
class), so a real signal does not flatten into noise. If a legitimate object ever
warns at catalog growth, the fix is to raise k with a documented reason, not to
silence it.

**F9 -- Gallery-cache backup + gitignore discipline. [NEW]** The gallery raw
archive is now an irreplaceable asset (fetched-once past). Backup is a SEPARATE
scheduled action (mirroring Tony's existing "backup on every cache update"),
targeting `data/solar-system/raw/` (served files are derived/regenerable and do
not need independent backup); the local backup path is GITIGNORED so backup
copies never enter the repo that serves to the web under the Pages budget; Tony's
Google Cloud auto-backup carries the off-site copy from there. Decoupled from the
builder -- a backup failure never blocks a good commit and vice versa. First
build is gated on this existing (pre-build gate 3). Tracked as L-106.

**Also ratified as drafted (not F-flagged):** the SHRINK GATE re-expressed as
point-count >= 95% per-object AND aggregate (v0.3 said "import the desktop's >5%
byte-shrink block"; point-count is the truer data-loss signal for date-keyed
dicts -- a conscious adaptation, S7 step 5).

---

## S1. What We're Building

One standalone Python script, `tools/gallery_cache_builder.py`, living in the
GALLERY repo (`tonyquintanilla.github.io`). Nightly it: reads the object-list
config -> fetches fresh from Horizons per object with the explicit canonical
center -> validates on write (structural gates abort; Guard v2 monitors/warns) ->
builds raw cache + derived served files in STAGING -> runs the validation suite ->
atomic swap -> single commit + push. No orrery imports; hard-won fetch specifics
are COPIED WITH PROVENANCE COMMENTS (S3). The deliberate duplication is ledgered
("two fetch paths exist by design; sync-on-change").

Directory layout (gallery repo):
```
tools/gallery_cache_builder.py
data/solar-system/
  objects_config.json          # S2 -- the single authority
  coverage_index.json          # served
  positions/<slug>.json        # served (spacecraft arcs only)
  feature_configs.json         # served (best-effort, Phase 2 prep)
  raw/
    vectors/<slug>.json      # raw archive (grows; AU/JD as fetched)
    elements/<slug>.jsonl    # elements history (F6)
    runs/<run_id>.json       # per-run build manifests
  .staging/                    # gitignored; build workspace
.gitignore                     # MUST also ignore the local backup path (F9)
```
The backup copy of `raw/` lives OUTSIDE the committed tree (F9) -- a gitignored
local path, mirrored off-site by Google Cloud; it is NOT a builder output.

---

## S2. Object-List Config (`objects_config.json`) -- the single authority

Both the builder and the coverage index derive from this file. Nothing about an
object lives anywhere else.

```json
{
  "schema_version": "1.0",
  "attribution": "Data: JPL/NASA Horizons",
  "defaults": { "cadence_hours": 24, "guard_k": 2.0,
                "freeze_after_days": 7, "backfill_days": 365 },
  "objects": [ ... ]
}
```

Per-object fields (required unless marked opt):
- `slug` -- index key, lowercase.
- `name` -- display name.
- `horizons_id` -- string ("399", "901", "-31", "2P").
- `id_type` -- "majorbody" | "smallbody" | "id" (house pattern: smallbody for
  comets/asteroids per `celestial_objects.py`; "id" for spacecraft per
  `spacecraft_encounters.py:630`).
- `category` -- planet | moon | dwarf_planet | asteroid | comet | spacecraft.
- `canonical_center` -- Horizons location string ("@sun", "@9", "@599").
- `center_slug` -- served slug; must resolve via the carried CENTER_SLUG_MAP.
- `trace_policy` -- "none" | "full-arc" ("osculating-history" reserved, L-101).
- `features` -- [] (flows to feature_configs; comet structure lives HERE,
  deferred -- never in orbit data).
- `overrides` (opt):
  - comet: `{"anchor": "Tp", "max_distance_au": 100}`
  - spacecraft: `{"start": "YYYY-MM-DD"}` -- a HINT (launch date, human context);
    the REAL arc start is discovered from Horizons at first build (F5/S3c). No
    `end` field (F7: no future is fetched).
  - `event_windows`: [] (reserved, L-104)
- `notes` (opt) -- human context.

**Seed = the tranche** (11 rows): earth, jupiter, saturn, moon, io, titan, pluto,
charon, apophis, voyager_1, **encke** -- slugs/ids/centers for the first ten
carried verbatim from v4 TEST_OBJECTS (`export_orbit_cache.py`), including `pluto`
at `@9` (barycenter trajectory) and `charon` at `@9`; encke added per F4.

**Worked row -- spacecraft (F5 model):**
```json
{ "slug": "voyager_1", "name": "Voyager 1", "horizons_id": "-31",
  "id_type": "id", "category": "spacecraft", "canonical_center": "@sun",
  "center_slug": "sun", "trace_policy": "full-arc", "features": [],
  "overrides": { "spacecraft": { "start": "1977-09-05" } },
  "notes": "start is a HINT (launch date); real arc start probed from Horizons
            at first build. No future fetched; nightly appends today's point." }
```

**Worked row -- comet (Encke; in the seed per F4):**
```json
{ "slug": "encke", "name": "2P/Encke", "horizons_id": "2P",
  "id_type": "smallbody", "category": "comet", "canonical_center": "@sun",
  "center_slug": "sun", "trace_policy": "none", "features": [],
  "overrides": { "comet": { "anchor": "Tp", "max_distance_au": 100 } },
  "notes": "Tp-anchored conic via solution-Tp resolution (S3a); exact Horizons
            record verified at dry-run (multiple apparitions resolve under
            '2P' -- pick current)" }
```

Config docs must state: **catalog growth beyond the tranche is gated on Guard v2**
(now a monitor -- the gate is the WARNING surfacing, not a reject).

---

## S3. Fetch, per object (astroquery jplhorizons)

Copy-with-provenance sources (cite file:line and "Copied from ... orrery HEAD
<SHA>; sync-on-change" in comments):
- `utc_to_tdb` -- `orbit_data_manager.py:41` (the TDB boundary fix).
- Range-query pattern + '@'-prefix center normalization + id_type passthrough --
  `orbit_data_manager.py:~670-690`.
- `refplane='ecliptic'` on `.vectors()` -- `spacecraft_encounters.py:~632`.
- Epoch parser (HH:MM), `_dt_to_jd`, `parse_osc_epoch_to_jd`,
  `_true_to_mean_anomaly_deg` (the MA-None fallback), CENTER_SLUG_MAP +
  `resolve_center_slug`, KM_PER_AU usage -- `export_orbit_cache.py:198-300`.
- **NEW (F4): solution-Tp resolution** -- `resolve_tp`, `fetch_solution_tp`
  (`osculating_cache_manager.py:459`), `cache_solution_tp`
  (`osculating_cache_manager.py:~555-620`). These read the solution-level TP from
  the Horizons raw response HEADER (comets/asteroids only) and cache it.

**3a. Osculating elements -- every non-spacecraft, nightly.**
`Horizons(id, id_type, location=canonical_center, epochs=epoch_jd).elements()`
(pattern: `osculating_cache_manager.py:496`).
- Default: epoch = today.
- **Comet override (`anchor: "Tp"`) -- corrected two-role Tp resolution (F4),
  matching `plot_perihelion_osculating_orbit` (`idealized_orbits.py:7089`):**
  1. `resolve_tp()` -> the SOLUTION TP from the Horizons header (Path 1 cached,
     Path 2 live `fetch_solution_tp()` then cache). This LOCATES the perihelion
     epoch in one shot; it is not the served anchor.
  2. Fetch osculating elements AT that epoch (bypass any cache for this
     epoch-specific fetch).
  3. SERVE that element set anchored on ITS OWN osculating TP
     (`osc_tp_at_perihelion = elements.get('TP')`) as `Tp_jd`, plus
     `max_distance_au`. This is the "converged" Tp -- osculating TP read AT
     perihelion has collapsed onto the true passage and is consistent with the
     served set. (v1's "elements at today -> read TP -> refetch once" is WRONG:
     a single step from far out does not converge; the solution TP gets there in
     one query.)
  - OPTIONAL (nice-to-have, not build-blocking): also serve `solution_Tp_jd`.
    The residual `solution_Tp_jd - Tp_jd` at perihelion is the integrated
    non-gravitational (outgassing) shift -- the desktop already renders it; if
    both numbers are served the browser gets it for free.
- `orbit_type` is DERIVED from fetched e (e < 1 elliptical, e >= 1 hyperbolic),
  not declared; a config `expected` mismatch warns.
- Append the fetched set to `raw/elements/<slug>.jsonl` (F6):
  `{run_id, epoch_jd, a, e, i, omega, Omega, MA, TP, retrieved}`.

**3b. Actual-motion accretion -- every non-spacecraft AND (nightly) every
spacecraft.** ONE range query: `epochs={'start': utc_to_tdb(today-7d), 'stop':
utc_to_tdb(today), 'step': '1d'}`, `location=canonical_center`,
`.vectors(refplane='ecliptic')` -- 8 points. Guard v2 (S4) monitors the batch.
Overwrite-by-date into `raw/vectors/<slug>.json`; dates older than
`freeze_after_days` are never re-fetched (frozen past). The **as-of-today point**
served in the index = the last point of this batch. Units: raw stores AU + JD
exactly as fetched; the derive step converts to km (KM_PER_AU, carried). Under
F5, spacecraft use this same nightly accretion for their live endpoint -- the
only spacecraft-specific step is the one-time first-build backfill (3c).

**3c. Spacecraft flown-arc backfill -- `--first-build` (and the optional
`--refresh-spacecraft`) only (F5).** ONE range query: start = discovered
ephemeris start, stop = today, step '1d'. Discovering the start: attempt from the
config `start` hint (or launch); if Horizons returns empty or clips the leading
edge, read the ACTUAL first available epoch from the response and begin there
(the same "let the API declare the bound" discipline F7 applies at the other end
-- symmetric: the config supplies HINTS, Horizons supplies VALUES). That
discovered start becomes the earliest frozen point in the archive forever, so it
is fact-derived, not launch+1. Guard: spacecraft sanity only (S4). Written to raw
once; served `positions/<slug>.json` in km/JD (v4 position-file format, carried).
Fallback if the range is rejected: split the span in half recursively (NOT fixed
75-epoch chunks; range-halving keeps the query count logarithmic), stitch by
date, assert no duplicate/missing dates at the seams. Thereafter the nightly (3b)
maintains the live endpoint; no future is ever fetched.

**3d. First build backfill (non-spacecraft).** `--first-build` runs 3b with
`start = today - backfill_days` (365): one ~366-point range query per object, then
the nightly takes over. Idempotent: re-running overwrites the same dates with the
same data.

No general position traces for non-spacecraft. No preset fetching (`presets` slot
exists, null; Apophis 2029 is L-104's business).

---

## S4. Guard v2 -- on write, as a MONITOR (F8; replaces the global 0.5 AU `#F`)

Applies to every fetched vector point of every object WITH osculating elements, in
whatever frame the canonical center defines. Let q = a(1-e), Q = a(1+e) from the
object's own current osculating set, k = 2.0:

- **Band (warning threshold), elliptical (e < 1):** `q/k <= |r| <= k*Q`. The
  upper bound flags heliocentric-scale points under a relative frame (the Charon
  35.7 AU class, ~10^5 x over); the lower bound flags relative-scale points under
  a heliocentric frame AND cross-body mixups (a point below q/2 cannot belong to
  the object's own orbit).
- **Hyperbolic (e >= 1):** `q/k <= |r| <= 1.1 * max_distance_au`.
- **Spacecraft (no elements): exempt from the band.** Sanity instead:
  0 < |r| < 200 AU, timestamps strictly increasing, no NaN/null coordinates.
  (Spacecraft sanity failures are a data-integrity problem, not a contamination
  monitor -- they may still WARN loudly, but a NaN/negative-r spacecraft point is
  a fetch error worth surfacing prominently.)
- **Violation behavior: WARN, do NOT reject or discard.** The fetched data is
  KEPT (the raw archive holds every point regardless) and served; a LOUD,
  DIAGNOSTIC warning is recorded in the run manifest and surfaced to a channel
  Tony monitors (S8). The warning MUST carry: object slug, offending `|r|`, the
  expected band `[q/k, k*Q]`, the `center` used, and the fetch params (epoch
  window, id_type). Optional severity: inner-bound = "review"; outer-bound (~>=10x
  the band) = "likely contamination". Rationale (F8): Guard is defense-in-depth,
  not the guarantee; a transient Horizons error should not veto a build or destroy
  the evidence. The genuine-contamination residual risk (a real bad point reaches
  served until Tony acts on the warning) is accepted CONSCIOUSLY, backed by
  provenance-by-construction upstream and the shrink gate + git + off-repo backup
  downstream.
- The carried **B3 magnitude re-check** (copied from `export_orbit_cache.py:
  ~494-510` with provenance comment) runs on the SERVED files in the nightly
  suite, ALSO as a MONITOR (warn) -- the continuity of the exact check that caught
  the original contamination, now reporting rather than blocking.

---

## S5. Raw cache formats

`raw/vectors/<slug>.json`:
```json
{ "object": "io", "center": "@599", "center_slug": "jupiter",
  "unit": "au", "epoch_type": "JD",
  "points": { "2026-07-01": { "jd": 2461222.5, "x": ..., "y": ..., "z": ... },
              "...": {} } }
```
Date-keyed (daily cadence by design). Overwrite-by-date = dict update on the
refresh window. Append-only outside it.

`raw/elements/<slug>.jsonl`: one JSON line per run (S3a).
`raw/runs/<run_id>.json`: the per-run build manifest --
`{run_id, started, finished, window, objects: {slug: fetched|backfilled|
failed:<reason>}, guard_warnings: [ {slug, |r|, band, center, params, severity} ],
structural_validation: pass|fail, committed: bool, repo_size_mb}`.
(Note: no `rejected` state for guard -- Guard is a monitor now; guard trips are
`guard_warnings`, not fetch outcomes.)

---

## S6. Derive step -> served outputs (v4 schema, carried)

From staged raw, per object: latest elements + `orbit_type` + anchor fields
(+ `Tp_jd` [converged], optional `solution_Tp_jd`, `max_distance_au` for comets)
+ `as_of_today` `{t, x, y, z}` in **km/JD** + `positions` ref (spacecraft only)
+ `event_link: null` + `presets: null` + `retrieved`.

Index top level: `schema_version`, `generated` (UTC ISO), `generator`
(name+version), `attribution` ("Data: JPL/NASA Horizons"), `served_window`
(a DERIVE PARAMETER -- starts as the full raw window; bounding it later is a
one-line change), `objects{}`.

**Validation split (F8):** STRUCTURAL invariants ABORT the run (they catch builder
bugs); MAGNITUDE/contamination checks WARN (they monitor provenance, now
guaranteed upstream).

STRUCTURAL (abort on failure):
- **#2** spacecraft -> no osculating AND positions present.
- **#3** every non-spacecraft -> osculating present.
- **#5** every `center` resolves to a valid slug.
- **#6** every non-null preset file exists on disk (vacuously true; slot null).
- **#8** every `positions.file` referenced exists on disk.
- **#C** osculating.center == config `center_slug` (center-match, carried).
- **#T** `as_of_today.t` within 48h of `generated` for every fetched
  (non-stale) object.
- **#W** served_window is contained in the raw window.
- **#U (unit sanity, was part of #V):** served km magnitudes ~= KM_PER_AU x raw
  AU magnitudes within a coarse factor (catches a KM_PER_AU/derive-conversion bug
  -- a builder correctness gate, distinct from the Guard band). ABORT on gross
  mismatch.

MONITOR (warn, never abort):
- **Guard v2 on served numbers** (the narrow per-object band re-applied post-km):
  reports contamination that survived to served. Warn.
- **B3 magnitude re-check** on served files. Warn.

`feature_configs.json`: best-effort from config `features` lists; renderers are
Phase 2; comet structure explicitly deferred (two-surface principle).

**Mixed-version reads (carried mitigation):** the index's `generated` value
doubles as the cache-buster -- exhibits append `?v=<generated>` to position-file
fetches and tolerate a missing file gracefully. The exhibit displays
"data as of <generated>" -- the staleness monitor that costs nothing.

---

## S7. Nightly atomicity -- the ordered, testable checklist

1. `run_id` = UTC timestamp. Window computed FROM TODAY at run time (idempotent,
   self-healing -- a missed night heals tomorrow).
2. Build entirely under `.staging/<run_id>/` (raw copy-forward + new fetches +
   derived served tree). The live tree is never touched.
3. Per-object isolation: each object's fetch in its own try/except; a FETCH
   FAILURE -> carry forward last-good raw for that object, mark it in the run
   manifest, CONTINUE the batch. (A Guard v2 trip is NOT a failure now -- it is a
   recorded warning; the data is kept. F8.)
4. Validation suite ON STAGING, every night: STRUCTURAL invariants (#2-#W, #U) +
   the shrink gate = ABORT on failure (no swap, no commit, `.staging/<run_id>/`
   retained for autopsy, run manifest `structural_validation: fail`). Guard v2 +
   B3 = MONITOR: record `guard_warnings`, do NOT abort.
5. Shrink gate (pattern: `orbit_data_manager.py:418-450`, provenance comment;
   re-expressed as POINT-COUNT): staged raw point-count >= 95% of live, per object
   AND in aggregate. Fail -> ABORT as step 4. (This is a data-LOSS gate and stays
   hard -- it is not the contamination monitor.)
6. Atomic swap: rename live -> `.prev`, staging served+raw -> live (`os.replace`,
   same filesystem); `.prev` deleted only after step 8 succeeds (within-run
   rollback; git is the rollback across runs).
7. Repo size tripwire: measure; > 800 MB -> WARN loudly (console + run manifest)
   but do not block. Escape hatch (split to a data repo; same-origin serving
   survives under the custom domain) documented in the config notes.
8. Single commit of the data paths, message `data: nightly YYYY-MM-DD`; push.
   Push failure (network): leave the commit local; tomorrow's push carries both.
9. The run manifest is written into `raw/runs/` BEFORE the commit, so every commit
   carries its own provenance record -- including any `guard_warnings`.
10. BACKUP (F9) is a SEPARATE scheduled action, not a builder step: it OBSERVES a
    successful commit and mirrors `raw/` to the gitignored local backup path (then
    Google Cloud carries it off-site). Decoupled -- a backup failure never blocks
    a commit, and the builder never waits on backup.

---

## S8. Deployment

- Desktop Task Scheduler now; the builder is standalone so migrating to a GitHub
  Action later is a scheduler detail. **Probe Actions this month** (one manual
  workflow-dispatch Horizons fetch) so the migration path is fact before needed.
- PAT: fine-grained, gallery repo only, `contents: write`, stored in the Windows
  credential store -- never in the script, never in the repo.
- The scheduled task runs `--nightly`; a failed exit code surfaces in Task
  Scheduler history, and the "data as of" display is the user-visible monitor.
- **Guard-warning surfacing (F8 requirement):** `guard_warnings` in the run
  manifest is not enough on its own -- if any guard warning fires, the run must
  surface it on a channel Tony actually reviews (a prominent console banner in the
  nightly summary at minimum; Tony's call on whether to add a stronger channel).
  A warning that is only written to a file nobody opens degrades the monitor to
  silent-accept.
- **Backup (F9):** a separate scheduled action mirrors `data/solar-system/raw/`
  to a gitignored local path on each successful cache update (same cadence as
  Tony's existing backup discipline); Google Cloud auto-backup provides the
  off-site copy. The local backup path is in `.gitignore`. The three integrity
  layers, distinct failure modes: shrink gate (bad write, prevented) / git revert
  (bad build that committed, rolled back) / off-repo backup (bad repo, survived).
  FIRST BUILD IS GATED on the backup action + gitignore entry existing (pre-build
  gate 3).

## S9. Interface

```
python tools/gallery_cache_builder.py --nightly            # default nightly run
                                      --first-build        # non-spacecraft 365d
                                                           #  backfill + spacecraft
                                                           #  flown-arc backfill
                                      --refresh-spacecraft # OPTIONAL, rare: force a
                                                           #  full re-pull of the
                                                           #  flown arc from the
                                                           #  discovered start (only
                                                           #  needed if Horizons
                                                           #  revises a past
                                                           #  ephemeris point;
                                                           #  NOT load-bearing)
                                      --dry-run [--object SLUG]
                                      --output-dir <path>  # default: data/solar-system/
```
`--dry-run`: full pipeline for one object (default: one of each category present
in config) through staging + validation, writes NOTHING outside `.staging/`,
prints the would-be run manifest. This is Stage 2's `--preflight-only` discipline,
carried by name in the docstring.

## S10. What to verify after build

1. Provenance scan Tier-1 = 0 on the new module.
2. Pre-build gate 3: the backup action AND the `.gitignore` backup-path entry
   both EXIST before first build.
3. `--dry-run` on voyager_1: confirm the ephemeris START is discovered from
   Horizons (not launch+1), the flown arc backfills, and NO future is fetched.
4. `--dry-run` on encke (LOAD-BEARING, F4): confirm the solution-Tp two-role
   resolution runs (`resolve_tp` -> epoch -> converged osculating TP served),
   the `2P` apparition disambiguation picks the current record, and the served
   `Tp_jd` MATCHES the desktop `resolve_tp` result (Mode 5 -- a valid-looking
   conic is not proof the epoch is right).
5. First build: spot-open `raw/vectors/charon.json` -- every magnitude inside
   Charon's Guard band (~0.000117 AU scale). Deliberately inject one out-of-band
   test point and confirm it produces a LOUD guard WARNING (not a silent accept
   and not a reject) -- the monitor's teeth.
6. Served `coverage_index.json`: `generated`, `attribution`, `served_window`
   present; `as_of_today` in km; Pluto/Charon centers = pluto_barycenter.
7. Kill-test atomicity: interrupt a run mid-fetch; confirm live tree untouched,
   no commit, staging retained.
8. Nightly x3: three consecutive scheduled runs produce three clean commits,
   frozen dates stable byte-for-byte, refresh window overwritten, spacecraft
   endpoint advancing one point/night.
9. Backup: confirm a successful commit triggers the separate backup action and
   `raw/` lands in the gitignored local path (and is NOT committed).
10. Exhibit displays "data as of <generated>".

## S11. Deferred -- named, not specced

L-100 shells interactive-vs-gallery split; L-101 osculating-history fan (its
future data already accretes via F6); L-102 spacecraft thinning (Douglas-Peucker,
served-side; raw stays daily); L-103 hyperbolic browser branch (port
`generate_hyperbolic_orbit_points`, `idealized_orbits.py:4719`); L-104 preset
generator (the null `event_link`/`presets` slots are its interface); L-105
`merge_orbit_data` desktop guard. NEW this session: L-106 gallery-cache backup +
gitignore (a first-build PRECONDITION, not deferred -- it must exist before first
build). Carry-forward tags: the np.interp containment lesson returns with Phase 2
composition; `--dry-run` descends from `--preflight-only`.

## S12. Lineage

GALLERY_DATA_SOURCE_HANDOFF v0.4 (this session's amendments) over v0.3 (converged
design). Code claims verified at orrery HEAD this session: ghost purge (`9febac5`,
absent-from-tree + gitignored); `utc_to_tdb` (odm:41); range-query house pattern
(odm:680, sce:~621/632 -- basis of F1); comet perihelion dispatcher
`_add_perihelion_osculating_orbit` (palomas_orrery.py:1533) + leaf
`plot_perihelion_osculating_orbit` (io:7089) -- BOTH exist (F2 correction);
solution-Tp resolver `fetch_solution_tp` (ocm:459) / `resolve_tp` (F4); shrink
guard (odm:418-450); carried derive/serve pieces (`export_orbit_cache.py`).
The comet non-grav delta (solution TP vs converged osculating TP) is rendered on
the desktop (io:7212-7233). Guard v2 evidence: Neso apoapsis 0.572 AU (fetched
July 8, 2026). Ledger: L-098; new L-106; sibling items L-100..L-105.

---

Manifest v1 authored July 2026 with Anthropic's Claude Fable 5.
v2 convergence review + revisions July 2026 with Anthropic's Claude Opus 4.8;
decisions ratified by Tony. Builder: Tony.
