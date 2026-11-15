<!-- Doc-Kind: hand | The brief for one Claude Code session through the python_work door: L-514 (the Mars room), session 1, the orrery's half: Phobos and Deimos keyed, in NASA's words, with JPL's periods and JPL's own accuracy. Communication; written once, read by its session. -->
# Brief: Phobos and Deimos in the orrery (L-514, session 1 of 2)

Built on orrery c314fe1a5b2a6b719a88a5a4fa51605c8bac53c5 at
https://github.com/tonylquintanilla/palomas_orrery
and gallery d3e97b1503d878a6fac0be4fe9131186b893d365 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io
(both branch main, read 2026-11-14, 22:10 Chicago). Nightly bot commits
since are expected. This brief is in documentation/ on Tony's computer,
not yet pushed.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD, a Claude Code session on Tony's computer, through the
python_work door, in the ORRERY only. Written November 14, 2026 with
Anthropic's Claude Opus 5.5, the coordinating session. Session 2, the
website's half, gets its own brief when it is next (Token Economy).

## What this is, in one paragraph

The Mars fold (L-514, the Mars room) needs its two moons. The website
can only serve a body the orrery exports, and the orrery exports only
an entry with a `'key'`. Phobos (401) and Deimos (402) have none, and
their words are typed, not NASA's; Deimos's say "Retrogade", which no
source supports. This session brings both up to the Moon's standard
(L-513): a key, JPL's name, NASA's own sentence with NASA's page as
the link, the period fetched around Mars, and an accuracy row cited to
JPL's paper on the very ephemeris Horizons serves.

## The rulings (Tony's words and times, Chicago, Nov 14)

1. 22:21, the build's two sessions: session 1 (this one) "-- yes".
2. 22:43, Phobos's sentence: "2" -- "Phobos is on a collision course
   with Mars."
3. 22:54, Deimos's sentence: "3" -- "Deimos is the smaller of the two
   Martian moons and is less irregular in shape."
4. 22:45, ESCAPADE (Tony's find) is its own round after the Mars build:
   "as you recommend." Out of scope here (L-533).
5. 23:10, the brief: "yes". The accuracy question he raised then
   ("can we say that a 2 km precision is the same as whole
   kilometers?") was settled by the 2025 paper below, by the Report
   test, not by a ruling.

The tap area is NOT in this build: L-523 (taps sent as hovers) made a
finger's 22-px reach site-wide, closed Nov 12. Session 2 checks only
that a tap near Mars picks the moon meant.

## What was read for this brief (re-check, do not trust)

- NASA's pages, both "last updated Nov 03, 2024", read Nov 14:
  - https://science.nasa.gov/mars/moons/phobos/ ("Phobos - NASA
    Science"): the sentence of ruling 2, word for word, plain
    apostrophes.
  - https://science.nasa.gov/mars/moons/deimos/ ("Deimos - NASA
    Science"): the sentence of ruling 3 is a Quick Facts line. The page
    says nothing of the orbit's direction.
- Horizons, Nov 14: Phobos and Deimos around Mars ('500@499') are
  served "{source: mar099}". A VEC_TABLE='2xr' request for Deimos
  printed "n.a." in every sigma column: JPL serves no uncertainty for
  these moons, so the accuracy must come from a paper.
- mar099's release note,
  https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/mar099.cmt
  (BVS/NAIF, June 2, 2025): states no position accuracy. Its
  "Chebyshev interpolation error: 2.000 meters" measures the file, not
  the moons. Do not cite it as accuracy.
- THE SOURCE: Brozovic, M., Jacobson, R. A. & Park, R. S. (2025),
  "Revised Ephemerides of the Martian Satellites, Phobos and Deimos",
  AJ 170:42, https://doi.org/10.3847/1538-3881/addab4 (open access).
  Its abstract: "We report on the new ephemerides (MAR099) for the
  satellites of Mars". Section 6, Conclusions, PDF page 13 of 14: "the
  realistic 1 sigma value for the uncertainties is on the order of a
  few kilometers for the next couple of decades" (the PDF prints the
  Greek sigma; the row is ASCII). Section 5.3 says the formal
  covariance is "overly optimistic": Phobos's should be scaled by about
  4, Deimos's doubled. Tony's local copy is in papers/, named
  Brozovi?_2025_AJ_170_42.pdf, the ? an accented c as Tony saved it
  (papers/ is local-only by .gitignore).
- Superseded, read and not to be cited: Jacobson (2010), AJ 139:668,
  p. 677 ("no better than 1 km" for Phobos, "roughly 2 km" for
  Deimos). It describes MAR085, two versions back.

## The work

Part 1, the entries (`celestial_objects.py`, the Mars moons block):
- Phobos: `'key': 'phobos'`, `'horizons_name'` as JPL's lookup
  answers it (the three steps L-513 used: `horizons_check.lookup_url`,
  `parse_lookup`, `keep`); `'mission_info': 'Horizons: 401. NASA:
  "Phobos is on a collision course with Mars."'`; `'mission_url':
  'https://science.nasa.gov/mars/moons/phobos/'` (replacing the image
  page). The typed period line goes.
- Deimos: the same shape, `'key': 'deimos'`; `'mission_info':
  'Horizons: 402. NASA: "Deimos is the smaller of the two Martian
  moons and is less irregular in shape."'`; the URL stays. The typed
  period and "Retrogade" go.
- Periods: `period_fetch.py` around Mars ('@499', the planet's centre,
  as the Moon's is '@399'; L-150 is the reason it is not the
  barycentre), days only, its own figures rule. Report each period as
  it prints.
- Report, and stop for Tony's go-ahead.

Part 2, the accuracy row and the export:
- ONE row in `constants_new.py`, beside the DE430 rows, for both moons
  (one source, one place), its name the session's choice in that
  family. Store the PLACE the words report to, by the Report test
  (provenance-discipline, Store the place): "a few kilometers" is 2 to
  9.999 km, all of which report to tens, so 10.0 km. State that
  reading in the report, in plain words, for Tony to check.
- Its Source and Read lines from the paper as above, the DOI address,
  page 13, Section 6; a line naming Section 5.3's scaling; a line
  naming the 2010 paper as read and superseded.
- The export (`export_objects.py`) and the orrery's maintenance run,
  read for its own green line. Name what the two new keys changed in
  the exports and checks (the Horizons check and its period comparison
  now include them; L-513 said "each gains both when it gets a key").
- Report, and stop.

Part 3, the records: L-514 (the Mars room), Where We Are by section,
the final report as CLAUDE.md asks, with the token count.

Out of scope, recorded, not chased: the website (session 2); Io,
Titan, Pluto and Charon's keys (L-515's leftover 1); ESCAPADE (L-533);
the orrery's Mars visualization shells.

## Skills this fires

Read each and compare its version line with the manifest:
horizons-orbital-mechanics (1.18), provenance-discipline (2.36),
orrery-coding-conventions (1.13; `mission_info` is hover text),
safe-file-editing (1.14), agentic-pre-test (1.3), and
ledger-and-session-records (1.23) for the close.

## Start

1. Record the base in the orrery folder (`git rev-parse HEAD`, `git
   ls-remote origin HEAD`, `git status`); stop if they disagree.
2. Read the skills above; name each with its version line.
3. Say Part 1 in one sentence and wait for Tony's go-ahead.

Plain speech, one question per message. Commit and push are Tony's.

Brief written November 14, 2026 with Anthropic's Claude Opus 5.5.
