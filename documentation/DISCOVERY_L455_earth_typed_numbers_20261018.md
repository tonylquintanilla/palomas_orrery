<!-- Doc-Kind: hand | Discovery list for L-455, Earth's share: every number typed into Earth's served words, as the Typed numbers check first printed it, and the orrery's low-orbit tooltip and hover. Lists; fixes nothing. -->
# L-455 discovery: the numbers typed into Earth's visitor text

Built on orrery 05cb185ada593eda178b79c57d2a3cbfcce97a24 at
https://github.com/tonylquintanilla/palomas_orrery ("cleanup") and gallery
10508dfc2ef1afd657e6630d18b7cf00ef50eca6 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io ("daily run
and L411 voyager 2 words"). Written 2026-10-18 by Anthropic's Claude Opus
5.5.

This is DISCOVERY, kept apart from remediation (The Braid): it lists
against one stated pattern and fixes nothing. What was done with each
line is in `WORDS_L455_earth_numbers_20261018.md`.

## How the website's list was found

By a check, not by hand (Tony, 2026-10-18: "mask every served number that
has a row behind it and fail on any digit left standing, so Earth's sweep
is the check's output and it runs on every website maintenance run").
`documentation/smoke_typed_numbers.js` in the gallery, the run's new
"Typed numbers" row, builds the Sun and Earth rooms from
`data/objects_config.json` three ways: as served, with every served
number scaled, and with every served word masked. A number a visitor
reads that moved with its row came from the row. One that did not move,
inside a served word, was typed there. A digit in a name (Voyager 2,
ISEE-3, IGRF-13), a citation's locator (an author's year in brackets, an
equation, section, figure, table or page number, a journal's volume and
page), a symbol's subscript or a constant inside a written equation is
not a number about nature and is not counted. Only what a visitor reads
is examined: the hovers, the drawer's names and the i panel.

Its first run, below, found 48 sentences: 40 in Earth's words and 8 in
the Sun's. The Sun's 8 are L-411's bulk, left for later sessions by
Tony's ruling of 2026-10-17; they are HELD on the check under L-411 and
printed every run.

## Earth's 40 sentences, as the check printed them

The standing digits are in [brackets]. "panel" is the i panel; "hover" is
the hover box; "name" is the drawer's row and the hover's first line.

```
earth / Earth: Inner Core / panel about:
    Temperatures near [5,400] degrees Celsius keep the inner core close to melting even under the weight of the whole planet.
earth / Earth: Outer Core / panel about:
    The outer core is molten iron and nickel with lighter elements mixed in, at [4,500] to [5,400] degrees Celsius.
earth / Earth: Lower Mantle / panel about:
    The lower mantle is solid silicate rock rich in iron and magnesium, at [2,200] to [4,500] degrees Celsius and under enormous pressure.
earth / Earth: Upper Mantle / panel about:
    It reaches from the base of the crust down to the top of the lower mantle, with temperatures from about [500] to [2,200] degrees Celsius.
earth / Earth: Crust / panel about:
    The crust is thin compared with the planet: [5] to [10] km under the oceans, where it is mostly basalt, and [30] to [50] km under the continents, where it is mostly granite.
earth / Earth: Crust / panel about:
    Surface temperatures range from about minus [80] to [60] degrees Celsius.
earth / Earth: Crust / panel note:
    Crust thickness ([5]-[10] km oceanic, [30]-[50] km continental) is below the drawn resolution.
earth / Earth: Crust / panel source_note:
    The Earth radius used as the unit stays the IAU's equatorial one: Prsa et al. (2016), AJ 152:41, on IAU [2015] Resolution B3.
earth / Earth: Lower Atmosphere (to the stratopause) / panel about:
    The troposphere, the lowest [12] km or so, is where clouds and weather form; above it the stratosphere, to about [50] km, holds the ozone layer.
earth / Earth: Lower Atmosphere (to the stratopause) / panel about:
    Together they contain [99] percent of the atmosphere's mass, mostly nitrogen and oxygen.
earth / Earth: Lower Atmosphere (to the stratopause) / panel about:
    Temperature falls from about [15] degrees Celsius at sea level to minus [60] at the top of the troposphere, then warms again toward the stratopause as ozone absorbs sunlight.
earth / Earth: Lower Atmosphere (to the stratopause) / panel note:
    Troposphere and stratosphere, [99]% of atmospheric mass.
earth / Earth: Lower Atmosphere (to the stratopause) / panel note:
    Drawn at the physical boundary since [2026-09-07] (L-[295]); before that at a visibility fraction its own hover contradicted.
earth / Earth: Upper Atmosphere (to the thermopause) / panel about:
    Above [50] km lie the mesosphere, where most meteors burn up, the thermosphere, where the aurora appears and the International Space Station flies, and, higher still, the beginning of the exosphere.
earth / Earth: Upper Atmosphere (to the thermopause) / panel about:
    In the thermosphere the gas can reach [2,000] degrees Celsius, yet it is so thin it would feel cold to the skin.
earth / Earth: Upper Atmosphere (to the thermopause) / panel note:
    The thermopause moves with solar activity over roughly [500]-[1,000] km; [600] km is the nominal figure.
earth / Earth: Low Earth Orbit, inner edge (180 km) / name:
    Earth: Low Earth Orbit, inner edge ([180] km)
earth / Earth: Low Earth Orbit, inner edge (180 km) / panel about:
    Low Earth orbit is the region from roughly [180] to [2,000] km up.
earth / Earth: Low Earth Orbit, inner edge (180 km) / panel about:
    Satellites there circle at every angle to the equator, so together they form a shell around Earth rather than a ring, and each completes an orbit in about [90] to [120] minutes.
earth / Earth: Low Earth Orbit, inner edge (180 km) / hover:
    Earth: Low Earth Orbit, inner edge ([180] km)
earth / Earth: Low Earth Orbit, outer edge (2,000 km) / name:
    Earth: Low Earth Orbit, outer edge ([2,000] km)
earth / Earth: Low Earth Orbit, outer edge (2,000 km) / panel about:
    Low Earth orbit is the region from roughly [180] to [2,000] km up.
earth / Earth: Low Earth Orbit, outer edge (2,000 km) / panel about:
    Satellites there circle at every angle to the equator, so together they form a shell around Earth rather than a ring, and each completes an orbit in about [90] to [120] minutes.
earth / Earth: Low Earth Orbit, outer edge (2,000 km) / hover:
    Earth: Low Earth Orbit, outer edge ([2,000] km)
earth / Earth: Low Earth Orbit, outer edge (2,000 km) / hover:
    The upper edge of low Earth orbit, about [2,000] km up, above which the sky belongs to higher orbits.
earth / Earth: Geostationary Belt (GEO) / panel about:
    In April [2029] the asteroid Apophis will pass inside this ring, a few thousand kilometers below the nearest satellites.
earth / Earth: Geostationary Belt (GEO) / panel note:
    A ring in the equatorial plane, not a sphere, tilted with Earth's equator by the served pole. [42,164] km from Earth's centre, [35,786] km up.
earth / Earth: Geostationary Belt (GEO) / hover:
    A ring of satellites [35,786] km above the equator that circle exactly as fast as Earth turns, so each hangs over one spot.
earth / Earth: Magnetopause / panel note:
    Under storm compression it can fall inside geostationary orbit ([6.6] R_E).
earth / Earth: Magnetopause / panel detail:
    At the declared conditions alpha is [0.59] -- two figures, because a6 is [0.58] +/- [0.01] and that carries straight through.
earth / Earth: Magnetotail / panel about:
    Spacecraft crossing it far downstream found that it stops widening about [120] Earth radii behind Earth and is about [60] Earth radii across beyond there.
earth / Earth: Magnetotail / panel about:
    ISEE-3 followed it out to [220] Earth radii, which is how far the spacecraft went rather than where the tail ends.
earth / Earth: Magnetotail / panel note:
    The straight widening between where the Sun-facing surface stops and [120] Earth radii is our choice: the measurements give only its two ends.
earth / Earth: Bow Shock / panel detail:
    At tau = [0] this is the standoff below.
earth / Earth: Inner Radiation Belt / panel note:
    The edges are their own rows below, as of [2026-09-14] (L-[305] item [7]); this note carried the span in prose until then, which is what let the served figure and the orrery's disagree.
earth / Earth: Inner Radiation Belt / panel detail:
    The field lines are drawn around Earth's spin axis: the daily average of the magnetic field, which turns with Earth and in [2020] was tilted 9.4105 degrees from it, shrinking 0.0493 degrees a year (IGRF-13 model).
earth / Earth: Outer Radiation Belt / panel note:
    Baker et al. (2018) was removed from this citation on [2026-09-14]: his figure [30] uses L* = [4.5] as a selected analysis location rather than a universal peak, and his span figure belongs on the edge row below.
earth / Earth: Outer Radiation Belt / panel detail:
    The field lines are drawn around Earth's spin axis: the daily average of the magnetic field, which turns with Earth and in [2020] was tilted 9.4105 degrees from it, shrinking 0.0493 degrees a year (IGRF-13 model).
earth / Earth: Hill Sphere (gravitational dominance over the Sun) / panel note:
    About [1.50] million km.
earth / Earth: Hill Sphere (gravitational dominance over the Sun) / panel note:
    The Moon at about [60] Earth radii sits well inside it, which is why it stays bound. a = [1] AU exactly; Earth's semi-major axis is [1.00000011] AU (NASA Earth Fact Sheet).
```

Sorted by kind (each sentence once):

- **Temperatures typed in degrees Celsius** (provenance-discipline 2.31
  says kelvin): the inner core, outer core, lower and upper mantle, the
  surface range, sea level and the tropopause, the thermosphere.
- **A number a row already holds, typed again**: the low-orbit edges
  (names, description, about), the geostationary ring's radius and
  height (description, note), the magnetotail's three sizes (about,
  note), the magnetopause's flaring coefficient a6 and its uncertainty,
  the Hill sphere's radius, the stratopause's 50 km in the upper
  atmosphere's about. Also 6.6 Earth radii, the geostationary ring's
  radius, in the magnetopause's note.
