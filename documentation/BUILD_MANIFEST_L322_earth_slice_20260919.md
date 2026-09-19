# Build Manifest -- L-322, the Earth slice: every Earth constant declares its unit, status, figures and who read its source

**Built on orrery `bb614c7fd4b8b7760c3512baa0c39964972a82e2`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `2ebd001f2ec5d358aa6bb5fa1c6a573be99a502d`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both HEADs were read live with `git ls-remote` on 2026-09-19. Both
repositories were cloned at those SHAs, and every number in section 3
was measured on those clones with the project's own reader,
`constants_rows.py`.**

**Rules this work runs under.** Also fetch, from the orrery at
`bb614c7f`: `PROJECT_INSTRUCTIONS.md` (v3.62) and these skills under
`skills/<name>/SKILL.md`: provenance-discipline 2.13,
ledger-and-session-records 1.11, safe-file-editing 1.11,
agentic-pre-test 1.2, gallery-cache-builder 1.5, interactive-exhibit
1.4. Inside Tony's Project they load as installed skills; compare each
loaded version line with the protocol's manifest table and STOP on a
mismatch. **In your first reply, name the rule files you actually
read.** A reply that does not name them tells Tony they were not read.

**Type: BUILD CONTRACT.** Written before the build, zero code.
**Prepared:** September 19, 2026 by Claude Fable 5.1, Tony Quintanilla
integrator. **For:** Claude Opus 5, as builder.
**Parent contract:**
`documentation/BUILD_MANIFEST_L322_mechanism_20260916.md`, which built
the machinery this walk uses and named this walk as its own session.
**Continues from** `HANDOFF_L334_editor_built_20260919.md` and
`HANDOFF_L322_mechanism_orrery_half_20260916.md`.

Who this is written for: Tony is a retired professional engineer who
builds this project by conversation with AI partners. He is not a
programmer, runs scripts from VS Code's Run button, and commits and
pushes through GitHub Desktop. The quality of the code in these
repositories is the product of that collaboration, not evidence of a
programmer at the keyboard. Write to him in plain sentences, one
request per message. He often works from his phone.

---

## 1. What this build is, in one paragraph

The orrery keeps its physical constants in one file,
`constants_new.py`. Tony has ruled that every constant there declares
four things in comment lines beside it: its unit, its provenance status,
how many significant figures it is good to, and who read the source
against it. The machinery that reads those lines, exports them and
checks them was built on 2026-09-16. No constant has yet been given all
four. This build visits each of the 57 constants whose names begin with
`EARTH_`, once, and writes them. When all 57 are done Earth is marked a
finished slice, and from then on a missing line on an Earth constant
fails the maintenance run instead of only being listed.

## 2. Tony's ruling of 2026-09-19 on who reads a source

On 2026-09-11 Tony ruled that a typed-in number gets checked by someone
reading the source against it, "where critical", and that phrase was
never defined. Asked on 2026-09-19, his answer, in his words:

> "what I meant by critical is where your own search tools cannot read
> a needed source but I can."

So the rule is about ACCESS, not importance:

- Where the builder can open the source, the builder reads it against
  the row and the row's line names the model.
- Where the builder cannot open it and Tony can, the row goes on Tony's
  reading list. That list is Tony's whole share of the reading.
- Where neither can open it, the citation fails provenance-discipline's
  Access Standard: re-home it to an open authority carrying the same
  value, or remove the claim and note the gap.

The scope of rows that need a read at all is unchanged from L-322
ruling (b): a measured row whose value is drawn in a published exhibit,
and any row that feeds one.

One caution the builder must respect. A model reading a source it can
open is a real check only if the source is actually opened. The Access
Standard's rule applies: the line records what was OPENED, with the
title as printed and the table or page, never a paper recalled from
training. A read reconstructed from memory is worse than no read,
because it stops the next reader from looking.

## 3. What was measured at orrery `bb614c7f`

**The store** holds 112 top-level rows. 57 begin with `EARTH_`: 40
typed numbers, 15 arithmetic expressions, and 2 rows in the
`TRANSITIONAL` list (the two magnetosphere standoffs, typed numbers
that are owed back to arithmetic).

**Fields written so far, Earth rows:** unit 28 of 57, status 28 of 57,
figures 0 of 57, read 0 of 57. Across the whole store, figures and read
are 0 of 112. `constants_rows.CLOSED_SLICES` is `()`.

**The 28 rows with a unit and a status** are the radiation belts (6),
the dipole tilt, the three solar wind conditions, Shue's eight
magnetopause coefficients and cut angle and scatter, Jelinek's bow
shock rows (R0, eps, lambda, cut angle, scatter), the two standoffs,
and the observed magnetotail. They need figures and a read line.
A model's read of 14 of them, from Tony's PDFs, is already recorded in
`documentation/L305_gap1_read_record_20260911.md`.

