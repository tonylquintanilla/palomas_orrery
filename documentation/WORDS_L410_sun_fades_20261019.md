<!-- Doc-Kind: hand | The words a visitor will read for the Sun's two fades (L-410 with L-131), revision 1, for Tony's review before the build. -->
# Words: the Sun's corona and dust cloud, revision 2

Built on orrery 6e0cfacd0b6aa42cb09b0ca765be94e68aab6f70 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
4fc320fa6d2e0e10d9a50b8b69006cbff96a1364 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: DESIGN (zero code). Written October 19, 2026 by Anthropic's
Claude Opus 5.5, for Tony to read before the build. Sources:
`SOURCES_L410_sun_corona_dust_20261019.md`. Revision 2, the same
evening, after Gemini's worksheet
(`REVIEW_L410_gemini_worksheet_20261019.md`): 1d's model changes,
3b now has a source, and a temperature is offered (3c).

How to read this list:
- A number in braces, {LIKE_THIS}, prints from a row in
  constants_new.py, with the row's citation. No number is typed.
- The same words serve both sites: the website's name, description,
  hover, panel text ("about") and drawing note; the orrery's checkbox
  name, hover and checkbox tooltip. The hover is the glance; the
  panel carries the rest.
- Distances in the orrery's hovers also print in AU, as every orrery
  distance does.
- Answer each item in place: "-- yes", "-- change to ...", "-- let's
  discuss".

## The rule both drawings follow (Tony, 2026-10-19)

Each dot's place shows how dense the gas or dust is; its brightness
shows how much sunlight reaches it, which falls with the square of
distance from the Sun. "Yes confirmed" for the corona as well as the
dust.

## 1. The corona (replaces "Inner Corona" and "Extended Corona")

**1a. Name.** Corona
(orrery checkbox: "-- Corona"; the two old checkboxes go)

**1b. Description** (website, one line).
The Sun's outer atmosphere: a very thin gas that thins out with height
until it becomes the solar wind.

**1c. Hover.**
Corona
The Sun's outer atmosphere, a very thin gas of electrons and ions.
It has no edge. It thins out with height, and at the Alfven surface,
about {ALFVEN_SURFACE_RADII} solar radii ({ALFVEN_SURFACE_RADII in AU} AU)
from the Sun's center, it becomes the solar wind.
Each dot's place shows how dense the gas is; its brightness shows how
much sunlight reaches it.

**1d. Panel text** (website "about"; orrery checkbox tooltip).
The corona's glow, seen at a total eclipse, is sunlight scattered by
its free electrons, called the K-corona (Boe and others, 2021). How
dense the gas is at each height comes from a model of the solar wind
from the Sun's surface out past Earth's orbit (Mann and others, 2023).
The dots follow it: crowded at the surface,
sparse by the Alfven surface. Farther out a second, fainter light
takes over, sunlight scattered by dust, the F-corona; that dust is
drawn as its own cloud.

**1e. Drawing note** (website `source_note`; the orrery says the same
in its tooltip).
The dots show the model's smooth average, drawn the same in every
direction. The real corona is lumpy, shaped by the Sun's magnetic
field into streamers and holes; the streamer belt is drawn
separately. The dots stop at the Alfven surface.

