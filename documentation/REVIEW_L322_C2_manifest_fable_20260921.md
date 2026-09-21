# Review -- the L-322 Stage C2 build manifest, before anything is built

**Built on orrery `b9cd48440a8879f7c79207dfc181bfaaf584caf4`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `06fdad8cc16da72d00e28c8066dbcbde7f590587`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both HEADs read live with `git ls-remote` on 2026-09-21 and both
repositories cloned there.** The first SHA is the orrery, the second is
the gallery. Both match the request. The manifest is not in either
repository; I reviewed the copy Tony carried.

**Type: REVIEW.** Written September 21, 2026 by Claude Fable 5.1, inside
Tony's Project. Reviews `BUILD_MANIFEST_L322_C2_magnetosphere_20260920.md`
by Claude Opus 5. Nothing was built and the manifest was not edited.

## Rule files I read

- Protocol v3.65: resident, in full.
- provenance-discipline 2.15 (installed copy reads 2.15, matches the
  table, identical to the repo copy): read IN FULL -- Report to the
  Figures You Have, The Figure Count Is a Declared Field Rules 1 to 8,
  The Store Carries the Verified Figure, The Read Field, Measured Is the
  Goal, A Drawing Approximation Does Not Promote. The rest NOT read.
- interactive-exhibit 1.4, gallery-cache-builder 1.6, gallery-assembler
  1.3, ledger-and-session-records 1.11, safe-file-editing 1.11: VERSION
  LINES ONLY, all match the table. From the ledger skill I also read the
  Anchor Requirement. I did not read the bodies, so findings below that
  touch those skills' rules lean on the manifest's account of them.
- Also opened: Wikipedia, Significant figures (fetched 2026-09-21);
  `DESIGN_L322_d_significant_figures_20260916.md` section on powers and
  Rule 3; `L305_gap1_read_record_20260911.md`; the rev2 brief section 3;
  `constants_new.py`, `test_derived_figures.py` (run), and
  `gallery/feature_renderers.js` around the two standoff hovers.

## What I re-measured, and what I accepted

Re-measured myself: the standoff (10.2518729724, agrees); each
coefficient's effect (0.090, 0.049, 0.012, 0.015, 0.082, agrees); the
combined 0.1326 (agrees); the km and AU values; the bow shock 13.5117;
every "After" string in section 6 (all agree); the figures checker's
output today (31 read, 15 OK, 16 not migrated, 1 no derived line,
agrees); that the renderer's bow shock recount leaves epsilon out and
prints `S.toFixed(2)` (agrees); that belt spans print `toFixed(1)`
(agrees).

Accepted as written: the closed-slice dry runs, the 78-link join count,
the mirror's behaviour on null entries, the RELABEL refusal, the 43-key
fixture, and everything about the cache swap.

---

## Findings

### 1. The propagated +/- 0.13 is the precision of the FIT, not of the magnetopause. The manifest never says which one the hover is claiming. -- **fix before the build; one part is Tony's**

Manifest 2.1, 4.2, section 6.

Shue's Table 1 uncertainties say how well the eight coefficients were
pinned down. Propagating them gives how well the MODEL'S AVERAGE surface
is known at the declared solar wind: +/- 0.13 Earth radii. The same
paper says real crossings sit 1.23 Earth radii (one standard deviation)
from that surface. That number is in the store
(`EARTH_MAGNETOPAUSE_SHUE_SCATTER_RADII`) and the manifest marks it "not
drawn" and walks past it.

This matters because Rule 3 gained a sentence two days ago, from my own
C1 review: a row may declare fewer figures when THE RELATION ITSELF is
approximate. Earth's Hill sphere was cut from seven figures to three
because the formula is off by about one percent. Shue's relation misses
individual crossings by twelve percent, and Jelinek's by five (0.69 on
13.5). The manifest does not say why the Hill sphere sentence applies
there and not here.

The page's own words already lean one way. The served bow shock text
says today: "what bounds this is the crossing scatter of 0.69 R_E".
Section 5.4 keeps that sentence and prints 13.5 beside it, which implies
+/- 0.05.

There is an honest argument for the manifest's choice. The hover names
the model and the declared conditions, so "10.3" can be read as "what
Shue's model gives", and that IS known to +/- 0.13. The scatter is then
a second fact about the real boundary, not an error bar on the first.
I think that reading is right. But it only holds if the visitor is told
the second fact. Today the magnetopause hover never mentions 1.23, and
neither hover prints its scatter as a line.

