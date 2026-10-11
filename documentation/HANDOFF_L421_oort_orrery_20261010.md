<!-- Doc-Kind: hand | Build record for L-421 (the typed facts), the inner Oort cloud, orrery side: the Hills cloud drawn as dots along orbits following Nesvorny et al. (2025) Fig. 3, the band from 10,000 to 20,000 au, the new rows, the sampler and its checks; what the gallery session needs. Written October 10, 2026. -->
# Handoff: L-421 (the typed facts), the inner Oort cloud, orrery side, built

Built on orrery 32619f8d6ac4cd0806da3ea8e7442f04ceea0ecd ("Update
WHERE_WE_ARE_10-10-26_1426_run_record.md") at
https://github.com/tonylquintanilla/palomas_orrery, WITH
`patch_L395_7_records_20261010.py` applied on top, as Tony had not run
it yet; the patch refuses until it has. Gallery
a7d1a542ae5b6d26dc3c658c339fcf721d181780 ("daily run again to check") at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read, not
touched. Both pinned with `git ls-remote` at the session's start.
This record lands with `patch_L421_5_oort_orrery_20261010.py`; its push
is the next commit.

- Type: BUILD, orrery only. From
  `documentation/HANDOFF_L421_oort_orrery_build_brief_20261009.md` and
  the design record `documentation/DESIGN_L421_inner_oort_tilt_20261009.md`.
- Skills loaded, read back in the first reply, each matching the
  manifest of protocol v3.89: provenance-discipline 2.28 (both
  reference files present; `references/figures.md` opened before any
  `# Figures:` line was written), ledger-and-session-records 1.18,
  orrery-coding-conventions 1.10, safe-file-editing 1.13 (version line
  read), agentic-pre-test 1.3.
- ledger-and-session-records reads 1.18, not 1.19: the 1.19 bump is in
  patch_L395_7, unrun when this session started. No skill version
  changed this session.
- The paper: Tony's copy, attached in this chat; the build read
  arXiv:2502.11252v1 as PDF and as text. Page numbers are that PDF's.

Session written October 2026 with Anthropic's Claude Opus 5.5.

## Read this first

- *The orrery draws the Hills cloud as dots along orbits that follow
  the paper's Fig. 3. The plane through the dots comes out tilted 34
  degrees to the ecliptic; the paper says about 30.*
- *The inner cloud gives way to the round outer cloud across a band,
  10,000 to 20,000 au. The Hills cloud thins out across it; the clumps
  and the galactic tide fill in across it.*
- *Still to do: Tony's look in the orrery window (section 7), then the
  gallery session (section 6).*

## 1. Rulings this session

- **The band's near end stays at 10,000 au** (brief section 2). Tony,
  17:57: "Confirmed as recommended".
- **The tilt check failed, and the build stopped before drawing.**
  Orbits spread evenly over the Fig. 2 and Fig. 3 captions' ranges
  give a plane tilted about 40 degrees, the orbits' own tilts averaging
  42. The frame was checked and is right (section 3). Tony attached the
  paper; Fig. 3 was read (section 2).
- **Tony, 18:27: "follow the paper. Draw following figure 3 and
  describe following the text. And cite everything."** So the drawing
  follows Fig. 3, the words say what the text says ("about 30"), and
  every number is a cited row.

## 2. Fig. 3, read into a table

- Fig. 3 (p. 19) plots one dot per orbit: galactic nodal longitude
  across, galactic inclination up. The PDF holds it as a JPEG, 714 by
  551 pixels, and it was read as stored.
- The script is `documentation/L421_fig3_reading_20261010.py`, a
  record, on no build path. It checks its axes against three lines the
  figure draws: the ecliptic node read at 186.21 degrees (the caption:
  186), the ecliptic plane at 59.87 (60), the polar orbits at 90.00
  (90). It stops if any is off by more than one degree, which caught a
  wrong frame once during the build.
- Dots are counted in cells 10 by 5 degrees, from how much of each
  cell is inked, correcting for dots that overlap. 203 cells, 2,052
  dots; 67% inside the caption's ranges.
- What the figure cannot say: in its densest part the dots run into
  solid black. The cells 140,85, 150,85 and 160,85 are held at the
  most the method gives, so the core is, if anything, under-weighted.
  Dots under the labels, arrows and star are lost; those parts are
  sparse.
- Sec. 2, p. 5 agrees with the reading: the orbits' nodes turn away
  from the ecliptic's by a rotation "broadly centered at ~30 deg",
  which puts them near 156 degrees, where the densest cells are.

## 3. What was built

`patch_L421_5_oort_orrery_20261010.py`. Every number that reaches the
picture or a hover is a row in `constants_new.py`.

**New rows in `constants_new.py`**, in a block after the Oort cloud's
edges, each with Unit, Status, Figures, Read, Source and Access:
- `INNER_OORT_DISK_OUTER_AU` = 10000, measured: sec. 1, p. 2 (the
  inner cloud at 1,000 < r < 10,000 au; the outer cloud at r > 10,000
  au roughly spherical). The band's near end.
- `HILLS_CLOUD_TILT_DEG` = 30, measured: sec. 1, p. 3 ("inclined i ~ 30
  deg to the ecliptic"). Printed by the hovers; the drawing's tilt is
  not set to it.
- `ECLIPTIC_NODE_GALACTIC_LON_DEG` = 186, measured: Fig. 3 caption,
  p. 19, and sec. 2, p. 5. Turns the paper's galactic longitudes into
  the frame the pole matrix builds.
- `HILLS_CLOUD_PERI_ARG_BAND1_LOW_DEG` / `_HIGH_DEG` = 70 / 180 and
  `HILLS_CLOUD_PERI_ARG_BAND2_LOW_DEG` / `_HIGH_DEG` = 250 / 360,
  measured: Fig. 2 caption, p. 18. The two arms.
- `HILLS_CLOUD_NODE_LOW_DEG` / `_HIGH_DEG` = 120 / 180 and
  `HILLS_CLOUD_INCL_GAL_LOW_DEG` / `_HIGH_DEG` = 75 / 90, measured:
  Fig. 3 caption, p. 19. Not drawn from; the sampler checks the reading
  against them.
- `HILLS_CLOUD_PLANES_READ`, declared: the Fig. 3 table, one entry per
  line keyed "node,inclination" (the constants change report reads a
  dict entry only on its own line, and a row name with a digit in it
  was refused, so the name carries none).
- `HILLS_CLOUD_PLANES_NODE_CELL_DEG` = 10 and
  `HILLS_CLOUD_PLANES_INCL_CELL_DEG` = 5, declared: the table's cells.
- `HILLS_CLOUD_ECCENTRICITY` = 0.8, declared: the paper shows today's
  eccentricities only as a plot (Fig. 6, p. 22); 0.8 makes the dots
  gather at the orbits' far ends, where the arms are. Tony's confirmed
  words already say it is chosen for the picture.
- `INNER_OORT_CLOUD_AU` keeps its value and source; its Note now says
  it is also the band's far end.

`constants_tokens.py`: two named-number tokens, `eccentricity` and
`dot_count`.

**`pole_frames.py`, new:** `create_pole_transformation_matrix` moved
there from `idealized_orbits.py` byte for byte, so code with no Plotly
or Tk can use it. `idealized_orbits.py` imports it from there, so every
caller, the galactic tide included, is unchanged.

**`hills_cloud_sampler.py`, new:** pure Python and numpy. Each orbit's
plane is a cell of the Fig. 3 table, chosen in proportion to its count,
then a point evenly inside it. Its argument of perihelion is picked in
one of the two bands, half the orbits each. Its far end is picked evenly
from `INNER_LIMIT_OORT_CLOUD_AU` to `INNER_OORT_DISK_OUTER_AU`, then
with a chance falling evenly to nothing at `INNER_OORT_CLOUD_AU`. Dots
go along each orbit evenly in time. `sample_hills_cloud(n_orbits,
points_per_orbit, rows=None, seed=None)` returns the dots in AU in the
drawing frame; `check()` runs the three checks; run it to print them.

**`solar_visualization_shells.py`:**
- `create_sun_hills_cloud_torus` draws the sampler's 600 orbits of 6
  dots, 3,600, the torus's count. Its typed `inner_radius=2000` and
  `outer_radius=20000` are gone. The name is kept because the dispatch
  calls it by it; the legend reads "Sun: Hills Cloud (tilted disk)".
  `customdata` stays "Hills Cloud Torus"; nothing in either repo keys on
  the old legend name (searched).
- `create_sun_outer_oort_clumpy`: its typed `radius_min=20000` and
  `radius_max=100000` read the rows now, and the clumps fill in across
  the band.
- `create_sun_galactic_tide`: its points start at the band's near end
  and fill in across it. The cone is unchanged, from 20,000 au.
- Shared fragments `_OORT_DISK_EDGE`, `_HILLS_TILT`,
  `OORT_BAND_SENTENCE` and `INNER_OORT_BAND_NOTE`, each printed from
  its row.
- The two comments citing Hills (1981) now cite the rows' sources.

**`palomas_orrery.py`:** the checkbox reads "-- Hills Cloud (tilted
disk)". **`orrery_maintenance_run.py`:** a 22nd gating checker, Hills
cloud sampler (L-421).

**`test_hills_cloud_sampler.py`, new:** each check shown failing on a
planted fault first -- the pole's RA and Dec swapped (frame), the node
row set to 0 (frame), the reading moved 120 degrees (reading), the tilt
row set to 60 (tilt) -- then the real rows. The first plant passed the
frame check by chance on longitude alone, so the frame check now reads
Sgr A*'s latitude too.

## 4. Where this differs from the brief, and why

- **A new row for 10,000 au**, not NASA's row with a second source.
  `OORT_CLOUD_OUTER_EDGE_LOW_AU` is NASA's low end of the whole cloud's
  outer edge; the paper's 10,000 au is where the inner disk gives way
  to the round cloud. They print the same number but are two
  quantities, so citing the paper on NASA's row would cite it for
  something it does not say. Each keeps its own row and source. (The
  design record, section 3, had proposed the new row.)
- **The node is a measured row, not a derived one.** The paper prints
  it, and the sampler checks the frame it gives against Sgr A*'s rows.
  A derived row would agree with itself by construction and check
  nothing.
- **The orbits' planes follow Fig. 3, not the captions' ranges**, by
  Tony's ruling of 18:27 (section 1).
- **The tilt check measures the plane through the dots**, not the
  average of the orbits' tilts. The paper's "about 30" is the tilt of
  the disk, the bodies together.

## 5. Verification

On copies, never on the deliverable (agentic-pre-test 1.3):
- Every changed file compiles.
- The sampler's checks: the plane through the dots 34.1 degrees from
  the ecliptic (judged on 4,000 orbits); the orbits' own tilts averaging
  40.8, spread 16.3; the two arms toward ecliptic longitudes 22 and 203,
  within 8 degrees of the ecliptic, the paper's "main axis aligned with
  the ecliptic"; Sgr A* at galactic longitude -0.44, latitude -0.05;
  12% of the dots inside 2,000 au, as orbits passing their near ends
  put them; 20% beyond 10,000 au.
- The orrery window, headless, ran until its timeout with no error.
- The live dispatch (`create_celestial_body_visualization`, Sun, the
  four Oort shells on) called the rewritten Hills cloud builder, shown
  by a spy: 3,600 dots from 230 to 19,496 au; the clumps from 12,752 au;
  the tide from 10,494 au; the inner Oort sphere at 20,000 au. Each
  hover printed and read; the new lines are at most 97 characters.
- The maintenance run on 32619f8 plus patch_L395_7 (21 of 21), then
  with this build: "22 of 22 gating checkers passed"; "GATE PATH: 0
  TIER-1 -- the push gate holds", 95 of 120 exported rows examined.
- Tier-1 in the whole tree: 293 before, 292 after, with this patch
  script in the root. The one that went is not a real clearing: it is
  `solar_visualization_shells.py`'s module docstring ("display string @
  line 1", 8 claims), which now names Nesvorny et al. (2025) in its
  credit block, so the scanner reads its numbers as cited. Those
  numbers describe the code (shell counts, point counts), not nature.
  `hills_cloud_sampler.py` carries none: its point counts and the
  checks' tolerances are passed as arguments, rendering settings kept
  where they are used.
- The patch on that base (the result matches the built files byte for
  byte), a second time (it says "already applied" and writes nothing),
  on 32619f8 without patch_L395_7 (it refuses, naming that patch), and
  on a copy with Windows line endings (written LF, each file named).

## 6. For the gallery session

- **Rows in `data/constants_export.json`:** `INNER_OORT_DISK_OUTER_AU`,
  `HILLS_CLOUD_TILT_DEG`, `ECLIPTIC_NODE_GALACTIC_LON_DEG`, the four
  `HILLS_CLOUD_PERI_ARG_BAND*` rows, the four caption rows
  (`HILLS_CLOUD_NODE_*`, `HILLS_CLOUD_INCL_GAL_*`),
  `HILLS_CLOUD_PLANES_READ` (a dict, unit `dot_count`), the two cell
  rows, `HILLS_CLOUD_ECCENTRICITY`. Tokens `eccentricity` and
  `dot_count`.
- **The sampler** is `hills_cloud_sampler.py` with `pole_frames.py`,
  numpy only. Inputs: those rows plus `INNER_LIMIT_OORT_CLOUD_AU`,
  `INNER_OORT_CLOUD_AU`, the two galactic pole rows, Sgr A*'s two
  degree rows and `EARTH_OBLIQUITY_J2000_DEG`. Serving its points or
  re-sampling in the browser is the gallery session's decision.
- **The words,** Tony's confirmed words of 2026-10-09 (design record
  sections 4, 5, 9). One clause changed so it says what is drawn, and
  it comes to Tony with the gallery words: the note's "picked within
  the ranges the model gives" became "picked where the model's orbits
  lie (its Fig. 3)".
