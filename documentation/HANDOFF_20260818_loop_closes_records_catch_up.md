# Handoff -- 2026-08-18 -- the loop closes, the records catch up

**Built on `b65ac115fc0f820e8270c0807249813c67bde7bc` at
https://github.com/tonylquintanilla/palomas_orrery (branch main);
gallery at `ff18d3e6fa31f70a8f525df471e751d046cf14fa` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.**
Both confirmed by live `git ls-remote`.

Type: **BUILD + DESIGN.**
Continues `HANDOFF_20260817_pilot_design_and_json_loop.md`, anchored at
`df81b335`. Where they disagree on a SHA or a count, this one is later.

Lands in `documentation/`.

---

## OBLIGATIONS THE NEXT SESSION MUST DISCHARGE FIRST

**One, and it cannot be cleared from inside the session that created
it.**

`provenance-discipline` went 2.3 -> 2.4 this session. The session that
bumped it loaded 2.3; a mid-session reinstall lands in the account and
stays invisible to a conversation already running. **Confirm the loaded
copy reads 2.4 before any provenance work.**

Measured on August 18: all ten skills compared loaded-against-repo, and
only `provenance-discipline` differs. The other nine are byte-identical.

The previous handoff's obligation -- give the visibility convention a
home -- was DISCHARGED. It is in the skill, and that is what the bump
is.

---

## RUN THESE FIRST, IN THIS ORDER

Two patches remain unrun. Both were verified on clean clones at
`b65ac115`, applied together, followed by the full maintenance runner:
13 of 13 green, 289 Tier-1.

1. `patch_L199_1_records_reconcile.py`
2. `python ledger_index.py` -- **not optional.** It rebuilds the index
   table and physically moves six newly-DONE blocks into their closed
   buckets. Skipping it leaves the table advertising three OPEN items
   that are not.
3. `patch_L199_2_plan_docs_to_head.py`

They touch no file in common, so 3 could run before 1. Prefer this
order: two sentences in the plan documents state the protocol is at
v3.41 and the skill at 2.4, and patch 1 is what makes those true.

`patch_L199_1` SUPERSEDES `patch_L204_2_ledger_reconcile.py`, which was
delivered and never run. Delete it. If it was run, patch 1 aborts on
its fingerprint and says so.

Four patches were run and pushed during the session and are already
archived: `patch_L204_1`, `patch_L201_2`, `patch_L188_1`,
`patch_L188_2`.

---

## What closed

**L-204 -- the loop's last inch.** The annotation grammar accepted only
a worksheet reference ending in `.md`, so a verdict returned as
`.jsonl` could be built, carried, filled, returned, checked and routed
-- and then REFUSED when somebody wrote it back into the code. Found by
an integration test, not by reading. The accepted set is now `.md`,
`.jsonl`, `.json`, defined once in the scanner with a test pinning the
checker's `JSON_SUFFIXES` against it. The shape rule -- a reference
names a FILE, not free prose -- did not move; `non_markdown_reference`
became `unsupported_reference_format`.

**L-200 -- the Resolved leg.** Grammar in `provenance_scanner`, linkage
layer in `worksheet_checker`. Four ways to fail, all mutation-proven,
plus a fifth for a markdown worksheet with no citation-verdict column.
The count prints on every run including zero.

**L-203 -- the visibility convention, in the skill.** A failure that
prints where the responder reads it gets an ANNOTATION; one that
appears nowhere gets a REFUSAL. Visibility decides, not severity.

**L-201, extended.** The builder is a Developer Tools card on the
dashboard -- un-indented, interactive, with the three prompts named in
order and the warning that the selection prompt DEFAULTS TO 1. Four
runner-covered checkers that were missing from the dashboard were added
and the generator cards reordered, so the indented group now matches
`maintenance_run.py` row for row AND in execution order, verified
against the runner's own lists rather than by eye.

**L-205 -- the runner says what happened.** `CHECKERS` rows gained a
report-only flag, set on the two tools that exit 0 whatever they find.
The summary counts the gating eleven and quotes the two report-only
verdicts underneath, in both branches. Four verdict lines that could
not move now carry `N of N`; deleting one test from each suite makes
them read 18, 19, 26, 17.

**L-199 parts 2 and 3, and the header** (in `patch_L199_1`, unrun).
Version history to `documentation/PROJECT_INSTRUCTIONS_HISTORY.md`
PART 1; the v3.37 lessons kept verbatim as PART 2; the ledger appendix
replaced by a pointer; the protocol trimmed to three entries with a
stated rule that a fourth pushes the oldest down. Protocol 1022 -> 1012
lines.

**Numbers.** Checker tests 105 -> 118. Cross-check tests 17 -> 19.
Routing unchanged at 68 of 110 routed, 8 clean. Tier-1 unchanged at
289.

---

## Rulings made this session

**1. The `.md` grammar widens** (Tony, 2026-08-18). Rendering accepted
JSON returns into markdown for citation was rejected: two stores of one
return, free to drift, with the integrity hash in only one of them.

