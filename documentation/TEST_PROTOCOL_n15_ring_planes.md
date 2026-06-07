TEST PROTOCOL -- N15 Ring-Plane Migration (Jupiter / Saturn / Neptune) -- all tests pass in the sandbox. copying to the github repo.
Tony + Claude | June 2026 | base SHA d33eb0c + N15 delta

SCOPE
Three changed files (rings now oriented by the IAU pole vector via
orient_to_planet_pole, replacing hardcoded axial-tilt rotations):
  jupiter_visualization_shells.py   ring system (had NO rotation; now oriented)
  saturn_visualization_shells.py    ring system + Enceladus plasma torus + radiation belts
  neptune_visualization_shells.py   ring system (retires the 32 deg X + 34 deg Z fudge)

NOT in this protocol: mercury_visualization_shells.py and venus_visualization_shells.py
(sodium-tail marker + Venus hover-text fixes) -- already tested this session.
Uranus rings were migrated in v23 (validated 0.0 deg) and are UNCHANGED here;
they appear below only as a regression anchor.

This is a DATA-CONTENT / GEOMETRY sweep on the live CUSTOM_SHELLS dispatch, not
control flow. py_compile alone is NOT sufficient -- an untouched file compiles
as cleanly as a correct one, and a builder that forgot the transform compiles
fine while rendering the ring in the wrong plane. Run the smoke test (Layer 1).

Division of labor: Claude did Layer 0 in the container (py_compile, ASCII, LF
on all three -- PASS). You own Layers 1-3: smoke on your repo, full-app launch
on Windows, and the Mode-5 render against the moons -- which is where this build
actually lives. A container cannot fetch Horizons, so no automated check can
confirm ring-vs-moon agreement; only your eyes can.

Promotion sequence (your pipeline): sandbox replace -> test (Layers 0-3) ->
copy to local repo -> commit + push -> confirm remote HEAD advanced -> record
new SHA -> project knowledge auto-syncs before next session.

----------------------------------------------------------------------
LAYER 0 -- File integrity [CRITICAL]   (~1 min) -- pass
----------------------------------------------------------------------
After copying the 3 files into the sandbox/repo, from the root:

  python -m py_compile jupiter_visualization_shells.py saturn_visualization_shells.py neptune_visualization_shells.py

Expect: no output (clean). Then confirm no Windows CRLF/BOM crept in on copy and
no non-ASCII was introduced:

  Look for non-ASCII (should report nothing new from this build):
  python - <<EOF
  for f in ['jupiter_visualization_shells.py','saturn_visualization_shells.py','neptune_visualization_shells.py']:
      s=open(f,encoding='utf-8').read()
      print(f, 'non-ascii:', [c for c in s if ord(c)>127][:5], '| CRLF:', '\r' in s)
  EOF

Claude container result: all three compile, 0 non-ASCII, LF (no CRLF).

----------------------------------------------------------------------
LAYER 1 -- Live-dispatch ring-plane smoke [CRITICAL]   (~5 sec) -- pass
----------------------------------------------------------------------
Drop smoke_ring_planes.py in the repo root and run:
  python smoke_ring_planes.py

