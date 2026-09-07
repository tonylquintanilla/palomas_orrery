"""
patch_L290_1_relay_anchor_and_session_records.py

Records the 2026-09-06 evening session in the ORRERY repo, and applies
the L-290 relay-anchor amendment under the four-step binding rule.

FIVE files, all-or-nothing:

  LEDGER_CONSOLIDATED.md
      L-288 updated (built, run, Mode 5 passed by the Studio path;
                     Gap narrowed to the untested json_converter path)
      L-289 CLOSED   (Mode 5, patches 5 and 6, Tony's rulings)
      L-290 RULED and APPLIED -> PENDING-GATE on the reinstall
      L-291 NEW      Earth exhibit: shells plus the Moon
      L-292 NEW      Earth shells the orrery does not draw
      L-293 NEW      Lunar standstill exhibit
      L-294 NEW      Explorer placeholder / heliocentric Earth
      L-295 NEW      Upper atmosphere shell vs its own hover text
      L-296 NEW      One session one bump; plan versions per design build

  documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md
      v25 -> v26; stale Status sentence corrected; one appended
      "you are here" subsection.

  skills/ledger-and-session-records/SKILL.md      1.9 -> 1.10
      The second anchor line for relay partners (two forms plus the
      read-back); one session, one bump; the plan restamps once per
      design build.

  PROJECT_INSTRUCTIONS.md                         v3.53 -> v3.54
      Header re-anchored; "Documents as handoffs" extended; the v3.54
      entry added and v3.51 moved out to keep three resident.

  documentation/PROJECT_INSTRUCTIONS_HISTORY.md
      v3.51 received into PART 1.

RUN THIS BEFORE skills_index.py -- the guard on PROJECT_INSTRUCTIONS.md
is taken before the manifest zone is regenerated.

Built on orrery 50cbd2df708f8dc16cb181d204f49dd36f14b367
at https://github.com/tonylquintanilla/palomas_orrery

Run from the ORRERY repo root with VS Code's Run button.
Then run ledger_index.py from the same place (it regenerates the index
zone and migrates the DONE block to its closed bucket).

All-or-nothing: every edit is verified in memory before any file is
written. Guards on md5 of LF-normalized content. No .bak -- git holds
the committed copy, and the guard refuses to run against a modified
working copy (safe-file-editing 1.10, Git Is the Backup).
"""

import hashlib
import os
import sys

REPO_FILES = {
    "LEDGER_CONSOLIDATED.md": "f9c08a9cb48adcff5503e906e8416885",
    os.path.join("documentation", "MASTER_PLAN_INTERACTIVE_GALLERY.md"):
        "ef0d39f14a7e0811835503a8476827a5",
    os.path.join("skills", "ledger-and-session-records", "SKILL.md"):
        "579d8327797835e059e8b90f99589e14",
    "PROJECT_INSTRUCTIONS.md": "bc881c8c3319620da7e19eac5b822aef",
    os.path.join("documentation", "PROJECT_INSTRUCTIONS_HISTORY.md"):
        "2336abf04bf08475eff43a834c4e9ff6",
}

SENTINEL = "[L-291]"

LEDGER = "LEDGER_CONSOLIDATED.md"
PLAN = os.path.join("documentation", "MASTER_PLAN_INTERACTIVE_GALLERY.md")
SKILL = os.path.join("skills", "ledger-and-session-records", "SKILL.md")
PROTOCOL = "PROJECT_INSTRUCTIONS.md"
HISTORY = os.path.join("documentation", "PROJECT_INSTRUCTIONS_HISTORY.md")


# --------------------------------------------------------------------
# L-288: built and run; narrow the Gap to the untested converter path
# --------------------------------------------------------------------

L288_OLD = """**Gap:** design round, then the Studio action; `json_converter.py` v2
branch already writes storage cards, so the writer exists.
"""

L288_NEW = """- **Built and run 2026-09-06**, one all-or-nothing patch over three
  files (`documentation/patch_L288_1_studio_live_card.py`, written with
  Anthropic's Claude Fable 5.1). `tools/json_converter.py` gains
  `live_scene_urls()` -- moved out of the editor so both tools read one
  list -- and `add_live_card()`, which writes a schema-v2 storage card
  with `live` set and empty `files`, and refuses a non-v2 config, an
  empty title, or a scene that already has a card.
  `tools/gallery_studio.py` gains the "New Interactive Card..." button
  and its dialog (`_new_live_card`). `tools/gallery_editor.py` now
  imports the shared function instead of owning it.
- **The design question is ANSWERED: a live card carries no still
  picture.** It is a placard with an Interactive tag. Studio authors
  it, the editor places it. (Tony's rulings; the lobby pass settled the
  no-picture half on the phone.)
- **Mode 5, 2026-09-06, iPhone, gallery `b8c5d437`: PASSED** by the
  Studio path end to end -- Studio wrote the card, it landed in
  Storage, the editor placed it, the card opened the scene.
- **Tony-action (do):** exercise the JSON CONVERSION path. The patch
  edited `json_converter.py`, and only the Studio path was walked.
  Convert one card through the converter and confirm a v2 config
  carrying a live card round-trips.
**Gap:** the converter path above; then DONE.
"""


# --------------------------------------------------------------------
# L-289: closed
# --------------------------------------------------------------------

L289_META_OLD = ("<!-- L:289 status:OPEN upd:2026-09-06 section:A flag: "
                 "rice:3/2/80/1 -->")
L289_META_NEW = ("<!-- L:289 status:DONE upd:2026-09-06 section:A flag: "
                 "rice:3/2/80/1 -->")

L289_OLD = """**Gap:** Mode 5 on `patch_L289_4`; Tony's rulings above; then DONE.
**Ref:** L-267 (Sun exhibit GUI), L-278 (why the HUD never calls
Plotly), interactive.html, feature_renderers.js (poleBasis),
HANDOFF 2026-09-05 (away session), HANDOFF 2026-09-06.
"""

