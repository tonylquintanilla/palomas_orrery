# Fable Review Response -- The Worksheet Checker (L-192 pre-design)

**Built on `00219d9852c65d653ae49855d3138050dd8f76dd`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Live HEAD re-verified equal to this anchor at read time
(`git ls-remote`, August 12, 2026). I fetched the repo directly at the
anchor; every number below was measured there, not recalled.**

**Type:** Mode 7 pre-design review response (collegial relay).
**Prepared:** August 12, 2026 by Claude Fable 5, for Tony Quintanilla
to carry into a fresh Opus session. Tony holds final judgment.

**On the correction first, because it is mine.** My written rule and my
measurement script disagreed, and 43/34 went to Tony wrong twice before
Opus caught it against the prose. The number is 50/27 and always was.
What this response does differently: every rule stated below was
implemented independently and tested against the production scanner
before being written down. My implementation of the written attachment
rule now agrees with the production scanner **row for row: 50 V2 units,
zero disagreements, and the same four orphan lines (constants_new.py
145-146 and 316-317)**. And my first attempt at that independent leg
was wrong in yet another way -- it classified a string inside a function
as "module-level" because a def is a module-level statement that
contains it -- which is worth recording because it is the third anchor
mistake by a second implementer in two days. The classification
predicate has to be stated as: *a unit is nested if and only if the
SMALLEST statement enclosing it is not module-level.* That wording
survived testing; my earlier wordings did not.

---

## 1. Verdict on the design

**Sound, with changes: the four layers stand, and the design needs an
identity-consistency check, a drift-since-check comparison it is
currently blind to, and DERIVED split out of QUALIFIED.**

The layer structure, the named failure states, the denominator-first
reporting, and the refusal to let a blank output pass are all right,
and they are right for reasons this project has already paid for. The
changes are in section 3; none of them adds a new tool or a new handle.

---

## 2. The five forks

### Fork 1 -- Row matching: (a) plus (c); (b) survives only as a
### role-aware fallback inside (a)

**Recommendation in one sentence: header-role mapping is the primary
matcher, the future-key rule is adopted alongside it, and value-based
search is permitted only against the CODE-VALUE column, never the
evidence column.**

The corpus measurement that decides this: the identifier cells are
bimodal. The constants worksheets are backtick-dense
(`constants_new_citation_verification_gpt.md`: 36 of 37 rows carry a
backticked name; the Claude counterpart 36 of 52), so name matching is
nearly free there. The display-string worksheets carry **zero**
backticked identifiers across all six batch1 files -- their identifier
is prose, plus row codes (Me6, G1, E4) that nothing in the code
references.

What rescues the display-string half is a fact about the tier2 schema
that also dissolves most of (b)'s circularity: those tables carry TWO
value columns -- `Code value` (what the checker read from the code at
the prompt's SHA) and `Your value` (what the checker found in sources).
Matching a row BY its Code-value cell and then verifying L2 against the
Your-value cell is two different cells; it is not finding the row by
the thing you then check. But telling those columns apart requires
header roles -- which is why (b) cannot stand alone and (a) is the
enabler.

The matching rule, stated to be testable, first hit wins:

1. Parse every markdown table; map headers to roles through a registry
   (identifier / code-value / evidence-value / value-verdict /
   citation-verdict / source / notes). A header set the registry does
   not recognise makes the whole worksheet WORKSHEET_UNREADABLE,
   announced, every run.
2. Identifier cell contains the unit's name, backticked or bare
   (constants), or the unit's anchor variable name (strings -- the
   attachment rule already knows the entry that introduces each
   string, so the name is available without new parsing).
3. Claim-prose containment: lowercase both the identifier-plus-notes
   cells and the unit's own string, collapse whitespace, MASK EVERY
   NUMERIC TOKEN, and require a shared fragment of at least 24
   characters. The mask is what keeps this non-circular: the match is
   on the prose around the numbers, never on the numbers.
4. Code-value cell equals the unit's value under L2 normalisation, AND
   at least one masked content word is shared.

A rule must produce a UNIQUE best row; a tie is AMBIGUOUS_ROW,
announced. Anything unmatched is UNMATCHED, announced with unit and
worksheet. The property worth stating: mis-tuning rule 3's threshold
produces visible UNMATCHED noise, not silent wrong matches -- except in
the tie case, which is why the tie must announce rather than pick.

The case I am unsure about, named as requested: **rows that paraphrase
the claim rather than quote it.** Masked containment fails on those,
and they land UNMATCHED. For the 18-file closed set (the artifact
bounds the audit), the honest disposition is a small hand-curated
mapping for the residue, Tony-ruled, in the exceptions file the project
already maintains -- not a cleverer matcher.

**(c) yes, alongside -- it is the fix-the-producer half.** Eight
schemas exist because the worksheet prompts never specified one. Future
prompt templates emit one schema with a key column, and the key is the
unit's anchor name (module plus variable or dict path), which both
sides can compute mechanically. The 18 existing files are grandfathered
as a closed set under rules 1-4.

