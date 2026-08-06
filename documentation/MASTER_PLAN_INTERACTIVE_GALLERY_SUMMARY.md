Where we are 8/5/2026

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
