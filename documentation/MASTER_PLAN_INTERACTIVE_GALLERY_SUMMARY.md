Where we are 8/18/2026

Updated 2026-08-18 after the August 17-18 sessions. Built on
b65ac115fc0f820e8270c0807249813c67bde7bc at
https://github.com/tonylquintanilla/palomas_orrery (branch main);
gallery at ff18d3e6fa31f70a8f525df471e751d046cf14fa at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both confirmed by live check on the date above.

Where a claim was TRUE when written and has since been overtaken, it is
left in place with a bracketed note rather than deleted. This document
is a record of what was tracked on a date, and one that silently
rewrites its own past stops being evidence of anything.

Companion to MASTER_PLAN_INTERACTIVE_GALLERY.md. The plan is the
reference document; this is the readable snapshot.

Section 5a of the plan was rewritten on August 16 as the critical
path -- end goal, one-way pipeline, five segments, and a "you are
here" table. CRITICAL_PATH_SUMMARY.md is its readable companion and
answers "how far to the end." THIS document answers "what is being
tracked right now." Read 5a for the shape of the work; read this for
its state.


THE SHORT VERSION

The worksheet checker is built and running. It is one of the twelve
checkers in maintenance_run.py, so the reconciliation Tony wanted
continual rather than one-shot is continual. The request builder that
sends questions out is built too, and the key rule that binds a
returned row to the right claim.

What the checker reports is the number that organizes Track 1:
110 annotations scored, EIGHT clean. Forty-eight route to SEND BACK,
twenty to CONVERSATION, thirty-four are noted with no route, and
twenty-four are not scanner-reachable. That is not a discouraging
result. Before the checker existed the same claims were unexamined and
looked fine.

  [Read 2026-08-16 as: 102 scored, THREE clean, 40 SEND BACK, 19
  CONVERSATION, 40 noted. The corpus grew and the clean count nearly
  tripled between the 16th and the 18th, and neither is a change in
  the world -- L-198 taught the scanner units it could not read, so
  claims that were always there became visible and rows that had been
  mis-parsed resolved.]

The dispatch loop is FINISHED and unused. Fable 5 and GPT 5.6 Sol
reviewed it blind on August 16; both said do not send it yet, and
between them found nine structural blockers where two were known.
Eight are closed. The ninth -- the truncated ordinal context window --
is deliberately not exercised by the pilot, since constants carry no
ordinals.

The last inch closed on August 18. Until then a returned verdict could
be built, carried, filled, returned, checked and routed, and then
REFUSED when somebody wrote it back into the code, because the
annotation grammar accepted only a markdown reference (L-204). Found by
an integration test, not by reading the code.

The chromosphere stylization is retired. The shell now draws at true
physical scale, 1.002875 solar radii, and the fact that it reads as a
hairline welded to the photosphere is the lesson rather than a defect.
That decision closed one of the nine blockers by removing the question
instead of answering it.

  [2026-08-16 read: "The next session opens with the builder-side
  marker join. Ninety-six continuation markers were placed in seven
  files on August 16 and the builder does not yet know they exist, so
  the largest blocker -- 45 of 65 dispatch rows showing a truncated
  citation -- is still live." DONE, L-196. The builder joins 153
  continuations on every build and refuses to build at all when a
  citation continues onto an unmarked line.]

What opens the next session is the DISPATCH. The request is one file,
reader-agnostic, 23 rows over constants_new.py, with every row's
expected disposition written down before it goes out
(PILOT_EXPECTED_DISPOSITIONS_20260817.md: 13 clear, 10 return, three
trap rows). If all 23 come back clear, that is agreement rather than
success, and the prediction file is what makes the difference
visible.


WHAT CLAUDE CHECKS BEFORE ANYTHING ELSE

