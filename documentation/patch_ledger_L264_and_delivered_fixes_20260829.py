"""
patch_ledger_L264_and_delivered_fixes_20260829.py

Writes the ledger block for L-264, which was cited in four committed
docstrings before it existed, and records that the L-260 and L-263 fixes
are built and delivered.

Built on orrery `e81059f5183182ceb27e2e0f2284b03654781c4b` at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
gallery `ae410c29b0ccdfe27eba1e4ec434a1113ad59d8f` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both confirmed against the live remote 2026-08-29.

ONE file, three edits. Detail blocks only; the index zone is not
touched. Run ledger_index.py afterwards.


WHY L-264 NEEDS A BLOCK AT ALL

The handle was minted inside two patch scripts and written into the
docstrings of both renamed runners, and all four are now committed. So
the code cites a ledger item that does not exist -- the same shape as
L-225, and the second time in one day that something was named without
being recorded. Writing the block is the repair; the pattern is the part
worth keeping.


WHAT IT WRITES

  1. L-264 (new, DONE, section C) -- the runner rename. Both halves are
     pushed and confirmed against the live remote, so this one really is
     closed rather than closing on a commit.

  2. L-260 gains the Mode 5 confirmation and the delivered axis fix. It
     stays OPEN: the phone half is untouched and cannot be delegated.

  3. L-263 gains the delivered value fix. It stays OPEN until the gallery
     commit lands, for the same reason L-236 did -- a ledger row claiming
     a file is committed before it is committed is a claim nothing can
     check.


AFTER RUNNING IT

  1. ledger_index.py            -- regenerates the index tables
  2. orrery_maintenance_run.py  -- should stay 11 of 11

Then commit.


HOW TO RUN IT

Drop this file into the ORRERY repo root and press Run.

Prepared August 2026 with Anthropic's Claude Opus 5 (L-264).
"""

import hashlib
import os
import sys

REPO_ROOT_FALLBACK = r"C:\Users\tonyq\Documents\GitHub\palomas_orrery"
PROBE = "constants_new.py"

LEDGER = "LEDGER_CONSOLIDATED.md"
LEDGER_MD5 = "eacf0903e25a39d56f6449f047eae7cf"


