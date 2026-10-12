<!-- Doc-Kind: hand | Design record for L-401 (the orrery's distance digits, printed by the errors JPL states): Tony's rulings of 2026-10-11, the discovery list, the three outside reviews and what they settled, the decisions still open, and the method the build follows. Zero code. Also the session record of build 1 of L-431 (orbital periods) working against JPL. -->
# L-401 (the orrery's distance digits): the design talk's rulings

Built on orrery 28a4636717920e86965f2e1777f3bf92386d1bb6 at
https://github.com/tonylquintanilla/palomas_orrery ("L431_4 _5 period in
hovers"); gallery e3536c8732d7b62faa5c09515e4b7f1d1c10af9c at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read, not
touched.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 11, 2026 with Anthropic's Claude Opus 5.5.

- Type: DESIGN SESSION (zero code), the second half of the session
  that built L-431's first build.
- Companions: the three review requests and returns, and their
  comparison, in `documentation/` under `REVIEW_L401_distance_digits_*`.
- Skills read this session, each matching the manifest:
  ledger-and-session-records 1.20, horizons-orbital-mechanics 1.2,
  provenance-discipline 2.28, provenance-cross-check 1.0,
  orrery-coding-conventions 1.10, agentic-pre-test 1.3,
  safe-file-editing 1.13. No skill version was cut.

## 1. Read this first

- *L-401 is next, by Tony's word.* It goes ahead of everything else on
  the Sun's and Earth's lists.
- *Most of the design is settled.* Three outside reviewers answered the
  same nine questions; where they agreed, or an earlier ruling of
  Tony's decides, it is settled (section 4).
- *Two rulings tonight:* a speed with no stated accuracy is printed to
  its distance's precision; the typed sky-position table comes out,
  settled now as part of this item.
- *Still open:* three small decisions (section 5), then the first
  build, the body hover.

## 2. Tony's words, in order

1. On seeing L-431's hover beside the distances: "the orbital periods
   look reasonable, but not the distances."
2. "It should be included as part of the braid and theme work for the
   sun and earth rooms."
3. "actually, let's promote L401 to next. accuracy and precision are
   fundamental. let's do it here. we have room."
4. "let's talk this through instead of a questionnaire. this is not
   simple."
5. "Please prepare and request to Fable and GPT and Gemini for their
   opinions. This is highly technical and my instinct only partially
   helpful."
6. On the speed: "Meters per second suggests precision limited by
   distance", then, offered two readings, "Reading 1": the speed's
   precision follows from the distance's, with no separate floor.
7. On the sky-position table: "let's follow Fable's recommendation."
   Then, having misread the question: "i think we should settle this
   now too" -- with this item, not as one of its own.

## 3. Discovery: where the orrery prints a computed number

A search of every module for a fixed-width number printed beside a
unit, and for the two shared formatters, found 376 sites in 110
functions across 34 files. By kind:

- The body hover, the first slice: `visualization_utils.format_detailed_hover_text`
  and its two formatters in `formatting_utils.py`, ten decimal places
  of an AU and ten significant figures of a kilometre. One function
  builds it for the static plot, the animation and the social export.
- Its sky-position line: `celestial_coordinates.py`,
  `MAJOR_BODY_UNCERTAINTIES` and `get_precision_note` (settled with
  this item, section 5).
- Markers on the plot: `apsidal_markers.py` (perihelion, aphelion,
  Kepler position, closest approach, encounters) and the
  closest-plotted-point hovers. Their dates ride L-431's build 2.
- Orbit hovers: `idealized_orbits.py`, 16 functions.
- Encounters and close approaches: `spacecraft_encounters.py`,
  `close_approach_data.py`.
- The fly-to buttons and the parameters window.
- Not this item: shells (store rows, already under the Figures rule),
  the stars (`sgr_a_*`, `exoplanet_*`), console prints.

## 4. Settled, by the reviews' agreement or an earlier ruling

Presented to Tony as settled on 2026-10-11; he went on to the open
questions. The evidence for each is in the comparison file.

1. **Planets and Pluto** keep the three 2014 rows (Folkner et al.,
   DE430). The 2021 DE440 paper gives fit residuals, not position
   accuracy, and says Uranus and Neptune are "statistically consistent
   with DE430" (read by GPT, Fable and Claude).
2. **The Moon** gains a row from the same 2014 report: "The present-day
   lunar orbit is known to submeter accuracy", stored as its place, 1
   metre (Fable; the build reads it before writing the row).
3. **Small bodies** take JPL's own 3-sigma uncertainty. Fable found,
   and Claude re-ran, that Horizons' vector query with
   `VEC_TABLE='2xr'` returns the 1-sigma position and velocity
   uncertainties with the position itself. Sedna from the Sun,
   2026-10-12: R_s 85,939.995 km; three times that is 257,820 km,
   against quantity 39's 257,817.569 km.
4. **No stated error** (the planets' moons in a planet-centred plot,
   spacecraft, Lagrange points, barycentres, the Sun as a body): print
   to whole kilometres, the website's floor, with a plain sentence that
   JPL states no accuracy for it. Never ten figures; never a dropped
   line. "No error" is its own state in the code, never a tiny invented
   one. A moon in a Sun-centred plot uses its planet's row as a floor
   (Fable).
5. **The level is 3-sigma**, and the box says in words which kind of
   figure it is: a published accuracy for the planets, a computed one
   for the date for a small body.
6. **Another centre:** the larger of the two bodies' errors (Tony's
   ruling of 2026-10-01, "use whichever is larger").
