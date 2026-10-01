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
