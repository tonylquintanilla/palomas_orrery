# Build Manifest -- L-322, the mechanism (units, figures, export, checks)

**Built on `6f124a79d828f99ccb760c4158742f2240024825`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
HEAD verified live at the time of writing. One ledger-only patch
(`patch_L322_3_design_round_ledger_20260916.py`) is pending on Tony's
machine; it changes no file this manifest builds on. Gallery at
`72a49552aa6ba4b21c2f58e3c5fe53f7d198590c` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.**

**Type: BUILD CONTRACT.** Written before the build, zero code. It says
what gets built, in what order, what each piece reads and writes, and
what makes each check fail. The session that builds it reads this
first, then the rulings it cites, and raises any disagreement between
the two rather than resolving it silently.

**Continues from** `documentation/HANDOFF_L322_design_round_20260916.md`
and `documentation/DESIGN_L322_d_significant_figures_20260916.md`.
Rulings: L-322 (nine of 2026-09-11, the slicing and token rulings of
2026-09-14, the four of 2026-09-16), L-335, L-325 (withdrawn).

**Prepared:** September 16, 2026 by Claude Fable 5.1, Tony Quintanilla
integrator.

**Skill obligation carried in.** The build session confirms
provenance-discipline reads **2.13** at load before any of this. The
skills this build fires: provenance-discipline (the store), safe-file-
editing (every patch), agentic-pre-test (every delivered file),
ledger-and-session-records (the as-built), gallery-cache-builder
(piece 6), interactive-exhibit (piece 6's hover formatting).

---

## 1. What is being built, in one paragraph

The orrery becomes the PRODUCER of its constants and the gallery a
CONSUMER that never reads orrery source. A new generator exports the
whole store as one JSON file, each row carrying its value rounded to
its declared figures, its unit token and its figure count, plus a
token table saying what each unit token means and a hash of the store
bytes it was made from. Three orrery checkers read that: one confirms
the export is not stale, one confirms every derived row's unit follows
from its inputs (astropy, inside the check), and the derived-figures
checker is rewritten to judge the declaration. On the gallery side a
generator pulls the export at a recorded orrery SHA, the nightly cache
builder fills every served number from it by name, and the hand-copied
values in `data/objects_config.json` retire. The store itself is walked
afterwards, Earth first, one visit per row; that walk is NOT this
manifest.

## 2. What is NOT in this manifest

- The Earth-slice walk of the store (53 rows; `# Unit:`, `# Status:`,
  `# Figures:`, `# Read:`). It follows this build and is its own
  session. Nothing here needs it, because every check reports rows it
  cannot judge by name instead of assuming them.
- Moving the five outside-store values (`planet_poles` x4, the tide
  radius) into the store. That is the Sun and Earth slices' work; piece
  6 reports them NOT IN STORE by name until then, as today.
- L-334, the store editor. It reads what piece 6 serves.
- Retiring `dimensionless` from the five rows that declare it. That
  is a slice edit; piece 4's token table simply has no entry for it,
  so those five rows report UNKNOWN TOKEN by name until they are
  visited.

## 3. Deliverables, in build order

| # | File | Repo | Kind | Depends on |
|---|---|---|---|---|
| 1 | `constants_tokens.py` | orrery | NEW module: the token table | -- |
| 2 | `export_constants.py` | orrery | NEW generator: writes `data/constants_export.json` | 1 |
| 3 | `test_constants_export.py` | orrery | NEW checker: export freshness and shape | 2 |
| 4 | `test_dimensions.py` | orrery | NEW checker: dimensional analysis of derived rows | 1 |
| 5 | `test_derived_figures.py` | orrery | REWRITE to Rule 8 | 1 |
| 6a | `gallery_maintenance_run.py` | gallery | patch: pull generator + two new live checks; retire the suffix reader and `SCALAR_UNITS` | 2 |
| 6b | `tools/gallery_cache_builder.py` | gallery | patch: fill served numbers from the export by name | 6a |
| 6c | `interactive.html` | gallery | patch: hover formats to the served `figures` | 6b |
| 7 | `orrery_maintenance_run.py`, `palomas_orrery_dashboard.py` | orrery | patch: wire 2, 3, 4 | 2, 3, 4 |

Pieces 1 to 5 and 7 are one orrery session. Piece 6 is a gallery
session and can follow later; nothing in 1 to 5 waits on it. Each piece
is delivered with its patch script (safe-file-editing Format A) and
passes the agentic pre-test on a throwaway copy before Tony sees it.

## 4. Piece 1 -- `constants_tokens.py`, the token table

**Ruling it implements.** 2026-09-14: one entry per token, in the
orrery, carried by the export; each token declares its dimension and,
where it has one, its factor. It REPLACES the gallery's `SCALAR_UNITS`
and suffix reader rather than adding to them. `dimensionless` is not a
token.

**Shape.** A plain dict, no imports from the store:

    TOKENS = {
        "km":      {"dimension": "km",         "defining_constant": None},
        "au":      {"dimension": "au",         "defining_constant": "KM_PER_AU"},
        "r_earth": {"dimension": "km",         "defining_constant": "EARTH_EQUATORIAL_RADIUS_KM"},
        "r_sun":   {"dimension": "km",         "defining_constant": "SUN_RADIUS_KM"},
        "deg":     {"dimension": "deg",        "defining_constant": None},
        "nt":      {"dimension": "nT",         "defining_constant": None},
        "per_nt":  {"dimension": "1/nT",       "defining_constant": None},
        "npa":     {"dimension": "nPa",        "defining_constant": None},
        "km_s":    {"dimension": "km/s",       "defining_constant": None},
        "l_shell": {"dimension": "l_shell",    "defining_constant": None},
        ...
    }

`dimension` is an astropy unit string, or the token's own name for a
named quantity with no dimension (`l_shell`), which piece 4 defines as
an irreducible unit so it compares with nothing. `defining_constant`
names the store row whose value is one of this token in the dimension's
base unit: one `r_earth` is `EARTH_EQUATORIAL_RADIUS_KM` km. The factor
is never typed in this file; piece 4 reads it from the store by name.

**Tokens to define at first build.** The eight the store uses today
(`deg`, `km_s`, `l_shell`, `npa`, `nt`, `per_nt`, `r_earth`, and
`dimensionless` NOT defined), plus the ones the suffix reader knew
(`km`, `au`, `r_sun`) and the ones the two dicts need (`days` for
`KNOWN_ORBITAL_PERIODS`, `k` for `spectral_subclass_temps`). A token the
store declares that the table lacks is a FAIL in piece 4, by name, so
the table grows by failing rather than by guessing.

**What makes it wrong.** A token whose `defining_constant` is not a
store name (piece 3 checks this at export); a dimension string astropy
cannot parse (piece 4 checks at import).

## 5. Piece 2 -- `export_constants.py`, the sixth generator

**Rulings.** 6 (the orrery exports; the gallery does not parse
source), 7 (the runner keeps it current), Fable review (export the
WHOLE store, not the pointed-at subset), Rule 6 of 2.13 (the export is
the reporting step: it rounds).

**Reads.** `constants_new.py` as bytes (for the hash) and as a module
(for values); the row blocks (the `blocks()` parser from
`test_derived_figures.py`, moved into a small shared reader,
`constants_rows.py`, so three checkers stop carrying three copies);
`constants_tokens.py`.

**Writes.** `data/constants_export.json`:

    {
      "generated": "2026-09-17T02:14:00Z",
      "orrery_sha": "<git HEAD at generation, or 'unpushed' if the working copy is dirty>",
      "store_sha256": "<sha256 of constants_new.py bytes>",
      "tokens": { ... piece 1, verbatim ... },
      "rows": {
        "EARTH_INNER_CORE_KM": {
          "value": 1221.5, "unit": "km", "figures": 5,
          "status": "measured V_SOURCED 2026-09-12", "derived": false
        },
        "EARTH_INNER_CORE_RADII": {
          "value": 0.19151, "unit": "r_earth", "figures": 5,
          "status": null, "derived": true
        },
        "LIGHT_MINUTES_PER_AU": {
          "value": 8.316746326444, "unit": "min", "figures": "exact", ...
        },
        ...
      },
      "not_exported": {
        "EARTH_LOWER_MANTLE_KM": "no # Unit: line",
        ...
      }
    }

**Rounding, per Rule 5 and 6.** `value` is `float("%.*g" % (figures,
raw))` when `figures` is an integer; the raw float when `figures` is
`exact`; and the raw float with `"figures": null` when the row has no
`# Figures:` line yet, so a consumer can tell a declared count from a
missing one. Nothing is rounded at rest; the store is untouched.

**A row with no `# Unit:` line is NOT exported.** It goes in
`not_exported` with the reason, by name. This is the per-slice gate of
2026-09-14 seen from the export: the gallery cannot join to a row that
has not been migrated, and it says so by name (piece 6b), instead of
serving a number with no unit. Today that is 82 of 110 rows; the count
falls with each slice.

**Dicts.** `KNOWN_ORBITAL_PERIODS` and `spectral_subclass_temps` export
as one row each with `"value"` a dict, the dict-level `# Unit:` line
applying to every entry. `planet_poles`, once moved (out of scope
here), follows the same shape.

**What makes it fail.** Any token in a `# Unit:` line that piece 1 does
not define (FAIL, by name); any `defining_constant` that is not a store
name (FAIL); `# Figures:` that is neither an integer nor `exact`
(FAIL, by name). The generator exits non-zero and writes nothing; the
runner shows it red.

## 6. Piece 3 -- `test_constants_export.py`, freshness and shape

**Ruling.** The Fable review's framing correction: the round trip is
TWO hops, and this is the orrery hop -- the export says what the store
holds.

**Checks, each printing what it compared.**

1. `store_sha256` in the export equals the sha256 of
   `constants_new.py` on disk. Prints both hashes. FAIL on mismatch:
   the store moved and the generator did not run. (The runner runs
   generators first, so a maintenance run cannot show this red except
   when the generator itself failed; a dashboard run of this test
   alone can.)
2. Every `rows` entry re-reads: value, unit and figures from the
   current store agree with the file. Prints the count examined and
   names any disagreement.
3. `not_exported` names exactly the rows on disk with no `# Unit:`
   line, no more and no fewer. Prints the count.
4. Every `defining_constant` in `tokens` resolves to a row.

**What makes it fail.** Any of the four. A green run prints the hash
compared, the row count and the not-exported count, so "did it run" is
answered by the output (A Check That Cannot Fail).

## 7. Piece 4 -- `test_dimensions.py`, dimensional analysis

**Rulings.** 4 (dimensional analysis is the real check on a unit
assignment, as its own check in a maintenance runner), 2026-09-16
(astropy inside the check, floats in the store; the orrery runner).

**Scope.** DERIVED rows only -- rows whose right-hand side is an
expression, found by the row reader, not by a Status word. A bare
literal asserts its unit and nothing in the file can contradict it;
those rows are listed as NOT CHECKABLE with the count, and that is the
correct result for them, not a gap.

**Method.** For each derived row: read its expression text; build a
namespace in which every store name it uses is an astropy Quantity
(the store's float times the token's unit, built from piece 1 with
`def_unit`, `l_shell` irreducible) and `np`/`math` functions are
available; evaluate; compare the result's unit to the row's declared
token. Measured this session on astropy 8.0.1:
`nT * per_nt` decomposes to dimensionless inside a `tanh`; `l_shell`
refuses conversion to dimensionless with `UnitConversionError`; the
Shue expression evaluates to `r_earth` when the pressure ratio is
dimensionless.

**Two hand rules the check must carry, because no unit algebra
carries them.**

- **Division by a defining constant is a conversion.**
  `EARTH_INNER_CORE_KM / EARTH_EQUATORIAL_RADIUS_KM` is km/km to
  astropy and `r_earth` to the store. Rule: when the expression divides
  by a row that is some token's `defining_constant`, the check treats
  the result as converted INTO that token (`Quantity.to(token)` on the
  numerator). Measured: `(1221.5 km).to(r_earth) = 0.19151 r_earth`.
- **A non-integer power is taken on the number in the paper's unit.**
  Shue's `Dp ** (-1/a5)` and Jelinek's `p ** (-1/eps)` are empirical
  fits whose coefficients absorb the unit; astropy would return
  `r_earth * npa^-0.15`. Rule: the base of a non-integer power is
  divided by one unit of its declared token before the power is taken,
  and the row's `# Derived:` line says so in words. Two rows today.

**Report.** Per derived row: `OK <name> <declared> == <computed>`,
`MISMATCH <name> declares <token>, expression gives <unit>`,
`UNKNOWN TOKEN <name> <token>` (not in piece 1), `NO UNIT <name>` (no
`# Unit:` line, expected until the row's slice visit -- counted, named,
FAIL only inside a closed slice). Then the counts, and the list of
bare-literal rows as NOT CHECKABLE.

**What makes it fail.** A MISMATCH anywhere; an UNKNOWN TOKEN anywhere;
a NO UNIT inside a closed slice. The closed-slice list is one constant
in the file, `CLOSED_SLICES = ()` at first build, gaining `"EARTH"`
when the Earth walk finishes; a row's slice is its name prefix.

**Expected first run at 6f124a79.** 27 `# Derived:` rows. 21 are
expressions and none of them has a `# Unit:` line yet, so all 21 report
NO UNIT. 6 are literals and report NOT CHECKABLE: the two transitional
standoffs (their expressions live only in their `# Derived:` lines until
they revert), the cut angle, and three older literals. Zero MISMATCH is
possible today only because nothing is checkable yet; the first real
verdicts arrive with the Earth slice. If a MISMATCH appears then, it is
a finding, not the checker.

## 8. Piece 5 -- `test_derived_figures.py`, rewritten to Rule 8

**Rulings.** L-325 withdrawn; Rule 8 of 2.13.

**What changes.** The `DERIVATIONS` formula table goes: with the store
holding expressions, Python already recomputes each row from its
inputs, so the checker no longer recomputes anything. Enumeration is by
the `# Derived:` line, not by a Status word. Per derived row it checks:

1. the row has a `# Figures:` line (else NOT YET MIGRATED, by name);
2. every input the line names appears in the expression text;
3. the declared count does not exceed the least count among the named
   inputs whose own `# Figures:` is an integer (exact and declared
   inputs skipped) -- for a product or quotient; for a sum or
   difference the coarsest decimal place, read from the input
   literals;
4. the literal stated on the `# Derived:` line, where one is, equals
   the expression rounded to the declared count (`%.*g`), so the
   comment cannot drift from the arithmetic.

**Transitional rows.** The two magnetosphere literals stay literals
until piece 6b lands and the gallery stops parsing the store; the
checker knows them by name as TRANSITIONAL and applies checks 1 to 3
without check 4's recomputation. The list is one constant and the
docstring says why it exists and when it empties.

**Expected first run.** 27 rows, 0 with `# Figures:` today -> 27 NOT
YET MIGRATED, by name, exit 0 while `CLOSED_SLICES` is empty. That is
the honest state and it replaces "All 2 derived rows recompute".

## 9. Piece 6 -- the gallery consumes the export

**Rulings.** 6, 8 (the join is in the assembler, not mixed into
`objects_config.json`), and the two gallery checks named on L-322.

**6a. `gallery_maintenance_run.py`.** A new GENERATOR, `Constants
export pull`: reads orrery HEAD via the commits API (as
`check_store_drift` does today), fetches
`data/constants_export.json` at that SHA, writes it to the gallery's
`data/constants_export.json` and the SHA to
`data/constants_export.sha` beside it. Two new LIVE checks replacing
`Store drift`: `Export freshness` -- the served copy's bytes equal the
orrery's at the recorded SHA, printing the SHA compared against (cannot
go green by never resolving); `Pointer join` -- every
`orrery_constant` in `objects_config.json` resolves to a `rows` entry
BY NAME, and a pointer with no row FAILS, by name, saying whether the
row is absent or `not_exported`. The suffix reader (`UNIT_BY_SUFFIX`,
`unit_of_constant`), `SCALAR_UNITS`, `store_conversions` and the
per-value `judge` RETIRE: the hand copy's net comes down with the hand
copy. `patch_L322_mark_transitional.py`'s comments already say which
lines these are.

