# `constants_new.py` Citation Verification -- Addendum on 17 Unresolved Rows

**Built on `00219d9852c65d653ae49855d3138050dd8f76dd`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
HEAD verified fresh; it matches the anchor in the request exactly.**

**Checker:** Claude Opus 5
**Original worksheet:** `worksheet_claude_constants_new.md`
(August 2, 2026, anchored at `225071f`)
**Addendum written:** August 13, 2026

Every value below was checked against `constants_new.py` **as it stands
at HEAD**, not as the original worksheet records it. The file has moved
substantially: values corrected, citations rewritten, and `#
Cross-checked:` annotations now live.

---

## Finding first: two annotations credit me with checks I did not do

This is not one of the 17 rows, and it is the most important thing in
the document.

Twenty annotations in `constants_new.py` cite one of my worksheets as a
Claude leg. **Eighteen are legitimate.** Two are not:

| Constant | What my worksheet actually said | What the annotation asserts |
|----------|--------------------------------|----------------------------|
| `BENNU_RADIUS_KM` | **UNVERIFIED.** "Not checked. Flagging because published Bennu mean radii cluster near 0.245 km, so this one is worth confirming rather than assuming." | `# Cross-checked: Claude 2026-08-02 -- Nolan et al. (worksheet_claude_constants_new.md)` |
| `ARROKOTH_RADIUS_KM` | **NO**, for the *old* value: 9.95 does not follow from its own stated dimensions. I never examined Keane et al. 2022 or the replacement value 9.1. | `# Cross-checked: Claude 2026-08-02 -- ... (worksheet_claude_constants_new.md)` |

Both follow the same pattern, and it is a pattern rather than two
slips. In each case my worksheet correctly said *this is wrong*,
someone then corrected the value against a **new source I never
examined**, and the annotation credited my worksheet as having
cross-checked the replacement.

**A worksheet that says a value is wrong is not a worksheet that says
the replacement is right.** Those are different claims resting on
different evidence, and the annotation form currently cannot tell them
apart. This is the same structural gap I flagged after the three-way
reconciliation -- that `# Cross-checked:` can only express agreement --
showing up from the other direction.

Two mitigations, so this is not alarming out of proportion:

- Both replacement values are **arithmetically self-consistent with
  their own stated inputs**. Bennu: V = 0.062 km^3 gives an
  equivalent-sphere radius of 0.2455 km, and a mean diameter of 492 m
  gives 246 m. Arrokoth: V = 3166 km^3 gives 9.109 km. Both match the
  constants to three figures.
- Bennu's 0.246 also matches the ~0.245 cluster my original worksheet
  pointed at, so the correction went the direction I indicated.

The values look right. The provenance claim is what overstates.

**Tony-action (decide):** whether these two annotations are removed,
reattributed to whoever actually opened Nolan 2013 and Keane 2022, or
left with a note. The worksheet checker being built will open
`worksheet_claude_constants_new.md`, look for Bennu, and find
UNVERIFIED -- so this will surface mechanically on the first run. Better
to rule on it now than to have it arrive as a checker failure.

---

## Verdict table -- the 17 unresolved rows

Row numbers are carried from the original worksheet so the rows can be
matched back.

