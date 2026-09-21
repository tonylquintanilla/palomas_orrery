# Brief for the next design session: write the Stage C2 build manifest (revision 2)

Built on orrery `ac397e52b890e76a0f795db466be095f0e48eaf2`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `a1a516cfbfe6c83fbd2c79c57a107feb0624ca27`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both HEADs read live with `git ls-remote` on 2026-09-20, and both
cloned there. The gallery will be one commit further on when you read
this: a one-character repair to `.gitignore`
(`patch_L216_6_gitignore_final_newline_20260920.py`). Read both remotes
yourself and name which SHA is which.

**This REPLACES `BRIEF_L322_C2_design_session_20260920.md`.** That
brief was written while the L-216 build ran and was anchored on the
state before it. Opus measured six things in it that needed correcting
(`ASBUILT_L216_cache_swap_20260920.md`, section 6). All six are taken up
here. Do not work from the first brief.

**Rules.** Inside Tony's Project the protocol (v3.65) and the skills
load on their own. Compare each loaded skill's version line with the
protocol's manifest table and STOP on a mismatch. This task fires
provenance-discipline 2.15, gallery-cache-builder 1.6,
interactive-exhibit 1.4, gallery-assembler 1.3 and
ledger-and-session-records 1.11. **gallery-cache-builder must read 1.6;
that obligation is carried from v3.65 and yours is the session that
discharges it.** **In your first reply, name the rule files you
actually read.**

**Type: DESIGN BRIEF.** Written September 20, 2026 by Claude Fable 5.1
at the end of a long design session, for a fresh Claude Fable session.
Tony Quintanilla integrator. The session that wrote this loaded its
skills on 2026-09-17 and could not see later reinstalls; that is one
reason the manifest is being written by a new session.

**How the work is divided.** Tony runs this as a relay. A Fable session
designs: it measures the pushed repositories, writes the build manifest,
and reviews what comes back. An Opus session builds from the manifest.
Tony carries documents between them and makes every judgment call. Tony,
2026-09-20: this "seems to work well. it is conservative with credits
and effective." Write for Tony in plain sentences, one request per
message. He is a retired professional engineer, not a programmer, and
often works from his phone.

---

## 1. The task

Write ONE build manifest for Stage C2 of L-322. It replaces the C2 part
of section 6 of `BUILD_MANIFEST_L322_earth_slice_20260919.md`. That
document stays filed as the contract C1 was built under. The builder
should start from your manifest plus the rules, not from eight
documents.

C2 is the visit to Earth's 28 magnetosphere constants in
`constants_new.py`. Measured at orrery `ac397e52`: all 57 `EARTH_`
constants have a unit and a status; 28 have no figure count, and those
28 are C2's. Each gains a figure count and, where in scope, a read
line. Five still declare the retired unit `dimensionless`:
`EARTH_MAGNETOPAUSE_SHUE_A5`, `_A6`, `_A8`,
`EARTH_BOW_SHOCK_JELINEK_EPS`, `EARTH_BOW_SHOCK_JELINEK_LAMBDA`. The two
standoff distances go back from typed numbers to arithmetic. Then Earth
is marked a finished slice.

**Closing Earth is a hard gate.** Inside a finished slice a gap FAILS
the run. `test_derived_figures.py` today names 16 constants NOT YET
MIGRATED. Three are Earth's and must all be migrated before
`CLOSED_SLICES` changes, or the closing commit goes red:
`EARTH_BOW_SHOCK_CUT_ANGLE_DEG`, `EARTH_MAGNETOPAUSE_STANDOFF_RADII`,
`EARTH_BOW_SHOCK_STANDOFF_RADII`. The other 13 are outside Earth and
stay named, not failed: `SOLAR_RADIUS_AU`, `LIGHT_MINUTES_PER_AU`,
`AU_PER_LIGHT_YEAR`, `CORE_AU`, `RADIATIVE_ZONE_AU`,
`CHROMOSPHERE_PHYSICAL_RADII`, `ROCHE_LIMIT_RADII`, `HAUMEA_RADIUS_KM`,
`SPEED_OF_LIGHT_M_S`, `SOLAR_MASS_KG`, `M_PER_AU`, `PARSEC_TO_AU`,
`SGR_A_DISTANCE_LY`. Run all three constants checkers yourself and
confirm what each would say about Earth once it is closed.

