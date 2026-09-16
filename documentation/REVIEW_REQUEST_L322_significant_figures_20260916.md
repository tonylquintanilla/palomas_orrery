# Review request -- significant figures in the constants store

Built on orrery `ebdc55cc4668c297d78ff1d46d2880b3cd78635f`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `72a49552aa6ba4b21c2f58e3c5fe53f7d198590c`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Rules this work runs under: also fetch, at the orrery SHA above,
`PROJECT_INSTRUCTIONS.md` (protocol v3.60),
`skills/provenance-discipline/SKILL.md` (version 2.12),
`skills/interactive-exhibit/SKILL.md` (version 1.3) and
`skills/orrery-coding-conventions/SKILL.md` (version 1.9). If you are
running inside the Paloma's Orrery Project, the protocol and skills are
already resident; say which copies you used.

Written by Claude Opus 5 in the Orrery Project, 2026-09-16, for Claude
Fable 5.1. Ledger item L-322, open question (d). A design round: no
code, no patches, no ledger handles.

---

## Who this is for

Tony Quintanilla, PE, is a retired civil and environmental engineer. He
is not a programmer. The codebase's structure is the product of his
collaboration with AI models, not something he wrote unassisted, so do
not read the code's polish as a programmer's fluency. He runs scripts
with VS Code's Run button. He decides what the project should be; how
the work is done is a technical matter, and he has said this question
is one. Write your reply so he can read it: plain sentences, and a
short explanation of any project term the first time you use it.

## The question, in Tony's words

His objective, stated 2026-09-16:

- Keep the formula and the full calculated answer. When a value is
  displayed, round it to the significant figures the constant's row
  declares, the way you write the final result of a problem.
- On 2026-09-12 he asked that certain values be calculated once and
  stored at their significant figures. His reason: calculated results
  can differ from one calculator to another, so pre-calculating
  simplified things. That was not a ruling to eliminate formulas,
  especially for values used once.
- "How you determine and consistently enforce significant figures in
  code and skills is a technical issue."

Your job is that technical design. The reference he supplied:

```
https://en.wikipedia.org/wiki/Significant_figures
```

Points from it that bear on this, paraphrased: keep extra digits
through intermediate steps and round only the final result; an exact
number has unlimited significant figures; products and quotients are
limited by the fewest significant figures among the inputs, sums and
differences by the coarsest decimal place; trailing zeros in a whole
number are ambiguous; and stating the count explicitly is one of the
recognised ways to remove that ambiguity.

This request deliberately carries no design from the session that
wrote it, so that your answer is independent. If you are inside the
Project, state in your header whether you searched past conversations,
and what you found if you did.

---

## Pre-flight, before anything else

Fetch `constants_new.py` at the orrery SHA and quote two lines: the line
that assigns `EARTH_BOW_SHOCK_STANDOFF_RADII`, and the first line of the
`# Derived:` comment beneath it. If you cannot fetch at that SHA, say so
and stop.

---

## What exists today

Measured by Claude at the SHAs above. Tags: [measured] means counted or
run; [read] means read in the file. Check what you can and say what you
could not reproduce.

**1. The store's shape.** `constants_new.py` is the orrery's single file
of verified numbers. It holds 112 top-level assignments: 81 typed
numbers (65 floats, 16 integers), 25 formulas, 5 containers
(`GRAVITATIONAL_INFLUENCE_RANGE_AU`, `CENTER_BODY_RADII`,
`KNOWN_ORBITAL_PERIODS`, `stellar_class_labels`,
`spectral_subclass_temps`), and one date (`HORIZONS_MAX_DATE`). 28 rows
carry a `# Unit:` line, all of them Earth rows. 30 carry a `# Status:`
line. [measured] The file's own docstring says derived values are
computed from primary constants and never hardcoded independently.
[read]

**2. The 25 formula rows.** `EARTH_INNER_CORE_RADII`,
`EARTH_OUTER_CORE_RADII`, `EARTH_LOWER_MANTLE_KM`,
`EARTH_LOWER_MANTLE_RADII`, `EARTH_UPPER_MANTLE_RADII`,
`EARTH_GEOSTATIONARY_RADIUS_KM`, `EARTH_GEOSTATIONARY_RADII`,
`EARTH_LEO_INNER_KM`, `EARTH_LEO_OUTER_KM`, `EARTH_LEO_INNER_RADII`,
`EARTH_LEO_OUTER_RADII`, `EARTH_STRATOPAUSE_RADII`,
`EARTH_THERMOPAUSE_RADII`, `SOLAR_RADIUS_AU`, `LIGHT_MINUTES_PER_AU`,
`AU_PER_LIGHT_YEAR`, `CORE_AU`, `RADIATIVE_ZONE_AU`,
`CHROMOSPHERE_PHYSICAL_RADII`, `SPEED_OF_LIGHT_M_S`,
`EARTH_HILL_SPHERE_KM`, `EARTH_HILL_SPHERE_RADII`, `SOLAR_MASS_KG`,
`M_PER_AU`, `SGR_A_DISTANCE_LY`. [measured] Claude's reading, not
verified: five of them convert between exactly defined quantities and
so carry no significant-figure limit -- `SOLAR_RADIUS_AU`,
`LIGHT_MINUTES_PER_AU`, `AU_PER_LIGHT_YEAR`, `SPEED_OF_LIGHT_M_S`,
`M_PER_AU`. Two are a sourced or chosen coefficient times the solar
radius: `CORE_AU` (0.2) and `RADIATIVE_ZONE_AU` (0.713).

