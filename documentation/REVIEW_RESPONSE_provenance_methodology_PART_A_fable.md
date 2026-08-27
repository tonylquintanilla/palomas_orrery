# Review response -- PART A -- provenance, golden artifacts, and the braided build order

**Reviewer:** Claude Fable 5, inside Tony's Claude project.
**Reviewing:** `REVIEW_PROMPT_provenance_methodology_PART_A.md`, which is
built on orrery `2d7f3258d1383cf752b206fa6875ee312e8f2f78` at
https://github.com/tonylquintanilla/palomas_orrery and gallery
`1a67b00d73813a1387ff1de7b77f8175c39c0f1e` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
**Date:** 2026-08-27.

**What I read, and what I did not.** I read Part A, the two master-plan
documents in the project folder (`MASTER_PLAN_INTERACTIVE_GALLERY.md`
v19 and `MASTER_PLAN_CRITICAL_PATH_SUMMARY.md`, both as of
2026-08-23/25), the resident protocol v3.44, and two installed skills
(provenance-discipline 2.7 and ledger-and-session-records 1.9; both
match the manifest). I did not open either repository, did not run the
scanner, and did not search past conversations for Part B. Every number
below that is not in Part A is an estimate and is marked as one.

**One disclosure about independence.** I share a model family with the
session that wrote Part A and with the Opus leg of the pilot. Where I
agree with a Claude conclusion, that agreement is weaker evidence than a
GPT or Gemini leg's would be. Where I disagree, weight it normally.

---

## 1. Verdicts

### G1 -- Verified information, served to the renderer and the reader

**The minimum mechanism is three things: one store, prose that derives
from it, and a citation that carries a quotation. Those answer three
different questions, and the current design mostly answers only the
first.**

The three properties in the question are separate, and they fail
separately.

CONSISTENT means one value, everywhere it appears. This is a structural
property. Either the value lives in `constants_new.py` and every hover
string, tooltip and comment interpolates it, or there is a second copy.
"The correction does not travel" is a consistency failure, not a
provenance failure. Both examples in Part A section 4 (the approach
distance wrong at seven prose sites, the shell radius wrong at four) are
second copies. Consistency is the only one of the three properties a
machine can fully check: any numeric literal on the served surface that
is not a declared drawing parameter is a finding. Provenance-discipline
2.7 already rules this ("One Value, One Home"). What is missing is a
checker in `maintenance_run.py` that enforces it on the served surface,
so the rule cannot be forgotten.

SOURCED means a provenance claim is recorded. The scanner checks that a
citation is present. It cannot check that it is true, and the record
shows that presence is exactly what suppresses suspicion: the 34% Hill
sphere under a stamp, and three wrong-paper citations in Batch 1 that
"looked right."

CORRECT means the number matches the world. No mechanism gives that
directly. The nearest proxy is a citation that can be FALSIFIED cheaply.
Part A section 3b offers the pilot measurement without interpretation; I
will interpret it. The one leg whose returns carried quotations caught
the Alfven error. The two legs whose returns carried none confirmed the
wrong value, and one of them described its own confirmation as a
recollection. A quotation makes a citation checkable by find-in-page in
under a minute. A paper name plus "confirmed" is checkable only by
redoing the research. A quotation also keeps the qualifier a bare number
drops -- "above the photosphere" was the whole error. Fabricated
quotations exist, but one find-in-page catches them; a fabricated
"confirmed" is caught by nothing.

So the minimum mechanism, for a value on the served path:

1. The value has one home in `constants_new.py`. Everything else
   interpolates it. (Consistency, mechanical.)
2. Its source record carries a locator (DOI, table, page, URL) AND a
   verbatim quotation of the sentence or table cell the number comes
   from, stored as data in the worksheet the annotation names.
   (Sourced, and falsifiable.)
3. The builder refuses to serve a MEASURED value that lacks both. A
   value that cannot meet this is either removed or re-classed as
   DECLARED with the hover saying so. (This is "silence is better,"
   enforced at the point where it bites.)
4. The served hover shows the source to the visitor. The source strings
   are already in the Sun's served configuration; whether the page
   renders them I do not know. If it does not, that is the cheapest
   possible "verified information to the reader": the reader can check,
   and a blank reads as a blank.

Tony's spot check then becomes: open the source, find the quote. That is
the one judgment he is best placed to make, and it costs minutes.

### G2 -- Simplify citation and verification

**Most of the apparatus can stay, because it is mechanical and cheap.
The parts to delete are the ones that ask a person to read rows, and the
concurrence criterion for the top rung, which the pilot showed measures
agreement rather than evidence.**

