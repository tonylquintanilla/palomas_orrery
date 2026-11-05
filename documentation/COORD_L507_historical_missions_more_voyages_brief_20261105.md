<!-- Doc-Kind: hand | Brief for a Claude Code session (build): historical missions, more voyages (L-507) -- Pioneer 10, Pioneer 11, Rosetta, DART and Akatsuki drawn in the Solar System room as Galileo and Cassini are, each path stopping on the day its mission ended, and a craft that flies on said to be flying and untracked; across both repositories. -->
# Brief: historical missions, more voyages (L-507)

Tony Quintanilla, PE | Claude Opus 5.5 (coordinating session) | November 5, 2026, afternoon, Chicago

Built on orrery ca4dceea55243e20e75689263ef31b996c8b1a3c at
https://github.com/tonylquintanilla/palomas_orrery and gallery
3660993e736641f1d1412bf9ed58244d419307dc at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, both read
live on Nov 5, 2026, 15:12 Chicago. The orrery commit that carries this
brief is the coordinating session's records patch on top of ca4dceea.

Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`,
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.

Type: BRIEF for one Claude Code session, opened through the python_work
door, working in both folders: the orrery first, then the website. Opus,
high effort (path plans and served dates, by `METHOD_MODEL_EFFORT.md`).
Its report ends with its token count as Claude Code prints it (the
protocol's Token Economy).

The machinery is slice 1's, built Nov 2 and 3 for Galileo and Cassini:
read L-507's body and
`documentation/COORD_L507_gallery_historical_missions_slice1_brief_20261102.md`
first. This brief says only what differs.

## 1. Why, in two sentences

Road stage 13 on Where We Are, the quick wins, second part: the ended
missions the orrery already lists, drawn on the website (Tony's order of
Nov 5; the instrument, a Code session from this brief, his go-ahead of
Nov 5, 13:27). Apollo 11's S-IVB is not in this build: it goes with
slice 2, the encounters (Tony, Nov 5, 13:27: "Apollo in slice 2").

## 2. The rulings

Slice 1's stand (L-507): a served positions file by the mission's path
plan, drawn whole and solid by `render_spacecraft.py`; the marker at the
path's last served point; the box opens "This mission ended on <date>.
The marker is where it was that day."; the Historical missions group;
the dates sentence on every spacecraft's box. Galileo's ruling, "Yes
stop at impact" (Nov 2), stops a path on its `mission_end` where JPL
runs past it.

New, for a craft that flew on after its mission ended (Tony, Nov 5,
15:17 Chicago, choosing option A of the coordinating session's question):
"A. but indicate the craft is still flying but not tracked."
- So the path stops on the day the mission ended, as Galileo's does,
  and the marker sits where the craft was that day.
- And the words say the craft is still flying and no one tracks it. The
  wording is drafted and waits for his "Approved" (section 5).
- Option B, declined: the path running on to JPL's last day, dashed
  after the mission's end.

## 3. What is already found, at the two SHAs above

Every line was read from the code. Re-read before building.

The orrery, `celestial_objects.py` (all `'object_type': 'trajectory'`,
`'is_mission': True`, symbol diamond-open; none has a 'key', a
'horizons_name' or a 'mission_end', so none is exported or planned):

| Entry | Line | id | start / typed end | JPL's ends, as the entry's comments record them | mission_url |
|---|---|---|---|---|---|
| Pioneer 10 | 918 | -23 | 1972-03-04 / 2002-03-03 | none before 1972-MAR-03 02:04; none after 2050-JAN-01 00:08 | NASA Ames archive page |
| Pioneer 11 | 925 | -24 | 1973-04-07 / 1995-09-29 | none before 1973-APR-06 02:25; "Science operations and daily telemetry ceased on September 30, 1995" (no JPL end recorded) | the same NASA page |
| Rosetta | 976 | -226 | 2004-03-03 / 2016-10-04 | none before 2004-MAR-02 09:25; none after 2016-OCT-04 23:59 | rosetta.esa.int |
| Akatsuki | 990 | -5 | 2010-05-22 / 2025-08-22 | none before 2010-MAY-21 00:51; none after 2025-AUG-23 23:58 | Wikipedia (not the agency's page) |
| DART | 1053 | -135 | 2021-11-25 / 2022-09-26 | none before 2021-NOV-24 07:16; "Impact: 26-Sep-2022 23:14:24.183 UTC (actual)" | nasa.gov/dart |

- The comments are older readings, not today's JPL. Read JPL again.
- `path_plan.py` takes a plan's span from JPL's first and last day, or
  to `mission_end` where it is set (line 481), and adds `mission_end` to
  a plan's inputs only where it is set (line 739).
- L-507's note received from L-476 (Nov 3, evening): in the DESKTOP
  orrery, Pioneer 10 has no plan, its line stops at its typed end
  (79.8 AU) while its marker is at today's position (142.2 AU). See
  step 1's stop point.

The website:
- `interactive.html` line ~2804 writes the ended opening from the
  path's last served day; ~2839 notes `mission_end`. The ended branch of
  `render_spacecraft.py` and `fetch_path_last_day` in the builder are
  slice 1's and serve these five unchanged.
- The objects mirror copies `REPLACED = ("name", "horizons_id",
  "id_type")` and `INSERTED = ("description", "info_url", "period",
  "path", "open_path", "horizons_name")` (`tools/mirror_objects.py`).
  Nothing that says a craft flies on reaches the room today.
- The mirror follows a body across e = 1 by itself since 3660993 (L-510);
  that does not touch spacecraft.

## 4. The work, in order

1. ORRERY, the five entries. A 'key' each (`pioneer_10`, `pioneer_11`,
   `rosetta`, `dart`, `akatsuki`, the website's slugs) and JPL's exact
   'horizons_name', read from JPL (horizons-orbital-mechanics, Which
   Record Serves a Body). Then each one's `mission_end` by that skill's
   method (An Ended Mission Ends on Its mission_end): JPL's last day and
   the mission's end as the AGENCY'S OWN PAGE states it (NASA for the
   Pioneers and DART, ESA for Rosetta, JAXA for Akatsuki), side by side,
   the page quoted on the entry.
   - Within a day: the page's date, as for Galileo and Cassini.
   - JPL runs past the page's end (an impact, or a craft that flew on):
     the page's date. Galileo's ruling and Tony's of Nov 5 cover both.
   - STOP and bring Tony one question, the two dates and their sources,
     when: the page's end is AFTER JPL's last day (no point to put the
     marker on); no agency page states an end (Akatsuki's link today is
     Wikipedia); or a page gives two dates (last contact and a declared
     end) and does not say which is the mission's end.
2. ORRERY, "still flying". For each craft that flew on, a field on its
   entry saying so, cited to a page that says the craft still flies (or
   still orbits). No page saying so: no field and no sentence, and the
   gap named (remove and note it). The field's name and its road to the
   room are the session's, as `mission_end`'s and `open_path`'s were:
   the export, the mirror's INSERTED list (with a case in
   `tools/test_mirror_objects.py`), the config, the room.
3. ORRERY, the plans: `path_plan.py` for the five, each plan's span and
   events printed and read. Akatsuki is a Venus orbiter (the orbiter
   rule, an arrival). Then the orrery's maintenance run, which exports
   them; Tier-1 0 on the gate path.
   - STOP POINT, L-476's note: plot Pioneer 10 Sun-centred in the
     desktop orrery after the change and report what the line and the
     marker show. If the marker still sits at today's predicted place
     beyond the line's end, bring Tony that one question; the ruling
     says the marker is where it was on its last day.
4. THE WORDS (section 5), before any is written into the room.
5. WEBSITE, in the same round as the export's new keys (a key in the
   export with no website entry stops the mirror, and the night with
   it; horizons-orbital-mechanics, KEYING): the five entries in
   `data/objects_config.json` (the mirror fills the rest), their rows in
   the Historical missions group, colours in `presentation.py`
   (method, recorded in the words file), the box's still-flying
   sentence, and companions by the plans (read them, do not type them).
6. CACHE: a hand build, so Tony sees them before the night. The
   Pioneers' spans run decades; read each positions file's size and say
   it (render size is watched).
7. CHECKS: the figures check's part 7 and the drawer walk's section 20
   gain the still-flying case; the mirror suite the new field; each
   shown failing once on a planted fault. Both maintenance runs green,
   read from their output.
8. PUSH ORDER, in the run order: orrery and website the same evening,
   orrery first, both before the next night (08:17 UTC).

## 5. The words, Tony's before they are written

Draft in `documentation/WORDS_L507_more_voyages_20261105.md` (slice 1's
`WORDS_L507_historical_missions_20261102.md` is the shape) and wait for
his "Approved". Plain words, one sentence to a bullet:
- the still-flying sentence, after the ended opening, for each craft
  whose page says it flies on (gist: "It is still flying, but no one has
  tracked it since."), with its source;
- each of the five's description;
- each `mission_end` with the sentence of the page it comes from;
- the colours (method, recorded).
Everything else in the box is slice 1's and unchanged.

## 6. The rules it runs under

Read each before the work it governs; open the first report with each
version line read, against the manifest: horizons-orbital-mechanics 1.17
(Which Record Serves a Body; An Ended Mission Ends on Its mission_end;
the orbiter rule; KEYING); gallery-cache-builder 1.17 (A Spacecraft Is
Fetched by Its Plan, its last-day fetch); interactive-exhibit 1.30 (the
spacecraft bullet, the drawer, companions); gallery-assembler 1.3;
orrery-coding-conventions 1.13 (Marker Symbol Convention);
provenance-discipline 2.36 (a served date prints what its source
earns); safe-file-editing 1.14; agentic-pre-test 1.3;
ledger-and-session-records 1.22.

Corrections that ride this session's bumps (one session, one bump; each
carried here from the coordinating session of Nov 5, L-510 and L-507):
- horizons-orbital-mechanics: An Ended Mission Ends on Its mission_end
  says "NASA's own mission page"; it becomes the agency's own page, and
  gains Tony's ruling of Nov 5 for a craft that flew on. Under Which
  Record Serves a Body, AN OPEN ORBIT IS NOT AN ELLIPSE calls piece C's
  website drawing "an open difference on L-484": read L-484 and correct
  the sentence to its state.
- gallery-cache-builder: the mirror now follows a body across e = 1
  (`tools/mirror_objects.py`, WHEN A BODY CHANGES SIDE, gallery
  3660993), and the builder's offline test compares its comets on open
  paths with the export by name and gives a stand-in orbit to a body
  newly drawn as one; the bullet A COMET ON AN OPEN PATH IS A PATH BODY
  and the onboarding section say so. Plus the new field in INSERTED.
- interactive-exhibit: the spacecraft bullet gains the still-flying
  sentence.
Each bump follows ledger-and-session-records' four steps in one commit,
with the protocol's version-history entry (v3.127).

## 7. Done when

- The five are served, drawn whole and solid, each marker on its
  mission's last day, with the approved words; a craft that flew on says
  so, where a page supports it.
- Both maintenance runs pass, read from their output; Tier-1 0 on the
  gate path; each new check case shown failing once.
- Tony's run order ends with his phone look: the five ticked from
  Historical missions, their boxes and companions; and the desktop
  orrery's Pioneer 10, Sun-centred.

## 8. Records, in the same session

- L-507: what was built, verified against claimed; slice 2 (the
  encounters, Apollo 11's S-IVB and Artemis II) untouched.
- L-510: the two carried corrections, closed in the bumps.
- Where We Are, by section: stage 13's line, the box, Signals read from
  files; nothing below the run-record marker.
- The report: files changed with their edit counts, the token count,
  Tony's run order, the Tony-action rollup, one question at most.

Written November 5, 2026 with Anthropic's Claude Opus 5.5.
