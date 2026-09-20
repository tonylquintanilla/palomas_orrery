# Review of L-322 Stage C1, for the builder

Reviewed at orrery `21065c5d95ecb22c79fa1f398644a30b73a9a5ed`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `2ead992b055054956816ddda3544e849e9789d9a`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both HEADs read live on 2026-09-19 and both repositories cloned there.

Reviewer: Claude Fable 5.1, for Tony Quintanilla. Contract:
`documentation/BUILD_MANIFEST_L322_earth_slice_20260919.md`. Rules:
provenance-discipline 2.14, The Figure Count Is a Declared Field and The
Read Field. Both uploaded files were read in full from disk, including
the run record, which did not arrive in context.

## What holds, checked independently

- Earth rows: unit 57 of 57, status 57 of 57, figures 29 of 57, read 12
  Earth rows plus `KM_PER_AU` and `GM_SUN_SI`. The 28 without figures are
  C2's magnetosphere rows.
- Export: 55 rows; its store hash `179dbd5877b8` matches
  `constants_new.py` at HEAD. The gallery's pulled export names orrery
  `4f547285`; the store has not changed since.
- Checkers run here: Derived figures 15 OK of 31; Dimensions 15 OK, 10 NO
  UNIT, 6 NOT CHECKABLE; Export check matches. All exit 0.
- Gallery: Cache in step passes; the cache holds 5710.0 and no 5711.
- Two reads re-opened by me. The NASA Earth Fact Sheet prints polar
  radius 6356.752 and volumetric mean radius 6371.000. The NOAA page
  prints "around 31 miles (50 km)" and "about 375 miles (600 km)" with
  the thermopause at the bottom of the exosphere. Both as recorded.
- The three citation corrections (rotation rate's table, the polar
  radius re-homed, TCB to TCG) and the IADC revision correction are the
  kind of finding the read exists to produce.

## Finding 1 -- a visitor-visible defect, live now

The geocorona's hover reads **"Radius: 1e+2 Earth radii"**. Before C1 it
read "100.0000 Earth radii". Reproduced by building Earth's scene in
node from the pushed config at `2ead992b` and at `2ebd001f`.

Cause: `fmtServed` in `gallery/feature_renderers.js` (line 155) returns
`value.toPrecision(figures)`. JavaScript switches to exponent notation
whenever the integer part has more digits than the figure count, so 100
at one figure prints as `1e+2`. C1 is the first time a served value met
that condition. C2 will add more: any value of 10 or more declared to
one figure, 100 or more to two, and so on.

The same hover then gives the altitude as 631,436 km, six figures beside
a one-figure floor. That part predates C1.

Needed: a formatter that rounds to the declared figures and prints plain
digits; and a check that fails when any built hover contains exponent
notation. No check in the gallery run reads the numbers in a hover,
which is why 14 of 14 passed over this.

## Finding 2 -- the padding rule contradicts Rule 2, and one premise is false

The walk settled that a trailing zero in a padded decimal place does not
count while a non-zero digit there does, giving 3480.0 four figures,
6371.000 four, and 1221.5 five.

Rule 2 of the skill says: "zeros after the decimal point at the end
count." That is the textbook rule Tony asked for by name. The walk's rule
makes a number's precision depend on which digit happens to land in the
last place. A column measured to 0.1 km ends in zero one time in ten.

The premise for the NASA row is also not what the page shows. The row
says the sheet is "padded to three decimals throughout". The same block
prints core radius 3485, mean density 5513, topographic range 20.4 and
escape velocity 11.186. It is not uniformly padded, so 6371.000 reads as
a deliberate seven figures, the same as the two radii above it.

The effect is conservative: hovers show fewer digits, never wrong ones.
But every `_RADII` row divides by the mean radius, so four figures there
caps all of them.

Needed: either apply Rule 2 as written (3480.0 is five, 6371.000 is
seven), or bring Tony the case for an exception as a rule for the skill.
It is not the builder's to settle inside a figures line. Two examples in
the skill are now stale either way and are owed to its next bump: Rule
1's "the trailing zero in 3480 is significant" and Rule 3's
"`6371.0 - 660` is good to units: 5711".

## Finding 3 -- the Hill sphere declares seven figures and disowns them

`EARTH_HILL_SPHERE_KM` declares `# Figures: 7` and the same line says
"The formula's own idealisation is coarser than any of this; report
1.50e6 km." The gallery formats from the declared count, so a visitor
sees "234.6388 Earth radii" and "1,496,558 km".

Rule 3 counts measured inputs. It has no place for a formula that is
itself an approximation, and the Hill radius is one: using Earth's
perihelion distance instead of its mean distance moves it by more than
one percent. The honest count is the one the line already names, three.

Needed: declare three and say why, and carry to the skill's next bump a
sentence that a row may declare FEWER figures than its inputs support
when the relation itself is approximate, with the reason in words.
`EARTH_GEOSTATIONARY_RADIUS_KM` at seven is sound by the rules and is
left alone; whether 6.610735 Earth radii is pleasant to read is Tony's
to judge on the phone.

## Finding 4 -- the disputed commit, from the commits themselves

Orrery `4417217` holds four files: `constants_new.py`, the read record,
the run record and the patch script. It holds none of the files every
maintenance run rewrites (`DATA_INVENTORY.md`, `PROVENANCE_AUDIT.md`,
`WORKSHEET_CHECK.md`, `data/provenance_history.json`). The next commit,
`4f54728`, holds all of them and the export.

So Tony excluded nothing, as he said twice. And the maintenance run had
not been run between the patch and that commit; the run record shows the
patch output followed directly by the gallery steps. The patch's own
closing text said nothing should change, which made the run look
optional. The builder's explanation, that Tony left a file out, was a
guess and was wrong.

Worth a line on the ledger: a commit made without the maintenance run is
visible afterwards by the absence of the files the run always rewrites.

## Carried forward from the pre-build comments, still open

The skill says a missing `# Read:` on an in-scope row inside a closed
slice FAILS. No check does that yet. The builder has said it will build
one before Earth closes. It should be demonstrated failing before
`CLOSED_SLICES` changes.

---

Written September 19, 2026 with Anthropic's Claude Fable 5.1.
