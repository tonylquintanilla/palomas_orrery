# HANDOFF -- 2026-08-30: the Sun exhibit's GUI shape, and what a
# report owes its reader

**Built on** orrery `70f12a7b5c260288c0fc1a135f45e547651c5d9f` at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
gallery `80759493dd03f7005eb9c4baae6448756893f884` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both confirmed against the live remote at session start.

**Type:** DESIGN. No production file was changed. Everything below is a
decision, a study, or a patch waiting to be run.

**Companion to** `documentation/HANDOFF_20260829_night_sun_finished.md`,
which set up this session's opening item. Not superseded; corrected in
one place (see L-262 below).

---

## What was decided

**The gallery grows toward the orrery.** Tony's ruling: "The gallery is
meant to produce the orrery to allow the user to assemble their own
scene. The question is the gui shape." Free object selection is
permanent. A boundary-ladder control was designed, prototyped and
withdrawn because it took that away -- it suited the Sun exhibit, where
every feature nests, and would have broken the moment orbits arrived.

**Four parts, no two doing the same job.** Cross markers carry identity,
radius and citation, and tapping one moves the camera. The i panel
carries descriptive material and the link out. The drawer is what is in
the scene -- a free multi-select list. The focus label is one thing,
where the camera is, and the handle that opens the drawer.

**One job per control.** The box draws; everything else on a row moves
the camera. Nothing does both. This also settled, by consequence, that
focusing no longer switches on a hidden shell.

**The i panel carries links, not curated prose** (L-265). The eighteen
`*_info` strings exist and work, and cannot ship: a live scanner run
returns 6 Tier-1 and 29 Tier-2 for `solar_visualization_shells.py`, the
info strings being the Tier-2 rows, and Tony's account of their origin
is that he wrote them largely with Gemini. Sending them to the gallery
means sending hundreds of numeric claims across the export gate to a
repo with no checker.

**A report has to be complete enough to act on where it lands.** Tony's
ruling, and the reason is the load-bearing part: "I can't go grep the
code for all the instances that built a count." A count only works for a
reader who can go find out what. Claude resets; Tony cannot read
everything. Neither can go looking.

---

## What was built

All four are in `/mnt/user-data/outputs` from this session and need
placing.

**`sun_gui_mockup.html`** -- a throwaway study, not a deliverable. Runs
real Plotly with radii, colours, opacities, point counts and sources
generated from `objects_config.json` rather than retyped, reusing the
live page's sphere geometry, hover format and framing rules. Tony ran a
written Mode 5 protocol against it over two rounds. All pass/fail checks
pass.

**`TEST_PROTOCOL_sun_gui_mockup.md`** -- the Mode 5 protocol, with each
check naming what would make it fail, and a section stating what the
study does not cover.

**`patch_L265_info_url_placeholder.py`** -- adds `info_url` to 20 named
features and an `info_urls` array to Earth's belt block. 22 links, all
`https://www.nasa.gov/`. Fingerprint-guarded, `.bak` written, refuses a
second run, proves structurally that nothing but the 22 keys changed.
Tested on a throwaway copy of the repo. **Not yet run against the real
file.**

**`sweep_collapsed_features.py`** -- discovery for L-268. Run at
gallery `80759493`: 20 stored as themselves, 16 collapsed, 0
unclassified.

**`LEDGER_ENTRIES_20260830.md`** -- L-265 through L-268 in house format
with index rows, plus an amendment to L-262. Handles verified free.

---

## Four defects found, and what each one teaches

**One. The L-262 diagnosis in last night's handoff is wrong.**
`smoke_framing.js` was never about `interactive.html`. It takes the page
path as an argument, and its markers live in
`gallery/solar_system_earth_test2.html`; the runner points it at the
wrong page and it reads its payload file from the wrong folder. Run
against the right page it passes all twelve checks -- verified this
session. Two one-line fixes, neither touching a live page. **This voids
the bundling argument** that L-262 should ride along with the portrait
work to save a Mode 5. It needs no Mode 5 at all.

