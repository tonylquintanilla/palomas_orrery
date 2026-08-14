# Fable Review Request -- Vocabulary, Notes, and the Send-Back (L-192)

**Built on `6de5e8debb0b157819c60abf1a81a82d692a82ae`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
HEAD verified live at the time of writing, August 13, 2026.
Gallery repo at `c2202dcc2c4ed210160ce6033b70346aef194b68` and not in
scope.**

**Type:** Mode 7 review request (collegial relay). Nothing is built
from this. No code expected back -- rulings on five decisions, and
anything the five miss.

**Prepared:** August 13, 2026 by Claude Opus 5, for Claude Fable 5.
Tony Quintanilla is the integrator and holds final judgment.

**Continues from** your pre-design review of this checker
(`documentation/FABLE_REVIEW_L192_worksheet_checker.md`, anchored
`00219d9`). The checker is now built, tested, wired into the
maintenance runner and the dashboard, and pushed. Your identity check
and your drift-since-check are both in it.

---

## Who you are writing for

Tony Quintanilla, PE, is a retired civil and environmental engineer, an
artist, and an anthropologist. He is not a professional software
developer and not a formally trained astronomer. He builds this project
as a "vibe coder" -- through conversation with AI partners rather than
writing code unassisted -- and holds sole commit authority.

**The codebase is not evidence of his personal programming skill.** Its
structure and discipline are the product of iterative collaboration.
Reading the code cold you would infer a skilled programmer wrote it;
that inference is wrong. Unpack jargon on first use and do not assume
CLI fluency -- he runs Python from VS Code's Run button and uses GitHub
Desktop.

What he owns personally is the workflow: the protocol, the ledger, the
design rulings, and the orchestration across models. Every ruling cited
in this document is his.

**On his reading load, which is a constraint and not a courtesy.** He
has stated plainly that he is limited in what he can read and absorb.
Lead with the ruling in one plain sentence, put evidence after it, and
do not stack a finding, a recommendation, an uncertainty and a question
into one breath.

---

## Why this is being asked NOW rather than after the next step

This is Tony's call and it reverses mine. I proposed reviewing after
the work was done. He pointed out that the expensive step is not the
review -- it is the ERRAND. The next action sends worksheets back to
the sessions that produced them, across several models, and a second
round of that because the vocabulary was wrong is what one relay is
worth avoiding.

So the decisions below are settled between him and me and NOT yet
executed. Nothing has been sent back. The checker is built and
report-only; no annotation has been stripped and no rung has moved.

---

## Ground truth, measured at the anchor

Reproducible from the repo at the SHA above. Please do reproduce them
-- see the note at the end about why that matters more than usual here.

- **134 cross-check annotation lines** across nine root modules.
- **104 of those are attached to a value the scanner scores.** The
  other 30 sit on code that never becomes a scored unit: four known
  orphans in `constants_new.py`, plus derived constants that are
  products of two names, module-level display strings the scanner does
  not reach, and dict keys in `shell_configs.py`. That is ledger item
  L-190 (scanner reach), not a defect in the checker.
- **17 distinct worksheets** are named by those 104.
- First run: **3 clean, 39 routed to send back, 22 routed to
  conversation, 43 noted without a route.**
- **19 of 73 numeric claims** in cross-checked display strings have a
  worksheet row. A further 27 numbers in those strings are the
  orrery's own operating instructions -- a manual scale to set, a frame
  weight to expect -- excluded and counted, because no worksheet row
  could ever address them.
- **438 verdict cells across the 17 cited worksheets. 75 are
  off-vocabulary (17%).** Distribution below.

### The four prompts stated four different vocabularies

| Prompt | Vocabulary it specified |
|---|---|
| `worksheet_prompt_constants_new.md` | YES / NO / PARTIAL / DEAD LINK / DERIVED |
| `worksheet_prompt_batch1_tier2_cross_check.md` | value: YES / NO / APPROX; citation: YES / NO / PARTIAL / DERIVED / UNSOURCED |
| `worksheet_prompt_batch1_tier1_sourcing.md` | YES / NO / APPROX / OUTDATED |
| three others | nothing at all |

