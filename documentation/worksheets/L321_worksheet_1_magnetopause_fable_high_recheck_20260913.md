# Citation worksheet 1 of 3 -- RETURN (recheck, high effort)
## Earth's magnetopause and magnetotail

**Built on** `f1bceefd05eeee0cac38fd519dd207314acb2383` at
https://github.com/tonylquintanilla/palomas_orrery

Vocabulary: v2 (2026-08-13)

**Checker:** Anthropic's Claude Fable 5.1, high effort tier, working in
Tony's Claude Project (protocol and installed skills resident,
provenance-discipline 2.11 loaded and matched against the manifest),
2026-09-13. This is an independent second pass over worksheet 1; the
earlier Fable return was not consulted while filling the table.

**Rule files read at that SHA** (shallow fetch of f1bceefd, HEAD
confirmed by `git ls-remote` at the same value):

- `PROJECT_INSTRUCTIONS.md`, section "Fetched vs Recalled Convention",
  lines 739-753 -- READ.
- `skills/provenance-discipline/SKILL.md`, sections "The Access
  Standard [CRITICAL]" (line 380) and "Worksheet Types" (line 756) --
  READ. The installed copy and the repo copy both read version 2.11.

**Code value check.** `EARTH_MAGNETOPAUSE_STANDOFF_RADII = 10.25` at
`constants_new.py` line 515, derived there from the five Shue
coefficients (lines 377-419) at the declared conditions
`EARTH_SOLAR_WIND_PRESSURE_NPA = 2.0` and `EARTH_SOLAR_WIND_BZ_NT = 0.0`
(lines 343-365). The visitor text is at `earth_visualization_shells.py`
lines 736-738 (panel) and 799-801 (hover), formatted `:.4g`, so the
visitor sees "10.25". Recomputed here: 10.2519.

**Access notes.** Wiley's page for Shue et al. (1998) is labelled "Free
Access" but refused my fetch (bot check), so for me it is WALLED; it
will likely open for Tony. The full text is OPEN on C. T. Russell's
UCLA site, with the equations and Table 1 served as images I cannot
read; the coefficient values were read from an open 2025 paper that
prints them. Every URL below was opened on 2026-09-13.

---

## The worksheet

