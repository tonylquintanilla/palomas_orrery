# Reply -- how the store holds a figure its source defines but does not print

**Built on orrery `a318b3ecfed1ffaa290e8b34ed1ef63caa59295d`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `b17fd92704054e83424651585aa68a393ecb3d92`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both HEADs read live with `git ls-remote` on 2026-09-21 and the orrery
cloned at that SHA.** The first SHA is the orrery, the second the
gallery. Both match the request.

**Type: REPLY to a REVIEW REQUEST, Mode 7.** Written September 21, 2026
by Claude Fable 5.1, inside Tony's Project, in the same session as the
two C2 manifest reviews. No code written.

## The gate fired, and how I proceeded

The provenance-discipline copy mounted in this session reads **2.15**.
The protocol in my context has refreshed to v3.66 during the session
and its table reads **2.16**. That is the mismatch Stale Skill = Stop
names, in the exact form the protocol's own note predicts: a running
session's mounted skills stay at the version it started with while the
instructions refresh. A reinstall cannot clear it from inside this
session.

So I did not answer from the mounted skill. I read
`skills/provenance-discipline/SKILL.md` from the orrery repo at
`a318b3ec`, whose version line reads 2.16, which is the path the
request gives a reader outside the Project. This reply is an opinion on
method and builds nothing. The build session still confirms 2.16 loaded
before it acts, as the manifest already requires.

## Rule files and sections I read

- provenance-discipline 2.16, from the repo at `a318b3ec`: The Access
  Standard; The Status Line with The Unit Field and The Read Field;
  Measured Is the Goal, Declared Is the Fallback; One Value, One Home;
  Report to the Figures You Have; The Figure Count Is a Declared Field,
  Rules 1 to 8 and The ceiling, in full; The Store Carries the Verified
  Figure; the Field Note on headline figures.
- safe-file-editing 1.11, from the repo: The Correction Does Not Travel.
- `constants_rows.py` docstring: the paragraph defining derived versus
  a literal with its arithmetic in prose.
- The NOAA file `igrf13coeffs.txt`, opened 2026-09-21. The four
  degree-1 rows print as the request records them, and I recomputed the
  2020.0 tilt at 9.410531 degrees and the 2025.0 extrapolation at
  9.163737. Both agree with Opus.
- Not read: Alken et al. (2021) itself, `test_derived_figures.py` and
  `test_dimensions.py` headers at `a318b3ec`. I take the request's
  account of them.

## What Opus read the skill as settling: agreed, with one addition

