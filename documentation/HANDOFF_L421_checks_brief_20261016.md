<!-- Doc-Kind: hand | Brief for the L-421 checks build, parts 2 and 3 of its Gap: the typed-facts survey becomes a gating check in the gallery run, and each served number's citation in data/objects_config.json is checked against its row in constants_new.py. L-262 (the framing test) closes alongside. Orrery export first, then the gallery. -->
# Brief: the L-421 checks, parts 2 and 3 (the typed facts, and the citations), with L-262 riding

Built on orrery 641e4691 (short 641e469, "Update
WHERE_WE_ARE_10-15-26_2236_run_record.md"; the code and the ledger are
b022097's, "L445 close") at
https://github.com/tonylquintanilla/palomas_orrery, and gallery
09d92918 (short 09d9291, "exports") at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 16, 2026 with Anthropic's Claude Fable 5.1, in the
coordination session of October 15-16.

- Type: BUILD brief. One session, three patches in order: the
  orrery's (the export carries each row's source), pushed; the
  gallery's (the mirror writes it, two new checks), pushed; the
  orrery's close (the dashboard button, the ledger, Where We Are).
  Tony's word on the one decision in section 4.
- Ledger: L-421 (the typed facts), open since 2026-10-06. Read its
  block first; its Gap names the two parts this build closes. L-262
  (the framing test) rides: item 1 of L-423 (the website's checks),
  which closes on a passing Page framing row that your runs of Oct 15
  and 16 already show.
- Order: stage 6 on the road, first on Earth's list (L-413) now that
  L-445 is closed. After it, Earth's design talks, then the Sun's list
  (L-412).
- ONE SESSION AT A TIME on each repository (the lesson of 2026-10-15:
  two build sessions moved each other's base). Pull HEAD at the start;
  if either repository has moved past the SHAs above, read the ledger
  again before writing anchors.

## 0. Before building

- Skills this task fires, confirmed against the manifest at HEAD:
  interactive-exhibit (1.15; the served-data provenance contract; who
  may write data/objects_config.json), provenance-discipline (2.29;
  citation inheritance for a derived row; the gate at export),
  gallery-cache-builder (1.10; objects_config.json), safe-file-editing
  (1.13), agentic-pre-test (1.3; the orrery's and the gallery's
  maintenance runs on throwaway copies), ledger-and-session-records
  (1.21; the close).
- THE OBLIGATION THAT TRAVELS: this session confirms its loaded copy of
  gallery-cache-builder reads 1.10 before touching objects_config.json
  (bumped 2026-10-16, protocol v3.100; Tony reinstalled it). The
  horizons-orbital-mechanics 1.8 obligation keeps travelling: nothing
  here fires that skill. If a loaded copy disagrees with the manifest,
  STOP (Stale Skill = Stop).

## 1. What was ruled, and what is not yet decided

- Tony's ruling, 2026-10-06 (on L-421): code types only sentences
  about the picture; a fact about nature, about a paper, or a source is
  served with its feature's words. The rule is in interactive-exhibit
  since 1.12. The survey that found the 17 typed facts was run by hand
  and is in neither repository; the manifest's step 7 said it becomes
  a gating check, shown failing first. That is part 2.
- L-421's own question, recorded 2026-10-06 and never checked: whether
  the citation beside each served number in `data/objects_config.json`
  agrees with the `# Source:` line of its row in `constants_new.py`.
  The checks compare the numbers and have never compared the words.
  That is part 3.
- Not yet ruled: what "agree" means for a citation, and which side
  owns the words. Section 4.

## 2. What is there

Part 2, the survey:
- The method (MANIFEST_L421_typed_facts_20261006.md, "How the list was
  found"): build both rooms twice, once as served and once with every
  served word replaced by a marker; any sentence still present without
  the marker was typed. The first run missed the `_model` key and
  reported two served formulas as typed, so the marker pass must cover
  every served word field, not a guessed list.
- The gallery run already builds every hover without a browser:
  `documentation/smoke_hover_budget.js` (the "Hover budget" row, node)
  evaluates `gallery/feature_renderers.js` and `gallery/earth_geometry.js`,
  builds the Earth room from the recorded fixtures
  (`documentation/payload_earth_scene.json`, `payload_earth.json`) and
  the Sun room straight from `data/objects_config.json`, with the frame
  constants from `data/solar-system/coverage_index.json` and the
  drawings from `data/solar-system/drawings/`. The survey check builds
  the rooms the same way. The jsdom harness in `tools/headless/` is
  Claude-only and needs a package the gallery does not carry; it is not
  the tool for a gating row.
- The served word fields have one home: `tools/store_writer.py`'s
  `WORD_FIELDS` ("name", "description", "about", "note", "source",
  "info_url", "hover"), plus the parallel word lists a belt serves
  (`hovers_plane` and its kin, as `flux_peak_of` does) and Earth's
  `orientation.words`. The survey reads that list from the writer, or
  the writer and the survey share one, rather than typing a second.
- What a visitor reads that the renderers do not build: each room's
  own description in `interactive.html`, which the skill allows as page
  text with its source in the page. The manifest left it for this
  check to read sentence by sentence.
- Typed sentences that are allowed: the streamer belt's caveat (S4, a
  drawing choice, ruled 2026-10-06), every hover's pointer line to the
  i panel, and sentences about the picture ("drawn at...", "the ring is
  drawn to scale"). The check keeps that list SHORT and NAMED, in the
  suite, so a new typed fact cannot hide in it.
- Expected result today: none. The website half's record of
  2026-10-11 ran the method by hand on the Sun room and found none
  after the build; the Earth room's thirteen were served on
  2026-10-06. The check's value is that it stays run.

Part 3, the citations (measured in this coordination session at
gallery 09d9291 and orrery 641e469, by a plain comparison of strings;
Claude's measurement, not a source, and the build re-measures):
- 119 links in `data/objects_config.json` carry `orrery_constant`. 83
  of them carry a `source` field beside the number; 36 carry none; 3
  point outside the store (the Sun's, Jupiter's and Saturn's
  `planet_poles`, already named ABSENT by the mirror).
- Of the 83, 8 match the orrery row's `# Source:` line word for word.
  72 differ, nearly all in the WORDING of the same work: the config
  writes "Suess and Nerney (2004) -- extent of the closed-field helmet,
  not of the streamer belt" where the row writes "Suess & Nerney (2004),
  Adv. Space Res. 33:668-675, bibcode ...". The config's text often
  carries a gloss after " -- " that says what the number is for; the
  row's carries the journal reference. A few orrery rows have no
  `# Source:` of their own because they are derived (SOLAR_RADIUS_AU
  from SUN_RADIUS_KM): their citation is their input rows', by
  provenance-discipline's inheritance rule, which
  `test_citation_inheritance.py` pins.
- The constants export (`export_constants.py`, schema 6) does not
  carry a row's source at all: each exported row has value, unit,
  figures, status, derived, read, inputs, uncertainty, prints and "in".
  So the gallery has no way to compare citations today; the config's
  `source` fields were typed by hand, once, and nothing watches them.
- The mirror (`tools/mirror_constants.py`) writes value, unit, figures,
  uncertainty, prints and "in" into each linked slot and, by its own
  docstring, "nothing else on the entry is touched -- not the source".
  The "Config mirror check" row (`tools/check_constants_links.py
  --mirror`) compares the same fields and no words.
- 36 config numbers with no source beside them is itself a finding the
  check names on its first run.

## 3. What to build

ORRERY FIRST (one patch, pushed before the gallery's):
- `export_constants.py` carries each row's citation: a `source` field
  (the `# Source:` text, with its `# Source+:` continuations joined),
  and for a derived row with none of its own, the sources of its
  inputs, resolved by the same rule `test_citation_inheritance.py`
  pins, with a field saying it was inherited. Schema moves to 7, with
  the docstring's schema line and `test_constants_export.py` following
  (the Constants export check: "Export matches the store").
- The gallery's three pulls require a schema; `pull_constants_export.py`
  wants `SCHEMA_WANTED` and the mirror `MIN_SCHEMA`. Raise both in the
  gallery patch; until the gallery patch runs, the gallery reads the
  new export and ignores the field, which is harmless.
- Nothing printed by the orrery changes. Tier-1 on the gate path stays
  0; the export is on the gate path, so the scanner reads the new
  field as what it is, a citation, not a claim.

THEN THE GALLERY (one patch):
- Part 3, the mirror: under section 4's option A, `mirror_constants.py`
  writes the orrery's citation into each linked slot's `source`, the
  way it writes the value, and the website's gloss, where one exists
  after " -- ", moves to a new field the website owns (`source_note`)
  in the same patch, so no words a visitor reads are lost. Under
  option B the mirror writes nothing and the check compares a key.
  Either way, `tools/check_constants_links.py --mirror` (the Config
  mirror check) gains the citation comparison, names every link whose
  citation disagrees or is missing, and fails on them; the Mirror suite
  (`tools/test_mirror_constants.py`) gains the cases.
- Who may write objects_config.json: the mirror for numbers,
  store_writer for words (interactive-exhibit). A citation written by
  the mirror is the orrery's; the gloss stays a word field
  store_writer and the exhibit store editor know. Add `source_note` to
  `WORD_FIELDS` and to the editor's boxes, or say why not, as the
  manifest's step 3 asked.
- The panel: `feature_renderers.js` prints the source in the i panel.
  Where the gloss moves to `source_note`, the panel prints both, the
  citation then the gloss, so the visitor's text reads as before. The
  Hover budget and Display figures rows must still pass; a hover does
  not carry citations (Tony's split of 2026-09-15).
- Part 2, the survey: a new node suite,
  `documentation/smoke_typed_facts.js`, and a gating row "Typed facts"
  in `gallery_maintenance_run.py`. It builds both rooms the way
  smoke_hover_budget.js does, collects every string the renderers
  produce (hover, panel about, note, source, footer, the drawer rows'
  words), builds them again with every served word field replaced by a
  marker, and reports every sentence that survived unchanged and is
  not on the named allowed list. It also reads each room's description
  in `interactive.html` and reports a sentence there that states a
  fact about nature with no source in the page. Output: count AND
  names, by room and feature (A Report Names Its Items).
- The orrery's dashboard (`palomas_orrery_dashboard.py`) gains the
  "Typed facts" button and its short line, in the gallery checks group,
  or Dashboard parity goes red (83 steps matched at b022097). The
  parity checker reads the gallery's run list at run time, so a button
  before its script is NOT FOUND and a script before its button is NO
  BUTTON: whichever lands first, one orrery run between the two
  patches would be red. So the button rides the orrery's CLOSE patch,
  which comes after the gallery's anyway: three patches, every run
  green. Order: orrery (the export), gallery (the mirror and the two
  checks), orrery (the button, the ledger, Where We Are, the record).
- L-262 (the framing test) rides in the ledger patch: both of its
  one-line fixes landed at ab66aba7; the Page framing row passed on
  2026-10-15 and 2026-10-16 (Tony's run records); close it, and move
  its residual (the live room's framing has no test) onto L-367 by
  handle, as L-423's item 1 says. L-423's item 1 is then done and its
  next open item is 3 (L-357, stale leftovers).

Cluster the Tail by Files Touched: before writing the patches, sweep
the open ledger for items whose files are `export_constants.py`,
`mirror_constants.py`, `check_constants_links.py`, `store_writer.py`,
`feature_renderers.js`, `gallery_maintenance_run.py`, the dashboard's
gallery group. L-322 (the IGRF epoch, a class) and L-430 (the orrery's
other uncited Oort lines) are near; carry one only if it is small, and
name any found.

## 4. The one decision, for Tony at the session's start

Which side owns the citation beside a served number?

- A (recommended; default if Tony is away): the orrery does. The
  export carries each row's `# Source:`, the mirror writes it into the
  config beside the number, and the check compares the two byte for
  byte, as it already does the value, the unit and the figure count.
  The website's own gloss on a number ("extent of the closed-field
  helmet, not of the streamer belt") keeps its place in a field the
  website owns, printed after the citation. Consequence: 72 config
  citations change wording on the first run, to the orrery's; nothing
  a visitor reads is lost, and the citation can no longer drift. This
  is the rule Tony gave on 2026-09-17 (L-322) for numbers: a tool that
  reads the orrery's export and writes into the config is transmitting,
  not keeping a second store.
- B: the website keeps its own wording, and the check compares only
  that both name the same work (first author and year, read from each
  string). Consequence: two hand-kept copies of every citation, and a
  check that cannot tell a changed page number from a changed paper.

Tony's word goes on L-421 and, as method, into interactive-exhibit's
served-data provenance contract (a bump, 1.16, with the protocol
entry, under One Session, One Bump) if A: a citation is served like a
number.

## 5. Planted faults, each shown caught, by name

- A typed fact about nature planted in `feature_renderers.js` (one
  sentence in a hover): the Typed facts row names the room, the
  feature and the sentence, and fails.
- The same sentence added to the allowed list: it passes, and the row
  prints the allowed list in full, so an addition is visible.
- A served word field removed from the writer's list: the row must
  report the field it could not cover, not pass by silence (A Check
  That Cannot Fail Is Not Passing).
- A fact typed into a room's description in `interactive.html` with no
  source in the page: named.
- A config citation edited by hand to a different work: the Config
  mirror check names the link and fails; under A, the next mirror run
  restores the orrery's and says so.
- A link with no `source` at all: named on the first real run (36 of
  them today) and fixed by the mirror under A, or named as missing
  under B.
- A derived row whose inherited citation is wrong in the export:
  `test_constants_export.py` catches it against the inheritance rule.
- The export at schema 6 read by the new mirror: refused by name.
- The orrery's Dashboard parity with the new gallery row and no button.

The orrery's maintenance run on a throwaway copy before delivery (31 of
31 at b022097, gate path 0); the gallery's offline run on a throwaway
copy (28 of 28 at 09d9291), plus the new Typed facts row. The gallery's
run needs the new export: ship the patch with a copy of the export and
its `.sha`, as L-345's did, so the offline run passes before Tony's
pull.

## 6. The look

- Tony's look on the phone: one Sun feature's i panel and one Earth
  feature's, where the citation now prints the orrery's words with the
  gloss after it (under A). The hover is unchanged.
- The Typed facts row's first real output, in his run record: the
  count and the names, expected none outside the allowed list.

## 7. Close

- L-421 to DONE after Tony's runs and look: parts 2 and 3 built, the
  survey a gating check, every served number's citation checked. A
  Closing Item Re-homes Its Loose Ends: read the whole block; L-430
  and L-434 already hold the Oort lines and the other dot clouds; name
  anything else by handle.
- L-262 to DONE, its residual on L-367. L-423's item 1 marked done.
- Where We Are: stage 6 done; stage 5 (Earth's list) moves to the
  design talks, the belts' shape first (L-330); stage 9 notes items 1
  and 2 done, next item 3; the box; the signals re-read; the marks
  reset; the run-record zone read first and emptied after.
- interactive-exhibit 1.16 if A (the contract: a citation is served
  like a number, and the gloss is the website's), with the protocol
  entry (v3.101) and the manifest; the reinstall is Tony's and the
  obligation travels.
- The build record,
  `documentation/HANDOFF_L421_checks_build_<date>.md`, in the ORRERY's
  documentation/; the spent gallery patch in the gallery's
  documentation/, the orrery patch in the orrery's.

## 8. Tony's actions, all of them

- (do) Start the build session from this brief; it confirms
  gallery-cache-builder 1.10 loaded.
- (decide) Section 4, A or B; default A.
- (do) Run the orrery patch; run `orrery_maintenance_run.py`; commit;
  push.
- (do) Run the gallery patch; run `gallery_maintenance_run.py` (the
  pulls bring the new export; the Config mirror check names what moved;
  the Typed facts row prints its names); commit; push; the live run.
- (do) Look at two i panels on the phone.
- (do) Run the orrery close patch; run `orrery_maintenance_run.py`
  (Dashboard parity with the new button; the ledger index); commit;
  push.
- (do) If interactive-exhibit was bumped: reinstall 1.16 in Settings >
  Skills; save PROJECT_INSTRUCTIONS.md as its versioned copy and copy
  it into the Project instructions.

Brief written October 2026 with Anthropic's Claude Fable 5.1.