7. **Units:** AU, kilometres and light time carry the same error, each
   placed by its own Report test.

## 5. Ruled tonight, and still open

Ruled:
- **The speed** (Tony, "Reading 1"): a small body's speed uses JPL's
  velocity uncertainties, combined into one bound (Fable). Any other
  body's speed is printed to the same relative precision as its
  distance, and the box says so. No separate metres-per-second floor.
  This can ADD digits: Mercury's speed earns about 41.92415 km/s.
- **The sky-position table** (Tony, "follow Fable's recommendation",
  then "settle this now too"): the typed values come out, with the
  ", typical" fallbacks; the line says JPL gives no uncertainty where it
  gives none, and says "as seen from Earth". Part of this item, in its
  first build, since that build opens the same hover. Kept for later:
  Fable's sourced figure for a planet, from its position row and its
  distance from Earth.

Open, one at a time at the next talk:
1. The box's shape: one light-time line (light-minutes under an hour,
   light-hours above); the surface line only where the centre has a
   surface; plain numbers, no scientific notation. All three reviewers
   proposed these.
2. L-431 build 1's sentence "JPL lists no orbit uncertainty for this
   body", which Fable shows is false of JPL for a planet; with Tony's
   word on the period hover's wording as a whole.
3. The speed of a body whose distance has no stated error (moons
   seen from their planet, spacecraft): Reading 1 gives it nothing to
   follow. The floor with a sentence, as for its distance, is the
   obvious candidate.

## 6. Method the build follows (not Tony's; recorded so it is not re-asked)

- Small bodies' positions are fetched with `VEC_TABLE='2xr'`, by a
  direct call to the Horizons API: astroquery 0.4.11 cannot ask for it
  (its request sets no VEC_TABLE). Columns are read by name (R_s, VR_s,
  VT_s, VN_s), never by position. No extra query.
- The sigma level is written into every field name (`range_3sigma_km`).
- An error is keyed by body, centre and date.
- Gemini's suggestion to fold quantity 39 into the existing sky-position
  query would give the range from Earth, not from the plot's centre:
  not used.
- Owed to horizons-orbital-mechanics at L-401's build, in one version
  with what L-431 owes it: the vector-table uncertainties and the
  astroquery limit; the two-centre test and its saved choice; SBDB's
  lookup of a pinned record by Horizons' name.

## 7. L-431 build 1, confirmed working

- Tony ran `patch_L431_4` and `_5` on 2026-10-11 and pushed them at
  28a4636. The patch's live check (his copy
  `documentation/WHERE_WE_ARE_10-11-26_1812_run_record.md`) asked JPL
  for four bodies: Encke's and Mercury's elements fetch and period
  query "agree"; 3I/ATLAS "none (open orbit)".
- His plot at 19:41 UTC saved period records for Mercury (around the
  Sun, its year change 31 seconds), Sedna (around the barycentre,
  JPL's uncertainty 1,864 days) and Encke (around the Sun, year change
  0.15 days). Tony: "the orbital periods look reasonable".
- His first screenshots showed the old hover because the orrery window
  was open before the patch ran; reopening it fixed that.

## 8. Tony-actions

- (do) Delete `patch_L401_1_on_the_room_lists_20261011.py` from the
  orrery folder. It was never run, and it put L-401 after L-421.
- (do) Run `patch_L401_2_design_close_20261011.py`, then
  `orrery_maintenance_run.py`; move the patch into `documentation/`;
  commit and push. The review files are already in `documentation/`.
- (decide, at the next talk) Section 5's three open questions.

Session record written October 2026 with Anthropic's Claude Opus 5.5.
