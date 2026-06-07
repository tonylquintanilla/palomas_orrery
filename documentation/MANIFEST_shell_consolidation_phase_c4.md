# MANIFEST: Shell Consolidation Step 3 -- Phase C4 (Saturn, Uranus, Neptune)

**Project:** Paloma's Orrery | Plotting Consolidation Step 3
**Date:** May 17, 2026 (v2, revised after Opus 4.6 review)
**Source prompt:** `PROMPT_shell_consolidation_for_opus_v6.md`
**Phase C3 handoff:** `HANDOFF_shell_consolidation_phase_c3.md` (May 16, 2026)
**Decisions reply:** `REPLY_c4_decisions_for_opus_4_7.md` (May 17, 2026, Tony + Opus 4.6)
**Manifest by:** Anthropic's Claude Opus 4.7 (audit + draft + revision)
**Pre-implementation review:** Anthropic's Claude Opus 4.6 (May 17, 2026)
**For execution by:** Anthropic's Claude Opus 4.6 (implementation) + Tony (integrator)

---

## 1. Phase C4 Scope and Execution Model

### What Phase C4 delivers

Phase C4 is the **final migration phase** of Step 3. It moves the three remaining
gas/ice giants -- Saturn, Uranus, and Neptune -- to the unified config-driven
dispatch, leaving only the Sun on `create_planet_visualization()`. After Phase C4:

- **Saturn** renders via `SHELL_CONFIGS['Saturn']` (6 sphere shells: core, metallic
  hydrogen, molecular hydrogen, cloud layer mesh3d, upper atmosphere, hill sphere)
  and `CUSTOM_SHELLS['Saturn']` (4 entries: magnetosphere, enceladus_plasma_torus,
  radiation_belts, ring_system).
- **Uranus** renders via `SHELL_CONFIGS['Uranus']` (5 sphere shells: core, mantle,
  cloud layer mesh3d, upper atmosphere, hill sphere) and `CUSTOM_SHELLS['Uranus']`
  (3 entries: magnetosphere, radiation_belts, ring_system).
- **Neptune** renders via `SHELL_CONFIGS['Neptune']` (5 sphere shells: core, mantle,
  cloud layer mesh3d, upper atmosphere, hill sphere) and `CUSTOM_SHELLS['Neptune']`
  (3 entries: magnetosphere, radiation_belts, ring_system).
- `rotate_to_sunward()` in `orrery_rendering.py` gets its FIRST real implementation
  of the `magnetic_tilt_deg` parameter (Phase C1 placeholder). Used by Uranus
  (60 deg). Saturn passes 0 (aligned dipole). Neptune passes 0 (internal
  region-specific handling, see Section 6.5).
- Five pre-existing issues in the source files are corrected during the migration:
  Uranus magnetosphere missing info marker (added), Uranus radiation belt dead-code
  cleanup (stripped), Saturn ring tooltip Jupiter-text copy-paste (rewritten),
  Neptune `create_neptune_field_lines` dead function (stripped), several info-marker
  positions referencing pre-rotation coordinates (corrected to post-transform).

After Phase C4:

| Component | Before C4 | After C4 |
|---|:---:|:---:|
| Bodies in SHELL_CONFIGS | 9 | 12 |
| Total sphere shell configs | 52 | 68 (+16: 6+5+5) |
| Bodies in CUSTOM_SHELLS | 5 | 8 |
| Total custom entries | 11 | 21 (+10: 4+3+3) |
| Bodies still on old dispatch | 4 | 1 (Sun) |
| `rotate_to_sunward()` exercised by | 5 bodies | 8 bodies (+Saturn, Uranus, Neptune) |
| `magnetic_tilt_deg` wired live | 0 bodies | 1 body (Uranus, 60 deg) |
| `sun_position` wired | No (Phase D) | No (Phase D) |

### What Phase C4 explicitly does NOT do

- Does NOT retire `create_planet_visualization()`. The Sun still uses it.
  Phase D retires it.
- Does NOT wire `sun_position` from ephemeris. Magnetospheres for Saturn, Uranus,
  Neptune (and previously Earth, Venus, Mars, Jupiter, Mercury) assume Sun at
  origin. Phase D handles this.
- Does NOT redesign `create_magnetosphere_shape()`. The default convention
  (-X sunward, Z = rotation/magnetic axis aligned) is preserved.
- Does NOT modify Saturn's six per-shell sun direction indicators in the old
  dispatch path -- they're removed automatically when Saturn migrates to the
  unified dispatch (same mechanism as Jupiter C3).
- Does NOT modify Neptune's `create_neptune_magnetic_poles()` traces (4 traces:
  magnetic center diamond, axis dashed line, north pole, south pole). They have
  inherent meaning (color-coded poles, diamond center marker) and already carry
  hovertext on their single points. The single-info-marker pattern applies to
  geometry-covering traces, not to inherently single-point informational markers.
- Does NOT touch `palomas_orrery.py`. The 26 GUI checkboxes for Saturn/Uranus/
  Neptune shells continue working through the unified dispatch.
- Does NOT remove the `print()` debug line at line 766 in `create_neptune_magnetic_poles`
  (`Returning {n} magnetic field traces`) or the error-handler `print()` at line 615
  in the magnetosphere builder. Out of scope, mechanical purity.
- Does NOT fix the Saturn radiation belt double-offset pattern (lines 873-890).
  Same kind of pre-existing issue as Uranus belts but Tony's reply did not call
  it out. Flagged in Decision Log as a Phase D / Mode 5 item.
- Does NOT fix the Neptune ring info marker rotation mismatch (line 1741 uses
  `neptune_tilt` while ring geometry uses 32 deg + 34 deg rotations). Flagged in
  Decision Log as a Phase D / Mode 5 item -- correcting it requires editorial
  decisions about Neptune's ring orientation that exceed C4's mechanical scope.
- Does NOT remove the dead Saturn upper atmosphere `_info` strings or other
  standalone `_info` variables. They remain available for tooltip wiring;
  Phase D rewires tooltips from configs.

### Execution order (canonical)

Per Tony Q8, the manifest is structured **by body**. Three top-level sections,
each independently verifiable. Saturn first (closest to Jupiter pattern), then
Uranus (introduces `magnetic_tilt_deg`), then Neptune (most complex).

1. **Pre-flight verification** (Section 2)
2. **Implement `magnetic_tilt_deg` in `rotate_to_sunward()`** (Section 3) --
   enables Section 5 (Uranus). Must precede Saturn/Uranus/Neptune sections.
3. **Saturn migration** (Section 4) -- Session 1 boundary
4. **Uranus migration** (Section 5) -- Session 2A boundary
5. **Neptune migration** (Section 6) -- Session 2B boundary
6. **Final verification** (Section 7)

If any verification step fails, STOP and resolve before proceeding.

### Session structure

Per Tony Q8 + the C3 implementation experience, suggested session boundaries:

- **Session 1**: Section 2 (preflight) + Section 3 (`rotate_to_sunward` mod) +
  Section 4 (Saturn). Largest body, establishes the gas giant pattern. Verify
  fully before proceeding.
- **Session 2**: Section 5 (Uranus) + Section 6 (Neptune). Uranus introduces
  `magnetic_tilt_deg=60` wiring (Section 3 already in place). Neptune is
  mechanical apart from the dead function strip.
- Alternative split: Session 2 (Uranus) + Session 3 (Neptune) if context
  pressure demands.

Implementing Claude: if Section 4 (Saturn) verifies cleanly but Uranus or Neptune
work requires session handoff, write a partial handoff at the section boundary --
the codebase remains functional with mixed-state dispatch (any bodies not yet
migrated continue through the old path).

### Why this order matters

Section 3 (`rotate_to_sunward` modification) is independent of Saturn migration
but logically C4 work because it's needed for Section 5 (Uranus). Doing it
before Saturn means Saturn's verification benefits from the same machinery
that Uranus relies on. Saturn passes `magnetic_tilt_deg=0` so the new code
path is exercised at the no-op edge case before Uranus exercises it for real.

Section 4 (Saturn) is the most similar to Jupiter C3 -- 6 sphere shells (mesh3d
cloud layer like Jupiter), 4 custom builders, magnetosphere with no bow shock
(same as Jupiter). It establishes the gas giant pattern for ice giants to follow.

Section 5 (Uranus) is the FIRST live use of `magnetic_tilt_deg`. Plus Uranus has
TWO pre-existing issues that get corrected during migration: missing magnetosphere
info marker (Q2) and radiation belt dead code (Q3). The migration is no longer
purely mechanical.

Section 6 (Neptune) is the most complex by trace count (6 magnetosphere traces
including poles/axis/center; 12 radiation belt traces including FAC) but is
fully mechanical for the dispatch migration. Two pre-existing source code
quirks get cleaned up: dead `create_neptune_field_lines` (Q4) and Neptune
radiation-belt-and-FAC info marker positions referencing pre-rotation coordinates.

---

## 2. Pre-flight Verification

### 2.1 Confirm Phase A+B+C1+C2+C3 are in place

```bash
python3 -c "
from orrery_rendering import (build_sphere_shell, create_info_marker,
                                rotate_to_sunward, create_ring_points)
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS

expected_sphere = {'Mercury', 'Moon', 'Planet 9', 'Pluto', 'Eris',
                   'Venus', 'Mars', 'Earth', 'Jupiter'}
expected_custom = {'Mercury', 'Venus', 'Mars', 'Earth', 'Jupiter'}

for body in expected_sphere:
    assert body in SHELL_CONFIGS, 'Phase A-C3 body %s missing from SHELL_CONFIGS' % body
for body in expected_custom:
    assert body in CUSTOM_SHELLS, 'Phase A-C3 custom body %s missing' % body

# Phase C4 bodies not yet present
for body in ('Saturn', 'Uranus', 'Neptune'):
    assert body not in SHELL_CONFIGS, '%s already in SHELL_CONFIGS - re-run?' % body
    assert body not in CUSTOM_SHELLS, '%s already in CUSTOM_SHELLS - re-run?' % body

assert len(SHELL_CONFIGS) == 9, 'Expected 9 bodies, got %d' % len(SHELL_CONFIGS)
assert len(CUSTOM_SHELLS) == 5, 'Expected 5 custom bodies, got %d' % len(CUSTOM_SHELLS)
assert len(SHELL_CONFIGS['Jupiter']) == 6
assert len(CUSTOM_SHELLS['Jupiter']) == 4

print('Phase A-C3 baseline OK (9 + 5 bodies)')
"
```

### 2.2 Confirm ring helper promotion is complete (Phase C3 work)

```bash
python3 -c "
from orrery_rendering import create_ring_points
import saturn_visualization_shells as s
import uranus_visualization_shells as u
import neptune_visualization_shells as n

# Saturn no longer has the local helper
assert not hasattr(s, 'create_ring_points_saturn'), 'Saturn local ring helper survived'

# Saturn/Uranus/Neptune all import from orrery_rendering
for mod in (s, u, n):
    src = open(mod.__file__).read()
    assert 'from orrery_rendering import create_ring_points' in src, \
        '%s missing orrery_rendering import' % mod.__name__
    assert 'create_ring_points_saturn' not in src, \
        '%s has stale create_ring_points_saturn reference' % mod.__name__

print('C3 ring helper promotion verified')
"
```

### 2.3 Confirm CENTER_BODY_RADII has all three bodies

```bash
python3 -c "
from constants_new import CENTER_BODY_RADII, KM_PER_AU
for body, expected_km in [('Saturn', 60268), ('Uranus', 25559), ('Neptune', 24764)]:
    r_km = CENTER_BODY_RADII[body]
    r_au = r_km / KM_PER_AU
    assert r_km == expected_km, '%s radius %f != %f' % (body, r_km, expected_km)
    print('%s: %.2f km = %.4e AU' % (body, r_km, r_au))
"
# Expected:
# Saturn:  60268.00 km = 4.0287e-04 AU
# Uranus:  25559.00 km = 1.7085e-04 AU
# Neptune: 24764.00 km = 1.6553e-04 AU
```

### 2.4 Confirm Saturn/Uranus/Neptune dispatch blocks present in planet_visualization.py

```bash
grep -n "if planet_name == 'Saturn':" planet_visualization.py
# Expected: one match around line 744

grep -n "if planet_name == 'Uranus':" planet_visualization.py
# Expected: one match around line 766

grep -n "if planet_name == 'Neptune':" planet_visualization.py
# Expected: one match around line 784
```

If any are missing or already replaced with delegations, STOP -- unexpected
state.

### 2.5 Confirm `create_neptune_field_lines` dead function exists for stripping

```bash
grep -n "^def create_neptune_field_lines" neptune_visualization_shells.py
# Expected: one match around line 770

# Confirm it is dead code (zero callers)
grep -c "create_neptune_field_lines" neptune_visualization_shells.py
# Expected: 1 (the definition line only). If > 1, function is called somewhere.

grep -c "create_neptune_field_lines" *.py | grep -v ":0$" | grep -v "neptune_visualization_shells.py:1"
# Expected: empty. Confirms no other module calls it.
```

If callers exist, STOP -- the function isn't actually dead.

### 2.6 Confirm Uranus magnetosphere is missing info marker (pre-existing)

```bash
python3 -c "
import uranus_visualization_shells as m
# Use an off-center test position so create_sun_direction_indicator
# emits its 2 traces. At origin (dist < 1e-10) the helper returns [],
# which would make the assertion misleading.
traces = m.create_uranus_magnetosphere((1.0, 0.0, 0.0))
print('Uranus magnetosphere pre-C4 (off-center): %d traces' % len(traces))
# Expected: 3 (1 geometry + 2 sun direction indicator traces, NO info marker)
# After C4 (off-center): 2 (1 geometry + 1 info marker, sun indicator stripped)
# After C4 (origin):     2 (1 geometry + 1 info marker)
"
```

Verifies the pre-existing omission. C4 adds the info marker.

### 2.7 Backup files Phase C4 will touch

Before any edits:

```
orrery_rendering.py                 -> orrery_rendering.py.phaseC4_backup
shell_configs.py                    -> shell_configs.py.phaseC4_backup
planet_visualization.py             -> planet_visualization.py.phaseC4_backup
saturn_visualization_shells.py      -> saturn_visualization_shells.py.phaseC4_backup
uranus_visualization_shells.py      -> uranus_visualization_shells.py.phaseC4_backup
neptune_visualization_shells.py     -> neptune_visualization_shells.py.phaseC4_backup
```

Six files. All will be modified.

### 2.8 Line ending and ASCII verification

```bash
for f in orrery_rendering.py shell_configs.py planet_visualization.py \
         saturn_visualization_shells.py uranus_visualization_shells.py \
         neptune_visualization_shells.py; do
    file "$f" | grep -q CRLF && echo "FAIL: $f CRLF" || echo "OK LF: $f"
done

python3 -c "
files = ['orrery_rendering.py', 'shell_configs.py', 'planet_visualization.py',
         'saturn_visualization_shells.py', 'uranus_visualization_shells.py',
         'neptune_visualization_shells.py']
for f in files:
    with open(f, 'rb') as fh:
        content = fh.read().decode('utf-8', errors='replace')
    issues = sum(1 for c in content if ord(c) > 127)
    print('%-45s %s' % (f, 'OK ASCII' if not issues else 'FAIL: %d non-ASCII' % issues))
"
```

All six files must be LF and ASCII.

---

## 3. Implement `magnetic_tilt_deg` in `rotate_to_sunward()`

### 3.1 Background and design decision

