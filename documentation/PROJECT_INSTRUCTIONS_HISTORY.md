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

v3.48 (August 29, 2026): No rule changed in this document. One skill
bump, recorded in the same commit that made it -- which is the whole
of the improvement over this morning.

safe-file-editing 1.8 -> 1.9 (L-236). Compare Content, Not Bytes
[QUALITY]. A guard or a check that compares RAW BYTES across a
Windows working copy refuses, or cries wolf, on files nobody has
changed: any tool writing in text mode leaves CRLF behind, git
normalises it back to LF on commit, and the two copies then differ
byte-for-byte while agreeing on every character. Compare the
LF-normalised content, write each file back in the style it was
found in, and SAY when normalisation was what saved it.

Two instances in one day earned it. A four-file patch refused
because ledger_index.py had left the ledger CRLF; the md5 was
reproduced exactly by converting the repo copy, which proved the
content was identical. Then the new gallery runner called a correct
deploy stale for the same reason. The second is the lesson: the
first had been diagnosed and fixed in the patch scripts hours
earlier and was not carried to the runner already written. One
producer, two consumers, one of them moved.

Kept at [QUALITY] on purpose. Both failure directions are loud, so
nothing is silently corrupted and nothing passes that should not;
what it costs is trust in the check. The critical tier stays short.

One obligation this bump cannot discharge from inside the session
that made it. A skill lives in three stores, and the account install
is the copy Claude actually loads; a reinstall is invisible to the
running conversation. So: safe-file-editing went to 1.9 at
`bfa9de2f`, the session that bumped it had loaded 1.8, and the next
session confirms its loaded copy reads 1.9 before doing patch work.

Version history: v3.45 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-08-31 when v3.51
made a fourth entry.)

v3.49 (August 30, 2026): One rule added, in two pieces and two tiers.
No skill changed. Landed in two commits the same evening; this entry
describes the settled form, and says below what the first commit got
wrong.

A Report Names Its Items [QUALITY], Part 3, immediately after A Check
That Cannot Fail Is Not Passing -- and a FOURTH move inside that gate,
make the delta name what moved. Tony's ruling, 2026-08-30. A count
states a size; names state what is there. A report giving only the size
is complete only for a reader who can go and find out what, and neither
reader here can -- Claude resets and will not open the file, Tony
cannot read everything and does not grep. A report has to be complete
enough to act on where it lands.

The first write-up had this as an attention problem, a number being
easy to skip past. Tony corrected it, and the correction is the rule:
a count is not a weak signal, it is a signal that only works for a
reader who can perform a lookup neither reader performs.

NOT a runner convention, and deliberately not a skill. Method Belongs
to the Skill was applied and answered the other way -- the grounds are
the two READERS rather than how any one tool reports, and the two
readers are what this protocol is for.

The scope is broader than the sweep that raised it, on Tony's
instruction of the same day: scanner and runner summaries, ledger and
handoff enumerations, counted claims in this document and in the
skills, and findings and backlogs. Not only counts of grouped features.

THE SPLIT IS THE PART THE FIRST COMMIT GOT WRONG. It put the whole rule
in at [CRITICAL]. This document's own promotion test is that a check
moves up when a failure demonstrates it was load-bearing. The naming
half has failed repeatedly and in view -- the scanner summary, the
audit's coordinates, the L-268 sweep, the pipeline count below -- and
every one of those was recoverable. The count-delta half has NOT been
witnessed here: nobody has yet cleared one Tier-1 finding and gained
another with the total unchanged. It is inferred, and it is the half
that can pass while blind. So the sharp case went into a gate that is
already [CRITICAL] and the general habit went in at [QUALITY], which
keeps the critical tier short and leaves a promotion path if the delta
case ever bites. A second Opus session argued it; Tony carried it.

THE FOUNDING CASE IS CORRECTED TOO, and how it was wrong is the lesson.
Check All Parallel Pipelines had read "5 parallel pipelines in
palomas_orrery.py" and named none, in the sentence telling the reader
to map ALL consumers. The five WERE named -- in README.md, which the
gate does not point to. And a second candidate list existed on a
DIFFERENT AXIS: six FETCHERS inside palomas_orrery.py against the
README's five CONSUMERS across the project. Two entries appear in both,
three of the consumers fetch nothing, and neither list is a subset of
the other. The gate had merged them, taking a cross-file count and
attaching a single-file scope, describing a set that does not exist --
then half-naming the real list in the next sentence, four of five,
missing social export. Tony's ruling: the gate means the CONSUMERS, the
names belong in the gate rather than in another document, and the
in-file scoping goes. All five paths were verified present at a667e128
before being written in, and two of them turn out to live in the
GALLERY repository under tools/, which the old scoping actively hid.
The fetcher list is kept on L-269 as the answer to a different
question. A count does not carry the axis it was counted on.

Ledger, first commit: L-265 through L-269 placed, and L-262's diagnosis
amended in view rather than corrected in place. The framing smoke test
was never about interactive.html, its row in the gallery runner gates,
and the fix is two lines needing no Mode 5. Confirmed the same evening:
the Page framing row now passes twelve checks in the gallery runner.

Version history: v3.46 moved down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-02 when v3.52
made a fourth entry.)

v3.50 (August 31, 2026): No rule changed in this document. One skill
bump, and a correction finally travelling.

orrery-coding-conventions 1.6 -> 1.7 (L-269), plus the same correction
in documentation/CLAUDE.md and README.md. v3.49 fixed Check All
Parallel Pipelines HERE and left three live stores carrying the old
merged sentence -- a cross-file count of five wearing a single-file
scope. One of the three is a skill that loads on every orrery session,
so the wrong instruction was being handed to whoever read it, including
Claude.

That is The Correction Does Not Travel in the shape the rule predicts:
the fix went into the document being edited and stopped there. It was
found by asking, on the day the rule landed, which OTHER stores carry
the sentence -- 46 documents, 43 of them archives and session records
correctly left alone.

All three now name the five consumers with their files and repos, and
say plainly that two of the five are in the GALLERY repository. That
last part is the load-bearing half: a reader following the old
instruction as written would grep one repo and find three of five.

The fetcher list is recorded beside the consumer list in
orrery-coding-conventions, labelled as the answer to a different
question, because the two are on different axes and neither is a subset
of the other.

One obligation this bump cannot discharge from inside the session that
made it. A skill lives in three stores, and the account install is the
copy Claude actually loads; a reinstall is invisible to the running
conversation. So: orrery-coding-conventions went to 1.7 at
`04bba3ca`, the session that bumped it had loaded 1.6, and the next
session confirms its loaded copy reads 1.7 before doing orrery visual
work.

Version history: v3.47 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-03 when v3.53
made a fourth entry.)

v3.51 (August 31, 2026): No rule changed in this document. One skill
bump, and the end of a habit nobody had decided on.

safe-file-editing 1.9 -> 1.10 (L-271). Git Is the Backup [QUALITY]:
patch scripts stop writing `.bak` and print the Discard Changes path
instead.

The argument is structural, which is what makes it a rule. A patch
guards on a content fingerprint and refuses when the working copy does
not match, so at the moment it writes, the file on disk is the committed
version. Git holds it. The `.bak` can never be the only copy, and the
one case where it would earn its place -- uncommitted work -- is exactly
the case the gate refuses to run in.

A stale copy is an active hazard rather than clutter. The orrery's own
.gitignore records why, from the sweep of 2026-08-29: a session grepping
for a value can hit one and read it as current, and two of the nine
swept that day were a superseded master plan and a superseded skill.

Tony's question was the whole of it -- "why do we create them at all?" --
and his correction to the rate stands with it: days, not weeks. All
eight swept from the gallery on 2026-08-31 were made in the preceding
two days. He also believed the maintenance runner cleaned them up. It
does not; the word does not appear in that file. What existed was one
manual sweep, which is how a habit gets mistaken for a mechanism.

The .gitignore rule was widened in the same commit. `*.bak` matches only
names ENDING in .bak, so `.bak1`, `.bak2` and `.bak_L271` slipped
through the 2026-08-29 sweep and kept being committed -- which is why
two close-approach cache backups survived it, and why the gallery, whose
rule was narrower still, kept all eight of its own.

One obligation this bump cannot discharge from inside the session that
made it. A skill lives in three stores, and the account install is the
copy Claude actually loads; a reinstall is invisible to the running
conversation. So: safe-file-editing went to 1.10 at `ccd1ac96`, the
session that bumped it had loaded 1.9, and the next session confirms its
loaded copy reads 1.10 before doing patch work.

Version history: v3.48 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-06 when v3.54
made a fourth entry.)




v3.52 (September 2, 2026): No rule changed in this document. One skill
bump, and a header that had stopped travelling.

gallery-assembler 1.1 -> 1.2 (L-279). Mode 5 as MEASUREMENT, not just
acceptance, plus a field note on mutating a plot from inside a Plotly
event handler.

The skill already owned this and was not used. Its `fires_when` line
said "Mode 5 acceptance" before tonight, and Claude version-checked the
skill during a four-hour hang investigation without ever opening it --
including at the moment of handing over a patch whose own output said
"this one needs Mode 5". The wording was the reason: acceptance reads as
judging something FINISHED, and nothing about a page that will not
respond sounds like acceptance. The trigger now names the diagnostic
case in the words Tony would use -- it hangs, it is unresponsive, it
worked yesterday.

The seven rules in that section are each attached to a failure that
earned them. Three came from stating conclusions about trials whose
CONDITIONS had been inferred rather than recorded, and Tony carried
every one of those corrections. That is the load this protocol exists to
spare him, and it is why the placement question was worth the time it
took. Tony's ruling: the home existed; use it.

THE HEADER HAD BEEN STALE SINCE v3.50. This line read v3.49 while the
document's own Version History carried v3.50 and v3.51 entries -- the
correction travelled into the history and stopped there, which is The
Correction Does Not Travel pointed at the version stamp itself. Fixed
here, along with the SHA anchor, which had also sat at `ded99fbe` across
three versions.

One gap recorded rather than closed: documentation/ has no archived copy
for v3.50 or v3.51. Their content is carried in full by their resident
Version History entries and git holds the exact bytes, so nothing is
lost; reconstructing the two files is a separate decision.

One obligation this bump cannot discharge from inside the session that
made it. A skill lives in three stores, and the account install is the
copy Claude actually loads; a reinstall is invisible to the running
conversation. So: gallery-assembler went to 1.2 at `e71f38ae`, the
session that bumped it had loaded 1.1, and the next session confirms its
loaded copy reads 1.2 before doing gallery work.

