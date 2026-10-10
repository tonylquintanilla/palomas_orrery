<!-- Doc-Kind: hand | Brief for the orrery side of the inner Oort cloud redraw (L-421, the typed facts): the new rows, the Hills cloud drawn as dots along orbits with its two arms and its tilt, the fuzzy band from 10,000 to 20,000 au, the export. The gallery side is a later session. Written October 9, 2026. -->
# Handoff: L-421 (the typed facts), the inner Oort cloud, the orrery-side build brief

Built on orrery aa46bb1 at https://github.com/tonylquintanilla/palomas_orrery
as read; this session starts AFTER Tony's L-414 push, so it pins HEAD
itself and confirms two things before building: `test_row_run.py`
exists at the repo root (L-414 landed) and the October 9 design record
is in documentation/. Gallery at 5ec4739b, read for what it serves, not
touched. Written by the Fable 5.1 coordination session of October 9,
which read the repo at HEAD and wrote no patch.

- Type: BUILD, orrery only. One patch: constants_new.py,
  solar_visualization_shells.py, shell_configs.py, a small new module
  for the orbit sampling, the ledger, Tony's page, a handoff. The
  gallery side (the mirror, the renderers, L-408's ring, the served
  words, the cache rebuild, the phone look) is the NEXT session, from
  its own brief, once this session's export is pushed.
- Inputs: the design record of October 9 (the Oort cloud design
  talk, its sections 1, 2a, 2, 3, 4, 5, 8, 9 and 10); L-421's block;
  the paper, Nesvorny et al. (2025), ApJ 983:1, arXiv:2502.11252v1,
  which Tony uploads from his papers/ folder (git never commits it).
- Skills this session fires: provenance-discipline (expected 2.28;
  the obligation from L-414 is that this session confirms its loaded
  copy reads 2.28 and its folder holds both reference files, and opens
  `references/figures.md` BEFORE writing any `# Figures:` line and
  says so), orrery-coding-conventions 1.10 (shells, hover text, the
  single info marker, render size), safe-file-editing 1.13,
  agentic-pre-test 1.3, ledger-and-session-records 1.18. Read back
  each loaded version in the first reply. The protocol is
  PROJECT_INSTRUCTIONS.md v3.87.

## Read this first

- *The design is ruled. The drawing is option A: dots along orbits
  picked inside the paper's ranges, so the tilt and the two arms come
  out of the orbits. The hover says "about 30 degrees" from a sourced
  row; the drawing's tilt is whatever the orbits give.*
- *One drawing question is still open and is asked FIRST, in one
  message (section 2). Nothing else needs Tony before the build.*
- *Every number that reaches a picture or a hover comes from a row in
  constants_new.py. The eccentricity is a declared row with its reason;
  nothing is typed.*
- *Before any dots are drawn, the sampler prints the mean tilt of its
  orbits to the ecliptic. Near 30 is the pass. This is the one check
  that can fail on the mechanism rather than on the picture.*

## 1. What is settled (from the design record, in Tony's rulings)

- The inner cloud gives way to the outer cloud across a fuzzy band
  from 10,000 to 20,000 au, both ends sourced: 10,000 from Nesvorny et
  al. (2025) (beyond it the cloud is roughly spherical), 20,000 from
  Portegies Zwart et al. (2021) ("about 20,000 au or less"). The disk
  is full to the near end and thins to nothing by the far end; the
  clumps and the tide are thin at the near end and full by the far
  end. Same point counts, spread differently; the render does not grow.
- The Hills cloud is drawn as dots along orbits picked inside the
  paper's stated ranges (Fig. 2: omegaG 70 to 180 and 250 to 360
  degrees; Fig. 3: iG 75 to 90 degrees, OmegaG 120 to 180 degrees; the
  ecliptic's ascending node at galactic longitude 186 degrees),
  turned into the ecliptic frame by the served galactic pole. The
  eccentricity is not stated in the paper (Fig. 6 shows it only as a
  plot): a declared pick with its reason on the row.
- The hover's words, the i panel's `about` and `note`, confirmed with
  the arms (record sections 4, 5, 9). The orrery's own torus hover
  (`hills_hover`) and `hills_cloud_torus_info` take the same words, in
  the orrery's convention (the full citation may sit in the hover
  there; on the website it goes to the panel).