| # | Job | Claim | Code value | Your value | Source unit | Source (URL opened, access word) | Value correct? | Citation correct? | Notes |
|---|-----|-------|-----------|-----------|-------------|----------------------------------|----------------|-------------------|-------|
| 1 | CITATION | Earth's magnetosphere extends about 10.25 Earth radii on the Sun-facing side | 10.25 R_E | 10.2519 at Bz = 0 nT, Dp = 2 nPa; report "about 10" | R_E, geocentric, on the aberrated Sun-Earth line | https://faculty.epss.ucla.edu/~ctrussell/russell_bib.html/papers/mpause_extreme/ OPEN (full text; equations and Table 1 are images); https://angeo.copernicus.org/articles/43/835/2025/ OPEN (Klingenstein et al. 2025, eq. 2 prints the Shue 1998 coefficients) | APPROX | DERIVED | Arithmetic closes: (10.22 + 1.29 tanh(0.184 x (0 + 8.14))) x 2^(-1/6.6) = 11.387 x 0.9003 = 10.2519. Inputs: the five coefficients are Shue's Table 1 fit (a1 = 10.22 +/- 0.10 per the store's own annotation, which I could not read off the image); Dp = 2 nPa is Shue's own "average value" (paper text, section 3); Bz = 0 nT is a project choice the paper does not make -- Shue uses +/- 4 nT as northward and southward averages. APPROX because this is a model output, not a measurement, and the model's own scatter is 1.23 R_E (Shue 1998 text) and above 0.8 R_E in the subsolar region against 2001-2022 crossings (Klingenstein et al. 2025, section 3.2). Four figures overstate what the fit supports. The derived value inherits the rung of its weakest input, which is the declared Bz. |
| 2 | CITATION | It stretches into a long magnetotail on the night side | (no figure) | hundreds of Earth radii, past the Moon at 60 R_E | R_E | https://science.nasa.gov/heliophysics/focus-areas/magnetosphere-ionosphere/ OPEN | YES | UNSOURCED | The text names no source for this clause. NASA Science: the nightside stretches into an immense magnetotail that fluctuates in length and can measure hundreds of Earth radii, far past the Moon's orbit at 60 Earth radii. Observed extents are row 7. |
| 3 | CITATION | It protects Earth from solar radiation | (no figure) | solar PARTICLE radiation and solar-wind erosion | -- | https://science.nasa.gov/heliophysics/focus-areas/magnetosphere-ionosphere/ OPEN | APPROX | UNSOURCED | No source named. NASA's wording is "solar and cosmic particle radiation" and "erosion of the atmosphere by the solar wind". The claim is right for charged particles (solar wind, solar energetic particles). It is wrong for sunlight, ultraviolet and X-rays, which a magnetic field does not touch -- the atmosphere and ozone do that work. As written, "solar radiation" reads as the whole of the Sun's output, so it overstates. One word fixes it: "charged particles from the Sun". |
| 4 | CITATION | It protects Earth from cosmic rays | (no figure) | partial shielding of Galactic cosmic-ray protons below about 32 GeV for an Earth-like magnetic moment | GeV (particle energy) | https://www.aanda.org/articles/aa/full_html/2015/09/aa25451-14/aa25451-14.html OPEN (Griessmeier et al. 2015, A&A 581, A44); https://science.nasa.gov/heliophysics/focus-areas/magnetosphere-ionosphere/ OPEN | YES | UNSOURCED | No source named. Griessmeier 2015, abstract: without a protecting magnetic field the particle flux to the atmosphere can rise by more than three orders of magnitude; for a planet with Earth's magnetic moment, partial shielding extends up to 32 GeV. Higher-energy cosmic rays pass through; the atmosphere is the larger shield at the surface (their 2016 companion paper, row 5). "Protects" is fair. "Blocks" would not be. |
| 5 | CITATION | ...making complex life possible | (no figure) | not established; open literature argues against necessity | -- | https://www.aanda.org/articles/aa/full_html/2016/03/aa25452-14/aa25452-14.html OPEN (Griessmeier et al. 2016, A&A 587, A159); https://ui.adsabs.harvard.edu/abs/2018A&A...614L...3G/abstract ABSTRACT (Gunell et al. 2018, A&A 614, L3); https://science.nasa.gov/heliophysics/focus-areas/magnetosphere-ionosphere/ OPEN | NO | UNSOURCED | Verdicted as stated: a causal claim that the magnetosphere is what makes complex life possible. No accessible source states it. Two open peer-reviewed sources argue the other way. Griessmeier 2016, conclusions: for a planet with an Earth-like atmospheric pressure, weak or absent magnetospheric shielding has a non-critical effect on biological dose rates; the atmosphere is the decisive factor, and removing the magnetosphere raises the surface dose by about a factor of two. Gunell 2018, abstract: magnetisation is not a sufficient condition for protecting a planet from atmospheric loss, and the observed escape rates from Earth, Mars and Venus are similar. NASA's outreach page does say life "initially developed and continues to be sustained under the protection of this magnetic environment" -- a weaker claim, and outreach prose rather than a primary. If a life sentence is wanted, NASA's wording is the most that can be sourced; the sentence as written cannot. |
| 6 | CITATION | Shue et al. (1998), J. Geophys. Res. 103:17691, doi:10.1029/98JA01103 supports the magnetopause standoff | citation row | eq. 10 of the paper gives r0, the subsolar standoff, as a function of Bz and Dp | R_E | https://faculty.epss.ucla.edu/~ctrussell/russell_bib.html/papers/mpause_extreme/ OPEN; https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/98JA01103 WALLED for me (bot check; page is labelled "Free Access") | YES | YES | The paper is the right authority: section 4 fits r0 = (a1 + a2 tanh[a3(Bz + a4)]) Dp^(-1/a5) and reports the optimized coefficients in Table 1 with a fit scatter of 1.23 R_E; section 2.1 gives the validity range -18 nT < Bz < 15 nT and 0.5 nPa < Dp < 8.5 nPa; section 3 uses Dp = 2 nPa as an average value. All of that is in the UCLA text. The coefficient values themselves I read from Klingenstein et al. 2025 eq. 2 (row 1), because the UCLA page serves Table 1 as an image. Frame: r0 is measured from Earth's centre along the aberrated Sun-Earth line, so "on the Sun-facing side" matches. Whether 10.25 is the right number to print is row 1's job. |
| 7 | DISCOVERY | How far downstream has Earth's magnetotail actually been observed? | (none stated) | Coherent tail with neutral sheet: to 80 R_E (Explorer 33, 1966-67) and to 220 R_E (ISEE-3, 1983). Signatures only: 900-1050 R_E (Pioneer 7, 1966). | R_E, geocentric (Ness: 1 R_E = 6378.2 km; Pioneer 7 was 24-28 R_E above the ecliptic) | https://ntrs.nasa.gov/api/citations/19670023428/downloads/19670023428.pdf OPEN (Ness, Scearce and Cantarano, GSFC preprint X-612-67-183, April 1967); https://ntrs.nasa.gov/citations/19830066648 ABSTRACT (Slavin et al. 1983, Geophys. Res. Lett. 10); https://science.nasa.gov/heliophysics/focus-areas/magnetosphere-ionosphere/ OPEN | YES | UNSOURCED | The text asserts only "a long magnetotail", which is supported; it names no source. Your reading of Ness 1967, checked against the paper: (a) NOT a single crossing -- Pioneer 7 was in the expected tail region from September 26 to October 3, 1966, and tail-like fields appeared intermittently for minutes to hours as the solar wind's changing direction swept the tail over the spacecraft; (b) "probable" is in the title, confirmed; (c) the abstract says a coherent, well-ordered tail with imbedded neutral sheet does not appear to have been observed, BUT the conclusions say the abrupt field reversals "may indicate the presence of an imbedded neutral sheet" -- so the paper reports probable neutral-sheet signatures while denying a coherent tail, and suggests the tail breaks into intertwined filaments by several hundred R_E. The same preprint records Explorer 33 seeing the tail and neutral sheet well-defined out to 80 R_E. What I opened is the April 1967 GSFC preprint of the paper, same authors and title; the JGR 72:3769 pages themselves sit behind Wiley and I did not open them. Later campaign, opened: ISEE-3 (Slavin et al. 1983) -- the tail keeps much of its near-Earth structure out to 220 R_E, stops flaring by 100-120 R_E, and settles to a diameter of about 60 R_E (the NTRS abstract prints "-1200" where "-120" is meant). Named but NOT opened, so not sources here: Fairfield 1968, J. Geophys. Res. 73:6179 ("the geomagnetic tail at 1000 R_E"); Mariani and Ness 1969, J. Geophys. Res. 74:5633 (Pioneer 8 at 500 R_E); Walker, Villante and Lazarus 1975, J. Geophys. Res. 80:1238 (Pioneer 7 at about 1000 R_E; a search snippet of its abstract reports field-reversal regions and tail characteristics similar to near Earth). For the drawing: `earth_visualization_shells.py` line 765 sets `'tail_length': 100`, a drawing parameter inside the ISEE-3 coherent range; noted, not promoted. |

---

## Two things outside the table

**What changed against the earlier return, in one sentence each.**
Row 3 now carries APPROX rather than a clean YES: "solar radiation"
without "particle" claims protection from sunlight and UV, which the
magnetosphere does not give. Row 7 now has a second opened source
(ISEE-3, 220 R_E) alongside Ness, and separates the coherent-tail
distances from the signature-only distance, which is the distinction
the worksheet asked for.

**Precision on row 1 is a decision for Tony, not for this table.** The
arithmetic is exact and the citation is right; what the fit supports is
"about 10", with the 10.25 living in the store as the evaluated model
value. Whether the hover prints 10.25, 10.3 or 10 is a display choice
the provenance skill's "When the source gives a range" section already
governs.

---

Rechecked September 2026 with Anthropic's Claude Fable 5.1 (high
effort), for Tony Quintanilla's Paloma's Orrery.
