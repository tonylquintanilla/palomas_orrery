<!-- Doc-Kind: generated | Which exact rows of constants_new.py a display prints, and where, in the orrery and the gallery; rebuilt by exact_rows_report.py. Do not hand-edit. -->
# Exact Rows Printed

Rebuilt by `exact_rows_report.py` on every orrery maintenance run. An exact row is one whose `# Figures:` line begins `exact`: a definition or a stated rule, not a measurement. provenance-discipline Rule 7 says a display prints such a row by a print count the row states, never by a width chosen where it is printed. This report lists every place a display prints one, with the code on that line, so the width it uses can be read.

## Summary

- 20 exact rows in `constants_new.py`.
- 7 printed by at least one display: `EARTH_LEO_UPPER_ALTITUDE_KM`, `EARTH_LEO_LOWER_ALTITUDE_KM`, `EARTH_VAN_ALLEN_OUTER_RADII`, `EARTH_SOLAR_WIND_PRESSURE_NPA`, `EARTH_SOLAR_WIND_BZ_NT`, `EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG`, `EARTH_BOW_SHOCK_CUT_ANGLE_DEG`.
- 18 printing lines: 8 in the orrery, 10 in the gallery.
- Gallery pointers to exact rows with no PRINTS entry (NOT FOLLOWED): 0.
- PRINTS entries that no longer match a pointer or a print line (BROKEN): 0.

## Printed

### `EARTH_LEO_UPPER_ALTITUDE_KM`

- orrery `earth_visualization_shells.py` line 1514: `f"Altitude range: {EARTH_LEO_LOWER_ALTITUDE_KM:,.0f} km to {EARTH_LEO_UPPER_ALTITUDE_KM:,.0f}...`
- orrery `shell_configs.py` line 2329: `f"Low Earth Orbit (LEO) is the region from roughly {EARTH_LEO_LOWER_ALTITUDE_KM:,.0f} km to {...`
- gallery `gallery/feature_renderers.js` line 1893 (config `/objects/1/features/earth_orbital_zones/leo_outer/altitude`): `kmAndAu(km.altitudeKm, km.altitudeFigures) + "<br>";`

### `EARTH_LEO_LOWER_ALTITUDE_KM`

- orrery `earth_visualization_shells.py` line 1514: `f"Altitude range: {EARTH_LEO_LOWER_ALTITUDE_KM:,.0f} km to {EARTH_LEO_UPPER_ALTITUDE_KM:,.0f}...`
- orrery `shell_configs.py` line 2329: `f"Low Earth Orbit (LEO) is the region from roughly {EARTH_LEO_LOWER_ALTITUDE_KM:,.0f} km to {...`
- gallery `gallery/feature_renderers.js` line 1893 (config `/objects/1/features/earth_orbital_zones/leo_inner/altitude`): `kmAndAu(km.altitudeKm, km.altitudeFigures) + "<br>";`

### `EARTH_VAN_ALLEN_OUTER_RADII`

- orrery `earth_visualization_shells.py` line 1293: `f"ring is the flux peak, L = {EARTH_VAN_ALLEN_OUTER_RADII:g} -- about {_km_above_surface(EART...`
- orrery `earth_visualization_shells.py` line 1299: `f"the L = {_band_low} to {_band_high} band; the drawn {EARTH_VAN_ALLEN_OUTER_RADII:g} is our ...`
- orrery `shell_configs.py` line 2318: `f"{EARTH_VAN_ALLEN_OUTER_RADII:g} Earth radii out (doi:10.1029/2024JA033504).\n"`
- gallery `gallery/feature_renderers.js` line 1018 (config `/objects/1/features/van_allen_belts/outer_belt_distance`): `? wrapHover("Drawn at " + fmtServed(distances[i], figures[i], 1) +`
- gallery `gallery/feature_renderers.js` line 1025 (config `/objects/1/features/van_allen_belts/outer_belt_distance`): `: "Drawn at " + fmtServed(distances[i], figures[i], 1) + " " +`
- gallery `gallery/feature_renderers.js` line 1028 (config `/objects/1/features/van_allen_belts/outer_belt_distance`): `? SOFT_BR + "(given as L = " + fmtServed(distances[i], figures[i], 1) +`
- gallery `gallery/feature_renderers.js` line 1031 (config `/objects/1/features/van_allen_belts/outer_belt_distance`): `"= " + kmAndAu(distances[i] * radiusKm,`

