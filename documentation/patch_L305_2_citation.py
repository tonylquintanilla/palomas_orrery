"""patch_L305_2_citation.py -- L-305: the paper's fetched reference and access point.

ORRERY repo (palomas_orrery). Run AFTER patch_L305_brief.py; the
fingerprint is of the ledger after it. Built on orrery 5fea1795.

Run: save in the orrery repo root, open in VS Code, click Run.  Or:
    python patch_L305_2_citation.py

One edit: item 6 of the L-305 paper-read brief gets the reference as
found by a web search on 2026-09-10 (DOI, journal, article number,
page count, URL, free access) so the next session opens the paper
instead of finding it. Search-result metadata, not a read of the
paper: the values inside stay to be read.

Written September 10, 2026 with Anthropic's Claude Fable 5.1.
"""
import hashlib, os, sys
LEDGER = "LEDGER_CONSOLIDATED.md"
LEDGER_MD5 = "7ab70e1aaa9131025c11b50f21bc5f3a"
OLD = b"""  6. The full reference with DOI, fetched from the paper itself, not
     recalled. (The session that wrote this brief recalls the paper as
     J. Geophys. Res. 2012 by Jelinek, Nemecek and Safrankova; treat
     that as a search key, not a citation.)"""
NEW = b"""  6. The full reference with DOI, confirmed against the paper itself.
     Found by web search 2026-09-10 (search-result metadata, not a
     read of the paper): Jelinek, K., Z. Nemecek, and J. Safrankova
     (2012), A new approach to magnetopause and bow shock modeling
     based on automated region identification, J. Geophys. Res., 117,
     A05208, 8 pages, doi:10.1029/2011JA017252. Free access at
     https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2011JA017252
     -- fetch that URL to start the read. One citing paper describes
     the model as a paraboloid of revolution; that is a hint for item
     1, not a value."""
def main():
    fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), LEDGER)
    if not os.path.exists(fn):
        print("ERROR: not found: %s (run from the orrery repo root)" % fn); return 1
    with open(fn, "rb") as f: content = f.read()
    got = hashlib.md5(content).hexdigest()
    if got != LEDGER_MD5:
        print("ERROR: fingerprint %s, expected %s -- run patch_L305_brief.py first, or already applied; nothing written" % (got, LEDGER_MD5)); return 1
    n = content.count(OLD)
    if n != 1:
        print("ANCHOR FAIL: expected 1 match, got %d" % n); return 1
    content = content.replace(OLD, NEW)
    with open(fn, "wb") as f: f.write(content)
    print("ok  %s edit 1" % LEDGER); print("patch applied (%d bytes)" % len(content))
    print("next: run ledger_index.py"); return 0
if __name__ == "__main__": sys.exit(main())