Expect: "SMOKE RESULT: ALL PASS", exit 0. Per structure, the fitted plane-normal
vs the IAU pole should read ~0 deg (tolerance 2.0 deg -- slack for ring
thickness and the radiation belts' z-undulation):
  Jupiter ring_system, Saturn ring_system, Saturn enceladus_plasma_torus,
  Saturn radiation_belts, Neptune ring_system, Uranus ring_system (anchor).

What this checks: it resolves each builder via its CUSTOM_SHELLS string (the
LIVE path), calls it, fits a plane to the geometry, and compares that plane to
the pole computed by orient_to_planet_pole itself. So a builder that forgot the
transform (ring left in the body XY plane, ~tilt deg off) or wired the wrong
body string will FAIL here. Read the LOADED-FILE AUDIT block first -- confirm
each module resolved to the live sandbox/repo path, not an archived twin.

What this does NOT check: that the pole-derived plane matches the MOONS' plane.
That needs Horizons and is the Layer-3 render. If this smoke disagrees with the
handoff, the smoke wins.

----------------------------------------------------------------------
LAYER 2 -- Full-app pre-test   (~2 min) -- pass
----------------------------------------------------------------------
  python -m py_compile palomas_orrery.py        # not edited, cheap gate
  python palomas_orrery.py                       # launch on Windows directly

On Windows do NOT apply the SystemButtonFace -> gray90 swap (Linux/macOS only).
Confirm the GUI launches, no import errors in the console (the new
orient_to_planet_pole import in three files resolves), and you can select a
ringed planet and plot. Watch the console for any caught-and-printed exception
during a plot -- a swallowed exception is where a dropped trace hides.

----------------------------------------------------------------------
LAYER 3 -- Mode 5 visual gate [the real test]   (your eyes)
----------------------------------------------------------------------
For each body, plot the ring system together with that body's ring-plane moons
and confirm they are COPLANAR. The pole transform is validated only when the
rings line up with the moons -- the smoke cannot see this.

  [ ] NEPTUNE -- the headline fix. Plot rings + Despina + Galatea (Horizons,
      i ~ 0.05-0.07 deg to Neptune's equator). Previously the rings sat 8.57 deg
      off this plane; they should now lie IN it. This is the most visible change. -- correct. the rings are on the same plane as despina and galatea but not triton. 
  [ ] SATURN -- plot rings + inner moons (Pan, Prometheus, Mimas, Enceladus,
      Tethys...). Rings were ~5 deg off; should now match the moon plane. -- correct; except that the tethy plane is slightly off the rest, maybe a degree or so. comparing to jupiter, i notice that saturn does not have analytical orbits. can you check?
  [ ] SATURN torus + belts -- the Enceladus plasma torus and the six radiation
      belts were migrated too. Confirm they are coplanar with the Saturn rings
      and moons now (previously all shared the -26.73 deg X-tilt, so they were
      mutually consistent but ~5 deg off the moons). If rings match the moons
      but the torus/belts do not, one of those two builders is mis-wired. -- correct
  [ ] JUPITER -- subtle (obliquity ~3 deg, so ~2 deg shift). Plot rings + Metis,
      Adrastea, Amalthea, Thebe. Also confirm the ring INFO MARKER now rides the
      ring (it was previously placed independently on the +X axis; it should now
      sit on the rendered ring, like the other bodies). -- correct.

-- removed obsolete analytical orbit pipelines for Mars and Jupiter. 

Regression (confirm nothing else moved):  -- pass
  [ ] URANUS rings still coplanar with the Uranus moons (UNCHANGED this build -- correct
      if Uranus shifted, something global broke).
  [ ] Other shells of Jupiter/Saturn/Neptune (magnetosphere, bow shock, Hill
      sphere, plasma torus geometry, radiation-belt shape) look unchanged apart
      from the plane reorientation. -- correct
  [ ] Bow shocks (last session's work) still render and nest correctly. -- correct

----------------------------------------------------------------------
RECORD (carry into the handoff)
----------------------------------------------------------------------
- Layers 0-2 pass/fail. -- pass
- Layer 1 smoke: ALL PASS? note any structure's angle if non-zero. -- pass
- Mode-5 verdict per body: Neptune rings vs Despina/Galatea; Saturn rings +
  torus + belts vs moons; Jupiter rings vs Metis/Adrastea/Amalthea/Thebe +
  marker-on-ring; Uranus regression unchanged. -- pass
- Housekeeping: saturn_visualization_shells.py rotate_points import is now DEAD
  (unused after N15) -- annotate "# DEAD: unused after N15" or remove (D3). -- # dead
- Base SHA the build was integrated onto: d33eb0c.
- New HEAD SHA after your push: __________  (send to Claude for the handoff).
