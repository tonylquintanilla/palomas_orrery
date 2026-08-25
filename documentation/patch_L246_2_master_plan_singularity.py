"""
patch_L246_2_master_plan_singularity.py

Writes the 2026-08-25 session into the two planning documents. Both were
last revised on 2026-08-23 and neither carries the ruling of the 25th,
so a note about today's work added on its own would sit inside a plan
that contradicts it.

Built on 1526a9cac5be3279bb62e6ddc467f9d59b9fb731 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

RUN COMMAND:  python patch_L246_2_master_plan_singularity.py
Save this file in the REPO ROOT, open it in VS Code, click Run.

  Success: two "ok" lines, then "patch applied to 2 file(s)".
  Failure: ERROR / ANCHOR FAIL, nothing written.

AFTER RUNNING:  python maintenance_run.py

WHAT THIS IS, AND WHAT IT IS NOT
--------------------------------
It is an APPEND to each document: one dated subsection in Section 5a of
the gallery master plan, one dated section in the critical-path summary.
Both new blocks say what changed on 2026-08-25 and leave the earlier
text standing.

It is NOT a re-sync. Both documents still carry 2026-08-23 readings in
their existing tables -- "Segment 3, assembler draw: NOT STARTED",
"Artifact 1, Earth: LOCKED" -- and those are now wrong. The new blocks
say so explicitly and name the rows, rather than editing them in place,
because a summary table re-measured without re-reading its source is
how the 105 / 107 / 110 drift happened in this same file. Re-measuring
those rows is its own pass against a live read.

WHAT CHANGES

  MASTER_PLAN_INTERACTIVE_GALLERY.md
      Section 5a gains a subsection before "What this section
      deliberately does not carry".
  MASTER_PLAN_CRITICAL_PATH_SUMMARY.md
      A section before "What would change the picture".
"""

import hashlib
import os
import sys

GALLERY_BLOCK = """### 2026-08-25 -- two changes, and a property the plan never named

Appended, not merged. The tables above were read on 2026-08-23 and two
of their rows are now wrong; they are named at the end of this
subsection rather than edited here.

**One. Artifacts reopen, and the ladder has a second axis.** Tony's
ruling, 2026-08-25. The seven golden artifacts are seven PROPAGATION
shapes -- conic, planetocentric, mean elements, spacecraft arc,
barycentric binary. That ladder is complete and unchanged. What the
orrery DRAWS is a different axis entirely: interiors, atmospheres,
magnetospheres, belts, tori, rings, comae, solar shells, Hill spheres.
Nothing in the five segments or the seven artifacts sequences that axis,
and nobody ever decided that some of it would be shown interactive-side
and some not. L-100 carried that as an inherited default from the
Phase-1b cost framing of 2026-07-08; it was never a ruling and is now
closed. Tony: "it is not my intent. The general intent is to redo the
orrery in the assembler. Part by part."

The consequence that arrives first: the resolver requests EVERY feature
key the cache carries for an object, and a golden record hashes
`feature_keys`, `trace_role_counts` and `legend_groups`. So adding a
feature family to a body FAILS every locked artifact containing it.
Under part-by-part that is the normal event, not an edge case, and
re-locking is normal rather than a failure. L-234 carries the work;
Artifact 1's Sun half is DONE, its Earth half is open.

**Two. A property this plan has been folding into provenance, and
should not.** Segment 1 reads "one store for feature constants,
provenance carried as data." Those are two independent properties and
only the second has ever had measurement, tooling or a place in the
order.

  PROVENANCE asks: is this value sourced?
  SINGULARITY asks: is there ONE of it?

A value can hold either without the other, and on 2026-08-25 one clean
example of each turned up:

`KM_PER_AU` is cited about as well as anything in the tree -- IAU 2012
Resolution B2, exact definition, two independent cross-checks recorded.
It also existed as thirteen literal copies across seven live modules,
one of them under a different name (`AU_KM`), plus three more names
aliasing the import. Perfect provenance, five names, sixteen sites.

S4714's semi-major axis is the inverse. Three stores held it: the
catalog said 520.0 and two consumer modules overwrote it to 800.0 at
import time, so which value a render used depended on import order. A
live path saw neither override, so the same star was drawn two ways --
and each view's prose was correct for its own value, one reporting 8.2%
of light speed at periapsis and the other 10%. The number drawn was
unsourced; the citation on file described the number that was not drawn.

**Why the audit could not see either.** The scanner scores literal
assignments. A second copy of a correctly-cited value is not a finding,
and a runtime dict mutation is not an assignment at all. So a Tier-1
count says nothing about how many places a value lives. Neither does the
drift checker: `constants_change_report.py` watches ONE file, so "No
changes to constants_new.py" was true and silent while a value moved
from 520 to 800 in a store it does not read. L-245 widens that check's
window in time; this widens it in space.

**Where this sits in the order: NOT on the path to Artifact 2.** Nothing
in it touches Saturn's rings or Jupiter's belts. It is recorded here so
it is visible, and it is explicitly not a gate -- the same reasoning the
braid ruling applied to the general audit on 2026-08-22. Handles: L-243
(the AU factor, closed 2026-08-25), L-244 (the class sweep, a Fable
candidate), L-246 (S4714, structural half closed), and the migration of
eight cited scalars out of `sgr_a_star_data.py` into `constants_new.py`.
The S-star catalog itself does NOT migrate as it stands -- it mixes
orbital elements with hex colours and prose, and needs L-240's
measured-versus-declared split first.

**Two rows above are stale and are deliberately left standing.**
"Segment 3, assembler draw: NOT STARTED" -- the Sun is now complete in
the assembler, 19 shells, Mode 5 passed on 2026-08-24 and 2026-08-25.
"Artifact 1, Earth: LOCKED" -- reopened by the ruling above, and its
golden record is stale in four fields (L-237). Re-measuring those rows
belongs to a pass that reads the repo, not to this append; a table
re-stated from memory is how the 105 / 107 / 110 drift happened in this
document.

"""

