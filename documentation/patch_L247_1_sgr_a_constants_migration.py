"""
patch_L247_1_sgr_a_constants_migration.py

L-247. Moves the Sagittarius A* physical constants out of
sgr_a_star_data.py and into constants_new.py, deletes the two nothing
reads, and sweeps the literals that were restating the migrated values
in prose and in arithmetic.

Built on c943c83246f937bdbe0db82c41a99fc4b21330b4 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

RUN COMMAND:  python patch_L247_1_sgr_a_constants_migration.py
Save this file in the REPO ROOT, open it in VS Code, click Run.

  Success: one "ok" per edit, then "patch applied to 6 file(s)".
  Failure: ERROR / ANCHOR FAIL / COUNT FAIL. Nothing written.

AFTER RUNNING:
  python ledger_index.py
  python maintenance_run.py
  Then regenerate the Sgr A* views and hover the black hole marker.

NO RENDERED VALUE CHANGES. Two hover strings stop being typed and start
being derived, and both produce the same characters they did before:
"4.154 million solar masses" and "26,670 light-years".

WHAT MOVES (7), and under what name

  G_CONST            -> GRAVITATIONAL_CONSTANT_SI
  SPEED_OF_LIGHT     -> SPEED_OF_LIGHT_M_S, DERIVED from the store's
                        existing SPEED_OF_LIGHT_KM_S rather than carried
                        as a second literal
  SOLAR_MASS_KG      -> same name
  AU_TO_METERS       -> M_PER_AU, derived from KM_PER_AU, matching the
                        store's KM_PER_AU naming rather than the old
                        AU_TO_ direction
  PARSEC_TO_AU       -> same name
  SGR_A_MASS_SOLAR   -> same name
  SGR_A_DISTANCE_LY  -> same name

sgr_a_star_data.py imports all seven. That is a re-export, not an
alias: one binding, one name, one value, so every module that reads
`data.SGR_A_MASS_SOLAR` keeps working with nothing to keep in step.

WHAT IS DELETED (2)

  YEAR_TO_SECONDS    defined, never read anywhere in the tree
  SGR_A_DISTANCE_PC  defined, never read, and 8178 appears nowhere else

Deleting rather than migrating is deliberate. A value nothing draws does
not belong in the file the scanner treats as the measurement layer --
moving it there grows the audit denominator for no consumer, which is
what The Artifact Bounds the Audit exists to stop.

WHAT IS SWEPT (7 literal sites)

  exoplanet_coordinates.py   206265 x3 in arithmetic, x1 in a docstring
                             -> PARSEC_TO_AU
  sgr_a_visualization_core.py and _arcs.py
                             "4.154 million solar masses" -> derived
                             "26,670 light-years"        -> derived

Those four literals are why PARSEC_TO_AU and SGR_A_DISTANCE_LY are
migrated rather than deleted with the other two. The NAME was dead in
sgr_a_star_data.py; the VALUE was alive in four other places, spelled
out. Deleting the name and leaving the number would have removed the
sourced copy and kept the unsourced ones.

FIX IN PASSING

sgr_a_star_data.py carries three non-ASCII bytes -- an em dash in a
comment at line 155. The encoding convention covers prose, this patch
already fingerprints the file, and a sweep for one character would never
be scheduled on its own. It is corrected here. Every line this patch
INSERTS is ASCII by gate; that em dash is pre-existing and is reported
separately in the run output.

NOT DONE, AND ROUTED INSTEAD

Building this found three more unnamed physical constants in
exoplanet_coordinates.py: 3.26156 (light-years per parsec), 4.74 (the
AU/yr to km/s factor, which is KM_PER_AU divided by seconds per Julian
year), and the seconds-per-year expression duplicated in
energy_imbalance.py line 65. None was in the ruling that authorised this
patch, so none is touched. They go to L-244, which is the sweep for this
class.
"""

import hashlib
import os
import py_compile
import re
import shutil
import sys
import tempfile