**The 29 rows with neither** need all four lines:

- Radii (3): `EARTH_EQUATORIAL_RADIUS_KM`, `EARTH_POLAR_RADIUS_KM`,
  `EARTH_MEAN_RADIUS_KM`.
- Interior (9): `EARTH_INNER_CORE_KM`, `EARTH_INNER_CORE_RADII`,
  `EARTH_OUTER_CORE_KM`, `EARTH_OUTER_CORE_RADII`,
  `EARTH_D660_DEPTH_KM`, `EARTH_LOWER_MANTLE_KM`,
  `EARTH_LOWER_MANTLE_RADII`, `EARTH_UPPER_MANTLE_KM`,
  `EARTH_UPPER_MANTLE_RADII`.
- Orbits (10): `EARTH_GM_KM3_S2`, `EARTH_ROTATION_RATE_RAD_S`,
  `EARTH_GEOSTATIONARY_RADIUS_KM`, `EARTH_GEOSTATIONARY_RADII`,
  `EARTH_LEO_UPPER_ALTITUDE_KM`, `EARTH_LEO_LOWER_ALTITUDE_KM`,
  `EARTH_LEO_INNER_KM`, `EARTH_LEO_OUTER_KM`, `EARTH_LEO_INNER_RADII`,
  `EARTH_LEO_OUTER_RADII`.
- Atmosphere (4): `EARTH_STRATOPAUSE_ALTITUDE_KM`,
  `EARTH_THERMOPAUSE_ALTITUDE_KM`, `EARTH_STRATOPAUSE_RADII`,
  `EARTH_THERMOPAUSE_RADII`.
- Far field (3): `EARTH_GEOCORONA_RADII`, `EARTH_HILL_SPHERE_KM`,
  `EARTH_HILL_SPHERE_RADII`.

**Five rows still declare the retired unit `dimensionless`:**
`EARTH_MAGNETOPAUSE_SHUE_A5`, `_A6`, `_A8`,
`EARTH_BOW_SHOCK_JELINEK_EPS`, `EARTH_BOW_SHOCK_JELINEK_LAMBDA`.
`constants_tokens.py` has a "named number" marker for a pure number
with a name; adding a token grows the table by a failing run, as
designed.

**Three expression rows have no `# Derived:` line:**
`EARTH_LEO_INNER_KM`, `EARTH_LEO_INNER_RADII`,
`EARTH_STRATOPAUSE_RADII`.

**Which rows need a read.** The gallery's config links 32 Earth
constants by name. Following each one's inputs gives 44 of the 57 that
are drawn or feed a drawn value. The 13 outside that set are
`EARTH_POLAR_RADIUS_KM`, the four interior `_RADII` expressions (the
gallery links the `_KM` rows instead), `EARTH_SOLAR_WIND_SPEED_KM_S`,
Shue's A1 to A5, and the two scatter rows. Shue's A1 to A5 are outside
it only because the magnetopause standoff is a typed number today; once
C2 turns it back into arithmetic they feed a drawn row and come into
scope. Re-derive this set yourself before relying on it; it moves when
the config moves.

**Two constants outside the slice feed it:** `KM_PER_AU` and
`GM_SUN_SI`, both through the Hill sphere. Neither has any field. The
unit checker cannot judge the Hill sphere until they do.

**Sources named on the typed rows today:** IERS Conventions (2010),
Technical Note 36 (equatorial and polar radius, GM, rotation rate); the
NASA Planetary Fact Sheet (mean radius); Dziewonski and Anderson 1981,
PREM (inner core, outer core, upper mantle); the IADC debris guidelines
(LEO upper altitude); NOAA JetStream (stratopause, thermopause);
Baliukin et al. (geocorona); Baker 2018, Meredith 2014 and Li, Tu 2024
(belts); Alken 2021, IGRF (dipole tilt); Shue 1998; Jelinek 2012;
Slavin et al. (magnetotail). `EARTH_LEO_LOWER_ALTITUDE_KM` shows no
source line to the reader. The skill already records that the 1981 PREM
paper is walled and its tabulation is open in several places.

**What the 2026-09-16 session predicted the walk will meet**, from a dry
run. Treat these as leads, not findings:

- `EARTH_GEOSTATIONARY_RADIUS_KM` fails the unit check if the rotation
  rate is declared in radians per second, because the cube root leaves
  a fractional power of radians.
- `EARTH_HILL_SPHERE_KM` fails by a factor of 1,000, because a typed
  `1.0e-9` that converts cubic metres to cubic kilometres is counted a
  second time once units are attached. The same shape waits in other
  slices; the built-in test row `FIX_EMBEDDED` shows the verdict.
