Here it is, in order. Gallery first, then the orrery ledger.

## Gallery repo

**1. Install the patch.** Save `patch_L342_2_display_figures_20260920.py` into the gallery repo root, next to `index.html`. Open it in VS Code and click Run.

Expect: a run of `ok` lines, then `patch applied (19 edits, 8 served slots, 2 files created)`. If you see a single `ERROR:` or `ANCHOR FAIL:` line instead, nothing was written — send me the line and stop there.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L342_2_display_figures_20260920.py
ok  feature_renderers.js               function servedFigures(node) {
ok  feature_renderers.js               function fmtKm(km) {
ok  feature_renderers.js               var hover = label + "<br><br>" +
ok  feature_renderers.js               var traces = [];
ok  feature_renderers.js               figures.push(servedFigures(node));
ok  feature_renderers.js               "= " + kmAndAu(distances[i] * radiusKm) + "<br>" +
ok  feature_renderers.js               var hover = label + "<br><br>" + descLine(cfg) +
ok  feature_renderers.js               function renderStreamerBand(slug, bodyName, cfg, where, ce
ok  feature_renderers.js               "Cusp: " + cuspR + " solar radii<br>= " +
ok  feature_renderers.js               function renderEquatorialRing(slug, bodyName, cfg, where, 
ok  feature_renderers.js               var hover = label + "<br><br>" + descLine(cfg);
ok  feature_renderers.js               var starRadiusKm = null;
ok  feature_renderers.js               traces = traces.concat(stampShell(stampLink(renderStreamer
ok  feature_renderers.js               var ringTraces = renderEquatorialRing(
ok  feature_renderers.js               var hover = label + "<br><br>" + descLine(cfg);
ok  feature_renderers.js               var radiusKm = measured(params.planet_radius, "km",
ok  feature_renderers.js               "= " + kmAndAu(r0 * radiusKm) + "<br>" +
ok  feature_renderers.js               var bsHover = bsLabel + "<br><br>" + descLine(bs) +
ok  objects_config.json                lower_atmosphere/altitude -> EARTH_STRATOPAUSE_ALTITUDE_KM
ok  objects_config.json                upper_atmosphere/altitude -> EARTH_THERMOPAUSE_ALTITUDE_KM
ok  objects_config.json                leo_inner/altitude -> EARTH_LEO_LOWER_ALTITUDE_KM
ok  objects_config.json                leo_inner/radius_km -> EARTH_LEO_INNER_KM
ok  objects_config.json                leo_outer/altitude -> EARTH_LEO_UPPER_ALTITUDE_KM
ok  objects_config.json                leo_outer/radius_km -> EARTH_LEO_OUTER_KM
ok  objects_config.json                geostationary_ring/radius_km -> EARTH_GEOSTATIONARY_RADIUS_KM
ok  objects_config.json                hill_sphere/radius_km -> EARTH_HILL_SPHERE_KM
ok  gallery_maintenance_run.py         Display figures checker added
ok  documentation/smoke_display_figures.js created
ok  documentation/fixture_hovers_cdfa74c3.json created (43 hovers)

patch applied (19 edits, 8 served slots, 2 files created)

NEXT, IN THIS ORDER. The new check is RED until step 3, on
purpose: the config now carries eight entries the served cache
does not, and the check reads the cache because that is the
file the browser fetches.
  1. python tools/mirror_constants.py
     Expect: 0 fields would change. That is the proof this
     patch wrote the export's own numbers.
  2. Pause OneDrive syncing.
  3. Rebuild the served cache with the cache builder.
  4. python gallery_maintenance_run.py
     Expect: Cache in step and Display figures both green.
  5. Move this script into documentation/, commit the config
     AND the cache together, push.
  6. python gallery_maintenance_run.py --live
  7. Look at Earth's room on your phone.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

**2. Check the mirror.** Open `tools/mirror_constants.py` and Run.

Expect: `0 field(s) would change`. That is the proof the patch wrote the export's own numbers rather than numbers it made up. If anything would change, stop and send me the output.

======================================================================
  CONFIG MIRROR -- data/constants_export.json -> data/objects_config.json
======================================================================

78 link(s): 45 served, 28 fallback, 5 outside the store.

DEFINITION, 1 link(s) transmitted as exactly 1:
  EARTH_EQUATORIAL_RADIUS_KM         1 r_earth by definition: this row is what the token table calls one r_earth

SERVED, 0 with something to write:
  every served link already holds the export's numbers

FALLBACK, 28 link(s) the export cannot serve yet:
  ALFVEN_SURFACE_RADII               no # Unit: line
  ALFVEN_SURFACE_RADII               no # Unit: line
  CHROMOSPHERE_PHYSICAL_RADII        no # Unit: line
  CORE_AU                            no # Unit: line
  EARTH_BOW_SHOCK_JELINEK_EPS        unit token 'dimensionless' is retired: names no quantity, so
  EARTH_BOW_SHOCK_JELINEK_LAMBDA     unit token 'dimensionless' is retired: names no quantity, so
  EARTH_MAGNETOPAUSE_SHUE_A6         unit token 'dimensionless' is retired: names no quantity, so
  EARTH_MAGNETOPAUSE_SHUE_A8         unit token 'dimensionless' is retired: names no quantity, so
  GRAVITATIONAL_INFLUENCE_AU         no # Unit: line
  HELIOPAUSE_RADII                   no # Unit: line
  HELMET_CUSP_RADII                  no # Unit: line
  INNER_CORONA_RADII                 no # Unit: line
  INNER_LIMIT_OORT_CLOUD_AU          no # Unit: line
  INNER_LIMIT_OORT_CLOUD_AU          no # Unit: line
  INNER_OORT_CLOUD_AU                no # Unit: line
  INNER_OORT_CLOUD_AU                no # Unit: line
  INNER_OORT_CLOUD_AU                no # Unit: line
  JUPITER_EQUATORIAL_RADIUS_KM       no # Unit: line
  OUTER_CORONA_RADII                 no # Unit: line
  OUTER_OORT_CLOUD_AU                no # Unit: line
  OUTER_OORT_CLOUD_AU                no # Unit: line
  RADIATIVE_ZONE_AU                  no # Unit: line
  ROCHE_LIMIT_RADII                  no # Unit: line
  SOLAR_RADIUS_AU                    no # Unit: line
  SUN_RADIUS_KM                      no # Unit: line
  SUN_RADIUS_KM                      no # Unit: line
  SUN_RADIUS_KM                      no # Unit: line
  TERMINATION_SHOCK_AU               no # Unit: line

OUTSIDE THE STORE, 5 link(s):
  create_sun_galactic_tide default   points outside constants_new.py
  planet_poles['Earth']              points outside constants_new.py
  planet_poles['Jupiter']            points outside constants_new.py
  planet_poles['Saturn']             points outside constants_new.py
  planet_poles['Sun']                points outside constants_new.py

Report only, nothing written: 0 field(s) would change across 0 served link(s); 28 fallback, 5 outside the store.

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

**3. Pause OneDrive syncing.**

**4. Rebuild the served cache**, the way you normally run the cache builder. This is the step that matters most, because the rooms draw their shells from the cache and not from the config. Afterwards, Earth's eight new `altitude` and `radius_km` entries should be in both `data/solar-system/coverage_index.json` and `feature_configs.json`.

[RECOVER] removed retained data\solar-system.prev (cleared read-only on 6 entries)
[sweep] kept 1 recent sibling(s) as autopsies: .staging_solar-system_20260917T234936Z
[ABORT] fail: swap raised: [WinError 5] Access is denied: 'data\\.staging_solar-system_20260920T150019Z' -> 'data\\solar-system' -- no commit; next run will self-heal

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

**Tony**
STOPPED. THE CACHE BUILD PUSH NOT DONE. THE COMMIT IS DEFECTIVE. 

before proceeding, this is what i did:

stopped the sync
ran the cache builder
restarted the sync
stopped the sync again because i realized that the commit might conflict
started the commit then stopped when i saw it was malformed every step was immediately after the previous. no significant time lag.

**Opus**
Good — that changes one step and removes another.

The sync being paused right now is the state you want, and it has been paused for some minutes, which is the settling time I was asking for. So you do not need to pause it again. Skip that part.

My point about step 3 was smaller than I made it sound: you resumed the sync briefly and then paused it again before staging anything, so OneDrive had very little chance to do anything to the wreckage. And it does not matter either way, because those files are about to be discarded.

What still stands is the settling explanation for the swap failure itself. Between your step 1 and step 2 there was no gap, and the builder writes hundreds of files and then renames the folder a moment later. Whatever still had that tree open — OneDrive finishing up, Defender scanning what was just written, the indexer — is what the rename hit. A pause stops transfers; it does not close handles that are already open.

## Where that leaves the recovery

**1.** Commit only the six non-cache files. Do not push. -- done

**2.** Discard everything still showing. -- done

**3.** Before re-running the builder, close any File Explorer window sitting inside `data\solar-system`, any VS Code tab on a file in there, and any browser on the local server. Leave the sync exactly as it is — paused.

**4.** Run the builder.

[RECOVER] removed retained data\solar-system.prev (cleared read-only on 6 entries)
[sweep] kept 2 recent sibling(s) as autopsies: .staging_solar-system_20260917T234936Z, .staging_solar-system_20260920T150019Z
[ABORT] fail: swap raised: [WinError 5] Access is denied: 'data\\.staging_solar-system_20260920T165747Z' -> 'data\\solar-system' -- no commit; next run will self-heal

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

STOPPED: THE COMMIT IS STILL MALFORMED. 

Rename the folder you already have.

The builder finished its work both times. It fetched, built and validated a complete generation, wrote its run manifest into it, and then failed on the last step — a single directory rename. Running it again repeats an hour of fetching to arrive at exactly the same folder you are already holding, and hands the same rename to the same lock. That is a third attempt at something that has failed twice.

There is also a cost to re-running that is easy to miss: each run leaves another staging folder behind, and you now have three. A fourth makes it harder to be sure which one you are renaming, and picking the wrong one is the only way this recovery can go wrong.

So the order stands:

1. Let the upload finish. -- done
2. Pause OneDrive for 8 or 24 hours, not 2. -- 24 hours
3. Rename `.staging_solar-system_20260920T165747Z` to `solar-system`. 
4. Run the maintenance run.

The maintenance run is what verifies the hand-moved generation, and it costs seconds rather than an hour. If **Cache in step** and **Display figures** both come back green, the cache is correct and you can commit. If either is red, send it to me — and only then would rebuilding be the right move, because at that point we would know something is actually wrong with the generation rather than with the rename.

Your screenshot answers the question. **None of those folders is named `solar-system`** — that one is genuinely missing, which is what we expected. The ones with numbers after them are not the builder's work at all.

Here is what each is:

- **`.staging_solar-system_20260920T165747Z`** — this is the one. The new generation from the run that failed at 11:57 this morning.
- `.staging_solar-system_20260920T150019Z` — the first failed run today, 10:00 AM. An autopsy.
- `.staging_solar-system_20260917T234936Z` — the 9/17 failure. An autopsy.
- `solar-system.prev` — your one-generation rollback. Leave it alone.
- **`solar-system (1)`, `solar-system (2)`, `solar-system (3)`, `1260806133443-solar-system`** — these are OneDrive conflict copies, from 9/5, 9/10, 9/18 and 9/6. The builder never creates a name like that. OneDrive makes them when it cannot reconcile a folder and gives up.

That last group is worth pausing on, because it is new evidence and it is not good news. OneDrive has been making duplicate copies of this exact directory for over two weeks. That is the same lock fighting the same folder, showing up in a different way. One of them, `1260806133443-solar-system`, was committed to the repository at some point and is sitting on the live site now.

## Do this

1. Rename **`.staging_solar-system_20260920T165747Z`** to **`solar-system`**. -- done
2. Run `gallery_maintenance_run.py` and send me the result.

Leave everything else exactly where it is. Do not delete the numbered folders yet — they are harmless where they sit, and I would rather sort out the cache before touching anything else in that directory.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.1s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     0.6s  rewrote data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite       7.5s  PASS (167 checks, 0 failures)
  PASS Mirror suite              0.1s  All 42 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing.
  PASS Store writer suite        3.1s  All 245 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 246 store-editor checks
                                    passed: every box the form offers
                                    is one the writer allows; the word
                                    list and the tick list differ by
                                    the belts, on purpose; nothing
                                    typed saves nothing; the save
                                    message does not promise a visitor
                                    sees what they cannot yet; and a
                                    red Cache in step is explained
                                    rather than just shown.
  PASS Config mirror check       0.1s  Every served link holds the
                                    export's value, unit and figure
                                    count; 45 link(s) compared, store
                                    248541a9ba5d.
  PASS Pointer join              0.1s  Every link is accounted for: 78
                                    link(s) against orrery b3faf14f,
                                    28 fallback named.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's features exactly: 4
                                    object(s), 34 named shell(s), in
                                    both cache files.
  PASS Feature renderers         0.9s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.1s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.1s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 55 hover(s) and 240
                                    number(s) examined; 12 graded, 43
                                    held to the fixture ===
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: 2 sibling(s), none stale.
                                    The sweep is keeping up.

======================================================================
  15 of 15 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: 2 sibling(s), none stale. The
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

Green across the board. The hand-moved generation is verified — **Cache in step** confirms the served cache holds the config's features exactly, and **Display figures** passes, which means the numbers a visitor will read are right.

That the rename worked in Explorer is itself useful: the lock is transient and timing-bound, not something permanently holding that folder. The fix for it is a retry loop around the swap, which is a small change to one function. That is for later, not now.

## Commit and push

Keep OneDrive paused through all of this.

**1. Check the change list before you commit.** It should contain only these:

- everything under `data\solar-system\`
- `data\constants_export.sha` — the export pull advanced it to `b3faf14f`, as expected. The export's contents are unchanged; only the recorded SHA moved.
- `MODULE_ATLAS.md` and `MODULE_INDEX.md`, if the generator touched them -- correct

If anything else appears — in particular anything under a `solar-system (1)`, `(2)`, `(3)` or `1260806133443-solar-system` folder — stop and tell me before committing. Those are the OneDrive conflict copies and they must not go to the site.

Clean. The top four are exactly what they should be — `constants_export.sha`, `coverage_index.json`, `feature_configs.json`, `positions\voyager_1.json` — and no conflict-copy folder is in the list.

Commit and push.

Then `gallery_maintenance_run.py --live`, resume OneDrive, and take a look at Earth's room on your phone. The upper atmosphere should read 600 km where it said 574, and the outer core 3,480.0 km.

**2. Commit all of it** with a summary naming the cache rebuild. -- done

**3. Push.** This sends both commits: the L342 commit you made earlier and this one. That is the config and the cache reaching the remote together, which is the whole point of the sequence. -- done

The push landed and the site has the right data. Remote HEAD is `1061ae4d9ad3b7a9b86b483b09db7f9cbd64eed2`, matching your commit, and I pulled that commit down and checked the served cache directly: all eight new entries are there, in `coverage_index.json`, which is the file the browser fetches. The upper atmosphere's altitude reads 600 km at two figures.

That is the round trip closed. The config and the cache went out together.

## What's left

1. **Run the live pass.** `gallery_maintenance_run.py --live`.
2. **Resume OneDrive.**
3. **Look at Earth's room on your phone.** Upper atmosphere at 600 km, outer core at 3,480.0 km.
4. **Then the orrery ledger patch**, when you're ready — `patch_L342_3_ledger_display_figures_20260920.py` from the orrery root, then `ledger_index.py`, then the orrery maintenance run, then commit and push.

One small thing in the diff, so it isn't a puzzle later. `MODULE_ATLAS.md` dropped from 38 modules to 37 and stopped listing `patch_L342_5_panel_notes_repair_20260919.py`. That is the atlas catching up on a move that already happened — yesterday's patch script was filed into `documentation/`, and the atlas only learns about it when the maintenance run regenerates it. Nothing was lost; the generator is simply current again.

**4. Run the live pass.** `gallery_maintenance_run.py --live`.

======================================================================
  gallery maintenance run -- LIVE (after a push)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

LIVE -- what the deployed site actually serves

  fetching 11 files from https://palomasorrery.com/
    SERVED   interactive.html                               matches the working copy
    SERVED   gallery/feature_renderers.js                   matches the working copy
    SERVED   gallery/earth_geometry.js                      matches the working copy
    SERVED   gallery/assembler/resolver.py                  matches the working copy
    SERVED   gallery/assembler/__init__.py                  matches the working copy
    SERVED   data/solar-system/coverage_index.json          matches (the working copy is CRLF)
    SERVED   data/solar-system/feature_configs.json         matches (the working copy is CRLF)
    SERVED   data/solar-system/positions/voyager_1.json     matches the working copy
    SERVED   gallery/arrival.js                             matches the working copy
    SERVED   gallery/nav_cluster.js                         matches the working copy
    SERVED   data/objects_config.json                       matches the working copy

  PASS Served reachability       1.7s  all 11 files served and
                                    byte-identical to the working copy

  orrery export pinned at b3faf14f

  PASS Export freshness          0.1s  the served export is the orrery's
                                    at b3faf14f, byte for byte

  orrery HEAD b3faf14f
  examining 33 of 78 links; the other 45 are served from the export
    NOT IN STORE  create_sun_galactic_tide default not a top-level constant in the store
                  /objects/0/features/oort_cloud/galactic_tide/typical_radius
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NO UNIT       EARTH_MAGNETOPAUSE_SHUE_A6       the constant's name declares no unit
                  /objects/1/features/earth_magnetosphere/magnetopause/surface/a6
    NO UNIT       EARTH_MAGNETOPAUSE_SHUE_A8       the constant's name declares no unit
                  /objects/1/features/earth_magnetosphere/magnetopause/surface/a8
    NO UNIT       EARTH_BOW_SHOCK_JELINEK_EPS      the constant's name declares no unit
                  /objects/1/features/earth_magnetosphere/bow_shock/surface/epsilon
    NO UNIT       EARTH_BOW_SHOCK_JELINEK_LAMBDA   the constant's name declares no unit
                  /objects/1/features/earth_magnetosphere/bow_shock/surface/lambda
    NOT IN STORE  planet_poles['Earth']            not a top-level constant in the store
                  /objects/1/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  33 pointers: 24 match, 0 DRIFT, 0 UNIT MISMATCH, 9 could not be examined.

  PASS Store drift               0.6s  33 pointers against orrery
                                    b3faf14f -- 24 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 9 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            33 pointers against orrery b3faf14f --
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

**5. Resume OneDrive** once the push is done.

**6. Look at Earth's room on your phone.** The two quickest tells are the upper atmosphere, which should read 600 km where it said 574, and the outer core at 3,480.0 km.

**5.** Keep the sync paused through the maintenance run, the commit and the push. Resume it only once both commits are on the remote.

The difference from the failed attempt is the settling time, and you already have it.

**5. Resume OneDrive** once the swap has finished.

**6. Run the maintenance run.** Open `gallery_maintenance_run.py` and Run.

Expect: `15 of 15 gating checkers passed`, which is one more row than before. The two to look at by name are **Cache in step** and **Display figures**. If Display figures is red and says the cache and the config build different hovers, step 4 did not complete — run it again rather than pushing.

Expect one file to change that you did not edit: `data/constants_export.sha`. The run pulls the export at orrery HEAD, and that moved when you filed the manifest. The export's contents are identical; only the recorded SHA advances.

**7. File the patch.** Move `patch_L342_2_display_figures_20260920.py` into `documentation/`.

**8. Commit and push** in GitHub Desktop. Commit the config and the cache **together** in one commit. That is the 2026-09-17 lesson: a config that goes out ahead of its cache breaks both rooms while every check passes.

**9. Run the live pass.** `gallery_maintenance_run.py --live`.

**10. Look at Earth's room on your phone**, with the table in section 2 of the handoff beside you. The two quickest tells are the upper atmosphere, which should read 600 km where it said 574, and the outer core, which should read 3,480.0 km.

## Orrery repo

**11. Install the ledger patch.** Save `patch_L342_3_ledger_display_figures_20260920.py` into the orrery repo root, next to `palomas_orrery.py`. Open it in VS Code and click Run.

**12. Rebuild the ledger index.** Open `ledger_index.py` and Run. Expect it to parse cleanly and regenerate the index.

**13. Run the orrery maintenance run.**

**14. File and push.** Move the script into `documentation/`, then commit and push.

Both patches refuse to run twice and write nothing at all if an anchor does not match, so a failed step leaves the working copy exactly as it was. Undo at any point is Discard Changes in GitHub Desktop.