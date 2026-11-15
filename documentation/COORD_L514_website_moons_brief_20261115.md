<!-- Doc-Kind: hand | The brief for one Claude Code session through the python_work door: L-514 (the Mars room), session 2, the website's half: Phobos and Deimos served around Mars, Mars a centre opening on its symbol alone. Communication; written once, read by its session. -->
# Brief: Phobos and Deimos on the website (L-514, session 2 of 2)

Built on orrery f5598c91657bf0ee9c02c685f4b0bc35fc5363d7 at
https://github.com/tonylquintanilla/palomas_orrery
and gallery d3e97b1503d878a6fac0be4fe9131186b893d365 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io
(both branch main, read 2026-11-15, 12:05 Chicago; both of Tony's
folders matched them). Nightly bot commits since are expected. This
brief is in the orrery's documentation/ on Tony's computer, not yet
pushed.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD, a Claude Code session on Tony's computer, through the
python_work door, in the GALLERY (website) folder; records in the
orrery's. Written November 15, 2026 with Anthropic's Claude Opus 5.5,
the coordinating session.

## What this is, in one paragraph

Session 1 (orrery 488cad20 to 49c0c14, Nov 14-15) keyed Phobos and
Deimos in the orrery: JPL's names, NASA's sentences, periods around
Mars (0.31914 and 1.2625 days), and one accuracy row,
`MAR099_PHOBOS_DEIMOS_POSITION_PLACE_KM` = 10.0 km (Brozovic, Jacobson
& Park 2025, AJ 170:42, Section 6). The objects export now holds both
(100 objects). The website has no entry for either moon, so nothing of
them reaches a visitor yet. This session serves them around Mars and
gives Mars the opening Tony ruled. Most of the page is already built:
step 2b of L-515 (one nested tree) made the moon's box pattern
(`SolarSystemFigures.childBox`), Go To on a moon opening the moon's own
box (ruling 4), the fixed row in every centre, and Centre on for any
body something is fetched around (`centresOf`). So the expected work is
data and checks, not page code. If the page does need code, say why in
the report before writing it.

## The rulings this build carries (L-514, all standing)

- Ruling 1 (Nov 6) and step 2b's ruling 16: Mars opens on its symbol
  alone; both moons off by default ("like the moon in the earth room").
- Ruling 2 and step 2b's ruling 14: Mars's fold lists Phobos, then
  Deimos, nearest first (shells join at the build-out).
- Ruling 3 and ruling 5 (Nov 14): each moon's box is the Moon's
  pattern, with NASA's sentence, its distance from Mars by the larger of
  the drift and JPL's accuracy, and its period in days.
- Ruling 4 (Nov 6, "B"): Go To on a moon opens the moon's own box. Built
  in 2b; check it holds for both moons.
- Step 2b's ruling 15: Centre on Mars puts Mars in the middle.
- The tap: L-523 (taps sent as hovers, closed Nov 12) made the 22-px
  reach site-wide. NOT in this build. What stays is ruling 4's risk:
  a tap near Mars must pick the moon meant, not Mars. Measure it.

## The work

Part 1, the two entries and their words:
- Two objects in `data/objects_config.json`, `phobos` (401) and
  `deimos` (402), in Io's shape: `category` moon, `availability`
  analytic, `parent` mars, `canonical_center` "@499", `center_slug`
  mars, `canonical_frame` parent-relative, `trace_policy` none. Find how
  an object entry is added today (Only two tools write the served
  config; the Tree parents check holds `parent` to `center_slug`) and
  say which way you use before using it.
- `gallery_maintenance_run.py --pull` at the orrery's HEAD: the objects
  mirror writes each moon's name, description (NASA's sentence),
  info_url and period around Mars; report what it wrote, and anything
  else that moved.
- A `position_accuracy` pointer on each moon to
  `constants_new.py::MAR099_PHOBOS_DEIMOS_POSITION_PLACE_KM`, written as
  the Moon's was (L-513), its value null; then
  `tools/mirror_constants.py --write` fills value, units and citation.
- Mars's opening by `store_writer.add_arrival`, as Jupiter's and
  Saturn's were: the symbol alone, both moons off.
- Report, and stop for Tony's go-ahead.

Part 2, served around Mars:
- The cache builder for the two new bodies, by gallery-cache-builder
  (A config change is not deployed until the cache is rebuilt): the
  coverage index lists both, fetched around '@499', each with its trust
  window; Cache in step goes green after the build, not before.
- The gallery run (`gallery_maintenance_run.py`), read for its own line,
  with Store drift reading MATCH for both new pointers by name, and the
  Solar System figures check no longer listing Phobos or Deimos as
  unkeyed (Io, Titan, Pluto and Charon stay listed).
- The headless walk (tools/headless): Mars's fold opens on the symbol
  alone; Centre on Mars; tick Phobos, Go To Phobos opens Phobos's box,
  its distance in tens of kilometres ("9,380 km"-like) with the
  sentence naming JPL's published accuracy; the same for Deimos.
- The tap near Mars, measured: in Mars's centred view, and in the
  root's view, how far on screen Phobos's marker sits from Mars's, and
  which a tap at Phobos picks. Name the views where the 22-px reach
  covers both, and what is picked there.
- Report, and stop.

Part 3, the records: L-514 (the Mars room), Where We Are by section,
the gallery's `INTERACTIVE_AS_BUILT.md` if the page changed, the final
report as CLAUDE.md asks, with the token count, and the phone look's
steps for Tony (upright): Mars's fold; Centre on Mars; tick each moon;
Go To each moon; tap each moon in the picture; Reset.

Out of scope, recorded, not chased: Mars's shells, axis, equator and
terminator (the build-out); Io, Titan, Pluto and Charon's keys (L-515's
leftover 1); ESCAPADE (L-533); guided encounters (L-529). An
interactive-exhibit bump only if a rule changes; the skill is at its cap
(L-522), so old lines move out first.

## Skills this fires

Read each and compare its version line with the manifest:
interactive-exhibit (1.42), gallery-cache-builder (1.19),
gallery-assembler (1.4; a test is handed to Tony), provenance-discipline
(2.36), safe-file-editing (1.14), and ledger-and-session-records (1.23)
for the close.

## Start

1. Record the base in both folders (`git rev-parse HEAD`, `git
   ls-remote origin HEAD`, `git status`); stop if they disagree.
2. Read the skills above; name each with its version line.
3. Say Part 1 in one sentence and wait for Tony's go-ahead.

Plain speech, one question per message. Commit and push are Tony's.

Brief written November 15, 2026 with Anthropic's Claude Opus 5.5.
