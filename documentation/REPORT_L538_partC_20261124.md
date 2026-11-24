<!-- Doc-Kind: hand | Part B's second half and Part C of L-538 (the orbiters' printed error): the floor and the reach built, the two faults fixed, the whole build tested on throwaway copies, and what Tony looks at on his phone. -->
# L-538 (the orbiters' printed error): Part B's second half and Part C

Built on 9e7bb99ffb77799759abe5a3e6d6dc556853da8e at
https://github.com/tonylquintanilla/tonyquintanilla.github.io and
7513fbab23605334f4fec31c8583057350638451 at
https://github.com/tonylquintanilla/palomas_orrery (branch main); ready
at "not pushed". Written November 24, 2026 by the Claude Code session
(Claude Opus 5.5) that wrote the Part A and Part B reports, working from
documentation/COORD_L538_partB_goahead2_20261124.md.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Read: the second go-ahead whole; agentic-pre-test 1.4 whole (it sends a
gallery builder deliverable to the gallery-cache-builder skill's layered
gate: the offline suite, a live build, the schedule), with
safe-file-editing 1.15 and ledger-and-session-records 1.24 read whole
earlier this session.

## The claim

On the dates a visitor can choose, Juno's and BepiColombo's boxes now
print an error never smaller than their real miss. Tested tonight against
JPL on a throwaway copy: no figure under its miss in 6,967 (Juno) and
3,620 (BepiColombo) of JPL's own points between the served ones, and in
every served point held out. The website's 53 gating checks pass on that
copy. Nothing is pushed; the live boxes change after Tony pushes and the
next night builds.

## 1. What was built since the first report

- THE FLOOR, as ruled: the sum, the chord figure plus R x (1 + L).
  `render_spacecraft.position_at` takes the day's reach (`reach_of`,
  `_loop_term`); `err_from` reads "loop" where the loop's term is the
  larger part. A day's reach applies to a trio of points whose span
  overlaps that day by more than two minutes, so a point at a day's first
  minute does not pull in the day before.
- THE REACH is served in BepiColombo's positions file beside t, x, y, z
  (`data.reach_t`, each day's 00:00 UTC; `data.reach_km`, rounded up to
  the metre), for the days a point a day apart only: inside the band the
  fine points hold the figure as they are. A file without a reach carries
  neither key. No line of `interactive.html` changed (its diff is empty).
- THE NIGHT'S TESTS use the figure the box will print and count every
  case, in the band and outside it; the count without the floor is kept
  as its witness (330 tonight).
- THE VALIDATOR'S #O also refuses a day without its reach, a reach
  inside the band, and a reach served for a craft served whole.
- THE CHECK POINTS SAVED: every fourth (`CAPTURE_CHECK_SAVE_EVERY`);
  the block and the record say both counts (Juno 6,967 tested, 1,742
  saved; BepiColombo 3,620 and 905).
- FAULT A, the pooled self-test: `test_curve_error.capture_self_test`,
  per craft. Every craft: its check points moved by ten times the figure
  and a kilometre, each caught (1,742 of 1,742; 905 of 905). A band-only
  craft: its reach taken away, its point a day must miss outside the band
  (83 do), or a finding by name. "Thinned to a point a day" is printed,
  not gated.
- FAULT B, the last arrival: `captures_of` reads every capture a plan
  carries, each ending at its departure, the next arrival or the span's
  end; `capture_of(obj, window)` uses the one whose stretch meets the
  window. Planted: a stand-in craft with a later arrival at Mars; read by
  its last arrival, the served craft ABORTs.
