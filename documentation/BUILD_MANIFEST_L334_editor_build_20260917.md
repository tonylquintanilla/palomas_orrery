# Build Manifest -- L-334: records first, then the arrival tidy-up, then the editor

**Built on gallery `1b077401bbec23d5a7a86c783cf4d92ed1643cbf`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
and orrery `cf414139df8b629d66fc9d1a80f7d89836e22e37`
at https://github.com/tonylquintanilla/palomas_orrery.
Both HEADs were read live with `git ls-remote` on 2026-09-17, and both
repositories were cloned at those SHAs to measure the facts below.**

**Rules this work runs under.** Also fetch, from the orrery at
`cf414139`: `PROJECT_INSTRUCTIONS.md` (v3.61) and these skills under
`skills/<name>/SKILL.md`: ledger-and-session-records 1.11,
safe-file-editing 1.11, agentic-pre-test 1.2, interactive-exhibit 1.3,
gallery-cache-builder 1.4, orrery-coding-conventions 1.9. If you are
working inside Tony's Project they load as installed skills; compare
each loaded version line with the protocol's manifest table and STOP on
a mismatch. **In your first reply, name the rule files you actually
read.** A reply that does not name them tells Tony they were not read.

**Type: BUILD CONTRACT.** Written before the build, zero code.
**Prepared:** September 17, 2026 by Claude Fable 5.1, Tony Quintanilla
integrator. **For:** Claude Opus 5, as builder.
**Companion, and what this does to it:**
`documentation/BUILD_MANIFEST_L334_store_editor_20260917.md` (the
"editor manifest"). Its sections 3, 6 and 7 stand as written and are
not repeated here. Its sections 2, 4, 5, 8, 9 and 10 are REPLACED by
this document. Where the two disagree, this one is later and was
measured on pushed bytes; raise the disagreement if it matters, do not
resolve it silently.
**Continues from** `HANDOFF_L334_arrival_and_cache_check_20260917.md`
and `HANDOFF_L322_mechanism_orrery_half_20260916.md`, both filed in
the orrery's `documentation/`.

Who this is written for: Tony is a retired professional engineer who
builds this project by conversation with AI partners. He is not a
programmer, runs scripts from VS Code's Run button, and commits and
pushes through GitHub Desktop. The quality of the code in these
repositories is the product of that collaboration, not evidence of a
programmer at the keyboard. Write to him in plain sentences, one
request per message. He often works from his phone.

---

## 1. What this build is, in one paragraph

Three stages, each pushed and confirmed before the next starts. Stage A
writes last session's decisions into the ledger, because today they
exist only in a handoff. Stage B moves the function that decides what a
room shows on opening out of the web page and into its own file, and
has the drawing code label each trace with the shell it belongs to, so
the function stops guessing from display names. A visitor should see no
difference. Stage C is the editor itself: a window where Tony changes
the words a visitor reads and ticks which shells are drawn on opening.

## 2. What is already true (verified on the pushed trees, 2026-09-17)

- Both patches the last handoff listed as "delivered, not yet run" ARE
  run and pushed. The gallery has `tools/check_cache_in_step.py`, wired
  into `gallery_maintenance_run.py` as "Cache in step". The orrery's
  `palomas_orrery_dashboard.py` has the matching button. Both patch
  scripts and the handoff are filed in `documentation/`.
- The gallery's offline maintenance run, on a throwaway copy of
  `1b077401` in the sandbox: **12 of 12 gating checkers passed.** Cache
  in step compared 4 objects and 34 named shells in both cache files.
  Config mirror check compared 17 links. Pointer join accounted for 70
  links against orrery `cf414139`. This is your baseline; re-run it
  before you change anything.
- The orrery's `ledger_index.py`: `OK: 330`. The highest handle in use
  is L-335, so the next free handle is L-336. Confirm before using it.
- NOT verified here: the orrery's maintenance run. The last handoff
  that ran it reports 16 of 16 at `6b282b2e`. Run it yourself for a
  baseline.

## 3. Facts the build rests on, measured at gallery `1b077401`

**Two files reach a visitor's browser, and they carry different
things.** `interactive.html` (3436 lines) fetches both
`data/solar-system/coverage_index.json` and `data/objects_config.json`
(near lines 2249 to 2253).

- The SHELLS and every word on them (name, description, about, note,
  source, link) are drawn from the cache, `coverage_index.json`. The
  cache builder copies them there from the config. So a change to a
  word reaches a visitor only after the cache builder has run.
