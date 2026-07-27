# Review & Scoping -- Provenance Scoring Refactor Cluster (L-155-L-162) + Priority Gaps

Tony Quintanilla, PE | Claude Fable 5 | July 26, 2026

**Built on** (both verified live via `git ls-remote` and fresh shallow
clones this session, not recalled; both match the requesting prompt's
anchors exactly):
- orrery (palomas_orrery) @ `91a1bebe3bed8ce2bfcea22d58ca9b9046e058df`
- gallery (tonyquintanilla.github.io) @ `0f8e62ebf5fef86a134dfbbfbc2788bee894e51a`

**Type:** REVIEW & SCOPING (Mode 7, Collegial relay). Zero code written or
proposed. Every claim below was checked against the fetched clones this
session; where a check could be *run* rather than read (the offline test
suite, JSON contents), it was run.

**Companion:** `FABLE5_PROMPT_provenance_refactor_review.md` (Sonnet 5's
request), `DESIGN_HANDOFF_provenance_scoring_and_pinning.md` (my July 22
design), `DESIGN_REVIEW_provenance_scoring_and_pinning.md` (Sonnet 5's
July 23 review).

---

## 1. Verification of the six numbered findings

All six were independently re-checked against the clones, not taken from
the prompt. Verdicts, with refinements where my read differs:

**Finding 1 -- CONFIRMED.** `provenance_scanner.py` at HEAD contains zero
occurrences of `MEASURED`, `RELATIONAL`, `UNCLASSIFIED`, `Cross-checked`,
`run_pinning_checks`, or `PINNING_MAP` (grep-counted individually, all
zero). Phases 1 and 3 of the build sequencing have not started.

**Finding 2 -- CONFIRMED, with one phrasing refinement.** Only three
named primary constants exist (`SUN_RADIUS_KM`, `EARTH_EQUATORIAL_RADIUS_KM`
+ polar, `JUPITER_EQUATORIAL_RADIUS_KM` + polar). Zero named constants
exist for the other 15 bodies, and `CENTER_BODY_RADII` still duplicates
the three primaries as raw literals (695700, 6378.137, 71492) rather than
referencing the names -- so even D5's original 3-body minimum hasn't been
applied. The refinement: every dict entry DOES carry an inline per-value
citation comment (Mercury through Planet 9, each attributed), so a reader
skimming the dict could wrongly conclude the prep is done. What L-162
requires -- promotion to named module-level constants, each becoming its
own scanner row -- has not started. The dict is well-cited but still
scores as one undifferentiated row.

**Finding 3 -- CONFIRMED.** No D3 calibration worksheet or result exists
anywhere in `documentation/`. The only files matching "D3" are the
unrelated shell-consolidation phase D3.1 series from an earlier track. The
only mentions of "calibration" in the whole documentation tree are inside
the two provenance design documents themselves. The design review's own
stated gate -- "the design should not be treated as build-ready until this
comes back" -- is unmet, and the worksheet it depends on has never been
drafted.

**Finding 4 -- CONFIRMED, and it is slightly WORSE than stated.** Zero
dedicated `#### [L-NNN]` ledger entries exist for the entire cluster --
and that includes **L-154 itself**, not just L-155-162. Grep for headers:
nothing between L-151 and L-163. The mentions of L-156, L-157, and L-160
that do exist in `LEDGER_CONSOLIDATED.md` are all cross-references from
the L-163 entry's Note/Gap/Ref text, not entries. So the item gating
Artifact 2, and its entire eight-item detour, live only in handoff
documents -- the ledger's own named failure mode ("floating items get
lost; capture on first mention"), running for four days on the project's
current critical path. Mitigating fact that makes the fix cheap: the
predesign handoff already contains fully ledger-formatted blocks
(header + metadata line + Gap + Ref) for L-154, L-155, L-156, L-157,
L-158, L-159, and L-160, and the design review contains the same for
L-161 and L-162. Formalization is mostly paste-and-update, not drafting.

