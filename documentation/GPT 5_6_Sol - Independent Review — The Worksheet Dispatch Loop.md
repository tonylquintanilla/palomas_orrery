# Independent Review — The Worksheet Dispatch Loop

## Verdict

**Do not dispatch the 65 rows yet.** The loop is not sound enough for first use, and the first thing I would fix is the handoff between the request builder and the checker: at the stated SHA, the builder writes a new `REQUEST_<batch>.md`, but the checker still selects the worksheet named in the existing `# Cross-checked:` annotation. A returned request therefore is not, by itself, the worksheet the checker evaluates; unless something else rewires the annotation, the new response sits outside the checking path and is reported as an uncited worksheet. I also found two additional blocking failures in the new schema: when both verdict columns exist the checker reads the value verdict and ignores the citation verdict, and display-string rows do not actually use their new Keys. Those are false-clean paths. The overall architecture remains worth keeping, but I would commission it with one deliberately adversarial end-to-end test before allowing a live worksheet to become evidence.

## 1. BLOCKING — The returned request is not actually wired back into the claim that generated it.

That breaks the loop before any question about scientific correctness arises.

**Verified.** `worksheet_request_builder.py` writes one file named `REQUEST_<batch>.md`. `worksheet_checker.py`, however, begins each claim by loading `worksheets.get(claim.worksheet)`, where `claim.worksheet` is the filename already written in the source annotation. It does not search for a returned request carrying the claim's Key. The checker then defines every worksheet not named by an annotation as uncited; `REQUEST_...` is not exempted as a prompt file.

So, for the example in the review packet, an annotation pointing to `worksheet_claude_constants_new.md` will still cause the checker to inspect that old worksheet after a new 65-row response is saved. The new response does not supersede or supplement it automatically.

**Recommendation.** Make the response handoff explicit before dispatch. I would not silently repoint the source annotations, because that would erase which worksheet the original `Cross-checked` claim referred to. Instead, give returned request files their own response identity and let the checker bind their rows to claims by Key in a distinct response-checking path. The existing annotation-to-old-worksheet audit can remain exactly what it is. A successful new response can then become evidence only after Tony decides what provenance annotation, if any, it earns.

This is the first change I would make because until this is settled the producer and consumer are processing different evidence objects.

## 2. BLOCKING — The nine-column schema asks two verdict questions, but the checker reads only one of them.

A responder can say that the value is correct and the citation is wrong, and the current checker will read the first answer while never judging the second.

**Verified.** The builder deliberately emits both `Value correct?` and `Citation correct?` columns. But `read_verdict()` tests for a value-verdict column first and returns immediately. It reaches the citation-verdict branch only when no value-verdict column exists.

That behavior made sense for older worksheets that had either a value verdict or a citation verdict. It is incompatible with the new table, which intentionally has both. The comment above the header registry even explains why value and citation scopes must not be conflated, but the new schema never gets both scopes processed.

This is a direct false clean. A row containing `Your value = 94`, `Value correct? = YES`, and `Citation correct? = NO` can be processed as a completed positive check without the `NO` becoming a citation finding.

**Recommendation.** Do not extend `read_verdict()`'s precedence rules. For tables carrying both columns, read and dispose of two verdicts independently. A value verdict and a citation verdict are two claims, and each needs its own completion state and result. Where a particular row legitimately has no citation question, applicability should be established before verdict processing rather than by silently ignoring a column.

I would add this exact adversarial row to the tests: value `YES`, citation `NO`. The test must fail unless the report contains the citation defect.

## 3. BLOCKING — The new Key regime is not actually used for display-string claims.

The builder gives those rows stable-looking `::cN` Keys, but the checker goes around them.

**Verified.** For ordinary constants, `check_claim()` passes `claim.key()` to `match_row()`, so Rule 0 can bind an exact Key and refuse fuzzy fallback. But as soon as the unit is a display string, `check_claim()` branches to `check_string_claim()` instead. That string path searches rows by the current numeric value plus words associated with the body and then takes `hits[0]`; it does not consult the Key column.

This means the system described in the packet as “builder mints keys; checker resolves them” is true for the constant path but not for the string-claim path. The review packet itself makes ordinal stability and the coexistence of keyed and fuzzy regimes central questions. At the anchored code, the answer is stronger than a hypothetical: the two regimes already coexist inside the new keyed worksheet.