What is carrying its weight: the two-move clearing rule (cite truly, or
remove and note the gap) is "silence is better" in procedural form and
should not move. The annotation grammar is one line pointing at a file;
fine. The JSONL request and return format produced 69 rows with zero
defects; fine. The scanner as a REPORT is fine. Tier-1 as a gate is fine
once its scope is right (see d below).

What to delete or change:

**(a) The concurrence criterion for V_CROSS_CHECKED.** The rung requires
two `# Cross-checked:` lines from two identities. Two models recalling
the same wrong value satisfy it. The retired `# Verified:` stamp was
retired because "it recorded that a model looked and nothing else"; two
such lines from two models is the same defect with a bigger denominator.
Keep the rung as a STATE. Change its criterion to: the annotation names
a worksheet row carrying a locator and a quotation. One quote
outperformed two concurrences in the only dispatch that has run. What is
lost: the 50 existing rows do not automatically re-qualify. Do not redo
them. They keep their annotations as history, and the serving gate
applies per slice as each body reaches its ladder step.

**(b) The 44 legacy stamps.** Delete all of them in one patch, now, not
"in Batch 2." The skill already says "replace on sight." A retired stamp
still in the file still stops the next reader from looking. The values
that were re-checked carry new annotations and lose nothing. The values
that were not re-checked are exactly the ones the stamp is shielding. If
the scanner currently credits the stamp as a citation, Tier-1 will rise,
and that is the honest number. (Whether it credits them I do not know.)

**(c) The 553 display-string claims, as PROVENANCE findings.** A hover
string that types a number is a second store. The right treatment is not
to cite it; it is to make it interpolate. On the served surface,
description text is ruled to be composed builder-side from the store
(master plan decision 17), so a typed number there is a consistency
finding, cleared by derivation, once, at the constant. So, to answer the
question as asked: which of the 553 are worth the current treatment?
None, as strings. The 225 in the paleoclimate modules are Earth System
and off the active path by the 2026-08-05 ruling. The 98 in
`shell_configs.py` and 49 in `idealized_orbits.py` are on the orrery's
own desktop path; their served counterparts derive from the store. What
IS worth verifying is the roughly twenty MEASURED store constants per
body that the served strings derive from (19 for the Sun; the twenty is
an extrapolation from one body). That is the denominator. Verify the
constant once; the strings inherit.

**(d) A narrowing that needs Tony's ruling.** "Tier-1 = 0 on the active
build path" is computed from the import graph. If that graph reaches the
shell modules' `_info` strings (Uranus restating 25,559 km nine times),
the gate is wider than the served surface, and it will keep pulling
desktop hover text into the gallery's gate. The 2026-08-27 ruling
already says the gate binds at serving. Make the scanner's gated set the
SERVED SURFACE: the measured fields in `feature_configs.json` and the
store constants they point to. That set is countable per step, which is
what the braid asked for.

**(e) A rule that removes a class of judgment call.** A dispatch return
without a locator and a quotation is not a check. The checker routes it
to NOT_A_CHECK automatically; it never reaches Tony as a divergence. The
consequence is a relay-configuration decision only Tony can make: a leg
that cannot quote is a lead-generation leg, not a verification leg.
Gemini's 1% quotation rate is consistent with a leg answering without
retrieval, which is the silent-no-search behaviour Tony has already
flagged for Gemini. The skill already says free-form model output is a
search plan and never citable. Apply that rule to the return format.

Not to delete: the worksheet-first rule, the vocabulary version line,
and the two-column verdict (value versus citation). Those are what make
a return machine-readable, and they cost nothing after the first use.

### G3 -- Simplify the golden artifact

**Replace it. The two stated purposes want two different comparisons,
and a single stored fourteen-field fingerprint serves neither once
features are added part by part.**

