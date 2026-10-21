<!-- Doc-Kind: hand | Review of Gemini 4's two address worksheets for L-456 (the Sun's 16 works, Earth's 23), set against this session's own re-opening of every work: what was confirmed, corrected, and not opened, and how each return did against the rules. -->
# Review: Gemini 4's address worksheets for L-456, against a re-opening of every work

Built on orrery 6a8d04c2ca0ba94a5fb2f5b70c3ebd82c0d934e3 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
30db99fb5ec7c5f996f5adbbf10c23cad1c416a4 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Written October 21, 2026 with Anthropic's Claude Opus 5.5, in the build
session the coordination brief `BRIEF_L456_addresses_build_20261021.md`
set up. Skills loaded and matching the manifest: provenance-discipline
2.32, provenance-cross-check 1.1, interactive-exhibit 1.18,
ledger-and-session-records 1.21, safe-file-editing 1.13.

## How the re-opening was done

Every work in both prompts was opened again by this session, whatever
the worksheet said (provenance-cross-check 1.1, The Slice Relay: a
return is a set of leads). Pages were read through the chat's web-fetch
tool; papers that refuse automated readers were read from Tony's own
copies in the orrery's `papers/` folder through the device link
(Murray 1989, Shue et al. 1998, Jelinek et al. 2012, the IADC
guidelines). Where Gemini's quote matched what this session read, the
row's `# Read:` line names both readers. The patch is
`patch_L456_4_addresses_orrery_20261021.py` (the rows) with
`patch_L456_5_addresses_website_20261021.py` (the six citations only the
website writes).

## 1. The Sun's worksheet (16 works)

`documentation/worksheets/worksheet_gemini4_medium_l456_sun_20261020.md`,
Gemini 4, medium tier, repository not imported. Its pre-flight PASSED:
it quoted arXiv:2202.11533's first sentence and named the page
correctly (Lamy, Gilardy and Llebaria).

### Confirmed on re-opening, address now on the row (12)

| # | Work | Address written | Where it was read |
|---|---|---|---|
| S2 | Matese and Whitmire (2011) | https://arxiv.org/abs/1004.4584 (website's tide citation) | arXiv PDF, sec. 2.2, "the dominant disk tidal term ... is proportional to \|sin B cos B\|" |
| S3 | Higuchi (2020) | https://arxiv.org/abs/2008.04324 (website's tide citation) | arXiv HTML, sec. 5 and sec. 6 item 4, "better than the explanation by Delsemme (1987)" |
| S4 | Gurnett et al. (2013) | the authors' copy at space.physics.uiowa.edu (the address Gemini gave, which differs in two places from the one our Access line held) | p. 1489, the 28 July 2012 and 25 August 2012 sentences |
| S5 | IAU 2015 Resolution B3 | the IAU's own PDF | Recommends 3, 1 R_sun^N = 6.957 x 10^8 m |
| S7 | Liu, Zhu and Hu (2011) | https://doi.org/10.1051/0004-6361/201116947, which resolves to A&A's free full text | eq. (2) and eq. (8), as the rows quote them |
| S8 | Murray (1989) | the ADS abstract page (the brief's address; ADS refuses this session, so it is the address Tony's scan came from) | Tony's scan in `papers/`: sect. 7.1, p. 329, the pole of J2000.0 is 12h 51m 26.2755s, +27 deg 7' 41.704" |
| S10 | Reid and Brunthaler (2004) | https://arxiv.org/abs/astro-ph/0408107 | the arXiv page: title and authors |
| S11 | NIST SP 811 | NIST's chapter 5 page | Table 6: the minute, hour and day, and the minute and second of arc |
| S13 | NASA Science, "Oort Cloud Facts" | the page | "Scale and Distance", the inner and outer edge sentence |
| S14 | Portegies Zwart et al. (2021) | https://doi.org/10.1051/0004-6361/202040096, which resolves to A&A's free full text | sec. 2.2 ("<~20 000 au") and the Fig. 2 and Fig. 3 captions ("about 0.65 pc") |
| S15 | Stone et al. (2005) | Caltech's record of the paper, authors.library.caltech.edu | the abstract sentence, 16 December 2004 at 94.01 AU |
| S16 | Suess and Nerney (2004) | the ADS abstract page Tony opened on 2026-08-21 | NTRS's copy of the abstract, its first sentence |

