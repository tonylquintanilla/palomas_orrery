# -*- coding: utf-8 -*-
"""patch_masterplan_v16.py -- Master Plan v15 -> v16, and refresh the
summary companion to match.

Built on 4b82384e32682d08371180a5bcb55a77dcab02bc
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery repo pinned separately at e7e8c5efbe8350e9cca900bafed7bcc8b44529e3
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.

HOW TO RUN
    Save this file in the REPO ROOT (the folder that contains
    documentation/ and LEDGER_CONSOLIDATED.md), open it in VS Code, and
    click Run. It edits two files inside documentation/.

    Success looks like: one "ok" line per edit, then "patch applied".
    Failure looks like: a single "ANCHOR FAIL" or "ERROR" line followed
    by "NOTHING WAS WRITTEN". On any failure both files are left exactly
    as they were, so it is always safe to re-check and re-run.

WHAT IT DOES
    documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md -- eight anchored
        edits (v15 -> v16). Nothing is deleted except three superseded
        status sentences, each replaced in place.
    documentation/MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md -- full
        rewrite, guarded by an MD5 of the expected base. If that file has
        changed since this patch was written, the guard fails and nothing
        is written.

Numbers in this patch were MEASURED at 4b82384 by running
provenance_scanner.py, not carried from the handoff. See the v16 block's
own note: the handoff's 207/580/117 figures predate its own anchor.

Patch written August 5, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

PLAN = os.path.join('documentation', 'MASTER_PLAN_INTERACTIVE_GALLERY.md')
SUMMARY = os.path.join('documentation',
                       'MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md')

# MD5 of the expected base content, taken AFTER CRLF normalization to LF.
PLAN_BASE_MD5 = '20dbc03e0cfb50d0d8ea68a9925a92c0'
SUMMARY_BASE_MD5 = '09f0add74c534400bf295b6b67906aa0'

# The plan already contains UTF-8 glyphs (section marks, check/circle
# status markers, em dashes). Anchors carrying them are written as escaped
# byte sequences so this script's own source stays pure ASCII.

CHECK = b'\xe2\x9c\x93'          # check mark
CIRCLE = b'\xe2\x97\x8b'         # open circle
SECT = b'\xc2\xa7'               # section sign
EMDASH = b'\xe2\x80\x94'         # em dash


# --------------------------------------------------------------------------
# MASTER PLAN EDITS
# --------------------------------------------------------------------------

NEW_CYCLE_PARAGRAPH = b"""

August 4-5 cycle (Claude Opus 5 orchestration + Fable 5 skills-layer
review; landed at `2becfbf`, recorded here at `4b82384`): two ledger
items closed and the record layer brought current. L-182 -- the Mars
Hill sphere corrected to 319.2 R_Mars across all seven copies, module
and live config alike, Mode 5 confirmed. L-178 -- both EARTH_RADIUS_KM
shadow constants removed from `earth_visualization_shells.py`, so the
conversion now runs straight through KM_PER_AU; the GEO belt moved
42,212 -> 42,165 km and the LEO band now renders on its own declared
200/2000 km bounds. (The ledger title says "shadow constants" but the
affected code is LEO/GEO band geometry -- no umbra is involved.)
Protocol v3.34 ratified, with two amendments: the GitHub Desktop /
Run-button preference restated as a preference where practical rather
than a prohibition, and Stale Skill = Stop [CRITICAL] added, halting a
session outright when a loaded skill's version disagrees with its
manifest row. All ten skills bumped and reconciled across their three
stores (repo `skills/`, the generated manifest table, the account
install), with `skills_index.py` now printing what the manifest was
advertising before it overwrites it. Ledger appendix caught up with the
v3.32, v3.33 and v3.34 entries, having stopped at v3.31.

L-182 names a failure class worth carrying forward: a correction that
reaches one copy of a two-copy pair is WORSE than no correction at all.
The August 1 cross-check derived the right Mars value, but its patch
targeted the shell module only; `shell_configs.py` never received it,
and the August 4 consistency pass then harmonized the module UP toward
the uncorrected copy, erasing the fix entirely. The rule that follows:
enumerate every consumer in the same patch, and state which copy is
authoritative AND why, citing the worksheet -- never infer authority
from which copy happens to be live."""

NEW_V16_BLOCK = b"""*New in v16 (August 5, 2026):*
- L-178 and L-182 CLOSED, both Mode 5 confirmed by Tony. Mars Hill
  sphere corrected to 319.2 R_Mars across all seven copies (L-182);
  Earth LEO/GEO band geometry freed of its two duplicate
  EARTH_RADIUS_KM shadow constants (L-178).
