<!-- Doc-Kind: hand | Brief for the session that makes the provenance scanner's Tier-1 total travel with its domain split (orrery, Earth System, stars, ...) everywhere the total prints, and gives a module's domain one home: the docstring Domain tag. Lifted out of the L-425 brief (its section 3d) to run as its own parallel session. Tony's ask of 2026-10-12 and 13. -->
# Brief: the Tier-1 total prints with its domains (L-437)

Built on orrery 400a9615ce7238ec4e836c5eeba9b359c5f619bf at
https://github.com/tonylquintanilla/palomas_orrery ("L431 build 2
L436"). The gallery is not touched.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 13, 2026 with Anthropic's Claude Fable 5.1, in the
coordination session of October 12 and 13.

- Type: BUILD brief (zero code). Report-only change; no scoring moves.
  No decision waits on Tony.
- This replaces section 3d of
  `documentation/HANDOFF_L425_citation_locations_brief_20261012.md`,
  which carried the same work; that brief now points here. The L-425
  session does not build the split.
- Ledger: opens L-437, by this session's closing patch. Record of the
  ask: `documentation/DESIGN_rulings_20261012.md`, ruling 2, last
  bullet.
- Parallel to: the dashboard's labels (building now), L-425, L-424
  with L-426, the Horizons move. Rules for building beside unpushed
  patches: `documentation/HANDOFF_scaffolding_sessions_coordination_20261013.md`,
  section 3. This build's files overlap the others only on
  `orrery_maintenance_run.py` (its summary wording), the ledger and
  Where We Are.

## 0. Before building

- Pull the orrery at HEAD and pin the SHA. At 400a9615 two patches sit
  in the root unrun: `patch_L431_7_look_fixes_20261013.py` and
  `patch_L436_1_idea_20261013.py`. If HEAD still carries them, they
  are Tony's to run; this build does not depend on either, but its
  Where We Are edit anchors on lines L-436's patch also touches, so
  the two must not both edit the Signals block. See section 3.
- Skills this task fires: provenance-discipline (confirm 2.28 against
  the manifest; Report Domain Classification and Scanner Mechanics are
  the sections this build rewrites), safe-file-editing,
  agentic-pre-test, ledger-and-session-records.
- Measure at HEAD before building; the numbers in section 1 are from
  400a9615's `PROVENANCE_AUDIT.md`.

## 1. What Tony asked, and what is already there

Tony, 2026-10-12: "the provenance checker is still reporting 288 tier 1
items. Can we separate this into meaningful groups, like orrery, earth
science and stars in the checker report?" And 2026-10-13: "could you
give me an updated handoff and prompt for the scanner report that
breaks the tier 1 results by grouping as we discussed? can this go
parallel to the other work?"