NEW_CONSTANTS = """
# ============================================================
# SAGITTARIUS A* AND GALACTIC-SCALE CONSTANTS
# Migrated 2026-08-25 from sgr_a_star_data.py under L-247. The values
# are unchanged; what changed is that there is now one of each.
# ============================================================

GRAVITATIONAL_CONSTANT_SI = 6.67430e-11
# Note: units m^3 kg^-1 s^-2.
# Review-note: no source line travelled with this value from
#              sgr_a_star_data.py, where it carried only a units
#              comment. Routed to L-247 for a dispatch. Not cited here,
#              because a citation written to fill the gap would be a
#              provenance claim nobody checked.

SPEED_OF_LIGHT_M_S = SPEED_OF_LIGHT_KM_S * 1000
# Derived: the store already holds this quantity in km/s. Carrying a
#          second literal would put two spellings of one exact value in
#          one file, which is the failure L-247 exists to close.

SOLAR_MASS_KG = 1.989e30
# Review-note: no source line travelled with this value. Routed to
#              L-247.

M_PER_AU = KM_PER_AU * 1000
# Derived: 1 AU in metres, from the IAU 2012 definition above.
# Note: replaces AU_TO_METERS in sgr_a_star_data.py, renamed to match
#       this file's KM_PER_AU direction rather than the AU_TO_ one.

PARSEC_TO_AU = 206265.0
# Review-note: no source line travelled with this value. It is the
#              small-angle arcseconds-per-radian figure and is used as a
#              bare literal in exoplanet_coordinates.py, swept to this
#              name by L-247. Routed for a dispatch.

SGR_A_MASS_SOLAR = 4.154e6
# Source: GRAVITY Collaboration 2019
# Review-note: the attribution above travelled with the value as an
#              inline comment and is carried here verbatim. It names no
#              paper, DOI or table, so it is a lead rather than a
#              citation. Routed to L-247.

SGR_A_DISTANCE_LY = 26670.0
# Review-note: no source line travelled with this value. It was restated
#              as prose in two hover strings, which now derive from it.
#              Routed to L-247.

"""

STAR_DATA_OLD = """G_CONST = 6.67430e-11           # Gravitational constant (m^3 kg^-1 s^-2)
SPEED_OF_LIGHT = 299792458.0    # Speed of light (m/s)
SOLAR_MASS_KG = 1.989e30        # Solar mass (kg)

# AU conversion \u2014 imported from constants_new.py for single source of truth.
# IAU 2012 defined value: 1 AU = 149,597,870.7 km exactly.
# Previous local values (1.496e8, 1.496e11) were off by ~2,129 km per AU.
# Source: IAU Resolution B2 (2012)
# Ref: https://www.iau.org/static/resolutions/IAU2012_English.pdf
# Verified: April 15, 2026
AU_TO_METERS = KM_PER_AU * 1000 # 1 AU in meters (1.495978707e11)

PARSEC_TO_AU = 206265.0         # 1 parsec in AU
YEAR_TO_SECONDS = 365.25 * 24 * 3600  # Seconds per Julian year
"""

STAR_DATA_NEW = """# Every physical constant this module used to define now lives in
# constants_new.py and is imported at the top of this file (L-247,
# 2026-08-25). YEAR_TO_SECONDS and SGR_A_DISTANCE_PC were deleted rather
# than migrated: nothing in the tree read either one.
"""

SGR_OLD = """SGR_A_MASS_SOLAR = 4.154e6      # Solar masses (GRAVITY Collaboration 2019)
SGR_A_MASS_KG = SGR_A_MASS_SOLAR * SOLAR_MASS_KG
SGR_A_DISTANCE_PC = 8178.0      # Distance from Earth (parsecs)
SGR_A_DISTANCE_LY = 26670.0     # Distance from Earth (light years)
"""

SGR_NEW = """SGR_A_MASS_KG = SGR_A_MASS_SOLAR * SOLAR_MASS_KG
"""

BLOCK_247 = """#### [L-247] Sgr A* constants migrated to the single source of truth
<!-- L:247 status:OPEN upd:2026-08-25 section:A flag: rice:3/3/90/2 -->
- **Tony's ruling, 2026-08-25:** conversion factors and physical
  constants live in `constants_new.py`, carry a source, and are called
  rather than replicated. This is that ruling applied to
  `sgr_a_star_data.py`, which held nine of them.
- **Seven migrated, two deleted.** `GRAVITATIONAL_CONSTANT_SI`,
  `SPEED_OF_LIGHT_M_S` (derived from the store's existing
  `SPEED_OF_LIGHT_KM_S` rather than carried as a second literal),
  `SOLAR_MASS_KG`, `M_PER_AU` (derived from `KM_PER_AU`),
  `PARSEC_TO_AU`, `SGR_A_MASS_SOLAR` and `SGR_A_DISTANCE_LY` moved.
  `YEAR_TO_SECONDS` and `SGR_A_DISTANCE_PC` were DELETED: each appeared
  exactly once in the whole tree, on its own definition line.
- **Deleting a dead constant rather than migrating it is the point.**
  Moving one into the file the scanner treats as the measurement layer
  grows the audit denominator for a value the orrery never draws --
  which is what The Artifact Bounds the Audit exists to stop.
- **Two of the four "dead" names were not dead in VALUE.** `206265`
  appears three times in arithmetic and once in a docstring in
  `exoplanet_coordinates.py`; `26,670 light-years` and `4.154 million
  solar masses` are typed into hover strings in
  `sgr_a_visualization_core.py` and `_arcs.py`. So the name was dead
  where the number was alive somewhere else, spelled out. Deleting the
  name and leaving the literals would have removed the sourced copy and
  kept the unsourced ones. All seven literal sites are swept; the two
  hover strings now derive and render the same characters.
- **What did NOT travel, and is stated rather than invented.** Only one
  of the seven carried any attribution at all -- `SGR_A_MASS_SOLAR`, as
  the inline comment "(GRAVITY Collaboration 2019)", which names no
  paper, DOI or table. It is carried verbatim as a lead. The other six
  arrive carrying a `# Review-note:` saying plainly that no source came
  with them. None was given a citation to fill the gap.
**Gap:** the dispatch. Seven values, six with no source and one with a
lead. This is the verification loop applied to a family that was
previously invisible to it, because the values sat in a module the
worksheet builder does not reach.
- **Note:** RICE 3/3/90/2 -> 4.1 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** L-243 (the AU factor); L-244 (the class sweep -- three more
unnamed constants found while building this: 3.26156 light-years per
parsec and 4.74 AU/yr to km/s in `exoplanet_coordinates.py`, and the
seconds-per-year expression in `energy_imbalance.py` line 65);
L-246 (S4714); No Shadow Constants [CRITICAL].

"""

