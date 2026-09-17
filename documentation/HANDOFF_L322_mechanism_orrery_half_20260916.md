# L-322's mechanism, orrery half: the export, the unit table and three checkers

Built on orrery `6b282b2e4f1223a83f0d71145c60cdda5cd10094`
at https://github.com/tonylquintanilla/palomas_orrery
Gallery at `72a49552aa6ba4b21c2f58e3c5fe53f7d198590c`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
Pushed at: the orrery SHA Tony reports after the rollup below. The
gallery does not move in this session.

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-16, late evening
Type: BUILD. One patch script, tested in the sandbox; nothing pushed by
Claude.
Handles: L-322 (orrery half built; gallery half and store slices
remain), L-325 (a line recording that its re-homed rewrite landed; the
decide is unchanged).
Companion: `documentation/BUILD_MANIFEST_L322_mechanism_20260916.md`,
the contract this session built from. Supersedes
`HANDOFF_L322_design_round_20260916.md`'s STILL OPEN item 1 and its
rollup item 6; everything else in it stands.

---

## STEP 0 -- for the next session, before anything else

1. `git ls-remote` both repositories. Expect the gallery at `72a49552`
   and the orrery at the SHA Tony reports.
2. Confirm `data/constants_export.json` is in the orrery at that SHA
   (raw fetch). The gallery half pulls it; if it is absent, the push
   did not include it, and nothing in the gallery session can start.
3. Version-check the skills the gallery half fires, at load, against
   the manifest: gallery-cache-builder 1.4, interactive-exhibit 1.3,
   provenance-discipline 2.13, safe-file-editing 1.11. This session's
   loaded copies matched all of them, and also read
   orrery-coding-conventions 1.9 and gallery-assembler 1.3, which
   discharges the obligation v3.60 carried.
4. `ledger_index.py` twice: `OK: 330`.

---

## WHAT WAS BUILT

One patch script, `patch_L322_4_mechanism_20260916.py`, all or nothing.
It does not touch `constants_new.py`.

**Five new files.**

- `constants_tokens.py` -- the table saying what each `# Unit:` name
  means. Twelve names: km, au, r_earth, r_sun, deg, nt, per_nt, npa,
  km_s, l_shell, days, k. Each has a dimension that astropy (the
  units library) can read. For au, r_earth and r_sun it also names
  the store row that defines one of that unit. `dimensionless` is kept
  in a separate RETIRED list, with the reason it retired. It replaces
  the gallery's `SCALAR_UNITS` and suffix reader, which retire in the
  gallery half.
- `constants_rows.py` -- one shared reader of the constants file,
  using Python's own parser. It also holds two short lists every
  checker needs: CLOSED_SLICES (empty until the Earth walk finishes)
  and TRANSITIONAL (the two magnetosphere standoffs).
- `export_constants.py` -- writes `data/constants_export.json`. Each
  exported row carries its value rounded to its declared figures, its
  unit, its figure count, its status, and whether it is derived. It also
  carries the unit table and the store's hash. Every row not exported is
  named with the reason.
- `test_constants_export.py` -- checks the export against the store:
  the hash, every row, the not-exported list, the defining rows, and
  the closed-slice rule.
- `test_dimensions.py` -- checks each derived row's unit against its
  arithmetic, using astropy inside the check. It compares both the
  dimension and the size, and carries the manifest's two hand rules.

**One rewritten file.** `test_derived_figures.py` now follows Rule 8
of provenance-discipline 2.13. It checks that no derived row declares
more significant figures than its inputs support, working through the
arithmetic by the textbook rules. It also checks that the row's comment
does not state more figures than it declares. The old formula table is
gone.

**Wiring.** The maintenance runner gains one generator (Constants
export) and two checkers (Constants export check, Dimensions). The
dashboard gains the matching three buttons, kept in alphabetical order,
and a new description for Test Derived Figures. The runner's own
description said four generators and eleven pass/fail checkers; that
was stale, and it now says six and sixteen.

**Built-in test rows.** Both new checkers first run a small built-in
set of made-up rows: 13 for the unit checker, 22 for the figures
checker. Every verdict must come out as expected, including a gap that
fails inside a finished slice. Today every real verdict is "not yet
migrated", so without these a pass would prove nothing. On their first
run they caught three bugs in the checker code:
- "km" and "deg" were being treated as pure numbers;
- astropy refused a hyperbolic tangent of per-nanotesla times
  nanotesla;
- a summary blamed the export for rows that were only unfinished.

All three are fixed.

---

## WHERE THE BUILD DEPARTED FROM THE MANIFEST

All five are method, not rulings, and each is also written in the
module that carries it.

