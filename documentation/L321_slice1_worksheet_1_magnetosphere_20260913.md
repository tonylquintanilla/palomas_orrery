# Citation worksheet 1 of 3 -- Earth's magnetopause and magnetotail

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

**What this is.** Paloma's Orrery draws Earth's magnetosphere and shows
text about it to visitors. We are checking every numeric and factual
claim in that text against sources we can actually open. This worksheet
covers the magnetopause and the magnetotail.

---

## The two jobs

Each row below says which job it is. They are different questions and a
good answer to one is a bad answer to the other.

**[CITATION]** -- the string names a source for this claim. Go to that
source and confirm it states the claim, at the stated precision. Then,
separately, check the value itself against an accessible primary source
of your own choosing.

**[DISCOVERY]** -- the string states something that may have no source
at all. Do not assume one exists. Do not reconcile it with any other
figure in this worksheet. Find whether an accessible source states it,
say which, and if none does, **say that**. UNSOURCED is a valid and
useful answer, and often the one we need.

**Access.** A source you cannot open without a login FAILS. Say so.
Record the URL you actually opened for every source, and one access
word: OPEN (full text), ABSTRACT, SNIPPET, WALLED.

---

## The text being checked, exactly as a visitor sees it

Rendered at the SHA above, with every interpolated number substituted.

### A. The hover on the magnetosphere surface

```
Earth: Magnetosphere

Earth's magnetosphere extends about 10.25 Earth radii on the Sun-facing side
and stretches into a long magnetotail on the night side. It protects Earth
from solar radiation and cosmic rays, making complex life possible.

Source (standoff): Shue et al. (1998), J. Geophys. Res. 103:17691.
```

### B. The magnetosphere paragraph of the information panel

```
Earth's magnetosphere extends about 10.25 Earth radii on the Sun-facing side
and stretches into a long magnetotail on the night side. It protects Earth
from solar radiation and cosmic rays, making complex life possible.
```

### C. The same claims in the checkbox tooltip

```
Earth's magnetosphere extends about 10.25 Earth radii on the Sun-facing side
and stretches into a long magnetotail on the night side. It protects Earth
from solar radiation and cosmic rays, making complex life possible.
...
Standoffs: Shue et al. (1998); Jelinek et al. (2012).
```

The 10.25 is not typed. It is computed in our data store from Shue's
equation 10 at declared solar wind conditions of Bz = 0 nT and dynamic
pressure = 2 nPa, and reported to four figures.

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
| 1 | CITATION | Earth's magnetosphere extends about 10.25 Earth radii on the Sun-facing side | 10.25 R_E | | | | | | |
| 2 | CITATION | It stretches into a long magnetotail on the night side | (no figure) | | | | | | |
| 3 | CITATION | It protects Earth from solar radiation | (no figure) | | | | | | |
| 4 | CITATION | It protects Earth from cosmic rays | (no figure) | | | | | | |
| 5 | CITATION | ...making complex life possible | (no figure) | | | | | | |
| 6 | CITATION | Shue et al. (1998), J. Geophys. Res. 103:17691, doi:10.1029/98JA01103 supports the magnetopause standoff | citation row | | | | | | |
| 7 | DISCOVERY | How far downstream has Earth's magnetotail actually been observed? | (none stated) | | | | | | |

---

## Notes on particular rows

**Row 5.** Verdict it as stated. Please do not soften "making complex
life possible" into something easier to defend -- if it overstates the
case, we want to know that.

**Row 6** is a citation row. It asks only whether Shue et al. supports
the standoff. Whether 10.25 is the right number is row 1's job.

**Row 7 is the point of this worksheet.** The text asserts a magnetotail
with no figure at all. We want to know what an accessible source says
about how far downstream the tail has been observed, and by what
measurement. Please give:

- the figure, with its uncertainty or range
- the reference frame (Earth radii from Earth's centre, unless the
  source says otherwise)
- whether the observation is of a **coherent tail** or only of a
  **signature** at that distance

We already hold one source and would like it verified rather than
replaced: Ness, Scearce and Cantarano (1967), *J. Geophys. Res.*
72:3769, doi:10.1029/JZ072i015p03769. Our reading is that it reports a
single Pioneer 7 crossing at roughly 900 to 1,050 Earth radii, that its
title says "probable", and that it reports no coherent tail with a
neutral sheet at that distance. Please confirm or correct that reading,
and say whether any later open source restates it or supersedes it.

If you name a later campaign -- ISEE-3, Geotail or anything else --
please open it. A remembered result is not a source.

---

Written September 2026 with Anthropic's Claude Opus 5, for Tony
Quintanilla's Paloma's Orrery.