**6b. `tools/gallery_cache_builder.py`.** For every served entry
carrying `orrery_constant`, the builder fills `value`, `unit` and
`figures` from the export row by name at build time, and a missing row
is a `ValidationAbort` naming the pointer. Two phases, because the
hand copies are live on the public page: FIRST the builder fills from
the export and prints every place the export disagrees with the hand
copy (expect the two standoffs at four figures against sixteen, and the
`dimensionless`/`l_shell` rows); Tony reads that list; THEN a patch
deletes the hand-copied `value`/`unit` from every pointed entry in
`objects_config.json`, leaving the pointer, the source and the
presentation fields. The join is in the builder because the builder is
what writes `feature_configs.json`, which is what the page reads; that
is what ruling 8's "assembler" is in this pipeline.

**6c. `interactive.html`.** Wherever a served number is formatted for
a hover or the i-panel, the format uses the served `figures`
(`toPrecision(figures)`), falling back to today's fixed format when
`figures` is null. Rule 7: never more figures than the row declares;
fewer is a display choice.

**What makes 6 fail.** Export freshness: a byte difference at the
recorded SHA, or the SHA not resolving. Pointer join: any pointer with
no row. Builder: any pointer with no row aborts the build. The Mode 5
check owed after 6b/6c: both rooms on the phone, every number the same
as before except the ones the disagreement list named.