FILES = {

    "constants_new.py": (
        "1a36adc0164e79b03d711763182f9d9c", [
            ("append the migrated constants",
             "anchor",
             "    'T': {0: 1300, 9: 600},       # T0 to T9 (optional)\n}\n",
             "    'T': {0: 1300, 9: 600},       # T0 to T9 (optional)\n}\n"
             + NEW_CONSTANTS),
        ]),

    "sgr_a_star_data.py": (
        "6b5c4c38c000828924de8597abc6bc45", [
            ("import the seven",
             "anchor",
             "from constants_new import KM_PER_AU, SPEED_OF_LIGHT_KM_S\n",
             "from constants_new import (\n"
             "    KM_PER_AU, SPEED_OF_LIGHT_KM_S,\n"
             "    GRAVITATIONAL_CONSTANT_SI, SPEED_OF_LIGHT_M_S, SOLAR_MASS_KG,\n"
             "    M_PER_AU, PARSEC_TO_AU, SGR_A_MASS_SOLAR, SGR_A_DISTANCE_LY,\n"
             ")\n"),
            ("remove the local physical constants",
             "anchor", STAR_DATA_OLD, STAR_DATA_NEW),
            ("remove the two dead Sgr A* constants",
             "anchor", SGR_OLD, SGR_NEW),
            ("retarget G_CONST",
             "token", rb"\bG_CONST\b", b"GRAVITATIONAL_CONSTANT_SI", 2),
            ("retarget SPEED_OF_LIGHT",
             "token", rb"\bSPEED_OF_LIGHT\b", b"SPEED_OF_LIGHT_M_S", 1),
            ("retarget AU_TO_METERS",
             "token", rb"\bAU_TO_METERS\b", b"M_PER_AU", 3),
        ]),

    "sgr_a_visualization_core.py": (
        "f37d28a0e6c52902f1c522c5517a5a0f", [
            ("derive the two typed figures",
             "anchor",
             "        f\"Mass: 4.154 million solar masses<br>\"\n",
             "        f\"Mass: {SGR_A_MASS_SOLAR / 1e6:.3f} million solar masses<br>\"\n"),
            ("derive the distance",
             "anchor",
             "        f\"Distance from Earth: 26,670 light-years<br><br>\"\n",
             "        f\"Distance from Earth: {SGR_A_DISTANCE_LY:,.0f} light-years<br><br>\"\n"),
            ("import the distance",
             "anchor",
             "    S_STAR_CATALOG, SGR_A_MASS_SOLAR, SCHWARZSCHILD_RADIUS_AU,\n",
             "    S_STAR_CATALOG, SGR_A_MASS_SOLAR, SGR_A_DISTANCE_LY,\n"
             "    SCHWARZSCHILD_RADIUS_AU,\n"),
        ]),

    "sgr_a_visualization_core_arcs.py": (
        "dc3c50ec02c7de4a7733aa29711f3996", [
            ("derive the two typed figures",
             "anchor",
             "        f\"Mass: 4.154 million solar masses<br>\"\n",
             "        f\"Mass: {SGR_A_MASS_SOLAR / 1e6:.3f} million solar masses<br>\"\n"),
            ("derive the distance",
             "anchor",
             "        f\"Distance from Earth: 26,670 light-years<br><br>\"\n",
             "        f\"Distance from Earth: {SGR_A_DISTANCE_LY:,.0f} light-years<br><br>\"\n"),
            ("import the distance",
             "anchor",
             "    S_STAR_CATALOG, SGR_A_MASS_SOLAR, SCHWARZSCHILD_RADIUS_AU,\n",
             "    S_STAR_CATALOG, SGR_A_MASS_SOLAR, SGR_A_DISTANCE_LY,\n"
             "    SCHWARZSCHILD_RADIUS_AU,\n"),
        ]),

    "exoplanet_coordinates.py": (
        "2b8770e9684ed72be6a33e531d047950", [
            ("import PARSEC_TO_AU",
             "anchor",
             "import numpy as np\nfrom datetime import datetime, timezone\n",
             "import numpy as np\nfrom datetime import datetime, timezone\n"
             "from constants_new import PARSEC_TO_AU\n"),
            ("sweep the four literal sites",
             "token", rb"206265", b"PARSEC_TO_AU", 4),
        ]),

    "LEDGER_CONSOLIDATED.md": (
        "1714a9764a76d2431ac1616100343584", [
            ("open L-247",
             "anchor",
             "\n## PENDING ACTION (Tony-side)\n",
             "\n" + BLOCK_247 + "## PENDING ACTION (Tony-side)\n"),
        ]),
}


