"""
patch_L234_7_ledger_rows.py

Writes the ledger rows the 2026-08-25 session drafted in its handoff but
never patched in. Target: LEDGER_CONSOLIDATED.md in the ORRERY repo
(https://github.com/tonylquintanilla/palomas_orrery), built on
4ad78a01a642166cb70218ae5728aa6f6c39d7f4.

RUN COMMAND:  python patch_L234_7_ledger_rows.py
Save this file in the SAME FOLDER as LEDGER_CONSOLIDATED.md, open it in
VS Code, click Run.

  Success: one "ok" line per edit, then "patch applied (N bytes)".
  Failure: a single "ERROR:" (bad base) or "ANCHOR FAIL" line. Nothing
           is written either way, so it is always safe to re-check and
           retry.

AFTER RUNNING:  python ledger_index.py
The index zone is generated. This script writes DETAIL blocks only and
never touches the zone between INDEX:START and INDEX:END.

WHAT IS PERMANENT: the ledger rows. This script is one-shot -- it guards
on a fingerprint that stops existing the moment it succeeds -- and is
archived to documentation/ once run.

Seventeen edits:
  NEW  L-234 .. L-241 and L-243 .. L-245 appended to section A
  NEW  L-242 appended to section G
  UPD  L-100 ruled and closed; L-137 note; L-190, L-158, L-181 notes
"""

import hashlib
import os
import sys

TARGET = "LEDGER_CONSOLIDATED.md"
BASE_FP = "08b4685604d5a642579c1f14ad2ccc81"   # content-normalized MD5 @ 4ad78a01


# --------------------------------------------------------------------------
# New detail blocks
# --------------------------------------------------------------------------

