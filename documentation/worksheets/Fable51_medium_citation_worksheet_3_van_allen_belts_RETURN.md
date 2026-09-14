# Citation worksheet 3 of 3 -- RETURN
## Earth's Van Allen belts

**Built on** `f1bceefd05eeee0cac38fd519dd207314acb2383` at
https://github.com/tonylquintanilla/palomas_orrery

Vocabulary: v2 (2026-08-13)

**Checker:** Anthropic's Claude Fable 5.1, working in Tony's Claude Project
(protocol and installed skills resident), 2026-09-13. Same session as
the worksheet 1 and 2 returns.

**Rule files read at that SHA:**

- `PROJECT_INSTRUCTIONS.md`, section "Fetched vs Recalled Convention"
  (lines 739-753 at f1bceefd) -- READ, earlier this session, from a
  shallow clone at the pinned SHA.
- `skills/provenance-discipline/SKILL.md`, sections "The Access
  Standard [CRITICAL]" (line 380) and "Worksheet Types" (line 756) --
  READ, same clone.

**Code value check.** `EARTH_VAN_ALLEN_INNER_RADII = 1.5` and
`EARTH_VAN_ALLEN_OUTER_RADII = 4.5` in `constants_new.py` at f1bceefd.
The span strings "1.1 to 2" and "3 to 7" are in the Note lines of those
two constants and in `earth_visualization_shells.py` line 892; the
altitude strings "1,000 km to 6,000 km" and "13,000 km to 60,000 km" are
at `earth_visualization_shells.py` lines 745 and 747. None of the four
extents is a constant; all four are typed prose.

**Both primaries opened in full.** Baker et al. (2018) is open access at
Springer and I read it. Li et al. (2025), doi:10.1029/2024JA033504, is
CC BY 4.0; Wiley bot-blocks my sandbox but the NSF Public Access
Repository serves the identical PDF, which I read in full. So every
citation row below is checked against the primary's own words, not a
snippet.

**The headline before the table.** The two peaks are sourced and
correct. None of the four extents is sourced in the text, and the
sources I opened do not state any of the four as written. Baker (2018)
does state extents -- and they are different numbers from all four.

---

