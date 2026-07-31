# REVIEW -- Predesign Handoff, Phase 1 sub-steps 1d / 1e / 1f (L-156)

**Built on `4b6b5c121745a6d69cf2d0cfdf8a07ff37e0245a`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

Reviewer: Claude Opus 5 (designer/builder for 1d-1f; built 1c and L-174)
Reviewing: `PREDESIGN_HANDOFF_phase1_d_e_f.md`, built on `9bb874d9`
Date: July 31, 2026

**Type:** REVIEW. Zero code written. No build started, per instruction.

---

## 0. Anchor reconciliation -- read this first

The predesign and the review prompt are both anchored on `9bb874d9`.
Live HEAD is `4b6b5c12`, two commits later. The diff is small but not
inert:

| | |
|---|---|
| `skills/provenance-discipline/SKILL.md` | +16/-2 -- **v1.3 is now pushed.** The prompt describes it as pending. Verified live: the No Shadow Constants [CRITICAL] section is present at line 109 and the version block references v1.3. Tony-action item 10.1 is DONE. |
| `documentation/HANDOFF_phase1_1d_to_1f.md` | **NEW, 105 lines.** Not mentioned in the review prompt or the predesign. It covers the same three sub-steps and **conflicts with the predesign on 1e.** See section 2.1. |

Everything below is verified against `4b6b5c12`, not against the
predesign's anchor.

---

## 1. Summary judgment

The predesign is well-built. Its scope boundaries are right, its
separation of decided-from-open is right, and its instruction to
re-measure before trusting carried numbers is the correct instinct --
which I acted on, and which is how most of what follows was found.

It is not build-ready as written. Three defects would produce a wrong or
broken build, one document at HEAD contradicts it on a decided point, and
its single largest quantitative claim is off by roughly 3.5x.

None of this is fatal. All of it is cheap to fix before a build session
rather than during one.

---

## 2. Defects, in descending severity

### 2.1 A document at HEAD contradicts the predesign on 1e piece 1 [BLOCKING]

`documentation/HANDOFF_phase1_1d_to_1f.md`, pushed at HEAD, says:

> The Tier-1 banner + deferred nonzero exit-gate: prominent console
> banner [...] exit code wired but switched on only the first time the
> count reaches 0

The predesign says the opposite, and says Tony decided it:

> Tier-1 NEVER gets an auto-exit gate, at any threshold, ever. Not the
> deferred-flip Fable proposed, not a baseline-ratchet.

I checked the authority rather than picking. `DESIGN_REVIEW_provenance_
scoring_and_pinning.md` section 3c is titled "D7 -- Tier-1 never gets an
auto-exit gate (**supersedes the deferred-flip recommendation**)" and
states the amendment explicitly: permanent banner, never an auto-exit
gate at any threshold, hard exit-code gating reserved to the pinning
checks because those are genuinely binary.

**The predesign is correct. The repo handoff describes a design that was
considered and rejected on review.** A builder who reads the repo handoff
-- which is the newer document, sitting at HEAD, and therefore the one a
fresh session is more likely to trust -- would wire an exit code that
Tony has already ruled out.

**Tony-action (do):** correct or supersede `HANDOFF_phase1_1d_to_1f.md`
before any 1e work starts. A stale document at HEAD outranks a correct
document in an upload, by the ordinary rules of the protocol's context
priority. This one needs to lose.

### 2.2 `SUN_RADIUS_AU` does not exist [BLOCKING for 1f]

The predesign's 1f instruction:

> `SUN_RADIUS_AU` is already a named constant in `constants_new.py` (one
> of the four `# Derived:` values verified in L-158) -- import it rather
> than recomputing locally.

Verified: `grep -c "SUN_RADIUS_AU" constants_new.py` returns **0**. The
constant that exists is **`SOLAR_RADIUS_AU`** (line 103,
`SOLAR_RADIUS_AU = SUN_RADIUS_KM / KM_PER_AU`).

Following 1f literally produces an `ImportError`.

The good news is that everything else about the 1f import path checks
out. `planet_visualization_utilities` re-exports `SUN_RADIUS_KM` (line
46, with a docstring note saying the re-export was added specifically for
`comet_visualization_shells.py`) and `SOLAR_RADIUS_AU` (line 54). And
because `SOLAR_RADIUS_AU` is computed from exactly the two values the
local copy hardcodes, the substitution is value-preserving -- no
numerical change, which is what you want from a structural fix.