A residual gap the fix does not close: once pointed correctly the test
guards a test page. `sunRefitFrame` in `interactive.html` still has no
test, and the GUI work adds framing logic to exactly that file.

**Two. A framing floor that would have followed us into the build.**
The study inherited `SUN_HALF_RANGE_AU` (0.25 AU) as a floor on the
frame. Fifteen of the eighteen shells are smaller than that, so framing
on the core, the radiative zone or the chromosphere all produced the
identical cube and adding any of them changed nothing on screen. The
floor is correct on the live page, where the frame only ever widens from
a fixed arrival view. It is wrong the moment the frame follows a chosen
object.

**Three. The sweep failed Tony's own rule within a minute of it
existing.** Jupiter's three belts printed as `radiation_belts[0..2]` --
the ignorable form. Their names exist in `BELT_STYLE` in the renderer;
the table-finder matched `name:` and missed `names:`. It reported them
as UNNAMED ANYWHERE rather than labelling them by index quietly, which
is the only reason the gap was visible.

**Four. Two of the eighteen info strings carry live constants.**
`outer_corona_info` and `alfven_surface_info` interpolate from
`constants_new.py` at render time. The study's hand copy froze them to
the literal text "(computed)" -- a shadow constant forming in real time,
and the clearest single argument for the cross-repo transport.

---

## Open, and carried

**The hang is not diagnosed.** Tony, Mode 5: hover text latches and the
display seizes when a cross marker and then the i button are used in
sequence. A headless browser confirmed Plotly's gl3d hover hit-tests by
reading pixels off the GPU on every mouse move -- "GPU stall due to
ReadPixels" in the console, across 8,119 points, and that is on the live
page's code path too. **The exact sequence could not be reproduced:**
synthetic mouse events do not reach Plotly's 3D hover machinery. The
applied fix -- clear the tooltip and set `hovermode: false` while the
panel is open -- is reasoned from mechanism, not witnessed. **Tony-action
(do):** say whether it cures the seize. If not, the next move is taking
the panel off the canvas rather than overlaying it.

**L-268's order, recommended and not yet ruled.** The braid: Earth's two
belts on Earth's rung, the other fourteen recorded. Reason it is not
mere deference -- Jupiter's and Saturn's features are served but drawn
by no exhibit, so converting them now would rest on code reading rather
than a render. Two conditions, or the braid version degrades: the
renderer falls back to the old shape with the fallback marked temporary
and naming L-268, and the sweep runs in
`gallery_maintenance_run.py` printing names. The counter-argument
stands: if those exhibits never come, the fallback lives forever and the
sweep never reads zero.

**There is no skill for the maintenance runner.** Checked across all ten
on 2026-08-30: the word appears once, in passing. Five rulings on runner
reporting are closed in the ledger and written nowhere that loads --
L-188 (built it), L-197 (say what passed), L-205 (verdict lines carry
evidence), L-212 (name every file written), L-236 (two moments, three
states). Three were wanted this session and unavailable, which is why
the sweep printed a count.

The question is not whether the rules are good. It is where they go, and
this session worked out that the answer depends on which reader:

- A runner header serves Tony -- he is inside the file when he writes a
  check, and reads the conventions in place. It does not serve Claude,
  who will not think to open that file.
- A skill serves Claude -- it loads whether or not anyone goes looking.
  It does not serve Tony, who does not read skills; he writes rules into
  them.

**Proposed, not decided:** the runner-specific conventions live in a
skill, and the runner header carries a one-sentence pointer rather than
a copy. A pointer that goes stale is visible; a diverged copy is not,
which is L-236's own lesson. **Tony-action (decide).**

The cost is real and should be weighed rather than waved past. A fifth
store under the stale-skill gate, firing rarely, for a rule set that may
be small enough not to earn it.

---

## A PROTOCOL AMENDMENT, confirmed 2026-08-30

**A REPORT NAMES ITS ITEMS.** Tony's ruling. This is NOT a runner
convention and does not belong in a skill: its grounds are the two
readers, and the two readers are what the protocol is for.

A count only serves a reader who can go and find out WHAT. Neither
reader here can. Claude resets every session and will not think to open
the file. Tony cannot read everything and does not grep. So a report has
to be complete enough to act on where it lands.

