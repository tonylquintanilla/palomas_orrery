<!-- Doc-Kind: hand | The words for the Sun room's eight held numbers (L-411), before and after, for Tony's approval before anything is written. -->
# The Sun's eight held numbers: the words, for your approval

Tony Quintanilla, PE | Claude Opus 5.5 (Claude Code) | November 2, 2026

Built on orrery 26a6dd04a15d3a261749fcb89078a80789b00790 at
https://github.com/tonylquintanilla/palomas_orrery and website
8c3947c19e2ec0bcd0ff891194453cf88865eb96 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.

From the brief `COORD_L411_sun_eight_held_numbers_brief_20261102.md`.
Nothing below is written yet. Each item says what a visitor reads now,
what I propose, and why. Every source was opened this session, from
the paper's own text, not from memory or a summary.

## In one look

| # | What | Proposal | Words change? |
|---|---|---|---|
| 1 | Core: centre temperature and density | print both from new rows (Bahcall 2001) | yes: 15 million becomes 16,000,000 |
| 2 | Radiative zone: 7 million to 2 million | top from a new row; "7 million" removed | yes |
| 3, 4 | Chromosphere's name "(2,000 km skin)" | name becomes "Chromosphere" | yes, on both sites |
| 5 | Chromosphere temperatures | your approved words of Oct 20, kept | one finding below |
| 6 | Alfven surface "April 2021" | no change to the words | no |
| 7, 8 | Hills cloud "A 2025 computer model" | the year moves into brackets | yes, slightly |

## 1. The core (website, the i panel)

Now: "It is about 15 million kelvin at the very center, where the gas is
about 150 times as dense as water under the weight of the layers above."

Proposed: "It is about 16,000,000 kelvin at the very center, where the
gas is about 150 times as dense as water under the weight of the layers
above."

- Source opened: Bahcall, Pinsonneault and Basu (2001), "Solar Models:
  current epoch and time dependences, neutrinos, and helioseismological
  properties", Table 5, the standard model: 15.696 million kelvin and
  152.7 grams per cubic centimetre at the centre.
- Why 16 and not 15: 15.696 rounds to 16, not 15. The old "15" came from
  NASA/Marshall's page, which gives 15,000,000 degrees Celsius.
- How many figures: two. The same table lists the paper's other models
  of the Sun, and they agree only to two figures (15.6 to 15.8 million;
  148 to 155 grams). That reason is written on each row.
- Why "16,000,000" and not "16 million": the website prints a number
  from a row in full digits. "16 million" would need a small new
  printing form in the website's code. Say if you want that instead.
- "Times as dense as water": the row is in grams per cubic centimetre,
  and water is one gram per cubic centimetre, so the number is the
  same. I write that on the row as a note.
- The core's citation on the i panel also changes: NASA/Marshall's
  sentence about the temperature and density comes off it, since the
  numbers now come from Bahcall et al. Its sentence about the core's
  size stays.

## 2. The radiative zone (website, the i panel)

Now: "Temperatures fall from about 7 million kelvin near the core to
about 2 million at the top of the zone."

Proposed: "Temperatures fall outward through it, to about 2,200,000
kelvin at the top of the zone."

- Source opened: the same paper, Table 6, the standard model: 2.18
  million kelvin at the base of the convection zone, which is the top of
  the radiative zone. Two figures, for the same reason as item 1, so
  2,200,000.
- The "7 million near the core" is removed. No source I could open gives
  it. The paper's own model table, which would, sits behind a robot
  check on the Institute for Advanced Study's site that I am not allowed
  to pass. The older 1995 table is only a PostScript file. NASA/Marshall
  gives 7,000,000 degrees Celsius and names no source.
- If you would rather keep it: open
  http://www.sns.ias.edu/~jnb/SNdata/Export/BP2000/bp2000stdmodel.dat in
  your browser, and read the temperature on the line where the radius
  column reads about 0.25. The sentence would then read "from about
  N kelvin at the edge of the core to about 2,200,000 at the top of the
  zone", printed from a row. That can be a later step.
- As in item 1, NASA/Marshall's temperature words come off the radiative
  zone's citation; its sentence on the million-year crossing stays,
  because the panel still says that.

## 3 and 4. The chromosphere's name (both sites)

Now: "Sun: Chromosphere (2,000 km skin)", as the drawer row, the legend
and the first line of the hover.

