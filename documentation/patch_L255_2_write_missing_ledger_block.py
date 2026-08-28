"""
patch_L255_2_write_missing_ledger_block.py

Writes the L-255 DETAIL block, which was never created.

Built on palomas_orrery @ a263f73d473bd2cd9de8241372ee9d1885045d04
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Confirmed against the live remote 2026-08-28.

WHY THIS EXISTS
  `patch_L255_1_skill_bumps_and_protocol_entry.py` RESERVED the handle
  L-255 and ran successfully on 2026-08-26. The protocol's v3.44 entry
  cites it. The ledger never received a block, so for two days the
  handle existed in two documents and in a patch filename while the
  status authority said nothing about it.

  Same shape as the L-225 gap the master plan recorded on 2026-08-23.
  One row per class, so this patch closes the instance and L-256's
  reference records the class.

STATUS IS DONE, NOT OPEN
  Every deliverable was verified present at HEAD before this block was
  written -- not inferred from the patch script's own report:

    provenance-discipline           2.7 landed (now 2.8 under L-256)
    orrery-coding-conventions       1.6 at HEAD
    PROJECT_INSTRUCTIONS.md         v3.44 entry resident
    PROJECT_INSTRUCTIONS_HISTORY    v3.41 present, once
    patch script                    archived in documentation/

ONE FILE, ONE EDIT.
  The block is placed in `## C. RECONCILED LEDGER`, which is where a
  DONE item belongs. The INDEX is NOT touched -- it is generated. Run
  ledger_index.py afterwards.

SAFETY
  MD5 guard computed after normalizing line endings; anchor asserted
  unique; post-conditions checked before the single write; original
  line-ending style preserved; .bak written beside the file.

HOW TO RUN
  Open in VS Code and press Run, with the repo root as the working
  directory. No arguments, no prompts.

Module updated: August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import shutil
import sys

TARGET = "LEDGER_CONSOLIDATED.md"
EXPECTED_MD5 = "7643743be25e0d6483362ca670f796ae"
BASE_SHA = "a263f73d473bd2cd9de8241372ee9d1885045d04"

ANCHOR = "#### [L-217] The Part A / Part B dispatch split is a check that cannot fail\n"

BLOCK = """#### [L-255] Skill bumps of 2026-08-26 -- handle reserved, block never written
<!-- L:255 status:DONE upd:2026-08-28 section:C flag: rice:2/3/40/1 -->
- **What the handle covers.** The two skill bumps and the protocol
  version entry delivered by
  `patch_L255_1_skill_bumps_and_protocol_entry.py` on 2026-08-26, run
  the same evening. Four files, all-or-nothing:
  `provenance-discipline` 2.6 -> 2.7, `orrery-coding-conventions`
  1.5 -> 1.6, `PROJECT_INSTRUCTIONS.md` to v3.44 with v3.41 moving out,
  and `PROJECT_INSTRUCTIONS_HISTORY.md` receiving it.
- **provenance-discipline 2.7 -- three sections, all gaps rather than
  refinements.** One Value, One Home [CRITICAL] states positively what
  No Shadow Constants only prohibited, with its scope boundary in the
  same breath: measured values migrate to `constants_new.py`, declared
  drawing parameters do not. Report to the Figures You Have [QUALITY]
  had no home in any skill -- compute at full precision, report to the
  figures the least precise input supports. A Breadcrumb Must Not Cite
  [CRITICAL] records that a `# Ref:` line or bare URL inside the
  thirty-line lookback becomes a citation for the unit beside it, so an
  honest pending-sourcing note carries a ledger handle and nothing else
  (L-253).
- **orrery-coding-conventions 1.6.** Marker Separation for Near-Equal
  Radii keeps its rule and loses its fixed number: the angular step is
  an OUTCOME, readable separation at the scale the family renders at,
  with 20 degrees for the solar skin stack and 10 for Earth's crust as
  the two worked cases. The required step depends on frame width and
  frame width depends on which shells are enabled, so one global number
  was always going to be wrong somewhere.
