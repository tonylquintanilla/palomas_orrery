"""patch_L305_brief.py -- L-305: the brief for the paper-read session.

ORRERY repo (palomas_orrery). Built on orrery 5fea1795 AS PATCHED BY
patch_L310_ledger.py -- run that one first; this script's fingerprint
is of the ledger after it.

Run: save this file in the orrery repo root (beside LEDGER_CONSOLIDATED.md),
open it in VS Code, click Run.  Or from a terminal in the repo root:
    python patch_L305_brief.py

What it does, all-or-nothing:
  LEDGER_CONSOLIDATED.md  -- L-305 gains one bullet: what the paper-read
                             session must bring back, so it opens targeted.
                             upd: stamp moves to 2026-09-10. The header
                             stamp from patch_L310_ledger.py is extended to
                             name this. Then run ledger_index.py.

Permanent: the ledger text. Disposable: this script.
Success prints one 'ok' per edit and 'patch applied'. Any failure prints one
ERROR / ANCHOR FAIL line and writes nothing.

Written September 10, 2026 with Anthropic's Claude Fable 5.1.
"""
import hashlib, os, sys

LEDGER = "LEDGER_CONSOLIDATED.md"
LEDGER_MD5 = "83cfc0c27227a15c7a5dca03369f4448"

EDITS = [
# 1. extend the header stamp written by patch_L310_ledger.py
(b"""(L-310 design ruled and built; L-313 opened), built on 5fea1795.""",
b"""(L-310 design ruled and built; L-313 opened; L-305 paper-read brief),
built on 5fea1795."""),
# 2. upd stamp on L-305
(b"""<!-- L:305 status:OPEN upd:2026-09-08 section:A flag: rice:4/4/60/4 -->""",
b"""<!-- L:305 status:OPEN upd:2026-09-10 section:A flag: rice:4/4/60/4 -->"""),
# 3. the brief, inserted above the Gap
(b"""**Gap:** fetch Jelinek et al. 2012 and read its fitted parameters from
the paper;""",
b"""- **Brief for the paper-read session (2026-09-10, written from the
  phone with no paper open; nothing below is a value).** The read is
  one job done in one stretch, on a model with the context to hold the
  whole paper, and it comes back with all of the following or it is
  not done:
  1. The magnetopause and bow shock surface equations exactly as the
     paper states them, with the paper's own symbol names.
  2. Every fitted coefficient with the table or equation number it was
     read from, including the flaring parameter and what it was fitted
     against.
  3. The solar wind inputs the model expects (dynamic pressure, IMF
     Bz, any others), and for each one either a served value with its
     own source or a stated fixed value with its source -- the exhibit
     draws one state, and that state has to be named.
  4. The validity range the authors state, so the hover can say where
     the drawn surface stops being the model.
  5. The magnetotail extent, which is NOT in this paper: a separate
     citation, or the tail drawn to a stated range with the gap named.
  6. The full reference with DOI, fetched from the paper itself, not
     recalled. (The session that wrote this brief recalls the paper as
     J. Geophys. Res. 2012 by Jelinek, Nemecek and Safrankova; treat
     that as a search key, not a citation.)
  Each of 1-6 lands in the ledger with a [verified @<sha>] tag before
  any renderer is touched; the constants go to `constants_new.py`
  under provenance-discipline 2.11 and A Drawing Approximation Does
  Not Promote.
**Gap:** fetch Jelinek et al. 2012 and read its fitted parameters from
the paper;"""),
]


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    fn = os.path.join(root, LEDGER)
    if not os.path.exists(fn):
        print("ERROR: not found: %s (run from the orrery repo root)" % fn); return 1
    with open(fn, "rb") as f:
        content = f.read()
    got = hashlib.md5(content).hexdigest()
    if got != LEDGER_MD5:
        print("ERROR: %s fingerprint %s, expected %s -- run patch_L310_ledger.py first, "
              "or this is already applied; nothing written" % (LEDGER, got, LEDGER_MD5)); return 1
    for i, (old, new) in enumerate(EDITS, 1):
        n = content.count(old)
        if n != 1:
            print("ANCHOR FAIL: %s edit %d expected 1 match, got %d: %r" % (LEDGER, i, n, old[:60]))
            return 1
        content = content.replace(old, new)
        print("ok  %s edit %d" % (LEDGER, i))
    with open(fn, "wb") as f:
        f.write(content)
    print("stamped header: %s" % LEDGER)
    print("patch applied (%d bytes)" % len(content))
    print("next: run ledger_index.py to rebuild the index zone")
    return 0


if __name__ == "__main__":
    sys.exit(main())
