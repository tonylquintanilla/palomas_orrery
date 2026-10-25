<!-- Doc-Kind: hand | L-443 slice 2 source check of 2026-10-24: every fetch behind the slice 2 words list, its URL, and the exact quote each name, date and number rests on (non-ASCII letters written in ASCII). -->
# Slice 2 sources: JPL names, data spans and visitor words, fetched 2026-10-24

Built on 206f96c at https://github.com/tonylquintanilla/palomas_orrery
and 96173b8 at https://github.com/tonylquintanilla/tonyquintanilla.github.io.

Read by Anthropic's Claude Opus 5.5 with WebFetch on 2026-10-24. None is
from memory. Skills loaded and followed: provenance-discipline 2.34,
interactive-exhibit 1.22, horizons-orbital-mechanics 1.9.

Caveat on exactness, as in CHECK_L443_jpl_names_20261022.md: WebFetch
passes each page through a reading model, which limits a quote to about
125 characters and sometimes trims column padding. Values were quoted
consistently. Where a quote below is the reading model's summary rather
than the page's words it says so ("summary:").

Non-ASCII written in ASCII: "Wierzchos" (Wikipedia and NASA's APOD
title end it in s-acute; JPL writes plain s); "Tsuchinshan-ATLAS"
(Wikipedia uses an en dash; JPL a hyphen); "-3.8", "-0.9" magnitudes
(Wikipedia uses a minus sign). 'Oumuamua: JPL's JSON answer gives an
ASCII apostrophe, U+0027 (asked separately).

## Fetches that failed

- `ssd-api.jpl.nasa.gov/api/horizons_lookup.api` (the address in the
  brief): every query failed (client_error), including two that work
  on the right host. The Lookup's address is
  `https://ssd.jpl.nasa.gov/api/horizons_lookup.api`; every Lookup
  below used it. The SBDB API at ssd-api.jpl.nasa.gov answered.
- Shell access to ssd.jpl.nasa.gov: refused by the session proxy
  (403). WebFetch was used throughout, as for slice 1.
- https://theskylive.com/c2025k1-info (C/2025 K1 and its three pieces'
  current link): client_error.
- https://theskylive.com/planetarium?obj=c2025v1 (Borisov's current
  link): client_error.
- https://in-the-sky.org/data/object.php?id=CK25R030 (PANSTARRS's
  current link): a bot-blocking page, "Oh noes!".
- https://www.esa.int/esearch?q=juice (JUICE's current link):
  robots_disallowed; it is a search page in any case.
- One note, not a failure: the reading model reported that the text
  answer for the Lookup of C/2025 N1 "includes formatting instructions
  addressed to an AI system", which it ignored. The JSON form of the
  same query was read again and is clean:
  `{"count":1,...,"result":[{"type":"comet (integrated barycenter)","alias":["3I","K25N010"],"pdes":"C/2025 N1","name":"ATLAS (C/2025 N1)","spkid":"1004083"}]}`.
  The values agree.

## A. Spacecraft: JPL name, sheet, and data span

Name query (one per spacecraft):
`https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND='<id>'&OBJ_DATA=YES&MAKE_EPHEM=YES&EPHEM_TYPE=VECTORS&CENTER='500@10'&START_TIME='2026-10-24'&STOP_TIME='2026-10-25'&STEP_SIZE='1d'`

Span queries: the same with OBJ_DATA=NO and START_TIME='1900-01-01',
STOP_TIME='1900-01-02' (gives "prior to"), then START_TIME='2200-01-01',
STOP_TIME='2200-01-02' (gives "after").

