<!-- Doc-Kind: hand | Brief for the session that makes the dashboard's 103 buttons readable: labels that name their script, a one-line description on every card, and a way to find a tool by eye. Tony's request of 2026-10-12. -->
# Brief: the dashboard's labels, descriptions and findability

Built on orrery c5dff25076294d1402498db424cb3761a245af21 at
https://github.com/tonylquintanilla/palomas_orrery. Gallery read at
f9453ddbc8b29ed15550a4e980bf3688eed79c82 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io; it is
touched only if the build renames rows of its maintenance run (section 4).
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 12, 2026 with Anthropic's Claude Fable 5.1, in a
coordination session; the design and the build are for an Opus session.

- Type: DESIGN SESSION record and build brief (zero code).
- Companion: `documentation/AUDIT_dashboard_labels_20261012.md`, the
  audit this brief rests on: every button with its script, the
  maintenance run's name for it, and its description length; the
  flagged labels; the three findability options with tradeoffs.
- Related ledger items: L-341 (the search, DONE), L-416 (every run step
  has a button, DONE), L-324 (holds the 2026-09-12 ruling on the order
  of the Maintenance Run group, and the unbuilt parity check).
- Not yet in the ledger. The build session's closing patch opens the
  next free handle for it and names this brief and the audit.

## 0. Before building

- Pull the orrery at HEAD and pin the SHA. This brief was cut at
  c5dff25, before Tony's run of `patch_L401_4_look_close_20261012.py`
  and its push; HEAD will have moved. Nothing in that patch touches the
  dashboard or either maintenance run.
- Skills this task fires: safe-file-editing (the patch),
  agentic-pre-test (the dashboard is a GUI; run it headless on a
  throwaway copy), ledger-and-session-records (the handle, the handoff,
  Tony's page), orrery-coding-conventions (the module docstring stamp).
  gallery-cache-builder fires only if a gallery maintenance-run row is
  renamed. Confirm each loaded version against the protocol's manifest
  before using it; the manifest in the repo at HEAD is the current one.
- Read the audit first. Its section 6 is the whole list.

## 1. What Tony asked, 2026-10-12

His words, in a coordination session, after confirming every maintenance
run row has a button: "Could you check for labeling that is easily
recognizable based on the script name and functionality? And pithy
descriptions? And easy way to find besides search?"

Offered a mock-up of one of three findability directions first, he
answered "None" and asked for this brief: the Opus session designs and
builds. Design choices go to Tony one at a time, in the build session
(section 5); the render is judged by his eyes (Mode 5).

## 2. What is already ruled, and stands

- The Maintenance Run group is GENERATORS then CHECKERS, each
  alphabetical, mirroring the runner's two sections (Tony, 2026-09-12,
  on L-324). A rename changes where a card falls in that order; it does
  not change the rule. Do not re-sort by kind.
- The search box filters name and description and redraws matches under
  their group headings (L-341). It stays; this brief adds ways to find a
  tool WITHOUT it, it does not replace it.
- Every check keeps its own button (Tony, 2026-10-10; recorded in the
  L-395 move brief). Collapsing checks behind one button is out, except
  the two guest book checks already behind "Guest Book Checks" by
  L-281's design.
