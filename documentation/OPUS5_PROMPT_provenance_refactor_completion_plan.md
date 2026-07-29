# Request: Provenance Refactor Cluster -- Completion Plan + Gaps + Priority Cleanup

Tony Quintanilla, PE | Claude Sonnet 5 | July 28, 2026

**Built on** (both verified live via `git ls-remote --symref` this session,
matching Tony's stated anchors exactly -- re-verify before you build anything
on either, since HEAD moves):
- orrery (palomas_orrery) @ `8ca3de8f111ee5495edbb6d4fb50f590278ff673`
  at https://github.com/tonylquintanilla/palomas_orrery (branch main)
- gallery (tonyquintanilla.github.io) @ `f4ce24cb68d2aa5834c6abcf98a1d7e0d5a68e8a`
  at https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main)

**Type:** REVIEW & SCOPING -> PRELIMINARY DESIGN HANDOFF (Mode 7, Collegial
relay). Zero code expected back -- your deliverable is a document, not a diff.

**Companion (read these; full list below):**
`PREDESIGN_HANDOFF_provenance_scoring_and_gallery_scanner.md` (Sonnet 5,
Jul 22) -> `DESIGN_HANDOFF_provenance_scoring_and_pinning.md` (Fable 5,
Jul 22) -> `DESIGN_REVIEW_provenance_scoring_and_pinning.md` (Sonnet 5,
Jul 23) -> `REVIEW_provenance_refactor_cluster_scoping.md` (Fable 5, Jul 26)
-> `LEDGER_SESSION_provenance_cluster_formalization.md` (Sonnet 5, Jul 27)
-> `HANDOFF_L162_scope_gaps.md` (Sonnet 5, Jul 28, unresolved). You are the
next link in that chain.

---

## Who you're writing for

Tony Quintanilla, PE, is a retired civil and environmental engineer, an
artist, and an anthropologist -- not a professional software developer and
not a formally trained astronomer. He builds this project (Paloma's Orrery,
~121 orrery modules + ~24-27 gallery modules, palomasorrery.com) as a "vibe
coder": through conversation with AI partners rather than writing code
unassisted. He holds sole commit authority and final judgment throughout,
and owns the whole workflow -- protocol, planning, handoffs, the ledger, and
orchestrating this exact multi-AI relay. Sonnet 5 (me) is handling
orchestration and as-built review; you are the design/build specialist for
this track.

The codebase's structure, docstrings, and engineering discipline are the
product of iterative Claude-Tony collaboration, not evidence of Tony's own
programming skill -- please don't read code quality as a signal about his
background. Unpack jargon rather than assume programmer or astronomer
fluency, in your handoff as much as in anything you'd hand back for a build.

---

## Why this, now

Phase 2 of the interactive gallery (client-side assembler) is mid-build.
Artifact 1 (Earth) is built and Mode-5 accepted. Artifact 2 (Jupiter/Saturn,
rings + radiation belts) is next in the artifact order but **BLOCKED**: the
JS feature-rendering layer it needs (L-154) surfaced a provenance-scanner
scoring problem while it was being scoped in July, and that problem opened
into its own design cluster -- L-155 through L-162 -- that now gates L-154,
and therefore gates Artifact 2.

Since `REVIEW_provenance_refactor_cluster_scoping.md` (Fable 5's broad
review, Jul 26) and the ledger-formalization pass (Jul 27) that followed it:

- **L-163** (module role/domain classification -- `ROLE_MAP` retired as a
  hand-maintained dict, now regenerated from docstring tags) has gone from
  "in progress" to **fully CLOSED, all 4 phases, both repos** -- this was
  the coverage-widening groundwork the scanner scoring fix depends on.
