# Session Handoff -- August 11, 2026 (second session)

**Built on `dea0bc0b17c800f9399069152fee569bef260bcb`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery pinned separately at `d5437f08f94feccd70b697729b52cdc44df8b51d`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
(unchanged this session).
Both HEADs verified live at session close.**

**Type: BUILD.** One new module, one transactional patch to a shared
tool, one record-layer patch. No orrery rendering code touched.

**Prepared:** August 11, 2026 by Claude Opus 5, Tony Quintanilla
integrator.

**Continues from** `documentation/HANDOFF_20260811_record_layer.md`
(anchored `ba2d6f0`).

**Closes:** L-189. Also closes that handoff's cleanup items 7 and 8,
which Tony had already done in `df7ca50` before this session opened.
**Opens:** nothing new in the ledger. One cleanup item below.

---

## Who you are working for

Tony Quintanilla, PE -- a retired civil and environmental engineer,
artist, and anthropologist. Not a professional programmer, not a formally
trained astronomer. He builds Paloma's Orrery through conversational AI
collaboration and holds sole commit authority and final judgment. The
codebase's structure and discipline are products of that collaboration;
do not read code quality as evidence of his personal programming fluency.

He runs Python by opening a file in VS Code and clicking Run, and works
through GitHub Desktop. Deliver runnable transactional patch scripts with
the run command in the docstring.

**Read the Process section at the bottom before your first substantive
reply.** The Register Rule is binding at protocol v3.37, and this session
tested it in both directions.

---

## Session-start reconciliation

Repo HEAD was `df7ca50`, one commit past the previous handoff's anchor.
That commit was Tony's own cleanup: it deleted the three `PREVIEW_` files
and the superseded `patch_protocol_v337.py`, and committed the handoff.
Items 7 and 8 of that handoff's do-list were therefore already closed
before this session began.

Item 9 changed shape rather than closing. The protocol no longer claims
the lessons archive lives in the ledger -- that sentence is gone at
v3.37. But the Version History section still states that the full
history from v1.0 through current lives in the ledger's Protocol Version
History appendix, and that appendix stops at v3.34. Versions v3.35,
v3.36 and v3.37 are not in it. Same false-claim class, different
sentence, and it is a correction rather than a decision.

---

## What happened

Two pushes.

| SHA | What |
|---|---|
| `df7ca50` | (Tony, pre-session) cleanup: PREVIEW files and the superseded protocol patch removed |
| `dea0bc0` | L-189: `provenance_history.py`, scanner patch, first history record, Fable review request filed |

---

## L-189: what shipped

A new module `provenance_history.py` (444 lines) plus eight anchored
edits to `provenance_scanner.py`.

**The shape is Tony's August 7 ruling unchanged.** One
`data/provenance_history.json`, a ring buffer of the last six runs,
tracked in git, because when an audit was taken and against which commit
is itself provenance.

**One reconciliation was made rather than asked.** The August 10 design
input said to follow the gallery cache builder's per-run record shape.
The builder writes one file per run into `data/solar-system/raw/runs/`
and has accumulated 23 of them since July. That LAYOUT was not adopted:
the builder runs nightly, the scanner runs several times in a working
session, and per-run files would churn the changed-files list in GitHub
Desktop constantly. The builder's FIELD VOCABULARY was adopted --
`run_id` as a compact UTC stamp, `started`, `finished`, `mode` -- so the
two histories read alike. Tony confirmed after the distinction was
explained plainly.

**Cadence: 1 day, compared by calendar date** (Tony, this session).
Once per day, not at a fixed time, because the run is manual. The
declared number is the point: a file that only accumulates runs cannot
report a run that never happened.

**Behavior.** The console prints the delta after the priority summary and
before the Tier-1 banner, and names any file whose Tier-1 count rose.
Files whose Tier-1 fell are not named -- a drop is the outcome the work
aims at, and naming it competes with the thing that needs a decision.
`PROVENANCE_AUDIT.md` carries a Run History table ahead of the risk
matrix. Nothing touches the exit code.

**First-run cost, predicted and attributable: 879 to 882 findings.** The
three are the new module's own `SCHEMA_VERSION`, `MAX_RUNS` and
`EXPECTED_CADENCE_DAYS` -- all Tier 3, all `dev_tools`, Tier-1 unchanged
at 206. The console explains this on the first run rather than letting
the jump read as a regression.

