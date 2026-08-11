"""
patch_ledger_L189_close.py -- close L-189 in LEDGER_CONSOLIDATED.md and
cross-reference the open half in L-188.

WHAT THIS DOES
    Three anchored edits to LEDGER_CONSOLIDATED.md:
      1. L-189 metadata: status OPEN -> DONE, dated 2026-08-11
      2. L-189 Gap/Ref replaced with the as-built record
      3. L-188 gains a note saying which half of L-189 waits on it

    The section tag is deliberately left at 'A'. ledger_index.py retags
    a DONE block to its closed bucket and physically relocates it; doing
    that by hand here would duplicate work the tool does correctly and
    could disagree with it.

HOW TO RUN IT
    Save this file into the palomas_orrery repo root (the folder holding
    LEDGER_CONSOLIDATED.md), open it in VS Code, and click Run.

    Or from a terminal in that folder:
        python patch_ledger_L189_close.py

    THEN run ledger_index.py the same way. That regenerates the index
    tables and moves the closed block into section C. The ledger is not
    finished until it has run.

WHAT SUCCESS LOOKS LIKE
    One "ok" line per edit, then "patch applied (N bytes)".

WHAT FAILURE LOOKS LIKE
    A single "ERROR:" line (wrong base file) or an "ANCHOR FAIL" line
    naming the edit whose text was not found. Either way NOTHING is
    written and the file on disk is untouched.

Built on dea0bc0b17c800f9399069152fee569bef260bcb
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

Written August 2026 with Anthropic's Claude Opus 5 (L-189).
"""

import hashlib
import os
import sys

TARGET = 'LEDGER_CONSOLIDATED.md'

# Content fingerprint with line endings normalized to LF.
BASE_MD5 = 'f32c594aa2b9708798991c63e4f42973'