L264 = (
    "#### [L-264] One name, two programs: the runners get repo-specific names\n"
    "<!-- L:264 status:DONE upd:2026-08-29 section:C flag: rice:3/4/95/1 -->\n"
    "- **The incident, 2026-08-29.** Two different programs were both\n"
    "  called `maintenance_run.py`, one per repository. The gallery's was\n"
    "  downloaded, the orrery's was displaced in the same folder, and the\n"
    "  dashboard button reported a file that was not there. The orrery\n"
    "  went three commits without its runner (`805f38c`, `c76bfa02`,\n"
    "  until `e81059f5`), and the deletion was invisible in the commit\n"
    "  that made it because it travelled beside an added patch script.\n"
    "- **Renamed.** `orrery_maintenance_run.py` here (L-188: four\n"
    "  generators, eleven checkers) and `gallery_maintenance_run.py` in\n"
    "  the gallery (L-236: six rows offline, two more under `--live`).\n"
    "  Each docstring now names the other, so the distinction does not\n"
    "  have to be rebuilt from this entry.\n"
    "- **Seven live references swept**, counted before the work rather\n"
    "  than after: the dashboard button, `module_atlas.py`'s role map,\n"
    "  `worksheet_checker.py` twice, and three test-module docstrings.\n"
    "  `MODULE_ATLAS.md` carried four more and was left alone because it\n"
    "  is generated. Zero references in any skill and zero in the\n"
    "  protocol, which is why the sweep was small.\n"
    "- **NOT swept, deliberately:** this ledger, the handoffs, and the\n"
    "  spent patch scripts under `documentation/`. They record what\n"
    "  happened under the name the file had at the time. Rewriting them\n"
    "  would be the item-rebasing leak this ledger already carries a\n"
    "  lesson about.\n"
    "- **Two dashboard rows added for the gallery runner**, offline and\n"
    "  `--live`, both launching in `GALLERY_REPO_DIR`. An earlier session\n"
    "  recommended AGAINST a dashboard entry, on the grounds that a\n"
    "  button in the orrery would reach into a sibling directory and\n"
    "  contradict the reasoning that put the runner in the gallery. That\n"
    "  was wrong and was asserted without reading the file: the dashboard\n"
    "  already launches gallery-repo tools that way, and Gallery Cache\n"
    "  Builder has done so for weeks. Tony caught it.\n"
    "- **A dashboard detail worth recording**, because it misled a\n"
    "  reading: the fifth element of an entry tuple is `interactive`, not\n"
    "  `indent`. Indent is the seventh. Gallery Builder Offline Tests\n"
    "  looked indented at a glance and was not.\n"
    "- **Nine tracked `.bak` files retired** in the same pass, and\n"
    "  `*.bak` added to `.gitignore`. They included 2,268 lines of\n"
    "  superseded master plan and a superseded copy of\n"
    "  provenance-discipline. A session grepping for a value or a rule\n"
    "  could hit one and read a retired state as current, which is The\n"
    "  Correction Does Not Travel with the correction sitting in the next\n"
    "  file along. Patch scripts still write backups; git no longer sees\n"
    "  them.\n"
    "- **The wider collision class, measured and left alone.** Six files\n"
    "  sit at the root of both repos under identical names:\n"
    "  `maintenance_run.py` (now fixed), `module_atlas.py`,\n"
    "  `add_docstrings.py`, `MODULE_ATLAS.md`, `MODULE_INDEX.md`,\n"
    "  `requirements.txt`. `module_atlas.py` is the same shape -- two\n"
    "  different programs, one name, both at a repo root. Recorded as a\n"
    "  class rather than renamed on spec.\n"
    "- **This block was written late, and that is the second instance\n"
    "  today.** L-264 was minted inside two patch scripts and written\n"
    "  into both renamed runners' docstrings, and all four were committed\n"
    "  before any block existed -- code citing a ledger item that was not\n"
    "  there, which is L-225's shape. The earlier instance the same day\n"
    "  was protocol v3.47 (L-258). Both were found by a person reading,\n"
    "  not by a check.\n"
    "- **Note:** RICE 3/4/95/1, confirmed by Tony 2026-08-29.\n"
    "**Ref:** L-188 (the orrery runner); L-236 (the gallery runner);\n"
    "L-225 (a handle cited with no entry); L-258 (the same failure,\n"
    "earlier the same day).\n"
    "\n"
)


EDITS = [
    (
        "L-260 gains the Mode 5 confirmation and the delivered axis fix",

        "**Gap:** both open. The axis fix is small and can ride with any next\n"
        "gallery patch; the phone read is Mode 5.\n",

        "- **Confirmed by Mode 5, 2026-08-29.** Tony's screenshot of the live\n"
        "  page shows tick labels reading 0.2, 0 and -0.2 with no axis names\n"
        "  and no unit anywhere. Not inferred from the code this time --\n"
        "  seen on the deployed exhibit, which is the gate that counts.\n"
        "- **Axis fix BUILT and delivered 2026-08-29** as\n"
        "  `patch_gallery_axis_titles_and_chromosphere_20260829.py`.\n"
        "  `buildSunLayout` gains X (AU), Y (AU), Z (AU) -- the desktop\n"
        "  orrery's own wording from `visualization_utils.py`'s\n"
        "  `build_scene_axes`, so this is the established visual language\n"
        "  carrying across rather than a new convention. The Solar System\n"
        "  Explorer's `buildLayout` has the same blank titles and is NOT\n"
        "  touched: it is a frozen exhibit on the A path and changing it is\n"
        "  a separate call with its own Mode 5.\n"
        "**Gap:** the phone. The axis half is delivered and closes on the\n"
        "gallery commit; the phone read is Mode 5 and is Tony's.\n",
    ),
    (
        "L-263 gains the delivered value fix",

        "**Gap:** one value in one file.\n",

        "- **BUILT and delivered 2026-08-29** in the same gallery patch as\n"
        "  L-260's axis titles. The value becomes 1.002874802357338, which\n"
        "  is what `constants_new.py` derives from 1.0 +\n"
        "  CHROMOSPHERE_PHYSICAL_KM / SUN_RADIUS_KM. Edited as TEXT rather\n"
        "  than by re-serialising the parsed JSON, so one digit changes\n"
        "  instead of 1,700 lines reflowing, and the result is re-parsed and\n"
        "  the value re-read before the file is written.\n"
        "- **Verified against the real store**, not asserted: the drift\n"
        "  check re-run after the edit reports 26 match, 0 DRIFT, where it\n"
        "  read 25 and 1 before.\n"
        "**Gap:** delivered, not yet committed. Closes on the gallery\n"
        "commit.\n",
    ),
    (
        "L-264 files in the reconciled archive",

        "#### [L-255] Skill bumps of 2026-08-26 -- handle reserved, block never written\n",

        L264
        + "#### [L-255] Skill bumps of 2026-08-26 -- handle reserved, block never written\n",
    ),
]


