# -*- coding: utf-8 -*-
"""patch_summary_v17.py -- refresh the master plan's summary companion
from the 8/5 snapshot to 8/7, matching master plan v17.

Built on d38d31482a8fedc8d6625930bc6d2ba2f15fb8cb
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery pinned at 61a78c00668573dbff111ec9f10a96b1cd2fdc35.

HOW TO RUN
    Save this file in the REPO ROOT (the folder holding documentation/),
    open it in VS Code, and click Run.

    Success: one "ok" line, then "patch applied".
    Failure: an "ERROR" line followed by "NOTHING WAS WRITTEN".

WHAT IT DOES
    Rewrites documentation/MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md in
    full, guarded by an MD5 of the expected base. If that file changed
    since this patch was written, the guard fails and nothing is written.

    No ledger edits, so ledger_index.py does NOT need to run after.

Patch written August 7, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = os.path.join('documentation',
                      'MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md')
BASE_MD5 = '76dcbf4dc5f10d935c1400dd2db75cb5'

NEW = b"""Where we are 8/7/2026

Built on d38d31482a8fedc8d6625930bc6d2ba2f15fb8cb at
https://github.com/tonylquintanilla/palomas_orrery (branch main);
gallery at 61a78c00668573dbff111ec9f10a96b1cd2fdc35 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.

Companion to MASTER_PLAN_INTERACTIVE_GALLERY.md v17. The plan is the
reference document; this is the readable snapshot.


THE SHORT VERSION

Two things changed on August 6-7, and the first one reorders everything.

Tony ruled that the constant-layer scaffolding comes BEFORE the
provenance batches, which come before Artifact 2. His reasoning is the
part to carry: a golden artifact is fingerprinted, so locking one on
values that are not yet sourced and derived means redoing the lock
later, not editing a number. Scaffolding first is the cheaper order, not
the slower one.

The second is that the scaffolding now has a transport design. Feature
geometry -- ring radii, belt extents, shell bounds -- lives in orrery
Python and has never had a way to reach the gallery except by hand. It
was copied once, months ago, and never again. The design that came out
of two Fable review rounds is simpler than anything proposed along the
way, and it requires no change at all to how Tony works.


PHASE 2 IS NOW THREE TRACKS

  Track 0   Constant layer scaffolding (L-181)
            Exit: one store, provenance carried as data, display text
            derived, transport working end to end.

  Track 1   Provenance batches (L-156)
            Exit: Batch 2 gas giants verified, on the Track 0
            scaffolding.

  Track 2   Artifact 2 (Jupiter/Saturn)
            Exit: golden artifact locked on verified, sourced, derived
            values.

This supersedes the August 5 instruction that all batches clear before
Artifact 2. Batches still precede the artifact; Track 0 now precedes the
batches. It is called Track 0 rather than renumbering, because Section 6
already cites "Phase 2 Track 1, Batch 1 / Batch 2" and existing handoffs
use those numbers.

L-181 also moved out of Section 6 (Prep Work) and into the phase
structure. As reframed it carries one store, a citation-form migration,
derivation across five restatement surfaces, a transport, and a
validation pass. That is phase-scale work, and leaving it in a section
meant for small gating tasks is why the August 6-7 design session kept
expanding -- implementation questions were being answered against no
scope boundary.


THE TRANSPORT DESIGN, IN PLAIN TERMS

The problem: Horizons can answer "where is Saturn tonight." It cannot
answer "how wide is Saturn's B ring." The first is a computed position,
fetched fresh every night. The second is a published measurement that
lives in orrery Python. Only the first has ever had a pipeline.

Confirmed live during this session: the 2026-08-06 nightly build
refreshed vectors, elements and positions, and touched NEITHER
objects_config.json NOR feature_configs.json. The build succeeded,
timestamps updated, every freshness signal read green -- and no feature
value moved, because nothing in that pipeline can move one.

The design, called fetch-and-import: each night the builder asks GitHub
for the orrery's current commit, downloads constants_new.py as plain
text at that exact commit, imports it, reads the feature values and
their sources, checks them, and writes them into the served cache.

What Tony does: nothing. Edit a constant, commit, push -- the workflow
he has today. No export step, no new file to run, no scheduled job
committing into the repo where he holds sole commit authority.

Importing rather than parsing matters because the store derives rather
than hardcodes. SOLAR_RADIUS_AU is computed from SUN_RADIUS_KM and
KM_PER_AU; CENTER_BODY_RADII maps body names to other named constants.
Seven of forty-five top-level assignments work this way, and that is the
store's own stated principle, not a defect. Python evaluates all of it
natively. Anything that tried to read the file without running it would
have to reimplement arithmetic the language already does.

This does not violate the builder's "no orrery imports" rule.
constants_new.py is a leaf: it imports numpy and datetime and nothing
else -- no Plotly, no shell modules. That is precisely why the old
exporter could not carry values across: reading shell configs drags
Plotly along, and reading the constants store does not.


HOW THE DESIGN GOT SIMPLER

Three times, a premise turned out to be false, and Tony found each one by
asking a plain question rather than by reading code.

