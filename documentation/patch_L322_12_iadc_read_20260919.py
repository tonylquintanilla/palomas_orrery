#!/usr/bin/env python3
"""
patch_L322_12_iadc_read_20260919.py -- ORRERY repo.

Run: save this file in the ORRERY repo ROOT (next to
PROJECT_INSTRUCTIONS.md), open it in VS Code and click Run.  Or:
python patch_L322_12_iadc_read_20260919.py

A patch is run from its repository's ROOT and filed in documentation/
AFTER it has run. This script refuses to run from documentation/.

Built on orrery 6071df8ec6b5158cc482914d1d13d0fdbce0412e
at https://github.com/tonylquintanilla/palomas_orrery
(gallery b1c11cc7300c8fa943e1c9358d0ce699b94cf19b
at https://github.com/tonylquintanilla/tonyquintanilla.github.io)

STAGE C1, the last row. Tony read the IADC guidelines on 2026-09-19 --
the only row on his reading list -- and imaged section 3.3.2. This patch
records that read and corrects one thing the read turned up.

WHAT IT DOES (2 files, 4 anchored edits):

  constants_new.py, EARTH_LEO_UPPER_ALTITUDE_KM

      The placeholder pointing at the read record becomes a real
      "# Read:" line naming Tony, with the section he actually opened
      and the words it actually carries.

      THE REVISION IS CORRECTED. The source line said "IADC-02-01 Rev. 3
      (June 2021)". The document at the row's own "# Ref:" link -- the
      one Tony downloaded and read -- is IADC-02-01 REVISION 2, dated
      March 2020. Its revision history table lists three issues and
      stops at "1 / 2 / 2020-03-01 / Update section 5.3.2". There is no
      Rev. 3 in it. The citation named a revision the linked document is
      not, which is the quiet kind of wrong: everything around it was
      right, so nothing looked odd.

      THE SECOND CLAIM ON THAT ROW IS CONFIRMED, not corrected. The
      source line says section 3.3.1 takes the equatorial radius as the
      reference surface. It does, in those words, and the line now
      quotes the figure it gives.

  documentation/L322_earth_read_record_20260919.md

      Section 2, "For Tony to read", becomes a record of the read rather
      than a request for it: what he opened, where the local copies
      live, what the paragraph says, and the two findings.

WHO READ WHAT, because the read line has to be true about this.
Tony opened the PDF, read 3.3.2 and imaged it. This session then opened
the same document at the same address and read it through, which is what
turned up the revision error and confirmed 3.3.1 -- neither is visible
in the paragraph Tony imaged. The line names Tony, because he did the
read the row needed; the corroboration is recorded in the read record
where there is room to say who found what.

THE PAPER AND THE IMAGE ARE NOT IN THE REPOSITORY, and that is correct.
documentation/papers/ is gitignored. Both files live on Tony's disk
only, and the read record says so rather than pointing at paths that a
later reader would not find.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written to EITHER file. Undo is Discard Changes in GitHub Desktop.
"""

import hashlib
import os
import sys

STORE = "constants_new.py"
RECORD = "documentation/L322_earth_read_record_20260919.md"

BASE = {
    STORE:  "6946a3f454438ed34575d7364fb0bb39",
    RECORD: "91f077fe7e2ed6d0d8b1bed0eb515264",
}


def fail(msg):
    print(msg)
    print("NOTHING was written to either file. Undo is Discard Changes in "
          "GitHub Desktop.")
    sys.exit(1)


def fingerprint(raw):
    return hashlib.md5(raw.replace(b"\r\n", b"\n")).hexdigest()


EDITS = []

EDITS.append((STORE, "STORE  EARTH_LEO_UPPER_ALTITUDE_KM  the read line, Tony's read",
    b"""# Read: for Tony -- see documentation/L322_earth_read_record_20260919.md.
# Read+: The primary IADC document could not be opened from this session;
# Read+: the definition was confirmed only in reproductions of it.
""",
    b"""# Read: IADC-02-01 Revision 2, section 3.3.2 (1), p. 8 -- "Region A,
# Read+: Low Earth Orbit (or LEO) Protected Region -- spherical region
# Read+: that extends from the Earth's surface up to an altitude (Z) of
# Read+: 2,000 km", 2026-09-19, Tony Quintanilla. Corroborated the same
# Read+: day by Claude Opus 5, which read the whole document and found
# Read+: the revision error corrected below. Detail, and where Tony's
# Read+: local copies of the paper and his image of the paragraph sit,
# Read+: are in documentation/L322_earth_read_record_20260919.md.
"""))