def main():
    if not os.path.exists("constants_new.py"):
        print("ERROR: run this from the repo root (constants_new.py not found here).")
        return 1

    staged = {}
    pre_nonascii = {}

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
        pre_nonascii[path] = sum(1 for b in data.replace(b"\r\n", b"\n") if b > 127)
        print("base ok  %-34s (%s)" % (path, "CRLF" if is_crlf else "LF"))

        out = data
        for edit in edits:
            label, kind = edit[0], edit[1]
            if kind == "anchor":
                old, new = edit[2], edit[3]
                try:
                    new.encode("ascii")
                except UnicodeEncodeError as e:
                    print("ERROR: non-ASCII in inserted text, %s / %s: %s"
                          % (path, label, e))
                    return 1
                o = old.encode("utf-8")
                n = new.encode("ascii")
                if is_crlf:
                    o = o.replace(b"\n", b"\r\n")
                    n = n.replace(b"\n", b"\r\n")
                c = out.count(o)
                if c != 1:
                    print("ANCHOR FAIL [%s / %s]: expected 1 match, got %d"
                          % (path, label, c))
                    print("  Nothing written.")
                    return 1
                out = out.replace(o, n)
            else:
                pattern, repl, expected = edit[2], edit[3], edit[4]
                found = len(re.findall(pattern, out))
                if found != expected:
                    print("COUNT FAIL [%s / %s]: expected %d, found %d"
                          % (path, label, expected, found))
                    print("  Nothing written.")
                    return 1
                out = re.sub(pattern, repl, out)
            print("ok  %-34s %s" % (path, label))

        staged[path] = (data, out, is_crlf)

    # No local redefinition of a migrated name may survive.
    dead = (rb"^G_CONST *=", rb"^SPEED_OF_LIGHT *=", rb"^SOLAR_MASS_KG *=",
            rb"^AU_TO_METERS *=", rb"^PARSEC_TO_AU *=", rb"^YEAR_TO_SECONDS *=",
            rb"^SGR_A_MASS_SOLAR *=", rb"^SGR_A_DISTANCE_PC *=",
            rb"^SGR_A_DISTANCE_LY *=")
    body = staged["sgr_a_star_data.py"][1].replace(b"\r\n", b"\n")
    for p in dead:
        if re.search(p, body, re.M):
            print("ERROR: a local definition survives in sgr_a_star_data.py "
                  "(%s). Nothing written." % p.decode())
            return 1

    for path, (_b, after, _c) in staged.items():
        open(path, "wb").write(after)

    print("")
    print("patch applied to %d file(s)" % len(staged))
    for path, (before, after, crlf) in staged.items():
        post = sum(1 for b in after.replace(b"\r\n", b"\n") if b > 127)
        note = ""
        if pre_nonascii[path] or post:
            note = "  [non-ASCII %d -> %d]" % (pre_nonascii[path], post)
        print("  %-34s %+6d bytes  (%s)%s"
              % (path, len(after) - len(before), "CRLF" if crlf else "LF", note))
    print("")
    print("encoding gate: inserted text ASCII-clean in every file; the 3")
    print("pre-existing non-ASCII bytes in sgr_a_star_data.py (an em dash at")
    print("line 155) were SWEPT with the block they sat in, not left behind.")

    print("")
    print("py_compile:")
    failed = 0
    tmpdir = tempfile.mkdtemp(prefix="l247_pyc_")
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
    print("     Constants change WILL report additions this time. That is the")
    print("     checker doing its job, not a fault.")
    print("  3. Regenerate the Sgr A* views and hover the black hole marker.")
    print("     Expect NO change: 4.154 million solar masses, 26,670")
    print("     light-years. Both are now derived rather than typed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