| id | Target body name line | Revised line | prior to | after |
|---|---|---|---|---|
| -31 | `Target body name: Voyager 1 (spacecraft) (-31)    {source: Voyager_1_ST+refit2022_m}` | `Revised: Aug 19, 2022   Voyager 1 Spacecraft (interplanetary) / (Sun)     -31` | `No ephemeris for target "Voyager 1 (spacecraft)" prior to A.D. 1977-SEP-05 13:59:24.3830 TDB` | `No ephemeris for target "Voyager 1 (spacecraft)" after A.D. 2100-JAN-01 00:00:00.0000 TDB` |
| -32 | `Target body name: Voyager 2 (spacecraft) (-32)    {source: Voyager_2_ST+refit2022_m}` | `Revised: Aug 19, 2022   Voyager 2 Spacecraft (interplanetary) / (Sun)     -32` | `... "Voyager 2 (spacecraft)" prior to A.D. 1977-AUG-20 15:32:32.1830 TDB` | `... "Voyager 2 (spacecraft)" after A.D. 2100-JAN-01 00:00:00.0000 TDB` |
| -98 | `Target body name: New Horizons (spacecraft) (-98) {source: NH_merged}` | `Revised: Sep 01, 2026        New Horizons Spacecraft                      -98` | `... "New Horizons (spacecraft)" prior to A.D. 2006-JAN-19 19:51:18.3305 TDB` | `... "New Horizons (spacecraft)" after A.D. 2050-JAN-01 00:00:00.0000 TDB` |
| -61 | `Target body name: Juno (spacecraft) (-61)         {source: Juno_merged}` | `Revised: Sep 30, 2026          Juno Spacecraft  / (Sun, Jupiter)           -61` | `... "Juno (spacecraft)" prior to A.D. 2011-AUG-05 17:19:12.1832 TDB` | `... "Juno (spacecraft)" after A.D. 2028-SEP-02 01:39:03.1619 TDB` |
| -49 | `Target body name: Lucy (spacecraft) (-49)         {source: Lucy_merged_DE430}` | `Revised: Oct 25, 2025            Lucy Spacecraft / Sun                     -49` | `... "Lucy (spacecraft)" prior to A.D. 2021-OCT-16 10:33:08.2834 TDB` | `... "Lucy (spacecraft)" after A.D. 2033-APR-02 17:27:41.3425 TDB` |
| -28 | `Target body name: JUICE (spacecraft) (-28)        {source: JUICE_merged}` | `Revised: Sep 27, 2026     JUICE Spacecraft / Sun-Jupiter-Ganymede          -28` | `... "JUICE (spacecraft)" prior to A.D. 2023-APR-14 12:43:26.8426 TDB` | `... "JUICE (spacecraft)" after A.D. 2031-JUL-21 06:30:13.4409 TDB` |
| -255 | `Target body name: Psyche (spacecraft) (-255)      {source: psyche_merged}` | `Revised: Sep 30, 2026            Psyche Spacecraft / Sun                  -255` | `... "Psyche (spacecraft)" prior to A.D. 2023-OCT-13 15:22:57.1394 TDB` | `... "Psyche (spacecraft)" after A.D. 2029-FEB-11 13:49:12.4055 TDB` |
| -159 | `Target body name: Europa Clipper (spacecraft) (-159) {source: Europa_Clipper_merged}` | `Revised: Sep 30, 2026    Europa Clipper (Spacecraft) / (Sun, Jupiter)     -159` | `... "Europa Clipper (spacecraft)" prior to A.D. 2024-OCT-14 16:15:03.7124 TDB` | `... "Europa Clipper (spacecraft)" after A.D. 2034-SEP-03 04:46:13.0131 TDB` |
| -121 | `Target body name: BepiColombo (Spacecraft) (-121) {source: BepiColombo_ESA}` | `Revised: Sep 30, 2026              BepiColombo / (Sun)                    -121` | `... "BepiColombo (Spacecraft)" prior to A.D. 2018-OCT-20 02:13:28.7194 TDB` | `... "BepiColombo (Spacecraft)" after A.D. 2027-APR-11 00:01:09.1855 TDB` |
| -144 | `Target body name: Solar Orbiter (spacecraft) (-144) {source: SOLO_ESA}` | `Revised: Sep 30, 2026       Solar Orbiter Spacecraft / Sun                -144` | `... "Solar Orbiter (spacecraft)" prior to A.D. 2020-FEB-10 04:56:58.8550 TDB` | `... "Solar Orbiter (spacecraft)" after A.D. 2030-NOV-20 04:41:30.5323 TDB` |
| -96 | `Target body name: Parker Solar Probe (spacecraft) (-96) {source: psp_merged}` | `Revised: Sep 30, 2026         Parker Solar Probe / Sun                    -96` | `... "Parker Solar Probe (spacecraft)" prior to A.D. 2018-AUG-12 08:16:23.3431 TDB` | `... "Parker Solar Probe (spacecraft)" after A.D. 2030-JAN-01 00:01:09.1839 TDB` |
| -64 | `Target body name: OSIRIS-REx (spacecraft) (-64)   {source: ORX_merged}` | `Revised: Sep 18, 2025     OSIRIS-REx/APEX Spacecraft / (Sun)               -64` | `... "OSIRIS-REx (spacecraft)" prior to A.D. 2016-SEP-08 23:06:08.2824 TDB` | `... "OSIRIS-REx (spacecraft)" after A.D. 2030-MAR-22 20:00:00.0000 TDB` |

Against the orrery's comments in celestial_objects.py (which are in UT
where they say "UT"; TDB runs about 65 to 69 seconds ahead of UT in
these years):

- -31, -32: no span comment in the orrery. Its end_date 2029-12-31 is
  inside JPL's data.
- -98: prior comment `2006-JAN-19 19:50:13.1460 UT` -- CONFIRMED (the
  same instant, 65 s apart by time scale). After comment
  `2030-JAN-01 11:58:50.8161 UT` -- CHANGED to 2050-JAN-01.
- -61: prior comment `2011-AUG-05 17:18:06.0000 UT` -- CONFIRMED. After
  comment `2028-SEP-30 23:58:50.8177 UT` -- CHANGED to 2028-SEP-02
  01:39:03 TDB. The orrery's end_date 2028-09-30 now lies past JPL's
  data. The sheet's own file table, read separately
  (`COMMAND='-61'&OBJ_DATA=YES&MAKE_EPHEM=NO`), still says
  `spk_ref_260808_280902_260926          2026-Dec-19 07:13   2028-Sep-30 23:55`;
  the file's name ends 280902, matching what Horizons serves. Also on
  that sheet: `The trajectory after 2026-Sep-23 is a planning prediction.`
  and, under major events, `End of mission: Sep   , 2025 (PJ76)`.
