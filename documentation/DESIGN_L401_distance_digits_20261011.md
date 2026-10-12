<!-- Doc-Kind: hand | Design record for L-401 (the orrery's distance hovers printed by the errors they earn): the discovery list, the slices, where each body's error comes from, and the decisions for Tony, one at a time. Draft for the design talk of 2026-10-11. -->
# L-401 (the orrery's distance digits): discovery and design

Built on orrery 28a4636717920e86965f2e1777f3bf92386d1bb6 at
https://github.com/tonylquintanilla/palomas_orrery ("L431_4 _5 period
in hovers"); gallery e3536c8732d7b62faa5c09515e4b7f1d1c10af9c at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read, not
touched.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 11, 2026 with Anthropic's Claude Opus 5.5.

- Type: DESIGN SESSION, draft. No code yet.
- Tony, 2026-10-11: "let's promote L401 to next. accuracy and precision
  are fundamental. let's do it here."
- The rule it applies: provenance-discipline 2.28, A Computed Position
  Prints What Its Errors Earn, and The ceiling's Report test. The
  period (L-431 build 1) already prints by it.

## 1. Read this first

- The orrery prints 376 numbers with fixed widths in 110 functions
  across 34 files. Not all are distances of bodies; section 2 sorts them.
- The first slice is the body hover, the one in your screenshots. One
  function builds it for the static plot, the animation and the social
  export: `visualization_utils.format_detailed_hover_text`.
- Each body's error has a source we can open: JPL's 2014 ephemeris
  report for the planets and Pluto (already three rows in the store),
  and Horizons' own 3-sigma range uncertainty for small bodies, read
  live on 2026-10-11.
- Three decisions are yours, one at a time (section 5).

## 2. Discovery: where the orrery prints a computed number

Found by searching every module for a fixed-width number printed beside
a unit, and for the two shared formatters. Counted by function; the
line list is the session's working file.

| Kind | Where | Functions |
|---|---|---|
| The body hover (slice 1) | `visualization_utils.py` | `format_detailed_hover_text`; `formatting_utils.format_maybe_float` (10 decimals) and `format_km_float` (10-figure scientific) |
| Its sky-position line | `celestial_coordinates.py` | `MAJOR_BODY_UNCERTAINTIES`, a typed table of arcseconds labelled "JPL DE440/441 ephemeris" |
| Markers drawn on the plot (slice 2) | `apsidal_markers.py`, `palomas_orrery.py` | `create_enhanced_apsidal_hover_text`, `add_perihelion_marker`, `add_apohelion_marker`, `add_actual_apsidal_markers`, `add_keplerian_position_marker`, `add_closest_approach_marker`; the closest-plotted-point hovers |
| Orbit hovers (slice 3) | `idealized_orbits.py` | `plot_idealized_orbits`, `add_mean_orbit_trace`, the moon and barycentre orbit plotters (16 functions) |
| Encounters and close approaches (slice 4) | `spacecraft_encounters.py`, `close_approach_data.py`, `apsidal_markers.py` | `_format_encounter_hover`, `format_approach_hover`, `add_encounter_marker` |
| Fly-to buttons | `visualization_utils.py` | `add_fly_to_object_buttons` |
| The parameters window | `orbital_param_viz.py` | `create_orbital_transformation_viz`, `update_plot` |
| Not this item | shells (`*_visualization_shells.py`, `shell_configs.py`) print store rows, which the Figures rule already governs; `sgr_a_*` and `exoplanet_*` are the stars, not these rooms; console prints and cache tools are not displays |

## 3. Where each body's error comes from

- Planets and Pluto: JPL's 2014 ephemeris report (Folkner et al.), the
  three rows already in `constants_new.py` (provenance-discipline, An
  Accuracy Stated in Words): terrestrial planets to 1 km, Jupiter and
  Saturn to 100 km, Uranus, Neptune and Pluto to 10,000 km. The
  display uses half a unit of that place.
- Small bodies: Horizons' own 3-sigma range uncertainty, quantity 39,
  asked from the plot's centre. Read live on 2026-10-11 from the Sun:
  Sedna 257,817.569 km (and 0.0002397 km/s on the range rate); Mercury
  "n.a.", as for every planet, which is why the planets use the report.
- Drift: none. The orrery's positions come from Horizons for the plot
  date itself.
- Light-minutes, light-hours and the distance to the centre's surface
  are the same distance in other units, so they carry the same error.

## 4. What the hover would print (the Report test)

| Body | Error | Now | By the rule |
|---|---|---|---|
| Mercury | 0.5 km (report: 1 km) | 0.4381591083 AU | 0.43815911 AU |
| | | 6.5547669633e+07 km | 65,547,670 km |
| | | 3.6440581856 light-minutes | 3.6440582 light-minutes |
| Sedna | 257,818 km (Horizons 3-sigma) | 82.8297793403 AU | 82.83 AU |
| | | 1.2391158620e+10 km | 12,391,000,000 km |
| | | 11.4812378152 light-hours | 11.481 light-hours |

A line under the distances would say where the error comes from, in
words you approve, as the period's line does.

## 5. Decisions for Tony, one at a time

1. The first slice and its sources: the body hover, with the planets'
   error from JPL's report and the small bodies' from Horizons' 3-sigma
   range uncertainty (one more Horizons question per body per plot).
2. A body JPL gives no figure for: the Moon and the planets' moons,
   spacecraft, Lagrange points. And the velocity line, which no source
   gives an accuracy for except a small body's range rate.
3. The sky-position line's "+/-0.005 arcsec, JPL DE440/441 ephemeris"
   for the planets comes from a typed table with no source; the small
   bodies' figures are fetched. A typed figure under JPL's name is the
   failure the provenance rules call worse than none.

## 6. Recorded, not this item

- The Sun's own hover prints "Distance to Center Surface:
  -6.9570000000e+05 (below mean datum)": its radius subtracted from its
  zero distance to itself. Slice 1 touches the line.
