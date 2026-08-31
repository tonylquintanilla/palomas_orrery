"""
patch_L269_4_pipeline_sweep.py

Run:  python patch_L269_4_pipeline_sweep.py
From: the ORRERY repo root (the folder holding PROJECT_INSTRUCTIONS.md).
In VS Code: open this file from that folder and click Run.

Built on orrery 04bba3cafda38470a117026ff3db848323a7f126 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

L-269, fourth and last. The correction travels.

WHY.
  v3.49 corrected Check All Parallel Pipelines in the protocol: five
  CONSUMERS, named, with their files and repos, and the "in
  palomas_orrery.py" scoping removed. Three LIVE stores were left
  carrying the old merged sentence, and one of them loads on every
  orrery session.

  That is The Correction Does Not Travel, in the shape the rule itself
  predicts. The fix went into the document being edited and stopped
  there.

  The three, by name:
    skills/orrery-coding-conventions/SKILL.md   loads every session
    documentation/CLAUDE.md                     read by relay partners
    README.md                                   read first by everyone

  The archived protocol snapshots and the session handoffs also carry
  it -- 43 more files. They are RECORDS and are correctly left alone. A
  record that rewrites its own past stops being evidence.

WHAT IT DOES (six files, seven edits, all-or-nothing).

  skills/orrery-coding-conventions/SKILL.md
    1. The pipelines bullet names the five consumers and drops the
       single-file scope.
    2. Skill version 1.6 -> 1.7.

  documentation/CLAUDE.md
    3. Same correction, in that file's own voice.

  README.md
    4. The five were already named here -- this is where the protocol's
       count came from. What it gains is WHERE each one lives, because
       two are in the gallery repo and the README's prose implies
       otherwise.

  PROJECT_INSTRUCTIONS.md
    5. Manifest row: orrery-coding-conventions 1.6 -> 1.7.
    6. Version history: v3.50 added, v3.47 REMOVED (it moves down).

  documentation/PROJECT_INSTRUCTIONS_HISTORY.md
    7. Receives v3.47 with the standard moved-down note.

THE SKILL BUMP'S FOUR STEPS, and which of them this patch can do.
  1. The version line in SKILL.md          -- done here.
  2. skills_index.py regenerating the row  -- this patch writes the row
     directly so the file is CONSISTENT, but you still run the indexer;
     if it rewrites identically, that is the check passing.
  3. This protocol version-history entry   -- done here.
  4. The commit                            -- yours.

  A FIFTH step this patch CANNOT do and must not pretend to: the
  account install. Settings > Skills is the copy Claude actually loads,
  a reinstall is invisible to a running session, and Stale Skill = Stop
  says not to clear that on anyone's word. So it is written into the
  handoff as an obligation the next session discharges against its own
  loaded copy.

SUCCESS: one "ok" line per edit, a byte count per file, "PATCH APPLIED".
FAILURE: one "ERROR" or "ANCHOR FAIL" line and NOTHING written.
One-shot; a second run aborts on the fingerprints.
"""

import hashlib
import os
import sys

EXPECTED = {
    "skills/orrery-coding-conventions/SKILL.md":
        "2fc39ea3cc18000263d4da8e44f14f50",
    "documentation/CLAUDE.md":
        "75b04c3683f95c8688ad2f13a6f752a6",
    "README.md":
        "735e4462399295df2e9db3f7bace9636",
    "PROJECT_INSTRUCTIONS.md":
        "268421dc5bf3c9a05c9853e353edc309",
    "documentation/PROJECT_INSTRUCTIONS_HISTORY.md":
        "4f72aeb0005d177d8c43a3a665c37e94",
}

# ------------------------------------------------------------ 1. skill
SKILL_OLD = b"""- Position data flows through 5 parallel pipelines in palomas_orrery.py --
  ALL must be patched. The same bugs appear independently in plot_objects /
  animate_objects and in the gallery pipeline. Map all consumers first.
"""