Recorded here on Tony's instruction, 2026-08-16, so the two of us
track the same list. These fire at session start, unprompted, and a
session that skips them is building on an unverified base.

  1. SHA round trip, both repos. A live remote read of HEAD for the
     orrery and the gallery, compared against what the handoff says
     was pushed. A matching HEAD confirms commit and push in one
     unforgeable check. A mismatch is reconciled BEFORE any build.

  2. Skill version check. Every skill Claude loads has its version
     line compared against the manifest row in PROJECT_INSTRUCTIONS.md.
     If they disagree, the session STOPS and asks Tony to push the
     current SKILL.md to skills/ and reinstall it in Settings.

     Two limits worth Tony knowing. The check is LOAD-triggered, so a
     skill bumped later in the same session produces a mismatch with
     nothing left to fire on. And a mid-session reinstall cannot be
     verified from inside the session -- the loaded copy appears bound
     at conversation start. So a mid-session bump is NOT cleared in
     session. It is written into the handoff as an obligation the next
     session discharges.

     CURRENTLY OUTSTANDING: provenance-discipline went 2.3 -> 2.4 on
     August 18. The session that bumped it loaded 2.3. The next
     session must confirm its loaded copy reads 2.4 before any
     provenance work.

     [The August 16 obligation -- safe-file-editing and
     orrery-coding-conventions at 1.3 -> 1.4 -- was discharged
     2026-08-17. All ten skills were compared loaded-against-repo on
     August 18 and only provenance-discipline differs.]

  3. Uploads enumerated. Some uploaded files arrive as readable text
     and others sit only on disk. The split is invisible from Tony's
     side. Claude lists the directory and reads the whole set before
     claiming to have reviewed anything.

  4. Ledger read. Open items, Tony comments and Gap notes, before
     proposing work.

  5. Handoff obligations discharged. Anything the previous session
     wrote down as unverifiable at the time.

What Tony can do with this list: push before a session starts so HEAD
is current, and keep the three skill stores in sync (repo skills/,
Settings, then skills_index.py) so the version gate has nothing to
catch.


THE FIVE RULINGS THAT CHANGE THE PLAN

Fetch-and-import is RATIFIED. Section 7, decision 12, moves from
RECOMMENDED to ratified. Each night the builder asks GitHub for the
orrery's current commit, downloads constants_new.py at that exact
commit, imports it, reads the feature values and their sources, and
writes them into the served cache. Two conditions attach. Because
importing a Python file executes its top-level code, a pre-import gate
checks the file's structure before it runs. And the fallback when GitHub
is unreachable must be OBSERVED at build time, not accepted on a
reviewer's word: it falls back to the last committed copy and never
writes empty features.

A registry entry has three zones. MEASURED fields are published values
and carry a source. DECLARED fields are developer style choices --
colors, opacity -- and are expected to have no source. DERIVED display
text is not stored at all; it is assembled from the other two.

A measured field carries value, unit, and source. Not a bare number with
the unit baked into the key name. Tony's reasoning: published values
arrive in mixed units anyway, so a conversion step is needed regardless.
Storage stays heterogeneous and conversion happens where the text is
built. This deleted an earlier recommendation for a per-feature unit
convention.

Display text is assembled on the BUILDER side, not in the browser.
Section 7, decision 17. Tony's reasoning: it is the only arrangement in
which the orrery and the assembler cannot drift apart. The accepted cost
is that the cache holds finished sentences, so rewording requires a
rebuild.

Migration runs structure first, Jupiter first. Section 7, decision 16.
Jupiter's served data is complete and correct today, so the transport
has something real to be tested against. Then Artifact 2's remaining
values are cross-checked into the proven structure, then the rest of the
migration, then whatever surfaces gets resolved.


THE REGISTRY SHAPE, IN PLAIN TERMS

Here is a ring entry as it exists today, before migration:

  'main_ring': {
      'inner_radius_km': 122500,      # sourced
      'outer_radius_km': 129000,      # sourced
      'thickness_km': 30,             # sourced
      'color': 'rgb(180, 120, 100)',  # developer choice
      'opacity': 0.7,                 # developer choice
      'name': 'Main Ring',
      'description': "...122,500 km to 129,000 km...about 30-300 km..."
  }