**Recommendation.** Make the rule worksheet-wide. If a row table has a Key column, every claim in it must be matched by Key, including each `cN` display-string claim, and a Key failure must never fall through to value/prose matching. If a legacy worksheet has no Key column, keep the old matcher for backward compatibility.

Also remove `hits[0]` as an acceptable resolution for keyed data. If two candidate rows somehow carry the same claim identity, that is ambiguity to report, not a choice to make.

## 4. BLOCKING — The documented `KEY_SHIFTED` protection is designed but not connected to the live checker.

The code currently contains the safeguard as an idea and a helper, not as an enforced property of returned rows.

**Verified.** `worksheet_keys.py` correctly identifies the ordinal problem: inserting a number before `c2` can silently make `c2` mean something else. Its design says issue-time claim count and unit are recorded and checked before value comparison, producing `KEY_SHIFTED` when either changes. A `shift_check()` helper exists. The unit test calls that helper directly.

But the request builder does not emit issue-time claim count or unit metadata in its schema, and the display-string checker does not call `shift_check()` before matching the rows. Instead it recomputes today's numeric claims and searches for their values.

So the answer to the packet's ordinal-stability question is: **today, no, the ordinal is not protected in the way `worksheet_keys.py` says it is.** If the old number disappears, the likely symptom is an unmatched claim. More dangerously, if an equal number exists elsewhere in the string, the fuzzy string matcher can bind that other claim and no `KEY_SHIFTED` warning need occur.

**Recommendation.** Implement the safeguard already documented: retain issue-time count, unit and extractor version as machine-readable request metadata and enforce them before examining the evidence value. I would go one step further and store a small normalized fingerprint of the local claim text. Count plus unit knowingly leaves the compensating-swap case open; a fingerprint would make that residual substantially harder to trigger accidentally.

## 5. BLOCKING — Finding A is right, and Shape A is the better repair.

The current `# Source:`/`# Ref:` arrangement asks the responder to verdict something that is often a claim rather than an authority.

**Verified.** The repository has exactly the pattern described in Finding A. `TERMINATION_SHOCK_AU`, for example, has a `# Source:` line describing Voyager 1's crossing, while Stone et al. is in `# Ref:`; the two recorded cross-checks name Stone et al. as what was verified. The same pattern appears for the Alfvén surface and other constants. The builder explicitly declares `Source` to be the only verdicted leg and treats `Ref`, `Also`, `See`, `Derived` and `Calculation` as context.

So I agree with Finding A for the reason stated in the packet, not merely as a formatting preference.

**Recommendation.** Use Shape A. `# Source:` should answer “what authority supports this?” The event narrative belongs in `# See:` or `# Note:`, and a mathematical step belongs in `# Calculation:`. For `ROCHE_LIMIT_RADII`, for example, Murray & Dermott belongs in `Source`; the Roche-limit equation and substituted densities belong in `Calculation`.

I would not use Shape B. Combining authority and narrative with `--` makes the line pleasant for a human but weakens its machine meaning again. A third option would be to teach the builder to infer the real authority from any citation leg, but that reintroduces interpretation precisely where this system benefits from an explicit grammar.

## 6. BLOCKING — Finding B is right, but “append the next unlabeled comment” is not a complete fix.

The truncation is real; the proposed parser rule would replace one silent ambiguity with another.

**Verified.** `legs_of()` recognizes only lines that themselves begin with one of the configured citation labels. Any continuation line that lacks a repeated label is skipped. The repository contains the examples in the packet: Mercury's source continues onto the next line containing the 1.45 and 1.96 radii; Mars continues onto a second line containing the Vignes values; and the Pluto Hill-sphere source continues over several lines. `CHROMOSPHERE_PHYSICAL_KM` likewise puts the chapter and physical result on its second source line.

The supplied review says this affects 45 of the 65 dispatch rows. I did not independently recount all 65, so I accept that count from the review packet rather than claiming to have remeasured it.

**Recommendation.** Fix the annotation grammar, not just the regex. An unlabeled indented comment is inherently ambiguous because the same form is used for wrapped notes and free prose. I would introduce an explicit continuation syntax for citation legs and normalize the affected sites to it. The builder can then join only an explicitly marked continuation and fail loudly when a citation appears to continue in an ambiguous form.

If you prefer not to introduce another label, the minimum safe alternative is for the builder to stop and report an ambiguous continuation rather than guessing. A naive indentation join can swallow prose that was never part of the source; that is exactly the kind of apparently helpful inference this audit machinery is designed to avoid.

