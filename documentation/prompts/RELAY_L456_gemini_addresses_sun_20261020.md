<!-- Doc-Kind: hand | Relay prompt for Gemini 4: find the open web address of each work the Sun room's citations name (L-456). Copy everything below the line into Gemini. -->
# Relay prompt for Gemini 4 -- web addresses for the Sun room's citations (L-456)

Written 2026-10-20 by Anthropic's Claude Opus 5.5 for Tony to carry to
Gemini 4. Copy everything below the line. Any effort tier will do: every
row names its work, so each is bounded (open it, find the sentence,
stop). Claude re-opens every address that comes back before it goes on
a row. The Earth room's works are a second prompt, RELAY_L456_gemini_addresses_earth_20261020.md: two shorter answers lose less if the Gemini app drops one.

---

Built on palomas_orrery e8e714da99e0ec102fe179341cf767458d2e8545 at
https://github.com/tonylquintanilla/palomas_orrery and
tonyquintanilla.github.io ca5339fd3c22d61a1540e4314726e85003e48751 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Every
citation below is written out here as the website serves it today, so
you do not need the repositories.
Vocabulary: v2 (2026-08-13)

## Who you are working for

Tony Quintanilla, PE, a retired civil and environmental engineer, builds
Paloma's Orrery, a 3D astronomy visualization (a desktop program and the
website palomasorrery.com), through conversation with AI partners. He is
not a professional programmer or astronomer. Please write plainly.

## The job

The website's information panel lists the sources behind each drawn
feature. Visitors should be able to tap a source and open it. These
citations name their work but carry no web address. For each WORK
below, find the address of a copy anyone can read, open it, and show
us that it is the same work and that it says what we cite it for.

## The rules this job follows

If you have imported the palomas_orrery repository, read this file and
name it at the top of your answer:
skills/provenance-discipline/SKILL.md -- sections The Access Standard
and What a Visitor Reads. If you have not imported it, say so; the
rules you need are here:

1. **Open copies first.** Prefer, in this order: the publisher's own
   open-access page; an arXiv preprint of the same paper; the NASA ADS
   abstract page; an agency's own page or document. A paywalled page is
   still worth reporting as the DOI's address, but say it is paywalled
   and keep looking for an open copy.
2. **Name what you opened.** The title and authors exactly as printed
   on the page you opened. A different paper with a similar title is a
   different work: say so.
3. **Quote it.** A short verbatim quote from the page you opened that
   carries what we cite the work for, with a locator (section, table,
   equation, page, or abstract). A row without both is recorded as
   UNVERIFIED whatever it says. If you are recalling rather than
   reading, say so and leave the row UNVERIFIED. Silence is better than
   a guess.
4. **Never build an address from memory.** Every address you report is
   one you opened in this session.

## Before any row: a pre-flight

Open this page and quote one sentence from it, so we know your fetching
works:

```
https://arxiv.org/abs/2202.11533
```

## Your answer's header

Start with one line naming your MODEL and your EFFORT TIER, then the
rule file you read (or "not imported").

## The table

One row per numbered work, in this exact layout:

| # | Work as we cite it (short) | Address opened | Access word | Title and authors as printed | Quote | Locator | Same work? | Says what we cite? | Notes |

- **Access word**: one of open full text, abstract, agency page, open
  document, paywalled, book (no open copy).
- Each verdict cell holds EXACTLY ONE token:

```
Same work?           YES  NO  UNVERIFIED
Says what we cite?   YES  NO  PARTIAL  UNVERIFIED
```

- Where a work has a DOI, also give its doi.org address in Notes, even
  when the open copy is elsewhere.
- Put every address as a bare URL inside a code block after the table,
  numbered by row. Links pasted as chips lose their address.
- Please deliver the whole answer as a downloadable Markdown file named
  worksheet_gemini4_<effort tier>_L456_sun_20261020.md, as well as in
  the chat.

## The works

Each row gives the work as our citation names it, then, after "We cite
it for:", the sentence or figure our citation rests on.

S1. Delsemme (1987), A&A 187:913
We cite it for: the aphelia of 152 long-period comets avoid both galactic polar caps and a strip along the galactic equator.

