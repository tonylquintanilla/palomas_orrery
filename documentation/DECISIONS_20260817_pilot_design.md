# Decisions -- 2026-08-17 -- the pilot's shape, and three items it needs first

**Built on `98b29f00dbd7e3be235a6f88d615718ccfc397dd` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**
Confirmed by live `git ls-remote`. Gallery repo untouched.

Type: **DESIGN RECORD.** No code was built this session. One patch was
delivered and has not been run.

Lands in `documentation/`. Companion to
`DESIGN_20260817_worksheet_selection.md`, same session.

---

## What was decided, in the order it was decided

**1. The pilot's object is the loop, not the citations.** Tony:
verification is what the loop provides. So rows are chosen to exercise
the mechanism, and every row's expected DISPOSITION is written down
before dispatch -- otherwise a pilot that comes back looking fine is
indistinguishable from one that never engaged.

**2. The pilot ends at re-verification in the code, not at routing.**
Legs 1 through 7: build, carry, fill, return, check, edit the
annotation, confirm the record moved. A row that routes correctly and
then cannot be turned into an annotation has failed the loop.

**3. The fuzzy half of leg 7 stays with a reader; the mechanical half
stays in the tool.** The checker's L2b layer already closes the loop
for VALUES -- it tells DRIFTED from CORRECTED from UNCHECKED_MOVE. It
does not close for citations: `ROLE_SOURCE` is mapped in the header
registry and read nowhere else, so a returned source cell is parsed and
dropped. Tony's ruling: leave the mechanical checker at numbers, do the
citation comparison with Claude, and have the tool check the paperwork
instead of the meaning.

**4. Two ledger handles, not one.** Selection is dispatch-side, the
`# Resolved:` leg is return-side, and they close independently.

**5. The pilot's selection is one file: `constants_new.py`, all 23
rows.** The rule is one line and the branch coverage is a property of
the file rather than of anyone's judgment -- clean standards rows, a
derived row whose cross-checks name no authority, a bare-URL source, a
never-checked row, four rows with joined continuations, and the
must-not-send-back canary. Blocker 7 (the truncated ordinal claim) is
deliberately NOT exercised: constants have no ordinals, and shipping a
known-defective presentation into the first dispatch would confound the
loop test.

**6. Reader count is not a property of the pilot.** One generated
request, carried to one reader or three. Per-reader identity is already
carried on the return side by the `# Cross-checked:` grammar. This came
out of Tony catching that a question about reader count implied
customized requests -- it did not, and asking it was the error.

**7. The checker emits JSON findings alongside its markdown report.**
Tony's suggestion, and it dissolved rather than answered the objection
it met: the round-two key-list consumer does not have to invent the
producer's format if the producer emits it. Precedent already in the
tool -- `data/worksheet_check_state.json`.

**8. The pilot's worksheet is JSON; markdown is the fallback.** Tony:
the purpose of the pilot is to test, so send the JSON; if a return
fails to parse, send the markdown. Markdown parsing stays live
permanently regardless, because the seventeen historical worksheets are
markdown.

**9. Each JSON row carries an integrity hash over its do-not-edit
fields.** Not for tamper-proofing -- for attribution. Without it, a
responder who rounds a code value produces an L2b mismatch that reports
the CODE as drifted, sending someone to investigate a constant that
never moved. A missing hash fails the row.

**10. The key-list consumer ships with L-201.** Selecting rows from a
checker-written list of send-backs is built in the same patch as the
selection mechanism and the JSON emitter that produces the list.

---

## Ledger blocks, ready to paste

Index rows for the table near the top:

```
| ! | L-200 | The `# Resolved:` leg -- record a verdict that landed | OPEN | 5.1 | 2026-08-17 |
| ! | L-201 | Request selection -- ask the builder for fewer rows | OPEN | 5.4 | 2026-08-17 |
| ! | L-202 | JSON worksheet format, with markdown as fallback | OPEN | 2.3 | 2026-08-17 |
```

### L-200

```
#### [L-200] The `# Resolved:` leg -- record a verdict that landed
<!-- L:200 status:OPEN upd:2026-08-17 section:A flag: rice:2/3/85/1 -->
- **What it is.** A record-only annotation leg naming the worksheet row
  whose verdict caused an edit, and the ledger handle that authorized
  it. Example shape:
  `# Resolved: <batch> <key> -- citation refuted, Source replaced (L-2xx)`
- **Why it is needed now.** The pilot ends at re-verification in the
  code (2026-08-17 ruling). Without this leg, an annotation edited in
  response to a verdict is indistinguishable from an unexplained edit,
  and the only record of which is which lives in a handoff.
- **It cites the KEY, never the row number.** `row_id` is positional and
  renumbers whenever the corpus changes; the key
  (`module.py::enclosing::label::cN`) is stable. Same failure the ledger
  already records for per-handoff item numbers.
- **Deliberately NOT in `CONTEXT_LEGS`.** As an unknown label it is
  invisible to the request, which is correct: a row dispatched a second
  time must not show the responder what the last one concluded. A
  context leg would anchor the way a Claude-derived figure anchors
  Gemini.
- **Measured, not assumed.** A `# Resolved:` line added to a real block
  in the patched sandbox: 100 rows, 0 unmarked, 0 problems, 153 joins --
  unchanged. It reads as a label, so it closes a leg run rather than
  tripping the L-196 ratchet. Nothing in the builder has to change.