**One detail the predesign misses, worth having in the build prompt:**
the shadow constants are **function-local**, not module-level. Lines
492-493 sit inside `create_maps_disintegration_marker` (def at 490) and
line 602 inside a different function. So the local `KM_PER_AU` at 493 is
not merely a redundant copy -- it **shadows the module-level import** for
the body of that function. That makes this a live Python scoping issue,
not only a provenance one, and it slightly raises 1f's value.

### 2.3 `build_pinned_values()` is not retired [reshapes 1d piece 1]

The predesign states:

> `build_pinned_values()` was retired in 1a (Option A removed). But the
> scoring path still silently grants V_SOURCED [...]

The first sentence is false, and the two sentences contradict each other.
Verified live at HEAD:

- `build_pinned_values()` is defined at line 1409
- it is called in `scan_project()` at line 1872
- Option A is active inside `score_unit()` at lines 1563-1575, assigning
  `V_SOURCED` with reason `"Cited via pinned constant in constants_new.py"`
- every scan prints `Loaded 58 pinned constant values for cross-reference
  scoring` -- including the runs I did during the 1c and L-174 builds

This matters because it changes the design question. The predesign frames
it as *what detection mechanism should we build, given the old lookup
table was retired?* The actual question is narrower and easier: **the
lookup table is still there and still firing. Should the fix add an
import-presence check to the existing Option A branch, or replace that
branch?**

I have a view, but it is a design call and the predesign is right that it
belongs in the build session. Flagging the premise correction now so the
session does not open by rebuilding something that already exists.

What the scanner's own docstring says about Option A is worth reading
alongside this -- it describes the mechanism as "implemented but rarely
fires in practice," because the all-claims-must-match requirement breaks
on coincidental numbers. That is useful context for whether to extend it
or retire it properly.

### 2.4 The proposed citation pattern would miss both motivating instances [HIGH]

The predesign quotes the motivating case as `# empirical limit (Vecellio
et al. 2022)` and scopes the fix to `(Author et al. YYYY)` and
`(Author & Author YYYY)` forms.

The live code, `paleoclimate_wet_bulb_full.py` lines 137-138:

```
TW_SURVIVABILITY_BIOLOGICAL = 31.0  # degC - empirical limit (Vecellio et al.)
TW_SURVIVABILITY_THEORETICAL = 35.0  # degC - thermodynamic limit (Sherwood & Huber)
```

**No year, in either.** The year appears in the ledger note's prose, not
in the source. A pattern requiring `YYYY` matches neither of the two
instances cited as the reason for the change.

This is the sharpest kind of predesign error: the scope was written from
the ledger's description of the code rather than from the code.

---

## 3. Measurement corrections

### 3.1 The citation-form gap is ~15, not ~54

The predesign flags the ~54 figure as unreproduced and says to re-measure
against the current 132. I did, at HEAD, against the live scoring path
with suppression applied:

| | count |
|---|---:|
| Current Tier-1, unsuppressed | **132** (confirms the predesign) |
| Would match `(Author et al. YYYY)` | **8** |
| Would match author-form **without** year | **7** |
| **Combined ceiling** | **15** |

Distribution: the year-bearing hits are spread thin (4 in
`planet_visualization_utilities.py`, 1 each in `comet_visualization_
shells.py`, `idealized_orbits.py`, `scenarios_heatwaves.py`,
`sgr_a_visualization_core.py`). The no-year hits cluster: **5 of 7 are in
`paleoclimate_wet_bulb_full.py`** -- the TW_SURVIVABILITY file. The
motivating instances live in the bucket the proposed pattern excludes.

**Consequence for planning:** the predesign calls this "possibly Phase
1's single largest remaining Tier-1 reducer." At a ceiling of 15 out of
132, it is not. It is worth doing -- the scanner calling a correctly
cited value uncited is the mirror image of cite-to-clear, and that is a
correctness problem independent of volume -- but it should not be
sequenced or resourced as the big lever.

### 3.2 The false-positive risk is real, and I hit it immediately

