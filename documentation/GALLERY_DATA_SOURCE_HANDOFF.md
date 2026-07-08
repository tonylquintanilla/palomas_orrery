# GALLERY DATA-SOURCE HANDOFF -- fetch-fresh rebuild (design session)

Tony Quintanilla, PE | Claude | July 8, 2026

**Type:** DESIGN SESSION (zero code) -- the architecture pivot for how the
gallery gets its orbit data. Converge here, then manifest, then build.
**Base:** orrery HEAD `d4c37cf` | gallery HEAD `4b086a6`.
**Supersedes:** the "read the legacy orrery cache" INPUT model of Stage 2
(manifest v4 S2). Everything else in v4 carries forward (see "What carries").
**Ledger:** L-098 (capture the pivot).

================================================================
THE PIVOT
================================================================
Stop reading the legacy desktop cache to feed the gallery. Build a clean,
purpose-built gallery cache by fetching fresh from Horizons with the correct
center per object, stored in the GALLERY repo, refreshed by a nightly batch.
The legacy `orbit_paths.json` stays exactly as it is, for the desktop orrery.

Why (the structural reason, not just the Charon bug): the desktop never trusts
its own position traces for orbits -- it draws orbits from osculating elements
and fetches fresh points only for the current view, so historical-trace
corruption is invisible there. The gallery does the opposite: it SERVES the
raw cached traces. So the gallery is exposed to precisely the data the desktop
is immune to. The Charon/Pluto contamination (heliocentric points under a
barycenter key, from a fetch before the `@9` override) is one instance; the
extent across 1501 accreted entries is unknowable, and `merge_orbit_data`
merges blindly by date with no frame check. Auditing that is whack-a-mole.
A clean, bounded, validated rebuild is cheaper and provably correct.

================================================================
DECIDED (Tony, this session)
================================================================
- FETCH-FRESH, not validate-or-refetch. Clean provenance over reuse.
- NIGHTLY BATCH refresh (the batch Horizons call we already planned).
- Cache lives in the GALLERY repo (new file), NOT the orrery -- repos stay
  separate-clean.
- Historical depth: start ~1 year back (see the window proposal below).

