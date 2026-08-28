"""
patch_L256_3_gate_binds_at_export.py

provenance-discipline 2.8 -> 2.9, and protocol v3.45 -> v3.46.

Built on palomas_orrery @ a263f73d473bd2cd9de8241372ee9d1885045d04
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Confirmed against the live remote 2026-08-28.

WHY, IN ONE PARAGRAPH
  The 2.8 section written earlier tonight put the provenance gate at
  SERVING. Tony's ruling later the same evening moves it upstream: the
  slice closes before a value leaves the orrery for the gallery cache.
  His reason is mechanical and it is decisive. `provenance_scanner.py`
  exists only in the orrery. `gallery_cache_builder.py` lives in the
  GALLERY repo and scores nothing -- it mentions provenance twice, once
  in a docstring recording where its copied constants came from and once
  in a warning string. So a gate at serving sits downstream of the last
  checker that exists, in a different repository, which is precisely
  "A Check That Cannot Fail Is Not Passing."

  The section is right about WHY and wrong about WHERE, and 2.9 splits
  them so a future session cannot relocate it back on the reasoning that
  publication is where the harm lands.

THREE FILES, FIVE EDITS, ALL-OR-NOTHING.

  skills/provenance-discipline/SKILL.md
    - version 2.8 -> 2.9 with a v2.9 paragraph
    - the gate section retitled and rewritten
    - front-matter description updated

  PROJECT_INSTRUCTIONS.md
    - v3.46 entry added; v3.43 removed (three stay resident)

  documentation/PROJECT_INSTRUCTIONS_HISTORY.md
    - v3.43 appended to PART 1

NOT TOUCHED
  LEDGER_CONSOLIDATED.md. Its fingerprint depends on whether
  patch_L255_2 and ledger_index.py have run, and guessing that would
  make this patch refuse for the wrong reason. L-256's block gains a
  line next session; the handoff carries it.

RUN ORDER
  This patch, then skills_index.py, then maintenance_run.py, then
  commit and push. It is independent of patch_L255_2 and either order
  works.

HOW TO RUN
  Open in VS Code and press Run, with the repo root as the working
  directory. No arguments, no prompts.

Module updated: August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import shutil
import sys

SKILL = os.path.join("skills", "provenance-discipline", "SKILL.md")
PROTOCOL = "PROJECT_INSTRUCTIONS.md"
HISTORY = os.path.join("documentation", "PROJECT_INSTRUCTIONS_HISTORY.md")

EXPECTED = {
    SKILL: "60d887a043347128a87003499581863a",
    PROTOCOL: "48433d4e98df47bfa86f04b756ca2f36",
    HISTORY: "b13e49fb2dcee470a4e79c0c06c078f9",
}

BASE_SHA = "a263f73d473bd2cd9de8241372ee9d1885045d04"


# ------------------------------------------------- the v3.43 entry text
# Defined once so the removal and the append cannot drift apart.

V343 = """v3.43 (August 25, 2026): One rule added, and it is a generalization
rather than a new idea. "The Braid -- The Artifact Orders the Work"
enters Part 3 directly after The Artifact Bounds the Audit, which it
extends by one axis: that rule bounds which values are in scope, this
one bounds which are in scope NEXT, for any correctness program rather
than for provenance alone. Origin: Tony's August 22 ruling had lived
only in the master plan, where it carries SEQUENCING authority for the
gallery. He was applying it across the constants work too -- from
memory, because it was written nowhere that fires. On August 25 a
constants migration ran global and did not terminate: one conversion
factor led to a shadow name, to three aliases, to a second constant at
38 sites across 11 modules, in one evening, with zero movement on the
artifact that ships. Tony's own framing, and the reason this entry
exists: "it is a meta-principle. its not even in the protocol as such."
The section's operative additions beyond the master plan's version are
the discovery/remediation split -- discovery enumerates and fixes
nothing, so it terminates -- and one ledger row per CLASS rather than
per instance. Handle L-250. Version history: v3.40 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.
"""


# ---------------------------------------------------------------- edits

EDITS = []


# --- S1 -- skill version header ---------------------------------------

EDITS.append((
    SKILL, "S1 skill version header",

    "Skill version: 2.8 | Cut from palomas_orrery @ 7f4a2f9f (v2.8),\n"
    "earlier @ 3faa72a0 (v2.7), @ f603be3 (v2.6), @ 731066f (v2.5),\n"
    "@ 6b99ace (v2.2), @ 00219d9 (v2.1), @ eb77c83 (v2.0),\n"
    "@ cdcdb4b (v1.9) | August 27, 2026\n",

    "Skill version: 2.9 | Cut from palomas_orrery @ a263f73d (v2.9),\n"
    "earlier @ 7f4a2f9f (v2.8), @ 3faa72a0 (v2.7), @ f603be3 (v2.6),\n"
    "@ 731066f (v2.5), @ 6b99ace (v2.2), @ 00219d9 (v2.1),\n"
    "@ eb77c83 (v2.0), @ cdcdb4b (v1.9) | August 28, 2026\n"
    "v2.9 moves the gate UPSTREAM, from serving to export, on Tony's\n"
    "ruling of 2026-08-28. 2.8 put it where the harm lands; 2.9 puts it\n"
    "where a check can still run. `provenance_scanner.py` exists only in\n"
    "the orrery repo, and `gallery_cache_builder.py` lives in the gallery\n"
    "repo and scores nothing, so a gate at serving sits downstream of the\n"
    "last checker in existence and across a repository boundary. The WHY\n"
    "is unchanged and the WHERE is separated from it explicitly, so the\n"
    "gate cannot drift back on the reasoning that publication is where a\n"
    "visitor is harmed. One section rewritten, nothing else touched.\n",
))


# --- S2 -- the gate section itself ------------------------------------

OLD_GATE = """## The Gate Binds at SERVING [CRITICAL]

