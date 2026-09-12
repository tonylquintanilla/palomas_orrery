# Review reply -- a figure in prose needs a home, and the L-321 rev 2 prompts

Reviewed against orrery `a4ead59ac3f3f390710c99c4e3687d60b444447c`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `1f44673faf2acd32340bfdd4b524b6c8af5dd376`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Tony Quintanilla, PE | reply written by Claude Fable 5.1, inside the
Paloma's Orrery Project (protocol and skills resident) | 2026-09-12
Type: DESIGN REVIEW REPLY (Mode 7, cooperative), covering both
documents. No code, no ledger handles.

## What I read

- `PROJECT_INSTRUCTIONS.md` v3.57, resident; the named sections.
- `skills/provenance-discipline/SKILL.md` 2.11 (installed copy, matches
  the manifest and was diffed byte-equal to the repo copy earlier
  today): When the Source Gives a Range, Geometry Constants Are
  First-Class Claims, One Value One Home, A Drawing Approximation Does
  Not Promote, Report to the Figures You Have, The Status Line.
- `skills/orrery-coding-conventions/SKILL.md` 1.8 (matches the
  manifest): Hover Text AU Convention, Visualization Constant vs Range
  Convention.
- At the SHA: `constants_new.py` rows 293-314 and 641-652;
  `earth_visualization_shells.py` 725-765 and 883-892;
  `shell_configs.py` 2295-2306; `solar_visualization_shells.py` 66-80;
  the gallery's `data/objects_config.json` (`van_allen_belts`,
  `magnetotail`) and `gallery_maintenance_run.py`'s `parse_constants`.
  I did not re-derive the conversion table; I spot-checked two cells and
  they hold.

## Where the framing is wrong, first

**1. The span figures ARE in the store. They are just not values.** Both
belt rows in `constants_new.py` carry the extent in a Note: "the inner
belt spans roughly L = 1.1 to 2" under the inner peak, "the outer belt
spans roughly L = 3 to 7" under the outer peak. The gallery's
`objects_config.json` repeats both, word for word, in its `note`
fields. So "neither figure was ever in the store" is not the diagnosis.
The diagnosis is: the figure is in the store as prose, where nothing
can interpolate it and nothing can check it, and every downstream copy
was typed from that prose. The mechanism the record proposes is still
the right one. The sentence that motivates it should say what actually
happened, because the actual failure -- a Note becoming a store -- is a
class, and it recurs wherever a row carries a figure in its Note that
the row's value does not hold.

**2. There are three frames, not two, and the store's own frame is the
one the record's table leaves out.** The store Notes say L. The hovers
say "Earth radii from Earth's centre." The tooltips say kilometres of
altitude. L is the McIlwain L-shell: the distance, in Earth radii, at
which a magnetic field line crosses the magnetic equator. For a dipole
that equals geocentric radius at the equator and nowhere else; a belt
spanning L = 3 to 7 reaches much lower altitudes at high latitude. The
hover was written from the Note and dropped the L. That is the same
omission the record found in the L-321 prompt -- a frame silently
changed in transcription -- one layer earlier. The peak rows have it
too: the sources put the outer peak at L = 4 and 5 and the store row
calls it R_E.

**3. Two skills state the range rule, and one is the superseded form.**
`provenance-discipline` (When the Source Gives a Range) says store the
range as data and interpolate it, and says in so many words that this
supersedes the weaker Batch 1 form: single best value in code, range in
the comment. `orrery-coding-conventions` 1.8 (Visualization Constant vs
Range Convention) still states that weaker form as the rule, with a
worked example. The belt rows are not a violation of anything; they are
that weaker convention, executed correctly. A fresh session loading the
coding skill for hover work would build the failure again. The master
copy of the rule is in the provenance skill; the coding skill should
point there. One ledger row, by class: a rule stated in two skills,
one superseded.

## Tony's rulings

**A. The slice.** Agree, with one boundary check. The tail is in on the
record's own logic and I agree; the reason to state on the row is that
the gallery already asserts an extent in prose ("past 1,000 radii"), so
the claim is rendered and is inside the bound. The exclusion of Shue's
and Jelinek's validity ranges is right.

**B. One frame.** Right conclusion, wrong frame, and the binary is
false.