The names also carry the SHAPE of the work, which a number cannot. "16"
is a size. "D Ring, C Ring, B Ring, A Ring, F Ring, G Ring, E Ring" says
it is the whole of one body's ring system, one kind of thing, mechanical
rather than seven separate judgments.

**And a count can be identical across a real change, which makes a
count-based report a check that cannot fail.** This is why the rule is a
protocol amendment and not a style preference. It belongs beside A Check
That Cannot Fail Is Not Passing -- arguably as a fourth move alongside
make success carry evidence, make the blind spot announce, and put the
check where it runs.

**Three instances, measured this session, spanning the range.**

*Done right -- `MODULE_ATLAS.md`.* "Undetermined role (4)" followed
immediately by the four filenames. Count and names together, names doing
the work. Whoever wrote it had already reached this rule; it is the
worked example.

*The pure failure -- the scanner's terminal summary.* It prints "292
TIER-1 FINDINGS IN THE SCANNED TREE", then explains at length that this
is not the gate, that the gate is Tier-1 = 0 on the active build path,
and that the line does not compute that subset. So the number a reader
needs is absent, the number present is the wrong one, and the
instruction is to go read another document.

*The interesting middle -- `PROVENANCE_AUDIT.md`.* It names the file and
the line, which is far better than a count. But the thing is called
"display string @ line 936". That is a coordinate, not a name; it is
`hover_text_sun_and_corona`. A session had to open the file at that line
to find out, which is exactly the lookup Tony cannot perform.

**A hole underneath the middle case, and it is the strongest evidence.**
The audit reports "No file's Tier-1 count rose," and the run history
tracks T1 as one number per run -- 292 across six runs. Both are count
deltas. Clear one Tier-1 finding and introduce another in the same file
and both report nothing changed. A names-based delta would say what was
cleared and what appeared.

**Tony-action (decide):** the wording and where it sits in Part 3, and
whether the second-level review is the ledger skill, as Tony proposed --
ledger items reviewed for the same property as they are touched.

**Scope note.** Fixing the scanner's summary and the audit's unit names
is real work and is NOT proposed here. The amendment states the
principle; remediation goes in slices, per the braid, and gets its own
handle when someone takes it up.

**A dead-link check does not exist** (L-266). The orrery already carries
roughly 470 URLs, each a provenance claim, and nothing asks whether any
still resolves. L-265 makes it load-bearing rather than merely useful.
Three shapes proposed, none chosen; **Tony-action (decide)** before any
of it is built. Note the trap: every placeholder resolves perfectly
well, so "is it dead" passes all 22.

**Unchanged from last night:** L-260's portrait defect is still live on
the public page -- this session designed the fix rather than shipping
it. L-257's three enforcement builds, the rendering ladder still absent
from the master plan, L-237, and segment 2.

---

## Tony-action list

- **(do)** Run `patch_L265_info_url_placeholder.py` from the gallery
  repo root.
- **(do)** Place `LEDGER_ENTRIES_20260830.md` into
  `LEDGER_CONSOLIDATED.md` and re-run `ledger_index.py`. RICE numbers
  are proposed, not confirmed.
- **(do)** Replace all 22 placeholder links with curated selections.
- **(do)** Say whether the `hovermode: false` fix cures the seize.
- **(decide)** L-268's order: the braid, or all sixteen with a harness.
- **(decide)** Where the runner conventions live.
- **(decide)** The protocol amendment's wording and placement, and
  whether the ledger skill carries the second-level review.
- **(decide)** Which shape the dead-link check takes.

---

## What a next session should confirm first

Both repos' HEADs against the anchors above. Then, before any patch
work, that its loaded `safe-file-editing` reads 1.9 and its
`provenance-discipline` reads 2.10 -- both were confirmed in this
session and both checks are load-triggered, so they do not carry.

*Session written August 30, 2026 with Anthropic's Claude Opus 5. Built
on orrery `70f12a7b`, gallery `80759493`; both confirmed against the
live remote at session start. No production file was modified.*