L289_NEW = """- **Mode 5, 2026-09-06, iPhone/Chrome, portrait and landscape, at
  gallery `b8c5d437`: patch 4 PASSED on all five trials** -- arrival
  state, the frame note, the triad through a touch rotation and an app
  switch, the HUD through +/-/Home and the drawer and a shell focus,
  and the L-288 Studio card. Protocol:
  `documentation/TEST_PROTOCOL_mode5_pre_earth_20260906.md` (gallery).
- **Tony-action (decide), DISCHARGED:** triad size "looks right"; the
  note's tap-toggle "works well"; triad colours accepted. Whether the
  EXPLORER room gets the same HUD: Tony's answer was "unclear", and it
  moves to L-294 rather than holding this item open.
- **The triad read as 90 degrees off the grid, and it was not.**
  Confirmed correct two independent ways: a hand projection of the
  arrival camera (eye 1.25/-1.25/0.75, up +z, aspect 1:1:1) predicts x
  right and about 21 degrees below horizontal, y right and 21 above, z
  vertical and 20 percent longer; measurement in Tony's screenshots
  gave 25 below, 22 above, z vertical, matching lengths. THE REAL
  CAUSE: the triad is an ORTHOGRAPHIC projection of three directions at
  the origin, while Plotly draws the box in PERSPECTIVE with the eye
  close in, so box edges at the frame corner project far steeper --
  measured 25 degrees on desktop, 45 on the phone. Compounding it, the
  Sun scene sets all three axis titles empty and the grid is uniform
  white, so nothing in the render could corroborate the triad.
- **Built and run 2026-09-06:** `patch_L289_5_axis_edge_colours.py`
  (guards `interactive.html` at `b8c5d437`) colours the three box edges
  meeting at the near corner -- `showline`/`linecolor`/`linewidth` on
  the Sun's scene axes, `?edge=N` (1..6, default 2) the Mode 5 switch.
  Verified against the installed plotly.js 2.35.2 source, not recalled:
  scene axes carry those keys (`lineEnable`/`lineColor`/`lineWidth` in
  `src/plots/gl3d/layout/convert.js`) and the edge is camera-selected
  by `computeLineOffset`, the same edge that carries that axis's tick
  numbers. Gallery moved to `9325c86f`.
- **Mode 5 on patch 5: desktop PASSED, phone FAILED.** In portrait the
  coloured edges run off the sides of the frame. Tony's redirect: draw
  the lines converging on the ORIGIN instead.
- **A trap avoided, read out of the bundle rather than recalled.**
  Plotly's zero lines cannot carry the triad's meaning: in
  `drawZero(j, i, ...)` the line runs along dimension `j` but takes
  `zeroLineColor[v]`, where `v` is the PLANE it sits in -- so the x
  colour would paint lines running along y and z. Separately, Tony's
  "the origin is half a tick off the centre" resolves as perspective,
  not as a tick error: Plotly paints grid and zero lines on the three
  background walls only, never through the interior, and `tick0` is
  already pinned to 0 on every path that sets spacing. No tick fix
  would give the cube a centre vertex.
- **Built and run 2026-09-06:** `patch_L289_6_origin_axes.py` (guards
  at `9325c86f`) adds three scatter3d line traces through the origin in
  the triad's hues (`sunOriginAxisPoints`, `sunCurrentHalfRange`,
  `sunOriginAxesInstall`, `sunOriginAxesUpdate`), installed after
  `buildSunDrawer` so the drawer gets no row and the arrival extent
  never counts them, re-cut to the current range on the `sunHudUpdate`
  hook (a `.then()` continuation, not an event handler -- the L-278
  hazard does not apply). `?axes=full|pos|off`, and `?edge=0` turns the
  box-edge colouring off. Rebuilt rather than drawn as one long clipped
  line because the nav buttons span 1e-5 to 5e3 AU and a two-vertex
  line loses the precision the clip test needs at the deep end (Plotly
  DOES clip 3D traces to the axis range -- fragment shader discards
  outside `clipBounds` -- both verified in 2.35.2).
- **The pre-test earned its place.** A standalone node exercise of
  `sunOriginAxisPoints` across three ranges and both forms found
  `axes=off` drawing the negative half instead of nothing -- unreachable
  today, since the install path returns early. Fixed before delivery;
  27 cases then passed.
- **Mode 5, 2026-09-06, phone: ACCEPTED.** Tony: "This works. It's a
  bit unusual but it is correct and one can't make a mistake!" All
  three lines cross at the Sun, z runs the full box height. `&axes=pos`
  (the three positive rays only, an exact match to the triad) is in the
  page and left as a non-default by Tony's decision; making it the
  default would be a one-line patch.
- **Tony-action (do):** archive `patch_L289_5_axis_edge_colours.py` and
  `patch_L289_6_origin_axes.py` to `documentation/` in the gallery repo.
**Gap:** none. CLOSED 2026-09-06 on Tony's Mode 5, per the rule that an
exhibit item closes on his eyes and not on the push.
**Ref:** L-267 (Sun exhibit GUI), L-278 (why the HUD never calls
Plotly), L-294 (the Explorer HUD question, carried out of here),
interactive.html, feature_renderers.js (poleBasis),
HANDOFF 2026-09-05 (away session), HANDOFF 2026-09-06.
"""


# --------------------------------------------------------------------
# New items, inserted after L-290's block
# --------------------------------------------------------------------

L290_TAIL_OLD = """**Ref:** L-276 (relay partners can read the repo; the Gemini snapshot
note), L-191 (the Fable relay), Mode 7 Key Principles,
skills/ledger-and-session-records/SKILL.md.

"""

