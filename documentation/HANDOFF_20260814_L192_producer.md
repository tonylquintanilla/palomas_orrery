# Session Handoff -- August 14, 2026

**Built on `305b2697648590e4a75551c73743abc98bd20c66`, pushed at
`65ca311512a5646551a8ed9e385863807809e2e9`
(the build landed at `92b5bf8f7def1bc384c165eb84224ad1e542125f`;
the Tier-1 banner patch ran after this document was written and
pushed at `65ca311`, which is where the session actually ends)
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery at `b486c68ab63abb25ae6d7dda73d0b4b6f64c0d0d`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io --
nightly cache run only, no source change.
Both HEADs verified live at session close.**

**Type: DESIGN plus BUILD.** The L-192 producer half was designed
across two AI reviews and five Tony rulings, and its first piece --
the shared key module -- is built, tested, pushed, and wired into the
maintenance runner. No request has been emitted and nothing has been
dispatched. No orrery rendering code touched.

**Continues from** `documentation/HANDOFF_20260813b_L192_vocabulary.md`
(anchored `b22bcf8` / `edf4c7f`).

**Prepared:** August 14, 2026 by Claude Opus 5, Tony Quintanilla
integrator.

---

## ONE OBLIGATION FOR THE NEXT SESSION, BLOCKING

**Confirm your loaded `ledger-and-session-records` reads 1.6.** The
skill went 1.5 to 1.6 at `92b5bf8`, adding the *Where a File Goes*
section. The session that bumped it had 1.5 loaded, and a mid-session
reinstall cannot be verified from inside the session -- the loaded copy
is bound when the conversation starts. Your load performs the check;
this note cannot. **If it reads 1.5, STOP and ask Tony to reinstall
before doing ledger, handoff, or file-placement work.**

The previous handoff's obligation was DISCHARGED: `provenance-
discipline` loaded at 2.3 and the manifest at HEAD read 2.3, checked
against both the resident protocol and the repo. `PROJECT_INSTRUCTIONS.md`
was re-uploaded to the Claude UI project and the skill reinstalled,
both confirmed by Tony this session.

---

## What happened

| SHA | What |
|---|---|
| `d9b06df` | key module, alias store, tests, pins, site list, Fable prompt |
| `92b5bf8` | both patches run: runner row added, skill to 1.6 |

Three patch scripts ran clean and are archived. A fourth
(`patch_L192_tier1_banner.py`) was delivered at session end and had
not been run at the time of writing.

---

## Five rulings, all Tony's

1. **Keys are tool-issued and shipped pre-filled.** Checkers fill
   evidence and verdict columns; they do not invent keys.
2. **Duplicated prose gets one row keyed to both sites**, not one row
   per site.
3. **The value-column job is a second emission mode of the same
   builder**, not a separate tool. A separate tool is the parallel-
   pipeline anti-pattern arriving on schedule.
4. **The alias map is built now rather than deferred**, so it is
   visible. Later reconsidered against a third option and confirmed --
   see below.
5. **Dedupe is exact canonical equality**, no fuzzy prose matching
   anywhere in the producer. Settled by measurement, not argument.

---

## THE CORRECTION THAT MATTERS MOST

**Three of the four "duplicate prose pairs" reported to Fable were not
duplicates.** They are SUBSET relations: the short module-level
`*_info` string is contained in the longer function `description`,
which then makes claims the short one never makes.

| Pair | Chars | Checkable claims |
|---|---|---|
| `pluto` 41 / 61 | 336 -> 1,975 | **1 -> 4** |
| `pluto` 136 / 155 | 383 -> 1,112 | 1 -> 1 |
| `pluto` 400 / 423 | 807 -> 2,920 | **1 -> 3** |
| `venus` 43 / 62 | 465 -> 465 | 2 -> 2 (identical) |

Only `venus` 43/62 is a true duplicate. Merging the others would have
commissioned one row for the short string and silently dropped claims
that exist only in the long one -- the false merge whose defining
property is that nothing announces it.

**The error was found by AST extraction of the string values.** The
original measurement grabbed text by line windows, which swallows
neighbouring content and reads a shared opening paragraph as "same
text."

### And how it was caught, which is the reusable part

Tony sent the same review prompt to Fable twice by accident, on a
phone with intermittent signal. **Run 1 confirmed the wrong pairs.
Run 2 caught them.** Same model, same prompt, same anchor, opposite
answers on the load-bearing number.

Run 1 agreed because it used the same line-window method the request
had used. That is the shared-method failure the August 12 lesson
names, reproduced exactly: cross-AI agreement confirms nothing when
both sides reach for the same tool. GPT, which could not execute
anything and reasoned from principle, also rejected the fuzzy merge.

**Standing implication: a single cross-check run is one sample.** When
a number is load-bearing and the reviewer's method is not visibly
different from the author's, agreement is weak evidence.

---

## Errand size, corrected twice

The request document at `305b269` says **15 distinct bodies of prose**.
That figure is wrong and the document carries it uncorrected -- it is
the record of what Fable actually received and should not be quietly
edited.

- Prose-body unit, corrected: **17 bodies plus 1 constant**
- **Claim unit, adopted: 36 checkable claims across 18 string sites,
  reducing to ~25 distinct signatures, plus 1 constant = ~26 dispatch
  rows.**

The 36-claims figure is verified from the checker's own report text.
The reduction to 25 signatures is Fable's figure and is NOT verified --
it needs the extractor's context windows to check.

The claim unit is correct because rows are per-claim by ruling 1. Both
Fable run 2 and GPT arrived at it independently.

---

## What was built at `d9b06df`

**`worksheet_keys.py`** -- mints and resolves keys. One owner, imported
by both the builder and the checker, so a key cannot be born stale from
two implementations disagreeing. Key shape:

    pluto_visualization_shells.py::create_pluto_core_shell::description::c1
    constants_new.py::CHROMOSPHERE_PHYSICAL_KM

No line number (edits shift them). No code value (drift would move the
pointer with the thing it must outlive). Enclosing name resolved by AST,
preferring the innermost function over local assignments.

**`worksheet_key_aliases.py`** -- the rename store, empty. Append-only,
entries added only in response to a KEY_STALE finding, imported by
default so a caller who forgets the argument gets the real map.

**`test_worksheet_keys.py`** -- 53 sites, 53 keys, zero collisions, plus
**53 PINNED keys** resolved against current source.

**`documentation/worksheets/L192_annotated_sites.txt`** and
**`L192_key_pins.txt`** -- the corpus and the pins.

### The finding inside the build

**The round-trip test as specified could not fail.** Minting a key from
today's source and resolving it against today's source agrees with
itself no matter what the source says. A rename in a throwaway copy
left it reporting 53 of 53 resolved, exit 0.

Pinned keys fixed it: keys written down at `305b269`, resolved against
current source. Five mutations now fail correctly -- rename without
alias (KEY_STALE), alias pointing at a typo (ALIAS_STALE), deleted pin
file, deleted alias store, and the pin file left at its old path after
the directory move.

**This was found by trying to break the test, not by reading it.**

---

## Fork B, ruled twice

Tony ruled for the alias map over deferral. Fable run 2 then proposed a
third option not on the table: a `# Formerly: old_name` comment at the
renamed definition, read by adjacency, with no second store at all.