**Finding 5 -- CONFIRMED.** `PROVENANCE_AUDIT.md` at HEAD is generated
July 17, 2026, and its risk-matrix table records Tier 1 = 105. The L-163
ledger entry (status DONE, upd 2026-07-26) records the in-sandbox 105->145
jump under widened `classify_role` coverage, explicitly marks *neither
number authoritative*, and records Tony's chat-confirmed decision that
baseline reconciliation is sequenced behind the L-154-162 cluster and does
not gate anything. Consistent with everything else found. One operational
note for every downstream session: until reconciliation, nobody should
cite either count as current -- the provenance-discipline skill's own
field note (stale committed audit copies) applies squarely here.

**Finding 6 -- RESOLVED: Phase 4 is DONE; the ledger's Gap prose is
stale.** The evidence stack: (a) `AS_BUILT_L163_phase4.md` exists,
built on orrery `ca9c706e`, describing all four edits applied;
(b) the skill files at HEAD carry the new content -- I read both:
`provenance-discipline` v1.2's role-driven-inclusion bullet and
`ledger-and-session-records` v1.4's Codebase Tooling bullet both describe
the regenerated-mirror model, exactly as Phase 4 scoped; (c) the Skill
Manifest zone in `PROJECT_INSTRUCTIONS.md` at HEAD reads 1.2 / 1.4 --
`skills_index.py` was run, closing the pre-existing manifest drift the
Gap text mentions; (d) `AS_BUILT_L163_closeout_L164.md` shows the
subsequent session flipped L-163's status to DONE and added L-164 -- but
its three edits did not include rewriting the Gap paragraph. So the
ledger now carries a DONE item whose Gap field still reads as an
outstanding to-do. One-line ledger fix: rewrite or strike the Phase 4
Gap text (the closed archive keeps the entry; the Gap just shouldn't
describe finished work as pending).

---

## 2. Current-state map: L-154 through L-162

Resolved against live HEAD. "Design settled" below means settled by the
design handoff as amended by the design review; "built" means code at
HEAD.

| Item | Decided | Built | Genuinely open |
|------|---------|-------|----------------|
| L-154 | Architecture ratified (JS renders features; Python never builds geometry). Three design questions captured in the resume handoff. | Nothing -- no feature-rendering JS exists anywhere in the gallery repo | The three design questions; PLUS a false claim in its own resume handoff (section 5 below) |
| L-155 | D6 (engine placement, PINNING_MAP, AST extraction, loud gallery-absent skip) + D7 as amended (hard exit for pinning only) | Nothing | Build (Phase 3); cross-repo rows activate with L-157 |
| L-156 | D1 (MEASURED/RELATIONAL), D2 as amended (explicit unclassified state + banner), D3 floor logic, D8 sweep resolutions | Nothing | D3 numbers unverified (calibration gate); build (Phases 1-2); naming conformance note below |
| L-157 | Scoped; gains D3-ladder calibration question + magnetosphere-vocabulary sequencing | Nothing | Worksheet drafting; Mode 7 relay (build Phase 4) |
| L-158 | D9: derived rung = V1 via two-factor check (`# Derived:` comment + AST confirms computed) | Nothing | Build (rides Phase 1) |
| L-159 | Annotation convention named (`# Illustrative:`); Planet 9 attached as a case by the review | Nothing | Enforcement-check design pass, deliberately deferred -- stays open past this cluster |
| L-160 | Retire recommended (design) and confirmed (review); five reference sites enumerated | Nothing -- file still at HEAD with all five sites (L-163 Phase 1 deliberately did NOT archive it, correctly waiting for this) | Tony's explicit call may be unrecorded (section 2a); execution rides Phase 3 |
| L-161 | Fully drafted, ledger-formatted, re-sequenced AFTER the build ships | Nothing | Paste into ledger; worksheet work post-Phase-1/2 |
| L-162 | Fully drafted: 15 promotions, Planet 9 excluded, before Phase 3 | Nothing (verified precisely -- finding 2) | Dedicated Sonnet prep session |