**2. The Resolved leg's first token is the worksheet FILENAME**, not
the batch. Measured: across 34 worksheets on disk, thirteen carry
"batch1" -- Gemini's, GPT's, Claude's, tier 1, tier 2, the follow-ups.
One batch, a dozen files. The check needs one-to-one. Filename is also
already the convention `# Cross-checked:` uses.

**3. Returned worksheets get a structured filename** (Tony,
2026-08-18). See below -- this is the one piece of NEW work the ruling
creates.

**4. The records restructure** -- B, keeping both records, with the
lessons file renamed rather than a new file created.

---

## L-206 and L-207 ship inside `patch_L199_1`

Both blocks are IN the records patch and land when it runs -- nothing
to paste. `ledger_index.py` files them and rebuilds the index; verified
on a clean clone, 202 blocks parsed, no consistency problems, 121 live
items.

L-206 is summarized below; L-207 has its own section further down and
its detail in `documentation/DESIGN_20260818_citation_prompt.md`.

**The shape, confirmed.**
`worksheet_<model>_<batch>_<YYYYMMDD>.jsonl`, e.g.
`worksheet_claude-opus-5_pilot_constants_new_20260818.jsonl`.
Underscores separate fields; hyphens live inside a field. Session is
the date, with a trailing letter when a day repeats.

The model field carries the VERSION; the annotation identity stays
bare. Two Claude legs then score as ONE identity -- conservative and
correct -- while the file records which two Claudes. No migration of
134 annotations.

**Name the pilot's return by hand at dispatch time.** The tooling is
unbuilt, and a rename later breaks every `# Resolved:` leg pointing at
the old name.

---

## L-207 -- the citation prompt, ruled and unbuilt

**The gap, measured.** The citation half of a return has no route out
of the file. `ROLE_SOURCE` is mapped in the header registry and read
NOWHERE. `ROLE_CITATION_VERDICT` is read in exactly two places: an
unreachable third branch of `read_verdict` (unreachable for JSON, which
always synthesizes a value column) and L-200's linkage check, which
fires only on a row a `# Resolved:` leg already names. Both halves are
parsed into the Table and stop.

**Not a defect in the split.** The 2026-08-17 ruling assigned the
citation comparison to a reader BECAUSE it is a language judgement
rather than a numerical one. What was never built is the leg carrying
the material to that reader.

**Tony's design, 2026-08-18.** The checker does two things in one run:
the numerical check exactly as now, and a CONSISTENT JSON prompt asking
Claude the citation question. A worklist is data; a prompt is a
request, and a request inherits the discipline the builder already has
-- keyed rows, a hash, a SHA anchor, generated rather than typed. Same
SHA plus same returns gives the same prompt, which is what makes a
citation review evidence rather than an opinion.

**Ruled: the prompt SHOWS the responder's citation verdict.** It makes
the review a comparison, and disagreement between their verdict and the
reviewer's is the lazy-responder canary -- measured per row, no
separate mechanism. The cost is anchoring, mitigated only by field
order and an instruction that disagreement is a finding rather than an
error. Structural blindness would be stronger and was traded away
deliberately.

**Not strictly blocking for the pilot.** 23 rows can be read by hand.
It IS blocking for the pilot to produce reproducible evidence, and it
does not scale to 110. Both orders are defensible and the design note
weighs them: building first tests the whole loop, dispatching first
replaces a predicted field list with a measured one.

Full detail: `documentation/DESIGN_20260818_citation_prompt.md`.

---

## On complexity, from the 2026-08-18 external review

The review's substantive point: the verification infrastructure now has
a larger state space than a person can hold, and the project has more
epistemic infrastructure than epistemic coverage -- Tier-1 at 289 and
RISING as the scanner's reach improves, not falling.

Its proposed rule is right and is adopted here: **every new provenance
feature should first ask whether it can be expressed by extending an
existing data boundary rather than adding another checking path.**
L-207 was checked against it rather than assumed to pass -- it is an
emitter over the Table the checker already builds, reusing `row_hash`
and the report writer, adding no layer and no verdict class. The
precedent is the JSON adapter, which converted JSON into the same Table
rather than creating a second checker.

That rule has no home yet. It belongs in `provenance-discipline`, and
deliberately NOT this session: writing it into the skill today would
bump 2.4 to 2.5 on top of an install nobody has confirmed, stacking two
unverifiable claims. It goes in with the L-207 build.

**And the balance underneath it.** Build L-207 and then stop. Without
it the pilot's fuzzy half cannot be read at all, so it is the leg that
makes the machinery usable rather than more polish. After it, the
default question stops being "what does the provenance system need
next" and becomes "which outstanding claim can this now settle."

Stated as a test rather than an intention: the next provenance feature
after L-207 should be one an actual RUN exposed the need for, not one a
design conversation invented.

**Three corrections to the review, none changing its conclusions.**
Line counts are about eight per cent low (checker 2124 not ~1950,
scanner 3453 not >3100, builder 819 not ~760). Tier-1 did not "remain"
at 289 -- it rose from 206, because L-198 taught the scanner units it
could not see, which sharpens the infrastructure-versus-coverage point
rather than weakening it. And the `read_verdict` precedence it flagged
is real and now has a handle: L-207.

---

## L-154, designed here so the next session builds

