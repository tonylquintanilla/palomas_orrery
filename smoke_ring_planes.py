"""
smoke_ring_planes.py - N15 ring-plane migration smoke test (live dispatch).

Verifies that each migrated ring / torus / belt builder actually routes its
geometry through orient_to_planet_pole(): it resolves each builder via its
CUSTOM_SHELLS string (the LIVE path, not the per-body function name), calls it,
fits a plane to the returned geometry, and checks that plane's normal against
the body's IAU pole direction (computed by orient_to_planet_pole itself, so a
builder that forgot the transform -- leaving its geometry in the body XY plane,
normal +Z -- or wired the wrong body string will FAIL).

WHAT THIS PROVES: the rings/torus/belts sit ON the planet's pole-derived plane.
WHAT IT DOES NOT PROVE: that the pole-derived plane matches the MOONS' plane.
A container cannot fetch Horizons, so ring-vs-moon agreement is the Mode-5
render gate (Despina/Galatea for Neptune, inner moons for Saturn). Same lesson
as the magnetosphere nest: the smoke is necessary, the render is sufficient.

Run from the repo root (or sandbox root) AFTER copying the edited files in:
    python smoke_ring_planes.py
Expect: "SMOKE RESULT: ALL PASS", exit 0. Each structure prints its fitted
plane-normal angle to the IAU pole; all should be ~0 deg (tolerance 2.0 deg,
slack for ring thickness and the radiation belts' z-undulation).

Module created: June 2026 with Anthropic's Claude Opus 4.8
"""

import os
import sys
import importlib

import numpy as np

# Make sure the run directory is importable (mirrors smoke_bow_shock.py).
RUN_DIR = os.path.dirname(os.path.abspath(__file__))
if RUN_DIR not in sys.path:
    sys.path.insert(0, RUN_DIR)

TOLERANCE_DEG = 2.0
MIN_GEOM_POINTS = 20  # geometry traces have many points; info markers have 1

# (body, shell_key). Uranus is the already-migrated regression anchor: it must
# still pass at ~0 deg, confirming the test methodology against a known-good.
TARGETS = [
    ('Jupiter', 'ring_system'),
    ('Saturn',  'ring_system'),
    ('Saturn',  'enceladus_plasma_torus'),
    ('Saturn',  'radiation_belts'),
    ('Neptune', 'ring_system'),
    ('Uranus',  'ring_system'),
]


def resolve_builder(builder_string):
    """'module.function' -> (module, callable). Also returns the module file."""
    module_name, func_name = builder_string.rsplit('.', 1)
    module = importlib.import_module(module_name)
    return module, getattr(module, func_name)


def fitted_plane_normal(traces):
    """Concatenate all geometry-trace points and return the best-fit plane
    normal (the least-variance singular direction)."""
    xs, ys, zs = [], [], []
    for tr in traces:
        tx = getattr(tr, 'x', None)
        if tx is None:
            continue
        ty = getattr(tr, 'y', None)
        tz = getattr(tr, 'z', None)
        if ty is None or tz is None:
            continue
        if len(tx) < MIN_GEOM_POINTS:
            continue  # skip single-point info markers
        xs.extend(list(tx))
        ys.extend(list(ty))
        zs.extend(list(tz))
    if len(xs) < MIN_GEOM_POINTS:
        return None, 0
    pts = np.vstack((np.asarray(xs, float),
                     np.asarray(ys, float),
                     np.asarray(zs, float))).T
    pts = pts - pts.mean(axis=0)
    _, _, vh = np.linalg.svd(pts, full_matrices=False)
    return vh[-1] / np.linalg.norm(vh[-1]), len(xs)


def expected_pole(body):
    """Pole direction in the ecliptic frame, via the SAME function the builders
    use -- so this is a true wiring check, not an independent reimplementation."""
    from idealized_orbits import orient_to_planet_pole
    ex, ey, ez = orient_to_planet_pole(np.array([0.0]), np.array([0.0]),
                                       np.array([1.0]), body)
    v = np.array([float(ex[0]), float(ey[0]), float(ez[0])])
    return v / np.linalg.norm(v)


def angle_between(u, v):
    # plane-normal sign is arbitrary, so compare with abs()
    return np.degrees(np.arccos(np.clip(abs(float(np.dot(u, v))), -1.0, 1.0)))


def main():
    from shell_configs import CUSTOM_SHELLS

    print("LOADED-FILE AUDIT (confirm these are the LIVE copies, not archived)")
    print(f"  run-dir on import path: {RUN_DIR}")
    seen = set()
    for body, key in TARGETS:
        builder_string = CUSTOM_SHELLS[body][key]['builder']
        module_name = builder_string.rsplit('.', 1)[0]
        if module_name in seen:
            continue
        seen.add(module_name)
        module, _ = resolve_builder(builder_string)
        print(f"    {module_name:34s} {getattr(module, '__file__', '?')}")
    print()

    all_pass = True
    for body, key in TARGETS:
        builder_string = CUSTOM_SHELLS[body][key]['builder']
        _, builder = resolve_builder(builder_string)
        try:
            traces = builder(center_position=(0, 0, 0))
        except TypeError:
            # a builder that also wants sun_position
            traces = builder(center_position=(0, 0, 0), sun_position=(0, 0, 0))

        normal, n_pts = fitted_plane_normal(traces)
        if normal is None:
            print(f"[{body:8s} {key:22s}] NO GEOMETRY POINTS FOUND -> FAIL")
            all_pass = False
            continue

        pole = expected_pole(body)
        off = angle_between(normal, pole)
        ok = off <= TOLERANCE_DEG
        all_pass = all_pass and ok
        tag = 'PASS' if ok else 'FAIL'
        note = '' if ok else f'  (exceeds {TOLERANCE_DEG} deg tol)'
        print(f"[{body:8s} {key:22s}] pts={n_pts:5d} "
              f"plane-normal vs IAU pole = {off:6.3f} deg -> {tag}{note}")

    print()
    print("SMOKE RESULT:", "ALL PASS" if all_pass else "FAIL")
    print("(Proves rings/torus/belts sit on the pole-derived plane. Ring-vs-MOON")
    print(" agreement is the Mode-5 render gate -- Horizons is unavailable here.)")
    sys.exit(0 if all_pass else 1)


if __name__ == '__main__':
    main()
