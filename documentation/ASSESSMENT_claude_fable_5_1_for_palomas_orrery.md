# Assessment: Claude Fable 5.1 as a partner on Paloma's Orrery

**Tony Quintanilla, PE | Claude Fable 5.1 | September 2, 2026**

Built on orrery `7314fa5558c78b08452cb2709bf1795d3ab57fb2` at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery `f68c74211caf16b941e89697d964ace54670eaf9` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main). Both HEADs matched by `git ls-remote` at session start. Both
repos were shallow-cloned and read; nothing below is from memory of the
project.

What was read this session: both READMEs, PROJECT_INSTRUCTIONS.md
v3.49-v3.51 (as loaded in the project), LEDGER_CONSOLIDATED.md (the
INDEX and the detail blocks for L-272 through L-277), MODULE_ATLAS.md
header, all ten SKILL.md files in the repo and the ten installed copies,
the Fable-authored documents in `documentation/` and every ledger line
that names Fable, and the gallery's assembler layout. Validators run:
`ledger_index.py --check` (272 blocks, clean), `skills_index.py` (10
skills parsed, clean), `py_compile` on constants_new.py,
provenance_scanner.py and ledger_index.py.

---

## 1. The short version

I am the same family of model this project has been using for
adversarial review, surveys and audits since July (the ledger's "Fable
5" entries), now at version 5.1. My strongest use here is the work
those entries already describe: reading both repositories whole,
measuring against the bytes, and finding where stores disagree. My
weakest use is anything that needs Tony's eyes, Tony's Windows machine,
or a scientific number I would otherwise recall.

Nothing about the project after late June 2026 is in my training. That
is the right way round for this protocol, because everything I know
about the current state came from the repo at HEAD and the documents
you loaded, which is where the protocol says it should come from.

---

## 2. Strengths, with the evidence

**Reading both repos in one pass and measuring rather than recalling.**
This session I cloned both repositories, read a 13,000-line ledger, ten
skills in two stores, and the atlas, and ran the project's own
validators, without running short of room. The project's failures are
mostly cross-store drift -- a skill in three stores, a pipeline count
in one file and its names in another, five position consumers across
two repos -- and cross-store comparison is the shape of work I do best.
The August 11 document-layer audit (F1: the push gate two stores
described was not the one you ratified; F2: a three-version hole in
the declared change log) is the kind of finding that comes from
reading everything at once.

**Running the checks instead of describing them.** The sandbox runs
Python 3, so `ledger_index.py`, `skills_index.py`,
`provenance_scanner.py` on a throwaway copy, the offline builder tests,
and a delivered patch script on a throwaway clone all run here before
you see them. A Check That Cannot Fail and A Report Names Its Items are
rules I can satisfy mechanically, because I can count and name against
real files and print what was examined.

**Patch scripts with the guards proven.** Fingerprinted,
all-or-nothing, anchor-verified, tested on a clone with each guard
forced to fire. The safe-file-editing 1.10 loop fits in one turn.

**Arguing a design before it lands.** The ledger records Fable rulings
that were accepted with amendments (the worksheet schema, the L-192
checker, the constant-unification review) and one that you rejected
after a counter-argument. Reviewing a proposed rule or manifest for
what it does not say is a good use of me, and it costs you a document
rather than a session.

**Sweeps with a stated pattern and a list as output.** L-244 is tagged
as a Fable candidate for exactly this reason: enumerate every literal
that duplicates a named constant, return the list, fix nothing. That is
discovery separated from remediation, which The Braid requires, and it
dispatches well to me because the answer has a denominator.

---

## 3. Weaknesses, with the evidence

**I sound the same when I am right and when I am wrong.** The protocol
already knows this; it is why the render wins and why Gemini is asked
de novo. Two cases in this project's own record are worth carrying:

- *A proxy presented as a measurement.* The L-191 reproduction returned
  53 on its first attempt because it skipped four strings it could not
  evaluate, silently. That was Opus, but the failure class is mine too.
  When I give you a count, the useful question is "what did it skip and
  how many did it examine," and a good answer prints both.
- *A general sentence trusted over a specific fact already read.* L-276:
  a session read the relay response in which Fable cloned the repo, and
  then repeated the protocol's "zero independent repo access" line
  anyway. I weight a resident document's general claim over specific
  evidence in hand. The defence is yours: when a document and a fact I
  just reported disagree, say so and I will re-read the fact.

**Scientific values from memory are the failure the provenance program
exists for.** I will produce a plausible ring radius or shell boundary
with a confident source attached. Fetched-versus-recalled stays the
rule. Do not ask me to fill a Tier-1 gap from recall; ask me to find and
read the source, or to remove the value and note the gap.

**Recommendations that are argued and wrong.** L-273: I offered a
generator and a checker, recommended the checker, and your indexer was
better than both. The ledger records it as a Claude error rather than
smoothing it over, which is the right treatment. Expect this to
recur when I converge too early; "open ended thinking" is the phrase
that stops it.

**Density.** The Register Rule exists because of me. Long tool-heavy
sessions and mobile sessions push me back toward four jobs per message.
"Just the decision" is a repair you should use freely.

**What the sandbox cannot reach.**
- It is Linux. L-274's OneDrive mtime refresh could not be reproduced
  here and was simulated. Anything Windows-, Tk- or OneDrive-specific
  gets a simulation, not a reproduction, and I should say which.
- Its network reaches GitHub, PyPI and npm only. palomasorrery.com is
  not on the list, so `gallery_maintenance_run.py --live` and the Node
  smoke suites against the deployed site are UNREACHABLE from here. I
  can fetch the site's HTML through the browser tool for a read, but I
  cannot run your live checks against it.
- Mode 5 stays yours. I can read a screenshot you upload and compare it
  against the code; I cannot judge the render's beauty and I cannot see
  the phone.

**Session-boundary limits the protocol already models.** I cannot
verify a mid-session skill reinstall, and I cannot see uploads that did
not land in context unless I `ls` the directory. Both are architectural
and both have rules; I am naming them so you do not expect otherwise.

**Memory is stale by design.** The memory summary loaded this session
said the protocol was at v3.48 and L-271 had closed; the repo says
v3.51 and L-271 OPEN. Memory sits at trust level 6 for a reason. The
SHA pair you sent is what made this session correct.

---

## 3a. On inventing plausible facts, and whether the architecture catches it

Added at Tony's request after he raised it directly: reviews and the
model's system card are reported to say Fable may invent plausible facts
and explanations more readily than Opus 5.

**What I can and cannot say about the premise.** I cannot confirm what
the system card says from memory; the model postdates most of what I
know about myself, and I have no privileged view of my own error rates.
That is the honest limit, and it is also the point: a model's
self-assessment of its confabulation rate is exactly the kind of fluent,
plausible claim that should not be taken from the model. If the reviews
say the rate is higher, treat that as the working assumption rather than
asking me to argue with it.

**It is not a new failure class.** Fetched-versus-recalled, "a citation
is a claim about provenance," and "the render wins" all exist because a
model produces a confident specific whether or not it has grounds. A
model that does this more often raises the rate of the failure the
protocol was built around; it does not add a different one. So the
question is whether the catches run often enough, not whether they
exist.

**Where the architecture is strong: values and bytes.** A recalled ring
radius meets the scanner, the Tier-1 gate on the build path, the
worksheet loop to a blind second model, and eventually the render. A
wrong patch meets the fingerprint. A wrong claim about what was pushed
meets the SHA. A count now has to print what it examined. For numbers
and code the rigor is there, and it was built by watching this exact
failure.

**Where it is weak: explanations.** The architecture checks what a value
is far better than it checks why something happened. A causal story
about a mechanism, a summary of what a past session decided, a reason a
design is correct, an account of the project's own history -- these land
in ledger detail blocks and handoffs as prose, and the ledger is the
institutional memory that future sessions read as fact. The record
already has the shape: L-276 is a session repeating a plausible general
sentence over specific evidence in hand; L-273 is a recommendation
argued fluently and wrong. Neither was a number, so no gate fired. Both
were caught by Tony reading closely, which does not scale and is the
scarcest resource in the project.

The ledger's evidence tags (`[verified @SHA]`, `[per chain]`,
`[render-confirmed Mode 5]`) cover code claims. Nothing equivalent marks
whether a MECHANISM claim in a block was confirmed by test, read in the
source, or inferred. L-274 happens to say "confirmed by test rather than
assumed" in its prose; most blocks do not say either way.