Three properties of the migrated form are settled.

Everything measured must sit at MODULE SCOPE -- readable without
executing anything. This is what makes L-181 a PRECONDITION for L-190
rather than more work for it. A value buried inside a drawing function
cannot be walked by a static pass over the code, which is exactly why
the scanner cannot see belt_distances today.

There is ONE not-yet-sourced state, not two. Tony's correction: the
orrery is the source, so if the orrery does not offer a value there is
nothing to render and no field to fill. A not-yet-sourced field is a
value that IS rendered but has no recorded provenance. It must be
distinguishable from absent, and it is never an empty field.

Derived text is not stored. CHROMOSPHERE_RADIUS_LINE is the working
precedent: two values stored in different units -- solar radii and
kilometres -- feeding one sentence that emits solar radii, AU and
kilometres.

One question stays open and is better answered with Jupiter in front of
you than in the abstract: should EVERY measured field be range-capable?
The evidence that it might: Jupiter's main ring description says the
thickness is about 30 to 300 km, while thickness_km says 30. The prose
is more accurate than the data it sits beside.


THE SCHEDULED NIGHTLY IS RETIRED

Tony's ruling, August 10. The builder now runs manually and he commits
it himself. The Windows task is DISABLED, not deleted, so the corrected
configuration survives if this is ever revisited.

His reasoning: "It can't run without my machine being on anyway and it's
consistent with me being the only commit authority. And obviates
complicated fail safe procedures that could also fail."

The first clause is the decisive one. The schedule created an appearance
of automation the setup could not deliver -- three nights were missed
this week and the failure was silent. A manual run is honest about what
it is. It also dissolves the surprise behind the August 10 gallery
incident: if Tony starts the build himself, he knows a build is in
flight and cannot walk into the swap window unaware.

What this does NOT dissolve is the cadence question, which changes shape
rather than going away. "Did the nightly run?" becomes "when did I last
run it?" Something still has to tell Tony the served data is eleven days
old. That is L-189, and the retirement makes it more load-bearing, not
less, because a manual build has no expected time at all.

A pre-commit hook refusing a deletion-only commit under
data/solar-system/ was designed before this ruling and is NOT BUILT
deliberately. It becomes relevant again if the schedule returns, if a
second person gains commit access to the gallery repo, or if the builder
ever runs unattended in any other form.


WHAT SHIPPED, AUGUST 10

L-186's mechanical half. The August 2 Gemini worksheet was recovered by
Tony and filed at documentation/worksheets/worksheet_gemini_constants_remaining.md.
Eight annotations in constants_new.py that named no file now point at
it, and three appended values were stripped -- two in eris, one in
venus. Cross-check annotation issues fell from 12 to 6. All six
remaining are duplicate_identity, and they need a look at each source
rather than a patch.

One shadow constant closed. orbit_data_manager.py held a local
KM_TO_AU = 1.0 / 149597870.7 duplicating KM_PER_AU, and now imports the
real one. The value is bit-identical and the patched module was
runtime-import tested with astroquery and astropy present, not merely
compiled.


A PROVENANCE FAILURE WORTH KEEPING

Claude took Tony's uploaded Gemini worksheet, rewrote it to house style
-- LaTeX converted, escaping stripped, a header and a provenance note
added -- and filed the result as the Gemini worksheet. Tony caught it:
"you have created a parallel unsourced worksheet not made by gemini."

The rule that came out of it: an evidence artifact is filed as received.
ASCII rules and naming conventions apply to code and to documents we
author. They do not apply to a document whose entire value is that
someone else wrote it.

