<!-- Doc-Kind: hand | Brief for one Claude Code session in the orrery: the Horizons check covers every entry the orrery asks JPL for, not only the entries the website serves (L-539). -->
# Brief: every entry checked against JPL (L-539)

Built on orrery 531c6826 at https://github.com/tonylquintanilla/palomas_orrery
(branch main). The website is not touched; it stood at gallery 5a7c96f8
at https://github.com/tonylquintanilla/tonyquintanilla.github.io when
this was written. Written November 22, 2026 by the coordinating session
(Claude Fable 5.2) for ONE Claude Code session in the ORRERY repository.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Read before building, and say back which you read, with each skill's
version line: the orrery's CLAUDE.md and the files it points to; the
skills `horizons-orbital-mechanics` (Checking an Entry Against JPL;
Where the Check Lives, and What It Compares; Which Record Serves a
Body, with its rule A SKIP NAMES WHAT FAILED), `provenance-discipline` (a stored
value's source; the push gate), `agentic-pre-test`, `safe-file-editing`,
`orrery-coding-conventions` (the module docstring standard) and
`ledger-and-session-records` (the closing records). Then this brief,
and L-539 (every entry checked), L-297 (the Lagrange points) and L-395
(the Horizons check) in LEDGER_CONSOLIDATED.md.

## 1. The ruling

Tony, November 19, 2026, 15:30, after L-297 (the Lagrange points) found
that the orrery's two L3 entries, asked of JPL as 3013 and 33, had
drawn the asteroids 3013 Dobrovoleva and 33 Polyhymnia under those
names, and that nothing had caught it: "Yes" -- the check covers every
entry the orrery asks JPL for. Its first run writes a one-time list,
each entry beside the name JPL gives its id, for Tony to scan once, as
the two L3 entries would have shown; from then on it stores JPL's name
and holds the entry to it every 30 days, a few per run, under the
maintenance run's 15 minutes.

On the order, November 22, 10:13, to the coordinating session's
proposal that this brief goes first and the owed skill text is written
while this session runs: "Confirmed as recommended including your final
thought".

## 2. What was found at orrery 531c6826 (read it; do not trust this list)

- THE CHECK SEES ONLY KEYED ENTRIES. `horizons_check.py`
  (`current_entries`) reads the list through
  `export_objects.build_objects`, which returns the entries that carry
  a 'key'. `data/horizons_confirmations.json` holds 110 records, one
  per key. The objects export copies each record's confirmation, and
  the website's own row reads the pulled export: on the night of Nov 22
  it said "110 of 110 confirmed, and 67 periods, within 30 days".
- THE COUNT, read again today from `celestial_objects.py` with
  `export_objects.definitions`: 184 entries, 110 with a key, 74 without.
  Of the 74, by their ids, 57 look asked of JPL: 43 moons (id_type
  'majorbody', object_type 'satellite'), 8 spacecraft (id_type 'id',
  object_type 'trajectory': Apollo 11 S-IVB, SOHO, Gaia, Hayabusa2,
  OSIRISREx, MarsRover, JamesWebb, Artemis II), 3 barycentres
  (Earth-Moon as 3, Patroclus-Menoetius as 20000617, Orcus-Vanth as
  20090482), Menoetius (120000617), Pluto (999) and 6AC4721. The other
  17 are Planet 9 and the exoplanets and their stars. This is L-539's
  own count of Nov 19 and it still holds.
- NO UNKEYED ENTRY CARRIES A `horizons_name`. All 110 keyed entries do,
  and `check_entry` holds a keyed entry to it character for character.
  An unkeyed entry has only its own `name`, its `id` and its `id_type`.
- THE id_type WORDS DIFFER. The check and the skill know a blank,
  'smallbody' and 'designation'. The unkeyed entries also use
  'majorbody' and 'id'.
- 6AC4721'S ID IS THE WORD 'none', id_type 'smallbody'. Tony keeps the
  entry on purpose (Nov 4, 2026): it shows how MAPS (C/2026 A1) was
  drawn from typed elements before JPL had it. Whether it is asked of
  JPL at all is for Part A. It is not removed and not re-pinned.
- ONE ID IS USED TWICE: '-64' by OSIRISREx and by the keyed OSIRISAPE.
- THE DATA SHEETS ALREADY REACH THE UNKEYED SPACECRAFT.
  `spacecraft_entries` takes every id starting with '-', keyed or not.
  So those eight have a sheet re-read and no identity check.
- THE NIGHT COMMITS ONLY DECLARED FILES. `.github/workflows/nightly.yml`
  adds the paths `orrery_maintenance_run.night_allow_list` returns, the
  night tools' declared outputs. A record this build writes to a file
  not declared there is written on GitHub's machine and thrown away,
  and the next night asks JPL for everything again.
- THE RUN'S LIMIT is `TOOL_TIMEOUT_SECONDS = 900` for one tool; the
  check waits `PAUSE_SECONDS = 2.0` between questions and asks an
  ordinary entry of both of JPL's indexes.

## 3. What to build

The outcomes, which are Tony's ruling:
1. Every entry the orrery asks JPL for is checked: its id names exactly
   one object at JPL, and JPL's name for it is on record.
2. The first run writes a one-time list for Tony to scan once: each
   entry's own name beside the name JPL gives its id.
3. From then on JPL's name is stored, and the entry is held to it every
   30 days.
4. A few per run: no night is long, and the worst night stays well
   under the 15 minutes.
5. The website sees nothing new. `data/objects_export.json` carries
   what it carries today for the 110, and every website row that reads
   it stays as it is. Show it: the export written before and after,
   compared, with only what a night moves moved.

How, which is yours to propose in Part A. These are the coordinating
session's starting points, not rulings:
- WHICH ENTRIES ARE ASKED is a rule read from the list (its id, id_type
  and object_type) and from the code that asks, never a typed list of
  names. The check prints how many are asked and names them, and names
  each entry not asked with its reason. An entry that fits neither side
  is named and fails the run. It is never dropped.
- THE RECORD for an entry with no key needs a name of its own, and a
  home the export does not copy from, so outcome 5 holds by
  construction. Say where, and declare the file to the night.
- WHERE JPL'S NAME LIVES: in the record, or as `horizons_name` on each
  entry in `celestial_objects.py` as the 110 have it. Give the cost of
  each. The second is an edit to 57 entries of the object dictionary.
- THE ONE-TIME LIST is a document in `documentation/`, read on a phone:
  one line per entry, the orrery's name, the id asked, JPL's name for
  it and JPL's kind. Put first the entries whose own name does not
  appear inside JPL's name, and say on the page that this order is a
  hint and not a verdict: JamesWebb against JPL's name for -170 is
  right and will look wrong; 3013 against "Dobrovoleva" was wrong and
  would have stood at the top. Count and names, both. One line says the
  110 keyed entries are already held to their typed names, and by what.
- THE SPREAD. Fifty-seven first confirmations made on one day come due
  on one day, every 30 days. Show the worst night's count of questions
  and its measured time, and spread the dates if that night is not
  small.
- A MISMATCH AT NIGHT. A keyed body is held at its last confirmed
  values and named under 'held' in the orrery's night record (L-485);
  the website's night then starts its commit title with HELD (L-525).
  The orrery's own title carries one flag today, EL NINO DUE
  (`NIGHT_TITLE_FLAGS`). An unkeyed entry serves nothing, so there is
  nothing to hold. Starting point: it is named on the night's record
  and flagged at the start of the orrery night's commit title, which
  is where Tony looks, and the night continues, by his rulings of
  Oct 31 ("we hold only where a project choice matters") and Nov 11
  ("Hold the bad data and report, then continue."). If you judge that
  this one is Tony's to rule, make it the one question of your Part A
  report.
- JPL UNREACHABLE says so, by name, as the check does today, and is not
  a failed identity.

PART A, no edits. Map: every place the orrery asks JPL about an entry
by its id (so "asked" is read, not assumed); how each id_type word
reaches JPL's two indexes, tried on JPL's live answers for one moon of
a planet, one moon of a small body (Dysnomia, 120136199), one
barycentre, one spacecraft and Pluto; what `export_objects.py` copies
from the record and what the website's checks read of it; the night's
declared outputs; `check_horizons_confirmations.py`. Then your
proposal for each starting point above, and the worst night. Stop with
that report. Tony carries it to the coordinating session.

PART B, after the go-ahead. The check, its record, the offline checker
and the suite. Each new check is shown able to fail, by a planted fault
caught by name: an unkeyed id that answers another object's name (the
L3 case, 3013 answering "3013 Dobrovoleva"); an id matching two
objects; an id matching none; an entry that fits neither "asked" nor
"not asked"; a stored name JPL has since changed; a record file the
night does not declare. `agentic-pre-test` before any file is called
done. Stop with a report and wait for the go-ahead.