- **The one open design fork in the cluster** -- how the Vulnerability
  ladder should treat cross-checked vs. merely-cited values -- closed via a
  three-AI calibration round (Gemini 3.1 Pro, GPT 5.5, Fable 5, Sonnet 5
  synthesis, Tony's final call), landing in `L-156`.
- **A fresh, still-unresolved scope gap surfaced on `L-162`** the day after
  formalization (`HANDOFF_L162_scope_gaps.md`, Jul 28) -- see below. It is
  NOT yet reflected as a `**Note:**` in the ledger's `[L-162]` block.

So: design is closed, the ladder is decided, the ledger has all nine items
as their own DETAIL blocks -- but **zero scanner code has been written**,
and one implementation decision that would trip up a build session is still
sitting open. This request asks you to do what the master plan's own "Next
Step" already names as your job (`MASTER_PLAN_INTERACTIVE_GALLERY.md`
S5a) -- **build the scanner's Phases 1-3** -- but as a **planning pass
first**: reconcile everything against live HEAD, close the open
implementation question, and hand back a build-ready plan for Tony and me
to sign off on before code gets written.

---

## What's already verified at HEAD (re-verify, don't just trust this)

Independently confirmed this session, live against the orrery SHA above --
not taken from any document's own claim about itself:

- **`L-163` is genuinely done.** `module_atlas.py` exports `classify_role`;
  `provenance_scanner.py` imports it (`from module_atlas import
  build_dependency_graph, classify_role`). `ROLE_MAP` is a generated mirror
  now, not hand-maintained.
- **`L-155`/`L-156` -- zero code written.** Grepped `provenance_scanner.py`
  for `MEASURED`, `RELATIONAL`, `UNCLASSIFIED`, `undetermined`,
  `Cross-checked`, `run_pinning_checks`, `PINNING_MAP`: **zero hits, all
  seven terms.** The scoring model and the pinning engine are still 100%
  design, 0% code.
- **`MODULE_DOMAIN_MAP` is still hand-maintained** inside
  `provenance_scanner.py` (`MODULE_DOMAIN_MAP = {` at line 353,
  `classify_domain()` at line 468) -- the L-163-follow-on retirement in
  favor of importing domain from `module_atlas.py` (an `L-156` Phase-3
  Gap item) has not happened.
- **`L-162` -- not started, and the gap is worse than "not started."**
  `constants_new.py` at HEAD carries exactly 3 named radius constants
  (`SUN_RADIUS_KM`, `EARTH_EQUATORIAL_RADIUS_KM` + `_POLAR_`,
  `JUPITER_EQUATORIAL_RADIUS_KM` + `_POLAR_`). `CENTER_BODY_RADII` still
  hardcodes those same three as raw literals (`695700`, `6378.137`,
  `71492`) rather than referencing the names, and the other 14 bodies
  (Mercury, Venus, Moon, Mars, Phobos, Saturn, Uranus, Neptune, Pluto,
  Bennu, Eris, Haumea, Makemake, Arrokoth -- Planet 9 excluded, see
  `L-159`) are still plain dict entries, each with a good inline citation
  but no named constant of its own.
- **`L-164` confirmed still present.** `dep_trace.py` has exactly 1279
  non-ASCII bytes across its 8 section-divider lines (byte-counted
  directly, not estimated).
- **`PROVENANCE_AUDIT.md` on disk is a July 17 snapshot generated under
  the OLD 4-rung vocabulary** (Fetched/Sourced/Stale/Recalled), not the new
  one (`FETCHED`/`CROSS-CHECKED`/`SOURCED`/`RECALLED`) `L-156` decides.
  Its printed `Tier 1 = 105` is stale on two counts: it predates `L-163`'s
  Phase 3b coverage-widening (which alone moved the in-sandbox number to
  145, per the ledger -- "neither number authoritative"), and it will read
  differently again once the ladder itself changes. Don't cite it as
  current in your plan; note it as a baseline that gets superseded by a
  fresh scan once `L-156` lands.
