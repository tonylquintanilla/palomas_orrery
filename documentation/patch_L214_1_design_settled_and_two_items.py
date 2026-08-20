"""Ledger patch -- L-214 design settled after Mode 7 review; L-217 and
L-218 opened.

RUN COMMAND:  python patch_L214_1_design_settled_and_two_items.py

Save this file into the SAME FOLDER as LEDGER_CONSOLIDATED.md (the repo
root), open it in VS Code, and click Run. Nothing else is needed.

Built on 97c520177b18d69e6b5d3943557fdea47f56e8bf at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT IT DOES
  Edit 1 -- appends the settled design to L-214 and rewrites its Gap.
  Edit 2 -- inserts L-217 (Part A / Part B dispatch defect) and L-218
            (22 unreached Cross-checked lines) at the end of section A.

AFTER IT RUNS
  Run ledger_index.py the same way, to regenerate the index tables.
  This script does NOT touch the index zone.

WHAT IS PERMANENT
  The script is disposable; the three ledger blocks it writes are not.
  Archive this file to documentation/ once it has run.

SUCCESS   one 'ok' line per edit, then 'patch applied (N bytes)'.
FAILURE   a single 'ERROR:' or 'ANCHOR FAIL' line; nothing is written.
"""

import hashlib
import os
import sys

TARGET = 'LEDGER_CONSOLIDATED.md'
BASE_FP = '429d10f03111923bf7901ba50c6b50c7'   # content md5, CRLF-normalized

L214_OLD = b"""**Note:** RICE is Claude's proposal, unratified.
**Gap:** the design choice itself. Counting is done; nothing is built.
Re-dispatching the affected rows after the fix is a separate decision,
because a second dispatch of a row this project has already argued
about is not an independent leg.
**Ref:** `worksheet_keys.py` `LEG_RE` / `legs_of` / `continues_a_leg`;
L-209 (the row that exposed it); L-203 (the Visibility Convention);
L-204; L-207; L-210 (three of whose rows this count implicates).
"""

