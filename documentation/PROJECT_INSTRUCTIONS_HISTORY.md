PROJECT INSTRUCTIONS -- HISTORY

Cut from b65ac115fc0f820e8270c0807249813c67bde7bc at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Assembled 2026-08-18 under L-199, from two records that were previously
in two different files.

THIS FILE IS A RECORD, NOT A STORE OF RULES. Nothing in it fires. No
session needs to read it to work correctly; it exists so that a
question about how the protocol got here can be answered by reading
rather than from memory.

  PART 1  The protocol's version history, v1.0 through v3.38. Moved
          here from the Appendix at the end of LEDGER_CONSOLIDATED.md,
          which now holds a pointer. The protocol document keeps the
          THREE most recent entries resident and a fourth pushes the
          oldest down into PART 1, so every entry lives in exactly one
          place and there is nothing here to keep in step.

  PART 2  The twenty-seven lessons removed from the protocol at v3.37,
          kept verbatim, each naming where the same instruction is
          still stated. This file used to be called LESSONS_ARCHIVE.md
          and was exactly this record; the rename adds the history
          beside it and takes nothing away.

Why they sit together. Both answer the same kind of question -- what
the protocol used to say and why it stopped saying it -- and neither
has a trigger, which is precisely why neither belongs in the resident
document. Keeping them in one file makes that shared property visible
instead of leaving two triggerless records in two places.

================================================================
PART 1 -- PROTOCOL VERSION HISTORY (v1.0 through v3.38)
================================================================

The protocol's change log lives here as of v3.30; the protocol document
keeps only the most recent entries. Skill-layer changes are logged here
too (or as L-items when they warrant one): skill name, new version, and
the SHA it was cut from.

v1.0-v3.12 (Oct 2025 - Feb 2026): Foundation through Gallery Studio workflow redesign.
  Covers: modes, alignment, discovery pathway, Einstein proof, platform integration,
  Windows encoding, Horizons center patterns, agentic/targeted guidance, xvfb pre-test,
  bottom-up editing, Unicode-safe editing, Mode 7, LF line endings, JPL binary IDs,
  parallel pipeline lesson, iterative design planning, irreducibility argument,
  Gallery Studio session, _studio flag, pan arrows, Hassabis corroboration,
  featured trace labels, gallery badges, studio workflow redesign.

v3.13 (Mar 5, 2026): Studio source vs export distinction. 3D axis dtick+range convention. Hover text AU convention.

v3.14 (Mar 9, 2026): The Epistemic Dialogue. Polycrisis framework. Gemini elevated to dialogue partner.

v3.15 (Mar 14, 2026): Adaptive encounter resolution design. Two-length-scale insight. Double-Helix as safety mechanism.

v3.16 (Mar 25, 2026): Verify base against handoff before building on multi-session files.

v3.17 (Apr 3, 2026): Competitive Mode 7. Activation vs provision. Interpretation gap as signal. Fog of war is the experiment.

v3.18 (Apr 10, 2026): Single info marker pattern. Credit line convention. Ghost tail legendgroup. MAPS elegy.

v3.19 (Apr 13, 2026): Marker symbol convention. Two-tier label system. Renderer refactor. Celestial sphere complete.

v3.20 (Apr 14, 2026): Module Docstring Standard. Module Atlas tooling (99 modules, 785 functions, 86K lines).

v3.21 (May 4, 2026): Project file staleness rule formalized. Object Encyclopedia. Encounter Export design.

v3.22 (May 12, 2026): Collegial Mode 7 pattern. The Weasley Principle. Single info marker codebase-wide refactor: 141 conversions, 18 files, 3 Claude models, 9-13 MB savings per render.

v3.23 (May 16, 2026): Procedural criticality framework -- three-tier taxonomy (CRITICAL / QUALITY / PRACTICE), a Part-2 principle with markers across Part 3. Broad-first methodology validated; procedure-to-judgment ratio scales with experience and shared context. Grounded in Tony's ops-management experience (LOTO, normalization of deviance).

v3.24 (May 29, 2026): Verify Execution, Not Appearance [CRITICAL] -- map the dispatch before editing leaves; compile != used != edited; swallowed exceptions hide render bugs. Agentic Pre-Test refined: data-content sweeps need a runtime smoke against the LIVE dispatch. Platform Neutrality [QUALITY]. Plotly facts (Scatter3d ignores border width, 8-symbol palette); transactional binary-mode patching. From the shell-consolidation dispatch discovery -- an inline-marker sweep editing dead code, an osculating marker silently absent 11 weeks; Tony's eyes caught both.

v3.24 re-issue (May 29, 2026): Enumerate Uploads Before Claiming a Review [CRITICAL] -- ls the uploads dir, read the whole set; the in-context subset is invisible to Tony and not authoritative. Recovered lessons the first pass missed (itself built on 9 of 19 handoffs -- the exact failure it names): floating-items-capture, verify-propagation-with-grep, central-factory-migration-intent, testing-in-dependency-order, smoke-test-deferred-pipelines, handoff-numbering-rebase drift.

v3.25 (May 31, 2026): Provenance Audit named as a Part-3 skill (scanner, Tier-1=0 goal, lookback-window mechanics, exceptions-file over-report gotcha). Fetched-vs-Recalled extended: three outcomes (cite / remove-and-note-the-gap / never cite-to-clear); a citation is a provenance claim that must be TRUE [CRITICAL]. From provenance Phase 1, after nearly papering a # Source over recalled data.

