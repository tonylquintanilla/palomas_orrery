# Citation worksheet 3 of 3 -- RETURN
## Earth's Van Allen belts

**Built on** `f1bceefd05eeee0cac38fd519dd207314acb2383` at
https://github.com/tonylquintanilla/palomas_orrery

Vocabulary: NOT STATED IN THE RETURN -- see the transfer gap below.

**Checker:** GPT 6 Medium, 2026-09-13. The return does not name the
model; Tony identified it when he supplied the response. Same session
as the worksheet 1 and 2 returns.

**Rule files read at that SHA, as stated in the return:**

- `PROJECT_INSTRUCTIONS.md`, section "Fetched vs Recalled Convention"
  -- READ, earlier in that conversation.
- `skills/provenance-discipline/SKILL.md`, sections "The Access
  Standard" and "Worksheet Types" -- READ, same.

---

## Transfer gap -- read this before citing any row

This return reached the project as pasted plain text rather than as a
file. Two things are missing, and until both are restored no row here
may be used to clear a citation.

**1. Every URL is gone.** The worksheet asked for the URL actually
opened for each source. In the text that arrived, each address had
collapsed to a link chip carrying no address. Those positions are
marked `[url lost]` below. The source NAMES and the access words
survived; the addresses did not. An access word with no URL is an
assertion about a read, not a record of one, which is the shape the
Access Standard exists to refuse.

This matters more on this worksheet than on the other two. Rows 3, 8
and 9 are the DISCOVERY rows, and this checker answered all three by
naming a source that states the figure -- Koskinen and Kilpua for the
inner belt span, Y. X. Li et al. (2023) for the outer belt span, and a
University of Minnesota mission page for the outer altitude pair.
Those three addresses are the most load-bearing in the round.