- A runner's card sits directly above its indented group, so what the
  automation runs stays visible (the dashboard's own docstring).
- Nothing written in a description is lost. The paragraphs carry
  rulings and dates; they move behind the card, they are not cut.

## 3. The three needs, with what the audit found and the shape recommended

### 3a. Labels that name their script

Found: 11 of 103 labels do not let you tell which script they run
("Builder Marker Join" is `test_worksheet_request_builder.py`; "Pointer
Join" and "Config Mirror Check" are both `check_constants_links.py`;
"Mirror Suite" is `test_mirror_constants.py`). 13 more carry a different
name from the row the maintenance run prints ("Constants relations" in
the run is "Test Constants Provenance" on the dashboard). Two habits:
one script under two labels that name the mode and drop the script;
"Test" on 20 of the 26 checkers and not the other 6, under a heading
that already says CHECKERS.

Recommended:
- THE BUTTON IS NAMED WHAT THE RUN PRINTS. One name per check, the same
  in `orrery_maintenance_run.py`, the gallery's
  `gallery_maintenance_run.py`, and the dashboard. When a row goes red,
  its button has that name. Where the run's name is itself poor
  ("Constants relations" for `test_constants_provenance.py`), rename
  both in the same patch, never one.
- One script, one base name; a mode is a suffix after two dashes:
  "Exact Rows Report" and "Exact Rows Report -- check"; "Status Lines"
  and "Status Lines -- shape only".
- The script's file name is printed on the card in small type under the
  label, so the mapping is visible without hovering. Today it is only a
  tooltip on the Launch button.
- "Test" comes off every checker label (Tony, 2026-10-12; section 5).
  The run's own row names mostly do without it already.

### 3b. A one-line description on every card

Found: the median description is 59 words, the longest 221; 47 of 103
run over 60 words. Each card shows its whole paragraph, wrapped at 600
px, so the page is 103 paragraphs in one column.

Recommended:
- Every entry gets a line of at most twelve words that says what the
  tool does, shown on the card. The paragraph stays, behind the card: a
  tooltip on the name, or an expand, the builder's choice, judged by
  Tony's eyes.
- A one-line description is a claim about what the script does. Write
  it from the script, not from the paragraph alone, and say so in the
  handoff: which were checked against source and how. The audit's
  section 4 holds five drafts of the shape; they are drafts.
- The LAUNCH_GROUPS entry is a tuple `(display_name, script_filename,
  description, [base_dir], [interactive], [args])`. Add the short line
  without disturbing the positional fields that 103 entries already use;
  a dict, or a sixth element with a default, are both fine. The
  search's filter on description should read both texts.

### 3c. Finding a tool by eye

Found: eight groups in one scrolling column, two with 34 and 36 cards.
The groups answer "which repository, which kind", not "what am I trying
to do".

The audit's section 5 gives three directions. Recommended order, under
The Braid (the artifact orders the work; one slice at a time):
- First, A and B together: shorter cards (3a and 3b do most of this on
  their own) and subheadings inside the gallery checks group, which has
  none. Its 34 cards fall into kinds: pulls from the orrery, mirror
  checks and suites, room smokes run by Node, the cache and its builder,
  the rest. The builder names the kinds from the scripts, not from this
  sentence, and keeps cards alphabetical under each.
- C, a "when" index above the groups (before a push; after editing
  constants_new.py; after a cache build; a room looks wrong; a new
  object), is recorded for a later slice. It is the one that answers the
  question Tony arrives with, and the one that goes stale unless each
  entry carries its occasions as data and the index is generated from
  them. Design it as data from the start if it is built at all; do not
  hand-write it.

## 4. Build notes (method; the build session settles these and records them)

- One patch script for the orrery, `patch_<handle>_<n>_dashboard_...py`,
  under safe-file-editing: anchored, all-or-nothing, LF, ASCII, the
  docstring stamp moved. If a gallery run row is renamed, a second
  patch for the gallery, with its own SHA pinned.
- THE PARITY CHECK, built this time. L-324's note of 2026-09-12 left it
  as backlog: nothing enforces that the runner's rows and the
  dashboard's buttons agree. Build it as a row of the orrery maintenance
  run that reads both files and compares NAMES, not counts, in both
  directions, for both repositories; it fails on a row with no button,
  a button whose name is not the run's, and a script it cannot read.
  Print what was compared and how many. A Check That Cannot Fail Is Not
  Passing: plant a mismatch and show it caught, in the handoff.
- The gallery's maintenance run and the Daily Run are read from the
  gallery repo at its pinned SHA. The dashboard already knows both
  roots (`GALLERY_REPO_DIR`).
- Pre-test: py_compile, then the dashboard under xvfb on a throwaway
  copy with customtkinter present; every card must draw, every Launch
  button must resolve its script (the "Not Found" state is the one to
  watch after renames), and the search must still redraw. The pre-test
  never edits the deliverable.
- `module_atlas.py` rebuilds MODULE_ATLAS.md from the docstring; the
  maintenance run does that. Say in the dashboard's docstring what
  changed and why, with the date.
- Carry the rulings of section 2 into the dashboard's docstring where
  they are not already there, so the next builder reads them in the file
  and not only here.
- What is permanent after the patch is spent: the short-description
  field, the printed script name, the gallery subheadings, the parity
  check and its planted-fault test. Say so in the handoff.

## 5. For Tony, one at a time, in the build session

(Three remain; the first was ruled the same day this brief was written.)

- RULED, 2026-10-12, same day, in chat: **"Test" comes off the checker
  labels.** Tony: "Confirmed". The heading says CHECKERS, the run's
  rows mostly do without it, and the labels get shorter. Record:
  `documentation/DESIGN_rulings_20261012.md`, ruling 5. Not a question
  for the build session.
- (decide) **Where the paragraph goes.** A tooltip on the card's name,
  or an expand arrow. Shown as a render, not described; Mode 5.
- (decide) **The gallery group's subheadings**, by name, once the
  builder has drawn them from the scripts.
- (decide, recorded, not urgent) **Whether the "when" index is built**,
  and if so from what tag.

## 6. Tony's actions, all of them

- (do) Push `patch_L401_4` first (its own brief); this build sits on
  that HEAD.
- (do) Start the Opus session from this brief and the audit, when it
  comes in your order.
- (decide) The items in section 5, in that session.
- (do) Run the patch, the maintenance run (the new parity row among
  them), open the dashboard and look; push.

Brief written October 2026 with Anthropic's Claude Fable 5.1.
