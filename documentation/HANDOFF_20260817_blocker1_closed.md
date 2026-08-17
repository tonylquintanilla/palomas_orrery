# Handoff -- 2026-08-17 -- blocker 1 closed, the runner learns to speak, and the scanner learns six units

**Built on `ce84f05f4501a009c1b19072996c1f180e6735f9` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**
Confirmed by live `git ls-remote`. Gallery repo untouched at
`3d10739b097e2b63395cf58742873cf378210e68`.

Type: **BUILD.**
Companion to `HANDOFF_20260816_review_and_chromosphere.md` and its
addendum, which record the first half of this work. Where they
disagree with this one on a SHA or a count, this one is later.

Lands in `documentation/`.

---

## OBLIGATIONS THE NEXT SESSION MUST DISCHARGE FIRST

Two, and neither can be cleared from inside the session that created it.

**The protocol was re-uploaded to the Claude project twice during this
session.** A project-knowledge update binds at conversation start, so
the running session kept working from v3.40 and could not read what
had landed. The next session confirms which protocol version it
actually loaded before treating any of it as current.

**Nothing else is outstanding on the skill layer.** Both
`safe-file-editing` and `orrery-coding-conventions` were confirmed at
1.4 at the start of this session, discharging the obligation the
2026-08-16 handoff carried. No skill was bumped here.

---

## What closed

**Blocker 1 of nine, completely.** A citation too long for one line
continued on a second line the request builder could not see, so the
worksheet quoted half a citation and asked a person to verdict it.
Marked, joined, ratcheted:

| Stage | What | Where |
|---|---|---|
| Mark, stage 1 | 96 lines, 7 corpus files | `patch_L196_1` (prior session) |
| Mark, stage 2 | 152 lines, 18 files | `patch_L196_13` |
| Join | builder reads `# Source+:` | `patch_L196_8` |
| Refuse | builder blocks on unmarked | `patch_L196_15` |

At HEAD: **100 rows over 52 sites, 153 continuation lines joined, zero
unmarked, zero malformed.** Full detail in ledger **L-196**.

**Blocker 9** was already closed by the chromosphere retirement. Seven
of nine remain: 2 and 6 have rulings and no build; 3, 4, 5, 7 and 8 are
open.

---

## What else landed

**L-197 -- the maintenance runner says what passed.** Four rows were
reporting side effects as verdicts and five ended in an ellipsis.
Three separate causes, one per row family: a verdict written to stderr
where the runner reads stdout; a correct verdict buried by an atexit
cleanup two lines later; and plain truncation at 44 characters, now
wrapped rather than widened. Plus hover text on all 41 dashboard Launch
buttons naming the repo and file each one runs.

**L-198 -- the scanner learns six units.** Ten annotated sites were
producing zero worksheet rows: the claim pattern knew `solar radii` and
`Earth radii` but not `Mars radii`, knew `km` but not `kilometers`, and
could not see across `million`. A second defect in the same pattern made
every percentage followed by a space invisible. Widened, measured on the
whole tree: **728 matches gained, 16 lost, all 16 false positives**
(percent-encoded URLs and `%s` placeholders), no real claim lost.

---

## Numbers that moved, and one that will surprise you

| | Before | After |
|---|---|---|
| Scanner Tier-1 | 206 | **289** |
| Checker | 59/102 routed, 3 clean | 68/110 routed, 8 clean |
| Dispatch | 64 rows / 42 sites | **100 rows / 52 sites** |
| Continuation lines joined | 0 | **153** |
| `EXTRACTOR_VERSION` | 1 | **2** |

**Tier-1 rising by 83 is not a regression.** Those are unsourced
numeric claims that were always there and were not being counted,
because the scanner could not see the number at all. The count did not
get worse; it got honest. The push gate reads Tier-1 on the ACTIVE
BUILD PATH, not the tree total.

---

## Rulings, in order

1. **Corpus-only for the loud failure**, not whole-tree. A file enters
   the corpus when it gains a `# Cross-checked:` line, and the refusal
   fires at the next build -- still before any worksheet is made from
   it. Whole-tree buys earlier notice at the cost of a permanent
   exemption list.
2. **Widen the claim vocabulary now**, not after the pilot. Taken after
   the re-pointing risk was measured rather than asserted: no worksheet
   has ever been issued, none of the 35 on disk carries a key, and not
   one pinned key carries an ordinal.
3. **Close the documentation for completed work** before the session
   ends. This handoff and ledger L-196 through L-198.

---

## Nine patch scripts, one naming note

`patch_L196_8` through `_16`. They all carry `L196` because they were a
running sequence, not because they belong to one handle: `_9` through
`_12` are L-197 and `_14` is L-198. The names are left alone -- they are
archived and pushed, and renaming them would break the only link between
the scripts and their run order. The ledger blocks carry the map.

