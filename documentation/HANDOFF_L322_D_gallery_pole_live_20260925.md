# Handoff -- L-322 Stage D: gallery pole live, phone tap lag fixed; the orrery magnetosphere next

**Built on orrery `62e938569382120e24373c14a98e5d85d1d36971` at
https://github.com/tonylquintanilla/palomas_orrery and gallery
`ce09f789921521b49643290015af6cd1ba21e038` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.** Both
HEADs read live with `git ls-remote` on 2026-09-25.

**Type: BUILD.** **Opens from**
`documentation/BUILD_MANIFEST_L322_D_earth_pole_20260922.md`, rev 3,
section 4.3, as amended by the two rulings in section 2 below.
**Companion records:** `RUN_RECORD_L322_D6_20260924.md`,
`RUN_RECORD_L322_D7_20260925.md`, `RUN_RECORD_gallery_tap_lag_20260925.md`,
each with Tony's run appended. **Supersedes**
`HANDOFF_L322_D_orrery_pole_built_20260924.md` for what remains.

**Rules this work ran under:** protocol v3.68; provenance-discipline 2.18,
gallery-cache-builder 1.6, gallery-assembler 1.3, interactive-exhibit 1.4,
horizons-orbital-mechanics 1.1, safe-file-editing 1.11, all eleven loaded
copies byte-identical to `skills/` at `fb8d927e`, checked at session start.

Written for Tony, a retired professional engineer who is not a
programmer, and for the session that builds the orrery magnetosphere.

---

## 1. What was built, and how each piece was verified

All three are pushed, each run by Tony, each followed by the offline and
live maintenance runs (all gating checkers passed every time).

- **D6, gallery `d892ed6e`: the cache builder serves Earth's pole and tilt
  of date.** It fetches Earth's north pole for the day (Horizons quantity
  32, target 399) and the Earth-Moon barycenter's orbit (target 3), works
  out the tilt with `tools/pole_of_date.py` (the orrery's geometry,
  copied), and serves both with their sources as `pole_of_date` in
  `coverage_index.json`. It also serves `frame_constants`: `KM_PER_AU` and
  `EARTH_OBLIQUITY_J2000_DEG`, read from the constants export. A structural
  check (`#P`) refuses a swap whose tilt is not what its own inputs give.
  New test `tools/test_pole_of_date.py`, 11 checks, run by the maintenance
  run as "Pole of date". Verified: Tony's build served 23.43816 degrees
  for 2026-09-25, 0.053 arcseconds from ERFA.
- **D7, gallery `199b8d9f`: the page reads the served pole and frame
  rows.** `gallery/feature_renderers.js` no longer types `KM_PER_AU` or
  the obliquity; a missing row is a warning, never a remembered number.
  The Earth room draws the pole of date for the axis, equator,
  geostationary ring and belts alike, and the axis hover prints the served
  tilt with its date. The Sun, Jupiter and Saturn draw as before (largest
  coordinate shift two parts in a hundred million; no hover changed).
  Verified: Tony's phone, two screenshots.