Version history: v3.49 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-08 when v3.55
made a fourth entry.)


v3.53 (September 3, 2026): One clause corrected, one note added. No
skill changed.

MODE 7 SAID RELAY PARTNERS CANNOT READ THE REPO, AND THEY CAN (L-276).
The "Documents as handoffs" clause gave as its reason that "the
receiving AI has zero independent repo access." This project's own
records disproved it: the L-191 relay response records Fable running
`git ls-remote` against the pinned SHA and parsing the source, and
Tony ruled 2026-09-02 that every model queried here reaches GitHub.
The anchor requirement is unchanged. Its reason now covers both kinds
of partner: the repo moves, so an un-anchored document does not say
which state it describes; one that can fetch needs the anchor to fetch
the right bytes, one that cannot needs it to know what it is reading.

The failure that surfaced it is the lesson. A session read the L-191
relay response, which says plainly that Fable cloned the repo, and
then repeated the blanket sentence anyway -- a general claim in a
trusted document held over specific evidence already in hand. The
same shape as trusting a handoff over the render, one layer up.

THE GEMINI NOTE, on Tony's question 2026-09-03: how does Gemini see the
repo without an upload or Drive? Google's documentation for the Gemini
web app answers it: one public repository can be IMPORTED as a
snapshot, but a GitHub URL in a prompt is not read, nothing is fetched
at a SHA, commit history is not visible, and the feature is not on
mobile. Written under AI Roles so the next session does not rediscover
it. Gemini is the second case in the corrected clause.

Version history: v3.50 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-10 when v3.56
made a fourth entry.)


v3.54 (September 6, 2026): One clause extended, one skill bumped
carrying three changes, and a design round that produced no code.

THE RELAY ANCHOR NOW NAMES THE RULES, NOT ONLY THE CODE (L-290).
"Documents as handoffs" already required built on <SHA> at <URL> on
every outbound document, and v3.53 had just corrected its reason to
cover partners that can fetch and partners that cannot. What neither
said was that PROJECT_INSTRUCTIONS.md and the task-relevant SKILL.md
files are fetch targets too. So a relay partner got the code with none
of the governance and worked on it without the rules the work runs
under.

The failure that earned it is small and exact. A parallel Claude
Sonnet session, outside this account and Project, reasoned correctly
to the right conclusion -- and then proposed a ledger handle that was
already taken and offered its entry "ready to paste", which the ledger
skill rules out. It had the repo. It did not have the ledger skill or
the live handle count, and nothing in the document it was given told
it where to look.

Two amendments beyond the drafts, both Tony's. The skills named are
the ones THE TASK FIRES, not a blanket list, because sending all ten
teaches a partner to skim. And the document ASKS FOR A READ-BACK: the
partner states which rule files it actually read, because a return
that does not name them is telling you it did not read them. That
read-back is the only part of the mechanism that can fail visibly --
an omitted anchor line looks exactly like one that was not needed.

One correction to the draft, and it is the kind this project keeps
finding. The Gemini bullet said no SHA pin is possible for the
protocol or skills "any more than it is for the code", so paste them
inline. But those files LIVE IN the orrery repo: a Gemini that
imported the orrery already HAS them, unpinnable but present. Gemini
imports ONE repository (v3.53's own note, L-276), so the real paste
case is a GALLERY import, which leaves it with no protocol and no
skills at all because they are in the other repo. The rule now splits
by which repo was imported.

ledger-and-session-records 1.9 -> 1.10, carrying three things.
The anchor amendment above; ONE SESSION, ONE BUMP -- a session does
not ship two versions of one skill, so everything it decides rides a
single version (Tony's ruling when this amendment and L-296 both
wanted 1.10); and the master plan restamps once per DESIGN BUILD
rather than at "key junctures", which was not countable and so kept
sending the judgment back to Tony.

The Earth exhibit was designed the same evening in a zero-code round
(L-291) and the Sun's chrome closed (L-289). Neither changed a rule
here. Record:
documentation/PREDESIGN_earth_exhibit_20260906.md in the gallery repo.

One obligation this bump cannot discharge from inside the session that
made it. A skill lives in three stores, and the account install is the
copy Claude actually loads; a reinstall is invisible to the running
conversation. So: ledger-and-session-records went to 1.10 at
`50cbd2df`, the session that bumped it had loaded 1.9, and the next
session confirms its loaded copy reads 1.10 before doing ledger work.

Version history: v3.51 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-11 when v3.57
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

v3.55 (September 8, 2026): No rule changed in this document. TWO skill
bumps, taken BEFORE the build they serve rather than inside it.

gallery-assembler 1.2 -> 1.3 (L-304) and provenance-discipline
2.10 -> 2.11 (L-306). The assembler skill gains four field notes from
the 2026-09-07/08 gallery session -- three Plotly 2.35.2 behaviours read
out of the shipped bundle, one viewer lesson that is not Plotly's. The
provenance skill gains A Drawing Approximation Does Not Promote
[CRITICAL].

THE SEQUENCING IS THE POINT, and it is a correction to a habit rather
than to a rule. This protocol already records, twice, that a bump made
mid-build cannot be verified from inside the session that made it: the
session loads the old copy, the reinstall lands invisibly, and the
confirmation has to be written forward as an obligation the NEXT
session discharges. v3.52 did that for gallery-assembler 1.2 and v3.54
for ledger-and-session-records 1.10. Both discharged correctly. But an
obligation that travels is a check deferred, and it only works because
somebody reads the handoff.

Tony asked whether the bump could be taken first. It can, and it is
strictly better: the build session loads 1.3 and 2.11 against a
manifest that says 1.3 and 2.11, and the gate fires on something it can
actually read rather than on a promise. Nothing travels. The obligation
paragraph is absent from this entry for the first time in four
versions, and that absence is the whole of the improvement.

Two bumps in one session is not a violation of ONE SESSION, ONE BUMP.
That rule is per SKILL -- a session does not ship two versions of one
skill. Two different skills ride one protocol entry, which is what this
one is.

THE RULE ADDED TO THE PROVENANCE SKILL, in one sentence: a number typed
into a renderer because the result looked right is not a constant
waiting for a home. Earth's magnetosphere is the founding case -- a half
ellipsoid with typed axes, a conic eccentricity typed at the call site,
and a sweep cap the code itself labels a MODE-5 KNOB, all of them
candidates for promotion into constants_new.py during L-291's
migration. Tony refused it. The rebuild on a cited model is L-305; the
step-3 split that followed is in L-291.

The header stamp and the SHA anchor move with this entry. v3.52 records
that they sat stale for three versions because the correction travelled
into the version history and stopped there.

Version history: v3.52 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

v3.56 (September 10, 2026): No rule changed in this document. TWO skill
bumps, both from closing the Earth exhibit (L-291).

interactive-exhibit 1.0 -> 1.1. Earth step 3 moved the page from one
`EXHIBIT === "<key>"` branch per room to an `EXHIBITS` table, and the
skill still described the branch in four places: the anatomy's switch
and class rows, step 3, and step 7's scene picker. Step 3 also gains
the driver rule the build found by running the resolver -- the body is
the CENTER, and `objects` is whatever the resolver accepts against it --
and step 7 gains a check for an existing card before Studio is opened,
with the order Studio forces. The rename paragraph now points at L-309,
which deferred the rename with its trigger.

ledger-and-session-records 1.10 -> 1.11. A Closing Item Re-homes Its
Loose Ends [QUALITY]: before an item goes DONE, each thing its body
records as not done gets a home in an open item, or is struck with a
reason. Three were riding inside closing items, one behind a pointer to
an item that never mentioned it, and one had already fired -- the
gallery editor's copy defect, recorded inside L-303, hid the first Earth
card from the desktop lobby.

THE CARD IS THE LESSON, and it is Verify Execution, Not Appearance one
layer out. The 2026-09-09 handoff said step 7, the card, had not
started. A card for the exhibit had been in the gallery since that
afternoon, made by copying a static card, and the session never read
the metadata that showed it. A review read it the next morning,
replayed the viewer's Featured rule against it, and predicted what each
screen would show; Tony's eyes then agreed. A handoff's claim about a
step is checked against the artifact that step produces.

Both skills read the same in all three stores before the bump. This
session loaded 1.0 and 1.10, so the obligation travels as usual:
interactive-exhibit went to 1.1 and ledger-and-session-records to 1.11
in patch_L291_15; the next session confirms its loaded copies read 1.1
and 1.11 before exhibit or ledger work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.53 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

v3.57 (September 11, 2026): No rule changed in this document. THREE
skill bumps, taken together at the close of the 2026-09-10 evening
session and BEFORE the builds they serve.

orrery-coding-conventions 1.7 -> 1.8 (L-317), interactive-exhibit
1.1 -> 1.2 (L-316, L-318), safe-file-editing 1.10 -> 1.11 (L-315).

TWICE IN ONE EVENING THE INTERACTIVE LACKED A SOLUTION THE ORRERY
ALREADY HAD, and that is what the first bump is for. The gallery drew
every info marker red, against orange and red shells, because Tony's
two-standards outline rule of May 2026 lived in the code and in
shell_configs.py comments and had never been written into the skill a
marker session loads (L-317). Separately, the orrery declares a marker
angle per shell where one is needed, while the gallery stepped from the
pole and left nine markers on the drawn axis (L-320). Only the first
was a skill gap; Tony ruled the second directly, keeping the gallery's
own steps.

The rule the first case earns is this document's own Context Priority
read from the other end: A CONVENTION THAT IS NOT IN THE SKILL DOES NOT
TRAVEL. The code is not the store a fresh session reads. The session
that drew those markers loaded the skill and could not have known.

interactive-exhibit gains the chrome the phone changed -- the arrow
cluster and its portrait placement, the drawer label -- and two Plotly
rules read out of v2.35.2's own source rather than recalled: a scene
relayout must carry the live camera, because a 3D replot re-applies the
layout's stored copy and a touch rotation never updates it; and a hover
box keeps its pointer only when it fits to one side of its point.

safe-file-editing gains A Guard Must Not Fence What a Generator
Rewrites. Three chained ledger patches refused this session: each was
fingerprinted against the previous one's raw output, while every one of
them told Tony to run ledger_index.py next -- which rewrites the zone
they were hashing. ledger_index.py now holds LF on write, as
skills_index.py already did one file away.

THREE BUMPS IN ONE ENTRY IS NOT A VIOLATION OF ONE SESSION, ONE BUMP.
That rule is per SKILL: a session does not ship two versions of one
skill. Three different skills ride one protocol entry, as two did at
v3.55 and v3.56.

These bumps are taken at the session's close rather than before its
builds, which v3.55 recorded as the better order. The builds they
describe had already happened; taking them now is what makes them
available to the NEXT session. So the obligation travels as usual: this
session loaded 1.7, 1.1 and 1.10, and a reinstall cannot be verified
from inside the session that made it. The next session confirms its
loaded copies read 1.8, 1.2 and 1.11 before doing marker, exhibit or
patch work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.54 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-16 when v3.60
made a fourth entry.)

