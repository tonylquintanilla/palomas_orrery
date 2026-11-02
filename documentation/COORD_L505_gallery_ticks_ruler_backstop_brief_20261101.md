<!-- Doc-Kind: hand | Brief for the next gallery Claude Code session: tick dots on the three axis lines, the grid chip replaced by a short ruler, Plotly's edge numbers off in every room (the Oct 31 rulings R1 to R4, L-505); the website's backstop line (12:17 UTC, L-485); the pins that move named. Written by the coordinating session; zero code. -->
# Brief: the gallery session (the axis ticks and the ruler, and the backstop line)

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session) | November 1, 2026, 15:40

Written at gallery b6574a0fa374be2faf526d7c5e5b6f8988515652 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main; the website's night commit of Nov 1, 16:11 UTC) and orrery
856922f81dd0c1f68b276e2786affa99eeff051e at
https://github.com/tonylquintanilla/palomas_orrery (branch main; Tony's
push of the orrery session of Nov 1). Both read live with git ls-remote
on Nov 1, 19:00 and 20:45 UTC and cloned at those commits; every line
number below was read from them. YOUR BASE IS HEAD WHEN YOU OPEN THE
SESSION, which will be a nightly commit or several newer on the
gallery (its night commits data under data/ and nothing this brief
touches); read it yourself and anchor everything there.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BRIEF for a build session in the GALLERY repository: item 2 of
the queue in `HANDOFF_coordination_20261101_afternoon.md`, section 3,
built from the design record
`DESIGN_axis_ticks_and_ruler_rulings_20261031.md` (Tony's rulings R1 to
R4 and the method notes of its section 4). The session reads this
file, that record, and `HANDOFF_coordination_20261101_morning.md`
section 2b (the backstop ruling) before anything else. The ledger
items: L-505 (the ticks and the ruler), NEW, opened by this session
at the next free handle (L-504 is the highest at 856922f8; the shared
link's item takes the handle after it); L-485 (a nightly run: the
website's backstop line); L-289 (the frame HUD: the chip's history,
closed as the chip goes). Records go in the ORRERY's documentation
folder per the ledger skill; the gallery folder gets nothing but the
code, as the gallery sessions of Oct 31 and Nov 1 did.

The orrery is READ, never written, from this session. One sentence for
an orrery skill (interactive-exhibit's HUD row, section 5) is written
on L-505 for the next orrery session.

## 0. The base, the skills, the order

- Gallery: HEAD, clean, after Tony's Pull origin (its nightly run
  commits at 08:17 UTC when GitHub is on time, up to seven hours later
  when it is not). Tony's run record for this session,
  `documentation/WHERE_WE_ARE_11-<d>-26_<hhmm>_run_record.md` in the
  ORRERY folder, appears when he copies the page; that one is
  expected. Anything else waiting is not.
- Orrery (the sibling folder): 856922f8 or newer, clean, read only.
- Skills this job fires, each read in full from the orrery folder
  before the work, versions stated in the first report against the
  manifest in the orrery's PROJECT_INSTRUCTIONS.md v3.120:
  safe-file-editing 1.14, interactive-exhibit 1.29 (the HUD row, the
  anatomy table, the headless recipe, Mode 5 phone sequence),
  gallery-cache-builder 1.16 (the Daily Run, A Served Number That
  Changes on Purpose), orrery-coding-conventions 1.12 (the marker
  taxonomy: what a small plain circle may already mean),
  ledger-and-session-records 1.22, agentic-pre-test 1.3. A Code session
  reads the repo's copies, which are the manifest's; the account's
  installed copies are Tony's to refresh and cannot be seen from Code.
- Order of work: section 1 (the backstop line, one line, first and
  smallest); section 2 (the ticks); section 3 (the ruler); section 4
  (the edge numbers off); section 5 (the checks and the pins that
  move); section 6 (the records). A session running out of room stops
  at a section boundary and says so; sections 1 and 2 to 4 are two
  separable builds, but R4 (edge numbers off) is built only in the
  same push as sections 2 and 3, because the record's own rule is
  that no room is left with a grid and no scale.
- The session asks Tony ONE question in all, and this brief leaves
  none open; sizes, weights and the halo are Mode 5, settled from the
  URL knobs in section 2.4 on Tony's phone, not asked in chat.

## 1. The backstop line (L-485; Tony's ruling of Nov 1, 12:04 Chicago)

- The fact and the ruling are in the morning addendum's section 2b and
  in the orrery's `.github/workflows/nightly.yml` at 856922f8, which
  the orrery session of Nov 1 built: both schedules keep their times
  and each gains a second scheduled line, so a night GitHub drops is
  caught the same day. Observed lateness: Oct 31 the orrery 6 h 22
  min; Nov 1 the orrery 7 h 0 min and the website 6 h 58 min (run 3,
  15:15 UTC).
