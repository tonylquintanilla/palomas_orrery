<!-- Doc-Kind: generated | Which exact rows of constants_new.py a display prints, and where, in the orrery and the gallery; rebuilt by exact_rows_report.py. Do not hand-edit. -->
# Exact Rows Printed

Rebuilt by `exact_rows_report.py` on every orrery maintenance run. An exact row is one whose `# Figures:` line begins `exact`: a definition or a stated rule, not a measurement. provenance-discipline Rule 7 says a display prints such a row by a print count the row states, never by a width chosen where it is printed. This report lists every place a display prints one, with the code on that line, so the width it uses can be read.

## Summary

- 40 exact rows in `constants_new.py`.
- 12 printed by at least one display: `SUN_RADIUS_KM`, `EARTH_LEO_UPPER_ALTITUDE_KM`, `EARTH_VAN_ALLEN_OUTER_RADII`, `EARTH_SOLAR_WIND_PRESSURE_NPA`, `EARTH_SOLAR_WIND_BZ_NT`, `EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG`, `EARTH_BOW_SHOCK_CUT_ANGLE_DEG`, `INNER_CORONA_RADII`, `OUTER_CORONA_RADII`, `HELMET_CUSP_RADII`, `INNER_LIMIT_OORT_CLOUD_AU`, `OUTER_OORT_CLOUD_AU`.
- 54 printing lines: 39 in the orrery, 15 in the gallery.
- Gallery pointers to exact rows with no PRINTS entry (NOT FOLLOWED): 0.
- Gallery pointers to exact rows read only to place a drawing (DRAWN, not printed): 12: `SUN_RADIUS_KM`, `ROCHE_LIMIT_DRAWN_RADII`, `GALACTIC_NORTH_POLE_RA_J2000_DEG`, `GALACTIC_NORTH_POLE_DEC_J2000_DEG`, `OUTER_OORT_CLOUD_AU`, `DE430_TERRESTRIAL_POSITION_PLACE_KM`, `EARTH_MAGNETOTAIL_DRAWN_RADIUS_RADII`, `EARTH_MAGNETOTAIL_DRAWN_END_RADII`, `EARTH_POLE_RA_J2000_DEG`, `EARTH_POLE_DEC_J2000_DEG`, `DE430_JUPITER_SATURN_POSITION_PLACE_KM`, `DE430_URANUS_NEPTUNE_PLUTO_POSITION_PLACE_KM`.
- PRINTS or DRAWN entries that no longer match a pointer or their line (BROKEN): 1: `sun_structures/photosphere` -> `fmtServed(cfg.radius.value, sunF`.

## Printed by the count

Rule 7: each printed exact row states a print count, each orrery line prints it through `exact_text()` or `row_text()`, and the gallery serves the count beside it. **PASSING: 12 rows, every one counted, on 54 lines.**

- `SUN_RADIUS_KM`: prints 4
- `EARTH_LEO_UPPER_ALTITUDE_KM`: prints 4
- `EARTH_VAN_ALLEN_OUTER_RADII`: prints 2
- `EARTH_SOLAR_WIND_PRESSURE_NPA`: prints 1
- `EARTH_SOLAR_WIND_BZ_NT`: prints 1
- `EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG`: prints 3
- `EARTH_BOW_SHOCK_CUT_ANGLE_DEG`: prints 3
- `INNER_CORONA_RADII`: prints 1
- `OUTER_CORONA_RADII`: prints 2
- `HELMET_CUSP_RADII`: prints 1
- `INNER_LIMIT_OORT_CLOUD_AU`: prints 1
- `OUTER_OORT_CLOUD_AU`: prints 1

## Printed

### `SUN_RADIUS_KM`

- orrery `solar_visualization_shells.py` line 202: `f" ({row_text('SUN_RADIUS_KM', 'au')} to {row_text('CHROMOSPHERE_TOP_KM', 'au')} AU).<br>"`
- orrery `solar_visualization_shells.py` line 204: `f"{exact_text('SUN_RADIUS_KM', grouping=True)} km in radius --<br>"`
- orrery `solar_visualization_shells.py` line 572: `f"* Including both the Convective Zone and the Photosphere, the radius is from {row_text('RAD...`
- orrery `solar_visualization_shells.py` line 1053: `f"* Including both the Convective Zone and the Photosphere, the radius is from {row_text('RAD...`