Proposed: "Sun: Chromosphere".

- The depth is already printed from its row, two lines down in the same
  hover: "A thin, reddish layer ... about 2,000 km deep." So nothing is
  lost.
- The other way, printing the number from the row inside the name, is
  not recommended: a name is a key, and the code that reads names would
  each have to fill it in.
- What moves with it: the orrery's two places that build the shell's
  name (`shell_configs.py`, `solar_visualization_shells.py`); on the
  website the served name, and four checks that look it up by name
  (Display figures and its saved hovers, Sun shells, Typed numbers).

## 5. The chromosphere's temperatures (both sites)

Your approved words of Oct 20 stay exactly as approved:
- Website: "its temperature rises with height, from about 4,000 kelvin
  at the bottom to about 7,000 near the top, and then climbs steeply
  into the much hotter corona."
- Orrery: "from about 4,000 Kelvin at its bottom to about 7,000 Kelvin
  near its top. Above that it climbs steeply into the corona, which is
  far hotter." And: "Temperature: about 4,000 K at the bottom to about
  7,000 K near the top."

One finding from opening the paper itself, Carlsson (2007), "Modeling
the Solar Chromosphere". It says both numbers, in two places:
- Section 1 describes the early models: a minimum "around 4000 K about
  500 km above the visible surface", then "a temperature rise to 8000 K
  at a height of about 2000 km".
- Section 2 describes the VAL3 models, the standard ones: "about 6000 K
  at 1000 km height and thereafter a gradual temperature increase to
  7000 K at 2000 km height".

So 4,000 comes from section 1 and 7,000 from section 2, and section 1's
own top figure is 8,000. I recommend keeping the approved words: 7,000
is the standard models' value at 2,000 km, exactly the depth the room
draws, and 4,000 is the minimum both kinds of model share. Each row
quotes its own section. The other choice is section 1 alone: "about
4,000 kelvin at the bottom to about 8,000 near the top".

## 6. The Alfven surface (website, the i panel)

Now and after: "NASA's Parker Solar Probe crossed this boundary in April
2021, the first spacecraft to fly inside the corona."

- No change to the words. The paper is already on this feature's Source
  line: Kasper and others (2021), "Parker Solar Probe Enters the
  Magnetically Dominated Solar Corona". Opened at the NSF's open copy,
  its abstract says: "At 09:33 UT on 28 April 2021 Parker Solar Probe
  entered the magnetized atmosphere of the Sun".
- Why it was held: the Typed numbers check lets a date stand only when
  its list names the work that states it. It names Apophis's April 2029
  that way, and this date was simply never added. I add it.

## 7 and 8. The Hills cloud (website, the i panel and the hover)

Now, panel: "A 2025 computer model finds instead a slightly warped disk
tilted about 30 degrees to the ecliptic, ..."
Proposed: "A computer model (Nesvorny and others, 2025) finds instead a
slightly warped disk tilted about 30 degrees to the ecliptic, ..."

Now, hover: "A 2025 computer model (Nesvorny and others) finds the disk
tilted about 30 degrees to the ecliptic, ..."
Proposed: "A computer model (Nesvorny and others, 2025) finds the disk
tilted about 30 degrees to the ecliptic, ..."

- Source opened: Nesvorny, Dones, Vokrouhlicky, Levison, Beauge and
  others, "A Spiral Structure in the Inner Oort Cloud", posted to arXiv
  on 16 February 2025: the inner cloud is "a slightly warped disk,
  roughly 15,000 au across, inclined i ~ 30" degrees to the ecliptic.
  The year, the authors and the 30 degrees all check.
- The 30 is already printed from its row. Only the year was typed.
- Why the brackets: the year is the paper's, part of its citation, and
  the check already accepts a year written that way, as it does for
  "(Boe and others, 2021)". The other way, leaving the words and adding
  the year to the check's list of dates, would treat a paper's year as
  an event's date.

## What I have not changed

The rest of the orrery's chromosphere text ("about 2,000 kilometers
(1,200 miles)") and the core's and radiative zone's orrery hovers are
the orrery-only group T on L-411, outside this brief.

Approved by Tony, November 2, 2026: "Approved". Built the same
evening; L-411 records what was built.

Written November 2, 2026 with Anthropic's Claude Opus 5.5.
