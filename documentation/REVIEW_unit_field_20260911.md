# Review request -- where does a constant's UNIT live?

Built on orrery `2432db648f317387527a920aa0f3d40c2ed2f3df`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `9c056d1a27554a3b0afd27530ab9995c9929ff96`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Tony Quintanilla, PE | request written by Claude Opus 5 | 2026-09-11
Type: DESIGN REVIEW REQUEST (Mode 7, cooperative). Zero code wanted back.
Origin: L-305 Gap item 3.

## Before you start -- the rules this task runs under

You are being asked to review work governed by a written protocol and a
skills layer that you do not have resident. Fetch these at the orrery
SHA above, and read them before answering:

- `PROJECT_INSTRUCTIONS.md` -- in particular Fetched vs Recalled
  Convention, The Artifact Bounds the Audit, The Braid, A Check That
  Cannot Fail Is Not Passing, and Check All Parallel Pipelines.
- `skills/provenance-discipline/SKILL.md`
- `skills/interactive-exhibit/SKILL.md` -- it owns the served-data
  provenance contract (value / unit / source / orrery_constant) and the
  live store-drift run.

**State in your reply which of those files you actually read.** A reply
that does not name them is telling us it did not read them.

The code you will be reading is polished, and that says nothing about
the author's fluency. Tony is a retired civil and environmental
engineer, not a professional programmer; the codebase is the product of
two years of AI collaboration under the protocol above. Write for him.
He holds sole commit authority and every judgment call. Unpack jargon on
first use.

## What to read in the code

- orrery `constants_new.py` -- the single value home. 1,466 lines,
  86 top-level numeric constants, each with provenance in structured
  comments above it.
- orrery `provenance_scanner.py` -- specifically `NUMERIC_CLAIM_RE`
  around line 1027 and the comment block above it.
- gallery `gallery_maintenance_run.py` -- `unit_of_constant`,
  `store_conversions`, `judge`, `check_store_drift` (lines 423-713).
- gallery `data/objects_config.json` -- the served config whose entries
  carry `orrery_constant` pointers.

## The situation, measured today rather than recalled

The gallery's store-drift check follows pointers in
`data/objects_config.json` back into the orrery's `constants_new.py` and
asks whether the served copy still says what the store says.

To compare two numbers it needs each side's unit. The config states its
unit outright. The orrery does not: the check infers the unit from a
SUFFIX ON THE CONSTANT'S NAME, and knows four -- `_RADII` (solar radii),
`_AU`, `_KM`, plus a special case where an `EARTH_`-prefixed `_RADII` is
Earth radii. Conversion factors are deliberately NOT typed into the
gallery; they are derived from store constants (`KM_PER_AU`,
`SOLAR_RADIUS_AU`, `EARTH_EQUATORIAL_RADIUS_KM`), because a number typed
into the checker would be a shadow constant, which is the failure the
check exists to find.

Measured at the two SHAs above:

- 53 pointers in the served config: 48 MATCH, 0 DRIFT, 0 NO UNIT, and
  5 NOT IN STORE. The five are values that are not top-level constants
  (`planet_poles['Sun']`, `['Earth']`, `['Jupiter']`, `['Saturn']`, and
  a function default in `create_sun_galactic_tide`).
- 38 distinct constants are reachable from those pointers; 33 are
  top-level in the store.
- All 33 are LENGTHS: 8 in AU, 7 in km, 11 in Earth radii, 7 in solar
  radii. The store has no served non-length constant today.
- `constants_new.py` uses a comment-key grammar with continuations
  (`# Source:` / `# Source+:`). Fourteen keys are in use: Note, Source,
  Derived, Ref, Also, See, Corrected, Resolved, Declared, Status,
  Calculation, Access, Sources, Record. There is NO `Unit:` key.
- `provenance_scanner.py` ALREADY carries a unit vocabulary, inside
  `NUMERIC_CLAIM_RE`, for detecting numeric claims in display strings.
  It covers AU, km, km/s, R_sun, deg, temperatures, masses and more, and
  it has a recorded history of being widened (L-195, with measured
  before-and-after counts).

## What is about to change, and why it forced the question

