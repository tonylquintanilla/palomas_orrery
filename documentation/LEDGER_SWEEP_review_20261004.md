<!-- Doc-Kind: hand | Review record: a sweep of the open ledger for closes, RICE, slice grouping, and errors, written beside the L-371/Earth session of 2026-10-04. -->
# Ledger sweep, October 4, 2026

Built on orrery cbde99dc703886cb7591e7a437b7a4bf7922f8f0 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
e7ef96eb07fbdede9a270965d216511eb4949043 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Nothing was pushed by this session.

- Type: DOCUMENTATION (zero code). A review, not a patch. Every change
  below is a proposal for the session working the ledger (Opus) to
  carry into its patch, after Tony's word where one is needed.
- Companion: `documentation/HANDOFF_L371_distance_cards_session_20261004.md`
  and the uploaded `WHERE_WE_ARE.md` with Tony's notes on it.
- Skills loaded: ledger-and-session-records 1.14 (matches the manifest).
  Also read to discharge L-407: provenance-discipline 2.25,
  earth-system-pipeline 1.2, interactive-exhibit 1.10.

## How the sweep was done

- Cloned both repositories at HEAD. The orrery is at cbde99dc, three
  pushes past the d7f2a594 the uploaded page was written at; the L-371
  close patch is in `documentation/` and its edits are in the ledger.
- Ran `ledger_index.py --check` on a copy: 407 blocks, no consistency
  problems; regenerating the index changed nothing, so the committed
  index is current.
- Parsed every block with the indexer's own parser: 246 live items,
  161 closed. Read the bodies of the Sun slice, the Earth list the
  handoff names, the lobby item, and every item whose body reports
  completion. Checked claims against the code where that was cheap.

## 1. Bookkeeping: close, or correct the record

Verified by this session (ready to close):

- **L-409, the licenses.** Both GitHub pages show "MIT license" in the
  sidebar (read from github.com, 2026-10-04). Tony's page says the
  same. The Gap's one check has passed. Close.
- **L-407, skill headers as YAML.** Its Gap was for a later session to
  confirm its loaded copies. This session loaded provenance-discipline
  2.25, earth-system-pipeline 1.2 and interactive-exhibit 1.10, and
  provenance-discipline's description runs to "Do not use for projects
  other than Paloma's Orrery", past the old cut at "adding or
  reviewing". The resident protocol is v3.79. Close. (The L-371 handoff
  says "no load to confirm next session"; that was true of its own
  session's skills, but L-407's obligation from 2026-10-02 was still
  open. It is discharged here.)
- **L-350, the magnetotail's observed extent "shown nowhere".** At
  gallery e7ef96eb `gallery/feature_renderers.js` line 2714 prints it
  in the magnetotail hover: "The drawing stops at 220 Earth radii,
  which is how far the spacecraft went, not where the tail ends."
  The renderer's comment credits L-322 Stage D gallery patch 3. The
  premise is gone. Close, noting the patch. (Not checked: whether that
  hover is still inside the 17-line budget the item worried about.)
- **L-406, the galactic tide.** Built and pushed on both sides; its
  only Gap is the Mode 5 look, which waits on L-408's ring and is
  already L-408's purpose. Close, with one line on L-408 saying the
  look of the tide's X is judged there.

Close candidates needing the Opus session's read:

- **L-234, the Sun in the assembler.** Its Gap is "the EARTH half",
  listing interiors, Hill sphere, axis, dipole cone, magnetosphere as
  not served. Earth's room is live. Served Earth keys at gallery HEAD:
  inner_core, outer_core, lower_mantle, upper_mantle, crust,
  lower_atmosphere, upper_atmosphere, geocorona, magnetopause,
  magnetotail, bow_shock, leo_inner, leo_outer, geostationary_ring,
  planet_radius. NOT among them: hill_sphere, rotation_axis,
  dipole_cone (the pole is served another way under L-322 Stage D).
  Before closing: say whether those three were decided against or are
  owed, and re-home them if owed.
