<!-- Doc-Kind: hand | Design record and session handoff for L-395's Horizons check: Tony's rulings from the design round of 2026-10-07, what JPL showed, and the build's scope. -->
# DESIGN -- L-395: checking the object list against JPL Horizons

Built on orrery 12693a53f9cb57c6beacada13f307985842b1780 at
https://github.com/tonylquintanilla/palomas_orrery, and gallery
4cfeca27d2a84171a0b278e20b1f79cf606a1f0b at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
This record lands with patch_L395_3_horizons_check_design_20261007.py;
the gallery is not touched.

Type: DESIGN SESSION (zero code). It is also this session's handoff.
Answers the five questions of
`documentation/HANDOFF_L395_horizons_check_design_20261005.md`.
Companion: `documentation/HORIZONS_ANSWERS_L395_20261007.md`, every
JPL answer Tony fetched this session, verbatim.

Session written October 2026 with Anthropic's Claude Opus 5.5.

## 1. Skills at session start

- Loaded and matching the protocol's manifest:
  horizons-orbital-mechanics 1.1, provenance-discipline 2.26,
  ledger-and-session-records 1.16, safe-file-editing 1.13.
- No skill changed this session.
- As the 2026-10-05 handoff asked, the opening checks (closing L-369,
  L-418, L-419) were left to the website session, and this session's
  ledger edit touches only L-395.

## 2. How the design was tested

- This chat's sandbox cannot reach JPL. So Tony ran each query in his
  browser and pasted the answer back: 28 answers, from two JPL
  services.
  - The Lookup service, `horizons_lookup.api`, which turns a name or
    number into the objects it matches.
  - Horizons' main service, `horizons.api`, which answers about one
    record or lists every record for a designation.
- Every claim in section 3 rests on one of those answers, named by
  its group and number in the companion file.

## 3. Tony's rulings, in the order they were made

Each was "confirmed" or "confirmed as recommended" unless quoted.

### Question 1: what JPL can confirm

- For each entry, JPL can confirm that it names exactly one object,
  and that object's name, type and designation.
- JPL cannot confirm the project's modelling choices, such as drawing
  Pluto about its barycentre, or our descriptions and links.
- A bare number is ambiguous, in two ways:
  - It matches an asteroid with that number: "499" also finds asteroid
    499 Venusia, "10" also finds 10 Hygiea (A2, A3).
  - It matches spacecraft with that number in their names: "9" finds
    an Apollo 9 rocket stage and two Falcon 9 boosters (A1).
- Searching only the major-body index removes the asteroids (D4) but
  not the spacecraft (B1), because spacecraft are in that index too.
