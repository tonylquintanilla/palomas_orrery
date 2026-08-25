"""
patch_L243_1_km_per_au.py

L-243. Retires every replicated copy of the AU conversion factor in the
orrery's live code. After this runs, 149597870.7 appears in exactly one
place a module can reach: KM_PER_AU in constants_new.py, sourced to
IAU 2012 Resolution B2.

Built on 13fdba49f515ccee4e107ec7c46d8b44c24fa773 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

RUN COMMAND:  python patch_L243_1_km_per_au.py
Save this file in the REPO ROOT (beside palomas_orrery.py), open it in
VS Code, click Run.

  Success: one "ok" line per edit, then "patch applied to 7 file(s)".
  Failure: a single ERROR / ANCHOR FAIL / COUNT FAIL line.
           NOTHING is written unless every edit in every file succeeded.

AFTER RUNNING -- the pre-test gate is NOT discharged by this script.
This is a data-content sweep: three of the seven modules build hover or
print strings from the factor. Per agentic-pre-test, run on your machine:
  1. py_compile on all seven (this script does that itself, see below)
  2. the xvfb / GUI run on a THROWAWAY copy
  3. a live-dispatch smoke -- open a plot whose hover shows a km distance
     (any object hover), a Sgr A* view (Schwarzschild radius line), and
     one spacecraft encounter marker.
The three sites that changed a rendered string are named in the report
this script prints at the end, so you know exactly what to look at.

WHAT IS PERMANENT: the code changes. This script is one-shot -- it guards
on fingerprints that stop existing the moment it succeeds -- and is
archived to documentation/ once run.

WHAT CHANGES

  palomas_orrery.py            2 literals -> KM_PER_AU (already imported
                               at line 259; pure replication)
  visualization_utils.py       import added; 3 literals
  shared_utilities.py          import added; 1 literal
  sgr_a_visualization_core.py  import added; 2 literals (hover)
  sgr_a_visualization_core_arcs.py
                               import added; 1 literal (hover)
  spacecraft_encounters.py     import added; schema comment corrected;
                               named shadow AU_KM DELETED; 14 uses
                               retargeted; 1 inline literal
  create_ephemeris_database.py import added; named shadow AU_TO_KM
                               DELETED; 1 use retargeted

Two named shadows, not one. The ledger row L-243 records AU_KM only;
AU_TO_KM in create_ephemeris_database.py line 133 was found while
building this patch and is function-local rather than module-level.
Update the row.

NOT TOUCHED, and deliberately:
  - constants_new.py itself.
  - The gallery's feature_renderers.js line 35. JavaScript cannot import
    a Python module; that copy is segment 2's surface.
  - visualization_utils.py's function at line 768, which takes KM_PER_AU
    as a PARAMETER. That is a constant threaded by argument, not a
    replicated value -- the caller passes the real one. Reported here
    because it is the kind of thing L-244's sweep should decide about,
    not because it is a violation.
"""

import hashlib
import os
import py_compile
import re
import shutil
import sys
import tempfile

IMPORT_LINE = "from constants_new import KM_PER_AU"

# --------------------------------------------------------------------------
# Edits, per file.
#   ("label", "anchor", old, new)   -> old must appear EXACTLY ONCE
#   ("label", "token",  pattern, replacement, expected_count)
# All anchors are whole source lines, verified unique at the base SHA.
# --------------------------------------------------------------------------

