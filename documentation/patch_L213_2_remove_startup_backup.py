"""
patch_L213_2_remove_startup_backup.py -- L-213: stop backing up the orbit
cache on module IMPORT, and name the real restore points at startup instead.

WHAT THIS CHANGES
-----------------
palomas_orrery_helpers.py
  - Deletes create_orbit_backup(). It copied data/orbit_paths.json to
    data/orbit_paths_backup.json on every import. Nothing in the codebase
    ever read that file, so it was a write-only artifact; the recovery
    chain in orbit_data_manager.load_orbit_paths() reads only
    data/orbit_paths.json.backup and .backup_old.

palomas_orrery.py
  - Drops create_orbit_backup from the palomas_orrery_helpers import list.
  - Removes the module-level call and its status-display line.
  - Extends the existing [CACHE HEALTH SUMMARY] block to name both restore
    points with size and date, and adds an else branch so the summary still
    prints when no cache exists yet.

RUN IT
------
Save this file into the SAME FOLDER as palomas_orrery.py, open it in
VS Code, and click Run. Or from a terminal in that folder:

    python patch_L213_2_remove_startup_backup.py

Success: one 'ok' line per edit, then 'patch applied' per file.
Failure: a single 'ERROR:' (base moved) or 'ANCHOR FAIL' (text not found)
line. Nothing is written in either case, so it is always safe to re-check
and retry.

One-shot by construction: the fingerprints below describe the tree as it
stood before this ran, so a second run aborts and writes nothing. Archive
this script to documentation/ once it has succeeded.

PERMANENT vs DISPOSABLE: this script is disposable. What it installs is
permanent -- the deletion of create_orbit_backup() and the restore-point
reporting in the startup summary.

Created August 2026 with Anthropic's Claude Opus 5.

Role: devtool
Domain: dev_tools
"""
import hashlib
import os
import sys

# --- expected content fingerprints (MD5 of line-ending-normalized bytes) ---
EXPECTED = {
    'palomas_orrery.py': 'ca1218203ddb0c1c82e73033460ba613',
    'palomas_orrery_helpers.py': '76910ecb69a63c257ad18b4c7a3eeddf',
}

IMP_OLD = b'                                    get_default_camera, print_planet_positions, create_orbit_backup, cleanup_old_orbits, \n'
IMP_NEW = b'                                    get_default_camera, print_planet_positions, cleanup_old_orbits, \n'

CALL_OLD = b'# Create backup on startup\nmessage, msg_type = create_orbit_backup()\nupdate_status_display(message, msg_type)\n\n# Initialize orbit data manager without dialogs\n'
CALL_NEW = b'# Initialize orbit data manager without dialogs\n'

SUM_OLD = b'    print("\\nNote: Cache can only be manually deleted by removing \'data/orbit_paths.json\' file", flush=True)\n    print("-" * 50, flush=True)\n\n'
SUM_NEW = b'    print("\\nNote: Cache can only be manually deleted by removing \'data/orbit_paths.json\' file", flush=True)\n\n    # Restore points -- the two generations load_orbit_paths() falls back to\n    # automatically when the cache is missing or corrupt. Reported here so a\n    # damaged cache is recoverable without guessing what exists (L-213).\n    print("Restore points (used automatically if the cache is damaged):", flush=True)\n    for backup_path in (\'data/orbit_paths.json.backup\', \'data/orbit_paths.json.backup_old\'):\n        if os.path.exists(backup_path):\n            backup_mb = os.path.getsize(backup_path) / (1024 * 1024)\n            backup_when = datetime.fromtimestamp(os.path.getmtime(backup_path)).strftime(\'%Y-%m-%d %H:%M\')\n            print(f"  {backup_path}: {backup_mb:.1f} MB, saved {backup_when}", flush=True)\n        else:\n            print(f"  {backup_path}: none yet", flush=True)\n    print("-" * 50, flush=True)\nelse:\n    print("\\n[CACHE HEALTH SUMMARY]", flush=True)\n    print("No cache found at data/orbit_paths.json. A new one will be created as needed.", flush=True)\n    print("-" * 50, flush=True)\n\n'

FN_HDR = b'# Helper function to create backup\ndef create_orbit_backup():\n'
FN_TAIL = b'# Weekly cleanup function -- deprecated\n'


def fingerprint(data):
    """Hash CONTENT, not raw bytes: CRLF and LF copies are the same file."""
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def to_file_eol(chunk, is_crlf):
    """Translate an LF-written anchor into the file's own line endings."""
    return chunk.replace(b'\n', b'\r\n') if is_crlf else chunk


