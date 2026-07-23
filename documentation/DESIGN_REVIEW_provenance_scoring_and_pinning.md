# Design Review -- Provenance Scoring Model Fix and In-Scanner Pinning Checks

Tony Quintanilla, PE | Claude Sonnet 5 | July 23, 2026

**Built on:**
- orrery (palomas_orrery) @ `9b4571851184e599f72de928cada16d30c9010f6`
- gallery (tonyquintanilla.github.io) @ `79710968241f21c8e6e1836bb1ad35219f1a31f0`
(Both confirmed unchanged since Fable's design handoff, verified again this
session via `git ls-remote`.)

**Type:** DESIGN REVIEW (zero scanner code). Companion to
`PREDESIGN_HANDOFF_provenance_scoring_and_gallery_scanner.md` and Fable 5's
`DESIGN_HANDOFF_provenance_scoring_model_fix_and_pinning_checks.md`.

---

## 1. Verification (independent, not a re-read of Fable's claims)

Every load-bearing factual claim in Fable's design was independently
reproduced, not just read and found plausible:

- Cloned both repos fresh; SHAs match Fable's exactly.
- Ran `provenance_scanner.py` myself against the full tree (not sparse):
  **105 Tier-1 findings**, `KM_PER_AU` scores 10, `SUN_RADIUS_KM` scores 6
  ("Imported by 2 module(s)") -- all match Fable's document exactly.
- Grepped the full repo for `test_constants_provenance` -- exactly the five
  files Fable named, nothing more, nothing missed.
- Grepped `constants_new.py` for named Saturn/Mercury/Venus/Mars/Moon
  primaries -- zero hits, confirming only Sun/Earth/Jupiter have them; the
  other 15 bodies live only inside `CENTER_BODY_RADII`.
- Confirmed `CENTER_BODY_RADII` is currently scored by the scanner as
  **one single row** (18 entries collapsed into one finding) -- meaning a
  wrong value for any one body is currently invisible in the report as a
  distinct problem.
- Sampled the 330 findings that would move under the V-ladder shift:
  **all 330 are display-string/hover-text claims**, already scored C=4
  today (display strings have always been categorical, unaffected by
  import count) -- so the flood is a D3 (Vulnerability) effect only, not
  a D1/D2 (Criticality) side effect.

Nothing checked came back different from what Fable's document asserts.

---

## 2. Decisions confirmed as-written (no changes requested)

- **D1** -- Two criticality categories (MEASURED/RELATIONAL); ring
  geometry sits in MEASURED. Confirmed, including under independent
  re-derivation of the same boundary (measured-vs-derived-from-something-
  tracked, not important-vs-unimportant).
- **D3** -- Cross-checked lands at V=1, same floor as FETCHED; merely-
  sourced moves to V=3. Confirmed as the correct read of the Arrokoth/
  Parker precedent. **Still needs to go to Gemini as a calibration
  question before the build locks the ladder in** -- see section 5,
  open dependency.
- **D4** -- Annotation form and ref-required anti-gaming rule. Confirmed.
- **D8** -- All five comprehensive-sweep resolutions. Confirmed.
- **D9** -- Two-factor STRUCTURAL rung (comment + AST confirmation, both
  required, mismatch is itself a finding). Confirmed -- this is the same
  fail-safe direction as D2's "unclassified defaults toward review," just
  expressed as "ambiguous defaults toward NOT claiming safety."
- **D10** -- Retire `test_constants_provenance.py` entirely, all five
  reference sites. Confirmed, strongly -- my own grep found zero calls or
  imports anywhere in three months.
- **Edge case (period vs. radius, same tier despite different failure
  shape)** -- confirmed, no objection raised.

---

## 3. Decisions amended

### 3a. D5 -- full de-duplication, not the 3-body minimum

Fable's D5 fixed the actual bug (duplication) by referencing the three
existing primaries and leaving the other 15 bodies as dict-only. Expanded
per this review: **promote all remaining bodies to named constants**,
because `CENTER_BODY_RADII` currently scores as one undifferentiated row
-- a wrong value for any single body is invisible as a distinct problem
today. Promoting each to its own named constant gives each one its own
scanner row, using existing mechanics, no new scanner code required for
that part.

**Scope: 15 new named constants** (Mercury, Venus, Moon, Mars, Phobos,
Saturn, Uranus, Neptune, Pluto, Bennu, Eris, Haumea, Makemake, Arrokoth),
each keeping its existing citation -- restructuring already-Gemini-
verified facts, not re-opening verification.

**One exclusion: Planet 9.** Its entry is a model estimate (the body has
never been directly observed), not a measurement. Tony's call: leave it
out of the MEASURED promotion entirely; carry it forward as its own case
for L-159 (disclosed-approximation work) instead.

