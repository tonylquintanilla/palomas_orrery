"""
patch_L271_2_no_bak_and_gitignore.py

Run:  python patch_L271_2_no_bak_and_gitignore.py
From: the ORRERY repo root (the folder holding PROJECT_INSTRUCTIONS.md).
In VS Code: open this file from that folder and click Run.

Built on orrery ccd1ac965a95db743bb2e47efe94b4438fd03fd3 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHY -- and the short version is that we have been generating litter to
insure against something git already covers.

  THERE IS NO CLEANUP FUNCTION. Tony thought the maintenance runner had
  one. Checked at ccd1ac96: the word "bak" does not appear in
  maintenance_run.py at all, and there is no cleanup script in the repo.
  What he is remembering is the ONE-TIME sweep of 2026-08-29, when nine
  tracked backups were deleted and the `*.bak` rule was added. That was
  a sweep, not a mechanism.

  THE BACKUPS ARE REDUNDANT BY CONSTRUCTION, which is the part that
  makes this a rule and not a preference. Every patch guards on a
  content fingerprint before it writes. If the working copy does not
  match, the patch refuses. So by the time any patch writes, the file on
  disk is the committed version -- git holds it, and Discard Changes in
  GitHub Desktop restores it. The `.bak` can never be the only copy. The
  one case where it would earn its place, uncommitted work, is exactly
  the case where the fingerprint gate stops the patch from running.

  AND A STALE COPY IS AN ACTIVE HAZARD, not just clutter. The orrery's
  own .gitignore already says why, written during that sweep: "A session
  grepping for a value can hit one and read it as current." Two of the
  nine were a superseded master plan and a superseded skill.

  THE RATE IS DAYS, NOT WEEKS. Tony's correction, and he is right. All
  eight of the gallery backups deleted by patch_L271_1 were created
  between 2026-08-29 and 2026-08-31. The handoff written that evening
  said "after a few weeks" and was wrong; it is corrected on L-271
  rather than quietly restated.

  WHY THEY SEEM TO COME AND GO. `*.bak` matches a name ENDING in .bak,
  so a plain `interactive.html.bak` is invisible in GitHub Desktop and
  simply sits on disk. `.bak1`, `.bak2` and `.bak_L271` are NOT matched,
  so those show up and get committed. That is exactly the split in the
  evidence: the orrery kept `close_approach_cache.json.bak1` and `.bak2`
  through the sweep that removed everything else, and the gallery -- whose
  rule was narrower still -- kept all eight.

WHAT IT DOES (five files, seven edits, plus two deletions).

  skills/safe-file-editing/SKILL.md
    1. New rule: Git Is the Backup [QUALITY]. Patch scripts stop writing
       .bak and print the Discard Changes path instead.
    2. Version 1.9 -> 1.10.

  .gitignore
    3. `*.bak` widened to cover `*.bak[0-9]` and `*.bak_*`, the two
       shapes that slipped through the 2026-08-29 sweep.

  data/close_approach_cache.json.bak1 and .bak2
    4. DELETED from disk so they stop being committed. Read the note
       below before running -- this one has a real argument on both
       sides.

  PROJECT_INSTRUCTIONS.md
    5. Manifest row: safe-file-editing 1.9 -> 1.10.
    6. Version history: v3.51 added, v3.48 removed (it moves down).

  documentation/PROJECT_INSTRUCTIONS_HISTORY.md
    7. Receives v3.48.

  LEDGER_CONSOLIDATED.md
    8. L-271 opened. The handle was used by patch_L271_1 in the gallery
       repo and never had a ledger block; this writes it.

ABOUT THOSE TWO CACHE BACKUPS, because deleting them is a judgment and
should not slide past as housekeeping.
  `close_approach_data.py` keeps a deliberate two-generation rotation:
  bak1 is the previous run, bak2 the one before. It is bounded at two
  and never grows, so it is NOT the litter this patch is about. What is
  wrong is that they are TRACKED -- every close-approach fetch then
  commits three files where one would do, and git already holds the
  previous cache in its history.
  Deleting them costs nothing: the rotation rebuilds them on disk at the
  next fetch, and the widened rule keeps them out of commits from now on.
  The rotation itself is untouched.

WHAT THIS PATCH DOES NOT DO, deliberately.
  It does not rewrite the existing patch scripts in documentation/.
  Those are spent and archived; editing a record to match a rule written
  after it is exactly the thing Stamp What You Change forbids.

  IT ALSO WRITES NO .bak OF ITS OWN. That would be absurd, and it is the
  first script to follow the rule it installs.

SUCCESS: one "ok" line per edit, a byte count per file, "PATCH APPLIED".
FAILURE: one "ERROR" or "ANCHOR FAIL" line and NOTHING written or
deleted. Undo is Discard Changes in GitHub Desktop.
One-shot; a second run aborts on the fingerprints.
"""

