<!-- Doc-Kind: hand | Session record for the Solar System room, Half 2 steps 1 to 3a (L-363), 2026-09-30 and 10-01. -->
# HANDOFF -- L-363 Half 2: design closed, five planets and Pluto served, room step 3a live

Built on orrery 10012821cf6289095912c0a5f2a0ae86d26ce1e1 at
https://github.com/tonylquintanilla/palomas_orrery, and gallery
0f513fd5d8ad2ce1e3ba5f19ea2f44388484690e at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Gallery pushed at 1530bb6d (step 2), f6d1ca95 (L-397), 432435a8 (step 3a).
Orrery: this record lands with the closing patch
patch_L363_ledger_half2_step3a_20260930.py.

Type: BUILD.
Supersedes: nothing. Companion to
HANDOFF_L363_three_strands_integrated_20260929.md (whose section 4 this
session carried out, and to whose local copy Tony appended the run
records of this session's patches).

Session written October 2026 with Anthropic's Claude Opus 5.5.

## 1. Skills at session start

All loaded copies matched the manifest: ledger-and-session-records
1.13 (the obligation from v3.74 is discharged), interactive-exhibit 1.6,
provenance-discipline 2.22, gallery-cache-builder 1.6, safe-file-editing
1.11, agentic-pre-test 1.2, orrery-coding-conventions 1.9,
horizons-orbital-mechanics 1.1. No skill was bumped this session; the
bumps this session's rulings need travel with L-398's build (section 6).

## 2. Rulings, in Tony's words where he gave them

- Ticking a planet in the drawer also opens its row: yes.
- Apophis keeps one row, under See more, until the near-Earth asteroids
  get their own design: yes.
- The room's settings are served, in a new top-level "rooms" section of
  data/objects_config.json: "confirmed as recommended". Every reader of
  the file (builder, assembler, both writers, the checks) reads only
  "objects"; checked before recommending.
- Home's tick order lives only in the open tab: "No stored information
  between sessions locally."
- Pluto in the Sun-centred room is the Pluto-Charon barycentre (Horizons
  9 @sun), by the barycentre rule; named "Pluto": "confirmed". Hover
  sentence, Tony's wording: "The symbol marks the gravitational center
  (barycenter) that Pluto and its moon Charon orbit together. It lies
  outside Pluto itself."
- Words: "See more" / "See fewer"; "Enter the Sun room" / "Enter the
  Earth room"; "No room or cards yet"; distances written out, not in
  exponent form; the x, y, z line dropped; the panel's Explorer sentence
  dropped ("the explorer will remain but not as a featured card").
- Source line: "Horizons id: 199", not "target"; "measured from the
  Sun's centre"; the date written out with the Julian date in brackets.
  Standing rule: "spell out JD, Julian date, the first time it is named
  in a card. i think that it is okay to use actual names as long as
  they are explained not just short hand."
- Figures: "use the actual sig figs"; then, confirmed, each distance
  prints the figures its measured error earns at the minute drawn, as a
  rule for every computed position (provenance skill). Then, on Tony's
  question about Pluto, the source's own accuracy enters: use whichever
  is larger (L-398, confirmed 2026-10-01), JPL's three groups as the
  source accuracy, Apophis keeps its distance with one line saying JPL's
  own uncertainty is not yet included (Tony: "We have been computing it
  all along from Horizons ephemeris").
- Descriptions and links: from the orrery's object dictionary, standard
  and in the skill; Pluto's row uses NASA's Pluto page (L-395).
- Work order, confirmed: the figures fix, then the dictionary export,
  then step 3b.
- L-397 "on a priority basis".
- From Tony's notes on Where We Are: the Sun's opening view in the orrery
  is "photosphere + 10%" (L-385); Earth's atmosphere "depends on the
  source. Re is based on the equatorial radius. The crust is ~0.99...
  Re" (L-389).

## 3. What was built, verified

| Patch | Repo | Pushed | Verified |
|---|---|---|---|
| patch_L363_7_half2_config_20260930.py | gallery | 1530bb6d | Tony's run: offline suite, six dry runs, first build, the six objects in the cache with their own windows covering today; read back live (all six @sun, ecliptic inclinations). Whole cache now trusted +/- 88 days (Mercury). |
| patch_L397_cache_in_step_all_objects_20260930.py | gallery | f6d1ca95 | Tony's run: 19 of 19 gating checks. In the sandbox: fails against the pre-build cache naming the six new bodies; self-test catches a broken comparison. |
| patch_L363_8_room_step3a_20260930.py | gallery | 432435a8 | Tony's run: all checks pass. Room's driver run in CPython on the real cache, compose run in Node: no warnings. NOT run in a browser by Claude; Tony viewed it live. |

## 4. Found this session

- The cache-in-step blind spot (L-397, fixed).
- The orbit cross's text box gave the distance of an arbitrary point on
  the orbit in exponent form; the word list had missed it. It now says
  "Mercury's orbit" (Tony may reword).
- Distance figures overclaim for the outer bodies (L-398, next).
- Three entries in OBJECT_DEFINITIONS had a field written twice (Earth,
  Moon, Patroclus-Menoetius Barycenter), the first silently discarded by
  Python and invisible to the provenance scanner. Tony fixed them by
  hand on 2026-10-01; not yet pushed when this was written. The export
  (L-395) gets a duplicate-field check.
- A stray folder data/solar-system (1) in Tony's gallery copy (L-400).

## 5. Discrepancies

- None between handoff and base: step 0 of the previous handoff had
  landed (L-363 updated, L-391 to L-396 present, plan v35).

## 6. Next session

1. Confirm the orrery HEAD carries this closing patch and Tony's
   dictionary fix (no entry in celestial_objects.py with a duplicated
   field).
2. L-398, the figures fix:
   - orrery: three rows in constants_new.py, citing Folkner et al. 2014
     (IPN Progress Report 42-196, abstract), stating each group's
     accuracy as the place the source names; provenance-discipline gains
     the computed-position rule and the "accuracy stated in words" case;
     exported.
   - gallery: each served object points at its group's row
     (orrery_constant, mirrored); the page uses the larger of drift and
     source accuracy; Apophis's line; interactive-exhibit records the
     rooms section and served row words (label, about, source_note).
3. L-395, the dictionary export (descriptions, NASA links, the
   duplicate check).
4. L-363 step 3b, the drawer, then Tony's phone check.

## 7. Tony-actions, rolled up

- (do) Run patch_L363_ledger_half2_step3a_20260930.py from the orrery
  root; then orrery_maintenance_run.py; commit together with the
  dictionary fix; push.
- (do) Look inside data/solar-system (1) in the gallery copy, then
  delete it (L-400).
- (decide, optional) Reword the orbit crosses if wanted.

============================================================

================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L363_ledger_half2_step3a_20260930.py
ok  LEDGER_CONSOLIDATED.md  header stamp
ok  LEDGER_CONSOLIDATED.md  L-397 to L-400 added
ok  LEDGER_CONSOLIDATED.md  L-395 note
ok  LEDGER_CONSOLIDATED.md  L-392 done
ok  LEDGER_CONSOLIDATED.md  L-389 Tony note
ok  LEDGER_CONSOLIDATED.md  L-385 Tony note
ok  LEDGER_CONSOLIDATED.md  L-363 session bullet
ok  documentation/WHERE_WE_ARE.md  rewritten
ok  documentation/HANDOFF_L363_half2_step3a_20260930.md  new

Stamps updated: the ledger's header line; Where We Are's date.
patch applied

NEXT:
  1. python orrery_maintenance_run.py  (rebuilds the ledger index)

======================================================================
  DAILY RUN -- Thursday October 01, 2026  10:59
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io
======================================================================
Daily Run steps, from C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io:
  1. Guest book updater                 tools\guestbook_updater.py  found
  2. Cache builder                      tools\gallery_cache_builder.py  found
  3. Gallery maintenance run, offline   gallery_maintenance_run.py  found
=== DAILY RUN: all 3 step scripts found
Last cache build: 2026-09-30 22:24 UTC, ok, 0 days ago.

======================================================================
  DAILY RUN step 1 of 3: Guest book updater
======================================================================
======================================================================
  guest book updater -- C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io
======================================================================
1 entry in the guest book; 172 gallery pages a link may point at.

Fetching the form's responses...
No new messages.

w write, r reply, x remove, p pin/unpin, f form address, s sheet address, q finish > q

======================================================================
  approved 0, declined 0, waiting 0; the guest book now has 1 entry
  No change to data/guestbook.json.
======================================================================

======================================================================
  Before the cache build: PAUSE ONEDRIVE and note the time.
  (OneDrive icon in the taskbar > Pause syncing > 2 hours.)
======================================================================
Press Enter when OneDrive is paused, or type s to skip the build today >
OneDrive paused at 10:59; the pause lasts until about 12:59.

======================================================================
  DAILY RUN step 2 of 3: Cache builder
======================================================================
[RECOVER] removed retained data\solar-system.prev (cleared read-only on 6 entries)
[sweep] kept 6 recent sibling(s) as autopsies: .staging_solar-system_mars_20260930T222412Z, .staging_solar-system_mercury_20260930T222405Z, .staging_solar-system_neptune_20260930T222418Z, .staging_solar-system_pluto_barycenter_20260930T222422Z, .staging_solar-system_uranus_20260930T222415Z, .staging_solar-system_venus_20260930T222409Z
[POLE] earth: pole of 2026-10-01 served (RA 0.69797, Dec 89.85017 deg); tilt 23.43808 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[done] run 20261001T160000Z (nightly): 19 objects

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

The builder's next steps start with the maintenance run.
The Daily Run runs it now.

======================================================================
  DAILY RUN step 3 of 3: Gallery maintenance run, offline
======================================================================
======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.6s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     1.1s  no change to
                                    data/constants_export.json,
                                    data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      17.3s  PASS (229 checks, 0 failures)
  PASS Pole of date              0.2s  POLE OF DATE: all 11 checks passed
                                    (frame angle, orrery, ERFA, block
                                    checker, and each shown able to
                                    fail).
  PASS Mirror suite              0.1s  All 64 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing,
                                    uncertainty written as served,
                                    Earth's pole served, print count
                                    written as served, "in" written as
                                    served and a slot served in
                                    another unit from it.
  PASS Store writer suite        6.0s  All 251 store-writer checks
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
                                    b6d8bfdb21f6.
  PASS Pointer join              0.1s  Every link is accounted for: 89
                                    link(s) against orrery 10012821,
                                    20 fallback named; read check: 43
                                    of 43 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's 19 object(s) and their
                                    features exactly: 4 object(s) with
                                    35 named shell(s), in both cache
                                    files.
  PASS Feature renderers         0.9s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.2s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.2s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 57 hover(s) and 296
                                    number(s) examined; 13 graded, 7
                                    graded by line, 44 held to the
                                    fixture ===
  PASS Guest book                0.1s  === GUEST BOOK: all 8 checks
                                    passed
  PASS Guest book updater        0.2s  === GUEST BOOK UPDATER: all 43
                                    checks passed (6 scripted runs,
                                    self-test first)
  PASS Daily run steps           0.1s  === DAILY RUN: all 3 step scripts
                                    found
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: 1 directory in data/ the
                                    builder did not make: solar-system
                                    (1). Check whether they belong
                                    there; the newer .gitignore rules
                                    keep the known conflict-copy
                                    shapes out of git but do not
                                    remove anything.

======================================================================
  19 of 19 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: 1 directory in data/ the builder
  last swap 2026-10-01T16:00:33.623388+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

======================================================================
  DAILY RUN -- summary
======================================================================
  Guest book updater           ok
  Cache builder                ok
  Maintenance run, offline     ok

  NEXT:
    1. GitHub Desktop: look at the change list, then commit and push.
    2. Then the dashboard's Gallery Maintenance Run -- live, AFTER a push.
    3. Resume OneDrive.
======================================================================

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20260930T161829Z, 1 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.3s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.1s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             0.7s  unchanged (1 checked, not written)
  Module atlas                 7.0s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               5.3s  rewrote DATA_INVENTORY.md
  Exact rows report            1.3s  unchanged (1 checked, not written) -- 8 of
                                     21 exact rows printed at 19 lines (9 orrery,
                                     10 gallery); 5 drawn only, 0 not followed, 0
                                     map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.2s  No changes to constants_new.py since HEAD.
  Constants relations          0.2s  21 of 21 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.6s  No figure count exceeds its inputs: 29
                                     derived row(s) read, 17 judged OK -- 17 OK,
                                     12 NOT YET MIGRATED, 1 NO DERIVED LINE, 1
                                     UNMARKED CONVERSION; 15 conversion(s)
                                     checked.
  Constants export check       0.9s  Export matches the store: sha256
                                     b6d8bfdb21f6 on both sides; 76 rows re-read,
                                     66 not exported, 26 tokens; 160 conversions
                                     re-computed, 10 of 10 worked cases hold.
  Exact rows by the count      1.0s  PASSING -- 8 printed exact rows each state a
                                     count; 9 orrery lines print through
                                     exact_text(); 10 gallery lines are served
                                     the count
  Dimensions                   0.9s  No unit contradicts its arithmetic: 44
                                     derived row(s) read -- 32 OK, 9 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.1s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.1s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 78 status lines in constants_new.py are
                                     well formed; 61 rows carry none.
  Row shape                    0.1s  All 142 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.2s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          20.6s  PASS -- all 309 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  2.2s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker            8.5s  76 of 114 routed, 8 clean
  Worksheet checker tests     16.2s  All 136 checks passed
  Worksheet key round trip     1.0s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         22.9s  All 76 checks passed
  Extractor pins               0.5s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner          11.3s  296 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  18 of 18 gating checkers passed -- 103.6s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           76 of 114 routed, 8 clean
    Provenance scanner          296 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2017 file(s) examined, 8 written, 1 created, 1 removed, 5 rewritten identically
    written   DATA_INVENTORY.md
    written   LEDGER_CONSOLIDATED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    created   documentation/patch_L363_ledger_half2_step3a_20260930.py
    removed   patch_L363_ledger_half2_step3a_20260930.py
    rewritten with identical bytes, no action needed:
      PROJECT_INSTRUCTIONS.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      documentation/HANDOFF_L363_three_strands_integrated_20260929.md
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  2. Move this script into documentation/.
  3. Commit with your celestial_objects.py fix, and push. -- 7a47269c09acd4d2f875f6c8d49070659c4c2ee9
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

========================================================================================

Now the mirror, with the new export, then every gallery check.Now the skill and protocol text.The figures fix is built: two patches, one for each repo, tested in my sandbox.

**Run them in this order:**
1. **The orrery patch, `patch_L398_1_accuracy_rows_and_skills_20261001.py`.** Run it in the orrery folder, then the orrery maintenance run. Then commit and push.
   - Between the two patches, the maintenance run's Exact rows report will say "1 map entries broken". That is expected, and it clears once the website patch has run.
   - Then reinstall `provenance-discipline` and `interactive-exhibit` from `skills/` in Settings > Skills.
   - Then replace the Project's instructions with the new `PROJECT_INSTRUCTIONS.md`.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L363_ledger_tony_notes_20261001.py
ok  LEDGER_CONSOLIDATED.md  header stamp
ok  LEDGER_CONSOLIDATED.md  L-400 done
ok  LEDGER_CONSOLIDATED.md  L-400 body
ok  LEDGER_CONSOLIDATED.md  L-398 Tony note
ok  LEDGER_CONSOLIDATED.md  L-396 goal line and 1.13
ok  LEDGER_CONSOLIDATED.md  L-396 date
ok  LEDGER_CONSOLIDATED.md  L-389 decide struck
ok  LEDGER_CONSOLIDATED.md  L-389 Tony note
ok  LEDGER_CONSOLIDATED.md  L-363 front door and orbit marker
ok  documentation/WHERE_WE_ARE.md  rewritten

Stamps updated: the ledger's header line; Where We Are's date.
patch applied

NEXT:
  1. python orrery_maintenance_run.py  (rebuilds the ledger index,
     and moves L-400 into the closed section)
  2. Move this script into documentation/.
  3. Commit and push.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L398_1_accuracy_rows_and_skills_20261001.py
ok  PROJECT_INSTRUCTIONS.md                        header v3.75, cut from 7a47269c
ok  PROJECT_INSTRUCTIONS.md                        version history: v3.75 entry
ok  PROJECT_INSTRUCTIONS.md                        version history: v3.72 moved down
ok  constants_new.py                               three DE430 accuracy rows (L-398)
ok  documentation/PROJECT_INSTRUCTIONS_HISTORY.md  PART 1: v3.72 received
ok  exact_rows_report.py                           DRAWN: position_accuracy, read to set a print place (L-398)
ok  skills/interactive-exhibit/SKILL.md            version line 1.6 -> 1.7, with the v1.7 paragraph
ok  skills/interactive-exhibit/SKILL.md            Provenance: a computed distance and position_accuracy
ok  skills/interactive-exhibit/SKILL.md            Served: the rooms section
ok  skills/interactive-exhibit/SKILL.md            Logic in its own file: the second instance
ok  skills/provenance-discipline/SKILL.md          version line 2.22 -> 2.23
ok  skills/provenance-discipline/SKILL.md          v2.23 paragraph in the header
ok  skills/provenance-discipline/SKILL.md          new section: A Computed Position Prints What Its Errors Earn
ok  documentation/project_instructions_v3_75.md    created

Stamps updated: provenance-discipline 2.23, interactive-exhibit
1.7, the protocol's header (v3.75, cut from 7a47269c).

patch applied (13 edits in 6 files, 1 new files)

NEXT:
  1. python orrery_maintenance_run.py -- it exports the three new
     rows and rebuilds the skill manifest (2.22 -> 2.23, 1.6 -> 1.7).
     Its Exact rows report will say "1 map entries broken" until the
     gallery patch has run. That is expected.

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261001T160421Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 0.9s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.1s  rewrote PROJECT_INSTRUCTIONS.md
  Constants export             1.1s  rewrote data/constants_export.json
  Module atlas                 5.6s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               4.5s  rewrote DATA_INVENTORY.md
  Exact rows report            1.3s  rewrote EXACT_ROWS_PRINTED.md -- 8 of 24
                                     exact rows printed at 19 lines (9 orrery, 10
                                     gallery); 5 drawn only, 0 not followed, 1
                                     map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.3s  0 removal verdict(s) cross-checked against
                                     the 145 name(s) the working copy assigns
  Constants relations          0.2s  21 of 21 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.6s  No figure count exceeds its inputs: 29
                                     derived row(s) read, 17 judged OK -- 17 OK,
                                     12 NOT YET MIGRATED, 1 NO DERIVED LINE, 1
                                     UNMARKED CONVERSION; 15 conversion(s)
                                     checked.
  Constants export check       1.0s  Export matches the store: sha256
                                     089a5baf0101 on both sides; 79 rows re-read,
                                     66 not exported, 26 tokens; 172 conversions
                                     re-computed, 10 of 10 worked cases hold.
  Exact rows by the count      1.1s  PASSING -- 8 printed exact rows each state a
                                     count; 9 orrery lines print through
                                     exact_text(); 10 gallery lines are served
                                     the count
  Dimensions                   1.0s  No unit contradicts its arithmetic: 44
                                     derived row(s) read -- 32 OK, 9 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.1s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.1s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 81 status lines in constants_new.py are
                                     well formed; 61 rows carry none.
  Row shape                    0.1s  All 145 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.2s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          16.5s  PASS -- all 309 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  1.5s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker            7.3s  76 of 114 routed, 8 clean
  Worksheet checker tests     13.1s  All 136 checks passed
  Worksheet key round trip     0.8s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         17.1s  All 76 checks passed
  Extractor pins               0.3s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner           8.4s  296 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  18 of 18 gating checkers passed -- 83.6s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           76 of 114 routed, 8 clean
    Provenance scanner          296 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2020 file(s) examined, 11 written, 0 created, 0 removed, 3 rewritten identically
    written   DATA_INVENTORY.md
    written   EXACT_ROWS_PRINTED.md
    written   LEDGER_CONSOLIDATED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROJECT_INSTRUCTIONS.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/constants_export.json
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  2. Move this script into documentation/. Commit and push. -- done
  3. Reinstall provenance-discipline and interactive-exhibit from
     skills/ to Settings > Skills. -- done
  4. Replace the Project's instructions in claude.ai with the new
     PROJECT_INSTRUCTIONS.md. -- done
  5. Then the gallery patch, patch_L398_2, which needs this push. -- c12994d27e6205371cd463b1b535afd0a2f4dd17
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

2. **The website patch, `patch_L398_2_distance_figures_20261001.py`.** Run it only after the orrery push, because the website fetches the new rows from GitHub. Then the gallery maintenance run, commit and push, then the live check.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L398_2_distance_figures_20261001.py
ok  data/objects_config.json       nine position_accuracy links, as the mirror writes them
ok  gallery_maintenance_run.py     checker row: Solar System figures
ok  gallery_maintenance_run.py     served files: gallery/solar_system_figures.js
ok  interactive.html               header: L-398 update line
ok  interactive.html               script tag: solar_system_figures.js
ok  interactive.html               driver: pass each body's position_accuracy
ok  interactive.html               compose: distance line from the file, and the sentence
ok  interactive.html               figures helpers moved out to gallery/solar_system_figures.js
ok  gallery/solar_system_figures.js new
ok  documentation/smoke_solar_system_figures.js new

patch applied

NEXT:
  1. python gallery_maintenance_run.py -- it pulls the orrery's new
     export first. Every gating checker should pass, including the
     new one, "Solar System figures", which prints each body's
     distance and what set its figures.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.2s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     1.4s  rewrote
                                    data/constants_export.json,
                                    data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      12.8s  PASS (229 checks, 0 failures)
  PASS Pole of date              0.2s  POLE OF DATE: all 11 checks passed
                                    (frame angle, orrery, ERFA, block
                                    checker, and each shown able to
                                    fail).
  PASS Mirror suite              0.1s  All 64 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing,
                                    uncertainty written as served,
                                    Earth's pole served, print count
                                    written as served, "in" written as
                                    served and a slot served in
                                    another unit from it.
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
                                    count; 74 link(s) compared, store
                                    089a5baf0101.
  PASS Pointer join              0.1s  Every link is accounted for: 98
                                    link(s) against orrery c12994d2,
                                    20 fallback named; read check: 43
                                    of 43 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's 19 object(s) and their
                                    features exactly: 4 object(s) with
                                    35 named shell(s), in both cache
                                    files.
  PASS Feature renderers         1.1s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.1s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.1s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.1s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 57 hover(s) and 296
                                    number(s) examined; 13 graded, 7
                                    graded by line, 44 held to the
                                    fixture ===
  PASS Solar System figures      0.1s  === PASS: 6 worked cases, 11
                                    drawer rows matched to their
                                    accuracy rows, 10 served
                                    distances; Uranus, Neptune and
                                    Pluto print to JPL's ten-thousands
                                    place ===
  PASS Guest book                0.1s  === GUEST BOOK: all 8 checks
                                    passed
  PASS Guest book updater        0.2s  === GUEST BOOK UPDATER: all 43
                                    checks passed (6 scripted runs,
                                    self-test first)
  PASS Daily run steps           0.1s  === DAILY RUN: all 3 step scripts
                                    found
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: 6 sibling(s), none stale,
                                    and nothing in data/ the builder
                                    did not make. The sweep is keeping
                                    up.

======================================================================
  20 of 20 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: 6 sibling(s), none stale, and
  last swap 2026-10-01T16:00:33.623388+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  2. Move this script into documentation/. Commit and push. -- done 58dd8f25ad7f3c01a2e4b03497abaa5091081f98
  3. python gallery_maintenance_run.py --live

======================================================================
  gallery maintenance run -- LIVE (after a push)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

LIVE -- what the deployed site actually serves

  fetching 14 files from https://palomasorrery.com/
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
    SERVED   gallery/solar_system_figures.js                matches the working copy
    SERVED   data/objects_config.json                       matches the working copy
    SERVED   gallery/guestbook.js                           matches the working copy
    SERVED   data/guestbook.json                            matches the working copy

  PASS Served reachability       2.6s  all 14 files served and
                                    byte-identical to the working copy

  orrery export pinned at c12994d2

  PASS Export freshness          0.1s  the served export is the orrery's
                                    at c12994d2, byte for byte

  orrery HEAD c12994d2
  examining 24 of 98 links; the other 74 are served from the export
    NOT IN STORE  create_sun_galactic_tide default not a top-level constant in the store
                  /objects/0/features/oort_cloud/galactic_tide/typical_radius
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  24 pointers: 20 match, 0 DRIFT, 0 UNIT MISMATCH, 4 could not be examined.

  PASS Store drift               1.1s  24 pointers against orrery
                                    c12994d2 -- 20 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 4 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            24 pointers against orrery c12994d2 --
  last swap 2026-10-01T16:00:33.623388+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  4. On your phone and desktop, open
     palomasorrery.com/interactive.html?exhibit=solar-system,
     tick Pluto, Neptune, Uranus, Jupiter and Apophis, and tap each.
     Pluto, Neptune and Uranus should end in 0,000 km; Apophis
     should have the extra line.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

3. **Your phone and desktop.** Open the Solar System room, tick Pluto, Neptune, Uranus, Jupiter and Apophis, and tap each one.

**What you should see (from the 1 October data):**
- Pluto: 35.6103 AU from the Sun (5,327,220,000 km). Before, it showed ten figures. -- no, 35.6108 AU and 5,327,300,000 km
- Neptune: 4,469,690,000 km, -- correct
- and Uranus: 2,908,370,000 km. -- no, 2,908,350,000
- Jupiter and Saturn end at hundreds of km, for example Jupiter at 793,908,700 km. -- Saturn is 1,411,367,900 km and Jupiter 793,946,800 km and 5.307207 AU
- - The inner planets look the same as before. -- not verified
- Apophis keeps its distance and adds your line: "JPL's own uncertainty for this position is not yet included." -- correct

**What the patches contain:**
- **The orrery's three accuracy rows.** They are cited to JPL's 2014 report, which I opened and read today.
- **The two skill updates and the protocol entry.** Version 2.23 of the provenance skill, version 1.7 of the room skill, and protocol v3.75.
- **The website changes.**
  - Nine bodies get a link to their group's row. -- unclear. the info button does not show a link. now or next?
  - The distance logic moves into its own file. -- unclear, please clarify
  - A new check joins the maintenance run. It fails if Pluto, Uranus or Neptune print finer than ten thousand km. It also fails if the page stops using the file. -- please add to the dashboard.

**How I tested them:**
- I ran both patches on throwaway copies, and each produced exactly the state I had tested.
- Every orrery and website check I could run in the sandbox passes.
- I ran the room's own Python and its text-box code on the real data, and the text boxes read as listed above.
- I did not open it in a browser. Your phone check is the real test.

The notes patch from earlier is still independent of these, so you can run it before or after. Once you have looked on your phone, I'll write the closing patch for the ledger and Where We Are.

Where this leaves us:
- The distance figures now follow JPL's own accuracy. That takes effect once you run both patches and push. -- done
- Next come the NASA descriptions and links for each body, then the drawer's new behaviours. -- okay

=========================================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L398_ledger_close_20261001.py
ok  LEDGER_CONSOLIDATED.md  header stamp
ok  LEDGER_CONSOLIDATED.md  L-401 and L-402 added
ok  LEDGER_CONSOLIDATED.md  L-398 done
ok  LEDGER_CONSOLIDATED.md  L-398 close block
ok  LEDGER_CONSOLIDATED.md  L-363 note
ok  palomas_orrery_dashboard.py  offline runner's list names the new check
ok  palomas_orrery_dashboard.py  button: Solar System Figures
ok  documentation/WHERE_WE_ARE.md  rewritten
ok  documentation/HANDOFF_L398_distance_figures_20261001.md  new

Stamps updated: the ledger's header line; Where We Are's date.
patch applied

NEXT:
  1. python orrery_maintenance_run.py  (rebuilds the ledger index
     and moves L-398 into the closed section)

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261001T183931Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.1s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.1s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             1.5s  unchanged (1 checked, not written)
  Module atlas                 6.2s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               5.4s  rewrote DATA_INVENTORY.md
  Exact rows report            1.6s  rewrote EXACT_ROWS_PRINTED.md -- 8 of 24
                                     exact rows printed at 19 lines (9 orrery, 10
                                     gallery); 8 drawn only, 0 not followed, 0
                                     map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.2s  No changes to constants_new.py since HEAD.
  Constants relations          0.2s  21 of 21 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.7s  No figure count exceeds its inputs: 29
                                     derived row(s) read, 17 judged OK -- 17 OK,
                                     12 NOT YET MIGRATED, 1 NO DERIVED LINE, 1
                                     UNMARKED CONVERSION; 15 conversion(s)
                                     checked.
  Constants export check       1.1s  Export matches the store: sha256
                                     089a5baf0101 on both sides; 79 rows re-read,
                                     66 not exported, 26 tokens; 172 conversions
                                     re-computed, 10 of 10 worked cases hold.
  Exact rows by the count      1.3s  PASSING -- 8 printed exact rows each state a
                                     count; 9 orrery lines print through
                                     exact_text(); 10 gallery lines are served
                                     the count
  Dimensions                   1.4s  No unit contradicts its arithmetic: 44
                                     derived row(s) read -- 32 OK, 9 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.1s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.1s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 81 status lines in constants_new.py are
                                     well formed; 61 rows carry none.
  Row shape                    0.1s  All 145 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.2s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          23.8s  PASS -- all 309 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  2.2s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker            8.9s  76 of 114 routed, 8 clean
  Worksheet checker tests     17.0s  All 136 checks passed
  Worksheet key round trip     1.4s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         28.3s  All 76 checks passed
  Extractor pins               0.6s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner          14.8s  296 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  18 of 18 gating checkers passed -- 118.8s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           76 of 114 routed, 8 clean
    Provenance scanner          296 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2022 file(s) examined, 9 written, 0 created, 0 removed, 4 rewritten identically
    written   DATA_INVENTORY.md
    written   EXACT_ROWS_PRINTED.md
    written   LEDGER_CONSOLIDATED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      PROJECT_INSTRUCTIONS.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  2. Move this script into documentation/. Commit and push. -- 6b2ef097da67e67ab8f748b5481c222e5dd34acc
  3. Optional: open the dashboard and press Solar System Figures
     under Gallery -- checks and data. It should end "=== PASS". 

Self-test: the worked cases fail on a Report test one place too fine, on a rule ignoring JPL's accuracy, and on the sentence printed for a body with a row.

Distances at each body's served minute (data/solar-system/coverage_index.json), 10 bodies:
  mercury           0.46485980 AU from the Sun (69,542,037 km)  -- set by whole kilometres
  venus             0.72696293 AU from the Sun (108,752,106 km)  -- set by whole kilometres
  earth             1.00132586 AU from the Sun (149,796,216 km)  -- set by drift
  apophis           0.85622593 AU from the Sun (128,089,576 km)  -- set by whole kilometres  + sentence
  mars              1.55826599 AU from the Sun (233,113,273 km)  -- set by whole kilometres
  jupiter           5.306952 AU from the Sun (793,908,700 km)  -- set by JPL's accuracy
  saturn            9.434651 AU from the Sun (1,411,403,600 km)  -- set by JPL's accuracy
  uranus            19.4413 AU from the Sun (2,908,370,000 km)  -- set by JPL's accuracy
  neptune           29.8781 AU from the Sun (4,469,690,000 km)  -- set by JPL's accuracy
  pluto_barycenter  35.6103 AU from the Sun (5,327,220,000 km)  -- set by JPL's accuracy

=== PASS: 6 worked cases, 11 drawer rows matched to their accuracy rows, 10 served distances; Uranus, Neptune and Pluto print to JPL's ten-thousands place ===

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

=================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L398_3_dashboard_wrapper_20261001.py
ok  documentation\run_solar_system_figures.py  new

patch applied

NEXT:
  1. python documentation/run_solar_system_figures.py -- it should
     end "=== PASS". (Optional; the dashboard button will do it.)


C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>python documentation/run_solar_system_figures.py
Self-test: the worked cases fail on a Report test one place too fine, on a rule ignoring JPL's accuracy, and on the sentence printed for a body with a row.

Distances at each body's served minute (data/solar-system/coverage_index.json), 10 bodies:
  mercury           0.46485980 AU from the Sun (69,542,037 km)  -- set by whole kilometres
  venus             0.72696293 AU from the Sun (108,752,106 km)  -- set by whole kilometres
  earth             1.00132586 AU from the Sun (149,796,216 km)  -- set by drift
  apophis           0.85622593 AU from the Sun (128,089,576 km)  -- set by whole kilometres  + sentence
  mars              1.55826599 AU from the Sun (233,113,273 km)  -- set by whole kilometres
  jupiter           5.306952 AU from the Sun (793,908,700 km)  -- set by JPL's accuracy
  saturn            9.434651 AU from the Sun (1,411,403,600 km)  -- set by JPL's accuracy
  uranus            19.4413 AU from the Sun (2,908,370,000 km)  -- set by JPL's accuracy
  neptune           29.8781 AU from the Sun (4,469,690,000 km)  -- set by JPL's accuracy
  pluto_barycenter  35.6103 AU from the Sun (5,327,220,000 km)  -- set by JPL's accuracy

=== PASS: 6 worked cases, 11 drawer rows matched to their accuracy rows, 10 served distances; Uranus, Neptune and Pluto print to JPL's ten-thousands place ===

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  2. Move this script into documentation/. Commit and push. -- 5a38de15d69df48749ba230cdfacf0e9d9e2fb5e
  3. Then the orrery's closing patch, which adds the button. -- correct
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 