NEW_ITEMS = """**Ref:** L-276 (relay partners can read the repo; the Gemini snapshot
note), L-191 (the Fable relay), Mode 7 Key Principles,
skills/ledger-and-session-records/SKILL.md.

#### [L-291] Earth exhibit: shells plus the Moon
<!-- L:291 status:OPEN upd:2026-09-06 section:A flag: rice:4/4/80/3 -->
- **Design settled 2026-09-06** in a zero-code conversation, step 1 of
  the `interactive-exhibit` skill's order. The full record, with every
  number and its source, is
  `documentation/PREDESIGN_earth_exhibit_20260906.md` (GALLERY repo).
  This entry is the handle; the record is the reasoning.
- **Scope:** Earth's shells plus the Moon, Earth-centered
  (`?exhibit=earth`). Chosen over shells alone, Earth-plus-Moon without
  shells, and Sun-plus-Earth's-orbit (which is L-294, not this).
  The Moon costs almost nothing: its served entry is already analytic,
  parent Earth, parent-relative, and its `features` dict is EMPTY, so
  it is one extra name in the driver's `objects` list. Tony's reason
  for the pairing: the Hill sphere is not decoration beside the Moon,
  it is the answer to why the Moon is bound.
- **Arrival frame: the edge is LOW EARTH ORBIT**, 8,371 km from centre
  (1.3125 equatorial radii). Half-range 1.1x that = 9,208 km = 1.4437
  radii = 6.155e-5 AU, which is Earth's floor constant, the analogue of
  `SUN_HALF_RANGE_AU`. Eight shells lit: inner core, outer core, lower
  mantle, upper mantle, crust, lower atmosphere, upper atmosphere, LEO.
  Tony's framing was "what we see from the ISS", and the station at
  about 400 km sits inside that frame.
- **Also ON at arrival:** Earth's axis and equator plane (the 23.4
  degree tilt reads at the surface; both poles are already in
  `idealized_orbits.py::planet_poles`, IAU 2018) and the Sun's
  direction.
- **Everything else in the drawer, unselected**, outward: Van Allen
  inner (1.5), Van Allen outer (4.5), geostationary belt (6.62),
  magnetosphere (10 sunward), bow shock (15 standoff), magnetotail (100
  as drawn), Earth-Moon L1-L5 (about 51-70), the Moon (about 60),
  exosphere (100), Hill sphere (235).
- **Four features added during the round.** (1) THE SUN'S DIRECTION is
  not optional: the orrery's magnetosphere is compressed 10 radii
  sunward with a tail and a conic bow shock and is rotated by
  `rotate_to_sunward`, so the exhibit must know where the Sun is. (2)
  THE AXIS AND EQUATOR -- Earth's served entry has no `orientation`
  block while the Sun's does. (3) LAGRANGE POINTS, by Tony's frame
  rule: a Lagrange point belongs to the frame that defines it, so
  Earth-Moon L1-L5 go here and Sun-Earth L1-L5 wait for L-294. (4)
  EXOSPHERE / GEOCORONA at 100 radii -- see L-292.
- **Sunlight is GEOMETRY, not a lighting model** (ruled). No shading:
  every shell in the gallery is a uniform-colour point cloud, shading
  Earth alone breaks one-chrome-many-rooms, and lighting is a rendering
  effect with nothing to source. Instead the terminator drawn as the
  great circle on the crust perpendicular to the Sun direction, plus a
  subsolar point marker carrying the hover. The hover SAYS the scene is
  a single epoch and the terminator is frozen -- the axis beside it
  implies a rotation the scene does not show.
- **The Moon's orbit, and a finding worth keeping.** Its osculating
  elements are served fresh (centre Earth, a = 0.0025481 AU, e =
  0.0339, i = 5.267 deg, epoch JD 2461289.5) but its measured trust
  window is 3.37 DAYS against Earth's 365.4 -- its node and apsides
  precess about a hundred times faster. NOTHING IN THE SERVING PATH
  ENFORCES THAT: `resolver.py` gates on the cache's global
  `served_window`, which is built only from objects whose
  `canonical_frame` is heliocentric, and the Moon is parent-relative,
  so it is not a participant. Its window is measured, recorded and read
  by nothing outside the builder's own offline test. The Sun exhibit
  never met this because it draws no orbits at all; Earth is the first
  exhibit to exercise the assembler's propagation path.
- **What the number bounds is the MARKER, not the ellipse**
  (`render_orbits.py` keeps orbit SHAPE and position MARKER as separate
  jobs). Tony's correction, and it stands: in the orrery each
  osculating ellipse is clean, and the perturbation shows as the SPREAD
  between ellipses fetched at different dates. RULING: full ellipse
  drawn faint, the arc within the trust window drawn brighter around
  the marker -- emphasis, not truncation, so it never claims the
  ellipse stops. No builder change.
- **The magnetosphere's four traces SPLIT into four drawer rows.** The
  orrery emits magnetosphere, bow shock, inner belt and outer belt from
  one call; the belts are trapped particles and the magnetopause is the
  solar wind meeting the field, and at 1.5 and 4.5 radii the belts sit
  far inside a magnetosphere starting at 10. Tony's note on why the
  grouping existed: LEGEND ECONOMY in the orrery, where rows are
  scarce. The exhibit has a scrolling drawer, so that pressure is gone
  -- and the general point is worth carrying, that groupings inherited
  from the orrery may be solving a constraint the exhibit does not
  have.
- **Provenance: the SCANNER IS NOT THE MECHANISM here.** It is the
  orrery's tool and the assembler does not pass through it. The check
  is the live store-drift run following `orrery_constant` pointers into
  `constants_new.py` at orrery HEAD, MATCH by name. In the store today:
  Earth's equatorial, polar and mean radii, the four interior
  boundaries (the L-249 conversion), `MOON_RADIUS_KM`, and both poles.
  Everything else is a typed literal in `earth_visualization_shells.py`.
  The closure plan SORTS BEFORE SOURCING: about six are DERIVED (crust
  = the radius; the atmosphere tops and LEO edges from altitudes
  already sourced in the hover text; geostationary from GM and the
  sidereal day; the Hill sphere from the masses and the semi-major
  axis); FIVE need a citation (both Van Allen distances, the
  magnetopause standoff, the bow shock standoff -- half done, the code
  line already carries a note -- and the geocorona, done, see L-292);
  the rest are DECLARED (belt thickness, tail radii, tail length,
  opacities, point counts). Order: one patch to `constants_new.py` with
  sources inline, scanner clean on the build path, push; then one patch
  to the gallery's `objects_config.json` adding the pointers; then the
  live run reads them back MATCH by name.
- **The magnetotail's 100 radii is RECLASSIFIED as DECLARED.** The real
  tail runs well past 1,000; 100 is a drawing choice wearing a
  physical-looking number, the same shape as the streamer belt's warp
  amplitude. The hover says the tail is drawn truncated.
- **Tony-action (do), BLOCKING THE BUILD:** install the
  `interactive-exhibit` skill to the account (Settings > Skills). The
  repo copy at `skills/interactive-exhibit/SKILL.md` reads 1.0 and
  matches the manifest; the design session READ it from the repo and
  could not LOAD it. Per Stale Skill = Stop, the building session
  confirms its loaded copy reads 1.0 first.
- **Still open, both downstream of the build:** the i-panel copy per
  feature with sources inline (writing, not design), and the `sun*`
  chrome renaming under the skill's One Chrome, Many Rooms rule -- grep
  `interactive.html` for `sun` inside the shared pieces and decide,
  piece by piece, rename / parametrize / leave.
- **Note:** RICE 4/4/80/3 -> 4.3 proposed, not confirmed.
**Gap:** the skill install; then the served-data work (step 2), the
build (step 3), and Mode 5 on the phone. Closes on Tony's eyes.
**Ref:** `documentation/PREDESIGN_earth_exhibit_20260906.md` (gallery),
L-292 (shells the orrery does not draw), L-293 (lunar standstill),
L-294 (the Explorer room and the heliocentric view), L-295 (the upper
atmosphere finding), L-249 (the interior constants conversion), L-289
(the HUD this exhibit inherits), skills/interactive-exhibit/SKILL.md.

#### [L-292] Earth shells the orrery does not draw
<!-- L:292 status:OPEN upd:2026-09-06 section:A flag: rice:3/3/75/2 -->
- **Opened 2026-09-06** during the Earth design round. One row per The
  Braid: the class is "Earth shells worth adding to the orrery", not
  one item per shell.
- **EXOSPHERE / GEOCORONA -- needed by L-291, so this one is not
  optional.** Earth has no exosphere shell today; it is folded into the
  "upper atmosphere" shell at 1.25 radii, while Mercury gets its own.
  SOURCED: the hydrogen geocorona was mapped by SWAN/SOHO Lyman-alpha
  to at least 100 Earth radii, past the earlier LAICA result of about
  50, and enclosing the Moon's orbit at about 60 -- Baliukin, Bertaux,
  Quemerais, Izmodenov and Schmidt (2019), J. Geophys. Res. Space
  Physics 124, 861-885, doi:10.1029/2018JA026136. The Moon flies
  through Earth's atmosphere.
- It earns the Sun direction a second time: solar radiation pressure
  compresses the exosphere into a DAYSIDE BULGE. Same sunward asymmetry
  as the magnetosphere, a completely different mechanism -- solar wind
  versus photon pressure. Drawn together they read as a pair.
- **MEO / GPS shell** at about 4.2 radii, inside the outer Van Allen
  belt; the overlap is the teaching point, since the constellation
  lives in the radiation. Not rendered by L-291, so nothing points at
  it and store drift will not check it -- harmless to add and park.
- **EARTH ROCHE LIMIT.** The Sun has one; Earth has none.
- **Note:** RICE 3/3/75/2 -> 3.4 proposed, not confirmed. The exosphere
  half is on L-291's critical path; the other two are not and should
  not be allowed to gate it.
**Gap:** the exosphere shell, with its constant in `constants_new.py`;
the other two when a build already has the file open.
**Ref:** L-291, L-295, earth_visualization_shells.py,
mercury_visualization_shells.py (the exosphere precedent).

#### [L-293] Lunar standstill: an exhibit made of four dated orbits
<!-- L:293 status:OPEN upd:2026-09-06 section:A flag: rice:3/4/60/3 -->
- **Opened 2026-09-06**, split out of the Earth design round so it does
  not become a drawer row nobody opens. Four osculating orbits at
  today, one month, one year and 9.3 years, fanning wider and wider.
  The progression IS the exhibit.
- **Why those intervals.** The Moon's orbit is nearly circular (served
  e = 0.034), so the swing of its long axis is almost invisible; what
  separates two drawn ellipses is the drift of the TILT direction,
  which goes all the way round in 18.6 years. Two orbits 9.3 years
  apart are therefore tipped opposite ways -- the widest gap the Moon
  can show. That cycle is the LUNAR STANDSTILL, watched from stone
  circles and canyon walls for four thousand years before anyone could
  say why. That is the exhibit's subject, not element drift.
- **The precedent already exists in the orrery.** With apsidal markers
  on, it resolves a comet's perihelion time, fetches the elements AT
  that moment, and draws that conic as a white dotted arc beside the
  conic for the plot date (`plot_perihelion_osculating_orbit`, called
  from palomas_orrery.py Capability D). Two orbits from two instants,
  each chosen because it means something. Tony's observation, and it is
  what turned this from a caveat into an exhibit.
- **Tony-action (decide), later:** whether this is a room in
  `interactive.html` or a curated card. Four orbits and a story may not
  need a drawer, a nav cluster and an i-panel. Decide when it is sized.
- **THE FOUR INTERVALS ARE PICKED BY LOOKING, NOT DECIDED HERE.** The
  19 and 41 degrees per year quoted in conversation came from the
  standard cycle lengths (18.6 and 8.85 years), NOT from a source
  checked that session. There is also a monthly wobble from the Sun's
  pull that may or may not swamp a one-month pair. The orrery fetches
  elements at any date, so this is an evening's looking, not a debate.
- **Builder cost:** the served cache holds ONE osculating block per
  object per nightly build. This needs several, at chosen epochs --
  gallery-cache-builder territory, and the reason it is its own item
  rather than part of L-291.
- **Note:** RICE 3/4/60/3 -> 2.4 proposed, not confirmed. Low score,
  high interest; it is a candidate for bundling under the plan's
  SEQUENCING authority rather than being run by RICE order.
**Gap:** measure the four intervals against real elements; then decide
room-or-card; then the builder work.
**Ref:** L-291 (where it came from), Halley and Encke (better versions
of the same picture), palomas_orrery.py Capability D,
idealized_orbits.py::plot_perihelion_osculating_orbit.

#### [L-294] The Explorer room's placeholder, and Earth's heliocentric view
<!-- L:294 status:OPEN upd:2026-09-06 section:A flag: rice:3/3/70/2 -->
- **Opened 2026-09-06.** Tony's question from the Mode 5 pass: should
  the Explorer view carry the home interactive URL at all, since it
  will eventually be replaced by a real solar-system interactive?
- **Two things now wait on this**, which is why it stops being a loose
  end. The Sun-Earth Lagrange points L1-L5 (Horizons 31-35) belong to a
  heliocentric frame by Tony's frame rule, so they are held here rather
  than drawn in the Earth room. And whether the EXPLORER gets the Sun's
  frame HUD -- Tony's answer at Mode 5 was "unclear" -- is really a
  question about what the Explorer is going to become.
- **The Hill sphere pairing rides here too.** Sun-Earth L1 and L2 sit
  at about 235 Earth radii, the same distance as Earth's Hill sphere,
  and that is not a coincidence -- it is the same balance point
  measured two ways. The Hill sphere is Earth's feature either way, so
  the same served entry serves both rooms and L1/L2 sit on its surface
  where the Sun-Earth line crosses. Scale note: at whole-orbit scale
  the Hill sphere is about half a percent of the frame, so the pairing
  only reads after a frame zoom onto Earth.
- **Note:** RICE 3/3/70/2 -> 3.2 proposed, not confirmed. Lagrange
  points do not travel on Keplerian orbits about their primary, so they
  need serving as MARKERS at the epoch rather than as orbits -- a
  different builder path from Earth and the Moon. Distances above are
  RECALLED, not checked; verify against Horizons before drawing.
- **Tony-action (decide):** what the Explorer room becomes, and whether
  the placeholder URL stays until then.
**Gap:** Tony's ruling on the Explorer; then the heliocentric view, and
the Sun-Earth Lagrange points with it.
**Ref:** L-291 (the frame rule that sent them here), L-289 (the HUD
question carried out of it), L-286 (rooms), interactive.html.

#### [L-295] The upper atmosphere shell disagrees with its own hover text
<!-- L:295 status:OPEN upd:2026-09-06 section:A flag: rice:2/2/90/1 -->
- **Found 2026-09-06** while inventorying Earth's shells for L-291.
  `create_earth_upper_atmosphere_shell` draws at `radius_fraction` 1.25,
  which is about 1,595 km altitude. Its own hover text says the upper
  atmosphere "extends from 50 km to about 1,000 km altitude". Those
  disagree by a factor of about 1.6.
- Which one is wrong is not settled here. The 1.25 may be a drawing
  choice that outran its caption, or the caption may be the stale half.
  Either way one of them is telling a visitor something the other
  contradicts, and both are on the page.
- **Note:** RICE 2/2/90/1 -> 3.6 proposed, not confirmed. Cheap, and it
  sits in a file L-291 and L-292 will both have open -- a Cluster the
  Tail candidate rather than a separate errand.
**Gap:** decide which number is right, fix the other, source the one
that survives.
**Ref:** L-291, L-292, earth_visualization_shells.py.

#### [L-296] Every design build earns a master plan version number
<!-- L:296 status:PENDING-GATE upd:2026-09-06 section:A flag: rice:3/3/90/1 -->
- **Tony's ruling, 2026-09-06:** "I think every design build earns a
  version number. I don't archive each version but replace them. I only
  keep each version of the protocol." Given when the Earth design round
  closed and Claude asked whether it counted as a restamp juncture.
- **What it sharpens.** `ledger-and-session-records` 1.9 says the plan
  "restamps at key junctures rather than at every change, because a
  juncture is its unit." A juncture is not countable, so the rule could
  not be applied without a judgment call every time -- and the call kept
  landing on Tony. A DESIGN BUILD is countable. Same rule, mechanical
  now.
- **The archiving half is the other half.** Master plan versions are
  REPLACED, not archived; only the protocol keeps a versioned copy per
  version. Git holds the superseded bytes either way, so nothing is
  lost, and it explains why the plan's own rolling stamp keeps three
  entries and simply drops the fourth rather than pushing it down into
  a history file the way the protocol does.
- **Applied immediately:** the plan went v25 -> v26 in this session's
  patch, with the Earth design round as the build that earned it, and
  the stale "the phone pass is the one thing carried" sentence in the
  Status block corrected in the same edit.
- **VERSION COLLISION, RULED AND DISCHARGED.** This ruling and L-290's
  relay-anchor amendment both belonged in
  `ledger-and-session-records`, and both wanted 1.10. Tony,
  2026-09-06: **"one session - one bump."** A session does not ship two
  versions of one skill; everything it decides rides one version. Both
  amendments went into a single 1.10 in the same commit. The rule is
  written into the skill's own Protocol and Skills Change Log section,
  since it governs every future bump and not just this one.
- **Note:** RICE 3/3/90/1 -> 8.1 proposed, not confirmed. High because
  the effort is one skill paragraph and the reach is every future plan
  update.
- **Same verification obligation as L-290:** the 1.10 install cannot be
  confirmed from inside the session that made it, so this is
  PENDING-GATE until the next session's load reads 1.10.
**Gap:** rides L-290's gate -- `skills_index.py`, the reinstall, the
push, then the next session's load.
**Ref:** L-290 (the same 1.10 bump), L-291 (the design build that
earned v26), skills/ledger-and-session-records/SKILL.md,
documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md.

"""