- **`L-168`** (gallery repo, `render_orbits.py::propagate_marker`, wrong
  solar-`K_GAUSS` mean motion for planetocentric moon markers) is still on
  the live dispatch path (`assemble.py:62`), coupled to the same trigger
  event as `L-154` -- dormant today only because Artifact 1 (Earth) is
  heliocentric. Not part of the provenance cluster itself, but gates the
  same resume point; see the priority-cleanup ask below.

Current RICE ordering for the whole gallery-active section, straight from
the ledger's generated index (`LEDGER_CONSOLIDATED.md` INDEX zone,
`### W.Active`), for your own prioritization sense -- verify these are
still current, don't assume:

| L# | Item | Status | RICE |
|----|------|--------|-----:|
| L-160 | Retire test_constants_provenance.py | OPEN | 8.1 |
| L-162 | CENTER_BODY_RADII de-duplication | OPEN | 8.1 |
| L-158 | Derived-constant vulnerability inheritance rule | OPEN | 5.6 |
| L-156 | Scanner scoring model fix | OPEN | 5.3 |
| L-155 | Cross-repo pinning checks | PENDING-GATE | 4.5 |
| L-168 | propagate_marker solar-GM bug | OPEN | 3.6 |
| L-161 | Gemini display-string sweep | OPEN | 3.1 |
| L-157 | Gemini shell-config cross-check | OPEN | 2.5 |
| L-154 | Gallery feature-rendering JS layer | BLOCKED | 2.1 |
| L-159 | Disclosed-approximation check | OPEN | 1.2 |

(`L-164` sits outside `W.Active`, in `D.Structural`, RICE 0.9 -- independent
cleanup, not gallery-gated. `L-078`, the parallel provenance-coverage
track, sits in `A. Active Separate Tracks`, RICE 0.9.)

---

## The fresh gap -- not yet in any plan

`HANDOFF_L162_scope_gaps.md` (Jul 28, the most recent document in this
whole chain) opened a session to execute `L-162` and found two
implementation questions that **no prior document answers**, blocking any
file edit:

1. **Naming convention.** Plain (`MARS_RADIUS_KM`, matching
   `SUN_RADIUS_KM`) or type-labeled (`MARS_EQUATORIAL_RADIUS_KM`, matching
   the `EARTH_EQUATORIAL_`/`_POLAR_` pattern used only where a body has two
   values)? The handoff leans plain (every one of the 14 targets is a
   single-value body, like Sun) but flags it as Tony's call, since your
   Phase 3 pinning engine references whatever names land here.
2. **Sun/Earth/Jupiter's own literal duplication.** `CENTER_BODY_RADII`
   still hardcodes their three values instead of referencing the existing
   named constants -- the original 3-body minimum never actually landed.
   `L-156`'s own Gap line reads "fix the `CENTER_BODY_RADII` duplication
   per `L-162`" -- worded as if the *whole* duplication problem belongs to
   `L-162`, in tension with `L-162`'s own detail block, which scopes to
   just the 14 *remaining* bodies. Neither is wrong on its face; they just
   haven't been reconciled.

**Resolve these in your plan, don't just re-flag them.** A build session
needs an answer, not another open question. Propose the naming convention
and state explicitly which item (`L-162` or `L-156`) owns the
Sun/Earth/Jupiter fix, with your reasoning -- Tony can override either call
when he reviews your handoff, but hand him a decision to approve, not a
fork to resolve from scratch.

One more small correction already caught and worth carrying forward: **"15
remaining bodies" should read 14** everywhere it appears (18 dict keys - 3
done - Planet 9 excluded = 14). The named list itself has always been
correct; only the count label is off by one.

---

## What to read

Base URL for raw fetches:
`https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/main/`

**Read first:**
- `LEDGER_CONSOLIDATED.md` -- search `[L-154]` through `[L-164]`, and
  `[L-078]` and `[L-168]` separately; the generated INDEX zone near the top
  for current RICE/status at a glance