A second, subtler failure sits alongside it. The August 7 instance,
asked whether it had fabricated the (Gemini worksheet) annotation, gave
an accurate account of its method -- it had pattern-matched an adjacent
line without checking -- and then concluded the CONTENT was fabricated
and offered to strip it. The recovered worksheet proves all three
specifics it believed it invented were true. Acting on that self-report
would have deleted a real citation. Unverified and true is still
unverified: the method was wrong, the content was not. An
over-confession is as much a calibration failure as a denial, and it is
more persuasive.


THE TRANSPORT, AND WHY IMPORT RATHER THAN PARSE

Horizons can answer "where is Saturn tonight." It cannot answer "how
wide is Saturn's B ring." The first is a computed position, fetched
fresh every night. The second is a published measurement living in
orrery Python, and only the first has ever had a pipeline. Confirmed
live: the 2026-08-06 nightly refreshed vectors, elements and positions
and touched neither objects_config.json nor feature_configs.json. Every
freshness signal read green and no feature value moved, because nothing
in that pipeline can move one.

What Tony does under the new design: nothing. Edit a constant, commit,
push -- the workflow he has today.

Importing rather than parsing matters because the store derives rather
than hardcodes. SOLAR_RADIUS_AU is computed from SUN_RADIUS_KM and
KM_PER_AU; CENTER_BODY_RADII maps body names to other named constants.
Six of forty-nine top-level assignments work this way, and that is the
store's stated principle, not a defect. Anything reading the file
without running it would have to reimplement arithmetic Python already
does. (Measured at HEAD.)

This does not violate the builder's no-orrery-imports rule.
constants_new.py is a leaf -- numpy and datetime, nothing else. No
Plotly, no shell modules. That is precisely why the old exporter could
not carry these values: reading shell configs drags Plotly along, and
reading the constants store does not.


BUILD REQUIREMENTS CARRIED FORWARD FROM THE FABLE ROUNDS

Four validation layers, each catching a different error class:

  1. Source presence -- an ABORT, not a warning. A physics value with no
     source stops the build.
  2. Unit-sanity RANGE checking. Shape validation and source-presence
     validation both PASS on a value whose units silently changed. Only
     magnitude bounds catch a km-to-AU slip.
  3. Cross-field ring invariant, inner <= outer.
  4. Nightly value-diff against last night's committed copy, logging
     old, new, and both orrery commit IDs. The only guard that sees
     CHANGE itself, which is the L-182 failure family.

On layer 3, a correction to Fable worth keeping: Fable recommended
strict inner < outer and said it catches nothing spurious. Verified
against the store, it fires on eight Neptune entries where inner and
outer are deliberately equal -- narrow ringlets modelled at a single
radius. Its directional claim holds; inner > outer is genuinely zero
across all thirty-three ring pairs. A check that fires spuriously on day
one is one people learn to ignore.

Three build requirements from round 2 remain live. Drop the dead imports
from constants_new.py -- numpy has been imported since April 5 2025 with
zero uses across all forty-six commits. Add a pre-import gate of roughly
ten lines checking two structural properties before the file runs: that
every import is on an allowlist, and that no dictionary has a duplicate
key. That second check is the one capability fetch-and-import otherwise
loses, because after import Python has already silently kept the last
duplicate. And define one name -- FEATURE_REGISTRY -- that the builder
reads and nothing else, so renames inside the store stay internal.

Round 1's findings still stand as scope: spectral_subclass_temps is an
uncited physical claim inside the store itself; KNOWN_ORBITAL_PERIODS
carries 'Phobos' twice; and the module-level *_info tooltip strings are
a FIFTH restatement surface, where Uranus restates 25,559 km nine times
and does arithmetic in prose.

A methodological note worth carrying. The design got SMALLER three
times, each time Tony asked a plain question and a premise turned out to
be false -- that the exporter was live, that derived constants were a
defect, that the gallery could not execute the file. The elaboration was
compensating for unexamined assumptions, not for real complexity.