- New failure class recorded (see """ + SECT + b"""6): a correction reaching one copy
  of a two-copy pair is worse than no correction, because the next
  consistency pass harmonizes toward the uncorrected copy.
- Protocol v3.34 plus the ten-skill reconciliation across three stores.
  Amendments: the git-GUI preference ruling, and Stale Skill = Stop
  [CRITICAL].
- **The push gate changes for this phase (Tony ratified 2026-08-05).**
  "Tier-1 = 0" becomes **"Tier-1 = 0 on the interactive build path."**
  The global gate was unreachable in practice: of 206 Tier-1 findings
  measured at `4b82384`, 105 sit in the Earth System domain, a
  subsystem Artifact 2 never touches. A gate nobody can reach stops
  functioning as a gate. The path is NAMED explicitly and COMPUTED
  rather than listed -- build-path membership is derived by walking the
  import graph from a small set of declared orrery-side entry points,
  which `dep_trace.py` already does, because a third hand-maintained
  module map would be a third store that drifts. The Earth System
  remainder gets its own L-item and its own schedule; deferring it does
  not endanger the interactive build.
- The gate is built BEFORE the batches it scopes (Tony's correction,
  2026-08-05). Deferring the definition of a gate to a later L-item is
  the same category error as deferring the gate.
- Scanner re-measured at `4b82384` by a live run, not carried: 877
  findings across 118 files -- Tier 1 206, Tier 2 581, Tier 3 88,
  Tier 4 2. Domain split of Tier 1: Earth System 105, orrery 91,
  stars 9, utilities 1, dev tools 0, gallery 0.
- Artifact-2 path measurement at the same SHA, per file:
  `shell_configs.py` 23 Tier-1, `idealized_orbits.py` 26,
  `planet_visualization_utilities.py` 4,
  `saturn_visualization_shells.py` 1,
  `uranus_visualization_shells.py` 1, `orrery_rendering.py` 1,
  `jupiter_visualization_shells.py` 0,
  `neptune_visualization_shells.py` 0 -- 56 across the named files.
  Two consequences worth stating plainly: the gas giant shells are
  ALREADY nearly clean, so Batch 2's job on those four files is VALUE
  VERIFICATION rather than Tier-1 clearance; and Artifact 2 is
  therefore not blocked by scanner debt in the shells themselves.
- Batch 2 (gas giants) is the stated gate before Artifact 2 -- all
  provenance batches clear first (Tony, 2026-08-05).
- L-176 scope boundary recorded so the item is not oversold later:
  illustrated dimensions catch CONSTANT-VS-TEXT drift, not values that
  are internally consistent but wrong. Mars drew exactly the 324.5
  R_Mars its text claimed, and both were wrong. Complementary to the
  provenance cross-check, not a substitute for it.
- Domain coverage gap confirmed live: `orrery_rendering.py` and
  `shell_configs.py` carry findings but have no MODULE_DOMAIN_MAP entry
  and silently default to `orrery`. Both are on the Artifact-2 path, so
  the single most important file in the gate would otherwise land in
  the pile by accident. Fix in the same pass that adds the domain split
  to the console output. Naming note for whoever greps for it: the
  audit's section is titled "Findings by File Type", not "Findings by
  Domain".

