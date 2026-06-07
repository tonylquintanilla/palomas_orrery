Here's a test protocol for this session's two deliverables — the dipole cone (6-file set: the 4 cone files plus the 2 hover edits) — ordered as gates, critical ones marked. The first two are fast and catch the structural failures; the render gate is where your eyes do the work the smoke can't.

**Gate 0 — Apply.** Replace the six files in the repo: `planet_visualization_utilities.py`, `shell_configs.py`, `planet_visualization.py`, `smoke_dipole_cone.py` (new), `uranus_visualization_shells.py`, `neptune_visualization_shells.py`. All built on `de12f56`. -- done

**Gate 1 — Syntax [CRITICAL, 10 sec].** `python -m py_compile` the five .py modules (not the smoke yet). Already clean my side; this just confirms the transfer didn't mangle anything. Fail here = bad copy/paste, not a logic problem. -- pass

    C:\Users\tonyq\OneDrive\Desktop\python_work\orrery>python -m py_compile planet_visualization_utilities.py shell_configs.py planet_visualization.py smoke_dipole_cone.py uranus_visualization_shells.py neptune_visualization_shells.py

    C:\Users\tonyq\OneDrive\Desktop\python_work\orrery>

**Gate 2 — Live-dispatch smoke [CRITICAL].** `python smoke_dipole_cone.py`. Expect `RESULT: PASS`. This is the gate that catches last session's failure class — it drives `create_celestial_body_visualization` with zero shells and asserts the cone actually reaches the render path for Uranus/Neptune (1 legend each) and is absent for Earth/Mars/Jupiter/Saturn. A builder that works but is never called fails *here*, not at Gate 1. If it prints any `FAIL` line, stop and send it to me.  -- pass

    PS C:\Users\tonyq\OneDrive\Desktop\python_work\orrery> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/orrery/smoke_dipole_cone.py
    body       tr  tilt_dev  sense_ok  src
    Uranus      8  7.11e-15      True  Ness et al. 1986, Voyager 2 
    Neptune     8  7.11e-15      True  Ness et al. 1989, Voyager 2 

    render path: dipole cone appears on body selection (0 shells), 1 legend each  OK
    omitted bodies (Earth/Mars/Jupiter/Saturn): no dipole cone  OK

    RESULT: PASS  (2 dipole cones wired + on-pole-tilt + correct sense + body-triggered; non-dipole bodies emit none)
    Reminder: spin/sweep-arrow rhyme and half_len_frac sizing are the Mode-5 render checks.
    PS C:\Users\tonyq\OneDrive\Desktop\python_work\orrery> 

