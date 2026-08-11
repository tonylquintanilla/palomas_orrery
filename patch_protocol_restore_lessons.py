"""
patch_protocol_restore_lessons.py

A FOLLOW-ON to the v3.37 trim. Run this only after that one.

WHAT IT DOES

  Puts fourteen lessons back into Part 5 of PROJECT_INSTRUCTIONS.md.

  The earlier patch moved all forty-one process and philosophical lessons
  out to documentation/LESSONS_ARCHIVE.md. On review that cut too much:
  twenty-seven of those bullets restate something already stated in a
  Part 3 gate, a Part 2 or Part 4 section, an Anti-Patterns row, a Mode 7
  table, a Quotable, or a skill that loads on task match -- but fourteen
  exist in exactly one place, and moving those to an archive file removed
  them from the system. An archive has no trigger. Nothing fires it.

  So the fourteen come back, resident, and the archive file keeps the
  twenty-seven as a record with a note saying where each still lives.

  Net effect: 824 lines to about 841. Still under 850.

FOUR CHANGES

  1. Restores the fourteen unique lessons to Part 5, in their original
     Process and Philosophical lists and their original order.
  2. Rewrites the pointer paragraph to describe what the archive file
     actually holds now -- the removed duplicates, not everything.
  3. Rewrites documentation/LESSONS_ARCHIVE.md so it says the same thing,
     naming for each entry the place it still lives.
  4. Updates the v3.37 version-history line, which currently reports only
     a line count, to say what changed and why.

Target file: PROJECT_INSTRUCTIONS.md (orrery repo root)
Also rewrites: documentation/LESSONS_ARCHIVE.md
Built on the working copy Tony uploaded August 11, 2026 (824 lines,
v3.37 header, not yet pushed; repo HEAD at that moment was
22b0db339e0ce99ca0a6a6dc11f1c9546845577f).

HOW TO RUN
  Save this file into the SAME folder as PROJECT_INSTRUCTIONS.md, open it
  in VS Code, and click Run.

  Or from a terminal in that folder:
      python patch_protocol_restore_lessons.py

WHAT SUCCESS LOOKS LIKE
  Four "ok" lines, then "patch applied" with the new line count.

WHAT FAILURE LOOKS LIKE
  A single line beginning "ERROR:" or "ANCHOR FAIL:". Nothing is written
  in either case, so it is always safe to re-check and run again.

  In particular, if you have edited PROJECT_INSTRUCTIONS.md since
  uploading it, this will stop with "base moved" rather than guess. Send
  the current file and I will rebuild.
"""

import hashlib
import os
import sys

TARGET = 'PROJECT_INSTRUCTIONS.md'
ARCHIVE = os.path.join('documentation', 'LESSONS_ARCHIVE.md')
BASE_MD5 = '2965a36639bd03bc7beff43081ace867'   # line-ending normalized

KEPT_LESSONS = 'Process:\n- Bugs become lessons when documented. Stories make science memorable\n- Pure design sessions (zero code) are first-class outputs\n- Derive from known quantities, don\'t estimate manually\n- Module Atlas as prompt artifact: complete and current reference for codebase-aware sessions\n- Fixing an invisible thing surfaces its neighbors. Budget for "now I can see it\'s too close to its neighbors" as the follow-on to any "nothing renders" fix\n- Central factories need explicit migration intent: migrate-in-scope, defer-with-tracked-backlog, or declare new-code-only. The danger zone is the unstated fourth option (factory exists, no plan) -- it gets quoted as a standard while call sites bypass it\n- Testing iterates in dependency order: regression gate, then features, then animation. Some bugs are only findable in later rounds (the Sun-checkbox-off bug needed Round 3). A three-round fix is fine when each round teaches something new\n- When deferring a pipeline patch, smoke-test the deferred pipeline to confirm it is in a KNOWN state, not just that it does not error\n- Handoff item numbers get rebased across versions (Paloma\'s shell track rebased twice: c4 1-22 -> D1 1-41 -> D2 42-54). A number means different things in different handoffs; items leak at the rebase. One authoritative running ledger beats per-handoff renumbering\n- Skills are stores too: author them in the repo, version them, SHA-stamp them, and let the ledger log their changes -- an unversioned knowledge layer is the drift class this protocol exists to kill\n\nPhilosophical:\n- The project makes Tony more informed -- that\'s the real output\n- Design gets simpler through conversation; it gets more complex through autonomous iteration\n- Procedure-to-judgment ratio scales inversely with experience and accumulated shared context. New project: more procedure. Mature partnership: more freedom. The skill is knowing which rules are load-bearing\n- "Tony\'s eyes win" extends to beauty, not just correctness: the render that confirmed the frames were right was the one that was beautiful -- and those turned out to be the same thing'

