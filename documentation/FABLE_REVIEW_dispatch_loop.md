# Review reply: the worksheet dispatch loop, before first use

**Built on `a872205d17ee5298d1bdc86c614b43506e82b22c` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**
Remote HEAD at review time equals the pinned commit -- no drift to
reconcile. Prepared August 15, 2026 by Claude (Fable role). Tony
Quintanilla holds every decision here.

---

## Verdict, one paragraph

The architecture is sound and the checker is genuinely well built --
keys that cannot be born unresolvable, a checker that does not write
and does not gate, two dispositions that keep incompleteness separate
from disagreement, and a test file whose 69 checks I ran and which
exercises every layer with an injected failure. Do not dispatch yet.
Five blocking defects, all cheap, all in the builder or the
annotations, none in the checker: the truncated citations (Finding B,
which I reproduced at exactly 45 of 65 rows), ordinal rows that show
the responder no per-claim context -- including three strings where
two rows carry the SAME number and the responder cannot tell them
apart even in principle -- a request that never states the seven legal
verdict tokens, a scripted "answer NO" instruction that pre-answers
one row's question, and the six event-narrative Source lines (Finding
A). The single thing I would change first is the pair that amounts to
"show the responder the true question": fix the leg joining and give
each ordinal row its own context window. Then run a small pilot
before spending external effort on all 65.

---

## Method -- what I verified versus what I reasoned about

Verified by execution at the pinned commit (I have repo access; I
cloned it and ran code):

- `git ls-remote` -- remote HEAD is `a872205`, the pinned commit.
- Read `worksheet_request_builder.py` in full (312 lines), and read
  `worksheet_checker.py` at the load-bearing points: `match_row` rule
  0, `VERDICT_TOKENS`, the L2b drift block (DRIFTED / CORRECTED /
  UNCHECKED_MOVE), `claim_rows`, and `shift_check` in
  `worksheet_keys.py`.
- Ran `build('.')`: 65 rows over 65 distinct keys, zero skipped
  files, per-file counts matching Section 3 of the request exactly.
- Reproduced Finding B mechanically: 33 annotated sites whose
  `# Source:` line loses a continuation, producing exactly 45 of the
  65 dispatch rows -- your numbers -- plus 2 further sites truncated
  on context legs only (47 rows total lose some leg text).
- Ran the test suites directly (`python3 test_worksheet_checker.py`,
  `test_worksheet_keys.py`): all 69 checks pass; 53 pinned keys
  resolve.
- Rendered the actual eris and chromosphere rows the responder would
  see, and searched all dispatched strings for duplicate claim
  values (found three units -- Finding 2 below).
- Read the six Finding-A Source lines and their `# Cross-checked:`
  lines in `constants_new.py`, and confirmed 206 Tier-1 in
  `PROVENANCE_AUDIT.md`'s run history.

Reasoned about, not verified: how an external responder will actually
behave, the canary design in Finding 7, and the judgment calls in the
seed answers. I did not read the 17 legacy worksheets this session.

One disclosure for seed 3: I am the same model family as the author
of this loop and of this prompt. My mitigation was to execute and
measure rather than agree; every count above is a reproduction, not a
reading. Where GPT reaches the same conclusions by a different
method, that agreement is the real signal; where we differ, weigh GPT
as the independent voice.

---

## Positions on Findings A and B

**Finding A -- right, and Shape A (swap) is the right repair.** I
verified all six Source lines at the SHA. One honest nuance: the
mechanical evidence is slightly weaker than presented for one row.
Five of the six `# Cross-checked:` lines name the Ref-line authority
(Stone, Gurnett, Kasper, Golub & Pasachoff, JHUAPL); the ROCHE line
reads "formula verified" -- the checkers verified the formula, which
is what the Source line states. The swap is still right there (the
authority belongs on the verdicted line), but the table's "all six"
framing is really "five of six, and the sixth by principle."

Why Shape A over Shape B: merging paper and event onto one line puts
two claims under one verdict cell, which recreates the compound-answer
problem at the annotation layer -- a responder judging "Stone et al.
-- Voyager 1 crossed at 94 AU" must silently decide which half NO
would refer to. The narrative is real content; `# See:` keeps it read
without making it judged. Third option considered and rejected:
verdicting the Ref leg when the Source is narrative makes the
verdicted object vary per row, which reintroduces the interpretation
the ruling removed.

One addition: after the six are fixed, add a lint to the builder -- a
Source line that matches no authority shape (author-year, standards
body, or URL) prints a warning at build time. That keeps the class
detectable instead of fixed-once. A check that fired this time by a
person reading should be able to fire next time by itself.

