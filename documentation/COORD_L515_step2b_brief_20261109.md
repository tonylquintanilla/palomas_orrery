<!-- Doc-Kind: hand | The brief for one Claude Code session on the website: L-515 (one nested tree), step 2b. Communication; written once, read by its session. -->
# Brief: one nested tree, step 2b (website)

Built on orrery a3e86c88a2c71dcd1d5a41a16b1f1c5f2e3bfabb at
https://github.com/tonylquintanilla/palomas_orrery
and gallery cea21af180b98a6694cb6bfb1083eca38e9b5c5d at
https://github.com/tonylquintanilla/tonyquintanilla.github.io
(both branch main, read 2026-11-09, 22:06 Chicago). The rulings this
brief cites (L-515 rulings 13 to 20) are on L-515 in Tony's next orrery
push, with this brief; the session reads them there. Nightly bot commits
since are expected.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD, a Claude Code session in the gallery repository, through the
python_work door. Written November 9, 2026, night, with Anthropic's Claude
Opus 5.5, the coordinating session, after Tony's rulings of 22:27 to
23:12 Chicago.

## What 2b is, in one paragraph

The Solar System room becomes the ONE picture and the ONE drawer (ruling
14). Each planet's row folds open to its shells and its moons together,
by distance; the moons are drawn at their planet's place by ADDING the
planet's worked-out position to the moon's own JPL elements around it.
"Centre on <body>" no longer opens another page: it moves the view so
the body sits in the middle (ruling 15, picture A), opens the body's own
served opening (ruling 16), draws the axis lines through it (ruling 17),
and the line at the top of the drawer becomes a path down the tree
(ruling 20). The Earth room folds into the root as the Sun room did; only
the Earth System door and the stars stay rooms of their own.

## Start

1. Record both bases; say whether either moved past the anchor.
2. Read the orrery's `documentation/WHERE_WE_ARE.md` and L-515 (one
   nested tree) in `LEDGER_CONSOLIDATED.md`: rulings 1 to 20, in full,
   and the method notes under step 2b's talk. Then L-514 (the Mars room),
   rulings 1 to 4 and its note received on Nov 9.
3. Skills, each against the manifest, by its read plan: interactive-exhibit
   (1.39, in full: this session changes its drawer, Centre on, framing and
   trail rules); gallery-assembler (1.3, in full: the assembler changes);
   gallery-cache-builder (1.18, the parts on objects_config, the arrival
   block, and "a config change is not deployed until the cache is
   rebuilt"); orrery-coding-conventions (1.13, the barycenter rule and the
   marker symbols); safe-file-editing (1.14); ledger-and-session-records
   (1.22). A loaded copy that disagrees with the manifest: stop and say so.