- So the check finds an entry's object in three steps:
  - Search JPL for the entry's `id`, limited to the index its
    `id_type` points at: blank means the major-body index (`group=mb`),
    "smallbody" means the small-body index (`group=sb`).
  - Keep only the match whose primary id equals the entry's `id`
    (major bodies), or whose primary designation equals it (small
    bodies, such as Apophis's `2004 MN4`).
  - Exactly one match must remain. Zero, or more than one, is a
    failure, printed by name.
- The check reads JPL's live answers, never a copy of JPL's
  documentation. The documentation gives Apophis's primary id as
  2099942 in one example; the live answer is 20099942, with 2099942
  as an older alias (C1).

### Question 2: which fields are compared, and what agrees

- `id` agrees when the steps above leave exactly one match.
- `id_type` agrees when the object is found in the index it points at
  and not in the other. Tested on purpose: Apophis is not found in the
  major-body index (E1), and Mars is not found in the small-body
  index, where "499" finds only 499 Venusia (E2).
- `horizons_name` (new, below) agrees when it equals JPL's object name
  exactly, character for character.
- `object_type` is compared only where it means something: "barycenter"
  against JPL's "barycenter", and the Sun's "fixed" against JPL's
  "Sun". The value "orbital" covers planets, asteroids and comets
  alike, so it is not checked; JPL's type is printed beside it. A
  clean kind field is L-395's separate round.
- Descriptions and links are not compared.

### A new field: `horizons_name`

- Tony asked to bring the list in line with Horizons' naming. A rename
  of the display names was weighed and not chosen:
  - An object's `name` is also the key other tables look it up by.
    "Pluto-Charon Barycenter" appears 37 times across 8 modules, 15 of
    them in `palomas_orrery.py`; "Apophis" 9 times across 7 modules,
    including `constants_new.py`.
  - Renaming them in step would touch all five paths that draw
    positions, and a missed one fails silently.
- Ruled instead: each checked entry gains `horizons_name`, JPL's exact
  name for the object.
  - `name` stays the orrery's own choice; none of its uses change.
  - `horizons_name` is a claim about JPL. Nothing in the orrery reads
    it except the check.
  - It is not an alias. In JPL's answers "Aliases" means other ids and
    designations for one object.
  - The display-name rename can come later, in the round that stops
    names being used as keys.
- What it catches: JPL renames objects, for instance when an asteroid
  is numbered or named. The check would report the change the day it
  happens.

### Question 3: where the check runs, and how often

- Two pieces.
  - The live check, Daily Run step 2, before the cache builder (Tony's
    placement: "I usually do the daily run suite first thing in the
    day"). It queries JPL for the entries that are due, prints every
    disagreement, and records each confirmation (date and what was
    confirmed) in a small file such as
    `data/horizons_confirmations.json`. If JPL cannot be reached it
    says so, records nothing for that entry, and the step fails.
  - The offline checker, in the gallery maintenance run (which is
    also Daily Run step 4, and runs before a push). It never touches
    the network. It fails when a served object has never been
    confirmed, is overdue, or has had its `id`, `id_type` or
    `horizons_name` changed since it was last confirmed. Without it,
    nothing would show that the live check had stopped running.
- So the check lives in the GALLERY repo, because `daily_run.py` does.
  - It reads the pulled `data/objects_export.json`, not
    `celestial_objects.py`. That is equivalent: the orrery's
    maintenance run already proves the export matches the list.
  - The export gains `horizons_name`.
- As every Daily Run step does, a failure in step 2 does not stop the
  cache build; the summary at the end names it.
- Cadence: each object is re-confirmed every 30 days, and at once
  after its entry changes. The 30 can be tuned later.
- Load on JPL (Tony asked about rate limits):
  - JPL publishes no per-hour limit for the Lookup that this session
    could find. Its documentation lists a "service unavailable" answer
    (code 503) for overload or maintenance.
  - A third-party Horizons library warns that JPL throttles parallel
    queries. That is the library's statement, not JPL's.
  - Safeguards, ruled in: one query at a time with a short pause
    between; any error counts as "could not reach JPL" and never
    passes; no rapid retries, a failed entry stays due for the next
    day; the 30-day cadence spreads the load when more entries arrive.
- The chat's network setting is not needed. The check runs on Tony's
  machine, which already reaches JPL every morning. Without the
  setting, the build is tested against the companion file's answers,
  and the first Daily Run after the build is the first live run.

### Question 4: pinned comet records

- A pinned record is an `id` that is one of Horizons' individual
  solution records (9000xxxx), not the comet's designation.
- The Lookup cannot see record numbers: "90000030" and "90000091" both
  return no matches (F2, F4). It knows Halley as "1P" and Encke as
  "2P" (F1, F3).
- So a pinned entry is checked through Horizons' main service:
  - Ask for the record: it must exist, and its name must equal
    `horizons_name`. For a pinned record `horizons_name` holds the
    main service's form, "1P/Halley" and "2P/Encke" (G1, G3).
  - List every record for that comet's designation (G2, G4). The pin
    must be the newest. If a newer record appears, the check reports
    "pin is stale" for Tony's ruling; it never re-pins on its own.
  - Record the record's solution date with each confirmation, as
    information, not a failure.
- Both pins are current today. Halley's `90000030` is the newest of 30
  records, the 1968 apparition; Encke's `90000091` is the newest of
  61, the 2023 apparition.
- JPL updates a record in place. Encke's record carries a solution
  dated 2026-Oct-01, fitted to observations through that day; Halley's
  was re-solved on 2025-Nov-21. So a pin fixes the apparition, not the
  numbers, and goes stale only when JPL adds a newer record. For Encke
  that should come around its next return, about 2027 (period 3.3
  years, last perihelion 2023-Oct-22, G3).
- Comets that are not pinned need nothing new. 3I/ATLAS's `id`
  `C/2025 N1` equals JPL's primary designation, and "3I" is an alias
  of the same record (F6, F7).

### Encke gets a list entry (Tony's proposal)

- Encke is served by the gallery (in `data/objects_config.json`,
  record 90000091) but has no entry in the orrery's list. So the
  gallery holds Encke's only definition, against the ruling that the
  list is the one definition of each object.
- Ruled: Encke is added to the list, which also makes it selectable in
  the orrery's own window. The entry:
  - `name` "Encke", matching Halley's style.
  - `id` `90000091`, the newest record.
  - `id_type` "smallbody".
  - `horizons_name` "2P/Encke".
  - `key` "encke", so the export carries it and the gallery's copy
    comes through the mirror like the other eleven.
- The gallery's entry keeps only its serving choices (the Tp anchor,
  the distance limit).

### Question 5: what each run prints

- Which copy of the list it checked, at which orrery commit.
- How many entries it examined, how many were due, and how many it
  queried.
- One line per entry: "agrees", "DISAGREES", "not due (confirmed on
  date)", or "could not reach JPL".
