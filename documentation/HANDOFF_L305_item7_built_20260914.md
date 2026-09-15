# A figure in prose finds a home, and a unit takes two belts with it

Built on orrery `fc34bdc2366a5269e0684071e3da7488d411632b`
at https://github.com/tonylquintanilla/palomas_orrery
Gallery at `0d8e6044f5a998a2c61b4a515ef5a4fa86cfea7a`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

The session opened at orrery `2f1a0c2f` and gallery `eab070a9`. The orrery
moved twice, `773e5c2d` then `fc34bdc2`. The gallery moved four times,
`deb29e6d`, `29bc1bd0`, then `0d8e6044`. Every HEAD read back with
`ls-remote`.

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-14
Type: BUILD + DOCUMENTATION. Six patch scripts, one design record.
Protocol v3.59 (this session raised it from v3.58).
Handles: L-305 item 7, L-322, L-323, L-325, L-327, L-328, L-329.
Continues `HANDOFF_L326_bump_and_push_20260914.md`, which it does not
supersede.

## STEP 0 -- Gates for the next session

- Version-check every skill at load. This session read and matched
  `provenance-discipline` 2.12, `ledger-and-session-records` 1.11,
  `safe-file-editing` 1.11, `orrery-coding-conventions` 1.8,
  `agentic-pre-test` 1.2 and `gallery-cache-builder` 1.4. None was bumped
  tonight.
- **The PROTOCOL moved to v3.59 and the Register Rule was rewritten.**
  Read it before writing anything to Tony. It is no longer a style
  preference. Compressed language is a channel only Claude can read, and
  the rule now says so in Tony's own words.
- `git ls-remote` both repos. Expect orrery `fc34bdc2` and gallery
  `0d8e6044`.
- Six spent patch scripts sit in the two repo roots and belong in
  `documentation/` (rollup item 1).

## WHAT HAPPENED

L-305 item 7 was built, in four parts plus a repair. The belts, the
magnetotail and the two model standoffs stopped being prose and became
rows that the text reads.

1. **The store, part 1.** Four belt edge rows in geocentric equatorial
   Earth radii, `EARTH_MAGNETOTAIL_OBSERVED_RADII` at 220 on Slavin et
   al. (1983), and the two peak rows corrected. The outer peak moved to
   `# Unit: l_shell` with `# Status: declared`, because 4.5 is a midpoint
   of an L band, and Baker came off its citation: his figure 30 uses
   L* = 4.5 as a selected analysis location, not a universal peak.
2. **Two scatter rows, part 4.** Shue's 1.23 R_E and Jelinek's 0.69 R_E,
   the spread of real crossings about each fitted surface. Both figures
   already sat inside other rows' comments; this gave them rows so a
   hover could read them.
3. **The strings, part 2.** Every figure a visitor reads in Earth's
   magnetosphere and belt text now interpolates a row. The kilometres are
   computed at render through one helper whose `sig` argument is
   REQUIRED, so a caller that forgets raises instead of inheriting a
   choice. Two claims the L-321 round did not support are gone: "making
   complex life possible", which three checker legs returned NO on
   against Griessmeier et al. (2016), and "protects Earth from solar
   radiation", which reads as sunlight rather than particles.
4. **The served data, part 3.** The four edges and the magnetotail extent
   became gallery rows; the two belt notes stopped carrying spans.
5. **The repair.** See THE LESSON.
6. **Protocol v3.59, and three new ledger items.** L-327 holds three tool
   changes, L-328 a subtraction pass on the skill layer, L-329 the
   Register Rule rewrite.

## WHAT TONY RULED

- **Ruling B, amended a second time.** The store holds geocentric
  equatorial Earth radii, and every belt row names the frame and the
  paper its figure follows. The rule behind revision 2 was right; the
  fact under it was wrong, because three open sources state the extents
  in geocentric radii rather than in L.
- **Kilometres stay, derived rather than stored,** rounded to the figure
  count each row's own source gives, labelled in the hover as a
  conversion, and the peaks get the same treatment.
- **Significant figures come from the row, not from a uniform rule.**
  Claude had written a helper that rounded everything to two figures.
  Meredith states the outer belt as 3 to 7, one figure each.
- **Standoff precision, settled and shipped.** Both standoffs print at
  the model's own precision, 10.25 and 13.51, with the physical scatter
  printed beside them. The resolution came from Fable: name the quantity
  before counting figures. A model evaluation carries the model's
  figures; a physical claim carries the physical uncertainty; the hover
  says which one it is printing. This closes a question carried since
  2026-09-13.
- **Zero new rules for the three misses of the evening.** Three tool
  changes instead, in L-327.
- **L-322 runs as mechanism-whole plus store-in-slices,** gated per
  slice, with (d) prioritised. Tony's note on adopting it: slices are
  consistent with the Braid.
- **`l_shell` is the right token and `dimensionless` is the defect.**
  Tony, against Claude, who had proposed the opposite. `deg` is the
  precedent: an angle is dimensionless too and the store gives it its own
  token.
- **`EARTH_VAN_ALLEN_OUTER_RADII` is to be renamed.** Not built tonight.

## THE LESSON OF THIS SESSION

**A served unit changed without checking who reads it, and it took both
belts off the page.**

