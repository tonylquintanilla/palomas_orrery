# Citation worksheet 1 of 3 -- RETURN
## Earth's magnetopause and magnetotail

**Built on** `f1bceefd05eeee0cac38fd519dd207314acb2383` at
https://github.com/tonylquintanilla/palomas_orrery

Vocabulary: v2 (2026-08-13)

**Checker:** GPT 6 Medium, 2026-09-13. The return does not name the
model; Tony identified it when he supplied the response.

**Rule files read at that SHA, as stated in the return:**

- `PROJECT_INSTRUCTIONS.md`, section "Fetched vs Recalled Convention"
  -- READ, directly at the pinned SHA.
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
refuse. The rows are still readable as findings, and the arithmetic in
rows 1 and 7 is checkable independently.

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
| 1 | CITATION | Earth's magnetosphere extends about 10.25 Earth radii on the Sun-facing side | 10.25 R_E | 10.25187297 R_E at the declared conditions | R_E from Earth's centre; Bz in nT; pressure in nPa | Shue et al., full paper [url lost] -- OPEN; equation 10 [url lost] -- OPEN; Kumar and Pulkkinen (2025) [url lost] -- OPEN | YES | DERIVED | Shue sec. 4, equation 10: r0 = [10.22 + 1.29 tanh(0.184(Bz + 8.14))]P^(-1/6.6). Substitution gives [10.22 + 1.29 tanh(0.184 x 8.14)] x 2^(-1/6.6) = 10.25187297, rounding correctly to 10.25. Independently selected primary research by Kumar and Pulkkinen reproduces this in sec. 2, equation 2, and compares the model with spacecraft observations. This verifies the calculation, not four-figure observational accuracy. Shue reports an overall model-observation standard deviation of 1.23 R_E. The visitor text omits the conditions that make this particular number applicable. |
| 2 | CITATION | It stretches into a long magnetotail on the night side | (no figure) | A long nightside magnetic tail | Not applicable | Shue et al. [url lost] -- OPEN; Fairfield (1968), original research [url lost] -- OPEN | YES | YES | Shue sec. 2.1 explicitly discusses "tail flaring" and an open nightside magnetopause; the qualitative geometry is supported. Fairfield's spacecraft measurements independently establish distant tail fields; its abstract describes "fields characteristic of the extended geomagnetic tail." However, the displayed source label explicitly limits its attribution to standoff, so the visitor-facing citation does not clearly attribute this separate claim. |
| 3 | CITATION | It protects Earth from solar radiation | (no figure) | Partial protection against charged solar particles | Not applicable | Shue et al. [url lost] -- OPEN; NASA/JPL explanation [url lost] -- OPEN | APPROX | UNSOURCED | Shue does not establish this radiation-protection claim. NASA's relevant wording is "harmful solar and cosmic particle radiation." Particle is essential: the magnetic field deflects charged particles, not sunlight or ultraviolet and X-ray photons generally. The statement needs that qualification. NASA is an accessible agency explanation, rather than a dedicated experimental radiation-shielding paper. |
| 4 | CITATION | It protects Earth from cosmic rays | (no figure) | Partial, energy-dependent shielding of cosmic-ray particles | Not applicable | Shue et al. [url lost] -- OPEN; Griessmeier et al. (2016), author full text [url lost] -- OPEN | YES | UNSOURCED | Shue does not address cosmic-ray shielding. Independently, Griessmeier et al. sec. 4.4 describes magnetic deflection "provided their energy is low enough." Protection is real but incomplete: sufficiently energetic particles penetrate, and the atmosphere supplies additional shielding. YES does not mean that all cosmic rays are excluded. |
| 5 | CITATION | ...making complex life possible | (no figure) | Necessity for complex life is not established | Not applicable | Shue et al. [url lost] -- OPEN; Griessmeier et al. (2016) [url lost] -- OPEN | NO | UNSOURCED | As stated, this turns a protective contribution into a necessary condition for complex life. Shue supplies no biological evidence. Griessmeier et al. sec. 4.4 finds that a sufficiently thick atmosphere protects against strong biological radiation from galactic cosmic rays "regardless of its magnetic field." That result does not settle every question about habitability, but it undermines the asserted necessity. NO identifies an unjustified categorical statement; it does not deny magnetic shielding's benefits. |
| 6 | CITATION | Shue et al. (1998), J. Geophys. Res. 103:17691, doi:10.1029/98JA01103 supports the magnetopause standoff | citation row | Supports a solar-wind-dependent subsolar standoff model | R_E | Shue et al., author-hosted full text [url lost] -- OPEN | YES | YES | The header identifies JGR 103, 17691-17700 (1998). Section 2.1 defines r0 as the "standoff distance at the subsolar point"; sec. 4 supplies the improved equation 10. "Subsolar" means directly toward the Sun. This clears the citation's relevance to standoff, independently of row 1's arithmetic. |
| 7 | DISCOVERY | How far downstream has Earth's magnetotail actually been observed? | (none stated) | Approximately 900-1,050 R_E: intermittent tail-field signatures; no established terminal length | Geocentric R_E; the original report defines 1 R_E = 6,378.2 km | Ness, Scearce and Cantarano (1967), NASA full-text report [url lost] -- OPEN; Fairfield (1968), NASA full-text follow-up [url lost] -- OPEN | YES | YES | The distance and "probable" reading are confirmed, with qualifications. Ness's abstract places Pioneer 7 at 900-1,050 R_E during September 26-October 3, 1966. This is the spacecraft's distance range, not an uncertainty interval for the tail's endpoint. Figure 1 uses Earth-centred solar-ecliptic coordinates. The range converts to approximately 5.74-6.70 million km. A magnetic-field instrument measured changes in strength and direction consistent with Earth-connected tail fields. The abstract says: "A coherent, well-ordered tail with imbedded neutral sheet does not appear to have been observed." However, the conclusions, report p. 9, discuss field reversals as possible neutral-sheet evidence. A neutral sheet separates oppositely directed tail fields. Thus, "no coherent tail demonstrated" is fair; "no neutral-sheet evidence" is too strong. One passage contained multiple brief intervals, not one isolated crossing. The later open source strengthens the interpretation: Fairfield compares Pioneer 7 with simultaneous Explorer 28 and 33 measurements, distinguishing tail-like fields from passing interplanetary fields. Its abstract identifies approximately ten intervals; pp. 13-14 discuss possible neutral-sheet crossings and a moving tail, while retaining filamentary structure as an alternative. This extends the evidence beyond a restatement, but does not demonstrate an uninterrupted coherent tail or a farther endpoint. The defensible classification is intermittent tail-field signatures at roughly 1,000 R_E. |

---

Transcribed September 2026 with Anthropic's Claude Opus 5, from the
checker's response as supplied by Tony Quintanilla.
