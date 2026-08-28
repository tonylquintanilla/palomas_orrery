"""
patch_L256_2_protocol_v3_45_and_ledger.py

Completes the four-link chain for the provenance-discipline 2.8 bump.

Built on palomas_orrery @ 7f4a2f9f046bc00ad9e418367b42beffaff89e7b
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

RUN THIS SECOND. patch_L256_1_provenance_discipline_2_8.py bumps the
skill; skills_index.py regenerates the manifest zone; this patch writes
the protocol version entry and the ledger rows. Link four is the one
that never fires on its own (L-230), which is why it is a patch rather
than a habit.

WHAT THIS DOES -- three files, eight edits, all-or-nothing.

  PROJECT_INSTRUCTIONS.md
    - header to v3.45, dated 2026-08-27, re-anchored to 7f4a2f9f
    - new section: Method Belongs to the Skill [QUALITY], placed after
      The Braid, which it extends by one axis
    - v3.45 version entry added at the top of Version History
    - v3.42 entry REMOVED (three stay resident; a fourth pushes the
      oldest down)

  documentation/PROJECT_INSTRUCTIONS_HISTORY.md
    - v3.42 appended to the end of PART 1, so it lives in exactly one
      place

  LEDGER_CONSOLIDATED.md
    - two DETAIL blocks: L-256 (the 2.8 bump and the status pass) and
      L-257 (the three enforcement builds the skill text defers)
    - the INDEX is NOT touched. It is generated. Run ledger_index.py
      after this patch.

SAFETY
  - MD5 guard on all THREE targets, computed after normalizing line
    endings, checked before anything is written.
  - Every anchor asserted unique across all files first.
  - All three files written only if every post-condition passes.
  - Original line-ending style preserved per file; .bak beside each.

HOW TO RUN
  Open in VS Code and press Run, with the repo root as the working
  directory. No arguments, no prompts.

Module updated: August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import shutil
import sys

PROTOCOL = "PROJECT_INSTRUCTIONS.md"
HISTORY = os.path.join("documentation", "PROJECT_INSTRUCTIONS_HISTORY.md")
LEDGER = "LEDGER_CONSOLIDATED.md"

EXPECTED = {
    PROTOCOL: "e79a7c3a73d5346501980bad71327572",
    HISTORY: "48d270742a786dd7f3358b3f7935899e",
    LEDGER: "a6cc5102a5de2d696cb32888395c002c",
}

BASE_SHA = "7f4a2f9f046bc00ad9e418367b42beffaff89e7b"


# ------------------------------------------------- the v3.42 entry text
# Removed from the protocol verbatim and appended to history verbatim.
# Defined once so the two halves cannot drift apart.

V342 = """v3.42 (August 23, 2026): No rule changed in this document. THREE skill
bumps, recorded here because the recording is the point.
(1) safe-file-editing 1.7 -> 1.8 (L-226), two of Tony's rulings. The
Encoding Gate now says PROSE explicitly -- it read "ASCII only in
delivered code" and a session took that as excluding markdown, leaving
23 non-ASCII characters in a master plan it was already patching, while
Stamp What You Change had said all along that markdown is not an
exception. The skill's two halves disagreed and the reader followed the
narrower one. And a new section, The Correction Does Not Travel, one
scope out from Stamp What You Change: that governs the file the patch is
editing, this governs the OTHER files quoting the value it just changed.
Founding case -- constants_new.py read 15 R_sun from August 22 and the
critical path summary still said 17 the next day, inside the paragraph
written to correct an earlier wrong claim about the same row.
(2) orrery-coding-conventions 1.4 -> 1.5 (L-227): Hover Line Width Is a
Convention, Not an Accident. Found by Mode 5 when a tooltip ran off the
viewport -- a hover string wrapped at 72 characters in the SOURCE with
no breaks on the lines, rendering as one 378-character run. Canonical
Text Format already governed which break character and said nothing
about how often.
(3) ledger-and-session-records 1.8 -> 1.9 (L-230), and it is why this
entry exists at all. Tony observed that a skill bump runs a four-link
chain -- SKILL.md, skills_index.py, the manifest zone, a protocol
version entry -- and that only the first three fire. The binding rule
gains its fourth step. Detection is designed and unbuilt: a
maintenance-suite checker that watches the TRANSITION, because the
naive form reports 10 of 10 skills and would be ignored by its second
run.
"""


# ---------------------------------------------------------------- edits
# (file, label, anchor, replacement)

EDITS = []


# --- P1 -- header ------------------------------------------------------

EDITS.append((
    PROTOCOL, "P1 header version and anchor",

    "Tony Quintanilla, PE | Claude | v3.44 | August 26, 2026\n"
    "\n"
    "Cut from 3faa72a0 at https://github.com/tonylquintanilla/palomas_orrery\n",

    "Tony Quintanilla, PE | Claude | v3.45 | August 27, 2026\n"
    "\n"
    "Cut from 7f4a2f9f at https://github.com/tonylquintanilla/palomas_orrery\n",
))


# --- P2 -- Method Belongs to the Skill, after The Braid ----------------

METHOD_ROUTING = """Method Belongs to the Skill
Companion to The Braid, one axis over again. That rule governs which
work is in scope next. This one governs who decides it.