### `EARTH_LEO_UPPER_ALTITUDE_KM`

- orrery `earth_visualization_shells.py` line 1521: `f"Low Earth Orbit (LEO) is the region from {row_text('EARTH_LEO_LOWER_ALTITUDE_KM')} km to {e...`
- orrery `earth_visualization_shells.py` line 1602: `f"Altitude range: {row_text('EARTH_LEO_LOWER_ALTITUDE_KM', grouping=True)} km to {exact_text(...`
- orrery `shell_configs.py` line 2378: `f"Low Earth Orbit (LEO) is the region from {row_text('EARTH_LEO_LOWER_ALTITUDE_KM', grouping=...`
- gallery `gallery/feature_renderers.js` line 2947 (config `/objects/1/features/earth_orbital_zones/leo_outer/altitude`): `kmAndAu(km.altitudeKm, km.altitudeFigures)) + "<br>";`

### `EARTH_VAN_ALLEN_OUTER_RADII`

- orrery `earth_visualization_shells.py` line 1382: `f"the poles, and they are thickest at L = {exact_text('EARTH_VAN_ALLEN_OUTER_RADII')}, about ...`
- orrery `earth_visualization_shells.py` line 1392: `f"the L = {_band_low} to {_band_high} band; the drawn {exact_text('EARTH_VAN_ALLEN_OUTER_RADI...`
- orrery `shell_configs.py` line 2358: `f"{exact_text('EARTH_VAN_ALLEN_OUTER_RADII')} Earth radii out (doi:10.1029/2024JA033504).\n"`
- gallery `gallery/feature_renderers.js` line 1586 (config `/objects/1/features/van_allen_belts/outer_belt_distance`): `fmtServed(distances[i], counts[i], 1) +`
- gallery `gallery/feature_renderers.js` line 1601 (config `/objects/1/features/van_allen_belts/outer_belt_distance`): `drawn: fmtServed(distances[i], counts[i], 1),`
- gallery `gallery/feature_renderers.js` line 1607 (config `/objects/1/features/van_allen_belts/outer_belt_distance`): `? SOFT_BR + "(given as L = " + fmtServed(distances[i], counts[i], 1) +`
- gallery `gallery/feature_renderers.js` line 1611 (config `/objects/1/features/van_allen_belts/outer_belt_distance`): `kmAndAu(distances[i] * radiusKm,`

### `EARTH_SOLAR_WIND_PRESSURE_NPA`

- orrery `earth_visualization_shells.py` line 1022: `f"Sun-facing side at a nominal solar wind pressure of {exact_text('EARTH_SOLAR_WIND_PRESSURE_...`
- orrery `earth_visualization_shells.py` line 1205: `f"side at a nominal solar wind pressure of {exact_text('EARTH_SOLAR_WIND_PRESSURE_NPA')} nPa....`
- orrery `earth_visualization_shells.py` line 1296: `f"Sun-facing side at a nominal solar wind pressure of {exact_text('EARTH_SOLAR_WIND_PRESSURE_...`
- gallery `gallery/feature_renderers.js` line 3214 (config `/objects/1/features/earth_magnetosphere/magnetopause/surface/pressure`): `pressure: fmtServed(dp, servedFigures(mpS.pressure), 1),`
- gallery `gallery/feature_renderers.js` line 3436 (config `/objects/1/features/earth_magnetosphere/bow_shock/surface/pressure`): `pressure: fmtServed(bsP, servedFigures(bsS.pressure), 1),`

### `EARTH_SOLAR_WIND_BZ_NT`

- gallery `gallery/feature_renderers.js` line 3213 (config `/objects/1/features/earth_magnetosphere/magnetopause/surface/bz`): `bz: fmtServed(bz, servedFigures(mpS.bz), 1),`

### `EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG`

- gallery `gallery/feature_renderers.js` line 3215 (config `/objects/1/features/earth_magnetosphere/magnetopause/surface/cut_angle`): `cut_angle: fmtServed(mpCut, servedFigures(mpS.cut_angle), 0)`

### `EARTH_BOW_SHOCK_CUT_ANGLE_DEG`

- gallery `gallery/feature_renderers.js` line 3437 (config `/objects/1/features/earth_magnetosphere/bow_shock/surface/cut_angle`): `cut_angle: fmtServed(bsCut, servedFigures(bsS.cut_angle), 0)`

