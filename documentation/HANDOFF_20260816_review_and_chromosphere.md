# Handoff -- 2026-08-16 -- the review that doubled the blocker list, and a stylization retired

**Built on `a872205d17ee5298d1bdc86c614b43506e82b22c`; pushed at
`86f529a3088028d6b579cae77feb73c797180013`, then
`f4043bf0b0ac5c4746f5a374d76a2b3a86b87bea`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**
Both SHAs confirmed by live `git ls-remote`. Gallery repo untouched at
`30b6968`.

Lands in `documentation/`.

---

## OBLIGATION THE NEXT SESSION MUST DISCHARGE FIRST

Two skills were bumped mid-session and **neither clears in session**.
The loaded copy appears bound at conversation start, so a reinstall
lands invisibly and Tony's word that he did it is an assertion standing
in for a check Claude cannot perform.

> `safe-file-editing` went to 1.4 at `86f529a` and
> `orrery-coding-conventions` went to 1.4 at `f4043bf`. The session that
> bumped them loaded 1.3 and 1.3. **The next session confirms its loaded
> copies read 1.4 against the manifest before doing any patch-script or
> marker work.**

Verified present in the repo at `f4043bf`: both `skills/` copies read
1.4, and the manifest zone in `PROJECT_INSTRUCTIONS.md` agrees.

---

## What this session was

It opened as a broad-reach review request and became the largest
single-session repair the dispatch loop has had. Fable 5 and GPT 5.6 Sol
reviewed the same packet blind. Both said do not dispatch. The blocker
list went from two to nine.

Everything they reported was re-verified against the pinned source
before being acted on. One GPT claim did not survive that check.

---

## Tony's rulings, in order

1. **The returned request gets its own checking path.** Bound to claims
   by key on a separate path; source annotations are NOT repointed,
   because repointing erases which worksheet the original
   `# Cross-checked:` claim referred to. The annotation is append-only.
2. **`# Resolved:` leg, carrying a ledger handle the checker verifies.**
   Third provenance kind: Source is the value's, Cross-checked is the
   check's, Resolved is the disagreement's. Dated prose alone cannot
   fail, and an unverifiable line that clears suspicion is cite-to-clear
   at a third layer. Named `Resolved` not `Resolution` because
   `resolution` is already a worksheet column role. **BUILD DEFERRED**
   to the first real disagreement, whose shape should settle whether a
   resolved dispute drops out of the action list and whether the handle
   must be closed.
3. **Truncation: explicit continuation marker, leg-specific, plus
   normalization.** Neither reviewer's shape. Marker first, then the
   builder joins on it, then the builder fails loudly on any unmarked
   continuation. Leg-specific (`# Source+:`) so a `Ref+` under a
   `Source:` is a mismatch the tool can report.
4. **Scope: all 165 sites, not the 48 in-scope ones.** Staged. A loud
   failure only works as a ratchet if nothing pre-existing trips it;
   leaving 117 unmarked guarantees the first person to annotate a new
   file weakens the check.
5. **Citation legs only** for the loud failure -- `Source`, `Ref`,
   `Also`, `See`, `Derived`, `Calculation`. A tail under `# Note:` is
   out of scope.
6. **Shape A** for the six event-as-authority citations.
7. **Retire the chromosphere stylization.** Draw at true scale; the
   invisibility is the lesson, not a defect. Legend name and info
   marker carry discoverability.
8. **L-180 stays on record and dormant**, not categorically superseded.
9. **On retirement, mark it retired** -- pins record it rather than
   losing it.
10. **Fix In Passing, Report It**, and **patch-script naming**, both
    into `safe-file-editing`.
11. **Harvest unrecorded conventions** into `orrery-coding-conventions`.

---

## What landed

| At | What |
|---|---|
| `86f529a` | Patches 1-3: 96 continuation markers in 7 files; chromosphere retired across 8 files; key retirement recorded. `safe-file-editing` 1.4. |
| `f4043bf` | Patch 4 (shared sites parser), patch 5 (protocol v3.40), `orrery-coding-conventions` 1.4. |

Five patch scripts, archived in `documentation/` as
`patch_L196_1..5`. All 12 maintenance checkers green at `f4043bf`.

**Chromosphere, verified by render:** shell at 1.002875 solar radii,
info marker at 20.00 degrees against the photosphere's 0.00, markers
0.365 solar radii apart where they were 0.003. Legend reads
`Sun: Chromosphere (2,000 km skin)`.

**Dispatch corpus 65 -> 64 rows**, zero rows with no `# Source:` leg.
Blocker 9 dissolved rather than being fixed.

---

## The nine blockers, and where they stand

| # | Finding | Status |
|---|---|---|
| 1 | 45 of 65 rows show a truncated citation | markers placed (stage 1); builder join NOT built |
| 2 | Six `# Source:` lines name an event, not an authority | Shape A ruled; swaps NOT built |
| 3 | With both verdict columns present, only the value verdict is read | open -- belongs on the new response path |
| 4 | String claims bypass the key rule entirely | open -- same |
| 5 | `shift_check()` never called by the checker | open -- same |
| 6 | Returned request not in the checker's evidence path | ruled (separate path); NOT built |
| 7 | 26 ordinal rows share 8 distinct excerpts; 3 units carry duplicate values | open, no ruling needed |
| 8 | The request never states the seven verdict tokens | open, no ruling needed |
| 9 | Builder scripted an answer for `CHROMOSPHERE_RADII` | **CLOSED** by the retirement |

