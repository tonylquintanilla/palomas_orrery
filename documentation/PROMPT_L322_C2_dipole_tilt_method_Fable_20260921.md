# Request for an opinion: how the store holds a figure its source defines but does not print

Built on orrery `a318b3ecfed1ffaa290e8b34ed1ef63caa59295d`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `b17fd92704054e83424651585aa68a393ecb3d92`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both HEADs were read live with `git ls-remote` on 2026-09-21 and both
repositories were cloned at those SHAs.

**Rules this work runs under.** Fetch `PROJECT_INSTRUCTIONS.md` (v3.66)
and `skills/provenance-discipline/SKILL.md` (version 2.16) from the
orrery at `a318b3ec`. If you are running inside Tony's Project with the
skills installed, confirm instead that the provenance-discipline copy
you loaded reads 2.16. Tony named the key skills for this question as
provenance, the store and significant digits; all three live in
provenance-discipline. The sections it turns on are: The Status Line,
with The Unit Field and The Read Field; Measured Is the Goal, Declared
Is the Fallback; The Access Standard; One Value, One Home; Report to the
Figures You Have, and The Figure Count Is a Declared Field (Rules 1 to
8, including The ceiling); The Store Carries the Verified Figure; and
the Field Note on transcribing headline figures. For how the store is
read, also open the docstring of `constants_rows.py` and the headers of
`test_derived_figures.py` and `test_dimensions.py`.

**In your reply, name the rule files and sections you actually read.**

From Claude Opus 5, carried by Tony | 2026-09-21
Type: REVIEW REQUEST, Mode 7 (collegial). No code is asked for.
Addressed to Claude Fable 5.1, who reviewed the C2 build manifest twice
(`documentation/REVIEW_L322_C2_manifest_fable_20260921.md` and
`documentation/REVIEW_L322_C2_manifest_fable_second_look_20260921.md`).

---

## Who is asking, and who decides

Tony Quintanilla, PE, is a retired civil and environmental engineer. He
is not a programmer. He directs the project, carries documents between
models, and makes every ruling. The code's quality comes from that
collaboration, not from Tony writing it.

This request exists because I put a question to Tony that he ruled is
not his. His words, 2026-09-21: "this is not a judgment problem. it is
how we store values in the store. if the method is not clear, we need to
figure that out." So the question below is METHOD. The answer should
resolve the same way next month for a different body and a different
constant, and it should end up written in the skill. Where the skill
already settles part of it, say which section. Where the skill is
silent, propose the wording, marked as proposed.

---

## What was found

The C2 build is under way from
`documentation/BUILD_MANIFEST_L322_C2_magnetosphere_20260920.md`.
Section 4.2 of that manifest flags `EARTH_DIPOLE_TILT_DEG` as a lead,
not a finding: its note says 9.6 is "rounded to a tenth of a degree" and
records NOAA's 9.41, and the builder was to open Alken et al. (2021) and
record what it prints. It does not print a tilt.

**What was opened, 2026-09-21, by Claude Opus 5.**

- Alken et al. (2021), open access at
  https://link.springer.com/article/10.1186/s40623-020-01288-x, full
  text. Title as printed: "International Geomagnetic Reference Field:
  the thirteenth generation", Earth, Planets and Space 73, article 49.
  Authors as printed: P. Alken, E. Thebault, C. D. Beggan and 62 others.
  The text prints no tilt angle. It says the geomagnetic poles are
  calculated from the three degree-1 Gauss coefficients and lie where
  the dipole axis meets a sphere of radius 6371.2 km. Its Table 2 holds
  the coefficients and its Table 4 the pole positions; both table pages
  refuse automated access.
- The coefficients in digital form, NOAA's file
  https://www.ngdc.noaa.gov/IAGA/vmod/coeffs/igrf13coeffs.txt, which the
  paper names as the digital form of its Table 2. As printed, in nT:

  | Epoch | g(1,0) | g(1,1) | h(1,1) |
  | --- | --- | --- | --- |
  | 2010.0 DGRF | -29496.57 | -1586.42 | 4944.26 |
  | 2015.0 DGRF | -29441.46 | -1501.77 | 4795.99 |
  | 2020.0 IGRF | -29404.8 | -1450.9 | 4652.5 |
  | 2020-25 secular variation, nT per year | 5.7 | 7.4 | -25.9 |

**What they give.** The tilt of the dipole axis from the rotation axis is
atan2(sqrt(g11^2 + h11^2), |g10|). Computed in the session from the
printed coefficients at full digits:

| Epoch | Tilt, degrees | Change over the previous 5 years |
| --- | --- | --- |
| 2010.0 | 9.983977 | |
| 2015.0 | 9.686947 | -0.2970 |
| 2020.0 | 9.410531 | -0.2764 |
| 2025.0, as 2020.0 plus five years of secular variation | 9.163737 | -0.2468 |

**Three things follow.**

1. The stored 9.6 matches no epoch the row names. It falls between 2015
   and 2020. This is not a rounding of a verified figure, which The
   Store Carries the Verified Figure would settle directly: the cited
   source does not contain the stored value at all.
2. The row's note says the tilt decreases "about 0.05 deg per decade".
   The source's own coefficients give about 0.5 to 0.6 degrees per
   decade, ten times that. The same sentence is served in the gallery.
3. The row says "epoch 2020-2025". Across that span the source's own
   numbers move the tilt from 9.41 to 9.16 degrees.

The row's note also records NOAA stating 9.41 from WMM2020 and 9.21 from
WMM2025. Those are a different model (the World Magnetic Model) and
neither page was opened.

---

## What I read the skill as settling -- check it

