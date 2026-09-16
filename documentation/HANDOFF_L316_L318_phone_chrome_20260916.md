# The phone's chrome settles: the drawer, the text box and the tap

Built on orrery `cce6a933216f2d21b8abfabbc48781faa4b5fe92`
at https://github.com/tonylquintanilla/palomas_orrery
Gallery at `52e953a71630fe2aa616a962cbba59aad56a3fcd`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

The session opened at orrery `04e385f3` and gallery `97867f3e`, both read
back with `ls-remote`. The orrery moved once, to `cce6a933`, when Tony
filed the previous handoff. The gallery moved five times: `c730a6ab`,
`29614e5`, `a4ef8cfc` (with a nightly run), `082dff59`, `52e953a7`. Every
HEAD was read back with `ls-remote`. After Tony pushes this session's
ledger patch the orrery moves again; that SHA is his to report.

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-15 to 2026-09-16
Type: BUILD + DOCUMENTATION. Six gallery patches, one orrery documentation
patch.
Handles: L-316 rounds 3 and 4, L-318 rounds 3 to 6, L-231, L-305, and two
new items, L-331 and L-332.
Continues `HANDOFF_L231_L305_magnetosphere_and_belts_20260915.md`, and
corrects it in four places (below). Does not supersede it: its STILL OPEN
list for L-305, L-322 and L-061 still stands.

---

## STEP 0 -- before you do anything

1. `git status --porcelain` in both repositories. Expect nothing.
2. `git ls-remote` both. Expect gallery `52e953a7`, and the orrery at the
   SHA Tony reports after the ledger patch.
3. Version-check every skill at load. This session read and matched
   `interactive-exhibit` 1.2, `ledger-and-session-records` 1.11,
   `safe-file-editing` 1.11 and `agentic-pre-test` 1.2. **The
   interactive-exhibit skill is now stale** about the rooms' chrome:
   read L-316 and L-318 in the ledger before touching the drawer, the
   text box, the arrow cross or tapping. L-332 is the skill bump.
4. If a maintenance run is pasted at the start, check which one it is.
   This session opened with a pasted run that was the PREVIOUS session's
   opening run. It showed six gating checkers where the committed runner
   has seven, and that was the tell.

---

## WHAT HAPPENED

The previous handoff left three interface changes ruled and unbuilt. All
three were built, and the phone kept showing the next thing, so the
session went six rounds on the rooms' chrome, each one checked on Tony's
phone before the next was built.

1. **The arrow cross** moved to the bottom left, as ruled (L-316 round 3).
   Later, once the text box no longer opened beside its marker, it went
   back to the top right (round 4), where Tony found it "a more intuitive
   and elegant view".
2. **The drawer row** was hard to hit. The selection box was 18 pixels,
   and every pixel around it belonged to the name, which did what GO did.
   The row's left end is now a 65-pixel target, rows are 44 pixels tall,
   and GO on an unticked shell ticks it (L-318 round 3). The backdrop now
   closes the text box as well as the drawer.
3. **Text boxes broke mid-sentence** because the text was wrapped twice,
   for the desktop and again for the phone. Breaks that only keep a
   desktop line short are now soft, and the phone rejoins them (round 4).
   That removed the orphan words but made the boxes only a line or two
   shorter.
4. **Tall boxes were cut off** at the side or bottom of the phone, and
   sometimes Plotly drew no arrow. On a portrait phone the box now has no
   arrow and sits mid-view (round 5). The desktop is unchanged, on Tony's
   word.
5. **Without the arrow, tapping a marker was trial and error.** Plotly's
   3D tap takes the nearest drawn point within 10 pixels from every
   trace, and a shell's text-less dots usually win. On a portrait phone
   they are now left out of the search, and the search is 22 pixels
   (round 6). Tony: "always opens on first tap. much improved."

---

## WHAT TONY RULED

- **The drawer keeps its box and GO.** Tick several shells, then go to
  one. The earlier idea of a one-target row with no box, and the "move
  the view only when the shell is too big" rule made for it, are
  withdrawn. Five rulings on the row, each "yes" -- see L-318 round 3.