EDITS = [
    (
        'L-189 status OPEN -> DONE',
        b"<!-- L:189 status:OPEN upd:2026-08-07 section:A flag: "
        b"rice:3/4/80/2 -->\n",

        b"<!-- L:189 status:DONE upd:2026-08-11 section:A flag: "
        b"rice:3/4/80/2 -->\n",
    ),
    (
        'L-189 as-built record',
        b"**Gap:** Build it. Additive change to a ~3,000-line shared tool;\n"
        b"treat as a shared-CI change with family-wide ripple.\n"
        b"**Ref:** provenance_scanner.py console summary block (~line 2909);\n"
        b"L-188; L-184.\n",

        b"**Note (2026-08-11): BUILT AND VERIFIED.** New module\n"
        b"  `provenance_history.py` (444 lines) plus eight anchored edits to\n"
        b"  `provenance_scanner.py`, applied by\n"
        b"  `patch_L189_run_history.py`. Shipped at `dea0bc0`.\n"
        b"- Shape is the 2026-08-07 ruling unchanged: one\n"
        b"  `data/provenance_history.json`, ring buffer of the last 6 runs,\n"
        b"  tracked in git. The per-run FIELDS follow the gallery cache\n"
        b"  builder's existing record vocabulary (`run_id` as a compact UTC\n"
        b"  stamp, `started`, `finished`, `mode`) rather than inventing a\n"
        b"  second one. Its one-file-per-run LAYOUT was not adopted: the\n"
        b"  builder runs nightly, the scanner runs several times in a working\n"
        b"  session, and the 23 files accumulated in the gallery repo since\n"
        b"  July show what that costs in the changed-files list.\n"
        b"- **Cadence declared: 1 day, compared by calendar DATE** (Tony,\n"
        b"  2026-08-11) -- once per day, not at a fixed time, because the run\n"
        b"  is manual. A file that only accumulates runs cannot report a run\n"
        b"  that never happened; the declared number is what makes the\n"
        b"  missing run detectable.\n"
        b"- Console prints the DELTA after the priority summary and before\n"
        b"  the Tier-1 banner, and NAMES any file whose Tier-1 rose. Files\n"
        b"  whose Tier-1 fell are not named: a drop is the outcome the work\n"
        b"  aims at, and naming it competes with the thing needing a call.\n"
        b"  `PROVENANCE_AUDIT.md` carries a Run History table ahead of the\n"
        b"  risk matrix.\n"
        b"- Informational only. The exit code is untouched, per the scanner's\n"
        b"  standing design review section 3c.\n"
        b"- **First-run cost, predicted and attributable: 879 -> 882\n"
        b"  findings.** The three are the new module's own SCHEMA_VERSION,\n"
        b"  MAX_RUNS and EXPECTED_CADENCE_DAYS -- all Tier 3, all\n"
        b"  `dev_tools`, Tier-1 unchanged at 206. The console says so on the\n"
        b"  first run rather than letting the jump read as a regression.\n"
        b"  **(decide)** whether those three earn `provenance_exceptions.json`\n"
        b"  entries: they are configuration, not factual claims, which is the\n"
        b"  textbook shape of an accepted residual.\n"
        b"- **`is_overdue()` and `overdue_lines()` ship UNCALLED, by design.**\n"
        b"  A scanner that is running cannot report that it did not run, so\n"
        b"  the staleness check cannot live inside the thing it watches.\n"
        b"  L-188 is the trigger; L-189 is the data. The module docstring\n"
        b"  says this explicitly so a later session does not remove them as\n"
        b"  dead code.\n"
        b"- The divergence checker noted above stays OUT of scope. It flags\n"
        b"  CITED claims that disagree with the store, where the scanner\n"
        b"  flags UNCITED ones -- a different check, and it belongs with\n"
        b"  L-190's reach work.\n"
        b"- **(do)** move `patch_L189_run_history.py` out of the repo root\n"
        b"  into `documentation/` (alongside `patch_dashboard_manual_builder\n"
        b"  .py`). It was committed to the root at `dea0bc0`; it is spent,\n"
        b"  its base fingerprint no longer matches, and while it sits there\n"
        b"  the scanner counts 119 files instead of 118 and `module_atlas.py`\n"
        b"  reports one undetermined module.\n"
        b"**Note (2026-08-11), measurement kept from the cadence discussion.**\n"
        b"  Every trust window in the gallery served cache is set by its\n"
        b"  CATEGORY CAP, never by measured propagation error -- across all\n"
        b"  eleven objects carrying a trust block, the error test has never\n"
        b"  been the binding constraint. Apophis alone binds the global\n"
        b"  served window: 647.0868619950488 days, identical to the served\n"
        b"  window's own width to the last digit, recentered on build time.\n"
        b"  The per-object windows that look alarming -- Io +/-5.3 hours,\n"
        b"  Charon +/-19 hours, Titan +/-2.0 days, Moon +/-3.4 days, Pluto\n"
        b"  +/-6.4 days -- are excluded from the global gate by frame per\n"
        b"  L-149 and are enforced by nothing. Tony's call: NOT its own\n"
        b"  ledger item, because the practical cost is sub-pixel. On a plot\n"
        b"  where the orbit spans 400 pixels the worst case (Moon) is about\n"
        b"  0.15 px after a day and 1.1 px after a week, and the orbit SHAPE\n"
        b"  does not degrade at all, being geometric. It is a gate that does\n"
        b"  not fire, not a picture that is wrong. Recorded here so the next\n"
        b"  session to find Io's five-hour window does not re-raise it.\n"
        b"**Verification:** sandbox clone at `df7ca50` -- patch applied,\n"
        b"scanner run three times, ring-buffer trim at 6, corrupt-file\n"
        b"tolerance, HEAD SHA read without invoking git, and the Tier-1-rose\n"
        b"path exercised against real per-file counts. Confirmed on Tony's\n"
        b"machine at `dea0bc0`: 882 findings, 206 Tier-1, dev_tools 39.\n"
        b"`[verified @dea0bc0]`\n"
        b"**Gap:** none -- move to section C.\n"
        b"**Ref:** `provenance_history.py`; `patch_L189_run_history.py`;\n"
        b"`documentation/HANDOFF_20260811_L189_run_history.md`; L-188 (the\n"
        b"staleness caller); L-190; L-184.\n",
    ),
    (
        'L-188 cross-reference',
        b"**Ref:** L-160 (the unrun test file that prompted it); L-184\n"
        b"(build-path push gate, same family); L-189.\n",

        b"**Note (2026-08-11):** L-189 shipped its data half and left the\n"
        b"  staleness check for this item to call. `provenance_history.py`\n"
        b"  exports `is_overdue(history, now)` and `overdue_lines(history)`;\n"
        b"  both are unused at `dea0bc0` and waiting on a caller here. The\n"
        b"  declared cadence is 1 day, compared by calendar date. This makes\n"
        b"  L-188 the trigger and L-189 the data, which is the reason the\n"
        b"  check does not live inside the scanner: a scanner that is running\n"
        b"  cannot report that it did not run.\n"
        b"**Ref:** L-160 (the unrun test file that prompted it); L-184\n"
        b"(build-path push gate, same family); L-189.\n",
    ),
]


def fail(msg):
    print("ERROR: %s" % msg)
    sys.exit(1)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(here, TARGET)

    if not os.path.isfile(target):
        fail("%s not found next to this script. Save this script into the "
             "folder that holds %s." % (TARGET, TARGET))

    with open(target, 'rb') as f:
        data = f.read()

    fingerprint = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
    if fingerprint != BASE_MD5:
        fail("base file has moved.\n"
             "       expected md5 (LF-normalized) %s\n"
             "       found                        %s\n"
             "       Nothing was written. Reconcile before applying."
             % (BASE_MD5, fingerprint))

    is_crlf = data.count(b'\r\n') > 0
    if is_crlf:
        print("note: target uses CRLF; anchors translated to match.")

    patched = data
    for label, old, new in EDITS:
        if is_crlf:
            old = old.replace(b'\n', b'\r\n')
            new = new.replace(b'\n', b'\r\n')
        count = patched.count(old)
        if count != 1:
            print("ANCHOR FAIL (%s): expected 1 match, found %d. "
                  "Nothing written." % (label, count))
            sys.exit(1)
        patched = patched.replace(old, new)
        print("  ok  %s" % label)

    with open(target, 'wb') as f:
        f.write(patched)

    print()
    print("patch applied (%d bytes)" % len(patched))
    print()
    print("NEXT: run ledger_index.py. It regenerates the index tables and")
    print("moves the closed L-189 block into section C. The ledger update")
    print("is not finished until that has run.")


if __name__ == '__main__':
    main()
