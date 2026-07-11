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

**tony**: should be 75 checks not 68. Running in Windows so the command is python not python3.

**output**: 
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\tools> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/tools/test_gallery_cache_builder_offline.py
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 11 objects
  ok  first-build structural validation passes (pass)
  ok  clean fakes -> no guard warnings
  ok  11 objects served (11)
  ok  attribution present
  ok  served_window field present
  ok  earth has parity/addition field 'name'
  ok  earth has parity/addition field 'horizons_id'
  ok  earth has parity/addition field 'category'
  ok  earth has parity/addition field 'availability'
  ok  earth has parity/addition field 'parent'
  ok  earth has parity/addition field 'stored_center'
  ok  earth has parity/addition field 'canonical_frame'
  ok  earth has parity/addition field 'trajectory_of'
  ok  earth has parity/addition field 'osculating'
  ok  earth has parity/addition field 'positions'
  ok  earth has parity/addition field 'presets'
  ok  earth has parity/addition field 'features'
  ok  earth has parity/addition field 'orbit_type'
  ok  earth has parity/addition field 'as_of_today'
  ok  earth has parity/addition field 'event_link'
  ok  earth.osculating has 'center'
  ok  earth.osculating has 'epoch_jd'
  ok  earth.osculating has 'a_au'
  ok  earth.osculating has 'e'
  ok  earth.osculating has 'i_deg'
  ok  earth.osculating has 'node_deg'
  ok  earth.osculating has 'peri_deg'
  ok  earth.osculating has 'M0_deg'
  ok  earth.osculating has 'source'
  ok  voyager_1: osculating null, positions present
  ok  voyager_1 position file on disk
  ok  position file unit km
  ok  B-3: serving_base + scene_features restored for v0.6 parity
  ok  B-3: positions block carries step_hours
  ok  earth as_of_today is km-scale (|r|=1.5e+08)
  ok  encke serves Tp_jd + solution_Tp_jd
  ok  encke orbit_type elliptical (e<1)
  ok  pluto/charon centered on pluto_barycenter
  ok  raw vectors written
  ok  elements JSONL history written
  ok  run manifest written
[done] run 20260709T000000Z (nightly): 11 objects
  ok  nightly structural validation passes
  ok  nightly did not shrink earth
  ok  frozen past point unchanged byte-for-byte
  ok  guard: clean charon point -> no warning
  ok  guard: 35.7 AU point -> exactly one warning
  ok  guard: outer-bound trip tagged likely-contamination
  ok  guard KEPT the point (monitor, not reject)
  ok  guard: spacecraft |r|>200 AU -> sanity warning
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 11 objects
[RECOVER] restoring C:\Users\tonyq\AppData\Local\Temp\tmpf7js9k4i\data\solar-system from C:\Users\tonyq\AppData\Local\Temp\tmpf7js9k4i\data\solar-system.prev (crash mid-swap)
[done] run 20260709T000000Z (nightly): 11 objects
  ok  A-1/N1: nightly recovered the whole generation from .prev after a crash
  ok  A-1: archive not thinned by recovery (3740 >= 3740)
  ok  A-1: recovered nightly validates
[ABORT] fail: nightly run but no live raw archive (possible unrecovered crash) -- refusing to build a thin cache
  ok  A-1: nightly with no generation ABORTS instead of committing thin
  ok  A-2: main() exits nonzero on structural abort
  ok  A-2: main() exits 0 on pass
  ok  A-4: majorbody/id -> None
  ok  A-4: smallbody/None pass through unchanged
  ok  DP: straight line -> 2 endpoints
  ok  DP: keeps the bend
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 11 objects
[warn] titan: FETCH FAILED (simulated Horizons outage); served last-good orbit, as_of_today nulled
[done] run 20260709T000000Z (nightly): 11 objects
  ok  A-3: failed Titan still SERVED (not vanished)
  ok  A-3: Titan conic served from last-good
  ok  A-3: Titan as_of_today NULLED (no stale marker)
  ok  A-3: run validates with a stale object
  ok  N4/#B3: correct km conversion passes
  ok  N4/#B3: un-converted (AU-valued) served point ABORTS
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 11 objects
[ABORT] fail: N3 object(s) dropped from a served set: ['titan']
  ok  N3: dropping a served object (titan) ABORTS the publication
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 11 objects
[warn] encke: FETCH FAILED (solution-TP request_failed for encke); served last-good orbit, as_of_today nulled
[done] run 20260709T000000Z (nightly): 11 objects
  ok  N5: solution-TP request failure serves last-good (not silent today-anchor)
[master (root-commit) 02cab93] data: nightly 2026-07-10
 1 file changed, 1 insertion(+)
 create mode 100644 data/f.txt
fatal: No configured push destination.
Either specify the URL from the command-line or configure a remote repository using

    git remote add <name> <url>

and then push using the remote name

    git push <name>

[commit] PUSH FAILED (Command '['git', '-C', 'C:\\Users\\tonyq\\AppData\\Local\\Temp\\tmpfxr1nnr1', 'push']' returned non-zero exit status 128.) -- committed locally only; remote is STALE
  ok  N2: local commit succeeds but no-remote push is NOT reported as pushed
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 11 objects
[dry-run] validated; wrote nothing outside C:\Users\tonyq\AppData\Local\Temp\tmppvji82xl\data\.staging_solar-system_20260709T000000Z
  ok  P2-2: --dry-run --object clears N3 + no-raw against an existing generation
