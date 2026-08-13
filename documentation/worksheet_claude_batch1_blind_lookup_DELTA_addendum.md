# Blind Lookup DELTA -- Machine-Readable Addendum

**Built on `00219d9852c65d653ae49855d3138050dd8f76dd`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

**Checker:** Claude Opus 5
**Original worksheet:** `worksheet_claude_batch1_blind_lookup_DELTA.md`
(August 3, 2026, anchored at `0739e6b`)
**Addendum written:** August 13, 2026
**Purpose:** format only. No research was revisited. Every verdict below
restates a finding already in the original file.

---

## INDEPENDENCE DISCLAIMER -- carried forward verbatim in substance

This is the part of the original document that must survive the
reformatting, and it applies to every row of the table below.

**I was not a blind checker on this batch.** The prompt that produced
the original file said I was not told what value to expect. That was
true of the prompt but not of me: I had written one of the three
follow-up worksheets and then read the other two in full before
starting, so I already knew the disputed values and which paper each leg
had proposed for each one.

**Two Claude passes are one leg reported twice.** The original file was
written as a delta because a completed Claude blind-lookup worksheet for
the same prompt already existed, timestamped three minutes earlier and
anchored to a different HEAD. Where the two passes agree, that is one
model running twice -- shared training, shared reasoning habits, and in
practice the same abstracts. It is not a second opinion, and it must not
be counted as convergence.

**Consequence for the annotation.** One annotation in
`eris_visualization_shells.py` line 41 cites this document as a Claude
leg. Whether it qualifies as a completed leg is Tony's ruling, and this
disclaimer is the information he needs to make it. My own view, offered
as input and not as the decision: rows BL-2 and BL-5 below carry real
independent research, while the rows marked UNVERIFIED carry none, and
no row here is blind.

---

## Verdict table

