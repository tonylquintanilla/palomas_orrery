# Earth Exhibit -- Predesign Record

Built on orrery `50cbd2df708f8dc16cb181d204f49dd36f14b367`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `90615b9f13a55d710593750316bf2b970dae241b`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-06
Protocol v3.53. Step 1 of the `interactive-exhibit` skill's order
("design round with Tony, zero code, record rulings before code").

CAVEAT ON THE SKILL. The `interactive-exhibit` skill was NOT loaded in
this session -- it is not installed to the account yet. Its repo copy at
`skills/interactive-exhibit/SKILL.md` was READ at the SHA above and reads
version 1.0, matching the manifest row. Reading is not loading. The
session that builds confirms its loaded copy reads 1.0 first.

---

## 1. Scope

The exhibit is Earth's shells plus the Moon, Earth-centered
(`?exhibit=earth`). Chosen over three alternatives:

- Sun exhibit plus Earth's orbit -- that is a change to the Sun room or
  the Explorer's job, not an Earth exhibit. Kept as a separate question
  (see Open Items).
- Shells alone -- the Moon costs nothing extra, see below.
- Earth plus Moon without shells -- two markers and an orbit; the
  Explorer already does that kind of view.

The Moon is free. Its entry is already served: analytic, parent Earth,
stored center Earth, parent-relative frame, and its `features` dict is
EMPTY, so it brings no shells and no new provenance pointers. It is one
extra name in the driver's `objects` list.

Tony's reason for the pairing: the Hill sphere is not decoration beside
the Moon, it is the answer to why the Moon is bound. Drawn together they
teach what neither teaches alone.

## 2. Arrival frame

EDGE AT LOW EARTH ORBIT. Largest visible on arrival is the LEO shell's
outer edge, 8,371 km from Earth's center (1.3125 equatorial radii, per
the orrery's own hover text: 6,571 to 8,371 km, 1.03 to 1.31 radii).

Half-range = 1.1 x 8,371 km = 9,208 km = 1.4437 radii = 6.155e-5 AU.
That is Earth's floor constant, the analogue of `SUN_HALF_RANGE_AU` 0.25.

Eight shells lit on arrival, innermost outward:
inner core, outer core, lower mantle, upper mantle, crust,
lower atmosphere (1.05), upper atmosphere (1.25), LEO (1.03-1.31).

Tony's framing: "what we see from the ISS." The station orbits at about
400 km at 51.6 degrees inclination (orrery figure, NASA-sourced), which
is 1.063 radii -- inside the upper atmosphere shell and inside LEO, so
the arrival frame is literally the station's neighbourhood.

ALSO ON AT ARRIVAL, both legible at this scale:
- Earth's axis and equator plane. The 23.4 degree tilt against the
  ecliptic reads right at the surface.
- The Sun's direction. Tells you which half of Earth is in daylight, and
  it is a precondition for the magnetosphere later (see 4).

## 3. Drawer, unselected on arrival

Outward from the frame edge:

| Row | Distance | Note |
|---|---|---|
| Van Allen inner belt | 1.5 radii | see 4, splitting |
| Van Allen outer belt | 4.5 radii | GPS would sit inside this |
| Geostationary belt | 6.62 radii, 42,164 km | |
| Magnetosphere | 10 radii sunward | compressed dayside |
| Bow shock | 15 radii standoff | conic, e=1.05 |
| Magnetotail | 100 radii as drawn | DECLARED, truncated -- see 4 |
| Moon | ~60 radii | orbit + marker, see 5 |
| Exosphere / geocorona | 100 radii | NEW shell, see 4 |
| Hill sphere | 235 radii | |
| Earth-Moon L1-L5 | ~51-70 radii | L4/L5 ride the Moon's orbit |

Turning on the Hill sphere rescales the frame by about 160x and the
whole arrival stack becomes a dot. Same behaviour as the Sun going out
to the Oort cloud, so the mechanism is proven.

## 4. Features added during the round

THE SUN'S DIRECTION. Not optional. The orrery's magnetosphere is not a
sphere -- it is compressed to 10 radii sunward, runs a tail 100 radii
long, and carries a separate conic bow shock standing off at 15, and the
code rotates all of it via `rotate_to_sunward`. An Earth-centered exhibit
must know where the Sun is at the epoch before it can draw the
magnetosphere honestly.

