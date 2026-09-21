# Build Manifest -- L-322 Stage C2: Earth's magnetosphere rows get their figures and reads, and Earth closes

**Built on orrery `b9cd48440a8879f7c79207dfc181bfaaf584caf4`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `06fdad8cc16da72d00e28c8066dbcbde7f590587`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both HEADs were read live with `git ls-remote` on 2026-09-20, twice, and
both repositories were cloned there. Orrery `b9cd4844` is `ac397e52`
plus the rev2 brief; gallery `06fdad8c` is `a1a516cf` plus the
`.gitignore` repair. Every number in section 3 was measured on those
clones with the project's own tools, and every hover string in section
6 was built in node from the pushed gallery files or worked by a
separate reference script, not recalled.**

**Rules this work runs under.** Inside Tony's Project the protocol
(v3.65) and the skills load on their own. This task fires
provenance-discipline 2.15, gallery-cache-builder 1.6,
interactive-exhibit 1.4, gallery-assembler 1.3,
ledger-and-session-records 1.11, safe-file-editing 1.11 and
agentic-pre-test 1.2. A reader outside the Project fetches
`PROJECT_INSTRUCTIONS.md` and `skills/<n>/SKILL.md` for each of those
from the orrery at `b9cd4844`. Compare each loaded version line with the
protocol's manifest table and STOP on a mismatch. **In your first reply,
name the rule files you actually read.**

**Type: BUILD CONTRACT.** Written before the build, zero code.
**Prepared:** September 20, 2026 by Claude Opus 5, in the DESIGN role
for this one step. Tony Quintanilla integrator.
**Why the roles are swapped.** The rev2 brief asked a design session to
write this, and it reached an Opus session. Fable recommended, and Tony
agreed, that Opus write it here, since the reading and measuring were
already done, and that a Fable session review it BEFORE anything is
built, so the relay still has two sessions checking each other.
**For:** Claude Fable 5.1 to review; then the builder.
**Revised** September 21, 2026 by Claude Opus 5 after Fable's review of
the same date, and again after Fable's second look; section 16 lists
each finding of both and what changed.
**Replaces** the C2 part of section 6 of
`documentation/BUILD_MANIFEST_L322_earth_slice_20260919.md`, which stays
filed as the contract C1 was built under. Sections 7 to 11 of that
document still govern except where this one says otherwise.
**Built from** `BRIEF_L322_C2_design_session_rev2_20260920.md`, every
section of which is taken up below.

Who this is written for: Tony is a retired professional engineer who
builds this project by conversation with AI partners. He is not a
programmer, runs scripts from VS Code's Run button, and commits and
pushes through GitHub Desktop. The quality of the code in these
repositories is the product of that collaboration, not evidence of a
programmer at the keyboard. Write to him in plain sentences, one request
per message. He often works from his phone.

---

## 1. What C2 is, in one paragraph

C2 visits the 28 Earth constants in `constants_new.py` that still have
no figure count: the radiation belts, the dipole tilt, the three solar
wind conditions, Shue's magnetopause rows, Jelinek's bow shock rows, the
two standoffs and the magnetotail. Each gets a figure count and, where
it is in scope, a line saying who read its source. Five retire the
token `dimensionless`. The two standoffs go back from typed numbers to
arithmetic. Then Earth is marked a finished slice, and from then on a
missing field on an Earth constant fails the maintenance run instead of
being listed. Four derived rows are added so that every number the
magnetosphere hovers print is computed in the store from full digits
and rounded once at the export. The gallery follows: a check that a
drawn Earth constant and everything feeding it has been read, hover
lines that print those served numbers instead of doing arithmetic on
rounded ones, and a re-recorded fixture.

## 2. What the skill settles, and what is Tony's

Everything in this manifest is method under the skills except 2.2, 2.3
and 2.4, and the build cannot start until those are answered here. An
earlier draft also put the magnetopause's figure count to Tony as a
decision. It is not one, and 2.1 records why.

### 2.1 The magnetopause standoff carries three figures -- settled by the skill

**Tony's instruction, 2026-09-20: "See the Skill on significant
digits."** The draft had said the skill gives no method for combining
several stated uncertainties. That was wrong. Rule 3 of The Figure Count
Is a Declared Field says a stated uncertainty decides and counting is
the fallback, and the procedure the skill adopted "as recommended",
`documentation/DESIGN_L322_d_significant_figures_20260916.md` section 4,
says: "Where any input carries a stated uncertainty, propagate that
instead and let it decide." The skill's named reference, the open
Wikipedia page Significant figures (read 2026-09-20), gives the
reporting step.

**Propagate.** The standoff is Shue's equation 10 at the store's
declared solar wind: 10.2518729724 Earth radii at full precision. Shue's
Table 1 states a standard deviation on every coefficient. To first
order -- each coefficient moved up and down by its standard deviation
and the half-difference taken, a central difference -- a1 moves the
standoff by +/- 0.090, a5 by +/- 0.082, a2 by +/- 0.049, a4 by
+/- 0.015 and a3 by +/- 0.012 Earth radii. Combined by root-sum-square,
the standard propagation for independent inputs, that is +/- 0.1326,
reported +/- 0.13. The direction matters: moving every coefficient only
up gives 0.129 and only down 0.136, which round to 0.13 and 0.14, so
the method names the central difference (4.0).

**Independence is an assumption, and the row states its bound.** The
five come from one fit and the paper gives no correlations; a1 and a2
are almost certainly correlated. So the true combined figure lies
somewhere between near zero and the plain sum, 0.25. The tenths place
holds up to 0.158, so "10.3" survives the assumption at 0.13 and would
not survive at 0.25. The kilometre line holds to two figures up to
0.2479, essentially the ceiling itself. The row says all of this.

**Report.** The page says that to report a single number, choose the
one whose implied uncertainty -- half a unit in its last place -- gives a
range close to the measured one. Its own example: 3.78 +/- 0.07 kg is
best quoted as 3.8 kg, and 3.78 +/- 0.09 kg still as 3.8, "since if
4 kg was reported then a lot of information would be lost". For
+/- 0.13, the tenths place implies +/- 0.05 and the units place
+/- 0.5; the tenths place is closer on either measure. So the standoff
is reported to tenths: **10.3, three figures.**

**Two things this corrects.** The row's present "REPORT 10.25", reasoned
from the largest single effect of +/- 0.09, was already one figure too
many by the page's own 3.78 +/- 0.09 example. And counting digits alone
(two figures, from a5 = 6.6) is only the fallback, for a source that
states no uncertainty.

**What the +/- 0.13 is, and what it is not.** It is how well Shue's
coefficients were pinned down, so it says how well the MODEL's surface
is known at the declared solar wind. It is not how well the real
magnetopause is known: the same paper puts real crossings 1.23 Earth
radii (one standard deviation) from that surface, and Jelinek's
crossings sit 0.69 from theirs. Both numbers are store rows. The hover
names the model and the conditions, so "10.3" reads as what Shue's model
gives, and that is known to 0.13; the scatter is a second fact about the
real boundary, not an error bar on the first. That reading holds only if
the visitor is told the second fact (Show the Envelope), and today
neither hover says it. Fable's review, Finding 1; how to tell the
visitor is Tony's (2.3).

| | Hover, Earth radii | Hover, km |
| --- | --- | --- |
| Today | Sunward standoff: 10.25 Earth radii | = 65,376 km (0.000437 AU) |
| After C2 | Sunward standoff: 10.3 Earth radii | = 65,000 km (0.00044 AU) |

**The kilometre line carries two figures, not three, by the same
rule.** Carried from the full digits, the same uncertainty is
+/- 845.9 km, written 850. The hundreds place implies +/- 50 km and the
thousands place +/- 500 km, and 500 is the closer, so 65,387.8 km is
reported as 65,000 km. In AU it is +/- 0.00000565, written 0.0000057,
closest to the +/- 0.000005 of the fifth decimal, so 0.00044. An earlier
draft wrote 840 and 0.0000056 by converting the already-rounded 0.132:
Rule 4 broken inside the document that enforces it, and the checker of
4.7 would have failed both rows on its first run. The reference page warns of exactly this when converting units:
choose the digits that give a comparable uncertainty, not the digit
count of the other unit. An earlier draft gave 65,400 km by counting;
that was one figure too many.

