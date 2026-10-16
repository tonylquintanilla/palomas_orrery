<!-- Doc-Kind: hand | Brief for the L-445 build: Earth's orbital period is asked of the Earth-Moon barycentre (Horizons target 3), not Earth's centre (399); the check asks the same target; the hover and the website say so. L-448 (the test file in the tracked tree) rides along. Orrery, with one small gallery patch for the website's words. -->
# Brief: Earth's period from the Earth-Moon barycentre (L-445), with L-448 riding

Built on orrery b4105c0c7224f5b58984c3ead8b26b1c8653909a at
https://github.com/tonylquintanilla/palomas_orrery ("Update
WHERE_WE_ARE_10-14-26_2250_run_record.md"; the code is 802e5bd's). The
gallery read at 95713f4912d3e1863390a246d2ba8004bc7cf4c9 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io ("daily
run again"); one small gallery patch for the website's sentence.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 15, 2026 with Anthropic's Claude Fable 5.1, in the
coordination session of that evening.

- Type: BUILD brief. One session. Tony's word on the hover's words at
  his look; everything else is ruled or is the builder's method.
- Ledger: L-445 (Earth's period), opened 2026-10-15 with Tony's ruling,
  "Confirmed as recommended, the barycenter." Read its block first.
  L-448 (the test file in the tracked tree) rides this session, Tony's
  ruling of 2026-10-15 in the coordination session.
- Order: road stage 8b, first on Earth's list (L-413). L-446 (the
  Daily Run's order) is a separate gallery build with its own brief;
  the two do not depend on each other and may run in either order.

## 0. Before building

- Pull the orrery at HEAD and pin it. If HEAD has moved past b4105c0,
  read the ledger's L-445 and L-448 blocks again before building.
- Skills this task fires, confirmed against the manifest at HEAD:
  horizons-orbital-mechanics (1.7; A Period Depends on Its Centre;
  Where the Check Lives, and What It Compares), safe-file-editing (the
  patches), agentic-pre-test (new code; the maintenance run on a
  throwaway copy), ledger-and-session-records (1.21; the close),
  interactive-exhibit (1.15; a body's period is the orrery's, printed
  as served, and reaches a visitor on the push).
- THE OBLIGATION THAT TRAVELS: this session confirms its loaded copy of
  horizons-orbital-mechanics reads 1.7 before any Horizons work. The
  session that bumped it (L-444, 2026-10-15) loaded 1.6; the L-401
  session the same evening also loaded 1.6. Nobody has yet read 1.7
  from inside a session. If the loaded copy reads 1.6, STOP and ask
  Tony to reinstall it (Stale Skill = Stop).

## 1. The ruling (Tony, 2026-10-15; recorded on L-445, not re-asked)

- Earth's orbital period is JPL's period for the Earth-Moon
  barycentre (Horizons target 3), around the Sun. Not Earth's centre
  (target 399).
- Earth's identity and position stay Earth's centre (399). Only the
  period's target changes.
- The hover says so, in the orrery and on the website.

Why (Claude's reading, on L-445, to be confirmed against JPL's PR for
target 3, never asserted): Earth's centre circles the Earth-Moon
barycentre once a month, so its speed, and the period worked out from
its position and speed, swing by about half a day either way through
the month. The barycentre makes no such loop.

## 2. What is there at b4105c0

- `celestial_objects.py`: Earth is `{'name': 'Earth', 'key': 'earth',
  'id': '399', 'id_type': None, ...}`. The Earth-Moon Barycenter is its
  own entry, `'id': '3'`, no key (not served).
- `orbital_period.build_period_record(horizons_id, id_type, date_str,
  location, previous, elements_p_days)` asks `query_period_pair` for
  the body it is given, around the chosen centre (the two-centre test:
  the Sun or the solar system's barycentre, whichever moves less in a
  year). It is called from ONE place,
  `osculating_cache_manager.fetch_osculating_elements`, with
  `query_id` (Earth: '399'); plotting and `period_fetch.py` both go
  through that call, so one change reaches both.
- Earth's record today (first live fetch, 2026-10-15, at 9579fcd):
  365.5364560333389 days around `@sun`; the two-centre test measured
  0.769 days of change in a year around the Sun and 1.76 around the
  barycentre, so the Sun was chosen and it prints to three figures,
  "366 days". `data/objects_export.json` and `data/osculating_cache.json`
  carry it; the website prints it.
- `build_period_record` also compares the elements fetch's own PR
  (`elements_p_days`, Earth 399's) with the period query, and records
  `agrees_with_elements_fetch`. With the period asked of target 3 and
  the elements of 399, those two are different bodies' periods and
  will not agree; that comparison must be skipped and the record must
  say why, not record DISAGREE.
- `orbital_period.drawing_orbit` pairs the drawn ellipse with the
  period by CENTRE, not by target: when the plot's fetched elements and
  the record share a centre (`@sun` for Earth), the orbit is drawn from
  the plot's own elements, Earth's. So the drawn orbit stays Earth's and
  the printed period becomes the barycentre's. Confirm this against the
  Orbit markers row (`test_orbit_markers.py`: "4 ellipses, 1080 drawn
  points on their period's centre; 14 markers, 9 dates") and say it in
  the hover if the words need it.
- `horizons_check.check_period` builds its query from
  `obj.get("horizons_id")` and the record's centre and date
  (`period_url`). For Earth that asks 399, so after the build it would
  compare the barycentre's period with Earth's centre's and report a
  false disagreement. It must ask the record's target.
- `period_fetch.py` fetches only a served body with NO fetched period.
  Earth has one. The build needs a way for the run to re-fetch Earth
  without Tony plotting it: see section 3.
- `export_objects.period_block` writes the period the website prints:
  `center`, `center_label` (from `orbital_period.centre_label`), years
  and days with their figure counts, `fetched`, `words`, and the
  `record`. The gallery's `tools/mirror_objects.period_copy` copies
  everything but `record` into `data/objects_config.json`, so a new
  field in the block reaches the website's config on the gallery's
  pull with no mirror change.
- The website's sentence, `gallery/solar_system_figures.js periodLine`:
  "Orbital period: N years (M days), around <center_label>, from JPL
  Horizons, fetched <date>." It reads `center`, `center_label`,
  `fetched`, `years`, `days`, `kind`, `open_orbit`, `words`. The gallery
  maintenance run's "Solar System figures" row ("5 period cases and 10
  served periods printed as the orrery printed them") pins that
  sentence.
- The orrery's hover, `orbital_period.period_hover_lines`: "Orbital
  period: N years (M days)<br>Around <label>, from JPL Horizons,
  fetched <date>.<br><why the digits>."
- L-448: `test_orbit_cache.py` writes `test_output/test_orbit_paths.json`
  (a valid and a deliberately corrupted entry, dated 2025) on every
  maintenance run, as the "Orbit cache" row. The file is tracked (since
  at least 87a5470); 8e50aea committed it as deleted mid-run and 464d872
  put it back byte for byte. `.gitignore` does not name `test_output/`.

## 3. What to build

ONE HOME for the target. The map from a body's Horizons id to the id
its period is asked of lives in `orbital_period.py`, beside
`VIEW_TO_OSCULATING_CENTRE` and `CENTRE_LABELS`: today one entry, 399
to 3. Every other reader takes the target from the RECORD, never from
a second map:

- `build_period_record` asks `query_period_pair` for the target, and
  writes `target` (the id asked) and `target_label` (its words, from
  `CENTRE_LABELS`: '3' is already "the Earth-Moon center of mass")
  into the record. For every other body the target is the body itself.
  The `agrees_with_elements_fetch` comparison runs only when the target
  IS the fetched body; otherwise the record carries a plain reason.
- `period_fetch.py` treats a served body whose record's `target` is
  not the target the map now names as MISSING, and fetches it with
  plotting's own call, as it does a body with no period. Its row then
  prints the body by name with the reason ("period asked of 399, now
  3"). That is how Earth is re-fetched on Tony's first run, and how a
  later target change reaches the website without anyone plotting.
- `horizons_check.check_period` asks the record's target (falling back
  to the body's id only for a record with no `target`, which after
  this build is none of the served bodies); the confirmation it writes
  to `data/horizons_confirmations.json` names the target and the query.
- `export_objects.period_block` adds `target` and `target_label` to
  the exported block. `test_objects_export.py` gains the check that a
  fetched period's block names its target.
- The orrery's hover (`period_hover_lines`) and the parameters-window
  text (`period_panel_text`) say whose period it is when the target is
  not the body. Proposed, for Tony's look: "For the Earth-Moon center
  of mass, around the Sun, from JPL Horizons, fetched <date>." The
  "why the digits" line is unchanged.
- The gallery: `periodLine` prints the same words when `target_label`
  is served and differs from the body ("For the Earth-Moon center of
  mass, around the Sun, ..."); a served period with no `target_label`
  prints as today. The "Solar System figures" row's pinned sentence
  gains Earth's case. One small gallery patch; it ships with the
  orrery's export so the gallery's offline run passes before the push.
- L-448: `test_orbit_cache.py` writes its fixture into a temporary
  folder (`tempfile.mkdtemp`, removed when the tests finish) instead of
  `test_output/`; `.gitignore` gains `test_output/`; the orrery patch
  deletes `test_output/test_orbit_paths.json` and the folder, so the
  deletion is what Tony commits and nothing recreates the file at that
  path. Check the maintenance run's FILES WRITTEN report and
  DATA_INVENTORY.md no longer name it.
- Digits: nothing new. The record's error is the year change (and SBDB
  sigma for a small body) as before; the barycentre's smaller year
  change earns more figures by the existing rule. Do not type an
  expected value anywhere; the live run and the check give it.

Where the target map is a judgment call (which other bodies get a
target other than themselves), it is not: today it is Earth only. The
Pluto-Charon barycentre's own period is L-443's loose end and stays
there.

## 4. Planted faults, each shown caught, by name

- Earth's period asked of 399 again (a record whose `target` is not
  the map's): `period_fetch.py` must name Earth as missing for that
  reason, and `test_period_fetch.py` shows it.
- The check asking the body's id while the record names another
  target: `test_horizons_check.py` plants a record with target 3 and a
  fake JPL answer for 399, and the check must ask 3.
- An export block for a fetched period with no `target`: the Objects
  export check fails by name.
- A hover for a body whose target is not itself that omits the target's
  words: `test_position_digits.py` (23 hovers examined) or the suite the
  builder finds nearer.
- `agrees_with_elements_fetch` recorded for a target that is not the
  fetched body: the record must carry the reason instead.
- L-448: the Orbit cache row passing with no file written under the
  repository root (the test's temporary folder is gone after the run).

Tests run offline on recorded JPL answers, as the Horizons check's and
the period fetch's suites do
(`documentation/worksheets/horizons_answers_L395.json`,
`documentation/worksheets/period_fetch_answers_L444.json`). Record the
answer for target 3 the same way. The first live run, on Tony's
machine, is the real test: the Period fetch row names Earth, the
Horizons check compares the new record with JPL the same run, and the
Horizons confirmations row still passes.

## 5. The look

- The orrery: Earth's hover from a Sun-centred plot, and the
  parameters window. Tony approves or changes the words.
- The website: Earth's hover in the Solar System room and the Earth
  room, after the gallery's pull. Until L-446 (the Daily Run's order)
  is built, the words reach the website on the FIRST Daily Run after
  the orrery's push (the pull is in the maintenance run, after the
  build, but the period's words are config, not cache); after L-446,
  the same. The orbit drawn around a period's centre is cache data and
  needs the builder; Earth's centre does not change here, so no cache
  change is expected. Say which in the build record.

## 6. Close

- L-445 to DONE after Tony's run and look, his verdicts quoted from
  his run record; L-448 to DONE with the commit that deletes the file.
- A Closing Item Re-homes Its Loose Ends: L-445 received "the look at
  the website" from L-444; it is discharged by section 5 or re-homed by
  handle.
- Where We Are: stage 8b done; stage 5 (Earth's list) moves to the
  rest of L-421's checks; the box, the signals re-read, the marks
  reset; the run-record zone read first and emptied after.
- horizons-orbital-mechanics: one sentence under A Period Depends on
  Its Centre, that a body's period may be asked of another target than
  the body (Earth: the Earth-Moon barycentre, target 3; the record
  carries `target`, and every reader takes it from the record). A
  session following the skill without it would ask 399. That is a bump
  (1.8) with the protocol entry, under One Session, One Bump; the
  reinstall is Tony's, and the obligation travels to the next session.
- The build record: `documentation/HANDOFF_L445_earth_period_build_20261015.md`
  (or the date built), in the orrery's documentation/; the spent gallery
  patch in the gallery's documentation/.

## 7. Tony's actions, all of them

- (do) Start the build session from this brief; it confirms
  horizons-orbital-mechanics 1.7 loaded before Horizons work.
- (do) Run the orrery patch; run `orrery_maintenance_run.py` (the
  Period fetch row names Earth; the Horizons check compares it); look
  at Earth's hover in the orrery; commit (the commit deletes
  `test_output/test_orbit_paths.json`); push.
- (do) Run the gallery patch; run `gallery_maintenance_run.py`; commit;
  push; the next Daily Run; look at Earth's hover on the website.
- (decide) The hover's words, at the look.
- (do) Reinstall horizons-orbital-mechanics (1.8) in Settings > Skills;
  save PROJECT_INSTRUCTIONS.md as its versioned copy and copy it into
  the Project instructions.

Brief written October 2026 with Anthropic's Claude Fable 5.1.