- **A number with no row and no citation**: the crust's two thickness
  ranges, the troposphere's 12 km, 99 percent of the atmosphere's mass,
  the thermopause's 500 to 1,000 km, the 90 to 120 minute orbit, the
  Moon at 60 Earth radii, alpha's 0.59.
- **Bookkeeping in a website note** (What a Visitor Reads, principles 2
  and 5): dates of rulings and ledger handles in the lower atmosphere's
  and both belts' notes; the Hill sphere's "a = 1 AU exactly"; Baker's
  figure 30 and L* = 4.5; the crust's source_note, a citation for the
  unit, which is wording for the store.
- **Dates of events**: Apophis in April 2029; the field model's epoch,
  2020, in the belts' plane sentence.
- **An equation's parameter**: tau = 0 in the bow shock's model.

## The orrery's low-orbit tooltip and hover

`earth_visualization_shells.py`, `earth_leo_shell_info` (the checkbox
tooltip) and `create_earth_leo_shell()`'s hover; plus a second copy of
the tooltip in `shell_configs.py`, CUSTOM_SHELLS['Earth']['leo'], found
while testing the live path. The edges already printed from their rows
(L-452). Typed:

- one orbit in 90 to 120 minutes; crossing the sky in about 6 minutes
- the ISS at about 400 km and 51.6 degrees; Starlink at about 550 km;
  Hubble at about 540 km