**3. Where a figure count is stated today.** No row has a dedicated
line for it. Fourteen rows state a count in comment prose, in several
wordings [measured]:

| Row | Stored as | Wording on the row |
|---|---|---|
| `EARTH_INNER_CORE_KM` | 1221.5 | "5 sig figs" |
| `EARTH_INNER_CORE_RADII` | formula | "5 significant figures" |
| `EARTH_OUTER_CORE_KM` | 3480.0 | "4 sig figs" |
| `EARTH_OUTER_CORE_RADII` | formula | "4 significant figures" |
| `EARTH_D660_DEPTH_KM` | 660.0 | "2 sig figs" |
| `EARTH_LOWER_MANTLE_RADII` | formula | "4 significant figures" |
| `EARTH_UPPER_MANTLE_KM` | 6346.6 | "5 sig figs" |
| `EARTH_UPPER_MANTLE_RADII` | formula | "5 significant figures" |
| `EARTH_GEOSTATIONARY_RADIUS_KM` | formula | "report 42,164 km" |
| `EARTH_LEO_OUTER_RADII` | formula | "report 1.03 and 1.31" (covers both LEO rows) |
| `EARTH_MAGNETOPAUSE_STANDOFF_RADII` | 10.25 | "REPORT 10.25" |
| `EARTH_BOW_SHOCK_STANDOFF_RADII` | 13.51 | "REPORT 13.51" |
| `SOLAR_RADIUS_AU` | formula | "consistent to 6 sig figs" (about an older typed value) |
| `LIGHT_MINUTES_PER_AU` | formula | "consistent to 5 sig figs" (about an older typed value) |

`EARTH_LOWER_MANTLE_KM` (6371.0 - 660) is noted in prose as good to
units, a decimal-place limit rather than a figure count. [read]

**4. Typed numbers do not reliably show their figures.** 23 of the 81
typed numbers end in ".0". Two disagree with their own prose:
`EARTH_OUTER_CORE_KM = 3480.0` says four figures, and
`EARTH_D660_DEPTH_KM = 660.0` says two. [measured]

**5. The one test that reads a count.** `test_derived_figures.py`, wired
into `orrery_maintenance_run.py`. [read]

1. It selects rows whose `# Status:` line contains "derived". Today that
   is only the two standoff rows. The 25 formula rows carry no status
   line and are never examined.
2. For each selected row, a hand-written formula in the test file
   recalculates the value from the current input constants.
3. It finds "REPORT" in the row's comment and counts the digits after
   it.
4. It rounds its result to that count and fails if the result differs
   from the reported figure, or if the stored value differs from it.
5. It fails if a selected row is stored as a formula rather than a
   typed number, and it fails on a derived row it has no formula for.

**6. Two skill passages that disagree.** In
`skills/provenance-discipline/SKILL.md`: "Report to the Figures You
Have" [QUALITY] says compute at full precision, keep the derivation as
a formula, and round when reporting. "A Derived Row Stores the Figure
Its Sources Support" [CRITICAL] says a derived row stores the rounded
figure, with the arithmetic recorded and a test that recomputes it. Its
scope paragraph covers rows whose inputs are declared constants, which
is all 25. Between them sits "The Store Carries the Verified Figure"
[CRITICAL]: a measured value at rest keeps every figure its source
supports, and rounding happens at the reporting step. Tony wants the
first passage kept; the second's reason is as he restated above. [read]

**7. The gallery today has its own calculator.**
`gallery_maintenance_run.py` in the gallery repo reads the orrery's
source text and evaluates it with a small evaluator of its own:
numbers, names, add, subtract, multiply, divide, power -- no function
calls such as `tanh`. Its store drift check compares each served value
against the store EXACTLY when the units are the same, and within
1e-12 relative when it converts units. So today the served file must
carry exactly what the store carries. One reason the magnetopause row
became a typed number was that this evaluator could not compute Shue's
formula (`test_derived_figures.py` header). [read] The page's
JavaScript is a third calculator.