PART C. The first run, by hand, against JPL. The one-time list written
to `documentation/`. `orrery_maintenance_run.py` whole, read green from
its output. The night's path run the way GitHub runs it (`--night`) on
a throwaway copy, to show the new record is among the files the night
would commit. The export compared before and after (outcome 5). Then
the closing records and report.

PART D, ONLY IF THE STARTING PROMPT NAMES IT: L-512's two leftover
asks, received from L-297 on Nov 19. A ticked Lagrange point still
enters the osculating pre-fetch, where JPL answers "Required masses not
defined, osculating elements not available", and the close-approach
cache asks JPL's small-body service by the point's number. A point has
no elements and no close approaches to ask for: it goes on the skip
lists, each with a comment naming what failed. The skill names five
lists in `palomas_orrery.py`; the pre-fetch's own stands twice there
(`plot_objects` and `animate_objects`), and `period_fetch.py` copies
it. Map every copy first, then change each or say why not (the
protocol's Check All Parallel Pipelines). If Part C has run long, leave
Part D on L-512 and say so.

NOT IN THIS SESSION.
- Any skill file. List on L-539 the rules you learned, in plain
  sentences, and name in the report what `horizons-orbital-mechanics`
  should say. The coordinating session writes them into one bump with
  the text L-541 (a plan's clock) already owes.
- Correcting an entry the list shows wrong. The list is Tony's to scan;
  a wrong entry found on the way is named at the top of the report and
  left as it is.
- Giving an unkeyed entry a key, or serving it. The website repository.
- The orrery's clock items left open on L-541: `path_drawing.py`,
  `utc_to_tdb`, `TDB_OFFSET`.
- A warning in the orrery's window when a ticked entry failed its
  check. Name it in the report if you think it is owed.

## 4. Delivery

- Work in the orrery repository only, through the python_work door.
  Record its base (`git rev-parse HEAD`, `git ls-remote origin HEAD`).
  The night commits under data/ every day, so the base may be a
  descendant of 531c6826; stop only if a file named in section 2 is not
  as described, and name what moved.
- Edit the files in Tony's working copy, ASCII and LF, each change
  stamped where it is made; Tony commits and pushes. Nothing is pushed
  by the session.
- The coordinating session has a patch waiting that edits the ledger
  and the skills. Tony runs it only after this session's work is
  pushed. Say so in the closing report's run order, so the two are not
  mixed in one commit.
- After Tony's push, the next orrery night is the proof on GitHub's
  machine: its Horizons check row names the new entries, and its commit
  carries the new record. Say in the report what that row should read.

## 5. The report

Plain words, in this order: what was built, file by file; the first
run's counts, with the entries named; the one-time list's file name and
what Tony does with it (scan it once, mark each line at the top "-- ok"
or "-- wrong" in his run record); the worst night; the export
comparison; the maintenance run's rows by name; what Tony does next;
the skill text owed; anything this brief got wrong. It opens with the
anchor line: built on <base SHA> at the orrery's URL; ready at <new SHA
or "not pushed">. It ends with the session's token count as Claude
Code's /cost prints it (Token Economy).
