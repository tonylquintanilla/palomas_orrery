# Review: how many digits the orrery's distances earn (L-401, the distance hovers)

    Model: Claude Fable 5.1 (configured identifier claude-fable-5-1; the
           serving model can differ from the configured one, so this is
           the configured name, not a verified one)
    Effort tier: the session's default reasoning effort. No effort
           setting was chosen for this answer, and the setting is not
           visible to me from inside the session.
    Date: 2026-10-11
    Rule files read (all at orrery commit 28a4636717920e86965f2e1777f3bf92386d1bb6,
           cloned with git and read from disk):
           PROJECT_INSTRUCTIONS.md (Fetched vs Recalled Convention;
             Show the Envelope of the Unknowable; also the Register Rule,
             which governs how this file is written)
           skills/provenance-discipline/SKILL.md (The Access Standard;
             A Computed Position Prints What Its Errors Earn; An Accuracy
             Stated in Words Is Stored as the Place It Reports To)
           skills/provenance-discipline/references/figures.md (The
             ceiling, all five parts, including the Report test)
           skills/horizons-orbital-mechanics/SKILL.md (whole file)
           skills/orrery-coding-conventions/SKILL.md (Hover Text Is
             Written for the Visitor)
           Code read: formatting_utils.py (whole), orbital_period.py
             (lines 1-160: the module header, report_exponent and
             format_by_error), visualization_utils.py (lines 795-830
             and the hover-assembly lines 914-933), celestial_coordinates.py
             (lines 130-500: MAJOR_BODY_UNCERTAINTIES, get_precision_note,
             format_radec_hover_component), palomas_orrery.py (fetch_position
             at 1233-1290; fetch_radec_for_hover at 1796-1860),
             constants_new.py (lines 3515-3600, the three DE430 rows),
             celestial_objects.py (lines 312-340, the Lagrange-point entries).
    Pre-flight: Horizons manual, "Definition of Observer Table Quantities",
           quantity 39, quoted verbatim:
           "39. Uncertainties in plane-of-sky radial direction
            Range and range rate (radial velocity) formal 3-standard-deviation
            uncertainties.
              Units: KM, KM/S
              Labels: RNG_3sigma RNGRT_3sig"
           Read at:
           https://ssd.jpl.nasa.gov/horizons/manual.html
           (The chat's web-fetch tool cuts this page off before that
           section, so I read it through the browser pane on Tony's
           computer, which also let me run two live Horizons queries;
           see Q8.)

## The one finding that changes the shape of the problem

Before the questions, one thing I found by running Horizons live, because
it changes several answers at once.

- Horizons' **vector table** -- the same kind of query the orrery already
  uses to fetch a body's position and velocity -- can return the
  uncertainties of the position and velocity **in the same answer**, when
  the table type is `2` with a modifier letter. `VEC_TABLE='2xr'` returns
  position, velocity, and their uncertainties in two coordinate systems.
  One of those systems, RTN, has an axis R that points from the plot's
  centre to the body. Its uncertainty, labelled `R_s`, is exactly the
  distance's uncertainty. Its velocity counterpart `VR_s` is the uncertainty
  of the speed along that line; `VT_s` and `VN_s` cover the other two
  directions.
- I ran it for Sedna from the Sun's centre for 2026-10-12 and got
  `R_s = 8.59399950E+04` km and `VR_s = 7.98911532E-05` km/s. Three times
  these are 257,820 km and 0.0002397 km/s, which match the `RNG_3sigma`
  (257,817.569 km) and range-rate 3-sigma (0.0002397 km/s) the project
  fetched from the observer table. So the two routes agree, and the
  vector-table numbers are **one-sigma**, while quantity 39 is
  **three-sigma**. The page labels them: "R_s    Radial direction 1-sigma
  position uncertainty (km)".
- I ran the same query for Mercury (`199`): every uncertainty column came
  back `n.a.`, as the manual says it will for a body with no covariance.
- The catch: `astroquery`, the library the orrery uses, does not set
  `VEC_TABLE` at all (so Horizons uses its default, type 3, which carries
  no uncertainties) and offers no parameter to change it. The orrery would
  have to call the Horizons web address directly for small bodies, the way
  `orbital_period.py` already calls the Small-Body Database address directly
  with `requests.get`. That is a change in how the position is fetched, not
  an extra query.

