# Session Handoff -- August 13, 2026

**Built on `b22bcf8f39dab375f6b5cf1207826575fdda3415`, pushed at
`edf4c7f05e62f1d835211652174d2f800b4e6297`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery unchanged at `c2202dcc2c4ed210160ce6033b70346aef194b68`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both HEADs verified live at session close.**

**Type: BUILD plus REVIEW plus RULINGS.** The worksheet checker is
built, tested, wired into the runner and the dashboard, reviewed by
Fable, and corrected in one integration pass. Three pushes:
`6de5e8d` (the checker), `dfabd0f` (the ledger as-built), `edf4c7f`
(the vocabulary integration). No orrery rendering code touched.

**Continues from** `documentation/HANDOFF_20260813_L192_rulings.md`
(anchored `6b99ace` / `b22bcf8`).

**Prepared:** August 13, 2026 by Claude Opus 5, Tony Quintanilla
integrator.

---

## TWO OBLIGATIONS FOR THE NEXT SESSION, BOTH BLOCKING

**1. Confirm your loaded `provenance-discipline` reads 2.3.** The skill
went 2.2 to 2.3 at `edf4c7f`. The session that bumped it had 2.2
loaded, and a mid-session reinstall cannot be verified from inside the
session -- the loaded copy is bound when the conversation starts. Your
load performs the check; this note cannot. **If it reads 2.2, STOP and
ask Tony to reinstall before doing any provenance work.** 2.3 carries
the settled vocabulary the checker now implements.

**2. `PROJECT_INSTRUCTIONS.md` changed and must be re-uploaded to the
Claude UI project.** `skills_index.py` rewrote the manifest row to 2.3
-- the runner reported `rewrote PROJECT_INSTRUCTIONS.md`, not
"unchanged," which is the distinction that runner change was built to
surface. A stale UI copy advertising 2.2 against a repo saying 2.3 is
exactly the three-week drift the Stale Skill gate exists to catch.

The previous handoff's obligation (2.2) was DISCHARGED: the skill
loaded at 2.2 and the manifest at HEAD read 2.2, checked against both
the resident protocol and the repo.

---

## What happened

| SHA | What |
|---|---|
| `6de5e8d` | `worksheet_checker.py`, its tests, runner rows, two dashboard buttons |
| `dfabd0f` | L-192 as-built recorded in the ledger |
| `edf4c7f` | skill 2.3, checker to the settled vocabulary, tests to match |

Five patch scripts ran and are archived in `documentation/`.

---

## The checker

Six layers over every cross-check annotation attached to a scored
value: the worksheet exists (L0), it belongs to the named checker
(LID), the row is located (L1), the value agrees with the evidence
(L2a), the value still equals what the checker read then (L2b), the
verdict amounts to a completed check (L3). It consumes the scanner's
attachment and has no annotation parser of its own. Report-only.

**Current run: 104 annotations, 3 clean, 41 send back, 20 to
conversation, 40 noted, 30 outside scanner reach.** 51 tests pass.

### The payload: four values moved after their check

| Constant | Checker read | Code now |
|---|---:|---:|
| `HELIOPAUSE_RADII` | 26,449 | 26,148 |
| `BENNU_RADIUS_KM` | 0.262 | 0.246 |
| `HAUMEA_RADIUS_KM` | 816 | 715 |
| `ARROKOTH_RADIUS_KM` | 9.95 | 9.1 |

**`HELIOPAUSE_RADII` IS NOT A DEFECT AND MUST NOT BE SENT BACK.**
Fable caught this and the code comment settles it: corrected 2026-08-02
from 26449 because the prior figure used 123 AU where Gurnett says
121.6, and *both checkers independently found the error*. The value
moved because the check worked. Sending it back would commission a
re-check of its own resolution. Bennu, Haumea and Arrokoth are the real
cases. **The eight DRIFTED findings need a human pass splitting
drift-with-recorded-cause from unexplained drift before any dispatch.**

---

## Fable's review: five rulings

Anchored at `6de5e8d`. Numbers re-derived independently with its own
tooling, differences reported rather than reconciled.

1. **Six tokens column-scoped -- YES.** The skill already said "two
   verdicts per row, never conflated" and then listed six on one flat
   line, so the prose knew what the vocabulary forgot.
