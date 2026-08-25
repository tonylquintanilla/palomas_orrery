"""
patch_L250_1_braid_part3_and_L244.py

Protocol v3.43. Adds "The Braid -- The Artifact Orders the Work" to
Part 3, moves the v3.40 version-history entry down into
PROJECT_INSTRUCTIONS_HISTORY.md to keep three resident, updates L-244
with the enumeration/remediation split, and opens L-250 as the handle
for the protocol change.

Built on 2bf0d06a37cb74b143f6407d52fe242cd3d2824f at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

RUN COMMAND:  python patch_L250_1_braid_part3_and_L244.py
Save this file in the REPO ROOT, open it in VS Code, click Run.

  Success: one "ok" per edit, then "patch applied to 3 file(s)".
  Failure: ERROR / ANCHOR FAIL, nothing written.

AFTER RUNNING:
  python ledger_index.py
  python maintenance_run.py

  The Skill manifest generator rewrites its own zone in
  PROJECT_INSTRUCTIONS.md. This patch does NOT touch that zone, so the
  generator should report "unchanged". If it reports a rewrite, read
  what changed before pushing.

WHY THE VERSION HISTORY MOVES
-----------------------------
The protocol keeps the THREE most recent entries resident and a fourth
pushes the oldest down (the rule L-199 asked for, stated in the Version
History section itself). Resident today: v3.42, v3.41, v3.40. Adding
v3.43 sends v3.40 to PROJECT_INSTRUCTIONS_HISTORY.md PART 1, verbatim,
with a line saying when and why it moved -- the same form the v3.39
entry carries from the last time this happened.

An entry lives in exactly one place, never both. This patch asserts that:
it fails if the moved block is not removed from the protocol, and fails
if it does not arrive in the history file.

WHAT CHANGES

  PROJECT_INSTRUCTIONS.md
      Header v3.42 -> v3.43, date and cut-from SHA updated.
      Part 3: new section after The Artifact Bounds the Audit.
      Version History: v3.43 added, v3.40 removed.
  documentation/PROJECT_INSTRUCTIONS_HISTORY.md
      PART 1 gains the v3.40 entry verbatim.
  LEDGER_CONSOLIDATED.md
      L-244 updated; L-250 opened.
"""

import hashlib
import os
import sys

# The v3.40 entry, lifted verbatim from the protocol. The patch removes
# exactly these bytes there and inserts exactly these bytes in the
# history file, so the two operations cannot disagree.
V340 = """v3.40 (August 16, 2026): No change to the protocol's own rules. Two
skills gained conventions, and both were earned the same way -- a
session hit the problem, Tony ruled, the rule went into the skill that
fires on it rather than into this document.

safe-file-editing 1.3 -> 1.4, two additions. (1) Fix In Passing, Report
It. Where a patch is already fingerprinting a file and finds a violation
of an ALREADY-RULED convention in it, fix it in the same patch and say
so, rather than noting it and moving on. Origin: a patch touching eight
files blocked itself on two Unicode arrows in a comment that predated
the work by months. Claude's first instinct was to report and leave it,
citing "fix only what asked." Tony's ruling: the convention was already
ruled, the file was already fingerprinted, and a separate sweep for two
characters would never be scheduled, so leaving it means it never gets
fixed. The anti-pattern "fix only what asked" guards against is
unreviewed DESIGN change, not mechanical compliance with a standing
rule. The encoding gate was rescoped with it -- hard-fail on non-ASCII
in inserted lines, sweep pre-existing where the conditions hold, and
print which of the two happened, because a gate that fails on somebody
else's bug blocks a correct patch and a gate that stays silent is how a
convention quietly stops being true. (2) Naming and Archiving a Patch
Script: name it patch_<handle>_<what>.py leading with the ledger handle,
number a sequence so sort order carries run order, archive to
documentation/ once run, and state which parts of the change are
permanent when the script is not. That convention was already 96 scripts
deep in documentation/ and written down nowhere, so a session that read
the delivery format still produced three unprefixed scripts and had to
be told.

orrery-coding-conventions 1.3 -> 1.4, two additions. (1) Marker
Separation for Near-Equal Radii. Where two shells sit within about 10%
of each other, the standing r*1.05 north-pole marker puts both in the
same place and Plotly shows one where the user expects two -- geometry
correct, legend correct, affordance silently absent. The inner shell
keeps the pole; each subsequent shell steps 20 degrees in polar angle at
its own radius. Separate angularly, never radially. Origin: the
chromosphere moved to true physical scale and its marker landed 0.003
solar radii from the photosphere's, about one pixel. The section says
explicitly that this is NOT the May 2026 ring-marker fix, which solved a
collision radially and cannot help at 0.29% -- reaching for it is the
trap. (2) Harvest the Conventions You Find. When you touch a file and
find a convention this skill does not hold, report it in the same
message as the work; do not silently follow it, because following
without naming is how it stays invisible. Promotion is Tony's judgment,
not the finder's. Origin: Tony's observation that "there are many
unrecorded conventions except in local files," which the patch-script
naming convention had just demonstrated.

Process note, recorded because it is the reason this entry exists at
all. Both skill files were delivered wrong before they were delivered
right, and neither error was caught by a check. The conventions file was
named for download disambiguation rather than for its destination and
was filed in documentation/, leaving two pushed source comments citing a
20-degree rule that existed in no store the skill loader reads --
cite-to-nonexistent-authority, live in the repo. Then the corrected file
was built by an insert written as a replace, which deleted its own
version block, Source line, criticality note, and the paragraph
recording what v1.2 added. Tony found that by reading the new file
against its sibling. The rebuild added a pure-addition check -- every
line of 1.3 must still be present in 1.4 -- which is the check that
should have run the first time. Deliverables now ship inside a folder
named for their destination.

"""

