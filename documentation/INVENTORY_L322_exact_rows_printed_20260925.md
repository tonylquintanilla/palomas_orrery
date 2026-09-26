# Inventory -- which exact rows a display prints, and how wide

**Built on orrery `de4eadc58e3de746183515dff422aaab3943fe6a` at
https://github.com/tonylquintanilla/palomas_orrery and gallery
`42a17abe16eebe5f03c790ad2a8f39f918c1ba7b` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.** Both
HEADs read live with `git ls-remote` on 2026-09-25.

**Type: DISCOVERY (reading only).** Nothing was changed and no width was
chosen. This lists what exists, so that the two sessions that act on it
start from the same list: gallery patch 3, which edits the Earth room's
hovers, and manifest section 6, which builds the `exact -- prints N`
field (provenance-discipline Rule 7, the exact row). Under The Braid,
discovery and remediation are kept apart; this is the first.

Rules: provenance-discipline 2.18 as installed; 2.19 is written but not
yet pushed, and changes only the rule's example.

Written for Tony, a retired professional engineer who is not a
programmer, and for those two sessions.

---

## 1. The answer in one paragraph

`constants_new.py` has 20 exact rows. Seven of them are printed by at
least one display, at 17 lines across the two repositories. The other 13
are used only in arithmetic. One of the seven, the solar wind pressure,
is printed differently by the two repositories: "2 nPa" in the orrery
and "2.0 nPa" in the gallery. Every gallery site chooses its width at
the call site, which is exactly what the exact-row rule forbids; every
orrery site does the same with a Python format code.

## 2. How the search was done

An "exact row" is a row whose `# Figures:` line begins `exact`, read
with `constants_rows.py`, the same reader the checkers use. There are 20.

**Orrery.** Every tracked `.py` file outside `documentation/`, except
`constants_new.py` itself, was searched for each of the 20 names in a
printing form: inside `{...}` in a formatted string, as the argument of
`_declared`, `_whole_figures` or `_with_uncertainty`, after `%`, or
inside `str(...)` or `format(...)`. For every row with no hit, each
remaining use was then read by hand, to catch a value printed through a
local name. None was.

**Gallery.** The page gets `constants_new.py` values in two ways only:
pointer entries in `data/objects_config.json` (a node carrying
`orrery_constant`), and the two rows served as `frame_constants`. Every
pointer to an exact row was followed to the line that prints it. The two
frame rows, `KM_PER_AU` and `EARTH_OBLIQUITY_J2000_DEG`, are used only
in arithmetic on the page.

**Not searched:** an exact row's value typed into text as words or
digits, rather than read from the row. Some were seen in passing
(section 5), but that class was not enumerated.

## 3. The seven exact rows a display prints

Each entry gives the row, its value as typed, then every line that
prints it, with the width that line chooses and what it prints today.

1. **`EARTH_SOLAR_WIND_PRESSURE_NPA`** (2.0, declared pending)
   - orrery `earth_visualization_shells.py` line 964, the checkbox
     tooltip: `:g`, prints "2".
   - orrery `earth_visualization_shells.py` line 1147, the magnetosphere
     hover: `:g`, prints "2".
   - orrery `earth_visualization_shells.py` line 1231, the bow shock
     hover: `:g`, prints "2".
   - gallery `gallery/feature_renderers.js` line 2142, the magnetopause
     hover: one decimal, prints "2.0".
   - gallery `gallery/feature_renderers.js` line 2217, the bow shock
     hover: one decimal, prints "2.0".
   - **The two repositories disagree** on this one row. A print count
     on the row settles it for both.
2. **`EARTH_SOLAR_WIND_BZ_NT`** (0.0, declared pending)
   - gallery `gallery/feature_renderers.js` line 2141, the magnetopause
     hover: one decimal, prints "0.0".
   - The rule says a zero prints as 0. The orrery does not print it.
3. **`EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG`** (120.0, declared)
   - gallery `gallery/feature_renderers.js` line 2144, the magnetopause
     hover: no decimals, prints "120". The skill's example from 2.19.
   - The orrery uses it only to stop the drawing.
4. **`EARTH_BOW_SHOCK_CUT_ANGLE_DEG`** (105.0, declared)
   - gallery `gallery/feature_renderers.js` line 2219, the bow shock
     hover: no decimals, prints "105".
   - The orrery does not use it; its bow shock is drawn by the shared
     shape code.