## 2. Read these, in this order

In the ORRERY's `documentation/`, all filed at `ac397e52`:

1. `BUILD_MANIFEST_L322_earth_slice_20260919.md` -- the parent contract.
   Sections 2, 6 and 9 matter most.
2. `HANDOFF_L322_C1_shipped_and_reviewed_20260919.md` -- what C1 did and
   what it left.
3. `REVIEW_L322_C1_fable_20260919.md` -- four findings from C1.
4. `BUILD_MANIFEST_L342_display_figures_20260920.md` -- the display fix,
   including the three rules a hover now follows.
5. `ASBUILT_L342_display_figures_20260920.md` -- how that fix was built.
   Sections 3 and 4 say what C2 meets in the renderer and the check.
6. `ASBUILT_L216_cache_swap_20260920.md` -- the cache swap hardening.
   Section 4 is a list of mistakes worth reading before you specify a
   patch. Section 6 is the source of this revision.
7. `L322_earth_read_record_20260919.md` -- the form a read record takes.
8. `L305_gap1_read_record_20260911.md` -- a model's read of 14 of the 28
   magnetosphere constants, already done.

In the GALLERY's `documentation/`: `smoke_display_figures.js` and its
fixture `fixture_hovers_cdfa74c3.json`.

Enumerate what Tony uploads and read all of it from disk. Treat every
claim in these documents as a lead and check it against the repository.
Two of this session's own errors came from skipping that. It copied a
handoff's claim about L-340 into a manifest without opening L-340, and
the claim was false. It described a folder as "42 published files that
serve nothing" and recommended deleting it without opening the files;
they were the only copy of 38 days of run history. A count does not say
what is there.

## 3. What the C2 manifest must contain that the old section did not

**The read check, built and shown failing before Earth closes.**
provenance-discipline says a missing `# Read:` on an in-scope constant
inside a finished slice FAILS. No check does that. The agreed shape: the
export gains two fields per constant, whether it has a read line and
what its inputs are; the gallery's link check, which knows which
constants are drawn, fails when a drawn Earth constant or one of its
inputs lacks a read line. Confirm this shape against the code before
you specify it.

