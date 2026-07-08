# FABLE 5 REVIEW -- Gallery Data-Source Pivot

**Reviewer:** Claude Fable 5 | July 8, 2026
**Artifact reviewed:** GALLERY_DATA_SOURCE_HANDOFF.md (+ manifest v4, ledger
L-098, and code/data at orrery HEAD)
**Mode:** Collegial Mode 7, broad-first adversarial. Deliverable per
FABLE_REVIEW_gallery_data_source.md.

---

## 0. Verification record (fetched, not recalled)

- **SHA round trip:** orrery HEAD `cde22c5`, gallery HEAD `4b086a6` --
  confirmed live via `git ls-remote`, both match Tony's stated values.
  The review prompt's base `d4c37cf` is 13 commits behind live HEAD; the
  delta is exactly the Stage 2 record (exporter, test protocols, manifest
  v4, this handoff, committed export outputs). Reviewed against live HEAD.
- **The contamination is empirically confirmed by this reviewer**, not
  taken from the handoff: `data/solar-system/positions/charon.json` at
  `cde22c5` declares `frame: barycenter-relative` and contains point
  magnitudes from 0.000117 AU (correct) to **35.695 AU** (heliocentric).
  `pluto.json` mixes ~0.000014 AU barycentric-relative points with
  35.695 AU heliocentric points under the same declared frame. The
  handoff's characterization is accurate.
- **`merge_orbit_data` claim confirmed at HEAD:** it merges via
  `data_points.update()` keyed by date, with zero frame, center, or
  magnitude awareness. The contamination mechanism is exactly there.
- **`#F` guard confirmed present** in `export_orbit_cache.py` (v4.1):
  relative-frame trace with max |r| > 0.5 AU drops to osculating-only.
- **Irregular-moon extremes (web-fetched July 8, 2026):** Neso passed
  apoapsis in July 2025 at **0.572 AU** from Neptune; S/2021 N 1's
  apoapsis is ~0.50-0.51 AU. Real bound moons cross 0.5 AU. This is
  load-bearing for item 3d below.

---

## 1. Per-item verdicts (one line each)

1. **The pivot itself: SOUND.** Fetch-fresh is the right call; reasoning
   holds (see 2.1).
2. **Open choice 1 (intermediate raw cache): SOUND** -- lean (a) correct,
   and it is the mechanism that resolves choice 3's tension.
3. **Open choice 2 (desktop now, Action later): SOUND** with three
   additions (idempotent self-healing runs, early Actions probe, PAT
   scope).
4. **Open choice 3 (daily, ever-growing, nightly commits): CONCERN** --
   right cadence, but "ever-growing archive" needs a raw/served split,
   provisional-leading-edge semantics, and a size tripwire before it is
   safe to build.
5. **Open choice 4 (object list config): SOUND** -- promote it to the
   single authority, add overrides + schema_version + attribution.
6. **Risks section: mostly SOUND;** git growth is smaller than feared,
   atomicity needs a specific pattern, `#F` at 0.5 AU **demonstrably
   breaks at catalog scale** (false-rejects Neso-class moons).
7. **Carry-forward: SOUND** -- nothing wrongly retained or discarded; two
   lessons must be ledger-tagged so they don't float away (see §5).
8. **Desktop merge guard: SOUND, worth doing** -- it would have prevented
   the original contamination; small, separate ledger item, low priority.

---

## 2. The pivot (review item 1)

**Would I pivot the same way? Yes.** The "extent is unknowable, so
rebuild" reasoning is not a fallacy here, for two reasons the handoff
could state more sharply:

**(a) It is a cost asymmetry, not epistemic surrender.** An audit of the
1,501 legacy entries can only certify the *magnitude-detectable* class of
contamination. Same-magnitude wrong-center contamination -- Pluto body
vs. barycenter points differ by ~0.00013 AU -- is invisible to any
magnitude audit, and the blind `update()` merge means it could exist
anywhere. Only provenance excludes it. Fetch-fresh with an explicit
center per object buys the *stronger* guarantee for *less* work than the
weaker audit.

**(b) The gallery's needs differ from the accreted pair set anyway.**
The legacy cache is every (object, center) pair ever plotted; the gallery
wants one canonical center per object. A fresh fetch aligned to the
object-list config is structurally simpler than mapping legacy pairs --
the pivot removes a translation layer, it doesn't just dodge a bug.

One honesty note for the handoff: state the guarantee correctly.
Fetch-fresh gives *provenance by construction*; `#F` is defense against
gross regressions only, and cannot catch the same-magnitude class. The
sentence "contamination can't enter by construction" should be attributed
to the explicit-center fetch, not to the guard.

---

## 3. Open choices -- recommended convergence (review item 2)

**Choice 1 -- intermediate raw cache: (a), ratify.** The raw archive is
the preservation asset; the derive step is cheap; and -- the point the
handoff misses -- **the raw/served split is what dissolves choice 3's
git-growth tension**: archive depth becomes a property of the raw cache,
served depth becomes a derive *parameter*. In 2036 the raw archive can
hold ten years while the browser downloads two. Decide the split now and
the "ever-growing archive committed nightly" stops being self-defeating.

