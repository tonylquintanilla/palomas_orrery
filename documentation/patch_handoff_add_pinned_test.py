"""
patch_handoff_add_pinned_test.py

One item added to the 2026-08-29 handoff, at Tony's ruling to carry it
rather than fix it in session.

Built on orrery `7d89c06c74f9ba4673b7658ce3b4b9df838a472d` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Confirmed against the live remote 2026-08-29.


WHY

`maintenance_run.py` reported one failing checker after the L-258 push:
Constants relations, `test_radiative_zone_au_derived_from_solar_radius`.
The failure is CORRECT and the constant is fine. The test hardcodes the
old measured value:

    \"\"\"RADIATIVE_ZONE_AU must equal 0.7 * SOLAR_RADIUS_AU.\"\"\"
    expected = 0.7 * SOLAR_RADIUS_AU

It is named as a derivation test, but 0.7 is a MEASURED value, not a
structural factor -- so it was a fifty-sixth pinned literal wearing a
structural test's name, and that is why it survived the 2026-08-13 sweep
that retired the other fifty-five.

`test_core_au_derived_from_solar_radius` has the identical shape with
0.2 and passes only because CORE_AU has not moved yet.

The handoff was written before the maintenance run and does not carry
this. It is added under "What is owed" so the next session does not have
to reconstruct it from a red checker alone, and a line goes into the
process notes because the checker firing is the system working.

Prepared August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

REPO_ROOT_FALLBACK = r"C:\Users\tonyq\Documents\GitHub\palomas_orrery"

PROBE = "constants_new.py"
TARGET = os.path.join("documentation", "HANDOFF_20260829_sun_ships.md")
TARGET_MD5 = "3dfc3c1cbbbe457e402a12edf06d9348"


def find_repo_root():
    here = os.path.dirname(os.path.abspath(__file__))
    for label, folder in (("beside this script", here),
                          ("working directory", os.getcwd()),
                          ("fallback path", REPO_ROOT_FALLBACK)):
        if os.path.isfile(os.path.join(folder, PROBE)):
            print("found %s in the %s" % (PROBE, label))
            return folder
    return None


EDITS = [
    (
        "add the pinned derivation tests under What is owed",
        "**L-257's three enforcement builds are unstarted.** The worksheet schema\n"
        "does not require `quote` and `locator`; nothing parses `# Status:`; the\n"
        "scanner still infers.\n",

        "**L-257's three enforcement builds are unstarted.** The worksheet schema\n"
        "does not require `quote` and `locator`; nothing parses `# Status:`; the\n"
        "scanner still infers.\n"
        "\n"
        "**Two pinned literals survive in `test_constants_provenance.py`, and\n"
        "one of them is failing right now.** `maintenance_run.py` reports\n"
        "Constants relations FAILED, 20 of 21, on\n"
        "`test_radiative_zone_au_derived_from_solar_radius`. The failure is\n"
        "CORRECT and the constant is fine: the test hardcodes\n"
        "`expected = 0.7 * SOLAR_RADIUS_AU`.\n"
        "\n"
        "It is named as a DERIVATION test, but 0.7 is a measured value rather\n"
        "than a structural factor. That is why it survived the 2026-08-13\n"
        "sweep that retired fifty-five pinned literals and kept eighteen\n"
        "structural tests on the stated grounds that none of them holds a copy\n"
        "of a measured value. This one did, wearing a structural test's name.\n"
        "\n"
        "`test_core_au_derived_from_solar_radius` is the identical shape with\n"
        "0.2 and passes only because `CORE_AU` has not moved. It will fire the\n"
        "moment the core is promoted off the low end of its 0.2-0.25 range.\n"
        "\n"
        "The structural claim both were reaching for is already covered by\n"
        "`test_solar_shell_ordering`, which holds no numbers at all. Restate\n"
        "both as ratio bounds rather than delete them. Tony's ruling\n"
        "2026-08-29: carry rather than fix in session -- the red checker is\n"
        "its own reminder and is loud enough not to get lost.\n",
    ),
    (
        "record the checker firing in the process notes",
        "**A test harness artifact worth not misreading.** Piping a patch's\n",

        "**A check that could fail, failing.** The pinned derivation test above\n"
        "is the counterexample to this session's other process notes: nobody\n"
        "found it by reading, and it was not caught by judgement. It fired on\n"
        "its own, in `maintenance_run.py`, the first time a value it silently\n"
        "depended on actually moved. That is what the August 12 rule asks for\n"
        "-- a check whose passing output proves the path was live -- and it\n"
        "is worth recording as working rather than only recording failures.\n"
        "\n"
        "**A test harness artifact worth not misreading.** Piping a patch's\n",
    ),
]


def main():
    print("patch_handoff_add_pinned_test.py")
    root = find_repo_root()
    if root is None:
        print("REFUSED: could not find %s. Move this script into the ORRERY"
              % PROBE)
        print("         repo root and run it again.")
        return 1

    path = os.path.join(root, TARGET)
    print("target :", path)
    if not os.path.isfile(path):
        print("REFUSED: no such file.")
        return 1

    with open(path, "rb") as fh:
        raw = fh.read()

    actual = hashlib.md5(raw).hexdigest()
    print("md5    : %s (expected %s)" % (actual, TARGET_MD5))
    if actual != TARGET_MD5:
        print("REFUSED: the handoff has changed since it was committed.")
        return 1

    if b"\r\n" in raw:
        print("REFUSED: CRLF line endings; this patch expects LF.")
        return 1

    text = raw.decode("utf-8")
    for name, old, _new in EDITS:
        n = text.count(old)
        print("  anchor x%d  %s" % (n, name))
        if n != 1:
            print("REFUSED: anchor matched %d times, expected 1." % n)
            return 1

    for _name, old, new in EDITS:
        text = text.replace(old, new, 1)

    out = text.encode("utf-8")
    before = sum(1 for c in raw if c > 127)
    after = sum(1 for c in out if c > 127)
    print("non-ascii bytes: %d -> %d" % (before, after))
    if after != before:
        print("REFUSED: the patch introduced non-ASCII text. Nothing written.")
        return 1

    with open(path + ".bak", "wb") as fh:
        fh.write(raw)
    with open(path, "wb") as fh:
        fh.write(out)

    print("")
    print("WROTE   %s  (%d -> %d bytes)" % (path, len(raw), len(out)))
    print("The handoff now carries the failing test. Nothing else to run.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
