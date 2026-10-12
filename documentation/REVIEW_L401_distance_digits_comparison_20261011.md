<!-- Doc-Kind: hand | The three reviews of L-401 (the orrery's distance digits) side by side: where they agree, where they split, what Claude checked itself, and the decisions left for Tony. -->
# L-401 (the orrery's distance digits): the three reviews compared

Built on orrery 28a4636717920e86965f2e1777f3bf92386d1bb6 at
https://github.com/tonylquintanilla/palomas_orrery; gallery
e3536c8732d7b62faa5c09515e4b7f1d1c10af9c at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, not
touched.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 11, 2026 with Anthropic's Claude Opus 5.5.

- The request: `documentation/REVIEW_L401_distance_digits_{fable,gpt,gemini}_20261011.md`.
- The returns, saved as received:
  `REVIEW_L401_distance_digits_return_fable5.1_default_20261011.md`,
  `REVIEW_L401_distance_digits_return_gpt6_high_20261011.md`,
  `REVIEW_L401_distance_digits_return_gemini_2.5pro_high_20261011.md`.

## 1. How much each return is worth

| Reviewer | Rule files read | Sources opened | Weight |
|---|---|---|---|
| Claude Fable 5.1 (default effort) | all five, from a clone at 28a4636 | yes; quoted; ran two live Horizons queries | full |
| GPT-6 (high) | all five, at 28a4636 | yes; quoted | full |
| Gemini 2.5 Pro (high) | none | none; every source marked "recall" | reasoning only; its numbers are not used |

Checked by Claude (Opus 5.5) this session, through the chat's web-fetch tool:
- Park et al. 2021 (DE440), as GPT and Fable quoted: fit residuals for
  most planets (Juno ranges "about 13 m", Cassini "about 3 m"), Uranus
  and Neptune "statistically consistent with DE430", and no orbit
  accuracy in kilometres for any planet. The inner planets' orbits
  "are aligned with ICRF3 with an average accuracy of about 0.2 mas".
- Fable's finding, re-run: Horizons' vector table with `VEC_TABLE='2xr'`
  returns Sedna's 1-sigma position and velocity uncertainties with the
  position. For 2026-10-12, from the Sun: R_s 85,939.995 km, T_s 1,682
  km, N_s 1,141 km; VR_s 7.989e-5, VT_s 2.863e-5, VN_s 3.916e-6 km/s.
  Three times R_s is 257,820 km, against quantity 39's 257,817.569 km.
  The API page: modifier codes on tables 1 and 2 "trigger output of
  formal statistical uncertainties", "for asteroids and comets only".

## 2. Question by question

| Q | Fable | GPT | Gemini | Reading |
|---|---|---|---|---|
| 1 Planets | keep the 2014 rows; DE440 states none | keep the 2014 rows; DE440 is residuals | DE440 numbers (recall) | AGREE, two to one with evidence: keep the 2014 rows |
| 1 Small bodies | vector table `2xr`, R_s x3 | quantity 39 | quantity 39 | AGREE on JPL's own figure; Fable's route gets it with the position |
| 1 The Moon | new row: 2014 "submeter", place 1 m | 2014 "submeter" as a start | LLR (recall) | Fable and GPT agree |
| 1 Moons, spacecraft, Lagrange points, barycentres | no source; Q3. Moons in a Sun-centred plot: at least the planet's row | no source; say so | per-class sources (recall) | AGREE: no source yet |
| 2 Level | 3-sigma (vector 1-sigma x3) | 3-sigma as given | 3-sigma as given | AGREE |
| 2 Words in the box | which kind, in words | which kind; no "+/-" for the planets' place | a "+/-" line | Fable and GPT agree |
| 3 No stated error | floor (whole km) + plain sentence; never ten figures with a note | floor + plain sentence; the floor is not an error | floor + note | AGREE |
| 4 Velocity, small bodies | VR, VT, VN combined, x3: a sourced bound | no full velocity error; caveat or omit | range-rate as a proxy | SPLIT; Fable's has a source GPT did not have |
| 4 Velocity, planets | same relative precision as the distance, declared and said | coarse with caveat, or omit | DE440 floor (recall) | SPLIT: Tony's |
| 5 Other centre | the larger of the two errors | root-sum-square only if independent; quantity 39 excludes the centre | root-sum-square | Tony already ruled "use whichever is larger" (2026-10-01) |
| 6 Sky-position table | remove; a live CRITICAL finding; own ledger item | remove; no "+/-" where JPL gives none | replace with DE440 values (recall) | Fable and GPT agree: remove |
| 7 Derived lines | same error per unit; one light-time line; surface line only for a real surface | same | same | AGREE |
| 8 Cost | none: `2xr` rides the position fetch (astroquery cannot ask; a direct call) | one more query, cached by body, centre, date | fold into the Earth query (wrong observer) | Fable's route, checked live |
| 9 | the rule can ADD digits; build 1's "JPL lists no orbit uncertainty" is false of JPL; label the sigma level in field names; digits may flicker in animations | motion is not error; "no error" must be its own state, never a tiny invented one; the surface line for centres with no surface | geometric vs apparent; no scientific notation; AU and km rounded apart | all useful |

## 3. Settled by agreement or by an earlier ruling

1. Planets and Pluto keep the 2014 rows. The Moon gains a 1 metre row
   from the same report's "submeter".
2. Small bodies take JPL's own 3-sigma, from the position fetch.
3. A number with no stated error prints at a stated floor, whole
   kilometres, with a plain sentence. Never ten figures; never a line
   dropped. "No error" is its own state in the code.
4. The level is 3-sigma, and the box says which kind of figure it is.
5. Another centre: the larger of the two errors (Tony, 2026-10-01).
6. Kilometres, AU and light time carry the same error, each placed by
   its own Report test.

## 4. Decisions for Tony, one at a time

1. Velocity: for small bodies, Fable's combined bound; for planets and
   the rest, the same relative precision as the distance (said in the
   box), or a floor with a sentence, or no speed line.
2. The sky-position table: remove its typed values and open it as its
   own item.
3. The box's shape: one light-time line; the surface line only where
   the centre has a surface; no scientific notation.
4. Build 1's sentence "JPL lists no orbit uncertainty for this body",
   which Fable shows is false of JPL for a planet.

## 5. Method, for the skill once built

- The vector table's `2xr` uncertainties, read by column name, and that
  astroquery cannot request them (a direct call, as `orbital_period.py`
  calls the Small-Body Database).
- The sigma level written into every field name (`range_3sigma_km`).
- Key an error by body, centre and date.
