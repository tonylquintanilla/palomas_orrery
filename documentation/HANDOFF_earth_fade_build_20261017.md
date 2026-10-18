<!-- Doc-Kind: hand | Session record of Earth's fade build (L-410): the hydrogen exosphere drawn as stored dots that thin out from 3 to 100 Earth radii in both instruments, three patches with Tony's run order; and the brief for the next session, Earth's design talk 2 (L-356 with L-375, and L-454). -->
# Handoff: Earth's fade, the build; and the brief for design talk 2

Built on orrery 785536e5b700518d17c86d8381f0994a15d20bb7 at
https://github.com/tonylquintanilla/palomas_orrery ("L330 leo contrast
close") and gallery 44a6225c0049a36e72c770ad4557be31dde72250 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io ("L330
website belt words L449 run records"). Nothing pushed by this session;
Tony pushes.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD (L-410, Earth's fade), and a brief for the next session's
DESIGN talk (section 5).
Companions: the design, `documentation/DESIGN_fades_rulings_20261017.md`;
the sources and rows, `documentation/SOURCES_earth_fade_20261017.md`;
the round-1 records earlier the same day,
`documentation/HANDOFF_earth_round1_build_20261017.md` and
`documentation/HANDOFF_earth_round1_close_20261017.md`.

## 1. Your run order (every Tony-action, in one list)

Each patch checks the files it edits and refuses rather than guess.

1. **(decide)** The look and the words, sent in the session with a
   render of both zooms. Run nothing below until they read right to you.
2. **(do)** Orrery folder: run `patch_L410_1_earth_fade_orrery_20261017.py`.
3. **(do)** Orrery folder: run `patch_L410_3_earth_fade_close_20261017.py`
   (the ledger, Where We Are, and this handoff).
4. **(do)** Orrery maintenance run (dashboard). Expect 31 of 31 gating,
   "Drawings export check" with 8 of 8 planted faults caught, and the
   gate line at 0 TIER-1. Your Earth plot this afternoon refreshed
   Earth's orbital elements (committed in 785536e5), so this run
   re-exports Earth's period and its Horizons check confirms it with
   JPL; that needs the internet, and would happen without these patches.
5. **(look)** Mode 5 in the orrery: plot Earth with the Exosphere
   (Geocorona) box on, and the belts. The dots thin out from Earth past
   the Moon's orbit; zoom in to see them among the belts. Hover the
   marker over the north pole, out at 100 Earth radii.
6. **(do)** Move the two orrery scripts into `documentation/`; commit;
   push. The website's Daily Run pulls the dots and rows from this push.
7. **(do)** Website folder: run `patch_L410_2_earth_fade_website_20261017.py`.
8. **(do)** The Daily Run. Expect its pulls to bring
   `data/drawings/earth_exosphere.json`, 29 of 29 gating, "Drawings"
   with 12 of 12 planted faults caught, and "Typed facts" with OPEN
   empty.
9. **(do)** Move the website script into `documentation/`; commit; push;
   then `python gallery_maintenance_run.py --live`.
10. **(look)** Mode 5 on the phone, in the Earth room: tick the
    exosphere; the dots, its hover, its i panel (the words and three
    Sources: where the dots start, the density, where they stop).

No skill changed, so nothing to reinstall.

## 2. What was built, and how it was checked

**Orrery patch (L-410).**
- `earth_exosphere_sampler.py`, new: 1,500 dots from 3 to 100 Earth
  radii. Each dot's distance is drawn from n(r) r^2, where n(r) is
  Zoennchen et al. (2022)'s eq. 7 to 15 Earth radii and then eq. 9's
  fall carried on from eq. 7's value there; its direction is even on
  the sphere; seed 410. Each dot's weight is the log of the density at
  its distance, 0 at 100 and 1 at 3 Earth radii, so both instruments
  shade it the same way. Its checks: every dot between the rows; in
  five shells, each holds the profile's share (four standard deviations
  or 15 percent); each weight is the one its distance gives.
- `constants_new.py`: the seven approved rows, and an eighth,
  `EARTH_EXOSPHERE_H_AT_RADII` (10 Earth radii), where the 35 atoms per
  cubic centimetre was measured, from the same abstract, so the hover
  does not type it. Three unit tokens in `constants_tokens.py`.
  `EARTH_GEOCORONA_RADII`'s note says it is now where the dots stop.
- `earth_visualization_shells.py`: `create_earth_exosphere_shell()` and
  the new hover words; `shell_configs.py` moves the exosphere from the
  sphere shells to the custom builders.
- `export_drawings.py` writes `data/drawings/earth_exosphere.json`;
  `test_drawings_export.py` checks it, with three planted faults (an
  inside dot, no fall-off, a wrong weight); 8 of 8 in all.
- `orrery_maintenance_run.py` watches the new file; the dashboard's
  Drawings Export card names all three drawings.

**Website patch (L-410).**
- `data/objects_config.json`: the geocorona is a `stored_fade` shape
  naming the drawing `earth_exosphere`; pointers to the four rows its
  words print (the mirror fills them at the Daily Run); each edge's
  sentence as its `hover_line`; the `about` and `note` in the approved
  words; the name drops "detected extent"; the sphere's opacity, point
  count and marker size are gone with the sphere.