`beltDistance()` in `gallery/feature_renderers.js` hard-checks the served
unit: anything that is not `"R_earth"` returns null and warns. Moving the
outer belt to `l_shell` made that call return null, the inner/outer pair
test right below it needs two numbers, and the renderer returned with
"nothing drawn" -- taking the INNER belt with it, which had changed
nothing. The Earth scene went from 18 drawer groups to 16.

Claude checked one consumer of that field, the drift checker, and
concluded. There were two.

The sharper half: **the check that catches this exists and gates, and it
was not run before the push.** `documentation/smoke_earth_geometry.js`
reads `data/objects_config.json` directly and asserts 18 drawer groups.
Run between the config patch and the push it would have failed. Run after
the repair it passed, and the live run then matched its prediction
exactly.

This is A Check That Cannot Fail Is Not Passing read from the other end.
The check could fail, would have failed, and was skipped.

A second instance the same evening, smaller and caught in the sandbox: a
patch edit rewrote the very block the patch used as an anchor, because
the same sentence appeared in both the before and the after text. The
patch then refused rather than writing something wrong.

## VERIFIED VS CLAIMED

Verified in this session:

- `test_status_lines.py`: 19 status lines to 26 to 28, none malformed.
- The provenance scanner: Tier-1 never rose across five runs. Two Tier-1
  findings Claude introduced were caught in the sandbox and fixed before
  delivery; a third, introduced by a docstring reword, was caught the
  same way.
- `ledger_index.py`: 324 L-blocks, no consistency problems, up from 321.
- The Earth scene geometry checker: FAIL at `29bc1bd0` reading three
  white outlines, PASS after the repair reading four.
- The live store-drift run: 58 pointers, 48 match, 0 DRIFT, 0 UNIT
  MISMATCH, 10 not examined -- the figure predicted in the config patch's
  own docstring before it was written, and matched exactly.
- Mode 5, by Tony, on desktop and in the gallery: belts correct in both.
- `v3.56` exists in exactly one file after the protocol patch: zero
  copies in `PROJECT_INSTRUCTIONS.md`, one in the history file.

Claimed, and NOT verified from inside this session:

- Nothing outstanding. The xvfb GUI pass was not run -- this sandbox has
  no tkinter and the orrery needs a live Horizons connection -- but Tony
  ran the render himself and reported it.

## OPEN

1. **L-322 is the next item, and it starts as a design round.** Five
   sub-questions are open and NOT ruled, (a) through (e). (a)'s own lean
   is to run after L-305, because two of its five values are the Sun's
   and Earth's poles. The sequencing and the unit-token finding are both
   filed in the item.
2. **Rename `EARTH_VAN_ALLEN_OUTER_RADII`.** Decided, not built. It
   touches the constant, the import and both uses in
   `earth_visualization_shells.py`, the pointer in the gallery config,
   and the served cache -- so it wants its own patch and its own drift
   run. The reason is not cosmetic: the name declares `_RADII`, the row
   declares `l_shell`, and if anyone ever gives `l_shell` a conversion
   factor the drift check will report MATCH on an equivalence that holds
   in one plane only.
3. **L-305 item 5**, the renderer port of Shue and Jelinek into
   `planet_visualization_utilities.py` and `gallery/feature_renderers.js`.
   Until it runs there is no magnetosphere or bow shock on the web page
   at all, and the scene checker's "no renderer for this feature key"
   warning is the expected state. Item 5 also DROPS
   `magnetic_tilt_deg=11` rather than promoting it.
4. **L-305 item 6b**, the served shape parameters, the cut angle, the
   declared conditions and the validity range.
5. **L-327 and L-328**, both new and both unstarted.
6. **(decide) L-325.** Both halves of its gap are done: the rule landed
   in 2.12 and the serving half was verified. Still OPEN because the
   patch that closed the gap deliberately did not change the status.
7. **Design record revision 3 has two known defects**, recorded in
   L-323's note rather than fixed: it rounds to two significant figures
   uniformly, superseded by the per-row ruling, and it never mentions
   item 5.
8. **A discrepancy worth a minute next time.** The Earth scene geometry
   FAIL Tony pasted at the START of this session lists three white
   outlines. A clean checkout at `eab070a9` PASSES with four. So that run
   did not come from a clean working copy at that SHA. It changes nothing
   about tonight, but the output was treated as a known-old failure on
   that basis, which was wrong.
9. **Unchanged from the 2026-09-13 handoff:** L-305 items 5, 6b and 8,
   L-318, L-316, L-319, L-313, L-314. L-322 is now item 1 above.

## TONY-ACTION ROLLUP

1. **(do)** Archive six spent patch scripts to `documentation/`. In the
   orrery: `patch_L305_item7_belt_rows.py`,
   `patch_L305_item7_scatter_rows.py`, `patch_L305_item7_strings.py`,
   `patch_L327_L328_session_20260914.py`. In the gallery:
   `patch_L305_item7_gallery_config.py`,
   `patch_L305_item7_belt_renderer.py`.
2. **(do)** File this handoff and
   `REVIEW_REQUEST_rules_vs_reasoning_20260914.md` to `documentation/`.
3. **(decide)** L-325 -- close it, or leave it open (OPEN item 6).
4. **(do, optional)** The two live defects in
   `HANDOFF_L321_crosscheck_round_20260913.md`, carried from the previous
   handoff and still there.

Written September 2026 with Anthropic's Claude Opus 5.