BLOCK_234 = """#### [L-234] Reopen Artifact 1: recreate the orrery's Sun in the assembler
<!-- L:234 status:OPEN upd:2026-08-25 section:A flag: rice:4/5/90/3 -->
- **Tony's ruling, 2026-08-25, in three parts.** (1) The artifact ladder
  has a SECOND AXIS that was never sequenced. The seven golden artifacts
  are seven PROPAGATION shapes -- conic, planetocentric, mean elements,
  spacecraft arc, barycentric binary -- and that ladder is complete and
  good. What the orrery DRAWS is a different axis entirely: interiors,
  atmospheres, magnetospheres, belts, tori, rings, comae, solar shells,
  Hill spheres. Nothing in the five segments or the seven artifacts
  sequences that axis. (2) Nobody ever decided that some structures
  would be shown and others not; L-100 carried that as an inherited
  default, never a ruling. (3) Artifacts REOPEN: reopen Artifact 1, get
  it right, then Artifact 2, and so on. "Right" means the orrery
  recreated in the assembler as far as possible. Re-locking is normal,
  not a failure, and the orrery may improve on the way -- as it did with
  the streamer belt.
- **Tony, verbatim:** "it is not my intent. The general intent is to
  redo the orrery in the assembler. Part by part."
- **The consequence that arrives first.** The resolver requests EVERY
  feature key the cache carries for an object, and the golden record
  hashes `feature_keys`, `trace_role_counts` and `legend_groups`. So
  adding a feature family to a body FAILS every locked artifact
  containing it. Under part-by-part that is the normal event, not an
  edge case.
- **Sun half: DONE 2026-08-25.** 19 shells in the assembler, 14 spheres
  and 5 custom. Six gallery-side patches, `patch_L234_1` through `_6`:
  Sun entry plus builder skip and three gates taught; centre features
  dispatched; the 14 spheres drawn; the L-227 hover-wrap fix with scoped
  smoke assertions; IAU solar pole plus the streamer band; the three
  Oort custom shells (torus, clumps, galactic tide). Also delivered:
  `smoke_sun_shells.js` (30 checks) and the two payload fixtures
  `payload_earth.json` and `payload_jupiter_saturn.json`, which had never
  been committed and without which the two existing smoke suites could
  not run at all.
- **Mode 5 passed twice.** 2026-08-24 on the 14 spheres; 2026-08-25 on
  the complete Sun ("looks great"). 44 traces from 8 requests -- Earth's
  4 geometry and 4 markers, the Sun's 18 and 18 -- reconciling exactly
  against the config. Two things the render confirmed that no unit test
  could: the band reads as a helmet and stalk tilted off the ecliptic,
  which is what the 7.225 degree plane fit predicted (L-229); and Frame
  on Sun returned a half-span of 0.279 AU, 1.2 times the outer corona at
  0.2326 AU, which is the legendonly skip in `frameLayout` working --
  without it the frame would have ranged to the gravitational influence
  at 150,000 AU and the Sun would have vanished into a pixel.
- **Three things the build discovered.** (a) THE SUN WAS NOT AN OBJECT:
  twelve entries in `objects_config.json` and none of them the Sun,
  which existed only as a scene centre drawn as a yellow marker, with no
  catalogue record and therefore no `features` key. (b) `frame-origin`
  IS LOAD-BEARING, NOT A LABEL: `served_window` is computed from every
  object whose `canonical_frame` is `heliocentric`, and a participant
  with no trust measurement NULLS that window for the whole cache,
  silently disabling the resolver's propagation bound site-wide --
  tested both ways. (c) THREE BUILDER GATES WOULD HAVE ABORTED THE
  NIGHTLY and reading the code found none of them; `assert_structural`
  invariant #3 aborts on any non-spacecraft with no osculating block,
  which would have killed every build, not just first ones.
- **Not on this path:** segment 2 (transport), the general provenance
  audit, L-225, L-231, and the barycentric solar scene (L-137).
**Gap:** the EARTH half. Inventory measured at orrery HEAD. Already
served: `atmosphere_shell` (1.05, 1.25) and `van_allen_belts`.
Interiors, not served: inner_core 0.19, outer_core 0.55, lower_mantle
0.85, upper_mantle 0.98, crust 1.0. Also not served: hill_sphere 235.0.
Custom, not served: rotation_axis, dipole_cone, magnetosphere, leo,
geostationary_belt. Missing: an `orientation` key -- Earth's pole is
RA 0, Dec 90 (IAU 2018, J2000 celestial north). Two shapes the Sun did
not need: five of the six new sphere entries sit BELOW the surface, so
L-238 is the first patch; and the magnetosphere is genuinely new
geometry -- not a sphere, not a torus, not a band. Earth's block in
`shell_configs.py` carries a block-level `# Source:` header naming USGS,
NASA Earth Fact Sheet, NOAA/NCEI and the Van Allen Probes, verified in
the April 2026 provenance audit; those are the sources the config
entries should carry, with an `orrery_constant` pointer, same pattern as
the Sun's.
- **Note:** RICE 4/5/90/3 -> 6.0 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect, then re-run
  `ledger_index.py`.
**Ref:** HANDOFF 2026-08-25 (orrery `4ad78a01`, gallery `64201783` ->
`88633707`); L-100 (closed by this ruling); L-235, L-237, L-238 (the
work in front); L-229 (the solar pole the band needed); L-239, L-240,
L-241 (orrery-side findings); L-080 (the artifact fingerprint's fields).

"""

BLOCK_235 = """#### [L-235] Checks that cannot fail, gallery side [three instances]
<!-- L:235 status:OPEN upd:2026-08-25 section:A flag: rice:3/4/95/1 -->
- **Found 2026-08-25 while building the Sun.** Three instances of the
  resident gate A Check That Cannot Fail Is Not Passing, all in the
  gallery repo, each reporting exactly what a real pass reports.
- **(1) `test_artifact1_earth.py` T5 reads `fp.compare(golden, golden)`**
  -- the fingerprint against itself. It cannot return a difference, and
  the stored `artifact_1_earth_alone.json` is never opened. Passing
  since July.
- **(2) `solar_system_earth_test2.html` line 99 prints "matches golden
  abbd01094852b57f" as a hardcoded `<summary>` caption.** Nothing
  compares. And `abbd01094852b57f` is `scene_spec_hash` ALONE -- the one
  field that cannot move when features change, which is precisely what
  part-by-part will keep changing.
- **(3) The two smoke suites read `payload_jupiter_saturn.json`,** which
  was a session artifact and was never committed, so neither suite could
  run at all. CLOSED 2026-08-25 by regenerating both payload fixtures.
**Gap:** instances 1 and 2. Point T5 at the STORED file, and either wire
the HTML caption to a real comparison or delete the claim. Worth pairing
with L-237, because re-cutting a golden that nothing compares against
buys very little.
- **Note:** RICE 3/4/95/1 -> 11.4 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** gallery `test_artifact1_earth.py`,
`solar_system_earth_test2.html`, `payload_earth.json`,
`payload_jupiter_saturn.json`; PROJECT_INSTRUCTIONS Part 3, A Check That
Cannot Fail Is Not Passing; L-236; L-237.

"""