- The "Inner Oort Cloud" sphere draws one line, which a band does not
  have. It follows Tony's ruling of 2026-10-03 for the cloud's other
  edges: one sphere, its hover giving the range and saying which end
  is drawn. Which end is a small question for the hover round; default
  to the far end (20,000 au, the row it reads today) and say so.
- L-408 (the galactic plane in the Sun room) rides the GALLERY
  session, not this one. Its only orrery need, the Sgr A* rows, is
  already met (L-420).

## 2. The one question first

The paper places the inner cloud at 1,000 to 10,000 au (sec. 1, p. 2;
sec. 5, p. 11) and also calls the disk "roughly 15,000 au across"
(sec. 1, p. 3; the abstract), which read as a diameter is a radius near
7,500 au; its Fig. 1 plots only a < 5,000 au. Tony confirmed "full out
to 10,000 au". Put to him in one message: keep the band's near end at
10,000 au (the paper's own stated range, and the row that already
exists), or move the disk's full extent nearer 7,500 au with the band
starting there. Recommendation: keep 10,000; the hover already says
"about", and the stated range is the paper's sentence while "across"
is a description of the spiral seen from afar. Either answer is built
the same way; only one row differs.

## 3. The rows (provenance-discipline governs every line)

- **No second 10,000 au row.** `OORT_CLOUD_OUTER_EDGE_LOW_AU = 10000`
  exists, sourced to NASA's Oort Cloud Facts. The band's near end reads
  it. Nesvorny et al. (2025) is added to that row the way the skill
  records a second independent source (sec. 1 p. 2 and footnote 7),
  not as a new row. One value, one home.
- **The far end** reads `INNER_OORT_CLOUD_AU = 20000` (Portegies
  Zwart 2021), unchanged. Its Note already says the transition is
  unclear; the band is that Note drawn.
- **New, sourced:** the tilt, 30 degrees (sec. 1 p. 3, "i ~ 30 deg";
  Figures per `references/figures.md`, read first); the omegaG ranges
  (two low/high pairs, Fig. 2 caption); the iG range (Fig. 3); the
  OmegaG range (Fig. 3); the ecliptic's ascending node at l = 186
  degrees (Fig. 3 caption), unless it is derivable from the pole rows
  already in the file, in which case it is a derived row and says so.
  Each with Source, Read (page and figure), Access (the arXiv address,
  open full text, the date) and its Figures line.
- **New, declared:** the orbits' eccentricity, `# Status: declared`
  with the reason (the paper shows it only as a plot, Fig. 6; the pick
  and why). The scanner after L-414 reads a declared row as its own
  kind and never scores it Tier-1; the audit lists it under Declared
  Rows.
- Row names follow the file's own pattern (HILLS_CLOUD_..., the
  _LOW/_HIGH pairs as OORT_CLOUD_INNER_EDGE does). Every row carries
  its Unit line. The row-shape, status-line, dimensions and relations
  checkers must all pass; the gate-path line must read 0.
- The stale comments over `inner_oort_info` and
  `hills_cloud_torus_info` ("Source: Hills (1981)") are corrected to
  the row's real source, as L-371 already did for the row itself.

## 4. The drawing

- **The sampler is its own small module**, pure Python, no Plotly, no
  Tk: given the rows (the band's ends, the ranges, the eccentricity
  pick, the galactic pole rows, the node), it returns the points. Why:
  the gallery will need the same points, and its nightly builder
  already computes served geometry in Python (render_orbits.py). A
  sampler with no GUI dependence can be carried to it; one in a
  Plotly builder cannot. Whether the gallery serves the computed
  points or re-samples in the browser is the gallery session's
  decision, not this one's; this session only keeps the door open.
- **The frame.** Orbits are drawn in the galactic frame (the paper's
  angles) and turned to the ecliptic by the same transform
  `create_sun_galactic_tide` already uses for the pole. Reuse it; do
  not write a second one (Duplicate rendering: extract to a source
  module).
- **The check that can fail.** Before the first picture, the sampler
  prints: how many orbits, how many points, the mean and spread of the
  orbits' inclination to the ecliptic, and the two arms' directions.
  Pass: the mean inclination is near 30 degrees and the arm directions
  fall in the paper's two omegaG bands. If the mean is far from 30,
  the ranges or the transform are wrong; stop and say so before
  drawing anything.