**Gate 3 — Mode-5 render, the cone (your eyes).** Plot Uranus, then Neptune:
- The cone is there on body selection with no shells checked (it's body-triggered), as a magenta translucent double-cone (hourglass) about the spin axis, one magenta generator line, a sweep arrow at each tip. -- pass: uranus, neptune
- The gold spin arrow and the magenta sweep arrow read as **one rotation** — same sense, concentric about the spin axis. This is the whole point; it's the thing you already confirmed lands on the sketch, now check it in the real plot. -- pass: uranus, neptune
- The cone sits **square to the rings and inner belt** (shared pole frame), and tilts with the spin axis. -- pass: uranus, neptune; see images
- Legend entry "Uranus: Dipole Cone" / "Neptune: Dipole Cone" toggles the whole group on and off as a unit. -- pass: uranus, neptune
- **Watch the console** for any caught-exception print — a swallowed error can drop one trace silently (the 11-week ghost lesson). All 8 traces should be present. -- pass: uranus, neptune

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
    [DEBUG] Sun can be center (numeric ID: 10)
    [DEBUG] Uranus can be center (numeric ID: 799)
    [CENTER MENU] Dynamic centers: Sun + ['Sun', 'Uranus']
    [DEBUG] Sun can be center (numeric ID: 10)
    [DEBUG] Uranus can be center (numeric ID: 799)
    [DEBUG] Ariel can be center (numeric ID: 701)
    [CENTER MENU] Dynamic centers: Sun + ['Sun', 'Uranus', 'Ariel']
    [DEBUG] Sun can be center (numeric ID: 10)
    [DEBUG] Uranus can be center (numeric ID: 799)
    [DEBUG] Ariel can be center (numeric ID: 701)
    [DEBUG] Umbriel can be center (numeric ID: 702)
    [CENTER MENU] Dynamic centers: Sun + ['Sun', 'Uranus', 'Ariel', 'Umbriel']
    [DEBUG] Sun can be center (numeric ID: 10)
    [DEBUG] Uranus can be center (numeric ID: 799)
    [DEBUG] Ariel can be center (numeric ID: 701)
    [DEBUG] Umbriel can be center (numeric ID: 702)
    [DEBUG] Titania can be center (numeric ID: 703)
    [CENTER MENU] Dynamic centers: Sun + ['Sun', 'Uranus', 'Ariel', 'Umbriel', 'Titania']
    [DEBUG] Sun can be center (numeric ID: 10)
    [DEBUG] Uranus can be center (numeric ID: 799)
    [DEBUG] Ariel can be center (numeric ID: 701)
    [DEBUG] Umbriel can be center (numeric ID: 702)
    [DEBUG] Titania can be center (numeric ID: 703)
    [DEBUG] Oberon can be center (numeric ID: 704)
    [CENTER MENU] Dynamic centers: Sun + ['Sun', 'Uranus', 'Ariel', 'Umbriel', 'Titania', 'Oberon']
    [DEBUG] Sun can be center (numeric ID: 10)
    [DEBUG] Uranus can be center (numeric ID: 799)
    [DEBUG] Ariel can be center (numeric ID: 701)
    [DEBUG] Umbriel can be center (numeric ID: 702)
    [DEBUG] Titania can be center (numeric ID: 703)
    [DEBUG] Oberon can be center (numeric ID: 704)
    [DEBUG] Miranda can be center (numeric ID: 705)
    [CENTER MENU] Dynamic centers: Sun + ['Sun', 'Uranus', 'Ariel', 'Umbriel', 'Titania', 'Oberon', 'Miranda']
    [DEBUG] Sun can be center (numeric ID: 10)
    [DEBUG] Uranus can be center (numeric ID: 799)
    [DEBUG] Ariel can be center (numeric ID: 701)
    [DEBUG] Umbriel can be center (numeric ID: 702)
    [DEBUG] Titania can be center (numeric ID: 703)
    [DEBUG] Oberon can be center (numeric ID: 704)
    [DEBUG] Miranda can be center (numeric ID: 705)
    [DEBUG] Portia can be center (numeric ID: 712)
    [CENTER MENU] Dynamic centers: Sun + ['Sun', 'Uranus', 'Ariel', 'Umbriel', 'Titania', 'Oberon', 'Miranda', 'Portia']
    [DEBUG] Sun can be center (numeric ID: 10)
    [DEBUG] Uranus can be center (numeric ID: 799)
    [DEBUG] Ariel can be center (numeric ID: 701)
    [DEBUG] Umbriel can be center (numeric ID: 702)
    [DEBUG] Titania can be center (numeric ID: 703)
    [DEBUG] Oberon can be center (numeric ID: 704)
    [DEBUG] Miranda can be center (numeric ID: 705)
    [DEBUG] Portia can be center (numeric ID: 712)
    [DEBUG] Mab can be center (numeric ID: 726)
    [CENTER MENU] Dynamic centers: Sun + ['Sun', 'Uranus', 'Ariel', 'Umbriel', 'Titania', 'Oberon', 'Miranda', 'Portia', 'Mab']
    [PRE-FETCH] Checking osculating elements for 7 objects...
    User chose to update Ariel
    Using Horizons ID: 701 (id_type: majorbody)
    [...] Fetching osculating elements for Ariel from JPL Horizons...
    Using Horizons ID: 701 (id_type: majorbody)
    [Horizons Query] ID: 701 | Type: majorbody | Location: @799 | Date: 2026-06-06 16:36
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    [OK] Fetched elements (solution date: 2026-06-06)
    Rotated: osculating_cache_backup.json [OK] osculating_cache_backup_old.json
    Backed up: osculating_cache.json [OK] osculating_cache_backup.json
    [OK] Saved: osculating_cache.json (2-gen protected)
    [PRE-FETCH] OK: Ariel: Updated
    User chose to update Umbriel
    Using Horizons ID: 702 (id_type: majorbody)
    [...] Fetching osculating elements for Umbriel from JPL Horizons...
    Using Horizons ID: 702 (id_type: majorbody)
    [Horizons Query] ID: 702 | Type: majorbody | Location: @799 | Date: 2026-06-06 16:36
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    [OK] Fetched elements (solution date: 2026-06-06)
    Rotated: osculating_cache_backup.json [OK] osculating_cache_backup_old.json
    Backed up: osculating_cache.json [OK] osculating_cache_backup.json
    [OK] Saved: osculating_cache.json (2-gen protected)
    [PRE-FETCH] OK: Umbriel: Updated
    User chose to update Titania
    Using Horizons ID: 703 (id_type: majorbody)
    [...] Fetching osculating elements for Titania from JPL Horizons...
    Using Horizons ID: 703 (id_type: majorbody)
    [Horizons Query] ID: 703 | Type: majorbody | Location: @799 | Date: 2026-06-06 16:36
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    [OK] Fetched elements (solution date: 2026-06-06)
    Rotated: osculating_cache_backup.json [OK] osculating_cache_backup_old.json
    Backed up: osculating_cache.json [OK] osculating_cache_backup.json
    [OK] Saved: osculating_cache.json (2-gen protected)
    [PRE-FETCH] OK: Titania: Updated
    User chose to update Oberon
    Using Horizons ID: 704 (id_type: majorbody)
    [...] Fetching osculating elements for Oberon from JPL Horizons...
    Using Horizons ID: 704 (id_type: majorbody)
    [Horizons Query] ID: 704 | Type: majorbody | Location: @799 | Date: 2026-06-06 16:36
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    [OK] Fetched elements (solution date: 2026-06-06)
    Rotated: osculating_cache_backup.json [OK] osculating_cache_backup_old.json
    Backed up: osculating_cache.json [OK] osculating_cache_backup.json
    [OK] Saved: osculating_cache.json (2-gen protected)
    [PRE-FETCH] OK: Oberon: Updated
    User chose to update Miranda
    Using Horizons ID: 705 (id_type: majorbody)
    [...] Fetching osculating elements for Miranda from JPL Horizons...
    Using Horizons ID: 705 (id_type: majorbody)
    [Horizons Query] ID: 705 | Type: majorbody | Location: @799 | Date: 2026-06-06 16:36
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    [OK] Fetched elements (solution date: 2026-06-06)
    Rotated: osculating_cache_backup.json [OK] osculating_cache_backup_old.json
    Backed up: osculating_cache.json [OK] osculating_cache_backup.json
    [OK] Saved: osculating_cache.json (2-gen protected)
    [PRE-FETCH] OK: Miranda: Updated
    User chose to update Portia
    Using Horizons ID: 712 (id_type: majorbody)
    [...] Fetching osculating elements for Portia from JPL Horizons...
    Using Horizons ID: 712 (id_type: majorbody)
    [Horizons Query] ID: 712 | Type: majorbody | Location: @799 | Date: 2026-06-06 16:36
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    [OK] Fetched elements (solution date: 2026-06-06)
    Rotated: osculating_cache_backup.json [OK] osculating_cache_backup_old.json
    Backed up: osculating_cache.json [OK] osculating_cache_backup.json
    [OK] Saved: osculating_cache.json (2-gen protected)
    [PRE-FETCH] OK: Portia: Updated
    User chose to update Mab
    Using Horizons ID: 726 (id_type: majorbody)
    [...] Fetching osculating elements for Mab from JPL Horizons...
    Using Horizons ID: 726 (id_type: majorbody)
    [Horizons Query] ID: 726 | Type: majorbody | Location: @799 | Date: 2026-06-06 16:36
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    [OK] Fetched elements (solution date: 2026-06-06)
    Rotated: osculating_cache_backup.json [OK] osculating_cache_backup_old.json
    Backed up: osculating_cache.json [OK] osculating_cache_backup.json
    [OK] Saved: osculating_cache.json (2-gen protected)
    [PRE-FETCH] OK: Mab: Updated
    [get_interval_settings] Read days_to_plot: 28
    [SYSTEM SCOPE] Center: Uranus, System: solar
    Uranus: Need 0 days from 2026-07-05 00:00:00 to 2026-07-04 16:35:00
    Checking orbit data for updates to 2026-07-04...
    Skipping invalid fetch request for Uranus: 2026-07-05 00:00:00 to 2026-07-04 16:35:00
    Rotated: orbit_paths.json.backup [OK] orbit_paths.json.backup_old
    Backed up: orbit_paths.json [OK] orbit_paths.json.backup
    [OK] Saved: orbit_paths.json (2-gen protected)
    Smart fetch complete: Updated 0 orbits with minimal data fetching. Saved approximately 0.0 hours of fetch time.
    Ariel (satellite): 51 dates from 2026-06-06 16:35:00 to 2026-07-04 16:35:00 (28 days)
    Umbriel (satellite): 51 dates from 2026-06-06 16:35:00 to 2026-07-04 16:35:00 (28 days)
    Titania (satellite): 51 dates from 2026-06-06 16:35:00 to 2026-07-04 16:35:00 (28 days)
    Oberon (satellite): 51 dates from 2026-06-06 16:35:00 to 2026-07-04 16:35:00 (28 days)
    Miranda (satellite): 51 dates from 2026-06-06 16:35:00 to 2026-07-04 16:35:00 (28 days)
    Portia (satellite): 51 dates from 2026-06-06 16:35:00 to 2026-07-04 16:35:00 (28 days)
    Mab (satellite): 51 dates from 2026-06-06 16:35:00 to 2026-07-04 16:35:00 (28 days)
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]

    Current Object Positions:
    ==================================================
    Uranus          Position: (   0.000,    0.000,    0.000) AU   Distance from center: Distance data unavailable
    Ariel           Position: (   0.001,   -0.000,   -0.001) AU   Distance from center:    0.001 AU
    Umbriel         Position: (  -0.002,    0.000,    0.000) AU   Distance from center:    0.002 AU
    Titania         Position: (   0.002,   -0.001,   -0.001) AU   Distance from center:    0.003 AU
    Oberon          Position: (  -0.004,    0.001,   -0.001) AU   Distance from center:    0.004 AU
    Miranda         Position: (   0.000,    0.000,    0.001) AU   Distance from center:    0.001 AU
    Portia          Position: (  -0.000,    0.000,   -0.000) AU   Distance from center:    0.000 AU
    Mab             Position: (   0.000,   -0.000,   -0.001) AU   Distance from center:    0.001 AU
    ==================================================
    [SCALING] Uranus child 'Miranda': a=0.000868 AU, apoapsis=0.000869 AU
    [SCALING] Uranus child 'Ariel': a=0.001276 AU, apoapsis=0.001277 AU
    [SCALING] Uranus child 'Umbriel': a=0.001778 AU, apoapsis=0.001786 AU
    [SCALING] Uranus child 'Titania': a=0.002916 AU, apoapsis=0.002924 AU
    [SCALING] Uranus child 'Oberon': a=0.003900 AU, apoapsis=0.003907 AU
    [SCALING] Uranus child 'Portia': a=0.000442 AU, apoapsis=0.000443 AU
    [SCALING] Uranus child 'Mab': a=0.000654 AU, apoapsis=0.000657 AU
    [SCALING] Uranus mode: using range +/-0.005860 AU (based on children's orbits)
    Sun direction indicator: Using shell radius 0.473258273454824, scale = 0.54425 AU
    [NORMAL MODE] Using dates_lists for plot_actual_orbits
    [NORMAL MODE] Ariel: 51 dates from 2026-06-06 16:35:00 to 2026-07-04 16:35:00
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]

    Processing trajectory for 701:
    Requested epochs: 51
    Returned vectors: 51
    Direct position matches: 51
    Interpolated positions: 0
    Final coverage: 51/51 epochs
    [NORMAL MODE] Plotted Ariel orbit with 51 points
    -> Added closest plotted marker for Ariel to Uranus: 0.001276 AU on 2026-06-26 20:25:24 UTC
    [NORMAL MODE] Umbriel: 51 dates from 2026-06-06 16:35:00 to 2026-07-04 16:35:00
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]

    Processing trajectory for 702:
    Requested epochs: 51
    Returned vectors: 51
    Direct position matches: 51
    Interpolated positions: 0
    Final coverage: 51/51 epochs
    [NORMAL MODE] Plotted Umbriel orbit with 51 points
    -> Added closest plotted marker for Umbriel to Uranus: 0.001770 AU on 2026-06-07 06:01:24 UTC
    [NORMAL MODE] Titania: 51 dates from 2026-06-06 16:35:00 to 2026-07-04 16:35:00
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]

    Processing trajectory for 703:
    Requested epochs: 51
    Returned vectors: 51
    Direct position matches: 51
    Interpolated positions: 0
    Final coverage: 51/51 epochs
    [NORMAL MODE] Plotted Titania orbit with 51 points
    -> Added closest plotted marker for Titania to Uranus: 0.002909 AU on 2026-06-07 19:27:48 UTC
    [NORMAL MODE] Oberon: 51 dates from 2026-06-06 16:35:00 to 2026-07-04 16:35:00
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]

    Processing trajectory for 704:
    Requested epochs: 51
    Returned vectors: 51
    Direct position matches: 51
    Interpolated positions: 0
    Final coverage: 51/51 epochs
    [NORMAL MODE] Plotted Oberon orbit with 51 points
    -> Added closest plotted marker for Oberon to Uranus: 0.003894 AU on 2026-06-12 20:25:24 UTC
    [NORMAL MODE] Miranda: 51 dates from 2026-06-06 16:35:00 to 2026-07-04 16:35:00
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]

    Processing trajectory for 705:
    Requested epochs: 51
    Returned vectors: 51
    Direct position matches: 51
    Interpolated positions: 0
    Final coverage: 51/51 epochs
    [NORMAL MODE] Plotted Miranda orbit with 51 points
    -> Added closest plotted marker for Miranda to Uranus: 0.000867 AU on 2026-06-26 06:59:00 UTC
    [NORMAL MODE] Portia: 51 dates from 2026-06-06 16:35:00 to 2026-07-04 16:35:00
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]

    Processing trajectory for 712:
    Requested epochs: 51
    Returned vectors: 51
    Direct position matches: 51
    Interpolated positions: 0
    Final coverage: 51/51 epochs
    [NORMAL MODE] Plotted Portia orbit with 51 points
    -> Added closest plotted marker for Portia to Uranus: 0.000440 AU on 2026-07-04 16:35:00 UTC
    [NORMAL MODE] Mab: 51 dates from 2026-06-06 16:35:00 to 2026-07-04 16:35:00
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]

    Processing trajectory for 726:
    Requested epochs: 51
    Returned vectors: 51
    Direct position matches: 51
    Interpolated positions: 0
    Final coverage: 51/51 epochs
    [NORMAL MODE] Plotted Mab orbit with 51 points
    -> Added closest plotted marker for Mab to Uranus: 0.000650 AU on 2026-06-16 05:03:48 UTC
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    Full hover text: <b>Uranus</b><br>Right Ascension: 04h 01m 24.043s<br>  (apparent, +/-0.3 arcsec, JPL DE440/441 ephemeris)<br>Declination: +20 deg 28' 57.97"<br>  (apparent, +/-0.3 arcsec, JPL DE440/441 ephemeris)<br><br>Distance from Center: 0.0000000000 AU<br>Distance: 0.0000000000e+00 kilometers<br>Distance: 0.0000000000 light-minutes<br>Distance: 0.0000000000 light-hours<br>Distance to Center Surface: -2.5559000000e+04 (below mean datum) kilometers<br>Velocity: N/A AU/day<br>Velocity: N/A km/hr (N/A km/sec)<br>Known Orbital Period: 84.0205 Earth years (30688.50 days)<br>Horizons: 799. NASA: "Uranus is the seventh planet from the Sun, and the third<br>largest planet in our solar system -- about four times wider than Earth."
    Minimal hover text: <b>Uranus</b><br>RA/Dec: 04h 01m 24.043s, +20 deg 28' 57.97" (apparent, +/-0.3 arcsec, JPL DE440/441 ephemeris)
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    Full hover text: <b>Ariel</b><br>Position at: 2026-06-06 16:35:00 UTC<br>Right Ascension: 04h 01m 23.290s<br>  (apparent, +/-0.3 arcsec, JPL DE440/441 ephemeris)<br>Declination: +20 deg 28' 51.17"<br>  (apparent, +/-0.3 arcsec, JPL DE440/441 ephemeris)<br><br>Distance from Center: 0.0012757790 AU<br>Distance: 1.9085382445e+05 kilometers<br>Distance: 0.0106103305 light-minutes<br>Distance: 0.0001768388 light-hours<br>Distance to Center Surface: 1.6529482445e+05 kilometers<br>Velocity: 0.0031829955 AU/day<br>Velocity: 19,840.39 km/hr (5.511 km/sec)<br>Known Orbital Period: 0.0069 Earth years (2.52 days)<br>Horizons: 701. Uranus orbital period: 2.52 Earth days.<br>Moon of Uranus
    Minimal hover text: <b>Ariel</b><br>RA/Dec: 04h 01m 23.290s, +20 deg 28' 51.17" (apparent, +/-0.3 arcsec, JPL DE440/441 ephemeris)
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    Full hover text: <b>Umbriel</b><br>Position at: 2026-06-06 16:35:00 UTC<br>Right Ascension: 04h 01m 25.255s<br>  (apparent, +/-0.3 arcsec, JPL DE440/441 ephemeris)<br>Declination: +20 deg 29' 00.53"<br>  (apparent, +/-0.3 arcsec, JPL DE440/441 ephemeris)<br><br>Distance from Center: 0.0017734652 AU<br>Distance: 2.6530661966e+05 kilometers<br>Distance: 0.0147494604 light-minutes<br>Distance: 0.0002458243 light-hours<br>Distance to Center Surface: 2.3974761966e+05 kilometers<br>Velocity: 0.0027024749 AU/day<br>Velocity: 16,845.19 km/hr (4.679 km/sec)<br>Known Orbital Period: 0.0113 Earth years (4.14 days)<br>Horizons: 702. Uranus orbital period: 4.14 Earth days.<br>Moon of Uranus
    Minimal hover text: <b>Umbriel</b><br>RA/Dec: 04h 01m 25.255s, +20 deg 29' 00.53" (apparent, +/-0.3 arcsec, JPL DE440/441 ephemeris)
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    Full hover text: <b>Titania</b><br>Position at: 2026-06-06 16:35:00 UTC<br>Right Ascension: 04h 01m 22.385s<br>  (apparent, +/-0.3 arcsec, JPL DE440/441 ephemeris)<br>Declination: +20 deg 28' 40.98"<br>  (apparent, +/-0.3 arcsec, JPL DE440/441 ephemeris)<br><br>Distance from Center: 0.0029119143 AU<br>Distance: 4.3561618514e+05 kilometers<br>Distance: 0.0242176531 light-minutes<br>Distance: 0.0004036276 light-hours<br>Distance to Center Surface: 4.1005718514e+05 kilometers<br>Velocity: 0.0021079923 AU/day<br>Velocity: 13,139.63 km/hr (3.650 km/sec)<br>Known Orbital Period: 0.0238 Earth years (8.71 days)<br>Horizons: 703. Uranus orbital period: 8.71 Earth days.<br>Moon of Uranus
    Minimal hover text: <b>Titania</b><br>RA/Dec: 04h 01m 22.385s, +20 deg 28' 40.98" (apparent, +/-0.3 arcsec, JPL DE440/441 ephemeris)
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    Full hover text: <b>Oberon</b><br>Position at: 2026-06-06 16:35:00 UTC<br>Right Ascension: 04h 01m 26.719s<br>  (apparent, +/-0.3 arcsec, JPL DE440/441 ephemeris)<br>Declination: +20 deg 28' 55.60"<br>  (apparent, +/-0.3 arcsec, JPL DE440/441 ephemeris)<br><br>Distance from Center: 0.0039068496 AU<br>Distance: 5.8445638576e+05 kilometers<br>Distance: 0.0324922776 light-minutes<br>Distance: 0.0005415380 light-hours<br>Distance to Center Surface: 5.5889738576e+05 kilometers<br>Velocity: 0.0018169315 AU/day<br>Velocity: 11,325.38 km/hr (3.146 km/sec)<br>Known Orbital Period: 0.0369 Earth years (13.46 days)<br>Horizons: 704. Uranus orbital period: 13.46 Earth days.<br>Moon of Uranus
    Minimal hover text: <b>Oberon</b><br>RA/Dec: 04h 01m 26.719s, +20 deg 28' 55.60" (apparent, +/-0.3 arcsec, JPL DE440/441 ephemeris)
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    Full hover text: <b>Miranda</b><br>Position at: 2026-06-06 16:35:00 UTC<br>Right Ascension: 04h 01m 24.144s<br>  (apparent, +/-0.3 arcsec, JPL DE440/441 ephemeris)<br>Declination: +20 deg 29' 06.58"<br>  (apparent, +/-0.3 arcsec, JPL DE440/441 ephemeris)<br><br>Distance from Center: 0.0008670039 AU<br>Distance: 1.2970194048e+05 kilometers<br>Distance: 0.0072106517 light-minutes<br>Distance: 0.0001201775 light-hours<br>Distance to Center Surface: 1.0414294048e+05 kilometers<br>Velocity: 0.0038626519 AU/day<br>Velocity: 24,076.85 km/hr (6.688 km/sec)<br>Known Orbital Period: 0.0039 Earth years (1.41 days)<br>Horizons: 705. Uranus orbital period: 1.41 Earth days.<br>Moon of Uranus
    Minimal hover text: <b>Miranda</b><br>RA/Dec: 04h 01m 24.144s, +20 deg 29' 06.58" (apparent, +/-0.3 arcsec, JPL DE440/441 ephemeris)
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    Full hover text: <b>Portia</b><br>Position at: 2026-06-06 16:35:00 UTC<br>Right Ascension: 04h 01m 23.928s<br>  (apparent, +/-0.5 arcsec, JPL DE440/441 ephemeris)<br>Declination: +20 deg 28' 53.83"<br>  (apparent, +/-0.5 arcsec, JPL DE440/441 ephemeris)<br><br>Distance from Center: 0.0004434373 AU<br>Distance: 6.6337276749e+04 kilometers<br>Distance: 0.0036879556 light-minutes<br>Distance: 0.0000614659 light-hours<br>Distance to Center Surface: 4.0778276749e+04 kilometers<br>Velocity: 0.0053902631 AU/day<br>Velocity: 33,598.83 km/hr (9.333 km/sec)<br>Known Orbital Period: 0.0014 Earth years (0.51 days)<br>Horizons: 712. Uranus orbital period: 0.513196 Earth days or 12.317 hours.<br>Moon of Uranus
    Minimal hover text: <b>Portia</b><br>RA/Dec: 04h 01m 23.928s, +20 deg 28' 53.83" (apparent, +/-0.5 arcsec, JPL DE440/441 ephemeris)
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    Full hover text: <b>Mab</b><br>Position at: 2026-06-06 16:35:00 UTC<br>Right Ascension: 04h 01m 23.616s<br>  (apparent, +/-0.1 arcsec, typical)<br>Declination: +20 deg 28' 55.67"<br>  (apparent, +/-0.1 arcsec, typical)<br><br>Distance from Center: 0.0006546732 AU<br>Distance: 9.7937715566e+04 kilometers<br>Distance: 0.0054447509 light-minutes<br>Distance: 0.0000907458 light-hours<br>Distance to Center Surface: 7.2378715566e+04 kilometers<br>Velocity: 0.0044385953 AU/day<br>Velocity: 27,666.85 km/hr (7.685 km/sec)<br>Known Orbital Period: 0.0025 Earth years (0.92 days)<br>Horizons: 726. Uranus orbital period: 0.923293 Earth days or 22.159 hours.<br>Moon of Uranus
    Minimal hover text: <b>Mab</b><br>RA/Dec: 04h 01m 23.616s, +20 deg 28' 55.67" (apparent, +/-0.1 arcsec, typical)

    [OSCULATING] Loading cached elements for Ariel...
    [OK] Using cached osculating elements
    Plotting osculating: i=97.7167 deg (ecliptic), epoch=2026-06-06 16:36 osc.
    [OK] Osculating orbit plotted (ecliptic frame)

    [OSCULATING] Loading cached elements for Umbriel...
    [OK] Using cached osculating elements
    Plotting osculating: i=97.7131 deg (ecliptic), epoch=2026-06-06 16:36 osc.
    [OK] Osculating orbit plotted (ecliptic frame)

    [OSCULATING] Loading cached elements for Titania...
    [OK] Using cached osculating elements
    Plotting osculating: i=97.7626 deg (ecliptic), epoch=2026-06-06 16:36 osc.
    [OK] Osculating orbit plotted (ecliptic frame)

    [OSCULATING] Loading cached elements for Oberon...
    [OK] Using cached osculating elements
    Plotting osculating: i=97.9057 deg (ecliptic), epoch=2026-06-06 16:36 osc.
    [OK] Osculating orbit plotted (ecliptic frame)

    [OSCULATING] Loading cached elements for Miranda...
    [OK] Using cached osculating elements
    Plotting osculating: i=98.5382 deg (ecliptic), epoch=2026-06-06 16:36 osc.
    [OK] Osculating orbit plotted (ecliptic frame)

    [OSCULATING] Loading cached elements for Portia...
    [OK] Using cached osculating elements
    Plotting osculating: i=95.0913 deg (ecliptic), epoch=2026-06-06 16:36 osc.
    [OK] Osculating orbit plotted (ecliptic frame)

    [OSCULATING] Loading cached elements for Mab...
    [OK] Using cached osculating elements
    Plotting osculating: i=96.2744 deg (ecliptic), epoch=2026-06-06 16:36 osc.
    [OK] Osculating orbit plotted (ecliptic frame)

    [ACTUAL APSIDAL] Checking satellites for apsidal markers...

    [ACTUAL APSIDAL] Processing Ariel
    Object ID: 701
    Center: Uranus
    Ariel: Using TP for perihelion: 2026-06-06 22:16:50
    Ariel: No Tapo provided - actual aphelion marker will not be plotted
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    Next periapsis: 2026-06-06 22:16:50.758817
        Fetched position for 2026-06-06 22:16:50
    Fetched 1 positions
    [HOVER DEBUG] Ariel Keplerian Periuranion (Epoch: 2026-06-06 16:36 osc.):
    ideal_pos is not None: True
    params is not None: True
    'epoch' in params: True
    epoch value: 2026-06-06 16:36 osc.
    angle_deg: 0.001 deg
    [OK] Added actual apsidal markers for Ariel

    [ACTUAL APSIDAL] Processing Umbriel
    Object ID: 702
    Center: Uranus
    Umbriel: Using TP for perihelion: 2026-06-07 07:28:37
    Umbriel: No Tapo provided - actual aphelion marker will not be plotted
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    Next periapsis: 2026-06-07 07:28:37.415495
        Fetched position for 2026-06-07 07:28:37
    Fetched 1 positions
    [HOVER DEBUG] Umbriel Keplerian Periuranion (Epoch: 2026-06-06 16:36 osc.):
    ideal_pos is not None: True
    params is not None: True
    'epoch' in params: True
    epoch value: 2026-06-06 16:36 osc.
    angle_deg: 0.000 deg
    [OK] Added actual apsidal markers for Umbriel

    [ACTUAL APSIDAL] Processing Titania
    Object ID: 703
    Center: Uranus
    Titania: Using TP for perihelion: 2026-06-07 23:11:52
    Titania: No Tapo provided - actual aphelion marker will not be plotted
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    Next periapsis: 2026-06-07 23:11:52.289773
        Fetched position for 2026-06-07 23:11:52
    Fetched 1 positions
    [HOVER DEBUG] Titania Keplerian Periuranion (Epoch: 2026-06-06 16:36 osc.):
    ideal_pos is not None: True
    params is not None: True
    'epoch' in params: True
    epoch value: 2026-06-06 16:36 osc.
    angle_deg: 0.000 deg
    [OK] Added actual apsidal markers for Titania

    [ACTUAL APSIDAL] Processing Oberon
    Object ID: 704
    Center: Uranus
    Oberon: Using TP for perihelion: 2026-06-12 23:28:26
    Oberon: No Tapo provided - actual aphelion marker will not be plotted
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    Next periapsis: 2026-06-12 23:28:26.773576
        Fetched position for 2026-06-12 23:28:26
    Fetched 1 positions
    [HOVER DEBUG] Oberon Keplerian Periuranion (Epoch: 2026-06-06 16:36 osc.):
    ideal_pos is not None: True
    params is not None: True
    'epoch' in params: True
    epoch value: 2026-06-06 16:36 osc.
    angle_deg: 0.001 deg
    [OK] Added actual apsidal markers for Oberon

    [ACTUAL APSIDAL] Processing Miranda
    Object ID: 705
    Center: Uranus
    Miranda: Using TP for perihelion: 2026-06-06 13:38:19
    Miranda: No Tapo provided - actual aphelion marker will not be plotted
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    Next periapsis: 2026-06-06 13:38:19.119079
        Fetched position for 2026-06-06 13:38:19
    Fetched 1 positions
    [HOVER DEBUG] Miranda Keplerian Periuranion (Epoch: 2026-06-06 16:36 osc.):
    ideal_pos is not None: True
    params is not None: True
    'epoch' in params: True
    epoch value: 2026-06-06 16:36 osc.
    angle_deg: 0.001 deg
    [OK] Added actual apsidal markers for Miranda

    [ACTUAL APSIDAL] Processing Portia
    Object ID: 712
    Center: Uranus
    Portia: Using TP for perihelion: 2026-06-06 10:40:18
    Portia: No Tapo provided - actual aphelion marker will not be plotted
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    Next periapsis: 2026-06-06 10:40:18.190371
        Fetched position for 2026-06-06 10:40:18
    Fetched 1 positions
    [HOVER DEBUG] Portia Keplerian Periuranion (Epoch: 2026-06-06 16:36 osc.):
    ideal_pos is not None: True
    params is not None: True
    'epoch' in params: True
    epoch value: 2026-06-06 16:36 osc.
    angle_deg: 0.302 deg
    [OK] Added actual apsidal markers for Portia

    [ACTUAL APSIDAL] Processing Mab
    Object ID: 726
    Center: Uranus
    Mab: Using TP for perihelion: 2026-06-06 23:09:41
    Mab: No Tapo provided - actual aphelion marker will not be plotted
    WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
    Next periapsis: 2026-06-06 23:09:41.442404
        Fetched position for 2026-06-06 23:09:41
    Fetched 1 positions
    [HOVER DEBUG] Mab Keplerian Periuranion (Epoch: 2026-06-06 16:36 osc.):
    ideal_pos is not None: True
    params is not None: True
    'epoch' in params: True
    epoch value: 2026-06-06 16:36 osc.
    angle_deg: 0.041 deg
    [OK] Added actual apsidal markers for Mab

    Keplerian Orbit Summary:
    Plotted Keplerian orbits for 7 objects:
    - Ariel
    - Umbriel
    - Titania
    - Oberon
    - Miranda
    - Portia
    - Mab

    Skipped Keplerian orbits for:
    [Camera Buttons] Auto-detected 7 target objects from positions
    [Camera Buttons] Added dropdown with 8 view options
    [Fly To Buttons] Auto-detected 7 target objects from positions
    [Fly To Buttons] Added dropdown with 8 fly-to options
    Visualization opened in browser
    Saving HTML (~10 KB + plot data, needs internet) to C:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_images/uranus_shells_uranus_center_test.html...
    HTML saved successfully.
    Window config saved to c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\window_config.json
    Window config saved to c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\window_config.json
    Window config saved to c:\Users\tonyq\OneDrive\Desktop\python_work\orrery\window_config.json

