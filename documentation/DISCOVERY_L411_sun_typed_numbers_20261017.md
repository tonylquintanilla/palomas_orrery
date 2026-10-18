<!-- Doc-Kind: hand | Discovery list for L-411: every number typed into the Sun's visitor text, sorted by kind. Lists; fixes nothing. -->
# L-411 discovery: the numbers typed into the Sun's visitor text

Built on orrery 6f4fc9b0e85bf27920cea5bc9e664ee85455bcf1 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
da442bf21c7d90bffc775e8f5e58d751265a1aa2 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, with
L-228's edits applied (this session). Written 2026-10-17 by Anthropic's
Claude Opus 5.5.

This is DISCOVERY, kept apart from remediation (The Braid): it lists
against one stated pattern and fixes nothing. The pattern: a digit
typed inside a string a visitor reads -- in the orrery, every
module-level `*_info`, `*_info_hover`, `hover_text_*` and `*_LINE`
string in `solar_visualization_shells.py`, and every hover or name
built inside its `create_sun_*` functions; on the website, every word
field under the Sun's entry in `data/objects_config.json`. Numbers
printed through a store row (`row_text`, `exact_text`, an f-string over
a constant) are NOT counted: they already have one home. Docstrings
and comments are not counted.

Tony's ruling on scope, 2026-10-17: this session works groups W, S, D
and N below; T, M and C (the bulk) stay on L-411 for later sessions,
one shell at a time, settled by method wherever a rule can.

## The count

- Orrery: 340 typed digit runs in 40 strings. The `*_info` and
  `*_info_hover` strings mostly repeat each other, so it is about 170
  distinct claims. Dates and years count as digit runs here.
- Website: 15 typed numbers a visitor reads, in 9 word fields
  (bookkeeping fields `_comment` and `_declared` are not read and not
  counted).

## The kinds, with where each lives

### W. The website's Sun words (served; a visitor reads them online)

- `sun_structures/core/about`: a quarter of the radius; a third of the
  mass; 15 million kelvin; 150 times water.
- `sun_structures/radiative/about`: a fifth and seven tenths of the
  radius; 7 million and 2 million kelvin; millions of years.
- `sun_structures/photosphere/about`: 500 km; 5,500 kelvin.
- `solar_atmosphere/chromosphere/name` and `/description`: 2,000 km
  (the store holds it, CHROMOSPHERE_PHYSICAL_KM).
- `solar_atmosphere/chromosphere/about`: a few thousand and 20,000
  kelvin.
- `solar_atmosphere/chromosphere/note`: "Derived: 1 + 2000 km /
  695700 km ... since 2026-08-16" -- retypes three store numbers and a
  ruling date in a website note (What a Visitor Reads, principles 3
  and 5).
- `solar_atmosphere/alfven_surface/about`: April 2021 (in its cited
  source); and the shape sentence "lower over the poles and higher over
  the streamer belt", the claim L-228 found backwards.
- `solar_wind/termination_shock/about`: 94.01 (the store holds it,
  TERMINATION_SHOCK_AU); Voyager 2's 84; "a few hundred kilometers a
  second".
- `orientation/note`: 7.25 degrees.

### S. A number the store already holds, typed again (no source hunt)

Printed through its row instead:
- Parker Solar Probe's closest approach typed as 8.8 R_sun in
  `outer_corona_info`, `outer_corona_info_hover`,
  `hover_text_sun_and_corona` and its tooltip. The store's
  PARKER_CLOSEST_RADII is 9.86, from the Sun's center; 8.8 is the
  altitude, the same error corrected on ALFVEN_SURFACE_RADII. The line
  "MAPS disintegrated at 8.33 R_sun, just inside Parker's record" is
  wrong as a result.
- The inner corona's "1-3 R_sun" in `hover_text_sun_and_corona` and its
  tooltip (INNER_CORONA_RADII).
- The helmets' 2-4 R_sun in `outer_corona_info` (HELMET_CUSP_LOW_RADII,
  HELMET_CUSP_HIGH_RADII).
- The radiative zone's 0.2 to 0.7 and 0.00325 AU, the photosphere's 0.7
  to 1 and 0.00465 AU (CORE_AU, RADIATIVE_ZONE_AU, SOLAR_RADIUS_AU;
  these meet L-386), and the chromosphere line's AU pair and depth
  printed by fixed widths (`CHROMOSPHERE_RADIUS_LINE`).
- The streamer band's 7.25 degrees in `band_hover` (the solar pole,
  `planet_poles`, a dict with no per-value rows -- not worked this
  session).
- The Roche formula's inputs in `roche_limit_info(_hover)`: 2.44,
  1,408 kg/m^3, ~500 kg/m^3 -- typed on ROCHE_LIMIT_RADII's
  Calculation lines, not rows (recorded on L-371).

### D. Statements out of date

