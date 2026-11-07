<!-- Doc-Kind: hand | The brief for one Claude Code session on the website: L-515 (one nested tree), steps 1 and 2a. Communication; written once, read by its session. -->
# Brief: one nested tree, steps 1 and 2a (website)

Built on orrery 18b70f0830a5ab4a37319e1270cea7a42d9f268d at
https://github.com/tonylquintanilla/palomas_orrery
and gallery 9c6093af12c7576333583766ed850fbf6528f097 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io
(both branch main, read 2026-11-07, 13:05 Chicago). The rulings this brief
cites are on L-515 in Tony's next orrery push; the session reads them there.
Nightly bot commits since are expected.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD, a Claude Code session in the gallery repository, through the
python_work door. Written November 7, 2026 with Anthropic's Claude Opus
5.5, the coordinating session, on Tony's go-ahead of 13:01 Chicago.

## Start

1. Record both bases; say whether either moved past the anchor (bot
   commits are expected).
2. Read the orrery's `documentation/WHERE_WE_ARE.md` and L-515 (one
   nested tree) in `LEDGER_CONSOLIDATED.md`: its twelve rulings and the
   adjudication of the three reviews. The returns are
   `documentation/REVIEW_L515_nested_tree_return_*_20261107.md`.
3. Skills, each against the manifest, by its read plan: interactive-exhibit
   (1.32, in full: this session changes its drawer rules), gallery-cache-builder
   (1.18, the parts on objects_config and "a config change is not deployed
   until the cache is rebuilt"), gallery-assembler (1.3, only if the
   session touches the assembler; step 2a should not), safe-file-editing
   (1.14), ledger-and-session-records (1.22).
4. Ask Tony ONE thing before building: this session will change
   interactive-exhibit's rules (the Solar System room's drawer, the
   room list, Reset in a centre), and a gallery session edits only the
   orrery's ledger and Where We Are. May it also edit the orrery's
   `skills/interactive-exhibit/SKILL.md`, run `skills_index.py`, and add
   the protocol's version entry, for one bump (the records skill's
   binding rule)? If no, the changes are carried on L-515 for the next
   orrery session.

## The job, in this order, with a stop after each part

Each part is reported before the next starts. If the session runs long,
it stops at the end of a part and says where it stopped.

**Part 1 (L-515 step 1): the tree is the fetched centre.**
- Read at the anchor: every object's `center_slug` is the centre JPL is
  asked around for it; `parent` differs from it for `pluto` ("sun") and
  `charon` ("pluto"), both served around `pluto_barycenter`; the Sun's
  `parent` is null, the root. Only the cache builder reads `parent`
  (`tools/gallery_cache_builder.py`, copied into the coverage index).
- Build a check in the gallery run: every object's `parent` equals its
  `center_slug` (the Sun's null as the root), naming each that does not.
  Show it failing first on the anchor's config (A Check That Cannot Fail),
  then correct the two `parent` values through a tool the config's rule
  allows (interactive-exhibit, Only two tools write the served config:
  add `parent` to `tools/store_writer.py`'s allow list if that is the
  method, and say so).
- Cache in step will be red until the nightly build copies the new
  parents; say so in the report, as for any config change.

**Part 2 (step 2a): one drawer, the root and Earth.**
- Keep `EXHIBITS` as per-centre compose hooks keyed by slug; the
  addresses `?exhibit=solar-system`, `?exhibit=sun` and `?exhibit=earth`
  keep opening what they open today until part 3 (returns 1 and 3).
- One drawer builder for both kinds of row: bodies (the Solar System
  room's served rows, groups, Find) and shells (the Sun's and Earth's
  legend groups). The two today are `ssBuildRows` with
  `gallery/solar_system_drawer.js` and `buildSunDrawer` with
  `gallery/drawer_order.js`.
- The fixed centre row in every centre (L-514 ruling 2, and Tony's note
  of Nov 6: Earth has none today): no tick box, always drawn, its name
  opening its text box and panel.
- The trail line at the top of a centre's drawer, "Solar system > Earth",
  its first part returning to the root (ruling 2, "A").
- In the root's list, "Enter the <name> room" becomes "Centre on <name>"
  (`WORDS.enter`); a body with no centre built reads "Not built yet"
  where the button would be (ruling 10).
- Returning to the root restores what the visitor had ticked there;
  Reset still starts fresh (ruling 10). Which Reset a centre gets, and
  where a child's row sits among shells, are interactive-exhibit's to
  rule (return 1, finding 10); write the rule, do not ask Tony.

**Part 3 (step 2a): the Sun's shells in the root (ruling 7).**
- The root lists the Sun's shells beside every body served around the
  Sun, the shells unticked on opening; they are drawn at the origin, so
  nothing is composed (return 1, finding 4: `buildFeatureTraces` already
  takes a body's position).
- `?exhibit=sun` opens the root with the Sun's shells ticked, at the Sun
  room's opening frame; the Sun room's row in `EXHIBITS` goes.
- How the root frames a 120 AU shell beside the planets is method
  (return 1, finding 7); the session writes the rule.

**Part 4, separable (L-165, Tony's ruling of Nov 7, 12:53): freeze past
the window.** When the minute opened lies past the served window, a room
draws at the last day its data covers and says so plainly, instead of
the resolver refusing. If parts 1 to 3 have run long, this part is left
for its own session and recorded.

Not in this session: composing a moon into its parent's view and the
off-origin focus (step 2b); Mars (step 3, L-514); encounters (step 4);
look toward (ruling 5); positions served for short windows (ruling 11).

## Checks

- `gallery_maintenance_run.py` (offline) green, read from its output;
  Cache in step red only for the reason part 1 names.
- The drawer checks (`documentation/smoke_solar_system_drawer.js`,
  `smoke_drawer_order.js`, `smoke_arrival.js`, `smoke_label_words.js`)
  updated for the one drawer, each shown failing once on a planted fault.
- The headless walks (`tools/headless/`): `walk_solar_system_drawer.js`,
  `walk_drawer_order.js`, `walk_shell_reset.js`, and `compare_rooms.js`
  between the anchor's page and the session's for every room, the
  differences named and each one intended.
- Every new file the page fetches joins `SERVED_FILES` in
  `gallery_maintenance_run.py`.
- ASCII only, LF line endings.

## Close

- Records: L-515's entry for the session; Where We Are by section; the
  interactive-exhibit bump if Tony allowed it (one bump, the four steps).
- The report: the file list with edits per file; the token count as the
  environment prints it (Token Economy); Tony's run order; his phone look
  list for the root, `?exhibit=sun` and `?exhibit=earth` (the drawer,
  the fixed row, the trail line, Centre on, Not built yet, the ticks on
  return, Reset); the Tony-action rollup.
- Commit and push are Tony's.