**8. The page chooses how many digits to print.** In the gallery's
`gallery/feature_renderers.js`: the raw number for solar radii (line
1439), four decimal places for Earth radii (lines 1309 and 1442), two
for a `radius_fraction` (line 781), one for the belts (lines 689-707),
two for the standoffs (lines 1675 and 1736). [read] Built with the
page's own code from the served data, three hovers print more than
their sources support [measured]:

- Sun, chromosphere: "Radius: 1.002874802357338 solar radii". The input
  is a textbook "about 2000 km".
- Earth, Hill sphere: "Radius: 234.6388 Earth radii". The row says to
  report 1.50e6 km.
- Earth, geocorona: "Radius: 100.0000 Earth radii". The source says the
  hydrogen is detected to at least 100 Earth radii.

**9. Served values that point at formula rows.** Eleven pointers in the
gallery's `data/objects_config.json` name a formula row: `CORE_AU`,
`RADIATIVE_ZONE_AU`, `SOLAR_RADIUS_AU`, `CHROMOSPHERE_PHYSICAL_RADII`,
`EARTH_LOWER_MANTLE_KM`, `EARTH_STRATOPAUSE_RADII`,
`EARTH_THERMOPAUSE_RADII`, `EARTH_LEO_INNER_RADII`,
`EARTH_LEO_OUTER_RADII`, `EARTH_GEOSTATIONARY_RADII`,
`EARTH_HILL_SPHERE_RADII`. Seven of them are served at full calculated
precision (the chromosphere and the six Earth radii rows). [measured]

**10. The planned export, not yet built** (L-322 rulings 6 to 8, in
`LEDGER_CONSOLIDATED.md`). The orrery will write one export of the
whole store; a check keeps it matched to the store's bytes; the
gallery stops reading orrery source; values are joined to gallery
presentation in the assembler. Under that design only Python
calculates a stored value. The unit field is being written body by
body, Earth first, one visit per row writing `# Unit:` and
`# Status:`. Whatever this review settles for figures is written in
that same visit.

---

## Questions

Answer each. Lead with your recommendation in one plain sentence, then
the reasons, then what it costs.

**Q1. Formula or pre-calculated number.** For a derived value, should
the row hold the formula, a pre-calculated number, or either -- and by
what rule does a row get one or the other? Tony's own criterion is
above. Make the rule mechanical enough that it gives the same answer
next month for a different row. Say what happens to the two standoff
rows under your rule.

**Q2. Declaring the count.** Where and how is a row's significant-
figure count declared so that a program can read it? Cover typed
measured values (item 4), formula rows, exact values (defined
constants and conversions between them), declared drawing choices such
as `EARTH_LEO_LOWER_ALTITUDE_KM = 200.0`, and sums and differences
limited by a decimal place rather than a figure count.

**Q3. Who rounds, and where.** Should rounding happen in the export, in
the page, or both? What does the gallery's exact-match check then
compare? How does the count reach the page, and how should the page
format it (JavaScript's `toPrecision` switches to exponent form for
some values)? The orrery's own hover text also prints stored values:
does the same declared count serve it?

**Q4. The check.** What should `test_derived_figures.py`, or whatever
replaces it, verify so that it cannot pass while blind? Include how it
finds every derived row rather than only rows with a status line, what
it can actually verify about a declared count (the count itself is a
person's judgement against the source), and what fails when an input
constant moves.

**Q5. The two skill passages.** How should item 6's passages be
reconciled so the skill says one thing? Substance only; the wording is
written in the Project.

**Q6. Tools.** Is an established library worth using -- an
uncertainty-propagation or significant-figure package, or `astropy`,
which is already a dependency -- or is a declared count per row the
right size for this project? Weigh what Tony can maintain.

**Q7. The framing.** What in this request is wrong or missing?

Out of scope: L-322's questions (a), (b), (c) and (e) except where they
touch figures; any edit to the served file.

---

## Reply format

1. A header naming your model, your effort tier, whether you ran inside
   or outside the Orrery Project, and whether you searched past
   conversations.
2. The anchor line, with the same two SHAs.
3. **What I read.** Each rule file by path and version, and each code
   file with the line ranges you read. A reply that does not name them
   will be read as not having read them.
4. Your answers to Q1 to Q7, with claims tagged [measured], [read] or
   [inferred].
5. Name items rather than counting them. Where a list would be long,
   name the kinds and give the path where the instances live.
6. Plain language throughout. Tony reads this.

Request written September 2026 with Anthropic's Claude Opus 5.
