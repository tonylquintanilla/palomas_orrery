# Worksheet return -- L-247 Sagittarius A* and galactic-scale constants

**Built on `cf865ffc12862eeaeee5c0d7b1a2627dc003d4bd` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**

Responding model: Anthropic Claude Opus 5.
Vocabulary: v2 (2026-08-13).
Answered August 25, 2026. Every value below was fetched from the cited
publication or agency page during this session, not recalled.

---

## Response table

| # | Constant | Code value | Code's source line | Your value | Your source | Value correct? | Citation correct? | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | `GRAVITATIONAL_CONSTANT_SI` -- Newtonian constant of gravitation | 6.67430e-11 m^3 kg^-1 s^-2 | none | 6.67430(15)e-11 m^3 kg^-1 s^-2 | CODATA 2022: Mohr, Newell, Taylor, Tiesinga, Rev. Mod. Phys. 97, 025002 (2025), DOI 10.1103/RevModPhys.97.025002, section XIV (preprint arXiv:2409.03787). NIST reference page: physics.nist.gov/cgi-bin/cuu/Value?bg | YES | UNSOURCED | Exact digit-for-digit match. Measured, not derived. Unchanged from CODATA 2018; the 2022 adjustment took in no new competitive datum for G. Relative standard uncertainty 2.2e-5, so digits beyond the sixth are meaningless. Code precision is exactly the published precision -- not overstated. |
| 2 | `SOLAR_MASS_KG` -- mass of the Sun | 1.989e30 kg | none | 1.98841e30 kg | Derived: (GM)_sun^N / G. (GM)_sun^N = 1.3271244e20 m^3 s^-2 exactly, IAU 2015 Resolution B3, published as Prsa et al. 2016, AJ 152, 41, Table 1, DOI 10.3847/0004-6256/152/2/41. G as row 1. Agency cross-check: NASA NSSDC Sun Fact Sheet, Bulk parameters, Mass 1,988,400e24 kg. | APPROX | UNSOURCED | Right to three significant figures, wrong in the fourth as written. Arithmetic: 1.3271244e20 / 6.67430e-11 = 1.98841e30 kg. The code's 1.989e30 is 0.0297% high. See Finding 1 -- it is not a typo, it is a legacy value carrying a superseded G. |
| 3 | `PARSEC_TO_AU` -- astronomical units per parsec | 206265.0 AU | none | 206264.806247... AU | Definitional, not measured. 1 pc = (648000/pi) au exactly, IAU 2015 Resolution B2, footnote 4 (Mamajek et al. 2015, arXiv:1510.06262); restated in Prsa et al. 2016, AJ 152, 41, section 2. | APPROX | UNSOURCED | See Finding 4 -- the honest token here is DERIVED and the form's two instructions disagree. Arithmetic: 648000 / 3.14159265358979 = 206264.806247096... The value follows from 1 au subtending 1 arcsec, so no source publishes it as a measurement. Code is 0.194 au high, relative error 9.4e-7. The trailing `.0` asserts a tenth-of-an-au precision the written number does not have; the true fourth decimal place is 8, not 0. |
| 4 | `SGR_A_MASS_SOLAR` -- mass of Sagittarius A* | 4.154e6 solar masses | `# Source: GRAVITY Collaboration 2019` | 4.154 +/- 0.014 (stat) e6 M_sun | GRAVITY Collaboration (Abuter et al.) 2019, "A geometric distance measurement to the Galactic center black hole with 0.3% uncertainty", A&A 625, L10, DOI 10.1051/0004-6361/201935656, Table 1, "Down-sampled data" column, row "Mass [10^6 M_sun]". | YES | PARTIAL | Exact match to one of three columns. The source line names a real and correct collaboration and year but no paper, and GRAVITY published several papers in 2019; it is resolvable only because the number is distinctive. Table 1's other two columns give 4.152 and 4.148. Precision is not overstated: the paper's own third digit is significant at the quoted 0.014 error. See Findings 2 and 3. |
| 5 | `SGR_A_DISTANCE_LY` -- distance to Sagittarius A* | 26670.0 light-years | none | 26673 +/- 83 ly | Derived from the same paper as row 4: R_0 = 8178 +/- 13 (stat) +/- 22 (sys) pc, GRAVITY Collaboration 2019, A&A 625, L10, equation (1) in section 4.2. Light-year per IAU convention (Julian year x c, 9460730472580800 m exactly). | APPROX | UNSOURCED | Arithmetic: 8178 pc x 3.2615638 ly/pc = 26673.07 ly. The code's 26670.0 is 3.1 ly low, which is 26673 rounded to four significant figures. Inverting, 26670.0 ly = 8177.06 pc, which matches no column of Table 1 (8179, 8178, 8175). Uncertainty: 13 and 22 pc in quadrature is 25.6 pc, or 83 ly. The trailing `.0` asserts 0.1 ly precision against a real uncertainty of about 83 ly -- overstated by roughly three orders of magnitude. |