L214_NEW = b"""**Note:** RICE is Claude's proposal, unratified.
- **DESIGN SETTLED 2026-08-19, after a Mode 7 review by Claude Fable 5
  and GPT.** Both legs reviewed the same two documents and both
  disagreed with Claude's six-part proposal in the same place. Tony's
  rulings this session are recorded below; the reconciliation of the
  two returns is `documentation/L214_REVIEW_RECONCILIATION_20260819.md`
  and the measurement under it is
  `documentation/L214_MEASUREMENT_20260819.md`.
- **The root cause is one layer below where the proposal was working.**
  `LEG_RE` is BUILT FROM the policy sets, so "the label is not in our
  vocabulary" and "this is not a labelled line" are the same condition.
  That is why deliberate withholding and silent dropping share one code
  path and are indistinguishable from inside it. The fix is to detect
  any `# Label:` line generically FIRST, then classify it. The invariant
  both legs propose: every syntactically labelled line attached to a
  claim finishes the builder in ONE NAMED DISPOSITION. There is no
  disposition called "fell through the regex."
- **Transport and grammar are two axes, not one list** (GPT's framing;
  Fable reaches the same two-by-two and calls the empty cell a fourth
  state). TRANSPORT says travels or withheld. GRAMMAR says validated or
  free-form. `Source` travels and is verdicted. `Note` travels as
  context. `Resolved` is withheld with a strict linkage grammar. The
  cell nothing occupied is withheld-and-free-form, which is where the
  moon line has been trying to live.
- **Tony's ruling: the free-form record label is `# Review-note:`.**
- **Tony's ruling: unclassified text is WITHHELD from the request and
  surfaced to Tony and Claude before dispatch.** This corrects Claude's
  reading of the earlier report-not-refuse ruling, which had routed
  unclassified text to the outside responder. Tony, asked directly who
  "we" was in "report so we can deal with it by reading": "I meant you
  and me reading fuzzy responses." Fable's asymmetry argument is the
  reason it matters -- withhold-by-default fails visibly and
  recoverably, ship-by-default fails invisibly and unrecoverably,
  because a contaminated leg does not error, it CONVERGES, and
  convergence is this system's success signal.
- **Tony's ruling: the registry work stays in L-214** rather than
  splitting into its own item, even though the review grew this from a
  label-set fix into a change of how a labelled line is recognised.
- **One home for the vocabulary, and it does not exist yet.** Checked
  at `97c52017`: `CROSS_CHECK_LINE_RE` and `RESOLVED_LINE_RE` are
  compiled in `provenance_scanner.py`, case-INsensitive.
  `worksheet_keys.py` names neither, and its `LEG_RE` is
  case-SENSITIVE. `Removed` and `Corrected` have NO pattern anywhere --
  they are prose conventions that happen to fall through. So the record
  set is two enforced labels plus two conventions, not four peers, and
  Claude's proposed `RECORD_LEGS = (four labels)` was inventing two of
  them. Fable's sharp version of the risk: the hazard is not naming the
  set twice in prose, it is COMPILING it twice from two literals.
- **The marker sweep is 12 lines at 8 sites, not 10 at 6.** Fable
  predicted the undercount; re-run with the project's own tooling at
  `97c52017` confirms it exactly. Relabelling the odd spellings to
  `# Note:` brings their own continuation lines into the unmarked set
  -- one under `PARKER_CLOSEST_RADII`, one under
  `venus_atmosphere_info`. [verified @97c52017]
- **The build carries an ORDER CONSTRAINT, not just a list** (Fable).
  The moon line must leave `Note` BEFORE or in the same transaction as
  the marker sweep. Sequenced the other way there is a window in which
  it carries valid `Note+:` markers and travels cleanly on the next
  moon-row dispatch; the ratchet protects only until the sweep
  completes, and after that nothing refuses.
- **The moon line has no other home** [verified @97c52017]. Fable
  raised the cheaper instance-level answer -- if the ledger already
  carried "second independent leg owed" for that row, the comment would
  be a redundant mirror to delete. It does not. No ledger item carries
  it. The comment is the sole record, so it is rehomed under
  `# Review-note:` rather than deleted.
- **The project-side report lands on the console at dispatch**, beside
  the existing refusal print, rather than in a new file. That is the
  surface already in Tony's routine when he presses Run; a report in a
  store nobody opens is a check that cannot fail.
**Gap:** the BUILD. Design is settled and nothing is built. In order:
generic label detection separated from policy; one home for the
vocabulary with the scanner and the checker importing rather than
compiling their own; `Note` admitted to context; `# Review-note:`
added as withheld free-form; the moon line rehomed; the four odd
labels fixed at source; the 12-line marker sweep. Re-dispatching the
affected rows afterwards is still a separate decision, because a
second dispatch of a row this project has already argued about in
writing is not an independent leg.
**Ref:** `worksheet_keys.py` `LEG_RE` / `legs_of` / `continues_a_leg`;
`provenance_scanner.py` `CROSS_CHECK_LINE_RE` / `RESOLVED_LINE_RE`;
`documentation/L214_MEASUREMENT_20260819.md`;
`documentation/L214_REVIEW_RECONCILIATION_20260819.md`;
`documentation/REVIEW_PROMPT_L214_20260819.md`;
L-209 (the row that exposed it); L-203 (the Visibility Convention);
L-204; L-207; L-210 (three of whose rows this count implicates);
L-217 (the dispatch defect this review surfaced).
"""

SECTION_A_END_OLD = b"""**Ref:** `documentation/DESIGN_20260818_unknown_verdict.md`;
`documentation/PILOT_CONVERGENCE_20260819.md` Part 5; L-207.

## PENDING ACTION (Tony-side)
"""