OPEN DECISIONS FOR TONY, IN ORDER OF NEED

  (decide) Migration shape and per-body sequence beyond Jupiter. L-181.
           Order is settled; the detail is better decided with Jupiter's
           ring entries in view.

  (decide) Saturn thickness_km. Absent from the served cache -- but is
           it absent from the ORRERY? If the orrery draws Saturn's rings
           with a thickness, the number exists in code and the gap is
           transport, not data. One look at the file settles it.

  (decide) The constructor-call count in decision 12. It says two
           assignments contain constructor calls. Measured: one,
           HORIZONS_MAX_DATE. Staleness explains a count going up, not
           down, so this one needs a look rather than a correction.


TRACK 0 STEP ONE IS DONE -- L-179 AND L-180 CLOSED

Ruled and shipped August 7. Tony ruled 150,000 AU, the midpoint of the
published 100,000-200,000 AU range, and 1.1 solar radii as the DRAWN
chromosphere shell with the physical extent of roughly 2,000 km stated
beside it.

Both closed by DERIVATION rather than replacement, which is why this
doubles as the first exercise of the Track 0 authoring pattern. Ranges
are stored as data; the light-year figure derives from constants already
in the store; one shared fragment per fact feeds every display site. No
displayed number is typed any more.

The geometry was never wrong -- the shells have drawn at the correct
radii since August 2. Only the words had drifted, across four
restatements, with every offline test passing throughout. That is
L-181's thesis in miniature.

What it did NOT exercise, stated plainly so nobody reads it as a
transport test: no fetch across the repo boundary, no pre-import gate,
no FEATURE_REGISTRY, no validation layers, no builder. It rehearsed the
authoring side only. Jupiter is still the pilot.

One live note carried forward: GRAVITATIONAL_INFLUENCE_RANGE_AU is a
tuple, and tuples become JSON lists under fetch-and-import. The
serialization boundary should handle that deliberately rather than
discover it.


SCANNER STATE

Two runs on August 10, twenty minutes apart, both reporting 880
findings. Underneath that identical total: shadow constants went 1 to 0,
one new file entered the scan, and orbit_data_manager.py changed shape.
Three real events, invisible in the summary line. This is the argument
for L-189 in one paragraph -- report the DELTA, not the total.

Measured at b65ac115 on August 18: 1025 findings across 128 files,
Tier 1 289, Tier 2 620, Tier 3 114, Tier 4 2.

  [August 7 at 1ba20c3: 879 findings across 117 files, Tier 1 206,
  Tier 2 583, Tier 3 88, Tier 4 2. Re-measured at 227f5b2 on August 16
  and UNCHANGED at 206 -- the chromosphere retirement and the
  continuation markers moved nothing, which was correct, since neither
  added nor removed a claim about the world.]

Tier 1 went 206 -> 289 in two days, and the paragraph above says that
should not happen. Both are right, and the reconciliation is the point
worth keeping: the POPULATION changed, not the world. L-198 taught the
scanner claim vocabulary it did not have -- per-body radii, spelled-out
kilometres, units separated from their number by an intervening word --
so claims that had always been in the code became visible and
countable. A scanner that sees more is not a codebase that got worse.
Read 289 against 206 as coverage, not regression.

  Tier 1 by domain, at b65ac115

    Earth System                150
    Orrery                      125
    Stars                        12
    Utilities                     2
    Dev Tools                     0
    Gallery                       0

Why the other tiers are not the target. Tier 2 is already adjudicated --
cited constants, staleness flags on verified strings, and known scanner
limitations, all documented as accepted residuals; info_dictionary.py
alone holds 119 as multi-line-string false positives. Tiers 3 and 4 are
low priority by construction, and 36 of Tier 3 sit in audit and
diagnostic scripts that never render anything.

The push gate for this phase is Tier-1 = 0 ON THE INTERACTIVE BUILD
PATH, not the global figure. The global gate was unreachable in
practice, since 105 of the 206 sit in a subsystem Artifact 2 never
touches, and a gate nobody can reach stops working as a gate.