**2. The vocabulary line is absent.** Worksheets 1 and 2 from the same
checker and the same session both carry `Vocabulary: v2 (2026-08-13)`.
This one does not. The header above records that rather than supplying
it, because an absent line means pre-v2 to any tool that reads it, and
writing the line myself would assert something the checker did not say.
The verdict tokens used below are all v2 tokens in their v2 columns,
which is suggestive and is not the same as the checker stating it.

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
| 1 | CITATION | The inner belt holds mainly protons | (no figure) | High-energy proton dominance | -- | Baker et al. (2018) [url lost] -- OPEN; Li et al. (2015) [url lost] -- OPEN | APPROX | YES | Baker's abstract explicitly describes proton dominance. Independently, Li's measurements confirm strong energetic protons but also abundant lower-energy electrons. "Mainly protons" is a conventional description of the high-energy radiation, not a count of all particles regardless of energy. |
| 2 | CITATION | The inner belt is drawn at its flux peak, 1.5 Earth radii from Earth's centre | 1.5 R_E | Approximately 1.5 R_E; measured peaks depend on proton energy | Baker: geocentric R_E; Selesnick: L | Baker et al. (2018) [url lost] -- OPEN; Selesnick et al. (2014) [url lost] -- OPEN | APPROX | YES | Baker sec. 2 explicitly places the proton flux peak near geocentric r ~ 1.5 R_E: no frame mismatch in this citation. Flux means particles passing through a given area per unit time. Independent check: Selesnick sec. 5 reports peaks near L = 1.5 for 46 and 66 MeV protons, versus 1.6 for 26 MeV; MeV means million electron volts, a particle-energy unit. L labels a magnetic shell and equals geocentric distance in Earth radii only at the magnetic equator in a dipole approximation. |
| 3 | DISCOVERY | Does a source state an inner edge and an outer edge for the INNER belt? The text says "spans roughly 1.1 to 2 Earth radii" | 1.1 to 2 R_E | Approximately 1.1-2 R_E for inner electrons at the equator | Equatorial geocentric R_E | Koskinen and Kilpua, sec. 1.1 [url lost] -- OPEN | APPROX | PARTIAL | A source states these endpoints, but specifically for the inner electron belt at equatorial distances. It separately describes energetic protons over approximately 1.1-3 R_E. Thus it does not establish 1.1-2 R_E as the complete boundary of the proton-dominated belt described by your hover. No uncertainty or measurement threshold accompanies these schematic extents. |
| 4 | DISCOVERY | Does a source state the INNER belt's extent in altitude? The text says "about 1,000 km to 6,000 km above Earth's surface" | 1,000-6,000 km | 1,000-6,000 km stated; physical endpoints unverified | km altitude above Earth's surface | Maiti and Ramachandran (2023), preprint [url lost] -- OPEN | UNVERIFIED | YES | An accessible source states this exact altitude range: sec. 1, first sentence. However, this is introductory background in a modelling preprint, not a measurement establishing the edges. Its accompanying conversion to "(0.2-2) R_E" above the surface is inconsistent: 1,000-6,000 km corresponds to approximately 0.157-0.941 Earth radii above the surface. This establishes the statement's existence, but does not independently validate its physical boundaries. |
| 5 | CITATION | Baker et al. (2018), Space Sci. Rev. 214:17, doi:10.1007/s11214-017-0452-7 supports row 2 - the PEAK | citation row | Approximately 1.5 R_E proton peak | Geocentric R_E | Baker et al. (2018) [url lost] -- OPEN | YES | YES | sec. 2 explicitly identifies that approximate distance as where inner-zone proton fluxes peak. This supports the peak citation. |
| 6 | CITATION | The outer belt holds mainly electrons | (no figure) | High-energy electron dominance | -- | Baker et al. (2018) [url lost] -- OPEN; Li et al. (2025) [url lost] -- OPEN; Li et al. (2015) [url lost] -- OPEN | YES | YES | Baker's abstract explicitly identifies outer-zone electron dominance; Li (2025) describes the outer electron belt. Independently, Li (2015), sec. 1 and its particle measurements, supports this description of the energetic radiation population. |
| 7 | CITATION | The outer belt is drawn at its flux peak, 4.5 Earth radii from Earth's centre | 4.5 R_E | Broad maximum around L = 4-5 | L; independent source also gives equatorial R_E | Li et al. (2025) [url lost] -- OPEN; Baker et al. (2018) [url lost] -- OPEN; Li et al. (2015) [url lost] -- OPEN | APPROX | PARTIAL | Li (2025), sec. 1, says "most intense around L = 4 and 5"; it does not publish a universal peak of 4.5. Independently, Li (2015), sec. 1, gives greatest intensity between 4 and 5 equatorial R_E for electrons above 500 keV and explains that successive belts can have different centres. Thus 4.5 is a plausible representative drawing position, but calling it the measured peak overstates the evidence. Converting L to a drawing radius requires the equatorial geometry qualification. Baker's support is assessed separately in row 11. |
| 8 | DISCOVERY | Does a source state an inner edge and an outer edge for the OUTER belt? The text says "spans roughly 3 to 7 Earth radii" | 3 to 7 R_E | Approximately L = 3-7 | L | Y. X. Li et al. (2023), full paper [url lost] -- OPEN | APPROX | PARTIAL | Yes: sec. 1, p. 109, explicitly places the outer belt between 3 and 7 L shells, describing a general quiet-time model. It is a published extent, not an uncertainty interval or a measured fixed boundary. The numbers match, but the source's magnetic-shell coordinates do not establish spherical edges at those geocentric distances. In a dipole approximation they correspond to 3-7 R_E at the magnetic equator only. |
| 9 | DISCOVERY | Does a source state the OUTER belt's extent in altitude? The text says "about 13,000 km to 60,000 km above Earth's surface" | 13,000-60,000 km | Approximately 13,000-60,000 km altitude | km altitude | University of Minnesota, mission announcement (2012) [url lost] -- OPEN | APPROX | YES | Yes, explicitly. The paragraph beginning "The inner Van Allen Belt lies..." gives the outer interval in kilometres altitude. This is the participating university's public mission description, not a research measurement defining sharp edges. It supplies no uncertainty, energy threshold or latitude qualification, and immediately explains that the regions change size and shape. |
| 10 | CITATION | The outer belt moves with geomagnetic activity | (no figure) | Its occupied region and boundaries change during magnetic storms | L for measured boundary positions | Baker et al. (2018) [url lost] -- OPEN; Li et al. (2025) [url lost] -- OPEN; Shi et al. (2020) [url lost] -- OPEN | YES | YES | Baker sec. 3.2 describes storm-dependent peak positions; Li (2025), sec. 2, documents storm-associated redistribution. Independently, Shi's Van Allen Probes study follows changing outer-belt inner boundaries through storms, including a statistical sample of 37 events. "Moves" is reasonable shorthand for changing particle distributions and boundaries, rather than rigid motion of an unchanged ring. |
| 11 | CITATION | The outer belt string names BOTH J. Geophys. Res. Space Physics (2025), doi:10.1029/2024JA033504 AND Baker et al. (2018) for row 7 - the PEAK. Does each support it? | citation row | Li: approximately L = 4-5; Baker: no fixed 4.5 peak established | Li: L; Baker: L and L* in relevant figures | Li et al. (2025) [url lost] -- OPEN; Baker et al. (2018) [url lost] -- OPEN | NO | PARTIAL | Li: PARTIAL, because sec. 1 supports a broad 4-5 L region, with the frame qualification. Baker: UNSOURCED for the fixed 4.5 peak. Its Figure 12 concerns variable peak locations; Figure 30's L* = 4.5 is a selected analysis location, not identification of a universal peak. L* is a related magnetic-shell coordinate accounting for field geometry. The combined citation therefore only partly supports row 7; both papers do not establish the stated peak. |

---

Transcribed September 2026 with Anthropic's Claude Opus 5, from the
checker's response as supplied by Tony Quintanilla.
