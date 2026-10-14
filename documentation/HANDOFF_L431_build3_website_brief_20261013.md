<!-- Doc-Kind: hand | Brief for L-431 build 3, the website: the orrery's export carries each body's period and the elements around its centre; every room's hover prints the period by the orrery's digits rule and draws the orbit around that centre; the Horizons check compares the period, and the check itself moves into the orrery's maintenance run (L-395) in the same session, so the comparison is built once, where it will live. The path back to the gallery. -->
# Brief: L-431 build 3, the website, with the Horizons check's move (L-395)

Built on orrery 28e1b7d1 at
https://github.com/tonylquintanilla/palomas_orrery ("maintenance", after
L-437's close) and gallery 924977a3 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io ("daily run
10-13-26"). This build touches BOTH; pin each at HEAD when the session
starts.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 13, 2026 with Anthropic's Claude Fable 5.1, in the
coordination session of October 12 and 13.

- Type: BUILD brief (zero code). The design is settled on L-431's
  record; Mode 5 on the phone is the acceptance.
- Companions: `documentation/DESIGN_L431_orbital_periods_rulings_20261011.md`
  (section 2 item 6, "periods are basic data, for all bodies and should
  be part of the hover text"; section 3 item 3, this build);
  `documentation/HANDOFF_L431_period_build1_20261011.md` (the period
  record's fields); `documentation/HANDOFF_L431_build2_look_fixes_20261013.md`
  (what the drawn orbit does around the barycentre, and Tony's ruling
  that no perturbation lines are drawn for it); L-401's digits rule
  (`documentation/DESIGN_L401_distance_digits_rulings_20261011.md`);
  provenance-discipline, A Computed Position Prints What Its Errors Earn
  (the website's existing display-figures rule).
- Why now: Tony, 2026-10-13, "I've gotten away from the gallery work.
  What's our path back?" This is stage 6a's last line and the first
  build in a week that opens the gallery's renderers. It reconnects
  what the orrery learned about periods and digits to what a visitor
  sees.
- **The Horizons check's move rides this build** (Tony, 2026-10-13:
  "should the initial horizons 30-day check go with this build?" --
  yes). Build 3 has the check compare each served period with JPL;
  the move (L-395) puts the check in the orrery's maintenance run
  beside the export. Built apart, the comparison would be written into
  the website's copy and then lifted out and rewritten in the orrery.
  Built together it is written once, where it lives, and the website's
  daily check reads the confirmation dates from the export from the
  start. The move's own brief,
  `documentation/HANDOFF_L395_horizons_check_move_brief_20261012.md`,
  is read WITH this one and its sections 2 to 4 are this build's
  sections 2d and 4 below; its first decision is ruled (option A,
  `DESIGN_rulings_20261012.md` ruling 6); its second has a default of
  no. The scaffolding list drops to three; the coordination note says
  so.

## 0. Before building

- Pull both repositories at HEAD and pin each SHA. Confirm no other
  session is building in the gallery (the design record's condition for
  this build). The dashboard-labels session may still be open; it
  touches the gallery only to rename maintenance-run rows.
- Skills this task fires: gallery-cache-builder (the nightly builder,
  the served cache, objects_config), interactive-exhibit (what a room
  may render and where its numbers come from; the served-data
  provenance contract), gallery-assembler (render_orbits.py, the
  propagation; the orbit drawn around a centre), horizons-orbital-
  mechanics (confirm 1.5: The Drawn Orbit Follows the Period's Centre),
  provenance-discipline (confirm 2.29), safe-file-editing,
  agentic-pre-test, ledger-and-session-records. Confirm each against the
  manifest at HEAD.
- Read `export_objects.py`'s docstring: only an entry with a `'key'` is
  exported (13 today), and the website's `tools/mirror_objects.py`
  copies named fields only. The export's schema is versioned
  (`schema`); this build bumps it.

## 1. What is settled

- The period comes from the orrery's fetch, every body; the typed
  table only when nothing was fetched, marked (L-431 rulings 1 to 5).
- Centre: the one whose period moves less in a year, named in the
  hover; moons and the Pluto system keep their own centre (ruling 2,
  method 3).
- Digits: the larger of the year's movement and SBDB's sigma, years
  and days each by its own error (ruling 3). The website's hovers print
  by the same rule as the orrery's, through the same place the
  website already grades a computed distance.
- The drawn orbit follows the period's centre; a barycentre ellipse in
  a Sun-centred scene is moved to where the barycentre is, found from
  the body's two element sets at one date (skill 1.4); no perturbation
  lines for an orbit drawn around the barycentre (Tony, 2026-10-13;
  skill 1.5).
- The Horizons check compares the period with JPL (ruling 6).

## 2. The build, by repository

### 2a. Orrery: the export carries the period

- `export_objects.py` writes, per exported object, the period record
  the orbit cache holds for it: centre, period in days, the error in
  days and what governs it (year change or SBDB sigma), the SBDB status
  words, the fetch date, and the elements around that centre with
  their epoch. A body with no fetched record exports the typed value
  marked `typed: true`, or nothing, by the fallback order. The
  export's `schema` bumps; `numbers` carries the period's figure count
  by the orrery's rule, as it carries the others.
- `test_objects_export.py` refuses an export whose period does not
  match the cache record it came from, and one that carries a period
  with no centre.
- The export is deterministic from `celestial_objects.py` plus the
  cache; say in the docstring that the cache is now an input, and
  fingerprint it.
- **Added 2026-10-13, on Tony's confirmation (L-431).** For a body
  whose period record names the solar system's barycentre (Sedna), the
  export carries BOTH element sets: the barycentre ones from the period
  record, which are drawn, and the Sun-centred ones the orrery fetches
  every time, at the same date. A barycentre ellipse is placed in a
  Sun-centred scene by pairing the two (horizons-orbital-mechanics, The
  Drawn Orbit Follows the Period's Centre): the body's position from
  each set at that date gives where the barycentre sits seen from the
  Sun, and the orbit is moved there. With the barycentre set alone the
  website cannot place the orbit. The pair is exported only when both
  sets are from one fetch date, as the orrery pairs them; otherwise the
  body is drawn from its Sun-centred elements, as the orrery does, and
  the export says so. `test_objects_export.py` refuses a barycentre
  record exported without its Sun-centred set. Tony, 2026-10-13, asked
  whether the heliocentric data should also be fetched, was told it
  already is and must travel with the barycentre set: "confirmed."

### 2b. Gallery: the mirror, the builder, the rooms

- `tools/mirror_objects.py` carries the new fields into
  `data/objects_config.json` as COPIES, never by hand; the Objects
  mirror check learns them. The cache builder reads the centre from
  the config when it fetches a body's elements, so the served elements
  and the served period share one centre.
- Every room's hover (`gallery/feature_renderers.js` or wherever the
  body hover is built; `gallery/solar_system_figures.js` for the Solar
  System room's figures) prints "Orbital period: N years (M days),
  around <centre>, from JPL Horizons, fetched <date>", the digits from
  the export's figure count, through the same grading
  `smoke_display_figures.js` and `smoke_solar_system_figures.js` already
  check. A typed period says so.
- The drawn orbit in a room follows the export's centre, using
  `render_orbits.py`'s existing propagation around the elements'
  centre; a barycentre orbit in a Sun-centred room is offset to the
  barycentre's position on the scene date (the orrery's method, skill
  1.4), and draws no perturbation lines.
- The Horizons check compares the served period with JPL's PR for
  each due object, as it compares id and name today; it does so from
  the orrery, after 2d.

### 2d. The Horizons check moves into the orrery (L-395), and compares the period

The move brief's section 2 is the shape; its section 4 the build
notes; read both. In this build's terms:
- A row of the orrery's maintenance run, beside the objects export,
  asks JPL only about entries that are due (never confirmed, 30 or
  more days old, or changed since) and re-reads each spacecraft's data
  sheet on the same cycle. It compares id, id_type, horizons_name,
  object_type where it means something, AND the period (PR) against
  the export's. A changed data sheet is cleared only by a patch to the
  row (ruling 6, option A).
- The confirmations live in the orrery's `data/`; the export carries
  each object's confirmation date and what was confirmed, beside its
  period. The thirteen confirmations of 2026-10-10 are carried over
  with their dates so the move re-asks JPL for nothing.
- The website's daily run loses step 2; its offline check stays and
  reads the dates from the pulled export, going red on the day a
  confirmation turns 30 days old and naming the objects.
`tools/horizons_check.py`, `tools/test_horizons_check.py` and the
recorded answers move into the orrery; the dashboard's buttons follow
them (every check keeps its button). The network-row convention this
sets (UNREACHABLE by name, never a pass) is the one L-425's link check
will match.

### 2e. Not in this build

- Adding objects to the website (L-438, its own brief).
- The typed table's 132 entries (one class, not chased).
- L-401 build 3's orrery slices (fly-to, parameters window, animation).

## 3. The look (Mode 5, on the phone and the desktop)

The Solar System room: hover Mercury, Sedna is not served, so hover
Encke and Pluto's barycentre; each shows its period line with the
centre named. Encke's and Halley's orbits still draw. Then the Earth
room and the Sun room: the period line on Earth and on one moon. The
smoke suites pass offline before Tony looks; the look judges the
words and the drawn orbits.

## 4. Build notes (method; the build session settles these and records them)

- Two patches, one per repository, each anchored, all-or-nothing, LF,
  ASCII, stamps moved: the orrery's first (it changes the export the
  gallery pulls, and gains the check's row), then the gallery's (the
  rooms, the mirror, the daily run losing step 2). The gallery patch refuses unless
  the pulled export carries the new schema, so Tony cannot run them out
  of order.
- Planted faults, shown caught: an export with a period and no centre;
  a mirror that drops the centre; a room hover printing a period to
  more figures than the export's count; a barycentre orbit drawn
  around the Sun; a Horizons check that passes a period JPL disagrees
  with. The smoke suites are Node; they run offline in the sandbox.
- The sandbox cannot reach JPL. The Horizons comparison is tested on
  recorded answers (the check's existing `horizons_answers_L395.json`
  pattern); Tony's Daily Run is the live test.
- Pre-test: the orrery's export round trip (export, pull, mirror, build
  dry-run, the rooms headless through `tools/headless`), the gallery's
  27 offline checks, and `gallery_maintenance_run.py` green before
  delivery.
- The Daily Run after Tony's push rebuilds the cache; a period reaches
  a visitor only then (gallery-cache-builder: a config change is not
  deployed until the cache is rebuilt). Say so in the handoff's run
  order.
- Skills: interactive-exhibit (what a room renders: the period line,
  its source), gallery-cache-builder (the builder reads the centre from
  the config; the daily run's steps), horizons-orbital-mechanics (where
  the check lives, the sheets' re-read). One version each, under One
  Session, One Bump, with the protocol entries and the manifest run in
  the same commit.
- Close: L-431 closes (all three builds) and L-395 closes (the check
  moved), each with its loose ends re-homed; the road's stages 6a and
  8 to [done]; Where We Are by section within its cap.

## 5. For Tony, one at a time, in the build session

- (decide, at the look) The render, on the phone and the desktop.
- (decide, only if raised) Whether a body with only a typed period
  prints it on the website at all, or prints "period not yet fetched".
  Recommended: print the typed value marked, as the orrery does, so the
  two agree.
- (decide, recorded, not urgent) Whether the identity check widens
  past the thirteen keyed entries (the move brief's second item).
  Default no; L-438 revisits it as objects are added.

## 6. Tony's actions, all of them

- (do) Finish the current machine list (patch_L436_1, the maintenance
  run, the two reinstalls, L-269's patch held, push).
- (do) Start the session from this brief.
- (do) Run the orrery patch, the orrery maintenance run, push; run the
  gallery patch, the Daily Run (it rebuilds the cache), push; the live
  check; then the look.
- (decide) The look.

Brief written October 2026 with Anthropic's Claude Fable 5.1.
