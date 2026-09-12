# Review request -- a build, before it is run

Built on orrery `a4ead59ac3f3f390710c99c4e3687d60b444447c`
at https://github.com/tonylquintanilla/palomas_orrery
The gallery repo is at `1f44673faf2acd32340bfdd4b524b6c8af5dd376` and is
NOT involved; nothing here is gallery-side.

Tony Quintanilla, PE | request written by Claude Opus 5 | 2026-09-12
Type: BUILD REVIEW REQUEST (Mode 7, cooperative). Zero code wanted back.
Origin: L-305 Gap item 4, plus the checker ruled in from your reply of
the same date (`documentation/REVIEW_REPLY_declared_values_and_the_gate_20260912.md`).

**The patch has NOT been run.** Both scripts are committed at the SHA
above so you can read them, and they sit unrun in Tony's working copy.
This review happens before the button is pressed, which is the whole
point of asking.

## Before you start -- the rules this task runs under

Fetch these at the orrery SHA above and read them before answering:

- `PROJECT_INSTRUCTIONS.md` -- A Check That Cannot Fail Is Not Passing,
  A Report Names Its Items, Fetched vs Recalled Convention, Show the
  Envelope of the Unknowable, Verify Execution Not Appearance, The
  Braid, Check All Parallel Pipelines.
- `skills/provenance-discipline/SKILL.md` -- The Status Line, Measured
  Is the Goal and Declared Is the Fallback, A Drawing Approximation Does
  Not Promote, The Store Carries the Verified Figure, Report to the
  Figures You Have, One Value One Home, A Breadcrumb Must Not Cite.
- `skills/safe-file-editing/SKILL.md` -- the patch script contract:
  fingerprints, transactional multi-file edits, the encoding gate,
  stamping, and A Guard Must Not Fence What a Generator Rewrites.
- `skills/orrery-coding-conventions/SKILL.md` -- hover text conventions.

**State in your reply which of those four you actually read.** A reply
that does not name them is telling us it did not read them.

## What to read in the code, all at the SHA above

- `patch_L305_magnetosphere_constants.py` -- the build. It carries the
  entire new constants block as a string literal, so reading the script
  IS reading the change.
- `test_status_lines.py` -- the checker the patch wires into the
  maintenance run.
- `constants_new.py` -- the two rows being superseded sit at 315 and
  326; `RADIATIVE_ZONE_AU` at 637 is touched in passing.
- `earth_visualization_shells.py` lines 720-860 -- the hovers whose
  format specifiers change, and the geometry that reads the two
  standoffs at 751 and 825.
- `shell_configs.py` -- the Earth `magnetosphere.tooltip` block near
  2290, which is the twin of the hover in the shells file.

The code is polished and that says nothing about the author's fluency.
Tony Quintanilla is a retired civil and environmental engineer with sole
commit authority, not a professional programmer; this codebase is two
years of AI collaboration. Unpack jargon on first use. Write for him.

## What the build does

Four files, all or nothing.

**`constants_new.py`.** Fifteen new rows: Shue et al. (1998)'s eight
magnetopause coefficients, Jelinek et al. (2012)'s three bow shock
parameters, a bow shock cut angle, and three declared solar wind
conditions. Both standoffs superseded --
`EARTH_MAGNETOPAUSE_STANDOFF_RADII` from a typed 10.0 to a typed
10.251872972379905, and `EARTH_BOW_SHOCK_STANDOFF_RADII` from a typed
12.5 to an expression over the new constants. A Lugaz-midpoint
derivation, a Farris & Russell "Model form" citation and a stale
migration Note are removed. Every row written carries a `# Unit:` line
and a `# Status:` line.

**`earth_visualization_shells.py` and `shell_configs.py`.** Six hover
and tooltip quotes interpolate the two standoffs with `:g`, which prints
six significant figures. With the new values that reads 10.2519 and
13.5117; both store rows say to report 10.25 and 13.51. The specifier
becomes `:.4g`. No words change.

**`orrery_maintenance_run.py`.** One line adding the checker to the
CHECKERS list.

## What has already been measured, so you need not redo it

Run on a clone at `da6bcea1`, whose four target files are byte-identical
to the SHA above:

- The patch applies clean; all four files ASCII and compiling.
- `test_constants_provenance.py` 21/21, `test_cross_checked.py` 19/19,
  `test_citation_inheritance.py` 20/20, `test_provenance_1d.py` 27/27 --
  unchanged from before the patch.
- The checker reports 19 status lines, 0 malformed.
- Each of the checker's six failing rules was broken in turn on a
  throwaway copy and each fired with the right row and reason; the
  unmutated control passed.