2. **Quoting Notes is transcription, not interpretation -- YES**, given
   four properties. Two were being violated live.
3. **Addendum / redo / new-job split -- YES**, plus: an addendum's
   drift comparison must read against *that worksheet's own anchor*, or
   it manufactures false drift.
4. **Disqualification stands.** The rung goes 77 to 50 to **28**, and
   28 is the true number. Execution rides one edit pass, not a separate
   strip.
5. **Keep the twenty tokens** (grandfathered) and fix compound
   handling.

**Ruling 5 was overturned by measurement, and Tony ruled.** Fable's
errand-economy argument was that reverting re-commissions work already
done. Measured: of the three tokens earlier prompts commissioned by
name, UNSOURCED appears ten times, DEAD LINK **zero**, OUTDATED
**zero**. Every other extra was invented at the keyboard, and nearly
all sit in the Resolution column of the five followup files *already
going back for redo*. The grandfathered population was being
re-commissioned regardless. **Settled: seven tokens -- the six,
column-scoped, plus UNSOURCED as a citation alias.** Cost, measured:
four annotations carry an unreadable verdict instead of two.

### Corrections to numbers this session had wrong

- **Eight root modules carry annotations, not nine.** Opus prose error.
- **Routing is 3 / 39 / 22 / 40 noted, not 43.** An ad-hoc script
  folded the 3 clean into "noted." The tool had been printing 40
  correctly throughout.
- **The citation-only population is 47 annotations, not 46.** 47 name
  those worksheets; 46 carry VALUE_VERDICT_ABSENT; one
  (`CHROMOSPHERE_PHYSICAL_KM`, Gemini) routes to UNMATCHED at L1 first.
- **"19 of 73 claims" counts claim-LEGS, not distinct claims.** A
  two-leg string contributes twice. The report should say which unit it
  counts. NOT YET FIXED.
- Verdict cells: 438 by Opus's rule, 460 by Fable's. Off-vocabulary: 75
  vs 83 leading-token / 126 whole-cell. Same order, different rules,
  both stated.

---

## What was built at `edf4c7f`

**`provenance-discipline` 2.2 -> 2.3.** Vocabulary assigned to columns
-- value: YES/NO/APPROX/UNVERIFIED, citation:
YES/NO/PARTIAL/DERIVED/UNSOURCED/UNVERIFIED. A vocabulary version line
worksheets state, so a tool reads a line instead of guessing from
dates. And a new CRITICAL section, *Quoting a Worksheet Is
Transcription, Not Interpretation*, with the four properties.

**The checker.** Registry twenty tokens to seven. Compound cells
flagged rather than trimmed in silence. Verdict cells quoted between
`<<` and `>>` and cut only at a stated limit with a visible marker.
**The Notes column now reaches the report** in both finding tables,
keyed to the matched row and nothing else.

**Tests.** 46 to 51. The two asserting the overturned rule were
replaced; four added for compound detection, quote delimiting, quote
truncation, and UNSOURCED surviving where NOT FOUND does not.

### Two defects the quoting work fixed, both live in the first report

A finding read `reads NO -- wrong authority -- wrong authority for a
value that may still be right` -- half checker, half template, fused
past telling apart. Another was cut mid-word at forty characters with
no marker. Both were transcription becoming interpretation by accident.
The question of whether a tool should quote a worksheet was never
hypothetical: the tool had been doing it, unspecified, since the first
run.

---

## NEXT SESSION: the producer half is not finished

**Do not dispatch the errand yet.** Fable's largest miss: the requests
can leave before the instruments that make them succeed exist, and then
round two happens by construction. Three things must be IN the
send-back prompts and none is built:

1. **The column-scoped vocabulary and the version line** in the prompt
   templates. The skill has them; the templates do not.
2. **A key column keyed by anchor name** (pre-design fork 1c).
   **UNMATCHED is 25 findings, the second-largest class, and nothing in
   the five decisions touches it.** An addendum that comes back unkeyed
   leaves all 25 standing after the errand is spent.
3. **The specific claims needing rows.** The checker's UNMATCHED and
   CLAIMS_UNADDRESSED lists are already that enumeration; the prompts
   should carry them rather than asking checkers to rediscover gaps.

