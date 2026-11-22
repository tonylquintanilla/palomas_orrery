<!-- Doc-Kind: hand | The working notes for the one skills bump, v3.145, handed from the coordinating session of Nov 22, 2026 to the next one: what each of five skills gains, what was checked, and what is still to choose. -->
# Handoff: the skills bump (v3.145), working notes

Built on orrery 97a8b733 at https://github.com/tonylquintanilla/palomas_orrery
(branch main) and gallery e6af10ea at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Written
Nov 22, 2026 by the coordinating session of that day (Claude Fable 5.2).

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: DOCUMENTATION. A handoff is a claim: check each line below
against the code at HEAD before it goes into a skill.

## What this is

One bump, five skills, one round of reinstalls for Tony, before the next
website build. The rules were gathered and checked against the code on
Nov 22; three skills have draft text below; two do not. Nothing in
skills/ or PROJECT_INSTRUCTIONS.md has changed since 531c6826, so every
line number below is good at 97a8b733.

Checked Nov 22: all twelve installed skills read the manifest's
versions, and the five below match the repo byte for byte
(gallery-cache-builder differs only by a wrapped fires_when line). So
v3.143's and v3.144's obligations are discharged: interactive-exhibit
1.44, gallery-pipeline 1.3, gallery-cache-builder 1.20,
provenance-discipline 2.37.

The patch's model is documentation/patch_L529_3_skills_and_protocol.py:
a list of (file, old, new), each old matching once; then
skills_index.py, ledger_index.py, skills_index.py --check and
doc_index.py --caps.

## Each skill is at its cap

Lines now, cap, and the oldest version entry that moves word for word
to documentation/SKILL_HISTORIES.md:

- safe-file-editing: 1.14 to 1.15; 765 of 765; the 1.12 block, lines
  27-49 (23 lines). Room enough; nothing else moves.
- gallery-assembler: 1.4 to 1.5; 307 of 307; the v1.2 note in its
  header (4 lines). About 10 more lines of room to find. It has no
  section yet in SKILL_HISTORIES.md.
- interactive-exhibit: 1.44 to 1.45; 738 of 738; the 1.42 entry, lines
  29-43 (15 lines). The three field notes, lines 714-726, can move, one
  line staying under the heading. That gives about 17 lines.
- gallery-cache-builder: 1.20 to 1.21; 942 of 944; the 1.18 entry,
  lines 25-35 (11 lines). About 16 more lines to find; read lines
  430-522, 728-773 and 791-799 for history that can move.
- horizons-orbital-mechanics: 1.19 to 1.20; 904 of 904; the 1.17 entry,
  lines 36-47 (12 lines). About 20 more lines plus L-539's; read lines
  601-794 and 104-190.

Few passages in these four are plain history any more; the earlier
bumps moved the easy ones. Choosing what moves needs the passages
read, not skimmed.

## safe-file-editing 1.15 (draft)

Under Unicode-Safe Editing, after the table:

    A MARK OUTSIDE ASCII IS TYPED AS ITS ESCAPE, AND THE BYTES ARE READ
    AFTER THE EDIT (v1.15, L-529). In a file kept ASCII, such a mark is
    written as its `\u` escape, as the file writes its others. Then read
    the file's bytes for anything above 0x7F: on 2026-11-20 an edit tool
    wrote raw characters where escapes had been typed (the website
    page's Play and Pause marks, an ellipsis, a walk's arrow), and only
    the bytes showed it.

Under A Delivered Patch Is Final, after its Origin paragraph:

    A PLACED FILE IS READ BACK (v1.15). A file placed in Tony's folder
    from a linked session is read back, its size at least, before he is
    told it is there. On 2026-11-22 a prompt file changed and placed
    again arrived with its first content under a new date; the size,
    1,666 bytes where 1,987 were sent, showed it, and a second placement
    seconds later landed.

## gallery-assembler 1.5 (draft)

Keep it short; the website's INTERACTIVE_AS_BUILT.md, The rooms' clock,
holds the detail. A new section after Trust / served_window system:

    ## One seam between the visitor's clock and JPL's (v1.5, L-541)

    A served `jd`, an orbit's date and a plan's moment are on JPL's
    clock (TDB); the minute a room is asked for is UTC. `resolver.py`
    is the one place they meet: it checks the UTC minute against the
    served window, which the builder makes on UTC, then adds the served
    difference (`coverage_index.json`, `clock.tdb_minus_utc_s`) once.
    The context carries both dates, and the drivers hand the page
    `moment_utc_jd` and `moment_tdb_jd`; `epoch_jd` and `epochJd` are
    gone. Nothing downstream converts again. With no clock block the
    room draws as before and warns. The gallery run's Room clock row
    holds it against JPL's places.

## interactive-exhibit 1.45 (draft; about 17 lines of room)

A new section after An encounter is a package:

    ### A visitor reads UTC; JPL's dates are on JPL's clock [QUALITY]
    v1.45, L-541 (Tony, 2026-11-21: "Yes"). Every date a visitor reads
    is UTC, and the date line is the visitor's own minute. A served
    `jd`, an orbit's date and a plan's moment are on JPL's clock (TDB),
    about 69 s ahead. The assembler converts once (gallery-assembler,
    One seam) and hands the page `moment_utc_jd` to print and
    `moment_tdb_jd` for lookups and drift; no page subtracts one from
    the other. A day printed from a JPL date is taken back to UTC
    first; from a served point's date it is read at the nearest minute
    (`SolarSystemFigures.servedDay`), a plan's moment as it stands.
    Only a body's source line names JPL's clock.