REMOVE_BULLETS = [
    "- Map multi-file changes before implementing. Parallel pipelines: fix in one doesn't propagate",
    '- Unicode in generated files breaks on Windows -- use ASCII',
    '- Agentic = confident but harder to review; targeted = visible changes',
    '- Multi-AI: Gemini for domain knowledge, Claude for implementation, Tony integrates',
    '- Iterative design beats first-draft architecture -- each round should simplify',
    '- Gallery pipeline: HTML export -> JSON converter -> gallery viewer',
    '- Flag-based contracts: _studio means "trust this, don\'t override." Strip unconditionally before guards',
    '- Renderer refactor: extract duplicated inline code into source module',
    '- /mnt/project/ is a read-only snapshot from session start. Does not update mid-session',
    '- Collegial Mode 7: Claude-to-Claude relay via Tony. No orchestration -- "here\'s the job, flag problems"',
    "- LOTO lesson: critical failures happen when procedures are not developed, not enforced, or not followed -- all three are distinct. The most critical procedure is often the one that feels unnecessary right up until it isn't",
    '- Map the dispatch before editing the leaves: grep for where a function is CALLED, not imported. Compile-clean and tests-pass do not detect that a function is never called',
    "- Structural fixes scale; data-side fixes don't. A violation in N consumers of one producer -> fix the producer. (83 sphere-shell pairs brought into compliance by 2 edits to the factory)",
    '- Handoffs are claims; runtime output is fact. When a smoke test contradicts a handoff, the smoke test wins and the handoff gets corrected',
    '- Data-content sweeps (hover text, legendgroup, marker styling) need a runtime smoke test that constructs and inspects traces on the LIVE dispatch -- a smoke test of the wrong path passes falsely',
    '- Transactional binary-mode patching for clustered edits: one script, anchored byte-level replaces, each asserting exactly one match -- all-or-nothing, fails loud on drift',
    "- Assign, don't hardcode, to stay in the house pattern: define color = 'white' once, reference it from both line and marker -- one-line restyle later",
    '- Enumerate uploaded files before claiming a review: the in-context subset is invisible to Tony and not authoritative. Read the whole set on disk first (lesson: a review and a protocol edit were both built on 9 of 19 handoffs)',
    '- Floating items get lost; capture on first mention. A bug "floating outside the deferred list" only closed when Tony asked "is this deferred?" -- promote observations into the ledger immediately, even if no work happens yet',
    '- Verify universal-propagation claims with grep. "A central factory exists" does not imply "every call site uses it" -- grep the actual call sites when propagation is load-bearing; don\'t trust the handoff narrative',
    "- Tony's session loop makes the repo trustworthy: sandbox -> test -> local repo -> provenance/atlas update -> push, all before a new session. Because the push precedes the session, repo HEAD == session-start ground truth by construction",
    "- Route around a fragile store you do not control to one you do: project knowledge proved it could be stale and haunted; the repo is Tony's, so make it the build base -- and ultimately remove the fragile store entirely (v3.30, July 2026)",
    '- Irreducibility protects both sides equally',
    "- Hassabis corroboration: AI's limitations map to why partnership outperforms autonomy",
    '- The Double-Helix IS the safety mechanism: error-correction and alignment are the same loop',
    '- The Weasley Principle: the vulnerability comes when the conversation becomes the only conversation',
    "- Broad-first requires judgment to recognize convergence. That judgment is Tony's",
]

