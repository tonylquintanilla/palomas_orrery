# Design -- L-345 decided: a value in another unit is computed, never stored

**Built on orrery `714293a901159be25074a95662526e4703cc92fc` at
https://github.com/tonylquintanilla/palomas_orrery and gallery
`2df02f3baead894ff40922bcadef9cb84c49fa07` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.** Both
HEADs read live with `git ls-remote` on 2026-09-28. Every measurement
below was taken on clones of those two commits.

**Type: DESIGN, for a BUILD in this session.** Nothing here has been
built. It finishes L-322 Stage D along the way.

**Rules this runs under:** protocol v3.71; provenance-discipline 2.21
(this session's loaded copy reads 2.21, which discharged v3.71's
obligation); interactive-exhibit 1.4; ledger-and-session-records 1.11;
safe-file-editing 1.11; agentic-pre-test 1.2.

Written for Tony, a retired professional engineer who is not a
programmer, and for the sessions that build it.

---

## 1. Tony's ruling, 2026-09-28

L-345 asked where a number's value in a second unit comes from: a row
per unit in `constants_new.py`, or the export working it out. Tony:

> follow the single source of truth principle. use the single best
> source for the store with provenance. compute all conversions
> instead of duplicating. we should build this architecture now. add
> to the skill if clarification is needed.

So: each quantity is ONE row, in the unit its best source gives it,
carrying that source. Its value in any other unit is computed from that
row, never stored as a second row.

## 2. What was found

**The store already holds 13 rows that are the same quantity as another
row, in a different unit.** Each is its source row multiplied or divided
by an exact defining number (the kilometres in an AU, one Earth radius,
one solar radius), and each carries its own figure count and status
line, a second declaration of a precision the first row already states.

| Row that is a conversion | Is the same quantity as |
|---|---|
| EARTH_INNER_CORE_RADII | EARTH_INNER_CORE_KM |
| EARTH_OUTER_CORE_RADII | EARTH_OUTER_CORE_KM |
| EARTH_LOWER_MANTLE_RADII | EARTH_LOWER_MANTLE_KM |
| EARTH_UPPER_MANTLE_RADII | EARTH_UPPER_MANTLE_KM |
| EARTH_GEOSTATIONARY_RADII | EARTH_GEOSTATIONARY_RADIUS_KM |
| EARTH_LEO_INNER_RADII | EARTH_LEO_INNER_KM |
| EARTH_LEO_OUTER_RADII | EARTH_LEO_OUTER_KM |
| EARTH_HILL_SPHERE_RADII | EARTH_HILL_SPHERE_KM |
| EARTH_MAGNETOPAUSE_STANDOFF_KM | EARTH_MAGNETOPAUSE_STANDOFF_RADII |
| EARTH_MAGNETOPAUSE_STANDOFF_AU | EARTH_MAGNETOPAUSE_STANDOFF_RADII |
| EARTH_BOW_SHOCK_STANDOFF_KM | EARTH_BOW_SHOCK_STANDOFF_RADII |
| EARTH_BOW_SHOCK_STANDOFF_AU | EARTH_BOW_SHOCK_STANDOFF_RADII |
| CHROMOSPHERE_PHYSICAL_RADII | CHROMOSPHERE_TOP_KM |

Two more are a sum written directly in a second unit:
`EARTH_STRATOPAUSE_RADII` and `EARTH_THERMOPAUSE_RADII` are each Earth's
radius plus an altitude, divided by Earth's radius. Their inputs are in
kilometres, so the sum belongs in kilometres, as `EARTH_LEO_INNER_KM`
and `CHROMOSPHERE_TOP_KM` already are.

**The page converts rounded numbers to print them.** The gallery's
`kmAndAu()` divides whatever kilometre figure it is handed by the
kilometres in an AU. When that figure was already rounded by the export,
the AU is worked from a rounded intermediate. For the chromosphere it
moves a digit: 0.00467 AU from the rounded 698,000 km, where the full
number gives 0.00466. That is the case that raised the question.

**The Sun's own conversion rows are not exported yet.** `SOLAR_RADIUS_AU`
(the solar radius in AU), `CORE_AU`, `RADIATIVE_ZONE_AU` and their
neighbours are the same kind of thing. They wait for the Sun's slice
(section 7).