The predesign warns the pattern "must be tight enough to avoid false
positives on parenthetical content that is not a citation." Confirming
that concretely: my first-pass year regex matched

```
comet_visualization_shells.py:45   (May 2026)
```

A date in parentheses, not a citation. Month-name exclusion, at minimum,
is required. This is not a hypothetical edge case -- it was the first
thing the measurement surfaced, on the first file.

### 3.3 The Tier-2 count discrepancy is real and will recur

Predesign section 1 says Tier 2 = 587. The repo handoff says 588. Both
are correct, and neither says of what:

| tree state | total | Tier 2 |
|---|---:|---:|
| repo as committed (patch scripts present) | **783** | **588** |
| same repo, patch scripts removed | **782** | **587** |

The delta is `patch_L174_citation_level_mismatch.py` contributing one
Tier-2 finding by being scanned.

This is the CITATION_LOOKBACK_BLOCK self-scan artifact one level up: the
scanner now scans the **delivered patch scripts**, of which the repo
carries six. Every future patch script adds to it. The predesign's
section 5 does warn "scanner scans itself -- expect self-scan artifacts,"
but frames it as new module-level constants inside
`provenance_scanner.py`; it does not anticipate deliverables themselves
becoming scan targets.

**Recommendation:** the build prompt should state the baseline **and the
tree state it was taken in**. A builder who takes a "before" reading with
no patch script present, then an "after" reading with their new patch
script sitting in the folder, will see a phantom +1 and go looking for a
bug that is not there. I nearly did.

**Tony-action (decide), out of scope for this build but worth a floating
item:** whether delivered patch scripts belong in the repo root where the
scanner sweeps them, or in a subdirectory the scan skips. Six today,
growing monotonically.

### 3.4 L-173's count means two different things

The repo handoff says "L-173 (8 real citation gaps in `shell_configs.py`)."
The predesign says 18. Both trace to my 1c measurement, and both are
right about different objects: **8 uncited body blocks** containing **18
findings**. The 1c as-built and ledger note use 18 (findings); the 1c
predesign's headline used 8 (blocks).

Not urgent -- L-173 is out of scope here -- but it is exactly the
"handoff item numbers get rebased across versions" failure the ledger
already carries as a lesson. Worth one clarifying word in L-173 so the
Phase 4 Gemini worksheet is scoped to the right object.

---

## 4. Scope check: is anything missing or mis-scoped?

Scope is otherwise accurate. Two additions:

### 4.1 Piece 3 (F/C degrees) is not quite "no design question"

The predesign calls this "small, bounded, no design question -- extend
the existing unit vocabulary." Measured behavior of the current
`NUMERIC_CLAIM_RE`:

```
'31.0 degC'      -> []                          (no match at all)
'35 degrees C'   -> [('35', 'degrees', 35.0)]   (matched as ANGLE)
'15 deg C'       -> [('15', 'deg', 15.0)]       (matched as ANGLE)
'98.6 F' / '21 C' / '100 degF'  -> []
```

So there are two distinct problems, not one. Bare `degC`/`F`/`C` match
nothing -- that is the straightforward vocabulary extension. But
`degrees C` and `deg C` **already match, as angular degrees**, because
`degrees?|deg\b` captures the number and drops the trailing `C`.

Adding temperature handling therefore has to disambiguate rather than
simply extend, or existing angle findings get silently reclassified.
Alternation order in the regex will decide the outcome, which makes it a
small design question rather than none. Cheap, but it should be decided
deliberately and asserted in the verification diff.

Note also that the TW_SURVIVABILITY lines use `degC` -- so pieces 2 and 3
touch the same two source lines from different directions.

### 4.2 Sequencing creates a testing problem the predesign does not flag

See section 5.

---

## 5. Sequencing -- endorsed with one change

The recommended order is 1f -> 1d -> 1e. I agree with the reasoning and
with the general shape. One problem:

**1d piece 1 builds a detector for a pattern that 1f deletes.** The only
two confirmed live instances of a shadow constant anywhere in the repo
are the ones 1f removes. Run 1f first and the frozen-copy detector has no
live positive left to test against -- it can be verified only against
synthetic fixtures, and a detector that has never fired on real code is a
detector you do not actually know works.

