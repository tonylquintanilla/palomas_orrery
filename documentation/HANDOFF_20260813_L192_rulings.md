# Session Handoff -- August 13, 2026

**Built on `6b99acec3d980c9de7e1770ef752d82a54c01db8`, pushed at
`b22bcf8f39dab375f6b5cf1207826575fdda3415`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery unchanged at `c2202dcc2c4ed210160ce6033b70346aef194b68`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both HEADs verified live at session close.**

**Type: DESIGN SESSION plus RECORD.** Three rulings, one skill version,
one ledger entry, one small runner change. No orrery rendering code
touched. The worksheet checker is still not built.

**Continues from** `documentation/HANDOFF_20260812b_L192_attachment.md`
(anchored `c5218f6` / `6b99ace`).

**Advances:** L-192 -- all three open decisions are ruled and recorded.
**Opens:** one (do) on Pluto's Hill sphere text.

**Prepared:** August 13, 2026 by Claude Opus 5, Tony Quintanilla
integrator.

---

## The obligation from the previous handoff is DISCHARGED

`provenance-discipline` loaded at 2.1 and the manifest row at HEAD read
2.1. No mismatch, nothing deferred from that one.

**A NEW obligation replaces it, same shape.** The skill went to 2.2
during this session. The session that bumped it had 2.1 loaded, and a
mid-session reinstall cannot be verified from inside the session --
the loaded copy appears bound at conversation start. **Confirm your
loaded copy reads 2.2 before doing any provenance work.** Your load
performs the check; this note cannot.

This matters more than usual for the next session, because 2.2 carries
the rules the L-192 checker implements. Building it from a 2.1 copy
means holding those rules in conversation instead of in the skill.

---

## What happened

| SHA | What |
|---|---|
| `2a7ead8` | `provenance-discipline` 2.1 -> 2.2; manifest regenerated |
| `173902b` | L-192 ledger entry, then its sequencing correction |
| `b22bcf8` | `maintenance_run.py` reports a write separately from a content change |

Session-start reconciliation: HEAD was `6b99ace`, exactly where the
previous handoff left it. Nothing to reconcile.

---

## The three rulings

All three of L-192's "Still open for Tony (decide)" items are closed.
Full capture is in the L-192 ledger block under **Forks ruled,
2026-08-13**; the prose below carries what a reader needs without the
ledger open.

**Fork 2 -- PARTIAL and APPROX return to the originator.**
Unconditionally, without first asking why the row is qualified. Neither
earns a leg toward the cross-checked rung. This is the August 13 rule --
we do not have to accept and interpret incomplete or malformed answers --
applied to the verdict vocabulary rather than only to unreadable
worksheets. Fable's middle answer, per-row exceptions recorded in
`provenance_exceptions.json`, was declined: it stores a judgement where
the simpler move is to get a better worksheet.

**DERIVED is not a third member of that family, and it had never been
defined.** It answers the CITATION question, not the value question --
no source publishes the number because the number is computed. It can
pair with any value verdict, including NO. A DERIVED row is COMPLETE
when it names its inputs, shows the arithmetic, and the arithmetic
closes; then L-158 governs and the value inherits the rung of its
weakest input, which hands the question to the premise rather than
settling it. A DERIVED row showing no work is incomplete and goes back.

**Fork 3 -- the checker does not write.** No `--propose` argument.
Proposed annotations are discussed in conversation before anything is
written. Fable had recommended a propose mode emitting a patch script
for review; the mode itself is declined, not merely its safeguards.

**Bennu and Arrokoth stay until the checker's first run.** The
disposition is return-to-originator, but the SEQUENCING is the ruling:
the first run should catch both as examples of an incomplete response,
and the catch is what routes them. Fixing them beforehand would remove
the only two known-true failures in the corpus, and a first run that
cannot fail is not a passing run.

---

## The correction that changed the design

