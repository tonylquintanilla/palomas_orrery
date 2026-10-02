<!-- Doc-Kind: hand | Session record for L-398, the Solar System room's distance figures, and Tony's notes of 2026-10-01. -->
# HANDOFF -- L-398: distances print what JPL's accuracy earns

Built on orrery 7a47269c09acd4d2f875f6c8d49070659c4c2ee9 at
https://github.com/tonylquintanilla/palomas_orrery, and gallery
c48f9a92e6d6094a8d25ae9413a94c17503ee50c at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Orrery pushed at c12994d2 (the notes patch and patch_L398_1). Gallery
pushed at 58dd8f25 (patch_L398_2). This record lands with the closing
patch patch_L398_ledger_close_20261001.py, after the gallery's
patch_L398_3_dashboard_wrapper_20261001.py.

Type: BUILD.
Supersedes: nothing. Follows HANDOFF_L363_half2_step3a_20260930.md,
whose section 6 items 1 and 2 this session carried out.

Session written October 2026 with Anthropic's Claude Opus 5.5.

## 1. Skills at session start

All loaded copies matched the manifest: ledger-and-session-records 1.13,
safe-file-editing 1.11, provenance-discipline 2.22, interactive-exhibit
1.6, gallery-cache-builder 1.6, gallery-assembler 1.3, agentic-pre-test
1.2. This session bumped provenance-discipline to 2.23 and
interactive-exhibit to 1.7 (protocol v3.75). Tony reinstalled both;
this session cannot see that. THE NEXT SESSION CONFIRMS its loaded
copies read 2.23 and 1.7 before any provenance, constants_new.py or
exhibit work.

## 2. Rulings

- Tony's notes on Where We Are, recorded by
  patch_L363_ledger_tony_notes_20261001.py: the lobby stays the front
  page and the Solar System room's card becomes the top featured card;
  whether a bare interactive.html link switches is "to be determined";
  the goal line reworded ("confirmed as recommended"); Earth's
  atmosphere is the provenance skill's to decide; the orbit markers
  keep their words; the stray folder deleted.
- The distance figures: an accuracy stated only in words is stored as
  the place the Report test gives for every value the words can mean,
  the coarser where they could mean two. Uranus, Neptune and Pluto at
  ten-thousands, one place coarser than the plan's wording. Tony:
  "Confirmed as recommended".
