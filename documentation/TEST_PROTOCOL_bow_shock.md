TEST PROTOCOL -- Bow Shock Build (Movement 1)
Tony + Claude | June 2, 2026 | base SHA a57aeb9 + bow-shock delta

SCOPE
Nine changed files:
  planet_visualization_utilities.py        (new shared create_bow_shock_shape)
  mercury/venus/earth/mars _visualization_shells.py   (inline shock -> shared conic call)
  jupiter/saturn/uranus/neptune _visualization_shells.py (new conic shock in magnetosphere builder)
  neptune_visualization_shells.py also: magnetopause sunward_distance 34 -> 26.5
This is a DATA-CONTENT sweep (new/changed traces, marker styling, hover text),
not control flow. py_compile alone is NOT sufficient -- an untouched file
compiles as cleanly as a correct one. Run the smoke test (Layer 1).

Division of labor: Claude did Layers 0-1 in the container (all PASS). You own
Layers 2-3 -- full-app launch on Windows and the Mode-5 visual gate, which is
where this build actually lives.

Plan's sound, and the order is right — test before promoting, push before syncing, expunge before sync so the connector can't sit beside stale manual copies. Four flags, in rough order of how much they'd bite:

Push, not just commit, before you sync project knowledge. The GitHub connector pulls from the remote repo, not your local commit. In GitHub Desktop, commit and push are separate actions — if step 4 commits locally but the push hasn't landed, your step-6 sync pulls the old remote HEAD and project knowledge comes back stale relative to the very files you just tested. So between "commit" and "sync," confirm the push actually completed and remote HEAD advanced. This is the one new ordering slip the connector pipeline introduces.

In the sandbox, read the loaded-file audit block before trusting the smoke result. That's the whole reason it's there. The sandbox has archived copies, so the audit's job is to show you that earth_visualization_shells.py et al. resolved to the live sandbox-root paths and not an archive\ twin. Layer 0 was clean, so the canonical copies are fresh — the audit just confirms the test loaded those. Glance at the top ten lines; if every path is the sandbox root, you're good.  -- pass