FILES = {

    "palomas_orrery.py": (
        "5e7d3a1f", [
            ("Orcus position print",
             "anchor",
             "print(f\"  -> Orcus position: ({x_orcus:.7f}, {y_orcus:.7f}, "
             "{z_orcus:.7f}) AU, r={r_orcus:.7f} AU (~{r_orcus * 149597870.7:.0f} km)\", flush=True)",
             "print(f\"  -> Orcus position: ({x_orcus:.7f}, {y_orcus:.7f}, "
             "{z_orcus:.7f}) AU, r={r_orcus:.7f} AU (~{r_orcus * KM_PER_AU:.0f} km)\", flush=True)"),
            ("Orcus radius print",
             "anchor",
             "print(f\"  -> Orcus: r={r_orcus:.7f} AU (~{r_orcus * 149597870.7:.0f} km)\", flush=True)",
             "print(f\"  -> Orcus: r={r_orcus:.7f} AU (~{r_orcus * KM_PER_AU:.0f} km)\", flush=True)"),
        ]),

    "visualization_utils.py": (
        "", [
            ("import",
             "anchor",
             "from celestial_coordinates import calculate_radec_for_position, format_radec_hover_component\n",
             "from celestial_coordinates import calculate_radec_for_position, format_radec_hover_component\n"
             + IMPORT_LINE + "\n"),
            ("zoom dtick km",
             "anchor",
             "        zoom_dtick_km = zoom_dtick * 149597870.7\n",
             "        zoom_dtick_km = zoom_dtick * KM_PER_AU\n"),
            ("distance display string",
             "anchor",
             "            dist_str = f\"{distance_from_center*149597870.7:.0f} km\"  # Convert AU to km\n",
             "            dist_str = f\"{distance_from_center*KM_PER_AU:.0f} km\"  # Convert AU to km\n"),
            ("distance parse back",
             "anchor",
             "                return float(dist_part.replace(' km', '').replace(',', '')) / 149597870.7\n",
             "                return float(dist_part.replace(' km', '').replace(',', '')) / KM_PER_AU\n"),
        ]),

    "shared_utilities.py": (
        "", [
            ("import",
             "anchor",
             "from orrery_rendering import create_info_marker\n",
             "from orrery_rendering import create_info_marker\n" + IMPORT_LINE + "\n"),
            ("dist_km",
             "anchor",
             "    dist_km = dist * 149597870.7\n",
             "    dist_km = dist * KM_PER_AU\n"),
        ]),

    "sgr_a_visualization_core.py": (
        "", [
            ("import",
             "anchor",
             "from save_utils import show_and_save\n",
             "from save_utils import show_and_save\n" + IMPORT_LINE + "\n"),
            ("Schwarzschild hover (labelled)",
             "anchor",
             "        f\"Schwarzschild Radius: {SCHWARZSCHILD_RADIUS_AU:.4f} AU "
             "({SCHWARZSCHILD_RADIUS_AU * 149597870.7:.0f} km)<br>\"\n",
             "        f\"Schwarzschild Radius: {SCHWARZSCHILD_RADIUS_AU:.4f} AU "
             "({SCHWARZSCHILD_RADIUS_AU * KM_PER_AU:.0f} km)<br>\"\n"),
            ("Schwarzschild hover (bare)",
             "anchor",
             "        f\"{SCHWARZSCHILD_RADIUS_AU:.4f} AU "
             "({SCHWARZSCHILD_RADIUS_AU * 149597870.7:.0f} km)<br><br>\"\n",
             "        f\"{SCHWARZSCHILD_RADIUS_AU:.4f} AU "
             "({SCHWARZSCHILD_RADIUS_AU * KM_PER_AU:.0f} km)<br><br>\"\n"),
        ]),

    "sgr_a_visualization_core_arcs.py": (
        "", [
            ("import",
             "anchor",
             "from plotly.subplots import make_subplots\n",
             "from plotly.subplots import make_subplots\n" + IMPORT_LINE + "\n"),
            ("Schwarzschild hover",
             "anchor",
             "        f\"Schwarzschild Radius: {SCHWARZSCHILD_RADIUS_AU:.4f} AU "
             "({SCHWARZSCHILD_RADIUS_AU * 149597870.7:.0f} km)<br>\"\n",
             "        f\"Schwarzschild Radius: {SCHWARZSCHILD_RADIUS_AU:.4f} AU "
             "({SCHWARZSCHILD_RADIUS_AU * KM_PER_AU:.0f} km)<br>\"\n"),
        ]),

    "spacecraft_encounters.py": (
        "", [
            ("import",
             "anchor",
             "from astroquery.jplhorizons import Horizons\n"
             "from astropy.time import Time\n",
             "from astroquery.jplhorizons import Horizons\n"
             "from astropy.time import Time\n" + IMPORT_LINE + "\n"),
            ("schema comment names the constant",
             "anchor",
             "#   dist_au:      Same in AU (km / 149597870.7)\n",
             "#   dist_au:      Same in AU (km / KM_PER_AU)\n"),
            ("delete named shadow AU_KM",
             "anchor",
             "\nAU_KM = 149597870.7  # 1 AU in km\n\n",
             "\n"),
            ("v_kms inline literal",
             "anchor",
             "    v_kms = v_au_day * 149597870.7 / 86400.0\n",
             "    v_kms = v_au_day * KM_PER_AU / 86400.0\n"),
            ("retarget AU_KM uses",
             "token",
             rb"\bAU_KM\b", b"KM_PER_AU", 14),
        ]),

    "create_ephemeris_database.py": (
        "", [
            ("import",
             "anchor",
             "from typing import Dict, Optional\n",
             "from typing import Dict, Optional\n" + IMPORT_LINE + "\n"),
            ("delete named shadow AU_TO_KM",
             "anchor",
             "    # Note: idealized_orbits.py uses AU, we need km\n"
             "    AU_TO_KM = 149597870.7\n",
             "    # Note: idealized_orbits.py uses AU, we need km.\n"
             "    # KM_PER_AU is imported from constants_new (L-243).\n"),
            ("retarget AU_TO_KM use",
             "token",
             rb"\bAU_TO_KM\b", b"KM_PER_AU", 1),
        ]),
}