- The ARRIVAL block is read straight from `objects_config.json`. The
  page hands that file's text to `sunApplyArrival` (line 2278).
  `coverage_index.json` and `feature_configs.json` contain no `arrival`
  key at all. So a change to which shells open drawn reaches a visitor
  as soon as the config is pushed, with no cache build.

The editor manifest's section 4 said the page reads the config
directly. That is half the picture, and the missing half is what broke
both live rooms on 2026-09-17.

**The arrival block as shipped** differs from the editor manifest's
plan. It is, for Earth:

    "arrival": { "_declared": "...", "drawn": ["crust"], "moon": false }

and for the Sun, `"drawn": ["photosphere"], "moon": false`. An optional
`min_half_range_au` is read by the page and used by neither room.

**`sunApplyArrival`** is lines 1718 to 1807 of `interactive.html`,
between `// ARRIVAL-START` and `// ARRIVAL-END` comment lines. It is
pure: no page elements, no Plotly. It has one caller, line 2278.
`documentation/smoke_arrival.js` tests it by cutting the text between
those two comment lines out of the page and running it in node. It
matches a trace to its shell by the END of the trace's legend group
name (body name, a colon, the shell's served name), because the traces
do not carry the shell's key.

**Where traces are built.** `gallery/feature_renderers.js` (1906
lines). `renderShellSet(slug, bodyName, featureKey, params, ...)` at
line 1351 already receives the shell's key as `featureKey`. Traces get
a `meta` object only when the shell has a link or a source (near lines
1260 to 1270). Legend groups are set at lines 446, 490, 1019, 1096 and
1620. The page loads its scripts at lines 127 to 132:
`feature_renderers.js`, `earth_geometry.js`, `nav_cluster.js`.

**The live check has a gap.** `gallery_maintenance_run.py --live`
compares eight served files with the working copy (`SERVED_FILES`,
line 254). The list does not include `data/objects_config.json` or
`gallery/nav_cluster.js`, and the browser fetches both. This is the
same fault as last session's lesson, that no check looked at the file
the browser reads, in a smaller place.

**The config** is 929 lines. `tools/mirror_constants.py` (689 lines)
holds the scanner the editor's writer must share: `Scanner`,
`parse_with_spans`, `render`, `member_separator`, `apply_changes`.

**The ledger.** Neither of the two L-334 texts written for it has been
applied: not the editor manifest's section 9, and not the last
handoff's. L-334's Gap line (near line 880) still reads "L-322 first;
then questions 2 to 5 in conversation".

**A stale sentence in a skill.** gallery-cache-builder 1.4, line 133,
calls the failed folder swap "one data point". It has now happened
three times.

---

## 4. Stage A -- the ledger patch (orrery repository)

One patch script against `LEDGER_CONSOLIDATED.md` at `cf414139`,
following safe-file-editing and the ledger block format in
ledger-and-session-records. You score RICE; the skill says how.

**On L-334**, above its Gap line, one note that merges the two
unapplied texts. It must say:

- Questions 2 to 5 were settled by Tony on 2026-09-17. The file is
  edited in place with the mirror's scanner, not dumped. A per-field
  line count plus a button that runs the offline checks. Tkinter from
  the Run button.
- Tony's arrival ruling, in his words: a room opens on "the surface
  shell plus frame elements like sun direction, axes, terminator", the
  Moon "with its box not selected". This supersedes the 0.25 AU Sun
  arrival of 2026-08-29 and the L-291 eight-shell Earth arrival.
- Piece 1 shipped as gallery `7c95435` with `59ba809`. Mode 5 on the
  phone, Tony: "yes, perfect. beautiful." No floor under the opening
  view; the view fits what is drawn.
- The contract is the editor manifest, amended by the handoff and by
  this document. Name all three files.
- New Gap: stages B and C of this document.

**New items.** Four, each its own block:

1. **The cache-in-step check and the fault behind it.** A config change
   was pushed ahead of the cache on 2026-09-17; the Sun's room lost 13
   shells and Earth's lost 10 on the live site while the run printed 11
   of 11, because no check read the file the browser reads. The check
   exists at gallery `1b077401` and passes there, and fails at
   `d2ca28b6` naming 36 differences. Open it and CLOSE it in the same
   patch, with the lesson: a config change is not deployed until the
   cache is rebuilt, and config and cache are committed together.
2. **A centre marker for bodies without shells.** Tony, at the phone
   check: the Sun's room has a "Sun" object at the centre and Earth's
   has none; "that might be a useful object to add for future solar
   system scenes without shells." OPEN.
3. **Logic that needs no browser lives in its own file.** Tony asked
   whether the page should be modularized. Claude's proposal: no
   general reorganisation; logic moves out of `interactive.html` when a
   build touches it, so a check can reach it. Record it as a PROPOSAL
   awaiting Tony's ruling, not as a rule. Stage B is its first
   instance.
4. **The live check does not cover every file the browser fetches**
   (section 3). OPEN; stage B closes it.

**A note on L-216**, the failed folder swap: third occurrence,
2026-09-17. Tony: "This is like the third time." He has suspended the
scheduled nightly run and builds by hand, pausing OneDrive syncing
first and watching GitHub Desktop's change list. Moving the
repositories out of OneDrive was raised and Tony's answer on
2026-09-17 was "not at this time". The skill's "one data point"
sentence is wrong and is owed a bump (stage C, piece 6).

**On L-322:** read its block before writing. The last handoff reports
the gallery half confirmed deployed (gallery `d2ca28b6`, cache rebuilt
at `9ff39cc4`). If the ledger does not say so yet, add a dated line
that does. The Earth slice remains open and is not part of this build.

**One ledger patch per pushed HEAD.** A ledger patch fingerprints the
file it edits. Do not cut a second one until Tony has pushed the first
and you have read the new HEAD.

**Done when:** the patch runs on a throwaway copy of `cf414139` and a
second run refuses; `ledger_index.py` run twice prints OK with the new
count both times, and you tell Tony that count.

---

## 5. Stage B -- the arrival tidy-up (gallery repository)

A visitor should see NO difference. That is the test.

1. **New file `gallery/arrival.js`.** It holds the arrival function,
   moved whole, attached to `window` the way `feature_renderers.js`
   attaches its own functions. The page loads it with a script tag
   after `feature_renderers.js`. The ARRIVAL-START to ARRIVAL-END block
   leaves `interactive.html`, replaced by a short comment saying where
   it went. Grep for every caller before and after; there should be
   exactly one.
2. **The renderers stamp each shell trace with its key.** In
   `feature_renderers.js`, every trace that belongs to a served shell
   carries `meta.shell_key`. Today `meta` exists only for shells with a
   link or a source, so the stamp must create it where it is absent and
   must not disturb `info_url`, `info_urls` or `source`, which the i
   panel reads. Trace the path from `featureKey` to each of the five
   places a legend group is set; do not assume all five are shell
   traces. Info markers made by `infoMarker` belong to a shell too.
3. **The arrival function matches on the key.** A trace whose
   `meta.shell_key` is in `drawn` is drawn. The Moon rule is unchanged.
   A trace with no key and a group other than "moon" is a frame element
   and is always drawn. Remove the end-of-name match; two ways of
   matching is how they come to disagree. Matching `drawn` entries by
   served NAME also goes, unless you find a config that uses it; the
   two shipped blocks use keys.
4. **`smoke_arrival.js` requires the new file** and stops cutting text
   out of the page. Its three deliberate breaks from last session must
   still fail it: a misspelled shell key, the Moon switched on, and a
   function that draws every shell. Add a fourth: a shell trace with
   its stamp removed must fail the check by name, because an unstamped
   shell would otherwise pass as a frame element and be drawn.
5. **`SERVED_FILES` gains** `gallery/arrival.js`,
   `gallery/nav_cluster.js` and `data/objects_config.json`.
6. **The cache.** The stamp is added by the renderer in the browser,
   not stored, so the cache should not change. Confirm with Cache in
   step rather than assuming.

**Done when:** the offline run is 12 of 12 on a throwaway copy; the
page's inline script still parses; the hover budget suite passes (the
interactive-exhibit skill notes it does not build the Sun room, so say
what it did and did not look at); the patch refuses a second run.
**Then it goes to Tony alone:** he runs the patch from the gallery
ROOT, moves it to `documentation/`, runs the maintenance run, commits,
pushes. You read the PUSHED tree for the patch's results, not for the
script's presence. After his push he runs the maintenance run with
`--live`, then opens both rooms on his phone. Stage C does not start
until he says both rooms look as they did.

