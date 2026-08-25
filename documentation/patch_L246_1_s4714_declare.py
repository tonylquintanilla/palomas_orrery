"""
patch_L246_1_s4714_declare.py

L-246, structural half only. Removes the two runtime overrides of
S_STAR_CATALOG['S4714']['a_au'] and puts the value in the catalog once,
declared as the drawing choice it is. The MEASURED value is not settled
by this patch and is routed to a dispatch.

Built on 1526a9cac5be3279bb62e6ddc467f9d59b9fb731 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

RUN COMMAND:  python patch_L246_1_s4714_declare.py
Save this file in the REPO ROOT, open it in VS Code, click Run.

  Success: one "ok" per edit, then "patch applied to 5 file(s)".
  Failure: ERROR / ANCHOR FAIL. Nothing is written unless every edit
           in every file succeeded.

AFTER RUNNING:
  python ledger_index.py
  python maintenance_run.py
  Then regenerate the Sgr A* views and check the two named at the end.

WHAT WAS WRONG
--------------
Three stores held one number. The catalog said 520.0. Two consumer
modules reached into the shared dict at import time and set it to
800.0:

  sgr_a_grand_tour.py line 39            a bare statement
  sgr_a_visualization_precession.py 33   a patch dict plus a function
                                         called on import

Because those are mutations of the shared dict rather than local
copies, the value a render used depended on which modules had been
imported. There is a live path that saw neither override:
sgr_a_visualization_animation.py imports the data module and the core
renderer and neither patcher, and calls get_star_data('S4714') at four
places.

So the same star was drawn two ways, and each view's text was correct
for its own value. The grand tour reports 8.2% of light speed at
periapsis; the animation's on-plot annotation says 10%. Both are right:
2*pi*sqrt(M/a * (1+e)/(1-e)) gives 24,693 km/s for a = 800 and 30,624
km/s for a = 520, using the module's own SGR_A_MASS_SOLAR = 4.154e6.
The first figure matches the grand tour's hover to the digit; the
second matches the comment the precession module wrote about the value
it was replacing.

WHAT CHANGES

  sgr_a_star_data.py        a_au 520.0 -> 800.0, with its declaration
                            below it in the registry's own labels
  sgr_a_grand_tour.py       override deleted; the stale "verify the
                            patch" comment corrected, since there is no
                            longer a patch to verify
  sgr_a_visualization_precession.py
                            override, patch dict and apply function
                            deleted
  sgr_a_visualization_animation.py
                            "10% light speed" -> "8% light speed". The
                            annotation was true of 520 and is false of
                            800 -- the correction has to travel to the
                            prose or this patch just moves the
                            disagreement
  LEDGER_CONSOLIDATED.md    L-246 opened

WHAT THIS PATCH DOES NOT DECIDE
-------------------------------
Whether 800.0 is right. It is not sourced, and it does not close: with
SGR_A_MASS_SOLAR = 4.154e6, Kepler's third law gives an 11.1 year
period for a = 800 against the 12.0 years stored beside it, and a
12.0 year period needs a = 842 AU with periapsis at 12.6 rather than
12.0. 800 was chosen to land periapsis on a round 12. That is a
question for a source read, not for a patch, and L-246 carries it.

The render does not change. Every path now draws what the grand tour
and the precession view already drew.
"""

import hashlib
import os
import py_compile
import shutil
import sys
import tempfile

DECLARATION = """        'a_au': 800.0,
        # Note: DECLARED DRAWING VALUE, not a measurement. 800.0 is chosen
        #       so that periapsis = a * (1 - e) = 12.0 AU, which is the
        #       figure this project draws and labels. Nobody has sourced
        #       800.0 itself.
        # Calculation: with SGR_A_MASS_SOLAR = 4.154e6, Kepler's third law
        #              gives P = 11.1 yr for a = 800, against the 12.0 yr
        #              stored below. A 12.0 yr period needs a = 842 AU,
        #              which puts periapsis at 12.6. So 800 satisfies the
        #              periapsis label and not the period.
        # Review-note: 520.0 was stored here until 2026-08-25, and two
        #              modules overwrote it to 800.0 at import time, so
        #              which value a render used depended on import order.
        #              The grand tour and precession views drew 800 and
        #              8.2% c; the animation drew 520 and 10.2% c, for the
        #              same star. Both overrides are gone and the value
        #              lives here.
        # Ref: L-246 -- the measured value is unverified and routed to a
        #      dispatch against Peissker et al. (2020).
"""

POINTER = """# S4714's semi-major axis lives in sgr_a_star_data.S_STAR_CATALOG with its
# declaration beside it (L-246). The runtime override that used to sit here
# is gone: it mutated the shared catalog, so the value another module saw
# depended on import order.
"""