A paragraph at the end of Phone first, and the conditions are stated:

    A SESSION THAT CHANGES THE PAGE RUNS THE WALKS (v1.45, L-545; Tony,
    2026-11-21: "should this be method?"). After a change to
    `interactive.html` or a script it loads, before the closing report:
    `tools/headless/walk_solar_system_drawer.js` and
    `walk_scene_moment.js` (jsdom 24.1.3 from npm, in a scratch
    folder), each count and any red check by name; and the gallery run
    on a copy holding only what a push carries (L-543). On Nov 21 a
    walk caught a day one day early that 53 green rows had passed.

Two more for this skill, not drafted:
- A new gallery-run row needs a button in the orrery's dashboard, and a
  website session may not edit the orrery. The brief says who adds it
  (L-550). Three times in three days: Encounters, Link cards, Room
  clock.
- The second half of the walks paragraph is the session's half of
  L-543 (green on Tony's computer, red on GitHub). Whether Tony does it
  before every push of his own is not ruled; do not write it as his.

## gallery-cache-builder 1.21 (not drafted; facts checked)

From L-541, in tools/gallery_cache_builder.py (`build_clock`) and
data/solar-system/coverage_index.json ("clock" and "witness"):
- THE CLOCK BLOCK. `build_clock` asks JPL its TDB-UT (a vectors query
  for Mercury, id 199; astroquery's delta_T; the Horizons manual:
  "After 1962, UT means UTC") at the window's first and last minute and
  the build's own, works out astropy's TDB minus UTC at the same
  minutes, and stops the build by name if the two differ by more than
  0.001 s or JPL's moves by more than 0.004 s across the window (a leap
  second inside it). Served on Nov 22: 69.182891 s, figure_from jpl.
- THE WITNESS. Each build serves JPL's places of Mercury (from its
  orbit) and 3I/ATLAS (from served points) at its own minute; the Room
  clock row compares places. A witness does not share its clock with
  what it tests: astropy and JPL each check the other.
- OPEN ON L-541, one line: daily points are asked at 00:01:00 on JPL's
  clock, 9 s before UTC midnight; keys and plan windows read as UTC.
From L-529, one rule waits for this skill, in the ledger's words "the
package's place and the night": an encounter's package lives under
data/encounters/, written by hand with its own tool; the night never
runs, swaps or commits it, and the sibling check knows the folder by
name. interactive-exhibit 1.44 already carries the encounter: read
what it says before repeating any of it.

## horizons-orbital-mechanics 1.20 (not drafted; facts checked)

Under The Clock Is Read as UTC (L-504), line 281:
- JPL'S DATES ARE ON JPL'S CLOCK (L-541, L-529). datetime_jd is JDTDB;
  an elements epoch is read on JPL's clock; a path plan's moments are
  TDB. A page prints one as UTC only after converting it.
- THE DIFFERENCE IS JPL'S OWN TDB-UT, 69.183 s in Nov 2026. 69.184 s is
  TT's figure (32.184 + 37) and was a brief's mistake. The orrery's
  whole-second 69 (`utc_to_tdb`, `TDB_OFFSET`) is open on L-541.
- AN OLD DATE HAS AN OLD DIFFERENCE: 42.185 s on 4 March 1972, 56.182 s
  on 20 October 1989 (astropy, 2026-11-21; L-541).
From L-539 (every entry checked): its own list of rules and skill text
is on the ledger item, under the build's record. Read it there. Three
corrections it found in this skill:
- Line 117 says Orcus (20090482) and Patroclus (20000617) are found in
  BOTH of JPL's lists; on Nov 22 the session found 20000617 only among
  the major bodies. Correct it from L-539's live answers for both.
- Line 146 names FIVE skip lists in palomas_orrery.py;
  idealized_orbits.py has another, ANALYTICAL_ONLY_SATELLITES, and its
  own id for Xiangliu, 92250881 (L-549).
- astroquery: the skill says 0.4.11; Tony's machine has 0.4.9;
  requirements.txt asks >=0.4.6. In it 'majorbody', 'id' and a blank
  all search the major bodies first and FALL THROUGH to the asteroids
  when nothing matches, which is how the two L3 entries drew asteroids.
  Tony's own output of Nov 22 carries astroquery's warning that
  'majorbody' and 'id' "are deprecated and replaced with ``None``,
  which has the same functionality". That bears on L-548 too.
New in the check, for the skill's Horizons-check section:
horizons_unserved.py; data/horizons_unserved_confirmations.json; the
answer "JPL has no object for this id", stored, waiting on Tony's look,
then held; the mark ("looked"), set by a session's one command from
Tony's words or by itself when the entry's name equals JPL's; due from
day 20, ten a night, red at day 30; the night's title flags JPL DIFFERS
and NEW JPL NAME.

## The protocol

A v3.145 entry; v3.142 moves down to PROJECT_INSTRUCTIONS_HISTORY.md,
PART 1. The obligation travels: Tony reinstalls five skills and pastes
the protocol; the session after confirms each loaded copy.

Session record written November 2026 with Anthropic's Claude Fable 5.2.