import hashlib
import os
import sys

EXPECTED = {
    "skills/safe-file-editing/SKILL.md":
        "357c0e5ad8e0ae1f9eda505c8f766d26",
    ".gitignore":
        "52879aa4438a59026780a32930336058",
    "PROJECT_INSTRUCTIONS.md":
        "19e212317fc804370333e2985b60989b",
    "documentation/PROJECT_INSTRUCTIONS_HISTORY.md":
        "b4dce2dec21984d6e87a593f445c8238",
    "LEDGER_CONSOLIDATED.md":
        "0d2d657854febd1c622325f853cfd112",
}

CACHE_BAKS = [
    "data/close_approach_cache.json.bak1",
    "data/close_approach_cache.json.bak2",
]

# ------------------------------------------------------- 1. the new rule
RULE_ANCHOR = b"""### Line Endings Are Not Content [QUALITY]
"""

RULE_NEW = b"""### Git Is the Backup [QUALITY]

A patch script does NOT write a `.bak`. It prints how to undo instead.

The reason is structural rather than tidy-minded. A patch guards on a
content fingerprint before it writes, and refuses when the working copy
does not match. So at the moment it writes, the file on disk IS the
committed version -- git holds it, and one button restores it. The
`.bak` cannot ever be the only copy. The single case where it would
earn its place, uncommitted work, is precisely the case the fingerprint
gate refuses to run in.

So say this, in the words of the tool the person actually uses:

```
FAILURE: ... NOTHING was written.
Undo is Discard Changes in GitHub Desktop.
```

Not writing them is worth more than deleting them later, because a
stale copy is an ACTIVE HAZARD and not just clutter. A session grepping
for a value can hit one and read it as current; when the nine tracked
backups were swept from the orrery on 2026-08-29, two of them were a
superseded master plan and a superseded skill.

The rate is days. All eight backups swept from the gallery on
2026-08-31 were created in the preceding two days.

**And `*.bak` does not mean what it looks like.** The glob matches a
name ENDING in `.bak`, so `page.html.bak` is silently ignored and sits
on disk unseen, while `page.html.bak2` and `page.html.bak_L271` are NOT
matched and get committed. Any ignore rule for this needs all three
shapes:

```
*.bak
*.bak[0-9]
*.bak_*
```

**A rotating runtime backup is a different thing and is fine.**
`close_approach_data.py` keeps two generations of its cache, bounded at
two, rebuilt by the program that owns it. That is a program managing its
own data, not a patch hedging against itself. Keep it out of the
repository all the same: git already holds the previous cache.

(Tony's question, 2026-08-31: "why do we create them at all?" He also
believed the maintenance runner cleaned them up. It does not -- the word
does not appear in it. What existed was one manual sweep, which is how
a habit gets mistaken for a mechanism. L-271.)

### Line Endings Are Not Content [QUALITY]
"""