A question about HOW THE WORK IS DONE is a skill rule. A question about
WHAT THIS PROJECT SHOULD BE is Tony's. Escalating the first kind is not
caution -- it spends the scarcest thing in the project, which is Tony's
attention, on something a rule can absorb permanently.

The test is whether the answer would be the same next month for a
different constant, a different body, a different file. If it would, it
is method: write it into the skill that fires on it, and bring Tony a
case the rule cannot express rather than the case itself.

Two failure directions, and the second is the quieter one. Escalating
method makes Tony the bottleneck on things that recur. Absorbing a
judgment call into a skill makes a rule out of something that was never
ruled -- and a skill loads every session, so it will be followed without
being noticed.

When it is unclear which kind a question is, ask THAT rather than
asking the question: "is this mine or the skill's?" is one item, and
answering it settles a class.

(Tony's rulings, August 27 2026, three in one evening: "Status line:
this should be decided by the skill unless there is a new edge case
referred to conversation," "Any model can cite. I thought you worked out
a mechanism to check," and -- on a range-handling question escalated in
the same message that had just conceded the point -- "Isn't #4 also a
skill method?" Both independent Mode 7 reviewers named the same pattern
the same day: decisions reach the sole integrator that a rule should
absorb. L-256.)



"""

EDITS.append((
    PROTOCOL, "P2 insert Method Belongs to the Skill",
    "PART 4: FOUNDATION\n",
    METHOD_ROUTING + "PART 4: FOUNDATION\n",
))


# --- P3 -- v3.45 version entry ----------------------------------------

V345 = """v3.45 (August 27, 2026): One rule added, one skill bumped, and the
rule was earned in the same session that produced the bump.

Method Belongs to the Skill [Part 3, after The Braid]. A question about
how the work is done is a skill rule; a question about what the project
should be is Tony's. Origin: three method questions escalated to him in
one evening -- the status-line format, the mechanism for checking a
citation, and which end of a sourced range to draw. He sent all three
back, the third with "Isn't #4 also a skill method?" after Claude had
conceded the principle two sentences earlier and then escalated anyway.
Both independent Mode 7 reviewers, working from the same prompt on the
same day and without seeing each other, had already named this as a
finding: decisions reach the sole integrator that a rule should absorb.

provenance-discipline 2.7 -> 2.8 (L-256), nine sections and four
revisions. The Gate Binds at SERVING moves the binding point from
drawing to publication -- a visitor takes what the site shows as true,
and nothing downstream of the orrery knows what a correct radius is. The
Access Standard makes reachability a precondition of a citation: open
full text, a free abstract, or a Scholar or Books snippet carrying the
qualifier, and no paywalls, because Tony has no research library. The
Status Line has every value in constants_new.py declare its own
provenance state so the scanner reads instead of inferring -- which
deletes the inference machinery behind four measured failures, the
thirty-line lookback among them. Measured Is the Goal, Declared Is the
Fallback carries the range rule: store the range as data, derive the
drawn value by a stated rule, and put the reason for the pick on the
row. The Exhibit Requirement makes a verdict without a quotation
UNVERIFIED, with the quotation demoted from the clearance to a routing
aid and the source text read in context becoming the evidence of record.
Retired in the same bump: the two-annotation criterion for
V_CROSS_CHECKED, which measures concurrence, and concurrence is what
kept a wrong Alfven surface alive while the dissenting leg carried the
evidence.

One defect worth recording rather than quietly fixing. The skill had
taught the chromosphere drawn at 1.1 solar radii as its worked example
of a declared visualization boundary, for eleven days after the code
promoted that value to the physical figure. A session read it and
reported the retired value to Tony as current -- the third superseded
state that session pulled forward from a document rather than from the
store, which is the argument for the status line stated as evidence
instead of as an idea. Examples Go Stale Like Values [QUALITY] is the
rule that follows.

Version history: v3.42 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

EDITS.append((
    PROTOCOL, "P3 insert v3.45 entry",
    "v3.44 (August 26, 2026): No rule changed in this document. TWO skill\n",
    V345 + "v3.44 (August 26, 2026): No rule changed in this document. TWO skill\n",
))


# --- P4 -- remove the v3.42 entry from the resident protocol ----------

EDITS.append((
    PROTOCOL, "P4 remove v3.42 from resident protocol",
    "\n" + V342 + "\nFunctional for Claude, readable for human, signal preserved.\n",
    "\nFunctional for Claude, readable for human, signal preserved.\n",
))