# Sites whose output a person can SEE. Named so the smoke test knows
# where to look rather than being told "check everything".
RENDERED_SITES = [
    "visualization_utils.py   -- object hover distance string, and the "
    "parse that reads it back",
    "sgr_a_visualization_core.py / _arcs.py -- Schwarzschild radius in "
    "the Sgr A* hover",
    "spacecraft_encounters.py -- encounter relative velocity (km/s)",
]


def norm(b):
    return b.replace(b"\r\n", b"\n")


def main():
    if not os.path.exists("constants_new.py"):
        print("ERROR: run this from the repo root (constants_new.py not found here).")
        return 1

    # Guard: the destination constant must exist and be the expected value.
    src = open("constants_new.py", "rb").read().decode("utf-8", "replace")
    if "KM_PER_AU = 149597870.7" not in src:
        print("ERROR: constants_new.py does not define KM_PER_AU = 149597870.7.")
        print("       Nothing written.")
        return 1
    print("ok  constants_new.py defines KM_PER_AU = 149597870.7")

    staged = {}

    for path, (_unused_fp, edits) in FILES.items():
        if not os.path.exists(path):
            print("ERROR: %s not found. Nothing written." % path)
            return 1
        data = open(path, "rb").read()
        is_crlf = data.count(b"\r\n") > 0
        out = data

        for edit in edits:
            label, kind = edit[0], edit[1]

            if kind == "anchor":
                old, new = edit[2], edit[3]
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

            elif kind == "token":
                pattern, repl, expected = edit[2], edit[3], edit[4]
                found = len(re.findall(pattern, out))
                if found != expected:
                    print("COUNT FAIL [%s / %s]: expected %d, found %d"
                          % (path, label, expected, found))
                    print("  Nothing written.")
                    return 1
                out = re.sub(pattern, repl, out)

            print("ok  %-32s %s" % (path, label))

        # No copy of the factor may survive in this file.
        left = out.count(b"149597870")
        if left:
            print("ERROR [%s]: %d copy/copies of the factor still present "
                  "after edits. Nothing written." % (path, left))
            return 1

        staged[path] = (data, out, is_crlf)

    # All files understood. Write together.
    for path, (before, after, _crlf) in staged.items():
        open(path, "wb").write(after)

    print("")
    print("patch applied to %d file(s)" % len(staged))
    for path, (before, after, crlf) in staged.items():
        print("  %-34s %+6d bytes  (%s)"
              % (path, len(after) - len(before), "CRLF" if crlf else "LF"))

    # py_compile: the first leg of the pre-test, run here so it cannot be
    # skipped. It proves the files parse. It does NOT prove the edited
    # lines are the lines that run -- that is the smoke test's job.
    print("")
    print("py_compile:")
    failed = 0
    tmpdir = tempfile.mkdtemp(prefix="l243_pyc_")
    for path in staged:
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
        print("%d file(s) failed to compile. The edits ARE written -- "
              "revert from git before retrying." % failed)
        return 1

    print("")
    print("STILL OWED -- the pre-test is not discharged by this script.")
    print("Run the xvfb leg on a throwaway copy, then look at these three")
    print("rendered outputs, which are the strings this patch changed:")
    for s in RENDERED_SITES:
        print("  - %s" % s)
    print("")
    print("Then: python maintenance_run.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
