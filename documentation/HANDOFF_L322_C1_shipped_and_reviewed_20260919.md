# HANDOFF -- C1 shipped and reviewed; the wide figures fix, then Stage C2

Built on orrery `c76fe01e539a15c3df641ed537bce5c80bccfc45`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `7ee912e592450b7fee6cde9befd115f599fed247`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Both anchors are the state AFTER everything below was pushed, read live
from both remotes on 2026-09-19.

**Type: BUILD.** Session of 2026-09-19, Tony with Anthropic's Claude
Opus 5, with a review partway through by Claude Fable 5.1.

**Continues from** `HANDOFF_L322_stages_A_and_B_20260919.md`. Its
companion contract,
`documentation/BUILD_MANIFEST_L322_earth_slice_20260919.md`, is NOT
replaced: sections 7 through 11 -- Stage D, out of scope, rules of
delivery, Tony's decisions -- are unchanged and still govern. Section 6,
Stage C1, is now done.

---

## READ THIS FIRST, before any provenance or store work

ONE SKILL WAS BUMPED IN THIS SESSION AND REINSTALLED BY TONY AFTER IT.
A reinstall lands in the account and stays invisible to the session that
makes it, so this session could not verify it and did not try.

    provenance-discipline    2.14 -> 2.15

CONFIRM YOUR LOADED COPY READS 2.15 before doing provenance or store
work. If it reads 2.14, that is the stale-skill gate and it stops the
task -- say so and ask Tony to reinstall, rather than working from what
loaded.

The protocol is v3.64 and carries the bump in one entry. What changed in
2.15 is small and load-bearing: **Rule 2 gained the condition it had
dropped** -- a trailing zero after a decimal point is significant only
when it falls within the source's measurement or reporting resolution --
and **Rule 3 gained a sentence** saying a row may declare fewer figures
than its inputs support when the relation itself is approximate. The
ASTM E29 reference is demoted to an aside; the open Wikipedia page is
the reference we work from.

---

## What this session did

**L-322 STAGE C1 IS DONE AND DEPLOYED.** The walk over the 29 Earth
constants that carried no fields, plus `KM_PER_AU` and `GM_SUN_SI`.
Measured at HEAD, not recalled: Earth rows carry unit 57 of 57, status
57 of 57, figures 29 of 57, and 12 carry a `# Read:` line. The 28
without figures are C2's magnetosphere rows. `CLOSED_SLICES` is still
`()`.

Five citation corrections came out of actually opening the sources, and
they are what the reading exists to produce. The rotation rate cited
IERS Table 1.1, which has no angular velocity in it -- it is Table 1.2.
The polar radius cited IERS as though that document tabulated one; it
does not, and it is re-homed to the NASA fact sheet which prints it.
Earth's GM was labelled TCB-compatible where the table's own footnote
says TCG. The IADC guidelines were cited as Rev. 3 (June 2021) and the
document is Revision 2, March 2020. And one drawn number moved: the
lower mantle from 5711 to 5710 km, because Ishii et al. (2018), open
access, gives the 660 km discontinuity as 660 +/- 10 km.

**TONY READ THE ONE ROW ONLY HE COULD OPEN.** The IADC guidelines,
section 3.3.2, imaged. The link was alive.

**L-341, THE DASHBOARD.** Seven groups instead of five, a Find box that
shows each match under its own group heading, and search on demand
rather than per keystroke. Closed in the ledger, with two rulings
recorded: that "what should I run now" is a question for this
conversation and not for the dashboard, and that the twenty checkers
under the maintenance runner were deliberately NOT re-sorted because
their alphabetical order is Tony's ruling of 2026-09-12.

**L-342, FROM FABLE'S REVIEW OF C1.** Four things, all fixed and pushed:
a live formatting defect, two figure counts, the skill bump, and the
visitor-facing note.

---

## The four findings, and what was done with each

**ONE. A DEFECT THAT WAS LIVE.** Earth's geocorona hover read "Radius:
1e+2 Earth radii". `fmtServed` used `value.toPrecision(figures)`, and
JavaScript switches that to exponent notation whenever the integer part
has more digits than the figure count. C1 declared the first figure
counts this store has ever carried, so it was the first time a served
value met the condition. **All fourteen gallery checks passed over it**,
because none of them read the numbers inside a hover. Fixed.