**Also unbuilt from Fable's review:** the worksheet-own-anchor rule for
L2b (an addendum without an anchor line is UNREADABLE for drift), and
the claims-fraction counting-unit label.

### Then, in order

**Dispatch,** three shapes: redo for the five followup files (51 of 60
cells off-vocabulary), addendum for the two large tier2 files (8 of
232), a new value-column job for the five citation-only files -- which
are well-formed and whose checkers did nothing wrong. **Word it as
commissioned scope, not checker error.** The same people are about to
be asked for the value half.

**Then ONE annotation edit pass**, never three: the backfill of the 27,
the strip-or-qualify of the 47, and the repointing of orphans and
addenda all edit the same lines in the same files. Repointing replaces
the reference rather than adding a second same-checker line, which
would trip the duplicate-identity diagnostic and fakes nothing anyway.

**Closeout is not zero findings.** The 30 unreachable lines stay until
L-190. Some UNMATCHED residue survives by design. The test is that
every annotation either clears or carries a recorded reason it does
not, with nothing in an unexamined pile.

---

## (do) -- outstanding

Items 1, 2, 3, 4 and 7 carry forward from the previous handoff
unchanged. Item 6 remains folded into the checker work and is still
not settled -- the provenance scanner still discards its full output on
every passing run, including the L-189 delta.

8. **`worksheet_checker.py` is `orrery` domain in the audit** despite
   its `Domain: dev_tools` docstring tag. `MODULE_DOMAIN_MAP` does not
   know the new module. Cosmetic; three Tier-3 findings either way.

---

## (decide) -- still open

1. Jupiter's ring entry count: 4 or 5.
2. Migration shape and per-body sequence beyond Jupiter (L-181).
3. Saturn `thickness_km`: absent from the served cache -- from the
   ORRERY too?
4. Tier-3 tuning constants and `provenance_exceptions.json`: the three
   in `provenance_history.py` **plus three more** from the checker
   (`MIN_PROSE_FRAGMENT`, `INSTRUCTION_LOOKBACK`,
   `INSTRUCTION_LOOKAHEAD`). One decision, six constants.
5. `LESSONS_ARCHIVE.md` line-count discrepancy (824 vs 882).
6. Are `DEFAULT_MARKER_SIZE` and `CENTER_MARKER_SIZE` in cross-check
   scope at all?
7. `WORKSHEET_CHECK.md` committed or generated-only. Consistency with
   `PROVENANCE_AUDIT.md` says committed. Mechanical.
8. Fable observed **11 uncited worksheets** where earlier documents
   said 9. The fork-5 set-change printing will settle it.

---

## Process -- read this before your first substantive reply

**Four findings this session came from Tony reading, not from anything
running.** The Hill sphere convention last session; this session the
dashboard button that was never added, the Notes column having no
reader, and the sequencing of Fable's review to before the errand
rather than after. None was findable by executing anything.

**The method note, and it is the same lesson one layer down from the
gate this protocol added at v3.39.** An over-broad slice in an editing
script deleted four functions -- 204 lines -- and `py_compile` reported
success. The file parsed perfectly and was hollow. `py_compile`
verifies that a file parses, never that it still contains what it is
supposed to contain, and a green result cannot distinguish the two. The
fix was a guard asserting the expected function set survives every
edit, run beside the compile check. Recovered from a throwaway sandbox
copy, which is the only reason it cost minutes.

**A second, smaller one in the same family.** A patch script's
docstring claimed the Notes cell reached the report; the edit did not
implement it. Caught by reading the docstring against the diff. The
fix was the code, not the claim -- a docstring asserting behaviour that
does not exist is the citation-layer failure moved into documentation.

**On the review itself:** the request deliberately withheld method
while stating every number, so Fable would derive rather than
reconcile. It found three Opus errors that way. That is the August 12
lesson working -- cross-AI independence protects against a shared
model, not a shared specification.

---

*Handoff prepared August 2026 with Anthropic's Claude Opus 5. Built on
`b22bcf8f39dab375f6b5cf1207826575fdda3415` and pushed at
`edf4c7f05e62f1d835211652174d2f800b4e6297` at
https://github.com/tonylquintanilla/palomas_orrery. Gallery at
`c2202dcc2c4ed210160ce6033b70346aef194b68` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io --
untouched by this session.*