- `solar_wind_info(_hover)`: "Both probes ... are currently exploring
  the heliosheath." Voyager 2 crossed the heliopause in 2018, Voyager 1
  in 2012.
- `streamer_belt_info`: "since 2026-08-22 it is no longer drawn as if
  it did" -- a ruling date in visitor text.

### N. The kinds L-411 names

- Voyager 2's 84 AU (`termination_shock_info(_hover)`, and on the
  website). Its comment credited it to Stone et al. (2005), which is
  Voyager 1's crossing only.
- Sedna's 936 AU (`gravitational_influence_info(_hover)`). JPL's
  Sun-centred elements today give its aphelion as 1,010 AU (SBDB,
  epoch 2461200.5); the 936 matches no fetched value, and which centre
  the orbit is taken around decides the number.
- The termination shock's "about 75 to 100 AU"
  (`termination_shock_info(_hover)`).
- "Wave motion out to 15 R_sun" in `band_hover` (DeForest et al. 2014's
  field-of-view floor).
- The temperatures: see T.

### T. Textbook physical figures (each needs a source or comes out)

- Temperatures: core 15 million K; radiative zone 7M to 2M K;
  photosphere ~5,500 K and 5778 K; chromosphere 4,000, ~6,000 to
  20,000, 10,000 K; inner corona 1-3M and 1-2M K, 1.5M K; outer corona
  and streamer belt ~1-2M K; heliosheath ~1,000,000 K; "200x hotter".
- Wavelengths worked out from those temperatures: 527.32 nm, ~290 nm,
  1.93 nm, ~1.159 nm, 2.897 nm.
- The core: 25% of the radius, 34% of the mass, 150 times water's
  density, 34% hydrogen and 64% helium (the same 34 twice: Bahcall et
  al. 2001 give the CENTER's hydrogen mass fraction as 0.340, which is
  not the core's share of the Sun's mass).
- Thicknesses: photosphere 500 km; chromosphere 2,000 km (1,200 mi).
- Speeds: 300-800 km/s; ~100 to 200 km/s past the shock.
- The corona's extents: "extends to 2-3 solar radii", "~2-3", "~2.3",
  the F-corona "beyond ~3" and "to ~15 R_sun", the E-corona "to ~2",
  the stalk "studied between 2 and 10".
- `hover_text_sun`: age 4.6 billion years, 5 billion more, 1.4 million
  km (865,000 mi), 109 Earths, 333,000 Earth masses, 73% and 25%,
  5778 K, 5,500 C, 10,000 F, 15 million C (27 million F), absolute
  magnitude 4.83; and three that are not facts about the Sun:
  "Distance: 0 pc", "Plotting marker size: 12 px", and "I've colored it
  chlorophyll green".
- The Oort cloud: "1-100 trillion objects >1km", "periods exceeding
  200 years", "about 2 light-years".

### M. MAPS C/2026 A1, observed event facts

Dates, times and distances of the comet's 2026 passage, in
`hover_text_sun_and_corona` and its tooltip, `alfven_surface_info(_hover)`,
`outer_corona_info_hover`, `inner_corona_info_hover`,
`roche_limit_info(_hover)` and `streamer_belt_info`: ~33 R_sun
(~0.15 AU) on April 2; the Alfven crossing April 3 ~18:00; break-up
April 4 08:15 at 8.33 R_sun (0.039 AU); perihelion April 4 14:22 at
1.23 R_sun (0.006 AU); ~36-40 hours outbound; dispersed by April 6;
~20 hours. Observations, so they migrate to the store with a source
(Observations Are Sourced Facts, and They Migrate).

### C. Comets that survived inside the Roche limit

`roche_limit_info(_hover)`: Ikeya-Seki (~5 km) at 1.66 R_sun
(0.008 AU); the Great Comet of 1843 at 1.19 R_sun (0.006 AU); Lovejoy
(C/2011 W3, ~500 m) at ~1.2 R_sun.

### Already cited in the string (citation details only)

Paper years and pages inside citations: Suess & Nerney 2004 (33:668),
2005; DeForest 2014 (787:124); Nesvorny 2025 (arXiv:2502.11252);
Cranmer 2023. These are not claims; they stay.

## Every string, with its typed digit runs