- **Points.** The torus's 3,600 (render size, Tony's standing
  concern). Points crowd at the orbits' far ends on their own; no
  weighting is added by hand. The thinning across the band comes from
  the orbit sample, not from deleting points after the fact, and the
  method is one sentence in the module's docstring.
- **`create_sun_hills_cloud_torus`** is rewritten to read the sampler;
  its typed defaults (`inner_radius=2000, outer_radius=20000`) go, and
  so does `create_sun_outer_oort_clumpy`'s `radius_min=20000`; both read
  rows. `planet_visualization.py` calls both with no arguments, so this
  is where the typed numbers were drawing.
- **The clumps and the tide** become thin at the near end and full by
  the far end. Their hovers say the band in words (the three served
  rows, formatted through `row_text` as today's `_OORT_HILLS_EDGE`
  is). Check all twelve strings that read `_OORT_HILLS_EDGE` still say
  something true once the edge is a band.
- **The single info marker** carries the hover (orrery-coding-
  conventions): geometry points `hoverinfo='skip'`, one marker at an
  uncluttered spot. Hover text in plain words, AU and km both.
- **shell_configs.py**: the `inner_oort` shell's `radius_au`, and any
  entry that names the torus's shape.
- Credit line in each module touched ("Module updated: October 2026
  with Anthropic's Claude Opus 5.5").

## 5. Tests (agentic-pre-test, throwaway copies)

- py_compile on every changed file and the patch.
- The sampler's own test: the printed tilt check above, pinned as a
  test that FAILS when the pole rows are swapped or the node is set to
  zero, so the pass means something.
- The xvfb run of the orrery with the Sun's shells on: Hills cloud,
  clumps, tide, inner Oort sphere drawn; the console shows no
  caught-error print; the live-dispatch smoke test confirms the
  rewritten builders are the ones called (map the dispatch; grep for
  the CALLS).
- orrery_maintenance_run.py on the patched copy: 21 of 21 gating
  checkers; "Scanner row run (L-414)" 16 of 16; the scanner's last
  line "GATE PATH: 0 TIER-1 -- the push gate holds"; the constants
  export regenerated with the new rows and its check passing.
- The patch on a clean clone, a second time over (refuses), and a
  CRLF copy.

## 6. Mode 5 and Tony's steps

- Tony's look is in the orrery's own window: the Sun with the Hills
  cloud, the clumps, the tide and the inner Oort sphere, turned in
  three dimensions. The patch's steps tell him which checkboxes.
  Looks wrong? Check reference frames first (the galactic pole
  transform is the suspect).
- Steps printed by the patch: run from the repo root (VS Code, Run);
  open the orrery and look; run orrery_maintenance_run.py; move the
  script into documentation/; commit and push. The gallery session
  starts from that push.

## 7. At the close

- The ledger: L-421 (the typed facts) records the orrery side done,
  by name: rows added, builders rewritten, the typed defaults gone;
  its Gap narrows to the gallery side, then the check (part 2), then
  the citation-agreement check (part 3). The design record is cited.
  L-408 gains one line: rides the gallery session. L-363's `_declared`
  "1.1 times" fix is still owed to the gallery session; say so.
- Tony's page, by section, handles labelled, nothing below the marker:
  the box says what the orrery now draws and that the website follows
  in the next session; road stage 6 updated.
- The handoff: `documentation/HANDOFF_L421_oort_orrery_20261009.md`
  (or the closing date), anchored on HEAD at start and at close, and
  carrying what the gallery session needs: the row names, the
  sampler's module name and its inputs, the export's new keys, and
  the confirmed words.

## 8. Not this session

- The gallery: `tools/mirror_constants.py`, `data/objects_config.json`,
  `gallery/feature_renderers.js`, `HILLS_CAVEAT`, the served `hover`,
  `about`, `note`, L-408's ring, poles and Sgr A*, the cache rebuild,
  the phone look.
- Part 2 of L-421 (the gating survey check) and part 3 (the
  citation-agreement check).
- L-425 (citation location checks): Tony has not ruled; nothing
  rides here.

Brief written October 9, 2026, with Anthropic's Claude Fable 5.1.