EDITS.append((STORE, "STORE  EARTH_LEO_UPPER_ALTITUDE_KM  revision corrected Rev. 3 -> Revision 2",
    b"""# Source: IADC Space Debris Mitigation Guidelines, IADC-02-01 Rev. 3
# Source+: (June 2021), section 3.3.2 -- the LEO Protected Region extends
# Source+: from the surface to an altitude of 2,000 km. Section 3.3.1 takes
# Source+: the equatorial radius as the reference surface, as this file does.
""",
    b"""# Source: IADC Space Debris Mitigation Guidelines, IADC-02-01 REVISION
# Source+: 2, March 2020, section 3.3.2 (1) -- the LEO Protected Region
# Source+: extends from the Earth's surface to an altitude of 2,000 km.
# Source+: Section 3.3.1 takes the equatorial radius as the reference
# Source+: surface, as this file does, and gives it as 6,378 km.
# Source+: Corrected 2026-09-19: the old line said "Rev. 3 (June 2021)".
# Source+: The document at the Ref link below, which is the one that was
# Source+: read, is Revision 2 of March 2020, and its revision history
# Source+: table ends there. No Rev. 3 was involved.
"""))

EDITS.append((RECORD, "RECORD  section 2 becomes the record of the read",
    b"""## 2. For Tony to read

One row. This is your whole share of the reading for C1.

### `EARTH_LEO_UPPER_ALTITUDE_KM` = 2000.0 km

**Where to look:** the IADC Space Debris Mitigation Guidelines,
IADC-02-01. The row's own `# Ref:` line points at
https://orbitaldebris.jsc.nasa.gov/library/iadc-space-debris-guidelines-revision-2.pdf

**What to look for:** the definition of the LEO Protected Region, in the
section on protected regions (section 3.3.2 in the revision the row
cites). It is usually labelled "Region A".

**The number you should expect to see:** an altitude of **2,000 km**,
with the region extending from the Earth's surface up to it. The row also
claims the guidelines take the **equatorial radius** as the reference
surface, so that is worth confirming in the same place.

**Why it is on your list and not read above.** This session could not
open the primary document. The definition was confirmed in several
independent reproductions of it, including a reproduction of the IADC
2007 protected-regions figure, and every one of them says 2,000 km from
the surface. But a reproduction is not the document, and The Access
Standard says a read records what was OPENED. So the row carries no
`# Read:` line naming a model; it carries a pointer to this file instead.

**If the link is dead** -- the row's URL says "revision-2" while the
source line says "Rev. 3 (June 2021)", so it may well be -- then the
citation fails The Access Standard and the row should be re-homed to
whatever the current IADC publication is, or to a standards body that
restates it. Tell me which and I will do it in C2.

**When you have read it,** the line to add is:

```
# Read: IADC Space Debris Mitigation Guidelines, LEO Protected Region,
# Read+: <the section number you actually found it in>, <date>, Tony
# Read+: Quintanilla
```
""",
    b"""## 2. Read by Tony, 2026-09-19 -- DONE

One row, and it is closed. The link was alive.

### `EARTH_LEO_UPPER_ALTITUDE_KM` = 2000.0 km

**What Tony opened.** The IADC Space Debris Mitigation Guidelines at the
row's own `# Ref:` address,
https://orbitaldebris.jsc.nasa.gov/library/iadc-space-debris-guidelines-revision-2.pdf
He downloaded it, read section 3.3.2 on page 8 of 14, and imaged the
paragraph.

**Where the local copies live.** `documentation/papers/` on Tony's disk,
as `iadc-space-debris-guidelines-revision-2.pdf` and
`EARTH_LEO_UPPER_ALTITUDE_KM_2000_km_tony_read.png`. **Neither is in the
repository, and that is deliberate** -- `documentation/papers/` is
gitignored, so a later reader will not find them by path. The address
above is what travels.

**What it says.** Section 3.3.2 (1): "Region A, Low Earth Orbit (or LEO)
Protected Region -- spherical region that extends from the Earth's
surface up to an altitude (Z) of 2,000 km". AGREES with 2000.0.
Exact -- a defined region boundary, not a measurement.

**Two findings this read turned up, neither visible in the imaged
paragraph.** After Tony confirmed the number, this session opened the
same document at the same address -- it was reachable on a second attempt
-- and read it through.

- **The revision was wrong, and is corrected.** The row's source line
  said "IADC-02-01 Rev. 3 (June 2021)". The document is IADC-02-01
  **Revision 2, March 2020**. Its revision history table lists exactly
  three issues -- 2002-10-15 initial, 2007-09-01 first revision,
  2020-03-01 update to section 5.3.2 -- and stops. There is no Rev. 3.
  The number, the section and the link were all right, which is why
  nothing looked odd.
- **The equatorial-radius claim is right, and is now quoted.** Section
  3.3.1: "the equatorial radius of the Earth is taken as 6,378 km and
  this radius is used as the reference for the Earth's surface from which
  the orbit regions are defined." The row said so already; it now carries
  the figure too.

**Who read, and why the line names Tony.** Tony opened the document and
read the paragraph the row depends on. That is the read the row needed
and the `# Read:` line names him. The corroborating pass is recorded here
rather than on the row, because a read line names a reader and a place,
not an audit trail.
"""))

