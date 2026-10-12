# Review request for GPT: how many digits the orrery's distances earn (L-401)

Built on orrery 28a4636717920e86965f2e1777f3bf92386d1bb6 at
https://github.com/tonylquintanilla/palomas_orrery ("L431_4 _5 period in
hovers"), with gallery e3536c8732d7b62faa5c09515e4b7f1d1c10af9c at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, which this
question does not touch.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\;
gallery C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\.
Written October 11, 2026 with Anthropic's Claude Opus 5.5, for ledger
item L-401 (the orrery's distance hovers, printed by the errors they
earn).

**The rules this work runs under.** You have no resident copy of this
project's protocol or skills. Please also fetch these, at the same
commit, 28a4636717920e86965f2e1777f3bf92386d1bb6, and say in your header which ones you actually read:

- `PROJECT_INSTRUCTIONS.md` (the project's protocol; the sections
  "Fetched vs Recalled Convention" and "Show the Envelope of the
  Unknowable")
- `skills/provenance-discipline/SKILL.md` (the sections "A Computed
  Position Prints What Its Errors Earn", "An Accuracy Stated in Words
  Is Stored as the Place It Reports To" and "The Access Standard")
- `skills/provenance-discipline/references/figures.md` (the paragraph
  "The ceiling", and its Report test)
- `skills/horizons-orbital-mechanics/SKILL.md`
- `skills/orrery-coding-conventions/SKILL.md` (the section "Hover Text
  Is Written for the Visitor")

## Who this is for, and the person asking

Tony Quintanilla, PE, is a retired civil and environmental engineer, an
artist and an anthropologist. He is not a professional programmer or a
trained astronomer. He builds Paloma's Orrery, a Python program that
draws the solar system in 3D from NASA JPL Horizons data, through
conversation with AI partners, and he makes every judgment call. The
code's structure and discipline come from that collaboration, not from
his own programming; please do not read the code's quality as evidence
of a programmer's fluency. Write your answer for him: plain words, each
technical term explained the first time.

He is asking three reviewers (Claude Fable, GPT and Gemini) the same
question separately. Your answer is compared with the others, not
shown to them.

## What to send back

One markdown file, which Tony will save as received. It opens with a
header:

    Model: <your model name and version>
    Effort tier: <the reasoning or effort setting this answer used>
    Date: <today>
    Rule files read: <each file you actually opened, by path>
    Pre-flight: <the sentence you quoted, and its URL>

Then one section per question (Q1 to Q9), each with:

- **Recommendation** -- what you would do, in one or two sentences.
- **Reasoning** -- why, in plain words.
- **Sources** -- only documents you opened in this session. For each:
  the title and authors as printed on the document, the URL as a bare
  address inside a code block, where in it (page, section, table), and
  a short verbatim quotation of the sentence that supports you. A
  source without a quotation is treated as recalled, not read.
- **If you say no source exists** -- the searches you ran and where you
  looked. "No source states this" is a claim about your search.
- **Confidence** -- high, medium or low, and what would change it.

Recall from training is welcome as reasoning, labelled as recall. It is
not a source.

**Pre-flight, before anything else:** open the Horizons manual at the
address below, find the definition of observer-table quantity 39 (the
range uncertainty), and quote it in your header. If you cannot open web
pages, say so in the header and answer from reasoning alone; that is
useful too, as long as it is labelled.

```
https://ssd.jpl.nasa.gov/horizons/manual.html
```

## The problem

When you hover over a body in the orrery's 3D plot, a text box shows
where it is. Here is the box for Mercury and for Sedna, exactly as the
program printed them on 2026-10-11 at 19:41 UTC, in a plot centred on
the Sun:

    Mercury
    Position at: 2026-10-11 19:41:00 UTC
    Right Ascension: 14h 40m 36.096s
      (apparent, +/-0.005 arcsec, JPL DE440/441 ephemeris)
    Declination: -18 deg 36' 52.99"
      (apparent, +/-0.005 arcsec, JPL DE440/441 ephemeris)
    Distance from Center: 0.4381591083 AU
    Distance: 6.5547669633e+07 kilometers
    Distance: 3.6440581856 light-minutes
    Distance: 0.0607343031 light-hours
    Distance to Center Surface: 6.4851969633e+07 kilometers
    Velocity: 0.0242129730 AU/day
    Velocity: 150,925.38 km/hr (41.924 km/sec)
    Orbital period: 0.240845 years (87.969 days)
    Around the Sun, from JPL Horizons, fetched 2026-10-11.
    Rounded to how much the period changes in a year;
    JPL lists no orbit uncertainty for this body.

    Sedna
    Right Ascension: 04h 10m 36.214s
      (apparent, +/-0.10 arcsec, JPL Horizons 3-sigma)
    Declination: +08 deg 54' 50.15"
      (apparent, +/-0.10 arcsec, JPL Horizons 3-sigma)
    Distance from Center: 82.8297793403 AU
    Distance: 1.2391158620e+10 kilometers
    Distance: 688.8742689149 light-minutes
    Distance: 11.4812378152 light-hours
    Distance to Center Surface: 1.2390462920e+10 kilometers
    Velocity: 0.0025684604 AU/day
    Velocity: 16,009.84 km/hr (4.447 km/sec)
    Orbital period: 11,390 years (4,160,000 days)
    Around the solar system's center of mass, from JPL Horizons, fetched 2026-10-11.
    Rounded to JPL's stated uncertainty in the orbit.

The orbital period line is new. It is printed by a rule the project
adopted: **a number shows only the digits its error supports.** The
period's error is the larger of two: how much the period itself
changes over a year, and JPL's stated uncertainty of the orbit fit
from its Small-Body Database, where the body has one. The digits are
then set by a "Report test": choose the decimal place whose implied
half-width (half a unit of that place) is closest, on a log scale, to
the error, with a tie going to the coarser place. Years and days are
each placed by their own error.

Every other number in the box is printed with a fixed width chosen
long ago: ten decimal places of an AU, ten significant figures of a
kilometre. Sedna's distance is printed to about ten metres. Tony wants
the distances and velocities printed by the same rule as the period.
That is the item under review (ledger item L-401). The difficulty is
finding an honest error for each number.

## What the project has found so far

These are facts read, not proposals:

1. **Planets and Pluto.** The project stores three rows from JPL's
   2014 ephemeris report (Folkner et al., "The Planetary and Lunar
   Ephemerides DE430 and DE431", IPN Progress Report 42-196). Its
   abstract gives the accuracy in words: the terrestrial planets'
   orbits to "a few hundred meters", Jupiter and Saturn to "tens of
   kilometers", Uranus, Neptune and Pluto to "several thousand
   kilometers". The project stored the decimal place those words
   report to (1 km, 100 km and 10,000 km), not a number the report
   never printed, and uses half a unit of that place as the error.
   Horizons now serves DE440/441 (Park et al. 2021), which the project
   reads as improving Jupiter, Saturn and Pluto and leaving Uranus and
   Neptune about the same, so the 2014 rows are a conservative bound.
   The rows: `constants_new.py`, lines 3522 to 3595.
2. **Small bodies.** Horizons gives a 3-sigma range uncertainty per
   body per date (observer-table quantity 39). Asked from the Sun's
   centre for 2026-10-12 00:00 UT, it returned Sedna's distance as
   82.8299853426285 AU with RNG_3sigma 257,817.569 km and a range-rate
   3-sigma of 0.0002397 km/s. For Mercury the same columns read "n.a."
3. **The bodies with nothing yet:** the Moon and the planets' moons,
   spacecraft, Lagrange points, barycentres, and the Sun itself.
4. **Velocity.** No source the project has found gives an accuracy for
   a body's speed, except a small body's range rate in item 2, which is
   only the part of the speed along the line of sight.
5. **Not always the Sun.** A plot can be centred on a planet, a moon
   or a barycentre. The distance is then between two bodies, each with
   its own error.
6. **The sky-position line.** The "+/-0.005 arcsec, JPL DE440/441
   ephemeris" shown for Mercury comes from a typed table in
   `celestial_coordinates.py` (`MAJOR_BODY_UNCERTAINTIES`), whose
   values have no recorded source. The small bodies' figures ("JPL
   Horizons 3-sigma") are fetched live, from observer quantities 36
   and 37.
7. **Cost.** The orrery already asks Horizons, per body per plot, for
   the position (vectors) and for the sky position with its
   uncertainty (from Earth's centre). Asking for quantity 39 from the
   plot's centre would be one more question per body per plot. An
   animation draws many frames.
8. **The derived lines.** Light-minutes, light-hours and the distance
   to the centre's surface are the same distance in other units, or
   minus a radius.

## The questions

- **Q1. Sources by kind of body.** For each kind -- planets and Pluto;
  small bodies; the Moon; other planets' moons; spacecraft; Lagrange
  points; barycentres; the Sun -- where should the distance error come
  from? Is there a better open source than the 2014 report for the
  planets, for instance the DE440 paper or a Horizons product?
- **Q2. One rule, two kinds of figure.** The planets' error is a
  2014 statement in words, the same every day; a small body's is a
  3-sigma figure computed for that date. Is it sound to print both by
  the same rule in the same box? Which level should the Report test
  take from a 3-sigma figure: the 3-sigma as given, one-sigma, or
  something else? How should the box tell a visitor which kind it is?
- **Q3. No stated error.** What should the box print for a number with
  no stated error? Options seen so far, not exhaustive and not ranked:
  a fixed floor (the project's website prints whole kilometres); the
  number as now with a note that no accuracy is known; leaving the line
  out until a source is found. Say what you would do and why.
- **Q4. Velocity.** Is there an honest source or derivation for the
  accuracy of a body's velocity, planets and small bodies? If not,
  what should the velocity lines do?
- **Q5. A centre other than the Sun.** How should two bodies' errors
  combine? Does Horizons' quantity 39, asked from that centre, already
  account for it?
- **Q6. The sky-position line.** What is the honest replacement for
  the typed planetary table in item 6?
- **Q7. The derived lines.** Do they simply carry the same error? Are
  all four distance lines worth keeping?
- **Q8. Cost.** Is there a cheaper honest route than one more Horizons
  question per body per plot, for instance because the uncertainty
  changes slowly and could be kept for a day per body?
- **Q9. What we missed.** Anything framed wrongly, or missing.

## Files to look at

All in the orrery repository at the anchor above:

- `visualization_utils.py` -- `format_detailed_hover_text`, which
  builds the box.
- `formatting_utils.py` -- the two fixed-width formatters it uses.
- `celestial_coordinates.py` -- `MAJOR_BODY_UNCERTAINTIES` and
  `get_precision_note`.
- `palomas_orrery.py` -- `fetch_position` (line 1233) and
  `fetch_radec_for_hover` (line 1796).
- `constants_new.py` -- the three planetary accuracy rows, lines 3522
  to 3595.
- `orbital_period.py` -- how the period line applies the rule; the
  model the distances would follow.

Thank you. This is a design question, and disagreement with the
framing is as useful as an answer.