- **L-305, the magnetosphere model.** The handoff's first job. My spot
  checks support closing: `magnetic_tilt_deg=11` removed (2026-09-15,
  earth_visualization_shells.py line 1130); the Lugaz-midpoint
  sentence deleted; Shue and Jelinek named 34 times across the two
  orrery files; the gallery renderer draws Shue, the Jelinek cut and
  the Slavin tail. Items (4) to (8) of its Gap read as landed. Its body
  is a 3,500-character archive; A Closing Item Re-homes Its Loose Ends
  applies: L-314 (live solar wind) and L-350 both point at it.
- **L-363, the Solar System room.** Not closeable, but its Gap of
  2026-09-29 still lists Half 2 as ahead -- design round, five
  planets, cache rebuild, drawer, Mode 5 -- and every one is built.
  Rewrite the Gap to what remains: (a) the swap, a bare
  interactive.html link opening this room and the Explorer at its own
  address (the page's road stage 6); (b) the arrival block's
  `_declared` sentence, still "1.1 times the largest distance" at
  gallery HEAD (data/objects_config.json line 1304) where the rule is
  1.2; (c) the two design-talk items, with Tony's new ruling recorded
  (section 4 below); (d) the editor-words question re-homed from
  L-404. Strike as settled the two "Tony-action (decide), at Half 2"
  lines at the block's end: ticking a row opens it (the design talk of
  2026-09-30 closed it) and Apophis sits under See more (built). Re-home
  "no gating checker reads index.html's lobby code" to L-367.

Smaller corrections:

- **L-228.** Its 2026-10-04 note says Claude does the Cranmer read; the
  older "Tony-action (do): the source read" below it says Tony does.
  Strike the (do). The `flag:Tony` that puts "[Tony]" on the index row
  then goes too; the (decide) on its RICE stays.
- **L-408.** Gap says "Build it next session, with the Sun's distance
  cards (L-371)". That session is over and L-408 was not built. It is
  the Sun slice's eighth item; say so.
- **L-412.** Gap "work down the list" -- Tony's note on the page puts
  Earth's list first. Record that.
- **L-216.** The 2026-10-04 Tony-action (do), delete the stray folder,
  is done by Tony's note on the page. Mark it.
- **`upd` not moved.** The L-371 close patch wrote 2026-10-04 notes
  into L-386, L-241, L-128, L-131 and L-136 and left their `upd` at
  2026-09-28, 08-25 and 07-17. L-406 carries 2026-10-03 notes under
  2026-10-02. The index sorts and ages by `upd`, so these read as
  untouched. Six items, one class.
- **Ledger header stamps.** The header's last "Module updated" line is
  the lobby-card session at a841ab6e. The L-406/L-407 pushes of
  2026-10-02, the L-371 patches of 2026-10-03 and the L-371 close of
  2026-10-04 added none. This matters for L-396: its candidate check
  compares the page's date against the ledger's newest stamp, and a
  stamp that lags makes that check pass on a stale page.
- **Section placement.** L-131 (dust cloud) and L-128 (comet ice lines)
  sit in D.Feature-B while L-412 has them as the Sun slice's items 9
  and 10. Move both to section A. L-136 stays in D.Feature-B with a
  Ref to L-363 (the Solar System room).
- **Status words.** L-308 (Gap: "none until the trigger fires") and
  L-068 (umbrella; "none of its own") are OPEN, so the index marks them
  as gaps. DEFERRED fits L-308; L-068 is tracking only.

## 2. RICE

- **67 of 246 live items are unscored, and all of them are L-343
  onward (from 2026-09-22).** Scoring stopped when the slices started.
  The index puts unscored items last, so L-363 and L-371 -- the two
  most worked items of the month -- sit at the bottom of section A
  under items nobody has touched since August. Two ways out, Tony's
  choice:
  - (decide) rule that an item inside an ordered slice (L-412 and the
    lists like it) needs no RICE, since the master plan's sequencing
    already outranks the score (ledger-and-session-records, L-221), and
    give the rest a coarse score when they are next opened; or
  - score all 67 now, which costs a session.
  Claude's recommendation is the first; the skill then carries it as
  method.