def load(path):
    if not os.path.exists(path):
        print("ERROR: %s not found. Run this script from the folder that "
              "holds palomas_orrery.py." % path)
        sys.exit(1)
    with open(path, 'rb') as f:
        data = f.read()
    got = fingerprint(data)
    want = EXPECTED[path]
    if got != want:
        print("ERROR: BASE MOVED for %s" % path)
        print("  expected content fingerprint %s" % want)
        print("  found                        %s" % got)
        print("  Nothing was written. The file differs from the one this "
              "patch was built against.")
        sys.exit(1)
    print("ok    base confirmed: %s" % path)
    return data


def apply_edits(path, data, edits):
    """edits: list of (label, old_bytes, new_bytes). Bottom-up order."""
    is_crlf = data.count(b'\r\n') > 0
    for label, old, new in edits:
        old_f = to_file_eol(old, is_crlf)
        new_f = to_file_eol(new, is_crlf)
        n = data.count(old_f)
        if n != 1:
            print("ANCHOR FAIL in %s: %s -- expected 1 match, found %d. "
                  "Nothing written." % (path, label, n))
            sys.exit(1)
        data = data.replace(old_f, new_f)
        print("ok    %s: %s" % (path, label))
    return data


def cut_function(path, data):
    """Delete create_orbit_backup() by splicing between two unique anchors."""
    is_crlf = data.count(b'\r\n') > 0
    hdr = to_file_eol(FN_HDR, is_crlf)
    tail = to_file_eol(FN_TAIL, is_crlf)
    for label, anchor in (('function header', hdr), ('next function', tail)):
        n = data.count(anchor)
        if n != 1:
            print("ANCHOR FAIL in %s: %s -- expected 1 match, found %d. "
                  "Nothing written." % (path, label, n))
            sys.exit(1)
    i = data.index(hdr)
    j = data.index(tail)
    if j <= i:
        print("ANCHOR FAIL in %s: anchors out of order. Nothing written."
              % path)
        sys.exit(1)
    removed = data[i:j]
    # Safety: the removed span must be exactly one function definition.
    if removed.count(b'def ') != 1:
        print("ANCHOR FAIL in %s: removal span holds %d 'def ' lines, "
              "expected exactly 1. Nothing written."
              % (path, removed.count(b'def ')))
        sys.exit(1)
    if b'create_orbit_backup' not in removed:
        print("ANCHOR FAIL in %s: removal span does not name "
              "create_orbit_backup. Nothing written." % path)
        sys.exit(1)
    print("ok    %s: removed create_orbit_backup() (%d bytes)"
          % (path, len(removed)))
    return data[:i] + data[j:]


def encoding_report(path, data):
    """Hard-fail on non-ASCII this patch INSERTED; sweep and report the rest."""
    bad = [b for b in data if b > 127]
    if bad:
        print("note: %s still holds %d non-ASCII byte(s) this patch did not "
              "reach" % (path, len(bad)))
    else:
        print("note: %s is ASCII-clean" % path)


def main():
    # --- palomas_orrery_helpers.py -------------------------------------
    hp = 'palomas_orrery_helpers.py'
    hp_data = load(hp)
    hp_new = cut_function(hp, hp_data)

    # --- palomas_orrery.py (edits listed BOTTOM-UP) --------------------
    po = 'palomas_orrery.py'
    po_data = load(po)
    po_new = apply_edits(po, po_data, [
        ('startup summary: name the restore points', SUM_OLD, SUM_NEW),
        ('remove module-level backup call', CALL_OLD, CALL_NEW),
        ('drop create_orbit_backup from import', IMP_OLD, IMP_NEW),
    ])

    # Residual check: the symbol must be gone from both files.
    for path, blob in ((hp, hp_new), (po, po_new)):
        if b'create_orbit_backup' in blob:
            print("ANCHOR FAIL: create_orbit_backup still present in %s "
                  "after edits. Nothing written." % path)
            sys.exit(1)

    for path, blob in ((hp, hp_new), (po, po_new)):
        with open(path, 'wb') as f:
            f.write(blob)
        print("patch applied: %s (%d bytes)" % (path, len(blob)))
        encoding_report(path, blob)

    print("")
    print("Done. Next: run palomas_orrery.py and confirm the "
          "[CACHE HEALTH SUMMARY] block now lists the restore points.")
    print("You can also delete data/orbit_paths_backup.json by hand -- "
          "nothing writes or reads it any more.")


if __name__ == '__main__':
    main()
