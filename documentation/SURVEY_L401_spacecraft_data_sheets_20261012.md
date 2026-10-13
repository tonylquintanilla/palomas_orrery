<!-- Doc-Kind: hand | Survey of the JPL Horizons data sheets of all 26 spacecraft the orrery draws, for L-401 (the distance digits): which state a trajectory uncertainty, in what form, and the revision date of each. Read 2026-10-12. -->
# Survey: the spacecraft data sheets (L-401, the distance digits)

Built on orrery 47815de273b30966769f7c679f889537dba994a5 at
https://github.com/tonylquintanilla/palomas_orrery. The gallery is not
touched.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 12, 2026 with Anthropic's Claude Opus 5.5.

- Type: DISCOVERY (a list; it fixes nothing by itself).
- Asked by Tony, 2026-10-12, with his ruling "A": a spacecraft's
  distance is rounded by the uncertainty its own Horizons data sheet
  states, converted at its distance from Earth and said to be ours.
- Prompted by Claude Fable 5.1, which read the Voyager 2 sheet the same
  day and found a stated figure the design had missed.
- Method: each sheet fetched through the chat's web-fetch tool at
  `https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND='<id>'&OBJ_DATA='YES'&MAKE_EPHEM='NO'`,
  and asked for its revision date, the trajectory's source, the end of
  tracking, and every statement of trajectory uncertainty with its
  units. The tool reads through a small model, so each quote below is
  as that model returned it; the Voyager figures were also read by
  Fable through the browser pane.

## 1. The answer

Of the 26 spacecraft (27 entries; OSIRIS-REx and OSIRIS-APEX share
-64), two sheets state a trajectory uncertainty: **Voyager 1 and
Voyager 2.** Both state it as a predicted pointing angle seen from
Earth, for 2030-Jan-1, with no sigma level and no distance uncertainty.
The other 24 state none.

Not counted as trajectory uncertainties, though they look like them:
Cassini's "Pointing accuracy = 2.0 mrad" (the spacecraft's attitude
control); Gaia's "accuracy down to 24 uas" (its star measurements);
JWST's "optical resolution: 0.1 arcseconds" (the telescope); New
Horizons' "2.3045(10)^6 km" (the sheet's way of writing 2.3045 x 10^6).

## 2. Sheet by sheet

| Spacecraft | Horizons id | Revised | Trajectory and tracking | Uncertainty stated |
|---|---|---|---|---|
| Voyager 1 | -31 | Aug 19, 2022 | 2022 refit by R. Jacobson; "no new tracking data possible since 1992" | "Formal predicted geocentric pointing uncertainty on 2030-Jan-1: RA +/- 1.701 arcseconds, DEC +/- 1.535 arcseconds" |
| Voyager 2 | -32 | Aug 19, 2022 | 2022 refit by R. Jacobson of 1989-1992 tracking; none since 1992 | "RA +/- 4.718 arcseconds, DEC +/- 3.715 arcseconds", same sentence |
| Apollo 11 S-IVB | -399110 | Mar 22, 2016 | reconstruction by D. R. Adamo, 2012 | none; "Uncertainties and errors in the extrapolated position prediction will increase" (no figure) |
| Pioneer 10 | -23 | Jul 27, 2005 | JPL Navigation Team | none; "should be used cautiously for high precision" (no figure) |
| Pioneer 11 | -24 | Jun 15, 2007 | JPL Navigation Team | none; same caution |
| Galileo | -77 | Feb 23, 2008 | data fit 1989 to Aug 12, 2002 | none |
| SOHO | -21 | Sep 01, 2026 | GSFC FDF | none; 1998 recovery gap "may be significant" (no figure) |
| Cassini | -82 | Sep 28, 2018 | post-mission reconstruction | none (2.0 mrad is attitude control) |
| Rosetta | -226 | Oct 24, 2016 | mission solutions | none |
| New Horizons | -98 | Sep 01, 2026 | KinetX, tracking to 2026-Jul-20 | none |
| Akatsuki | -5 | Aug 06, 2025 | ISAS/JAXA/JPL, fit to 2024-Apr-26 | none |
| Juno | -61 | Sep 30, 2026 | JPL navigation; planning prediction after 2026-Sep-23 | none |
| Gaia | -139479 | May 16, 2025 | ESOC, to 2025-Mar-28 | none (24 uas is the star survey) |
| Hayabusa2 | -37 | Jun 30, 2026 | JAXA, fit to 2026-Jun-29 | none |
| OSIRIS-REx / APEX | -64 | Sep 18, 2025 | reconstructed solutions | none; a "large jump at the 2026 merge" noted |
| Parker Solar Probe | -96 | Sep 30, 2026 | fit to 2026-Sep-01 | none |
| Mars 2020 (MarsRover) | -168 | Feb 18, 2021 | JPL navigation | none |
| Lucy | -49 | Oct 25, 2025 | fit to 2025-Sep-08 | none |
| DART | -135 | Mar 01, 2024 | final reconstruction | none |
| JWST | -170 | Sep 21, 2026 | GSFC FDF, to Sep 20 | none (0.1 arcsec is the telescope) |
| JUICE | -28 | Jun 30, 2026 | ESA, to June 16 | none |
| Psyche | -255 | Sep 30, 2026 | JPL navigation, to August 11 | none |
| Europa Clipper | -159 | Sep 30, 2026 | JPL navigation, to 2026-Sep-22 | none |
| BepiColombo | -121 | Jun 30, 2026 | ESA, fit to 2026-Jun-14 | none |
| Solar Orbiter | -144 | Sep 30, 2026 | ESA, fit to 2026-Sep-17 | none |
| Artemis II | -1024 | Apr 20, 2026 | NASA/JSC | none |

## 3. What the build does with it

- Four rows in `constants_new.py`, `VOYAGER_1_POINTING_RA_2030_ARCSEC`
  and its three siblings, each with its sheet as the source.
- The hover converts the larger of RA and DEC at the spacecraft's
  distance from Earth (fetched with the sky position, the same query)
  and says, in words, that JPL states this angle for 2030 and none for
  the distance, so the conversion is ours.
- The other 24 keep whole kilometers with "JPL states no accuracy for
  this position", which this survey shows is true of their sheets.
- A sheet can change: twelve of these were revised in 2026. Tony,
  2026-10-12: "agree. let's add it to the horizons check that runs
  every 30 days i believe." Recorded on L-395 (the Horizons check), to
  be built in its own session: on its 30-day cycle the check re-reads
  each sheet and reports a moved "Revised:" date or a changed stated
  uncertainty, for a person; it never edits a row. The same day Tony
  ruled that the check moves into the orrery's maintenance run, beside
  the objects export; the brief is
  `documentation/HANDOFF_L395_horizons_check_move_brief_20261012.md`.

Survey written October 2026 with Anthropic's Claude Opus 5.5.
