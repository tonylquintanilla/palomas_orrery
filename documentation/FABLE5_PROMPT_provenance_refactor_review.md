# Review & Scoping Request: Provenance Scoring Refactor Cluster (L-155-L-162) + Priority Gaps

Tony Quintanilla, PE | Claude Sonnet 5 | July 26, 2026

**Built on** (verified live via `git ls-remote` this session, not recalled):
- orrery (palomas_orrery) @ `91a1bebe3bed8ce2bfcea22d58ca9b9046e058df`
- gallery (tonyquintanilla.github.io) @ `0f8e62ebf5fef86a134dfbbfbc2788bee894e51a`

**Type:** REVIEW & SCOPING (Mode 7, Collegial relay) -- zero code, zero build
manifest expected back. Your output here is the broad review/scoping step;
Opus 5 designs and builds from it next.

---

## Who you're writing for

Tony Quintanilla, PE, is a retired civil and environmental engineer, an
artist, and an anthropologist -- not a professional software developer and
not a formally trained astronomer. He builds this project (Paloma's Orrery,
~121 modules / ~92K lines, palomasorrery.com) as a "vibe coder": through
conversation with AI partners rather than writing code unassisted. He holds
sole commit authority and final judgment throughout, and owns the whole
workflow -- protocol, planning, handoffs, the ledger, and orchestrating this
exact multi-AI relay.

Important: the codebase's structure, docstrings, and engineering discipline
are the product of iterative Claude-Tony collaboration, not evidence of
Tony's own programming skill. Please don't read code quality as a signal
about his background. Unpack jargon rather than assume programmer or
astronomer fluency -- in your response as much as in anything you'd hand
back for a build.

---

## Why this review, right now

Paloma's Orrery is mid-build on an interactive web gallery (Phase 2 of a
client-side assembler). Artifact 1 (Earth) is built and Mode-5 accepted.
Artifact 2 (Jupiter/Saturn, rings + radiation belts) is next -- but it's
**blocked**: the JS feature-rendering layer it needs (L-154) surfaced a
provenance-scanner scoring problem while it was being scoped, and that
problem opened into its own design cluster (L-155 through L-162) that now
gates L-154, and therefore gates Artifact 2.

Separately, we just closed L-163 (today) -- the module/domain classification
refactor (`ROLE_MAP`/`MODULE_DOMAIN_MAP` -> docstring-driven, auto-
regenerated) -- which was itself groundwork for the provenance work, since
it's what widens the scanner's coverage. That's now done. This request is
the next step: a comprehensive read of where the provenance-scoring cluster
actually stands, before anyone builds anything else, plus a wider look at
what else on the ledger deserves attention before Phase 2 resumes.

---

## What's already verified at HEAD (re-verify, don't just trust this)

Checked directly against the SHA above this session. Please independently
confirm or correct each -- this project's whole discipline is fetched-not-
recalled, and I'd rather you catch my error than repeat it:

1. **The scanner build hasn't started.** `provenance_scanner.py` has none of
   the design's vocabulary yet -- no `MEASURED`/`RELATIONAL`/`UNCLASSIFIED`,
   no `Cross-checked` annotation handling, no `run_pinning_checks`, no
   `PINNING_MAP`. Phases 1 and 3 of the design's 4-phase build sequencing
   are both still at zero.
2. **L-162's prep work hasn't started.** `constants_new.py` still only
   names Sun, Earth, and Jupiter; the other 15 `CENTER_BODY_RADII` bodies
   are still dict-only, undifferentiated as one scanner row.
3. **The D3 Gemini calibration -- the design review's own stated "next
   concrete action" -- doesn't appear to have happened.** No worksheet or
   result document for it exists anywhere in `documentation/`.
4. **L-155 through L-160 have no dedicated ledger entries.** `L-161` and
   `L-162` were fully drafted, ledger-formatted, in
   `DESIGN_REVIEW_provenance_scoring_and_pinning.md` (July 23) but that text
   was never pasted into `LEDGER_CONSOLIDATED.md` -- none of L-155-162
   appear in the ledger's INDEX. Worth checking this isn't the ledger's own
   named failure mode ("floating items get lost") happening to itself.
