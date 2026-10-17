<!-- Doc-Kind: hand | Session record of Earth's round-1 build: the run-records check (L-449), the belts as the orrery's stored dots (L-330), the words and citations (L-451, L-452, L-450), the aberration sentence (L-314), the four hovers fitted to 17 lines, and the fades design (L-410); three patches and the close, with Tony's run order. -->
# Handoff: Earth round 1, the build (and the fades design)

Built on orrery da78b80fc7cf38c87d9d32d5b491b58023777561 at
https://github.com/tonylquintanilla/palomas_orrery (the code is
a73bc24a's, "patch earth round 1 close"; da78b80 adds only Tony's run
record) and gallery f49b3e6974cc1183fe8f64f24878d6e2b6f540f2 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io ("daily
run 10-17-26"). Nothing pushed by this session; Tony pushes.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD, with a design talk at its end (zero code).
Companions: the brief it built,
`documentation/HANDOFF_earth_round1_build_brief_20261016.md`; the
approved words, `documentation/WORDS_earth_round1_20261017.md`, its
revision 2 and the new-only copy; the fades design,
`documentation/DESIGN_fades_rulings_20261017.md`.

## 1. Your run order (every Tony-action of this session, in one list)

Each patch checks the files it edits and refuses rather than guess.

1. **(do)** Website folder: run `patch_L449_1_run_records_20261017.py`.
2. **(do)** Orrery folder: run `patch_L330_2_belts_words_citations_20261017.py`.
3. **(do)** Orrery folder: run `patch_earth_round1_build_close_20261017.py`
   (the ledger, Where We Are, and this record with the design record).
4. **(do)** Orrery maintenance run (dashboard). Expect 31 of 31 gating,
   "Drawings export check" 5 of 5 planted faults, the gate line 0 TIER-1.
5. **(look)** Mode 5 in the orrery: plot Earth with the magnetosphere on.
   The two belts as curved dots; the belt, magnetosphere, bow shock and
   LEO hovers.
6. **(do)** Move the two orrery scripts into `documentation/`; commit;
   push. Patch 2 must be pushed before step 9: the Daily Run pulls the
   belts' drawing from GitHub.
7. **(do)** Reinstall three skills in Settings > Skills:
   provenance-discipline (2.30), interactive-exhibit (1.17),
   gallery-cache-builder (1.11).
8. **(do)** Website folder: run `patch_L330_3_website_belts_words_20261017.py`.
9. **(do)** The Daily Run. Until it has run, the Earth checks fail on the
   belts' drawing not being served; that is expected. Expect 29 of 29
   gating, "Drawings" 7 of 7 planted faults, "Typed facts" saying OPEN
   is empty.
10. **(do)** Move the two website scripts into `documentation/`; commit;
    push; then `python gallery_maintenance_run.py --live`.
11. **(look)** Mode 5 on the phone, the Earth room: the belts (arrival,
    rotate, tap a belt, its text box and i panel); the magnetopause and
    bow shock hovers and i panels; the i panels' Source lines with no
    repeated notes; the low-orbit inner edge at 180 km.
12. **(decide)** At that look, three wordings Claude chose (section 4).

## 2. What was built, and how it was checked

**Patch 1, website (L-449).** The builder prints two `[RUNS]` lines:
how many run records the copy step found and carried. The Daily Run
compares the new cache's `raw/runs/` with the replaced cache's after
the builder and, on a loss, stops before the maintenance run, naming
each lost record with both copies' paths. Ruled at the session's start:
stop and name, not put back. Builder suite 238 checks; the gallery run
29 of 29 gating in a sandbox copy.

**Patch 2, orrery (L-330, L-314, L-452 with L-450).**
- `van_allen_belt_sampler.py`, new: the belts' dots, scattered at random
  along dipole field lines r = L cos^2(latitude) (Koskinen and Kilpua
  2022, sec. 1.2.1, open), between each belt's edge rows, thickest at
  its peak, from seed 330, 1,200 and 2,000 dots; its checks catch a dot
  off its field lines, below the ground, or a belt not thickest at its
  peak. Stored as `data/drawings/van_allen_belts.json` in Earth radii.
- The belts drawn from those dots, in Tony's approved hovers; the
  aberration sentence on the magnetosphere and bow shock; the low-orbit
  inner edge at ESA's 180 km, a measured row now; the citation lines
  cleaned as approved; the 660 km row names Ishii et al. (2018).
- Skills: provenance-discipline 2.30 (What a Visitor Reads, the five
  principles), interactive-exhibit 1.17 (source_note holds only a
  drawing choice; scattered dots are a stored drawing),
  gallery-cache-builder 1.11 (the run-records check); protocol v3.102.
- Tested: the orrery maintenance run 31 of 31 gating on the patched
  tree; scanner gate path 0 Tier-1, whole tree 280 as before; the GUI
  starts; applied clean and on a Windows-line-ending copy.

**Patch 3, website (L-330, L-451, L-452, L-314).**
- The belts drawn from the stored dots, scaled by the served Earth
  radius, turned to the pole, shaded by weight; "Thickest at";
  `hovers_shape` (was `hovers_rings`); the field lines' citation in the
  i panel (`details`).
- The five held sentences served on their numbers (`hover_line`, and
  the tilt's as `orientation.words.tilt_of_date`); sentence 7 reworded,
  8 cut; the Typed facts check's OPEN list empty.
- The 35 notes kept, reworded or removed as approved, through
  `tools/store_writer.py`, which now edits a number's `source_note` and
  can remove one; the Crust's note without its attribution.
- The aberration sentence served; LEO at 180 km in its name and abouts.
- Drawings in Earth radii accepted by the pull, the builder and the
  Drawings check; the belts checked by their field lines, 7 planted
  faults in all.
- The Earth scene re-recorded; a new hover fixture,
  `fixture_hovers_L330_on_f49b3e69.json`.
- Tested in a sandbox copy that stood in for your Daily Run (patch 2's
  export and drawing laid in, mirrored, the served features rebuilt):
  29 of 29 gating. A turned frame planted in the drawing turns the belt
  checks red. Applied clean and on a Windows-line-ending copy; your
  website files matched the base, patch 1 aside.

## 3. Rulings this session (each recorded in the ledger)

- L-449: a lost run record stops the Daily Run and is named.
- L-330: random dots ("Yes, random. And it shows the density better
  too."); the inner belt curved ("it reads okay"), so option C (inner
  belt flat) is not used.
- The words: approved by principle, then item by item (revision 2).
- The low-orbit inner edge: ESA's 180 km ("A, as recommended. settled.").
- The principles for what a visitor reads: into provenance-discipline
  2.30, "so that it is uniformly applied".
- The 17-line limit: "Move some lines to i panel" -- the belts' plane
  sentence; the magnetopause's paper and solar wind; the bow shock's
  paper, pressure and where its drawing stops.
- The fades (L-410, L-454): see the design record.

## 4. Three wordings Claude chose, for your look

- Low-orbit inner edge, the note after its Source: "The region itself
  begins at the surface; the inner edge is drawn at the lowest height
  satellites fly." (The approved "chosen for the picture" stopped being
  true at ESA's 180 km.)
- Crust, the note after its Source: "The Earth radius used as the unit
  stays the IAU's equatorial one: Prsa et al. (2016), AJ 152:41, on IAU
  2015 Resolution B3."
- Bow shock, i panel: "Jelinek et al. (2012), at dynamic pressure 2 nPa.
  Drawn to 105 deg from the nose: that is where the drawing stops, not
  where the shock ends." (The second sentence lost its antecedent when
  it moved out of the hover.)

## 5. Found, and where it went

- The Typed facts check met the Sun Direction's orbital-period line for
  the first time once the Earth scene was re-recorded (it entered with
  L-431 build 3). Its body and centre are the orrery's served labels;
  it is on ALLOWED as the page's account of its data, by shape. Change
  it if you disagree.
- L-410 already held fuzzy boundaries with a range idea; today's rule
  replaces it (Tony: "Yes it replaces the range idea. Those examples
  still have fades.").
- Typed numbers in served words with no row: the crust's thicknesses
  (5 to 10 km and 30 to 50 km) and the magnetopause note's 6.6 Earth
  radii. One class: L-455.
- Method owed to interactive-exhibit's next version: `panel_words`,
  `hover_line`, `details`, a number's `source_note` (editable and
  removable), sentences moved to the i panel for the 17-line limit.
  Carried on L-435.
- The website keeps `evenBeltRings()` for a body with served belt edges
  and no stored drawing (none today; Jupiter has no edge rows). The
  orrery removed its copy in patch 2. Carried on L-330's note.

## 6. Skill obligations travel

A reinstall during a session is not visible to it. The next session
confirms its loaded copies read provenance-discipline 2.30,
interactive-exhibit 1.17 and gallery-cache-builder 1.11 before work
that fires them. horizons-orbital-mechanics 1.8 (v3.99) still travels:
no work this session fired it. This session confirmed
ledger-and-session-records 1.21 at load, as the manifest expects.

## 7. Next

Earth's list (L-413): after your Mode 5 looks close L-330, L-451, L-452
and L-450, either the build of Earth's fade (L-410, designed) or
design talk 2, the field's model and offset (L-356 with L-375), which
the moving-edge device (L-454) joins. Your call which first.

Session written October 17, 2026 with Anthropic's Claude Opus 5.5.
