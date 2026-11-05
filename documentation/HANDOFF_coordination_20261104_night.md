<!-- Doc-Kind: hand | Coordination handoff, Nov 3 to 4: where L-512 (fallbacks when JPL cannot answer) stands after slice a, what the next coordinating session does first, and the threads it carries. Points at the ledger; does not restate it. -->
# Handoff: coordination, November 3 to 4, 2026

Tony Quintanilla, PE | Claude Opus 5.5 (coordinating session) | November 4, 2026, night, Chicago

Built on orrery bf10bcea9f2f067846edcef3564c2bdd8db9ddd4 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
5abca2c614f348e9183b313a6c48de310f1dfc98 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, both read
live on Nov 4, 22:55 Chicago.

Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`,
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.

Type: COORDINATION handoff, to the next coordinating session (Opus,
standard effort, chat). The ledger holds the detail; this says where to
look and what is next.

## 1. First, at the session's start

- Confirm both HEADs against the anchor above.
- List `python_work` on Tony's computer. This session had the computer
  linked but NO folder connected, and its request for one was refused
  by the app's own check, never shown to Tony. Files went to him as
  downloads. If the listing comes back empty, say so at once.
- Run, or have Tony run, `patch_L508_1_code_prompts_section.py` if it
  is not yet in `documentation/`: at bf10bcea its lines are not in the
  ledger, and it still applies cleanly there (tested on a copy). It
  carries, on L-508 (a held body's alarm), the section on Code prompts
  for ledger-and-session-records' next version, and on L-509 (obsolete
  code) the line that 6AC4721 is kept on purpose.

## 2. Where L-512 (fallbacks when JPL cannot answer) stands

- The rulings: `documentation/MAP_L512_jpl_fallbacks_20261104.md`, its
  last section (Tony, Nov 4, 12:36 to 12:56). The prompt that built
  slice a: `documentation/COORD_L512_slice_a_prompt_20261104.md`.
- Part 1 done (the path-or-orbit decision falls back to a body's typed
  elements). Slice a, part A1 done and committed at e7ea3294 (the
  saved-path writer removed; every JPL question asked fresh, checked
  over the whole repository). Part A2 done and committed at bf10bcea
  (`jpl_outcome.py`: "no such body" is told apart from "JPL
  unreachable"). Tony's look passed both, wifi off and on.
- Tony's rulings of the evening, on L-512: MK2, Xiangliu and 6AC4721
  keep their drawings from their typed elements whatever JPL answers
  (Xiangliu: Kiss et al. 2017; MK2: arXiv:2509.05880; 6AC4721: MPEC
  2026-A49). JPL answers "out of bounds" for MK2's and Xiangliu's ids,
  and their primaries' system barycentres; it knows Vanth.
- The saved-path files: gone from the repository's `data/`; copies of
  June and July kept in `python_work\orrery\archived\`, outside the
  repository. The file-absent maintenance run passed, 35 of 35.
- Carried on L-512 for horizons-orbital-mechanics' next version: A2's
  two out-of-date fallback sentences. Slice b rewrites both, so they
  ride slice b's bump.

## 3. Next: slice b

Mechanism 1 of the rulings: when JPL cannot be reached, the position
marker and the path over the plot's dates are propagated from the
committed osculating elements (`data/osculating_cache.json`), one
propagator for every orbit body; the three copies of the four-name
fallback list go; the hover says "propagated from JPL's elements of
<epoch date>"; static plot first, then the animation. Tony's look
closes it, wifi off and on. Its prompt is written by the next
coordinating session, now that it is next, in the shape that worked
for slice a: the rulings' section named, the start check, an inventory
before any removal, stops between parts, records at each part's end.
Then slice c (the committed positions record for path bodies, written
by the orrery's night).

## 4. The other threads, in the road's order

- L-484 (the two agree): its check's brief, written with
  interactive-exhibit's next version as an orrery records patch. Piece C
  of C/2025 K1 is its first open difference.
- L-510 (the typed fields stop deciding), part 2: the path plan asked
  from before any launch.
- L-511 (the export carries the words), behind the check.
- Ledger-and-session-records' next version: L-508's alarm and the Code
  prompt section ride one bump.
- Not yet looked at: the website's C/2025 K1 pieces after the night
  (piece C was expected to drop) and Psyche's path end moving to 24 Feb
  2029. The nightly build log at the gallery's HEAD shows the last
  build as 20261103T193343Z.

## 5. For the method

- A candidate on L-508 (once the patch runs): how many reviews a prompt
  gets. Slice a's prompt had six; A1's inventory then added four more
  items on its own (an uncalled dialog copy, a startup line, a skip
  list, the loader's backup restore). Settle it with Tony: did the
  reviews find anything the inventory would not have?
- Tony's run records: `WHERE_WE_ARE_11-3-26_1158_run_record.md` (Nov 3
  to 4, morning) and `WHERE_WE_ARE_11-4-26_1735_run_record.md` (Nov 4,
  slice a).

Written November 4, 2026 with Anthropic's Claude Opus 5.5.