Ledger item L-305 rebuilds Earth's magnetosphere on two published
models -- Shue et al. (1998) for the magnetopause, Jelinek et al. (2012)
for the bow shock -- and will add 15 new served pointers: Shue's eight
coefficients, Jelinek's R0 / eps / lambda, a bow-shock cut angle in
degrees, and three declared solar wind conditions (2 nPa, 0 nT,
400 km/s).

Only 3 of those 15 are lengths. The other 12 are per-nanotesla,
nanotesla, nanopascal, degrees, km/s, and five dimensionless numbers.
Run against the real check, those 15 pointers return **3 MATCH and
12 NO UNIT**. A NO UNIT pointer is printed and counted as unexaminable,
but only DRIFT makes the check report FAIL -- so the run would go green
with twelve of L-305's fifteen new values unchecked, and L-305's own
closing requirement, "MATCH by name for every new pointer", would not be
reachable.

A first patch was written that simply extended the gallery's suffix
table with `_PER_NT`, `_NT`, `_NPA`, `_DEG`, `_KM_S` and
`_DIMENSIONLESS`. It works -- 15 of 15 MATCH -- and it has been HELD
UNRUN, because it puts a naming vocabulary for ORRERY constants inside
the GALLERY repo, which is the shadow-constant failure one level up.

## Tony's reading, which is what we want you to test

In his words: the issue resides and is resolved in the orrery, and is
transported to the gallery as-is. One source of truth. He wants a unit
FIELD in the store -- a `# Unit:` line beside the value -- for three
reasons he named: correct dimensional analysis, provenance, and
consistent worksheet completion.

He also ruled the migration bounded by The Braid: not all 86 constants,
but the ones the two live interactive exhibits (Sun and Earth) actually
render.

He does not read the code. He reasoned to this from the architecture.

## The questions

1. **Is his reading right?** Does a unit belong in the store as a
   declared field, with the gallery consuming it and holding no
   vocabulary of its own? If you think the suffix convention is
   defensible and the declared field is over-engineering, say so.

2. **Where does the unit vocabulary live so it exists once?** The
   scanner already has one in `NUMERIC_CLAIM_RE`. Is that the same
   vocabulary as a constant's declared unit, or two different jobs that
   would be wrong to merge -- detecting a claim in prose versus
   declaring a value's dimension?

3. **Who enforces a missing `Unit:` line?** The gallery check sees only
   served constants and reports without gating. The scanner is the
   stronger enforcer and has the tiering machinery, but it lives in the
   orrery and cannot read the gallery's `objects_config.json`, so it has
   no way to know which 33 constants are in the bound. Requiring `Unit:`
   on all 86 grows the denominator by 53 and is the failure The Artifact
   Bounds the Audit names. A proxy was proposed -- "any constant
   carrying a `Source:` line" -- but there are 131 `Source:` lines
   against 86 top-level constants, so that proxy is wider than the bound
   and has not been counted properly.

4. **Is "reachable from a served pointer" the right bound?** A
   `SUN_`/`EARTH_` prefix cut was considered and rejected, because the
   Sun's own constants carry no prefix (`CORE_AU`,
   `HELIOPAUSE_RADII`, `ALFVEN_SURFACE_RADII`,
   `CHROMOSPHERE_PHYSICAL_RADII`). If you see a better selector, name
   it.

5. **Is a unit name enough for dimensional analysis, or must the store
   declare a DIMENSION too?** Lengths convert among themselves via
   factors already derived from the store. Everything else would compare
   exactly against itself and never convert. Does that hold up, or does
   it break the first time two units share a dimension outside length --
   say nPa against Pa, or degrees against radians?

6. **What does this do to worksheets?** A worksheet currently verifies a
   value and its citation. Tony wants unit declaration to make worksheet
   completion consistent. Does a unit column belong in the worksheet
   schema, and does that change what a checker is asked to verify?

## What we do NOT want back

- No patches, no diffs, no code. This is a design round; the build
  happens afterwards under the protocol's own rules.
- Do not propose ledger handles or write ledger blocks. Handles are
  issued in the orrery repo and a proposed one is usually already taken.
- Do not re-derive the measurements above. If you think one is wrong,
  say which and how you would check it.

Prose is fine, and disagreement is the point of asking. Where you think
the framing in this document is itself wrong, say that first.

Written September 2026 with Anthropic's Claude Opus 5.
