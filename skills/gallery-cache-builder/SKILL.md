---
name: gallery-cache-builder
description: Nightly data-serving pipeline for the Paloma's Orrery web gallery (Phase 1b, ledger L-098). Use for any task touching tools/gallery_cache_builder.py, tools/test_gallery_cache_builder_offline.py, inspect_staging.py, debug_encke_tp.py, gallery_cleanup.py, data/objects_config.json, the data/solar-system/ serving cache (coverage_index.json, feature_configs.json, positions/, raw/), atomic-swap / .prev / .staging_* / .quarantine_* semantics, Guard v2, dry-run / first-build / nightly modes, documentation/TESTING_PROTOCOL.md layers, or wiring interactive.html to the served data; for the rule that a config change is not deployed until the cache is rebuilt; and whenever a rename or a delete under data/ is refused with "Access is denied" (WinError 5), or the swap log data/cache_swap_log.jsonl is being read or written; and for daily_run.py's order, a failed pull and the run records check. Do NOT use for the Studio/converter/viewer curation chain (that is gallery-pipeline) or for projects other than Paloma's Orrery.
fires_when: Nightly builder, atomic swap and its retry/roll-back/swap log, "Access is denied" under data/, coverage_index, serving cache, objects_config, dry-run/first-build/nightly, builder testing layers, the Daily
  Run's order and a failed pull, the run records and their check, a spacecraft fetched by its path plan, a pull that does not match the push, a comet on an open path fetched by its plan (is_path_body, open_path), a small body's own uncertainty (position_uncertainty, the match rule), every JPL question asked fresh (HORIZONS_CACHE), a drawing named on a room's row, an ended mission's last day (fetch_path_last_day), a held body (HELD), a Lagrange point served as a point (serving_shape 'point'), the clock block and its witness, an encounter's package
---

# Gallery Cache Builder (Phase 1b data serving)

Read this file in 3 parts: lines 1-237, 238-505, 506-728.