# --- H1 -- append v3.42 to the end of history PART 1 -------------------

EDITS.append((
    HISTORY, "H1 append v3.42 to history PART 1",
    "### Preserved verbatim: v3.29 Technical lessons (now field notes in skills)\n",

    V342
    + "\n(Moved down from the resident protocol on 2026-08-27 when v3.45\nmade a fourth entry.)\n\n"
    + "### Preserved verbatim: v3.29 Technical lessons (now field notes in skills)\n",
))


# --- L1 -- ledger DETAIL blocks ---------------------------------------

LEDGER_ROWS = """#### [L-256] provenance-discipline 2.8, and the status pass it enables
<!-- L:256 status:OPEN upd:2026-08-27 section:A flag: rice:3/3/70/2 -->
- **What landed.** Nine sections and four revisions, from Tony's rulings
  of 2026-08-27 and two independent Mode 7 reviews returned the same
  day. Delivered as `patch_L256_1_provenance_discipline_2_8.py` and
  `patch_L256_2_protocol_v3_45_and_ledger.py`; drafts at
  `documentation/DRAFT_provenance_discipline_2_8_sections.md` and its
  companion additions file.
- **The load-bearing one is The Status Line.** Every value in
  `constants_new.py` declares its own kind (measured / declared /
  derived) and, for measured values, its rung. The scanner READS that
  instead of inferring it. Four measured failures trace to the
  inference and all four die with it: the thirty-line lookback
  crediting a neighbour's annotation (the Oort case, L-192),
  `# Verified:` matching the citation pattern, a bare URL in a
  breadcrumb scoring as a source (L-253), and orphan section-header
  annotations the grammar cannot express.
- **The Access Standard is Tony's, and it is narrower than it sounds.**
  No paywalls -- open full text, a free abstract, or a Scholar or Books
  snippet carrying the qualifier. Measured against the store the same
  evening: most citations already pass, NASA ADS closes the pre-arXiv
  astronomy gap, and the casualty list is three textbooks plus PREM.
  Remedy is re-homing to an accessible authority, not deletion.
- **The status pass, in two stages, both status-only.** BETA on the
  Sun's nineteen plus one dict, because the Sun's values happen to
  contain every hard case -- an exact definition, a frame qualifier, a
  value re-sourced after an error, a pre-arXiv citation, a textbook, a
  derived value, a range midpoint, and a pure declared block. Then the
  FULL store. Measured at `7f4a2f9f`: 67 top-level assignments (46
  literal scalars, 16 expressions, 3 dicts, 2 lists), with the dicts
  holding 160 entries and the lists 14 -- about 236 statusable items,
  of which 160 sit inside dicts. The beta must therefore include a dict
  or it proves the format for 30 percent of the store.
- **No value changes in the pass.** Discovery and remediation stay
  separated per The Braid. Rows that need to move are recorded and
  fixed later, by the ladder step that serves them.
- **A second output nobody has counted.** The pass can only status what
  is IN the store. Measured values living as bare literals inside
  function bodies (belt distances) and values held in three stores at
  once (the S4714 case) are outside it. The pass produces that count as
  a by-product; it is L-181's backlog getting its first denominator.
  Report the number before acting on it.
- **Note:** RICE 3/3/70/2 is Claude's proposed score. Reach 70 because
  the status line changes what every future provenance session reads
  first.
  **Tony-action (decide):** confirm or redirect the score, and rule on
  which dict joins the beta (`spectral_subclass_temps`, 9 entries and
  flagged by Fable in August as an uncited physical claim inside the
  store, or `CENTER_BODY_RADII`, 18 entries).
**Gap:** the status pass has not started. The beta is scoped and
unscheduled.
**Ref:** L-181 (single-source-of-truth constant layer); L-192 (the
attachment window); L-249 (Earth interior, the founding case for
measured-is-the-goal); L-253 (A Breadcrumb Must Not Cite); L-257 (the
enforcement builds); The Braid [CRITICAL] and Method Belongs to the
Skill, resident protocol Part 3.

#### [L-257] Three enforcement builds the 2.8 skill text defers
<!-- L:257 status:OPEN upd:2026-08-27 section:A flag: rice:2/3/60/2 -->
- **Why one row and not three.** All three are the same failure shape:
  a rule stated only in a skill fires when somebody remembers it. Per
  the braid, one row per class.
- **(a) Worksheet schema gains required `quote` and `locator`
  fields**, with a missing exhibit routed to UNVERIFIED rather than
  weighed. The rule is in The Exhibit Requirement; the checker that
  refuses such a row does not exist.
- **(b) Status-line parser.** The scanner reads `# Status:` and reports
  a measured value carrying none as UNEXAMINED rather than passing it.
  This is the "make the blind spot announce" half of A Check That
  Cannot Fail Is Not Passing; without it a partial pass is invisible.
- **(c) Remove the inference.** The thirty-line lookback and the
  citation-pattern matching stop scoring rungs once (b) lands.
  Declaration and inference must not both be live, or the property has
  two stores and One Value, One Home is violated on a property instead
  of a number.
- **Ordering.** (b) and (c) land only AFTER the full status pass
  completes, because wiring the scanner to read status makes the status
  authoritative, and a set of claims should not become authoritative
  before the independent review pass has read them.
- **The review pass is structural, not factual.** Checking a status
  assignment asks whether a source exists, whether it has been
  access-tested, and whether a value is measured or a pick from a
  range. No astronomy, so ONE leg, no worksheets, and none of the
  dispatch machinery.
- **Note:** RICE 2/3/60/2 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Gap:** all three unbuilt. (a) is independent and can precede the
status pass; (b) and (c) are gated on it.
**Ref:** L-256; A Check That Cannot Fail Is Not Passing [CRITICAL],
resident protocol Part 3.

"""