5. **`PROVENANCE_AUDIT.md` at HEAD is dated July 17 (105 Tier-1 findings)
   and predates today's L-163 close.** L-163's own ledger entry (status
   DONE, updated today) notes an in-sandbox rescan under the widened
   `classify_role` coverage surfaced 105 -> 145 Tier-1, and records that
   reconciling this against a real baseline is deliberately sequenced
   *behind* the L-154-162 cluster -- a call the ledger says Tony confirmed
   in chat today. Worth a sanity check against everything else you find.
6. **L-163's own Phase 4 status is ambiguous in the ledger text.** The
   entry both notes an outstanding "Phase 4 (do)" gap (rewriting two
   skills off the retired `ROLE_MAP` model) and, separately, the skill
   files at HEAD already show `provenance-discipline` at v1.2 and
   `ledger-and-session-records` at v1.4, both stamped as cut from
   `palomas_orrery` today. Please resolve which is actually current.

---

## What to read

Base URL for everything below:
`https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/main/`

**Read these first:**
- `LEDGER_CONSOLIDATED.md` -- search `[L-163]` for the just-closed entry,
  and the INDEX header for current open-item counts
- `PROVENANCE_AUDIT.md` -- the July 17 snapshot described above
- `provenance_scanner.py`
- `constants_new.py`
- `documentation/DESIGN_HANDOFF_provenance_scoring_and_pinning.md` -- your
  own design, July 22 (D1-D10)
- `documentation/DESIGN_REVIEW_provenance_scoring_and_pinning.md` -- Sonnet
  5's independent re-verification and amendments (D2, D5, D7 changed; L-161
  and L-162 drafted here)
- `documentation/MASTER_PLAN_UPDATE_provenance_and_prep.md` -- the
  sequencing note tying this cluster to the gallery blockage

**Reference as needed:**
- `documentation/PREDESIGN_HANDOFF_provenance_scoring_and_gallery_scanner.md`
- `documentation/HANDOFF_gallery_feature_layer_L154_resume.md` -- what
  L-154 needs once this cluster closes
- `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md` -- sections 5a and 6
- `MODULE_ATLAS.md`, `module_atlas.py`,
  `documentation/ROLE_DOMAIN_CLASSIFICATION_HANDOFF.md`,
  `documentation/AS_BUILT_L163_phase3b_close.md` -- the classification
  track that just closed and is why scanner coverage just widened
- `skills/provenance-discipline/SKILL.md`,
  `skills/ledger-and-session-records/SKILL.md` -- current conventions

---

## The ask

1. **Verify, don't summarize.** Reason from the fetched source itself
   rather than trusting anything above, including my six numbered findings.
   Flag anywhere your read differs.
2. **Give Tony a clean current-state map of L-155 through L-162**: what's
   actually decided, what (if anything) is built, what's genuinely still
   open -- resolved against live HEAD, not against what the design documents
   claim about themselves.
3. **Propose a sequenced path to close the cluster**, building on (or
   revising) the design review's own ordering: Gemini D3 calibration ->
   L-162 prep -> scanner Phases 1-3 -> L-161's Gemini sweep -> ledger
   formalization. Say plainly where you'd change that order and why.
4. **Widen the lens.** Look across `LEDGER_CONSOLIDATED.md`'s other open
   items (Section A "Active Separate Tracks" and D.Priority especially) for
   anything that intersects with, or should be weighed against, Phase 2
   gallery work resuming. L-114 (`objects_config.json` stranded by the
   atomic swap, also blocking crash-recovery in the gallery builder) carries
   the highest RICE score of anything currently open on the ledger -- worth
   an honest look, not a presumed verdict.
5. **Surface what we haven't asked about.** Gaps, drift, stale claims, or
   genuine opportunities you notice reading broadly. This is explicitly
   broad-first work -- a checklist closeout isn't the goal.

## What this isn't

No code, no scanner diffs, no build manifest -- that's Opus 5's job once
this scoping lands. Zero code written or proposed, same as your July 22
design session.

## Where this goes next

Tony carries your review back into this thread. From there: Opus 5 designs
and builds against it; Gemini takes any remaining fact-level cross-checks
(the D3 calibration question, if it's still open, chief among them); Tony
does the Mode 5 visual/judgment review; GPT gets pulled in for selective
design cross-checks if needed; I (Sonnet 5) handle orchestration and
as-built verification once building starts. You're the broad review and
scoping step in that chain -- reason freely, and don't feel bound to the
sequencing proposed above if you see a better one.

---

*Review requested July 2026 with Anthropic's Claude Sonnet 5.*