- **Three high scores that no longer mean "do this next".** L-252
  (11.4) has "Gap: none in the tool" and one unruled vocabulary
  question -- a G-section open question, not a 11.4 build. L-235 (11.4)
  and L-237 (10.8) are real but 40 days untouched; they belong in the
  gallery-checks group below, where their Effort falls. Re-score or
  re-section L-252; leave L-235 and L-237 for the grouping.
- **Two low scores inside the active slice.** L-131 and L-128 are
  2/2/50/2 = 1.0 from July, scored as loose ideas. Both now have a
  design talk scheduled (L-412 items 9 and 10), which raises
  Confidence and lowers Effort. Claude's proposal: 3/3/70/2 = 3.2 each,
  for Tony to confirm or redirect.
- **L-216 (3.8).** The fix is built and tested; what remains is
  watching the swap log for a retry, and a move off OneDrive Tony has
  declined to decide. A watch is not a 3.8 build. Either lower it or
  mark it DEFERRED with the watch stated -- Tony's call.
- Items L-228 (3.0), L-241 (3.8) and L-292 (3.4) carry Claude-proposed
  scores still marked unratified. They can be confirmed in passing.

## 3. Grouping under the braid: what belongs together

Two slices exist. A third group is visible and has no list.

- **The Sun slice (L-412).** Ordered; this sweep's bookkeeping is in
  section 1. Tony's note moves it behind Earth's list.
- **Earth's list.** The handoff asks Opus to write it in L-412's shape
  after reading L-305 and L-292 against the code. What this sweep adds
  to that read:
  - L-350 closes now (section 1).
  - L-305 reads as done on the code; its loose ends want homes.
  - L-292's Gap STANDS. The handoff says "an exosphere shell naming the
    geocorona now exists". In the orrery it does not: Earth's shells in
    `shell_configs.py` are Inner Core, Outer Core, Lower Mantle, Upper
    Mantle, Crust, Lower Atmosphere, Upper Atmosphere and Hill Sphere;
    the geocorona is a sentence inside the Upper Atmosphere hover
    (lines 1539 and 1548). The shell that exists is the gallery's
    `earth_exosphere/geocorona` row, which L-292 already records.
  - L-369: all five typed obliquities are still there at HEAD. The
    line numbers moved: palomas_orrery.py 5842, 8073, 8891 (were 5835,
    8066, 8884); the other two unchanged.
  - L-383: the two "drawn at the flux peak" lines are now 2352 and
    2353 (were 2321 and 2322). Still waits on L-349's wording.
  - L-234's Earth half: the close candidate in section 1 is Earth's
    too, since every key it lists as unserved is served.
- **A third group with no list: the gallery's checks.** These items
  open the same files -- `gallery_maintenance_run.py`,
  `documentation/smoke_*.js`, `documentation/payload_earth_scene.json`
  -- and Cluster the Tail says that is the grouping that survives:
  - L-300: `sweep_collapsed_features.py` exists in the gallery root
    and is not registered in `gallery_maintenance_run.py` (checked at
    e7ef96eb). "One small patch" since 2026-09-07, RICE 8.1.
  - L-235: two checks that cannot fail (T5 at the wrong file; a caption
    with no comparison behind it). RICE 11.4, since 2026-08-25.
  - L-237: Artifact 1's golden record, stale. RICE 10.8. Pairs with
    L-235 by its own Gap.
  - L-262: the framing smoke test has never run against the live page.
    RICE 11.4.
  - L-367: no checker opens a new room. Unscored.
  - L-378: phone behaviour has no automated check, or a stated decision
    that it stays manual. Unscored.
  - L-379: the recorded Earth payload is aging; three checks patch it
    piece by piece. Unscored.
  - L-357: stale gallery artifacts no check reads; a (decide) on one
    fixture. Unscored.
  - L-360, L-380, L-388: the hover budget's blind spot, the export pull
    order, the pull that prints success on failure. Unscored.
  Three of these are the top of the whole board by score and none has
  moved in six weeks, which is the "correctly deprioritized or dropped"
  question the skill names. Proposal: one ordered item in L-412's shape,
  after Earth's list -- or at least L-300 and L-379 folded into the next
  gallery patch that opens the runner, since each is one small change.
  (decide) whether this becomes the third slice.