BLOCK_236 = """#### [L-236] Gallery maintenance runner [designed, unbuilt]
<!-- L:236 status:OPEN upd:2026-08-25 section:A flag: rice:4/4/80/4 -->
- **Shape.** A `maintenance_run.py` in the GALLERY repo, plus a
  dashboard button in the existing Gallery and Web group.
- **Why it belongs in the gallery, not the orrery.** Every input it
  reads is there. A checker run from the orrery would reach a sibling
  directory that exists only on Tony's machine, and a check that cannot
  find its target skips quietly -- the same failure class as the three
  instances in L-235.
- **First roster:** module atlas and index (generators); the artifact-1
  golden compared against the STORED file; the three Node suites, with
  Node's absence REPORTED rather than skipped; served-cache structural
  validation; config feature-shape validation.
**Gap:** designed, not built.
- **Note:** RICE 4/4/80/4 -> 3.2 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** L-188 (the orrery-side maintenance runner this mirrors); L-235.

"""

BLOCK_237 = """#### [L-237] Artifact 1's golden record is stale and needs re-cutting
<!-- L:237 status:OPEN upd:2026-08-25 section:A flag: rice:3/4/90/1 -->
- **Unblocked 2026-08-25:** Mode 5 passed on the complete Sun, so the
  gate this was waiting on is discharged.
- **Cut 2026-07-11; it differs from today in four fields,** three of
  which predate the 2026-08-25 session: `cache_snapshot_id`;
  `coordinate_bounds` (the nightly refreshes Earth's osculating
  elements); `warnings`, which still carries "served_window is null",
  untrue since 2026-07-22; and `feature_keys`, which gains the Sun's
  six.
**Gap:** re-cut it. Pair with the L-235 T5 fix -- re-cutting a record
that nothing compares against buys very little.
- **Note:** RICE 3/4/90/1 -> 10.8 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** L-234; L-235; L-080 (the fingerprint's field list).

"""

BLOCK_238 = """#### [L-238] radius_fraction > 1.0 assumes every shell is above the surface
<!-- L:238 status:OPEN upd:2026-08-25 section:A flag: rice:3/5/95/1 -->
- **`_validate_feature_shapes` in `gallery_cache_builder.py` asserts
  it.** True of every shell served so far. False of every INTERIOR shell
  in the orrery.
- **It blocks the Earth build.** Earth's inner core at 0.19 walks
  straight into it, and five of the six new sphere entries sit below the
  surface. This is the Earth half's FIRST patch.
**Gap:** relax the invariant to admit interior shells without losing
whatever it was protecting against, then re-run the builder's testing
layers.
- **Note:** RICE 3/5/95/1 -> 14.3 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** gallery `tools/gallery_cache_builder.py`;
`documentation/TESTING_PROTOCOL.md`; L-234 (the Earth half).

"""

BLOCK_239 = """#### [L-239] Seed the three Oort builders so a render is reproducible
<!-- L:239 status:OPEN upd:2026-08-25 section:A flag: rice:2/2/90/1 -->
- **Orrery-side recommendation from assembler work, 2026-08-25.**
  `create_sun_hills_cloud_torus`, `create_sun_outer_oort_clumpy` and
  `create_sun_galactic_tide` in `solar_visualization_shells.py` draw
  from the GLOBAL numpy RNG, so the same figure looks different on every
  render.
- **The streamer band's own docstring already names this and declines to
  copy it.** The assembler ports are seeded.
- **Recommendation:** seed all three in the orrery with the same pattern
  -- a `RandomState` local to the builder, seed in the config -- so the
  two instruments agree about whether a render is reproducible.
**Gap:** nothing depends on it today. It will matter the first time an
Oort scene is fingerprinted.
- **Note:** RICE 2/2/90/1 -> 3.6 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** `solar_visualization_shells.py` lines ~1411, ~1475, ~1551
(verified at orrery `4ad78a01`); the gallery's Sun custom shells; L-234;
L-241 (same three builders).

"""

