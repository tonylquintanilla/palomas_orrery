"""
patch_L243_2_au_to_km_aliases.py

L-243, second and final pass. Retires the three surviving AU_TO_KM
aliases -- names, not values. Each one already imports KM_PER_AU and
assigns it to a second name, so no number changes anywhere in this
patch. Also corrects the L-243 ledger row, which records one named
shadow when there were five names in total.

Built on e5eb3ca83b506559b58204e283bbb291f96b1d42 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

RUN COMMAND:  python patch_L243_2_au_to_km_aliases.py
Save this file in the REPO ROOT (beside constants_new.py), open it in
VS Code, click Run.

  Success: one "ok" line per edit, then "patch applied to 4 file(s)".
  Failure: ERROR / ANCHOR FAIL / COUNT FAIL. Nothing is written unless
           every edit in every file succeeded.

AFTER RUNNING:
  python ledger_index.py
  python maintenance_run.py
  Then open palomas_orrery.py in VS Code, click Run, and check two
  hovers -- named at the end of this script's output.

WHY THIS IS A SECOND PATCH RATHER THAN PART OF THE FIRST
--------------------------------------------------------
patch_L243_1 swept the VALUE: every literal 149597870.7 in live code.
It found the shadows by grepping the number, which cannot find a name
that holds no number. These three do exactly that -- `AU_TO_KM =
KM_PER_AU` -- so they were invisible to that measurement and are being
reported here rather than quietly folded in. The L-243 row's count is
corrected in the same patch, because a fix that does not reach the
record describing it is the failure that rule exists to name.

WHAT WAS THERE BEFORE, AND WHY
------------------------------
All three are residue of the April 2026 provenance pass, which replaced
the hardcoded numbers and deliberately kept the names. close_approach_
data.py says so in the two comment lines above its alias: "Local alias
preserved for minimal churn in existing callsites." That was a
reasonable call then and it is being reversed now on Tony's ruling of
2026-08-25 -- kill the name, because a second name is how AU_KM
survived a convention that already forbade it. Recorded because
deleting a deliberate decision without noting it is how a decision gets
silently reversed.

WHAT CHANGES

  sgr_a_star_data.py       alias DELETED. It is dead -- defined at line
                           161, used nowhere in the tree. The provenance
                           comment block above it stays, because it also
                           documents AU_TO_METERS on the next line.
  close_approach_data.py   alias and its two-line rationale comment
                           DELETED; 3 uses retargeted.
  apsidal_markers.py       function-local alias DELETED; 2 uses
                           retargeted.
  LEDGER_CONSOLIDATED.md   L-243 gains a correction Note.

NOT TOUCHED, and deliberately:
  - AU_TO_METERS in sgr_a_star_data.py line 162. That is KM_PER_AU *
    1000 -- a derived quantity in different units, not a second name for
    the same one. Three real consumers. Legitimate derivation.
  - The 86400.0 in apsidal_markers.py. Seconds per day is a definition,
    not a measurement.
  - provenance_scanner.py line 2523, whose alias table still lists
    ('KM_PER_AU', 'AU_TO_KM', 'AU_IN_KM'). After this patch no code
    uses either alias, and AU_IN_KM never existed at all. Whether the
    scanner should stop expecting names the codebase no longer has is a
    judgment about the scanner, not a mechanical cleanup -- L-244.
"""

import hashlib
import os
import py_compile
import re
import shutil
import sys
import tempfile

