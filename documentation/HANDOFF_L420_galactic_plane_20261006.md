<!-- Doc-Kind: hand | Session record for L-420, the galactic plane and the galactic centre in the orrery. -->
# Handoff: L-420, the galactic plane and the galactic centre

Built on orrery 51436054330aefd6be2a7efd93ebd58f06c4a2d2
at https://github.com/tonylquintanilla/palomas_orrery
(gallery ed48d078ceb639f5f98f13f4c6abc129f722c566
at https://github.com/tonylquintanilla/tonyquintanilla.github.io;
not touched). Pushed at: (Tony writes the SHA here.)

- Type: BUILD.
- Supersedes: nothing. Runs beside the two sessions of 2026-10-05,
  Earth's website patch and the Horizons design round, and touches
  neither's files.
- Patches, in order: `patch_L420_2_galactic_plane_and_centre_20261006.py`
  (the code), `patch_L420_3_session_close_20261006.py` (this record, the
  ledger, a line in the website session's handoff).

## What was asked

- Tony, 2026-10-06: "Build L-420". The design was ruled on 2026-10-05:
  the galactic plane and its poles in the Celestial Grid, the galactic
  centre in the Star Background.
- Tony confirmed the plan and the words: "Yes, confirmed as
  recommended".

## What was done

- The galactic centre's row was sourced first.
  - Source: Liu, Zhu and Hu, arXiv:1110.6268, sec. 3.2, eq. (8), read
    as the ar5iv HTML rendering on 2026-10-06 by Claude Opus 5.5. It
    prints Sgr A*'s position from Reid and Brunthaler (2004), measured
    with the Very Long Baseline Array: 17h 45m 40.0400s,
    -29 deg 00' 28.138".
  - It is the same paper the galactic pole rows already cite.
  - New rows in `constants_new.py`: `SGR_A_STAR_RA_ICRS_ARCSEC`,
    `SGR_A_STAR_DEC_ICRS_ARCSEC` (exact as printed), and the derived
    `SGR_A_STAR_RA_ICRS_DEG`, `SGR_A_STAR_DEC_ICRS_DEG`.
- A check on the existing pole row came free.
  - The paper's eq. (7) gives the point the frame defines as galactic
    longitude zero.
  - It lies on the plane drawn from the store's pole to a
    hundred-millionth of a degree.
  - Sgr A* sits 0.05 degrees from the plane. Nothing drawn can show it.
- `star_sphere_builder.py`
  - `build_galactic_grid()` computes the galactic plane and both poles
    from the store's rows when the plot is drawn. The saved star file,
    `star_data/star_sphere_vmag35.json`, is not rebuilt.
  - Celestial Grid: a violet circle, and violet crosses labelled NGP and
    SGP, drawn the way NCP/SCP and NEP/SEP are.
  - Star Background: a violet dot labelled "Sgr A*", always hoverable.
  - Fixed in passing: with Labels on, the celestial and ecliptic pole
    hovers showed the short label ("NCP") where the full name was meant.
    The hover pointed at the label field instead of the name field.
- `palomas_orrery.py`
  - Both "Ecliptic Coordinates (J2000)" boxes, the static plot's and
    the animation's, gain the violet-circle line.
  - The Celestial Sphere, Star Background, Celestial Grid and Labels
    tooltips name the plane, its poles and Sgr A*.

## The words, as approved

- Sgr A* hover:
      Sagittarius A*
      The black hole at the centre of our galaxy
      Its direction from the Sun, among the stars
- Galactic pole hovers, with Labels on:
      North Galactic Pole (NGP)
      Perpendicular to the disk of our galaxy
  and the same for the South Galactic Pole (SGP).
- Box line:
      Violet circle: Galactic plane, the disk of the Milky Way
      (NGP, SGP its poles)
- No number is printed, so the tilt of the plane (about 60 degrees to
  the ecliptic) needed no derived row.

## Verified, and how

- Both patches ran on a copy of 51436054 and a second run refused.
  patch_L420_2 also ran on a CRLF copy and wrote the same bytes.
- py_compile on the three code files; the GUI started headless.
- The live call path: the GUI's `add_celestial_sphere_traces` is the
  edited function. It was called with each switch on and off:
  - Labels off: the new markers show their labels and no hover, as the
    other poles do. Labels on: the full names.
  - Star Background off: no Sgr A*. Celestial Grid off: no plane.
- The maintenance run, against the same run at 51436054:
  - Every checker gives the same verdict. Constants export rows go from
    101 to 105; derived rows read go from 34 to 36.
  - The scanner's Tier-1 findings are the same 296, compared file by
    file, not by the total. A first build added one, a docstring saying
    "90 degrees"; it was reworded before delivery.
  - The two new measured rows score 15, cited and not yet cross-checked,
    the same as the galactic pole rows.
  - Reset completeness fails in the sandbox at 51436054 too: it needs
    a Tk colour only Windows has. Not this patch.
- NOT verified: how it looks. That is Tony's look.

## Running beside the other sessions

- Where We Are was not rewritten: the website session owns it this
  round. The lines below are for the next rewrite, and patch_L420_3 adds
  a pointer to them in the website session's handoff.
- In the ledger this session edited only L-420 and the header stamp.
  Its edits match only the lines they change, so the sessions' patches
  apply in either order.

## For the next Where We Are

- Changed: the orrery's Celestial Grid draws the galactic plane, a
  violet circle, with its poles NGP and SGP; the Star Background marks
  Sagittarius A*, the direction of the galaxy's centre.
- Changed: the pole hovers show their full names with Labels on.
- Needs Tony: a look at the violet circle, the Sgr A* dot and the new
  line in the coordinate box.
- Road: not a stage of its own; an orrery item done between stages.
- Details: L-420.
- Changed: the desktop orrery opens on Linux and macOS again. Its
  panels use one grey, gray90, that every system knows (L-027).
- Needs Tony: a look at the panels on Windows, a shade darker than
  before; and, when convenient, a run on a Mac.
- Changed: each coordinate circle says what it is in a hover cross,
  and the galactic tide is brighter, with a cone showing its shape.
- Needs Tony: a look at the tide from the side, and a design decision
  on whether the phone gets the galactic plane, Sgr A* and the cone
  (L-408).
- Changed (2026-10-07): the galactic plane work in the orrery is
  finished. The tide shows its X, and the cone marks where the tide
  works hardest. Your look on the tide is done.
- Still waiting: the phone's design decision (L-408).

## Later the same session: L-027, the panel colour

- Tony asked why the maintenance run's Reset completeness check fails
  in the sandbox: "We should not have any windows only requirements.
  This is a cross platform project."
- Found: palomas_orrery.py set its panels to `SystemButtonFace`, a
  colour name only Windows knows, at 23 sites. On Linux the window
  never opens. The file history shows Tony's January fix (`gray90`)
  was swapped back on 2026-06-12 by commit ec333df, and later records
  read the damaged file as the original. Full account on L-027.
- Built: `patch_L027_1_panel_colour_20261006.py`. `PANEL_BG = 'gray90'`
  defined once, used at the 23 sites; agentic-pre-test 1.3 drops the
  colour swap from the headless test; protocol v3.83, with v3.80
  moved to the history file.
- Verified on a copy with both L-420 patches run first: the window
  starts headless with no swap; the maintenance run passes every
  checker, Reset completeness included, for the first time in the
  sandbox; the skill headers check passes; a second run refuses.
- Obligation: agentic-pre-test went to 1.3 at the commit Tony makes;
  this session loaded 1.2; the next session confirms its loaded copy
  reads 1.3 before any pre-test.
- Running beside the other sessions: this patch also edits
  PROJECT_INSTRUCTIONS.md. If another session lands a v3.83 first,
  this patch refuses at the header line and writes nothing; it then
  needs rebuilding on the new protocol.

## After Tony's look: the circles' hovers, the brighter tide

- Pushed at e7073fce. Tony's look: "looks great", with two notes --
  the galactic tide is very faint and its X cannot be made out, and
  the circles' descriptions should move from the box to hover
  markers on the circles.
- Found: a brighter tide alone shows two lobes, not an X. Tony chose
  a brighter tide plus a faint double cone where its strength peaks.
- Built: `patch_L420_4_circle_hovers_and_tide_20261006.py`, on
  e7073fce. The words Tony approved are on L-420.
- Tony noted the phone shows none of this; that design decision is
  recorded on L-408.

## Closed, 2026-10-07

- Pushed at 12693a53. Tony's look: "correct"; "images look great at
  5000. the X is clearly visible even without the cone."
- The points alone show the X, which the sketch had said they would
  not. The cone stays: "I think the cone is useful to illustrate the
  tidal influence as physics."
- L-420 closed by `patch_L420_5_close_20261007.py`. The phone's
  question stays on L-408.

## Tony-actions

(do)
1. Run `patch_L420_2_galactic_plane_and_centre_20261006.py` in the
   orrery root.
2. Run `patch_L420_3_session_close_20261006.py` the same way.
3. Run `orrery_maintenance_run.py`. Its Constants export step rewrites
   `data/constants_export.json` with the four new rows.
4. Move both patch scripts into `documentation/`, commit and push.
5. Plot with Star Background, Celestial Grid and Labels on, and look:
   the violet colour, the marker sizes, where the labels sit.
6. After steps 1 and 2, run `patch_L027_1_panel_colour_20261006.py`
   the same way, then the maintenance run again. Every checker should
   pass.
7. Look at the panels: a shade darker grey than before, the grey of
   January to June.
8. Move the script into `documentation/`, commit and push with the
   others.
9. Reinstall agentic-pre-test in Settings > Skills, and replace the
   Project's instructions with PROJECT_INSTRUCTIONS.md (v3.83).
10. Run `patch_L420_4_circle_hovers_and_tide_20261006.py`, then the
    maintenance run; move the script into `documentation/`, commit
    and push.
11. Plot the Sun with Galactic Tide, Celestial Grid and Star
    Background on. Turn until the violet circle is edge-on, and look
    at the tide and its cone; hover the three circles' crosses.

## Next session

- L-420 closed 2026-10-07.
- Close L-027 on Tony's run and look; confirm agentic-pre-test 1.3
  loaded.
- Nothing else is opened by this session.

Session written October 2026 with Anthropic's Claude Opus 5.5.