What this means for the questions: the small bodies' distance error and
velocity error come free with the position (Q1, Q4, Q8); they come from
the plot's own centre (Q5); and they arrive as one-sigma, so the project
must choose a level once (Q2).

Sources for this section:
- NASA/JPL Horizons API documentation, "VEC_TABLE Parameter":
  ```
  https://ssd-api.jpl.nasa.gov/doc/horizons.html
  ```
  Quotation: "Modifier codes are accepted for values 1 and 2 to trigger
  output of formal statistical uncertainties when available (for asteroids
  and comets only)." And the code table: "r  RTN uncertainties (radial,
  transverse, normal)".
- Live Horizons answers, read 2026-10-11 through the browser pane (these
  are fetched data, not a document; the addresses are the queries):
  ```
  https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND='90377'&OBJ_DATA='NO'&MAKE_EPHEM='YES'&EPHEM_TYPE='VECTORS'&CENTER='500@10'&START_TIME='2026-10-12'&STOP_TIME='2026-10-13'&STEP_SIZE='1d'&VEC_TABLE='2xr'&OUT_UNITS='KM-S'&CSV_FORMAT='YES'
  https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND='199'&OBJ_DATA='NO'&MAKE_EPHEM='YES'&EPHEM_TYPE='VECTORS'&CENTER='500@10'&START_TIME='2026-10-12'&STOP_TIME='2026-10-13'&STEP_SIZE='1d'&VEC_TABLE='2xr'&OUT_UNITS='KM-S'&CSV_FORMAT='YES'
  ```
  Sedna's answer header: "Output format   : 2xr (pos. & vel.
  w/uncertainties: XYZ, RTN)". Its symbol table: "R_s    Radial direction
  1-sigma position uncertainty (km)" and "VR_s   Radial direction 1-sigma
  velocity uncertainty (km/sec)".
- astroquery source, `astroquery/jplhorizons/core.py`, the `vectors_async`
  request payload:
  ```
  https://raw.githubusercontent.com/astropy/astroquery/main/astroquery/jplhorizons/core.py
  ```
  The payload sets `VEC_LABELS`, `VEC_CORR` and `VEC_DELTA_T`; the string
  `VEC_TABLE` does not appear in the file.

## Q1. Sources by kind of body

**Recommendation.** Planets and Pluto: keep the 2014 rows; there is no
better open source with a number or words in it. Small bodies: the
`R_s` column above, from the plot's centre, times three. The Moon: a new
row from the same 2014 report ("submeter"), place 1 metre. Other planets'
moons, spacecraft, Lagrange points and the solar-system barycentre: no
source states an accuracy; treat them as Q3. The Sun as a body: no source
either; Q3.

**Reasoning.**

- *Planets and Pluto.* I read the DE440/441 paper (Park et al. 2021), which
  is open access. It states no orbit accuracy in metres or kilometres for
  any planet. It gives fit residuals (how well the model matches the
  measurements, e.g. "The rms residual of the Juno ranges is about 13 m"),
  which are not the same thing as how well the orbit is known, and it says
  Uranus and Neptune are "statistically consistent with DE430". So the 2014
  words remain the only open statement, and the project's reading of them
  as a conservative bound holds. The Horizons manual adds one sentence in
  words for the whole class: "Uncertainties in major planet ephemerides
  range from meter to 1000+ km in the state-of-the-art JPL/DE441
  ephemeris". That is too wide to place any one planet by, but it is a
  Horizons product confirming that today's ephemeris still spans the same
  range the 2014 words describe. I would add it to the three rows' comments
  as a second read, not as a new row.
- *Small bodies.* Explained above. Prefer the vector-table `R_s` over
  quantity 39 because it rides the position fetch and is already in the
  plot's own geometry (centre and date).
- *The Moon.* The 2014 abstract: "The present-day lunar orbit is known to
  submeter accuracy through fitting lunar laser ranging data". "Submeter"
  means under one metre, so by the project's own rule (store the place the
  words report to) the row is 1 metre, that is 0.001 km. This is the Moon's
  distance from Earth. In a Sun-centred plot the Moon's distance from the
  Sun carries Earth's error (1 km place), which is larger, and the larger
  wins.