- Tony asked for the new check on the dashboard.
- Tony's idea, recorded as L-402: choose a date, or animate, within the
  range the cache is trusted for, with the range following only the
  bodies drawn ("without Mercury or without the Moon to get more
  range"). Not scheduled; Claude suggested a design talk after the
  drawer.

## 3. What was built, verified

| Patch | Repo | Pushed | Verified |
|---|---|---|---|
| patch_L363_ledger_tony_notes_20261001.py | orrery | c12994d2 | Tony's run, every edit ok. |
| patch_L398_1_accuracy_rows_and_skills_20261001.py | orrery | c12994d2 | Tony's maintenance run: 18 of 18 gating. In the sandbox: LF and CRLF copies, refuses a rerun and the wrong folder; store checks pass; scanner Tier 1 unchanged at 296, the new rows at Tier 2. |
| patch_L398_2_distance_figures_20261001.py | gallery | 58dd8f25 | Tony's runs: 20 of 20 offline, live 14 of 14 files byte-identical, export at c12994d2. In the sandbox: the room's real driver run in CPython on the real cache, its compose run in Node; the new check fails on the unpatched gallery with 18 named problems. Tony's phone: places as designed (ledger L-398). |
| patch_L398_3_dashboard_wrapper_20261001.py | gallery | -- | Sandbox: the wrapper passes from the root and refuses from documentation/. |
| patch_L398_ledger_close_20261001.py | orrery | -- | This patch: ledger, dashboard button, Where We Are, this record. |

## 4. Found this session

- The orrery's own distance hovers print by fixed widths -- ten decimal
  places of an AU in the detailed hover. Recorded as L-401, one class
  row, not chased.
- My first message said the front-door ruling replaced a plan to make
  the room the website's opening page. The plan only ever meant a bare
  interactive.html link. Corrected in L-363.
- My delivery message said "nine bodies get a link", which read as a
  visitor link. It meant a pointer in objects_config.json.

## 5. Discrepancies

- None between handoff and base.

## 6. Next session

1. Confirm the loaded skills read provenance-discipline 2.23 and
   interactive-exhibit 1.7.
2. L-395: a short design talk on the orrery's object list, then the
   export of descriptions and NASA links, with the duplicate-field
   check.
3. L-363 step 3b, the drawer, then Tony's phone check.

## 7. Tony-actions, rolled up

- (do) Run patch_L398_3_dashboard_wrapper_20261001.py in the gallery
  root; move it to documentation/; commit and push.
- (do) Run patch_L398_ledger_close_20261001.py in the orrery root; then
  orrery_maintenance_run.py; move the patch to documentation/; commit
  and push.

=========================================================================

 PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L395_mars_jupiter_links_20261001.py
ok  celestial_objects.py     Mars links to science.nasa.gov/mars/
ok  celestial_objects.py     Jupiter links to science.nasa.gov/jupiter/

patch applied (2 edits in 1 file)

NEXT:
  1. Move this script into documentation/.
  2. Commit and push. It can go with this session's closing
     patch, or on its own now.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>  

==============================================================================

The website patch is fixed, and both patches are ready to run.

**What changed since last turn:**

- The website patch now also adds Apophis under 2004 MN4 to the cache builder's stand-in Horizons data. With that line, the builder's suite passes all 229 checks again.
- I re-ran the website's maintenance run on a patched copy. Every check passes except two, and neither is a problem with the patch:
  - "Pole of date" fails only in my sandbox, which lacks the pyerfa library your machine has.
  - "Cache in step" fails, as expected, until the cache is rebuilt under Apophis's new id.
- I ran the room's own setup code on the patched copy, using the real cache. All eleven bodies, the Sun included, now arrive with their description and NASA link, and the room reports no warnings.

**The order to run them in.** Neither repo has moved since this morning, so start at step 1.

1. **Orrery folder:** run `patch_L395_1_objects_export_20261001.py`, then `orrery_maintenance_run.py`.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L395_1_objects_export_20261001.py
ok  celestial_objects.py           Mars links to science.nasa.gov/mars/ (already done)
ok  celestial_objects.py           Jupiter links to science.nasa.gov/jupiter/ (already done)
ok  celestial_objects.py           key 'sun' on Sun
ok  celestial_objects.py           key 'mercury' on Mercury
ok  celestial_objects.py           key 'venus' on Venus
ok  celestial_objects.py           key 'earth' on Earth
ok  celestial_objects.py           key 'mars' on Mars
ok  celestial_objects.py           key 'jupiter' on Jupiter
ok  celestial_objects.py           key 'saturn' on Saturn
ok  celestial_objects.py           key 'uranus' on Uranus
ok  celestial_objects.py           key 'neptune' on Neptune
ok  celestial_objects.py           key 'pluto_barycenter' on Pluto-Charon Barycenter
ok  celestial_objects.py           key 'apophis' on Apophis
ok  celestial_objects.py           Pluto-Charon Barycenter: unsourced period removed; links to NASA's Pluto page
ok  celestial_objects.py           Sun: stray space inside the closing quote removed
ok  celestial_objects.py           Apophis: closing full stop added
ok  ORBITAL_MECHANICS_README_v1_4.md dated note: the code now uses 920136108, Haumea itself
ok  orrery_maintenance_run.py      GENERATORS: Objects export
ok  orrery_maintenance_run.py      CHECKERS: Objects export check
ok  export_objects.py              created
ok  test_objects_export.py         created

patch applied

NEXT:
  1. python orrery_maintenance_run.py -- its new Objects export
     writes data/objects_export.json, and Objects export check
     should read: OBJECTS EXPORT: pass

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261001T201738Z, 1 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.0s  unchanged (1 of 1 rewritten, content
                                     identical)
  Skill manifest               0.1s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             1.3s  unchanged (1 checked, not written)
  Objects export               0.1s  rewrote data/objects_export.json
  Module atlas                 6.5s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               5.6s  rewrote DATA_INVENTORY.md
  Exact rows report            1.4s  unchanged (1 checked, not written) -- 8 of
                                     24 exact rows printed at 19 lines (9 orrery,
                                     10 gallery); 8 drawn only, 0 not followed, 0
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
  Constants export check       1.0s  Export matches the store: sha256
                                     089a5baf0101 on both sides; 79 rows re-read,
                                     66 not exported, 26 tokens; 172 conversions
                                     re-computed, 10 of 10 worked cases hold.
  Objects export check         0.1s  pass
  Exact rows by the count      1.3s  PASSING -- 8 printed exact rows each state a
                                     count; 9 orrery lines print through
                                     exact_text(); 10 gallery lines are served
                                     the count
  Dimensions                   1.2s  No unit contradicts its arithmetic: 44
                                     derived row(s) read -- 32 OK, 9 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.2s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.1s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 81 status lines in constants_new.py are
                                     well formed; 61 rows carry none.
  Row shape                    0.1s  All 145 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.3s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          19.0s  PASS -- all 309 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  1.6s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker            9.6s  76 of 114 routed, 8 clean
  Worksheet checker tests     15.4s  All 136 checks passed
  Worksheet key round trip     0.8s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         17.4s  All 76 checks passed
  Extractor pins               0.3s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner           8.5s  296 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  19 of 19 gating checkers passed -- 94.3s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           76 of 114 routed, 8 clean
    Provenance scanner          296 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2027 file(s) examined, 8 written, 2 created, 1 removed, 5 rewritten identically
    written   DATA_INVENTORY.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    written   module_atlas.py
    created   data/objects_export.json
    created   documentation/patch_L395_1_objects_export_20261001.py
    removed   patch_L395_1_objects_export_20261001.py
    rewritten with identical bytes, no action needed:
      LEDGER_CONSOLIDATED.md
      PROJECT_INSTRUCTIONS.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  2. Move this script into documentation/ (and the small Mars and
     Jupiter patch, run or not).
  3. Commit and push. The gallery patch pulls the export from the
     orrery's pushed state, so this push comes first.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

   - The new line "Objects export check" should read `OBJECTS EXPORT: pass`.
   - The small Mars and Jupiter patch is no longer needed, because this patch makes the same two fixes. Move it to `documentation/` unrun, along with this patch.
   - Then commit and push. -- 
  
1. **Website folder:** run `patch_L395_2_objects_mirror_20261001.py`, then `gallery_maintenance_run.py`.
   - "Objects mirror" lists the 23 fields it wrote.
   - "Cache in step" fails, naming Apophis's Horizons id.
2. **Website folder:** run `daily_run.py` to rebuild the cache, then run the maintenance run again. "Cache in step" should now pass.
   - Move the patch to `documentation/`, then commit and push.
3. On your phone, open the Solar System room, tap a planet, and open the info panel. You should see NASA's sentence and a "Read more at NASA" link.

Once you've done that, tell me what step 4 showed, and I'll write the closing patch for the ledger, Where We Are and the session record.

Where this leaves us:

- The orrery's object list now feeds the website, for the Solar System room's eleven bodies.
- After your runs, the room's info panel shows each body's description and NASA link.