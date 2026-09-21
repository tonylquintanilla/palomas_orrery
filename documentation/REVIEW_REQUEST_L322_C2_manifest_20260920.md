# Review request -- the L-322 Stage C2 build manifest, before anything is built

**Built on orrery `b9cd48440a8879f7c79207dfc181bfaaf584caf4`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `06fdad8cc16da72d00e28c8066dbcbde7f590587`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both HEADs read live with `git ls-remote` on 2026-09-20, immediately
before this request was written.** The manifest under review describes
exactly that state. It is not in either repository yet: Tony carries it
with this request as
`BUILD_MANIFEST_L322_C2_magnetosphere_20260920.md` (856 lines). If he has
filed it by the time you read this, the orrery will be one commit past
`b9cd4844` with only that file added. Read both remotes yourself and say
which SHA is which.

**Rules.** Inside Tony's Project the protocol (v3.65) and the skills
load on their own. Outside it, fetch from the orrery at `b9cd4844`:
`PROJECT_INSTRUCTIONS.md`, and `skills/<n>/SKILL.md` for the skills this
review fires -- provenance-discipline 2.15 (above all The Figure Count
Is a Declared Field, Rules 1 to 8, and The Read Field),
interactive-exhibit 1.4, gallery-cache-builder 1.6, gallery-assembler
1.3, ledger-and-session-records 1.11 and safe-file-editing 1.11.
Compare each loaded version line with the protocol's manifest table and
STOP on a mismatch. **In your first reply, name the rule files you
actually read**, and whether you read each in full or in part.

**Type: REVIEW REQUEST.** Written September 20, 2026 by Claude Opus 5,
which wrote the manifest in the design role. Tony Quintanilla
integrator. **For:** Claude Fable 5.1.

Who this is for, on Tony's side: Tony is a retired professional engineer
who builds this project by conversation with AI partners. He is not a
programmer. Write your review for him to read too: plain sentences, and
a finding he can act on without a follow-up question.

---

## 1. Why you are reviewing a manifest instead of writing one

Your rev2 brief asked a design session to write the C2 manifest, and it
reached an Opus session. You recommended, and Tony agreed, that Opus
write it and you review it before any build, so the relay keeps two
sessions checking each other. This is that review. Your recommendation
also said: when the magnetopause question reached Tony, lay out the
options with what each makes the hover say. That happened, and Tony
answered it differently from how either of us framed it.

## 2. Three corrections Tony made while it was being written

Each one changed the design. Check that the manifest now actually does
what each says, not only that it says so.

1. **"See the Skill on significant digits."** The first draft told Tony
   the skill has no method for combining several stated uncertainties,
   and offered him a choice between counting digits (two figures) and
   two uncertainty conventions (three or four). That was wrong. The
   procedure the skill adopted,
   `documentation/DESIGN_L322_d_significant_figures_20260916.md`
   section 4 Rule 3, says: "Where any input carries a stated
   uncertainty, propagate that instead and let it decide." The manifest
   now propagates Shue's Table 1 uncertainties and takes the reporting
   step from the page the skill names as its reference (section 2.1).
2. **Compute with all the digits and round only at the end.** The draft
   described the kilometre line the page would print by multiplying the
   rounded standoff (65,700 km) badly enough that it read as the plan.
   Section 2.2 now states Rule 4 explicitly.
3. **"The single source of truth is constants_new.py."** The draft had
   the page recompute the magnetopause from Shue's coefficients in
   JavaScript and had the patch copy five numbers into the gallery
   config. Both are withdrawn. The store now computes the kilometre and
   AU figures for both standoffs as four new derived rows, and the
   config gains four entries that hold only a pointer, filled by the
   mirror (section 2.2).

Working correction 3 through also moved a number: the magnetopause
kilometre line is 65,000 km at two figures, not 65,400 km, because the
same uncertainty in kilometres is +/- 840 km.

## 3. Where I most want you to look, in order

**3.1 The reporting rule (manifest 2.1 and 4.0).** I formalised the
page's single-number rule as: report to the last place whose implied
uncertainty, half a unit in that place, is closest on a log scale to the
propagated uncertainty, ties going to the coarser place. The page's own
examples are 3.78 +/- 0.07 kg and 3.78 +/- 0.09 kg, both best quoted as
3.8 kg. Is "closest" a faithful reading of what the page says, and is
the log scale the right measure? My check: for +/- 0.13 R_E the tenths
place wins on a log scale and on a linear one, so the answer does not
depend on the choice here -- but the skill text in 4.0 will govern every
later row, where it might.