- **Tap lag, gallery `ce09f789`.** A marker tap opened Plotly's hover box,
  which took about 12 seconds to close (Tony's measurement). Cause, read
  from Plotly 2.35.2's source and measured headless: on a touch screen
  Plotly re-sends its click on every redraw while the point stays picked,
  and the page re-framed on each click, which redrew, which clicked again
  (127 clicks and 63 re-framings in 10 s). Fixed in `interactive.html`:
  one focus per press, and every new press drops Plotly's pick itself.
  Verified: Tony's phone, both rooms, "all correct".

## 2. Rulings this session

- **Order (Tony, 2026-09-25).** The orrery magnetosphere (old item 2) is
  built BEFORE gallery patch 3, so the sourced tail's rows exist and patch
  3 draws the same tail in the gallery at the same time as its other
  clean-ups. The tail is built once.
- **The tail's sources (Tony, 2026-09-25), replacing manifest 4.3's
  choice.** Read this session, not recalled:
  - **Slavin, Smith, Sibeck, Baker, Zwickl and Akasofu (1985)**, J.
    Geophys. Res. 90:10875, doi:10.1029/JA090iA11p10875, abstract (read on
    the publisher's abstract page through a search result; the page itself
    refuses bots): flaring ceases on average at |X| = 120 +/- 10 Earth
    radii; low-latitude tail diameter 60 +/- 5 Earth radii at |X| = 130 to
    225, from 756 magnetopause crossings. **Use this for the flare end and
    the diameter.** With stated uncertainties, Rule 3 decides the figures.
  - **Slavin, Tsurutani, Smith, Jones and Sibeck (1983)**, Geophys. Res.
    Lett. 10:973, doi:10.1029/GL010i010p00973, abstract fetched at
    ntrs.nasa.gov/citations/19830066648: flaring ceases at 100 to 120
    Earth radii; the tail keeps its near-Earth structure out to X = -220.
    **Use this only for the 220 reach**, which is already the store row
    `EARTH_MAGNETOTAIL_OBSERVED_RADII`.
  - **A misprint in the 1983 abstract**, to be quoted on the row as
    printed: "Beyond X = -100 to -1200 earth radii the tail diameter ...
    nearly constant at ... approximately 60". Read as -120, because the same
    abstract puts the end of flaring at 100 to 120. Do not correct it
    silently.
  - Consequence for manifest 4.3: the declared construction "which point
    in 100 to 120 the flare stops at" is gone. The flare end is the 1985
    measured value, 120, with its +/- 10 in the hover. Two declared
    constructions remain, each a stated rule on its row: the radius grows
    in a straight line from the magnetopause cut to the flare end, and the
    drawing ends at the 220 row, which the hover says is how far the
    spacecraft went, not where the tail ends.

## 3. What remains of Stage D, in order

1. **The orrery's magnetosphere (manifest 4.3, amended above).**
   - New rows in `constants_new.py`: the flare end (120, +/- 10) and the
     tail diameter (60, +/- 5), each sourced to Slavin et al. (1985), plus
     the declared constructions as rows with their reasons.
   - `earth_visualization_shells.py`: the five numbers chosen by eye (the
     12 and 10 widths, the tail's 100, 15 and 25; manifest 4.3 gives the
     lines at the manifest's base) are removed. The orrery draws the Shue
     surface from the store rows, cut at
     `EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG`, as the gallery room already does,
     and adds the sourced tail. The tail's starting radius is computed from
     the Shue surface at the cut, not typed. The hover's "an approximation
     of the shape, not the model's own" goes.
   - The belts: `belt_thickness` removed; each belt's rings spread across
     its served edges, the peak ring brighter.
   - Load agentic-pre-test before delivering; the xvfb run and the
     live-dispatch smoke test apply (the orrery's shell dispatch map is in
     orrery-coding-conventions).
2. **Gallery patch 3 (manifest section 5, the rest).** The gallery draws
   the same tail from the served rows; the unused tail numbers and both
   `belt_thickness` in `data/objects_config.json` deleted, the belts spread
   across their edges; the axis hover's sidereal period from the row (with
   a pointer entry for it), re-homed sources, and the "no rotation period
   is stated because none is served" sentence replaced; Earth's
   orientation source string names Horizons; the magnetic-tilt source
   sentence's factor-of-ten rate corrected; `tools/test_mirror_constants.py`
   line 373 expects SERVED; D5's cone cleanup if the gallery draws a cone;
   the cache rebuilt, because the config changes.
3. **How exact rows print (manifest section 6).** Unchanged from the
   previous handoff.

## 4. For the ledger, one row per class

- **The phone tap lag** -- fixed at `ce09f789`; record it as DONE. L-344
  is taken; the next free handle at orrery `62e93856` was L-363.
- **Phone behaviour of the rooms has no automated check.** The tap-lag
  loop was found and measured only in a headless browser with WebGL, which
  the maintenance run does not have.
- **The hover budget check can pass blind.** Its only floor is "at least
  one hover"; with the frame rows missing it measured 2 of 96 and passed.
  D7 made it fail on missing frame rows; the weak floor remains.
- **A recorded payload is aging.** `documentation/payload_earth_scene.json`
  (2026-09-08) predates the pole of date and carries the magnetic tilt as
  9.6 where the served cache has 9.4105.
- **The cache builder types its own `KM_PER_AU`** beside the served row
  from the export. Equal today; nothing checks they stay equal.
- **The maintenance routine pulls the constants export after the build**,
  so the served `frame_constants.orrery_sha` names the export from before
  that pull. Same values; the routine could pull first.
- **L-311** -- DONE when gallery patch 3 lands. L-325 and L-342 close per
  manifest section 8 (carried from the previous handoff).
- The previous handoff's other classes stand: Earth's eccentric dipole
  offset, other bodies' cone hovers, the scanner's proximity rule, and
  provenance-discipline 2.18's stale worked example (23.439291).

## 5. Tony-actions

- (do) File this handoff and the three run records in the orrery's
  `documentation/`, and the two gallery patch scripts and the tap-lag
  patch in the gallery's `documentation/`.
- (do) File the tap-lag ledger row (section 4).
- (decide) The Sun's Auto view, carried from the previous handoff.

---

Session written September 2026 with Anthropic's Claude Opus 5.5.
