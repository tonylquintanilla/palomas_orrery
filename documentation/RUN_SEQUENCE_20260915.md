# Run and test sequence, 2026-09-15

Nine patches. Orrery first, then gallery, because the gallery's drift check
reads the orrery's pushed HEAD.

Two patches are **withdrawn**. Delete them without running:
`patch_L330_belt_plane_ledger_item.py` and
`patch_L231_belt_plane_amendment.py`.

Two are **already in** from earlier tonight and need nothing:
`patch_L305_l_shell_scalar_unit.py` (gallery) and
`patch_L305_item6b_magnetopause_cut_angle.py` (orrery).

---

## Step 0 — before anything

In BOTH repositories:

```
git status --porcelain
```
**Tony**: nothing on both

Expect nothing. If `data/objects_config.json` shows as modified in the
gallery, that is the local drift that made the Earth scene checker report
three white outlines instead of four at the start of tonight. Fix it with:

```
git checkout -- data/objects_config.json
```

Every patch below fingerprints its target and refuses on a mismatch, so a
dirty file will stop the sequence rather than corrupt it. That is the guard
working, not a failure.

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>git status --porcelain

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>git checkout -- data/objects_config.json
error: pathspec 'data/objects_config.json' did not match any file(s) known to git

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>


C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>git status --porcelain

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>git checkout -- data/objects_config.json

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

---

## Part 1 — the orrery

Run from the orrery repo root, in this order.

### 1. The ledger

```
python patch_L231_L305_L330_belt_plane_ruling.py
python ledger_index.py
```

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>python patch_L231_L305_L330_belt_plane_ruling.py
OK: ledger updated.
    L-231 amended: ruling recorded, five findings, gap rewritten
    L-305 gap extended: why the typed tilt should not wait
    L-330 opened: the belt's shape, separate from its plane
    line endings preserved (LF)

Next: python ledger_index.py
      Expect ONE more block than the previous run reported.

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>python ledger_index.py
OK: 325 L-blocks parsed, no consistency problems.
Index regenerated (196 live items) in C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\LEDGER_CONSOLIDATED.md.

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

Expect: three places updated, and ONE more block than the last run
reported. No consistency problems.

### 2. The dipole tilt into the store

```
python patch_L231_dipole_tilt_to_store.py
python -c "import constants_new as c; print(c.EARTH_DIPOLE_TILT_DEG)"
python -c "import planet_visualization_utilities as p; print(p.PLANET_DIPOLE['Earth']['tilt_deg'])"
```

Expect: both print `9.6`. If the second one raises an ImportError, the
import line did not land — stop and say so.

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>python patch_L231_dipole_tilt_to_store.py
OK: two files written.
    constants_new.py                       (LF)
    planet_visualization_utilities.py      (LF)

Next:
  python -c "import constants_new as c; print(c.EARTH_DIPOLE_TILT_DEG)"
  python -c "import planet_visualization_utilities as p; print(p.PLANET_DIPOLE['Earth']['tilt_deg'])"
  Both must print 9.6.
  python provenance_scanner.py   (Tier-1 must not rise)

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>python -c "import constants_new as c; print(c.EARTH_DIPOLE_TILT_DEG)"
9.6

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>python -c "import planet_visualization_utilities as p; print(p.PLANET_DIPOLE['Earth']['tilt_deg'])"
9.6

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

### 3. The belts into Earth's equatorial plane

```
python patch_L231_belt_plane_orrery.py
python -m py_compile earth_visualization_shells.py
```

Expect: three changes reported, and a silent compile.

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>python patch_L231_belt_plane_orrery.py
OK: earth_visualization_shells.py written (LF).
    belts rotated into Earth's equatorial plane
    saddle warp removed
    uncited magnetic_tilt_deg=11 removed from the magnetopause