**What it costs, measured.** `test_derived_figures.py` implements only
the counting fallback: a dry run declaring more than two figures fails
with "its inputs support 2". So the checker learns the uncertainty
route (4.7), and the skill writes down the method before the walk uses
it (Stage C2-0, section 4.0). Neither is a question for Tony; both are
the skill's own rule being implemented.

### 2.2 Every number the hovers print comes from the store -- and the one question

**Tony's instruction, 2026-09-20: "The single source of truth is
constants_new.py."** An earlier draft had the page recompute the
magnetopause from Shue's coefficients in JavaScript, which would have
put equation 10 in two places, and had the patch copy five numbers into
the gallery config. Both are withdrawn.

**The problem, which is Rule 4.** The export rounds the standoff to
10.3. If the page multiplies that by Earth's radius it starts from a
rounded number: "= 65,700 km" where the full digits give 65,387.8, and
"0.00043 AU" where they give 0.00044. Rule 4: "Compute from the PRIMARY
inputs at full precision; round once."

**The design.** The store computes every number the two hovers print,
from full digits, and the export rounds each once. Four derived rows
join the store (4.3a):

| New row | Computed as | Exported |
| --- | --- | --- |
| `EARTH_MAGNETOPAUSE_STANDOFF_KM` | standoff in Earth radii x Earth's equatorial radius | 65,000 km, 2 figures |
| `EARTH_MAGNETOPAUSE_STANDOFF_AU` | that / `KM_PER_AU` | 0.00044 AU, 2 figures |
| `EARTH_BOW_SHOCK_STANDOFF_KM` | standoff in Earth radii x Earth's equatorial radius | 86,200 km, 3 figures |
| `EARTH_BOW_SHOCK_STANDOFF_AU` | that / `KM_PER_AU` | 0.000576 AU, 3 figures |

They are within the audit's bound because the page renders them; they
are new rows only because the numbers had no home in the store before.
The page prints them as served and computes nothing for these lines.

**How they reach the page.** The mirror writes numbers but will not
create an entry, and the words tool writes words only. So the gallery
patch adds four entries -- `standoff_km` and `standoff_au` beside each
standoff -- and, since 2.3 was answered A, a `scatter` entry beside
each, six in all, that carry ONLY a pointer to the store row and a unit, with
`"value": null` and no figure count. The mirror then writes every number
and count from the export. Measured on throwaway copies: the mirror
fills entries of exactly that shape, "value null -> 65000.0" and
"figures (absent) -> 2", and nothing in the patch types a number.

**The question, which is Tony's.** Adding those six pointer entries is
still the patch writing `data/objects_config.json` directly, which is
the one-off exception on L-340 whose limits Tony has not ruled on. The
difference from its two earlier uses is that no number is written; the
store supplies every one. The alternative is to teach the mirror to add
an entry itself, which is a larger build and a change to one of the two
sanctioned writers.

**Recommendation: pointer-only entries, with L-340 recording the
narrow form as the standing rule** (Fable's view, Tony's decision).
**Tony's answer, 2026-09-21: yes -- "Confirmed as recommended."** From
now on a patch may add an entry to `data/objects_config.json` that holds
a pointer to a store row and nothing else; every number and count in it
comes through the mirror from `constants_new.py`. Anything more is still
not allowed without a ruling.

### 2.3 How the hovers tell the visitor about the scatter -- Tony's

Two honest ways, from Fable's review, Finding 1. The words in either are
Tony's.

| | Magnetopause hover | Bow shock hover |
| --- | --- | --- |
| **A. Keep the model's figures and add one line** (recommended by Fable and by Opus) | "Sunward standoff: 10.3 Earth radii = about 65,000 km (0.00044 AU)" and a line such as "Real crossings scatter about 1.2 Earth radii around this." | "Sunward standoff: 13.5 Earth radii = about 86,200 km (0.000576 AU)" and "Real crossings scatter about 0.7 Earth radii around this." |
| **B. Let the scatter set the digits** | "Sunward standoff: 10 Earth radii = about 70,000 km (0.0004 AU)" | "Sunward standoff: 14 Earth radii = about 90,000 km (0.0006 AU)" |

The word "about" is Fable's suggestion
(Finding 10): a visitor who multiplies 10.3 by Earth's radius gets
65,700, and "=" between the two lines is not quite honest.

A makes the two scatter rows printed numbers, so they come into read
scope (their reads are in the L-305 record) and each is served through a
pointer-only entry like those in 2.2, six entries instead of four. B
changes the skill text of 4.0: the scatter would set the count, and the
input uncertainties would only confirm it.

**Tony's answer, 2026-09-21: A -- "Confirmed as recommended."** The
exact words come to him with the other hover wording before the gallery
patch is cut (section 13, item 5).

### 2.4 The bow shock's cut angle becomes declared -- Tony confirms

Section 4.4 moves `EARTH_BOW_SHOCK_CUT_ANGLE_DEG` from measured to
declared. Moving a row that way is a demotion under a CRITICAL section
of the skill. Its twin, the magnetopause's 120 degrees, became declared
on Tony's ruling of 2026-09-14, which called the two "the same shape",
and Fable takes the manifest's side (Finding 8) on condition that Tony
says yes once. **Tony's answer, 2026-09-21: yes -- "Confirmed as
recommended."** The row's status line names this ruling.

## 3. What was measured

**The store** holds 113 top-level rows. 57 begin with `EARTH_`. All 57
carry a unit and a status; 29 carry a figure count; 12 carry a read
line. The 28 without a count are listed in section 4. Five still declare
`dimensionless`: `EARTH_MAGNETOPAUSE_SHUE_A5`, `_A6`, `_A8`,
`EARTH_BOW_SHOCK_JELINEK_EPS`, `EARTH_BOW_SHOCK_JELINEK_LAMBDA`.
`constants_rows.CLOSED_SLICES` is `()` and `TRANSITIONAL` names the two
standoffs.

**The three checkers today, and with Earth closed on a throwaway copy.**

- `test_derived_figures.py`: 31 derived rows read, 15 OK, 16 NOT YET
  MIGRATED, 1 NO DERIVED LINE (`CORE_AU`); exit 0. Closed: FAILS on
  exactly `EARTH_BOW_SHOCK_CUT_ANGLE_DEG`,
  `EARTH_MAGNETOPAUSE_STANDOFF_RADII`, `EARTH_BOW_SHOCK_STANDOFF_RADII`.
  The other 13 are outside Earth and stay named: `SOLAR_RADIUS_AU`,
  `LIGHT_MINUTES_PER_AU`, `AU_PER_LIGHT_YEAR`, `CORE_AU`,
  `RADIATIVE_ZONE_AU`, `CHROMOSPHERE_PHYSICAL_RADII`,
  `ROCHE_LIMIT_RADII`, `HAUMEA_RADIUS_KM`, `SPEED_OF_LIGHT_M_S`,
  `SOLAR_MASS_KG`, `M_PER_AU`, `PARSEC_TO_AU`, `SGR_A_DISTANCE_LY`.
- `test_dimensions.py` (needs astropy): 15 OK, 10 NO UNIT, 6 NOT
  CHECKABLE; exit 0. Closed: STILL exit 0, because NOT CHECKABLE is not
  a gap. Three of the six are Earth's (the two standoffs and the bow
  shock cut angle). C2 removes all three from that list (section 4).
- `test_constants_export.py`: 55 rows exported; hashes match. Closed:
  FAILS 34 ways -- the 28 rows without a count, the five retired tokens
  a second time, and the export's own closed-slice list.

