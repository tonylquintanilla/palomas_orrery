<!-- Doc-Kind: hand | Brief for a talk-only session, run in parallel with the L-456 addresses build: the two Earth questions stopped on Oct 20 by the Stale Skill gate (the website's dipole cone, the device for edges that move), one method-or-Tony's question, and the "report a problem" message's words. Zero code; no patch; the rulings go to a design record and a handoff for the next close. -->
# Brief: talks, part 2 (a talk-only session, in parallel with a build)

Built on orrery 6a8d04c ("talks", 2026-10-21 08:40) at
https://github.com/tonylquintanilla/palomas_orrery and gallery
30db99f ("daily run 10-21-26") at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Run
`git ls-remote` on both at the start and read the newest handoff if
either has moved: a build session is running beside this one and may
push during it.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: DESIGN SESSION (zero code). Written October 21, 2026 by
Anthropic's Claude Fable 5.1, in a coordination session, for a Claude
Opus talk session. Follows `HANDOFF_design_talks_20261020.md`,
section 5 (what was stopped), and its record
`DESIGN_talks_rulings_20261020.md`, talk 6.

## 1. Read this first

- *This session builds nothing and edits no repository file.* A build
  session (`HANDOFF_L456_addresses_build_brief_20261021.md`) is
  running at the same time; it owns the ledger, Where We Are, the
  skills and the protocol for the day. Two patches on those files
  from two sessions would collide. So this session's output is two
  attachments for Tony's orrery `documentation/`: a design record and
  a handoff whose section 3 lists the ledger lines and the Where We
  Are changes for whichever session closes next. Tony's words of
  2026-10-20 apply: "This is a talk only session. No builds to avoid
  conflicts."
- Load interactive-exhibit and confirm the loaded copy reads 1.18
  (the manifest at 6a8d04c; the reinstall was done 2026-10-20). That
  was the gate that stopped talks (b) and (c) last night. If the
  loaded copy reads 1.17, stop and tell Tony, as the gate says. If the
  build session has pushed a 1.19 by the time this session loads
  (the drawer-order rule), the manifest will say 1.19 and the loaded
  copy 1.18: that is also a stop; say so and ask Tony to reinstall,
  or hold the two Earth questions and do items 3 and 4 only.
- Also load provenance-discipline 2.32 (item 3) and
  ledger-and-session-records 1.21 (the record and handoff).
- Tony is likely on his phone. One question per message, plain
  words, every handle with its label. He can look at the live site;
  he cannot run the desktop orrery.

## 2. The talks, in order

### Talk A. Does the website draw the dipole cone? (L-375, the dipole's offset, second half; re-homed from L-234)

- What it is: the orrery draws Earth's dipole as a cone, the swept
  envelope of every direction the dipole axis could point over a day,
  since neither instrument models Earth's rotation phase (the
  protocol's Show the Envelope). The website draws Earth's rotation
  axis with a cone HEAD (`gallery/earth_geometry.js`, "the axis
  half-length, cone head at the end, as the orrery draws") but NOT the
  dipole's swept cone. No ruling against drawing it on the website was
  ever found (L-375's note of 2026-10-04).
- Settled already: the offset of the magnetic centre is said in the
  dipole's hover in words, not drawn (talk 6(b), 2026-10-20, "A");
  IGRF-14 is confirmed for the six rows (talk 6(a)); the belts are a
  density field tilted to the dipole (L-330). The tilt itself comes
  from the IGRF rows (about 9.4 degrees for 2020; about 9.2 for 2025
  once IGRF-14 lands).
- To do before asking: read how the orrery draws the cone
  (`earth_visualization_shells.py`, the dipole block near line 1194)
  and how the website draws the axis head, so the cost is concrete:
  the website already has the tilt, the pole and the cone primitive;
  a swept cone is one more trace in the Earth room's drawer under the
  dipole's row.
- The question for Tony (Mode 5, with a sketch in words or a quick
  headless render if the session can make one): draw the swept cone
  on the website as the orrery does, under the dipole's existing
  drawer row; or leave the website with the tilted axis and the words.
  Recommendation to offer: draw it, because the cone is the device
  talk B is about to reuse, and the Earth room is the template for the
  other planets' rooms (L-433).
- Where to read: L-375; L-234's close; `DESIGN_talks_rulings_20261020.md`
  talk 6(b); the protocol's Show the Envelope.

### Talk B. The device for edges that move (L-454; the magnetopause, the bow shock, and their kind)

- What it is: Tony's ruling of 2026-10-17 split fuzzy boundaries three
  ways (`DESIGN_fades_rulings_20261017.md`): nature thinning out is a
  FADE; an edge known only as a range is a drawn CHOICE with words; a
  REAL EDGE THAT MOVES stays sharp at its model and gets "a second
  drawn device like the movement cone we use for the dipole." Which
  device, and what it shows, was split off as L-454.
- The store already holds the spread: the magnetopause's crossings
  scatter about Shue et al. (1998)'s model with a standard deviation
  of 1.23 Earth radii; the bow shock's about Jelinek et al. (2012)'s
  with 0.69 Earth radii. Both numbers are the crossings' scatter about
  the model under the conditions sampled, NOT the range the edge moves
  through as the solar wind changes (a storm pushes the magnetopause
  inside geostationary orbit, 6.6 Earth radii, from a quiet 10 or 11).
- What the Sun decided, so Earth can take it or not: the Alfven
  surface is drawn sharp at 19.7 solar radii (Kasper et al. 2021,
  Parker's first crossing), the corona's dots END there (L-410, built
  2026-10-20), and the range it moves through, about 10 to 20 solar
  radii (Cranmer et al. 2023), is in WORDS only (L-228, done
  2026-10-17). So the Sun has no second device yet; its edge is a
  sharp model surface with a sourced range in the hover. Say this to
  Tony plainly: the Sun's slice did not meet this question first,
  though the ledger thought it might.
- Options to put, one at a time, each with its honest cost:
  1. A translucent band either side of each surface, half a standard
     deviation wide or one, drawn from the two scatter rows. Cheap;
     but a band drawn from a standard deviation shows where crossings
     were measured, not where the edge goes in a storm, and the words
     have to say so.
  2. Two faint surfaces at the quiet and storm positions, from
     sourced solar-wind pressures. Both models already take pressure
     as an input: `EARTH_MAGNETOPAUSE_STANDOFF_RADII` and
     `EARTH_BOW_SHOCK_STANDOFF_RADII` are computed from
     `EARTH_SOLAR_WIND_PRESSURE_NPA`, a DECLARED 2.0 nPa (row near
     line 1939). So a storm surface is the same expression at a
     second, sourced pressure: one or two new measured rows (a
     quiet and a storm dynamic pressure, with their sources). This
     shows motion, which is what the ruling asked for, at the cost
     of sourcing those inputs.
  3. Words only, as the Sun does today: the model surface sharp, the
     hover giving the scatter and the storm range with their sources.
     No device. Honest; but it leaves the ruling's "second drawn
     device" unbuilt for every edge of this kind.
  4. Live: the surface moves with today's solar wind from NOAA SWPC
     (L-314, already on Earth's list as talk 4, with the aberration
     taken early). Not a device for the scatter; a different answer
     to the same question, and the one that makes 2 unnecessary.
  The recommendation to offer: 3 now for both rooms (it is what the
  Sun already does, and it costs nothing), with 4 as the device when
  L-314 is built, and 1 and 2 declined because a band drawn from a
  standard deviation would be read as the edge's range, which it is
  not. But present all four; the convergence is Tony's.
- Whatever is ruled applies by kind, not per edge: the magnetopause,
  the bow shock, the Alfven surface and the heliosphere's edges
  (termination shock, heliopause) are one class. Record the ruling so
  the Sun's slice can apply it to its three without a second talk.
- Where to read: L-454; L-314; L-305 (the magnetosphere's rebuild,
  closed, where the two scatter rows came in); `constants_new.py`
  rows EARTH_MAGNETOPAUSE_SHUE_* and the Jelinek rows; L-228 and
  L-410 for the Sun's edge.

### Talk C. Method or Tony's? Reading an unsourced agency page one layer down

- What it is: in talk 1 of 2026-10-20 (the chromosphere's
  temperature), three summary pages (NASA's Sun Fact Sheet,
  NASA/Marshall, Montana State) disagreed with each other and none
  named a source; the answer came from reading the scientific model
  they summarise (Carlsson 2007). The talks handoff left one line for
  Tony: is "an agency summary page that names no source is read one
  layer down, to the scientific work, before its figure becomes a
  row" a rule for provenance-discipline, or a ruling of his for that
  case?
- The protocol's test (Method Belongs to the Skill): would the answer
  be the same next month for a different constant, a different body,
  a different file? It would. So the session's own recommendation is
  that it is method, and the ask is one line: "is this mine or the
  skill's?" If Tony says the skill's, it goes on the ledger as a line
  for provenance-discipline's next version (2.33), riding whichever
  build next bumps that skill (one session, one bump); it is NOT
  bumped by this session. Note for the rule's wording: The Access
  Standard already ranks "an agency's own page or document" as an
  open route; this rule narrows it: an agency page that names its
  source is fine as the copy opened; one that names none is a lead,
  not a source, where a scientific work exists.

### Talk D. The "report a problem" message's words (L-458)

- What it is: Tony's idea of 2026-10-20, confirmed: every room's i
  panel gets a link that opens the guest book's Google Form with its
  message box already written, naming the room and the feature, for
  the visitor to edit and send; reports land in the guest book's
  sheet and the Daily Run shows them to Tony, kept private, never
  offered for the lobby. The ledger's Gap says the message's words
  come to Tony as a list first. The first draft, from L-458: "Problem
  report -- Sun room, Corona. What looks wrong (a number, a sentence,
  a source, a link, or the drawing)? If you know a better source,
  please name it:"
- To do before asking: draft the words list: the link's label in the
  panel; the pre-filled message (its first line, which the updater
  will recognise as a report; the prompt lines); and the one line the
  panel shows beside the link saying where the report goes. Plain
  words, no project terms, nothing typed that a row serves (What a
  Visitor Reads). Also one question of mechanism Tony can answer from
  the phone: whether the link should carry the page's address (the
  room and feature as the visitor saw them) in the pre-filled text,
  so he can open the same view.
- The question for Tony: approve or mark the list, one item at a
  time. The Tony-action (do) at the build (the form's "Get pre-filled
  link", once) stays on the ledger for the build; not this talk.

## 3. Not in this brief

- Earth's talks 3 to 6 on L-413 (L-321, L-314's fetch, L-297 and
  L-294, L-374 and L-061): they wait behind the Sun's slice (ruling of
  2026-10-17). If talk B lands on option 4, say in the record that
  L-314 moves up, and leave the decision of when to Tony's next
  coordination session; do not hold talk 4 here.
- The not-urgent items on Where We Are (whether the editor edits the
  Solar System room's rows; choosing a date, and animation).
- Anything the build session is doing: the addresses, the drawer
  order, the fourteen pairs.

## 4. At the close

- Design record `documentation/DESIGN_talks2_rulings_<date>.md`, one
  section per talk, each ruling in Tony's words with the date, what
  was read to put it (with addresses), and the options declined.
- Handoff `documentation/HANDOFF_talks2_<date>.md`: the anchor;
  section 3 the ledger lines by handle (L-375, L-454, L-413, L-458,
  the provenance-discipline line if talk C says skill), and the Where
  We Are changes (Waiting on you: the three questions leave the list;
  Settled: the new dated lines); section 5 what is still open; section
  6 the skill versions this session loaded.
- Both go to Tony as attachments for the orrery's `documentation/`.
  No patch. The close patch that carries them is the next build
  session's (the addresses session if it is still open; otherwise the
  one after), and that handoff says so in its first line.
- Close with two or three lines of "Where this leaves us".

Brief written October 21, 2026 with Anthropic's Claude Fable 5.1.