**A complete row that disagrees is a FINDING, not a defective
worksheet.** Send-back fires on INCOMPLETENESS. It does not fire on
DISAGREEMENT. A row that names its inputs and shows its arithmetic has
already given everything needed to settle the question, so returning it
asks for what we already hold.

So a mismatch is reported loudly and routed to conversation, with no
cause assigned by any tool. Three outcomes, none of them the default:
CONVENTION MISMATCH, THE CODE'S NUMBER IS WRONG, THE WORKSHEET'S
DERIVATION IS WRONG. Every one is confirmed in conversation **unless the
rule is already stated** -- which is what makes writing an adjudication
down worth the effort.

**The Hill sphere is the worked example, and this session had it wrong
first.** The initial pass filed Eris and Pluto as live value errors
because checkers computing at semimajor axis disagreed with the code.
Tony's correction: the standard Hill radius carries an eccentricity
factor, a(1-e)(m/3M)^(1/3), so what it returns is the PERIHELION Hill
radius. The checkers had dropped the (1-e). For Eris at e~0.44 that is
14.2 Mkm against 8.0 Mkm -- a gap that reads as a gross error and is
not one. Nobody did bad arithmetic.

Two dispositions follow, and the checker names which one applies. An L2
MISMATCH routes to CONVERSATION, because the cause is open. An L3
failure -- an annotation asserting a completed check over a row
recording an incomplete one -- routes to SEND BACK, because the cause is
already known.

---

## What was built

**`provenance-discipline` 2.1 -> 2.2.** Five edits: the DERIVED
definition and its completeness test in the verdict vocabulary; the
send-back clause split so PARTIAL and APPROX return unconditionally; a
new CRITICAL subsection, *A Complete Row That Disagrees Is a Finding*,
carrying the three outcomes and the two recording shapes; and the phrase
"ran out of session" replaced, since it read as though Tony's account
were the thing running out. It meant the checker's own conversation
stopping partway.

**`maintenance_run.py`** now reports a write separately from a content
change. `fingerprint()` became `snapshot()` and returns two facts, the
modification time and the content hash. Three states:

    Ledger index      0.2s  unchanged (1 of 1 rewritten, content identical)
    Module atlas      3.6s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
    <no-write case>   0.0s  unchanged (1 checked, not written)

Origin: `skills_index.py` rewrites its manifest zone every run whether
or not the bytes move, so `PROJECT_INSTRUCTIONS.md` gets a new timestamp
and looks changed in Windows Explorer while the runner correctly says
"unchanged." Both were right and the screen said nothing about the
difference. It is operational, not cosmetic -- a real change to
`PROJECT_INSTRUCTIONS.md` has to be re-uploaded to the Claude UI and a
byte-identical rewrite does not.

The third branch was exercised before delivery on a disposable copy with
a no-op generator spliced in, because it would not otherwise have run
once, and a branch that has never executed is a branch that cannot fail.

---

## (do) -- outstanding

Items 1-4 carry forward from the previous handoff unchanged. Item 5 is
closed (the patch script was archived). Item 6 is unchanged and is
folded into the checker build below. Item 7 is new.

1. **Open the ledger handle for the claim class** -- claims about the
   project that no tooling checks. Fable's earlier audit found fourteen
   in fifteen documents, eleven mechanically checkable. Still not open.

2. **Record the scheduled-build retirement in the ledger.** The
   deployment-model decision block still describes the scheduled nightly
   as the operating model. Note the pre-commit fail-safe as designed but
   not built.

3. **Note on the L-191 block:** manual-scale instructions are
   orrery-surface-only and must not be collapsed into shared text that
   reaches the transport. 32 live in `shell_configs.py`.

4. **Record the eighteen inline literals** duplicating cited constants:
   `KM_PER_AU` 14 sites in 8 files, `MOON_RADIUS_KM` 3 in 2,
   `SUN_RADIUS_KM` 2 in 1. Inline in f-strings, so the scanner sees one
   of nineteen.

