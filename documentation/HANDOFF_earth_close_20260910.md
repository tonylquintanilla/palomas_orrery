# Earth exhibit closed; L-291 and L-303 DONE; two skill bumps

Built on orrery `1ee1cc617979477e7fd00d607828004f4fe957d2`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `57fd93c62606cb91ed56050885dd7ce6f3852859`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
Pushed at: orrery -- the commit carrying `patch_L291_15_close_20260910.py`
(the next session reads it from `git log`). Gallery did not move.

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-10
Type: DOCUMENTATION (review and closing patch; no code).
Protocol v3.56. Handles: L-291, L-303, L-168, L-237, L-288, L-310,
L-311, L-312.

**Supersedes** the OPEN list of `HANDOFF_earth_step3_close_20260909.md`.
**Companions:** `documentation/REVIEW_earth_close_20260910.md` (the
review, with Tony's annotations); `patch_L291_15_close_20260910.py`.

---

## STEP 0 -- Gates for the next session

- **Skill obligation.** interactive-exhibit went 1.0 -> 1.1 and
  ledger-and-session-records 1.10 -> 1.11 in `patch_L291_15`. This
  session loaded 1.0 and 1.10, which matched the repo, the install and
  the manifest before the bump. The next session confirms its loaded
  copies read 1.1 and 1.11 before exhibit or ledger work. L-310's design
  round fires interactive-exhibit, so its load is the check.
- `git ls-remote` both repos. Orrery should be one commit past
  `1ee1cc61`, or two if the spent patch was moved separately; gallery
  should still be `57fd93c6` unless a nightly ran.

## WHAT HAPPENED

- **The review found the card step already done, badly.** A card
  opening `?exhibit=earth` had been in the gallery since 2026-09-09
  12:54, made in the editor by copying the static Earth-and-Moon portrait
  card. It kept the portrait's pairing tag, so the lobby's Featured rule
  hid it on the desktop. The prior handoff said the step had not
  started.
- **Tony rebuilt the card** -- deleted the copy, New Interactive Card in
  Studio, placed and featured in the editor -- and pushed gallery
  `57fd93c6`. The first SHA he reported, `77165da`, was the orrery
  commit saving his annotated review; the round trip showed the gallery
  had not moved yet, and his screenshot at 9:52 matched the old copy.
- **Mode 5, desktop and phone, on the lobby**: eight featured cards on
  each, the interactive Earth and Moon among them; on the phone the
  static pairs appear once. L-291 and L-303 closed.
- **Two controls existed and were not found**: Studio's New Interactive
  Card button (cause not established) and the editor's File > Reload
  from disk. Both recorded in L-288.
- **L-310's prior art, from Tony**: Studio's pan/zoom arrows. Read at
  `57fd93c6`, they are a full D-pad for 2D, a 15-degree rotation for
  polar, and reset-and-zoom only for 3D, withdrawn because the arrows
  had no detectable effect there. Recorded in L-310.

## WHAT `patch_L291_15` CHANGED

| File | Change |
|---|---|
| `LEDGER_CONSOLIDATED.md` | L-291, L-303 DONE; L-311, L-312 opened; L-237, L-288, L-310, L-168 amended; header stamp |
| `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md` | v29; Section 5a 2026-09-09/10; two handoff locations corrected |
| `skills/interactive-exhibit/SKILL.md` | 1.1 |
| `skills/ledger-and-session-records/SKILL.md` | 1.11 |
| `PROJECT_INSTRUCTIONS.md` | v3.56; v3.53 moved down |
| `documentation/PROJECT_INSTRUCTIONS_HISTORY.md` | receives v3.53 |
| `documentation/HANDOFF_earth_close_20260910.md` | this file |

## OPEN, IN ORDER

1. **L-310, the camera-step design round** -- Tony's pick, zero code,
   works from the phone. Start from its 2026-09-10 bullets: a 3D step
   moves the camera eye, not the ranges; three control sets exist
   (L-285).
2. **L-311** -- serve Earth's rotation period (derived from the store's
   IERS rate) and obliquity; the axis hover states them. Both repos.
3. **L-305** -- the magnetosphere on Jelinek et al. 2012; its own design
   session first.
4. **The plan's order**: L-237 (re-cut Artifact 1's record, now with the
   planetocentric test), step 4 the transport, step 5 Jupiter and
   Saturn. Whether Earth's slice of L-268 is done is unrecorded.
5. **When Studio or the editor is next open**: L-288's findings and
   L-312 (the copy defect, two files on one card, two titles).

## TONY-ACTION ROLLUP

1. **(do)** Run `patch_L291_15_close_20260910.py` (orrery root, Run).
2. **(do)** Run `skills_index.py` (Run). It rewrites the manifest rows
   to 1.1 and 1.11.
3. **(do)** Copy `PROJECT_INSTRUCTIONS.md` to
   `documentation/project_instructions_v3_56.md` (File Explorer: copy,
   paste, rename). Do this after step 2 so the archive holds the new
   manifest.
4. **(do)** Run `ledger_index.py` (Run). It moves L-291 and L-303 to
   section C and adds L-311 and L-312 to the board.
5. **(do)** Move the spent patch into `documentation/`.
6. **(do)** GitHub Desktop: commit, push; report the orrery SHA.
7. **(do)** Reinstall interactive-exhibit and ledger-and-session-records
   (Settings > Skills).
8. **(do)** If this Project's instructions carry the protocol text,
   replace them with v3.56.
9. **(do, later)** Retype the two portrait titles when the editor is
   next open (L-312 carries them).

## WHAT THIS SESSION LEARNED

- **Check a step against what it produces.** "Step 7 not started" was
  a claim; `gallery_metadata.json` was the fact, one read away.
- **"We need a button" can mean "the button could not be found."** Both
  controls Tony asked about or missed already existed.
- **A replay on served data predicts; it does not accept.** It named
  both screens correctly, and still waited for Tony's eyes -- which
  first saw the site serving the old file, because the push had not
  landed.

Written September 2026 with Anthropic's Claude Opus 5.