- `constants_new.py` stays at 1 Tier-1 finding
  (`EARTH_SOLAR_WIND_BZ_NT`), which is expected: the scanner's window
  inference is L-322's, not this build's.
- The hover quotes render 10.25 and 13.51.

If you think a measurement is wrong, name it and say how you would
check it. Do not re-derive them.

## The questions

1. **The magnetopause literal.** Shue's standoff needs a hyperbolic
   tangent, and the gallery's store parser evaluates only + - * / and
   **, so an expression there would be dropped silently and the pointer
   would leave the drift check. It is therefore typed, at the full
   float value of the expression it would be, with a `# Derived:` block
   giving the arithmetic and the reporting figure. Is a seventeen-digit
   literal the honest form, or is this false precision at rest that The
   Store Carries the Verified Figure does not actually license?

2. **A derived constant inheriting from a declared pending one.** The
   bow shock standoff is written as
   `EARTH_BOW_SHOCK_JELINEK_R0_RADII * EARTH_SOLAR_WIND_PRESSURE_NPA **
   (-1.0 / EARTH_BOW_SHOCK_JELINEK_EPS)`. The pressure is `declared
   pending` against L-314. So a derived row inherits from a row that is
   backlog, and when the live feed lands the standoff moves with it. Is
   that the right coupling or a trap?

3. **Naming.** The coefficients use the paper's own Table 1 indices --
   `EARTH_MAGNETOPAUSE_SHUE_A1_RADII` and so on -- on the argument that
   a reader can go to row a1 and check. Five rows carry no unit suffix
   at all because they are dimensionless, and their `# Unit:` line says
   so. Is that readable English, or is the index notation opaque, and
   is there a naming choice here that is really naming-to-satisfy a
   machine?

4. **The cut angle.** Jelinek states a local-time envelope of plus or
   minus 7 hours. The store holds one row, 105 degrees, as `measured
   V_SOURCED`, with the 7 h times 15 deg/h conversion in a `# Derived:`
   line -- the same shape as `EARTH_GM_KM3_S2`, which converts the
   published m^3 s^-2 and stays one measured row. The alternative was
   to store the 7 hours and derive the angle. Which is right?

5. **The checker's tiers.** Six rules fail the run; two things are
   reported without failing (a status line with no ISO date, and the
   count of rows carrying no status line). The date is soft because the
   skill's own examples omit it. Is any failing rule too strict, is any
   reported item one that should gate, and is there a seventh rule the
   checker should have and does not?

6. **A rule of yours that was dropped, and why.** Your reply proposed
   that a `declared` row whose block also matches the citation patterns
   is a contradiction. `INNER_CORONA_RADII` disproves it: it is declared
   at 3 solar radii and cites the paper that states the convention. The
   source says where the convention comes from; it does not claim to
   measure the value. The check was dropped. Do you agree, or is there
   a narrower form worth keeping?

7. **`RADIATIVE_ZONE_AU`, fixed in passing.** Its existing status line
   read `measured` with no rung, which the grammar requires. The patch
   adds `V_SOURCED` and nothing else. But the row is
   `0.713 * SOLAR_RADIUS_AU` -- a sourced literal times a stored
   constant -- which by the grammar's letter looks like `derived`. The
   kind was left alone for L-322's walk. Is adding a rung to a kind that
   may be wrong better or worse than leaving the row malformed?

8. **The format specifier.** `:.4g` at six call sites carries the same
   figure count the store row states in prose. That is arguably a second
   store of one property, which is the failure One Value One Home names.
   The alternative -- a declared figure count read by the call sites --
   is exactly L-322's open question (d) and does not exist yet. Is
   `:.4g` the right interim, or does it entrench something?

9. **The interim render.** The drawn magnetopause moves from 10.0 to
   10.25 Earth radii and the bow shock from 12.5 to 13.51, because the
   existing shell code already reads both constants. So the desktop
   orrery's geometry changes when this lands, before the L-305 renderer
   port replaces those shapes entirely. Acceptable interim, or should
   the constants wait for the renderer?

10. **Check All Parallel Pipelines.** Two consumers were found by
    grepping: the hover strings and the drawn geometry. Was one missed?

## What we do NOT want back

- No patches, no diffs, no code. If something should change, say what
  and why.
- Do not propose ledger handles or write ledger blocks.
- Do not re-run or re-derive the measurements above.

Prose is fine, and disagreement is the point of asking. Where you think
the framing here is itself wrong, say that first.

Written September 2026 with Anthropic's Claude Opus 5.