- `provenance_scanner.py`, `constants_new.py`, `module_atlas.py`,
  `dep_trace.py` -- the actual code the plan has to land on
- `documentation/HANDOFF_L162_scope_gaps.md` -- the fresh, unresolved gap
- `documentation/DESIGN_HANDOFF_provenance_scoring_and_pinning.md` (Fable
  5's design, D1-D10) and `documentation/DESIGN_REVIEW_provenance_scoring_and_pinning.md`
  (Sonnet 5's amendments -- D2, D5, D7 changed; L-161/L-162 drafted here)
- `documentation/REVIEW_provenance_refactor_cluster_scoping.md` (Fable 5's
  broad review, Jul 26 -- current-state map, proposed sequencing, the
  Tony-action rollup)
- `documentation/LEDGER_SESSION_provenance_cluster_formalization.md`
  (Sonnet 5, Jul 27 -- how all nine items got their own ledger blocks, and
  the D3 vulnerability-ladder calibration close-out)
- `documentation/D3_calibration_worksheet_vulnerability_ladder.md` -- the
  four-rung ladder's evidence base (Arrokoth, Parker Solar Probe, the
  anchoring near-miss, the Gemini-cross-check-itself-wrong case)
- `MASTER_PLAN_INTERACTIVE_GALLERY.md` sections 5a (Execution Map,
  including "Next Step") and 6 (Prep Work) -- current plan-level framing
- `skills/provenance-discipline/SKILL.md` (v1.2) and
  `skills/ledger-and-session-records/SKILL.md` (v1.4) -- governing
  conventions for the scanner and for how you should format your output

**Reference as needed:**
- `documentation/PREDESIGN_HANDOFF_provenance_scoring_and_gallery_scanner.md`
  -- the originating record (why this started)
- `documentation/ROLE_DOMAIN_CLASSIFICATION_HANDOFF.md` and
  `documentation/AS_BUILT_L163_phase1.md` through
  `documentation/AS_BUILT_L163_phase4.md` -- the just-closed classification
  track and exactly what it shipped
- `documentation/HANDOFF_gallery_feature_layer_L154_resume.md` -- what
  L-154 needs once this cluster closes (its own resolver bug, corrected in
  place; three open design questions for its own future session)
- `PROVENANCE_AUDIT.md` -- the stale Jul 17 snapshot, useful only as "what
  the old vocabulary reported," per the caveat above
- gallery repo: `gallery/assembler/render_orbits.py` (`propagate_marker`,
  ~line 90) and `gallery/assembler/assemble.py` (~line 62) for `L-168`'s
  live call site, if you touch the priority-cleanup ask below

---

## The ask

1. **Verify, don't summarize.** Reason from the fetched source itself,
   including re-running `git ls-remote` for both repos before you start --
   flag anywhere your read differs from mine above or from any of the
   chain documents.
2. **Give Tony a clean current-state map of `L-154` through `L-164`**
   (the cluster plus its two immediate structural neighbors), resolved
   against live HEAD, not against what the design documents claim about
   themselves.
3. **Resolve the `L-162` scope gap explicitly** -- naming convention, and
   which item owns the Sun/Earth/Jupiter literal fix -- with a recommendation,
   not just a restatement of the fork.
4. **Produce a phased, build-ready completion plan for
   `L-155/156/157/158/159/160/161/162`.** Specific enough that a
   subsequent build session could work from it directly, not "build Phases
   1-3" as a one-line label:
   - What lands in each phase (the design docs already sketch this --
     confirm, correct, or sharpen it against current HEAD).
   - Build ownership per item: which are yours to build directly, and
     which are Mode 7 Gemini relay through Tony (`L-157`, `L-161`) --
     restate the blind-worksheet requirement (no Claude-derived figures in
     the draft) for both, since it's already been the fix for one
     near-miss in this project's own history.
   - Where `L-162` and `L-164` best slot in, given both are independent of
     the phase sequence itself.
   - The Tier-1-never-auto-exits rule and the pinning engine's hard
     exit-code gate (`L-155`) stay as decided -- flag only if you think
     either needs revisiting, don't silently relitigate.
5. **Widen the lens.** Look at `L-078` (provenance-scanner systematic
   coverage via `module_atlas` role classification -- the parallel,
   partially-live track: step 1 shipped July 4, step 2's vocabulary
   near-miss detector is designed but untuned) and say plainly whether/how
   it interacts with or should be resequenced around this cluster. Note
   anything else you find reading broadly -- gaps, drift, stale claims,
   genuine opportunities. This is explicitly broad-first work, the way
   Fable 5's Jul 26 review was; a checklist closeout isn't the goal.
6. **Priority cleanup: what's next once `L-155-162` close.** A concrete,
   RICE-informed list (use the table above as your starting point, not
   fresh guesses) of what becomes actionable the moment the cluster lands
   -- at minimum:
   - `L-154` resume: restate its own known resolver bug (`resolver.py`
     line ~133, `tuple(dict)` drops nested feature params) as a first-fix,
     and its three open design questions (geometry-building approach,
     legend behavior, artifact sequencing), per
     `HANDOFF_gallery_feature_layer_L154_resume.md`.
   - `L-168`'s `propagate_marker` fix -- flag it as a pre-flight gate
     before `L-154`'s build reaches a planetocentric moon, not an
     afterthought.
   - `L-164`'s trivial ASCII cleanup -- cheap, no dependency, land it
     whenever convenient.
   - `L-078`'s remaining triage (the ~104-145 Tier-1 findings, the 4+1
     coverage-gap modules, the vocabulary near-miss tuning) -- your call
     on whether this rides alongside `L-161`'s Gemini sweep or stays fully
     separate.