1. **Derived rows are found two ways, which gives 31, not 27.** Rows
   are found both by their arithmetic and by their `# Derived:` line.
   Four expressions have no `# Derived:` line of their own, and a
   checker looking only for the line would never see them:
   `EARTH_LEO_INNER_KM`, `EARTH_LEO_INNER_RADII`,
   `EARTH_STRATOPAUSE_RADII`, `CORE_AU`. They are reported as NO
   DERIVED LINE.
2. **`dimensionless` is listed as retired, not unknown.** As the
   manifest specified it, the export would have failed on every run
   because of the five rows still declaring it. Those rows are now
   named as waiting for their slice visit. Any OTHER unit name the
   table lacks still fails the run, so the table still grows by
   failing.
3. **Two changes to the unit table.** The unit `au` has dimension km,
   not au: its defining row is in kilometres, and "one au is
   149,597,870.7 au" reads wrong. A named pure number such as l_shell
   is marked "named number" instead of by its own name, because the
   own-name marker collided with km and deg.
4. **The export file carries no timestamp and no git SHA.** The same
   constants always give the same file, so a maintenance run with no
   store change writes nothing. A file cannot name the commit that
   contains it anyway. The gallery records the orrery SHA when it
   pulls.
5. **The export checker also applies the finished-slice rule.** Inside
   a finished slice, a row missing its unit, status or figure count
   fails; outside one it is only named. This follows Tony's
   2026-09-14 ruling, which covers every row, not only derived ones.

---

## VERIFIED VS CLAIMED

Verified in the sandbox, on a fresh copy of the orrery at `6b282b2e`,
in the order of the rollup below:

- **The patch run.** It printed nine `ok` lines and wrote files
  identical, byte for byte, to the tested build. A second run refused
  and wrote nothing.
- **The patch's refusals and edge cases.** It keeps Windows line
  endings where it finds them. It refuses, writing nothing, when an
  edited file has changed since `6b282b2e`. It still applies when only
  the ledger's generated index has changed.
- **Ledger index:** `OK: 330` on both runs.
- **Maintenance run:**
  - 16 of 16 pass/fail checkers passed; the unpatched baseline was 14
    of 14.
  - The provenance scanner's top tier stayed at 292, and it reports
    that no file's top-tier count rose.
  - Its total rose by 2, from two low-priority notes on internal
    settings in two new tools: the export format number (`SCHEMA`) and
    the unit checker's comparison tolerance (`REL_TOL`). Those two
    files also join the scanner's existing "domain coverage gap" list.
- **Second maintenance run:** the export was unchanged and not
  written.
- **Each new checker run alone** exited 0. The numbers at `6b282b2e`:
  - the export carries 23 of 112 rows and names the other 89 (5 still
    declaring `dimensionless`, 84 with no unit line);
  - the unit checker reads 31 derived rows: 25 with no unit, 6 that
    cannot be checked;
  - the figures checker reads the same 31, all not yet migrated, 4 of
    them with no `# Derived:` line.
- **With the Earth slice marked finished** on a throwaway copy, all
  three checkers failed and named the Earth rows.
- **Dashboard**, under a virtual display: all three new buttons are
  drawn, and their scripts exist.
- **Encoding:** every delivered file is ASCII with LF line endings.

The sandbox needed two workarounds that do not apply on Tony's machine.
The Windows colour name `SystemButtonFace` was swapped on the throwaway
copy only, following the agentic-pre-test skill. The repo's
requirements were installed so that the Reset completeness and Orbit
cache checkers could run.

Claimed and NOT verified here:

- That the run on Tony's Windows machine matches. Environment-dependent
  lines, such as the data inventory, will differ.
- The push itself.

---

## WHAT THE EARTH WALK WILL MEET

These come from a dry run on a throwaway copy, with plausible units
written onto the Earth rows. The extra unit names used there are NOT in
the table.

- **15 derived rows pass and 2 fail.** Both failures are properties of
  the arithmetic, not errors in the checker.
  - `EARTH_GEOSTATIONARY_RADIUS_KM`: if Earth's rotation rate is
    declared in radians per second, the cube root leaves "radians to
    the two-thirds" in the unit.
  - `EARTH_HILL_SPHERE_KM`: the typed `1.0e-9` that converts cubic
    metres to cubic kilometres is counted a second time once units are
    attached, a factor of 1,000.
- **The second failure is a class, not a single row.** The typed 1000s
  in `SPEED_OF_LIGHT_M_S` and `M_PER_AU`, the 60 in
  `LIGHT_MINUTES_PER_AU`, and the 365.25 x 86400 in
  `AU_PER_LIGHT_YEAR` have the same shape. The built-in test row
  `FIX_EMBEDDED` shows the verdict they will get in their slices.
- **The two standoffs pass** once their exponents get a "named number"
  unit. Both hand rules fire, and the row's line says so.
