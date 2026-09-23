# Earth Exhibit -- Build Order for the Next Session

Built on orrery `d7151aafd8563901e3e1f478be0f4f280da56849`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `92e98ca98e15e0425a48931fca9365f0b52f426f`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-06
Protocol v3.54. Ledger handle: L-291.

This is the ORDER, not the design. Every ruling this build implements is
in `documentation/PREDESIGN_earth_exhibit_20260906.md` (GALLERY repo),
which is the authority for what the exhibit draws and why. Read it
first; do not re-litigate what it settles.

The steps below are the `interactive-exhibit` skill's own eight, with
Earth's specifics filled in. Step 1 is done.

---

## STEP 0 -- Gates, before anything else

Two skill installs happened on 2026-09-06 and could NOT be verified from
inside the session that made them. This session's load is the check.

- **`ledger-and-session-records` must read 1.10.** If the loaded copy
  reads 1.9, STOP per Stale Skill = Stop and tell Tony. If it reads
  1.10, say so plainly -- that discharges L-290 and L-296, both of which
  are PENDING-GATE waiting on exactly this, and both can then close.
- **`interactive-exhibit` must load and read 1.0.** The 2026-09-06
  design session could only READ the repo copy; it was not installed
  then. If it does not load at all, the build stops here.

Then the ordinary session start: pull both repos at HEAD, record the
base SHAs, and reconcile if either has moved past the anchor above.

## STEP 2 -- Served data (the bulk of the work)

Nothing renders until Earth's entry in the gallery's
`data/objects_config.json` carries every feature the design draws, each
measured value with value / unit / source / orrery_constant.

Earth has TWO feature groups today (atmosphere shell, Van Allen belts)
and needs roughly a dozen. The predesign record's section 6 sorts the
work into three buckets, and SORTING BEFORE SOURCING is the point -- it
is not a dozen citations.

- **DERIVED, no source needed:** crust radius (it IS the equatorial
  radius), lower and upper atmosphere tops, LEO inner and outer edges,
  geostationary radius (from GM and the sidereal day), Hill sphere
  radius (from the masses and the semi-major axis). Derive, do not type
  -- same move as L-249 on the interior.
- **NEEDS A CITATION, five:** both Van Allen belt distances, the
  magnetopause sunward standoff, the bow shock standoff (HALF DONE --
  the code line already carries a note, textbook ~15 radii against a
  measured nominal 11-14), and the geocorona (DONE -- Baliukin et al.
  2019, JGR Space Physics 124, 861-885, doi:10.1029/2018JA026136, at
  least 100 Earth radii).
- **DECLARED, marker not source:** belt thickness, tail base and end
  radii, the magnetotail length, opacities, point counts.

Order within the step: one patch to the ORRERY's `constants_new.py`
adding the block with sources inline; provenance scanner clean on the
active build path; push. THEN one patch to the GALLERY's
`objects_config.json` adding the `orrery_constant` pointers. NOT IN
STORE is fixed by adding the constant, never by removing the pointer.

Also in this step:
- **The exosphere shell does not exist in the orrery** (L-292). It is
  folded into the upper atmosphere shell at 1.25 radii. It has to be
  built before the exhibit can draw it.
- **The magnetosphere's four traces split into four served rows** --
  magnetosphere, bow shock, inner belt, outer belt. The orrery emits
  them from one call; do not inherit that grouping.
- **Earth needs an `orientation` block** (pole RA/Dec). The Sun's entry
  has one, Earth's does not. Both poles are already in the orrery store
  at `idealized_orbits.py::planet_poles`, IAU 2018.
- **Confirm the nightly builder covers Earth, the Moon and the
  Earth-Moon Lagrange points**, and that `coverage_index.json` lists
  them. Earth and the Moon are already covered and analytic. THE
  LAGRANGE POINTS ARE NOT, and they are a different serving path --
  they do not travel on Keplerian orbits about their primary, so they
  need serving as MARKERS at the epoch. This is gallery-cache-builder
  work and it is the least-known part of the whole build. Size it
  before committing to it; if it is large, it is legitimate to ship
  Earth without them and let them follow.
- **L-295 sits in a file this step has open:** the upper atmosphere
  shell is drawn at 1.25 radii (about 1,595 km altitude) while its own
  hover text says 50 km to about 1,000 km. Cluster the tail rather than
  making a separate errand of it.