BLOCK_246 = """#### [L-246] S4714's semi-major axis was three values in three stores
<!-- L:246 status:OPEN upd:2026-08-25 section:A flag: rice:3/4/85/2 -->
- **Found 2026-08-25 by Mode 5.** Tony sent a Grand Tour screenshot to
  confirm an unrelated import. The hover read `Semi-major axis: 800 AU`
  and the catalog read 520.0.
- **Three stores, one number.** `sgr_a_star_data.py` held
  `'a_au': 520.0`. Two consumer modules reached into the SHARED dict at
  import time and set it to 800.0 -- `sgr_a_grand_tour.py` line 39 as a
  bare statement, and `sgr_a_visualization_precession.py` line 33 as a
  patch dict plus a function called on import. The second one states its
  own reasoning: "We apply this patch at runtime so the original data
  module stays clean." The intent was to protect the source of truth and
  the effect was to make it depend on import order.
- **A live path saw neither override.**
  `sgr_a_visualization_animation.py` imports the data module and the core
  renderer and no patcher, and calls `get_star_data('S4714')` at four
  places. So the same star was drawn two ways.
- **And each view's PROSE was correct for its own value.** The grand
  tour hover reports 8.2% of light speed at periapsis; the animation's
  on-plot annotation says 10%. Both are right:
  `2*pi*sqrt(M/a * (1+e)/(1-e))` with the module's own
  `SGR_A_MASS_SOLAR = 4.154e6` gives 24,693 km/s for a = 800 and 30,624
  km/s for a = 520. The first matches the hover to the digit.
- **The scanner cannot see any of it.** It scores literal assignments. A
  runtime dict mutation is not one, and a value inside a dict literal is
  not a scored unit either -- the same reachability class as L-190's
  ring and belt numbers.
- **STRUCTURAL HALF CLOSED 2026-08-25** by
  `patch_L246_1_s4714_declare.py`: both overrides deleted, the value in
  the catalog once, declared with `# Note:`, `# Calculation:` and
  `# Review-note:` legs, and the animation's "10% light speed"
  annotation corrected to 8%. The render does not change; every path now
  draws what the grand tour already drew.
**Gap:** the MEASURED value. 800.0 is not sourced and does not close.
With `SGR_A_MASS_SOLAR = 4.154e6`, Kepler's third law gives P = 11.1 yr
for a = 800 against the 12.0 yr stored beside it; a 12.0 yr period needs
a = 842 AU, putting periapsis at 12.6 rather than 12.0. So 800 was
chosen to land periapsis on a round 12 rather than to satisfy the orbit.
`S4711` has the same shape -- a = 572 with a stored 7.6 yr period, where
Kepler gives 6.7. Route both to a dispatch against Peissker et al.
(2020), which the module cites in a COMMENT
(`sgr_a_grand_tour.py` line 122) in a different file from the data.
- **Note:** RICE 3/4/85/2 -> 5.1 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect, and whether the S-star
  catalog joins the worksheet corpus at all -- today no entry in it
  carries a `# Source:` line.
**Ref:** `sgr_a_star_data.py` S_STAR_CATALOG; `sgr_a_grand_tour.py`;
`sgr_a_visualization_precession.py`; `sgr_a_visualization_animation.py`;
L-190 (values the scanner cannot reach); L-240 (measured vs declared);
The Artifact Bounds the Audit.

"""

FILES = {

    "sgr_a_star_data.py": (
        "f21e78b39ba53ba4b7617b31a3c270f6", [
            ("declare a_au in the catalog",
             "        'a_au': 520.0,\n",
             DECLARATION),
        ]),

    "sgr_a_grand_tour.py": (
        "7beb765c288ffb4268ecfb9dc261f20f", [
            ("delete runtime override",
             "# =============================================================================\n"
             "# ACCURACY PATCH (S4714)\n"
             "# =============================================================================\n"
             "# Adjusting semi-major axis to match literature velocity (~8% c at periapsis)\n"
             "# This gives periapsis = 12 AU (matching Peissker et al. 2020)\n"
             "data.S_STAR_CATALOG['S4714']['a_au'] = 800.0\n",
             POINTER),
            ("correct the stale 'verify the patch' comment",
             "    # Verify S4714 patch\n",
             "    # Report S4714's drawn geometry from the catalog (L-246).\n"),
        ]),

    "sgr_a_visualization_precession.py": (
        "152f59f1b67f1b92cb433ac153617cd6", [
            ("delete patch dict, function and import-time call",
             "# =============================================================================\n"
             "# ACCURACY PATCH - S4714\n"
             "# =============================================================================\n"
             "# Issue: Original a=520 AU, e=0.985 gave periapsis ~7.8 AU and velocity 10.2% c\n"
             "# Fix: Raise semi-major axis to 800 AU to match literature:\n"
             "#      - Periapsis: ~12 AU (matches Peissker et al. 2020)\n"
             "#      - Velocity: ~8% c (matches literature value)\n"
             "#\n"
             "# We apply this patch at runtime so the original data module stays clean.\n"
             "\n"
             "S4714_ACCURACY_PATCH = {\n"
             "    'a_au': 800.0,  # Was 520.0\n"
             "    # This gives periapsis = 800 * (1 - 0.985) = 12 AU\n"
             "    # And velocity ~24,000 km/s = 8% c\n"
             "}\n"
             "\n"
             "def apply_accuracy_patches():\n"
             "    \"\"\"Apply literature-based corrections to orbital elements.\"\"\"\n"
             "    # Patch S4714\n"
             "    for key, value in S4714_ACCURACY_PATCH.items():\n"
             "        data.S_STAR_CATALOG['S4714'][key] = value\n"
             "    \n"
             "    # Verify the patch\n"
             "    star = data.get_star_data('S4714')\n"
             "    peri = data.calculate_periapsis_au(star['a_au'], star['e'])\n"
             "    v_peri = data.calculate_periapsis_velocity(star['a_au'], star['e'])\n"
             "    print(f\"S4714 patched: periapsis = {peri:.1f} AU, velocity = {data.format_velocity(v_peri)}\")\n"
             "\n"
             "# Apply patches on import\n"
             "apply_accuracy_patches()\n",
             POINTER),
        ]),

    "sgr_a_visualization_animation.py": (
        "351d52d99503b9300050401e89ded817", [
            ("correct the speed claim the override made false",
             "        text=\"Watch S4714 (red): hangs at apoapsis, then SNAPS through "
             "periapsis at 10% light speed!\",\n",
             "        text=\"Watch S4714 (red): hangs at apoapsis, then SNAPS through "
             "periapsis at 8% light speed!\",\n"),
        ]),

    "LEDGER_CONSOLIDATED.md": (
        "de0f848b16c9b6b9a95b95051d6a10f3", [
            ("open L-246",
             "\n## PENDING ACTION (Tony-side)\n",
             "\n" + BLOCK_246 + "## PENDING ACTION (Tony-side)\n"),
        ]),
}

