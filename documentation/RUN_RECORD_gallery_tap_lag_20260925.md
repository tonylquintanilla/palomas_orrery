# Run record -- the phone tap lag: Plotly's marker box took about 12 seconds to close

**Built on gallery `199b8d9fc9de65154e23c47f33e16641f7ff1047` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io**, read live
on 2026-09-25. **Patch:** `patch_gallery_tap_lag_marker_box_20260925.py`.
**Rules:** gallery-assembler 1.3 (Mode 5 as measurement; never mutate a
plot from inside a Plotly event; read Plotly's bundle rather than
theorise), interactive-exhibit 1.4, safe-file-editing 1.11.

**Ledger:** no handle yet. L-344 is taken; the next free handle at orrery
`62e93856` is L-363. One row, for Tony to file.

## What Tony saw

On his phone, 2026-09-25, after patch D7: tapping the rotation axis's
marker opens Plotly's own hover box; tapping elsewhere to close it took
about 12 seconds (his measurement). The same text opened from the drawer
closes at once.

## What causes it, read from Plotly 2.35.2 and measured

Read from the unminified `plotly.js` 2.35.2 bundle (`npm pack
plotly.js-dist@2.35.2`), `src/plots/gl3d/scene.js` render:

- The hover box is redrawn on every render from gl-plot3d's current pick,
  and on a touch screen ("tablet mode", set by any touchstart on the
  canvas) the same render EMITS `plotly_click` again whenever the pick is
  within 5 px. So while the tapped marker stays picked, every redraw is a
  new click.
- gl-plot3d moves the pick only when the browser sends a mouse event
  (`mouse-change`). A phone sends synthetic mouse events for a tap, but
  whether and when it does for the tap meant to close the box is up to the
  browser.
- The page answers each `plotly_click` by focusing that shell, which
  re-frames the view with a relayout, which redraws, which clicks again.