v3.26 (June 2, 2026): Session-Start Repo Pull [CRITICAL] -- the GitHub repo at HEAD is ground truth; pull and SHA-pin, build on repo or fresh upload, /mnt/project + project knowledge demoted to orientation. From the stale-Earth thread: a duplicate upload shadowed the current file and a true ghost was served through a project-knowledge replacement; repo-pull validated byte-for-byte.

v3.27 (June 4, 2026): Project knowledge now auto-syncs from the repo (no manual add/delete), retiring v3.26's stale-snapshot + served-ghost class at source. Session-Start reframed around "The SHA is the round trip" -- a matching remote HEAD confirms commit + push + sync in one unforgeable check. Foundation gains "access is not understanding." Quotable: "Our work is not just right -- it's beautiful."

v3.28 (June 6, 2026): Two additions (Movement-2 dipole-cone session, handoff v27). (1) Live repo vs snapshots -- the repo is live-readable any time (re-pull after a push; reading HEAD is the round-trip check, run live: de12f56 -> c25bdd7); project knowledge does NOT re-sync mid-session; un-pushed edits live only in uploads, which stay tier 1. (2) Show the Envelope of the Unknowable -- companion to Fetched-vs-Recalled: where a value is genuinely unknowable (rotation phase / instantaneous azimuth), show the envelope, not a faked point, and say so in the hover where the shape is approximate; faking an unknowable value is the cite-over-recalled failure class [CRITICAL].

v3.29 (June 22, 2026): Three amendments from the animation-refactor sessions (L-003). (1) Agentic Pre-Test [CRITICAL] corrected -- the SystemButtonFace<->gray90 sed round trip is NOT idempotent (palomas_orrery.py has 26 native gray90 literals), so swap on a THROWAWAY copy and discard it; never restore-in-place on the deliverable. (2) Live-dispatch smoke test folded into the data-sweep gate -- exec the whole module under xvfb with the tk mainloop suppressed, to exercise the real path rather than a lookalike. (3) grep -c in && chains [QUALITY] -- grep -c exits non-zero on a zero count, silently breaking the chain; run verification greps standalone or join with ;. Cleanup: merged the duplicate data-sweep paragraphs, trimmed the redundant Uploads-Before-Project-Files block to a pointer, corrected the stale xvfb archive line, dropped the [NEW v3.23] tag.