v3.58 (September 14, 2026): No rule changed in this document. ONE
skill bump, taken as the session's FIRST action, ahead of the build it
serves.

provenance-discipline 2.11 -> 2.12 (L-326). Five rules from the L-321
cross-check round, and one that L-325 parked for this bump.

THE ROUND THAT EARNED THEM SURVIVED BECAUSE ITS LEGS FAILED
DIFFERENTLY, and that is the entry's one idea. Four checkers took the
same three worksheets on Earth's magnetosphere. One had the discipline
and marked three belt-extent rows UNSOURCED, where three open
full-text sources state those figures. One found the sources and lost
every URL in the clipboard. One could not fetch at all and said so
plainly. One found the thing nobody else did and misnamed two of the
three others. No single leg would have got there, and that was luck
rather than design.

Each rule is the shape of one of those failures. A Negative Verdict
Shows Its Search [CRITICAL], because UNSOURCED is the only verdict
pointing at no document anybody can open, so a DISCOVERY row carries
its search log. A Source Names What Was Opened, Not What It Cites
[CRITICAL], because the right URL under the wrong author name is
invisible without a second fetch. A Link Is an Object, Not Text
[QUALITY], with the file the checker exported kept as the record
rather than the paste. Two roster corrections: Gemini's fetching is
TIER-dependent, so L-276's constraint is about the interface and the
tier rather than the vendor, and a checker inside this Project is not
independent for a rerun, because past chats are searchable. And Route
the Effort Tier by Job Type [QUALITY], Tony's ruling of 2026-09-13.

A DERIVED ROW STORES THE FIGURE ITS SOURCES SUPPORT [CRITICAL] is the
sixth, and it is not from the round. It is L-325's Gap, parked on
2026-09-12 on the rule that a skill bump cannot be verified from
inside the session that makes it.

ONE ADDITION THE DRAFT DID NOT ASK FOR, recorded because a later
reader will find it and wonder. The draft's first and fifth notes both
use "DISCOVERY row" as established vocabulary. It was not: the term
was defined in the L-321 worksheet prompt and never travelled into the
skill. So Worksheet Types also gains the [CITATION] / [DISCOVERY]
definitions and the ten-column schema the three worksheets actually
ran, transcribed from the prompt rather than composed. This is v3.57's
lesson in a second store: A CONVENTION THAT IS NOT IN THE SKILL DOES
NOT TRAVEL.

THE ORDERING IS v3.55's, and this is the second entry to use it. The
bump is taken before the build it serves -- L-305 item 7, the citation
job on Earth's belt scalars -- so the stale-skill gate fires on a
matching manifest instead of on a promise carried in a handoff. The
2026-09-13 handoff made it the next session's first action for exactly
that reason, and declined to take it in the session that drafted it,
because a rushed edit to a CRITICAL skill is how a bad rule ships.
That gap earned its keep: the draft's third note was false when
written and was falsified four hours later in the same session.

The obligation still travels, because reinstalling is not something a
session can check on itself. This session loaded 2.11; the next
session confirms its loaded copy reads 2.12 before provenance work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.55 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-16 when v3.61
made a fourth entry.)

v3.59 (September 14, 2026): ONE RULE REWRITTEN, the Register Rule, on
Tony's instruction of the same evening. No skill bumped.

WHAT THE OLD WORDING GOT WRONG. It opened "plain speech is the default"
and then gave the compressed voice a home in this document and in the
skills. Read together, those two sentences describe a shared shorthand
that simply belongs in a different place. Tony's correction: it is not
shared. He cannot read it and Claude can, so it is a channel with one
party on it.

THE ASYMMETRY IS NOW THE RULE'S REASON rather than a footnote to it.
Claude holds the whole session at once and unpacks a compressed phrase
without effort. Tony is living through the session and cannot, and
noticing that a sentence is too dense already costs him the reading.
Compression is therefore free on one side and expensive on the other,
which is why every earlier version of this rule decayed: nothing in
writing a compressed sentence tells the writer it failed.

SUMMARIES ARE NAMED as where it fails, because that is where it failed
on 2026-09-14. A closing list of decisions names each one rather than
stating it, and a list of names is compressed prose wearing bullet
points. The evening produced four of those before Tony said so.

The three checks, the two supporting defaults and the backstop are
unchanged. What changed is the opening, which is the part that has to
carry the rule when a session is moving.

The header stamp and the SHA anchor move with this entry.

Version history: v3.56 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-19 when v3.62
made a fourth entry.)

v3.60 (September 16, 2026): No rule changed in this document. TWO
skill bumps, taken as the session's first action, ahead of the build
they serve.

interactive-exhibit 1.2 -> 1.3 (L-332) and orrery-coding-conventions
1.8 -> 1.9 (L-331).

THE EXHIBIT SKILL WAS FIVE ROUNDS STALE. Version 1.2 was cut on
2026-09-11 and described the rooms' chrome as L-316 round 2 and L-318
rounds 1 and 2 left it. Six more rounds ran on Tony's phone on
2026-09-15/16, each checked before the next was built, and the skill
that fires on any edit to that chrome did not know any of them: the
arrow cross's corner is now one CSS rule; a drawer row has a finger-
sized target and GO ticks an unticked shell; a break inside a sentence
is soft; the portrait phone's text box has no arrow and sits mid-view;
and a phone tap reaches a marker through a second Plotly rule read from
v2.35.2's pick pass. The skill also gains the hover budget suite in its
pre-test step, with the note that the suite does not build the Sun
room -- which is how four Sun hovers missed the move to the i panel
(L-331). A checker passes on what it does not look at.

THE ONE NEW RULE IS TONY'S, and it rides both skills. On 2026-09-16,
reading the Sun room's Galactic Tide hover -- "DECLARED --" at the top,
"Not a measurement." at the bottom -- he said that declared-not-
measured means little to a visitor, and then made it general: "In
general we should avoid compressed language in the hovertext." That is
this document's Register Rule pointed the other way: the Register Rule
governs what Claude writes to Tony; this governs what the plot says to
a visitor, who has been through none of the conversation. It is written
into interactive-exhibit for the gallery's hovers and into
orrery-coding-conventions for the orrery's, because the orrery's hovers
are where it reaches next (L-321), and a convention that is not in the
skill a hover session loads does not travel. The rule changes the
words, not the facts or the caveats; reworded hovers go to Tony first.

THE ORDERING IS v3.55's: the bumps precede L-331's build, so the next
exhibit session's stale-skill gate fires on a matching manifest. The
obligation still travels: this session loaded 1.2 and 1.8, and a
reinstall cannot be verified from inside the session that makes it. The
next session confirms its loaded copies read 1.3 and 1.9 before exhibit
or hover work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.57 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-19 when v3.63
made a fourth entry.)

v3.61 (September 16, 2026): No rule changed in this document. ONE
skill bump, taken ahead of the store work it serves.

provenance-discipline 2.12 -> 2.13 (L-335). L-322 (d), significant
figures, is ruled, and one ruling of four days earlier is withdrawn.

THE PROCEDURE IS THE TEXTBOOK ONE, written down once. Tony asked for
standard methods and named the reference. The skill now says: the
figure count is a declared field, "# Figures:", beside every value, the
way the unit is; a literal is counted by the standard rules; a derived
row keeps the fewest figures of its measured inputs for a product or
quotient and the coarsest decimal place for a sum or difference, with
exact and declared numbers never limiting the result; the arithmetic
runs from the primary inputs at full precision and rounds ONCE, half to
even; and the export is where that rounding happens, carrying the count
beside the value so the gallery formats without guessing.

THE RULING WITHDRAWN IS L-325's, that a derived row stores a rounded
literal so a test can announce when an input moves. Tony withdrew it in
the same message that adopted the procedure, because a rounded literal
at rest is a rounded intermediate for every row that chains from it.
The objection that earned the ruling, sixteen digits copied into a
gallery config, is now answered at the export rather than at rest. The
skill keeps a stub where the rule stood, so a reader who meets the two
literal rows knows why they look the way they do.

WHAT MADE IT URGENT was measured, not recalled. The store holds 27
derived rows and the checker could see 2 of them, because it found
derived rows by a word on a Status line that 25 rows do not carry. It
ran green this session on the 2. The skill also disagreed with itself:
one section said a derived row stays an expression and the withdrawn
one said it stores a literal, and 21 rows followed the first while 2
followed the second. Rule 8 has the checker enumerate by the
"# Derived:" line and name every row it cannot judge.

ONE ADDITION BEYOND THE EIGHT RULES. The new section says the figure
field works "like # Unit:", and the skill had never defined "# Unit:";
L-322 ruling 1 lived only in the ledger. The Status Line gains The Unit
Field. A convention that is not in the skill does not travel -- v3.57's
lesson, a third time.

THE ORDERING IS v3.55's: the bump precedes the Earth-slice walk that
writes the field. The obligation travels: this session loaded 2.12, and
a reinstall cannot be verified from inside the session that makes it.
The next session confirms its loaded copy reads 2.13 before provenance
or store work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.58 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-19 when v3.64
made a fourth entry.)

v3.62 (September 19, 2026): No rule changed in this document. TWO skill
bumps, taken after the build they record rather than before it, which is
the exception to v3.55's ordering and is stated here so it is not read as
a precedent: these rules were LEARNED in the build, and there was nothing
to write before it ran.

interactive-exhibit 1.3 -> 1.4 (L-334) and gallery-cache-builder
1.4 -> 1.5 (L-336, L-216).

