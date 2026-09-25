# Handoff -- L-322 Stage D: Earth's pole of date built in the orrery; the rest of Stage D to build

**Built on orrery `fb8d927e1581f6ad2fe49aa04a8d30d50e7f8d71` at
https://github.com/tonylquintanilla/palomas_orrery and gallery
`d037929110878de85a172ce955c15f24d2298902` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.** Both
HEADs read live with `git ls-remote` on 2026-09-24. `fb8d927e` is D5
(`ee850d0b`) plus a commit carrying the pole cache and the osculating
cache. `d0379291` is a nightly cache build; its swap succeeded first
time, and the gallery's offline and live maintenance runs both passed
with the export pinned at orrery `ee850d0b`.

**Type: BUILD.** **Opens from**
`documentation/BUILD_MANIFEST_L322_D_earth_pole_20260922.md`, rev 3.
**Companion records:** `documentation/RUN_RECORD_L322_D2_20260923.md`
through `RUN_RECORD_L322_D5_20260923.md`, one per patch, each with the
tests it ran and Tony's own run appended. **Supersedes** nothing; the
manifest stays the contract for what remains.

**Rules this work ran under:** provenance-discipline 2.18 (the loaded
copy byte-identical to `skills/` at `bba21459`), ledger-and-session-
records 1.11, horizons-orbital-mechanics 1.1, orrery-coding-conventions
1.9, safe-file-editing 1.11, agentic-pre-test 1.2, and protocol v3.68 in
the repo. The Project's pasted instructions were still v3.67 on
2026-09-23; Tony may want to paste v3.68 in.

Written for Tony, a retired professional engineer who is not a
programmer, and for the session that builds the rest.

---

## 1. What was built, and how each piece was verified

Four patches in the orrery, each run by Tony, each followed by the
orrery maintenance run and a push. Every patch was tested first on a
throwaway copy in the sandbox. Verified means Tony's run or push
confirmed it; each push was checked by fingerprint against what the
patch was built to produce.

- **D2 (`8fffbe1d`).** New rows in `constants_new.py`: Earth's sidereal
  rotation period (23.93447 hours, derived from the rotation rate through
  an exact `S_PER_HOUR`), the two fallback pole rows (the frame's own
  axis), and the frame's defining angle, `EARTH_OBLIQUITY_J2000_ARCSEC`
  = 84381.448, whose row says in words it is not Earth's tilt. The
  `planet_poles` dict moved into `constants_new.py`. Four unit tokens.
  The two conversion rows are sourced to NIST SP 811. Verified: Tony's
  maintenance run, "Constants change" red on the expected lines only.
- **D3 (`1319e496`).** `earth_pole_of_date.py`: fetches Earth's north
  pole for the plot's date (Horizons observer quantity 32, target 399,
  from the Sun) and the Earth-Moon barycenter's osculating orbit (target
  3 about the Sun), caches both in `data/earth_pole_cache.json`, and
  computes the tilt as the angle between them. Earth's axis, dipole cone
  and belts point along the pole of date. The axis hover prints the tilt
  with its date. Falls back to the frame's axis, and says so, when
  Horizons cannot be reached. `test_earth_pole_of_date.py`, 14 offline
  checks, in the maintenance run. Verified: Tony's plot of 2026-09-23
  showed 23.43814 degrees, 0.05 arcseconds from ERFA's true tilt.
- **D4 (`50343e03`).** Tony's ruling, "auto scale should show any
  rendered feature": the Auto cube for a center body is the larger of
  twice the outermost sphere shell and 1.2 times the reach of every
  feature drawn, except the Sun-direction arrow, which is instead fitted
  inside the cube. The live check judges against ERFA's true tilt with
  a 1-arcsecond allowance. The hover names "the Earth-Moon barycenter,
  the gravitational center of the Earth-Moon system" (Tony's wording).
  Two dashboard buttons. Verified: Tony's plot on Auto showed the whole
  axis and cone and their hovers.
- **D5 (`ee850d0b`).** Earth's dipole cone hover: the tilt prints once,
  from the row; the typed centre offset (0.085 Earth radii, 540 km,
  22 N 140 E) is removed and the cone starts at Earth's centre; plain
  words replace "the honest sweep"; every cone hover wraps long lines.
  Verified: Tony's plot.

**Tony's live check, 2026-09-24, the measurements the gallery half
needs.** Tilt minus ERFA's true obliquity: -0.25, +0.11, +0.06, +0.02
and -0.19 arcseconds for 2000-01-01, 2026-09-01, 2026-09-24, 2050-01-01
and 2100-01-01. The monthly wobble of Earth's own orbit (target 399)
against the barycenter's: -7.57 to +7.87 arcseconds across September
2026, a spread of 15.43. That measurement replaces the manifest's
recalled estimate of about 8 arcseconds each way.

## 2. Discrepancies surfaced

- **Rev 3's worked case used Earth's own orbit.** The ruling moved the
  tilt to the barycenter's orbit; the build uses target 3 throughout.
- **The Auto scale cut off anything past the outermost sphere shell**,
  including the axis and cone tips and their hover markers. Found when
  Tony saw no hover; fixed in D4. It predated Stage D.
