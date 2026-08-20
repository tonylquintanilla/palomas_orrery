# Review return -- L-214 leg vocabulary
# Second leg, Claude Fable 5

**Reviewing `REVIEW_PROMPT_L214_20260819.md` and
`L214_MEASUREMENT_20260819.md`, both cut from
`97c520177b18d69e6b5d3943557fdea47f56e8bf` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**

This review is built on those two documents alone. The repo was
deliberately not fetched and no project skills were loaded, so that the
WHAT I COULD NOT JUDGE section reflects the prompt's actual
sufficiency rather than gaps this reviewer quietly filled.

## Reviewer disclosures, before anything else

**This leg is partially contaminated, and Tony should weigh it as
such.** This session runs inside the Paloma's Orrery project. It
carries resident memory of the project's principles, the protocol, and
the general state of the provenance work. It did not carry the L-214
design conversation or the six-part proposal -- those arrived only in
these documents -- but it is not the fresh-chat-outside-any-project leg
the dispatch rule prescribes for full independence.

**The Part-A-before-Part-B ordering cannot be executed by a model.**
The prompt arrived as one document in one context; there is no way for
me to have written Part A without Part B already read. I mark
convergences honestly below. This is itself a finding about the
dispatch protocol: for a model leg, the anti-anchoring instruction as
written is a check that cannot fail -- nothing in any answer
distinguishes a reviewer who complied from one who could not. If the
split matters, it needs two physical dispatches: Part A sent alone,
answer collected, then Part B sent.

**One verification I could run without the repo:** Part 2's simulated
counts reconcile exactly against Part 1's quoted text. Rebuilding the
match set with only lowercase `Note` added, the multi-line sites are
SUN_RADIUS_KM (2 continuation lines), CHROMOSPHERE_PHYSICAL_KM (2),
STREAMER_BELT_RADII (1), ROCHE_LIMIT_RADII (1), mercury (2), moon (2)
-- six sites, ten lines, with venus's `NOTE:` and Parker's
`HELIOCENTRIC:` correctly excluded from a `Note`-only rebuild. The
measurement is internally consistent, and its two method checks (the
reproduced 12/55 and the reproduced known-good zero) are the right
shape of evidence.

---

## Part A

### A1 -- the shape

The claim first: the missing piece is not only a named state. It is a
second output channel.

The builder currently has exactly one output, the request. Anything
that must not enter the request can therefore only be expressed as
silence, and "withheld on purpose" and "nobody has classified this"
are the same silence. That is why correct behaviour and the defect
share a code path: with one channel, there is no way for a withhold to
leave evidence. Give the builder two outputs -- the REQUEST, which the
responder sees, and a REPORT, which the project sees at dispatch time
-- and every state becomes a pair of visible behaviours. Nothing exits
through an unmatched branch, because there is no disposition whose
implementation is "do nothing."

The states, and what each does to a line:

1. **VERDICTED** (`Source`). Request: shipped, ruled on. Report:
   counted.
2. **CONTEXT** (`Ref`, `Also`, `See`, `Derived`, `Calculation`,
   `Note`). Request: shipped, not verdicted. Report: counted.
3. **RECORD** (`Cross-checked`, `Removed`, `Corrected`, `Resolved` --
   a named set). Request: withheld. Report: counted by label, e.g.
   "2 record legs withheld at this site." The count is what makes
   purpose distinguishable from accident: a deliberate withhold can
   say how many things it withheld; a fall-through cannot say
   anything.