EDITS.append((RECORD, "RECORD  the header stops promising a list that no longer exists",
    b"""Tony's reading list -- the rows this session could not open. There is one
of them.
""",
    b"""Tony's reading list. It had one row on it; Tony read it on 2026-09-19
and section 2 now records that read rather than asking for it.
"""))


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        fail("ERROR: this script is running from documentation/. Move it "
             "to the repository ROOT and run it there.")
    for path in (STORE, RECORD):
        if not os.path.exists(path):
            fail("ERROR: " + path + " is not here. Run this from the "
                 "ORRERY repo root.")

    raws = {}
    for path in (STORE, RECORD):
        with open(path, "rb") as handle:
            raws[path] = handle.read()
        got = fingerprint(raws[path])
        if got != BASE[path]:
            fail("ERROR: " + path + " is not the file this patch was cut "
                 "against.\n  expected " + BASE[path] + "\n  found    "
                 + got + "\nIf the patch already ran, this is what a "
                 "second run looks like: it refuses.")

    out = dict(raws)
    for path, label, old, new in EDITS:
        is_crlf = raws[path].count(b"\r\n") > 0
        if is_crlf:
            old = old.replace(b"\n", b"\r\n")
            new = new.replace(b"\n", b"\r\n")
        n = out[path].count(old)
        if n != 1:
            fail("ANCHOR FAIL: expected exactly 1 match, found %d -- %s\n"
                 "  anchor began: %r" % (n, label, old[:70]))
        out[path] = out[path].replace(old, new)

    for path, data in out.items():
        try:
            data.decode("ascii")
        except UnicodeDecodeError as exc:
            fail("ERROR: the result for " + path + " is not ASCII (%s)."
                 % exc)

    for path, data in out.items():
        with open(path, "wb") as handle:
            handle.write(data)

    for path, label, _old, _new in EDITS:
        print("  ok  " + label)
    print("")
    for path in sorted(out):
        print("      %-52s %7d -> %7d bytes"
              % (path, len(raws[path]), len(out[path])))
    print("")
    print("patch applied (2 files, %d edits)" % len(EDITS))
    print("")
    print("NOW, in order:")
    print("  1. Run the orrery maintenance run. Nothing should change")
    print("     except the two files above: this patch touches no value,")
    print("     so the export and every checker should be unmoved.")
    print("  2. Move this script into documentation/.")
    print("  3. Commit and push. Report the new SHA.")
    print("")
    print("Undo at any point is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
