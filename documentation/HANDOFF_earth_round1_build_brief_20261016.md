<!-- Doc-Kind: hand | Build brief from Earth's design talk, round 1: the belts curved as a density field (L-330, render first), the eight held sentences (L-451), citation wording into the store and the website's notes cut to drawing choices (L-452, L-450), the run records kept and their loss stopped (L-449), and the unturned magnetosphere said in its hover (L-314). -->
# Brief: Earth round 1, the build (L-330, L-451, L-452, L-450, L-449, L-314)

Built on orrery 48c84c3 ("Update WHERE_WE_ARE_10-16-26_1708_run_record.md";
the code and the ledger are 25a99ee's, "L421 close") at
https://github.com/tonylquintanilla/palomas_orrery, and gallery 2090a8b
("patch km radius label") at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
The design talk's ledger patch, `patch_earth_round1_close_20261016.py`,
lands on top of 48c84c3; the build starts from whatever HEAD Tony's push
of it gives, and says that SHA.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\
Written October 16, 2026 with Anthropic's Claude Opus 5.5, at the close
of the design talk.

- Type: BUILD. Three patches or fewer, one repository at a time, every
  run green between them; a throwaway render and Tony's look before the
  belts are built in either instrument.
- Companion: `documentation/DESIGN_earth_round1_rulings_20261016.md`,
  every ruling below in Tony's words. Read it first; this brief does not
  restate the reasons.
- Ledger: L-330, L-451, L-452, L-450, L-449, L-314, under L-413
  (Earth's list), road stage 5. Read the blocks at HEAD, not from here.
- The natural break, if this is two sessions: Tony's look at the
  render. Patch 1 (L-449) does not wait for it.

## 0. Before the build

- Pull both repositories at HEAD and pin them. The orrery should be the
  design talk's push on top of 48c84c3; the gallery 2090a8b plus any
  Daily Run commits. Reconcile anything else before building.
- Skills this build fires, each confirmed at load against the manifest:
  interactive-exhibit (1.16), gallery-cache-builder (1.10),
  orrery-coding-conventions (1.10), provenance-discipline (2.29),
  safe-file-editing (1.13), agentic-pre-test (1.3),
  ledger-and-session-records (1.21). horizons-orbital-mechanics 1.8
  still travels; nothing here fires it.
- The Register Rule: Tony reads this build's messages on a phone or in a
  chair. One question per message.

## 1. The one decision for the build's start

- (decide) When the Daily Run finds run records missing after a build
  (section 3, patch 1), does it stop and name them, leaving the
  putting-back to Tony's word as both times on 2026-10-15 and 10-16; or
  does it put them back from `data/solar-system.prev` itself and say so?
  Claude's recommendation: stop and name them, printing where the
  copies are. Putting files back automatically hides the event the
  check exists to show, while the cause is unknown.

## 2. The throwaway render (no patch) and Tony's look

Ruled (L-330): both belts drawn curved along dipole field lines (option
A), as a DENSITY FIELD, two versions side by side for Tony's look:

1. dots on a REGULAR pattern that thins by a formula;
2. dots SCATTERED AT RANDOM, as the Sun's streamer belt is.

What the render draws, and what it may not:
- Each belt fills the space between the two dipole field lines through
  its served edges (inner belt 1.1 to 2.0 Earth radii, outer 3.0 to
  7.0, read from `constants_new.py`'s edge rows, never typed), using
  r = L cos^2(latitude). READ A SOURCE FOR THE RELATION before drawing
  it (a named textbook or paper, with its page or equation), per
  provenance-discipline; the relation is a formula, so its source goes
  where the drawing code and the hover can cite it.
- Cut at the crust (r >= 1 Earth radius): a declared drawing choice.
- About the spin axis, in the equatorial plane's frame, as L-231 ruled:
  a declared drawing choice the hover states (magnetic geometry drawn
  around the spin axis, the daily average).
- The dots are thickest at the served peak, in the equator, thinning
  across the belt and up each field line. The fade's shape is not
  measured: a declared drawing choice, said in the hover as the
  streamer belt's is ("drawn to show the shape, not measured"). No
  separate peak line is ruled; the render may show one faintly only if
  Tony asks.
- Point budget: what Earth's room carries on a phone. Count the dots and
  say the count.
- The render is a scratch script and an HTML file sent to Tony. It is
  not committed and touches no repository file.

Tony's look rules: regular or random; whether the inner belt reads near
the ground (where its inner field line lands at about 17 degrees) or
falls back to C (inner belt flat, outer curved); anything about the
fade he sees. If RANDOM: L-434's ruling applies (the orrery places the
dots and the website draws them as given, like the Hills cloud through
`export_drawings.py`), which adds the export to patch 2 and the reader
to patch 3. If REGULAR: each instrument draws it from the rows, the
rule written in both and held to the same answers by a check, as
`_even_belt_rings` and `evenBeltRings` are today.

## 3. The patches, in order

### Patch 1, gallery: the run records (L-449)

Ruled: keep every record until the cause of the loss is found; then a
deliberate limit, its number set then, with each removal named. The
check goes in now.

- `tools/gallery_cache_builder.py`, at the copy step (`run_build`, the
  `shutil.copytree(live_raw, staging / 'raw')` at line 2197 at
  2090a8b): print how many records `live_raw / 'runs'` held, and how
  many `staging / 'raw' / 'runs'` held after the copy, with both paths.
  The builder deletes no record.
- `daily_run.py`: between step 3 (the builder) and step 4 (the
  maintenance run), compare the new `data/solar-system/raw/runs/` with
  the replaced cache's, `data/solar-system.prev/raw/runs/`. A record in
  the old and not the new STOPS the Daily Run before the maintenance run
  and before anything reaches the change list, naming each lost record
  and where its copy is. On success it prints what it compared: the two
  counts and the folders ("carried 85 of 85, plus tonight's").
- A check that can fail: plant a loss in the builder's offline suite
  (`tools/test_gallery_cache_builder_offline.py`) or the Daily Run's,
  and show the stop fires and names the record.
- The cause: record what the two new prints show on the next loss, in
  L-449. Do not chase past the records.
- If the comparison is a new Daily Run step, it needs its dashboard
  button in the same push (the orrery's Dashboard parity row).
- Run: the gallery's offline maintenance run green; Tony's next Daily
  Run is the live test.

### Patch 2, orrery: the belts, the hovers, the citations, the skills

After Tony's look. In `earth_visualization_shells.py`,
`constants_new.py`, `export_drawings.py` (if random), the skills, and
the protocol.

- The belts as Tony's look ruled, replacing the flat rings
  (orrery-coding-conventions: hover AU and km, single info marker,
  legend groups). The hover, rewritten for the curved shape: what is
  measured (the edges, the peak, their sources), what is drawn by
  choice (the curve about the spin axis, the cut at the crust, the
  fade), in plain words (L-331). The words go to Tony first.
- The aberration (L-314): the magnetopause and bow shock hovers each
  gain one sentence, drawn unturned along the Sun-Earth line, the real
  nose turned a few degrees toward Earth's motion depending on the
  solar wind's speed; sourced to the Shue and Jelinek rows; no typed
  number. The words go to Tony first.
- Citations (L-452 and L-450, Tony's rule): every piece of wording in
  the website's 35 `source_note`s that bears on its citation moves
  into the row in `constants_new.py`: into `# Source:` when it is part
  of the citation (a locator, an edition, an arXiv number or a URL the
  website had), otherwise into the row's other comment lines. L-450's
  rows at the same time: store notes out of `# Source:` ("Converted to
  km^3 s^-2 here.", "IAU B3 rounds to 6378.1 km", the HELMET_CUSP
  "4.0 is the TOP..." text) into other comment lines; the IADC edition
  (Revision 2 or 3) checked against the document actually read; the
  660-km row's Source naming its work (Ishii et al. 2019 is on its Ref
  line). Every edit by provenance-discipline; the list to Tony first.
- Skills, ONE bump each, in this patch's commit with the protocol
  (the four steps, ledger-and-session-records):
  - interactive-exhibit 1.17: `source_note` holds only a drawing
    choice beside a citation; wording that bears on a citation lives in
    the store (Tony, 2026-10-16). And the belts as a density field,
    with which kind (formula or stored drawing) Tony's look chose.
  - gallery-cache-builder 1.11: the run records are kept until L-449's
    cause is found, then a limit with each removal named; the Daily
    Run's records check, where it sits and what it prints.
  - protocol v3.102 naming both; the oldest resident entry moves down.
- Run: the orrery maintenance run green, the gate path Tier-1 = 0, the
  export (schema 7) carrying the new citations; Tony's look at the
  Earth plot in the orrery (Mode 5): the belts and the two hovers.

### Patch 3, gallery: the website side

- The belts in `gallery/feature_renderers.js` (`renderBelts`) to match
  the orrery: a formula drawn on the page, or the orrery's stored
  drawing read as given. Shell stamps (`meta.shell_key`) on every new
  trace (interactive-exhibit, A shell trace carries its key);
  `documentation/smoke_arrival.js` and the payload that feeds it
  re-recorded if the trace set changes.
- The belts' served words (`hovers_rings`, `hovers_plane`,
  `hovers_band` and whatever replaces them) rewritten for the curved
  shape through `tools/store_writer.py`, in Tony's approved words.
- The eight sentences (L-451), as ruled: 1 to 5 SERVED with their
  rows' sources (any new word field added to `store_writer.py`'s
  `WORD_FIELDS` or `SERVED_WORDS_PATCHED` first, the check's one
  home); 6 ALLOWED; 7 reworded in `interactive.html` to "Where that is
  so, the text beside it says so." and ALLOWED; 8 CUT from Earth's
  description (the belts' served `hovers_plane` already says it). The
  Typed facts check's OPEN list is then empty, and the check says so.
- The notes (L-452): the mirror (`tools/mirror_constants.py`) writes
  the new citations from patch 2's export; each `source_note` that is
  not a drawing choice is removed through the store writer; the Crust's
  served `note` keeps its drawing-choice words without "(Tony,
  2026-09-28)".
- The aberration sentence served on the magnetopause and bow shock, in
  the words Tony approved for the orrery.
- `documentation/smoke_hover_budget.js`: every hover under its CEILING
  (17 lines). The aberration sentence adds a line to two hovers that
  were fitted to that ceiling on 2026-10-06; fit them, do not raise it.
- Run: the gallery's offline maintenance run green; served words need
  the cache rebuilt, so they reach a visitor after the next Daily Run;
  `gallery_maintenance_run.py --live` after the push. Tony's look on
  the phone (Mode 5): the Earth room's belts (arrival, rotate, tap a
  belt, its text box and i panel), the magnetopause and bow shock
  hovers, the i panels' Source lines with no repeated notes.