**Do not build it away from the machine.** Reasoning below.

**The defect, measured at the gallery HEAD.** `resolver.py:133` reads

```python
features = tuple(rec.get("features") or ())
```

`rec["features"]` for Saturn is a dict carrying `ring_system` with D
through G and every inner and outer radius in km. `tuple()` on a dict
returns its KEYS, so all seven rings collapse to the single string
`"ring_system"` one line before anything could use them. The numbers
are already within the browser's reach and are discarded on arrival.
`FeatureRequest.params` exists, defaults to `{}`, and is never
populated.

**It splits in two.**

*Half A, stop discarding.* Carry the dict into `FeatureRequest.params`;
widen `ResolvedObject.features` from `Tuple[str, ...]`. Verifiable
mechanically -- assert the report returns seven rings with radii. No
pixel drawn.

*Half B, draw them.* New rendering code in the shared JS layer. Mode 5.

**Why half A is not safe to do blind, which was the surprise.** The
L-080 fingerprint includes `feature_keys` from the resolved context,
and `compare()` treats every non-position field as an exact match. Half
A alone moves Artifact 1's locked fingerprint. That is a deliberate
golden re-open -- the same one L-166 anticipates -- and it needs Tony
present to re-accept Artifact 1 rather than arriving as a surprise
diff.

**And the sequencing argument still holds.** Rings drawn today would be
drawn from unverified numbers, which is what should not be locked into
a reference artifact.

---

## Open items

**Tony-action (decide)**

- The pilot dispatch itself -- when. Nothing blocks it.
- Carried unchanged: the lazy responder, claim typing, cross-worksheet
  disagreement, what UNKNOWN does, the pluto 614/638 merge, transition
  sequencing, whether batching becomes real.

**Claude-side, ready to build, no ruling outstanding**

- L-207, the citation prompt. Ruled 2026-08-18, unbuilt.
- L-206's two supporting pieces.
- L-154, at the machine.
- Blocker 7, the ordinal context window. Not exercised by the pilot.

**Known and not fixed**

- Eleven of thirteen checker rows still resolve their verdict by last
  line, so any of them can be displaced the moment something prints
  later. Giving every row a hint substring is the general cure and was
  not attempted (L-197, carried into L-205).
- The gallery-cache-builder skill and the ledger's deployment-model
  block still describe the retired nightly schedule as live. The
  `TESTING_PROTOCOL.md` instance is corrected in `patch_L199_2`; the
  master plan's was already fixed before this session.
- `info_dictionary.py` holds ten non-ASCII characters inside strings a
  person reads. Content decision, left alone.

---

## The pilot, unchanged and ready

Run the builder from the dashboard card. Selection **2**
(`constants_new`, 23 of 100 rows); batch name; anchor SHA = whatever
HEAD reads at that moment. Send the `.jsonl`; the `.md` is the fallback
if a return will not parse.

**Read `PILOT_EXPECTED_DISPOSITIONS_20260817.md` BEFORE reading the
returns.** 13 clear, 10 return, three trap rows. If all 23 clear, that
is agreement, not success.

---

## Process record: what did not survive checking

Four defects of Claude's, none caught by a passing check.

1. **A patch script that scanned itself.** The first sandbox run of the
   Resolved-leg patch reported one leg with a linkage problem. The
   phantom was the script's own worked example, sitting at the start of
   a line inside a string literal. It would have produced a false
   finding on the first real run. The example is now composed rather
   than written out.
2. **A widened tuple that compiled and died.** `patch_L188_1`'s first
   cut added a seventh field to the runner's results rows and missed a
   failure-detail loop unpacking a fixed width. `py_compile` cannot see
   a tuple width. Found by running it.
3. **A recalled anchor.** The skill's grammar line was quoted from
   memory as `(<ref>.md)`; the file says `(<worksheet>.md)`. The patch
   aborted and wrote nothing, which is the guard working.
4. **A superseded instruction left inside quotation marks.** The
   TESTING_PROTOCOL correction argued that a retired instruction in a
   protocol read at the moment of doing the thing is one somebody
   follows -- and then quoted it verbatim. A check written for the
   patch caught the contradiction.

**One process improvement worth carrying.** The report-only summary and
the four verdict lines were both found by Tony asking a plain question
of the runner's own output -- "is this intent or result?" -- rather
than by any check. The answer was "result, but one that cannot move,"
which is the third instance this month of a line that reads the same
whether or not anything happened.

---

## For the next session, in order

1. Confirm the loaded `provenance-discipline` reads 2.4.
2. Confirm both SHAs after Tony's push.
3. Then, in whatever order Tony wants -- none blocks another:
   L-207 (the citation prompt), the dispatch, L-154 at the machine, or
   L-206's two supporting pieces. The one sequencing question worth
   deciding deliberately is L-207 before or after the first dispatch;
   the design note weighs both.

---

*Session written August 2026 with Anthropic's Claude Opus 5. Built on
`b65ac115fc0f820e8270c0807249813c67bde7bc` at
https://github.com/tonylquintanilla/palomas_orrery; gallery at
`ff18d3e6fa31f70a8f525df471e751d046cf14fa`.*
