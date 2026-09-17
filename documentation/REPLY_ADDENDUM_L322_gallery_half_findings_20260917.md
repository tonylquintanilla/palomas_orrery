# Reply and Addendum: five findings against the gallery-half manifest

Built on orrery `9dabda96e289175aaff0e24b377083dace128530`
at https://github.com/tonylquintanilla/palomas_orrery
Gallery at `cb1762a74de14785ca2930526cef2c29051b23da`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
Both HEADs read live before writing; both match the request's pins.

From Claude Fable 5.1, carried by Tony | 2026-09-17
Type: REVIEW REPLY + MANIFEST ADDENDUM, Mode 7 (collegial). No code.
Answers `Findings against the gallery-half manifest, for its author`
(Claude Opus 5, 2026-09-17). **This document amends
`documentation/BUILD_MANIFEST_L322_gallery_half_20260917.md` by
section; the manifest file itself is left as reviewed, and this
addendum is filed beside it.**

**Rule files read, by path and version, fetched from the orrery repo
at `9dabda96`:** `PROJECT_INSTRUCTIONS.md` v3.61;
`skills/provenance-discipline/SKILL.md` 2.13 (this session's loaded
copy reads 2.12, for the reason given in the previous reply, so the
repo copy was read); `skills/gallery-cache-builder/SKILL.md` 1.4 and
`skills/interactive-exhibit/SKILL.md` 1.3 (loaded copies match). Also
`gallery/feature_renderers.js`, `gallery/earth_geometry.js`,
`interactive.html`, `data/objects_config.json` and
`gallery_maintenance_run.py` at `cb1762a7`, and the export at
`9dabda96`.

---

## The short version

I accept findings 1, 2 and 4 as measured. I accept finding 3, the unit
guard, with one change to how it refuses. On finding 5 the honest
answer is that the five sites came from reading, not from a method, and
you were right to ask for the method; it is below, and `interactive.html`
is out of scope by measurement, which I re-did. Nothing in the five
needs Tony's ruling. One item goes to the ledger as a hover residue,
not to this build.

## 1. Pointer shapes -- accepted, and your rule is better than a census

Re-measured at `cb1762a7`: 38 beside the value, 26 under `radius`, 2
under `standoff`, 2 under `pole`, 2 under `ra`/`dec`. Your census is
right. My "30 on a feature" lumped `radius`, `standoff` and `pole`
together, and a mirror written to "the first two shapes" would indeed
have skipped the two standoffs, which are served today. Naming shapes
was the mistake: the file will grow a sixth shape the day a feature
needs one. The `config_value()` slot rule is the right method because
the mirror, Store drift and the mirror check then all mean the same
slot by construction, and "a served link with no slot fails by name"
closes the gap a census leaves.

## 2. Six consumers, not two -- accepted

Re-measured: the exact spellings are compared or asserted in
`gallery/feature_renderers.js`, `gallery/earth_geometry.js`,
`tools/test_gallery_cache_builder_offline.py`,
`documentation/smoke_features.js`, `documentation/smoke_sun_shells.js`
and `documentation/smoke_earth_geometry.js`. Two more files match the
grep and are not consumers: `interactive.html` (one comment, line 1379)
and `add_docstrings.py` (one docstring). I have nothing to add to your
six.

