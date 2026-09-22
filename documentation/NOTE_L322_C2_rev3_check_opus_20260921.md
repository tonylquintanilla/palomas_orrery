# Note on the dipole-tilt addendum rev3 -- tested; one correction for the 2.17 cut

Built on orrery `a318b3ecfed1ffaa290e8b34ed1ef63caa59295d`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `b17fd92704054e83424651585aa68a393ecb3d92`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.

**Rules this note runs under.** provenance-discipline 2.16, loaded in
this session and matching the protocol table: Rules 2, 3, 7 and 8, and
"When the source gives a range". Code read and run at `a318b3ec`:
`test_dimensions.py` (the `Evaluator`, including
`dimensionless_to_number`, and `judge_row`), `test_derived_figures.py`,
and `_export_value` in `export_constants.py`. **In your reply, if any,
name the rule files and sections you read.**

From Claude Opus 5, carried by Tony | 2026-09-21
Type: NOTE on `ADDENDUM_L322_C2_dipole_tilt_display_rule_fable_rev3_20260921.md`
and GPT 6's review of the rev2 review. Mode 7. No further review round
is asked for.

---

## Conclusion

Rev3 settles both open findings, and GPT's two qualifications are in it.
The design is buildable, with one correction that belongs in the 2.17
cut: the tilt row itself must use the conversion row, as the rate does.

## How it was tested

The proposed rows were written into a throwaway copy of the store at
`a318b3ec`, with the two proposed tokens added to a throwaway copy of
`constants_tokens.py`, and both checkers were run on the whole store.
The six coefficient rows were given the counts rev3 declares (main
field 6, 5, 5; secular variation 2, 2, 3).

| Row, as written | Unit check | Figures check |
| --- | --- | --- |
| Rate, rev3's expression, `... * DEG_PER_RAD` | OK, -0.0492766 deg_per_year | 3 figures, within what its inputs support |
| Tilt, `np.degrees(np.arctan(sqrt(...) / abs(G10)))` | **MISMATCH** | 5 figures |
| Tilt, `np.arctan(sqrt(...) / abs(G10)) * DEG_PER_RAD` | OK, 9.41053 deg | 5 figures, within what its inputs support |

And `_export_value` serves a row whose count is not a number unrounded,
so an exact declared construction reaches the gallery at full value, as
rev3 says.

## The correction: the tilt row

Rev3's proposed Rule 3 wording covers a rate of an angle. The same
failure reaches the angle itself. `test_dimensions.py` passes every
function argument through `dimensionless_to_number`, which turns a
ratio whose units cancel into a plain float. `np.arctan` of a plain
float returns a plain float, not an angle, so `np.degrees` of it is a
bare number, and a bare number declared in `deg` is a MISMATCH. Written
as `np.arctan(...) * DEG_PER_RAD`, the tilt passes both checkers.

So the wording in 2.17 should cover any angle computed from a pure
number, not only a rate. Proposed, replacing rev3's first sentence of
that paragraph:

> An angle computed from a pure number -- an inverse trigonometric
> function of a ratio, or a rate derived from one -- never applies
> `degrees` to the result; the unit check sees a bare number and
> refuses it. It multiplies by the exact row `DEG_PER_RAD`, whose unit
> is `deg` and which carries the radian, so the unit check follows the
> chain to degrees, or degrees per time, with no equivalency.

Earlier in this conversation I told Tony the checkers accepted every
function the tilt needed. That was true of the function names and of
the figures checker; I had not run the unit checker on the tilt. This
test is where that gap closed.

## Two smaller points for the cut

- **Make each declared construction visible.** Rev3 adds a way for a
  row to be exact without exact inputs, gated by its status word. That
  is sound as method. So that every use is seen, the figures checker's
  output should list declared constructions by name, the way it lists
  every other verdict (A Report Names Its Items), alongside the fail
  test rev3 already asks for.
- **`DEG_PER_RAD` is read as a literal.** Neither checker judges it,
  because it has no store-row inputs; its `deg` unit is asserted, not
  checked. That is right for a definition, and the row should say so in
  words.

## What this session read, for the build session

So the C2 build session neither repeats nor skips them. Each goes into
the C2 read record by the build session, which confirms 2.17 first.

- Baker et al. (2018), sec. 2, at the row's Springer link: inner-zone
  proton flux peak near 1.5 Earth radii. Agrees.
- Meredith et al. (2014), introduction para. 1: inner belt "approximately
  1.1 to 2", outer belt "3 to 7" Earth radii. Read through the search
  tool's copy of the Wiley article page; the row's NORA PDF could not be
  opened by this session's fetch tool.
- Li, Tu et al. (2024), introduction para. 1, at par.nsf.gov: outer belt
  "approximately 3 to 7" Earth radii.
- Alken et al. (2021), full text at the Springer link: no tilt printed;
  the geomagnetic poles are computed from the three degree-1 Gauss
  coefficients.
- NOAA `igrf13coeffs.txt`: the degree-1 rows for 2010.0, 2015.0, 2020.0
  and the 2020-25 secular variation, as tabled in the earlier request.
- Alken et al. (2021) Table 4, 2020.0 row: north geomagnetic pole 80.65,
  -72.68, WGS84 geodetic latitude. Read through the search tool's copy of
  a ResearchGate upload of the paper, not the publisher's table page.
  The coefficients, converted to geodetic latitude, give 80.6512 and
  -72.6797.
- NOT read: the magnetotail source (NTRS 19830066648), and the band
  sources for the outer belt's L = 4 to 5, which rev3 now makes rows.

---

Written September 21, 2026 with Anthropic's Claude Opus 5.
