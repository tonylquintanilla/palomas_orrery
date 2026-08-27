# HANDOFF -- 2026-08-27 -- The suite goes green, the validator admits interiors, and the rendering ladder gets written

**Orrery: `6ceb3f76c665a678d34a623aa47cb1cc0b427574`, unchanged all
session** (https://github.com/tonylquintanilla/palomas_orrery, branch
main). **Gallery: `f4d4f9fde5a888bc308bcc8a626ca37509f4c592` ->
`1a67b00d73813a1387ff1de7b77f8175c39c0f1e`.** Both read from the live
remote at the time of writing. Confirmed gallery HEAD moves, in order:
`f4d4f9fd`, `0cabfb3b`, `5410177`, `1a67b00d`.

**ONE PATCH WAS DELIVERED AND NOT RUN** when this was written:
`patch_L257_1_rendering_ladder.py`, which writes the rendering ladder
into both planning documents. At `6ceb3f76` neither document carries it.
Do not assume it landed -- read the files.

**Type: BUILD plus DESIGN.** Two gallery patches landed and were proven.
One planning patch is queued. The Earth render did not start.

---

## What this session was about

It opened on the L-238 validator, the item the previous handoff named as
the direct blocker on the Earth build. That closed in one small patch.
Running its test then exposed that the gallery's offline suite had not
completed since the Sun landed on 2026-08-25, which took a second patch.
The rest of the evening was a design conversation that produced a
document neither planning file had: what the gallery actually SHOWS, and
in what order.

---

## What landed

| Patch | Result |
|---|---|
| `patch_L238_1_interior_shell_invariant.py` | `_validate_feature_shapes` relaxed from `radius_fraction > 1.0` to `> 0.0`; two regression checks added where the branch had none. Committed at gallery `0cabfb3b`. |
| `patch_L256_1_offline_suite_sun_expectations.py` | Four failures repaired, all test-side. Suite now **PASS (149 checks, 0 failures)**. Committed at gallery `5410177`. |
| (no script) | `data/solar-system.prev_old/objects_config.json` untracked and deleted; `.gitignore` widened to `data/solar-system.prev*/`. Committed at gallery `1a67b00d`. |
| `patch_L257_1_rendering_ladder.py` | **DELIVERED, NOT RUN.** Section 5a-bis into the master plan, a closing section into the critical path summary. |

---

## L-238 -- the validator that refused every interior shell

The builder asserted `radius_fraction > 1.0`, which reads "the shell is
above the surface." True of every shell served so far, false of every
interior shell in the orrery. Earth's inner core is 0.19 of the surface
radius, so the four boundaries closed on 2026-08-26 could not have been
served at all.

Relaxed to `> 0.0`, which still refuses a missing key arriving as 0 and
a sign error. No ceiling added -- the Sun's outer shells run to
thousands of solar radii. The branch had NO test before this; it now has
one in each direction, and the ABORT half is the load-bearing one.

---

## L-256 -- the suite that had not run to the end since the Sun landed

Running L-238's tests surfaced this. Measured on an UNPATCHED tree at
`f4d4f9fd`: the suite printed 135 lines and then died on an uncaught
`KeyError`, not a check failure. Twelve checks after that point had not
executed since 2026-08-25.

Four failures, all in the test file. The builder was correct in every
case.

- Two hand-built fixtures construct an object dict with no
  `canonical_frame`, a key `assert_structural` began reading when L-234
  landed the Sun. **The second fixture had never executed at all**, so
  it never got the chance to crash.
- `12 objects served` was a hardcoded literal; the config holds 13.
  Replaced by a count derived from the loaded config, which tests the
  stronger thing and cannot go stale again. **This is the one change in
  the set that alters what a check MEANS**, and it was ruled before the
  patch was written.
- The M2 trust loop demanded `two_body_rate_v1` from every object but
  Voyager. `features_only_result()` deliberately serves
  `not_applicable` with a null window for a frame origin, and says why.
  The loop gained a third branch keyed on `canonical_frame ==
  FEATURES_ONLY_FRAME` rather than on the slug, so it holds for any
  future frame origin.

**Sizing method worth repeating.** Before proposing anything, the
fixture key alone was applied to a THROWAWAY copy and the suite run to
completion. That established there was nothing else behind the crash:
149 checks, the same three failures, no new ones. A repair cannot be
sized while a third of the suite has never executed.

---

## Tony's rulings

