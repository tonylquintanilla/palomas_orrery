<!-- Doc-Kind: hand | Session close of Oct 25, 2026: build B of slice 2 cut after the spacecraft (L-443) -- the orbiter rule, the twelve keyed and served, drawn solid then dashed; L-461 built; four skill bumps; the comets left for the next session. -->
# Session close: the spacecraft in the Solar System room (build B, part 1)

Tony Quintanilla, PE | Claude Opus 5.5 | October 25, 2026

Built on orrery 0c27f47ad631efbfc611a80404095649025687d6 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery b1a4ce6c7fc72b17571a13e18ab11df98b86485b at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main), both read with git ls-remote at the session's start.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD. Started from `HANDOFF_L443_slice2_buildB_brief_20261024.md`
with `COORD_L443_drawer_groups_ruling_20261024.md` and
`COORD_L461_stop_ruling_20261025.md`, which answered the brief's three
questions. Cut after the spacecraft and before the comets, as Tony's
opening message allowed. Supersedes nothing; the comets' part of build B
starts from section 6 here.

## 1. What came out of it

- **The orbiter rule, in the path plan** (orrery patch_L443_12). A
  spacecraft that enters a planet's gravity region and loops keeps two
  events, its arrival and its departure; the loops between are dropped.
  One that never leaves keeps its arrival. Passes of the Sun stay.
  Every event now says which kind it is. Juno's 113 events should fall
  to about 4, Europa Clipper's 87 to about 5.
- **OSIRIS-APEX's Earth pass of 2029-04-13 checked.** NASA: the route to
  Apophis takes "six close Sun passes" and "three gravity assists from
  Earth". The plan has six Sun passes near 0.5 AU and three Earth passes
  after the sample drop (Sept 2025, March 2027, April 13 2029). JPL's
  data sheet lists no dates; nothing contradicts them.
- **The twelve spacecraft keyed** (orrery patch_L443_13), with JPL's
  names and your approved words. The preview flag, its list and its
  button are gone; a permanent "Path Plan -- every path, now" button
  replaces the button. The patch carries your preview's plans across,
  so no second half-hour run.
- **The spacecraft in the Solar System room** (gallery patch_L443_15).
  A Spacecraft group right after Earth's row, the twelve in launch
  order. Each path drawn solid where it has flown and dashed where JPL
  predicts it will go: JPL's own word, as you ruled (Juno's data sheet
  calls its future part "a planning prediction"). Text box in your words. Go To fits a whole path.
- **The builder fetches each path by its plan**: JPL's whole span, a
  point every 7 days thinned where it runs straight, finer steps around
  each event, and a daily tail around today. Fetched whole again when
  the orrery makes a new plan (every 30 days).
- **L-461 built.** When the orrery the Daily Run pulled is not the newest
  commit in your orrery folder, the run stops before the builder and
  says what to do.
- **Four skills bumped**: horizons-orbital-mechanics 1.11,
  gallery-cache-builder 1.12, interactive-exhibit 1.24,
  safe-file-editing 1.14 (protocol v3.112).

## 2. Your run order

On the orrery, in VS Code, each with the Run button:

1. `patch_L443_12_orbiter_rule_20261025.py` (delivered first), then
   `test_path_plan.py`: "23 of 23 checks passed". Then the dashboard's
   "Path Plan -- preview of slice 2" (about half an hour); paste its
   output into the chat.
2. Close the dashboard. `patch_L443_13_keys_20261025.py`. It prints an
   "ok" line per file, then a line saying it carried twelve plans and
   removed the preview's file, then "patch applied".
3. `patch_L443_14_session_close_20261025.py`, these records and the four
   skill bumps. Same shape.
4. `orrery_maintenance_run.py`. New today: the Horizons check asks JPL
   about the twelve spacecraft (they are new), so it needs the
   internet; the Path plan row says twelve paths and "Asked JPL for:
   nothing".