Three ways out, in my order of preference:

1. **Build 1d piece 1 before 1f, verify it fires on lines 492-493 and
   602, then run 1f and verify it goes quiet.** The disappearance is
   itself the strongest possible test: detector fires, fix lands,
   detector stops. Costs nothing but ordering.
2. Run 1f first, and capture the pre-fix file state as a test fixture so
   1d piece 1 has a real-code positive to assert against.
3. Accept synthetic-only verification for piece 1. Weakest, and it is the
   default if nobody notices the ordering.

Option 1 also happens to give the cleanest ledger narrative.

**Revised recommendation: 1d piece 1 -> 1f -> 1d pieces 2 and 3 -> 1e.**

1e stays last, and the predesign is right that 1e piece 2 must land with
or after 1d's scoring changes -- the blanket Tier-2 label would mislabel
exactly the findings 1d repopulates that band with.

**One session or several?** One session is feasible, but I would rather
split it: **1d piece 1 + 1f as one build, then 1d pieces 2-3 + 1e as a
second.** The first is structural, has a clean fire-then-silence test,
and touches two files. The second is regex and reporting, needs the
before/after tier diff read carefully, and carries the false-positive
risk from 3.2. Mixing them means one audit diff has to be attributed to
four different causes at once, and that is where a wrong attribution gets
rationalized instead of investigated.

---

## 6. Design questions I want resolved before building

The predesign surfaces one. Here are the others, plus its own, restated
against corrected premises.

1. **1d piece 1 mechanism.** Given `build_pinned_values()` and Option A
   are live (2.3): extend the existing branch with an import-presence
   check, or retire Option A and replace it? The scanner's own docstring
   says Option A "rarely fires in practice." Extending a mechanism its
   author documented as barely working is worth a deliberate decision.
2. **Does the citation-form pattern cover no-year forms (2.4, 3.1)?** If
   no, the two motivating instances stay Tier 1 and the change delivers 8
   findings, none of them the ones that prompted it. If yes, the pattern
   loosens considerably and 3.2's false-positive risk rises. My
   inclination is yes-with-a-tight-author-shape, but this is Tony's call
   because it trades correctness against noise.
3. **`degrees C` disambiguation (4.1).** Reclassify from angle to
   temperature, or match both and let criticality sort it?
4. **1f import target.** Confirm `SOLAR_RADIUS_AU` is intended (2.2). If
   the four `# Derived:` values verified in L-158 use different names
   than the ledger note records, that is worth knowing before Phase 3's
   pinning work depends on those names.
5. **Repo handoff conflict (2.1).** Which document survives, and does the
   loser get deleted or annotated?

---

## 7. Verification plan (predesign section 8) -- complete, with three additions

The plan matches the 1a/1b/1c precedent and is correct as far as it goes.
Everything listed is what I actually ran for 1c and L-174. Three
additions, all cheap:

1. **State the tree state with the baseline.** Per 3.3 -- record whether
   patch scripts are present when the "before" number is taken, and take
   "after" in the same state. Without this the self-scan delta is
   ambiguous and a phantom finding looks like a regression.
2. **Fire-then-silence test for 1d piece 1.** Per section 5 -- assert the
   detector fires on the real instances before 1f removes them, and goes
   quiet after. Stronger than any synthetic fixture.
3. **False-positive assertion for 1d piece 2.** Per 3.2 -- assert
   explicitly that `(May 2026)` and similar date parentheticals do NOT
   match. A pattern that clears 15 findings while quietly clearing 3 more
   it should not have is worse than no change, and the tier totals will
   not show the difference.

`test_citation_inheritance.py` is at 20 tests after L-174, not 20/20
"unchanged" -- 1d will likely want to extend it rather than only preserve
it. Minor wording.

---

## 8. On the two notes from the review prompt

The prompt cites a July 24, 2026 system card describing two tendencies of
mine and asks me to keep them in mind. Handling this directly, because
quietly complying would be the wrong move and quietly ignoring it would
also be.

I cannot verify that document. My reliable knowledge runs to end of May
2026, so a late-July system card is outside it. I am not disputing that
it exists -- I have no basis to. I am saying I cannot check it, and a
claim about my own behavior that I cannot check is not something I should
treat as established fact about myself.