# --------------------------------------------------------------------
# Master plan: one appended "you are here" subsection
# --------------------------------------------------------------------

PLAN_OLD = """### What this section deliberately does not carry
"""

PLAN_NEW = """### 2026-09-06 (evening) -- the Sun's axis question closes, and Earth
is designed

Measured at orrery `50cbd2df` and gallery `90615b9f`, both confirmed
against the live remotes. Appended, not merged.

**The Sun's chrome is finished.** L-289 is CLOSED on Tony's Mode 5.
Patch 4 passed all five trials on the phone in both orientations, and
then the triad turned out to read as 90 degrees off the grid while
being provably correct -- an orthographic triad beside a perspective
box, with every axis title empty and the grid uniform white, so nothing
in the render could corroborate it. Two more rounds fixed that: box
edges coloured per axis (right on desktop, off the sides of a portrait
frame on the phone), then three coloured lines through the origin.
Tony: "This works. It's a bit unusual but it is correct and one can't
make a mistake!" That is three Mode 5 rounds on one piece of chrome,
and none of the three failures was visible headless.

**Earth is designed, zero code.** The full record is
`documentation/PREDESIGN_earth_exhibit_20260906.md` in the gallery
repo; L-291 is the handle. The exhibit is Earth's shells plus the
Moon, arriving at LOW EARTH ORBIT -- Tony's framing was "what we see
from the ISS" -- with eight shells lit and everything from the Van
Allen belts outward waiting in the drawer. Four things were added
during the round: the Sun's direction (not optional, since the
magnetosphere is compressed sunward and rotated to face it), the axis
and equator, Earth-Moon Lagrange points, and an exosphere shell that
does not exist yet.

**Two rulings from that round worth carrying into every later exhibit.**
A Lagrange point belongs to the FRAME THAT DEFINES IT -- so Earth-Moon
here and Sun-Earth held for a heliocentric view, one rule with no
case-by-case exceptions. And sunlight is GEOMETRY, not a lighting
model: the terminator is a great circle perpendicular to the Sun
direction, computed rather than shaded, because a shading model on
Earth alone would break one-chrome-many-rooms and would be a rendering
effect with nothing to source.

**What the round found that nobody was looking for.** The Moon's
osculating elements carry a measured trust window of 3.37 days against
Earth's 365, and NOTHING IN THE SERVING PATH ENFORCES IT -- the
resolver gates on the cache's global served_window, which is built only
from heliocentric objects, and the Moon is parent-relative. The Sun
exhibit never met this because it draws no orbits at all. Earth is the
first exhibit to exercise the assembler's propagation path, and that is
a property of step 3 the plan had not named.

**A backlog item became an exhibit.** Tony's question about why one
year rather than one lunar month led to the lunar standstill: the
Moon's orbit is nearly circular, so what separates two drawn ellipses
is the drift of the tilt direction, which comes full circle in 18.6
years. Four dated orbits fanning apart is a room of its own (L-293),
and the orrery already does the same trick for comets at perihelion.

**What this does to the order.** Nothing moves. Step 3, Earth into the
assembler, has had its design conversation and is now blocked on ONE
Tony-action: installing the `interactive-exhibit` skill to the account,
since a session can read the repo copy but cannot load it. Step 2's
remaining item (L-286's rooms page) is unchanged.

### What this section deliberately does not carry
"""