What I would change:
- The skill text in 4.0 says which uncertainty the route propagates
  (the stated uncertainties of the inputs) and says plainly that a
  model's scatter about the data is a different quantity, governed by
  the "relation itself is approximate" sentence and by Show the
  Envelope. This is method; it will recur at Jupiter and Saturn.
- Both scatter rows come into scope, get read lines, and each hover
  gains one line, for example "Real crossings scatter about 1.2 Earth
  radii around this." **The words are Tony's.** So is the choice between
  this and the blunter alternative, which is to let the scatter set the
  count ("10 Earth radii", "14 Earth radii"). I recommend the line, not
  the blunter count.
- The same class covers the outer belt's "28,701.615 km". It is not only
  ugly. It is a midpoint picked from a range known to one figure, shown
  to eight. "Exact for counting" describes the arithmetic, not the belt.

### 2. Two stated uncertainties in the manifest were computed from a rounded intermediate, and the manifest's own checker would fail them. -- **fix before the build**

Manifest 2.1, 4.2, 4.3a.

Full digits give +/- 845.9 km and +/- 0.00000565 AU. At two figures
those are 850 km and 0.0000057 AU. The manifest writes 840 and
0.0000056, which is what you get by converting the already-rounded
0.132. That is Rule 4 broken inside the document that enforces it. The
checker in 4.7 fails a row whose stated uncertainty differs from the
recomputed one, so these two `# Figures:` lines would go red on the
first run. The reported values (65,000 km, 0.00044 AU) do not move.

### 3. The checker's "move each primary by its uncertainty" does not say which way, and the answer changes. -- **fix before the build**

Manifest 4.7, 4.0.

The standoff is curved in a5. Moving every coefficient UP by one
standard deviation gives a combined 0.129, which rounds to 0.13. Moving
every one DOWN gives 0.136, which rounds to 0.14. The average of the two
(a central difference) gives 0.133. The manifest must name the central
difference, in the skill text and in the checker, or the row and the
checker can disagree about a number neither got wrong.

### 4. Independence is the right default, but the row should state the bound, because the reported place is not safe across it. -- **fix before the build (row wording only)**

Manifest 2.1, 4.3.

Coefficients from one fit are correlated; a1 and a2 almost certainly
are, since the fit only sees their weighted sum near Bz = 0. With no
correlations published, the true combined figure lies anywhere from
near zero up to the plain sum, 0.24. Under the 4.0 reporting rule the
tenths place holds only up to 0.158. So "10.3" survives the assumption
at 0.13 and would not survive it at 0.24. The kilometre line is safe
across the whole range. The row should say: independent by assumption,
plain-sum ceiling 0.24, tenths place holds to 0.158. Finding 1's scatter
line makes this less sharp for the visitor, but the row is a record.

### 5. The reporting rule is a fair reading of the page, and the log scale is OURS. The skill text must say so. -- **fix before the build**

Manifest 4.0. Request 3.1.

The page says only that the implied range should be "close to" the
measured one, and that going coarser loses "a lot of information". It
gives no measure. Closest-on-a-log-scale reproduces both of the page's
examples, and it is the sensible measure because implied uncertainties
step by factors of ten. A linear measure would keep the tenths place up
to +/- 0.27, which overstates precision five-fold, so log is also the
more honest of the two. But "log scale" and "ties go coarser" are this
project's formalisation, not the page's words. Version 2.14 went wrong
by restating the source with words changed and nobody able to see it.
The 4.0 text should mark the line: what the page says, then what we
add and why.

One more sentence is needed there. The text says a primary with no
stated uncertainty contributes its implied half-unit. It does not say
when the uncertainty route fires at all. I take the intent to be: only
when at least one input STATES an uncertainty; otherwise counting. That
needs writing down, because the two routes give different answers. For
the bow shock, counting gives 13.5 and the implied route would give
13.51.

### 6. The implied half-unit is sound, with one honest label. -- **note**

Manifest 4.7. Request 3.5.

The page sanctions it ("may be implied"). It does invent a number the
source never stated, so the row naming which primaries were implied is
the right safeguard, and the manifest has it. A half-unit is a full
half-width, not a standard deviation, so mixing it with Shue's standard
deviations slightly overstates. For Earth's radius it adds nothing
measurable. Leave it, and say in the skill text that it errs large.

### 7. The read check can miss one shape of row. -- **fix before the build**

Manifest 5.5. Request 3.8.