The `magnetic_tilt_deg` parameter was added to `rotate_to_sunward()` in Phase C1
as a placeholder (currently a no-op; see `orrery_rendering.py` lines 264-267).
Phase C4 implements it for the first time, driven by Uranus's 60-degree dipole-
vs-rotation-axis offset (Tony Q1: "implement magnetic_tilt_deg=60 now ... this
is fundamental to the shell structure").

**Tony's directive (REPLY_c4_decisions Q1):**

> Add a second Rodrigues rotation about the planet's rotation axis by
> `magnetic_tilt_deg` degrees AFTER the sunward rotation.

**Implementation approach (confirmed by Opus 4.6 review, May 2026):**
Apply the magnetic tilt as a rotation about the **X axis** (the
bow-shock-to-sunward direction in the default geometry frame) BEFORE
the sunward rotation. Tony's literal directive "rotate about the
rotation axis after sunward" cannot produce the intended visual because
the magnetosphere shape generated by `create_magnetosphere_shape()` is
symmetric about Z; rotation about Z is a no-op. The X-axis-before
operation is the only rotation that tilts the dipole while keeping the
bow shock on the sun line.

**Physics anchored to `create_magnetosphere_shape()` (verified by Opus 4.6):**

The shape's coordinates are generated as:
```
y = params['equatorial_radius'] * rho * cos(theta)   # 27.5 R_U for Uranus
z = params['polar_radius']      * rho * sin(theta)   # 17.5 R_U for Uranus
```

The cross-section perpendicular to X is an ellipse with the **wide axis along
Y** (equatorial, perpendicular to dipole) and the **narrow axis along Z**
(polar, along dipole). This is the magnetopause being more compressed in
the polar direction than the equatorial -- standard physics.

Symmetries of the shape under candidate rotations:

| Rotation axis | Effect on geometry | Effect on bow shock | Verdict |
|---------------|--------------------|--------------------|---------|
| About X (any angle) | Tilts YZ cross-section -- wide/narrow axes rotate. The dipole axis (formerly Z) sweeps into the YZ plane. | Stays at -X. | **CORRECT** |
| About Z (the body's rotation axis) | Mixes X and Y. | Moves off -X. | Physics error |
| About Y (literal Y axis) | Mixes X and Z. | Tilts up/down. | Physics error |

The X-axis rotation is the only one that produces a visible dipole tilt
while preserving the sunward bow shock orientation. After the subsequent
sunward Rodrigues rotation, the entire transformed structure (bow shock +
tilted dipole) is carried onto the actual sun direction.

**Result for Uranus (60 deg, X-axis):** The magnetic equator (the wide
direction of the magnetosphere) is tilted 60 degrees from the geometric
equator. This is the Voyager 2 "Uranus has a sideways magnetic field"
visual.

**Sign convention:** The implementation rotates by `+magnetic_tilt_deg`
about `+X` using the standard right-hand rule. For Uranus with
`magnetic_tilt_deg=60`, the +Z dipole axis tilts toward **-Y** (verified
against the rotation matrix: `new_pz = py*sin + pz*cos` maps the +Z unit
vector to `(0, -sin(60), cos(60)) = (0, -0.866, 0.5)`).

Uranus's actual dipole orientation in inertial space varies with rotation
phase -- the choice of +Y vs -Y direction is editorial and can be flipped
in Mode 5 if the dominant Voyager-2-era convention prefers the other sign.
Negating the angle flips the dipole pole direction.

### 3.2 Code change in `orrery_rendering.py`

Locate the existing `rotate_to_sunward()` function (line 180-269). Replace the
current implementation. Key changes:

1. Apply the X-axis magnetic tilt rotation FIRST (lines marked NEW below).
2. Existing sunward rotation logic preserved verbatim.
3. The placeholder NOTE block (lines 264-267) is removed (the placeholder is
   no longer needed -- magnetic_tilt_deg is now live).
4. Docstring updated to describe the new behavior.

**Replace the existing `rotate_to_sunward()` function body with:**

```python
def rotate_to_sunward(px, py, pz, center_position=(0, 0, 0),
                     sun_position=(0, 0, 0), magnetic_tilt_deg=0):
    """Rotate points from default -X sunward to actual sunward direction.

    Default geometry generation convention: magnetosphere structures (bow
    shock, magnetotail, etc.) are generated with -X as the sunward direction
    and Z as the magnetic dipole axis (also = rotation axis when the two are
    aligned). For off-center views (body offset from origin) or body-centered
    views where the Sun is offset, this function rotates the geometry to
    point toward the actual sunward direction.

    When magnetic_tilt_deg > 0, an additional rotation about the bow-shock-to-
    tail axis (X axis in the default frame) is applied BEFORE the sunward
    rotation. This tilts the magnetic dipole axis (originally aligned with
    Z) into the YZ plane by magnetic_tilt_deg degrees, modeling the offset
    between the magnetic dipole and the rotation axis. The bow-shock-to-tail
    direction is preserved. This is mathematically equivalent to applying
    the tilt about the actual sunward direction AFTER the sunward rotation.

    Parameters:
        px, py, pz (np.ndarray): Point coordinates in default frame
        center_position (tuple): (x, y, z) AU position of the body's center
        sun_position (tuple): (x, y, z) AU position of the Sun.
                              Default (0, 0, 0) = Sun at origin (heliocentric).
                              Phase D wires actual Sun position from ephemeris.
        magnetic_tilt_deg (float): Angular offset between rotation axis and
                                    magnetic dipole axis (degrees).
                                    Default 0 = aligned dipoles (Mercury, Venus,
                                    Mars, Saturn, Jupiter, Neptune passes 0
                                    -- internal handling). Used live by Uranus
                                    (60 deg) as of Phase C4. Earth (~11 deg)
                                    and Jupiter (~10 deg) eligible for Phase D
                                    activation.

    Returns:
        (rx, ry, rz): rotated point arrays

    Module updated: May 2026 with Anthropic's Claude Opus 4.7
    """
    import math
    import numpy as np

    # Step 1: Magnetic tilt about the X axis (bow-shock-to-tail) BEFORE sunward
    # rotation. Tilts the magnetic dipole axis (originally Z) into the YZ
    # plane by magnetic_tilt_deg. Preserves bow-shock-to-tail orientation.
    if magnetic_tilt_deg != 0:
        angle_rad = math.radians(magnetic_tilt_deg)
        cos_t = math.cos(angle_rad)
        sin_t = math.sin(angle_rad)
        new_py = py * cos_t - pz * sin_t
        new_pz = py * sin_t + pz * cos_t
        py = new_py
        pz = new_pz

    # Step 2: Sunward rotation. Maps default -X to actual sunward direction
    # via Rodrigues rotation.
    center_x, center_y, center_z = center_position
    sun_x, sun_y, sun_z = sun_position

    # Vector from body center toward Sun
    dx, dy, dz = sun_x - center_x, sun_y - center_y, sun_z - center_z
    dist = math.sqrt(dx**2 + dy**2 + dz**2)

    if dist < 1e-12:
        # Body and Sun coincident (or both at origin): default -X convention
        return px, py, pz

    # Actual sunward unit vector
    sx, sy, sz = dx / dist, dy / dist, dz / dist

    # Default sunward direction (geometry convention: -X)
    fx, fy, fz = -1.0, 0.0, 0.0

    # Dot product (cosine of angle between default and actual sunward)
    dot = fx * sx + fy * sy + fz * sz

    if dot > 0.9999:
        # Already aligned
        return px, py, pz

    if dot < -0.9999:
        # Anti-parallel: 180 deg rotation around Z axis
        return -px, -py, pz

    # Cross product gives rotation axis
    ax = fy * sz - fz * sy
    ay = fz * sx - fx * sz
    az = fx * sy - fy * sx
    alen = math.sqrt(ax**2 + ay**2 + az**2)
    ax, ay, az = ax / alen, ay / alen, az / alen

    # Rodrigues' rotation formula
    angle = math.acos(max(-1.0, min(1.0, dot)))
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)

    rx = np.empty_like(px, dtype=float)
    ry = np.empty_like(py, dtype=float)
    rz = np.empty_like(pz, dtype=float)

    for i in range(len(px)):
        p = (float(px[i]), float(py[i]), float(pz[i]))
        # v*cos(a) + (k x v)*sin(a) + k*(k.v)*(1-cos(a))
        kdotv = ax * p[0] + ay * p[1] + az * p[2]
        rx[i] = p[0] * cos_a + (ay * p[2] - az * p[1]) * sin_a + ax * kdotv * (1 - cos_a)
        ry[i] = p[1] * cos_a + (az * p[0] - ax * p[2]) * sin_a + ay * kdotv * (1 - cos_a)
        rz[i] = p[2] * cos_a + (ax * p[1] - ay * p[0]) * sin_a + az * kdotv * (1 - cos_a)

    return rx, ry, rz
```

### 3.3 Edit method

Use `str_replace` on `orrery_rendering.py` with old_str = the entire existing
`def rotate_to_sunward(...)` block (lines 180-269 in the current source) and
new_str = the block above. Match on the full function signature and body to
ensure the replacement is unique.

After the edit, confirm:

```bash
python3 -m py_compile orrery_rendering.py
```

### 3.4 Verification after Section 3

```bash
python3 -c "
import math
import numpy as np
from orrery_rendering import rotate_to_sunward

# Test 1: magnetic_tilt_deg=0 is a no-op (regression check)
px = np.array([1.0, 0.0, 0.0])
py = np.array([0.0, 1.0, 0.0])
pz = np.array([0.0, 0.0, 1.0])
rx, ry, rz = rotate_to_sunward(px, py, pz, magnetic_tilt_deg=0)
assert np.allclose(rx, px) and np.allclose(ry, py) and np.allclose(rz, pz), \
    'magnetic_tilt_deg=0 changed coordinates (must be no-op)'
print('magnetic_tilt_deg=0 no-op: PASS')

# Test 2: magnetic_tilt_deg=90 around X rotates Y to Z and Z to -Y
# (For a unit vector originally on +Y, after 90-deg rotation about X it lands on +Z.)
px = np.array([0.0])
py = np.array([1.0])
pz = np.array([0.0])
rx, ry, rz = rotate_to_sunward(px, py, pz, magnetic_tilt_deg=90)
# After tilt: py=0, pz=1. Sunward rotation is no-op (sun at origin = body at origin).
assert abs(rx[0]) < 1e-9 and abs(ry[0]) < 1e-9 and abs(rz[0] - 1.0) < 1e-9, \
    'magnetic_tilt_deg=90 did not map +Y to +Z'
print('magnetic_tilt_deg=90 about X (Y -> Z): PASS')

# Test 3: magnetic_tilt_deg=60 combined with sunward rotation. With body at
# default origin and sun at default origin, sunward rotation is a no-op, so
# magnetic_tilt_deg=60 should be the only transformation.
px = np.array([0.0])
py = np.array([0.0])
pz = np.array([1.0])  # On +Z (rotation axis = magnetic axis pre-tilt)
rx, ry, rz = rotate_to_sunward(px, py, pz, magnetic_tilt_deg=60)
# After 60-deg X-axis rotation: +Z goes to (0, -sin60, cos60) = (0, -0.866, 0.5)
expected_y = -math.sin(math.radians(60))
expected_z = math.cos(math.radians(60))
assert abs(ry[0] - expected_y) < 1e-9 and abs(rz[0] - expected_z) < 1e-9, \
    'magnetic_tilt_deg=60 did not produce expected rotation: got y=%f z=%f, expected y=%f z=%f' % \
    (ry[0], rz[0], expected_y, expected_z)
print('magnetic_tilt_deg=60 about X axis: PASS')

# Test 4: magnetic_tilt_deg combines with sunward rotation order check
# Body at (0, 0, 0), sun at (1, 0, 0). Actual sunward = +X (the OPPOSITE of
# default -X). Anti-parallel case -> 180-deg about Z. Combined with 60-deg
# X tilt applied FIRST.
px = np.array([1.0])
py = np.array([0.0])
pz = np.array([0.0])  # On +X (anti-sunward in default = tail tip)
rx, ry, rz = rotate_to_sunward(px, py, pz, center_position=(0,0,0),
                                sun_position=(1,0,0), magnetic_tilt_deg=60)
# After X-tilt: (1, 0, 0) -> (1, 0, 0) (point on X axis is invariant under X rotation)
# After sunward rotation (anti-parallel = 180 about Z): (1, 0, 0) -> (-1, 0, 0)
# So the tail tip ends up on the -X side, which is now anti-sunward. Correct.
assert abs(rx[0] + 1.0) < 1e-9, 'Sunward rotation after X-tilt failed for X-axis point'
print('magnetic_tilt_deg=60 + sunward rotation order: PASS')

print()
print('Section 3 verification complete')
"
```

If all four assertions pass, Section 3 is correct and Section 5 can rely on it.

If any fail, STOP and debug -- the magnetic_tilt_deg implementation has a bug.

---

## 4. Saturn Migration (Session 1)

Saturn has 6 sphere shells, 4 custom builders (magnetosphere, enceladus_plasma_torus,
radiation_belts, ring_system), and 6 per-shell sun direction indicators that get
stripped on migration. One pre-existing content error to fix: the standalone
`saturn_ring_system_info` tooltip references Jupiter's moons (Metis, Adrastea,
Amalthea, Thebe) -- this is a copy-paste from Jupiter that gets corrected in
the CUSTOM_SHELLS tooltip rewrite.

### 4.1 Saturn sphere configs

Saturn has 6 sphere shells. Five are standard scatter3d (`create_sphere_points`),
one is mesh3d (cloud layer, resolution=24). Per the source audit:

| Shell | n_points | radius_fraction | opacity | color | marker_size | Geom |
|---|---:|---:|---:|---|---:|---|
| core | 25 | 0.6 | 1.0 | rgb(240, 240, 255) | 4.0 | scatter3d |
| metallic_hydrogen | 25 | 0.9 | 1.0 | rgb(225, 220, 235) | 3.5 | scatter3d |
| molecular_hydrogen | 25 | 0.99 | 1.0 | rgb(220, 200, 175) | 3.0 | scatter3d |
| cloud_layer | n/a | 1.0 | 1.0 | rgb(210, 180, 140) | n/a | mesh3d (resolution=24) |
| upper_atmosphere | 20 | 1.1 | 0.5 | rgb(240, 245, 250) | 3.0 | scatter3d |
| hill_sphere | 20 | 1120 | 0.3 | rgb(0, 255, 0) | 2.0 | scatter3d |

Note: Saturn's `metallic_hydrogen` and `molecular_hydrogen` colors and opacities
must be extracted from the source file (lines 121-198 and 198-278 approximately)
via the auto-generation script -- the manifest values above are documented
estimates and the script must produce exact source values.

### 4.2 Auto-generation script for Saturn sphere configs

Save as `generate_phase_c4_saturn_configs.py` and run from the project directory.
The script parses the source module via AST, extracts the `layer_info` dict
and `create_sphere_points(n_points=...)` argument from each shell builder, and
emits a config block ready to paste into `shell_configs.py`. The same script
is reused for Uranus (Section 5.2) and Neptune (Section 6.2) by changing
`BODY`, `PATH`, and `SHELLS`.

```python
# generate_phase_c4_saturn_configs.py
"""Auto-generate Saturn sphere config blocks for Phase C4 shell_configs.py.

Parses saturn_visualization_shells.py via AST to extract each sphere builder's
layer_info dict and n_points argument. Emits a block of dict literals in the
shell_configs.py format. Run, inspect, then paste into the SHELL_CONFIGS
dictionary.
"""
import ast
import sys
import textwrap

BODY = 'Saturn'
PATH = 'saturn_visualization_shells.py'

# (shell_key, builder_function_name, info_string_variable_name)
SHELLS = [
    ('core',               'create_saturn_core_shell',               'saturn_core_info'),
    ('metallic_hydrogen',  'create_saturn_metallic_hydrogen_shell',  'saturn_metallic_hydrogen_info'),
    ('molecular_hydrogen', 'create_saturn_molecular_hydrogen_shell', 'saturn_molecular_hydrogen_info'),
    ('cloud_layer',        'create_saturn_cloud_layer_shell',        'saturn_cloud_layer_info'),
    ('upper_atmosphere',   'create_saturn_upper_atmosphere_shell',   'saturn_upper_atmosphere_info'),
    ('hill_sphere',        'create_saturn_hill_sphere_shell',        'saturn_hill_sphere_info'),
]
MESH3D_SHELLS = {'cloud_layer'}
MESH3D_RESOLUTION = 24

# Marker sizes from source audit (Section 4.1)
MARKER_SIZES = {
    'core': 4.0, 'metallic_hydrogen': 3.5, 'molecular_hydrogen': 3.0,
    'upper_atmosphere': 3.0, 'hill_sphere': 2.0,
}

def get_func_body(tree, func_name):
    """Return the AST body of a top-level function by name."""
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            return node
    raise KeyError(func_name)

def find_layer_info(func_node):
    """Find the assignment `layer_info = {...}` and return its dict node."""
    for stmt in ast.walk(func_node):
        if isinstance(stmt, ast.Assign):
            for tgt in stmt.targets:
                if isinstance(tgt, ast.Name) and tgt.id == 'layer_info':
                    if isinstance(stmt.value, ast.Dict):
                        return stmt.value
    raise ValueError('layer_info dict not found in %s' % func_node.name)

def dict_to_python(d):
    """Convert an ast.Dict (string-keyed, literal-valued) to a Python dict."""
    out = {}
    for k, v in zip(d.keys, d.values):
        if not isinstance(k, ast.Constant):
            continue
        out[k.value] = ast.literal_eval(v) if not isinstance(v, ast.JoinedStr) else None
    return out

def find_n_points(func_node):
    """Find the n_points argument to create_sphere_points()."""
    for stmt in ast.walk(func_node):
        if isinstance(stmt, ast.Call):
            func = stmt.func
            name = func.attr if isinstance(func, ast.Attribute) else getattr(func, 'id', '')
            if name == 'create_sphere_points':
                for kw in stmt.keywords:
                    if kw.arg == 'n_points' and isinstance(kw.value, ast.Constant):
                        return kw.value.value
    return None

def emit_block():
    src = open(PATH, 'rb').read().decode('utf-8')
    tree = ast.parse(src)

    print("    '%s': {" % BODY)
    print()
    for shell_key, func_name, info_var in SHELLS:
        try:
            func = get_func_body(tree, func_name)
            li = find_layer_info(func)
            info = dict_to_python(li)
        except (KeyError, ValueError) as e:
            print("        # %s: SKIPPED -- %s" % (shell_key, e), file=sys.stderr)
            continue

        radius_fraction = info.get('radius_fraction')
        color = info.get('color')
        opacity = info.get('opacity', 1.0)
        name = info.get('name', shell_key.replace('_', ' ').title())

        print("        '%s': {" % shell_key)
        print("            'name': '%s'," % name)
        print("            'color': '%s'," % color)
        print("            'opacity': %r," % opacity)
        print("            'radius_fraction': %r," % radius_fraction)
        if shell_key in MESH3D_SHELLS:
            print("            'geometry_type': 'mesh3d',")
            print("            'mesh_resolution': %d," % MESH3D_RESOLUTION)
        else:
            n_points = find_n_points(func) or 20
            print("            'n_points': %d," % n_points)
            print("            'marker_size': %r," % MARKER_SIZES[shell_key])
        print("            'hover_text': %s," % info_var)
        print("        },")
        print()
    print("    },")

if __name__ == '__main__':
    emit_block()
```

Usage:
```bash
python3 generate_phase_c4_saturn_configs.py > saturn_block.txt
# Inspect saturn_block.txt against the table in Section 4.1.
# Hover text uses the existing module-level *_info string symbols
# (already imported into shell_configs.py from prior phases).
```

After running, manually verify:

- All 6 shells have `radius_fraction`, `opacity`, `color`, `name`, `hover_text`.
- `cloud_layer` has `geometry_type='mesh3d'` and `mesh_resolution=24`.
- All others have `marker_size` (4.0 / 3.5 / 3.0 / 3.0 / 2.0).
- All non-mesh3d shells have `n_points` (25 / 25 / 25 / 20 / 20).

For Uranus, change `BODY = 'Uranus'`, `PATH = 'uranus_visualization_shells.py'`,
and the `SHELLS` list to the 5 Uranus shells (Section 5.1). For Neptune, the
5 Neptune shells (Section 6.1). Marker sizes and mesh3d shells stay the same.

### 4.3 Saturn imports (top of `saturn_visualization_shells.py`)

Saturn already imports `create_ring_points` from `orrery_rendering` (Phase C3).
Add the two C4 imports:

```python
from orrery_rendering import create_ring_points, rotate_to_sunward, create_info_marker
```

Method: `str_replace` on the existing line
`from orrery_rendering import create_ring_points` (line 22) with the augmented
line above.

The `from shared_utilities import create_sun_direction_indicator` import (line 21)
remains -- it's still used by the sphere shell functions (upper_atmosphere and
hill_sphere) which become unreachable after migration but stay in place.
Phase D removes the import.