RENDERED = [
    "sgr_a_grand_tour.py  -- unchanged: still 800 AU, periapsis 12.0 AU, "
    "24,693 km/s, 8.2% c",
    "sgr_a_visualization_animation.py -- CHANGES: S4714 now drawn at 800 "
    "instead of 520, so its periapsis loop tightens and the on-plot text "
    "reads 8% rather than 10%",
]


def main():
    if not os.path.exists("constants_new.py"):
        print("ERROR: run this from the repo root (constants_new.py not found here).")
        return 1

    staged = {}
    for path, (base_fp, edits) in FILES.items():
        if not os.path.exists(path):
            print("ERROR: %s not found. Nothing written." % path)
            return 1
        data = open(path, "rb").read()
        fp = hashlib.md5(data.replace(b"\r\n", b"\n")).hexdigest()
        if fp != base_fp:
            print("ERROR: base moved for %s." % path)
            print("  expected content-md5 %s" % base_fp)
            print("  found                %s" % fp)
            print("  Nothing written.")
            return 1
        is_crlf = data.count(b"\r\n") > 0
        print("base ok  %-36s (%s)" % (path, "CRLF" if is_crlf else "LF"))

        out = data
        for label, old, new in edits:
            try:
                new.encode("ascii")
            except UnicodeEncodeError as e:
                print("ERROR: non-ASCII in replacement for %s / %s: %s"
                      % (path, label, e))
                return 1
            o, n = old.encode("ascii"), new.encode("ascii")
            if is_crlf:
                o = o.replace(b"\n", b"\r\n")
                n = n.replace(b"\n", b"\r\n")
            c = out.count(o)
            if c != 1:
                print("ANCHOR FAIL [%s / %s]: expected 1 match, got %d"
                      % (path, label, c))
                print("  anchor: %r" % old[:78])
                print("  Nothing written.")
                return 1
            out = out.replace(o, n)
            print("ok  %-36s %s" % (path, label))

        staged[path] = (data, out, is_crlf)

    # No runtime mutation of the catalog may survive.
    for path, (_b, after, _c) in staged.items():
        if path.endswith(".py") and b"S_STAR_CATALOG['S4714']" in after:
            print("ERROR [%s]: a catalog override survives. Nothing written." % path)
            return 1

    for path, (_b, after, _c) in staged.items():
        open(path, "wb").write(after)

    print("")
    print("patch applied to %d file(s)" % len(staged))
    for path, (before, after, crlf) in staged.items():
        print("  %-38s %+6d bytes  (%s)"
              % (path, len(after) - len(before), "CRLF" if crlf else "LF"))

    print("")
    print("py_compile:")
    failed = 0
    tmpdir = tempfile.mkdtemp(prefix="l246_pyc_")
    for path in staged:
        if not path.endswith(".py"):
            continue
        try:
            py_compile.compile(
                path,
                cfile=os.path.join(tmpdir, os.path.basename(path) + "c"),
                doraise=True)
            print("  ok    %s" % path)
        except py_compile.PyCompileError as e:
            print("  FAIL  %s: %s" % (path, e))
            failed += 1
    shutil.rmtree(tmpdir, ignore_errors=True)
    if failed:
        print("")
        print("%d file(s) failed to compile. The edits ARE written -- revert "
              "from git before retrying." % failed)
        return 1

    print("")
    print("NEXT, in order:")
    print("  1. python ledger_index.py")
    print("  2. python maintenance_run.py")
    print("  3. Regenerate the Sgr A* views and look at these:")
    for s in RENDERED:
        print("       - %s" % s)
    return 0


if __name__ == "__main__":
    sys.exit(main())
