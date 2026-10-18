<!-- Doc-Kind: hand | Session record of the Sun's numbers build, the first half of L-412: the Alfven ranges (L-228), the typed numbers' first groups (L-411), the Sun's unexported rows (L-386), the exact-rows check and the eyeballed numbers (L-371), the kelvin rule; two patches, with Tony's run order. -->
# Handoff: the Sun's numbers (L-412, first half)

Built on orrery 6f4fc9b0e85bf27920cea5bc9e664ee85455bcf1 at
https://github.com/tonylquintanilla/palomas_orrery ("L412 sun next")
and gallery da442bf21c7d90bffc775e8f5e58d751265a1aa2 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io ("daily
run again and L410 earth fade website"). Nothing pushed by this
session; Tony pushes.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD. Written October 17, 2026 by Anthropic's Claude Opus 5.5.
Companions, both shipped by the orrery patch:
`documentation/DISCOVERY_L411_sun_typed_numbers_20261017.md` (every
number typed into the Sun's visitor text, by kind and by string) and
`documentation/WORDS_L411_L386_sun_numbers_20261017.md` (the wording
list, revision 2, which Tony approved). L-228's wording list was
approved in the conversation at 21:25 and is not in a file.

## 1. Your run order (every Tony-action of this session, in one list)

Each patch checks the lines it edits and refuses rather than guess.

1. **(do)** Orrery folder: run `patch_L412_2_sun_numbers_20261017.py`.
2. **(do)** Orrery maintenance run (dashboard). Expect every checker to
   pass, the gate line "0 TIER-1", and the whole tree still 280. Two
   lines are new: "Exact rows by the count" reads 0 not followed, and
   the Constants change report lists 13 new rows and says
   PARKER_CLOSEST_RADII is NOW DERIVED (was 9.86).
3. **(look)** Mode 5 in the orrery: plot the Sun with its shells and
   read the hovers of the core, radiative zone, photosphere,
   chromosphere, inner and outer corona, streamer band, Alfven surface,
   termination shock, heliopause and gravitational influence (Sedna).
   The core is drawn larger, at a quarter of the Sun's radius.
4. **(do)** Move the orrery script into `documentation/`; commit; push.
   This push must come before step 6: the website's Daily Run pulls the
   new rows from GitHub.
5. **(do)** Reinstall provenance-discipline (2.31) in Settings > Skills.
6. **(do)** Website folder: run `patch_L411_1_sun_words_20261017.py`.
7. **(do)** The Daily Run. Its pulls write the Sun's new values and
   citations into the config, then it builds. Until the build has run,
   "Cache in step" and "Display figures" are red; that is expected.
   After it, expect every gating check to pass, "Display figures" with
   48 hovers held to the new fixture.
8. **(do)** Move the website script into `documentation/`; commit the
   config, the cache, the renderer and the fixture together; push; then
   `python gallery_maintenance_run.py --live`.
9. **(look)** Mode 5 on the phone, the Sun room: the text boxes and i
   panels of the core, radiative zone, photosphere, chromosphere,
   Alfven surface and termination shock.

## 2. What was built

**The orrery, `constants_new.py`.** Thirteen new rows, each read from
an open source tonight:
- The Alfven surface's usual range, 10 and 20 solar radii, from
  Cranmer et al. (2023), abstract and sec. 3.1; and DeForest, Howard
  and McComas (2014)'s 15 solar radii, as what it is: a coronagraph's
  field-of-view floor.
- The core's radius, 0.25 solar radii, and the photosphere's thickness
  (100 km) and temperature (5,700 K), from Hathaway's NASA/Marshall
  solar interior and photosphere pages.
- The radiative zone's edge, a measured 0.713 +/- 0.003, from Delahaye
  and Pinsonneault.
- Parker Solar Probe's closest approach as its altitude, 6.16 million
  km (Johns Hopkins APL; the date from NASA SVS); the distance from the
  centre is derived, and its solar radii are a conversion (9.85).
- The termination shock's range, 80 to 100 AU (Treumann and Jaroschek
  2008); Voyager 2's crossing at 84 AU (NASA SVS); and the wind's speed
  either side of it, about 320 and 200 km/s (Li, Wang and Richardson
  2008, Table 1).
CORE_AU, RADIATIVE_ZONE_AU and SOLAR_RADIUS_AU are conversions of
their rows. The chromosphere's depth is re-homed to an open source
(the Yohkoh Public Outreach Project, Montana State).

**The orrery, `solar_visualization_shells.py`.** The Sun's hovers
print those numbers from their rows, each with a citation the visitor
sees. The pole-and-streamer ranges are gone; they had the shape
backwards. The Voyagers' line says both are past the heliopause.
Sedna's farthest point, 937 AU from the solar system's centre of mass,
is worked out from the period record the orrery fetched on 2026-10-13,
not typed. The streamer belt's text no longer carries a ruling date.

**The orrery's checks.** `exact_rows_report.py` now follows every Sun
pointer to an exact row, reads a shell's served slot by the mirror's
own rule, and compares a slot served in another unit through the
export's counts. `constants_change_report.py` names a typed row that
became a derived one, instead of calling it unreadable: tonight's
maintenance run failed on exactly that, for PARKER_CLOSEST_RADII.

**The rule.** provenance-discipline 2.31: temperatures are stored and
printed in kelvin.

**The website.** In `data/objects_config.json` the core, radiative
zone and photosphere point at their new rows, new linked numbers serve
the photosphere's thickness and temperature, the chromosphere's depth,
the Alfven surface's range and the termination shock's numbers, and
the Sun's words are Tony's approved revision 2. A small helper in
`gallery/feature_renderers.js`, `withShellWords`, fills a shell's
radius and its linked numbers into its words, with each citation
beside them; Earth's room is unchanged by it. The display-figures
fixture is re-recorded with exactly two hovers different, the core and
the radiative zone, whose radius lines changed.

## 3. Tony's rulings this session

- "Source it or remove it, one number at a time; every wording change
  comes to me as a list before it ships." (the starting prompt)
- L-411's scope: groups W, S, D and N tonight, the bulk left on L-411.
  Asked whether that was the recommendation: "yes. and the goal should
  be to settle as much as possible by method rather than by
  judgement."
- Kelvin: "don't we standardize on degrees Kelvin? the conversion is
  routine." Then: "good point. we should add this to the skill." Now
  provenance-discipline 2.31.
- "No source?", on three removals: each had one, and each is back from
  it. Revision 2 of the wording list: "read and approved."
- "the numbers half ends with Earth's sweep (L-455), the same method."
  Then L-455 next session and the close tonight, and the twelve
  eyeballed shape numbers with the drawings: "confirmed as
  recommended."

## 4. How it was checked

- Every orrery store check passes on the working copy: derived
  figures, dimensions, the export and its check, citation inheritance,
  status lines, row shape, the scanner's row run and recognition pins.
- The orrery maintenance run: one failure, Constants change, which was
  the checker's own blind spot and is fixed in this patch; the run is
  repeated on the patched copy before delivery (section 6).
- Exact rows: PASSING, 12 of 40 exact rows printed at 54 lines, 12
  drawn only, 0 not followed, 0 broken; a planted wrong count was
  caught by name.
- Provenance scanner: gate path 0 Tier-1; whole tree 280, unchanged.
  The Sun file still has 6 Tier-1 findings, all in the core's
  textbook text, group T, left on L-411.
- The pre-test: the orrery compiles, opens its window under a headless
  display with no error, and the live dispatch prints the new strings
  and none of the old ones.
- The website: every check passes on a copy whose cache was given the
  config's Sun features, as the builder copies them. Without that,
  "Cache in step" and "Display figures" are red, as expected.
- The patches were run on throwaway copies of both repositories at the
  SHAs above, and their output compared with the working copies.

## 5. Skill versions and what travels

This session's loaded copies read provenance-discipline 2.30,
interactive-exhibit 1.17 and gallery-cache-builder 1.11 (discharging
v3.102's obligation), horizons-orbital-mechanics 1.8 (discharging
v3.99's), ledger-and-session-records 1.21, safe-file-editing 1.13 and
agentic-pre-test 1.3, as the manifest expected.

A reinstall during a session is not visible to it. The next session
confirms its loaded copy reads provenance-discipline 2.31 before
provenance work.

## 6. What is left, and the next session

- L-455 (typed numbers in the website's served words), Earth's share,
  is the last item of the Sun's numbers half. Discovery first, then
  each number sourced or removed. It holds the Crust and magnetopause
  notes, Earth's interior and atmosphere paragraphs typed in degrees
  Celsius, and the orrery's low-orbit numbers. One wording question is
  yours there: Earth's surface temperatures, "minus 80 to 60 degrees
  Celsius", would read as about 190 to 330 kelvin.
- L-411 keeps its bulk: groups T, M and C in the discovery file, the
  streamer band's 7.25 degrees, the Roche formula's typed inputs, and
  the orrery photosphere's 5,500 K with the wavelength worked from it.
- The twelve eyeballed shape numbers (the streamer belt's seven, the
  clumpy Oort cloud's five) go with the drawings, on L-412.
- The question for after L-455: which of the Sun's drawings follow?

Starting prompt for the next session:

```
Build session: L-455 (typed numbers in the website's served words),
Earth's share: the last item of the Sun's numbers half on L-412 (the
Sun's list). Same method as the Sun's numbers: discovery first, every
typed number in Earth's served words and in the orrery's low-orbit
hover, then each sourced into a row or removed, one number at a time.
Temperatures in kelvin (provenance-discipline 2.31). Every wording
change comes to me as a list before it ships. One question per
message, plain speech. Pull both repositories and say the SHAs; the
handoff is documentation/HANDOFF_L412_sun_numbers_20261017.md.
Confirm your loaded provenance-discipline reads 2.31 before provenance
work; name the interactive-exhibit and gallery-cache-builder versions
if any work fires them. At the close: the handoff, the ledger patch,
Where We Are, and the one question: which of the Sun's drawings
follow.
```
