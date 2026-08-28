# Independent Mode 7 Review — Part A  
## Provenance, golden artifacts, and the braided build order

## 1. Verdict per goal

### G1 — Verified information served to the renderer and to the reader

**A published measured value needs one canonical definition, evidence from an identifiable source, and an automated guarantee that every served copy comes from that canonical value; multiple model approvals are not the minimum requirement.**

I would separate SOURCED, CONSISTENT, and CORRECT very sharply.

A value is **SOURCED** when the record identifies where it came from and preserves enough evidence to determine that the cited source actually contains the claimed information. A bare citation is insufficient. The evidence can be a quotation, a table row, a database field, or another precise extract plus a locator. The important point is that a later reviewer can inspect what the source actually said without trusting the checking model's recollection.

The pilot result matters here. Returns without direct evidence could confidently confirm a value that was semantically wrong, while the evidence-bearing return caught that an altitude above the photosphere had been mistaken for a distance from the Sun's centre. I would therefore make this a hard rule: **a model's conclusion is not verification evidence unless the return also carries inspectable source evidence.** A model return without that evidence can suggest a source or raise a question, but it cannot clear a publication gate.

A value is **CONSISTENT** when the project has one authoritative stored representation of it and every renderer, tooltip, explanatory string, and other published use either derives from that representation or is automatically checked against it. This is not a citation problem. It is a data-integrity problem. The cases where a correction reached one copy but not seven other sites are evidence that consistency must be mechanical rather than remembered.

A value is **CORRECT** only when the source evidence supports the exact quantity the program claims to use. That requires a semantic definition as well as a number: what quantity is being represented, its units, its reference origin or frame where relevant, and any epoch or condition that changes its meaning. The Alfvén-surface example is exactly the kind of failure a correct citation alone will not prevent.

That is the minimum publication package I would use for measured feature constants: canonical value; explicit semantic definition; source locator plus inspectable evidence; automated consistency across served uses; and an independent second check only when the quantity is high-consequence, semantically ambiguous, surprising, conflicting, or otherwise flagged.

This is also where the distinction between ephemerides and feature constants is decisive. Nightly Horizons positions effectively repair themselves through reconstruction, while copied feature constants can preserve an error indefinitely. They should not have identical verification requirements.

### G2 — Simplify citation and verification

**Keep the scanner and the evidence discipline, but stop treating hundreds of display-string claims as if each deserves a miniature multi-model research project.**

The present machinery is too broad rather than fundamentally misguided.

I would retain the scanner as an inventory and triage instrument. Vulnerability and criticality are useful concepts. I would retain the active-build-path boundary, because it turns an unbounded cleanup into work attached to something Tony is actually preparing to publish.

I would also retain the two legitimate outcomes for a questionable claim: establish its provenance or remove it and record the gap. That implements Tony's "silence is better" principle directly. The retired verification stamps demonstrate why merely adding something that looks like provenance is worse than leaving the claim visibly unresolved.

What I would stop doing is treating `V_CROSS_CHECKED` as a generally desirable destination for every factual statement. Two or three models repeating a claim is not intrinsically stronger evidence. The useful part of the competitive process is independent examination of evidence, not the number of model names attached to a value.

The default dispatch should therefore become **one evidence-bearing check**, with a second independent leg triggered by risk or disagreement. A third leg should be exceptional. The current competitive loop should survive as an escalation mechanism, not as the normal definition of verification.

I would also stop trying to clear all 553 display-string claims with equal ceremony. The file says 284 Tier-1 display strings contain 553 individual claims. I cannot tell from Part A which individual claims deserve which treatment, but I can give the decision rule.

A quantitative statement that controls geometry or is presented to the reader as a physical measurement should come from the canonical verified store whenever technically possible. A quantitative explanatory statement that does not control rendering should have traceable evidence if it remains on the published site. Low-value descriptive material should not consume a two- or three-model verification cycle merely because a scanner can identify it; if it cannot be cheaply sourced, shorten it or remove it.

The Sun example suggests the right direction. Out of 111 served numeric values, 85 are declared drawing parameters and only 26 sites represent 19 distinct measured values. The provenance system should care intensely about those 19 scientific quantities and very little about the 85 drawing choices.