- **A likely figures finding.** `EARTH_D660_DEPTH_KM`'s source line
  says two significant figures. `EARTH_LOWER_MANTLE_KM`'s `# Derived:`
  line treats 660 as good to units. Once figure counts are written, the
  checker will report that as OVER-DECLARED; built-in test row
  `FIX_DIFF` is exactly this case.
- **The Earth slice is 57 rows, not 53.** That is the count of rows
  whose names start with EARTH_ at `6b282b2e`; the design-round
  handoff carried an older number.
- **What slice membership needs later.** Membership is read from the
  name up to the first underscore. That works for Earth. The Sun slice
  will need an explicit list, because its rows start with SUN_, SOLAR_,
  CORE_, RADIATIVE_, CHROMOSPHERE_ and others.

---

## STILL SAYS SOMETHING FALSE, and why it was left

`constants_new.py` still says that `test_derived_figures.py`
recomputes the two standoffs and fails when the rounding stops holding.
That is no longer true. The statement appears in three places: the
module description's L-325 paragraph, and the Notes of
`EARTH_MAGNETOPAUSE_STANDOFF_RADII` and
`EARTH_BOW_SHOCK_STANDOFF_RADII`. The store was not a target of this
build. The Earth-slice visit that turns both rows back into expressions
rewrites those Notes. The patch prints this reminder when it runs.

---

## THE LESSONS

**The built-in test rows paid for themselves on the first run.** A
checker whose every real verdict is "not yet migrated" passes whether
or not its logic works. The three bugs above would all have waited for
the Earth walk and shown up there as confusing verdicts on real rows.

**A stamp copied from a handoff can carry the wrong model.** This
session first stamped its files with "Claude Fable 5.1", the previous
session's model, taken from that session's handoff. It was corrected
to Claude Opus 5 before delivery. The stamp is provenance, so it has to
name the model that actually made the change.

---

## STILL OPEN, in Tony's order (as of 2026-09-16, late evening)

1. **L-322, the gallery half** (piece 6 of the manifest), in the
   gallery repo:
   - pull the export at a recorded orrery SHA;
   - replace the Store drift check with Export freshness and Pointer
     join;
   - have the nightly builder fill served numbers from the export by
     name, in two phases (first print where the export and the
     hand-copied values disagree, then delete the hand copies);
   - format hovers to the served figure count;
   - retire the suffix reader and `SCALAR_UNITS`.
2. **L-322, the Earth slice.** Visit each EARTH_ row once, writing
   `# Unit:`, `# Status:`, `# Figures:` and, where a person has read
   the source, `# Read:`. The two standoffs revert to expressions and
   leave TRANSITIONAL. CLOSED_SLICES becomes ("EARTH",). This follows
   the gallery half, because the standoffs can only revert once the
   gallery stops parsing the store.
3. **L-334, the editor**, and the items the design-round handoff
   carried (L-331's residue, L-333, L-330, L-231, L-273's gallery
   half, L-061): unchanged.
4. **For provenance-discipline 2.14**, beside the worksheet schema
   column promised on 2026-09-11:
   - Rule 8's enumeration sentence should name both routes, arithmetic
     and `# Derived:` line;
   - The Unit Field could point at `constants_tokens.py` and name the
     retired list and the "named number" marker.

---

## TONY-ACTION ROLLUP

1. **(do)** Save `patch_L322_4_mechanism_20260916.py` in the orrery
   repo root, beside `constants_new.py`. Open it in VS Code and click
   Run. Expect nine lines starting with `ok`, then `patch applied`. If
   it prints `ERROR` or `ANCHOR FAIL`, nothing was written; paste the
   output here.
2. **(do)** Move the patch script into `documentation/`. Do this
   BEFORE step 4, so the generated documents do not count the script
   as a module.
3. **(do)** Run `ledger_index.py` twice. Expect `OK: 330` both times.
4. **(do)** Run `orrery_maintenance_run.py`. Expect:
   - "Constants export ... rewrote data/constants_export.json";
   - "16 of 16 gating checkers passed";
   - "292 TIER-1 FINDINGS".

   If the Dimensions row fails saying astropy is not installed, install
   it; it is already in `requirements.txt`. Paste the summary block
   here either way.
5. **(do)** File this handoff in `documentation/`.
6. **(do)** Commit and push. The commit must include the new
   `data/constants_export.json` and the five new modules; GitHub
   Desktop lists them as new files. Report the SHA.
7. **(decide)** L-325: close it as SUPERSEDED by L-322 now, or leave it
   OPEN until its two literal rows revert. Carried unchanged.
8. Next session: STEP 0 above, then the gallery half.

---

Session written September 2026 with Anthropic's Claude Opus 5.
