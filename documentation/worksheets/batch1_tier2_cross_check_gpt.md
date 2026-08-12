# Independent Cross-Check Worksheet — Batch 1 Tier 2

**Prompt commit:** `2ccf6839c4278f01db00fbe2101440ab267a90c2`  
**Cross-checker:** GPT-5.6 Thinking  
**Date:** August 2, 2026

## Method

This worksheet evaluates two distinct questions for every row: whether the code value agrees with authoritative evidence, and whether the named citation actually contains or supports that value at the stated precision. Mission-level citations are marked partial when a specific publication or dataset is needed. Hill-sphere values are treated as derivations from JPL orbital and mass inputs rather than as values directly published by JPL.

## Worksheet

| # | Claim | Code value | Cited source | Your value | Your source | Value correct? | Citation correct? | Notes |
|---|---|---|---|---|---|---|---|---|
| M1 | Moon inner core radius | ~240 km | Weber et al. 2011 | ~240 km | NASA Moon Facts; Weber et al. 2011 | YES | YES | Directly supported; NASA now repeats 240 km. |
| M2 | Moon inner core temperature | 1600–1700 K | Weber et al. 2011 | Not established in cited paper at that precision | Lunar interior thermal models vary | APPROX | NO | Weber et al. is a seismic-structure paper, not a direct temperature source. |
| M3 | Moon outer core radius | ~330 km | NASA Moon Fact Sheet; Weber et al. 2011 | ~330 km total fluid-core radius | Weber et al. 2011; NASA Moon Facts | YES | YES | NASA describes 240 km solid inner core plus ~90 km liquid shell. |
| M4 | Partially molten boundary-layer thickness | ~150 km | Weber et al. 2011 | ~150 km | Weber et al. 2011 | YES | YES | Supported as a low-velocity partially molten layer. |
| M5 | Moon outer-core temperature | 1300–1600 K | Weber et al. 2011 | Model-dependent; not directly given there | Thermal-evolution literature | APPROX | NO | Citation does not publish this range. |
| M6 | Deep moonquake depth range | 700–1200 km | NASA Moon Fact Sheet; Apollo seismic reports | Mostly 700–1000 km; some literature extends toward 1200 km | NASA MSFC Seismology; Apollo seismic literature | APPROX | PARTIAL | NASA MSFC explicitly gives 700–1000 km, not 700–1200. |
| M7 | Moon Hill-sphere radius | ~60,000 km | NASA SSD | ~61,500 km at mean Earth–Moon distance | Derived from Earth/Moon masses and mean separation | APPROX | UNSOURCED | JPL supplies inputs; it does not publish a single Moon Hill-sphere constant. |
| M8 | Moon Hill sphere in lunar radii | 34.53 R_Moon | Derived | 60,000/1737.4 = 34.53 | Arithmetic | YES | DERIVED | Correct from the code’s rounded 60,000 km premise; using ~61,500 km gives ~35.4 radii. |
| Er1 | Eris bulk density | ~2.5 g/cm³ | Sicardy et al. 2011 | 2.52 ± 0.05 g/cm³ | Sicardy et al. 2011 | YES | YES | Direct match by rounding. |
| Er2 | Eris rocky mass fraction | >85% | Sicardy et al. 2011 implied | Model-dependent; not established by density alone | Interior-composition modeling required | NO | UNSOURCED | Bulk density does not uniquely determine rock mass fraction without assumptions. |
| Er3 | Eris radius | 1163 km | Sicardy et al. 2011 | 1163 ± 6 km | Sicardy et al. 2011 | YES | YES | Direct match. |
| Er4 | Eris density | 2.52 g/cm³ | Sicardy et al. 2011 | 2.52 ± 0.05 g/cm³ | Sicardy et al. 2011 | YES | YES | Direct match. |
| Er5 | Eris core temperature model | 875 K | Glein et al. 2024 | 875 K model value appears plausible but model-specific | Glein et al. 2024 | APPROX | PARTIAL | Should be labeled as one modeled interior temperature, not a measured value. |
| Er6 | Eris geometric albedo | 0.96 | Sicardy et al. 2011 | 0.96 with uncertainty | Sicardy et al. 2011 | YES | YES | Directly supported. |
| Er7 | Eris average orbital distance | ~67.8 AU | NASA SSD | ~67.8 AU semimajor axis | JPL orbital elements | YES | YES | Correct as semimajor axis. |
| Er8 | Eris Hill sphere at average distance | ~9.4 Mkm (~0.06 AU) | Derived from NASA SSD | ~14.2 Mkm (~0.095 AU) | Standard Hill formula using a=67.78 AU and Eris mass | NO | DERIVED | 9.4 Mkm does not follow from average distance. |
| Er9 | Eris perihelion distance | ~38 AU | NASA SSD | ~37.9 AU | JPL orbital elements | YES | YES | Correct by rounding. |
| Er10 | Eris Hill sphere at perihelion | ~8.1 Mkm | Derived from NASA SSD | ~8.0 Mkm | Standard Hill formula | APPROX | DERIVED | Good rounded result. |
| Er11 | Dysnomia orbital distance | ~37,000 km | NASA SSD | ~37,000 km semimajor axis | JPL satellite elements | YES | YES | Supported approximately. |
| Me1 | Mercury outer-core thickness | 1074 km | Margot et al. 2012 | Not a uniquely measured shell thickness of 1074 km | Margot et al. 2012 and later interior models | NO | NO | The citation is commonly used for core size/state, but 1074 km as outer-core thickness is not cleanly supported. |
| Me2 | Mercury crustal thickness | ~35 km | Sori 2018 | ~35 km assumed/model average | Genova et al. 2019; Sori-related gravity modeling | APPROX | PARTIAL | 35 km is a model assumption/average, not a globally measured constant. |
| Me3 | Diamond layer from impacts on graphite | qualitative | Pei et al. 2024 | Hypothesized diamond formation under impact processing | Pei et al. 2024 | YES | YES | Should remain explicitly hypothetical. |
| Me4 | Mercury exosphere composition | O, Na, H, He, K | NASA Mercury Fact Sheet | These are major detected species | NASA Mercury facts/MESSENGER | YES | YES | Correct qualitative list. |
| Me5 | Mercury sodium tail extent | up to 10,000 R_M | Potter & Morgan 1985; MESSENGER | Not supported by Potter & Morgan 1985 at this scale | Modern sodium-tail observations | NO | NO | The cited 1985 discovery paper does not establish a 10,000-radius tail. |
| Me6 | Mercury sodium tail in km | ~24 million km | Derived | 24.4 million km if 10,000 radii | Arithmetic | YES | DERIVED | Arithmetic is correct, but premise Me5 is unsupported. |
| Me7 | Mercury magnetopause standoff | 1.45 R_M | Winslow et al. 2013 | 1.45 R_M average | Winslow et al. 2013 | YES | YES | Direct match. |
| Me8 | Mercury magnetotail radius at 3 R_M downstream | 2.7 R_M | Winslow et al. 2013 | ~2.7 R_M | Winslow et al. 2013 | YES | YES | Directly stated in abstract. |
| Me9 | Mercury bow-shock standoff | 1.96 R_M | Winslow et al. 2013 | 1.96 R_M average fit | Winslow et al. 2013 | YES | YES | Direct match. |
| Me10 | Mercury Hill-sphere code radius_fraction | not supplied in prompt | NASA SSD | ~94.8 R_M at semimajor axis; ~75.3 R_M at perihelion | Standard Hill formula from JPL inputs | — | UNSOURCED | Cannot compare to code because radius_fraction was omitted from prompt. |
| V6 | Venus core radius | ~3200 km | NASA Venus Fact Sheet | Poorly constrained; rough estimates near 3000–3500 km | Margot et al. 2021 and interior models | APPROX | NO | NASA fact pages do not establish a measured 3200 km core radius. |
| V7 | Venus sidereal rotation period | 243 days | NASA Venus Fact Sheet | 243.0226 days average | Margot et al. 2021; NASA | APPROX | YES | Correct rounding. |
| V8 | Venus mesosphere range | ~60–100 km | ESA Venus Express; Pioneer Venus | Approximately 65–100 km, convention-dependent | Venus atmospheric reviews | APPROX | PARTIAL | Mission-level citation is too vague. |
| V9 | Venus thermosphere range | ~100–200+ km | ESA Venus Express; Pioneer Venus | Begins around 100–120 km and extends upward | Venus upper-atmosphere literature | APPROX | PARTIAL | No sharp universal top at 200 km. |
| V10 | Venus dayside thermosphere temperature | ~300 K | ESA Venus Express | Strongly altitude/local-time dependent; ~300 K can occur | Venus Express upper-atmosphere studies | APPROX | PARTIAL | Not a single average thermospheric constant. |
| V11 | Venus nightside cryosphere altitude | 90–120 km | ESA Venus Express | Cold nightside region occurs roughly 90–120 km | Venus Express SPICAV/SOIR studies | YES | PARTIAL | Value defensible; citation needs a specific paper. |
| V12 | Venus ionosphere peak altitude | 120–140 km | ESA Venus Express | Typically ~140 km, variable | Pioneer Venus/Venus Express ionosphere studies | APPROX | PARTIAL | Range is reasonable but broad mission citation is vague. |
| V13 | Venus bow-shock dayside range | 1.3–1.7 R_V | ESA Venus Express | Typical subsolar values near 1.4–1.5 R_V, variable | Shan et al. 2015 and Venus Express studies | APPROX | PARTIAL | Broad range is defensible, source needs specificity. |
| V14 | Venus induced magnetopause | 1.05–1.1 R_V | Zhang et al. 2007 | Near 1.05–1.1 R_V for induced boundary | Zhang et al. 2007 | YES | YES | Reasonable representation of the induced boundary. |
| V15 | Venus magnetotail extent | 45–60 R_V | ESA Venus Express; Pioneer Venus | Observed to at least 60 R_V in newer flybys | Edberg et al. 2024/2025 | YES | NO | Value now supported by newer missions, not by the cited older mission pages as stated. |
| V16 | Venus bow-shock code standoff | 1.4 R_V | Shan et al. 2015 | ~1.36–1.46 R_V | Shan et al. 2015 | YES | YES | 1.4 is a good representative value. |
| V17 | Venus Hill-sphere radius | ~1.0 Mkm / ~167 R_V | NASA SSD; NASA fact sheet | ~1.00 Mkm / ~165 R_V | Standard Hill formula from JPL inputs | APPROX | UNSOURCED | JPL provides inputs, not this derived constant. |
| V18 | Code uses 166 R_V | 166 | Derived | ~165–166 R_V depending constants/rounding | Arithmetic from Hill radius and Venus radius | YES | DERIVED | 166 is reasonable; citation text saying 167 is just a rounding mismatch. |
| P1 | Pluto rocky-core diameter | ~1700 km | Stern et al. 2015; Bierson et al. 2020 | Interior models commonly use ~1700 km diameter | Pluto interior-model literature | APPROX | PARTIAL | Model-dependent, not directly measured by New Horizons. |
| P2 | Core diameter fraction | ~70% of Pluto diameter | Same | 1700/2376.6 ≈ 71.5% | Derived from modeled diameter and measured Pluto diameter | APPROX | DERIVED | Correct arithmetic if P1 is adopted. |
| P3 | Pluto core temperature | ~1000 K | Same | Model-dependent; not uniquely established | Thermal-evolution models | APPROX | NO | The cited papers do not establish a measured 1000 K constant. |
| P4 | Pluto subsurface-ocean thickness | 100–180 km | Stern et al. 2015; Bierson et al. 2020 | Model-dependent range; not uniquely constrained | Bierson et al. 2020 and later ocean models | APPROX | PARTIAL | Needs wording as a model range. |
| P5 | Pluto lithosphere thickness | 45 to several hundred km | Same | Highly model-dependent | Pluto tectonic/thermal models | APPROX | PARTIAL | Too broad to function as a measured constant. |
| P6 | Sputnik Planitia N2 ice fraction | >98% | Stern et al. 2015 | Sputnik is N2-dominated, but >98% is not established by Stern 2015 | New Horizons compositional mapping | NO | NO | Citation overstates quantitative purity. |
| P7 | Water-ice mountain height | 2–3 km | Stern et al. 2015 | 2–3 km | Stern et al. 2015/New Horizons reporting | YES | YES | Supported. |
| P8 | Sputnik Planitia surface age | <10 Myr | Stern et al. 2015 | Upper limit around 10 Myr from crater absence | Stern et al. 2015; McKinnon et al. | YES | YES | Supported as an upper-limit estimate. |
| P9 | Pluto pressure relative to Earth | 1/100,000 | Stern et al. 2015; Gladstone et al. 2016 | ~1 Pa vs 101,325 Pa ≈ 1/100,000 | New Horizons atmospheric measurements | APPROX | DERIVED | Ratio is derived; papers report pressure, not usually this exact phrasing. |
| P10 | Pluto haze extent | up to 200 km | Stern et al. 2015; Gladstone et al. 2016 | At least/up to >200 km | Gladstone et al. 2016; Cheng et al. 2017 | YES | YES | Supported. |
| P11 | Number of haze layers | 20+ | Same | About 20 distinct layers | NASA/New Horizons; Cheng et al. 2017 | APPROX | YES | ‘About 20’ is safer than a strict minimum of 20+. |
| P12 | Pluto exobase altitude | ~1700 km / ~1.43 R_Pluto | Gladstone et al. 2016 | ~1700 km altitude; 1.43 R is inconsistent if altitude is above surface | Gladstone et al. 2016 | NO | PARTIAL | 1700 km altitude corresponds to ~2.43 Pluto radii from center; 1.43 R is 1700 km center-distance. |
| P13 | Pluto surface temperature | ~40 K | Gladstone et al. 2016 | ~38–55 K depending location/model | Pluto atmospheric/climate studies | APPROX | PARTIAL | Reasonable rounded value. |
| P14 | Temperature at 30 km | ~110 K | Gladstone et al. 2016 | ~110 K near 20–40 km | Gladstone et al. 2016; later climate models | YES | YES | Supported approximately. |
| P15 | Pluto Hill sphere | ~5.99 Mkm (0.04 AU) | NASA SSD | ~7.95 Mkm at semimajor axis; ~5.98 Mkm at perihelion | Standard Hill formula from JPL inputs | NO | DERIVED | 5.99 Mkm is a perihelion value, not an average-distance value. |
| P16 | Pluto moon count | 5 | NASA SSD | 5 | NASA Pluto Moons | YES | YES | Charon, Styx, Nix, Kerberos, Hydra. |