**Choice 2 -- desktop Task Scheduler now, Action later: (i), ratify,**
with three requirements folded into the manifest:
- **Idempotent, self-healing runs.** The window is computed from *today*
  at run time, so a missed night heals on the next run with no special
  casing. State this as a design property, not an accident.
- **Probe Actions early.** One manual workflow-dispatch fetch from a
  GitHub runner, this month, just to learn whether Horizons-from-CI is
  viable -- so the migration path is fact, not hope, before it's needed.
- **PAT hygiene.** The scheduled task needs push credentials: a
  fine-grained PAT scoped to the gallery repo only, contents:write,
  stored in the Windows credential store, never in the script.

**Choice 3 -- daily cadence + window: ratify the cadence, amend the
archive semantics.** Three amendments:

- **The leading edge is provisional.** Points beyond today are
  *predictions*; Horizons solutions update (materially for comets and
  NEOs, trivially for planets). A strict never-overwrite archive freezes
  stale predictions into the record. Define: nightly re-fetch and
  **overwrite** `[today - k, today + horizon]` (k ~ 7 days); only points
  older than k are archival-frozen. Append-only for the past,
  refresh for the future. This is the single most expensive thing to
  discover after the build (see §6 ranking).
- **Raw/served split** per choice 1: raw grows forever, served window is
  a derive parameter (start: the full raw window; bound it when it
  matters).
- **Git growth: quantified, and it's fine -- with a tripwire.** One
  point per object per day is ~60-80 bytes of JSON; packed deltas per
  object-day are sub-KB. Even a 100-object catalog is tens of MB of
  history per year. The binding constraint is not this pipeline -- it is
  the gallery repo's existing 474 MB against the ~1 GB Pages guidance.
  So: accept, add a repo-size check to the nightly run with an alert
  threshold (~800 MB), and document the escape hatch (split to a data
  repo; same-origin serving survives because project repos serve under
  the same custom domain). Do NOT reach for LFS or history squashes now
  -- both are complexity for a problem that is a decade away at tranche
  scale. Commit-noise: adopt a fixed message convention
  (`data: nightly YYYY-MM-DD`) so history stays greppable.

**Choice 4 -- object list config: ratify, and promote it.** Make it the
single authority both the builder and the coverage index derive from,
with: per-object optional overrides (cadence, preset event windows),
a `schema_version`, and the attribution string (L-086). This is the
envelope principle made into a file.

---

## 4. Risks weighed + `#F` (review item 3)

**Nightly atomicity -- the pattern the manifest should specify:**
1. Build everything to a **staging directory**.
2. Run the full validation suite there -- invariants + `#F` + the B3
   check that caught the original contamination, **every night**, not
   just at build time.
3. Atomic swap into place; **single commit; no commit on any failure.**
4. **Per-object failure isolation:** one object erroring keeps its
   last-good data (and its stale `retrieved` stamp makes that visible in
   the index); it never aborts the batch.
5. Git itself is the rollback -- the previous nightly commit is the
   backup. Import the desktop's >5%-shrink block as a pre-commit gate.
6. **Staleness must be visible without alert infrastructure:** the
   exhibit already fetches `coverage_index.json` -- have it display
   "data as of <generated>". A silently-dead nightly job then shows
   itself to every visitor (and to Tony) instead of rotting for three
   weeks. This is the cheapest monitoring that exists.