Murray's direction cosines were checked too: the third column of his
eq. (33) gives RA 192.8594812 and Dec 27.1282512 degrees, within
0.0004 arcseconds of the two pole rows. That was the check the brief
asked for, against the pole figures cited through Liu, Zhu and Hu.

### Corrected and re-homed (1)

- **S12, Murray and Dermott, the Roche limit.** The row named Sec. 4.6;
  the book's contents put the Roche zone at 4.8 and 4.6 is the
  Darwin-Radau relation. Read on the authors' own book site
  (ssdbook.maths.qmul.ac.uk, chapter 4's sections in order) and in the
  printed contents Gemini quoted. Gemini's correction was right. The
  book has no open copy, so the row was RE-HOMED (The Access Standard)
  to Rappaport, S., Sanchis-Ojeda, R., Rogers, L. A., Levine, A. and
  Winn, J. N. (2013), "The Roche limit for close-orbiting planets",
  https://arxiv.org/abs/1307.4080, sec. 2, eq. (1): "The Roche limiting
  distance for a body comprised of an incompressible fluid", a_min =
  2.44 R (rho_s/rho_p)^(1/3), "R is the radius of the parent star".
  Read 2026-10-21 by this session; the book stays as an Also line at
  sec. 4.8.

### Did not open (3), all to Tony's reading list

- **S1, Delsemme (1987).** ADS refuses automated readers; Semantic
  Scholar refused this session too. Gemini read it through Semantic
  Scholar's abstract. Address known (ADS).
- **S6, Archinal et al. (2018), the Sun's pole.** Springer, USGS and
  ResearchGate did not give this session the paper. The PDF in Tony's
  `papers/` folder is the 2019 CORRECTION to the report (Celest. Mech.
  Dyn. Astron. 131:61), not the report, and does not hold the Sun's
  pole. Gemini quoted Table 1 from ResearchGate. Tony opened the DOI
  from his phone on 2026-10-21: the paper is not free, and the abstract
  he pasted names the report but not the Sun's pole. RE-HOMED (The
  Access Standard): NASA NAIF's planetary constants kernel
  pck00011.tpc (N. Bachman, 2022), https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/pck00011.tpc,
  read 2026-10-21 by this session, names this report as its source and
  prints BODY10_POLE_RA = 286.13 and BODY10_POLE_DEC = 63.87, the
  values our pole uses. The website's citation now names NAIF's file,
  with the report as the layer below. (The 2019 correction in `papers/`
  does not touch the Sun.)
- **S9, the Hipparcos volume, sec. 1.5.3.** The ESA PDF opens but the
  fetch tool reads only its opening pages, and the sandbox cannot reach
  cosmos.esa.int. Gemini could not reach p. 91 either and quoted
  Perryman et al. (1998) instead. Murray (1989) is now read directly
  and gives the same pole, so this is the third layer, not a gap in the
  row. Address known.

### Still without a link after this build

None of the Sun's served citations.

### How the Sun's return did against the rules

Good. Every row carried a quotation and a locator; it said plainly
where it could not open a page (ADS for S8, the PDF's truncation for
S9) and marked those UNVERIFIED rather than guessing. Its one
correction (S12) was right. Two faults, both in transfer rather than
reading: six DOIs came wrapped in Google redirect addresses in the
table (the bare-URL block was clean), and it named S13's author as
Amanda Barnett where the page today names Alicia Cermak.

## 2. Earth's worksheet (23 works)

`worksheet_gemini4_medium_L456_earth_20261021.md`, Gemini 4, medium
tier, repository not imported (its Canvas names the file
`..._20261020.md`). It was not in the orrery's
`documentation/worksheets/` when the work began, so the Earth half was
re-opened from the original prompt's rows
(`documentation/prompts/RELAY_L456_gemini_addresses_earth_20261020.md`)
without it. Tony then sent its share link,
https://gemini.google.com/share/c965fea3cc63, read 2026-10-21 in the
desktop app's browser; the comparison below is against that page.
Tony saves Gemini's exported file into `documentation/worksheets/`;
the exported file is the record.

**No Earth row's `# Read:` line names Gemini**, even where its quote
matches what this session read. A run that did not open its own
pre-flight page has not shown that it reads; a matching quote from it
could be a read or a recollection, and the row cannot tell which. The
Sun's run, whose pre-flight passed, is named where it matched.

### The return's failed pre-flight, first

