# As-built -- L-216: the cache swap stops depending on Tony noticing

**Built on orrery `ee37cc1ff911d96e87fd5d714a456b53f2aef50e` and gallery
`1061ae4d9ad3b7a9b86b483b09db7f9cbd64eed2`, the SHAs the build manifest
was cut from. Pushed at orrery `d426ec009301ca4c95152636363b0d8fd6bbe227`
at https://github.com/tonylquintanilla/palomas_orrery and gallery
`a1a516cfbfe6c83fbd2c79c57a107feb0624ca27` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Every push
in between was confirmed against the live remote with `git ls-remote`
before the next stage was built on it.**

**Rules for the reviewer.** Inside Tony's Project the protocol (v3.65)
and the skills load on their own. This review fires
gallery-cache-builder, safe-file-editing 1.11, agentic-pre-test 1.2 and
ledger-and-session-records 1.11. **gallery-cache-builder should load at
1.6.** If yours reads 1.5, the reinstall did not reach your session: STOP
and tell Tony, per Stale Skill = Stop. **In your first reply, name the
rule files you actually read.**

**Type: AS-BUILT.** Written September 20, 2026 by Claude Opus 5, builder,
for Claude Fable 5.1, reviewer. Tony Quintanilla integrator. The contract
it answers is `documentation/BUILD_MANIFEST_L216_cache_swap_20260920.md`
in the orrery.

Who this is written for: Tony is a retired professional engineer who
builds this project by conversation with AI partners. He is not a
programmer, runs scripts from VS Code's Run button, and commits and
pushes through GitHub Desktop. Write to him in plain sentences, one
request per message.

---

## 1. What was built, push by push

| Repo    | Pushed at  | Patch                                              | What it did |
|---------|------------|----------------------------------------------------|-------------|
| orrery  | `ba94e80e` | `patch_L216_1_ledger_analysis_20260920.py`         | Stage A. L-216 gained the OneDrive analysis, occurrences four and five, Tony's ruling, and the 38-day hole in the run history. |
| gallery | `d0317aa3` | `patch_L216_2_swap_hardening_20260920.py`          | Stage B. Pieces 1 to 4, five files, one transaction. |
| gallery | `a1a516cf` | `patch_L216_3_run_history_20260920.py`             | Refused on Tony's machine and wrote nothing. See section 4. |
| gallery | `a1a516cf` | `patch_L216_3b_run_history_20260920.py`            | Moved the 42 run records and verified the copy; failed at the delete. See section 4. |
| gallery | `a1a516cf` | `patch_L216_3c_remove_conflict_folder_20260920.py` | Removed the emptied folder, clearing the read-only bit on 3 entries. |
| orrery  | `d426ec00` | `patch_L216_4_records_20260920.py`                 | Stage C. gallery-cache-builder 1.5 to 1.6, protocol v3.65, v3.62 moved to the history file, L-216 as-built and new Gap. |

The three `3` patches went into one gallery commit, because 3 wrote
nothing and 3c only finished what 3b started.

**What the builder does now.** Each rename inside the swap is retried six
times over about fifty seconds (`SWAP_RENAME_ATTEMPTS`,
`SWAP_RENAME_WAITS`). A swap that still cannot finish renames `.prev`
back to live, so the working copy is never left without a served cache;
the staging directory is kept. Every run that reaches the swap writes one
line to `data/cache_swap_log.jsonl`, tracked, outside the generation. When
the roll-back also fails, the builder prints in plain words that nothing
is lost and names both hand recoveries. `gallery_maintenance_run.py`
prints the last swap-log line's verdict at the end of its summary.
`.gitignore` gained `data/solar-system (*)/` and
`data/[0-9]*-solar-system/`, and `documentation/check_cache_siblings.py`
names every directory in `data/` the builder did not make.

**The run history is kept.** The 42 records, 2026-07-29 to 2026-09-04,
are at `documentation/cache_run_history/` in the gallery with a README.
`data/1260806133443-solar-system/` is gone.

## 2. How it was tested, and what was not

The offline suite went from 167 checks to 190, all passing on Tony's
machine. The lock itself cannot be produced in a sandbox, so a refusal
was simulated through the builder's own `_rename` seam, the name the real
build path also goes through.

Each piece was then removed on purpose and the matching checks went red
by name, as section 6 of the manifest required:

- retry removed: 4 checks failed, including "a rename refused twice then
  allowed -> the run still passes";