| # | Claim in code | Code value | Your value | Source | Value correct? | Notes |
|---|---------------|-----------|-----------|--------|----------------|-------|
| BL-1 | Mercury sodium tail extent | 10,000 R_M (~24 million km) | ~1,400 R_M (~3.4 million km) maximum published | Baumgardner, Wilson & Mendillo 2008, GRL 35:L03201; Schmidt et al. 2010, Icarus 207:9 | NO | Baumgardner abstract states the tail extent as ~1.5 degrees, nearly 1400 Mercury radii. Schmidt states more than 1000 R_M, and records no tail beyond 120 R_M during the January 2008 MESSENGER flyby period. Code value is 7.1x the largest published figure. Potter & Morgan 1985 not opened; the tail literature consistently dates to Potter et al. 2002 and later, so it is very likely NOT ADDRESSED there, but I did not confirm that and do not report it as confirmed. Settles the GPT-Gemini conflict in GPT's favour. |
| BL-2 | Eris central temperature | 875 K, cited to Glein et al. 2024 | 875 K, from Nimmo & Brown 2023 | Nimmo, F. & Brown, M.E. 2023, Science Advances 9:eadi9201 | YES | Value confirmed, citation wrong. The paper states that the present-day chondritic heating rate is about 4.5e-12 W/kg, so the present-day central temperature of Eris should be about 875 K, taking k = 3 W/m/K and surface temperature Ts = 30 K. FOUR model inputs, not three: the heating rate is the one that sets the scale and both GPT and the earlier Claude pass omitted it. Authors are Nimmo and Brown; GPT hedged toward Szakats et al. 2023 (A&A 669:L3), which is the separate tidal-locking discovery paper that Nimmo & Brown cite as input. Use "central", not "core" -- the paper gives a centre temperature from a conductive profile. |
| BL-3 | Mercury interior dimensions (Margot 2012; Hauck 2013) | outer core 1074 km | -- | -- | UNVERIFIED | Not attempted. Neither paper opened. Two Claude passes have now declined this row; it should route to a checker who is not Claude. |
| BL-4 | Venus atmospheric structure (Bertaux 2007; Seiff 1985 VIRA) | mesosphere 60-100 km; thermosphere 100-200+ km; dayside ~300 K; cryosphere 90-120 km; ionosphere peak 120-140 km | -- | -- | UNVERIFIED | Not attempted. Neither source opened. Two Claude passes have now declined this row. |
| BL-5 | Lunar core temperatures | inner core 1600-1700 K; outer core 1300-1600 K | no temperature located in any Williams paper | Williams et al. LLR reviews (arXiv gr-qc/0411095, gr-qc/0412049); lunar thermal-evolution literature | UNVERIFIED | NOT FOUND, and probably not findable in that form. The Williams LLR work publishes core size, state, and dissipation -- a 1-sigma upper limit on core radius of 352 km (pure Fe) or 374 km (fluid Fe-FeS eutectic), about 20% of the lunar radius -- not temperature. Same category error as citing Weber et al. 2011. A thermal-evolution study I did reach states that present-day core temperature estimates vary by about 350-500 K across models, which cannot support a 100 K-wide citation presented as fact. Gemini's attribution to Williams et al. 2006 does not survive contact with what the Williams papers are about. |
| BL-5b | Lunar core dimensions (by-product of BL-5) | inner core 240 km; outer core 330 km | inner core 0-280 km; fluid outer core 200-380 km | GRAIL-era lunar core structure modelling; Williams et al. LLR constraints | YES | Both code values fall inside the published ranges. The geometry the shells render is sourceable even though the temperatures printed beside it are not -- worth knowing before anyone deletes the whole block. Not a BL item in the original prompt; surfaced while failing to resolve BL-5. |
| BL-6 | Pluto core temperature | ~1,000 K, present tense | abstract contains no temperature at all | Bierson, Nimmo & Stern 2020, Nature Geoscience 13:468 | NO | Abstract read in full from Nature and three mirrors. Its content is a cold-start versus hot-start comparison against New Horizons geology, concluding Pluto was relatively hot when it formed, producing ~0.5% linear strain over the last 3.5 Gyr. The quantitative constraint the paper is known for is a formation timescale -- under about 30,000 years -- not a temperature. Gemini supplied a quotation about internal temperatures above 1000 K; that sentence is not in the abstract, and its content misdescribes the paper's argument, which runs from surface tectonics rather than ocean survival. Ocean survival is Kamata et al. 2019, which Bierson cites. |
| BL-7 | Pluto surface temperature | ~40 K | 37 +/- 3 K | Gladstone et al. 2016, Science 351, read via a secondary source quoting it | PARTIAL | The value is genuinely half-right: 40 K sits at the top edge of the published error bar, so it is not wrong, but it is not the published central value either. Marked PARTIAL rather than UNVERIFIED because the finding is real; the limitation is that I read it in a source quoting Gladstone, not in the paper. Confirm against the paper before annotating. |
| BL-8 | Hill sphere mass convention for binaries | Pluto uses system mass (caption 5.99 Mkm) | system mass is the physically meaningful choice | Reasoning from orbital mechanics; NOT a source lookup | DERIVED | Murray & Dermott not reached, and no JPL SSD statement of convention found. Offered as reasoning, weight accordingly. At Pluto's Hill radius the Pluto-Charon separation is a few tenths of a percent of the distance involved, so the pair is gravitationally indistinguishable from a point mass at the barycentre; using Pluto alone describes a body that is not there. Because r_H scales as mass^(1/3): Pluto-Charon at ~12% companion fraction gives +3.9%, Eris-Dysnomia at ~8.4% gives +2.7%. For Pluto that is 5.756 Mkm against 5.981 Mkm, and the code's caption says 5.99, so the code already uses system mass. TRAP: a mass derived from a satellite's orbit is a system mass by construction, so a database value may already include the companion and adding it again double-counts. Check whether JPL SSD's Eris mass of 1.66e22 kg is Eris alone or the system before applying any correction. I did not resolve this. |

---

## Row count reconciliation

Nine rows for eight BL items. BL-5b is a by-product finding recorded in
the original file's section 4, given its own row because it carries a
different verdict from BL-5 and concerns different constants. If the
checker expects exactly eight rows, BL-5b is the one to drop or merge.

---

## Tony-action rollup

- **(decide)** Whether the `eris_visualization_shells.py` line 41
  annotation citing this document counts as a completed Claude leg,
  given the disclaimer above.
- **(do)** BL-3, BL-4, and BL-8 need a checker who is not Claude. Two
  Claude passes have declined all three.
- **(do)** Confirm BL-7 against Gladstone et al. 2016 directly before
  acting on it.

---

*Format-only addendum prepared August 13, 2026 by Claude Opus 5. The
original file remains the historical record and was not edited.*