v3.30 (July 1, 2026): The skills refactor (L-002). The protocol becomes the
constitution of a two-layer system: Part 3's task-triggered conventions and
procedures extracted into eight repo-authored skills (skills/<name>/SKILL.md,
each versioned and SHA-stamped; installed to the account as a deployment
step), with the resident document keeping the checkpoint CRITICAL gates, the
modes, the principles, the Foundation, and the quotables. Skill set at 1.0:
orrery-coding-conventions, safe-file-editing (portable), agentic-pre-test,
horizons-orbital-mechanics, provenance-discipline, earth-system-pipeline,
gallery-pipeline, ledger-and-session-records -- all cut from palomas_orrery
@ b29ad3f8 (gallery-pipeline also from tonyquintanilla.github.io @ 89c8bf30).
Part-3 technical lessons distributed into skills as field notes; the full
v3.29 Technical lessons list is preserved verbatim below for institutional
memory. Skill Manifest table added to Part 3 as the under-trigger backstop
and version drift check; a Triggers row added ("Relevant skill unfired ->
load it"). Skills 6-8 are first-time capture: Earth System pipeline +
human-cost restraint discipline, gallery pipeline + WYSIWYG authority,
ledger/handoff/manifest conventions -- knowledge that previously lived only
in handoffs and code. Version history moved here; the ledger is now the
change log for protocol and skills. Extraction audit trail:
documentation/MAPPING_TABLE_L002.md. Designed with Claude Opus 4.6; built
with Claude Fable 5 via collegial relay; Tony integrated.

v3.31 (July 4, 2026): Project-knowledge GitHub sync removed; Context Priority
simplified to 7 tiers (the repo, the protocol+skills, and uploads are the
three stores). skills_index.py devtool (L-097) auto-generates the Skill
Manifest table between markers, same pattern as ledger_index.py; fires_when
frontmatter field added to all 8 skills for editorial control of the manifest.
Protocol header still reads v3.30; filename bumped to v3_31. Reviewed and
built with Claude Opus 4.6.

v3.32 (July 19-20, 2026): Two additions. (1) The anchor requirement
generalized from handoffs to any document leaving a session -- audit
prompts, review requests, relay manifests, as-builts -- each opens with
"built on <SHA> at <URL>"; an un-anchored document is unverifiable by a
receiving AI with no repo access of its own (Part 1 Key Principles, Part 3
SHA Round Trip; line 326 corrected to match). (2) The Orrery and the
Assembler added to Foundation, plus a matching quotable: the assembler
inherits knowledge from the orrery, not machinery -- it exists to solve a
problem the orrery never has -- surfaced via M2 Layer 2 live-Horizons
testing (L-149, L-150, L-151). Corrected mid-push: ledger-and-session-
records was already at 1.2 (July 19) when this version was drafted; the
Skill Manifest table was still showing 1.0, and this entry's own first
draft nearly re-generalized already-generalized content before the
mismatch was caught (L-152, retroactive entry). Skill Manifest bumped to
1.2/1.1/1.1 (ledger-and-session-records / provenance-discipline /
gallery-cache-builder) to match actual repo state, and a new row added
for gallery-assembler (L-151).

v3.33 (July 30, 2026): The Register Rule added to Part 2. The protocol's compressed reference voice is distinguished from explanation voice -- lead with the claim, one idea per sentence, no aphorisms in an explanation, gloss project terms on first use each session. Two yes-or-no checks before sending (does this paragraph do one job; does any sentence point at a label instead of saying the thing), with the test being "can Tony act on this without a follow-up question." Backstop: Tony says "opaque" at the point it fails, Claude rewrites that passage, and the miss is captured as a field note so it accumulates rather than repeating. Manifest table refreshed to 1.2/1.1/1.6.

v3.34 (August 5, 2026): Two amendments, both from the Fable skills-layer review. (1) WHO TONY IS: the GitHub Desktop / Run-button preference is stated as a preference where practical, not a prohibition. The earlier "never the git command line" wording read as a ban and put the section in conflict with safe-file-editing's git apply delivery format (Fable Job 2 #16); Tony's ruling keeps the GUI as default and treats a terminal step as a fallback. The surviving obligation is unchanged: don't hand over an operation outside Tony's known working set without explaining what it does and what could go wrong. (2) Stale Skill = Stop [CRITICAL] added under the Skill Manifest. A skill lives in three stores -- repo skills/, the account install Claude actually loads, and the generated manifest table. When a loaded skill's version disagrees with its manifest row, the session STOPS rather than proceeding and mentioning it later, and asks Tony to push to skills/ and reinstall in Settings. The prior wording asked only to "reconcile before trusting it," and the manifest still advertised 1.1/1.4 against an actual 1.2/1.6 for about three weeks with nothing surfacing it. Supporting change outside the protocol: skills_index.py now prints what the manifest was advertising before overwriting it, so running the tool reports drift instead of silently absorbing it; the prevention side is the binding rule in ledger-and-session-records v1.5.

v3.35 (August 7, 2026): Updated skill safe-file-editing (v1.3).

v3.36 (August 8, 2026): Register Rule amended (Part 2). A
message-level Check 0 added ahead of the two paragraph-level checks --
does this message ask Tony for one thing. The prior checks were
paragraph-scoped and could all pass while a message carried four
separate jobs, which is the load that actually fails. Two supporting
defaults added: answer first with evidence only on request, and
capture goes in a file rather than in the conversation. Backstop
corrected -- "opaque" is a repair, not the mechanism, because Tony has
stated he cannot sustain flagging density in real time; the check runs
on Claude's side before sending. "Just the decision" added as a second
Tony-side lever. Origin: a full mobile session in which the rule did
not fire once.

v3.37 (August 11, 2026): Two changes. (1) "The Artifact Bounds the
Audit" added to Part 3 -- Tony's August 8 ruling, drafted for the first
time. (2) Protocol trimmed from 882 lines to 849: version history
v3.29-v3.33 dropped (the ledger carries it) and twenty-seven Part 5
lessons removed as restatements of rules already stated where they
fire. A first cut moved ALL forty-one lessons to an archive file and
was reversed the same day -- an archive has no trigger, so the fourteen
with no counterpart elsewhere would have left. A lesson duplicated by a
firing rule is redundant; a lesson that is nowhere else IS the archive.

v3.37.1 (August 11, 2026): provenance-discipline skill v1.8 -> v1.9.

v3.38 (August 11, 2026): Two changes, both from Fable's document-layer
claim audit. (1) Two dead pointers to documentation/PROJECT_ORIGIN.md
corrected -- the file is at the repo root (finding F11). (2) Stale
Skill = Stop gains its two known limits. The gate is LOAD-TRIGGERED, so
a manifest that changes later in the same session creates a mismatch
with nothing to fire on -- which is exactly what happened when
provenance-discipline went 1.8 to 1.9 mid-session and the mismatch
surfaced only because a later check re-read the file for an unrelated
reason. And a mid-session reinstall CANNOT be verified from inside the
session: the loaded copy appears bound at conversation start, so the
reinstall lands in the account and stays invisible until the next
session. Tony's ruling: do not add an assertion-based clear. "Tony
reinstalled it" is a claim, not a check, and accepting it in place of a
read is cite-to-clear moved into the skill layer. The verification is
deferred into the handoff and discharged by the next session's load.
Skill-layer companion: provenance-discipline v1.9 narrows the push gate
to the ACTIVE BUILD PATH (L-184, ratified 2026-08-05), keeping global
Tier-1 = 0 as the destination rather than the firing rule (finding F1).

v3.39 (August 12, 2026): One change. "A Check That Cannot Fail Is Not
Passing" added to Part 3 as a CRITICAL gate, immediately after Verify
Execution, Not Appearance, which it extends: that gate asks whether the
edited code is the code that runs, this one asks whether the check being
trusted can produce a failure at all. Origin was three instances in a
single session, each in a different layer and each indistinguishable
from a pass -- the provenance-discipline skill teaching an annotation
format its own parser could not read, test_constants_provenance.py
pinning 55 values in a file no routine executed, and
constants_change_report.py reporting clean both for an edit shape it
could not parse and for a path git does not track. The gate's three
moves are: make success carry evidence, make the blind spot announce,
and put the check where it actually runs. Tony's confirming question --
what tells us it is working -- is the one that found the third instance.
(Moved down from the resident protocol on 2026-08-23 when v3.42 made a
fourth entry.)

v3.41 (August 18, 2026): Records restructure and a skill bump.
No rule changed. (1) The version history left this document: v1.0-v3.38
now live in documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1, the
file that was LESSONS_ARCHIVE.md and still carries the v3.37 lessons
record verbatim as PART 2. The ledger's appendix is replaced by a
pointer. Three entries stay resident and a fourth pushes the oldest
down, which is the cap L-199 asked for; its part 1, a sizing section,
is still unbuilt. (2) The header gained an anchor and lost a
contradiction -- the repo copy read August 16 and the copy installed in
the Claude UI read August 17 under the SAME version, two stores with
nothing watching them the way Stale Skill = Stop watches the skills.
(3) provenance-discipline 2.3 -> 2.4 (L-203, L-204): the visibility
convention got a home, and the annotation grammar now accepts a .jsonl
or .json worksheet reference, because a returned verdict could be
checked and routed and then refused when written back into the code.
The reinstall cannot be verified from inside the session that makes it,
so the NEXT session confirms its loaded copy reads 2.4 before doing
provenance work.

(Moved down from the resident protocol on 2026-08-26 when v3.44 made a
fourth entry.)

v3.40 (August 16, 2026): No change to the protocol's own rules. Two
skills gained conventions, and both were earned the same way -- a
session hit the problem, Tony ruled, the rule went into the skill that
fires on it rather than into this document.

safe-file-editing 1.3 -> 1.4, two additions. (1) Fix In Passing, Report
It. Where a patch is already fingerprinting a file and finds a violation
of an ALREADY-RULED convention in it, fix it in the same patch and say
so, rather than noting it and moving on. Origin: a patch touching eight
files blocked itself on two Unicode arrows in a comment that predated
the work by months. Claude's first instinct was to report and leave it,
citing "fix only what asked." Tony's ruling: the convention was already
ruled, the file was already fingerprinted, and a separate sweep for two
characters would never be scheduled, so leaving it means it never gets
fixed. The anti-pattern "fix only what asked" guards against is
unreviewed DESIGN change, not mechanical compliance with a standing
rule. The encoding gate was rescoped with it -- hard-fail on non-ASCII
in inserted lines, sweep pre-existing where the conditions hold, and
print which of the two happened, because a gate that fails on somebody
else's bug blocks a correct patch and a gate that stays silent is how a
convention quietly stops being true. (2) Naming and Archiving a Patch
Script: name it patch_<handle>_<what>.py leading with the ledger handle,
number a sequence so sort order carries run order, archive to
documentation/ once run, and state which parts of the change are
permanent when the script is not. That convention was already 96 scripts
deep in documentation/ and written down nowhere, so a session that read
the delivery format still produced three unprefixed scripts and had to
be told.

orrery-coding-conventions 1.3 -> 1.4, two additions. (1) Marker
Separation for Near-Equal Radii. Where two shells sit within about 10%
of each other, the standing r*1.05 north-pole marker puts both in the
same place and Plotly shows one where the user expects two -- geometry
correct, legend correct, affordance silently absent. The inner shell
keeps the pole; each subsequent shell steps 20 degrees in polar angle at
its own radius. Separate angularly, never radially. Origin: the
chromosphere moved to true physical scale and its marker landed 0.003
solar radii from the photosphere's, about one pixel. The section says
explicitly that this is NOT the May 2026 ring-marker fix, which solved a
collision radially and cannot help at 0.29% -- reaching for it is the
trap. (2) Harvest the Conventions You Find. When you touch a file and
find a convention this skill does not hold, report it in the same
message as the work; do not silently follow it, because following
without naming is how it stays invisible. Promotion is Tony's judgment,
not the finder's. Origin: Tony's observation that "there are many
unrecorded conventions except in local files," which the patch-script
naming convention had just demonstrated.

Process note, recorded because it is the reason this entry exists at
all. Both skill files were delivered wrong before they were delivered
right, and neither error was caught by a check. The conventions file was
named for download disambiguation rather than for its destination and
was filed in documentation/, leaving two pushed source comments citing a
20-degree rule that existed in no store the skill loader reads --
cite-to-nonexistent-authority, live in the repo. Then the corrected file
was built by an insert written as a replace, which deleted its own
version block, Source line, criticality note, and the paragraph
recording what v1.2 added. Tony found that by reading the new file
against its sibling. The rebuild added a pure-addition check -- every
line of 1.3 must still be present in 1.4 -- which is the check that
should have run the first time. Deliverables now ship inside a folder
named for their destination.

(Moved down from the resident protocol on 2026-08-25 when v3.43
made a fourth entry.)

v3.42 (August 23, 2026): No rule changed in this document. THREE skill
bumps, recorded here because the recording is the point.
(1) safe-file-editing 1.7 -> 1.8 (L-226), two of Tony's rulings. The
Encoding Gate now says PROSE explicitly -- it read "ASCII only in
delivered code" and a session took that as excluding markdown, leaving
23 non-ASCII characters in a master plan it was already patching, while
Stamp What You Change had said all along that markdown is not an
exception. The skill's two halves disagreed and the reader followed the
narrower one. And a new section, The Correction Does Not Travel, one
scope out from Stamp What You Change: that governs the file the patch is
editing, this governs the OTHER files quoting the value it just changed.
Founding case -- constants_new.py read 15 R_sun from August 22 and the
critical path summary still said 17 the next day, inside the paragraph
written to correct an earlier wrong claim about the same row.
(2) orrery-coding-conventions 1.4 -> 1.5 (L-227): Hover Line Width Is a
Convention, Not an Accident. Found by Mode 5 when a tooltip ran off the
viewport -- a hover string wrapped at 72 characters in the SOURCE with
no breaks on the lines, rendering as one 378-character run. Canonical
Text Format already governed which break character and said nothing
about how often.
(3) ledger-and-session-records 1.8 -> 1.9 (L-230), and it is why this
entry exists at all. Tony observed that a skill bump runs a four-link
chain -- SKILL.md, skills_index.py, the manifest zone, a protocol
version entry -- and that only the first three fire. The binding rule
gains its fourth step. Detection is designed and unbuilt: a
maintenance-suite checker that watches the TRANSITION, because the
naive form reports 10 of 10 skills and would be ignored by its second
run.

(Moved down from the resident protocol on 2026-08-27 when v3.45
made a fourth entry.)

v3.43 (August 25, 2026): One rule added, and it is a generalization
rather than a new idea. "The Braid -- The Artifact Orders the Work"
enters Part 3 directly after The Artifact Bounds the Audit, which it
extends by one axis: that rule bounds which values are in scope, this
one bounds which are in scope NEXT, for any correctness program rather
than for provenance alone. Origin: Tony's August 22 ruling had lived
only in the master plan, where it carries SEQUENCING authority for the
gallery. He was applying it across the constants work too -- from
memory, because it was written nowhere that fires. On August 25 a
constants migration ran global and did not terminate: one conversion
factor led to a shadow name, to three aliases, to a second constant at
38 sites across 11 modules, in one evening, with zero movement on the
artifact that ships. Tony's own framing, and the reason this entry
exists: "it is a meta-principle. its not even in the protocol as such."
The section's operative additions beyond the master plan's version are
the discovery/remediation split -- discovery enumerates and fixes
nothing, so it terminates -- and one ledger row per CLASS rather than
per instance. Handle L-250. Version history: v3.40 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-08-28 when v3.46
made a fourth entry.)

