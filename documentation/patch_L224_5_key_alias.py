"""
patch_L224_5_key_alias.py

Repairs the one gating checker the L-224 rename turned red.

THE FINDING
    The maintenance run after patch_L224_3 reported:

        Worksheet key round trip -- FAILED (exit 1)
          constants_new.py:195  KEY_STALE: no STREAMER_BELT_RADII
          constants_new.py::STREAMER_BELT_RADII  KEY_STALE
          Aliases installed: 0

    Cause confirmed: STREAMER_BELT_RADII was renamed to
    HELMET_CUSP_RADII on 2026-08-22 (L-224). Eight CODE consumers moved
    with the producer. The key registry is DATA, not code, and did not
    -- so the worksheet pointing at the old key went stale.

WHY AN ALIAS AND NOT AN EDIT
    worksheet_key_aliases.py exists for exactly this and states the
    reason in its own header: the code should be renameable, and the
    WORKSHEET MUST NOT BE EDITED, because a worksheet records what was
    known on its date. Editing one to match today's code is the same
    failure as citing over recalled data. So the evidence stays where
    it was written and the POINTER is repaired in a third place.

    Its rule 1: an entry is added when a checker run reports KEY_STALE
    and a human confirms the cause was a rename. Both have happened --
    the run above, and Tony's rename ruling on 2026-08-22.

    Append only. Nothing here is ever edited or deleted; an alias
    records something that happened, and history does not un-happen.

WHAT IT CHANGES
    worksheet_key_aliases.py -- one entry. Nothing else, anywhere.

HOW TO RUN
    Repo root, VS Code Run. Then re-run the maintenance run: the
    round-trip checker should read 52 sites, 0 unresolved, 1 alias
    installed, and go green. Then commit, push, archive.

Built on ef3e084a37e65f65d1744b716f73008be689e0f8 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written August 22, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = "worksheet_key_aliases.py"
EXPECTED_FP = "99ff33f6cc41615eeb57e736b0b29a47"

OLD = b"ALIASES = {}\n"
NEW = b'''ALIASES = {
    # L-224, 2026-08-22. STREAMER_BELT_RADII = 6.0 became
    # HELMET_CUSP_RADII = 4.0 when the solar streamer belt stopped being
    # a sphere. The rename was the substance of that item, not
    # cosmetic: 6.0 was an unsourced drawing choice sitting above the
    # closed helmet and inside the open stalk, representing neither
    # (L-210). 4.0 is the top of the helmet range Suess & Nerney (2004)
    # states, and it names a CUSP rather than an outer edge.
    #
    # Added in response to a KEY_STALE finding, per rule 1 above: the
    # maintenance run of 2026-08-22 reported the stale key at
    # constants_new.py:195 and on the pinned key, and Tony confirmed
    # the cause was the rename.
    'constants_new.py::STREAMER_BELT_RADII':
        'constants_new.py::HELMET_CUSP_RADII',
}
'''


def main():
    if not os.path.exists(TARGET):
        print("ERROR: %s not found. Run this from the repo root." % TARGET)
        sys.exit(1)
    with open(TARGET, "rb") as f:
        data = f.read()
    fp = hashlib.md5(data.replace(b"\r\n", b"\n")).hexdigest()
    if fp != EXPECTED_FP:
        print("ERROR: BASE MOVED on %s" % TARGET)
        print("  expected %s" % EXPECTED_FP)
        print("  found    %s" % fp)
        print("  Nothing was written. If an alias was already added by")
        print("  hand, this patch is not needed -- check the file.")
        sys.exit(1)
    print("base ok: %s, %d bytes, %s"
          % (TARGET, len(data), "CRLF" if b"\r\n" in data else "LF"))

    if any(b > 127 for b in NEW):
        print("ERROR: inserted text is not ASCII.")
        sys.exit(1)

    crlf = b"\r\n" in data
    o = OLD.replace(b"\n", b"\r\n") if crlf else OLD
    n = NEW.replace(b"\n", b"\r\n") if crlf else NEW
    c = data.count(o)
    if c != 1:
        print("ANCHOR FAIL: expected exactly 1 match for the empty "
              "ALIASES dict, found %d." % c)
        print("  Nothing was written.")
        sys.exit(1)
    with open(TARGET, "wb") as f:
        f.write(data.replace(o, n))
    print("ok   one alias entry appended")

    # ---- evidence, and every check below can fail -------------------
    fails = 0
    import importlib
    sys.path.insert(0, os.getcwd())
    for mod in ("worksheet_key_aliases", "worksheet_keys"):
        if mod in sys.modules:
            del sys.modules[mod]
    try:
        A = importlib.import_module("worksheet_key_aliases")
        got = A.ALIASES.get("constants_new.py::STREAMER_BELT_RADII")
        ok = got == "constants_new.py::HELMET_CUSP_RADII"
        print("  %s  alias imports and maps to the new key"
              % ("PASS" if ok else "FAIL"))
        fails += 0 if ok else 1
        print("  %s  exactly one entry (append-only store, first entry)"
              % ("PASS" if len(A.ALIASES) == 1 else "FAIL"))
        fails += 0 if len(A.ALIASES) == 1 else 1
    except Exception as exc:
        print("  FAIL  alias store does not import: %s" % exc)
        fails += 1

    # The real test: does the OLD key now resolve through the alias to a
    # site that exists? This is what the round-trip checker asks.
    try:
        K = importlib.import_module("worksheet_keys")
        src = {"constants_new.py": open("constants_new.py").read()}
        res, reason = K.resolve("constants_new.py::STREAMER_BELT_RADII", src)
        ok = res is not None
        print("  %s  old key resolves through the alias%s"
              % ("PASS" if ok else "FAIL", "" if ok else " -- %s" % reason))
        fails += 0 if ok else 1
    except Exception as exc:
        print("  FAIL  resolve() raised: %s" % exc)
        fails += 1

    import py_compile
    try:
        py_compile.compile(TARGET, doraise=True)
        print("  PASS  %s compiles" % TARGET)
    except Exception as exc:
        print("  FAIL  %s does not compile: %s" % (TARGET, exc))
        fails += 1

    if fails:
        print("")
        print("ERROR: %d check(s) failed after writing. Revert %s and "
              "report this." % (fails, TARGET))
        sys.exit(1)

    print("")
    print("NEXT: re-run the maintenance run. The round-trip checker")
    print("should report 0 unresolved and 1 alias installed, and 13 of")
    print("13 should pass. Then commit, push, archive this script.")


if __name__ == "__main__":
    main()