- **Earth's dipole centre offset was drawn wrong in shape**: the whole
  offset along the spin axis, while the hover said it points mostly
  sideways. The offset had no source. Removed in D5; see section 4.
- **The provenance scanner went from 293 to 295 in D5, and both are
  Mercury's.** Two Mercury strings in `PLANET_DIPOLE` (its offset note
  and its tilt note) had counted as cited only because Earth's
  `# Source:` line sat inside the scanner's 30-line lookback; D5's new
  lines moved it out. They were always uncited.
- **provenance-discipline 2.18's worked example** says the obliquity
  prints 23.439291 degrees. Rev 3 withdrew that; the skill text is stale
  on this point and should change at its next bump.
- **Two patch files are in the orrery's root folder**, not
  `documentation/`: `patch_L322_D_4_orrery_autoscale_and_live_check_20260923.py`
  and `patch_L322_D_5_orrery_earth_cone_hover_20260923.py`. They are
  committed there. Move both into `documentation/`.

## 3. Open decision for Tony

- **The Sun on Auto.** With its inner shells, the Sun's view now opens
  about 31 times wider (its half-width goes from 0.0093 AU to 0.29 AU),
  because its rotation axis is drawn 52 solar radii long
  (`half_len_frac` 50 in `PLANET_ROTATION`). Mercury with every shell
  opens about 9 times wider, set by its sodium tail. Both follow the
  ruling literally. Whether the Sun's axis should be drawn shorter is a
  drawing choice for Tony's eye, not yet made.

## 4. For the ledger, one row per class

- **L-311: DONE when the gallery half lands** (manifest section 8). The
  orrery half of it is done.
- **L-325 and L-342: close**, per manifest section 8, Tony's rulings of
  2026-09-22.
- **Earth's eccentric dipole offset**, to source from Koochak and
  Fraser-Smith (2017), Earth and Space Science 4, 626,
  doi:10.1002/2017EA000280, or from IGRF-13's degree-2 coefficients
  with a sourced formula. The publisher's site refused this session as
  a bot. Drawing it also needs Earth's rotation phase, which the orrery
  does not model.
- **Other bodies' cone hovers**: tilts printed as a rounded "~",
  typed offsets, and radius abbreviations (R_M, R_J, R_S). Mercury,
  Jupiter and Saturn, each in its own slice.
- **The scanner's proximity rule** can count a string as cited by a
  neighbour's source.
- The classes in manifest section 7 stand as written.

## 5. What remains of Stage D, in the order to build it

Each piece has its governing sections in the manifest. The next
session re-anchors both repositories and confirms its loaded skills
before starting.

1. **The gallery half (manifest section 5, rev 3).**
   - `tools/gallery_cache_builder.py` fetches Earth's pole (quantity 32,
     target 399) and the barycenter's osculating orbit (target 3 about
     the Sun) at the epoch it already uses, and serves both with source
     blocks. The tilt is derived in the builder and served with both
     inputs named; the page prints it and does not compute it.
   - The builder's geometry must match `earth_pole_of_date.py`. Test it
     against the same ERFA check, and against a fixture taken from a
     real response: `data/earth_pole_cache.json` in the orrery holds two
     real days (2026-09-23 and 2026-09-24) with their source blocks.
   - `poleBasis` reads the served pole. `KM_PER_AU` and the obliquity
     typed at `gallery/feature_renderers.js` lines 70 and 74 are
     deleted; a missing row is a page warning, never a remembered
     number.
   - The axis hover in `gallery/earth_geometry.js`: re-homed sources, the
     sidereal period from the row, the tilt of date with its date, and
     the barycenter wording the orrery uses.
   - The unused magnetotail numbers and both belts' `belt_thickness` in
     `data/objects_config.json` are deleted; the magnetic-tilt source
     sentence's factor-of-ten rate is corrected;
     `tools/test_mirror_constants.py` line 373 expects SERVED.
   - The gallery's own dipole cone hover, if it has one, gets D5's
     cleanup.
   - The cache is rebuilt after the config change.
2. **The orrery's magnetosphere (manifest section 4.3).** The five
   numbers chosen by eye in `earth_visualization_shells.py` are replaced
   by the Shue surface and a tail from Slavin et al. (1983), read by the
   builder at ntrs.nasa.gov/citations/19830066648. The belts spread
   across their served edges. The gallery then draws the same tail.
3. **How exact rows print (manifest section 6).** Each of the twelve
   exact rows states its print count on its `# Figures:` line, the
   checker refuses a count larger than the literal's digits, the export
   carries it, and `fmtServed` prints by it. Every affected hover is
   listed before and after for Tony's Mode 5 look.

Order note: 1 and 2 both change the gallery's Earth room, so the tail
can be built once in the gallery if 2 goes first. The designer's call.

## 6. Tony-actions

- (do) Move the D4 and D5 patch files from the orrery root into
  `documentation/`, and file this handoff there.
- (do) Paste protocol v3.68 into the Project's instructions if it is
  not there yet.
- (decide) The Sun's Auto view, section 3, whenever convenient.

---

Session written September 2026 with Anthropic's Claude Opus 5.5.