- `gallery/feature_renderers.js`: `renderStoredFade()` draws the dots
  as given, scaled by Earth's served radius, turned to the pole, shaded
  by weight; one info marker over the pole at 100 Earth radii.
- `tools/check_drawings.py`: the exosphere is round, so it has no plane
  to check; it is judged by its mechanism instead -- between the served
  edges, centred on Earth, thinning out -- with three planted faults;
  12 of 12 in all.
- `documentation/smoke_display_figures.js` grades the two edge
  sentences by its own arithmetic, pinned: "3 Earth radii, about 20,000
  km (0.0001 AU)" and "100 Earth radii, about 600,000 km (0.004 AU)".
- `documentation/payload_earth_scene.json` re-recorded.
- `gallery_maintenance_run.py`: the live check also fetches the belts'
  and the exosphere's served dots (section 4).

**Tested.** Orrery: the maintenance run on a clean copy with the patch
applied; 32 of 33 checkers passed here, 30 of 31 gating, the one
red being "Horizons confirmations", which cannot reach JPL from the
sandbox to confirm Earth's re-exported period (step 4); "Drawings export
check" 8 of 8 planted faults caught; "Dashboard parity" green; the gate
line 0 TIER-1, whole tree 280 as before. Website: a stand-in for your Daily Run
(the patched copy, the orrery's new export and drawing laid in,
mirrored, the served features and drawings rebuilt): 29 of 29 gating.
Both patches applied clean, and on a copy with Windows line endings,
and refuse a second run. The website's own renderer was drawn headless
and matches the orrery's picture.

## 3. Choices made in the build, for your look

- The eighth row (above): One Value, One Home, not a design change.
- The shading: opacity 25 to 90 percent and size 1.5 to 3 by weight, as
  for the belts; the colour the old shell had, pale lavender.
- The info marker over the north pole at 100 Earth radii, where the old
  shell's sat.
- The 2024 paper's day-night sentence is cited on the row where the
  dots start, so a visitor sees the source of "denser near the line
  from the Sun to Earth" (What a Visitor Reads, principle 4).
- From 3 to 7 Earth radii the hydrogen's pale lavender dots sit among
  the outer belt's light blue ones; the two colours are close. Your eye
  decides.

## 4. Found, and where it went

- The live check's list of files the browser fetches named the Hills
  cloud's drawing but not the belts' (missed by L-330's patch 3). Fixed
  in the website patch, with the exosphere's.
- The orrery dashboard's Drawings Export card still described only the
  Hills cloud. Fixed in the orrery patch.
- Placing the new builder beside the old upper-atmosphere function
  pushed that dead function's text out of the scanner's reach of its
  citation (Tier-1 280 to 281). The builder was moved beside the
  low-orbit builder instead; 280 again. The dead function is L-254's.
- Owed to interactive-exhibit's next version: the `stored_fade` shape
  (L-435).

## 5. Next session: Earth's design talk 2 (the brief)

Tony, 2026-10-17: "we can hold the design talk 2 for the handoff." Zero
code. Three items, all about Earth's magnetic field and how it moves.
Read each in the ledger first; the questions below are where to start,
one at a time.

1. **L-356 (IGRF-14).** The belts' plane and the dipole cone use
   IGRF-13's 2020 coefficients, whose drift was a forecast for 2020 to
   2025; IGRF-14 replaces them. Question: re-source the six rows to
   IGRF-14 and move the epoch, so the hovers' "for 2020 (IGRF-13 model)"
   becomes the new model's date? Method says yes once read; the talk
   only needs to confirm the slice.
2. **L-375 (the dipole's offset).** Earth's magnetic dipole sits off
   the planet's centre, by an amount that turns with Earth once a day;
   neither instrument models Earth's rotation phase. Questions: is the
   offset shown at all; if so, as an envelope (the dipole cone's
   pattern) rather than one position; and whether the website draws the
   dipole cone, which only the orrery does today. The starting source,
   Koochak and Fraser-Smith (2017), has not been read: the publisher
   refused the session. Read it first.
3. **L-454 (edges that move).** The magnetopause and bow shock stay
   sharp at their models; their motion gets a second drawn device, like
   the dipole cone. The store already holds how far real crossings sit
   from each model (1.23 and 0.69 Earth radii). Questions: what the
   device looks like (a translucent band either side of the surface? a
   second surface at each end?), and what the spread means -- the
   crossings' scatter about the model, not the range the edge moves
   through with the solar wind. The Alfven surface and the
   heliosphere's edges are the same kind, in the Sun's slice later.

After talk 2, Earth's list (L-413) has talks 3 to 6; talk 4 (L-314)
keeps the solar-wind fetch.

## 6. Skill obligations

This session confirmed its loaded copies read provenance-discipline
2.30 and interactive-exhibit 1.17 (discharging v3.102's obligation for
both), and orrery-coding-conventions 1.10, agentic-pre-test 1.3 and
ledger-and-session-records 1.21, as the manifest expects. Still
travelling: gallery-cache-builder 1.11 (v3.102) and
horizons-orbital-mechanics 1.8 (v3.99); no work this session fired
either.

Session written October 17, 2026 with Anthropic's Claude Opus 5.5.