- **GO on an unticked shell ticks it.** This amends L-267's G2 in that
  one case; GO still never hides anything.
- **A tap outside the drawer closes the drawer and the text box.**
- **On a phone the text box has no arrow.** "It is very useful but it is
  not indispensable." Start there and see how it reads; it read okay.
- **Leave the desktop as it is**, for the text box and for tapping: "the
  mouse pointer is fine enough to pick out the marker."
- **The arrow cross goes back to the top right**, and the open drawer
  still hides it ("it's okay as-is").
- **Both parts of the tap fix, phone only.**
- **Jupiter's orrery belt builder can wait** for Jupiter's room (L-231).
- **The Galactic Tide should be correct now**, because the Sun room is a
  built interactive -- "but declared not measured means little to a
  visitor." The caveat stays beside the number, in plain words (L-331).
- **A standing rule: "In general we should avoid compressed language in
  the hovertext."** Project vocabulary ("served", "sourced", "drawing
  choice") and capitalised labels ("DECLARED", "A DRAWING LIMIT",
  "FROZEN") are compression. The rule changes the words, not the facts or
  the caveats (L-331).

---

## CORRECTIONS TO THE PREVIOUS HANDOFF

- **Change (a) was the arrow cross, not the navigation cluster.** Tony's
  words were "move the arrow cross to the bottom left above the drawer."
  The + and - buttons were never in question.
- **The frame HUD comment was not stale.** The cluster is on the left, at
  the top. The previous handoff suspected it without opening
  `nav_cluster.js`. It also said the page had one rule about the cluster;
  the page decides when the cross moves, so both files change.
- **The drawer row had two targets, not three.** "go" was a label, and
  the name and GO ran the same code.
- **Change (c) is wider than one sentence.** Both rooms' info text still
  says the sources are in the hover, and four Sun hovers never moved
  their citations to the panel. That is L-331.

The previous session read the first, second and fourth and agreed; the
third was found after.

---

## VERIFIED VS CLAIMED

Verified inside the session:

- Every gallery patch ran on a clean copy of the pushed tree and refused
  a second run; the drawer patch also refused to run before the cross
  patch.
- The gallery's own checkers after every patch. Because none of them
  exercises the chrome, four stand-in pages ran the page's own functions:
  the cross (21 checks), the drawer (25), the text box (16) and tapping
  (22). Each fails on the tree before its patch.
- The desktop's text box is the same object as before round 5, and all 68
  desktop hover boxes are unchanged, line for line, by round 4.
- Every Plotly behaviour the fixes depend on was read from plotly.js
  2.35.2's source, the version the page loads: how `<br soft>` is split,
  and the pick pass (radius, nearest pixel, hover-skip dropped
  afterwards). Why Plotly sometimes drew no arrow was NOT pinned down;
  round 5 removed the arrow on the phone instead.
- The Jupiter disagreement (L-231) and the four Sun hovers and the
  checker that misses them (L-331), in the files at the SHAs above.
- `ledger_index.py` on the patched ledger: 327 blocks, no consistency
  problems.

Claimed and NOT verified from inside the session:

- Every render. The sandbox has no WebGL and no phone. Tony ran each
  round on his phone and reported, and his words are in the ledger.
- The previous session's build (magnetosphere, belt plane, hover-to-panel)
  is recorded in L-231 and L-305 from its handoff, marked as such.

---

## THE LESSON

**Measure before you describe.** Twice this session a plausible
explanation was only partly right. Tony's reading of the text boxes --
unnecessary line breaks -- was right about the orphan words, but
measuring showed they cost one or two lines, and the width was the real
height. And I wrote before-and-after line counts into the soft-break
patch's notes before running anything; the run disagreed with every one,
and the notes were corrected before delivery. The tap fix went the other
way: the cause was read from Plotly's source first, and the fix worked on
the first phone test.

