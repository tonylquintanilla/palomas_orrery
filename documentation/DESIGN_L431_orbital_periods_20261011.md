<!-- Doc-Kind: hand | Design record for L-431 (orbital periods from JPL): Tony's rulings of 2026-10-10, what JPL's numbers show for Encke and Sedna, the proposed rule for which centre and how many digits, every place the orrery reads a period, and the questions the next session starts with. Zero code. -->
# L-431 (orbital periods from JPL): design record

Built on orrery 9f1547821a1957544f0ae94a77cc64c5a3ab4114 at
https://github.com/tonylquintanilla/palomas_orrery ("L395 L421") and
gallery a7d1a542ae5b6d26dc3c658c339fcf721d181780 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read,
not touched. Written October 10-11, 2026 with Anthropic's Claude Opus
5.5, at the close of the L-421 (the typed facts) orrery session.

- Type: DESIGN RECORD (zero code). The build is the next session's.
- Tony, 2026-10-10: "i would want to start with this issue. it is
  important for how we model the orbital periods for all bodies,
  especially highly perturbed ones." The next session opens here.
- Skills that fire on this work: horizons-orbital-mechanics (1.2),
  provenance-discipline (2.28; "A Computed Position Prints What Its
  Errors Earn"), orrery-coding-conventions (hover text),
  agentic-pre-test, safe-file-editing.

## 1. Read this first

- *Ruled by Tony on 2026-10-10:* the orrery takes each body's period
  from JPL Horizons (its "PR" line), for every body that has one, not
  just Encke; the hover shows that fetched period, not the typed table;
  and the period prints only the digits its errors earn.
- *Found:* for a distant body the period depends heavily on which
  centre the elements are taken around. Around the Sun, Sedna's period
  changed by 370 years between 2025-10-10 and 2026-10-10. Around the
  solar system's barycentre (its centre of mass) it changed by 7 days.
  For Encke the reverse holds: the Sun is the steady centre.
- *Proposed, for Tony to confirm or change:* ask JPL for both centres a
  year apart and use the one whose period moves less; print to the
  larger of JPL's stated uncertainty and that one-year change.
- *Questions the next session starts with:* section 7.

## 2. What started it

Tony's look at Encke in the orrery window (run record of 2026-10-10,
attached in chat): Encke's hover has no orbital period. The hover's
"Known Orbital Period" line reads only `KNOWN_ORBITAL_PERIODS` in
`constants_new.py`, a hand-typed table, and Encke was never added to
it. Tony then attached Encke's osculating elements from Horizons and
pointed at the PR line: "the sidereal orbit period in seconds (PR) is
available from the osculating ephemeris". His rulings followed, in his
words:

- "we should implement this as a general update not just for encke,
  but for all objects with PR."
- Asked whether the hover would show the new PR and not the fallback:
  yes.
- "can you determine the correct number of significant digits? Encke
  is one thing, Sedna is another, for example."

## 3. What JPL says (read 2026-10-10 and 2026-10-11)

Horizons, elements table (EPHEM_TYPE=E), at 2025-Oct-10 and
2026-Oct-10 00:00 TDB. Encke is record 90000091 ("2P/Encke", source
JPL#K273/22, elements epoch 2023-Dec-13); Sedna is 90377 ("90377 Sedna
(2003 VB12)", source JPL#51, epoch 2018-Oct-20). PR is in seconds;
days and years below are PR / 86400 and / 31,557,600 (Julian years).
Read through the chat's web-fetch tool, which quotes the lines; the
heliocentric 2026 values match Tony's two attached Horizons files.

| Body, centre | PR 2025-10-10 (s) | PR 2026-10-10 (s) | in days, 2026 | change in a year |
|---|---|---|---|---|
| Encke, Sun (500@10) | 1.042507355591868E+08 | 1.042260028993200E+08 | 1206.32 | 0.29 days |
| Encke, barycentre (500@0) | 1.040374836468454E+08 | 1.033675327314541E+08 | 1196.38 | 7.75 days |
| Sedna, Sun (500@10) | 4.076403195668284E+11 | 3.959569681377396E+11 | 4,582,835 | 370 years |
| Sedna, barycentre (500@0) | 3.594328436666299E+11 | 3.594322752931561E+11 | 4,160,096 | 6.6 days |

In years, 2026: Encke 3.3027 around the Sun; Sedna 11,389.72 around
the barycentre, and 12,547 around the Sun (12,917 a year earlier).
The header of Tony's Sedna file, at its 2018 epoch, gives 10,514 years
around the Sun. Same body, same orbit solution, three answers from
10,514 to 12,917 years: the Sun's own wobble around the barycentre,
mostly from Jupiter, is large next to Sedna's slow motion, so its
heliocentric elements swing.

JPL's Small-Body Database (sbdb.api, full precision), the fit's
uncertainty:

- Encke, orbit K273/20, epoch JD 2460147.5 (2023-Jul-22), condition
  code 1: per 1207.248132847095 d, sigma 0.00021413 d.
- Sedna, orbit 51, epoch JD 2461200.5 (2026-Jun-09), condition code 1:
  per 4630851.183590915 d (12,679 years), sigma 1864 d (5.1 years);
  a 543.7195289104732 au, sigma 0.1459 au.

SBDB's period is heliocentric at its own epoch, so for Sedna it is a
fourth answer. Its sigma measures how well the observations fix the
orbit, not which centre to use; it still bounds the digits.

## 4. Proposed: which centre

Ask Horizons for the period around the Sun and around the barycentre,
each at the plot date and a year later. Use the centre whose period
changes less, and say which in the hover. On the numbers above this
picks the Sun for Encke and the barycentre for Sedna, which is what
the physics says: inner bodies orbit the Sun, distant ones orbit the
whole solar system's mass.

Moons and the Pluto system are different: their centre is their
planet (or the Pluto-Charon barycentre), already set by
`center_body` in `osculating_cache_manager.py`. Whether the two-centre
test applies to them is question 3 in section 7.

## 5. Proposed: how many digits

provenance-discipline's "A Computed Position Prints What Its Errors
Earn" (Tony, 2026-10-01: "use whichever is larger"), applied to a
period. Two errors:

- The change in a year: how much the osculating period itself moves.
  A perturbed body has no single period; this is the honest bound on
  "the" period at the plot date.
- JPL's sigma from SBDB, where the body has one.

Print to the larger, each unit (days, years) placed by its own error:

- Encke: the year's change, 0.29 days, beats the sigma, 0.0002 days.
  "3.303 years (1206 days)".
- Sedna: the sigma, 5.1 years, beats the year's change, 0.02 years.
  "11,390 years (4,160,000 days)".

Planets and the Moon have no SBDB entry; they print by the year's
change alone and the hover says so (the rule's own clause for a body
with no source-accuracy row).

A hyperbolic orbit has no period: Horizons prints PR as 9.999E+99 (to
be confirmed live; question 1). The hover then says "none (open
orbit)", as the table's None entries do now.

