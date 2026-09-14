# The 2.12 bump, taken before the build it serves

Built on orrery `2f1a0c2f03a15927a6667bf4297f2a07991bfdfe`
at https://github.com/tonylquintanilla/palomas_orrery
Gallery at `eab070a94e53296c05b384eb342085884ef56341`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

The session opened at orrery `bfc0505e` and pushed twice:
`047d676d` (the bump, the protocol entry, the ledger row) and
`2f1a0c2f` (the L-325 Gap correction). Both round trips confirmed by
`ls-remote`. The gallery did not move.

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-14
Type: DOCUMENTATION + BUILD. Three patch scripts, zero application code.
Protocol v3.58. Handles: L-326, L-325, L-321, L-305.
Continues `HANDOFF_L321_crosscheck_round_20260913.md`, which it does not
supersede -- that file remains the session record for the cross-check
round, defects and all (see OPEN item 6).

## STEP 0 -- Gates for the next session

- **Confirm the loaded `provenance-discipline` reads 2.12 BEFORE any
  provenance work.** This session bumped 2.11 -> 2.12 and its own
  loaded copy stayed at 2.11 to the end: re-read from disk after Tony
  reinstalled, same md5 (`5c163d28`) as before the patch. That is the
  documented architectural limit, not a mistake anyone made. The
  manifest now reads 2.12, so a session whose loaded copy reads 2.11
  has a live stale-skill mismatch and STOPS.
- Version-check `ledger-and-session-records` and `safe-file-editing` at
  load as usual. Both read 1.11 and matched the manifest this session.
- `git ls-remote` both repos. Expect orrery `2f1a0c2f` and gallery
  `eab070a9`. If either has moved, read what landed before building.
- Three spent patch scripts sit in the orrery repo ROOT and belong in
  `documentation/` (rollup item 1).

## WHAT HAPPENED

1. **The session opened on a review of a patch that had already run.**
   Fable reviewed `patch_L321_handoff_bump_first.py` against the
   handoff as delivered in that conversation and recommended not
   running it. The repo pull settled it: the patch was in at
   `bfc0505e` ("L321 handoff fix", 2026-09-13 23:33), and the filed
   handoff is byte-identical to the uploaded copy. A reviewer without
   repo access cannot tell a pending patch from a spent one.
2. **Its two substantive findings were real, and are live in the filed
   handoff rather than pending.** Item 5 says the Gemini Flash 3.8
   returns are deliberately not filed, while rollup item 2 still lists
   `gemini-flash-3-8` among the slugs to file. And "only the Pro ones
   are" filed was false at the moment the handoff describes, because
   nothing was filed yet. Tony's ruling, 2026-09-14: the Flash returns
   were not responsive and are deliberately unfiled. The rollup slug
   is the stale half.
3. **Its third finding resolved against the repo.** The claim that
   draft note 3 was false when written is checkable: note 3 is A Link
   Is an Object, Not Text, and `patch_L321_correct_link_lesson.py` --
   filed and run -- names the falsification in its own WHY block.
   Fable did not have the draft. Its line-count correction was right:
   1711.
4. **`provenance-discipline` 2.11 -> 2.12** via
   `patch_L321_provenance_2_12.py`, nine edits, one file. The five
   L-321 method rules and L-325's parked Gap rule.
5. **One addition beyond the reviewed draft.** Draft notes 1 and 5 both
   used "DISCOVERY row" as established vocabulary and the skill never
   defined it -- the term lived in the L-321 worksheet prompt and never
   travelled. Worksheet Types therefore also gained the `[CITATION]` /
   `[DISCOVERY]` definitions and the ten-column schema the three
   worksheets ran, transcribed from
   `documentation/L321_slice1_prompts_rev3_20260912.md` and the
   worksheet tables rather than composed.
6. **Protocol v3.58, ledger L-326, v3.55 moved down** via
   `patch_L326_protocol_v3_58.py`. The v3.55 block was MOVED, not
   retyped: the script cuts those bytes out of `PROJECT_INSTRUCTIONS.md`
   and inserts them into `PROJECT_INSTRUCTIONS_HISTORY.md` PART 1, so
   the two copies cannot drift.
7. **A false claim, written and corrected the same day.** See below.

## VERIFIED VS CLAIMED

Verified in this session:

- `skills_index.py` reported "manifest said 2.11, SKILL.md says 2.12"
  and regenerated the zone. Both fingerprints in the second patch hash
  OUTSIDE the generated zones; confirmed by computing them before and
  after `skills_index.py` and getting identical values.
- `ledger_index.py`: 321 L-blocks, no consistency problems, 193 live
  items. Baseline before L-326 was 320.