Purpose 2, browser-and-desktop agreement, is a SAME-INPUT comparison:
the same served cache, the same date, computed in CPython and in
Pyodide, compared to each other. It needs no stored artifact. It needs
the builder to write a handful of sampled positions into the served
index (it already computes them), and the interactive page to compute
the same samples in Pyodide and compare on load. The tolerance should be
tight and its unit stated. Both sides are float64, so anything beyond
the last handful of digits (on the order of 1e-9 relative; the unit is
Tony's to choose) is a real finding. A 0.001 tolerance in AU would be
150,000 km, about 40% of the Earth-Moon distance. I do not know the
unit of the 0.001. This check runs on every visit and cannot go stale,
because its reference is regenerated with the cache. If the Pyodide side
has never produced a fingerprint -- Part A does not say -- then purpose
2 has so far been asserted rather than measured, and this is the
higher-priority half.

Purpose 1, a slightly wrong position, is a REGRESSION comparison. A
stored snapshot of today's assembly cannot serve it, because the inputs
refresh nightly and a change in output cannot be told apart from a
change in input. Two smaller things serve it:

- A fixture test. One frozen input (one object's served elements at one
  epoch, a few hundred bytes) and expected positions taken from a
  Horizons vector query at that epoch, recorded with the query
  parameters the served schema already uses for provenance. The test
  propagates the fixture and asserts agreement within the tolerance the
  trust window implies. This never changes unless the code or the
  fixture changes, and it compares against ground truth rather than
  against yesterday's self. So it catches wrong-from-the-start, not only
  changed-since-July.
- The trust measurement (`served_window`) already compares propagation
  against Horizons over time, if I understand M2 correctly. A
  propagation bug of the planetocentric-mean-motion kind would collapse
  the window to minutes. If that is what M2 measures, it is already the
  strongest wrong-position detector in the system and it runs every
  build. I could not confirm this from Part A; see section 5.

The remaining fields -- trace counts, legend groups, feature keys,
bounds -- are scene STRUCTURE. Under the 2026-08-25 ruling that
artifacts reopen, they will fail on every step of the ladder by design.
Replace the stored counts with a contract check that stores nothing:
every feature key the served config carries for an object produces a
trace; every trace carries a legend group matching the convention;
bounds are finite and enclose the samples. Mechanical, no golden file,
no re-lock.

The harness comparing to itself is Part A's finding (a), and it is the
case the protocol's "A Check That Cannot Fail Is Not Passing" gate was
written for. Whatever replaces it must print what it compared, against
what, and how many samples -- "12 samples vs fixture <hash>: max error
2e-11 AU" -- so that a pass carries evidence.

What is lost: the idea of a one-time LOCK. The 2026-08-25 ruling already
conceded that re-locking is normal, which is another way of saying the
lock never did what its name says.

A cheaper alternative exists: repair the existing harness to read the
stored file, exclude the three volatile fields, and put a tolerance on
bounds. One evening. I recommend against it, because it leaves a
mechanism that fails on every feature addition, and a seventeen-step
ladder adds features at every step.

### G4 -- Simplify Tony's judgment calls

**Four decisions reaching Tony today should be absorbed by rules, and
four questions that are not reaching him should.**

Should not reach him:

1. Whether a dispatch return counts as verification. Rule: locator plus
   quotation, or NOT_A_CHECK. (G2e.)
2. Which copy of a value is authoritative when two disagree. Already
   ruled -- the store wins -- but the FINDING still arrives by hand: a
   consistency audit, a Mode 5 screenshot sent for something else. Make
   it a checker: any literal on the served surface that matches a store
   constant, and any served measured field whose value differs from the
   store constant it points to. The Sun's nine-of-nine match was checked
   by a person; the pointer is already in the data. (Whether the pointer
   is machine-readable I do not know.)
3. Whether a golden-artifact diff after a feature addition is
   legitimate. With the contract check in G3 there is no diff to judge.
4. What the current count is. Documents restated 105, 107 and 110 for
   one figure inside a week. A count a tool prints should live in a
   generated zone (the skill manifest is the working precedent) or not
   appear in prose at all.

Should reach him and is not:

1. The tolerance, in a stated unit, for "slightly wrong." He knows what
   error is visible at render scale for each scene; nobody else does.
2. What "published" means for the serving gate. Is a local `http.server`
   on his machine serving? I would say no: a push to gallery `main` is
   publication, because Pages deploys it. But that is his ruling to
   make, and the ladder text should carry it.
3. What happens to a value that cannot be sourced but is already drawn.
   "Not served" for a ring radius means a missing ring on the public
   site. The alternative is to publish it re-classed as DECLARED, with
   the hover saying "drawing choice, not a measurement" -- the
   streamer-belt precedent. There will be many such cases; a standing
   default (which way, absent a reason) would absorb most of them.
4. Whether he will actually perform the find-in-page spot check, and at
   what rate (three quotes per body, say). If the answer is no, the
   quotation requirement still improves the record but stops being a
   verification. Better to say so than to let it look like one.

### G5 -- The braided order

**The order is sound -- render first, slice bounded to what the step
serves, gate at publication -- and it has one structural hole: while the
transport is a hand copy, "the correction does not travel" moves onto
the public site the moment a second body is published.**

Why the order is right. Rendering makes a value visible, so gross errors
(wrong frame, wrong magnitude) become something eyes catch. Bounding the
slice to what the step serves makes it countable, so it terminates.
Gating at serving rather than drawing costs nothing that cannot be
undone in an afternoon. All three follow from the braid ruling and from
the two failure modes in section 4.

The failure modes:

1. **Step 12 changes what step 4 published.** Under
   one-store-with-derivation, the change is one edit in
   `constants_new.py`; the builder re-composes the served text on the
   next build; step 4 is corrected without anyone remembering it. That
   holds only if the served value was DERIVED from the store at build
   time. Today `objects_config.json` is maintained by hand (segment 2,
   designed and not built). So a correction at step 12 lands in the
   store and not in the gallery's copy, and the public site keeps the
   wrong value silently. That is the worst version of the second failure
   mode, because a visitor takes it as true. The plan says segment 2 is
   not on the path to Artifact 2. That is true of DRAWING Artifact 2 and
   false of PUBLISHING anything after it. Either fetch-and-import lands
   before the third body is published, or an interim check makes the
   builder compare each served measured field against the store constant
   it already points to and refuse to build on mismatch. The interim
   check is about one evening and does not need the fetch.

2. **Shared constants cross steps.** `KM_PER_AU`, the solar radius and
   the parsec factor feed many bodies. A change at step 9 re-renders
   step 1. So every check in the suite -- contract, fixture,
   served-versus-store -- runs across ALL published bodies on every
   build, not per step. A per-step check goes stale the step after it
   passes.

3. **The golden artifact as designed invalidates itself at every step**
   (G3). Keeping it per step means either re-locking seventeen times or,
   more likely, ignoring a red check everyone knows is red for a
   legitimate reason. That is how a real failure hides.

4. **The gate lives in discipline instead of in the builder.** Seventeen
   steps, one person, evenings. A step whose render takes one evening
   and whose slice takes three will be tempting to publish without the
   slice. The gate must be the builder refusing to serve a MEASURED
   value without provenance, so that skipping is impossible rather than
   discouraged. Master plan decision 15(a) already aborts on a missing
   source; extend it to the quotation requirement and it is the gate.

5. **The render is oversold as a provenance check.** It catches
   magnitude and frame. It does not catch the Alfven case: one solar
   radius on fifteen, about 7%, invisible at any zoom. The plan's
   sentence "a wrong ring radius becomes something Tony's eyes can
   catch" is true for factor-of-two errors and false for the errors the
   pilot actually found. Mode 5 acceptance must never be recorded as, or
   drift into, "verified." Two different words in the record.

6. **Step 3 is a conversation inside a rendering ladder.** "A GUI
   conversation" has no render, no slice, no artifact. It will either
   block steps 4 through 17 or be skipped. Pull it out of the ladder as
   a parallel item, or bound it to one evening and one decision. I do
   not know what it covers.

7. **The slice denominator must be stated before the step, not
   discovered during it.** The Sun's slice is 19 measured values. That
   number should be written at the top of each step before work starts,
   and the step stops at zero. Otherwise "now I can see its neighbour is
   wrong" turns the slice back into the global sweep the braid was
   ruled to end.

8. **Three sequencing structures now exist:** the seven golden artifacts
   (propagation shapes), the seventeen-step ladder (draw order), and the
   ledger. The 2026-08-25 ruling separated the first two by axis, which
   is right. The risk is drift among three lists. A clean reconciliation:
   the seven propagation shapes become fixture tests (G3) that always
   run; the ladder is the only sequence of work; the ledger holds status.
   Then nothing is "Artifact 4" any more, and nothing needs re-locking.

---

## 2. Delete list

| Mechanism | What is lost |
|---|---|
| The concurrence criterion for V_CROSS_CHECKED (two checker lines). Replace with locator plus quotation. | The 50 populated rows stop counting as top rung until each reaches its serving slice. Nothing else; the pilot shows concurrence was not evidence. |
| The 44 legacy `# Verified:` stamps, all at once. | Nothing. Re-checked values carry new annotations. Tier-1 may rise if the scanner credits the stamp; that is the honest number. |
| Display-string claims as provenance findings on the served path. Reclassify as consistency findings, cleared by interpolation. | The 553-claim denominator. The 225 paleoclimate claims were already off the active path. |
| The stored fourteen-field golden fingerprint as a gate. | A one-time lock that was never being checked and would fail on every ladder step by design. Keep the existing file as a historical record. |
| Restated counts in prose documents. | Nothing; the tool prints them. |
| Legs that return no quotation, from the VERIFICATION dispatch. They stay for lead generation. | One leg's concurrence per row. Tony's ruling, not mine; he runs the relay. |

## 3. Keep list

- `constants_new.py` as the one home, with the MEASURED / DECLARED
  split. Everything else in this review depends on it.
- The two-move clearing rule. It is "silence is better" as a procedure.
- Tier-1 as a mechanical gate, narrowed to the served surface (needs
  Tony's ruling).
- The builder's abort-on-missing-source (decision 15a). It is the real
  gate; extend it, do not replace it.
- The JSONL request and return format, the two-column verdict, and the
  vocabulary version line. They make returns machine-readable at no
  recurring cost.
- The annotation grammar. One line that points at a file; the file gains
  fields, the line does not change.
- The browser-versus-desktop agreement check, as a LIVE comparison. It
  is the central claim of the architecture, and it appears to be
  unmeasured so far.
- Mode 5, with its limit stated in the record: it catches frame and
  magnitude, not percent.
- The braid and the serving gate. The order is right; only its
  enforcement point and the transport are wrong.
- The blind-source-lookup round (present the claim with the value
  removed). It is the one existing step that defeats anchoring, and it
  produced Batch 1's best catches.

## 4. Cost estimate (evenings, one person; all estimates)

| Item | Evenings |
|---|---|
| Delete the 44 stamps: one patch script, scanner before and after | under 1 |
| Worksheet schema: `locator` and `quote` become required fields; checker routes missing to NOT_A_CHECK | 1 |
| Builder: served measured field equals the store constant it points to; refuse on mismatch | 1, if the pointer is machine-readable (unknown) |
| Builder: refuse to serve MEASURED without locator and quote (extends 15a) | under 1 |
| Served-surface consistency checker in `maintenance_run.py` (literals matching store values) | 1 to 2; L-158's frozen-literal detector may already do half (unknown) |
| Fixture test: one object, expected positions from Horizons | 1 |
| Live Pyodide-versus-CPython sample comparison on page load | 1 to 2; the Pyodide plumbing exists in `interactive.html` |
| Structural contract check replacing stored counts | 1 |
| Ladder text: definition of "published," per-step denominator, step 3 pulled out | part of the existing withheld patch |
| **Total new work** | **roughly 8 to 10, spread across the ladder, not in front of it** |

The deletions cost under one evening combined and remove recurring
cost: every future step that would have re-locked an artifact, and every
dispatch row that would have reached Tony as a divergence between two
recollections.

Applying the skill's own "Extend a Boundary Before Adding a Path" test
to these proposals: the locator and quote are FIELDS on a record that
already travels (the worksheet row); the builder checks EXTEND decision
15(a); the contract check REPLACES a path rather than adding one. The
served-surface consistency checker is the one new path, and it is the
one that answers the property no tool measures today.

The alternative of repairing the golden harness in place is one evening,
and I recommend against it (G3).

## 5. What I could not assess

- `provenance_scanner.py`: whether `# Verified:` stamps are credited as
  citations; whether the frozen-literal detector already catches prose
  copies; what the V ladder holds beyond V_SOURCED and V_CROSS_CHECKED.
- The golden-artifact harness: which environment computes the
  fingerprint; whether Pyodide has EVER produced one; the unit of the
  0.001 tolerance. My G3 claim that purpose 2 is unmeasured depends on
  this.
- `served_window` / M2: whether the trust measurement compares
  propagated positions against Horizons vectors. My claim that it
  already serves purpose 1 depends on this; if it measures something
  else, strike that paragraph.
- The active build path: which entry points `dep_trace.py` walks, and
  whether the shell modules' `_info` strings are in the gated set. G2(d)
  is moot if they are already excluded.
- `objects_config.json` and `feature_configs.json`: whether the
  per-field pointer to a store constant is a machine-readable key or a
  prose string. The one-evening builder check depends on it.
- `DRAFT_rendering_ladder_section.md`: what step 3 covers; whether steps
  state a denominator; what the draft says "published" means.
- The pilot worksheets: whether `source` and `notes` are free text only,
  and whether any field already exists for a quotation.
- `constants_new.py`: how many measured values the full seventeen steps
  serve. "About twenty per body" is an extrapolation from one body.
- Whether the served hover text shows sources to the visitor today.
- Whether L-238 (`_validate_feature_shapes` asserting
  `radius_fraction > 1.0`) is still open at this SHA. If it is, Earth's
  interior cannot be served regardless of provenance, and that repair
  precedes step 2.

I do not know any of these. None of them changes the direction of the
five verdicts; several change their cost.

---

*Prepared 2026-08-27 by Anthropic's Claude Fable 5, reviewing Part A
only, without repository access and without reading Part B. Filed as a
record, not a tool input: `documentation/` per the ledger skill.*