EDITS.append((
    LEDGER, "L1 insert L-256 and L-257 DETAIL blocks",
    "## PENDING ACTION (Tony-side)\n",
    LEDGER_ROWS + "## PENDING ACTION (Tony-side)\n",
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
        print("  fingerprint OK  %-46s %s" % (path, "CRLF" if had_crlf else "LF"))

    print("\nApplying %d edits across %d files...\n" % (len(EDITS), len(files)))

    # Pass 1: uniqueness, no writes.
    for path, label, anchor, _repl in EDITS:
        n = files[path]["text"].count(anchor)
        if n != 1:
            print("FAIL: anchor for %s appears %d times in %s (need 1)."
                  % (label, n, path))
            print("Nothing was written.")
            return 1
    print("All %d anchors unique.\n" % len(EDITS))

    # Pass 2: apply in memory.
    for path, label, anchor, repl in EDITS:
        files[path]["text"] = files[path]["text"].replace(anchor, repl, 1)
        print("  applied  %s" % label)

    p_txt = files[PROTOCOL]["text"]
    h_txt = files[HISTORY]["text"]
    l_txt = files[LEDGER]["text"]

    print("")
    checks = [
        ("protocol header reads v3.45",
         "| Claude | v3.45 | August 27, 2026" in p_txt),
        ("protocol re-anchored to 7f4a2f9f",
         "Cut from 7f4a2f9f at https://" in p_txt),
        ("Method Belongs to the Skill present",
         "Method Belongs to the Skill\n" in p_txt),
        ("v3.45 entry present", "v3.45 (August 27, 2026):" in p_txt),
        ("v3.42 gone from resident protocol",
         "v3.42 (August 23, 2026):" not in p_txt),
        ("exactly three resident version entries",
         sum(p_txt.count("\nv3.4%d (" % n) for n in range(0, 10)) == 3),
        ("v3.42 now in history", "v3.42 (August 23, 2026):" in h_txt),
        ("history move note present",
         "when v3.45\nmade a fourth entry" in h_txt),
        ("L-256 DETAIL present", "#### [L-256]" in l_txt),
        ("L-257 DETAIL present", "#### [L-257]" in l_txt),
        ("L-256 index comment well-formed",
         "<!-- L:256 status:OPEN upd:2026-08-27 section:A" in l_txt),
        ("L-257 index comment well-formed",
         "<!-- L:257 status:OPEN upd:2026-08-27 section:A" in l_txt),
        ("ledger INDEX zone untouched",
         l_txt.count("## INDEX (generated") == 1),
        ("protocol pure ASCII", all(ord(c) < 128 for c in p_txt)),
        ("history pure ASCII", all(ord(c) < 128 for c in h_txt)),
        ("ledger pure ASCII", all(ord(c) < 128 for c in l_txt)),
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
    print("  1. Run ledger_index.py to regenerate the ledger INDEX.")
    print("     L-256 and L-257 will not appear on the status board")
    print("     until you do -- this patch wrote DETAIL blocks only.")
    print("  2. Run maintenance_run.py -- all checkers must pass.")
    print("  3. Commit and push, then confirm the remote HEAD.")
    print("  4. Reinstall provenance-discipline to your account profile")
    print("     (Settings > Skills).")
    print("")
    print("  The reinstall CANNOT be confirmed from inside the session")
    print("  that makes it. The NEXT session confirms its loaded copy")
    print("  reads 2.8 before doing provenance work.")
    print("")
    print("  NOTE, not fixed here: L-255 is cited in the v3.44 protocol")
    print("  entry and has no DETAIL block in the ledger. Same shape as")
    print("  L-225. Worth a look; deliberately not patched blind.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