- -49: comments `2021-10-16 10:33:08.283 (min. for current target body)`
  and `2033-04-02 17:27:41.343 (max. ...)` -- CONFIRMED, both.
- -28: min `2023-04-14 12:43:26.843` -- CONFIRMED. Max
  `2031-07-21 06:31:30.022` -- same day, 77 s later than JPL now gives.
  Sheet: `juice_orbc_000114_230414_310721_v01                 2023-Apr-14   2031-Jul-21`.
- -255: min `2023-10-13 15:22:57.139` -- CONFIRMED. Max
  `2029-06-26 14:29:49.496` -- CHANGED to 2029-FEB-11 13:49:12 TDB.
  The orrery's end_date 2029-06-26 now lies past JPL's data. Sheet's
  last file: `psyche_ref_260904-290211_260805_v1               2027-Feb-01 12:00 2029-Feb-11`.
- -159: min `2024-10-14 16:15:03.712` -- CONFIRMED. Max
  `2031-02-07 18:17:27.695` and after `2031-FEB-07 18:16:18.5105 UT` --
  CHANGED to 2034-SEP-03. Sheet's last file:
  `ref_241014_340903_21F31_MEGA_L241014_A300411_LP05_V7  2027-Jan-23  2034-Sep-03`.
- -121: min `2018-10-20 02:13:28.719` -- CONFIRMED. Max
  `2027-04-07 00:01:09.186` and after `2027-APR-06 23:59:59.9998 UT` --
  CHANGED to 2027-APR-11 00:01:09 TDB. Sheet:
  `bc_mpo_fcp_00236_20181020_20270411_v01  2018-Oct-20 02:14  2027-Apr-10 23:59`.
- -144: min `2020-02-10 04:56:58.855` -- CONFIRMED. Max
  `2030-11-20 04:03:15.162` -- same day, now 04:41:30 TDB.
- -96: no prior comment (orrery start_date 2018-08-13 is inside). After
  comment `2029-FEB-01 00:00:00.0000 UT` -- CHANGED to 2030-JAN-01.
  Sheet's last file: `spp_nom_20180812_20300101_v044_PostV7    2027-Jan-20 00:00  2030-Jan-01 00:00`.
