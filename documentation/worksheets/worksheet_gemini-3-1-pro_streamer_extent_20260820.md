# Worksheet return -- streamer belt radial extent

**Built on `9b9743d300070a69aac11229b9392845edb3488a` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Recorded August 20, 2026 with Anthropic's Claude Opus 5.**

Model: Gemini 3.1 Pro. Batch: `streamer_extent`. Date: 2026-08-20.
Follow-up to `worksheet_gemini-3-1-pro_reconciliation_sources_20260820.md`,
whose group 2 failed to answer this question.

Row this bears on: `constants_new.py::STREAMER_BELT_RADII`, handle L-210.

---

## 1. Why there was a follow-up

The nine-source read of 2026-08-20 asked Golub & Pasachoff, "The Solar
Corona" (2010) for the radial extent of helmet streamers. It came back
with a cavity height near 1 R_sun, a loose 5-10 R_sun bound on coronal
structure generally, and a location given only as "Chapter 1 /
Introduction." It was the one return in nine with no figure, no
uncertainty and no findable position.

On that basis Tony ruled the citation removed and `STREAMER_BELT_RADII
= 6.0` recorded as an assumption with no verified source
(`patch_L210_4_streamer_belt_unsourced.py`). This worksheet is the
follow-up that found what the earlier read could not.

## 2. What Gemini returned -- first response

Reported that the answer depends on which part of the structure is
being measured, and that the two parts differ by roughly an order of
magnitude.

**The base and cusp, ~1.5 to 2.5 R_sun.** The dome of closed magnetic
loops. At the top, solar wind pressure overcomes the closed field and
forms a cusp that transitions to open field lines. Cited to Antiochos
(1998), ApJ, for the streamer belt reaching the source surface near 2.5
R_sun, where the cusp defines the base of the heliospheric current
sheet.

**The stalk or ray, tens of R_sun.** Above the cusp the oppositely
directed open field lines form a thin current sheet, which the solar
wind stretches outward. Reported as routinely tracked to 30 R_sun and
beyond in coronagraph data. The supporting reference given was "a 2026
arXiv paper on solar precursors to magnetic switchbacks," with no
authors and no title.

## 3. What Gemini returned -- second response

Two references, both with DOIs, in response to a request for work
specifically analysing SOHO/LASCO coronagraph data.

- Suess, S. T., & Nerney, S. (2004). Flow in streamer boundaries, and
  streamer stability. *Advances in Space Research*, 33, 668-675.
  DOI 10.1016/s0273-1177(03)00237-0
- Decraemer, B., Zhukov, A. N., & Van Doorsselaere, T. (2019).
  Three-dimensional Density Structure of a Solar Coronal Streamer
  Observed by SOHO/LASCO and STEREO/COR2 in Quadrature.
  *The Astrophysical Journal*, 883, 152. DOI 10.3847/1538-4357/ab3b58

## 4. Claude's independent verification

Tony's instruction: the source check is the verification. What follows
is what was actually retrieved, and what could not be.

**Suess & Nerney (2004) -- VERIFIED, and it answers the question.**
Publisher abstract retrieved. It states that streamers can extend to
many solar radii while the closed field regions, or helmets, "reach no
higher than 2-4 solar radii." It also makes a point the orrery's hover
text does not currently convey: the brightness boundary that defines a
streamer in white light separates two different FLOW REGIMES, rather
than separating static plasma from expanding solar wind. The paper is
real, the DOI resolves, the authors and volume match.

A companion Suess & Nerney abstract (NASA NTRS 20050207488, Solar Wind
11 / SOHO 16, 2005) is titled for flow in thin streamer boundaries,
streamer stalks and plumes BETWEEN 2 AND 10 SOLAR RADII -- a named band
for the stalk region, from the same authors.

**Decraemer et al. (2019) -- VERIFIED as a citation, but it does NOT
answer this question.** ApJ 883, 152 confirmed; DOI, authors and
affiliations all match; abstract retrieved via the arXiv preprint
(arXiv:1908.05034). The paper forward-models a streamer stalk as a
plasma slab centred on a current sheet, with electron density described
by separate radial, transverse and face-on profiles, fitted
simultaneously to SOHO and STEREO data in quadrature. It reports
density structure, not a radial boundary. Citable for what a stalk IS;
not citable for how far it reaches.

**Antiochos (1998) -- NOT VERIFIED.** Not retrieved. And a caution
that matters more than the retrieval: 2.5 R_sun is the conventional
PFSS *source surface*, a boundary chosen by the model rather than
measured. Citing it as a physical extent would repeat exactly the
DeForest error this row already made -- taking a number that plays one
role in a paper and using it for another. Do not cite it for an extent
without reading the paper.

**The switchback-precursor paper -- NOT CITABLE.** No authors, no
title, dated 2026 and past this model's knowledge. Nothing to check.

## 5. Verdict

| Claim | Status |
|---|---|
| Helmets reach no higher than 2-4 R_sun | VERIFIED -- Suess & Nerney 2004 |
| Streamers extend to many solar radii | VERIFIED -- same abstract |
| Streamer boundaries/stalks studied 2-10 R_sun | VERIFIED -- Suess & Nerney 2005 abstract title |
| Stalk is a plasma slab around a current sheet | VERIFIED -- Decraemer 2019 |
| Stalks tracked to 30 R_sun and beyond | NOT VERIFIED -- no citable source supplied |
| Cusp at ~2.5 R_sun | NOT VERIFIED -- and it is a model surface, not a measurement |

**Bearing on the row.** 6.0 R_sun sits ABOVE the 2-4 R_sun helmet
ceiling and INSIDE the 2-10 R_sun band named for streamer boundaries
and stalks. So it does not represent the helmet, and no source names it
as a boundary of anything.

**Tony's ruling, 2026-08-20.** Keep 6.0 as a visualization assumption.
Let the hover text explain the two-part reality and its ranges, with
references. The shell is a rough equivalent of the structure in any
case, and saying so is more honest than choosing one regime's number
and presenting it as the boundary.

That ruling also fixes a live error: the hover text currently states
that helmet streamers extend to 4-6 R_sun, at nine sites across
`solar_visualization_shells.py` and `spacecraft_encounters.py`. Suess &
Nerney contradicts it directly.
