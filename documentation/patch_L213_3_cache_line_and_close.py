"""
patch_L213_3_cache_line_and_close.py -- L-213 follow-on: print the live orbit
cache alongside its two restore points, and close L-213 in the ledger.

WHAT THIS CHANGES
-----------------
palomas_orrery.py
  - The startup restore-point block now lists data/orbit_paths.json itself
    first, then .backup and .backup_old. save_orbit_paths() copies with
    shutil.copy2, which preserves mtime, so each printed date is when that
    CONTENT was written, not when the copy was taken. Without the live
    cache on screen, two old backup dates cannot be told apart from a
    healthy cache nobody has written to lately. The label changes from
    "saved" to "written" for the same reason.

LEDGER_CONSOLIDATED.md
  - L-213 moves to DONE / section C, with the as-built record, the
    corrected risk statement, and the module-level __main__ finding.

RUN IT
------
Save this file into the repo root (the folder holding palomas_orrery.py),
open it in VS Code, and click Run. Or from a terminal in that folder:

    python patch_L213_3_cache_line_and_close.py

Success: one 'ok' line per edit, then 'patch applied' per file.
Failure: a single 'ERROR:' (base moved) or 'ANCHOR FAIL' line. Nothing is
written in either case.

AFTER IT RUNS: re-run ledger_index.py so the INDEX table picks up the
DONE status, then archive this script to documentation/.

PERMANENT vs DISPOSABLE: this script is disposable. The startup block and
the ledger entry are permanent.

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


PO = 'palomas_orrery.py'
LG = 'LEDGER_CONSOLIDATED.md'

EXPECTED = {
    PO: '3afd26d9a1e7df5bfc75e4f7838b82d6',
    LG: 'a5696711c7a71cbd0079d52011eb9478',
}

PO_OLD = b'    print("Restore points (used automatically if the cache is damaged):", flush=True)\n    for backup_path in (\'data/orbit_paths.json.backup\', \'data/orbit_paths.json.backup_old\'):\n        if os.path.exists(backup_path):\n            backup_mb = os.path.getsize(backup_path) / (1024 * 1024)\n            backup_when = datetime.fromtimestamp(os.path.getmtime(backup_path)).strftime(\'%Y-%m-%d %H:%M\')\n            print(f"  {backup_path}: {backup_mb:.1f} MB, saved {backup_when}", flush=True)\n        else:\n            print(f"  {backup_path}: none yet", flush=True)\n'
PO_NEW = b'    # Cache and its two restore points, newest first. save_orbit_paths()\n    # copies with shutil.copy2, which PRESERVES mtime, so each date is when\n    # that CONTENT was written rather than when the copy was taken: the live\n    # cache carries the last save, .backup the save before it, .backup_old\n    # the one before that. Printing all three together is what makes a\n    # stalled rotation visible -- two old backup dates alone cannot be told\n    # apart from a healthy cache nobody has written to lately (L-213).\n    print("Cache and restore points (date = when that content was written):", flush=True)\n    for cache_path in (\'data/orbit_paths.json\',\n                       \'data/orbit_paths.json.backup\',\n                       \'data/orbit_paths.json.backup_old\'):\n        if os.path.exists(cache_path):\n            cache_mb = os.path.getsize(cache_path) / (1024 * 1024)\n            cache_when = datetime.fromtimestamp(os.path.getmtime(cache_path)).strftime(\'%Y-%m-%d %H:%M\')\n            print(f"  {cache_path}: {cache_mb:.1f} MB, written {cache_when}", flush=True)\n        else:\n            print(f"  {cache_path}: none yet", flush=True)\n'
LG_META_OLD = b'<!-- L:213 status:OPEN upd:2026-08-19 section:A flag: rice:2/3/75/2 -->\n'
LG_META_NEW = b'<!-- L:213 status:DONE upd:2026-08-19 section:C flag: rice:2/3/75/2 -->\n'
LG_TAIL_OLD = b"**Note:** RICE is Claude's proposal, unratified.\n**Gap:** unmeasured -- how large the cache is, how often it is written\nin a session, and whether any other module-level side effect in\n`palomas_orrery.py` fires on the same import. The third question is\nthe one worth asking early, because a module-level call that runs\nduring a test suite is a pattern rather than an instance.\n**Ref:** L-212 (the block that surfaced it); `palomas_orrery.py:3649`;\n`palomas_orrery_helpers.py:791`; `test_reset_completeness.py:39`.\n"
LG_TAIL_NEW = b'- **As built** (`patch_L213_2_remove_startup_backup.py`, run 2026-08-19;\n  pushed at `81108b2f`). `create_orbit_backup()` deleted from\n  `palomas_orrery_helpers.py`, its module-level call and import removed\n  from `palomas_orrery.py`, and the startup summary extended to name the\n  restore points. `data/orbit_paths_backup.json` deleted by hand.\n- **The risk statement above was WRONG, and the correction is the point\n  of this entry.** It said a corrupted cache would overwrite the good\n  backup on the next import. That file was never a recovery source.\n  `load_orbit_paths()` reads `data/orbit_paths.json.backup` and\n  `.backup_old` and nothing else; a repo-wide grep found the only\n  mentions of `orbit_paths_backup.json` were the two lines that wrote\n  it. So the defect was a pointless write of a file no code read, not a\n  live threat to recovery.\n- **The repair L-213 called "the real one" already existed.**\n  `save_orbit_paths()` writes through a temp file, re-reads it to confirm\n  the JSON parses, rotates `.backup` into `.backup_old`, copies the\n  current cache to `.backup`, and refuses any save that shrinks the cache\n  by more than 5 percent. Moving the import-time copy next to the write\n  would have added a third copy of a job already done twice. Tony\'s\n  ruling, 2026-08-19: two files, not three, and delete the odd one.\n- **Mode 5 confirmed** on the launch log of 2026-08-19: 1,501 orbits\n  loaded, both restore points printed, no `[STARTUP]` backup line, no\n  file written.\n- **The fix\'s own output then exposed a second defect, in the block this\n  item added.** The two restore points read 130.4 MB dated August 5 and\n  August 4, which looks two weeks stale and is not. `shutil.copy2`\n  preserves mtime, so a backup\'s date is when its CONTENT was written,\n  not when the copy was taken -- `.backup` carries the previous save,\n  `.backup_old` the one before that, and the most recent save\'s date\n  lives only on the live cache, which the block did not print. Two\n  readings fitted the same screen: no cache write in two weeks\n  (expected during provenance work) or writes happening without\n  rotation (a defect). Fixed by `patch_L213_3_cache_line_and_close.py`,\n  which prints the live cache alongside its two restore points and\n  relabels the timestamp. Success now carries evidence: three dates read\n  as a sequence and a stalled rotation announces itself.\n- **The module-level answer to the Gap question.** `palomas_orrery.py`\n  has no `if __name__ == "__main__"` guard anywhere -- the whole file\n  runs on import, including the working-directory change and\n  `root.mainloop()`. `test_reset_completeness.py` survives that only by\n  replacing `tk.Misc.mainloop` with a no-op before importing.\n  `create_orbit_backup()` was the ONLY module-level statement that wrote\n  into `data/`. The missing guard is a separate problem and is NOT\n  closed by this item.\n**Note:** RICE is Claude\'s proposal, unratified.\n**Gap:** the missing `__main__` guard, deliberately left open (see the\nlast bullet). Not opened as its own item pending Tony\'s call on whether\nit is worth the startup-behaviour change to the GUI and the tests.\n**Ref:** L-212 (the block that surfaced it); `orbit_data_manager.py`\n`save_orbit_paths` / `load_orbit_paths` (the real backup chain);\n`documentation/patch_L213_2_remove_startup_backup.py`;\n`documentation/patch_L213_3_cache_line_and_close.py`.\n'


def main():
    po = load(PO, EXPECTED[PO])
    po = apply_edits(PO, po, [
        ('startup block: list the live cache with its restore points',
         PO_OLD, PO_NEW, 1),
    ])

    lg = load(LG, EXPECTED[LG])
    lg = apply_edits(LG, lg, [
        ('L-213: as-built record and corrected risk statement',
         LG_TAIL_OLD, LG_TAIL_NEW, 1),
        ('L-213: status OPEN -> DONE, section A -> C',
         LG_META_OLD, LG_META_NEW, 1),
    ])

    write_all([
        (PO, po, [PO_NEW]),
        (LG, lg, [LG_META_NEW, LG_TAIL_NEW]),
    ])
    print("")
    print("Next: run ledger_index.py, then archive this script to "
          "documentation/.")


if __name__ == '__main__':
    main()