**Provenance binds at SERVING, not at drawing.** "We should not serve to
the interactive gallery incompletely sourced renders." This EXTENDS the
existing "governs what may be LOCKED, not what may be BUILT" line rather
than replacing it. Drawing locally gates nothing; publishing does,
because a visitor takes what the site shows as true.

**The golden fingerprint rides in step, not as a prep that blocks.** "I
have no objection as long as this is also done in step and not as a prep
that blocks." Consequence: the seven golden artifacts stop being a
parallel track and fold into the steps that render their bodies.

**The rendering ladder, seventeen steps, explicitly provisional.** "Along
these lines, not a final ruling. We should revisit the scheme at each
major junction." Full table in the queued patch. Step 3 is a GUI
conversation placed deliberately AFTER two renders: look first, then
design the controls.

**Commit L-238 over a red suite rather than hold it.** The red predated
the patch and belonged to a different thing; coupling them would have
been the shape the braid rules against.

**Do not patch the 2026-08-26 handoff's Tier-1 count.** The correction
is carried here instead: the count ended the previous session at **292,
not 291**. The constants work took it to 291 and `patch_L249_3` returned
it to 292. The added finding is a NEW sentence in
`orrery_rendering.py`'s module docstring carrying a 10% threshold, not a
re-partition of existing prose -- verified by deleting that one
paragraph and re-running the scanner, which returns 291.

---

## The Sun is not as complete as we believed

The ladder's step 1 renders the Sun "as is" on the understanding that
render, provenance AND golden artifact were all done for it. Measured at
orrery `6ceb3f76` and gallery `1a67b00d`, one of the three holds.

**Render: COMPLETE.** 19 shells, Mode 5 passed 2026-08-24 and 25.

**Provenance: NOT complete, and the gap is in the prose.** The constants
are largely in order -- `SUN_RADIUS_KM`, `HELIOPAUSE_RADII`,
`GRAVITATIONAL_INFLUENCE_AU`, `ALFVEN_SURFACE_RADII`,
`ROCHE_LIMIT_RADII` all named and sourced; the chromosphere derives from
`CHROMOSPHERE_PHYSICAL_KM`. But `solar_visualization_shells.py` carries
SIX Tier-1 findings, every one a public-facing display string, holding
42 uncited claims between them. The constants were sourced and the hover
text describing them was not -- "The Correction Does Not Travel" exactly.
The Sun's pole RA and declination also sit in `idealized_orbits.py`
rather than the store.

**Golden artifact: DOES NOT EXIST.** The harness folder holds one file
and it is `artifact_1_earth_alone.json`.

**Step 1's slice is countable.** The Sun's served features carry 111
numeric values. 85 are declared drawing parameters; 26 sites are
measured, holding **19 distinct values**. Five of the nineteen appear at
more than one site -- 13 sites for 5 values -- which is L-244's
singularity class arriving in the SERVED data.

---

## Two findings about the golden machinery

**It has never compared anything.** T5 fingerprints today's assembly and
compares it to itself, so it has printed OK every run since July without
opening the stored file. The HTML instance is a hardcoded caption.

**And a working one could not have stayed green for a day.** `compare()`
matches every field but `position_samples` exactly, including
`cache_snapshot_id` -- a timestamp the nightly rewrites each run -- and
`coordinate_bounds`, which moves whenever the nightly refreshes Earth's
elements. Three of fourteen fields are guaranteed to differ after any
build.

**Ruled, deferred:** extend the existing 0.001 tolerance to
`coordinate_bounds`, or state a separate one. One line.

**Artifact 1's T3 is ALSO already failing** at `1a67b00d`, unrecorded
anywhere. It expects Earth's two feature families and now gets eight,
because the Sun is the scene's centre and brings its six. That is the
part-by-part consequence predicted on 2026-08-25, arriving for real.
Measured `compare(stored, live)` directly: exactly four differences,
`cache_snapshot_id`, `feature_keys`, `coordinate_bounds`, `warnings`.
L-237's list was right. `position_samples` is absorbed by tolerance.

L-235 and L-237 are PARKED by agreement -- the machinery needs the
invariant/context split before the pair is worth doing.

---

## The measurement that reframes the remaining distance

**`interactive.html` renders nothing from the served cache.** Zero
references to `coverage_index.json`, `feature_configs.json` or
`data/solar-system`. Its orbits are eight sets of Keplerian elements
hardcoded in the HTML -- the Phase 0 demonstration of July 6, frozen on
the A path by design. The nightly build reaches no visitor.