CRITICAL_PATH_BLOCK = """## Two properties, not one

**Added 2026-08-25.** The rest of this document was written on
2026-08-23 and is not re-measured here.

This file opens by saying the assembler creates no data, it imports, and
that everything except positions travels by being copied. True, and
incomplete in a way that only became visible on 2026-08-25.

Whether a number is SOURCED and whether there is only ONE of it are
different questions. The provenance work answers the first. Nothing has
been answering the second, and no tool in the routine can: the scanner
scores literal assignments, so a second copy of a correctly-cited value
raises nothing, and a value overwritten at runtime is not an assignment
at all.

Two findings on the same day, one of each kind.

**Perfect citation, sixteen sites.** `KM_PER_AU` carries the IAU 2012
Resolution B2 definition with two independent cross-checks recorded
beside it. It also appeared as thirteen literal copies across seven live
modules -- one under a different name -- with three further names
aliasing the import. Nothing was wrong with the number anywhere. There
were simply five names for it.

**Three stores, two values, and two renders that disagreed.** The S-star
catalog held S4714's semi-major axis as 520 AU. Two viewer modules
reached into that shared dictionary at import time and set it to 800.
A third viewer imported neither, so it drew the star at 520 -- and said
so on the plot, annotating 10% of light speed where the others said 8%.
Both figures were arithmetically right for the value each view was
holding. The drawn number was unsourced; the citation on file described
the number that was not drawn.

**And the check that should have caught the second one reported clean.**
`constants_change_report.py` compares `constants_new.py` against its last
commit. S4714 does not live there. "No changes to constants_new.py" was
true, and said nothing at all about a value that moved by 54% in a file
one directory over. The checker's scope is its denominator, and the
output does not name it.

**What this does NOT change.** None of it is on the path to Artifact 2.
Saturn's rings and Jupiter's belts are untouched by any of it. It is
written here because a reader asking "how far to the end" deserves to
know that a whole property of the constant layer had no measurement
until now -- not because it belongs in front of the rendering work. The
argument is the same one made on 2026-08-22 about the general audit: a
precondition that does not terminate is not a plan, and this one has no
denominator yet either.

Handles: L-243 (the AU factor, closed same day), L-244 (the class sweep,
scoping not started), L-246 (S4714, structural half closed and the
measured value routed to a dispatch), L-245 (the drift check's window).

One further note, because it is the reason this section exists rather
than a ledger row alone. Both findings were surfaced by a person
looking: one by Tony's standing instruction that conversion factors be
called rather than replicated, one by a Mode 5 screenshot sent to
confirm something unrelated. Neither came from a passing check, and no
check in the routine would have produced either.

---

"""

FILES = {
    "documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md": (
        "b0e76054edb96f6f5a39bdf56c05513c", [
            ("Section 5a gains the 2026-08-25 subsection",
             "### What this section deliberately does not carry\n",
             GALLERY_BLOCK + "### What this section deliberately does not carry\n"),
        ]),
    "documentation/MASTER_PLAN_CRITICAL_PATH_SUMMARY.md": (
        "b26f277763e158f286488d44416e51f1", [
            ("two-properties section added",
             "## What would change the picture\n",
             CRITICAL_PATH_BLOCK + "## What would change the picture\n"),
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
        print("base ok  %-52s (%s)" % (path, "CRLF" if is_crlf else "LF"))

        out = data
        for label, old, new in edits:
            try:
                new.encode("ascii")
            except UnicodeEncodeError as e:
                print("ERROR: non-ASCII in replacement for %s: %s" % (path, e))
                return 1
            o, n = old.encode("ascii"), new.encode("ascii")
            if is_crlf:
                o = o.replace(b"\n", b"\r\n")
                n = n.replace(b"\n", b"\r\n")
            c = out.count(o)
            if c != 1:
                print("ANCHOR FAIL [%s]: expected 1 match, got %d" % (label, c))
                print("  Nothing written.")
                return 1
            out = out.replace(o, n)
            print("ok  %s" % label)

        staged[path] = (data, out, is_crlf)

    for path, (_b, after, _c) in staged.items():
        open(path, "wb").write(after)

    print("")
    print("patch applied to %d file(s)" % len(staged))
    for path, (before, after, crlf) in staged.items():
        print("  %-52s %+6d bytes  (%s)"
              % (path, len(after) - len(before), "CRLF" if crlf else "LF"))
    print("")
    print("NEXT: python maintenance_run.py")
    print("")
    print("STILL STALE, deliberately, and named inside the new text:")
    print("  Section 5a 'You are here': Segment 3 reads NOT STARTED (the Sun")
    print("  is complete in the assembler) and Artifact 1 reads LOCKED (it")
    print("  reopened on 2026-08-25). Re-measuring those rows is a pass that")
    print("  reads the repo, not an append.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
