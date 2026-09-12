# Design record, revision 2 -- units in the store, and the orrery as producer

Built on orrery `2432db648f317387527a920aa0f3d40c2ed2f3df`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `9c056d1a27554a3b0afd27530ab9995c9929ff96`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-11
Type: DESIGN (zero code). Origin: L-305 Gap item 3.
**Supersedes** `DESIGN_unit_field_and_export_20260911.md` (revision 1) of
the same date, which went to Claude Fable 5.1 for review. Fable's reply
is folded in below and its corrections are named where they land.

## For a reviewer without the resident layer

Fetch at the orrery SHA above and read before replying:
`PROJECT_INSTRUCTIONS.md` (The Artifact Bounds the Audit, The Braid,
A Check That Cannot Fail Is Not Passing, Check All Parallel Pipelines),
and `skills/` for `provenance-discipline`, `interactive-exhibit`,
`gallery-cache-builder`, `gallery-assembler`. **Name in your reply which
you read.**

The author of this code is not a professional programmer. Tony
Quintanilla is a retired civil and environmental engineer with sole
commit authority; the codebase's polish is the product of two years of
AI collaboration and says nothing about his fluency with the mechanism.
Unpack jargon on first use.

## What revision 1 got wrong

**One framing error, found by Fable, and it is the important one.**
Revision 1 called the new gallery check "the SHA round trip" as though
it were one hop. It is two: the gallery serving what the orrery
published, and the orrery publishing what the store holds. Revision 1
left the second hop unchecked. The fix, which this revision adopts: the
export carries the hash of the `constants_new.py` bytes it was generated
from, and a checker in the orrery runner compares that hash to the file
on disk. The runner informs the push but is not a hook, so a push
without a run would otherwise leave a stale export with nothing saying
so.

**One count of ours was low.** Revision 1 named six constants whose unit
cannot be read from the name. Measured: **17 of 88**.

**One count of Fable's was low.** Its review says the suffix reader
covers "the 42 values the check already handles correctly." Measured:
**71 of 88** are suffix-readable. Its argument survives -- the
cross-check would still only protect values that already work -- and the
retiring reader can draft 71 first-pass `# Unit:` lines rather than 42.

## Measured, at the two SHAs above

Every figure produced this session by running the real code.

**The served config.** `data/objects_config.json`: 40 KB, 163 dicts, 53
carrying an `orrery_constant` pointer. The other ~110 are gallery
presentation -- colour, opacity, `n_points`, `marker_size`, `info_url`.
Both kinds share a dict today. **Nothing generates the file**; the only
writes are one-off patch scripts.