SKILL_NEW = b"""- Position data reaches a viewer through FIVE parallel CONSUMERS, and a
  fix in one does not propagate. Map ALL of them first. Named here rather
  than counted, because a count does not say what it counted (L-269):
    static plot        plot_objects              palomas_orrery.py
    animation          animate_objects           palomas_orrery.py
    social export      export_social_view        palomas_orrery.py
    gallery curation   tools/gallery_studio.py   GALLERY repo
    JSON conversion    tools/json_converter.py   GALLERY repo
  TWO OF THE FIVE ARE IN THE OTHER REPOSITORY. Grep one repo and you find
  three. The old wording said "5 parallel pipelines in palomas_orrery.py",
  which put a cross-file count inside a single-file scope and hid them.
- FETCHING is a different question with a different answer. Six functions
  in palomas_orrery.py acquire position data -- resolve_shell_sun_position,
  update_orbit_paths, plot_actual_orbits, plot_objects, animate_objects,
  open_orbital_param_visualization -- across fetch_position,
  fetch_trajectory, fetch_orbit_path and orbit_data_manager, with
  plot_objects alone holding three near-identical branches. Three of the
  five consumers above fetch nothing; they render what was already
  fetched. Do not substitute one list for the other.
"""

SKILL_VER_OLD = b"Skill version: 1.6 | Cut from palomas_orrery @ 3faa72a0 (v1.6),\n"
SKILL_VER_NEW = (b"Skill version: 1.7 | Cut from palomas_orrery @ 04bba3ca (v1.7),\n"
                 b"earlier @ 3faa72a0 (v1.6),\n")

# ------------------------------------------------------------ 3. CLAUDE.md
CLAUDE_OLD = b"""**Parallel pipelines exist.** palomas_orrery.py routes position data through
5 parallel pipelines. A fix in one does not propagate to others. Before
patching data flow, map ALL consumers first.
"""

CLAUDE_NEW = b"""**Parallel pipelines exist, and two of them are in the OTHER repo.**
Position data reaches a viewer through five consumers, and a fix in one
does not propagate. Map ALL of them before patching data flow:
static plot (`plot_objects`), animation (`animate_objects`) and social
export (`export_social_view`) in `palomas_orrery.py`; gallery curation
(`tools/gallery_studio.py`) and JSON conversion
(`tools/json_converter.py`) in the GALLERY repo. The old wording here
said "5 parallel pipelines" in `palomas_orrery.py`, which hid the two
that are not (L-269).

**Fetching is a different list.** Six functions in `palomas_orrery.py`
acquire position data; three of the five consumers above fetch nothing.
The fetcher list is in `orrery-coding-conventions`.
"""

# ------------------------------------------------------------ 4. README
README_OLD = b"""Position data flows through five parallel pipelines (static plot, animation,
social export, gallery curation, JSON conversion) -- a change to something
like hover text can touch all five, each with its own path. This is the
project's central maintenance discipline: fixes must be checked across every
consumer.
"""

README_NEW = b"""Position data flows through five parallel consumers, each with its own
path, so a change to something as small as hover text can touch all five.
This is the project's central maintenance discipline: a fix must be
checked across every consumer, not just the one that reported the bug.

| Consumer | Where |
|---|---|
| Static plot | `plot_objects` in `palomas_orrery.py` |
| Animation | `animate_objects` in `palomas_orrery.py` |
| Social export | `export_social_view` in `palomas_orrery.py` |
| Gallery curation | `tools/gallery_studio.py`, in the **gallery** repo |
| JSON conversion | `tools/json_converter.py`, in the **gallery** repo |

Two of the five live in the gallery repository, so checking only this one
finds three of five.
"""

# ------------------------------------------------------ 5. manifest row
MANIFEST_OLD = b"""orrery-coding-conventions    1.6  Markers, hover text, axes, shells,
"""
MANIFEST_NEW = b"""orrery-coding-conventions    1.7  Markers, hover text, axes, shells,
"""

# ------------------------------------------------ 6. version history
V350_ANCHOR = b"""v3.49 (August 30, 2026): One rule added, in two pieces and two tiers.
"""