BLOCK_240 = """#### [L-240] Split declared drawing parameters from measured values
<!-- L:240 status:OPEN upd:2026-08-25 section:A flag: rice:4/4/70/4 -->
- **Orrery-side recommendation from assembler work, 2026-08-25.** The
  gallery's `objects_config.json` now stores the two kinds APART: the
  streamer belt's cusp (Suess and Nerney) and fade (Kasper) sit in
  `{value, unit, source}` nodes, while the warp amplitude, lobe count
  and widths sit under a `drawing` block whose `_declared` field says
  plainly that nobody has sourced them. The orrery mixes both kinds in
  one dict with comments alongside.
- **This is the STRUCTURAL half of the reachability problem.** The
  scanner cannot tell a measurement from a drawing choice because the
  code does not distinguish them, so the audit either over-counts
  (chasing citations for `n_points`) or under-counts.
- **Recommendation:** adopt the same split in `constants_new.py`'s
  FEATURE_REGISTRY when L-181 designs it -- measured entries carry a
  source field as DATA, declared entries carry a declaration string. The
  gallery has now proved the shape works.
**Gap:** gated on L-181's design pass; not a separate build.
- **Note:** RICE 4/4/70/4 -> 2.8 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** L-181; L-190; L-232; gallery `data/objects_config.json`.

"""

BLOCK_241 = """#### [L-241] Hills torus hover states the cloud bounds, not the drawn ring
<!-- L:241 status:OPEN upd:2026-08-25 section:A flag: rice:2/2/95/1 -->
- **`create_sun_hills_cloud_torus` hovers "2,000 to 20,000 AU".** The
  drawn surface runs 5,570 to 16,953 AU about a ring at 11,000, because
  a torus built from an inner and an outer bound puts its surface at the
  MID-radius.
- **Neither statement is wrong** -- the bounds are the cloud, the ring
  is the drawing -- but a reader measuring the picture against the hover
  will find they disagree.
- **Recommendation: say both.** Identical in the assembler; fix both or
  neither.
**Gap:** minor. Fold into the next touch of either instrument.
- **Note:** RICE 2/2/95/1 -> 3.8 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** `solar_visualization_shells.py`; L-234; L-239 (same builders).

"""

BLOCK_242 = """#### [L-242] Two convention candidates awaiting a ruling (OPEN QUESTION)
<!-- L:242 status:OPEN upd:2026-08-25 section:G flag: rice:2/3/80/1 -->
- **Captured 2026-08-25 under capture-on-first-mention.** Both were
  raised as candidates by the sessions that hit them; neither has been
  ruled. Promotion is Tony's judgment, not the finder's. They are
  written here so they do not live only in a handoff -- which is what
  the first one is about.
- **(a) A handoff that opens ledger items should either carry the patch
  that writes them, or say plainly that it does not.** Home would be
  `ledger-and-session-records`. Origin, 2026-08-25: the handoff of that
  date drafted eight items and carried a Tony-action (do) reading "run
  `ledger_index.py` after the ledger patch" while no ledger patch was
  ever produced. The instruction read as completed work while pointing
  at nothing. That handoff passed every check a handoff has -- the
  anchor was there, the (do) list was there, the items were fully
  drafted -- and nothing in the document could reveal that the rows did
  not exist. It was caught by the next session reading the ledger at
  HEAD and finding it stopped at L-233. Same shape as the three
  instances in L-235: a record reporting complete without the thing it
  describes ever having run.
- **(b) A corrected patch built while its predecessor is already
  running, shipped as a follow-on fingerprinted against the PATCHED
  state rather than as a revert.** Home would be `safe-file-editing`.
  Origin, 2026-08-25: it worked, and both routes were proved
  byte-identical. Whether that makes it a convention or a one-off is the
  open question.
**Gap:** **Tony-action (decide)** on each. Either ruling that lands as a
skill bump runs the four-link chain -- SKILL.md, `skills_index.py`, a
protocol version-history entry, one commit (L-230).
- **Note:** RICE 2/3/80/1 -> 4.8 is Claude's proposed score.
**Ref:** HANDOFF 2026-08-25; L-235; L-230 (the four-link binding rule);
L-223 (a paste is an unverified transfer).

"""

