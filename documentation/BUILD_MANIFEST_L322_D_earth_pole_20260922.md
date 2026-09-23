# Build Manifest -- L-322 Stage D: Earth's pole moves into constants_new.py (rev 2)

**Built on orrery `751aff3f416b22d534578677191d1492b5b41b31`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `36ef1727ca22fcc51badebad052a1a322b650dd1`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both HEADs were read live with `git ls-remote` on 2026-09-22 and both
repositories were cloned there. Every line number below was read on
those clones.** **Re-anchored for rev 2 on 2026-09-23:** both remotes
moved, orrery to `ac25d4f44a0607f734fdf98f21095e869abe790b` (one run
record under `documentation/`) and gallery to
`2e0fa8f5de7ec1dc99597dc302e4e4c4eb745e72` (L-303 card work and a
nightly cache build). Of the files Stage D edits, only
`data/solar-system/coverage_index.json` moved, and the cache build
rewrites it. Both clones were moved to those HEADs and every test in rev
2 ran there. The build session re-anchors again.

**Rules this work runs under.** Inside Tony's Project the protocol
(v3.67) and the skills load on their own. This task fires
provenance-discipline 2.17, ledger-and-session-records 1.11,
interactive-exhibit 1.4, gallery-cache-builder 1.6, gallery-assembler
1.3, horizons-orbital-mechanics 1.1, orrery-coding-conventions 1.9,
safe-file-editing 1.11 and agentic-pre-test 1.2. All eleven installed
skills were byte-compared with `skills/` at `751aff3f` on 2026-09-22 and
are identical, so the 2.17 obligation from v3.67 is discharged. A reader
outside the Project fetches `PROJECT_INSTRUCTIONS.md` and
`skills/<name>/SKILL.md` for each of those from the orrery at
`751aff3f`. **In your first reply, name the rule files you actually
read.**

**Type: BUILD CONTRACT.** Written before the build, zero code.
**Prepared:** September 22, 2026 by Claude Opus 5.5, Tony Quintanilla
integrator. **Opens from** `documentation/HANDOFF_L322_C2_built_20260922.md`,
section 4 item 3. **Handle:** L-322 Stage D, which bundles all of
L-311, the obliquity and the rotation period (section 3 says why).
**Revised** the same day after Tony's rulings on the first draft;
section 3 records them. **Rev 2**, 2026-09-23, answers Claude Fable
5.1's review (`REVIEW_L322_D_manifest_fable_20260923.md`); section 11
gives each finding its disposition. Rev 2 also uses the files' formal
names where rev 1 said "the store", on Tony's instruction of
2026-09-22.

Who this is written for: Tony, a retired professional engineer who is
not a programmer, and the session that builds it. Terms are explained
where they first appear.

---

## 1. What Stage D is, in one paragraph

Earth's rotation pole is typed as a pair of numbers inside
`idealized_orbits.py`, outside `constants_new.py`, so the gallery's
checks list it as "not a top-level constant in the store". It draws the
axis of a closed room, so it owes the four fields every closed-slice row
carries: unit, status, figure count and a read of its source. The
handoff expected a rate-and-angle row. Reading the cited source changed
that: the paper cited for Earth's pole does not contain it, and the pair
of numbers turns out not to be a measurement at all. It is the drawing
frame's own axis. What actually tilts Earth's axis in both drawings is a
second number, the angle between the equator and the ecliptic, and that
number is typed twice under the wrong name. Stage D puts both into the
`constants_new.py`, adds Earth's rotation period to the hover from a rate that file
already holds, corrects the citations a visitor can see. The axis does not move.
What does move, after Tony's rulings of 2026-09-23, is Earth's
magnetosphere in the orrery and the radiation belts in both drawings:
every number there chosen by eye is replaced by sourced rows.

## 2. What was measured

### 2.1 The cited paper does not contain Earth's pole

Every Earth pole citation in both repositories names the IAU working
group report of 2015, Archinal et al. (2018), Celestial Mechanics and
Dynamical Astronomy 130:22. The report was OPENED on 2026-09-22 by
Claude Opus 5.5 from the USGS reprint at
https://astropedia.astrogeology.usgs.gov/download/Docs/WGCCRE/WGCCRE2015reprint.pdf.
What it says about Earth, in four places:

- The abstract, page 2, says the approximate expressions for the Earth
  were removed from this edition.
- Table 1, pages 8 and 9, lists the Sun and the planets. Earth is not
  in it. Footnote 2, page 9, says the earlier expressions were
  inaccurate, failed near the year 2000, and that users should go to
  the IERS (the International Earth Rotation and Reference Systems
  Service) for Earth.
- Table 2, page 10, lists Earth's satellite as "See Sect. 3", and
  Section 3, page 14, says the old closed formulae for the Moon's pole
  are no longer given.
- Section 10, item 2, page 39, repeats that Earth's expressions were
  removed.

So a citation to this report for Earth's pole is a citation to a paper
that says, in print, it no longer gives one. That is the failure the
protocol names wrong-but-cited, and it is visible to visitors: the
room's information panel prints the gallery's source string as
"Source: ...". The same report also has no Earth rotation angle, so the
room's line crediting the sense of rotation to "Earth's prime-meridian
angle W" in that report is wrong in the same way. The report's
GENERAL definition, that a body whose angle W increases with time turns
prograde, is real and is in Section 2, page 6.

The sites that carry the citation:

- `idealized_orbits.py` lines 50 to 60: the dict comment and the Earth
  and Moon entries.
- `data/objects_config.json` line 862 (gallery): Earth's orientation
  source string.
- `gallery/earth_geometry.js` line 265: the axis marker's source, which
  reaches the panel.
- `data/solar-system/feature_configs.json` and `coverage_index.json`:
  served copies, rewritten by the next cache build.

### 2.2 What Earth's pole actually is in this project