### `EARTH_SOLAR_WIND_PRESSURE_NPA`

- orrery `earth_visualization_shells.py` line 964: `f"Sun-facing side at a nominal solar wind pressure of {EARTH_SOLAR_WIND_PRESSURE_NPA:g} nPa.\n"`
- orrery `earth_visualization_shells.py` line 1147: `f"side at a nominal solar wind pressure of {EARTH_SOLAR_WIND_PRESSURE_NPA:g} nPa. It stretche...`
- orrery `earth_visualization_shells.py` line 1231: `f"Sun-facing side at a nominal solar wind pressure of {EARTH_SOLAR_WIND_PRESSURE_NPA:g} nPa.<...`
- gallery `gallery/feature_renderers.js` line 2142 (config `/objects/1/features/earth_magnetosphere/magnetopause/surface/pressure`): `" nT, dynamic pressure " + fmtServed(dp, servedFigures(mpS.pressure), 1) +`
- gallery `gallery/feature_renderers.js` line 2217 (config `/objects/1/features/earth_magnetosphere/bow_shock/surface/pressure`): `fmtServed(bsP, servedFigures(bsS.pressure), 1) +`

### `EARTH_SOLAR_WIND_BZ_NT`

- gallery `gallery/feature_renderers.js` line 2141 (config `/objects/1/features/earth_magnetosphere/magnetopause/surface/bz`): `"Bz " + fmtServed(bz, servedFigures(mpS.bz), 1) +`

### `EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG`

- gallery `gallery/feature_renderers.js` line 2144 (config `/objects/1/features/earth_magnetosphere/magnetopause/surface/cut_angle`): `"Drawn to " + fmtServed(mpCut, servedFigures(mpS.cut_angle), 0) +`

### `EARTH_BOW_SHOCK_CUT_ANGLE_DEG`

- gallery `gallery/feature_renderers.js` line 2219 (config `/objects/1/features/earth_magnetosphere/bow_shock/surface/cut_angle`): `"Drawn to " + fmtServed(bsCut, servedFigures(bsS.cut_angle), 0) +`

## Printed to a terminal only

A tool logging a value is not a display a visitor sees, so these are not counted above.

- `KM_PER_AU`: orrery `export_orbit_cache.py` line 385: `print(" constants_new.KM_PER_AU: %s" % KM_PER_AU)`

## Not printed

No display prints these exact rows. Under Rule 7 they carry no print count. The number is how many other orrery lines name the row, so a use that prints it through another name can still be found by reading those lines.

- `KM_PER_AU`: named on 215 other orrery line(s).
- `S_PER_HOUR`: named on 0 other orrery line(s).
- `EARTH_POLE_RA_J2000_DEG`: named on 6 other orrery line(s).
- `EARTH_POLE_DEC_J2000_DEG`: named on 6 other orrery line(s).
- `ARCSEC_PER_DEG`: named on 0 other orrery line(s).
- `EARTH_OBLIQUITY_J2000_ARCSEC`: named on 0 other orrery line(s).
- `EARTH_OBLIQUITY_J2000_DEG`: named on 8 other orrery line(s).
- `DEG_PER_RAD`: named on 0 other orrery line(s).
- `EARTH_SOLAR_WIND_SPEED_KM_S`: named on 0 other orrery line(s).
- `EARTH_MAGNETOTAIL_DRAWN_RADIUS_RADII`: named on 3 other orrery line(s).
- `EARTH_MAGNETOTAIL_DRAWN_END_RADII`: named on 3 other orrery line(s).
- `GM_SUN_SI`: named on 0 other orrery line(s).
- `M3_PER_KM3`: named on 0 other orrery line(s).

## How the search works

Orrery: every tracked `.py` file outside `documentation/`, except `constants_new.py` and this tool, searched for each exact row's name inside `{...}` in a formatted string, as the argument of `_declared`, `_whole_figures` or `_with_uncertainty`, after `%`, or inside `str(...)` or `format(...)`. Comment lines are skipped.

Gallery: each pointer in `data/objects_config.json` to an exact row, followed to its print lines by the PRINTS table in the tool: the page script, the function and a piece of the print line. A pointer with no entry, or an entry that matches nothing, is reported above rather than dropped. Page scripts read: `gallery/arrival.js`, `gallery/earth_geometry.js`, `gallery/feature_renderers.js`, `gallery/nav_cluster.js`, `interactive.html`.

Not searched: an exact row's value typed into text as words or digits instead of read from the row.