SECTION_A_END_NEW = b"""**Ref:** `documentation/DESIGN_20260818_unknown_verdict.md`;
`documentation/PILOT_CONVERGENCE_20260819.md` Part 5; L-207.

#### [L-217] The Part A / Part B dispatch split is a check that cannot fail
<!-- L:217 status:OPEN upd:2026-08-19 section:A flag: rice:3/3/90/1 -->
- **Found by the reviewer it was meant to constrain, 2026-08-19.** The
  L-214 review prompt asked each model leg to answer Part A (derive
  your own structure) BEFORE reading Part B (critique ours), to stop
  the reviewer anchoring on Claude's proposal. Fable's disclosure: the
  prompt arrives as ONE document in ONE context, so there is no way for
  a model to write Part A without Part B already read, and NOTHING IN
  ANY ANSWER DISTINGUISHES A REVIEWER WHO COMPLIED FROM ONE WHO COULD
  NOT.
- **The corroboration is in the other leg.** GPT's A3 opens with "my
  prediction before consulting the measured result is" and then states
  the measured result to the digit. That is the tell. It is not GPT's
  fault -- the instruction asked for something the format made
  impossible.
- **This is an instance of the protocol's own CRITICAL gate**, A Check
  That Cannot Fail Is Not Passing, in the dispatch layer rather than in
  code. The prompt was authored in this session, so the gate did not
  fire on its own author.
- **Fable's remedy:** two physical dispatches. Part A sent alone,
  answer collected, THEN Part B sent. Anything less is the ritual
  without the check.
- **The related contamination finding, same review.** Fable ran INSIDE
  the Paloma's Orrery project and disclosed it unprompted: it carried
  resident memory of the protocol and the general state of the
  provenance work, though not the L-214 design conversation. The
  fresh-chat-outside-any-project rule exists for exactly this and was
  not followed for that leg. Its review was still the sharper of the
  two, which is worth noting and is not a reason to relax the rule.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** decide whether the two-dispatch protocol becomes standing
practice for any prompt carrying Claude's own proposal, and if so
record it in `provenance-discipline` or
`ledger-and-session-records` -- whichever fires at dispatch time.
**Tony-action (decide):** which skill hosts it, or whether a
one-document prompt simply stops claiming the split.
**Ref:** `documentation/REVIEW_PROMPT_L214_20260819.md` (the prompt
that carried the defect); `documentation/L214_REVIEW_RECONCILIATION_
20260819.md` Part 4; L-214; L-203 (the Visibility Convention, same
family of reasoning).

#### [L-218] 22 Cross-checked lines attach to no unit
<!-- L:218 status:OPEN upd:2026-08-19 section:A flag: rice:2/3/70/2 -->
- **Announced by the L-214 measurement, 2026-08-19, and parked there.**
  `worksheet_checker.collect_claims` returns an `unreached` list
  alongside its claims. At `97c52017` that list holds 22
  `# Cross-checked:` lines that match the scanner's pattern but attach
  to no scored unit. [verified @97c52017]
- **Why it was parked and why that is not good enough.** All 22 are
  record legs, so none of them could enter the L-214 defect count, and
  the measurement said so. Fable's reading: "It reads like a finding
  living in a footnote; it deserves its own handle and a look." That is
  correct -- an orphaned record annotation is either expected structure
  or a second latent defect, and nobody has established which.
- **What it would mean if it is a defect.** A `# Cross-checked:` line
  that attaches to no unit is a review verdict that landed in the code
  and is invisible to the tooling that reads verdicts. That is the same
  shape as L-214 one layer over: material written down correctly and
  read by nothing.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** list the 22, classify each as expected or defective, and
decide from the classification rather than in advance.
**Ref:** `worksheet_checker.py` `collect_claims`;
`documentation/L214_MEASUREMENT_20260819.md` (where the number is
announced); L-214.

## PENDING ACTION (Tony-side)
"""

EDITS = [
    ('L-214 design settled', L214_OLD, L214_NEW),
    ('L-217 + L-218 inserted', SECTION_A_END_OLD, SECTION_A_END_NEW),
]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, TARGET)
    if not os.path.exists(path):
        print('ERROR: %s not found next to this script.' % TARGET)
        print('       Save the script into the same folder as the ledger.')
        return 1

    with open(path, 'rb') as handle:
        data = handle.read()

    fp = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
    if BASE_FP != '__FILL__' and fp != BASE_FP:
        print('ERROR: BASE MOVED. expected %s, found %s' % (BASE_FP, fp))
        print('       Nothing written. Reconcile before re-running.')
        return 1
    print('base fingerprint %s' % fp)

    is_crlf = data.count(b'\r\n') > 0
    print('line endings: %s' % ('CRLF' if is_crlf else 'LF'))

    staged = data
    for name, old, new in EDITS:
        if is_crlf:
            old = old.replace(b'\n', b'\r\n')
            new = new.replace(b'\n', b'\r\n')
        count = staged.count(old)
        if count != 1:
            print('ANCHOR FAIL: %s -- expected 1 match, found %d'
                  % (name, count))
            print('             Nothing written.')
            return 1
        staged = staged.replace(old, new)
        print('ok  %s' % name)

    for handle_name in ('L-217', 'L-218'):
        marker = ('#### [%s]' % handle_name).encode('ascii')
        if staged.count(marker) != 1:
            print('ANCHOR FAIL: %s header count is %d, expected 1'
                  % (handle_name, staged.count(marker)))
            print('             Nothing written.')
            return 1

    with open(path, 'wb') as handle:
        handle.write(staged)
    print('patch applied (%d bytes)' % len(staged))
    print('')
    print('NEXT: run ledger_index.py the same way to rebuild the index.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
