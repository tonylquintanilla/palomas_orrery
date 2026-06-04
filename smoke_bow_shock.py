"""
smoke_bow_shock.py - Live-dispatch smoke test for the bow-shock build.

Run from a directory that contains ONLY live copies (a clean repo checkout or
the local repo dir) -- NOT the archive sandbox. Imports are BY NAME from the
script's own directory; the LOADED-FILE AUDIT printed first shows exactly which
copy of each module was imported -- read it to confirm no archived path crept in.

Resolves each magnetosphere builder via its CUSTOM_SHELLS 'builder' string (the
live path the app uses), calls it, and inspects the actual traces.

PASS per body requires ALL of:
  - exactly one 'X: Bow Shock' geometry trace (hoverinfo='skip', finite, non-empty)
  - exactly one cross info-marker in that legendgroup
  - NEST: bow-shock nose stands sunward of the magnetopause nose
          (near-axis comparison, so a tilted magnetosphere's off-axis flank
           does not count -- that is reported separately as an info note).
The nest check is the one that the earlier smoke test lacked; it would have
caught Mercury's Earth-scaled magnetosphere (sunward_distance 10 vs shock 1.96).
"""
import importlib, sys, os
import numpy as np
import shell_configs as sc

BODIES = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
CENTER = (1.0, 0.0, 0.0)
SUN = (0.0, 0.0, 0.0)
_sdir = np.array([SUN[i] - CENTER[i] for i in range(3)], float); _sdir /= np.linalg.norm(_sdir)
_cv = np.array(CENTER, float)

def _proj(tr):
    P = np.column_stack([np.array(tr.x, float), np.array(tr.y, float), np.array(tr.z, float)]) - _cv
    s = P @ _sdir
    perp = np.linalg.norm(P - np.outer(s, _sdir), axis=1)
    return s, perp

def audit_loaded_files():
    print("LOADED-FILE AUDIT (confirm these are the LIVE copies, not archived)")
    print("  run-dir on import path: %s" % (sys.path[0] or os.getcwd()))
    names = ['shell_configs', 'planet_visualization_utilities']
    names += ['%s_visualization_shells' % b.lower() for b in BODIES]
    for n in names:
        mod = sys.modules.get(n)
        print("    %-34s %s" % (n, getattr(mod, '__file__', '<not loaded>') if mod else '<not loaded>'))
    print("")

def main():
    for b in BODIES:
        importlib.import_module('%s_visualization_shells' % b.lower())
    audit_loaded_files()

    allpass = True
    for b in BODIES:
        mag = sc.CUSTOM_SHELLS.get(b, {}).get('magnetosphere')
        if not mag:
            print("[%-8s] NO magnetosphere entry" % b); allpass = False; continue
        modname, funcname = mag['builder'].rsplit('.', 1)
        traces = getattr(importlib.import_module(modname), funcname)(center_position=CENTER, sun_position=SUN)

        nm = "%s: Bow Shock" % b
        geo = [t for t in traces if getattr(t, 'name', None) == nm and getattr(t, 'hoverinfo', None) == 'skip']
        info = [t for t in traces if getattr(t, 'legendgroup', None) == nm
                and getattr(getattr(t, 'marker', None), 'symbol', None) == 'cross']
        magt = [t for t in traces if getattr(t, 'name', None) in (
                    "%s: Magnetosphere" % b, "%s: Induced Magnetosphere" % b)
                and getattr(t, 'hoverinfo', None) == 'skip']

        okg, oki = (len(geo) == 1), (len(info) == 1)
        fin, npts = False, 0
        nest_ok, shock_nose, mag_nose, mag_gmax = True, float('nan'), float('nan'), float('nan')
        if okg:
            s_sh, _ = _proj(geo[0])
            xs = np.array(geo[0].x, float)
            fin = len(xs) > 0 and np.all(np.isfinite(np.column_stack(
                [np.array(geo[0].x, float), np.array(geo[0].y, float), np.array(geo[0].z, float)])))
            npts = len(xs)
            shock_nose = float(s_sh.max())
            if magt:
                s_m, perp_m = _proj(magt[0])
                tau = 0.25 * shock_nose
                near = s_m[perp_m < tau]
                mag_nose = float(near.max()) if near.size else float(s_m.max())
                mag_gmax = float(s_m.max())
                nest_ok = shock_nose > mag_nose

        status = 'PASS' if (okg and oki and fin and nest_ok) else 'FAIL'
        if status == 'FAIL':
            allpass = False
        print("[%-8s] %-34s geo=%d info=%d pts=%d finite=%s nest=%s -> %s"
              % (b, funcname, len(geo), len(info), npts, fin, nest_ok, status))
        if okg and magt and not nest_ok:
            print("           NEST FAIL: shock nose=%.6f AU  magnetopause nose=%.6f AU (shock is INSIDE)" % (shock_nose, mag_nose))
        if okg and magt and mag_gmax > shock_nose and nest_ok:
            print("           note: magnetosphere off-axis flank reaches %.6f AU > shock nose %.6f AU"
                  " (tilted envelope; Mode-5 / Movement-2, not a nest failure)" % (mag_gmax, shock_nose))

    print("\nSMOKE RESULT:", "ALL PASS" if allpass else "FAILURES PRESENT")
    return 0 if allpass else 1

if __name__ == '__main__':
    sys.exit(main())
