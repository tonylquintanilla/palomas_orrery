# The rooms open on the body itself, and the cache gets a check

Built on gallery `9ff39cc4516c7b443f39c1c22e3e8bb338815a8a`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
Orrery at `bb481bf43fe117e34342bd9d992fe9cc116edc70`
at https://github.com/tonylquintanilla/palomas_orrery

The session opened at orrery `9dabda96` and gallery `cb1762a7`. Tony
pushed the orrery twice (`2ef16f3b`: L-322 piece 0 and the L-334 plan;
`bb481bf4`: cleanup, which also filed a copy of the gallery's
`patch_L334_1b` script in the orrery's `documentation/`, where it does
not belong)
and the gallery five times: `34feead`, `e0395e9`, `d2ca28b6` (the L-322
gallery half), then `7c95435`, `59ba809`, `9ff39cc4` (the arrival scene
and a rebuilt cache). Every HEAD named here was read back live. Two
patches delivered at the end of the session are NOT pushed; section
"Delivered, not yet run" names them.

Tony Quintanilla, PE | Claude Fable 5.1 | 2026-09-17, one session, most
of it on Tony's phone
Type: DESIGN + BUILD.
Handles: L-334 (design settled, piece 1 built, Mode 5 passed), L-322
(gallery half confirmed deployed, and a deployment fault found), L-216
(third occurrence).
Companion: `documentation/BUILD_MANIFEST_L334_store_editor_20260917.md`,
which this handoff AMENDS in four places (see "Amendments to the
manifest").
Continues from `HANDOFF_L331_rooms_described_L334_editor_20260916.md`.

---

## STEP 0 -- before you do anything

1. `git status --porcelain` in both repositories. Expect nothing.
2. `git ls-remote` both. Expect the SHAs Tony reports after running the
   two patches under "Delivered, not yet run". If the gallery is still
   at `9ff39cc4`, they have not been run.
3. Version-check every skill at load. This session loaded, and each
   matched the protocol's manifest: ledger-and-session-records 1.11,
   interactive-exhibit 1.3, safe-file-editing 1.11, agentic-pre-test
   1.2, gallery-cache-builder 1.4. No skill was bumped.
4. If `tools/check_cache_in_step.py` exists, run
   `python gallery_maintenance_run.py` and expect 12 of 12.

---

## What happened

**The design of L-334 was settled in four short exchanges.** The
manifest carries it. The ruling that mattered was Tony's: a room opens
on "the surface shell plus frame elements like sun direction, axes,
terminator", and "exclude the moon with its box not selected." That
replaced two earlier rulings of his own: the Sun's 0.25 AU arrival of
2026-08-29, and Earth's eight-shell arrival from the L-291 round of
2026-09-06/08, where the terminator started off.

**Piece 1, the arrival scene, was built and shipped.** Each room's
object in `data/objects_config.json` has an `arrival` block naming the
shells drawn when the room opens. A new function in `interactive.html`,
`sunApplyArrival`, applies it before the opening view is measured, so
the view fits what is drawn. With no block, the page behaves as before.
Tony's Mode 5, both rooms on the phone, 2026-09-17 evening: "yes,
perfect. beautiful."

**The patch did not run the first time, and nothing said so.** Tony
filed the script in `documentation/` and ran it from there. It stopped
with "not in the gallery repo root" and wrote nothing, and the push
went out without it. Claude found it by reading the pushed tree: the
page was byte for byte unchanged.

**The L-322 gallery half broke both live rooms, and 11 checks passed.**
Tony's phone showed the Sun's room with 9 drawer rows instead of 18 and
Earth's with 8. His guess was a conflict with the L-322 deployment, and
it was. The rooms draw their shells from the served cache,
`data/solar-system/coverage_index.json`, which the cache builder copies
from the config. L-322 changed the unit spellings in the config and in
the renderers (`R_sun` to `r_sun`), and was pushed before the builder
had run. The cache still held the old spelling, and the renderers
refused every shell that used it. Claude reproduced the phone's drawer
row for row by building the rooms from the cache record in node.

**The cache rebuild failed at the folder swap, for the third time.**
"Access is denied" renaming the staging folder into `data\solar-system`,
which left the working copy with no served cache and GitHub Desktop
offering 67 changes, most of them deletions. Tony did not push. The
recovery was the rule in gallery-cache-builder (L-216), with one step
added because the same change list held the arrival work: commit the
non-cache files first, then discard the rest, then re-run. Tony paused
OneDrive syncing for the re-run and it succeeded.

**A check now compares the cache with the config.** Built and tested,
delivered, not yet run. It passes at `9ff39cc4` and fails at `d2ca28b6`,
the exact state that broke the rooms, naming 36 differences.

---

## Verified vs claimed

Verified inside the session:

- Every patch was run on a throwaway copy of the PUSHED tree it names,
  and a second run refused. `patch_L334_1` was also run on a copy where
  the L-322 mirror's spelling changes had been imitated, and on the real
  tree after L-322 was pushed.
- The arrival check was broken on purpose three ways (a misspelled shell
  key, the Moon switched on, the page function drawing every shell) and
  failed each time, naming the cause.
- The cache-in-step check was run against two real commits: pass at
  `9ff39cc4`, fail at `d2ca28b6`.
- At `9ff39cc4`: the cache holds only the new unit spellings; both rooms
  build fully from the served cache record with no shell refused; the
  full offline maintenance run passes 11 of 11 in the sandbox, 12 of 12
  with the new check applied.
- The page's inline script parses after the arrival edit.

Claimed and NOT verified here:

- Every render. The rooms cannot start in the sandbox. Tony's phone is
  the only test of what a visitor sees, and his word is quoted above.
- The line in `interactive.html` that sizes the opening view runs only
  in a browser. The arrival check prints the width it expects and does
  not judge the page's own arithmetic.
- The dashboard patch. Tkinter and customtkinter are not installed in
  the sandbox, so the window was never started. What was checked: the
  file compiles, and the new row has the same seven-field shape as the
  Mirror Suite row beside it.

---

## Delivered, not yet run

1. `patch_L334_1c_cache_in_step_20260917.py` -- GALLERY root. Creates
   `tools/check_cache_in_step.py` and adds "Cache in step" to the
   maintenance run. Expect 12 of 12.
2. `patch_L334_1d_dashboard_cache_in_step_20260917.py` -- ORRERY root.
   Adds the Cache In Step button, and corrects a description that said
   "the three Node smoke suites" when the run has six.

Both must be run from their repository's ROOT, then moved into
`documentation/`. Filing first and running second is what silently
skipped `patch_L334_1`.

---

## Lessons

**No check looked at the file the browser reads.** Eleven checks built
their scenes from the config or from a recorded fixture, and the rooms
draw from the cache. A green run said nothing about the live site. The
arrival check written this session had the same blind spot. The general
form: for anything a visitor sees, ask which file the browser actually
fetches, and make one check read that file.

**A config change is not deployed until the cache is rebuilt.** This was
true before tonight and written down nowhere Claude found. It changes
the routine for the mirror, for any config patch, and for the editor:
change the config, run the cache builder, run the maintenance run,
commit config and cache together, push.

**A patch that refuses can look like a patch that ran.** The refusal
printed one line and exited. The protection is on the other side: after
a push, read the pushed tree for the patch's results, not for the
patch's presence.

**The manifest was written on an un-pushed base, against the rule in
ledger-and-session-records.** It said so in its header, and Tony was
spending phone time before his credits reset. It still cost something:
the manifest's picture of how words reach a visitor was wrong in the
way the cache fault later showed. See the amendments.

---

## Amendments to the manifest

1. **Section 2's preconditions are met.** L-322's two patches are
   pushed and the cache is rebuilt. The build can start.
2. **Piece 1 is DONE**, with two differences from the plan. The block
   holds `drawn` and `moon`, with an optional `min_half_range_au` that
   neither room uses; with a block present there is no floor under the
   opening view. And the match from a trace to its shell reads the END
   of the legend group name, because the renderers do not put the
   shell's key on the trace. The cure is for `feature_renderers.js` to
   stamp the key into each trace's `meta`; it is now free to edit.
3. **The editor's Save is not the end of the road.** Words typed in the
   editor reach a visitor only after the cache builder runs. The editor
   needs to say so after a save, and its Run checks button will show
   "Cache in step" red until the builder has run. Decide at the build
   whether the editor offers to start the builder.
4. **Section 8, item 1 (the floor) is settled by Tony's phone check:**
   no floor, the view fits what is drawn.

---

## Still open, for Tony's order

1. **L-334, piece 2 onward: the editor itself.** Next build session.
2. **Move `sunApplyArrival` out of `interactive.html`** into its own
   file under `gallery/`, and have the renderers stamp each trace with
   its shell key. Tony asked whether the page should be modularized.
   Claude's answer: not a general reorganisation now, but a rule --
   logic that needs no browser lives in its own file, where a check can
   reach it, and existing logic moves out when a build touches it. Not
   yet a ruling.
3. **A centre marker for bodies without shells.** Tony, at the phone
   check: the Sun's room has a "Sun" object at the centre, as the orrery
   does, and Earth's has none; "that might be a useful object to add for
   future solar system scenes without shells." New item, not yet in the
   ledger.
4. **L-216, the failed swap.** Tony: "This is like the third time", and
   it is the reason he suspended the scheduled nightly run and builds by
   hand, watching the change list and stopping if the commit does not
   form correctly. The skill still calls the `staging -> live` failure
   "one data point"; that sentence is now wrong and is owed a skill
   bump. The structural cause is that the repository lives under
   OneDrive. Pausing sync before a build worked tonight. The lasting
   fix is moving the repository out of OneDrive's reach, which is a
   change to Tony's machine outside his usual working set and needs its
   steps and risks written out before he decides.
5. **`data/solar-system/feature_configs.json` has no reader Claude
   could find** in the page or the assembler. The new check covers it
   anyway. Whether it is still needed is a question, not a finding.
6. **Carried from the last handoff, untouched:** L-331's residue (the
   page-built hovers), L-333, L-330, L-231, L-273's gallery half, L-061.