Next:
  python -m py_compile earth_visualization_shells.py
  python provenance_scanner.py
  Then render Earth and look: belts coplanar with the equator
  and the GEO ring, flat, and the magnetopause upright inside
  the bow shock.

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>python -m py_compile earth_visualization_shells.py

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

### 4. Orrery checks

```
python provenance_scanner.py
python test_status_lines.py
```

Expect: Tier-1 does NOT rise, and no file's Tier-1 count rises. The new
store row will likely add ONE Tier-2 finding, the same as the cut-angle row
did — cited, not independently cross-checked.



C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>python provenance_scanner.py
Provenance Scanner -- scanning .

Loaded exceptions: 17 suppressed fingerprints, 5 accepted residuals
Loaded 117 pinned constant values for cross-reference scoring
Suppressed 26 known false positives (see data/provenance_exceptions.json)
17 string(s) sit in an uncited block inside a cited one -- citation level mismatch, see audit
4 orphan annotation(s) -- attached to no claim, granted no credit, see audit
    constants_new.py:904
    constants_new.py:905
    constants_new.py:1196
    constants_new.py:1197
Audit written to PROVENANCE_AUDIT.md
  1065 findings across 137 files

Priority summary:
  Tier 1 (16-20):   292 findings -- FIX NOW
      earth_science     149
      orrery            129
      stars              12
      utilities           2
  Tier 2 (10-15):   655 findings -- REVIEW
      orrery            539
      earth_science      74
      stars              42
  Tier 3 (5-9):   116 findings -- LOW PRIORITY
      orrery             69
      dev_tools          39
      stars               6
      earth_science       2
  Tier 4 (1-4):     2 findings -- LOWEST PRIORITY
      orrery              2

Run history (data/provenance_history.json):
  previous run 20260915T041248Z (15 hours earlier, HEAD 68102e1)
  delta   total +1   T1 +0   T2 +1   T3 +0   T4 +0
  no file's Tier-1 count rose.

======================================================================
  292 TIER-1 FINDINGS IN THE SCANNED TREE

  Informational only. This does not affect the exit code,
  and it is NOT the push gate. The gate is Tier-1 = 0 on
  the ACTIVE BUILD PATH (provenance-discipline 2.3,
  L-184). This line does not compute that subset -- it
  counts every Tier-1 finding anywhere in the tree, most
  of them off the path the gate judges. Read
  PROVENANCE_AUDIT.md for the build-path findings.
  The call is yours.
======================================================================

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>python test_status_lines.py
======================================================================
  STATUS LINE GRAMMAR -- constants_new.py
======================================================================

Scored from a status line: 30 of 110 rows.
  The denominator counts every top-level ALL-CAPS assignment,
  including dicts and label tables. The unit design record's 88
  counts numeric constants only; these are different axes.
  measured (22)
  declared (3): EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG, EARTH_VAN_ALLEN_OUTER_RADII, INNER_CORONA_RADII
  declared pending (3): EARTH_SOLAR_WIND_BZ_NT, EARTH_SOLAR_WIND_PRESSURE_NPA, EARTH_SOLAR_WIND_SPEED_KM_S
  derived (2): EARTH_BOW_SHOCK_STANDOFF_RADII, EARTH_MAGNETOPAUSE_STANDOFF_RADII
No status line: 80 of 110 rows -- unexamined, not passing.
  These are scored by the scanner's window inference, which the
  Status Line rule says to delete. That walk is L-322's.

Row shape: 112 top-level assignment(s) read, 0 failed.
  A value that is not a container literal must fit on the
  assignment's own line, because constants_change_report.py
  reads values line by line (L-324).

Results: 30 status line(s) checked, 0 malformed; 112 row shape(s) read, 0 wrong.

All 30 status lines in constants_new.py are well formed; 80 rows carry none.

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

### 5. Render it — this is the Mode 5 call

Open Earth with the belts, the magnetosphere and the geostationary ring
switched on. Three things to look for:

- Both belts now lie in the same plane as the equator and the
  geostationary ring, rather than 23 degrees off it. -- correct; see uploaded image