THE AXIS AND EQUATOR. Earth's served entry has no `orientation` block;
the Sun's does. Both poles are already in the orrery store --
`idealized_orbits.py::planet_poles`, Earth at RA 0.00 / Dec 90.00 and the
Moon at RA 269.99 / Dec 66.54, both IAU 2018 -- and the same `poleBasis`
the gas giants use reads them unchanged.

LAGRANGE POINTS. The orrery carries both sets: Earth-Moon L1-L5 (Horizons
3011-3015) and Sun-Earth L1-L5 (Horizons 31-35).

TONY'S RULING: a Lagrange point belongs to the FRAME THAT DEFINES IT.
Earth-Moon L1-L5 go in this exhibit. Sun-Earth L1-L5 wait until Earth's
heliocentric orbit is drawn -- which ties them to the Explorer question
(Open Item 3). One rule, no case-by-case exceptions.

The Earth-Moon five sit at roughly 51-70 Earth radii, in the Moon's own
neighbourhood, with L4 and L5 riding the Moon's orbit sixty degrees ahead
and behind. Distances recalled, NOT checked -- verify against Horizons
before anything is drawn.

DEFERRED WITH THEM, AND NOT LOST: Sun-Earth L1 and L2 sit at about 235
radii, the same distance as the Hill sphere, and that is not a
coincidence -- it is the same balance point measured two ways. Tony's
resolution: THE HILL SPHERE DRAWS IN THE HELIOCENTRIC ROOM TOO. It is
Earth's feature either way, so the same served entry serves both rooms
with no duplicate provenance work, and there L1 and L2 sit on its
surface where the Sun-Earth line crosses. The coincidence becomes
visible instead of asserted.

Scale note for that room: at whole-orbit scale the Hill sphere is about
half a percent of the frame, so the pairing only reads after a frame
zoom onto Earth. Not the arrival picture.

TECHNICAL, and why this is builder work rather than a config line:
Lagrange points do not travel on Keplerian orbits around Earth. Sun-Earth
L1 sits permanently sunward and merely circles once a year in an
Earth-centered frame; the Earth-Moon points ride the Moon. The cache's
trust machinery works by fitting two-body propagation, so these need
serving as MARKERS at the epoch rather than as orbits. A different path
from Earth and the Moon.

EXOSPHERE / GEOCORONA. New shell, and the strongest single addition.
Earth has none today -- the exosphere is folded into the "upper
atmosphere" shell at 1.25 radii. The hydrogen geocorona was mapped by
SWAN/SOHO to at least 100 Earth radii, past the earlier LAICA result of
about 50, and enclosing the Moon's orbit at about 60 (Baliukin, Bertaux,
Quemerais, Izmodenov & Schmidt 2019, J. Geophys. Res. Space Physics 124,
861-885, doi:10.1029/2018JA026136). The Moon flies through Earth's
atmosphere.

It earns the Sun direction a second time: solar radiation pressure
compresses the exosphere into a dayside bulge. Same sunward asymmetry as
the magnetosphere, entirely different mechanism -- solar wind versus
photon pressure. Drawn together they read as a pair.

SUNLIGHT AS GEOMETRY, NOT AS LIGHTING. Ruled: no shading model. Every
shell in the gallery is a uniform-colour point cloud; shading Earth alone
breaks one-chrome-many-rooms, and the gas giants would want it next.
Lighting is a rendering effect, not a measurement, so it would land in
the DECLARED zone with nothing to source.

Instead: the terminator drawn as the great circle on the crust
perpendicular to the Sun direction -- real geometry, computed from the
sun vector and Earth's radius, nothing invented -- plus a subsolar point
marker carrying the hover. Visible at arrival because the shells above it
sit at 0.5 and 0.3 opacity.

HOVER MUST SAY: the scene is a single epoch, so the terminator is frozen.
The axis beside it implies a rotation the scene does not show. Silence
would read as precision the model lacks (Show the Envelope of the
Unknowable).

