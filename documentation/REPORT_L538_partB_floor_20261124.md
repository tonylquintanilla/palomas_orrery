<!-- Doc-Kind: hand | Part B's first report on L-538 (the orbiters' printed error): the measures and proposals the go-ahead's section 3 asks for before the room's code is touched, and the builder, validator and check built so far. -->
# L-538 (the orbiters' printed error): Part B, the floor and the room

Built on 9e7bb99ffb77799759abe5a3e6d6dc556853da8e at
https://github.com/tonylquintanilla/tonyquintanilla.github.io and
6a42ab3bc703bac58ad80d9b738c3cd546803d47 at
https://github.com/tonylquintanilla/palomas_orrery (branch main); ready
at "not pushed". Written November 24, 2026 by the Claude Code session
(Claude Opus 5.5) that wrote the Part A report, working from
documentation/COORD_L538_partB_goahead_20261124.md.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Read: the go-ahead whole, L-538's note of 2026-11-24 in the ledger, and
safe-file-editing 1.15 and ledger-and-session-records 1.24 whole before
the first edit. `patch_L538_2_partB_ruling_and_encounter.py` ran clean
(15 edits, the go-ahead written, ledger_index.py and doc_index.py --caps
"ok") and is moved into documentation/.

## The claim

The loop floor holds. BepiColombo, served a point a day outside the band,
never prints a figure smaller than its miss when the figure is the larger
of today's and its loop's reach times (1 + the parabola's weight sum):
0 over in 5,547 tests from its arrival to the end of JPL's data, worst
0.85. The room is not touched yet. The builder, the validator and the
widened check are built and pass the offline suite, 599 of 599.

## 1. Which craft gets which, measured week by week

Day-by-day steps by both tests, across each craft's whole capture from
the window's first day to the end of JPL's data, then the fine layer's
size for every week's window (about 88 days either side):
- JUNO: 71 to 614 fine points, every week from 2026-11-24 to 2028-11-21
  (36 to 46 KB until mid-2028, falling as the window passes JPL's end on
  2028-09-02). 132 questions for the two years; a night's 33.
- BEPICOLOMBO, whole-window: 13,138 points today, 17,650 (about 1.36
  MB) from 2027-01-12 to 2027-02-16, falling after JPL's end on
  2027-04-10. The coordinating session's arithmetic (13,400, 1.0 MB)
  was right in shape and low in size: from January most days need 15
  minutes and some 5. A whole night of it asked 191 questions, 73 s.
- PROPOSED: a limit of 3,000 fine points across the window
  (`CAPTURE_FINE_LIMIT`), five times Juno's most and under half of what
  BepiColombo projects the night it switches (6,684). The builder
  projects the next round's total before asking it, so a craft past the
  limit costs only the rounds below it.

## 2. The band

Yesterday 00:00 to the end of the day after tomorrow, at an hour,
refined by both tests: tonight BepiColombo's two pass days at 30
minutes, Juno's at an hour. The night builds at 08:17 UTC (a second
schedule at 12:17), and the date box shows 00:00 UTC of the day chosen,
so a visitor stays inside the band until about 40 hours after the next
build is due: one failed night is covered, two in a row are not. Outside
the band the box still holds, by the day's refined step (Juno) or the
floor (BepiColombo).

## 3. The floor

THE FORM. The larger of the chord figure and R x (1 + L), where:
- R is the craft's farthest distance from its planet's centre over the
  days the three served points span, served per day;
- L is the sum of the sizes of the parabola's three weights at that
  minute (`position_at` has them): about 1.0 to 1.25 between evenly
  spaced points, larger next to the band's edge, where spacings differ.
WHY. The craft is its planet plus an offset of at most R. The parabola
through three points carries the planet's part to within about the chord
figure, and moves the three offsets by at most L x R; the craft's own
offset is at most R more. So the miss is at most about the chord figure
plus R x (1 + L).
WORKED FROM AND TESTED BY DIFFERENT POINTS. R comes from JPL's points
around Mercury's centre every 10 minutes (20,161 points; 3,938 to 66,901
km). The test is JPL's Sun-centred check points every 37 minutes from a
different start (5,412), and BepiColombo's daily points held out (135).
The forms side by side, from the arrival to the end of JPL's data:

    chord alone                540 over, worst 2.87
    larger of chord and R      224 over, worst 1.65
    larger of chord and 2R       0 over, worst 0.87
    larger of chord and R(1+L)   0 over, worst 0.85
    chord plus R(1+L)            0 over, worst 0.80

RECOMMENDED: the larger of the chord figure and R x (1 + L). Twice R
held too, but by luck of even spacing; at the band's edge L passes 1.
The sum is the strict bound, kept in reserve.