---

## 6. Stage C -- the editor (gallery repository)

Pieces 2 to 6 of the editor manifest, section 5, with its section 6 as
the test list. Read both. What follows is only what has changed.

**Piece 2, the writer.** As written. It gains a third operation beside
"replace one string" and "replace one list of strings": replace one
true-or-false value, for the arrival block's `moon`. The refusal list
(`value`, `unit`, `figures`, `orrery_constant`) stands. Add `_declared`
and `_comment` to it: those are the file's own record of why a block
exists, and the editor's form does not offer them.

**Piece 3, the window.** As written, with the arrival panel now
concrete: one tick box per served shell, by key, and one for the Moon,
written to `drawn` and `moon`. `min_half_range_au` is not offered.

**Saving is not deploying, and the window must say so truthfully.**
This replaces the handoff's amendment 3 with what was measured in
section 3:

- After a save that changed any WORD, the window says, in plain
  sentences: these words are in the config; a visitor sees them after
  the cache builder has run; pause OneDrive syncing first; then run the
  checks, and commit the config and the cache together.
- After a save that changed only the ARRIVAL ticks, no cache build is
  needed. But do not make Tony learn two routines. The window gives the
  same instruction either way and adds one line saying the arrival
  change itself needs only the push.
- The window does NOT start the cache builder. The builder's folder
  swap fails under OneDrive (L-216) and Tony runs it by hand, watching
  the change list, for that reason. A button that starts it from inside
  another window hides exactly what he is watching for. This is the
  default; Tony may redirect it.

