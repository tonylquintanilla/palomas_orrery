# Review reply -- where does a constant's UNIT live?

Built on orrery `2432db648f317387527a920aa0f3d40c2ed2f3df`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `9c056d1a27554a3b0afd27530ab9995c9929ff96`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Reply written by Claude (Fable 5.1), inside the Paloma's Orrery Project, 2026-09-11.
Answers the review request of the same date (origin L-305 Gap item 3).
Design round only. No code, no handles.

## What I read

- `PROJECT_INSTRUCTIONS.md` v3.57 -- resident in this Project, not fetched.
  The sections the request names were read: Fetched vs Recalled, The
  Artifact Bounds the Audit, The Braid, A Check That Cannot Fail Is Not
  Passing, Check All Parallel Pipelines, and A Report Names Its Items.
- `skills/provenance-discipline/SKILL.md` -- installed copy, version 2.11,
  which matches the manifest. Read: Worksheet Types and the schema, The
  Exhibit Requirement, Geometry Constants Are First-Class Claims, and
  the dict-level status-line rule.
- `skills/interactive-exhibit/SKILL.md` -- installed copy, version 1.2,
  which matches the manifest. Read: Provenance is part of the build and
  step 5 (store drift reads MATCH).
- Fetched at the SHAs above and read: orrery `constants_new.py` (all
  1,466 lines skimmed, the Earth exhibit block read closely),
  `provenance_scanner.py` lines 1002-1060 and the comment-binding notes
  in its header, gallery `gallery_maintenance_run.py` lines 423-713, and
  gallery `data/objects_config.json` (parsed with the maintenance
  script's own `collect_pointers` / `config_value`).

## Three places the request's framing is off

I say these first because two of them change the answers below.

1. **The 12 NO UNIT going green is a bug on its own, whatever the unit
   design ends up being.** `check_store_drift` returns FAIL only on
   DRIFT. NO UNIT, NO VALUE and NOT IN STORE are printed and summed as
   "could not be examined" and the run stays PASS. That is exactly the
   shape A Check That Cannot Fail Is Not Passing describes: an
   unexamined pointer reports the same colour as a checked one. Fixing
   the verdict is independent of, and prior to, deciding where the
   unit vocabulary lives.

2. **"The store has no served non-length constant today" is true of
   the store and false of the served config.** Four of the 53 pointers
   already carry a non-length unit or no unit at all, and all four
   point outside `constants_new.py`: the two Jupiter and Saturn pole
   pointers carry `deg`, the two Sun and Earth orientation pointers
   carry an empty unit string, and all four resolve to
   `idealized_orbits.py::planet_poles[...]`. Degrees are not arriving
   with L-305; they are being served now, unchecked, and have been
   since the Earth exhibit. That is an existing class, not a new one.

3. **"Transported to the gallery as-is" is not what the pipeline does
   today.** The served config states its own unit and it is often not
   the store's: `CORE_AU` is served in `R_sun`; eleven `_KM` constants
   are served in `r_earth`. The check converts across units on 27 of
   the 48 matches. So the gallery legitimately needs a conversion
   table; what it must not need is a naming vocabulary. Those are two
   different things and the request treats them as one. (Two smaller
   corrections: the annotation block sits BELOW the assignment, not
   above; and "131 `Source:` lines" counts 59 `# Source:` heads plus 72
   `# Source+:` continuations. 49 of the 59 heads sit directly under an
   assignment.)

## Q1 -- Is Tony's reading right?

Yes, with one edge he has not named. A unit belongs in the store as a
declared field beside the value, and the gallery should read it rather
than decode a name. The suffix convention is not wrong as naming --
`_KM`, `_AU`, `_RADII` are readable and should stay -- it is wrong as
the ONLY declaration, decoded by a table that lives in the consumer.
The store itself already proves suffix-decoding does not scale: it
holds `EARTH_GM_KM3_S2`, `EARTH_ROTATION_RATE_RAD_S`,
`SPEED_OF_LIGHT_KM_S`, `SGR_A_DISTANCE_PC`, `SGR_A_MASS_SOLAR`,
`GRAVITATIONAL_CONSTANT_SI`. A compound unit or an abbreviation like
`_SI` cannot be recovered from the name without a growing table, and
the L-305 patch that was held is that table growing.

The edge: once a `# Unit:` line exists and the name still carries a
suffix, the constant declares its unit twice, and two declarations are
a drift class. The rule that closes it is cheap: the `Unit:` line is
the declaration; a suffix, where present, is checked for agreement
with it by the scanner, and a disagreement is a finding. That turns
the suffix from a second source of truth into a check on the first.

Is the declared field over-engineering? No. The file already runs a
fourteen-key comment grammar with a parser that reads it. A fifteenth
key is the smallest possible change to the store's own convention, and
far smaller than the alternative of restructuring 88 assignments into
objects.

## Q2 -- Where does the vocabulary live so it exists once?

The scanner's `NUMERIC_CLAIM_RE` and a constant's `Unit:` line are
two different jobs and would be wrong to merge as they stand. The
regex is a DETECTOR for prose: it needs synonyms ("km", "kilometers",
"kilometres", "solar radii", "R_sun", "[Any]+ radii") because prose
spells a unit many ways, and a broad match there costs only a false
positive. A DECLARATION needs the opposite: exactly one canonical
spelling per unit, so that the gallery's `r_sun` and the store's
`R_sun` and a worksheet's "solar radii" are recognisably the same key.

What should exist once is not the regex but a canonical unit TABLE in
the orrery: one row per unit, with its canonical key and its accepted
prose spellings. The regex is generated from the table's spellings;
`Unit:` lines are validated against the table's keys; the gallery
lowercases and compares against the same keys it reads out of the
store. Whether that table lives inside `provenance_scanner.py` (the
only thing that parses the annotation grammar today) or in a small
module of its own is a method question for the provenance skill under
Method Belongs to the Skill, not one to escalate. I would put it in
the scanner and let the gallery never see it.

## Q3 -- Who enforces a missing `Unit:` line?

Two checks, two questions, each where it already runs. Neither needs
the bound written into a second store.

- **The gallery check enforces PRESENCE, on exactly the bound.** It
  only ever sees served pointers, so "every served constant declares a
  unit" is the question it is already asking; it just does not fail
  when the answer is no. Make NO UNIT (and NO VALUE) a FAIL verdict
  alongside DRIFT. The denominator is the served set by construction,
  the bound never has to be exported to the orrery, and L-305's own
  closing line -- MATCH by name for every new pointer -- becomes
  reachable and checkable in the same run. This is the fix from
  framing point 1 and it costs one condition in one return statement.

- **The scanner enforces VALIDITY, everywhere.** Any `Unit:` line
  present must carry a key from the table, and a `Unit:` line must
  agree with the name's suffix where the name has one. This is global,
  but it is discovery against a stated pattern over a finite tree, so
  it terminates, and it requires no judgment. It does NOT require
  presence, which is what would grow the denominator by 53.

The `Source:` proxy should be dropped, and not only because it was
miscounted. `Source:` marks provenance; the bound is about serving.
They are different axes, and Check All Parallel Pipelines already
records what a count carried across axes does.

## Q4 -- Is "reachable from a served pointer" the right bound?

Yes, and it is the only one that is the artifact rather than a stand-in
for it. Any prefix cut is a proxy that has to be maintained by hand and
fails silently the first time a Sun constant lacks a prefix, which four
already do. The pointer set is the exhibit's rendered numbers, it is
enumerable at any commit, and it is already the thing the check walks.

One class to name while we are here, so it is not counted as "five
NOT IN STORE" forever: the five are values that are not top-level in
`constants_new.py` (four dict entries and one function default). A
`Unit:` line is a top-level-constant mechanism and will not reach them.
The provenance skill already has a dict-level status line that scopes
one kind and one source to a whole dict; a dict-level `Unit:` is the
same shape. That is a follow-on question, not this one, but the
selector answer should not pretend those five are inside it.

## Q5 -- Unit name, or dimension too?

A unit name is enough, and a dimension field would be premature. The
thing that must NOT happen is a silent fall-through when two units
share a dimension and no factor exists between them. Today the check
already refuses to type factors and reports "config unit has no factor
in the store" when a unit is unknown -- that is the right shape. Keep
it, and make that verdict fail the run too. So: same key on both
sides, compare exactly; different keys with a store-derived factor,
convert and compare; different keys and no factor, FAIL with the pair
named. nPa against Pa or degrees against radians then arrives as a
loud failure that names the missing factor, which is what we want. It
does not arrive as a wrong MATCH, and that is the only way a dimension
field would earn its place.

Two factors will not come from the store and that should be said now
rather than discovered later: degrees-to-radians is pi, and a
dimensionless quantity needs an explicit key (`1` or `dimensionless`)
so that "no unit" and "unit is none" are distinguishable. An absent
`Unit:` line must never read as dimensionless. Five of L-305's fifteen
new values are dimensionless, so this is the first case, not a
hypothetical.

## Q6 -- Worksheets

A unit column belongs in the worksheet schema, and it changes what the
checker is asked to verify in one specific way. Today a citation
verdict asks whether the named source publishes the value. It does not
ask in what unit. A row can be value-YES and citation-YES while the
code holds the number in a different unit than the source states it,
and the schema has nowhere to say so. For L-305 that is the live risk:
Shue's coefficients, a pressure in nPa that a paper may state in Pa, a
field in nT, a speed in km/s. The check "is 2 the right number" passes
whether the unit is nPa or Pa.

So the added column is the source's unit as the checker read it, and
a fourth thing goes in Notes: the conversion, if any, between the
source's unit and the store's `Unit:` line, or "none". That is the
existing `Derived:` discipline (report no more figures than the
numerator) moved into the worksheet where the checker can be held to
it. It also gives The Exhibit Requirement's quotation something to
carry: a quote that states "3.986004418e14 m^3 s^-2" and a store line
that says km^3/s^2 are reconciled on the worksheet, not in a
reviewer's head.

## In one paragraph, for the decision

Declare `# Unit:` in the store as a fifteenth comment key. Keep the
name suffixes and have the scanner check they agree. Put one canonical
unit table in the orrery; generate the prose regex from it and validate
`Unit:` lines against it; the gallery reads keys out of the store and
holds only store-derived conversion factors. Make the gallery run FAIL
on NO UNIT, NO VALUE and no-factor, so the bound enforces itself
without being exported. Add a source-unit column to the worksheet
schema. Do the migration on the 33 constants the served pointers
reach, plus L-305's fifteen. Then the five NOT IN STORE and the four
already-served degree pointers are one named class for a later slice.