def find_repo_root():
    here = os.path.dirname(os.path.abspath(__file__))
    for label, folder in (("beside this script", here),
                          ("working directory", os.getcwd()),
                          ("fallback path", REPO_ROOT_FALLBACK)):
        if os.path.isfile(os.path.join(folder, PROBE)):
            print("found %s in the %s" % (PROBE, label))
            return folder
    return None


def main():
    print("patch_ledger_L264_and_delivered_fixes_20260829.py")
    root = find_repo_root()
    if root is None:
        print("REFUSED: could not find %s. Move this script into the ORRERY"
              % PROBE)
        print("         repo root and run it again.")
        return 1

    path = os.path.join(root, LEDGER)
    print("")
    print("target :", LEDGER)
    if not os.path.isfile(path):
        print("REFUSED: no such file.")
        return 1
    with open(path, "rb") as handle:
        raw = handle.read()

    was_crlf = b"\r\n" in raw
    content = raw.replace(b"\r\n", b"\n") if was_crlf else raw
    actual = hashlib.md5(content).hexdigest()
    print("md5    : %s (expected %s)%s"
          % (actual, LEDGER_MD5, "   [CRLF]" if was_crlf else ""))
    if actual != LEDGER_MD5:
        print("REFUSED: %s is not in the state this patch expects." % LEDGER)
        print("         Nothing written.")
        return 1

    text = content.decode("utf-8")
    for label, old, _new in EDITS:
        count = text.count(old)
        print("  anchor x%d  %s" % (count, label))
        if count != 1:
            print("REFUSED: anchor matched %d times, expected 1." % count)
            print("         Nothing written.")
            return 1
    for _label, old, new in EDITS:
        text = text.replace(old, new, 1)

    out = text.encode("utf-8")
    before = sum(1 for byte in raw if byte > 127)
    after = sum(1 for byte in out if byte > 127)
    print("  non-ascii bytes: %d -> %d" % (before, after))
    if after != before:
        print("REFUSED: the patch introduced non-ASCII text.")
        return 1

    backup = raw
    final = out.replace(b"\n", b"\r\n") if was_crlf else out
    with open(path + ".bak", "wb") as handle:
        handle.write(backup)
    with open(path, "wb") as handle:
        handle.write(final)
    print("")
    print("WROTE   %s  (%d -> %d bytes%s)"
          % (LEDGER, len(backup), len(final), ", CRLF" if was_crlf else ""))

    print("")
    print("Next, in this order:")
    print("  1. ledger_index.py            -- regenerates the index")
    print("  2. orrery_maintenance_run.py  -- should stay 11 of 11")
    print("")
    print("Then commit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
