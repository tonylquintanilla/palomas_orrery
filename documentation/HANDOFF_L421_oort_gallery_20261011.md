<!-- Doc-Kind: hand | Build record for L-421 (the typed facts), the inner Oort cloud, website side, with L-408 (the galactic plane in the Sun room): the orrery stores the Hills cloud's dots and the website draws them, the band, the served words, the Galactic Plane row; Tony's runs and look. Written October 11, 2026. -->
# Handoff: L-421 (the typed facts), the inner Oort cloud, website side, built

Built on orrery 84d329a12575d923daa06ffa104012ce11abc925 ("L431 run
record notes") at https://github.com/tonylquintanilla/palomas_orrery
and gallery fd17abf1cf99169289acfeb0a45f84365265c255 ("daily run") at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, both
pinned with `git ls-remote` at the session's start. Middle push: orrery
1bbd9fe160471cbd3c3a036e4b750c314bf88c88 (patch_L421_6). Gallery
pushed at e5a3d13f64ea493d8b5142e2d05e40030d483ac8 (patch_L421_7). The
close, `patch_L421_9_close_20261011.py` (orrery) and
`patch_L421_8_suite_line_endings_20261011.py` (gallery), is built on
those two.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Every patch of this session was saved there directly; the session was
linked to Tony's computer.

- Type: BUILD, gallery with one orrery patch, and the close.
- From `documentation/HANDOFF_L421_oort_gallery_build_brief_20261011.md`
  (the brief, also attached in chat), the orrery record
  `documentation/HANDOFF_L421_oort_orrery_20261010.md` and the design
  record `documentation/DESIGN_L421_inner_oort_tilt_20261009.md`.
- Companion: `documentation/WHERE_WE_ARE_10-11-26_1311_run_record.md`,
  Tony's run record, the primary record of his rulings and looks.
- Skills loaded, each read back and each matching protocol v3.90's
  manifest: interactive-exhibit 1.14, gallery-cache-builder 1.8,
  ledger-and-session-records 1.19 (the three obligations the brief
  carried), safe-file-editing 1.13, agentic-pre-test 1.3,
  gallery-assembler 1.3, provenance-discipline 2.28.

Session written October 2026 with Anthropic's Claude Opus 5.5.

## Read this first

- *The website draws the Hills cloud from the orrery's own 3,600 dots.
  The orrery places them; the website places none. Tony's look on the
  phone: correct, "beautiful".*
- *The clumps and the galactic tide begin thin at 10,000 AU and are
  full by 20,000 AU, as the orrery draws them. L-408's Galactic Plane
  row is live and closed.*
- *ledger-and-session-records goes to 1.20: every handoff, brief and
  design record names Tony's two local folders in its header. The next
  session confirms its loaded copy reads 1.20.*

## 1. Rulings this session

- **How the website gets the dots: "A"** (Tony, 10:59). Put to him as
  three ways in one message: A, the orrery exports the dots and the
  website draws them; B, a copy of the sampler in the gallery; C, a
  second sampler in JavaScript. Recommendation A.
- **Other shells** (Tony asked, 10:54): stored drawings fit shapes of
  scattered dots placed by random numbers or a model; shapes that are a
  few numbers and a formula stay computed. Where the files live:
  `data/drawings/` in both repositories, the served copy in
  `data/solar-system/drawings/`. A new ledger item for the rest. Tony,
  11:04: "Confirmed as recommended". It is L-434.
- **Ignored JSON in data/** (Tony asked, 11:08): checked with git's own
  rule test in both repositories; neither ignores the new paths, and git
  has no size rule. The orrery's checker now fails if git ever ignores
  the file.
- **The changed clause** in the Hills cloud's note, "picked where the
  model's orbits lie (its Fig. 3)": Tony, "correct".
- **The dashboard:** "please add this and any other new checks to the
  dashboard" (beside the pull, in the run record). Done in the close.
- **The skill:** ledger-and-session-records 1.20 with the folders rule
  recorded on L-351, one version only (Tony's opening message).

## 2. What was built

**Orrery, `patch_L421_6_drawings_export_20261011.py`** (pushed 1bbd9fe1):
- `hills_cloud_sampler.py`: `drawn_hills_cloud()`, the cloud as drawn,
  its three settings (600 orbits, 6 dots each, seed 421) written once,
  as function defaults like the module's other settings.
- `solar_visualization_shells.py`: the orrery window draws
  `drawn_hills_cloud()`; every plot is the same cloud (L-239 for this
  builder).
- `export_drawings.py` (new, the ninth generator): writes
  `data/drawings/hills_cloud.json` -- 3,600 dots in AU, rounded to whole
  AU, with the settings, the rows' names and their sha256, and the
  fitted plane's tilt. Written only when the dots change, LF.
- `test_drawings_export.py` (new, the 23rd gating checker): the file is
  the drawing its rows give today, git does not ignore it, its tilt
  matches; three faults planted first (a dot moved, the eccentricity
  row changed, the file reported ignored).
- Two dashboard buttons: Drawings Export, Test Drawings Export.

**Gallery, `patch_L421_7_oort_gallery_20261011.py`** (pushed e5a3d13f):
- `data/objects_config.json`: the Hills cloud is "Hills Cloud (tilted
  disk)", shape `served_dots`, `drawing.dots` "hills_cloud"; its
  served hover, description, about and note in Tony's confirmed words
  (design record sections 4, 5, 9), with {tilt}, {near}, {far}; linked
  rows `tilt` (HILLS_CLOUD_TILT_DEG) and `thins_from`
  (INNER_OORT_DISK_OUTER_AU), each with the paper's full citation and
  its arXiv link for the i panel. The clumps and the tide: `inner_radius`
  to INNER_OORT_DISK_OUTER_AU, a new `full_from` (INNER_OORT_CLOUD_AU),
  the clumps' hover with the orrery's "It begins where the inner
  cloud's disk thins out." The Inner Oort Cloud sphere: a served range
  and a note naming the band. L-408's `galactic_plane`. The Solar
  System room's "1.2 times" (L-363). Structure by the patch, words as
  the store writer writes them, numbers as the mirror writes them; the
  mirror settles on it unchanged.
- `gallery/feature_renderers.js`: `setDrawings()` and `drawingNames()`;
  the Hills cloud from the served dots; `HILLS_CAVEAT` and
  `torusPoints` gone; `bandKeep()`, the orrery's `_outer_cloud_keep()`
  rule, for the clumps and the tide; `withFilledWords()` for an about or
  note naming rows; `renderGalacticPlane()`.
- `interactive.html`: before a room is drawn, each named drawing is
  fetched from the served cache and handed over; one that cannot be read
  is reported and only its shape is missing.
- `tools/gallery_cache_builder.py`: `serve_drawings()` copies each named
  drawing into the served cache, LF, and ABORTs by name if one is
  missing.
- `tools/pull_drawings.py` (new generator), `tools/check_drawings.py`
  (new gating checker: pulled, served byte for byte, the tilt fitted
  again by its own arithmetic, three planted faults).
- Checks updated for the drawing: the builder's offline suite, Sun
  shells (46 checks: the dots as served, the tilt, the band's fade, the
  galactic plane's ring, poles, centre and angle), display figures (the
  fixture re-recorded as
  `documentation/fixture_hovers_L421_3_on_fd17abf1.json`, exactly the
  Oort hovers different), arrival, hover budget, the siblings report
  (`data/drawings/` known by exact name).

**The close:** gallery `patch_L421_8_suite_line_endings_20261011.py`
(section 4) and orrery `patch_L421_9_close_20261011.py`: the ledger,
Tony's page by section, this record, the dashboard's two gallery
buttons, ledger-and-session-records 1.20, the protocol to v3.91.

## 3. Verification before anything reached Tony

- Both patches on clean copies, a second time ("already applied"), on
  copies with Windows line endings (written LF, named), and from a wrong
  folder (refused).
- Orrery maintenance run on a copy: 23 of 23, gate path 0, whole tree
  292 (a first draft named the settings as module constants and the
  scanner counted two Tier-1 off the gate path; moved to function
  arguments, back to 292). The window opened headless; the live
  dispatch drew exactly the file's dots.
- Gallery maintenance run on a copy after a stand-in cache rebuild (the
  features copied as the builder copies them): 27 of 27. The real cache
  rebuild needs JPL and was Tony's.
- The Sun room, headless (`tools/headless`, the real page and driver):
  booted with no error; 3,600 dots; every trace keyed; the words filled;
  the Galactic Plane's six traces hidden at arrival, drawn when its row
  is ticked. With the drawing removed: two warnings, the Hills cloud
  absent, the room ready.
- The drawn plane: 30.9 degrees, by the sampler and again by the
  gallery checker's own arithmetic.
- The typed-facts survey (the method of 2026-10-06, by hand): the Sun
  room typed one fact about nature before this build, none after.
- The Wikipedia link for the galactic plane answered and places the
  north galactic pole in Coma Berenices.

## 4. Tony's runs and look, and the one red line

From `documentation/WHERE_WE_ARE_10-11-26_1311_run_record.md`:
- Orrery: patch_L421_6, the maintenance run, "23 of 23", gate path 0;
  pushed at 1bbd9fe1.
- Gallery: patch_L421_7; the pull ("Pulled drawings from orrery
  1bbd9fe1: hills_cloud (3600 dots)"); the Daily Run: the cache built
  (run 20261011T183843Z, every rename first try), the maintenance run
  26 of 27; pushed at e5a3d13f.
- The red line: the builder suite's "L-421: every named drawing served
  byte for byte". The suite wrote its stand-in drawing as text, CRLF on
  Windows; the builder serves every drawing LF, as it should. Reproduced
  here by giving the stand-in CRLF; fixed by writing it as bytes, with a
  new check that a CRLF drawing is served LF. 234 checks.
- The phone, each "correct": the tilted disk with its arms; the text box
  with three distances and "about 30 degrees"; the clumps and the tide
  thin inside the Inner Oort Cloud sphere; the Galactic Plane edge-on,
  a pole marker, the i panel's "60 degrees". Two screenshots in chat.
  Tony: "beautiful. thanks."

## 5. Found, and where each went

- The other scattered-dot shells (the streamer band, the clumps, the
  tide): L-434, opened.
- The clumps and the tide still unseeded in the orrery: L-239.
- The served-drawing contract, undescribed in interactive-exhibit:
  owed to its next version on L-351 (nothing in it is wrong; carried,
  not bumped).
- The tide's cone and brightness on the phone, L-408's one unruled
  point: re-homed to L-412 at L-408's close.
- The run-record zone's two sentences ("no patch edits below the
  marker" and "the close empties the live zone"), owed on L-351 since
  2026-10-08: left owed. Tony's words beside it can be read two ways,
  and this version carries only the rule he named.
- The gallery's `patch_L421_7` was not yet in `documentation/` at
  e5a3d13f; the gallery fix's NEXT says so.

## 6. Tony's steps

1. **(do)** Gallery: run `patch_L421_8_suite_line_endings_20261011.py`,
   then `gallery_maintenance_run.py` ("234 checks", "27 of 27"); move it
   and `patch_L421_7` into `documentation/`; commit and push; then the
   live run.
2. **(do)** Orrery: run `patch_L421_9_close_20261011.py`, then
   `orrery_maintenance_run.py` (23 of 23; it rewrites the skill's read
   plan, the manifest row and the ledger's index); move the script and
   the orrery's `patch_L421_6` if still in the root into
   `documentation/`; commit and push.
3. **(do)** Upload `skills/ledger-and-session-records/SKILL.md`
   (Settings > Skills) and replace the Project's instructions with
   `PROJECT_INSTRUCTIONS.md` (v3.91).

## 7. What travels

- ledger-and-session-records went to 1.20 at this close; this session
  loaded 1.19. The next session confirms its loaded copy reads 1.20
  before ledger or handoff work.
- Next on the road: L-421's check (part 2) and the citation agreement
  (part 3); the orbital periods (L-431) are with the other session.