| # | Constant | Code value | Your value | Source | Value correct? | Citation correct? | Notes |
|---|----------|-----------|-----------|--------|----------------|-------------------|-------|
| B1 | `EARTH_EQUATORIAL_RADIUS_KM` | 6378.137 | 6378.137 (IERS); B3 publishes 6378.1 | IERS Conventions (McCarthy & Petit 2004; Petit & Luzum 2010), via IAU 2015 B3 / Prsa et al. 2016 | YES | YES | Was PARTIAL. Resolved by the file, not by new research: the code now carries the note "B3 rounds to 6378.1 km; full precision from IERS Conventions", which discloses exactly the gap I flagged. A citation that states its own precision limit is correct. No change needed. |
| B2 | `EARTH_POLAR_RADIUS_KM` | 6356.752 | 6356.752 (IERS); B3 publishes 6356.8 | IERS Conventions (Petit & Luzum 2010); IAU B3 rounds to 6356.8 km | YES | YES | Was PARTIAL. The source line has been rewritten to name IERS as the authority with B3 as the rounded standard, which is what I recommended. Resolved. |
| D1 | `CORE_AU` | 0.2 * SOLAR_RADIUS_AU | 0.2-0.25 R_sun is the conventional range; no measured boundary exists | Bahcall, Pinsonneault & Basu 2001, ApJ 555:990; Carroll & Ostlie 2017 Ch. 11 | DERIVED | UNVERIFIED | The code now declares this a visualization boundary at the low end of the conventional range, which implements my earlier finding: a standard solar model produces a continuous profile with no radius at which anything changes state, so "the core extends to 0.2 R_sun" is a description wrapped around that profile, not a model output. The reframing is the right fix. I still cannot open BPB 2001's radial-profile tables or Carroll & Ostlie Ch. 11 to confirm either supports 0.2 specifically. |
| D2 | `RADIATIVE_ZONE_AU` | 0.7 * SOLAR_RADIUS_AU | tachocline ~0.713 R_sun (helioseismic) | Christensen-Dalsgaard, Gough & Thompson 1991, ApJ 378:413 | DERIVED | UNVERIFIED | Materially improved since my original pass. The old citation said "Standard solar model", which named the wrong FIELD -- the tachocline is a helioseismology result, not an SSM output. The citation now names a specific helioseismology paper, which is the correct kind of source. I did not open CDGT 1991 and cannot confirm it publishes 0.713. |
| D3 | `CHROMOSPHERE_RADII` | 1.1 (was 1.5 at my anchor) | physical chromosphere ~2000 km above photosphere = ~1.003 R_sun | Carroll & Ostlie 2017, Ch. 11 | DERIVED | UNVERIFIED | Value changed since my anchor and the substance is now resolved by others: 1.1 is declared a DRAWN shell radius, with the physical extent split into `CHROMOSPHERE_PHYSICAL_KM = 2000` and `CHROMOSPHERE_PHYSICAL_RADII`. Two figures answering two questions, both labeled -- this is the honest form. Gemini is the leg that reached the book; I cannot open Carroll & Ostlie and my verdict on the citation is unchanged. |
| D4 | `INNER_CORONA_RADII` | 3 | -- | Golub & Pasachoff, "The Solar Corona" (2010) | UNVERIFIED | UNVERIFIED | No book access. Note the separate problem, unchanged since August 2: the citation gives no page or chapter, so it is unverifiable even by someone holding the book. If this row is routed to Gemini, ask for a page. |
| D5 | `OUTER_CORONA_RADII` | 50 | -- | "Various"; Mann et al. 2004, A&A 414:1127 | UNVERIFIED | UNVERIFIED | "Various" is not a source. The Mann reference is specific and checkable by anyone with journal access -- it is a paper, not a book, so this row does NOT need Gemini. Also the only constant in Group D carrying no `# Cross-checked:` annotation at all, so nothing has touched it in either pass. |
| D6 | `STREAMER_BELT_RADII` | 6.0 | helmet streamers 4-6 R_sun per the code's own note | Golub & Pasachoff 2010; DeForest, Howard & McComas 2014, ApJ 787:124 | UNVERIFIED | UNVERIFIED | The DeForest reference has changed since my anchor, from "DeForest et al. (2018)" to a specific 2014 ApJ paper with volume and page. That half is a journal article and is reachable without book access -- the most likely of the six D rows to close. The value takes the top of a stated 4-6 range, and the code now discloses that ("Visualization cutoff at upper end of 4-6 R_sun observed range"), which answers the concern I raised. |
| E4 | `INNER_LIMIT_OORT_CLOUD_AU` | 2000 | 1,000-5,000 AU across the literature; 2,000-20,000 AU is the standard inner-cloud subdivision | Duncan, Quinn & Tremaine 1987 (inner Hills cloud ~3x10^3 AU); Dones et al. 2004; Fernandez 1997 | APPROX | NO | Value is defensible: 2,000 AU is the low end of the commonly quoted inner-cloud range and appears in the standard "inner Oort cloud 2,000-20,000 AU" subdivision. The citation is not. **Oort (1950) placed the comet reservoir between 25,000 and 200,000 AU** -- his own inner boundary was an order of magnitude beyond 2,000, so citing him for a 2,000 AU inner edge is backwards. Hills (1981) argued the true inner boundary lies inward of 2x10^4 AU but the specific few-thousand figure traces to Duncan et al. 1987. Recommend recite. |
| E5 | `INNER_OORT_CLOUD_AU` | 20000 | 2x10^4 AU | Hills, J.G. 1981 | YES | YES | Clean confirmation, and the strongest result in this addendum. Hills 1981 found the critical semimajor axis a_c = 2x10^4 AU satisfying both the stellar-encounter rate and typical comet lifetime; the Hills cloud continues inward of that. Multiple independent reviews state the boundary as Hills 1981's, at exactly 20,000 AU. Value and citation both correct as written. |
| E6 | `OUTER_OORT_CLOUD_AU` | 100000 | literature range 50,000-200,000 AU | Oort 1950 (2x10^5 AU); Weissman 1996 (~5x10^4 AU) | APPROX | NO | The two cited sources bracket the code's value from opposite sides without either publishing it: Oort's outer limit was 200,000 AU, Weissman 1996 gives roughly 50,000 AU. 100,000 AU is the standard round figure between them and the code's note "~0.5 parsec" is arithmetically right (100,000 AU = 0.485 pc). But no cited source states it. Recommend either citing a source that does publish 10^5, or noting that the value is a midpoint of a disputed range. |
| G1 | `MERCURY_RADIUS_KM` | 2439.7 | 2439.7 | NASA NSSDCA Mercury Fact Sheet (Williams, NASA GSFC) | YES | YES | **Resolved -- this was the row that prompted the request.** I opened the cited fact sheet. It publishes volumetric mean radius **2439.7 km**, polar radius 2438.3 km, and ellipticity **0.0009** -- so both the value and the code's parenthetical "oblateness ~0.0009" are correct as written. The 0.3 km disagreement I flagged is real but is not an error: JPL SSD's 2439.4 km mean radius is a separate determination, and the code cites the source that publishes 2439.7. Worth knowing that NSSDCA has itself been updated -- older mirrors of the same fact sheet show polar radius 2439.7 and ellipticity 0.0000, i.e. a perfectly spherical Mercury. The current sheet is the one the code matches. |
| G3 | `MOON_RADIUS_KM` | 1737.4 | 1737.4 | NASA NSSDCA Moon Fact Sheet; IAU/LRO reference radius (Archinal et al. 2011) | YES | YES | Was UNVERIFIED here but I resolved it on August 2 in `worksheet_claude_constants_remaining.md` item 5. NSSDCA gives volumetric mean radius 1737.4 km and flattening 0.0012, so both the value and the code's oblateness parenthetical check out. It is also the IAU/LRO lunar reference radius used for USGS map scales, so it is a datum rather than only a fact-sheet number. JPL Horizons carries 1737.53 km, a 0.13 km spread far below anything the orrery renders. |
| G9 | `PLUTO_RADIUS_KM` | 1188.3 | 1188.3 +/- 1.6 | JPL SSD (attributed there to Archinal et al. 2018); code cites Nimmo et al. 2017 | YES | UNVERIFIED | Value confirmed independently via JPL SSD, which gives 1188.3 +/- 1.6 for both equatorial and mean radius. I did not open Nimmo et al. 2017, so I cannot confirm that specific paper publishes it. The citation is plausible -- New Horizons occultation is the right provenance for this number -- but plausible is not verified. |
| G10 | `BENNU_RADIUS_KM` | 0.246 (was 0.262 at my anchor) | 0.246 | Nolan et al. 2013 radar shape model; OSIRIS-REx OLA, per the code comment | YES | UNVERIFIED | Value changed since my anchor and the new value is right: it matches the ~0.245 km cluster my original worksheet pointed at, and it is self-consistent with both stated inputs (V = 0.062 km^3 gives 0.2455 km; mean diameter 492 m gives 246 m). I did not open Nolan et al. 2013 or the OLA results. **See the finding at the top of this document -- this row carries an annotation citing my worksheet, which marked it UNVERIFIED.** |
| G11 | `ERIS_RADIUS_KM` | 1163 | 1163 +/- 6 | Sicardy et al. 2011, Nature 478:493 | YES | YES | Was PARTIAL because the file cited two sources that disagreed -- Sicardy's 1163 alongside a section header naming JPL SSD, which publishes 1200 +/- 50 (Brown & Schaller 2007). The current file cites Sicardy only, which resolves the conflict. I confirmed the value and citation against the Nature paper during the Batch 1 Tier 2 pass. Separately: Nimmo & Brown 2023 (Sci. Adv. 9:eadi9201) is a better citation than Sicardy for any claim that Eris is differentiated with a rocky core, since Sicardy reports density only. |
| G13 | `MAKEMAKE_RADIUS_KM` | 715 | 714 +/- 7 (mean); 717 +/- 7 (equatorial) | JPL SSD, attributed there to Brown 2013 | APPROX | PARTIAL | The value sits inside the published error bar but is not the published mean, so it is genuinely half-right rather than unresolved. The citation names "Brown et al." with no year, paper, or journal, which is not locatable -- JPL SSD attributes its figure to Brown 2013. Recommend either 714 citing Brown 2013 via JPL SSD, or keeping 715 with the year added. **Also flagged:** `HAUMEA_RADIUS_KM` was corrected to 715 on August 2, so two different bodies now carry the identical constant value. Both are individually defensible, but identical values on unrelated constants are worth one deliberate look before they are trusted. |

