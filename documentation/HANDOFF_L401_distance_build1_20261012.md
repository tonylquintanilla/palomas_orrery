<!-- Doc-Kind: hand | Session record for build 1 of L-401 (the orrery's distance digits): the body hover printed by the errors JPL states, the speed with it, the typed sky-position table out, the checker and its planted faults, and Tony's look at five hovers. -->
# Handoff: L-401 (the distance digits), build 1, the body hover

Built on orrery 47815de273b30966769f7c679f889537dba994a5 at
https://github.com/tonylquintanilla/palomas_orrery ("handoff L401") and
gallery e3536c8732d7b62faa5c09515e4b7f1d1c10af9c at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read, not
touched. Pushed at: Tony's commit after running the patch; the next
session reads it with `git ls-remote`.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 12, 2026 with Anthropic's Claude Opus 5.5.

- Type: BUILD, orrery only.
- Brief: `documentation/HANDOFF_L401_distance_build1_brief_20261011.md`
  (Fable 5.1, 2026-10-11). Design:
  `documentation/DESIGN_L401_distance_digits_rulings_20261011.md`.
- Patch: `patch_L401_3_body_hover_20261012.py`, saved in the orrery
  folder. Move it to `documentation/` after the run.
- Skills loaded, each matching the manifest: provenance-discipline
  2.28, horizons-orbital-mechanics 1.2, orrery-coding-conventions 1.10,
  safe-file-editing 1.13, agentic-pre-test 1.3,
  ledger-and-session-records 1.20. The 1.20 obligation is discharged.

## 1. Read this first

- *The hover now prints each distance and speed to the digits JPL's
  errors earn.* A planet by its published row; a small body by JPL's
  own uncertainty for the date, fetched with its position; anything
  else at whole kilometers with a sentence saying JPL states none.
- *One message to Tony: the look (section 6).* His verdicts go in his
  run record, one per line.
- *The obligation that travels:* horizons-orbital-mechanics went to
  1.3 in this patch; this session loaded 1.2. The next session confirms
  its loaded copy reads 1.3 before Horizons work.

## 2. What the patch does

Code (verified in the sandbox, section 5):
- `position_accuracy.py`, new. Works out the error for one body, one
  centre and one date, in one place the hover reads, and builds the
  hover's distance and speed lines from it. Also fetches a small body's
  position with its 2xr uncertainty.
- `visualization_utils.py`: `format_detailed_hover_text` prints its
  distance and speed lines through `position_accuracy.py`. One
  light-time line; the surface line only where the centre has a solid
  surface; plain numbers.
- `palomas_orrery.py`: `fetch_position` asks a small body's position
  with `VEC_TABLE='2xr'`, by a direct call, in place of astroquery's
  call; no extra query. If it fails, the old call runs and the hover
  says the uncertainty is not included.
- `palomas_orrery_helpers.py`: `fetch_trajectory` marks a frame it
  interpolated, or copied from another date; the animation's positions
  worked out from elements are marked too (in `palomas_orrery.py`).
- `celestial_coordinates.py`: `MAJOR_BODY_UNCERTAINTIES` and the
  "typical" fallbacks are gone. The sky line says "as seen from Earth",
  and that JPL gives no uncertainty where it gives none.
- `orbital_period.py`: the false sentence "JPL lists no orbit
  uncertainty for this body" now says why the Small-Body Database gave
  no sigma, in true words.
- `constants_new.py`: `DE430_MOON_POSITION_PLACE_KM` (the 2014 report's
  abstract, "The present-day lunar orbit is known to submeter accuracy
  through fitting lunar laser ranging data", read 2026-10-12) and
  `S_PER_DAY` (NIST SP 811, Table 6, "1 d = 24 h = 86 400s", read
  2026-10-12), and four Voyager rows, each spacecraft's predicted
  pointing uncertainty in RA and DEC from its Horizons data sheet.
  `constants_tokens.py`: the token `s_per_d`.
- `test_position_digits.py`, new: the checker. In the maintenance run
  as "Position digits (L-401)", with its dashboard button, "Test
  Position Digits".

Records: the spacecraft survey
(`documentation/SURVEY_L401_spacecraft_data_sheets_20261012.md`,
created), the ledger (L-401, L-431, L-399, the header stamp), Tony's
page by section, horizons-orbital-mechanics 1.3, the protocol v3.92
(v3.89 moved to the history), this handoff.

Permanent, after the script is archived: the two new modules, the two
rows and the token, the checker and its button, the skill version.

## 3. Method decided in the build (not Tony's; recorded so it is not re-asked)

- **A body with no stated error, seen from a centre with one.** If the
  centre's error is no larger than the kilometer floor, nothing that
  prints changes, and the pair keeps the no-error state: a spacecraft
  or a Lagrange point seen from Earth. If it is larger, it governs, by
  the larger-of-two ruling: a Lagrange point seen from Neptune prints to
  Neptune's 10,000 km place. The first draft kept none in both cases;
  the review below found the second one wrong.
- **An unstated error is not a large one** (Tony, 2026-10-12: "we know
  spacecraft distance to fine precision because of signal travel time,
  not to 10,000 km. actually, the precision of Neptune in that fly by
  would have been increased due to knowing where Voyager was, not
  Voyager's decreased."). "The true uncertainty may be larger" is said
  only where JPL does give a figure that is not included here (a small
  body's 2xr not fetched) or the position is not JPL's. A moon seen from
  the Sun (Io): its orbit about Jupiter is fitted, not unknown.
- **Then the Voyagers' data sheets (Tony's ruling "A", 2026-10-12).**
  Claude Fable 5.1 read the Voyager 2 sheet and found a stated figure;
  Claude Opus 5.5 read both Voyager sheets and surveyed all 26
  (`documentation/SURVEY_L401_spacecraft_data_sheets_20261012.md`).
  JPL's Voyager positions are a 2022 refit of tracking that ended in
  1992; each sheet states a predicted pointing uncertainty seen from
  Earth, for 2030, as an angle (Voyager 1: 1.701 and 1.535 arcseconds;
  Voyager 2: 4.718 and 3.715), and none for the distance. So the
  Voyager 2 case above was wrong a second time: Voyager is the weak
  part, by a lot. The hover now converts the larger angle at the
  spacecraft's distance from Earth (about 210,000 km for Voyager 1 and
  490,000 km for Voyager 2 today) and says the conversion is ours.
  The distance from Earth comes from the sky-position query (quantity
  20, astroquery's `delta`, same query). Where it was not fetched (the
  animation) the hover says JPL's figure is not included. Recorded
  rather than claimed: the angle is sideways to the line from Earth,
  while the hover's distance runs almost along it; the two-way tracking
  to 1992 constrained that direction better, but JPL gives no number,
  so the sideways figure is the only scale, and rounding to it can err
  only toward fewer digits. The 2030 figure is used for every date,
  coarser than JPL knew near the encounters. The sheets' 30-day re-read
  goes on the Horizons check, by Tony's word, in its own session (L-395).
- **The sky line's words narrowed:** "Horizons gives no uncertainty
  with it", not "JPL gives none", since a data sheet can state one.
- **Known limit, recorded:** the DE430 rows are today's accuracy,
  applied to every date. Near a flyby the spacecraft's tracking tied
  the planet to it (Voyager 2 at Neptune, 1989), so the true error of
  that distance was far smaller, and the hover is coarser than JPL
  knew: the safe direction, never finer. Using a spacecraft's tracking
  near its encounters belongs with the encounter markers' slice.
- **The Sun adds nothing, on either side.** A planet's published
  accuracy is that of its orbit about the Sun, so the Sun seen from
  Earth is as well known as Earth seen from the Sun, and prints by
  Earth's row. The design record's list of no-error cases names "the
  Sun as a body"; read literally, the Sun seen from Jupiter would print
  to whole kilometers, finer than Jupiter's own 100 km place. Seen from
  a barycentre the Sun has no stated error, which is the case that list
  covers. Raised here rather than settled silently.
- **The local pairs.** A moon seen from its own planet, or a body seen
  from its system's barycentre, has no stated error, except inside the
  Earth and Moon system (the Moon, Earth, their barycentre), where
  every distance is the Moon's orbit or a share of it, and the Moon's
  row applies.
- **What counts as a small body:** orbital_period's test by id_type,
  plus any small-body record number (9 followed by seven digits)
  whatever its id_type. From a centre other than the Sun, an entry
  with a small-body `helio_id` is fetched by its system record, which
  has no 2xr; its hover says JPL's figure is not included, not that
  JPL states none.
- **The words follow the figure that governs.** A floor case governed
  by a small body's own figure keeps the computed words; the part with
  no figure is named with the true reason (JPL states no accuracy, JPL's figure
  is not included here, or no accuracy is stated). A speed set by the
  one meter per second floor in a floor case says part of the speed has
  no stated uncertainty. No speed sentence when there is no speed.
- **Reading 1 uses the distance's printed precision.** "The same
  relative precision as its distance" is taken as the error the
  distance is printed by, the larger of its own and the whole-kilometer
  floor. For the Moon seen from Earth the floor governs.
- **A sigma of zero, or not a number, is no figure**, and lands in the
  no-error state with "not included".
- **Animation frames that are not JPL's for their date** state no
  accuracy: the positions the animation works out from elements, and
  the frames `fetch_trajectory` interpolates or copies from another
  date (both now marked).
- **The surface line** is left out for the Sun, Jupiter, Saturn,
  Uranus, Neptune and Planet 9, and for a centre with no radius in
  `CENTER_BODY_RADII` (it used to print the distance again with a
  radius of 0).
- **Unit conversions go through rows**, `S_PER_DAY` and `S_PER_HOUR`;
  the light-hour test is light time over one hour, from
  `SPEED_OF_LIGHT_KM_S`, with no typed 60.
- **The display rules carry their rulings as sources**: the half-unit
  (provenance-discipline 2.28), the 3-sigma level (the design record,
  section 4), the two floors (the design record and the brief).

## 4. Found, recorded and not chased (The Braid)

- The animation's positions come from `fetch_trajectory`, which does
  not ask for 2xr, so a small body's animation hover says its
  uncertainty is not included. One class with the other slices; the
  entries fetched by a system record from a centre other than the Sun
  are the same class.
- `orbital_period._is_small_body` reads id_type only, so C/2025_K1
  (record 90004912, id_type 'id') is not asked of the Small-Body
  Database and its period line says the database "has no entry".
  Recorded on L-431.
- The RA and Dec themselves print to fixed widths
  (`celestial_coordinates.extract_jpl_radec`). One class with the
  sourced angular figure for a planet, kept for later.
- `format_maybe_float` and `format_km_float` are unchanged. The hover
  no longer calls them; their other callers are other slices' sites.
  `visualization_utils.py` still imports them; harmless, left.

## 5. Tested (sandbox, which cannot reach JPL)

- py_compile on every touched file; ASCII and LF on every file.
- The headless run: the orrery's window opens under xvfb with no edit
  to the copy.
- Live dispatch, with JPL's answers stubbed from ones recorded
  2026-10-12: the real `fetch_position` and `add_celestial_object` for
  Mercury, Sedna and Encke from the Sun, Io from Jupiter, and Voyager
  1. The hover was read back from the figure. Sedna and Encke each made
  one 2xr query and no astroquery vector query. Sedna's 3-sigma came
  out at 257,819.985 km, against quantity 39's 257,817.569 km.
- A cold review by a separate Claude agent, which had not seen the
  work being made, before delivery. It found, and this build fixed:
  a no-error body ignoring a larger centre error (high); floor
  sentences that called a computed figure "published", or said "JPL
  states none" for a figure that was only not fetched; C/2025_K1 and
  the system-record entries classed as having no stated error; a zero
  sigma bringing back ten figures; a crash on a speed that is not a
  number and a speed sentence with no speed; Earth from the Earth-Moon
  barycentre; animation frames not from JPL carrying JPL's words. Each
  is now a fixture, a sweep or a planted fault in the checker.
- Tony's two corrections of 2026-10-12, before he ran the patch
  (section 3): no "may be larger" for a part JPL simply states no
  figure for; and, after Fable's reading, the Voyagers' data-sheet
  figures. The patch was rebuilt and replaced in the orrery folder
  each time.
- The checker: eleven planted faults, each caught by name (the brief's
  six; the 2xr call removed from `fetch_position`; the 2xr columns
  read by position; a no-error body ignoring its centre; a zero sigma
  taken as a figure; the Voyagers' data-sheet figures dropped). Then
  23 hovers and 165 lines against errors it works out itself, the
  Voyagers' from the four rows by name; five pairs printing the same
  from either end; every listed object hovered from the Sun, Earth and
  Neptune (496 hovers); odd inputs; three recorded 2xr answers.
- Maintenance run on a patched copy: 24 of 24, "0 TIER-1 -- the push
  gate holds". Whole tree 288 Tier-1, against 292 before: the typed sky
  table's four findings gone, none added.
- The patch twice (the second refuses, nothing written) and on a
  CRLF copy with notes of Tony's in the page and the ledger (matched,
  written LF, said so, notes kept).

Not tested here, and the patch's live check and Tony's look cover it:
JPL's real answers, the real 2xr text on Tony's machine, and the
window's hover.

## 6. Tony's look, one message

- Run `patch_L401_3_body_hover_20261012.py` from the orrery folder. At
  its end it asks JPL for the five bodies at today's date, 00:00 UTC,
  and prints each hover as the orrery will show it, and checks Sedna's
  3-sigma against quantity 39.
- Run `orrery_maintenance_run.py`: 24 of 24, and "0 TIER-1 -- the push
  gate holds".
- Open the orrery fresh (after the patch). Set the time to 00:00 to see
  the same numbers. Plot Mercury, Sedna and Encke from the Sun, Io from
  Jupiter, and Voyager 1, and hover each. Compare with the patch's
  printout line by line.
- What each should show:
  - Mercury: kilometers to the whole kilometer, AU to eight decimals,
    light-minutes; no surface line (the Sun has no solid surface);
    "rounded to JPL's published accuracy for Mercury's orbit"; the speed
    to the same relative precision, about six decimals in km/sec.
  - Sedna: kilometers to the nearest million, AU to two
    decimals, light-hours; "JPL's uncertainty for this position on this
    date, at three standard deviations"; the speed by JPL's velocity
    uncertainty, three decimals in km/sec.
  - Encke: kilometers to the nearest thousand; the same sentences as
    Sedna.
  - Io from Jupiter: whole kilometers; no surface line; "JPL states no
    accuracy for this position, so distances are shown to the whole
    kilometer"; "JPL states no uncertainty for this body's speed".
  - Voyager 1: kilometers to the nearest million (its sideways
    figure, about 210,000 km, sets the place), AU to three
    decimals, light-hours; "rounded to JPL's predicted sky-position
    uncertainty for Voyager 1 in 2030, 1.701 arcseconds seen from
    Earth", and that the conversion is ours; the speed to the same
    relative precision.
  - Every sky line says "as seen from Earth"; a planet's and Voyager's
    say "Horizons gives no uncertainty with it"; Sedna's and Encke's
    show JPL's figure.
- His verdicts, in his run record, "-- correct" or "-- not clear" per
  line: the no-error sentences; the Voyager sentence; the speed
  sentences; the reworded period sentence; the sky line's words; the
  light-time line; the surface line's presence or absence.
- Then move the patch into `documentation/`, commit and push.

## 7. Tony-actions

- (do) Run the patch, then the maintenance run.
- (do) Open the orrery fresh and hover the five bodies.
- (decide) The words, line by line, in the run record.
- (do) Move the patch into `documentation/`; commit and push.
- (do) Reinstall horizons-orbital-mechanics 1.3 to the account
  (Settings > Skills) from `skills/horizons-orbital-mechanics/SKILL.md`.

## 8. Tony's look, and its fixes (added 2026-10-12, at c5dff250)

Tony ran patch_L401_3 and the maintenance run (24 of 24, 0 Tier-1) and
pushed at c5dff250; his run record is
`documentation/WHERE_WE_ARE_10-12-26_1025_run_record.md`. He plotted the
Sun view (Mercury, Sedna, Encke, Voyager 1) and Io from the Sun and from
Jupiter, and sent the files; each hover was read out of them and matched
section 6. Io's 423,260 km was checked against its plotted position:
423,260.07 km. His verdicts, line by line in chat:

- The no-error sentences, the Voyager sentence, the speed sentences, the
  one light-time line: "yes".
- **The surface line, restored.** "previously we measured from 1
  radius"; "we decided 'surface' meant the solid surface or the gas
  surface as defined as one radius", more than a year ago, before the
  ledger. Build 1 had dropped it for the Sun and the giant planets on
  the reviewers' proposal. Now every centre with a radius gets it, as
  before. One radius is the 1-bar level for a giant planet and the
  photosphere for the Sun (IAU 2015 Resolution B3); 1 bar = 100,000 Pa,
  1 atm = 101,325 Pa (CGPM 1954), the convention is 1 bar. That
  Archinal et al. 2018 states 1 bar for Saturn, Uranus and Neptune is
  not yet confirmed. Detail on L-401.
- **The period sentence.** "why mention the small body data base it
  does not apply." A planet or moon now reads only "Rounded to how much
  the period changes in a year." Confirmed as recommended.
- **The sky line.** "are the two forms clear side by side? -- no."
  Option B, confirmed: "Sky position seen from Earth:", the two
  coordinates, one uncertainty line. The words offered were "none given
  by JPL for this body"; built as "none given by JPL with this
  position", because the Voyagers' sheets give a figure for 2030.

The lesson: a decision older than the ledger lives only in what the
code does. When a build would remove something the orrery already
does, it treats that as an old decision and asks first.

Also ruled in this session, on L-395 (the Horizons check): the check
moves into the orrery's maintenance run, beside the objects export.
Brief: `documentation/HANDOFF_L395_horizons_check_move_brief_20261012.md`.

Built by `patch_L401_4_look_close_20261012.py`: `position_accuracy.py`,
`orbital_period.py`, `celestial_coordinates.py`,
`test_position_digits.py` (13 planted faults, and a check of the period
sentence for six database statuses), and the records. Maintenance run
24 of 24, 0 Tier-1 on the gate path.

- (do) Run patch_L401_4, then the maintenance run; hover Io from
  Jupiter once; push.

Session record written October 2026 with Anthropic's Claude Opus 5.5.