---

## Open items

**Tony-action (decide)**

- **The pilot slice.** Both August reviewers required a small pilot
  before the full corpus, chosen to force every structural branch --
  including at least one row that should route SEND BACK and one to
  CONVERSATION. Needs a design conversation, not a patch.
- **Should a mismatched marker also refuse?** It currently reports. The
  distinction drawn was visibility: a mismatch prints into the
  worksheet where the responder reads it; an unmarked continuation
  appears nowhere. Recorded in L-196 as Claude's call, open to reversal.
- Carried unchanged from 2026-08-16: the lazy responder (Fable wants
  disclosed canaries, GPT wants the code value hidden -- not
  compatible), claim typing, cross-worksheet disagreement, what UNKNOWN
  does, the pluto 614/638 merge, transition sequencing, whether batching
  becomes real.

**Claude-side, ready to build, no ruling outstanding**

- Six Shape A swaps, `constants_new.py` roughly 195-277. This is what
  remains of **L-195**; its Gap was narrowed accordingly.
- Ordinal context window: excerpt around each claim's offset rather
  than the whole string truncated to 90 characters. Blocker 7, and it
  matters more now that the dispatch is 100 rows.
- Print the seven verdict tokens in the request. Blocker 8.

**Known and not fixed**

- Eleven of thirteen checker rows still resolve their verdict by last
  line, so any of them can be displaced by a print that arrives later.
  Giving every row a hint is the general cure. Recorded in L-197.
- `info_dictionary.py` holds ten non-ASCII characters inside strings
  the reader sees -- superscripts in `g/cm3` and `m/s2`, em-dashes in
  prose, and the surname Wierzchos. Rewriting them changes what a person
  reads and misspells a name, so it is a content decision and was left
  alone. The stage 2 patch reports them on every run.
- `constants_change_report.py:17` still names `CHROMOSPHERE_RADII` in a
  docstring example. Harmless, reads as live. Carried from 2026-08-16.

---

## Process record: what did not survive checking

Four defects of Claude's, and the pattern in them is worth more than
the list.

1. **A sweep that compared a pattern against itself.** The first
   false-positive measurement for the widened claim regex reported zero
   differences -- because it put the repo on the path ahead of the
   sandbox and loaded the OLD scanner. A clean result that could not
   have been anything else. Caught only because zero contradicted a
   count taken a minute earlier. The rerun asserts the two patterns
   differ before comparing.
2. **A rule that could not fail, shipped as far as the sandbox.** The
   unmarked-continuation detector has two parts: padded lines are
   continuation, unpadded labelled lines are labels. Deleting the
   padding rule left all 41 tests passing, because the label pattern
   allowed only one space after the `#` and was already rejecting
   padded lines by itself. Found by a mutation expected to break
   something that did not. The label pattern was loosened so the
   padding rule decides the case it is documented as deciding.
3. **A cause asserted from one site.** The ten silent sites were first
   attributed to ranges, hedged but stated, from reading one string
   without checking the others. The actual cause was the unit
   vocabulary. Establish WHAT differs before saying WHY -- the same
   lesson the fingerprint field note already carries.
4. **A choice offered without measuring it.** "Widen now or dispatch
   now" was put to Tony as a risk trade before the risk had been
   measured; his answer was that he had no way to assess it, which was
   correct and was the failure. Measuring took four minutes and made
   the answer obvious.

**What caught them.** One by a contradiction between two of Claude's
own numbers, one by a mutation test, one by Tony asking a plain
question, one by Tony saying the message was opaque. Not one was caught
by a passing check. That is the same ratio the 2026-08-16 handoff
recorded, and the same conclusion: checks get built after the failure,
not before it.

**What the checks did catch.** Every patch was sandbox-run from a clean
clone at HEAD before delivery, and every behaviour added was mutation
tested in both directions -- the join removed, the join made
over-eager, the run-closing reset dropped, a marker un-marked in a real
file, a failing assertion injected into the orbit cache suite, the
re-pin step broken to prove the rollback restores. The stage 2 patch's
own detector was validated by reproducing stage 1's answer set exactly:
48 runs, 96 lines, the same line numbers.

---

## For the next session, in order

1. Confirm the loaded protocol version against the repo copy.
2. Six Shape A swaps.
3. Ordinal context window and the verdict token list.
4. Design the pilot slice.

---

*Prepared August 17, 2026 with Anthropic's Claude Opus 5. Built on
`ce84f05f4501a009c1b19072996c1f180e6735f9` at
https://github.com/tonylquintanilla/palomas_orrery.*