v3.44 (August 26, 2026): No rule changed in this document. TWO skill
bumps and one long build, recorded here because the recording is the
fourth link of the chain L-230 named and the only one that does not
fire on its own.

(1) provenance-discipline 2.6 -> 2.7, three sections, all gaps rather
than refinements. One Value, One Home [CRITICAL] states positively what
No Shadow Constants only prohibited: a numeric value's home is
constants_new.py, and everything else -- drawing, hover string, tooltip,
comment, and code that cannot run -- references it. Its scope boundary
is stated in the same breath, because without it the rule reads as
hauling n_points and marker_size into the constants file: measured
values migrate, declared drawing parameters do not. Report to the
Figures You Have [QUALITY] had no home in any skill; compute at full
precision, report to the figures the least precise input supports, and
a subtraction is governed by decimal places. A Breadcrumb Must Not Cite
[CRITICAL] records that a Ref line or a bare URL inside the scanner's
thirty-line lookback becomes a citation for the unit beside it, so an
honest pending-sourcing note carries a ledger handle and nothing else.

(2) orrery-coding-conventions 1.5 -> 1.6 (L-249): the angular step in
Marker Separation for Near-Equal Radii becomes an outcome rather than a
fixed 20 degrees, with 20 for the solar skin stack and 10 for Earth's
crust as the two worked cases. The required step depends on frame width
and frame width depends on which shells are enabled, so one global
number was always going to be wrong somewhere.