STILL_STATED_IN = [
    'Part 2 Multi-File Changes; Part 3 Check All Parallel Pipelines [CRITICAL]',
    "Part 2 Anti-Patterns, 'Use unicode in code'; safe-file-editing Encoding Gate",
    'Part 2 Agentic vs Targeted Choice table',
    'Part 1 Mode 7 AI Roles table',
    "Part 2 Iterative Design Planning; Anti-Patterns 'Build first architecture'",
    'gallery-pipeline skill (fires on gallery work)',
    "Part 2 Anti-Patterns, 'Guard strips with if list:'; gallery-pipeline skill",
    "Part 2 Anti-Patterns, 'Duplicate rendering -> Extract to source module'",
    "Part 1 Context Priority 'Project file staleness'; Part 3 Uploads Before Project Files [CRITICAL]",
    "Part 1 Mode 7 Patterns table, 'Collegial'",
    'Part 2 Procedural Criticality, closing paragraph (LOTO, verbatim)',
    'Part 3 Verify Execution, Not Appearance [CRITICAL] -- verbatim',
    "Part 5 Quotables, 'fix the producer'; Part 2 Anti-Patterns",
    "Part 2 Anti-Patterns, 'handoff is a claim, render is fact'",
    'Part 3 Agentic Pre-Test [CRITICAL]; agentic-pre-test skill',
    "safe-file-editing skill, 'Transactional Patching for Clustered Edits'",
    'orrery-coding-conventions skill',
    'Part 3 Enumerate Uploads Before Claiming a Review [CRITICAL] -- verbatim',
    "Part 5 Quotables, 'Floating items get lost; capture on first mention'",
    "Part 5 Quotables, 'Grep, don't trust the narrative'",
    'Part 3 Session-Start Repo Pull [CRITICAL] -- states the loop verbatim',
    "Part 5 Quotables, 'Route around the store you don't control'",
    'Part 4 The Irreducibility Argument',
    'Part 4 The Hassabis Corroboration',
    'Part 4 The Double-Helix IS the Safety Mechanism',
    'Part 4 The Weasley Principle',
    'Part 4 Broad-First as Valid Methodology',
]

# ------------------------------------------------------------------
# 1. The pointer paragraph as it stands, and its replacement.
# ------------------------------------------------------------------

OLD_POINTER = """The PROCESS and PHILOSOPHICAL lessons moved to
documentation/LESSONS_ARCHIVE.md on August 11, 2026, verbatim. Read them
when a decision turns on how this project has learned to work, rather than
on a rule that must fire unprompted -- the gates that must fire are in
Part 3, not there."""

NEW_POINTER = """The PROCESS and PHILOSOPHICAL lessons below exist in only one place.
Twenty-seven others were removed on August 11, 2026, each a restatement of a
rule already stated where it fires; documentation/LESSONS_ARCHIVE.md lists
them against the place each still lives. That file is a record, not a store.

@@KEPT@@"""

# ------------------------------------------------------------------
# 2. Version-history line.
# ------------------------------------------------------------------

OLD_VH = "v3.37 (August 11, 2026): Protocol reduced from 882 to 824 lines."

NEW_VH = """v3.37 (August 11, 2026): Two changes. (1) "The Artifact Bounds the Audit"
added to Part 3 -- Tony's August 8 ruling, drafted for the first time.
(2) Protocol trimmed from 882 lines: version history v3.29-v3.33 dropped
(the ledger carries it) and twenty-seven Part 5 lessons removed as
restatements of rules already stated where they fire. A first cut moved ALL
forty-one lessons to an archive file and was reversed the same day -- an
archive has no trigger, so the fourteen with no counterpart elsewhere would
have left. A lesson duplicated by a firing rule is redundant; a lesson that
is nowhere else IS the archive."""

# ------------------------------------------------------------------
# 3. The archive file, rewritten.
# ------------------------------------------------------------------