- Owed there too: L-408 (the galactic plane on the phone) with its
  poles and Sgr A*, as Tony ruled 2026-10-09; the L-363 `_declared`
  "1.1 times" fix; the cache rebuild; the phone look.

## 7. Mode 5, Tony's look in the orrery window

Centre on the Sun; under the Sun's shells tick Hills Cloud (tilted
disk), the clumpy outer Oort cloud, the galactic tide and the Inner
Oort Cloud sphere; plot, and turn it.
1. The Hills cloud is a disk tipped against the planets' plane, its
   dots thickest along two opposite arms near the ecliptic.
2. The clumps and the tide begin thin inside the Inner Oort Cloud
   sphere (20,000 au) and are full outside it.
3. The hovers read as in section 8.
Looks wrong? The frame is the suspect first: the galactic pole rows
and the node row.

## 8. Words changed in the orrery, old and new

Hills cloud: replaced by Tony's confirmed words with the citation (in
the hover and `hills_cloud_torus_info`). The torus text, its "toroidal"
shape and its uncited list are gone.

Galactic tide hover (Tony's approved words of 2026-10-02), one line:
- old: "From 20,000 to 100,000 AU"
- new: "From 10,000 AU, filling in by 20,000 AU, to 100,000 AU"

Clumpy outer cloud hover:
- old: "20,000-100,000+ AU"
- new: "From 10,000 AU, filling in by 20,000 AU, to 100,000+ AU" and a
  line "It begins where the inner cloud's disk thins out"

Inner Oort Cloud sphere (hover and tooltip): a first line added, "The
inner cloud gives way to the round outer cloud between 10,000 and
20,000 AU; this sphere is drawn at 20,000 AU, the far end."

Every string that printed the single 20,000 au edge (the gravitational
reach, the inner limit, the inner cloud, the clumps' and the tide's
tooltips) now says "between 10,000 and 20,000 AU" where it meant the
boundary; the tooltips' structure line says "a disk tilted about 30
degrees to the ecliptic" where it said "disk-like/toroidal".

## 9. Found, and where each went

- Uncited lines in the orrery's Oort tooltips and the Sun's
  gravitational-reach text -- the 1 to 100 trillion objects, 2012
  VP113, NEOWISE, short-period comets and a disk, Sedna's 936 AU --
  are one class, recorded as L-430, not chased.
- The paper's Fig. 3 is a picture, and its densest part cannot be
  counted. Recorded on the table's row and in section 2.

## 10. Tony's steps

1. **(do)** In the orrery repo's root folder, run
   `patch_L395_7_records_20261010.py` first if you have not, then
   `patch_L421_5_oort_orrery_20261010.py`, then
   `orrery_maintenance_run.py`. Expect "22 of 22 gating checkers
   passed".
2. **(do)** The look, section 7.
3. **(do)** Move both patch scripts into `documentation/`; commit and
   push. The gallery session starts from that push.

## 11. What travels

- From last session, unchanged: once patch_L395_7 is run and the two
  skills are reinstalled, the next session confirms its loaded copies
  read ledger-and-session-records 1.19 and horizons-orbital-mechanics
  1.2.
- No skill version changed this session.
- Next on the road: the gallery side of the inner Oort cloud, with
  L-408, then L-421's check (part 2) and the citation agreement (part
  3).
