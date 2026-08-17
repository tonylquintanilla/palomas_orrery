# Handoff -- 2026-08-17 (evening) -- the pilot gets a shape, and the loop gets everything but its last inch

**Built on `df81b3358823139784dcd1e80052c6685dd86e22` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**
Confirmed by live `git ls-remote`. Gallery repo untouched at
`3d10739b097e2b63395cf58742873cf378210e68`.

Type: **BUILD + DESIGN.**
Second handoff of 2026-08-17. The morning one
(`HANDOFF_20260817_blocker1_closed.md`) is anchored at `ce84f05` and
records the blocker 1 work. Where they disagree on a SHA or a count,
this one is later.

Lands in `documentation/`.

---

## OBLIGATIONS THE NEXT SESSION MUST DISCHARGE FIRST

**One, and it cannot be cleared from inside the session that created
it.**

The visibility convention (below, L-203) has NO HOME. It is recorded in
`documentation/DECISIONS_20260817_pilot_design.md` at HEAD, and a
decisions file is a record -- nothing loads it at the moment of need.
Its home is `skills/provenance-discipline/SKILL.md`, which has not been
edited. Until it is, the convention is not in force anywhere a session
would find it.

The morning handoff's obligation -- confirm the loaded protocol version
-- was DISCHARGED at the start of this session. The loaded copy read
v3.40, August 16 2026, and was byte-identical to `PROJECT_INSTRUCTIONS.md`
at repo HEAD (same md5 after line-ending normalization, 59,065 bytes,
skill manifest row-for-row identical). The two re-uploads did not change
what a new session reads.

No skill was bumped this session. `provenance-discipline` loaded at 2.3
and `safe-file-editing` and `ledger-and-session-records` at 1.4 and 1.6,
each matching its manifest row.

---

## What closed

Four patches, all run by Tony, all pushed, all with the maintenance
runner green afterward.

| Patch | What | Files |
|---|---|---|
| `patch_L195_1` | Seven Shape A swaps | `constants_new.py` |
| `patch_L201_1` | Selection, JSON emitter, row hash, blocker 8 | builder + its tests |
| `patch_L202_1` | JSON return reader, LH layer, routing file | checker + its tests |

**L-195 -- Shape A, complete.** Six ruled sites plus `OUTER_CORONA_RADII`
taken in passing. The authority now sits on the `# Source:` line the
worksheet verdicts; the event or formula moved to `# See:` or
`# Derived:`. No value changed -- proven by importing the module before
and after and diffing all 52 module-level names.

