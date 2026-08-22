"""
patch_L224_2_band_generator_and_builder.py

L-224 build, patch 1 of 2. PURELY ADDITIVE.

Adds the streamer band shape generator and the builder that wraps it.
Nothing calls either one when this patch lands, so it CANNOT change what
renders. Patch 2 throws the switch: registry move, constant rename,
labels, and the dead-function removal.

WHY THIS SHAPE OF PATCH
    The function everyone would reach for --
    solar_visualization_shells.create_sun_streamer_belt_shell -- is DEAD.
    It is defined once, imported once by planet_visualization.py, and
    never called. The sphere on screen comes from
    SHELL_CONFIGS['Sun']['streamer_belt'] through build_sphere_shell in
    orrery_rendering.py. So this is a dispatch move onto the live
    CUSTOM_SHELLS path, not a rewrite of that function. CUSTOM_SHELLS
    already carries four Sun entries, three of them built by
    solar_visualization_shells, so the pattern is proven.

WHAT IT ADDS  (two files, three anchored edits)
    planet_visualization_utilities.py
      1. STREAMER_BAND_DEFAULTS + create_streamer_band_shape(), appended
         at end of module, beside create_magnetosphere_shape and
         create_bow_shock_shape. Params dict in, body-frame point arrays
         out, caller places and scales -- the same contract those two
         use. Returns FIVE arrays rather than three, because the fade
         needs per-point alpha and size; documented at the function.
      2. Currency stamp.

    solar_visualization_shells.py
      3. create_streamer_band_shape added to the existing
         planet_visualization_utilities import, plus
         create_sun_streamer_band() appended at end of module, plus a
         currency stamp. One anchor for the import, one for the tail.

WHAT IT DOES NOT TOUCH
    shell_configs.py, palomas_orrery.py, constants_new.py,
    planet_visualization.py. No registry entry, no constant, no label,
    no deletion. All of that is patch 2.

MEASURED BEFORE DELIVERY, not asserted
    The generator was prototyped and run in the sandbox. At the defaults
    below it emits 4332 points spanning exactly 1.000 to 20.000 R_sun,
    with a largest radial gap of 0.21 R_sun (no ring artifacts), a
    z-extent of about +/-6.8 R_sun against a sphere's +/-20 (it is a
    band), and identical output across calls (seeded RandomState).

    The one non-negotiable from L-224 -- the stalk must never show an
    edge -- holds BY CONSTRUCTION, not by luck: alpha is computed from
    each point's OWN jittered radius rather than from its shell, so a
    point cannot be displaced past fade_radius while carrying alpha
    from inside it. Measured: 0 points beyond 19.7 R_sun with any alpha
    above zero, while the array itself runs on to 20.0. The terminus
    exists in the data and never on screen.

NOTE ON THE CUSP RADIUS
    The builder reads STREAMER_BELT_RADII, which is still 6.0 at this
    commit. Patch 2 renames it to HELMET_CUSP_RADII and sets it to 4.0,
    and the builder follows automatically. Nothing calls the builder
    until patch 2, so the interim value never renders.

HOW TO RUN
    Save into the repo ROOT, open in VS Code, click Run. Or:

        python patch_L224_2_band_generator_and_builder.py

    Then, as the pre-test protocol asks after any module edit:

        python -m py_compile planet_visualization_utilities.py
        python -m py_compile solar_visualization_shells.py

    Then commit, push, and archive this script to documentation/.
    The render will NOT change. That is the point of patch 1.

PERMANENT vs DISPOSABLE
    Disposable. The generator and builder are the permanent half.

Built on f1910ca11a7ff0677cbb9657a2c8cd5bf0287168 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written August 22, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

UTIL = "planet_visualization_utilities.py"
SHELLS = "solar_visualization_shells.py"

FP = {
    UTIL: "f5ce84b3e838fc3990c77dddbf31bac5",
    SHELLS: "1181179f3c8d39e110f5871d9fc2f9fd",
}

# Patch 1 is additive and must not touch the registries, the constants
# or the legacy import site. Fingerprinted so "untouched" is a check
# that can fail rather than an assertion in the header.
MUST_NOT_CHANGE = {
    "shell_configs.py": "5a456c12f14cf19f2a6f09d34c5ac0af",
    "palomas_orrery.py": "a22003eadeea738218b25b6617442d5e",
    "constants_new.py": "e2c2bf056551ff53410222224c10cb7b",
    "planet_visualization.py": "8088a87174dad4c0f31013bc288fd5ff",
}


# =====================================================================
# planet_visualization_utilities.py -- edit 1: the generator
# =====================================================================

U1_OLD = b"""    hover = '<br>'.join(lines)
    traces.append(go.Scatter3d(
        x=[tip[0]], y=[tip[1]], z=[tip[2]], mode='markers',
        marker=dict(size=5, color=color, symbol='cross',
                    line=dict(color='white', width=1)),
        name=legend, legendgroup=legend, showlegend=False,
        text=[hover], hovertemplate='%{text}<extra></extra>'))

    return traces