"""

PLAN_EDITS = [
    ('MP-1', 'header status v15 -> v16',
     b'**Status:** v15 -- Phase 2 (solar system assembler) BUILD UNDERWAY.',
     b'**Status:** v16 -- Phase 2 (solar system assembler) BUILD UNDERWAY.'),

    ('MP-2', 'header current-HEAD anchor -> v16 SHAs',
     b'HEAD orrery `17913aef` / gallery `22c947c9`',
     b'HEAD orrery `4b82384e` / gallery `e7e8c5ef`'),

    ('MP-3', 'last-updated date',
     b'**Last updated:** August 4, 2026',
     b'**Last updated:** August 5, 2026'),

    ('MP-4', 'Batch 2 named as the gate before Artifact 2',
     CHECK + b' Phase 2 Track 1 Batch 1 COMPLETE, ' + CIRCLE +
     b' Phase 2 Track 1 Batch 2 NEXT.',
     CHECK + b' Phase 2 Track 1 Batch 1 COMPLETE, ' + CIRCLE +
     b' Phase 2 Track 1 Batch 2 NEXT.\n'
     b'Batch 2 is now the stated gate before Artifact 2 (Tony, 2026-08-05):\n'
     b'all provenance batches clear before the Jupiter/Saturn artifact\n'
     b'proceeds.'),

    ('MP-5', 'August 4-5 cycle paragraph + L-182 failure class',
     b'\n\nCross-check methodology updated: the competitive pattern',
     NEW_CYCLE_PARAGRAPH +
     b'\n\nCross-check methodology updated: the competitive pattern'),

    ('MP-6', 'scanner state re-measured at HEAD',
     b'- Scanner state: Tier 1 207 -> 207 (provenance-neutral). Batch 2 (gas\n'
     b'  giants) is next, directly unblocking Artifact 2.',
     b'- Scanner state: Tier 1 207 -> 207 (provenance-neutral). Batch 2 (gas\n'
     b'  giants) is next, directly unblocking Artifact 2.\n'
     b'- Re-measured at `4b82384` on 2026-08-05 by a live scanner run, not\n'
     b'  carried: 877 findings across 118 files -- Tier 1 206, Tier 2 581,\n'
     b'  Tier 3 88, Tier 4 2. The 207/580/117 figures above were measured\n'
     b'  before the August 4-5 patches landed; one finding moved Tier 1 ->\n'
     b'  Tier 2. Recorded as a reminder that a number quoted in a handoff\n'
     b'  can predate that handoff\'s own anchor.'),

    ('MP-7', 'insert *New in v16* block',
     b'---\n\n## ' + SECT + b'11 ' + EMDASH +
     b' Protocol & Skills Review (from Phase 0)',
     NEW_V16_BLOCK + b'---\n\n## ' + SECT + b'11 ' + EMDASH +
     b' Protocol & Skills Review (from Phase 0)'),

    ('MP-8', 'tail base SHAs -> v16',
     b'Base: orrery @ `b59cb72` / gallery @ `22c947c9`.\nPhase 0 closed.',
     b'Base: orrery @ `4b82384` / gallery @ `e7e8c5e` (v16; v15 was orrery\n'
     b'`b59cb72` / gallery `22c947c9`).\nPhase 0 closed.'),

    ('MP-9', 'tail: Batch 2 gate + build-path push gate',
     b'Track 1 Batch 2 NEXT: gas giants (jupiter, saturn, uranus, neptune).',
     b'Track 1 Batch 2 NEXT: gas giants (jupiter, saturn, uranus, neptune)\n'
     b'-- and the stated gate before Artifact 2. Push gate for this phase:\n'
     b'Tier-1 = 0 ON THE INTERACTIVE BUILD PATH, with the path computed from\n'
     b'the import graph rather than listed by hand. The gate gets built\n'
     b'before the batches it scopes.'),

    ('MP-10', 'tail: skill updates landed',
     b'Skill updates pending: orrery-coding-conventions (visualization\n'
     b'constant vs range, Hill sphere standard, <br> direction) and\n'
     b'provenance-discipline (cross-check conventions, model credit).',
     b'Skill updates LANDED 2026-08-05: all ten skills bumped and reconciled\n'
     b'across repo, manifest, and account install --\n'
     b'orrery-coding-conventions 1.3, provenance-discipline 1.7,\n'
     b'ledger-and-session-records 1.5, safe-file-editing 1.2,\n'
     b'agentic-pre-test 1.2, gallery-pipeline 1.2, gallery-assembler 1.1,\n'
     b'gallery-cache-builder 1.2, horizons-orbital-mechanics 1.1,\n'
     b'earth-system-pipeline 1.1. Protocol at v3.34.'),
]


# --------------------------------------------------------------------------
# SUMMARY COMPANION -- full rewrite, MD5-guarded
# --------------------------------------------------------------------------

SUMMARY_NEW = b"""Where we are 8/5/2026

Built on 4b82384e32682d08371180a5bcb55a77dcab02bc at
https://github.com/tonylquintanilla/palomas_orrery (branch main);
gallery at e7e8c5efbe8350e9cca900bafed7bcc8b44529e3 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.