**Scoped as prep work, not scanner-build work** -- see section 4 (L-162).
Sequencing note: doing this *before* Fable's Phase 2/3 build touches D5/D6
simplifies the pinning engine itself -- it can pin against 18 named
constants directly instead of needing dict-path AST extraction for 15 of
them. Worth finishing before Phase 3 starts, not just "eventually."

### 3b. D2 -- explicit UNCLASSIFIED state, not a filter-ordering fix

Fable's D2 didn't specify whether the cosmetic gate or the MEASURED/
RELATIONAL split runs first. Concrete failure case: a purely cosmetic
rendering value (e.g. a shell-opacity dict) that doesn't match the
cosmetic name heuristic ("opacity" isn't "color"/"label") and doesn't
match either physical vocabulary would default *up* to MEASURED -- the
highest tier -- under D2 as written.

**Amendment (Tony's design, not a variant of "defaults up"): add a
distinct UNCLASSIFIED outcome.** Anything that can't be confidently placed
in cosmetic, MEASURED, or RELATIONAL lands in the review tier regardless
of what a guessed score would have produced. This makes the filter-order
question moot -- neither filter's mistake can go silently unnoticed,
because ambiguity itself is now a visible, forced-review signal rather
than something resolved by a guess in either direction. **Decided: gets
its own banner**, same visibility tier as the Tier-1 banner -- not a
normal finding row with a distinct label.

### 3c. D7 -- Tier-1 never gets an auto-exit gate (supersedes the
deferred-flip recommendation)

Fable recommended banner-now, hard-exit-when-count-first-hits-0. On
review: that's still judging by a number (is it zero yet), not by what
the findings actually are. A baseline-ratchet alternative was considered
and also rejected on the same grounds -- it judges by whether the count
moved, which has the identical flaw one level up (a trivial new finding
auto-fails a fine run; a serious finding replacing a trivial one at equal
count auto-passes a bad one). This is the same mistake D1 already
corrected (criticality by volume, not by type), just re-appearing at the
whole-backlog level.

**Amendment: Tier-1 gets a permanent, prominent banner and never an
auto-exit gate, at any threshold, ever.** "Is 105 (or 60, or 20) findings
okay to push past" is a judgment call every time, not a number to
formalize. The hard, automatic exit-code gate belongs only to the pinning
checks, because those are genuinely binary -- a value matches its cited
source or it doesn't.

### 3d. D6 -- no change (reviewed and accepted as-is)

The gallery-repo-missing skip (loud notice, no effect on exit code) was
raised as a concern and dropped on review: Tony's actual operating
environment makes a silently-broken sibling path implausible -- any repo
reorganization would break other relative-path-dependent things first and
loudly. D6 stands as Fable wrote it.

---

## 4. New ledger items from this review

#### [L-161] Gemini sweep -- clear the display-string Tier-2 backlog
<!-- L:161 status:OPEN upd:2026-07-23 section:W.Active flag: rice:3/3/70/2 -->
- **What.** Once D3 ships, ~330 currently-C=4/V=2 display-string citations
  move from Tier 3 to Tier 2 (independently confirmed: sampled all 330,
  all are hover-text claims, none newly re-scored by D1/D2 -- this is
  purely the V-ladder effect). Roughly 130 of those were already Gemini-
  verified by the April 2026 worksheets and just need D4's backfill
  annotation (mechanical, no new Gemini time). The remainder need a
  genuinely new sweep.
- **File concentration, confirmed empirically:** 84% of the 330 sit in 15
  files. `celestial_objects.py` alone is 50 findings with **zero prior
  worksheet coverage**. Neptune, Uranus, Solar, Saturn, Pluto,
  `idealized_orbits.py`, and `planet_visualization_utilities.py` shell/
  utility files have also never had a Gemini pass.
- **Two tracks:** (1) backfill already-worksheeted files (Earth, Jupiter,
  Mercury, comets, star_notes, info_dictionary) with D4's annotation;
  (2) new worksheets for `celestial_objects.py` first, then the rest of
  the uncovered list, using the proven worksheet template.
- **Sequencing, revised on review:** originally proposed to run alongside
  the Phase 1-2 scanner build. **Changed: sequence AFTER the build ships,
  not parallel with it** -- the urgency (a large visible Tier-2 queue)
  doesn't exist until D3 actually lands; running it in parallel adds a
  third simultaneous thread for no real gain. Start once Phase 1-2 close.
- **Practical note carried from review:** consider running this through
  the same Mode 7 relay channel as L-157 (sequentially, not merged in
  scope) rather than opening a second, separate Gemini engagement --
  reduces operational threads without merging two genuinely different
  populations (display strings vs. shell-geometry config values).
**Gap:** draft first worksheet (`celestial_objects.py`); confirm backfill
list against the April worksheets' actual coverage before assuming which
~130 are already clear.
**Ref:** L-156, L-157, L-160; `documentation/worksheet_*.md` set.

#### [L-162] CENTER_BODY_RADII full de-duplication -- prep work for a dedicated Sonnet session
<!-- L:162 status:OPEN upd:2026-07-23 section:W.Active flag: rice:3/3/90/1 -->
- **What.** Promote all 15 remaining `CENTER_BODY_RADII` bodies (see 3a
  above) to named constants, each keeping its existing citation. Excludes
  Planet 9 (speculative, not measured -- see 3a). This is client-side prep
  work ahead of the scanner build, not part of Fable's design-build --
  legitimate to do now, scoped as its own clean session rather than folded
  into this already-long review.
- **Why now, not "eventually":** simplifies L-155/L-156's Phase 3 pinning
  engine -- it can reference 18 named constants directly instead of
  needing dict-path AST extraction for 15 of them. Best landed before
  Phase 3 starts.
**Gap:** dedicated Sonnet session: fresh SHA pull, safe-file-editing
discipline (bottom-up, ASCII, py_compile clean), credit line, update
`CENTER_BODY_RADII` to reference the new names instead of literals.
**Ref:** `constants_new.py`; L-156 D5 (as amended, section 3a); the design
handoff's own build Phase 2.

---

## 5. Sequencing correction -- D3's Gemini calibration is prep work, not a later bundle

Originally suggested bundling this with whichever worksheet goes out first
for L-157 or L-161. **Corrected on Tony's call: this is a preparatory
item, done before the design is treated as final -- not folded into
later, lower-urgency sweeps.**

Reasoning: D1's category boundaries, D7's Tier-1 flood math, and the tier
placements throughout this whole review all assume D3's specific numbers
(cross-checked = V1, sourced-only = V3) are correctly calibrated. Building
everything else on top of an unverified assumption and checking it later
is the same ordering mistake this whole session exists to catch elsewhere
-- verify the foundational input before anything else is built on it, not
after. The design should not be treated as build-ready until this comes
back.

**Next concrete action:** draft the D3 calibration worksheet (cross-
checked = same floor as fetched; sourced-only downgraded from the current
V=2 -- both against the Arrokoth/Parker precedent) and carry it to Gemini
*before* Fable's revision is treated as final, not after.

---

## 6. Prompt back to Fable 5

*(Optimized the same way as the original design prompt -- brief, reason-
first, explicit boundaries, claim-grounding. Paste as the next message in
the design thread.)*

> Tony reviewed your design with an independent pass (Sonnet 5) -- reran
> the scanner, re-grepped both repos, sampled the findings your document
> summarized, rather than trusting the summary. Everything factual
> checked out exactly. Three amendments came out of it, plus one new
> piece of scope; nothing else changes.
>
> **D5, expanded:** reference all 15 remaining `CENTER_BODY_RADII` bodies
> as named constants, not just the 3 with existing primaries -- because
> the dict currently scores as one undifferentiated row, so a wrong value
> for any single body is invisible as a distinct problem today. Exclude
> Planet 9 (model estimate, not a measurement -- carries forward to L-159
> instead). This is being done as separate prep work ahead of your build,
> not something you need to design further -- treat Phase 2/3 as pinning
> against 18 named constants, not 3 named + 15 dict-path lookups.
>
> **D2, replaced:** instead of relying on filter order between the
> cosmetic gate and the MEASURED/RELATIONAL split, add a distinct
> UNCLASSIFIED outcome. Anything that can't be confidently placed in any
> of the three categories lands in the review tier regardless of what a
> guessed score would produce. This removes the filter-ordering question
> entirely rather than answering it. **It gets its own banner**, same
> visibility tier as the Tier-1 banner (Tony's call) -- not folded into a
> normal finding row with just a distinct label.
>
> **D7, corrected:** Tier-1 never gets an auto-exit gate, at any threshold
> -- not the deferred-flip you proposed, and not a baseline-ratchet either
> (considered and rejected on review, same reasoning as D1: judging by a
> trending number is the same mistake as judging by import count, one
> level up). Permanent banner, human judgment, indefinitely. The hard
> exit-code gate stays exclusive to the pinning checks, which are
> genuinely binary.
>
> **Sequencing correction: your D3 ladder goes to Gemini before this
> design is final, not after.** Not a later bundle with L-157 or L-161's
> worksheets -- a preparatory step, now, gating whether this design is
> build-ready at all. D1's boundaries and D7's flood math both assume D3's
> specific numbers hold; verify the input before anything else gets built
> on it. Hold your revision as provisional until that calibration comes
> back -- if Gemini pushes back on the V=1/V=3 split, D1 and D7 may need
> a second look too.
>
> Everything else in your document -- D1, D3's floor logic, D4, D6, D8,
> D9, D10, the four-phase build sequencing -- stands as you wrote it.
> Incorporate the amendments above, but treat the design as provisional
> until the D3 calibration worksheet comes back from Gemini -- that's the
> next concrete action, not a parallel one. This is still design work --
> no code yet.

---

*Review written July 2026 with Anthropic's Claude Sonnet 5.*
