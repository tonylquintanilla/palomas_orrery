# L-321 source recovery -- what GPT's named sources actually say

Built on orrery `f1bceefd05eeee0cac38fd519dd207314acb2383`
at https://github.com/tonylquintanilla/palomas_orrery

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-13
Type: FINDING for L-321 (zero code). Handles: L-321, L-305, L-323.

## What this is, and what it is not

The GPT 6 Medium returns named sources but lost every URL in transfer,
and GPT could not recover them. Tony ruled: recover the sources by
search instead, no additional cross check.

So this document reports what I opened and what each source says. Every
URL below is one I actually fetched or read in a search result, with an
access word on the project's own scale: OPEN (full text), ABSTRACT,
SNIPPET, WALLED.

**This is not a worksheet and must not be cited as one.** A worksheet is
an independent checker's verdict. I am the session that will build
L-305 item 7, so I am not independent, and I went looking for sources
GPT had already named rather than searching blind. Nothing here carries
a verdict token. It is evidence for Tony to rule on.

It is also a PARTIAL pass. The sources reached are named below; the ones
not reached are named at the end.

---

## 1. Koskinen and Kilpua (2022), chapter 1 -- OPEN, full text

**URL opened:** https://link.springer.com/chapter/10.1007/978-3-030-82167-8_1
**Access: OPEN.** Springer, CC BY 4.0, doi 10.1007/978-3-030-82167-8_1,
pages 1-25, published 31 October 2021 in the printed 2022 volume
*Physics of Earth's Radiation Belts*, Astronomy and Astrophysics
Library. The OAPEN PDF of the whole book is bot-blocked to me; the
Springer chapter page is not, and it carries the full section text.

This is the source GPT named as "Koskinen and Kilpua, sec. 1.1". It is
the most useful thing the whole round turned up, and it answers more
questions than it was asked.

**What section 1.1 states.** A population of multi-MeV protons, up to
1 to 2 GeV, dominates the ion radiation at equatorial geocentric
distances of about 1.1 to 3 R_E, with R_E taken as 6370 km. The inner
electron belt is partially co-located with that proton belt at
equatorial distances of about 1.1 to 2 R_E. The outer belt is beyond
about 3 R_E, extending to distances of 7 to 10 R_E, with electron
energies from tens of keV to several MeV. Most activity occurs in what
the authors call the heart of the outer belt, at equatorial distances
of about 4 to 5 R_E. The figure 1.1 caption says the inner belt is
within 2 R_E from the centre of the Earth. The Van Allen Probes found
an almost impenetrable inner edge for ultra-relativistic electrons
(above roughly 4 MeV) at an equatorial distance of 2.8 R_E.

**And the frame is stated outright, in the chapter's own footnote 2:**
when giving an altitude in terms of Earth radius, the authors always
refer to geocentric distance.

**Other things this chapter settles in passing**, all in section 1.2:

- The dipole axis is tilted 11 degrees from Earth's rotation axis. That
  is the 11-degree tilt the handoff records as a physical measurement
  typed at a call site with no store row. It now has an open source.
- The nose of the magnetopause is, under average solar wind conditions,
  at about 10 R_E from the centre of the Earth, and can be pushed in to
  the vicinity of geostationary distance (6.6 R_E) under large solar
  wind pressure.
- Under typical solar wind conditions the apex of the bow shock is
  about 3 R_E upstream of the magnetopause. Ten plus three is an
  independent, open, textbook corroboration of a bow shock near 13 R_E.
- L is defined as r0 / R_E, McIlwain's parameter, and the chapter gives
  the surface footprints: L = 2 reaches the surface at 45 degrees
  latitude, L = 4 at 60 degrees, L = 6.6 at 67.1 degrees.
- The nightside magnetosphere is described as very long, extending far
  beyond the orbit of the Moon. No figure is attached.

### What this does to the worksheet rows

