<!-- Doc-Kind: hand | Build record for L-431 (orbital periods from JPL), build 1 of 3: the period in the orrery's hovers. What was built, how it was tested, what Tony looks at, and what waits for builds 2 and 3. -->
# L-431 (orbital periods from JPL): build 1, the period in the hovers

Built on orrery 41e9a1d569098d35f327870ca30050cb83645924 at
https://github.com/tonylquintanilla/palomas_orrery ("Update
WHERE_WE_ARE_10-11-26_1311_run_record.md"); gallery
e3536c8732d7b62faa5c09515e4b7f1d1c10af9c at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read, not
touched.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 11, 2026 with Anthropic's Claude Opus 5.5.

- Type: BUILD. Patches `patch_L431_4_period_in_hovers_20261011.py`
  (the code) and `patch_L431_5_records_20261011.py` (the ledger, Where
  We Are, this record), run in that order in the orrery folder.
- Built from `documentation/DESIGN_L431_orbital_periods_rulings_20261011.md`,
  sections 2 to 5, and L-431 in the ledger.
- Skills loaded, each matching the manifest: ledger-and-session-records
  1.20 (the obligation the design session carried is discharged),
  horizons-orbital-mechanics 1.2, provenance-discipline 2.28,
  orrery-coding-conventions 1.10, agentic-pre-test 1.3,
  safe-file-editing 1.13. No skill version was cut.

## 1. Read this first

- The orrery's hovers now print each body's orbital period from JPL,
  around the centre it is steadiest about, to the digits its errors
  earn. A period from the typed table says it is typed.
- Nothing drawn moves. The ellipses and the perihelion and aphelion
  markers still use what they used (build 2).
- Your part: run the two patches, read the live check the first one
  prints, then look at Encke, Sedna and Mercury and approve the words
  (section 4).

## 2. What was built

`orbital_period.py`, new:
- One Horizons query per centre asks for the period at the plot date
  and a Julian year later (a year earlier, if Horizons refuses the
  later date).
- At a body's first fetch, the two-centre test: around the Sun and
  around the solar system's barycentre; the centre whose period moved
  less in the year is kept, and the choice is saved. A later fetch
  asks only the chosen centre: two queries in all, the elements and
  the period, not four. If the chosen centre's period then moves more
  than the other centre's did when the choice was made, the test runs
  again. (The rulings record left this to the build; this is the
  choice.)
- Moons and the Pluto system keep the centre the orrery gives them,
  with no test.
- JPL's stated uncertainty of the orbit, from the Small-Body Database,
  for small bodies only. A pinned record number such as Encke's
  90000091 cannot be found there, so it is looked up by the name
  Horizons gives the record: "2P/Encke" becomes "2P".
- The digits: the larger of the year's change and that uncertainty,
  years and days each placed by its own error, by the Report test of
  provenance-discipline (The ceiling). Never fewer than one figure.
- The fallback order for showing: the fetched period saved in the
  orbit cache; the same record carried forward when a later fetch
  could not get one; then the typed table, marked as typed.

The orbit cache, `data/osculating_cache.json`, keeps a `period` record
beside each entry's elements: the period in days, the centre, the plot
date it is for, the date it was fetched, the year's change, the SBDB
uncertainty and what SBDB said, the larger error and which one it was,
the saved test, and whether the elements fetch's own period agreed. It
is written only by a fetch you accept in the "Update Orbital
Elements?" box. The direct fetches in `idealized_orbits.py` and
`spacecraft_encounters.py` do not ask for it and cost what they did.

Readers, each reading through `orbital_period.py`:
- The hover, `visualization_utils.format_detailed_hover_text`: the
  static plot, the animation and the social export all build it there.
- The orbital parameters window's Orbital Period row.
- The precession note's orbit count, in `palomas_orrery.py`.
- `fetch_position`'s period record in `palomas_orrery.py`. Nothing reads
  that record today; it follows the rule so a later reader is right.

Also: the elements fetch keeps Horizons' period as `P_days`, and the
period record says whether it agrees with the period query.
`D_PER_JULIAN_YEAR` (365.25 days, exact, IAU Style Manual, "SI Units",
Table 5, read 2026-10-11) and its unit token `d_per_yr`, so neither the
years nor the year's step divides by a bare number. The export carries
the row and the token, as it already carries `S_PER_HOUR`; the
gallery's 27 offline checks pass with the new export in place.

## 3. How it was checked

Before building, through the chat's web-fetch tool (2026-10-11):
- Horizons labels the period PR, and prints 9.999E+99 for C/2025 N1's
  open orbit.
- SBDB gives the period as `per` with a sigma (Sedna "1900" days
  without full precision; the design read 1864 with it).
