<!-- Doc-Kind: hand | Review request, for an outside model (GPT or Gemini), carried by Tony: is our rule for how many digits a distance prints the standard practice, and where do professionals get position uncertainties by class of body. Belongs to L-560 (a digit is earned). Communication. -->
# Review request: how many digits may a public page print for a body's distance?

For Tony: paste everything below the line into GPT or Gemini, and bring
the reply back to a session. Sending it to both gives two independent
readings; one is enough to start.

---- paste below this line ----

Built on orrery 489e4128056cd08fa46b0c11b90c64fe477ab028
at https://github.com/tonylquintanilla/palomas_orrery (branch main)
and website fafdaeb6ce199b0d5f436dc4c77870f7d1c5c33e
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
(branch main), both read 2026-11-27, 08:53 Chicago. The talk this
request comes from is recorded in the orrery's ledger, item L-560, in
a note of Nov 27 that was not yet pushed when this was written.
Everything you need is in this request.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Rules this work runs under. If you can fetch from GitHub, read
`PROJECT_INSTRUCTIONS.md` and `skills/provenance-discipline/SKILL.md`
in the orrery repository at the commit above, and say in your reply
which of the two you actually read. If you cannot fetch, say so; the
two rules that matter here are these:
- A number is either fetched from a source or it is removed. A
  plausible number from memory is not acceptable. If you cannot quote
  a source for a figure, say "recalled, not verified", or say you do
  not know. "I do not know" is a good answer.
- A citation must be true, not just present. For every figure give
  the source, the place in it (page, section or table), a link, and a
  short exact quotation.

Who you are writing for. Tony Quintanilla is a retired civil and
environmental engineer, an artist and an anthropologist. He is not an
astronomer and not a programmer, and he calls himself an amateur here.
He makes every decision on this project. Write in plain language and
explain a technical term the first time you use it. Do not propose
code.

## The situation

Paloma's Orrery (palomasorrery.com) is a public website that draws the
solar system. Every position comes from NASA JPL's Horizons service.
When a visitor taps a body, a box prints its distance, for example:

    0.32001664 AU from the Sun (47,873,807 km)

Tony's concern: a lay visitor reads all those digits as true, and for
many bodies nothing supports them. His objective, in his words: "show
what we know at its correct accuracy and precision, and its source."

The rule we have settled on:
- The number of digits printed is precision. What earns a digit is an
  uncertainty: the source's own statement of how far the truth may be
  from its number.
- A box prints only the digits a sourced uncertainty supports, and
  names that source. The digits JPL prints are never themselves the
  evidence.
- Where to get the uncertainty, in order: (1) JPL's own figure for
  that body; (2) the standard source for its class of body; (3) the
  published literature.
- Only the uncertainty's order of magnitude is needed, since that
  decides which place the figure rounds to.

What we have so far:
- Planets: one row each from JPL's 2014 planetary ephemeris report:
  Mercury, Venus, Earth and Mars 1 km; Jupiter and Saturn 100 km;
  Uranus, Neptune and the Pluto system 10,000 km.
- The Moon 0.001 km; Phobos and Deimos 10 km, from the 2025 paper on
  JPL's MAR099 ephemeris.
- Asteroids, comets on closed orbits and dwarf planets: Horizons
  serves a 1-sigma uncertainty with the position (its vector table
  with uncertainties); we print to three times that. 52 bodies.

What we lack, 41 boxes that today print whole kilometres:
- Moons: Io, Titan, Pluto and Charon. JPL's page "Planetary Satellite
  Ephemerides" names their ephemerides: JUP365 (reference: R. A.
  Jacobson, 2021, listed as a personal communication), SAT441
  (Jacobson 2022, AJ 164:199), PLU060 (Brozovic and Jacobson 2024, AJ
  167:256). We read JUP365's own comment file from NAIF: it states no
  uncertainty for any moon.
- 21 spacecraft, among them Voyager 1 and 2, New Horizons, Juno,
  Parker Solar Probe, BepiColombo, and ended missions such as Pioneer
  10 and 11 at their last contact.
- 13 comets and interstellar objects drawn as paths, among them C/West
  (1975 V1), 1I/'Oumuamua and 3I/ATLAS; and Halley, Ikeya-Seki and
  Bennu, for which Horizons states no uncertainty.

## The questions

1. Is this rule the standard practice? How do the professional
   producers decide how many digits to print for a position or a
   distance: the Astronomical Almanac, JPL Horizons, IMCCE in Paris,
   the Minor Planet Center? Is the rule written down anywhere we can
   cite?

2. Does a citable table or document exist that gives position
   uncertainty by class of body: planets, the major moons of each
   planet, spacecraft? If one exists, name it with its place and a
   link. If none exists, say so plainly.

3. For Jupiter's four large moons under JUP365: which published source
   states how well their positions are known, and what is the order of
   magnitude in kilometres? Give the quotation and its place.

4. The same for Titan under SAT441, and for Pluto and Charon under
   PLU060.

5. For interplanetary spacecraft: is there any statement, citable for
   the whole class, of how well a trajectory is known? Please keep
   three cases apart: a craft being tracked now; a mission that has
   ended, at its last contact; and a predicted path. Or must each
   mission be looked up on its own, and where?

6. For a comet or interstellar object not observed for years or
   decades: does JPL give an uncertainty for its present position, how
   fast does it grow, and is printing any distance for it defensible?

7. An alternative we are weighing. Decide first how many figures a lay
   reader can use, say four significant figures, and print no more
   than that for any body. A source is then needed only to show that
   the uncertainty is smaller than the last printed digit. Is that how
   printed almanacs and NASA's public pages work? What are its
   weaknesses?

8. Have we mixed anything up between precision, accuracy and
   uncertainty? In particular: a formal uncertainty from an orbit fit
   against the true error; and one sigma against three sigma. Which
   should a public page use, and say?

## What to send back

- An answer to each question by its number, the plain answer first.
- For every figure: the source, its place, a link, and a short exact
  quotation; or the words "recalled, not verified".
- Where the honest answer is that no standard exists, say that.
- Which of the project's rule files you read, or that you could not
  fetch them.

Written November 2026 with Anthropic's Claude Fable 5.2.