A second one, the previous session's lesson again: **a checker passes on
what it does not look at.** The hover budget suite said every hover
points at the i panel. It never builds the Sun room, where four do not.

---

## STILL OPEN

1. **L-332** -- bump the interactive-exhibit skill to 1.3 first.
2. **L-331** -- the visitor text, the four Sun hovers, adding the Sun
   room to the hover budget suite, and a plain-language pass over every
   hover the gallery builds. The Sun room is live, so this should be
   next. Counted at gallery `52e953a7`: "served" in 14 hovers, "sourced",
   "drawing choice" and "illustrative" in 5 each, capitalised labels in 4.
   Proposed wording for the Galactic Tide: "Drawn at 50,000 AU
   (7.48e+12 km): a point chosen for the picture, midway between the
   Hills cloud and the cloud's outer edge. It is not a measured
   distance." All reworded hovers go to Tony before they ship. The Moon's
   hover (the assembler's `render_orbits.py`) and the orrery's hovers
   (L-321) are where the rule reaches next.
3. **L-231** -- Jupiter's orrery belt builder waits for Jupiter's room,
   and that build must do it before the room ships.
4. **Close L-316 and L-318?** L-316 still wants the desktop title and
   cross looked at on their own.
5. **Carried, unchanged:** L-330 (the belts' shape), L-322 (reading a
   constant's unit from the store's own line, which also clears most of
   the store-drift report's 13 unexamined pointers), L-061, and the
   previous handoff's STILL OPEN item 3: lower the hover budget ceiling
   from 17 when the tallest hover comes down. It is still 17.

---

## WHERE THE KNOBS ARE (gallery `52e953a7`)

- `interactive.html` line 2539, `SUN_LABEL_WRAP_CHARS = 34`: characters
  per line in the drawer's text box, phone and desktop.
- Lines 2540-2541, `SUN_LABEL_PHONE_X` and `SUN_LABEL_PHONE_Y`, both 0.5:
  where the phone's box is centred. For x, 0 is left and 1 is right; for
  y, 0 is the bottom and 1 is the top.
- Line 2543, `SUN_LABEL_FONT_PX = 12`.
- Line 2736, `SUN_PICK_RADIUS_PX = 22`: the phone's tap search.
- `gallery/nav_cluster.js` line 147, `.nav-cross-apart`: the corner the
  phone's arrow cross sits in.
- `gallery/feature_renderers.js` lines 169-170, `HOVER_WIDTH` and
  `SOFT_BR`.
- `documentation/smoke_hover_budget.js` line 57, `CEILING = 17`.

Line numbers move with every patch; search for the names. The line
numbers given in chat before round 6 are five lower than these.

---

## TONY-ACTION ROLLUP

1. **(do)** In the orrery, run `patch_L316_L318_ledger_and_plan_20260916.py`,
   then `python ledger_index.py LEDGER_CONSOLIDATED.md` (expect 327
   blocks, no problems), push, and report the SHA.
2. **(do)** File this handoff to the orrery's `documentation/`.
3. **(do)** Archive spent patch scripts to `documentation/`: in the
   gallery, `patch_L316_4_cross_top_right_again.py` and
   `patch_L318_6_phone_tap_picking.py`; in the orrery,
   `patch_L231_dashboard_hover_budget.py` and, once run, this session's
   ledger patch.
4. **(do)** If you downloaded `patch_L331_drawer_row_targets.py`, delete
   it. It is a leftover from an abandoned attempt, was never run, and is
   in neither repository.
5. **(decide)** Delete the two withdrawn, never-run patches archived in
   the orrery's `documentation/`: `patch_L231_belt_plane_amendment.py`
   and `patch_L330_belt_plane_ledger_item.py`. Both sessions recommend
   it; the patch that replaced them names them in its own notes.
6. **(decide)** Close L-318. Close L-316 after a look at the desktop's
   title and cross.
7. **(decide)** The reworded hovers, starting with the Galactic Tide's
   (L-331).

---

Session written September 2026 with Anthropic's Claude Opus 5.
