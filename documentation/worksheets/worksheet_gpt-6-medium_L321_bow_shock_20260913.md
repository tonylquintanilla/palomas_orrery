# Citation worksheet 2 of 3 -- RETURN
## Earth's bow shock

**Built on** `f1bceefd05eeee0cac38fd519dd207314acb2383` at
https://github.com/tonylquintanilla/palomas_orrery

Vocabulary: v2 (2026-08-13)

**Checker:** GPT 6 Medium, 2026-09-13. The return does not name the
model; Tony identified it when he supplied the response. Same session
as the worksheet 1 return.

**Rule files read at that SHA, as stated in the return:**

- `PROJECT_INSTRUCTIONS.md`, section "Fetched vs Recalled Convention"
  -- READ, earlier in that conversation.
- `skills/provenance-discipline/SKILL.md`, sections "The Access
  Standard" and "Worksheet Types" -- READ, same.

The return states that the sources below were opened on September 13,
2026.

---

## Transfer gap -- read this before citing any row

This return reached the project as pasted plain text rather than as a
file, and one required field did not survive the paste.

**Every URL is gone.** The worksheet asked for the URL actually opened
for each source. In the text that arrived, each address had collapsed
to a link chip carrying no address. Those positions are marked
`[url lost]` below. The source NAMES and the access words survived; the
addresses did not.

Until the addresses are restored, no row here may be used to clear a
citation. An access word with no URL is an assertion about a read, not
a record of one, which is the shape the Access Standard exists to
refuse. The rows are still readable as findings, and row 2's arithmetic
is checkable independently.

**One normalization, stated because it touches the checker's own
words.** The table is transcribed verbatim except that non-ASCII
characters were transliterated, per the project's encoding gate:
curly quotes to straight, em and en dashes to `--` and `-`, the
approximately-equal sign to `~`, the multiplication sign to `x`, the
section sign to `sec.`, subscripts and superscripts written inline
(`r0`, `P^(-1/6.6)`), accented names to their unaccented forms, and
en dashes in numeric ranges to `-`. Nothing else was altered, added
or reordered.

---

| # | Job | Claim | Code value | Your value | Source unit | Source (URL opened, access word) | Value correct? | Citation correct? | Notes |
|---|-----|-------|-----------|-----------|-------------|----------------------------------|----------------|-------------------|-------|
| 1 | CITATION | The bow shock is the boundary where the supersonic solar wind is first slowed by Earth's magnetic field | (no figure) | A shock ahead of the magnetopause where solar wind is substantially slowed, compressed and heated | Not applicable | Jelinek et al. (2012) [url lost] -- OPEN; Urbar et al. (2019) [url lost] -- OPEN; Farris and Russell (1994) [url lost] -- ABSTRACT | NO | PARTIAL | Jelinek sec. 1 supports a shock ahead of the magnetic obstacle, but not the complete wording. "First slowed" is too absolute: Urbar's abstract reports "a systematic deceleration of the solar wind protons with a decreasing distance to the bow shock." This occurs in the foreshock -- the disturbed region upstream of the shock. "By Earth's magnetic field" also compresses the mechanism misleadingly: Earth's magnetosphere supplies the obstacle, while collective electric and magnetic processes mediate the shock. Your Farris-Russell reading is consistent with its accessible abstract: it develops a standoff relation incorporating Mach number and obstacle size and curvature. Mach number compares flow speed with a relevant wave speed. It does not justify treating that relation as a prediction of the complete drawn surface. I read its abstract, not its full paper. |
| 2 | CITATION | It is typically located about 13.51 Earth radii upstream on the Sun-facing side | 13.51 R_E | 13.51173611 R_E for p = 2 nPa; approximately 13.5 R_E for display | R_E from Earth's centre; p in nPa; aberrated GSE coordinates | Jelinek et al. (2012), full paper [url lost] -- OPEN; authors' 2010 proceedings paper [url lost] -- OPEN; Ingale et al., author manuscript [url lost] -- OPEN; Lugaz et al. (2016) [url lost] -- OPEN | APPROX | DERIVED | Arithmetic passes: equation 14 gives 15.02 x 2^(-1/6.55) = 13.51173611, correctly rounded to 13.51. The 2 nPa input lies within the recommended 0.6-11 nPa range. This is a pressure-conditioned prediction, not a universal quiet-time distance; pressure alone does not establish quiet conditions. Four significant figures overstate physical precision in this visitor sentence. Print "about 13.5." I found no coefficient uncertainties accompanying the fitted relation. Figure 7 describes model-crossing differences, not uncertainty in the constants or a hard bound at 2 nPa. Its numeric image label was not readable through my retrieval; the authors' open 2010 paper explicitly confirms a bow-shock standard deviation of about 0.69 R_E, p. 160. Independently selected Ingale sec. 3.2.1 reproduces the equation, corroborating transcription rather than providing independent measurements. Lugaz supplies broader physical corroboration through its normal-condition range. |
| 3 | CITATION | Jelinek, Nemecek and Safrankova (2012), J. Geophys. Res. 117:A05208, doi:10.1029/2011JA017252 supports the bow shock standoff | citation row | Supports R_BS = 15.02 p^(-1/6.55) | R_E from Earth's centre; p in nPa | Jelinek et al. (2012) [url lost] -- OPEN | YES | YES | Section 4, equation 14, supplies this relation. Section 5.1 identifies distance "from the Earth center." The model axis uses aberrated GSE -- Earth-centred solar-ecliptic coordinates rotated to account for Earth's orbital motion. Its nose is therefore slightly displaced from the exact Sun-Earth line. The citation supports the standoff form; row 2 handles arithmetic and precision. |
| 4 | CITATION | Lugaz et al. (2016), Nat. Commun. 7:13001, doi:10.1038/ncomms13001 states that under normal solar wind the bow shock forms at a subsolar distance of 11 to 14 Earth radii | corroboration row | 11-14 R_E under normal solar-wind conditions | R_E, explicitly defined as 6,371 km; geocentric subsolar distance | Lugaz et al. (2016), full article [url lost] -- OPEN; Jelinek et al. (2012) [url lost] -- OPEN | YES | YES | The introduction explicitly states "Under normal solar wind conditions" and "a subsolar distance of 11-14 Earth radii." These are Earth-centred nose distances, not altitudes above the surface or separations from the magnetopause; no one-radius correction is appropriate. Lugaz does not specify an aberration correction for this broad introductory range. The agreement is meaningful as a broad consistency check: both concern the sunward bow-shock distance, and 13.51 lies within the range. It is not validation under identical conditions: Lugaz gives no matching 2 nPa selection, uncertainty distribution, or quiet-time sample definition. Its original investigation concerns unusual sub-Alfvenic conditions; the 11-14 range is introductory normal-condition context, not the measured result of that event. It should remain corroboration, not the source or uncertainty interval of the drawn value. |

---

Transcribed September 2026 with Anthropic's Claude Opus 5, from the
checker's response as supplied by Tony Quintanilla.
