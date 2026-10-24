<!-- Doc-Kind: hand | Coordination note: Tony's ruling of Oct 23 on Gonggong's skip (L-470), from a talk-only session; the next machine session builds it. -->
# Coordination note: Gonggong comes off the skip lists, and the run is the test

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session, talk only) | October 23, 2026

Built on orrery b90d895a4ef1cdc31daec7a20fef8c34369fa24c at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 25e4d24228a191622df68b447f519782162977ea at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main).
Both read live with git ls-remote on Oct 23. Three patches from the
afternoon's build session sit unrun in Tony's folders (website patch 1,
orrery patches 2 and 3 of L-472); this note does not depend on them.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: COORDINATION NOTE (zero code). Closes the discussion owed on
L-470 (entries the website cannot serve). Companion to
horizons-orbital-mechanics 1.9, Which Record Serves a Body.

## What was found, from the files

- Gonggong is on all six skip lists in `palomas_orrery.py` (lines 4461,
  4687, 4898, 5848, 6455, 6946 at b90d895) and on `SKIP_NAMES` in
  `period_fetch.py` (line 138). No comment names what failed.
- Commit c60572d, 2026-02-04, "Center bodies and social media view",
  put it there: Weywot came off the lists ("JPL data works at Quaoar")
  and Gonggong went on in the same edit, with Weywot's comment left
  beside it. The lists' heading, "These TNO moons have no usable JPL
  parent-centered ephemeris", does not describe Gonggong.
- Tony, Oct 23: "I'm not aware of any problem." No note in the code or
  the ledger records one.
- Gonggong IS served on the website (the trans-Neptunian group, about
  90 AU today); the skip only stops the orrery fetching its orbit
  elements and the period fetch asking for its period, so its hover
  carries the one typed period among 62 bodies ("550.34 years. Typed
  value, not fetched from JPL").

## Tony's ruling, Oct 23

"Yes, or just take it off the skip list and see if it fails."

Read as: the test the skill calls for runs through the checks that
already exist, not through a separate probe. Remove the name, run the
maintenance run, and let the run say whether JPL answered.

No rule is written in advance for a mixed result (JPL answering around
the Sun but not around another centre); it is written only if the test
produces that case.

## What the next machine session builds

One small orrery patch, then the runs:

1. Take Gonggong off all six lists in `palomas_orrery.py` AND off
   `SKIP_NAMES` in `period_fetch.py`, in the same patch.
   `test_period_fetch.py` holds the copy to its source, so the two
   must move together.
2. The maintenance run. The period fetch asks 2007 OR10 (the small-body
   record) around the Sun; the Horizons check confirms it. A failure is
   named in the run's output. If it fails: revert, and the skip line
   gains its comment (record, centre, date), as the skill requires.
3. One look in the orrery with Gonggong as the centre body, to cover
   the centre the maintenance run does not ask.
4. If all of it answers: commit and push; the website's Daily Run pulls
   the fetched period and the typed one is replaced. L-470's Gonggong
   instance closes.

## Tony-action rollup

- **(do)** At the next machine session, after the three L-472 patches
  are run and pushed: the Gonggong patch and the runs above.
- **(do)** Save this note's ruling into your run record, or leave this
  file where it is; the next session reads documentation/ either way.

Written October 23, 2026 with Anthropic's Claude Fable 5.1.
