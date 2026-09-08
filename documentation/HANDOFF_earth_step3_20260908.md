# Earth Exhibit -- Handoff for Step 3 (the code)

Built on orrery `af4c604ed48540876b3165bc772411cd0dc7d0c9`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `700b426d4cecc1f80fd6f9ca5758e5058ea497a6`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Tony Quintanilla, PE | Claude Fable 5.1 | 2026-09-08
Protocol v3.54. Ledger handle: L-291. Master plan v27.

Written for the next Claude session inside this Project. A partner
without the Project reads these first, live at the SHAs above:
`PROJECT_INSTRUCTIONS.md` (orrery root) and, for this task,
`skills/interactive-exhibit/SKILL.md`, `skills/gallery-assembler/SKILL.md`,
`skills/ledger-and-session-records/SKILL.md`. State back which you read.

This is the STATE and the ORDER, not the design. The design is
`documentation/PREDESIGN_earth_exhibit_20260906.md` (gallery repo) and
it is unchanged; do not re-litigate what it settles. The build order it
was written against is `documentation/HANDOFF_earth_build_order_20260906.md`
(gallery repo); this document supersedes its steps 0-2 and points at
its steps 3-8.

---

## STEP 0 -- Gates

- **No skill was bumped this session**, so there is no mid-session
  install to verify. Load `interactive-exhibit` (expect 1.0),
  `gallery-assembler` (1.2), `ledger-and-session-records` (1.10),
  `orrery-coding-conventions` (1.7), `safe-file-editing` (1.10); each
  must match the manifest in PROJECT_INSTRUCTIONS.md Part 3.
- Ordinary session start: `git ls-remote` both repos, record the base
  SHAs, reconcile if either moved past the anchor above. Tony reported
  the orrery at `af4c604e` and the gallery at `700b426d` at close, and
  both were confirmed against the remotes.
- **Tony-action pending, not a gate:** run
  `patch_L291_7_ledger_masterplan_20260908.py` (orrery root), then
  `ledger_index.py`, commit, push. If the ledger does not yet carry
  L-301..L-304 at session start, that patch has not run; ask.

## WHERE STEP 2 LEFT THINGS (done)

Orrery. 21 sourced constants in `constants_new.py` (the "Earth exhibit
block" after `EARTH_UPPER_MANTLE_RADII`, plus the Hill sphere pair after
`GM_SUN_SI`). Every Earth shell in `earth_visualization_shells.py` and
`shell_configs.py` reads them; no drawn literal remains. Both atmosphere
shells draw their sourced boundaries (stratopause 50 km, thermopause
600 km), markers stepped 20/30 degrees (L-295 closed). Every live Earth
hover ends in a scoped Source line (L-299 rule, skill bump pending).
Two values moved when sourced and Tony accepted both: bow shock
15 -> 12.5 R_E; LEO edges 6571/8371 -> 6578/8378 km.

Gallery. Earth's `objects_config.json` entry is in the measured shape:
value / unit / source / orrery_constant on every rendered number, nine
groups -- `earth_interior`, `earth_atmosphere`, `earth_exosphere`,
`earth_orbital_zones`, `earth_geostationary`, `earth_magnetosphere`,
`van_allen_belts`, `hill_sphere`, `orientation`. The nightly of
2026-09-08 serves it. Live store drift: 24 Earth pointers MATCH by name,
0 DRIFT anywhere; the five "could not be examined" are pole pointers
into `idealized_orbits.py` and the galactic-tide default -- the known
class, none new.

What draws TODAY in the Explorer room: interior stack (5), atmosphere
(2), geocorona (1), LEO edges (2), belts (2), Hill sphere (1) = 13
traces, each info marker ending in its Source line. The shell-set
renderer reads `R_earth`, `km`, and `planet_radius`; the belt renderer
reads measured distances.

What does NOT draw, and the dispatch names them: `earth_geostationary`
(an equatorial ring; needs `orientation`) and `earth_magnetosphere`
(magnetopause and bow shock standoff shapes; magnetotail declared).
Their renderers are step 3. The smoke test pins exactly those two
warnings; when the renderers land, the pin moves in the same commit.

## STEP 3 -- Code (next)

Read `interactive-exhibit` step 3 first. Then, in this order:

1. **Two renderers in `gallery/feature_renderers.js`.**
   - `earth_geostationary`: a ring in the body's equatorial plane at
     `radius` (R_earth), oriented by `poleBasis(orientations[slug])`
     the way `renderRingSystem` is; warn and draw in the ecliptic if no
     orientation, as the ring renderer does. Row shape is
     `{shape: "equatorial_ring", radius: {value, unit}, ...}`.
   - `earth_magnetosphere`: rows `magnetopause` and `bow_shock` carry
     `standoff: {value, unit: "R_earth"}` and `shape`; `magnetotail`
     is declared (length 100, base 15, end 25 radii). Sun direction is
     needed for the nose; take it from the scene the way the orrery
     does (Earth-to-Sun vector), and the hover MUST say the tail is
     drawn to 100 radii against a real tail past 1,000.
   - Update `documentation/smoke_features.js`: the two expected
     warnings become zero; the trace count 13 becomes 13 + what the
     new renderers add; the Source-line pin should hold for the new
     markers too. Regenerate nothing -- the fixture already carries the
     rows.
   - `pin_artifact1_known_failure.py` does not move (served keys are
     unchanged by renderers).