**`is_overdue()` and `overdue_lines()` ship UNCALLED, by design.** A
scanner that is running cannot report that it did not run, so the
staleness check cannot live inside the thing it watches. L-188 is the
trigger, L-189 is the data. The module docstring says so explicitly, so
a later session does not remove them as dead code.

**Verification.** Sandbox clone at `df7ca50`: patch applied, scanner run
three times, ring-buffer trim at six, corrupt-file tolerance, HEAD SHA
read without invoking git, and the Tier-1-rose path exercised against
real per-file counts. Confirmed on Tony's machine at `dea0bc0`: 882
findings, 206 Tier-1, `dev_tools` 39 -- matching the sandbox exactly.

---

## The measurement worth keeping

Taken while settling the cadence, and recorded in L-189 rather than as
its own ledger item on Tony's call.

**Every trust window in the gallery served cache is set by its category
cap, never by measured propagation error.** Across all eleven objects
carrying a trust block, the error test has never been the binding
constraint.

Apophis alone binds the global served window. Its trust window is
647.0868619950488 days wide; the served window is 647.0868619950488 days
wide, identical to the last digit, recentered on build time. It binds by
policy -- one orbital period, the asteroid category rule -- not by
physics. Its measured two-body error is 3.1e-6 degrees per day, which on
the error test alone would run about 80,000 days.

The per-object windows that look alarming are Io at +/-5.3 hours, Charon
at +/-19 hours, Titan at +/-2.0 days, Moon at +/-3.4 days, and Pluto at
+/-6.4 days. All five are excluded from the global gate by frame per
L-149, and the resolver checks one bound for an entire scene, so nothing
enforces them.

**The practical cost is sub-pixel.** On a plot where the orbit spans 400
pixels, the worst case (the Moon) is about 0.15 px after a day and 1.1 px
after a week -- and the second figure is the builder's own linear
error-rate model extrapolated past where it was measured, not a
measurement. The orbit SHAPE does not degrade at all, being geometric.
This is a gate that does not fire, not a picture that is wrong. Recorded
so the next session to find Io's five-hour window does not re-raise it as
alarming.

---

## (do) -- outstanding

Items 1-6 carry forward from the August 10 handoff unchanged. Item 7 is
new this session. Items 7 and 8 of the previous handoff are closed;
item 9 is restated below at its corrected target.

### Provenance -- needs Tony's judgment, not a patch

1. **Resolve six `duplicate_identity` sites** against the sources:
   `constants_new.py` 423, eris 218, mercury 49, pluto 41,
   `shell_configs.py` 128, venus 528. Each needs a look at the source to
   decide whether one annotation is redundant or a checker name is wrong.
   This is reading, and it is the natural first item of a working session.

### Ledger

2. **Open a handle for the second L-190 class:** claims about the codebase
   that no tooling checks. Evidence stands at nine instances. The newest,
   found this session and still live at `dea0bc0`: the protocol says the
   full version history v1.0-through-current lives in the ledger's
   Protocol Version History appendix, and that appendix stops at v3.34.
   This replaces the previous handoff's item 9, which described the same
   defect at a sentence that has since been rewritten.

3. **Record the scheduled-build retirement in the ledger.** The skill is
   done (1.3) and the plan is done; the ledger's deployment-model decision
   block near line 4555 still describes the scheduled nightly as the
   operating model. Note the pre-commit fail-safe as designed-but-not-
   built, relevant only if the schedule returns, a second person gains
   commit access, or the build ever runs unattended.

4. **Note on the L-191 block:** manual-scale instructions are
   orrery-surface-only and must not be collapsed into shared text that
   reaches the transport. 32 live in `shell_configs.py` as copies of
   shell-module text.

5. **Record the eighteen inline literals** duplicating cited constants:
   `KM_PER_AU` 14 sites in 8 files, `MOON_RADIUS_KM` 3 in 2,
   `SUN_RADIUS_KM` 2 in 1. Same violation as the shadow constant but
   inline in f-strings rather than named assignments, so the scanner sees
   one of nineteen. Scope-and-sequence work, distinct from L-181's
   migration, and evidence for item 2.

