# GALLERY BUILDER BUILD MANIFEST v1 -- gallery_cache_builder.py

**Type:** BUILD MANIFEST (Mode 2 -- agentic, new standalone module, GALLERY repo)
**Author:** Claude Fable 5 (per FABLE5_MANIFEST_REQUEST_gallery_builder.md);
Opus 4.8 convergence-review before build.
**Design source:** GALLERY_DATA_SOURCE_HANDOFF v0.3 (converged; the source of
truth). Where this manifest and v0.3 disagree, the disagreement is FLAGGED in
S0 -- nothing silently resolved.
**Base:** orrery HEAD `081ee18` | gallery HEAD `4b086a6` -- both confirmed
live via `git ls-remote` this session (July 8, 2026). Re-resolve live HEADs at
build session start; do not hardcode.
**Pre-build gates:**
(1) GHOST PURGE -- **VERIFIED SATISFIED at `081ee18`** (commit `9febac5`
    "remove obsolete cache"): `git ls-tree -r` shows `data/solar-system/` and
    `_export_out/` deleted from the orrery repo; `.gitignore` at HEAD covers
    both paths. Request S8 is closed; no build-session action needed beyond a
    one-line re-confirm if orrery HEAD has moved.
(2) Copy-source availability: `export_orbit_cache.py`,
    `orbit_data_manager.py` (utc_to_tdb, range-query pattern, shrink guard),
    `idealized_orbits.py` present at orrery HEAD -- verified this session.
**Post-build gates:** provenance scan Tier-1 = 0 on the new module before
push; `--dry-run` clean on one object; first full build passes the complete
validation suite before its commit.

---

## S0. Flags -- forks found and decisions made (review these first)

Per the request: every decision the handoff left open, and every spot where
the handoff and live code disagree.

**F1 -- Chunking vs range query (handoff/request vs code: resolved toward
code).** The request specifies spacecraft arcs "fetched in CHUNKS (~75
epochs/query)." No chunking exists anywhere in the code at HEAD, and the
house pattern is the opposite: every desktop fetch uses a Horizons **range
query** (`epochs={'start','stop','step'}`) -- `spacecraft_encounters.py`
fetches an entire mission window at 1h step in ONE call (line ~622), far more
epochs than a Voyager daily arc. The ~75 limit applies to **discrete epoch
lists**, not ranges. This manifest specs range-query primary (one call per
spacecraft arc, ~17,900 daily points for Voyager, ~1.4 MB served); the
chunked discrete-list fetch is documented only as a fallback if the dry-run
hits a server-side range cap (recalled cap ~90k output lines -- unsourced;
dry-run verifies).

**F2 -- Function name correction.** The handoff cites
`_add_perihelion_osculating_orbit()`. No such symbol at HEAD. The real
function is **`plot_perihelion_osculating_orbit`** (`idealized_orbits.py:7089`;
referenced by `comet_visualization_shells.py:586`). Same concept, wrong name;
all provenance comments must cite the real symbol.

**F3 -- Refresh-window semantics reinterpreted under the conic model
(decision made; ratify).** v0.3's rule "overwrite [today-7d, today+horizon]"
was drafted in the trace era. With general traces retired, non-spacecraft
objects fetch NO future points -- the conic covers the future visually and
the as-of-today point is "you are here." This manifest sets **horizon = 0
for non-spacecraft**: the nightly vectors window is `[today-7d, today]`
(8 daily points in one range query, overwrite-by-date; dates older than 7d
are frozen). The raw archive still grows -- one frozen point per object per
night -- which IS the preservation asset accreting. Predictions exist only
in spacecraft arcs (see F5).

**F4 -- No comet in the seed tranche (fork presented, not decided).** The
tranche has no comet, so the Tp-anchored fetch path -- the one genuinely
novel fetch behavior in this builder -- ships unexercised. Options:
(a) add one comet to the seed (recommended: cheap, and the tranche's stated
purpose is covering every pattern); (b) accept untested until catalog growth.
The config's worked comet row (S2) is ready either way. **Tony decides.**

**F5 -- Spacecraft arcs: write-once + manual refresh (decision made;
ratify).** Fetched once at `--first-build`; the nightly does NOT re-fetch
them. Rationale: ballistic SPK solutions are effectively frozen for a
coasting spacecraft, and nightly re-fetching a 17,900-point arc violates
"the nightly builder stays light." The leading-edge principle is honored by
an explicit `--refresh-spacecraft` flag (run annually or on solution-update
news). The run manifest records spacecraft as `skipped: write-once` so the
skip is visible, not silent.

