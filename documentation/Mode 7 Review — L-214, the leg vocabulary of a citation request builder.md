# Part A

## A1. Structure the vocabulary by detection first, policy second

My ruling is that the present structure is conflating two different questions: **“Is this a labelled leg?”** and **“What are we allowed to do with this leg?”** Those should be separated.

The first stage should recognize any syntactically valid labelled comment. In other words, the parser — the code that turns the comment block into pieces — should recognize the general shape `# Label:` without yet deciding whether that label is `Source`, `Note`, `Resolved`, or something nobody has classified. Today `LEG_RE` recognizes only labels already admitted to `VERDICTED_LEG` or `CONTEXT_LEGS`; consequently an unknown label and an intentionally withheld record label both disappear through the same unmatched branch. That is the architectural source of L-214.

After detection, a single vocabulary registry should classify the label. By “registry” I mean one authoritative table of valid labels and their behavior, not separate tuples that different tools independently know about.

I would give every known label at least two independent properties.

The first property is **transport role**. A `VERDICTED` leg travels and receives a verdict. A `CONTEXT` leg travels but does not receive a verdict. A `RECORD` leg is deliberately withheld because it carries prior review history. An `UNKNOWN` leg has been detected syntactically but has no transport classification yet.

The second property is **grammar**. Some legs are free-form prose. Some have a strict format that another checker validates. `Resolved`, for example, is RECORD by transport role but has a strict linkage grammar. A future free-form prior-review note could also be RECORD while having no such grammar.

That separation matters. “Withheld” is a transport decision. “Free-form” or “strictly validated” is a grammar decision. They should not be forced into the same state variable.

The dispositions then become straightforward. `Source` travels and is verdicted. `Ref`, `Also`, `See`, `Derived`, `Calculation`, and now `Note` travel as context. `Cross-checked`, `Removed`, `Corrected`, and `Resolved` are positively recognized and deliberately withheld. An unclassified label is positively recognized as unclassified and reported with its text rather than silently vanishing.

I would add one qualification to that last sentence: **reported does not have to mean supplied as evidence to the outside reviewer.** The builder should preserve and surface the unknown text to Tony, but the transport stage should not pretend an unknown label has already been judged safe to send. That distinction becomes important in A2 and B3.

This preserves the decisions already made: `Note` becomes context, unknown labels are reported rather than causing refusal, the report contains their text, and the four odd spellings are corrected at source rather than institutionalized as parser aliases.

## A2. The Moon line shows that transport role and prose format are different things

The exceptional line is the `moon_hill_sphere_info` note:

> `SINGLE-LEG. Only the Claude tier-2 worksheet carries the 58,147-64,901 km range... A second independent leg is still owed for V2 scoring.`

The measurement correctly identifies why it is different. This is not ordinary scientific context surrounding a value. It records what previous reviewers did and did not conclude and explicitly says another independent review is owed.

Therefore it must not travel to that next independent reviewer.

The important implication is larger than “this one Note needs a different label.” It demonstrates that `Note` cannot mean “miscellaneous prose which is always safe to send.” The line's problem is not its syntax. Its problem is its **provenance role**: it records prior adjudication.

At the same time, moving the prose under `Resolved` merely because `Resolved` is withheld is structurally wrong. The prompt tells us that `Resolved` has its own strict grammar and linkage checker. The Moon sentence is a record, but it is not a `Resolved` record.

I therefore think the vocabulary needs a free-form record label. I would give it a name that states why it is withheld, something like `Review-note` or `Prior-review`, rather than something generic like `Internal`. The exact word is less important than the structural rule: it belongs to the RECORD transport class while using a free-form grammar.

That does **not** require a fourth transport state. It requires recognizing that RECORD can contain more than one grammar.

The Moon line is valuable because it reveals the hidden axis.

## A3. Yes, I would predict the refusal

From the gathering loop in section 1, my prediction before consulting the measured result is that adding `Note` to the recognized vocabulary will expose previously invisible continuation defects.

Today an unrecognized `# Note:` closes the open run. Once `Note` becomes recognized, it opens a real leg. Any following comment that semantically continues that note but lacks `# Note+:` will therefore satisfy the existing unmarked-continuation test. The builder should refuse.

The measurement confirms exactly that: adding `Note` produces **10 unmarked continuation lines at 6 sites**, changing the builder from writing successfully to refusing.

So yes, that is the consequence I independently expect from the code shown.

