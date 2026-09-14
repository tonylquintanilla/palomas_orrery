# Citation worksheet 3 of 3 -- Earth's Van Allen belts

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

**What this is.** Paloma's Orrery draws Earth's two radiation belts and
shows text about them to visitors. Four of the figures below describe
how far the belts extend, and we do not currently know whether any
source states them. That is the main question this worksheet asks.

---

## The two jobs

Each row below says which job it is, and this worksheet genuinely needs
both. Please do not treat a DISCOVERY row as though it were a citation
row with a missing citation.

**[CITATION]** -- the string names a source for this claim. Go to that
source and confirm it states the claim, at the stated precision. Then,
separately, check the value against an accessible primary source of your
own choosing.

**[DISCOVERY]** -- the string states a figure that may have no source at
all. **Do not assume one exists.** Do not reconcile it with any other
figure in this worksheet. Find whether an accessible source states an
edge for that belt, say which source, and if none does, **say that**.
UNSOURCED is a valid and useful answer, and for these four rows it may
well be the right one.

**Access.** A source you cannot open without a login FAILS. Say so.
Record the URL you actually opened for every source, and one access
word: OPEN (full text), ABSTRACT, SNIPPET, WALLED.

---

## The text being checked, exactly as a visitor sees it

Rendered at the SHA above, with every interpolated number substituted.

### A. The hover on the inner belt

```
Inner Van Allen Belt: Region of trapped charged particles (mainly protons).
Drawn at the flux peak, 1.5 Earth radii from Earth's centre; the belt
spans roughly 1.1 to 2 Earth radii.
Source (peak): Baker et al. (2018), Space Sci. Rev. 214:17, doi:10.1007/s11214-017-0452-7.
```

### B. The hover on the outer belt

```
Outer Van Allen Belt: Region of trapped charged particles (mainly electrons).
Drawn at the flux peak, 4.5 Earth radii from Earth's centre; the belt
spans roughly 3 to 7 Earth radii and moves with geomagnetic activity.
Source (peak): J. Geophys. Res. Space Physics (2025), doi:10.1029/2024JA033504; Baker et al. (2018).
```

### C. The belt paragraphs of the information panel

```
Inner Van Allen Belt: Region of trapped charged particles (mainly protons)
extending from about 1,000 km to 6,000 km above Earth's surface.
Outer Van Allen Belt: Region of trapped charged particles (mainly electrons)
extending from about 13,000 km to 60,000 km above Earth's surface.
```

### D. The same claims in the checkbox tooltip

```
Inner Van Allen Belt: trapped protons, drawn at the flux peak 1.5 Earth radii out
(Baker et al. 2018). Outer Van Allen Belt: trapped electrons, drawn at the flux peak
4.5 Earth radii out (doi:10.1029/2024JA033504).
```

The tooltip carries the two flux peaks and no extent, so no row below
comes from it. It is included so you can see every place these claims
appear.

---

## The worksheet

Fill this in and return it as ONE table. Do not add or remove rows.

Verdict cells carry **exactly one token**.
`Value correct?` -- YES, NO, APPROX, UNVERIFIED.
`Citation correct?` -- YES, NO, PARTIAL, DERIVED, UNSOURCED, UNVERIFIED.
All reasoning goes in Notes, nowhere else.

Where a source states a figure in a different unit or reference frame
than we do, put the source's own unit in `Source unit` and the
conversion in Notes. Please read the frame note below before filling
that column in.