**F6 -- Osculating elements history retained in raw (decision made;
ratify).** Elements are fetched nightly (cheap; one provenance chain). The
raw cache appends each night's element set to a per-object JSONL history
(~100 bytes/object/night). This makes the deferred L-101 osculating-history
fan buildable FROM THE ARCHIVE later, with zero refetching -- preservation
principle applied to elements, not just vectors. Served index carries the
latest set only.

**F7 -- "Horizons horizon 2029-12-12" is unsourced.** Not found in code or
handoff v0.3's verified claims. The dry-run probes the actual Voyager SPK
end (attempt the full range; on rejection, read the error's stated span and
set the config `end` from fact). Do not hardcode the recalled date.

**F8 -- Guard v2 nailed: k = 2.0, two-sided, per-trace reject.** Handoff
gave k ~ 1.5-2. Chosen 2.0: osculating a,e are snapshots, and Kozai-class
irregulars (the Neso case that motivated Guard v2) swing widely between
snapshots -- 1.5 risks false-rejecting the very objects the guard was fixed
for. Separation survives: worst-case moon band (Neso: 2 x 0.33 AU x 1.57 ~
1.04 AU) vs. Neptune's 30 AU heliocentric magnitude is still ~29x. And the
band is **two-sided** (S4) -- which also catches the reverse class (relative-
scale points under a heliocentric key) that a max-only check passes.

---

## S1. What We're Building

One standalone Python script, `tools/gallery_cache_builder.py`, living in the
GALLERY repo (`tonyquintanilla.github.io`). Nightly it: reads the object-list
config -> fetches fresh from Horizons per object with the explicit canonical
center -> validates on write (Guard v2) -> builds raw cache + derived served
files in STAGING -> runs the full validation suite -> atomic swap -> single
commit + push. No orrery imports; hard-won fetch specifics are COPIED WITH
PROVENANCE COMMENTS (S3). The deliberate duplication is ledgered
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
```

---

## S2. Object-List Config (`objects_config.json`) -- the single authority

Both the builder and the coverage index derive from this file. Nothing about
an object lives anywhere else.

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
- `id_type` -- "majorbody" | "smallbody" | "id" (house pattern: smallbody
  for comets/asteroids per `celestial_objects.py`; "id" for spacecraft per
  `spacecraft_encounters.py:631`).
- `category` -- planet | moon | dwarf_planet | asteroid | comet | spacecraft.
- `canonical_center` -- Horizons location string ("@sun", "@9", "@599").
- `center_slug` -- served slug; must resolve via the carried CENTER_SLUG_MAP.
- `trace_policy` -- "none" | "full-arc" ("osculating-history" reserved, L-101).
- `features` -- [] (flows to feature_configs; comet structure lives HERE,
  deferred -- never in orbit data).
- `overrides` (opt):
  - comet: `{"anchor": "Tp", "max_distance_au": 100}`
  - spacecraft: `{"start": "YYYY-MM-DD", "end": null}` (null end = probe the
    SPK horizon at dry-run, F7)
  - `event_windows`: [] (reserved, L-104)
- `notes` (opt) -- human context.

**Seed = the tranche** (the house "9-object tranche" label; it enumerates 10
rows since Saturn was added in v4): earth, jupiter, saturn, moon, io, titan,
pluto, charon, apophis, voyager_1 -- slugs/ids/centers carried verbatim from
v4 TEST_OBJECTS (`export_orbit_cache.py`), including `pluto` at `@9`
(barycenter trajectory) and `charon` at `@9`.

**Worked row -- spacecraft:**
```json
{ "slug": "voyager_1", "name": "Voyager 1", "horizons_id": "-31",
  "id_type": "id", "category": "spacecraft", "canonical_center": "@sun",
  "center_slug": "sun", "trace_policy": "full-arc", "features": [],
  "overrides": { "spacecraft": { "start": "1977-09-06", "end": null } },
  "notes": "start = launch + 1 day; end probed from SPK at dry-run (F7)" }
