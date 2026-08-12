# Cross-Check Worksheet -- Batch 1 Tier 1 Sourcing (Claude's Leg)

**Built on `e902549ee9e34afb2842fcdcc926b43da06c562c`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

**Checker:** Claude Opus 5
**Date:** 2026-08-02
**Job:** value verification + source discovery for uncited Tier 1 claims

---

## Base reconciliation

The prompt anchors to `2ccf683`; live HEAD is `e902549`. I pulled
`eris_visualization_shells.py` and `venus_visualization_shells.py` at
both SHAs and diffed them: **byte-identical**. The claim text in the
prompt matches the files exactly. Building on `e902549`.

---

## Headline

**Eris is clean.** All three claims trace to a single sentence in the
Nature paper, and two of them match it word-for-word in substance. One
Eris citation covers the whole block.

**Venus is mostly clean with one real error and one split source.** The
composition figures are exact. The troposphere height is wrong. And the
pressure and temperature figures depend on *which* NASA page you call
the authority, because two of them disagree.

---

## Worksheet

| # | Claim in code | Code value | My value | My source | Match? |
|---|---------------|-----------|----------|-----------|--------|
| E1 | Upper limit on Eris surface pressure | ~1 nanobar | ~1 nanobar (1-sigma), for N2, Ar, or CH4 | Sicardy et al. 2011, *Nature* 478:493-496 | **YES** |
| E2 | Eris atmosphere vs Pluto's | ~10,000x thinner | ~10,000x more tenuous than Pluto's present atmosphere | Same paper, same sentence | **YES** |
| E3 | Temperature at aphelion | around -240 degC | Preferred model is an isothermal N2 atmosphere near **30 K** = **-243 degC** | Same paper (Supplementary model description) | **APPROX** |
| V1 | Surface pressure vs Earth | ~90x | **92 bars** (NSSDCA fact sheet); **~93x** (NASA Science, current page); ~95 bars at mean radius (Britannica) | NASA NSSDCA Venus Fact Sheet; NASA Science Venus Facts | **APPROX -- low** |
| V2 | CO2 fraction | ~96.5% | **96.5%** CO2 near surface, by volume | NASA NSSDCA Venus Fact Sheet | **YES** |
| V3 | N2 fraction | ~3.5% | **3.5%** N2 near surface, by volume | Same fact sheet | **YES** |
| V4 | Surface temperature | ~464 degC | **737 K = 464 degC** (NSSDCA); **467 degC** (NASA Science, current page) | Both NASA | **YES to NSSDCA** |
| V5 | Troposphere height | ~60 km | **~65 km**; mesosphere runs 65-120 km | Pioneer Venus-derived atmospheric structure; Britannica Venus atmosphere | **NO** |

---

## Eris -- all three claims, one citation

The Nature abstract carries E1 and E2 in a single sentence: no nitrogen,
argon, or methane atmosphere is detected above a surface pressure of
roughly 1 nanobar, which the authors describe as about ten thousand
times more tenuous than Pluto's atmosphere at that time.

That is as direct a hit as citation verification gets. The code's
phrasing is a close restatement of the paper's own comparison, which
means the claim and its source were never actually separated -- only the
`# Source:` line was missing.

**E3 needs a small decision.** The paper's preferred model assumes an
isothermal nitrogen atmosphere near 30 K, which is -243 degC. The code
says around -240 degC, or 33 K. Three kelvin warm.

This is not a measurement, so "wrong" is the wrong word for it. Eris's
surface temperature is modeled, not measured, and the number the paper
uses is a modeling assumption. But the code should not carry a rounder,
warmer figure than its own source while implying precision. Two honest
options: change to around -243 degC and cite the paper's model, or keep
-240 degC and say in the text that it is approximate.

One point worth knowing for E2's durability: Pluto's surface pressure
rose monotonically from 1988 to 2016 and sits near 10 microbar. Since
10 microbar is 10,000 nanobar, the ratio in the code survives the
increase. The comparison is stable, not date-sensitive in practice --
which is worth noting because the scanner flagged this block as
date-sensitive recalled.

**Citation to write:**

```
# Source: Sicardy et al. 2011, Nature 478:493-496 -- multi-chord
#         stellar occultation of 6 Nov 2010; 1 nbar upper limit,
#         ~10,000x more tenuous than Pluto's; 30 K isothermal N2 model
```

---

## Venus -- composition exact, two figures needing a decision, one wrong

### V2 and V3 are exact

The NASA NSSDCA Venus Fact Sheet gives atmospheric composition near the
surface by volume as 96.5% carbon dioxide and 3.5% nitrogen. Those are
the code's numbers, to the digit. Nothing to change.

### V1 and V4: which NASA page is the authority?

This is the interesting one, and it is a decision rather than a fix.