| # | Job | Claim | Code value | Your value | Source unit | Source (URL opened, access word) | Value correct? | Citation correct? | Notes |
|---|-----|-------|-----------|-----------|-------------|----------------------------------|----------------|-------------------|-------|
| 1 | CITATION | The inner belt holds mainly protons | (no figure) | | | | | | |
| 2 | CITATION | The inner belt is drawn at its flux peak, 1.5 Earth radii from Earth's centre | 1.5 R_E | | | | | | |
| 3 | DISCOVERY | Does a source state an inner edge and an outer edge for the INNER belt? The text says "spans roughly 1.1 to 2 Earth radii" | 1.1 to 2 R_E | | | | | | |
| 4 | DISCOVERY | Does a source state the INNER belt's extent in altitude? The text says "about 1,000 km to 6,000 km above Earth's surface" | 1,000-6,000 km | | | | | | |
| 5 | CITATION | Baker et al. (2018), Space Sci. Rev. 214:17, doi:10.1007/s11214-017-0452-7 supports row 2 -- the PEAK | citation row | | | | | | |
| 6 | CITATION | The outer belt holds mainly electrons | (no figure) | | | | | | |
| 7 | CITATION | The outer belt is drawn at its flux peak, 4.5 Earth radii from Earth's centre | 4.5 R_E | | | | | | |
| 8 | DISCOVERY | Does a source state an inner edge and an outer edge for the OUTER belt? The text says "spans roughly 3 to 7 Earth radii" | 3 to 7 R_E | | | | | | |
| 9 | DISCOVERY | Does a source state the OUTER belt's extent in altitude? The text says "about 13,000 km to 60,000 km above Earth's surface" | 13,000-60,000 km | | | | | | |
| 10 | CITATION | The outer belt moves with geomagnetic activity | (no figure) | | | | | | |
| 11 | CITATION | The outer belt string names BOTH J. Geophys. Res. Space Physics (2025), doi:10.1029/2024JA033504 AND Baker et al. (2018) for row 7 -- the PEAK. Does each support it? | citation row | | | | | | |

---

## Three reference frames, and two of them look alike

Please read this before filling in the `Source unit` column.

**L**, the McIlwain L-shell. The distance, in Earth radii, at which a
magnetic field line crosses the magnetic equator. It is dimensionless.
Most radiation-belt literature states belt extents in L. For a dipole
field, L equals geocentric distance **at the magnetic equator and
nowhere else** -- a belt at L = 4 reaches much lower altitudes at high
latitude.

**Geocentric distance in Earth radii**, measured from Earth's centre.
This is what our hover text says.

**Altitude in kilometres**, measured from Earth's surface. This is what
our information panel says. It differs from geocentric distance by one
Earth radius.

If your source states L, put **L** in the `Source unit` column. Please
do **not** treat it as interchangeable with our "Earth radii from
centre". Saying they are the same is a claim about the field geometry,
and it is only true at the equator.

Rows 2 and 7 may deserve PARTIAL on `Citation correct?` for the frame
alone -- our text says Earth radii from centre where the sources may say
L. That is a correct verdict, not a complaint about the worksheet.

---

## The conversion, so nobody has to compute it

At Earth's equatorial radius of 6,378.1 km:

| Row | As written | Converted |
|-----|-----------|-----------|
| 3 | 1.1 to 2 radii from centre | 638 to 6,378 km altitude |
| 4 | 1,000 to 6,000 km altitude | 1.16 to 1.94 radii from centre |
| 8 | 3 to 7 radii from centre | 12,756 to 38,269 km altitude |
| 9 | 13,000 to 60,000 km altitude | 3.04 to 10.41 radii from centre |

**Both pairs disagree.** The inner belt differs by about 360 km at the
low end. The outer belt agrees at the low end within rounding and
differs by roughly a factor of 1.5 at the high end.

Please do **not** reconcile them. Do not assume one is a rounding of the
other, and do not pick a winner. Rows 3, 4, 8 and 9 are each answered on
their own, against a source. Deciding which figure survives is our job.
Telling us what the sources actually say is yours -- and "no source
states this" is among the more useful things you can tell us.

---

## One more note on row 5

Our inner belt text cites Baker et al. (2018) for the **peak** only. It
does not cite Baker for the span. So row 5 asks only about the peak.
Whether Baker also happens to state an extent is row 3's question, and
if he does, please say so there rather than here.

---

Written September 2026 with Anthropic's Claude Opus 5, for Tony
Quintanilla's Paloma's Orrery.
