<!-- Doc-Kind: hand | Design record for the design talks of 2026-10-20 (a design session, zero code): each talk's ruling in Tony's words, with what was read to put the question. -->
# The design talks of October 20, 2026: rulings

Built on orrery e8e714da99e0ec102fe179341cf767458d2e8545 at
https://github.com/tonylquintanilla/palomas_orrery ("L410 sun fades
close and cleanup") and gallery ca5339fd3c22d61a1540e4314726e85003e48751
at https://github.com/tonylquintanilla/tonyquintanilla.github.io ("L 410
fixture hovers"). Both read with `git ls-remote` at session start,
17:05 Chicago time: neither had moved, so the L-456 patches were unrun.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

- Type: DESIGN SESSION (zero code). Talk only, by Tony's word: "This
  is a talk only session. No builds to avoid conflicts."
- Follows the brief Tony attached, written by Claude Fable 5.1 at
  4:33 pm. Tony asked to start with its item 3.
- Skills loaded, each matching the manifest at e8e714d:
  ledger-and-session-records 1.21, provenance-discipline 2.32 (its
  reference `figures.md` read), orrery-coding-conventions 1.11, and
  interactive-exhibit 1.17 from talk 2 on.
- No ledger or Where We Are patch was built: by the brief's section 1,
  it waits until Tony has run `patch_L456_2_session_close_20261020.py`
  and pushed, and is then built on that new HEAD. Until it lands, the
  rulings below are not recorded (the document stack rule).

## Talk 3. L-401's two open questions (the orrery's distance digits)

### (a) A number from a model with no stated accuracy: the analytical Moon's average distance

What was read (orrery at e8e714d):
- `idealized_orbits.calculate_moon_orbital_elements` types
  `a = 0.002570  # AU (384,400 km)`, with no source line. Nothing is
  worked out: it is one typed number. 0.002570 AU converts to
  384,466.5 km, so the comment and the value disagree by 67 km.
- `plot_moon_ideal_orbit` prints it through
  `position_accuracy.au_text` in the no-error state, "not_from_jpl":
  the whole-kilometre floor gives "a=0.00257000 AU", then "No accuracy
  is stated for this position, so distances are shown to the whole
  kilometer." The trailing zeros claim kilometre precision a
  four-figure number does not have.
- NASA NSSDCA, "Moon Fact Sheet",
  https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html, read
  2026-10-20 by Claude Opus 5.5: "Semimajor axis (10^6 km) 0.3844";
  the same table prints "Orbit eccentricity 0.0549" and "Inclination
  to ecliptic (deg) 5.145". Open, so it meets the Access Standard.

Options put: A, source it and print its own figures; B, keep the
kilometre floor and change only the sentence; C, remove the distance
from this hover.

Tony asked: "Do we need sources for option A?" Answered: one, the Fact
Sheet, already opened; nothing goes on his reading list and no outside
check is needed.

**Ruling, Tony, 2026-10-20: "A".**

What it means for the build (when the file is next opened; L-401
build 3 stays parked, each part with its feature):
- A row in `constants_new.py` for the Moon's mean semimajor axis in
  kilometres, cited to the Fact Sheet line, with `# Read:` naming the
  reader and date, and its figures (four, the source prints 0.3844 x
  10^6 km). The AU value is computed from it, never typed.
- The hover prints "a = 384,400 km (0.002570 AU)", each unit by its own
  Report test of the row's figures, and the sentence, offered in
  these words: "The Moon's average distance from Earth, from NASA's
  Moon Fact Sheet. This orbit is an average shape, not a measured
  position." The final wording goes to Tony side by side before it
  ships (orrery-coding-conventions, Hover Text Is Written for the
  Visitor).
- Method, to provenance-discipline's `references/figures.md` at its
  next version: a number taken from an average model prints to its
  source's figures; the whole-kilometre floor is kept for positions
  JPL gives without an error.

### (b) Computed numbers that are not distances or speeds

What was read (orrery at e8e714d, `idealized_orbits.py`):
- The analytical Moon's e prints `{e_ana:.6f}` and its i `{i_ana:.2f}`.
  e is a typed mean 0.0549 plus a typed evection term 0.01098 times a
  cosine, both unsourced; i is a typed 5.145. The Fact Sheet line read
  for (a) prints both means, 0.0549 and 5.145.