"""

U1_NEW = b'''    hover = '<br>'.join(lines)
    traces.append(go.Scatter3d(
        x=[tip[0]], y=[tip[1]], z=[tip[2]], mode='markers',
        marker=dict(size=5, color=color, symbol='cross',
                    line=dict(color='white', width=1)),
        name=legend, legendgroup=legend, showlegend=False,
        text=[hover], hovertemplate='%{text}<extra></extra>'))

    return traces


# =========================================================================
# Streamer band geometry (L-224)
# =========================================================================
# Shared shape generator, same contract as create_magnetosphere_shape and
# create_bow_shock_shape above: a params dict in, body-frame point arrays
# out, and the CALLER does placement, scaling and trace construction.
# Placed here rather than inline in solar_visualization_shells.py for the
# reason create_bow_shock_shape was extracted from four inline copies in
# June 2026 -- shaped geometry has one home.
#
# It returns FIVE arrays where its siblings return three. The extra two
# are per-point alpha and marker size, and they are the whole point: the
# streamer stalk has no outer edge, so it must dissolve rather than stop,
# and Plotly's marker.opacity is a scalar while marker.color and
# marker.size accept per-point arrays. Fading through a colour array is
# therefore the only way to draw an edgeless object in one trace.
#
# Units are SOLAR RADII throughout. The caller scales to AU.

STREAMER_BAND_DEFAULTS = {
    # --- radial structure -------------------------------------------
    'base_radius': 1.0,        # photosphere; the band starts at the surface
    'cusp_radius': 4.0,        # the pinch -- where closed loops open
    'fade_radius': 19.7,       # alpha reaches ZERO here (Alfven surface)
    'outer_radius': 20.0,      # last generated point, already invisible
    # --- the silhouette ---------------------------------------------
    'base_half_width_deg': 38.0,   # arcade footprint along the neutral line
    'cusp_half_width_deg': 9.0,    # the narrowest point
    'helmet_exponent': 1.7,        # >1 stays wide, then pinches near the cusp
    'stalk_taper': 0.45,           # further narrowing of the stalk, fractional
    'fade_exponent': 1.8,          # >1 dissolves; 1.0 smears
    # --- the warp (ONE configuration, near solar minimum) ------------
    'warp_amp_deg': 15.0,      # neutral-line tilt off the equator
    'warp_lobes': 2,           # two-lobe warp: the ballerina skirt
    # --- sampling ----------------------------------------------------
    'n_radial_helmet': 12,
    'n_radial_stalk': 30,
    'n_lon': 32,
    'n_lat': 5,
    'jitter': 0.42,            # fraction of local spacing; kills ring artifacts
    'seed': 20260822,          # seeded so the render is reproducible
    # --- appearance ---------------------------------------------------
    'max_alpha': 0.55,
    'base_marker_size': 3.2,
    'tip_marker_size': 1.4,
}


def create_streamer_band_shape(params=None):
    """Point cloud for a helmet-and-stalk streamer band (L-224).

    The streamer belt is not a shell and has no single radius. Below the
    cusp it is a closed magnetic arcade over the neutral line -- wide,
    dense, and bounded. Above the cusp it is an open stalk along the
    current sheet, which thins into the slow solar wind and has no outer
    edge at all. This generator draws both as ONE object whose character
    changes with radius, which is what they are.

    Returns
    -------
    (xs, ys, zs, alphas, sizes) : five equal-length lists
        Positions in SOLAR RADII in the body frame; per-point alpha in
        [0, max_alpha]; per-point marker size. Feed alphas into an rgba
        colour array and sizes into marker.size -- see
        solar_visualization_shells.create_sun_streamer_band.

    Two invariants worth knowing before changing anything here.

    NO VISIBLE EDGE, BY CONSTRUCTION. Alpha is evaluated at each point's
    OWN jittered radius, never at the radius of the shell it was sampled
    from. That is deliberate: with per-shell alpha, a point jittered
    outward past fade_radius would carry a non-zero alpha from inside it
    and draw a stray edge. Evaluating per point makes that impossible
    rather than unlikely. Points continue to outer_radius with alpha
    already at zero, so the array has a terminus and the screen does not.

    REPRODUCIBLE. Jitter comes from a seeded RandomState, not the global
    one, so two runs give byte-identical geometry. The sibling Oort
    builders in solar_visualization_shells.py use unseeded np.random and
    do re-roll every render; that is their existing behaviour, not a
    pattern to copy for anything a reference artifact will fingerprint.
    """
    import math

    p = dict(STREAMER_BAND_DEFAULTS)
    if params:
        p.update(params)

    base_r, cusp_r = float(p['base_radius']), float(p['cusp_radius'])
    fade_r, out_r = float(p['fade_radius']), float(p['outer_radius'])
    base_w = math.radians(float(p['base_half_width_deg']))
    cusp_w = math.radians(float(p['cusp_half_width_deg']))
    warp = math.radians(float(p['warp_amp_deg']))
    lobes = int(p['warp_lobes'])
    helm_e, fade_e = float(p['helmet_exponent']), float(p['fade_exponent'])
    taper, a_max = float(p['stalk_taper']), float(p['max_alpha'])
    s0, s1 = float(p['base_marker_size']), float(p['tip_marker_size'])
    jit = float(p['jitter'])
    n_h, n_s = int(p['n_radial_helmet']), int(p['n_radial_stalk'])
    rs = np.random.RandomState(int(p['seed']))

    span = max(1e-9, fade_r - cusp_r)

    def _fade_fraction(r):
        return min(1.0, max(0.0, (r - cusp_r) / span))

    def alpha_at(r):
        if r <= cusp_r:
            return a_max
        return a_max * (1.0 - _fade_fraction(r)) ** fade_e

    def size_at(r):
        if r <= cusp_r:
            return s0
        return s0 + (s1 - s0) * _fade_fraction(r)

    d_h = (cusp_r - base_r) / max(1, n_h - 1)
    d_s = (out_r - cusp_r) / max(1, n_s - 1)
    shells = ([(r, True) for r in np.linspace(base_r, cusp_r, n_h)] +
              [(r, False) for r in np.linspace(cusp_r, out_r, n_s)[1:]])

    xs, ys, zs, alphas, sizes = [], [], [], [], []
    for r_shell, in_helmet in shells:
        if in_helmet:
            t = 0.0 if cusp_r == base_r else (r_shell - base_r) / (cusp_r - base_r)
            t = min(1.0, max(0.0, t))
            half_w = cusp_w + (base_w - cusp_w) * (1.0 - t) ** helm_e
            n_lon, n_lat, step = int(p['n_lon']), int(p['n_lat']), d_h
        else:
            u = min(1.0, max(0.0,
                             (r_shell - cusp_r) / max(1e-9, out_r - cusp_r)))
            half_w = cusp_w * (1.0 - taper * u)
            # Density thins outward as well as alpha. Opacity alone reads
            # as a uniform sheet turned down; thinning reads as a sheet
            # coming apart, which is what actually happens.
            n_lon = max(10, int(round(int(p['n_lon']) * (1.0 - 0.70 * u))))
            n_lat = max(3, int(round(int(p['n_lat']) * (1.0 - 0.45 * u))))
            step = d_s
        lat_jit = half_w * jit / max(1, n_lat - 1)
        for lon in np.linspace(0.0, 2 * math.pi, n_lon, endpoint=False):
            # The neutral line is warped, not flat. This is the ballerina
            # skirt at its origin, in ONE configuration near solar minimum.
            lam0 = warp * math.sin(lobes * lon)
            for off in np.linspace(-half_w, half_w, n_lat):
                r_pt = min(out_r, max(base_r,
                                      r_shell + jit * step * rs.uniform(-1.0, 1.0)))
                lam = lam0 + off + lat_jit * rs.uniform(-1.0, 1.0)
                cos_lam = math.cos(lam)
                xs.append(r_pt * cos_lam * math.cos(lon))
                ys.append(r_pt * cos_lam * math.sin(lon))
                zs.append(r_pt * math.sin(lam))
                alphas.append(round(alpha_at(r_pt), 4))
                sizes.append(round(size_at(r_pt), 3))

    return xs, ys, zs, alphas, sizes
'''


U2_OLD = b"""Role: rendering
Domain: orrery
\"\"\"
"""

U2_NEW = b"""Module updated: August 2026 with Anthropic's Claude Opus 5 (L-224:
create_streamer_band_shape -- helmet-and-stalk band geometry for the
solar streamer belt, per-point alpha so the stalk has no visible edge)