SKILL_VER_OLD = b"Skill version: 1.9 | Cut from palomas_orrery @ bfa9de2f (v1.9),\n"
SKILL_VER_NEW = (b"Skill version: 1.10 | Cut from palomas_orrery @ ccd1ac96 "
                 b"(v1.10),\nearlier @ bfa9de2f (v1.9),\n")

# --------------------------------------------------------- 3. .gitignore
IGNORE_OLD = b"""*.bak
"""

IGNORE_NEW = b"""# Widened 2026-08-31 (L-271): *.bak matches only names ENDING in
# .bak, so .bak1, .bak2 and .bak_L271 slipped through the sweep above
# and kept getting committed. All three shapes now.
*.bak
*.bak[0-9]
*.bak_*
"""

# ------------------------------------------------------- 5. manifest row
MANIFEST_OLD = b"""safe-file-editing             1.9  Editing existing files, patch scripts,
"""
MANIFEST_NEW = b"""safe-file-editing            1.10  Editing existing files, patch scripts,
"""

MANIFEST_ALT_OLD = b"""safe-file-editing            1.9  Editing existing files, patch scripts,
"""
MANIFEST_ALT_NEW = b"""safe-file-editing            1.10 Editing existing files, patch scripts,
"""

# ---------------------------------------------------- 6. version history
V351_ANCHOR = b"""v3.50 (August 31, 2026): No rule changed in this document. One skill
"""

V351 = b"""v3.51 (August 31, 2026): No rule changed in this document. One skill
bump, and the end of a habit nobody had decided on.

safe-file-editing 1.9 -> 1.10 (L-271). Git Is the Backup [QUALITY]:
patch scripts stop writing `.bak` and print the Discard Changes path
instead.

The argument is structural, which is what makes it a rule. A patch
guards on a content fingerprint and refuses when the working copy does
not match, so at the moment it writes, the file on disk is the committed
version. Git holds it. The `.bak` can never be the only copy, and the
one case where it would earn its place -- uncommitted work -- is exactly
the case the gate refuses to run in.

A stale copy is an active hazard rather than clutter. The orrery's own
.gitignore records why, from the sweep of 2026-08-29: a session grepping
for a value can hit one and read it as current, and two of the nine
swept that day were a superseded master plan and a superseded skill.

Tony's question was the whole of it -- "why do we create them at all?" --
and his correction to the rate stands with it: days, not weeks. All
eight swept from the gallery on 2026-08-31 were made in the preceding
two days. He also believed the maintenance runner cleaned them up. It
does not; the word does not appear in that file. What existed was one
manual sweep, which is how a habit gets mistaken for a mechanism.

The .gitignore rule was widened in the same commit. `*.bak` matches only
names ENDING in .bak, so `.bak1`, `.bak2` and `.bak_L271` slipped
through the 2026-08-29 sweep and kept being committed -- which is why
two close-approach cache backups survived it, and why the gallery, whose
rule was narrower still, kept all eight of its own.

One obligation this bump cannot discharge from inside the session that
made it. A skill lives in three stores, and the account install is the
copy Claude actually loads; a reinstall is invisible to the running
conversation. So: safe-file-editing went to 1.10 at `ccd1ac96`, the
session that bumped it had loaded 1.9, and the next session confirms its
loaded copy reads 1.10 before doing patch work.

Version history: v3.48 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

HIST_ANCHOR = b"""(Moved down from the resident protocol on 2026-08-31 when v3.50
made a fourth entry.)
"""

HIST_NOTE = b"""(Moved down from the resident protocol on 2026-08-31 when v3.51
made a fourth entry.)

"""

# --------------------------------------------------------- 8. the ledger
L271_BLOCK = b"""#### [L-271] Patch scripts wrote backups nothing ever removed
<!-- L:271 status:OPEN upd:2026-08-31 section:A flag: rice:4/3/95/1 -->
- **Tony's question, 2026-08-31, and it is the whole of the finding:**
  "why do we create them at all?" Asked after
  `patch_L271_1_gallery_bak_cleanup.py` deleted eight tracked backups
  from the gallery repo and two more appeared within the hour, written
  by the next two patches.