- The osculating-against-mean comparison box prints
  `Delta-e: {delta_e:+.8f}` and `Delta-i: {delta_i:+.4f} deg`, from
  Horizons' osculating elements and the typed mean elements in
  `orbital_elements.py`.

Claude first put this as a choice of WHEN (three options). Tony: "I
am unclear on the conflict." There was none: the rules already
exist (`references/figures.md` Rules 2, 3 and 7: a typed number keeps
its source's digits, a difference keeps the coarser decimal place,
a display never prints more or fewer than the row declares), and
nothing here is drawn on the website, so by The Braid each waits for
its file to be opened.

**Ruling, Tony, 2026-10-20**, asked whether to record (b) as method
rather than a ruling of his: "Yes, and by the braid rule we should do
this in the Moon slice, correct?" Confirmed.

What it means:
- METHOD, not a ruling: these numbers print by the existing digit
  rules; nothing new goes into the skill for them.
- The analytical Moon's three numbers (its distance from (a), its
  eccentricity and its tilt) are fixed together, in the Moon's
  slice. That slice is not yet a stage on the road; L-355's Gap
  already names "the Moon's slice" after Earth's Stage D. The close
  patch puts a line on L-401 so that slice finds this work.
- With the Fact Sheet's four-decimal mean, the Moon's e prints to four
  decimals; its i prints 5.145 deg, one digit more than today.
- The comparison box's Delta-e and Delta-i go with the parameters
  window, L-401 build 3's first part, which needs the same reading of
  each body's mean elements for their digits.

Talk 3 is closed: L-401's two open questions are answered.

When the Moon's slice comes is not decided. Tony, 2026-10-20: "I have
not decided when to do the moon slice. Probably after the symbols
integration into the website." Recorded as his leaning, not a ruling;
the close patch does not put a Moon stage on the road.

Then, on the order of the talks: "let's move to item 1 then in order."

## Talk 1. The chromosphere's new words (L-411, the typed numbers left in the Sun's hovers)

### What was there (orrery e8e714d, gallery ca5339f)

- Website, the chromosphere's "about" (`data/objects_config.json`):
  "its temperature rises with height, from about 6,000 kelvin at the
  bottom to about 20,000 at the top." Its citation is NASA/Marshall's
  chromosphere page, which gives degrees Celsius.
- Orrery, `chromosphere_info` and `chromosphere_info_hover` in
  `solar_visualization_shells.py`, which disagree with each other: "from
  around 4,000 Kelvin at the photosphere to about 20,000 Kelvin at the
  inner corona", and "Temperature: ~6,000 to 20,000 K, for a average of
  10,000 K" with "Radiates at an average peak wavelength of ~290 nm",
  the wavelength worked out from the unsourced average.

### What was read, in order (all 2026-10-20, Claude Opus 5.5, through the chat's web-fetch tool)

1. NASA NSSDCA, "Sun Fact Sheet" (D. R. Williams, last updated 9 May
   2024), https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html:
   "Temperature at top of photosphere: 4400 K"; "Temperature at bottom
   of photosphere: 6600 K"; "Temperature at top of chromosphere:
   ~30,000 K"; "Chromosphere thickness: ~2500 km". It names NO source
   for any temperature: no references, and its one footnote is on the
   rotation period.
2. Yohkoh Public Outreach Project, Montana State University Solar
   Physics, "Things are heating up again",
   https://solar.physics.montana.edu/YPOP/Spotlight/SunInfo/Transregion.html:
   20,000 K "in the upper chromosphere"; the transition region "about
   100 km thick". No date, author or references.
3. Hathaway, D. H., NASA/Marshall Solar Physics, the chromosphere page,
   https://solarscience.msfc.nasa.gov/chromos.shtml (dated August 11,
   2014; last updated January 14, 2025): "the temperature rises from
   6000 degrees C to about 20,000 degrees C". No references.