## STEP 3 -- Code

One `EXHIBIT === "earth"` branch. Driver spec with `objects` = Earth and
the Moon, `center` = Earth.

- **Half-range floor: 6.155e-5 AU** (9,208 km, 1.4437 equatorial
  radii). That is 1.1x LEO's outer edge at 8,371 km. Earth's analogue of
  `SUN_HALF_RANGE_AU`.
- **Eight shells lit on arrival:** inner core, outer core, lower
  mantle, upper mantle, crust, lower atmosphere, upper atmosphere, LEO.
- **Also ON at arrival:** the axis with its equator plane, and the Sun's
  direction. Everything else is a drawer row, unselected.
- **The terminator** is a great circle on the crust perpendicular to the
  Sun direction, plus a subsolar point marker carrying the hover. It is
  GEOMETRY. There is no lighting model and there will not be one.
- **The Moon's orbit:** full ellipse faint, the arc within the trust
  window brighter around the marker. Emphasis, not truncation.
  `render_orbits.py` already separates orbit SHAPE (a geometric sweep,
  no time in it) from position MARKER (Kepler from mean anomaly); the
  3.37-day window bounds the marker only.
- **Hovers that must say something:** the scene is a single epoch, so
  the terminator is frozen and the axis beside it implies a rotation the
  scene does not show. The magnetotail is drawn truncated at 100 radii
  against a real tail past 1,000. Silence reads as precision.

Then the shared chrome, by parameter. The skill's One Chrome, Many Rooms
rule fires here: grep `interactive.html` for `sun` inside the shared
pieces -- drawer, nav cluster, frame zoom, i-panel, frame HUD, consent
gate, back link -- and decide piece by piece, rename / parametrize /
leave. Earth is the second user, which is what makes a `sun*` name wrong
rather than merely specific.

## STEP 4 -- Pre-test in the sandbox

`node --check` on the page script. A stand-in scene for chrome that can
run without Pyodide. THE EXHIBIT ITSELF CANNOT START IN THE SANDBOX --
the CDN is blocked -- so say so in the handoff rather than implying a
run happened.

## STEP 5 -- Push and the live run

`gallery_maintenance_run.py --live`. Store drift must read MATCH for
every new pointer, BY NAME, not by count. A count delta cannot fail.

## STEP 6 -- Mode 5 on the phone

Tony's eyes, iPhone, both orientations. Mode 5 is MEASUREMENT, not just
acceptance (gallery-assembler 1.2): state the CONDITIONS, not only the
actions, and have each trial name what it rules out.

The Sun took three Mode 5 rounds on its chrome alone and none of the
three failures was visible headless. Budget for that rather than
treating a second round as a setback.

## STEP 7 -- The card

Studio -> New Interactive Card (L-288) -> pick the scene. The picker
reads `EXHIBIT === "earth"` LITERALLY from the page source, so the key
must appear in exactly that form. Title, placard, sources. It lands in
Storage; the editor places it; featured if it belongs on the lobby.

A live card carries NO still picture -- it is a placard with an
Interactive tag.

**Note:** L-288's own converter path is still untested. If this session
is in `json_converter.py` anyway, exercising it closes that item.

## STEP 8 -- Ledger

L-291 closes on Tony's Mode 5, not on the push.

---

## What this build does NOT do

- **Sun-Earth Lagrange points.** A Lagrange point belongs to the frame
  that defines it (Tony's rule). Sun-Earth L1-L5 wait for the
  heliocentric view of Earth's orbit -- that is L-294, together with the
  Explorer room's placeholder question.
- **The lunar standstill.** Four dated orbits fanning apart is its own
  room or card (L-293), not a drawer row here. It needs the served cache
  to hold several osculating blocks per object; it holds one.
- **Anything from the Earth System climate work.** Tony ruled that out
  of scope for this exhibit.
- **GPS/MEO and the Earth Roche limit** (L-292). Wants, not gaps.

## Open questions this session may hit

1. **How big is the Lagrange-point serving work?** Unknown, and it is
   the one place this build could balloon. Size it early.
2. **The `sun*` renaming** has no ruling yet -- it is piece-by-piece
   judgment at step 3.
3. **i-panel copy** per feature, with sources inline. Writing, and it is
   real work that is easy to leave to the end and then rush.