6. **The runner's checker-delta gap** (filed in L-188). Unchanged, and
   NOT what this session's runner change addressed. See below.

7. **Pluto's reader-facing Hill sphere text states no basis.** Its
   `# Source:` comments name perihelion 29.66 AU and the Pluto-Charon
   system GM, and `radius_fraction` 5041 is consistent with them, but
   the hover text and tooltip say only "approximately 5.99 million
   kilometers." Eris already carries the fix -- its shell text names
   both figures and says the shell draws perihelion. Apply the same to
   `pluto_visualization_shells.py` and `shell_configs.py`.

---

## (decide) -- still open

L-192's three are closed. The rest are unchanged from the previous
handoff.

1. **Jupiter's ring entry count: 4 or 5.** The pilot is scoped by it.
2. **Migration shape and per-body sequence beyond Jupiter** (L-181).
3. **Saturn `thickness_km`:** absent from the served cache, but is it
   absent from the ORRERY?
4. **Do the three `provenance_history.py` constants earn
   `provenance_exceptions.json` entries?** Tier 3, low stakes.
5. **`LESSONS_ARCHIVE.md` line-count discrepancy** (824 vs 882).
6. **Are `DEFAULT_MARKER_SIZE` and `CENTER_MARKER_SIZE` in cross-check
   scope at all?** Visual choices, not measurements.

---

## Next session

**L-192's build: the worksheet checker.** It now has a complete rule set
to implement -- the attachment rule from `878e2c9`, and this session's
verdict semantics. Fork 1 (header-role mapping plus a key column going
forward), fork 4 (joins `maintenance_run.py`, one line with a
denominator, report-only) and fork 5 (uncited worksheets, one line
steady-state) were already settled in the previous session's review.

**(do) item 6 is folded into this build, deliberately.** The checker's
fork-4 ruling is an output-shape decision about `maintenance_run.py`,
and item 6 is the same question about the same runner: the provenance
scanner never fails, so its full output -- including the L-189 run-to-run
delta that is already built and already printed -- is discarded on every
passing run. That is why the day the cross-checked rung fell from 77 to
50, with four orphan annotations found, none of it reached the screen.
Two candidate fixes were sketched and neither chosen: a second verdict
hint reusing the existing CHECKERS-table mechanism, or printing a
checker's whole output whenever its summary line moves since the last
run. They cover different ground. Settle it once, with the checker in
hand.

**Then the backfill of the 27**, verdict-gated, starting with the four
orphan annotations in `constants_new.py`.

Carried from the previous session and still true: 134 live annotations,
all parsing under the L-186 grammar, 18 distinct worksheets named, zero
dangling. The existence half is clean; the value half is the build.

---

## Process -- read this before your first substantive reply

The Register Rule held, and one thing about it is worth carrying.

Tony asked what "NOOP" meant and what "ran out of session" meant. Both
were jargon that had gone unglossed -- one in a test output, one sitting
in the skill's own body since v2.1. The rule's second half is plain
language, and it is the half that slips while the one-ask half is being
satisfied.

**The method note worth carrying is smaller than last session's and the
same in kind.** This session's first reading of the Hill sphere rows was
confident and wrong: it classified a convention difference as a live
value error, in both Eris and Pluto, and would have written that into
the ledger. What caught it was Tony reading the finding and knowing the
formula. The tell was available in the artifact -- Eris's own shell text
already named both bases and said which one it drew -- and the session
had read that file without noticing the file was answering the question.

---

*Handoff prepared August 2026 with Anthropic's Claude Opus 5. Built on
`6b99acec3d980c9de7e1770ef752d82a54c01db8` and pushed at
`b22bcf8f39dab375f6b5cf1207826575fdda3415` at
https://github.com/tonylquintanilla/palomas_orrery. Gallery at
`c2202dcc2c4ed210160ce6033b70346aef194b68` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io --
untouched by this session.*