| Quantity | NSSDCA Venus Fact Sheet | NASA Science "Venus Facts" |
|----------|------------------------|---------------------------|
| Surface pressure | 92 bars | about 93x Earth's |
| Surface temperature | 737 K = **464 degC** | **467 degC** (872 degF) |

The code's 464 degC matches NSSDCA exactly. Its "about 90 times" matches
neither -- it is low against both, and low against Britannica's ~95 bars
at the elevation of the mean radius.

The spread is real, not sloppiness. Venus surface pressure varies with
surface elevation, so a single number is always a convention about which
datum you mean, and the two NASA pages made different roundings. 464 and
467 degC are 737 K and 740 K, the same physical claim reported from
different sources.

**Recommend:** pick NSSDCA as the authority for both, since it is the
fact sheet the rest of the file already cites, and change 90 to **92**
so the pressure and the temperature come from the same page. Citing one
page and using a number from neither is the state to avoid.

### V5 is wrong: the troposphere runs to ~65 km, not 60

The Venus temperature-height profile gives a troposphere from the
surface to about 65 km, holding roughly 99% of the atmosphere by mass,
with the mesosphere above it from 65 to 120 km and the thermosphere from
120 km out.

60 km is a real boundary on Venus, but it is roughly where the
continuous cloud deck tops out, not where the troposphere ends.

The code's own sentence shows the conflation. It says the troposphere
extends to approximately 60 km and that this region "contains the dense,
hot air and the main cloud layers" -- but the main cloud deck runs from
about 47-48 km up to about 70 km, so on the code's own numbers the
clouds stick out the top of its troposphere.

**Recommend:** 65 km.

**Citation to write:**

```
# Source: NASA NSSDCA Venus Fact Sheet (Williams, NASA GSFC) --
#         92 bars surface pressure, 737 K (464 degC), 96.5% CO2 /
#         3.5% N2 near surface by volume. Troposphere to ~65 km
#         (Pioneer Venus atmospheric structure); mesosphere 65-120 km.
```

---

## One structural note beyond the claims

The Venus text is duplicated verbatim at lines 328 and 345 -- once in
`venus_atmosphere_info` and once inside
`create_venus_atmosphere_shell()`. The prompt already notes they are
duplicates.

Whatever you change, it has to land in both, and a citation added to one
does not cover the other. That is the parallel-pipeline pattern in
miniature: two copies of one claim, and a fix to either one leaves the
other reading as though it were verified.

**Recommend** having the shell description reference
`venus_atmosphere_info` rather than restating it, so the claim exists
once and the citation attaches to one place. If that is more surgery
than this batch wants, then at minimum the `# Source:` comment goes
above both copies, and both get corrected together.

---

## Tony-action rollup

- **(do)** Add the Eris citation above the `layer_info` block in
  `create_eris_atmosphere_shell()`. E1 and E2 are verified as written.
- **(decide)** E3: change -240 degC to -243 degC and cite the paper's
  30 K model, or keep -240 degC with an explicit "approximate" in the
  display text.
- **(decide)** V1: change 90 to 92 (NSSDCA) or 93 (NASA Science), and
  pick one page as the authority for the block.
- **(do)** V4 needs no change if NSSDCA is the authority. If you prefer
  the current NASA Science page, it becomes 467 degC -- but then V1
  should be 93 for consistency.
- **(do)** V5: change 60 km to 65 km. This one is a straight correction,
  not a judgment call.
- **(decide)** Whether to de-duplicate the Venus atmosphere text now or
  correct both copies in place.
- **(do)** Compare against GPT's and Gemini's legs. E1 and E2 should
  converge cleanly since all three will find the same abstract; V5 is
  the row where divergence would be most informative, because 60 km is
  a plausible-looking wrong answer that a model working from memory
  could easily reproduce.

---

## Sources consulted live

- Sicardy, B. et al. 2011, "A Pluto-like radius and a high albedo for
  the dwarf planet Eris from an occultation", *Nature* 478:493-496
  (abstract and figure captions describing the 30 K isothermal model)
- Meza et al., Pluto lower atmosphere and pressure evolution from
  ground-based stellar occultations 1988-2016 (for the Pluto pressure
  baseline behind E2)
- Nature Astronomy 2026, atmosphere detection on (612533) 2002 XV93
  (quotes Pluto's average surface pressure as 10 microbar)
- NASA NSSDCA Venus Fact Sheet (Williams, NASA GSFC)
- NASA Science, "Venus: Facts" (current page)
- Britannica, Venus atmosphere (thermal structure and cloud deck)
- Pioneer Venus-derived Venus atmospheric structure tables
  (troposphere / mesosphere / thermosphere boundaries)

---

*Worksheet prepared August 2, 2026 by Claude Opus 5, independently of
the GPT and Gemini legs.*