# path -> (content-normalized md5 at the base SHA, [edits])
#   ("label", "anchor", old, new)                  old matches EXACTLY ONCE
#   ("label", "token", pattern, replacement, N)    regex, asserted count
FILES = {

    "sgr_a_star_data.py": (
        "399e52b6300f1eb2668c5869db573140", [
            ("delete dead alias",
             "anchor",
             "AU_TO_KM = KM_PER_AU            # 1 AU in kilometers (149,597,870.7)\n",
             ""),
        ]),

    "close_approach_data.py": (
        "86780c3eb7272d0c5ded846bd7984d53", [
            ("delete alias and its rationale",
             "anchor",
             "# Local alias preserved for minimal churn in existing callsites.\n"
             "# Canonical source: constants_new.KM_PER_AU.\n"
             "AU_TO_KM = KM_PER_AU\n"
             "\n",
             ""),
            ("retarget 3 uses",
             "token",
             rb"\bAU_TO_KM\b", b"KM_PER_AU", 3),
        ]),

    "apsidal_markers.py": (
        "74e3b696ac5c1cfe594ead923e22f743", [
            ("delete function-local alias",
             "anchor",
             "    AU_TO_KM = KM_PER_AU\n"
             "    AU_PER_DAY_TO_KM_PER_S = AU_TO_KM / 86400.0\n",
             "    AU_PER_DAY_TO_KM_PER_S = KM_PER_AU / 86400.0\n"),
            ("retarget remaining use",
             "token",
             rb"\bAU_TO_KM\b", b"KM_PER_AU", 1),
        ]),

    "LEDGER_CONSOLIDATED.md": (
        "f3411276af547d793b0f761695097c66", [
            ("L-243 count corrected",
             "anchor",
             "L-178 (the EARTH_RADIUS_KM duplicate, same class); L-244.\n",
             "L-178 (the EARTH_RADIUS_KM duplicate, same class); L-244.\n"
             "**Note (2026-08-25) -- the count above is corrected.** The row\n"
             "says thirteen replications and ONE named shadow. Thirteen is\n"
             "right for VALUES. The name count is five: `AU_KM` in\n"
             "`spacecraft_encounters.py` and `AU_TO_KM` in\n"
             "`create_ephemeris_database.py` both held the literal and were\n"
             "retired by `patch_L243_1`; three more held no number at all --\n"
             "`AU_TO_KM = KM_PER_AU` in `sgr_a_star_data.py` (dead, used\n"
             "nowhere), `close_approach_data.py` (3 uses) and\n"
             "`apsidal_markers.py` (function-local, 2 uses) -- and were\n"
             "retired by `patch_L243_2`.\n"
             "The miss is the useful part and it is a measurement error, not\n"
             "an oversight: the sweep was scoped by grepping 149597870, and a\n"
             "grep for a number cannot find a name that holds no number.\n"
             "All three were residue of the April 2026 provenance pass, which\n"
             "replaced the values and kept the names on purpose --\n"
             "`close_approach_data.py` said so in a comment above its alias.\n"
             "Left visible rather than restated, because the next reader has\n"
             "nothing else to check the count against.\n"
             "**Ref (added):** `patch_L243_2_au_to_km_aliases.py`;\n"
             "`provenance_scanner.py` line 2523, whose alias table still\n"
             "expects `AU_TO_KM` and `AU_IN_KM` -- routed to L-244.\n"),
        ]),
}

RENDERED_SITES = [
    "close_approach_data.py -- a close-approach hover: distance in km "
    "and the +/- uncertainty",
    "apsidal_markers.py     -- a perihelion or apoapsis marker hover: "
    "distance in km, and relative speed in km/s",
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
        print("base ok  %-26s (%s)" % (path, "CRLF" if is_crlf else "LF"))

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

            print("ok  %-26s %s" % (path, label))

        # No alias name may survive in a source file this patch edited.
        if path.endswith(".py"):
            left = len(re.findall(rb"\bAU_TO_KM\b|\bAU_KM\b", out))
            if left:
                print("ERROR [%s]: %d alias name(s) still present after edits. "
                      "Nothing written." % (path, left))
                return 1

        staged[path] = (data, out, is_crlf)

    for path, (before, after, _crlf) in staged.items():
        open(path, "wb").write(after)

    print("")
    print("patch applied to %d file(s)" % len(staged))
    for path, (before, after, crlf) in staged.items():
        print("  %-30s %+6d bytes  (%s)"
              % (path, len(after) - len(before), "CRLF" if crlf else "LF"))

    print("")
    print("py_compile:")
    failed = 0
    tmpdir = tempfile.mkdtemp(prefix="l243_2_pyc_")
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
    print("  3. Open palomas_orrery.py in VS Code, click Run, and check")
    print("     these two hovers -- they are what this patch could break:")
    for s in RENDERED_SITES:
        print("       - %s" % s)
    print("")
    print("No number changed in this patch. Every alias already held")
    print("KM_PER_AU, so the only possible failure is a name that no longer")
    print("resolves, which shows up as a crash rather than a wrong figure.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