- `EARTH_LOWER_MANTLE_KM` will probably report as OVER-DECLARED: the
  660 km row's source supports two figures and the `# Derived:` line
  treats 660 as good to units.
- `EARTH_D660_DEPTH_KM` carries a note that a cross-check is owed
  before the row counts as confirmed (L-253).

**The gallery, at `2ebd001f`.** The export serves 23 rows. Of the
config's 70 links to orrery constants, 53 are not yet served by the
export and still go through the older drift check in
`gallery_maintenance_run.py`; 24 of those 53 are Earth's. Each Earth
row this walk completes moves a link from the old check to the new
ones. The gallery's offline maintenance run is 14 of 14.

**L-249 is built and its ledger block does not say so.** The block is
OPEN, dated 2026-08-25, with a Gap reading "blocked on patch_L248_1".
At `bb614c7f` the four interior boundaries are in the store with their
own source lines, `shell_configs.py` lines 1372 to 1407 take their
radius fractions from those constants, and the five `patch_L249_*`
scripts and `HANDOFF_20260826_L249_...md` are filed. The mantle
disagreement its Note left open is settled in the code.

---

## 4. Stage A -- the ledger patch (orrery)

One patch. It carries the corrections the last two days produced, so
the walk starts from a ledger that is true.

1. **L-337**, as its first change: Tony's addition of 2026-09-19,
   quoted whole from the handoff. The marker is a centring object; the
   Sun's room has one; Earth's needs one; the orrery already offers it.
2. **L-249**: a dated note saying what was built on 2026-08-26 and
   where, then CLOSE it. Its one live residue, the cross-check owed on
   `EARTH_D660_DEPTH_KM`, is carried by this walk and by L-253; say so.
3. **L-322**: a dated line that the gallery half is done and deployed
   (gallery `d2ca28b6`, cache rebuilt at `9ff39cc4`); Tony's ruling in
   section 2, quoted; and a new Gap naming this manifest.
4. **L-340**: a finding from Claude Fable 5.1's review of 2026-09-19.
   `documentation/smoke_arrival.js` compares each room's opening with a
   fixed list written into the check (`EXPECTED`, by display name).
   Ticking another shell to open drawn, or renaming "Crust" or
   "Photosphere", in the editor turns the Arrival check red. A cache
   build does not clear it and the editor does not explain it.
   Reproduced on a throwaway copy of `2ebd001f`. The check should read
   what it expects from the config's own arrival block, by key.
5. **L-340** also already holds the one-off patch that wrote the config
   directly; confirm it is there and add nothing.

**Done when:** the patch runs on a throwaway copy and refuses a second
run; `ledger_index.py` twice prints OK with the same count.

## 5. Stage B -- the skill learns the read line, BEFORE the walk

`# Read:` is parsed by `constants_rows.py` and ruled on L-322, and
provenance-discipline 2.13 does not define it. A convention that is not
in the skill does not travel; the protocol has recorded that lesson
three times. So provenance-discipline goes to 2.14 first, following the
bump routine in ledger-and-session-records, with one protocol entry
(v3.63). It gains:

- **The Read Field**, beside The Unit Field: the form
  `# Read: <page or table>, <date>, <reader>`; the scope from L-322
  ruling (b); Tony's ruling of section 2, in his words; the three
  branches (builder can open, only Tony can, nobody can); and that a
  model's line names the model.
- **Rule 8's enumeration sentence** names both routes to a derived row:
  its arithmetic and its `# Derived:` line.
- **The Unit Field** points at `constants_tokens.py` and names the
  retired list and the "named number" marker.
- **The worksheet schema column** saying whether a verdict is Tony's or
  a model's, promised on 2026-09-11.

Bring Tony the exact wording of The Read Field before cutting the
patch. It is his ruling being written down.

**The session ends here.** A reinstall cannot be verified from inside
the session that makes it. Stage C is a NEW session, and its first act
is confirming its loaded copy reads 2.14.

## 6. Stage C -- the walk (orrery, then gallery)

**Per row, one visit, in this order.** `# Unit:` with a token from
`constants_tokens.py`. `# Status:` in the form the skill gives.
`# Figures:` by Rules 1 to 3, with a typed number's trailing zeros
settled from the source in words. `# Derived:` on every expression,
going back to the measured primaries (Rule 4). `# Read:` where the row
is in scope. The comment lines already on the row are kept; this adds
fields, it does not rewrite notes, except where a note states something
now false.

**Two pushes, so each can be reviewed.**

- **C1: the 29 rows with no fields**, plus `KM_PER_AU` and `GM_SUN_SI`
  as inputs. Those two belong to no body's slice; visit them now and
  say so on the rows.
