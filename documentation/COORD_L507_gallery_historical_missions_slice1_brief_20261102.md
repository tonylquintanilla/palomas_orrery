<!-- Doc-Kind: hand | Brief for a Claude Code session (build): historical missions, slice 1 (L-507) -- Cassini and Galileo drawn in the Solar System room as Voyager is, an ended mission's marker on its last day, and the dates sentence on every spacecraft's text box; across both repositories. -->
# Brief: historical missions, slice 1 (L-507)

Tony Quintanilla, PE | Claude Opus 5.5 (coordinating session) | November 2, 2026, evening, Chicago

Built on orrery 0d2d2a0ea5cd09e3f5ff9618dea499a56123140b at
https://github.com/tonylquintanilla/palomas_orrery and gallery
c77f87f64c0ba619326a02e7f876d94eda4767be at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, both read
live on Nov 3, 02:50 UTC.

Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`,
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.

Type: BRIEF for one Claude Code session, opened through the python_work
door, working in both folders: the orrery first, then the website. Opus,
high effort (path plans are orbital mechanics, and the words are served
numbers and dates, by `METHOD_MODEL_EFFORT.md`). Its report ends with
its token count, as Claude Code prints it (protocol v3.122, Token
Economy).

## 1. Why, in two sentences

Tony ruled on Nov 2 (14:32, and the Fable talk after it) that past
voyages are drawn in the Solar System room exactly as Voyager is, on
today's date, their path over the mission's own dates. The road's next
stage is this slice (12a on Where We Are); the Sun's eight are done and
Tony's phone look passed all seven (his run record of Nov 2, 17:47).

## 2. The rulings, as L-507 records them (read its body first)

- Slice 1 uses existing machinery: a served positions file fetched by
  the mission's path plan across its whole span, the line drawn by
  `render_spacecraft.py`. No change to the room's date.
- The new words: the text box says the path spans the mission's own
  dates while the planets are drawn where they are today, so a flyby
  bends the line where the planet was, not where it is. That sentence
  lands on EVERY spacecraft's box, Voyager's too.
- An ended mission gets its marker at the path's last served point,
  where it was on its last day, the whole line solid. Its box opens
  "This mission ended on <date>. The marker is where it was that day."
  No hover on the line (one info marker per body).
- The marker's symbol is orrery-coding-conventions' to set (method).
  Whether the ended line looks different is Tony's, on the render
  (Mode 5): build it solid, as ruled, and he judges.
- Tony, Nov 1, 15:51: "a separate group for historical missions in
  addition to active missions." So the drawer gets a group row of its
  own beside Spacecraft. This brief's reading; its label goes in the
  words file (section 5) for his approval.
- Which voyages: Cassini and Galileo, the two Tony named. More are one
  orrery key each afterwards, his choice; the report lists the orrery's
  other ended missions as candidates and builds none of them.

## 3. What is already found, at the two SHAs above

Every line here was read from the code. Re-read before building.

The orrery:
- `celestial_objects.py` has Galileo ('id' -77, start 1989-10-20, end
  2003-09-29) and Cassini ('id' -82, start 1997-10-16, end 2017-09-14),
  both `'object_type': 'trajectory'`, `'is_mission': True`, symbol
  diamond-open. Neither has a 'key' or a 'horizons_name', so neither is
  exported (`export_objects.py`, "WHICH ENTRIES ARE EXPORTED") or
  planned (`path_plan.py` plans every entry with a 'key'). Their
  comments record JPL's data ends: Galileo "No ephemeris ... after A.D.
  2003-SEP-30 11:58:55", Cassini "after A.D. 2017-SEP-15 11:56:50".
- `path_plan.py` takes a path's span from JPL's own first and last day,
  not the list's end_date. So the last served point is JPL's data end.
- The worked example of adding a spacecraft end to end is L-443's build
  B: `documentation/HANDOFF_L443_slice2_buildB_spacecraft_20261025.md`.
  Follow its order; do not redesign it.

The website:
- `gallery/assembler/render_spacecraft.py`, `build_spacecraft_traces`:
  when the minute shown is past the last served point
  (`position_at` returns None), it draws the whole path solid with NO
  marker and returns a warning. That is the branch slice 1 changes: a
  marker at the last served point, its meta carrying `path_start_jd`,
  `path_end_jd` and an error for a served point (zero: it is not worked
  out between points), and a mark that it ended.
- `interactive.html`, the text box for `b.kind === "spacecraft"`
  (around line 3160): the distance line from
  `SolarSystemFigures.pathDistanceLine`, the note that JPL's own
  uncertainty is not served, then `SPACECRAFT_PATH_WORDS` ("Its path is
  solid where it has already flown, and dashed where JPL's predicted
  path takes it next, as far as <day>."). For an ended mission that
  sentence is wrong (nothing is dashed) and the distance is its last
  day's, not today's. Both need words of their own (section 5).
- `spacecraftSourceLine` (around line 2804) reads the span from the
  marker's meta, so it serves an ended mission unchanged once the meta
  is there.
- All twelve served spacecraft are active, so the ended branch has
  never run on real data. `data/objects_config.json`'s room rows list
  them under the Spacecraft group (around line 2515).

## 4. The work, in order

1. ORRERY. Give Galileo and Cassini a 'key' (`galileo`, `cassini`, the
   slug the website will use) and JPL's exact 'horizons_name', read
   from JPL, never typed from memory (horizons-orbital-mechanics,
   Which Record Serves a Body). Run `path_plan.py`: both are orbiters,
   so read its orbiter rule for an arrival and a capture; print each
   plan's span and events and read them. Then the orrery's maintenance
   run, which exports both; Tier-1 0 on the gate path.
2. CHECK THE END DATE, and stop here if it fails. For each mission, put
   JPL's last served day beside the mission's end as a page you can
   open states it (NASA's mission page, or JPL's data sheet). If they
   differ by more than a day, stop and bring Tony the two dates and
   their sources: the ruling says "where it was on its last day", and
   a JPL path that runs past the mission's end would put the marker on
   a day it no longer existed. One question, nothing else in it.
3. Tony pushes the orrery (his run order). Then the WEBSITE pulls the
   export; the mirror brings both entries in.
4. WEBSITE, the renderer: the ended branch of `build_spacecraft_traces`
   as section 3 says, its symbol by orrery-coding-conventions' Marker
   Symbol Convention (the table's spacecraft row is diamond-open; if a
   rule is needed for an ended one, it is that skill's to add).
5. WEBSITE, the room: the drawer's group row for ended missions beside
   Spacecraft, by interactive-exhibit's drawer rules (order, Home,
   companions, Find a body); the text box's words from section 5, once
   approved; companions by `SolarSystemDrawer.companions` unchanged
   (Cassini's plan should tick Venus, Earth, Jupiter and Saturn by
   itself: read it, do not type it).
6. Cache: the builder serves both by their plans (gallery-cache-builder,
   A Spacecraft Is Fetched by Its Plan); a hand build, as L-411's
   session did, so Tony sees them before the night.
7. Checks: the figures check's part 7 and the drawer walk's section 20
   each gain the ended case, each shown failing once on a planted fault
   (a check that cannot fail is not passing). Both maintenance runs
   green, read from their output.

## 5. The words, Tony's before they are written

Draft in `documentation/WORDS_L507_historical_missions_20261102.md`
(the L-411 session's words file is the shape) and wait for his
"Approved". Plain words, one sentence to a bullet:
- the dates sentence, for every spacecraft (section 2's gist);
- the ended box's opening, verbatim as ruled, with the date's source;
- the ended path's sentence, replacing the solid-and-dashed one;
- the distance line's qualifier, that it is the distance on its last
  day (the place a served point earns, never finer than whole
  kilometres, provenance-discipline 2.23);
- the group row's label.
Everything else in the box is unchanged.

## 6. The rules it runs under

Read each before the work it governs; open the first report with each
version line read, against the manifest:
interactive-exhibit 1.29 (the spacecraft and companions bullets; the
drawer); gallery-assembler 1.3 (render_spacecraft.py); gallery-cache-
builder 1.16 (A Spacecraft Is Fetched by Its Plan); horizons-orbital-
mechanics 1.13 (a spacecraft path's plan, the orbiter rule, JPL's exact
name); orrery-coding-conventions 1.12 (Marker Symbol Convention);
provenance-discipline 2.36 (a served date and a distance print what
their sources earn); safe-file-editing 1.14; agentic-pre-test 1.3;
ledger-and-session-records 1.22.

Two skill corrections ride this session, since it opens both skills
anyway (one session, one bump; both carried from L-505 (the ticks and
the ruler), closed Nov 2):
- interactive-exhibit: wherever its L-505 bullet says dots, x marks;
  and the spacecraft bullet gains the ended branch and the dates
  sentence.
- orrery-coding-conventions: the Marker Symbol Convention table gains
  an x row (coordinate ticks: the axes' scale marks and the ruler) and
  the cross row becomes info markers alone; plus any ended-spacecraft
  rule step 4 adds.
Each bump follows ledger-and-session-records' four steps in one commit,
with the protocol's version-history entry (v3.123).

## 7. Done when

- Galileo and Cassini are served, drawn whole and solid, each with its
  marker at its last served point and the approved words; Voyager's box
  and every active spacecraft's carries the dates sentence.
- Both maintenance runs pass, read from their output; Tier-1 0 on the
  gate path; the two new check cases each shown failing once.
- Tony's run order ends with his phone look: Cassini and Galileo
  ticked, their boxes, their companions, Voyager 1's box; and his
  Mode 5 word on the ended line.

## 8. Records, in the same session

- L-507: what was built, verified against claimed; slice 2 untouched.
- Where We Are, by section: 12a's line, the box, Signals read from
  files; nothing below the run-record marker.
- The two skill bumps and the protocol entry, if built (section 6).
- The report: files changed with their edit counts, the token count,
  Tony's run order, the Tony-action rollup, one question at most.

Written November 2, 2026 with Anthropic's Claude Opus 5.5.