- **A fourth group that is already scattered: what each skill is owed
  at its next bump.** Carried sentences sit in L-351, L-390, L-216
  (gallery-cache-builder: the `[SWAP]` line, the run order, the empty
  "(N)" folders), L-371 (provenance-discipline's range example;
  predict the scanner's change not its total), L-363
  (gallery-pipeline's wide-card fields; ledger-and-session-records'
  rule that a patch checks Tony-annotated files by line). A session
  bumping a skill has to find them by reading five items. Proposal:
  L-351 becomes the one place, with one line per skill naming its owed
  changes by source handle. Method, not a ruling; Claude can do it.

## 4. Other errors and omissions

- **Tony's five notes on WHERE_WE_ARE.md are not in the repo.** The
  page is rewritten in place every session, so they are lost unless the
  ledger patch takes them first. They are:
  1. Earth's old items before the Sun's item 3 (to L-412's Gap).
  2. "Add ledger cleanup to the next items" -- this document.
  3. The close patches: done. The stray folder: done (to L-216).
  4. The GO arrow: "the text box needs to remain in the center. if not
     possible, don't implement the arrow." A ruling, to L-363's
     design-talk list. It also means the arrow cannot amend the L-318
     mid-view ruling, which the L-363 note had allowed for.
  5. A question, answered below.
- **Tony's question: is the scattered disk the fuzzy-boundary idea?**
  No. L-136, the scattered disk, is a population of distant icy bodies
  to draw as a region in the Solar System room, beside the Kuiper belt.
  L-410, fuzzy boundaries, is a way of drawing any edge that is known
  only as a range -- a band that fades between two sourced rows -- with
  the outer corona first. They meet only in that a scattered disk's
  edges are themselves ranges, so when L-136 is designed, L-410's
  drawing rule would apply to it. One line on L-136 saying so would
  close the question.
- **The handoff's L-292 claim** (section 3) is the one statement in it
  that the code contradicts.
- **L-363's `_declared` sentence** (section 1) was listed as a "small
  fix for the next build" on 2026-10-02 and did not ride patch_L363_14.
- **L-396's check and the header stamps** (section 1): the proposed
  check is only as good as the stamp it reads. Either the patch
  convention stamps the header every time, or the check reads the
  ledger's newest `upd` instead. Worth saying on L-396 before the check
  is built.

## Tony-actions, rolled up

- (decide) RICE: rule that slice members need no score, or score the
  67 (section 2).
- (decide) Whether the gallery's checks become the third ordered slice
  (section 3).
- (decide) L-131 and L-128 at 3/3/70/2; L-216 lowered or DEFERRED;
  L-228, L-241, L-292 scores confirmed (section 2).
- (decide) L-357's one fixture, if the gallery-checks group is taken up.
- (do) Nothing; the closes and corrections above go into the Opus
  session's ledger patch, which Tony runs as usual.

## For the Opus session, in order

1. Take Tony's five page notes into the ledger before the page is
   rewritten (section 4).
2. Close L-409, L-407, L-350, L-406 with the verifications above
   (section 1); mark L-216's (do) done; fix L-228, L-408, L-412's Gaps.
3. Read L-305 and L-234 for close with re-homing; rewrite L-363's Gap.
4. Write Earth's list, with L-292's Gap standing and the corrected
   line numbers.
5. Move the six `upd` fields; move L-131 and L-128 to section A;
   retag L-308 and L-068.
6. Put the RICE decision and the gallery-checks decision to Tony.
7. Stamp the ledger header for this close, and say so on L-396.

Session written October 2026 with Anthropic's Claude Fable 5.1.