---

## Verdict summary

| Verdict | Value correct? | Citation correct? |
|---------|---------------:|------------------:|
| YES | 8 | 6 |
| APPROX | 3 | -- |
| PARTIAL | -- | 1 |
| DERIVED | 3 | -- |
| NO | -- | 2 |
| UNVERIFIED | 3 | 8 |
| **Total** | **17** | **17** |

**Nine of the seventeen rows closed.** Six closed on new research or on
corrections the file has absorbed since my anchor (B1, B2, E5, G1, G3,
G11); three closed as APPROX or PARTIAL with a specific recommendation
(E4, E6, G13).

**Eight rows still carry UNVERIFIED on the citation.** Six are Group D.

---

## What is left, and who should get it

**Route to Gemini (book access required):** D1 Carroll & Ostlie Ch. 11,
D3 Carroll & Ostlie Ch. 11, D4 Golub & Pasachoff. Ask D4 for a page
number -- without one the citation is unverifiable even with the book
in hand.

**Route to anyone with journal access (no book needed):** D2
Christensen-Dalsgaard, Gough & Thompson 1991 ApJ 378:413; D5 Mann et
al. 2004 A&A 414:1127; D6 DeForest, Howard & McComas 2014 ApJ 787:124;
G9 Nimmo et al. 2017; G10 Nolan et al. 2013 and the OSIRIS-REx OLA
results. These five are the cheapest remaining wins and none of them
needs Gemini.