Companion to MASTER_PLAN_INTERACTIVE_GALLERY.md v16. The plan is the
reference document; this is the readable snapshot.


THE SHORT VERSION

Artifact 2 -- the Jupiter/Saturn golden artifact -- is the next build
target. Two things stand between here and it, and they are different
kinds of thing. One is a missing piece of code: the client-side
JavaScript that draws served features (rings, shells, radiation belts)
does not exist anywhere in the repo, so the data arrives correctly and
nothing renders it. The other is a standing instruction from Tony: all
provenance batches clear before Artifact 2 proceeds, which makes Batch 2
(the gas giants) a gate rather than a queue item.

The August 4-5 cycle did not advance either of those directly. It closed
two ledger items, ratified protocol v3.34, reconciled the skills layer,
and -- most consequentially -- changed what the push gate means.


THE GATE CHANGE (the load-bearing decision of this cycle)

The old push gate was "Tier-1 findings = 0," where Tier 1 is the
provenance scanner's highest-severity band: constants that are uncited,
contradicted, or otherwise unsupported. There are 206 of them at HEAD.

Roughly half sit in the paleoclimate and Earth-scenario subsystem, which
Artifact 2 never touches. So the gate was unreachable in practice, and a
gate nobody can reach stops working as a gate.

Tony ratified the change on August 5: the gate becomes "Tier-1 = 0 on
the interactive build path." Two conditions attach to it.

First, the path is COMPUTED, not declared. Build-path membership is
derived by walking the import graph outward from a few named orrery-side
entry points -- dep_trace.py already performs that walk. The alternative,
a third hand-maintained list of modules, would be a third store that
drifts out of agreement with the other two, and store drift is precisely
the failure this whole cycle kept surfacing.

Second, the gate is BUILT BEFORE the batches it scopes. This was Tony's
correction to an earlier proposal that would have opened it as a ledger
item for later. Deferring the definition of a gate is the same category
error as deferring the gate.

The Earth System remainder is real debt, but it belongs to a dormant
subsystem with no active ledger work and no owning skill section. It
gets its own L-item and its own schedule.


WHAT CLOSED, AUGUST 4-5

L-182 -- Mars Hill sphere. Corrected to 319.2 R_Mars across all seven
copies, module and live config alike. Mode 5 confirmed.

This one earned a lesson. The August 1 cross-check derived the right
value, but its patch reached only the shell module; shell_configs.py
never got it. The August 4 consistency pass then harmonized the module UP
toward the uncorrected copy and erased the fix. The general form: a
correction that reaches one copy of a two-copy pair is worse than no
correction at all, because the next consistency pass will harmonize
toward the copy that was missed.

L-178 -- Earth LEO/GEO band geometry. Both duplicate EARTH_RADIUS_KM
constants removed from earth_visualization_shells.py; conversion now runs
straight through KM_PER_AU. The GEO belt moved 42,212 -> 42,165 km and
the LEO band now renders on its own declared 200/2000 km bounds. (The
ledger title says "shadow constants," but the code affected is band
geometry -- no umbra involved.)

Protocol v3.34. Two amendments. The GitHub Desktop / VS Code Run button
is now stated as a preference where practical rather than a prohibition,
resolving a conflict Fable flagged with safe-file-editing's delivery
format. And Stale Skill = Stop [CRITICAL] was added: when a loaded
skill's version disagrees with its manifest row, the session halts and
asks for a push and a reinstall, rather than proceeding and mentioning it
afterwards. The manifest had been advertising wrong versions for about
three weeks with nothing surfacing it.

Skills layer. All ten skills bumped and reconciled across their three
stores -- the repo, the generated manifest table, and the account
install. Current versions: orrery-coding-conventions 1.3,
provenance-discipline 1.7, ledger-and-session-records 1.5,
safe-file-editing 1.2, agentic-pre-test 1.2, gallery-pipeline 1.2,
gallery-cache-builder 1.2, gallery-assembler 1.1,
horizons-orbital-mechanics 1.1, earth-system-pipeline 1.1.

Ledger appendix caught up with the v3.32, v3.33 and v3.34 entries; it
had stopped at v3.31.


SCANNER STATE, MEASURED AT 4b82384

A live run, not a figure carried from a handoff: 877 findings across 118
files. Tier 1 206, Tier 2 581, Tier 3 88, Tier 4 2.

