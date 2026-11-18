<!-- Doc-Kind: hand | Brief for a Claude Code session (build): ESCAPADE's path (L-533) -- the two craft, Blue and Gold, drawn in the Solar System room by their path plans, their Earth flyby, their months at L2 shown as a new kind of event (a loiter), and their arrival at Mars; across both repositories. -->
# Brief: ESCAPADE's path (L-533)

Tony Quintanilla, PE | Claude Opus 5.5 (coordinating session) | November 18, 2026, morning, Chicago

Built on orrery 0d2b5ebe1bd823cce034ad4c3f01038a085e3aaa at
https://github.com/tonylquintanilla/palomas_orrery and gallery
41029763feab805f8749fd9a8d38676809f8ccb1 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, both read
live on Nov 18, 2026, 08:51 Chicago. The orrery commit that carries
this brief is Tony's push of it on top of 0d2b5ebe.

Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`,
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.

Type: BRIEF for one Claude Code session, opened through the python_work
door, working in both folders: the orrery first, then the website. Opus,
high effort (orbital mechanics, by `METHOD_MODEL_EFFORT.md`). Three
parts, a report and Tony's go-ahead after each. Its last report ends
with its token count as Claude Code prints it (the protocol's Token
Economy).

The machinery is the path plan's (L-443, L-476) and the more-voyages
build's (L-507): read L-533's body on the ledger first, then
`documentation/COORD_L507_historical_missions_more_voyages_brief_20261105.md`
for the shape of keying a craft in both repositories. This brief says
only what differs.

## 1. Why, in two sentences

Road stage 15 on Where We Are: ESCAPADE's path, next after El Nino's
page (Tony, Nov 18, 10:08: "Let's move on the path build and then the
design."). It is the first of three parts Tony set out on Nov 15 (16:16,
"There are three paths: paths under spacecraft, paths under
destinations, encounters at every flyby and destination"); only the
first is this build.

## 2. What this build is, and is not

IS: Blue and Gold drawn in the Solar System room as Psyche and Europa
Clipper are, each by its path plan, with rows in the drawer's Spacecraft
group, in the orrery and on the website.

IS NOT, each waiting for the design round after this build (L-534
(missions by destination), L-529 (guided encounters)):
- a row under Mars, or any destination row;
- an encounter told as a story, or entries in `spacecraft_encounters.py`;
- the Lagrange points drawn as bodies (L-297, after the design round).

## 3. The rulings

- Tony, Nov 15, 16:07: "Yes let's draw it now and add it as a row under
  mars too in addition to the spacecraft drawer." The Mars row rides the
  destination rule, built for every mission at once: not here.
- Tony, Nov 15, 16:22, "Yes", to the coordinator's correction: a
  Lagrange point has no mass and gives no gravity assist. ESCAPADE's time
  at L2 is shown as its OWN KIND OF EVENT, a loiter at a Lagrange point,
  in NASA's words. The gravity assist stays at the powered Earth flyby.
- The craft's identity is read from JPL, never typed (L-533's body):
  ESCAPADE-Blue is -9, ESCAPADE-Gold -10, read in Horizons on Nov 15.
  "EscaPADE STAGE" (-9901495) is the rocket stage, not a craft to draw.

## 4. What is already found, at the two SHAs above

Every line was read from the code or the page. Re-read before building.

NASA's article of 2026-11-09, read again Nov 18,
https://science.nasa.gov/science-research/heliophysics/nasas-escapade-completes-powered-earth-flybys-now-en-route-to-mars/:
- Launched Nov 13, 2025; a "loiter" or "Earth-proximity" orbit around
  L2, about a million miles from Earth, a "kidney-bean-shaped course".
- EACH CRAFT MADE ONE POWERED EARTH FLYBY, not two. "The first
  spacecraft made its closest approach around 5 a.m. EST on Saturday,
  Nov. 7", about 1,000 miles up; "the second did so two days later",
  Nov 9, about 650 miles up. L-533's body says "the Earth flybys" of
  each path as if both made two: that is wrong, and this build's
  records correct it.
- The page never says which craft is Blue and which is Gold, and gives
  the Mars orbit insertions only together: "planned for Sept. 7 and
  Sept. 9, 2027". So which craft flew by first, and which arrives first,
  is read from JPL's positions by the plan, never assigned from the page.
- L-533 also records JPL's data ends: Blue to 2027-Sep-12 00:28, Gold to
  2027-Sep-10 00:28.

The orrery:
- No file mentions ESCAPADE.
- A flying craft's entry, Psyche's (`celestial_objects.py` line 1200):
  'key', 'id', 'horizons_name', 'var_name', 'color_key', 'symbol'
  'diamond-open', 'object_type' 'trajectory', 'id_type' 'id',
  'is_mission' True, 'start_date', JPL's limits as comments,
  'mission_url', 'mission_info'. No 'end_date' (a planned entry carries
  none, L-476).
- The other places a craft is named: `palomas_orrery.py` (its IntVar,
  line 3484 for JUICE's, and its `create_mission_checkbutton`, line
  10162), `constants_new.py` (its colour, line 5548 for Psyche's),
  `info_dictionary.py` (its info text, line 1392 for Psyche's, quoting
  JPL's sheet). Map them again by grep before editing; this list is a
  start, not a proof.
- `path_plan.py`: the searched bodies are `MAJOR_BODIES` (line 278) and
  the served small bodies; an event's kind is flyby, arrival, departure
  or perihelion (`WORD`, line 260); `orbiter_rule` (line 646) groups the
  days inside a body's Hill sphere into stretches, and a stretch with
  more than one nearest approach is a capture, its approaches between
  the first and last dropped.

The website:
- Psyche's entry, `data/objects_config.json` objects[28]: slug
  `psyche_spacecraft`, parent `sun`, centre `@sun`, category and
  availability `spacecraft`; its path plan copied in by the mirror. Its
  drawer row: `rooms.solar-system.drawer.rows[52]`, `"in":
  "spacecraft"`, after which comes Europa Clipper's.
- Colours: `gallery/assembler/presentation.py` line 103.
- `tools/gallery_cache_builder.py`, `CENTER_SLUG_MAP` (line 233) reads
  '9' and '@9' as the Pluto-Charon barycentre, and at line 393 strips a
  leading '@'. Blue's id is '-9'.

## 5. The three things to measure first

THE EARTH STRETCH. The orbiter rule could misread ESCAPADE's year near
Earth. L2 lies about as far from Earth as the edge of Earth's Hill
sphere (both near 1.5 million km by the textbook figures; read both from
JPL in the run). If a craft stays inside Earth's Hill sphere from launch
to its flyby, the rule reads one long stretch with several nearest
approaches: a capture already under way on the first day, whose
approaches between are dropped. Then the flyby could be printed as a
"departure", or lost. If the craft drifts in and out at the edge, the
stretch breaks into pieces with nearest approaches of their own, and
could print flybys that NASA never describes.

THE MARS ARRIVAL. JPL's data runs only one to three days past each
orbit insertion. A capture needs more than one nearest approach inside
Mars's Hill sphere. With one, the rule prints a "flyby" of Mars.

THE LOITER. No rule finds one today. JPL serves the Lagrange points as
bodies: the Sun-Earth-Moon barycentre's L2 is 32 (L-533's body). The
loiter is found from JPL's positions, not typed from NASA's page; its
words are NASA's.

## 6. The work, in order

PART 1. Orrery, key and measure. Nothing pushed.
1. Read each craft's record in JPL: its exact name for 'horizons_name',
   its first and last day, its data sheet. Confirm -9 and -10 by the
   main service (JPL's Lookup with "ESCAPADE" finds only the stage, by
   L-533's body).
2. Key both entries in `celestial_objects.py`, Psyche's shape, keys
   `escapade_blue` and `escapade_gold` (the website's slugs), and their
   places in `palomas_orrery.py`, `constants_new.py` and
   `info_dictionary.py`. The words are placeholders until section 7's
   "Approved".
3. Run `path_plan.py` for the two and print each plan's span and events.
4. Measure, launch to flyby, daily: each craft's distance from Earth,
   from L2 (body 32), and Earth's Hill sphere radius as `hill_km` gives
   it. Print the counts, not the table: how many days inside, how many
   stretches, how many nearest approaches in each.
5. REPORT, then STOP:
   - each plan's events beside NASA's (one Earth flyby each, Nov 7 or
     Nov 9; Mars orbit insertion Sept 7 or 9, 2027), and which craft is
     which;
   - each event that disagrees, named;
   - a proposed rule for the loiter, with its numbers (what makes a
     stretch of days a loiter, what the event records, what its window
     and step draw), and whether it, or any change to the orbiter rule,
     could change another craft's plan;
   - one question at most for Tony.
   Tony's go-ahead decides the loiter rule. The rule then goes into
   horizons-orbital-mechanics (section 8): it is method from then on.

PART 2. Orrery, build and export.
6. The loiter kind in `path_plan.py`, by the rule as ruled, with its
   case in `test_path_plan.py`, shown failing once on a planted fault.
   If the rule can change another plan, `RULE` moves and every plan is
   made again: say which plans and about how long it takes, before it
   runs.
7. Map every reader of an event's kind before adding one, in both
   repositories (the protocol's Check All Parallel Pipelines): the
   orrery's drawing (`path_drawing.py`), the export, the mirror, the
   builder's thinning of an event's window, and the room's box. Name
   them in the report.
8. The orrery's maintenance run, green, read from its output; Tier-1 0
   on the gate path.
9. REPORT: files changed, the plans as made, a desktop plot of both
   craft Sun-centred and centred on Earth (a picture each), the readers
   mapped. Tony's go-ahead.

PART 3. Website, in the same round as the export's new keys (a key in
the export with no website entry stops the mirror, and the night with
it; horizons-orbital-mechanics, KEYING).
10. The two entries in `data/objects_config.json` (the mirror fills the
    rest); their rows in the Spacecraft group after Europa Clipper's;
    colours in `presentation.py`; the loiter in the box and in every
    reader named at step 7.
11. A check that the builder can never read '-9' as the Pluto-Charon
    barycentre, shown failing once on a planted fault (an lstrip of
    '-').
12. CACHE: a hand build, so Tony sees them before the night. Read each
    positions file's size and say it; say how many points the loiter
    adds.
13. Both maintenance runs green, read from their output.
14. REPORT, with Tony's run order ending in his phone look: both craft
    ticked from Spacecraft, their boxes, the flyby and the loiter seen
    with Go To Earth and Earth's frame zoom.
15. PUSH ORDER: orrery first, then the website, the same evening, not
    while a night is running.

## 7. The words, Tony's before they are written

Draft in `documentation/WORDS_L533_escapade_20261118.md` (slice 1's
`WORDS_L507_historical_missions_20261102.md` is the shape) and wait for
his "Approved". Plain words, one sentence to a bullet, each with its
source:
- each craft's description and info text (JPL's sheet; NASA's page);
- the loiter's words, NASA's own ("loiter", "kidney-bean-shaped
  course");
- the colours. Blue and Gold suggest themselves; that is Tony's eye
  (Mode 5), not a rule.
American spelling in our sentences; NASA's quoted words as NASA wrote
them. Nothing about which craft did what that the plan did not find.

## 8. The rules it runs under

Read each before the work it governs; open the first report with each
version line read, against the manifest: horizons-orbital-mechanics 1.18
(Which Record Serves a Body; How a Path's Events Are Found, the orbiter
rule; KEYING); gallery-cache-builder 1.19 (A Spacecraft Is Fetched by
Its Plan); interactive-exhibit 1.42 (the spacecraft bullet, the drawer);
gallery-assembler 1.4; orrery-coding-conventions 1.13 (Marker Symbol
Convention); provenance-discipline 2.36; safe-file-editing 1.14;
agentic-pre-test 1.3; ledger-and-session-records 1.23.

Bumps that ride this session (one session, one bump; each by
ledger-and-session-records' four steps in one commit, the protocol's
version entry v3.142):
- horizons-orbital-mechanics: the loiter, as ruled at Part 1, under How
  a Path's Events Are Found, with ESCAPADE as its worked case.
- gallery-cache-builder and interactive-exhibit: only if steps 7 and 10
  change what they say.

## 9. Done when

- Blue and Gold are served and drawn by their plans, each with its Earth
  flyby, its loiter at L2 and its Mars arrival as JPL's positions show
  them, with the approved words.
- Both maintenance runs pass, read from their output; Tier-1 0 on the
  gate path; each new check shown failing once.
- Tony's phone look.

## 10. Records, in the same session

- L-533: what was built, verified against claimed; the correction (one
  Earth flyby each); the loiter rule as ruled. The row under Mars and the
  encounters untouched, waiting for the design round (L-534, L-529).
- Where We Are, by section: stage 15's line, the box, Signals read from
  files; nothing below the run-record marker.
- The report: files changed with their edit counts, the token count,
  Tony's run order, the Tony-action rollup, one question at most.

Written November 18, 2026 with Anthropic's Claude Opus 5.5.
