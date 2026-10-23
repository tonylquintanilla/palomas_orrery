<!-- Doc-Kind: hand | L-443 source check of 2026-10-22, a reader's results file saved word for word (non-ASCII letters written in ASCII). -->
# Source check: asteroids (22 bodies)

Descriptions read from slice1.json, which is pinned at orrery bfb6c474
(https://github.com/tonylquintanilla/palomas_orrery) and gallery 0bb34344
(https://github.com/tonylquintanilla/tonyquintanilla.github.io).
Every page cited below was fetched live on 2026-10-22. The quotes are the
fetch tool's extraction of each page. On the JPL API pages the tool gave
summaries of the data rows, not verbatim text.

A note on time scales: the JPL close-approach API (cad.api) gives its
times in TDB, not UTC. Its documentation (https://ssd-api.jpl.nasa.gov/doc/cad.html)
describes the `cd` field as "time of close-approach (formatted calendar
date/time, TDB)". In 2024, TDB was about 69 seconds ahead of UTC.

---

## Vesta
No numbers.
- LINK: the current link is https://dawn.jpl.nasa.gov/. It redirects (302) to https://science.nasa.gov/mission/dawn/, "Dawn - NASA Science", which is the hub page for the whole Dawn mission (Vesta and Ceres). FAILS the rule. Replacement, opened: https://science.nasa.gov/solar-system/asteroids/4-vesta/, "4 Vesta - NASA Science". It is about Vesta only.

## 16 Psyche
- "August 2029" (when the Psyche mission reaches the asteroid). **CONFIRMED for the date. The wording needs care.**
  - https://science.nasa.gov/solar-system/asteroids/16-psyche/, "Asteroid Psyche": "Psyche begins its prime mission at the asteroid in August 2029."
  - https://science.nasa.gov/mission/psyche/, "Psyche": "Psyche will begin its prime mission in August 2029." The same page also says the spacecraft "is on its way to begin exploring asteroid Psyche by August 2029."
  - The current link, https://news.arizona.edu/news/large-craters-offer-clues-origin-asteroid-16-psyche ("Large craters offer clues to the origin of asteroid 16 Psyche | University of Arizona News"), gives only the year: "NASA's Psyche mission will arrive in 2029 to determine its origin."
  - Caveat: NASA dates the start of the prime mission ("by August 2029"), not an arrival. Our sentence says the mission "will reach the asteroid in August 2029". A wording that stays within NASA's statement is "begins its prime mission at the asteroid in August 2029".
- LINK: the current link is the University of Arizona news story. It loads, but it is a university news story, not a NASA page. FAILS the rule. Replacement, opened: https://science.nasa.gov/solar-system/asteroids/16-psyche/, "Asteroid Psyche".

## Lutetia
No numbers.
- LINK: https://www.nasa.gov/image-article/asteroid-lutetia/, "Asteroid Lutetia - NASA". It loads and is specific to Lutetia. PASSES, but it is thin: the page holds one image and the caption "Asteroid Lutetia at closest approach by the Rosetta spacecraft." I found no science.nasa.gov page for Lutetia: /asteroids/21-lutetia/ and /asteroids/lutetia/ both returned client errors, and NASA's asteroid index page does not list Lutetia.

## Steins
No numbers.
- LINK: the current link is https://www.esa.int/Science_Exploration/Space_Science/Rosetta, "ESA - Rosetta". It is the general Rosetta mission page, where Steins appears only as one date in the mission timeline. FAILS the rule. There is no NASA page for Steins: science.nasa.gov/solar-system/asteroids/2867-steins/ returned a client error, and NASA's asteroid index does not list Steins. Replacement, opened: https://en.wikipedia.org/wiki/2867_%C5%A0teins, "2867 Steins".

## Donaldjohanson
- "Apr 20, 2025" (the Lucy flyby). **CONFIRMED.**
  - https://science.nasa.gov/solar-system/asteroids/donaldjohanson/, "Asteroid Donaldjohanson": "obtained a close look at Donaldjohanson as flew by on April 20, 2025, on its way to explore the Jupiter Trojan asteroids."
  - https://science.nasa.gov/mission/lucy/, "Lucy - NASA Science", lists Donaldjohanson as "April 20, 2025" (Eastern Time).
  - https://lucy.swri.edu/Donaldjohanson.html, "(52246) Donaldjohanson": "April 20, 2025".
  - https://en.wikipedia.org/wiki/52246_Donaldjohanson, "52246 Donaldjohanson": "Lucy made its closest approach to Donaldjohanson on 20 April 2025 17:51 UTC."
- "D~4 km". **DIFFERS.**
  - NASA (the page above): "about 5 miles (8 km) long and 2 miles (3.5 km) wide at the widest point." NASA calls this a preliminary estimate.
  - SwRI (the page above): "approx. 5 x 2 miles (8 x 3.5 km)".
  - Wikipedia (the page above), citing Marchi et al. (2026), Science: "The asteroid has overall dimensions of 8.8 km x 4.4 km x 3.1 km."
  - A single diameter of about 4 km is not stated on any of these pages. The body is elongated: about 8 to 9 km long and 3 to 4 km wide.
- "C-type". **CONFIRMED.**
  - SwRI (the page above): "Type: C-type". The page names no source.
  - Wikipedia (the page above): "Donaldjohanson is classified as a C-type asteroid." It cites Marchi et al. (2026), Science, which is a source-naming page.
  - The NASA page does not give a type.
- LINK: https://science.nasa.gov/solar-system/asteroids/donaldjohanson/, "Asteroid Donaldjohanson". It loads and is specific to the body. PASSES.

## Dinkinesh
No numbers.
- LINK: https://science.nasa.gov/solar-system/asteroids/dinkinesh/, "Dinkinesh - NASA Science". It loads and is specific to the body. PASSES.

## Eros
- "in 2000-2001" (NEAR Shoemaker orbited it, then landed). **CONFIRMED.**
  - https://science.nasa.gov/solar-system/asteroids/433-eros/, "433 Eros - NASA Science": NEAR "moved into orbit around Eros on Valentine's Day", "Feb. 14, 2000", and "carried out humanity's first asteroid landing on Feb. 12, 2001."
- "first asteroid to be orbited and landed on". **CONFIRMED.**
  - The same page: "Eros is famous as the first asteroid to be orbited by a spacecraft, and the first asteroid to have a spacecraft land on it."
- LINK: https://science.nasa.gov/solar-system/asteroids/433-eros/, "433 Eros - NASA Science". It loads and is specific to the body. PASSES.

## Bennu
No numbers.
- LINK: https://science.nasa.gov/solar-system/asteroids/101955-bennu/, "Bennu - NASA Science". It loads and is specific to the body. PASSES.

## Ryugu
- "in 2020" (Hayabusa2 returned samples). **CONFIRMED.** (The "2" in Hayabusa2 is part of a name, not a number.)
  - https://en.wikipedia.org/wiki/162173_Ryugu, "162173 Ryugu": "returned the sample capsule to Earth on 5 December 2020." Also: "On 6 December 2020 (Australian time), a capsule containing the samples landed in Australia and after a brief search was retrieved."
- LINK: https://en.wikipedia.org/wiki/162173_Ryugu, "162173 Ryugu". It loads. I found no NASA page for Ryugu: science.nasa.gov/solar-system/asteroids/162173-ryugu/ and /ryugu/ both returned client errors, and NASA's asteroid index does not list Ryugu. PASSES, since Wikipedia is the fallback.

## Itokawa
- "in 2010" (Hayabusa returned samples). **CONFIRMED.**
  - https://science.nasa.gov/solar-system/asteroids/25143-itokawa/, "25143 Itokawa - NASA Science": "It delivered the sample to Earth on 13 June 2010."
  - https://en.wikipedia.org/wiki/25143_Itokawa, "25143 Itokawa": "The sample capsule was returned to Earth and landed at Woomera, South Australia on 13 June 2010".
- "first asteroid from which samples were returned". **CONFIRMED on the NASA page.**
  - NASA (the page above): "In 2005, 25143 Itokawa became the first asteroid from which samples were captured and brought to Earth for analysis."
  - Wikipedia words it differently: "It was the first asteroid to be the target of a sample-return mission".
- LINK: the current link is https://en.wikipedia.org/wiki/25143_Itokawa. It loads, but a NASA page specific to the body exists, so it FAILS the rule. Replacement, opened: https://science.nasa.gov/solar-system/asteroids/25143-itokawa/, "25143 Itokawa - NASA Science".

## Kamo oalewa
No numbers.
- LINK: https://www.jpl.nasa.gov/news/small-asteroid-is-earths-constant-companion/, "Small Asteroid Is Earth's Constant Companion | NASA Jet Propulsion Laboratory (JPL)". It loads and is a NASA/JPL page about this body. PASSES on the letter of the rule. Note: it is a 2016 news story. It uses the designation 2016 HO3 and never the name Kamo'oalewa, so a visitor cannot tell it is the same object. NASA's asteroid index has no page for the body. If a page that carries the name is preferred, I opened https://en.wikipedia.org/wiki/469219_Kamo%CA%BBoalewa, "469219 Kamo'oalewa", and that article cites this same JPL story.

## 2025 PN7
The description's "2025" and "7" are the designation, not numbers.
- Its non-numeric claim, CONFIRMED in passing: https://en.wikipedia.org/wiki/2025_PN7 (title printed as "2025 PN_{7}"): "2025 PN7 is a small near-Earth asteroid and the most recently discovered quasi-satellite of Earth."
- LINK: https://en.wikipedia.org/wiki/2025_PN7. It loads and is specific to the body. A web search found no NASA page for this body. PASSES.

## 2024 PT5
- "8-9-2024" (August 9, 2024, as the closest approach). **DIFFERS.** The sources give August 8.
  - JPL close-approach API, https://ssd-api.jpl.nasa.gov/cad.api?des=2024%20PT5&date-min=2024-01-01&date-max=2025-12-31&dist-max=0.2: its row is "2024-Aug-08 20:00" (TDB), 0.00379 AU, with a time uncertainty under one minute. A second row gives 2025-Jan-09 02:11.
  - https://en.wikipedia.org/wiki/2024_PT5 (title "2024 PT_{5}"): "The most recent closest approach to Earth was 8 August 2024 at roughly 567,000 km (352,000 mi)".
  - 20:00 TDB on August 8 is still August 8 in UTC. The date becomes August 9 only in time zones at least 4 hours east of UTC.
- LINK: the current link is https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=2024%20PT5, "Small-Body Database Lookup". It is a tool page, and without JavaScript nothing about the body renders. FAILS the rule. Replacement, opened: https://science.nasa.gov/blogs/planetary-defense/2024/10/02/nasa-to-track-asteroid-2024-pt5-on-next-close-pass-january-2025/, "NASA to Track Asteroid 2024 PT5 on Next Close Pass, January 2025 - NASA Science". It is a NASA blog post about this body, and it does not state the August date. The alternative, if a reference article is preferred over a blog post, is https://en.wikipedia.org/wiki/2024_PT5 (opened).

## 2025 PY1
No numbers. The description reads "Near-Earth asteroid."
- LINK: the current link is https://www.jpl.nasa.gov/asteroid-watch/next-five-approaches/, "Next Five Asteroid Approaches | NASA Jet Propulsion Laboratory (JPL)". It is a general tool page, and 2025 PY1 does not appear on it today. FAILS the rule. **I found no replacement.** https://en.wikipedia.org/wiki/2025_PY1 does not exist (url_not_found), and a web search found no NASA page for the body. The only body-specific JPL source I reached was the close-approach API (one row, 2025-Aug-18 22:10 TDB, 0.0019742 AU). It is a data feed, not a page for visitors.

## 2023 JF
- "May 9, 2023" (it flew past Earth). **CONFIRMED.**
  - JPL close-approach API, https://ssd-api.jpl.nasa.gov/cad.api?des=2023%20JF&date-min=2023-01-01&date-max=2023-12-31&dist-max=0.2: "2023-May-09 23:41" (TDB), 0.00214 AU.
  - https://en.wikipedia.org/wiki/List_of_asteroid_close_approaches_to_Earth_in_2023: its row for 2023 JF gives 2023-05-09 and "320,322 km (199,000 mi; 0.002141 AU; 0.8333 LD)".
- LINK: the current link is https://www.nasa.gov/solar-system/near-earth-object-observations-program/, "Near-Earth Object Observations Program - NASA". It is a program hub page, and 2023 JF does not appear on it. FAILS the rule. **I found no replacement.** https://en.wikipedia.org/wiki/2023_JF does not exist (url_not_found), and a web search found no NASA page for the body. The nearest is the Wikipedia list of 2023 close approaches above, which is a list, not an article about the body.

## 2024 DW
- "2-22-2024" (closest approach). **CONFIRMED.**
  - JPL close-approach API, https://ssd-api.jpl.nasa.gov/cad.api?des=2024%20DW&date-min=2024-01-01&date-max=2024-12-31&dist-max=0.2: "February 22, 2024, at 04:37" (TDB), about 0.0015 AU, with a time uncertainty under one minute.
  - https://en.wikipedia.org/wiki/List_of_asteroid_close_approaches_to_Earth_in_2024: its row is "2024-02-22 | 2024-02-19 G96 Mt. Lemmon Survey | 2024 DW | 224,554 km (139,531 mi; 0.00150105 AU; 0.58416 LD)".
- "approximately 5 UTC". **CONFIRMED to the nearest hour.** The JPL value is 04:37 TDB, which is about 04:36 UTC. If an exact figure is wanted, it is "04:37 TDB".
- "Keplerian orbit perturbation from Jupiter". **NOT FOUND.** None of the pages I opened states it. The Wikipedia 2024 list does not mention Jupiter, and the JPL rows hold no such statement. https://en.wikipedia.org/wiki/2024_DW does not exist.
- LINK: the current link is https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=2024%20DW, the "Small-Body Database Lookup" tool page. FAILS the rule. **I found no replacement.** There is no Wikipedia article (url_not_found), and a web search found no NASA page for the body. The nearest is the Wikipedia list of 2024 close approaches.

## 2024 YR4
- "12-25-2024". **CONFIRMED.**
  - JPL close-approach API, https://ssd-api.jpl.nasa.gov/cad.api?des=2024%20YR4&date-min=2024-01-01&date-max=2024-12-31&dist-max=0.2: "2024-Dec-25 at 04:46" (TDB), 0.00554 AU, with a time uncertainty under one minute.
  - https://en.wikipedia.org/wiki/2024_YR4 (title "2024 YR_{4}"): "The asteroid made a close approach to Earth at a distance of 828,800 kilometres" on "25 December 2024, two days before its discovery." The same page gives "Discovery date: 27 December 2024".
  - This was a close approach made before the asteroid was discovered, not a discovery date. The NASA body page (https://science.nasa.gov/solar-system/asteroids/2024-yr4/, "Asteroid 2024 YR4") gives no discovery date and no 2024 close-approach date. Its only date is "When discovered, asteroid 2024 YR4 appeared to have a small chance of impacting Earth on Dec. 22, 2032."
- "4:46 UTC". **DIFFERS, by the time-scale label.** JPL gives 04:46 TDB. TDB was about 69 seconds ahead of UTC, so the time in UTC is about 04:45. Writing either "04:46 TDB" or "about 04:45 UTC" would be correct.
- LINK: https://science.nasa.gov/solar-system/asteroids/2024-yr4/, "Asteroid 2024 YR4". It loads and is specific to the body. PASSES.

## Eurybates
- "Aug 12, 2027" (the Lucy flyby). **DIFFERS.** The two preferred sources give August 11.
  - https://lucy.swri.edu/Eurybates.html, "(3548) Eurybates": "Date: August 11, 2027".
  - https://science.nasa.gov/mission/lucy/, "Lucy - NASA Science", under "Flyby Date (Eastern Time)": "Aug. 11, 2027".
  - Wikipedia gives 12 August. https://en.wikipedia.org/wiki/3548_Eurybates: "The flyby is scheduled for 12 August 2027". The timeline in https://en.wikipedia.org/wiki/Lucy_(spacecraft) also gives "12 August 2027".
  - It may be August 12 in UTC, but no SwRI or NASA page I opened says so.
- "D~64 km". **CONFIRMED on SwRI, which names no source.**
  - SwRI (the page above): "Size: est 64 km (39-40 miles)".
  - Wikipedia (the page above), citing WISE/NEOWISE, AKARI and IRAS: "Eurybates measures between 63.89 and 72.14 kilometers in diameter". Its lead says "approximately 68 kilometers", and its infobox gives a mean of 69.3+/-1.4 km.
- "C-type". **CONFIRMED.** SwRI: "Type: C-type". Wikipedia: "Eurybates has been characterized as a carbonaceous C-type asteroid by both the Lucy mission team".
- Queta "~1 km". **CONFIRMED.** Wikipedia, citing Noll et al. (2020): "It is at least 6,000 times fainter than Eurybates, suggesting that Queta is likely very small, about 1.2 +/- 0.4 km". The estimate assumes Queta has the same albedo as Eurybates. SwRI names Queta but gives no size.
- "first C-type Trojan to be visited". **NOT FOUND.** No page I opened says it: not SwRI, not NASA's Lucy page, not the Wikipedia article on Eurybates or on Lucy. Wikipedia calls Eurybates Lucy's "first main target", which is a different claim.
- LINK: the current link is https://lucy.swri.edu/Eurybates.html. It loads and is specific to the body, but it is neither a NASA page nor Wikipedia. FAILS the rule as written. NASA has no body page: its asteroid index lists none of the Trojans. Replacement, opened: https://en.wikipedia.org/wiki/3548_Eurybates, "3548 Eurybates".

## Patroclus-Menoetius Barycenter
- "March 3, 2033" (the Lucy flyby). **The two preferred sources disagree.**
  - https://science.nasa.gov/mission/lucy/, "Lucy - NASA Science", under "Flyby Date (Eastern Time)": "March 3, 2033". This matches our text.
  - https://lucy.swri.edu/targets/Patroclus-Menoetius.html, "Patroclus and Menoetius": "Lucy will flyby this pair on March 2, 2033." This matches the orrery code comment.
  - https://en.wikipedia.org/wiki/Lucy_(spacecraft): its timeline gives "2 March 2033". https://en.wikipedia.org/wiki/617_Patroclus gives only "scheduled for a flyby in 2033".
  - Time zone does not explain the gap: March 3 in Eastern Time is also March 3 in UTC. One of the two agency pages is wrong, and the pages do not show which. I counted this number as CONFIRMED in the summary, on the NASA page, but it needs a ruling.
- LINK: the current link is https://lucy.swri.edu/targets/Patroclus-Menoetius.html. It loads and is specific to the pair, but it is neither a NASA page nor Wikipedia. FAILS the rule as written. NASA has no body page. Replacement, opened: https://en.wikipedia.org/wiki/617_Patroclus, "617 Patroclus".

## Polymele
- "Sep 15, 2027" (the Lucy flyby). **DIFFERS from NASA.**
  - https://science.nasa.gov/mission/lucy/, "Lucy - NASA Science", under "Flyby Date (Eastern Time)": "Sept. 14, 2027".
  - Wikipedia gives 15 September. https://en.wikipedia.org/wiki/15094_Polymele: "The flyby is scheduled for 15 September 2027". The Lucy (spacecraft) article's timeline also gives "15 September 2027".
  - I could not open the SwRI page to compare. Both https://lucy.swri.edu/Polymele.html and /targets/Polymele.html were refused (robots_disallowed).
- "D~21 km". **CONFIRMED on Wikipedia.**
  - Wikipedia (the page above): "Polymele measures 21.075 kilometers in diameter".
  - NASA gives a different measure. https://www.nasa.gov/feature/goddard/2022/nasa-s-lucy-team-discovers-moon-around-asteroid-polymele, "NASA's Lucy Team Discovers Moon Around Asteroid Polymele": "which is itself around 17 miles (27 km) along its widest axis." Its 27 km is the widest axis, not a mean diameter.
- "P-type". **CONFIRMED.** Wikipedia (the page above): "Polymele has been characterized as a primitive P-type asteroid by the investigators of the Lucy mission."
- Shaun "~5 km". **CONFIRMED.**
  - NASA (the 2022 page above): "this satellite is roughly 3 miles (5 km) in diameter."
  - Wikipedia: "The satellite is a smaller asteroid about 5-6 kilometers (3.1-3.7 miles) in diameter".
- "discovered 2022 via occultation". **CONFIRMED.**
  - https://lucy.swri.edu/2022/08/18/DiscovingASatellite.html, "Discovering a Satellite": "On the evening of March 26, 2022, Polymele was predicted to briefly occult a nondescript 11th magnitude star."
  - Wikipedia: "Following observations of an occultation on 26 March 2022, the Lucy mission team reported the discovery of a" satellite.
  - The NASA 2022 page says "On March 27, Lucy's science team discovered that" the asteroid has a satellite. It is the same event, a day later in its wording.
- LINK: the current link is https://lucy.swri.edu/Polymele.html. The fetch tool was refused (robots_disallowed), so I could not see whether it loads in a browser. It is neither a NASA page nor Wikipedia, so it FAILS the rule as written. NASA has no body page. Replacement, opened: https://en.wikipedia.org/wiki/15094_Polymele, "15094 Polymele".

## Leucus
- "Apr 18, 2028" (the Lucy flyby). **CONFIRMED.**
  - https://lucy.swri.edu/Leucus.html, "(11351) Leucus": "Date: April 18, 2028".
  - https://science.nasa.gov/mission/lucy/ (Eastern Time): "April 18, 2028".
  - https://en.wikipedia.org/wiki/11351_Leucus: "The flyby is scheduled for 18 April 2028".
- "D~40 km". **CONFIRMED on Wikipedia. SwRI gives a different figure.**
  - Wikipedia (the page above): "approximately 40 kilometers (25 miles) in diameter". Its infobox gives "Mean diameter: 41+/-0.7 km (surface equivalent)".
  - SwRI (the page above): "Size: est 34 km (21-22 miles)". SwRI names no source.
- "D-type". **CONFIRMED.** SwRI: "Type: D-type". Wikipedia: "Leucus is a D-type asteroid".
- "~446 hours" (rotation). **CONFIRMED on the Wikipedia infobox.**
  - Wikipedia's infobox: "Synodic rotation period: 445.683+/-0.007 h".
  - The same article's introduction says "a rotation period of 466 hours", which contradicts its own infobox and looks like a typo. The older measurements it cites are 513.7 hours (2013) and 440 hours (2016).
  - SwRI gives no rotation period.
- LINK: the current link is https://lucy.swri.edu/Leucus.html. It loads and is specific to the body, but it is neither a NASA page nor Wikipedia. FAILS the rule as written. NASA has no body page. Replacement, opened: https://en.wikipedia.org/wiki/11351_Leucus, "11351 Leucus".

## Orus
- "Nov 11, 2028" (the Lucy flyby). **CONFIRMED.**
  - https://lucy.swri.edu/Orus.html, "(21900) Orus": "Date: November 11, 2028."
  - https://science.nasa.gov/mission/lucy/ (Eastern Time): "Nov. 11, 2028".
  - https://en.wikipedia.org/wiki/21900_Orus: "The flyby is scheduled for 11 November 2028".
- "D~51 km". **CONFIRMED on SwRI, which names no source.**
  - SwRI (the page above): "Size: est 51 km (31-32 miles)."
  - Wikipedia gives other figures: "approximately 53 kilometers (33 miles) in diameter", and an infobox mean of "60.5+/-0.9 km (area equivalent)".
- "D-type". **CONFIRMED.** SwRI: "Type: D-type." Wikipedia: "Orus is characterized as a D-type and C-type asteroid by the Lucy mission team". Its infobox lists "Spectral type: C . D" (a middle dot between the two).
- "last L4 Trojan visit before heading to L5". **CONFIRMED from a table, not from a sentence.**
  - In https://en.wikipedia.org/wiki/Lucy_(spacecraft), Orus is the last L4 entry in the mission timeline table (11 November 2028). The next event is an Earth flyby on 26 December 2030. The article's trajectory summary says the orbit "falls back to Earth for another flyby, then on to Jupiter's L5."
  - No page states the claim in a sentence. SwRI's Orus page does not mention L4 or L5.
- LINK: the current link is https://lucy.swri.edu/Orus.html. It loads and is specific to the body, but it is neither a NASA page nor Wikipedia. FAILS the rule as written. NASA has no body page. Replacement, opened: https://en.wikipedia.org/wiki/21900_Orus, "21900 Orus".

---

Pages opened (successfully): science.nasa.gov/mission/dawn/; science.nasa.gov/solar-system/asteroids/ (index), /4-vesta/, /16-psyche/, /donaldjohanson/, /dinkinesh/, /433-eros/, /101955-bennu/, /25143-itokawa/, /2024-yr4/; science.nasa.gov/mission/psyche/; science.nasa.gov/mission/lucy/; science.nasa.gov/blogs/planetary-defense/2024/10/02/nasa-to-track-asteroid-2024-pt5-on-next-close-pass-january-2025/; www.nasa.gov/image-article/asteroid-lutetia/; www.nasa.gov/solar-system/near-earth-object-observations-program/; www.nasa.gov/feature/goddard/2022/nasa-s-lucy-team-discovers-moon-around-asteroid-polymele; www.jpl.nasa.gov/news/small-asteroid-is-earths-constant-companion/; www.jpl.nasa.gov/asteroid-watch/next-five-approaches/; ssd.jpl.nasa.gov/tools/sbdb_lookup.html (2024 PT5); ssd-api.jpl.nasa.gov/cad.api (2024 PT5, 2024 DW, 2024 YR4, 2023 JF, 2025 PY1); ssd-api.jpl.nasa.gov/doc/cad.html; www.esa.int/Science_Exploration/Space_Science/Rosetta; news.arizona.edu/news/large-craters-offer-clues-origin-asteroid-16-psyche; lucy.swri.edu/Eurybates.html, /targets/Patroclus-Menoetius.html, /Leucus.html, /Orus.html, /Donaldjohanson.html, /2022/08/18/DiscovingASatellite.html; en.wikipedia.org/wiki/162173_Ryugu, 25143_Itokawa, 2867_Steins, 469219_Kamo'oalewa, 2025_PN7, 2024_PT5, 2024_YR4, List_of_asteroid_close_approaches_to_Earth_in_2023, List_of_asteroid_close_approaches_to_Earth_in_2024, 52246_Donaldjohanson, 3548_Eurybates, 15094_Polymele, 11351_Leucus, 21900_Orus, 617_Patroclus, Lucy_(spacecraft). Failed to load: science.nasa.gov/solar-system/asteroids/21-lutetia/, /lutetia/, /2867-steins/, /162173-ryugu/, /ryugu/ (client errors); lucy.swri.edu/Polymele.html, /targets/Polymele.html, /mission.html (robots_disallowed); en.wikipedia.org/wiki/2024_DW, 2023_JF, 2025_PY1 (do not exist).