**The check built is not the check the review asked for, and the reason
is measured.** A check that fails on any hover containing exponent
notation was written first and run: it fails on TWENTY hovers that are
correct -- the Oort cloud's "2.00e+3 AU", Jupiter's main ring at
"2.01e-7", the Moon at "3.684e+05". A check with twenty standing
exceptions is not a check. What was built runs every served value
carrying a figure count through the renderers' own formatter. It was
demonstrated failing by restoring the old formatter.

**TWO. THE WALK DECIDED A RULE IN THE WRONG PLACE.** Meeting PREM's
`3480.0`, it wrote into that constant's own comment that a trailing zero
in a padded decimal place does not count. The skill said the opposite.
Both were wrong, and the cited page settles it on RESOLUTION. Tony's
ruling: implement the rules as the page states them.
`EARTH_OUTER_CORE_KM` 4 -> 5, `EARTH_MEAN_RADIUS_KM` 4 -> 7, both
inherited by their `_RADII` rows. One premise was also factually false
and the review caught it: the mean radius row claimed the NASA sheet is
padded to three decimals throughout, and the same block prints 3485,
5513, 20.4 and 11.186.

**THREE. THE HILL SPHERE DECLARED SEVEN FIGURES AND DISOWNED THEM** in
its own next sentence, so a visitor saw 234.6388 Earth radii. Now three.
The rule this needed did not exist and is now in the skill.

**FOUR. THE DISPUTED COMMIT, settled by the commits.** Orrery `4417217`
holds four files and none of the files a maintenance run always
rewrites. So Tony excluded nothing, as he said twice, and the run had
not been run. The builder's explanation -- that a file was left out of
the commit -- was a guess and was wrong, and the patch's own closing
text, which said nothing would change, is what made the run look
optional. **Worth keeping: a commit made without the maintenance run is
visible afterwards by the absence of the files the run always rewrites.**

---

## What the next session does, in order

### 1. The wide figures fix, and the check that would have caught it

**THIS IS THE FIRST TASK AND IT IS NOT STARTED.** Tony found it at the
window after C1 shipped: Earth's outer core still reads "3,480 km"
rather than "3480.0 km", although the store declares five figures, the
export carries five, and the cache serves five.

**The cause is a dispatch question, not a formatting one.** Only shells
served in Earth radii go through `fmtServed`. Shells served in
kilometres go through `kmAndAu` -> `fmtKm`, and `fmtKm` rounds with
`maximumFractionDigits: 0` unconditionally. So a declared count is
carried all the way to the last step and then ignored.

**Tony's instruction, 2026-09-19, is the scope:** "we need to ensure the
right significant figures are displayed here and elsewhere." That means
WIDE. `kmAndAu` has SIXTEEN call sites in
`gallery/feature_renderers.js`, across Jupiter's rings, Saturn's, the
Sun's shells and Earth's interior. A narrow fix would leave the same
fault in fifteen other places to be found one room at a time.

**The check built for finding 1 cannot catch this, and that is the
lesson to carry.** It tests the formatter, not which formatter each
branch reaches -- the leaf instead of the dispatch, committed in the
same session that quoted the rule about it. The new check must compare
what a BUILT HOVER contains against the declared count, not what the
formatter returns in isolation. It should be demonstrated failing on the
outer core before the fix goes in.

Call sites where a declared count exists and is currently dropped are
the shell and shell-set hovers; sites with no declared count must keep
their present behaviour exactly, and that has to be shown rather than
assumed.

### 2. Stage C2, section 6 of the manifest, unchanged

The 28 magnetosphere rows get their four fields. The five rows still
declaring the retired token `dimensionless` get real ones --
`EARTH_MAGNETOPAUSE_SHUE_A5`, `_A6`, `_A8`,
`EARTH_BOW_SHOCK_JELINEK_EPS`, `EARTH_BOW_SHOCK_JELINEK_LAMBDA`; the
gallery's live run already names four of them as NO UNIT, so the gallery
is pointing at where to start. The two magnetosphere standoffs revert
from rounded literals to expressions and leave
`constants_rows.TRANSITIONAL`. Then `CLOSED_SLICES = ("EARTH",)`.