Recorded from the brief (Claude Fable 5.1, 2026-10-21): asked to open
arXiv:2202.11533 and quote a sentence, Gemini described a Gaia
lensed-quasar paper by Jalan and others. The page is Lamy, Gilardy and
Llebaria, "Observations of the Solar F-corona from Space", as the Sun's
run reported the day before. So that run did not open its pre-flight
page, and its 23 rows are leads only.

The page shows the same failure: its pre-flight row names "Gaia GraL:
Gaia Gravitational Lens Systems. VII. X-ray Observations of Lensed
Quasars; Priyanka Jalan, Jean Surdej, Dominik Sluse, et al.", with
the status "Opened and verified in this session".

### Gemini's 23 rows against this session's reads

- **Matched what this session read (13):** E2, E3, E6, E7, E12, E14,
  E15, E16, E17, E18, E20, E21, E23. Same quote, same place.
- **E1, Alken et al.: Gemini wrong.** It puts the pole in Table 3,
  quoting a ResearchGate PDF, and says Table 4 lists observatories. The
  journal's own page (link.springer.com, through the DOI), read
  2026-10-21 in the desktop app's browser, numbers them the other way:
  "Table 3 Magnetic observatories contributing data used in the
  construction of IGRF-13" and "Table 4 Magnetic pole position since
  1900 determined from IGRF-13". The rows keep Table 4. Its figures,
  80.65 and -72.68, agree.
- **E9, IERS TN 36: PARTIAL, about a figure we do not use.** Its note
  is that Table 1.2 (GRS80) gives a_E = 6378137 m; our row holds
  6378.1366 km, which is Table 1.1's 6378136.6 m, as cited. Its other
  point agrees with this session's read of sec. 2.1.1: the pole offsets
  are 17.1 and 5.0 mas, and the +/-0.02" there is the FK5 equator's
  accuracy. The pole row's Source line already states the offsets.
- **E5, PREM:** the same three radii, from two other open tabulations
  (GFZ Potsdam and SOEST Hawaii). This session used the one at P.
  Shearer's UCSD page; any of the three would do.
- **E8:** the same sentence, from a mirror at juliaastro.org; this
  session used the IAU's own PDF.
- **E4, Baliukin et al.:** Gemini quotes the abstract from ResearchGate;
  this session could not open ResearchGate or Wiley. Tony then read
  it from his phone (Did not open, below), and Gemini's quote matches
  his.