### `INNER_CORONA_RADII`

- orrery `comet_visualization_shells.py` line 565: `f"Inside Inner K-corona (~{row_text('INNER_CORONA_RADII')} R_sun, ~{row_text('INNER_CORONA_RA...`
- orrery `comet_visualization_shells.py` line 738: `f"Roche limit (about {row_text('ROCHE_LIMIT_RADII')} R_sun, {row_text('ROCHE_LIMIT_RADII', 'a...`
- orrery `solar_visualization_shells.py` line 527: `f"* Solar Inner Corona (extends to 2-3 solar radii; drawn at {row_text('INNER_CORONA_RADII')}...`
- orrery `solar_visualization_shells.py` line 803: `f"* F-corona (dust-scattered): {row_text('INNER_CORONA_RADII')}-{row_text('OUTER_CORONA_RADII...`
- orrery `solar_visualization_shells.py` line 1013: `f"* Solar Inner Corona (extends to 2-3 solar radii; drawn at {row_text('INNER_CORONA_RADII')}...`
- orrery `solar_visualization_shells.py` line 1145: `f'* Inner Corona (K-corona): 1-{row_text('INNER_CORONA_RADII')} R_sun, ~1-3 million K<br>'`
- orrery `solar_visualization_shells.py` line 1172: `f'* Inner Corona (K-corona): 1-{row_text('INNER_CORONA_RADII')} R_sun, ~1-3 million K<br>'`
- gallery `gallery/feature_renderers.js` line 2932 (config `/objects/0/features/solar_atmosphere/inner_corona`): `? fmtServed(cfg.radius.value, sunF, 0) : String(cfg.radius.value);`

### `OUTER_CORONA_RADII`

- orrery `solar_visualization_shells.py` line 482: `f"This shell marks the extended outer solar corona at {row_text('OUTER_CORONA_RADII')} solar ...`
- orrery `solar_visualization_shells.py` line 493: `f"* This {row_text('OUTER_CORONA_RADII')} R_sun shell represents the faint, extended F-corona...`
- orrery `solar_visualization_shells.py` line 793: `f"Extended outer solar corona at {row_text('OUTER_CORONA_RADII')} solar radii ({row_text('OUT...`
- orrery `solar_visualization_shells.py` line 803: `f"* F-corona (dust-scattered): {row_text('INNER_CORONA_RADII')}-{row_text('OUTER_CORONA_RADII...`
- orrery `solar_visualization_shells.py` line 1150: `f'* Extended Corona (F-corona): {row_text('OUTER_CORONA_RADII')} R_sun, a boundary chosen for...`
- orrery `solar_visualization_shells.py` line 1177: `f'* Extended Corona (F-corona): {row_text('OUTER_CORONA_RADII')} R_sun, a boundary chosen for...`
- gallery `gallery/feature_renderers.js` line 2932 (config `/objects/0/features/solar_atmosphere/outer_corona`): `? fmtServed(cfg.radius.value, sunF, 0) : String(cfg.radius.value);`

### `HELMET_CUSP_RADII`

- orrery `comet_visualization_shells.py` line 554: `f"(~{row_text('HELMET_CUSP_RADII')} R_sun, ~{row_text('HELMET_CUSP_RADII', 'au')} AU)<br>"`
- orrery `comet_visualization_shells.py` line 562: `f"Inside the helmet cusp (~{row_text('HELMET_CUSP_RADII')} R_sun, "`
- orrery `comet_visualization_shells.py` line 563: `f"~{row_text('HELMET_CUSP_RADII', 'au')} AU): {helmet_status}<br>"`
- orrery `comet_visualization_shells.py` line 737: `f"({row_text('HELMET_CUSP_RADII')} R_sun, {row_text('HELMET_CUSP_RADII', 'au')} AU),<br>"`
- orrery `solar_visualization_shells.py` line 798: `f"* Streamer belt: the helmets pinch at {row_text('HELMET_CUSP_RADII')} R_sun, and the stalk ...`
- orrery `solar_visualization_shells.py` line 838: `f"and dense at the base, pinching at the cusp at {row_text('HELMET_CUSP_RADII')} R_sun where ...`
- orrery `solar_visualization_shells.py` line 1147: `f'* Streamer Belt (Visible Corona): helmets pinch at {row_text('HELMET_CUSP_RADII')} R_sun, t...`
- orrery `solar_visualization_shells.py` line 1174: `f'* Streamer Belt (Visible Corona): helmets pinch at {row_text('HELMET_CUSP_RADII')} R_sun, t...`
- orrery `solar_visualization_shells.py` line 2040: `f"higher than {row_text('HELMET_CUSP_LOW_RADII')}-{row_text('HELMET_CUSP_HIGH_RADII')} R_sun,...`
- orrery `solar_visualization_shells.py` line 2041: `f"({row_text('HELMET_CUSP_RADII', 'km', grouping=True)} km, {row_text('HELMET_CUSP_RADII', 'a...`
- gallery `gallery/feature_renderers.js` line 2008 (config `/objects/0/features/solar_atmosphere/streamer_belt/cusp_radius`): `"Cusp: " + (servedText(cfg.cusp_radius) || cuspR) + " solar radii<br>= " +`

