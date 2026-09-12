# Review reply -- the L-305 item 4 build, before it is run

Reviewed against orrery `a4ead59ac3f3f390710c99c4e3687d60b444447c`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `1f44673faf2acd32340bfdd4b524b6c8af5dd376`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
(the gallery IS involved -- see the first framing point).

Tony Quintanilla, PE | reply written by Claude Fable 5.1, inside the
Paloma's Orrery Project (protocol and skills resident) | 2026-09-12
Type: BUILD REVIEW REPLY (Mode 7, cooperative). No code, no diffs,
no ledger handles.

## What I read

- `PROJECT_INSTRUCTIONS.md` v3.57, resident, the named sections.
- `skills/provenance-discipline/SKILL.md` 2.11, `safe-file-editing`
  1.11, `orrery-coding-conventions` 1.8 -- all three installed copies
  match the manifest. Provenance was diffed byte-equal to the repo
  earlier today; the other two were checked by version line only.
- `patch_L305_magnetosphere_constants.py` and `test_status_lines.py`
  in full. `constants_new.py`, `earth_visualization_shells.py`
  720-860, `shell_configs.py` 2290-2310, `orrery_maintenance_run.py`,
  all at the SHA. A shallow clone of both repos at HEAD, grepped for
  every consumer of the two standoffs. In the gallery:
  `gallery_maintenance_run.py` (`parse_constants`, `check_store_drift`),
  `data/objects_config.json`, `feature_configs.json`,
  `coverage_index.json`, `gallery/feature_renderers.js`.
- I ran `test_status_lines.py` against the UNPATCHED store to see its
  output shape (2 of 86 rows carry a status line; it fails on
  `RADIATIVE_ZONE_AU`, which the patch fixes). I did not apply the patch
  and did not re-derive the request's measurements. I did recompute the
  two literals independently: 10.251872972379905 and
  13.511736110493397 both reproduce, and moving a1 by its +/- 0.10 or a5
  by its +/- 0.5 moves r0 by 0.090 and 0.076, so "the fourth figure is
  the last one supported" is right.

## Where the framing is wrong, first

**1. "No words change" is false, and it is the one thing that should
stop the button.** The bow shock hover in `earth_visualization_shells.py`
(line 849) says the value is drawn at the midpoint of Lugaz's 11-14 R_E,
and line 851 cites Lugaz as the source of the standoff. After the patch
the number in that sentence is 13.51, which is Jelinek at 2 nPa, not a
Lugaz midpoint. The hover would then quote a number and cite a paper
that does not give it -- wrong-but-cited, in the visitor's face, the
failure the whole store rebuild exists to remove. Line 796 (magnetosphere
hover, Lugaz as a standoff source) and `shell_configs.py` 2305
("Standoffs: Shue; Lugaz") have the same problem in milder form: Lugaz
is now a corroborating range, not a source of either standoff. The code
comment at 822-824 ("the store now holds the measured midpoint") goes
stale the same way. These are the L-321 magnetosphere strings, and
that slice may own the rewrite -- but a patch cannot land that turns a
true sentence false and leave the fix to another item. Either the
words travel with this patch or this patch waits for them.

**2. The gallery is involved.** `data/objects_config.json` (and the two
files the nightly builder derives from it, `feature_configs.json` and
`coverage_index.json`) carry the two standoffs as 10.0 and 12.5 with
`source` and `note` strings that repeat exactly the two claims this
patch retires: "Drawn at the midpoint of that range" and "Model form:
Farris & Russell (1994)". The store-drift check compares VALUES only,
so after the push it will report DRIFT on the numbers -- and say nothing
about the text, because it does not read it. The request says a
gallery patch is built against the new SHA; it needs to carry the
source and note strings, not just the values. Answer to question 10 is
therefore: yes, a consumer was missed, and it is the one Check All
Parallel Pipelines warns about by name -- in the other repository.

**3. The drift-parser premise behind question 1 is wrong.** The request
says a tanh expression "would be dropped silently and the pointer would
leave the drift check." Read `parse_constants`: an expression it cannot
evaluate is left out, and `check_store_drift` then reports the pointer
as NOT IN STORE, prints it under notables, and counts it as "could not
be examined." That is announced, not silent. It is also non-gating and
carries the wrong reason ("not a top-level constant"), so the decision
to type the literal still stands -- but for the honest reason: the row
would leave the CHECKED set, not the report.

**4. The request miscounts its own checker.** It says six rules fail
the run and two things are reported without failing. The docstring and
the code have eight failing rules and three reported items. A Report
Names Its Items: the request's count does not carry the axis it was
counted on. The rules themselves are fine; the sentence describing
them is not.

**5. Three of the four files are unstamped.** Stamp What You Change
says every file type, in the same transaction, and the patch prints
which stamps it updated. It stamps `constants_new.py` and prints that
it did. `earth_visualization_shells.py`, `shell_configs.py` and
`orrery_maintenance_run.py` are edited with no currency-block update.
The format-specifier change is small; the runner change adds a checker
to the maintenance run, which changes what that module does.

## The questions

