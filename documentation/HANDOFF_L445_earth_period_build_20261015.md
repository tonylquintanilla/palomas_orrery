<!-- Doc-Kind: hand | Build record for L-445: Earth's orbital period asked of the Earth-Moon barycentre (Horizons target 3), in the orrery and on the website; L-448 (the test file in the tracked tree) rode it. -->
# Build record: Earth's period from the Earth-Moon barycentre (L-445), with L-448

Built on orrery 77245ea87179455bb4794ba7ed8712b98350fdb7 at
https://github.com/tonylquintanilla/palomas_orrery ("L445 L446 rulings
and briefs"; no code changed since the brief's b4105c0) and gallery
95713f4912d3e1863390a246d2ba8004bc7cf4c9 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io ("daily
run again").
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 15, 2026 with Anthropic's Claude Opus 5.5.

- Type: BUILD. Companion to
  `documentation/HANDOFF_L445_earth_period_brief_20261015.md`.
- Ledger: L-445 and L-448, both still OPEN: they close on Tony's run
  and look.
- Skills loaded and confirmed against the manifest:
  horizons-orbital-mechanics 1.7 (the obligation of v3.98, discharged),
  safe-file-editing 1.13, agentic-pre-test 1.3,
  ledger-and-session-records 1.21. This build bumps
  horizons-orbital-mechanics to 1.8 (protocol v3.99); the next session
  confirms its loaded copy reads 1.8 before work that fires it.

## 1. What JPL says (checked, not asserted)

The brief asked for Claude's reading on L-445 to be confirmed against
JPL's PR for target 3 before relying on it. The session's shell cannot
reach JPL; the chat's web-fetch tool can, and read four elements rows
for target 3 at Earth's record minute (2026-10-15 10:52 TDB, JD
2461328.952777778) and a Julian year later. They are quoted verbatim in
`documentation/worksheets/period_answers_L445.json` under "rows", and
each is self-consistent: 360/N equals PR to sixteen figures.

| Target 3 around | PR at the date | PR a year later | Change |
|---|---|---|---|
| the Sun | 365.2513622323839 d | 365.2552267297335 d | 0.0038645 d |
| the solar system's barycentre | 361.05535813579 d | 363.5791397905601 d | 2.5238 d |

So the reading holds: the barycentre's period around the Sun sits near
the familiar year and barely moves, where Earth's centre's printed
365.5364560333389 d (366, three figures). The two-centre test keeps the
Sun. Rounded by its own year change, the period prints 1.00000 years
(365.25 days), five and six figures where it had three.

## 2. What was built

ORRERY (patch_L445_1_earth_period_20261015.py)

- `orbital_period.py`: `PERIOD_TARGETS = {'399': '3'}`, the one home of
  the map, beside `VIEW_TO_OSCULATING_CENTRE` and `CENTRE_LABELS`.
  `period_target()` applies it only around the Sun; `record_target()`
  reads a record's target (or, before L-445, the id its elements fetch
  asked); `target_words()` gives "for <whose>, " when the period is
  another body's. `build_period_record` asks the target, writes
  `target` and `target_label`, skips the comparison with the elements
  fetch's PR with a plain reason (`elements_fetch_not_compared`), and
  drops a previous record asked of another target, so the two-centre
  test runs for the new one. The hover and the parameters window say
  whose period it is. `drawing_orbit` never draws the record's
  elements, which are the target's, as the body's orbit.
- `export_objects.py`: a fetched period's block names `target` and
  `target_label`; a record naming no target and no horizons_id is
  refused; a period asked of another body is never paired with this
  body's elements; the run's summary line names whose period it is.
- `period_fetch.py`: a fetched period asked of another target than the
  map now names is missing, named "period asked of 399, now 3"; the
  read-back requires the new target; a period that comes back asked of
  the old target (the fetch keeps the last one when the new query
  fails) is JPL not reached, and nothing is saved.
- `horizons_check.py`: asks the period's target, with no id_type when
  that is another body; a change of target makes the period due at
  once; the confirmation records the target; the agree line names it.
