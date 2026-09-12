"""
patch_L305_bow_shock_one_line.py - put the bow shock assignment on one
line so constants_change_report.py can read it.

Run it:
    Save this file into the ORRERY repo root (beside constants_new.py),
    open it in VS Code and click Run.

WHY. The 2026-09-12 maintenance run failed one checker, Constants
change, which reported:

    EARTH_BOW_SHOCK_STANDOFF_RADII REMOVED (was 12.5)
    2 changed line(s) carry a number but match no shape this tool reads.

The constant was not removed. It was rewritten as a parenthesised
assignment spanning three lines, and `constants_change_report.py`
matches `NAME = value` on ONE line. Seeing the name with nothing
readable after it, the tool concluded the row was gone -- and then
correctly announced that two lines carried numbers it could not
examine. The tool behaved well. The assignment did not.

That form was the only multi-line assignment among the file's 88
top-level rows, and it was introduced by the L-305 item 4 patch. This
puts it back on one line at 135 characters, against a previous longest
assignment line of 115.

After this, the report reads the row as DERIVED, names its three
parents, and records that the line owes no `# Source:` of its own
because each parent is watched. Verified against 5b88007f before
delivery.

The VALUE does not change: 13.511736110493397 before and after. The
gallery's store-drift check parses with `ast` and read the multi-line
form correctly either way, so nothing served is affected.

FAILURE: any assert below fires and NOTHING is written.
Undo is Discard Changes in GitHub Desktop.

Module created: September 2026 with Anthropic's Claude Opus 5.

Role: devtool
Domain: dev_tools
"""

import hashlib
import os
import py_compile
import sys
import tempfile

TARGET = "constants_new.py"
BASE_FINGERPRINT = "1267659208d21ebb08546246d4199875"

OLD = """EARTH_BOW_SHOCK_STANDOFF_RADII = (
    EARTH_BOW_SHOCK_JELINEK_R0_RADII
    * EARTH_SOLAR_WIND_PRESSURE_NPA ** (-1.0 / EARTH_BOW_SHOCK_JELINEK_EPS))
"""

NEW = ("EARTH_BOW_SHOCK_STANDOFF_RADII = EARTH_BOW_SHOCK_JELINEK_R0_RADII "
       "* EARTH_SOLAR_WIND_PRESSURE_NPA ** (-1 / EARTH_BOW_SHOCK_JELINEK_EPS)\n")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, TARGET)
    if not os.path.exists(path):
        print("ERROR: %s is not beside this script. Put this file in the "
              "orrery repo root and run it there. NOTHING was written."
              % TARGET)
        return 1

    raw = open(path, "rb").read()
    was_crlf = b"\r\n" in raw
    content = raw.replace(b"\r\n", b"\n") if was_crlf else raw

    actual = hashlib.md5(content).hexdigest()
    if actual != BASE_FINGERPRINT:
        print("ERROR: base moved. %s content md5 is %s, this patch was built "
              "against %s. NOTHING was written."
              % (TARGET, actual, BASE_FINGERPRINT))
        print("       Undo is Discard Changes in GitHub Desktop.")
        return 1
    print("ok   base fingerprint matches%s" % (" [CRLF]" if was_crlf else ""))

    old_b = OLD.encode("ascii")
    n = content.count(old_b)
    if n != 1:
        print("ANCHOR FAIL: the three-line assignment matched %d times, "
              "expected 1. NOTHING was written." % n)
        return 1
    out = content.replace(old_b, NEW.encode("ascii"))
    print("ok   bow shock assignment is one line again (135 chars)")

    try:
        out.decode("ascii")
    except UnicodeDecodeError as exc:
        print("ANCHOR FAIL: result is not ASCII (%s). NOTHING was written."
              % exc)
        return 1

    probe = os.path.join(tempfile.gettempdir(), "_probe_constants_new.py")
    open(probe, "wb").write(out)
    try:
        py_compile.compile(probe, doraise=True)
    except py_compile.PyCompileError as exc:
        print("ANCHOR FAIL: result does not compile (%s). NOTHING was "
              "written." % exc)
        return 1
    finally:
        if os.path.exists(probe):
            os.remove(probe)
    print("ok   encoding gate: ASCII clean and compiles")

    final = out.replace(b"\n", b"\r\n") if was_crlf else out
    with open(path, "wb") as handle:
        handle.write(final)
    print("patch applied (%d bytes, was %d)" % (len(final), len(raw)))
    print("")
    print("NEXT: run orrery_maintenance_run.py (Run button), then commit")
    print("      and push.")
    print("")
    print("      EXPECT Constants change to FAIL ONCE MORE on that run,")
    print("      with a DIFFERENT reason than before:")
    print("")
    print("        2 changed line(s) carry a number but match no shape")
    print("        this tool reads.  -    EARTH_BOW_SHOCK_JELINEK_R0_RADII")
    print("")
    print("      Those two lines are the OLD three-line form being")
    print("      DELETED. The tool cannot parse a line it is watching")
    print("      disappear, and it refuses to be silent about it, which")
    print("      is correct. The row itself now reads cleanly above that")
    print("      notice, as DERIVED with its three parents named.")
    print("")
    print("      It clears on the push. Once the one-line form is at")
    print("      HEAD there is nothing unreadable left in the diff, and")
    print("      the next run reports 'No changes since HEAD' and exits")
    print("      0. Verified here by committing locally and re-running.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