### 4.4 Saturn cloud layer info marker style update (line ~458-469)

Saturn's cloud layer has a distinct info marker pattern: separate `name`
(`"Saturn: Cloud Layer (Info)"`) and `legendgroup` matching the same name,
NOT matching the geometry's `legendgroup` (`"Saturn: Cloud Layer"`).
This is the pre-existing "info marker visible when toggled off" bug from
C3 handoff item 20.

**Current source (lines 453-469):**

```python
    hover_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=6, color=layer_info['color'], opacity=0.9,
                    symbol='cross', line=dict(color='white', width=1)),
        name=trace_name,
        legendgroup=trace_name,
        text=[layer_info['description']],
        customdata=[f"Saturn: {layer_info['name']}"],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )
```

where `trace_name = f"Saturn: {layer_info['name']} (Info)"`.

After C4 migration, the cloud layer is handled by `build_sphere_shell()`, which
emits the info marker with legendgroup matching the geometry trace_name
(`"Saturn: Cloud Layer"`) -- bug fixed structurally. NO direct edit needed
to the source function (it becomes unreachable and stays in place).

**No action required for this subsection.** Documented for the verification
plan (Mode 5 item: confirm Saturn cloud layer info marker disappears when
toggled off).

### 4.5 Saturn upper atmosphere refactor (line ~480-597)

The upper atmosphere is a sphere shell, but it has an unusual pattern:
emit traces inline, then append a `create_sun_direction_indicator` call.
Both the geometry trace and info marker work fine in the new dispatch
(legendgroup matches), but the sun indicator gets stripped.

After C4: `create_saturn_upper_atmosphere_shell` becomes unreachable
from the dispatch (handled by `build_sphere_shell` via config). The function
stays in place. Per-shell sun indicator naturally goes away.

**No direct source edit required.** Documented for verification.

### 4.6 Saturn magnetosphere refactor (line ~599-671)

**Pattern matches Jupiter exactly** (C3 Section 5.1). Three changes:
(1) sunward rotation, (2) info marker update, (3) sun indicator removal.

#### 4.6.1 Apply sunward rotation to magnetosphere geometry

Saturn's magnetic dipole is essentially aligned with its rotation axis
(`magnetic_tilt_deg=0`, per Tony Q1: "Saturn passes 0"). The default
`rotate_to_sunward()` call without an explicit `magnetic_tilt_deg` uses 0.

**Current source (lines 620-629):**

```python
    # Create magnetosphere main shape
    x, y, z = create_magnetosphere_shape(params)
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # Apply center position offset
    x = np.array(x) + center_x
    y = np.array(y) + center_y
    z = np.array(z) + center_z
```

**Replace with:**

```python
    # Create magnetosphere main shape (generated with -X as sunward)
    x, y, z = create_magnetosphere_shape(params)
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # Rotate to actual sunward direction, then offset to center position.
    # Saturn's magnetic axis is essentially aligned with its rotation axis
    # (~0 deg tilt), so magnetic_tilt_deg=0 (default).
    x, y, z = np.array(x), np.array(y), np.array(z)
    x, y, z = rotate_to_sunward(x, y, z, center_position=center_position)
    x = x + center_x
    y = y + center_y
    z = z + center_z
```

#### 4.6.2 Replace magnetosphere info marker (lines ~651-662)

**Current source:**

```python
    traces.append(go.Scatter3d(
        x=[x[0]], y=[y[0]], z=[z[0]],
        mode='markers',
        marker=dict(size=6, color='rgb(200, 200, 255)', opacity=0.9,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        legendgroup='Saturn: Magnetosphere',
        text=[mag_desc],
        customdata=['Saturn: Magnetosphere'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    ))
```

**Replace with:**

```python
    traces.append(create_info_marker(
        x[0], y[0], z[0],
        'rgb(200, 200, 255)', mag_desc, 'Saturn: Magnetosphere'
    ))
```

#### 4.6.3 Remove per-shell sun indicator (lines ~664-669)

**Current source:**

```python
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius=500 * SATURN_RADIUS_AU
    )
    for trace in sun_traces:
        traces.append(trace)

    return traces
```

**Replace with:**

```python
    return traces
```

Trace count: 1 (geometry) + 1 (info marker) = **2 traces**. Same as Jupiter.

### 4.7 Saturn Enceladus plasma torus refactor (line ~676-787)

Tony Q7: NOT rotated. Equatorial structure. The current source applies Saturn's
axial tilt (-26.73 deg) via `rotate_points` INSIDE the builder (lines 686-687,
722-725) -- this is the AXIAL TILT (rotation axis vs ecliptic), which Tony
explicitly flagged in the reply: "axial tilt vs magnetic tilt -- Saturn/Uranus
radiation belt builders apply axial tilt (obliquity) internally to place belts
in the planet's actual equatorial plane. This is physically correct and must
be PRESERVED."

**Preserve all internal `rotate_points` calls and the axial tilt math.**
Only update the info marker style and strip the sun indicator.

#### 4.7.1 Replace Enceladus torus info marker (lines ~767-778)

**Current source:**

```python
    traces.append(go.Scatter3d(
        x=[enceladus_torus_x_final[0]], y=[enceladus_torus_y_final[0]],
        z=[enceladus_torus_z_final[0]],
        mode='markers',
        marker=dict(size=6, color='rgb(200, 220, 255)', opacity=0.9,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        legendgroup='Saturn: Enceladus Plasma Torus',
        text=enceladus_text,
        customdata=['Saturn: Enceladus Plasma Torus'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    ))
```

**Replace with:**

```python
    traces.append(create_info_marker(
        enceladus_torus_x_final[0], enceladus_torus_y_final[0],
        enceladus_torus_z_final[0],
        'rgb(200, 220, 255)', enceladus_text[0], 'Saturn: Enceladus Plasma Torus'
    ))
```

Note: `enceladus_text` in the source is a one-element LIST (`["Enceladus
plasma torus: ..."]`, line 735-747). Pass `enceladus_text[0]` (the bare string)
to `create_info_marker`, matching the unified contract that all other info
markers use.

#### 4.7.2 Remove per-shell sun indicator (lines ~780-785)

Same pattern as 4.6.3. Replace the 6-line sun_indicator block with `return traces`.

Trace count: 1 (geometry) + 1 (info marker) = **2 traces**.

### 4.8 Saturn radiation belts refactor (line ~794-929)

#### 4.8.0 Pre-flight audit: double-offset check

Before any edits to the Saturn radiation belt builder, audit the
source for the same pre-existing double-offset pattern documented in
Uranus belts (Section 5.7). Read `saturn_visualization_shells.py`
lines 794-929 and look for:

```python
# Pattern A: belt arrays offset by center BEFORE axial tilt
belt_x = np.array(belt_x) + center_x   # <- first offset
belt_y = np.array(belt_y) + center_y
belt_z = np.array(belt_z) + center_z

# ... tilt applied to already-offset arrays ...
belt_x_tilted, ... = rotate_points(belt_x, belt_y, belt_z, ..., 'x')

# Pattern B: SECOND offset applied AFTER tilt
belt_x_final = belt_x_tilted + center_x   # <- second offset (doubles)
```

If both Pattern A and Pattern B are present in Saturn source, it is
the same bug. Decision in that case: fix it now during C4 (strip
Pattern A; keep Pattern B; matches Uranus 5.7 cleanup), since the
behavior change is the same character as Uranus and avoids leaving
the same bug unfixed in a sibling module.

If Pattern A is absent or Pattern B is different, the Saturn source
is correct as written. Preserve unchanged.

Document the audit outcome in the C4 handoff document. This is a ~5
minute read; the cheap audit prevents a separate cleanup pass in
Phase D.

#### 4.8.1 Belt definitions

Saturn emits **6 radiation belts** (Tony Q6 confirmed: 12 traces = 6 components
x 2). Belt names from source (line 798-799):

1. `Belt from A-Ring to Mimas`
2. `Belt from Mimas to Enceladus`
3. `Belt from Enceladus to Tethys`
4. `Belt from Tethys to Dione`
5. `Belt from Dione to Rhea`
6. `Belt outward of Rhea`

The info marker replacement appears once but executes six times (inside the
`for i, belt_distance in enumerate(belt_distances)` loop).

**Axial tilt preserved** (line 839, 884-886). This is the -26.73 deg obliquity.

#### 4.8.1 Replace per-belt info marker (lines ~909-920, inside the loop)

**Current source:**

```python
        traces.append(go.Scatter3d(
            x=[belt_x_final[0]], y=[belt_y_final[0]], z=[belt_z_final[0]],
            mode='markers',
            marker=dict(size=6, color=belt_colors[i], opacity=0.9,
                        symbol='cross', line=dict(color='white', width=1)),
            name='',
            legendgroup=belt_names[i],
            text=[belt_texts[i]],
            customdata=[belt_names[i]],
            hovertemplate='%{text}<extra></extra>',
            showlegend=False
        ))
```

**Replace with:**

```python
        traces.append(create_info_marker(
            belt_x_final[0], belt_y_final[0], belt_z_final[0],
            belt_colors[i], belt_texts[i], belt_names[i]
        ))
```

`belt_texts[i]` is a plain string per source line 800-826 (each belt_texts
entry is built via string concatenation). Pass directly.

#### 4.8.2 Remove per-shell sun indicator (lines ~922-927)

Same pattern. Replace with `return traces`.

Trace count: 6 belts * (1 geom + 1 info) = **12 traces**.

#### 4.8.3 Note on pre-existing radiation belt offset pattern

Saturn radiation belts at lines 872-890 have an interesting pattern: offset
applied at lines 873-875, then no-op recast at 880-882, then rotate around
X axis at 885 (which rotates the offset coordinates), then offset applied
AGAIN at 888-890. The behavior in body-centered view (center_position=0,0,0)
is correct because the offset is zero. In heliocentric view, this double-offsets
the belts. This is a pre-existing bug, NOT flagged for fix in Tony's C4
reply. Phase C4 preserves the existing behavior exactly.

Flagged in Section 8 Decision Log for Phase D / Mode 5 review.

### 4.9 Saturn hill sphere (line ~943-1019)

Same pattern as upper_atmosphere -- sphere shell with per-shell sun indicator.
After migration, `create_saturn_hill_sphere_shell` becomes unreachable; sun
indicator naturally stripped. **No direct source edit required.**

### 4.10 Saturn ring system refactor (line ~1038-1239)

