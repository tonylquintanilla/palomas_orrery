# HANDOFF 2026-08-19 -- one row closed, two gaps opened

**Built on `d25b5368875217b8a24593d9431265448e037b69` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery at `8a4aa41268ed9efadea9ad6b40fabe880ce8bef8` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.**

One patch was delivered after that anchor was read and is expected to
land in the commit carrying this file:
`patch_L216_1_swap_lock_and_l214_count.py`. **Confirm HEAD, then confirm
it ran** -- L-216 should be in the ledger index table and L-214 should
carry a COUNTED bullet. If HEAD is not what this file expects, reconcile
before building.

Readable cold. Nothing below assumes the reader was present.

---

## Carried obligations, and the first one is CRITICAL

**1. Confirm the loaded `ledger-and-session-records` reads 1.7 before
doing ledger work.** [CRITICAL, Stale Skill = Stop.] This session loaded
1.6, bumped the skill to 1.7, and reinstalled it to the account profile
-- but a mid-session reinstall cannot be verified from inside the session
that makes it. The manifest in `PROJECT_INSTRUCTIONS.md` was regenerated
and says 1.7. Check your own loaded copy against it at load time.

**2. `gallery-cache-builder` needs a 1.4 bump and was deliberately NOT
bumped.** The discard-and-re-run recovery rule (see L-216) belongs in it.
It was held back to avoid stacking a second unverifiable reinstall on top
of obligation 1. Discharge 1 first, then bump this one.

**3. Archive `patch_L216_1_swap_lock_and_l214_count.py` to
`documentation/`** once run, per the naming-and-archiving convention.

---

## What the next session does

**Decide the L-214 design, then return to the reconciliation.** Tony's
ordering: the builder gap comes first because it pertains to the basic
work. The measurement that gates the design is now done and is in the
ledger.

L-214 is a three-way choice with no obvious winner:

- **Widen** `CONTEXT_LEGS` to include `Note`. One label, 17 lines,
  and it would have changed what three of the pilot's hardest rows were
  checked against.
- **Refuse** on any unrecognised label under a claim. This is what the
  Visibility Convention argues for: a defect with no reader has no
  correction path, so silence is worse than a hard stop.
- **Report** dropped labels into the worksheet, where a responder can
  name them.

These are not exclusive. The reason not to just do the obvious one is
that `Note` is a free-form label doing many jobs across the corpus, and
promoting it wholesale hands responders text nobody curated for them.

**Then the reconciliation, which has not moved.** Four of the five ranked
rows are still open: `STREAMER_BELT_RADII`, `EARTH_EQUATORIAL_RADIUS_KM`,
`HAUMEA_RADIUS_KM`, `BENNU_RADIUS_KM`. Read
`documentation/PILOT_CONVERGENCE_20260819.md` Part 6 first. Note that the
first three of those are implicated by the L-214 count -- their decisive
context was redacted from the dispatch -- so whether their verdicts stand
is now partly a question about the loop rather than about the values.

---

## What happened this session

**L-213 closed, and its own risk statement was wrong.** The orbit cache
backup fired on module IMPORT rather than on cache write.
`create_orbit_backup()` copied `data/orbit_paths.json` to
`data/orbit_paths_backup.json` on every import of `palomas_orrery.py`,
including every maintenance run. The ledger said a corrupted cache would
overwrite the good backup. It would not have: nothing in the codebase
ever READ that file. The real recovery chain --
`data/orbit_paths.json.backup` and `.backup_old`, rotated inside
`save_orbit_paths()` behind a temp-file write, a JSON re-read and a
5-percent shrink guard -- was already doing the job the ledger proposed
building. Tony's ruling: two files, not three; delete the odd one.

**A second defect surfaced in the fix's own output.** The new startup
block listed the two restore points as 130.4 MB dated August 5 and 4,
which looks two weeks stale and is not. `shutil.copy2` preserves mtime,
so a backup's date is when its CONTENT was written, not when the copy was
taken. The live cache's date -- the only one that reveals the last save
-- was not printed. Fixed by printing all three together.

**L-209 closed: `ALFVEN_SURFACE_RADII` was an ALTITUDE used as a
heliocentric radius.** The shell is drawn from Sun centre, so it rendered
one solar radius small. Corrected to 19.7, sourced to the Kasper et al.
2021 PRL body text, which gives the crossing interval as 19.7 to 18.4
solar radii from the center of the Sun. The widely quoted 18.8 is the
press release's altitude figure; the paper does not print it.

**The correction was already in the file, on lines nobody could see.**
Two comment lines under the constant already said "HELIOCENTRIC: from Sun
center ... Kasper's paper says 18.4-19.7 R_sun from center." A previous
session found the distinction, wrote it down, and left the value alone.
Those lines rode on a bare `Note:` and an invented `HELIOCENTRIC:` label,
neither of which the request builder reads. That is L-214.