- The build, in the gallery's `.github/workflows/nightly.yml`: under
  `schedule:` (line 43 on), after `- cron: '17 8 * * *'` (line 51), a
  second line `- cron: '17 12 * * *'`, with a comment in the file's own
  voice naming L-485 and the ruling (Nov 1, 12:04), quoting GitHub's
  two sentences on delayed and dropped schedules ONCE, read from
  GitHub's page by the session and dated (the orrery's file at
  856922f8 carries the same two sentences in its own comment; mirror
  its wording so the two files say the same thing), and saying why a
  second firing is harmless: the concurrency group `nightly-run`
  (lines 64 to 65) queues it behind a run still going, and a clean
  second run commits only its record. The header comment gains one
  "Updated November <d>, 2026" sentence. The file must still load as
  valid workflow YAML (a YAML load, as the orrery session did).
- The website's dashboard line reads the record, not the schedule:
  nothing else changes.

## 2. The ticks: dots on the three axis lines, every room (R1, R2)

**2.1 What exists, read at b6574a0.** Every room (Sun, Earth, Solar
System; `body.sun-exhibit`) draws three axis LINES through the origin
as scatter3d traces: `sunOriginAxisPoints` (interactive.html line
4468), `sunOriginAxesInstall` (4489; added once after the drawer is
built and the arrival extent measured, so the drawer has no row for
them and they cannot widen the opening view; `hoverinfo: "skip"`,
`showlegend: false`, `name: "axis x"` and so on, width 6, colours
`SUN_AXIS_COLORS` at 4438), and `sunOriginAxesUpdate` (4516; restyled
to the current half-range at the end of every frame change, from
`sunHudUpdate` at 4667). `SUN_ORIGIN_AXES` (4460) reads `?axes=full|pos|off`
from the address. The grid step is `sunGridDtick` (3547: the span
over six, snapped to 1, 2, 5, 10 times a power of ten), written into
all three axes' `dtick` at every frame change (3564 to 3566, 3676 to
3678, 3696 to 3698, 5315 to 5318, 5825 to 5827) and read back by
`sunGridChipUpdate` (4537). The Explorer page (`buildLayout`, 2076, no
`.sun-exhibit` class) has none of this: no HUD, no origin axes; see
section 4.

**2.2 The build.** One new trace per axis, installed beside the axis
lines in `sunOriginAxesInstall` and restyled beside them in
`sunOriginAxesUpdate`: `type: "scatter3d", mode: "markers"`, the
points at every multiple of the grid step d from -r to r along that
axis (the same `d` the layout's `dtick` holds; read it, do not
recompute it another way, or the dots and the grid lines part on a
zoom), `marker.size` an array: the small size at an odd multiple of d,
the large size at an even multiple (R2: the major at every second
step, twice the minor; 0 gets no dot, or the small one, Mode 5),
`marker.color` the axis's hue, `marker.symbol` a plain circle,
`hoverinfo: "skip"`, `showlegend: false`, no legendgroup, `name:
"ticks x"` and so on. A marker faces the screen at a fixed pixel size,
so it never foreshortens edge-on and never shrinks with zoom (Gemini's
note, ruled 20:20): that is why the ticks are dots and not line
segments. `?axes=off` turns the ticks off with the lines.

**2.3 The sizes, against the bodies.** The renderers draw bodies as
markers too (`gallery/feature_renderers.js`; the fixed sizes there read
8 and 11, most are computed), and Earth's blue marker sits on the blue
axis. Read the marker taxonomy in orrery-coding-conventions first, and
the sizes the renderers and `solar_system_drawer.js` give bodies, and
keep the tick dots well below them: the brief's starting values are 3
px minor and 6 px major, Mode 5 decides. A tick dot must not read as a
body at any zoom, and the low camera angle (the scene seen along the
plane of the orbits, the view for comparing tilts) goes on the Mode 5
list, as the record says.

**2.4 The Mode 5 knobs, the house pattern.** As `?edge=N` and
`?axes=` already do (4446, 4460), read once at script evaluation:
`?tick=<minor>,<major>` for the two dot sizes in pixels, and
`?ruler=<width>` for the ruler's line length (section 3). Defaults in
the code are the brief's starting values; Tony's phone settles them
and a follow-up edit writes the settled numbers in as the defaults,
with the knobs left in place. The session prints the knob syntax in
its report, with two or three addresses to try.

## 3. The ruler: the grid chip replaced, every room (R3)