- about 11,000 active satellites in low orbit, nearly 7,000 of them
  Starlink; more than 35,000 tracked debris objects larger than 10 cm
- GEO "5x farther out"; the tooltip's "GEO satellites at 35,786 km"
- the drawing's `STARLINK_KM = 6921.0` (550 km above the 6,371 km MEAN
  radius, where the shell is drawn against the equatorial one), a 150 km
  spread around it and a 60/40 mix of even and clustered dots, all chosen
  by eye
- the source comment named the UCS database and ESA's debris office as
  "counts as of early 2026" under the retired "Verified: April 2026 via
  Gemini fact-check" stamp; neither was a read.

## Met outside the slice, recorded by class (The Braid)

- **The orrery's other Earth tooltips and hovers type the same numbers**:
  the interior's Celsius temperatures and the crust's thickness ranges
  (`earth_inner_core_info` through `earth_crust_info`), the lower and
  upper atmosphere's (`earth_atmosphere_info`, the `shell_configs.py`
  Earth atmosphere hover, `earth_upper_atmosphere_info`), the
  geostationary tooltip's satellite count and Apophis figures. The rows
  added for the website serve them too. One ledger class; L-455
  re-homed it at its close to L-413 (Earth's list), whose talks open
  those files, with the geostationary height's last digit (35,786.03
  printed against 35,786.04 from a row).
- **The Sun's 8**: on L-411, held on the check.