BLOCK_243 = """#### [L-243] Retire the replicated AU conversion factor
<!-- L:243 status:OPEN upd:2026-08-25 section:A flag: rice:3/3/95/2 -->
- **Tony's instruction, 2026-08-25:** conversion factors live in
  `constants_new.py`, carry a source, and are CALLED -- not replicated ad
  hoc.
- **The definition is already exemplary.** `KM_PER_AU = 149597870.7` at
  `constants_new.py` line 56, sourced to IAU 2012 Resolution B2 as an
  exact definition, with two independent cross-checks recorded (Claude
  and GPT, both 2026-08-02, each naming its worksheet). Nothing to do
  there.
- **Thirteen live-code replications across seven modules**, measured at
  orrery `4ad78a01`: `palomas_orrery.py`, `visualization_utils.py`,
  `shared_utilities.py`, `spacecraft_encounters.py`,
  `sgr_a_visualization_core.py`, `sgr_a_visualization_core_arcs.py`,
  `create_ephemeris_database.py`. Most are an inline `* 149597870.7`
  inside an f-string. Five of the seven import nothing from
  `constants_new` today.
- **One is a NAMED shadow and it is the dangerous one.**
  `spacecraft_encounters.py` line 70: `AU_KM = 149597870.7  # 1 AU in
  km`, used 14 times in that module. A grep for `KM_PER_AU` does not
  find it, which is how it survived a convention that already forbids
  it. Its schema comment at line 59 states the divisor as a literal too
  -- The Correction Does Not Travel applies to that line in the same
  patch.
- **Recommendation: retire the NAME, not only the value.** An alias
  (`AU_KM = KM_PER_AU`) would remove the second number while leaving the
  second name, and a second name is how this one started. Fourteen
  mechanical substitutions in a data-table module where the diff reads
  easily.
- **Two things measured clean and worth recording.** `SUN_RADIUS_KM` has
  ZERO live replications -- 695700 appears nowhere outside its
  definition. And `constants_new.py` imports only numpy and datetime, so
  it is a leaf: importing it into any of the seven carries no
  circular-import risk.
- **The gallery's copy cannot be removed.** `feature_renderers.js` line
  35 holds `var KM_PER_AU = 149597870.7;`. JavaScript cannot import a
  Python module, so that is segment 2's surface by construction -- and
  one line is as small as that surface gets.
**Gap:** one transactional patch across the seven modules. Touches hover
strings, so the agentic-pre-test data-sweep gate applies: py_compile,
xvfb run on a throwaway copy, live-dispatch smoke.
- **Note:** RICE 3/3/95/2 -> 4.3 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** `constants_new.py` line 56; No Shadow Constants [CRITICAL];
L-178 (the EARTH_RADIUS_KM duplicate, same class); L-244.

"""

BLOCK_244 = """#### [L-244] Sweep for replicated conversion factors as a class [Fable candidate]
<!-- L:244 status:OPEN upd:2026-08-25 section:A flag: rice:3/4/70/3 -->
- **The companion to L-243, and deliberately separate from it.** L-243
  is countable today -- thirteen sites, seven modules, one shadow name --
  and it closes. This one names the CLASS: any conversion factor
  replicated rather than imported.
- **Why the two are split.** A class with no detector has no
  denominator, which is the audit-that-never-closes shape the resident
  rule warns about. Tony's 2026-08-25 framing: do the narrow one now,
  carry the broad one as an item.
- **Candidate route: a Fable sweep.** Broad-reach scoping is what that
  leg is for, and the question suits it -- enumerate every numeric
  literal in the codebase that duplicates a value already named in
  `constants_new.py`, whatever it is called locally. The answer is a
  list, not a judgment, which is the shape that dispatches well.
**Gap:** scope the dispatch. Until it runs there is no count, and until
there is a count this item cannot be sized honestly.
- **Note:** RICE 3/4/70/3 -> 2.8 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect, and whether Fable
  carries it.
**Ref:** L-243 (the narrow instance); L-181; L-190 (scanner reach).

"""