Tony asked for a recommendation. **The map stands**, for three reasons:

1. A misplaced breadcrumb is indistinguishable from a missing one -- one
   blank line and the comment is inert while looking present. A dict
   entry matches or it does not.
2. It would add a prose-parsed convention to a project whose recurring
   failure is prose-parsed conventions.
3. The proximity argument does not survive KEY_STALE. The report names
   the stale key and prints the string to add, so the map does not have
   to be remembered either.

Checked, not assumed: a `# Formerly:` comment would NOT be mistaken for
an annotation -- `CROSS_CHECK_LINE_RE` requires the literal
`# Cross-checked:` prefix.

**If function renames ever produce enough churn that entries stop being
added, the breadcrumb comes back.**

---

## Design settled and NOT yet built

Adopted from GPT without needing a ruling:

- **The uncommitted-bytes guard.** The builder refuses to emit if the
  source it scanned is not represented by the anchor commit. This is
  the SHA round trip applied at the producer.
- **Key uniqueness as a build-time invariant**, not a one-time
  measurement. One key, one claim site; a violation is a build error.
- **Hand-authored oracle fixtures** with expected keys written
  literally in the test, not computed by a helper sharing the
  production interpretation.
- **Claim-level dispatch.**
- **Schema version separate from vocabulary version** -- two different
  contracts.

From Fable run 2:

- **The witness mechanism for Fork A.** The pre-filled row must quote
  the claim's context anyway; that quoted fragment, numbers masked, IS
  the re-pointing detector. Ordinal and witness must agree.
  Insert-a-number-ahead yields KEY_REPOINTED, not DRIFTED.
- **A merge manifest** printed at build time for every row keyed to
  more than one occurrence.
- **A batch manifest** so an errand that never returns is visible.
- **KEY_STALE needs its own destination** in the report -- it is
  code-side repair, not send-back and not conversation, and would
  otherwise age in "noted."

---

## NEXT SESSION

### Two rulings that BLOCK dispatch

**1. The extractor constants (decide item 4).** `MIN_PROSE_FRAGMENT`,
`INSTRUCTION_LOOKBACK`, `INSTRUCTION_LOOKAHEAD` decide which numbers
count as claims. `::cN` counts checkable claims, so retuning them
re-points every issued ordinal corpus-wide with zero prose edits.
**Settling these after dispatch invalidates the errand retroactively.**
This was Fable run 2's largest catch and it was not on the blocking
list before.

**2. The eight DRIFTED findings.** A human pass splitting drift-with-
recorded-cause from unexplained drift. `HELIOPAUSE_RADII` **must not be
sent back** -- the code comment shows it moved as the correction two
checkers independently found; sending it back commissions a re-check of
its own resolution. Bennu, Haumea and Arrokoth are the real cases.

### Then build the builder