**The dry run of this manifest's store changes** (the magnetopause at
two figures, the only count the checker accepts today; cut angle
declared; Earth closed) passed every store checker the orrery run
executes: Derived figures (30 read, 17 OK), Dimensions (17 OK, 10 NO
UNIT, 3 NOT CHECKABLE, none Earth's), the export (60 rows) and its
check, Constants relations, Status lines, Row shape, Citation
inheritance, Cross-check annotations. At four figures for the
magnetopause, Derived figures failed three ways, which shows the
checker implements only the counting fallback of Rule 3 (2.1).

**Nothing in the gallery reads the two standoffs out of the store.** The
renderers read them from the served config. The one gallery tool that
parses `constants_new.py`, the old Store drift check, examines only
links the export does NOT serve; both standoffs are served. Its own
evaluator skips an expression it cannot evaluate rather than failing, so
`np.tanh` in the store does not break it.

**The gallery at `06fdad8c`.** The pointer join counts 78 links: 45
SERVED, 28 FALLBACK, 5 ABSENT. Four of the fallbacks are Earth's -- a6,
a8, epsilon and lambda, held back by the retired token. The page asserts
`"dimensionless"` for exactly those four, in `measured(...)` calls in
`gallery/feature_renderers.js`. The mirror calls that change a RELABEL:
it refuses by default and writes it only with `--accept-relabel NAME`,
which Tony cannot pass from the Run button.

**Built with the renderer as it stands** (counts written into a copy of
the served block, the four asserts changed), three lines come out wrong:
the magnetopause km line (2.2); the bow shock's line in Earth
radii, which is printed with `S.toFixed(2)` whatever count is served,
and its km line, whose count leaves epsilon out and so gives four; and
both belt spans, printed with `toFixed(1)` whatever count is served.

## 4. Stage C2-a -- the orrery patch

One patch, run from the orrery ROOT, filed in `documentation/` after it
runs. It fingerprints every file it edits by CONTENT (line endings
normalised) and refuses on a mismatch; it keeps line endings as found;
ASCII throughout; bottom-up, transactional, and a second run refuses.

### 4.0 Stage C2-0 -- the skill writes down how a stated uncertainty decides

provenance-discipline 2.15 -> 2.16, one protocol entry (v3.66), by the
bump routine in ledger-and-session-records, BEFORE the walk: the checker
in 4.7 implements it and the walk applies it, and a convention that is
not in the skill does not travel. Six additions join Rule 3 -- which
uncertainty, an approximate relation, when the uncertainty ceiling
applies, how to propagate, how to report, and the form -- each checkable
against the page the skill already names or marked as the project's own:

- **Which uncertainty.** The route propagates the stated uncertainties
  of the INPUTS -- how well they were measured or fitted. A model's
  scatter about the data it was fitted to is a different quantity. It
  describes the real thing around the model, it is governed by the
  sentence on a relation that is itself approximate and by Show the
  Envelope, and it is shown beside the value rather than propagated
  into it.
- **An approximate relation: show or cap.** Where the source publishes
  the size of the relation's mismatch as a number the store can hold and
  the page can show, show it beside the value, as the two standoffs'
  crossing scatters are. Where it does not, cap the count and say why on
  the row, as the Hill sphere's is. This settles which of Rule 3's two
  answers applies.
- **When the uncertainty ceiling applies.** A row's ceiling -- the most
  figures it may declare -- is set by propagation whenever at least one
  measured primary in its chain STATES an uncertainty, and by counting
  otherwise. A row may always declare its ceiling or fewer. It writes
  the uncertainty form on its figures line only when it declares MORE
  than counting alone allows, so the reason for the extra figures is on
  the row; a row that counts and stays within its ceiling keeps its
  counting line. Implied uncertainties alone never set a ceiling: the
  bow shock standoff, whose chain states none, is 13.5 by counting and
  would be 13.51 if they did.
- **Propagate.** Move each primary up and down by its uncertainty and
  take the half-difference (a central difference); combine the changes
  by root-sum-square, through the whole chain from the primaries, from
  full digits -- Rule 4 applies to an uncertainty exactly as it applies
  to a value. That assumes the inputs are independent; where the source
  gives no correlations the row says so, and where the reported place
  would not survive the plain sum of the effects, the row gives both
  numbers. A primary that states no uncertainty contributes its implied
  one, half a unit in its last place; that is a full half-width, not a
  standard deviation, so it errs large. Declared conditions and exact
  numbers contribute nothing.
- **Report. What the page says:** report a single number so that its
  implied range is "close to" the measured one, since going coarser
  loses "a lot of information"; its examples are 3.78 +/- 0.07 kg and
  3.78 +/- 0.09 kg, both best quoted as 3.8 kg. **What this project
  adds, and why:** "close" is measured on a log scale, because implied
  uncertainties step by factors of ten -- a linear measure would keep
  the tenths place up to +/- 0.27 and overstate the precision five-fold
  -- and a tie goes to the coarser place. Where the uncertainty is
  printed beside the value, it takes one or two figures and the value
  ends in the same place.
- **The form.** A measured row whose source states an uncertainty writes
  it on its figures line: `# Figures: 4 -- Table 1 prints 10.22,
  uncertainty 0.10`. A derived row whose count is set this way writes
  `# Figures: 3 -- uncertainty 0.13, root-sum-square of <inputs>`, and
  the checker recomputes it.

Tony answered 2.3 on 2026-09-21 with A, so the first bullet stands as
written and the bump can be cut.

The origin line quotes Tony's instruction of 2026-09-20 and names the
magnetopause standoff as the worked case. The session that cuts the bump
ends there: a reinstall cannot be verified from inside it, so the C2
build is a new session whose first act is confirming it loaded 2.16.

### 4.1 The four tokens, in `constants_tokens.py`

All `"dimension": "named number"`, no defining constant. The names are
method and Fable should check them.

| Token | Rows | Meaning, in plain words |
| --- | --- | --- |
| `inverse_exponent` | `SHUE_A5`, `JELINEK_EPS` | the n in a power law p^(-1/n): a pure number that says how weakly a distance follows the pressure |
| `flaring_exponent` | `SHUE_A6` | how fast the magnetopause widens away from the nose; Shue's alpha, whose leading term this is |
| `log_pressure_coefficient` | `SHUE_A8` | a pure number multiplying the natural logarithm of a pressure in nanopascals |
| `shape_factor` | `JELINEK_LAMBDA` | the ratio setting how wide Jelinek's paraboloid opens against its length |

### 4.2 The 28 rows, and the four new ones

Each row gets `# Figures:` and, where marked, `# Read:`, in the same
comment block as its unit and status. Existing lines are kept; notes are
rewritten only where they state something now false.

| Row | Value | Figures | Read line |
| --- | --- | --- | --- |
| `EARTH_VAN_ALLEN_INNER_RADII` | 1.5 | 2 -- Baker (2018) prints 1.5 | builder opens Baker (2018), sec. 2 |
| `EARTH_VAN_ALLEN_OUTER_RADII` | 4.5 | exact -- a declared pick from a range | none; declared |
| `EARTH_VAN_ALLEN_INNER_BELT_INNER_EDGE` | 1.1 | 2 | builder opens Meredith (2014), intro para. 1 |
| `EARTH_VAN_ALLEN_INNER_BELT_OUTER_EDGE` | 2.0 | 1 if the page prints "2", 2 if it prints "2.0" | same |
| `EARTH_VAN_ALLEN_OUTER_BELT_INNER_EDGE` | 3.0 | 1 if the pages print "3" | Meredith (2014) and Li, Tu et al. (2024) |
| `EARTH_VAN_ALLEN_OUTER_BELT_OUTER_EDGE` | 7.0 | 1 if the pages print "7" | same |
| `EARTH_DIPOLE_TILT_DEG` | 9.6 | 2, subject to the lead below | builder opens Alken et al. (2021) |
| `EARTH_SOLAR_WIND_PRESSURE_NPA` | 2.0 | exact -- a declared condition | none; declared |
| `EARTH_SOLAR_WIND_BZ_NT` | 0.0 | exact -- a declared condition | none; declared |
| `EARTH_SOLAR_WIND_SPEED_KM_S` | 400.0 | exact -- a declared condition | none; declared, not drawn |
| `EARTH_MAGNETOPAUSE_SHUE_A1_RADII` | 10.22 | 4 -- Table 1 prints 10.22, uncertainty 0.10 | from the L-305 record |
| `EARTH_MAGNETOPAUSE_SHUE_A2_RADII` | 1.29 | 3 -- 1.29, uncertainty 0.06 | from the record |
| `EARTH_MAGNETOPAUSE_SHUE_A3_PER_NT` | 0.184 | 3 -- 0.184, uncertainty 0.007 | from the record |
| `EARTH_MAGNETOPAUSE_SHUE_A4_NT` | 8.14 | 3 -- 8.14, uncertainty 0.39 | from the record |
| `EARTH_MAGNETOPAUSE_SHUE_A5` | 6.6 | 2 -- 6.6, uncertainty 0.5; token `inverse_exponent` | from the record |
| `EARTH_MAGNETOPAUSE_SHUE_A6` | 0.58 | 2 -- 0.58, uncertainty 0.01; token `flaring_exponent` | from the record |
| `EARTH_MAGNETOPAUSE_SHUE_A7_PER_NT` | -0.007 | 1 -- -0.007, uncertainty 0.0005 | from the record |
| `EARTH_MAGNETOPAUSE_SHUE_A8` | 0.024 | 2 -- 0.024, uncertainty 0.0004; token `log_pressure_coefficient` | from the record |
| `EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG` | 120.0 | exact -- a declared drawing limit | none; declared |
| `EARTH_BOW_SHOCK_JELINEK_R0_RADII` | 15.02 | 4 | from the record, eq. 14, p. 5 |
| `EARTH_BOW_SHOCK_JELINEK_EPS` | 6.55 | 3; token `inverse_exponent` | from the record, eq. 14, p. 5 |
| `EARTH_BOW_SHOCK_JELINEK_LAMBDA` | 1.17 | 3; token `shape_factor` | from the record, sec. 4 |
| `EARTH_BOW_SHOCK_CUT_ANGLE_DEG` | 105.0 | exact -- a declared drawing limit (4.4) | from the record, sec. 2 para. 9 |
| `EARTH_MAGNETOPAUSE_SHUE_SCATTER_RADII` | 1.23 | 3 | from the record, p. 17,697; printed under 2.3 A |
| `EARTH_BOW_SHOCK_JELINEK_SCATTER_RADII` | 0.69 | 2 | from the record, fig. 7; printed under 2.3 A |
| `EARTH_MAGNETOPAUSE_STANDOFF_RADII` | arithmetic (4.3) | 3 -- uncertainty 0.13, root-sum-square of a1 to a5 (2.1) | none; derived |
| `EARTH_BOW_SHOCK_STANDOFF_RADII` | arithmetic (4.3) | 3 -- set by `EARTH_BOW_SHOCK_JELINEK_EPS` (6.55, 3) | none; derived |
| `EARTH_MAGNETOTAIL_OBSERVED_RADII` | 220.0 | 2 -- the zero in 220 is not stated significant | builder opens the NTRS abstract |
| `EARTH_MAGNETOPAUSE_STANDOFF_KM` (new) | arithmetic (4.3a) | 2 -- uncertainty 850, carried from the standoff's primaries | none; derived |
| `EARTH_MAGNETOPAUSE_STANDOFF_AU` (new) | arithmetic (4.3a) | 2 -- uncertainty 0.0000057, carried from the standoff's primaries | none; derived |
| `EARTH_BOW_SHOCK_STANDOFF_KM` (new) | arithmetic (4.3a) | 3 -- set by `EARTH_BOW_SHOCK_JELINEK_EPS` through the standoff | none; derived |
| `EARTH_BOW_SHOCK_STANDOFF_AU` (new) | arithmetic (4.3a) | 3 -- the same | none; derived |

**Where a count depends on what the page prints, the read decides it.**
Rule 2: a trailing zero counts when it falls within the source's
reporting resolution. Meredith's introduction as quoted on the row reads
"from about 1.1 to 2 Earth radii" -- if the page prints "2", the stored
`2.0` carries one figure. The builder records what the page actually
prints, and the row says so in words.

**The read lines from the L-305 record.** Fourteen rows take their read
from `documentation/L305_gap1_read_record_20260911.md`, a model's read
of Tony's PDFs: Shue's eight coefficients, Jelinek's R0, epsilon and
lambda, the bow shock cut angle, and the two scatter rows. Each line names the table, equation
or section the record names, the record's date and "Claude Fable 5.1".
The builder cannot open those papers itself (Wiley's bot detection) and
does not try to re-read them; a read reconstructed from memory would be
worse than none.

**The builder's own reads.** Seven rows, all behind open links already
on their `# Access:` lines: the five belt rows (Baker 2018 at
link.springer.com; Meredith 2014 at nora.nerc.ac.uk; Li, Tu et al. 2024
at par.nsf.gov), the dipole tilt (Alken et al. 2021, Earth Planets
Space, open access) and the magnetotail (NTRS 19830066648). Each goes in
a new read record, `documentation/L322_earth_read_record_C2_<date>.md`,
in the form of the C1 record: what was opened, the title as printed,
where in it, what it says, the verdict. A row the builder cannot open
goes in that file's "For Tony to read" section with the link, where to
look and the number to expect. That section is expected to be empty.
Never a list in chat.

**Lead, not a finding: the dipole tilt.** The row's own note says 9.6 is
"rounded to a tenth of a degree" and records NOAA's 9.41 for WMM2020.
Rounding at rest is the tell of The Store Carries the Verified Figure.
The builder opens Alken et al. (2021) and records what it prints. If it
prints a different figure, or prints no tilt and the value is derived
from its coefficients, that changes a number a hover quotes ("tilted
9.6 degrees"), which Tony sees before it ships.

After the patch: 61 Earth rows (57 and the four new ones), all with a
count; 33 carry a read line (12 before, 21 added: 14 from the record,
including the two scatter rows, and 7 from the builder's reads).

**Three C1 figures lines are brought to the field form.** Three primaries
finished in C1 state their uncertainty in prose, and the checker of 4.7
reads only the field form of 4.0, never prose. So this patch writes, at
the head of each existing line and keeping its words after:

| Row | Figures line gains | Source of the number |
| --- | --- | --- |
| `EARTH_EQUATORIAL_RADIUS_KM` | `uncertainty 0.0001` (km) | IERS, 0.1 m on 6378136.6 m |
| `EARTH_GM_KM3_S2` | `uncertainty 0.0008` (km^3 s^-2) | IERS, 8e5 m^3 s^-2 |
| `EARTH_D660_DEPTH_KM` | `uncertainty 10` (km) | Ishii et al., 660 +/- 10 km |

No count changes. Measured on the dry-run store (4.7): every derived
Earth row stays within its ceiling once these three are read.

### 4.3 The two standoffs go back to arithmetic

```python
EARTH_MAGNETOPAUSE_STANDOFF_RADII = (
    EARTH_MAGNETOPAUSE_SHUE_A1_RADII
    + EARTH_MAGNETOPAUSE_SHUE_A2_RADII * np.tanh(
        EARTH_MAGNETOPAUSE_SHUE_A3_PER_NT
        * (EARTH_SOLAR_WIND_BZ_NT + EARTH_MAGNETOPAUSE_SHUE_A4_NT))
) * EARTH_SOLAR_WIND_PRESSURE_NPA ** (-1.0 / EARTH_MAGNETOPAUSE_SHUE_A5)

EARTH_BOW_SHOCK_STANDOFF_RADII = (
    EARTH_BOW_SHOCK_JELINEK_R0_RADII
    * EARTH_SOLAR_WIND_PRESSURE_NPA ** (-1.0 / EARTH_BOW_SHOCK_JELINEK_EPS))
```

The store already imports numpy as `np`; the reader classifies both as
expressions and the dimensions checker's power rule handles the fitted
pressure exponents (its Shue fixture is this equation). The dry run
wrote each on one line; if the builder wraps them as above, Row shape
must still pass.

**Their figure lines.** The bow shock: "3 -- set by
EARTH_BOW_SHOCK_JELINEK_EPS (6.55, 3). Rule 3's fewest figures, over R0
(4) and epsilon (3); the pressure is declared and skipped. The exponent
-1/6.55 is 0.153 in size, below one, so Rule 3 drops no figure." The
magnetopause: "3 -- uncertainty 0.13, root-sum-square of
EARTH_MAGNETOPAUSE_SHUE_A1_RADII to EARTH_MAGNETOPAUSE_SHUE_A5", then in
words that the five are taken as independent because the paper gives no
correlations, that their plain sum is 0.25 and the tenths place holds
only to 0.158, and that the tenths place is the one whose implied
uncertainty is closest (2.1). A `# Figures:` line on a derived row must
name what set its count, or the checker fails it ("NAMES NO INPUT"); 4.7
makes the uncertainty form an accepted way of doing that.

**Their `# Derived:` lines** keep the arithmetic and state the result at
the declared count, never at seventeen digits: the checker fails a
derived comment that states more figures than the row declares
("COMMENT OVERSTATES").

**They leave `TRANSITIONAL`.** It becomes `()`, and the docstring
paragraph in `constants_rows.py` describing the list says it is empty
since C2 and why, rather than deleting the history.

**Three paragraphs are rewritten, because the rows are no longer typed
numbers** -- not because they were false. Measured at `ba94e80e` by the
L-216 build, the test does read both rows today and reports them NOT YET
MIGRATED, so the comments described a check that was wired and waiting.

- The two row notes, at the lines reading "test_derived_figures.py now
  recomputes this row" and "test_derived_figures.py recomputes this row
  from its inputs". Each note's first paragraph, which says the stored
  value is the reported figure rather than the arithmetic result, is
  replaced WHOLE with a paragraph saying the row is arithmetic again
  since C2, that the export rounds it to its declared count (Rule 6),
  and that the L-325 ruling that made it a literal was withdrawn on
  2026-09-16. The rest of each note (supersessions, Lugaz, Farris &
  Russell, storm compression) is kept word for word.
- The module docstring's "Module updated ... (L-325 ...)" entry is
  history and is not edited. A new entry is appended, dated, saying the
  two rows are arithmetic again, and that the previous entry's sentence
  about `test_derived_figures.py` describes the L-325 version of that
  test, replaced on 2026-09-16.

Anchor each replacement on whole sentences, and read the text after the
anchor first.

### 4.3a The four new rows

Placed directly after each standoff, each with unit, status, figures and
a `# Derived:` line that goes back to the measured primaries (Rule 4):

```python
EARTH_MAGNETOPAUSE_STANDOFF_KM = (
    EARTH_MAGNETOPAUSE_STANDOFF_RADII * EARTH_EQUATORIAL_RADIUS_KM)
EARTH_MAGNETOPAUSE_STANDOFF_AU = EARTH_MAGNETOPAUSE_STANDOFF_KM / KM_PER_AU
EARTH_BOW_SHOCK_STANDOFF_KM = (
    EARTH_BOW_SHOCK_STANDOFF_RADII * EARTH_EQUATORIAL_RADIUS_KM)
EARTH_BOW_SHOCK_STANDOFF_AU = EARTH_BOW_SHOCK_STANDOFF_KM / KM_PER_AU
```

These are expressions over full-precision rows, not over rounded
copies: the store holds no rounded value anywhere in the chain (Rule 6),
so the export computes each from Shue's and Jelinek's published digits
and rounds once. Units `km` and `au`. Status `derived -- inherits` the
rows each uses. The magnetopause pair take their count by the
uncertainty route of 4.7, carried through the standoff. The bow shock
pair declare 3 by counting, set by epsilon; Jelinek states no
uncertainty, but Earth's radius in the same chain does, so their ceiling
is set by propagation, and it is also 3 (measured). A dry run exported
65,000 km at 2 figures and 86,200 km at 3.

### 4.4 The bow shock cut angle becomes a declared drawing limit

Its status today is `measured V_SOURCED`, with a `# Derived:` line
converting Jelinek's +/- 7 hours of local time into 105 degrees. Seven
hours is one figure, so counted as measured the row carries one figure,
the export rounds it to 100, and the drawn shock would stop five
degrees short. Rule 2 names this case: "A DECLARED drawing condition (a
chosen solar wind pressure, a chosen cut angle) is exact for counting."
The magnetopause's 120 degrees is declared for the same reason, on
Tony's ruling of 2026-09-14, and its own note calls the two "the same
shape". No ruling makes the bow shock's measured.

So: `# Status: declared 2026-09-21 -- a drawing limit, not an edge`, with
a `# Declared:` line naming Tony's ruling of 2026-09-21 (2.4);
`# Figures: exact -- a declared drawing limit`; the conversion text
moves from `# Derived:` to `# Declared:` lines, as the magnetopause
row's reason is written; the Source and Access lines stay; and the row
takes a read line from the record, because the seven hours were read.

**Fable, look at this one.** Moving text off a `# Derived:` line removes
the row from the derived-figures list and from the dimensions checker's
NOT CHECKABLE list. That is correct only because no store row enters
the arithmetic -- seven hours is not in the store and 15 degrees an hour
is a definition. The alternative, keeping `# Derived:` with `# Figures:
exact`, also passes (dry run: "OK, exact") and leaves the row listed as
NOT CHECKABLE inside a closed slice indefinitely. This manifest takes
the first; say if you would take the second.

### 4.5 Earth closes

`constants_rows.CLOSED_SLICES = ("EARTH",)`, in the same patch as the
rows, so there is no pushed state with Earth closed and rows unvisited.

### 4.6 The export carries what the read check needs

`export_constants.py` adds two fields to every exported row: `read`, the
row's `# Read:` lines as a list (empty when none), and `inputs`, the
store rows its expression uses, from `constants_rows` (empty for a
typed number). `SCHEMA` goes from 2 to 3. `test_constants_export.py`
adds both to `ROW_FIELDS`, so a stale export fails there.

### 4.7 The figures checker learns the uncertainty route

`test_derived_figures.py` today checks only counting. It gains the
ceiling of 4.0, in a form that can fail and that does not depend on how a
line happens to be phrased:

- **For every derived row it works out the ceiling.** If any measured
  primary in the row's chain states an uncertainty in the field form,
  the ceiling is the count the propagated uncertainty supports under the
  reporting rule of 4.0; otherwise it is the counting ceiling it checks
  today.
- **Propagation.** Trace the row to its primaries; move each up and down
  by its stated uncertainty, or by its implied half-unit where it states
  none; declared and exact inputs contribute nothing; re-evaluate the row
  through its chain from full digits, the way the export evaluates the
  store; take the half-difference; combine by root-sum-square.
- **It FAILS when the declared count exceeds the ceiling.** A row that
  declares its ceiling or fewer passes, and where the counting and
  uncertainty ceilings differ the output prints both.
- **It FAILS when a row declares more than counting allows without the
  uncertainty form on its line**, and when the stated uncertainty,
  rounded to the digits stated, differs from the recomputed one -- which
  is how a one-sided step or a rounded intermediate is caught.
- **It FAILS when a named input is not in the row's chain.**
- **It reads uncertainties only from the field form**, never from prose.
  A primary whose figures line mentions an uncertainty in words but has
  no field is named in the output as unread, so the blind spot
  announces; 4.2 brings the three C1 cases to the field.
- **Output**: per row, the declared count, the counting ceiling, the
  uncertainty ceiling where one was computed, and the verdict, with the
  number of rows examined.
- **Fixtures** gain a row that passes by uncertainty, a C1-shaped row
  that counts within its ceiling and passes, and one for each failure
  above; they run first, as the existing ones do.

**Measured on the dry-run store, with this rule:** all nineteen derived
Earth rows in it pass and none is over-declared. (The two AU rows were
not in that store; each is its km row divided by an exact factor, so it
shares that row's ceiling.) Fifteen of the nineteen are C1 rows whose
chains reach a stated uncertainty: through Earth's radius or GM, and
`EARTH_LOWER_MANTLE_KM` through the 660 km depth alone.
The widest gaps are the Hill sphere (declares 3, ceiling 10; its cap is
the approximate relation, on the row) and LEO's inner edge in Earth
radii (declares 8, ceiling 10); fewer is always allowed. An earlier
draft named Earth's equatorial radius as a primary that states no
uncertainty. It states one.

## 5. Stage C2-b -- the gallery patch

One patch, run from the gallery ROOT after the orrery push, filed in
`documentation/` after it runs. Same guards as 4. Every body other than
Earth must build byte-identical hovers; the fixture proves it.

### 5.1 The renderer, `gallery/feature_renderers.js`

1. **The four unit asserts** move to the new tokens, in the same commit
   as the relabel: `mpS.a6` to `flaring_exponent`, `mpS.a8` to
   `log_pressure_coefficient`, `bsS.epsilon` to `inverse_exponent`, `bsS["lambda"]`
   to `shape_factor`. A mismatch refuses the value and the shape
   disappears, which is the 2026-09-17 failure; that is why they move
   together.
2. **Belt spans.** `beltSpan` also returns each edge's served count. The
   span line prints an edge with a count by Rule F (`fmtServed`) and an
   edge without one exactly as today (`toFixed(1)`).
3. **Both standoff hovers print what the store computed.** The line in
   Earth radii prints the served standoff at its served count -- the
   magnetopause already does; the bow shock stops printing
   `S.toFixed(2)`. The km line prints the served `standoff_km` and the
   served `standoff_au`, each at its own count, the AU to min(3, its
   count) as Rule F already says. `kmAndAu` gains an optional served AU
   so it prints rather than divides. Any word Tony approves for these
   lines, such as "about", is printed ONLY where a served `standoff_km`
   is present, never inside the shared `kmAndAu` path unconditionally,
   so no other body's hover can move. Where no `standoff_km` is served
   (any body without one), the line behaves exactly as today.
4. **Nothing in these two hovers is counted or computed in the page.**
   The bow shock's recount, which left epsilon out, and the
   magnification branch after it, are removed: the store declares the
   count and `test_derived_figures.py` checks it. Say that in the
   comment. The page still computes the bow shock's SHAPE from
   Jelinek's served coefficients, because a curve has to be drawn in the
   browser, and its consistency warning against the served standoff
   stays as it is.
5. **Each standoff hover gains its scatter line** (2.3 A), printing the
   served `scatter` entry at its count or shorter (Rule 7), in the words
   Tony approves. With no scatter served -- any other body -- there is
   no line, and nothing else moves.
6. **The magnetopause is drawn from the served standoff**, as today.
   At 10.3 instead of 10.25 its nose moves 319 km outward, about 0.05
   Earth radii. That is a change to a drawn number and Tony sees it on
   the phone (section 9).

A renderer warning fails the display check, so every new warning is a
real gate.

### 5.2 Six pointer entries (Tony's ruling, 2.2)

In `data/objects_config.json`, inside each of `magnetopause` and
`bow_shock`, directly after `standoff` so the shell's own link still
finds `standoff` first: `standoff_km` and `standoff_au`, each written as
`{"value": null, "unit": "km", "orrery_constant":
"constants_new.py::EARTH_MAGNETOPAUSE_STANDOFF_KM"}` and so on, in place,
with the shared scanner (`tools/mirror_constants.py`'s
`parse_with_spans`). No number and no figure count is written by the
patch. The mirror run of 5.3 fills them. If any still holds `null`
afterwards, the patch puts `data/objects_config.json` back byte for byte
as it found it and says so; refusing after writing would leave empty
entries in a served file. The patch's description records the use of
L-340's exception and that it wrote no number. Two more entries of the
same kind serve the scatter rows (2.3 A), six in all. The pointer join
rises from 78 links to 84.

### 5.3 The relabel, through the mirror

The patch's last step runs the two sanctioned tools itself, because the
relabel needs a flag Tony cannot pass from the Run button:
`tools/pull_constants_export.py`, then `mirror_constants.run(root,
write=True, accept=(...))` naming exactly the four rows. Before that it
checks the pulled export shows Earth closed and the four new tokens,
and if not, refuses and tells Tony to push the orrery first.

### 5.4 The words, through the words tool

Both standoffs' served `source` strings type the standoff and a figure
claim that C2 makes false: "gives 10.25 R_E. Reported to four figures:
..." and "gives 13.51 R_E. Reported to four figures: ...". The patch
removes that sentence from each through `tools/store_writer.py`, keeping
the citation, the equation, the declared conditions, the corroboration
and, for the bow shock, the crossing scatter -- without the typed
0.69, since the hover now prints it from the store (2.3 A). The
hover already prints the standoff, so the prose need not. **The new wording goes to Tony
before the patch is cut** (interactive-exhibit, Hover text is written
for the visitor).

### 5.5 The read check, in `tools/check_constants_links.py --join`

A new section of the pointer join, which already reads the closed-slice
list from the export and already gates the gallery run.

- For every SERVED link whose row is in a closed slice, walk the row and
  its `inputs`, and theirs, through the export.
- Every row reached whose status begins `measured` must have a non-empty
  `read`. Declared and derived rows need none; a derived row is checked
  through its inputs. Inputs outside the slice count -- `KM_PER_AU` and
  `GM_SUN_SI` reach the Hill sphere this way, and both carry reads.
- A row reached that is not in the export FAILS, named, as could not be
  examined. So does an export without the `read` and `inputs` fields.
- So does a row reached whose status begins `derived` and whose
  `inputs` are empty. That is a typed number whose arithmetic lives in a
  `# Derived:` comment, the shape Rule 8 names; a walk by inputs would
  stop there with its measured sources never examined. None is left in
  Earth after C2, and the check does not rely on that.
- It prints links walked, rows reached, measured rows, and rows with a
  read, and names each missing row with the drawn link that reached it.

It treats every served link as drawn, because it cannot see what the
page shows. One linked row is served and shown nowhere today,
`EARTH_MAGNETOTAIL_OBSERVED_RADII`; its source is open, so it is read
rather than excepted.

### 5.6 The display check, `documentation/smoke_display_figures.js`

- `ACCEPTANCE` gains the four hovers, each listing the numbered lines in
  section 6 as literal strings, graded by finding each line verbatim in
  the built hover. A listed hover the run never builds FAILS, as the
  Earth shells already do.
- The fixture is re-recorded, then renamed
  `fixture_hovers_L322c2_on_06fdad8c.json`, and the check's two
  references and its header say it was recorded on gallery `06fdad8c`
  with the C2 patch applied.

## 6. What the four hovers must read afterwards

Worked by the reference script from the store's primaries at full
precision, by Rules S, P and F of L-342 and Rules 3 to 7 of the skill.
The AU figure count is min(3, the count). These strings are the
acceptance test. If the builder's own working gives a different string
for any row, do not pick one: show Tony both and the step where they
part.

| Hover | Line | Today | After |
| --- | --- | --- | --- |
| Magnetopause | radii | Sunward standoff: 10.25 Earth radii | Sunward standoff: 10.3 Earth radii |
| Magnetopause | km | = 65,376 km (0.000437 AU) | = 65,000 km (0.00044 AU), served; wording per 2.3 |
| Magnetopause | conditions | Bz 0.0 nT, dynamic pressure 2.0 nPa | unchanged (declared, exact) |
| Magnetopause | cut | Drawn to 120 deg ... | unchanged (declared, exact) |
| Bow Shock | radii | Sunward standoff: 13.51 Earth radii | Sunward standoff: 13.5 Earth radii |
| Bow Shock | km | = 86,180 km (0.000576 AU) | = 86,200 km (0.000576 AU), served; wording per 2.3 |
| Bow Shock | pressure, cut | 2.0 nPa; Drawn to 105 deg | unchanged (declared, exact) |
| Both standoffs | scatter | none | one new line each (2.3 A), words Tony's |
| Inner Radiation Belt | peak | Drawn at 1.5 Earth radii | unchanged |
| Inner Radiation Belt | km | = 9,567 km (0.0000640 AU) | = 9,600 km (0.000064 AU) |
| Inner Radiation Belt | span | Measured extent: 1.1 to 2.0 Earth radii | Measured extent: 1.1 to 2 Earth radii, if the read finds "2" |
| Outer Radiation Belt | peak | Drawn at 4.5 Earth radii ... (given as L = 4.5: ...) | unchanged (declared, exact) |
| Outer Radiation Belt | km | = 28,702 km (0.000192 AU) | = 28,701.615 km (0.000192 AU) |
| Outer Radiation Belt | span | Measured extent: 3.0 to 7.0 Earth radii | Measured extent: 3 to 7 Earth radii, if the reads find "3" and "7" |
| Both belts | tilt | tilted 9.6 degrees from it | unchanged, unless the tilt lead finds otherwise |

**Without the renderer changes in 5.1, three of these come out wrong**
(section 3): the magnetopause km line prints "= 65,700 km (0.000439
AU)" by multiplying the rounded 10.3, the bow shock prints "13.51" and
"86,180 km", and both spans keep one decimal. **The magnetopause's "10.3
Earth radii = 65,000 km" reads as three figures beside two.** Both are
right: each is the full value rounded once to what its uncertainty
supports in its own unit (2.1).

**The outer belt's "28,701.615 km" is correct by the rules and ugly.**
A declared pick is exact for counting, so the product keeps the planet
radius's eight figures, as LEO's inner edge does. Rule 7 lets a display
show fewer; that is Tony's readability call, with the geocorona and
LEO, after he looks.

## 7. The fixture, and what is allowed to move

Exactly four keys of the fixture's 43 change: `earth/Earth:
Magnetopause`, `earth/Earth: Bow Shock`, `earth/Earth: Inner Radiation
Belt`, `earth/Earth: Outer Radiation Belt`. They move because their
served numbers gain counts at C2. **No Sun, Jupiter or Saturn hover
moves**, and neither do Earth's three frame hovers (axis, Sun direction,
terminator). Section 4 of the L-342 as-built said the SUN's hovers move
at C2; that was wrong, and this is the correction. Before re-recording,
the builder reads every named difference, confirms each is a row of
section 6, and says in the ledger which hovers moved and why.

## 8. Every new or changed check is shown failing

On throwaway copies, before delivery, with the output in the run record:

- **The read check**, with Earth closed: remove the read line from
  `EARTH_DIPOLE_TILT_DEG` (a drawn row) and from `KM_PER_AU` (reached
  only as an input). Each run fails and names the row and the link that
  reached it. Then an export missing the new fields fails.
- **The display check**: restore `toFixed(2)` on the bow shock, and
  separately `toFixed(1)` on one belt edge; each fails by name. Change
  one character of a Sun hover; the fixture fails.
- **The uncertainty route** (4.7): declare four figures on the
  magnetopause with uncertainty 0.13; state 0.14, the one-sided answer;
  state 840 on the km row, the answer from a rounded intermediate;
  write `uncertainty` on `EARTH_BOW_SHOCK_STANDOFF_RADII`, the only bow
  shock row whose chain states none; raise a C1 row one figure above its
  ceiling (`EARTH_LEO_INNER_RADII` to 11); give a C1 row more figures
  than counting allows with no uncertainty form on its line; and delete
  the new field from Earth's radius so its prose is left unread. Each
  fails and names the row.
- **The read check's empty-inputs rule** (5.5): a fixture row that is
  derived, has empty inputs and is reached from a served link fails as
  could not be examined.
- **The rollback** (5.2): force one pointer entry to stay `null`; the
  patch restores the config byte for byte and says so.
- **The three store checkers**, each made to fail once on an Earth row
  and name it: remove one `# Figures:` line (Derived figures and the
  export check), and give a standoff an input with a wrong token
  (Dimensions).
- **The served lines**: set one `standoff_km` back to `null`; the
  gallery patch rolls the config back, as 5.2 says, and the display
  check fails by name. Then serve
  the bow shock standoff one step off its computed shape; the existing
  warning fires and the display check fails.

## 9. Order of delivery

1. **This manifest to Fable** for a second look, with Tony's answers to
   2.2, 2.3 and 2.4 written into section 2.
2. **Stage C2-0**, the skill bump of 4.0, in its own session or at the
   end of the review session. Tony pushes it and reinstalls the skill.
3. **A new build session** confirms it loaded provenance-discipline
   2.16 and the rest of the manifest table, and reads this file.
4. **Stage C2-a.** Tony runs the orrery patch from the orrery ROOT, runs
   the orrery maintenance run, moves the patch to `documentation/`,
   commits, pushes, and reports the SHA. The run rewrites the export and
   the generated files every time; a commit without them shows the run
   was skipped.
5. **Before the gallery patch is cut**, Tony approves the hover words
   (section 13, item 5), and section 6 is updated with the exact
   strings. The display check grades by finding each line verbatim, so
   the strings are fixed first and the builder never writes both the
   hover and the line it is graded against.
6. **Stage C2-b.** Tony runs the gallery patch from the gallery ROOT.
   Then, as one routine: pause OneDrive syncing and note the time; run
   the cache builder by hand; read the last line of
   `data/cache_swap_log.jsonl`; run the gallery maintenance run until
   every gating checker is green, "Cache in step" included; move the
   patch to `documentation/`; commit the config and the cache TOGETHER
   with everything else; push; run the live check; look at Earth's room
   on the phone with section 6 beside him.
7. **The ledger patch** in the orrery, one per pushed HEAD. It carries
   Tony's four rulings of 2026-09-20 and 2026-09-21 in his words: on
   L-322, the magnetopause count by the skill (2.1), the scatter lines
   (2.3) and the cut angle (2.4); on L-340, the pointer-only entry as the
   standing rule, replacing the one-off exception (2.2). It also carries
   the classes of section 11, one row each.

The swap log is new since L-216. This is the first real build on the
hardened swap: a line with more than one attempt and outcome `ok` is a
lock it absorbed; a line with one attempt proves nothing either way.

## 10. Rules of delivery

- A question about how to COUNT figures is never settled inside one
  constant's comment. It goes to Tony or to the skill.
- The maintenance run is run before every commit. A patch's closing
  text never says the run is optional or that nothing will change.
- Anchor a text edit on a whole sentence. Read the next fragment first.
- Any check that reads what a visitor sees builds from the served cache,
  `data/solar-system/coverage_index.json`, not only from the config.
- A long list of numbers does not go in chat. Tony's reading list is a
  file with the link, where to look, and the number to expect.
- A guard compares CONTENT, not raw bytes.
- Nothing in the cache tree is removed with a plain `shutil.rmtree`;
  gallery-cache-builder 1.6 gives the pattern to use.
- A file a patch appends to must end with a line break afterwards.
- A patch runs from its repository's ROOT and is filed in
  `documentation/` after it runs. Say this to Tony each time.
- After every push, read the pushed tree for what the patch should have
  changed. Read both remotes and name which SHA is which.
- Every checker result reported says how many rows it examined and
  names the ones it could not judge.
- Stamp files with your own model name.
- If anything in section 3 has moved when you look, stop and say so.

## 11. Recorded, not built -- one ledger row per class

- **A figure count can describe the arithmetic and not the claim.**
  A model's value beside a larger published scatter; a declared pick
  from a coarse range printed at full arithmetic precision. Instances:
  the two standoffs (answered in C2 by 2.3), the outer belt's
  28,701.615 km, LEO's inner edge, the geocorona. (Fable, Finding 1.)
- **A stated uncertainty computed from a rounded intermediate.** Rule 4
  applies to uncertainties as it does to values. (Finding 2.)
- **Unit-conversion rows multiply by shell.** C2 adds a km and an AU
  row per standoff. Every other shell that prints km and AU from a
  rounded value needs the same, so decide ONCE, before the next slice,
  whether the answer is rows per shell or the export converting each
  row itself from full digits. Not decided here. (Finding 9.)
- **A derived row with empty inputs is invisible to a walk by inputs.**
  (Finding 7.)
- **The page converts a served km value to AU in several shell
  hovers.** Where the km is itself a rounded derived value, that is a
  rounded number used in a calculation. Measured today it moves no
  digit (the Hill sphere gives 0.0100 AU both ways), which is luck, not
  a guarantee. C2 fixes its own two hovers by serving the AU; the class
  is recorded for L-342.
- **The page re-derives the bow shock standoff to draw its shape**,
  a second working of Jelinek's equation 14 beside the store's. Its
  consistency warning guards it. Recorded, not changed here.
- **Other rows may be over-precise the same way.** Any derived row
  outside Earth whose inputs state uncertainties was counted, not
  propagated. Recorded as a class for the slices that reach them; not
  chased here.
- **The outer belt's hover says "where the measured particle flux
  peaks"** while its store row is a declared midpoint, "not a measured
  peak". Words are Tony's; recorded for him.
- **The magnetotail's observed extent is served and shown nowhere.**
- **Corrections to the L-342 as-built**, for the record: the Sun's
  hovers do not move at C2; and "the renderer already drops a figure"
  for the bow shock does not fire, because the drop is conditioned on
  an exponent above one and this one is 0.153, and its count left
  epsilon out.
- **Owed to interactive-exhibit's next bump**, unchanged from the brief:
  a hover prints a served primary where the store has one and computes
  with figure propagation where it does not; now also, a count is READ
  from the served entry, never recounted in the browser.
- **Owed to the next protocol bump touching Stale Skill = Stop**,
  unchanged: a running session's mounted skills stay at the version it
  started with, while the project instructions in its context refresh.

## 12. Out of scope

- Stage D, Earth's pole moving into the store. It follows C2.
- The Sun's slice and every other body's; their hovers must not move.
- L-340's Arrival-check list; L-337's centring marker.
- Retiring the old drift check, the suffix reader and `SCALAR_UNITS`.
  After C2 the drift check examines 24 links (28 fallbacks less Earth's
  four); the Sun's are still there.
- Any new measured or declared constant. Four derived reporting rows
  are added under Tony's instruction of 2026-09-20 (2.2).
- Moving the repositories off OneDrive. Tony's, undecided, not pressed.

## 13. Tony's decisions, and when they fall due

1. **(settled, 2026-09-20)** The magnetopause count: the skill gives
   three figures (2.1).
2. **(settled, 2026-09-21)** How the hovers tell the visitor about the
   scatter: A, one line each (2.3).
3. **(settled, 2026-09-21)** The bow shock's cut angle becomes declared
   (2.4).
4. **(settled, 2026-09-21)** The gallery patch may add pointer-only
   entries, and L-340 records that as the standing rule (2.2).
5. **(approve, before the gallery patch is cut)** The reworded source
   strings for the two standoffs (5.4), and the hover words of 2.3;
   section 6 is then updated with the exact strings (section 9, step 5).
6. **(read, only if the file lists any)** The "For Tony to read"
   section of the C2 read record. Expected empty.
7. **(look, after the gallery push)** Earth's room on the phone.
8. **(decide, end of C2)** L-325: close it as superseded, since the rows
   it made literals are arithmetic again and its ruling was withdrawn
   on 2026-09-16. Recommendation: close.
9. **(decide, after looking)** Whether any rule-correct number is shown
   shorter: the geocorona at 600,000 km twice, LEO's inner edge at
   6,578.1366 km, and now the outer belt at 28,701.615 km.

## 14. Done when

With `CLOSED_SLICES = ("EARTH",)`: the orrery maintenance run passes;
the three constants checkers judge every Earth row and list none as not
yet migrated or not checkable; each has been made to fail once on
purpose on an Earth row and named it. The gallery run passes with
"Cache in step", "Display figures" and the pointer join green; the join
counts 84 links and prints 24 fallbacks, down from 28, with none
Earth's; its read
section examines every measured row reached from a served Earth link.
The fixture diff names exactly the four hovers of section 7. Tony has
looked at the room on his phone.

## 15. Tony-action rollup

1. **(done, 2026-09-21)** The questions in 2.2, 2.3 and 2.4, answered and written into section 2.
2. **(do)** File this manifest in the orrery's `documentation/`, commit,
   push. Carry it to a Fable session for review, with both SHAs, saying
   which is which.
3. **(do)** After Stage C2-0: push the skill and the protocol entry,
   reinstall provenance-discipline 2.16, and start a new session for
   the build.
4. **(do)** At each stage: run the patch from the ROOT of the repository
   it names, run that repository's maintenance run, move the patch to
   `documentation/`, commit, push, report the SHA.
5. **(do)** Before the cache build: pause OneDrive syncing and note the
   time; afterwards, read the last line of `data/cache_swap_log.jsonl`.


## 16. Fable's review of 2026-09-21, and what changed

Each finding was checked here before it was taken up; where Fable's own
figure needed a correction, it says so.

1. **The +/- 0.13 is the fit's precision, not the magnetopause's.**
   Accepted. 2.1 now says which it is; 4.0 says which uncertainty the
   route propagates and that a model's scatter is shown, not
   propagated; the choice of how the visitor is told went to Tony, who
   chose A on 2026-09-21 (2.3).
2. **Two uncertainties computed from a rounded intermediate.** Accepted
   and re-measured: 845.9 km and 0.00000565 AU from full digits, written
   850 and 0.0000057 (2.1, 4.2).
3. **The step direction changes the answer.** Accepted and re-measured:
   up 0.129, down 0.136, central 0.1326. The central difference is named
   in 4.0 and 4.7, and section 8 tests the one-sided answer failing.
4. **State the independence bound.** Accepted. One correction to the
   review: the plain sum is 0.2481, so 0.25, not 0.24; and the kilometre
   line is not safe across the whole range but sits on its boundary at
   the ceiling (holds to 0.2479). Neither changes the reported figures.
5. **The log scale is ours; say when the route fires.** Accepted. 4.0
   separates the page's words from the project's addition, with the
   reason, and states when the route fires; re-measured that the bow
   shock would be 13.51 under implied uncertainties and is 13.5 by
   counting.
6. **The implied half-unit errs large.** Accepted; 4.0 says so.
7. **The read check can miss a derived row with empty inputs.**
   Accepted; 5.5 fails it, section 8 tests it.
8. **The cut angle, with Tony's yes.** Taken to Tony, who confirmed it
   on 2026-09-21 (2.4).
9. **Section 12 contradicted the four new rows.** Accepted; section 12
   reworded; the rows-per-shell question recorded once in section 11,
   not decided here.
10. **"=" between two differently rounded lines.** Taken to Tony with
    the hover words (2.3).
11. **Leave the drawn 10.3 and the AU class for C2.** Agreed; no change.
12. **Smaller points.** The rollback in 5.2 is now specified; the token
    for a8 is `log_pressure_coefficient`; 2.16 waits on 2.3; the rest
    needed no change.

**Fable's second look, 2026-09-21.** Fable confirmed the twelve were
taken up and re-measured the two corrections to its own figures. New
findings:

- **A. The fail rule would have failed fourteen finished C1 rows, or
  missed them only because their uncertainties are in prose** (blocked
  the build). Accepted and measured. The count is fifteen, not
  fourteen: Fable's list missed `EARTH_LOWER_MANTLE_KM`, which reaches
  the 660 km depth alone. Those fifteen, and C2's own bow shock km row,
  chain through Earth's radius, GM or the 660 km depth, which state
  uncertainties. The rule is replaced by Fable's option 1,
  which is method: the ceiling is set by propagation where any primary
  states an uncertainty, and a row fails only by declaring MORE than its
  ceiling. Run over the nineteen derived Earth rows of the dry-run
  store, none fails. The three C1 lines move to the field form (4.2),
  the checker reads only that form and names unread prose (4.7), the
  wrong example is gone, and section 8 tests a C1 row and names
  `EARTH_BOW_SHOCK_STANDOFF_RADII`.
- **B. Two answers for an approximate relation.** Accepted; 4.0 gains
  the show-or-cap sentence.
- **C. "about" must not leak into other bodies' hovers.** Accepted; 5.1
  prints it only where a served `standoff_km` is present.
- **D. Section 6 lines not yet strings.** Accepted; section 9 step 5 and
  section 13 item 5 fix the strings before the gallery patch is cut.
- **E. Leftovers.** The additions to Rule 3 are named and counted; the
  5.2 heading records the ruling; section 8 says "rolls back"; the
  closing stamp carries both dates.

---

Written September 20, 2026, and revised September 21, 2026, with
Anthropic's Claude Opus 5.