I regard that consequence as evidence **for** the continuation-marker rule, not against it. The rule has found text whose attachment had previously been ambiguous only because the containing leg was invisible. Once `Note` becomes a real leg, its continuation lines should be made real too.

The design lesson is that adding a recognized label is a schema migration, not merely a one-word parser change. Recognition and continuation cleanup need to land together. The proposed ten `# Note+:` edits are therefore not cleanup after the design; they are part of implementing the design correctly.

The marker also retains an important property described in the prompt: it says which leg a continuation belongs to, rather than allowing nearby prose to be absorbed merely because it follows another line. I would preserve that ratchet.

## A4. The different framing is: stop parsing “approved labels” and start parsing “labelled statements”

I think there is a structurally different framing, and it is the main recommendation of this review.

The system is currently treating its label vocabulary partly as a parser grammar. I would instead treat the comments as a small typed document format.

First detect every labelled statement. Then classify it. Then validate its continuation form. Then apply its transport policy. Then, where applicable, apply its label-specific grammar checker.

That ordering removes the possibility that “not in our approved vocabulary” means “does not exist.”

Under this framing, an unknown `# Whatever:` line is not a parser failure and is not context. It is a successfully parsed labelled statement whose classification is missing. A RECORD line is likewise successfully parsed, but its classification says to withhold it. The two cases can no longer share a silent branch.

This also produces a useful invariant for the project: **every syntactically labelled line attached to a claim must finish the builder in one named disposition.** It was sent for verdict, sent as context, withheld as record, or surfaced as unclassified. There should be no fifth disposition called “fell through the regex.”

That is the structural change I would make even if none of the twelve measured examples existed. The measurement demonstrates why it is needed: the current mechanism dropped twelve labelled lines at twelve of fifty-five claim sites without saying so.

# Part B

## B1. The six-part proposal is directionally right, but it stops one layer too low

Items 1, 2, 4 and 5 are sound migrations. `Note` should become context. Record labels should become explicit rather than disappearing accidentally. The odd labels should be normalized at source. The newly recognized multiline notes need their continuation markers.

The largest difference from my Part A is that I would not solve this primarily by expanding `CONTEXT_LEGS` and adding `RECORD_LEGS`. Those sets describe policy, but the present defect begins earlier: `LEG_RE` itself uses the policy sets to decide what constitutes a leg.

That coupling should end.

The most important change is therefore not `RECORD_LEGS`; it is **generic label detection followed by classification through one registry**.

That makes item 3 safer as well. “Anything in neither set” should not have to be discovered by failing to match the parser that recognizes the sets. It should already have been recognized as a labelled statement and then receive the explicit classification `UNKNOWN`.

Item 6 is where the proposed structure reveals its own limitation. The Moon line should not be forced into `Resolved`. It needs a free-form RECORD label.

## B2. Do not add a fourth state merely to encode grammar

A fourth state called something like “withheld free-form” would work operationally, but I think it would preserve the conceptual mistake.

The Moon line and `Resolved` have the same transport policy: both must be withheld from the next reviewer. They differ in grammar.

So I would not make “withheld free-form” a peer of VERDICTED, CONTEXT and RECORD. I would keep RECORD as the transport role and give RECORD legs different grammar profiles.

`Resolved` can be RECORD plus strict resolved-linkage grammar. `Review-note` can be RECORD plus free-form grammar.

That arrangement also scales better. If another structured record form appears later, you do not need a fifth state for “withheld structured but structured differently.” You add another RECORD label with another validator.

The defective item 6 is therefore a symptom of a structural error, but a fairly precise one: **transport classification and grammar classification have been collapsed into one label taxonomy.**

## B3. Yes, automatically shipping unknown text creates a contamination path

There is a structural reason to expect more Moon-like cases.

An unknown label is, by definition, a label whose semantic role the system does not know. Therefore the system has no basis for asserting that its contents are safe context for an independent reviewer.

Some unknowns will be harmless scientific notes. Some will be maintenance notes like the duplicated Venus text. The measurement already contains that benign example. But future unknowns can just as easily contain prior reviewer conclusions, status information, discarded values, instructions to maintainers, or other material that changes how an independent reviewer approaches the row.

The Moon example proves that this is not hypothetical.

The structural protection I recommend is **quarantine without disappearance**. Unknown labelled text should be preserved and reported to Tony with the actual text, satisfying the ruling that unknown labels are read rather than refused. But it should not automatically enter the evidence bundle shown to the outside reviewer until its label has been classified.