**THE READ CHECK IS OWED BEFORE EARTH CLOSES, and it is still not
built.** The skill says a missing `# Read:` on an in-scope row inside a
closed slice FAILS, and no check does that. Fable raised it before C1
and again after. The agreed shape: the export gains two fields per row,
whether it has a read line and what its inputs are, and the gallery's
existing link check -- which knows which constants are drawn -- fails
when a drawn Earth constant inside a closed slice lacks one. The inputs
field is what covers the twelve rows that FEED a drawn row without being
linked by name. It must be demonstrated failing before `CLOSED_SLICES`
changes.

### 3. Stage D

Earth's pole moving into the store. Its own push, after C.

---

## Open items, and their state

    L-322  OPEN. C1 done and deployed. C2 and D remain.
    L-342  OPEN. Findings 1 to 4 are fixed and pushed. What remains is
           the wide kilometre-path fix, its check, and the geocorona's
           altitude line -- "631,436 km", six figures beside a
           one-figure floor, which PREDATES C1 and is a separate
           question about what an altitude derived from a declared
           floor should show.
    L-341  CLOSED. The dashboard. One unratified proposal in its block:
           the GUI behaviour test that found the "stars" gap lives only
           in the session that wrote it, and whether it joins the
           checkers is Tony's call.
    L-340  OPEN. The Mode 5 pass over the editor window; the
           smoke_arrival.js EXPECTED-list finding; and a Tony-action
           (decide) on whether the one-off config-write exception stays
           narrow.
    L-337  OPEN. A centre marker for bodies without shells. Tony's
           addition of 2026-09-19 is in the ledger; still open is where
           it comes from and what it says on hover.
    L-253  OPEN, and it gained something. Ishii et al. (2018),
           Sci. Rep. 8:6358, open access, gives the 660 km
           discontinuity as 660 +/- 10 km with six seismological
           studies behind it. That is a SOURCED figure for the
           variation L-253 has been holding as unsourced. It is NOT a
           second independent cross-check leg -- same research group as
           the 2019 paper -- so the Review-note's obligation stands.
           Recorded, not acted on.
    L-325  OPEN. Its (decide) falls due at the end of C2, when the
           standoffs revert.
    L-216  OPEN for the cause. The folder swap under OneDrive.

---

## Tony-action rollup

1. **(do)** File this handoff in the orrery's `documentation/`, commit,
   push. Give the next session this file, the build manifest and
   Fable's review, saying which is which.
2. **(decide)** Whether the dashboard's GUI behaviour test joins the
   checkers, on L-341.
3. **(decide)** Whether the one-off config-write exception stays narrow,
   on L-340.
4. **(decide)** L-325, at the end of C2.
5. **(do)** Pause OneDrive syncing before every cache build.
6. **(look)** Both rooms on the phone after each gallery push, and the
   Mode 5 pass over the editor window when there is time.

---

## Two things this session learned the hard way

**A SENTENCE IS NOT A LINE.** Both room panels are built from an array
of string fragments. Twice, the fragment anchored on was the first half
of a sentence that continued in the next fragment, so new prose landed
in the middle of it and went live in both rooms. An anchor that ends
without punctuation is the middle of a sentence, and the only way to see
that is to read the NEXT fragment before anchoring. The repair replaced
each note WHOLE rather than patching it, so the halves cannot come apart
again.

**A PATCH THAT SAYS "NOTHING WILL CHANGE" MAKES THE MAINTENANCE RUN LOOK
OPTIONAL.** The export stamps itself with a hash of the whole
`constants_new.py`, comments included, so a comment-only patch DOES move
it. The closing text of `patch_L322_12` said the opposite, having
measured the opposite earlier in the same session. A patch's closing
instructions are read as a prediction; when the prediction is wrong, the
step gets skipped.

---

Session written September 2026 with Anthropic's Claude Opus 5.
