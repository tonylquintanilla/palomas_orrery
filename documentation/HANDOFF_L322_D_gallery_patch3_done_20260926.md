# Handoff -- L-322 Stage D: gallery patch 3 done; how exact rows print is next

**Built on orrery `e21d9dd9b185996995a90a0e53b589c84d7932d3` at
https://github.com/tonylquintanilla/palomas_orrery and gallery
`93d8ae9caead6ab801d854b46fae5b297747fc6c` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.** Both
HEADs read live with `git ls-remote` on 2026-09-26, after Tony's last push.

**Type: DESIGN, then BUILD.** The next session settles the print counts
with Tony, then builds manifest section 6.

**Opens from** `documentation/BUILD_MANIFEST_L322_D_earth_pole_20260922.md`,
rev 3, section 6, with `EXACT_ROWS_PRINTED.md` in the orrery root as the
list to work from. **Companion records:**
`documentation/RUN_RECORD_L322_D_p3_gallery_20260926.md` and
`documentation/RUN_RECORD_L322_D13_20260926.md`, each with Tony's run
appended. **Supersedes**
`HANDOFF_L322_D_orrery_magnetosphere_built_20260925.md` for what remains;
that handoff stays the record of D8, D9 and D10.

**Rules this work ran under:** protocol v3.69; provenance-discipline 2.19
(this session's loaded copy read 2.19, which discharged v3.69's
obligation), interactive-exhibit 1.4, gallery-cache-builder 1.6,
gallery-assembler 1.3, safe-file-editing 1.11, agentic-pre-test 1.2,
ledger-and-session-records 1.11. Every loaded copy was byte-identical to
`skills/` at orrery `43ba290b`. No skill changed this session, so no
reinstall is owed.

Written for Tony, a retired professional engineer who is not a
programmer, and for the session that builds section 6.

---

## 1. What was built, and how each piece was verified

Two patches, run by Tony in order, each followed by its repository's
maintenance run, and confirmed on his phone.