## Highest-priority corrections

The most consequential numerical problems are the Eris and Pluto Hill-sphere descriptions. Using the standard Hill approximation with the cited JPL inputs, Eris is about 14.2 million km at its semimajor axis and about 8.0 million km at perihelion. The code's 8.1-million-km perihelion value is sound, but 9.4 million km is not the corresponding average-distance result.

For Pluto, approximately 5.99 million km is the perihelion Hill radius. At Pluto's semimajor axis, the result is about 7.95 million km. The existing citation therefore associates a correct perihelion-scale number with the wrong orbital condition.

Pluto's exobase wording also mixes altitude and center-distance. An exobase 1,700 km above the surface lies about 2.43 Pluto radii from the center. A center-distance of 1.43 Pluto radii is about 1,700 km from the center, or only about 510 km above the surface.

The Eris rocky mass fraction above 85%, Mercury's 1,074 km outer-core thickness, the 10,000-Mercury-radius sodium tail, the quantitative >98% nitrogen purity for Sputnik Planitia, and several interior temperatures are not adequately supported by their named citations.

## Provenance recommendations

For every Hill sphere, cite JPL for the mass and orbital elements, then label the displayed radius as `Derived:` with the exact formula and whether semimajor-axis, instantaneous-distance, or perihelion distance was used.

Replace broad citations such as “NASA MESSENGER Mission,” “ESA Venus Express,” and “NASA SSD” with a paper, table, dataset, or exact mission page whenever a numerical precision is claimed.

Label interior dimensions and temperatures as model-dependent where they are not directly observed. Keep artistic shell dimensions separate from scientific measurements.

## Overall result

A substantial fraction of the values are scientifically reasonable, but citation quality is uneven. The strongest fully verified blocks are the Sicardy Eris radius/density/albedo values, the Winslow Mercury magnetosphere parameters, the Venus rotation period, Pluto's 2–3 km mountains and young Sputnik surface, the Pluto haze observations, and the five-moon count.

The most common failure mode is not an obviously absurd number; it is a defensible or familiar number attached to a citation that does not publish that specific claim.
