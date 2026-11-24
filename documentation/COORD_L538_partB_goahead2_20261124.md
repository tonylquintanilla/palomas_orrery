<!-- Doc-Kind: hand | The coordinating session's answer to Part B's first report on L-538 (the orbiters' printed error): the floor's form, two faults found reading the code, and the go-ahead for the room and Part C. -->
# Go-ahead for the room: the orbiters' printed error (L-538)

Built on orrery 6a42ab3bc703bac58ad80d9b738c3cd546803d47 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 9e7bb99ffb77799759abe5a3e6d6dc556853da8e at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Both of
Tony's working copies are ahead of those, not pushed: the orrery by
`patch_L538_2_partB_ruling_and_encounter.py` and two reports, the
gallery by Part B's first half.
Written November 24, 2026 by the coordinating session (Claude Fable
5.2) for the Claude Code session that wrote
`documentation/REPORT_L538_partB_floor_20261124.md`. It follows
`documentation/COORD_L538_partB_goahead_20261124.md`; where the two
differ, this one holds.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

WHAT WAS READ, from Tony's folders, so you know what this rests on:
the report whole (9,618 bytes); the additions to
`tools/test_curve_error.py` whole (182 lines); in
`tools/gallery_cache_builder.py`, the settings, `capture_of` and
`capture_span`, and a search of its 710 added lines for a craft named
in the logic (none; names stand only in comments). The rest of the
builder and the offline suite were not read. The three files compile
and are ASCII. The patch landed: Where We Are reads November 24 with
130 lines above its marker, and the go-ahead in the folder equals the
one built.

## 1. The floor

THE FORM: the SUM, the chord figure plus R x (1 + L). Not the larger
of the two.
- Your own reasoning gives the sum: the planet's part within about the
  chord figure, the three offsets moved by at most L x R, the craft's
  own offset at most R more. The larger-of holds only while the two
  parts do not line up, which is the kind of luck you named for 2R.
- The cost is nothing a visitor sees: worst 0.80 against 0.85, and at
  most one place in the rounding on some days.
- A figure that fails turns a night red and costs a session to find.
- `err_from` says "loop" when the loop's term is the larger part.

WHERE IT ENTERS: as you proposed. `position_at` takes the day's reach
as an optional argument; the builder writes the reach into the
positions file beside t, x, y, z; no line of `interactive.html`
changes. Part C shows that by the page's diff being empty.

THE BOX'S WORDS: no change, as you say.

## 2. Accepted as proposed

The limit of 3,000 fine points and the projection before a round is
asked; 80 questions; no question past 40,000 rows; the band and what
you found about a visitor late in a served night; the check points'
start moved by the date; JPL's header read and printed.

THE CHECK POINTS SAVED: every fourth, as you recommend. The build
tests all of them each night; the saved ones are the offline row's
witness, not its census. The served block and the build's record say
both counts, tested and saved. This is the coordinating session's
decision as method, told to Tony on Nov 24; his to overrule.

## 3. Two faults found reading the code

A. THE SELF-TEST IS POOLED, AND THE FLOOR WILL BLIND IT. In
`test_curve_error.py`, `thin_over` is summed over every capture craft
and the row fails only when the sum is zero. Once the floor is in,
BepiColombo thinned to a point a day passes by design, so Juno's close
passes alone keep the sum above zero, and nothing shows that
BepiColombo's half can fail. Make it per craft, and make it not depend
on the craft's orbit:
- every craft: its check points moved by a known amount (ten times the
  figure, say) must each be caught, which proves they are read and
  compared;
- a band-only craft: with the reach taken away, its point a day must
  miss somewhere outside the band, which proves the floor is what
  holds it. If it does not miss, that is a finding printed by name,
  never a silent pass.
Keep "thinned to a point a day" as a printed line; it is no longer the
gate.

B. `capture_of` TAKES THE LAST ARRIVAL. A craft orbiting one body with
a later arrival in its plan is not seen as captured: the later arrival
is chosen and its stretch misses the window. No served plan has two
arrivals today; JUICE should one day, at Jupiter and then Ganymede
(said from memory, not checked). Take every capture the plan carries
and use the
one whose stretch meets the window. Planted fault: a stand-in craft
with two arrivals, in the first one's stretch today.

## 4. Not this build

JPL's own sentence on BepiColombo, "Data fit through 2026-Nov-17,
prediction thereafter", means its arrival and its orbit since are the
plan, and ESA reported the burn cut short. Whether a spacecraft's
source line should carry JPL's sentence is put to Tony as its own
item. Do not build it. Keep printing it in the build's record.

## 5. Go ahead

Build the floor and the reach, the two fixes of section 3, and the
check of the floor. Then Part C as the brief has it: a whole build on
a throwaway copy, every other served file compared by name, the
gallery run read green from its own output, the nightly commit's
growth measured against the repository's size, and what Tony looks at
on his phone written before he looks: BepiColombo's box today and on a
day outside the band, Juno's on one of its close passes, each with
what it read before and what it should read now. Then the closing
records and the report. Nothing is pushed by the session.

Written November 2026 with Anthropic's Claude Fable 5.2.