Measured headless: the live Earth room, loaded in Chromium with WebGL
(SwiftShader) at a 390 x 844 phone size with touch, the real
`interactive.html`, `feature_renderers.js` and `earth_geometry.js`,
Plotly 2.35.2, and Pyodide replaced by the recorded Earth payload plus the
served pole of date. The marker was found by scanning gl-plot3d's own
pick (Earth's axis marker, trace 42). With the pick held as a phone holds
it:

| | clicks in 10 s | re-framings in 10 s | a closing tap with no mouse event |
|---|---|---|---|
| live page (`199b8d9f`) | 127 | 63, without end | box still up; the test could not finish |
| with the patch | 3 | 1 | box gone in 0.14 s |

The Sun room with the patch: 3 clicks, 1 re-framing in 8 s, closed in
0.11 s. A screenshot of the held box matches Tony's IMG_1564.

What this does not prove: that iOS Safari holds the pick exactly as the
emulation does. The loop is Plotly's and the page's code, and runs on any
browser that keeps the pick; the 12 seconds is what that loop costs on
Tony's phone. His phone is the test.

## The fix

In `interactive.html`:

1. The `plotly_click` handler acts once per press. A press is counted at
   `pointerdown` in the plot; repeated clicks from the same press are
   ignored.
2. Every new press in the plot drops gl-plot3d's pick itself -- the same
   fields its own mouse handler clears -- and asks for a redraw, so
   `scene.js` removes the box and emits `plotly_unhover`. If the press
   lands on a marker, the browser's events pick it again. This reaches
   into the pinned Plotly's internals, as `sunTapPicking` already does,
   and does nothing if they are not where 2.35.2 keeps them. It runs in a
   DOM handler, not a Plotly event, and calls no `Plotly.*` function.

## Tests

- Every offline checker of the maintenance run passes with the patch.
- The patch applied to a fresh clone of `199b8d9f` gives a byte-identical
  page; a second run refuses and writes nothing.
- No permanent check was added for the loop: it needs a browser with
  WebGL, which the maintenance run does not have. One ledger class: phone
  behaviour of the rooms has no automated check.

## Tony's run

Pushed at gallery `ce09f789921521b49643290015af6cd1ba21e038`. Tony's
output is below the line. Read by Claude Opus 5.5:

- The patch applied: one ok line, three edits. Offline run 16 of 16
  gating; live run 2 of 2, all 11 served files byte-identical.
- Mode 5, Tony's phone, 2026-09-25: in the Earth room, a tap on the
  axis's marker then a tap on empty space closes the box at once; the
  same after waiting ten seconds with the box up; the same with a marker
  in the Sun room. Tony: "all correct". The 12-second lag is gone.

---

---

Written September 25, 2026 with Anthropic's Claude Opus 5.5.

=======================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_gallery_tap_lag_marker_box_20260925.py
  ok  interactive.html: 3 edit(s)

PATCH APPLIED

NEXT STEPS
  1. Run gallery_maintenance_run.py with the Run button. No cache
     build is needed.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.1s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     1.8s  no change to
                                    data/constants_export.json,
                                    data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      10.4s  PASS (210 checks, 0 failures)
  PASS Pole of date              0.2s  POLE OF DATE: all 11 checks passed
                                    (frame angle, orrery, ERFA, block
                                    checker, and each shown able to
                                    fail).
  PASS Mirror suite              0.1s  All 42 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing.
  PASS Store writer suite        3.0s  All 245 store-writer checks
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
                                    count; 58 link(s) compared, store
                                    6d4bb4fd4f54.
  PASS Pointer join              0.1s  Every link is accounted for: 87
                                    link(s) against orrery 62e93856,
                                    24 fallback named; read check: 41
                                    of 41 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's features exactly: 4
                                    object(s), 34 named shell(s), in
                                    both cache files.
  PASS Feature renderers         0.1s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.1s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.1s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.1s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 56 hover(s) and 270
                                    number(s) examined; 13 graded, 4
                                    graded by line, 43 held to the
                                    fixture ===
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: no sibling directories and
                                    nothing in data/ the builder did
                                    not make.

======================================================================
  16 of 16 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: no sibling directories and
  last swap 2026-09-25T18:42:47.090627+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  2. Commit and push, -- ce09f789921521b49643290015af6cd1ba21e038

  3. then run the live check as before.

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

  PASS Served reachability       2.4s  all 11 files served and
                                    byte-identical to the working copy

  orrery export pinned at 62e93856

  PASS Export freshness          0.4s  the served export is the orrery's
                                    at 62e93856, byte for byte

  orrery HEAD 62e93856
  examining 29 of 87 links; the other 58 are served from the export
    NOT IN STORE  create_sun_galactic_tide default not a top-level constant in the store
                  /objects/0/features/oort_cloud/galactic_tide/typical_radius
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NOT IN STORE  planet_poles['Earth']            not a top-level constant in the store
                  /objects/1/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  29 pointers: 24 match, 0 DRIFT, 0 UNIT MISMATCH, 5 could not be examined.

  PASS Store drift               1.1s  29 pointers against orrery
                                    62e93856 -- 24 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 5 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            29 pointers against orrery 62e93856 --
  last swap 2026-09-25T18:42:47.090627+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  4. On your phone, in the Earth room: tap the axis's marker, then
     tap empty space. The box should close at once. Tap the marker
     and wait ten seconds before closing; it should still close at
     once. Do the same with a marker in the Sun room. -- all correct
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

===============================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L283_2_wall_art_label_20260925.py
  ok  Google's label read from Gemini_palomas_orrery_logo.png (796 bytes)
  ok  label placed after the JFIF header; image data unchanged
  ok  the result is the file that was tested
  wrote palomas_orrery_wall.jpg (97516 bytes, was 96687)

patch applied to 1 file

WHAT TO DO NEXT, in this order:

  1. Move THIS script into documentation/. It has run. -- done
  2. Run the gallery maintenance run:
         python gallery_maintenance_run.py
     Expect every gating checker to pass, as before.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.2s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     1.0s  no change to
                                    data/constants_export.json,
                                    data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      11.0s  PASS (210 checks, 0 failures)
  PASS Pole of date              0.2s  POLE OF DATE: all 11 checks passed
                                    (frame angle, orrery, ERFA, block
                                    checker, and each shown able to
                                    fail).
  PASS Mirror suite              0.1s  All 42 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing.
  PASS Store writer suite        3.0s  All 245 store-writer checks
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
                                    count; 58 link(s) compared, store
                                    6d4bb4fd4f54.
  PASS Pointer join              0.1s  Every link is accounted for: 87
                                    link(s) against orrery 62e93856,
                                    24 fallback named; read check: 41
                                    of 41 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's features exactly: 4
                                    object(s), 34 named shell(s), in
                                    both cache files.
  PASS Feature renderers         0.8s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.2s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.1s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 56 hover(s) and 270
                                    number(s) examined; 13 graded, 4
                                    graded by line, 43 held to the
                                    fixture ===
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: no sibling directories and
                                    nothing in data/ the builder did
                                    not make.

======================================================================
  16 of 16 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: no sibling directories and
  last swap 2026-09-25T18:42:47.090627+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  3. In GitHub Desktop the change list should show exactly two
     files: palomas_orrery_wall.jpg and this script under
     documentation/. Commit and push. -- 1a816f24ddd04f0e60f97ac88f4da78730a47d23
  4. After the push: python gallery_maintenance_run.py --live

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

  PASS Served reachability       3.3s  all 11 files served and
                                    byte-identical to the working copy

  orrery export pinned at 62e93856

  PASS Export freshness          0.1s  the served export is the orrery's
                                    at 62e93856, byte for byte

  orrery HEAD 62e93856
  examining 29 of 87 links; the other 58 are served from the export
    NOT IN STORE  create_sun_galactic_tide default not a top-level constant in the store
                  /objects/0/features/oort_cloud/galactic_tide/typical_radius
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NOT IN STORE  planet_poles['Earth']            not a top-level constant in the store
                  /objects/1/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  29 pointers: 24 match, 0 DRIFT, 0 UNIT MISMATCH, 5 could not be examined.

  PASS Store drift               0.9s  29 pointers against orrery
                                    62e93856 -- 24 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 5 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            29 pointers against orrery 62e93856 --
  last swap 2026-09-25T18:42:47.090627+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  5. On the phone, after about ten minutes, close the page and
     open it again: the lobby should look exactly as before. -- yes
  6. Tell Claude the new gallery SHA.

TONY-ACTION ROLLUP for this patch:
  (do)     steps 1 to 6 above.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 


