<!-- Doc-Kind: generated | The skill manifest: each skill's version and when it fires, written by skills_index.py from skills/*/SKILL.md. Do not edit by hand. -->
# Skill manifest

Written by `skills_index.py` from each skill's own header (its
`fires_when` field) and its `Skill version:` line. Do not edit it by
hand: the next run rewrites the whole file. The protocol,
`PROJECT_INSTRUCTIONS.md`, keeps only the skills' names (v4.0,
L-522). A skill's own header is what loads it; this table is for
looking up versions and triggers in one place.

```
Skill                        Ver  Fires when
orrery-coding-conventions    1.14 Markers, hover text, axes, the opening view
                                  (Auto scale), shells, legendgroups,
                                  docstrings, new visuals
safe-file-editing            1.15 Editing existing files, patch scripts,
                                  sed/regex edits, encoding checks (portable)
agentic-pre-test             1.4  BEFORE delivering complete files/agentic
                                  code; after data-content sweeps
horizons-orbital-mechanics   1.21 Horizons queries, centers, frames, osculating
                                  elements, encounters, comet record pinning,
                                  2xr uncertainties, periods, the drawn orbit's
                                  centre, the Horizons check
                                  (horizons_check.py, its period comparison and
                                  the data sheets' re-read), the period fetch
                                  before it (period_fetch.py), which record
                                  serves a body (helio_id, re-pinning a comet,
                                  JPL's exact name, a body on a skip list), a
                                  spacecraft path's plan and its flybys
                                  (path_plan.py -- the Hill sphere, JPL's GM,
                                  the window and step, the orbiter rule for an
                                  arrival, a departure, a capture), a comet
                                  whose designation matches its own pieces, a
                                  comet on an open path's plan (its span, its
                                  TP, its perihelion), an entry asked by JPL's
                                  number in the Horizons check, the clock read
                                  as UTC (utc_clock), astroquery's saved
                                  answers (cache=), a 2xr answer with no figure
                                  (n.a.), Pluto's period asked of its
                                  barycentre, an ended mission's mission_end
                                  (its path stopped on the day it ended; the
                                  agency's own page; a craft that flew on and
                                  its end_note; an end after JPL's data; a cut
                                  on a craft still flying, path_cutoff and
                                  cutoff_file, JPL REFIT), a capture's passes
                                  of the Sun (riding_passes), a loiter near a
                                  Lagrange point (ESCAPADE's), the orrery's
                                  drawing of a path by its plan
                                  (path_drawing.py, only around the Sun), a
                                  small body drawn as a path or an orbit by its
                                  database e (path_or_orbit.py,
                                  data/small_body_solutions.json), an entry the
                                  website does not serve
                                  (horizons_unserved.py), JPL's dates on JPL's
                                  clock
provenance-discipline        2.37 Scanner runs, audits, citations, constants,
                                  pre-push (Tier-1 = 0 on the active build
                                  path)
provenance-cross-check       1.1  Cross-check worksheets and relay prompts,
                                  adjudicating returns, writing Cross-checked
                                  and Resolved lines
earth-system-pipeline        1.3  KMZ layers, Google Earth web, a layer's page
                                  and its walk, ERA5/ERDDAP/IPC, scenarios, ANY
                                  human-cost visualization or text
gallery-pipeline             1.3  Gallery Studio, json_converter, index.html
                                  viewer, gallery cards, the gallery editor's
                                  scene, encounter and link cards
ledger-and-session-records   1.25 Ledger edits, ledger_index.py, RICE,
                                  handoffs, manifests, atlas, dep_trace,
                                  WHERE_WE_ARE.md at every session's end
gallery-assembler            1.6  render_orbits.py, resolver.py,
                                  cache_reader.py, the seam between UTC and
                                  JPL's clock, propagation math, golden
                                  artifact builds, Mode 5 acceptance,
                                  orrery/assembler boundary questions, AND any
                                  time a served page misbehaves and the cause
                                  is unknown -- it hangs, it freezes, it is
                                  unresponsive, it worked yesterday, a console
                                  error appears, or Claude is about to hand
                                  Tony a test to run
gallery-cache-builder        1.24 Nightly builder, atomic swap and its
                                  retry/roll-back/swap log, "Access is denied"
                                  under data/, coverage_index, serving cache,
                                  objects_config, dry-run/first-build/nightly,
                                  builder testing layers, the Daily Run's order
                                  and a failed pull, the run records and their
                                  check, a spacecraft fetched by its path plan,
                                  a pull that does not match the push, a comet
                                  on an open path fetched by its plan
                                  (is_path_body, open_path), a small body's own
                                  uncertainty (position_uncertainty, the match
                                  rule), every JPL question asked fresh
                                  (HORIZONS_CACHE), a drawing named on a room's
                                  row, a path's last day, flying or ended
                                  (fetch_path_last_day), a held body (HELD), a
                                  Lagrange point served as a point
                                  (serving_shape 'point'), the clock block and
                                  its witness, an encounter's package
interactive-exhibit          1.45 a room or exhibit in interactive.html
                                  (?exhibit=); its drawer and chrome (nav
                                  cluster, frame zoom, i panel, HUD, text box,
                                  consent, back link); the served words and
                                  numbers a room prints and where they come
                                  from (store_writer, exhibit_store_editor,
                                  objects_config.json); what a room opens on;
                                  testing a room (the gallery run's checks,
                                  tools/headless); carding an exhibit in
                                  Studio; a Lagrange point's marker and box, a
                                  name's side (label_side_for); an encounter
                                  (data/encounters/, tools/encounter_fetch.py,
                                  its player); a card's fold beside a row
                                  (Scenes, Encounters, Links); a date a visitor
                                  reads (UTC); a page change's walks
```
