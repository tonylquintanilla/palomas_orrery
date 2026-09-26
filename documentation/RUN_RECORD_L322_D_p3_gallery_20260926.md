# Run record -- L-322 Stage D, gallery patch 3: the magnetotail and the belts

**Built on gallery `c6000f03324fc6cdf1d192d0c1c77b91c10dd25f` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io and orrery
`43ba290b20ed17aee22a9bb7c121ff0b1a8fca3e` at
https://github.com/tonylquintanilla/palomas_orrery.** Both HEADs read live
with `git ls-remote` on 2026-09-26, at the start of the session and again
before the patch was written.

The patch is `patch_L322_D_p3_gallery_tail_belts_20260926.py`, run from the
gallery root and archived to the gallery's `documentation/`. It runs
before the orrery's patch D13 (see `RUN_RECORD_L322_D13_20260926.md`).

Rules this work ran under: protocol v3.69; provenance-discipline 2.19
(the loaded copy read 2.19, discharging v3.69's obligation),
interactive-exhibit 1.4, gallery-cache-builder 1.6, gallery-assembler 1.3,
safe-file-editing 1.11, agentic-pre-test 1.2, ledger-and-session-records
1.11. Every loaded copy was byte-identical to `skills/` at orrery
`43ba290b`.

Written for Tony, a retired professional engineer who is not a
programmer, and for the session that follows.

---

## 1. Rulings this session

- **The magnetotail is its own entry in the drawer** (Tony, 2026-09-26,
  option A of two). Option B, part of the Magnetopause row, would have left
  the tail's sources with nowhere to show in the i panel, which shows one
  row's sources, and GO on Magnetopause would have framed out to 220 Earth
  radii. Tony added: the two views, with the tail and without it, each get
  their own framing, which is what a separate row gives.
- **The words a visitor reads were shown to Tony before the build finished,
  and he said continue.** Two were shortened after that to fit the hover
  budget; section 4 names both.
- **The plan, with the orrery patch D13 added to it**, confirmed as
  recommended.

## 2. What the patch changes

- **`data/objects_config.json`.**
  - The `magnetotail` entry becomes a served shell: a name, a one-line
    description, an i-panel paragraph, a note, a source, a link, and
    pointer entries for the four tail rows (`flare_end`, `diameter`,
    `drawn_radius`, `drawn_end`) beside the existing `observed_extent`.
    Its colour and opacity are the magnetopause's, so the two read as one
    surface. `length_radii`, `base_radii`, `end_radii` and the old colour
    and opacity are gone; the `_declared` sentence is rewritten.
  - `observed_extent`'s source keeps only the reach; the 1983 abstract's
    figures for the end of widening and the diameter now sit with the 1985
    rows.
  - Earth's belts lose `belt_thickness` and `n_rings`; `_declared` says the
    ring count follows from the edge and peak rows.
  - The magnetic tilt's source sentence is corrected: the paper prints no
    tilt, the store computes it at five figures, and it shrinks by about
    0.049 degrees a year, not 0.05 per decade.
  - Earth's `orientation`: the pole's two numbers point at
    `EARTH_POLE_RA_J2000_DEG` and `EARTH_POLE_DEC_J2000_DEG` instead of
    `idealized_orbits.py`; the source names Horizons for the pole drawn
    and the IERS for the fallback, and says the IAU report was cited
    until today; a `rotation_period` pointer entry is added for
    `EARTH_SIDEREAL_ROTATION_PERIOD_H`.
  - The 14 `uncertainty` fields the mirror writes (section 3).
- **`gallery/feature_renderers.js`.**
  - The magnetotail, in `renderMagnetosphere`, drawn only if the
    magnetopause was. Its start is worked out from the served Shue rows at
    the served cut; rings run from there to the drawn end, with a ring
    added exactly at the flare end so the bend sits where the row puts it.
    It is stamped with its own shell key, `magnetotail`, so the arrival
    rule hides it on arrival like every other shell but the crust.
  - The belts: `evenBeltRings()`, the page's copy of the orrery's
    `_even_belt_rings()`, reading decimals to a thousandth as the orrery's
    `limit_denominator(1000)` does, capped at 25 rings. The peak ring is a
    second trace in the same drawer row, opacity 1.0 and twice the size;
    the info marker sits on it. A belt with no edges keeps a served
    thickness (Jupiter) or, with neither, is drawn as one ring with a
    warning. The 0.5 fallback is gone.
  - The magnetopause hover's sentence about where the drawing stops now
    says the boundary is drawn on as the magnetotail.
- **`gallery/earth_geometry.js`.** The axis hover states the period from
  the served row at its served count. Its panel source credits the sense
  of rotation to the IAU report's general definition (section 2, page 6)
  and its statement that Earth's rotation is direct (section 7, page 27),
  both read in the report this session, and adds the period's source. The
  module description no longer calls the frame angle the renderer's own
  IAU 2006 obliquity.
- **`tools/mirror_constants.py`.** `uncertainty` joins `value`, `unit` and
  `figures`. A null is never inserted, and an export before schema 4,
  which has no such key, leaves entries as they were.
- **`tools/test_mirror_constants.py`.** Case 17, the uncertainty field;
  case 18, Earth's pole served; case 9's link outside the store is
  Jupiter's pole now.
- **The three smoke checks.**
  - `smoke_earth_geometry.js` takes the magnetosphere and the period from
    the served cache, as it already took the pole of date, because the
    recorded payload predates them. It checks the tail as a shape (where it
    starts, where it bends, where it ends, round, the marker on it), the
    belts' rings against the orrery's answers, and the axis hover's period.
    Its `normal()` helper now picks three points that span a trace: with
    several rings in one trace, its old choice put three points on one
    radial line and read as a false 23-degree tilt.
  - `smoke_hover_budget.js` measures the room with the served
    magnetosphere, so the tail's hover is measured at all.
  - `smoke_display_figures.js` grades the tail line by line and the axis
    period against the served row, drops the retired sentences, and holds
    the rest to a re-recorded fixture,
    `documentation/fixture_hovers_L322d_p3_on_c6000f03.json`. The D7
    fixture is left in place, unreferenced.

## 3. How it was verified, in the sandbox

- **The whole gallery maintenance run: 16 of 16 gating checkers passed**,
  after the served cache's feature copies were refreshed from the config
  the way `derive_served()` copies them (the sandbox cannot reach
  Horizons; your real cache build replaces this step). The same result on
  a fresh clone of `c6000f03` with only the patch applied.
- **The patch reproduces the sandbox byte for byte** on a fresh clone,
  refuses a second run, and keeps CRLF on a working copy that has it.
- **Each new check was shown failing.** Tail radius off by one percent:
  four tail checks fail. Peak ring as faint as the others: both belts'
  peak checks fail. The axis sentence reworded: the period check fails.
  `uncertainty` removed from the mirror's fields: two mirror checks fail.
- **The mirror writes 14 fields and a second run writes none**: eight on
  Earth's radius (`"0.0001"`), the magnetopause's three coefficients, its
  standoff in Earth radii, kilometres and AU.
- **The exact-row print lines are unchanged.** `EXACT_ROWS_PRINTED.md` at
  orrery `43ba290b` lists ten gallery lines; after this patch the report
  still finds all ten with nothing broken. What it found new is section 5.
- **Hover sizes.** The tail's hover is 17 lines, at the ceiling; the outer
  belt's is 17; the axis hover's 17.
- **D5's cone cleanup** does not apply: the gallery draws no dipole cone,
  only the two spin-arrow heads on the axis.

## 4. The visitor-facing text

The magnetotail's hover, under its name:

    Earth's magnetic field, drawn out by the solar wind into a long tail on
    the night side.

    Spacecraft found the tail stops widening about 120 Earth radii behind
    Earth, plus or minus 10, and is about 60 Earth radii wide beyond there,
    plus or minus 5.
    That is about 770,000 km (0.0051 AU) and 380,000 km (0.0026 AU).
    The straight widening up to that point is our choice; the measurements
    give only its two ends.
    The drawing stops at 220 Earth radii, which is how far the spacecraft
    went, not where the tail ends.
    Drawn round, its average shape; at any moment it is often flattened.

The kilometre line was "... 770,000 km (0.0051 AU) behind Earth and
380,000 km (0.0026 AU) wide." when Tony saw it; "behind Earth" and "wide"
were dropped to bring the hover from 18 lines to the 17 allowed. The
sentence before it gives the order.

Its i-panel paragraph:

    The solar wind drags Earth's magnetic field out behind the planet into
    a long tail. Spacecraft crossing it far downstream found that it stops
    widening about 120 Earth radii behind Earth and is about 60 Earth radii
    across beyond there. ISEE-3 followed it out to 220 Earth radii, which
    is how far the spacecraft went rather than where the tail ends. The
    tail is drawn round, which is close to its shape on average; at any
    moment it is often flattened, in a direction set by the solar wind's
    own magnetic field, which keeps changing.

The belts' new sentence, both belts:

    The belt is one continuous region; its evenly spaced rings only mark its
    extent, and the brighter ring marks where it is most intense.

Tony saw a three-line version ("The belt is one continuous region. The
rings only mark its extent: they are evenly spaced from its inner edge to
its outer edge, and the brighter ring marks where the belt is most
intense."); it was shortened to two lines because the outer belt's hover
was 18. The edges it dropped are on the next lines of the same hover
("Measured extent: 3 to 7 Earth radii"). "Drawn 0.5 radii wide, a width
chosen for the picture." is gone.

The magnetopause's sentence: "That is where the drawing stops, not where
the surface ends: it widens down the tail without limit." became "Beyond
that angle the boundary is drawn as the magnetotail."

The axis hover: "This scene is one epoch: the axis is the line Earth turns
about; the turning itself is not shown, and no rotation period is stated
because none is served." became "Earth turns once every 23.93447 hours
measured against the stars. The turning is not animated, because nothing
on the crust marks a longitude to watch it by."

## 5. For the ledger, one row per class

- **Jupiter's belt thickness is a typed 0.5 with no source.** Served in
  `radiation_belts`, drawn by no room, and it has no edge rows to draw
  across. Waits for the braid; this build kept it rather than draw
  Jupiter's belts some new way unasked. The manifest and the previous
  handoff said "both `belt_thickness` entries"; this is the second one.
- **The recorded Earth scene is overlaid piece by piece.** Three checks now
  take the pole of date, the magnetosphere and the rotation period from
  the served cache because `documentation/payload_earth_scene.json` (a
  recording of 2026-09-08/09) predates them. It still carries the 9.6
  tilt and the old belt thickness. Extends the existing aging-payload row;
  a recapture would retire the overlays.
- **The tail's hover is at the line ceiling (17).** Anything added to it
  needs a line taken away.
- **There is no Wikipedia article for the magnetotail;** the link is the
  Magnetosphere article.

Carried, now done by this patch: L-311's gallery half; the axis period and
re-homed sources; the orientation source; the tilt sentence; the test at
line 373 (now case 9 and case 18); the mirror's docstring (three
`planet_poles` links).

## 6. Tony's run

(Append the patch output, the cache builder's last swap-log line, the
gallery maintenance run's summary, the live run, and what the phone
showed: the tail with and without framing, both belts, the axis hover, and
the Sun room.)

---

Session written September 2026 with Anthropic's Claude Opus 5.5.

===============================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L322_D_p3_gallery_tail_belts_20260926.py
  ok  data/objects_config.json: 18 edit(s)
  ok  gallery/feature_renderers.js: 17 edit(s)
  ok  gallery/earth_geometry.js: 6 edit(s)
  ok  tools/mirror_constants.py: 6 edit(s)
  ok  tools/test_mirror_constants.py: 8 edit(s)
  ok  documentation/smoke_earth_geometry.js: 8 edit(s)
  ok  documentation/smoke_hover_budget.js: 1 edit(s)
  ok  documentation/smoke_display_figures.js: 10 edit(s)
  ok  documentation/fixture_hovers_L322d_p3_on_c6000f03.json: new file (18843 bytes)
  ok  stamps: 'Module updated' / 'Updated' lines added to
      feature_renderers.js, earth_geometry.js, mirror_constants.py,
      test_mirror_constants.py and the three smoke checks

PATCH APPLIED

NEXT STEPS, in this order
  1. Pause OneDrive syncing, and note the time (a pause lasts
     2 hours).
  2. Run the cache builder: open tools/gallery_cache_builder.py and
     click Run, from the gallery repo root, or use the dashboard's
     button. The config changed, so nothing reaches a visitor until
     this has run.

[RECOVER] removed retained data\solar-system.prev (cleared read-only on 6 entries)
[sweep] no sibling directories present
[POLE] earth: pole of 2026-09-26 served (RA 0.72394, Dec 89.85020 deg); tilt 23.43816 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[done] run 20260926T213000Z (nightly): 13 objects

----------------------------------------------------------------------
WHAT TO DO NEXT, before you commit anything:

  1. Run the gallery maintenance run, from this same folder:
         python gallery_maintenance_run.py
     Every gating checker should pass. Its LAST line reads the
     swap log back and should agree with the [SWAP] line above.
  2. In GitHub Desktop, look at the change list. A good build
     shows changed and added files and NO pile of deletions.
  3. Commit and push.
  4. After the push, check what the live site serves:
         python gallery_maintenance_run.py --live

TONY-ACTION ROLLUP for this run:
  (do)     steps 1 to 4 above, in that order.
----------------------------------------------------------------------

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>


  3. Read the last line of data/cache_swap_log.jsonl: the swap
     should say it succeeded.

{"attempts": {"live_to_prev": 1, "staging_to_live": 1}, "error": null, "mode": "nightly", "outcome": "ok", "reached": "staging_to_live", "run_id": "20260926T213000Z", "time": "2026-09-26T21:30:02.295547+00:00"}

  4. Run gallery_maintenance_run.py with the Run button. All 16
     gating checkers should pass. A red 'Cache in step' means
     step 2 has not happened.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.6s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     0.9s  rewrote data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      11.2s  PASS (210 checks, 0 failures)
  PASS Pole of date              0.2s  POLE OF DATE: all 11 checks passed
                                    (frame angle, orrery, ERFA, block
                                    checker, and each shown able to
                                    fail).
  PASS Mirror suite              0.1s  All 51 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing,
                                    uncertainty written as served,
                                    Earth's pole served.
  PASS Store writer suite        4.5s  All 251 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 252 store-editor checks
                                    passed: every box the form offers
                                    is one the writer allows; the word
                                    list and the tick list differ by
                                    the belts, on purpose; nothing
                                    typed saves nothing; the save
                                    message does not promise a visitor
                                    sees what they cannot yet; and a
                                    red Cache in step is explained
                                    rather than just shown.
  PASS Config mirror check       0.1s  Every served link holds the
                                    export's value, unit and figure
                                    count; 65 link(s) compared, store
                                    a2d6b97d161e.
  PASS Pointer join              0.1s  Every link is accounted for: 93
                                    link(s) against orrery 43ba290b,
                                    24 fallback named; read check: 43
                                    of 43 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's features exactly: 4
                                    object(s), 35 named shell(s), in
                                    both cache files.
  PASS Feature renderers         1.0s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.2s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.2s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.3s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 57 hover(s) and 288
                                    number(s) examined; 13 graded, 5
                                    graded by line, 44 held to the
                                    fixture ===
  PASS Artifact 1 assembler      0.3s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: no sibling directories and
                                    nothing in data/ the builder did
                                    not make.

======================================================================
  16 of 16 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: no sibling directories and
  last swap 2026-09-26T21:30:02.295547+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  5. Now the orrery: save patch_L322_D_13_exact_rows_drawn_20260926.py
     in the orrery root, run it, 
     
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L322_D_13_exact_rows_drawn_20260926.py
  ok  exact_rows_report.py: 15 edit(s)
  ok  documentation/RUN_RECORD_L322_D13_20260926.md: new file (3437 bytes)
  ok  documentation/RUN_RECORD_L322_D_p3_gallery_20260926.md: new file (11959 bytes)
  ok  stamps: the module history line added to exact_rows_report.py

PATCH APPLIED

NEXT STEPS
  1. Run orrery_maintenance_run.py with the Run button. Its 'Exact
     rows report' line should say '4 drawn only, 0 not followed,
     0 map entries broken'. If it says 4 not followed, gallery
     patch 3 has not run in the gallery folder beside the orrery.

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20260926T183557Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.0s  unchanged (1 of 1 rewritten, content
                                     identical)
  Skill manifest               0.1s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             0.6s  unchanged (1 checked, not written)
  Module atlas                 6.9s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               5.0s  rewrote DATA_INVENTORY.md
  Exact rows report            0.9s  rewrote EXACT_ROWS_PRINTED.md -- 7 of 20
                                     exact rows printed at 18 lines (8 orrery, 10
                                     gallery); 4 drawn only, 0 not followed, 0
                                     map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.2s  No changes to constants_new.py since HEAD.
  Constants relations          0.2s  21 of 21 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.7s  No figure count exceeds its inputs: 41
                                     derived row(s) read, 28 judged OK -- 28 OK,
                                     13 NOT YET MIGRATED, 1 NO DERIVED LINE.
  Constants export check       1.3s  Export matches the store: sha256
                                     a2d6b97d161e on both sides; 85 rows re-read,
                                     54 not exported, 26 tokens.
  Dimensions                   1.1s  No unit contradicts its arithmetic: 41
                                     derived row(s) read -- 28 OK, 10 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.1s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.2s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 87 status lines in constants_new.py are
                                     well formed; 49 rows carry none.
  Row shape                    0.1s  All 139 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.3s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          16.3s  PASS -- all 309 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  1.6s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker            8.8s  76 of 114 routed, 8 clean
  Worksheet checker tests     13.6s  All 136 checks passed
  Worksheet key round trip     0.8s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         17.1s  All 76 checks passed
  Extractor pins               0.3s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner          13.9s  295 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  17 of 17 gating checkers passed -- 91.4s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           76 of 114 routed, 8 clean
    Provenance scanner          295 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  1983 file(s) examined, 8 written, 0 created, 0 removed, 5 rewritten identically
    written   DATA_INVENTORY.md
    written   EXACT_ROWS_PRINTED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      LEDGER_CONSOLIDATED.md
      PROJECT_INSTRUCTIONS.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  2. Move this script into documentation/. Commit the orrery,
     with the rewritten EXACT_ROWS_PRINTED.md, and push. -- 56c4b30e430bda1d2f621aa3bfb9678ac769dcd9
  3. Append your run to the two new run records in documentation/.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

     then run orrery_maintenance_run.py.
     Its 'Exact rows report' line should say '4 drawn only,
     0 not followed, 0 map entries broken'.

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20260926T213640Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 0.9s  unchanged (1 of 1 rewritten, content
                                     identical)
  Skill manifest               0.1s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             0.6s  unchanged (1 checked, not written)
  Module atlas                 5.8s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               3.8s  unchanged (1 of 1 rewritten, content
                                     identical)
  Exact rows report            0.7s  unchanged (1 checked, not written) -- 7 of
                                     20 exact rows printed at 18 lines (8 orrery,
                                     10 gallery); 4 drawn only, 0 not followed, 0
                                     map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.2s  No changes to constants_new.py since HEAD.
  Constants relations          0.2s  21 of 21 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.5s  No figure count exceeds its inputs: 41
                                     derived row(s) read, 28 judged OK -- 28 OK,
                                     13 NOT YET MIGRATED, 1 NO DERIVED LINE.
  Constants export check       0.9s  Export matches the store: sha256
                                     a2d6b97d161e on both sides; 85 rows re-read,
                                     54 not exported, 26 tokens.
  Dimensions                   0.8s  No unit contradicts its arithmetic: 41
                                     derived row(s) read -- 28 OK, 10 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.1s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.1s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 87 status lines in constants_new.py are
                                     well formed; 49 rows carry none.
  Row shape                    0.1s  All 139 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.2s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          10.5s  PASS -- all 309 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  1.5s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker            8.2s  76 of 114 routed, 8 clean
  Worksheet checker tests     13.8s  All 136 checks passed
  Worksheet key round trip     0.8s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         16.9s  All 76 checks passed
  Extractor pins               0.3s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner           8.2s  295 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  17 of 17 gating checkers passed -- 75.9s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           76 of 114 routed, 8 clean
    Provenance scanner          295 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  1983 file(s) examined, 6 written, 0 created, 0 removed, 6 rewritten identically
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      DATA_INVENTORY.md
      LEDGER_CONSOLIDATED.md
      PROJECT_INSTRUCTIONS.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  6. Move this script into the gallery's documentation/ folder.
     Commit the gallery (config, cache, code, fixture, this
     script) and push. Commit and push the orrery.

-- gallery moved to 93d8ae9caead6ab801d854b46fae5b297747fc6c
-- orrery moved to e21d9dd9b185996995a90a0e53b589c84d7932d3

  7. Run python gallery_maintenance_run.py --live once the site
     has updated.

======================================================================
  gallery maintenance run -- LIVE (after a push)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

LIVE -- what the deployed site actually serves

  fetching 11 files from https://palomasorrery.com/
    SERVED   interactive.html                               matches the working copy
    SERVED   gallery/feature_renderers.js                   matches the working copy
    SERVED   gallery/earth_geometry.js                      matches the working copy
    SERVED   gallery/assembler/resolver.py                  matches the working copy
    SERVED   gallery/assembler/__init__.py                  matches the working copy
    SERVED   data/solar-system/coverage_index.json          matches (the working copy is CRLF)
    SERVED   data/solar-system/feature_configs.json         matches (the working copy is CRLF)
    SERVED   data/solar-system/positions/voyager_1.json     matches the working copy
    SERVED   gallery/arrival.js                             matches the working copy
    SERVED   gallery/nav_cluster.js                         matches the working copy
    SERVED   data/objects_config.json                       matches the working copy

  PASS Served reachability       1.5s  all 11 files served and
                                    byte-identical to the working copy

  orrery export pinned at 43ba290b

  PASS Export freshness          0.1s  the served export is the orrery's
                                    at 43ba290b, byte for byte

  orrery HEAD e21d9dd9
  examining 28 of 93 links; the other 65 are served from the export
    NOT IN STORE  create_sun_galactic_tide default not a top-level constant in the store
                  /objects/0/features/oort_cloud/galactic_tide/typical_radius
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  28 pointers: 24 match, 0 DRIFT, 0 UNIT MISMATCH, 4 could not be examined.

  PASS Store drift               1.0s  28 pointers against orrery
                                    e21d9dd9 -- 24 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 4 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            28 pointers against orrery e21d9dd9 --
  last swap 2026-09-26T21:30:02.295547+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  8. On your phone, in the Earth room: tick Magnetotail in the
     drawer and tap GO. The tail should run from the back of the
     magnetopause out to about 220 Earth radii, widening and then
     straight, in the magnetopause's colour; tap its cross for the
     hover. -- correct
     
     Tick each radiation belt: evenly spaced rings with one
     brighter, larger ring. -- correct
     
     Tap the rotation axis: the hover gives
     23.93447 hours. -- correct
     
     Then open the Sun room; it should look as it
     did. --correct
     
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