ARCHIVE_TEXT = """LESSONS REMOVED FROM PROJECT_INSTRUCTIONS.md AT v3.37

August 11, 2026. Working copy at the time was 824 lines; repo HEAD was
22b0db339e0ce99ca0a6a6dc11f1c9546845577f at
https://github.com/tonylquintanilla/palomas_orrery.

THIS FILE IS A RECORD, NOT A STORE. Nothing in it is load-bearing. Every
bullet below was removed from the protocol's Part 5 Lessons Archive
because the same instruction is already stated somewhere that FIRES -- a
Part 3 CRITICAL gate, a Part 2 or Part 4 section, an Anti-Patterns row, a
Mode 7 table, a Quotable, or a skill that loads on task match. Each entry
names where it still lives.

The lessons that exist in only one place are NOT here. They stayed
resident in the protocol, which is the point of the cut.

Why this file was briefly something else. An earlier version of this
trim moved all forty-one lessons here and left the protocol with only a
pointer. That was wrong and was reversed the same day. A skill fires on
task match and the ledger is read at session start, but an archive file
has no trigger -- so the fourteen lessons with no counterpart elsewhere
would have quietly left the system. The v3.30 precedent, where technical
lessons went into skills, does not transfer, because skills fire.

If any line below turns out to be doing work its counterpart does not do,
put it back in the protocol. That judgment is Tony's, and this file exists
so it can be made by reading rather than from memory.

"""


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, TARGET)

    if not os.path.exists(path):
        print("ERROR: " + TARGET + " not found next to this script.")
        print("       Put this file in the orrery repo root and run again.")
        return 1
    if not os.path.isdir(os.path.join(here, 'documentation')):
        print("ERROR: no documentation/ folder here. Wrong directory?")
        return 1

    with open(path, 'rb') as f:
        data = f.read()

    fp = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
    if fp != BASE_MD5:
        print("ERROR: base moved. " + TARGET + " is not the file this patch")
        print("       was built against. Expected " + BASE_MD5 + ",")
        print("       found " + fp + ". Nothing was written.")
        print("       Send me the current file and I will rebuild.")
        return 1

    text = data.decode('utf-8')
    crlf = '\r\n' in text
    if crlf:
        text = text.replace('\r\n', '\n')

    # --- edit 1 + 2: pointer paragraph, with the lessons restored ---
    if text.count(OLD_POINTER) != 1:
        print("ANCHOR FAIL: pointer paragraph matched "
              + str(text.count(OLD_POINTER)) + " times. Nothing written.")
        return 1
    text = text.replace(OLD_POINTER, NEW_POINTER.replace('@@KEPT@@', KEPT_LESSONS))
    print("ok   fourteen unique lessons restored to Part 5")
    print("ok   pointer paragraph rewritten")

    # --- edit 3: version-history line ---
    if text.count(OLD_VH) != 1:
        print("ANCHOR FAIL: v3.37 history line matched "
              + str(text.count(OLD_VH)) + " times. Nothing written.")
        return 1
    text = text.replace(OLD_VH, NEW_VH)
    print("ok   v3.37 version-history entry rewritten")

    if sum(1 for ch in text if ord(ch) > 127):
        print("ANCHOR FAIL: non-ASCII characters present. Nothing written.")
        return 1

    if crlf:
        text = text.replace('\n', '\r\n')
    with open(path, 'wb') as f:
        f.write(text.encode('ascii'))

    # --- edit 4: rewrite the archive as a record ---
    out = [ARCHIVE_TEXT]
    for i, b in enumerate(REMOVE_BULLETS):
        out.append(str(i + 1) + ". " + b[2:])
        out.append("   STILL STATED IN: " + STILL_STATED_IN[i])
        out.append("")
    with open(os.path.join(here, ARCHIVE), 'wb') as f:
        f.write("\n".join(out).encode('ascii'))
    print("ok   " + ARCHIVE + " rewritten as a record ("
          + str(len(REMOVE_BULLETS)) + " entries)")

    count = len(text.replace('\r\n', '\n').split('\n'))
    print("")
    print("patch applied -- " + TARGET + " is now " + str(count)
          + " lines (was 824).")
    print("")
    print("The Skill Manifest zone is untouched. Bump provenance-discipline")
    print("to 1.8 and gallery-cache-builder to 1.3, then run skills_index.py")
    print("and it will rewrite that table itself.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