THE ARTIFACT-2 PATH, PER FILE

  shell_configs.py                      35
  idealized_orbits.py                   29
  planet_visualization_utilities.py      4
  saturn_visualization_shells.py         1
  uranus_visualization_shells.py         1
  orrery_rendering.py                    1
  jupiter_visualization_shells.py        0
  neptune_visualization_shells.py        0
                                        --
                                        71

  [August 16: 23, 26, and a total of 56. The two that moved are the
  L-198 vocabulary effect again, not new debt.]

Two things follow, both good news. The gas giant shells are already
nearly clean -- two Tier-1 findings across all four files -- so Batch 2's
job on them is VALUE VERIFICATION, not Tier-1 clearance, and Artifact 2
is not blocked by scanner debt in the shells themselves. And the
critical path is tractable: fifty-six findings across eight named files.


LEDGER ITEMS BY TRACK

  Track 0     L-181  Complete the constant layer -- the Track 0 build
              L-179  Solar gravitational influence  DONE
              L-180  Solar chromosphere  ON RECORD, DORMANT -- the
                     stylization it governed is retired, so it governs
                     nothing. NOT categorically superseded; a future
                     stylization anywhere would revive it.
              L-176  Illustrated dimensions in shell hover text

  Track 1     L-186  Cross-check annotation issues  DONE
              L-192  Worksheet checker  BUILT and running as one of
                     the maintenance checkers. Request builder built.
                     Key rule built. DISPATCH machinery now complete;
                     eight of nine blockers closed, the ninth
                     deliberately unexercised by the pilot.
              L-196  Citation continuations: mark, join, refuse  DONE
              L-197  Maintenance runner output: say what passed  DONE
              L-198  Claim vocabulary: the units the scanner could
                     not see  DONE -- and the reason Tier 1 moved
                     206 -> 289
              L-200  The Resolved leg -- record a verdict that
                     landed  DONE
              L-201  Request selection -- ask the builder for fewer
                     rows  DONE; also a dashboard card
              L-202  JSON worksheet format, markdown as fallback  DONE
              L-203  The visibility convention, now in the skill  DONE
              L-204  The worksheet reference may be JSON  DONE -- the
                     last inch of the loop
              L-205  The runner's verdict lines carry evidence  DONE
              L-193  Worksheet corpus reconciliation
              L-194  Text-only assertions (no number in the claim)
                     DEFERRED, blocking nothing
              L-195  Citation legs -- authority not in the # Source:
                     line. Six of 65 dispatch rows. Shape A ruled,
                     swaps NOT built.
              L-196  Chromosphere retirement, continuation markers,
                     key retirement record  DONE
              L-177  Mercury Hill sphere convention
              L-184  Interactive build-path push gate

  Track 2     L-154  JS feature-rendering layer -- does not exist yet.
                     Now precisely diagnosed: resolver.py:133 reduces a
                     feature dict to its keys, models.py:91 types the
                     field to match, and no code in the gallery repo
                     reads feature_configs.json at all. Two lines and a
                     type, then the renderers.

  Tooling     L-188  Maintenance runner -- one command, the whole
                     suite  DONE
              L-189  Provenance scanner: run history and run-to-run
                     delta  DONE
              L-190  Scanner reach: anything rendered must be reachable
              L-191  Display-text duplication across the shell modules

  Independent L-185  Source discipline for assembler constants
              L-187  info_dictionary numeric-overlap enumeration
              L-183  Stars skill scope
              L-124  Systematic color-accuracy pass, low priority

Two items still need handles. The second L-190 class -- claims about the
codebase that no tooling checks -- and a record of the scheduled-build
retirement, which changes how the serving pipeline operates and
therefore belongs in the ledger and in the gallery-cache-builder skill.


CORRECTIONS TO CARRY

Counts that are wrong in one or more documents, recorded here so they
are fixed once rather than argued twice.