### `INNER_LIMIT_OORT_CLOUD_AU`

- orrery `palomas_orrery.py` line 10512: `f"* Inner Limit of Oort Cloud: {row_text('INNER_LIMIT_OORT_CLOUD_AU', grouping=True)} AU\n* O...`
- orrery `solar_visualization_shells.py` line 149: `_OORT_INNER_EDGE = row_text('INNER_LIMIT_OORT_CLOUD_AU', grouping=True)`
- orrery `solar_visualization_shells.py` line 1660: `f'From {_OORT_INNER_EDGE} AU ({row_text("INNER_LIMIT_OORT_CLOUD_AU", unit="km", grouping=True...`
- gallery `gallery/feature_renderers.js` line 2274 (config `/objects/0/features/oort_cloud/hills_cloud_torus/inner_radius`): `hover += "From " + (fmtAuServed(cfg.inner_radius) || fmtAu(lo)) +`
- gallery `gallery/feature_renderers.js` line 2938 (config `/objects/0/features/oort_cloud/inner_oort_limit`): `hover += "Radius: " + servedText(cfg.radius) + " AU<br>";`

### `OUTER_OORT_CLOUD_AU`

- orrery `palomas_orrery.py` line 10512: `f"* Inner Limit of Oort Cloud: {row_text('INNER_LIMIT_OORT_CLOUD_AU', grouping=True)} AU\n* O...`
- orrery `solar_visualization_shells.py` line 163: `_OORT_OUTER_EDGE = row_text('OUTER_OORT_CLOUD_AU', grouping=True)`
- gallery `gallery/feature_renderers.js` line 2341 (config `/objects/0/features/oort_cloud/outer_oort_clumpy/outer_radius`): `var z = fmtAuServed(cfg.outer_radius) || fmtAu(hi);`
- gallery `gallery/feature_renderers.js` line 2341 (config `/objects/0/features/oort_cloud/galactic_tide/outer_radius`): `var z = fmtAuServed(cfg.outer_radius) || fmtAu(hi);`
- gallery `gallery/feature_renderers.js` line 2938 (config `/objects/0/features/oort_cloud/outer_oort`): `hover += "Radius: " + servedText(cfg.radius) + " AU<br>";`

## Printed to a terminal only

A tool logging a value is not a display a visitor sees, so these are not counted above.

- `KM_PER_AU`: orrery `export_orbit_cache.py` line 385: `print(" constants_new.KM_PER_AU: %s" % KM_PER_AU)`
- `EARTH_OBLIQUITY_J2000_DEG`: orrery `star_sphere_builder.py` line 514: `print(f" Obliquity: {EARTH_OBLIQUITY_J2000_DEG}\u00b0")`

## Not printed

No display prints these exact rows. Under Rule 7 they carry no print count. The number is how many other orrery lines name the row, so a use that prints it through another name can still be found by reading those lines.

- `KM_PER_AU`: named on 221 other orrery line(s).
- `PARSEC_TO_AU`: named on 10 other orrery line(s).
- `S_PER_HOUR`: named on 3 other orrery line(s).
- `S_PER_DAY`: named on 12 other orrery line(s).
- `D_PER_JULIAN_YEAR`: named on 16 other orrery line(s).
- `EARTH_POLE_RA_J2000_DEG`: named on 6 other orrery line(s).
  - gallery: read to draw, not printed, at `gallery/feature_renderers.js` line 972 (config `/objects/1/features/orientation/pole/ra`): `var ra = measured(pole.ra, "deg", slug + "/orientation/pole/ra", warn);`