- The offline suite: 603 of 603 (the base's 588, the first report's 11,
  and 4 more: the room's floor worked by hand, the reach served and
  placed, the self-test per craft with three planted faults, the floor in
  #O, fault B).

## 2. The whole build, on throwaway copies

Two copies of the website at 9e7bb99f, one with the four changed files
and one without, each built by the night's own command from JPL at the
same time (19:15 UTC). Every served file compared by name, the build's
own clock stamps left out: 755 the same, 80 different, all of them:
- the two craft: positions/juno.json (290 points to 758),
  positions/bepicolombo.json (1,518 to 1,674, with its reach),
  raw/vectors/ of each (the fine layer kept apart), raw/checks/ of each
  (new), their entries in coverage_index.json (the capture block, the
  file's size and points), and the run record (its capture lines);
- 71 element logs, raw/elements/*.jsonl: each differs only in its run's
  stamp;
- the window's edges, in coverage_index.json, the clock block and the
  eight Lagrange points' entries: 30 seconds apart, each build's own
  minute; both 88.0 days either side, set by Mercury;
- Chariklo: JPL answered it with a 503 in the changed copy's build
  only, so it was held there from the morning's build;
- data/cache_swap_log.jsonl, each build's own line.
The changed copy then built a second night: Chariklo's hold ended, the
two craft's counts came out the same.

THE GALLERY RUN on the changed copy, after the second night: "53 of 53
gating checkers passed", Curve error "ok -- 3043 points held out across
21 served files, and 2 capture craft held to JPL's own points".
After the first night it was red on one row, Solar System figures:
"chariklo: the served cache has no as_of_today or trust". See section 5.

TONIGHT'S FIGURES (the build's record):
- Juno, whole: 502 fine points, 33 questions to JPL, 14.3 s; 0 over in
  6,967 check points and 500 held out; worst 0.98 of the figure.
- BepiColombo, band: 234 fine points, 10 questions, 13.9 s; 0 over in
  3,620 and 232; worst 0.98; its reach on 89 days, 5,650 to 66,528 km.
- JPL's header: Juno "Revised: Nov 03, 2026", no fit date; BepiColombo
  "Revised: Nov 23, 2026", "Data fit through 2026-Nov-17, prediction
  thereafter."

## 3. What a night commits

REPLACED by section 2 of `REPORT_L538_close_20261124.md`: the check
points are no longer committed (Tony's ruling of Nov 24, 14:00), and a
night now commits about 47 KB more before packing. As written first:

The files these two craft change each night, compressed: about 312 KB
against 200 KB without this work, so about 112 KB more a night before
git packs it. The check points are 64 KB of it and change whole each
night (their start moves), so they will not pack much smaller. The
repository is 84 MB packed since February; the last five nights
committed 11 to 860 KB each once packed. So this adds between about 23
and 41 MB a year, roughly a quarter to a third more than the repository
grows now.

## 4. What Tony looks at on his phone

After he pushes the website and the next night has built (the night
pulls, builds, then runs the gallery checks). The Solar System room;
choose each date in the date box (it shows 00:00 UTC); tap the craft.
The figures below are tonight's build; the night's will be close.

- BEPICOLOMBO TODAY (Nov 24): before "0.3555374 AU from the Sun
  (53,187,640 km)", good to 7 km and off by 11.5 km. Now "0.35553741 AU
  from the Sun (53,187,639 km)", good to 0.4 km and off by less than
  0.1 km. One more digit.
- BEPICOLOMBO ON A DAY OUTSIDE THE BAND (Dec 20): before "0.4641167 AU
  from the Sun (69,430,900 km)", good to 20 km and off by 3,956 km. Now
  "0.464 AU from the Sun (69,400,000 km)", good to 25,461 km (the loop's
  reach) and off by 10 km. Fewer digits: this is the coarser, true
  figure Tony ruled for.
- JUNO ON ITS CLOSE PASS (Dec 16): before "5.33 AU from the Sun
  (797,000,000 km)", good to 574,154 km and off by 3,238,706 km. Now
  "5.3276211 AU from the Sun (797,000,770 km)", good to 4.5 km and off
  by 0.5 km. Many more digits.
The sentence under each ("JPL's own uncertainty ... is not served") is
as before.

## 5. Found in passing, not this item

A body held because JPL did not answer it is served with no
as_of_today (`hold_from_prior` in the builder), and the gallery run's
Solar System figures row refuses that, so any night JPL refuses one body
is red there, whatever else is right. Seen on Chariklo tonight. Recorded
on L-538's note for the coordinating session to give its own item.

## 6. Owed

- The skill text for gallery-cache-builder (the capture pass, the floor,
  the limits, the finer-step rule as method), which stands at its cap: not
  written here, by the brief.
- Tony's look, then L-538 closes.

## 7. The one question

The saved check points make the website's repository grow by about 23
MB a year more (section 3). Keep saving them, or keep them out of the
repository and let the night test them only?

## Where this leaves us

- Built and tested on throwaway copies; nothing pushed.
- The live boxes change after the push and the next night.

Written November 2026 with Anthropic's Claude Opus 5.5.