**Piece 4, the checks button.** As written. After a word save and
before the builder runs, "Cache in step" will be red, and that is
correct. Beside a red "Cache in step" the window says why and what
clears it. Every other red verdict is shown as the run printed it.

**Piece 5, the suite.** As written, plus: the true-or-false operation;
the two new refusals; and a save of arrival ticks followed by the
Arrival check passing on the saved file.

**Piece 6, records.** Module docstrings with Run-button instructions.
The gallery README's pipeline section gains the editor and
`gallery/arrival.js`. Two skill bumps, carried by ONE protocol entry
(v3.62), following the bump routine in ledger-and-session-records:

- interactive-exhibit 1.3 to 1.4: the arrival block; the key stamped on
  each trace; who may write the config (the mirror for numbers, the
  editor for words and arrival ticks, nobody by hand); and the rule
  from last session, that for anything a visitor sees, one check must
  read the file the browser fetches.
- gallery-cache-builder 1.4 to 1.5: a config change is not deployed
  until the cache is rebuilt, and the two are committed together; the
  "one data point" sentence corrected to three occurrences, with
  Tony's hand routine (pause syncing, watch the change list, stop if
  the commit does not form correctly) written down as the current
  practice.

A skill reinstall cannot be verified from inside the session that makes
it. Write the obligation into your handoff for the next session to
discharge, in the form the protocol gives.

**Pre-test.** Every delivered file goes through agentic-pre-test. The
editor is a Tkinter window, so the headless run under a virtual display
applies, on a THROWAWAY copy. The `SystemButtonFace` colour swap, if
needed, is made on the throwaway only.

**Done when:** every check in the editor manifest's section 6 has been
made to fail once on purpose and then passes; and Tony has edited one
real hover through the window, run the builder, pushed, and looked at
it on his phone.

---

## 7. Out of scope

- The Earth slice of L-322. It follows this build.
- Moving the repositories out of OneDrive. Tony, 2026-09-17: "not at
  this time."
- The centre marker (stage A item 2). Recorded, not built.
- Whether `data/solar-system/feature_configs.json` still has a reader.
  The last handoff found none. A question, not a finding; leave it.
- Everything the editor manifest's section 7 already excludes: the
  page-built hovers (L-331's residue), Jupiter's and Saturn's blocks
  (L-231), the static gallery's Studio.
- Colours and opacity in the editor. Not built unless Tony asks.

## 8. Rules of delivery, each one earned last session

- A patch is run from its repository's ROOT and filed in
  `documentation/` AFTER it has run. Filed first and run second, it
  stops with one line, writes nothing, and the push goes out without
  it. Say this to Tony each time, in those words.
- After every push, read the pushed tree for what the patch should have
  changed.
- Stamp your own files with your own model name. A stamp copied from a
  handoff carries the wrong model.
- ASCII and LF in every delivered file.
- If anything measured in section 3 has moved when you look, stop and
  say so before building on it.

## 9. Tony's decisions, and when they fall due

1. **(decide, stage A)** Whether "logic that needs no browser lives in
   its own file" becomes a rule. Stage B goes ahead either way.
2. **(look, after stage B)** Both rooms on the phone: same as before?
3. **(decide, stage C, only if he disagrees)** The editor does not
   start the cache builder.
4. **(look, end of stage C)** One real hover, edited through the
   window, seen on the phone.

## 10. Tony-action rollup

1. **(do)** File this manifest in the orrery's `documentation/`,
   commit, push. Give Opus this file and the new orrery SHA.
2. **(do)** At each stage: run the patch from the ROOT of the
   repository it names, move it to `documentation/`, run that
   repository's maintenance run, commit, push, report the SHA.
3. **(do)** Pause OneDrive syncing before every cache build.

---

Written September 17, 2026 with Anthropic's Claude Fable 5.1.