WHAT THE EXHIBIT SKILL GAINS is what a room opens on and who may write
the file it is read from. The arrival block is served rather than coded,
and it is the one part of a room's data the page reads directly, so a
change to it reaches a visitor on the push while a change to a shell's
words waits for the cache builder. Every trace belonging to a served
shell now carries that shell's key, and a trace that loses its stamp is
DRAWN rather than hidden, which is why that rule is CRITICAL and why a
check reads every trace the renderers build. Two tools write the served
config and each has an ALLOW list rather than a refusal list. And Tony's
ruling of 2026-09-18 is in it: logic that needs no browser lives in its
own file, his reason -- the size of interactive.html -- first, and the
testability reason second.

WHAT THE BUILDER SKILL GAINS was true long before anyone wrote it down.
A CONFIG CHANGE IS NOT DEPLOYED UNTIL THE CACHE IS REBUILT, and the two
are committed together. On 2026-09-17 the config went out ahead of the
cache and both rooms broke on the live site -- the Sun showing 9 drawer
rows instead of 18 -- while eleven checks passed, because every one of
them read the config or a fixture and none read the file the browser
fetches. The same bump corrects this skill's own claim that the failed
folder swap was "one data point": there have been three, and the
exposure is established rather than unlucky.

THE OBLIGATION TRAVELS, as it always does. This session loaded 1.3 and
1.4, and a reinstall cannot be verified from inside the session that
makes it. The next session confirms its loaded copies read 1.4 and 1.5
before exhibit or cache work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.59 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-20 when
v3.65 made a fourth entry.)

v3.63 (September 19, 2026): No rule changed in this document. ONE
skill bump, taken ahead of the walk it serves, which is v3.55's
ordering.

provenance-discipline 2.13 -> 2.14 (L-322). The READ is written down.

IT HAD BEEN A RULING SINCE 2026-09-11 AND LIVED ONLY IN THE LEDGER.
L-322 ruling (b) said a bare literal's check is a human reading the
source against it, "where critical", and the skill that fires on every
constants session did not carry any of it. This is the same lesson as
v3.57 and v3.61: a convention that is not in the skill does not travel,
and the field the walk is about to write has to be defined before the
walk writes it.

WHAT "CRITICAL" MEANS IS TONY'S, AND IT IS ABOUT ACCESS. Asked on
2026-09-19 what the word meant, he said it is "where your own search
tools cannot read a needed source but I can", and glossed "need" in the
same message: a number is in the store and needs a source. So the split
is not by importance. An unimportant number behind a wall only Tony can
open still goes to him; a load-bearing number Claude can open never
does. Three branches follow -- the builder reads what it can open and
names itself on the row, a row only Tony can open goes to him in a FILE
with the link, where to look and the number to expect, and a source
neither can open fails The Access Standard and is re-homed or removed.
His reading list is his WHOLE share: nothing else in a slice walk asks
him to read a source.

A MODEL'S READ COUNTS, AND THE LINE SAYS SO. Tony confirmed this
directly rather than leaving it to be inferred: the model may read a
source. The fourteen magnetosphere rows already work that way. What
does NOT count is a read reconstructed from training, because the line
then stops the next reader from looking while recording nothing that
was checked -- a `# Source:` over recalled data, one layer out.

THE WORDING WAS APPROVED BEFORE IT WAS CUT. It is his ruling being
written down, so the section was brought to him in full and he answered
four questions about it point by point. Three smaller things ride the
same bump: The Unit Field now points at `constants_tokens.py`, which
owns the token table, the retired list and the "named number" marker;
Rule 8's enumeration names both routes to a derived row, its arithmetic
and its `# Derived:` line, which are not the same set; and the
worksheet schema gains the "Read by" column promised on 2026-09-11 and
missed by 2.13.

THE OBLIGATION TRAVELS, as it always does. This session loaded 2.13,
and a reinstall cannot be verified from inside the session that makes
it. The next session confirms its loaded copy reads 2.14 before any
provenance or store work, and that session is Stage C, the walk itself.

The header stamp and the SHA anchor move with this entry.

Version history: v3.60 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-21 when
v3.66 made a fourth entry.)

v3.64 (September 19, 2026): No rule changed in this document. ONE
skill bump, taken after a review found a rule being decided in the
wrong place.

provenance-discipline 2.14 -> 2.15 (L-342). THE FIGURE RULES ARE
REPAIRED AGAINST THE SOURCE THEY CITE.

WHAT WENT WRONG IS INSTRUCTIVE AND IS NOT A COUNTING ERROR. L-322's
Earth walk met PREM's `3480.0` and had to decide whether that trailing
zero counted. The skill's Rule 2 said it did, full stop. The walk
decided it did not, wrote a reason into that one constant's comment
line -- that a zero in a padded decimal place is the table's formatting
-- and moved on. Both were wrong, and the page the skill cites settles
it: a trailing zero after a decimal point counts WHEN IT FALLS WITHIN
THE SOURCE'S REPORTING RESOLUTION. Rule 2 had dropped four words, which
made it wrong for the page's own example of 1500 m; the walk's
replacement was wrong the other way and, worse, was settled inside a
comment where it read as fact and would have been followed without
being noticed. That is the second failure direction Method Belongs to
the Skill names, and this is what it looks like in practice.

RULE 3 GAINS A SENTENCE IT NEVER HAD: a row may declare fewer figures
than its inputs support when the relation ITSELF is approximate, with
the reason in words on the row. Counting governs how precision flows
through arithmetic and says nothing about a formula that is an
idealisation to begin with. Earth's Hill sphere declared seven figures
by counting and told the reader in its own next sentence to report
three, and the gallery, which formats from the declared count, showed a
visitor 234.6388 Earth radii.

THE ASTM REFERENCE IS DEMOTED TO AN ASIDE, on Tony's ruling. E29 costs
$86, so a rule this project works from could not be opened by anybody
in the loop -- the skill-layer form of a citation nobody read, and a
failure of our own Access Standard. Its scope is conformance with
specification limits, which this store does not have. The reference is
now the open page alone, so every rule can be checked against it by
anybody. Asked whether to adopt the standard verbatim instead of
restating it, the answer is that verbatim would not have helped: what
failed was that nobody could check the restatement against its source
without opening the source.

THE OBLIGATION TRAVELS, as it always does. This session loaded 2.14,
and a reinstall cannot be verified from inside the session that makes
it. The next session confirms its loaded copy reads 2.15 before any
provenance or store work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.61 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-22 when
v3.67 made a fourth entry.)

v3.65 (September 20, 2026): No rule changed in this document. ONE
skill bump, taken AFTER the build it records, which is v3.62's
exception rather than v3.55's ordering: three of these rules were
learned while the build ran and there was nothing to write before it.

gallery-cache-builder 1.5 -> 1.6 (L-216). THE CACHE SWAP STOPS
DEPENDING ON TONY NOTICING.

WHAT LANDED, in the gallery at `a1a516cf`. Each rename inside the swap
is retried for about fifty seconds. A swap that still cannot finish
renames the previous generation back, so the working copy is never left
without a served cache and GitHub Desktop never shows the pile of
deletions. And every run that reaches the swap writes one line to
`data/cache_swap_log.jsonl`, a tracked file OUTSIDE the generation --
which L-216 has said since 2026-08-19 must come first, because a run
whose swap fails strands its own record where `.gitignore` hides it.
The offline suite went from 167 checks to 190, and each of the three
pieces was removed on purpose to confirm the matching checks go red by
name.

THE COUNT IS FIVE, and the two ends of the list are the argument. The
first occurrence, 2026-07-24, was a SCHEDULED run: nobody knew a build
was in flight, the mass deletion was read as routine cleanup, and it
was committed and pushed before being reverted. The human check did not
merely risk failing; it failed once. The last two, both on 2026-09-20,
happened with OneDrive syncing PAUSED, so pausing is not the cure it
looked like. Tony's words are in L-216: "catching the failures depended
on me stopping with the malformed commit lists, but the fix was not
obvious."

TWO RULES IN THE SKILL CAME FROM MISTAKES MADE DURING THE BUILD, and
both are the same shape. A patch script called plain `shutil.rmtree` on
the cache tree and was refused by the read-only attribute OneDrive sets
-- the exact failure `_rmtree_force` was written for, in a docstring
the session had read an hour earlier. And the build manifest described
a folder by a COUNT, "42 published files that serve nothing", written
by an author who had not opened them; they were the only copy of 38
days of run history. Knowledge that lives only inside a function does
not fire, and a count does not say what is there. Both now live in the
skill.

THE MOVE OFF ONEDRIVE IS NOT DECIDED and is not to be pressed. Tony
ruled "do option 1 and take it from there as needed" on 2026-09-20; the
analysis he asked to have recorded, including what a move would need
first, is written into L-216.

THE OBLIGATION TRAVELS, as it always does. This session loaded 1.5, and
a reinstall cannot be verified from inside the session that makes it.
The next session confirms its loaded copy reads 1.6 before cache work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.62 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-23 when
v3.68 made a fourth entry.)

v3.66 (September 21, 2026): No rule changed in this document. ONE
skill bump, taken ahead of the build it serves, which is v3.55's
ordering.

provenance-discipline 2.15 -> 2.16 (L-322). HOW A STATED UNCERTAINTY
DECIDES A FIGURE COUNT IS WRITTEN DOWN.

THE RULE WAS ALREADY THERE, AND IT WAS NOT APPLIED. Rule 3 said a
stated uncertainty decides and counting is the fallback, and the
procedure it was adopted from says to propagate. The C2 design session
missed both and put a choice to Tony between counting digits and two
uncertainty conventions. His answer was "See the Skill on significant
digits." It was method, which Method Belongs to the Skill had already
said. What the skill lacked was HOW -- which uncertainty, how to
propagate it, how to report it, and when it applies -- and the
checker counts only, so the C2 build implements the new text.

THE WORKED CASE. Shue's five coefficient uncertainties propagate to
+/- 0.13 Earth radii at the declared solar wind, which the reference
page's single-number rule reports to tenths: 10.3, where the store had
carried 10.25. In kilometres the same uncertainty supports two
figures, 65,000 km. Two more of Tony's corrections the same day shaped
the design around it: compute with all the digits and round only at
the end, which is Rule 4, and "The single source of truth is
constants_new.py", which put the kilometre and AU figures in the store
rather than in the page.

WHAT IS OURS IS MARKED AS OURS. The page says to report so that the
implied range is close to the measured one. That closeness is measured
on a log scale is this project's choice, and it is written apart from
the page's words with its reason -- 2.14 went wrong by restating a
source with words changed and nobody able to see it.