BRAID = """
The Braid -- The Artifact Orders the Work
Companion to The Artifact Bounds the Audit, one axis over. That rule
governs which values are IN SCOPE at all. This one governs which are in
scope NEXT -- and it applies to any correctness program, not only to
provenance.

A precondition that does not terminate is not a plan. Run an audit, a
migration or a sweep GLOBALLY and it has no denominator: it cannot
finish, and it cannot be sized, so it silently becomes a gate on
everything downstream of it. Bound it to what the CURRENT ARTIFACT
renders and it becomes countable, which is the whole point.

The test is mechanical. If the current artifact does not reach it, it
waits.

Two halves, both load-bearing. The program does not STOP -- it stops
being a GATE; the general work continues beside the delivery work rather
than in front of it. And a finding outside the current slice is
RECORDED, not chased: ONE ledger row per CLASS, never one per instance,
so the backlog grows by kinds rather than by counts.

Separate DISCOVERY from REMEDIATION and neither becomes a search.
Discovery enumerates against a stated pattern and terminates because the
tree is finite; it produces a list and fixes nothing. Remediation
happens later, in slices. When the two are the SAME activity, each fix
surfaces the next and there is no stopping condition -- "no more
findings" is not a thing anyone can verify.

The tell that this rule is being violated is a correctness program whose
next step is always generated by its last one.

(Tony's ruling, August 22 2026, for provenance -- the braid; generalized
August 25 2026 after a constants migration ran global and did not
terminate. One conversion factor led to a shadow name, to three aliases,
to a second constant at 38 sites across 11 modules, in a single evening,
while the artifact on the critical path moved not at all. Section 5a of
MASTER_PLAN_INTERACTIVE_GALLERY.md carries the sequencing form; this is
the principle. L-250.)

"""

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

L244_NOTE = """**Note (2026-08-25) -- the dispatch is bounded, and this is its shape.**
Raised by Tony: a sweep of this kind "can become its own rabbit hole,
chasing all the findings."
- **The hole opens only when DISCOVERY and REMEDIATION are the same
  activity.** That is what happened on 2026-08-25: fixing while
  searching, so every fix opened the next search, with no stopping
  condition because "no more findings" cannot be verified. Fable
  ENUMERATES and fixes nothing. The output is ledger rows; the fixing
  happens later, in slices, under The Braid (PROJECT_INSTRUCTIONS Part
  3, added v3.43).
- **The denominator is finite and measured at `2bf0d06a`:** 55
  module-level names in `constants_new.py`, four of them derived,
  against roughly 1,100 distinct multi-decimal literals in the live
  tree.
- **The pattern is mechanical:** a numeric literal equal to a value
  already named in `constants_new.py`, or derivable from named values
  within one or two steps, within a stated rounding tolerance. That
  definition catches `3.26156` and `4.74` and needs no judgment about
  what counts as a physical constant -- which is the wider version that
  would not terminate.
- **Report by CONSTANT, not by SITE.** One row per constant-and-module
  pair with a count, not one per occurrence. `3.26156` is ONE finding
  across eleven modules, the way L-248 writes it. Otherwise the sweep
  inflates the ledger by an order of magnitude and creates a second
  problem while solving the first.
- **Timing: the enumeration runs BESIDE the Earth build, not before
  it.** It touches no file and runs outside the project context window,
  which is what the Mode 7 scoping leg is for. Wait for
  `patch_L248_1` and L-249 to land so it is not enumerating values
  about to change; a few days of staleness would not matter for a
  sizing exercise, but those two are close.
- **Why the enumeration is worth doing soon even though remediation is
  not.** The dangerous crack is the undocumented one. A count turns
  "there may be more of these" into a finite list with RICE scores,
  which is the difference between a background worry and a backlog.
**Ref (added):** L-248; L-250; PROJECT_INSTRUCTIONS Part 3, The Braid.
"""