Counted by the pattern above, in source order within each string, at
the base named at the top (before this session's L-411 edits).

- `CHROMOSPHERE_RADIUS_LINE` (3): 5, 5, 0
- `gravitational_influence_info` (2): 160,000, 936
- `outer_oort_info` (1): 200
- `inner_oort_info` (1): 200
- `inner_limit_oort_info` (1): 200
- `hills_cloud_torus_info` (4): 2025, 3, 2025, 2502.11252
- `outer_oort_clumpy_info` (4): 1-100, 1, 2012, 113
- `galactic_tide_info` (4): 1-100, 1, 2012, 113
- `solar_wind_info` (7): 1, 2, 1977, 1, 1, ~1,000,000, 2.897
- `termination_shock_info` (5): 75 to 100, 1, 2, 84, ~100 to 200
- `outer_corona_info` (9): 2-4, 2004, 2023, 28,, 2021, ~1-2, ~8.8, 2024, ~1.159
- `inner_corona_info` (5): 1-3, 2-3, 1-2, 1.5, 1.93
- `chromosphere_info` (7): 2,000, 1,200, 4,000, 20,000, ~6,000 to 20,000, 10,000, ~290
- `photosphere_info` (6): 500, 0.7 to 1, 0.00465, 2, ~5,500, 527.32
- `radiative_zone_info` (4): 0.2 to 0.7, 0.00325, 7, 2
- `core_info` (9): 25, 34, 15, 150, 34, 64, 3, 3, 4
- `gravitational_influence_info_hover` (1): 936
- `outer_oort_info_hover` (1): 200
- `inner_oort_info_hover` (1): 200
- `inner_limit_oort_info_hover` (1): 200
- `solar_wind_info_hover` (7): 1, 2, 1977, 1, 1, ~1,000,000, 2.897
- `termination_shock_info_hover` (5): 75 to 100, 1, 2, 84, ~100 to 200
- `outer_corona_info_hover` (13): 2023, 28,, 2021, ~1-2, ~8.8, 2024, ~1.159, 2026, 1, 3, ~33, 2,, 2026,
- `streamer_belt_info` (22): 2026-08, 22, 2, 10, 2004,, 33, 668, 2005,, 11, 2-3, ~3, ~15, ~2, ~1-2, 2026, 1, 3, ~0.15, ~33, 2,, 2026, 3-4
- `roche_limit_info` (25): 2.44, 1, 3, 1,408, 3, ~500, 3, 1965, 1,, ~5, 1.66, 0.008, 1843, 1.19, 0.006, 2011, 3,, ~500, ~1.2, 2026, 1, ~8.33, 0.039, 1-2, 1.23
- `roche_limit_info_hover` (23): 2.44, 1, 3, 1,408, 3, ~500, 3, ~5, 1.66, 0.008, 1843, 1.19, 0.006, 2011, 3,, ~500, ~1.2, 2026, 1, 8.33, 0.039, 1.23, 0.006
- `alfven_surface_info` (13): 2023, 28,, 2021,, 1, ~5, 2023, 2026, 1, 3,, ~18, 00, 20, 1-2
- `alfven_surface_info_hover` (13): 28,, 2021, 1, ~5, 2023, 300-800, 2026, 1, 3,, 18, 00, ~20, 1-2
- `inner_corona_info_hover` (11): ~2-3, 1-3, ~2.3, ~3, 2026, 1, 1.23, 2-3, 1-2, 1.5, 1.93
- `chromosphere_info_hover` (7): 2,000, 1,200, 4,000, 20,000, ~6,000 to 20,000, 10,000, ~290
- `photosphere_info_hover` (6): 500, 0.7 to 1, 0.00465, 2, ~5,500, 527.32
- `radiative_zone_info_hover` (4): 0.2 to 0.7, 0.00325, 7, 2
- `core_info_hover` (9): 25, 34, 15, 150, 34, 64, 3, 3, 4
- `hover_text_sun_and_corona` (33): 1-3, ~1-3, 28,, 2021, ~8.8, 2024, 200, 2026, 1, 2026, 2,, ~33, ~0.153, 3, ~18, 00,, 3, 4, 08, 15,, 8.33, 0.039, 4, 14, 22,, 1.23, 0.006, ~36-40, 6, 8.8, 0.041, 8.33, 0.039
- `hover_text_sun_and_corona_tooltip` (33): 1-3, ~1-3, 28,, 2021, ~8.8, 2024, 200, 2026, 1, 2026, 2,, ~33, ~0.153, 3, ~18, 00,, 3, 4, 08, 15,, 8.33, 0.039, 4, 14, 22,, 1.23, 0.006, ~36-40, 6, 8.8, 0.041, 8.33, 0.039
- `hover_text_sun` (20): 4.6, 5, 1.4, 865,000, 109, 333,000, 73, 25, 5778, 5,500, 10,000, 15, 27, 4.83, 2, 1.000000, 1.00, 0, 0, 12
- `create_sun_chromosphere_shell() / shell_trace / name=` (1): 2,000
- `create_sun_chromosphere_shell() / info_trace` (2): 2,000, 2,000
- `create_sun_hills_cloud_torus() / hills_hover` (3): 2025, 2025, 2502.11252
- `create_sun_streamer_band() / band_hover` (14): 2004, 33, 668-675, 2014, 787, 124, 15, 0, 6, 11, 7.25, 2018, 15, 224
