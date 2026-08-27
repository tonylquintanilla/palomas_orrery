# Mode 7 review request -- PART B of 2 -- critique of a proposal

**Built on orrery `2d7f3258d1383cf752b206fa6875ee312e8f2f78` at
https://github.com/tonylquintanilla/palomas_orrery (branch main), gallery
`1a67b00d73813a1387ff1de7b77f8175c39c0f1e` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main). Both confirmed against the live remote on 2026-08-27.**

**Send this only after Part A's answer is on record.** It carries a
proposal that Part A deliberately withheld. If you are reading it before
answering Part A, stop and say so -- that is a finding, not a
formality.

Your Part A answer stands. Do not revise it. This is a separate
question.

---

## The proposal

Produced by the Claude session that wrote Part A, on 2026-08-27, and
confirmed by Tony the same evening. It is a change to how a verification
return is judged.

**1. The exhibit requirement.** Every returned worksheet row must carry
two new fields: a verbatim QUOTATION from the named source containing
the claim, and a LOCATOR (DOI, bibcode, section, table, page, or
resolvable URL). A row returning a verdict without both is recorded
UNVERIFIED regardless of what the verdict says. It is not weighed, not
averaged against another leg, and not read as weak agreement.

The reasoning: a leg that read the document can quote it; a leg that
recalled restates the citation it was given. That difference is a
property of the RETURN rather than of the claim, so testing it requires
no domain knowledge.

**2. Leg counts change accordingly.**

- Citation verification -- "does the named source contain this claim?"
  -- takes ONE leg, provided it carries an exhibit. The check then moves
  from the model to Tony: read the quotation, see whether the claim is in
  it. Thirty seconds, no astronomy.
- Value verification -- where a value must be FOUND rather than
  confirmed -- keeps TWO legs.
- A leg returning no exhibit does not reduce the count. It contributes
  nothing.

**3. The mechanical layer absorbs the largest class.** Most of what has
actually gone wrong in this project is the codebase disagreeing with
itself rather than disagreeing with the literature: a correction landing
in one of two copies, prose stating a number the drawn geometry does not
use, sibling constants measured from different origins, one value living
under five names. The proposal is that one-home, prose-interpolates,
geometry-derives and siblings-agree become mechanical checks in the
existing maintenance runner, with no model involved, leaving the
dispatch loop for genuine source questions only.

**4. Tier-1 = 0 means cited and internally consistent, not "verified."**
Cross-checked stays a rung that is earned deliberately, never a gate.

## What we are asking you

**B1.** Attack the exhibit requirement. The obvious objection is that a
model that fabricates a citation can fabricate a quotation. Is the
requirement therefore theatre? If not, say precisely what it buys and
what it does not.

**B2.** The evidence offered for it is a single dispatch of 138 rows,
reported in Part A. It shows quote-presence separating a leg that read
from a leg that recalled. It does NOT show quote-presence predicting
correctness row by row within one leg. Is the inference sound at the
strength claimed? What would test it properly, cheaply?

**B3.** Does dropping citation verification to one leg weaken the
defense against fabrication, given that the failure this project has
actually suffered is fabrication? Note that in the one dispatch on
record, two legs concurred on a wrong value and one dissented.

**B4.** Where does your Part A answer disagree with this proposal? Name
the disagreements plainly rather than reconciling them. A reviewer who
independently derived something close to this is useful evidence; so is
a reviewer who did not, and who thinks it is wrong.

**B5.** What does the proposal not address that your Part A answer said
mattered?

## Answer format

One plain sentence per item before elaboration. Cost in evenings for
anything you propose adding. Name explicitly anything you could not
assess without a file, and say "I do not know" rather than inferring.