4. Ask Tony ONE thing before building: this session changes
   interactive-exhibit's rules AND gallery-assembler's (its "No
   composition between frames" section, below). May it edit both skills'
   SKILL.md in the orrery, run `skills_index.py`, and add one protocol
   version entry, one bump each, in one commit (the records skill's
   binding rule)? If no, the changes are carried on L-515.

## The job, in four parts, with a stop and a report after each

**Part 1: the moons in the root (rulings 13, 8, 18).**
- Compose a child into the root: its position and its orbit are its own
  JPL elements around its parent PLUS the parent's position worked out
  for the same minute. Today `resolver.py` raises FrameRejectionError for
  an object stored around another centre; where the composition lives
  (resolver, driver or a new module) is method -- say which and why.
  Adding to a child's own answer is not the retired subtraction of two
  JPL answers; gallery-assembler's "No composition between frames" is
  amended to say which is which, in its bump.
- The moons served at the anchor: the Moon (earth), Io (jupiter), Titan
  (saturn), Pluto and Charon (pluto_barycenter). Each gets a row folded
  under its parent's row, behind an arrow, closed on opening (ruling 13).
  A body row that heads a fold is new: a body that ticks AND folds.
- Ticking a moon ticks its parent; unticking the moon leaves the parent.
- A moon's box: its distance from its parent (ruling 8), by the Moon's
  pattern (L-513); past its checked span (the trust block's delta_days
  around element_epoch_jd), one sentence saying so and the digits set by
  its measured drift (ruling 18). The sentence is a proposal for Tony's
  phone look and joins Typed facts' ALLOWED, named in the report.
- Go To on a moon opens the MOON's own box (L-514 ruling 4), in the root
  and wherever else a moon is drawn; the Earth room's Moon Go To, carried
  since Nov 7, is fixed here.

**Part 2: the view moved (rulings 15, 16, 17, 20).**
- Off-origin frames: today every frame is a box centred on the Sun
  (`sunFrameOn`, `navHome`, ranges [-r, r]). Go To, Centre on, +, - and
  Home frame about the view's middle. Go To on a moon puts its parent at
  the middle and fits the moon's whole orbit (L-479).
- PRECISION, measured before it is fixed: WebGL keeps 32-bit floats,
  about 7 digits. Measure the error at Earth's, Jupiter's and Pluto's
  distances (Math.fround on real positions is enough to size it) and
  report the numbers. The fix, as method: before a centred or close view
  is drawn, shift the whole drawing so the body in focus sits at the
  scene's origin, in 64-bit numbers. Every reader of a trace's positions
  (framing, the count line, the Sun line, the direction arrows, the text
  box's anchor) must agree on the shift.
- "Centre on <body>" on every body ruling 9 names (something drawn or
  fetched around it): the Sun, Earth, Jupiter, Saturn, the Pluto system;
  read from the config (`centresOf`), never typed. It opens the body's
  own served arrival block; the Sun's is `?exhibit=sun`'s (the
  photosphere and the rotation axis). What was ticked stays ticked; the
  count line counts what is outside; Home and Reset return to the Sun's
  view. Jupiter and Saturn get arrival blocks by L-514 ruling 1's
  pattern, the symbol alone: for Tony's phone look.
- The three axis lines and their x marks run through the middle of a
  centred view, in the Sun's directions, as the Earth room draws them
  today (ruling 17); the frame note gains one line saying where they
  cross (words for the phone look).
- The trail line is a path (ruling 20): every part but the last a centre
  and a link to that centre's opening, ticks kept; the last part what is
  in focus, bold, no link; shown always, "Solar system" alone on opening.

**Part 3: Earth folds into the root (ruling 14).**
- Earth's served shells and its guides become rows in Earth's fold, with
  the Moon, by distance (the strict-distance rule); compose draws them
  at Earth's place. `?exhibit=earth` opens the root centred on Earth, on
  Earth's opening. The Earth room's `EXHIBITS` row and `EARTH_DRIVER` are
  marked OBSOLETE and kept (Tony's ruling of Nov 3, L-509), as the Sun
  room's were. Whether the Sun line stays, now that the Sun is drawn at
  its true place, is method; say what was chosen and why.
- Loading: the root must not fetch every planet's drawings on every
  opening. Fetch a body's stored drawings when its fold or its centre
  first needs them; report the sizes.
- Scenes and places: the moons' rows and Earth's shell rows are places
  (L-519 part 2) with nothing more; the gallery editor's tree
  (`tools/drawer_places.py`) and the New Scene window's known rows
  (`tools/scene_card.py`) learn them. A scene made centred on Earth keeps
  `?exhibit=earth` (L-519's leftover 1).

**Part 4: the other folds.**
- Jupiter's and Saturn's served shells (ring_system, radiation_belts,
  orientation; ring_system, orientation) in their folds with Io and
  Titan, by distance.
- The Pluto system: the row reads "Pluto system" (ruling 19); the
  barycentre drawn as the open white square in both views
  (`render_objects.build_center_marker`; the coordinator's lean for the
  phone look, not ruled); Pluto and Charon in its fold.

Not in this session: picture B, positions measured from a centre (ruling
15, with the date span); ruling 11's 48-hour positions (with Mars, step
3); Mars and its moons (step 3); the Moon's shells; encounters (step 4).

## Checks

- `gallery_maintenance_run.py` (offline) green, read from its output.
- The drawer, drawer order, arrival, label words, typed facts, display
  figures, picture folds, drawer places and scene cards checks updated,
  each new rule shown failing once on a planted fault.
- Headless walks (`tools/headless/`): the drawer walk with new sections
  for the moon folds, Centre on, the trail path and the shifted frames;
  `compare_rooms.js` between the anchor's page and the session's, the
  root, `?exhibit=sun` and `?exhibit=earth`, every difference named and
  each one intended. The three old reds of L-521 stay recorded, not
  chased.
- The precision measurement, its numbers in the report.
- Every new file the page fetches joins `SERVED_FILES`.
- ASCII only, LF line endings.

## Close

- Records: L-515's entry for the session; Where We Are by section; the
  two skill bumps if Tony allowed them (one bump each, the four steps,
  carrying L-515's received note of Nov 8 on Reset's frame, from L-518).
- The report: the file list with edits per file; the token count as the
  environment prints it; Tony's run order; his phone-look list for each
  part (the moon folds and a moon's box past its span; Centre on for the
  Sun, Earth, Jupiter, Saturn and the Pluto system; the axis lines and
  the frame note's line; the trail path; Earth's fold; the open square;
  an Earth scene); the Tony-action rollup.
- Commit and push are Tony's.
