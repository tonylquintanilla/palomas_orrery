# Gallery Cache Builder -- Testing Protocol

Tony Quintanilla, PE | Claude Opus 4.8 | July 10, 2026
Applies to: tools/gallery_cache_builder.py (Phase 1b, L-098; remediation L-109)

## Purpose

The builder is unattended nightly infrastructure that mutates an irreplaceable
archive (the JPL Horizons raw cache). "Runs without errors" is not the gate.
This protocol defines the three verification layers, in the order they run, and
which reviewer level owns each. The core principle: an offline suite proves the
LOGIC; only the live render on Tony's hardware proves the OUTPUT.

**tony**: framing issue: the builder creates a new cache. the idea was that the original cache contains framing errors that would be impossible to fully identify and fix. the solution was a new cache. 

## Layer 1 -- Offline suite (automated, every change)

Run: `python3 tools/test_gallery_cache_builder_offline.py`
State: 68 checks, 0 failures. Mocks the Horizons fetch layer (no network); must
run from a clean checkout (config resolved from data/solar-system/, A-8).

**tony**: should be 75 checks not 68.

What it PROVES (logic that can be reasoned about statically):
- Pipeline: first-build -> derive -> structural validation -> atomic swap ->
  nightly re-run with the shrink gate.
- A-1/N1 whole-generation crash-recovery: simulate a crash mid whole-directory
  swap (the live generation moved to .prev) and confirm the next run RESTORES the
  complete generation intact, and a true unrecovered loss ABORTS instead of
  committing thin. Because the whole generation is now ONE swap unit, a crash can
  only ever leave a complete old or complete new generation -- never a mix (N1).
- N2 push verification: git_commit distinguishes committed_local from
  pushed_remote (a silent push failure is not reported as published).
- N3 object-set continuity: dropping a previously-served object ABORTS; a
  clipped tiny first-build backfill ABORTS. N4/#B3 conversion-consistency
  (served km == raw AU x KM_PER_AU). N5 structured solution-TP outcomes.
- A-2 exit codes: main() returns nonzero on a structural abort, 0 on pass.
- A-3 stale-serve: a failed fetch serves the last-good conic with as_of_today
  NULLED (object does not vanish; no stale marker).
- A-4 id_type normalization; Douglas-Peucker (drops straight runs, keeps bends);
  B-3 schema parity (serving_base / scene_features / step_hours); the Guard v2
  MONITOR path (warn + keep, never reject).

What it CANNOT prove (structural blind spots -- these are Layer 2/3):
- Real Horizons responses: column names, the 2P header TP= presence, whether a
  pre-SPK spacecraft start clips or errors, apparition disambiguation (CAP;).
- The real desktop cache as a decimation scaffold.
- The RENDER: that a served conic or arc actually draws correctly.

## Layer 2 -- Live dry-run sequence (Tony's hardware, before scheduling)

The container cannot reach ssd.jpl.nasa.gov; this layer is Tony's machine. Order
mirrors manifest S10 (staging -> validate -> atomic swap -> commit):

1. `--dry-run --object <slug>` per tranche object (now runnable in both repo
   states -- P2-2): validate + write nothing
   outside .staging. Confirm the astroquery version is logged (a builder TODO --
   L-112) and there are no id_type deprecation warnings.
2. Encke (2P): confirm the raw vectors header carries TP=. If present, the
   solution-Tp anchor holds; if absent, the conic still draws but Tp_jd degrades
   to elements-at-today -- decide accept vs. alternative here. Cross-check the
   resolved Tp against the desktop resolve_tp for the same object.
3. Voyager 1: confirm the authoritative start is accepted (no invalid-date
   error), the coarse backbone + flyby-window densification fetch, and the
   Douglas-Peucker prune count is sane. Inspect the arc SHAPE, not just the count.
4. Manual crash-recovery drill (once): interrupt a real run during the single
   whole-generation swap; re-run; confirm recover_incomplete_swap restores the
   complete generation. With the whole-directory swap (N1) the browser can only
   ever see a complete old or complete new generation, so this drill now confirms
   atomicity rather than demonstrating a desync.
5. First real `--first-build` on the 11-object tranche, then one `--nightly`.

## Layer 3 -- Schedule

Only after Layers 1-2 pass on the tranche: enable the nightly Task Scheduler job
(working dir = repo root). Watch the first unattended runs; a nonzero exit
(A-2) now surfaces in Task Scheduler history. Backup discipline (L-106) stays in
force: the git history + off-site copy are the archive's rollback of last resort.

## Reviewer level -- recommendation (Mode 7 vs Mode 5)

The question is not either/or. The two modes gate different things, and the
right answer is BOTH, sequenced:

- **Mode 7 (multi-AI adversarial -- Fable) gates the CODE, before the live gate.**
  Recommended for this builder. It earned its place this cycle: the offline
  suite is written by the same author as the code and structurally cannot reach
  the unattended-failure seams (a crash mid-swap, an always-zero exit, a fast
  moon served a stale point). A second, independent adversarial reader found
  exactly those (A-1, A-2, A-3) plus doc drift (B-1, B-2). For novel
  infrastructure whose failure modes are silent and expensive, a Mode 7 read of
  the logic before anything runs live is high-value and cheap relative to the
  cost of an unattended archive-loss.

- **Mode 5 (Tony's visual / render gate) is the AUTHORITATIVE gate on OUTPUT.**
  No AI can perform it from a container. The offline suite mocks Horizons; it
  can pass while the rendered conic or arc is wrong. The Encke Tp match, the
  Voyager arc shape, and the first dry-run render are Tony's eyes on live
  hardware -- and the render wins over any handoff or green suite.

**Recommended sequence:** offline suite (Layer 1, automated) -> Mode 7 code
review (Fable, before live) -> live dry-runs + first build (Layer 2, Mode 5,
Tony, authoritative) -> schedule (Layer 3). Mode 7 gates the logic; Mode 5 gates
reality. Neither replaces the other: a green suite and a Fable sign-off still do
not authorize scheduling until Tony has seen the render.