- **The check is linkage, not meaning.** Three existence facts: the leg
  parses, it names a worksheet row that exists, and that row's citation
  verdict was one requiring an edit. Refuses on a leg pointing at a row
  that does not exist. Prints how many legs it examined, so a clean run
  says what it looked at.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** unbuilt. Fields depend on nothing outstanding -- reader count
was removed from its critical path 2026-08-17.
**Ref:** L-192 (Break 5); L-196 (the ratchet it must not trip); L-201.
```

### L-201

```
#### [L-201] Request selection -- ask the builder for fewer rows
<!-- L:201 status:OPEN upd:2026-08-17 section:A flag: rice:2/3/90/1 -->
- **The defect.** `build()` returns the whole annotated corpus and
  `main()` renders every row -- 100 rows over 52 sites at HEAD. There is
  no way to ask for fewer, so producing a pilot slice today means
  hand-editing the generated file, which breaks the request's own
  do-not-edit instruction and yields a slice no second run reproduces.
- **A selection is code, not typing.** Named entries in the module, each
  a name, a one-line purpose, and a predicate. `main()` lists them at
  the prompt; blank means the whole corpus, so today's behaviour is the
  default.
- **Ships with exactly two:** `all`, and `constants_new` (the pilot's
  23 rows). Stratified caps from the design note are NOT built --
  decision 5 removed the need for them.
- **Selection runs AFTER the L-196 refusal, never before.** Excluding a
  site must never excuse an unmarked continuation; a ratchet with a
  bypass is not a ratchet.
- **The request records its own selection:** name, count against corpus
  size ("23 of 100"), and the statement that keys identify rows.
- **Checker emits JSON findings** alongside `WORKSHEET_CHECK.md`,
  carrying routed rows by key. Precedent:
  `data/worksheet_check_state.json`.
- **A key list is legitimate only when the checker wrote it.** Never one
  a person typed. The test is whether the list can be regenerated.
- **The key-list consumer ships WITH this item** (Tony, 2026-08-17). The
  earlier case for deferring it was that building the consumer meant
  inventing the producer's format; the JSON findings emission removes
  that, since the producer exists in the same patch. What remained
  against it was an unexercised path that looks available -- weaker than
  the risk of the rule being written down and not read under pressure.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** unbuilt. Full detail in
`documentation/DESIGN_20260817_worksheet_selection.md`.
**Ref:** L-196; L-200; L-202.
```

### L-202

```
#### [L-202] JSON worksheet format, with markdown as fallback
<!-- L:202 status:OPEN upd:2026-08-17 section:A flag: rice:2/3/75/2 -->
- **Why.** The checker carries tolerance machinery that exists only
  because the interchange is prose: eight header spellings mapped to the
  source column alone, an emphasis stripper, and 15 unrecognised columns
  in the current run. A keyed object deletes that defect class -- a
  field name is right or it fails loudly.
- **The known risk, stated.** Failure granularity inverts. Markdown
  degrades row by row; JSON fails whole-file. Hedge: rows written one
  object per line, so a truncated return is salvageable object by
  object.
- **Tony's ruling 2026-08-17:** the purpose of the pilot is to test, so
  send the JSON; if a return fails to parse, send the markdown.
- **Markdown parsing stays live permanently.** The seventeen historical
  worksheets are markdown. This is a format ADDED, never a replacement.
- **One producer, two views.** The markdown renderer and the JSON
  emitter both run off the same `Request` list. No second source of
  truth.
- **Row integrity hash, approved 2026-08-17.** Eight hex characters over
  the joined, normalized do-not-edit fields (key, claim, code value),
  written by the builder and recomputed by the checker. The case is
  ATTRIBUTION, not tamper-proofing: without it, a responder who rounds a
  code value produces an L2b mismatch reporting the CODE as drifted,
  sending someone to investigate a constant that never moved. A missing
  hash FAILS the row -- a hash that passes when absent is a check that
  cannot fail. The run reports how many were verified.
- **Rejected alternative:** rebuilding rows from the anchor SHA to
  compare directly. More exact, but only works while the tree still
  matches the anchor, and by the time a return lands it usually does
  not.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** unbuilt. Needs a checker-side JSON reader as well as a builder
-side emitter.
**Ref:** L-201; L-192 (L2b, the layer the hash protects from
misattribution).
```

### Amendment to L-196, not a new handle

The mismatched-marker question (report vs refuse) is settled as a
CONVENTION rather than a one-off ruling. The general rule: **a failure
that prints where the responder reads it gets an annotation; a failure
that appears nowhere gets a refusal. Visibility decides, not severity.**
Its home is the `provenance-discipline` skill, next to the annotation
grammar. No builder behaviour changes.

---

## Next session, in order

1. Confirm the loaded `provenance-discipline` version before doing
   provenance work. It is expected at 2.3 and will need a bump when the
   visibility convention lands -- and a mid-session bump cannot be
   verified from inside the session that makes it.
2. Run `patch_L195_1_shape_a_swaps.py` (delivered 2026-08-17, not yet
   run) and confirm its output.
3. Build L-201 and L-202 as ONE patch. Selection, the JSON emitter, the
   checker's JSON findings, and the key-list consumer all edit
   `worksheet_request_builder.py` or `worksheet_checker.py`; two patches
   fingerprinting the same file would abort the second by construction.
4. Build L-200.
5. Write the pilot's expected dispositions for all 23 rows BEFORE
   dispatch. This is the artifact that lets the pilot fail.

---

*Prepared August 17, 2026 with Anthropic's Claude Opus 5. Built on
`98b29f00dbd7e3be235a6f88d615718ccfc397dd` at
https://github.com/tonylquintanilla/palomas_orrery.*