Provenance binds where a claim reaches a reader, not where it is drawn.

Drawing a shell locally gates nothing. It costs an afternoon to undo and
nobody outside the room sees it. SERVING it to the interactive gallery
is different: a visitor takes what the site shows as true, and there is
no point downstream of the orrery where a wrong radius is caught -- not
the builder, not the resolver, not the browser. None of them knows what
a correct ring radius is.

So each rendering step closes its own provenance slice BEFORE it ships,
and the slice is bounded by what that step serves.

This EXTENDS the earlier line that the asymmetry "governs what an
artifact may LOCK, not what may be BUILT." That sentence was about
fingerprinted golden artifacts and is not withdrawn. Publication is the
sharper boundary.

The braid is intact: the audit stays bounded by the current artifact,
stays countable, and stays off the critical path as a gate. What moved
is where it binds.
"""

NEW_GATE = """## The Gate Binds at EXPORT [CRITICAL]

**A value's provenance closes before it LEAVES THE ORRERY. Not before it
is drawn, and not before it is published.**

Three points, and they are not the same point.

**Why the gate exists: SERVING.** A visitor takes what the site shows as
true. There is no place downstream of the orrery where a wrong radius is
caught -- not the builder, not the resolver, not the browser. None of
them knows what a correct ring radius is.

**Where the gate FIRES: EXPORT.** The orrery is the last place a check
can run. `provenance_scanner.py` lives in the orrery repo and scans the
orrery tree. `gallery_cache_builder.py` lives in the GALLERY repo and
scores nothing -- it mentions provenance twice, once in a docstring
recording where its copied constants came from and once in a warning
string. The two repositories do not share a checker. So a gate placed at
publication sits downstream of the last instrument in existence, and a
gate nothing can enforce is A Check That Cannot Fail Is Not Passing
wearing a different hat.

**What is still free: DRAWING.** A local render gates nothing. It costs
an afternoon to undo and nobody outside the room sees it.

So the rule in operational form: **a body's slice closes before its
values enter `objects_config.json` and the served cache** -- not
afterwards, and not before the page goes live. A body cannot be added to
the served set and cleared later.

The property this buys is easier to state than the one it replaces. The
cache becomes, by construction, a set of values whose provenance was
closed at the moment they entered it. "Everything served has been
checked" is a claim about a boundary crossing, which happens once and
can be gated. "Everything published has been checked" is a claim about
an accumulating set, which has to be re-established on every build.

**A consequence, recorded because it changes a priority.**
`objects_config.json` is maintained BY HAND in the gallery repo. So the
export boundary this gate names is, today, a human copy with no check on
it at all. That makes the cross-repo transport (master plan segment 2)
the gate's missing enforcement point rather than a defence against
later drift, which is higher than the plan currently places it.

This EXTENDS the earlier line that the asymmetry "governs what an
artifact may LOCK, not what may be BUILT." That sentence was about
fingerprinted golden artifacts and is not withdrawn.

The braid is intact: the audit stays bounded by the current artifact,
stays countable, and stays off the critical path as a gate. What moved
is where it binds.

