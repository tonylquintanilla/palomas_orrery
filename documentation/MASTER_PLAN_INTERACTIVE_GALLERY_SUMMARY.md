Where we are 8/11/2026

Updated 2026-08-11 after the August 8-10 session. Built on
4509c08 at
https://github.com/tonylquintanilla/palomas_orrery (branch main);
gallery at 02d71637e100c4faf6ddaa23cdbc9b6f4a88ddc0 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.

Companion to MASTER_PLAN_INTERACTIVE_GALLERY.md v17. The plan is the
reference document; this is the readable snapshot.

The plan is now current with this snapshot. Every August 8 ruling is
written into Section 7 -- decision 12 ratified, 16 and 17 ruled, and 18
added for the registry's three-zone shape. Where the two documents once
disagreed they now agree, so either is safe to read.


THE SHORT VERSION

Track 0 is no longer waiting on decisions. On August 8 Tony ruled the
five questions that were blocking it -- the transport, the shape of a
registry entry, what a measured field carries, where display text gets
assembled, and what order the migration runs in. Nothing in Track 0 now
needs a ruling before work can start.

The order changed in a way worth stating plainly. Artifact 2 was blocked
behind Track 0 and Batch 2. It is now step 2: prove the registry
structure on Jupiter first, where the served data is already complete
and correct so the transport gets a real acceptance test, then
cross-check Artifact 2's remaining values into the proven structure.
Structure first, values second.

Two smaller things landed on August 10. L-186's mechanical half is done
-- eight annotations repointed at a real worksheet file, three appended
values stripped -- and one shadow constant is gone. The scheduled
nightly build is retired; Tony now runs the builder by hand and commits
it himself.

The next session opens with the build of L-189, the
scanner run history.


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
Tony and filed at documentation/worksheet_gemini_constants_remaining.md.
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

  (decide) Where the L-188 run-all push-gate binding lands -- L-188 or
           L-184.

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

The tier breakdown below was measured at 1ba20c3 on August 7 and has not
been re-measured since: 879 findings across 117 files, Tier 1 206,
Tier 2 583, Tier 3 88, Tier 4 2.

  Tier 1 by domain

    Earth System                105
    Orrery                       91
    Stars                         9
    Utilities                     1
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

  shell_configs.py                      23
  idealized_orbits.py                   26
  planet_visualization_utilities.py      4
  saturn_visualization_shells.py         1
  uranus_visualization_shells.py         1
  orrery_rendering.py                    1
  jupiter_visualization_shells.py        0
  neptune_visualization_shells.py        0
                                        --
                                        56

Two things follow, both good news. The gas giant shells are already
nearly clean -- two Tier-1 findings across all four files -- so Batch 2's
job on them is VALUE VERIFICATION, not Tier-1 clearance, and Artifact 2
is not blocked by scanner debt in the shells themselves. And the
critical path is tractable: fifty-six findings across eight named files.


LEDGER ITEMS BY TRACK

  Track 0     L-181  Complete the constant layer -- the Track 0 build
              L-179  Solar gravitational influence  DONE
              L-180  Solar chromosphere  DONE
              L-176  Illustrated dimensions in shell hover text

  Track 1     L-186  Cross-check annotation issues -- mechanical half
                     done, six duplicate_identity sites remain
              L-177  Mercury Hill sphere convention
              L-184  Interactive build-path push gate

  Track 2     L-154  JS feature-rendering layer -- does not exist yet

  Tooling     L-188  Maintenance runner -- one command, the whole suite
              L-189  Provenance scanner: run history and run-to-run
                     delta  -- NEXT SESSION'S BUILD
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

Jupiter's registry entry count is unsettled. The August 7 revision of
this summary said five; the August 10 session counted four ring entries.
Confirm before the pilot starts, since the pilot is scoped by it.

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

Protocol at v3.35. The v3.36 Register Rule amendment is drafted at
documentation/REGISTER_RULE_AMENDMENT_v3.36.md and NOT YET APPLIED. "The
Artifact Bounds the Audit" is ruled for Part 3 but has no drafted text
anywhere in the repo -- it needs writing, not applying.

Phases 0, 1a and 1b are all closed. Layer 3, the nightly Task Scheduler
job, is RETIRED as of August 10 -- disabled, not deleted. Several
documents still describe it as live: MASTER_PLAN_INTERACTIVE_GALLERY.md
line 40, documentation/TESTING_PROTOCOL.md line 292, the
gallery-cache-builder skill line 70, and the deployment-model decision
block in the ledger near line 4555.

Entry written August 2026 with Anthropic's Claude Opus 5.