**A table of expected hover lines for four hovers.** The Magnetopause,
the Bow Shock, the Inner Radiation Belt and the Outer Radiation Belt are
held byte for byte today in the gallery's fixture, beside 18 Sun hovers
C2 does not touch, because their served numbers have no figure count.
C2 gives them counts, so all four change on the first C2 push and the
fixture goes red. That is correct behaviour. The manifest must give the
expected lines, worked from the rules by hand the way section 5 of the
display manifest does. It must tell the builder to re-record the fixture
as the L-342 as-built's section 4 describes, naming which hovers moved
and why. (That section says the SUN's hovers move at C2. They do not.)

**The bow shock's reason in words.** Its standoff is the R0 coefficient
times pressure raised to a power. The renderer already drops a figure
there. The L-342 as-built says the constant then owes a reason in
words, and that C2 writes it. Check that against Rule 3 of the skill.

**The standoffs, stated correctly this time.** Both are on
`constants_rows.TRANSITIONAL` as typed numbers. Three places in
`constants_new.py` say `test_derived_figures.py` recomputes them. The
first brief called that false. Opus measured it more carefully: the test
does read both rows, and reports them NOT YET MIGRATED because neither
has a figure count. The comments describe a check that is wired and
waiting. L-322's ruling is that both revert to arithmetic at this
visit. When they do, they leave `TRANSITIONAL`, and those three
paragraphs need rewriting because the rows are no longer typed numbers.
Specify the rewrite for that reason. Before the revert, confirm by grep
that nothing in the gallery reads those two constants out of the store.
L-325's decide falls due when they revert.

**What C1 and the two builds since have taught, as rules of delivery.**

- A question about how to COUNT figures is never settled inside one
  constant's comment. It goes to Tony or to the skill.
- The maintenance run is run before every commit. A patch's closing
  text never says the run is optional or that nothing will change. A
  commit made without the run shows afterwards by the absence of the
  files the run always rewrites.
- Anchor a text edit on a whole sentence. Read the next fragment first.
- Any check that reads what a visitor sees builds from the served cache,
  `data/solar-system/coverage_index.json`, not only from the config.
- A long list of numbers does not go in chat. Tony's reading list is a
  file with the link, where to look, and the number to expect.
- A guard compares CONTENT, not raw bytes. Git stores LF and Tony's
  working copy may hold CRLF for the same file.
- Nothing in the cache tree is removed with a plain `shutil.rmtree`.
  OneDrive marks those folders read-only; gallery-cache-builder 1.6
  says what to use.
- A file a patch appends to must end with a line break afterwards.

## 4. The cache builder: done, and what C2 should expect from it

The three changes the first brief recommended are built and pushed
(gallery `d0317aa3` and `a1a516cf`, orrery `d426ec00`; skill 1.6,
protocol v3.65). Each rename in the swap is retried for about fifty
seconds. A swap that still fails puts the old cache back, so the working
copy is never left without a served cache. Every run that reaches the
swap writes one line to `data/cache_swap_log.jsonl`. The 42 run records
from the stray folder are kept at `documentation/cache_run_history/` in
the gallery, and the stray folder is gone.

**Not yet proven.** No real lock has met the new code, and at
`a1a516cf` the swap log does not exist yet because no build has run
since. Each of C2's cache builds will add a line. A line with more than
one attempt and outcome `ok` is the first real evidence. The C2
manifest should tell Tony to pause OneDrive syncing before each build,
note the time he paused, and look at the last log line afterwards.

Tony checked `solar-system (1)`, `(2)` and `(3)` on his own machine on
2026-09-20 and found all three empty. They are ignored by git and he may
delete them.

**Moving the repositories off OneDrive is Tony's decision and is
undecided.** L-216 holds the analysis. His ruling on 2026-09-20 was to
harden the swap "and take it from there as needed." Do not press it. He
also raised moving the project to Linux; this session's view was that
the cause is OneDrive, not Windows, and that a folder move on the same
machine would be the smaller step if one is ever needed. That too is
his to raise again, not yours.

## 5. Other things open, so they are not rediscovered

- L-340: the Arrival check compares against a fixed list of display
  names, so a correct edit in the store editor turns it red. Recorded,
  not built.
- L-340: whether one-off patches may write the config directly stays a
  narrow exception. Tony's decide. It has been used twice.
- L-337: a centring marker for Earth's room. Open.
- Owed to interactive-exhibit's next bump: a hover prints a served
  primary where the store has one, and computes with figure propagation
  where it does not.
- Owed to the next protocol bump that touches Stale Skill = Stop:
  measured on 2026-09-20, a running session's mounted skill copy stays
  at the version it started with, while the project instructions in its
  context DO refresh. So a long session can see a manifest row it cannot
  match. That is expected, not a failed reinstall.
- Tony has not yet said which rule-correct numbers he wants shown
  shorter. Two candidates: the geocorona at 600,000 km twice, and the
  LEO inner edge at 6,578.1366 km.
- Stage D, Earth's pole moving into the store, follows C2.

## 6. First message to Tony

After the gates, tell him in a few plain sentences what you read and
what you measured. Ask him one thing.

---

Written September 20, 2026 with Anthropic's Claude Fable 5.1.