S2. Matese and Whitmire, arXiv:1004.4584, sec. 2.2
We cite it for: the galactic tide's main term goes as |sin B cos B|.

S3. Higuchi (2020), AJ 160:134
We cite it for: a reading of the comets' galactic-latitude pattern that differs from Delsemme's (row S1).

S4. Gurnett, D. A., Kurth, W. S., Burlaga, L. F. and Ness, N. F. (2013), "In situ observations of interstellar plasma with Voyager 1", Science 341, 1489-1492, doi:10.1126/science.1241681
We cite it for: p. 1489: the first sign of the heliopause came on 28 July 2012, at 121 AU; the last of five crossings was on 25 August 2012.

S5. IAU 2015 Resolution B3 (nominal solar radius), published as Prsa et al. (2016), AJ 152, 41, doi:10.3847/0004-6256/152/2/41
We cite it for: the nominal solar radius, 695,700 km. Report both the IAU's own page for the resolution, if one opens, and the paper.

S6. IAU 2018 (Archinal et al.), the IAU Working Group on Cartographic Coordinates and Rotational Elements report
We cite it for: the Sun's north pole in ICRF equatorial coordinates (right ascension and declination of the pole).

S7. Liu, Zhu and Hu, "Constructing a Galactic coordinate system based on near-infrared and radio catalogs", arXiv:1110.6268
We cite it for: eq. (2): the north galactic pole at J2000.0, alpha = 12h 51m 26.2755s, delta = +27 deg 07' 41.704"; sec. 3.2, eq. (8): Sgr A* at alpha = 17h 45m 40.0400s, delta = -29 deg 00' 28.138".

S8. Murray, C. A. 1989, A&A 218, 325
We cite it for: the transformation to galactic coordinates adopted for Hipparcos (the paper Liu, Zhu and Hu draw the pole from).

S9. ESA 1997, The Hipparcos and Tycho Catalogues, ESA SP-1200
We cite it for: the catalogue's adopted galactic pole (the volume Liu, Zhu and Hu cite as the standard).

S10. Reid, M. J. and Brunthaler, A. 2004, ApJ 616, 872
We cite it for: the absolute position of Sgr A* from Very Long Baseline Array measurements.

S11. NIST Special Publication 811, Guide for the Use of the SI, sec. 5.1.1, Table 6
We cite it for: the units accepted for use with the SI: the minute is 60 seconds, the hour 3600 seconds, and the second of arc one sixtieth of the minute of arc, which is one sixtieth of the degree.

S12. Murray & Dermott, "Solar System Dynamics" (1999), Sec. 4.6
We cite it for: the Roche limit. This is a book: report a publisher's page or an open excerpt only if one opens; "book (no open copy)" is a fine answer.

S13. NASA Science, "Oort Cloud Facts"
We cite it for: the inner edge of the Oort cloud is thought to lie between 2,000 and 5,000 AU from the Sun, and the outer edge between 10,000 and 100,000 AU.

S14. Portegies Zwart, S., Torres, S., Cai, M. X. and Brown, A. G. A. (2021), "Oort cloud Ecology II: the chronology of the formation of the Oort cloud", A&A 652, A144, doi:10.1051/0004-6361/202040096
We cite it for: sec. 2.2: the Hills cloud lies between the outer edge of the parking zone and the inner edge of the Oort cloud, at about 20,000 au or less; the Sun's Hill radius in the Galactic potential is about 0.65 pc (Fig. 2 and Fig. 3 captions; sec. 5).

S15. Stone, E. C., Cummings, A. C., McDonald, F. B., Heikkila, B. C., Lal, N. and Webber, W. R. (2005), "Voyager 1 explores the termination shock region and the heliosheath beyond", Science 309, 2017-2020, doi:10.1126/science.1117684
We cite it for: abstract: Voyager 1 crossed the termination shock on 16 December 2004 at 94.01 AU.

S16. Suess & Nerney (2004), Adv. Space Res. 33:668-675, bibcode 2004AdSpR..33..668S
We cite it for: "the closed field regions, or helmets, reach no higher than 2-4 solar radii".


## What not to do

- Do not propose wording for the website.
- Do not combine rows.
- Do not fill a cell from memory. If you could not open a page, the
  cell is UNVERIFIED and Notes says what stopped you.