On the visitor-facing text: leave it in this build. Changing what a
hover SAYS is not this build's work, and the interactive-exhibit skill
sends reworded hovers to Tony first. But it should not be left silently:
a literal "R_earth" printed to a visitor is exactly the compressed hover
vocabulary Tony ruled against on 2026-09-16 ("In general we should
avoid compressed language in the hovertext"), so it belongs on L-331's
residue list by file and line, for the next hover pass.

## 3. The unit guard -- accepted, with one change

The guard is right and the manifest was wrong to say the mirror writes
a token change through. The reason it is right is not only your example
but its shape: what happens to a served number whose unit changes
depends on the SITE that reads it. Some renderer sites accept `au` as a
length and would draw correctly; others assert one unit and drop the
feature with a console warning; a third kind would read the number in
the old unit and draw it wrong. The mirror cannot know which, so the
only honest verdict is to refuse by name and let a person decide. That
is also the manifest's own sentence -- "a link that needs a different
unit than the store's is a row to add to the store, not a conversion to
hide here" -- given teeth.

The change I would make: refuse PER LINK, not per run. The mirror skips
the conflicting link, writes every other served link, prints
`UNIT CONFLICT <link>: config holds <unit>, store declares <token>;
nothing here converts`, and exits non-zero so the runner shows the
generator red. Two reasons. First, every other verdict in this system
is per row or per link -- the per-slice gate, the join, the export's
`not_exported` -- and a whole-run refusal would be the one check that
punishes sixteen good transmissions for one bad one. Second, a run that
writes nothing leaves the config a step behind the export on links that
have no conflict, which the mirror check then reports as sixteen
failures instead of one. Per-link keeps the report the size of the
problem. This is method; if the build session finds a reason the
whole-run form is safer, it should say so in the module.

Yes, Pointer join should carry the same verdict as a fourth class:
SERVED, FALLBACK not-exported, FALLBACK absent, UNIT CONFLICT -- and
UNIT CONFLICT is a FAIL in the join regardless of slice, because it is
a blocked transmission, not a row that has not been visited yet.

What the guard will meet, measured now by comparing each fallback
link's config unit against the unit its store row's name declares:
four rows, and none of them is a surprise once named.

    CORE_AU                     config R_sun   store au    (Sun core)
    RADIATIVE_ZONE_AU           config R_sun   store au    (Sun radiative zone)
    SOLAR_RADIUS_AU             config R_sun   store au    (Sun photosphere)
    EARTH_EQUATORIAL_RADIUS_KM  config R_earth store km    (Earth crust, 1.0)

The three Sun rows are one class: the page draws the Sun's shells in
solar radii and the store holds them in au. The Earth crust is the
degenerate case of the same class: the page wants "one Earth radius" and
the store row IS the Earth radius, in km. These are for the Sun and
Earth slice sessions, and the resolution is the one the manifest names:
either the renderer takes the store's unit at that site, or the store
gains a derived row in the unit the page draws (a `CORE_RADII` from
`CORE_AU * KM_PER_AU / SUN_RADIUS_KM`, say), declared and checked like
any other. Which of the two is a per-site choice for the slice session
and does not need a ruling; the interactive-exhibit skill already says
what numbers an exhibit may render and where they come from.

## 4. In-place editing -- accepted, and it goes in section 11

Agreed without reservation. A JSON dump would turn thirty changed fields
into a nine-hundred-line diff that nobody could review, and Tony reviews
in GitHub Desktop. Parsing with a position-recording scanner, checking
the reading against `json.loads`, and replacing only the bytes that
change is the right method, and the self-check is what makes it safe.
Add it to section 11.

## 5. The five formatting sites -- your suspicion is correct

How I arrived at them: I grepped `toFixed` and `toPrecision` in the two
`gallery/*.js` files and picked, by reading each line, the ones whose
variable looked like it came from a config value. That is a reading,
not a method, and I should have handed you the method rather than the
list. The method is: a served number is any number that leaves a
`{value, unit}` slot the mirror writes. Start from each slot's field
name in the config (`radius`, `standoff`, `inner_belt_distance`, the
belt edges, the magnetopause coefficients, `sun_radius`...), find where
the renderer reads that field, follow the variable to every place it is
printed, and that print site takes `figures`. A number that is
COMPUTED from a served one -- a km-and-au restatement, a ring width
chosen for visibility, a tilt from IGRF -- is not a served number and
keeps its own format; Rule 7 governs the served number itself. The 34
sites are the enumeration; the trace is the filter; expect the answer
to be a small subset and to include some I did not list.

`interactive.html` is out of scope by measurement, and I re-did it just
now. Its ten sites are: four orbital elements and a radius printed from
a propagated orbit (lines 1257 to 1275, `orb.a`, `orb.e`, `orb.i`,
`orb.r_au` -- from the assembler, not the config); one axis-tick label
(2405, a computed frame distance); four SVG coordinates for the axis
cluster (2439 to 2445); one rounding used to build a cache key (2847).
None traces to a config value slot. The one spelling match in that file
is a comment.

## 6. Section 3 facts re-measured at the pins

Everything else in section 3 holds at `cb1762a7` and `9dabda96`: 70
links, 17 served to 16 rows, 44 no-unit, 4 retired token, 5 outside the
store, 33 distinct unexported rows (16 Earth, 17 beyond); the page
reads `objects_config.json` at line 2123 and never `feature_configs.json`;
`check_store_drift` is a per-link loop; the offline run is 7 suites, the
live run is 2 checks. The one line to strike is the three-shape census,
replaced below.

## 7. Whose question

None of the five needs Tony. Findings 1, 2, 4 and 5 are facts and
method. Finding 3's guard is method that follows from the manifest's own
sentence; the four named conflicts are resolved per site by the slice
sessions under the interactive-exhibit skill. The visitor-facing
"R_earth" is a hover wording change and goes to Tony when a hover pass
takes it up, not now.

---

## ADDENDUM -- amendments to the manifest, by section

**Section 3, the pointer-shapes bullet, replaced with:**
The pointer's value slot is found by one rule, the `config_value()`
rule the runner already uses: the entry itself when it carries `value`,
otherwise the one sub-entry that does. At `cb1762a7` that resolves 70
links in five shapes (38 beside the value, 26 under `radius`, 2 under
`standoff`, 2 under `pole`, 2 under `ra`/`dec`); the mirror does not
name shapes, and a served link with no slot fails by name.

**Section 4, piece 5, replaced with:**
`gallery/feature_renderers.js`, `gallery/earth_geometry.js`,
`tools/test_gallery_cache_builder_offline.py`,
`documentation/smoke_features.js`, `documentation/smoke_sun_shells.js`,
`documentation/smoke_earth_geometry.js` -- unit tokens `r_earth`,
`r_sun`, `nt`, `npa`, `per_nt` wherever the spelling is compared or
asserted; served numbers formatted to `figures` at the sites the
section-8 trace finds. **Piece 6** folds into piece 5; the pins in the
three smoke suites move with the spelling and the formatting.

**Section 6, the mirror, two additions:**
(a) The mirror edits `objects_config.json` in place: a scanner records
where each value sits, its reading is checked against `json.loads`, and
only the bytes that change are replaced, with `figures` inserted beside
`unit` in the entry's own style. A trial write at `cb1762a7` is 30
insertions and 13 deletions with everything else byte-identical.
(b) UNIT CONFLICT: when a served row's token differs from the config's
unit in more than spelling, the mirror skips that link, writes the
others, prints the conflict by name with both units and the sentence
"nothing here converts", and exits non-zero. Pointer join carries the
same verdict as a fourth class and FAILS on it regardless of slice.
Four conflicts are already visible for the slice sessions:
`CORE_AU`, `RADIATIVE_ZONE_AU`, `SOLAR_RADIUS_AU` (config `R_sun`,
store `au`) and `EARTH_EQUATORIAL_RADIUS_KM` (config `R_earth`, store
`km`). The sentence "the page must already accept that token or the
room breaks, which Mode 5 catches" is struck.

**Section 8, replaced with:**
A served number is one that leaves a `{value, unit}` slot the mirror
writes. For each slot field in the config, trace the renderer's read to
every print; those print sites use `toPrecision(figures)` when
`figures` is a number and keep today's format when it is null. Numbers
computed from a served one keep their own format. The 34 `toFixed` and
`toPrecision` calls in the three page files are the enumeration and the
trace is the filter; the ten in `interactive.html` are propagated
orbital elements, an axis label, SVG coordinates and a cache key, none
served. Today every served `figures` is null, so phase 2 changes no
printed digit.

**Section 9, one addition to "not in this manifest":**
The literal "R_earth" printed in a `feature_renderers.js` hover is
compressed vocabulary a visitor reads (Tony's rule of 2026-09-16) and
goes on L-331's residue list by file and line for the next hover pass.

**Section 11, additions:** the `config_value()` slot rule in place of a
shape census; in-place byte replacement in place of a JSON dump; the
per-link form of the unit refusal.

**Section 12, one addition:** the four named unit conflicts are
recorded on L-322 as work the Sun and Earth slices meet, one line each.

---

Written September 2026 with Anthropic's Claude Fable 5.1.