Skill version: 1.22 | 2026-11-24, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ eb90dff7 and gallery @ 727ebf79. v1.22 (L-522, the
skill's split; L-538, the orbiters' printed error): what the builder
and the Daily Run do moved whole to the gallery's
`CACHE_BUILDER_AS_BUILT.md`; eight sections keep their headings here,
with their rules. Adds A Capture Craft's Box Never Claims Less Than Its
Miss. Riding it, three sentences gone stale (`--commit`, Layer 1's
count, a field note's line numbers). The 1.19 entry moved out.
Earlier: 1.21 | 2026-11-22, with Anthropic's Claude Fable 5.2, at
palomas_orrery @ 849bf462 and gallery @ e6af10ea. v1.21 (L-541, a
plan's clock; L-529, guided encounters) adds The Clock Block and Its
Witness and, under Sibling directory semantics, an encounter's package.
Riding it: the website's second night run exists. Written by the
coordinating session from the ledger and the builder at e6af10ea. The
1.18 entry and five passages of history moved out to stay at the cap.
Earlier: 1.20 | 2026-11-19, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ a70d98c5 and gallery @ 56bc3fab. v1.20 (L-297, the
Lagrange points) adds A Lagrange Point Is Served as a Point, the fourth
serving shape. To stay at the cap, the 1.17 entry, Fetch facts proven
live and a size note of 2026-10-25 moved out. Read from L-297's notes
and the gallery's builder at 56bc3fab before it was written.
Older entries are in documentation/SKILL_HISTORIES.md, moved there on
2026-10-05 (L-418), 2026-10-14 (L-431), 2026-10-15 (L-446), 2026-10-17
(L-449), 2026-10-25 (L-443), 2026-10-26 (L-443), 2026-10-29 (L-399),
2026-10-31 (L-485), 2026-11-01 (L-484), 2026-11-02 (L-507),
2026-11-05 (L-507), 2026-11-11 (L-525), 2026-11-19 (L-297) and
2026-11-22 (L-541) and
2026-11-24 (L-522).

The standalone builder that fetches fresh JPL Horizons data and deploys the
web gallery's served cache. It runs unattended every night on GitHub's
computer, through `daily_run.py --night`, whose gate decides whether the
night's files are committed; Tony can also run it by hand for a build the
same day (see Operating mode below).
What the builder and the Daily Run do now is the gallery's
`CACHE_BUILDER_AS_BUILT.md`, at its root; this skill keeps the rules.
A build that changes them changes that page in the same commit, and
a session reads the page's section for the part it changes (L-522).


## Contents

Generated from this file's headings. skills_index.py --check fails
if this list and the headings disagree (L-418).

- Operating mode -- unattended every night, since October 31 2026
- What it is
- Swap blast radius [QUALITY]
- Sibling directory semantics [QUALITY]
- The swap retries, rolls back, and leaves a record [QUALITY]
- Recovery by hand, when the roll-back also fails [QUALITY]
- The cause, and what is still open
- Never shutil.rmtree anything in this tree [QUALITY]
- The sibling report names what the builder did not make [QUALITY]
- A config change is not deployed until the cache is rebuilt [CRITICAL]
- The Builder Reads the Period's Centre [QUALITY]
- A Spacecraft Is Fetched by Its Plan [QUALITY]
- A Lagrange Point Is Served as a Point [QUALITY]
- The Clock Block and Its Witness [QUALITY]
- A Small Body's Own Uncertainty Is Served [QUALITY]
- Every Question Is Asked of JPL, Fresh [QUALITY]
- A Body That Fails Its Test Is Held [QUALITY]
- A Capture Craft's Box Never Claims Less Than Its Miss [QUALITY]
- The Daily Run's Steps [QUALITY]
- A Served Number That Changes on Purpose [QUALITY]
- Validation stance
- Commit with round-trip verify
- The three-layer gate (documentation/TESTING_PROTOCOL.md, orrery repo)
- Adding a new object -- the full sequence, and where it silently breaks
- Field notes

## Operating mode -- unattended every night, since October 31 2026

THE NIGHT (L-485; Tony's rulings R1 to R5 of 2026-10-25,
documentation/DESIGN_L485_nightly_run_rulings_20261025.md). The
gallery's `.github/workflows/nightly.yml` runs `python daily_run.py
--night` on GitHub's computer at 08:17 UTC (`cron: '17 8 * * *'`), an
hour after the orrery's own night at 07:17, and can be fired by hand
from the Actions tab. The first run, by hand, was clean on 2026-10-31
(commit c1c578f5, by github-actions[bot]). What makes it safe is the
night's GATE, not a person at the keyboard: the workflow commits only
when `daily_run.py --night` exits 0, and stages only its allow-list
(`daily_run.py --allow-list`). The gate's conditions are on the
as-built page, under The Daily Run's Steps; one of them is the guard
this section used to call designed and not built.

- THE DELETIONS-ONLY GUARD IS BUILT, in the gate: a change under
  `data/solar-system/` that is deletions only stops the night, by name.
  That is the August 10 failure -- a half-swapped cache committed by
  someone who did not know a build was running -- refused by the
  machine. (Until 2026-10-31 this was a `pre-commit` hook "deliberately
  NOT built", relevant "if the builder ever runs unattended in any
  other form". It now does.)
- The builder runs with no flags, never `--commit`: it swaps the new
  cache in and stops, and the workflow's own commit step commits after
  the gate.
- A red night commits nothing; the run's log on the Actions tab is its
  only record, and the previous served cache stays live.
- `concurrency: group: nightly-run`, without cancel-in-progress: a run
  fired by hand waits for a running night rather than overlapping it,
  and checks out `main` as it stands when it starts.

BY HAND, for a build the same day. The builder is launched from the
dashboard's Developer Tools group, or by running
`tools/gallery_cache_builder.py` from the GALLERY REPO ROOT. The root
matters: `--config` and `--output-dir` default to paths relative to the
working directory, so launching from `tools/` fails at load_config. No
flags runs nightly mode, and Tony commits in GitHub Desktop. Tony's
morning order since the night exists: Pull origin on both repositories
first, then anything else, without waiting for a night that has not
run yet (the as-built page, The Daily Run's Steps, the night form,
says why).

The history (the Windows task retired on 2026-08-10, after a scheduled
run's failed swap was committed on 2026-07-24) is in
documentation/SKILL_HISTORIES.md since 2026-11-11.

How old the served data is: the night's record,
`data/nightly_run_record.json`, carries its last clean run, and the
orrery's dashboard prints it, red when more than a day old. L-189's
staleness check is the older answer to the same question. A GALLERY-repo tool; this skill is authored in
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
_rename_with_retry / restore_after_failed_swap / swap_log_write /
print_failed_swap_advice / recover_incomplete_swap / _sweep_siblings
(deployment), guard_monitor /
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
radius it belongs on. recover_incomplete_swap runs at build start, so a
crash mid-swap self-heals on the next run (why that needed L-114:
documentation/SKILL_HISTORIES.md).

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
- data/encounters/ is not the builder's (v1.21, L-529): an encounter's
  package is written by hand by `tools/encounter_fetch.py`; the night
  never runs, swaps or commits it, and the sibling check knows the
  folder by name (interactive-exhibit, An encounter is a package).

## The swap retries, rolls back, and leaves a record [QUALITY]

Built 2026-09-20 (L-216), at gallery `a1a516cf`. Before it, a refused
`staging -> live` rename left the working copy with no served cache, a
change list that looked like total loss, and the run's own record stranded
inside a directory `.gitignore` hides. Whether anything bad happened next
depended on Tony reading that change list correctly.

THREE THINGS THE BUILDER NOW DOES, in the order L-216 asked for them.

- EVERY RUN THAT REACHES THE SWAP WRITES ONE LINE to
  `data/cache_swap_log.jsonl`, a TRACKED file that is a SIBLING of the
  served directory rather than part of it -- same blast-radius reasoning
  as the config (L-114). The line is appended with outcome `started`
  before the swap and that same line is rewritten with the outcome after,
  so a process killed outright mid-swap leaves a `started` line saying a
  run reached the swap and never reported back. A dry run writes nothing.
  This came FIRST because without it nothing else here is observable.
- EACH RENAME IS RETRIED. `SWAP_RENAME_ATTEMPTS` is 6 and
  `SWAP_RENAME_WAITS` spends about fifty seconds in total, which is longer
  than any refusal measured. Every attempt after the first prints.
- A SWAP THAT STILL CANNOT FINISH PUTS THE OLD CACHE BACK.
  `restore_after_failed_swap` renames `.prev` back to live with the same
  retries and returns one word -- `live_intact`, `rolled_back`,
  `nothing_to_restore` or `rollback_refused` -- read off the filesystem
  rather than off whichever rename raised. The staging directory is KEPT;
  the sweep reaps it after keep_days.

READING THE LOG IS THE ONLY EVIDENCE THERE IS, because a retry that worked
looks exactly like a run with no problem at all. A LINE WITH MORE THAN ONE
ATTEMPT AND OUTCOME `ok` IS A FAILURE THIS BUILD ABSORBED. A log that only
ever shows one attempt means the lock has not recurred, and proves nothing
either way -- say that rather than claiming success.
`gallery_maintenance_run.py` prints the last line's verdict at the end of
its summary, so it lands on a screen Tony already reads.

WHAT TONY DOES, and it is a routine rather than a judgement call:

  1. RETIRED 2026-10-10: no OneDrive pause. Tony: "the retry is
     sufficient." The builder retries a refused rename and the swap log
     records it; the Daily Run no longer asks (L-216).
  2. Run the builder by hand -- see Operating mode.
  3. Watch GitHub Desktop's change list; do not commit if it looks wrong.
  4. Afterwards, read the last line of `data/cache_swap_log.jsonl`.

Step 4 is new with this version and it is the point of the whole build:
it is the one step that does not depend on anyone noticing anything.
AT NIGHT THE GATE DOES STEPS 3 AND 4 (v1.15, L-485): it reads the swap
log's last line back off the disk and requires tonight's run with
outcome ok, and it refuses a change under `data/solar-system/` that is
deletions only, before anything is committed.

## Recovery by hand, when the roll-back also fails [QUALITY]

The builder now prints these in plain words when it needs them. They are
here too, because a session explaining them should not have to read the
source to do it.

- DISCARD AND RE-RUN. In GitHub Desktop, discard the changes, then run the
  builder again; discard restores the live tree from HEAD byte for byte.
  ONE STEP IS ADDED when the change list also holds work that is NOT the
  cache -- which it did on 2026-09-17, because the arrival work was
  sitting beside the wreckage. COMMIT THE NON-CACHE FILES FIRST, then
  discard the rest, then re-run. A blanket discard throws away
  committed-worthy work.
- RENAME THE STAGING FOLDER. In File Explorer, rename
  `.staging_solar-system_<runid>` to `solar-system`. Tony did this on
  2026-09-20, minutes after Python had been refused, and it worked -- so
  the lock is brief, and Windows will rename a directory it refuses to
  delete.

Three conditions make the discard rule safe and they travel WITH it:

- the live tree is committed, so HEAD has something to restore from;
- the swap is all-or-nothing, so a failed run leaves a COMPLETE `.prev` or
  a complete staging directory and never a mixed one;
- nothing reaches the remote until Tony commits by hand.

Running with `--commit` breaks the third condition and therefore
breaks the rule. Do not use `--commit`: Tony commits and pushes
(the protocol), and at night the workflow commits after the
gate. L-216 closed on 2026-10-08; this did not lapse with it.
The night never passes it: its workflow commits after the gate, and a
night whose swap was not ok, or whose served change is deletions only,
commits nothing, so the third condition holds at night by the gate
instead of by Tony.

## The cause, and what is still open

A filesystem lock -- OneDrive -- makes directory renames fail. WHICH of
the swap's renames it catches decides the damage. Catching the `.prev`
cleanup is harmless and self-heals; the roughly 30
`solar-system.quarantine_*` directories from 2026-07-21 onward are that,
one per night, printing as normal because the builder is built to survive
it. Catching `staging -> live` is the one that hurts.

FIVE OCCURRENCES: 2026-07-24, 2026-08-19, 2026-09-17, and TWICE on
2026-09-20. The exposure is established, not bad luck. The first was
not caught and was committed; the last two came with OneDrive paused,
so pausing is no cure. The account is in documentation/SKILL_HISTORIES.md.

MOVING THE REPOSITORIES OFF ONEDRIVE is the lasting fix and it is
UNDECIDED. Tony, 2026-09-17: "not at this time"; on 2026-09-20, having
seen occurrences four and five, he ruled "do option 1" -- harden the swap
-- "and take it from there as needed". It changes his machine outside his
usual working set. Do NOT propose it casually. If he raises it, what he
wants first is the data inventory, a backup plan for the gitignored local
data (966.8 MB, including star tables he says are difficult to rebuild),
the steps in GitHub Desktop's own terms, and what could go wrong at each
step. The whole analysis is written out in L-216 so it need not be argued
from memory again.

## Never shutil.rmtree anything in this tree [QUALITY]

Every directory under `data/` here carries the Windows read-only attribute
OneDrive sets. Windows permits RENAMING a read-only directory and REFUSES
to delete one, so a plain `shutil.rmtree` dies with `[WinError 5] Access
is denied` at the first subdirectory it reaches. The files inside are not
read-only; only the directories are. Use the `_rmtree_force` pattern: an
`onexc`/`onerror` callback that ADDS the write bit and retries, returning
the count of entries that needed it so a recovery that fired is reported
rather than silent.

THIS APPLIES TO ANY CODE TOUCHING THE TREE, not only the builder. On
2026-09-20 a patch script moving 42 run records out of a conflict copy
called plain `shutil.rmtree` and failed exactly this way, after the
records had been copied and verified. Nothing was lost and the commit was
unaffected -- rmtree unlinks files before it removes directories, and it
failed at the rmdir of a folder it had just emptied -- but a second patch
was needed to finish. The fix already existed in `_rmtree_force` with the
reason in its docstring, and the session that wrote the patch had read
that function an hour earlier. Knowledge that lives only inside a function
does not fire; that is why it is in the skill now.

[QUALITY] rather than [CRITICAL] on this document's own promotion test:
the failure is LOUD and recoverable, and the critical tier only works
while it stays short.

## The sibling report names what the builder did not make [QUALITY]

`documentation/check_cache_siblings.py` globbed only the two name shapes
the BUILDER makes, so four OneDrive conflict copies sitting beside the
cache -- `solar-system (1)`, `(2)`, `(3)` and `1260806133443-solar-system`
-- printed as "no sibling directories". It was a report that could not see
the thing it exists to report. Since 2026-09-20 it classifies EVERY
directory in `data/` and names anything that is neither the live cache,
nor `.prev`, nor a builder-made sibling, under its own heading. `.gitignore`
carries the two known conflict-copy shapes, `data/solar-system (*)/` and
`data/[0-9]*-solar-system/`. Neither the rules nor the report removes
anything; they make it visible.

JUDGE A CONFLICT COPY BY WHAT IS INSIDE IT, not by its name. One of those
four had been committed and published by accident and was described as 42
published files that serve nothing -- a count, from someone who had not
opened them. They turned out to be the ONLY copy of the run history for
2026-07-29 to 2026-09-04, 38 days the live cache's own records skip,
including the 2026-08-19 failure. Those 42 records now live at
`documentation/cache_run_history/` in the gallery repo, with a README
saying where they came from.

## A config change is not deployed until the cache is rebuilt [CRITICAL]

The rooms in `interactive.html` draw their shells from the SERVED CACHE,
`data/solar-system/coverage_index.json`, which this builder copies from
`data/objects_config.json`. Pushing the config alone changes nothing a
visitor sees -- except where the two disagree, and there it breaks the
page.

WHAT HAPPENED, 2026-09-17 (L-336). L-322's gallery half was pushed at
gallery `d2ca28b6` before the builder had run. The unit spellings had
changed in the config and in the renderers (`R_sun` to `r_sun`); the
cache still held the old spelling; the renderers refused every shell
that used it. Tony's phone showed the Sun's room with 9 drawer rows
instead of 18 and Earth's with 8, on the live site, while the
maintenance run printed 11 of 11.

THE ROUTINE, and it is one routine rather than a judgement call:

  1. Change `data/objects_config.json`.
  2. Run this builder, by hand -- see Operating mode. (The night runs
     it too, but on GitHub's copy, so a change not yet pushed is not in
     it.)
  3. Run `python gallery_maintenance_run.py`.
  4. Commit the CONFIG AND THE CACHE TOGETHER, and push.

`tools/check_cache_in_step.py` gates step 3 and compares the served
cache against the config it was built from. A red "Cache in step" right
after a config change is CORRECT and means step 2 has not happened yet.
So is a red Solar System figures check (v1.15, from L-501's close), for
a body the config names and the cache does not hold yet.

THE ONE EXCEPTION, and it is worth knowing because it is the only part
of a room's data the page reads directly: the `arrival` block --
`drawn` and `moon` -- is fetched from `data/objects_config.json` by
`gallery/arrival.js`, not from the cache. A change to what a room OPENS
on needs only the push. Everything else needs the builder.

Three more fields are read from the config by the rooms' drivers, not
from the cache, so they too reach a visitor on the push alone: a body's
`position_accuracy` (L-398), its `description` and `info_url` (L-395),
and its `period` (L-431 build 3), which `tools/mirror_objects.py` copies
from the orrery's export. The orbit drawn around a period's centre is
NOT one of them: it is the cache's `drawn_orbit`, and needs the builder.
Nor is a small body's own uncertainty, the cache's
`position_uncertainty` (A Small Body's Own Uncertainty Is Served).

A STORED DRAWING NAMED ON A ROOM'S ROW IS SERVED TOO (v1.14, L-503).
`serve_drawings()` copies the drawings named under the served objects'
features and, since 2026-10-29, those named on the rows of the config's
`"rooms"` section, which the served index does not hold
(`serve_drawings(staging, index, drawings_dir, rooms=...)`). The main
belt's cloud, the Solar System room's own row, is the first.
`tools/pull_drawings.py` reads the rooms section the same way, so the
orrery's file is pulled before the build serves it.

## The Builder Reads the Period's Centre [QUALITY]

What it does: `CACHE_BUILDER_AS_BUILT.md`, under this title.

- The `period` block is the orrery's, copied onto each entry by
  `tools/mirror_objects.py` from its export, never by hand.
- The served `osculating` block, its positions and its trust
  stay Sun-centred. A `drawn_orbit` is served beside them, at
  the SAME date, never in their place; no perturbation lines are
  drawn for it (Tony, 2026-10-13).
- A set from another date is never paired: the builder raises, the
  pre-swap check aborts, and `tools/check_cache_in_step.py` asks the
  same question from the other side, with the same rule.
- Which bodies this touches is decided by the orrery's period
  records, not here.

## A Spacecraft Is Fetched by Its Plan [QUALITY]

What it does: `CACHE_BUILDER_AS_BUILT.md`, under this title.

- THE PLAN IS THE ORRERY'S ("One path rule, the orrery's."): made by
  `path_plan.py`, copied by `tools/mirror_objects.py`, never by hand.
- Nothing is extended past the span. JPL's predicted part is fetched
  with the rest, and asked again whole when the plan is new, since JPL
  revises it.
- A flyby is never thinned away: an event's window is thinned at its
  own scale and merged after the backbone's thinning.
- An ended mission's last served point is on its span's last day.
- `as_of_today` is today's point, never the path's last; none when no
  point lies within two days before today.
- The shrink gate holds a re-fetch by a new plan out of its count, and
  names it.
- No plan and no typed start: the object fails by name and is served
  last-good, never asked from 1970.
- The offline suite gives a path body with no plan a stand-in plan, so
  it does not depend on a pull.
- A COMET ON AN OPEN PATH IS A PATH BODY: one test, `is_path_body`,
  asked wherever the builder asks "is this a spacecraft?".
- A body that changes side across e = 1 is followed by the mirror,
  never by hand; a side change over fields set by hand is refused, and
  the drawer row is left for a person to check. The suite compares
  such comets with the export by name, with no count to bump.

## A Lagrange Point Is Served as a Point [QUALITY]

What it does: `CACHE_BUILDER_AS_BUILT.md`, under this title.

- A point has no mass and no orbit: no elements are fetched, only
  JPL's positions, a day apart across the window and an hour apart
  near today (Tony, 2026-11-19).
- A point never takes part in the window, so it cannot narrow it.
- JPL's answer is held to the point's own name.
- A failed fetch serves the saved days, today's point nulled.

## The Clock Block and Its Witness [QUALITY]

What it does: `CACHE_BUILDER_AS_BUILT.md`, under this title.

- A served `jd` is on JPL's clock (TDB) and a visitor's minute is UTC,
  so each build serves the difference, asked of JPL and worked out by
  astropy; the build stops, by name, when the two disagree or JPL does
  not answer.
- A witness does not share its clock with what it tests.

## A Small Body's Own Uncertainty Is Served [QUALITY]

What it does: `CACHE_BUILDER_AS_BUILT.md`, under this title.

- Each small body is asked JPL's own uncertainty; the planets and
  Pluto keep JPL's planetary report, from the config. It is cache
  data, so it reaches a visitor only after a build.
- AN ANSWER THAT CANNOT BE SERVED HONESTLY SERVES NOTHING, NAMED,
  and never costs the orbit.
- JPL's answer is matched to the served point within the body's own
  3-sigma, floored and capped; the cap stays under half the closest
  pair of records measured, so one record's answer cannot stand in for
  another's.
- A REFUSAL NAMES ITS NUMBERS, and the run record keeps the refused
  answer.

## Every Question Is Asked of JPL, Fresh [QUALITY]

What it does: `CACHE_BUILDER_AS_BUILT.md`, under this title.

- Every astroquery call the builder makes passes
  `cache=HORIZONS_CACHE`, which is False: a saved answer handed back
  serves an old orbit under a new "retrieved" stamp. The offline suite
  holds every call to the setting; the orrery made the same choice.

## A Body That Fails Its Test Is Held [QUALITY]

What it does: `CACHE_BUILDER_AS_BUILT.md`, under this title.

- Tony, 2026-11-11: "Hold the bad data and report, then continue."
- A moon, or any body with its own span, is NOT held for a number over
  the limit: over it is likely physics, and an older orbit draws it
  worse.
- A held body is served from its entry in the replaced cache, its hold
  copied forward while it lasts; `.prev` is never the store. It leaves
  the served window, is tested every build, and ends when it passes.
- REPORTED, NOT RED: the night's commit title names each held body.
- More than `HOLD_LIMIT` held is a failed build.
- A fault in the maths, not the data, is held while drawn wrong;
  the title is then the only signal.

## A Capture Craft's Box Never Claims Less Than Its Miss [QUALITY]

v1.22, L-538 (2026-11-24). A craft orbiting a planet turns faster
than its served points are spaced, so the room's figure for its
place can be smaller than its real miss (Juno on its close pass of
2026-12-16: good to 574,000 km, off by 3.2 million). What the
builder does about it is on the as-built page, under this title.
These are the rules it follows.

- WHO IS DECIDED BY THE PLAN, NEVER BY A NAME: a craft whose plan
  carries an arrival whose stretch meets the date window. No craft
  is named in the logic, and a plan with two arrivals is read for
  the one that meets the window.
- WHICH SHAPE IS DECIDED BY A MEASURED SIZE, not by a name (the
  coordinating session's reading, as method). Fine points across
  the whole window where they stay small (Tony, 2026-11-23, 23:39:
  "Yes"). Where they do not, fine points around today, a point a
  day elsewhere, and outside the band a figure never smaller than
  the reach of the craft's loop (Tony, 2026-11-24, 09:38: "I agree
  with your recommendation. Fine points around today."). That is a
  coarser, TRUE figure, permanent, and not the stopgap he declined
  on 2026-11-19.
- THE FINER-STEP RULE. When the test finds a step too coarse for a
  craft, the builder makes that craft's step finer, down to a
  floor, and it comes to Tony only if the floor still fails. For a
  craft served whole it covers the daily part as well as the band
  around today (Tony, 2026-11-24, 08:12: "yes"); a craft served in
  the band only keeps a point a day outside it, with the loop's
  floor.
- TWO TESTS, AND THE SECOND IS THE ONE THAT SEES. Each served
  point held out and predicted from the rest; and JPL's own points
  between the served ones. The first alone passed BepiColombo
  while its box was wrong (Part A's report, 56 of 728 minutes).
  Each craft has its own self-test, never a pooled one: a pooled
  count lets one craft's failures stand for another's.
- THE FLOOR IS THE SUM of the chord's figure and the loop's term,
  not the larger of the two: the larger holds only while the two
  parts do not line up.
- JPL'S IN-BETWEEN POINTS ARE NOT COMMITTED (Tony, 2026-11-24,
  14:00: "i agree with the recommendation"). The night tests
  against them. A run anywhere else names each craft it could not
  hold, and never counts it as held. The night is told by a flag,
  never guessed.
- A SIZE IS MEASURED BEFORE A LIMIT IS SET OR A RULING IS ASKED.
  On 2026-11-23 "about 22 KB a craft" was offered as a number and
  ruled on; BepiColombo's measure was 30 times that and more.

## The Daily Run's Steps [QUALITY]

What it does: `CACHE_BUILDER_AS_BUILT.md`, under this title.

- THE ORDER IS THE POINT (Tony's design, 2026-09-27): the guest book,
  the pulls from the orrery, this builder, the maintenance run. The
  pulls come BEFORE the builder, so the build reads what the orrery
  exported today.
- The pull list has ONE home, the maintenance run's GENERATORS. Do not
  add the pulls to `daily_run.py`'s STEPS as rows of their own: that
  is a second copy of the list.
- A PULL THAT CANNOT FETCH FAILS, AND THE DAILY RUN STOPS (Tony's
  option A, 2026-10-15): nothing is built on yesterday's export;
  option B, build on the previous pull and say so in red, was
  declined.
- A PULL THAT DOES NOT MATCH THE PUSH IS A FAILED PULL (Tony,
  2026-10-25: "stop. confirmed."). The cure is Pull origin, orrery
  then website, then the Daily Run again; no retry, no wait.
- EVERY RUN RECORD IS KEPT until the cause of the losses is found,
  then a deliberate limit, its number set at that time, with the
  builder naming each record it removes (Tony, 2026-10-16); on a loss,
  stop and name (2026-10-17).
- AT NIGHT THE GATE DECIDES THE COMMIT: the same steps with no
  keyboard, the guest book skipped (Tony, 2026-10-31), and a red night
  commits nothing. A hold is not red.
- THE MORNING DOES NOT WAIT FOR THE NIGHT (Tony, 2026-11-01): he pulls
  first, and a night that lands later comes with his next Pull origin.
- Apart from the pulls and the records, a step that reports a problem
  does not stop the next. Nothing in the Daily Run commits or pushes.

## A Served Number That Changes on Purpose [QUALITY]

Learned 2026-11-01 (v1.16, L-484, L-485): the orrery's export moved one
served number on purpose (Earth's inner Van Allen belt, 9,600 km to
10,000 km) and two of the website's CHECKS still held the old one.

- THE WEBSITE'S CHECKS CONSUME THE EXPORT TOO. The gallery's "Display
  figures" row, `documentation/smoke_display_figures.js` in the
  gallery repo, pins what the export serves two ways: ACCEPTANCE_LINES,
  the approved wording of each listed hover, and the hover fixture
  every built hover is compared with (`FIXTURE`, a
  `fixture_hovers_<handle>_on_<sha>.json` beside it, re-recorded when
  hovers change on purpose). A served number that moves moves the
  hover, and both pins fail, by name.
- SO BEFORE THE PUSH, GREP THE OTHER REPOSITORY'S CHECKS for the number
  that moves, in the form a visitor reads it ("9,600"), and not only
  its renderers. The orrery session of 2026-10-31 and the coordinating
  session that wrote its brief read the renderers alone.
- THE BRIEF FOR SUCH A CHANGE NAMES THE PINS THAT MOVE, by file, or
  says that none does and how that was found. The gallery session then
  moves each pin in the build that pulls the new export, re-records the
  fixture, and proves the old figure fails by name (2026-11-01:
  `fixture_hovers_L484_on_c1c578f5.json`, "9,600" planted and failing).
- A CHANGE MEANT TO MOVE NOTHING SERVED is proved the other way round:
  save `data/objects_export.json` (or `data/constants_export.json`)
  before the change, diff it after, and name every field that moved.

The check refusing was the gate working; the lesson is that the session
making the change can know ahead. provenance-discipline binds at the
export and asks whether a served number is TRUE (The Gate Binds at
EXPORT); this section is about the other repository still expecting
the old one, which is why it lives here, beside the Daily Run that
pulls the export.

## Validation stance

Two dispositions, and the difference is load-bearing:
- ABORT (raise ValidationAbort -> nonzero exit; the nonzero exit surfaces in
  the console Tony is watching when he starts the run by hand, and at
  night in the run's log on the gallery's Actions tab, where the gate
  reads the builder's exit and turns the night red, so nothing is
  committed -- through 2026-08-10 this read "Task Scheduler history is
  the monitoring channel"): structural invariants (#2/#3/#C/#8), #B3
  conversion-consistency (served km must equal raw * AU at the matching point),
  the #T as_of_today freshness check, and the shrink_gate (per-object AND
  aggregate point count must be >= 95% of the live generation; first build is
  exempt), and more than HOLD_LIMIT bodies held (v1.19, L-525).
- WARN AND KEEP, never reject: Guard v2 (guard_monitor / emit_guard_warnings,
  the per-object k*a(1+e) distance band). It is a MONITOR, not a gate.

Field note: an inline comment mislabels this as "guard/B3 WARN" (search for that string; its line moves with every build).
#B3 is an ABORT -- the code raises ValidationAbort. The module docstring is
correct; the inline comment is stale (candidate cleanup, tracked separately).

## Commit with round-trip verify

git_commit (N2) does not report pushed_remote until it has confirmed the remote
branch CONTAINS the new SHA (git branch -r --contains). A local commit that
never reached GitHub Pages is the exact failure this closes -- the same SHA
round-trip discipline the project uses by hand, baked into the builder.

## The three-layer gate (documentation/TESTING_PROTOCOL.md, orrery repo)

- Layer 1 -- offline suite (mocked fetch, 604 checks at v1.22): proves the LOGIC. Run
  `python3 tools/test_gallery_cache_builder_offline.py` from a CLEAN checkout
  after ANY builder or config-layout change -- it is the canary for path
  assumptions (the L-114 config move silently broke it until the test's own
  path was swept; see field notes).
- Layer 2 -- live dry-run on Tony's hardware: `--dry-run --object <slug>` per
  tranche object, then a real --first-build. Proves the OUTPUT against real
  Horizons.
- Layer 3 -- scheduling (unattended nightly). LIVE AGAIN since
  2026-10-31, in the GitHub Action form (L-485): the gallery's
  workflow at 08:17 UTC. Its gate is the night's (`daily_run.py
  --night`, The Daily Run's Steps, on the as-built page); its health
  summary is the night's
  record, `data/nightly_run_record.json`, which the orrery's dashboard
  reads. The Windows task retired on 2026-08-10 stays disabled. The
  gap-aware catch-up L-098 / L-111 named is not built.

## Adding a new object -- the full sequence, and where it silently breaks

Beyond the three-layer gate above, onboarding a genuinely NEW object needs
two things the general gate description doesn't spell out:

- **--first-build fetches the full 365-day backfill for a new
  non-spacecraft object; nightly mode only [today - freeze, today].**
  first-build also carries the N3 floor check (rejects a
  clipped/truncated fetch), which nightly skips. Whether that matters
  depends on how the room draws the body (v1.15, from L-443's close):
  one drawn from its ELEMENTS, as every orbit in the Solar System room
  is, needs only today's point, so a Daily Run (or the night) onboards
  it -- slice 1's 50 bodies and 2026 ED138 went in that way. A body
  whose drawing needs the past positions themselves needs --first-build.
  Spacecraft and comets on an open path are the other exception: they
  are fetched by their plan, whole when the plan is new. A comet that
  changes side needs no onboarding: the mirror follows it (A Spacecraft
  Is Fetched by Its Plan, on the as-built page, v1.18). An ended mission
  is a spacecraft keyed with `mission_end` (and `end_note`, `cutoff_note`
  where set), which the
  mirror copies (`INSERTED`, since v1.18, L-507 more voyages); its
  config entry is written by hand as Galileo's is, the mirror filling
  the rest.
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

## Field notes

- The moved config had FOUR consumers (builder argparse default, offline-test
  primary path, offline-test comment, TESTING_PROTOCOL prose). Moving the file
  without sweeping the consumers broke Layer 1 at HEAD (L-114/F1). When a
  producer moves, grep every consumer -- then run Layer 1 from a clean clone as
  the proof they all moved.
- The orrery's `osculating_cache_manager.save_cache` writes
  `data/osculating_cache.json` in text mode with no `newline=''`, so on
  Windows every save turns it CRLF; git stores it LF (`* text=auto
  eol=lf`), and on GitHub's Linux computer it is LF anyway (v1.15, from
  L-485). A difference that is only line endings is not a change.
- A BODY THE ORRERY HOLDS IS NOT YET HONOURED HERE (v1.15, L-485, the
  hold). Since 2026-10-31 the orrery's Horizons check holds a body whose
  identity JPL no longer gives as the list does, and its objects export
  (schema 4) carries a `hold` block in that body's confirmation: since
  when, why, what the list says and what JPL said. This builder does
  not read it: `tools/mirror_objects.py` copies only its REPLACED and
  INSERTED fields and drops the rest unnamed, the builder asks JPL by
  the mirrored `horizons_id`, its last-good path re-stamps
  `source.retrieved`, and the website's own confirmations check goes
  red at day 30. So a held body is still fetched and served, and the
  website's night goes red at day 30, as before the hold. Nothing is
  held today. The website's half -- the mirror carries the mark, the
  builder serves last-good named with its own data's date, the hover
  prints the held date, the website's check passes held as held -- is a
  gallery session after the ruler build, recorded on L-485.