That is different from today's defect. Today it vanishes. Under quarantine it becomes conspicuous to the operator.

If the project requires the diagnostic to live in the generated worksheet itself, then it should at minimum be segregated as an explicit builder diagnostic and identified as unclassified rather than presented alongside citation context. But that is weaker protection because the outside model still sees the words and can be anchored by them. A human-facing pre-dispatch diagnostic is structurally cleaner.

The builder still does not interpret the prose. It simply declines to infer that “unknown” means “safe context.”

## B4. The duplicated record vocabulary is a real risk; give it one home

Yes, I think this is exactly the kind of duplication that will eventually drift.

If the request builder knows that `Resolved` is a RECORD leg, while a separate checker independently knows that `Resolved` is a special raw-text construct, then the system has two places that must change when the vocabulary changes.

The single home should be the label registry.

That registry should know that `Resolved` exists, that its transport role is RECORD, and that it has a particular grammar type. The request builder obtains the RECORD set from the registry. The linkage checker obtains the labels relevant to its validation from the same registry. Neither should independently spell the authoritative list.

This does not require putting all validation logic into one giant module. The actual `Resolved` validator can remain wherever it properly belongs. What should be centralized is the declarative fact that `Resolved` is a known leg, has RECORD disposition, and is governed by that validator.

That distinction keeps the “one source of truth” small without making one module responsible for everything.

## B5. The dangerous six-month failure is not a crash; it is a successful request containing the wrong information

The design fails silently six months from now if a new label can be introduced and a valid-looking worksheet can still be produced while the label either disappears or travels under the wrong policy.

The same is true if a new RECORD label is added to one consumer but not another, if a newly recognized multiline label exposes continuation lines but its migration is not performed, or if prior-review prose is casually stored under `Note` because `Note` has become the project's general-purpose comment label.

The prevention mechanism should be expressed as invariants rather than memories.

A syntactically labelled attached line must always receive a disposition. No labelled line may silently disappear. Every label's role comes from one registry. No RECORD leg may enter the responder payload. An UNKNOWN leg must visibly surface to the operator. A recognized multiline leg must obey its continuation-marker rule. The registry and the specialist validators must agree about which labels they own.

The builder should also report counts of what it did. A run that says, in effect, “12 context legs carried, 4 record legs withheld, 1 unknown label reported” is much harder to misread than one that silently omits a category.

That is how I would make future vocabulary drift announce itself without making every vocabulary imperfection a refusal.

# CHALLENGE

I do not challenge Tony's four rulings as stated.

I would, however, challenge a narrower implementation interpretation of ruling 2 if “reported” is taken to mean **automatically shown as citation context to the outside reviewer**.

“Report so we can deal with it by reading not refusing” does not require the system to classify unknown prose as safe evidence. The Moon line demonstrates why those are different decisions.

My interpretation preserves the ruling more literally: unknown text is never dropped and never blocks generation merely because it is unknown; it is surfaced, with its text, for human classification. What it is *not* allowed to do is silently acquire CONTEXT semantics merely because it was not recognized.

# WHAT I COULD NOT JUDGE

I could not determine from the supplied material exactly how `continues_a_leg` decides that an ordinary comment line is a continuation rather than unrelated prose. The measured behavior gives confidence in these examples, but not enough information to judge that detector's general false-positive or false-negative behavior.

I also could not determine whether the builder already has a human-facing pre-dispatch diagnostics surface separate from the worksheet sent to the outside reviewer. That matters to my quarantine recommendation. If no such surface exists, adding one is a workflow choice beyond what the quoted code establishes.

I could not determine the grammars, if any, attached to `Cross-checked`, `Removed`, or `Corrected`; the prompt gives the strict grammar only for `Resolved`. I therefore cannot say whether the proposed registry should associate validators with all four RECORD labels or only some of them.

I cannot tell whether there are labelled comment forms elsewhere in the repository that never reach `collect_claims`. The measurement explicitly says there are 22 unreached `# Cross-checked:` lines, all record legs, which usefully announces that its twelve-line count is a measurement of attached claim sites rather than a universal inventory of every labelled comment in the repository.

Finally, I cannot determine whether the twelve currently dropped lines exhaust the semantic risks of making `Note` travel. They establish the immediate migration set, and they expose the Moon contamination case, but the supplied material is not enough to prove that future authors will consistently distinguish ordinary context notes from prior-review notes. That is why I think the structural registry and a dedicated free-form RECORD label matter more than repairing the twelve current examples alone.