---

## Open items

**Tony-action (decide)**

1. **Lazy responder.** Fable wants disclosed canaries; GPT wants
   `Value correct?` removed and the code value hidden. Not compatible
   -- one adds a detector, the other removes the affordance. Both
   confirmed the attack is real and undetectable today. Deferrable
   until after the pilot.
2. **Claim typing.** Partly dissolved with the chromosphere. Whether
   measurement / derived / design become real row types, or the
   question waits for a measured population.
3. Carried from 2026-08-15, unchanged: cross-worksheet disagreement,
   what UNKNOWN does, the pluto 614/638 merge, transition sequencing,
   whether batching becomes real.

**Claude-side, ready to build, no ruling outstanding**

- Stage 2 normalization: 117 runs, 235 lines, 23 files. Fingerprints
  must be regenerated against `f4043bf`.
- Builder marker join + loud failure on unmarked continuation. This is
  what makes the 96 stage-1 markers do anything.
- Six Shape A swaps (`constants_new.py` 195-277, a tight cluster,
  disjoint from the continuation sites).
- Ordinal context window: excerpt around each claim's offset.
- Print the seven verdict tokens in the request.

**Not yet written**

- Ledger entries: L-194 through L-196, and the L-192 as-built for this
  session.
- `constants_change_report.py:17` still names `CHROMOSPHERE_RADII` in a
  docstring example. Harmless, reads as live.

**Standing constraint from both reviewers**

A small pilot before the full 64, chosen to force every structural
branch -- including at least one row that should route to SEND BACK and
one to CONVERSATION. A run where everything is expected to pass does
not test routing.

---

## Process record: what did not survive checking

**Claude's errors, six, and only two were caught by a check.**

1. **A verification check that could not pass.** After stage 1, Claude
   scanned for remaining unmarked continuations using the scanner that
   built the original census -- which does not know `# Source+:` is a
   label. It counted every just-marked line as still unmarked and
   reported the count had risen. Caught by re-reading the result
   against what it claimed to measure, not by any gate.
2. **The ASCII gate blocked on somebody else's bug.** It checked the
   whole output file rather than inserted lines, so two pre-existing
   Unicode arrows aborted a correct patch. **Caught by the gate**,
   though the gate was the thing that was wrong.
3. **`test_extractor_pins.py` was never checked for.** Patch 3 taught
   one consumer of `L192_annotated_sites.txt` about the RETIRED tag and
   never grepped for others. There were two. The maintenance run went
   red on `int('2026-08-16')`. Straight parallel-pipeline failure --
   the rule was not run at all. **Caught by Tony's maintenance run.**
4. **A skill file named for download convenience, not destination.**
   `SKILL_orrery_coding_conventions.md` was filed in `documentation/`,
   where two lookalikes already sat. Two pushed source comments then
   cited a 20-degree rule that existed in no store the skill loader
   reads -- cite-to-nonexistent-authority, live in the repo. **Caught
   by reading the manifest** after the round trip.
5. **An insert written as a replace.** The corrected skill file was
   built with `src[:i] + section + src[j+1:]`, which deleted everything
   between the header and the next heading: the version line, the
   Source line, the criticality note, and the paragraph recording what
   v1.2 added. Since `skills_index.py` reads that version line, the
   file would have installed with no version to find. **Caught by
   Tony**, reading the new file against its sibling.
6. **GPT's line counts, relayed as a question rather than a fact.**
   GPT reported the builder at 288 lines and the checker at 1,510 at
   the anchor and concluded the packet was written against a later
   working copy. Fresh clone and raw fetch of the pinned blob both give
   312 and 1,650. Its Finding 14 premise is false; the behaviours it
   said were missing are missing anyway. **Caught by checking rather
   than relaying.**

**What the checks did catch.** All four of GPT's checker blockers were
confirmed against the pinned source before being recorded. The
retirement record was mutation-tested in both directions before
delivery, as was the shared parser guard. The pure-addition check
written after defect 5 ran on the v3.40 patch and reported 0 of 959
lines lost.

**The pattern worth keeping.** Four of six were caught by a person
reading. The two the system caught, it caught because someone had
recently been burned into building the check -- the ASCII gate existed
because of an earlier encoding failure, and the pure-addition check
exists only because defect 5 happened first. Checks get built after the
failure, not before it. The reviews are what changed that ratio
elsewhere: nine blockers found before a single worksheet went out.

---

## For the next session, in order

1. Confirm both skills load at 1.4.
2. Regenerate stage 2 fingerprints against `f4043bf`.
3. Builder marker join, since stage 1's 96 markers currently do
   nothing.
4. Shape A swaps, ordinal window, token list.
5. Ledger entries L-194 through L-196 and the L-192 as-built.

---

*Prepared August 16, 2026 with Anthropic's Claude Opus 5. Built on
`f4043bf0b0ac5c4746f5a374d76a2b3a86b87bea` at
https://github.com/tonylquintanilla/palomas_orrery.*
