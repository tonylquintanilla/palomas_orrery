# Design record -- units in the store, and the orrery as producer

Built on orrery `2432db648f317387527a920aa0f3d40c2ed2f3df`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `9c056d1a27554a3b0afd27530ab9995c9929ff96`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-11
Type: DESIGN (zero code). Origin: L-305 Gap item 3, which asked a narrow
question and opened a wide one.
Status: Tony's rulings are recorded below as ruled. The questions at the
end are open and go to Fable before anything is built.

This document is both the session record and the review request. A
reviewer should read it as a design to attack, not a decision to ratify.

## For a reviewer without the resident layer

If you are reading this outside the Paloma's Orrery Project, you have no
resident protocol and no installed skills. Fetch these at the orrery SHA
above and read them before replying:

- `PROJECT_INSTRUCTIONS.md` -- The Artifact Bounds the Audit, The Braid,
  A Check That Cannot Fail Is Not Passing, Check All Parallel Pipelines,
  Fetched vs Recalled Convention.
- `skills/provenance-discipline/SKILL.md` -- constants, citations, units.
- `skills/interactive-exhibit/SKILL.md` -- it owns the served-data
  provenance contract (value / unit / source / orrery_constant) that
  this design changes.
- `skills/gallery-cache-builder/SKILL.md` -- it owns the serving cache
  and `data/objects_config.json`, the file this design splits.
- `skills/gallery-assembler/SKILL.md` -- the design moves a join into
  the assembler.

**Name in your reply which of those you actually read.** A reply that
does not name them is telling us it did not read them.

The author of this code is not a professional programmer. Tony
Quintanilla is a retired civil and environmental engineer with sole
commit authority and final judgment; the codebase's polish is the
product of two years of AI collaboration under the protocol above and
says nothing about his fluency with the mechanism. Unpack jargon on
first use. Write for him.

## How this started

L-305 rebuilds Earth's magnetosphere on two published models and will
add fifteen served values. Twelve of them are not lengths. The gallery's
store-drift check infers each constant's unit from a SUFFIX on its name
and knows only `_RADII`, `_AU`, `_KM` and an Earth-radii special case,
so those twelve report NO UNIT -- printed, counted as unexaminable, and
not a failure, because only DRIFT fails. The run would have gone green
with twelve of fifteen new values unchecked.

A patch extending the gallery's suffix table was written and HELD
UNRUN, because it put a naming vocabulary for orrery constants inside
the gallery repo.

## Measured, at the two SHAs above

Not recalled. Every figure below was produced this session by running
the real code against the real files.

**The served config.** `data/objects_config.json` is 40 KB, 163 dicts,
of which 53 carry an `orrery_constant` pointer. The other ~110 are
presentation the gallery owns: colour, opacity, `n_points`,
`marker_size`, `info_url`. Both kinds sit in the SAME dict -- one entry
holds `"radius": {"value": 0.2, "unit": "R_sun"}` beside
`"color": "rgb(70, 130, 180)", "n_points": 25`.

**Nothing generates that file.** The only writes are one-off patch
scripts in `documentation/`. It is maintained by hand.

**The check today.** 53 pointers: 48 MATCH, 0 DRIFT, 0 NO UNIT, 5 NOT
IN STORE. The five are values that are not top-level constants --
`idealized_orbits.py::planet_poles['Sun']`, `['Earth']`, `['Jupiter']`,
`['Saturn']`, and a default in
`solar_visualization_shells.py::create_sun_galactic_tide`. Two of them
already serve `deg` and two serve an empty unit, so non-length units are
ALREADY being served unchecked. (Credit: Fable found this; it corrects
an earlier draft of ours that said the served set was all lengths.)

**Of the 48 matches**, 44 compare in the same unit, 2 convert across
units (`SOLAR_RADIUS_AU` served as `r_sun`,
`EARTH_EQUATORIAL_RADIUS_KM` served as `r_earth`), and 2 take a
coefficient fast path. An earlier review put the conversion count at 27
of 48; run through `judge`'s real branches it is 2.

**The store.** `constants_new.py` holds 88 top-level assignments: 57
bare literals and 31 expressions. Its annotation grammar sits BELOW each
assignment and uses fourteen keys with `+:` continuations -- Note,
Source, Derived, Ref, Also, See, Corrected, Resolved, Declared, Status,
Calculation, Access, Sources, Record. There is no `Unit:` key. There are
59 `# Source:` heads and 72 `# Source+:` continuations; 51 heads sit
directly under an assignment.

**Suffix decoding does not scale.** Six constants exist whose unit
cannot be read from the name: `EARTH_GM_KM3_S2`,
`EARTH_ROTATION_RATE_RAD_S`, `SPEED_OF_LIGHT_KM_S`, `SGR_A_DISTANCE_PC`,
`SGR_A_MASS_SOLAR`, `GRAVITATIONAL_CONSTANT_SI`. All six return None.

