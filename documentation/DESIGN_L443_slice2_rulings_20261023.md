<!-- Doc-Kind: hand | Design record: Tony's rulings for L-443 slice 2, the spacecraft and the comets on open paths, with what was measured to put them to him. -->
# Slice 2 of the objects: the design talk's rulings

Tony Quintanilla, PE | Claude Opus 5.5 | October 23, 2026

Built on orrery b90d895a4ef1cdc31daec7a20fef8c34369fa24c at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 25e4d24228a191622df68b447f519782162977ea at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main), both read with git ls-remote on Oct 23.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: DESIGN SESSION (zero code). Held from Tony's phone on the
afternoon of Oct 23, after the view talk (L-472).

Companion to: `documentation/DESIGN_L443_objects_rulings_20261022.md`
(slice 1's rulings, which sent the spacecraft and the 14 open-path
comets to this slice) and `documentation/HANDOFF_L443_slice1_build_20261022.md`,
section 6. Supersedes nothing.

Skills the build fires, by name: horizons-orbital-mechanics (nearest
approaches, which record serves a body, the 30-day cycle),
gallery-cache-builder (the builder fetching by the plan),
interactive-exhibit (the room drawing the paths, the hover words),
gallery-assembler (the drawn path), provenance-discipline (any typed
date or number), safe-file-editing, agentic-pre-test (orrery code).

## 1. The rulings, in Tony's words

Each ruling answers a question put to him in the chat, with the
measurements in section 2.

1. **One path rule, the orrery's.** Asked whether every path in slice 2
   should take a coarse backbone, thinned where it runs straight, with
   fine steps around each event, the window and the step worked out
   from that event's distance and speed, and the events read from the
   orrery: "Yes, confirmed. Good solution."
2. **The orrery and the website alike.** "if there are better
   approaches for the orrery maybe we can implement them there also so
   the two are as Consistent as possible." Agreed: the orrery works out
   each path's plan once and serves it, as it places the stored
   drawings; the website's builder fetches by it, and the orrery's own
   plot later draws by it. The orrery's side is its own ledger item,
   L-476, after slice 2.
3. **The first set is group A.** "I agree, A." The twelve spacecraft
   still flying among the planets (section 2).
4. **A flyby belongs in the room of the body flown past.** "the
   respective spacecraft encounters should be included in that body's
   room, so for voyager 1 Jupiter and Saturn for Example." And what the
   room shows: "The room should show the flyby so basically the high
   curvature part and nearest approach or approaches if many orbits are
   involved." For road stages 12 and 13, not this slice.
5. **The nearest approach places an event; a sourced date is extra.**
   "Maybe use the nearest approach which is mechanical instead of a
   sourced date although a sourced date can be added for the hover or
   info." The nearest approach is found from JPL's own positions and
   needs no citation. A sourced date, where one is added, carries its
   own citation.
6. **Solid to today, dashed after, for both.** For the spacecraft: "Yes
   planned as dashed would be good. But the orrery does not do this
   today." For the comets too: "One rule for both." The part after
   today is JPL's own: Horizons' planned trajectory for a spacecraft,
   as far as the mission's plan runs, and its prediction from the
   fitted orbit for a comet; never a line the website extends (Tony:
   "Is the predicted served by JPL not a line projection right?").
7. **The future part is fetched again on the 30-day cycle.** "Yes and a
   30-day check for updates sounds right and fits our method."

## 2. What was measured to put them

Read on Oct 23 at the SHAs above, not run unless it says so.

- **The orrery's 27 spacecraft** (celestial_objects.py, ids starting
  with "-"), none with a 'key', so none is exported to the website.
  Voyager 1 is on the website from before the export existed.
- **Group A, twelve, still flying among the planets:** Voyager 1,
  Voyager 2, New Horizons, Juno, Lucy, JUICE, Psyche, Clipper (Europa
  Clipper), BepiColombo, SolO (Solar Orbiter), Parker, OSIRISAPE
  (OSIRIS-APEX).
- **Group B, near Earth, for the Earth room later:** JamesWebb, Gaia,
  SOHO, Artemis II.
- **Group C, ended, for when a date can be chosen:** Pioneer 10,
  Pioneer 11, Galileo, Cassini, Rosetta, Akatsuki, DART, Hayabusa2,
  OSIRISREx, MarsRover, Apollo 11 S-IVB.