The split exists and the total travels without it:
- `PROVENANCE_AUDIT.md`, "Findings by File Type", at 400a9615: orrery
  117 Tier-1 in 56 files (`shell_configs.py` 35, `idealized_orbits.py`
  25 after build 2's four exceptions), Earth System 149 in 13 files
  (three paleoclimate modules carry 112), stars 12 in 11 files
  (`exoplanet_coordinates.py` 5), utilities 2, dev tools 0, gallery 0.
  Whole tree 280.
- The scanner's console prints "Whole tree: 280 Tier-1" with no split
  (`provenance_scanner.py` line 3251 at 400a9615). The maintenance run
  quotes the GATE PATH line only. Tony's page prints "Whole tree: 280"
  in its Signals block.
- `data/provenance_history.json` already carries a `domain_counts`
  field per run, but it is the ALL-TIER total per domain (orrery 779,
  Earth System 226), not Tier-1 per domain. It answers a different
  question from the one Tony asked, and a reader of the history would
  take it for the split. Name this in the handoff as the near-miss it
  is.
- A module's domain has two homes. `provenance_scanner.py` keeps a
  hand list, `MODULE_DOMAIN_MAP`, with its own `classify_domain`;
  every module declares `Domain:` in its docstring in the same six
  words, and `module_atlas.classify_domain` reads that. At c5dff25 the
  two disagreed on 12 files (eleven dev tools filed as orrery, and
  `data_acquisition.py`, tagged stars, whose one Tier-1 finding is
  counted as orrery), and 15 files with findings were in no list and
  defaulted to orrery, printed as a "Domain coverage gap". Measure
  again at HEAD.

## 2. The build

### 2a. The split prints wherever the total prints

The form, everywhere: `280: orrery 117, Earth System 149, stars 12,
utilities 2`. Domains with zero are left out of the line and kept in
the table. Names beside the count, as the GATE PATH line already does.
- The scanner's console summary: the "Whole tree" line.
- `PROVENANCE_AUDIT.md`: its Priority Summary or header, wherever the
  whole-tree total is first stated; the "Findings by File Type" table
  stays as the full breakdown.
- The run history (`provenance_history.py`): a `tier1_by_domain` field
  per run, beside `domain_counts`, which keeps its meaning and gets a
  comment saying what it counts. The history's own summary line, if it
  prints a total, prints the split.
- The maintenance run's summary: the scanner's row already quotes the
  GATE PATH line; add the whole-tree line with its split as the row's
  second line, or in the FILES WRITTEN block's notes, the builder's
  call, so the split reaches the run's output without displacing the
  gate.
- Where We Are, Signals: "Whole tree: N: orrery a, Earth System b,
  stars c" READ FROM THE AUDIT when the page is written, as the block's
  own rule says.

### 2b. One home for a module's domain

- `provenance_scanner.classify_domain` reads the module's docstring
  `Domain:` tag through `module_atlas.classify_domain` (or the same
  reader, imported), and `MODULE_DOMAIN_MAP` goes. One Value, One Home,
  on a property.
- The "Domain coverage gap" note then names only a module with NO tag,
  which is the atlas's existing coverage-gap meaning; at c5dff25 two
  modules had none. A module with a tag the vocabulary does not know is
  named too, as the atlas does.
- A `Domain:` tag is the store; the tag's vocabulary is the six words
  the audit's table already uses. The skill's Report Domain
  Classification section is rewritten to say so (section 2d).

### 2c. Plant it

- A file whose docstring tag and the old hand list disagreed
  (`data_acquisition.py`, tagged stars, listed orrery) is shown filed
  by its tag, and its finding moves from orrery to stars in the table.
- A file with no tag is shown named in the gap.
- The console line, the audit line and the history field are shown to
  agree with the table's column sums, by a test that reads all four.
- A planted change to one domain's count with the total unchanged (one
  finding moved between domains) is shown to change the printed line:
  the split is what makes the total's delta name what moved (A Check
  That Cannot Fail Is Not Passing, fourth move).
- `test_row_run.py` pins the scanner's row reading and the gate path;
  extend it or add `test_domain_split.py`, named what it prints, with
  a dashboard button and a maintenance-run row (the dashboard build's
  rule: the button is named what the run prints).

### 2d. The skill

provenance-discipline, two sections, one version under One Session,
One Bump, with the protocol entry and the manifest run in the same
commit:
- Report Domain Classification: the docstring tag is the store;
  `MODULE_DOMAIN_MAP` is gone; the gap note names untagged modules.
- Scanner Mechanics: a bullet saying the whole-tree total prints with
  its domain split everywhere it prints, and that
  `tier1_by_domain` in the history is Tier-1 while `domain_counts` is
  all tiers.
If L-425's session has already bumped provenance-discipline when this
build closes, this build's sentences ride a second version only if
that one is pushed; otherwise they are handed to the L-425 session to
carry. Say which happened in the handoff.

### 2e. Not in this build

- Any scoring change. Nothing here moves a finding between tiers.
- The 288 (now 280) themselves: the path, not a sweep
  (`DESIGN_rulings_20261012.md`, ruling 7).
- L-425's three checks and their rows. That brief keeps them.

## 3. Parallel-build notes

- `orrery_maintenance_run.py`: the dashboard build renames rows and
  L-425 adds three; this build changes only the scanner row's summary
  wording. Anchor on that row's own lines.
- Where We Are: this build edits the Signals block's "Whole tree" line
  only. `patch_L436_1` edits the page's not-urgent list, one Settled
  line and one details line; `patch_L431_7` may edit the box and the
  road. Anchor on the Signals line alone, and if it has moved under
  you, re-anchor on the new text rather than widening the match.
  Every patch adding a page line removes one; the page is at its
  130-line cap.
- The ledger: open L-437 at the end of section A (or where the
  indexer's rules put a new open item) and add one stamp line to the
  header; anchor on the "Review and RICE update" line, which every
  patch leaves in place.
- A patch predicts the scanner's CHANGE, not its total: this build's
  prediction is "no Tier-1 count moves; one finding moves from orrery
  to stars" (if `data_acquisition.py`'s tag still disagrees at HEAD).

## 4. Tony's actions, all of them

- (do) Start the session from this brief, in parallel with the
  dashboard build or after it.
- (do) Run the patch and the maintenance run; read the scanner's row
  and the audit's header; push.
- (decide) Nothing; the design is Tony's own ask, answered by the
  skill's rules.

Brief written October 2026 with Anthropic's Claude Fable 5.1.