## 4. Words to Tony before anything ships

One list, sent before patches 2 and 3 are built, plain and short:
- the belts' new hover, orrery and website;
- the aberration sentence;
- sentences 1 to 5 as served (their text is today's; only where it
  lives changes) and 7's new wording;
- for each of the 35 notes: dropped, moved into which row's citation
  or comment, or kept as a drawing choice, with the words;
- the `# Source:` lines edited in `constants_new.py` (L-450 and the
  moved wording).

## 5. The close

- L-330 closes on Tony's look in both instruments. L-451 closes when
  the Typed facts OPEN list is empty on his run. L-452 and L-450 close
  on his approval of the words and a green run. L-449 stays open for
  its cause; its check part is recorded done. L-314 keeps the whole
  solar-wind item; the aberration sentence is recorded on it.
- Re-home loose ends (A Closing Item Re-homes Its Loose Ends): C (the
  inner belt flat) if not used; the deliberate limit on run records,
  owed when L-449's cause is found.
- Where We Are by section; the design talks go on in L-413's order:
  next, L-356 with L-375 (IGRF-14 and the dipole's offset, which also
  carries the South Atlantic Anomaly the curved belts cannot show
  centred).
- The skill obligations travel: the next session confirms its loaded
  interactive-exhibit reads 1.17 and gallery-cache-builder 1.11.

## 6. Tony's actions, all of them

- (do) Run `patch_earth_round1_close_20261016.py` in the orrery, the
  orrery maintenance run, commit, push (the design talk's close).
- (decide) At the build's start: on a run-record loss, stop and name,
  or put back from `.prev` and say so (section 1).
- (decide) At the render: regular or random dots; the inner belt
  curved or flat.
- (decide) The words list (section 4), before patches 2 and 3 ship.
- (do) Each patch, its run, commit, push, one repository at a time.
- (do) Reinstall interactive-exhibit 1.17 and gallery-cache-builder
  1.11 after patch 2's push.
- (do) Mode 5: the orrery's Earth plot after patch 2; the Earth room on
  the phone after patch 3 and the next Daily Run.

Brief written October 16, 2026 with Anthropic's Claude Opus 5.5.