================================================================
ARCHITECTURE (proposed -- ratify the open choices)
================================================================
A standalone builder in the gallery repo:

  gallery builder (astroquery, no orrery import)
    -> reads a gallery OBJECT LIST (object + center + features)
    -> fetches per object: osculating elements + daily position vectors
       in the object's CANONICAL center (sun / earth / jupiter / saturn /
       pluto_barycenter / ...), with the #F magnitude guard ON WRITE
    -> writes a clean gallery raw cache  (gallery repo)
    -> derives the served files (coverage_index.json + positions/*.json)
       -- the same v4 schema, unchanged
  run nightly (deployment detail, below); commit + push to the gallery repo

The `#F` frame guard becomes a SOURCE-side gate here: a fetched trace whose
magnitude is inconsistent with its declared frame is rejected at write, so
contamination can never enter the gallery cache in the first place. (The
export-side `#F` guard stays too, as defense in depth.)

--- Open choice 1: intermediate raw cache, or direct-served? ---
  (a) RECOMMENDED -- builder writes a clean raw gallery cache (full-fidelity
      fetched vectors), and a derive step writes the served files from it.
      Keeps the raw fetched data (fits "data preservation"), lets us re-derive
      different served views without re-fetching. Two artifacts.
  (b) builder writes the served files directly, no intermediate. Simpler, one
      step, but the raw fetch is not preserved separately.
  Lean (a): the raw archive is the preservation asset; deriving is cheap.

--- Open choice 2: where it runs nightly ---
  (i)  Desktop Task Scheduler now (reliable, your IP, fast to stand up),
       migrate to a GitHub Action later. RECOMMENDED start.
  (ii) GitHub Action in the gallery repo from the start (fully self-contained,
       no desktop dependency) -- but Horizons-from-CI (shared runner IPs, rate
       limits) is unproven; test one fetch from Actions before committing.
  Because the builder is standalone, this is a scheduler detail, not an
  architecture change -- (i) now, (ii) later, same script.

--- Open choice 3: date window + cadence ---
  Proposal: DAILY cadence; window = [anchor, today + horizon], grown nightly,
  never dropping old points (an ever-growing archive -- preservation).
    anchor  = 1 year before first build (your "go back ~1 year").
    horizon = today + 1 year (rolling; nightly appends the new leading edge).
  Rationale: osculating gives the full orbit shape for ANY object (slow outer
  bodies included), so the daily trace only needs to supply recent+near-future
  actual motion, not a full slow orbit. ~2-year rolling daily window x tens of
  objects is a few MB -- trivial. Preset windows (e.g. Apophis 2029 close
  approach) are fetched as separate event-specific spans when those presets
  are built. Fast moons (Io) stay osculating-only at daily cadence, exactly as
  now; sub-daily traces remain the deferred time-keyed-cache follow-on.

--- Open choice 4: object list scope ---
  Start with the 9-object tranche (proven), then grow to a curated gallery
  catalog. The list is a gallery-repo config: {slug, name, horizons_id,
  category, canonical center, features}. This is the v4 TEST_OBJECTS promoted
  to a data file the builder and the coverage index share.

================================================================
WHAT CARRIES FORWARD FROM STAGE 2 (unchanged)
================================================================
- The v4 product model (osculating primary; direct trace additive).
- The coverage_index + position-file schema (reconciled to design handoff
  v0.6; verified field-for-field).
- The invariants (#2,#3,#5,#6,#8,#C) and the #F frame guard (now also source-
  side).
- The center-slug map, epoch parser (HH:MM), JD convention, KM_PER_AU.
- Osculating cache: the `@9` override makes current osculating fetches correct;
  the tranche osculating already matches the desktop exactly. Re-fetching it
  fresh with validation is cheap insurance.
What changes: only the SOURCE. `export_orbit_cache.py`'s "read the desktop
caches" input is replaced by "fetch fresh." The derive/serve half is reused.

================================================================
RISKS / REVIEW TARGETS (known; Fable to weigh + find more)
================================================================
- GIT GROWTH: a nightly commit of a growing cache to the gallery repo grows
  git history. Git delta-compresses append-mostly JSON well, but over years
  clone/history size climbs, and the same-repo-serving model keeps the data in
  the tracked tree. Options to weigh: commit only the SERVED files (smaller,
  derived) and keep the raw cache OUT of git (build artifact / release asset);
  an orphan data branch; git LFS; periodic squash; or accept it. This tension
  with the "ever-growing archive" choice (3) is the biggest open risk.
- NIGHTLY FAILURE MODES: partial fetch, Horizons downtime, rate limits, a
  single object erroring mid-run. The builder must be atomic -- never leave a
  half-written cache -- with the desktop's backup + size-guard discipline (a
  save that would shrink the cache >5% is blocked).
- STANDALONE vs REUSE: a standalone astroquery fetch avoids coupling the gallery
  to the orrery, but reimplements fetch logic (a parallel pipeline -- a named
  anti-pattern). Is a minimal vectors+elements fetch simple enough to own
  separately, or should the builder import one thin shared fetch module? Weigh
  repo-separation against duplication.
- #F THRESHOLD (0.5 AU): robust for the 9-object tranche, but does it hold
  across ALL gallery objects -- distant irregular moons (parent-relative up to
  ~0.2 AU), near-Earth objects, comets? Confirm it separates every legitimate
  frame from heliocentric contamination, or make it parent/frame-aware.
- OSCULATING SOURCE: fetch osculating fresh (clean provenance) vs trust the
  desktop's `@9`-override osculating (already correct for the tranche). Fresh is
  cheap insurance; confirm no reason to prefer reuse.
- CADENCE: daily trace -- right gallery-wide? Fast moons stay osculating-only;
  is that acceptable, or do some objects warrant the deferred sub-daily
  (time-keyed) fetch sooner?


1. Tony ratifies choices 1-4 (or redirects).
2. Manifest: the standalone gallery builder (fetch + validate + write raw cache
   + derive served files) + the nightly-run wiring + the object-list config.
3. Build (separate session): the builder, pre-tested; a first full build over
   the window; #F source guard verified; commit the gallery cache + served
   files; schedule the nightly run.
4. The old contamination question closes itself: the gallery never reads the
   legacy cache, so Charon/Pluto (and every object) come out clean by
   construction.

Ledger L-098 delta: pivot from legacy-cache-read to fetch-fresh gallery cache
in the gallery repo; nightly batch; standalone builder; #F guard promoted to
source-side. Stage 2 schema/model/served-format retained. New sibling item
candidate: the `merge_orbit_data` source-side frame guard for the DESKTOP
cache (optional hardening; prevents recurrence of legacy-style contamination).

---

Design handoff written July 2026 with Anthropic's Claude Opus 4.8.