---

## Ledger text for the next session to apply

No ledger patch was cut. On L-334, above its Gap line:

> **Design SETTLED and piece 1 BUILT, 2026-09-17.** Contract:
> `documentation/BUILD_MANIFEST_L334_store_editor_20260917.md`, amended
> by `documentation/HANDOFF_L334_arrival_and_cache_check_20260917.md`.
> Tony's ruling: a room opens on "the surface shell plus frame elements
> like sun direction, axes, terminator", the Moon "with its box not
> selected"; this supersedes the 0.25 AU Sun arrival of 2026-08-29 and
> the L-291 eight-shell Earth arrival. Shipped as gallery `7c95435`
> with `59ba809`; Mode 5 on the phone, Tony: "yes, perfect. beautiful."
>
> **Gap:** pieces 2 to 6 of the manifest, the editor itself.

New items to open: the cache-in-step check and the deployment fault
that prompted it (closed on delivery once Tony runs the patch, with the
lesson above); the centre marker; the modularizing rule; and a note on
L-216 recording the third occurrence and Tony's manual routine.

---

## Tony-action rollup

1. **(do)** GALLERY root: run `patch_L334_1c_cache_in_step_20260917.py`,
   move it to `documentation/`, run the maintenance run (12 of 12),
   commit, push.
2. **(do)** ORRERY root: run
   `patch_L334_1d_dashboard_cache_in_step_20260917.py`, move it to
   `documentation/`, file this handoff there too, run the orrery
   maintenance run, commit, push. Report both SHAs.
3. **(do)** Pause OneDrive syncing before each cache build until item 4
   below is decided.
4. **(decide)** Whether to move the repositories out of OneDrive. Ask
   for the steps and risks first.
5. **(decide)** The modularizing rule, and the centre marker.

---

Session written September 2026 with Anthropic's Claude Fable 5.1.
