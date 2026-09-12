"""
patch_masterplan_20260912.py - the 2026-09-12 entry in the master plan.

Run it:
    Save this file into the ORRERY repo root, open it in VS Code and
    click Run. It edits documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md.

Adds one dated entry after the 2026-09-11 one and before the section
"What this section deliberately does not carry". Nothing else moves.

The guard fingerprints the whole file, LF-normalised. One-shot.

FAILURE: the assert fires and NOTHING is written.
Undo is Discard Changes in GitHub Desktop.

Module created: September 2026 with Anthropic's Claude Opus 5.

Role: devtool
Domain: dev_tools
"""

import hashlib
import os
import sys

TARGET = os.path.join("documentation", "MASTER_PLAN_INTERACTIVE_GALLERY.md")
BASE_FINGERPRINT = "e40014c205bf1dd98a90271a2f3cd59e"

ANCHOR = """standoff written as an expression rather than a typed number. Record:
`documentation/DESIGN_unit_field_and_export_rev2_20260911.md`.

"""

ENTRY = """### 2026-09-12 -- the magnetosphere gets its models, and a Note turns out to be a store

**L-305 Gap item 4 landed** (pushed at `5b88007f`). Earth's magnetopause
is now Shue et al. (1998) and its bow shock is Jelinek et al. (2012),
carried by fifteen new rows in `constants_new.py` -- eight Shue
coefficients, Jelinek's R0 / eps / lambda, a bow shock cut angle, and
three declared solar wind conditions pointing at L-314. Both standoffs
are superseded and derived rather than typed. Every row written carries
a `# Unit:` line and a `# Status:` line.

**A patch may not leave its own output untrue, and that is the ruling
worth carrying.** The new bow shock figure made a cited hover sentence
arithmetically false: it told the visitor the value was drawn at the
midpoint of Lugaz's 11 to 14 Earth radii, and 13.51 is Jelinek at 2 nPa,
not a midpoint of anything. Tony's ruling split the work. The DELETIONS
and the attribution corrections travelled with the patch, because the
new number is what made those sentences false. The REWRITE -- the
validity ranges, the frame note, the gap between the two models -- stays
with item 7, after L-321's verdicts. Nothing new was said; four
sentences left and two attributions moved.

**`test_status_lines.py` shipped and is in the maintenance run.** It
enforces the Status Line grammar on every row that carries one: a
measured row carries a rung and a real `# Source:`; a declared row
carries neither a rung nor a citation on the status line itself; a
pending row names a handle; a derived row names inputs that exist. Rows
without a status line are reported and counted, not gated -- that walk
is L-322's. All eight failing rules were negative-tested before
delivery. Two rulings came out of building it: a scanner change to read
status lines belongs to L-322 with the one walk, not in front of L-305;
and a declared row MAY cite, because `INNER_CORONA_RADII` cites the
paper that states its convention.

**The belts opened a class, and it is not the one we thought.** Three
figures for the outer radiation belt reach a visitor: the drawn torus at
the flux peak, a hover saying 3 to 7 Earth radii, a tooltip saying
13,000 to 60,000 km. A Fable review corrected our diagnosis: the span IS
in the store, as prose in each row's `# Note:`, where nothing can
interpolate it and nothing can check it. **A Note became a store** --
and it had already drifted inside a single row, since the outer belt's
own Source cites Baker at 3 to 6.5 Earth radii while its Note two lines
below says L = 3 to 7. Tony's reframe closed it: units convert and
significant figures already govern them, so the frame is a convention,
not a design question. What the viewer must be told is which STATE each
number is in -- measured, an envelope with no sharp edge, or a
stylization. A radiation belt has no edge; we store the envelope with
its sources or we state the absence, and we do not pick a winner out of
a range. L-323 carries it; the magnetotail extent joined the slice.

**L-314 gained its sampling decision.** A nightly spot value is the
wrong sampler for a coronal mass ejection -- a shock compresses the
magnetosphere for hours, and a once-a-day build most likely misses the
event worth showing, leaving the viewer a quiet magnetosphere on the day
of a severe storm. The builder takes the day's ENVELOPE instead: minimum,
maximum and mean of each input and of both derived standoffs. What makes
it worth a viewer's attention, measured against the stored coefficients:
geostationary orbit sits at 6.6 Earth radii and the exhibit already
serves it, and at 10 nPa with Bz at -20 nT the magnetopause stands off
at 6.32 -- inside the satellites. Pressure alone barely does it; the
exponent is -1/6.6, so a tenfold jump moves the nose 29 per cent.
Southward field is what lets the boundary in. What it may not say is
that a CME caused it: that is an analysis, and Kp and the G-scale are
what is measured and publishable.

**Next.** L-305 items 6 (the gallery config, carrying three retired
claims), 5 (the port), 7 (the hovers, after L-321's verdicts), 8 (store
drift, then Mode 5 on the phone first). L-323's design record and
revision 3 prompts are owed and the 2026-09-11 prompts must not be sent
as they stand. Handoff:
`documentation/HANDOFF_L305_L323_20260912.md`.

"""


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, TARGET)
    if not os.path.exists(path):
        print("ERROR: %s is not under this script's directory. Put this file "
              "in the orrery repo ROOT. NOTHING was written." % TARGET)
        return 1

    raw = open(path, "rb").read()
    was_crlf = b"\r\n" in raw
    content = raw.replace(b"\r\n", b"\n") if was_crlf else raw

    actual = hashlib.md5(content).hexdigest()
    if actual != BASE_FINGERPRINT:
        print("ERROR: base moved. %s content md5 is %s, built against %s. "
              "NOTHING was written." % (TARGET, actual, BASE_FINGERPRINT))
        return 1
    print("ok   base fingerprint matches%s" % (" [CRLF]" if was_crlf else ""))

    old_b = ANCHOR.encode("ascii")
    n = content.count(old_b)
    if n != 1:
        print("ANCHOR FAIL: the 2026-09-11 entry's tail matched %d times, "
              "expected 1. NOTHING was written." % n)
        return 1
    out = content.replace(old_b, old_b + ENTRY.encode("ascii"))
    print("ok   2026-09-12 entry added after the 2026-09-11 one")

    try:
        ENTRY.encode("ascii")
    except UnicodeEncodeError as exc:
        print("ANCHOR FAIL: added text is not ASCII (%s). NOTHING was "
              "written." % exc)
        return 1
    print("ok   encoding gate: added text is ASCII")

    final = out.replace(b"\n", b"\r\n") if was_crlf else out
    with open(path, "wb") as handle:
        handle.write(final)
    print("patch applied (%d bytes, was %d)" % (len(final), len(raw)))
    print("")
    print("NEXT: commit and push, then report the SHA.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