The tooltip count is 124, not 126. The raw grep returns 126, but two
matches are documentation -- a module docstring and a comment. The real
key definitions are 83 in SHELL_CONFIGS plus 41 in CUSTOM_SHELLS. Two
live sites in the ledger carry 126, one of which contradicts its own
83-plus-41 breakdown in the same bullet. (Corrected 2026-08-11: this
note said two; there were three. A fourth sits inside a completed-batch
historical record and is correctly left alone -- correcting it would
falsify the record.)

Top-level assignments in constants_new.py are 49 with 6 derived, not 45
with 7.

Jupiter's registry entry count is SETTLED at four, confirmed at 253bcdd
on August 15. Jupiter 4, Saturn 7, Uranus 11, Neptune 11, total 33 --
matching L-181's enumeration. The five came from counting
inner_radius_km including the line that reads the key.

Eighteen inline literals still duplicate cited constants -- KM_PER_AU at
14 sites in 8 files, MOON_RADIUS_KM at 3 in 2, SUN_RADIUS_KM at 2 in 1.
Same violation as the shadow constant, but written inline inside
f-strings rather than as named assignments, so the scanner sees one of
nineteen.


ALREADY RESOLVED

L-178 (Earth LEO/GEO band geometry) and L-182 (Mars Hill sphere) both
closed August 5, Mode 5 confirmed. L-162 (CENTER_BODY_RADII naming)
done. Artifact 1 (Earth) built and Mode-5 accepted, golden fingerprint
locked. L-179 and L-180 closed August 7. L-186's mechanical half and one
shadow constant closed August 10.