TWO REVIEWS BEFORE THE CUT. Claude Fable 5.1 reviewed the text in the
C2 manifest twice. The first review found that the propagated figure
is the fit's precision and not the magnetopause's -- real crossings
scatter 1.23 Earth radii -- which became the show-or-cap sentence and,
on Tony's ruling, a scatter line in each hover. The second found that
an earlier form of the ceiling rule would have failed fifteen finished
C1 rows; the rule now fails a row only for claiming more than its
uncertainty supports, and measured over every derived Earth row, none
does.

THE OBLIGATION TRAVELS, as it always does. This session loaded 2.15,
and a reinstall cannot be verified from inside the session that makes
it. The next session confirms its loaded copy reads 2.16 before any
provenance or store work, and that session is the C2 build, from
documentation/BUILD_MANIFEST_L322_C2_magnetosphere_20260920.md.

The header stamp and the SHA anchor move with this entry.

Version history: v3.63 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-25 when
v3.69 made a fourth entry.)

v3.67 (September 22, 2026): No rule changed in this document. ONE
skill bump, the second taken ahead of the C2 build, which is v3.55's
ordering applied twice to one build.

provenance-discipline 2.16 -> 2.17 (L-322). A DISPLAY NEVER CHOOSES A
COUNT, AND THREE STORAGE FORMS ARE WRITTEN DOWN.

THE QUESTION THAT STARTED IT WAS TONY'S. Asked whether Earth's dipole
tilt should print 9.4 or 9.4105, the reviewing session offered a
readability call. Tony, 2026-09-21: "when it comes to a decision,
what is the basis? the basis should be in the skill not arbitrary."
There was none. Rule 7 let a display show fewer figures and said
nothing about when, so every use of it reached the integrator, which
is the failure Method Belongs to the Skill names. Rule 7 is replaced
whole: a display prints the declared count; a number that reads as
too many figures is a finding about the row, fixed under Rule 3 where
it is recorded, never by the page. That takes item 9 -- the
geocorona, LEO's inner edge, the outer belt -- off Tony's decision
list, because each resolves on its row.

THE TILT WAS THE WORKED CASE, AND IT WAS WRONG IN THE STORE. IGRF-13
prints no tilt; it prints the three degree-1 coefficients and says the
pole is computed from them. The stored 9.6 is in no epoch of the
cited source, and the row's drift rate was off by a factor of ten.
Three forms are now in the skill. A whole the source defines from
parts it prints is a derived row over rows for the parts, never a
typed result with its working in a comment. A rate is the derivative
expression, never a difference of two evaluations, because the
difference form takes its count from the largest inputs and not from
the quantities the rate rests on. An angle computed from a pure
number multiplies by the exact row DEG_PER_RAD instead of calling
degrees, because the unit check sees a bare number and refuses the
call -- found only when Opus ran the unit checker on the tilt, which
nobody had done, including the session that had said the checkers
accepted everything the tilt needed.

THE OUTER BELT TAUGHT THE DECLARED CONSTRUCTION. Its peak is typed
4.5 with its L = 4 to 5 band in prose, which When the source gives a
range already did not allow. Making it an expression over two
one-figure band rows met three rules at once: Rule 2 says a declared
pick is exact, the checker counts an expression from its measured
inputs, and the export rounds to the count -- and measured, that
exported 4.0 for the gallery while the orrery drew 4.5 from the
float, two consumers drawing two rings. Rule 2 now names a declared
construction: exact as a rule, accepted by the checker only on a row
whose status begins declared, served unrounded so every consumer
draws the same value, and shown to the visitor as the range and the
rule rather than as a measurement.

EACH ROUND WAS TESTED BEFORE THE NEXT. Five documents on 2026-09-21,
by Claude Fable 5.1 and Claude Opus 5 with one round reviewed by GPT
6, and each one's proposals were run through the figures walker, the
unit checker and the export on a throwaway copy of the store before
the next was written. Three of Fable's own proposals failed those
runs and were corrected in the next revision: a row that was at once
an expression over measured rows and exact, a rate counted at two
figures where the sum inside it carries three, and a function the
checkers do not know. The reach of the new Rule 7 was enumerated
before it was adopted, as The Braid requires: the gallery's Earth
room gains no failure, and the orrery's Earth hovers carry 47 format
sites on 35 lines, named by line in the rev2 addendum, of which four
come into C2 and the rest are one ledger class with no automated
coverage, stated as such so a closed slice is not read as covering
them.

THE OBLIGATION TRAVELS, as it always does. The session that cut this
bump had 2.15 mounted, the protocol in its context having refreshed
to 2.16 mid-session, which is the note owed to Stale Skill = Stop
since the C2 manifest; it worked from the repo copy at 1f6e55a9 and
said so. The next session confirms its loaded copy reads 2.17 before
any provenance or store work, and that session is the C2 build, from
documentation/BUILD_MANIFEST_L322_C2_magnetosphere_20260920.md with
its section 17.

The header stamp and the SHA anchor move with this entry.

Version history: v3.64 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-27 when
v3.70 made a fourth entry.)

v3.68 (September 23, 2026): No rule changed in this document. ONE
skill bump, taken ahead of the build it serves, which is v3.55's
ordering.

provenance-discipline 2.17 -> 2.18 (L-322). WHERE A DRAWING NUMBER
LIVES, AND HOW AN EXACT NUMBER PRINTS.

THREE KINDS OF DRAWING NUMBER ARE TONY'S RULING. A physical value, such
as a size, an edge or a cut angle, lives in constants_new.py, sourced
or declared. A value chosen by eye does not promote, and is replaced as
the braid reaches it, published rooms first. A rendering setting, such
as opacity, point count, colour, marker or font, stays in the drawing
code. Tony, 2026-09-22: "these are defined in the code not in
constants new." The skill had contradicted itself on this for two
versions, one section keeping opacity and point count in the drawing
code and another listing them as stored. The test between the kinds is
whether changing the number moves where something is drawn. Earth's
belt thickness was the case that needed it: it looks like a setting,
it moves where the rings sit, and with no source it is replaced by the
belts' served edges.

THE EXACT ROW CAME FROM A QUESTION NOBODY COULD ANSWER. The Stage D
manifest asked how many figures Earth's obliquity should print. It is
exact, because Horizons defines its ecliptic frame by it, and Rule 7
said nothing about exact rows. Measured, the gallery printed every
exact row by a width chosen at each call site. Claude Fable 5.1's
answer: store a definition in the form it is printed, 84381.448
arcseconds, and print its own digits. Claude Opus 5.5 added the print
count as a field on the row, because a Python literal cannot tell a
meant trailing zero from a typing habit: counted from the literal, a
floor chosen as 200 km would print as 200.0.

THE CONVERSION ROW CAME FROM A CHECK THAT PASSED WHILE WRONG. Fable
ran the unit checker on the draft rotation-period row, written with a
bare divide-by-3600, and it failed: the checker converts units by
itself and found 0.0066 hours against 23.93 stored. The figures checker
passed the same row, so one checker alone looked green. A conversion is
now an exact row with its own unit.

THE MIDPOINT BECAME THE DEFAULT ON TONY'S READING. Asked where the
magnetotail's flare should end inside its sourced 100 to 120 Earth
radii, Tony said he thought the midpoint was already the skill's rule.
It was the practice in every case and not written anywhere. It is
written now: the midpoint, unless the row states a reason for an end.

THE OBLIGATION TRAVELS, as it always does. This session loaded 2.17,
and a reinstall cannot be verified from inside the session that makes
it. The next session confirms its loaded copy reads 2.18 before any
provenance or constants_new.py work, and that session is the Stage D
build, from documentation/BUILD_MANIFEST_L322_D_earth_pole_20260922.md
revision 2, with Fable's review filed beside it.

The header stamp and the SHA anchor move with this entry.

Version history: v3.65 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-28 when
v3.71 made a fourth entry.)

v3.69 (September 25, 2026): No rule changed in this document. ONE
skill bump, taken ahead of the build that will next read the rule it
touches.

provenance-discipline 2.18 -> 2.19 (L-322). A WORKED EXAMPLE THAT HAD
GONE STALE IS REPLACED.

WHAT WAS WRONG. Rule 7's exact row gave Earth's obliquity as its
example: it "prints 23.439291 degrees". That was written on the
morning of 2026-09-23. Later that day the Stage D manifest's revision 3
changed the axis hover to print the tilt of date, worked out from the
pole Horizons serves, and D6 and D7 built it. Since then no display
prints the obliquity; its row is only the angle that defines the
ecliptic frame. The example described a hover that no longer exists.

HOW IT WAS FOUND. Two handoffs carried it as a ledger class, the
second without re-checking it. Tony asked what "stale" meant, and then
two questions: were the consumers of the obliquity using a correct
number, and should the skill change now so it is not forgotten. The
consumers were checked in the orrery, in the export and in the
gallery's served cache: all carry 23.439291111 degrees, and all use it
to turn equatorial directions into Horizons' ecliptic frame, never as
Earth's tilt and never printed. Nothing on screen was wrong.

THE NEW EXAMPLE is the gallery's magnetopause hover, which prints the
exact row EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG today with a width chosen at
its call site, the thing the rule forbids. The obliquity stays in the
text as the case of an exact row no display prints, which carries no
print count.

WHY NOW. Tony: update it now so it is not forgotten. The next two
Stage D sessions both reach this rule: gallery patch 3 edits the Earth
room's hovers, where the cut angle is printed, and manifest section 6
builds the print-count field itself. A stale example in a skill that
loads every session is followed without being noticed.

THE OBLIGATION TRAVELS, as it always does. This session loaded 2.18,
and a reinstall cannot be verified from inside the session that makes
it. The next session confirms its loaded copy reads 2.19 before any
provenance or constants_new.py work, and that session is gallery patch
3, from documentation/HANDOFF_L322_D_orrery_magnetosphere_built_20260925.md.

The header stamp and the SHA anchor move with this entry.

Version history: v3.66 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-28 when
v3.72 made a fourth entry.)

v3.70 (September 27, 2026): No rule changed in this document. ONE
skill bump, provenance-discipline 2.19 -> 2.20 (L-322). WHERE A
TRAILING ".0" COMES FROM IS WRITTEN DOWN.