V350 = b"""v3.50 (August 31, 2026): No rule changed in this document. One skill
bump, and a correction finally travelling.

orrery-coding-conventions 1.6 -> 1.7 (L-269), plus the same correction
in documentation/CLAUDE.md and README.md. v3.49 fixed Check All
Parallel Pipelines HERE and left three live stores carrying the old
merged sentence -- a cross-file count of five wearing a single-file
scope. One of the three is a skill that loads on every orrery session,
so the wrong instruction was being handed to whoever read it, including
Claude.

That is The Correction Does Not Travel in the shape the rule predicts:
the fix went into the document being edited and stopped there. It was
found by asking, on the day the rule landed, which OTHER stores carry
the sentence -- 46 documents, 43 of them archives and session records
correctly left alone.

All three now name the five consumers with their files and repos, and
say plainly that two of the five are in the GALLERY repository. That
last part is the load-bearing half: a reader following the old
instruction as written would grep one repo and find three of five.

The fetcher list is recorded beside the consumer list in
orrery-coding-conventions, labelled as the answer to a different
question, because the two are on different axes and neither is a subset
of the other.

One obligation this bump cannot discharge from inside the session that
made it. A skill lives in three stores, and the account install is the
copy Claude actually loads; a reinstall is invisible to the running
conversation. So: orrery-coding-conventions went to 1.7 at
`04bba3ca`, the session that bumped it had loaded 1.6, and the next
session confirms its loaded copy reads 1.7 before doing orrery visual
work.

Version history: v3.47 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

HIST_ANCHOR = b"""(Moved down from the resident protocol on 2026-08-30 when v3.49
made a fourth entry.)
"""

HIST_NOTE = b"""(Moved down from the resident protocol on 2026-08-31 when v3.50
made a fourth entry.)