The founding build was L-249, Earth's interior boundaries. Five patches
in one evening took four radius fractions that had been approximate
values taken by hand in 2024 and made them derivations of sourced radii
in constants_new.py, with the hover prose interpolating the same
constants. Three shells moved; the lower mantle moved 290 km. Two
defects of the class this protocol exists to catch were found in the
work itself rather than afterwards: a reference true of a constant and
false of the note beneath it, and a region check whose slice came out
empty so it passed having examined nothing. Handles L-249, L-253,
L-254, L-255. Version history: v3.41 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-08-29 when v3.47
made a fourth entry.)

v3.45 (August 27, 2026): One rule added, one skill bumped, and the
rule was earned in the same session that produced the bump.

Method Belongs to the Skill [Part 3, after The Braid]. A question about
how the work is done is a skill rule; a question about what the project
should be is Tony's. Origin: three method questions escalated to him in
one evening -- the status-line format, the mechanism for checking a
citation, and which end of a sourced range to draw. He sent all three
back, the third with "Isn't #4 also a skill method?" after Claude had
conceded the principle two sentences earlier and then escalated anyway.
Both independent Mode 7 reviewers, working from the same prompt on the
same day and without seeing each other, had already named this as a
finding: decisions reach the sole integrator that a rule should absorb.

