<!-- Doc-Kind: hand | JPL's answers of 2026-11-01 for the six periodic comets asked by designation with CAP, four ways, through the orrery's own code; the test of section 4.4 of the comet-pins brief, and what reading the readers found before the switch. A record. -->
# Check: the six periodic comets asked by designation with CAP (L-470)

Tony Quintanilla, PE | Claude Opus 5.5 (the orrery's Claude Code session) | November 1, 2026

Built on orrery 6a434ed87956548e7c93f03a23d54c0d2f12e1f0 at
https://github.com/tonylquintanilla/palomas_orrery (branch main), with
gallery b6574a0fa374be2faf526d7c5e5b6f8988515652 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io read only.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: DOCUMENTATION (a record of JPL's answers; no code changed by it).
It is the test of section 4.4 of
`COORD_L470_orrery_comet_pins_backstop_brief_20261101.md`. The switch
itself (4.5 to 4.9) was not built this session; why is in section 3.

## 1. What was asked

For each of the six comets the orrery pins to a record number, four
questions, one every 1.5 to 2 seconds:

- astroquery (the orrery's installed 0.4.9.post1),
  `Horizons(id=<des>, id_type='designation', location='@sun',
  epochs=2461345.5).elements(closest_apparition=True, cache=False)`,
  whose COMMAND astroquery writes as `"DES=2P; CAP;"`;
- the same with `no_fragments=True`, `"DES=2P; CAP; NOFRAG;"`;
- a raw address through `horizons_check.live_fetch`, COMMAND
  `DES=<des>;CAP;` quoted with `urllib.parse.quote(..., safe="=")` as
  `period_url` quotes `command_of`'s output, so every `;` is sent as
  `%3B`;
- the same with `;NOFRAG;`.

Each answer was read back with `horizons_check.parse_record` (the name
on JPL's header line, the first `Rec #:` and its `Soln.date:`) and
JPL's own clock on its header line.

## 2. JPL's answers

Every answer is LIVE: JPL's clock in each header reads 2026-Nov-01,
12:07:55 to 12:08:44 (JPL's clock, Pacific). This is the fresh read the
brief asked for; the coordinating session's copies of Nov 1 carried the
clock of Oct 31, 19:05 (its 4.2).

| Comet | Asked as | JPL's name | Record | Soln.date | The pin |
|---|---|---|---|---|---|
| Tempel 2 | 10P | 10P/Tempel 2 | 90000214 | 2026-Oct-22_15:52:05 | 90000214 |
| Schaumasse | 24P | 24P/Schaumasse | 90000356 | 2026-Jul-07_05:58:32 | 90000356 |
| Howell | 88P | 88P/Howell | 90000901 | 2026-Oct-14_16:22:22 | 90000901 |
| Churyumov-Gerasimenko | 67P | 67P/Churyumov-Gerasimenko | 90000703 | 2026-Sep-04_10:25:07 | 90000703 |
| Halley | 1P | 1P/Halley | 90000030 | 2025-Nov-21_15:57:34 | 90000030 |
| Encke | 2P | 2P/Encke | 90000091 | 2026-Oct-22_15:51:34 | 90000091 |

All four forms gave the same name, record and solution date for each
comet: 24 answers, 0 disagreements. Each equals the pin in
`celestial_objects.py` and the coordinating session's fetch of Oct 31.

THE TRAP, ASKED AGAIN. The same question with a bare `;` in the address
(`COMMAND='DES=2P;CAP;'` unencoded) was refused by JPL with HTTP 400,
which `live_fetch` reports as "could not reach JPL". On Oct 31 the same
mistake returned Encke's whole list of 61 records. Either way the
encoded form is the only one that answers with one record, and a
refusal is loud where a list was quiet.

## 3. Why the switch waits for the next orrery session

The test passed, so by the brief the readers switch next. Reading them
at 6a434ed found that the orrery's PLOTTING recognises a periodic comet
by its record number or by `id_type` in places the brief's list (4.5)
does not name. With the six asked as `id: '2P', id_type:
'designation'`, each would stop treating them as comets, and nothing
would error:

- `palomas_orrery.py`, `_is_comet` (line 1699): a comet is an id
  beginning `C/` or `A/`, a name beginning `C/` or `<n>I/`, or a numeric
  id of 90000000 or more. "2P" is none of these. Its caller at line
  1778 is the perihelion-orbit pass.
- `palomas_orrery.py`, the comet-tail tests at lines 2618 (the
  animation's spec list), 6386 (the static plot) and 7730 (the
  animation's frames): `id_type in ['smallbody', 'id']`, commented
  "Numeric IDs for ambiguous comets". A comet asked by designation
  gets no tail.
- `orbital_period.py` (lines 406 and 451) and `position_accuracy.py`
  (line 232) recognise a pinned record by the pattern `^9\d{7}$`, as
  the brief says.

So the switch is a sweep of the orrery's comet tests as well as of its
Horizons calls, and its proof is Tony's look at a plot with Encke's
tail, not only the suites. That is more than this session's room, and
the brief's own rule is to stop before section 4 rather than leave it
half built. Nothing of section 4 was written into the code.

Two facts for that session's design, from this test:

- astroquery adds CAP only through the query methods' own
  `closest_apparition=True`, not through the constructor, so a helper
  that every reader calls (the brief's recommendation) has to own the
  query call, or subclass `Horizons` and set the default there.
- requirements.txt asks for `astroquery>=0.4.6`, so GitHub's computer
  installs the newest each night and Tony's machine has 0.4.9.post1.
  The COMMAND each writes for CAP should be read on both before the
  helper is trusted (`elements(get_query_payload=True, ...)`).

Written November 1, 2026 with Anthropic's Claude Opus 5.5.