Wrong frame: the frame the source states is L for both belts, not
Earth radii from centre. B on its own terms -- "the frame the source
states" -- puts the rows in L, dimensionless, with a Note that at the
magnetic equator L reads as geocentric distance in Earth radii, which is
where the torus is drawn. Calling it R_E in the store is a conversion
nobody stated, one level down from the one the record caught.

False binary: "one frame" and "a kilometre presentation" are not
opposed. The file's own worked precedent prints AU and light-years from
ONE constant by arithmetic inside the f-string
(`solar_visualization_shells.py` 72-80). A belt string can print the
stored L and derive an equatorial altitude from it in the same line,
and the two cannot disagree because one is computed from the other.
That is exactly the by-construction association Tony asked for. The
coding skill's Hover Text AU Convention (every distance hover carries
two units) is also a standing rule that B as worded would break.

So: one frame in the STORE, which is L; derived presentations in the
STRING, as many as help a visitor, each computed from the row. The
altitude figures leave the strings as typed numbers and may come back
as arithmetic. Whether a lay visitor is better served by kilometres is
Tony's call; the design should not need the ruling.

**C. Values at item 7.** Agree without reservation. Storing a number
the worksheets are about to check is storing a number to be corrected.

## The questions

**1. Tuple or two scalars.** Two scalars. Three reasons, and the
precedent survives them.

- Provenance is per number. The record's own example -- a well-measured
  inner edge and a variable outer edge -- is the belt case exactly; the
  outer belt's outer edge "moves with geomagnetic activity" and the
  inner edge does not. One `# Status:` on a tuple forces one state on
  two things.
- The checker's derived rule names INPUTS, and a top-level scalar is
  what it resolves. A drawn value derived from a range names two
  scalars cleanly; naming a tuple's element is a form nothing in the
  file uses.
- The gallery's parser evaluates numeric expressions and a tuple is not
  one, which the record measured. Two scalars reach the served side in
  the existing value / unit / source / pointer shape with no second
  shape and no parser change. That is the answer to the second half of
  question 3 too.

The precedent stays as it is. Braid: forward-going on rows touched, and
`GRAVITATIONAL_INFLUENCE_RANGE_AU` becomes a one-line class in the
backlog ("range rows held as tuples: 1"), not a migration.

**2. The checker.** The check that would have caught it already runs,
and it was blind for the reason found this morning. The provenance
scanner flags number-plus-unit tokens in display strings; "3 to 7 Earth
radii" is such a token. The belt strings were not flagged as uncited
because the same string carries "Source (peak): Baker..." and the
scanner's window credits the whole block. A citation for the peak
cleared the span. That is the window inference again, and it is
L-322's -- a citation should clear the figures it names, not the block.

So interpolation IS the rule, and it is already written (One Value One
Home: prose counts). A grep for bare numerals is the wrong new tool
because the scanner is that grep, with a unit vocabulary, an exceptions
file and a run history. What is missing is not detection; it is the
scanner believing a nearby citation covers a number the citation does
not mention. Fix that once, in the scanner, and this class stops being
invisible.

**3. The tail.** Neither rule wins, because they are not about the same
number. Split it:

- The DRAWN 100 is a shape, in the same family as the 15-radius base
  and 25-radius end beside it. A Drawing Approximation Does Not Promote
  and One Value One Home's own scope boundary (declared drawing
  parameters stay where drawn) both say no store row. The gallery's
  copy is a served drawing parameter, the same kind of duplicate as
  every opacity in `objects_config.json`; the two repos already carry
  those in parallel by design.
- The OBSERVED extent is the number that earns a row, because prose
  states it (the gallery already does) and Show the Envelope says the
  hover must. That row's honest form is the envelope, not "about
  1,000": Ness reports a single crossing at 900 to 1,050 radii with
  "probable" in the title, which is a signature, not a coherent tail.
  Prompt 1 row 7 is the right question. Two later deep-tail campaigns
  are worth the checkers' attention -- ISEE-3's 1983 passes and
  Geotail's early orbits, both a few hundred radii downstream -- but I
  am naming those from recall, not from a source I opened, so they are
  candidates to verify and not figures to store.