Role: rendering
Domain: orrery
\"\"\"
"""


# =====================================================================
# solar_visualization_shells.py -- edits 3 and 4
# =====================================================================

S1_OLD = b"""from planet_visualization_utilities import (create_sphere_points, SOLAR_RADIUS_AU, CORE_AU, RADIATIVE_ZONE_AU, SUN_RADIUS_KM,
"""

S1_NEW = b"""from planet_visualization_utilities import (create_sphere_points, create_streamer_band_shape,
                                            STREAMER_BAND_DEFAULTS,
                                            SOLAR_RADIUS_AU, CORE_AU, RADIATIVE_ZONE_AU, SUN_RADIUS_KM,
"""


S2_OLD = b"""        'Sun: Galactic Tide Region',
        customdata='Galactic Tide Region'
    )
    return [shell_trace, info_trace]
"""

S2_NEW = b'''        'Sun: Galactic Tide Region',
        customdata='Galactic Tide Region'
    )
    return [shell_trace, info_trace]


# =========================================================================
# Streamer band -- CUSTOM_SHELLS builder (L-224)
# =========================================================================
# Wired via CUSTOM_SHELLS['Sun']['streamer_belt'] in patch 2. Until then
# nothing calls this and the render is unchanged.
#
# Replaces the sphere that SHELL_CONFIGS['Sun']['streamer_belt'] drew at
# a single radius. Two things were wrong with that sphere: helmet
# streamers form only over the magnetic neutral line, so a full sphere
# asserted them over the poles where coronal holes are instead; and its
# radius was a drawing choice with no boundary under it (L-210 withdrew
# the 4-6 R_sun range as unsourced).
#
# Source: constants_new.py HELMET_CUSP_RADII (STREAMER_BELT_RADII until
# patch 2) -- the cusp, not an outer edge.

def create_sun_streamer_band(center_position=(0, 0, 0)):
    """Streamer belt as one warped band: closed helmet, open stalk.

    Parameters
    ----------
    center_position : tuple
        Sun position. Accepted for interface uniformity with the
        CUSTOM_SHELLS dispatch contract; geometry translation is
        deferred here exactly as in the sibling Oort and tide builders.

    Returns a list of plotly traces, per the CUSTOM_SHELLS contract.

    One info marker only, per the single-info-marker convention, sitting
    just outside the band's edge at the cusp -- the pinch is where the
    eye goes and where the physics is. It is NOT at a pole: this is a
    band, and the poles are empty by design.
    """
    cusp_rs = float(STREAMER_BELT_RADII)   # patch 2: -> HELMET_CUSP_RADII = 4.0
    fade_rs = float(ALFVEN_SURFACE_RADII)  # dissolves across the Alfven surface

    params = {'cusp_radius': cusp_rs,
              'fade_radius': fade_rs,
              'outer_radius': fade_rs * 1.015}
    xs, ys, zs, alphas, sizes = create_streamer_band_shape(params)

    scale = SOLAR_RADIUS_AU
    x_au = [v * scale for v in xs]
    y_au = [v * scale for v in ys]
    z_au = [v * scale for v in zs]
    # Per-point rgba. marker.opacity is a scalar in Plotly; the colour
    # array is what lets one trace fade to nothing.
    colors = ['rgba(255, 200, 80, %.4f)' % a for a in alphas]

    # Figures interpolated from the constants, never typed, so the hover
    # cannot drift from what is drawn (L-179 / L-180 convention).
    def _km_au(r_solar):
        return (r_solar * SUN_RADIUS_KM, r_solar * SOLAR_RADIUS_AU)

    cusp_km, cusp_au = _km_au(cusp_rs)
    fade_km, fade_au = _km_au(fade_rs)
    fov_km, fov_au = _km_au(15.0)

    band_hover = (
        "One object with two regimes, not a shell with a radius.<br><br>"

        "CLOSED HELMET -- the dense, wide base. Magnetic arcades stand "
        "over the neutral line, closed at both ends. They reach no "
        f"higher than 2-4 R_sun, and the band pinches at {cusp_rs:.1f} "
        f"R_sun ({cusp_km:,.0f} km, {cusp_au:.6f} AU) where they open.<br>"
        "Source: Suess & Nerney (2004), Adv. Space Res. 33:668-675 -- "
        "stated there as established background, not measured by it, so "
        "the pinch is drawn soft rather than sharp.<br><br>"

        "OPEN STALK -- above the pinch. A thin sheet along the current "
        "sheet. It has NO outer edge: it thins into the slow solar wind, "
        "so this drawing dissolves instead of stopping. Nothing is drawn "
        f"past the Alfven surface at {fade_rs:.1f} R_sun ({fade_km:,.0f} "
        f"km, {fade_au:.6f} AU), where the corona becomes wind. Beyond "
        "that the sheet continues as the heliospheric current sheet, out "
        "to the heliopause.<br><br>"

        "THE VISIBLE EDGE. That a sharp brightness boundary exists is a "
        "coronagraph observation. What it DIVIDES is an interpretation: "
        "Suess & Nerney take it as reasonable to assume it separates "
        "fast coronal-hole wind from slow wind. Slow-wind origin is not "
        "settled, so the edge is drawn and its meaning is attributed.<br><br>"

        "DeForest, Howard & McComas (2014), ApJ 787:124 followed inbound "
        f"wave motion out to 15 R_sun ({fov_km:,.0f} km, {fov_au:.6f} "
        "AU). That is the coronagraph's field of view, not an extent -- "
        "a floor, not an edge.<br><br>"

        "THE WARP is drawn in ONE configuration, near solar minimum. The "
        "neutral line's tilt sweeps toward the poles across the 11-year "
        "cycle; this is the shape, not a measurement of today's.<br><br>"

        "Drawn as a visualization assumption where no measured boundary "
        "exists (L-224)."
    )

    band_trace = go.Scatter3d(
        x=x_au, y=y_au, z=z_au,
        mode='markers',
        marker=dict(size=sizes, color=colors, symbol='circle'),
        name='Sun: Streamer Belt',
        legendgroup='Sun: Streamer Belt',
        hoverinfo='skip',
        showlegend=True
    )

    # Info marker: at the cusp, at the longitude where the warp peaks,
    # stepped just outside the band edge so it is not buried in points.
    lon_i = math.pi / 4.0
    lat_i = math.radians(STREAMER_BAND_DEFAULTS['warp_amp_deg']
                         + STREAMER_BAND_DEFAULTS['cusp_half_width_deg'] + 6.0)
    r_i = cusp_rs * SOLAR_RADIUS_AU * 1.02
    info_trace = create_info_marker(
        r_i * math.cos(lat_i) * math.cos(lon_i),
        r_i * math.cos(lat_i) * math.sin(lon_i),
        r_i * math.sin(lat_i),
        'rgb(255, 200, 80)',
        f"Sun: Streamer Belt<br><br>{band_hover}",
        'Sun: Streamer Belt',
        customdata='Streamer Belt'
    )
    return [band_trace, info_trace]
'''


S3_OLD = b"""Role: rendering/shells
Domain: orrery

Module updated: May 2026 with Anthropic's Claude Opus 4.6
"""

S3_NEW = b"""Role: rendering/shells
Domain: orrery

Module updated: August 2026 with Anthropic's Claude Opus 5 (L-224:
create_sun_streamer_band -- the streamer belt as a warped helmet-and-
stalk band; the sphere it replaces is retired in patch 2)