**L-201 -- the builder can be asked for fewer rows.** Named selections
in the module, listed at the prompt, blank meaning the whole corpus.
Three ship: `all`, `constants_new` (the pilot's 23 rows), and
`sendbacks`, which reads a checker-written key list. Selection runs
after the L-196 refusal.

**L-202 -- JSON both ways.** The request is emitted as JSON Lines beside
the markdown, each row carrying an eight-character hash over its
do-not-edit fields. The checker reads a returned `.jsonl` into the same
Table the markdown parser produces, so every layer runs unchanged, and a
new layer LH routes back any row whose hash is wrong (`ROW_MODIFIED`) or
absent (`ROW_HASH_MISSING`). A markdown table has no integrity map, and
that reads NOT APPLICABLE rather than pass.

**Blocker 8, in passing.** Both formats now print the accepted verdict
words, read from `worksheet_checker.VERDICT_TOKENS` rather than retyped,
so the request cannot name a vocabulary the checker rejects.

**Numbers.** Builder tests 41 -> 61. Checker tests 69 -> 105. Routing
unchanged at 68 of 110 routed, 8 clean. Scanner Tier-1 unchanged at 289.
`data/worksheet_routed.json` now exists with 40 keys.

---

## The finding that matters most, and it blocks the dispatch

**The annotation grammar refuses a JSON worksheet.**

`provenance_scanner.parse_cross_checks` requires the parenthetical
reference to end in `.md`. A line citing a `.jsonl` return is refused
with the code `non_markdown_reference`, earns nothing, and is reported
as a diagnostic. Measured, not read:

    # Cross-checked: Claude 2026-08-17 -- IAU B2 (worksheet_claude_pilot.jsonl)
    -> records: []   issues: [(..., 'non_markdown_reference')]

    the same line ending .md
    -> records: [('Claude', '2026-08-17', 'worksheet_claude_pilot.md')]

Found by building a simulated JSON return, annotating a constant to cite
it, and running the checker -- which listed the worksheet as UNCITED. A
reading of the code would not have produced this; the integration test
did.

**Consequence.** Leg 6 of the loop -- turning a returned verdict into an
annotation in the code -- cannot cite a JSON return. Everything up to
leg 5 now works. This is the last inch.

**The ruling Tony has not yet made.** The `.md` condition does two jobs.
It enforces that the reference is a FILENAME rather than free prose,
which is the anti-gaming part of L-186 and should stay. It also pins the
only format worksheets had in August 2026, which stopped being true on
2026-08-17. Three ways through, with Claude's recommendation first:

1. **Widen the extension set** to `.md`, `.jsonl`, `.json`. The shape
   check survives intact. One condition in one function, plus the tests
   that pin it, plus renaming `non_markdown_reference` -- which would
   otherwise become a name that misdescribes its own rule.
2. **Keep `.md`, have the checker render accepted JSON returns into
   markdown** for archiving and citation. The grammar never moves, but
   the archived artifact becomes a derivative whose fidelity nothing
   checks -- two stores of one return, free to drift, with the hash in
   only one of them.
3. **Keep `.md`, require a hand-written markdown companion.** Same
   drift, plus manual work per return.

---

## Ledger block, ready to paste

L-196 went DONE this session, so the visibility convention cannot attach
there. Index row:

```
| ! | L-203 | The visibility convention -- give it a home in the skill | OPEN | 3.6 | 2026-08-17 |
```

```
#### [L-203] The visibility convention -- give it a home in the skill
<!-- L:203 status:OPEN upd:2026-08-17 section:A flag: rice:2/3/85/1 -->
- **The convention.** A failure that prints where the responder reads it
  gets an ANNOTATION; a failure that appears nowhere gets a REFUSAL.
  Visibility decides, not severity.
- **Where it came from.** L-196 left one question open as Claude's call:
  should a mismatched continuation marker refuse rather than report? It
  currently reports. The distinction drawn was that a mismatch prints
  into the worksheet where the responder reads it, while an unmarked
  continuation appears nowhere. Tony's ruling 2026-08-17: settle it as a
  CONVENTION rather than a one-off, because the same distinction governs
  every future case of the same shape.
- **It has a record and no home.** Recorded in
  `documentation/DECISIONS_20260817_pilot_design.md`. Nothing loads a
  decisions file at the moment of need. Its home is
  `skills/provenance-discipline/SKILL.md`, next to the annotation
  grammar.
- **No behaviour changes.** The builder already reports mismatches and
  refuses unmarked continuations. This writes down WHY, so the next case
  is decided rather than re-argued.
- **Mechanics.** Edit the skill, bump 2.3 -> 2.4, run `skills_index.py`
  to regenerate the manifest table in PROJECT_INSTRUCTIONS.md, reinstall
  to the account profile. Per the Stale Skill limits, a mid-session
  reinstall cannot be verified from inside the session that makes it --
  so the bump becomes an obligation the FOLLOWING session discharges by
  reading its own loaded copy.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** unwritten. The convention is in force nowhere a session would
find it.
**Ref:** L-196 (where the question arose); L-186 (the annotation
grammar it sits beside).
```

---

## Open items

**Tony-action (decide)**

- **The `.md` grammar.** Above. Blocks the dispatch.
- **The pilot's dispatch itself** -- when, and to how many readers. Reader
  count was removed from the critical path this session: the request is
  one file, reader-agnostic, and per-reader identity is already carried
  on the return side by the `# Cross-checked:` grammar.
- Carried unchanged: the lazy responder, claim typing, cross-worksheet
  disagreement, what UNKNOWN does, the pluto 614/638 merge, transition
  sequencing, whether batching becomes real.

**Claude-side, ready to build, no ruling outstanding**

- **L-200, the `# Resolved:` leg and its linkage check.** Designed and
  measured, not written. A `# Resolved:` line added to a real block
  produced 100 rows, 0 unmarked, 0 problems, 153 joins -- unchanged --
  so it reads as a label and does not trip the L-196 ratchet. Build it
  in the same patch as the grammar change: both touch the annotation
  grammar and the checker that reads it.
- **Blocker 7**, the ordinal context window. Not exercised by the pilot
  (constants have no ordinals) and deliberately so.

**Known and not fixed**

- Eleven of thirteen checker rows still resolve their verdict by last
  line. Recorded in L-197.
- `info_dictionary.py` holds ten non-ASCII characters inside strings a
  person reads. Content decision, left alone.
- `constants_change_report.py:17` still names `CHROMOSPHERE_RADII` in a
  docstring example. Harmless, reads as live.

---

## The pilot, as decided

Ten decisions, recorded in full in
`documentation/DECISIONS_20260817_pilot_design.md`. The four that shape
everything else:

1. **The pilot's object is the LOOP, not the citations.** Tony:
   verification is what the loop provides.
2. **It ends at re-verification in the code**, not at routing. A row
   that routes correctly and then cannot become an annotation has failed
   the loop.
3. **The mechanical checker stays at numbers; the citation comparison is
   done by a reader.** The tool checks the paperwork -- that a
   `# Resolved:` leg exists and names a real row -- not the meaning.
4. **The selection is one file:** `constants_new.py`, all 23 rows. The
   branch coverage is a property of the file rather than of anyone's
   judgement about which rows are interesting.

`documentation/PILOT_EXPECTED_DISPOSITIONS_20260817.md` predicts **13
clear, 10 return**, row by row, with three trap rows whose wrong answer
is diagnostic (`SUN_RADIUS_KM` nominal vs measured, `HELIOPAUSE_RADII`
AU vs solar radii, `BENNU_RADIUS_KM` metres vs km). That file must be
read BEFORE the returns are read. If all 23 clear, that is agreement,
not success.

---

## Process record: what did not survive checking

Four defects of Claude's this session. Not one was caught by a passing
check.

1. **A safety guard that only caught what I had remembered.** The Shape
   A patch's first invariant listed the citation bodies by hand and
   checked their counts. A mutation deleting one line from one edit
   passed, because the deleted line was not on the list. Replaced with a
   structural check: strip the leg labels from both sides of every edit,
   and the remaining text must be identical in any order. Proven
   load-bearing -- removing it lets the dropped-line mutation through.
2. **A claim about the ratchet that a mutation disproved.** I wrote that
   the ORDER of statements in `main()` stops a selection from bypassing
   the L-196 refusal. Reordering it changed nothing. What enforces the
   rule is which collection the refusal loop reads -- the whole corpus,
   never the selected subset. The comment now says the true thing and a
   test pins the one-word mutation that does bypass it.
3. **An integrity layer with no test that asked it to fail.** The LH
   layer had a test for the markdown NOT-APPLICABLE case only, so a
   mutation making it return early for EVERY status passed all 96
   checks. Now five checks ask it to fail.
4. **A test that asserted a file an earlier run had written.** The
   routing test checked that `data/worksheet_routed.json` exists -- and
   it did, from a real run minutes earlier. Replacing the write with
   `pass` passed. It now writes into a fresh temporary directory, where
   existence proves THIS call wrote it, and checks a non-zero count
   against the file's own contents.

**What caught them.** Four mutation tests. The pattern from the morning
handoff repeats exactly: checks get built after the failure, not before
it. Defects 3 and 4 are the same defect as 1 -- a check that cannot
fail -- found in three different layers on one day.

**What the checks did catch.** Every patch was applied to a clean clone
at HEAD and verified byte-identical to the tree it was tested on. Every
behaviour added was mutation tested in both directions: seven mutations
against the builder tests, ten against the checker tests, all turning
the suite red except the two that exposed defects 3 and 4. The full
maintenance runner ran green on a throwaway copy with `SystemButtonFace`
swapped, since that Tk colour does not resolve on Linux.

---

## For the next session, in order

1. Confirm the loaded `provenance-discipline` version before any
   provenance work. Expected 2.3 unless L-203 landed first.
2. Rule on the `.md` grammar.
3. Build the grammar change and L-200 as ONE patch -- both touch the
   annotation grammar and the checker that reads it.
4. Land L-203 in the skill, bump 2.3 -> 2.4, regenerate the manifest,
   reinstall, and write the verification into the NEXT handoff.
5. Then the dispatch: run the builder with selection 2, send the
   `.jsonl`, and read the expected dispositions before reading the
   returns.

---

*Prepared August 17, 2026 with Anthropic's Claude Opus 5. Built on
`df81b3358823139784dcd1e80052c6685dd86e22` at
https://github.com/tonylquintanilla/palomas_orrery.*
