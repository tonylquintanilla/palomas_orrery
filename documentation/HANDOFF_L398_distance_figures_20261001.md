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