**1. The magnetopause literal.** Honest, on one condition. Full float at
rest with a stated reporting figure is the file's own docstring rule
("held at full float precision and REPORTED to the significant figures
their least precise input supports"), and the row is `derived`, not
`measured`, so The Store Carries the Verified Figure does not bite --
that rule is about a measured value that rounds itself. Typing 10.25
instead would make the store differ from the expression the moment
L-322 swaps it in.

The condition: a literal that says "I am this expression" is a claim
nobody checks. Change a5 and the literal stays. That is a check that
cannot fail, at rest. Something that EXECUTES must recompute the value
from the stored coefficients and compare -- a pinned assertion in the
maintenance run, the same shape as the 55-pin test file that nobody ran
for ten days, except wired into the tool already in the routine. With
that, seventeen digits are the expression's own value, verified every
run. Without it they are seventeen digits.

**2. Derived from declared pending.** Right coupling, incompletely
declared. A derived row inherits its inputs' state by definition -- the
skill says it is never cleared on its own. So both standoffs are
pending too, and when L-314 lands they move; that is the point. The
gap: neither derived row says so. The backlog reads as three rows and is
five in effect, and the numbers visitors see are the pending ones. The
status line on each standoff should carry the pending state it
inherits, or the checker should report "derived rows with a pending
input" by name. The second is better -- it is the rule, computed, rather
than a hand-written echo that can drift.

**3. Naming.** The Table 1 indices are the right choice, because the
check a reader performs is "go to row a1 and look," and any English
name would have to be translated back to that. `A7_PER_NT` with a
negative stored value and the sign note is the one place a reader could
stumble, and the note handles it. The unit-suffix-free dimensionless
names with a `# Unit: dimensionless` line are consistent with L-322
ruling 1 and are not naming for a machine. Fine as written.

**4. The cut angle.** One measured row with the conversion on it, as
built. Hours to degrees at 15 deg/h is a unit conversion, exact by
definition, and the file already has two rows on that pattern
(`EARTH_GM_KM3_S2`, `RADIATIVE_ZONE_AU`). Storing 7 h and deriving
would make a `derived` row whose input is a literal 15 that is not in
the store, which the checker's own rule 7 would reject. One refinement
to the prose: the NUMBER is measured; the DECISION to stop the drawn
shock at the fit's support is a drawing rule, and the Note should say
that plainly so the row does not read as if the paper drew the cut.

**5. The checker.** No failing rule is too strict. The soft date is
right to stay soft while the skill's examples omit it. The un-gated
coverage count is right for L-322's walk. Three additions, in order of
value:

- Report, by name, derived rows with a `declared pending` input
  (question 2).
- Report, by name, `derived` rows whose right-hand side is a bare
  literal -- the class the magnetopause row founds, "derived by hand,
  not executed." Naming that class every run is what keeps the literal
  honest until the parser is retired.
- Check that a `declared pending` handle exists in
  `LEDGER_CONSOLIDATED.md`, which is in the repo. Rule 6 accepts any
  `L-nnn`; a handle that names no item is backlog that cannot be
  counted, which is the thing rule 6 is for.

One blind spot to record, not fix here: the parser attaches comments
only below a plain assignment or a parenthesised one. The skill says a
dict may carry a status line for the dict; a `# Status:` below a
closing brace is invisible to this checker and would pass unexamined.
None exist today (two dict rows, neither carries one). Worth one line
in the checker's docstring so the next session knows the edge.

**6. The dropped rule.** Agree. `INNER_CORONA_RADII` disproves the
strong form: a declared value may cite the source of the convention.
The narrower form is already in the checker as rule 8 -- the STATUS
LINE must not cite -- and that is the residual worth keeping. No
regex on the row's body can tell "cites the convention" from "cites a
number the paper does not give"; that distinction is the scanner's job
once it reads status lines, and it resolves by not scoring declared
rows on citation at all.

**7. `RADIATIVE_ZONE_AU`.** Better. The skill's own founding case for
The Store Carries the Verified Figure treats that row as measured (a
sourced figure, unit-converted), which is the same ruling as the cut
angle and the GM row. So the KIND is not in doubt by the skill's
precedent; only the rung was missing, and V_SOURCED matches the row's
Source-and-no-cross-check state. Leaving it malformed would have made
the new checker fail on its first run for a row this patch did not
touch, which is worse than a rung on a kind three precedents support.

**8. `:.4g`.** Right interim, and it entrenches nothing new. `:g` was
already a figure-count decision (six figures) at six sites; `:.4g`
makes the count match the store rows' stated reporting figure. The
migration L-322(d) faces is six sites either way. What it does NOT fix
is the words around the number (framing point 1); the specifier is the
smaller of the two changes those six quotes need.

**9. The interim render.** The geometry moving from 10.0/12.5 to
10.25/13.51 is acceptable -- the shells already read the store, so the
change is the store becoming right, not a new coupling. The hover text
is what makes it unacceptable as built. Fix the words and the interim
is fine.

**10. Parallel pipelines.** See framing point 2. In the orrery repo the
grep is complete: six quotes and two geometry reads, as the request
says. In the gallery repo: three served JSON files (one hand-edited,
two generated from it) carrying the values and the retired citations,
consumed by `feature_renderers.js`; and the drift check, which reads
values only. Five consumers across two repos, not two in one.

## Not asked, noted in passing

- `earth_visualization_shells.py` line 725 carries `# Verified: April
  2026 via Gemini fact-check`, the stamp the skill retired. Not this
  patch's, and it sits in a file this patch already opens. Class, not
  instance: retired stamps in the earth shells file.
- The frame claim in the new block header (Shue in aberrated GSM,
  Jelinek in aberrated GSE, both symmetric about the aberrated line) I
  did not verify against the papers. It reads as a read-record claim,
  and the read record is named on the a1 row; that is where it should
  be checkable.
- `EARTH_SOLAR_WIND_SPEED_KM_S` lands with an unwritten reason and no
  consumer at this SHA (nothing draws the aberration yet). Two absences
  on one row. Honest as written; the L-305 renderer is what gives it a
  consumer, and the reason should be written before that renderer
  reads it.

## The one decision

Do the hover words change in this patch, or does this patch wait for
L-321's strings? Everything else above is a checker addition or a
stamp, and none of it needs the button held.

Written September 2026 with Anthropic's Claude Fable 5.1.