- **Verified at `a263f73d`, not inferred from the patch's own report.**
  `orrery-coding-conventions` reads 1.6; the v3.44 entry is resident;
  v3.41 appears once, in history; the patch script is archived in
  `documentation/`. `provenance-discipline` reads 2.8 rather than 2.7
  because L-256 bumped it again on 2026-08-27 -- the 2.7 content is
  present and intact beneath it.
- **The failure this row records is the ledger gap itself.** The handle
  was reserved by a patch filename and cited in the protocol's version
  entry, and the status authority carried nothing. The plan carries
  SEQUENCING authority and the ledger carries STATUS authority (L-221),
  so a handle living only in a plan or a filename is unfindable by the
  document that is supposed to answer for it. Detected 2026-08-28 by a
  patch that printed the gap rather than filling it blind.
- **Why a handle can be reserved before its row exists.** A patch is
  named for its handle before it runs, and the row is normally written
  in the same session. Here the session ended at the push. The fourth
  link of L-230's chain fired; the ledger row is a fifth step nobody
  had named.
**Ref:** L-230 (the four-link skill-bump chain); L-253 (A Breadcrumb
Must Not Cite); L-249 (the Earth interior build this session served);
L-256 (the 2.8 bump, which records this gap as a class); L-225 (the
same shape, recorded in the master plan 2026-08-23).

"""


def main():
    if not os.path.isfile(TARGET):
        print("FAIL: %s not found. Run this from the repository root."
              % TARGET)
        return 1

    raw = open(TARGET, "rb").read()
    had_crlf = b"\r\n" in raw
    norm = raw.replace(b"\r\n", b"\n")

    got = hashlib.md5(norm).hexdigest()
    if got != EXPECTED_MD5:
        print("FAIL: fingerprint mismatch. Nothing was written.")
        print("  expected: %s" % EXPECTED_MD5)
        print("  actual:   %s" % got)
        print("Re-pull LEDGER_CONSOLIDATED.md at %s." % BASE_SHA[:8])
        print("If you have run ledger_index.py since the last commit, the")
        print("INDEX zone will have been rewritten and this guard will")
        print("refuse -- commit that first, then re-cut this patch.")
        return 1

    try:
        text = norm.decode("ascii")
    except UnicodeDecodeError as exc:
        print("FAIL: target is not pure ASCII (%s)." % exc)
        return 1

    print("Fingerprint OK. %d lines, %s on disk."
          % (text.count("\n"), "CRLF" if had_crlf else "LF"))

    if "L:255" in text:
        print("FAIL: an L-255 block already exists. Nothing was written.")
        return 1

    n = text.count(ANCHOR)
    if n != 1:
        print("FAIL: anchor appears %d times (need exactly 1)." % n)
        return 1

    lines0 = text.count("\n")
    text = text.replace(ANCHOR, BLOCK + ANCHOR, 1)

    checks = [
        ("L-255 block present", "#### [L-255]" in text),
        ("index comment well-formed",
         "<!-- L:255 status:DONE upd:2026-08-28 section:C" in text),
        ("placed inside the reconciled section",
         text.index("## C. RECONCILED LEDGER") < text.index("#### [L-255]")),
        ("L-217 block still intact", "#### [L-217]" in text),
        ("INDEX zone untouched", text.count("## INDEX (generated") == 1),
        ("pure ASCII", all(ord(c) < 128 for c in text)),
    ]

    print("")
    failed = [n2 for n2, ok in checks if not ok]
    for name, ok in checks:
        print("  %-42s %s" % (name, "OK" if ok else "FAIL"))
    if failed:
        print("\nFAIL: %d post-condition(s) failed. Nothing was written."
              % len(failed))
        return 1

    shutil.copy2(TARGET, TARGET + ".bak")
    out = text.encode("ascii")
    if had_crlf:
        out = out.replace(b"\n", b"\r\n")
    with open(TARGET, "wb") as fh:
        fh.write(out)

    print("\nWROTE %s  (%d -> %d lines)" % (TARGET, lines0, text.count("\n")))
    print("  backup: %s.bak" % TARGET)
    print("")
    print("NEXT: run ledger_index.py, then maintenance_run.py, then")
    print("      commit and push and confirm the remote HEAD.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