- -64: after comment `2030-MAR-01 19:58:50.8146 UT` -- CHANGED to
  2030-MAR-22 20:00 TDB. One record serves both the orrery's OSIRISREx
  and OSIRISAPE entries. Sheet lines on the rename:
  `2022-Apr-25 Mission was approved for 18-month Apophis rendevous, to be`
  / `renamed "OSIRIS-APEX"`; `in 2029 and renamed OSIRIS-APEX ("APophis EXplorer").`
  (JPL's spelling "rendevous" kept.)

## B. Comets: JPL names (Lookup, both indexes)

Lookup: `https://ssd.jpl.nasa.gov/api/horizons_lookup.api?sstr=<desig>&group=<sb|mb>&format=text`.
Every mb query below returned `NOTICE: no matches found`.

| entry | sb query | blocks | Object name | Type | Primary SPKID | Primary designation | Aliases |
|---|---|---|---|---|---|---|---|
| Tsuchinshan | C/2023 A3 | 1 | Tsuchinshan-ATLAS (C/2023 A3) | comet (integrated barycenter) | 1003913 | C/2023 A3 | K23A030 |
| ATLAS | C/2024 G3 | 1 | ATLAS (C/2024 G3) | comet (integrated barycenter) | 1003993 | C/2024 G3 | K24G030 |
| West | C/1975 V1 | 1 | West (C/1975 V1-A) | comet (integrated barycenter) | 1001163 | **C/1975 V1-A** | J75V01a |
| McNaught | C/2006 P1 | 1 | McNaught (C/2006 P1) | comet (integrated barycenter) | 1002410 | C/2006 P1 | K06P010 |
| C/2025_K1 | C/2025 K1 | **4** | ATLAS (C/2025 K1); ATLAS (C/2025 K1-B); ATLAS (C/2025 K1-C); ATLAS (C/2025 K1-D) | comet (integrated barycenter), all four | 1004075; 1004099; 1004101; 1004106 | C/2025 K1; -B; -C; -D | K25K010; K25K01b; K25K01c; K25K01d |
| C/2025_K1-B | C/2025 K1-B | 1 | ATLAS (C/2025 K1-B) | comet (integrated barycenter) | 1004099 | C/2025 K1-B | K25K01b |
| C/2025_K1-C | C/2025 K1-C | 1 | ATLAS (C/2025 K1-C) | comet (integrated barycenter) | 1004101 | C/2025 K1-C | K25K01c |
| C/2025_K1-D | C/2025 K1-D | 1 | ATLAS (C/2025 K1-D) | comet (integrated barycenter) | 1004106 | C/2025 K1-D | K25K01d |
| PANSTARRS | C/2025 R3 | 1 | PANSTARRS (C/2025 R3) | comet (integrated barycenter) | 1004093 | C/2025 R3 | K25R030 |
| Borisov | C/2025 V1 | 1 | Borisov (C/2025 V1) | comet (integrated barycenter) | 1004097 | C/2025 V1 | K25V010 |
| 1I/Oumuamua | A/2017 U1 | 1 | 'Oumuamua | asteroid (integrated barycenter) | 50788063 | A/2017 U1 | 1I, 3788040, 1003540, K17U010 |
| 2I/Borisov | C/2019 Q4 | 1 | Borisov (C/2019 Q4) | comet (integrated barycenter) | 1003639 | C/2019 Q4 | 2I, K19Q040 |
| 3I/ATLAS | C/2025 N1 | 1 | ATLAS (C/2025 N1) | comet (integrated barycenter) | 1004083 | C/2025 N1 | 3I, K25N010 |
| Wierzchos | C/2024 E1 | 1 | Wierzchos (C/2024 E1) | comet (integrated barycenter) | 1003985 | C/2024 E1 | K24E010 |

Notes:
- West: the one block's primary designation is C/1975 V1-A, not the
  orrery's id C/1975 V1, so the three-step identity check finds no
  match by designation. Main service, both
  `COMMAND='DES=C/1975 V1;'` and `COMMAND='C/1975 V1;'`, return one
  record: `JPL/HORIZONS                 West (C/1975 V1-A)            2026-Oct-24 14:36:24`,
  `Rec #:90002090 (+COV) Soln.date: 2021-Apr-15_23:29:24     # obs: 113 (199 days)`,
  `1: soln ref.= JPL#2, data arc: 1976-03-10 to 1976-09-25`.
- 'Oumuamua: JSON form (`...sstr=A/2017%20U1&group=sb&format=json`):
  name field `'Oumuamua`, first character ASCII apostrophe U+0027, no
  \u escape. JPL's name has no "1I/" and its type is asteroid.

## C. C/2025 K1: which record

Main service: `https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND='<...>'&OBJ_DATA=YES&MAKE_EPHEM=NO`
(';' sent as %3B).

- `COMMAND='DES=C/2025 K1;'` -- a list, four records:
  ```
  Record #  Epoch-yr  >MATCH DESIG<  Primary Desig  Name
  90004925    2025    C/2025 K1      C/2025 K1       ATLAS
  90004926    2025    C/2025 K1-B    C/2025 K1-B     ATLAS
  90004927    2025    C/2025 K1-C    C/2025 K1-C     ATLAS
  90004928    2025    C/2025 K1-D    C/2025 K1-D     ATLAS
  (4 matches. To SELECT, enter record # (integer), followed by semi-colon.)
  ```
- `COMMAND='C/2025 K1;'` (the orrery's commented-out form) -- the same
  four-record list.
- `COMMAND='90004912'` (the orrery's live pin) -- now a different comet:
  `JPL/HORIZONS                PANSTARRS (C/2025 B1)          2026-Oct-24 14:28:16`,
  `Rec #:90004912 (+COV) Soln.date: 2026-Mar-07_14:43:13     # obs: 50 (2024-2025)`,
  `1: soln ref.= JPL#4, data arc: 2024-12-24 to 2025-02-22`.
- `COMMAND='90004913'` (the orrery comment's number for K1-B) -- also
  another comet now: `Borisov (C/2025 B2)`, `Rec #:90004913 (+COV) Soln.date: 2026-Oct-22_09:12:13`.
- `COMMAND='90004925'` -- `JPL/HORIZONS                  ATLAS (C/2025 K1)            2026-Oct-24 14:28:16`,
  `Rec #:90004925 (+COV) Soln.date: 2026-Oct-09_14:42:28   # obs: 2413 (2025-2026)`,
  `EC= 1.000257251473882   QR= .3342124973850316   TP= 2460956.9397878055`,
  `1: soln ref.= JPL#34, data arc: 2025-04-08 to 2026-01-11`,
  non-gravitational model present:
  `A1= 6.870056390762E-9   A2= -1.885501146317E-9  A3= -2.329905629158E-9`.
  The record does not call itself fragment A.
- `COMMAND='DES=1004075;'` (JPL's SPK id for the parent) -- one record,
  the right one: `ATLAS (C/2025 K1)`, `Rec #:90004925 (+COV) Soln.date: 2026-Oct-09_14:42:28`.
- `COMMAND='DES=C/2025 K1-B;'` -- one record:
  `ATLAS (C/2025 K1-B)`, `Rec #:90004926 (+COV) Soln.date: 2026-Feb-27_13:15:17    # obs: 278 (2025-2026)`,
  `EC= 1.002033474126155`, `1: soln ref.= JPL#13, data arc: 2025-11-05 to 2026-01-06`.
- `COMMAND='DES=C/2025 K1-C;'` -- one record:
  `ATLAS (C/2025 K1-C)`, `Rec #:90004927 (+COV) Soln.date: 2026-Feb-27_13:16:00    # obs: 158 (2025-2026)`,
  `EC= .9999940934318799`, `1: soln ref.= JPL#14, data arc: 2025-11-25 to 2026-01-10`.
- `COMMAND='DES=C/2025 K1-D;'` -- one record:
  `ATLAS (C/2025 K1-D)`, `Rec #:90004928 (+COV) Soln.date: 2026-Jan-10_16:30:52      # obs: 107 (33 days)`,
  `EC= 1.002459703720921`, `1: soln ref.= JPL#5, data arc: 2025-11-26 to 2025-12-29`.
- Arcs compared for "shortest of the four": parent 2025-04-08 to
  2026-01-11; B 2025-11-05 to 2026-01-06; C 2025-11-25 to 2026-01-10;
  D 2025-11-26 to 2025-12-29 (33 days). D is shortest.

## D. Comets: JPL's class and tilt (SBDB)

`https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=<desig>` (the parent by
`?spk=1004075`, because `sstr=C/2025 K1` answers
`"specified query matched more than one object"`, count 4). e is shown
as SBDB rounds it; i in degrees.

| fullname | orbit_class | e | i | epoch (JD) |
|---|---|---|---|---|
| C/2023 A3 (Tsuchinshan-ATLAS) | HYP Hyperbolic Comet | 1 | 139 | 2460448.5 |
| C/2024 G3 (ATLAS) | HYP Hyperbolic Comet | 1 | 117 | 2460480.5 |
| C/1975 V1-A (West) | HYP Hyperbolic Comet | 1 | 43.1 | 2442908.5 |
| C/2006 P1 (McNaught) | HYP Hyperbolic Comet | 1 | **77.8** | 2454065.5 |
| C/2025 K1 (ATLAS) | HYP Hyperbolic Comet | 1, sigma 1.3e-06 | 148 | 2460941.5 |
| C/2025 K1-B (ATLAS) | HYP Hyperbolic Comet | 1, sigma 7.9e-05 | 148 | 2460997.5 |
| C/2025 K1-C (ATLAS) | COM Comet | 1, sigma 3.1e-05 | 148 | 2461026.5 |
| C/2025 K1-D (ATLAS) | HYP Hyperbolic Comet | 1, sigma 0.00015 | 148 | 2461033.5 |
| C/2025 R3 (PANSTARRS) | HYP Hyperbolic Comet | 1 | 125 | 2461063.5 |
| C/2025 V1 (Borisov) | HYP Hyperbolic Comet | 1.01 | 113 | 2460983.5 |
| 'Oumuamua (A/2017 U1) | HYA Hyperbolic Asteroid | 1.2 | 123 | 2458080.5 |
| C/2019 Q4 (Borisov) | HYP Hyperbolic Comet | 3.36 | 44.1 | 2458853.5 |
| C/2025 N1 (ATLAS) | HYP Hyperbolic Comet | 6.14 | 175 | 2461090.5 |
| C/2024 E1 (Wierzchos) | HYP Hyperbolic Comet | 1 | 75.2 | 2460818.5 |

- McNaught: i = 77.8 deg, under 90. The orrery's "Retrograde
  (left-handed) orbit" is WRONG; removed.
- Fragment C: JPL's EC .9999940934 falls short of 1 by 0.0000059;
  SBDB's sigma on e is 0.000031, five times larger. "Still bound" and
  "~13 million years" cannot be told from JPL's own fit; removed.
- C/2025 V1 discovery, `...sbdb.api?sstr=C/2025%20V1&discovery=1`:
  `"discovery":{}` (empty).
- "Opposite direction to the planets" is used for i over 90 deg:
  Tsuchinshan, ATLAS (G3), C/2025 K1 and B, C, D, PANSTARRS, Borisov
  (V1), 'Oumuamua, 3I/ATLAS. Not for West, McNaught, 2I/Borisov,
  Wierzchos.

## E. Visitor words and links: spacecraft

Voyager 1 and 2
- https://voyager.jpl.nasa.gov/mission/ (current link, both) -- loads.
  "The twin spacecraft Voyager 1 and Voyager 2 were launched by NASA in
  separate months in the summer of 1977"; "Voyager 2 launched on August
  20, 1977". It does not itself say "farthest". PASSES the link rule
  (NASA, specific to Voyager); unchanged.
- https://science.nasa.gov/mission/voyager/voyager-1/ -- title
  "Voyager 1: The Farthest Spacecraft -- NASA Science" (dash written
  plainly). "No spacecraft has gone farther than NASA's Voyager 1.";
  "Voyager 1 crossed into interstellar space in August 2012 and
  continues to collect data."; "Voyager 1 is the first human-made
  object to venture into interstellar space."; launch "Sept. 5, 1977 /
  12:56:01 UT".
- https://science.nasa.gov/mission/voyager/voyager-2/ -- title
  "Voyager 2: First To Visit All Four Giants -- NASA Science". "Voyager
  2 is the only spacecraft to study all four of the solar system's
  giant planets at close range."; "Voyager 2 is the only spacecraft to
  visit Uranus and Neptune."; launch "Aug. 20, 1977 / 14:29:44 UT".

New Horizons
- https://www.nasa.gov/mission_pages/newhorizons/main/index.html
  (current) -- 302 to https://science.nasa.gov/mission/new-horizons/.
- https://science.nasa.gov/mission/new-horizons/ -- title "New
  Horizons". "flying by the dwarf planet and its moons on July 14,
  2015."; "In early 2019, New Horizons flew past its second major
  science target."; key dates list: Arrokoth flyby Jan. 1, 2019
  (summary); "remains healthy deep in the Kuiper Belt" (Alan Stern,
  quoted on the page).

Juno
- https://www.nasa.gov/mission_pages/juno/main/index.html (current) --
  302 to https://science.nasa.gov/mission/juno/.
- https://science.nasa.gov/mission/juno/ -- title "Juno - NASA
  Science". "entered orbit around Jupiter on July 4, 2016."; "completed
  its primary mission by mid-2021, offering revelations about Jupiter's
  interior structure, atmosphere (including polar cyclones, deep
  atmosphere, and auroras), and magnetosphere."; "will continue its
  exploration of Jupiter, its ring system, and moons through September
  2025."; listed "Active Mission".
- https://science.nasa.gov/photojournal/junos-mission-goes-on --
  "Juno's Mission Goes On", January 13, 2021: "through September 2025,
  or until the spacecraft's end of life." (found by a search for a
  newer extension; none found).

Lucy
- https://www.nasa.gov/lucy (current) -- 302 to
  https://science.nasa.gov/mission/lucy/.
- https://science.nasa.gov/mission/lucy/ -- title "Lucy - NASA
  Science". Launch "Oct. 16, 2021."; Trojans "share an orbit around the
  Sun with Jupiter."

JUICE
- https://www.esa.int/esearch?q=juice (current) -- robots_disallowed;
  an ESA search page.
- https://www.esa.int/Science_Exploration/Space_Science/Juice -- title
  "ESA - Juice". "its three large ocean-bearing moons - Ganymede,
  Callisto and Europa" (dash written plainly); launched "14 April
  2023."; arrival "July 2031." The page does not say Juice will orbit
  Ganymede, so the words do not.

Psyche (spacecraft)
- https://psyche.ssl.berkeley.edu/ (current) -- loads; title "Psyche
  Mission | A Mission to a Metal World"; the reading model could not
  find who runs it; caption: "for eventual arrival in 2029." Not a NASA
  address.
- https://science.nasa.gov/mission/psyche/ -- title "Psyche". "The
  Psyche spacecraft launched Oct. 13, 2023, on a mission to a unique
  metal-rich asteroid with the same name."; "By August 2029 the
  spacecraft will begin exploring asteroid Psyche."; "Scientists think
  the asteroid has a high metal content." No page opened says "Arrival
  phase ends June 2029"; removed.

Europa Clipper
- https://europa.nasa.gov/ (current) -- 302 to
  https://science.nasa.gov/mission/europa-clipper/.
- https://science.nasa.gov/mission/europa-clipper/ -- title "Europa
  Clipper - NASA Science". "Europa Clipper launched Oct. 14, 2024, on a
  journey to explore Europa, Jupiter's ocean world."; "to reach Jupiter
  in April 2030."; "Scientists think that under the icy surface of
  Jupiter's moon Europa a saltwater ocean exists"; objective "Determine
  if Europa has conditions suitable to support life."; "conduct 49
  close flybys of Europa."

BepiColombo
- https://sci.esa.int/web/bepicolombo (current) -- title "ESA Science &
  Technology - BepiColombo". "Launched on 20 October 2018"; "When it
  arrives at Mercury in late 2025."; "BepiColombo is a joint mission
  between ESA and the Japan Aerospace Exploration Agency (JAXA)."
- https://www.esa.int/Science_Exploration/Space_Science/BepiColombo --
  title "ESA - BepiColombo". Launched "20 October 2018 on an Ariane 5
  rocket from Europe's Spaceport."; "Arrival at Mercury: December
  2026."; "2 orbiters".
- https://www.esa.int/Science_Exploration/Space_Science/BepiColombo/Latest_updates_BepiColombo_s_arrival_at_Mercury
  (found by search) -- title "Latest updates: BepiColombo's arrival at
  Mercury", updated 3 September 2026. "The composite spacecraft will
  enter orbit around Mercury on 21 November 2026"; "MPO and Mio will
  separate from each other on 9-10 December 2026."; "The mission's
  science phase is set to begin in April 2027."; "led by the European
  Space Agency (ESA) in close collaboration with the Japan Aerospace
  Exploration Agency (JAXA)."
- The orrery's "arriving in 2025" is WRONG. The three ESA pages
  disagree on the arrival date (decision 2).

Solar Orbiter
- https://en.wikipedia.org/wiki/Solar_Orbiter (current) -- loads. "The
  Solar Orbiter (SolO) is a Sun-observing probe developed by the
  European Space Agency (ESA) with a NASA contribution."
- https://www.esa.int/Science_Exploration/Space_Science/Solar_Orbiter --
  title "ESA - Solar Orbiter". "Launch date: February 2020"; "taking
  images of the Sun from closer than any spacecraft before and being
  the first to look at its polar regions."; "The closest-ever images of
  the Sun, the first ever close-up images of the Sun's polar regions".
  This page does not name NASA; the NASA contribution rests on the
  Wikipedia sentence above.

Parker Solar Probe
- https://www.nasa.gov/content/goddard/parker-solar-probe (current) --
  302 to https://science.nasa.gov/mission/parker-solar-probe/.
- https://science.nasa.gov/mission/parker-solar-probe/ -- title "Parker
  Solar Probe - NASA Science". Launch "Aug. 12, 2018 / 7:31 UTC"; "On a
  mission to "touch the Sun," NASA's Parker Solar Probe became the first
  spacecraft to fly through the corona" ... "the Sun's upper atmosphere
  - in 2021."; "to study the heating of the solar corona, and to explore
  what accelerates the solar wind." The page gives two closest
  distances, "about 3.9 million miles (6.2 million kilometers) of the
  Sun" and "about 4 million miles (6.5 million kilometers) of the Sun's
  surface"; no distance used.

OSIRIS-APEX
- https://science.nasa.gov/category/missions/osiris-apex/ (current) --
  loads; a category listing of posts, title "OSIRIS-APEX (...) Archives
  - NASA Science". Not a mission page.
- https://science.nasa.gov/mission/osiris-apex/ -- title "OSIRIS-APEX -
  NASA Science". "OSIRIS-APEX, formerly OSIRIS-REx"; rendezvous "June
  2029."; Apophis "rare close encounter with Earth in April 2029."

## F. Visitor words and links: comets

Tsuchinshan (C/2023 A3)
- https://en.wikipedia.org/wiki/C/2023_A3_(Tsuchinshan-ATLAS) (current)
  -- loads. "also known as the Great Comet of 2024"; "discovered by the
  Purple Mountain Observatory in China on 9 January 2023"; perihelion
  "on 27 September 2024," "when it became visible to the naked eye."
- NASA search (science.nasa.gov comet Tsuchinshan-ATLAS C/2023 A3):
  only image pages (www.nasa.gov/image-detail/pettit-comet-c2023a3-and-a-meteor).
  No NASA body page; Wikipedia stays.

ATLAS (C/2024 G3)
- https://en.wikipedia.org/wiki/C/2024_G3_(ATLAS) (current) -- loads.
  "Dubbed the Great Comet of 2025, it was the brightest comet of 2025";
  "discovered by the Asteroid Terrestrial-impact Last Alert System
  (ATLAS) survey on 5 April 2024"; "After perihelion the comet
  reappeared in the southern hemisphere."; "It became clearly visible
  with naked eye and on 18 January its tail was reported to be 4
  degrees long,".
- NASA search: APOD picture pages only
  (science.nasa.gov/image-article/apod-2025-february-5-comet-g3-atlas-setting-over-a-chilean-hill/).
  Wikipedia stays (it passes the rule; slice 1 kept passing links).

West (C/1975 V1)
- https://en.wikipedia.org/wiki/Comet_West (current) -- loads. "Comet
  West, formally designated as C/1975 V1, 1976 VI, and 1975n, was a
  comet described as one of the brightest objects"; "one of the
  brightest objects to pass through the inner Solar System in 1976";
  "As the comet passed within 30 million km of the Sun, the nucleus was
  observed to split into four fragments."; "The first report of the
  split came around 7 March 1976". No phrase about a bright tail.

McNaught (C/2006 P1)
- https://science.nasa.gov/solar-system/comets/ (current) -- title
  "Comets", a general page; does not mention McNaught. FAILS the rule.
- https://en.wikipedia.org/wiki/C/2006_P1_(McNaught) -- loads. "Great
  Comet of 2007"; "discovered on 7 August 2006 by British-Australian
  astronomer Robert H. McNaught"; "It was the brightest comet in over
  40 years, and was easily visible to the naked eye for observers in
  the Southern Hemisphere in January and February 2007."
- NASA search: SOHO and APOD picture pages only; no NASA body page.

C/2025 K1 and pieces B, C, D
- https://theskylive.com/c2025k1-info (current, all four) -- failed.
- https://science.nasa.gov/asset/hubble/fragmenting-comet-c-2025-k1/
  (reached first as science.nasa.gov/?p=1206950 from a search, then
  fetched directly) -- title "Fragmenting Comet C/2025 K1 - NASA
  Science". "Hubble caught K1 fragmenting into at least four pieces,
  each with a distinct coma"; "just a month after K1's closest approach
  to the Sun."; images "taken consecutively on Nov. 8, 9, and 10, 2025."
- https://www.stsci.edu/contents/news-releases/2026/news-2026-010 --
  title "NASA's Hubble Unexpectedly Catches Comet Breaking Up", March
  18, 2026. "Though it had been intact just days before, K1 fragmented
  into at least four pieces while Hubble was watching."; "had just
  passed its closest approach to the Sun and was heading out of the
  solar system."; "published Wednesday in the journal Icarus." No
  break-up date or estimate given.
- The orrery's "~Oct 16" break-up and "Icarus Feb 2026" are not what
  these pages say; removed. "This record is Fragment A" rests on no
  page or record; removed.

PANSTARRS (C/2025 R3)
- https://in-the-sky.org/data/object.php?id=CK25R030 (current) --
  blocked.
- https://en.wikipedia.org/wiki/C/2025_R3_(PANSTARRS) and
  https://en.wikipedia.org/wiki/C/2025_R3_(PanSTARRS) -- both load; the
  article title is "C/2025 R3 (PanSTARRS)". "The comet was discovered
  by PanSTARRS in images obtained on 8 September 2025."; "is a
  hyperbolic Oort cloud comet"; "On 11 April the comet was spotted with
  naked eye, with an estimated magnitude of 5.1."; "its ion tail was at
  least 7 degrees long" (8 April); "little dust tail was visible". Its
  outbound-ejection sentence rests on JPL Horizons data (summary); not
  used. No phrase about Jupiter or "gas-rich".

Borisov (C/2025 V1)
- https://theskylive.com/planetarium?obj=c2025v1 (current) -- failed.
- https://en.wikipedia.org/wiki/C/2025_V1_(Borisov) -- lands on a
  "Comet Borisov" list page, not an article: "C/2025 V1 (Borisov), an
  Oort cloud comet with a weakly hyperbolic eccentricity of
  1.0082+/-0.0015" (plus-minus written plainly). No discovery date.
- https://en.wikipedia.org/wiki/Comet_Borisov -- about 2I/Borisov; does
  not mention C/2025 V1.
- A web search for its discovery date found only news and amateur
  sites, none an authority. The date is removed.
- https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=C%2F2025%20V1
  -- loads, title "Small-Body Database Lookup"; nothing about the comet
  shows without JavaScript. Used as the link, as slice 1 used JPL's
  database page for 2025 PY1.

1I/'Oumuamua (A/2017 U1)
- https://www.jpl.nasa.gov/news/solar-systems-first-interstellar-visitor-dazzles-scientists/
  (current) -- loads; "Solar System's First Interstellar Visitor
  Dazzles Scientists", Nov. 20, 2017. "the first confirmed object from
  another star."; "was discovered Oct. 19 by the University of Hawaii's
  Pan-STARRS1 telescope." PASSES; unchanged.
- https://science.nasa.gov/solar-system/comets/oumuamua/ -- loads,
  "'Oumuamua - NASA Science": "The first known interstellar object to
  visit our solar system,"; "discovered Oct. 19, 2017 by the University
  of Hawaii's Pan-STARRS1 telescope."

2I/Borisov (C/2019 Q4)
- https://science.nasa.gov/solar-system/comets/2i-borisov/ (current) --
  loads, "Comet 2I/Borisov - NASA Science". "Comet 2I/Borisov is the
  first confirmed interstellar comet."; "Only one other visitor from
  another solar system has been spotted,"; discovered by Gennady
  Borisov "on Aug. 30, 2019." PASSES; unchanged.
- Wikipedia (Comet_Borisov, above): "It was discovered by the Crimean
  amateur astronomer and telescope maker Gennadiy Borisov on 29 August
  2019 UTC". The day differs from NASA's; month only. NASA's spelling
  of the name is used, as NASA's page is the link.

3I/ATLAS (C/2025 N1)
- https://science.nasa.gov/blogs/planetary-defense/2025/07/02/nasa-discovers-interstellar-comet-moving-through-solar-system/
  (current) -- loads; published July 2, 2025, updated February 9, 2026;
  the NASA-funded ATLAS survey telescope in Rio Hurtado, Chile, "first
  reported observations of a comet that originated from interstellar
  space." PASSES; unchanged.
- https://science.nasa.gov/solar-system/comets/3i-atlas/ -- loads,
  "Comet 3I/ATLAS - NASA Science". "Comet 3I/ATLAS is the third known
  object from outside our solar system"; "first reported observations
  to the Minor Planet Center of comet 3I/ATLAS on July 1, 2025."

Wierzchos (C/2024 E1)
- https://apod.nasa.gov/apod/ap260217.html (current) -- 302 to
  https://science.nasa.gov/image-article/apod-2026-february-17-tails-of-comet-wierzchos/,
  which loads: "APOD: 2026 February 17 - Tails of Comet Wierzchos -
  NASA Science". "shows a 5-degree long ion tail as well as three
  shorter dust tails." No mention of carbon dioxide.
- https://en.wikipedia.org/wiki/C/2024_E1_(Wierzchos) -- loads.
  "discovered on 3 March 2024 by Polish astronomer Kacper Wierzchos";
  "Cometary emission activity for C/2024 E1 has been driven by carbon
  dioxide (CO2)."; "C/2024 E1 (Wierzchos) is a hyperbolic Oort cloud
  comet"; "three distinct dust tails spaning near 90 degrees"
  (Wikipedia's spelling).

## Counts

26 entries: 12 spacecraft, 14 comet entries (C/2025_K1 is one live
entry with a commented-out twin above it). JPL names read: 26 of 26.
Spacecraft spans read: 12 of 12, 24 error lines. Comet Lookups: 14 sb,
14 mb (all mb "no matches found"). SBDB reads: 14 comets plus the
discovery query. Fetches that failed: the wrong-host Lookup (all
queries), the shell route to JPL, and four current links (theskylive
twice, in-the-sky, ESA search).