MAGNETOTAIL RECLASSIFIED. The 100-radii tail length is a drawing choice
wearing a physical-looking number; the real tail runs well past 1,000
radii. Same shape as the streamer belt's warp amplitude. It moves to
DECLARED, and the hover says the tail is drawn truncated.

## 5. The Moon's orbit

FINDING. The Moon's osculating elements are served and fresh -- center
Earth, a = 0.0025481 AU, e = 0.0339, i = 5.267 deg, epoch JD 2461289.5,
retrieved 2026-09-06T13:31:38Z. But its measured trust window is
3.37 DAYS against Earth's 365.4. Its node and apsides precess about a
hundred times faster than Earth's, so a two-body fit goes stale within
days.

Nothing in the serving path enforces that. `resolver.py` gates on the
cache's global `served_window` (currently about 647 days wide), and that
window is built only from objects whose `canonical_frame` is
heliocentric (`TRUST_WINDOW_PARTICIPANT_FRAME`, builder line ~1067). The
Moon is parent-relative, so it is not a participant. Its 3.37-day window
is measured, recorded, and read by nothing outside the builder's own
offline test.

The Sun exhibit never met this because it draws no orbits at all. Earth
is the first exhibit to exercise the assembler's propagation path.

WHAT THE NUMBER MEANS. `render_orbits.py` keeps two jobs apart: the orbit
SHAPE is a geometric sweep of true anomaly with no time in it, and the
position MARKER is propagated from mean anomaly through Kepler. So the
ellipse is exact at its epoch regardless. The 3.37 days bounds the
MARKER, not the ellipse.

Tony's correction, and it stands: in the orrery each osculating ellipse
is clean; the perturbation shows as the SPREAD between ellipses fetched
at different dates, not as degradation within one. The difference in the
gallery is only that the cache holds one snapshot per object per nightly
build.

RULING: full ellipse drawn faint, with the stretch of arc within the
trust window drawn brighter around the marker. Emphasis, not truncation
-- it never claims the ellipse stops. Bright means we would stand behind
the Moon really being there; faint means it is the path, not a promise.
No builder change.

## 6. Provenance plan

The scanner is NOT the mechanism here. It is the orrery's tool, and the
assembler does not pass through it. The exhibit's check is the LIVE STORE
DRIFT run, which follows each `orrery_constant` pointer into
`constants_new.py` at orrery HEAD and reports MATCH / DRIFT / NOT IN
STORE by name.

IN THE STORE TODAY, for Earth and the Moon:
`EARTH_EQUATORIAL_RADIUS_KM`, `EARTH_POLAR_RADIUS_KM`,
`EARTH_MEAN_RADIUS_KM`, `EARTH_INNER_CORE_KM`, `EARTH_INNER_CORE_RADII`,
`EARTH_OUTER_CORE_KM`, `EARTH_OUTER_CORE_RADII`, `EARTH_D660_DEPTH_KM`,
`EARTH_LOWER_MANTLE_KM`, `EARTH_LOWER_MANTLE_RADII`,
`EARTH_UPPER_MANTLE_KM`, `EARTH_UPPER_MANTLE_RADII`, `MOON_RADIUS_KM`,
plus both poles in `idealized_orbits.py::planet_poles`. That is the L-249
conversion.

NOT IN THE STORE. Everything else is a typed literal in
`earth_visualization_shells.py`. Sort before sourcing -- most need no
literature at all:

DERIVED (no source needed; derive, do not type):
- crust radius -- it IS the equatorial radius
- lower atmosphere top, upper atmosphere top -- from altitudes already in
  the hover text with sources attached
- LEO inner and outer edges -- same
- geostationary radius -- from Earth's GM and the sidereal day
- Hill sphere radius -- from Earth's and the Sun's masses and the
  semi-major axis

NEEDS A CITATION (five):
- Van Allen inner belt distance (1.5 radii)
- Van Allen outer belt distance (4.5 radii)
- magnetopause sunward standoff (10 radii)
- bow shock standoff (15 radii) -- HALF DONE: the code line already
  carries a note, textbook ~15 against a measured nominal 11-14
