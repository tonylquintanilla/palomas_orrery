<!-- Doc-Kind: hand | Brief for a Claude Code session: road stage 14, the Moon's standards, with the Pluto row's records. -->
# Brief: the Moon's standards, and the Pluto row's records (road stage 14)

Built on orrery 197bc0d at https://github.com/tonylquintanilla/palomas_orrery
and gallery 6c93d0a at https://github.com/tonylquintanilla/tonyquintanilla.github.io
(both branch main, read Nov 6, 2026, 17:25 Chicago). This brief is pushed
after 197bc0d, so the session's base is one commit later; nightly bot
commits may follow.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BRIEF, for one Claude Code session through the python_work door.
Written by the coordinating session of Nov 6, evening (Claude Opus 5.5).
Tony's go-ahead, Nov 6, 17:25: "go thanks."

## Skills this job fires

Read each in full before the work, and name its version line against
the manifest. Two carry v3.127's open check: confirm that the copy you
load reads the version shown.
- interactive-exhibit 1.31 (open check), gallery-cache-builder 1.18
  (open check)
- horizons-orbital-mechanics 1.18 (confirmed loaded Nov 6), provenance-
  discipline 2.36, safe-file-editing 1.14, agentic-pre-test 1.3,
  ledger-and-session-records 1.22, orrery-coding-conventions 1.13 (for
  Part 2's marking only)

## Part 1: the Moon gets the orrery's standards (the build)

The road's words: "the Moon gets the orrery's words, link, period and
uncertainty."

Today, read at the anchor:
- The website draws the Moon in the Earth room as an orbit around Earth
  (`interactive.html`, the room's `"objects": ["moon"]`;
  `data/objects_config.json` slug `moon`, centre `@399`). Its entry has
  no description, no info link and no period.
- The orrery's Moon entry (`celestial_objects.py`, `'name': 'Moon'`,
  id 301) has no `'key'`, so `export_objects.py` does not export it.
  L-484 (the two agree) names the Moon among the served objects with no
  key, outside the check until it gets one.
- What the orrery has for it: `mission_info` and `mission_url`
  (NASA's Moon page) on the entry; a `'Moon'` entry in
  `info_dictionary.py`; and its accuracy row in `position_accuracy.py`,
  `DE430_MOON_POSITION_PLACE_KM`.

The change, by the method the skills already carry (the keying of
L-443's slices and of L-501, 2026 ED138, are the worked cases):
1. Key the orrery's Moon entry `'moon'`, the website's slug. JPL's exact
   name is read live from JPL the day it is keyed, never typed. Ask
   301 by the Horizons check's three steps: a bare number also finds
   small bodies.
2. Its period comes from the period fetch, around the centre the orrery
   gives a moon (Earth). Never typed.
3. Which of the orrery's sentences a visitor may read is the provenance
   rules' call (provenance-discipline, What a Visitor Reads). An
   unsourced sentence stays out, and the gap is named.
4. The uncertainty: find what the website prints for the Moon's
   position accuracy today, and whether the orrery's DE430 row reaches
   it. A number with no citation is not served.
5. The website picks up the key in the same round: its objects mirror
   copies the new fields onto the `moon` entry. Then the Daily Run's
   pull has to match the push.

Stop and bring Tony ONE question if: JPL cannot be reached (UNREACHABLE
is not a pass); the website would print a number with no citation; or
the words need his choice.

Done when: both repositories' maintenance runs end all green, read from
their output; the Moon is in the Horizons check and in L-484's check by
name; and Tony has looked at the Moon's text box in the Earth room.

## Part 2: the Pluto row's records (no build)

Tony's rulings of Nov 6, in his words. From his run record
`documentation/WHERE_WE_ARE_11-6-26_1625_run_record.md`: "for a solar
system view the barycenter vs pluto is trivial. however, for a local
view, say a pluto drawer, it is not trivial, and we should show the
barycenter and the pluto - charon pair orbiting around it. and drawing
the other moons around the barycenter is critical otherwise their
orbits are drawn distorted. ... the orrery has a legacy option to have
the center as pluto, which indeed plots the moon orbits distorted. we
don't need this option." Then, at 17:20: "are we creating a pluto room
now? or just keeping the solar view." The coordinating session's answer
was that we are keeping the Solar System view, and Tony's "go thanks"
(17:25) accepted that answer with this brief.

Record, without building:
- L-150 (trusting a near-equal pair): the Solar System room's Pluto row
  stays as it is: the Pluto-Charon barycentre (JPL 9), named Pluto, with
  its sentence. The local view is ruled for the Pluto room (road stage
  15): centred on the barycentre, Pluto and Charon circling it, the
  other moons drawn around it.
- L-509 (obsolete code): the second case. The orrery's Pluto-centred
  view of the moons (`idealized_orbits.plot_pluto_barycenter_orbit`,
  its `center_id='Pluto'` "Traditional view" mode, and wherever the GUI
  offers it). Map every place first, then mark each one DEPRECATED in
  the form `palomas_orrery.py` already uses, with no change to what it
  does. It is removed when the Pluto room is built, or when L-509's talk
  rules.
- Where We Are: the Pluto line leaves Waiting on you, and a Settled line
  takes its place.

## At the end

The records skill's session close, and Tony's file list, run order and
action rollup. End with the token count as Claude Code prints it.

Written November 6, 2026 with Anthropic's Claude Opus 5.5.
