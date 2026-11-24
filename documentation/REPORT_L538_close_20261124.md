<!-- Doc-Kind: hand | The closing report of L-538 (the orbiters' printed error): the check points kept out of the repository by Tony's ruling, the tests run again, the night's commit measured again, the closing records and three new items. -->
# L-538 (the orbiters' printed error): the closing report

Built on 9e7bb99ffb77799759abe5a3e6d6dc556853da8e at
https://github.com/tonylquintanilla/tonyquintanilla.github.io and
7513fbab23605334f4fec31c8583057350638451 at
https://github.com/tonylquintanilla/palomas_orrery (branch main); ready
at "not pushed". Written November 24, 2026 by the Claude Code session
(Claude Opus 5.5) that wrote the Part A, B and C reports, working from
documentation/COORD_L538_close_goahead_20261124.md, read whole.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

## The claim

JPL's check points are out of the website's repository, as Tony ruled
(Nov 24, 14:00). The night still tests the boxes against them, and a run
anywhere else names each craft it could not test. Every test passes
again. L-538 stays open until Tony's look on his phone.

## 1. The change

- `.gitignore` names `data/solar-system/raw/checks/`. The build writes
  the check points there as before. On a throwaway git repository made on
  the built copy, `git add -A -- data/solar-system/` takes 409 files and
  none under raw/checks; the night commit's refusal check
  (`git status --porcelain --untracked-files=all`) sees none either.
- THE NIGHT IS TOLD BY A FLAG, never guessed: `gallery_maintenance_run.py`
  hands the Curve error row `--night` in its night pass only (NIGHT_ARGS,
  night_checkers), which `daily_run.py --night` runs on GitHub's
  computers after the build, in the same workspace.
- `tools/test_curve_error.py`, `hold_captures`:
  - wherever the check points exist, they are held, as before;
  - with `--night` and none written, the craft is red by name;
  - anywhere else with none, the craft's line says its JPL half is NOT
    HELD HERE, with the night's own test as its served block records it,
    and it is not counted as held; its held-out half still gates. The
    row's last line names the craft not held.
- The builder's words about the saved points say they are never
  committed. Nothing else in the builder changed.

## 2. The tests, again

- The offline suite: 604 of 604. The new check plants the folder gone:
  the night's run is red naming both stand-in craft, and any other run
  names both as not held, none counted as held. It also holds the
  `.gitignore` line and that only the night's pass hands `--night`.
- Curve error on the built copy, four ways:
  - by day with the check points: "2 capture craft held to JPL's own
    points";
  - with `--night` and the check points: the same;
  - by day without them, as on Tony's computer after a pull: "0 capture
    craft held ... JPL's points not held here for bepicolombo, juno",
    each with its night's test (Juno 6,967 tested, 0 over, worst 0.978;
    BepiColombo 3,620, 0, 0.984), exit 0;
  - with `--night` and without them: FAIL, both craft named.
- The gallery run on the built copy: "53 of 53 gating checkers passed"
  by day without the check points, and "53 of 53" with `--night`.
- WHAT A NIGHT COMMITS, in place of Part C's section 3: the files the
  two craft change each night, compressed, are about 248 KB against
  200 KB without this work, so about 47 KB more a night before git packs
  it (Part C measured 112 KB with the check points). These files change
  only in part from night to night, so git's packing makes them smaller
  still; at most about 17 MB a year on a repository of 84 MB. What a
  visitor loads: all 42 spacecraft files, 1,084 KB to about 1,125 KB
  (the coordinating session's figure).

## 3. The closing records

- L-538: the coordinating session's note of the afternoon, word for
  word; this session's closing note; the Gap (Tony's push, the night,
  his look; the skill text for gallery-cache-builder owed to the
  coordinating session). It stays OPEN.
- L-529 (guided encounters): one line under its note of Nov 24, the
  design record and the recommendation, not ruled, that BepiColombo's
  arrival wait until JPL's path is fitted past it.
- THREE NEW ITEMS:
  - L-553 (a held body turns the night red): Chariklo in Part C, a JPL
    503, the held entry served with no as_of_today
    (`hold_from_prior`), the Solar System figures row refusing it.
  - L-554 (JPL's sentence when a path is a prediction): OPEN, Tony's
    decision; the coordinating session recommends the sentence in the
    spacecraft's source line, a small build of its own.
  - L-555 (orbiters in general): OPEN, its talk first, on
    `DESIGN_orbiters_in_general_20261124.md`; BepiColombo's arrival its
    first test.
- Where We Are, by section: the box, Do next, the road, Settled,
  Waiting on you (L-554 and the arrival's order) and the next design
  talk (L-555), Where the details are; still 130 lines above the
  marker.
- Part C's section 3 points here.

## Where this leaves us

- Built and tested; nothing pushed.
- After the push and the next night, Tony looks at the three boxes of
  Part C's section 4, and L-538 closes on his look.

Written November 2026 with Anthropic's Claude Opus 5.5.