4. Carlsson, M. (Institute of Theoretical Astrophysics, University of
   Oslo), "Modeling the Solar Chromosphere", arXiv:0704.1509,
   https://arxiv.org/pdf/0704.1509, read twice, the two reads agreeing.
   Sect. 1: the early one-dimensional models have "a temperature
   falling to a minimum around 4000 K about 500 km above the visible
   surface", a rise to about 8000 K at about 2000 km, then a very rapid
   rise to coronal temperatures. Sect. 2, the VAL3 models (Vernazza,
   Avrett and Loeser 1981): the minimum near 500 km, about 6000 K at
   1000 km, about 7000 K at 2000 km, then a very steep rise; "a
   temperature plateau introduced between 20000 and 30000 K" to
   reproduce the Lyman lines' total flux, which "was no longer
   necessary in the FAL models". The read was through the fetch tool's
   summary, not the PDF's bytes (the sandbox cannot reach arXiv); the
   build re-opens it before writing the rows.
5. Rutten, R. J., "The Quiet-Sun Photosphere and Chromosphere",
   arXiv:1110.6606: the chromosphere "does not stand for a spherical
   shell but for a thin, very warped and highly dynamic interface
   surface"; the VAL3C temperature minimum at h = 500 km; the
   transition region at h = 2100 km. No temperatures.

### How the question moved

- Claude's first draft used the Fact Sheet for both ends: 4,400 K at
  the bottom, about 30,000 K at the top.
- Tony: "Should we ask Gemini for a cross check? How do we judge
  between these sources?" Claude: no new relay (Gemini's check of
  2026-10-19 is what found this, and it had misquoted the Fact Sheet),
  and offered the top as a range, 20,000 to 30,000.
- Tony: "Is this a range or a disagreement among sources. Which is more
  current? What is the fact sheet's source?" Claude: a disagreement;
  the range was Claude's explanation, not the sources'; page dates are
  edit dates, not measurement dates; the Fact Sheet names no source,
  and neither do the other two. Recommended finding the primary source
  before writing words.
- Tony: "Yes let's look for the primary source. I'm surprised these
  fact sheets do not provide sources." The search found the models the
  figures come from (read 4 and 5 above). The 20,000 to 30,000 K the
  summary pages call "the top" is the old model's plateau at the foot
  of the steep climb to the corona, which later models dropped; through
  almost all of the chromosphere the models stay under about 7,000 K.

### Ruling, Tony, 2026-10-20: "Approved."

The words, as drafted from Carlsson (2007):

- Website: "its temperature rises with height, from about 4,000 kelvin
  at the bottom to about 7,000 near the top, and then climbs steeply
  into the much hotter corona." The sentence's citation moves from
  NASA/Marshall's page to Carlsson (2007), with its open address on the
  Source line (provenance-discipline 2.32).
- Orrery, the longer sentence: "from about 4,000 Kelvin at its bottom
  to about 7,000 Kelvin near its top. Above that it climbs steeply into
  the corona, which is far hotter."
- Orrery, the summary line: "Temperature: about 4,000 K at the bottom
  to about 7,000 K near the top." The unsourced 10,000 K average and
  the ~290 nm wavelength worked out from it are removed (words a person
  wrote, so Tony's to approve; approved with the draft).
- The two numbers print from two new rows in `constants_new.py`, in
  kelvin (2.31), each cited to Carlsson (2007) with its section, a
  `# Read:` line, and one figure each.

Then, Tony: "But why do we say 'much hotter' instead of 1,000,000 K".
Claude offered the corona's measured row, CORONA_TEMPERATURE_MAX_K
(up to 2 million, NASA Science "Sun: Facts"), and not
CORONA_MODEL_TEMPERATURE_K (1.18 MK, a setting of the density model,
which its own row says is not a measured temperature). Tony: "I forgot
we were Talking about the chromosphere not the corona." Asked whether
to keep the approved words, with "much hotter": **"Yes"**. The
corona's own words carry its temperature; the chromosphere's sentence
carries only the chromosphere's numbers.

### Captured, not decided

- **A colour for the corona's fade, set by its temperature** (Tony,
  2026-10-20: "add a 'black body' color element to the corona fade to
  conform with its temperature"). A talk of its own, on the Sun's list
  (L-412) beside L-410. Claude's caution for that talk, from its own
  knowledge and to be sourced there: the corona's visible light is
  mostly sunlight scattered by its electrons plus a few emission lines,
  not the glow of a hot body, so a colour set by temperature could
  state something untrue.
  SETTLED THE SAME EVENING. Tony: "Question: stars vary in color by
  temperature why not the corona?" Claude: a star's surface is dense
  and opaque and glows with a temperature colour; the corona is thin
  and nearly transparent, its own light mostly X-rays and ultraviolet
  at particular wavelengths, and its white light at an eclipse mostly
  the Sun's own light scattered by its free electrons (Claude's own
  knowledge, unsourced, not for a visitor). Tony: "So basically the
  light is scattered sun light not its own light? Keep as is."
  **Ruling, Tony, 2026-10-20: the corona's colour is kept as it is;
  no temperature colour.** Nothing goes on L-412 for it.