The unit of verification should therefore migrate toward the **distinct canonical scientific quantity**, not every textual occurrence of its number.

### G3 — Simplify the golden artifact

**Repair the golden-artifact idea by making it much smaller and deterministic; the present fourteen-field live-scene snapshot is testing too many unstable things and is not currently proving what its name implies.**

The current harness has one fatal problem and two design problems. It compares today's output with itself rather than the stored artifact; several recorded fields are deliberately unstable; and the sole stored artifact has already become obsolete because legitimate assembler functionality changed.

I would replace the fourteen-field artifact with a small **assembly contract fixture**.

Give it fixed inputs: a fixed epoch, fixed cached input data, fixed configuration, and fixed feature selection. Do not run the correctness test against whatever the nightly build happens to contain.

Store only outputs that answer the two questions the mechanism exists to answer. For structural regression, keep the centre, expected object identities, feature keys, and enough trace-role information to prove that the expected assembly occurred. For numerical regression, keep a small number of deliberately chosen position samples or coordinates that would expose the kinds of slight displacement you care about.

Delete timestamps from the comparison. Delete exact comparison of naturally moving coordinate bounds. Do not store volatile fields merely because they are easy to serialize.

Then run the same frozen fixture through CPython and Pyodide and compare their normalized outputs numerically using a defined tolerance appropriate to the quantity. That establishes cross-runtime equivalence far more directly than two separately generated fourteen-field snapshots.

There is an important limitation: **agreement between Pyodide and CPython proves equivalence, not physical correctness.** If both runtimes execute the same wrong formula, they will agree perfectly. The stored expected position samples therefore need to originate from an independently accepted known-good case, not simply be regenerated by the code under test.

I would call these artifacts "golden fixtures" or "assembly fixtures" rather than scene records, because the frozen input is as important as the expected output.

Seven small fixtures are reasonable. Seven elaborate scene dossiers are unnecessary.

### G4 — Simplify Tony's judgment calls

**Tony should decide scientific meaning and publication policy; machines should decide syntax, duplication, routing, tolerances, and whether a previously approved scene has been invalidated.**

Tony should not be deciding whether a worksheet has the required fields, whether an evidence locator exists, whether duplicated constants disagree, whether a numerical comparison is inside a declared tolerance, whether a return uses an accepted grammar, or whether a previously passing fixture needs to be rerun after a shared dependency changed. Those are deterministic questions.

He also should not routinely decide which model to send a routine verification to. The process should say: first evidence-bearing check; escalate on disagreement, semantic ambiguity, high consequence, or weak evidence.

Nor should Tony repeatedly decide whether twenty textual copies of the same number are mutually consistent. The software should identify one canonical quantity and report any disagreeing copies as a defect.

The judgments that should remain with him are different. He should decide what the project claims a scientific quantity actually means. He should decide whether conflicting authoritative sources represent different definitions or a genuine conflict. He should decide whether a gap is acceptable for publication, whether a doubtful public statement is worth retaining, and whether an exceptional finding justifies overriding the normal gate.

There is one additional judgment I think he should be asked to make once, rather than hundreds of times: **define the project's source-and-semantics policy by class of quantity.** In other words, establish what counts as sufficient evidence, what conditions require independent verification, and what happens when no adequate source exists.

I would also require a compact semantic contract for each feature family before it is served. The key question is not just "what is the radius?" but "what do we mean here by radius?" That decision belongs with Tony because it determines what the visualization claims to represent.

All of these automated checks should be reachable through one ordinary Python entry point that Tony can open in VS Code and run. Nothing I am recommending requires him to operate a command-line workflow, CI system, or pre-commit infrastructure. His operating constraint is explicit in the request.

### G5 — Review the braided step-by-step order

**The braided order is sound if every new step also revalidates the previously published set; it is unsafe if each body is certified once and then treated as permanently finished.**

I agree with the decision to bind provenance at serving rather than drawing. Local experimentation should remain cheap, while publication deserves a stronger contract.

I also agree with attaching provenance work to the body or feature being brought online rather than making 292 tree-wide findings a prerequisite to any browser progress. That is a sensible termination strategy for one person.

The dangerous word is "step."