**Gate 4 — Regression (didn't break Movement-1).**
- Rotation axis still renders on Uranus/Neptune (and unchanged elsewhere) — the cone shares its dispatch block, so confirm both coexist. -- pass: uranus, neptune
- Rings, belts, magnetosphere, bow shock all still render as before. -- pass: uranus; please review Neptune. the rings and arcs are alined with the satellites, but the belts are unclear and may not be. 
- A non-dipole body (Earth, Mars) plots normally and shows **no** dipole cone. -- pass: earth, jupiter, saturn
- Toggle a shell checkbox on/off: the cone should not double-render or vanish (it's excluded from the shell loop on purpose). -- pass: uranus, neptune

**Gate 5 — Hover text.**
- Dipole-cone cross marker (at the +tip): tilt, sense, "one arbitrary instant," offset-deferred, source line. -- pass: uranus, neptune
- Magnetosphere envelope hover, **Uranus and Neptune**: now carries the schematic/approximate disclosure (standoff + tilt sourced; oblateness + tail approximate) and points to the Dipole Cone. This is the *only* check the 2 hover-edit files need — they're text-only, no smoke required. -- pass: uranus, neptune
- Bow shock hover: unchanged. -- pass: uranus, neptune

**Gate 6 — Parallel pipeline (the one easy-to-miss check).** If your rotation axis or magnetosphere appear in **animation** frames, confirm the dipole cone does too — it's wired in `create_celestial_body_visualization`, so it rides whatever path that function feeds. If your animate path is separate and the cone doesn't show in frames, that's a known parallel-pipeline gap to note in the handoff, not a bug in this code. -- uranus, neptune: the dipole and rotational axis work correctly, but there are other issues: the central object does not plot, the sun direction indicator does not plot, and the magnetospheere and shock are pointed towards the -x line. defer this issue to the animation refactor sessions. we will need to carefully plan, check, and correct. 

**Gate 7 — Commit, push, round trip.** Once Gates 2–5 hold: commit and push, then `git ls-remote HEAD` and confirm it equals the new SHA. Record `built on de12f56 -> pushed at <new SHA>` in the handoff. Matching remote HEAD = commit + push + sync confirmed. -- github local repo smoke and provenance pass; pushed to github. new SHA: c25bdd7d9267b4cfd43e3c8df021917bd1a49745

Quick map of who's verified what: Gates 1 and the builder geometry are already green my side; Gate 2 is the live-dispatch confirmation only your env can run; Gates 3–6 are your eyes, which is the gate that actually decides. If Gate 2 fails or anything in Gate 3 looks off, send me the console output and I'll trace it.