## 7. BLOCKING — A responder can still manufacture a green worksheet without performing an independent check.

The present request asks the reviewer to certify a number while showing them that number in advance.

**Verified.** The builder prints the Code value as read-only context and in the table, then asks the responder for “Your value” and a separate value verdict. The review packet itself identifies the attack: copying Code value into Your value and answering `confirmed` throughout can look perfect.

**Reasoned judgment.** No deterministic checker can prove that a language model genuinely opened a source. But the form should not make non-verification indistinguishable from verification by construction.

**Recommendation.** I would remove `Value correct?` from the responder's job. The responder's evidence should be “my independently obtained value” plus a specific retrievable source; the checker can determine whether that value agrees with the code. That eliminates one self-certifying field.

For stronger independence, do not show the Code value during the independent value lookup. Preserve it locally in the dispatch manifest so the checker still knows what was present at issue time. Citation checking is a different task because it necessarily exposes the claim and its cited source; if both functions must be done by the same model in one static Markdown file, true blinding is impossible. That is a reason to distinguish “independent value lookup” from “citation audit,” not to pretend the anchoring does not exist.

At minimum, a completed value check should require a nonblank, specific Source field. At the anchored checker I found the Source role registered as a column, but no production read that uses its contents as a completion requirement.

## 8. SHOULD FIX — `CHROMOSPHERE_RADII = 1.1` should not be treated as an unsourced physical measurement.

It is an explicit visualization decision and needs a different claim type, not a bad citation.

**Verified.** The source code is unusually clear here: 1.1 is the drawn shell radius, deliberately enlarged for visibility, while `CHROMOSPHERE_PHYSICAL_KM = 2000` separately records the physical quantity and its source.

**Recommendation.** Give provenance items a small type distinction before asking citation questions: factual measurement, derived value, and visualization/design choice are enough to solve this case. A visualization choice should carry its rationale and, where relevant, point to the physical value it intentionally departs from. It should not be asked “is the citation for 1.1 correct?” when nobody claims 1.1 is a measured chromosphere boundary.

I would **not** add `N/A` to the seven-token verdict vocabulary to accommodate this. Applicability belongs in the row type. Once the question is correctly typed, there is no verdict to make.

## 9. CONSIDER — The compound-answer concern is less broken than it appears.

The rendered schema separates the free-form numerical answer from the token verdicts.

**Verified.** The builder tells the responder to put a range and reduction rule in `Your value`, while separately requiring one token in each verdict cell. That is internally coherent. The line in the module's introductory documentation describing a value verdict “plus” the number is looser than the actual table, but the table itself does not require a token and qualification in one cell.

**Recommendation.** Keep the separation and tighten the introductory wording so it matches the actual columns. Let ranges remain evidence requiring human interpretation or a `RANGE` report; do not expand the verdict parser so it starts interpreting prose attached to tokens.

On this point, I would not redesign the schema.

## 10. CONSIDER — Keep the seven-token vocabulary narrow.

I do not see a missing verdict word that justifies reopening the registry.

**Reasoned judgment.** The apparent missing case, “not applicable,” is better solved by not asking an inapplicable question. The aesthetic chromosphere value is the clean example. Likewise, explanatory qualifications belong in Notes or the evidence field rather than in an enlarged set of verdict synonyms.

The narrow vocabulary is load-bearing because it keeps the checker from becoming a natural-language interpreter. I would preserve it unless a future case genuinely expresses a new evidentiary state rather than a different kind of row.

## 11. CONSIDER — Claude is not disqualified merely because Claude wrote the builder, but same-family scientific rechecking is weaker independence.

The relevant independence question is who produced the evidence being verified, not who wrote the plumbing that printed the table.

**Reasoned judgment.** I see no circularity in GPT reviewing the structure of Claude-authored Python when the Python itself is directly inspectable. I likewise would not say that a fresh Claude instance is logically incapable of filling a Claude-built form. But when an existing annotation says Claude performed the scientific cross-check, asking another Claude instance to establish that same scientific fact gives less protection against correlated model habits than sending that row to GPT or Gemini.

For the first evidentiary dispatch, I would preferentially cross families: Claude-origin checks to GPT or Gemini, GPT-origin checks to Claude or Gemini, and so on. The more important requirement is that the responder actually reaches the cited or independently selected authority. Different model names without independent evidence are not independent verification.