### Fork 2 -- What counts as a completed check: CONFIRMED yes,
### PARTIAL/APPROX no by default, DERIVED split out entirely

**Framed for Tony's ruling, with my recommendation visible.**

CONFIRMED-class verdicts (YES, CONFIRMED) earn a leg. That half is not
contested.

**DERIVED needs splitting out, and it is different in kind, as the
pre-design suspected.** A derived value was never measured; the verdict
records that the derivation was confirmed. The project has already
placed derived values on their own rung (the L-158 ruling) and the
Track 0 registry design gives them their own zone. So a DERIVED row is
not a leg toward "independently verified against primary sources," and
it is also NOT pending work -- it is closed by derivation, and its
trust question routes to its input constants. The tool should say
"closed-by-derivation," count it separately, and stop there. Putting
the 27-28 DERIVED rows in a queue would manufacture work the audit's
own bounds exclude.

**PARTIAL and APPROX: no leg by default, and here is the tension Tony
is actually ruling on.** Counting them reproduces the Oort failure in
miniature -- an annotation asserting more than the record. Not counting
them strands defensibly-correct values at V3 forever unless someone
re-runs a check; Mercury's PARTIAL, for instance, was a citation nuance
that GPT's YES leg resolved in the same batch. The middle shape I
recommend offering him: a QUALIFIED row earns a leg only by an explicit
per-row ruling, recorded in the exceptions file, visible in the audit.
Never by token class. That keeps every promotion a human decision with
an audit trail, which is what the competitive pattern already assumes
the integrator does.

One mapping the design must state because the tier2 schema forces it:
those tables carry BOTH `Value correct?` and `Citation correct?`. **A
leg toward the cross-checked rung reads the VALUE verdict.** A row with
value-YES and citation-NO is a citation bug to fix in the source line,
not a failed check of the value -- and the reverse (citation fine,
value wrong) is a loud L2/L3 finding. Conflating the two columns would
misclassify both directions.

The remaining ~17 long-tail tokens: exact-match table only, everything
else UNREADABLE and announced. Do not fuzzy-match verdicts. Supporting
evidence from this review: my token count and the pre-design's disagree
by up to 62 on YES (209 vs 271) because we used two different counting
rules on the same corpus -- which is precisely why L3 must parse the
verdict COLUMN by header role and report which column it read, not grep
for tokens.

### Fork 3 -- Writing: `--propose` mode, patch script, never in place,
### with the row quoted verbatim beside every proposed annotation

**Recommendation in one sentence: the third option, with one added
requirement that addresses the self-satisfaction objection directly.**

The objection is real and it has a precise shape after this week: the
risk is not forgery, it is a MATCHER BUG writing annotations against
wrong rows and the same matcher later confirming them -- the shared-
misreading failure from this morning, mechanized. The mitigation is
that the propose artifact must quote each worksheet row verbatim next
to each proposed annotation, so Tony's review runs against the
evidence, not against the tool's claim about the evidence. The batch is
small (27 units plus the two orphan headers), so full human review is
feasible, and a Mode 7 spot-check of the patch is cheap if wanted.

Strictly-read-only is not the safe option it sounds like. Hand-copying
thirty-odd filenames, dates, and checker names is exactly how
annotation errors enter -- the skill's own Worksheet First, Annotation
Second rule exists because of one. A tool that copies the filename from
the row it verified is less error-prone than a hand, provided the hand
still holds the pen at the review step. The patch-script format is the
project's standing delivery mechanism -- anchored, fingerprinted,
all-or-nothing -- which here cuts only one way: in favour.

### Fork 4 -- What makes it run: hang the scoped check off the moments
### drift enters, and re-measure the cost premise rather than inherit it

**Recommendation in one sentence: an incremental mode cheap enough to
ride the existing pre-push scanner routine, scoped to what changed,
report-only at first; the full-corpus mode stays manual.**

I am arguing against the ledger's cost ruling explicitly, as invited:
34 markdown files is kilobytes, and with a per-file content-hash cache
(state alongside `provenance_history.json`, same pattern as L-189) the
steady-state cost of "nothing changed" is a hash comparison. If the
ledger's cost concern was something other than file size -- output
noise, runtime budget of the maintenance runner, something I cannot see
from here -- then that reason should be stated where the ruling lives,
and I defer to it.

But cost is not the deciding argument; moment-of-introduction is. The
drift enters at three doors, and each has a hook that already exists or
nearly does:

- **A value edit** -- `constants_change_report.py` already names the
  worksheets to re-check. Wire the checker there, scoped to those
  files. This door is half-built.
- **An annotation edit** -- the scanner already runs pre-push on the
  active build path. The checker runs beside it, scoped to annotations
  whose (unit, worksheet) tuple hash moved since the last recorded run.
- **A worksheet edit** -- the content-hash cache notices by itself.

Report-only at first: the checker's findings go in the audit, and they
do NOT gate pushes. Expanding the Tier-1 push gate is a separate,
explicit Tony (decide), not a side effect of wiring a new tool into the
same moment. And whatever carries it must print its denominator on
success -- the runner's current print-only-on-failure behaviour is the
exact gap that hid 77-to-50 (do-item 6), and this tool's output is the
kind that gap eats.