provenance-discipline 2.7 -> 2.8 (L-256), nine sections and four
revisions. The Gate Binds at SERVING moves the binding point from
drawing to publication -- a visitor takes what the site shows as true,
and nothing downstream of the orrery knows what a correct radius is. The
Access Standard makes reachability a precondition of a citation: open
full text, a free abstract, or a Scholar or Books snippet carrying the
qualifier, and no paywalls, because Tony has no research library. The
Status Line has every value in constants_new.py declare its own
provenance state so the scanner reads instead of inferring -- which
deletes the inference machinery behind four measured failures, the
thirty-line lookback among them. Measured Is the Goal, Declared Is the
Fallback carries the range rule: store the range as data, derive the
drawn value by a stated rule, and put the reason for the pick on the
row. The Exhibit Requirement makes a verdict without a quotation
UNVERIFIED, with the quotation demoted from the clearance to a routing
aid and the source text read in context becoming the evidence of record.
Retired in the same bump: the two-annotation criterion for
V_CROSS_CHECKED, which measures concurrence, and concurrence is what
kept a wrong Alfven surface alive while the dissenting leg carried the
evidence.

One defect worth recording rather than quietly fixing. The skill had
taught the chromosphere drawn at 1.1 solar radii as its worked example
of a declared visualization boundary, for eleven days after the code
promoted that value to the physical figure. A session read it and
reported the retired value to Tony as current -- the third superseded
state that session pulled forward from a document rather than from the
store, which is the argument for the status line stated as evidence
instead of as an idea. Examples Go Stale Like Values [QUALITY] is the
rule that follows.

Version history: v3.42 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-08-29 when v3.48
made a fourth entry.)

v3.46 (August 28, 2026): No rule changed in this document. One skill
correction, recorded here because the recording is the fourth link of
L-230's chain and the only one that does not fire on its own.

provenance-discipline 2.8 -> 2.9 (L-256). The Gate Binds at SERVING
becomes The Gate Binds at EXPORT. 2.8 was written earlier the same
evening and placed the gate where the harm lands -- a visitor taking a
served value as true. Tony's ruling of 2026-08-28 moves it upstream to
where a check can still run: "I think provenance should be settled
before it leaves the orrery to the gallery cache. There is no
provenance checker in the gallery."

Verified rather than assumed before the edit was written.
provenance_scanner.py exists only in the orrery repo. The nightly
builder lives in the GALLERY repo and scores nothing -- two mentions of
provenance in the whole file, one a docstring line recording where its
copied constants came from, one a warning string. The two repositories
do not share a checker, so a gate at publication sits downstream of the
last instrument in existence. That is A Check That Cannot Fail Is Not
Passing in the pipeline layer rather than in code.

The section now separates WHY from WHERE explicitly, because the
correction is exactly the kind a future session would undo by
reasoning from harm rather than from enforceability. Why: serving.
Where it fires: export. What stays free: drawing.

One consequence raises a priority. objects_config.json is maintained by
hand in the gallery repo, so the export boundary the gate names is
today a human copy with no check on it. The cross-repo transport
becomes the gate's missing enforcement point rather than a defence
against later drift -- higher than MASTER_PLAN_INTERACTIVE_GALLERY.md
currently places segment 2, and an amendment that document is owed.

Version history: v3.43 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-08-30 when v3.49
made a fourth entry.)

v3.47 (August 29, 2026): One rule amended, and one skill bump
recorded a day late.

The Register Rule [Part 2] makes PLAIN SPEECH THE DEFAULT. Tony's
instruction, 2026-08-29: "please use plain speech in your chat as the
default." The earlier wording made plain speech a REGISTER -- one
entered for explanations, design rationale and as-built narrative --
so ordinary delivery prose sat outside the three checks and passed
them by not being subject to them. The compressed voice keeps its
home in this document and in the skills, where a line is reference
somebody scans because they already own the idea. It leaves the chat.

The case that earned it, from the same session and about this same
patch: "I left it out of the patch rather than expand scope into the
protocol without your word; it's captured as L-258's Gap with a
Tony-action." Tony: "I don't follow." Three project labels in one
clause, in a sentence that was not explaining anything. Handle L-261.

provenance-discipline 2.9 -> 2.10 (L-258). The Store Carries the
Verified Figure [CRITICAL], added under Report to the Figures You
Have, which governed REPORTING and left the stored value uncovered.
Where a source gives a verified figure more precise than the stored
value, the store carries the verified figure; rounding happens at the
reporting step, never at rest. Founding case: RADIATIVE_ZONE_AU held
0.7 beside its own comment saying it rounded 0.713 -- the store
recording that it was rounding, and rounding anyway, in a value drawn
on a public page. Narrowed in the same breath against the two cases
it would damage: a pick from a range stays a declared choice, and a
visibility stylization promotes when the physical value becomes
drawable rather than for want of digits.

Tony's ruling, 2026-08-29, and his reason for making it a SKILL rule
rather than a decision: it resolves the same way next month, for a
different constant, in a different file. That is Method Belongs to
the Skill applied to its own layer.

The bump's own record is its own lesson. Steps 1, 2 and 4 travelled
together on August 29 -- the version line, skills_index.py, the
commit. Step 3, this entry, did not. The manifest going current on
its own DISGUISED the omission, exactly as the binding rule warns:
the protocol looked updated because half of it was. It surfaced the
same day, in the next session, by reading the manifest against the
history -- not by any check, because the check that would catch it is
L-230, designed and unbuilt.