Optional but cheap: re-run the 10-second smoke once more in the local repo after you copy, before you push. The audit then prints repo paths instead of sandbox paths — a clean-location confirmation — and it catches a faithless copy (a file that didn't make it across, or got truncated). It's the "test against ground truth" move applied to the promotion step itself. Skip it if the copy is a simple file-overwrite you trust; include it if you want the promote step verified, not assumed. -- pass

Don't expect expunge to clear the before_none ghost. That file already survived a full project-knowledge replacement, so a UI expunge may not evict it either — it's a platform-side artifact, not a document you can delete. If it still surfaces in search after expunge-and-sync, that's expected and harmless now (project knowledge is orientation-only), and it stays a thumbs-down-to-Anthropic item rather than anything you chase. -- done 

After the push, grab the new HEAD SHA — that's the token for the v24 handoff ("bow-shock build pushed at <SHA>"), and the anchor the next session pulls against. With that, the loop is fully closed: tested at the source, promoted to the clean repo, project knowledge rebuilt as a projection of it, and the next session opens on a known hash. Your Mode-5 verdict is the only substantive thing still outstanding. -- not clear where to get the SHA. the project knowledge has been synced with GitHub repo.

----------------------------------------------------------------------
LAYER 0 -- File integrity [CRITICAL]   (~1 min) -- pass
----------------------------------------------------------------------
After copying the 9 files into the local repo, from the repo root:

  python -m py_compile planet_visualization_utilities.py mercury_visualization_shells.py venus_visualization_shells.py earth_visualization_shells.py mars_visualization_shells.py jupiter_visualization_shells.py saturn_visualization_shells.py uranus_visualization_shells.py neptune_visualization_shells.py

Expect: no output (clean). Then confirm ASCII/LF (Windows can inject CRLF/BOM
on copy):
  - no file should contain non-ASCII except the pre-existing em-dash at
    planet_visualization_utilities.py (one line, not from this build).

output: -- pass
C:\Users\tonyq\OneDrive\Desktop\python_work\orrery>python -m py_compile planet_visualization_utilities.py mercury_visualization_shells.py venus_visualization_shells.py earth_visualization_shells.py mars_visualization_shells.py jupiter_visualization_shells.py saturn_visualization_shells.py uranus_visualization_shells.py neptune_visualization_shells.py

C:\Users\tonyq\OneDrive\Desktop\python_work\orrery>

----------------------------------------------------------------------
LAYER 1 -- Live-dispatch smoke [CRITICAL]   (~10 sec) -- pass
----------------------------------------------------------------------
Drop smoke_bow_shock.py in the repo root and run:
  python smoke_bow_shock.py

Expect: "SMOKE RESULT: ALL PASS", exit 0. Per body: geo=1, info=1, pts=900,
finite=True. The giants print shock-vs-magnetosphere sunward extent; Neptune
is EXPECTED to show "tilted envelope pokes past shock nose" -- that is the
known Movement-2 item, not a failure.

This reproduces, on YOUR integrated files, the dispatch check Claude ran:
each magnetosphere builder resolved via its CUSTOM_SHELLS string (the live
path), called, traces inspected. If this disagrees with Claude's handoff, the
smoke test wins and the handoff is wrong.

output:
PS C:\Users\tonyq\OneDrive\Desktop\python_work\orrery> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/orrery/smoke_bow_shock.py
LOADED-FILE AUDIT (confirm these are the LIVE copies, not archived)
  run-dir on import path: c:\Users\tonyq\OneDrive\Desktop\python_work\orrery
    shell_configs                      c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\shell_configs.py
    planet_visualization_utilities     c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\planet_visualization_utilities.py
    mercury_visualization_shells       c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\mercury_visualization_shells.py
    venus_visualization_shells         c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\venus_visualization_shells.py
    earth_visualization_shells         c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\earth_visualization_shells.py
    mars_visualization_shells          c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\mars_visualization_shells.py
    jupiter_visualization_shells       c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\jupiter_visualization_shells.py
    saturn_visualization_shells        c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\saturn_visualization_shells.py
    uranus_visualization_shells        c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\uranus_visualization_shells.py
    neptune_visualization_shells       c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\neptune_visualization_shells.py

[Mercury ] create_mercury_magnetosphere_shell geo=1 info=1 pts=900 finite=True nest=True -> PASS
[Venus   ] create_venus_magnetosphere_shell   geo=1 info=1 pts=900 finite=True nest=True -> PASS
[Earth   ] create_earth_magnetosphere_shell   geo=1 info=1 pts=900 finite=True nest=True -> PASS
[Mars    ] create_mars_magnetosphere_shell    geo=1 info=1 pts=900 finite=True nest=True -> PASS
[Jupiter ] create_jupiter_magnetosphere       geo=1 info=1 pts=900 finite=True nest=True -> PASS
[Saturn  ] create_saturn_magnetosphere        geo=1 info=1 pts=900 finite=True nest=True -> PASS
[Uranus  ] create_uranus_magnetosphere        geo=1 info=1 pts=900 finite=True nest=True -> PASS
[Neptune ] create_neptune_magnetosphere       geo=1 info=1 pts=900 finite=True nest=True -> PASS
           note: magnetosphere off-axis flank reaches 0.009300 AU > shock nose 0.005777 AU (tilted envelope; Mode-5 / Movement-2, not a nest failure)

SMOKE RESULT: ALL PASS
PS C:\Users\tonyq\OneDrive\Desktop\python_work\orrery> 

----------------------------------------------------------------------
LAYER 2 -- Full-app pre-test   (~2 min) -- pass
----------------------------------------------------------------------
  python -m py_compile palomas_orrery.py        # not edited, but cheap gate
  python palomas_orrery.py                       # launch on Windows directly
On Windows you do NOT apply the SystemButtonFace -> gray90 swap (that is the
Linux/macOS workaround only). Confirm the GUI launches, no import errors in
the console, and you can select a planet and plot. Watch the console for any
caught-and-printed exception during a plot -- a swallowed exception is where a
dropped marker hides (protocol: Verify Execution). 

output: 
C:\Users\tonyq\OneDrive\Desktop\python_work\orrery>python -m py_compile palomas_orrery.py

C:\Users\tonyq\OneDrive\Desktop\python_work\orrery>

output:
PS C:\Users\tonyq\OneDrive\Desktop\python_work\orrery> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/orrery/smoke_bow_shock.py
LOADED-FILE AUDIT (confirm these are the LIVE copies, not archived)
  run-dir on import path: c:\Users\tonyq\OneDrive\Desktop\python_work\orrery
    shell_configs                      c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\shell_configs.py
    planet_visualization_utilities     c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\planet_visualization_utilities.py
    mercury_visualization_shells       c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\mercury_visualization_shells.py
    venus_visualization_shells         c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\venus_visualization_shells.py
    earth_visualization_shells         c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\earth_visualization_shells.py
    mars_visualization_shells          c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\mars_visualization_shells.py
    jupiter_visualization_shells       c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\jupiter_visualization_shells.py
    saturn_visualization_shells        c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\saturn_visualization_shells.py
    uranus_visualization_shells        c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\uranus_visualization_shells.py
    neptune_visualization_shells       c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\neptune_visualization_shells.py

[Mercury ] create_mercury_magnetosphere_shell geo=1 info=1 pts=900 finite=True nest=True -> PASS
[Venus   ] create_venus_magnetosphere_shell   geo=1 info=1 pts=900 finite=True nest=True -> PASS
[Earth   ] create_earth_magnetosphere_shell   geo=1 info=1 pts=900 finite=True nest=True -> PASS
[Mars    ] create_mars_magnetosphere_shell    geo=1 info=1 pts=900 finite=True nest=True -> PASS
[Jupiter ] create_jupiter_magnetosphere       geo=1 info=1 pts=900 finite=True nest=True -> PASS
[Saturn  ] create_saturn_magnetosphere        geo=1 info=1 pts=900 finite=True nest=True -> PASS
[Uranus  ] create_uranus_magnetosphere        geo=1 info=1 pts=900 finite=True nest=True -> PASS
[Neptune ] create_neptune_magnetosphere       geo=1 info=1 pts=900 finite=True nest=True -> PASS
           note: magnetosphere off-axis flank reaches 0.009300 AU > shock nose 0.005777 AU (tilted envelope; Mode-5 / Movement-2, not a nest failure)

SMOKE RESULT: ALL PASS
PS C:\Users\tonyq\OneDrive\Desktop\python_work\orrery> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/orrery/palomas_orrery.py
Working directory set to: c:\Users\tonyq\OneDrive\Desktop\python_work\orrery
Interpreter: C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe
Working directory: c:\Users\tonyq\OneDrive\Desktop\python_work\orrery
Window config file: c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\window_config.json
Restored window geometry: 1536x793+0+5
Window will be maximized
[STARTUP] Backup created: data/orbit_paths_backup.json (123.6MB)
[CACHE INFO] Total orbits cached: 1498
[CACHE INFO] To manually delete cache, remove 'data/orbit_paths.json' file

============================================================
LOADING ORBIT CACHE FROM: data/orbit_paths.json
============================================================

Cache loaded successfully: 1498 valid entries

[CACHE HEALTH SUMMARY]
Total cached orbits: 1498
Orbits by center object:
  3I/ATLAS: 5 orbits
  Apophis: 2 orbits
  Arrokoth: 4 orbits
  Bennu: 2 orbits
  Bennu/OSIRIS: 1 orbits
  Earth: 134 orbits
  Earth-Moon Barycenter: 3 orbits
  Eris: 2 orbits
  Eris-Dysnomia Barycenter: 4 orbits
  Eris/Dysnomia: 101 orbits
  Haumea: 11 orbits
  Haumea System Barycenter: 3 orbits
  Juno: 4 orbits
  Jupiter: 104 orbits
  K1: 2 orbits
  K1-B: 1 orbits
  K1-C: 1 orbits
  K1-D: 1 orbits
  L1: 2 orbits
  L2: 3 orbits
  Leucus: 1 orbits
  Makemake: 1 orbits
  Mars: 106 orbits
  Menoetius: 2 orbits
  Mercury: 102 orbits
  Moon: 112 orbits
  Neptune: 101 orbits
  Orcus: 3 orbits
  Orcus-Vanth Barycenter: 3 orbits
  Patroclus: 2 orbits
  Patroclus-Menoetius Barycenter: 4 orbits
  Phobos: 6 orbits
  Planet 9: 5 orbits
  Pluto: 102 orbits
  Pluto-Charon Barycenter: 9 orbits
  Polymele: 1 orbits
  Quaoar: 1 orbits
  Quaoar-Weywot Barycenter: 2 orbits
  R2: 1 orbits
  Saturn: 101 orbits
  Sun: 156 orbits
  Uranus: 101 orbits
  Vanth: 2 orbits
  Venus: 101 orbits

Note: Cache can only be manually deleted by removing 'data/orbit_paths.json' file
--------------------------------------------------
[DEBUG] Sun can be center (numeric ID: 10)
[DEBUG] Mercury can be center (numeric ID: 199)
[DEBUG] Venus can be center (numeric ID: 299)
[DEBUG] Apophis can be center (has center_id)
[DEBUG] Earth can be center (numeric ID: 399)
[DEBUG] Moon can be center (numeric ID: 301)
[DEBUG] Earth-Moon Barycenter can be center (numeric ID: 3)
[DEBUG] EM-L1 can be center (numeric ID: 3011)
[DEBUG] EM-L2 can be center (numeric ID: 3012)
[DEBUG] EM-L3 can be center (numeric ID: 3013)
[DEBUG] EM-L4 can be center (numeric ID: 3014)
[DEBUG] EM-L5 can be center (numeric ID: 3015)
[DEBUG] L1 can be center (numeric ID: 31)
[DEBUG] L2 can be center (numeric ID: 32)
[DEBUG] L3 can be center (numeric ID: 33)
[DEBUG] L4 can be center (numeric ID: 34)
[DEBUG] L5 can be center (numeric ID: 35)
[DEBUG] Bennu can be center (has center_id)
[DEBUG] Itokawa can be center (has center_id)
[DEBUG] Ryugu can be center (has center_id)
[DEBUG] Eros can be center (has center_id)
[DEBUG] Mars can be center (numeric ID: 499)
[DEBUG] Phobos can be center (numeric ID: 401)
[DEBUG] Deimos can be center (numeric ID: 402)
[DEBUG] Dinkinesh can be center (has center_id)
[DEBUG] Vesta can be center (has center_id)
[DEBUG] Donaldjohanson can be center (has center_id)
[DEBUG] Ceres can be center (has center_id)
[DEBUG] 16 Psyche can be center (has center_id)
[DEBUG] Orus can be center (has center_id)
[DEBUG] Polymele can be center (has center_id)
[DEBUG] Eurybates can be center (has center_id)
[DEBUG] Patroclus-Menoetius Barycenter can be center (numeric ID: 20000617)
[DEBUG] Patroclus can be center (has center_id)
[DEBUG] Menoetius can be center (has center_id)
[DEBUG] Leucus can be center (has center_id)
[DEBUG] Jupiter can be center (numeric ID: 599)
[DEBUG] Metis can be center (numeric ID: 516)
[DEBUG] Adrastea can be center (numeric ID: 515)
[DEBUG] Amalthea can be center (numeric ID: 505)
[DEBUG] Thebe can be center (numeric ID: 514)
[DEBUG] Io can be center (numeric ID: 501)
[DEBUG] Europa can be center (numeric ID: 502)
[DEBUG] Ganymede can be center (numeric ID: 503)
[DEBUG] Callisto can be center (numeric ID: 504)
[DEBUG] Saturn can be center (numeric ID: 699)
[DEBUG] Pan can be center (numeric ID: 618)
[DEBUG] Daphnis can be center (numeric ID: 635)
[DEBUG] Prometheus can be center (numeric ID: 616)
[DEBUG] Pandora can be center (numeric ID: 617)
[DEBUG] Mimas can be center (numeric ID: 601)
[DEBUG] Enceladus can be center (numeric ID: 602)
[DEBUG] Tethys can be center (numeric ID: 603)
[DEBUG] Dione can be center (numeric ID: 604)
[DEBUG] Rhea can be center (numeric ID: 605)
[DEBUG] Titan can be center (numeric ID: 606)
[DEBUG] Hyperion can be center (numeric ID: 607)
[DEBUG] Iapetus can be center (numeric ID: 608)
[DEBUG] Phoebe can be center (numeric ID: 609)
[DEBUG] Uranus can be center (numeric ID: 799)
[DEBUG] Ariel can be center (numeric ID: 701)
[DEBUG] Umbriel can be center (numeric ID: 702)
[DEBUG] Titania can be center (numeric ID: 703)
[DEBUG] Oberon can be center (numeric ID: 704)
[DEBUG] Miranda can be center (numeric ID: 705)
[DEBUG] Portia can be center (numeric ID: 712)
[DEBUG] Mab can be center (numeric ID: 726)
[DEBUG] Neptune can be center (numeric ID: 899)
[DEBUG] Triton can be center (numeric ID: 801)
[DEBUG] Despina can be center (numeric ID: 805)
[DEBUG] Galatea can be center (numeric ID: 806)
[DEBUG] Pluto-Charon Barycenter can be center (numeric ID: 9)
[DEBUG] Pluto can be center (numeric ID: 999)
[DEBUG] Charon can be center (numeric ID: 901)
[DEBUG] Styx can be center (numeric ID: 905)
[DEBUG] Nix can be center (numeric ID: 902)
[DEBUG] Kerberos can be center (numeric ID: 904)
[DEBUG] Hydra can be center (numeric ID: 903)
[DEBUG] Orcus-Vanth Barycenter can be center (numeric ID: 20090482)
[DEBUG] Orcus can be center (has center_id)
[DEBUG] Vanth can be center (has center_id)
[DEBUG] Haumea can be center (has center_id)
[DEBUG] Hi'iaka can be center (has center_id)
[DEBUG] Namaka can be center (has center_id)
[DEBUG] Quaoar can be center (has center_id)
[DEBUG] Weywot can be center (has center_id)
[DEBUG] Arrokoth can be center (has center_id)
[DEBUG] Makemake can be center (numeric ID: 20136472)
[DEBUG] MK2 can be center (numeric ID: 120136472)
[DEBUG] Gonggong can be center (has center_id)
[DEBUG] Xiangliu can be center (has center_id)
[DEBUG] Eris can be center (has center_id)
[DEBUG] Dysnomia can be center (has center_id)
[CENTER MENU] Dynamic center dropdown initialized (starts with Sun only)
[CENTER MENU] Added traces to 182 object variables
Restored sash positions: [529, 1013]

----------------------------------------------------------------------
LAYER 3 -- Mode 5 visual gate [the real test]   (your eyes)
----------------------------------------------------------------------
Plot each body with its magnetosphere/shells enabled. For EACH of the 8
(Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune):

  [ ] Bow shock renders -- faint peach cloud (rgb 255,200,150), small, low
      opacity. Legend entry "X: Bow Shock". -- pass: mercury, venus, earth, mars; jupiter, saturn, uranus
  [ ] Shape is CONIC -- nose toward the Sun, flaring away. (Inner four no
      longer the old paraboloid.) -- pass: mercury, venus, earth, mars, jupiter, saturn, uranus
  [ ] Nose points sunward along +X toward the Sun position. Cross-check with
      the sun-direction indicator. If a shock points the wrong way, it is a
      rotate_to_sunward / reference-frame issue (low incl = equatorial,
      high = ecliptic). -- pass: mercury, venus, earth, mars, jupiter, saturn, uranus
  [ ] Shock sits OUTSIDE the magnetopause on the sunward side (shock nose
      farther from planet than the magnetosphere boundary). -- pass: mercury, venus, earth, mars, jupiter, saturn, uranus
  [ ] One info marker (cross) at the nose. Hover shows the text; giants carry
      km AND AU. Standoff distance looks sane vs planet radius
      (Earth ~15 R_E, Jupiter ~82 R_J, etc.) -- the "kissing test" analog. -- pass: mercury, venus, earth, mars, jupiter, saturn, uranus
  [ ] Legend toggle: clicking "X: Bow Shock" hides BOTH the cloud and its
      marker together (single legendgroup). -- pass: mercury, venus, earth, mars, jupiter, saturn, uranus

Specific watch items from the build:
  [ ] EARTH changes by design -- paraboloid -> conic. This is the one body
      whose appearance differs from last session on purpose. Confirm it reads
      right, not broken. -- confirmed
  [ ] Flank flare width -- the conic flares wider than the old paraboloids
      (physically correct). If any reads too broad, the knob is in
      create_bow_shock_shape: lower a_max = a_asymptote * 0.92. One-line change,
      propagates to all 8. -- i don't have an intuition about this
  [ ] NEPTUNE -- the magnetosphere envelope pokes past the shock nose on its
      tilted (47 deg) flank (smoke confirmed). Decide if it reads acceptably or
      needs the Movement-2 cone. Expected, flagged, not a bug.
  [ ] Hover text AU convention -- the 4 INNER bodies' existing bow-shock hover
      still says "radii" only (no km/AU), unlike the giants. Known gap; say the
      word and Claude adds km/AU to the inner four. -- not an issue

Neptune:
N15 (or next free number) — Neptune ring/arc plane misframed [PRIORITY 1, next session]. Ring system oriented by hardcoded tilt_angle=32° (x) + final_orientation=34° (z), pole-derived code commented out. Measured 8.57° off Neptune's true equatorial plane (ring normal (0.296,−0.439,0.848) vs pole (0.356,−0.307,0.883)); ring tilt 32° vs true 28.0°, plus wrong azimuth. Despina/Galatea (Horizons, i≈0.05–0.07° to equator) are the correct plane; rings don't match. Neptune analog of the Uranus U3 105° fudge. Fix: migrate to orient_to_planet_pole (validated 0.0° against the Uranus moons in v23). Found by Tony's Mode-5; confirmed by computation. First action next session, BEFORE the migration: grep the other ringed bodies (Saturn, Jupiter — and re-confirm Uranus stayed fixed) for the same hardcoded-angle pattern, to size the sweep rather than patch one-off.
Two things to carry into that session so they're not lost:

The scope question is unresolved on purpose — whether this is one body or a sweep is the first thing to determine, because the answer changes whether it's a patch or a migration pass. Don't let "just fix Neptune" win by default before the grep.
The verification gate is the moons, not the smoke test — same as Uranus U3 and the magnetosphere nest. A container test can't fetch Horizons, so it'll false-pass on ring-vs-ring; your render against Despina/Galatea is the real check.

Regression (Claude moved code; confirm nothing else broke):
  [ ] URANUS radiation belts still render (Claude removed a misplaced block
      from create_uranus_radiation_belts; net should be unchanged). -- correct
  [ ] NEPTUNE magnetosphere still looks like a magnetosphere, just slightly
      smaller sunward (magnetopause 34 -> 26.5).
  [ ] Other shells of all 8 (rings, plasma torus, radiation belts, hill
      sphere) unchanged. -- pass: earth, mars, jupiter, saturn, uranus


----------------------------------------------------------------------
RECORD (carry into v24 handoff)
----------------------------------------------------------------------
- Layers 0-2 pass/fail. -- pass
- Mode-5 verdict per body; flank-flare decision (keep 1.05 / lower 0.92). -- leave
- Neptune poke-through: accept now / queue Movement-2.
- Inner-four km/AU hover: leave / fix. -- leave
- Base SHA the build was integrated onto; new HEAD SHA after your push.

other issues:
- Mercury sodium tail info marker is located at the center and is invisible if the mercury object is selected. it might be helpful to offset it. 
- it would be informative to illustrate planetary rotational axes with directional rotation arrows at the poles
- adjust venus upper atmosphere and magnetosphere hovertext to fit in the window