- geocorona extent (100 radii) -- DONE, Baliukin et al. 2019, above

DECLARED (marker, not source):
- belt thickness, tail base and end radii, magnetotail length,
  opacities, point counts

ORDER: one patch to `constants_new.py` adding the block with sources
inline, scanner clean on the build path, push. Then one patch to the
gallery's `data/objects_config.json` adding the pointers. Then the live
run reads them back MATCH by name. That is the gap closed.

## 7. Proposed ledger items

ORRERY SHELL ADDITIONS (one row, by class, per The Braid):
- exosphere / geocorona shell -- IN this exhibit, so needed either way
- MEO / GPS shell at 4.2 radii, inside the outer Van Allen belt; the
  overlap is the teaching point. Not rendered here, so nothing points at
  it and store drift will not check it. Harmless to add and park.
- Earth Roche limit -- the Sun has one, Earth has none
- FINDING, separate: the upper atmosphere shell is drawn at 1.25 radii
  (about 1,595 km altitude) while its own hover text says the upper
  atmosphere runs 50 km to about 1,000 km. Those disagree.

LUNAR STANDSTILL EXHIBIT (its own item, not part of Earth):
Four osculating orbits at today, one month, one year and 9.3 years,
fanning wider and wider. Rationale for the intervals: the Moon's orbit is
nearly circular (e = 0.034), so the swing of its long axis is almost
invisible; what separates two drawn ellipses is the drift of the TILT
direction, which goes all the way round in 18.6 years. So 9.3 years apart
are tipped opposite ways -- the widest gap the Moon can show. That cycle
is the lunar standstill, watched from stone circles and canyon walls for
four thousand years before anyone could say why.

Precedent: the orrery already does this for comets. With apsidal markers
on, it resolves perihelion time, fetches the comet's elements AT that
moment, and draws that conic as a white dotted arc beside the conic for
the plot date -- two orbits from two instants, each chosen because it
means something.

Two cautions recorded with the item:
- Whether it is a room in `interactive.html` or a curated card is a
  separate decision. Four orbits and a story may not need a drawer, a nav
  cluster and an i-panel.
- THE FOUR INTERVALS ARE PICKED BY LOOKING, NOT DECIDED HERE. The 19 and
  41 degrees per year quoted in conversation came from the standard cycle
  lengths (18.6 and 8.85 years), not from a source checked this session.
  There is also a monthly wobble from the Sun's pull that may or may not
  swamp a one-month pair. The orrery fetches elements at any date, so
  this is an evening's looking.

## 8. Open items

1. CLOSED -- Lagrange sets ruled by frame, see section 4.
2. CLOSED -- VAN ALLEN SPLIT INTO SEPARATE DRAWER ROWS. The orrery's
   magnetosphere function
   emits FOUR traces at once: magnetosphere, bow shock, inner belt, outer
   belt. The served entry SPLITS them into four rows. The belts are
   trapped particles; the magnetopause and bow shock are the solar wind
   meeting the field. Different phenomena, and at 1.5 and 4.5 radii the
   belts sit far inside a magnetosphere that starts at 10.

   Tony's note on why the grouping existed: LEGEND ECONOMY in the orrery,
   where rows are scarce. The exhibit has a scrolling drawer instead of a
   legend, so that pressure is gone. Worth remembering as a general point
   -- groupings inherited from the orrery may be solving a constraint the
   exhibit does not have.
3. THE EXPLORER ROOM'S PLACEHOLDER URL, and with it the heliocentric view
   of Earth's orbit. Tony's question from the Mode 5 pass. Option 1 in
   section 1 touches the same ground, and the Sun-Earth Lagrange points
   now WAIT ON THIS -- it is no longer a loose end.
4. i-panel copy per feature, with sources inline. Writing, not design.
5. `sun*` CHROME RENAMING. The skill's One Chrome, Many Rooms rule: grep
   `interactive.html` for `sun` inside the shared pieces and decide,
   piece by piece, rename / parametrize / leave. Step 3 work.

## 9. What this record does NOT decide

Nothing about code. No file has been opened for editing. The build begins
only after the `interactive-exhibit` skill is installed and its loaded
copy is confirmed to read 1.0.