**But the assembler HAS run in a browser.**
`gallery/solar_system_earth_test.html` and `..._test2.html` load it into
Pyodide, fetch the coverage index and `objects_config.json`, assemble and
render. Their headers call them throwaway dev pages requiring local
HTTP.

So the first step is not "build a rendering system." It is closer to
"promote a working dev page to a reachable exhibit, and give it
something worth showing."

---

## Corrections to this session's own claims

- **"The two new L-238 checks sit past the crash point."** They do not.
  Both ran and passed in the first suite run. The count of checks after
  the crash line was measured; the assumption that mine were among them
  was not.
- **"135 ok lines."** That figure counted ok AND FAIL lines together.
  Three FAILs were present in the baseline and were not reported,
  because the grep was for a line count and never looked for the word
  FAIL.
- **"138 -> 140 checks."** Carried from the previous handoff rather than
  measured, and the suite could not reach 138 anyway. Real total: 149.
- **The 292 diagnosis.** The first account blamed a scanner unit
  boundary moving under inserted lines and said no new prose was
  involved. Both halves wrong; corrected by experiment.
- **A post-condition asserting the fixture key would appear twice**
  found three. A pre-existing `'canonical_frame': 'heliocentric'` sits
  at line 294 in an unrelated literal. Tightened to count the fixture
  shape. The patch refused to write until it was right.
- **Scope.** A confirmed one-line handoff correction was delivered as a
  five-edit patch, then followed by two design questions stacked at the
  end of a long evening. Tony stopped it. The patch was withdrawn
  unrun.

---

## Ledger

**Opened:** L-256 (the offline suite's Sun expectations -- BUILT and
committed this session), L-257 (the rendering ladder -- patch queued).
**Needs a row:** the `compare()` tolerance asymmetry, ruled and
deferred. Artifact 1's failing T3, currently recorded nowhere.
**Parked by agreement:** L-235, L-237.
**Still open from the previous handoff:** L-249's status line and stale
Gap; L-253 and L-254 RICE (rows exist, scored 1.2 and 2.8); L-254's
sweep shape; the `REQUEST_<batch>.md` classification question.

---

## Skills and protocol

Loaded and matched at session start: `provenance-discipline` 2.7,
`orrery-coding-conventions` 1.6, `safe-file-editing` 1.8,
`ledger-and-session-records` 1.9, plus `gallery-assembler` and
`gallery-cache-builder`. **The previous session's carried obligation is
DISCHARGED** -- both bumped skills load at their manifest versions.

No skill or protocol version changed this session.

---

## (do) and (decide) -- Tony-side

- **(do)** Run `patch_L257_1_rendering_ladder.py` from the ORRERY repo
  root, review the two new sections, and commit.
- **(do)** Archive this session's three patch scripts to
  `documentation/`.
- **(decide)** When the Sun's nineteen values close -- at step 1,
  alongside step 2, or at step 3 when the exhibit takes shape. Step 1
  renders "as is" and only step 2 says "complete with provenance."
- **(decide)** Whether the `compare()` tolerance fix and Artifact 1's
  failing T3 get their own handles or ride on L-235.
- **(open)** The nightly's `.prev` lock. It self-healed this session by
  quarantining, which is the designed fallback working. Quarantine
  folders are gitignored and accumulate on disk; worth a sweep.

---

## Next session -- the goal is the Sun on screen

**First three cheap things, in this order.**

1. SHA round trip: orrery `6ceb3f76` or later, gallery `1a67b00d` or
   later, both read live. One orrery patch was queued when this was
   written, so expect the orrery HEAD to be ahead.
2. Confirm loaded skill versions against the manifest. Nothing was
   bumped this session, so this should be quiet.
3. Read Section 5a-bis of the master plan before proposing anything. The
   ladder is the sequencing authority now, and it is provisional by
   ruling -- revisit at each junction.

**Then step 1: render the Sun and look.** Everything it needs is served.
The work is the page, not the data. The two dev pages already do the
hard part; what does not exist is a reachable exhibit.

Two things to settle in the same breath, because they are the first
junction: whether the Sun's nineteen values close before or after that
first look, and what the page is for.

*Session written August 27, 2026 with Anthropic's Claude Opus 5. Orrery
`6ceb3f76c665a678d34a623aa47cb1cc0b427574`, unchanged; gallery
`f4d4f9fde5a888bc308bcc8a626ca37509f4c592` to
`1a67b00d73813a1387ff1de7b77f8175c39c0f1e`. Both confirmed against the
live remote. One patch, `patch_L257_1_rendering_ladder.py`, was
delivered and unrun at the time of writing.*
