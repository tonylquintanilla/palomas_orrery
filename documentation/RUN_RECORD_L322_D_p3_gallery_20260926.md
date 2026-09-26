# Run record -- L-322 Stage D, gallery patch 3: the magnetotail and the belts

**Built on gallery `c6000f03324fc6cdf1d192d0c1c77b91c10dd25f` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io and orrery
`43ba290b20ed17aee22a9bb7c121ff0b1a8fca3e` at
https://github.com/tonylquintanilla/palomas_orrery.** Both HEADs read live
with `git ls-remote` on 2026-09-26, at the start of the session and again
before the patch was written.

The patch is `patch_L322_D_p3_gallery_tail_belts_20260926.py`, run from the
gallery root and archived to the gallery's `documentation/`. It runs
before the orrery's patch D13 (see `RUN_RECORD_L322_D13_20260926.md`).

Rules this work ran under: protocol v3.69; provenance-discipline 2.19
(the loaded copy read 2.19, discharging v3.69's obligation),
interactive-exhibit 1.4, gallery-cache-builder 1.6, gallery-assembler 1.3,
safe-file-editing 1.11, agentic-pre-test 1.2, ledger-and-session-records
1.11. Every loaded copy was byte-identical to `skills/` at orrery
`43ba290b`.

Written for Tony, a retired professional engineer who is not a
programmer, and for the session that follows.

---

## 1. Rulings this session

- **The magnetotail is its own entry in the drawer** (Tony, 2026-09-26,
  option A of two). Option B, part of the Magnetopause row, would have left
  the tail's sources with nowhere to show in the i panel, which shows one
  row's sources, and GO on Magnetopause would have framed out to 220 Earth
  radii. Tony added: the two views, with the tail and without it, each get
  their own framing, which is what a separate row gives.
- **The words a visitor reads were shown to Tony before the build finished,
  and he said continue.** Two were shortened after that to fit the hover
  budget; section 4 names both.
- **The plan, with the orrery patch D13 added to it**, confirmed as
  recommended.

## 2. What the patch changes

- **`data/objects_config.json`.**
  - The `magnetotail` entry becomes a served shell: a name, a one-line
    description, an i-panel paragraph, a note, a source, a link, and
    pointer entries for the four tail rows (`flare_end`, `diameter`,
    `drawn_radius`, `drawn_end`) beside the existing `observed_extent`.
    Its colour and opacity are the magnetopause's, so the two read as one
    surface. `length_radii`, `base_radii`, `end_radii` and the old colour
    and opacity are gone; the `_declared` sentence is rewritten.
  - `observed_extent`'s source keeps only the reach; the 1983 abstract's
    figures for the end of widening and the diameter now sit with the 1985
    rows.
  - Earth's belts lose `belt_thickness` and `n_rings`; `_declared` says the
    ring count follows from the edge and peak rows.
  - The magnetic tilt's source sentence is corrected: the paper prints no
    tilt, the store computes it at five figures, and it shrinks by about
    0.049 degrees a year, not 0.05 per decade.
  - Earth's `orientation`: the pole's two numbers point at
    `EARTH_POLE_RA_J2000_DEG` and `EARTH_POLE_DEC_J2000_DEG` instead of
    `idealized_orbits.py`; the source names Horizons for the pole drawn
    and the IERS for the fallback, and says the IAU report was cited
    until today; a `rotation_period` pointer entry is added for
    `EARTH_SIDEREAL_ROTATION_PERIOD_H`.
  - The 14 `uncertainty` fields the mirror writes (section 3).
- **`gallery/feature_renderers.js`.**
  - The magnetotail, in `renderMagnetosphere`, drawn only if the
    magnetopause was. Its start is worked out from the served Shue rows at
    the served cut; rings run from there to the drawn end, with a ring
    added exactly at the flare end so the bend sits where the row puts it.
    It is stamped with its own shell key, `magnetotail`, so the arrival
    rule hides it on arrival like every other shell but the crust.
  - The belts: `evenBeltRings()`, the page's copy of the orrery's
    `_even_belt_rings()`, reading decimals to a thousandth as the orrery's
    `limit_denominator(1000)` does, capped at 25 rings. The peak ring is a
    second trace in the same drawer row, opacity 1.0 and twice the size;
    the info marker sits on it. A belt with no edges keeps a served
    thickness (Jupiter) or, with neither, is drawn as one ring with a
    warning. The 0.5 fallback is gone.
  - The magnetopause hover's sentence about where the drawing stops now
    says the boundary is drawn on as the magnetotail.
- **`gallery/earth_geometry.js`.** The axis hover states the period from
  the served row at its served count. Its panel source credits the sense
  of rotation to the IAU report's general definition (section 2, page 6)
  and its statement that Earth's rotation is direct (section 7, page 27),
  both read in the report this session, and adds the period's source. The
  module description no longer calls the frame angle the renderer's own
  IAU 2006 obliquity.
- **`tools/mirror_constants.py`.** `uncertainty` joins `value`, `unit` and
  `figures`. A null is never inserted, and an export before schema 4,
  which has no such key, leaves entries as they were.
- **`tools/test_mirror_constants.py`.** Case 17, the uncertainty field;
  case 18, Earth's pole served; case 9's link outside the store is
  Jupiter's pole now.
- **The three smoke checks.**
  - `smoke_earth_geometry.js` takes the magnetosphere and the period from
    the served cache, as it already took the pole of date, because the
    recorded payload predates them. It checks the tail as a shape (where it
    starts, where it bends, where it ends, round, the marker on it), the
    belts' rings against the orrery's answers, and the axis hover's period.
    Its `normal()` helper now picks three points that span a trace: with
    several rings in one trace, its old choice put three points on one
    radial line and read as a false 23-degree tilt.
  - `smoke_hover_budget.js` measures the room with the served
    magnetosphere, so the tail's hover is measured at all.
  - `smoke_display_figures.js` grades the tail line by line and the axis
    period against the served row, drops the retired sentences, and holds
    the rest to a re-recorded fixture,
    `documentation/fixture_hovers_L322d_p3_on_c6000f03.json`. The D7
    fixture is left in place, unreferenced.

## 3. How it was verified, in the sandbox

- **The whole gallery maintenance run: 16 of 16 gating checkers passed**,
  after the served cache's feature copies were refreshed from the config
  the way `derive_served()` copies them (the sandbox cannot reach
  Horizons; your real cache build replaces this step). The same result on
  a fresh clone of `c6000f03` with only the patch applied.
- **The patch reproduces the sandbox byte for byte** on a fresh clone,
  refuses a second run, and keeps CRLF on a working copy that has it.
- **Each new check was shown failing.** Tail radius off by one percent:
  four tail checks fail. Peak ring as faint as the others: both belts'
  peak checks fail. The axis sentence reworded: the period check fails.
  `uncertainty` removed from the mirror's fields: two mirror checks fail.
- **The mirror writes 14 fields and a second run writes none**: eight on
  Earth's radius (`"0.0001"`), the magnetopause's three coefficients, its
  standoff in Earth radii, kilometres and AU.
- **The exact-row print lines are unchanged.** `EXACT_ROWS_PRINTED.md` at
  orrery `43ba290b` lists ten gallery lines; after this patch the report
  still finds all ten with nothing broken. What it found new is section 5.
- **Hover sizes.** The tail's hover is 17 lines, at the ceiling; the outer
  belt's is 17; the axis hover's 17.
- **D5's cone cleanup** does not apply: the gallery draws no dipole cone,
  only the two spin-arrow heads on the axis.

## 4. The visitor-facing text

The magnetotail's hover, under its name:

    Earth's magnetic field, drawn out by the solar wind into a long tail on
    the night side.

    Spacecraft found the tail stops widening about 120 Earth radii behind
    Earth, plus or minus 10, and is about 60 Earth radii wide beyond there,
    plus or minus 5.
    That is about 770,000 km (0.0051 AU) and 380,000 km (0.0026 AU).
    The straight widening up to that point is our choice; the measurements
    give only its two ends.
    The drawing stops at 220 Earth radii, which is how far the spacecraft
    went, not where the tail ends.
    Drawn round, its average shape; at any moment it is often flattened.

The kilometre line was "... 770,000 km (0.0051 AU) behind Earth and
380,000 km (0.0026 AU) wide." when Tony saw it; "behind Earth" and "wide"
were dropped to bring the hover from 18 lines to the 17 allowed. The
sentence before it gives the order.

Its i-panel paragraph:

    The solar wind drags Earth's magnetic field out behind the planet into
    a long tail. Spacecraft crossing it far downstream found that it stops
    widening about 120 Earth radii behind Earth and is about 60 Earth radii
    across beyond there. ISEE-3 followed it out to 220 Earth radii, which
    is how far the spacecraft went rather than where the tail ends. The
    tail is drawn round, which is close to its shape on average; at any
    moment it is often flattened, in a direction set by the solar wind's
    own magnetic field, which keeps changing.

The belts' new sentence, both belts:

    The belt is one continuous region; its evenly spaced rings only mark its
    extent, and the brighter ring marks where it is most intense.

Tony saw a three-line version ("The belt is one continuous region. The
rings only mark its extent: they are evenly spaced from its inner edge to
its outer edge, and the brighter ring marks where the belt is most
intense."); it was shortened to two lines because the outer belt's hover
was 18. The edges it dropped are on the next lines of the same hover
("Measured extent: 3 to 7 Earth radii"). "Drawn 0.5 radii wide, a width
chosen for the picture." is gone.

The magnetopause's sentence: "That is where the drawing stops, not where
the surface ends: it widens down the tail without limit." became "Beyond
that angle the boundary is drawn as the magnetotail."

The axis hover: "This scene is one epoch: the axis is the line Earth turns
about; the turning itself is not shown, and no rotation period is stated
because none is served." became "Earth turns once every 23.93447 hours
measured against the stars. The turning is not animated, because nothing
on the crust marks a longitude to watch it by."

## 5. For the ledger, one row per class

- **Jupiter's belt thickness is a typed 0.5 with no source.** Served in
  `radiation_belts`, drawn by no room, and it has no edge rows to draw
  across. Waits for the braid; this build kept it rather than draw
  Jupiter's belts some new way unasked. The manifest and the previous
  handoff said "both `belt_thickness` entries"; this is the second one.
- **The recorded Earth scene is overlaid piece by piece.** Three checks now
  take the pole of date, the magnetosphere and the rotation period from
  the served cache because `documentation/payload_earth_scene.json` (a
  recording of 2026-09-08/09) predates them. It still carries the 9.6
  tilt and the old belt thickness. Extends the existing aging-payload row;
  a recapture would retire the overlays.
- **The tail's hover is at the line ceiling (17).** Anything added to it
  needs a line taken away.
- **There is no Wikipedia article for the magnetotail;** the link is the
  Magnetosphere article.

Carried, now done by this patch: L-311's gallery half; the axis period and
re-homed sources; the orientation source; the tilt sentence; the test at
line 373 (now case 9 and case 18); the mirror's docstring (three
`planet_poles` links).

## 6. Tony's run

(Append the patch output, the cache builder's last swap-log line, the
gallery maintenance run's summary, the live run, and what the phone
showed: the tail with and without framing, both belts, the axis hover, and
the Sun room.)

---

Session written September 2026 with Anthropic's Claude Opus 5.5.