**Standalone vs reuse: standalone is right, with copy discipline.** The
desktop fetch path is entangled with exactly the machinery being escaped
(tkinter callbacks, date-only keys, the blind merge). A minimal
astroquery vectors+elements fetch is small enough to own. But the
hard-won specifics must be *copied with provenance comments*, not
re-derived: the `utc_to_tdb` TDB-boundary fix, id_type handling, center
override syntax. Ledger the deliberate duplication ("two fetch paths
exist by design; sync-on-change") so the parallel-pipeline anti-pattern
is a managed exception, not an accident. Cross-repo import would couple
deployment and break the Actions future -- a documented copy is the
honest form here.

**`#F` threshold -- the one place the handoff's risk instinct
under-shoots.** Fetched evidence: Neso's July 2025 apoapsis is 0.572 AU
from Neptune; S/2021 N 1 sits at ~0.50-0.51 AU. A global 0.5 AU
threshold **false-rejects real moons** the moment the catalog grows to
extreme irregulars -- while still passing same-magnitude contamination.
Fix is elegant because the v4 model already fetches the answer:
osculating is PRIMARY, so the expected geometry is in hand.
**Guard v2: per-object band from the object's own osculating** --
accept max |r| <= k * a(1+e) (k ~ 1.5-2 for perturbation slack), and
flag any relative-frame trace whose magnitude approaches the parent's
heliocentric distance. For the 9-object tranche, 0.5 AU is fine as-is;
**gate catalog growth on guard v2**, and say so in the object-list
config's docs.

**Osculating source: fetch fresh, ratify.** One provenance story for the
entire gallery cache beats a hybrid where elements and vectors have
different custody chains. Cost is trivial.

**Cadence: ratify.** Daily gallery-wide, fast moons osculating-only,
sub-daily stays the deferred time-keyed follow-on. Consistent with the
v4 model's own logic.

---

## 5. Missing considerations + carry-forward (review items 4-5)

**Found missing (ranked in §6):**

1. **Leading-edge refresh semantics** -- covered in choice 3 above;
   absent from the handoff entirely.
2. **Committed contamination is live at orrery HEAD.** The pivot says
   the contamination "closes itself," but I verified the contaminated
   served files are *committed and pushed* in the orrery repo at
   `cde22c5` -- both `_export_out/` and `data/solar-system/` (35.7 AU
   points in barycenter-relative files). These are stale ghosts: a
   future session that finds "served files in the repo" will trust
   them, and `data/solar-system/` is the very path name the gallery
   will use. **The pivot's first build step should remove or quarantine
   both directories in the orrery repo** (and gitignore the exporter's
   output path). This is the protocol's own stale-store failure class;
   route around it now.
3. **Mixed-version reads.** Nightly updates + browser/CDN caching mean
   a client can hold a fresh index against stale position files or vice
   versa. Cheap mitigation: the exhibit appends `?v=<generated>` to
   position-file fetches, and tolerates a 404/missing file gracefully.
   (GitHub Pages CDN TTL is short -- ~10 min, recalled not fetched --
   so this is a correctness nicety, not a crisis. Verify the TTL claim
   before relying on it.)
4. **Per-run provenance.** Beyond per-object `retrieved` stamps, commit
   a small per-run build manifest (run id, window, objects fetched,
   guard results, failures). The nightly log becomes the provenance
   trail, and partial failures become visible in history instead of
   silent.
5. **Attribution field.** Top-level `attribution: "Data: JPL/NASA
   Horizons"` in the coverage index (the L-086 pattern). Horizons data
   is US-government public domain (recalled; low risk) -- this is
   courtesy and policy, not license anxiety.
6. **Builder testing strategy.** `--dry-run` (fetch one object,
   validate, write nothing) as the descendant of Stage 2's
   `--preflight-only`; the B2/B3 protocol promoted from build-time test
   to nightly gate.

**Carry-forward audit: the claim "only the source changes" holds.**
Field-checked the retained list against manifest v4; nothing wrongly
retained, nothing wrongly discarded. Two lessons need explicit ledger
tags so they don't float away with the retired subtraction model:
- The **np.interp containment/clamp hazard** (retired invariant #4's
  lesson) returns the day Phase 2 wide-view composition returns. Tag the
  deferral.
- Stage 2's **pre-flight discipline** should be named as carried into
  the builder's `--dry-run`, not silently reinvented.

---

## 6. New risks ranked by cost to discover AFTER the build

1. **Frozen stale predictions** (no leading-edge refresh semantics) --
   discovered months later as data archaeology + user-visible wrong
   paths for comets/NEOs; expensive to untangle from a strict
   append-only archive.
2. **Silent nightly death** -- a gallery quietly three weeks stale;
   costless to prevent now (the "data as of" display), embarrassing to
   discover from a visitor.
3. **The committed contaminated ghosts at orrery HEAD** -- a future
   session or tool trusts `data/solar-system/`; this is the exact
   failure class the protocol was written against, sitting in the repo
   right now.
4. **`#F` false-rejects at catalog growth** -- extreme irregular moons
   silently vanish to osculating-only, and the guard that was
   protection reads as a data bug months later.
5. **Mixed-version CDN reads** -- rare, confusing, unreproducible bug
   reports.
6. **PAT scope/storage** -- low probability, high blast radius.

---

## 7. Would I build this?

**Yes** -- after folding in: the atomicity pattern (§4), the
provisional-leading-edge semantics (§3, choice 3), the raw/served split
(§3, choice 1), the orrery-repo ghost cleanup (§5.2), and the guard-v2
gate on catalog growth (§4). None of these changes the architecture; all
of them are cheaper now than after the first month of nightly commits.
The 9-object tranche can build with `#F` at 0.5 AU unchanged.

**Two rounds: yes, worth it** -- but narrowly scoped. After Opus folds
these in, I'd re-check only the nightly atomicity section and the
refresh-window semantics; those are where the remaining hidden failure
modes live. Everything else converges on this round.

---

Review written July 8, 2026 with Anthropic's Claude Fable 5.
Verification: git ls-remote (both repos), git diff d4c37cf..cde22c5,
direct inspection of served JSON at HEAD, export_orbit_cache.py and
orbit_data_manager.py at HEAD, web search (Neso / S/2021 N 1 apoapsis).