`worksheet_request_builder.py`, both emission modes, one schema. Then
the key rule plus KEY_REPOINTED/KEY_STALE in the checker. Then the
oracle fixtures.

### Then dispatch, then ONE annotation edit pass

Three shapes: redo for the five followup files, addendum for the two
large tier2 files, a new value-column job for the five citation-only
files -- worded as commissioned scope, not checker error. The backfill,
the strip-or-qualify, and the repointing all edit the same lines in the
same files.

**Closeout is not zero findings.** The test is that every annotation
either clears or carries a recorded reason it does not.

---

## (do) -- outstanding

Items 1, 2, 3, 4 and 7 carry forward from the previous handoff
unchanged. Item 6 remains unsettled -- the scanner still discards its
full output on every passing run.

8. **`worksheet_checker.py` is `orrery` domain in the audit** despite
   its `dev_tools` docstring tag. `MODULE_DOMAIN_MAP` does not know the
   module. Cosmetic. `worksheet_keys.py`, `worksheet_key_aliases.py`
   and `test_worksheet_keys.py` are new and will land the same way.
9. **CLOSED -- the Tier-1 banner was reworded and verified.** The
   patch ran clean at `65ca311` and the runner now prints `206
   TIER-1 FINDINGS IN THE SCANNED TREE` above `All 11 checkers
   passed`, which no longer contradicts it. Kept here rather than
   deleted: the reason below is why the banner said what it said
   for three protocol versions, and that is worth reading once.
10. **Correction note for the Fable prompt document** at `305b269`,
    carrying the 15-bodies figure. Append rather than edit.
11. **The claims-fraction counting-unit label** ("19 of 73 claims"
    counts claim-legs) is still not fixed, and the report has a second
    instance of the same defect: the class table sums to 88 finding
    rows while the tables hold 128 body rows. One header line stating
    both retires it.
12. **Gallery cache builder quarantined a locked `.prev`** on the
    nightly run (`WinError 5`, `data/solar-system.quarantine_
    20260815T021433Z`). Expected recovery behaviour, but the
    quarantine directory accumulates and nothing prunes it.

### On item 9, the banner

The scanner prints `206 TIER-1 FINDINGS -- PUSH GATE NOT MET` and two
lines later `Informational only. This does not affect the exit code.`
Both are true. The gate moved to the ACTIVE BUILD PATH at
`provenance-discipline` 2.3 (L-184), so a global count is not the gate
number.

A warning that announces a failure and then says it fails nothing
trains the reader to skim it. The patch reports the count, states
plainly that it is not the gate, and names what the gate is judged on.
It does not invent a build-path count, because the scanner does not
compute one -- that is a design decision, not a banner edit.

---

## (decide) -- still open

1. Jupiter's ring entry count: 4 or 5.
2. Migration shape and per-body sequence beyond Jupiter (L-181).
3. Saturn `thickness_km`: absent from the served cache -- from the
   ORRERY too?
4. **Tier-3 tuning constants and `provenance_exceptions.json`** -- now
   BLOCKING dispatch, see above. Six constants, one decision.
5. `LESSONS_ARCHIVE.md` line-count discrepancy (824 vs 882).
6. Are `DEFAULT_MARKER_SIZE` and `CENTER_MARKER_SIZE` in cross-check
   scope at all?
7. `WORKSHEET_CHECK.md` committed or generated-only.
8. Fable observed 11 uncited worksheets where earlier documents said 9.
9. **`pluto` 614/638 merge.** Under the claim-signature rule they share
   their science claim and merge; the prose rule declined them. Fable
   run 2 believes merging is correct and flags it as Tony's to confirm
   from the merge manifest.

---

## Process -- read this before your first substantive reply

**Two findings this session came from Tony reading, not from anything
running.** The active-versus-archived file placement (which became
skill 1.6, in corrected form) and the contradiction in the Tier-1
banner. Neither was findable by executing anything.

**Three checks that could not fail, all in one session.** The round-trip
test that agreed with itself. The banner patch's own idempotence
sentinel, which used lowercase `not` against a banner printing `NOT`,
so a second run reported a drifted file instead of an applied patch --
caught by running the patch twice rather than by reading it. And the
`py_compile`-passes-hollow-file case carried over from last session.
The v3.39 gate is earning its place at a rate of about three per
session.

**On the file placement rule.** Tony's framing was active-versus-
archived. The corrected framing in skill 1.6 is READ BY A TOOL versus
READ BY A PERSON, because a worksheet is the most finished thing in the
project and lives in `worksheets/` anyway -- the checker opens it every
run. His cut would have sent the worksheets themselves the wrong way.
The origin note in the skill records both.

**On register.** Tony worked part of this session from a phone while
walking. Executive-summary format was requested twice. One thing per
message, answer first, evidence on request.

---

*Handoff prepared August 2026 with Anthropic's Claude Opus 5. Built on
`305b2697648590e4a75551c73743abc98bd20c66` and pushed at
`65ca311512a5646551a8ed9e385863807809e2e9` at
https://github.com/tonylquintanilla/palomas_orrery. Gallery at
`b486c68ab63abb25ae6d7dda73d0b4b6f64c0d0d` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.*