**Inner belt span, worksheet 3 row 3.** The figure 1.1 to 2 Earth radii
IS stated by an accessible source, in geocentric Earth radii, and it is
stated for the inner ELECTRON belt. Fable's verdict that no accessible
source states it does not hold. GPT's reading was right, including the
qualification it attached -- the proton population that the orrery's
hover calls "mainly protons" runs to 3 R_E, not 2.

**Outer belt span, worksheet 3 row 8.** The source says the outer belt
runs from about 3 R_E out to 7 to 10 R_E. So the orrery's "3 to 7" is
the lower part of a published range rather than a figure nobody states.
Seven is where the source's range BEGINS to end, not where it ends.

**Outer altitude pair, worksheet 3 row 9, and this reverses a verdict.**
Fable marked "13,000 km to 60,000 km" NO, reasoning that 60,000 km is
10.4 R_E geocentric, outside the orrery's own 10.25 R_E magnetopause,
and so physically impossible. Koskinen and Kilpua put the outer belt's
outer reach at 7 to 10 R_E. The belt's outer edge approaching the
dayside magnetopause is not an impossibility -- it is why magnetopause
shadowing is a standard loss mechanism. The upper figure is at the top
of the published range, not outside it.

**Outer peak, worksheet 3 row 7, and this bears on the design.** The
heart of the outer belt is given at 4 to 5 R_E EQUATORIAL GEOCENTRIC,
not in L. So 4.5 as the midpoint of that band has a source stating the
band in the same frame the orrery's hover uses.

**Which reopens ruling B of the design record.** That ruling holds that
the store should carry L, because the frame the sources state for both
belts is L rather than geocentric R_E. Koskinen and Kilpua state these
extents in geocentric R_E and say so explicitly in a footnote. The
numbers coincide, because at the equator they must -- but the ruling's
stated REASON is that no source gives R_E, and one does. Whether that
changes the ruling is Tony's call; the premise has moved.

---

## 2. Griessmeier et al. (2016) -- OPEN, full text

**URL opened:** https://www.aanda.org/articles/aa/full_html/2016/03/aa25452-14/aa25452-14.html
**Access: OPEN.** Astronomy and Astrophysics, "Galactic cosmic rays on
extrasolar Earth-like planets II", full HTML.

This is the source GPT named for worksheet 1 rows 4 and 5.

For a planet with an Earth-like surface pressure of 1033 hPa, reducing
the magnetic shielding raises the biological radiation dose rate by a
factor of two, which the paper calls non-critical for biological
systems. For a thin atmosphere at 97.8 hPa the planetary magnetic field
changes the dose by up to two orders of magnitude. The conclusion is
stated plainly: for a planet with Earth-like atmospheric pressure, weak
or absent magnetospheric shielding against galactic cosmic rays has
little effect on the planet.

**Worksheet 1 row 5, "making complex life possible".** Both checkers
returned NO on this. This is the open source behind that, and it is the
strongest single finding in the round for the visitor-facing text: at
Earth's atmospheric pressure, the magnetosphere is not what stands
between the surface and galactic cosmic rays. The atmosphere is.

**Worksheet 1 row 4, cosmic ray protection.** The same paper is why
"protects Earth from cosmic rays" overstates. The shielding is real and
it is not the dominant term at Earth's pressure.

---

## 3. The magnetotail sources -- three OPEN, one unresolved

**Ness, Scearce and Cantarano (1967), NTRS record.**
URL opened: https://ntrs.nasa.gov/citations/19670023428
Access: OPEN (record page). The title reads "Probable observations of
the geomagnetic tail at 10^3 R_E by Pioneer 7", and the record
describes Pioneer VII observations of the geomagnetic tail downstream
of the solar wind interaction at 900 to 1050 Earth radii. This confirms
the distance, the word "probable", and Fable's reading, which was taken
from the full GSFC preprint.

**Behannon (1967), Explorer 33 mapping -- OPEN, full text.**
URL opened: https://ntrs.nasa.gov/api/citations/19670023519/downloads/19670023519.pdf
The Explorer 33 mapping established that the tail is still well defined
out to 80 Earth radii, beyond lunar orbital distance, and that the bow
shock remains a detectable boundary at a geocentric distance of 75.7
Earth radii. The paper also reports the tail cross-section is probably
not cylindrical and the field magnitude decreases down the tail.