- For a pinned comet: whether the pin is the newest record, and the
  solution date.
- For each disagreement: the entry and the field; the list's value and
  JPL's value one above the other; and the exact query used, so Tony
  can paste it into a browser and see JPL's answer himself.
- A closing line: PASS, or FAIL naming every disagreeing entry and
  field.
- The check never edits the list. It runs in the gallery repo and
  cannot reach `celestial_objects.py`. Fixes come through a session's
  patch: simple errors fixed and reported, choices brought to Tony.
- The first live run is expected to show every entry agreeing, because
  `horizons_name` is filled from today's answers. So the offline tests
  must include deliberately wrong entries, and the check must catch
  every one (A Check That Cannot Fail Is Not Passing).

### MAPS and 3I/ATLAS: tested cases, not yet checked live

- Tony added them to the test sample, with Halley, as three kinds of
  comet the planets cannot test.
  - MAPS (`C/2026 A1`), a sungrazer. JPL holds one record, 90004956,
    named "MAPS (C/2026 A1)", with one solution dated 2026-Jun-05,
    fitted to 472 observations from 2026-Jan-13 to 2026-Mar-28 (G5).
    Perihelion was 2026-Apr-04 at 0.0057 au from the Sun's centre. So
    the observations behind the solution stop a week before
    perihelion.
  - Searching "2026 A1" among comets finds only MAPS itself (F5): as
    far as these answers show, JPL holds no fragment records. The
    orrery's own MAPS plot draws a disintegration marker and a ghost
    tail, not fragments; those layers are not Horizons facts and the
    check does not compare them.
  - 3I/ATLAS (`C/2025 N1`), on a hyperbolic orbit. JPL calls it "ATLAS
    (C/2025 N1)" and lists "3I" as an alias (F6, F7).
- They show that JPL's comet names carry the designation in brackets,
  so our "MAPS" and "3I/ATLAS" would not equal JPL's names. The
  `horizons_name` field holds JPL's form, so that is no obstacle.
- Ruled: tested cases now, with their answers in the companion file.
  They are checked live when the website serves them, or when stage 9
  reaches the rest of the list.

## 4. Found this session, recorded on L-395

- Encke is served with no list entry (above; ruled to be fixed by the
  build).