- The hover then says both, and the 100 in that sentence interpolates
  the drawing parameter from where it is drawn, while the observed
  figure interpolates the store. Two numbers, two homes, one sentence
  that cannot drift from either.

**4. Discovery beyond Earth.** The pattern is already stated, in code:
the scanner's numeric-claim regex, number plus a unit from its
vocabulary, in a display string. It terminates because the tree is
finite, and its output is already a list: PROVENANCE_AUDIT.md's
display-string class, which the skill records at 284 findings holding
553 claims. Dates have no unit and are excluded; axis labels carrying
"AU" or "km" will appear and are a class to name and set aside. Do not
write a second enumerator; read the one that exists and split its list
by whether the numeral is interpolated. That split is the only new
work, and it can be done by grep for `{` inside the flagged strings.

**5. Naming and reporting.** Two scalars need two names; the
precedent's `_RANGE_` shape does not carry. `_INNER_EDGE` / `_OUTER_EDGE`
for each belt reads as English and says which end is which, where
`_LOW` / `_HIGH` would not survive the inner belt (whose "high" edge is
lower than the outer belt's "low" one). Unit: whatever the source
states, which for both belts is L.

"3 to 7", not "3.0 to 7.0". The sources give integers, Report to the
Figures You Have says report what the input supports, and `:g` prints
3.0 as 3. The figure count is stated on the row, in prose, as the file
already does; the specifier lives with the string, as this morning's
`:.4g` ruling settled, and both wait on L-322(d) for the declared form.
Same interim as the standoffs, no new entrenchment.

## The rev 2 prompts

Five things, in order of consequence.

**1. Rev 2 depends on a patch that does not exist yet.** "What changed"
item 3 says the pending L-305 patch deletes the Lugaz midpoint sentence
and moves the bow shock's attribution to Jelinek. At this SHA the patch
changes format specifiers only; the words are untouched. That was the
first finding of the build review, and it is still Tony's ruling to
make. If the words change inside the patch, rev 2 is right as written.
If they wait for L-321, prompt 2 must row the Lugaz sentence and the
Lugaz attribution as they stand, because they will be what the checker
reads. Say which in the header.

**2. Prompt 3 row 5 assigns a citation the string does not make.** The
inner belt string reads "Source (peak): Baker et al. (2018)". It cites
Baker for the PEAK. Row 5 tells the checker Baker "supports rows 2 and
3", which hands the span a citation nobody wrote. UNSOURCED is the
verdict the design record itself expects for row 3; the prompt should
let the checker reach it. Row 11 gets this right ("supports row 7"
only). Make row 5 match.

**3. Three frames, not two.** The frame note says rows 3 and 4 are "the
same inner belt in two reference frames." The store's frame is L, the
hover says geocentric R_E, the tooltip says altitude. A checker whose
source states L will write L in the Source unit column and may treat it
as identical to the hover's R_E; the note should name L as the frame
the sources most likely use and say that it equals equatorial
geocentric R_E for a dipole and nothing more. The same applies to the
peak rows 2 and 7, which the string calls R_E and the sources call L.

**4. Rows 4 and 9 are being checked so that ruling B can retire them.**
Rev 2 removed the Lugaz rows because verifying a sentence about to be
deleted "spends its time on nothing," and then keeps the altitude rows
that ruling B deletes. There is a good reason -- the altitude figures
may be the better-sourced ones and the worksheets decide which survives
-- but the prompt should say that, or the two decisions read as
contradictory. The header calls the job CITATION VERIFICATION; rows 3,
4, 8 and 9 are value discovery, and the checker should know which job
each row is.

**5. Small.** The common header's read-back asks for two files; it
should also name `skills/orrery-coding-conventions` only if the checker
is expected to judge string form, which it is not -- so two is right.
Prompt 1 row 5 ("making complex life possible"), verdicted as stated:
good; that is the row most likely to come back NO, and it should.

## The one decision

The rulings stand with one amendment: the store frame for the belts is
L, as the sources state it, and the hover may print kilometres derived
from it. Everything else above is a prompt correction or a class for
the ledger. What is still open from the build review -- whether the
bow shock words change in the L-305 patch -- decides whether rev 2 can
be sent as written.

Written September 2026 with Anthropic's Claude Fable 5.1.