First: "the exporter." Both the design handoff and Fable's first review
wrote it as though pointing at something live. export_orbit_cache.py is a
dormant Phase 1b seeding tool -- nothing imports or calls it on any
automated path.

Second: derived constants as a complication. After the exporter fell, the
session proposed reading the store without executing it, then found seven
derived assignments and wrote that up as a defect. Tony asked why the
store holds both a primary and a derived value. The answer proved the
store correct: SOLAR_RADIUS_AU has eleven consumer files, and deleting it
would push that arithmetic into eleven places.

Third: that the gallery could not execute the file. Never tested. The
builder already hard-depends on numpy through astroquery, so the
environment has everything the store needs.

The design got smaller each time a premise was removed. That is worth
treating as diagnostic: the elaboration was compensating for an
unexamined assumption, not for real complexity.


FOUR VALIDATION LAYERS, FOUR DIFFERENT ERROR CLASSES

  1. Source presence -- an ABORT, not a warning. A physics value without
     a source stops the build.

  2. Unit-sanity RANGE checking. Shape validation and source-presence
     validation both PASS on a value whose units changed. Only magnitude
     bounds catch a km-to-AU slip.

  3. Cross-field ring invariant, inner <= outer.

  4. Nightly value-diff against last night's committed copy, logging old,
     new, and both orrery commit IDs. The only guard that sees CHANGE
     itself, which is the L-182 failure family.

On layer 3, a correction to Fable worth recording. Fable recommended
strict inner < outer and stated it catches nothing spurious today.
Verified against the store, it would fire on eight Neptune entries where
inner and outer are deliberately equal -- narrow ringlets modelled at a
single radius (Le Verrier at 53,200 km; six Adams arcs at 62,932 km). Its
directional claim holds: inner > outer is genuinely zero across all
thirty-three ring pairs. A check that fires spuriously on day one is one
people learn to ignore.


WHAT THE TWO FABLE ROUNDS FOUND

Round 1 endorsed the architecture and found four things the evidence
chain had missed. spectral_subclass_temps is an uncited physical claim
inside the store itself, so the convention has to apply at home before it
is enforced outward. KNOWN_ORBITAL_PERIODS carries the key 'Phobos'
twice -- same value today, and Python silently keeps the last, which is
the argument for a validation pass. The module-level *_info tooltip
strings are a FIFTH restatement surface: Uranus restates 25,559 km nine
times and does arithmetic in prose, and had derivation covered the dict
descriptions but not these, the *_info strings would have become the
surviving duplicate -- L-182's exact shape, which the build was on course
to recreate. And the gallery constant enumeration missed four sites,
including three bare 149597870.7 literals inline in gallery_studio.py.

Round 2 endorsed fetch-and-import and added build requirements. Drop the
dead numpy and timedelta imports from constants_new.py -- both are
imported and never used, so the store becomes standard-library-only. Add
a pre-import gate of roughly ten lines that checks two structural
properties before importing: that every import is on an allowlist, and
that no dictionary has a duplicate key. That second check is the one
capability fetch-and-import otherwise loses, because after import Python
has already silently kept the last duplicate. And define one name --
FEATURE_REGISTRY -- that the builder reads and nothing else, so every
rename or regrouping inside the store stays internal.


OPEN DECISIONS FOR TONY, IN ORDER OF NEED

  (decide) Ratify fetch-and-import. Plan Section 7 decision 12. Two
           reviewers recommend it; no ruling yet.

  (decide) Pilot slice inside Track 0. Section 7 decision 16. Fable
           recommends migrating Jupiter alone -- five entries -- through
           the full Track 0 treatment and building the transport
           end-to-end against it, then scaling to the remaining
           thirty-two, which needs zero transport rework. The argument:
           the transport cannot be tested against today's store at all,
           since no source fields exist yet for abort-on-missing-source
           to act on. So "transport after Track 0" really means "first
           end-to-end test after all thirty-seven entries move" -- the
           largest possible batch before the first proof. Jupiter also
           holds the prose cases that resist naive interpolation. Cost:
           two passes over the migration tooling instead of one.

  (decide) Interpolation locus. Section 7 decision 17. The served cache
           can hold templates plus values, with the assembler filling
           them in at render time; or finished strings, with the builder
           filling them in at build time. Fable recommends builder-side:
           it keeps the assembler dumb and moves template errors to build
           time where quarantine exists, rather than into a browser. It
           decides the cache schema, so it is decided before the schema
           is written.

  (decide) L-179 and L-180 values. Section 7 decision 14, and Track 0's
           first step. See the note below -- a patch addressing both is
           already sitting in the repo unrun.

  (decide) Annotation parser ruling. L-186, Track 1. Three annotations
           name a worksheet .md file but append the checked value, e.g.
           "(batch1_tier2_followup_gpt.md: 14.27 Mkm)". The parser tests
           that the parenthetical ENDS in .md, so a richer annotation is
           rejected for carrying more provenance, not less. Strip the
           values, or extend the pattern? Claude's lean is extend; it
           sits adjacent to "do not loosen a checker to clear findings,"
           so the ruling is Tony's.


UNRUN PATCH SITTING AT HEAD

