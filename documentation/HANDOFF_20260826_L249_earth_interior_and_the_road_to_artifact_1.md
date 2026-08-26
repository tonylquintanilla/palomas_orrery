# HANDOFF -- 2026-08-26 -- L-249: Earth's interior gets one source each, and the road back to Artifact 1

**Orrery: `4fd02ddb41d4971d54b67e438ea8c72c4fc27b27` ->
`3faa72a0533850dccd056742470c788aad9b04e0`**
(https://github.com/tonylquintanilla/palomas_orrery, branch main).
**Gallery: `f4d4f9fde5a888bc308bcc8a626ca37509f4c592`, untouched all
session.** Both read from the live remote at the time of writing.
Confirmed HEAD moves, in order: `4fd02ddb`, `daf8c09c`, `c0555c55`,
`e858c235`, `fc25ef23`, `3faa72a0`.

**ONE PATCH WAS DELIVERED AND NOT RUN** when this was written:
`patch_L255_1_skill_bumps_and_protocol_entry.py`. At `3faa72a0` the two
skills still read 2.6 and 1.5 and the protocol still reads v3.43. Do not
assume it landed -- read the files.

**Type: BUILD.** Six patches, all orrery-side. No gallery work. The
Earth build did not start; what closed is the step that was holding it.

---

## What this session was about

It opened as "resolve the mantle question so step 2 can proceed" and
became the whole of L-249. Earth's four interior boundary radii were
approximate fractions taken by hand when the shells were first drawn in
2024. They now derive from sourced radii in `constants_new.py`, and the
hover prose interpolates the same constants, so the drawing and the
sentence beside it cannot disagree.

Three shells moved. Against a drawn radius of 6,378.1366 km:

| shell | was | now | delta |
|---|---|---|---|
| inner core | 1,211.8 | 1,221.5 | +9.7 |
| outer core | 3,508.0 | 3,480.0 | -28.0 |
| lower mantle | 5,421.4 | 5,711.0 | +289.6 |
| upper mantle | 6,250.6 | 6,346.6 | +96.0 |

Mode 5 confirmed twice: the shells, then the marker separation.

---

## What landed

| Patch | Result |
|---|---|
| `patch_L249_1_earth_interior_constants.py` | Ten names in `constants_new.py` -- four sourced primaries, `EARTH_MEAN_RADIUS_KM`, five derived |
| `patch_L249_1b_earth_interior_relation_tests.py` | Section 10 in `test_constants_provenance.py`, six relation tests, suite 15 -> 21 |
| `patch_L253_1_d660_note_strip_and_breadcrumb.py` | Two unsupported figures removed from `EARTH_D660_DEPTH_KM`; L-253 opened to hold them |
| `patch_L249_2_earth_shell_wiring.py` | Earth joins the Phase C4 reference pattern; four `radius_fraction` and four hover/tooltip pairs wired to the constants |
| `patch_L249_3_crust_marker_separation.py` | `build_sphere_shell()` gains `info_polar_deg`; Earth's crust steps 10 degrees |
| `patch_L254_1_dead_builder_markers.py` | Earth's eight dead sphere-shell builders marked; L-254 opened with the census |
| `patch_L255_1_skill_bumps_and_protocol_entry.py` | **DELIVERED, NOT RUN.** Two skill bumps and the protocol version entry |

Tier-1 findings 292 -> 291. The five new primaries appear in
`PROVENANCE_AUDIT.md` as *cited, not independently cross-checked*, which
is correct: they are in the worksheet corpus and pick up their
cross-check legs through the ordinary dispatch loop rather than needing
a special errand.

---

## Tony's rulings

**The fractions were approximate, not declared.** "When I first drew
these shells I took approximate radius fractions not exact. With better
provenance we can use the same constant to calculate the radius fraction
as the hovertext." That settled the mantle question and answered L-240
for the whole Earth interior block: every value in it is a measurement,
none is a declared drawing choice.

**One value, one home -- and it is general.** `constants_new.py` is the
only store for a numeric value, in prose as much as in code. Confirmed
with its scope boundary in the same exchange: measured values migrate,
declared drawing parameters (`n_points`, `marker_size`,
`info_polar_deg`) do not, and the rule is forward-going on files touched
rather than a repo-wide sweep opened on the day.

**Significant figures.** Compute at full precision; report to the
figures the least precise input supports. A subtraction is governed by
decimal places.

**Do not add unsourced numbers.** Ruled against three crustal-thickness
ranges that had been proposed for the upper mantle hover. "The goal of
the artifact is complete provenance before we move to the next
artifact."

**The breadcrumb goes in the ledger, not the code.** Keep an unsourced
figure pending sourcing rather than lose it -- but out of
`constants_new.py`, where a reference within the scanner's lookback
would read as a citation for the value beside it.

**Ten degrees, and move the crust.** On the marker collision: rotate the
crust's cross, "because that is the odd layer visually." The standing
rule would have moved it too, being the outer of the pair.

**Dead code: annotate now, sweep later.**

---

## The two defects found in this session's own work

Recorded because both are the class this protocol exists to catch, and
both were found before delivery rather than after.

**A reference true of a constant and false of the note beneath it.**
`EARTH_D660_DEPTH_KM` was written with a `# Ref:` to Ishii et al.
(2019), Nature Geoscience 12:869-872. That reference is real, correctly
transcribed, and supports the 660 km depth. It supports NEITHER figure
in the `# Note:` under it -- the +/-60 km lateral variation came from a
review paper that was never cited, and the 750 km depression came from a
different Ishii paper, the 2022 Nature one. Ishii 2019 is about the
transition's SHARPNESS. The citation passed every check while asserting
a provenance that did not exist, and it was written two messages after
Claude quoted that rule at Tony. Repaired by `patch_L253_1`.

**A region check that examined nothing.** `patch_L249_2`'s
stale-literal post-condition sliced the Earth block as
`c_text[index("'Earth': {") : index("'crust': {")]`. The second index
has no start position, so it returns MERCURY's crust, earlier in the
file, and the slice came out empty. The check reported pass having
looked at zero characters. Caught only because a second post-condition
failed for an unrelated reason. It now searches from the block's start,
refuses an empty slice, and prints how many characters it examined.

A third, smaller: a post-condition asserting `'60 km'` was gone fired on
the clean base, because `60 km` is a substring of the legitimate
`660 km`. That one caught itself, which is the good failure.

---

## What the post-conditions found that a reading would not have

`patch_L249_2`'s stale-literal check found a **fourth store per value**.
Each dead `create_earth_*_shell` builder holds its own `<br>` copy of
the prose in `layer_info['description']`, so Earth's boundary figures
lived in four places, not three. All four are now on the reference
pattern.

That led to the L-254 census, measured at `fc25ef23`: **82
`create_*_shell` functions across 15 modules, 6 live, 76 dead.** The six
live ones are all reached through a `CUSTOM_SHELLS` `'builder'` string
resolved at `planet_visualization.py` line 440 by `rsplit` plus
`getattr` -- the four magnetospheres, Earth's LEO, Earth's
geostationary belt. That is the only dynamic call route in the codebase,
which is what makes the number safe to state. Per module: earth 8, solar
14, mars 7, jupiter 6, moon 6, pluto 6, saturn 6, venus 6, eris 5,
neptune 5, uranus 5, planet9 2.

---

## Ledger

**Opened:** L-253 (the 660's depth variation, held unsourced), L-254 (76
dead sphere-shell builders), L-255 (this session's skill bumps -- handle
reserved by `patch_L255_1`; the row itself is NOT yet written).
**Effectively closed but not yet marked:** L-249. Every part of its
shape is built. Its status line still reads OPEN and its Gap still says
"blocked on `patch_L248_1`", which landed the night before -- a stale
Gap that was noticed at session start and never repaired.

---

## Corrections to this session's own claims

- **"The cores move about 8 km each."** The outer core moves 28 km
  inward. The 8 came from the hover prose's rounded 3,500; PREM's
  core-mantle boundary is 3,480.
- **Three of four fractions given to four significant figures too many.**
  `0.1915138`, `0.5456150`, `0.8953994` were hand arithmetic and wrong in
  the 6th-7th digit. Then corrected again: the honest forms are
  `0.19151`, `0.5456`, `0.8954`, because the inputs never supported ten
  digits.
- **"The choice is Phase C4 or hand-syncing the tooltip."** There was a
  third option, and it was the important one: two strings that both
  interpolate the same constant cannot disagree numerically. The one-store
  rule never required the restructure. Phase C4 was still right, for the
  smaller reason that it makes the edits simpler and closes Earth's slice
  of L-191.
- **`Role: rendering/shells`** in a patch anchor. The file says
  `Role: rendering`. Recalled, not read; the anchor check caught it in
  the sandbox.

---

## Skills and protocol

Loaded and matched at session start: `safe-file-editing` 1.8,
`provenance-discipline` 2.6, `ledger-and-session-records` 1.9,
`orrery-coding-conventions` 1.5.

**CARRIED OBLIGATION.** `patch_L255_1` takes `provenance-discipline` to
2.7 and `orrery-coding-conventions` to 1.6. A reinstall cannot be
verified from inside the session that makes it, so:

> **The next session confirms its loaded copies read
> `provenance-discipline` 2.7 and `orrery-coding-conventions` 1.6
> before doing provenance or marker work.**

The protocol goes v3.43 -> v3.44 in the same patch, and v3.41 moves down
into `PROJECT_INSTRUCTIONS_HISTORY.md` PART 1. The UI copy was at v3.43
as of this session and will need re-uploading at v3.44.

---

## (do) and (decide) -- Tony-side

- **(do)** Run `patch_L255_1_skill_bumps_and_protocol_entry.py` from the
  repo root. Then, in order: `skills_index.py PROJECT_INSTRUCTIONS.md`,
  reinstall both skills in Settings > Skills, `maintenance_run.py`,
  re-upload `PROJECT_INSTRUCTIONS.md` at v3.44.
- **(do)** Archive this session's patch scripts to `documentation/`.
- **(decide)** RICE for L-253 (2/2/60/2) and L-254 (3/3/95/3).
- **(decide)** L-254's sweep shape: do the remaining 68 dead builders get
  deleted, archived as modules, or annotated in place? And do the unused
  imports at `planet_visualization.py` lines 129-139 go with them?
- **(decide)** Whether L-249 closes now. Its build is done; only the
  status line and the stale Gap remain.
- **(open)** The nightly's `[RECOVER] could not remove retained
  data\solar-system.prev (WinError 5)` quarantine. Carried from the
  previous handoff, untouched again.
- **(open, carried)** From the previous handoff and still unaddressed:
  the `REQUEST_<batch>.md` classification question, and whether a row's
  prose RICE score should exist at all given the index computes it.

---

## Next session -- the goal is Artifact 1 on the host

**First three cheap things, in this order.**

1. SHA round trip: orrery `3faa72a0` or later, gallery `f4d4f9fd`, both
   read live. One patch was queued when this was written, so expect the
   orrery HEAD to be ahead.
2. Confirm the loaded skill versions against the manifest -- and
   discharge the carried obligation above before any provenance or marker
   work.
3. Read L-235, L-237 and L-238 before proposing anything. This is the
   first gallery work in several sessions and those three rows are the
   whole of what stands in front of the Earth build.

**Then the path, which has not changed shape.** Steps 1 and 2 closed
this session.

1. ~~`patch_L248_1`, the constants-change gate~~ -- DONE, previous session.
2. ~~L-249, the Earth slice of L-181~~ -- DONE this session.
3. **L-235's T5 fix with L-237's golden re-cut.** Gallery-side.
   Independent of everything above.
4. **L-238, the `radius_fraction > 1.0` validator.** Gallery-side. It
   blocks the Earth build directly: the validator refuses any shell above
   the surface, and Earth has four of them (atmosphere 1.05, upper
   atmosphere 1.25, and the belts).
5. **Earth's config entries and the interior shell rendering.** The
   first step that consumes what this session built.
6. **The magnetosphere** -- a design pass, not a port.
7. **Mode 5, then re-lock.** Golden fingerprint `abbd01094852b57f` is
   stale and gets re-cut at step 3.

**Steps 3 and 4 are gallery-side and independent, and they are the
natural opening.** Neither depends on tonight's work; both are on the
critical path to a local render of Artifact 1.

**What tonight bought for that render.** When Earth's interior reaches
the assembler, every value it serves has exactly one source. L-232 says
the gallery's served constants currently carry sources that nothing
checks -- the orrery side of that is now clean for this body, which
means the served values can be traced back rather than re-derived.

---

*Session written August 26, 2026 with Anthropic's Claude Opus 5. Orrery
`4fd02ddb41d4971d54b67e438ea8c72c4fc27b27` to
`3faa72a0533850dccd056742470c788aad9b04e0`; gallery
`f4d4f9fde5a888bc308bcc8a626ca37509f4c592`, untouched. Both confirmed
against the live remote. One patch, `patch_L255_1`, was delivered and
unrun at the time of writing.*
