<!-- Doc-Kind: hand | The older version history of the long skills, moved out of each SKILL.md so the skill opens with its rules. A record, not a store of rules. -->
# Skill histories

Moved here from the skills' own SKILL.md files on 2026-10-05 (L-418),
from palomas_orrery @ 72e3b55805c29f1f08a583864bd815a47e7434c6 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

THIS FILE IS A RECORD, NOT A STORE OF RULES. Nothing in it fires, and
no session needs to read it to work correctly. Each skill keeps its
three latest version entries; when a fourth is added, the oldest moves
to the end of that skill's section here -- the rule the protocol uses
for its own history. Every entry below is word for word as it stood in
the skill, in the skill's own order.

## provenance-discipline

v2.23 settles L-398 with one new section, A Computed Position Prints
What Its Errors Earn. A distance worked out from served elements prints
to the Report test's place for the LARGER of two errors: how far our
arithmetic may have drifted from Horizons, and how well JPL knows where
the body is at all. Tony's ruling, 2026-10-01: "use whichever is
larger". Drift alone had printed Pluto to ten figures. The section's
second half is the case the source's accuracy forced: an ACCURACY
STATED ONLY IN WORDS is stored as the place those words report to --
the place the Report test gives for every value the words can mean,
the coarser where they could mean two -- and never as a number the
source does not print. JPL's 2014 report gives three groups, so 1 km,
100 km and 10,000 km. The last is one place coarser than the session
plan of 2026-10-01 said; Tony confirmed it as recommended the same day.
v2.22 settles L-345: A VALUE IN ANOTHER UNIT IS COMPUTED, NEVER STORED,
AND ITS COUNT COMES FROM ITS SOURCE ROW ALONE. Each quantity is one row,
in the unit its best source gives it, with that source. Its value in
any other unit is worked out from the row's full digits and rounded
once, by constants_rows.conversions(), and the export serves it as
"in" (schema 6); no second row states it. The count: the source row's
uncertainty -- stated, or half a unit of its last declared place, or
half a unit of the last place of an exact row's print count -- scaled
by the exact factor, then the Report test's place. It replaces 2.21's
"for now" sentence, so a single measured value scaled by an exact row
is no longer left under fewest figures. It cuts both ways: the
chromosphere keeps 1.003 solar radii, and the bow shock's 13.5 Earth
radii is 86,000 km (two figures), not 86,200. Rule 8's checker
paragraph is widened to match. Tony's ruling, 2026-09-28, on Claude
Fable 5.1's recommendation; handle L-345.
v2.21 adds one paragraph to Rule 3: a value good to a decimal place,
scaled by an exact row, keeps its place and not its figure count. A
sum good to thousands of kilometres divided by the nominal solar
radius is good to thousandths of a solar radius; counted by fewest
figures it would keep three, and three figures of 1.003 is a factor
of seven coarser than three figures of 698,000, because the leading
digit went from 6 to 1. The reference page names the case as its
unit-conversion exception (8 inches converts to 20. cm, not 20 cm).
It reaches sums and differences only; a single measured value scaled
by an exact row stays under fewest figures for now.
Rule 1 gains the seventh form that carries it; the ceiling's
implied-uncertainty bullet says a converted place is not that; the
Report bullet cross-links; Rule 8 says how the checker finds the
place and prints it. The worked case is the top of the chromosphere,
which prints 1.003 and not 1.00: at 1.00 the export, which rounds to
the count, would have drawn it on the photosphere and erased the
2,000 km hairline promoted on 2026-08-16. Before this the two forms
of the same expression counted differently, 1.00 sum-first and 1.003
divide-first, and the unit check forced the coarser. Tony's ruling,
2026-09-28, on Claude Fable 5.1's recommendation, checked against
the reference page the same day. Handle L-322.
v2.20 writes down where a trailing ".0" comes from, in Rule 2. It is
Python, by three routes, and none of them is a statement about
significant figures: a decimal point is typed to make a number a
float, Python's division always returns a float, and a float printed
without a format always shows ".0". So a row's figure count is never
read from its literal, its printed form or its exported form, which is
why the count and an exact row's print count are both fields. Tony
asked for the claim to be checked and added on 2026-09-27, when the
Stage D print counts were settled from what each row says it was
chosen with. Checked by running Python 3 and Node. RULE 7'S EXACT ROW
is brought into line with the code that builds it, orrery patch D15:
the print count is read only directly after "exact --"; a declared
construction prints the digits of the value its rule gives, so the
outer belt's midpoint of 4 and 5 prints 4.5; the checker refuses a
count with more digits than the number has, one too small to write it
in full, and anything but 1 on a zero; and exact_rows_report.py
--check fails the maintenance run while any printed exact row is not
printed by its count. The last two are Claude Opus 5.5's additions in
building D15, approved by Tony the same day. Handle L-322.
v2.19 replaces one worked example that had gone stale. Rule 7's exact
row said Earth's obliquity "prints 23.439291 degrees". Since the Stage
D manifest's revision 3 (2026-09-23) no display prints the obliquity:
the axis hovers print the tilt of date, worked out from the pole
Horizons serves, and the obliquity row is used only as the angle that
defines the ecliptic frame. The rule itself stands; the example now is
the gallery's magnetopause hover, which prints the exact row
EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG today with a width chosen at the call
site. Found carried in two handoffs; checked against the skill, the
manifest and the code on 2026-09-25, where every consumer of the
obliquity was also confirmed to use the right value for the right job.
Handle L-322.
v2.18 settles where a drawing number lives and how an exact number
prints, before L-322 Stage D builds on both. THE SCOPE BOUNDARY in One
Value, One Home becomes THREE KINDS OF DRAWING NUMBER, Tony's ruling
of 2026-09-22: a physical value (a size, an edge, a cut angle) lives
in constants_new.py, sourced or declared; an eyeballed value does not
promote and is cleaned up as the braid reaches it; a rendering setting
(point count, opacity, colour, marker, font) stays in the drawing
code. The test is whether changing the number moves WHERE something
is drawn. This removes a contradiction: A Drawing Approximation Does
Not Promote said opacity and point count stay in the store, while One
Value, One Home kept them in the drawing code. RULE 7 GAINS THE EXACT
ROW: an exact quantity is stored in the form its definition prints,
every exact row a display prints states a print count as a field, and
the page prints by that count instead of by a width chosen at each
call site. RULE 1 gains the sixth form that carries it. RULE 3 GAINS
THE CONVERSION ROW: a unit conversion inside an expression is an
exact row with a compound-unit token, never a bare 3600, because the
unit check converts units by itself. WHEN THE SOURCE GIVES A RANGE
gains its default: the midpoint, unless the row states a reason for
an end. Worked cases: Earth's obliquity, which Horizons defines as
84381.448 arcseconds, and Earth's sidereal rotation period, whose
bare-divisor draft failed the unit check while the figures check
passed it. From Claude Fable 5.1's review of the Stage D manifest and
Claude Opus 5.5's answers to it, 2026-09-23; every form was run
through both checkers on a throwaway copy at ac25d4f4. Handle L-322.
v2.17 closes the gap a display decision opened. Asked whether Earth's
dipole tilt should print 9.4 or 9.4105, a reviewer offered a
readability call; Tony asked what the basis was -- "the basis should
be in the skill not arbitrary" -- and there was none: Rule 7
permitted a shorter display and gave no method. RULE 7 IS REPLACED
WHOLE: a display prints the declared count and never chooses fewer;
a number that reads as too many figures is a finding about the ROW,
fixed under Rule 3, never by the page. RULE 2 GAINS THE DECLARED
CONSTRUCTION: a drawing value that is a stated rule over measured
rows is exact as a construction, the checker accepts exact on it
only when its status begins declared, and the export serves it
unrounded so every consumer draws the same value. RULE 3 GAINS two
rules for a derived quantity: a rate is written as the derivative,
never as a difference of two evaluations, because the difference
form takes its count from the largest inputs rather than from the
quantities the rate rests on; and an angle computed from a pure
number multiplies by the exact row DEG_PER_RAD instead of calling
degrees, because the unit check sees a bare number and refuses the
call. SHOW OR CAP gains the snapshot of a moving quantity: where the
source publishes the rate, the store holds its inputs and the page
shows the epoch and the rate. RULE 6 says a whole the source defines
from parts it prints is a derived row over rows for the parts, never
a typed result with its working in a comment. WHEN THE SOURCE GIVES A
RANGE says a pick typed as a literal with its range in prose does not
meet it. The worked cases: Earth's dipole tilt, which IGRF-13 does
not print and which the store held at 9.6, a figure in no epoch of
the cited source; its rate; and the outer belt's peak, a midpoint of
the L = 4 to 5 band typed as a literal with the band in prose. Five
documents by Claude Fable 5.1 and Claude Opus 5 on 2026-09-21, each
tested against the checkers before the next was written; GPT 6
reviewed one round. Handle L-322.
v2.16 writes down how a stated uncertainty decides a figure count,
before L-322 Stage C2 builds the check for it. Rule 3 already said the
uncertainty decides and counting is the fallback, and the procedure it
was adopted from says to propagate; neither said how, and the checker
counts only. On Tony's instruction of 2026-09-20, "See the Skill on
significant digits", the magnetopause standoff was worked by the rule:
Shue's five coefficient uncertainties propagate to +/- 0.13 Earth
radii, which the reference page's single-number rule reports to
tenths, 10.3 -- the stored 10.25 was a figure too many. RULE 3 GAINS
THE CEILING, in five parts: which uncertainty is propagated (the
inputs', not a model's scatter about its data); show or cap for an
approximate relation; when propagation sets the ceiling and when
counting does; how to propagate (central difference, root-sum-square,
from full digits, independence stated with its bound, an implied
half-unit for a primary that states none); and how to report, with
the page's words kept apart from the log-scale measure this project
adds. RULE 1 gains the field form of an uncertainty, so a checker
reads a field and never prose. RULE 8 gains the ceiling check,
specified here and built at C2. Claude Fable 5.1 reviewed the text
twice before it was cut; its second look found that an earlier form
of the ceiling rule would have failed fifteen finished C1 rows, and
the rule now fails a row only for claiming more than its uncertainty
supports. Handle L-322.
v2.15 repairs the figure rules against the source they cite, after
Claude Fable 5.1's review of L-322 Stage C1 found the walk deciding a
rule inside one constant's comment. RULE 2 GAINS THE CONDITION IT HAD
DROPPED: a trailing zero after a decimal point is significant when it
falls within the source's reporting resolution, which is what the cited
page says and what makes 1500 m two figures rather than four. Without
it the rule was simply wrong, and the walk's invented alternative --
that a padded zero never counts -- was wrong the other way. RULE 3
GAINS a sentence it never had: a row may declare FEWER figures than its
inputs support when the relation is itself approximate, with the reason
in words on the row. Earth's Hill sphere is the case; it declared seven
and told the reader to report three. THE ASTM REFERENCE IS DEMOTED TO
AN ASIDE on Tony's ruling of 2026-09-19: E29 costs $86, so a rule this
project works from could not be opened by anybody in the loop, which
fails our own Access Standard; and its scope is conformance with
specification limits, which the orrery does not have. Two stale
examples are corrected. Handle L-342.
v2.14 writes down L-322 ruling (b), the read. It has been a ruling
since 2026-09-11 and lived only in the ledger, and a convention that is
not in the skill does not travel -- the protocol has recorded that
lesson three times. The Status Line gains The Read Field: a
"# Read: <page or table>, <date>, <reader>" line on a measured row
whose value is DRAWN in a published exhibit, or that feeds one. WHO
DOES THE READING IS DECIDED BY ACCESS, on Tony's ruling of 2026-09-19,
so the builder reads what it can open and names itself, a row only Tony
can open goes to him in a FILE and never as a list in chat, and a
source neither can open fails The Access Standard. A model's read
counts and the line says so; a read reconstructed from training is
worse than no read, because it stops the next reader from looking. The
Unit Field now points at constants_tokens.py, which owns the token
table, the RETIRED_TOKENS list and the "named number" marker, and names
"# Read:" among the fields a row's single slice visit writes. Rule 8's
enumeration names BOTH routes to a derived row -- its arithmetic and
its "# Derived:" line -- because a typed number carrying a
"# Derived:" note is a literal whose arithmetic lives in prose, and the
checker must still name it. The worksheet schema gains the "Read by"
column promised on 2026-09-11 and missed by 2.13. Handle L-322.
v2.13 settles L-322 (d), significant figures, on Tony's rulings of
2026-09-16. The Figure Count Is a Declared Field [QUALITY] joins
Report to the Figures You Have: a "# Figures:" line beside every
value, counted by the standard rules (fewest figures for products
and quotients, coarsest decimal place for sums and differences,
exact and declared numbers never limit a result), computed from the
primary inputs at full precision and rounded ONCE at the reporting
step, half to even. A Derived Row Stores the Figure Its Sources
Support [CRITICAL] is WITHDRAWN on Tony's word of the same day: a
rounded literal at rest is a rounded intermediate for every row that
chains from it, which is the error the procedure exists to prevent.
The store holds the derivation; the export rounds. The Status Line
gains The Unit Field, carrying L-322 ruling 1 into the skill, where
it had not travelled. Handles L-322, L-325, L-335.
v2.12 adds five rules from the L-321 cross-check round and one
carried from L-325's Gap. Worksheet Types gains the row-job
vocabulary the round actually ran -- [CITATION] and [DISCOVERY] --
with the schema that carries it, and two rules that depend on it: A
Negative Verdict Shows Its Search [CRITICAL], because UNSOURCED is
the one token pointing at no document anybody can open, and Route
the Effort Tier by Job Type [QUALITY], Tony's ruling of 2026-09-13.
The Access Standard gains a source names what was OPENED, after a
checker returned the right URLs under the wrong author names. Step 1
of the Review-Repair Protocol gains A Link Is an Object, Not Text
[QUALITY] and the three things the prompt must require. The roster
records that Gemini's fetching is tier-dependent, so L-276's
constraint is about the interface and the tier rather than the
vendor, and that a checker inside the Project is not independent for
a rerun. A Derived Row Stores the Figure Its Sources Support
[CRITICAL] joins The Store Carries the Verified Figure, closing the
Gap L-325 parked for this bump. Handles L-321, L-325, L-314.
v2.11 adds A Drawing Approximation Does Not Promote [CRITICAL],
directly after Measured Is the Goal, Declared Is the Fallback,
whose direction of travel it bounds. That section says a declared
value is promoted to a measured one as soon as it can be; this one
says a number that was never a value -- a shape typed into a
renderer because the render looked right -- has nothing to promote
and must not be moved into the store. Founding case: Earth's
magnetosphere, where a half ellipsoid with typed axes, a conic
eccentricity typed at the call site and a sweep cap the code itself
labels a MODE-5 KNOB were all candidates for promotion into
constants_new.py, and Tony refused it -- "we are not promoting
Mode 5 approximations." Handle L-306.
v2.10 adds The Store Carries the Verified Figure [CRITICAL] under
Report to the Figures You Have, which governed REPORTING and left
the stored value uncovered. Founding case: RADIATIVE_ZONE_AU held
0.7 beside its own comment saying it rounded 0.713 -- the store
recording that it was rounding, and rounding anyway, in a value
drawn on a public page. The rule is narrowed in the same breath
against the two cases it would damage: a pick from a range stays
a declared choice, and a visibility stylization promotes when the
physical value becomes drawable rather than for want of digits.
Tony's ruling, 2026-08-29, and the reason it is a SKILL rule and
not a decision: it resolves the same way next month, for a
different constant, in a different file. Handle L-258.
v2.9 moves the gate UPSTREAM, from serving to export, on Tony's
ruling of 2026-08-28. 2.8 put it where the harm lands; 2.9 puts it
where a check can still run. `provenance_scanner.py` exists only in
the orrery repo, and `gallery_cache_builder.py` lives in the gallery
repo and scores nothing, so a gate at serving sits downstream of the
last checker in existence and across a repository boundary. The WHY
is unchanged and the WHERE is separated from it explicitly, so the
gate cannot drift back on the reasoning that publication is where a
visitor is harmed. One section rewritten, nothing else touched.
v2.8 adds nine sections and revises four passages, from Tony's
rulings of 2026-08-27 and the two independent Mode 7 reviews of the
same date. The Gate Binds at SERVING [CRITICAL] moves the binding
point from drawing to publication. The Access Standard [CRITICAL]
makes reachability a precondition of a citation -- no paywalls.
The Status Line [CRITICAL] has each value declare its own provenance
state so the scanner reads instead of inferring. Measured Is the
Goal, Declared Is the Fallback [CRITICAL] carries the range rule.
The Exhibit Requirement [CRITICAL] makes a verdict without a
quotation UNVERIFIED. A Cross-Check Retires With Its Value or Its
Citation [CRITICAL], Observations Are Sourced Facts [CRITICAL],
Uncited Goes to the Ledger [QUALITY], and Examples Go Stale Like
Values [QUALITY] complete the set. Revised: the exhibit's reader,
Gemini's book access (demoted to lead generation), the
two-annotation criterion for V_CROSS_CHECKED (retired -- it measures
concurrence), and one stale worked example. Handle L-256.
v2.7 adds three sections from Tony's rulings of 2026-08-26, each of
them a gap this skill had rather than a refinement of something it
said. One Value, One Home [CRITICAL] states positively what No Shadow
Constants only prohibited, and extends it to prose and to dead code.
Report to the Figures You Have [QUALITY] had no home in any skill.
A Breadcrumb Must Not Cite [CRITICAL] records why an honest
"pending sourcing" note cannot carry its own references (L-253).
Founding case for the first two: Earth's four interior hover strings
typed their boundary figures for months beside a radius_fraction that
disagreed with them by up to 297 km, and nothing here covered it.
v2.6 adds The Two-Dispatch Rule [CRITICAL] under Model Roles in the
Competitive Pattern -- L-217, after a Mode 7 review prompt asked two
model legs to answer Part A before reading Part B, which neither could
do and neither answer could be distinguished on.
Source: project_instructions_v3_29.md Part 3 (Provenance Audit, Fetched vs
Recalled) + food insecurity build handoff + scanner source at HEAD. v1.1
adds the report domain-classification mechanics, the Review-Repair
Protocol (promoted from documentation/provenance_audit_handoff_v4.md),
and field notes from the F1 provenance-cleanup groundwork session (July
2026): the by-file/by-file-type report breakdown, a self-referential
scanning quirk, and a stale-audit-doc near-miss. v1.2 updates the
role-driven-inclusion bullet for L-163 Phase 3: a coverage gap is
resolved by tagging the module's own docstring, since ROLE_MAP is now a
regenerated mirror rather than a hand-maintained dict. MODULE_DOMAIN_MAP
and classify_domain() are unaffected and remain hand-maintained. v1.3
adds No Shadow Constants [CRITICAL]: local copies of constants_new.py
values must be deleted and replaced with proper imports -- a frozen copy
bypasses the citation chain and drifts silently, same failure class as
citing over recalled data. v1.4 rewrites Review-Repair Protocol step 2:
cross-checking is the competitive pattern (same worksheet, independent
models, Tony compares), not one model reviewing another's output.
v1.5 adds Model Roles (tested roles for Claude, GPT, Gemini, Fable in
the competitive pattern -- emerged from the Mars and constants_new.py
cross-check sessions, August 2026), two worksheet types (value
verification vs citation verification), the Cross-checked annotation
format, and the Batch Worksheet Workflow. v1.6 adds two rounds to that
workflow (blind source lookup and the Fable consistency audit), the
model-credit convention, the retirement of the `# Verified:` stamp
format, Geometry Constants as First-Class Claims, and three field notes
-- all earned in the L-156 Phase 2 Batch 1 cross-check and the Fable
shell-consistency audit, August 3-4, 2026. v1.8 adds Worksheet First,
Annotation Second (an annotation naming a worksheet that does not exist
is cite-to-clear in the annotation's own format) and the field note that
an evidence artifact is filed as received -- both earned August 10, 2026,
when a recovered worksheet proved an annotation true that the session had
already talked itself into calling fabricated.
v1.9 narrows The Goal State to the ACTIVE BUILD PATH gate Tony
ratified 2026-08-05 (L-184), keeping global Tier-1 = 0 as the
stated destination rather than the firing rule. The skill had
carried the retired global gate for a week; caught by Fable's
document-layer claim audit, finding F1, August 11, 2026.

v2.0 (August 12, 2026) replaced the annotation grammar: checker first,
optional ` -- <source>` clause, and the retired source-first order now
REFUSED as `legacy_source_first` rather than reconstructed. The old
order was ambiguous by construction -- a source carrying its own
publication year ate the check date, so the model name landed outside
the checker identity and two annotations by two DIFFERENT models read
as one checker written twice. All 134 lines were migrated. The
store-binding check lives in skills_index.py, which asserts that every
annotation example in every SKILL.md parses as the scanner reads it --
placed there because it runs at the moment a skill changes, which is
the moment the drift is introduced.

v2.1 (August 13, 2026) extends Worksheet First, Annotation Second with
two clauses about what the worksheet has to CONTAIN, and specifies the
worksheet table schema and verdict vocabulary at the prompt so the
evidence arrives usable. Earned August 12-13: two annotations in
constants_new.py credited a worksheet for checks it explicitly did not
perform, and one cited worksheet was prose a tool cannot read. Tony's
ruling -- we do not have to accept and interpret incomplete or
malformed answers -- is the second clause, and the session that
produced the evidence can be reopened to finish the job.

v2.2 (August 13, 2026) defines DERIVED, which v2.1 listed in the
verdict vocabulary without ever saying what it meant, and separates
two things the send-back rule had run together. A row that is
INCOMPLETE goes back to its originator. A row that is COMPLETE and
disagrees with the code is a FINDING and comes to conversation,
because the disagreement may be a convention mismatch rather than an
error in either place. Earned August 13 on the Eris and Pluto Hill
sphere rows, where checkers computing at semimajor axis disagreed
with code computing at perihelion and nobody had done bad
arithmetic. Tony's rulings: PARTIAL and APPROX return
unconditionally, and an adjudication is recorded with its reason so
the next run does not re-raise it.

The resident protocol carries the two governing principles as CRITICAL
gates: Fetched-vs-Recalled (a citation is a provenance claim that must be
TRUE; source-then-cite, never cite-to-clear) and Show the Envelope of the
Unknowable. This skill carries the working procedures and the scanner's
mechanics. If this skill and the resident gates ever seem to disagree, the
gates win -- flag it.


v2.4 (August 17, 2026) carries three changes, all earned the same day.
The annotation grammar now accepts a `.jsonl` or `.json` worksheet
reference as well as `.md` (L-204). The `.md` condition did two jobs:
it required the parenthetical to name a FILE rather than free prose,
which is the anti-gaming half of L-186 and does not move, and it
pinned the only worksheet format that existed in August 2026. The JSON
return format (L-202) landed 2026-08-17, and a returned verdict could
then be built, carried, filled, checked and routed -- and refused by
that one condition when somebody wrote it back into the code. Found by
an integration test, not by a reading. The Resolved Leg section is new
(L-200): a record-only leg saying which returned verdict caused an
edit. And The Visibility Convention is new (L-203), promoting a
one-off ruling about the request builder into the general rule it was
always an instance of.

v2.5 (August 18, 2026) adds Extend a Boundary Before Adding a Path,
the rule an external review proposed on 2026-08-18 and Tony adopted
the same day. It lives here rather than in the resident protocol
because it fires while a provenance feature is being designed, which
is when this skill loads. L-207, the citation prompt, was the first
item checked against it rather than assumed to pass.

The skill's v2.24 entry, moved here word for word on 2026-10-08 when
v2.27 made a fourth entry (L-418):
v2.24 settles L-395 with one new section, A Simple Error a Check Finds
Is Fixed and Reported. Tony's ruling, 2026-10-01: "simple errors such
as the Apophis naming discrepancy should be fixed and reported." It
says what counts as simple, that the fix rides the same patch and is
named, what comes to Tony instead, how a number in a served description
is sourced or removed, and how the rule sits beside The Braid.

A section withdrawn on 2026-09-16, moved here word for word on
2026-10-08 when v2.27 split the skill (L-418). It stood under Report
to the Figures You Have, after The Store Carries the Verified Figure:

### A Derived Row Stores the Figure Its Sources Support -- WITHDRAWN

Ruled by Tony on 2026-09-12 (L-325) and WITHDRAWN by him on 2026-09-16
as counter-productive under The Figure Count Is a Declared Field. The
rule said a derived row stores a literal rounded to its declared count,
so that a test could announce when an input moved. Under Rule 4 a
rounded literal at rest is a rounded intermediate for every row that
chains from it, and under Rule 6 the objection that earned the ruling
-- sixteen digits copied into a gallery config -- is answered at the
export instead. The stub stays so a reader who finds L-325 or the two
literal rows knows what happened to the rule.

## interactive-exhibit

Earlier: 1.8 | 2026-10-01, with Anthropic's Claude Opus 5.5, from
orrery @ feb5e369 and gallery @ 43993b49. v1.8 (L-395) records that a
body's name, Horizons id, description and NASA link on the website are
copies written by tools/mirror_objects.py from the orrery's object
list, and what the Solar System room's info panel shows.
Earlier: 1.7 | 2026-10-01, with Anthropic's Claude Opus 5.5, from
orrery @ 7a47269c and gallery @ c48f9a92. v1.7 (L-398, L-363, L-392)
records what the Solar System room serves and how it prints a
distance. A room that is not one body keeps its settings in the
config's top-level "rooms" section, with the words a visitor sees for
each drawer row. A computed distance prints by the larger of the drift
and JPL's own accuracy, served on the object as "position_accuracy";
a body with none says so in Tony's sentence. And the figures logic is
the second file moved out of interactive.html under L-338.
Earlier: 1.6 | 2026-09-28, with Anthropic's Claude Opus 5.5, from
orrery @ 2a7d26b9 and gallery @ 52da593c. v1.6 (L-345) adds three rules
under Provenance is part of the build, each what the L-345 gallery patch
built and Tony approved: where cutting a served AU to three figures
would round a tie, the served digits print in full and the hover check
names the case; the mirror writes a slot measured in another unit from
its row's "in"; and a shell may serve a radius_note, a sentence under
its radius line.
Earlier: 1.5 | 2026-09-28, from orrery @ 714293a9 and gallery @
2df02f3b. v1.5 (L-345) adds one rule under Provenance is part of the
build: a hover prints a number in a unit from the served "in" and never
converts a served number itself.
Earlier: 1.4 | Cut from gallery @ d9d7a48f (interactive.html,
gallery/arrival.js, gallery/feature_renderers.js, gallery/nav_cluster.js,
tools/store_writer.py, tools/exhibit_store_editor.py,
gallery_maintenance_run.py, documentation/smoke_arrival.js) and orrery @
e1a79f67 (LEDGER_CONSOLIDATED.md L-334, L-336, L-338, L-339) |
2026-09-19, with Anthropic's Claude Opus 5
v1.4 (L-334) carries what a room OPENS on and who may write the file it
is read from. Five rules: the arrival block is served, not coded; every
trace belonging to a served shell carries that shell's key, and one that
loses it is DRAWN rather than hidden; only two tools write
data/objects_config.json, and each has an allow list rather than a
refusal list; one check must read the file the browser actually fetches;
and logic that needs no browser lives in its own file, which is Tony's
ruling of 2026-09-18. Built through three pushes on 2026-09-18/19,
Mode 5 on Tony's phone between each.
v1.3 (L-332) carries the phone chrome as six rounds on Tony's phone left
it on 2026-09-15/16 (L-316 rounds 3 and 4, L-318 rounds 3 to 6). The
arrow cross's corner is set by one CSS rule and the method that moves it
says nothing about the corner; a drawer row has a finger-sized selection
target and GO on an unticked shell ticks it, amending L-267's G2 in that
one case; a line break inside a sentence is soft and the phone rejoins
it; on a portrait phone the text box has no arrow and sits mid-view; and
a phone tap reaches a shell's marker rather than its dots, through a
second Plotly rule read from v2.35.2. Step 4 gains the hover budget
suite. One new rule: hover text is written for the visitor -- Tony's
standing rule of 2026-09-16, the Register Rule pointed at what a visitor
reads (L-331). Version 1.2 described the chrome as rounds 1 and 2 left
it, which was five rounds stale when this was cut.
Earlier: v1.2 (L-316, L-318) records what the chrome gained after Tony's phone:
the nav cluster's four arrow buttons and their portrait placement, the
drawer label, and two Plotly rules the build found by reading v2.35.2's
source rather than recalling it -- a scene relayout carries the live
camera, and a hover box keeps its pointer only when it fits to one side.
Earlier: v1.1 (L-291) corrects what Earth step 3 made untrue and adds what its
close taught about carding. The page picks a room from an `EXHIBITS`
table now, not an `EXHIBIT === "<key>"` branch, and four places still
said branch: the anatomy's switch and class rows, step 3, and step
7's picker. Step 3 gains the driver rule the build found by running
the resolver; step 7 gains the check for an existing card and the
order Studio forces; the rename paragraph points at L-309, which
deferred it; one field note.
Earlier: v1.0 cut from gallery @ fc8d9fb3 (interactive.html,
feature_renderers.js, data/objects_config.json, gallery_maintenance_run.py,
tools/gallery_studio.py) and orrery @ a57e86b8 (LEDGER_CONSOLIDATED.md
L-260, L-267, L-278, L-282, L-288, L-289) | 2026-09-06
Written with Anthropic's Claude Fable 5.1 before the Earth exhibit, on
Tony's question "do we have a skill that defines how we build
interactives?" The answer was no; the Sun's pattern lived only as code
and as ledger history. Everything below was read from those files at
the pinned SHAs, not recalled.
Earlier: 1.9 | 2026-10-02, with Anthropic's Claude Opus 5.5, from
orrery @ b3cfc780 and gallery @ cfc53490, with gallery patches
patch_L404_1_rooms_in_store_editor_20261001.py and
patch_L363_9_room_step3b_drawer_20261002.py. v1.9 (L-405) writes down
what two builds of one session taught, sorted on Tony's review of
2026-10-02 into method rather than judgement. The sentence saying every
reader of data/objects_config.json ignores "rooms" was wrong and is
corrected. The store writer may change a rooms-section room's `drawn`
and `highlight`, and the editor lists rooms from both places a room can
live (L-404). The Solar System room's drawer is recorded as shared
chrome with four additions, with Tony's framing ruling -- where a body
is now, plus 20% (L-363 step 3b). And step 4 gains the headless recipe:
a room's real driver in CPython, the real page in jsdom with a stand-in
Plotly, and the other rooms compared before and after (tools/headless/).

## safe-file-editing

Source: project_instructions_v3_29.md Part 3 + Part 5 technical lessons;
v1.1 adds the delivery-format convention from a same-day incident (a
transactional patch silently never run; see Field Notes). v1.3 adds
Line Endings Are Not Content, earned when a patch aborted twice on a
CRLF working copy whose bytes were identical to the repo's. v1.4 adds
Fix In Passing, Report It, after a patch blocked itself on two Unicode
arrows that predated it by months, and Naming and Archiving a Patch
Script, an unstated convention 96 scripts deep that Tony had been
following alone. v1.5 adds Stamp What You Change (L-220), after Tony
observed that this project updates bodies more reliably than it updates
anchors, dates and module descriptions. v1.6 generalises that section to
every file type, because 1.5's only concrete example was a Python module
docstring and the rule's founding case was stale Markdown headers -- it
would not have fired on the files it was written for. v1.7 adds A Paste
Is An Unverified Transfer (L-223), which extends the delivery rule to
prose, markdown and ledger files -- every example in 1.6 was code, and
this project had been hand-editing a 579 KB ledger on that silence.
v1.8 (L-226) does two things, both from Tony's rulings of 2026-08-23.
It rescopes the Encoding Gate to say PROSE explicitly, because a
session read "delivered code" as excluding markdown and left 23
non-ASCII characters in a file it was already patching. And it adds
The Correction Does Not Travel, one scope out from Stamp What You
Change: that section governs the file the patch is editing, this one
governs the other files quoting the value it just changed.

## orrery-coding-conventions

v1.6 (L-249) makes the angular step in Marker Separation for
Near-Equal Radii an OUTCOME rather than a fixed 20 degrees, with 20 and
10 recorded as the two worked cases. Earned when Earth's upper mantle
moved to its sourced radius and its cross vanished under the crust's.
Source: project_instructions_v3_29.md Part 3 + Part 5 technical lessons.
v1.4 adds Marker Separation for Near-Equal Radii to the Single Info
Marker Pattern, earned when the chromosphere moved to true scale and its
marker landed one pixel from the photosphere's; and Harvest the
Conventions You Find, which is how this skill grows.
v1.5 (L-227) adds Hover Line Width Is a Convention, Not an Accident,
found by Mode 5 when a tooltip ran off the viewport: a hover string had
been wrapped at 72 characters in the SOURCE with no `<br>` on the
lines, and rendered as one 378-character run. Canonical Text Format
already governed `\n` versus `<br>` and said nothing about width.

v1.2 adds the conventions earned in the L-156 Phase 2 Batch 1 cross-check
and the Fable shell-consistency audit (August 3-4, 2026): the
visualization-constant-vs-range convention, the Hill sphere documentation
standard (including the measured per-body state, which does NOT yet match
the intended convention), the canonical `\n` direction for module _info
strings, dual-pipeline detail added to the shell dispatch section, and
layer-chain gap handling. Two field notes added.

## ledger-and-session-records

Sources: LEDGER_CONSOLIDATED.md header, ledger_index.py at HEAD, handoff
v28 (consolidation) and v29 (cleanup), food insecurity handoffs. v1.3
adds the Tony-action (do)/(decide) tag convention and its rollup rule,
surfaced during the L-163 build-prep session (July 24, 2026) when a
handoff's Tony-only to-do items were found scattered across its body
with no consistent tag, discovered only because a builder session
(Opus 5) had to hunt for them by reading the whole document. v1.4
rewrites the Codebase Tooling ROLE_MAP bullet for L-163 Phase 3: a new
module is classified by tagging its own docstring, not by hand-adding a
ROLE_MAP entry, because ROLE_MAP became a regenerated mirror that the
next module_atlas.py run overwrites. v1.7 adds Cluster the Tail by
Topic, Not by Age -- Tony's ruling of August 19, 2026, replacing a
by-age triage, after a measurement found 54 of 107 open items both
below RICE 3.0 and untouched for a month (L-215). v1.8 adds the
master plan to The Document Stack as a SEQUENCING authority rather
than a rung in the status ordering, with Tony's ruling that
bundling items to complete a planned step supersedes RICE order,
and extends the status rule from handoff-vs-manifest to any session
document contradicting a settled ledger decision (both L-221,
August 20, 2026). v1.9 (L-230) does two things to the Protocol and
Skills Change Log. It adds the FOURTH step to the binding rule -- a
skill bump also earns a protocol version-history entry, which is
Tony's observation of August 23, 2026 that three links of a
four-link chain were firing. And it corrects that section's own
opening claim, which still said the protocol's version history lives
in the ledger appendix five days after v3.41 replaced that appendix
with a pointer. v1.10 carries THREE changes from one session
(2026-09-06), which is itself the first of them. ONE SESSION, ONE BUMP
(L-296): a session does not ship two versions of one skill, so
everything it decides rides one version. The SECOND ANCHOR LINE for
relay partners with no resident layer (L-290), in the Anchor
Requirement section, with two forms and a read-back. And the master
plan restamps once per DESIGN BUILD (L-296) rather than at "key
junctures", which was not countable and so kept returning the judgment
to Tony. v1.11 (L-291) adds A Closing Item Re-homes Its Loose Ends:
before an item goes DONE, each thing its body records as not done gets
a home in an open item, or is struck with a reason. Three were found
riding inside closing items on 2026-09-10, one of them behind a pointer
to an item that never mentioned it. v1.12 (L-333, L-362; 2026-09-28,
with Anthropic's Claude Opus 5.5) changes The Document Stack: the master
plan is ONE document at two zooms, an executive summary and the body,
with the critical path inside the body as Section 5a, and the summary
is rewritten at every restamp. Its two companion files were retired
with the plan's v34. Tony's ruling of 2026-09-28: "i think we should
integrate these reports. the summary as an executive summary. the body
should keep its critical path section." The companions had restamped
with v19 and v20 and not with v21 through v33, because nothing tied
them to the plan's own cadence.

v1.13 (L-396; 2026-09-30, with Anthropic's Claude Opus 5.5) adds Where
We Are to The Document Stack: `documentation/WHERE_WE_ARE.md`, one page
written for Tony rather than for the work, rewritten in place inside
every session's ledger patch, with this session's changes marked and
the must-reads in italics. Tony, 2026-09-30: "i struggle to keep the
big picture. it's the old dilemma of loosing the forest for the trees."

The skill's v1.14 entry, moved here word for word on 2026-10-07 when
v1.17 made a fourth entry (L-422):
Earlier: 1.14 | Cut from palomas_orrery @ b3cfc780 (v1.14),
earlier @ 5db8bbe0 (v1.13), @ 2a7d26b9 (v1.12), @ 1ee1cc61 (v1.11), @ 50cbd2df (v1.10), @ 41c0b279 (v1.9), @ 3586970d (v1.8),
@ 434a712b (v1.7), @ 305b269 (v1.6), @ 3398970 (v1.5) | September 10,
2026, with Anthropic's Claude Opus 5
v1.14 (L-405; 2026-10-02, with Anthropic's Claude Opus 5.5) adds A Wrong
Sentence in a Skill: Bump Now, or Carry It, under the change log. A
session had to decide it for itself on 2026-10-01 (L-404); Tony's review
of 2026-10-02 sorted it as method, so the skill answers it now.

The skill's v1.15 entry, moved here word for word on 2026-10-08 when
v1.18 made a fourth entry (L-418):
Earlier: 1.15 | 2026-10-05, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 72e3b558. v1.15 (L-418) adds one paragraph under the change log, A skill
keeps three version entries, which writes down what this version does
to all six long skills. A contents list now opens the skill, generated from its headings, and
skills_index.py --check fails if the two disagree. Version history
older than the two entries below moved to
documentation/SKILL_HISTORIES.md. Both because a plain read of a
long file shows its start and end and leaves out its middle, where
the rules are (Tony, 2026-10-05).

## gallery-cache-builder

v1.4 adds Recovery from a failed swap: discard and re-run -- Tony's
operational rule of 2026-08-19, after a nightly run wiped the served tree
and the ~30 quarantine directories turned out to be the same mechanism
printing harmlessly every night since July 21 (L-216).