- The gallery's note on Encke in `data/objects_config.json` calls its
  record a "2022-epoch solution". JPL gives the epoch as 2023 (G3,
  G4). The note goes when Encke's identity facts move into the list.
- `objects_config.json` serves 19 objects. Only the eleven come from
  the export. Eight carry identity facts defined in the gallery: Moon,
  Io, Titan, Pluto, Charon, Voyager 1, Halley and Encke. Seven of them
  have list entries without a `key`; Encke has none. L-395's Gap
  already lists the remaining served objects as open.
- JPL's own Lookup documentation is out of date for Apophis's primary
  id (above).
- I predicted that "9" would match asteroid 9. It did not; the extra
  matches were spacecraft (A1). Recorded because the design moved on
  the answer, not the prediction.

## 5. The build, for the next session

Read this record and the companion file first. Pull both repos at
HEAD and name each commit; the website session may have pushed.

In the ORRERY repo:
- `horizons_name` on the twelve keyed entries, from today's answers:
  Sun "Sun", Mercury "Mercury", Venus "Venus", Earth "Earth", Mars
  "Mars", Jupiter "Jupiter", Saturn "Saturn", Uranus "Uranus", Neptune
  "Neptune", Pluto-Charon Barycenter "Pluto Barycenter", Apophis
  "99942 Apophis", Encke "2P/Encke".
- Encke's new entry, with the fields in section 3. It also needs what
  every list entry carries -- `var_name`, `color_key`, `symbol`,
  `object_type`, a description (`mission_info`) and a link
  (`mission_url`) -- following Halley's entry as the pattern. The
  description's words and the link are Tony's to approve, and any
  number in the description is sourced or left out
  (provenance-discipline, A Simple Error a Check Finds Is Fixed and
  Reported). Check what else in the orrery looks Encke up by name
  before adding it.
- `export_objects.py` and `test_objects_export.py` carry
  `horizons_name`; the test fails on a keyed entry without one.

In the GALLERY repo:
- The live check, a new script, as Daily Run step 2 in
  `daily_run.py`, with its own Dashboard button, the way Earth Pole
  Live Check has one.
- The offline checker, in `gallery_maintenance_run.py`.
- The mirror copies `horizons_name` if the website needs it; otherwise
  only the check reads it from the pulled export.
- Encke's facts come from the export after the next pull and mirror.
  Check what the mirror writes over the gallery's current name
  "2P/Encke": the website's displayed name would become the list's
  "Encke" unless the build says otherwise.
- Offline tests built on the companion file's answers, including
  deliberately wrong entries the check must catch. Re-fetch each
  answer once first, as the companion file says.

Order: orrery first (the field and Encke's entry, then the export),
push; then the gallery.

## 6. For Where We Are

The website session owns `documentation/WHERE_WE_ARE.md` this round.
These lines are for its next rewrite:

- Changed this session:
  - The check of the orrery's object list against JPL Horizons is
    designed. Tony tested every part of it by hand against JPL's own
    services.
  - Encke will get its own entry in the orrery's list; until now only
    the website defined it.
- Do next:
  - *The check is built, in a fresh session, from
    `documentation/DESIGN_L395_horizons_check_20261007.md`.*
- Waiting on you, at the build:
  - Encke's description and link.
  - Whether Halley joins the check too (below).

## 7. Open for Tony

- (decide) At the build: whether Halley is keyed and checked too. It
  is served by the gallery, has a list entry, and is the other pinned
  record. Keying it makes the pinned-record check test two pins
  instead of one; it also brings Halley's words and link from the
  list to the website.
- (decide) At the build: Encke's description and link.

## 8. Tony-actions, rolled up

- (do) Run patch_L395_3_horizons_check_design_20261007.py in the
  ORRERY repo root (VS Code, Run).
- (do) Run orrery_maintenance_run.py; it rebuilds the ledger's index.
- (do) Move the patch into documentation/; commit and push.
- (decide) At the build: Halley, and Encke's description and link
  (section 7).
