#!/usr/bin/env python3
"""
patch_L322_D_18_ledger_stage_d_rows_20260928.py -- ORRERY repo.

Run: save this file in the ORRERY repo ROOT (next to
palomas_orrery.py), open it in VS Code and click Run. The terminal
equivalent is: python patch_L322_D_18_ledger_stage_d_rows_20260928.py

A patch is run from its repository's ROOT and filed in documentation/
AFTER it has run. This script refuses to run from documentation/.

Built on orrery a7868eee04575abeeae303a6ca6a700890e835f1
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 2df02f3baead894ff40922bcadef9cb84c49fa07
at https://github.com/tonylquintanilla/tonyquintanilla.github.io,
read only)

WHAT IT DOES. It edits one file, LEDGER_CONSOLIDATED.md. Five Stage D
handoffs and the Stage D manifest each listed things "for the ledger",
and none of them was ever filed. This files all of them at once:

  New items, L-368 to L-385 (one per kind of problem):
  L-368  Other bodies' typed poles disagree with their cited table or
         cite a withdrawn report
  L-369  Earth's obliquity typed outside constants_new.py
  L-370  Jupiter and Saturn numbers typed only in objects_config.json
  L-371  The Sun room's served numbers: 43 with no link, and radii
         printed with no count
  L-372  Two drawing settings live in constants_new.py
  L-373  A unit conversion by a bare number inside a constants_new.py
         expression
  L-374  Showing Earth's precession over time (Tony's idea)
  L-375  Earth's eccentric dipole offset is not drawn
  L-376  Other bodies' dipole-cone hovers: typed offsets and
         abbreviated radii
  L-377  The provenance scanner's proximity rule can count a string as
         cited by a neighbour's source
  L-378  Phone behaviour of the rooms has no automated check
  L-379  The recorded Earth scene payload is aging
  L-380  The gallery maintenance routine pulls the constants export
         after the cache build
  L-381  The uncertainty field's pattern reads a full stop as a
         decimal point
  L-382  Earth's magnetosphere costs about 42 percent more per
         animation frame
  L-383  shell_configs.py's magnetosphere tooltip is behind
  L-384  The scaling rule stops short of a single measured value
  L-385  The orrery's Auto view of the Sun opens about 31 times wider
         -- carries your open decision

  A line added to six open items, where the problem is the same kind
  as one already recorded: L-243, L-345, L-350, L-351, L-352, L-360.

  A Stage D status note on L-322.

  Three items closed, per your rulings of 2026-09-22:
  L-311 (done, both halves), L-325 (superseded by L-322), L-342.

RUN THE LEDGER INDEX AFTERWARDS: python ledger_index.py. It rebuilds
the index tables and moves the three closed items into section C. This
patch does not touch the INDEX zone and does not fingerprint it.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written September 28, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os
import sys

LEDGER = "LEDGER_CONSOLIDATED.md"

# Fingerprinted OUTSIDE the INDEX zone, which ledger_index.py
# regenerates (safe-file-editing, A Guard Must Not Fence What a
# Generator Rewrites).
BASE_OUTSIDE_INDEX = "dc20a5d89c36158764f319e42592283c"

INDEX_START = "<!-- INDEX:START"
INDEX_END = "<!-- INDEX:END -->"

EDITS = [('<!-- L:360 status:OPEN upd:2026-09-22 section:A flag: rice: -->\n', '<!-- L:360 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n'), ('**Gap:** Have the budget also measure hovers', '- **A second way it passes blind (2026-09-28):** its only floor is "at\n  least one hover". With the frame rows missing it measured 2 of 96\n  hovers and passed. D7 made it fail on missing frame rows; the weak\n  floor itself remains. Found 2026-09-25.\n**Gap:** Have the budget also measure hovers'), ('<!-- L:352 status:OPEN upd:2026-09-22 section:A flag: rice: -->\n', '<!-- L:352 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n'), ('**Gap:** Design the helper, then sweep', "- **Also in this class (2026-09-28):** the orrery's solar hovers print AU\n  at a fixed width, `:.5f` on `SOLAR_RADIUS_AU`\n  (`solar_visualization_shells.py` line 102), a row with no `# Figures:`\n  line yet. The chromosphere's AU happens to match its count.\n  [verified @a7868eee]\n**Gap:** Design the helper, then sweep"), ('<!-- L:351 status:OPEN upd:2026-09-22 section:A flag: rice: -->\n', '<!-- L:351 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n'), ("**Gap:** Each lands with its store's next bump.", "- **provenance-discipline, scanner mechanics, if it recurs (2026-09-28):**\n  comparing the scanner's findings as a SET of names cannot see a second\n  finding that looks like one already there. D8's result stood because\n  the scanner's own count agreed; D9 and D10 compared counted lists.\n**Gap:** Each lands with its store's next bump."), ('<!-- L:350 status:OPEN upd:2026-09-22 section:A flag: rice: -->\n', '<!-- L:350 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n'), ('**Gap:** Decide whether the magnetotail hover should print it', '- **Three things about the same hover (2026-09-28).** The magnetotail\'s\n  hover is at the hover budget\'s ceiling of 17 lines, so printing the\n  observed extent means taking a line away. There is no Wikipedia\n  article for the magnetotail; its link is the Magnetosphere article\n  [verified @2df02f3b]. And the drawn tail widens about 44 percent from\n  20 to 120 Earth radii behind Earth at its central width, 32 percent at\n  its low end, against the 1983 "about 30 percent"; the 1983 figure is\n  inside the 1985 envelope, so the construction stands, and the note is\n  on the flare-end row in `constants_new.py`. [per chain]\n**Gap:** Decide whether the magnetotail hover should print it'), ('<!-- L:345 status:OPEN upd:2026-09-22 section:A flag: rice: -->\n', '<!-- L:345 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n'), ('**Gap:** The decision above, then the next slice builds to it.', "- **Also in this class (2026-09-28):** the ORRERY's magnetosphere hover\n  gives its distances in Earth radii only, with no kilometres or AU, in\n  its old lines and the ones D8 added. Each would need a row with a\n  declared count, as the standoffs got at C2, or the export converting.\n  Found 2026-09-25.\n**Gap:** The decision above, then the next slice builds to it."), ('<!-- L:342 status:OPEN upd:2026-09-22 section:A flag:! rice:4/4/95/2 -->\n', '<!-- L:342 status:DONE upd:2026-09-28 section:A flag: rice:4/4/95/2 -->\n'), ('- **Ref:** `gallery/feature_renderers.js`;\n', "- **2026-09-28 -- CLOSED**, Tony's ruling of 2026-09-22, filed now. Its\n  remaining work is L-343 (LEO's inner edge and the geocorona) and\n  L-345 (converting a rounded served km to AU in the page), each of\n  which already carries it.\n- **Ref:** `gallery/feature_renderers.js`;\n"), ('<!-- L:325 status:OPEN upd:2026-09-22 section:A flag: rice:3/3/90/2 -->\n', '<!-- L:325 status:DONE upd:2026-09-28 section:A flag: rice:3/3/90/2 -->\n'), ('**Ref:** L-305, L-314, L-322, `constants_new.py`,\n', "**Note (2026-09-28) -- CLOSED as SUPERSEDED by L-322**, Tony's ruling of\n2026-09-22, filed now. Nothing this item built is still in the tree.\nLoose ends: none.\n**Ref:** L-305, L-314, L-322, `constants_new.py`,\n"), ('<!-- L:322 status:OPEN upd:2026-09-22 section:A flag: rice:4/5/70/6 -->\n', '<!-- L:322 status:OPEN upd:2026-09-28 section:A flag: rice:4/5/70/6 -->\n'), ('**Ref:** L-305, L-306 (approximations are not promoted), L-314,', '**Note (2026-09-28) -- Stage D, where it stands.** Orrery patches D1 to\nD17 and gallery patches 1 to 3 have landed (orrery `a7868eee`, gallery\n`2df02f3b`). The records are the Stage D handoffs in `documentation/`,\nthe latest `HANDOFF_L322_D_print_counts_orrery_done_20260928.md`. Earth\'s\npole of date is fetched from Horizons and drawn in both; the magnetosphere\nand the magnetotail are drawn in both; the seven exact rows a display\nprints now state a print count (manifest section 6, orrery half, D15).\nprovenance-discipline went 2.18 to 2.21 across these sessions.\n- **Records, not work.** The phone tap lag was found and fixed at gallery\n  `ce09f789`: DONE. The pole row the 2026-09-22 Gap above planned as a\n  rate and an angle does not exist in that form: the source shows Earth\n  has no such row in this frame (manifest section 7). And one session\n  shipped two versions of provenance-discipline, 2.20 and 2.21, against\n  ONE SESSION, ONE BUMP; protocol v3.71 says so, and it is noted here so\n  it is not repeated by habit.\n- **The Stage D handoffs listed ledger rows that were never filed.** Five\n  handoffs and the manifest each carried them forward as "for the\n  ledger". Filed together on 2026-09-28: new rows L-368 to L-385; added\n  lines on L-243, L-345, L-350, L-351, L-352 and L-360; L-311, L-325 and\n  L-342 closed.\n**Gap (2026-09-28):** Stage D\'s last piece is one gallery patch. It\ncarries the unrun gallery patch 4\'s work (the Earth room prints exact\nrows by their served count) and the Sun room\'s (the chromosphere and the\nphotosphere radii). Finished when the orrery\'s "Exact rows by the count"\npasses with the gallery beside it and the gallery maintenance run passes\n17 of 17. Then points (2) and (3) of the Gap above.\n**Ref:** L-305, L-306 (approximations are not promoted), L-314,'), ('<!-- L:311 status:OPEN upd:2026-09-10 section:A flag: rice:2/2/90/1 -->\n', '<!-- L:311 status:DONE upd:2026-09-28 section:A flag: rice:2/2/90/1 -->\n'), ('**Ref:** L-291 (step 3 record), L-292 (not this), provenance-discipline\n', "**Note (2026-09-28) -- CLOSED, both halves.** Built in L-322 Stage D.\nThe sidereal rotation period is a derived row,\n`EARTH_SIDEREAL_ROTATION_PERIOD_H`, served in Earth's entry as\n`rotation_period` and quoted in the axis hover since gallery patch 3\n(gallery `93d8ae9c`) [verified @2df02f3b]. The obliquity half changed\nshape at manifest revision 3: the axis hover prints Earth's tilt of date,\nworked out from the pole Horizons serves, instead of a served obliquity.\nLoose ends: none recorded as not done. Drawing the rotation itself needs\na rotation phase the orrery does not model; that is carried on L-375.\n**Ref:** L-291 (step 3 record), L-292 (not this), provenance-discipline\n"), ('<!-- L:243 status:OPEN upd:2026-08-25 section:A flag: rice:3/3/95/2 -->\n', '<!-- L:243 status:OPEN upd:2026-09-28 section:A flag: rice:3/3/95/2 -->\n'), ('routed to L-244.\n\n#### [L-244] Sweep for replicated', "routed to L-244.\n**Note (2026-09-28):** one more replication, in the gallery.\n`tools/gallery_cache_builder.py` line 132 types its own\n`KM_PER_AU = 149597870.7` beside the row the constants export serves.\nEqual today; nothing checks they stay equal. Unlike the page's copy in\n`feature_renderers.js`, this one is Python and could read the served\nrow. Found 2026-09-25, gallery `ce09f789`. [verified @2df02f3b]\n\n#### [L-244] Sweep for replicated"), ('#### [L-367] No checker opens a new room (checks, gallery)\n', '#### [L-385] The orrery\'s Auto view of the Sun opens about 31 times wider since Stage D (orrery, Tony\'s eye)\n<!-- L:385 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n- **Found 2026-09-24** building L-322 Stage D\'s orrery autoscale (D4).\n  With its inner shells on, the Sun\'s view opens about 31 times wider\n  than before: its half-width goes from 0.0093 AU to 0.29 AU, because\n  its rotation axis is drawn 52 solar radii long (`half_len_frac` 50 in\n  `PLANET_ROTATION`). Mercury with every shell opens about 9 times\n  wider, set by its sodium tail. Both follow the autoscale ruling\n  literally. [per chain]\n- Carried as an open decision through four Stage D handoffs with no\n  ledger row; filed 2026-09-28.\n- **Tony-action (decide):** whether the Sun\'s axis should be drawn\n  shorter. A drawing choice for Tony\'s eye.\n**Gap:** Tony\'s decision above; if shorter, one change to `half_len_frac` for the Sun.\n**Ref:** `documentation/HANDOFF_L322_D_orrery_pole_built_20260924.md` sec. 3; L-322.\n\n#### [L-384] The scaling rule stops short of a single measured value scaled by an exact row (skills, store)\n<!-- L:384 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n- **Recorded, not built.** provenance-discipline 2.21 (L-322 D16,\n  2026-09-28) says a sum or difference scaled by an exact row keeps its\n  decimal place, carried through the scaling, not its figure count. On\n  purpose, it leaves a SINGLE measured value scaled by an exact row\n  under the fewest-figures rule. The reference page, Wikipedia\'s\n  Significant figures, allows more in its unit-conversion exception\n  (8 inches becomes 20. cm).\n- Nothing needs the wider form today.\n**Gap:** When a row needs the page\'s full unit-conversion exception, widen Rule 3 then, deliberately, with that row as the case.\n**Ref:** skills/provenance-discipline/SKILL.md, Rule 3; PROJECT_INSTRUCTIONS.md v3.71; L-322.\n\n#### [L-383] shell_configs.py\'s magnetosphere tooltip says nothing of the tail and puts the belts at the flux peak (orrery, words)\n<!-- L:383 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n- **Found 2026-09-25** building L-322 D8 to D10. `shell_configs.py`\n  holds a copy of the magnetosphere tooltip that no display reads, kept\n  in step with its live twin by hand. It says nothing about the\n  magnetotail, which D8 now draws, and still says both Van Allen belts\n  are "drawn at the flux peak" (lines 2321 and 2322 at orrery\n  `a7868eee`). [verified @a7868eee]\n- The same wording question is open for the gallery on L-349.\n**Gap:** Bring the copy into line when L-349\'s wording is ruled, or retire the copy.\n**Ref:** `shell_configs.py`; `earth_visualization_shells.py`; L-349; L-322.\n\n#### [L-382] Earth\'s magnetosphere costs about 42 percent more per orrery animation frame since D8 (orrery, rendering)\n<!-- L:382 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n- **Found 2026-09-25** building L-322 D8. Each animation frame with\n  Earth\'s magnetosphere on grew from about 147 KB to about 209 KB when\n  D8 drew the magnetotail; D9 held it level. [per chain]\n- A rendering matter, not a correctness one: whether animation feels\n  slower is for Tony\'s eye.\n**Gap:** Tony watches an Earth animation with the magnetosphere on and decides whether it needs thinning.\n**Ref:** `earth_visualization_shells.py`; `documentation/HANDOFF_L322_D_orrery_magnetosphere_built_20260925.md`; L-322.\n\n#### [L-381] The uncertainty field\'s pattern reads a sentence\'s full stop as a decimal point (export, checks)\n<!-- L:381 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n- **Found 2026-09-25** building L-322 D8 to D10. A row\'s comment\n  written "uncertainty 10. The ..." was served as the\n  uncertainty "10.", because the pattern that reads the number takes the\n  full stop as a decimal point. [per chain]\n- Every row today follows the number with a unit, a comma or the end of\n  the line, so nothing served is wrong. Nothing checks that the next row\n  will.\n**Gap:** The reader stops a number at a full stop followed by a space, and a test row proves it.\n**Ref:** `constants_rows.py`; `export_constants.py`; `test_constants_export.py`; L-322.\n\n#### [L-380] The gallery maintenance routine pulls the constants export after the cache build (gallery, routine)\n<!-- L:380 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n- **Found 2026-09-25** at gallery `ce09f789`. The routine builds the\n  served cache and then pulls `constants_export.json` from the orrery,\n  so the served `frame_constants.orrery_sha` names the export from\n  BEFORE that pull. The values are the same today; the SHA stamp is one\n  step behind. [per chain]\n**Gap:** Pull the export first, then build, so the stamp names the export the cache was built from.\n**Ref:** gallery `gallery_maintenance_run.py`; gallery `tools/gallery_cache_builder.py`; L-322.\n\n#### [L-379] The recorded Earth scene payload is aging, and three checks patch it piece by piece (checks, gallery)\n<!-- L:379 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n- **Found 2026-09-25, grown 2026-09-26.** Gallery\n  `documentation/payload_earth_scene.json` was recorded 2026-09-08. It\n  predates Earth\'s pole of date and the new magnetosphere, and still\n  carries the magnetic tilt as 9.6 where the served cache has 9.4105\n  [verified @2df02f3b], and the old belt thickness.\n- At gallery patch 3 (gallery `93d8ae9c`), three checks began taking\n  the pole of date, the magnetosphere and the rotation period from the\n  served cache instead, laid over the recording. Each new served piece\n  adds another overlay. [per chain]\n- Related, not the same: L-360 (the hover budget reads recorded\n  payloads) and L-367 (no checker boots a new room).\n**Gap:** Recapture the payload from the current cache; the overlays then retire.\n**Ref:** gallery `documentation/payload_earth_scene.json`; gallery `documentation/smoke_*.js`; L-360; L-367.\n\n#### [L-378] Phone behaviour of the rooms has no automated check (checks, gallery)\n<!-- L:378 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n- **Found 2026-09-25.** The phone tap lag fixed at gallery `ce09f789`\n  was found and measured only in a headless browser with WebGL. The\n  maintenance run has no such browser, so nothing in it would see a\n  phone-only regression. Tony\'s phone is the only check.\n**Gap:** A phone-sized headless run in the maintenance suite, or a stated decision that the phone check stays manual.\n**Ref:** gallery `interactive.html`; gallery `gallery_maintenance_run.py`; L-367.\n\n#### [L-377] The provenance scanner\'s proximity rule can count a string as cited by a neighbour\'s source (checks)\n<!-- L:377 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n- **Found 2026-09-24** building L-322 Stage D. The scanner treats a\n  string as cited when a `# Source:` sits near it, so a string can pass\n  on the strength of a source written for the line beside it. A check\n  that passes without having checked. [per chain]\n**Gap:** Measure how often it happens, then tie a citation to the line it names.\n**Ref:** `provenance_scanner.py`; skills/provenance-discipline/SKILL.md (scanner mechanics).\n\n#### [L-376] Other bodies\' dipole-cone hovers: typed offsets and abbreviated radii (orrery, words)\n<!-- L:376 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n- **Found 2026-09-24** building L-322 D5, Earth\'s cone hover. The other\n  bodies\' cone hovers print their tilts as a rounded "~", carry typed\n  offsets, and abbreviate their radii (R_M, R_J, R_S). Mercury, Jupiter and\n  Saturn. [per chain]\n- The shared tilt line is already on L-352. This row is the rest.\n**Gap:** Each body\'s own slice.\n**Ref:** `planet_visualization_utilities.py`; L-352; L-322.\n\n#### [L-375] Earth\'s eccentric dipole offset is not drawn (store, Earth)\n<!-- L:375 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n- **Found 2026-09-24** building L-322 D5. Earth\'s magnetic dipole sits\n  off the planet\'s centre. A source to start from: Koochak and\n  Fraser-Smith (2017), Earth and Space Science 4, 626,\n  doi:10.1002/2017EA000280; or IGRF-13\'s degree-2 coefficients with a\n  sourced formula. The publisher\'s site refused the session as a bot, so\n  nothing has been read yet.\n- Drawing it also needs Earth\'s rotation phase, which the orrery does\n  not model.\n**Gap:** Read the source; then decide how, or whether, to show an offset that depends on a rotation phase the orrery does not model.\n**Ref:** `earth_visualization_shells.py`; `constants_new.py`; L-356 (IGRF-14).\n\n#### [L-374] Showing Earth\'s precession over time (orrery, idea)\n<!-- L:374 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n- **Tony, 2026-09-23:** fetching the pole of date "would allow us to\n  model precession in the future." Not built in Stage D.\n**Gap:** An idea, recorded; no design yet.\n**Ref:** L-322 Stage D (pole of date); `documentation/BUILD_MANIFEST_L322_D_earth_pole_20260922.md` sec. 7.\n\n#### [L-373] A unit conversion by a bare number inside a constants_new.py expression (store)\n<!-- L:373 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n- **Found 2026-09-22** in revision 1 of the Stage D manifest\'s period\n  row. An expression that divides by a bare 3600, 60 or 1000 converts a\n  unit the unit checker does not know about, so the checker converts\n  again and the stored value disagrees with the arithmetic.\n- Claude Fable 5.1 notes the class also reaches `LIGHT_MINUTES_PER_AU`\n  and its neighbours among the rows not yet migrated.\n**Gap:** A sweep of `constants_new.py` expressions for bare conversion numbers, each replaced by its named conversion row.\n**Ref:** `constants_new.py`; `documentation/BUILD_MANIFEST_L322_D_earth_pole_20260922.md` sec. 7; L-243; L-244.\n\n#### [L-372] Two drawing settings live in constants_new.py (orrery, store)\n<!-- L:372 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n- **Found 2026-09-22.** `DEFAULT_MARKER_SIZE` and `CENTER_MARKER_SIZE`\n  (lines 1718 and 1720 at orrery `a7868eee`) are drawing choices, not\n  facts, and are read by `palomas_orrery.py` and\n  `palomas_orrery_helpers.py`. [verified @a7868eee]\n- `HORIZONS_MAX_DATE`, between them, is a fact about the data source and\n  stays.\n**Gap:** Move the two marker sizes into the drawing code.\n**Ref:** `constants_new.py`; `palomas_orrery.py`; `palomas_orrery_helpers.py`.\n\n#### [L-371] The Sun room\'s served numbers: 43 with no link, and radii printed with no count (gallery, the Sun\'s slice)\n<!-- L:371 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n- **Found 2026-09-22 and 2026-09-28.** In `data/objects_config.json`\n  the Sun carries 43 numbers with no link to a store row, not yet sorted\n  into measurements and drawing choices (manifest section 2.6). [per\n  chain]\n- The Sun room\'s "Radius:" line (the `r_sun` branch of\n  `feature_renderers.js`) prints each served value as it is, with no\n  figure count. The chromosphere and the photosphere are being fixed in\n  the gallery patch that finishes L-322 Stage D; the others, such as the\n  Alfven surface at 19.7, stay as they are until their rows carry\n  counts.\n- The Sun is the next body\'s slice, since its room is published.\n**Gap:** The Sun\'s slice: sort the 43, give each measured one a row and a count, and print by the count.\n**Ref:** gallery `data/objects_config.json`; gallery `gallery/feature_renderers.js`; L-322 Gap (3); L-345.\n\n#### [L-370] Jupiter and Saturn numbers typed only in objects_config.json (gallery, store)\n<!-- L:370 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n- **Found 2026-09-22 and 2026-09-26.** Jupiter\'s and Saturn\'s ring radii\n  and thicknesses, 32 numbers, are typed in `data/objects_config.json`\n  with no store row behind them (manifest section 2.6). [per chain]\n- Jupiter\'s `radiation_belts` entry also serves a `belt_thickness` of\n  0.5 with no source. No room draws it, and it has no edge rows to draw\n  across. Earth\'s was replaced in Stage D; Jupiter\'s was kept on\n  purpose. [verified @2df02f3b]\n**Gap:** Jupiter\'s and Saturn\'s slices.\n**Ref:** gallery `data/objects_config.json`; L-231; L-322.\n\n#### [L-369] Earth\'s obliquity typed outside constants_new.py (orrery, store)\n<!-- L:369 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n- **Found 2026-09-22.** The obliquity is typed by hand in five places\n  that do not read the store row: `star_sphere_builder.py` line 46\n  (`OBLIQUITY_DEG = 23.4393`); visitor text saying "23.4" in\n  `palomas_orrery.py` lines 5835, 8066 and 8884; and\n  `coordinate_system_guide.py` line 441. [verified @a7868eee; the\n  manifest\'s line numbers were from an older tree]\n- The store row itself is used correctly everywhere it is read\n  (protocol v3.69\'s entry).\n**Gap:** Point each at the store row; the visitor text says "about 23.4" from the row.\n**Ref:** `constants_new.py`; `star_sphere_builder.py`; `palomas_orrery.py`; `coordinate_system_guide.py`.\n\n#### [L-368] Other bodies\' typed poles disagree with their cited table or cite a withdrawn report (orrery, store)\n<!-- L:368 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n- **Found 2026-09-22** measuring for L-322 Stage D (manifest section\n  2.5). In the typed `planet_poles` dict, Mercury\'s, Uranus\'s and\n  Neptune\'s entries disagree with the table they cite at the year 2000,\n  and the Moon\'s cites a report that withdrew it. Earth had the second\n  fault and is fixed. [per chain]\n- Horizons quantity 32 serves every body\'s pole of date from its own\n  rotation model, as Stage D now does for Earth. Fetching them retires\n  the typed dict and both faults with it.\n**Gap:** Each body\'s slice fetches its pole of date; the dict retires when the last one does.\n**Ref:** `idealized_orbits.py`; `documentation/BUILD_MANIFEST_L322_D_earth_pole_20260922.md` sec. 2.5 and 7; L-322.\n\n#### [L-367] No checker opens a new room (checks, gallery)\n')]


def split_index(text):
    if INDEX_START in text and INDEX_END in text:
        a = text.index(INDEX_START)
        b = text.index(INDEX_END) + len(INDEX_END)
        return text[:a] + text[b:]
    return text


def fingerprint(data):
    lf = data.replace(b"\r\n", b"\n")
    return hashlib.md5(split_index(lf.decode("utf-8")).encode("utf-8")
                       ).hexdigest()


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit(
            "ERROR: run this from the ORRERY repo ROOT, next to "
            "palomas_orrery.py -- not from documentation/. NOTHING was "
            "written.")
    if not os.path.isfile(LEDGER):
        raise SystemExit(
            "ERROR: %s is not here, so this is not the orrery root. "
            "NOTHING was written." % LEDGER)

    with open(LEDGER, "rb") as handle:
        raw = handle.read()
    got = fingerprint(raw)
    if got != BASE_OUTSIDE_INDEX:
        raise SystemExit(
            "ERROR: %s is not the file this patch was built against.\n"
            "       expected %s, found %s.\n"
            "       (The INDEX zone is excluded, so running "
            "ledger_index.py is not the cause.)\n"
            "       NOTHING was written. Undo is Discard Changes in "
            "GitHub Desktop." % (LEDGER, BASE_OUTSIDE_INDEX, got))

    is_crlf = raw.count(b"\r\n") > 0
    text = raw.decode("utf-8")
    applied = []
    for old, new in EDITS:
        o = old.replace("\n", "\r\n") if is_crlf else old
        n = text.count(o)
        if n != 1:
            raise SystemExit(
                "ANCHOR FAIL: expected 1 match in %s, found %d:\n  %r\n"
                "NOTHING was written." % (LEDGER, n, old[:70]))
        text = text.replace(o, new.replace("\n", "\r\n") if is_crlf else new)
        applied.append(old.strip().split("\n")[0][:56])

    with open(LEDGER, "wb") as handle:
        handle.write(text.encode("utf-8"))

    for line in applied:
        print("ok  %-24s %s" % (LEDGER, line))
    print("")
    print("patch applied (%d edits)" % len(EDITS))
    print("")
    print("NEXT:")
    print("  1. python ledger_index.py   (moves L-311, L-325, L-342 to C)")
    print("  2. python orrery_maintenance_run.py")
    print("     Expect 19 of 20 as before: 'Exact rows by the count'")
    print("     still fails until the gallery patch lands.")
    print("  3. Move this script into documentation/. Commit and push.")
    print("  4. Tell Claude the new orrery SHA.")


if __name__ == "__main__":
    main()