4. **HELD** (a new label, name Tony's -- candidates in B2). Withheld,
   free-form, no grammar. Request: withheld. Report: counted. This is
   the home the moon line never had.
5. **UNCLASSIFIED** (any other labelled line in a claim block).
   Request: **withheld** -- this is where I diverge from the proposal,
   argued in B1. Report: full text and location, per rulings 2 and 3.
   The run continues. The count ratchets toward zero, because every
   report either promotes the label into the vocabulary or fixes the
   source the way ruling 4 fixed the four odd labels. Steady state:
   this state is empty, and its emptiness prints as a number.

Success carries evidence, in the style the measurement itself models:
"55 claim sites; 55 Source legs shipped; N context lines shipped; M
record legs withheld; 0 unclassified." That line cannot print unless
the classification actually ran.

Why UNCLASSIFIED withholds instead of ships: the builder cannot know
whether unknown prose is contaminating, and the two failure modes are
not symmetric. Withhold-by-default fails visibly and recoverably -- a
responder misses context, the report says exactly what was missed, and
the next dispatch carries it once a human classifies it.
Ship-by-default fails invisibly and unrecoverably -- a contaminated leg
does not error; it converges, and convergence is this system's success
signal. Under "the tool carries; the reader judges," shipping unknown
prose is a judgment: it is the builder deciding the prose is safe.
Note also that this reading is, I believe, what ruling 2 says: "report
so we can deal with it by reading" locates the reader on the project
side, in the report channel, not in the outbound request.

### A2 -- the different line

`moon_hill_sphere_info`. It is record semantics wearing a context
label: it names which model produced the range, states that the other
two did not publish it, and declares that a second leg is owed.
Shipping it pre-answers exactly the re-dispatch it describes.

Two implications beyond the measurement's own framing of it:

**The vocabulary caused the misfiling.** There was no withheld
free-form slot, so an author holding review-history prose had exactly
one label meaning "miscellaneous note" and used it. The moon line is
not an author error to be corrected once. It is the signature of a
missing state, and the class will recur until the state exists,
because people file prose under the least-wrong label available.

**Ruling 1 flips this failure class's polarity.** Under the old regime
the misfile was accidentally safe -- dropped along with everything
else. The moment `Note` ships, the identical authorial habit becomes a
live contamination path. So the fourth state is not cleanup that can
follow ruling 1 at leisure; it is a precondition of ruling 1 landing
safely. The deployment-order consequence is in B1.

(Convergence marked: the measurement's Part 3 identifies the line and
the contamination stake. The two implications above are mine.)

### A3 -- the prediction

Honest position first: the measurement was in my context before any
prediction could form, so the ritual is void for this leg. What I can
say is that the quoted gathering loop entails Part 2's result and the
direction is fully derivable from section 1 alone: admit `Note` to
`LEG_RE` and every `# Note:` opens a leg; its unmarked tail becomes
`unmarked`; the L-195 ratchet refuses the run. The exact 10-at-6
needs the corpus, and I verified those numbers reconcile against
Part 1's quoted text (see disclosures).

What the consequence teaches about the continuation-marker rule:
**vocabulary admission is a migration, not a configuration change.**
The rule couples recognition to continuation-marking so that no label
can enter the shipping set with its tail silently truncated -- and
truncation is the worst of the three possible states, worse than the
whole note being dropped, because a shipped first line reads to the
responder as a complete note. Today the whole note is invisible, which
is at least consistent. A naive addition would ship the first line and
drop the tail, which is inconsistent and undetectable from the
receiving end. The refusal is the only thing standing between those
two states, and Part 2 is a demonstration of the refusal working --
a check failing correctly, on demand. The cost the rule imposes (every
admission forces touching the corpus) is the feature.

One forward obligation falls out: every future label admission carries
the same sweep. The refusal will announce it regardless, but the
session that hits it cold will lose an hour rediscovering why. Worth a
line in the skill that fires on this work.

### A4 -- a different framing

Three, in descending usefulness.

**Channels, not states.** Already used in A1, but stated as the
reframe it is: the design conversation has been asking "which set does
each label belong to?" The prior question is "how many outputs does
the builder have?" With one output, the taxonomy debate is unwinnable,
because withholding has no representation -- it can only be silence.
With two outputs, every state is a (request, report) pair, and the
"fourth state" stops being mysterious: the vocabulary always implied a
two-by-two -- travels or withheld, grammar-validated or free-form.
`Source`: travels, validated. `Note`: travels, free. The record four:
withheld, validated. The empty cell is withheld-and-free, and the moon
line has been trying to live in it all along.

**Author-time, not dispatch-time.** All classification currently
happens when a dispatch is built, which can be months after the
comment was written. Vocabulary totality -- every label in a claim
block belongs to some named set -- is a corpus property, checkable by
the scanner that already walks these files in routine, at the moment
the author who wrote the line is still in session. The builder keeps
its defensive handling (depth), but the steady-state catch moves
upstream to the producer. Fix the producer, not the N dispatches.

**Separate the stores** -- named in order to be set aside. Every
defect in this episode is a multiplexing artifact: one comment block
above a constant is serving three audiences at once -- the responder
(context), the future maintainer (code notes), and the review record
(history). The radical answer is to evict the review record from
source entirely and let the worksheets and ledger be the only record
store, at which point the builder ships everything and withholds
nothing. I set it aside: the annotation grammar and its linkage
checker embody a standing decision that record annotations live in
code, and one misfiled line does not justify re-litigating it. But the
framing explains the pressure: the vocabulary keeps growing states
because the file hosts audiences.

---

## Part B

### B1 -- differences from the six items, ranked

**1. Item 3's destination.** The proposal routes unclassified text
into the outbound request; my structure routes it to the project-side
report and withholds it from the request. This is the difference that
matters most, for two reasons. It sets the safety polarity for exactly
the material nobody has ever screened -- and B3 argues that material
is where the moon-line class lives. And I read Tony's recorded ruling
-- "report so we can deal with it by reading not refusing" -- as
locating the reader on the project side. If that reading is right, the
implementation has inverted the ruling it implements. The documents
use "worksheet" for both the outbound request and the return, so I
flag the term rather than assume it (final section); but the B3 gloss
makes the proposal's intent unambiguous, and it is the intent I am
disputing.

**2. The withheld free-form state is present from the start.** The
proposal discovers its need through item 6's failure and leaves it
unresolved. A2 argues it is a precondition of ruling 1, not a patch to
be found later.

**3. The six items are a list; they need to be a migration with an
order constraint.** As sequenced, items 1 and 5 are landable while
item 6 is known-defective. In that window the moon note carries valid
`Note+:` markers and travels cleanly on the next moon-row dispatch --
the ratchet protects only until the marker sweep completes, and after
that nothing refuses. The constraint: the moon line leaves `Note`
before or in the same transaction as the item-5 sweep.

**4. Item 5's count is the pre-item-4 number.** After item 4 converts
venus's `# NOTE:` and Parker's `# HELIOCENTRIC:` to `# Note:`, their
continuation lines -- one each, quoted in Part 1 of the measurement --
join the unmarked set, and the other two converted instances may add
more. The sweep is at least twelve lines, not ten. The refusal will
announce this at first run, so it is a manifest defect rather than a
silent one -- but a migration whose own manifest undercounts its steps
is evidence the six items were derived separately rather than
integrated as one change.

### B2 -- is the fourth state right?

Yes -- and it is not an addition. It is the fourth cell of the
two-by-two that was always the real structure: travels-or-withheld
crossed with validated-or-free. Naming the axes matters more than
adding the state, because the axes give the next author choosing a
label a rule instead of a list, and they prevent a fifth ad-hoc state
appearing the next time a line fits nothing. Candidate names: a
free-form `# History:` reads naturally for review-history prose;
`# Held:` states the disposition itself. Naming is Tony's.

One cheaper instance-level answer belongs on the table before the
state is built. The moon line's content -- a leg owed, who published
what -- is queue state. If the reconciliation queue or ledger is
already the authoritative store for "second leg owed" (I could not
verify this from the documents; final section), then the code comment
is a mirror that created a hazard, and deleting it in favour of the
real store solves instance one with zero new machinery. That does not
remove the need for the state -- A2's argument stands that authors
will keep producing withheld-worthy prose -- but the first occupant of
the new state should be prose that has no other home, not prose that
already has one.

Symptom-of-a-worse-error check: the candidate worse error is
co-location itself (A4, third framing). That is real pressure, but it
is ruled infrastructure, and one misfiled line does not overturn it.
The fourth state is the right answer at the right scope.

### B3 -- does item 3 create an unnamed contamination path?

Yes, and structurally -- the moon line is an instance of a class, not
a fluke. Three reasons to expect more:

**The corpus was written under a regime where unrecognized labels were
inert.** Any author could write anything under any invented label with
no consequence, and `HELIOCENTRIC:` proves invention happens. Item 3
retroactively publishes prose that was written as private. The 22
unreached `Cross-checked` lines the measurement announces are adjacent
evidence that record material sits loose in these files in ways the
tooling does not fully reach.

**Label invention is ongoing**, and item 3 makes every future invented
label ship-by-default at the moment of invention -- the highest-risk
moment, since an invented label has by definition never been screened
by anyone.

**Nothing in the pipeline can stop it, by design.** The builder must
not judge prose. Under item 3 the only screen is a human eye on
outbound requests, a discipline that thins as the corpus grows and the
pipeline earns trust.

What stops the class: channel separation -- unknown material withheld
and surfaced, inert until a human classifies it -- plus the fourth
state, so the misfiling pressure itself drops. Two narrower guards are
available and both are lexical, not semantic, so they stay inside
"the tool carries": (a) risk concentrates on re-dispatched rows, which
are exactly the rows possessing record legs, and the presence of a
record leg is syntax -- the report can say "this row has record legs
and ships N context lines; read them before dispatch," pointing the
eye where the risk lives without interpreting anything; (b) optionally,
a fixed keyword tripwire over outbound context text (the record label
names, "worksheet," the model names) that flags into the report and
never refuses. I mark (b) as optional and mildly hazardous: a
half-defense can breed the trust that lets the other half lapse.

### B4 -- two homes for the record set

Real risk, and the exact class this project has been burned by
repeatedly. The right single home is the module that already owns the
grammar: the measurement names `worksheet_keys` as holding `LEG_RE`,
`OTHER_LABEL_RE`, and `continues_a_leg`. The verdicted label, the
context tuple, the new named record set, the held label, and every
regex derived from them belong there as the single producer; the
request builder, the Resolved-walking tool, and the linkage checker
all import. The hazard is not naming the set twice in prose -- it is
compiling it twice from two literals. If the walking tool currently
carries its own `Resolved` pattern, then item 2's implementation IS
that tool's migration to the shared import; otherwise item 2 recreates
the disease it treats.

And per the project's own gate: the totality check -- every label in
the corpus belongs to some exported set -- must live in a flow that
actually runs, meaning the scanner or the builder's own report, not a
test file nothing executes.

### B5 -- the six-month silent failure

Record-semantics prose under a shipping label, dispatched, anchoring a
leg. Every other failure mode in this design has an alarm: unmarked
continuations refuse, unclassified labels report, grammar violations
fail the linkage checker. This one produces a valid request, a fluent
return, and -- the actual damage -- convergent legs. Convergence is
this system's success signal, and contamination manufactures it. Six
months out, every observable symptom is an improvement: agreement
rates up, reconciliation queue down, dispatches smoother. Independence
has quietly become circulation, and nothing in the pipeline can say
so. That asymmetry -- the worst failure mimics the best outcome -- is
the strongest single argument for withhold-by-default on anything
unscreened.

Secondary candidates, briefly. The report channel going unread: a
report nobody opens is a check that cannot fail, so bind it into the
output the dispatch flow already produces, with an evidence-carrying
success line and a ratchet on the unclassified count. Vocabulary drift
if the sets are ever duplicated (B4). And `Note` becoming the junk
drawer: it is now the least-committal shipping label, prose will
accrete there, requests will bloat, and record-semantics will keep
gravitating to it because it remains the path of least resistance.
Note-lines-per-row is a slow gauge worth an occasional glance.

---

## CHALLENGE

None against section 3's four rulings as Tony stated them. One against
the proposal's reading of rulings 2 and 3: if "reported into the
worksheet" means the outbound request, I dispute that reading, not the
ruling -- "so we can deal with it by reading" locates the reader on
the project side. If Tony's actual intent was responder-side shipping,
then this review's central objection (B1 point 1, B3) should be read
as a challenge to that intent: it trades the method's one
non-negotiable property, leg independence, for convenience in the rare
case.

---

## WHAT I COULD NOT JUDGE

- **Which document "worksheet" denotes in ruling 3 and item 3.** The
  documents use the word for both the outbound request and the return.
  My most consequential critique pivots on that referent.
- **Where `problems` and the existing reporting currently surface** --
  request, return, console, or a file. The channel structure I propose
  may already partly exist; these documents do not show it.
- **The `Resolved:` grammar and the linkage checker** are quoted
  secondhand. Whether a relaxed free-form variant could live inside
  them, rather than a new label beside them, is beyond these documents.
- **Whether the reconciliation queue or ledger already carries "second
  leg owed" for the moon row** -- this decides whether the moon line
  is a redundant mirror (delete it) or the sole record (rehome it).
  Marked inference: resident memory of this project suggests the
  ledger tracks owed items, but that is memory, not these documents,
  and I flag it rather than rely on it.
- **The other tool that walks raw text for `Resolved` legs** -- one
  sentence of description; its migration cost under B4 is unknowable
  from here.
- **The 22 unreached `Cross-checked` lines.** Announced, attributed to
  record legs "attaching to no unit," and parked. I cannot judge
  whether orphaned record annotations are expected structure or a
  second latent defect. It reads like a finding living in a footnote;
  it deserves its own handle and a look.
- **The counts 12/55 and the 128-file scope** -- method-verified by
  the measurement's own two checks, which is the right shape of
  evidence, but this leg could not rerun them.

---

*Review performed August 19, 2026 by Anthropic's Claude Fable 5, in an
in-project session (contamination disclosed above). Built on the two
documents cut from `97c520177b18d69e6b5d3943557fdea47f56e8bf`; no repo
access used.*
