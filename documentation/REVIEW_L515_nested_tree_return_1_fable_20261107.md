<!-- Doc-Kind: hand | A reviewer's return on the L-515 design-review request: the website's room system as one nested tree. Communication; written once, read by its receiver. -->
# Design review return: one nested tree in place of isolated rooms (L-515)

Built on orrery 27f6f5bdc34616f2eecd19e290a51a0eaa059c08 at
https://github.com/tonylquintanilla/palomas_orrery (branch main)
and gallery ae68a93aa1ba6fac94e0b16d19247f6e3f2c0c29 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main).
Both were still HEAD when fetched, 2026-11-07, about 11:00 Chicago.

Reviewer: Anthropic's Claude Fable 5.1, in Tony's Orrery Project on
claude.ai, from the request
`documentation/REVIEW_L515_nested_tree_request_20261107.md` (the
attached prompt). Zero code.

## 1. The rule files read

Fetched from the orrery at the SHA above, each version line matching
the manifest in PROJECT_INSTRUCTIONS v3.128:
- `PROJECT_INSTRUCTIONS.md` (resident in the Project; Part 4 "The
  Orrery and the Assembler" and Part 3 "Fetched vs Recalled" read again).
- `skills/interactive-exhibit/SKILL.md`, 1.32: the anatomy table, "What
  a room opens on is SERVED", "The Solar System room's drawer", "Only
  two tools write the served config", "One check reads the file the
  browser fetches".
- `skills/gallery-assembler/SKILL.md`, 1.3, in full.
- `skills/gallery-cache-builder/SKILL.md`, 1.18: "A config change is
  not deployed until the cache is rebuilt", "Adding a new object".
- `skills/horizons-orbital-mechanics/SKILL.md`, 1.18: "Horizons Center
  Body Rules", "How a Path's Events Are Found", "Encounter and Flyby
  Resolution".
Also read: `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md` (OQ-F and
the v4 reconciliation note), ledger L-515, L-514 and L-297, and in the
gallery `interactive.html` (the `EXHIBITS` table and the three drivers),
`gallery/assembler/resolver.py`, `assemble.py`, `render_orbits.py`,
`gallery/feature_renderers.js`, `gallery/arrival.js`,
`tools/gallery_cache_builder.py`, `tools/mirror_objects.py`,
`data/objects_config.json` and `data/solar-system/coverage_index.json`.

## 2. Findings, most important first

**1. Rule 7 cannot be kept at any centre but the Sun for a neighbourhood
child, because drawing it there needs a position the website refuses to
make.** A neighbourhood child (rule 1: the Atens under Venus, missions
under Earth) is served around the Sun only. To draw it in an
Earth-centred view the page would have to subtract Earth's Sun-centred
position from the child's, which is the retired operation, and the
assembler refuses the scene before any trace is built. So from Earth's
centre a visitor could tick "Spacecraft" in the branch and nothing could
be drawn. VERIFIED: `gallery/assembler/resolver.py`, `resolve()`, step 4
("Frame rejection: object must be stored in the scene's center frame",
`FrameRejectionError`); the Earth driver's own comment, `interactive.html`,
`EARTH_DRIVER` ("Listing Earth as an object is rejected, because Earth is
stored relative to the Sun"). QUESTION, Tony's (WHAT): either (A) a
neighbourhood child is only LISTED under its parent, and ticking it from
the parent's centre returns the visitor to the Sun's view with it ticked;
or (B) the nightly build also fetches it around the parent it is listed
under (JPL can centre on a planet, `500@399`), which is a second fetch
per child and makes Artemis-around-Earth possible. The rules as written
promise (B)'s result with (A)'s data.

**2. Rule 4's worked case cannot open on today's cache, for two separate
reasons.** First, the page checks the requested moment against ONE
served window for the whole scene; at this build the window runs
2026-08-11 to 2027-02-03, and the Psyche craft's Mars flyby is
2026-05-15. VERIFIED: `resolver.py`, `resolve()`, step 3
(`OutOfServedWindowError`); `data/solar-system/coverage_index.json`,
`served_window`. Second, the flyby's five-minute window is served around
the Sun, not around Mars; the builder fetches every point of a path
around the object's one `canonical_center`. VERIFIED:
`tools/gallery_cache_builder.py`, `process_object()` and
`fetch_path_by_plan()`, both passing `obj['canonical_center']`;
`data/objects_config.json`, `psyche_spacecraft.path.events[1]`. What an
encounter needs from the build (HOW, a builder rule, not Tony's): the
event's window fetched a second time around the body met -- the orrery's
own path planner already asks JPL exactly that way (horizons skill, "How
a Path's Events Are Found": "Around a major body the path is asked
centred on it ('500@<id>')"), and the builder has a precedent for a
second-centre fetch of one object (`needs_drawn_orbit()`, Pluto's
ellipse around the barycentre); and a way for an encounter scene to
carry its own window instead of the whole-site one. Two more pieces are
undecided: an encounter with a SMALL body (Lucy's asteroids, OSIRIS-APEX
at Apophis) needs a numeric JPL centre id in the config, since Horizons
cannot centre on a designation (horizons skill, "Only NUMERIC IDs can be
coordinate centers"); and a planet's moons at an encounter date months
from today's elements -- see finding 5.

**3. Rule 2's "focus is valuable for flybys" is the one place the
page's drift would show, and it should be struck.** In a Sun-centred
view a spacecraft is drawn from JPL's served positions, which do not
drift, but the planet is propagated in the browser from today's
elements, which do. The cache measures Mars's drift at 4.7e-6 degrees
per day (VERIFIED: `coverage_index.json`, `objects.mars.trust.
error_rate_deg_per_day`); over the 176 days from today's elements back
to the Psyche flyby that is about 0.0008 degrees, which at Mars's
distance is about 3,000 km (INFERRED: my arithmetic on the served rate),
against a pass at 8,000 km. Zooming in on that pass in the Sun's view
would draw the craft on the wrong side of Mars by nearly half the
passing distance. A flyby is therefore always a CENTRE on the body met
(rule 4), never a focus in the Sun's view. Focus stays right for comet
features and for moons, where everything in the picture rides one
chain of served answers (finding 4).

**4. Adding is sound, and the assembler already does it; the request's
sentence about subtraction needs one correction.** What was retired in
July (master plan, OQ-F and the v4 note; gallery-assembler skill, "No
composition between frames") was deriving a SMALL relative vector by
subtracting two LARGE, nearly equal Sun-centred ones. Placing a small
shape at a large position is the opposite operation and loses nothing,
and the website does it at HEAD: Pluto's ellipse around the barycentre
is moved to where the barycentre sits, and the offset is found as
Pluto-around-the-Sun minus Pluto-around-the-barycentre, a large vector
minus a tiny one. VERIFIED: `render_orbits.py`, `drawn_orbit_offset()`;
`assemble.py`, the `drawn_orbit` block. Features are already drawn
around a body's propagated position: `feature_renderers.js`,
`buildFeatureTraces()`, `center = body.position`; the Sun room passes
`{sun: [0,0,0]}`. So rule 5 is an extension of existing practice, not
new ground. On error: composition carries the parent's error onto the
child unchanged, so errors add and never cancel, and the parent-child
geometry stays exactly what JPL served. At the Sun's scale nothing can
show: the Moon's whole orbit is 0.0026 AU, under one pixel in a one-AU
frame. It can show only where a composed child is drawn beside a body
that is NOT on its chain, which is finding 3's case.

**5. One rule can replace the two kinds of "under", and the config
already holds both fields it needs -- but one object contradicts it.**
Every served object has a tree field, `parent`, and a frame field,
`center_slug` (the centre JPL served it around). A single rule covers
rules 1, 5, 6 and 7 at once: a thing can be drawn from centre C when
there is a chain of served centres from C down to it, and its place is
the sum of the served vectors along that chain (Moon in the Sun's view =
Earth-around-Sun plus Moon-around-Earth; an Earth-Moon Lagrange point =
Earth-around-Sun plus point-around-Earth; Charon = barycentre-around-Sun
plus Charon-around-barycentre). Composition climbs the tree and never
crosses it, which is finding 1 in one sentence. The contradiction:
Charon's `parent` is "pluto" but its `center_slug` is
"pluto_barycenter", and Pluto's own `parent` is "sun" though it is served
around the barycentre too. VERIFIED: `data/objects_config.json`, objects
`charon`, `pluto`, `pluto_barycenter`. HOW (a skill rule): make `parent`
the served centre for every orbiting body (Pluto and Charon under
pluto_barycenter, which is already the drawer's "Pluto" row), and keep
"listed under" as a separate drawer field for the neighbourhood groups.
With that, rule 1's "kind of child" needs no new field: a child is
orbiting when its parent is its served centre, and listed when it is
not.

**6. "Centre on the Sun" is undefined, because the website has two
Sun-centred rooms that differ in framing, epoch and content.** The Sun
room draws shells at today 00:00 UTC and frames whole shapes at 10
percent; the Solar System room draws bodies at the minute opened and
frames on positions at 20 percent, with no shells at all. VERIFIED:
`interactive.html`, `EXHIBITS.sun` (no `epochNow`, `halfRangeAu` 0.25,
features composed) and `EXHIBITS["solar-system"]` (`epochNow`,
`frameOnPosition`, `frameMargin` 1.2, compose comment "no features are
built, so no shells"). Tony's tree lists "Sun (shells; comets by type)"
UNDER "Solar system". QUESTION, Tony's (WHAT): is the Sun's shell room
the root itself with its shells unticked on arrival, or a node under the
root that a visitor enters? The trail line's first word ("Solar system
>") and rule 3's "returns to the Sun" depend on it.

**7. Rule 7's own example does not work in the root view today.** The
Solar System room builds no feature traces, so the Heliopause cannot be
ticked there beside Voyager 1; it lives in the Sun room. The mechanism
exists (finding 4), and the root's compose would call
`buildFeatureTraces` with every drawn body's propagated position, which
is rule 5 exactly. VERIFIED: `interactive.html`,
`EXHIBITS["solar-system"].compose`. Two things follow and neither is
decided: the root's 20-percent position framing against a 120-AU shell
(the skill's "anything larger than the frame goes to the drawer, not
dropped" is the Sun room's rule), and the Sun's 00:00 UTC epoch becoming
moot once its shells draw in a room that draws at the minute opened.

**8. Rule 6 reopens L-297, whose sizing rests on an epoch the Earth room
no longer uses.** L-297 found a Lagrange point fits none of the three
served shapes and sized a fourth, an `epoch_marker` placed at JPL's
position for the scene's epoch, "today 00:00 UTC ... the same instant"
as the cache's. The Earth room has since drawn at the minute opened
(`epochNow`, Tony's ruling of 2026-09-27). VERIFIED: ledger L-297;
`interactive.html`, `EXHIBITS.earth.epochNow`. The Moon is propagated
to that minute; a point fixed at midnight would lag it by the Moon's
motion since midnight, up to about 13 degrees of its orbit by the next
midnight (360 degrees over the served 27.3-day period). So the Earth-Moon
points need served positions through the day, not one marker, or the
L-297 design re-sized. The Sun-Earth points (L-294) are served around
the Sun and would be listed under Earth: a neighbourhood child by rule
1's words, drawable only from the root by finding 5's chain rule, which
is what rule 6 says ("drawn in the centre JPL serves it around").

**9. Step 1 of the build order has no writer.** No tool writes `parent`:
the objects mirror copies name, id, description, link, period and path
from the orrery's export and nothing else, and the config's rule is that
only two tools edit it, by an allow list. VERIFIED:
`tools/mirror_objects.py`, "WHAT IT WRITES"; interactive-exhibit, "Only
two tools write the served config". The orrery's own list has no parent
field either, and Phobos and Deimos carry no `key`, so the mirror cannot
link them (ledger L-514, "At the base"). VERIFIED: `celestial_objects.py`,
the Moon, Phobos and Deimos entries. QUESTION (HOW, a method a skill can
settle): the tree's edge is authored in the orrery entry and mirrored,
or in the config with a store_writer allow-list path. The neighbourhood
edges (which group sits under which planet) are curation -- Tony's, and
data, by L-489's ruling on compositions -- and belong on the rooms-section
rows as a field, not in a rule that guesses them from distances.

**10. Step 2 merges two drawers that the code keeps apart, and L-514 has
already ruled the merged shape for Mars.** A body room's drawer is built
from the traces' legend groups (shells) with `ssDrawer` null; the Solar
System room's is built from served rows (bodies) with group rows, Find,
and its own Reset. VERIFIED: interactive-exhibit, "The Solar System
room's drawer: bodies, not shells"; `gallery/solar_system_drawer.js`.
L-514's ruling 2 lists Mars fixed, then Phobos and Deimos, shells joining
later: one drawer holding both kinds. Three things a builder would guess:
which Reset a body centre gets (the Sun's and Earth's put back the
arrival; the Solar System room's puts back the served opening and folds
groups); whether the arrival block's one-off `moon: true/false` key
(`gallery/arrival.js`, legend group "moon") becomes a list of children by
slug; and where a child's row sits among shells (`drawer_order.js` orders
shells by where each begins, so a moon could slot by its distance). All
three are HOW questions for interactive-exhibit, not Tony's.

**11. The order is safe for existing rooms if the tree replaces the room
LIST and not the per-body compose.** The Earth room's picture is
Earth-specific code (`gallery/earth_geometry.js`, `composeScene`: the Sun
line, the day-night edge, the pole, the Moon's trusted arc); a Mars
centre will want its own. So `EXHIBITS` survives as per-centre compose
hooks keyed by slug, the addresses `?exhibit=sun` and `?exhibit=earth`
keep opening them, and index.html's cards keep working. The only
visible changes in step 2 are the trail line, the merged drawer, and
"Enter the <name> room" (`solar_system_drawer.js`, `WORDS.enter`)
becoming "Centre on <name>". VERIFIED. What must stay green: the
`documentation/smoke_*.js` checks, the `tools/headless` walks, the Earth
scene fixture (`tools/record_earth_scene.py`), and
`gallery_maintenance_run.py --live`'s `SERVED_FILES` if the page fetches
a new file (interactive-exhibit, "One check reads the file the browser
fetches"). Both rooms are Mode 5 targets, by "One chrome, many rooms".

**12. Four more things a builder would have to guess, with the answer I
would give each.** (a) A centre's address: `?exhibit=<slug>`, as rooms
are written today, so nothing already linked breaks (HOW). (b) When
"Centre on" is offered: when the served index holds the body's record
AND at least one object stored around it; the resolver already warns
when a centre has no record ("re-run the nightly builder", `resolver.py`
step 4b), so the button is read from `coverage_index.json`, never typed
(HOW). (c) A moon's trusted arc is capped at an eighth of its period
(gallery-assembler, `_TRUST_CAP_DIVISOR`): the Moon's is 3.4 days today
(VERIFIED, `objects.moon.trust.window_days`), Io's 0.22 days, and
Phobos's would be under an hour; whether a Mars centre draws that sliver
is Mode 5, Tony's eyes. (d) What the trail line's first word is, which
is finding 6.

**13. Rule 8 is sound and needs one thing drawn and one thing sourced.**
Look-toward needs a drawn target; in Earth's view the Sun is today a
direction line, derived from Earth's own served elements and negated
(`EARTH_DRIVER`, `_sun.dir`, `distAu`) -- one served answer turned round,
allowed by finding 5's chain rule, so a Sun marker at that distance is a
small addition. VERIFIED. The sentence about precession since 2000, if a
visitor reads it, is a factual claim and needs a source before it is
printed; the drawing itself computes the direction and types nothing
(Fetched vs Recalled). INFERRED.

## 3. The build order

Keep the four steps, with three changes. Step 1 shrinks to a data
correction and a writer: set `parent` to the served centre (Pluto and
Charon under the barycentre), add the neighbourhood field to the rooms
rows, and give Phobos and Deimos their orrery keys so the mirror can
link them (finding 9). Before step 2, take finding 1 (A or B) and
finding 6 (what the root is) to Tony, because the drawer and the trail
line cannot be built without them; then build step 2 with `EXHIBITS`
kept as compose hooks (finding 11). Step 3, Mars with its moons, stands
on L-514's four rulings. Step 4 should be preceded by its own builder
slice -- the second-centre fetch of an event window and a scene-level
window -- since without it no encounter can open (finding 2); and rule
2's flyby sentence should be struck before any encounter is designed
(finding 3). L-297 (the Lagrange points) is re-sized for the minute-opened
epoch and slots after Mars.