2. **The `EXHIBIT === "earth"` branch in `interactive.html`.** Driver
   spec: `objects` Earth and Moon, `center` Earth, half-range floor
   6.155e-5 AU (Earth's `SUN_HALF_RANGE_AU`). Eight shells lit on
   arrival: inner core, outer core, lower mantle, upper mantle, crust,
   lower atmosphere, upper atmosphere, LEO. Also on: axis with equator
   plane, Sun direction. Everything else a drawer row, unselected.
3. **The terminator** is geometry: a great circle on the crust
   perpendicular to the Sun direction plus a subsolar marker carrying
   the hover. No lighting model.
4. **The Moon's orbit:** full ellipse faint, the trust-window arc
   brighter around the marker (`render_orbits.py` already separates
   shape from marker; the 3.37-day window bounds the marker only).
5. **Hovers that must say something:** the scene is one epoch, so the
   terminator is frozen and the axis implies a rotation the scene does
   not show; the tail is truncated. Silence reads as precision.
6. **The shared chrome, by parameter.** Grep `interactive.html` for
   `sun` inside drawer, nav cluster, frame zoom, i-panel, frame HUD,
   consent gate, back link; decide piece by piece -- rename /
   parametrize / leave. No ruling exists yet; it is judgment at the
   point of edit, and the reason to rename is that Earth is the second
   user.
7. **i-panel copy** per feature with sources inline. The served rows
   already carry the source strings; the panel can read them rather
   than restate them.

Steps 4-8 as in `HANDOFF_earth_build_order_20260906.md`: `node --check`
and a stand-in scene in the sandbox (the exhibit cannot start there --
say so); push and `--live`; Mode 5 on the phone, conditions stated;
the Studio card via New Interactive Card (the picker reads
`EXHIBIT === "earth"` literally); L-291 closes on Tony's eyes.

## OPEN ITEMS THAT TOUCH THIS BUILD

- **L-303 (Tony to decide):** one card with two file slots, or one card
  per orientation. Tony prefers separate cards. The fact that bears:
  the viewer no longer filters the grid by device, so separate cards
  need device filtering back. Do not change the card model until
  ruled. It does not block step 3.
- **L-288 (Tony-action, do):** the served Earth-and-Moon PORTRAIT file
  still carries the grey hover box; it was exported before the Studio
  fix. Re-export the portrait scene through Studio and re-convert with
  P; with L-301's pairing the converter replaces the portrait slot on
  the same card.
- **L-297:** Earth-Moon Lagrange points are deferred; a builder session
  of its own. Not in this exhibit.
- **L-292:** the orrery still has no exosphere/geocorona shell of its
  own (`EARTH_GEOCORONA_RADII` exists; `SHELL_CONFIGS['Earth']` does
  not draw it). Gallery side is served. Small orrery patch when a
  session has that file open.
- **L-299 / L-304 (skill bumps pending):** orrery-coding-conventions 1.8
  (a hover that quotes a number names its source) and gallery-assembler
  1.3 (four Plotly/viewer field notes). One session, one bump each.
- **L-300:** `sweep_collapsed_features.py` into the gallery maintenance
  runner as a gating checker -- ruled, not yet written. Earth's four
  magnetosphere rows retire four of L-268's sixteen when the renderer
  lands.
- **L-298 (Tony to discuss):** seeing the orrery-vs-exhibit feature
  gap -- tool or judgment. Not blocking.

## FILES THIS SESSION LEFT (all pushed unless noted)

Orrery: `patch_L291_1..5` (constants, migration, atmosphere, hover
sources, ledger) -- spent, at the repo root; they read as two Tier-1
findings in the scanner until moved to `documentation/` on the usual
sweep. `patch_L291_7_ledger_masterplan_20260908.py` -- NOT YET RUN.

Gallery: `patch_L288_1` (converter path, grey box), `patch_L291_6`
(served entry, seven files), `patch_L286_1` (3D rotation),
`patch_L287_2` (pairing), `patch_viewer_infocard_tap_20260908`
(card tap; Artifact 1 pin) -- all spent and pushed.
`documentation/SIZING_earth_moon_lagrange_20260907.md` -- the L-297
record; confirm it landed in `documentation/`.

## WHAT THIS SESSION LEARNED THAT IS NOT IN A RULE YET

- The store-drift checker, the renderers, the builder's validator and
  two test files all encoded "the Sun is the only exhibit" in small
  ways (unit tables, key lists, bare-number shapes). Each surfaced as
  a check failing, which is the system working; expect the same class
  for Jupiter.
- The served card is a better test rig than the sandbox for the
  pipeline: four defects in one day, none reproducible here (WebGL,
  touch, OneDrive).
- Every Plotly behaviour that bit this session was verifiable by
  grepping the shipped `plotly-2.35.2.min.js`, which npm can fetch
  into the sandbox. Do that before theorising.

Written September 2026 with Anthropic's Claude Fable 5.1.