Worth noting for future reference: the handoff that scoped this session
recorded 207/580/117. Those numbers were measured before the August 4-5
patches landed, which is to say before the handoff's own anchor. One
finding moved from Tier 1 to Tier 2. Small in itself, but it is a
reminder that a number inside a document can predate the SHA that
document is anchored to.

Tier 1 by domain:

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
positives. Clearing them would mostly mean writing exception entries for
things already understood. Tier 3 and 4 (90 together) are low priority
by construction, and 36 of the Tier 3 sit in dev_tools -- audit and
diagnostic scripts that never render anything.


THE ARTIFACT-2 PATH, PER FILE

Measured at the same SHA:

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

Two things follow, and both are good news.

The gas giant shells are already nearly clean. Jupiter has zero Tier-1
findings and Neptune zero; Saturn and Uranus have one each. Batch 2's job
on those four files is VALUE VERIFICATION, not Tier-1 clearance. Artifact
2 is not blocked by scanner debt in the shells themselves.

And the critical path is tractable: 56 findings across eight named files,
dominated by shell_configs.py and idealized_orbits.py. shell_configs.py's
share should shrink as Batch 2 lands.

(These 56 are the named-file subset. The computed path from Task 2b may
differ once the import walk runs -- that is the point of computing it.)


WHAT COMES NEXT, IN ORDER

1. Master plan v16 -- DONE, this patch.

2. Build the interactive-build-path gate. Two pieces. The cheap one:
   print the per-domain split under each tier line in the scanner's
   console output, and close the domain coverage gap -- orrery_rendering.py
   and shell_configs.py currently have findings but no MODULE_DOMAIN_MAP
   entry, so they default to `orrery`. shell_configs.py is the single most
   important file the gate covers, and it is landing in the generic bucket
   by accident. The piece needing a decision: which orrery-side entry
   points define the build. (Naming note: the audit section is titled
   "Findings by File Type", not "Findings by Domain".)

3. L-176 -- illustrated dimensions in shell hover text. Add a line of the
   form "illustrated between _ and _ radii, a thickness of _ km,"
   computed at render time from radius_fraction, so text can be checked
   against the plot by eye rather than by hand. Natural home is
   build_sphere_shell in orrery_rendering.py -- one producer, and every
   sphere shell inherits. Custom geometry needs separate handling.

   Scope boundary, so it is not oversold: this catches drift between a
   constant and the text describing it, which was the Batch 1 class. It
   does NOT catch a value that is internally consistent but wrong. Mars
   drew exactly the 324.5 R_Mars its text claimed and both were wrong.
   Complementary to the cross-check, not a substitute.

4. Phase 2 Track 1 Batch 2 -- three-model competitive cross-check for the
   gas giants (jupiter, saturn, uranus, neptune). Known inputs waiting:
   the Saturn Hill sphere, whose radius_fraction of 1120 draws about 67.5
   Mkm against text claiming 91 Mkm, with a citation that contradicts
   itself inside one sentence; L-177's Mercury convention question; 42
   remaining "Verified: April 2026" stamps in live modules; and false
   "not yet rendered" claims in dead tooltips.

5. Resume L-154's JS feature-rendering layer, then build Artifact 2.

6. Phase 2 Track 2 -- new worksheets for uncovered files, starting with
   celestial_objects.py (54 findings).

7. L-181 -- single-source-of-truth constant layer. The structural fix
   behind most of the drift findings above.

8. L-155 / L-160 -- Phase 3, pinning engine and test retirement.

9. Earth System Tier-1 remainder (105 findings) -- own L-item, own
   schedule, off the interactive build path.


OPEN DECISIONS FOR TONY, IN ORDER OF NEED

  (decide) Orrery-side entry points for the computed build path.
  (decide) L-176 text format, and whether stylized shells show the
           physical value alongside the illustrated one. Mercury's crust
           draws about 88.8 km against a stated 26 km; Venus's draws
           about 121 km against 10-30 km. Both are flagged in code as
           deliberate Mode 5 stylizations.
  (decide) L-176 ordering against the L-181 constant layer -- before,
           with, or after.
  (decide) L-177 Mercury Hill sphere convention. radius_fraction 94.4
           matches no convention: perihelion is 71.9, semi-major 90.5,
           aphelion 109.1, and the # Source comment asserts perihelion.
  (decide) L-183 stars skill scope -- where sgr_a_* and the shared
           visualization_2d/3d/core/utils modules belong.

  (do)     Update this project's custom-instructions field to the v3.34
           PROJECT_INSTRUCTIONS.md at HEAD. The field is still on v3.33,
           which advertises stale skill versions in its manifest table.
           The repo and the account install are both current; only the
           pasted copy is behind.