- **For provenance-discipline, proposed as method** (not yet ruled
  whether it is method): an agency summary page that names no source
  for a figure is read one layer down, to the scientific work the
  figure comes from, before the figure becomes a row. Three agency
  pages tonight gave three answers and named no source between them.
  To Tony at the close: "is this mine or the skill's?"
- The Fact Sheet's "Chromosphere thickness: ~2500 km" beside our
  2,000 km: the depth is not this talk (it changes with the
  chromosphere's shell, and Gemini 4 noted 1,000 to 5,000 km across
  sources). Not chased.

## Talk 2. The galactic tide on the phone (L-412, the Sun's list; from L-408 at its close)

### What was read (gallery ca5339f, orrery e8e714d)

- A correction to the brief: the website draws NO cone.
  `feature_renderers.js` draws the tide (`tide_field`,
  `tideFieldPoints`) as dots only, from its own seeded random numbers,
  with the served drawing block of `data/objects_config.json`:
  `n_points` 2000, `opacity` 0.3, `marker_size` 1.2. The cone and the
  brighter tide are the ORRERY's, from L-420 (2026-10-06; Tony's
  "brighter plus cone"): 5,000 points at twice the size and twice the
  opacity, and a faint pink double cone between the Oort cloud's two
  edges at the latitude where |sin b cos b| peaks, worked out as
  arctan(1). Tony's look at the orrery, 2026-10-07: "images look great
  at 5000. the X is clearly visible even without the cone", and "I
  think the cone is useful to illustrate the tidal influence as
  physics." Its approved hover line: "The pink cone marks that halfway
  line, where the tide changes comets' orbits the most."

### Tony's look (Mode 5), 2026-10-20, 18:35, iPhone, portrait, the Sun room, the tide ticked

"By trial and error one can visualize the X more or less but one needs
to look for it. The orrery's drawing is more clear." His screenshot
shows the faint 2,000 dots about the axes, with no X at that angle.

### Ruling, Tony, 2026-10-20: "Yes"

To: "Shall the phone's tide take the orrery's look, brighter and with
the pink cone?" So the website's tide takes the orrery's L-420 look:

- the orrery's dots, 5,000 at twice the size and opacity (how they
  reach the phone is talk 5's question: a stored drawing or the
  website's own draw);
- the pink double cone, which is a few served numbers and a formula
  (the two edges, the served galactic pole, the angle where the tide
  peaks), so the website works it out itself and it is not stored
  (Tony's rule of 2026-10-11, L-434);
- the hover line already approved for the orrery.
The website's tide hover then goes to Tony with old and new side by
side before it ships (Hover Text Is Written for the Visitor). The
cone's angle prints from the same working as the orrery's, never typed.
Whether the cone needs a hover of its own: the orrery names it in the
tide's hover with one line; the phone follows the orrery unless his
look at the build says otherwise.

## Talk 4. The Solar System room (L-363): the highlighted row; GO's arrow

### (a) The highlighted row

What was read (gallery ca5339f): the room's drawer rows are served in
`data/objects_config.json`, `"rooms"`, in order outward from the Sun
(Sun, Mercury, Venus, Earth, Apophis behind See more, Mars, Jupiter,
Saturn, Uranus, Neptune, Pluto); `gallery/solar_system_drawer.js` keeps
them in served order; `interactive.html` has no scroll to the
highlighted row when the drawer opens.

Options put: A, keep the outward order and scroll the highlighted row
into view near the top when the drawer opens; B, pin the highlighted
row at the top, so every name tap moves its row.

**Ruling, Tony, 2026-10-20: "A. That's what I was thinking of not B
that would be confusing."** The order stays outward from the Sun; the
drawer scrolls so the highlighted row is in view when it opens. Page
chrome only, no served data; a shared-chrome change, so the Sun and
Earth rooms are checked by the headless comparison and the phone.

### (b) An arrow from Go To's text box to its body

Settled before the talk: Tony, 2026-10-04: "the text box needs to
remain in the center. if not possible, don't implement the arrow."

What was read (gallery ca5339f, `interactive.html`): `sunLabelShow`
makes the upright phone's box a page annotation (`xref`/`yref`
"paper"), centred, `showarrow` false (L-318 round 5); elsewhere a scene
annotation with Plotly's own arrow, which places the box beside its
point, which is why the earlier arrow moved the box. The HUD already
reads the live camera every frame (`sunHudWatch`, `getCamera`) and
redraws page chrome from it.

