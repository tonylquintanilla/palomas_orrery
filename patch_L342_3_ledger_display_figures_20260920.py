#!/usr/bin/env python3
"""
patch_L342_3_ledger_display_figures_20260920.py -- ORRERY repo.

Run: save this file in the ORRERY repo ROOT (next to
palomas_orrery.py), open it in VS Code and click Run.  Or:
python patch_L342_3_ledger_display_figures_20260920.py

A patch is run from its repository's ROOT and filed in documentation/
AFTER it has run. This script refuses to run from documentation/.

Built on orrery b3faf14f98d84516b1076599f59ac415a9bf5347
at https://github.com/tonylquintanilla/palomas_orrery
(gallery cdfa74c3b12cd50e8955acefb75e36f4bcbbe4ca
at https://github.com/tonylquintanilla/tonyquintanilla.github.io)

It records, in LEDGER_CONSOLIDATED.md:

  L-342  the two faults the gallery patch of the same date fixed, the
         check that reads built hovers, the two amendments Claude Fable
         5.1 made to its own build manifest, and the closing of the
         geocorona altitude this item had left open.

  L-340  the second use of the one-off config-write exception, which
         that item asked to have recorded when it is used again.

RUN THE LEDGER INDEX AFTERWARDS: python ledger_index.py. This patch does
not touch the INDEX zone and does not fingerprint it, so running the
index before or after makes no difference to whether it applies.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written September 20, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

LEDGER = "LEDGER_CONSOLIDATED.md"

# Fingerprinted OUTSIDE the INDEX zone, which ledger_index.py
# regenerates: a guard that includes it refuses for a reason that is not
# about content (safe-file-editing, A Guard Must Not Fence What a
# Generator Rewrites).
BASE_OUTSIDE_INDEX = "1ae1c361e00257d77e5da084b0dd6db0"

INDEX_START = "<!-- INDEX:START"
INDEX_END = "<!-- INDEX:END -->"


EDITS = [

# -- L-342: what shipped, and the open item it closes ----------------
("""- **STILL OPEN.** The read check: the skill says a missing `# Read:` on
  an in-scope row inside a closed slice FAILS, and no check does that
  yet. It must be demonstrated failing before `CLOSED_SLICES` changes.
  Also open: the geocorona hover gives its altitude as 631,436 km, six
  figures beside a one-figure floor, which predates C1.
""",
"""- **THE TWO FAULTS THE FIGURES FIX ADDRESSED, 2026-09-20.** Built from
  `documentation/BUILD_MANIFEST_L342_display_figures_20260920.md` by
  Claude Fable 5.1, on gallery `cdfa74c3` and orrery `b3faf14f`. The
  FIRST was formatting: a shell's radius in Earth radii printed to its
  declared figures while the kilometre line beside it went through
  `fmtKm`, which always rounded to a whole number, so the outer core
  read \"3,480 km\" beside a radius declared to five figures. The SECOND
  was arithmetic, and no formatter could have repaired it: the hover
  computed the kilometre line and the altitude FROM the value the
  export had already rounded. The upper atmosphere therefore told a
  visitor \"Altitude: 574 km\" -- (1.09 - 1) x 6378.1366, worked from a
  radius rounded to three figures -- where its source says 600. No
  rounding of 574 gives 600. Fixed by SERVING the eight constants the
  store already held (`EARTH_THERMOPAUSE_ALTITUDE_KM` and seven others)
  and printing them, and computing in the browser only what the store
  does not hold. `patch_L342_2_display_figures_20260920.py` in the
  gallery.
- **THE GEOCORONA ALTITUDE IS CLOSED**, the item this entry left open
  above. It read 631,436 km, six figures beside a one-figure floor; it
  reads 600,000 km now, and so does its radius, because at the one
  figure the source supports the two are the same number.
- **THE CHECK READS BUILT HOVERS, WHICH IS THE LESSON OF THE FIRST
  ONE.** `smoke_display_figures.js` grades 12 Earth hovers against the
  figure rules and against the manifest's acceptance table, holds 43
  hovers with no declared count byte for byte against a fixture
  recorded at `cdfa74c3`, and FAILS ON ANY NUMBER IN A HOVER IT CANNOT
  ACCOUNT FOR -- an unexamined number is a failure rather than a
  silence. It was demonstrated red on the unpatched tree, naming the
  outer core and the 574 km among 34 findings, and red three further
  ways after the fix: a count ignored at one call site, a served
  `altitude` removed so the browser falls back to subtracting, and a
  count-less Sun hover changed by one character. The gallery runner
  goes from 14 gating checkers to 15.