- Two push round trips, both HEADs read back by `ls-remote`.
- The gallery serves 10.25 and 13.51 at
  `/features/earth/earth_magnetosphere/magnetopause/standoff/value` and
  `.../bow_shock/standoff/value` at `eab070a9`; the live Store drift run
  against orrery `047d676d` reports 53 pointers, 48 match, 0 DRIFT, 0
  UNIT MISMATCH, 5 not examined.

Claimed, and NOT verifiable from inside this session:

- That the account install now reads 2.12. Tony uploaded it. The copy
  this conversation loads still reads 2.11. Discharging this is STEP 0.

## THE LESSON OF THIS SESSION

**A handoff sentence transcribed into the ledger without checking the
artifact.** `patch_L326_protocol_v3_58.py` rewrote L-325's Gap and
carried one sentence straight out of the 2026-09-12 handoff: that
L-305 item 6 still served 10.0 and 12.5, so the live drift check
reported 2 DRIFT. It served 10.25 and 13.51 and reported 0. The
sentence was already false when it was written, and Tony's own live
gallery run falsified it within the hour.

This is Fetched vs Recalled one layer out from where that rule usually
fires. The recalled source was not training memory but a handoff --
which the protocol already classifies as a CLAIM, below the repo and
the render. Corrected at `2f1a0c2f` by `patch_L325_gap_correction.py`,
which records how it got in as well as what it should say.

A second, smaller instance in the same session: the first patch's own
console output said "expect 317 L-blocks parsed" when the baseline was
320. Caught by running `ledger_index.py` on a throwaway rather than by
reading the number.

## OPEN

1. **L-305 item 7 -- the citation job. This is the next session's
   work**, after STEP 0's skill check. Four belt scalars, the
   magnetotail row at 220, the outer peak's unit, and the four typed
   extents becoming interpolations. The 2.12 bump was taken to serve
   exactly this, which is why it went first.
2. **Design record revision 3 -- the item most at risk of being
   missed**, because item 7 reads the design record and not this
   handoff. It needs ruling B's lost premise, the four extents now
   sourced, row 9's reversal, and the magnetotail at 220.
3. **(decide) L-325's status.** Both halves of its Gap are now closed
   -- the rule landed in 2.12, and the serving half is verified above.
   The item is still OPEN and the patch deliberately did not change
   that.
4. **(decide) Design ruling B** -- keep L, or move the store to
   geocentric Earth radii now that three open sources state it that
   way. Carried unchanged from the 2026-09-13 handoff.
5. **(decide) Standoff precision.** Fable High: the fit supports "about
   10", with 10.25 living in the store as the evaluated model value.
   The same question stands for 13.51. Carried unchanged.
6. **The two defects in the filed 2026-09-13 handoff are still there.**
   The `gemini-flash-3-8` slug in rollup item 2, and the tense of "only
   the Pro ones are" in item 5. Both are now historical-record defects
   in a document the next session may read; neither blocks anything.
7. **Deferred with a home**, carried unchanged: three of GPT's sources
   remain without an address (Urbar et al. 2019, Ingale et al., Kumar
   and Pulkkinen 2025), none load-bearing; and the two altitude pairs
   (1,000-6,000 km and 13,000-60,000 km) rest on a magazine article, a
   news article and a university outreach page, and are item 7's to
   dispose of.
8. **Unchanged from the 2026-09-13 handoff**, with statuses re-read
   from the ledger at `2f1a0c2f` rather than copied forward:
   **L-305** items 5, 6b and 8 (OPEN), **L-322**, **L-318**, **L-316**,
   **L-319**, **L-313**, **L-314** (all OPEN). Two corrections to that
   list: **L-315 is DONE** as of 2026-09-11 and should not have been
   carried as open, and **L-305 item 6 is verified landed** per the
   drift run above.

## TONY-ACTION ROLLUP

1. **(do)** Archive three spent patch scripts from the repo root to
   `documentation/`: `patch_L321_provenance_2_12.py`,
   `patch_L326_protocol_v3_58.py`, `patch_L325_gap_correction.py`.
2. **(do)** File this handoff to `documentation/`.
3. **(decide)** L-325 -- close it, or leave it open (OPEN item 3).
4. **(decide)** Design ruling B (OPEN item 4).
5. **(decide)** Standoff precision (OPEN item 5).
6. **(do, optional)** Correct the two live defects in
   `documentation/HANDOFF_L321_crosscheck_round_20260913.md`
   (OPEN item 6). Say the word and it is a one-edit patch.

Written September 2026 with Anthropic's Claude Opus 5.
