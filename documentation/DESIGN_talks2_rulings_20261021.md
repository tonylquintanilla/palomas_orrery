<!-- Doc-Kind: hand | Design record, talks part 2 (Oct 21, 2026): four rulings -- the website draws Earth's dipole cone; the device for edges that move; reading an unsourced agency page one layer down is method, with its skill wording; the "report a problem" link's words. Zero code. -->
# Design record: talks, part 2 (October 21, 2026)

Built on orrery 6a8d04c ("talks", 2026-10-21 08:40) at
https://github.com/tonylquintanilla/palomas_orrery and gallery
30db99f ("daily run 10-21-26") at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Both
re-read with `git ls-remote` at the session's start (10:52) and
unmoved.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: DESIGN SESSION (zero code). A talk-only session run beside the
L-456 (the i panel's sources and links) addresses build, from the brief
"talks, part 2" that Claude Fable 5.1 wrote in the coordination session
of Oct 21 (attached to this chat; not in the repo at 6a8d04c, so cited
by title). Companion:
`HANDOFF_talks2_20261021.md`, whose section 3 carries the ledger lines
and the Where We Are changes. No repository file was edited.

Each ruling is in Tony's words with its time (Chicago). Every number
below was read from the store or worked out from its rows in this
session; none is recalled.

## Talk A. The website draws Earth's dipole cone (L-375, the dipole's offset, second half)

**Ruling, 11:36:** "draw Earth's dipole cone, as a new drawer row
starting unticked"

**A correction to the brief.** The brief said the cone would be "one
more trace in the Earth room's drawer under the dipole's row". There is
no dipole row. At gallery 30db99f the website draws nothing for Earth's
dipole: `data/objects_config.json` lists Earth's features as
earth_interior, earth_atmosphere, earth_exosphere, earth_orbital_zones,
earth_geostationary, earth_magnetosphere, van_allen_belts, hill_sphere
and orientation, and the dipole's tilt is served only as
`van_allen_belts.magnetic_tilt` (pointing at
`constants_new.py::EARTH_DIPOLE_TILT_DEG`), used inside the belts'
hover sentence. So the cone is a new feature and a new drawer row, not
a trace under an existing one.

**What was read to put it:**
- The orrery's cone: `planet_visualization_utilities.py`,
  `build_dipole_cone_traces` and `PLANET_DIPOLE` (about lines 755 to
  1050 at 6a8d04c). A magenta double cone (two `Mesh3d` nappes, opacity
  0.16) about the IAU spin pole, half-angle the tilt; one generator line
  at an arbitrary azimuth; a rim arc and arrowhead at each tip, sized
  and sensed like the rotation axis's spin arrow; one info marker at
  the north tip. Earth's apex is at the centre; its hover says the
  offset exists and why it is not drawn.
- The website's axis: `gallery/earth_geometry.js`, the Rotation Axis
  and Equator block (about lines 300 to 400 at 30db99f). It already has
  the pole basis, the axis half-length rule and the arrowhead
  construction the cone would reuse.
- The arrival block: Earth's `arrival.drawn` is `["crust"]`.

**For the build (method, from the skills, not further rulings):**
- It is a SERVED feature, so every one of its traces carries
  `meta.shell_key` (interactive-exhibit, A shell trace carries its
  key). Without the stamp it reads as a frame element and draws on
  arrival, against the ruling's "starting unticked". `smoke_arrival.js`
  must see it.
- Its tilt points at the same constant the belts' tilt does,
  `EARTH_DIPOLE_TILT_DEG`: one value, one home. Its words (name, hover,
  about, the offset sentence, the "one moment, every direction in a
  day" sentence) are served words on its row, written through
  `tools/store_writer.py`'s word fields, so the Typed facts check
  masks them (interactive-exhibit 1.18, the typed-fact rule). The
  orrery's hover wording is the starting draft; reworded hovers go to
  Tony before they ship.
- The offset sentence is the one already settled (talk 6(b) of
  2026-10-20): said in words, not drawn.
- Its info link is chosen at the build by the link rule (NASA if a
  page is specific to Earth's dipole, else Wikipedia), from a URL
  fetched live that day.
- Colour matches the orrery's magenta, `rgb(255, 93, 210)`, so the two
  instruments read the same (a declared drawing choice).
- Mode 5 on the phone, portrait first, before it is called done.

**Raised and not taken.** For Earth the cone is a choice, not a
necessity: the room knows the minute it was opened, and Earth's turning
angle is published, so the magnetic axis's real direction at that
minute could be drawn. (For Uranus it cannot be.) Put to Tony with the
recommendation; he ruled for the cone. Recorded so it is not re-raised
as new.

**Declined:** leaving the website with the tilt in words only.

## Talk B. The device for edges that move (L-454; the magnetopause, the bow shock, and their kind)

**Ruling, 11:46,** after a draft drawing (11:41: "Can you show me a
draft of option 2"): "That looks right and yes separate the two rows so
they don't clash by default. And please keep option 4 for future
consideration. Thanks."

**What is ruled:**
- Each model surface stays drawn sharp where it is drawn today. Beside
  it, two faint surfaces: the same model at the low and the high end of
  the range of conditions it was fitted to. The words say so, and say
  that a big storm can push the edge past the inner one.
- The magnetopause's faint pair and the bow shock's faint pair belong
  each to its own drawer row and show only with it, so the four dashed
  surfaces never appear together unless both rows are ticked. (Tony's
  "separate the two rows so they don't clash by default". The draft
  showed why: at high pressure the bow shock sits inside where the
  magnetopause is at low pressure.)
- Option 4, the surfaces moving with today's solar wind from NOAA
  (L-314), is kept for future consideration, not declined.
- It applies BY KIND, to every real edge that moves: the magnetopause,
  the bow shock, the Sun's Alfven surface, and the heliosphere's
  termination shock and heliopause. The Sun's slice applies it without
  a second talk.

**What was read to put it** (`constants_new.py` at 6a8d04c):
- `EARTH_SOLAR_WIND_PRESSURE_NPA = 2.0`, declared pending (L-314). Its
  `# Declared:` lines cite Shue et al. (1998) p. 17,695 for 2 nPa as an
  average, Shue's fitted range 0.5 to 8.5 nPa (p. 17,693), and
  Jelinek's recommended range 0.6 to 11 nPa (conclusion, para. 30).
- `EARTH_MAGNETOPAUSE_SHUE_SCATTER_RADII = 1.23` (p. 17,697) and
  `EARTH_BOW_SHOCK_JELINEK_SCATTER_RADII = 0.69` (fig. 7): scatter of
  crossings about each model, not the range the edge moves through.
  This is why option 1 was declined.
- Shue's coefficients A1 to A8 (10.22, 1.29, 0.184, 8.14, 6.6, 0.58,
  -0.007, 0.024) and cut angle 120 degrees; Jelinek's R0 15.02, eps
  6.55, lambda 1.17 and cut angle 105 degrees.
- `ALFVEN_SURFACE_RADII = 19.7` and the two range rows
  `ALFVEN_SURFACE_RANGE_LOW_RADII = 10`, `_HIGH_RADII = 20` (Cranmer et
  al. 2023, abstract, https://arxiv.org/abs/2310.05887).

**Worked out from those rows, at Bz = 0 (working figures for the
talk, not rows; a build prints from its own rows):**

| Surface, nose distance | low end | today | high end |
|---|---|---|---|
| Magnetopause, Shue, 0.5 / 2 / 8.5 nPa | 12.65 | 10.25 | 8.23 Earth radii |
| Bow shock, Jelinek, 0.6 / 2 / 11 nPa (its own range) | 16.24 | 13.51 | 10.42 Earth radii |

Geostationary orbit is 6.6 Earth radii; even the high-pressure
magnetopause stays outside it.

**For the build (method, following from the ruling's words "the range
it was fitted to"):**
- Each model takes its OWN paper's range. The draft drawing used
  Shue's 0.5 and 8.5 for both surfaces, for speed; the bow shock's
  pair is Jelinek's 0.6 and 11, so its numbers above differ from the
  draft's (16.70 and 10.83).
- The four ends become four measured rows (two per paper), each read
  from the open paper at the build and given `# Read:` lines; today
  they live only in a `# Declared:` comment. The faint surfaces are
  derived from them; nothing is typed in a renderer.
- The Alfven surface's 10 and 20 are a different kind of range from
  Shue's and Jelinek's: where the surface spends most of its time,
  which is motion, not a fit's validity. The words say which each is.
  The drawn 19.7 sits next to the high end, so the Sun's slice should
  look at whether the outer faint surface is distinguishable from the
  drawn one (a Mode 5 question there, not here).
- Faint means fewer, dimmer dots than the model surface: rendering
  settings, in the drawing code.

**Declined:** option 1, a band from the scatter, because it would be
read as the edge's range, which it is not. Option 3, words only, because
it leaves the ruling of 2026-10-17's second drawn device unbuilt. (The
brief recommended option 3; it assumed the pressure inputs still needed
sourcing, and the store showed they are already cited in an open paper.)

## Talk C. Reading an unsourced agency page one layer down: the skill's

**Ruling, 11:49:** "The skill's and ask in your design to amend the
skill not just add to the ledger."

So this record carries the amendment itself, for the next build that
bumps provenance-discipline (2.33) to paste in. It is not bumped by
this session (one session, one bump; the build session owns the skills
today).

**Where:** provenance-discipline, The Access Standard, directly after
the paragraph beginning "**A source names what was OPENED, not what it
cites.**" and its L-321 note.

**The paragraph to add, as written:**

> **An agency summary that names no source is a lead, not a source.**
> A page from an agency or a university that states a figure and names
> no work it comes from -- a fact sheet, an outreach page, a course
> page -- is not cited for that figure where a scientific work behind
> it exists. Read one layer down: find the paper, model or data set the
> figure comes from, open it, and cite that, under the rules above. An
> agency page that names its source stays a good copy to open, and
> where the agency itself made the measurement its page is the source.
> When summary pages disagree and none names a source, that is the
> signal to go down a layer, not to pick one. Where no work behind the
> figure can be found or opened, the figure is removed and the gap
> noted (Fetched vs Recalled).
>
> (Tony's ruling, 2026-10-21, that this is method. The case, 2026-10-20:
> the chromosphere's temperature, where NASA's Sun Fact Sheet,
> NASA/Marshall and Montana State gave different figures and none named
> a source; the figure came from Carlsson (2007), the model they
> summarise.)

**Why it is method** (the protocol's Method Belongs to the Skill): it
resolves the same way next month for a different constant, a different
body, a different file. It narrows the Access Standard's open route 1,
which ranks "agency documents" as open full text, to the agency pages
that name their source or report the agency's own measurement.

## Talk D. The "report a problem" link (L-458)

**Rulings:** 11:55 "Approved and please add the same info button that
is in the front page that has my name and email."; 11:57 "A" (the About
card opened from inside the i panel); 11:58 "Yes" (the report carries
the page's address).

**The words, approved, exactly as a visitor reads them** (the room and
feature filled in by the page; the Sun's corona as the example):

1. The link's label in the i panel: `Report a problem`
2. The line beside it: `Opens our guest book with a note already
   started. Reports go privately to the person who keeps this gallery
   and are never shown in the lobby.`
3. The message's first line, which the guest book updater recognises as
   a report: `Problem report -- Sun room, Corona`
4. The prompt lines under it:
   - `What looks wrong? It might be a number, a sentence, a source, a
     link, or the drawing.`
   - `If you know a better source, please name it:`
5. The message's last line (11:58): `Page: <the room's address>`, for
   example `Page: https://palomasorrery.com/interactive.html?exhibit=sun`.
   Labelled so it reads as information, not a prompt. It names the room
   only, not what was ticked or how the view was turned; the room and
   feature are also in the first line.

**Changed from the ledger's first draft:** the question is a sentence
with its choices after it, so it reads on a phone without a bracket;
item 2 is new (the ledger asked for it and had no words); item 2 says
"the person who keeps this gallery" rather than Tony's name, because
what a visitor reads carries no names; item 5 is new.

**About this gallery (11:55, 11:57, option A).** Under the report link,
a line `About this gallery` opens the front page's About card -- the
one `index.html` opens from its footer "i" button at 30db99f (id
`about-overlay`, about line 2359): what Paloma's Orrery is, the
Instagram and source-code links, the credit line, the licence, and
`tonyquintanilla@gmail.com`. So a visitor deciding whether to report
can see who keeps the gallery and write to him directly.
- Option A, not B: one "i" button in the room. B, a second corner
  button, was declined because the room's chrome already uses "i" for
  the feature panel and two "i" buttons would read as one.
- It is the SAME card, shared, not a copy in `interactive.html`
  (interactive-exhibit, One chrome, many rooms; the rule that logic a
  build touches moves to its own file). How it is shared is the
  build's call.

**For the build:**
- Items 1, 2, 4 and "About this gallery" are typed sentences about how
  to use the page. The Typed facts check (`smoke_typed_facts.js`) will
  find them; each joins its ALLOWED list as "how to use the page", and
  the row prints the additions.
- The guest book updater shows a message beginning `Problem report` to
  Tony as a report, private, never offered for the lobby (already on
  L-458).
- Tony-action (do), at the build, unchanged from L-458: in the guest
  book form's editor, "Get pre-filled link" once.

## Where this leaves us

- The website will draw Earth's dipole as the orrery does, and every
  real edge that moves gets two faint surfaces at the ends of its
  model's range, with the live solar wind kept for later.
- The "go one layer down" rule is written out, ready for
  provenance-discipline's next version.
- The report link's words are settled, with the About card and the
  page's address beside it; all four wait for builds.

Record written October 21, 2026 with Anthropic's Claude Opus 5.5.