WHAT PROMPTED IT. The session that opened the Stage D print-count
build, manifest section 6, settled the print counts of the seven
printed exact rows from what each row's own comment says it was chosen
with: the declared solar wind pressure prints "2 nPa" because Shue's
paper uses 2 nPa, not "2.0". Tony confirmed that, and asked that the
claim behind it be checked and put in the skill: that the trailing
zero in a value like 2.0 comes from Python, not from significant
figures.

WHAT THE CHECK FOUND. Checked by running Python 3 and Node. The claim
holds, by three routes rather than one. Python needs a decimal point to
make a number a float, so rows are typed 200.0, and the stored float
keeps no record of how it was typed. Python's division always returns
a float, so 4 / 2 is 2.0. And a float printed without a format,
including by json.dumps into constants_export.json, always shows ".0".
The gallery's "2.0 nPa" turned out to be a fourth case: the page's own
toFixed(1), applied to a value JavaScript had read as plain 2.

WHAT THE SKILL NOW SAYS. Rule 2 gains one paragraph naming the three
routes and what follows from them: a row's figure count is never read
from its literal, its printed form or its exported form, which is why
the count and an exact row's print count are both fields. A choice
that really was made to a trailing zero says so on its # Declared:
line.

RULE 7'S EXACT ROW MATCHES THE CODE THAT BUILDS IT, orrery patch D15,
built the same session. The print count is read only directly after
"exact --". A declared construction prints the digits of the value its
rule gives, so the outer belt's midpoint of 4 and 5 prints 4.5. The
checker refuses a count with more digits than the number has, one too
small to write it in full, and anything but 1 on a zero. And
exact_rows_report.py --check fails the maintenance run while a printed
exact row is not printed by its count. The second refusal and the
declared construction's count were Claude's additions while building
D15; Tony approved both on 2026-09-27, on the condition that the code,
the provenance rules and the significant-figure rules all agree.

THE OBLIGATION TRAVELS, as it always does. This session loaded 2.19,
and a reinstall cannot be verified from inside the session that makes
it. The next session confirms its loaded copy reads 2.20 before any
provenance or constants_new.py work. That session is gallery patch 4,
the gallery half of section 6.

The header stamp and the SHA anchor move with this entry.

Version history: v3.67 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-28 when
v3.73 made a fourth entry.)

v3.71 (September 28, 2026): No rule changed in this document. ONE
skill bump, provenance-discipline 2.20 -> 2.21 (L-322). A SUM SCALED
BY AN EXACT NUMBER KEEPS ITS DECIMAL PLACE.

WHAT PROMPTED IT. Settling the Sun room's chromosphere hover, which
printed its radius as 1.002874802357338 solar radii. The top of the
chromosphere is the Sun's radius, 695,700 km, exact by the IAU's
definition, plus a depth Carroll & Ostlie give as about 2,000 km, one
figure. The sum is good to thousands of kilometres, 698,000 km. Divided
by the exact solar radius, the counting rule as written gave 1.00:
three figures, an implied error of about 3,500 km on a 2,000 km layer.
Written the other way, 1 + 2,000 / 695,700, the same rule gave 1.003,
and the unit check forced the coarser form. And the export rounds each
row to its count, so at 1.00 the chromosphere would have been drawn on
the photosphere, erasing the 2,000 km hairline ruled on 2026-08-16.

WHAT THE SKILL NOW SAYS. Rule 3 gains one paragraph: a sum or
difference, scaled by an exact row, keeps its decimal place carried
through the scaling, not its figure count. 1,000 km is 0.0014 solar
radii, nearest the thousandths, so the chromosphere prints 1.003. The
reference page, Wikipedia's Significant figures, names this as the
unit-conversion exception to its multiplication guideline: 8 inches
becomes 20. cm, not 20 cm. A single measured value scaled by an exact
row is deliberately left under the fewest-figures rule for now. Rule 1
gains the form that carries it, the ceiling says a converted place is
not an implied uncertainty, and Rule 8 specifies the checker, which is
built with the chromosphere rows.

WHO DECIDED. Claude Fable 5.1 recommended the rule; Tony ruled for it
on 2026-09-28. Claude Opus 5.5 checked the reference and the numbers
the same day and added the scope sentence, which Tony confirmed.

THE OBLIGATION TRAVELS. This bump was written in Fable's session and
lands from this one, which had already shipped 2.20. The next session
confirms its loaded copy reads 2.21 before any provenance or
constants_new.py work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.68 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-30 when
v3.74 made a fourth entry.)

v3.72 (September 28, 2026): No rule changed in this document. TWO
skill bumps, one version each, for one ruling (L-345):
provenance-discipline 2.21 -> 2.22 and interactive-exhibit 1.4 -> 1.5.
A VALUE IN ANOTHER UNIT IS COMPUTED, NEVER STORED.

WHAT PROMPTED IT. Planning the Sun room's chromosphere hover. Served
from its own kilometre row, the kilometre line would read 698,000 km,
but the page works out the AU by dividing the kilometre figure it is
served, and the served figure is already rounded: 0.00467 AU, where
the full digits give 0.00466. That was ledger item L-345's open
question -- a second row per unit, or the export doing the
conversion. And constants_new.py already held 13 rows that were
another row in a different unit, each stating its own precision a
second time.

TONY'S RULING, 2026-09-28: "follow the single source of truth
principle. use the single best source for the store with provenance.
compute all conversions instead of duplicating. we should build this
architecture now. add to the skill if clarification is needed." Then,
on the count rule, after Claude Fable 5.1's review: "confirmed as
recommended", as the skill's method rather than his judgment.

WHAT THE SKILLS NOW SAY. provenance-discipline Rule 3 gains the rule
and replaces 2.21's "for now" sentence: each quantity is one row, in
the unit its best source gives it; its value in any other unit is
worked out from the row's full digits and rounded once, and its count
comes from the source row alone -- the source's uncertainty scaled by
the exact factor, then the Report test's place. The chromosphere
keeps 1.003 solar radii and 0.00466 AU; the bow shock's 13.5 Earth
radii becomes 86,000 km, two figures, because its last figure is
worth 638 km. Rule 8's checker paragraph is widened to match.
interactive-exhibit gains one rule: a hover prints a unit it is
served and never converts a served number to print it.

ONE WORDING CORRECTION to Fable's text, recorded in the skill. It said
"the power of ten nearest that scaled uncertainty"; its own worked
numbers and the Report test it names compare the uncertainty with
half a unit in each place. Read literally, the bow shock's AU would
have kept three figures, against the ruling's own table.

THE BUILD. Orrery patch D19 carries the mechanism with these bumps:
constants_rows.conversions() and the export's "in" field, schema 6,
with test_constants_export.py re-computing every served conversion
and holding eight worked cases. D20 retires the 13 conversion rows;
one gallery patch then prints from "in".

THE OBLIGATION TRAVELS. This session loaded 2.21 and 1.4. The next
session confirms its loaded copies read provenance-discipline 2.22 and
interactive-exhibit 1.5 before any provenance, constants_new.py or
exhibit work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.69 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-10-01 when
v3.75 made a fourth entry.)

v3.73 (September 28, 2026): No rule changed in this document. TWO
skill bumps, one version each, for one design build (L-345, patch
D20): ledger-and-session-records 1.11 -> 1.12 and interactive-exhibit
1.5 -> 1.6.

WHAT PROMPTED IT. Patch D20 finished L-345: the fifteen rows in
constants_new.py that were another row in a different unit became
names computed from that row, marked "# Conversion: of <ROW>", with no
count, status or source of their own, and test_derived_figures.py now
names any row shaped like a conversion that is not marked. It was
shown failing on the real store before it was trusted. The same patch
moved the orrery's crust to Earth's mean radius, in the words Tony
approved on 2026-09-28, and restamped the master plan to v34.

LEDGER-AND-SESSION-RECORDS 1.12, The Document Stack. The master plan
is ONE document at two zooms: an executive summary at the top, and the
body, with the critical path kept inside it as Section 5a. The summary
is rewritten at every restamp. Tony's ruling of 2026-09-28: "i think we
should integrate these reports. the summary as an executive summary.
the body should keep its critical path section." The two companion
files had not moved since August while the plan went from v21 to v33
(L-333, L-362); they are retired as dated records.

INTERACTIVE-EXHIBIT 1.6, three rules under Provenance is part of the
build, each describing what the L-345 gallery patch built. Where
cutting a served AU to three figures would round a tie, the served
digits print in full and the hover check names the case (Tony's ruling
of 2026-09-28; the inner core's 0.000008165 AU). The mirror writes a
slot measured in another unit from its row's "in". And a shell may
serve a radius_note, a sentence under its radius line, as the crust
does.

THE OBLIGATION TRAVELS. This session loaded 1.11 and 1.5. The next
session confirms its loaded copies read ledger-and-session-records
1.12 and interactive-exhibit 1.6 before any ledger, handoff or exhibit
work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.70 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-10-01 when
v3.76 made a fourth entry.)

v3.74 (September 30, 2026): No rule changed in this document. ONE
skill bump, ledger-and-session-records 1.12 -> 1.13 (L-396). TONY'S
PAGE: WHERE WE ARE.

WHAT PROMPTED IT. Tony, 2026-09-30: "i struggle to keep the big
picture. it's the old dilemma of loosing the forest for the trees."
The master plan's summary and critical path had been tried for that
and had not really helped: both are written for the work, and both
move only at design builds. He asked for one running document he can
read at the end of every turn and every session, practical both to
write and to read. Then he asked for the parts changed this session
and the immediate next steps to be marked, because "attention is a
human limitation", and for bullets in place of paragraphs.

WHAT THE SKILL NOW SAYS. The Document Stack gains Where We Are:
documentation/WHERE_WE_ARE.md, one file rewritten in place and
updated inside every session's ledger patch. It has a fixed shape: a
Read This First box, the road from start to goal, right now, the next
three steps, and what waits on Tony. This session's changes are
marked, the must-reads are in italics, and the marks are cleared at
each update. And a turn that changes the picture ends with two or
three bullets under "Where this leaves us". Nothing checks the page
yet; the candidate check is recorded on L-396.

THE SAME SESSION (2026-09-29 and 30) brought three strands of work
together and recorded Tony's order of work: the Solar System room's
second half first, then the Sun's numbers, then the room becomes the
website's home page. After that, the orrery's other objects come to
the website from its own object list, checked against JPL Horizons
(L-363, L-395; master plan v35).