- **There is no cleanup function, and Tony believed there was.** He
  thought `maintenance_run.py` removed them. Checked at `ccd1ac96`: the
  word "bak" does not appear in that file, and the repo has no cleanup
  script. What he was remembering is the ONE-TIME sweep of 2026-08-29,
  when nine tracked backups were deleted and the `*.bak` rule added.
  That is how a habit gets mistaken for a mechanism.
- **They are redundant BY CONSTRUCTION, which is what makes this a rule
  rather than a preference.** A patch guards on a content fingerprint
  and refuses when the working copy does not match, so at the moment it
  writes, the file on disk is the committed version. Git holds it;
  Discard Changes restores it. The `.bak` can never be the only copy.
  The one case where it would earn its place, uncommitted work, is
  exactly the case the gate refuses to run in.
- **A stale copy is an ACTIVE HAZARD, not clutter.** The reason is
  already written in the orrery's own `.gitignore` from the August 29
  sweep: a session grepping for a value can hit one and read it as
  current. Two of the nine were a superseded master plan and a
  superseded skill.
- **CORRECTION, Tony's, 2026-08-31: the rate is days, not weeks.** The
  handoff of that evening said the eight gallery backups were "what that
  looks like after a few weeks." Measured: all eight were created
  between 2026-08-29 and 2026-08-31. Corrected here rather than restated
  quietly, because the wrong number made the problem look slower than it
  is.
- **Why they seem to come and go.** `*.bak` matches a name ENDING in
  `.bak`, so a plain `interactive.html.bak` is invisible in GitHub
  Desktop and sits on disk unseen. `.bak1`, `.bak2` and `.bak_L271` are
  NOT matched, so those surface and get committed. That is exactly the
  split in the evidence: the orrery kept
  `data/close_approach_cache.json.bak1` and `.bak2` through the sweep
  that removed everything else, and the gallery -- whose rule was
  `*.json.bak` only -- kept all eight.
- **Fixed in protocol v3.51 / safe-file-editing 1.10.** Patch scripts
  stop writing `.bak` and print the Discard Changes path. The orrery's
  ignore rule was widened to all three shapes in the same commit; the
  gallery's was widened by `patch_L271_1` on 2026-08-31.
- **The two close-approach cache backups are a different thing and were
  still deleted.** `close_approach_data.py` keeps a deliberate
  two-generation rotation, bounded at two and rebuilt by the program
  that owns it. That is not litter. Being TRACKED is the defect: every
  fetch committed three files where one would do, and git already holds
  the previous cache. The rotation is untouched and rebuilds them on
  disk at the next fetch.
- **Gap: the spent patch scripts in `documentation/` are not
  rewritten.** They wrote `.bak` because the rule then said to. Editing
  a record to match a rule written after it is what Stamp What You
  Change forbids.
- **Gap: the gallery repo has no ledger.** L-271's first patch ran there
  and this block is in the orrery, which is where the ledger lives. The
  cross-repo record is this line.
- **Claude:** RICE 4/3/95/1 -> 11.4 proposed, not confirmed. Effort 1
  because the rule and both ignore rules are written; what remains is
  habit, and the skill enforces that.
- **Ref:** L-236 (the runner that first surfaced backup churn); L-269
  (The Correction Does Not Travel, the same shape one layer over);
  Stamp What You Change and Git Is the Backup, safe-file-editing 1.10.