- **Gallery patch 3, gallery `93d8ae9c`.**
  - The Earth room draws the magnetotail as its own entry in the drawer
    (Tony's ruling, option A of two). It continues the magnetopause from
    where that surface stops, widens in a straight line to 120 Earth radii
    behind Earth, keeps a radius of 30 to 220, and is round, from the four
    tail rows of `constants_new.py`. Its hover prints the two measured
    sizes with their served uncertainties.
  - Each radiation belt is evenly spaced rings from its served inner edge
    to its served outer edge, on the step that lands on its peak: ten for
    the inner belt, nine for the outer. The peak ring is brighter and twice
    the size. Earth's typed 0.5 thickness is gone.
  - `tools/mirror_constants.py` copies each row's uncertainty into
    `data/objects_config.json`.
  - Earth's pole points at the two fallback rows in `constants_new.py`;
    its source names Horizons and the IERS. The axis hover states the
    23.93447-hour sidereal period from the served row. The magnetic tilt's
    source sentence lost its factor-of-ten error.
  - Verified: the cache swap worked first time; the gallery maintenance
    run passed 16 of 16; the live run found all 11 files served
    byte-identical, and the store-drift check now finds Earth's pole in the
    store (only the Sun's, Jupiter's and Saturn's poles remain outside it).
    Tony's phone: the tail, both belts, the axis hover and the Sun room all
    correct.
- **Orrery patch D13, orrery `56c4b30e`, then `e21d9dd9` for the
  maintenance files.** `exact_rows_report.py` gains a DRAWN table for
  gallery pointers to exact rows that are read only to place a drawing:
  the tail's drawn radius and drawn end, and Earth's two fallback pole
  rows. Verified: the orrery maintenance run passed 17 of 17 and its
  report reads "7 of 20 exact rows printed at 18 lines (8 orrery,
  10 gallery); 4 drawn only, 0 not followed, 0 map entries broken".

## 2. Rulings this session

- **The magnetotail is its own drawer entry** (Tony, 2026-09-26). Tony
  added that the two views, with the tail and without it, each get their
  own framing, which a separate entry gives.
- **The visitor-facing words** were shown to Tony before the build
  finished, and he said continue. Two were shortened afterwards to fit the
  hover limit of 17 lines; the gallery run record, section 4, gives both
  versions.
- **The orrery patch D13 was added to the plan** (Tony, 2026-09-26,
  confirmed as recommended).

## 3. What remains of Stage D: how exact rows print (manifest section 6)

**The rule is already in the skill.** provenance-discipline 2.19, Rule 7:
a display prints an exact row by a print count the row states, never by a
width chosen where it is printed. What is not built is the field that
carries the count and the code that reads it.

**The list is `EXACT_ROWS_PRINTED.md`.** At orrery `e21d9dd9` it names
seven printed exact rows, on 18 lines:

- `EARTH_LEO_UPPER_ALTITUDE_KM` (typed 2000.0) and
  `EARTH_LEO_LOWER_ALTITUDE_KM` (typed 200.0): two orrery lines each,
  `earth_visualization_shells.py` and `shell_configs.py`, both `,.0f`; one
  gallery line each, the LEO hovers' altitude line.
- `EARTH_VAN_ALLEN_OUTER_RADII` (4.5, a declared construction over its
  band rows): three orrery lines, all `:g`; four gallery lines in
  `renderBelts`.
- `EARTH_SOLAR_WIND_PRESSURE_NPA` (typed 2.0): three orrery lines, `:g`;
  two gallery lines, the magnetopause and bow shock hovers.
- `EARTH_SOLAR_WIND_BZ_NT` (typed 0.0): one gallery line, the
  magnetopause hover.
- `EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG` (typed 120.0) and
  `EARTH_BOW_SHOCK_CUT_ANGLE_DEG` (typed 105.0): one gallery line each.

The other thirteen exact rows are not printed and need no count. Four of
them are read by the gallery only to draw, which D13 now reports.

**What the build does, per manifest section 6.**

1. Each printed exact row states its print count on its `# Figures:`
   line, for example `exact -- prints 3`.
2. A checker refuses a print count larger than the digits the literal
   actually has, and a zero, such as Bz's 0.0, prints as 0.
3. The export serves the count beside each row; the mirror copies it into
   `data/objects_config.json`.
4. The 18 lines print by the served count: `fmtServed` in
   `gallery/feature_renderers.js`, and the orrery's f-strings.
5. Every hover that changes is listed before the patch with its text today
   and after, and Tony looks at each one on his phone (Mode 5).

**Finished means** the report shows every printed exact row carrying a
count and every printing line reading it. The report should gain a check
that says so, in the same way D13's DRAWN table is checked, so that
"finished" is something a run can fail.

**Questions to settle with Tony before building, one at a time.** A print
count on a declared pick records how the pick was stated, and the manifest
itself notes that the typed literal cannot say whether `200.0` meant 200
or 200.0. So the next session should first ask Tony, as its one question,
whether this is his to rule on or the skill's: "Does each declared pick
print the digits it was chosen with (2 nPa, 200 km, 120 degrees), or is
there a case where the trailing zero was meant?" If he answers once for
the class, the counts follow and the build needs no further rulings.
Visitor text that would change if picks print their chosen digits:

- The magnetopause and bow shock hovers today print "dynamic pressure
  2.0 nPa" and "Bz 0.0 nT"; they would read "2 nPa" and "0 nT".
- The outer belt's 4.5 already prints as 4.5 and would not change.
- The cut angles and LEO altitudes already print as whole numbers.

**Reach, measured at C2.** The orrery's Earth hovers carry 47 format sites
on 35 lines, of which the report counts 8 as printing an exact row. The
rest are one ledger class with no automated coverage (see section 4); do
not read a closed section 6 as covering them.

## 4. For the ledger, one row per class

New this session (from the gallery run record, section 5):

- **Jupiter's belt thickness is a typed 0.5 with no source.** It is served
  in `radiation_belts`, drawn by no room, and has no edge rows to draw
  across. It waits for the braid. The manifest and the previous handoff
  said "both `belt_thickness` entries"; this is the second one, kept on
  purpose.
- **The recorded Earth scene is overlaid piece by piece.** Three checks
  take the pole of date, the magnetosphere and the rotation period from
  the served cache, because `documentation/payload_earth_scene.json`
  predates them. It still carries the 9.6 tilt and the old belt thickness.
  This extends the existing aging-payload row; a recapture would retire
  the overlays.
- **The magnetotail's hover is at the line ceiling of 17.** Anything added
  to it needs a line taken away.
- **There is no Wikipedia article for the magnetotail;** its link is the
  Magnetosphere article.

Closing, per manifest section 8 and this build:

- **L-311: DONE**, both halves.
- **L-325: close**, superseded by L-322 (Tony's ruling, 2026-09-22).
- **L-342: close**; what remains is L-343 and L-345 (Tony's ruling,
  2026-09-22).

Carried from the previous handoff, unchanged:

- The orrery's magnetosphere hover gives Earth radii without kilometres or
  AU.
- The drawn tail's growth and the 1983 "about 30 percent" (the note is on
  the flare-end row).
- The uncertainty field's pattern reads a sentence's full stop as a
  decimal point.
- Earth's magnetosphere costs about 42 percent more per orrery animation
  frame since D8.
- `shell_configs.py`'s magnetosphere tooltip says nothing about the tail
  and still says the belts are drawn at the flux peak.
- A scanner comparison by set could pass blind.
- Phone behaviour of the rooms has no automated check.
- The hover budget check's weak floor ("at least one hover").
- The cache builder types its own `KM_PER_AU` beside the served row.
- The gallery maintenance routine pulls the export after the build.
- Earth's eccentric dipole offset, other bodies' cone hovers, and the
  scanner's proximity rule.
- The orrery's Earth hovers' 47 format sites on 35 lines, with no
  automated coverage.

The phone tap lag and provenance-discipline 2.18's stale worked example
are both done and drop off the list. The next free handle at orrery
`62e93856` was L-363; re-read the ledger index before assigning one.

## 5. For the next session

- Confirm the loaded skill versions match the manifest, as usual. None is
  owed a check beyond that.
- A parallel chat is building a symbols-only Explorer room in
  `interactive.html` (`documentation/HANDOFF_explorer_symbols_half1_20260926.md`).
  Section 6 should not need that file; if it does, check whether that
  chat has pushed and build on the new HEAD.
- Read `EXACT_ROWS_PRINTED.md` again at the session's own base: the line
  numbers above will have moved.

## 6. Tony-actions

- (do) File this handoff in the orrery's `documentation/`.
- (do) File the ledger rows in section 4, and close L-311, L-325 and L-342.
- (decide) The Sun's Auto view, carried from the previous handoff.

---

Session written September 2026 with Anthropic's Claude Opus 5.5.