**Needs no checker, only a decision:** E4 and E6 recitations, G13's
value-or-year choice, and the two annotation attributions in the
finding above.

---

## Tony-action rollup

- **(decide)** The `BENNU_RADIUS_KM` and `ARROKOTH_RADIUS_KM`
  annotations, which credit my worksheet for checks it explicitly did
  not perform. This will surface as a checker failure on the first run
  if it is not ruled on first.
- **(do)** `E4`: recite the 2,000 AU inner limit to Duncan, Quinn &
  Tremaine 1987. Oort 1950 places his own inner boundary at 25,000 AU,
  so the current citation points the wrong way by an order of magnitude.
- **(do)** `E6`: neither Oort 1950 (2x10^5 AU) nor Weissman 1996
  (~5x10^4 AU) publishes 100,000 AU. Either recite or disclose it as a
  midpoint.
- **(decide)** `G13`: 714 citing Brown 2013, or 715 with a year added.
  And take one look at Haumea and Makemake both reading 715.
- **(do)** `G1`, `G3`, `B1`, `B2`, `E5`, `G11` need no further work.
  Value and citation both correct as they stand at HEAD.
- **(do)** Route D2, D5, D6, G9, G10 to a journal-access checker and
  D1, D3, D4 to Gemini, per the split above.

---

*Addendum prepared August 13, 2026 by Claude Opus 5. The original
worksheet was not edited; it remains the record of what was known on
August 2. Sources opened this session: NASA NSSDCA Mercury Fact Sheet;
Oort cloud structure literature (A&A 2021 Oort Cloud Ecology II; Duncan,
Quinn & Tremaine 1987 and Hills 1981 as quoted across five independent
reviews); `constants_new.py` at HEAD.*