**Finding B -- right, the proposed fix is right in direction, and the
risk you name is real but fails in the safe direction.** The key
asymmetry: over-joining (swallowing a free-prose line into a Source
leg) is VISIBLE -- the request is a human-read document and the extra
text appears right there in the row context. Under-joining, the
current behavior, is silent. So a slightly greedy join plus one human
pass over the emitted file is the right shape. Concretely: append
unlabeled comment lines to the most recent extracted leg, stopping at
the next labeled line, a blank comment, or the block's end; have the
builder PRINT how many continuation lines it joined and -- more
important -- report any unlabeled comment line it did not attach to
anything. The current defect is a silent drop; the fix must not be a
silent join. Completeness check after the fix: re-run the builder and
confirm the five sample rows in your Section 4 table read whole,
including the eris row that currently ends mid-parenthesis.

---

## Numbered findings

### 1. [BLOCKING -- is Finding B] Truncated citations, reproduced at 45/65

Covered above. Reproduced by execution: 33 sites, 45 rows on the
Source leg; 2 more sites on context legs. Fix before dispatch --
these rows ask the responder to verdict a sentence fragment.

### 2. [BLOCKING] Ordinal rows show no per-claim context, and three strings have duplicate values no responder can tell apart

The claim: a responder cannot answer the string rows as dispatched,
because the row does not show which number in the string it asks
about.

Evidence (executed): every ordinal row of a string shows the SAME
90-character excerpt -- the first 90 characters of the whole string.
For `eris_hill_sphere_info`, rows R25-R28 all display "SELECT MANUAL
SCALE OF AT LEAST 0.1 AU TO VISUALIZE. 1.3 MB PER FRAME FOR HTML.
Hill Sp..." -- pure UI instructions -- against code values 67.8,
0.095, 38, and 37,000, with the sentences those numbers live in cut
off. Worse: three dispatched units carry DUPLICATE raw values --
`pluto...haze_layer::description` has "200" twice,
`pluto...atmosphere::description` has "200" and "1700" twice each,
`venus...upper_atmosphere::description` has "100" and "120" twice. For
those pairs the two rows are byte-identical from the responder's side
except for the ordinal, which names a position they cannot see.
Answers to those rows are unverifiable by construction.

Recommendation: the extractor already computes each claim's character
offset (`physical_claims` recomputes offsets on purpose). Excerpt a
window AROUND each claim's position for that row's Claim cell, with
the number itself visibly marked. That fixes both the missing context
and the duplicate ambiguity in one change.

### 3. [BLOCKING] The request never states the legal verdict vocabulary

The claim: the responder is told "use one token per verdict cell" and
is never told which tokens exist.

Evidence (executed): I read `render()` in full. The "What each column
asks" section explains the columns; nowhere in the emitted file do
the seven tokens (`yes`/`confirmed`/`correct`, `partial`/`approx`/
`approximate`, `no`, `unverified`, `unsourced`, `derived`) appear.
The seven-token registry exists because a twenty-token registry was
measured to be words invented at the keyboard -- and this request
reproduces the conditions of that measurement: an external model with
no vocabulary list will invent words, everything comes back
UNREADABLE, and the first dispatch becomes a send-back exercise.

Recommendation: enumerate the tokens in the request with one line of
semantics each, and define the boundary cases the corpus is known to
produce: yes = the source states this number at this precision;
partial/approx = the code value sits inside the source's stated range
or rounds from it; no = outside it; unverified = you did not complete
the check; unsourced = you looked and the source publishes no such
number; derived = the value follows from stated inputs -- verdict the
inputs in Notes. Without the semantics, two honest responders will
split yes/approx on the same row and convergence detection turns to
noise.

### 4. [BLOCKING] The builder scripts an answer -- "Answer Citation correct? as NO"

The claim: one row's verdict is pre-written by the tool that asks the
question, and the pre-written answer is wrong for the row it fires on.