"""


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
                "  Nothing was written." % (path, want, got))
        tag = "  [CRLF; matched after normalising]" if crlf else ""
        print("  ok  %-46s %s%s" % (path, got, tag))
        files[path] = {"content": content, "crlf": crlf, "orig": raw}

    # Read AFTER the fingerprints, so a second run reports "base moved"
    # rather than a confusing complaint about a block that is correctly
    # no longer there.
    pi = files["PROJECT_INSTRUCTIONS.md"]["content"]
    try:
        a = pi.index(b"v3.47 (August 29, 2026)")
        b = pi.index(b"\nFunctional for Claude, readable for human")
    except ValueError:
        die("could not locate the v3.47 block to move down.")
    v347 = pi[a:b].rstrip(b"\n") + b"\n\n"
    print("  ok  v3.47 block read from the protocol (%d bytes), not retyped"
          % len(v347))

    inserted = (SKILL_NEW + SKILL_VER_NEW + CLAUDE_NEW + README_NEW
                + MANIFEST_NEW + V350 + v347 + HIST_NOTE)
    if any(byte > 127 for byte in inserted):
        die("inserted text is not ASCII.")
    print("  ok  inserted text is ASCII (%d bytes)" % len(inserted))

    edits = [
        ("skills/orrery-coding-conventions/SKILL.md",
         "pipelines bullet: five consumers NAMED, fetcher list added",
         SKILL_OLD, SKILL_NEW),
        ("skills/orrery-coding-conventions/SKILL.md",
         "skill version 1.6 -> 1.7", SKILL_VER_OLD, SKILL_VER_NEW),
        ("documentation/CLAUDE.md",
         "same correction, in that file's voice", CLAUDE_OLD, CLAUDE_NEW),
        ("README.md",
         "the five gain their files and repos", README_OLD, README_NEW),
        ("PROJECT_INSTRUCTIONS.md",
         "manifest row 1.6 -> 1.7", MANIFEST_OLD, MANIFEST_NEW),
        ("PROJECT_INSTRUCTIONS.md",
         "version history: add v3.50", V350_ANCHOR, V350 + V350_ANCHOR),
        ("PROJECT_INSTRUCTIONS.md",
         "version history: remove v3.47 (it moves down)", v347, b""),
        ("documentation/PROJECT_INSTRUCTIONS_HISTORY.md",
         "PART 1 receives v3.47",
         HIST_ANCHOR, HIST_ANCHOR + b"\n" + v347 + HIST_NOTE),
    ]

    print("\nEDITS")
    for path, label, old, new in edits:
        content = files[path]["content"]
        n = content.count(old)
        if n != 1:
            print("ANCHOR FAIL (%d matches, expected 1): %s -- %s"
                  % (n, path, label))
            print("  anchor head: %r" % old[:70])
            print("NOTHING WAS WRITTEN.")
            sys.exit(1)
        files[path]["content"] = content.replace(old, new)
        print("  ok  %-52s %s" % (label, path))

    # Post-write checks that could actually fail.
    print("\nVERIFY")
    probes = [
        ("skills/orrery-coding-conventions/SKILL.md",
         b"Skill version: 1.7", 1, "skill declares 1.7"),
        ("PROJECT_INSTRUCTIONS.md",
         b"orrery-coding-conventions    1.7", 1, "manifest row says 1.7"),
        ("skills/orrery-coding-conventions/SKILL.md",
         b"- Position data flows through 5 parallel pipelines", 0,
         "the skill's INSTRUCTION no longer says it"),
        ("documentation/CLAUDE.md",
         b"**Parallel pipelines exist.** palomas_orrery.py routes", 0,
         "CLAUDE.md's INSTRUCTION no longer says it"),
        ("README.md",
         b"five parallel pipelines", 0,
         "README no longer carries it"),
        ("skills/orrery-coding-conventions/SKILL.md",
         b"tools/gallery_studio.py", 1,
         "the skill names the gallery-repo consumer"),
        ("documentation/PROJECT_INSTRUCTIONS_HISTORY.md",
         b"v3.47 (August 29, 2026)", 1, "v3.47 landed in the archive"),
    ]
    bad = []
    for path, probe, want, what in probes:
        n = files[path]["content"].count(probe)
        ok = (n == want)
        print("  %s %-48s (%d, expected %d)"
              % ("ok " if ok else "DIFF", what, n, want))
        if not ok:
            bad.append(what)
    resident = files["PROJECT_INSTRUCTIONS.md"]["content"].count(b"\nv3.")
    print("  %s resident version entries: %d (expected 3)"
          % ("ok " if resident == 3 else "DIFF", resident))
    if resident != 3:
        bad.append("resident version entry count")
    if bad:
        print("  NOTHING WAS WRITTEN.")
        sys.exit(1)

    print("\nWRITE")
    for path in EXPECTED:
        out = files[path]["content"]
        if files[path]["crlf"]:
            out = out.replace(b"\n", b"\r\n")
        with open(path + ".bak", "wb") as f:
            f.write(files[path]["orig"])
        with open(path, "wb") as f:
            f.write(out)
        print("  wrote %-46s %7d bytes (%+d)  [.bak]"
              % (path, len(out), len(out) - len(files[path]["orig"])))

    print("\nPATCH APPLIED")
    print("\nNEXT, all yours:")
    print("  (do) Run skills_index.py. The manifest row is already 1.7, so")
    print("       'unchanged, content identical' is the check PASSING, not")
    print("       the indexer doing nothing.")
    print("  (do) REINSTALL orrery-coding-conventions in Settings > Skills.")
    print("       This is the step no patch and no session can verify. The")
    print("       account copy is what Claude loads, and a reinstall is")
    print("       invisible to a running conversation. It is written into")
    print("       the handoff for the next session to confirm at 1.7.")
    print("  (do) Run maintenance_run.py, then commit all six files")
    print("       together -- the bump's four steps are one commit.")
    print("\nCorrected, by name:")
    print("  skills/orrery-coding-conventions/SKILL.md   loads every session")
    print("  documentation/CLAUDE.md                     relay partners")
    print("  README.md                                   read first")
    print("\nStill carrying the old sentence, and correctly LEFT ALONE:")
    print("  43 archived protocol snapshots and session handoffs. They are")
    print("  records. A record that rewrites its own past stops being")
    print("  evidence.")


if __name__ == "__main__":
    main()