- **THE MANIFEST WAS CORRECTED TWICE BY ITS OWN AUTHOR**, and the
  record should show where. Claude Opus 5 raised that a check built
  only on `data/objects_config.json` could pass while the site still
  showed 574 km, since the rooms draw from the served cache. Fable
  agreed, amended section 6, and corrected Opus on which cache file:
  the page fetches `data/solar-system/coverage_index.json`, and nothing
  opens `feature_configs.json`. Opus's second worry -- that the cache
  builder filters a shell's contents -- was wrong, from a JSON dump
  truncated above the key it was looking for; the builder copies the
  whole features block. The check now reads the cache and fails if the
  cache and the config would build different hovers, in every room.
  That gate fired for real during the build.
- **THE FIXTURE EARNED ITS PLACE ON THE FIRST RUN.** It caught a fault
  the builder had just introduced: the Sun's termination shock is
  served in AU, not in body radii, and the first version of
  `shellKmLines` multiplied 94 AU by the solar radius. It would have
  told a visitor 65 million km instead of 14 billion, in a hover
  nothing else in this build was looking at.
- **STILL OPEN.** The read check: the skill says a missing `# Read:` on
  an in-scope row inside a closed slice FAILS, and no check does that
  yet. It must be demonstrated failing before `CLOSED_SLICES` changes.
  **Tony-action (decide), after the push:** whether any rule-correct
  number should be shown shorter for readability, by name. Two are
  worth looking at on the phone -- the geocorona, whose altitude and
  radius now both read 600,000 km, and LEO's inner edge at
  6,578.1366 km.
"""),

# -- L-340: the exception's second use -------------------------------
("""  **Tony-action (decide):** whether that exception stays narrow in those
  words. Claude Fable 5.1's view, 2026-09-19, is that it should -- a
  deletion is rare enough that teaching the writer to delete buys less
  than the new ways it could go wrong.
""",
"""  **Tony-action (decide):** whether that exception stays narrow in those
  words. Claude Fable 5.1's view, 2026-09-19, is that it should -- a
  deletion is rare enough that teaching the writer to delete buys less
  than the new ways it could go wrong.
- **THE EXCEPTION WAS USED A SECOND TIME, 2026-09-20, by L-342's
  figures patch.** It added eight served entries to
  `data/objects_config.json` -- an `altitude` or a `radius_km` inside a
  shell's own block, each with its value, unit, figure count and its
  own `orrery_constant`. The mirror cannot CREATE a slot, only fill one
  that is there, and the store writer writes words rather than numbers,
  so neither tool can express this change either. The patch said so in
  its own description, as the exception requires. **The proof it wrote
  the right numbers is mechanical:** a mirror run straight afterwards
  reported no change, and the link check went from 37 served links to
  45 with every one holding the export's value, unit and count.
  Recorded here because this item asked for it when the exception is
  used again.
"""),
]


def split_index(text):
    if INDEX_START in text and INDEX_END in text:
        a = text.index(INDEX_START)
        b = text.index(INDEX_END) + len(INDEX_END)
        return text[:a] + text[b:]
    return text


def fingerprint(data):
    lf = data.replace(b"\r\n", b"\n")
    return hashlib.md5(split_index(lf.decode("utf-8")).encode("utf-8")
                       ).hexdigest()


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit(
            "ERROR: run this from the ORRERY repo ROOT, next to "
            "palomas_orrery.py -- not from documentation/. NOTHING was "
            "written.")
    if not os.path.isfile(LEDGER):
        raise SystemExit(
            "ERROR: %s is not here, so this is not the orrery root. "
            "NOTHING was written." % LEDGER)

    with open(LEDGER, "rb") as handle:
        raw = handle.read()
    got = fingerprint(raw)
    if got != BASE_OUTSIDE_INDEX:
        raise SystemExit(
            "ERROR: %s is not the file this patch was built against.\n"
            "       expected %s, found %s.\n"
            "       (The INDEX zone is excluded, so running "
            "ledger_index.py is not the cause.)\n"
            "       NOTHING was written. Undo is Discard Changes in "
            "GitHub Desktop." % (LEDGER, BASE_OUTSIDE_INDEX, got))

    is_crlf = raw.count(b"\r\n") > 0
    text = raw.decode("utf-8")
    applied = []
    for old, new in EDITS:
        o = old.replace("\n", "\r\n") if is_crlf else old
        n = text.count(o)
        if n != 1:
            raise SystemExit(
                "ANCHOR FAIL: expected 1 match in %s, found %d:\n  %r\n"
                "NOTHING was written." % (LEDGER, n, old[:70]))
        text = text.replace(o, new.replace("\n", "\r\n") if is_crlf else new)
        applied.append(old.strip().split("\n")[0][:56])

    with open(LEDGER, "wb") as handle:
        handle.write(text.encode("utf-8"))

    for line in applied:
        print("ok  %-24s %s" % (LEDGER, line))
    print("")
    print("patch applied (%d edits)" % len(EDITS))
    print("")
    print("NEXT:")
    print("  1. python ledger_index.py")
    print("  2. python orrery_maintenance_run.py")
    print("  3. Move this script into documentation/, commit, push.")


if __name__ == "__main__":
    main()