Put to Tony, with a sketch: the page draws the line itself, from the
centred box's edge to the body's place on screen, redrawn from the
live camera as the HUD is; hidden when the body is off screen or
behind the box; upright phone only (the desktop and a sideways phone
keep Plotly's arrow). Moderate new page drawing, judged only on the
phone.

**Ruling, Tony, 2026-10-20: "Yes, as recommended".** This supersedes
nothing: the box stays centred, as ruled on 2026-10-04, and the line
is drawn by the page. Shared chrome, so the Sun and Earth rooms' upright
text boxes get it too unless the build says otherwise; the
headless comparison and the phone check every room.

Talk 4 is closed: L-363's Gap (c) is answered.

## Talk 5. Stored drawings for the other scattered-dot shapes (L-434)

Settled before the talk (Tony, 2026-10-11, "Confirmed as recommended"):
stored drawings for shapes drawn as dots scattered by random numbers or
a model; not for shapes that are a few numbers and a formula.

What was counted (gallery ca5339f, orrery e8e714d):
- The galactic tide: the website draws 2,000 dots
  (`tideFieldPoints`, served `n_points`); the orrery 5,000
  (`create_sun_galactic_tide`), unseeded, fresh each run. Talk 2 gives
  the phone the orrery's 5,000: about 80 kB stored.
- The Oort cloud's clumps: 15 clumps of 50 to 200 dots, about 1,900,
  both sites (`create_sun_outer_oort_clumpy`, unseeded in the orrery):
  about 30 kB stored.
- The streamer band, on the corona's row: a grid set by about twenty
  served numbers (`streamerBandPoints`), 4,332 dots, each with a small
  random jitter in radius and latitude. Not random scatter.
- Sizes measured against the served drawings: `hills_cloud.json`
  58,250 bytes for 3,600 dots; `sun_corona.json` 61,266 bytes for
  2,500 dots with weights.

Put to Tony: by his rule the tide and the clumps qualify, and storing
them also settles the orrery's unseeded draws (L-239); the streamer
band is the formula case and stays drawn by the website. This departs
from the brief's recommendation, which put the band first.

**Ruling, Tony, 2026-10-20: "Confirmed".** The galactic tide and the
Oort cloud's clumps become stored drawings, together; the streamer band
(L-224) stays worked out by the website from its served numbers. The
tide's stored dots are the orrery's 5,000 of L-420, so talk 2's
brighter look and this build are one build; its cone is computed by the
website. When the build comes is the road's: the Sun's slice (L-412).

## Talk 6. Earth's talk 2: the field, its offset, and edges that move (L-356, L-375, L-454; on L-413, Earth's list)

Said to Tony first: Earth's builds wait behind the Sun's slice by his
ruling of 2026-10-17; the talk is held, the builds wait unless he says
otherwise. The talk's own brief is section 5 of
`documentation/HANDOFF_earth_fade_build_20261017.md`.

### (a) L-356: IGRF-14

What was read: NOAA NCEI / IAGA, "14th Generation International
Geomagnetic Reference Field Schmidt semi-normalised spherical harmonic
coefficients, degree n=1,13",
https://www.ngdc.noaa.gov/IAGA/vmod/coeffs/igrf14coeffs.txt, read
2026-10-20 by Claude Opus 5.5 through the web-fetch tool. Columns
2020.0, 2025.0 and 2025-30 (SV), nT and nT per year:
g 1 0 -29403.41, -29350.0, 12.6; g 1 1 -1451.37, -1410.3, 10.0;
h 1 1 4653.35, 4545.5, -21.5. (IGRF-13's 2020 values in the store:
-29404.8, -1450.9, 4652.5; its forecast drift 5.7, 7.4, -25.9.)
Worked by Claude from the 2025.0 column, by the store's own
expressions: the dipole tilt about 9.21 degrees (9.41 from IGRF-13
for 2020); its rate about -0.041 degrees per year. The printed counts
come from the rows' figures at the build, not from this note.

**Ruling, Tony, 2026-10-20: "Confirmed and it can be done when
convenient."** The six rows are re-sourced to IGRF-14's 2025.0 column
and its 2025-30 drift, with `# Read:` lines; the hovers say "for 2025
(IGRF-14 model)". Method decides the names (the rows' IGRF13 in their
names goes with the re-sourcing) and the counts. Timing: Tony's
"when convenient" lifts it out of the wait behind the Sun's slice, as
the ledger's note of 2026-10-17 offered: a small build of its own,
on any evening.

