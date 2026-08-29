"""
patch_handoff_carry_four.py

Four items added to the 2026-08-29 handoff, all at Tony's ruling to
carry rather than fix in session.

**This REPLACES patch_handoff_add_pinned_test.py AND
patch_handoff_carry_three.py.** Neither was run; each carried a subset.
Run only this one.

Built on orrery `7d89c06c74f9ba4673b7658ce3b4b9df838a472d` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Confirmed against the live remote 2026-08-29.


ITEM 1 -- two pinned literals in test_constants_provenance.py

`maintenance_run.py` reported one failing checker after the L-258 push.
The failure is CORRECT and the constant is fine: the test hardcodes the
old measured value, `expected = 0.7 * SOLAR_RADIUS_AU`. It is named as a
derivation test, but 0.7 is a MEASURED value, not a structural factor --
which is why it survived the 2026-08-13 sweep that retired fifty-five
pinned literals. `test_core_au_derived_from_solar_radius` is the
identical shape with 0.2 and is silent only because CORE_AU has not
moved.


ITEM 2 -- the Sun exhibit's axes carry no units

Copied from the Solar System Explorer's own convention, blank axis
titles, so it is not a deviation introduced by the Sun exhibit. But it
lands differently: the Explorer's frame is always about 35 AU, and the
Sun's moves from 0.26 AU on arrival to 173,250 AU with the gravitational
influence drawn. A visitor reads ticks saying "150k" with nothing saying
what of. Every hover on the page carries both km and AU; the axes are
the one surface that does not.


ITEM 3 -- mobile is untested, and it is a Mode 5 item

Nobody has opened the exhibit on a phone. The legend is an eighteen-entry
overlay and the modebar is hidden below 768 px by the gallery's existing
convention. Tony's note, 2026-08-29: deferred deliberately, because the
major thing was done.

ITEM 4 -- there is no maintenance runner on the gallery side

Tony's observation, 2026-08-29, and this session is the argument for
it. Measured at gallery `c367b262`: no maintenance runner, no
equivalent of the orrery's generator-then-checker pass, and the one
real suite -- `tools/test_gallery_cache_builder_offline.py`, 149
checks -- sits in no routine at all.

A process note is also added, because the failing checker is the one
thing in this session that no person found by reading.


HOW TO RUN IT

Drop this file into the ORRERY repo root and press Run.

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
        "add all four carried items under What is owed",
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
        "both as ratio bounds rather than delete them.\n"
        "\n"
        "**The Sun exhibit's axes carry no units.** The tick labels read\n"
        "\"150k\" with nothing saying what of. This is copied from the Solar\n"
        "System Explorer's own convention -- blank axis titles, `title:\n"
        "{ text: '', font: { size: 1 } }` -- so it is not a deviation the Sun\n"
        "exhibit introduced. It lands differently here. The Explorer's frame\n"
        "is always about 35 AU; the Sun's moves from 0.26 AU on arrival to\n"
        "173,250 AU with the gravitational influence drawn, so a visitor has\n"
        "no way to know the number is AU rather than km.\n"
        "\n"
        "Every hover on the page carries km AND AU, per the standing hover\n"
        "convention. The axes are the one surface on the page that does not.\n"
        "Small fix, and the only thing currently on the live page that is\n"
        "arguably wrong rather than merely unfinished.\n"
        "\n"
        "**Mobile is untested, and it is a Mode 5 item.** Nobody has opened\n"
        "the Sun exhibit on a phone. The legend is an eighteen-entry overlay\n"
        "panel and the modebar is hidden below 768 px by the gallery's\n"
        "existing convention, so the phone experience is unknown -- on a site\n"
        "whose whole premise is that it works on one. Tony deferred this\n"
        "deliberately on 2026-08-29 because the major thing was done; it\n"
        "cannot be delegated, since Mode 5 is his render and his eyes.\n"
        "\n"
        "**There is no maintenance runner on the GALLERY side, and the\n"
        "asymmetry is backwards.** `maintenance_run.py` runs thirteen\n"
        "checkers and lives in the orrery, which is Tony's desktop. The\n"
        "gallery is the PUBLIC surface, and it has no runner at all.\n"
        "Measured at gallery `c367b262`: nothing named maintenance, runner or\n"
        "run_all anywhere in the repo. The one real suite,\n"
        "`tools/test_gallery_cache_builder_offline.py` at 149 checks, is a\n"
        "file somebody has to remember -- which is A Check That Cannot Fail\n"
        "Is Not Passing in its third form: put the check where it runs.\n"
        "\n"
        "**This session is the argument.** Three of the four defects were on\n"
        "the gallery side and no orrery check could reach any of them: Pages\n"
        "serving no `.py` at all, the orphan info markers in the shared\n"
        "renderer, and `objects_config.json` drifting from `constants_new.py`.\n"
        "\n"
        "Two candidate checks, named because each would have caught one of\n"
        "today's failures and both are cheap:\n"
        "\n"
        "*(a) A served-reachability check.* Fetch ONE file per critical path\n"
        "family from the LIVE site and require 200 -- an assembler module, the\n"
        "coverage index, a positions file. The Jekyll failure was invisible to\n"
        "`python -m http.server`, where every previous test had run, and would\n"
        "have been caught in a single request. The check has to run against\n"
        "the CDN, because that is the thing that was broken.\n"
        "\n"
        "*(b) A store-drift REPORT.* Thirty entries in `objects_config.json`\n"
        "already carry `orrery_constant` pointers like\n"
        "`constants_new.py::RADIATIVE_ZONE_AU`. Nothing follows them. A\n"
        "read-only checker that fetches `constants_new.py` at the orrery HEAD\n"
        "SHA and reports every pointer whose value disagrees would have caught\n"
        "0.7 against 0.713 the moment it happened.\n"
        "\n"
        "It is NOT the transport and does not replace segment 2 -- it moves\n"
        "nothing and fixes nothing. It converts a silent hole into a loud one\n"
        "for a fraction of the cost, and it can be built BEFORE the transport\n"
        "rather than instead of it. The pointers are already there; only the\n"
        "checker that follows them is missing.\n"
        "\n"
        "It should not be a copy of the orrery's runner. Different repo,\n"
        "different failure modes: the orrery's checkers ask whether a value is\n"
        "sourced, and the gallery's would ask whether what is SERVED matches\n"
        "what was exported and can actually be fetched. No ledger handle yet.\n",
    ),
    (
        "record the checker firing in the process notes",
        "**A test harness artifact worth not misreading.** Piping a patch's\n",

        "**A check that could fail, failing.** The pinned derivation test above\n"
        "is the counterexample to the rest of this section. Nobody found it by\n"
        "reading and it was not caught by judgement. It fired on its own, in\n"
        "`maintenance_run.py`, the first time a value it silently depended on\n"
        "actually moved. That is the outcome the 2026-08-12 rule was written\n"
        "for -- a check whose passing output proves the path was live -- and\n"
        "it is worth recording as working, not only recording failures.\n"
        "\n"
        "**A test harness artifact worth not misreading.** Piping a patch's\n",
    ),
]


def main():
    print("patch_handoff_carry_four.py")
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
        print("REFUSED: the handoff is not in the state this patch expects.")
        print("         If patch_handoff_add_pinned_test.py was already run,")
        print("         this one is redundant for item 1 and must be re-cut")
        print("         for items 2 and 3.")
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
    print("")
    print("The handoff now carries all four. Nothing else to run.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
