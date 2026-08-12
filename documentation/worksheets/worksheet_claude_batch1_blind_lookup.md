# Blind Source Lookup -- Batch 1 Final Resolution (Claude's Leg)

**Built on `31c266664cf0d2fbe0e8ffc02895c975bb717248`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

**Checker:** Claude Opus 5
**Date:** 2026-08-03
**Resolved:** 4 of 8 items reached the source. The other 4 are marked
NOT ATTEMPTED and are not to be read as passing.

Base note: the prompt anchors to `2ccf683`; live HEAD is `31c2666`.
This worksheet touches no repo files, so the drift does not affect the
results -- recorded for the log.

---

## Summary

| # | Topic | Reached the source? | Headline |
|---|-------|--------------------|----------|
| BL-1 | Mercury sodium tail | **Yes, 2 of 3 papers** | Max published extent is **~1,400 R_M**. |
| BL-2 | Eris central temperature | **Yes, exact sentence** | **875 K confirmed**, with all three inputs. |
| BL-5 | Lunar core temperatures | Partly | **NOT FOUND** in Williams. See below. |
| BL-6 | Pluto internal temperature | **Yes, full abstract** | Abstract contains **no temperature at all**. |
| BL-3 | Mercury interior dimensions | No | NOT ATTEMPTED |
| BL-4 | Venus atmospheric structure | No | NOT ATTEMPTED |
| BL-7 | Pluto surface temperature | Second-hand only | See caveat |
| BL-8 | Hill sphere binary convention | No | NOT ATTEMPTED; reasoning offered, not sourced |

---

## BL-1: Mercury sodium tail extent

| Paper | What it says | Resolution |
|-------|-------------|------------|
| **B. Baumgardner, Wilson & Mendillo 2008**, *GRL* 35, L03201 | The abstract reports a tail extending about 1.5 degrees on the sky, which the authors state is **nearly 1,400 Mercury radii**, driven by radiation pressure on sodium atoms sputtered from the surface over the preceding ~15 hours. | **~1,400 R_M** |
| **C. Schmidt, Wilson, Baumgardner & Mendillo**, *Icarus* | Observations from McDonald Observatory since May 2007 show a sodium tail stretching **more than 1,000 Mercury radii**, about a full degree of sky. The same abstract adds that **no tail was observed beyond 120 R_M** during the January 2008 MESSENGER flyby period, or at a similar orbital phase in July 2008. | **>1,000 R_M, highly variable** |
| **A. Potter & Morgan 1985**, *Science* 229, 651 | **Not directly reached.** Every secondary source I found treats it as the discovery paper for sodium in Mercury's *exosphere*; the tail literature is consistently dated to Potter et al. 2002 and later. Strongly indicated NOT ADDRESSED, but I did not open the 1985 abstract and will not report it as confirmed. | **Not verified** |

### What this settles

The code's 10,000 R_M has no support in either paper I reached. It is
**7.1 times** Baumgardner's figure, which is the largest directly imaged
extent in the literature. The derived "~24 million km" in the same block
inherits the error; 1,400 R_M is about 3.4 million km.

This resolves the sharpest divergence in the previous round in GPT's
favour. Gemini attributed ~10,000 R_M to these same two papers, and
neither states it.

**A worthwhile detail for the display text.** Schmidt's non-detection
beyond 120 R_M at two separate epochs is not a footnote -- it says the
tail's length varies by roughly an order of magnitude with Mercury's
orbital phase, because the effect is driven by radiation pressure that
depends on the planet's radial velocity relative to the Sun. A single
number misrepresents the phenomenon whichever number you pick. The
honest text gives the range and says what drives it.

**Citation discrepancy, minor.** The prompt lists paper C as
"Observations of Mercury's sodium tail", *Icarus* 207, 9-16. The paper I
found at that journal and volume is "Orbital effects on Mercury's
escaping sodium exosphere", by Schmidt, Wilson, Baumgardner and
Mendillo. Same authors and topic, different title. Worth reconciling
before the citation is written.

---

## BL-2: Eris internal temperature -- confirmed, with the sentence

I reached the paper body. It states that the present-day chondritic
heating rate is about 4.5 x 10^-12 W kg^-1, so **the present-day central
temperature of Eris should be about 875 K**, taking k = 3 W m^-1 K^-1
and a surface temperature of 30 K.

All three inputs GPT predicted are present and correct.

**The paper is Nimmo & Brown 2023**, *Science Advances* 9(46), eadi9201,
DOI 10.1126/sciadv.adi9201 -- Francis Nimmo (UC Santa Cruz) and Michael
E. Brown (Caltech). GPT hedged the authorship as "Szakats et al./Nimmo
and coauthors"; Szakats et al. 2023 (*A&A* 669, L3) is the separate
paper that discovered Eris's tidally locked rotation, which this one
cites.