**The orrery runner.** `orrery_maintenance_run.py` runs five GENERATORS
(ledger index, skill manifest, module atlas, data inventory, document
index) and fourteen CHECKERS whose verdict informs the push call. Two
checkers are marked report-only. `doc_index.py`'s comment records Tony's
ruling on why it is a generator: a checker "would leave the
hand-maintained copy in place and only make its drift loud, which is the
opposite of fixing the producer."

## Tony's rulings this session

**1. A unit is a declared field, not a suffix.** `# Unit:` becomes a
fifteenth comment key beside the value. His reason, in his words: in
engineering he has always used units, not literals. A unit is data about
a number, not part of the number's name.

**2. The suffix is dropped as a declaration, not cross-checked.** A
review proposed keeping the suffix and having the scanner check it
agrees with the `Unit:` line. Tony declined: two declarations of one
fact can disagree. Names stay readable English; machinery stops parsing
them.

**3. Order matters, and it is measured.** Remove suffix reading before
the `Unit:` lines exist and 46 of 48 checks go dark -- reporting NO UNIT
while the run still shows green. So: `Unit:` lines land first, then
missing-unit-fails and suffix-dropping land together.

**4. Dimensional analysis is the real check.** A text check asks whether
a unit string is spelled correctly; only dimensional analysis asks
whether it is the CORRECT unit. A constant labelled `km` that is
actually a speed passes a spell-check. Tony's view: this belongs as its
own check in a maintenance runner. The 31 expressions already carry
checkable dimensions -- `EARTH_LEO_INNER_KM = EARTH_EQUATORIAL_RADIUS_KM
+ EARTH_LEO_LOWER_ALTITUDE_KM` is only valid between like dimensions.

**5. A cited value is a new constant unless it can be derived.** A
fitted coefficient from a paper is a primary datum with nothing behind
it but its source. A number a paper prints that our own constants could
compute should be an EXPRESSION, not a literal. Tested: Jelinek's bow
shock standoff derives in the store's own parser
(`15.02 * 2 ** (-1 / 6.55)` = 13.5117); Shue's magnetopause standoff
needs a hyperbolic tangent and is silently DROPPED by the parser, which
allows only add, subtract, multiply, divide and power.

**6. The orrery exports; the gallery does not parse orrery source.**
The parser runs gallery-side today only because no export exists -- the
check independently re-reads the store to catch hand-copy errors. Under
this design the orrery emits the 53 value/unit/source triples as a
generated file, the arithmetic resolves in the orrery where `math` is
simply imported, and the gallery never interprets Python.

**7. The export cannot go stale, because the orrery runner keeps it
current** -- a sixth GENERATOR alongside the five that exist, run on
every revision, exactly as `data_inventory.py` and `doc_index.py` are
run now.

**8. The join happens in the assembler, not in the config file.** Orrery
values and gallery presentation stop sharing a dict. The gallery keeps
colour, opacity, point counts and info URLs; the orrery owns value, unit
and source; the assembler joins them on the pointer name.

## What this does to the gallery's drift check

It does not disappear. It changes question. It stops asking "does this
hand copy match the store" and starts asking "is the export I serve the
one the orrery published" -- which is the SHA round trip, and unforgeable
in a way a value-by-value comparison is not.

## Open questions -- for the reviewer

1. **Attack ruling 2.** A prior review argued for keeping suffixes with
   a scanner agreement check. Tony overruled it on the grounds that two
   declarations can disagree. If that is wrong -- if the agreement check
   catches a migration typo that nothing else catches -- say so now.

2. **Does the export supersede the value-by-value drift check, or do
   both live?** If the export is generated and SHA-pinned, is a
   per-value comparison still earning its place, or is it the
   hand-maintained copy's net being kept after the hand copy is gone?

3. **Where do the five non-top-level values go?** `planet_poles[...]`
   entries and a function default cannot carry a `# Unit:` line, which
   is a top-level-constant mechanism. Two of them already serve `deg`
   unchecked. Does an export change this, and is a dict-level unit
   declaration the answer?

4. **Is the assembler the right join point, or the cache builder?** The
   builder already fetches, stages, guards and swaps served data
   nightly; the assembler already resolves scenes from served data.
   Which one should hold the join, and why?

5. **Dimensional analysis against what, for the 57 bare literals?** The
   31 expressions check themselves. A bare literal from a paper has no
   arithmetic to contradict, and L-305's fifteen are all bare literals.
   Is there a real check there, or is the honest answer that provenance
   is the only check a primary datum gets?

6. **The `tanh` question, if ruling 6 holds.** If arithmetic resolves
   orrery-side before export, does the store still need a function
   whitelist in its parser, or does the need vanish with the export?

7. **Sequencing.** L-305 is on the critical path and its renderer is the
   next deliverable. Does it proceed under today's architecture and get
   migrated later, or does the export land first? The Braid says bound
   the program to what the current artifact renders; it does not say
   which of two programs goes first.

## What we do not want back

No code, no diffs, no patches. No ledger handles or ledger blocks --
handles are issued in the orrery repo and a proposed one is usually
already taken. Do not re-derive the measurements; if you think one is
wrong, name it and say how you would check it.

Disagreement is the point of asking. Where the framing here is itself
wrong, say that first.

Written September 2026 with Anthropic's Claude Opus 5.
