# Handoff -- L-345: conversions are served and the gallery prints them; orrery patch D20 is next

**Built on orrery `807e9dd535211b2bdb91263b49988e1494c308a8` at
https://github.com/tonylquintanilla/palomas_orrery; pushed at
`2a7d26b9fc200a1ceae6afb3af541e5d60c33f54`. Gallery built on
`2df02f3baead894ff40922bcadef9cb84c49fa07` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io; pushed at
`52da593c50d28803297cebe261fd2be13470c8c3`.** Both HEADs read live with
`git ls-remote` on 2026-09-28. The pushed files of both patches were
compared with the trees this session tested, and they are identical.

**Type: BUILD.** The next session builds orrery patch D20. One small
design question is inside it (section 4, item 3: the orrery crust
hover's words), and Tony answers it before the patch ships.

**Supersedes** `HANDOFF_L345_D19_done_gallery_next_20260928.md` for what
remains; that file stays the record of D18 and D19.
**Companion records:** `documentation/PREBUILD_L345_gallery_hover_changes_20260928.md`
(the before-and-after list, filed by D19a);
`documentation/DESIGN_L345_conversions_computed_20260928.md` and
`documentation/RULING_L345_conversion_count_rule_20260928.md`.
Tony's run records are in
`HANDOFF_L322_D_print_counts_orrery_done_20260928.md`.

**Rules this work ran under:** protocol v3.72. Loaded and confirmed at
session start: provenance-discipline 2.22 and interactive-exhibit 1.5
(the obligation the last handoff carried is discharged), and every other
skill matching the manifest. No skill changed this session; D20 carries
two bumps (section 4, item 6).

Written for Tony, a retired professional engineer who is not a
programmer, and for the session that builds next.

---

## 1. What was built, and how each piece was verified

- **Orrery patch D19a (orrery `b61d1982`).** Two new rows, each Earth's
  equatorial radius plus an altitude the store already held:
  `EARTH_STRATOPAUSE_RADIUS_KM`, 6428 km at 4 figures, and
  `EARTH_THERMOPAUSE_RADIUS_KM`, 6980 km at 3. The export serves them in
  Earth radii as 1.0078 and 1.094. `test_constants_export.py` pins both
  (10 pins, was 8). The ledger records the order on L-345. Tony's
  maintenance run: 19 of 20, the one failure the expected "Exact rows by
  the count".
- **The gallery patch (gallery `7b230cf` and `52da593c`),**
  `patch_L345_gallery_conversions_served_20260928.py`. It carried all of
  gallery patch 4's work, and patch 4 itself was never run.
  - The mirror copies the export's `"in"` onto each served node, and
    writes a slot measured in another unit from its row's `"in"` entry
    for that unit. Nothing is converted in the gallery. Mirror suite
    case 20; shown failing when the mirror ignores `"in"`.
  - Eleven pointers moved off conversion rows onto the rows they come
    from. The two standoffs' `standoff_km` and `standoff_au` nodes were
    removed; the standoff serves both through `"in"` now.
  - The crust points at `EARTH_MEAN_RADIUS_KM` (section 2) and serves
    Tony's approved sentence as a new field, `radius_note`.
  - `feature_renderers.js` prints every km and AU line from `"in"`
    where a node serves it. The AU stays at three figures, except where
    cutting a served value would round a tie (section 2). The Sun's
    radius line prints by a served count and is singular at 1.
  - `smoke_display_figures.js` works the expected lines from `"in"` by
    its own arithmetic, grades the new lines, names each served AU tie in
    its report, and gained two self-test ways to go red. Shown failing
    when the tie rule or the served units are broken. New fixture:
    `documentation/fixture_hovers_L345_on_2df02f3b.json`.
  - The patch also writes `data/constants_export.json` and `.sha` at
    orrery `b61d1982`, so the config and the export it was made from
    travel together (finding in section 5).
  - Every Earth and Sun hover was diffed before and after: exactly the
    approved lines changed, nothing else in any room.
- **Tony's runs:** gallery maintenance run 19 of 19; phone check of both
  rooms "correct"; orrery maintenance run 18 of 18 gating checkers, with
  "Exact rows by the count" PASSING. (The patch's steps said "20 of 20";
  two of the twenty are report-only, so 18 of 18 is the right count.)

## 2. Rulings this session

- **The order (Tony, "confirmed as recommended"):** D19a, then the
  gallery patch, then D20, so every visible change reached one phone
  check.
- **The three-figure AU line and a tie (Tony, 2026-09-28):** where
  cutting a served, already-rounded AU value to three figures would
  round a tie -- the dropped digits exactly a 5 -- the page prints the
  served digits in full. Today that is the inner core, 0.000008165 AU.
  Checked against the skills in chat: it is Rule 7's main rule, not a
  new exception; what the skills lack is a sentence saying when the
  exception steps aside (section 4, item 6).
- **The crust is drawn at Earth's mean radius (Tony, 2026-09-28: "let's
  just do it now").** Reasons agreed in chat: a sphere at the mean
  radius stays nearer sea level everywhere than one at the equatorial
  radius, and the interior layers come from PREM, whose surface is the
  6,371 km sphere -- the store's own upper-mantle row says "24.4 km
  below the mean radius". The Earth radius as a UNIT stays equatorial:
  Prsa et al. (2016), AJ 152:41, on IAU 2015 Resolution B3, reads an
  unqualified terrestrial radius as the equatorial one. Tony, on why:
  it is a drawing choice, because we draw a sphere, not the flattened
  shape.
- **The crust's words (Tony, "approved"):** "This is Earth's mean
  radius: the radius of a ball with the same volume as the smooth,
  slightly flattened shape fitted to sea level. The Earth radius used as
  a unit here is the equatorial radius, as the International
  Astronomical Union recommends, so the mean radius is a little less
  than one. The ground itself rises and falls from this by kilometres."
- **The mean radius keeps its 7 figures.** 6,371.000 km is the radius of
  the ball with the reference ellipsoid's volume; recomputed from the
  ellipsoid's axes it agrees within a metre either way. The figures
  describe the model, and the hover says so.
- **Wait for D20 (Tony):** until D20, the orrery draws the crust at
  6,378 km while the gallery draws it at 6,371 km. Invisible at that
  scale, and no check compares the two.

## 3. The two questions Tony asked at the close

**Does D20 close Earth's slice?** Earth's slice closed earlier, in the
sense the export uses: `closed_slices` has been `["EARTH"]`, every
`EARTH_` row visited and gated. L-322 Stage D's finishing condition
(its Gap of 2026-09-28) was met by the gallery patch: "Exact rows by the
count" passes with the gallery beside the orrery, and the gallery run
passes. D20 finishes L-345, the conversion work. What stays open on
Earth after it is recorded classes, not the slice: chiefly the orrery's
own Earth hovers, which format numbers by a width chosen at each line
(L-352, L-387) and which no checker reads.

**Does it close the Sun's slice?** No. That is its own build, and the
next body after Earth under L-322's Gap. Today `closed_slices` is Earth
only; 14 of the Sun room's links point at rows with no `# Unit:` line
and are not exported, so the mirror leaves them as hand-typed values
(L-371, L-386). The Sun's slice walks each of those rows once, re-homes
each conversion row to the unit its source gives (L-386), and only then
closes. The chromosphere is already done, which is a start.

## 4. What D20 builds

1. **The rows.** The 13 conversion rows stop being rows:
   `EARTH_INNER_CORE_RADII`, `EARTH_OUTER_CORE_RADII`,
   `EARTH_LOWER_MANTLE_RADII`, `EARTH_UPPER_MANTLE_RADII`,
   `EARTH_GEOSTATIONARY_RADII`, `EARTH_LEO_INNER_RADII`,
   `EARTH_LEO_OUTER_RADII`, `EARTH_HILL_SPHERE_RADII`,
   `EARTH_MAGNETOPAUSE_STANDOFF_KM`, `EARTH_MAGNETOPAUSE_STANDOFF_AU`,
   `EARTH_BOW_SHOCK_STANDOFF_KM`, `EARTH_BOW_SHOCK_STANDOFF_AU`, and
   `CHROMOSPHERE_PHYSICAL_RADII` (re-written as
   `CHROMOSPHERE_TOP_KM / SUN_RADIUS_KM`). Also
   `EARTH_STRATOPAUSE_RADII` and `EARTH_THERMOPAUSE_RADII`, re-written as
   their new kilometre rows divided by `EARTH_EQUATORIAL_RADIUS_KM`.
   Each keeps its name and `# Unit:` line, loses `# Figures:` and
   `# Status:`, and gains a marker the reader recognizes, naming its
   source row. The export lists it under not_exported with that reason;
   the closed-slice gate skips it. **Measured at gallery `52da593c`: no
   gallery pointer names any of these fifteen**, so the gallery is not
   touched.
2. **The check that can fail.** `test_derived_figures.py` gains Rule 8's
   widening: a row that is one row scaled only by exact rows, and is not
   marked as a conversion, fails by name. Show it failing before
   trusting it.
3. **The orrery's crust moves to the mean radius.** In `shell_configs.py`
   Earth's crust `radius_fraction` is 1.0 today; it becomes the mean
   radius over the equatorial, computed from the two rows, not typed.
   The crust's hover says "Source (radius): IERS Conventions (2010) ...
   equatorial radius" and must change. **Its new words go to Tony before
   the patch ships**; the gallery's approved sentence is the obvious
   start. In `constants_new.py`, the FRAME NOTE above
   `EARTH_MEAN_RADIUS_KM` (about 7 km between the drawn surface and
   PREM's) and that row's own note ("NOT the radius the orrery draws
   to") must be rewritten, and the L-249 comment beside the crust's
   `info_polar_deg` ("about 31 km") becomes 24.4 km. Mode 5 in the
   orrery: Tony's eye on the Earth interior.
4. **Hold every other orrery hover byte for byte,** with the pre-delivery
   test (agentic-pre-test), because this is display code. One orrery
   hover prints a conversion name by its count: the Sun's chromosphere,
   `CHROMOSPHERE_PHYSICAL_RADII` at 1.003; after it loses its
   `# Figures:` line it needs a count, and the computed count is 4, the
   same. No other conversion name is printed through `figures_of()` or
   `_declared()` (measured at `807e9dd5`; re-measure at `2a7d26b9`).
5. **The master plan restamps to v34** with an executive summary at the
   top, written from the current state; section 5a stays the critical
   path, brought current; both companion files get a short retirement
   line; L-333 and L-362 close pointing at v34 (Tony's ruling of
   2026-09-28, recorded in the superseded handoff, section 2).
6. **Two skill bumps, one commit, one protocol entry (v3.73),** under the
   binding rule; v3.70 moves down to the history file.
   - **ledger-and-session-records 1.11 -> 1.12:** The Document Stack --
     the plan is one document at two zooms, executive summary and body,
     with the critical path inside the body; the summary is rewritten at
     every restamp.
   - **interactive-exhibit 1.5 -> 1.6:** under Provenance is part of the
     build, (a) where cutting a served AU to three figures would round a
     tie, the served digits print in full, and the hover check names
     each case; (b) the mirror serves a slot measured in another unit
     from its row's `"in"`; (c) a shell may serve a `radius_note`, a
     sentence under its radius line where the number needs one to be
     read rightly. Tony was told (a) would be written here.
   - Check first that no other session has bumped either skill since
     `2a7d26b9`.

## 5. For the ledger, one row per class, filed by D20

- **L-345 closes** when D20 lands: the gallery prints from `"in"`
  (gallery `52da593c`) and the store holds no conversion rows.
- **L-333 and L-362 close** with the plan's v34.
- **L-322** gains a note: Stage D's finishing condition met at orrery
  `2a7d26b9` and gallery `52da593c`; its Gap's point (2) is done
  (L-345 decided and built); point (3), the Sun's slice, is next.
- **New row -- the pull that cannot fail.** In the gallery maintenance
  run, "Constants export pull" reported PASS "no change" in this
  session's sandbox when it could not reach GitHub at all (an N-A inside
  it), and "Config mirror" then rewrote the config from the older export
  still on disk: 36 fields written backwards and 5 links refused. Tony's
  runs reach GitHub, so it has not happened there, and the gallery patch
  shipped its export to rule it out this time. The class: a generator
  whose failure prints as success, followed by a writer that trusts it.
  (A Check That Cannot Fail Is Not Passing.)
- **The crust ruling** is recorded on L-345's closing note, with the
  orrery crust move that completes it.
- **L-387** gains a line: the orrery prints the LEO edges as "1.03 to
  1.31 Earth radii" (`earth_visualization_shells.py`, `.2f`), shorter
  than the gallery's served count. Same value, a width chosen on the
  line.

## 6. For the next session

- Confirm the loaded skills match the manifest.
- Re-anchor both repositories.
- Build section 4, in the order given; bring Tony the orrery crust
  hover's words before delivery.

## 7. Tony-actions

- (do) File this handoff in the orrery's `documentation/`.
- (do) File the unrun `patch_L322_D_p4_gallery_print_counts_20260927.py`
  in the gallery's `documentation/`, as a record; the gallery patch
  carried its work.
- (decide, in the D20 session) The orrery crust hover's new words.
- (decide, still open) The Sun's Auto view, L-385.

---

Session written September 2026 with Anthropic's Claude Opus 5.5.