On the substance, the two notes land differently.

**Scope over-engineering** is fair and useful, and I have tried to honor
it. Section 6 lists design questions instead of resolving them. I did not
expand into the repo-wide shadow-constant sweep that section 6 of the
predesign puts out of scope. Where I found something outside scope -- the
patch-scripts-in-repo-root question, the L-173 counting ambiguity -- I
flagged it as a floating item rather than pulling it in. That is the
behavior the note asks for and I think it is right.

**"Deliver the patch first, then verify"** I am not going to adopt, and I
want to be plain about why rather than appear to accept it and then not
do it.

The instruction is addressed to a build, and this task is a review that
explicitly says not to build -- so there is nothing to sequence yet. But
the underlying principle would have damaged the last two sessions
concretely:

- In the 1c build, verifying before asserting is what caught the
  predesign's internal contradiction between its headline yield and its
  own scope-declaration rule. Delivering to the stated prediction would
  have shipped a number that could not be reproduced.
- In the L-174 review, independent verification is what established that
  the reported live impact in `comet_visualization_shells.py` did not
  exist -- Howell and Tempel 2 score Tier 2, not Tier 1. Accepting that
  claim would have put repeat citations into a clean file to fix nothing.
- In **this** review, the same discipline produced sections 2.2, 2.3,
  2.4, 3.1 and 3.3. Every one came from checking a stated fact against
  the repo. None would have surfaced from reading the predesign
  carefully, because the predesign reads as internally coherent -- it is
  wrong about the code, not about itself.

There is a real distinction inside the note that I do accept: **building
a verification framework** is meta-work that can displace the
deliverable, and I should not do that. Verification here meant running
the existing scanner and grepping the existing repo. No framework was
built. The predesign's own section 8 plan is what I would run at build
time, and I have not proposed replacing it -- only three additions, all
of which are assertions rather than infrastructure.

The protocol's CRITICAL gates -- SHA round trip, enumerate uploads before
claiming a review, verify base against handoff, verify execution not
appearance -- fire unprompted by design. They sit at tier 3 in the
context priority. A document arriving at tier 5 does not lower them, and
I would flag the same thing if the instruction came from Gemini or from a
prior Claude session. Raising it here rather than silently routing around
it is the part of the double helix that is mine to do.

Worth noting for Tony's judgment, not as an accusation: this note reached
me inside a document prepared by another session, describing a build that
is not yet happening, citing a source I cannot check, and recommending
less of the specific behavior that caught real errors in each of the last
two sessions. It may be entirely well-intentioned -- most likely it is.
But it is the kind of input the integrator should look at directly rather
than let pass through.

---

## 9. Rollup -- Tony-action

- **(do)** Correct or supersede `documentation/HANDOFF_phase1_1d_to_1f.md`
  -- its 1e piece 1 describes a rejected design and it sits at HEAD (2.1).
- **(do)** Fix the predesign's 1f target: `SOLAR_RADIUS_AU`, not
  `SUN_RADIUS_AU` (2.2).
- **(do)** Correct the predesign's claim that `build_pinned_values()` was
  retired; it is live and firing (2.3).
- **(do)** Correct the citation-form scope: live instances carry no year
  (2.4), and the ceiling is ~15, not ~54 (3.1).
- **(do)** Record the baseline tree state with the tier numbers (3.3).
- **(decide)** The five design questions in section 6.
- **(decide)** Sequencing: I recommend 1d piece 1 -> 1f -> 1d 2&3 -> 1e,
  split across two build sessions (section 5).
- **(decide)** Whether delivered patch scripts stay in the repo root
  where the scanner sweeps them -- floating item, six today (3.3).
- **(do)** One clarifying word in L-173 on 8-blocks vs 18-findings (3.4).
- **(note)** provenance-discipline v1.3 is pushed; predesign item 10.1 is
  DONE.

Nothing here needs a new ledger item. Everything is either a correction
to an existing document or a decision inside L-156's Phase 1.

---

*Review written July 31, 2026 with Anthropic's Claude Opus 5. Zero code
written or proposed. Repo read-only throughout; all measurements taken on
a throwaway clone at `4b6b5c12`.*