- **E10, E11, E19, E22: secondary sources, as the brief warned.** E10
  from a 2010 conference precursor by the same authors; E11 UNVERIFIED
  (it reached only LASP's list and a summary); E19 and E22 from
  Nishida (2000) and Sibeck and Lin (2014). This session read E10 and
  E11 in the papers themselves; E19 Tony read in its own abstract; E22 stays on his list. No row
  was re-homed to a secondary paper.
- **E13: PARTIAL**, because Li, Tu et al. state the outer belt and not
  the inner. Our row cites them for the outer belt only, so nothing to
  change.

### How Earth's return did against the rules

Poorly, and visibly so, which is the pre-flight doing its job. The
pre-flight failed, and the run marked it "Opened and verified". Its one
correction (E1's table number) was wrong. It leaned on secondary papers
for four works, as the brief warned. Its bare-URL block was clean, but
the Canvas copy wraps seven DOIs in Google redirect addresses, as the
Sun's did. Where it did reach the work (thirteen rows) its quotes are
verbatim. Taken as leads, it named the open copies for E7 and E12
that this session also found.

### Confirmed on re-opening (20)

| # | Work | Address written | Where it was read |
|---|---|---|---|
| E1 | Alken et al. (2021) | https://doi.org/10.1186/s40623-020-01288-x, the journal's open page | Table 4, row 2020.0, north geomagnetic pole 80.65, -72.68 |
| E2 | IGRF-13 coefficient file | NOAA NCEI's copy of the file | g 1 0, g 1 1, h 1 1 at 2020.0 and their SV |
| E3 | Baker et al. (2018) | https://doi.org/10.1007/s11214-017-0452-7, Springer's open full text | sec. 2, r ~ 1.5 R_E |
| E5 | PREM (Dziewonski and Anderson 1981) | the model's open tabulation, Table A.1 of "The PREM Model" at P. Shearer's UCSD page (re-homed: the paper is walled) | 1221.5, 3480.0 and 6346.6 km |
| E6 | Folkner et al. (2014) | JPL's own PDF of IPN Progress Report 42-196 | the abstract |
| E7 | IADC guidelines, Rev. 2 | NASA Orbital Debris Program Office's copy, also read in Tony's copy | 3.3.1 and 3.3.2 (1), p. 8 |
| E8 | IAU 2012 Resolution B2 | the IAU's PDF of its 2012 resolutions | Recommends 1, the exact au |
| E9 | IERS Conventions (2010), TN 36 | the IERS Conventions Centre's PDF | Tables 1.1 and 1.2; sec. 2.1.1's pole offsets |
| E10 | Jelinek et al. (2012) | https://doi.org/10.1029/2011JA017252 (AGU, free to read; refuses automated readers) | Tony's copy: eq. 14, lambda_BS = 1.17, Fig. 7(a) 0.69 R_E |
| E11 | Li et al. (2025) | NSF's public-access copy, par.nsf.gov | sec. 1 para. 1, L = 4 and 5 |
| E12 | Meredith et al. (2014) | the NERC Open Research Archive's copy | introduction para. 1, 1.1 to 2 and 3 to 7 R_E |
| E13 | Li, Tu et al. (2024) | NSF's public-access copy | introduction, 3 to 7 R_E |
| E14 | NASA Earth Fact Sheet | the page | volumetric mean radius 6371.000 km |
| E15 | Ishii et al. (2018) | https://doi.org/10.1038/s41598-018-24832-y, open | 660 +/- 10 km |
| E16 | NOAA JetStream | the page | 50 km; 85 to 600 km |
| E17 | NASA, "Earth's Atmospheric Layers" | the NASA image article of that title (January 22, 2013) | 50 km; 600 km |
| E18 | Shue et al. (1998) | https://doi.org/10.1029/98JA01103 (AGU, free to read; refuses automated readers) | Tony's copy: Table 1 "After Fit", a1 to a8; 1.23 R_E |
| E20 | Slavin et al. (1983) | NTRS's record, already on the row; added to the website's magnetotail citation | the abstract: out to X = -220 Earth radii; five authors as the row names them |
| E21 | Sibeck and Lin (2014) | NTRS's PDF (website's magnetotail citation) | the abstract: cross-sections "elongated in the direction parallel to the component of the IMF in the plane perpendicular to the Sun-Earth line" |
| E23 | JPL Horizons manual | the manual's page | "International Celestial Reference Frame (ICRF)": at most 0.02 arcseconds |

Eighteen of these gained an address on orrery rows (E1 to E3, E5 to
E18, and E23). E20's row already carried its NTRS address; E20 and E21
gain theirs in the website's own magnetotail citation.

One note from the reading. E17: the page our row means is NASA's "Earth's Atmospheric Layers"
image article; NASA Science's "multi-layered cake" page gives the
thermosphere to 700 km and is a different page.

### Did not open (1), to Tony's reading list; two he read

- **E4, Baliukin et al. (2019): read by Tony.** Wiley and HAL refuse
  automated readers. Tony opened the DOI from his phone on 2026-10-21
  (the paper is free) and pasted the abstract: "The geocorona was found
  to extend at least up to 100 Earth radii (RE) with an intensity of 5
  Rayleigh". The row carries the DOI's address and names Tony.
- **E19, Slavin et al. (1985): read by Tony.** Wiley refuses automated
  readers, and the NTRS hit for it is a different paper (a 1985
  Chapman Conference paper by the same group). Tony opened the DOI from
  his phone on 2026-10-21 and pasted the abstract, which is free though
  the paper is not: "On the basis of 756 magnetopause crossings a
  low-latitude magnetotail diameter of 60+/-5 RE at |X| = 130 - 225 RE
  is determined" and "Flaring ceases on average at |X| = 120 +/- 10
  RE". Both rows and the website's magnetotail citation now carry the
  DOI's address, and the rows' Read lines name Tony.
- **E22, Maezawa et al. (1997).** ScienceDirect refuses automated
  readers. Address known (DOI). Cited only in the website's own
  magnetotail words.

### Secondary papers (the brief's E10, E11, E19, E22)

The brief warned that Gemini leaned on secondary papers for these four.
This session used none: E10 was read in the paper itself (Tony's copy),
E11 in the paper itself (NSF's copy of the same article), E19 in its
own abstract (Tony's read), and E22 was not opened and goes to Tony. Nothing was re-homed to a
secondary paper.

## 3. What is left without a link, by name

Sun (0).
Earth (0). Maezawa et al. (1997) sits inside
the website's magnetotail citation, which now links its other three
works.

Session record written October 2026 with Anthropic's Claude Opus 5.5.