patch_L179_L180_derivation.py was committed at d38d314 and has not been
run -- L-179 and L-180 still read status:OPEN in the ledger. It did not
come from the August 6-7 design session.

Checked before recording: its anchor 6623c69 is one commit back and is a
real ancestor, and none of its five target files have changed since, so
its base is still valid. It closes both items by making every displayed
figure DERIVE from constants_new.py rather than be typed -- which is the
Track 0 approach, so it is aligned rather than competing. It touches
constants_new.py, planet_visualization_utilities.py,
solar_visualization_shells.py, palomas_orrery.py, and
test_constants_provenance.py.

One small note for later: it adds GRAVITATIONAL_INFLUENCE_RANGE_AU as a
tuple. Under fetch-and-import, tuples become JSON lists, which the
serialization boundary check should handle deliberately rather than
discover.


SCANNER STATE, MEASURED AT 4b82384

A live run, not a figure carried from a handoff: 877 findings across 117
files. Tier 1 206, Tier 2 581, Tier 3 88, Tier 4 2. (An earlier revision
of this summary said 118 files; the extra one was a patch script sitting
in the test directory during measurement, not a repo file.)

Tier 1 by domain, now printed under each tier line in the scanner's own
console output as of the Task 2a patch:

  Earth System                105
  Orrery                       91
  Stars                         9
  Utilities                     1
  Dev Tools                     0
  Gallery                       0

Why the other tiers are not the target. Tier 2 (581) is already
adjudicated -- cited constants, staleness flags on verified strings, and
known scanner limitations, all documented as accepted residuals.
info_dictionary.py alone holds 119 of them as multi-line-string false
positives. Tier 3 and 4 (90 together) are low priority by construction,
and 36 of the Tier 3 sit in dev_tools -- audit and diagnostic scripts
that never render anything.

The push gate for this phase is "Tier-1 = 0 on the interactive build
path," not the global figure. The global gate was unreachable in
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
is not blocked by scanner debt in the shells themselves. And the critical
path is tractable: fifty-six findings across eight named files, dominated
by shell_configs.py and idealized_orbits.py, whose share should shrink as
Batch 2 lands.


LEDGER ITEMS BY TRACK

  Track 0     L-181  Complete the constant layer -- the Track 0 build
              L-179  Solar gravitational influence, 150,000 vs 126,000 AU
              L-180  Solar chromosphere, three inconsistent extents
              L-176  Illustrated dimensions in shell hover text

  Track 1     L-186  Twelve cross-check annotation issues, before Batch 2
              L-177  Mercury Hill sphere convention
              L-184  Interactive build-path push gate (2a done, 2b reshaped)

  Track 2     L-154  JS feature-rendering layer -- does not exist yet

  Independent L-185  Source discipline for assembler constants, about
                     eight sites, plus a retirement note for
                     export_orbit_cache.py and its dashboard menu entry
              L-187  info_dictionary numeric-overlap enumeration, deferred
              L-183  Stars skill scope
              L-124  Systematic color-accuracy pass, low priority


ALREADY RESOLVED

L-178 (Earth LEO/GEO band geometry) and L-182 (Mars Hill sphere, 319.2
R_Mars across all seven copies) both closed August 5, Mode 5 confirmed.
L-162 (CENTER_BODY_RADII naming) done. Artifact 1 (Earth) built and
Mode-5 accepted, golden fingerprint locked. Protocol at v3.34 and all ten
skills reconciled across their three stores. Phase 0, Phase 1a and Phase
1b all closed; Layer 3 (Task Scheduler) live, with a known intermittent
promotion-step glitch still being watched.

Entry written August 2026 with Anthropic's Claude Opus 5.
"""


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(root, TARGET)
    if not os.path.exists(path):
        print("ERROR: %s not found." % TARGET)
        print("       Save this script in the REPO ROOT, not documentation/.")
        print("       NOTHING WAS WRITTEN.")
        return 1

    with open(path, 'rb') as f:
        data = f.read()

    norm = 0
    if b'\r\n' in data:
        norm = data.count(b'\r\n')
        data = data.replace(b'\r\n', b'\n')
        print("fix CRLF     normalized %d line endings to LF" % norm)

    got = hashlib.md5(data).hexdigest()
    if got != BASE_MD5:
        print("ERROR: summary base does not match.")
        print("       expected md5 %s" % BASE_MD5)
        print("       found    md5 %s" % got)
        print("       The file changed since this patch was written.")
        print("       NOTHING WAS WRITTEN. Re-pull and rebuild.")
        return 1

    try:
        NEW.decode('utf-8')
    except UnicodeDecodeError as exc:
        print("ERROR: replacement is not valid UTF-8 (%s)." % exc)
        print("       NOTHING WAS WRITTEN.")
        return 1

    with open(path, 'wb') as f:
        f.write(NEW)

    print("ok  SUM-1  summary companion rewritten to 8/7/2026 (matches v17)")
    print("")
    print("patch applied%s" % (" (+%d CRLF normalized)" % norm if norm else ""))
    print("  %s" % TARGET)
    print("")
    print("No ledger edits, so ledger_index.py does NOT need to run.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