### (b) L-375: the offset of Earth's magnetic centre

What was read: Koochak and Fraser-Smith (2017) could not be reached
(the search found no open copy). Read instead, 2026-10-20 by Claude
Opus 5.5 through the web-fetch tool: Laundal, K. M. and Richmond, A. D.,
"Magnetic Coordinate Systems", Space Science Reviews (2017),
arXiv:1611.10321, https://arxiv.org/pdf/1611.10321, Sect. 3.3
"Eccentric Dipole (ED) Coordinates": the Schmidt eccentric dipole has
the centred dipole's size and direction, its centre placed to minimise
the n = 2 terms, from the first eight Gauss coefficients; with IGRF-12
for 2015 "the shift of the eccentric dipole away from the center of
the Earth is delta = RE sqrt(eta^2 + zeta^2 + xi^2) ~ 576.8 km" (Eqs.
23 to 28); "Since 1950, the eccentric dipole ... has moved away from
the center of the Earth at an almost constant speed of ~ 2.5
km/year." Koochak and Fraser-Smith stay on Tony's reading list for
his machine, not needed for the ruling.

Put to Tony: the offset is fixed to the ground, so its direction in
space turns once a day with a rotation phase neither instrument
models; at about a tenth of Earth's radius the centre lies inside the
opaque globe, and at the belts' scale it is a speck. Options: A, say
it in the dipole's hover in words, the figure worked out from IGRF-14
by the paper's formula; B, draw the envelope (a ring of every place
over a day), which needs a see-through globe; C, leave it out.

**Ruling, Tony, 2026-10-20 (23:05): "A".** The dipole's hover gains
one sentence: the field's centre sits about N km from Earth's centre,
turning with Earth, with N worked out from IGRF-14's 2025.0
coefficients (degree 1 and 2, the first eight) by Laundal and
Richmond's Eqs. 23 to 28, a derived row in `constants_new.py` cited to
the paper and the coefficient file; not typed, not the 2015 figure.
Rides with (a)'s IGRF-14 build. Nothing is drawn for it. The hover's
words go to Tony side by side before they ship.

### Stopped here: (b)'s second half and (c)

At 23:05 the session context showed the protocol at v3.106 and the
manifest at interactive-exhibit 1.18: `git ls-remote` read orrery
23f708869e8d2b06bb5e206574a8c9b59d3d2cfa ("L456 session close and
Gemini worksheet") and gallery
4778944fabd68099af119b91703562d5f3361c3f, and the repo's
`skills/interactive-exhibit/SKILL.md` read "Skill version: 1.18".
This session had loaded 1.17. The two questions left -- whether the
website draws the dipole cone (L-375's second half), and the device
for edges that move (L-454) -- decide what the Earth room draws, which
is that skill's work, so the Stale Skill gate stopped them. Tony,
asked whether to close and carry them: "yes, please give me the
handoff. thanks. good talk session."

The rulings of talks 2, 4 and 5 were made under 1.17, which was the
manifest's version when they were made.

Session record written October 2026 with Anthropic's Claude Opus 5.5.