## 3. The architecture, in four parts

**The store (`constants_new.py`).** One row per quantity, in the unit
its best source states, with the source, the status line and the
figure count. A sum or difference that makes a new quantity (a shell's
radius from a planet's radius plus an altitude) is a row, in the unit of
its inputs. A value in another unit is not a row.

What happens to the 13 names: they stop being rows. Each loses its
`# Figures:`, status and source lines and is marked as a conversion of
the row it comes from. The orrery's drawing code can keep using the
name, because a name that is computed from the one row holds no second
value and states no second precision. The export does not serve it, and
no pointer in the gallery may name it. (The alternative, replacing
every use with a function call, touches about ten orrery modules for no
change in what is true. Recorded in section 8 as a choice the build can
revisit.)

**The export (`export_constants.py`, `constants_rows.py`).** For every
row whose unit is a length -- kilometres, AU, Earth radii, solar radii,
all four already declared in the export's unit table with their
defining numbers -- the export serves the row's value in each of the
four units, worked out from the full digits and rounded once. Schema 6.
Each served row gains a field such as:

    "in": {"km":      {"value": 698000.0, "figures": 3},
           "au":      {"value": 0.00466,  "figures": 3},
           "r_sun":   {"value": 1.003,    "figures": 4},
           "r_earth": {"value": 109.4,    "figures": 4}}

A value in Earth radii for a solar shell is never printed and costs a
few bytes; serving every length unit for every length row avoids
deciding which body a row belongs to, which the store does not record.

**The mirror (`tools/mirror_constants.py`).** Copies `"in"` onto the
served node, as it copies `"prints"` and `"uncertainty"`. Pointers in
`data/objects_config.json` move from the 13 conversion names to the
rows they come from. Neither the mirror nor `store_writer` writes
pointers, so the move is one patch's edit, as every pointer was first
written.

**The page (`gallery/feature_renderers.js`).** A hover prints a number
in a unit by reading that unit from the node's `"in"`. It never
multiplies or divides a served, rounded number to print it. It still
converts freely to DRAW, where a rounded number moves nothing a visitor
can see. A printed number whose node has no `"in"` (an unvisited slice)
prints exactly as it does today, so nothing outside the closed slices
moves.

## 4. How a computed conversion gets its figure count -- no rule changes

A conversion is a value scaled by an exact row, which provenance-
discipline Rules 3 and 4 already cover: counting by fewest figures,
propagating a stated uncertainty, and 2.21's place rule for a sum.
`test_derived_figures.py` already works out, for each derived row, the
largest count each method allows. **The export gives a conversion the
smaller of the two** -- the most figures the rules permit and no more.

Measured against the 13 rows' declared counts, that reproduces every
one:

| Row | Declared | Counting allows | Propagation allows | Computed |
|---|---|---|---|---|
| EARTH_INNER_CORE_RADII | 5 | 5 | 5 | 5 |
| EARTH_OUTER_CORE_RADII | 5 | 5 | 5 | 5 |
| EARTH_LOWER_MANTLE_RADII | 3 | 3 | 3 | 3 |
| EARTH_UPPER_MANTLE_RADII | 5 | 5 | 5 | 5 |
| EARTH_GEOSTATIONARY_RADII | 7 | 7 | 7 | 7 |
| EARTH_LEO_INNER_RADII | 8 | 8 | 10 | 8 |
| EARTH_LEO_OUTER_RADII | 8 | 8 | 9 | 8 |
| EARTH_HILL_SPHERE_RADII | 3 | 3 | 8 | 3 |
| EARTH_MAGNETOPAUSE_STANDOFF_KM | 2 | 3 | 2 | 2 |
| EARTH_MAGNETOPAUSE_STANDOFF_AU | 2 | 2 | 2 | 2 |
| EARTH_BOW_SHOCK_STANDOFF_KM | 3 | 3 | 3 | 3 |
| EARTH_BOW_SHOCK_STANDOFF_AU | 3 | 3 | 3 | 3 |
| CHROMOSPHERE_PHYSICAL_RADII | 4 | place rule, 4 | -- | 4 |

So the build changes WHERE the count comes from, not what any number
prints. The build proves this by the recorded hovers: every hover not
listed in section 5 must match its recording byte for byte.

**One asymmetry the table shows.** The magnetopause standoff is served
as 10.3 Earth radii (3 figures) beside 65,000 km (2 figures). The
kilometre count follows the paper's stated uncertainty, 850 km; the
radii count was declared by counting. Computed, the radii figure would
also take 2 figures and print 10. That is the one place where computing
disagrees with a declared number, and it is on the SOURCE row, not a
conversion, so the build does not touch it. Recorded in section 7.

**The skill clarification Tony allowed.** provenance-discipline gains a
short section, "A Value in Another Unit Is Computed, Never Stored":
section 1's ruling, the store rule of section 3, and the count rule
above. interactive-exhibit gains one rule: a hover prints a unit from
the served `"in"`, never by arithmetic on a served number. That second
one replaces the line L-351 holds for its next bump.

## 5. What a visitor will see change

Everything patch 4 was built to change in the Earth room, and two Sun
hovers:

| Room | Hover | Today | After |
|---|---|---|---|
| Earth | Magnetopause | Bz 0.0 nT, dynamic pressure 2.0 nPa | Bz 0 nT, dynamic pressure 2 nPa |
| Earth | Bow shock | at dynamic pressure 2.0 nPa | at dynamic pressure 2 nPa |
| Earth | Crust | Radius: 1.0000 Earth radii | Radius: 1 Earth radius |
| Sun | Chromosphere | Radius: 1.002874802357338 solar radii / = 697,700 km (0.00466 AU) | Radius: 1.003 solar radii / = 698,000 km (0.00466 AU) |
| Sun | Photosphere | Radius: 1 solar radii | Radius: 1 solar radius |

Nothing else. The build records a new fixture and lists every changed
hover before Tony's phone check.

## 6. The build, in order

1. **Orrery patch D19: the mechanism.** `constants_rows.py` computes a
   row's value and count in each length unit. `export_constants.py`
   serves `"in"`, schema 6. `test_constants_export.py` checks every
   conversion against its source row's full digits. provenance-
   discipline 2.22, interactive-exhibit 1.5, protocol v3.72, one commit.
   The ledger records L-345 as decided.
2. **Orrery patch D20: the rows.** The 13 conversion names stop being
   rows. The stratopause and thermopause become kilometre sums, with
   their radii names kept as conversions. A new check fails on any row
   that is a pure conversion of another row, so the store cannot grow
   one again unnoticed, and it is shown failing before it is trusted.
   The orrery's hovers that print these names are checked byte for
   byte, with the pre-delivery test (agentic-pre-test), because they
   are display code.
3. **One gallery patch.** Patch 4's work unchanged; the mirror copies
   `"in"`; pointers move from the 13 names to their rows; the page
   prints units from `"in"`; the Sun's "Radius:" line prints by the
   served count, singular at exactly 1; a new fixture.
4. **Tony's runs:** cache build, gallery maintenance run, push, phone
   check, then the orrery maintenance run, where "Exact rows by the
   count" should pass.

Each patch is tested on a throwaway copy with its repository's checks
before it reaches Tony.

## 7. Recorded, not built -- for the ledger, one row per class

- **The Sun's conversion rows**, not exported yet: `SOLAR_RADIUS_AU`,
  `CORE_AU`, `RADIATIVE_ZONE_AU`, the Oort cloud and termination shock
  rows in AU, and their neighbours. Each is re-homed to its source's
  unit when the Sun's slice walks it.
- **Conversion rows outside the exported slices** on other bodies, the
  same class.
- **The magnetopause standoff's radii count** (3) disagrees with the
  count its own stated uncertainty gives (2). A finding on the source
  row, for Tony's eye, since fixing it changes "10.3" to "10".

## 8. Choices the build may revisit, with the reason for each

- **Keeping the 13 names as computed conversions** rather than replacing
  their uses. Chosen because it is true (one value, one precision) and
  touches the fewest files. If a later reading of the principle wants
  the names gone, the new check makes every use easy to find.
- **All four length units on every length row.** Chosen because the
  store does not say which body a row belongs to. If `"in"` proves
  bulky in the served cache, it narrows to km, AU and the body's own
  radius.

---

Written September 28, 2026 with Anthropic's Claude Opus 5.5.
