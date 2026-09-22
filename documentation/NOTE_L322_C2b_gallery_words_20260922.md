# What Earth's room will say after Stage C2-b -- the words, for approval

Built on orrery `26f26fdbf1a6590ff4bafcfb13606461ab500a3b`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `42fd97dd1a1badd224377246adcdb55e862894ea`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

**Type: WORDS FOR TONY.** September 22, 2026, with Anthropic's Claude
Opus 5.5. The build manifest (section 9, step 5) says these words are
fixed before the gallery patch is cut, because the display check grades
each hover line by finding it word for word. Once you approve them they
become section 6's acceptance strings.

"Today" below was built from the served cache at `42fd97dd` with the
real renderer, not read out of the source. "After" is the proposed
wording. Numbers in the "after" column are the ones the store now
serves at `26f26fdb`; none is typed.

Mark anything you want changed. Anything you do not mark ships as
written.

---

## 1. Magnetopause hover

| Line | Today | After |
| --- | --- | --- |
| standoff | Sunward standoff: 10.25 Earth radii | Sunward standoff: 10.3 Earth radii |
| distance | = 65,376 km (0.000437 AU) | That is about 65,000 km (0.00044 AU). |
| NEW | -- | Spacecraft that cross the real boundary typically find it within 1.23 Earth radii of this model. |

Why "about": a visitor who multiplies 10.3 by Earth's radius gets
65,700, which reads as 66,000. The page prints 65,000 because the store
computes it from the unrounded 10.25 and rounds once, to the two
figures its own uncertainty supports. Both numbers are right; "about"
keeps the pair from reading as an exact equation.

Why "within 1.23" and not "about 1.2": the manifest's example (2.3)
was written before provenance-discipline 2.17, which says a display
prints the count the row declares and never fewer. The row declares
three figures, so the line prints 1.23. That is the skill's call, not a
wording choice.

Why "typically": 1.23 is a standard deviation -- how far real crossings
usually fall from the fitted surface. "Typically within" says that
without the statistics word.

## 2. Bow shock hover

| Line | Today | After |
| --- | --- | --- |
| standoff | Sunward standoff: 13.51 Earth radii | Sunward standoff: 13.5 Earth radii |
| distance | = 86,180 km (0.000576 AU) | That is about 86,200 km (0.000576 AU). |
| NEW | -- | Spacecraft that cross the real shock typically find it within 0.69 Earth radii of this model. |

Same reasons as the magnetopause. "About" is kept here too so the two
hovers read alike.

## 3. Both radiation belts -- the tilt sentence

Today, one sentence:

> The ring lies in Earth's equatorial plane, the daily average of the
> magnetic equator, which is tilted 9.6 degrees from it (IGRF-13, epoch
> 2020-2025) and turns with Earth once a day.

After, split into two so each does one job:

> The ring lies in Earth's equatorial plane, the daily average of the
> magnetic equator, which is tilted 9.4105 degrees from it and turns
> with Earth once a day.
>
> That tilt is for 2020 (IGRF-13 model) and shrinks by 0.0493 degrees
> a year.

No "about" before 0.0493: it is printed to the three figures its row
declares, and "about" in front of three figures reads oddly. "For 2020"
says the epoch in words; the page no longer types "2020-2025", because
the epoch now comes from the store.

## 4. Outer radiation belt -- where it is drawn

Today, two lines:

> Drawn at 4.5 Earth radii, where the measured particle flux peaks
> (given as L = 4.5: where that field line crosses the magnetic equator)
> = 28,702 km (0.000192 AU)

After, two lines, and the kilometre line goes:

> Drawn at 4.5 Earth radii: halfway across the band, 4 to 5 Earth radii
> out at the magnetic equator, where the belt is most intense.
>
> The halfway point is our choice for the picture, not a measured peak.

Why the kilometre line goes: 4.5 is now a rule (the midpoint of two
measured ends), not a measurement. The manifest (17.4) says a rule is
not printed as if it were measured, and a kilometre figure would have
been 28,701.615 km -- eight figures on a number nobody measured.

Why "L" is gone: the interactive-exhibit skill lists "L shell" without
explanation as compression. The new sentence says what L measures
(distance out at the magnetic equator) instead of naming it.

## 5. Numbers that change with no new words

These follow from the rows' declared counts. Listed so nothing on the
phone surprises you.

| Hover | Today | After |
| --- | --- | --- |
| Inner belt, distance | = 9,567 km (0.0000640 AU) | = 9,600 km (0.000064 AU) |
| Inner belt, extent | Measured extent: 1.1 to 2.0 Earth radii | Measured extent: 1.1 to 2 Earth radii |
| Outer belt, extent | Measured extent: 3.0 to 7.0 Earth radii | Measured extent: 3 to 7 Earth radii |

"1.1 to 2" will look uneven. It is what the sources print: Meredith
(2014) gives "1.1" and "2", and the store now declares each end by what
its source printed.

The magnetopause's drawn nose moves about 319 km outward (10.25 to
10.3 Earth radii). You will not see that on the phone, but it is a
drawn number, so it is listed.

## 6. The information panel -- the two source strings

These are read in the "i" panel, not the hover. The change removes the
sentence that typed the old standoff and claimed four figures. Nothing
else is reworded.

**Magnetopause**, the sentence removed:

> ...gives 10.25 R_E. Reported to four figures: Table 1 gives a1 to
> +/- 0.10 R_E and a5 to +/- 0.5, and either alone moves the result by
> about +/- 0.09.

After:

> Shue et al. (1998), J. Geophys. Res. 103:17691, doi:10.1029/98JA01103
> -- eq. 10 evaluated at the declared conditions (Bz = 0 nT, Dp = 2
> nPa). Corroboration: Lugaz et al. (2016), doi:10.1038/ncomms13001 --
> typical subsolar magnetopause 9-11 R_E, which contains this.

**Bow shock**, the sentence removed:

> ...gives 13.51 R_E. Reported to four figures: the paper states no
> uncertainty on its fitted numbers, and what bounds this is the
> crossing scatter of 0.69 R_E (fig. 7).

After:

> Jelinek, Nemecek and Safrankova (2012), J. Geophys. Res. 117:A05208,
> doi:10.1029/2011JA017252 -- eq. 14, R_BS = 15.02 p^(-1/6.55),
> evaluated at the declared pressure of 2 nPa. The paper states no
> uncertainty on its fitted numbers; how far real crossings fall from
> the fit (fig. 7) is given in the hover. Corroboration: Lugaz et al.
> (2016), Nat. Commun. 7:13001, doi:10.1038/ncomms13001 -- 11-14 R_E
> subsolar under normal solar wind, which contains this.

## 7. What does NOT change

- Every other line of these four hovers: the descriptions, the solar
  wind conditions, the cut angles, "Not tilted", the i-button pointer.
- "where the measured particle flux peaks" on the INNER belt. The
  wording question is on the ledger as its own class; it is not changed
  here.
- Every other Earth hover, and every Sun, Jupiter and Saturn hover. The
  build proves this against the recorded fixture.

---

Written September 2026 with Anthropic's Claude Opus 5.5.