Both drawings place everything in the frame JPL Horizons calls the
ecliptic of J2000. The Horizons manual
(https://ssd.jpl.nasa.gov/horizons/manual.html, opened 2026-09-22)
says that frame is built from the ICRF (the International Celestial
Reference Frame, the radio-source frame astronomers' coordinates are
tied to) by a fixed tilt of 84381.448 arcseconds, the IAU 1976 value.
Horizons' own output headers describe the frame's z-axis as pointing
in the sense of Earth's north pole at the reference epoch.

So Earth's pole at the year 2000 sitting at right ascension 0, declination
90 is not a measured value. It is the ICRF's own z-axis, which by
construction is Earth's mean pole of the year 2000 to within a very small
offset that the IERS Conventions (2010), Technical Note 36, chapter 5,
describe. That is where the working group sends users for Earth, and the
`constants_new.py` already cites that document for Earth's radius. The builder opens
chapter 5, reads the size of that offset, and states it on the row. This
manifest does not state the number because it was not read here.

The consequence for the fields: the pole rows are exact, as a
definition is, not measured and not derived.

### 2.3 The number that actually tilts the axis

With the pole on the ICRF z-axis, the tilt both drawings show is
exactly the frame's tilt. The code computes 23.439290999999994 degrees;
84381.448 / 3600 is 23.439291111. The two agree to the seven decimals
typed. Where the number lives:

- `idealized_orbits.py` line 3352: `np.radians(23.439291)`, labelled
  "IAU 2006".
- `gallery/feature_renderers.js` line 74: `23.439291`, labelled "IAU
  2006", and every gallery room's pole passes through it.
- Printed as `'23.44 deg'`, typed text, in `PLANET_ROTATION['Earth']`,
  `planet_visualization_utilities.py` line 531 (the orrery's axis
  hover).
- Printed as `tiltDeg.toFixed(2)` in `gallery/earth_geometry.js`
  around line 258 (the room's axis hover).

The value is right and the label is wrong. The value matches the
Horizons frame, which is the one that matters, because this rotation
must match the frame the positions were delivered in. No IAU 2006
document was opened, so this manifest makes no claim about what that
standard's value is; it only says the label names a standard nobody
checked. L-311 already records that the obliquity is not served.

### 2.4 Who reads the pole

Orrery, all through `create_planet_transformation_matrix('Earth')`:

- `earth_visualization_shells.py` line 1098, via `orient_to_planet_pole`:
  the radiation belts.
- `planet_visualization_utilities.py`, `build_rotation_axis_traces`:
  Earth's axis line and spin arrows.
- `planet_visualization_utilities.py`, `build_dipole_cone_traces`: the
  dipole cone, hung on the pole.
- `idealized_orbits.py` `debug_planet_transformation`: dead code by its
  own comment, reads the dict.

Gallery:

- `gallery/feature_renderers.js` `poleBasis`, called by
  `gallery/earth_geometry.js` `build`: the axis, the equator ring, the
  geostationary tilt.
- `tools/mirror_constants.py`: reports the four `planet_poles` links as
  ABSENT.
- `tools/test_mirror_constants.py` line 373: asserts Earth's link is
  ABSENT. This test must change in the same patch.
- `gallery_maintenance_run.py` line 950: lists it NOT IN STORE.

### 2.5 The other pole entries, discovery only

The pole dict moves into `constants_new.py` in this stage (section 4.2), so it
was compared with Table 1 of the opened report at the year 2000. The
Sun, Venus, Mars (once its periodic terms are evaluated), Jupiter,
Saturn and Pluto agree within the report's own stated accuracy of about
a tenth of a degree. Four do not:

- Mercury: declination 61.45 against the table's 61.4155.
- Uranus: 257.43 and -15.10, which are the table's values for Uranus's
  moons; Uranus itself is 257.311 and -15.175.
- Neptune: 299.36 and 43.46 drop a periodic term; the full expression
  gives 299.33 and 42.95.
- Moon: cites a table row that now reads "See Sect. 3".

The dict comment says six entries "cross-check exactly against the same
IAU table". For Uranus and Neptune that is false. None of this is fixed
here; section 7 records it.

### 2.6 Where the gallery still holds numbers of its own

Tony, 2026-09-22: "the store (constants_new.py) serves the orrery. the
orrery serves the gallery. the gallery should not have a separate
store." The path that is meant to carry every number is:
`constants_new.py`, then `export_constants.py` writes
`data/constants_export.json` in the orrery, then
`tools/pull_constants_export.py` copies that file into the gallery at a
named orrery commit, then `tools/mirror_constants.py` writes the values
into `data/objects_config.json`, then the cache build serves them to the
page. Measured on gallery `36ef1727`, four kinds of number reach the
page some other way:

- **Typed in the page code, no check:** `KM_PER_AU` and the obliquity,
  `gallery/feature_renderers.js` lines 70 and 74. Stage D removes both.
- **Links the export cannot serve yet, 24,** because the `constants_new.py` row has
  no unit line, so the config keeps a hand-typed copy (the mirror calls
  these FALLBACK): Sun rows (the radius, chromosphere, coronae, helmet
  cusp, Alfven surface, radiative zone, core, heliopause, termination
  shock, gravitational influence, solar radius in AU), the Oort cloud
  rows, `JUPITER_EQUATORIAL_RADIUS_KM` and `ROCHE_LIMIT_RADII`. Each
  closes in its own body's slice.
- **Links that point outside `constants_new.py`, 5:** the four `planet_poles`
  entries and the galactic tide's default. Stage D takes Earth's.
- **Numbers in the config with no link at all, 82:** Jupiter 18 and
  Saturn 14, all ring radii and thicknesses, which are measurements
  typed only in the gallery; the Sun 43, not yet sorted into drawing
  choices and measurements; Earth 7, all declared drawing choices (the
  magnetotail drawn to 100, 15 and 25 Earth radii, its opacity, the
  belts' thickness, ring count and point count). The skill keeps
  drawing choices out of `constants_new.py`, but Earth's seven are typed a
  second time in `earth_visualization_shells.py`, so the orrery and the
  gallery can drift apart on them with nothing to notice. Section 9
  carries that one to Tony.

## 3. What is in this stage, and Tony's rulings

**The obliquity.** The closed slice requires the fields on every row
that draws the room. The obliquity draws Earth's axis in both drawings
as much as the pole does; with the pole on the frame's axis it is the
ONLY number that does. So by the rule it comes into `constants_new.py`, and it
brings the obliquity half of L-311 with it. Tony, 2026-09-22: yes to
both.

**The rotation period.** The first draft left it out because the room
draws no rotation. Tony ruled it in, 2026-09-22: "this is such a
fundamental fact that we should store it and quote it in the hovertext.
we don't render rotation because there is no reference point in the
crust shell. but this could be done in the future." So L-311 comes in
whole. Nothing new needs sourcing. `constants_new.py` already holds
`EARTH_ROTATION_RATE_RAD_S = 7.292115e-5`, read on 2026-09-19 from IERS
TN36 Table 1.2 with all four fields; the period is derived from it
(4.1). The hover says why the turning is not shown, in Tony's terms:
nothing on the crust marks a longitude to watch.

**Kilometres per AU is already in `constants_new.py`.** Tony asked; it is,
`KM_PER_AU` at `constants_new.py` line 114, exact, with its read. The
problem is on the gallery side only. The renderer does not read that
row; it types its own copy, `var KM_PER_AU = 149597870.7`, at
`gallery/feature_renderers.js` line 70, with a comment saying it
mirrors `constants_new.py`. Nothing checks that the two agree. The obliquity is
typed three lines further down in the same way. Stage D makes the page
read both from the served rows and deletes the two typed copies.
The rows in `constants_new.py` do not change.

## 4. The orrery half

### 4.1 New rows in `constants_new.py`

Every new Earth row takes the `EARTH_` prefix, because the checkers
decide slice membership by the name's first word and only `EARTH` is
closed. A row named for the ecliptic would sit outside every check,
which is a check that cannot fail. The two conversion rows belong to no
body's slice, as `DEG_PER_RAD` does.

Every row below except the precession rate was written into a throwaway
copy of `constants_new.py` at `ac25d4f4`, with the new tokens, and both
`test_dimensions.py` and `test_derived_figures.py` were run on it on
2026-09-23. All pass.

- **The pole.** `EARTH_POLE_RA_J2000_DEG = 0.0` and
  `EARTH_POLE_DEC_J2000_DEG = 90.0`. Unit `deg`. Status `declared`, a
  frame definition. Figures `exact -- the ICRF's z-axis, by the frame's
  construction`. Source: IERS Conventions (2010), TN36, chapter 5, and
  the Horizons manual's frame definition. Read: the builder's own, from
  both, naming the chapter and the page. The row says in words that the
  frame was built from Earth's mean pole of 2000, so the pole is the
  frame's axis up to the offset chapter 5 gives, and that a pole at
  declination 90 has no meaningful right ascension, so the 0.0 is a
  placeholder the transform ignores.
- **The obliquity, in the form its definition prints.**
  `EARTH_OBLIQUITY_J2000_ARCSEC = 84381.448`, unit `arcsec` (a new
  token), status `declared`, the angle that defines the Horizons
  ecliptic-of-J2000 frame from the ICRF, figures `exact -- a frame
  definition`. Then `ARCSEC_PER_DEG = 3600.0`, unit `arcsec_per_deg` (a
  new token), exact. Then `EARTH_OBLIQUITY_J2000_DEG =
  EARTH_OBLIQUITY_J2000_ARCSEC / ARCSEC_PER_DEG`, unit `deg`, derived,
  exact. This is Fable's form (section 11, finding 2). It lets the unit
  checker judge the degree row instead of trusting a literal with no
  inputs, and the checker reports it at 23.4393 degrees.
- **The rotation period.** `S_PER_HOUR = 3600.0`, unit `s_per_h` (a new
  token), exact. Then `EARTH_SIDEREAL_ROTATION_PERIOD_H = 2.0 * math.pi
  / EARTH_ROTATION_RATE_RAD_S / S_PER_HOUR`, unit `hours` (a new token),
  status `derived`, inheriting `EARTH_ROTATION_RATE_RAD_S`, figures `7
  -- set by EARTH_ROTATION_RATE_RAD_S`. It prints 23.93447 hours. The
  row says it is the sidereal period, a turn against the stars, because
  the 24-hour day a visitor knows is the turn against the Sun.
  - Rev 1 wrote this with a bare `/ 3600.0`. Fable found, and this
    session re-ran and confirmed, that the unit checker fails that form:
    it converts seconds to hours by itself, computes 0.006648 hours and
    finds 23.93447 stored. The figures checker passes the same row, so
    it looked green to one checker.
  - Two pi stays a bare number on purpose. The `rad_s` token already
    treats the radian as dimensionless.
  - Rev 1 said the token table has no time unit. That was wrong: it has
    `days`. It has no `hours`, which is why one is added.
- **The precession rate.** The builder reads it in TN36 chapter 5 and
  stores it in the unit the chapter prints, with a token added for that
  unit. Any degrees-per-year form is derived from it through an exact
  conversion row, never converted by hand. If the chapter gives no form
  that can be stored as a row, the builder stops and says so rather
  than typing a remembered number. The obliquity's own rate follows the
  same rule (5, the hover rule).

### 4.2 The pole dict moves into `constants_new.py`

Ruling (a) of L-322, 2026-09-14: `planet_poles` becomes a dict in
`constants_new.py`, and `idealized_orbits.py` imports it. Earth's entry
reads the two new rows. Every other entry keeps its value exactly and
carries no status line, which is how the file says the pass has not
reached them. The false "cross-check exactly" sentence is removed. The
Moon's entry gets a one-line note that the cited table no longer has a
row for it. `solar_visualization_shells.py` line 1655, which names the
dict's old home in a comment, is updated.

The dict's comment also says, in words, that the checkers read only
top-level rows, so no checker sees the other bodies' entries. The move
changes where they live, not whether anything checks them. Each is
checked when its own body is walked.

### 4.3 The orrery's code sites

- `idealized_orbits.py` line 3352 reads `EARTH_OBLIQUITY_J2000_DEG`,
  and the "IAU 2006" label goes.
- `PLANET_ROTATION['Earth']['period_str']` in
  `planet_visualization_utilities.py` interpolates the period row
  instead of typing `'23.93 h'`.
- `PLANET_ROTATION['Earth']['obliquity_str']` interpolates the
  obliquity row instead of typing `23.44`, printed by the exact-row rule
  in section 6.
- **The orrery's magnetosphere shape.** Tony's ruling of 2026-09-23
  (section 9): the five numbers chosen by eye in
  `earth_visualization_shells.py`, the 12 and 10 Earth-radii widths at
  lines 856 and 857 and the tail's 100, 15 and 25 at lines 860 to 862,
  are removed. The orrery draws the Shue surface the gallery room
  already draws, from the rows in `constants_new.py`, cut at
  `EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG`, and adds the sourced tail below.
  The hover's sentence calling the shape "an approximation of the shape,
  not the model's own" goes, because it stops being true.
- **The sourced tail.** New measured rows from Slavin et al. (1983),
  read by the builder from the abstract at
  ntrs.nasa.gov/citations/19830066648: where flaring stops, 100 and 120
  Earth radii as two rows, and the tail diameter far downstream, near
  60. The tail's radius where it leaves the surface is not typed; it is
  the Shue surface's distance from the Sun-Earth line at the cut angle,
  computed from the rows (about 20 Earth radii at the declared solar
  wind). Three declared constructions remain, each a stated rule over
  those rows with its reason on the row, under When the Source Gives a
  Range: which point in 100 to 120 the flare stops at, that the radius
  grows in a straight line between the two sourced points, and that the
  drawing ends at `EARTH_MAGNETOTAIL_OBSERVED_RADII`, which the hover
  says is how far the spacecraft went, not where the tail ends. The
  hover shows the ranges.
- **The belts.** `belt_thickness` at line 867 is removed. Each belt's
  rings are spread across its served edges, with the peak ring drawn
  brighter (section 5).

## 5. The gallery half

- **Earth's pole.** In `data/objects_config.json`, Earth's
  `orientation` block, the two pole values become pointer entries to
  the new rows, so `tools/mirror_constants.py` writes them as SERVED.
  The source string becomes the frame's own statement from 2.2.
- **The two typed numbers in the drawing code.** `KM_PER_AU` and the
  obliquity at `gallery/feature_renderers.js` lines 70 and 74 are
  deleted, and the page reads the served rows. If a row is missing, the
  page says so in its warnings and draws no tilt, rather than falling
  back to a remembered number. Where in the served files these two rows
  sit is the builder's design, reported with the patch. Every room that
  calls `poleBasis`, the Sun's included, is smoke-tested before and
  after, because the change reaches them all.
- **The axis hover in `gallery/earth_geometry.js`.**
  - The sources are re-homed. The pole goes to the frame. The sense of
    rotation goes to the report's Section 2 definition, plus a source
    the builder opens for Earth turning prograde.
  - It states the sidereal rotation period from the served row. The
    sentence saying no period is stated "because none is served" goes.
    In its place the hover says the turning is not animated because
    nothing on the crust marks a longitude to watch it by.
  - It prints the tilt from the served obliquity row by the exact-row
    rule in section 6.
  - **One rule for the pole and the tilt,** because both are values of
    the year 2000 and both really move. The hover names the epoch for
    both. Each shows its rate, read in TN36 chapter 5, beside its value.
    If the chapter gives no storable rate for one of them, the hover
    says that value moves slowly and gives no number, and the same then
    holds for the other, so the two are never treated differently.
    Fable's review asked for exactly this: one rule applied to both
    rows.
  - Earth's served entry gains pointer entries for the period row and
    the rate rows.
- **The magnetotail entry.** Nothing in the gallery reads its
  `length_radii`, `base_radii`, `end_radii`, `color` or `opacity`. A
  search of every gallery script, page and tool on 2026-09-23 found no
  reader. The room does not draw a tail. Those five typed numbers are
  deleted, and the `_declared` sentence that describes them is rewritten
  to say the gallery draws no tail. The served `observed_extent` link
  stays, since it is a sourced row ready for a future drawing. The
  gallery then draws the same sourced tail as the orrery (4.3), from
  the served rows, so the two drawings of the magnetosphere match.
- **The belts.** `belt_thickness` is removed from both belt entries in
  `objects_config.json`, and the renderer's fallback of 0.5 in
  `feature_renderers.js` goes with it. Each belt's rings are spread
  between its served inner and outer edges, and the ring at the served
  peak is drawn brighter. Tony, 2026-09-23: yes. Whether the belts
  should also follow the field lines stays with L-330, for Tony's eye.
- **A wrong sentence in the served config.** Earth's `magnetic_tilt`
  source string says the tilt is "rounded to a tenth of a degree" and
  drifts "about 0.05 deg per decade". The served value is 9.4105 at
  five figures, and the served rate is -0.0493 degrees per year, which
  is about 0.49 per decade, ten times the sentence's figure. This is the
  factor-of-ten error v3.67 records as fixed in `constants_new.py`; the
  config's copy of the prose was never updated. As far as a search of
  the drawing code shows, this string does not reach the visitor's
  panel, but it is served, and the file is open in this build, so it is
  corrected here.
- `tools/test_mirror_constants.py` line 373 expects SERVED, and the
  mirror's docstring says three `planet_poles` links, not four.
- The cache is rebuilt after the config change, because a config change
  is not deployed until the cache is rebuilt (gallery-cache-builder).

## 6. How an exact row prints

Rev 1 asked whether Rule 7 answers a number that is exact by
definition. Fable's answer is method, and rev 2 adopts it with one
addition. It goes into provenance-discipline 2.18 (section 12), so the
build waits for that version.

**What happens today.** `fmtServed` in `gallery/feature_renderers.js`
prints a row served as exact with `toFixed(digits)`, a number of
decimal places chosen at each of its 20 call sites. The export serves
twelve exact rows on gallery `2e0fa8f5`: `KM_PER_AU`,
`EARTH_LEO_UPPER_ALTITUDE_KM`, `EARTH_LEO_LOWER_ALTITUDE_KM`,
`EARTH_VAN_ALLEN_OUTER_RADII`, `DEG_PER_RAD`,
`EARTH_SOLAR_WIND_PRESSURE_NPA`, `EARTH_SOLAR_WIND_BZ_NT`,
`EARTH_SOLAR_WIND_SPEED_KM_S`, `EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG`,
`EARTH_BOW_SHOCK_CUT_ANGLE_DEG`, `GM_SUN_SI` and `M3_PER_KM3`.

**Fable's rule.** An exact quantity is stored in the form its
definition prints, and it prints its definition's digits. The export
carries a print count for each exact row, and a derived exact row
inherits the count of its defining input. The obliquity then prints
23.439291 degrees, eight figures, from 84381.448.

**The addition, and why.** Fable counts the print figures from the
typed literal by Rule 2, giving "2.0 is 2; 120 is 3". But the file types
`120.0`, not `120`, and Python types most whole numbers with a `.0`
by habit. Rule 2 says a trailing zero after the decimal point counts
only when it falls within the source's reporting resolution, and a
declared pick has no source resolution. So the literal cannot say
whether `200.0` means 200 or 200.0, and a print count read from it
would turn a typing habit into visitor text: "200.0 km" for a floor
that was chosen as 200. Counted consistently, 120.0 would be four
figures, not three. The fix: every exact row states its print count as
a field on its `# Figures:` line, for example `exact -- prints 3`, and
the checker refuses a print count larger than the digits the literal
actually has. A zero, such as the solar wind's Bz of 0.0, prints as 0.

**The reach.** Every hover that prints one of the twelve rows is listed
before the patch with its text today and its text after, and Tony's
Mode 5 look covers each one. The Earth room carries most of them.

## 7. Recorded, not built -- one ledger row per class

- **Pole entries that disagree with their cited table at the year
  2000:** Mercury, Uranus, Neptune (2.5).
- **Pole entries citing a report that withdrew them:** Earth, fixed
  here, and the Moon.
- **The obliquity typed outside `constants_new.py` in other
  artifacts:** `star_sphere_builder.py` line 46 (23.4393), and "23.4" in
  visitor text at `palomas_orrery.py` lines 5787, 8014 and 8832 and
  `coordinate_system_guide.py` line 441.
- **Measured numbers typed only in `objects_config.json`:** Jupiter's
  and Saturn's ring radii and thicknesses, 32 numbers (2.6).
- **Sun numbers in `objects_config.json` with no link, 43, not yet
  sorted** into measurements and drawing choices (2.6). The Sun comes
  next, since its room is published.
- **Rendering settings in `constants_new.py`:** `DEFAULT_MARKER_SIZE`
  and `CENTER_MARKER_SIZE`, read by `palomas_orrery.py` and
  `palomas_orrery_helpers.py`, move to the drawing code. The same block
  holds `HORIZONS_MAX_DATE`, which is a fact about the data source, not
  a drawing choice, and stays.
- **A unit conversion by a bare number inside a `constants_new.py`
  expression** (a 3600, a 60, a 1000). The unit checker converts units
  by itself, so a bare divisor makes the stored value disagree with the
  arithmetic. Found in rev 1's period row; Fable notes the class also
  reaches `LIGHT_MINUTES_PER_AU` and its neighbours in the list of rows
  not yet migrated.
- **A discrepancy with the handoff**, noted on L-322: it planned a
  rate-and-angle row, and the source shows Earth has no such row in
  this frame.

## 8. The first lines of the next ledger patch

- **L-311: DONE when this build lands**, both halves.
- **L-325: close**, superseded by L-322. Tony's ruling, 2026-09-22.
- **L-342: close**; both open points were answered and what remains
  is L-343 and L-345. Tony's ruling, 2026-09-22.

## 9. For Tony

**Ruled, 2026-09-22:** Stage D takes the pole, the obliquity and the
rotation period into `constants_new.py`, and the gallery reads
kilometres per AU and the obliquity from the served rows instead of its
own typed copies. L-311 closes with this build.

**Ruled, 2026-09-22, on drawing numbers.** Three kinds, and each has
one home:

- A number that stands for something physical (a size, an edge, a
  cut angle) lives in `constants_new.py`. A measured one is sourced; a
  decided one is declared, with its reason and range on the row.
- A number chosen by eye before the sourcing rules existed is cleaned
  up as the braid reaches it, through the three outcomes of A Drawing
  Approximation Does Not Promote.
- A rendering setting, such as opacity, point count, ring count, color,
  marker type and size or font, makes no claim about the object and
  stays in the drawing code. Tony: "these are defined in the code not
  in constants new."

The test between the first and third kinds is whether changing the
number moves where something is drawn, or only changes how it looks.

**Ruled, 2026-09-22, on order.** Published rooms are retrofitted
first, featured ones before the rest, because visitors reach them
first.

**A correction to what rev 1 told Tony.** Rev 1 said the Earth room
draws the magnetotail sizes and the belt thickness, and Tony ruled on
that basis that both are handled in this build. The room does not draw
a tail; only the orrery does. Rev 2 therefore deletes the gallery's
unused copies and records the orrery's tail (sections 5 and 7). The
belt thickness IS drawn by the room.

**Ruled, 2026-09-23, on the belts and the magnetosphere.** The belt
thickness is a physical size with no source, so it is removed and each
belt is drawn across its served edges. The orrery's magnetosphere
shape and tail, chosen by eye, are replaced by the Shue surface plus a
tail built from Slavin et al. (1983), and the gallery draws the same
tail (option 1 of two offered; option 2 was the surface with no tail).
Tony preferred option 1 because it shows more.

**(do)** Nothing until the build.

## 10. Done when

- The pole, obliquity and period rows carry unit, status, figures and a
  read, and pass both checkers inside the closed slice.
- The mirror reports Earth's pole SERVED, and no Earth link is NOT IN
  STORE.
- No file in either repository cites the 2015 report for Earth's pole
  or Earth's rotation angle.
- `feature_renderers.js` types no measured or defined number.
- Both axis hovers state the sidereal rotation period from the period
  row, and neither types it.
- Every exact row prints by its stated print count, and the before and
  after text of each affected hover is listed.
- `objects_config.json` carries no magnetotail number that nothing
  reads.
- Every changed check is shown failing once by name before it passes.
- Tony's Mode 5 look finds the Sun room unchanged except for its hover
  text, and accepts the new belts and the tail in both drawings of
  Earth.
- No number that moves where something is drawn in Earth's
  magnetosphere is typed in either repository.

## 11. Fable's review, finding by finding

- **1, the period row fails the unit checker.** Accepted. Re-run in
  this session on a throwaway copy at `ac25d4f4`: the bare form fails
  as Fable says, and the `S_PER_HOUR` form passes both checkers (4.1).
- **2, exact rows and Rule 7.** Accepted, with the print-count field
  added (section 6), because counting from a Python float literal
  cannot tell a meant trailing zero from a typing habit. The arcsecond
  form of the obliquity was re-run here and passes both checkers.
- **3, the magnetotail and belt thickness missing from the build
  sections.** Accepted that they were missing. Not accepted as
  proposed: declared rows "with the reason on each row" would promote
  numbers chosen by eye, which A Drawing Approximation Does Not Promote
  forbids. And the finding rested on rev 1's error: the gallery room
  draws no tail. Section 9 corrects that and asks Tony one question
  about the belt.
- **4, the precession token and the obliquity's drift.** Accepted
  (4.1, and the one hover rule in section 5).
- **5, smaller points.** Accepted: the right ascension note (4.1), the
  note that the moved dict is not checked (4.2), and naming whose frame
  the obliquity defines. Fable's recalled figure for IAU 2006 is not
  used anywhere, as Fable says it should not be.
- **The gate Fable reported.** Fable's session had provenance-discipline
  2.15 mounted and read 2.17 from the repository. This session has 2.17
  mounted, byte-identical to `skills/` at `751aff3f`.

## 12. Before the build: provenance-discipline 2.18

One skill version carries all of these, because one session ships one
version of a skill:

- Tony's three kinds of drawing number and the test between them
  (section 9). It removes the contradiction between One Value, One Home
  and A Drawing Approximation Does Not Promote.
- The exact-row rule: stored in the form its definition prints, a
  stated print count on every exact row, and the page prints by it
  (section 6).
- The bare-number conversion rule: a unit conversion inside an
  expression is an exact row with a compound-unit token (4.1).

- The midpoint as the default pick inside a sourced range, unless the
  row states a reason for an end (Tony, 2026-09-23).

Written as `patch_L322_D_1_prov218_skill.py`, built on `ac25d4f4`,
which also adds protocol v3.68 and moves v3.65 into the history file.
Tested on a throwaway copy: every edit applied, a second run refused on
the changed fingerprint, `skills_index.py` then reported the manifest
moving 2.17 to 2.18 with no consistency problems, and all three files
stayed ASCII with LF endings.

The session that cuts 2.18 cannot confirm its own reinstall. So the
build runs in a later session, which confirms it has 2.18 loaded before
touching `constants_new.py`. Fable's review is filed beside this
manifest as `documentation/REVIEW_L322_D_manifest_fable_20260923.md`.

---

Written September 2026 with Anthropic's Claude Opus 5.5.