**2a. The five Tony calls -- partially unrecorded.** The design handoff's
section 4 reserved five decisions explicitly for Tony. Tracing what the
review actually records: call 5 (Tier-1 exit timing) was superseded by
the D7 amendment; call 2's judgment rides the D3 calibration either way;
the D2 amendment is explicitly marked "Tony's design" and the banner
"Tony's call." But calls **1** (ring geometry in MEASURED), **3**
(period-vs-radius same tier), and **4** (retire vs. wrapper) are
confirmed in the review *by Sonnet's analysis* -- the review's own
convention of marking Tony's calls explicitly ("Tony's call," "corrected
on Tony's call") implies the unmarked confirmations were the reviewer's,
not Tony's. They may well have been settled in chat; the record doesn't
show it. Ledger formalization is exactly where these get captured --
three one-line **(decide)** items, or three one-line confirmations if
already made.

**2b. Naming conformance for the builder.** The L-163 ledger entry
records Tony's decision: the sentinel name is **`undetermined`**, and
"the L-156 cluster's `UNCLASSIFIED` conforms to this name, not the other
way around." The design review's D2 amendment predates that decision and
uses `UNCLASSIFIED` literally. Whoever builds Phase 1 should implement
the concept from the review under the name (or naming pattern) from
L-163's decision -- flagged here so the build doesn't faithfully
implement a superseded label.

---

## 3. Proposed sequencing (revised)

The proposed order was: D3 calibration -> L-162 -> Phases 1-3 -> L-161 ->
ledger formalization. One structural change, one insertion, everything
else preserved:

**Move ledger formalization from LAST to FIRST.** Three reasons. It is
nearly free -- the blocks are already drafted and ledger-formatted in the
predesign and review; the work is paste, status-update per the design
outcomes, `ledger_index.py`, push. It closes a live instance of the
project's own named failure mode on the critical path -- nine floating
items, four days and counting, including the item that gates Artifact 2.
And it creates the channel the rest of the sequence needs: the three
unrecorded Tony calls (2a) and the stale-item closeouts (section 4)
belong in ledger blocks with **Tony:**/**(decide)** tags, which cannot
exist until the blocks do. Formalizing last means running the entire
build with the backlog living in prose documents -- the exact drift class
the ledger exists to kill.

**The full revised order:**

1. **Ledger + record hygiene session** (one session, cheap, ledger-only):
   paste L-154-L-162 blocks; update statuses per design + review; record
   or capture the three Tony calls; fix L-163's stale Gap prose; close
   L-114 and likely L-120 with verification tags (section 4); correct the
   L-154 resume handoff's resolver claim (section 5). Also draft the D3
   calibration worksheet in this same session -- it's small, and step 2
   can't start without it.
2. **D3 Gemini calibration** (Tony-side, Mode 7): carry the worksheet to
   Gemini. This runs in parallel with step 3 -- it gates the *scanner
   build*, not the constants prep.
3. **L-162 prep session** (Sonnet, dedicated, as scoped): 15 promotions,
   Planet 9 excluded, dict rewritten to reference the names,
   safe-file-editing discipline. Independent of D3's answer.
4. **Scanner build, Phases 1-3** (Opus 5, per the amended design), gated
   on D3 returning clean. If Gemini pushes back on V=1/V=3, D1 and D7 get
   the second look the review already flagged before any code. Build
   notes for Opus 5: the `undetermined` naming conformance (2b); the
   scanner-scans-itself delta discipline (provenance-discipline field
   note); Phase 1 closes with a line-by-line before/after audit diff.
5. **Phase 4 relay (L-157)**, then **L-161's sweep** -- sequentially
   through the same Gemini channel, as the review already re-sequenced.
6. **Gallery re-entry:** land the resolver one-liner (section 5) in the
   first gallery build session; L-154 resume design session against the
   corrected handoff; Artifact 2.

Steps 2 and 3 are genuinely parallel; nothing else is. The review's
own gate order (scoring before Gemini sweep; pinning activates only
against cross-checked numbers) is preserved intact.

---

## 4. The wider lens: what the ledger says vs. what HEAD says

I checked the top-scored open items in Section A, D.Priority, and
W.Active against live code, and ran the checks where runnable. Three of
the four highest-visibility "open" items are stale in the same direction:

**L-114 (RICE 16.2, highest on the ledger) -- appears DONE at HEAD;
its own acceptance check passes.** The ledger entry (upd 07-12) says the
config file moved but the builder still defaults to the old path. At
gallery HEAD, all four Gap edits have landed: the builder's `--config`
default is `data/objects_config.json` (line 1450), the module docstring
describes the new home, `test_gallery_cache_builder_offline.py` resolves
the sibling path (its comment even says "updated L-114"), and
`TESTING_PROTOCOL.md` line 25 carries the new prose. The entry's stated
acceptance check was "re-run the offline suite from a clean clone" -- I
did, this session, from a fresh shallow clone: **PASS, 138 checks, 0
failures.** Recommend: Tony confirms nothing local is un-pushed, then
flip to DONE with `[verified @0f8e62e]`. This removes the presumption
that D.Priority holds a major open blocker -- it doesn't.

**L-120 (RICE 7.6, "Halley not yet in the served index") -- likely
stale.** At gallery HEAD, `coverage_index.json` serves 12 objects
including `halley` and `encke`, and `served_window` is populated (not
null). The item as titled is satisfied. Whether a residual (a Mode-5
Halley render check, or the artifact-4 build itself) keeps a narrowed
version open is Tony's call -- but the entry as written no longer
describes HEAD.

**L-118 (DONE) -- confirmed genuinely done**, not just claimed:
`feature_configs.json` at HEAD is populated with full per-object params
(12 objects; Earth atmosphere shells, Jupiter/Saturn ring geometry all
present, derived from `objects_config.json` as designed). Worth stating
because it sharpens what actually blocks Artifact 2: the data is served
and populated; only the JS layer (L-154) and the resolver line (section
5) stand between the served cache and a rendered Jupiter.

**L-121 and L-122 -- verified genuinely still open** (no plotly wheel
anywhere in the gallery repo; `data/solar-system.prev_old/` still
committed). L-122 is minutes of work and could ride any gallery session.

**Pattern worth naming:** three high-scored items checked, two stale-open
and one stale-in-Gap (L-163). The ledger's own field note -- "the v28
consolidation found open items already done" -- is recurring. The
formalization session (step 1) should include a quick verification sweep
of W.Active and D.Priority statuses while it has both clones open. This
is cheap insurance against RICE-driven planning being steered by scores
attached to finished work.

**Independent of the cluster:** L-062 (README refresh, 5.1, top of
Section A) has no dependency on any of this and can interleave whenever a
session opens; the Tier-1 baseline reconciliation stays parked behind the
cluster per Tony's recorded call -- no change proposed.

---

## 5. What nobody asked about: two stale claims on the resume path

**5a. The "settled resolver bug" is NOT fixed at HEAD -- and the resume
handoff says it is.** This is the most consequential thing this review
found. `HANDOFF_gallery_feature_layer_L154_resume.md`, section 1,
"Already confirmed, not open," states: *"The resolver bug (params
silently dropped by `tuple(dict)` in `resolver.py`) is fixed and settled
-- small, targeted, not an architecture question."* At gallery HEAD,
`resolver.py` line 133 still reads `features = tuple(rec.get("features")
or ())` -- and `objects_config.json`'s `features` values are dicts full
of params (verified by loading the JSON: Earth's atmosphere fractions,
Jupiter's ring radii, all present), so `tuple(dict)` still keeps keys
only and drops every parameter. The design handoff had this right: the
fix was *decided*, "can land whenever a gallery build session next
opens." The resume handoff promoted decided to done. Since that handoff
exists precisely so a future session can resume L-154 without
re-deriving context, a builder trusting it would skip the fix and then
debug a mystery downstream. This is the handoffs-are-claims failure in
its cleanest form, caught before it cost anything. Fix: one annotation
to the resume handoff (or a correction note in L-154's new ledger
block), plus the one-liner itself in the next gallery build session.
Whether the JS layer should even consume params via the resolver versus
reading `feature_configs.json` directly is one of L-154's own open
design questions -- not adjudicated here; but whichever way that lands,
the handoff must stop claiming the fix exists.

**5b. Same handoff, same pattern, second instance.** The resume
handoff's section 1 also describes `CENTER_BODY_RADII` as "now with all
bodies individually named, per L-162" -- present tense, for work that has
not started (finding 2). Its preamble does say "the provenance work
should already be done" when read -- so this is deliberate
future-as-present framing, not an error -- but it is the same shape as
5a, and 5a proves a reader can miss the preamble. The correction note
from 5a should cover both lines: one sentence marking section 1's
claims as "true only after the detour closes; verify at HEAD on
resume."

**5c. Small observations, captured so they don't float:**
- The L-163 entry's Ref line and Note reference "L-154-162" as a cluster
  -- once the blocks exist (step 1), those references resolve to real
  entries instead of dangling handles. No action beyond step 1 itself.
- `PROVENANCE_AUDIT.md`'s July 17 snapshot will now disagree with any
  fresh scan in two ways at once (the L-163 coverage widening AND, once
  Phase 1 ships, the rescored tiers). The reconciliation item Tony
  already sequenced should regenerate the committed audit as its closing
  act, so the repo copy and reality reconverge in one move.
- L-160's target file still existing at HEAD is correct, not drift --
  L-163 Phase 1 explicitly declined to archive it because "its L-160
  absorption target doesn't exist yet." The sequencing discipline held.
  Noted so nobody "fixes" it early.

---

## 6. Consolidated Tony-action rollup

Per the ledger-and-session-records rollup rule -- every Tony-action item
above, in one place:

- **(decide)** Confirm or issue the three design calls: ring geometry in
  MEASURED; period-vs-radius sharing the top tier; retire (vs. wrapper)
  for `test_constants_provenance.py`. All three recommended-yes by both
  design and review; only your word closes them. (Section 2a.)
- **(decide)** L-114: confirm no un-pushed local edits remain, then
  approve flipping it to DONE. (Section 4.)
- **(decide)** L-120: closes outright, or narrows to a named residual?
  (Section 4.)
- **(do)** Carry the D3 calibration worksheet to Gemini once step 1
  drafts it; carry the result back. (Section 3, step 2.)
- **(do)** After the step-1 ledger session lands: commit + push via
  GitHub Desktop, then paste the new HEAD SHA into the thread so the
  next session builds on ground truth.

Nothing here requires an operation outside your known working set --
every (do) is a GitHub Desktop commit/push or a copy-paste relay you
already run daily.

---

## 7. Bottom line

The cluster's design is genuinely in good shape -- decided, reviewed,
amendments reconciled, with exactly one open verification gate (D3) that
was correctly identified two sessions ago and simply never executed.
Nothing in the design needs re-litigating. What the cluster needs is not
more thinking but *recording and sequencing*: nine items into the ledger,
three calls onto the record, one worksheet to Gemini, two stale claims
corrected on the resume path, and two finished items closed so the
priority board tells the truth. Then the build order the review proposed
runs essentially as written. The most important single sentence for
whoever opens the next session: **the resolver fix has not landed, no
matter what the resume handoff says.**

---

*Review written July 2026 with Anthropic's Claude Fable 5. Zero code
written or proposed; both repos read-only throughout; every runnable
check (offline suite, JSON loads, greps) executed against fresh clones
at the pinned SHAs.*