The `provenance-discipline` skill (v2.2, current) states six: YES, NO,
PARTIAL, APPROX, DERIVED, UNVERIFIED. **No prompt ever asked for
UNVERIFIED**, and checkers wrote it 16 times anyway -- they had a state
and no word for it. **UNSOURCED, DEAD LINK and OUTDATED were each asked
for by name** and are not in the skill.

### Off-vocabulary cells by file group

| Group | Files | Verdict cells | Off-vocabulary |
|---|---:|---:|---:|
| Citation-only, well-formed | 5 | 91 | 3 |
| Followup and blind-lookup | 5 | 60 | 51 |
| The two large tier2 cross-checks | 2 | 232 | 8 |
| Remainder | 5 | 55 | 13 |

---

## The five decisions

### 1. The vocabulary: six tokens, assigned to columns

**Proposed.** Keep exactly six, and stop listing them as one flat set:

- **Value correct?** -- YES / NO / APPROX / UNVERIFIED
- **Citation correct?** -- YES / NO / PARTIAL / DERIVED / UNVERIFIED

Everything else becomes NO with the reason in Notes. DEAD LINK,
OUTDATED and UNSOURCED all collapse to citation-NO. CONFIRMED collapses
to YES. WRONG VALUE and WRONG CITATION disappear, because two columns
already say which one is wrong.

The column assignment is not cosmetic. The tier2 prompt used APPROX for
the value question and PARTIAL for the citation question -- they were
never synonyms -- and the skill's flat list loses that, so a checker
reading it cannot tell which word belongs to which question.

**What we are unsure about.** Does collapsing UNSOURCED into citation-NO
lose something that matters? "The named source does not publish this
specific value" and "the named source publishes a different value" are
different findings with different repairs, and the six cannot tell them
apart. Notes can, if Notes has a reader -- which is decision 2.

### 2. Does quoting the Notes cell in the report count as interpretation?

**This is Tony's question and he raised the risk himself.**

Context: he asked who reads the Notes column. The answer, checked
rather than assumed, is that nothing does. The checker reads Notes in
three places, all of them row-MATCHING -- it uses the prose to work out
which row is about which value -- and never reports what a cell says.
`WORKSHEET_CHECK.md` prints finding codes and the tool's summary of
them, never the checker's own words.

So "the reason goes in Notes" currently means the reason goes nowhere.

**Proposed.** The report's finding tables print the matched row's Notes
cell verbatim beside each routed finding. The verdict is still decided
by the token and only the token; no tool reads the prose to decide
anything.

**Tony's stated risk: misinterpretation.** His position is that
interpreting a malformed answer is exactly what the August 13 rule took
off the table, and that a tool surfacing prose invites a reader to
interpret it. My position is that quoting is transcription, not
interpretation, and that it also guards the matcher -- a quoted row
obviously about something else reveals a bad match immediately, which
is your own argument from the propose-mode review, still standing after
the mode itself was declined.

We did not settle it. Rule on it, and say plainly if you think the
distinction between transcription and interpretation holds up under
use rather than only in principle.

### 3. Addendum or redo, per file group

**Proposed**, and the precedent is already on disk:
`worksheet_claude_constants_new_addendum.md` covers 17 unresolved rows
from its original, names that original and its anchor, and checks
values against HEAD rather than against what the original recorded.

- **Two large tier2 files** -- 8 bad cells in 232. **Addendum.**
  Re-running 232 rows to fix 8 is disproportionate, and they carry the
  bulk of the display-string evidence.
- **Five followup and blind-lookup files** -- 51 bad cells in 60.
  **Redo.** An addendum covering 85% of the rows is a redo wearing a
  different name, and the files are small.
- **Five citation-only files** -- well-formed, 3 bad cells in 91. **Not
  an addendum to fix rows at all.** A new job on the same constants:
  the value column nobody ever asked for.