**3.1 What exists.** `#sun-grid-chip` (markup at 1501, styles at 688
to 717: a grey pill, `background: rgba(17,24,39,0.94)`, a border,
`cursor: pointer`) is filled by `sunGridChipUpdate` (4537) with
`grid <b>0.5 AU</b>`, from the x axis's `dtick`; below a thousandth of
an AU it adds the kilometres in brackets (Earth's arrival grid is 2e-5
AU). It sets `sunGridLabel`, which the AU note reads ("Here the grid
lines are 0.5 AU apart.", `sunAuNoteFill` 4562), and a tap on the chip
opens that note (`sunAuNoteShow`). The site credit (palomasorrery.com)
is placed just under the chip, measured from the chip's box (3853 to
3878). The HUD is a row across the bottom, the triad in its centre and
the chip at its right end (L-502; CSS at 659 to 692).

**3.2 The build.** The chip's element stays, with its id, its tap and
its place, and its CONTENT becomes a short inline SVG ruler: a short
horizontal line in neutral white (the key stands for all three axes),
the 0 end unmarked, a small dot at one step and a larger dot at two
steps, THE SAME SYMBOLS AND SIZES as the axes' dots (R3 refined 20:22:
"shouldn't the ruler use the same style"), and two labels under or
beside the dots: the one-step and two-step values with the unit on
both, as Tony wrote them ("0.5 AU", "1 AU"; "0.2 AU", "0.4 AU"; "50
AU", "100 AU"), the phone may shorten the minor's if it crowds. The
values are `d` and `2d` from the same `dtick` the ticks read, printed
by the same digit rule `sunGridChipUpdate` uses today (the decimals
from the step's magnitude), so the ruler's numbers and the dots'
spacing cannot disagree; the ruler re-labels on every frame change as
the chip does now. The ruler is a KEY to the dots on the axes, not a
screen length; its line length is `?ruler=` (2.4), starting value 56
px. THE UNIT FOLLOWS THE ROOM: the ruler prints what the chip prints
today in that room, AU everywhere and the kilometres in brackets below
a thousandth of an AU; how two labels with kilometres fit at Earth's
arrival grid is Mode 5, and the AU note's sentence keeps printing the
full form.
- The background goes transparent (Tony, 17:50: "so it does not
  obscure the website url"): the pill's background and border go; the
  labels get a thin dark halo (text-shadow) so they stay readable over
  the corona and the belt's cloud (Gemini's note). The site credit's
  placement still measures from the chip's box, so re-measure after
  the change and keep the credit clear below it; the Explorer's own
  placement (3853 on) is untouched.
- `sunGridLabel` keeps its full text ("0.5 AU") so the AU note's
  sentence is unchanged; the headless walk reads it (section 5).
- The AU note gains nothing; the FRAME NOTE (#sun-frame-note, 1507 to
  1521) gains one sentence saying what the dots on the axes and the
  ruler are ("The dots on the three axis lines mark the grid: a small
  dot at every grid step, a larger one at every second step. The
  ruler at the right shows those two steps with their values."), page
  words with no number typed; its Source line is unchanged.

## 4. Plotly's edge numbers off, in the rooms (R4)

- In `buildSunLayout` (3915 on) the `axisTemplate` gains
  `showticklabels: false`; `ticksuffix`, `tickfont`, `exponentformat`
  and the per-axis `showline` stay (the coloured box edge is the
  axis's own line and is not a number). Grid lines stay (`showgrid:
  true`). That is one template for all three axes, so every room loses
  the numbers in the same build that gives every room the dots and the
  ruler.
- The phone resize handler's `tickfont` relayout (6413 to 6418) and
  `axisTickFont` (4052) then set a font no number uses in the rooms;
  the Explorer still uses `axisTickFont` through `buildLayout` (2086),
  so the function stays; the relayout lines in `onSunResize` are
  removed or kept with a one-line comment, the session's call.
- THE EXPLORER KEEPS ITS NUMBERS. R1 says every scene; the record's
  section 4 makes whether the Explorer draws the same frame a fact to
  read. Read at b6574a0: it does not. `body:not(.sun-exhibit)
  .sun-chrome { display: none; }` (658) hides the HUD there, and
  `sunOriginAxesInstall` is called only from the exhibit boot (4347),
  so the Explorer has no axis lines to carry dots and no chip to
  become a ruler. R4's own clause, "no room is left with a grid and no
  scale", therefore keeps Plotly's numbers on the Explorer, which
  `buildLayout` (2076) sets separately; nothing there changes. The
  report says so in one line, and L-505 records it; if Tony wants the
  Explorer to match, that is a build of its own with its own frame.

## 5. The checks, and the pins that move (L-484's lesson)

By gallery-cache-builder 1.16's rule, the pins that this build moves
are named here, before the build, and the session greps for the rest:
- `tools/headless/walk_solar_system_drawer.js` lines 656 to 663 read
  the chip's `textContent` with `/^grid\s*/` stripped and expect the AU
  note to say "Here the grid lines are <that> apart.": with the ruler
  the chip's text is no longer "grid 0.5 AU". The walk reads the
  spacing from `sunGridLabel` (or a `data-spacing` attribute the ruler
  sets), by the same rule as before; the walk is run after the build
  (the headless recipe, interactive-exhibit 1.29) and read to its end.
- The five checks the record names must not see the tick traces as
  features: `smoke_drawer_order.js`, `smoke_hover_budget.js`,
  `smoke_label_words.js`, `smoke_drawn_ends.js` and
  `tools/sweep_collapsed_features.py`. Read at b6574a0, none of them
  reads the live page's traces; they read the renderers' output and the
  served cache, and the axis lines are already invisible to them for
  that reason. The tick traces are installed the same way (after the
  drawer, no legendgroup, hover skipped), so the expectation is that
  the whole maintenance run is green with no edit to a check; the
  session proves it by running it (36 of 36 at b6574a0, or the count
  the run prints) rather than by this reading.
- `smoke_typed_numbers.js` and `smoke_typed_facts.js` read the served
  words, not the page's HTML; the frame note's new sentence types no
  number anyway.
- The orrery's interactive-exhibit 1.29 anatomy row for the frame HUD
  (SKILL.md line 128) and its grid-chip sentences become wrong with
  this build: written on L-505 for the next orrery session, which
  bumps the skill; not edited from the gallery.
- `gallery_studio.py` does not read the chip (grepped). Grep the
  gallery again at HEAD for `sun-grid-chip`, `grid chip` and `axis x`
  before the push, and name every hit in the report.

The proof: the offline maintenance run green, read from its output;
the headless walk green with its moved pin; the Daily Run unchanged.
Then Tony's push (GitHub Pages deploys the code on push; the nightly
run is not needed for it), and his phone: all three rooms, the dots on
the axes at two sizes, the ruler with two labels and no pill, no
numbers on the box edges, the AU note opening from the ruler, the
frame note's new sentence; then the Mode 5 pass with the knobs.

## 6. Records

- L-505 (the ticks and the ruler), opened: R1 to R4 by handle to the
  design record; what was built, by file and function; the Explorer
  kept as it is and why; the Mode 5 knobs and Tony's settled values
  when they come; the pin moved in the headless walk; the sentence for
  interactive-exhibit's next version (the HUD row: a ruler, not a
  chip; the dots on the axes; the edge numbers off in the rooms).
- L-485 (a nightly run): the website's backstop line built, with the
  ruling and the observed lateness; both repositories now have two
  times.
- L-289 (the frame HUD): the chip replaced by the ruler, one entry,
  and its gap closed.
- Where We Are: the box (Changed: the dots and the ruler, the edge
  numbers off, the website's second time; Do next: the push and the
  phone look with the knobs; Needs you now: the morning routine,
  unchanged), the road's 11b line (both backstops built), the marker
  and the zone below it untouched, the page's 130-line cap above the
  marker kept, the ledger's index rebuilt.
- The final report per the gallery's CLAUDE.md: the skills read with
  their version lines; files changed with edit counts; the knob
  addresses to try; Tony's run order; the rollup. ASCII, LF, the
  encoding gate on every file changed.

## 7. Tony's run order after the session (for Code to print, and for Tony)

1. Paste Code's final report to the coordinating session; wait for its
   word.
2. GitHub Desktop, website: Pull origin first if it shows a number (the
   night may have committed); then commit and push, everything in the
   change list together. Then the orrery: commit and push the records
   and your run record.
3. Your phone, after closing the saved tab, in each of the three rooms:
   the dots on the three axis lines, the ruler at the bottom right with
   two labels and no grey pill, no numbers on the box edges, a tap on
   the ruler opening the AU note, the triad opening the frame note with
   its new sentence. Then the knob addresses from the report, and your
   word on sizes, the ruler's length and the halo (Mode 5).
4. The next morning: the website's Actions tab shows a run at 08:17 UTC
   or a late one, or one at 12:17 if GitHub dropped the night; clean;
   its commit, if any, touches data only. Pull origin on both.
5. Send the gallery's and the orrery's SHAs to the coordinating
   session, with your Mode 5 word.

## 8. Tony-action rollup

- (do) Open a Claude Code session on the gallery repository (the
  python_work door: the prompt names the gallery) and paste the short
  prompt the coordinating session gives you; it points here.
- (do) Afterwards, the run order in section 7; the Mode 5 pass is the
  part only you can do.
- (decide) Nothing before the session. After it, your phone's word on
  the sizes, the ruler's length and the halo.

Written November 1, 2026 with Anthropic's Claude Fable 5.1.