**What goes.** The two old hovers and tooltips, and the website's
"Inner Corona" and "Outer Corona" entries. Their temperatures ("1-3
million K", "one to three million kelvin"), the "~2.3" and "~3 R_sun"
crossover, and the "1.93 nm" and "1.159 nm" wavelengths have no row
behind them and are not carried. If you want a temperature back, it
needs a source and a row first.

## 2. The dust cloud (new)

**2a. Name.** Zodiacal Dust Cloud (F-corona)
(orrery checkbox: "-- Zodiacal Dust Cloud (F-corona)")

**2b. Description** (website, one line).
Dust spread through the inner solar system in a flattened cloud. Near
the Sun its scattered sunlight is the F-corona.

**2c. Hover.**
Zodiacal Dust Cloud
Dust spread through the inner solar system, flattened toward the plane
the planets move in. It thins with distance from the Sun and has no
edge; the drawing stops at {ZODIACAL_DUST_OUTER_AU} AU.
Each dot's place shows how dense the dust is; its brightness shows how
much sunlight reaches it.
Near the Sun this dust is seen as the F-corona.

**2d. Panel text.**
This dust scatters sunlight. Near the Sun that light is the F-corona,
the part of the zodiacal light closest to the Sun (Boe and others,
2021). The cloud's shape follows the model fitted to the COBE
satellite's infrared sky: its density falls with distance from the
Sun to the power {ZODIACAL_DUST_DENSITY_EXPONENT}, and it is flattened
toward a middle plane tilted {ZODIACAL_DUST_TILT_DEG} degrees to
Earth's orbit (Kelsall and others, 1998). Close to the Sun the dust
thins from about {DUST_DEPLETION_OUTER_RADII} solar radii inward and
is gone by about {DUST_FREE_ZONE_RADII}, the dust-free zone (Lamy and
others, 2022); Parker Solar Probe saw the first signs of it (Howard
and others, 2019). There, the cloud's middle plane is also warped
(Lamy and others, 2022), which the drawing does not show.

**2e. Drawing note.**
The cloud has no edge. The dots stop at {ZODIACAL_DUST_OUTER_AU} AU,
where the COBE model stops adding up its light. Only the model's
smooth cloud is drawn, not the narrow dust bands it also includes.

## 3. Left out on purpose, for you to decide

**3a. Forward scattering.** Dust sends most of the light it scatters
nearly straight on, which is why the F-corona is brightest just beside
the Sun, and it depends on where the viewer stands, so no drawing of
the cloud can show it. I would like to say this in the panel, but the
sources read so far do not state it in words, so it is out until one
does. Keep looking for a source, or leave it out?

**3a, after Gemini.** Still unsourced. Its sources were a paper about
dust on a telescope's own lenses, a paper not re-opened, and a
commercial web page; a review re-opened here does not say it either.
Recommended: leave it out.

**3b. Where the dust comes from: now sourced.** Proposed for the end of
2d:
Judged by its infrared glow, most of this dust comes from comets
whose orbits Jupiter shapes, the Jupiter-family comets:
{ZODIACAL_DUST_JFC_LOW_PERCENT} to {ZODIACAL_DUST_JFC_HIGH_PERCENT}
percent. Asteroids give less than {ZODIACAL_DUST_ASTEROID_MAX_PERCENT}
(Nesvorny and others, 2010).
Keep, change, or leave out?

**3c. A temperature for the corona (optional).** NASA's "Our Sun:
Facts" page gives the corona as reaching up to 2 million degrees
Celsius, which is 2 million kelvin to the figure printed. Proposed for
the end of 1d: "The corona is very hot, up to about
{CORONA_TEMPERATURE_MAX_K} kelvin, far hotter than the surface below
it (NASA)." The page is re-opened at the build before it becomes a
row. Keep it, or leave the temperature out?

## 4. The rows these words need (written at the build)

| Row | Value | Kind | From |
|---|---|---|---|
| the corona's density | Table 8 | measured | Mann et al. 2023, their own model, 1 to 250 solar radii; Leblanc (eq. 7) only beyond 1.8 |
| ZODIACAL_DUST_DENSITY_EXPONENT | 1.34 | measured | Kelsall et al. 1998, Table 1 |
| ZODIACAL_DUST_BETA, _GAMMA, _MU | 4.14, 0.942, 0.189 | measured | same |
| ZODIACAL_DUST_TILT_DEG, _NODE_DEG | 2.03, 77.7 | measured | same |
| ZODIACAL_DUST_OUTER_AU | 5.2 | declared | the model's cutoff, sec. 4.2 |
| DUST_DEPLETION_OUTER_RADII | 19 | measured | Lamy et al. 2022, abstract |
| DUST_FREE_ZONE_RADII | 5 | measured | same |
| ZODIACAL_DUST_JFC_LOW_PERCENT, _HIGH_PERCENT | 85, 95 | measured | Nesvorny et al. 2010, abstract (3b, if kept) |
| ZODIACAL_DUST_ASTEROID_MAX_PERCENT | 10 | measured | same |
| CORONA_TEMPERATURE_MAX_K | 2e6 | measured | NASA, "Our Sun: Facts" (3c, if kept) |

ALFVEN_SURFACE_RADII is already a row. The names are proposals; the
build settles them by the store's conventions.

Session written October 2026 with Anthropic's Claude Opus 5.5.
