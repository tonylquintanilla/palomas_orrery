"""
patch_L216_1_swap_lock_and_l214_count.py -- close out the session: record the
gallery swap failure and its cause (L-216), and the L-214 label count.

WHAT THIS CHANGES
-----------------
LEDGER_CONSOLIDATED.md only. No code.
  - L-216 opened: the nightly swap fails under a filesystem lock (WinError 5,
    OneDrive), the evidence from both runs, the discard-and-re-run recovery
    rule with the three conditions that make it safe, and the visibility gap
    that comes before any swap fix.
  - L-214 updated with the measurement: 12 of 55 claim sites carry a label the
    request builder cannot read, 9 of them in constants_new.py, and three of
    the five rows still on the reconciliation queue are among them.

RUN IT
------
Save this file into the repo root (the folder holding palomas_orrery.py),
open it in VS Code, and click Run. Or from a terminal in that folder:

    python patch_L216_1_swap_lock_and_l214_count.py

Success: one 'ok' line per edit, then 'patch applied'.
Failure: a single 'ERROR:' or 'ANCHOR FAIL' line. Nothing is written.

AFTER IT RUNS: re-run ledger_index.py (or maintenance_run.py), then archive
this script to documentation/.

PERMANENT vs DISPOSABLE: this script is disposable; the ledger entries are
permanent.

Created August 2026 with Anthropic's Claude Opus 5.

Role: devtool
Domain: dev_tools
"""

import hashlib
import os
import sys


def fingerprint(data):
    """Hash CONTENT, not raw bytes: CRLF and LF copies are the same file."""
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def to_file_eol(chunk, is_crlf):
    """Translate an LF-written anchor into the file's own line endings."""
    return chunk.replace(b'\n', b'\r\n') if is_crlf else chunk


def load(path, expected):
    if not os.path.exists(path):
        print("ERROR: %s not found. Run this script from the repo root "
              "(the folder holding palomas_orrery.py)." % path)
        sys.exit(1)
    with open(path, 'rb') as f:
        data = f.read()
    got = fingerprint(data)
    if got != expected:
        print("ERROR: BASE MOVED for %s" % path)
        print("  expected content fingerprint %s" % expected)
        print("  found                        %s" % got)
        print("  Nothing was written.")
        sys.exit(1)
    print("ok    base confirmed: %s" % path)
    return data


def apply_edits(path, data, edits):
    """edits: (label, old, new, expected_count). Bottom-up order."""
    is_crlf = data.count(b'\r\n') > 0
    for label, old, new, want in edits:
        old_f = to_file_eol(old, is_crlf)
        new_f = to_file_eol(new, is_crlf)
        n = data.count(old_f)
        if n != want:
            print("ANCHOR FAIL in %s: %s -- expected %d match(es), found %d. "
                  "Nothing written." % (path, label, want, n))
            sys.exit(1)
        data = data.replace(old_f, new_f)
        print("ok    %s: %s%s" % (path, label,
                                  " (x%d)" % want if want > 1 else ""))
    return data


def encoding_report(path, data, inserted):
    """Hard-fail on non-ASCII INSERTED; report pre-existing separately."""
    for chunk in inserted:
        bad = [b for b in chunk if b > 127]
        if bad:
            print("ERROR: this patch would insert %d non-ASCII byte(s) into "
                  "%s. Nothing written." % (len(bad), path))
            sys.exit(1)
    left = sum(1 for b in data if b > 127)
    if left:
        print("note: %s still holds %d non-ASCII byte(s) this patch did not "
              "reach" % (path, left))
    else:
        print("note: %s is ASCII-clean" % path)


def write_all(results):
    for path, blob, inserted in results:
        with open(path, 'wb') as f:
            f.write(blob)
        print("patch applied: %s (%d bytes)" % (path, len(blob)))
        encoding_report(path, blob, inserted)