Evidence (executed): `render()` emits, for any row with no `# Source:`
leg: `Cited source: none recorded. Answer "Citation correct?" as NO
and say so in Notes.` I ran `build()`: exactly one row triggers it --
`constants_new.py::CHROMOSPHERE_RADII`, the one value in the dispatch
that is deliberately not physical (drawn at 1.1 for visibility;
physical ~1.003; Tony's ruling, L-180). A scripted verdict is a check
that cannot fail -- the answer arrives regardless of whether anyone
looked -- and here it also records a citation defect against a value
that makes no citation claim. Both halves of the project's own rule
are violated at once.

Recommendation: the builder partitions claim types before dispatch.
A drawn/convention value is excluded from the value-and-citation
questionnaire, and the exclusion is ANNOUNCED in the request ("out of
scope: 1 drawn value, listed below with its ruling"), the same way the
Not-reached section already announces unreadable files. If a check is
wanted for it, the checkable questions are different ones: does the
physical anchor hold (CHROMOSPHERE_PHYSICAL_KM = 2000 -- already a
normal row), and does the display text say the shell is drawn larger
than physical. Never instruct a verdict. This also answers seed 8.

### 5. [BLOCKING -- is Finding A] Six Source lines name events, not authorities

Position and repair shape above. Fifteen minutes of annotation edits
plus the builder lint. Blocking only in the narrow sense that those
six rows as dispatched ask whether a claim supports itself.

### 6. [SHOULD FIX] The anchor SHA is typed by hand and verified by nothing

The claim: the builder reads the working tree but stamps whatever SHA
Tony types, so the one line that makes every future check of this
corpus possible is an assertion, not a check.

Evidence (executed): `main()` prompts `input('Anchor SHA for this
request: ')` and accepts any non-empty string. The builder collects
claims from the files on disk; nothing ties those bytes to the typed
SHA. A typo, or an uncommitted edit sitting in the tree, produces a
request whose anchor is false -- and a false anchor is worse than a
missing one for exactly the reason the protocol gives about
citations: it suppresses the suspicion that would catch it. Related
observation, same drift class: `PROVENANCE_AUDIT.md`'s run history
already contains run rows stamped with SHAs that are not ancestors of
today's HEAD -- recorded anchors that no longer correspond to pushed
history (plausibly benign local commits later amended, but
unverifiable now, which is the point).

Recommendation: the builder reads `.git/HEAD` itself (pure file
reads, no git command line -- two small file opens), displays the SHA
it found, and asks Tony to confirm rather than transcribe. Print a
plain warning with it: "if you have edited files since your last
commit, this SHA does not describe what this request was built from
-- commit and push first." That converts the anchor from a claim into
a check, within Tony's known workflow.

### 7. [SHOULD FIX] Nothing catches the lazy responder -- seed 1's false clean is real as designed

The claim: a responder who copies each Code value into "Your value"
and types `yes` sixty-five times produces a perfectly green report,
and no layer of the checker can notice.

Evidence (read): the checker compares the row's evidence to the
code's value; copied evidence matches by construction. The
instruction "Your value -- the number the source states" helps
honest responders and does nothing against lazy ones. The competitive
two-responder pattern is the primary defense, and it is a good one,
but a lazy pair defeats it, and the failure mode of a tired model
producing plausible confirmations is exactly the failure class this
project has already met three times in citations.

Recommendation, two layers. (a) Cheap and procedural: the Source
column is already required to be "specific enough to find again";
after each return, Tony spot-checks a small random sample of rows
against the stated locator. (b) Mechanical, for at least the pilot:
honest canaries. The builder perturbs the pre-filled Code value in a
few rows, records the true values and the canary keys in a sealed pin
file the responder never sees, and the request DISCLOSES THAT
CANARIES EXIST without saying which rows ("this file contains a small
number of seeded errors; the checker knows which"). The checker then
requires every canary to come back refuted-with-correction; a
confirmed canary quarantines the whole worksheet as unread diligence.
Disclosure keeps the document honest and kills the stale-erratum risk
-- the file announces its own seeding. The checker must exempt canary
rows from L2b drift so the perturbation is not misread as code
movement. This makes responder diligence falsifiable, which is the
project's own test applied to the responder.

### 8. [SHOULD FIX] A mangled Key column silently downgrades the matching regime -- seed 5's case exists

The claim: the two row-matching regimes are selected per table by
whether a recognizable Key header is present, so a returned keyed
worksheet whose Key header got mangled in editing falls back to the
four fuzzy rules without anyone deciding that.

Evidence (read): rule 0 in `match_row` fires only when
`table.column(ROLE_KEY)` finds a header mapping to `key` or `row
key`. Rule 0 itself is built right -- it does not fall through, and
it hunts the table for stale keys before concluding KEY_ABSENT. But
the regime CHOICE happens upstream of rule 0, on header text. A
responder's editor rewraps the table, or they retitle the column
"Keys", and 65 keyed rows silently bind by prose rules 1-4 -- where a
notes cell mentioning another body's value can produce a wrong bind,
which is the exact failure keys were introduced to end.

Recommendation: any worksheet carrying the request's own marker (the
"Extractor version: N. Key format:" line the builder already emits)
must bind by key or fail loudly -- one finding class, no fuzzy
fallback for that file. The marker is already in every emitted
request; the checker just has to honor it.

### 9. [CONSIDER] Dispatch a pilot batch before the full 65 -- and 65 is the right target

Seed 7 in two halves. The target is right: these 65 rows are the
claims the project already TRUSTS -- annotations asserting a check
was done. By the project's own rule, wrong-but-cited is worse than
uncited, so auditing the trusted set before sourcing the 206 known
gaps attacks the invisible-error class first. The 206 are honest
gaps; the 65 are potential false confidence. Keep the target.

But stage it. Findings 1-5 show the instrument had five defects on
the day of its first review; external reviewer effort is the scarce
resource, and a full 65-row dispatch is also the loop's first-ever
end-to-end run. Fix the blockers, then dispatch a pilot of roughly
15 rows chosen to span every row class: clean-source constants, the
six post-swap event rows, string ordinals including one
duplicate-value pair, and a canary or two. Run the checker on what
comes back. Every class of defect the pilot surfaces costs one
conversation instead of the credibility of a 65-row corpus.

### 10. [CONSIDER] Smaller observations, one line each

- **Seed 4 (ordinal stability): two nets already exist and they are
  good.** `shift_check` fires on claim-count or unit change BEFORE
  any value comparison, and L2b compares the row's pre-filled Code
  cell against the code now. The residual silent case is an edit that
  swaps two equal values between ordinals -- harmless, since the
  values are equal. One nuance: a renumbering edit will be REPORTED
  as value drift rather than as renumbering, which sends the reader
  to the wrong repair; acceptable, but worth knowing.
- **Seed 6 (compound answers): self-consistent.** The number and the
  token live in different columns with different reading rules --
  "Your value" is read as free text for numbers, verdict cells are
  read as bare tokens. A compliant range-plus-rule answer lands as a
  RANGE record, which the checker records without routing, so
  following the instructions does not generate send-back noise.
- **Seed 9 (vocabulary): the narrowness is load-bearing; nothing is
  missing once semantics are stated** (Finding 3). UNVERIFIED vs
  UNSOURCED is the distinction registries usually lack, and it is
  here. Resist adding tokens; add definitions.
- **Seed 2 (citation question as scoped): the separation survives
  contact only after Findings 1 and 5 land.** The row already labels
  the verdicted text explicitly ("this is what Citation correct?
  answers"), which is the right mechanism -- but today that labeled
  text is a fragment in 45 rows and a self-supporting narrative in 6.
  Fix those and the scoping is answerable.
- **Seed 3 (who answers): dispatch to GPT and Gemini; Claude only as
  tiebreak.** The builder's output is transcription and is
  mechanically checkable -- I checked it -- so Claude AUTHORING the
  request is fine. But many of the 65 annotations record Claude as
  the 2026-08-02 checker, and a Claude responder would be re-running
  the same model over its own asserted checks, which the project's
  own rule says is not verification.
- **The request could announce filtered numbers.** `physical_claims`
  drops display-instruction numbers (scale advice, file sizes) by
  design; the builder discards the count. One line per string --
  "N numbers here were classified as display instructions and are
  not asked about" -- makes that blind spot announce.
- **Trivial:** Section 3 of the review request says "four fields are
  for the responder"; the emitted table has five blank columns (Your
  value, Source, Value correct?, Citation correct?, Notes). The
  builder's own docstring counts four by folding Source into field 2.
  No consequence; worth aligning the words.

---

## What I did not find

I looked for and did not find: a way for a key to bind to the wrong
row once rule 0 is engaged (the no-fall-through design closes it); a
consistency gap between builder-minted and checker-resolved keys
(shared `worksheet_keys.py`, and the 53-pin suite passes); any
problem with the no-write, no-gate constraints (both are right, and
the stated reason -- a matcher confirming its own writes -- is the
correct fear). Seed 10 invited "this whole approach is wrong." It is
not. The loop's shape -- pre-filled questions, narrow vocabulary,
transcription-grade checking, human-owned causes -- is the correct
response to the failure history that produced it. The defects found
are all in the last mile between the corpus and the responder's eyes,
and every one is fixable this week.

---

*Built on `a872205d17ee5298d1bdc86c614b43506e82b22c` at
https://github.com/tonylquintanilla/palomas_orrery. All counts in
this reply were measured against that commit on 2026-08-15; none is
recalled.*