WHERE IT ENTERS: one place, `render_spacecraft.position_at`, given the
day's reach as an optional argument; the error is the larger of the
two, `err_from` "loop" when the floor sets it. The builder writes the
reach into the positions file it already serves (beside t, x, y, z), so
`build_spacecraft_traces` finds it in the payload the page already
fetches; no line of interactive.html changes. The readers, mapped again:
- makes: `render_spacecraft.position_at`, `build_spacecraft_traces`
  (meta `interp_err_km`), `build_point_traces` (no reach: unchanged);
- calls them: gallery/assembler/assemble.py, compose_children.py;
- reads it in the page: interactive.html, the spacecraft box (line about
  4618, `pathDistanceLine`) and the Lagrange points' two boxes (about
  4469 and 4570, `pointBox`, no reach: unchanged);
- prints it: gallery/solar_system_figures.js, `pathDistanceLine`;
- checks it: tools/test_curve_error.py, the builder's capture pass,
  tools/test_compose_children.py (points only),
  documentation/smoke_room_clock.js (its witnesses are Mercury and
  3I/ATLAS, no capture craft), documentation/smoke_solar_system_figures.js
  (the rounding, unchanged);
- golden artifacts: none holds a craft in a capture.

THE BOX'S WORDS. No change needed, I think: every spacecraft's box
already prints "x AU from the Sun (y km)" to the place its working-out
earns, with no words about why, so BepiColombo's prints fewer digits in
the same sentence.

## 4. The four smaller things

- THE LIMITS, measured with the builder's own pass live tonight: Juno 33
  questions, 13.6 s, 501 fine points, none over; BepiColombo 10
  questions, 12.9 s, switched to the band at 6,684 projected, 233 fine
  points, its loop's reach 5,650 to 66,901 km. Set: 80 questions
  (`CAPTURE_QUESTION_LIMIT`), and no question longer than 40,000 rows:
  JPL refuses a list of moments past a few hundred (measured), so each
  run of failing days up to a week apart is one question.
- THE CHECK POINTS' START moves each night: 3 + (Julian day x 11 mod 37)
  minutes past the span's first minute, printed in the record and on the
  served block (5 tonight, 16 tomorrow).
- HOW FRESH JPL'S PATH IS, now read from JPL's own header and printed:
  BepiColombo "Revised: Nov 23, 2026", "Data fit through 2026-Nov-17,
  prediction thereafter.", trajectory bc_mpo_fcp_00243_20181020_20270411;
  Juno "Revised: Nov 03, 2026", spk_rec_110805_*_260824, no fit date
  printed. The plan's old arrival does not mislead the room's list: the
  list reads only the bodies a plan names. JPL today puts the arrival at
  18:44, 3,071.2 km; the plan of Nov 4, 18:48, 3,073.0 km. The thousands of
  km were the orbit after it, which the fine layer replaces.
- WHAT A NIGHT COMMITS: the raw archive is committed every night (the
  builder adds all of data/solar-system/). The fine layer adds about 59
  KB for Juno and 28 KB for BepiColombo there; BepiColombo's positions
  file stays near today's 115 KB; the check points as saved are 421 KB
  (Juno) and 212 KB (BepiColombo). Measured against the repository's 84
  MB in Part C.

## 5. Built so far (gallery, not pushed)

- tools/gallery_cache_builder.py: the capture pass (`capture_of`,
  `capture_span`, `build_capture_layer`, `process_capture`, the served
  `capture` block, the check points saved under raw/checks/), the
  validator's #O (`capture_problems`), a path body kept out of the window
  by name, JPL's header read (`fetch_path_revised`).
- tools/test_curve_error.py: "Curve error" holds every capture craft,
  held out and against the saved check points, with its own self-test.
- tools/test_gallery_cache_builder_offline.py: 11 new checks on two
  stand-in craft, every planted fault of the brief caught by name; the
  stand-in spacecraft's arc made continuous within a day. 599 of 599
  pass (588 on the base, run on a throwaway copy of HEAD).
- NOT BUILT: the floor in `position_at`, the reach in the positions
  file, the check of the floor. Until they are, "Curve error" is red: on
  today's served cache by name for Juno and BepiColombo (no fine points
  served yet), and after a build for BepiColombo outside the band. So
  the website must not be pushed before Part C.

## 6. The one question

The check points, saved so the gallery run can hold the box offline, add
about 0.6 MB to every night's commit. I recommend saving every fourth one
(still about 1,700 for Juno and 900 for BepiColombo), since the build
itself tests all of them and refuses the night on any miss. Save all of
them, or every fourth?

## Where this leaves us

- The floor's form and where it enters are proposed; the room waits for
  the go-ahead.
- Nothing is pushed in the website; its Curve error row is red by name
  until Part C.

Written November 2026 with Anthropic's Claude Opus 5.5.