PLAN_STATUS_OLD = """**Status:** v25 -- Phase 2 (solar system assembler) BUILD UNDERWAY;
**the first feature-bearing exhibit is LIVE.** The Sun ships at
`palomasorrery.com/interactive.html?exhibit=sun`, unlinked from the
landing page, Mode 5 accepted 2026-08-29 (gallery `ac9a5c7b`). Its GUI
(L-267) is complete on desktop as of 2026-09-03 (gallery `98cc99bd`): a
drawer replaces the legend, cross markers and rows move the camera, and
the i panel follows the focus and carries each shell's curated link
(L-265, DONE). The phone pass is the one thing carried.
"""

PLAN_STATUS_NEW = """**Status:** v26 -- Phase 2 (solar system assembler) BUILD UNDERWAY;
**the first feature-bearing exhibit is LIVE AND COMPLETE.** The Sun
ships at `palomasorrery.com/interactive.html?exhibit=sun`, unlinked
from the landing page, Mode 5 accepted 2026-08-29 (gallery
`ac9a5c7b`). Its GUI (L-267) is complete on desktop as of 2026-09-03
(gallery `98cc99bd`): a drawer replaces the legend, cross markers and
rows move the camera, and the i panel follows the focus and carries
each shell's curated link (L-265, DONE). The phone pass is DONE as of
2026-09-06, and the frame HUD with it (L-289, closed on Tony's Mode
5). **The second exhibit, EARTH, is DESIGNED AND NOT BUILT** (L-291):
shells plus the Moon, arriving at low Earth orbit, blocked only on the
`interactive-exhibit` skill install.
"""

PLAN_STAMP_OLD = """**Last updated:** September 6, 2026 (v25: Section 5a gains the
2026-09-06 subsection -- the phone passed the lobby and the sweep and
failed the edge labels, rebuilt as the frame HUD; the order unchanged;
Earth opens as a design conversation next; with Anthropic's Claude
Fable 5.1. v24, September 5, 2026: the 2026-09-05 subsection -- L-287
live; lobby, 2D sweep and twelve-edge labels built and render-gated.
v23, September 4, 2026: step 2 realigned from the hall to the lobby,
rooms and editor -- L-280 retired, L-282 rewritten, L-286 and L-287
opened.)
"""

PLAN_STAMP_NEW = """**Last updated:** September 6, 2026 (v26: the EARTH exhibit designed in
a zero-code round -- shells plus the Moon, arriving at low Earth orbit;
a Lagrange point belongs to the frame that defines it; sunlight is
geometry, not a lighting model; the Moon's 3.37-day trust window found
unenforced; L-289 closed and the Sun's chrome finished; Section 5a
gains the 2026-09-06 evening subsection; with Anthropic's Claude Opus
5. v25, September 6, 2026: Section 5a gains the 2026-09-06 subsection
-- the phone passed the lobby and the sweep and failed the edge labels,
rebuilt as the frame HUD; the order unchanged; Earth opens as a design
conversation next; with Anthropic's Claude Fable 5.1. v24, September 5,
2026: the 2026-09-05 subsection -- L-287 live; lobby, 2D sweep and
twelve-edge labels built and render-gated.)
"""


L290_META_OLD = ("<!-- L:290 status:OPEN upd:2026-09-06 section:A flag: "
                 "rice:4/3/90/1 -->")
L290_META_NEW = ("<!-- L:290 status:PENDING-GATE upd:2026-09-06 section:A "
                 "flag: rice:4/3/90/1 -->")

L290_ADD_OLD = """- **Tony-action (decide):** accept, amend or decline the two drafts.
**Gap:** Tony's ruling; then the protocol edit, the skill bump, the
reinstall, and the manifest regeneration, in one push.
"""