**Conclusion.** Enough rigor for what I would want to be trusted with,
if the division of labor stays as it is: this model where the output is
a checkable list or a document read adversarially; the implementation
partner where the loop is tight and the render is near. The one
addition proposed, and it is a protocol question for Tony rather than a
skill method: when a ledger block or handoff asserts WHY something
happened, it says whether that was tested, read in the source, or
inferred -- the same evidence axis the value claims already carry.
Proposed, not ruled.

---

## 4. Best use cases, ranked

1. **Session-start audit and cross-store sweep.** Both SHAs, skills
   against manifest, README document table against the root set, the
   five consumers, the two repos. One turn; findings in a file.
2. **Class-level discovery sweeps with a stated pattern** (L-244, the
   L-254 remaining nine modules, the L-192 site store). List out,
   nothing fixed, denominator stated.
3. **Adversarial review of a rule, manifest or design note before it
   lands.** Send the document with its anchor; get back what it does
   not cover and the counter-argument.
4. **Devtools with tests, where the sandbox proves them:** `doc_index.py`
   (L-273), reanchoring the L-192 store to names (L-277 option b), the
   dashboard's Node dispatch (L-275). These are the kind of build where
   "it ran here" is real evidence.
5. **Patch-script delivery for existing files,** tested on a throwaway
   clone with guards verified.