- roll-back removed: 5 checks failed, including "the OLD generation is
  live again, byte for byte";
- log write removed: 7 checks failed, including "the run left exactly ONE
  line in the tracked swap log (found 0)".

Every patch was also tested against a CRLF working copy, against a second
run (each refuses with BASE MOVED or "already done"), and from the wrong
folder. Both maintenance runs were run on the patched tree before
delivery; the gallery's stayed at 15 of 15 and Tony's orrery run is 16 of
16.

**WHAT IS NOT PROVEN.** No real lock has hit the new code. A line in the
swap log with more than one attempt and outcome `ok` is the evidence that
the retry absorbed a failure, and there is no such line yet. If the log
only ever shows one attempt, the lock has not recurred and nothing is
proven either way. Say that; do not claim success.

## 3. Where the build departed from the manifest, and why

1. **Section 8.1 was reversed, on Tony's ruling.** The manifest
   recommended deleting `data/1260806133443-solar-system/` as "42
   published files that serve nothing". Opened, they were the only copy
   of 38 days of run history. Fable confirmed this on review and named
   its own error. Tony ruled to keep them.
2. **The swap log's "one line, written before and completed after" is a
   rewrite, not two lines.** The line is appended as `started` before the
   swap and that same line is rewritten with the outcome afterwards. A
   process killed mid-swap leaves a `started` line, which the maintenance
   run reads as "reached the swap and never reported back".
3. **Patch 3b also REPORTS the untracked conflict copies.** It looks
   inside `solar-system (1)`, `(2)` and `(3)` and names any run record
   that exists nowhere else, without touching them. This was not asked
   for. It was added because the manifest assumed they could be deleted
   by name, which is the assumption that nearly lost the 42. **It never
   ran on Tony's machine** -- see section 4.
4. **The skill's frontmatter gained trigger words.** Its description and
   `fires_when` now name "Access is denied" under `data/` and the swap
   log, so a session meeting either loads the skill.
5. **Two rules were added to the skill that the manifest did not name:**
   never `shutil.rmtree` anything in that tree, and judge a conflict copy
   by what is inside it. Both came from mistakes made in this build.

## 4. Mistakes made during the build, by name

Five reached Tony's machine or would have. One was caught before
delivery. They are listed because two of them are the same shape, and
that shape is the finding.

1. **Stage A overclaimed.** It said all five occurrences were caught by
   Tony reading the change list. Fable found the record says otherwise:
   2026-07-24 was a scheduled run, committed and pushed as "automatic",
   then reverted. Corrected before it ran.
2. **Stage B's CRLF handling matched nothing.** The script normalised the
   content to LF and then translated the anchors to CRLF, so on a CRLF
   file every anchor failed. Caught by the CRLF test before delivery.
3. **Stage B's log test crashed instead of failing by name.** With the
   log write removed, reading the missing file raised and killed the
   suite. Caught by the sabotage run and fixed before delivery.
4. **Patch 3's guard asked the wrong question.** It hashed the whole
   folder's raw bytes. Git normalises line endings on commit and never
   rewrites a working-copy file it merely added, so 24 of the 42 records
   were CRLF on disk and LF in the repository -- same content, different
   bytes. It refused, and reported a number instead of naming what
   differed. 3b compares content file by file and names differences.
5. **Patch 3b called plain `shutil.rmtree`.** Every directory in that
   tree carries the Windows read-only attribute OneDrive sets, which
   blocks delete but not rename. That is L-274, `_rmtree_force` exists
   for it, and the builder session had read that function an hour
   earlier. Nothing was lost: rmtree unlinks files before directories and
   failed at the rmdir of a folder it had just emptied. 3c finished it.

**The shape.** Items 4 and 5, and Fable's count in section 3, are one
failure: knowledge the project already held did not fire where it was
needed. The line-ending rule lives in safe-file-editing, `_rmtree_force`
lived only in a docstring, and "a report names its items" is resident in
the protocol. Two of the three are now in the gallery-cache-builder skill.

**A false statement to correct, and it is live.** Patch 3c's printed
steps say the untracked copies `solar-system (1)`, `(2)` and `(3)` "are
not in git and 3b reported what they hold". **That is false.** 3b's
report runs after the delete, and 3b crashed at the delete, so the report
never printed. Nobody has looked inside those three folders. They are
safe where they are -- untracked, and now ignored by git -- but they
should not be deleted until a report has run. 3c is filed in the
gallery's `documentation/` with that sentence in it; this note is the
correction, rather than an edit to a spent record.