- `EARTH_POLE_DEC_J2000_DEG`: named on 6 other orrery line(s).
  - gallery: read to draw, not printed, at `gallery/feature_renderers.js` line 973 (config `/objects/1/features/orientation/pole/dec`): `var dec = measured(pole.dec, "deg", slug + "/orientation/pole/dec", warn);`
- `ARCSEC_PER_DEG`: named on 2 other orrery line(s).
- `EARTH_OBLIQUITY_J2000_ARCSEC`: named on 0 other orrery line(s).
- `EARTH_OBLIQUITY_J2000_DEG`: named on 18 other orrery line(s).
- `GALACTIC_NORTH_POLE_RA_J2000_DEG`: named on 9 other orrery line(s).
  - gallery: read to draw, not printed, at `gallery/feature_renderers.js` line 2306 (config `/objects/0/features/oort_cloud/galactic_tide/galactic_pole/ra`): `var gra = measured(gp.ra, "deg", where + "/galactic_pole/ra", warn);`
  - gallery: read to draw, not printed, at `gallery/feature_renderers.js` line 2371 (config `/objects/0/features/oort_cloud/galactic_plane/galactic_pole/ra`): `var gra = measured(gp.ra, "deg", where + "/galactic_pole/ra", warn);`
- `GALACTIC_NORTH_POLE_DEC_J2000_ARCSEC`: named on 0 other orrery line(s).
- `GALACTIC_NORTH_POLE_DEC_J2000_DEG`: named on 8 other orrery line(s).
  - gallery: read to draw, not printed, at `gallery/feature_renderers.js` line 2307 (config `/objects/0/features/oort_cloud/galactic_tide/galactic_pole/dec`): `var gdec = measured(gp.dec, "deg", where + "/galactic_pole/dec", warn);`
  - gallery: read to draw, not printed, at `gallery/feature_renderers.js` line 2372 (config `/objects/0/features/oort_cloud/galactic_plane/galactic_pole/dec`): `var gdec = measured(gp.dec, "deg", where + "/galactic_pole/dec", warn);`
- `DEG_PER_RAD`: named on 2 other orrery line(s).
- `EARTH_SOLAR_WIND_SPEED_KM_S`: named on 0 other orrery line(s).
- `EARTH_MAGNETOTAIL_DRAWN_RADIUS_RADII`: named on 3 other orrery line(s).
  - gallery: read to draw, not printed, at `gallery/feature_renderers.js` line 3266 (config `/objects/1/features/earth_magnetosphere/magnetotail/drawn_radius`): `var tailRadius = measured(tl.drawn_radius, "r_earth",`
- `EARTH_MAGNETOTAIL_DRAWN_END_RADII`: named on 3 other orrery line(s).
  - gallery: read to draw, not printed, at `gallery/feature_renderers.js` line 3268 (config `/objects/1/features/earth_magnetosphere/magnetotail/drawn_end`): `var tailEnd = measured(tl.drawn_end, "r_earth", tlWhere + "/drawn_end",`
- `ROCHE_LIMIT_DRAWN_RADII`: named on 6 other orrery line(s).
  - gallery: read to draw, not printed, at `gallery/feature_renderers.js` line 2893 (config `/objects/0/features/solar_atmosphere/roche_limit/drawn_radius`): `drawAu = measuredRadiusAu(cfg.drawn_radius,`