L290_ADD_NEW = """- **What v3.53 ALREADY covered, checked at orrery `50cbd2df`
  2026-09-06**, which is what narrowed the amendment to the real gap:
  HOW each partner reads the repo was already written under AI Roles
  from L-276 (Claude and GPT fetch live at a pinned SHA; Gemini's web
  app imports one public repo as a snapshot of HEAD, cannot read a URL
  given in a prompt, cannot fetch at a SHA, cannot see commit history,
  and is not on mobile). The "Documents as handoffs" clause already
  required `built on <SHA> at <URL>` on every outbound document, with a
  reason covering both kinds of partner, and the Anchor Requirement
  gate already applied it uniformly. THE GAP WAS NARROWER THAN
  "anchors": none of it named `PROJECT_INSTRUCTIONS.md` or the
  task-relevant `SKILL.md` files as fetch targets, so a partner got the
  code with none of the governance and read what was built without the
  rules the build ran under.
- **Tony's ruling 2026-09-06: ACCEPT both drafts, with three
  amendments.** His reason for doing it now rather than deferring:
  work is moving between Opus, Fable and GPT under credit limits, so
  the relay discipline is load-bearing exactly when the flexibility is
  needed.
  1. **The Gemini bullet carried a factual error.** The draft said no
     SHA pin is possible for the protocol or skills "any more than it
     is for the code", so paste excerpts inline. But
     `PROJECT_INSTRUCTIONS.md` and `skills/` LIVE IN the orrery repo:
     if Gemini imported that repo it already HAS both files, just
     unpinnable, fixed to whenever the import happened. The real
     pasting case is the one the draft was describing without knowing
     it -- Gemini imports ONE repository, so a gallery import leaves it
     with no protocol and no skills at all, because they are in the
     other repo. The corrected bullet splits by WHICH REPO WAS
     IMPORTED, not by whether Gemini can fetch.
  2. **Name the skills by what the TASK fires**, not "the specific
     files" -- the same judgment the resident protocol already asks for
     under "Relevant skill unfired -> Load it by name".
  3. **Ask the partner to state back which rule files it actually
     read.** A return document that does not name them is telling you
     it did not read them. This is the only part of the mechanism that
     can FAIL VISIBLY; without it nothing can (A Check That Cannot Fail
     Is Not Passing).
- **Applied 2026-09-06 in one commit, per the four-step binding rule:**
  the protocol's "Documents as handoffs" bullet extended (v3.54);
  `ledger-and-session-records` 1.9 -> 1.10 with the two-form template
  in its Anchor Requirement section; `skills_index.py` regenerates the
  manifest row; one commit. The bump also carries L-296 -- see below.
- **Tony-action (do):** run `skills_index.py`, then REINSTALL
  `ledger-and-session-records` to the account (Settings > Skills), then
  commit and push. The reinstall is the step with no artifact prompting
  it.
- **THIS BUMP CANNOT BE VERIFIED FROM INSIDE THE SESSION THAT MADE IT.**
  A skill lives in three stores and the account install is the copy
  Claude actually loads; a reinstall is invisible to the running
  conversation. So: `ledger-and-session-records` went to 1.10 at the
  SHA this session pushes, the session that bumped it had loaded 1.9,
  and THE NEXT SESSION CONFIRMS ITS LOADED COPY READS 1.10 BEFORE DOING
  LEDGER WORK. Status is PENDING-GATE, not DONE, because that is what
  the state honestly is.
**Gap:** `skills_index.py`, the reinstall, the push; then the next
session's load confirms 1.10 and this closes.
"""



# --------------------------------------------------------------------
# skills/ledger-and-session-records/SKILL.md  ->  1.10
# --------------------------------------------------------------------

SKILL_VER_OLD = """Skill version: 1.9 | Cut from palomas_orrery @ 41c0b279 (v1.9), earlier
@ 3586970d (v1.8), @ 434a712b (v1.7), @ 305b269 (v1.6), @ 3398970
(v1.5) | August 23, 2026, with Anthropic's Claude Opus 5
"""

SKILL_VER_NEW = """Skill version: 1.10 | Cut from palomas_orrery @ 50cbd2df (v1.10),
earlier @ 41c0b279 (v1.9), @ 3586970d (v1.8), @ 434a712b (v1.7),
@ 305b269 (v1.6), @ 3398970 (v1.5) | September 6, 2026, with
Anthropic's Claude Opus 5
"""

SKILL_HIST_OLD = """in the ledger appendix five days after v3.41 replaced that appendix
with a pointer.
"""

SKILL_HIST_NEW = """in the ledger appendix five days after v3.41 replaced that appendix
with a pointer. v1.10 carries THREE changes from one session
(2026-09-06), which is itself the first of them. ONE SESSION, ONE BUMP
(L-296): a session does not ship two versions of one skill, so
everything it decides rides one version. The SECOND ANCHOR LINE for
relay partners with no resident layer (L-290), in the Anchor
Requirement section, with two forms and a read-back. And the master
plan restamps once per DESIGN BUILD (L-296) rather than at "key
junctures", which was not countable and so kept returning the judgment
to Tony.
"""

SKILL_PLAN_OLD = """restamps at key junctures rather than at every change, because a
juncture is its unit; stepwise updating is the ledger's job. That
cadence is not staleness to be corrected by restamping more often.
"""

SKILL_PLAN_NEW = """restamps once per DESIGN BUILD; stepwise updating is the ledger's job.
That is Tony's ruling of 2026-09-06 (L-296), replacing "at key
junctures": a juncture is not countable, so the rule could not be
applied without a judgment call every time, and the call kept landing
on Tony. A design build is countable. Versions are REPLACED, not
archived -- only the PROTOCOL keeps a versioned copy per version -- and
git holds the superseded bytes either way, which is why the plan's own
rolling stamp keeps three entries and simply drops the fourth instead
of pushing it down into a history file. That cadence is not staleness
to be corrected by restamping more often.
"""

SKILL_ANCHOR_OLD = """This is the document-layer form of the protocol's SHA Round Trip
CRITICAL gate -- applies uniformly regardless of document type or
audience.
"""

SKILL_ANCHOR_NEW = """This is the document-layer form of the protocol's SHA Round Trip
CRITICAL gate -- applies uniformly regardless of document type or
audience.

**A document leaving this Project needs a SECOND anchor line** when the
receiving partner has no resident protocol and no installed skills --
true for GPT, Gemini, and any Claude session outside this account and
Project (L-290). The code anchor says WHICH BYTES to read; this one
says WHAT RULES the work runs under. Without it a partner operates on
the code with none of the conventions governing how the work is done.

NAME THE SKILLS THE TASK FIRES, not a blanket list. Same judgment the
resident protocol already asks for under "Relevant skill unfired ->
Load it by name": a provenance review needs provenance-discipline, a
patch needs safe-file-editing, and sending all ten teaches the partner
to skim.

The wording depends on what the partner can actually do:

- **Claude or GPT (fetch-capable).** Name the files as fetch targets at
  the same pinned SHA: "also fetch PROJECT_INSTRUCTIONS.md and
  skills/<name>/SKILL.md at <SHA>." These partners pull the exact bytes
  the way they pull code -- L-191 records Fable running `git ls-remote`
  against a pinned SHA and parsing the source.
- **Gemini (snapshot-only, L-276).** Split by WHICH REPO WAS IMPORTED,
  not by whether it can fetch. `PROJECT_INSTRUCTIONS.md` and `skills/`
  live IN the orrery repo, so a Gemini that imported the orrery ALREADY
  HAS both -- unpinnable, fixed to whenever the import happened, but
  present. Name the import state and point at the paths: "operating
  from an orrery snapshot imported [date]; the protocol and skills are
  in that snapshot at `PROJECT_INSTRUCTIONS.md` and `skills/`."
  Gemini imports ONE repository, so a GALLERY import leaves it with no
  protocol and no skills at all -- they are in the other repo. THAT is
  the paste case: state the limitation and put the relevant excerpt in
  the document itself rather than pointing at a path.

**ASK FOR THE READ-BACK.** The outbound document asks the partner to
state which rule files it actually read. A return document that does
not name them is telling you it did not read them. This is the only
part of the mechanism that can FAIL VISIBLY; the anchor line itself
cannot, because a document that omits it looks exactly like one that
did not need it (A Check That Cannot Fail Is Not Passing).

Either way the requirement is the one above, one layer up: an
un-anchored document does not say what it describes, and for a partner
with no resident layer, "what it describes" includes the rules and not
only the code.

(Origin, 2026-09-06: a parallel Claude Sonnet session, outside this
account and Project, reached a correct conclusion and then proposed a
handle already taken and offered a ledger entry "ready to paste" --
both exactly the failures this rule prevents. It had the code and none
of the ledger skill's delivery rules. Tony ruled it in the same
session, his reason being that work now moves between Opus, Fable and
GPT under credit limits, so the relay discipline is load-bearing
precisely when the flexibility is wanted.)
"""