### Fork 5 -- The nine uncited worksheets: one line steady-state, full
### list only when the set changes

**Recommendation in one sentence: report the count and the date it last
changed on every run; print the list only when the set differs from the
recorded state.**

"9 uncited worksheets pending wiring -- unchanged since 2026-08-12" is
one line, loses nothing, nags no one. The state file from fork 4 makes
the delta free. When the set changes in either direction -- a new
uncited file appears, or one becomes cited -- the full list prints
once. The pending-work ledger note remains the durable record; the
checker's line is a pointer, not a second store.

---

## 3. What the design misses

**First: identity and date are asserted by every annotation and checked
by no layer.** L0-L3 verify existence, row, value, verdict -- but the
annotation also names WHO checked and WHEN, and the V2 rung is defined
by two DISTINCT checkers. Two annotations naming different checkers
whose evidence is one leg would pass all four layers and fake the rung.
This is not hypothetical machinery: the corpus already contains a file
explicitly warning against exactly this (the DELTA file: "two Claude
passes are one model running twice"). The check is cheap and testable:
*the named worksheet's filename must contain the annotation's checker
token, case-folded.* Measured today: **134 of 134 pass**, and all 18
cited filenames carry a model token, so the rule needs no exceptions
map on day one. A clean baseline is the right time to pin a check --
this is L0's situation, and the same answer applies: it can still fail,
so it is worth having. The date is weaker: report annotation dates
earlier than the worksheet's own stated date as a diagnostic, no gate;
worksheets carry their dates in inconsistent prose and a strict rule
would false-positive on legitimate next-day annotation writing. That
unsure case is named deliberately.

**Second: the design is blind to drift-since-check, and the schema
already contains the cure.** The tier2 tables record `Code value` --
the value the checker read from the code at the prompt's SHA. Comparing
that cell to the code's value NOW detects a value edited after its
check, which is the committed-history failure the whole tool exists to
reach, caught directly rather than inferred. Split L2 in two: **L2a**,
evidence agreement (code-now vs the evidence-value cell), and **L2b**,
drift-since-check (code-now vs the code-value cell), failure state
DRIFTED, loud. L2b only exists where the schema carries the column --
header-role mapping knows when that is.

**Third: L2a's comparison must be exact-or-rounded, not "within
tolerance."** Mercury is the cautionary case sitting in the corpus:
2439.7 (code, NSSDCA) vs 2439.4 +/- 0.1 (JPL, in a worksheet cell). A
significant-figures tolerance calls those a match at three figures and
the finding vanishes. The testable predicate: MATCH iff the values are
equal after unit normalisation, OR the evidence value equals the code
value rounded to the evidence cell's displayed precision. A range cell
("2000-5000 AU") is never MATCH; it is RANGE, its own class, surfaced.
A comparison that needed a unit conversion is MATCHED-VIA-CONVERSION,
its own class, because the conversion imports the project's own
constants into the comparator and that dependency should be visible.

**Fourth: the one verdict-less citation needs a named disposition, and
I identified it.** It is `worksheet_claude_batch1_blind_lookup_DELTA.md`,
cited exactly once, from `eris_visualization_shells.py:41` (the Claude
leg on Nimmo & Brown). The file is a self-declared delta record, not a
worksheet, and it says so. Filed-as-received is the standing rule, so
the file is legitimate; the checker cannot read it and should not
pretend to. Disposition: one hand-ruled exceptions entry (Tony decide:
does that pass constitute a completed Claude leg?), else it reports
UNREADABLE every run, which is the honest default.

A smaller one, diagnostic not layer: the rung is per-unit but the
evidence is per-claim, and a display string can carry many claims. For
each cross-checked string, report claims-addressed over claims-present
as a count. Bounded by what the string contains at this commit, so the
denominator cannot grow by imagination.

**Ledger economy, answered plainly: this is one item.** The checker,
its propose mode, its state file, and fork 2's verdict ruling are all
L-192's body. The value-edit trigger rides the existing
`constants_change_report.py`; the runner printing fix is already filed
under L-188's do-item. No new handles.

---

## 4. Second questions, listed separately

1. **Reconcile the YES count once the column parser exists.** 271 and
   209 are both rule-dependent grep-level numbers; neither is wrong
   until the rule is stated, and the parser's number will supersede
   both.
2. **State-file placement**: `data/` beside `provenance_history.json`
   seems right; mechanical, not a design question.
3. **Boundary note**: the eighteen inline literals duplicating cited
   constants (handoff do-item 4) can drift with no worksheet ever
   naming them -- outside L-192's bounds by construction, already
   filed. Worth one sentence in the checker's docs so nobody expects
   this tool to catch that class.

---

*Review response prepared August 12, 2026 with Anthropic's Claude
Fable 5, built on `00219d9852c65d653ae49855d3138050dd8f76dd` at
https://github.com/tonylquintanilla/palomas_orrery*