THE OBLIGATION TRAVELS. This session loaded 1.12. The next session
confirms its loaded copy reads 1.13 before any ledger, handoff or
session-record work -- which every session does at its end.

The header stamp and the SHA anchor move with this entry.

Version history: v3.71 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-10-02 when
v3.77 made a fourth entry.)

v3.75 (October 1, 2026): No rule changed in this document. TWO
skill bumps, one version each, for one build (L-398):
provenance-discipline 2.22 -> 2.23 and interactive-exhibit 1.6 -> 1.7.
A COMPUTED DISTANCE PRINTS WHAT ITS ERRORS EARN.

WHAT PROMPTED IT. Tony's question on 2026-10-01 about the Solar System
room: "does Horizons serve the distance to pluto with 9 significant
digits?" It did not. The room's figures came from how closely the page
reproduces Horizons, not from how well JPL knows where the planet is,
and Pluto printed ten figures where JPL's own report says several
thousand kilometres.

WHAT THE SKILLS NOW SAY. provenance-discipline gains A Computed
Position Prints What Its Errors Earn: a distance worked out at display
time prints to the Report test's place for the LARGER of the measured
drift and the source's own accuracy (Tony: "use whichever is larger").
Its second half is the case the source forced: an accuracy stated only
in words is stored as the place those words report to, the place the
Report test gives for every value the words can mean, the coarser where
they could mean two, and never as a number the source does not print.
JPL's 2014 report gives 1 km, 100 km and 10,000 km for its three groups.
interactive-exhibit records the rooms section of objects_config.json
and the words a drawer row may carry, the "position_accuracy" link
and Tony's sentence for a body with none, and the second file moved
out of interactive.html.

ONE PLACE COARSER THAN THE PLAN. The session plan said the place the
words name, thousands for "several thousand". Every value those words
allow reports to ten-thousands, so that is what the rule gives. Tony
confirmed it as recommended on 2026-10-01.

THE BUILD. Orrery patch patch_L398_1 adds the three rows to
constants_new.py; gallery patch patch_L398_2 links nine bodies to them
and prints by them, with a new gating check.

THE OBLIGATION TRAVELS. This session loaded 2.22 and 1.6. The next
session confirms its loaded copies read provenance-discipline 2.23 and
interactive-exhibit 1.7 before any provenance, constants_new.py or
exhibit work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.72 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-10-02 when
v3.78 made a fourth entry.)

v3.76 (October 1, 2026): No rule changed in this document. TWO
skill bumps, one version each, for one build (L-395):
provenance-discipline 2.23 -> 2.24 and interactive-exhibit 1.7 -> 1.8.
THE ORRERY'S OBJECT LIST FEEDS THE WEBSITE.

WHAT PROMPTED IT. The Solar System room's info panel had no description
and no NASA link, and the website's object facts were typed by hand
from the orrery's list. Tony's rulings of 2026-10-01: the website keeps
copies written by a tool and checked (the constants pattern); each
served entry gains a 'key' spelled as the website's slug; one
description and one link per object, cleaned in the orrery; and
"simple errors such as the Apophis naming discrepancy should be fixed
and reported."

WHAT THE SKILLS NOW SAY. provenance-discipline gains A Simple Error a
Check Finds Is Fixed and Reported: what counts as simple, that the fix
rides the same patch and is named, what comes to Tony instead, how a
number in a served description is sourced or removed, and how this
sits beside The Braid. interactive-exhibit records that a body's name,
Horizons id, description and link on the website are copies written by
tools/mirror_objects.py, and what the room's panel shows.

THE BUILD. Orrery patch_L395_1 adds the key, export_objects.py and its
check; gallery patch_L395_2 adds the pull, the mirror and its suite,
and the panel's words and link.

THE OBLIGATION TRAVELS. This session loaded 2.23 and 1.7. The next
session confirms its loaded copies read provenance-discipline 2.24 and
interactive-exhibit 1.8 before any provenance or exhibit work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.73 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-10-02 when
v3.79 made a fourth entry.)

v3.77 (October 2, 2026): No rule changed in this document. TWO
skill bumps, one version each, for one session (L-405):
interactive-exhibit 1.8 -> 1.9 and ledger-and-session-records 1.13 ->
1.14. THE SKILLS CATCH UP WITH THE SESSION'S TWO BUILDS.

WHAT PROMPTED IT. The session made the Exhibit Store Editor list every
room (L-404) and built the Solar System room's drawer (L-363 step 3b).
Tony then asked to sort what the session did into method already in
the skills, method that needed a skill, and drawing decisions and
judgement -- and, the review done, to "take care of the skills now and
the numbers in the next session."

WHAT THE SKILLS NOW SAY. interactive-exhibit corrects its sentence that
every reader of objects_config.json ignores the "rooms" section; says
what the store writer may change in a room that is not one body, and
that the editor lists rooms from both places a room can live; records
the Solar System room's drawer as the shared drawer with four
additions, and Tony's framing ruling of 2026-10-02 -- where each body
is now, plus 20%; and gives step 4 the headless test recipe, now filed
in the gallery's tools/headless/. ledger-and-session-records gains A
Wrong Sentence in a Skill: Bump Now, or Carry It. The test is what a
session would do if it followed the sentence: something wrong means
correct it now, nothing different means carry it on the ledger to the
next version.

JUDGEMENT KEPT OUT OF THE SKILLS. Five calls Claude made inside the
drawer build were put to Tony as his, and he confirmed them. They are
recorded as his rulings on L-363, not written as method.

THE OBLIGATION TRAVELS. This session loaded 1.8 and 1.13. The next
session confirms its loaded copies read interactive-exhibit 1.9 and
ledger-and-session-records 1.14 before any exhibit, ledger, handoff or
session-record work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.74 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-10-04 when
v3.80 made a fourth entry.)

v3.78 (October 2, 2026): No rule changed in this document. ONE
skill bump, one version (L-406): interactive-exhibit 1.9 -> 1.10.
THE GALACTIC TIDE IS DRAWN IN THE GALAXY'S PLANE.

WHAT PROMPTED IT. Sorting the Sun room's 43 unlinked numbers (L-371)
found the galactic tide's words saying its bodies are thinned near the
galaxy's plane while the drawing thinned them near the ecliptic. Tony's
ruling of 2026-10-02: fix it now, as a drawing choice made more
correct. The source then showed the pattern was wrong too: comets the
tide sends in avoid the galaxy's plane AND its poles. Tony confirmed
drawing both, and drawing the tide between the outer Oort cloud's two
stored edges instead of a typed 50,000 AU.

WHAT THE SKILL NOW SAYS. Asked whether the skills cover how a feature's
hover, info panel and drawing are written, the answer was that the
hover and the drawing were covered and the info link was not: Tony's
rule lived only on L-265. interactive-exhibit 1.10 writes it down -- a
NASA page where one is specific to the feature, otherwise English
Wikipedia, the corona the one named exception.

THE BUILD. Orrery patch_L406_1 adds the galactic pole of J2000 to
constants_new.py, gives the pole matrix its own function, and redraws
the orrery's tide; gallery patch_L406_2 redraws the website's tide in
Tony's approved words and corrects the check that measured the
ecliptic under the galactic plane's name.

THE OBLIGATION TRAVELS. This session loaded 1.9. The next session
confirms its loaded copy reads interactive-exhibit 1.10 before any
exhibit work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.75 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-10-05 when
v3.81 made a fourth entry.)

v3.79 (October 2, 2026): No rule changed in this document. TWO
skill bumps, one version each (L-407): earth-system-pipeline 1.1 ->
1.2 and provenance-discipline 2.24 -> 2.25. A SKILL'S HEADER IS READ
AS YAML.

WHAT PROMPTED IT. Settings refused interactive-exhibit 1.10 with
"malformed YAML frontmatter": patch_L406_1 had put new fires_when words
on a line of their own; patch_L406_3, pushed at 81e19ef, put them back
on one line, still 1.10. skills_index.py had read the same header by its
own looser rules and built the manifest without complaint, and as a
generator its exit code did not count, so the maintenance run passed 19
of 19 on a skill that could not be installed. Tony's word, 2026-10-02:
do L-407 now.

WHAT CHANGED. skills_index.py reads every header as YAML, with PyYAML
where installed and built-in rules otherwise, names which, and fails on
a header YAML refuses, one with no name or description as text, or a
value YAML silently cuts short at " #". orrery_maintenance_run.py runs
it with --check as the checker Skill headers. The check found two more:
earth-system-pipeline's description held ": ", which YAML refuses; and
provenance-discipline's held "# Source:", so YAML read only its first
200 characters, and the installed skill has been chosen by that cut
description. Both descriptions are now quoted. No rule in any skill
changed.

THE OBLIGATION TRAVELS. This session loaded interactive-exhibit 1.9,
earth-system-pipeline 1.1 and provenance-discipline 2.24. The next
session confirms its loaded copies read 1.10, 1.2 and 2.25, and that
provenance-discipline's description no longer ends at "adding or
reviewing".

The header stamp and the SHA anchor move with this entry.

Version history: v3.76 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-10-05 when
v3.82 made a fourth entry.)

v3.80 (October 4, 2026): No rule changed in this document. ONE
skill bump, one version (L-415): safe-file-editing 1.11 -> 1.12. A
PATCH WRITES LF AND SAYS SO.

WHAT PROMPTED IT. A ledger patch's test notes said a CRLF copy of the
ledger kept its CRLF. Tony: "why do we leave windows line endings
uncorrected. I thought the rule was to convert to lf when found and
report." The skill said both: Fix In Passing lists CRLF as a violation
to fix, while Line Endings Are Not Content and Compare Content, Not
Bytes said to write each file back in the style found, because
flipping the endings shows every line changed.

WHAT THE TEST SHOWED. Under `* text=auto eol=lf`, which both repos
carry, that reason is false: a CRLF working copy shows as modified with
nothing inside it, and writing it LF clears the mark. The reason holds
only for a file committed CRLF before the rule existed; 22 such files
remain, named on L-133.

WHAT THE SKILL NOW SAYS. A patch writes LF and reports a file that
arrived CRLF. A file committed CRLF keeps its endings, is named, and
waits for L-133's one-commit sweep. Patches and generators now follow
the same convention.

THE OBLIGATION TRAVELS. This session loaded 1.11. The next session
confirms its loaded copy reads safe-file-editing 1.12 before any patch
work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.77 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-10-06 when
v3.83 made a fourth entry.)