SKILL_BUMP_OLD = """Do not leave any of it to a later checkpoint someone has to remember.
"""

SKILL_BUMP_NEW = """Do not leave any of it to a later checkpoint someone has to remember.

**ONE SESSION, ONE BUMP [QUALITY].** A session does not ship two
versions of one skill. Everything a session decides about a given skill
rides a SINGLE version number, in a single commit, under the four steps
above. Two amendments arriving the same evening do not become 1.10 and
1.11; they become one 1.10 carrying both. (Tony's ruling, 2026-09-06,
when L-290's relay-anchor amendment and L-296's plan-version rule both
wanted 1.10. Each bump costs a protocol history entry, a manifest
regeneration and a reinstall, so splitting them multiplies the
ceremony and the chances of step 3 not firing -- and it makes the
version history harder to read, since two entries then describe one
evening.)
"""


# --------------------------------------------------------------------
# PROJECT_INSTRUCTIONS.md  ->  v3.54
# --------------------------------------------------------------------

PROTO_HDR_OLD = """Tony Quintanilla, PE | Claude | v3.53 | September 3, 2026

Cut from faac433f at https://github.com/tonylquintanilla/palomas_orrery
"""

PROTO_HDR_NEW = """Tony Quintanilla, PE | Claude | v3.54 | September 6, 2026

Cut from 50cbd2df at https://github.com/tonylquintanilla/palomas_orrery
"""

PROTO_MODE7_OLD = """- Documents as handoffs: Copy/paste AI responses to share context --
  every outbound document (audit prompt, review request, relay
  manifest) opens with built on <SHA> at <URL>, same as a handoff.
  The repo moves, so an un-anchored document does not say which
  state it describes. A partner that can fetch needs the anchor to
  fetch the right bytes; a partner that cannot needs it to know what
  it is reading.
"""

PROTO_MODE7_NEW = """- Documents as handoffs: Copy/paste AI responses to share context --
  every outbound document (audit prompt, review request, relay
  manifest) opens with built on <SHA> at <URL>, same as a handoff.
  The repo moves, so an un-anchored document does not say which
  state it describes. A partner that can fetch needs the anchor to
  fetch the right bytes; a partner that cannot needs it to know what
  it is reading.
  A partner without resident access to this Project -- GPT, Gemini,
  or a Claude instance outside it -- also has no PROJECT_INSTRUCTIONS.md
  and no installed skills. The anchor for such a document names those
  as fetch targets too, not just the code repo, or the partner
  operates on the code with none of the conventions governing how the
  work is done. Name the SKILLS THE TASK FIRES, not a blanket list,
  and ask the partner to state back which rule files it actually read
  -- a return document that does not name them is telling you it did
  not read them, and that read-back is the only part of this that can
  fail visibly. Wording differs by what the partner can do with a SHA;
  ledger-and-session-records carries the two forms. (L-290.)
"""

PROTO_HIST_OLD = """v3.53 (September 3, 2026): One clause corrected, one note added. No
skill changed.
"""

PROTO_HIST_NEW = """v3.54 (September 6, 2026): One clause extended, one skill bumped
carrying three changes, and a design round that produced no code.

THE RELAY ANCHOR NOW NAMES THE RULES, NOT ONLY THE CODE (L-290).
"Documents as handoffs" already required built on <SHA> at <URL> on
every outbound document, and v3.53 had just corrected its reason to
cover partners that can fetch and partners that cannot. What neither
said was that PROJECT_INSTRUCTIONS.md and the task-relevant SKILL.md
files are fetch targets too. So a relay partner got the code with none
of the governance and worked on it without the rules the work runs
under.

The failure that earned it is small and exact. A parallel Claude
Sonnet session, outside this account and Project, reasoned correctly
to the right conclusion -- and then proposed a ledger handle that was
already taken and offered its entry "ready to paste", which the ledger
skill rules out. It had the repo. It did not have the ledger skill or
the live handle count, and nothing in the document it was given told
it where to look.

Two amendments beyond the drafts, both Tony's. The skills named are
the ones THE TASK FIRES, not a blanket list, because sending all ten
teaches a partner to skim. And the document ASKS FOR A READ-BACK: the
partner states which rule files it actually read, because a return
that does not name them is telling you it did not read them. That
read-back is the only part of the mechanism that can fail visibly --
an omitted anchor line looks exactly like one that was not needed.

One correction to the draft, and it is the kind this project keeps
finding. The Gemini bullet said no SHA pin is possible for the
protocol or skills "any more than it is for the code", so paste them
inline. But those files LIVE IN the orrery repo: a Gemini that
imported the orrery already HAS them, unpinnable but present. Gemini
imports ONE repository (v3.53's own note, L-276), so the real paste
case is a GALLERY import, which leaves it with no protocol and no
skills at all because they are in the other repo. The rule now splits
by which repo was imported.

ledger-and-session-records 1.9 -> 1.10, carrying three things.
The anchor amendment above; ONE SESSION, ONE BUMP -- a session does
not ship two versions of one skill, so everything it decides rides a
single version (Tony's ruling when this amendment and L-296 both
wanted 1.10); and the master plan restamps once per DESIGN BUILD
rather than at "key junctures", which was not countable and so kept
sending the judgment back to Tony.

The Earth exhibit was designed the same evening in a zero-code round
(L-291) and the Sun's chrome closed (L-289). Neither changed a rule
here. Record:
documentation/PREDESIGN_earth_exhibit_20260906.md in the gallery repo.

One obligation this bump cannot discharge from inside the session that
made it. A skill lives in three stores, and the account install is the
copy Claude actually loads; a reinstall is invisible to the running
conversation. So: ledger-and-session-records went to 1.10 at
`50cbd2df`, the session that bumped it had loaded 1.9, and the next
session confirms its loaded copy reads 1.10 before doing ledger work.

Version history: v3.51 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

v3.53 (September 3, 2026): One clause corrected, one note added. No
skill changed.
"""


# --------------------------------------------------------------------
# The v3.51 block leaves the protocol and lands in the history file
# --------------------------------------------------------------------

