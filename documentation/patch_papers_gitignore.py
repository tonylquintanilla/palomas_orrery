"""patch_papers_gitignore.py -- a local-only papers/ folder beside
documentation/, ignored by git so nothing in it is ever pushed.

ORRERY repo (palomas_orrery). Built on orrery 297dec69 at
https://github.com/tonylquintanilla/palomas_orrery

Run: save this file in the orrery repo root (beside .gitignore), open it
in VS Code, click Run.  Or from a terminal in the repo root:
    python patch_papers_gitignore.py

Why: the repo is public, so a journal PDF committed to documentation/ is
downloadable by anyone, and reposting a publisher's PDF is usually not
allowed even when the article is free to read. The Jelinek 2012 paper was
committed there on 2026-09-10.

What it does, all-or-nothing:
  .gitignore   gains a /papers/ rule with a comment saying why. The one
               non-ASCII character already in it (an em dash in the orbit
               cache comment) becomes "--" in passing.
  papers/      created, empty, if it is not already there. Git never
               tracks it, so it exists on this machine only.

It does NOT move any PDF. After running it:
  - In File Explorer, move the PDFs you want kept out of documentation/
    and into papers/. GitHub Desktop will list them as deleted; that is
    correct -- the copies in papers/ are untouched and stay local.
  - Commit and push. The files leave the current repo; they remain in its
    history, which is usually enough for a paper, but anything holding a
    key should have the key replaced.

Guard: .gitignore's text, line endings normalised, must match orrery
297dec69. Its Windows line endings are kept.

Permanent: the .gitignore rule and the folder. Disposable: this script.
Success prints one 'ok' per step and 'patch applied'. Any failure prints
one ERROR / ANCHOR FAIL line and writes nothing.
Undo is Discard Changes in GitHub Desktop.

Written September 10, 2026 with Anthropic's Claude Opus 5.
"""
import hashlib, os, sys

REL = ".gitignore"
EXPECTED = "3f3bc20b7e9de04ae83388a7e5cb7d1b"

EMDASH_OLD = b"# Orbit cache (local desktop data \xe2\x80\x94 web-served via separate data repo)"
EMDASH_NEW = b"# Orbit cache (local desktop data -- web-served via separate data repo)"

RULE = b"""
# Local-only reference papers, never pushed (2026-09-10). This repo is
# public, and a journal's PDF may not be reposted even when the article
# is free to read. Keep papers in papers/ beside documentation/; git
# leaves the folder and everything in it out of every commit. A session
# that needs a paper gets it uploaded into its chat.
/papers/
"""


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    fn = os.path.join(root, REL)
    if not os.path.exists(fn):
        print("ERROR: not found: %s (run from the orrery repo root)" % fn); return 1
    with open(fn, "rb") as f:
        raw = f.read()
    was_crlf = b"\r\n" in raw
    lf = raw.replace(b"\r\n", b"\n")
    got = hashlib.md5(lf).hexdigest()
    if got != EXPECTED:
        if b"\n/papers/\n" in lf:
            print("ERROR: .gitignore already ignores /papers/ -- already applied; nothing written"); return 1
        print("ERROR: %s content %s, expected %s -- not orrery 297dec69; nothing written" % (REL, got, EXPECTED)); return 1
    if lf.count(EMDASH_OLD) != 1:
        print("ANCHOR FAIL: the orbit cache comment line was not found once"); return 1
    lf = lf.replace(EMDASH_OLD, EMDASH_NEW)
    print("ok  %s -- em dash in the orbit cache comment made ASCII" % REL)
    if not lf.endswith(b"\n"):
        lf += b"\n"
    lf += RULE
    print("ok  %s -- /papers/ rule added" % REL)
    if sum(1 for c in lf if c > 127):
        print("ERROR: non-ASCII remains in .gitignore; nothing written"); return 1
    papers = os.path.join(root, "papers")
    if os.path.exists(papers) and not os.path.isdir(papers):
        print("ERROR: a file named papers exists in the repo root; nothing written"); return 1
    with open(fn, "wb") as f:
        f.write(lf.replace(b"\n", b"\r\n") if was_crlf else lf)
    if os.path.isdir(papers):
        print("ok  papers/ already exists; left as is")
    else:
        os.makedirs(papers)
        print("ok  papers/ created")
    print("patch applied")
    print("next: move the PDFs into papers/ in File Explorer, then commit and push in GitHub Desktop")
    return 0


if __name__ == "__main__":
    sys.exit(main())