STAMP COUNT NOTE

42 "Verified: April 2026" stamps remain in live modules --
shell_configs.py 14, earth_visualization_shells.py 13,
jupiter_visualization_shells.py 9, comet_visualization_shells.py 6.
A repo-wide grep returns 59, but the other 17 sit in a test fixture
(test_citation_inheritance.py, 2) and in spent patch scripts still
parked in the repo root (patch_mercury_cross_check.py 6,
patch_mars_cross_check.py 4, patch_eris_cross_check.py 3,
patch_shell_configs_geometry.py 2). An earlier revision of this summary
said 44; 42 is the measured live-module figure.


ALREADY RESOLVED

L-162 (CENTER_BODY_RADII naming) done. L-163 (module role/domain
classification) -- role side closed; domain side deferred into the L-156
cluster. Artifact 1 (Earth) built and Mode-5 accepted, golden fingerprint
locked. Phase 0, Phase 1a, and Phase 1b all closed; Layer 3 (Task
Scheduler) live with a known intermittent promotion-step glitch still
being watched.

Entry written August 2026 with Anthropic's Claude Opus 5.
"""


# --------------------------------------------------------------------------
# HARNESS
# --------------------------------------------------------------------------

def load(path, label, expect_md5):
    """Read, normalize CRLF, and guard against an unexpected base."""
    if not os.path.exists(path):
        print("ERROR: %s not found." % path)
        print("       Save this script in the REPO ROOT, not in documentation/.")
        return None, None
    with open(path, 'rb') as f:
        data = f.read()
    norm = 0
    if b'\r\n' in data:
        norm = data.count(b'\r\n')
        data = data.replace(b'\r\n', b'\n')
        print("fix CRLF     %s: normalized %d line endings to LF" % (label, norm))
    got = hashlib.md5(data).hexdigest()
    if got != expect_md5:
        print("ERROR: %s base does not match." % label)
        print("       expected md5 %s" % expect_md5)
        print("       found    md5 %s" % got)
        print("       The file changed since this patch was written.")
        print("       NOTHING WAS WRITTEN. Re-pull and rebuild the patch.")
        return None, None
    return data, norm


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    plan_path = os.path.join(root, PLAN)
    summary_path = os.path.join(root, SUMMARY)

    plan, plan_norm = load(plan_path, 'master plan', PLAN_BASE_MD5)
    if plan is None:
        return 1
    summary, summary_norm = load(summary_path, 'summary', SUMMARY_BASE_MD5)
    if summary is None:
        print("       (master plan untouched.)")
        return 1

    # Verify EVERY anchor before writing ANYTHING.
    for eid, label, old, new in PLAN_EDITS:
        c = plan.count(old)
        if c != 1:
            print("ANCHOR FAIL: %s (%s) matched %d, expected 1." % (eid, label, c))
            print("             NOTHING WAS WRITTEN. Both files are unchanged.")
            print("             Fix the cause, then RE-RUN this script.")
            return 1

    for eid, label, old, new in PLAN_EDITS:
        plan = plan.replace(old, new, 1)
        print("ok  %-7s %s" % (eid, label))

    summary = SUMMARY_NEW
    print("ok  %-7s %s" % ('SUM-1', 'summary companion rewritten to 8/5/2026'))

    for data, label in ((plan, 'master plan'), (summary, 'summary')):
        try:
            data.decode('utf-8')
        except UnicodeDecodeError as exc:
            print("ERROR: %s result is not valid UTF-8 (%s)." % (label, exc))
            print("       NOTHING WAS WRITTEN.")
            return 1

    with open(plan_path, 'wb') as f:
        f.write(plan)
    with open(summary_path, 'wb') as f:
        f.write(summary)

    total_norm = plan_norm + summary_norm
    print("")
    print("patch applied%s" % (" (+%d CRLF normalized)" % total_norm
                               if total_norm else ""))
    print("  %s  -> v16" % PLAN)
    print("  %s  -> 8/5/2026" % SUMMARY)
    print("")
    print("No ledger edits here, so ledger_index.py does NOT need to run.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