V351_BLOCK = """v3.51 (August 31, 2026): No rule changed in this document. One skill
bump, and the end of a habit nobody had decided on.

safe-file-editing 1.9 -> 1.10 (L-271). Git Is the Backup [QUALITY]:
patch scripts stop writing `.bak` and print the Discard Changes path
instead.

The argument is structural, which is what makes it a rule. A patch
guards on a content fingerprint and refuses when the working copy does
not match, so at the moment it writes, the file on disk is the committed
version. Git holds it. The `.bak` can never be the only copy, and the
one case where it would earn its place -- uncommitted work -- is exactly
the case the gate refuses to run in.

A stale copy is an active hazard rather than clutter. The orrery's own
.gitignore records why, from the sweep of 2026-08-29: a session grepping
for a value can hit one and read it as current, and two of the nine
swept that day were a superseded master plan and a superseded skill.

Tony's question was the whole of it -- "why do we create them at all?" --
and his correction to the rate stands with it: days, not weeks. All
eight swept from the gallery on 2026-08-31 were made in the preceding
two days. He also believed the maintenance runner cleaned them up. It
does not; the word does not appear in that file. What existed was one
manual sweep, which is how a habit gets mistaken for a mechanism.

The .gitignore rule was widened in the same commit. `*.bak` matches only
names ENDING in .bak, so `.bak1`, `.bak2` and `.bak_L271` slipped
through the 2026-08-29 sweep and kept being committed -- which is why
two close-approach cache backups survived it, and why the gallery, whose
rule was narrower still, kept all eight of its own.

One obligation this bump cannot discharge from inside the session that
made it. A skill lives in three stores, and the account install is the
copy Claude actually loads; a reinstall is invisible to the running
conversation. So: safe-file-editing went to 1.10 at `ccd1ac96`, the
session that bumped it had loaded 1.9, and the next session confirms its
loaded copy reads 1.10 before doing patch work.

Version history: v3.48 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

PROTO_DROP_OLD = V351_BLOCK

PROTO_DROP_NEW = ""

HIST_OLD = """(Moved down from the resident protocol on 2026-09-03 when v3.53
made a fourth entry.)
"""

HIST_NEW = """(Moved down from the resident protocol on 2026-09-03 when v3.53
made a fourth entry.)

""" + V351_BLOCK + """(Moved down from the resident protocol on 2026-09-06 when v3.54
made a fourth entry.)
"""


EDITS = [
    (LEDGER, L288_OLD, L288_NEW),
    (LEDGER, L289_META_OLD, L289_META_NEW),
    (LEDGER, L289_OLD, L289_NEW),
    (LEDGER, L290_META_OLD, L290_META_NEW),
    (LEDGER, L290_ADD_OLD, L290_ADD_NEW),
    (LEDGER, L290_TAIL_OLD, NEW_ITEMS),
    (PLAN, PLAN_STATUS_OLD, PLAN_STATUS_NEW),
    (PLAN, PLAN_STAMP_OLD, PLAN_STAMP_NEW),
    (PLAN, PLAN_OLD, PLAN_NEW),
    (SKILL, SKILL_VER_OLD, SKILL_VER_NEW),
    (SKILL, SKILL_HIST_OLD, SKILL_HIST_NEW),
    (SKILL, SKILL_PLAN_OLD, SKILL_PLAN_NEW),
    (SKILL, SKILL_ANCHOR_OLD, SKILL_ANCHOR_NEW),
    (SKILL, SKILL_BUMP_OLD, SKILL_BUMP_NEW),
    (PROTOCOL, PROTO_HDR_OLD, PROTO_HDR_NEW),
    (PROTOCOL, PROTO_MODE7_OLD, PROTO_MODE7_NEW),
    (PROTOCOL, PROTO_DROP_OLD, PROTO_DROP_NEW),
    (PROTOCOL, PROTO_HIST_OLD, PROTO_HIST_NEW),
    (HISTORY, HIST_OLD, HIST_NEW),
]


def fail(msg):
    print("ABORTED: %s" % msg)
    print("No file was written.")
    sys.exit(1)


def main():
    # 0. Location check.
    for path in REPO_FILES:
        if not os.path.isfile(path):
            fail("%s not found. Run this from the ORRERY repo root." % path)

    # 1. Read, normalize, fingerprint.
    original = {}
    working = {}
    for path, expected in REPO_FILES.items():
        with open(path, "rb") as fh:
            raw = fh.read()
        original[path] = raw
        text = raw.replace(b"\r\n", b"\n").decode("ascii")
        actual = hashlib.md5(text.encode("ascii")).hexdigest()
        if actual != expected:
            if SENTINEL in text:
                fail("%s already contains %s -- this patch has been run. "
                     "Nothing to do." % (path, SENTINEL))
            fail("%s fingerprint mismatch.\n  expected %s\n  actual   %s\n"
                 "  The working copy is not the committed version this "
                 "patch was written against (orrery 50cbd2df). Use GitHub "
                 "Desktop's Discard Changes, or re-cut the patch."
                 % (path, expected, actual))
        working[path] = text

    # 2. Apply every edit in memory. Each anchor must appear exactly once.
    for i, (path, old, new) in enumerate(EDITS, 1):
        count = working[path].count(old)
        if count != 1:
            fail("edit %d in %s: anchor found %d times, expected exactly 1."
                 % (i, path, count))
        working[path] = working[path].replace(old, new, 1)
        print("  edit %d ok  (%s)" % (i, path))

    # 3. ASCII gate on the result.
    for path, text in working.items():
        try:
            text.encode("ascii")
        except UnicodeEncodeError as exc:
            fail("%s: non-ASCII character introduced (%s)." % (path, exc))

    # 4. Write. Line endings restored per file as they were found.
    for path, text in working.items():
        had_crlf = b"\r\n" in original[path]
        out = text.replace("\n", "\r\n") if had_crlf else text
        with open(path, "wb") as fh:
            fh.write(out.encode("ascii"))
        print("  wrote %s (%s line endings)"
              % (path, "CRLF" if had_crlf else "LF"))

    print("")
    print("Done. 19 edits across 5 files.")
    print("")
    print("LEDGER_CONSOLIDATED.md")
    print("  L-288 updated (built, run, Mode 5 passed; Gap narrowed to the")
    print("        untested json_converter path)")
    print("  L-289 CLOSED")
    print("  L-290 RULED and APPLIED -> PENDING-GATE on the reinstall")
    print("  L-291 Earth exhibit: shells plus the Moon          [NEW]")
    print("  L-292 Earth shells the orrery does not draw        [NEW]")
    print("  L-293 Lunar standstill exhibit                     [NEW]")
    print("  L-294 Explorer placeholder / heliocentric Earth    [NEW]")
    print("  L-295 Upper atmosphere shell vs its own hover text [NEW]")
    print("  L-296 One session one bump; plan versions          [NEW]")
    print("")
    print("documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md")
    print("  v25 -> v26 in the Status block and the Last updated stamp")
    print("  the stale 'phone pass is the one thing carried' corrected")
    print("  one appended 'you are here' subsection")
    print("")
    print("skills/ledger-and-session-records/SKILL.md   1.9 -> 1.10")
    print("  second anchor line for relay partners, two forms + read-back")
    print("  one session, one bump")
    print("  the master plan restamps once per design build")
    print("")
    print("PROJECT_INSTRUCTIONS.md                     v3.53 -> v3.54")
    print("  header re-anchored to 50cbd2df")
    print("  'Documents as handoffs' extended (L-290)")
    print("  v3.54 history entry added; v3.51 moved out")
    print("")
    print("documentation/PROJECT_INSTRUCTIONS_HISTORY.md")
    print("  v3.51 received into PART 1")
    print("")
    print("NEXT, in this order:")
    print("  1. ledger_index.py    (index zone; migrates DONE L-289)")
    print("  2. skills_index.py    (manifest row -> 1.10)")
    print("  3. REINSTALL ledger-and-session-records to the account")
    print("     (Settings > Skills). This is the step with no artifact")
    print("     prompting it, and the one the binding rule says gets")
    print("     skipped.")
    print("  4. commit and push -- all of it in ONE commit.")
    print("")
    print("Then, separately: install the interactive-exhibit skill. It")
    print("blocks the Earth build, not this commit.")


if __name__ == "__main__":
    main()