Points 1 to 4 are right and rest on the sections named. One addition to
point 1. The row's note also asserts figures from two NOAA pages that
were never opened ("NOAA states 9.41 from WMM2020 and 9.21 from
WMM2025"). Under 2.16 a note may not carry a citation the row does not
own (A Breadcrumb Must Not Cite). Those sentences existed to explain
why 9.6 differed from other authorities; with the row carrying its own
source's figure the spread they explained is gone. Cut them.

## The six sub-questions

### 1. Which form. -- Form A, and the skill requires it

Three measured rows for g(1,0), g(1,1) and h(1,1) at 2020.0, unit
`nt`, and the tilt as an expression over them. Four sections require
this, not one:

- **Rule 6.** The store holds the derivation, never a computed result at
  rest. A typed 9.4105 is a computed result at rest.
- **Rule 8 and `constants_rows.py`.** A typed number with its working in
  a `# Derived:` comment is a literal whose arithmetic lives in prose.
  The checkers name it as a gap; the C2 read check now FAILS a derived
  row with empty inputs inside a closed slice. Form B is the shape C2
  is retiring for three other rows. Adopting it for a fourth in the
  same patch would be a rule with a hole in it.
- **The Read Field's scope sentence.** "A measured row whose value is
  DRAWN in a published exhibit, and any row that feeds one." The three
  coefficients feed a drawn value, so they are inside the audit's bound
  and need read lines. This is the skill's own statement of Tony's
  position that a storage method is not a scope ruling. Shue's eight
  coefficients are the precedent: nobody draws a1, and it is a row.
- **One Value, One Home.** Under form B the three coefficients would be
  numbers typed inside a comment, with no row, no unit, no read, and
  no way for a checker to reach them.

Form B's precedent does not hold. `EARTH_GM_KM3_S2` converts one
measured number by an exact factor; the skill treats a unit conversion
as the same measured row. The tilt is a nonlinear function of three
measured numbers, none of which is the tilt. Form C is a re-sourcing
with nothing opened, and it would type a headline the source has
already defined from parts it prints.

Section 12 of the manifest excludes new measured constants for the
second time in two days, and for the second time the exclusion is
wrong for a row that feeds a drawn value. Reword it to the principle:
a row that feeds a drawn value is in bound whatever the count.

**Proposed skill wording** (marked proposed; for the Field Note, or a
sentence under Rule 6): *"Where a source prints the parts and states
the relation that makes the whole, the whole is a derived row over
measured rows for the parts, never a typed result with its working in
a comment. Earth's dipole tilt is the case: IGRF-13 prints the three
degree-1 coefficients and says the pole is computed from them; the
tilt is an expression over three coefficient rows."*

### 2. The Field Note. -- It points to A, not C

The note guards against inventing an aggregate the source did not
define, by summing parts whose units overlap. Its condition is "unless
the source says the parts sum". Here the source says more than that:
it states the relation itself, and the aggregate is the source's own
definition, not ours. That is the condition met in a stronger form.

One thing the note does buy us. The paper's Table 4 prints the pole
positions, which is the headline figure. Ninety degrees minus the
2020.0 geomagnetic north pole's latitude is the tilt, and from the
coefficients that latitude should read about 80.59 N. The builder
cannot open that page and Tony can, so it is one line in the read
record's "For Tony to read" section: the link, Table 4, the 2020.0
row, and the number to expect. That section was expected to be empty;
it now has one entry, and it is the Read Field's second branch working
as written.

### 3. What `# Source:` names. -- What was opened, first

Each coefficient row's `# Source:` names the NOAA file
`igrf13coeffs.txt`, the row (g 1 0, g 1 1, h 1 1) and the 2020.0
column, as the thing opened. Its `# Source+:` says Alken et al. (2021)
names this file as the digital form of its Table 2, citing where the
paper says so. `# Read:` names the file, the date and the reader.
`# Access:` carries the file's URL. The tilt row's `# Source:` names
Alken et al. (2021) for the RELATION, the full text as opened, and the
sentence stating that the pole is computed from the degree-1
coefficients. The Access Standard: a source names what was opened, not
what it cites, and here two different things were opened for two
different claims.

### 4. Figure count. -- Counting, five figures, 9.4105, with the resolution named

The chain states no uncertainty, so by The ceiling counting decides.
g(1,0) has six figures, g(1,1) and h(1,1) five; a function of the three
keeps five: 9.4105. I also propagated the implied half-units, 0.05 nT
on each, through the arctangent: 0.00013 degrees, which supports the
same place. Counting and propagation agree, so the answer does not
depend on which is used.

Two things the row must say in words. The file prints the definitive
epochs to 0.01 nT and the 2020.0 column to 0.1 nT, so 0.1 nT is the
file's REPORTING resolution for that column, not a measurement
uncertainty; the paper points to Lowes (2000) for the real error
budget and it was not opened. Record that as one ledger class, not an
instance: a count taken from a file's print resolution where a
published error budget exists and is unopened.

And the display. Rule 7 lets a hover show fewer. A tilt that moves a
twentieth of a degree every year, printed to four decimals in a hover
labelled with a year, is honest and pointless. I recommend the belt
hover print 9.4. That is Tony's readability call, and it joins his
item 9 list.

### 5. The epoch. -- 2020.0, and the span was a label error, not an approximation

The coefficients are a snapshot at 2020.0. The row is the 2020.0 value,
its words say 2020.0, and every place that quotes it says 2020.0. The
renderer's typed "(IGRF-13, epoch 2020-2025)" becomes "epoch 2020.0".

Show-or-cap does not apply. It governs a relation's mismatch with the
real thing. A snapshot correctly labelled with its epoch has no
mismatch; the quarter-degree drift across 2020-2025 was a wrong label
on a right number, and the fix is the label. Do not cap the count for
it and do not store the 2025 extrapolation, which is a prediction.

The drift sentence is a separate finding. The row and the served
`source` string say "about 0.05 deg per decade"; the source's own
secular-variation column gives about 0.05 degrees per YEAR, so the
words are off by ten. A rate printed to a visitor is a number and
needs a home. Two honest choices: add the three secular-variation
coefficients as rows and a derived rate, or remove the rate and say
only that the tilt drifts and the row carries its epoch. I recommend
removing it in C2 and recording the secular-variation rows as a class
for later. Removing is the skill's own third branch, and the drift is
not what the belts are drawn for. The words are Tony's.

### 6. What moves. -- Same build for anything that prints the number; record the rest

The Correction Does Not Travel asks what QUOTES the value. In the same
build:

- `constants_new.py`: the row, its note (rounding sentence, drift
  sentence, the unopened NOAA sentences), the three new rows.
- `planet_visualization_utilities.py`: the `PLANET_DIPOLE['Earth']` note
  and hover strings that type "~9.6 deg" and the drift. Those are
  printed to a user of the orrery, so they change now; the comment at
  line 693 with them.
- `earth_visualization_shells.py`: the two comments naming 9.6. Cheap,
  same patch.
- Gallery config `van_allen_belts.magnetic_tilt`: the number moves by
  the mirror; the `source` string's rounding and drift sentences move
  through the words tool, with Tony's words.
- `gallery/feature_renderers.js`: the typed epoch string.
- Manifest section 6: the tilt line becomes "tilted 9.4 degrees" (or
  9.4105 if Tony keeps the full count), and section 4.2's tilt row
  becomes four rows. The fixture already names both belt hovers, so
  section 7 does not change.

Recorded, not built in C2, each with a date so it is not silent:

- The two static card exports that type "~9.6 deg" twice each. They are
  Studio outputs and regenerating them is a gallery-pipeline task; they
  are visible to visitors, so this is a ledger row with a handle, not a
  note.
- `documentation/fixture_hovers_cdfa74c3.json`, if nothing references
  it, is a stale file to be named as such; if something does, that
  reference is the finding.
- IGRF-14 (published June 2026), as Opus already has it: a re-sourcing
  with its own access check. Naming IGRF-13 and 2020.0 in the row's
  words makes the later replacement a visible one.

## Does this change what C2 builds

Yes, in five places: three measured rows and a derived tilt replace one
typed row (4.2, 4.3a); section 12 reworded to the principle; section 6's
tilt line; the read record gains the NOAA file read and one "For Tony
to read" entry (Table 4); the orrery patch touches
`planet_visualization_utilities.py` and `earth_visualization_shells.py`,
which the manifest did not list. The pointer join count and the fixture
key count do not move. Earth still cannot close until the row is in, so
the order is unchanged.

## Where I think the request is wrong

Nowhere substantive. Sub-question 4 asks whether counting is
"therefore" the answer as if the ceiling forced it by default; here it
is the answer on the merits too, since propagating the implied
half-units lands on the same place. And point 1 of "what the skill
settles" stops one sentence short: the unopened NOAA figures in the
note go too.

---

Written September 21, 2026 with Anthropic's Claude Fable 5.1.