- **The 14 comets on open or barely closed paths** (slice 1's rulings,
  section 2): Tsuchinshan, ATLAS (C/2024 G3), West, McNaught, C/2025
  K1 and fragments B, C, D, PANSTARRS (C/2025 R3), Borisov (C/2025
  V1), 1I/Oumuamua, 2I/Borisov, 3I/ATLAS, Wierzchos.
- **Flybys on record** (spacecraft_encounters.py, SPACECRAFT_ENCOUNTERS):
  three spacecraft. New Horizons (Jupiter Gravity Assist, Pluto Flyby,
  Arrokoth Flyby), Psyche (Mars Gravitational Assist, Flyby of
  Phobos), Artemis II (Earth Departure (TLI), Lunar Closest Approach,
  Reentry & Splashdown), each with dist_km and v_kms.
- **The orrery's curvature rule** (spacecraft_encounters.py,
  `_calculate_encounter_resolution`): the step is the time to travel
  half a circle at the flyby distance and speed, over about 30 points,
  snapped to a Horizons step; the window is one and a half times the
  time to cross four flyby distances either side. It serves the
  encounter views only.
- **The orrery's whole-path plot** (palomas_orrery.py,
  `create_dates_list_for_object`): an even count of points across the
  object's dates, the count set in the GUI.
- **The orrery's close-pass orbit from elements** (idealized_orbits.py,
  `plot_hyperbolic_osculating_orbit`): points densest at closest
  approach, spreading toward the open ends.
- **The website's Voyager 1** (gallery data/objects_config.json and
  tools/gallery_cache_builder.py): a point every 7 days from launch,
  thinned by Douglas-Peucker at 0.02 AU where the path runs straight;
  daily points inside two flyby windows typed into the config with no
  source (1979-02-15 to 03-25 and 1980-10-25 to 11-25); 223 points
  served; each night appends the last 8 days, one small query.
- **Dashed lines can be drawn.** Plotly 2.35.2's own schema, read from
  the shipped bundle: scatter3d `line.dash` takes dash, dashdot, dot,
  longdash, longdashdot and solid. The comment in gallery
  `gallery/assembler/render_orbits.py`, `build_orbit_traces` ("scatter3d
  line has no 'dash' attribute (2D-only)") is wrong; corrected when
  slice 2 opens that file. How a dashed line looks on the phone is
  Tony's to judge.

## 3. For the build session: method, not rulings

These are how the work is done, decided by the skills (the protocol's
Method Belongs to the Skill); a case a rule cannot express comes back to
Tony.

- Each group A spacecraft gets its 'key' in celestial_objects.py, with
  its description's numbers checked against a page opened that day,
  as slice 1's were.
- The plan is made in the orrery and served in its export: for each
  path, its span (launch or the record's start, to the end of JPL's
  data), its events, and each event's window and step.
- An event is a nearest approach found in JPL's positions, by a coarse
  pass then a fine one, as `resolve_encounter_time` already does: a
  spacecraft's to each body it passes, every close pass for one in
  orbit (Juno), a comet's perihelion. Voyager 1's two typed windows are
  replaced by events found this way.
- The future part is fetched again on the Horizons check's 30-day cycle.
  Its words in the hover ("planned" for a spacecraft, "predicted" for a
  comet) are visitor words and go to Tony before they ship.
- L-461 (pull matches push) builds with this slice, as recorded.
- The nightly cost is measured on the first real build, as slice 1's
  was.

## 4. Where this leaves the slice

Designed. The build follows Tony's phone look of the L-472 patch, on a
base that includes patch_L472_1 and patch_L472_2.

## 5. The Settled lines today's patches took off Where We Are

Kept here word for word, to keep the page under its line cap. Each
ruling also lives in the skill that fires on it.

- A citation's web address goes on its own Source line. Links checked
  every 30 days. Problem reports through the guest book's form. (Oct 20)
- Earth's dipole cone drawn, unticked. Agency pages read one layer
  down. Report words approved. (Oct 21)
- Every view, still and animated, opens on the farthest thing drawn,
  shell or orbit, plus 20%; the center body's axis and cone end just
  past its farthest shell. Kelvin stays. (Oct 18-19)

Session record written October 2026 with Anthropic's Claude Opus 5.5.