6. **Ledger tooltip count: 124, not 126.** Two of the 126 grep matches are
   documentation -- the module docstring at line 12 and a comment at line
   2062. Real key definitions: 83 in SHELL_CONFIGS + 41 in CUSTOM_SHELLS.
   Two ledger sites carry 126, one of which contradicts its own
   "83 sphere + 41 custom" breakdown in the same bullet. Also check the
   historical entry near line 5357.

### Cleanup this session created

7. **Move `patch_L189_run_history.py` out of the repo root into
   `documentation/`**, alongside `patch_dashboard_manual_builder.py`. It
   was committed to the root at `dea0bc0`. It is spent -- its base
   fingerprint no longer matches, so it cannot run again -- and while it
   sits in the root the scanner counts 119 files instead of 118 and
   `module_atlas.py` reports one undetermined module. The same applies to
   `patch_ledger_L189_close.py` once it has been run.

---

## (decide) -- still open

Unchanged from the previous handoff except where noted.

1. **The constructor-call count in master plan decision 12.** It said two
   assignments contain constructor calls. Measured: one,
   `HORIZONS_MAX_DATE = datetime(...)`. Staleness explains a count going
   UP, not down, so this needs a look rather than a correction.

2. **Jupiter's ring entry count: 4 or 5.** The August 7 summary said five;
   the August 10 session counted four; the plan's v17 correction note says
   "Jupiter is 4, not 5" while decision 16's Fable recommendation still
   says 5. The pilot is scoped by it, and it should be settled by reading
   the file's structure rather than argued.

3. **Where the L-188 run-all push-gate binding lands** -- L-188 or L-184.

4. **Migration shape and per-body sequence beyond Jupiter** (L-181). Order
   is settled; the detail wants Jupiter's ring entries in view.

5. **Saturn `thickness_km`:** absent from the served cache, but is it
   absent from the ORRERY? One look at the file settles it.

6. **New:** do the three new `provenance_history.py` constants earn
   `provenance_exceptions.json` entries? They are configuration, not
   factual claims, which is the textbook shape of an accepted residual.
   Low stakes either way; they sit at Tier 3.

---

## Next session

**Fable's document-layer claim audit is in flight.** The review request
is at `documentation/FABLE_REVIEW_document_layer_claims.md`, anchored at
`df7ca50`, scoped to fifteen live documents and explicitly excluding
handoffs (a handoff's claims are historical; its anchor does not move).
Reading those findings is the natural opener -- it is reading with
material in front of Tony, which is the layout that produces findings.

Then do-item 1, the six `duplicate_identity` sites. Then the migration
shape conversation, then Track 0 proper.

L-188 is the natural follow-on to this session's work: it is the caller
that makes L-189's staleness check live, and its own open decision
(**dashboard entry that replaces the eight, or a script run before every
push**) is unchanged.

---

## Process -- read this before your first substantive reply

The Register Rule is binding at v3.37. Its message-level check is the one
that matters:

**Check 0: does this message ask Tony for ONE thing?** A finding, a
recommendation, an uncertainty, and a new question are four things. Send
the one that is due; the rest wait or go in a file.

Two supporting defaults, both binding: **answer first, evidence on
request**, and **capture goes in a file, not in the conversation**.

Do not rely on Tony saying "opaque." The check runs on your side before
sending. "Just the decision" is his second lever.

**This session tested the rule in both directions, and both are worth
carrying.**

Tony said "can you simplify the question and focus on the decision
needed" after a message that carried a clarification, a cadence answer,
a measurement, a table, and a recommendation. Every paragraph did one
job; the message did five. That is Check 0 failing exactly as the rule
describes, and the repair was a two-sentence question.

Then he asked "what is the practical impact?" about a finding that had
been presented as important. Measuring it honestly showed sub-pixel
displacement -- the finding was real but its weight had been overstated.
**Say which kind a finding is: "I found this" or "this should change
what you do next."** Getting that wrong in the alarming direction costs
Tony a decision he did not need to make. The correction cost one
message; not making it would have cost a ledger item and a session.

The pattern underneath both: you do not have deep understanding of this
codebase, you have what you grepped this session. Raising something
usually means you just found it, not that you weighed it. Measure before
you weight it, and say which you did.

---

*Handoff prepared August 2026 with Anthropic's Claude Opus 5, built on
`dea0bc0b17c800f9399069152fee569bef260bcb` at
https://github.com/tonylquintanilla/palomas_orrery and
`d5437f08f94feccd70b697729b52cdc44df8b51d` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io*
