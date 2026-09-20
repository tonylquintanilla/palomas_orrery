# Brief for the next design session: write the Stage C2 build manifest

Built on orrery `ee37cc1ff911d96e87fd5d714a456b53f2aef50e`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `1061ae4d9ad3b7a9b86b483b09db7f9cbd64eed2`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both HEADs read live with `git ls-remote` on 2026-09-20.

**Rules.** Inside Tony's Project the protocol (v3.64) and the skills
load on their own. Compare each loaded skill's version line with the
protocol's manifest table and STOP on a mismatch. This task fires
provenance-discipline 2.15, gallery-cache-builder 1.5,
interactive-exhibit 1.4, gallery-assembler 1.3 and
ledger-and-session-records 1.11. **In your first reply, name the rule
files you actually read.**

**Type: DESIGN BRIEF.** Written September 20, 2026 by Claude Fable 5.1
at the end of a long design session, for a fresh Claude Fable session.
Tony Quintanilla integrator. The session that wrote this had loaded its
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
should start from your manifest plus the rules, not from six documents.

C2 is the visit to Earth's 28 magnetosphere constants in
`constants_new.py`. Each gains a figure count and, where in scope, a
read line. Five of them trade the retired unit `dimensionless` for a
real one. The two standoff distances go back from typed numbers to
arithmetic. Then Earth is marked a finished slice.

## 2. Read these, in the orrery's `documentation/`, in this order

1. `BUILD_MANIFEST_L322_earth_slice_20260919.md` -- the parent contract.
   Sections 2, 6 and 9 matter most.
2. `HANDOFF_L322_C1_shipped_and_reviewed_20260919.md` -- what C1 did and
   what it left.
3. `REVIEW_L322_C1_fable_20260919.md` -- four findings from C1.
4. `BUILD_MANIFEST_L342_display_figures_20260920.md` -- the display fix,
   including the three rules a hover now follows.
5. `ASBUILT_L342_display_figures_20260920.md` -- how that fix was built
   and installed. **Not yet filed at `ee37cc1f`.** Ask Tony for it if it
   is still missing. Read section 5 with care.
6. `L322_earth_read_record_20260919.md` -- the form a read record takes.
7. `L305_gap1_read_record_20260911.md` -- a model's read of 14 of the 28
   magnetosphere constants, already done.

Enumerate what Tony uploads and read all of it from disk. Treat every
claim in these documents as a lead and check it against the repository.
This session once copied a handoff's claim about L-340 into a manifest
without opening L-340, and the claim was false.

## 3. What the C2 manifest must contain that the old section did not

**The read check, built and shown failing before Earth closes.**
provenance-discipline says a missing `# Read:` on an in-scope constant
inside a finished slice FAILS. No check does that. The agreed shape: the
export gains two fields per constant, whether it has a read line and
what its inputs are; the gallery's link check, which knows which
constants are drawn, fails when a drawn Earth constant or one of its
inputs lacks a read line. Confirm this shape against the code before
you specify it.

**A table of expected hover lines for four hovers.** The magnetopause,
the bow shock and the two radiation belts are held byte for byte today
in `documentation/fixture_hovers_cdfa74c3.json`, because their served
numbers have no figure count. C2 gives them counts, so all four hovers
change on the first C2 push and the fixture goes red. That is correct
behaviour. The manifest must give the expected lines, worked from the
rules by hand the way section 5 of the display manifest does, and must
tell the builder to re-record the fixture as the as-built's section 4
describes, naming which hovers moved and why.

**A correction to the as-built.** Its section 4 says the fixture goes
red when C2 gives the SUN's numbers a count. C2 does not touch the Sun.
The hovers that move are the four Earth hovers named above.

**The bow shock's reason in words.** Its standoff is the R0 coefficient
times pressure raised to a power. The renderer already drops a figure
there. The as-built says the constant then owes a reason in words, and
that C2 writes it. Check that against Rule 3 of the skill.

**The standoffs' revert.** Before they go back to arithmetic, confirm by
grep that nothing in the gallery still reads those two constants out of
the store. Three places in `constants_new.py` say
`test_derived_figures.py` recomputes them; that is false and C2 corrects
it. L-325's decide falls due when they revert.

**What C1 taught, as rules of delivery.**

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

## 4. The cache builder comes first, and why

The cache builder's folder swap has now failed five times (L-216). The
last two were on 2026-09-20 with OneDrive syncing paused, so pausing is
not a reliable cure. C2 needs at least two more cache builds.

The as-built's section 5 recommends three small changes. This session
agrees with all three and recommends they be built BEFORE C2, as their
own short manifest or as the first stage of yours:

1. Retry the `staging -> live` rename a few times with a short wait.
   Tony renamed the same folder by hand minutes after Python was
   refused, which shows the lock is brief.
2. Record the swap's outcome somewhere that survives a failed swap.
   Today the run's record is stranded inside the staging folder.
3. Keep OneDrive's conflict copies out of git: `solar-system (N)` and
   `<digits>-solar-system`.

Verified at gallery `1061ae4d`: `data/1260806133443-solar-system` is
tracked, 42 files, and published on the site. Whether to remove it is
Tony's decision.

**Moving the repositories off OneDrive is Tony's decision and his
answer on 2026-09-17 was "not at this time."** Do not press it. If he
asks, he wants the steps and the risks written out first.

## 5. Other things open, so they are not rediscovered

- L-340: the Arrival check compares against a fixed list of display
  names, so a correct edit in the store editor turns it red. Recorded,
  not built.
- L-340: whether one-off patches may write the config directly stays a
  narrow exception. Tony's decide. It has now been used twice.
- L-337: a centring marker for Earth's room. Open.
- Owed to interactive-exhibit's next bump: a hover prints a served
  primary where the store has one, and computes with figure propagation
  where it does not.
- Tony has not yet said which rule-correct numbers he wants shown
  shorter. Two candidates: the geocorona at 600,000 km twice, and the
  LEO inner edge at 6,578.1366 km.
- Stage D, Earth's pole moving into the store, follows C2.

## 6. First message to Tony

After the gates, tell him in a few plain sentences what you read, what
you measured, and whether the cache builder changes should go first.
Ask him one thing.

---

Written September 20, 2026 with Anthropic's Claude Fable 5.1.
