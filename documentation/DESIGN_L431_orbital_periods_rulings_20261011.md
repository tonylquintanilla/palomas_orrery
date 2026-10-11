<!-- Doc-Kind: hand | Design record for L-431 (orbital periods from JPL): Tony's rulings at the design talk of 2026-10-11, the order of the three builds, the method the build follows, and Mercury's numbers. Zero code. Companion to DESIGN_L431_orbital_periods_20261011.md, which holds the first findings. -->
# L-431 (orbital periods from JPL): the design talk's rulings

Built on orrery 324a574f4dd50f8acdea211b1d814f577343f927 at
https://github.com/tonylquintanilla/palomas_orrery ("v3.91 and run
record") and gallery e3536c8732d7b62faa5c09515e4b7f1d1c10af9c at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read,
not touched.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 11, 2026 with Anthropic's Claude Opus 5.5.

- Type: DESIGN SESSION (zero code). The builds are later sessions'.
- Companion to `documentation/DESIGN_L431_orbital_periods_20261011.md`.
  That record keeps JPL's numbers (its section 3) and every place the
  orrery reads a period today (its section 6). Its proposals (sections
  4 and 5) are now ruled, as below, and its section 7's questions are
  all answered in section 4 here.
- Skills read: ledger-and-session-records 1.19 was the copy this
  session loaded. The repo moved to 1.20 during the session (the inner
  Oort cloud's website session cut it at 1bbd9fe1, protocol v3.91).
  The next session confirms its loaded copy reads 1.20 before ledger
  or handoff work.
- Skills the builds fire: horizons-orbital-mechanics (1.2),
  provenance-discipline (2.28; "A Computed Position Prints What Its
  Errors Earn"), orrery-coding-conventions (hover text),
  agentic-pre-test, safe-file-editing; interactive-exhibit and
  gallery-cache-builder for the website step.

## 1. Read this first

- *Every ruling Tony was asked for is made.* Seven, in section 2.
- *Three builds, in order:* the period in the orrery; then the drawn
  orbit and the perihelion and aphelion markers, with Tony's look;
  then the website. Section 3.
- *Nothing is left for Tony before the first build.* The words the
  hover prints are his to approve at the first build's look.

## 2. The rulings, in order, Tony's words

1. **Where the period comes from.** The orrery takes each body's
   period from its Horizons fetch, JPL's own PR ("sidereal orbit
   period"), for every body that has one. The typed table
   `KNOWN_ORBITAL_PERIODS` is used only when nothing has been fetched.
   Tony: "Confirmed. I agree with this approach."
2. **Which centre.** Horizons is asked for the period around the Sun
   (500@10) and around the solar system's barycentre, its centre of
   mass (500@0), each at the plot date and a year later. The centre
   whose period moves less over the year is used, and the hover names
   it. No distance threshold: nothing sources one. Tony: "Confirmed
   as recommended".
3. **How many digits.** The larger of two errors sets them: the
   period's movement over the year around the chosen centre, and
   JPL's stated uncertainty of the orbit fit (SBDB's sigma) where the
   body has one. Years and days are each rounded by their own error,
   by the Report test (provenance-discipline, The ceiling). A body
   with no SBDB entry -- the planets, the Moon and the other moons --
   prints by the year's movement alone, and the hover says so.
   Tony: "Confirmed".
4. **The typed table.** It stays as the last fallback. A hover that
   reaches it says so, with a short note such as "typed value, not
   fetched from JPL", and prints the value as typed. Its 132 entries
   are not sourced or corrected now; they stay one ledger class on
   L-431, not chased (The Braid). Tony: "Confirmed."
5. **The fallback order.** Tony asked whether the fetched period
   could be written back to the table as the next fallback. Answer:
   the orbit cache, `data/osculating_cache.json`, already does that
   job, without a program editing its own code in `constants_new.py`.
   The order is: a fresh fetch; then the last fetched period, saved
   in the cache with its centre, its date and its error; then the
   typed table with its note. The hover gives the fetch date. Tony:
   "Confirmed".
6. **The website.** Tony: "periods are basic data, for all bodies and
   should be part of the hover text." So the website step follows the
   orrery build directly, not when some room first needs it: the
   export carries each body's period with its centre, date and error,
   every body's hover in the rooms shows it, and the website's daily
   Horizons check compares the period with JPL too. Tony: "Confirmed".
7. **The drawn orbit and the markers.** The drawn ellipse is taken
   around the same centre as the period, so the hover and the drawing
   describe one orbit. The perihelion and aphelion markers use the
   fetched period, in the same fallback order. Both change what is
   drawn, so they are one build with one look. Tony: "Confirmed." and
   "Confirmed. This is the best solution."

## 3. The three builds, in order

All under L-431. The orrery and gallery each pin their own SHA.

1. **The period (orrery).** Keep PR from the elements fetch
   (`orbit_data_manager.query_horizons_elements`), store it in the
   orbit cache with the centre, the fetch date and the year's
   movement (`osculating_cache_manager.fetch_osculating_elements`),
   read SBDB's sigma where the body has one, and use the fallback
   order everywhere the period is read for SHOWING: the hover
   (`visualization_utils.format_detailed_hover_text`), the orbital
   parameters window (`orbital_param_viz.py`), the fetch's position
   record and the precession warning (`palomas_orrery.py`). The
   drawn ellipse and the markers do not change in this build. Done
   when Tony looks at Encke, Sedna and Mercury in the orrery window
   and the hovers read as section 5 below.
2. **The drawn orbit and the markers (orrery), Mode 5.** The ellipse
   around the period's centre (`idealized_orbits.py`), following the
   existing Pluto-Charon barycentre pattern, which already draws
   Pluto and Charon from elements fetched around their barycentre;
   and the markers' dates from the fetched period (`apsidal_markers.py`,
   the places named in the first record's section 6). Sedna's
   ellipse shrinks from about 540 au around the Sun to about 506 au
   around the barycentre (2026-10-10). Done on Tony's look at the
   render.
3. **The website (gallery, after the orrery builds).** The orrery's
   export carries each body's period, centre, date and error; every
   body's hover in the rooms prints it by the same digits rule; the
   Daily Run's Horizons check compares the period with JPL. It waits
   until no other session is building in the gallery.

## 4. Method the builds follow (not Tony's; recorded so it is not re-asked)

The first record's section 7, answered:

1. **The column.** astroquery's `elements()` documents the period as
   "P", in days, from Horizons' PR. The first build confirms it live
   on Encke, Sedna, Mercury and one open-orbit comet, and prints what
   it found. For an open orbit Horizons prints PR as 9.999E+99 (to be
   confirmed live); the hover then says "none (open orbit)".
2. **Which centre:** ruled, section 2.
3. **Moons and the Pluto system.** They keep the centre the orrery
   already gives them through `center_body` (their planet, or the
   Pluto-Charon barycentre). No two-centre test. They print by the
   year's movement, with the note.
4. **The drawn orbit:** ruled, section 2, item 7.
5. **Cost.** The two-centre test runs on a body's FIRST fetch, and
   its choice is saved in the cache. A refresh then asks only for the
   chosen centre, at the plot date and a year later: two queries, not
   four. A refresh that sees the chosen centre move more than the
   other did when it was chosen may re-run the test; the build decides
   and says so.
6. **The typed table:** ruled, section 2, items 4 and 5.
7. **The markers:** ruled, section 2, item 7.

Owed to horizons-orbital-mechanics at the first build's close, as
method, once the build has shown it working: the two-centre test, and
that the choice is saved at first fetch (Method Belongs to the Skill).

## 5. What the hovers will read (for the first build's look)

From JPL's numbers at 2026-10-10, by the digits rule:

| Body | Centre (chosen) | Larger error | Prints |
|---|---|---|---|
| Encke | Sun | year's movement, 0.29 d | 3.303 years (1206 days) |
| Sedna | barycentre | SBDB sigma, 1864 d (5.1 yr) | 11,390 years (4,160,000 days) |
| Mercury | Sun | year's movement, 3.7 s | 0.2408455 years (87.9688 days) |

Mercury, read 2026-10-11 from Horizons (EPHEM_TYPE=ELEMENTS, DE441,
00:00 TDB, through the chat's web-fetch tool, which quoted the lines):

| Centre | PR 2025-10-10 (s) | PR 2026-10-10 (s) | change in a year |
|---|---|---|---|
| Sun (500@10) | 7.600508693862242E+06 | 7.600505042307498E+06 | 3.65 s |
| barycentre (500@0) | 7.845795957243782E+06 | 7.778018708926311E+06 | 0.78 days |

Around the barycentre Mercury's period reads 90.8 and then 90.0 days,
against 87.9688 around the Sun. Mercury is close enough to the Sun
that the Sun's own wobble around the barycentre, mostly from Jupiter,
is a large share of its distance: Sedna's case reversed, and the
reason a fixed distance rule could not serve both. Mercury's
perihelion precession turns the orbit and moves the date of closest
approach, not the period; JPL's integration includes relativity.

The words beside each figure -- the centre, "by the year's movement
only", "typed value, not fetched from JPL", the fetch date -- are
proposed by the first build and approved by Tony at its look
(provenance-discipline: words the display's owner approved).

## 6. Skill versions this session

Tony asked at the opening for ledger-and-session-records 1.20, with
the rule recorded on L-351: every handoff, brief and design record
names his two local folders in its header beside the GitHub line. The
inner Oort cloud's website session cut exactly that version during
this session, at 1bbd9fe1 (`patch_L421_9_close_20261011.py`,
protocol v3.91), and L-351 records it landed. One skill version only,
so this session cut none. This record follows 1.20's header rule.

## 7. Tony-actions

- (do) Run `patch_L431_3_design_close_20261011.py` in the orrery
  folder, then `orrery_maintenance_run.py`, then commit and push.
- (do) If not done yet: upload ledger-and-session-records 1.20 to
  Settings > Skills.

Session record written October 2026 with Anthropic's Claude Opus 5.5.