## 12. SHOULD FIX — Sixty-five is the right audit population, but it is too large for the commissioning run.

Use a deliberately difficult pilot before spending 65 external reviews.

The packet says these 65 rows audit places where somebody has already claimed a cross-check, while 206 Tier-1 findings remain elsewhere. I think validating the existing `Cross-checked` claims first is defensible. A false assertion that something has already been verified is more dangerous to this provenance system than an openly unsourced value, because the former suppresses suspicion.

But I would not make all 65 the first end-to-end exercise. First run a small commissioning batch chosen to force every structural branch: a normal keyed constant, a display string with several ordinals, a multiline Source, one of Finding A's Source/Ref inversions, a range, a deliberately wrong citation verdict, and the chromosphere visualization choice. Deliberately include at least one answer that should go to SEND BACK and one that should go to CONVERSATION. A first run in which everything is expected to pass does not test routing.

Once that batch behaves exactly as predicted, run the 65. Then turn external-review effort toward the unsourced Tier-1 population.

## 13. BLOCKING — There is no end-to-end test of the actual new contract, and the existing tests therefore miss the failures above.

The new schema is being tested in pieces rather than as a round trip.

**Verified.** `test_worksheet_checker.py` explicitly says the Key rule is inert against the live corpus and tests it with a synthetic table. That synthetic table does contain both verdict columns, but the tests shown there exercise row matching, not the full checking path that should process both verdicts. `test_worksheet_keys.py` directly exercises `shift_check()`, but that proves the helper works, not that the checker invokes it on a returned request.

**Recommendation.** Before dispatch, add one contract test that starts with the builder's emitted table and ends with checker findings. It should not construct a hand-written approximation of the schema. Have the builder render a tiny request, fill the response cells in the test, save it under the response convention decided in Finding 1, and run the checker.

That one test should prove at least four things simultaneously: the returned file is actually consumed; both verdict columns are independently acted upon; a display-string row binds by its exact Key; and an ordinal shift stops before value comparison. If that test had existed, the first three blockers in this review would have surfaced immediately.

## 14. SHOULD FIX — The review packet and the stated anchor are not perfectly synchronized.

Before changing code from this review, verify which revision Tony actually intends to dispatch.

**Verified.** I fetched the files directly at `a872205d17ee5298d1bdc86c614b43506e82b22c`, as requested. At that SHA, the raw request builder is reported as 288 lines rather than the packet's 312, and the checker as 1,510 rather than 1,650. More importantly than line counts, the anchored implementation does not fully exhibit two behaviors the packet describes as settled: keyed matching for display strings and enforced ordinal-shift detection.

This could simply mean the review document was prepared against a later working copy than the committed anchor. I cannot resolve that from the repository snapshot alone.

**Recommendation.** In GitHub Desktop, verify that the code intended for first dispatch is committed and that its commit identifier is the one named in the review. If there is a newer commit, rerun this review against that identifier rather than reconciling the two versions by hand. The SHA is useful precisely because it should make “which code did we review?” a question with one answer.

## Bottom line

Findings A and B are both real. **A is right and Shape A is the right repair. B is right, but the proposed unlabeled-continuation join is not safe enough; make continuation explicit or fail on ambiguity.**

I found four structural issues beyond them that I consider more important than either: the returned request is not yet in the checker's evidence path; the new two-verdict table only has one verdict read; display-string Keys are emitted but ignored; and the promised ordinal-shift protection is not wired into that path. Any one of the first three is enough for me to withhold dispatch.

After those are repaired, I would keep the basic architecture. The separation between a non-writing checker and a request-producing tool is sound. The narrow verdict vocabulary is sound. The distinction between SEND BACK for incomplete work and CONVERSATION for completed disagreement is sound. What is missing is not a new conceptual layer; it is proof that the layers already designed are connected end to end.

**Verification boundary.** I directly read the exact-SHA versions of `worksheet_request_builder.py`, `worksheet_checker.py`, `worksheet_keys.py`, `test_worksheet_checker.py`, `test_worksheet_keys.py`, `constants_new.py`, and representative Mercury, Mars and Pluto shell modules. Claims about those implementations above are based on those files. I treated the stated 65-row and 206-Tier-1 corpus counts, including the 45-of-65 truncation count, as supplied measurements from the review request rather than independently reproducing the entire corpus scan. The larger recommendations about blinding, model independence, commissioning order and provenance typing are my design judgments.