LG = 'LEDGER_CONSOLIDATED.md'
EXPECTED = {'LEDGER_CONSOLIDATED.md': '3cf2f42b73154dc2c252c554a777338c'}
LG_EDITS = [('L-214: the label count, measured', b'**Gap:** unmeasured -- how many rows in the 23-row pilot corpus, and how\nmany across `constants_new.py`, carry a label the builder does not read.\nThat count comes before the design.\n**Ref:** `worksheet_keys.py` `LEG_RE` / `legs_of` / `continues_a_leg`;\nL-209 (the row that exposed it); L-203 (the Visibility Convention);\nL-204; L-207.\n', b'- **COUNTED 2026-08-19 at `d25b5368`, using the project\'s own\n  `collect_claims` and `LEG_RE`.** 12 of 55 claim sites carry a label\n  the builder cannot read; 9 of the 12 are in `constants_new.py`, the\n  others one each in the Mercury, Venus and Moon shell modules.\n- **Two kinds of dropped label, and only one is a defect.** The RECORD\n  legs -- `Cross-checked` (216 lines), `Removed` (18), `Corrected` (16)\n  -- are deliberately invisible to the request, so a second reader\n  cannot see what the last one concluded. That is correct behaviour.\n  What remains after excluding them is almost one label: `Note` at 17\n  lines, plus `HELIOCENTRIC` at 2 and `NOTE` at 2.\n- **The finding that reframes the pilot: THREE of the five rows still\n  on the reconciliation queue are on this list, and in each case the\n  redacted Note is what the responders spent the dispatch\n  rediscovering.**\n  - `STREAMER_BELT_RADII` -- "Visualization cutoff at upper end of 4-6\n    R_sun observed range." The row where the citation was found\n    inverted. No leg was told the value was a drawing choice.\n  - `EARTH_EQUATORIAL_RADIUS_KM` -- "B3 rounds to 6378.1 km; full\n    precision from IERS Conventions." All three legs flagged exactly\n    this by three different routes. The file already said it.\n  - `INNER_CORONA_RADII` -- "Visualization boundary for inner\n    (K-)corona; physical extent 2-3 R_sun." The row where all three\n    legs split on whether a visualization boundary is verdictable at\n    all, which is an open ruling. The file answers it in a line none of\n    them could see.\n- **Two more worth naming.** `HELIOPAUSE_RADII`, the canary row, hides\n  its conversion arithmetic in a Note -- two legs reproduced that\n  arithmetic to the digit rather than reading it. And `HELIOCENTRIC`\n  appears TWICE, on `ALFVEN_SURFACE_RADII` and `PARKER_CLOSEST_RADII`:\n  the same invented label, both times on the origin question that\n  produced L-209.\n- **What the count changes.** Adding `Note` to `CONTEXT_LEGS` is one\n  label and would have altered what three of the pilot\'s hardest rows\n  were checked against. The Visibility Convention still argues for\n  REFUSING on an unrecognised label rather than walking past it\n  silently, since a label nobody reads has no correction path. Widen,\n  refuse, or report-into-the-worksheet remains undecided -- but it is\n  now a design conversation with a measurement under it.\n**Note:** RICE is Claude\'s proposal, unratified.\n**Gap:** the design choice itself. Counting is done; nothing is built.\nRe-dispatching the affected rows after the fix is a separate decision,\nbecause a second dispatch of a row this project has already argued\nabout is not an independent leg.\n**Ref:** `worksheet_keys.py` `LEG_RE` / `legs_of` / `continues_a_leg`;\nL-209 (the row that exposed it); L-203 (the Visibility Convention);\nL-204; L-207; L-210 (three of whose rows this count implicates).\n', 1), ('L-216: opened, gallery swap lock', b'#### [L-215] Ledger cleanup by topic, not by age\n', b"#### [L-216] Gallery swap fails under a filesystem lock (OneDrive)\n<!-- L:216 status:OPEN upd:2026-08-19 section:A flag: rice:3/3/85/2 -->\n- **2026-08-19: the nightly run wiped the served tree.** GitHub Desktop\n  showed 56 deletions in the gallery repo and zero additions.\n  `data/solar-system/` was absent while BOTH halves of the generation\n  survived: `solar-system.prev` (the previous generation) and\n  `.staging_solar-system_20260819T214723Z` (the new one). Nothing was\n  committed and nothing was lost.\n- **The zero-additions reading was an artifact.** The gallery\n  `.gitignore` hides `data/.staging_*/`, `data/solar-system.prev/` and\n  `data/solar-system.quarantine_*/`, so a half-completed swap looks\n  exactly like total loss.\n- **The build was clean; only the swap failed.** Run record\n  `20260819T214723Z.json`: `structural_validation: pass`,\n  `guard_warnings: []`, finished 13.8 s after start. Good data that\n  never landed -- not the guard catching a bad build.\n- **Reproduced the same evening, and it named itself.** A manual re-run\n  printed: `[RECOVER] could not remove retained data\\solar-system.prev\n  ([WinError 5] Access is denied: data\\solar-system.prev\\raw\\elements);\n  swap will quarantine it`. The lock is real and persistent. The repo\n  lives under `C:\\Users\\tonyq\\OneDrive\\...`, and a sync engine holding\n  a handle on a directory is what makes a rename fail.\n- **WHICH rename it catches is the whole difference.** The re-run hit\n  the CLEANUP rmtree, which the code handles by design -- quarantine\n  and carry on -- and the swap completed. The failing run hit\n  `staging -> live`, which has no in-run recovery and leaves the live\n  directory missing. Same cause, different victim.\n- **The pile was the signal all along.** ~30 `solar-system.quarantine_*`\n  directories run back to 2026-07-21, one per night. Each is a run\n  where the retained `.prev` could not be removed. The mechanism has\n  been printing every night for a month and reading as normal, because\n  the builder is built to survive it.\n- **Recovery, and it is the operational rule (Tony, 2026-08-19):** for\n  a cache hiccup, DISCARD the deletions in GitHub Desktop and RE-RUN.\n  Discard restores the live tree from HEAD byte for byte; the re-run\n  builds a fresh generation. Three conditions make it safe and they\n  should travel with the rule: the live tree is committed, the swap is\n  all-or-nothing so a failure leaves a COMPLETE `.prev` or staging and\n  never a mixed one, and nothing reaches the remote until Tony commits.\n  Running with `--commit` would break the third.\n- **The visibility gap, and it comes BEFORE the swap fix.** The run\n  record is written INSIDE the generation, so a run whose swap fails\n  strands its own record in a directory `.gitignore` hides. The\n  committed history will show the 18th, the 19th 23:10 run, and no sign\n  that a run in between lost its data. The swap OUTCOME needs recording\n  outside the generation, or every recurrence costs another evening of\n  inference. Same Visibility Convention shape as L-214, one layer out.\n- **Then the cause.** Retry the renames with backoff if the lock is\n  transient at the moment of the swap, or move the repo off OneDrive if\n  it is not. WinError 5 on the cleanup proves persistence at run START;\n  it does not prove the swap window is equally exposed.\n- **Tony-action (do):** the operational rule above belongs in\n  `gallery-cache-builder`, which would be 1.4. NOT bumped tonight:\n  `ledger-and-session-records` went to 1.7 today and that reinstall is\n  unverified from inside this session. Discharge that first, then bump\n  this one. Same pattern as the dispatch-hygiene rule on 2026-08-19.\n**Note:** RICE is Claude's proposal, unratified.\n**Gap:** unmeasured -- whether the `staging -> live` rename is exposed\nto the same lock as the cleanup, or was unlucky once. One data point.\n**Ref:** `tools/gallery_cache_builder.py` `atomic_swap_dir` (~1176),\n`recover_incomplete_swap` (~1223), `_sweep_siblings` (~1241) in the\ngallery repo; run records `20260819T214723Z.json` (failed) and\n`20260819T231042Z.json` (recovered); gallery at `8a4aa41`; L-098 (the\nbuilder); L-214 (the same visibility shape).\n\n#### [L-215] Ledger cleanup by topic, not by age\n", 1)]


def main():
    lg = load(LG, EXPECTED[LG])
    lg = apply_edits(LG, lg, LG_EDITS)
    write_all([(LG, lg, [e[2] for e in LG_EDITS])])
    print("")
    print("Next: ledger_index.py, then archive this script to documentation/.")


if __name__ == '__main__':
    main()
