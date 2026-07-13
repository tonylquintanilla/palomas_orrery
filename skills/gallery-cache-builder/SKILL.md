---
name: gallery-cache-builder
description: Nightly data-serving pipeline for the Paloma's Orrery web gallery (Phase 1b, ledger L-098). Use for any task touching tools/gallery_cache_builder.py, tools/test_gallery_cache_builder_offline.py, inspect_staging.py, debug_encke_tp.py, gallery_cleanup.py, data/objects_config.json, the data/solar-system/ serving cache (coverage_index.json, feature_configs.json, positions/, raw/), atomic-swap / .prev / .staging_* / .quarantine_* semantics, Guard v2, dry-run / first-build / nightly modes, documentation/TESTING_PROTOCOL.md layers, or wiring interactive.html to the served data. Do NOT use for the Studio/converter/viewer curation chain (that is gallery-pipeline) or for projects other than Paloma's Orrery.
fires_when: Nightly builder, atomic swap, coverage_index, serving cache, objects_config, dry-run/first-build/nightly, builder testing layers
---

# Gallery Cache Builder (Phase 1b data serving)

Skill version: 1.1 | Cut from tonyquintanilla.github.io @ a08bdd10 (code) and palomas_orrery @ af58f7f8 (context) | 2026-07-12

The standalone nightly builder that fetches fresh JPL Horizons data and deploys
the web gallery's served cache. A GALLERY-repo tool; this skill is authored in
the orrery repo per the L-002 convention (both SHAs on the cut line, like
gallery-pipeline). For the interactive Studio/converter/viewer chain, load
gallery-pipeline instead.

## What it is