5. **`EARTH_VAN_ALLEN_OUTER_RADII`** (4.5, a declared construction, the
   midpoint of the L = 4 to 5 band)
   - orrery `earth_visualization_shells.py` line 1293, the outer belt
     hover: `:g`, prints "4.5".
   - orrery `earth_visualization_shells.py` line 1299, the same hover,
     "our midpoint of it": `:g`, prints "4.5".
   - orrery `shell_configs.py` line 2318, the outer belt's tooltip copy
     (dead data, kept in step with its live twin): `:g`, prints "4.5".
   - gallery `gallery/feature_renderers.js` lines 1018, 1025 and 1028,
     the belt hover's three forms: one decimal, prints "4.5".
   - Both repositories agree today.
6. **`EARTH_LEO_LOWER_ALTITUDE_KM`** (200.0, declared, a drawing floor)
7. **`EARTH_LEO_UPPER_ALTITUDE_KM`** (2000.0, measured, figures exact)
   - These two are printed together on each line.
   - orrery `earth_visualization_shells.py` line 1514, the LEO hover:
     `:,.0f`, prints "200" and "2,000".
   - orrery `shell_configs.py` line 2329, the LEO tooltip: `:,.0f`,
     prints "200" and "2,000".
   - gallery `gallery/feature_renderers.js` line 1893, the shell hover's
     altitude line: the km printer falls back to no decimals when the
     row is exact, prints "200 km" and "2,000 km", and then adds an AU
     figure at three significant figures, for example "0.00134 AU".
   - Both repositories agree on the kilometres. The AU figure is a
     conversion of an exact row printed at a width chosen by the
     printer; section 6 should decide whether the print count governs
     it too.

Seventeen printing lines in all. Eight are in the orrery: six in
`earth_visualization_shells.py` and two in `shell_configs.py`. Nine are
in `gallery/feature_renderers.js`.

## 4. The thirteen exact rows no display prints

Used in arithmetic only:
`KM_PER_AU`, `S_PER_HOUR`, `ARCSEC_PER_DEG`, `DEG_PER_RAD`,
`M3_PER_KM3`, `GM_SUN_SI`, `EARTH_POLE_RA_J2000_DEG`,
`EARTH_POLE_DEC_J2000_DEG`, `EARTH_OBLIQUITY_J2000_ARCSEC`,
`EARTH_OBLIQUITY_J2000_DEG`, `EARTH_SOLAR_WIND_SPEED_KM_S`,
`EARTH_MAGNETOTAIL_DRAWN_RADIUS_RADII`,
`EARTH_MAGNETOTAIL_DRAWN_END_RADII`.

Two notes on these:
- `KM_PER_AU` appears once in a print statement, at
  `export_orbit_cache.py` line 385, but that is a tool's console log, not
  a display a visitor sees.
- The two drawn tail rows are not printed on purpose: the magnetosphere
  hover prints the measured rows (the flare end, the width, the observed
  reach) and says the drawing's rules in words.

Under the rule, these thirteen carry no print count.

## 5. Found in passing, not enumerated

- **Typed copies of exact values in gallery text.** The two LEO entries
  in `data/objects_config.json` type the values into words: their names
  read "(200 km)" and "(2,000 km)", and their `about` text reads "200 to
  2,000 km". These do not follow the rows if the rows change. The class
  was not searched for.
- **Two gallery comments cite the Rule 7 that 2.17 replaced.**
  `gallery/feature_renderers.js` lines 201 and 402 say a display "may
  show FEWER figures" than the row declares. Since provenance-discipline
  2.17 a display prints the declared count, and a number that reads as
  too many figures is fixed on the row. The code near line 402 still
  shortens the AU figure to three, which is the old rule in action.

## 6. For the two sessions that act on this

- **Gallery patch 3** edits the magnetopause and bow shock hovers, where
  five of the gallery's nine lines are (2141, 2142, 2144, 2217, 2219). It
  should leave their widths alone unless section 6 has landed, and not
  add new call-site widths for exact rows.
- **Manifest section 6** has seven rows to give a print count and
  seventeen lines to move onto it, both repositories together. The
  search in section 2 can be re-run at its start to confirm the list has
  not grown.

---

Written September 2026 with Anthropic's Claude Opus 5.5.
