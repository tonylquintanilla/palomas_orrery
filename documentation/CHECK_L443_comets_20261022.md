<!-- Doc-Kind: hand | L-443 source check of 2026-10-22, a reader's results file saved word for word (non-ASCII letters written in ASCII). -->
# Source check: 12 comets (slice1.json, field "desc")

Repos pinned: orrery bfb6c474 (https://github.com/tonylquintanilla/palomas_orrery), gallery 0bb34344 (https://github.com/tonylquintanilla/tonyquintanilla.github.io).
All pages below were fetched live on 2026-10-22. Orbit figures (periods, perihelion dates and distances) were not checked, per the task.

Note on "Retrograde": none of the pages opened for Hyakutake, Ikeya-Seki or Lemmon prints the word "retrograde". Each prints an inclination above 90 degrees, and an inclination above 90 degrees is what "retrograde" means. Those three are marked "CONFIRMED (by inclination)" so the basis is visible. JPL's Small-Body Database API was also opened for each, as a second source for the inclination.

---

## Tempel 2 (10P/Tempel)

- "Discovered 1873 by Wilhelm Tempel"
  - Page: https://en.wikipedia.org/wiki/10P/Tempel -- title "10P/Tempel"
  - Quote: "It was discovered on 4 July 1873 by Wilhelm Tempel."
  - Verdict: CONFIRMED
- "Deep Space 1 flyby 2001"
  - Page: https://en.wikipedia.org/wiki/10P/Tempel -- title "10P/Tempel". The page does not mention Deep Space 1. The missions it names for 10P were proposed or cancelled: "The Jet Propulsion Laboratory proposed a flyby of the comet with a flight spare of Mariner 4." / "It was the original target of the Comet Rendezvous Asteroid Flyby (CRAF) mission" / "The program was cancelled in November 1979."
  - Page: https://en.wikipedia.org/wiki/Deep_Space_1 -- title "Deep Space 1". The 2001 target was 19P/Borrelly: "the flyby of Comet Borrelly was a great success and returned extremely detailed images of the comet's surface." Infobox closest approach: "22 September 2001, 22:29:33 UTC." The page does not mention Tempel or 10P.
  - Page: https://science.nasa.gov/solar-system/comets/19p-borrelly/ -- title "19P/Borrelly - NASA Science". Quote: "NASA's Deep Space 1 spacecraft encountered comet Borrelly on Sept. 22, 2001."
  - Verdict: DIFFERS. Deep Space 1 flew by 19P/Borrelly in 2001, not 10P/Tempel. No page opened states a Deep Space 1 flyby of 10P/Tempel. The sentence should come out.
- Link: https://en.wikipedia.org/wiki/10P/Tempel -- loads, specific to the body. NASA's comet hub (https://science.nasa.gov/solar-system/comets/) lists no 10P page (it has 9P/Tempel 1, a different comet). PASSES the rule.

## Schaumasse (24P)

- "Discovered 1911"
  - Page: https://en.wikipedia.org/wiki/24P/Schaumasse -- title "24P/Schaumasse"
  - Quote (infobox): "Discovery date: 1 December 1911"; also "Discovered by: Alexandre Schaumasse"
  - Verdict: CONFIRMED
- Link: https://en.wikipedia.org/wiki/24P/Schaumasse -- loads, specific. No NASA body page on the hub. PASSES.

## Howell (88P)

- "Discovered 1981 by Ellen Howell"
  - Page: https://en.wikipedia.org/wiki/88P/Howell -- title "88P/Howell"
  - Quote: "It was discovered on 29 August 1981 by Ellen Howell."
  - Verdict: CONFIRMED
- Link: https://en.wikipedia.org/wiki/88P/Howell -- loads, specific. No NASA body page on the hub. PASSES.

## Churyumov (67P/Churyumov-Gerasimenko)

- Rosetta "August 2014 through September 2016"
  - Page: https://science.nasa.gov/solar-system/comets/67p-churyumov-gerasimenko/ -- title "67P/Churyumov-Gerasimenko - NASA Science"
  - Quotes: Rosetta "rendezvoused with this comet in August 2014" (fragment of a longer sentence); "The mission ended with the spacecraft's controlled impact on the comet's surface on Sept. 30, 2016."
  - Verdict: CONFIRMED (agency page, mission event)
- Link: the NASA page above -- loads, specific. PASSES.

## Hale-Bopp (C/1995 O1)

- "Visible to the naked eye for a record 18 months"
  - Page: https://science.nasa.gov/solar-system/comets/c-1995-o1-hale-bopp/ -- title "C/1995 O1 (Hale-Bopp) - NASA Science"
  - Quote: "Due to its large size, this comet was visible to the naked eye for 18 months in 1996 and 1997." (18 months stated; the word "record" is not.)
  - Page: https://en.wikipedia.org/wiki/Comet_Hale%E2%80%93Bopp -- title "C/1995 O1 (Hale-Bopp) (Great Comet of 1997)"
  - Quotes: "Its massive nucleus size made it visible to the naked eye for a record 18 months." / "...it was visible to the naked eye for twice as long as the previous record-holder." The same article also gives 569 days, about 18.5 months (paraphrased by the fetch tool; not quoted exactly).
  - Verdict: CONFIRMED (the "record" from Wikipedia; the 18 months from both)
- Link: the NASA page above -- loads, specific. PASSES.

## Hyakutake (C/1996 B2)

- "Passed very close to Earth in 1996"
  - Page: https://nssdc.gsfc.nasa.gov/planetary/hyakutake.html -- title as printed "Comet Hyakatuke" (sic)
  - Quote: "Comet Hyakutake, also designated Comet C/1996 B2, approached within 0.1 AU of the Earth (about 15 million km) on March 25."
  - Page: https://en.wikipedia.org/wiki/Comet_Hyakutake -- title "C/1996 B2 (Hyakutake) (Great Comet of 1996)". Quote: "The closest approach occurred on 25 March at a distance of 0.1 AU (15 million km; 39 LD)."
  - Verdict: CONFIRMED
- "Retrograde"
  - NSSDC page above: "Orbital inclination: 124.924 deg."
  - Wikipedia page above, infobox: "Inclination: 124.922 deg"
  - JPL SBDB API https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=C/1996%20B2 -- "C/1996 B2 (Hyakutake)", i = 125 deg
  - Verdict: CONFIRMED (by inclination; no page prints the word "retrograde")
- Link: https://science.nasa.gov/mission/ulysses/ -- loads; title "Ulysses - NASA Science". It is the NASA/ESA Ulysses mission page (the solar-polar spacecraft, 1990-2009). Its only mention of the comet: "The spacecraft's May 1996 encounter with comet Hyakutake revealed comet tails are far longer than expected." Not about the comet. FAILS the rule.
  - Replacement (NASA, specific to the body): https://nssdc.gsfc.nasa.gov/planetary/hyakutake.html -- title as printed "Comet Hyakatuke" (opened). NASA's comet hub has no science.nasa.gov page for Hyakutake; this NSSDC fact page is NASA's comet-specific page.
  - Wikipedia alternative (opened): https://en.wikipedia.org/wiki/Comet_Hyakutake -- "C/1996 B2 (Hyakutake) (Great Comet of 1996)"

## Ikeya-Seki (C/1965 S1-A)

- "One of the brightest comets of the 20th century"
  - Page: https://en.wikipedia.org/wiki/Comet_Ikeya%E2%80%93Seki -- title "C/1965 S1 (Ikeya-Seki) (Great Comet of 1965)"
  - Quote: "It proved to be one of the brightest comets seen in the last thousand years"
  - The only page opened that states our wording is the current info link (Tony's own site, below), which is not an open source under rule 3.
  - Verdict: DIFFERS. Wikipedia makes the stronger claim ("last thousand years"), not "20th century". Our sentence is weaker than, and consistent with, the page, but no allowed page states it as we have it.
- "Retrograde"
  - Wikipedia page above, infobox: "Inclination: 141.864 deg (A) 141.861 deg (B)"
  - JPL SBDB API https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=C/1965%20S1-A -- "C/1965 S1-A (Ikeya-Seki)", i = 142 deg
  - Verdict: CONFIRMED (by inclination; no page prints the word "retrograde")
- Link: https://sites.google.com/view/tony-quintanilla/comets/ikeya-seki-1965 -- loads; title "Paloma's Orrery - Ikeya-Seki (1965)". It is a page on Tony Quintanilla's own Google Sites account (the Paloma's Orrery site), about the comet, with links to animated orbit plots. Not a NASA or Wikipedia page. FAILS the rule.
  - No NASA body page found: NASA's comet hub lists none, and a search for a science.nasa.gov Ikeya-Seki page returned only APOD "sungrazer" picture pages.
  - Replacement (Wikipedia, opened): https://en.wikipedia.org/wiki/Comet_Ikeya%E2%80%93Seki -- "C/1965 S1 (Ikeya-Seki) (Great Comet of 1965)"

## NEOWISE (C/2020 F3)

- No numbers to check. Two things noted from pages opened, not counted below: Wikipedia (https://en.wikipedia.org/wiki/C/2020_F3_(NEOWISE)) states "NEOWISE is known for being the brightest comet in the northern hemisphere since Comet Hale-Bopp in 1997." and "The orbital inclination of 129 degrees classifies it as a retrograde comet." JPL SBDB (https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=C/2020%20F3) gives i = 129 deg. Both agree with the description.
- Link: https://www.nasa.gov/missions/neowise/nasas-neowise-celebrates-10-years-plans-end-of-mission/ -- loads; title "NASA's NEOWISE Celebrates 10 Years, Plans End of Mission". It is about the NEOWISE space telescope mission; the comet appears only as one of the mission's discoveries ("The mission has also discovered 25 comets, including the long-period comet C/2020 F3 (NEOWISE)."). Not about the comet. FAILS the rule.
  - NASA option, specific to the comet (opened): https://www.nasa.gov/centers-and-facilities/jpl/comet-neowise-sizzles-as-it-slides-by-the-sun-providing-a-treat-for-observers/ -- title "Comet NEOWISE Sizzles as It Slides by the Sun, Providing a Treat for Observers". This is a 2020 JPL news article about the comet, not a NASA body page; NASA's comet hub has no NEOWISE body page. (Fetched at the old www.nasa.gov/feature/jpl/... address; the page gives the canonical address above.)
  - Wikipedia option (opened): https://en.wikipedia.org/wiki/C/2020_F3_(NEOWISE) -- the fetch reported no printed title line; the article's lead names it "C/2020 F3 (NEOWISE) or Comet NEOWISE".

## Lemmon (C/2025 A6)

- "In Fall 2025, Comet Lemmon is brightening and moving into morning northern skies"
  - Page: https://apod.nasa.gov/apod/ap250930.html -- title "APOD: 2025 September 30 - Comet Lemmon Brightens"
  - Quote: "Comet Lemmon is brightening and moving into morning northern skies."
  - Verdict: CONFIRMED, with the page's date attached: the statement is as of 30 September 2025. Note: Wikipedia (https://en.wikipedia.org/wiki/C/2025_A6_(Lemmon)) puts the comet in the morning sky in August and in the evening sky in October ("visible in the sunset sky with a solar elongation of 42 degrees"). The description reads as present tense about a past season.
- "Retrograde"
  - Page: https://en.wikipedia.org/wiki/C/2025_A6_(Lemmon) -- title "C/2025 A6 (Lemmon)"; infobox "Inclination: 143.66 deg"
  - JPL SBDB API https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=C/2025%20A6 -- "C/2025 A6 (Lemmon)", i = 144 deg
  - The APOD page does not mention the orbit.
  - Verdict: CONFIRMED (by inclination; no page prints the word "retrograde")
- Link: https://apod.nasa.gov/apod/ap250930.html -- loads; a NASA page about this comet (a dated picture page). No NASA body page on the hub. PASSES the rule as written. Wikipedia alternative opened: https://en.wikipedia.org/wiki/C/2025_A6_(Lemmon) -- "C/2025 A6 (Lemmon)".

## SWAN (C/2025 R2)

- "discovered on September 11, 2025"
  - Page: https://en.wikipedia.org/wiki/C/2025_R2_(SWAN) -- title "C/2025 R2 (SWAN)"
  - Quote: "...is a long-period comet discovered on 11 September 2025 by Vladimir Bezugly through SWAN imagery." (sentence begins "C/2025 R2 (SWAN), formerly known as SWAN25B,")
  - Verdict: CONFIRMED
- "a non-periodic comet"
  - Same page and sentence: "is a long-period comet". The page does not use "non-periodic".
  - Verdict: DIFFERS (page says "long-period comet")
- Link: https://en.wikipedia.org/wiki/C/2025_R2_(SWAN) -- loads, specific. No NASA body page on the hub. PASSES.

## MAPS (C/2026 A1)

- "Kreutz sungrazer comet discovered on 13 January 2026 from the AMACS1 Observatory in the Atacama Desert, Chile"
  - Page: https://en.wikipedia.org/wiki/C/2026_A1_(MAPS) -- title "C/2026 A1 (MAPS)"
  - Quote (first sentence, as returned in fragments): "C/2026 A1 (MAPS), formerly known by its temporary designation as 6AC4721, was a Kreutz sungrazer comet" ... "discovered on 13 January 2026" ... "from the AMACS1 Observatory in the Atacama Desert". Chile appears only in the infobox: "Discovery site: AMACS1, Chile (W94)".
  - Verdict: CONFIRMED. Note: the page uses the past tense ("was a Kreutz sungrazer comet").
- Link: https://en.wikipedia.org/wiki/C/2026_A1_(MAPS) -- loads, specific. No NASA body page on the hub. PASSES.

## Wierzchos (C/2024 E1)

- "CO2-driven Oort Cloud comet"
  - Page: https://en.wikipedia.org/wiki/C/2024_E1_(Wierzchos) -- the fetch reported no printed title line; the article's subject is "C/2024 E1 (Wierzchos)"
  - Quotes: "Cometary emission activity for C/2024 E1 has been driven by carbon dioxide (CO2)." / "C/2024 E1 (Wierzchos) is a hyperbolic Oort cloud comet, discovered on 3 March 2024 by Polish astronomer Kacper Wierzchos."
  - Verdict: CONFIRMED (Wikipedia). The current info link (APOD, below) states neither: it mentions dicarbon, not carbon dioxide ("The green hue of the coma comes from the breakdown of dicarbon molecules by sunlight."), and says "The hyperbolic orbit of this comet indicates that it will likely become an interstellar traveler."
- "Multiple dust tails post-perihelion"
  - Wikipedia page above: "In mid February the comet featured a thin ion tail 3 degrees long and three distinct dust tails spaning near 90 degrees." The same page gives perihelion as 20 January 2026, so mid-February is after perihelion.
  - APOD page below: the image "shows a 5-degree long ion tail as well as three shorter dust tails." (no mention of perihelion)
  - Verdict: CONFIRMED
- Link: https://apod.nasa.gov/apod/ap260217.html -- returns a 302 redirect to https://science.nasa.gov/image-article/apod-2026-february-17-tails-of-comet-wierzchos/ , which loads; title "APOD: 2026 February 17 - Tails of Comet Wierzchos - NASA Science". A NASA page about this comet (a dated picture page). No NASA body page on the hub. PASSES the rule as written; the stored address is a redirect, and the redirect target is the live address.

---

## Counts (17 claims)

- CONFIRMED: 14 (three of these, the "Retrograde" lines for Hyakutake, Ikeya-Seki and Lemmon, rest on a printed inclination above 90 degrees, not the word)
- DIFFERS: 3 (Tempel 2 Deep Space 1 flyby -- it was 19P/Borrelly; Ikeya-Seki "20th century" -- Wikipedia says "last thousand years"; SWAN "non-periodic" -- Wikipedia says "long-period")
- NOT FOUND: 0
- Links failing the one-link rule: Hyakutake (Ulysses mission page), Ikeya-Seki (Tony's Google Sites page), NEOWISE (NEOWISE mission page). Wierzchos passes but its stored address redirects.

Pages opened: en.wikipedia.org/wiki/10P/Tempel; en.wikipedia.org/wiki/Deep_Space_1; science.nasa.gov/solar-system/comets/19p-borrelly/; en.wikipedia.org/wiki/24P/Schaumasse; en.wikipedia.org/wiki/88P/Howell; science.nasa.gov/solar-system/comets/67p-churyumov-gerasimenko/; science.nasa.gov/solar-system/comets/c-1995-o1-hale-bopp/; en.wikipedia.org/wiki/Comet_Hale%E2%80%93Bopp; science.nasa.gov/mission/ulysses/; nssdc.gsfc.nasa.gov/planetary/hyakutake.html; en.wikipedia.org/wiki/Comet_Hyakutake; sites.google.com/view/tony-quintanilla/comets/ikeya-seki-1965; en.wikipedia.org/wiki/Comet_Ikeya%E2%80%93Seki; www.nasa.gov/missions/neowise/nasas-neowise-celebrates-10-years-plans-end-of-mission/; www.nasa.gov/feature/jpl/comet-neowise-sizzles-as-it-slides-by-the-sun-providing-a-treat-for-observers; en.wikipedia.org/wiki/C/2020_F3_(NEOWISE); apod.nasa.gov/apod/ap250930.html; en.wikipedia.org/wiki/C/2025_A6_(Lemmon); en.wikipedia.org/wiki/C/2025_R2_(SWAN); en.wikipedia.org/wiki/C/2026_A1_(MAPS); apod.nasa.gov/apod/ap260217.html (302) -> science.nasa.gov/image-article/apod-2026-february-17-tails-of-comet-wierzchos/; en.wikipedia.org/wiki/C/2024_E1_(Wierzchos); science.nasa.gov/solar-system/comets/ (hub, to check for body pages); ssd-api.jpl.nasa.gov/sbdb.api for C/1996 B2, C/1965 S1-A, C/2025 A6, C/2020 F3.
