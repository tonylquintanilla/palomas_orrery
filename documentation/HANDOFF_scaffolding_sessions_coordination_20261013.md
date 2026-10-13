<!-- Doc-Kind: hand | Coordination note for the four scaffolding sessions (the dashboard's labels, L-425, L-424 with L-426, the Horizons check's move), which run beside L-431 build 2 rather than after it. Says what changed since the briefs were cut, the running order, and the rules for a patch built while another session's patch is unpushed. -->
# The scaffolding sessions: order and parallel-build rules

Built on orrery c9722520c6316d3136489e37abf0179c93a39703 at
https://github.com/tonylquintanilla/palomas_orrery ("L431 build 2":
that commit carries build 2's brief and Tony's run record, not its
patch). The gallery is read at
f9453ddbc8b29ed15550a4e980bf3688eed79c82 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io and is
touched only by the Horizons move session.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 13, 2026 with Anthropic's Claude Fable 5.1, in the
coordination session of October 12.

- Type: coordination note (zero code). It sits in front of four briefs
  and changes none of their scope.
- The four briefs, all in `documentation/`, all at HEAD:
  1. `HANDOFF_dashboard_labels_brief_20261012.md` (+ its audit,
     `AUDIT_dashboard_labels_20261012.md`)
  2. `HANDOFF_L425_citation_locations_brief_20261012.md`
  3. `HANDOFF_L424_L426_worksheet_checker_brief_20261012.md`
  4. `HANDOFF_L395_horizons_check_move_brief_20261012.md`
- Tony's rulings behind them: `DESIGN_rulings_20261012.md`.

## 1. What changed since the briefs were cut

- Tony's run of 2026-10-12 pushed everything the briefs assumed:
  patch_L401_4 and patch_L433_1 applied, maintenance run 24 of 24,
  push gate 0, Io's hover looked at (3fec6997); then v3.92 (4037362b).
  The Project's instructions now read v3.92 and the installed
  horizons-orbital-mechanics reads 1.3; each session confirms its own
  loaded copies as usual.
- L-431 build 2 is being built in its own session, started
  2026-10-13, from `HANDOFF_L431_build2_orbits_markers_brief_20261012.md`.
  Its patch is NOT yet pushed. It will edit `idealized_orbits.py`,
  `apsidal_markers.py`, `orbital_param_viz.py`, `palomas_orrery.py`,
  `orbital_period.py`, `data/provenance_exceptions.json`, the ledger
  (L-431, L-401), Where We Are (stage 6a, the box) and possibly
  `test_position_digits.py` and `orrery_maintenance_run.py`'s row list.
- The four in-passing exception entries of ruling 7 belong to build 2,
  not to L-425. L-425's brief says nothing about them; this note says
  so to stop both from adding them.

## 2. The running order, Tony's choice

Any order works for scope; this one minimises collisions with build 2
and with each other:

1. **The dashboard's labels** first. It touches
   `palomas_orrery_dashboard.py`, `orrery_maintenance_run.py` (row
   names), the gallery's `gallery_maintenance_run.py` (row names, if
   any are renamed), the ledger and the page. Build 2 may add a row to
   the maintenance run; see section 3.
2. **L-425** second. Its three new rows and buttons are named by the
   dashboard build's rule (the button is named what the run prints),
   so it is simpler after that build has landed. It also adds the
   domain split (section 3d) to the scanner, the run history and the
   page's Signals line.
3. **L-424 with L-426** third or in parallel with 2: it touches only
   `worksheet_checker.py`, `test_worksheet_checker.py`, the
   provenance-cross-check skill, the ledger and the page. No overlap
   with build 2 or the dashboard build beyond the records.
4. **The Horizons check's move** last: it touches both repositories,
   the maintenance run (a network row), the dashboard, `data/`,
   `export_objects.py` and `test_objects_export.py`, and it benefits
   from the dashboard rule and the L-425 network-row convention being
   settled first (L-425's brief, section 3c, says whichever lands
   first sets the convention; with this order it is L-425).