**One requirement that came out of measuring the precedent, and it is
the part most likely to be dropped.** That existing addendum is cited by
NOTHING. No annotation points at it, so the checker counts it as
uncited pending work. The evidence was produced, it is good, and it is
invisible to the tool. **Any addendum requires repointing the
annotation to it**, which is annotation editing, which means the
addendum requests and the annotation backfill are one pass rather than
two.

### 4. Disqualifying the 46 citation-only annotations

**Tony's ruling, already made.** Forty-six of the 104 annotations name a
worksheet whose only verdict column is `Citation correct?`. Those
worksheets asked whether the cited source publishes the value, and
answered -- a completed check of a narrower question than the
annotation asserts. Those annotations are disqualified until the value
half exists.

Two things worth your attention rather than your agreement:

- The worksheets are **not** malformed and their checkers did nothing
  wrong. The prompt says so in its own words: "Citation verification,
  not value discovery." What was incomplete is the job that was
  commissioned.
- Making the disqualification true means stripping or qualifying 46
  annotations, which moves the top trust rung down **further than the
  attachment rule did** -- that one took it from 77 units to 50. Say if
  you think the second-order effect on the audit changes the ruling, or
  only its sequencing.

### 5. My unilateral divergence, stated as mine

Your pre-design review said: exact-match verdict table, everything else
announced UNREADABLE, do not fuzzy-match verdicts.

**I built a registry of twenty tokens.** Beyond the skill's six it
reads CONFIRMED, CORRECT, INCORRECT, WRONG, WRONG VALUE, WRONG
CITATION, NOT FOUND, UNSOURCED, NOT CHECKED and N/A, each carrying a
scope that says whether it answers the value question or the citation
question. I added no fuzzy matching. I made the call mid-build without
asking, and it is recorded in the ledger as unruled.

The riskier half is smaller and worse than the token count suggests.
About fifteen cells are compound -- "CONFIRMED for 700-1200 km, with
qualification", "YES for 1.64 R_M", "PARTIAL / citation needs
correction". My classifier reads the leading token and discards the
rest. That is the tool deciding a qualification does not matter.

**Measured cost of reverting to the six: four findings move**, from
conversation to send back. Not the twenty the token count implies --
most off-vocabulary cells sit in rows no annotation points at.

Decisions 1 and 5 are the same decision seen from two ends. If the six
stand, the registry shrinks to six.

---

## What to send back

Tony will paste your response into a fresh session. Open with the same
anchor line this document carries.

Then, in this order:

1. **One sentence per decision**, 1 through 5, with your ruling and its
   reason. Say plainly where you are uncertain rather than picking to
   be decisive.
2. **Anything the five decisions MISS** -- a failure mode this
   sequencing cannot detect, a group of files that needs different
   treatment, an assumption that will not hold once the addenda arrive.
3. **Second questions, listed separately at the end** rather than woven
   in.

Two constraints from this project's standing rules, either of which you
may argue against explicitly:

- **The artifact bounds the audit.** Scope is what the code contains at
  this commit. An audit whose denominator grows whenever someone thinks
  of something never closes, and an audit that never closes stops being
  read.
- **Ledger economy.** All of this is L-192's body. Say plainly if you
  think any of it earns a separate handle.

---

## The measurement request, and why it is not routine

**Reproduce the numbers before you use them.** Every figure in this
document is stated so it can be checked against the repo at the anchor,
and I have deliberately NOT described how I computed any of them.

That omission is the point. On August 12 your written attachment rule
and your own measurement script disagreed, my independent
implementation read the same prose the same wrong way, and I reported
the agreement to Tony as confirmation. It was confirmation of a shared
misreading. The number went to him wrong twice.

Cross-AI independence protects against a shared model, not a shared
specification. So: derive the 104, the 30, the 438, the 75, the 46 and
the 19-of-73 from the artifact, and tell me where your numbers differ
from mine rather than reconciling to them.

And as before: **where you state a rule below, state it in a form you
would be willing to have tested against an implementation you did not
write.** If a rule has a case you are unsure about, name the case.

---

*Review request prepared August 2026 with Anthropic's Claude Opus 5,
built on `6de5e8debb0b157819c60abf1a81a82d692a82ae` at
https://github.com/tonylquintanilla/palomas_orrery*