5. Move the three patches into `documentation\`.
6. GitHub Desktop: commit everything and push. The commit also carries
   `COORD_L461_stop_ruling_20261025.md`, already in your folder, and
   the removal of `data/path_plans_preview.json`.
7. Settings > Skills: reinstall horizons-orbital-mechanics (1.11),
   gallery-cache-builder (1.12), interactive-exhibit (1.24) and
   safe-file-editing (1.14).

On the website, in VS Code:

8. `patch_L443_15_spacecraft_room_20261025.py`. One "ok" line per file,
   then "patch applied". Move it into `documentation\`.
9. The dashboard's **Daily Run** (not the maintenance run alone). Its new
   line after the pulls should read "Pull matches push: the orrery
   pulled is <code>, the newest commit in your orrery folder." Its build
   fetches the twelve paths for the first time: a few minutes more than
   usual. The maintenance run at its end checks them.
10. GitHub Desktop: commit and push; then the live maintenance run.
11. **Phone look**, the Solar System room: open the Spacecraft group;
    tick Voyager 1, Juno and Parker Solar Probe one at a time; for each,
    is the path solid behind and dashed ahead, and does its text box
    read right? Go To on Voyager 1: does the view hold its whole path?
    Then Reset.

## 3. What was checked, and how

- **The orbiter rule**: the path plan's suite, 23 of 23, with two
  made-up orbiters around Mars (one leaves, one stays), each giving
  exactly its arrival (and departure) to the minute; a planted fault
  keeping every loop fails.
- **Patch 13's carrying step**: tested on a preview made by the new rule
  (all twelve carried, the preview's file removed, the maintenance
  run's Path plan row then asking JPL nothing) and on your current
  preview, made by the old rule (none carried, each named, the button
  named as the fix).
- **The orrery's maintenance run**, keyed copy against the untouched
  repo: every row the same except the two that need JPL for the new
  entries (the Horizons check and its confirmations), which your run
  settles. The push gate holds: 0 Tier-1 on the gate path with the
  twelve keyed; the whole tree 276, as before.
- **The website, simulated end to end here** (fake straight-line paths,
  since this sandbox cannot reach JPL): the orrery's export pulled into
  a copy, the mirror writing each plan, the builder fetching by them,
  the room's driver drawing all twelve with no warnings. The builder's
  suite 434 of 434 on both configs, with nine new checks; the drawer
  walk 121 of 121, with a spacecraft section, shown failing on a
  predicted part drawn solid; the figures check's new part 7; the Sun
  and Earth rooms identical before and after (every row, both
  buttons), and both Reset walks 33 of 33. The website's offline run:
  every gating row passes on the simulation but the Horizons
  confirmations (the twelve have not met JPL yet, as on your machine
  before step 4) and the Artifact 1 pin, which passes on the real
  cache.
- **L-461**: five made-up cases and two planted faults, run by the
  existing "Daily run steps" check; and it reads this sandbox's clone
  of the orrery as 0c27f47.
- **Each patch**: applied to a clean copy in run order and refusing a
  second run; your folders' copies of every file it edits match GitHub.
- **Not seen yet**: real paths (the simulation's are straight), the
  sizes the real build serves, and anything on the phone.

## 4. Decided by method, and what is yours

Decided by the skills' method, and written into them:
- **Each event window is thinned at its own scale.** The first simulated
  build served about 1.7 MB of positions, nearly all from passes of the
  Sun: the encounter rule gives a pass at 0.3 AU a window of about 50
  days either side at 6-hour steps. A point is now kept only where the
  path bends away by more than 1% of the passing distance. 68 KB on the
  straight test paths; the real build measures the real size.
- **The marker is worked out between served points**, on the curve
  through the three nearest, and the distance prints to the place that
  working-out earns. Near today the builder serves a point a day.
- **A row the cache does not hold yet is named, not fatal.** Until now
  one missing body would have stopped the whole room.
- **The orrery's colours** for the twelve; Voyager 1 changes from the
  website's own coral to the orrery's white.
- **Labels** where the orrery's name is shorthand: OSIRIS-APEX, Parker
  Solar Probe, Solar Orbiter, Psyche spacecraft (the asteroid keeps
  "Psyche"), Europa Clipper.
- **The test suite gives a spacecraft with no plan a stand-in plan**, as
  it does stand-in drawings, so it never depends on a pull.

Yours, at the next design talk:
1. The comets' visitor words, "hyperbolic" in plain words among them,
   and the three groups' words (Comets, Hyperbolic comets, Interstellar
   objects).
2. With the class check's list in hand: whether a group gathering
   several JPL classes (Near-Earth asteroids: Atira, Aten, Apollo, Amor)
   stays one row.

## 5. Settled lines this close took off Where We Are

Kept here word for word, to keep the page under its line cap:
- "Groups fold open in the drawer; a room is for a body with more than
  its symbol. Every body fetched every build. Every comet drawn from
  today's orbit. Open-path comets go with the spacecraft. (Oct 22)"
- "Paths: one rule, planned in the orrery; nearest approaches place the
  fine steps; solid to today, dashed after. (Oct 23)"
- "An orbiter: its arrival and departure are flybys; between, it rides
  with its planet, the loops left for the planet's room. (Oct 24)"

## 6. The next session: the comets (build B, part 2)

Read this, the brief's sections 2.5 and 4, and the drawer-groups note.
- Added the same evening, after Tony's runs: two fixes followed (orrery
  patch_L443_16, the Horizons check reading JPL's empty answer for a
  spacecraft; gallery patch_L443_17, the builder stopping at JPL's last
  minute, so the Voyagers are fetched; Voyager 1 goldenrod). Their
  record is on L-443. Confirm from Tony's run record that both ran, the
  Horizons check confirmed the twelve, and both Voyagers drew.
- Added later that night: a spacecraft ticks its companions (its flyby
  planets and the farthest it reaches) and the i panel reads one
  sentence to a bullet (orrery patch_L443_18, gallery patch_L443_19;
  interactive-exhibit 1.25, protocol v3.113). Confirm the loaded
  interactive-exhibit reads 1.25, and Tony's phone look, before the
  comets. The heliopause beside the Voyagers is L-488, for a design talk.
- Confirm the loaded skills read horizons-orbital-mechanics 1.11,
  gallery-cache-builder 1.12, interactive-exhibit 1.24 and
  safe-file-editing 1.14 before work that fires them.
- Read Tony's run record of today's runs; check the real build's sizes
  and the phone look before building on them.
- The comets: path_plan plans each open-path comet (the span ruling: a
  year before perihelion to a year past today, clipped to JPL; the
  perihelion its event); the fourteen keyed with their website entries
  and words; the drawer's three groups after the Sun by JPL's class
  (Comets with piece C; Hyperbolic comets, ten; Interstellar objects,
  three); the room drawing each comet's path solid then dashed,
  "predicted" in its words; the words to Tony first.
- The class check: every existing drawer group against each body's SBDB
  class, any mismatch named; Tony decides on a group that gathers
  several classes.
- Still open beside it: L-484's check (design, then build), L-476 (the
  orrery reads its dates from the plan), L-465 (the Sun axis hover's
  words).

## 7. Permanent, and temporary

Permanent: the orbiter rule and its suite checks; the twelve keys and
their words; the export's no-period rule for a spacecraft; the "Path
Plan -- every path, now" button; the builder's fetch by plan, its window
thinning, its shrink-gate exemption, its 1,000 AU bound; the room's
spacecraft drawing, text box and source line; the figures check's part
7 and the walk's section 20; the Daily Run's pull-match stop and its
fixtures; the four skill versions. Temporary: none. The one-time step in
patch 13 that carries the preview's plans runs once.

## 8. Tony-action rollup

- **(do)** The run order of section 2, steps 1 to 11.
- **(do)** Paste the preview's output (step 1) into the chat.
- **(decide)** At the next design talk: the comets' words and the groups'
  words; whether Near-Earth asteroids splits by JPL class.

Written October 25, 2026 with Anthropic's Claude Opus 5.5.