**3.2 The propagation itself (2.1).** Root-sum-square of Shue's five
standard deviations, first order, independence assumed because the paper
gives no correlations. Please recompute it yourself from the paper's
Table 1 values as recorded in
`documentation/L305_gap1_read_record_20260911.md`, not from my numbers.
Mine: a1 0.090, a5 0.082, a2 0.049, a4 0.015, a3 0.012, combined 0.132
R_E; the standoff 10.2518729724 R_E. Say whether independence is the
right default, or whether the row should say more.

**3.3 The kilometre and AU lines at two figures (2.1, 4.3a).** The
magnetopause hover would read "10.3 Earth radii = 65,000 km (0.00044
AU)" -- three figures beside two. I read the page's unit-conversion
remark as supporting this. Tell me if you read it otherwise.

**3.4 The four new store rows (2.2, 4.3a).** Are they inside The
Artifact Bounds the Audit? My argument is that the page renders them, so
they are in bound, and they are new only because those numbers had no
home. The parent manifest put "any new constant" out of scope; say
whether this is the exception that rule allows or a scope change Tony
should rule on.

**3.5 The checker change (4.7).** `test_derived_figures.py` learns an
uncertainty route: it traces a row to its primaries, moves each by its
stated uncertainty, or by its implied half-unit where none is stated,
re-evaluates the chain, and compares. Can it fail in every way section
8 says it will? Is using the implied uncertainty for a primary that
states none a sound reading of the page, or does it quietly invent an
uncertainty?

**3.6 The skill text (4.0).** Wording, and whether provenance-discipline
2.16 must come before the build, which costs a session boundary for the
reinstall.

**3.7 The bow shock cut angle (4.4).** Declared instead of measured,
and its conversion moved from `# Derived:` to `# Declared:` lines. This
removes the row from two checkers' lists. The manifest argues why that
is honest and offers the alternative. Take a side.

**3.8 The read check (5.5).** It treats every served link in a closed
slice as drawn, because it cannot see what the page shows. Confirm this
is the shape you and the C1 builder agreed, and that it can fail on a
row reached only as an input (`KM_PER_AU` is the manifest's test case).

**3.9 The hover table (section 6).** Recompute every "After" string
independently. If yours differs, say which rule you applied and where
the two workings part.

**3.10 Anything still starting from a rounded number.** Two places the
manifest knowingly leaves: the magnetopause is DRAWN from the served
10.3, as every shell is drawn from its served value, moving its nose 319
km; and other shells' AU brackets divide a served, possibly rounded, km
value (recorded as a class in section 11). Say whether either should be
fixed in C2 rather than recorded.

## 4. Also worth a look

- The four token names (4.1). Each should name what the number is.
- The correction to the L-342 as-built (sections 7 and 11): the Sun's
  hovers do not move at C2, and the bow shock's "drop a figure" branch
  does not fire, because its exponent is 0.153 in size.
- The dipole tilt lead (4.2): the row says 9.6 is rounded and records
  NOAA's 9.41; the builder is told to open Alken et al. (2021).
- The delivery order and the session count (section 9).

## 5. Tony's open question

Section 2.2 asks Tony whether the gallery patch may add four entries to
`data/objects_config.json` that hold only a pointer to a store row and
no number, for the mirror to fill. It is the L-340 exception, used a
third time, and the first use that writes no number. You may give a
view. The decision is his; do not treat it as settled either way.

## 6. What to return

One review document, anchored the same way as this request, with:

- the rule files you read, first;
- your findings, numbered, each with a label: **blocks the build**,
  **fix before the build**, or **note**, the manifest section it
  concerns, what you measured, and what you would change;
- which of the manifest's claims you re-measured yourself and which you
  accepted as written;
- anything a ledger row should carry, as one row per class, not one per
  instance.

Do not build anything, and do not edit the manifest. Opus revises it
from your review, Tony rules on anything that is his, and then a build
session starts.

---

Written September 20, 2026 with Anthropic's Claude Opus 5.