7. **Propose ledger updates**, paste-ready per the block format in
   `skills/ledger-and-session-records/SKILL.md` -- `**Note:**` additions to
   existing `[L-162]`/`[L-156]` blocks resolving the scope gap, not full
   rewrites. I'll run `ledger_index.py` after Tony approves.

## What this isn't

No code, no scanner diffs, no build manifest -- that's the *next* session's
job, once Tony and I have reviewed and adjusted what you hand back here.
Zero code written or proposed, same discipline as Fable 5's Jul 22 design
session and Jul 26 review.

## Format your output as

A **PRELIMINARY DESIGN HANDOFF**, per this project's own conventions
(`skills/ledger-and-session-records/SKILL.md`):
- Opens with **Built on** (both repos, freshly re-verified via
  `git ls-remote`, not copied from this prompt) and **Type: DESIGN SESSION
  (zero code)**.
- **Companion** line back to this prompt and the chain documents above.
- Body per "The ask," in whatever order reads clearest -- you don't need to
  mirror my numbering.
- **Tony-action (do)** / **Tony-action (decide)** tags on anything needing
  his hands-on action or judgment call, inline wherever they occur, swept
  into one consolidated rollup list at the close -- not scattered through
  the body.
- Close with: "Handoff written [Month Year] with Anthropic's Claude Opus 5."

## Where this goes next

Tony carries your handoff back into this thread. From there: I (Sonnet 5)
independently re-verify your claims against live HEAD the same way this
prompt re-verified the documents before it; Tony reviews and makes the
genuine judgment calls (the `L-162` naming decision chief among them);
then a build session -- you, Opus 5 -- executes the finalized Phases 1-3
plan. `L-157` and `L-161` follow via Mode 7 Gemini relay through Tony,
sequentially, not in parallel. `L-162` and `L-164` land independently,
whenever a session is free, per whatever slotting you recommend. You're
the completion-planning step in that chain -- reason freely, and don't feel
bound to any sequencing proposed above if you see a better one.

---

*Prompt drafted July 2026 with Anthropic's Claude Sonnet 5.*