6. **Ledger and handoff drafting to file,** not into chat.

Not a good use: filling scientific values, judging aesthetics,
reproducing OS-specific failures, live-site verification, or any task
whose scope is "everything" with no artifact bound.

---

## 5. Conditions for prompting me

- **Send both SHAs**, as you did today. It is the one input that makes
  everything else checkable.
- **Say which mode and what shape the output is:** a decision, a list, a
  patch, a review. "Thoughts?" and "open ended thinking" get
  alternatives; "just the decision" gets one sentence.
- **Withhold the expected count on a survey.** You already do this and it
  is why the 20 became 58. Keep doing it.
- **Name the artifact bound.** "Sweep the Sun exhibit's build path" has a
  denominator; "sweep the codebase" does not.
- **Say whether a sweep is discovery or remediation.** If I am to fix
  nothing, say so; otherwise each fix opens the next search.
- **When I report a count, ask what it skipped.** If I cannot answer, the
  count is a proxy.
- **Un-pushed work arrives as an upload, and say it is un-pushed.** The
  repo shows only committed bytes.
- **Name the skill if the task is borderline.** The Stale Skill = Stop
  gate fires on load, so naming the skill in the prompt makes the load
  happen.
- **Say when you are on the phone.** Mobile sessions need shorter
  messages and fewer open items per message; I will not infer it.
- **One task per prompt lands better than four**, for the same reason
  the Register Rule asks one thing per message of me.
- **Do not ask me to confirm a reinstall mid-session.** Write it into
  the handoff and the next session checks it.

---

## 6. Observations from this session's read (not findings; not chased)

- Both installed skills that the v3.50 and v3.51 handoffs carried as
  obligations (orrery-coding-conventions 1.7, safe-file-editing 1.10)
  read the expected version from the account install. Both obligations
  are discharged as of this session.
- PROJECT_INSTRUCTIONS.md as loaded carries a header of `v3.49 | August
  30, 2026 | Cut from ded99fbe` while its version history runs to v3.51
  (August 31). The header and the newest entry disagree. Not checked
  against the repo copy; it may be the project-knowledge copy that is
  behind.
- MODULE_ATLAS.md reports three modules with no valid `Role:` tag:
  `test_extractor_pins.py`, `test_worksheet_keys.py`,
  `worksheet_key_aliases.py`. L-163 closed at zero undetermined; these
  are newer files. Named here so the count does not read as a
  regression.
- The README's generated document table shows five rows as untagged.
  That is L-273's known remaining scope (the generators must emit the
  tag), not a new gap.