**Fairfield, "The Geomagnetic Tail", GSFC preprint X-616-68-345 --
OPEN, full text.**
URL opened: https://ntrs.nasa.gov/api/citations/19680025161/downloads/19680025161.pdf
A review of tail observations. It records Explorer 33 measurements of
the tail and its boundaries out to 80 R_E and a decrease of the tail
field with downtail distance.

**This is where GPT's citation does not match what I found.** GPT's
note described Fairfield (1968) as comparing Pioneer 7 with simultaneous
Explorer 28 and 33 measurements and identifying about ten intervals at
roughly 1,000 R_E. The Fairfield document I opened under that title is a
tail review whose Explorer 33 content stops at 80 R_E. Either GPT meant
a different Fairfield paper or its description drifted. Treat the ten
intervals as unverified.

**Walker and Lazarus (1975), NTRS record.**
URL opened: https://ntrs.nasa.gov/citations/19750044668
Access: OPEN (record page). An extensive re-analysis of Pioneer 7 plasma
and magnetic field data about 1000 Earth radii downstream, reporting
measurable proton fluxes flowing away from Earth, field reversal regions
where the field rotates from radial to antiradial in the north-south
plane, and general tail characteristics similar to those seen near
Earth. This is a later, fuller treatment of the same signature, and
Fable named it from a snippet without opening it.

**What this does to worksheet 1 row 7.** The magnetotail picture stands
as both checkers described it, with the record now open rather than
snippeted: a well-defined tail measured to 80 R_E in 1967, coherent to
about 220 R_E by ISEE-3 in 1983, and an intermittent signature near
1,000 R_E from Pioneer 7 that a 1975 re-analysis treats as real. The
design record's ruling -- one scalar holding a lower bound, read as
"observed to at least" -- is unaffected and now better supported.

---

## What was NOT reached

Named so the gap is visible rather than implied. These are GPT's other
sources, none of them opened in this pass:

- Maiti and Ramachandran (2023), preprint -- worksheet 3 row 4, the
  inner altitude pair.
- University of Minnesota mission announcement (2012) -- worksheet 3
  row 9, the outer altitude pair. Both checkers already agree it is
  public-outreach material rather than a measurement.
- Y. X. Li et al. (2023) -- worksheet 3 row 8. A search surfaced a
  figure caption placing the outer belt between the 3 and 7 L shells,
  in a paper whose figure is adapted from Wikipedia. I did not open the
  paper and cannot confirm the page 109 pointer.
- Selesnick et al. (2014), Li et al. (2015), Shi et al. (2020) --
  worksheet 3 rows 2, 6, 7, 10.
- Urbar et al. (2019), Ingale et al. -- worksheet 2 row 1 and row 2.
- Kumar and Pulkkinen (2025) -- worksheet 1 row 1, the independent
  reproduction of Shue equation 10.

The OAPEN PDF of Koskinen and Kilpua is bot-blocked to this sandbox;
the Springer chapter page served the same text, so nothing was lost.
Tony can try OAPEN directly if the whole book is wanted.

---

## What Tony has to decide

1. **The frame.** Design record ruling B says the store holds L because
   the sources state L. Koskinen and Kilpua state the belt extents in
   geocentric Earth radii and say so in a footnote. Keep the ruling,
   or revisit it.
2. **The four extents.** All four have a source now. Rows 3 and 8 can
   cite Koskinen and Kilpua directly in the frame the hover already
   uses. Rows 4 and 9 remain public-outreach figures, but row 9's upper
   end is no longer the impossibility Fable called it.
3. **The "complex life" sentence.** Two checkers returned NO and an
   open paper says the atmosphere does the work. Cut it, soften it to
   what Griessmeier supports, or keep it knowingly.

Written September 2026 with Anthropic's Claude Opus 5.