**The check today.** 53 pointers: 48 MATCH, 0 DRIFT, 0 NO UNIT, 5 NOT
IN STORE. Of the 48 matches, 44 compare in the same unit, 2 convert, 2
take a coefficient fast path. (Revision 1's reviewer put conversions at
27 of 48; run through `judge`'s real branches it is 2.)

**The five NOT IN STORE**, named: `idealized_orbits.py::planet_poles`
for Sun, Earth, Jupiter and Saturn, and a default in
`solar_visualization_shells.py::create_sun_galactic_tide`. Two already
serve `deg` and two an empty unit, so non-length units are ALREADY
served unchecked. (Fable's find; revision 1 said the served set was all
lengths.)

**The store.** 88 top-level assignments: 57 bare literals, 31
expressions. Annotations sit BELOW each assignment, fourteen keys with
`+:` continuations, no `Unit:` key. 59 `# Source:` heads, 72
continuations, 51 heads directly under an assignment. **2 of 88 carry a
`# Status:` line.**

**Importing the store is safe.** `constants_new.py` imports numpy and
datetime, defines one function (`color_map`), and has no top-level
statement other than its docstring. Nothing executes on import.

**L-305's fifteen**, run against the real check today: 3 MATCH, 12 NO
UNIT. **Dropping the suffix before `# Unit:` lines exist**: 2 MATCH, 46
NO UNIT.

**Derivation.** Jelinek's bow shock standoff evaluates in the store's
own parser (`15.02 * 2 ** (-1 / 6.55)` = 13.5117). Shue's magnetopause
standoff needs `tanh` and is silently DROPPED.

**The orrery runner.** Five GENERATORS, fourteen CHECKERS whose verdict
informs the push call, two marked report-only. `doc_index.py`'s comment
records Tony's ruling on generator-versus-checker: a checker "would
leave the hand-maintained copy in place and only make its drift loud,
which is the opposite of fixing the producer."

## Tony's rulings

Rulings 1 to 8 are from revision 1 and all survived review. Fable's
finding, which is worth repeating: five of them are not new judgments
but rules the provenance skill already carries, applied to units --
the Status Line rule (a declaration is the only store, inference is
REMOVED rather than kept as a fallback) and One Value One Home.

**1. A unit is a declared field, not a suffix.** `# Unit:` becomes a
fifteenth comment key. In his words: in engineering he has always used
units, not literals. A unit is data about a number, not part of the
number's name.

**2. The suffix is dropped as a declaration, not cross-checked.** Two
declarations of one fact can disagree. Names stay readable English;
machinery stops parsing them. Fable attacked this on request and
withdrew: a suffix agreement check can only fire on constants that have
a suffix, so it protects the values least likely to be wrong and nothing
new. It adds one READING rule, not a scanner rule: a name carrying a
unit word must agree with its `# Unit:` line, because a reader will
trust `_KM` over a comment. And the retiring suffix reader gets one last
job -- generating the first draft of the 71 `# Unit:` lines it can read.

**3. Order matters.** `# Unit:` lines land first; missing-unit-fails and
suffix-dropping land together. Otherwise 46 of 48 checks go dark while
the run stays green.

**4. Dimensional analysis is the real check.** A text check asks whether
a unit is spelled correctly; only dimensional analysis asks whether it
is the CORRECT unit. Its own check in a maintenance runner. The 31
expressions carry checkable dimensions -- `EARTH_LEO_INNER_KM =
EARTH_EQUATORIAL_RADIUS_KM + EARTH_LEO_LOWER_ALTITUDE_KM` is valid only
between like dimensions.

**5. A cited value is a new constant unless it can be derived.** A
fitted coefficient from a paper is a primary datum. A number a paper
prints that our constants could compute is an EXPRESSION.

**6. The orrery exports; the gallery does not parse orrery source.** The
gallery parses today only because no export exists. Fable sharpened
this: the need for a `tanh` whitelist does not vanish with the export,
it vanishes with the PARSER. The generator IMPORTS `constants_new.py`
and reads names; every expression evaluates the way Python evaluates it.
Both parsers -- the gallery's and the store's arithmetic walker -- are
deleted. The only text read is the comment grammar, which the scanner
already owns.

**7. The export cannot go stale**, because the orrery runner keeps it
current as a sixth GENERATOR -- plus the store-hash checker named above.

**8. The join happens in the assembler, not in the config file.** The
builder SERVES the export (fetched from the orrery at HEAD each nightly
run, the SHA recorded, inside the swap directory, failing rather than
serving yesterday's). The assembler JOINS at scene time, which keeps the
served export byte-exact and is what makes the gallery-side hash check
possible at all.

**9. `constants_new.py` holds physical values only.** NEW this
revision, and it is the ruling that simplifies the rest. Five values in
the store are not measurements and have no unit to declare. Rather than
invent a "no unit applies" mark, they leave the file. Then every line in
the store has a unit, a blank is unambiguously an error, the export is
the whole file, and there is no skip list and no second list of what the
gallery wants. The file becomes what its name half-claims: the store of
measured and derived physical values.

### The five, with destinations ruled and import direction checked

| Value | Destination | Why it works |
|---|---|---|
| `stellar_class_labels` | `visualization_core.py` | `visualization_2d` and `visualization_3d` already import from core; `star_visualization_gui` changes one import line |
| `HORIZONS_MAX_DATE` | `celestial_objects.py` | 194 objects with Horizons IDs and 65 date-range fields; already imports `datetime`; imports nothing from `constants_new`, so no cycle |
| `DEFAULT_MARKER_SIZE` | `palomas_orrery_helpers.py` | see below |
| `CENTER_MARKER_SIZE` | `palomas_orrery_helpers.py` | see below |
| `spectral_subclass_temps` | STAYS | physical -- kelvin; used in 9 modules; needs a `# Unit:` line like everything else |
| `KNOWN_ORBITAL_PERIODS` | STAYS | physical -- days; used in 18 modules; same |

The marker sizes were first ruled into `palomas_orrery.py`. That fails:
`palomas_orrery.py` imports FROM `palomas_orrery_helpers.py` at line 84,
so helpers cannot import back without a cycle. Helpers already imports
`constants_new` at line 171 and already holds shared plotting utilities,
so defining them there and letting `palomas_orrery.py` take them on the
import line it already has is the same idea one level down, with no new
module. Tony's ruling on being shown the cycle.

Note for whoever moves `stellar_class_labels`: its four importing files
are the only ones seen this session carrying CRLF line endings.

## Two additions from Fable, adopted

**Export the whole store, not the 53 pointed-at values.** Exporting only
what the gallery points at means the orrery must keep a list of what the
gallery wants, and that list drifts. The store is the denominator and it
is closed at any SHA. With ruling 9 in place this is exactly "every
physical value, each with a unit."

**The `# Unit:` walk is the `# Status:` walk.** Only 2 of 88 carry a
`# Status:` line, and the Status Line rule is [CRITICAL] -- an unmarked
value is unexamined. The migration that visits each assignment to write
a unit is the same visit that writes its status. Two walks over one file
for one reason is one review done twice.

## What the gallery's drift check becomes

Not one check, but two, and neither is today's:

- **Gallery side:** the served export's bytes equal the orrery's export
  at a recorded orrery SHA, printing the SHA compared against so it
  cannot go green by never resolving.
- **Join side:** every pointer in the gallery's config resolves to a row
  in the export, by name, and a pointer with no row FAILS. That is the
  check the current run cannot make -- it prints NOT IN STORE five times
  and stays green.

The per-value comparison is the hand copy's net, kept after the hand
copy is gone. Retire it.

## Sequencing, ruled

L-305's renderer proceeds under today's architecture. The export is not
a gate on it. The bounded cost: twelve of fifteen new values report NO
UNIT until the export lands, recorded as ONE ledger row for the class,
not fifteen. The held gallery suffix patch stays held and is not run.

Two things go into L-305 now because the export will require them
anyway: `# Unit:` lines on the fifteen, and the derivation for the bow
shock standoff.

## Still open

1. **The five non-top-level values.** Fable proposes the Status Line
   scoping -- `planet_poles` is one dict, one kind, one unit, so one
   line on the dict -- and that One Value One Home puts it in the store,
   with the `create_sun_galactic_tide` default becoming a named
   constant. Not yet ruled. Its lean is to do this AFTER L-305, as its
   own slice, because two of the five are the Sun's and Earth's poles
   and a wrong move puts a closed exhibit back under Mode 5.

2. **Whether the derive-and-compare check is real for these two
   papers.** Fable proposes transcribing both a paper's coefficients and
   a result printed from them, deriving one from the other. Checked
   against the PDFs and it is thinner than it sounds here: Jelinek's R0
   IS the standoff at 1 nPa, so deriving it is circular, and Shue's
   redundancy sits in Table 1's SEED column rather than the fitted
   values being stored. What IS available is Jelinek's second refit at
   eqs. 17-18 -- 12.90 and 14.94 against the model's 12.82 and 15.02 --
   which catches a transcription slip but is not the check described.
   **Ruled 2026-09-11, after this revision's first draft:** three
   options, not two -- the eqs. 17-18 refit, provenance alone stated on
   the row, or TONY'S OWN READ of the paper against the row, recorded
   with page or table, date, and that it was his. The three available
   checks cover different failures and none substitutes for another:
   Mode 5 sees a wrong UNIT instantly and a wrong third decimal never,
   so it is a backstop rather than a check; a cross-model worksheet
   reads the digits and is blind to the render; Tony's read is the only
   one that reaches precision. It needs a scope written once ("where
   critical") and a recorded verdict, or a lapsed habit reads exactly
   like a performed check. A row verified by Tony is a different
   provenance state from one verified by a model, and the worksheet
   schema should say which.

3. **A home for the dimensional check.** Ruling 4 says its own check in
   a maintenance runner. Which runner, and what it checks for the 57
   bare literals, is unsettled. A bare literal has no arithmetic to
   contradict it; provenance may be the only check it gets, and saying
   so on the row is the honest state.

## What we do not want back

No code, no diffs, no patches. No ledger handles or ledger blocks. Do
not re-derive the measurements; if one is wrong, name it and say how you
would check it. Disagreement is the point of asking.

Written September 2026 with Anthropic's Claude Opus 5.