BLOCK_245 = """#### [L-245] Constants drift check compares against the last COMMIT, not the last RUN
<!-- L:245 status:OPEN upd:2026-08-25 section:A flag: rice:3/4/90/2 -->
- **Raised 2026-08-25 from Tony's question about carrying a backup copy
  of `constants_new.py` to diff against.** The backup was declined on
  Tony's own prior ruling; the gap behind the question is real and this
  is it.
- **The declined half, for the record.** `constants_change_report.py`
  states under WHY THERE IS NO SECOND COPY OF ANY NUMBER that a stored
  list of expected values is a second dictionary, a second dictionary is
  hand-maintained, and a hand-maintained copy goes stale -- citing
  `test_constants_provenance.py`, which was that copy: 52 pinned
  literals, six of them behind an August 2 correction batch for ten
  days. A backup of the whole file is that failure at maximum size.
- **The real gap.** The tool compares the WORKING TREE against the LAST
  COMMIT, and says so: it is a pre-commit reader. That fits Tony's loop
  exactly -- sandbox, test, local repo, maintenance run, commit, push --
  but only while the run precedes the commit. Run the suite after
  committing and the diff is empty. The output still prints "compared
  against <sha> <subject>", which is honest evidence git resolved and
  ran, and still reads as nothing changed. Same green, different
  meaning.
- **Fix, confirmed by Tony 2026-08-25: store the last-run SHA, not a
  file.** Compare against the commit the last maintenance run examined
  rather than against HEAD. Git still holds every prior value, so no
  second copy of any number exists and the 2026-08-12 ruling stands
  intact. The window becomes "since anybody last looked" instead of
  "since the last commit."
- **Shared state with L-230.** The skill-version transition watcher needs
  the same "since the last run" anchor to see a version move while the
  protocol version did not. One small run-state file, two checks reading
  it. Build them together or the second one invents a second store.
**Gap:** design the run-state file (location, what it holds, what
happens on a first run with no prior state), then amend
`constants_change_report.py` and build L-230's watcher against it.
- **Note:** RICE 3/4/90/2 -> 5.4 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** `constants_change_report.py`; `maintenance_run.py` CHECKERS row
1; L-230 (the transition watcher); L-188 (the runner);
PROJECT_INSTRUCTIONS Part 3, A Check That Cannot Fail Is Not Passing.

"""

NEW_A = BLOCK_234 + BLOCK_235 + BLOCK_236 + BLOCK_237 + BLOCK_238 + \
        BLOCK_239 + BLOCK_240 + BLOCK_241 + BLOCK_243 + BLOCK_244 + \
        BLOCK_245


# --------------------------------------------------------------------------
# Edits: (label, old, new) -- each must match EXACTLY ONCE
# --------------------------------------------------------------------------