## 3. Rules for a patch built while another session's patch is unpushed

These are the ledger skill's rules applied to two sessions at once;
nothing here is new.

- **Build on HEAD, not on the other session's working copy.** Pull at
  HEAD and pin the SHA. The other session's changes are not in the
  repository until Tony pushes them, so a patch cannot anchor on them.
- **Records are edited at their own anchors, never by rewrite.** The
  ledger and Where We Are are edited by both sessions. Each patch
  edits only the lines of its own items (its L-blocks, its lines in
  the page's box, road, Settled and details) and checks each anchor
  exactly once. A patch that rewrites a whole section will refuse or
  overwrite after the other has run. The page's "Last updated" line
  is the one line both will touch: anchor on the date, not the
  wording, and the second to run wins; neither refuses on it.
- **The maintenance run's row list.** Build 2 may add a row; the
  dashboard build renames rows; L-425 adds three. Each patch inserts
  or renames ITS rows by anchoring on neighbouring rows it does not
  change, so order of running does not matter. The dashboard build's
  parity check (names in the run against names on the dashboard, both
  directions) is what catches a row left without a button by whichever
  patch ran second; the session that runs second fixes the mismatch in
  its own patch and says so.
- **The Tier-1 total.** Build 2's four exceptions take the orrery's
  count down by four. A patch predicts the scanner's CHANGE, not its
  total (provenance-discipline, Scanner Mechanics), so a scaffolding
  patch says "minus N on these files" and does not state 288 or 284.
- **Tony runs patches in the order he receives them, one maintenance
  run after each.** A patch that refuses on an anchor another patch
  moved is reported back to its session with the output; the session
  re-anchors on the new HEAD and redelivers. Nothing is hand-edited.
- **The page's cap.** Where We Are is at 130 of 130 lines above the
  marker after patch_L433_1. Every patch that adds a line to it must
  remove one, and checks the cap before writing, as patch_L433_1 does.
  Candidates to shorten: the Settled lines of Oct 10 and 11 as they
  become habit; the details list.

## 4. Tony's actions, all of them

- (do) Commit and push this note with the next run, so each session
  can read it beside its brief.
- (do) Start each session from its prompt below, in the order of
  section 2 or your own; run each patch as it arrives, maintenance run
  after each, push after each.
- (decide) Nothing here; the decisions are in each brief's section 5.

## 5. The starting prompts

Each is complete on its own; paste one into a new chat in this
Project.

### Dashboard labels

    Design-and-build session for the dashboard's labels, descriptions
    and findability. Read documentation/HANDOFF_scaffolding_sessions_coordination_20261013.md
    first, then documentation/HANDOFF_dashboard_labels_brief_20261012.md
    and documentation/AUDIT_dashboard_labels_20261012.md, all in the
    orrery repo. Pull the orrery at HEAD and pin the SHA. Pin the
    gallery's SHA separately; touch it only if a maintenance-run row
    there is renamed. L-431 build 2 is being built in another session
    and is not yet pushed: build on HEAD, edit the ledger and Where We
    Are at your own items' anchors only, and insert or rename your
    maintenance-run rows by anchoring on rows you do not change.

    Load safe-file-editing, agentic-pre-test, ledger-and-session-records
    and orrery-coding-conventions, and confirm each loaded version
    against the manifest in the repo's PROJECT_INSTRUCTIONS.md before
    using it.

    The "Test" question is already ruled (it comes off). Bring me the
    brief's three remaining section 5 decisions one at a time, with a
    render where the brief says the render decides. Then build: one
    patch for the orrery, the parity check included and shown catching
    a planted mismatch, pre-tested on a throwaway copy. Close with the
    ledger item under the next free handle, the handoff, and Where We
    Are by section, within its 130-line cap.

### L-425, the citation location checks

    Design-and-build session for L-425, the citation location checks.
    Read documentation/HANDOFF_scaffolding_sessions_coordination_20261013.md
    first, then documentation/HANDOFF_L425_citation_locations_brief_20261012.md
    and documentation/DESIGN_rulings_20261012.md (ruling 2) in the
    orrery repo. Pull the orrery at HEAD and pin the SHA. The gallery
    is not touched. L-431 build 2 may still be unpushed: build on HEAD,
    edit the records at your own items' anchors only, and do not add
    the four idealized_orbits.py exceptions, which are build 2's.

    Load provenance-discipline, safe-file-editing, agentic-pre-test and
    ledger-and-session-records, and confirm each loaded version against
    the manifest in the repo's PROJECT_INSTRUCTIONS.md before using it.

    Measure again at HEAD first. Then bring me the section 5 decisions
    one at a time, the excused classes as one named list with a
    recommendation per class. Then build: one new checker with its
    planted-fault tests, three maintenance-run rows and buttons named
    what they print, the link check with its 30-day record in data/,
    the Tier-1 domain split printed beside the total everywhere it
    prints and the scanner reading each module's docstring Domain tag
    (section 3d), one patch script, pre-tested on a throwaway copy.
    Close with L-425's ledger block, the handoff, and Where We Are by
    section, within its 130-line cap.

### L-424 with L-426, the worksheet checker

    Build session for L-424 and L-426, the worksheet checker's compare().
    Read documentation/HANDOFF_scaffolding_sessions_coordination_20261013.md
    first, then documentation/HANDOFF_L424_L426_worksheet_checker_brief_20261012.md
    in the orrery repo. Pull the orrery at HEAD and pin the SHA. The
    gallery is not touched. Other sessions may have unpushed patches:
    build on HEAD and edit the records at your own items' anchors only.

    Load provenance-cross-check, provenance-discipline,
    safe-file-editing, agentic-pre-test and ledger-and-session-records,
    and confirm each loaded version against the manifest in the repo's
    PROJECT_INSTRUCTIONS.md before using it.

    Nothing waits on me; the design is settled. Build it: two words for
    a moved value, rounding to significant figures, the planted tests
    shown caught, the skill's bullet updated in one version with the
    protocol entry and the manifest run in the same commit, one patch
    script, pre-tested on a throwaway copy. Close L-424 and L-426 in
    the ledger, with the handoff and Where We Are by section, within
    its 130-line cap.

### The Horizons check's move (L-395)

    Build session for L-395, moving the Horizons check into the
    orrery's maintenance run. Read
    documentation/HANDOFF_scaffolding_sessions_coordination_20261013.md
    first, then documentation/HANDOFF_L395_horizons_check_move_brief_20261012.md
    and documentation/DESIGN_rulings_20261012.md (ruling 6: a changed
    data sheet is cleared by the row, option A) in the orrery repo.
    Pull the orrery at HEAD and pin the SHA; pull the gallery at HEAD
    and pin its SHA separately, since this build touches both. Build
    on HEAD and edit the records at your own items' anchors only. If
    L-425 has landed, match its network-row convention; if not, set it
    and say so.

    Load horizons-orbital-mechanics (confirm it reads 1.3),
    gallery-cache-builder, safe-file-editing, agentic-pre-test and
    ledger-and-session-records, and confirm each loaded version against
    the manifest in the repo's PROJECT_INSTRUCTIONS.md before using it.

    The first section 5 decision is ruled (option A). Bring me the
    second only if you need it now; its default is no. Then build: the
    check and its suite moved into the orrery with their recorded
    answers, the confirmations carried over with their dates, the
    sheets' record seeded from the survey, the export carrying the
    dates, the website's daily run losing step 2 and its offline check
    reading the dates from the pulled export, every network answer in
    the tests recorded and every fault planted first, one patch per
    repository, each pre-tested on a throwaway copy. Close with L-395's
    ledger block, the handoff, Where We Are by section within its
    130-line cap, and the skill bumps under One Session, One Bump.

Coordination note written October 2026 with Anthropic's Claude Fable 5.1.