Module updated: May 2026 with Anthropic's Claude Opus 4.6
"""


PLAN = [
    (UTIL, [("1  band generator appended", U1_OLD, U1_NEW),
            ("2  utilities currency stamp", U2_OLD, U2_NEW)]),
    (SHELLS, [("3  import create_streamer_band_shape", S1_OLD, S1_NEW),
              ("4  builder appended", S2_OLD, S2_NEW),
              ("5  shells currency stamp", S3_OLD, S3_NEW)]),
]


def fail(msg):
    print("ERROR: " + msg)
    sys.exit(1)


def main():
    # ---- read and fingerprint everything BEFORE writing anything -----
    originals = {}
    for path, _edits in PLAN:
        if not os.path.exists(path):
            fail("%s not found. Run this from the repo root." % path)
        with open(path, "rb") as f:
            originals[path] = f.read()
        fp = hashlib.md5(originals[path].replace(b"\r\n", b"\n")).hexdigest()
        if fp != FP[path]:
            print("ERROR: BASE MOVED on %s." % path)
            print("  expected fingerprint : " + FP[path])
            print("  this file            : " + fp)
            print("  Nothing was written to any file.")
            sys.exit(1)
        print("base ok: %-36s %6d bytes  %s"
              % (path, len(originals[path]),
                 "CRLF" if b"\r\n" in originals[path] else "LF"))

    # ---- ASCII gate on inserted text ---------------------------------
    for path, edits in PLAN:
        for label, _old, new in edits:
            bad = [b for b in new if b > 127]
            if bad:
                fail("edit %s would insert %d non-ASCII byte(s). Refusing."
                     % (label, len(bad)))
    print("note: all inserted text is ASCII")

    # ---- build every result in memory; write only if ALL succeed -----
    results = {}
    for path, edits in PLAN:
        data = originals[path]
        is_crlf = b"\r\n" in data
        for label, old, new in edits:
            o, n = old, new
            if is_crlf:
                o = o.replace(b"\n", b"\r\n")
                n = n.replace(b"\n", b"\r\n")
            count = data.count(o)
            if count != 1:
                print("ANCHOR FAIL on edit %s in %s: expected exactly 1 "
                      "match, found %d." % (label, path, count))
                print("  anchor began: %r" % o[:70])
                print("  Nothing was written to any file.")
                sys.exit(1)
            data = data.replace(o, n)
            print("ok   edit %s  (+%d bytes)" % (label, len(n) - len(o)))
        results[path] = data

    for path, data in results.items():
        with open(path, "wb") as f:
            f.write(data)
        print("wrote %s (%d bytes, was %d)"
              % (path, len(data), len(originals[path])))

    # ---- success carries evidence ------------------------------------
    print("")
    print("verification, read back from disk:")
    tally = [0]

    def check(desc, ok):
        if not ok:
            tally[0] += 1
        print("  %s  %s" % ("PASS" if ok else "FAIL", desc))

    with open(UTIL, "rb") as f:
        u = f.read().replace(b"\r\n", b"\n")
    with open(SHELLS, "rb") as f:
        s = f.read().replace(b"\r\n", b"\n")

    check("generator defined in utilities",
          b"\ndef create_streamer_band_shape(params=None):" in u)
    check("defaults table present",
          b"STREAMER_BAND_DEFAULTS = {" in u)
    check("alpha evaluated per point, not per shell",
          b"alphas.append(round(alpha_at(r_pt), 4))" in u)
    check("builder defined in shells",
          b"\ndef create_sun_streamer_band(center_position=(0, 0, 0)):" in s)
    check("builder imports the generator and the defaults",
          b"create_sphere_points, create_streamer_band_shape," in s
          and b"STREAMER_BAND_DEFAULTS," in s)
    check("builder returns the CUSTOM_SHELLS contract",
          s.count(b"return [band_trace, info_trace]") == 1)
    check("legend name is the renamed one",
          b"name='Sun: Streamer Belt'," in s)
    check("builder is defined exactly once and never called",
          s.count(b"create_sun_streamer_band(") == 1)
    for _p, _want in MUST_NOT_CHANGE.items():
        _got = "missing"
        if os.path.exists(_p):
            with open(_p, "rb") as _f:
                _got = hashlib.md5(
                    _f.read().replace(b"\r\n", b"\n")).hexdigest()
        check("untouched by patch 1: %s" % _p, _got == _want)
    check("old sphere function still present (patch 2 removes it)",
          b"def create_sun_streamer_belt_shell():" in s)
    check("both currency stamps added",
          b"(L-224:" in u and b"(L-224:" in s)
    failures = tally[0]

    # ---- compile both, which is a check that can fail ----------------
    import py_compile
    for path in (UTIL, SHELLS):
        try:
            py_compile.compile(path, doraise=True)
            print("  PASS  %s compiles" % path)
        except Exception as exc:
            print("  FAIL  %s does not compile: %s" % (path, exc))
            failures += 1

    if failures:
        print("")
        print("ERROR: %d check(s) failed AFTER writing. Restore both "
              "files from git and report this." % failures)
        sys.exit(1)

    print("")
    print("The render is UNCHANGED by design -- nothing calls the new")
    print("builder until patch 2. Commit, push, and archive this script")
    print("to documentation/.")


if __name__ == "__main__":
    main()
