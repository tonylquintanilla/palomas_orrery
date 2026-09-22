# Addendum, revision 3 -- the pick-by-rule row, the angle-rate row, and two corrections

**Built on orrery `a318b3ecfed1ffaa290e8b34ed1ef63caa59295d`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `b17fd92704054e83424651585aa68a393ecb3d92`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both HEADs re-read live on 2026-09-21; neither has moved.**

**Type: ADDENDUM rev3, Mode 7.** Written September 21, 2026 by Claude
Fable 5.1, after `REVIEW_L322_C2_tilt_addendum_rev2_opus_20260921.md`
and GPT 6 Medium's review of that review, both carried by Tony. It
amends rev2 in the four places below and leaves the rest of rev2
standing: the withdrawals, the tilt row at five figures, the six
coefficient rows, the reach enumeration, and the proposed Rule 7 text.

**Rule files and sections read.** provenance-discipline 2.16 from the
repo at `a318b3ec` (mounted copy 2.15, as before): Rules 2, 3, 7, 8, The
ceiling, When the source gives a range. Code at `a318b3ec`, read and
run: `test_derived_figures.py` (the header's rules 1-4, the `Figures`
walker's `FUNCS`, `NUMBERS` and its `exact` branch at lines 346-352),
`test_dimensions.py` (`FUNCTIONS`, `NUMBERS`, `FAILING`, and
`dimensionless_to_number`), `export_constants.py` (`round_to` and the
exact branch). astropy 7 installed in the sandbox to test finding B.

All four findings are accepted. GPT's two qualifications are taken up
where they land (B and A).

---

## Finding A. A pick-by-rule over measured rows -- settled as method

**What was wrong.** Rev2 asked for a row that is at once an expression
over two one-figure measured rows and "exact". The checker refuses
that (exact only when every input is exact), one figure exports as
4.0, and the orrery draws 4.5 from the float. Two consumers, two rings.

**What the skill already settles.** When the source gives a range: the
display "interpolate[s] the range rather than restate[s] the drawn
value as a measurement." So the hover shows the band from its two rows
and does not print the pick's own digits, or a kilometre figure of
them, as a measurement. That retires "28,701.615 km" for a reason the
skill states: the line "Drawn at 4.5 Earth radii = 28,701.615 km" is the
drawn value restated as a measurement, and it goes. The hover says
where the peak is placed and by what rule: "Drawn at the midpoint of
the L = 4 to 5 band in which the sources place the outer belt's
greatest intensity", band served.

**What the skill did not settle: how the row is counted and served.**
Rule 2 makes a declared pick exact; Rule 3 and the walker count an
expression from its measured inputs; the export rounds to the count.
When they meet on one row, the drawing moves. The resolution, which is
GPT's distinction made mechanical: a DECLARED CONSTRUCTION is exact as
a construction, and its measured inputs keep their own provenance on
their own rows.

- The row's `# Status:` begins `declared` and names the rule. Its
  `# Figures:` reads `exact -- declared construction: midpoint of
  <row>, <row>`.
- The checker accepts `exact` on a row whose status begins `declared`
  (not `declared pending`), provided every row the line names is in
  the expression -- the name check Rule 8 already runs. A `measured`
  or `derived` row still cannot declare exact over measured inputs.
  The status line is a field the checker can read, and it is what
  says the row is a choice.
- The export serves an exact row unrounded, as it already does, so
  the gallery and the orrery draw the same 4.5.
- The two band rows are measured, one figure each, with their reads.
  They carry the provenance; the construction carries the rule.

**Proposed wording**, under Rule 2 after "A DECLARED drawing condition
... is exact for counting":

> A DECLARED CONSTRUCTION -- a drawing value that is a stated rule over
> measured rows, such as the midpoint of a sourced band -- is exact for
> counting in the same way, and its `# Figures:` line names the rule
> and the rows: `exact -- declared construction: midpoint of <rows>`.
> The checker accepts `exact` only on a row whose status begins
> `declared`, with every named row in the expression; the export serves
> it unrounded, so every consumer draws the same value. The
> construction is not a measurement and the hover does not print it as
> one: it shows the range from the rows and states the rule. Earth's
> outer-belt peak is the case (L-322 C2).

## Finding B. The rate row, rewritten so both checkers judge it

**1. `hypot` goes.** Written with `sqrt(G11**2 + H11**2)`, which both
function tables know. No checker learns a function.

**2. Three figures, not two.** Rev2 counted only products and
quotients. The expression contains the sum `G11*S11 + H11*SH`, and
Rule 3 counts a sum by decimal place: both terms are good to the
thousands, so the sum carries three figures and the row does. The
walker's answer, confirmed by Opus and by GPT: **-0.0493 degrees per
year, three figures.** The `# Figures:` line says the sum set it.

The propagation from the file's print resolution, about 0.00013
degrees per year, is CORROBORATION only, as GPT says: it takes each
coefficient's implied half-unit as independent, it says nothing about
the model's real error or about future drift, and under The ceiling
implied uncertainties never replace counting. The row may cite it as
corroboration with those assumptions named, or omit it.

**3. The unit check: how a rate of an angle is written.** Tested with
astropy at `a318b3ec`'s function table: the core expression evaluates
to 1/year, `np.degrees` refuses it ("Can only apply 'degrees' function
to quantities with angle units"), and CANNOT EVALUATE is on the FAILING
list. GPT is right that an equivalency alone does not repair it.

The route that needs no checker change: **an exact conversion row
carries the radian.**

```python
DEG_PER_RAD = 180.0 / np.pi
# Unit: deg
# Figures: exact -- a definition; the radian is dimensionless

EARTH_DIPOLE_TILT_RATE_DEG_PER_YEAR = (
    (abs(EARTH_IGRF13_G10_NT)
     * (EARTH_IGRF13_G11_NT * EARTH_IGRF13_G11_SV_NT_PER_YEAR
        + EARTH_IGRF13_H11_NT * EARTH_IGRF13_H11_SV_NT_PER_YEAR)
     / np.sqrt(EARTH_IGRF13_G11_NT**2 + EARTH_IGRF13_H11_NT**2)
     + np.sqrt(EARTH_IGRF13_G11_NT**2 + EARTH_IGRF13_H11_NT**2)
     * EARTH_IGRF13_G10_SV_NT_PER_YEAR)
    / (EARTH_IGRF13_G11_NT**2 + EARTH_IGRF13_H11_NT**2
       + EARTH_IGRF13_G10_NT**2)
) * DEG_PER_RAD
```

(The second term is `- H * d|g10|/dt` with `d|g10|/dt = -g10'` for
negative g10, so it appears as `+ H * g10'`.) Measured with astropy:
nT * nT/yr / nT^2 = 1/yr, times a quantity in deg = deg/yr, with no
equivalency; value -0.0492766. Both walkers know `np.pi` and `sqrt`.
Tokens: `nt_per_year` maps to nT/yr and `deg_per_year` to deg/yr in
`constants_tokens.py`; the checker compares the computed deg/yr against
the declared token and reports OK.

**Proposed wording**, added to the Rule 3 paragraph on rate rows in
rev2:

> A rate of an angle never applies `degrees` to a non-angle; the
> arithmetic yields inverse time and the unit check refuses the call.
> It multiplies by the exact row `DEG_PER_RAD`, whose unit is `deg` and
> which carries the radian, so the unit check follows the chain to
> degrees per time with no equivalency. Angle-rate rows use time-rate
> tokens (`nt_per_year`, `deg_per_year`).

The hover prints the rate at the row's count: "decreasing about 0.0493
degrees a year". Words Tony's.

## Finding C. Corrected

The four `:.4g` sites do not print "10.25" after C2; the store no
longer holds it. They print the new expression's value to four
significant figures, which exceeds the declared three: excess displayed
precision, failing the current Rule 7. They come into C2 for that
reason.

## Finding D. Stated on the ledger row

The deferred class -- the orrery's Earth display sites, 43 remaining
after the four above -- has NO automated coverage: no checker reads
orrery display formatting. The ledger row says so in its first
sentence, so that a closed Earth slice is not read as covering those
sites. It is a Braid deferral, not a pass.

## What this changes in the manifest, beyond rev2

- 4.1: two tokens, `nt_per_year` and `deg_per_year`.
- 4.2/4.3a: `DEG_PER_RAD`, exact; the rate row as written above, three
  figures; the outer-belt pick as a declared construction over two band
  rows.
- 4.7: the checker accepts `exact` on a declared-status row with its
  named rows in the expression; shown failing on a `measured` row
  declaring exact over a measured input.
- Section 6: the outer belt's "Drawn at 4.5 Earth radii = 28,701.615
  km" line is replaced by the rule-and-band line; the belt tilt line
  prints the rate at three figures.
- Section 11: the deferred display class carries the no-coverage
  sentence.

---

Written September 21, 2026 with Anthropic's Claude Fable 5.1.