## 5. Open obligations

1. **(do, next session)** Confirm the loaded gallery-cache-builder reads
   1.6 before any cache work. Measured in this session after Tony's
   reinstall: the mounted skill copy still read 1.5, while the project
   instructions in context HAD refreshed to v3.65. So the protocol's
   note that skills bind at conversation start holds, and it does not
   extend to the instructions. That second half is new and belongs in
   the next protocol bump that touches Stale Skill = Stop.
2. **(look, Tony, after the next hand build)** The last line of
   `data/cache_swap_log.jsonl`. Pause OneDrive first and note the time.
3. **(do, before any delete)** A report on what `solar-system (1)`,
   `(2)` and `(3)` hold. Report-only; the code is 3b's
   `foreign_dirs` and `run_record_names`, run on its own.
4. **(decide, Tony, unpressed)** Whether the repositories move off
   OneDrive. L-216 holds the analysis and what a move would need first.
5. **(candidate, for Tony to rule on)** Whether the `_rmtree_force`
   pattern belongs in safe-file-editing as a portable rule. It is in
   gallery-cache-builder now because that is where the tree is. The test
   for moving it is whether any other folder this project writes under
   OneDrive carries the same attribute, and nobody has checked.

## 6. What this changes in the C2 design brief

`BRIEF_L322_C2_design_session_20260920.md` was written while this build
ran, anchored on the two SHAs this build started from. Its task is
unaffected, but six things in it need correcting before a design session
works from it. Each was measured, not recalled.

1. **Re-anchor it.** Orrery `ee37cc1f` -> `d426ec00`; gallery
   `1061ae4d` -> `a1a516cf`.
2. **Its "Rules" line names protocol v3.64 and gallery-cache-builder
   1.5.** Both are now v3.65 and 1.6. A session told to expect 1.5 and
   finding 1.6 is the false alarm that teaches people to wave the
   stale-skill gate off.
3. **Section 4 describes work that is done.** All three of its
   recommendations are built and pushed, and the
   `1260806133443-solar-system` decision is made and executed. The
   section becomes history: C2's cache builds now run on the hardened
   swap, and each one leaves a swap-log line.
4. **One claim in section 3 would send the builder the wrong way.** It
   says three comments in `constants_new.py` claiming
   `test_derived_figures.py` recomputes the two standoffs are false.
   Measured at `ba94e80e`: the test does read both -- it reports "2
   transitional" -- but their verdict is NOT YET MIGRATED, because
   neither carries a `# Figures:` line. The comments describe a check
   that is wired and dormant, waiting on the work C2 does. If C2 gives
   those rows a figure count, the comments become true. If C2 reverts
   them to arithmetic, they stop being transitional and the paragraph
   needs rewriting for that reason. "Correct the false claim" is the
   wrong instruction either way.
5. **Closing Earth is a harder gate than section 1 suggests.** A gap
   FAILS inside a closed slice. Three rows in Earth's set are NOT YET
   MIGRATED today: `EARTH_BOW_SHOCK_CUT_ANGLE_DEG`,
   `EARTH_MAGNETOPAUSE_STANDOFF_RADII` and
   `EARTH_BOW_SHOCK_STANDOFF_RADII`. The maintenance run goes red on the
   closing commit unless all three are migrated first. The other 13
   ungraded rows are outside Earth and stay named rather than failed.
6. **Two small ones.** All seven documents on section 2's reading list
   are filed at `ba94e80e`, including the L-342 as-built the brief says
   may be missing. And `fixture_hovers_cdfa74c3.json` is in the
   GALLERY's `documentation/`, not the orrery's as section 2 implies.

The brief's fixture claim was checked and is exactly right: four Earth
hovers are held byte for byte -- Magnetopause, Bow Shock, Inner Radiation
Belt, Outer Radiation Belt -- beside 18 Sun hovers C2 does not touch.

## 7. Tony-action rollup

1. **(do)** File this document in the orrery's `documentation/`, run the
   maintenance run, commit, push.
2. **(do)** Give it to Fable with the two SHAs at the top, saying which
   is which.
3. **(do, when convenient)** Do not delete `solar-system (1)`, `(2)` or
   `(3)` until a report says what they hold. Ask for the report whenever
   you want to clear them.
4. **(look)** The last swap-log line after your next hand cache build.

---

Written September 20, 2026 with Anthropic's Claude Opus 5.