(Tony's rulings. 2026-08-27, the principle: the gate binds where a
claim reaches a reader, not where it is drawn. 2026-08-28, the
placement: "I think provenance should be settled before it leaves the
orrery to the gallery cache. There is no provenance checker in the
gallery." The second corrects the first without withdrawing it.)
"""

EDITS.append((SKILL, "S2 rewrite the gate section", OLD_GATE, NEW_GATE))


# --- S3 -- front-matter description -----------------------------------

EDITS.append((
    SKILL, "S3 front-matter description",
    "build path, and it binds at SERVING).",
    "build path, and it binds at EXPORT from the orrery).",
))


# --- P1 -- v3.46 entry -------------------------------------------------

V346 = """v3.46 (August 28, 2026): No rule changed in this document. One skill
correction, recorded here because the recording is the fourth link of
L-230's chain and the only one that does not fire on its own.

provenance-discipline 2.8 -> 2.9 (L-256). The Gate Binds at SERVING
becomes The Gate Binds at EXPORT. 2.8 was written earlier the same
evening and placed the gate where the harm lands -- a visitor taking a
served value as true. Tony's ruling of 2026-08-28 moves it upstream to
where a check can still run: "I think provenance should be settled
before it leaves the orrery to the gallery cache. There is no
provenance checker in the gallery."

Verified rather than assumed before the edit was written.
provenance_scanner.py exists only in the orrery repo. The nightly
builder lives in the GALLERY repo and scores nothing -- two mentions of
provenance in the whole file, one a docstring line recording where its
copied constants came from, one a warning string. The two repositories
do not share a checker, so a gate at publication sits downstream of the
last instrument in existence. That is A Check That Cannot Fail Is Not
Passing in the pipeline layer rather than in code.

The section now separates WHY from WHERE explicitly, because the
correction is exactly the kind a future session would undo by
reasoning from harm rather than from enforceability. Why: serving.
Where it fires: export. What stays free: drawing.

One consequence raises a priority. objects_config.json is maintained by
hand in the gallery repo, so the export boundary the gate names is
today a human copy with no check on it. The cross-repo transport
becomes the gate's missing enforcement point rather than a defence
against later drift -- higher than MASTER_PLAN_INTERACTIVE_GALLERY.md
currently places segment 2, and an amendment that document is owed.

Version history: v3.43 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

EDITS.append((
    PROTOCOL, "P1 insert v3.46 entry",
    "v3.45 (August 27, 2026): One rule added, one skill bumped, and the\n",
    V346 + "v3.45 (August 27, 2026): One rule added, one skill bumped, and the\n",
))


# --- P2 -- header ------------------------------------------------------

EDITS.append((
    PROTOCOL, "P2 header version and anchor",

    "Tony Quintanilla, PE | Claude | v3.45 | August 27, 2026\n"
    "\n"
    "Cut from 7f4a2f9f at https://github.com/tonylquintanilla/palomas_orrery\n",

    "Tony Quintanilla, PE | Claude | v3.46 | August 28, 2026\n"
    "\n"
    "Cut from a263f73d at https://github.com/tonylquintanilla/palomas_orrery\n",
))


# --- P3 -- remove v3.43 from the resident protocol --------------------

EDITS.append((
    PROTOCOL, "P3 remove v3.43 from resident protocol",
    "\n" + V343 + "\nFunctional for Claude, readable for human, signal preserved.\n",
    "\nFunctional for Claude, readable for human, signal preserved.\n",
))


# --- H1 -- append v3.43 to history ------------------------------------

EDITS.append((
    HISTORY, "H1 append v3.43 to history PART 1",
    "### Preserved verbatim: v3.29 Technical lessons (now field notes in skills)\n",
    V343
    + "\n(Moved down from the resident protocol on 2026-08-28 when v3.46\nmade a fourth entry.)\n\n"
    + "### Preserved verbatim: v3.29 Technical lessons (now field notes in skills)\n",
))


# ---------------------------------------------------------------- apply

def main():
    missing = [p for p in EXPECTED if not os.path.isfile(p)]
    if missing:
        print("FAIL: not found: %s" % ", ".join(missing))
        print("Run this from the repository root.")
        return 1

    files = {}
    for path, want in EXPECTED.items():
        raw = open(path, "rb").read()
        had_crlf = b"\r\n" in raw
        norm = raw.replace(b"\r\n", b"\n")
        got = hashlib.md5(norm).hexdigest()
        if got != want:
            print("FAIL: fingerprint mismatch on %s. Nothing was written."
                  % path)
            print("  expected: %s" % want)
            print("  actual:   %s" % got)
            print("Re-pull that file at %s." % BASE_SHA[:8])
            return 1
        try:
            text = norm.decode("ascii")
        except UnicodeDecodeError as exc:
            print("FAIL: %s is not pure ASCII (%s)." % (path, exc))
            return 1
        files[path] = {"text": text, "crlf": had_crlf,
                       "lines0": text.count("\n")}
        print("  fingerprint OK  %-46s %s"
              % (path, "CRLF" if had_crlf else "LF"))

    print("\nApplying %d edits across %d files...\n" % (len(EDITS), len(files)))

    for path, label, anchor, _repl in EDITS:
        n = files[path]["text"].count(anchor)
        if n != 1:
            print("FAIL: anchor for %s appears %d times in %s (need 1)."
                  % (label, n, path))
            print("Nothing was written.")
            return 1
    print("All %d anchors unique.\n" % len(EDITS))

    for path, label, anchor, repl in EDITS:
        files[path]["text"] = files[path]["text"].replace(anchor, repl, 1)
        print("  applied  %s" % label)

    s_txt = files[SKILL]["text"]
    p_txt = files[PROTOCOL]["text"]
    h_txt = files[HISTORY]["text"]

    print("")
    checks = [
        ("skill reads 2.9",
         "Skill version: 2.9 | Cut from palomas_orrery @ a263f73d" in s_txt),
        ("no 2.8 version line remains", "Skill version: 2.8" not in s_txt),
        ("gate section retitled to EXPORT",
         "## The Gate Binds at EXPORT [CRITICAL]" in s_txt),
        ("old SERVING heading gone",
         "## The Gate Binds at SERVING" not in s_txt),
        ("why/where separated",
         "Why the gate exists: SERVING." in s_txt
         and "Where the gate FIRES: EXPORT." in s_txt),
        ("transport consequence recorded",
         "the gate's missing enforcement point" in s_txt),
        ("front matter says EXPORT",
         "it binds at EXPORT from the orrery" in s_txt),
        ("protocol header reads v3.46",
         "| Claude | v3.46 | August 28, 2026" in p_txt),
        ("protocol re-anchored to a263f73d",
         "Cut from a263f73d at https://" in p_txt),
        ("v3.46 entry present", "v3.46 (August 28, 2026):" in p_txt),
        ("v3.43 gone from resident protocol",
         "v3.43 (August 25, 2026):" not in p_txt),
        ("exactly three resident version entries",
         sum(p_txt.count("\nv3.4%d (" % n) for n in range(0, 10)) == 3),
        ("v3.43 now in history", "v3.43 (August 25, 2026):" in h_txt),
        ("history move note present",
         "when v3.46\nmade a fourth entry" in h_txt),
        ("skill pure ASCII", all(ord(c) < 128 for c in s_txt)),
        ("protocol pure ASCII", all(ord(c) < 128 for c in p_txt)),
        ("history pure ASCII", all(ord(c) < 128 for c in h_txt)),
    ]

    failed = [n for n, ok in checks if not ok]
    for name, ok in checks:
        print("  %-42s %s" % (name, "OK" if ok else "FAIL"))

    if failed:
        print("\nFAIL: %d post-condition(s) failed. Nothing was written."
              % len(failed))
        return 1

    for path, rec in files.items():
        shutil.copy2(path, path + ".bak")
        out = rec["text"].encode("ascii")
        if rec["crlf"]:
            out = out.replace(b"\n", b"\r\n")
        with open(path, "wb") as fh:
            fh.write(out)
        print("\nWROTE %s  (%d -> %d lines)"
              % (path, rec["lines0"], rec["text"].count("\n")))

    print("")
    print("NEXT, in order:")
    print("  1. Run skills_index.py -- it should report the 2.8 -> 2.9")
    print("     transition. If it says the manifest already matched,")
    print("     something did not land; stop and look.")
    print("  2. Run maintenance_run.py.")
    print("  3. Commit and push, then confirm the remote HEAD.")
    print("  4. Reinstall provenance-discipline to your account profile.")
    print("")
    print("  Carried obligation, unchanged in shape: the NEXT session")
    print("  confirms its loaded copy reads 2.9 before provenance work.")
    print("")
    print("  NOT DONE HERE: L-256's ledger block should gain a line")
    print("  recording the 2.9 correction. Left out because the ledger's")
    print("  fingerprint depends on whether patch_L255_2 and")
    print("  ledger_index.py have run. The handoff carries it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
