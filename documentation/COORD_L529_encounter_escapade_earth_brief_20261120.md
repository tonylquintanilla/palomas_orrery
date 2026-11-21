<!-- Doc-Kind: hand | Brief for one Claude Code session (build), in the website: the first encounter (L-529), ESCAPADE's Earth flybys -- a package of JPL's positions and velocities around Earth, a row under Earth, and the whole-visit animation; slice 1 of two. -->
# Brief: the first encounter, ESCAPADE's Earth flybys (L-529), slice 1

Tony Quintanilla, PE | Claude Fable 5.2 (coordinating session) | November 20, 2026, afternoon, Chicago

Built on orrery c442793ac73a7ecd69c2d39aec3dae4b93305a75 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
ae56a94460fb83f703cd0c9665a146f27eade66f at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, both read
live on Nov 20, 2026, 15:27 Chicago. The orrery commit that carries this
brief is Tony's push of it on top of c442793a.

Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`,
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.

Type: BRIEF for ONE Claude Code session, opened through the python_work
door, Opus, high effort (JPL queries and provenance, by
`METHOD_MODEL_EFFORT.md`). The work is in the website. The orrery is
read, and touched only for the records in Part C. Each report ends with
the token count as Claude Code prints it (the protocol's Token Economy).
If the session nears a compaction, it stops at a part's end and says so.

Read first, whole: `documentation/DESIGN_encounters_20261120.md` in the
orrery, today's design record. Then L-529 (guided encounters), L-534
(missions by destination) and L-533 (ESCAPADE) on the ledger. Today's
rulings are in the design record and not yet on the ledger; the
coordinating session's close moves them. Where the record and the
ledger differ, the record is the later word.

## 1. Why, in two sentences

Tony's miss on ESCAPADE's phone look (Nov 18): "The only thing I miss
are the dates of flybys." His design of Nov 20: an encounter is a
completed pass, kept as its own package, opened from the fold of the
body it is centred on, and played with every body moving.

## 2. What this slice is, and is not

IS:
- one package of JPL's positions and velocities around Earth, for
  ESCAPADE-Blue, ESCAPADE-Gold and the Moon, over one window, made by a
  tool run by hand;
- one scene, the whole visit, opening on Earth's Hill sphere, played on
  an even clock with a running date, and each twin's distance and speed;
- one row under Earth that opens it, and the way back;
- the checks that hold all three.

IS NOT (each waits, by Tony's rulings or for slice 2):
- the two close views of the passes, and escape speed beside the speed;
- any new sentence about the mission. Slice 2 brings NASA's "powered
  Earth flybys" through the orrery's words, with Tony's approval;
- the L2 loiter as an encounter; the Mars arrival; any row under Mars;
- an encounter for any other craft; a date picker;
- the Go To rule (Tony's note of Nov 20, its own item);
- a change to the nightly builder's fetches, or to the orrery's code.

## 3. The rulings (design record, sections 2 and 7)

1. An encounter is a completed pass of a craft by a body. Only
   completed ones are built.
2. Its row lives in the fold of the body it is centred on: these
   flybys, under Earth.
3. The twins share one encounter.
4. No date picker: the window is chosen ahead and its data fetched for
   this encounter alone (Tony, Nov 12 and Nov 20).
5. Everything in the scene moves, the Moon included.
6. The body's Hill sphere sets the window and the view the encounter
   opens on. For a craft that loitered at the sphere's edge, the window
   opens at its last crossing inward before its pass. (Tony, Nov 20,
   15:01: "Yes".)
7. Three views, each on an even clock; the visitor moves from one to
   the next when ready (Tony, 15:13: "Three works."). THIS SLICE BUILDS
   THE FIRST, the whole visit, frames about an hour apart, each pass
   marked with its date.
8. The speed is shown (Tony, 15:07: "Yes."). It is JPL's velocity
   around Earth, never worked out by differencing positions.
9. The page already says where the twins are going: each twin's served
   description names Mars and the purpose. "The path ends at Mars. That
   is enough for now." (Tony, 14:46.) The encounter shows that
   description where it shows a twin's words.

Figures the coordinating session gave Tony from memory are listed in
the record's section 7. None is a source. Read every figure from JPL or
from the served files.

## 4. What is already found, at the two SHAs above

THE PLAN'S EVENTS (orrery `data/path_plans.json`; the website's copy on
each twin's entry in `data/objects_config.json`, `path.events`, written
by `tools/mirror_objects.py`). Times UTC, distances from Earth's centre:
- Blue (JPL -9): flyby of Earth, closest 2026-11-07 10:01, 8,033.8 km,
  window 08:44 to 11:17 at one minute.
- Gold (JPL -10): flyby of Earth, closest 2026-11-09 11:00, 7,382.6 km,
  window 09:51 to 12:08 at one minute.
- Each has a loiter at SEMB-L2 before it, ending at its pass, and the
  orrery's plan (not the website's copy) holds `left`: 2026-11-18 for
  Blue, 2026-11-20 for Gold, the day each passed twice the Hill radius
  outbound.

THE WINDOW IS NOT IN THE PLAN. The plan's flyby window is the two and a
half hours that need minute points. The twins were launched inside
Earth's Hill sphere and loitered on its edge for a year, so ruling 6's
crossings have to be read from JPL (Part A).

THE HILL RADIUS IS HELD TWICE. The website serves Earth's Hill sphere
as a shell: `objects[earth].features.hill_sphere`, radius 235 Earth
radii, served in km as 1,500,000 to three figures. The orrery's plan
holds `hill_km`
worked from JPL: 1,483,391 km at Blue's pass, 1,482,669 at Gold's. The
plan's figure is not on the website's copy of the events. RULE FOR THIS
BUILD: the window is read against the sphere the scene draws, the
served shell. Part A reports the plan's crossings beside it.

THE BODIES. Earth is 399; the Moon is 301, served around Earth (`@399`);
both twins are served around the Sun only. The website never changes
centres by subtracting (gallery-assembler; the protocol's The Orrery
and the Assembler), so the twins are asked of JPL around Earth.
Earth-Sun L2 is JPL's 32, SEMB-L2, served around the Sun.

THE BUILDER'S FETCH. `tools/gallery_cache_builder.py`,
`fetch_vectors_range`: positions only, ecliptic, the clock as TDB from
UTC, `cache=HORIZONS_CACHE` (False). It returns no velocities. The
orrery's own fetch reads `vx`, `vy`, `vz` from the same table and takes
the speed as the root of their squares (`palomas_orrery.py`).

THE PAGE. `interactive.html` draws every room at one minute; nothing in
it plays through time. The old gallery's animations and the orrery's
use Plotly's own frames, slider and Play and Pause. Saved Scenes are
the pattern for a row that opens a link: a card in
`gallery/gallery_metadata.json` placed by `drawer_row`, shown in a fold
under its row with an arrow and no Go To, Back returning to the fold
(`gallery/picture_folds.js`, `tools/scene_card.py`; the as-built's
Scenes passage). A Scene opens at the visitor's now; an encounter opens
at its own time. Tony, Nov 9: "A specific time is for the future date
picker and encounters."

THE LIVE ROOMS reach 88 days either side of today, so these flybys
leave them in early February 2027. The package must not depend on
`data/solar-system/` for any position.

THE NIGHT. The website's night commits only its allow-list
(`daily_run.py`, `night_allow_list`) and swaps `data/solar-system/`
whole. A package kept outside that folder is never swapped and never
committed by the night.

## 5. The session, in three parts

Stop after each part with a report, and wait for Tony's go-ahead.

PART A. Measure and prove. Nothing served, nothing committed.
1. THE CROSSINGS. Ask JPL, fresh, for each twin's distance from Earth's
   centre from its launch to today, fine enough to place a crossing to
   the hour. Hold each answer to JPL's own name for the id (L-539's
   lesson). Report every crossing of the served shell's radius, in and
   out, with its date; then, for each twin, its last crossing inward
   before its pass and its first crossing outward after it. Print the
   window ruling 6 gives: Blue's or Gold's last crossing inward,
   whichever is earlier, to the later of the two crossings outward, and
   its length in days. Beside it, the same against the plan's `hill_km`.
2. JPL'S RECORD. Quote what JPL's header for -9 and for -10 says of the
   trajectory's source and date, so "completed" rests on JPL's words.
3. THE PACKAGE'S MOMENTS, proposed: every hour across the window, and
   every minute of each twin's flyby window from the plan. All bodies
   are asked at the same moments, so every frame is a moment JPL was
   asked for and nothing is worked out between points. Ask positions
   and velocities around Earth for Blue, Gold and the Moon. Check the
   answer against the plan: each twin's closest moment and distance in
   the package beside the plan's event, printed.
4. EARTH-SUN L2, proposed, Tony rules: say whether JPL answers for 32
   around Earth, and if it does, include it in the proof picture. It
   sits on the sphere's edge, where the twins loitered.
5. THE DIGITS. A frame's distance and speed are JPL's own at that
   moment, and JPL states no uncertainty for a spacecraft. Read
   provenance-discipline, A Computed Position Prints What Its Errors
   Earn, and propose what each may print, with four printed examples.
   Where the rule does not reach this case, say so; do not pick.
6. ONE MOVING SCENE, headless (`tools/headless/`), the smallest that
   proves the page can play: Earth, its Hill shell drawn from the served
   shell by the renderer Earth's fold uses, the Moon and one twin moving
   through about twenty moments by Plotly's own frames. Report what of
   the shared chrome holds while it plays and what breaks: the frame
   zoom, + and -, turning the view mid-play, the HUD, the text box, the
   count line, the name labels, the view's middle, Back. No plot is
   changed from inside a Plotly event handler (interactive-exhibit).
7. THE SHAPE, proposed in plain words: the address that opens an
   encounter; where its logic lives (its own file, by L-338); whether
   it needs Pyodide at all; what it reuses of the shared chrome by
   parameter; the tool's name and the package's place and layout.
8. REPORT, then STOP: the dates of step 1, the size of the answer of
   step 3, pictures of step 6 at desktop and phone width. ONE question
   for Tony: the window, with its measured dates. L2 is shown, not
   asked, unless JPL refuses it.

PART B. The package, the scene, the row.
9. THE TOOL, in the website's `tools/`, run by Tony from VS Code's Run
   button with no arguments: asks JPL fresh, writes the package under
   `data/encounters/`, and prints what it asked, of which id, around
   which centre, and what came back. The package carries, for each
   body, JPL's id and name, the centre, the span, the steps and the
   moment retrieved; positions in km and velocities in km/s by the
   store's own conversion, named; and each twin's speed, worked once by
   the tool from JPL's three components and stored beside them with a
   line saying so. The page prints what the package holds and computes
   no figure. A second run with nothing changed says so and rewrites
   nothing but the retrieved stamp, or nothing at all: say which.
10. THE SCENE, the whole visit. Opens centred on Earth, framed on the
    Hill sphere by the frame rule (the farthest thing framed plus 10
    percent, across the narrow side). Drawn: Earth; the Hill shell with
    its served words; the Moon and its path over the window; each twin
    and its whole path in the package, the minute points included, so
    a visitor who zooms in on a pass sees a curve and not a corner;
    L2 if ruled in. Each closest pass is marked with its date and time,
    UTC, read from the plan's event, never typed. Played by Plotly's
    own frames on the hourly moments: Play, Pause and a slider a thumb
    can use on a phone held upright; the visitor's zoom and turn are
    kept while it plays. A line under the title carries the frame's
    date and time, and each twin's distance from Earth's centre and
    speed. A tap on a body opens the page's one text box: its name, its
    served description, the frame's figures, and a source line (JPL's
    id and name, "around Earth's centre", the moment retrieved).
11. THE WORDS. Only names, served words, figures and source lines. A
    sentence that describes the drawing itself is allowed ("Each frame
    is one hour."). List every string a visitor reads, for Tony's look.
12. THE ROW. A fold named "Encounters" under Earth's row, by the Scenes
    fold's pattern: one card in `gallery/gallery_metadata.json`, placed
    at Earth, its name "ESCAPADE's Earth flybys", an arrow and no Go
    To; the two dates beside the name, read from the plan's events on
    the twins' entries, never typed in the card. A tap opens the
    encounter; Back returns to the fold; Find finds it by name. Say how
    the Scene cards, Picture folds and Drawer places rows treat the new
    card, and change them so each looks at it.
13. THE CHECKS, each shown failing once on a planted fault, each named
    in the report with what it examined and how many (the protocol's A
    Check That Cannot Fail Is Not Passing):
    - a package row in `gallery_maintenance_run.py`: every body shares
      the moments; no gap in the hours; the minute windows whole; each
      twin's closest pass in the package agrees with the plan's event
      on its entry, moment and distance. That last one is also the
      alarm if the orrery's plan ever moves a completed pass;
    - a headless walk: the row opens the scene; Play moves the twins
      and the Moon and the date; Pause holds; a tap opens the box; Back
      returns to the fold;
    - the hover and typed-facts suites cover the new scene. A checker
      passes on what it does not look at;
    - every new file the browser fetches joins `SERVED_FILES`;
    - `documentation/check_cache_siblings.py` will name
      `data/encounters/` as something the builder did not make. Teach
      it the folder by name; do not silence it (gallery-cache-builder,
      The sibling report names what the builder did not make);
    - `night_allow_list` unchanged, and shown not to hold the package.
14. THE AS-BUILT. A section "Encounters" in `INTERACTIVE_AS_BUILT.md`,
    in the commit that changes the page (L-522).
15. REPORT: files changed with their edit counts; pictures at phone
    and desktop width of the opening, a moment mid-fall, each closest
    pass and the end; the words of step 11. Tony's go-ahead.

PART C. The runs, the records, the push.
16. The website's maintenance run green, read from its output.
17. RECORDS, in the orrery: a note on L-529 (what was built and
    measured, the window as ruled, verified against claimed); a line on
    L-533 pointing at it; Where We Are by section (the box, stage 15's
    line, Signals read from files), nothing below the run-record
    marker. The orrery's maintenance run for the index and the caps.
18. FOR THE COORDINATOR, not built here: each rule this build learned
    that will hold for the next encounter, as plain sentences, sorted
    under interactive-exhibit and gallery-cache-builder. The
    coordinating session writes the skill bumps after the push (the
    lesson of Nov 19).
19. REPORT, with Tony's run order: the tool, if he is to run it again;
    commit and push the website and the orrery, not while a night is
    running (read the newest "Nightly run" commit times in both
    repositories; on Nov 20 they were about 10:10 a.m. and 1:10 p.m.
    Chicago for the orrery, 11:03 a.m. and 2:32 p.m. for the website);
    `gallery_maintenance_run.py --live` after the push. Then his phone
    look, upright, written only for what the scene draws.

## 6. The rules it runs under

Read each before the work it governs; open the first report with each
version line read, against the manifest (protocol v3.143):
interactive-exhibit 1.43; gallery-cache-builder 1.20; gallery-assembler
1.4; gallery-pipeline 1.2 (the card); horizons-orbital-mechanics 1.19
(centres, the clock as UTC, `cache=`, JPL's exact name);
provenance-discipline 2.37; orrery-coding-conventions 1.13 (markers,
hover text); safe-file-editing 1.14; agentic-pre-test 1.3 (the new
tool); ledger-and-session-records 1.23.

One session at a time in the website's folder. The cleanup round's
first session (L-533's last day, L-538) edits the nightly builder
there; it and this one are not run together.

## 7. Done when

- The package is on disk, made by the tool from JPL, every figure in it
  JPL's or worked from JPL's with its line.
- A row under Earth opens the whole visit; it plays on an even clock
  with the Moon and both twins moving; each pass carries its date; the
  date, distances and speeds follow the frame.
- Nothing a visitor reads is typed in the page or the card but names
  and sentences about the drawing.
- Every new check has failed once on a planted fault, by name; the
  website's maintenance run passes, read from its output.
- The night neither swaps nor commits the package.
- Tony's phone look.

## 8. Open, for slice 2's talk

The two close views and how the visitor moves between the three; escape
speed, worked from JPL's figure for Earth's gravity, in the close views
only; NASA's words for the powered flybys, through the orrery; how a
completed encounter is asked again if JPL replaces a twin's predicted
path with its measured one; the loiter's view.

Written November 20, 2026 with Anthropic's Claude Fable 5.2.