EDITS = [
    (
        "L-234..L-241 + L-243..L-245 appended to section A",
        "\n## PENDING ACTION (Tony-side)\n",
        "\n" + NEW_A + "## PENDING ACTION (Tony-side)\n",
    ),
    (
        "L-242 appended to section G",
        "\n## H. GALLERY / STUDIO TRACK (website repo; low-activity)\n",
        "\n" + BLOCK_242 + "## H. GALLERY / STUDIO TRACK (website repo; low-activity)\n",
    ),
    (
        "L-100 status OPEN -> DONE",
        "<!-- L:100 status:OPEN upd:2026-07-08 section:G flag: rice:2/2/50/2 -->",
        "<!-- L:100 status:DONE upd:2026-08-25 section:G flag: rice:2/2/50/2 -->",
    ),
    (
        "L-100 ruling recorded",
        "  feature_configs.json. Ref: GALLERY_DATA_SOURCE_HANDOFF.md v0.3.\n",
        "  feature_configs.json. Ref: GALLERY_DATA_SOURCE_HANDOFF.md v0.3.\n"
        "**RULED AND CLOSED 2026-08-25 (Tony).** The default recorded above --\n"
        "shells gallery-side, the interactive kept light -- was inherited from\n"
        "the Phase-1b cost framing of 2026-07-08 and was never a decision. Tony:\n"
        "\"it is not my intent. The general intent is to redo the orrery in the\n"
        "assembler. Part by part.\" So the answer to \"which shells, if any, also\n"
        "render interactive-side\" is ALL of them, taken part by part, with\n"
        "artifacts reopening as families are added. See L-234.\n",
    ),
    (
        "L-137 upd date",
        "<!-- L:137 status:PARKED upd:2026-07-17 section:G flag: rice:2/2/50/2 -->",
        "<!-- L:137 status:PARKED upd:2026-08-25 section:G flag: rice:2/2/50/2 -->",
    ),
    (
        "L-137 use-case note",
        "**Ref:** to_do_ideas.md (pre-ledger, 4/16/26). \n",
        "**Note (2026-08-25):** the use case this item's Gap names has\n"
        "surfaced. The Sun HAS an ephemeris relative to the SSB (target 10,\n"
        "origin @0) and the schema would take it -- Pluto and Charon are\n"
        "already stored at `@9`. It does not help the Sun scene: the resolver\n"
        "refuses any object whose stored centre differs from the scene's, and\n"
        "the assembler is built never to transform between frames. So a\n"
        "barycentric SOLAR SCENE is a real future artifact rather than a\n"
        "coordinate-basis switch. Still PARKED; recorded so the reopening\n"
        "condition is visible when that artifact is scheduled. See L-234.\n"
        "**Ref:** to_do_ideas.md (pre-ledger, 4/16/26). \n",
    ),
    (
        "L-190 upd date",
        "<!-- L:190 status:OPEN upd:2026-08-07 section:A flag: rice:4/4/80/3 -->",
        "<!-- L:190 status:OPEN upd:2026-08-25 section:A flag: rice:4/4/80/3 -->",
    ),
    (
        "L-190 measured count",
        "**Ref:** L-181 (the enumerated belt/torus surface); L-189 (run history\n",
        "**Note (2026-08-25), measured at HEAD.** The scanner extracts only\n"
        "DISPLAY STRINGS from the shell modules -- 10 units for Saturn, 20 for\n"
        "Jupiter, 116 for `shell_configs.py`, every one of kind `string`. The\n"
        "ring, belt and torus NUMBERS are function-local literals and are not\n"
        "scored units at all. The surface: 33 ring entries at three fields each\n"
        "(99 numbers) plus 28 belt and torus values, across four modules. None\n"
        "of it is reachable by `worksheet_request_builder.py`. Same gap as\n"
        "stated above, now with a count. See L-181, L-240.\n"
        "**Ref:** L-181 (the enumerated belt/torus surface); L-189 (run history\n",
    ),
    (
        "L-158 upd date",
        "<!-- L:158 status:OPEN upd:2026-07-27 section:W.Active flag: rice:4/2/70/1 -->",
        "<!-- L:158 status:OPEN upd:2026-08-25 section:W.Active flag: rice:4/2/70/1 -->",
    ),
    (
        "L-158 measured instance",
        "**Ref:** `constants_new.py` derived-constants section; L-156 (holds the\n"
        "full ladder this rule attaches to).\n",
        "**Note (2026-08-25), a measured instance from the assembler build.**\n"
        "Four of the Sun's fourteen sphere radii are DERIVED EXPRESSIONS the\n"
        "scanner does not score: `SOLAR_RADIUS_AU`, `CORE_AU`,\n"
        "`RADIATIVE_ZONE_AU`, `CHROMOSPHERE_PHYSICAL_RADII`. All four are\n"
        "richly cited; all four are unreachable, because the scanner scores\n"
        "LITERAL ASSIGNMENTS. The claims inside them -- the 0.2 core factor and\n"
        "the 0.7 radiative-zone factor -- are already declared as visualization\n"
        "boundaries with the measured ranges named, which is the right shape\n"
        "and invisible to the tooling. See L-190.\n"
        "**Ref:** `constants_new.py` derived-constants section; L-156 (holds the\n"
        "full ladder this rule attaches to).\n",
    ),
    (
        "L-181 upd date",
        "<!-- L:181 status:OPEN upd:2026-08-06 section:A flag: rice:5/5/70/5 -->",
        "<!-- L:181 status:OPEN upd:2026-08-25 section:A flag: rice:5/5/70/5 -->",
    ),
    (
        "L-181 two figures corrected",
        "**Ref:** FABLE_shell_consistency_audit_report.md section 2 (Job 2),\n"
        "migration status summary table.\n",
        "**Note (2026-08-25) -- two figures above CORRECTED against HEAD.** The\n"
        "\"about 22 physical values\" in the belt and torus surface is 28:\n"
        "Neptune's four belt regions were never counted. And \"ZERO carry a\n"
        "`# Source:`\" is no longer true -- at HEAD three of the eight blocks\n"
        "do: Jupiter's rings (NASA Ring Fact Sheet, Galileo), Jupiter's belts\n"
        "(NASA Magnetosphere Overview, Juno) and Neptune's belts (Voyager 2;\n"
        "Ness et al. 1989). Saturn's rings, Saturn's belts, both tori and\n"
        "Uranus's belts carry nothing. The bullets above are left as written\n"
        "because they record what was found on 2026-08-07. See L-240 for the\n"
        "structural recommendation this surface now has, and L-190 for the\n"
        "reachability count.\n"
        "**Ref:** FABLE_shell_consistency_audit_report.md section 2 (Job 2),\n"
        "migration status summary table.\n",
    ),
]