- Both belts are flat. The old saddle lifted each ring by a fifth of its
  radius, twice per circuit — nearly a full Earth radius up and down on the
  outer belt. -- correct
- The magnetopause is upright inside the bow shock, not leaning. It used to
  lean 11 degrees while the bow shock did not. -- correct
  -- the hovertext still mentions the 9.6 dipole tilt

If any of that looks wrong, stop before pushing.


============================================================
    PALOMA'S ORRERY - Dashboard
============================================================
    Author: Tony Quintanilla
    "Data Preservation is Climate Action"
============================================================

Python detected:
Python 3.13.0

Starting Dashboard...
Working directory: C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github

[DASHBOARD] Dashboard ready.
[DASHBOARD] Launched: palomas_orrery.py  (PID 11028)
[DASHBOARD] [palomas_orrery] Working directory set to: C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github
[DASHBOARD] [palomas_orrery] Interpreter: C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe
[DASHBOARD] [palomas_orrery] Working directory: C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github
[DASHBOARD] [palomas_orrery] Window config file: C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\window_config.json
[DASHBOARD] [palomas_orrery] Restored window geometry: 1536x793+0+5
[DASHBOARD] [palomas_orrery] Window will be maximized
[DASHBOARD] [palomas_orrery] ============================================================
[DASHBOARD] [palomas_orrery] LOADING ORBIT CACHE FROM: data/orbit_paths.json
[DASHBOARD] [palomas_orrery] ============================================================
[DASHBOARD] [palomas_orrery] Cache loaded successfully: 1501 valid entries
[DASHBOARD] [palomas_orrery] [CACHE HEALTH SUMMARY]
[DASHBOARD] [palomas_orrery] Total cached orbits: 1501
[DASHBOARD] [palomas_orrery] Orbits by center object:
[DASHBOARD] [palomas_orrery]   3I/ATLAS: 5 orbits
[DASHBOARD] [palomas_orrery]   Apophis: 2 orbits
[DASHBOARD] [palomas_orrery]   Arrokoth: 6 orbits
[DASHBOARD] [palomas_orrery]   Bennu: 2 orbits
[DASHBOARD] [palomas_orrery]   Bennu/OSIRIS: 1 orbits
[DASHBOARD] [palomas_orrery]   Earth: 135 orbits
[DASHBOARD] [palomas_orrery]   Earth-Moon Barycenter: 3 orbits
[DASHBOARD] [palomas_orrery]   Eris: 2 orbits
[DASHBOARD] [palomas_orrery]   Eris-Dysnomia Barycenter: 4 orbits
[DASHBOARD] [palomas_orrery]   Eris/Dysnomia: 101 orbits
[DASHBOARD] [palomas_orrery]   Haumea: 11 orbits
[DASHBOARD] [palomas_orrery]   Haumea System Barycenter: 3 orbits
[DASHBOARD] [palomas_orrery]   Juno: 4 orbits
[DASHBOARD] [palomas_orrery]   Jupiter: 104 orbits
[DASHBOARD] [palomas_orrery]   K1: 2 orbits
[DASHBOARD] [palomas_orrery]   K1-B: 1 orbits
[DASHBOARD] [palomas_orrery]   K1-C: 1 orbits
[DASHBOARD] [palomas_orrery]   K1-D: 1 orbits
[DASHBOARD] [palomas_orrery]   L1: 2 orbits
[DASHBOARD] [palomas_orrery]   L2: 3 orbits
[DASHBOARD] [palomas_orrery]   Leucus: 1 orbits
[DASHBOARD] [palomas_orrery]   Makemake: 1 orbits
[DASHBOARD] [palomas_orrery]   Mars: 106 orbits
[DASHBOARD] [palomas_orrery]   Menoetius: 2 orbits
[DASHBOARD] [palomas_orrery]   Mercury: 102 orbits
[DASHBOARD] [palomas_orrery]   Moon: 112 orbits
[DASHBOARD] [palomas_orrery]   Neptune: 101 orbits
[DASHBOARD] [palomas_orrery]   Orcus: 3 orbits
[DASHBOARD] [palomas_orrery]   Orcus-Vanth Barycenter: 3 orbits
[DASHBOARD] [palomas_orrery]   Patroclus: 2 orbits
[DASHBOARD] [palomas_orrery]   Patroclus-Menoetius Barycenter: 4 orbits
[DASHBOARD] [palomas_orrery]   Phobos: 6 orbits
[DASHBOARD] [palomas_orrery]   Planet 9: 5 orbits
[DASHBOARD] [palomas_orrery]   Pluto: 102 orbits
[DASHBOARD] [palomas_orrery]   Pluto-Charon Barycenter: 9 orbits
[DASHBOARD] [palomas_orrery]   Polymele: 1 orbits
[DASHBOARD] [palomas_orrery]   Quaoar: 1 orbits
[DASHBOARD] [palomas_orrery]   Quaoar-Weywot Barycenter: 2 orbits
[DASHBOARD] [palomas_orrery]   R2: 1 orbits
[DASHBOARD] [palomas_orrery]   Saturn: 101 orbits
[DASHBOARD] [palomas_orrery]   Sun: 156 orbits
[DASHBOARD] [palomas_orrery]   Uranus: 101 orbits
[DASHBOARD] [palomas_orrery]   Vanth: 2 orbits
[DASHBOARD] [palomas_orrery]   Venus: 101 orbits
[DASHBOARD] [palomas_orrery] Note: Cache can only be manually deleted by removing 'data/orbit_paths.json' file
[DASHBOARD] [palomas_orrery] Cache and restore points (date = when that content was written):
[DASHBOARD] [palomas_orrery]   data/orbit_paths.json: 130.9 MB, written 2026-09-14 23:18
[DASHBOARD] [palomas_orrery]   data/orbit_paths.json.backup: 130.9 MB, written 2026-09-14 21:49
[DASHBOARD] [palomas_orrery]   data/orbit_paths.json.backup_old: 130.9 MB, written 2026-09-07 11:16
[DASHBOARD] [palomas_orrery] --------------------------------------------------
[DASHBOARD] [palomas_orrery] [DEBUG] Sun can be center (numeric ID: 10)
[DASHBOARD] [palomas_orrery] [DEBUG] Mercury can be center (numeric ID: 199)
[DASHBOARD] [palomas_orrery] [DEBUG] Venus can be center (numeric ID: 299)
[DASHBOARD] [palomas_orrery] [DEBUG] Apophis can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Earth can be center (numeric ID: 399)
[DASHBOARD] [palomas_orrery] [DEBUG] Moon can be center (numeric ID: 301)
[DASHBOARD] [palomas_orrery] [DEBUG] Earth-Moon Barycenter can be center (numeric ID: 3)
[DASHBOARD] [palomas_orrery] [DEBUG] EM-L1 can be center (numeric ID: 3011)
[DASHBOARD] [palomas_orrery] [DEBUG] EM-L2 can be center (numeric ID: 3012)
[DASHBOARD] [palomas_orrery] [DEBUG] EM-L3 can be center (numeric ID: 3013)
[DASHBOARD] [palomas_orrery] [DEBUG] EM-L4 can be center (numeric ID: 3014)
[DASHBOARD] [palomas_orrery] [DEBUG] EM-L5 can be center (numeric ID: 3015)
[DASHBOARD] [palomas_orrery] [DEBUG] L1 can be center (numeric ID: 31)
[DASHBOARD] [palomas_orrery] [DEBUG] L2 can be center (numeric ID: 32)
[DASHBOARD] [palomas_orrery] [DEBUG] L3 can be center (numeric ID: 33)
[DASHBOARD] [palomas_orrery] [DEBUG] L4 can be center (numeric ID: 34)
[DASHBOARD] [palomas_orrery] [DEBUG] L5 can be center (numeric ID: 35)
[DASHBOARD] [palomas_orrery] [DEBUG] Bennu can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Itokawa can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Ryugu can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Eros can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Mars can be center (numeric ID: 499)
[DASHBOARD] [palomas_orrery] [DEBUG] Phobos can be center (numeric ID: 401)
[DASHBOARD] [palomas_orrery] [DEBUG] Deimos can be center (numeric ID: 402)
[DASHBOARD] [palomas_orrery] [DEBUG] Dinkinesh can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Vesta can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Donaldjohanson can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Ceres can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] 16 Psyche can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Orus can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Polymele can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Eurybates can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Patroclus-Menoetius Barycenter can be center (numeric ID: 20000617)
[DASHBOARD] [palomas_orrery] [DEBUG] Patroclus can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Menoetius can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Leucus can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Jupiter can be center (numeric ID: 599)
[DASHBOARD] [palomas_orrery] [DEBUG] Metis can be center (numeric ID: 516)
[DASHBOARD] [palomas_orrery] [DEBUG] Adrastea can be center (numeric ID: 515)
[DASHBOARD] [palomas_orrery] [DEBUG] Amalthea can be center (numeric ID: 505)
[DASHBOARD] [palomas_orrery] [DEBUG] Thebe can be center (numeric ID: 514)
[DASHBOARD] [palomas_orrery] [DEBUG] Io can be center (numeric ID: 501)
[DASHBOARD] [palomas_orrery] [DEBUG] Europa can be center (numeric ID: 502)
[DASHBOARD] [palomas_orrery] [DEBUG] Ganymede can be center (numeric ID: 503)
[DASHBOARD] [palomas_orrery] [DEBUG] Callisto can be center (numeric ID: 504)
[DASHBOARD] [palomas_orrery] [DEBUG] Saturn can be center (numeric ID: 699)
[DASHBOARD] [palomas_orrery] [DEBUG] Pan can be center (numeric ID: 618)
[DASHBOARD] [palomas_orrery] [DEBUG] Daphnis can be center (numeric ID: 635)
[DASHBOARD] [palomas_orrery] [DEBUG] Prometheus can be center (numeric ID: 616)
[DASHBOARD] [palomas_orrery] [DEBUG] Pandora can be center (numeric ID: 617)
[DASHBOARD] [palomas_orrery] [DEBUG] Mimas can be center (numeric ID: 601)
[DASHBOARD] [palomas_orrery] [DEBUG] Enceladus can be center (numeric ID: 602)
[DASHBOARD] [palomas_orrery] [DEBUG] Tethys can be center (numeric ID: 603)
[DASHBOARD] [palomas_orrery] [DEBUG] Dione can be center (numeric ID: 604)
[DASHBOARD] [palomas_orrery] [DEBUG] Rhea can be center (numeric ID: 605)
[DASHBOARD] [palomas_orrery] [DEBUG] Titan can be center (numeric ID: 606)
[DASHBOARD] [palomas_orrery] [DEBUG] Hyperion can be center (numeric ID: 607)
[DASHBOARD] [palomas_orrery] [DEBUG] Iapetus can be center (numeric ID: 608)
[DASHBOARD] [palomas_orrery] [DEBUG] Phoebe can be center (numeric ID: 609)
[DASHBOARD] [palomas_orrery] [DEBUG] Uranus can be center (numeric ID: 799)
[DASHBOARD] [palomas_orrery] [DEBUG] Ariel can be center (numeric ID: 701)
[DASHBOARD] [palomas_orrery] [DEBUG] Umbriel can be center (numeric ID: 702)
[DASHBOARD] [palomas_orrery] [DEBUG] Titania can be center (numeric ID: 703)
[DASHBOARD] [palomas_orrery] [DEBUG] Oberon can be center (numeric ID: 704)
[DASHBOARD] [palomas_orrery] [DEBUG] Miranda can be center (numeric ID: 705)
[DASHBOARD] [palomas_orrery] [DEBUG] Portia can be center (numeric ID: 712)
[DASHBOARD] [palomas_orrery] [DEBUG] Mab can be center (numeric ID: 726)
[DASHBOARD] [palomas_orrery] [DEBUG] Neptune can be center (numeric ID: 899)
[DASHBOARD] [palomas_orrery] [DEBUG] Triton can be center (numeric ID: 801)
[DASHBOARD] [palomas_orrery] [DEBUG] Despina can be center (numeric ID: 805)
[DASHBOARD] [palomas_orrery] [DEBUG] Galatea can be center (numeric ID: 806)
[DASHBOARD] [palomas_orrery] [DEBUG] Pluto-Charon Barycenter can be center (numeric ID: 9)
[DASHBOARD] [palomas_orrery] [DEBUG] Pluto can be center (numeric ID: 999)
[DASHBOARD] [palomas_orrery] [DEBUG] Charon can be center (numeric ID: 901)
[DASHBOARD] [palomas_orrery] [DEBUG] Styx can be center (numeric ID: 905)
[DASHBOARD] [palomas_orrery] [DEBUG] Nix can be center (numeric ID: 902)
[DASHBOARD] [palomas_orrery] [DEBUG] Kerberos can be center (numeric ID: 904)
[DASHBOARD] [palomas_orrery] [DEBUG] Hydra can be center (numeric ID: 903)
[DASHBOARD] [palomas_orrery] [DEBUG] Orcus-Vanth Barycenter can be center (numeric ID: 20090482)
[DASHBOARD] [palomas_orrery] [DEBUG] Orcus can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Vanth can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Haumea can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Hi'iaka can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Namaka can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Quaoar can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Weywot can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Arrokoth can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Makemake can be center (numeric ID: 20136472)
[DASHBOARD] [palomas_orrery] [DEBUG] MK2 can be center (numeric ID: 120136472)
[DASHBOARD] [palomas_orrery] [DEBUG] Gonggong can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Xiangliu can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Eris can be center (has center_id)
[DASHBOARD] [palomas_orrery] [DEBUG] Dysnomia can be center (has center_id)
[DASHBOARD] [palomas_orrery] [CENTER MENU] Dynamic center dropdown initialized (starts with Sun only)
[DASHBOARD] [palomas_orrery] [DASHBOARD] Dashboard ready.
[DASHBOARD] [palomas_orrery] [CENTER MENU] Added traces to 182 object variables
[DASHBOARD] [palomas_orrery] Restored sash positions: [489, 1013]
[DASHBOARD] [palomas_orrery] [DEBUG] Sun can be center (numeric ID: 10)
[DASHBOARD] [palomas_orrery] [DEBUG] Earth can be center (numeric ID: 399)
[DASHBOARD] [palomas_orrery] [CENTER MENU] Dynamic centers: Sun + ['Sun', 'Earth']
[DASHBOARD] [palomas_orrery] [get_interval_settings] Read days_to_plot: 28
[DASHBOARD] [palomas_orrery] [SYSTEM SCOPE] Center: Earth, System: solar
[DASHBOARD] [palomas_orrery] Earth: Need 1 days from 2026-10-13 00:00:00 to 2026-10-13 14:03:00
[DASHBOARD] [palomas_orrery] Checking orbit data for updates to 2026-10-13...
[DASHBOARD] [palomas_orrery] Fetching 1 days for Earth (gap in cache)
[DASHBOARD] [palomas_orrery] Fetching orbit data for Earth from 2026-10-13 to 2026-10-13
[DASHBOARD] [palomas_orrery]   Rotated: orbit_paths.json.backup [OK] orbit_paths.json.backup_old
[DASHBOARD] [palomas_orrery]   Backed up: orbit_paths.json [OK] orbit_paths.json.backup
[DASHBOARD] [palomas_orrery] [OK] Saved: orbit_paths.json (2-gen protected)
[DASHBOARD] [palomas_orrery] Smart fetch complete: Updated 0 orbits with minimal data fetching. Saved approximately 0.0 hours of fetch time.
[DASHBOARD] [palomas_orrery] Current Object Positions:
[DASHBOARD] [palomas_orrery] ==================================================
[DASHBOARD] [palomas_orrery] Earth           Position: (   0.000,    0.000,    0.000) AU   Distance from center: Distance data unavailable
[DASHBOARD] [palomas_orrery] ==================================================
[DASHBOARD] [palomas_orrery] [SCALING] Earth child 'Moon': a=0.002570 AU, apoapsis=0.002711 AU
[DASHBOARD] [palomas_orrery] [SCALING] Earth mode: using range +/-0.004067 AU (based on children's orbits)
[DASHBOARD] [palomas_orrery] Sun direction indicator: Using shell radius 0.004263520978042905, scale = 0.00490 AU
[DASHBOARD] [palomas_orrery] [NORMAL MODE] Using dates_lists for plot_actual_orbits
[DASHBOARD] [palomas_orrery] Full hover text: <b>Earth</b><br><br><br>Distance from Center: 0.0000000000 AU<br>Distance: 0.0000000000e+00 kilometers<br>Distance: 0.0000000000 light-minutes<br>Distance to Center Surface: -6.3781366000e+03 (below mean datum) kilometers<br>Velocity: N/A AU/day<br>Velocity: N/A km/hr (N/A km/sec)<br>Known Orbital Period: 1.0000 Earth years (365.26 days)<br>Our home planet.
[DASHBOARD] [palomas_orrery] Minimal hover text: <b>Earth</b>
[DASHBOARD] [palomas_orrery] [ACTUAL APSIDAL] Checking satellites for apsidal markers...
[DASHBOARD] [palomas_orrery] Keplerian Orbit Summary:
[DASHBOARD] [palomas_orrery] Plotted Keplerian orbits for 0 objects:
[DASHBOARD] [palomas_orrery] Skipped Keplerian orbits for:
[DASHBOARD] [palomas_orrery] [Camera Buttons] Auto-detected 0 target objects from positions
[DASHBOARD] [palomas_orrery] [Camera Buttons] Added dropdown with 1 view options
[DASHBOARD] [palomas_orrery] [Fly To Buttons] Auto-detected 0 target objects from positions
[DASHBOARD] [palomas_orrery] [Fly To Buttons] Added dropdown with 1 fly-to options
[DASHBOARD] [palomas_orrery] Visualization opened in browser
[DASHBOARD] [palomas_orrery] User chose not to save
[DASHBOARD] [palomas_orrery] Window config saved to C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\window_config.json

### 6. Push the orrery

```
git add -A && git commit && git push

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch main
# Your branch is ahead of 'origin/main' by 1 commit.
#   (use "git push" to publish your local commits)
#
# Changes to be committed:
#       modified:   LEDGER_CONSOLIDATED.md
#       modified:   PROVENANCE_AUDIT.md
#       modified:   constants_new.py
#       modified:   data/provenance_history.json
#       new file:   documentation/PROMPT_fable_belt_plane_20260914.md
#       modified:   documentation/RUN_SEQUENCE_20260915.md
#       modified:   earth_visualization_shells.py
#       new file:   patch_L231_L305_L330_belt_plane_ruling.py
#       new file:   patch_L231_belt_plane_amendment.py
#       new file:   patch_L231_belt_plane_orrery.py
#       new file:   patch_L231_dipole_tilt_to_store.py
#       new file:   patch_L305_item6b_magnetopause_cut_angle.py
#       new file:   patch_L330_belt_plane_ledger_item.py
#       modified:   planet_visualization_utilities.py
#
~
~
~
~
~
~
~
~
~
~
~
.git/COMMIT_EDITMSG [unix] (14:08 15/09/2026)   

git ls-remote origin HEAD
```

Note the new SHA. The gallery's drift check will read it.

---

## Part 2 — the gallery

Run from the gallery repo root, in this order. **The order is enforced by
fingerprints** — each patch expects the tree the previous one left.

### 7. The served surface rows

```
python patch_L305_item6b_served_surface_rows.py
python gallery_maintenance_run.py
```

Expect: 11 rows added, and the Earth scene UNCHANGED at 18 drawer groups.
This patch adds no names, so it must not move the picture at all.

### 8. The magnetosphere drawing code

```
python patch_L305_item5_magnetosphere_render.py
node documentation/smoke_earth_geometry.js gallery/feature_renderers.js gallery/earth_geometry.js
```

Expect: ALL CHECKS PASSED, 20 drawer groups, no warnings, nothing named
absent, and ten new legs about the two surfaces.

### 9. The fixture sync

```
python patch_L305_item5_fixture_sync.py
node documentation/smoke_earth_geometry.js gallery/feature_renderers.js gallery/earth_geometry.js
```

Expect: ALL CHECKS PASSED, and the border leg listing twenty markers —
sixteen red and four white.

### 10. The belts into Earth's equatorial plane

```
python patch_L231_belt_plane_gallery.py
node documentation/smoke_earth_geometry.js gallery/feature_renderers.js gallery/earth_geometry.js
```

Expect: ALL CHECKS PASSED, with ten more legs — each belt shares a plane
with the equator and the geostationary ring, each is flat, each hover names
the drawn width as a choice and gives the sourced span.

### 11. Serve and quote the tilt

```
python patch_L231_serve_and_quote_tilt.py
node documentation/smoke_earth_geometry.js gallery/feature_renderers.js gallery/earth_geometry.js
```

Expect: ALL CHECKS PASSED, including one leg per belt confirming the hover
carries 9.6 degrees with its model and epoch.

### 12. The full offline run

```
python gallery_maintenance_run.py
```

Expect: all six gating checkers pass.

**Note:** the Earth scene geometry checker may still report the white
outline finding if that turns out to be a real disagreement rather than
local drift. It gates. If it fires, Step 0 is the first thing to re-check.

### 13. Push the gallery

```
git add -A && git commit && git push
python gallery_maintenance_run.py --live
```

Expect, and this is a prediction stated before the run:

```
70 pointers: 56 match, 0 DRIFT, 1 UNIT MISMATCH, 13 could not be examined.
```

The one unit mismatch is `EARTH_VAN_ALLEN_OUTER_RADII` — its name declares
Earth radii and the config says L shell. That is the true state of the row
and it clears when L-322 teaches the checker to read the store's own
`# Unit:` line. The thirteen unexamined are four belt edges, the four Shue
and Jelinek coefficients with no unit suffix in their names, the four
planet poles and the galactic tide default.

If the match count is anything other than 56, stop and read the list rather
than assuming it is the same cause.

### 14. Look at the page

Open the Earth exhibit. Two things are new in the drawer:

- **Magnetopause** and **Bow Shock**. Both are far larger than the arrival
  frame, so they wait in the drawer rather than being lit on arrival. Turn
  them on together. The bow shock ends wider and shorter than the
  magnetopause; that is correct and is two papers' drawing limits, not a
  fact about the two boundaries.
- The belts are now in the same plane as the geostationary ring.

---

## If something stops

Every patch writes nothing unless its fingerprint matches, so a failure
leaves the tree exactly as it was. The message names the file and says what
it expected. Send it over and I will look.

## What is still open after all this

- **L-330**, the belt's shape: rings at the peaks versus the region between
  the served edges. Needs your eye on the plane fix first.
- **L-322**, teaching the maintenance checker to read units from the
  store's own comment line rather than from constant names. That clears
  five of the thirteen unexamined pointers and the one unit mismatch.
- **L-305 item 6b** remainder and the handoff edits from the start of the
  session.