**Two qualifications that belong in the code comment.**

The paper immediately adds that 875 K is about 500 K *below* the melting
temperature of rock, which is the point of the calculation -- it implies
a rock viscosity so high that dissipation in the core is negligible.
Quoting 875 K without that context inverts the paper's argument.

And it is a modeled present-day central temperature from a
conduction-only calculation, not a measurement. Later work
(a 2025 thermal-orbital evolution study) models peak central
temperatures near 1,300 K under different assumptions, so 875 K is one
model's output, not a settled figure.

**Recommended:** cite Nimmo & Brown 2023 with the three inputs recorded
in the comment, and describe it as modeled.

---

## BL-6: Pluto internal temperature -- the abstract has no temperature in it

I retrieved the full abstract of Bierson, Nimmo & Stern 2020, *Nature
Geoscience* 13, 468-472, verbatim from two independent sources
(Nature's own page and Semantic Scholar's record). They match each other
exactly.

The abstract argues that Pluto accreted relatively hot with an early
subsurface ocean, contrasting this with the conventional cold-start
picture, and states the observable consequence: a hot start produces an
early rapid extension phase followed by a prolonged one, totalling about
0.5% linear strain over the last 3.5 Gyr, which matches the extensional
faults New Horizons observed.

**It contains no temperature value of any kind.** Not 1000 K, not a
present core temperature, not a formation temperature. The press
coverage I found is consistent -- it emphasises formation in under
~30,000 years and the retention of gravitational energy, and quotes no
temperature either.

### On the quotation in the previous round

Gemini reported this item CONFIRMED and supplied what reads as a direct
quotation about a hot start "achieving internal temperatures >1000 K"
being required to explain the ocean's survival.

That sentence is not in the abstract. Its "We find that..." construction
is abstract phrasing, and the actual abstract opens differently and
makes a different argument -- about tectonics and strain, not
temperature.

I cannot rule out that some similar statement appears in the body, which
I did not reach. But I can state plainly that the quoted sentence is not
where a sentence of that form would be, and that the abstract's actual
content does not support a present-day core temperature.

**Recommended:** GPT's NOT FOUND stands. Remove the ~1,000 K core
temperature, or replace it with a claim the paper does make. And treat
the quotation itself as unverified -- this is a case where a checker
supplied evidence more specific than the source supports, which is
precisely the failure mode the competitive pattern exists to catch.

---

## BL-5: Lunar core temperatures -- NOT FOUND, with a likely origin

I could not find a Williams et al. 2006 paper stating lunar core
temperatures of 1600-1700 K.

What James G. Williams's lunar work actually constrains is **core size,
state, and dissipation**, not temperature. Lunar Laser Ranging analyses
give the moment of inertia, evidence that the core is fluid, core-mantle
boundary oblateness, and upper limits on core radius -- 352 km for a
pure iron core or 374 km for a fluid Fe-FeS eutectic (Williams et al.
2001). Temperature is not an LLR observable.

Laneuville et al. 2014 concerns core crystallization regime and thermal
conductivity (a 50 W m^-1 K^-1 core), not a stated core temperature.

**A likely origin for the number, offered as a lead rather than a
finding.** The experimental petrology literature uses **1600 K as a
lunar core-mantle boundary condition** -- a 2024 *GRL* study on Fe-S-P
transport properties states lunar CMB conditions as 5 GPa and 1600 K.
That is a real, published lunar temperature. But it describes the **top
of the core**, not the inner core, and it comes from high-pressure
experiments, not from Williams.

This matches the concern I raised in the reconciliation: Gemini's own
description placed 1600-1700 K "at the core-mantle boundary" while the
code assigns it to the inner core.

**Recommended:** both lunar core temperatures remain unsourced. If they
are kept, they need a thermal-model paper that states them, and the
labels need to match what that paper describes. A checker with journal
access should look at Zhai et al. 2024 (*GRL*) and the Laneuville
thermal-evolution series for a CMB temperature that can be cited
properly.

---

## BL-7: Pluto surface temperature -- second-hand only

I did not reach Gladstone et al. 2016 directly. In an earlier session I
found a peer-reviewed *Icarus* paper on Pluto and Triton atmospheres
that attributes to Gladstone et al. 2016 a surface pressure of ~10-12
microbar and a **surface temperature of 37 +/- 3 K**.

That is a citation of a citation. It is good evidence and I would expect
it to hold, but it is not the source speaking, and this worksheet is
explicitly about what the source says.

**Recorded as:** 37 +/- 3 K, second-hand. The code's ~40 K sits at the
top edge of that error bar.

---

## BL-8: Hill sphere convention for binaries -- NOT ATTEMPTED

I did not look up how JPL SSD, Murray & Dermott, or other standard
references treat the primary-versus-system-mass question, so I have no
sourced answer.

I can offer the physical reasoning, clearly labeled as reasoning:

The Hill radius comes from the circular restricted three-body problem,
where the relevant quantity is the mass of the body whose gravity
competes with the Sun's. For a satellite far outside the Pluto-Charon
pair, that competing mass is the pair's total, because at that distance
the pair acts as a single gravitating body. That argues for system mass
when the question is "do Nix, Hydra, Kerberos and Styx stay bound," and
it is consistent with what I reverse-engineered from the code earlier:
Pluto's 5.99 Mkm equals a perihelion Hill radius computed with the
Pluto-Charon system mass, which is 4% larger than Pluto alone gives.

**That reasoning is not a citation and should not become one.** For
Eris-Dysnomia the mass ratio is 0.084, so the system-mass choice moves
the Hill radius by under 3% -- smaller than the perihelion-versus-
semimajor swing this batch already found.

**Recommended:** route BL-8 to a checker who can open Murray & Dermott
section 3.12 or 4.x. Two conventions are in play across the project's
Hill spheres -- which distance, and which mass -- and both should be
stated in every comment. The distance choice is the larger effect.

---

## BL-3 and BL-4: NOT ATTEMPTED

**BL-3 (Mercury interior dimensions, Margot 2012 and Hauck 2013).** Not
reached this session. From the previous round, GPT and Gemini agree that
Hauck 2013 publishes a **core radius of 2020 +/- 30 km** and that
neither paper states a 1074 km outer-core thickness. That agreement is
worth something, but it is two checkers' reports, not the source.

**BL-4 (Venus atmospheric structure, Bertaux 2007 and Seiff 1985
VIRA).** Not reached. This item asks five separate questions across two
sources and is the largest single lookup in the batch; it deserves its
own session rather than the tail end of one.

---

## What this round adds to the ladder question

Three of the four items I reached ended with the source **not** saying
what a citation claimed:

- 10,000 R_M: the papers say 1,400 and >1,000.
- Lunar 1600-1700 K: Williams does not publish temperatures.
- Pluto ~1000 K: the abstract publishes no temperature.

The one that confirmed cleanly -- Eris 875 K -- confirmed because
someone had already named the right paper. The blind-lookup format
worked exactly where a prior round had done the identification work, and
returned NOT FOUND everywhere the identification was still a guess.

That is worth recording as a property of the method, not just a result:
**blind lookup verifies attributions; it does not discover them.** When
no leg has found the source, sending the same question to three more
legs mostly produces three more NOT FOUNDs. The productive move at that
point is to accept the gap and mark the claim unsourced.

Which brings back the annotation question. Seven claims in this batch
have now been searched by three independent checkers and not sourced.
That is a stronger, more expensive result than "uncited," and the ladder
has no way to record it. A claim that survived three independent
searches without a source is not V3 with a bad citation -- the citation
is actively misleading, and the honest rung is below V4 RECALLED,
because a recalled value at least does not claim otherwise.

---

## Tony-action rollup

**(do) -- resolved, act now**

1. **BL-1**: replace 10,000 R_M with the published range. Recommend
   giving both figures -- ~1,400 R_M maximum imaged (Baumgardner et al.
   2008) and non-detection beyond 120 R_M at some orbital phases
   (Schmidt et al.) -- since the variability is the physics. Fix the
   derived "~24 million km" in the same block.
2. **BL-2**: cite Nimmo & Brown 2023, *Sci. Adv.* 9, eadi9201, record
   the three model inputs, describe 875 K as modeled, and add that it
   sits ~500 K below rock's melting point, which is the paper's actual
   point.
3. **BL-6**: remove Pluto's ~1,000 K core temperature. The cited
   abstract contains no temperature.
4. **BL-5**: mark both lunar core temperatures unsourced pending a
   thermal-model citation.

**(decide)**

5. Whether BL-1's display text gives a range rather than a single
   number.
6. Whether the ladder gains a way to record "searched by N independent
   checkers, not found."

**(do) -- still open, needs a checker with source access**

7. **BL-3** Mercury interior dimensions -- confirm Hauck's 2020 +/- 30
   km directly.
8. **BL-4** Venus atmospheric structure -- five values, two sources, own
   session.
9. **BL-7** Gladstone et al. 2016 surface temperature, first-hand.
10. **BL-8** Murray & Dermott on the binary Hill sphere convention.

---

*Prepared August 3, 2026 by Claude Opus 5, independently of the GPT and
Gemini legs. Sources reached live: Baumgardner et al. 2008 (GRL 35,
L03201) via the AGU abstract; Schmidt et al. via the Icarus abstract;
Nimmo & Brown 2023 (Sci. Adv. 9, eadi9201) body text; Bierson et al.
2020 (Nat. Geosci. 13, 468) abstract via Nature and Semantic Scholar;
Williams LLR literature and Zhai et al. 2024 (GRL) for the lunar CMB
condition.*