v3.81 (October 5, 2026): No rule changed in this document. SIX
skill bumps, one version each (L-418): provenance-discipline 2.25 ->
2.26, interactive-exhibit 1.10 -> 1.11, safe-file-editing 1.12 ->
1.13, orrery-coding-conventions 1.9 -> 1.10,
ledger-and-session-records 1.14 -> 1.15 and gallery-cache-builder 1.6
-> 1.7. A LONG SKILL OPENS WITH ITS CONTENTS.

WHAT PROMPTED IT. A Claude Sonnet 5.5 session checked the skills
against Anthropic's documented limits. All eleven pass the hard rules,
which skills_index.py --check now enforces (L-417). Five are over
Anthropic's 500-line guideline, provenance-discipline almost six times.
Measured here: a plain read of a file that long shows its start and its
end and leaves out the middle, and provenance-discipline's first 423
lines were version history, so a plain read showed the history and the
field notes and none of the rules. Tony asked whether a contents
section would help, and that the sections be arranged so more of them
are read whole; then that all five be done, and gallery-cache-builder
with them, which is under 500 lines but long enough to be cut the same
way.

WHAT CHANGED. Each of the six opens with a contents list of its
headings, and skills_index.py --check fails a skill over 500 lines that
has none, and any skill whose list and headings disagree. Version
history older than three entries moved, word for word, to
documentation/SKILL_HISTORIES.md. provenance-discipline's sections are
ordered critical, then quality, then untiered, then its two long
procedures, then the field notes; every section's text was checked
unchanged. One rule is new, in ledger-and-session-records: a skill
keeps three version entries, and a long skill keeps its contents list
true. No other skill's rules changed.

THE OBLIGATION TRAVELS. This session's loaded copies were the versions
before these. The next session confirms its loaded copies read
provenance-discipline 2.26, interactive-exhibit 1.11, safe-file-editing
1.13, orrery-coding-conventions 1.10, ledger-and-session-records 1.15
and gallery-cache-builder 1.7, and that each opens with its contents.

STILL OPEN. Moving provenance-discipline's two long procedures into
reference files loaded only when needed is recorded on L-418, not
scheduled.

The header stamp and the SHA anchor move with this entry.

Version history: v3.78 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-10-06 when
v3.84 made a fourth entry.)

v3.82 (October 5, 2026): No rule changed in this document. ONE
skill bump, one version (L-419): ledger-and-session-records 1.15 ->
1.16. A PATCH NEVER REFUSES TONY'S NOTES.

WHAT PROMPTED IT. The session's closing patch, patch_L413_3, guarded
documentation/WHERE_WE_ARE.md by a fingerprint of the whole file and
refused: Tony had marked two lines "-- done" and dated the header.
Tony: "i though annotations would not be refused." His rule of
2026-10-03 had said exactly that, but it lived only in one earlier
patch's code, so a later session did not have it. Asked whether it goes
into the skill now or later: "yes because I am using our handoffs or
the where we are as run records."

WHAT CHANGED. ledger-and-session-records, under Where We Are: a patch
checks Where We Are, a handoff or the ledger only at the lines it
edits, never by a whole-file fingerprint; a rewrite of Where We Are
first copies every line Tony changed into the session's handoff and
prints them. patch_L413_4 is the worked example. Its v1.13 entry moved
to documentation/SKILL_HISTORIES.md, by the three-entry rule.

THE OBLIGATION TRAVELS. A reinstall during a session is not visible to
that session. The next session confirms its loaded copy reads
ledger-and-session-records 1.16, along with the five other skills
v3.81 named.

The header stamp and the SHA anchor move with this entry.

Version history: v3.79 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-10-07 when
v3.85 made a fourth entry.)

v3.83 (October 6, 2026): No rule changed in this document. ONE
skill bump, one version (L-027): agentic-pre-test 1.2 -> 1.3. THE
PRE-TEST RUNS THE FILE AS IT IS.

WHAT PROMPTED IT. A session reported that the maintenance run's Reset
completeness check fails in the sandbox because it needs a screen
colour only Windows has. Tony: "We should not have any windows only
requirements. This is a cross platform project." The file history
showed it was a regression, not the starting state: Tony's commit of
2026-01-09 had replaced the Windows-only Tk colour name
SystemButtonFace with gray90, and commit ec333df of 2026-06-12 swapped
all 26 back -- the reverse of the pre-test's own colour swap, applied
to the real file. Since then the orrery's window could not open on
Linux, and every headless run passed because the test swapped the
colour out of its copy first.

WHAT CHANGED. patch_L027_1 names the colour once in palomas_orrery.py,
PANEL_BG = 'gray90', at all 23 sites. agentic-pre-test 1.3 drops the
swap: the headless run uses an unedited copy, and an error naming
something only one system has is a finding to fix, never to swap past.
Its throwaway rule keeps its place, with the founding case as the
history shows it. Tony, on the colour: "Confirmed as recommended. And
should we improve the skill also?"

THE OBLIGATION TRAVELS. A reinstall during a session is not visible to
that session. The next session confirms its loaded copy reads
agentic-pre-test 1.3 before any pre-test.

The header stamp and the SHA anchor move with this entry.

Version history: v3.80 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-10-08 when
v3.86 made a fourth entry.)

v3.84 (October 6, 2026): No rule changed in this document. ONE
skill bump, one version (L-421): interactive-exhibit 1.11 -> 1.12. A
FACT ABOUT A FEATURE IS SERVED, NOT TYPED.

WHAT PROMPTED IT. Building Earth's website patch, Claude told Tony the
skill already required the inner belt's word "protons" to be served.
It did not: it required served numbers, and let page text carry its
source in the page. Tony: "I thought the only source of truth is the
constants py and the objects list ... not from the code." Asked then
where the info panel's facts are stored, a search of both rooms found
17 facts typed in code. Tony ruled them part of finishing the Earth and
Sun slices, "the work is here", not backlog.

WHAT CHANGED. interactive-exhibit, under Provenance is part of the
build: code may type only sentences about the picture; a fact about
nature, about a paper, or a source is served on its feature's row and
printed as given. Its v1.9 entry moved to
documentation/SKILL_HISTORIES.md, by the three-entry rule. The 17 are
listed in documentation/MANIFEST_L421_typed_facts_20261006.md, for a
fresh session to build.

THE OBLIGATION TRAVELS. A reinstall during a session is not visible to
that session. The next session confirms its loaded copy reads
interactive-exhibit 1.12 before any exhibit work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.81 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-10-09 when
v3.87 made a fourth entry.)

v3.85 (October 7, 2026): No rule changed in this document. ONE
skill bump, one version (L-422): ledger-and-session-records 1.16 ->
1.17. TONY'S PAGE IS EDITED BY SECTION, AND ITS END IS HIS.

WHAT PROMPTED IT. The Fable 5.1 ledger sweep of October 4 to 7 read
Where We Are and found the same facts in four sections, and found that
a closing patch built before a parallel session had rewritten the page
whole and erased that session's lines. Tony then said how he uses the
page: "I use the where we are to record the run record and rename it
with a time stamp." His timestamped copies hold the patch output and
his verdict beside each test line -- the primary record of his rulings.

WHAT CHANGED. ledger-and-session-records, under Where We Are -- Tony's
page: each fact once, the READ THIS FIRST box is the page, Settled and
Signals added; a patch edits the page by section, never whole; the page
ends with a marker, and below it is Tony's run-record zone, which no
patch edits and which the close reads from his latest timestamped copy;
every ledger handle on the page carries a short label ("all ledger
L-xxx items should have a brief parenthetical label"); the check to
build is the date and a cap of 130 lines above the marker. Under Ledger
Block Format: an item inside an ordered list needs no RICE score, his
ruling of the same day (L-412). Under Where a File Goes: records go to
the orrery's documentation/, flat, no subfolders ("Subfolders are more
steps and also I scan the files to see what the recent changes were").
The skill's v1.14 entry moved to documentation/SKILL_HISTORIES.md, by
the three-entry rule. Where We Are itself was rewritten in the new
shape, this once, the page it replaced copied into the handoff.

THE OBLIGATION TRAVELS. A reinstall during a session is not visible to
that session. The next session confirms its loaded copy reads
ledger-and-session-records 1.17 before any ledger, handoff or
session-record work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.82 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-10-10 when
v3.88 made a fourth entry.)

v3.86 (October 8, 2026): No rule changed in this document. THREE
skills, one version each (L-418): provenance-discipline 2.26 -> 2.27,
the new skill provenance-cross-check 1.0, and
ledger-and-session-records 1.17 -> 1.18. PROVENANCE-DISCIPLINE IS
SPLIT, AND A LONG FILE CARRIES ITS READ PLAN.

WHAT PROMPTED IT. provenance-discipline was 137,837 characters in 2,590
lines, and one read of a file does not show that much. The design
session's viewer showed 16,000 characters, from the start and the end;
this session's reader showed the first 1,106 lines and said it had
stopped. So the skill that guards facts and sources was the one least
likely to be read whole. Tony ruled the split on 2026-10-06 ("Read and
confirmed"), and a trial skill showed on 2026-10-08 that an installed
skill keeps the extra files in its folder.

WHAT CHANGED. The relay procedure, the Review-Repair Protocol, is the
new skill provenance-cross-check, with its worksheet sections in a
reference file. provenance-discipline keeps its rules, with the
figure-count rules and the field notes in two reference files, each
opened when its pointer says. Every moved section is word for word
apart from the edits the patch lists, and the patch proves it. Riding
2.27: L-371 (the Sun room's served numbers), L-390 (the conversion
marker) and L-252 (the checker's fourth outcome). skills_index.py
writes a read plan into every file longer than one read, and its
--check fails on a part too long, a line no part covers, or a reference
file named and missing or present and never named.
ledger-and-session-records 1.18 records those two conventions and names
provenance-cross-check for review prompts. Four other long skills get
their read plans at their next version, by Tony's ruling of the same
day, and skills_index.py names them on every run. The manifest has a
twelfth row.

THE OBLIGATION TRAVELS. A reinstall during a session is not visible to
that session. The next session confirms its loaded copies read
provenance-discipline 2.27, provenance-cross-check 1.0 and
ledger-and-session-records 1.18; lists both skill folders and finds
their reference files; and, on its first figures task, says whether it
opened the figures reference file before writing a figure count.

The header stamp and the SHA anchor move with this entry.

Version history: v3.83 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-10-10 when
v3.89 made a fourth entry.)

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