[dry-run] validated; wrote nothing outside C:\Users\tonyq\AppData\Local\Temp\tmpgf_i71tg\data\.staging_solar-system_20260709T000000Z
  ok  P2-2: --dry-run --object works on a clean machine (no raw archive)
[warn] voyager_1: DP thin glide 2548 -> 2 points (tol=0.02 AU)
[done] run 20260703T000000Z (first-build): 11 objects
  ok  P2-1: spacecraft first-build passes #T (arc ends today, not a stale stride point)
  ok  P2-1: spacecraft as_of_today is fresh regardless of stride phase
  ok  #B3: correct per-component conversion passes
  ok  #B3: swapped axes (magnitude-preserving) ABORTS component-wise
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 11 objects
[warn] encke: FETCH FAILED (solution-TP request_failed for encke); served last-good orbit, as_of_today nulled
[done] run 20260709T000000Z (nightly): 11 objects
  ok  P2-9: stale comet carries its comet block forward (not nulled)

PASS (75 checks, 0 failures)
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\tools> 

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

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>python tools/gallery_cache_builder.py --dry-run --object earth
[dry-run] validated; wrote nothing outside data\.staging_solar-system_20260711T014052Z

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>python tools/gallery_cache_builder.py --dry-run --object jupiter
[dry-run] validated; wrote nothing outside data\.staging_solar-system_20260711T014200Z

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>python tools/gallery_cache_builder.py --dry-run --object saturn
[dry-run] validated; wrote nothing outside data\.staging_solar-system_20260711T014213Z

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>python tools/gallery_cache_builder.py --dry-run --object moon
[dry-run] validated; wrote nothing outside data\.staging_solar-system_20260711T014242Z

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>python tools/gallery_cache_builder.py --dry-run --object io
[dry-run] validated; wrote nothing outside data\.staging_solar-system_20260711T014258Z

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>python tools/gallery_cache_builder.py --dry-run --object titan
[dry-run] validated; wrote nothing outside data\.staging_solar-system_20260711T014315Z

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>python tools/gallery_cache_builder.py --dry-run --object pluto
[dry-run] validated; wrote nothing outside data\.staging_solar-system_20260711T014332Z

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>python tools/gallery_cache_builder.py --dry-run --object charon
[dry-run] validated; wrote nothing outside data\.staging_solar-system_20260711T014351Z

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>python tools/gallery_cache_builder.py --dry-run --object apophis
[dry-run] validated; wrote nothing outside data\.staging_solar-system_20260711T014411Z

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>python tools/gallery_cache_builder.py --dry-run --object voyager_1
[dry-run] validated; wrote nothing outside data\.staging_solar-system_20260711T014436Z

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>python tools/gallery_cache_builder.py --dry-run --object encke
[dry-run] validated; wrote nothing outside data\.staging_solar-system_20260711T014455Z

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

2. Encke (2P): confirm the raw vectors header carries TP=. If present, the
   solution-Tp anchor holds; if absent, the conic still draws but Tp_jd degrades
   to elements-at-today -- decide accept vs. alternative here. Cross-check the
   resolved Tp against the desktop resolve_tp for the same object.

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>python tools\inspect_staging.py data\.staging_solar-system_20260711T210156Z
=== Elements (most recent fetch per object) ===
  encke: TP = 2460240.0283  (2023-10-22 12:40 UTC)

**Tony**: pass  

1. Voyager 1: confirm the authoritative start is accepted (no invalid-date
   error), the coarse backbone + flyby-window densification fetch, and the
   Douglas-Peucker prune count is sane. Inspect the arc SHAPE, not just the count.

 C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>python tools\inspect_staging.py data\.staging_solar-system_20260711T014436Z

=== Position arcs (spacecraft) ===
  voyager_1: 105 points
      from 1977-09-06 00:00 UTC  (JD 2443392.5)
      to   2026-07-11 00:00 UTC  (JD 2461232.5)  

**Note**: 
This looks right, and the numbers actually tell a good story if you know what to expect from Voyager 1's real trajectory.
105 points, split roughly two ways:

The two flyby windows (Jupiter, Feb–Mar 1979; Saturn, Oct–Nov 1980) are fetched daily and never thinned — together that's about 70 days ≈ 70 points, always kept in full.
The remaining ~35 points cover everything else: the 1977–1979 approach, the Jupiter-to-Saturn transfer, and then the nearly 46-year straight-line escape from 1980 to today. That last stretch is genuinely close to a straight line in 3D space — Voyager's been coasting on a ballistic trajectory since the Saturn flyby — so Douglas-Peucker collapsing that whole span down to just a handful of points is correct behavior, not data loss. A curve only needs points where it actually curves.

The date range is the cleanest confirmation: starts exactly at 1977-09-06 (launch + 1 day, matching the config), ends exactly at 2026-07-11 — today. That's the P2-1 fix working on real data, not just in the offline suite.

**Tony**: pass

2. First real `--first-build` on the 11-object tranche, then one `--nightly`.

3. Manual crash-recovery drill (once): interrupt a real run during the single
   whole-generation swap; re-run; confirm recover_incomplete_swap restores the
   complete generation. With the whole-directory swap (N1) the browser can only
   ever see a complete old or complete new generation, so this drill now confirms
   atomicity rather than demonstrating a desync.

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