---

## Findings

### 1. Row 2 is right for the wrong reason, and the reason is a retired G

`SOLAR_MASS_KG` is not a measured quantity. The Sun's mass in kilograms
is not observed directly; what is observed to high precision is the
product G x M, and the IAU fixes that product by definition as
(GM)_sun^N = 1.3271244e20 m^3 s^-2 exactly. A mass in kilograms is then
whatever you get when you divide that by whichever G you hold.

Divide by the current G and you get 1.98841e30 kg. Divide by the CODATA
1986 value, G = 6.67259e-11, and you get 1.98892e30 kg, which is
1.989e30 to four figures. That is where the code's number comes from.
The two NASA pages still online make the same point: the current Sun
Fact Sheet reads 1,988,400e24 kg, while an older mirrored copy of it
still reads 1,989,100e24 kg. The value did not change because the Sun
changed. It changed because G did.

This matters more than 0.03% usually would, because `constants_new.py`
now holds both factors of a product that is known far better than either
factor. Multiplying the file's own two constants gives

    6.67430e-11 x 1.989e30 = 1.327518e20 m^3 s^-2

against a defined 1.3271244e20. The file therefore contains a solar
gravitational parameter that is 0.030% off a quantity the IAU declares
exact, and it contains it implicitly, where nothing is watching it. Any
calculation of the form G x (mass in solar masses x SOLAR_MASS_KG)
inherits that error -- which is every Schwarzschild radius, escape
velocity, and orbital period in the galactic-scale block.

Two repairs are available and they are not equivalent. Setting
`SOLAR_MASS_KG = 1.98841e30` makes the product right to five figures and
keeps the file's present shape. Introducing `GM_SUN_SI = 1.3271244e20`
as the primary constant and deriving the kilogram value from it makes
the product exact by construction and puts the definitional quantity in
the file rather than a rounding of it. The second is the one that cannot
drift when CODATA next moves G. I have no view on whether that is worth
the migration cost here; that is a scope call.

### 2. Rows 4 and 5 are one measurement, not two

The mass and the distance in this block came out of the same orbit fit
of the same star, and they are strongly correlated. The paper is
explicit about it: for astrometry alone the two are degenerate along
M proportional to R_0 cubed, and Figure 3 is a joint posterior in the
mass-R_0 plane precisely because neither is meaningful without the
other. Section 4.2 quotes a sensitivity of 1.4e3 M_sun per pc.

The practical consequence is a rule about future edits rather than a
defect in the present values. If either row is ever updated -- to the
2022 GRAVITY multi-star result, for instance, which moved both -- the
other must move in the same edit and from the same paper. Taking a newer
distance while keeping the 2019 mass would produce a pair that no
publication supports and that no single-value check would flag, because
each number would still be individually citable.

I would suggest the eventual annotation say so, rather than leaving two
independent-looking `# Source:` lines over what is really one row of one
table.

### 3. The 4.154 column is not the 8178 column