```

**Worked row -- comet (example; enters the seed only if F4 goes (a)):**
```json
{ "slug": "encke", "name": "2P/Encke", "horizons_id": "2P",
  "id_type": "smallbody", "category": "comet", "canonical_center": "@sun",
  "center_slug": "sun", "trace_policy": "none", "features": [],
  "overrides": { "comet": { "anchor": "Tp", "max_distance_au": 100 } },
  "notes": "Tp-anchored conic; exact Horizons record verified at dry-run
            (multiple apparitions resolve under '2P' -- pick current)" }
```

Config docs must state: **catalog growth beyond the tranche is gated on
Guard v2** (this builder ships it, so the gate is satisfied by construction
-- the sentence exists so the config, the authority, says so).

---

## S3. Fetch, per object (astroquery jplhorizons)

Copy-with-provenance sources (cite file:line and "Copied from ... orrery
HEAD <SHA>; sync-on-change" in comments):
- `utc_to_tdb` -- `orbit_data_manager.py:41` (the TDB boundary fix).
- Range-query pattern + '@'-prefix center normalization + id_type
  passthrough -- `orbit_data_manager.py:~670-690`.
- `refplane='ecliptic'` on `.vectors()` -- `spacecraft_encounters.py:~632`.
- Epoch parser (HH:MM), `_dt_to_jd`, `parse_osc_epoch_to_jd`,
  `_true_to_mean_anomaly_deg` (the MA-None fallback), CENTER_SLUG_MAP +
  `resolve_center_slug`, KM_PER_AU usage -- `export_orbit_cache.py:198-300`.

**3a. Osculating elements -- every non-spacecraft, nightly.**
`Horizons(id, id_type, location=canonical_center, epochs=epoch_jd).elements()`
(pattern: `osculating_cache_manager.py:496`).
- Default: epoch = today.
- Comet override (`anchor: "Tp"`): two-step -- (1) elements at today; read
  the `TP` field (verified present in the elements set at HEAD); (2) re-fetch
  elements AT epoch = TP; serve the Tp-epoch set with `Tp_jd` as the anchor
  field + `max_distance_au`. Matches `plot_perihelion_osculating_orbit`
  (`idealized_orbits.py:7089` -- F2 name correction).
- `orbit_type` is DERIVED from fetched e (e < 1 elliptical, e >= 1
  hyperbolic), not declared; a config `expected` mismatch warns.
- Append the fetched set to `raw/elements/<slug>.jsonl` (F6):
  `{run_id, epoch_jd, a, e, i, omega, Omega, MA, TP, retrieved}`.

**3b. Actual-motion accretion -- every non-spacecraft, nightly.**
ONE range query: `epochs={'start': utc_to_tdb(today-7d), 'stop':
utc_to_tdb(today), 'step': '1d'}`, `location=canonical_center`,
`.vectors(refplane='ecliptic')` -- 8 points. Guard v2 (S4) on the batch.
Overwrite-by-date into `raw/vectors/<slug>.json`; dates older than
`freeze_after_days` are never re-fetched (frozen past). The **as-of-today
point** served in the index = the last point of this batch. Units: raw
stores AU + JD exactly as fetched (full fidelity); the derive step converts
to km (KM_PER_AU, carried).

**3c. Spacecraft full-arc -- `--first-build` / `--refresh-spacecraft` only
(F5).** ONE range query: start = config start, stop = probed SPK end (F7),
step '1d'. Guard: spacecraft sanity only (S4). Written to raw once; served
`positions/<slug>.json` in km/JD (v4 position-file format, carried).
Fallback if the range is rejected: split the span in half recursively
(NOT fixed 75-epoch chunks; range-halving keeps the query count logarithmic),
stitch by date, assert no duplicate/missing dates at the seams.

**3d. First build backfill.** `--first-build` runs 3b with
`start = today - backfill_days` (365): one ~366-point range query per
object, then the nightly takes over. Idempotent: re-running overwrites the
same dates with the same data.

No general position traces for non-spacecraft. No preset fetching (`presets`
slot exists, null; Apophis 2029 is L-104's business).

---

## S4. Guard v2 -- on write (replaces the global 0.5 AU `#F`)

Applies to every fetched vector point of every object WITH osculating
elements, in whatever frame the canonical center defines. Let q = a(1-e),
Q = a(1+e) from the object's own current osculating set, k = 2.0 (F8):

- **Elliptical (e < 1): accept the batch iff every point satisfies
  q/k <= |r| <= k*Q.** Two-sided: the upper bound catches heliocentric-scale
  points under a relative frame (the Charon 35.7 AU class, rejected ~10^5 x);
  the lower bound catches relative-scale points under a heliocentric frame
  AND cross-body mixups (Pluto-body points in a Charon fetch fall below
  Charon's q/k).
- **Hyperbolic (e >= 1): accept iff q/k <= |r| <= 1.1 * max_distance_au.**
- **Spacecraft (no elements): exempt from the band.** Sanity instead:
  0 < |r| < 200 AU, timestamps strictly increasing, no NaN/null coordinates.
- **Violation behavior: REJECT the whole object's fetch for this run** --
  never clip points out (partial contamination means untrusted provenance).
  Keep last-good raw; the object serves stale with its old `retrieved`
  stamp; record the rejection + offending magnitudes in the run manifest.
- The carried **B3 magnitude re-check** (copied from
  `export_orbit_cache.py:~494-510` with provenance comment) runs on the
  SERVED files in the nightly validation suite -- defense in depth behind
  Guard v2, and the continuity of the exact check that caught the original
  contamination.

---

## S5. Raw cache formats

`raw/vectors/<slug>.json`:
```json
{ "object": "io", "center": "@599", "center_slug": "jupiter",
  "unit": "au", "epoch_type": "JD",
  "points": { "2026-07-01": { "jd": 2461222.5, "x": ..., "y": ..., "z": ... },
              "...": {} } }
```
Date-keyed (daily cadence by design -- this builder never stores sub-daily;
the deferred time-keyed follow-on is a different artifact). Overwrite-by-date
= dict update on the refresh window. Append-only outside it.

`raw/elements/<slug>.jsonl`: one JSON line per run (S3a).
`raw/runs/<run_id>.json`: the per-run build manifest --
`{run_id, started, finished, window, objects: {slug: fetched|skipped:
write-once|failed:<reason>|rejected:<guard detail>}, guard_results,
validation: pass|fail, committed: bool, repo_size_mb}`.

---

## S6. Derive step -> served outputs (v4 schema, carried)

From staged raw, per object: latest elements + `orbit_type` + anchor fields
(+ `Tp_jd`, `max_distance_au` for comets) + `as_of_today` `{t, x, y, z}` in
**km/JD** + `positions` ref (spacecraft only) + `event_link: null` +
`presets: null` + `retrieved`.

Index top level: `schema_version`, `generated` (UTC ISO), `generator`
(name+version), `attribution` ("Data: JPL/NASA Horizons"), `served_window`
(a DERIVE PARAMETER -- starts as the full raw window; bounding it later is a
one-line change, not a schema change), `objects{}`.

Invariants asserted before the index is written (carried set + new):
- **#2** spacecraft -> no osculating AND positions present.
- **#3** every non-spacecraft -> osculating present.
- **#5** every `center` resolves to a valid slug.
- **#6** every non-null preset file exists on disk (vacuously true; slot null).
- **#8** every `positions.file` referenced exists on disk.
- **#C** osculating.center == config `center_slug` (center-match, carried).
- **#V** (new) Guard v2 re-verified against the SERVED numbers (post-km-
  conversion -- catches a unit-conversion bug, not just source contamination).
- **#T** (new) `as_of_today.t` within 48h of `generated` for every fetched
  (non-stale) object.
- **#W** (new) served_window is contained in the raw window.

`feature_configs.json`: best-effort from config `features` lists; renderers
are Phase 2; comet structure explicitly deferred (two-surface principle).

**Mixed-version reads (carried mitigation):** the index's `generated` value
doubles as the cache-buster -- exhibits append `?v=<generated>` to
position-file fetches and tolerate a missing file gracefully. The exhibit
displays "data as of <generated>" -- the staleness monitor that costs
nothing.

---

## S7. Nightly atomicity -- the ordered, testable checklist

1. `run_id` = UTC timestamp. Window computed FROM TODAY at run time
   (idempotent, self-healing -- a missed night heals tomorrow, by design).
2. Build entirely under `.staging/<run_id>/` (raw copy-forward + new
   fetches + derived served tree). The live tree is never touched.
3. Per-object isolation: each object's fetch+guard in its own try/except;
   failure or Guard rejection -> carry forward last-good raw for that
   object, mark it in the run manifest, CONTINUE the batch.
4. Full validation suite ON STAGING, every night: invariants #2-#W + the
   B3 served-file re-check. ANY failure -> ABORT: no swap, no commit,
   `.staging/<run_id>/` retained for autopsy, run manifest written with
   `validation: fail`.
5. Shrink gate (pattern: `orbit_data_manager.py:418-450`, provenance
   comment): staged raw point-count >= 95% of live, per object AND in
   aggregate. Fail -> ABORT as step 4.
6. Atomic swap: rename live -> `.prev`, staging served+raw -> live
   (`os.replace`, same filesystem); `.prev` deleted only after step 8
   succeeds (belt-and-suspenders rollback within the run; git is the
   rollback across runs).
7. Repo size tripwire: measure; > 800 MB -> WARN loudly (console + run
   manifest) but do not block. The escape hatch (split to a data repo;
   same-origin serving survives under the custom domain) is documented in
   the config notes, not improvised at 2 a.m.
8. Single commit of the data paths, message `data: nightly YYYY-MM-DD`;
   push. Push failure (network): leave the commit local; tomorrow's push
   carries both -- no retry loop.
9. The run manifest is written into `raw/runs/` BEFORE the commit, so every
   commit carries its own provenance record.

---

## S8. Deployment

- Desktop Task Scheduler now; the builder is standalone so migrating to a
  GitHub Action later is a scheduler detail. **Probe Actions this month**
  (one manual workflow-dispatch Horizons fetch) so the migration path is
  fact before it's needed.
- PAT: fine-grained, gallery repo only, `contents: write`, stored in the
  Windows credential store (git credential manager) -- never in the script,
  never in the repo.
- The scheduled task runs `--nightly`; a failed exit code surfaces in Task Scheduler
  history, and the "data as of" display is the user-visible monitor.

## S9. Interface

```
python tools/gallery_cache_builder.py --nightly            # default nightly run
                                      --first-build        # 365d backfill + spacecraft arcs
                                      --refresh-spacecraft # manual arc re-fetch (F5)
                                      --dry-run [--object SLUG]
                                      --output-dir <path>  # default: data/solar-system/
```
`--dry-run`: full pipeline for one object (default: one of each category
present in config) through staging + validation, writes NOTHING outside
`.staging/`, prints the would-be run manifest. This is Stage 2's
`--preflight-only` discipline, carried by name in the docstring.

## S10. What to verify after build

1. Provenance scan Tier-1 = 0 on the new module.
2. `--dry-run` on voyager_1 (probes SPK end, F7) and on the comet row if
   F4 = (a): confirm the Tp two-step and the anchor fields.
3. First build: spot-open `raw/vectors/charon.json` -- every magnitude
   inside Charon's Guard band (~0.000117 AU scale); the 35.7 AU class is
   structurally impossible now, confirm anyway (Mode 5 of data).
4. Served `coverage_index.json`: `generated`, `attribution`,
   `served_window` present; `as_of_today` in km; Pluto/Charon centers =
   pluto_barycenter.
5. Kill-test atomicity: interrupt a run mid-fetch; confirm live tree
   untouched, no commit, staging retained.
6. Nightly x3: three consecutive scheduled runs produce three clean
   commits, frozen dates stable byte-for-byte, refresh window overwritten.
7. Exhibit displays "data as of <generated>".

## S11. Deferred -- named, not specced

L-100 shells interactive-vs-gallery split; L-101 osculating-history fan
(its future data already accretes via F6); L-102 spacecraft thinning
(Douglas-Peucker, served-side; raw stays daily); L-103 hyperbolic browser
branch (port `generate_hyperbolic_orbit_points`, `idealized_orbits.py:4719`);
L-104 preset generator (the null `event_link`/`presets` slots are its
interface); L-105 `merge_orbit_data` desktop guard. Carry-forward tags: the
np.interp containment lesson returns with Phase 2 composition; `--dry-run`
descends from `--preflight-only`.

## S12. Lineage

GALLERY_DATA_SOURCE_HANDOFF v0.3 (converged design; v0.1 Opus 4.8 -> v0.2
Fable 5 review -> v0.3 trace & conic model). Code claims verified at orrery
HEAD `081ee18` this session: ghost purge (`9febac5`), `utc_to_tdb`
(odm:41), range-query house pattern (odm:684, sce:622 -- basis of F1),
`plot_perihelion_osculating_orbit` (io:7089 -- F2), shrink guard
(odm:418-450), carried derive/serve pieces (`export_orbit_cache.py`).
Guard v2 evidence: Neso apoapsis 0.572 AU (fetched July 8, 2026). Ledger:
L-098; sibling items L-100..L-105.

---

Manifest v1 authored July 2026 with Anthropic's Claude Fable 5.
Convergence review: Claude Opus 4.8 (pending). Builder: Tony.