A step cannot become an immutable island after it passes.

Suppose step 4 is published and step 12 later changes a shared assembler function. Step 4's scientific provenance may still be perfectly valid, because none of its source constants changed. But its golden fixture must rerun, because its rendered result may have changed.

If step 12 instead changes a canonical constant used by step 4, both the provenance state and the golden result for step 4 are potentially stale.

If step 12 merely adds an isolated feature with no shared dependency, step 4 may require nothing beyond the normal regression run.

The publication model therefore needs **invalidation**, not repeated global recertification.

Each published scene should know which canonical scientific values and which shared assembly components it depends upon. A changed dependency marks the affected prior fixtures stale automatically. Before serving, all stale published fixtures rerun. Provenance needs to be revisited only when a scientific-data dependency or its semantic definition changed.

Even without a perfect dependency graph, seventeen planned fixtures are few enough that the simplest safe version is attractive: whenever a new rendering step is prepared for publication, rerun the golden fixture for every previously published step. The provenance slice can remain dependency-triggered. Seventeen small deterministic tests are cheap; seventeen repeated human provenance reviews are not.

The principal failure modes of the braided approach are therefore retroactive breakage of earlier scenes; shared constants escaping the supposed body boundary; a correction being made locally while duplicated prose remains stale; cumulative interactions that do not appear when a body is tested alone; and treating "previously passed" as equivalent to "still valid."

None of these requires abandoning the braid. They require treating publication status as revocable when its dependencies change.

## 2. Delete list

### Delete 1 — The retired `# Verified: April 2026 via Gemini fact-check` stamps

Delete them as verification indicators. They have demonstrated that they can create false confidence without preserving evidence. What is lost is only the historical assertion that a model once looked at the value. That history could remain in a changelog if desired, but it should confer zero trust.

### Delete 2 — `V_CROSS_CHECKED` as a universal higher destination

Stop treating two independent model annotations as the natural maturity state of every value. Preserve multi-model checking as an escalation path. What is lost is a simple global count of "cross-checked" rows. What is gained is a closer relationship between verification cost and actual risk.

### Delete 3 — Multi-model dispatch as the default

Make one evidence-bearing verification the normal case. Escalate to a second model when the first result is ambiguous, conflicting, surprising, high-consequence, or otherwise flagged. A third leg should be rare. What is lost is routine consensus. Given the pilot evidence, routine consensus is not strong enough evidence to justify its cost.

### Delete 4 — Per-copy scientific verification where the copy can derive from a canonical value

Verify the canonical scientific quantity and make published copies derive from it or be checked automatically against it. What is lost is a separate verification badge beside every repetition. That badge is less valuable than guaranteeing there is only one truth-bearing value to correct.

### Delete 5 — The fourteen-field live golden scene as presently defined

Keep the concept but delete volatile and irrelevant comparison fields, particularly timestamps and exact nightly coordinate bounds. Replace the mechanism with frozen-input fixtures and a small stable output contract. What is lost is breadth of snapshot coverage. What is gained is a test whose failures actually mean something.

### Delete 6 — Tree-wide clearance as a practical work objective

Continue measuring tree-wide debt if it is informative, but do not make Tony's working objective "clear 553 display claims." The active serving path is the correct boundary. What is lost is the aesthetic satisfaction of a globally clean audit. For a one-person project, that is not worth delaying useful work.

## 3. Keep list

### Keep 1 — The publication boundary

Do not simplify away the distinction between drawing locally and serving publicly. It is one of the strongest design decisions in Part A.

### Keep 2 — The honest-gap rule

"Cite it truthfully or remove it and record the gap" is excellent. Preserve it. A system designed to prevent fabricated certainty must explicitly permit uncertainty.

### Keep 3 — Evidence, not model confidence

A verification return should preserve inspectable evidence and a locator. The model's verdict is secondary.

### Keep 4 — Canonical values plus automated consistency

This is essential because Part A documents corrections that reached one copy while stale copies survived elsewhere. Provenance without consistency is not enough.

### Keep 5 — Active-path scoping

The work has to terminate. Verifying what is about to become public is defensible. Clearing the whole repository before continuing is not.

### Keep 6 — Independent checking where consequences justify it