- `HILLS_CLOUD_PLANES_NODE_CELL_DEG`: named on 3 other orrery line(s).
- `HILLS_CLOUD_PLANES_INCL_CELL_DEG`: named on 3 other orrery line(s).
- `HILLS_CLOUD_PLANES_READ`: named on 6 other orrery line(s).
- `HILLS_CLOUD_ECCENTRICITY`: named on 4 other orrery line(s).
- `DE430_TERRESTRIAL_POSITION_PLACE_KM`: named on 10 other orrery line(s).
  - gallery: read to draw, not printed, at `gallery/solar_system_figures.js` line 108 (config `/objects/1/position_accuracy`): `if (node.unit === "km" && typeof node.value === "number") {`
  - gallery: read to draw, not printed, at `gallery/solar_system_figures.js` line 109 (config `/objects/1/position_accuracy`): `v = node.value;`
  - gallery: read to draw, not printed, at `gallery/solar_system_figures.js` line 108 (config `/objects/4/position_accuracy`): `if (node.unit === "km" && typeof node.value === "number") {`
  - gallery: read to draw, not printed, at `gallery/solar_system_figures.js` line 109 (config `/objects/4/position_accuracy`): `v = node.value;`
  - gallery: read to draw, not printed, at `gallery/solar_system_figures.js` line 108 (config `/objects/5/position_accuracy`): `if (node.unit === "km" && typeof node.value === "number") {`
  - gallery: read to draw, not printed, at `gallery/solar_system_figures.js` line 109 (config `/objects/5/position_accuracy`): `v = node.value;`
  - gallery: read to draw, not printed, at `gallery/solar_system_figures.js` line 108 (config `/objects/6/position_accuracy`): `if (node.unit === "km" && typeof node.value === "number") {`
  - gallery: read to draw, not printed, at `gallery/solar_system_figures.js` line 109 (config `/objects/6/position_accuracy`): `v = node.value;`
- `DE430_JUPITER_SATURN_POSITION_PLACE_KM`: named on 8 other orrery line(s).
  - gallery: read to draw, not printed, at `gallery/solar_system_figures.js` line 108 (config `/objects/2/position_accuracy`): `if (node.unit === "km" && typeof node.value === "number") {`
  - gallery: read to draw, not printed, at `gallery/solar_system_figures.js` line 109 (config `/objects/2/position_accuracy`): `v = node.value;`
  - gallery: read to draw, not printed, at `gallery/solar_system_figures.js` line 108 (config `/objects/3/position_accuracy`): `if (node.unit === "km" && typeof node.value === "number") {`
  - gallery: read to draw, not printed, at `gallery/solar_system_figures.js` line 109 (config `/objects/3/position_accuracy`): `v = node.value;`
- `DE430_URANUS_NEPTUNE_PLUTO_POSITION_PLACE_KM`: named on 8 other orrery line(s).
  - gallery: read to draw, not printed, at `gallery/solar_system_figures.js` line 108 (config `/objects/7/position_accuracy`): `if (node.unit === "km" && typeof node.value === "number") {`
  - gallery: read to draw, not printed, at `gallery/solar_system_figures.js` line 109 (config `/objects/7/position_accuracy`): `v = node.value;`
  - gallery: read to draw, not printed, at `gallery/solar_system_figures.js` line 108 (config `/objects/8/position_accuracy`): `if (node.unit === "km" && typeof node.value === "number") {`
  - gallery: read to draw, not printed, at `gallery/solar_system_figures.js` line 109 (config `/objects/8/position_accuracy`): `v = node.value;`
  - gallery: read to draw, not printed, at `gallery/solar_system_figures.js` line 108 (config `/objects/12/position_accuracy`): `if (node.unit === "km" && typeof node.value === "number") {`
  - gallery: read to draw, not printed, at `gallery/solar_system_figures.js` line 109 (config `/objects/12/position_accuracy`): `v = node.value;`
- `DE430_MOON_POSITION_PLACE_KM`: named on 5 other orrery line(s).
- `GM_SUN_SI`: named on 0 other orrery line(s).
- `M3_PER_KM3`: named on 1 other orrery line(s).

## How the search works

Orrery: every tracked `.py` file outside `documentation/`, except `constants_new.py` and this tool, searched for each exact row's name inside `{...}` in a formatted string, as the argument of `_declared`, `_whole_figures` or `_with_uncertainty`, after `%`, or inside `str(...)` or `format(...)`. Comment lines are skipped.

Gallery: each pointer in `data/objects_config.json` to an exact row, followed to its print lines by the PRINTS table in the tool: the page script, the function and a piece of the print line. A pointer read only to place a drawing is named instead in the DRAWN table, by the line that reads it, and that line must not be a print line. A pointer with no entry, or an entry that matches nothing, is reported above rather than dropped. Page scripts read: `gallery/arrival.js`, `gallery/earth_geometry.js`, `gallery/feature_renderers.js`, `gallery/guestbook.js`, `gallery/nav_cluster.js`, `gallery/solar_system_drawer.js`, `gallery/solar_system_figures.js`, `interactive.html`.

Not searched: an exact row's value typed into text as words or digits instead of read from the row.