- Tests, each with planted faults shown caught by name:
  `test_period_fetch.py` part 6 (eight faults, five in a copy of
  orbital_period.py), `test_horizons_check.py` (the check asking 399
  against a planted 399 answer that would agree), `test_objects_export.py`
  (a record naming no target, an exported block naming none),
  `test_position_digits.py` (the target's words dropped).
- `documentation/worksheets/period_answers_L445.json`: JPL's answers
  for target 3 (verbatim rows), Earth's entry as L-444's live run wrote
  it, Earth's elements answer read back from it, and for the check one
  answer built around JPL's row and one PLANTED answer for 399, each
  saying which it is.
- L-448: `test_orbit_cache.py` writes into a temporary folder it
  removes, and fails if a run leaves a file beside it (shown failing on
  a copy that writes into `test_output/` again); `.gitignore` gains
  `test_output/`; the patch deletes `test_output/test_orbit_paths.json`.
- horizons-orbital-mechanics 1.8 (its 1.5 entry to
  `documentation/SKILL_HISTORIES.md`), protocol v3.99 (v3.96 to the
  history file), the ledger's L-445 and L-448, Where We Are.

GALLERY (patch_L445_2_gallery_period_words_20261015.py)

- `gallery/solar_system_figures.js` `periodLine`: prints "for
  <target_label>, " before the centre when one is served; a period with
  none prints as before. The Earth room uses the same function.
- `documentation/smoke_solar_system_figures.js`: Earth's case as a
  sixth worked case, and a planted fault (the words dropped).

## 3. Method calls the brief left to the builder

- The map applies only to a period taken around the Sun. Earth around
  the Earth-Moon barycentre (the 'Earth@3' cache entry, from that view)
  is Earth's own monthly loop and stays 399. Tested with a planted
  fault that applies the map everywhere.
- `target_label` is null when the period is the body's own, so "for
  Earth" is never printed; a reader prints the words exactly when they
  are served.
- The seven other fetched bodies are NOT re-fetched. Their records
  predate L-445 and have no `target`; until L-445 the period was always
  asked of the id the elements fetch asked, which the cache's metadata
  keeps, so the export names that as their target. A confirmation
  written before L-445 is read the same way, so their periods are not
  made due by this build.
- A refused period query for Earth is UNREACHABLE with nothing saved,
  not a FAIL with the old record saved. Found by a planted fault, and
  fixed before delivery.

## 4. The drawn orbit and its markers

Earth's period stays around the Sun, so `drawing_orbit` pairs it with
the plot's own elements by centre: the drawn ellipse is Earth's own,
399's, as before. The perihelion and aphelion markers are now timed by
the barycentre's period instead of Earth's centre's; the aphelion
marker is half a period from perihelion, so its date moves by half the
difference of the two periods, a few hours. The marker's hover says
nothing about which period it was timed by, so its words need no
change. The orbit markers row passes unchanged ("4 ellipses, 1080
drawn points on their period's centre; 14 markers, 9 dates"), on its
own fixture. If the record ever chose the solar system's barycentre,
the guard keeps Earth drawn from its own elements and the orbit's
hover says whose period it is (tested).

## 5. Pre-test, on throwaway copies (nothing here was run on the deliverable)

- The orrery's maintenance run, whole, on a copy of the changed tree:
  31 of 31 gating checkers passed. The one red row was Period fetch,
  UNREACHABLE for Earth, because this workspace cannot reach JPL: it
  named Earth "period asked of 399, now 3" and saved nothing. FILES
  WRITTEN did not name `test_output/`, and no such folder was made.
- A rehearsal of the first live run on the same kind of copy, with
  JPL's recorded answers standing in for the network: the period fetch
  re-fetched Earth (target 3, around the Sun, fresh two-centre test);
  the Horizons check asked COMMAND='3' and agreed; the export wrote
  Earth's block with its target. The orrery printed:
  - hover: "Orbital period: 1.00000 years (365.25 days)" / "For the
    Earth-Moon center of mass, around the Sun, from JPL Horizons,
    fetched 2026-10-15." / "Rounded to how much the period changes in
    a year."
  - parameters window: "365.25 days (1.00000 yr), JPL, for the
    Earth-Moon center of mass, around the Sun"
- That export carried through the gallery: the mirror wrote the config,
  and the website's sentence read "Orbital period: 1.00000 years
  (365.25 days), for the Earth-Moon center of mass, around the Sun,
  from JPL Horizons, fetched 2026-10-15." The gallery's offline
  maintenance run then passed every row.
- Both patches run on copies of the repositories at the two SHAs above,
  LF and CRLF working copies; a second run refuses and writes nothing.

## 6. When the words reach the website

The period's words are config, not cache. The gallery's maintenance run
pulls the orrery's export from GitHub at the orrery's latest commit and
mirrors it into `data/objects_config.json`, so: the orrery push first,
then the gallery patch and its maintenance run, then the gallery push,
and the words are live on that push. Earth's centre does not change, so
the served cache needs nothing and no builder run is involved. The
Daily Run will pull the same export on its next run either way.

## 7. Tony's actions, all of them

- (do) Save `patch_L445_1_earth_period_20261015.py` in the orrery
  folder (it is already there if this session wrote it to your
  computer); open it in VS Code and click Run.
- (do) Run `orrery_maintenance_run.py`. Look for the Period fetch row
  naming Earth ("period asked of 399, now 3") and PASS, and the
  Horizons check comparing Earth's period with JPL.
- (do) Plot Earth from the Sun and look at its hover and the orbital
  parameters window.
- (decide) The hover's words: keep "For the Earth-Moon center of mass,
  around the Sun, from JPL Horizons, fetched <date>." or change them.
- (do) Move the patch into documentation/; commit (the commit includes
  the deletion of `test_output/test_orbit_paths.json`); push.
- (do) In the gallery folder, run
  `patch_L445_2_gallery_period_words_20261015.py`, then
  `gallery_maintenance_run.py`; move the patch into the gallery's
  documentation/; commit; push. Look at Earth's hover in the Solar
  System room and the Earth room.
- (do) Reinstall horizons-orbital-mechanics (1.8) in Settings > Skills;
  save PROJECT_INSTRUCTIONS.md as
  `documentation/project_instructions_v3_99.md` and copy it into the
  Project instructions.

Then the close: L-445 and L-448 to DONE, quoting your run record; Where
We Are's stage 8b to done.

Session written October 2026 with Anthropic's Claude Opus 5.5.