## 10. Piece 7 -- wiring

`orrery_maintenance_run.py`: `Constants export` joins GENERATORS
(after Skill manifest, before Module atlas, since the atlas indexes the
new modules); `Constants export check` and `Dimensions` join CHECKERS
beside `Derived figures`, all gating. `palomas_orrery_dashboard.py`:
one button each, on Tony's standing instruction that a new test gets
both. The runner's docstring and the dashboard's gain the L-322 stamp.

## 11. Order of landing, and why

1 -> 2 -> 3, then 4 and 5 (independent of each other), then 7, in one
orrery session with one commit. Piece 6 in a following gallery session.
The Earth-slice walk after both. The token table comes first because
everything reads it; the export before its checker because a checker
with nothing to check is a check that cannot fail; the gallery last
because until the export exists the gallery has nothing to consume, and
today's `Store drift` keeps working meanwhile (ruling 3: do not turn
the old check off before the new one is on).

## 12. Verification the build session owes

- Agentic pre-test on every delivered file, on a throwaway copy of the
  pushed tree: `py_compile`, the runner's full maintenance run, each new
  checker run alone with its output read, not just its exit code.
- The expected first-run numbers in sections 7 and 8, measured, not
  assumed; a difference is a finding to record, not to explain away.
- `git ls-remote` after Tony's push; the as-built handoff anchored
  there.
- The Tier-1 gate: this build adds no display strings and no
  constants, so the scanner's active-path count should not move.

## 13. Decisions taken in this manifest that are method, not rulings

Named so the build session can overturn them without a ruling if the
code disagrees: the export file's path and field names (section 5);
the shared row reader `constants_rows.py`; `CLOSED_SLICES` as a
constant in the checkers rather than a file; the gallery pull as a
generator rather than a hand copy; the two-phase retirement of the
hand copies in 6b. None of these change what Tony ruled.

## 14. Numbers this manifest rests on, measured at 6f124a79 / 72a49552

110 store assignments; 28 `# Unit:` lines across 8 tokens (13
`r_earth`, 5 `dimensionless`, 3 `deg`, 2 `nt`, 2 `per_nt`, 1 each
`npa`, `km_s`, `l_shell`); 30 Status lines, 80 rows without; 27
`# Derived:` rows (21 expressions, 4 literals without Status, 2
transitional literals); 0 `# Figures:` lines; 70 served pointers, 65
resolving to the store, 5 outside it; `objects_config.json` unit
strings `au`, `deg`, `dimensionless`, `km`, `l_shell`; astropy 8.0.1
in the sandbox, already imported by 22 orrery modules.
