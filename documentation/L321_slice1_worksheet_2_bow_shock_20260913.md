# Citation worksheet 2 of 3 -- Earth's bow shock

This document is complete and self-contained. Send it as it stands.

**Built on** `f1bceefd05eeee0cac38fd519dd207314acb2383` at
https://github.com/tonylquintanilla/palomas_orrery

Before you start, read these two files at that SHA and say in your reply
which of them you actually read:

- `PROJECT_INSTRUCTIONS.md` -- the section "Fetched vs Recalled
  Convention"
- `skills/provenance-discipline/SKILL.md` -- the sections "The Access
  Standard" and "Worksheet Types"

A reply that does not name them is telling us it did not read them.

**Who this is for.** Tony Quintanilla is a retired civil and
environmental engineer, an artist and an anthropologist. He is not a
professional programmer and not a trained astronomer. The polish of the
code you are about to read is the product of AI collaboration and says
nothing about his fluency, so please unpack technical terms on first use
rather than assuming they land.

**What this is.** Paloma's Orrery draws Earth's bow shock and shows text
about it to visitors. We are checking every numeric and factual claim in
that text against sources we can actually open.

---

## The two jobs

Each row below says which job it is.

**[CITATION]** -- the string names a source for this claim. Go to that
source and confirm it states the claim, at the stated precision. Then,
separately, check the value itself against an accessible primary source
of your own choosing.

**[DISCOVERY]** -- the string states something that may have no source
at all. Find whether an accessible source states it, say which, and if
none does, **say that**. UNSOURCED is a valid answer.

**Access.** A source you cannot open without a login FAILS. Say so.
Record the URL you actually opened for every source, and one access
word: OPEN (full text), ABSTRACT, SNIPPET, WALLED.

---

## The text being checked, exactly as a visitor sees it

Rendered at the SHA above, with every interpolated number substituted.

### A. The hover on the bow shock surface

```
Earth: Bow Shock

Bow Shock: The boundary where the supersonic solar wind is first slowed
by Earth's magnetic field, typically located about 13.51 Earth radii upstream
from Earth on the Sun-facing side.
The Bow Shock points towards the Sun along the X-axis. The XY plane is the ecliptic.

Source (standoff): Jelinek et al. (2012), J. Geophys. Res. 117:A05208, doi:10.1029/2011JA017252.
```

### B. The bow shock paragraph of the information panel

```
Bow Shock: The boundary where the supersonic solar wind is first slowed
by Earth's magnetic field, typically located about 13.51 Earth radii upstream
from Earth on the Sun-facing side.
```

The 13.51 is not typed. It is computed in our data store as
R = 15.02 x p^(-1/6.55) with p = 2 nPa, the declared solar wind dynamic
pressure, and reported to four figures.

---

## The worksheet

Fill this in and return it as ONE table. Do not add or remove rows.

Verdict cells carry **exactly one token**.
`Value correct?` -- YES, NO, APPROX, UNVERIFIED.
`Citation correct?` -- YES, NO, PARTIAL, DERIVED, UNSOURCED, UNVERIFIED.
All reasoning goes in Notes, nowhere else.

Where a source states a figure in a different unit or reference frame
than we do, put the source's own unit in `Source unit` and the
conversion in Notes.

| # | Job | Claim | Code value | Your value | Source unit | Source (URL opened, access word) | Value correct? | Citation correct? | Notes |
|---|-----|-------|-----------|-----------|-------------|----------------------------------|----------------|-------------------|-------|
| 1 | CITATION | The bow shock is the boundary where the supersonic solar wind is first slowed by Earth's magnetic field | (no figure) | | | | | | |
| 2 | CITATION | It is typically located about 13.51 Earth radii upstream on the Sun-facing side | 13.51 R_E | | | | | | |
| 3 | CITATION | Jelinek, Nemecek and Safrankova (2012), J. Geophys. Res. 117:A05208, doi:10.1029/2011JA017252 supports the bow shock standoff | citation row | | | | | | |
| 4 | CITATION | Lugaz et al. (2016), Nat. Commun. 7:13001, doi:10.1038/ncomms13001 states that under normal solar wind the bow shock forms at a subsolar distance of 11 to 14 Earth radii | corroboration row | | | | | | |

---

## Notes on particular rows

**Row 2.** Two separate questions live here and we want both answered.
Does Jelinek's relation, evaluated at 2 nPa, actually give 13.51? And is
13.51 a defensible figure for a quiet-time subsolar bow shock at all,
against whatever source you would reach for independently?

Please also say whether four significant figures is more than the source
supports. Our own reading is that Jelinek states no uncertainty on the
fitted constants, so what bounds the value is the scatter of the
crossings themselves -- about 0.69 Earth radii in the paper's figure 7.
If you think 13.51 implies a precision the data does not carry, say so
plainly. We would rather print 13.5, or 14, than overstate.

**Row 3** is a citation row. It asks only whether Jelinek supports a
subsolar standoff of this form. Whether our arithmetic is right is
row 2's job.

**Row 4 is not the source of the drawn value and is not claimed to be.**
This range no longer appears in any text shown to visitors. It is kept
in our data store as a corroborating range, and we want to know two
things: does Lugaz state 11 to 14 Earth radii, and in what reference
frame. Our drawn value of 13.51 sits inside that range, and we would
like to know whether that agreement is meaningful or coincidental --
whether the two are even measuring the same thing under the same
conditions.

---

## One thing we removed, in case you find it

Until recently this text said the bow shock value was "drawn at the
midpoint" of Lugaz's 11 to 14 range, and elsewhere cited Farris &
Russell (1994), *J. Geophys. Res.* 99:17681, for the model **form**.
Both are gone. The midpoint claim was false once the value came from
Jelinek, and our reading of Farris & Russell is that it gives the
standoff distance for a given Mach number and takes the obstacle's shape
as an **input** rather than predicting it -- so citing it for a shape
was a miscitation.

If you think that reading of Farris & Russell is wrong, please say so in
the Notes of row 1. We would rather be corrected than leave a paper out
that belonged in.

---

Written September 2026 with Anthropic's Claude Opus 5, for Tony
Quintanilla's Paloma's Orrery.