## 6. Where the orrery reads a period today [at 9f15478]

`KNOWN_ORBITAL_PERIODS` (`constants_new.py`, line 3036): 132 typed
entries in days, 13 of them None, none with a Source line. Its readers,
by what they do:

Shown to Tony:
- `visualization_utils.format_detailed_hover_text` (lines 866-891):
  the "Known Orbital Period" line, "{years:.4f} Earth years ({days:.2f}
  days)" -- the fixed widths this design replaces. Special case: Pluto
  around the Pluto-Charon barycentre, typed 6.387 days.
- `palomas_orrery.py` lines 1298-1320: the period for the fetch's
  position record, then one computed from `planetary_params` a.
- `palomas_orrery.py` line 1022: the precession warning's "orbits in
  range", defaulting to 1.0 day when the table has no entry.
- `orbital_param_viz.py` line 282: fills a missing period.

Used to compute:
- `apsidal_markers.py` lines 910, 1170, 1308: the next perihelion and
  aphelion dates from TP plus the period. Here the period changes where
  a marker is DRAWN, not only what a hover says.
- `apsidal_markers.py` line 1688: mean motion from
  `orbital_period_days`, else Kepler's law from a.
- `idealized_orbits.py` lines 3434 (satellites), 4162 (the Moon, with
  27.321661 typed as a default), 5845 (aphelion dates).
- `export_orbit_cache.py` line 411: a diagnostic only.

The fetch: `orbit_data_manager.query_horizons_elements` (lines
1677-1900) reads a, e, incl, w, Omega, Tp, MA, TA and q from
astroquery's `elements()` and does not keep the period;
`osculating_cache_manager.fetch_osculating_elements` (line 367) stores
those in `data/osculating_cache.json` (115 entries).

## 7. Questions for the next session, in order

1. **Read the column live.** astroquery's `elements()` is documented as
   returning the period as "P", in days (from Horizons' PR). Confirm on
   Encke, Sedna and one hyperbolic comet, and what an open orbit gives.
   Method; no ruling needed.
2. **Which centre.** Confirm section 4, or choose another rule. Tony's.
3. **Moons and the Pluto system.** Their centre is their planet. Do
   they print by the year's change alone? Method, unless the answer
   changes what the hover says.
4. **The drawn orbit has the same problem.** The orrery draws a
   distant body's ellipse from its heliocentric elements. Sedna's
   heliocentric semi-major axis was 540 au on 2026-10-10 against 506 au
   around the barycentre, and it moves year to year. A period from the
   barycentre beside an ellipse drawn around the Sun disagree. Is this
   the same build or its own item? Tony's: it is how the orrery models
   perturbed bodies, his words in section 2.
5. **Cost.** Two centres times two dates is four queries per body per
   refresh, against one now. The cache's refresh interval may carry it
   (perhaps the year's change only on first fetch). Method.
6. **The typed table.** Once the fetched period is in the hover, the
   table is a fallback for when JPL is unreachable. Its 132 entries are
   one ledger class on L-431, not chased (The Braid). Whether the
   fallback prints at all, or the hover says "not fetched", is Tony's.
7. **The apsidal markers.** They compute dates from the period. Moving
   them to the fetched period changes drawn markers, which is a Mode 5
   look. Same build or after? Tony's.

## 8. What does not change

- Encke's place in the comet list moves to the top in this session's
  close (Tony: "i order the comets by date of first apparition by this
  Horizons Id"). That is a list order, separate from this design.
- The website (gallery) prints no orbital period today; nothing there
  waits on this.