Recorded a day late and said so, rather than backfilled as though it
had been here. A document whose subject is anchors being true is the
wrong place to be casual about when something was written.

Version history: v3.44 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-08-31 when v3.50
made a fourth entry.)



### Preserved verbatim: v3.29 Technical lessons (now field notes in skills)

- Cache: cache[name]['elements'] (nested dict)
- Reference frames can differ for same object; inclination reveals coordinate system
- Osculating elements must match viewing center (Charon@9)
- Horizons centers: Only numeric IDs work. helio_id vs center_id: opposite directions
- JPL binary IDs: 20XXXXXX (barycenter), 920XXXXXX (primary), 120XXXXXX (secondary). Derive primary from secondary via mass ratio
- Plotly camera: Axis ranges control zoom, not camera distance
- xvfb-run enables headless GUI testing; SystemButtonFace -> gray90 for Linux on a THROWAWAY copy -- the swap is NOT idempotent (26 native gray90 literals in palomas_orrery.py), so never restore-in-place on the deliverable
- Python binary mode (rb/wb) preserves line endings and Unicode; sed can corrupt multi-byte UTF-8
- Position data flows through 5 parallel pipelines in palomas_orrery.py -- ALL must be patched
- Plotly customdata survives JSON extraction; _studio flag survives -- downstream consumers can detect curated plots
- Plotly.js native touch works on mobile/tablet without custom code
- D-pad pan arrows: 2D uses Plotly.relayout on axis ranges, 3D uses camera eye/center shifting
- Stacked bugs: fixing one can reveal a second that was invisible before
- JS: JSON.stringify(undefined).substring() crashes; always guard with || ''
- position: fixed escapes CSS containment; position: absolute stays inside parent
- Plotly 3D annotations go on scene.annotations; 2D on layout.annotations
- Gallery Studio source vs export: source has figure-native values; export has _studio_config overlay
- Horizons step format: {number}{unit} (1m, 5m, 1h, 6h, 1d)
- Encounter resolution: cube scale (dist_km * 4) frames view; curvature scale drives fetch step
- Roche limit is not absolute: tensile strength allows survival inside it
- Celestial sphere in ecliptic frame: unit vectors rotated from equatorial via obliquity about X axis
- Sphere shells render via SHELL_CONFIGS -> build_sphere_shell -> create_info_marker (factory). Inline markers in *_visualization_shells.py are dead code for sphere shells; custom geometry (magnetospheres, rings, belts) routes via CUSTOM_SHELLS and uses the live inline path
- Plotly Scatter3d ignores marker border WIDTH (plotly.js #4118) -- the contrast lever is FILL color, not border. 3D symbol palette is only 8: circle, circle-open, cross, diamond, diamond-open, square, square-open, x
- A swallowed exception in try/except hides render bugs; an undefined variable can drop a marker silently for weeks. Check the console for the caught-error print
- grep -c exits non-zero on a zero count, silently breaking an && chain (the next command never runs while output looks complete) -- run verification greps standalone or join with ;
- GitHub is reachable in-environment: git ls-remote gives branch+HEAD SHA with no auth; raw.githubusercontent.com fetches files byte-exact. The HEAD SHA is the unforgeable current-state token AND the round-trip check -- a matching remote HEAD confirms commit + push + sync at once (project knowledge auto-syncs from the repo as of v3.27)
- The two surviving store failures are honest and visible -- no push, or no sync -- both show as a HEAD mismatch. (v3.26's stale-snapshot + served-ghost failures came from the manual step, retired in v3.27)

================================================================
PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37
================================================================

LESSONS REMOVED FROM PROJECT_INSTRUCTIONS.md AT v3.37

August 11, 2026. Working copy at the time was 824 lines; repo HEAD was
22b0db339e0ce99ca0a6a6dc11f1c9546845577f at
https://github.com/tonylquintanilla/palomas_orrery.

THIS FILE IS A RECORD, NOT A STORE. Nothing in it is load-bearing. Every
bullet below was removed from the protocol's Part 5 Lessons Archive
because the same instruction is already stated somewhere that FIRES -- a
Part 3 CRITICAL gate, a Part 2 or Part 4 section, an Anti-Patterns row, a
Mode 7 table, a Quotable, or a skill that loads on task match. Each entry
names where it still lives.

The lessons that exist in only one place are NOT here. They stayed
resident in the protocol, which is the point of the cut.

Why this file was briefly something else. An earlier version of this
trim moved all forty-one lessons here and left the protocol with only a
pointer. That was wrong and was reversed the same day. A skill fires on
task match and the ledger is read at session start, but an archive file
has no trigger -- so the fourteen lessons with no counterpart elsewhere
would have quietly left the system. The v3.30 precedent, where technical
lessons went into skills, does not transfer, because skills fire.

If any line below turns out to be doing work its counterpart does not do,
put it back in the protocol. That judgment is Tony's, and this file exists
so it can be made by reading rather than from memory.


1. Map multi-file changes before implementing. Parallel pipelines: fix in one doesn't propagate
   STILL STATED IN: Part 2 Multi-File Changes; Part 3 Check All Parallel Pipelines [CRITICAL]

2. Unicode in generated files breaks on Windows -- use ASCII
   STILL STATED IN: Part 2 Anti-Patterns, 'Use unicode in code'; safe-file-editing Encoding Gate

3. Agentic = confident but harder to review; targeted = visible changes
   STILL STATED IN: Part 2 Agentic vs Targeted Choice table

4. Multi-AI: Gemini for domain knowledge, Claude for implementation, Tony integrates
   STILL STATED IN: Part 1 Mode 7 AI Roles table

5. Iterative design beats first-draft architecture -- each round should simplify
   STILL STATED IN: Part 2 Iterative Design Planning; Anti-Patterns 'Build first architecture'

6. Gallery pipeline: HTML export -> JSON converter -> gallery viewer
   STILL STATED IN: gallery-pipeline skill (fires on gallery work)

7. Flag-based contracts: _studio means "trust this, don't override." Strip unconditionally before guards
   STILL STATED IN: Part 2 Anti-Patterns, 'Guard strips with if list:'; gallery-pipeline skill

8. Renderer refactor: extract duplicated inline code into source module
   STILL STATED IN: Part 2 Anti-Patterns, 'Duplicate rendering -> Extract to source module'

9. /mnt/project/ is a read-only snapshot from session start. Does not update mid-session
   STILL STATED IN: Part 1 Context Priority 'Project file staleness'; Part 3 Uploads Before Project Files [CRITICAL]

10. Collegial Mode 7: Claude-to-Claude relay via Tony. No orchestration -- "here's the job, flag problems"
   STILL STATED IN: Part 1 Mode 7 Patterns table, 'Collegial'

11. LOTO lesson: critical failures happen when procedures are not developed, not enforced, or not followed -- all three are distinct. The most critical procedure is often the one that feels unnecessary right up until it isn't
   STILL STATED IN: Part 2 Procedural Criticality, closing paragraph (LOTO, verbatim)

12. Map the dispatch before editing the leaves: grep for where a function is CALLED, not imported. Compile-clean and tests-pass do not detect that a function is never called
   STILL STATED IN: Part 3 Verify Execution, Not Appearance [CRITICAL] -- verbatim

13. Structural fixes scale; data-side fixes don't. A violation in N consumers of one producer -> fix the producer. (83 sphere-shell pairs brought into compliance by 2 edits to the factory)
   STILL STATED IN: Part 5 Quotables, 'fix the producer'; Part 2 Anti-Patterns

14. Handoffs are claims; runtime output is fact. When a smoke test contradicts a handoff, the smoke test wins and the handoff gets corrected
   STILL STATED IN: Part 2 Anti-Patterns, 'handoff is a claim, render is fact'

15. Data-content sweeps (hover text, legendgroup, marker styling) need a runtime smoke test that constructs and inspects traces on the LIVE dispatch -- a smoke test of the wrong path passes falsely
   STILL STATED IN: Part 3 Agentic Pre-Test [CRITICAL]; agentic-pre-test skill

16. Transactional binary-mode patching for clustered edits: one script, anchored byte-level replaces, each asserting exactly one match -- all-or-nothing, fails loud on drift
   STILL STATED IN: safe-file-editing skill, 'Transactional Patching for Clustered Edits'

17. Assign, don't hardcode, to stay in the house pattern: define color = 'white' once, reference it from both line and marker -- one-line restyle later
   STILL STATED IN: orrery-coding-conventions skill

18. Enumerate uploaded files before claiming a review: the in-context subset is invisible to Tony and not authoritative. Read the whole set on disk first (lesson: a review and a protocol edit were both built on 9 of 19 handoffs)
   STILL STATED IN: Part 3 Enumerate Uploads Before Claiming a Review [CRITICAL] -- verbatim

19. Floating items get lost; capture on first mention. A bug "floating outside the deferred list" only closed when Tony asked "is this deferred?" -- promote observations into the ledger immediately, even if no work happens yet
   STILL STATED IN: Part 5 Quotables, 'Floating items get lost; capture on first mention'

20. Verify universal-propagation claims with grep. "A central factory exists" does not imply "every call site uses it" -- grep the actual call sites when propagation is load-bearing; don't trust the handoff narrative
   STILL STATED IN: Part 5 Quotables, 'Grep, don't trust the narrative'

21. Tony's session loop makes the repo trustworthy: sandbox -> test -> local repo -> provenance/atlas update -> push, all before a new session. Because the push precedes the session, repo HEAD == session-start ground truth by construction
   STILL STATED IN: Part 3 Session-Start Repo Pull [CRITICAL] -- states the loop verbatim

22. Route around a fragile store you do not control to one you do: project knowledge proved it could be stale and haunted; the repo is Tony's, so make it the build base -- and ultimately remove the fragile store entirely (v3.30, July 2026)
   STILL STATED IN: Part 5 Quotables, 'Route around the store you don't control'

23. Irreducibility protects both sides equally
   STILL STATED IN: Part 4 The Irreducibility Argument

24. Hassabis corroboration: AI's limitations map to why partnership outperforms autonomy
   STILL STATED IN: Part 4 The Hassabis Corroboration

25. The Double-Helix IS the safety mechanism: error-correction and alignment are the same loop
   STILL STATED IN: Part 4 The Double-Helix IS the Safety Mechanism

26. The Weasley Principle: the vulnerability comes when the conversation becomes the only conversation
   STILL STATED IN: Part 4 The Weasley Principle

27. Broad-first requires judgment to recognize convergence. That judgment is Tony's
   STILL STATED IN: Part 4 Broad-First as Valid Methodology