"""

L271_ANCHOR = b"## PENDING ACTION (Tony-side)"


def die(msg):
    print("ERROR: " + msg)
    sys.exit(1)


def main():
    if not os.path.exists("PROJECT_INSTRUCTIONS.md"):
        die("run this from the orrery repo root.")

    files = {}
    print("BASE CHECK -- content fingerprints (CRLF-normalised)")
    for path, want in EXPECTED.items():
        if not os.path.exists(path):
            die("not found: %s" % path)
        with open(path, "rb") as f:
            raw = f.read()
        crlf = b"\r\n" in raw
        content = raw.replace(b"\r\n", b"\n") if crlf else raw
        got = hashlib.md5(content).hexdigest()
        if got != want:
            die("base moved for %s\n  expected %s\n  found    %s\n"
                "  Nothing was written or deleted." % (path, want, got))
        tag = "  [CRLF; matched after normalising]" if crlf else ""
        print("  ok  %-46s %s%s" % (path, got, tag))
        files[path] = {"content": content, "crlf": crlf, "orig": raw}

    # The v3.48 block is READ from the protocol, not retyped.
    pi = files["PROJECT_INSTRUCTIONS.md"]["content"]
    try:
        a = pi.index(b"v3.48 (August 29, 2026)")
        b = pi.index(b"\nFunctional for Claude, readable for human")
    except ValueError:
        die("could not locate the v3.48 block to move down.")
    v348 = pi[a:b].rstrip(b"\n") + b"\n\n"
    print("  ok  v3.48 block read from the protocol (%d bytes), not retyped"
          % len(v348))

    # The manifest row's column width may differ by one space depending on
    # how skills_index laid out a two-character version. Accept either.
    man_old, man_new = MANIFEST_OLD, MANIFEST_NEW
    if pi.count(man_old) != 1 and pi.count(MANIFEST_ALT_OLD) == 1:
        man_old, man_new = MANIFEST_ALT_OLD, MANIFEST_ALT_NEW

    inserted = (RULE_NEW + SKILL_VER_NEW + IGNORE_NEW + man_new + V351
                + v348 + HIST_NOTE + L271_BLOCK)
    if any(byte > 127 for byte in inserted):
        die("inserted text is not ASCII.")
    print("  ok  inserted text is ASCII (%d bytes)" % len(inserted))

    edits = [
        ("skills/safe-file-editing/SKILL.md",
         "new rule: Git Is the Backup [QUALITY]", RULE_ANCHOR, RULE_NEW),
        ("skills/safe-file-editing/SKILL.md",
         "skill version 1.9 -> 1.10", SKILL_VER_OLD, SKILL_VER_NEW),
        (".gitignore",
         "*.bak widened to all three backup shapes", IGNORE_OLD, IGNORE_NEW),
        ("PROJECT_INSTRUCTIONS.md",
         "manifest row 1.9 -> 1.10", man_old, man_new),
        ("PROJECT_INSTRUCTIONS.md",
         "version history: add v3.51", V351_ANCHOR, V351 + V351_ANCHOR),
        ("PROJECT_INSTRUCTIONS.md",
         "version history: remove v3.48 (it moves down)", v348, b""),
        ("documentation/PROJECT_INSTRUCTIONS_HISTORY.md",
         "PART 1 receives v3.48",
         HIST_ANCHOR, HIST_ANCHOR + b"\n" + v348 + HIST_NOTE),
        ("LEDGER_CONSOLIDATED.md",
         "L-271 opened", L271_ANCHOR, L271_BLOCK + L271_ANCHOR),
    ]

    print("\nEDITS")
    for path, label, old, new in edits:
        content = files[path]["content"]
        n = content.count(old)
        if n != 1:
            print("ANCHOR FAIL (%d matches, expected 1): %s -- %s"
                  % (n, path, label))
            print("  anchor head: %r" % old[:70])
            print("NOTHING WAS WRITTEN OR DELETED.")
            sys.exit(1)
        files[path]["content"] = content.replace(old, new)
        print("  ok  %-46s %s" % (label, path))

    print("\nVERIFY")
    probes = [
        ("skills/safe-file-editing/SKILL.md",
         b"Skill version: 1.10", 1, "skill declares 1.10"),
        ("skills/safe-file-editing/SKILL.md",
         b"### Git Is the Backup [QUALITY]", 1, "the rule is present"),
        ("PROJECT_INSTRUCTIONS.md",
         b"safe-file-editing            1.10", 1, "manifest row says 1.10"),
        (".gitignore", b"*.bak_*", 1, "the ignore covers .bak_ suffixes"),
        (".gitignore", b"*.bak[0-9]", 1, "the ignore covers .bak1/.bak2"),
        ("LEDGER_CONSOLIDATED.md",
         b"\n#### [L-271] ", 1, "L-271's header is four-hash"),
        ("LEDGER_CONSOLIDATED.md",
         b"<!-- L:271 status:OPEN", 1, "L-271 will be indexed"),
        ("documentation/PROJECT_INSTRUCTIONS_HISTORY.md",
         b"v3.48 (August 29, 2026)", 1, "v3.48 landed in the archive"),
    ]
    bad = []
    for path, probe, want, what in probes:
        n = files[path]["content"].count(probe)
        ok = (n == want)
        print("  %s %-46s (%d, expected %d)"
              % ("ok " if ok else "DIFF", what, n, want))
        if not ok:
            bad.append(what)
    resident = files["PROJECT_INSTRUCTIONS.md"]["content"].count(b"\nv3.")
    print("  %s resident version entries: %d (expected 3)"
          % ("ok " if resident == 3 else "DIFF", resident))
    if resident != 3:
        bad.append("resident version entry count")
    if bad:
        print("  NOTHING WAS WRITTEN OR DELETED.")
        sys.exit(1)

    # No .bak. This is the first script to follow the rule it installs.
    print("\nWRITE -- and note there is no .bak; that is the point")
    for path in EXPECTED:
        out = files[path]["content"]
        if files[path]["crlf"]:
            out = out.replace(b"\n", b"\r\n")
        with open(path, "wb") as f:
            f.write(out)
        print("  wrote %-46s %7d bytes (%+d)"
              % (path, len(out), len(out) - len(files[path]["orig"])))

    print("\nDELETE -- the two TRACKED cache rotation backups, by name")
    for p in CACHE_BAKS:
        if os.path.exists(p):
            size = os.path.getsize(p)
            os.remove(p)
            print("  removed %-44s %8d bytes" % (p, size))
        else:
            print("  absent  %-44s (nothing to do)" % p)
    print("  close_approach_data.py's rotation is untouched and rebuilds")
    print("  them on disk at the next fetch. The widened rule keeps them")
    print("  out of commits from now on.")

    print("\nPATCH APPLIED")
    print("  Undo is Discard Changes in GitHub Desktop, which is exactly")
    print("  what this patch's rule says to say.")
    print("\nNEXT, all yours:")
    print("  (do) Run skills_index.py. The manifest row is already 1.10,")
    print("       so 'unchanged, content identical' is the check PASSING.")
    print("  (do) Run ledger_index.py. L-271 is new, so the index changes.")
    print("  (do) REINSTALL safe-file-editing in Settings > Skills. No")
    print("       patch and no session can verify this one.")
    print("  (do) Run maintenance_run.py, then commit everything as one.")
    print("  (do) Delete the leftover backups on disk in BOTH repos. They")
    print("       are ignored now, so GitHub Desktop will not show them:")
    print("         orrery   *.bak, *.bak1, *.bak2, *.bak_L*")
    print("         gallery  interactive.html.bak_L267A, .gitignore.bak_L271,")
    print("                  data/objects_config.json.bak")
    print("\nWhat changed, by name:")
    print("  skills/safe-file-editing/SKILL.md   Git Is the Backup; 1.9 -> 1.10")
    print("  .gitignore                          three backup shapes, not one")
    print("  PROJECT_INSTRUCTIONS.md             manifest row; v3.51; v3.48 out")
    print("  documentation/PROJECT_INSTRUCTIONS_HISTORY.md   receives v3.48")
    print("  LEDGER_CONSOLIDATED.md              L-271 opened")
    print("  data/close_approach_cache.json.bak1 and .bak2   deleted")


if __name__ == "__main__":
    main()