1. The 9.6 cannot stay. A citation has to be true, not just present,
   and the read verdict is that the source disagrees (the protocol's
   Fetched vs Recalled, and The Read Field).
2. The value is the one the cited source actually gives, worked from its
   printed numbers at full digits and rounded once, at the reporting
   step (Rules 4 to 6).
3. The row's source names what was opened (The Access Standard).
4. IGRF-14 exists: the Springer page lists "International geomagnetic
   reference field: the fourteenth generation", published 29 June 2026.
   It was not opened. Moving to it changes which work the row cites,
   which The Store Carries the Verified Figure calls a re-sourcing with
   its own access check, so it is recorded and not done in C2.

---

## The question: what form does the store require for this row?

Four candidate forms. I do not know which the skill requires, and that
is the question.

**A. Three measured rows and a derived tilt.** `g(1,0)`, `g(1,1)` and
`h(1,1)` at 2020.0 become measured store rows, unit `nt`, each with
source, status, figure count and read line. The tilt becomes an
expression over them. This matches Rule 6 (the store holds the
derivation, never a computed result at rest) and Rule 4. It adds three
rows that section 12 of the manifest excludes ("any new measured or
declared constant"). Tony's position is that a storage method is not a
scope ruling: if the method requires the rows, they are required.

**B. One measured row with its working on a `# Derived:` line.** The
tilt is typed as the computed number, and the arithmetic is written in a
comment. `EARTH_GM_KM3_S2` has this shape for IERS's unit conversion,
and the bow shock cut angle had it for hours to degrees. Against it:
`constants_rows.py` treats such a row as a literal whose arithmetic
lives in prose; `test_dimensions.py` lists it NOT CHECKABLE; manifest
section 4.4 moved the bow shock cut angle off exactly this shape so
Earth could close with nothing listed as not checkable (section 14);
and the typed number is a computed result at rest. GM's conversion is
exact and linear in one input. This is a nonlinear function of three
measured inputs.

**C. Re-home to an open source that prints the tilt for a named epoch.**
The row stays a typed measured value. Nothing that prints it has been
opened. This changes the cited work, so it is a re-sourcing.

**D. Something else.**

**Sub-questions.**

1. Which form, and which section of the skill requires it? If none does,
   propose the rule as skill wording, marked as proposed.
2. The Field Note says to transcribe headline figures and never compute
   them from parts unless the source says the parts sum. Here the
   source prints no headline figure but does state how the pole, and so
   the tilt, is computed from the coefficients. Does that count as the
   source saying so, or does the note point toward form C?
3. Under form A, what does each coefficient row's `# Source:` name: the
   NOAA file, which is what was opened, with Alken et al. (2021) Table 2
   as the work it transcribes, or the reverse?
4. Figure count. The file prints the 2020.0 coefficients to 0.1 nT and
   states no uncertainty. The paper points to Lowes (2000) for IGRF
   errors; not opened. Counting gives five figures (from g11 and h11),
   so 9.4105. The ceiling says implied uncertainties alone never set a
   ceiling. Is counting therefore the answer?
5. The epoch. The coefficients are a snapshot at 2020.0 plus a predicted
   rate to 2025.0, and the tilt moves by a quarter of a degree across
   the span the row names. Is the row the 2020.0 value, with its words
   saying 2020.0 and not 2020-2025? Or does quoting one number for a
   span make the relation approximate, so that show-or-cap applies and
   the count is capped, or the span is shown?
6. What else moves. The list below is what quotes the value or its
   drift today. Which of these must change in the same build (The
   Correction Does Not Travel), and which are recorded for later?

---

## What quotes the value today

Orrery at `a318b3ec`:
- `constants_new.py`, `EARTH_DIPOLE_TILT_DEG`: the value 9.6, and its
  note's sentences on rounding to a tenth and on drifting "about 0.05
  deg per decade".
- `planet_visualization_utilities.py`: the comment at line 693, and the
  `PLANET_DIPOLE['Earth']` note and hover strings at lines 723 and 733,
  which type "~9.6 deg" and the same drift rate. The table's
  `tilt_deg` already reads the store row.
- `earth_visualization_shells.py`: comments at lines 869 and 1046 that
  mention "the sourced 9.6" and "the real 9.6-degree magnetic tilt".

Gallery at `b17fd927`:
- `data/objects_config.json`, `van_allen_belts.magnetic_tilt`: the
  value is served from the store by pointer, so the mirror moves it; its
  `source` string types "Rounded to a tenth of a degree" and the "0.05
  deg per decade" drift, which only the words tool can change.
- `gallery/feature_renderers.js`, the belt hover: prints the served
  tilt, then types "(IGRF-13, epoch 2020-2025)" in the page.
- `gallery/solar_system_20260907_earth_shells_moon_gallery.json` and
  `..._mobile.json`: static card exports whose dipole cone hover types
  "~9.6 deg" twice each.
- `documentation/fixture_hovers_cdfa74c3.json`, an older fixture.

---

## What comes back

A return document, anchored to the SHAs you read, that:
- names the rule files and sections you actually read;
- answers sub-questions 1 to 6, each with the skill section it rests on,
  or with proposed skill wording where the skill is silent;
- says whether the answer changes what C2 builds, and where;
- says plainly anything above that you think is wrong, including my
  reading of what the skill settles.

## Meanwhile

Earth cannot be marked a finished slice while this row is unsettled, so
nothing from C2 is delivered to Tony until the answer is in. I will keep
building the rest of the orrery patch in the sandbox so that only this
row waits.

---

Written September 21, 2026 with Anthropic's Claude Opus 5.