Do not eliminate competitive verification entirely. It is valuable for ambiguous definitions, conflicting sources, unusually consequential constants, and cases where the first verifier's reasoning is doubtful.

### Keep 7 — Cross-runtime testing

The browser-versus-desktop equivalence claim is central enough that CPython/Pyodide comparison deserves a dedicated test. Simplify that test; do not remove it.

### Keep 8 — Regression coverage of everything already published

Every new browser step must prove that the previously published set still works. This is the mechanism that prevents step 12 from silently invalidating step 4.

## 4. Cost estimate

I would expect the policy simplification itself to cost about **one evening**: define the semantic/evidence requirements, the escalation rule, and what constitutes a publishable gap.

Changing verification so that evidence-bearing single-leg review is the default and multi-model checking becomes escalation looks like roughly **one to two evenings**, assuming the existing request builder and checker can be adapted rather than replaced.

Reducing the golden-artifact harness to deterministic fixed-input fixtures and making CPython/Pyodide compare the same normalized output looks like the largest addition, approximately **two to three evenings**. This estimate assumes the existing harness already knows how to invoke both paths. I do not know whether that assumption is true.

Adding automatic invalidation or, more simply, rerunning all previously published golden fixtures before each new publication step looks like **one evening** if implemented as a straightforward runner. A sophisticated dependency graph could cost considerably more and I would not build it unless the simple seventeen-fixture regression sweep becomes measurably burdensome.

Cleaning out or neutralizing the legacy verification stamps and making their values unresolved until properly evidenced looks like **less than one evening mechanically**. Re-verifying the underlying scientific values is a separate cost and should occur only as those features approach publication.

My proposed initial simplification therefore looks like approximately **five to eight evenings of infrastructure work**, followed by provenance work distributed across the rendering ladder rather than a 553-claim campaign.

I would reject any alternative that saves those five to eight evenings by replacing them with recurring manual judgment. Infrastructure is worthwhile here only when it permanently removes decisions from Tony's queue.

## 5. What I could not assess

I do not know whether `provenance_scanner.py` can already distinguish canonical measured quantities from drawing parameters and duplicated display uses. I would need to see `provenance_scanner.py` to judge how much of my proposed simplification is already latent in its model.

I do not know whether `constants_new.py` is centralized enough to support "verify once, derive everywhere," or whether scientific quantities are structurally duplicated in ways that would make that expensive. I would need `constants_new.py` and representative consuming modules to assess that.

I do not know whether the existing golden-artifact harness can feed exactly the same frozen input to CPython and Pyodide. I would need the assembler's golden-artifact harness to estimate the repair accurately.

I do not know whether the proposed seventeen-step ladder contains hidden cross-step dependencies that make the body-by-body boundary unsound. I would need `DRAFT_rendering_ladder_section.md` to review the actual sequencing rather than the summary of it.

I do not know whether the pilot's quotation and locator statistics hide important differences in source quality, task wording, or scoring. I would need `PILOT_CONVERGENCE_20260819.md` and representative returned worksheets before making stronger claims about Claude, GPT, or Gemini performance. The measurements given in Part A are enough to reject model consensus as evidence by itself, but not enough to rank the models generally.

I do not know whether the `provenance-discipline` skill already encodes an evidence standard close to the one I am recommending. I would need that skill before proposing changes to its grammar or workflow.

I do not need Part B to reach the judgments above.

## Overall judgment

The project does not need more verification machinery. It needs to concentrate the machinery it already has around three separate obligations: **evidence that the scientific quantity means what the project says it means, one authoritative value everywhere it is used, and deterministic regression proof that later work did not damage what is already public.**

The provenance system is strongest where it says "show the evidence or leave a gap." It is weakest where model agreement can masquerade as evidence.

The golden system is strongest in its intended purpose and weakest in its current choice of inputs and fields. Freeze the input, shrink the contract, and make previous fixtures rerun.

And the braided build order should proceed. I would approve it with one amendment before it enters the master plan:

**A rendering step may be certified locally, but publication certification belongs to the whole published set. Every later step must automatically revalidate earlier affected work before serving.**

With that amendment, the braid is not a compromise around provenance. It is a practical way to make provenance finishable.