**Twelve typed copies of 18.8 became reads of the constant.** Tony's
standing approach: constants live in `constants_new.py`, modules call
them, and the explanation is visible in the file. Eight interpolations in
`solar_visualization_shells.py`, one each in
`comet_visualization_shells.py` and `info_dictionary.py` (which gained
its first import), and two sites that cannot read a value -- a docstring
and a `# Source:` comment -- had the figure dropped.

**L-215 opened: cleanup by topic, not by age.** Tony's proposal,
replacing a by-age triage. RICE Effort is a property of an item GIVEN
what else is open, so an item is cheaper inside a file the job already
holds. Baseline: 107 open items, 54 both below RICE 3.0 and untouched for
30-plus days. The first sweep found L-028 already DONE and still counted
as debt at 69 days, and a ruled ASCII violation in a file this session
had open. Recorded in `ledger-and-session-records` 1.7.

**The gallery nightly wiped its served tree, and we found out why.** See
L-216. Short version: a filesystem lock, almost certainly OneDrive, makes
directory renames fail. Which of the swap's three renames it catches
decides whether you get a harmless quarantine or a missing live tree. It
has been catching the harmless one every night since July 21 -- that is
what the ~30 quarantine directories are.

---

## Key documents

| Document | What it answers |
|---|---|
| `PROJECT_INSTRUCTIONS` v3.41 (resident) | How this project works. |
| `documentation/PILOT_CONVERGENCE_20260819.md` | What the pilot found. Start here for the reconciliation. |
| `LEDGER_CONSOLIDATED.md` | L-209, L-213, L-215 closed today; L-214, L-216 opened; L-181, L-191, L-210, L-211 are the live neighbours. |
| `documentation/patch_L213_2_remove_startup_backup.py` | As-run. |
| `documentation/patch_L213_3_cache_line_and_close.py` | As-run. |
| `documentation/patch_L209_2_alfven_migration.py` | As-run. |
| `documentation/patch_L215_1_by_topic_cleanup.py` | As-run. |

Skills that fire on this work: `provenance-discipline` (2.5),
`safe-file-editing` (1.4), `ledger-and-session-records` (1.7),
`gallery-cache-builder` (1.3), `orrery-coding-conventions` (1.4).
Compare each against the manifest at load.

---

## Errors and process failures, recorded

**1. Claude offered a ruled convention as a choice.** Asked how to
propagate the corrected Alfven value, Claude presented "retype at 15
sites" versus "interpolate" as two options. No Shadow Constants
[CRITICAL] was in the loaded `provenance-discipline` and settles it.
Tony's correction: "Our approach is to migrate constants to
constants_new.py and have the modules call the constant."

**2. Claude read a truncated grep window and reported a false absence.**
It told Tony the heliocentric distinction had been "caught for the
sibling and missed here." It had not been missed; it was documented two
lines below the window Claude had looked at.

**3. Claude misattributed an ASCII violation to L-187.** L-187 is
`info_dictionary` numeric-overlap enumeration and has nothing to do with
encoding. The violation had no ledger item at all.

**4. The patch filenames said the opposite of the run order.** Two
patches were delivered with a cross-handle dependency --
`patch_L209_2` had to run after `patch_L213_3` -- but the sequence number
is scoped to its own ledger handle, so sort order contradicted run order
and only the prose carried it. The base guard caught it and wrote
nothing. **The naming convention has no way to express a cross-handle
sequence; that is a real gap in `safe-file-editing` and is not yet
recorded as an item.**

**Not an error, recorded because it shaped the evening.** The gallery
cache emergency consumed roughly half the session and had nothing to do
with the scheduled work. The reconciliation Tony opened the day asking
for closed exactly one of its 13 rows.

---

## What NOT to do

**Do not treat any responder claim as a verdict.** Unchanged from the
previous handoff, and now sharper: three of the queued rows were checked
against a redacted version of themselves.

**Do not re-dispatch the affected rows reflexively after fixing L-214.**
A second dispatch of a row this project has already argued about in
writing is not an independent leg.

**Do not bump `gallery-cache-builder` before obligation 1 is
discharged.**

**Do not run the gallery builder with `--commit` while L-216 is open.**
The discard-and-re-run recovery depends on nothing reaching the remote
until Tony commits by hand.

---

*Written August 19, 2026 with Anthropic's Claude Opus 5. Built on
`d25b5368875217b8a24593d9431265448e037b69`; gallery at
`8a4aa41268ed9efadea9ad6b40fabe880ce8bef8`.*
