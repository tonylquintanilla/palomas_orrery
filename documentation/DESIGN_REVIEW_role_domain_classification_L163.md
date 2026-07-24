# Design Review -- ROLE_MAP / Domain Classification Redesign (L-163)

Tony Quintanilla, PE | Claude Fable 5 | July 23, 2026

**Built on:**
- orrery (palomas_orrery) @ `bdab1674d8794c67aeb000ee83176e295565f637`
- gallery (tonyquintanilla.github.io) @ `c2a323b7cea5c885995b7d4750a06c42383e5605`
(Both re-confirmed live via `git ls-remote` this session; exact match to
the reviewed handoff's own Built-on line.)

**Type:** DESIGN REVIEW (zero code). Reviewing
`ROLE_DOMAIN_CLASSIFICATION_HANDOFF.md` (Sonnet 5, L-163) specifically
for integration with the provenance-scoring cluster (L-154 through
L-162), whose design I authored
(`DESIGN_HANDOFF_provenance_scoring_and_pinning.md`) and whose review
amendments (`DESIGN_REVIEW_provenance_scoring_and_pinning.md`) I have
re-read in full at HEAD this session, alongside the predesign and
`MASTER_PLAN_UPDATE_provenance_and_prep.md`.

**Reviewer's verification scope, honestly stated.** Per the review
prompt, I did not re-audit L-163's own repo-wide reference checks. I did
independently re-verify the claims that sit on the boundary with my
cluster: the scanner's `MODULE_DOMAIN_MAP` / `DOMAIN_LABELS` mechanics
and its existing coverage-gap notes (provenance_scanner.py lines
300-345, 462-464, 1521-1600), `dep_trace.py`'s `get_category()` fallback
(matches Section 4a exactly, including `_ROLE_TO_VISUAL` being a
separate presentation table), ROLE_MAP's 94-entry count, the absence of
`PINNING_MAP` in the scanner at HEAD, and L-155's actual scope in the
predesign (a pinning table over `objects_config.json` values -- it does
not consume module classification; L-163's scope correction is right).

---

## Recommendation up front

**Build-ready as designed, with three integration amendments below.**
The sequencing L-163 proposes -- landing before my cluster's build -- is
correct and I endorse it. The one thing that must not slip: the deferred
domain-code retirement currently has no landing spot in my cluster's
build plan (amendment 2). Fix that in the ledger before either thread
builds, and the two threads coordinate cleanly.

---

## 1. Confirmed as-written

**Q1 -- the precedent citation holds, and is now stronger than the
handoff realizes.** My D2 cites "the same pattern the scanner already
uses for ROLE_MAP and domain coverage gaps." The pattern being cited is
the *visible coverage-gap note* -- the report section listing what
couldn't be classified -- not the default direction. L-163 keeps that
note (the UNCATEGORIZED/UNDETERMINED report section) and strengthens the
resolution from default-with-visible-note to refuse-to-guess. My
citation survives intact.

More than that: Tony's amendment 3b to my own design (in the Sonnet 5
review) replaced D2's defaults-up with a distinct UNCLASSIFIED outcome,
forced into the review tier, with its own banner. L-163's `undetermined`
sentinel and 3b's UNCLASSIFIED state are the *same design*, arrived at
independently on two different axes (role/domain classification;
criticality classification). The convergence is evidence both are right.
Sequencing L-163 first means my cluster's mechanism extends an
already-corrected precedent rather than a legacy one -- exactly as
L-163's Section 12 argues. Confirmed.

**Q2 -- the `test_constants_provenance.py` disposition matches D10's
intent exactly.** D10's retirement executes in my build's Phase 3 (the
pinning engine), not before; until Phase 3 ships and the constants_new
pins are verified working inside `run_pinning_checks()`, the standalone
file is the only working copy of that logic. L-163's "tag it `devtool`,
sweep normally, archive only after L-155/156/160 ship" is precisely the
right read. The tag is written onto a file that will later be archived
-- a few minutes of throwaway work, and the correct call, since the file
must stay classified for as long as it lives. No cleaner sequencing
exists; do it as written.

**Also confirmed, no changes:** the `dep_trace.py` 4a fix folded into
this build (verified against the code -- the fallback's hardcoded
heuristic and silent `'other'` are real, and `_ROLE_TO_VISUAL` is
correctly exempted as presentation, not classification); the gallery
4-value domain vocabulary mirroring the skill boundaries; `SCAN_PATHS`
as an explicit list with collision flagging; `__init__.py` exemption;
the raw-docstring parser being NEW rather than reusing
`get_module_docstring()` (verified: that function is a paragraph-joining
summarizer and would mangle a structured tag); MODULE_INDEX.md not being
a fourth consumer.

---

## 2. Amended (three items)

### 2a. D10's five listing sites change shape once L-163 lands --
### update the retirement checklist

D10 enumerates five hand-edit sites for retiring
`test_constants_provenance.py`, two of which are the `ROLE_MAP` entry in
`module_atlas.py` and the `MODULE_DOMAIN_MAP` entry in the scanner.
After L-163:

- The ROLE_MAP site **stops being a hand-edit**. ROLE_MAP becomes a
  regenerated marker zone; when Phase 3 archives the file, the entry
  disappears on the next `module_atlas.py` run. The Phase 3 checklist
  must say "delete file, run module_atlas.py" -- otherwise a builder
  following D10 literally will either hunt for a hand-edit that no
  longer exists or, worse, hand-edit inside a generated zone (the exact
  anti-pattern both designs exist to kill).
- The MODULE_DOMAIN_MAP site's fate depends on amendment 2b below --
  if the domain retirement lands in Phase 3 as I recommend, the whole
  dict is gone and the site vanishes entirely.
- A pleasant property worth naming: under L-163 the file's own
  `Role:`/`Domain:` tag is self-cleaning -- it dies with the file. The
  new mechanism removes cleanup sites rather than adding one.

### 2b. The deferred domain-code retirement has no landing spot --
### assign it to my build's Phase 3

L-163 defers "provenance_scanner.py retires
MODULE_DOMAIN_MAP/DOMAIN_LABELS and imports domain from
module_atlas.py" to "the provenance scanner refactor" / "the L-156
cluster." Checked against my own build plan: **no phase contains that
work.** MODULE_DOMAIN_MAP appears in my design only as a D10 cleanup
site. As written, the deferral points at a plan that doesn't include
it -- the floating-item failure class, and this review is the place it
gets caught.

Recommended fix: **the domain retirement joins Phase 3**, explicitly,
gated on "L-163 sweep complete" (the tags must exist before the scanner
can import them). Phase 3 is the natural home because it already edits
MODULE_DOMAIN_MAP for D10's cleanup -- folding the retirement in means
one scanner edit instead of two, and per 2a it deletes the D10 cleanup
site outright. Phase 1 was considered (it is "one coherent edit to
provenance_scanner.py") and rejected: gating Phase 1 on the full
121-module sweep would couple my cluster's critical path to L-163's
longest task, whereas Phase 3 already sits behind Phases 1-2 and the
sweep can complete in that window. Ledger action: add the gate and the
phase assignment to L-156's (or L-163's) Gap text so no build session
has to rediscover this.

### 2c. The sweep changes scan scope -- sequence it before L-157's
### worksheet is drafted, and re-baseline the counts

The scanner's own comments confirm ROLE_MAP "drives which files get
SCANNED at all." L-163's sweep gives real roles to 19 modules currently
invisible to scanning, five of which carry claim-shaped content --
`shell_configs.py` alone holds 91 strings. Executing the sweep therefore
**pulls new findings into the audit**, landing in the middle of finding
counts my cluster carefully calibrated: the 105-finding Tier-1 frontier
(D7's flood math), and L-161's 330-item Tier-2 queue.

This is not a problem -- it is the L-078 coverage-widening track working
as intended -- but it is an *unwritten sequencing dependency*. My D8.3
already records the precedent: every vocabulary extension has surfaced
hidden findings, so it sequences immediately before L-157 so new
findings land in the worksheet instead of as fresh Tier-1 noise.
Role-classification widening is the same class of event, and
`shell_configs.py` is literally shell-config geometry -- L-157's own
population. Recommended: (1) run the L-163 sweep, re-run the scanner,
and treat the post-sweep counts as the baseline my Phases 1-2 close
against; (2) draft L-157's worksheet only after the sweep, so the newly
visible shell_configs content is in scope from the start. One line in
L-157's ledger Gap captures both.

---

## 3. New scope (small, capture in the ledger)

**Sentinel terminology collision.** L-163 introduces `undetermined`
(role/domain); my cluster's amended D2 introduces `UNCLASSIFIED`
(criticality). Same semantics, different names, and both will eventually
appear in the same audit report. This is the identical trap L-163's own
Section 10 flags for `utility`/`utilities`. Recommend picking one term
for "could not classify, forced review" across both mechanisms -- or,
if they stay distinct, a one-line note in each report section saying the
other exists. My weak preference: adopt `undetermined` in both, since
L-163 ships first and the reports should read as one vocabulary.

**Minor notes, no action required:**
- L-163's Section 10 calls the domain fallback a silent default;
  verified at HEAD it is default-plus-visible-gap-note (the report lists
  unmapped files). "Tracked separately" in the same sentence already
  concedes this, so no correction needed -- but the accurate framing
  *helps* L-163's case: the existing pattern is closer to the new design
  than "silent" implies, making the upgrade an evolution, not a rescue.
- Retiring MODULE_DOMAIN_MAP/DOMAIN_LABELS removes two deliberately
  scored findings from the scanner's self-scan (my design's history
  notes them at Tier 3/4). The Phase 3 before/after diff discipline
  already covers this; noting so the delta isn't a surprise.
- Archiving `smoke_rotation_axis.py` removes its 1 claim-shaped string
  from the coverage gap by removing the file. Legitimate -- archival is
  one of the ways a coverage gap closes -- worth one word in the sweep's
  as-built so the count change is explained.

---

## 4. Answers to the three prompt questions, in one line each

1. **Citation and sequencing:** citation holds (it cites the gap-note
   pattern, which L-163 strengthens); L-163-first is correct; the 3b
   amendment and L-163's sentinel independently converged on the same
   design, which strengthens both.
2. **test_constants_provenance.py:** the read of D10 is exactly right;
   keep-tag-sweep-archive-later is the correct sequence; see 2a for the
   checklist refinement the new mechanism enables.
3. **Cluster internals:** one real gap found (2b -- the domain
   retirement's missing landing spot), one unwritten dependency (2c --
   sweep-before-L-157), one naming collision (Section 3). Pinning
   engine placement untouched by L-163 -- correctly left alone.

---

## Gap

- Ledger edits to make before either thread builds: add "domain
  retirement -> Phase 3, gated on L-163 sweep complete" (2b); add
  "sweep before L-157 worksheet drafting + post-sweep re-baseline" to
  L-157/L-163 (2c); record the sentinel-terminology decision (Section 3).
- Update D10's Phase 3 checklist wording per 2a when the build manifest
  is drafted.
- Everything else in L-163 proceeds as written, pending Tony's
  confirmations already listed in its own Gap (the 7 archive candidates,
  tag placement template).

## Ref

`ROLE_DOMAIN_CLASSIFICATION_HANDOFF.md` (reviewed document);
`DESIGN_HANDOFF_provenance_scoring_and_pinning.md` (D2, D6, D7, D8.3,
D10, Phases 1-4); `DESIGN_REVIEW_provenance_scoring_and_pinning.md`
(amendments 3a-3c, L-161, L-162);
`PREDESIGN_HANDOFF_provenance_scoring_and_gallery_scanner.md` (L-155
scope); `MASTER_PLAN_UPDATE_provenance_and_prep.md`;
`provenance_scanner.py` (lines 300-345 domain comment, 462-464
classify_domain, 1521-1600 gap notes), `module_atlas.py`,
`dep_trace.py` (get_category, ~line 156) -- all read at orrery HEAD
`bdab1674`; L-078, L-154 through L-163.

---

*Review written July 2026 with Anthropic's Claude Fable 5. Zero code
written or proposed; both repos read-only throughout.*