BLOCK_250 = """#### [L-250] The Braid added to Part 3 as a general principle
<!-- L:250 status:DONE upd:2026-08-25 section:C flag: rice:4/4/95/1 -->
- **Protocol v3.43, 2026-08-25.** "The Braid -- The Artifact Orders the
  Work" added to Part 3 directly after The Artifact Bounds the Audit,
  which it extends by one axis: that rule bounds which values are in
  scope, this one bounds which are in scope NEXT, and it applies to any
  correctness program rather than to provenance alone.
- **Why it was not already there.** Tony's ruling of 2026-08-22 lived
  only in `MASTER_PLAN_INTERACTIVE_GALLERY.md` Section 5a, which carries
  SEQUENCING authority for the gallery. He was applying it to the
  constants work as well -- from memory, because it was written nowhere
  that fires. Tony, 2026-08-25: "it is a meta-principle. its not even in
  the protocol as such."
- **What made it urgent.** A constants migration ran global on
  2026-08-25 and did not terminate. One conversion factor led to a
  shadow name, to three aliases, to a second constant at 38 sites across
  11 modules, in a single evening, while the artifact on the critical
  path moved not at all. Every step was locally justified and nobody
  chose the day's shape.
- **Two additions beyond the master plan's version.** The
  DISCOVERY/REMEDIATION split -- discovery enumerates against a stated
  pattern and fixes nothing, so it terminates because the tree is finite
  -- and ONE ledger row per CLASS rather than one per instance, so the
  backlog grows by kinds instead of counts.
- **Version history.** v3.40 moved down to
  `documentation/PROJECT_INSTRUCTIONS_HISTORY.md` PART 1 to keep three
  entries resident, per the rule L-199 asked for.
**Gap:** none. Closed on delivery.
**Ref:** PROJECT_INSTRUCTIONS v3.43 Part 3; L-244 (the first program the
rule bounds); L-248; L-199 (the three-resident cap); The Artifact Bounds
the Audit.

"""

FILES = {

    "PROJECT_INSTRUCTIONS.md": (
        "5114efdd2d23e018e01e94e86f02cea3", [
            ("header v3.42 -> v3.43",
             "Tony Quintanilla, PE | Claude | v3.42 | August 23, 2026\n\n"
             "Cut from 41c0b279 at https://github.com/tonylquintanilla/palomas_orrery\n",
             "Tony Quintanilla, PE | Claude | v3.43 | August 25, 2026\n\n"
             "Cut from 2bf0d06a at https://github.com/tonylquintanilla/palomas_orrery\n"),
            ("Part 3: The Braid added after The Artifact Bounds the Audit",
             "half is his nuance, and it is the half a completeness instinct will drop.)\n",
             "half is his nuance, and it is the half a completeness instinct will drop.)\n"
             + BRAID),
            ("version history: v3.43 added",
             "v3.42 (August 23, 2026): No rule changed in this document. THREE skill\n",
             V343 + "v3.42 (August 23, 2026): No rule changed in this document. THREE skill\n"),
            ("version history: v3.40 removed", V340, ""),
        ]),

    "documentation/PROJECT_INSTRUCTIONS_HISTORY.md": (
        "6bf0a8a4c71051c0a70d9d033b393d7d", [
            ("PART 1 receives v3.40",
             "### Preserved verbatim: v3.29 Technical lessons (now field notes in skills)\n",
             V340
             + "(Moved down from the resident protocol on 2026-08-25 when v3.43\nmade a fourth entry.)\n\n"
             + "### Preserved verbatim: v3.29 Technical lessons (now field notes in skills)\n"),
        ]),

    "LEDGER_CONSOLIDATED.md": (
        "83b3acf2d70602e6a960f3ac0dbe49b1", [
            ("L-244 gains the dispatch shape",
             "**Ref:** L-243 (the narrow instance); L-181; L-190 (scanner reach).\n",
             L244_NOTE
             + "**Ref:** L-243 (the narrow instance); L-181; L-190 (scanner reach).\n"),
            ("open L-250",
             "\n## PENDING ACTION (Tony-side)\n",
             "\n" + BLOCK_250 + "## PENDING ACTION (Tony-side)\n"),
        ]),
}