Protocol at v3.41 (August 18) -- a records restructure and a skill
bump, no rule changed. The version history left the protocol document
for documentation/PROJECT_INSTRUCTIONS_HISTORY.md, which is
LESSONS_ARCHIVE.md renamed and now carries both records; the ledger's
appendix became a pointer; three entries stay resident and a fourth
pushes the oldest down. The header gained an anchor and lost a
contradiction -- the repo copy read August 16 and the copy installed in
the Claude UI read August 17 under the same version.
provenance-discipline is at v2.4.

  [August 16 read: protocol at v3.40, provenance-discipline at v2.3.
  v3.40's own entry records two skill bumps and the two bad deliveries
  that preceded the good ones -- safe-file-editing 1.4 adding Fix In
  Passing, Report It and the patch-script naming convention, and
  orrery-coding-conventions 1.4 adding Marker Separation for
  Near-Equal Radii and Harvest the Conventions You Find. v3.36's
  Register Rule amendment, v3.37's "The Artifact Bounds the Audit",
  v3.38's two limits on Stale Skill = Stop and v3.39's "A Check That
  Cannot Fail Is Not Passing" all remain in force.]

Phases 0, 1a and 1b are all closed. Layer 3, the nightly Task Scheduler
job, is RETIRED as of August 10 -- disabled, not deleted.

The four documents that described it as live were re-checked on August
18, and the list itself had gone stale.
MASTER_PLAN_INTERACTIVE_GALLERY.md line 40 was ALREADY corrected and
states the retirement with its reasoning. TESTING_PROTOCOL.md Layer 3
was still telling a reader to enable the schedule and is corrected in
the same patch as this note -- it mattered more than the others,
because a testing protocol is read at the moment of doing the thing it
describes. The gallery-cache-builder skill and the ledger's
deployment-model block still need a look; the line numbers recorded
here have moved and are not worth trusting.

That a to-do list about staleness went stale is the ordinary case, not
an irony. It is why the entries above carry what was measured and when
rather than a line number.

AUGUST 12-13: THE PROVENANCE LAYER GREW TEETH

Two sessions, no rendering code touched, and Track 0 did not move. What
changed is what the tooling can now catch.

L-186 closed, and it turned out not to be a data question at all. Six
findings had been carried through three handoffs as "each needs a look
at the source." All six were the parser misreading correct
annotations, because the old annotation format let a source's own
publication year eat the check date. The fix was the format. All 134
annotations were migrated.

L-188 and L-189 closed. `maintenance_run.py` now runs four generators
and twelve checkers in one command, about 40 seconds. Its very first
pass found two test files that had been red for days and that nobody
ran, which is the argument for the runner in one sentence.

Fifty-five pinned constant values were retired from the test suite.
They were pinning pre-correction numbers and nobody had updated them.
`constants_change_report.py` replaces them and stores no numbers at all
-- it asks git what moved and reads both values out of the diff, which
means it covers constants that do not exist yet.

L-192 is the one worth reading twice. The scanner had been granting
its top trust rung -- cross-checked -- to values on the strength of
annotations written for a DIFFERENT value a few lines away. The
deciding case was the inner Oort cloud limit, which wore the top badge
while the two worksheets it was credited with read UNVERIFIED and
PARTIAL for that exact number. A recorded non-verification was
rendering as a completed check.

Credit now requires the annotation to touch the value's own
declaration. The cross-checked count fell from 77 to 50. Nothing got
worse; 50 was always the real number.

Two things from those sessions are worth carrying beyond them.

The first is a correction. A measurement went to Tony wrong twice
before it was caught -- Fable's written rule and its own script
disagreed, and the independent check reproduced the error because it
read the same prose the same wrong way. Two implementations agreeing
is only as good as the specification they share. The right split is 50
and 27.

The second is a move that is now standing procedure: reopen the
session that produced the evidence. Two cited worksheets were
unusable, and the design was drifting toward building a parser clever
enough to interpret them. Tony's ruling was that we do not have to
accept and interpret incomplete or malformed answers. Going back to
the August 2-4 conversation and asking it to finish closed nine of
seventeen open rows, settled Mercury's radius after eleven days, and
turned up two annotations crediting a worksheet for checks it had
explicitly declined to make. Old sessions persist, they hold the
research context, and asking them to finish costs a fraction of
starting over.

The worksheet checker itself is designed and reviewed and NOT built.
That is the next build, and one question goes first: whether a
half-confirmed verdict can count as a completed check.

  [Both since done. The checker was built and now runs continually;
  the half-confirmed question was ruled. Left as written because it
  is the record of what was true then.]


WHAT IS TRACKED RIGHT NOW -- 2026-08-18

  Unstarted and unblocked
    The pilot dispatch. 23 rows over constants_new.py, request built
      by selection 2, sent as JSON with markdown as the fallback,
      expected dispositions written before it goes out.

  Ready to build, no ruling outstanding
    Resolver + models fix (L-154) -- two lines and a type, then the
      renderers. Independent of every provenance question, and now the
      only item on this list. It is the smallest piece of work between
      the project and a Saturn that renders.
    Ordinal context window (blocker 7) -- 26 rows share 8 excerpts.
      Not exercised by the pilot on purpose.

  Waiting on a ruling
    Lazy responder: canaries, or remove the self-certifying field
    Claim typing: real row types, or wait for a measured population
    Cross-worksheet disagreement, what UNKNOWN does, pluto 614/638,
      transition sequencing, whether batching becomes real
    The Resolved leg's first token: shipped as the worksheet FILENAME,
      where the design wrote <batch>. Claude's reading, unruled.

  Carried as an obligation
    Confirm provenance-discipline loads at 2.4 before provenance work

  [2026-08-16 list, for the record: builder marker join (DONE, L-196),
  stage 2 continuation markers (DONE), six Shape A citation swaps
  (DONE as seven, L-195), print the seven verdict tokens (DONE), and
  ledger entries for L-194, L-195, L-196 and the L-192 as-built (all
  written).]


Entry written August 2026 with Anthropic's Claude Opus 5. Updated
August 18, 2026, built on b65ac115fc0f820e8270c0807249813c67bde7bc;
gallery at ff18d3e6fa31f70a8f525df471e751d046cf14fa.