A smaller version of the same point, and it is the one place where I
think the code is quietly self-inconsistent rather than merely rounded.

Table 1 has three columns. The mass 4.154e6 belongs to the "Down-sampled
data" column, whose distance is R_0 = 8179 pc. The headline R_0 = 8178
that the abstract and equation (1) carry is the "Noise model fit"
column, whose mass is 4.152e6. The code has taken the mass from one
column and (as best I can reconstruct) the distance from the other.

The magnitude is trivial -- one part in two thousand, far inside the
paper's own error bars. I raise it because it is invisible to any check
that verifies numbers one at a time, and because it is the same failure
shape as Finding 2 one level down: a pair pulled from a table where the
rows are not independent.

If it were mine I would take both from the noise-model column, which is
the one the paper leads with, and record the column name in the
annotation so the next reader does not have to reconstruct which of the
three was used.

### 4. Row 3 exposes a conflict inside the request form

The instructions say two things about row 3 that cannot both be
followed. The header of the citation column offers `DERIVED` as a token,
and the question list says explicitly that a defined or derived quantity
should be marked as such rather than have a citation forced onto it. But
the paragraph above the table says rows 1, 2, 3 and 5 name no source in
the code, so write `UNSOURCED`.

For row 3 these give different answers. `UNSOURCED` is a true statement
about the code -- the line carries no source. `DERIVED` is a true
statement about the quantity -- 648000/pi is a definition and there is
no measurement to cite. They describe different objects, and the column
header says the citation verdict is about the source named in the code,
which points to `UNSOURCED`.

I wrote `UNSOURCED` in the cell, because that instruction is the more
specific one and it names row 3 directly. But I think the form wants a
different fix rather than a ruling: `DERIVED` and `UNSOURCED` are not
alternatives on the same axis. One says where the value came from, the
other says what the code claims about it. A future revision of the
vocabulary might make that a separate column, or drop `DERIVED` from
this one and let the Notes carry it.

Row 2 has a weaker form of the same problem: it is also derived, but
unlike row 3 it has an authority to point at, since the IAU publishes
the input and NASA publishes the output.

### 5. What the closure check can and cannot settle

I tried to test rows 1, 2 and 4 against each other using a quantity the
paper derives independently: it reports the angular Schwarzschild radius
as R_s/R_0 = 10.022 +/- 0.020 (stat) +/- 0.032 (sys) microarcsec.

Recomputing that from the code's constants gives 10.0305 microarcsec.
Recomputing it with the corrected solar mass gives 10.0275. Both sit
inside the paper's combined uncertainty, so the check passes -- and it
passes either way, which means it does not discriminate between the two
solar masses and cannot be used to argue the code's value is fine. I
report it because a check that returns green for both branches of the
question it was aimed at has not answered that question, and it would be
easy to read the green as a clearance.

What it does establish is weaker but real: the five constants are
mutually consistent at the level the paper's own error bars can see, so
there is no gross unit or scale error hiding in the block.

### 6. Nothing here is stale, but row 4 has a successor

For completeness rather than as a defect: GRAVITY has published later
determinations, including a multi-star fit in A&A 657, L12 (2022) that
gives a different mass and distance pair. The 2019 values are not wrong
and remain widely cited. Whether the orrery should track the most recent
publication or pin a stated epoch is a policy question I have no basis
to answer from inside this worksheet, but it is the sort of thing worth
deciding once rather than per constant.

---

## One procedural note about this return

The request's footer records that it was written with Claude Opus 5,
and I am Claude Opus 5. I have no access to the session that wrote it
and no proposal travelled with it, so this answer is independent in the
sense that matters mechanically. It is not independent in the sense of
being a different model family. If the second return is also a Claude,
the pair will not test what the two-model design is meant to test.

*Return written August 25, 2026 with Anthropic's Claude Opus 5, against
`cf865ffc12862eeaeee5c0d7b1a2627dc003d4bd`. Ledger: L-247.*
