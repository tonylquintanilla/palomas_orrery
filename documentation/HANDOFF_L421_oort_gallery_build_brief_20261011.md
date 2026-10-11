<!-- Doc-Kind: hand | Brief for the gallery side of the inner Oort cloud redraw (L-421, the typed facts): the Sun room draws the Hills cloud the orrery now draws, the band from 10,000 to 20,000 au, the served words; L-408 (the galactic plane in the Sun room) rides it. Written October 11, 2026. -->
# Handoff: L-421 (the typed facts), the inner Oort cloud, the gallery-side build brief

Built on orrery 84d329a12575d923daa06ffa104012ce11abc925 ("L431 run
record notes", 2026-10-11 09:25 CDT) at
https://github.com/tonylquintanilla/palomas_orrery and gallery
fd17abf1cf99169289acfeb0a45f84365265c255 ("daily run", 2026-10-11) at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. The
session pins both HEADs itself at its start. On Tony's computer the two
repositories are `C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`
(orrery) and `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`
(gallery); a session linked to his computer saves each patch in that
repository's root folder, where he runs it. Written by the Fable 5.1
coordination session of October 11, which read both repos at HEAD and
wrote no patch.

- Type: BUILD, gallery, with one small orrery patch if the session
  takes the recommendation in section 2 (an export of the sampled
  points), and a records patch in the orrery at the close.
- Inputs, in this order: section 6 of
  `documentation/HANDOFF_L421_oort_orrery_20261010.md` (what the
  orrery half hands over: the rows now in `data/constants_export.json`,
  the sampler, the words); sections 1, 3, 4, 5, 9 and 10 of
  `documentation/DESIGN_L421_inner_oort_tilt_20261009.md` (Tony's
  rulings and confirmed words, including L-408's); section 8 of the
  orrery record (every hover the orrery changed, old and new, which
  the website's words follow); L-421 and L-408 in the ledger.
- Skills this session fires: interactive-exhibit 1.14 (the Sun room,
  its drawer, the served-data contract, the Mode 5 phone sequence),
  gallery-cache-builder 1.8 (objects_config.json, the mirror, the
  cache rebuild), gallery-assembler 1.3 (served geometry; the
  orrery/assembler boundary), provenance-discipline 2.28 (served words
  with their sources), safe-file-editing 1.13, agentic-pre-test 1.3
  (if the orrery is touched), ledger-and-session-records 1.19. Read
  back each loaded version in the first reply. Two obligations travel
  here and are discharged by that read-back: interactive-exhibit must
  read 1.14 and gallery-cache-builder 1.8 (from v3.89). The protocol is
  PROJECT_INSTRUCTIONS.md v3.90.
- A second Opus session is running beside this one: the L-431
  (orbital periods) design talk, conversation only. It touches no
  gallery file and no renderer. Both sessions close by editing the
  ledger and Tony's page, by section; Tony runs the two closing
  patches one after the other, in the order he chooses.

## Read this first

- *The website still draws the Hills cloud as a flat ring with a
  typed caveat. The orrery now draws the paper's tilted disk with its
  two arms, and a band from 10,000 to 20,000 au where the inner cloud
  gives way to the outer. This session makes the website draw what
  the orrery draws, with the same words, served.*
- *One architecture question is asked first, in one message (section
  2): whether the website serves the orrery's sampled points or
  re-samples them in the browser. Recommendation: serve them.*
- *L-408 (the galactic plane in the Sun room) rides this build, as
  Tony ruled on October 9: the ring, the pole line, both poles marked,
  the direction of Sagittarius A*, with its one wrong sentence
  rewritten. Its words are confirmed (design record, section 10).*
- *Every fact a visitor reads is served from its row with its source
  (interactive-exhibit 1.14). Code types only words about the
  picture.*

## 1. What the orrery half built, in one place

- Rows, now in `data/constants_export.json` for the gallery to pull:
  `INNER_OORT_DISK_OUTER_AU`, `HILLS_CLOUD_TILT_DEG`,
  `ECLIPTIC_NODE_GALACTIC_LON_DEG`, the four
  `HILLS_CLOUD_PERI_ARG_BAND*` rows, the four caption rows
  (`HILLS_CLOUD_NODE_*`, `HILLS_CLOUD_INCL_GAL_*`),
  `HILLS_CLOUD_PLANES_READ` (a dict, unit `dot_count`), two cell rows,
  `HILLS_CLOUD_ECCENTRICITY` (declared, with its reason). Two new
  tokens: `eccentricity`, `dot_count`. The band's near end reads
  `OORT_CLOUD_OUTER_EDGE_LOW_AU` (10,000, NASA, with Nesvorny et al.
  2025 added as a second source); its far end reads
  `INNER_OORT_CLOUD_AU` (20,000, Portegies Zwart 2021). No second
  10,000 row was made.
- The sampler: `hills_cloud_sampler.py` with `pole_frames.py`, numpy
  only, in the orrery's root. `sample_hills_cloud(n_orbits,
  points_per_orbit, rows=None, seed=None)` returns the dots;
  `check(rows, seed=421, ...)` prints the frame check, the Fig. 3
  reading and the plane's tilt (34.1 degrees on a large sample against
  the paper's "about 30"; PASS). The orrery draws 600 orbits, 3,600
  dots.
- The words: Tony's confirmed words of October 9 for the Hills cloud's
  hover, `about` and `note` (design record sections 4, 5, 9), with one
  clause the orrery session changed so it says what is drawn: the
  note's "picked within the ranges the model gives" became "picked
  where the model's orbits lie (its Fig. 3)". That clause comes to
  Tony with the website words, once, before they ship. The clumps'
  and the tide's hovers now say "From 10,000 AU, filling in by 20,000
  AU, to 100,000 AU"; the Inner Oort Cloud sphere says the inner cloud
  gives way between 10,000 and 20,000 AU and that the sphere is drawn
  at the far end.

## 2. The one question first: served points, or the browser re-samples

What the orrery's points are: a drawing recipe run once, with a seed,
from served rows. Three ways the website can get the same picture:

- **A. Serve the points.** The orrery's maintenance run exports the
  sampled dots (seeded, so the file is reproducible; 3,600 dots by
  three coordinates is about 100 kB) into a small file beside
  `data/constants_export.json`; the gallery pulls it the way it pulls
  the constants export, checks its hash, and the cache builder serves
  it with the Sun's other features. The renderer draws dots it is
  given. One implementation, one check (the sampler's own), and the
  website's disk is the orrery's disk to the dot.
- **B. Copy the sampler into the gallery** and run it in the nightly
  build. Two copies of one module, which the pull step would have to
  prove byte-identical each night, or they drift.
- **C. Re-sample in JavaScript** in `feature_renderers.js`. A second
  implementation of the orbit sampling and the galactic-frame
  transform, which needs its own tilt check and can disagree with the
  orrery's.

Recommendation: **A**. It follows the project's own rule for the two
instruments: the orrery computes, the website caches and reconstructs;
what transfers is the knowledge, not the machinery. It also settles,
for this builder, L-239 (seeding the Oort builders so a render is
reproducible): the export's seed is the record. The cost is one small
orrery patch (the export and its check in the maintenance run) and
Tony's orrery push before the gallery half, the same middle stop the
L-395 build used.

Put A, B and C to Tony in one message with this recommendation. If he
says A, the orrery export comes first, then his push, then the gallery
half on that push.

## 3. The gallery half

- **`data/objects_config.json`**, through the tools that may write it
  (store_writer / exhibit_store_editor; never by hand): the Sun's
  `oort_cloud` block. `hills_cloud_torus` becomes the tilted disk: its
  served `description`, `hover`, `about`, `note`, name ("Hills Cloud
  (tilted disk)"), link (Wikipedia, "Hills cloud"), and its links to
  the rows above (the tilt as `{tilt}`, the band's ends as `{near}` and
  `{far}`). `outer_oort_clumpy.inner_radius` and
  `galactic_tide.inner_radius` become the band (thin at the near end,
  full by the far end); `inner_oort.radius` stays 20,000 with the new
  first line in its hover. Encke's `_declared` "1.1 times" sentence
  (L-363), owed since October 4, is fixed in the same pass; it is one
  word.
- **`gallery/feature_renderers.js`**: the Hills cloud draws the served
  dots (or re-samples, if Tony chose C); `HILLS_CAVEAT`, the typed
  caveat, goes; the clumps and the tide fade in across the band; the
  same point counts as today, spread differently (render size). The
  single info marker carries the hover; geometry points carry none.
- **The i panel**: `{tilt}`, `{near}`, `{far}` filled from the served
  rows in `about` and `note` as the hover already does; the orrery
  record flags this as a build check, not a given. The full citation
  (Nesvorny et al. 2025, with the arXiv link) goes to the panel, the
  short attribution stays in the hover (L-231).
- **L-408, the galactic plane**: a drawer row "Galactic Plane", off by
  default, in the Sun room: a faint ring in the galaxy's plane at the
  tide's outer edge, a line along the galactic pole through the Sun,
  the two poles marked, and the direction of Sagittarius A* as a
  marker on the same ring, all reading the served pole rows and the
  Sgr A* degree rows already in the export. Words: section 10 of the
  design record, word for word, including the rewritten sentence
  ("The Hills cloud stands nearly at right angles to the galaxy's
  plane, turned there by the same tide over billions of years") with
  its three locators; the Sgr A* marker says "The direction of the
  centre of our galaxy, seen from the Sun" and not "black hole", which
  the row's source does not state. Link: Wikipedia, "Galactic
  coordinate system", confirmed to answer before shipping. On the
  phone it is a row like any other; the design's "whether the phone
  draws it" is answered by the row being off by default.
- **The headless room test** (`tools/headless`): the Sun room boots,
  the Hills cloud's trace carries its shell key, the served words
  reach the hover and the panel with the placeholders filled, the
  Galactic Plane row toggles, and no sentence in the room is typed
  that the typed-facts survey of October 6 would count (run that
  survey's method on the room before and after; it is the check part
  2 of L-421 will later make gating).
- **Figures**: the tilt prints as "about 30 degrees" from its row; the
  distances print through the served `in` as today; no number is
  typed in JavaScript.

## 4. Verification before anything reaches Tony

- The pull: the gallery's constants export matches the orrery's at
  HEAD byte for byte (the existing check), and the new rows are in it
  by name.
- If A: the points file's hash matches the orrery's; the cache builder
  serves it; the renderer reads it; a plane fitted through the served
  dots in the browser (or in the builder) prints a tilt near the
  orrery's 34 degrees. That number is the one check that fails on the
  mechanism rather than the picture; print it.
- The gallery maintenance run offline: every gating row passes,
  including the Horizons rows now in it; the mirror check reports the
  new links; the collapsed-features check counts the Sun's shells as
  before plus the new row.
- The Sun room's hover-length budget on the phone: the new Hills
  cloud hover and the Galactic Plane words inside the 17-line limit.
- Patches twice over and on a CRLF copy, as always.

## 5. Tony's steps, in order

1. (decide) A, B or C, section 2, in one message.
2. If A: run the orrery export patch, `orrery_maintenance_run.py`
   (expect 22 of 22 and "GATE PATH: 0 TIER-1"), move the script into
   documentation/, commit and push.
3. Run the gallery patch; run the Daily Run (the Horizons check, then
   the cache rebuild, then the offline maintenance run); commit and
   push; the live maintenance run.
4. The phone look, with the Home Screen clip's tab closed first: the
   Sun room, the Hills cloud ticked, then the clumps and the tide,
   then the Galactic Plane row. His verdicts beside each line.
5. Run the orrery records patch, the maintenance run, push.

## 6. At the close

- The ledger: L-421 (the typed facts) records the gallery side done
  by name; its Gap narrows to part 2 (the survey as a gating check)
  and part 3 (the citation-agreement check). L-408 (the galactic
  plane in the Sun room) closes on Tony's look. L-363's `_declared`
  line struck. L-239 gains a line if A settled the seed for this
  builder.
- Tony's page, by section, handles labelled, nothing below the
  marker; the page is at 129 lines, so trim before adding. The box
  says the website now draws what the orrery draws.
- The handoff: `documentation/HANDOFF_L421_oort_gallery_20261011.md`
  in the orrery, anchored on both HEADs at start, at the middle push,
  and at the close.
- The obligation that travels: none new unless a skill is bumped. If
  interactive-exhibit gains a line (served geometry pulled from the
  orrery, if A), that is 1.15, one version, and the next session
  confirms it. Do not bump a second skill.

## 7. Not this session

- Part 2 of L-421 (the gating survey check) and part 3 (the
  citation-agreement check): the next L-421 session.
- L-431 (orbital periods): the other open session's design talk.
- L-432 (default colours) and L-433 (the road after): Tony's, later.
- Any room but the Sun's.

Brief written October 11, 2026, with Anthropic's Claude Fable 5.1.