- *Other planets' moons.* JPL's satellite-ephemeris page lists an ephemeris
  file and a reference paper per system but states no accuracy. The
  reference papers (mostly R. A. Jacobson's) do state uncertainties, but
  one paper per planetary system, each to be opened and read. That is a
  ledger class, not something to settle here. One honest thing is
  available now: in a Sun-centred plot a moon's distance from the Sun is
  the planet's distance plus a small offset, so its error is **at least**
  the planet's row. Printing the moon by its planet's row, and saying so,
  is sourced and conservative in the direction that matters. In a
  planet-centred plot the moon's distance is the satellite-ephemeris
  quantity, which has no row yet: Q3.
- *Spacecraft.* The manual says trajectories come from navigation teams,
  are updated "weekly or monthly", and gives one accuracy sentence only for
  low Earth orbit ("Predictions more than a few days into the future can
  have 10s or 100's of km of error"). No per-spacecraft accuracy. Q3.
- *Lagrange points.* These are Horizons major bodies (31-35, 3011-3015).
  Their data sheet (I opened SEMB-L1's) describes the point and gives no
  accuracy. Recall, labelled as such: Horizons computes them from the
  Sun's and the Earth-Moon barycentre's positions, so their error would be
  those bodies' errors; but no document I opened says so. Q3.
- *Barycentres.* The Pluto row already says it is about the Pluto-Charon
  barycentre. The Earth-Moon barycentre is what the terrestrial row
  describes as well as Earth itself (the 2014 fit is to the barycentre's
  orbit; recall, not quoted). The solar-system barycentre relative to the
  Sun has no stated accuracy. Q3.

**Sources.**

- Park, R. S., Folkner, W. M., Williams, J. G. & Boggs, D. H. (2021), "The
  JPL Planetary and Lunar Ephemerides DE440 and DE441", The Astronomical
  Journal 161:105 (open access, CC-BY 4.0):
  ```
  https://iopscience.iop.org/article/10.3847/1538-3881/abd414
  ```
  Abstract: "The orbit of Jupiter has improved substantially by fitting to
  the Juno radio range"; body, section 5.1 Residuals: "The rms residual of
  the Juno ranges is about 13 m." Body: "The orbits of Uranus and Neptune
  are mainly constrained by astrometry and radio range measurements to the
  Voyager flybys" and that they are "statistically consistent with DE430".
  No sentence states an orbit accuracy in km.
- Folkner, W. M., Williams, J. G., Boggs, D. H., Park, R. S. & Kuchynka, P.
  (2014), "The Planetary and Lunar Ephemerides DE430 and DE431", IPN
  Progress Report 42-196, abstract:
  ```
  https://ipnpr.jpl.nasa.gov/progress_report/42-196/196C.pdf
  ```
  "The present-day lunar orbit is known to submeter accuracy through
  fitting lunar laser ranging data". Also re-read: "The orbits of Jupiter
  and Saturn are determined to accuracies of tens of kilometers" and
  "limit position accuracies to several thousand kilometers."
- Horizons manual, "Statement of Ephemeris Limitations":
  ```
  https://ssd.jpl.nasa.gov/horizons/manual.html
  ```
  "Uncertainties in major planet ephemerides range from meter to 1000+ km
  in the state-of-the-art JPL/DE441 ephemeris, used as the basis for
  spacecraft navigation, mission planning and radar astronomy." Same
  section: "Cartesian state vectors are output in all their 16
  decimal-place glory. This does not mean all digits are physically
  meaningful."
- Horizons manual, "Spacecraft Trajectories in Horizons": "Spacecraft
  trajectory data in Horizons may only be updated weekly or monthly and
  doesn't change in-between." and "Predictions more than a few days into
  the future can have 10s or 100's of km of error".
- JPL "Planetary Satellite Ephemerides" page:
  ```
  https://ssd.jpl.nasa.gov/sats/ephem/
  ```
  The only accuracy wording: "These ephemerides are used by Horizons to
  provide high-precision ephemerides for the planetary satellites." No
  number.
- SEMB-L1 data sheet (live Horizons answer):
  ```
  https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND='31'&OBJ_DATA='YES'&MAKE_EPHEM='NO'
  ```
  "The Sun & Earth-Moon Barycenter Lagrange-1 point (SEMB-L1) is a location
  where the Earth's gravitational field partially counters that of the
  Sun." No accuracy stated.

**Confidence.** High that no open document states planetary orbit
accuracy in distance better than the 2014 words (I read the DE440 paper's
abstract and residuals section and searched it for "accuracy", "known to",
"within"). Medium on the moons: I did not open the Jacobson papers, so I
cannot say what they would give. A reader who opens one per system would
change the moons' answer from Q3 to a row.

## Q2. One rule, two kinds of figure

**Recommendation.** Yes, print both by the same rule, because both are
first turned into the same object -- a half-width in kilometres -- before
the Report test sees them. Take the **three-sigma** level for small bodies
(multiply the vector table's one-sigma by three). Tell the visitor which
kind it is in the last line of the box, in words, the way the period line
already does.

**Reasoning.**

- The rule asks one question of every number: how far could this be wrong?
  For a planet the answer is a bound JPL stated in words; the project
  stores the place the words report to and uses half that place as the
  half-width. For a small body the answer is a statistic JPL computes for
  the date. Different in origin, same in kind once in kilometres. The
  Report test does not care where the half-width came from; the box must,
  and it says so in words.
- Why three-sigma and not one. Three reasons, in order of weight. First,
  the project's own planetary half-widths "err large" on purpose
  (figures.md: a half-width "is a full half-width rather than a standard
  deviation, so it errs large"), so a bound-like level keeps the two kinds
  comparable. Second, the manual warns the formal numbers can be too small:
  "If there are systematic biases ... results can be optimistic" and "results
  can also be optimistic for times far from the solution epoch". Erring
  large is the honest direction. Third, the sky-position line already
  prints three-sigma; one level per box is easier to explain. The cost is
  one fewer digit about half the time (three is nearly half a decade on a
  log scale, log10(3) = 0.48). For Sedna: one-sigma gives 82.830 AU and
  12,391,200,000 km; three-sigma gives 82.83 AU and 12,391,000,000 km.
- "Something else": one could argue for the full three-dimensional error
  (`X_s`, `Y_s`, `Z_s` combined) rather than the radial part alone. No. The
  distance is a length along R, and only the error along R moves it; the
  sideways errors move the body across the sky, which is the RA/Dec line's
  business. R_s is the right column.
- What the box says. For a planet: "Rounded to how well JPL's 2014
  ephemeris report says this planet's orbit is known." For a small body:
  "Rounded to JPL's stated 3-sigma uncertainty of this body's orbit for
  this date." The word "stated" carries the manual's caveat without
  lecturing.

**Sources.**

- Horizons manual, "Statistical Uncertainties":
  ```
  https://ssd.jpl.nasa.gov/horizons/manual.html
  ```
  "Output for asteroids and comets can include formal +/- 3-standard-deviation
  statistical orbit uncertainty quantities. There is a 99.7% chance the
  actual value is within given bounds." and "If there are systematic biases
  (such as measurement timing, reduction, or star-catalog errors), results
  can be optimistic."
- The project's own rule text, figures.md, The ceiling, Propagate: "that is
  a full half-width rather than a standard deviation, so it errs large."

**Confidence.** High that both can share the rule. Medium on three versus
one: it is a convention, and either is defensible once stated; what would
change my mind is Tony preferring the box to carry a stated "+/-" next to
the number, in which case one-sigma with "+/-" printed is the physicists'
habit and the Report test's reference examples (3.78 +/- 0.07 kg) read that
way.

## Q3. No stated error

**Recommendation.** Print at a stated floor and say, in plain words, that
JPL states no accuracy for this body's position. Make the floor the same as
the website's -- whole kilometres -- so the two displays agree. Do not
leave the line out, and do not print ten figures with a note; the note
does not undo the digits.

**Reasoning.**

- The project's own rule for the gallery already decided this shape: a body
  with no accuracy row "prints by its drift and SAYS so in the display".
  The orrery has no drift (it asks Horizons live), so the only remaining
  limit is the display's floor. Printing at the floor and saying it is a
  floor is the orrery's version of the same rule.
- Why not "the number as now with a note". Show the Envelope says silence
  reads as precision; ten figures with a disclaimer under them is still ten
  figures. A visitor reads the number, not the footnote.
- Why not leave the line out. The distance is the main thing the hover
  exists to tell. Removing it for Voyager because JPL publishes no
  uncertainty would remove the most-asked number from the bodies people ask
  about most.
- The honest weakness of a floor: for a distant spacecraft, whole
  kilometres is still eleven figures. The sentence under it has to do the
  work: "Shown to whole kilometers, a display limit, not a measured
  accuracy; JPL states no uncertainty for this body's position." That is
  more words than the other boxes, which is right -- the body that knows
  least should say most.
- Order of preference when some source exists: a row (planets, the Moon);
  then the parent planet's row as a lower bound (moons, Sun-centred); then
  the floor with the sentence.

**Sources.** None states a floor; this is a design answer. The rule text
relied on is skills/provenance-discipline/SKILL.md, A Computed Position
Prints What Its Errors Earn: "A body with no source-accuracy row yet
prints by its drift and SAYS so in the display, in words the display's
owner approved".

**If I say no source exists.** For spacecraft I searched the Horizons
manual's text for "spacecraft", "accuracy of", "uncertainties are", and
read the "Spacecraft Trajectories in Horizons" and "Statement of Ephemeris
Limitations" sections; for Lagrange points I searched the manual for
"Lagrange" (no hits) and opened SEMB-L1's data sheet; for the satellites I
opened JPL's satellite-ephemeris page. None states a position accuracy for
these kinds.

**Confidence.** High on the shape (floor plus sentence). Medium on whole
kilometres as the floor; a relative floor (a fixed number of figures) is
simpler for far bodies, but it is a second convention to explain and the
website already chose kilometres.

## Q4. Velocity

**Recommendation.** Small bodies: a source now exists -- the vector
table's velocity uncertainties (`VR_s`, `VT_s`, `VN_s`). Take the length of
that three-part error (root-sum-square), times three, as the speed's
half-width; it cannot be smaller than the true speed error, so it errs
large in the honest direction. Planets and everything else: no source
states a speed accuracy. Print the speed to the same number of significant
figures as the distance line in the same box, and say so: "shown to the
same relative precision as the distance; JPL states no separate accuracy
for the speed."

**Reasoning.**

- The speed is the length of the velocity vector. Horizons gives the
  uncertainty of each component. The error of a length is never more than
  the length of the error vector (recall: a basic property of vectors, not
  a source). So the root-sum-square of the three components is a bound.
  For Sedna that is 8.50e-5 km/s one-sigma, 2.55e-4 km/s three-sigma, which
  prints the speed as 4.447 km/s -- the same digits as today, by
  coincidence.
- For planets, "same relative precision as the distance" is a declared
  construction, and the box must say it. The reasoning behind it (recall,
  labelled): for a body on a near-Keplerian orbit, a fractional error in
  distance maps to a comparable fractional error in speed, within a factor
  of about two, which the Report test's log scale mostly absorbs. I do not
  claim a source for that; it is the reason the construction is
  reasonable, not a citation.
- A consequence worth seeing before building: for Mercury the construction
  earns **more** digits than today. Half a kilometre over 65.5 million km
  is eight parts in a billion; applied to 41.924 km/s it earns 41.9240
  km/s or finer. The project's rule allows "never finer than a floor the
  display states", so the display may cap it; but note the rule can add
  digits as well as remove them, and the planets' velocity is where it
  does.
- The alternative -- dropping the velocity's digits to a fixed width with
  no claim -- is what the box does now, and it is the thing under review.

**Sources.**

- Live Horizons answer for Sedna (address under the first section):
  "VR_s   Radial direction 1-sigma velocity uncertainty (km/sec)" with the
  values `7.98911532E-05, 2.86312463E-05, 3.91586337E-06` for `VR_s, VT_s,
  VN_s`.

**If I say no source exists** for planetary speed accuracy: I searched the
DE440 paper for "velocity" and "km/s" via the fetch tool's summary and the
Horizons manual's text for "velocity uncertainty"; the only hits are the
small-body columns above and the SPK description.

**Confidence.** High for small bodies. Medium for planets; the
construction is sound but it is ours, and a reviewer who prefers "remove
and note the gap" over any construction would print the planets' speed at
the floor instead. That is a judgment for Tony.

## Q5. A centre other than the Sun

**Recommendation.** Take the **larger** of the two bodies' half-widths,
not their root-sum-square, and name in the box which body set it. For a
small body seen from a planet, the Horizons `R_s` from that centre is the
small body's own error only; it does not include the planet's. So the
rule is: larger of (`R_s` times three, the centre's row).

**Reasoning.**

- Root-sum-square is for independent random errors of known size. The
  planetary rows are places, not standard deviations, and the errors of
  two planets in one ephemeris are not independent (they were fitted
  together; Earth-Mars range in particular is measured directly to
  metres, so the distance between them is better known than either
  heliocentric position). Combining them by a formula would claim a
  statistics we do not have. "The larger" is the one combination that
  claims nothing beyond the inputs, and it is already Tony's ruling of
  2026-10-01 ("use whichever is larger").
- A planet and its own moon share the planet's heliocentric error
  entirely, so the moon-from-planet distance has only the satellite
  error (Q3 until a row exists); the Moon from Earth has its own 1 metre
  row.
- Does quantity 39 (or `R_s`) from a planet centre include the planet's
  error? Recall, not read: Horizons maps the small body's own orbit
  covariance; the manual describes these as "statistical orbit
  uncertainty quantities" of the asteroid or comet, and describes major
  bodies' states as interpolated from stored ephemerides with no
  uncertainty attached ("Interpolation generally recovers the state to
  the millimeter level" is about the interpolation, not the orbit). So
  the planet's error is not in it, and the "larger of" rule adds it.

**Sources.**

- Horizons manual, "General Definitions", Major Body: "Their state vectors
  are obtained by interpolating previously defined ephemerides, such as
  DE441. Interpolation generally recovers the state to the millimeter
  level."
  ```
  https://ssd.jpl.nasa.gov/horizons/manual.html
  ```
- Park et al. 2021 (address under Q1), on the directly-measured
  Earth-Mars distance: "The rms residual of the MEX ranges is about 2 m
  and the rms residuals of the MGS, ODY, and MRO ranges are about 0.7 m."

**Confidence.** High on "larger of". Medium on the claim that Horizons'
small-body covariance excludes the planet's error; it is standard practice
but I did not find it written in the manual.

## Q6. The sky-position line

**Recommendation.** Retire `MAJOR_BODY_UNCERTAINTIES` and the type-based
"typical" fallbacks in `get_precision_note`. They are a typed table with
no source, and the line attributes them to "JPL DE440/441 ephemeris",
which is a citation over recalled data -- the protocol's own [CRITICAL]
failure. For small bodies keep the fetched three-sigma. For planets, print
RA and Dec to the angle the planet's distance row subtends at its distance
from Earth, as a declared construction stated in words; or, if the project
prefers no construction, print them at a stated floor with "JPL states no
sky-position uncertainty for this body here."

**Reasoning.**

- The table's values (Mercury 0.005", Moon 0.0001", Sedna 10") have no
  recorded source, and the comment says "Based on DE440/441 planetary
  ephemeris and mission data", which the DE440 paper does not support (it
  gives no angular accuracies for planets; its only angular figures are
  occultation residuals for Pluto, "about 8 mas in R.A."). The protocol
  says: "Never embed lookup tables from training memory." This is one.
  Three outcomes: it cannot be sourced, so remove it and note the gap.
- The fallback branch ("+/-10 arcsec" for a name starting with digits,
  "+/-5 arcsec" for a comet, "+/-1 arcsec" otherwise, labelled ", typical")
  is the same thing one step down. Horizons returns `n.a.` for bodies
  without a covariance, and that is the honest thing to print: "JPL gives
  no uncertainty for this body's sky position."
- The construction for planets: a position error of e kilometres at a
  distance d kilometres from Earth is an angle of e/d radians, times 206,265
  for arcseconds (exact conversion). For Mercury at about 1 AU today, the
  terrestrial half-width 0.5 km gives 0.0007", so RA to about 0.0001 s of
  time. The construction is pure arithmetic on a sourced row, which
  figures.md's "propagate" allows; the only assumption is that the sky
  error is the position error seen edge-on, which errs large if anything.
  It must be labelled as ours in the row and said plainly in the box.
- Note for the words: the RA/Dec line is from Earth's centre whatever the
  plot's centre is (`fetch_radec_for_hover` uses `location='@399'`). The
  box should say "as seen from Earth"; today it does not.

**Sources.**

- Park et al. 2021 (address under Q1): "The rms residuals of the stellar
  occultations are about 8 mas in R.A. and about 11 mas in decl." -- the
  paper's only angular figures, for Pluto, and residuals rather than
  accuracies.
- The orrery's own code at 28a46367: `celestial_coordinates.py` lines
  136-140, the comment "Based on DE440/441 planetary ephemeris and mission
  data" above a table with no `# Source:` line; lines 488-493, the
  "`, JPL DE440/441 ephemeris`" and "`, typical`" source notes.

**Confidence.** High that the table must go. Medium on the construction;
it is the kind of method question the skill can absorb (Method Belongs
to the Skill), and the alternative floor is also honest.

## Q7. The derived lines

**Recommendation.** Kilometres, light-minutes and light-hours carry the
same error, converted exactly into each unit, and each is placed by its
own Report test (the skill already says so: "Each unit is reported by its
own uncertainty"). Distance to the centre's surface carries the larger of
the position error and the radius's own uncertainty. Keep AU and
kilometres always; keep one light-time unit, chosen by size; keep the
surface line only when the centre is a body with a surface, not a
barycentre or a Lagrange point.

**Reasoning.**

- Conversions are exact numbers (the AU and the speed of light are
  defined), so the error converts without growing. The place can differ
  by unit because decades fall in different spots: Sedna at three-sigma
  prints 82.83 AU (two decimals) but 688.87 light-minutes (two decimals)
  and 11.481 light-hours (three). That is the rule working, not a fault.
- The surface line subtracts a radius. The Sun's 695,700 km is the value
  Horizons itself uses ("Center radii    : 695700.0, 695700.0, 695700.0 km"
  in the Sedna answer); that it is a nominal value fixed by convention
  (IAU 2015) is recall, not read here. A planet's mean radius has its own
  stated uncertainty; a gas giant's "surface" is a defined pressure level. So the surface line's error is the larger of the position's and
  the radius's, and for a gas-giant centre the hover should say the
  surface is a defined level. Where the centre is a barycentre or a
  Lagrange point there is no surface and the line should not print
  (`CENTER_BODY_RADII.get(name, 0)` prints the distance twice today).
- Four distance lines is a lot of glance. Mercury's 0.0607 light-hours and
  Sedna's 689 light-minutes add nothing the other unit did not say. One
  light-time unit, light-minutes below one hour and light-hours above,
  keeps the teaching (how long light takes) and loses a line. This is a
  Mode 5 call, Tony's.

**Sources.** The project's rule text, figures.md, The ceiling, Report:
"Each unit is reported by its own uncertainty, so a value and its
conversion can carry different counts". No external source needed; the
conversions are definitions.

**Confidence.** High on the error carrying over. The line-count question
is taste.

## Q8. Cost

**Recommendation.** There is a cheaper route, and it costs nothing: fetch
small bodies' positions with `VEC_TABLE='2xr'` and the uncertainties
arrive in the same answer, for every frame of an animation too, since an
animation's frames come back as rows of one table. Planets need no fetch
(rows). No caching is needed for correctness; if the project wants to
keep the uncertainty for a day per body anyway, that is safe for the
digit count, because the Report test only notices a change of a factor of
about three, and a distant body's uncertainty does not move that much in
a day.

**Reasoning.**

- Today: one vectors query (position) plus one observer query (RA/Dec with
  36 and 37) per body per plot. Proposed: the same two, with the vectors
  query asking for `2xr` instead of the default. Zero added questions.
- The price is implementation, not traffic: `astroquery` cannot ask for
  `2xr`, so the small-body position fetch would move to a direct call of
  the Horizons API address, parsed from its CSV. `orbital_period.py`
  already does exactly this kind of direct call for the Small-Body
  Database, so the pattern exists in the codebase. The columns to read
  are named in the answer's own symbol table (`R_s`, `VR_s`, `VT_s`,
  `VN_s`); the parser should find them by name, not position.
- One caution on caching for near-Earth objects: their uncertainty can
  change quickly near an encounter (the manual says mappings are "optimistic
  for times far from the solution epoch, particularly for objects having
  close planetary encounters"). A per-day cache is fine for the digit
  count; a per-month cache is not for those bodies. Since the uncertainty
  comes free, I would not cache at all.

**Sources.**

- Horizons API documentation (address under the first section): the
  `VEC_TABLE` table and "Modifier codes are accepted for values 1 and 2".
- The two live Horizons answers under the first section (Sedna filled,
  Mercury `n.a.`).
- astroquery `core.py` (address under the first section): no `VEC_TABLE`.

**Confidence.** High. I ran the query and read the columns.

## Q9. What we missed

Framing first, then smaller things.

- **The rule can add digits.** The review assumes the rule shortens
  numbers. For the planets it mostly leaves the distance alone (Mercury:
  0.43815911 AU, 8 decimals instead of 10; 65,547,670 km instead of
  65,547,669.633) and it *lengthens* the speed (Q4). Decide before building
  whether the orrery has a fine floor as the gallery does, and state it in
  the display.
- **The Mercury box already contains a wrong-sounding sentence.** "JPL
  lists no orbit uncertainty for this body" is true of the Small-Body
  Database and false of JPL, which states the planets' accuracy in the
  2014 report the project stores. A visitor reads it as "JPL does not know
  how well it knows Mercury". Say instead: "JPL's Small-Body Database has
  no entry for a planet; the period is rounded to how much it changes in
  a year."
- **One-sigma versus three-sigma is already mixed in the codebase.** The
  observer table gives three-sigma (36, 37, 39); the vector table gives
  one-sigma. Whoever builds this should write the level into the cache
  record's field name (`range_3sigma_km`, not `range_sigma_km`) so the two
  cannot be confused later.
- **The sky-position line's attribution is a live [CRITICAL] finding**
  (Q6), independent of L-401. It is shipping a `# Source`-shaped claim
  ("JPL DE440/441 ephemeris") over a typed table. I would open it as its
  own ledger item rather than fold it into the distance work.
- **Digit count can flicker in animations.** A small body whose
  uncertainty sits near a decade boundary will print a different number
  of digits from one frame to the next. Harmless, but visible; if it
  bothers the eye, hold the place for the whole animation at the first
  frame's value and say nothing, since the difference is below the error.
- **Barycentre centres have no surface** (Q7); the surface line currently
  prints anyway, with radius 0.
- **The Sun as a body in an SSB-centred plot** has no stated accuracy and
  will fall to the floor. Recall, not sourced: its error is the planets'
  errors scaled by their mass fractions, so metres to tens of metres; too
  small to matter for a visitor, but the floor sentence handles it
  honestly without that reasoning.
- **Nothing is wrongly framed in the brief** except one word: "finding an
  honest error for each number" treats the error as a property of the
  number. It is a property of the *pair* -- the body and the centre -- and
  for small bodies of the date as well. The cache record should be keyed
  that way (body, centre, date), as the period record already is keyed by
  body and centre.

**Sources.** The code and rule text cited above; no new documents.

**Confidence.** High on the Mercury sentence and the sigma-level mixing,
which are read from the box and the live answers. Medium on the rest; they
are design observations.

## Where this leaves it, in three lines

- Small bodies get an honest distance error and an honest speed error from
  the position fetch itself, at no extra cost, once the fetch asks for
  `2xr`.
- Planets and the Moon are sourced by the 2014 report's words and need no
  fetch; the moons, spacecraft, Lagrange points and barycentres have no
  source yet and print at a stated floor with a plain sentence.
- The sky-position table is the one thing here that is wrong today rather
  than merely too long.