| # | Job | Claim | Code value | Your value | Source unit | Source (URL opened, access word) | Value correct? | Citation correct? | Notes |
|---|-----|-------|-----------|-----------|-------------|----------------------------------|----------------|-------------------|-------|
| 1 | CITATION | The inner belt holds mainly protons | (no figure) | Yes -- "an inner zone dominated by high-energy protons" (abstract); "comprised dominantly of very energetic protons (ranging up to multiple GeV energies)" (sec. 2) | n/a | Baker et al. (2018), https://link.springer.com/article/10.1007/s11214-017-0452-7 (OPEN, full text). | YES | UNSOURCED | The claim is right and Baker states it plainly. UNSOURCED because the hover's only source label reads "Source (peak)", which scopes Baker to the 1.5 figure and leaves this sentence uncited. Fix is one word: "Source (peak, species)". One nuance for the panel, not a correction: Baker also says the inner zone holds "copious fluxes of low- and medium-energy electrons"; "mainly protons" is about the high-energy, hazardous population, which is the honest reading of "dominated". |
| 2 | CITATION | The inner belt is drawn at its flux peak, 1.5 Earth radii from Earth's centre | 1.5 R_E | 1.5 R_E, geocentric, for 10-100 MeV protons | geocentric r in R_E (Baker gives R_E = 6372 km) | Baker et al. (2018), OPEN, sec. 2: protons of ~10 to ~100 MeV "are quite stable in time near the geocentric radial distance of r ~ 1.5 R_E ... at which the inner zone proton fluxes peak". | YES | YES | Value, frame and species all match. Baker uses geocentric r here, not L, so the frame worry the worksheet raised does NOT apply to this row -- no PARTIAL needed. The peak is for the energetic-proton population; lower-energy electron profiles in the inner zone peak elsewhere and vary. |
| 3 | DISCOVERY | Does a source state an inner edge and an outer edge for the INNER belt? Text says "spans roughly 1.1 to 2 Earth radii" | 1.1 to 2 R_E | No source states 1.1 to 2. What the two primaries state: inner belt "extends from just above the dense atmosphere out to an equatorial altitude of about 10,000 km" (about 1.0 to 2.6 R_E geocentric at the equator); a proton "shoulder" at 1.7 <= r <= 2.5 R_E; slot region L ~2 to 3 (Baker). "The inner belt (L < 2) also contains protons" (Li). | altitude in km and geocentric r in R_E (Baker); L (Li) | Baker et al. (2018), OPEN, sec. 2 and 3.2. Li et al. (2025), https://par.nsf.gov/servlets/purl/10575739 (OPEN, full text; same PDF Wiley serves), sec. 1. | APPROX | UNSOURCED | UNSOURCED is the answer to the row's question: no accessible source I found states "1.1 to 2". The OUTER edge near 2 is well supported (Li's "L < 2"; Baker's slot beginning at L ~2 for electrons). The INNER edge of 1.1 R_E (about 640 km altitude) is not stated anywhere I opened; Baker says only "just above the dense atmosphere", and the belt dips to a few hundred km over the South Atlantic. Baker's own equatorial extent runs further out than 2 (to ~10,000 km altitude, ~2.6 R_E), because he counts the variable proton shoulder. So the text's span is a reasonable typed rounding, not a sourced pair. If you keep a span, "from just above the atmosphere to about 2 Earth radii" is what Baker and Li together support, and it can carry Baker as source. |
| 4 | DISCOVERY | Does a source state the INNER belt's extent in altitude? Text says "about 1,000 km to 6,000 km above Earth's surface" | 1,000-6,000 km | A source states it exactly, but it is a magazine article, and the same lead author's peer-reviewed review gives a different upper figure (about 10,000 km equatorial altitude). Other public-facing sources give 6,000-12,000 km (ESA). | altitude above the surface, km | Baker & Jaynes (2014), American Scientist 102(5):374, https://www.americanscientist.org/article/new-twists-in-earths-radiation-belts (SNIPPET; the page returns a browser check to my sandbox; the search snippet shows the sentence "The inner belt extends from an altitude of about 1,000 to 6,000 kilometers above Earth"). ESA Cluster page, https://sci.esa.int/web/cluster/-/52831-earth-plasmasphere-and-the-van-allen-belts (SNIPPET, states 6,000-12,000 km for the inner belt). Baker et al. (2018), OPEN, sec. 2 ("about 10,000 km"). | APPROX | UNSOURCED | The 1,000-6,000 km pair is a common popular-science statement and Baker himself wrote it in 2014, so "does a source state it" is YES -- but it is the weakest of the sources, popular rather than reviewed, and it disagrees with his 2018 review and with ESA's page. The panel attaches no source to it. Three public sources, three different pairs, is the tell that these are conventions rather than measurements: the inner belt has no sharp edges, and any altitude pair depends on which particle energy you count and where in latitude you look. Recommendation is in the closing section. |
| 5 | CITATION | Baker et al. (2018), Space Sci. Rev. 214:17, doi:10.1007/s11214-017-0452-7 supports row 2 -- the PEAK | citation row | Yes | geocentric r in R_E | Baker et al. (2018), OPEN, https://link.springer.com/article/10.1007/s11214-017-0452-7. Bibliographic details confirmed on the page: Space Science Reviews vol. 214, article 17, published 12 Dec 2017 (2018 volume), open access, authors Baker, Erickson, Fennell, Foster, Jaynes, Verronen. | YES | YES | The citation string is correct and the paper states the peak at geocentric r ~ 1.5 R_E for inner-zone protons. As instructed, Baker's extents are reported in row 3, not here. |
| 6 | CITATION | The outer belt holds mainly electrons | (no figure) | Yes -- "an outer zone dominated by high-energy electrons" (Baker abstract); "comprised of mildly to highly relativistic electrons (~100 keV to >= 10 MeV)" (Baker sec. 2); "the outer radiation belt ... consists of energetic electrons" (Li 2025 sec. 1, and Li et al. 2024 GRL). | n/a | Baker et al. (2018), OPEN. Li et al. (2025), OPEN via NSF PAR. | YES | UNSOURCED | Same shape as row 1: correct, stated by both primaries, but the hover's source label is scoped to the peak. Baker adds that multi-MeV protons "are not considered to be a regular feature in the outer zone", which is the honest sense of "mainly electrons". |
| 7 | CITATION | The outer belt is drawn at its flux peak, 4.5 Earth radii from Earth's centre | 4.5 R_E | Li (2025): the outer belt "is most intense around L = 4 and 5". Li et al. (2024): "centered near L = 4". Baker (2018) states no peak position for the outer belt, only its extent, and shows (fig. 12) that the peak L moves inward with storm strength. | L (dimensionless; equals geocentric R_E at the magnetic equator only) | Li et al. (2025), OPEN via NSF PAR, sec. 1. Li et al. (2024), GRL 51:e2023GL107521, https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2023GL107521 (SNIPPET; bot-blocked, the search snippet shows the introduction sentence). Baker et al. (2018), OPEN. | APPROX | DERIVED | 4.5 is the midpoint of Li's "L = 4 and 5"; no source publishes 4.5, so DERIVED, and the derivation is complete (input named, arithmetic trivial). APPROX rather than YES on two grounds. Frame: the sources say L, the text says Earth radii from centre; equal at the magnetic equator, which is where the torus is drawn, so the drawing is fine, but the text should say "at the equator" or say L. Physics: the outer belt has no fixed peak -- Baker's fig. 12 places the MeV-electron peak anywhere from L ~3 to ~5 depending on storm minimum Dst -- so "the flux peak" is a quiet-time typical value, and the hover should say so. |
| 8 | DISCOVERY | Does a source state an inner edge and an outer edge for the OUTER belt? Text says "spans roughly 3 to 7 Earth radii" | 3 to 7 R_E | No source states 3 to 7. Baker (2018) states two close pairs: "the outer zone is broad in spatial extent (from r ~ 3 R_E to r >= 6.5 R_E)" and, from SAMPEX, "typically extends from L ~ 3.0 to roughly L = 6.5", with the inner edge reaching L ~2.5 under strong driving. ESA's public page says 4 to 7 R_E. | geocentric r in R_E and L (Baker); R_E (ESA) | Baker et al. (2018), OPEN, sec. 2 and 3.4. ESA Cluster page (SNIPPET). | APPROX | UNSOURCED | The row's answer: a source does state edges, and they are 3 and about 6.5, not 3 and 7. Baker's ">= 6.5" leaves room for 7 on the outside, and geosynchronous orbit at 6.6 R_E sits inside the belt in every account, so "3 to 7" is a fair rounding -- but it is a rounding of a source the text does not cite. "About 3 to 6.5 Earth radii" can carry Baker (2018) as source directly, with no rounding at all. |
| 9 | DISCOVERY | Does a source state the OUTER belt's extent in altitude? Text says "about 13,000 km to 60,000 km above Earth's surface" | 13,000-60,000 km | A magazine article by the same lead author states it exactly. The peer-reviewed sources do not, and its upper figure is inconsistent with them: 60,000 km altitude is 10.4 R_E geocentric, beyond Baker's 6.5 and beyond the orrery's own 10.25 R_E dayside magnetopause. | altitude above the surface, km | Baker & Jaynes (2014), American Scientist (SNIPPET, as row 4; the snippet reads "the outer belt spans from about 13,000 to 60,000 kilometers"). ESA Cluster page (SNIPPET; 25,000-45,000 km). Baker et al. (2018), OPEN; sec. 1 gives the whole belt system as "a few hundred km to ~40,000 km above Earth's surface". | NO | UNSOURCED | The lower figure is fine: 13,000 km altitude is 3.04 R_E, matching Baker's r ~3. The upper figure is the problem. 60,000 km altitude places the outer edge outside the dayside magnetopause the orrery draws at 10.25 R_E, which is physically impossible for trapped particles on the day side, and Baker's own 2018 introduction caps the radiation belt region at about 40,000 km altitude (about 7.3 R_E). The 60,000 km figure recurs in popular summaries (several search hits) and appears to be a convention that travels without a measurement behind it. NO because the pair as written is not correct against the reviewed primary or against the orrery's own geometry, whatever a magazine sentence says. |
| 10 | CITATION | The outer belt moves with geomagnetic activity | (no figure) | Yes -- "highly variable on essentially all temporal scales and shows tremendous variability as well as significant variations in the outer belt spatial extent"; inner edge "shows considerable variability in spatial location", reaching L ~2.5 under strong solar wind forcing; MeV peak position tracks storm Dst (fig. 12) | n/a | Baker et al. (2018), OPEN, sec. 3.4. | YES | UNSOURCED | Correct and strongly stated by Baker, who also names the driver (solar wind speed, with V >= 500 km/s filling the belt and V <= 300 km/s nearly emptying it in 2008-09). Uncited in the hover for the same scoping reason as rows 1 and 6. |
| 11 | CITATION | The outer belt string names BOTH J. Geophys. Res. Space Physics (2025), doi:10.1029/2024JA033504 AND Baker et al. (2018) for row 7 -- the PEAK. Does each support it? | citation row | Li (2025): supports "most intense around L = 4 and 5" -- not 4.5, and in L. Baker (2018): does NOT state an outer-belt peak position; it states the extent (r ~3 to >= 6.5) and shows the peak moving with storms. | L (Li); geocentric r (Baker) | Li et al. (2025), OPEN via NSF PAR, sec. 1; bibliographic details confirmed on the PDF: JGR Space Physics 130, e2024JA033504, received 5 Nov 2024, accepted 9 Jan 2025, CC BY, authors Li, Xiang, Mei, O'Brien, Brennan, Zhao, Baker, Temerin. Baker et al. (2018), OPEN. | APPROX | PARTIAL | Split verdict, so PARTIAL for the pair. The 2025 paper is the right authority for the peak and supports it at the level of "L = 4 and 5" -- the 4.5 is ours (row 7, DERIVED). Two things the hover should know about that paper: its subject is two NEW, temporary storm belts at L ~2 and L ~2.5-3.5, and the sentence we rely on is one line of its introduction summarising the normal belts; and that sentence is about the ELECTRON belts, so it is correctly used for the outer belt here, but the same sentence's "inner belt centred near L = 1.5" is also an electron statement, which matters if it is ever cited for the proton peak (Baker is the right source for that, row 5). Baker (2018) does not support the outer PEAK at all and should be moved to the extent and the "moves with activity" sentence, where it is the best source available. Naming the 2025 paper only by journal and year, without authors, is also unusual; "Li et al. (2025)" is how everyone else cites it. |

---

## What Tony has to decide

1. The two altitude pairs (rows 4 and 9). They come from a 2014
   magazine article, not a paper, they disagree with Baker's 2018
   review, and the 60,000 km outer edge is outside the orrery's own
   magnetopause. Recommendation: drop both altitude pairs from the
   panel and state extents once, in one frame, sourced to Baker (2018).
2. The two radii spans (rows 3 and 8). Neither is stated as written.
   Baker supports "from just above the atmosphere to about 2 Earth
   radii" and "about 3 to 6.5 Earth radii"; print those with Baker as
   source, or keep the rounded spans and accept they are uncited.
3. Source labels (rows 1, 6, 10, 11). Widen "Source (peak)" so Baker
   covers species, extent and variability, and move Baker off the outer
   peak, which only Li et al. (2025) supports.

Rows 2 and 5 clear as they stand. Row 7 stands as DERIVED once the
hover says "at the equator" or "L".