Tony Q5: Adams ring arcs do NOT apply (those are Neptune). Saturn has 7 ring
components (D, C, B, A, F, G, E), each with its own info marker. Tony Q7:
NOT rotated -- but the source DOES apply Saturn's axial tilt (-26.73 deg)
to rings via `rotate_points(..., saturn_tilt, 'x')` (lines 1166, 1185, 1218).
This is the **axial tilt** (Tony's clarification: PRESERVE).

**Preserve** all axial tilt math. Update info marker style. Strip sun indicator.

#### 4.10.1 Replace per-ring info marker (lines ~1219-1230, inside the loop)

**Current source:**

```python
        mx_t, my_t, mz_t = rotate_points([outer_radius_au], [0.0], [0.0], saturn_tilt, 'x')
        traces.append(go.Scatter3d(
            x=[mx_t[0] + center_x], y=[my_t[0] + center_y], z=[mz_t[0] + center_z],
            mode='markers',
            marker=dict(size=6, color=ring_info['color'], opacity=0.9,
                        symbol='cross', line=dict(color='white', width=1)),
            name='',
            legendgroup=f"Saturn: {ring_info['name']}",
            text=[ring_info['description']],
            customdata=[f"Saturn: {ring_info['name']}"],
            hovertemplate='%{text}<extra></extra>',
            showlegend=False
        ))
```

**Replace with:**

```python
        mx_t, my_t, mz_t = rotate_points([outer_radius_au], [0.0], [0.0], saturn_tilt, 'x')
        traces.append(create_info_marker(
            mx_t[0] + center_x, my_t[0] + center_y, mz_t[0] + center_z,
            ring_info['color'], ring_info['description'],
            f"Saturn: {ring_info['name']}"
        ))
```

The `rotate_points` line for marker positioning is preserved -- it places the
info marker on the tilted ring at the outer radius. Same approach as Uranus
and Neptune rings.

#### 4.10.2 Remove per-shell sun indicator (lines ~1232-1237)

Same pattern. Replace with `return traces`.

Trace count: 7 rings * (1 geom + 1 info) = **14 traces**.

### 4.11 Saturn CUSTOM_SHELLS entry

In `shell_configs.py`, after the Jupiter block in `CUSTOM_SHELLS`, add:

```python

    # ============================================================
    # Saturn
    # ============================================================
    # Source: NASA Saturn Fact Sheet; NASA Cassini Mission;
    #         NASA Saturn Magnetosphere Overview; Cassini Mission: Enceladus;
    #         NASA Voyager 2 Saturn Encounter; Mankovich & Fuller (2021).
    # Verified: April 2026 provenance audit via Gemini fact-check.
    'Saturn': {

        'magnetosphere': {
            'builder': 'saturn_visualization_shells.create_saturn_magnetosphere',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.2 AU TO VISUALIZE.\n"
                "1.4 MB PER FRAME FOR HTML.\n\n"
                "Saturn has a large magnetosphere, the region of space dominated by its\n"
                "magnetic field. Saturn's magnetic field is unique because its magnetic\n"
                "axis is almost perfectly aligned with its rotational axis (~0 deg tilt).\n"
                "The magnetosphere deflects the solar wind and traps charged particles,\n"
                "creating auroras at the poles. Material from Enceladus's plumes\n"
                "contributes plasma to Saturn's magnetosphere and its E ring.\n\n"
                "Note: This visualization shows only the magnetosphere envelope. The bow\n"
                "shock (at ~22-27 R_S standoff) is not yet rendered; it can be added\n"
                "editorially in a future enhancement to match the Mercury/Venus/Mars/Earth\n"
                "pattern."
            ),
        },

        'enceladus_plasma_torus': {
            'builder': 'saturn_visualization_shells.create_saturn_enceladus_plasma_torus',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.005 AU TO VISUALIZE.\n"
                "634 KB PER FRAME FOR HTML.\n\n"
                "Donut-shaped region of charged particles primarily sourced from Saturn's\n"
                "moon Enceladus. Water vapor and icy particles vented from south-polar\n"
                "geysers (hundreds of kg/s) are ionized by UV radiation and electron\n"
                "bombardment, forming a torus centered on Enceladus's orbit (~3.95 R_S).\n"
                "The Enceladus plasma torus is a significant plasma source for Saturn's\n"
                "inner magnetosphere and feeds Saturn's diffuse E ring."
            ),
        },

        'radiation_belts': {
            'builder': 'saturn_visualization_shells.create_saturn_radiation_belts',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.01 AU TO VISUALIZE.\n\n"
                "Saturn has multiple distinct radiation belts trapped within its\n"
                "magnetosphere. Unlike Earth's relatively simple Van Allen belt structure,\n"
                "Saturn's belts are heavily shaped by its rings and moons, which absorb\n"
                "charged particles and create characteristic gaps.\n\n"
                "The visualization shows six belt regions defined by adjacent moon orbits:\n"
                "Belt from A-Ring to Mimas, Belt from Mimas to Enceladus, Belt from\n"
                "Enceladus to Tethys, Belt from Tethys to Dione, Belt from Dione to Rhea,\n"
                "and Belt outward of Rhea. The primary source of high-energy particles is\n"
                "the collision of galactic cosmic rays with Saturn's atmosphere.\n\n"
                "The same builder produces all six belt traces as separate legend entries."
            ),
        },

        'ring_system': {
            'builder': 'saturn_visualization_shells.create_saturn_ring_system',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.005 AU TO VISUALIZE.\n"
                "22.2 MB PER FRAME FOR HTML.\n\n"
                "Saturn's spectacular ring system is composed primarily of water ice\n"
                "particles with some rocky debris and dust. The rings extend hundreds of\n"
                "thousands of kilometers from the planet but are typically only about\n"
                "10 meters thick.\n\n"
                "The visualization shows seven ring components from inner to outer:\n"
                "  * D Ring (66,900-74,500 km): innermost and faintest of the main rings\n"
                "  * C Ring (74,658-92,000 km): wider but fainter than A and B\n"
                "  * B Ring (92,000-117,500 km): brightest and most massive\n"
                "  * A Ring (122,340-136,800 km): outermost bright ring; Encke and Keeler\n"
                "    gaps shepherded by Pan and Daphnis\n"
                "  * F Ring (140,210-140,420 km): narrow, dynamic, shepherded by Pandora\n"
                "    and Prometheus\n"
                "  * G Ring (166,000-175,000 km): faint and dusty\n"
                "  * E Ring (180,000-480,000 km): broad, diffuse, sourced by icy particles\n"
                "    from Enceladus\n\n"
                "The rings lie in Saturn's equatorial plane (-26.73 deg axial tilt applied\n"
                "in the builder). The Cassini Division (4,800 km gap between A and B) is\n"
                "the most prominent gap.\n\n"
                "The same builder produces all seven ring traces as separate legend entries."
            ),
        },

    },
```

Note that the tooltip is **freshly written** -- the standalone
`saturn_ring_system_info` string in the source (lines 1021-1036) contains
Jupiter content (Metis, Adrastea, Amalthea Gossamer Ring, Thebe Gossamer Ring)
from a pre-existing copy-paste error. Per Tony's reply: "Fix during extraction.
Use the per-ring `description` fields from the function body, which have correct
Saturn-specific text." The fresh tooltip above is built from the per-ring
descriptions in `create_saturn_ring_system()` ring_params (lines 1052-1160).

### 4.12 Saturn dispatch delegation

In `planet_visualization.py`, find the Saturn dispatch block (lines 744-764).

**Replace the entire 21-line if-block with:**

```python
    if planet_name == 'Saturn':
        # Step 3 Phase C4: delegate to unified config-driven dispatch.
        # Custom geometry: saturn_magnetosphere, saturn_enceladus_plasma_torus,
        # saturn_radiation_belts (6 belts), saturn_ring_system (7 rings)
        # via CUSTOM_SHELLS lazy import.
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Saturn',
            center_object='Saturn',
        )
```

The 10 shell_vars GUI checkboxes (saturn_core, saturn_metallic_hydrogen,
saturn_molecular_hydrogen, saturn_cloud_layer, saturn_upper_atmosphere,
saturn_ring_system, saturn_radiation_belts, saturn_enceladus_plasma_torus,
saturn_magnetosphere, saturn_hill_sphere) continue to work -- the unified
dispatch reads them and routes to the appropriate sphere or custom builder.

### 4.13 Bottom-up edit order within `saturn_visualization_shells.py`

Apply edits in order from highest line number to lowest to prevent drift:

1. Section 4.10.2 (ring sun indicator removal, ~line 1232)
2. Section 4.10.1 (ring info marker, ~line 1219)
3. Section 4.8.2 (belt sun indicator removal, ~line 922)
4. Section 4.8.1 (belt info marker, ~line 909)
5. Section 4.7.2 (torus sun indicator removal, ~line 780)
6. Section 4.7.1 (torus info marker, ~line 767)
7. Section 4.6.3 (magnetosphere sun indicator removal, ~line 664)
8. Section 4.6.2 (magnetosphere info marker, ~line 651)
9. Section 4.6.1 (magnetosphere sunward rotation, ~line 620)
10. Section 4.3 (imports at top of file)

Note that `str_replace` is content-matching (location-independent), so order
is discipline not correctness.

### 4.14 Saturn verification

After Sections 4.3-4.13 are complete:

```bash
python3 -m py_compile shell_configs.py planet_visualization.py saturn_visualization_shells.py

python3 -c "
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS
assert 'Saturn' in SHELL_CONFIGS
assert 'Saturn' in CUSTOM_SHELLS
assert len(SHELL_CONFIGS['Saturn']) == 6
assert len(CUSTOM_SHELLS['Saturn']) == 4
expected_custom = {'magnetosphere', 'enceladus_plasma_torus', 'radiation_belts', 'ring_system'}
assert set(CUSTOM_SHELLS['Saturn'].keys()) == expected_custom

# Sphere builder smoke
from orrery_rendering import build_sphere_shell
for shell_name, cfg in SHELL_CONFIGS['Saturn'].items():
    traces = build_sphere_shell(cfg, 'Saturn', (0, 0, 0))
    assert len(traces) == 2, 'Saturn/%s: expected 2 traces, got %d' % (shell_name, len(traces))
print('Saturn sphere builder smoke: PASS')

# Custom geometry smoke and trace counts
import importlib
mod = importlib.import_module('saturn_visualization_shells')

trace_counts = {
    'create_saturn_magnetosphere': 2,           # 1 geom + 1 marker (no bow shock)
    'create_saturn_enceladus_plasma_torus': 2,  # 1 geom + 1 marker
    'create_saturn_radiation_belts': 12,        # 6 belts * (1 geom + 1 marker)
    'create_saturn_ring_system': 14,            # 7 rings * (1 geom + 1 marker)
}

for fname, expected in trace_counts.items():
    traces = getattr(mod, fname)((0, 0, 0))
    actual = len(traces)
    assert actual == expected, '%s: expected %d, got %d' % (fname, expected, actual)
    print('  %s: %d traces' % (fname, actual))

# Rotation isolation
import numpy as np

# Magnetosphere rotates (180-deg test: body at -X = anti-sunward)
mag_origin = mod.create_saturn_magnetosphere((0, 0, 0))
mag_off = mod.create_saturn_magnetosphere((-1.0, 0.0, 0.0))
origin_x = np.array(mag_origin[0].x)
off_x = np.array(mag_off[0].x) - (-1.0)
assert np.allclose(off_x, -origin_x, atol=1e-9), 'Saturn magnetosphere rotation failed'
print('Saturn magnetosphere rotation: PASS (180 deg test)')

# Enceladus torus NOT rotated (axial tilt internal)
torus_origin = mod.create_saturn_enceladus_plasma_torus((0, 0, 0))
torus_off = mod.create_saturn_enceladus_plasma_torus((-1.0, 0.0, 0.0))
# X range comparison (torus is random-jittered, so direct comparison wouldn't work)
o_xr = np.array(torus_origin[0].x).max() - np.array(torus_origin[0].x).min()
f_xr = (np.array(torus_off[0].x) - (-1.0)).max() - (np.array(torus_off[0].x) - (-1.0)).min()
assert abs(o_xr - f_xr) < 0.001, 'Saturn Enceladus torus unexpectedly rotated by sunward rotation'
print('Saturn Enceladus torus: PASS (unrotated)')

# Belts NOT rotated by sunward rotation (axial tilt is internal)
# Note: cannot do direct comparison due to the pre-existing offset pattern;
# instead verify the X RANGE of the first belt geometry trace is unchanged.
belts_origin = mod.create_saturn_radiation_belts((0, 0, 0))
belts_off = mod.create_saturn_radiation_belts((-1.0, 0.0, 0.0))
b_o_xr = np.array(belts_origin[0].x).max() - np.array(belts_origin[0].x).min()
b_f_xr = (np.array(belts_off[0].x) - (-1.0)).max() - (np.array(belts_off[0].x) - (-1.0)).min()
# Note: due to pre-existing double-offset bug, exact comparison may not match.
# This X-range test is the loosest valid check.
print('Saturn radiation belts X-range origin: %.4f, off: %.4f (similar if not rotated by sunward)' % (b_o_xr, b_f_xr))

# Rings NOT rotated
rings_origin = mod.create_saturn_ring_system((0, 0, 0))
rings_off = mod.create_saturn_ring_system((-1.0, 0.0, 0.0))
r_o_x = np.array(rings_origin[0].x)
r_f_x = np.array(rings_off[0].x) - (-1.0)
# Random thickness so allow tolerance
assert abs(r_o_x.max() - r_f_x.max()) < 1e-6, 'Saturn rings unexpectedly rotated'
print('Saturn rings: PASS (unrotated)')

# Dispatch delegation in place
import inspect, planet_visualization
src = inspect.getsource(planet_visualization.create_planet_visualization)
assert 'create_saturn_core_shell(center_position)' not in src, 'Old Saturn dispatch survived'
print('Saturn dispatch: PASS (old block removed)')

print()
print('Section 4 (Saturn) verification PASS')
"
```

All assertions must pass. If any fail, STOP and debug before proceeding to
Section 5 (Uranus).

---

## 5. Uranus Migration (Session 2, Part A)

Uranus migration follows the same template as Saturn (Section 4). Three
notable differences:

1. **`magnetic_tilt_deg=60`** wired in CUSTOM_SHELLS magnetosphere entry
   (first real use of the parameter; relies on Section 3 implementation).
2. **Missing info marker** added to `create_uranus_magnetosphere`
   (pre-existing omission; matches Mars C1 item 14 fix).
3. **Dead code cleanup** in radiation belts: silent first offset
   assignment, no-op variable recast, dead Y-axis tilt assignment, and
   commented-out blocks. This is the only `# Source:` finding for C4 that
   changes behavior in the heliocentric view (the dead Y-tilt was being
   silently overwritten by a subsequent assignment, so removing it has
   no effect; the silent first offset, however, was a real source of the
   pre-existing double-offset pattern that gets fixed when migration
   reaches the unified center_position application path). Flagged for
   Mode 5 visual diff -- belts should sit at the same axial position as
   before, but the implementation path is cleaner.

### 5.1 Uranus sphere configs

Five sphere shells. Source: `uranus_visualization_shells.py`.

| Shell | n_points | marker_size | opacity | radius_fraction | geometry |
|-------|---------:|------------:|--------:|----------------:|----------|
| core | 25 | 4.0 | 1.0 | 0.2 | scatter3d |
| mantle | 25 | 3.5 | 0.9 | 0.7 | scatter3d |
| cloud_layer | 24 | -- | 0.9 | 1.0 | mesh3d |
| upper_atmosphere | 20 | 3.0 | 0.5 | 1.16 | scatter3d |
| hill_sphere | 20 | 2.0 | 0.3 | 2770.0 | scatter3d |

Hill sphere radius_fraction: 70.8e6 km / URANUS_RADIUS_KM
= 70,800,000 / 25,559 = 2769.7 (rounded to 2770.0). Verify against
source line ~1112 in `create_uranus_hill_sphere_shell`.

### 5.2 Auto-generation script for Uranus sphere configs

Reuse the script from Section 4.2 with these parameter changes:

```python
BODY = 'Uranus'
PATH = 'uranus_visualization_shells.py'

SHELLS = [
    ('core',             'create_uranus_core_shell',             'uranus_core_info'),
    ('mantle',           'create_uranus_mantle_shell',           'uranus_mantle_info'),
    ('cloud_layer',      'create_uranus_cloud_layer_shell',      'uranus_cloud_layer_info'),
    ('upper_atmosphere', 'create_uranus_upper_atmosphere_shell', 'uranus_upper_atmosphere_info'),
    ('hill_sphere',      'create_uranus_hill_sphere_shell',      'uranus_hill_sphere_info'),
]

MARKER_SIZES = {
    'core': 4.0, 'mantle': 3.5,
    'upper_atmosphere': 3.0, 'hill_sphere': 2.0,
}
```

`MESH3D_SHELLS` and `MESH3D_RESOLUTION` unchanged. Run, inspect, paste
into `shell_configs.py`. If the script output disagrees with the
Section 5.1 table, the script wins -- read the source manually to
reconcile.

### 5.3 Uranus imports (top of `uranus_visualization_shells.py`)

Current state (line 18-21):

```python
from planet_visualization_utilities import (URANUS_RADIUS_AU, KM_PER_AU, create_sphere_points, create_magnetosphere_shape,
                                            rotate_points)
from orrery_rendering import create_ring_points
from shared_utilities import create_sun_direction_indicator
```

After C4:

```python
from planet_visualization_utilities import (URANUS_RADIUS_AU, KM_PER_AU, create_sphere_points, create_magnetosphere_shape,
                                            rotate_points)
from orrery_rendering import create_ring_points, rotate_to_sunward, create_info_marker
from shared_utilities import create_sun_direction_indicator
```

The `create_sun_direction_indicator` import remains (still used by
sphere shells that have sun indicators in source, until those `sun_traces`
loops are stripped). After all sun_traces stripping (Section 5.5, 5.7,
5.8, 5.9), this import becomes unused -- defer cleanup to Phase D.

### 5.4 Uranus cloud layer (line ~182-345)

**No direct source edit required.** The Uranus cloud layer function
`create_uranus_cloud_layer_shell` becomes unreachable after C4 dispatch
delegation (Section 5.11). The new emission path is
`build_sphere_shell()` in `orrery_rendering.py`, driven by the
`cloud_layer` entry in `SHELL_CONFIGS['Uranus']` (Section 5.1). The
helper enforces the single-info-marker pattern and uses the canonical
`create_info_marker()` placement (north pole at radius * 1.05).

Verification: after dispatch delegation, call
`build_sphere_shell(SHELL_CONFIGS['Uranus']['cloud_layer'], 'Uranus',
(0, 0, 0))` and confirm it returns 2 traces (mesh3d + info marker).

The source function `create_uranus_cloud_layer_shell` stays in place but
unused. Phase D decides whether to archive it.

### 5.5 Uranus upper atmosphere -- sun_traces removal (line ~358-440)

Standalone sphere builder with embedded sun indicator. Same pattern as
Saturn 4.5. The sphere shell itself moves to SHELL_CONFIGS; the
sun_traces loop at the end of the function is stripped.

Verify the function ends with:

```python
    sun_traces = create_sun_direction_indicator(
        center_position=center_position,
        shell_radius=...
    )
    for trace in sun_traces:
        traces.append(trace)

    return traces
```

Strip the `sun_traces = ...` block and the `for trace in sun_traces:`
loop. Keep `return traces`. The shell+info_trace pair remains; just the
sun indicator block is removed.

Net effect: sphere shell function still exists in source (preserved
verbatim minus sun indicator) but is unused after dispatch delegation.
Phase D decides per-function fate.

### 5.6 Uranus magnetosphere refactor (line ~456-510)

This is the trickiest Uranus refactor. THREE changes:

1. **Add center_position offset BEFORE rotate_to_sunward.** Currently
   the function applies center offset directly to the geometry; the new
   pattern is rotate first (geometry in default frame), then offset.

2. **Add missing info marker.** Source emits only the geometry trace
   (line 488-501). Add an info marker after the geometry trace using
   `create_info_marker()`.

3. **Pass `magnetic_tilt_deg=60`.** First real use of the parameter.

Current source (lines 456-510):

```python
def create_uranus_magnetosphere(center_position=(0, 0, 0)):
    """Creates Uranus's main magnetosphere structure."""
    params = {
        'sunward_distance': 21,
        'equatorial_radius': 27.5,
        'polar_radius': 17.5,
        'tail_length': 300,
        'tail_base_radius': 15,
        'tail_end_radius': 75,
    }

    for key in params:
        params[key] *= URANUS_RADIUS_AU

    x, y, z = create_magnetosphere_shape(params)

    center_x, center_y, center_z = center_position

    x = np.array(x) + center_x
    y = np.array(y) + center_y
    z = np.array(z) + center_z

    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=2.0,
                color='rgb(200, 200, 255)',
                opacity=0.3
            ),
            name='Uranus: Magnetosphere',
            hoverinfo='skip',
            showlegend=True
        )
    ]

    sun_traces = create_sun_direction_indicator(
        center_position=center_position,
        shell_radius=300 * URANUS_RADIUS_AU
    )
    for trace in sun_traces:
        traces.append(trace)

    return traces
```

After C4:

```python
def create_uranus_magnetosphere(center_position=(0, 0, 0), sun_position=(0, 0, 0)):
    """Creates Uranus's main magnetosphere structure.

    Phase C4: rotated to face the actual Sun direction via
    rotate_to_sunward(). magnetic_tilt_deg=60 applies an additional
    rotation about the X axis (bow-shock-to-tail) to model Uranus's
    60-degree dipole-vs-rotation-axis offset.

    Note: source had no info marker (pre-existing omission, same
    pattern as Mars C1 item 14). C4 adds one via create_info_marker(),
    positioned at the first point of the rendered geometry (matching
    the radiation-belts and ring-system pattern in this module).

    Module updated: May 2026 with Anthropic's Claude Opus 4.7
    """
    params = {
        'sunward_distance': 21,
        'equatorial_radius': 27.5,
        'polar_radius': 17.5,
        'tail_length': 300,
        'tail_base_radius': 15,
        'tail_end_radius': 75,
    }

    for key in params:
        params[key] *= URANUS_RADIUS_AU

    x, y, z = create_magnetosphere_shape(params)

    x = np.array(x)
    y = np.array(y)
    z = np.array(z)

    # Phase C4: rotate to face actual Sun direction, with magnetic tilt
    # (X-axis rotation about the bow-shock-to-tail axis; see Section 3.1
    # for physics rationale)
    x, y, z = rotate_to_sunward(
        x, y, z,
        center_position=center_position,
        sun_position=sun_position,
        magnetic_tilt_deg=60,
    )

    # Apply center offset to rotated geometry
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z

    trace_name = 'Uranus: Magnetosphere'

    description = (
        "Uranus's Magnetosphere: tilted 60 degrees from the rotation axis -- "
        "itself tilted 97.77 degrees from the orbital plane. This produces a "
        "magnetosphere geometry with no analog in the rest of the solar system: "
        "the dipole axis sweeps a wide cone as Uranus rotates, modulating the "
        "magnetosphere's solar-wind interaction on a ~17-hour cycle.<br><br>"
        "Source: Ness et al. (1986) Science -- Voyager 2 magnetometer."
    )

    geom_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=2.0,
            color='rgb(200, 200, 255)',
            opacity=0.3
        ),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True,
    )

    # Phase C4: add info marker at first point of rendered geometry
    # (pre-existing omission in source). Matches the source's
    # radiation-belt and ring-system info marker pattern.
    info_trace = create_info_marker(
        x[0], y[0], z[0],
        'rgb(200, 200, 255)', description, trace_name
    )

    return [geom_trace, info_trace]
```

Two trace return after migration: geometry + info marker. Source
returned 1 + sun indicators. Net change: 1 -> 2 (info marker added,
sun indicators dropped).

**On `create_info_marker()` signature.** The helper signature
(`orrery_rendering.py` line 27) is:

```python
def create_info_marker(x, y, z, color, text, legendgroup, customdata=None)
```

It places the marker at exactly `(x, y, z)` -- no internal offset. The
"north pole at radius * 1.05" offset lives inside `build_sphere_shell()`,
not the marker helper. For custom (non-sphere) geometry like
magnetospheres, the caller is responsible for picking the marker
position; the convention used here matches the source's existing
radiation-belt and ring-system patterns: first point of the rendered
geometry array.

**Note on `legendgroup`:** Source omits `legendgroup='Uranus: Magnetosphere'`
on the geometry trace (line 488-500 lacks it). The refactor adds it
explicitly so the info marker's `legendgroup='Uranus: Magnetosphere'`
(set inside `create_info_marker()`) properly groups with the geometry.
This is a side-effect bug fix: previously toggling the magnetosphere
off would leave the (non-existent) marker behind in the legend; now
toggling off hides both.

### 5.7 Uranus radiation belts refactor (line ~518-702)

Belt builder with two component belts (Inner, Outer). Applies axial
tilt (`uranus_tilt = np.radians(105)`, empirical value vs nominal
97.77 deg, line 595). Source has cleanup work needed.

#### 5.7.1 Dead code to strip (per Tony's decision Q1.b)

Lines to strip in source (bottom-up):

1. **Line 660-663** (the SECOND post-tilt offset block):
   ```python
           # Apply center position offset
           belt_x_final = belt_x_tilted + center_x
           belt_y_final = belt_y_tilted + center_y
           belt_z_final = belt_z_tilted + center_z
   ```
   **KEEP** this block -- this is the offset that actually takes
   effect for the geometry trace (lines 666-680 use `belt_*_final`
   from this block, NOT from line 648's `rotate_points(..., 'y')`
   output -- the line 648 assignment is overwritten by line 661 which
   uses `belt_x_tilted`, not `belt_x_final` from line 648).

2. **Lines 644-658** (commented-out dead code block):
   ```python
               # First apply rotation around x-axis
       #    x_tilted, y_tilted, z_tilted = rotate_points(x, y, z, np.radians(uranus_tilt), 'x')

               # Then apply rotation around y-axis with the same angle
           belt_x_final, belt_y_final, belt_z_final = rotate_points(belt_x_tilted, belt_y_tilted, belt_z_tilted, uranus_tilt, 'y')

           # Apply center position offset
       #    x = np.array(x) + center_x
       #    y = np.array(y) + center_y
       #    z = np.array(z) + center_z

           # Apply center position offset
       #    x_final = np.array(x_tilted) + center_x
       #    y_final = np.array(y_tilted) + center_y
       #    z_final = np.array(z_tilted) + center_z
   ```
   The `rotate_points(..., 'y')` assignment at line 648 is silently
   overwritten by line 661 (`belt_x_final = belt_x_tilted + center_x`
   uses `belt_x_tilted`, not `belt_x_final` from line 648). So the
   Y-axis rotation has no effect on the rendered belts. **STRIP**
   the entire commented-out block (lines 644-658) AND the live
   `belt_x_final, ... = rotate_points(..., 'y')` line at 648.

3. **Lines 635-638** (silent first offset block):
   ```python
           # Apply center position offset
           belt_x = np.array(belt_x)
           belt_y = np.array(belt_y)
           belt_z = np.array(belt_z)
   ```
   This is a no-op variable recast (the arrays were already numpy
   arrays from the prior `belt_x = np.array(belt_x) + center_x`
   block at line 629-631). **STRIP** these four lines including the
   comment.

4. **Lines 628-631** (the FIRST offset block):
   ```python
           # Apply center position offset
           belt_x = np.array(belt_x) + center_x
           belt_y = np.array(belt_y) + center_y
           belt_z = np.array(belt_z) + center_z
   ```
   This applies center offset to the PRE-tilt geometry. The tilt is
   applied at line 641 using `belt_x` (already offset), so the offset
   is rotated along with the geometry. Then line 661's
   `belt_x_final = belt_x_tilted + center_x` adds center offset
   AGAIN to the rotated geometry. This is the pre-existing
   double-offset bug.

   **STRIP** the first offset block (lines 628-631). The correct
   offset is the post-tilt block (lines 660-663), which is preserved.

#### 5.7.2 What remains after cleanup

The radiation belts now follow the correct pattern:
1. Generate belt geometry in default frame (untranslated).
2. Apply axial tilt (X-axis rotation) -- physically correct for
   placing belts in Uranus's equatorial plane.
3. Apply center offset to the tilted geometry.
4. Emit geometry trace + info marker.

The axial tilt is PRESERVED (Tony's clarification Q7) -- it is NOT
the same rotation as `magnetic_tilt_deg`. Radiation belts are
axis-anchored (rotate with the planet's actual equatorial plane);
they do NOT rotate to face the Sun.

#### 5.7.3 Info marker pattern

Inside the for-loop (lines 665-693), source emits a geometry trace
plus a manual info marker. The info marker at lines 682-693 uses
`belt_x_final[0]` (the FIRST point of the tilted, offset belt) --
this is the final post-tilt-post-offset coordinates.

Replace the inline scatter3d info marker with a `create_info_marker()`
call. The helper takes a literal `(x, y, z)` position (no internal
radius offset -- that offset is internal to `build_sphere_shell()`,
not the marker helper). The signature in `orrery_rendering.py` line 27 is:

```python
def create_info_marker(x, y, z, color, text, legendgroup, customdata=None)
```

Final code for the per-belt info marker, matching Saturn 4.6.2:

```python
        traces.append(create_info_marker(
            belt_x_final[0], belt_y_final[0], belt_z_final[0],
            belt_colors[i], belt_texts[i], belt_names[i]
        ))
```

This places the cross marker exactly at the first point of the
tilted-and-offset belt geometry, matching the source's intent. The
helper centralizes marker style (size, symbol, outline) so future
style updates propagate from one place.

#### 5.7.4 Sun indicator removal

Strip the `sun_traces = create_sun_direction_indicator(...)` block at
lines 695-700.

#### 5.7.5 Trace count after C4

4 traces = 2 belts x 2 (geometry + info marker). Matches v6 prompt.

### 5.8 Uranus hill sphere (line ~1105-1178)

Standalone sphere builder. Move config to SHELL_CONFIGS. Source has
sun indicator embedded -- strip the sun_traces block. Same pattern as
Saturn 4.9.

### 5.9 Uranus ring system refactor (line ~738-1091)

11 rings -> 22 traces (11 geometry + 11 info markers). Source already
uses `create_ring_points()` (Phase C3 promotion). Source applies
compound rotation (X-axis then Y-axis, both at `uranus_tilt = 105 deg`)
to place rings in Uranus's near-vertical equatorial plane.

**Rings stay UNROTATED by `rotate_to_sunward()`** -- they are equatorial,
gravity-anchored. The compound X+Y rotation in source is the axial tilt
implementation (NOT the same as `magnetic_tilt_deg`); KEEP it. This is
the asymmetric tilt convention Uranus uses (105 deg empirical fit).

Net change to the function: strip the `sun_traces` block at lines
1084-1089. All other geometry preserved.

The per-ring info markers (lines 1069-1082 use compound-rotated
`mx_t2[0]+center_x` etc. as the position) should be rewritten using
the `create_info_marker()` helper for consistency. Position computation
unchanged; only the trace construction is replaced:

```python
        traces.append(create_info_marker(
            mx_t2[0] + center_x, my_t2[0] + center_y, mz_t2[0] + center_z,
            ring_info['color'], ring_info['description'],
            f"Uranus: {ring_info['name']}"
        ))
```

The position remains the compound-tilted outer-radius point projected
into the rendered frame; only the marker construction is centralized.

### 5.10 Uranus CUSTOM_SHELLS entry

Schema matches Jupiter (`shell_configs.py` line 1775) and Saturn
(Section 4.11): `'builder'` = single string path
`module.function_name`, `'tooltip'` = inline string.

```python
    'Uranus': {

        'magnetosphere': {
            'builder': 'uranus_visualization_shells.create_uranus_magnetosphere',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.5 AU TO VISUALIZE.\n"
                "560 KB PER FRAME FOR HTML.\n\n"
                "Uranus's magnetosphere has the most extreme geometry of any planet:\n"
                "the magnetic axis is tilted 60 degrees from the rotation axis, and\n"
                "Uranus itself is tilted 97.77 degrees from its orbital plane. The\n"
                "result is a magnetosphere with no analog in the solar system, with\n"
                "the dipole axis sweeping a wide cone as Uranus rotates and modulating\n"
                "the solar-wind interaction on a ~17-hour cycle.\n\n"
                "Source: Ness et al. (1986) Science -- Voyager 2 magnetometer."
            ),
        },

        'radiation_belts': {
            'builder': 'uranus_visualization_shells.create_uranus_radiation_belts',
            'tooltip': (
                "560 KB PER FRAME FOR HTML.\n\n"
                "Uranus has two main radiation belt regions (Inner and Outer) at\n"
                "approximately 3-10 R_U. Voyager 2 (1986) measurements showed\n"
                "Uranus's electron belts are surprisingly intense -- comparable to\n"
                "Earth's, and much stronger than Saturn's. The source is primarily\n"
                "the planet's upper atmosphere.\n\n"
                "Voyager 2 was the first and so far only spacecraft to directly\n"
                "observe them during its flyby in 1986.\n\n"
                "The same builder produces both traces (separate legend entries):\n"
                "Inner Radiation Belt, Outer Radiation Belt."
            ),
        },

        'ring_system': {
            'builder': 'uranus_visualization_shells.create_uranus_ring_system',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.001 AU TO VISUALIZE.\n\n"
                "Uranus has 13 known rings, discovered in 1977 via stellar\n"
                "occultation and confirmed by Voyager 2 in 1986. The rings are\n"
                "narrow, dark, and arranged in Uranus's near-vertical equatorial\n"
                "plane -- following the planet's 97.77-degree axial tilt rather\n"
                "than the orbital plane.\n\n"
                "Components rendered:\n"
                "  Rings 6, 5, 4 (innermost narrow rings)\n"
                "  Alpha, Beta, Eta, Gamma, Delta (mid rings)\n"
                "  Epsilon (outer narrow ring, brightest)\n"
                "  Nu, Mu (outer faint gossamer rings)\n\n"
                "Source: Elliot et al. (1977) Nature -- discovery via occultation;\n"
                "Voyager 2 (1986); de Pater et al. (2006) -- gossamer rings."
            ),
        },

    },
```

**No imports added to `shell_configs.py`.** Tooltip strings are inline,
matching the Jupiter pattern at lines 1775-1840.

### 5.11 Uranus dispatch delegation in `planet_visualization.py`

Replace the entire Uranus block at lines 766-782:

```python
    if planet_name == 'Uranus':
        # Step 3 Phase C4: delegate to unified config-driven dispatch.
        # Same pattern as Saturn (Phase C4, this session).
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Uranus',
            center_object='Uranus',
        )
```

### 5.12 Bottom-up edit order within `uranus_visualization_shells.py`

Edit lines in DECREASING line-number order to avoid line-number drift:

1. Strip `sun_traces` from `create_uranus_hill_sphere_shell` (~line 1105+).
2. Strip `sun_traces` from `create_uranus_ring_system` (line 1084-1089).
3. Replace ring info markers with `create_info_marker()` in
   `create_uranus_ring_system` (line 1069-1082 -- position unchanged,
   style centralized).
4. Strip `sun_traces` from `create_uranus_radiation_belts` (line 695-700).
5. Replace radiation belt info markers with `create_info_marker()` in
   `create_uranus_radiation_belts` (line 682-693).
6. Radiation belts dead code cleanup (line 660-663 KEEP, 644-658 STRIP,
   635-638 STRIP, 628-631 STRIP). Apply in reverse: 644-658 first
   (highest line range), then 635-638, then 628-631.
7. Strip `sun_traces` from `create_uranus_upper_atmosphere_shell`
   (in function body, late lines).
8. Refactor `create_uranus_magnetosphere` (lines 456-510) -- the
   ENTIRE function body is replaced per Section 5.6.
9. Cloud layer: no source edit (Section 5.4).
10. Update imports at top (line 18-21).

### 5.13 Uranus verification

```bash
python3 -c "
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS

# Sphere configs
expected_sphere = {'core', 'mantle', 'cloud_layer', 'upper_atmosphere', 'hill_sphere'}
assert set(SHELL_CONFIGS['Uranus'].keys()) == expected_sphere

# Custom configs
expected_custom = {'magnetosphere', 'radiation_belts', 'ring_system'}
assert set(CUSTOM_SHELLS['Uranus'].keys()) == expected_custom

# Sphere builder smoke
from orrery_rendering import build_sphere_shell
for shell_name, cfg in SHELL_CONFIGS['Uranus'].items():
    traces = build_sphere_shell(cfg, 'Uranus', (0, 0, 0))
    assert len(traces) == 2, 'Uranus/%s: expected 2 traces, got %d' % (shell_name, len(traces))
print('Uranus sphere builder smoke: PASS')

# Custom geometry trace counts
import importlib
mod = importlib.import_module('uranus_visualization_shells')

trace_counts = {
    'create_uranus_magnetosphere': 2,    # 1 geom + 1 marker (info marker NEW)
    'create_uranus_radiation_belts': 4,  # 2 belts * (1 geom + 1 marker)
    'create_uranus_ring_system': 22,     # 11 rings * (1 geom + 1 marker)
}

for fname, expected in trace_counts.items():
    traces = getattr(mod, fname)((0, 0, 0))
    actual = len(traces)
    assert actual == expected, '%s: expected %d, got %d' % (fname, expected, actual)
    print('  %s: %d traces' % (fname, actual))

# Magnetosphere rotation isolation (with magnetic_tilt_deg=60)
import numpy as np

mag_origin = mod.create_uranus_magnetosphere((0, 0, 0))
mag_off = mod.create_uranus_magnetosphere((-1.0, 0.0, 0.0))
origin_x = np.array(mag_origin[0].x)
off_x = np.array(mag_off[0].x) - (-1.0)
assert np.allclose(off_x, -origin_x, atol=1e-9), 'Uranus magnetosphere rotation failed'
print('Uranus magnetosphere rotation (180 deg + magnetic_tilt=60): PASS')

# Belts NOT rotated by sunward rotation (X-axis axial tilt is internal)
belts_origin = mod.create_uranus_radiation_belts((0, 0, 0))
belts_off = mod.create_uranus_radiation_belts((-1.0, 0.0, 0.0))
b_o_x = np.array(belts_origin[0].x)
b_f_x = np.array(belts_off[0].x) - (-1.0)
assert np.allclose(b_o_x, b_f_x, atol=1e-9), 'Uranus radiation belts unexpectedly rotated'
print('Uranus radiation belts: PASS (unrotated, after cleanup)')

# Rings NOT rotated
rings_origin = mod.create_uranus_ring_system((0, 0, 0))
rings_off = mod.create_uranus_ring_system((-1.0, 0.0, 0.0))
r_o_x = np.array(rings_origin[0].x)
r_f_x = np.array(rings_off[0].x) - (-1.0)
assert np.allclose(r_o_x.max(), r_f_x.max(), atol=1e-6), 'Uranus rings unexpectedly rotated'
print('Uranus rings: PASS (unrotated)')

# Dispatch delegation
import inspect, planet_visualization
src = inspect.getsource(planet_visualization.create_planet_visualization)
assert 'create_uranus_core_shell(center_position)' not in src, 'Old Uranus dispatch survived'
print('Uranus dispatch: PASS (old block removed)')

print()
print('Section 5 (Uranus) verification PASS')
"
```

If any assertion fails, STOP and debug. The radiation belt assertion
is particularly sensitive to the dead-code cleanup -- if the first
offset block is not stripped, the belts will be offset by 2 * center_x
(visible as 1.0 AU shift in the heliocentric test).


---

## 6. Neptune Migration (Session 2, Part B)

Neptune is the most complex C4 body. Key differences from Saturn/Uranus:

1. **Internal magnetic tilt handling preserved.** Neptune's
   `create_neptune_magnetosphere` applies its own 47-deg tilt (Y-axis)
   + 60-deg azimuth (Z-axis) + 0.55 R_N offset internally, with
   region-specific (bow shock / internal / tail) rotation. Per Tony's
   decision Q1/Q3: pass `magnetic_tilt_deg=0` to `rotate_to_sunward()`.
   Double-tilting would be a physics error.
2. **Magnetic poles preserved as 4 separate traces** (diamond mag center,
   axis dashed line, blue north pole, red south pole). These are
   inherently single-point or single-line traces -- NO conversion to
   single-info-marker pattern. KEEP as 4 traces with their own legend
   entries.
3. **Dead function `create_neptune_field_lines` stripped** (lines 770-860,
   plus the "THIS FUNCTION APPEARS OBSOLETE" comment at line 769).
4. **Pre-existing info marker position bugs in radiation belts and
   field-aligned currents** fixed during migration.

### 6.1 Neptune sphere configs

Five sphere shells. Source: `neptune_visualization_shells.py`.

| Shell | n_points | marker_size | opacity | radius_fraction | geometry |
|-------|---------:|------------:|--------:|----------------:|----------|
| core | 25 | 4.0 | 1.0 | 0.25 | scatter3d |
| mantle | 25 | 3.5 | 0.9 | 0.85 | scatter3d |
| cloud_layer | 24 | -- | 0.9 | 1.0 | mesh3d |
| upper_atmosphere | 20 | 3.0 | 0.5 | 1.01 | scatter3d |
| hill_sphere | 20 | 2.0 | 0.3 | 4685.0 | scatter3d |

Hill sphere radius_fraction: 116e6 km / NEPTUNE_RADIUS_KM
= 116,000,000 / 24,764 = 4684.6 (rounded to 4685.0). Verify against
source line ~1783 in `create_neptune_hill_sphere_shell`.

### 6.2 Auto-generation script for Neptune sphere configs

Reuse the script from Section 4.2 with these parameter changes:

```python
BODY = 'Neptune'
PATH = 'neptune_visualization_shells.py'

SHELLS = [
    ('core',             'create_neptune_core_shell',             'neptune_core_info'),
    ('mantle',           'create_neptune_mantle_shell',           'neptune_mantle_info'),
    ('cloud_layer',      'create_neptune_cloud_layer_shell',      'neptune_cloud_layer_info'),
    ('upper_atmosphere', 'create_neptune_upper_atmosphere_shell', 'neptune_upper_atmosphere_info'),
    ('hill_sphere',      'create_neptune_hill_sphere_shell',      'neptune_hill_sphere_info'),
]

MARKER_SIZES = {
    'core': 4.0, 'mantle': 3.5,
    'upper_atmosphere': 3.0, 'hill_sphere': 2.0,
}
```

`MESH3D_SHELLS` and `MESH3D_RESOLUTION` unchanged. Run, inspect, paste
into `shell_configs.py`. If the script output disagrees with the
Section 6.1 table, the script wins.

**Note on `*_info` symbol names.** Verify the info-string variable names
in the source file match what the auto-gen `SHELLS` tuples reference.
Neptune source uses module-level `*_info` strings adjacent to each
builder function definition (e.g., `neptune_core_info` near
`create_neptune_core_shell`). If any name differs, adjust the
`SHELLS` tuple before running.

### 6.3 Neptune imports (top of `neptune_visualization_shells.py`)

Source has internal `import` statements inside each function (a
non-standard pattern in this codebase). The migration adds top-level
imports without removing the function-local ones (function-local
imports are harmless redundancy; touching them is out of scope).

Add to the top of `neptune_visualization_shells.py`:

```python
from orrery_rendering import create_ring_points, rotate_to_sunward, create_info_marker
```

The `from orrery_rendering import create_ring_points` line was added in
Phase C3 -- update it to import the additional symbols.

### 6.4 Neptune cloud layer (line ~201-364)

**No direct source edit required.** The Neptune cloud layer function
`create_neptune_cloud_layer_shell` becomes unreachable after C4
dispatch delegation (Section 6.12). The new emission path is
`build_sphere_shell()` in `orrery_rendering.py`, driven by the
`cloud_layer` entry in `SHELL_CONFIGS['Neptune']` (Section 6.1). The
helper enforces the single-info-marker pattern and uses the canonical
`create_info_marker()` placement.

Verification: after dispatch delegation, call
`build_sphere_shell(SHELL_CONFIGS['Neptune']['cloud_layer'], 'Neptune',
(0, 0, 0))` and confirm it returns 2 traces (mesh3d + info marker).

The source function `create_neptune_cloud_layer_shell` stays in place
but unused. Phase D decides whether to archive it.

### 6.5 Neptune upper atmosphere -- sun_traces removal

Standalone sphere builder. Strip embedded sun indicator. Same pattern
as Saturn 4.5 / Uranus 5.5.

### 6.6 Neptune magnetosphere refactor (lines ~469-634)

This is the most physics-sensitive refactor in C4. The function does
its OWN region-specific tilt/azimuth/offset handling for bow shock /
internal / tail regions. This handling is PRESERVED.

Changes:
1. Add `sun_position=(0, 0, 0)` parameter to function signature.
2. After all internal rotations and the final coordinate offset
   concatenation, apply `rotate_to_sunward()` with `magnetic_tilt_deg=0`
   (the 47-deg tilt is already applied internally; double-tilting would
   be a physics error).
3. Strip the embedded `sun_traces` block.
4. Replace the inline info marker with `create_info_marker()`,
   positioned at the first point of the sunward-rotated, offset
   geometry.
5. **Leave `create_neptune_magnetic_poles` UNTOUCHED.** Bounded scope
   per Opus 4.6 review (May 2026). See 6.6.2 below.

Current source (lines 469-634): emits 1 magnetosphere geometry trace
(line 573-587), 1 inline info marker (line 588-599), then the
sun_traces block (601-606), then 4 magnetic pole traces (608-632
via `create_neptune_magnetic_poles`). Total source: 1 + 1 + N_sun + 4
where N_sun is typically 2 (line + arrow). Excluding sun traces:
6 traces.

After C4: 6 traces (1 magnetosphere + 1 info marker + 4 magnetic
poles). Sun traces dropped. Info marker switches to `create_info_marker()`.

#### 6.6.1 The sunward rotation question for Neptune magnetosphere

The function applies its OWN rotations to the internal magnetosphere
region (lines 530-547). After this, `x_final, y_final, z_final`
contain the assembled geometry in Neptune's body frame, with the
default convention: bow shock at -X, tail at +X.

The `rotate_to_sunward()` call must operate on this assembled
geometry BEFORE center offset is applied. Code structure:

```python
    # Recombine the components (line 545-547 in source, KEEP)
    x_final = np.concatenate([bow_shock_x, int_x2, tail_x2])
    y_final = np.concatenate([bow_shock_y, int_y2, tail_y2])
    z_final = np.concatenate([bow_shock_z, int_z2, tail_z2])

    # Phase C4 NEW: rotate to face actual Sun direction.
    # magnetic_tilt_deg=0 because the internal 47-deg tilt is already
    # applied above (region-specific rotation on lines 530-547).
    # Double-tilting would be a physics error.
    x_final, y_final, z_final = rotate_to_sunward(
        x_final, y_final, z_final,
        center_position=center_position,
        sun_position=sun_position,
        magnetic_tilt_deg=0,
    )

    # Apply center offset to rotated geometry (REPLACE source lines 549-555)
    center_x, center_y, center_z = center_position
    x_final = x_final + center_x
    y_final = y_final + center_y
    z_final = z_final + center_z
```

#### 6.6.2 Magnetic poles call site -- BOUNDED SCOPE

`create_neptune_magnetic_poles(center_position, offset_distance,
magnetic_tilt, azimuthal_angle)` generates 4 traces representing
the magnetic field center (diamond at the 0.55 R_N offset), the
magnetic axis (dashed line through the tilted axis), and north/south
pole markers.

**Decision (Opus 4.6 review, Tony approved May 17 2026): leave
`create_neptune_magnetic_poles` UNTOUCHED for C4.** The call site
at line 610 keeps its current 4-argument form.

Consequence: the 4 pole/axis traces stay in Neptune's body frame.
They do NOT track the sunward direction. The envelope cloud (the
visually dominant feature) DOES rotate correctly because of Section
6.6.1.

**Visible effect for Mode 5:** in heliocentric Neptune renders with
Neptune at any position not on the +X axis, the 4 pole traces will
drift off the rotated envelope. For Neptune at, say, (28, 12, -1) AU,
the envelope rotates ~23 degrees to face origin; the poles do not.
Misalignment will be noticeable to someone looking for it -- the
poles will appear slightly inside or outside the envelope rather
than along its magnetic axis.

This is accepted for C4 mechanical migration. Phase D wires
`sun_position` from ephemeris at every magnetosphere call site,
which is the natural pass for upgrading `create_neptune_magnetic_poles`
to track the sunward direction. Documented in Section 8.2.

**The full-fix path** (extending `create_neptune_magnetic_poles`
signature with `sun_position` and wrapping point emission in a
`_emit` helper) is sketched in Section 8.2 item 6 for Phase D
implementation.

#### 6.6.3 Sun indicator removal

Strip the `sun_traces = create_sun_direction_indicator(...)` block at
lines 601-606.

#### 6.6.4 Info marker style

Source uses an inline scatter3d info marker at line 588-599 with
position `[x_final[0], y_final[0], z_final[0]]` (first point of the
post-rotation, post-offset geometry). Replace with `create_info_marker()`:

```python
    traces.append(create_info_marker(
        x_final[0], y_final[0], z_final[0],
        'rgb(30, 136, 229)', magnetosphere_text[0], 'Neptune: Magnetosphere'
    ))
```

The position computation must use the sunward-rotated, offset
coordinates from Section 6.6.1 (not the source's pre-sunward-rotation
values). The helper centralizes marker style; position is the caller's
responsibility -- matches the Saturn 4.6.2 pattern.

### 6.7 Strip `create_neptune_field_lines` (lines 769-860)

Per Tony's decision Q4 (changed from "leave" to "strip"). The function
is defined but never called. Strip the function definition AND the
"THIS FUNCTION APPEARS OBSOLETE" comment at line 769.

Lines to remove: 769 through 860 inclusive (the entire function block
plus the preceding obsolete-marker comment). 92 lines.

After stripping, the file shrinks from 1844 lines to ~1752 lines (with
other Section 6 edits possibly adjusting further).

### 6.8 Neptune radiation belts refactor (lines ~867-1103)

This is the most complex builder in C4. Emits multiple belt geometries
plus field-aligned currents (via internal helper call). Per v6 prompt:
12 traces total = (3 belts + cusp region + 2 FAC) x 2.

#### 6.8.1 Pre-existing info marker position bug at line 1078

Source line 1077-1088:
```python
        traces.append(go.Scatter3d(
            x=[belt_x[0]], y=[belt_y[0]], z=[belt_z[0]],
            mode='markers',
            ...
            name='',
            legendgroup=f"Neptune: {belt['name']}",
            text=[belt['description']],
            ...
        ))
```

`belt_x[0]` is the FIRST point of the PRE-rotation belt geometry.
After the rotation block (lines 1010-1055), the actual rendered
geometry uses `x_final = x_rotated2 + magnetic_center_x`. The info
marker should be placed at the FIRST point of the FINAL (post-rotation,
post-offset) geometry.

**Bug fix AND helper adoption:** replace the inline scatter3d with a
`create_info_marker()` call using the post-rotation, post-offset
position. Final code:

```python
        traces.append(create_info_marker(
            x_final[0], y_final[0], z_final[0],
            belt['color'], belt['description'], f"Neptune: {belt['name']}"
        ))
```

This is a content fix (marker visibly relocates from off-axis to the
actual belt) plus style centralization. Flag for Mode 5.

#### 6.8.2 Pre-existing info marker position bug in FAC at line 1211

Same bug in `create_field_aligned_currents`. Source line 1210-1221:
```python
        traces.append(go.Scatter3d(
            x=[current_x[0]], y=[current_y[0]], z=[current_z[0]],
            ...
        ))
```

`current_x[0]` is pre-rotation. Fix position AND adopt helper:

```python
        traces.append(create_info_marker(
            x_final[0], y_final[0], z_final[0],
            params.get('color', 'rgb(200, 200, 255)'),
            params['description'], f"Neptune: {params['name']}"
        ))
```

`x_final, y_final, z_final` are defined at lines 1186-1188 in source
(post-rotation, post-magnetic-center-offset).

#### 6.8.3 Radiation belts NOT rotated by `rotate_to_sunward()`

Per Tony's decision Q7. Belts are axis-anchored. The internal
magnetic_center offset (which incorporates Neptune's dipole offset)
is part of the belt builder's logic and stays internal.

No change to belt rotation handling. Only the info marker bugs are
fixed (Sections 6.8.1, 6.8.2).

#### 6.8.4 Sun indicator removal

Strip the `sun_traces` block at lines 1096-1101.

#### 6.8.5 Trace count after C4

12 traces total. Source structure (verify by reading belt definitions
~ lines 870-1000):
- 3 belts (inner / outer / plasma): 3 * 2 = 6 traces.
- 1 cusp region: 1 * 2 = 2 traces.
- 2 FAC traces (dawn / dusk via `create_field_aligned_currents`):
  2 * 2 = 4 traces.

Total: 6 + 2 + 4 = 12.

If actual count differs from 12 after running the smoke test, inspect
the source belt definitions and reconcile. The v6 prompt's "3 belts
+ cusp + 2 FAC" is from a previous audit; final count must come from
running `len(create_neptune_radiation_belts((0,0,0)))` and
inspecting the belt definitions.

### 6.9 Neptune hill sphere

Same pattern as Saturn 4.9 / Uranus 5.8. Move config to SHELL_CONFIGS.
Strip sun indicator from source.

### 6.10 Neptune ring system refactor (lines ~1254-1762)

11 ring components -> 22 traces. Source uses `create_ring_points()`
(Phase C3 promotion). Source applies compound rotation: X-axis at
32 deg, Y-axis at 34 deg (NOT `neptune_tilt = 28.32 deg`). The
neptune_tilt value is used only in the info marker placement at line
1741, which creates a known geometric mismatch (info marker tilted at
28.32 deg, geometry tilted at 32+34 deg).

**Defer rotation mismatch fix to Phase D** (rationale: the geometry
rotation is empirical fit for visual correctness; the info marker
placement should use the same rotation parameters but this requires
reading what 32 and 34 actually are and reconciling with neptune_tilt.
Out of scope for C4 mechanical migration).

Section 8 documents this as a known issue.

For C4:
1. Strip `sun_traces` block at the end of the function.
2. KEEP all rotation logic (geometry compound rotation + info marker
   neptune_tilt). Geometric mismatch preserved -- documented for Phase D.
3. Replace inline ring info markers with `create_info_marker()` calls,
   preserving the source's position computation (compound-tilted
   outer-radius point in the rendered frame). For each ring/arc, replace
   the inline `go.Scatter3d(...)` at line ~1741 with:
   ```python
        traces.append(create_info_marker(
            mx_t2[0] + center_x, my_t2[0] + center_y, mz_t2[0] + center_z,
            ring_info['color'], ring_info['description'],
            f"Neptune: {ring_info['name']}"
        ))
   ```
   This is style centralization only; positions unchanged.
4. Adams ring arcs (Liberte, Egalite 1, Egalite 2, Fraternite,
   Courage) are 5 of the 11 ring components -- they're built inline
   using custom angular range geometry rather than full rings, but
   they still emit 1 geometry + 1 info marker per arc. Total ring
   trace count: 11 * 2 = 22. KEEP all arc geometry preserved.

### 6.11 Neptune CUSTOM_SHELLS entry

Schema matches Jupiter (`shell_configs.py` line 1775), Saturn
(Section 4.11), and Uranus (Section 5.10): `'builder'` = single string
path `module.function_name`, `'tooltip'` = inline string.

```python
    'Neptune': {

        'magnetosphere': {
            'builder': 'neptune_visualization_shells.create_neptune_magnetosphere',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.5 AU TO VISUALIZE.\n"
                "1.0 MB PER FRAME FOR HTML.\n\n"
                "Neptune's magnetosphere is dramatically tilted (47 degrees from\n"
                "the rotation axis) and significantly offset (more than half a\n"
                "Neptune radius from the planet's center). The result is an extremely\n"
                "asymmetric magnetosphere that varies greatly depending on Neptune's\n"
                "16-hour rotation.\n\n"
                "Rendered features:\n"
                "  * Magnetosphere envelope with internal 47-deg tilt + 60-deg azimuth\n"
                "  * Bow shock facing the actual Sun direction\n"
                "  * 4 magnetic-pole structures (mag center, axis, north, south poles)\n\n"
                "Source: Voyager 2 Mission Archive; Ness et al. (1989, Science) --\n"
                "the only spacecraft to visit Neptune; all parameters from the 1989 flyby."
            ),
        },

        'radiation_belts': {
            'builder': 'neptune_visualization_shells.create_neptune_radiation_belts',
            'tooltip': (
                "560 KB PER FRAME FOR HTML.\n\n"
                "Neptune has a complex radiation belt environment shaped by its\n"
                "47-degree-tilted, offset magnetic field. The belts include inner\n"
                "and outer regions plus a cusp region, with field-aligned currents\n"
                "(FAC) connecting magnetospheric regions.\n\n"
                "All parameters derive from the Voyager 2 flyby (1989), the only\n"
                "in-situ visit to Neptune.\n\n"
                "The same builder produces all belt + cusp + FAC traces (separate\n"
                "legend entries per region)."
            ),
        },

        'ring_system': {
            'builder': 'neptune_visualization_shells.create_neptune_ring_system',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.001 AU TO VISUALIZE.\n"
                "22.2 MB PER FRAME FOR HTML.\n\n"
                "Neptune has 5 named rings (Galle, Le Verrier, Lassell, Arago, Adams)\n"
                "plus diffuse outer dust. The Adams Ring is famous for its arc\n"
                "structure -- five named arcs (Courage, Liberte, Egalite 1, Egalite 2,\n"
                "Fraternite) confined by gravitational resonance with the moon\n"
                "Galatea.\n\n"
                "Source: NASA Planetary Ring Node; Smith et al. (1989, Science) --\n"
                "Voyager 2 encounter; subsequent Hubble and ground-based observations."
            ),
        },

    },
```

**No imports added to `shell_configs.py`.** Tooltip strings are inline,
matching the Jupiter pattern.

### 6.12 Neptune dispatch delegation in `planet_visualization.py`

Replace the entire Neptune block at lines 784-800:

```python
    if planet_name == 'Neptune':
        # Step 3 Phase C4: delegate to unified config-driven dispatch.
        # Same pattern as Saturn / Uranus (Phase C4, this session).
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Neptune',
            center_object='Neptune',
        )
```

### 6.13 Bottom-up edit order within `neptune_visualization_shells.py`

Edit lines in DECREASING line-number order:

1. Strip `sun_traces` from `create_neptune_hill_sphere_shell` (~1776+).
2. Strip `sun_traces` from `create_neptune_ring_system` (end of function ~1760).
3. Replace ring info markers with `create_info_marker()` calls in
   `create_neptune_ring_system` (line ~1741 -- position unchanged,
   style centralized).
4. Replace FAC info marker with `create_info_marker()` at line 1210-1221
   AND fix position bug (current_x[0] -> x_final[0]).
5. Strip `sun_traces` from `create_neptune_radiation_belts` (lines 1096-1101).
6. Replace radiation belt info marker with `create_info_marker()` at
   line 1077-1088 AND fix position bug (belt_x[0] -> x_final[0]).
7. Strip dead `create_neptune_field_lines` function (lines 769-860,
   plus the "OBSOLETE" comment at 769).
8. **`create_neptune_magnetic_poles` UNTOUCHED** (bounded scope per
   Section 6.6.2).
9. Refactor `create_neptune_magnetosphere` body (lines 469-634)
   per Section 6.6. Add `sun_position` parameter. Apply
   `rotate_to_sunward(magnetic_tilt_deg=0)` after `x_final, y_final,
   z_final = np.concatenate(...)` block. Strip `sun_traces`. Replace
   inline info marker with `create_info_marker()` at the sunward-rotated,
   offset first point. Leave `create_neptune_magnetic_poles` call site
   at line 610 UNCHANGED (4 arguments, no `sun_position`).
10. Strip `sun_traces` from `create_neptune_upper_atmosphere_shell`
    (~365+, in function body).
11. Cloud layer: no source edit (Section 6.4).
12. Update imports at top.

### 6.14 Neptune verification

```bash
python3 -c "
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS

# Sphere configs
expected_sphere = {'core', 'mantle', 'cloud_layer', 'upper_atmosphere', 'hill_sphere'}
assert set(SHELL_CONFIGS['Neptune'].keys()) == expected_sphere

# Custom configs
expected_custom = {'magnetosphere', 'radiation_belts', 'ring_system'}
assert set(CUSTOM_SHELLS['Neptune'].keys()) == expected_custom

# Sphere builder smoke
from orrery_rendering import build_sphere_shell
for shell_name, cfg in SHELL_CONFIGS['Neptune'].items():
    traces = build_sphere_shell(cfg, 'Neptune', (0, 0, 0))
    assert len(traces) == 2, 'Neptune/%s: expected 2 traces, got %d' % (shell_name, len(traces))
print('Neptune sphere builder smoke: PASS')

# Custom geometry trace counts
import importlib
mod = importlib.import_module('neptune_visualization_shells')

trace_counts = {
    'create_neptune_magnetosphere': 6,    # 1 geom + 1 marker + 4 poles
    'create_neptune_radiation_belts': 12, # 3 belts + cusp + 2 FAC, each * 2
    'create_neptune_ring_system': 22,     # 11 rings/arcs * 2
}

for fname, expected in trace_counts.items():
    traces = getattr(mod, fname)((0, 0, 0))
    actual = len(traces)
    assert actual == expected, '%s: expected %d, got %d' % (fname, expected, actual)
    print('  %s: %d traces' % (fname, actual))

# Magnetosphere rotation (with magnetic_tilt_deg=0 but internal 47 deg preserved)
import numpy as np

mag_origin = mod.create_neptune_magnetosphere((0, 0, 0))
mag_off = mod.create_neptune_magnetosphere((-1.0, 0.0, 0.0))
origin_x = np.array(mag_origin[0].x)
off_x = np.array(mag_off[0].x) - (-1.0)
assert np.allclose(off_x, -origin_x, atol=1e-9), 'Neptune magnetosphere rotation failed'
print('Neptune magnetosphere rotation (180 deg): PASS')

# Belts NOT rotated by sunward rotation
belts_origin = mod.create_neptune_radiation_belts((0, 0, 0))
belts_off = mod.create_neptune_radiation_belts((-1.0, 0.0, 0.0))
b_o_x = np.array(belts_origin[0].x)
b_f_x = np.array(belts_off[0].x) - (-1.0)
assert np.allclose(b_o_x, b_f_x, atol=1e-9), 'Neptune radiation belts unexpectedly rotated'
print('Neptune radiation belts: PASS (unrotated)')

# Rings NOT rotated
rings_origin = mod.create_neptune_ring_system((0, 0, 0))
rings_off = mod.create_neptune_ring_system((-1.0, 0.0, 0.0))
r_o_x = np.array(rings_origin[0].x)
r_f_x = np.array(rings_off[0].x) - (-1.0)
assert np.allclose(r_o_x.max(), r_f_x.max(), atol=1e-6), 'Neptune rings unexpectedly rotated'
print('Neptune rings: PASS (unrotated)')

# Dead function stripped
import neptune_visualization_shells
assert not hasattr(neptune_visualization_shells, 'create_neptune_field_lines'), 'Dead function survived'
print('Neptune create_neptune_field_lines: PASS (stripped)')

# Dispatch delegation
import inspect, planet_visualization
src = inspect.getsource(planet_visualization.create_planet_visualization)
assert 'create_neptune_core_shell(center_position)' not in src, 'Old Neptune dispatch survived'
print('Neptune dispatch: PASS (old block removed)')

print()
print('Section 6 (Neptune) verification PASS')
"
```

If the magnetosphere rotation assertion fails, check the order of
operations: sunward rotation must happen BEFORE the center offset.
The internal region-specific rotations (47-deg Y-axis, 60-deg Z-axis)
happen BEFORE sunward rotation -- both internal-rotation operations
and sunward rotation are in the body frame (pre-translation).

If trace counts differ, inspect the source belt/ring definitions
to reconcile. Most likely cause: cusp region and FAC trace counts
may not match the 12 prediction.


---

## 7. Final Verification Plan

Run after Sections 3-6 complete. All assertions must PASS before Phase
C4 is considered done.

### 7.1 Final state inventory

After C4 completion, the system should have:

| Component | Expected count |
|-----------|---------------:|
| Bodies in SHELL_CONFIGS | 12 (Mercury, Moon, Planet 9, Pluto, Eris, Venus, Mars, Earth, Jupiter, Saturn, Uranus, Neptune) |
| Total sphere shell configs | 68 (52 from C3 + 16 from C4: 6 Saturn + 5 Uranus + 5 Neptune) |
| Bodies in CUSTOM_SHELLS | 8 (5 from C3 + 3 from C4: Saturn, Uranus, Neptune) |
| Total custom entries | 21 (11 from C3 + 10 from C4: 4 Saturn + 3 Uranus + 3 Neptune) |
| Bodies on old dispatch | 1 (Sun) |
| `rotate_to_sunward()` exercised | 8 bodies (Mercury, Venus, Mars, Earth, Jupiter, Saturn, Uranus, Neptune) |
| `create_ring_points()` used by | 4 bodies (Saturn, Uranus, Neptune; Jupiter uses local helper) |
| `magnetic_tilt_deg` used by | 1 body (Uranus, value=60) |

### 7.2 Phase C4 final verification

```bash
python3 -c "
import sys
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS

# Bodies in SHELL_CONFIGS
expected_sphere_bodies = {
    'Mercury', 'Moon', 'Planet 9', 'Pluto', 'Eris',
    'Venus', 'Mars', 'Earth', 'Jupiter',
    'Saturn', 'Uranus', 'Neptune',
}
actual = set(SHELL_CONFIGS.keys())
missing = expected_sphere_bodies - actual
extra = actual - expected_sphere_bodies
assert not missing, 'Missing SHELL_CONFIGS bodies: %s' % missing
print('SHELL_CONFIGS bodies: %d (expected 12)' % len(actual))
assert len(actual) == 12, 'Wrong body count'

# Total sphere configs
total_sphere = sum(len(v) for v in SHELL_CONFIGS.values())
print('Total sphere configs: %d (expected 68)' % total_sphere)
assert total_sphere == 68, 'Wrong sphere config count'

# Bodies in CUSTOM_SHELLS
expected_custom_bodies = {
    'Mercury', 'Venus', 'Mars', 'Earth', 'Jupiter',
    'Saturn', 'Uranus', 'Neptune',
}
custom_actual = set(CUSTOM_SHELLS.keys())
missing = expected_custom_bodies - custom_actual
extra = custom_actual - expected_custom_bodies
assert not missing, 'Missing CUSTOM_SHELLS bodies: %s' % missing
print('CUSTOM_SHELLS bodies: %d (expected 8)' % len(custom_actual))
assert len(custom_actual) == 8, 'Wrong custom body count'

# Total custom entries
total_custom = sum(len(v) for v in CUSTOM_SHELLS.values())
print('Total custom entries: %d (expected 21)' % total_custom)
assert total_custom == 21, 'Wrong custom entry count'

# Saturn / Uranus / Neptune dispatch delegation
import inspect, planet_visualization
src = inspect.getsource(planet_visualization.create_planet_visualization)
for body in ('saturn_core', 'uranus_core', 'neptune_core'):
    assert 'create_%s_shell(center_position)' % body not in src, (
        'Old dispatch survived for %s' % body
    )
print('All old dispatch blocks removed (Saturn / Uranus / Neptune)')

# rotate_to_sunward magnetic_tilt_deg=60 verified for Uranus
from shell_configs import CUSTOM_SHELLS
# The configs themselves don't contain the magnetic_tilt_deg parameter;
# that's hardcoded in the Uranus magnetosphere builder. Spot-check
# the builder source for the parameter.
import inspect
import uranus_visualization_shells
mag_src = inspect.getsource(uranus_visualization_shells.create_uranus_magnetosphere)
assert 'magnetic_tilt_deg=60' in mag_src, 'Uranus magnetic_tilt_deg=60 not wired'
print('Uranus magnetic_tilt_deg=60: PASS')

print()
print('===== Phase C4 FINAL VERIFICATION PASS =====')
"
```

### 7.3 Cross-body rotation isolation

Verify that magnetospheres rotate sunward and rings/belts do NOT,
across all three C4 bodies:

```bash
python3 -c "
import numpy as np
import importlib

for body, mod_name, mag_func, belt_func, ring_func in (
    ('Saturn',  'saturn_visualization_shells',
     'create_saturn_magnetosphere',
     'create_saturn_radiation_belts',
     'create_saturn_ring_system'),
    ('Uranus',  'uranus_visualization_shells',
     'create_uranus_magnetosphere',
     'create_uranus_radiation_belts',
     'create_uranus_ring_system'),
    ('Neptune', 'neptune_visualization_shells',
     'create_neptune_magnetosphere',
     'create_neptune_radiation_belts',
     'create_neptune_ring_system'),
):
    mod = importlib.import_module(mod_name)

    # Magnetosphere rotation
    mag_o = getattr(mod, mag_func)((0, 0, 0))
    mag_f = getattr(mod, mag_func)((-1.0, 0.0, 0.0))
    ox = np.array(mag_o[0].x); fx = np.array(mag_f[0].x) - (-1.0)
    assert np.allclose(fx, -ox, atol=1e-9), '%s magnetosphere rotation failed' % body
    print('%s magnetosphere: rotated' % body)

    # Belt NOT rotated by sunward (axial tilt internal)
    b_o = getattr(mod, belt_func)((0, 0, 0))
    b_f = getattr(mod, belt_func)((-1.0, 0.0, 0.0))
    ox = np.array(b_o[0].x); fx = np.array(b_f[0].x) - (-1.0)
    assert np.allclose(ox, fx, atol=1e-6), '%s radiation belts unexpectedly rotated' % body
    print('%s belts: NOT rotated (correct)' % body)

    # Rings NOT rotated
    r_o = getattr(mod, ring_func)((0, 0, 0))
    r_f = getattr(mod, ring_func)((-1.0, 0.0, 0.0))
    ox = np.array(r_o[0].x); fx = np.array(r_f[0].x) - (-1.0)
    assert np.allclose(ox.max(), fx.max(), atol=1e-6), '%s rings unexpectedly rotated' % body
    print('%s rings: NOT rotated (correct)' % body)
    print()

print('Cross-body rotation isolation: PASS')
"
```

### 7.4 Mode 5 visual verification checklist (Tony)

After all assertions pass, Tony validates visually:

| Check | Body | Expected |
|-------|------|----------|
| All sphere shells render (core, mantle, cloud, upper atmosphere, hill sphere) | S/U/N | All visible, centered |
| Cloud layer is solid mesh3d | S/U/N | Mesh, not point cloud |
| Hill sphere visible at manual scale >= 0.5 AU | S/U/N | Visible |
| Magnetosphere rotates with off-center view | S/U/N | Tail away from Sun |
| Magnetic tilt visible on Uranus magnetosphere | U | Dipole axis tilted 60 deg from rotation axis |
| Neptune magnetic poles visible and aligned with magnetosphere | N | 4 traces visible |
| Neptune internal magnetic tilt preserved (47 deg) | N | Asymmetric magnetosphere |
| Rings equatorial, NOT rotated by sunward direction | S/U/N | Static ring plane |
| Radiation belts axial, NOT rotated by sunward direction | S/U/N | Static belt position |
| Enceladus torus equatorial, NOT rotated | S | Static torus |
| Saturn ring tooltip references SATURN moons, not Jupiter | S | Tooltip correct |
| Saturn cloud layer info marker hidden when toggled off | S | No orphan marker |
| Uranus cloud layer info marker hidden when toggled off | U | No orphan marker |
| Neptune cloud layer info marker hidden when toggled off | N | No orphan marker |
| Sun direction indicator: ONE per render | S/U/N | Single indicator |
| Animation heliocentric: shells NOT displayed | S/U/N | Static body only |
| Animation Saturn/Uranus/Neptune-centered: static shells, moons orbit | S/U/N | Correct |
| GUI tooltips on all shell checkboxes | S/U/N | All present |
| Uranus radiation belts at correct axial position (cleanup side effect) | U | No 2x offset from prior bug |

Note: the Uranus belt axial position check (last row) is the visual
verification of the Section 5.7 dead-code cleanup. Tony's pre-existing
expectation may include the double-offset position; after C4, the
belts move to their physically-correct position. Confirm acceptable.

### 7.5 Compile and lint

```bash
python3 -c "
import compileall, sys
ok = compileall.compile_file('orrery_rendering.py', force=True, quiet=1) and \
     compileall.compile_file('shell_configs.py', force=True, quiet=1) and \
     compileall.compile_file('planet_visualization.py', force=True, quiet=1) and \
     compileall.compile_file('saturn_visualization_shells.py', force=True, quiet=1) and \
     compileall.compile_file('uranus_visualization_shells.py', force=True, quiet=1) and \
     compileall.compile_file('neptune_visualization_shells.py', force=True, quiet=1)
sys.exit(0 if ok else 1)
"
```

All 6 files must compile cleanly.

### 7.6 LF and ASCII verification

```bash
for f in orrery_rendering.py shell_configs.py planet_visualization.py \
         saturn_visualization_shells.py uranus_visualization_shells.py \
         neptune_visualization_shells.py; do
    # CRLF check
    if grep -lU $'\r' "$f"; then
        echo "FAIL: $f contains CRLF"
        exit 1
    fi
    # ASCII check
    if ! file "$f" | grep -q "ASCII"; then
        echo "FAIL: $f is not ASCII"
        exit 1
    fi
done
echo "LF / ASCII verification: PASS"
```

### 7.7 Run provenance scanner

```bash
python3 provenance_scanner.py
```

Expected: 0 Tier-1 findings on the 6 touched files. Existing Tier-2
residuals are accepted per Phase C3 audit.

---

## 8. Decision Log and Open Items

### 8.1 Decisions made during this manifest authoring

| # | Decision | Rationale |
|---|----------|-----------|
| 1 | `magnetic_tilt_deg` applied as X-axis rotation in the default frame BEFORE sunward Rodrigues rotation. Sign: `+magnetic_tilt_deg` about `+X`; for Uranus tilts +Z dipole toward -Y | Opus 4.6 physics review (May 2026) confirmed: only rotation that tilts the dipole while preserving sunward bow shock. Z-axis rotation (Tony's literal directive) is a physics error -- moves bow shock off -X. Y-axis rotation also wrong |
| 2 | Saturn ring tooltip rewritten with Saturn-specific content during extraction | Tony's decision Q: fix the Jupiter copy-paste error |
| 3 | Uranus magnetosphere info marker added (was missing in source) | Tony's decision Q2: add it, last chance before Phase D |
| 4 | Uranus radiation belt dead code stripped (3 separate blocks: pre-tilt offset, no-op variable recast, dead Y-axis rotation, commented-out blocks) | Tony's decision Q1.b. Behavior change: belts move to correct axial position |
| 5 | `create_neptune_field_lines` (lines 769-860, dead) stripped | Tony's decision Q4 (changed from "leave" to "strip") |
| 6 | Neptune `create_neptune_magnetic_poles` UNTOUCHED for C4 (bounded scope) | Opus 4.6 review + Tony approval May 17 2026. Phase D's `sun_position` ephemeris pass-through is the natural moment to extend this helper. C4 stays mechanical |
| 7 | Neptune radiation belts info marker position bug fixed (line 1078: belt_x[0] -> x_final[0]) AND helper adopted | Pre-existing bug. Marker was floating off-axis; fix relocates it to belt |
| 8 | Neptune FAC info marker position bug fixed (line 1211: current_x[0] -> x_final[0]) AND helper adopted | Same pattern as Section 8.1.7 |
| 9 | Saturn radiation belts pre-existing double-offset audited before touching, fixed only if confirmed same bug | Per Opus 4.6 review item 10: cheap audit step at top of Saturn implementation. If same pattern as Uranus belts, fix in C4; if not, preserve and document for Phase D |
| 10 | Neptune ring system info marker rotation mismatch (neptune_tilt=28.32 vs geometry rotation 32+34) NOT fixed in C4 | Out of scope for mechanical migration. Documented for Phase D |
| 11 | All info markers use `create_info_marker()` helper. Positions match source intent (first point of geometry for non-sphere; helper enforces north pole at radius*1.05 for sphere shells via `build_sphere_shell`) | Centralizes marker style. Helper signature is `create_info_marker(x, y, z, color, text, legendgroup, customdata=None)` -- places marker at literal (x, y, z), no internal offset |
| 12 | Magnetosphere `legendgroup` added to Uranus geometry trace (source omits it) | Required so info marker (which adds a legendgroup) properly groups. Side-effect bug fix |
| 13 | Magnetic tilt sign convention: right-hand rule about +X. +60 deg tilts +Z toward -Y. Mode 5 can flip the sign if Voyager-2-era convention prefers the other direction | Documented in Section 3.1; aligns with rotation matrix used in `rotate_to_sunward()` |

### 8.2 Items deferred to Phase D

These are flagged for follow-up after C4 closes:

1. **Earth (`magnetic_tilt_deg=11`) and Jupiter (`magnetic_tilt_deg=10`)**
   wiring. Visually subtle at those angles. Phase D's `sun_position`
   pass-through revisits every body's magnetosphere call site; add the
   tilt parameter at that point.

2. **Saturn radiation belt pre-existing double-offset bug.** Source
   appears to apply center offset twice (pre-tilt and post-tilt) --
   same pattern as Uranus belts. C4 includes an audit step at the top
   of Saturn implementation (Section 4.8 step 0); if confirmed, fix in
   C4. If audit shows the pattern is different, Mode 7 (Gemini) review
   in Phase D can confirm whether the post-tilt-only offset is
   physically correct.

3. **Neptune ring info marker rotation mismatch.** Geometry uses
   compound X (32 deg) + Y (34 deg) rotation; info marker placement
   uses `neptune_tilt = 28.32 deg`. Fix during Phase D ring system
   audit.

4. **Neptune `print()` debug statement at line 766** in
   `create_neptune_magnetic_poles`. Cosmetic. Remove during Phase D.

5. **Function-local imports in `neptune_visualization_shells.py`**
   (each function repeats `import numpy as np`, etc.). Harmless
   redundancy; clean up during Phase D module-level reorganization.

6. **Neptune magnetic poles `sun_position` extension.** Per Section
   6.6.2, C4 leaves `create_neptune_magnetic_poles` untouched. In
   off-axis heliocentric views (Neptune not on +X), the 4 pole/axis
   traces drift off the rotated envelope. Phase D fix: extend the
   signature with `sun_position=(0, 0, 0)`, wrap point assembly with
   a `_emit` helper:
   ```python
   def _emit(px, py, pz):
       rx, ry, rz = rotate_to_sunward(
           np.asarray(px), np.asarray(py), np.asarray(pz),
           center_position=center_position,
           sun_position=sun_position,
           magnetic_tilt_deg=0,
       )
       return rx + center_x, ry + center_y, rz + center_z
   ```
   Refactor each pole trace's point assembly to use `_emit()`. Update
   the call site at line 610 in `create_neptune_magnetosphere` to pass
   `sun_position`. ~30 lines of surgery; coincides with Phase D's
   ephemeris wiring sweep.

7. **`create_sun_direction_indicator` import in S/U/N modules**
   becomes unused after sun_traces stripping. Remove during Phase D
   import cleanup.

8. **Sun unification** (final body on old dispatch). Phase D primary
   work item.

9. **`sun_position` wiring**. Phase D wires actual ephemeris-derived
   Sun position into the rotate_to_sunward call sites for all 8
   sunward-rotated bodies. Item 6 happens during this pass.

10. **Retire `create_planet_visualization()`** after Sun migrates.
    Phase D work item.

11. **Archive dead shell files**: any sphere shell builder functions
    that remain unused after C4 dispatch delegation (cloud_layer,
    upper_atmosphere, hill_sphere for Saturn/Uranus/Neptune). Phase D
    per-function decision.

12. **Tooltip rewiring**: GUI tooltips that reference function names
    or paths that have changed. Phase D.

### 8.3 Open questions for Tony

Resolved during Opus 4.6 review (May 17 2026):

- ~~Neptune `create_neptune_magnetic_poles` signature change~~ -> Bounded
  scope. Helper untouched in C4; full fix queued for Phase D (Section
  8.2 item 6).
- ~~`magnetic_tilt_deg` rotation axis interpretation~~ -> Confirmed
  X-axis rotation before sunward. Z-axis (Tony's literal directive)
  is a physics error -- moves bow shock off -X.

Still open for Mode 5 visual review during implementation:

1. **Uranus radiation belt axial position change** (Section 5.7):
   the dead-code cleanup fixes a pre-existing double-offset bug that
   moved belts to an incorrect position. After C4, belts move to
   their physically correct position. Acceptable, or preserve the
   bug for visual consistency with prior renders?

2. **Uranus magnetic_tilt_deg sign convention** (Section 3.1):
   +60 deg about +X tilts +Z dipole toward -Y. If the Voyager-2-era
   convention prefers the other direction, flip the sign at the C4
   call site (Section 5.6) -- one-character change.

3. **Neptune radiation belt trace count**: predicted 12 traces
   (3 belts + cusp + 2 FAC, each x 2). Audit found the same structure
   but the exact count must be confirmed by running the smoke test.
   If different, reconcile by reading belt definitions at runtime.

4. **Neptune magnetic pole misalignment in heliocentric views**
   (Section 6.6.2): the 4 pole/axis traces will visibly drift off
   the rotated envelope for Neptune at any position not on +X axis.
   Expected for bounded scope. Mode 5 confirms this is acceptable
   for C4 (Phase D fixes via item 8.2.6).

---

## 9. Phase C4 Summary

### 9.1 Files modified

| File | Lines (before) | Lines (after, est.) | Changes |
|------|---------------:|--------------------:|---------|
| `orrery_rendering.py` | 309 | ~325 | `magnetic_tilt_deg` X-axis rotation implemented in `rotate_to_sunward()` |
| `shell_configs.py` | 1,840 | ~2,150 | +Saturn 6 sphere configs, +Uranus 5 sphere configs, +Neptune 5 sphere configs in SHELL_CONFIGS; +Saturn 4 custom entries, +Uranus 3 custom entries, +Neptune 3 custom entries in CUSTOM_SHELLS (inline tooltip strings, no module imports) |
| `planet_visualization.py` | 901 | ~858 | Saturn / Uranus / Neptune dispatch blocks (lines 744-800, 57 lines) replaced with 3 x 9-line delegation blocks (-30 net) |
| `saturn_visualization_shells.py` | 1,251 | ~1,180 | Imports updated, magnetosphere refactored (rotation), 6 sun_traces stripped, ring tooltip rewritten, custom builders' info markers migrated to `create_info_marker()`. Belt double-offset audit (Section 4.8.0) may add ~5 line cleanup if same bug as Uranus |
| `uranus_visualization_shells.py` | 1,178 | ~1,090 | Imports updated, magnetosphere refactored (rotation + info marker added + magnetic_tilt_deg=60), 5 sun_traces stripped, radiation belt dead code cleanup (~15 lines stripped), all info markers migrated to `create_info_marker()` |
| `neptune_visualization_shells.py` | 1,844 | ~1,740 | Imports updated, magnetosphere refactored (sunward rotation, internal 47-deg tilt preserved, info marker via helper). `create_neptune_magnetic_poles` UNTOUCHED (bounded scope; full fix queued for Phase D). Dead `create_neptune_field_lines` stripped (~92 lines). 5 sun_traces stripped, radiation belt + FAC info marker position bugs fixed via `create_info_marker()` adoption |

Total: 6 files modified. Net change: +400 lines in `shell_configs.py`,
~-200 lines across the three visualization shell modules (Neptune
contributes ~-100 of that from the dead-function strip).

### 9.2 What Phase C4 delivers

| Component | Before C4 | After C4 |
|-----------|----------:|---------:|
| Bodies in SHELL_CONFIGS | 9 | 12 |
| Total sphere shell configs | 52 | 68 |
| Bodies in CUSTOM_SHELLS | 5 | 8 |
| Total custom entries | 11 | 21 |
| Bodies on old dispatch | 4 | 1 (Sun only) |
| `rotate_to_sunward()` users | 5 | 8 |
| `magnetic_tilt_deg` users | 0 | 1 (Uranus=60) |

### 9.3 What Phase C4 explicitly does NOT do

- Saturn pre-existing belt double-offset bug (audited in Section 4.8.0;
  fixed only if confirmed same pattern as Uranus, otherwise preserve
  and document for Phase D)
- Neptune ring info marker rotation mismatch (preserve, document for Phase D)
- Neptune `create_neptune_magnetic_poles` `sun_position` extension --
  bounded scope; 4 pole/axis traces stay in body frame, visible
  misalignment in heliocentric views accepted for C4 (Phase D fixes
  via Section 8.2 item 6)
- Earth/Jupiter `magnetic_tilt_deg` wiring (Phase D)
- `sun_position` ephemeris pass-through (Phase D)
- Sun unification (Phase D)
- Function-local import cleanup (Phase D)
- Dead sphere shell function archival (Phase D per-function decision)
- Animation path for shells (still skipped in heliocentric animation)

### 9.4 Risk register

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Neptune magnetosphere rotation order incorrect | Low | High (physics) | Section 6.6 documents ordering: internal tilt FIRST, then sunward. Smoke test asserts 180-deg rotation works |
| Uranus radiation belt visual change rejected by Mode 5 | Medium | Medium (cosmetic) | Section 8.3 question 1 flags for Tony review |
| Neptune magnetic pole misalignment visible in heliocentric Mode 5 | High | Low (cosmetic) | Section 6.6.2 documents the expected behavior; full fix queued for Phase D Section 8.2.6 |
| Neptune trace count mismatch (predicted 12) | Medium | Low | Section 6.14 smoke test detects; reconcile from source |
| Saturn ring tooltip rewrite introduces new errors | Low | Low | Side-by-side review during Section 4.11 |
| `magnetic_tilt_deg` rotation sign wrong for Voyager-2 convention | Low | Low (cosmetic) | Mode 5 visual review; one-character fix to flip sign |
| `create_info_marker()` mis-signature regressions in implementer | Low | High | Section 8.1.11 documents the helper contract; Saturn 4.6.2 provides reference usage |

---

## 10. Workflow Provenance

### 10.1 Authorship

- **Manifest author**: Anthropic's Claude Opus 4.7 (audit + draft +
  revision incorporating 4.6 review feedback)
- **Manifest input**: Tony Quintanilla (PROMPT_shell_consolidation_for_opus_v6.md,
  REPLY_c4_decisions_for_opus_4_7.md, HANDOFF_shell_consolidation_phase_c3.md)
- **Source audit**: Claude Opus 4.7, reading `/mnt/project/` files at
  paths `saturn_visualization_shells.py`, `uranus_visualization_shells.py`,
  `neptune_visualization_shells.py`, `orrery_rendering.py`,
  `planet_visualization.py`, `constants_new.py`,
  `planet_visualization_utilities.py`, `shell_configs.py`,
  `shared_utilities.py`
- **Pre-implementation review pass**: Anthropic's Claude Opus 4.6
  (May 17 2026) -- caught `create_info_marker()` signature drift,
  `CUSTOM_SHELLS` schema mismatch, smoke-test off-by-one, and
  contributed the magnetosphere shape symmetry analysis that
  confirmed X-axis rotation as the correct physics for
  `magnetic_tilt_deg`. Also recommended bounded scope for the Neptune
  magnetic poles helper. Three Claudes, one Tony, zero orchestration
  framework (cf. v3.22 protocol)
- **Implementation**: Anthropic's Claude Opus 4.6 (in a separate
  session, executing this revised manifest)
- **Integration and Mode 5 visual verification**: Tony Quintanilla
- **Mode 7 adversarial review**: Gemini (optional, for physics
  questions in Section 8.3 if Mode 5 surfaces concerns)

### 10.2 Module credit line

All 6 touched files get the credit line:

```python
# Module updated: May 2026 with Anthropic's Claude Opus 4.7
```

Insert near the top of each file's docstring (or as a top-level
comment if no docstring). Opus 4.7 credited for manifest authorship;
Opus 4.6 will use the same credit line during implementation since
this is one continuous Phase C4 effort.

### 10.3 Manifest version

This is the revised Phase C4 manifest (v2, May 17 2026). The revision
incorporates Opus 4.6 pre-implementation review feedback documented
in Section 10.1. Companion documents:

- `PROMPT_shell_consolidation_for_opus_v6.md` (Tony's prompt to Opus 4.7)
- `REPLY_c4_decisions_for_opus_4_7.md` (Tony's design decisions reply)
- `HANDOFF_shell_consolidation_phase_c3.md` (Phase C3 state input)
- `MANIFEST_shell_consolidation_phase_c4.md` (this document, v2)

Revision summary (v1 -> v2):
- `create_info_marker()` calls corrected to actual signature
  `(x, y, z, color, text, legendgroup, customdata=None)` across
  Uranus and Neptune sections (v1 invented a non-existent keyword API)
- `CUSTOM_SHELLS` entries for Uranus and Neptune rewritten to use
  the live schema `{'builder': 'module.function', 'tooltip': '...'}`
  with inline tooltip strings (v1 invented a different schema)
- Section 3.1 magnetic_tilt physics expanded with shape-symmetry
  analysis confirming X-axis-before-sunward as the only correct
  rotation; sign convention pinned (+60 deg about +X tilts +Z toward
  -Y)
- Neptune `create_neptune_magnetic_poles` bounded scope confirmed;
  full-fix moved to Phase D Section 8.2 item 6
- Section 2.6 smoke test uses off-center test position
- Sections 5.4 and 6.4 rewritten to mirror Saturn 4.4 "no source
  edit required" pattern (cloud layer migrates to SHELL_CONFIGS)
- Section 4.8.0 audit step added for Saturn radiation belt
  double-offset check
- Section 4.2 auto-generation script embedded inline (was stub
  referencing a C3 artifact)
- Sections 5.2 and 6.2 simplified to point at the 4.2 script with
  body-specific parameter blocks

After C4 completes, a corresponding `HANDOFF_shell_consolidation_phase_c4.md`
will be authored by Opus 4.6.

### 10.4 References

- Phase A architecture (config-driven dispatch): Mercury migration
- Phase B (Moon, Planet 9): SHELL_CONFIGS expansion
- Phase C1 (Pluto, Eris, Venus, Mars): rotate_to_sunward proven for
  4 bodies, ring helper still local to Saturn
- Phase C2 (Earth): hill sphere, Van Allen belts
- Phase C3 (Jupiter): first gas giant; ring helper promoted to
  `orrery_rendering.py`
- Phase C4 (Saturn, Uranus, Neptune): this manifest

---

*Paloma's Orrery | palomasorrery.com*
*Phase C4 -- the final migration phase before Phase D cleanup.*
*"Three Claudes, one Tony, zero orchestration framework." -- May 2026*