def main():
    if not os.path.exists(TARGET):
        print("ERROR: %s not found. Save this script beside it." % TARGET)
        return 1

    with open(TARGET, "rb") as f:
        data = f.read()

    # Fingerprint the CONTENT, not the raw bytes: a Windows working copy
    # may hold CRLF where the repo holds LF, and that is not a change.
    norm = data.replace(b"\r\n", b"\n")
    fp = hashlib.md5(norm).hexdigest()
    if fp != BASE_FP:
        print("ERROR: base moved.")
        print("  expected content-md5 %s" % BASE_FP)
        print("  found                %s" % fp)
        print("  (%d bytes, %d CRLF)  Nothing written." % (data.count(b"\n"), data.count(b"\r\n")))
        return 1

    is_crlf = data.count(b"\r\n") > 0
    print("base ok  (content-md5 %s, %s)" % (fp, "CRLF" if is_crlf else "LF"))

    # Encoding gate on what this patch INTRODUCES.
    for label, _old, new in EDITS:
        try:
            new.encode("ascii")
        except UnicodeEncodeError as e:
            print("ERROR: non-ASCII in inserted text for edit '%s': %s" % (label, e))
            return 1
    pre = sum(1 for b in norm if b > 127)
    print("note: inserted text is ASCII-clean; %s"
          % ("%d pre-existing non-ASCII byte(s) remain in the file "
             "this patch did not reach" % pre if pre else
             "file holds 0 pre-existing non-ASCII bytes"))

    out = data
    for label, old, new in EDITS:
        o = old.encode("ascii")
        n = new.encode("ascii")
        if is_crlf:
            o = o.replace(b"\n", b"\r\n")
            n = n.replace(b"\n", b"\r\n")
        count = out.count(o)
        if count != 1:
            print("ANCHOR FAIL [%s]: expected 1 match, got %d" % (label, count))
            print("  anchor: %r" % old[:70])
            print("  Nothing written.")
            return 1
        out = out.replace(o, n)
        print("ok  %s" % label)

    with open(TARGET, "wb") as f:
        f.write(out)

    print("patch applied (%d bytes -> %d bytes, +%d)"
          % (len(data), len(out), len(out) - len(data)))
    print("NEXT: run  python ledger_index.py  to regenerate the index zone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