- **C2: the 28 magnetosphere rows.** Figures and read lines; the five
  `dimensionless` rows get real tokens; the two standoffs revert to
  expressions and leave `TRANSITIONAL`, and the three places in
  `constants_new.py` that say `test_derived_figures.py` recomputes
  them are corrected. Before reverting, confirm by grep that nothing in
  the gallery still parses those two rows out of the store. Then
  `CLOSED_SLICES = ("EARTH",)`.

**The reading.** For each in-scope measured row, try to open the source
under the Access Standard. Record what happened in ONE file,
`documentation/L322_earth_read_record_<date>.md`, a row per constant:
what was opened (title as printed), where in it, what it says, and the
verdict. Rows the builder could not open go in a second section of the
same file, "For Tony to read", each with the link, where to look, and
the number he should expect to see. Do not put that list in chat. Tony
answers from the file; his lines are written with his name and the
date he read.

**A row that fails is a finding, not a blocker for the others.** A
value that disagrees with its source, a citation nobody can open, a
unit check that fails on the arithmetic: fix what is method (rewriting
the Hill sphere's conversion so the factor is not counted twice is
method), and bring Tony only what changes a drawn value. Any change to
a number that a room draws is visitor-visible and is Tony's to see
first.

**After each orrery push, the gallery follows.** Pull the export, run
the config mirror, run the cache builder with OneDrive syncing paused,
run the gallery maintenance run, commit config and cache TOGETHER,
push. Served numbers will now be rounded to their declared figures, so
some hovers may show fewer digits than before. Tell Tony which, by
name, before he looks at the rooms on his phone.

**Done when:** with `CLOSED_SLICES = ("EARTH",)`, the orrery
maintenance run passes and the three constants checkers judge every
Earth row instead of listing it as not yet migrated; each checker has
been made to fail once on purpose on an Earth row and named it; the
gallery run passes with "Cache in step" green; the count of links still
going through the old drift check has dropped, and you tell Tony from
what to what, naming the Earth links that remain if any.

## 7. Stage D -- Earth's pole moves into the store

L-322 ruling (a): the pole orientation served for Earth lives in
`idealized_orbits.py` as `planet_poles['Earth']`, outside the store,
and moves in during Earth's slice. It draws a closed room's axis, so
it is its own push with the smoke suites run before and after and a
phone check by Tony. Tony's words on the risk: "migrating constants
into the store always carries some risk, but it is manageable and
necessary to have a single source of truth." The Sun's, Jupiter's and
Saturn's poles and the galactic tide default wait for their own slices.

## 8. Out of scope

- The Sun's slice and every other body's. Note that slice membership is
  read from the name up to the first underscore, which works for Earth
  and will not for the Sun.
- Retiring the old drift check, the suffix reader and `SCALAR_UNITS`.
  That patch is owed when no link is left for it to examine, and the
  Sun's links will still be there.
- Building the fix for the Arrival check. Stage A records it.
- L-325's decide (close as superseded, or leave open until the
  standoffs revert). C2 reverts them, so raise it with Tony then.
- Any new constant. The audit is bounded by what the orrery renders.

## 9. Rules of delivery

- A patch is run from its repository's ROOT and filed in
  `documentation/` AFTER it has run. Say this to Tony each time.
- After every push, read the pushed tree for what the patch should have
  changed. Read both remotes and name which SHA is which; two were
  transposed last session.
- One ledger patch per pushed HEAD.
- A patch that changes `constants_new.py` fingerprints it and refuses
  on a mismatch. Line endings are kept as found. ASCII throughout.
- Every checker result you report says how many rows it examined and
  names the ones it could not judge.
- Stamp your files with your own model name.
- If anything in section 3 has moved when you look, stop and say so.

## 10. Tony's decisions, and when they fall due

1. **(approve, stage B)** The wording of The Read Field.
2. **(read, stage C)** The rows on "For Tony to read", from the file.
3. **(look, after each gallery push)** Both rooms on the phone.
4. **(decide, end of C2)** L-325.
5. **(look, stage D)** Earth's axis after the pole moves.

## 11. Tony-action rollup

1. **(do)** File this manifest and
   `HANDOFF_L334_editor_built_20260919.md` in the orrery's
   `documentation/`, commit, push. Give Opus this file and both SHAs,
   saying which is which.
2. **(do)** At each stage: run the patch from the ROOT of the
   repository it names, move it to `documentation/`, run that
   repository's maintenance run, commit, push, report the SHA.
3. **(do)** After stage B, reinstall provenance-discipline 2.14 and
   start a new session for stage C.
4. **(do)** Pause OneDrive syncing before every cache build.

---

Written September 19, 2026 with Anthropic's Claude Fable 5.1.