- astroquery 0.4.11 asks for AU and days and names PR "P", in days
  (its own source, `jplhorizons/__init__.py`).

The sandbox cannot reach JPL. So the end-to-end live check is yours:
the first patch, after it writes, asks JPL for Encke, Sedna, Mercury
and 3I/ATLAS and prints each record and its hover. It writes nothing.

In the sandbox, on a throwaway copy, with JPL faked from the rulings
record's section 5:
- The hovers print exactly section 5's three lines (below).
- Sedna's centre is the barycentre; Mercury's and Encke's the Sun.
- 3I/ATLAS prints "none (open orbit)".
- The Moon, viewed from Earth, is measured around Earth with no test.
- A refresh asks Horizons twice: the elements, then the chosen centre.
- A failed period query keeps the last fetched record.
- Pluto viewed from the Pluto-Charon barycentre keeps its typed 6.387
  days, marked typed, and never borrows the Sun-centred period.
- The orrery window opens headless; the maintenance run passes 23 of
  23; the push gate holds at 0 Tier-1; the whole tree stays at 292.

## 4. Your look: the words, old and new

The words beside each figure are yours to approve
(orrery-coding-conventions, Hover Text Is Written for the Visitor). Old
hover, every body: "Known Orbital Period: 0.2408 Earth years (87.97
days)".

New, as the sandbox printed them from section 5's numbers:

Encke
    Orbital period: 3.303 years (1206 days)
    Around the Sun, from JPL Horizons, fetched 2026-10-11.
    Rounded to how much the period changes in a year.

Sedna
    Orbital period: 11,390 years (4,160,000 days)
    Around the solar system's center of mass, from JPL Horizons, fetched 2026-10-11.
    Rounded to JPL's stated uncertainty in the orbit.

Mercury
    Orbital period: 0.2408455 years (87.9688 days)
    Around the Sun, from JPL Horizons, fetched 2026-10-11.
    Rounded to how much the period changes in a year;
    JPL lists no orbit uncertainty for this body.

A typed one (Venus, until it is fetched)
    Orbital period: 0.615198 years (224.701 days)
    Typed value, not fetched from JPL.

An open orbit
    Orbital period: none (open orbit)
    Around the Sun, from JPL Horizons, fetched 2026-10-11.

The numbers in your window will come from JPL's live answers, so they
may differ from section 5 in the last place.

Four checks:
1. Tick Encke, Sedna and Mercury, press Plot, answer Yes to each
   "Update Orbital Elements?" box. The console prints a "[L-431
   period]" line for each: the two centres' year changes and the one
   kept.
2. Hover each. The lines read as above.
3. Open the orbital parameters window and pick Encke: the Orbital
   Period row reads "1206 days (3.303 yr), JPL, around the Sun".
4. The ellipses and the perihelion and aphelion markers are where they
   were.

## 5. Found, recorded on L-431 and not chased

- 39 moons' descriptions in `celestial_objects.py` type a period, e.g.
  "Saturn orbital period: 0.94 Earth days". Their hovers will show
  that typed figure under the fetched one. One class.
- SBDB's 2P solution is not Horizons' record 90000091: its sigma read
  0.00011075 days on 2026-10-11, where L-431 recorded 0.00021413. Both
  are far below Encke's year change, 0.29 days, so the print does not
  move.
- `VIEW_TO_OSCULATING_CENTRE` in `orbital_period.py` copies the block in
  `palomas_orrery.py` that sets `osculating_center_body`. The pre-test
  checked they agree. Build 2 works on that path and gives it one home.
- Still on the typed period until build 2: the parameters window's
  estimated perihelion and aphelion dates, `apsidal_markers.py`,
  `idealized_orbits.py`.
- `get_fallback_elements` reads the plain cache key, not the
  centre-aware one. Build 2 works on that path.
- The bare 365.25s in other modules. One class.

## 6. Owed

To horizons-orbital-mechanics, once your live run shows build 1
working: the two-centre test, its choice saved at first fetch, and
SBDB's lookup of a pinned record by Horizons' name (Method Belongs to
the Skill). Not cut this session: the build has not yet been seen
working against JPL.

## 7. Tony-actions

- (do) Save both patches in the orrery folder (already there if this
  session was linked to your computer). Run
  `patch_L431_4_period_in_hovers_20261011.py`; paste its output,
  including the live check, into your run record.
- (do) Run `patch_L431_5_records_20261011.py`, then
  `orrery_maintenance_run.py`. Expect 23 of 23 and "0 TIER-1 -- the
  push gate holds"; the whole tree should not move.
- (do) The four checks in section 4.
- (decide) The hover's words, section 4.
- (do) Move both patches into `documentation/`; commit and push.

Session record written October 2026 with Anthropic's Claude Opus 5.5.