tools/gallery_cache_builder.py: read data/objects_config.json -> fetch fresh
from JPL Horizons per object at its explicit canonical center -> validate in a
STAGING directory -> whole-generation atomic swap of data/solar-system/ ->
single verified commit + push. It REPLACES the served generation every run by
design (the prior cache's framing errors were unfixable in place), so "runs
without errors" is never the gate -- validation is. No orrery imports; the
hard-won fetch specifics are provenance-copied from the orrery with per-function
# Source comments, kept in sync on change.

Key functions: run_build (orchestrator), derive_served (raw -> served files),
assert_structural + shrink_gate (validation), atomic_swap_dir /
recover_incomplete_swap / _sweep_siblings (deployment), guard_monitor /
emit_guard_warnings (Guard v2), git_commit (push with round-trip verify),
douglas_peucker (glide thinning), load_config, main.

## Swap blast radius [QUALITY]

atomic_swap_dir replaces data/solar-system/ WHOLESALE (live -> .prev,
staging -> live; a rename is all-or-nothing, so a crash leaves either a
COMPLETE .prev or a COMPLETE live, never a mixed generation). Anything that must
survive a build lives OUTSIDE that directory. The config is a sibling,
data/objects_config.json, for exactly this reason (L-114: it was stranded into
.prev on every real build when it lived inside). Before adding any file the
builder READS but does not WRITE into staging, decide which side of the blast
radius it belongs on.

## Sibling directory semantics [QUALITY]

- data/solar-system.prev/ is the retained ONE-GENERATION rollback and the
  self-healing recovery source. NORMAL BUT SCARY: it looks like a stale
  duplicate; never hand-delete it. recover_incomplete_swap clears it at the
  next run's start once live is confirmed healthy.
- .staging_solar-system_* and solar-system.quarantine_* siblings are crash
  remnants. _sweep_siblings reaps them after keep_days (default 3); recent ones
  are kept deliberately as autopsies (A-11). Throwaway; do not build on them.
- A stale .prev that recovery cannot clear (e.g. a Windows file lock from a
  backup/AV process) is QUARANTINED and the run proceeds, rather than wedging
  every future run; the sweep reaps the quarantine later.

## Recovery ordering (why L-114 mattered twice)

recover_incomplete_swap runs at build start. load_config reads the sibling
data/objects_config.json, so it no longer depends on the swap-managed directory
existing -- which is what used to deadlock: config-inside-the-swap-dir meant a
crash mid-swap left load_config unable to read the config before recovery could
restore the directory. Moving the config out (L-114) closed that; a crash
mid-swap now self-heals on the next run.

## Validation stance

Two dispositions, and the difference is load-bearing:
- ABORT (raise ValidationAbort -> nonzero exit; Task Scheduler history is the
  monitoring channel): structural invariants (#2/#3/#C/#8), #B3
  conversion-consistency (served km must equal raw * AU at the matching point),
  the #T as_of_today freshness check, and the shrink_gate (per-object AND
  aggregate point count must be >= 95% of the live generation; first build is
  exempt).
- WARN AND KEEP, never reject: Guard v2 (guard_monitor / emit_guard_warnings,
  the per-object k*a(1+e) distance band). It is a MONITOR, not a gate.

Field note: an inline comment near line 755 mislabels this as "guard/B3 WARN".
#B3 is an ABORT -- the code raises ValidationAbort. The module docstring is
correct; the inline comment is stale (candidate cleanup, tracked separately).

## Commit with round-trip verify

git_commit (N2) does not report pushed_remote until it has confirmed the remote
branch CONTAINS the new SHA (git branch -r --contains). A local commit that
never reached GitHub Pages is the exact failure this closes -- the same SHA
round-trip discipline the project uses by hand, baked into the builder.

## The three-layer gate (documentation/TESTING_PROTOCOL.md, orrery repo)

- Layer 1 -- offline suite (mocked fetch, 75 checks): proves the LOGIC. Run
  `python3 tools/test_gallery_cache_builder_offline.py` from a CLEAN checkout
  after ANY builder or config-layout change -- it is the canary for path
  assumptions (the L-114 config move silently broke it until the test's own
  path was swept; see field notes).
- Layer 2 -- live dry-run on Tony's hardware: `--dry-run --object <slug>` per
  tranche object, then a real --first-build. Proves the OUTPUT against real
  Horizons.
- Layer 3 -- scheduling (unattended nightly). Correctness/operability items
  gate this (gap-aware catch-up, a health summary) -- see L-098 / L-111.

## Adding a new object -- the full sequence, and where it silently breaks

Beyond the three-layer gate above, onboarding a genuinely NEW object needs
two things the general gate description doesn't spell out:

- **--first-build is required, not --nightly, for a new non-spacecraft
  object.** Verified in code: only first-build mode fetches the full
  365-day backfill window for non-spacecraft objects; nightly mode only
  fetches [today - freeze, today] -- a few days. Add an object and run
  --nightly and it onboards with almost no data. first-build also carries
  the N3 floor check (rejects a clipped/truncated fetch), which nightly
  skips. Spacecraft are the one exception: a genuinely new one has no
  prior points, so the code auto-detects this (`not points`) and
  backfills fully regardless of mode.
- **Layer 1's offline suite has a hardcoded served-object COUNT
  assertion** (`check(len(objs) == N, ...)`), separate from the per-object
  ELEMS mock keys. Adding a new object's ELEMS entry is necessary but not
  sufficient -- the count itself needs bumping too, or Layer 1 fails on a
  fully correct addition. Caught concretely adding Halley (11 -> 12): the
  ELEMS/fake_solution_tp mocks were right the first pass; the count
  assertion was the thing still pointing at the old total.

Full sequence for onboarding: (1) source horizons_id/id_type/dates from
celestial_objects.py rather than deriving them -- usually already there
(see horizons-orbital-mechanics for the record-pinning rule); (2) add the
ELEMS mock entry (+ fake_solution_tp branch if Tp-anchored) AND bump the
count assertion; (3) Layer 1 from a clean checkout; (4) Layer 2:
--dry-run --object <slug> against real Horizons; (5) --first-build (not
--nightly, per above).

## Fetch facts proven live (2026-07-11 gate)

- Periodic comets pin to a specific 900000XX record (Encke 90000091; Halley
  90000030 pattern). The short-designation trap and full rule live in
  horizons-orbital-mechanics.
- Spacecraft arcs: a coarse glide (fetch_step, ~7d) + daily densify inside
  curated event_windows (flybys) + douglas_peucker thinning of the GLIDE ONLY
  (windows are pinned, exempt). Voyager 1 verified: both windows fully daily,
  zero gaps; 49-year glide 2549 -> 29 points with a genuine 12-year straight
  segment. Refresh is overwrite-by-date on the forward window; the past is
  frozen.

## Field notes

- The moved config had FOUR consumers (builder argparse default, offline-test
  primary path, offline-test comment, TESTING_PROTOCOL prose). Moving the file
  without sweeping the consumers broke Layer 1 at HEAD (L-114/F1). When a
  producer moves, grep every consumer -- then run Layer 1 from a clean clone as
  the proof they all moved.
- interactive.html (gallery repo root) is the EVENTUAL consumer of the served
  data; at the time of writing it does not yet read data/solar-system/ (zero
  references -- verified). Describe the wiring as future work (L-102's open
  question), not as existing.

Origin: created for L-098 (Phase 1b) from Fable 5's 2026-07-12 Mode 7 review;
every code fact verified against gallery HEAD 8e060677 / orrery HEAD e83fe9ce
with Anthropic's Claude Opus 4.8.