def main():
    if not os.path.exists("constants_new.py"):
        print("ERROR: run this from the repo root (constants_new.py not found here).")
        return 1

    staged = {}
    for path, (base_fp, edits) in FILES.items():
        if not os.path.exists(path):
            print("ERROR: %s not found. Nothing written." % path)
            return 1
        data = open(path, "rb").read()
        fp = hashlib.md5(data.replace(b"\r\n", b"\n")).hexdigest()
        if fp != base_fp:
            print("ERROR: base moved for %s." % path)
            print("  expected content-md5 %s" % base_fp)
            print("  found                %s" % fp)
            print("  Nothing written.")
            return 1
        is_crlf = data.count(b"\r\n") > 0
        print("base ok  %-46s (%s)" % (path, "CRLF" if is_crlf else "LF"))

        out = data
        for label, old, new in edits:
            try:
                new.encode("ascii")
            except UnicodeEncodeError as e:
                print("ERROR: non-ASCII in inserted text, %s / %s: %s"
                      % (path, label, e))
                return 1
            o, n = old.encode("ascii"), new.encode("ascii")
            if is_crlf:
                o = o.replace(b"\n", b"\r\n")
                n = n.replace(b"\n", b"\r\n")
            c = out.count(o)
            if c != 1:
                print("ANCHOR FAIL [%s / %s]: expected 1 match, got %d"
                      % (path, label, c))
                print("  Nothing written.")
                return 1
            out = out.replace(o, n)
            print("ok  %-46s %s" % (path, label))

        staged[path] = (data, out, is_crlf)

    # An entry lives in exactly one place. Assert the move happened both ways.
    proto = staged["PROJECT_INSTRUCTIONS.md"][1].replace(b"\r\n", b"\n")
    hist = staged["documentation/PROJECT_INSTRUCTIONS_HISTORY.md"][1].replace(b"\r\n", b"\n")
    tag = b"v3.40 (August 16, 2026):"
    if tag in proto:
        print("ERROR: v3.40 still present in the protocol. Nothing written.")
        return 1
    if hist.count(tag) != 1:
        print("ERROR: v3.40 appears %d time(s) in the history file, expected 1. "
              "Nothing written." % hist.count(tag))
        return 1
    print("ok  v3.40 lives in exactly one place (removed above, present below)")

    # Three version entries resident, not four.
    resident = sum(proto.count(b"\nv3.%d (" % n) for n in (39, 40, 41, 42, 43))
    if resident != 3:
        print("ERROR: %d version entries resident, expected 3. Nothing written."
              % resident)
        return 1
    print("ok  three version entries resident (v3.43, v3.42, v3.41)")

    # The generated manifest zone must be untouched.
    before = staged["PROJECT_INSTRUCTIONS.md"][0].replace(b"\r\n", b"\n")
    def zone(b):
        i = b.find(b"<!-- SKILL-MANIFEST:START")
        j = b.find(b"<!-- SKILL-MANIFEST:END")
        return b[i:j]
    if zone(before) != zone(proto):
        print("ERROR: the generated skill-manifest zone changed. Nothing written.")
        return 1
    print("ok  skill-manifest zone byte-identical")

    for path, (_b, after, _c) in staged.items():
        open(path, "wb").write(after)

    print("")
    print("patch applied to %d file(s)" % len(staged))
    for path, (before_b, after, crlf) in staged.items():
        print("  %-46s %+6d bytes  (%s)"
              % (path, len(after) - len(before_b), "CRLF" if crlf else "LF"))
    print("")
    print("NEXT, in order:")
    print("  1. python ledger_index.py")
    print("  2. python maintenance_run.py")
    print("     Skill manifest should report 'unchanged'. If it rewrites,")
    print("     read what changed before pushing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