The shape matches what the rev2 brief records as agreed, and treating
every served link as drawn is the safe direction. It can fail on
`KM_PER_AU`. The gap: the walk follows the export's `inputs`, which
come from the row's EXPRESSION. A typed number whose arithmetic lives
in a `# Derived:` comment has empty inputs, so a walk reaches it, sees
"derived, needs no read", and stops with its measured sources never
examined. Rule 8 of the skill names exactly this shape. After C2 I
found none left in Earth, but the check should not depend on that. A
row whose status is derived and whose inputs are empty FAILS as "could
not be examined".

### 8. The bow shock cut angle: I take the manifest's side, with one condition. -- **Tony confirms**

Manifest 4.4. Request 3.7.

Declared is the honest status. The paper says its data reach "in the
range of" seven hours from noon; stopping the drawn curve there is this
project's choice, and the seven hours is the reason for the choice. The
alternative leaves a row listed as "not checkable" inside a closed slice
for good, which teaches everyone to read past that list. The condition:
the twin row, the magnetopause's 120 degrees, became declared on Tony's
ruling of 2026-09-14. Moving a row from measured to declared is a
demotion under a CRITICAL section of the skill. The manifest treats it
as method. I think Tony's earlier ruling covers it ("the same shape"),
but he should say yes once, in a line.

### 9. The four new rows are in bound, and section 12 contradicts them. -- **fix before the build; note for the ledger**

Manifest 2.2, 4.3a, section 12. Request 3.4.

The page prints these numbers, so they are inside the bound. They are
expressions, not copies, so they are not a second home for the value.
Tony's instruction that the store is the single source of truth already
decided the direction. But section 12 still lists "Any new constant" as
out of scope, six sections after adding four. It should say: no new
MEASURED or DECLARED constant; four derived reporting rows are added
under Tony's instruction of 2026-09-20.

For the ledger: this is two rows per shell. Every other shell that
prints km and AU will need the same pair, and section 11 already
records that class. Decide ONCE, before the next slice, whether the
answer is two rows per shell or the export converting every
`earth_radii` row itself from full digits. Do not decide it here.

### 10. Three figures beside two is right; the equals sign is the problem. -- **note, words are Tony's**

Section 6. Request 3.3.

I read the page's unit-conversion remark the same way Opus does. But a
visitor who multiplies 10.3 by Earth's radius gets 65,700, and the hover
says "= 65,000 km". Both numbers are honest and the "=" between them is
not quite. "about 65,000 km" costs one word.

### 11. Rounded numbers still in use: leave both for C2. -- **note**

Request 3.10. Drawing the magnetopause from the served 10.3 moves the
nose 319 km, a quarter of the fit's own uncertainty and a fortieth of
the scatter. Every shell is drawn from its served value and an exception
here would be a second convention. The AU-from-rounded-km class is
correctly recorded and not chased.

### 12. Smaller points. -- **notes**

- 5.2: if any entry is still `null` after the mirror runs, the patch
  must put the config back as it found it, not only refuse. Refusing
  after writing leaves four null entries in a served file.
- 4.1 token names: `inverse_exponent`, `flaring_exponent` and
  `shape_factor` name what the number is. `per_ln_npa` names how it is
  used and reads like a unit. It is a pure number; `log_pressure_coefficient`
  says so.
- The dipole tilt lead is handled correctly. Nothing to add.
- 3.6: yes, 2.16 must come before the build, and the session boundary is
  worth its cost: the checker implements the text and the walk writes
  the form. But do not cut 2.16 until findings 1, 3 and 5 are settled,
  because all three change its wording.
- Session count and order in section 9: sound.

## Tony's open question (2.2), a view only

I would allow the pointer-only entries. Writing a pointer and no number
keeps the rule that matters, which is that no number is typed into the
gallery config by hand. Teaching the mirror to create entries changes
one of only two sanctioned writers to save four lines, once. The cost
is that L-340's "one-off" exception is now used three times, and an
exception used three times is a practice. When Tony rules, L-340 should
record the narrowed form as the rule: a patch may add an entry that
holds a pointer and nothing else.

## For the ledger, one row per class

- **A figure count can describe the arithmetic and not the claim.**
  Model values beside a larger published scatter; declared picks from a
  coarse range printed at full arithmetic precision. Instances: the two
  standoffs, the outer belt, LEO's inner edge, the geocorona. (Finding
  1.)
- **A stated uncertainty computed from a rounded intermediate.** Rule 4
  applies to uncertainties as it does to values. (Finding 2.)
- **Unit-conversion rows multiply by shell.** Decide the mechanism once.
  (Finding 9.)
- **A derived row with empty inputs is invisible to any walk by
  inputs.** (Finding 7.)

---

Written September 21, 2026 with Anthropic's Claude Fable 5.1.
