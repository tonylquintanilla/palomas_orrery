"""
patch_protocol_v337.py

Takes PROJECT_INSTRUCTIONS.md from 882 lines to about 838, and adds the
one section that was ruled in August but never drafted.

FOUR CHANGES

  1. Adds "The Artifact Bounds the Audit" to Part 3, immediately after
     Show the Envelope of the Unknowable. Tony's ruling of August 8.

  2. Removes 27 bullets from the Part 5 Lessons Archive. Every one of
     them restates an instruction that is already stated somewhere that
     FIRES -- a Part 3 CRITICAL gate, a Part 2 or Part 4 section, an
     Anti-Patterns row, a Mode 7 table, a Quotable, or a skill that loads
     on task match. The lessons that exist in only one place are NOT
     touched and stay resident.

     Each removed line, with the place it still lives, is listed in
     documentation/LESSONS_REMOVED_v337.md, which this script writes
     BEFORE it edits anything. Read that file if you want to check the
     call; put back any line that turns out to be doing work its
     counterpart does not do.

  3. Trims version-history entries v3.29 through v3.33. These are safe to
     drop because the ledger appendix genuinely carries the version
     history -- that is what that appendix is. v3.34 onward stay resident.

  4. Replaces the non-ASCII em dashes with " -- ", applying the protocol's
     own encoding rule to itself.

WHAT THIS DELIBERATELY DOES NOT DO

  The claim that the complete lessons archive is preserved verbatim in the
  ledger is left ALONE. It is false -- that appendix is a per-version
  change log and has never carried those lists -- but deciding where
  institutional memory should live is its own conversation, and it should
  not ride along inside a trim.

Target file: PROJECT_INSTRUCTIONS.md (orrery repo root)
Also writes: documentation/LESSONS_REMOVED_v337.md
Built on 22b0db339e0ce99ca0a6a6dc11f1c9546845577f

HOW TO RUN
  Save this file into the SAME folder as PROJECT_INSTRUCTIONS.md, open it
  in VS Code, and click Run.

  Or from a terminal in that folder:  python patch_protocol_v337.py

WHAT SUCCESS LOOKS LIKE
  A "wrote documentation/..." line, then one "ok" line per change, then
  "patch applied" with the new line count.

WHAT FAILURE LOOKS LIKE
  A single line beginning "ERROR:" or "ANCHOR FAIL:". Nothing is written
  to PROJECT_INSTRUCTIONS.md in either case, so it is always safe to
  re-check and run again.

AFTERWARD
  The Skill Manifest zone is untouched on purpose -- skills_index.py
  generates it. Two skills are due a bump (provenance-discipline to 1.8,
  gallery-cache-builder to 1.3); edit those, then run that tool and it
  will rewrite the table itself.
"""

import hashlib
import os
import sys

TARGET = 'PROJECT_INSTRUCTIONS.md'
RECORD = os.path.join('documentation', 'LESSONS_REMOVED_v337.md')
BASE_MD5 = '7817887f7c0677b0b71ade5e8783b671'   # line-ending normalized
SHA = '22b0db339e0ce99ca0a6a6dc11f1c9546845577f'

# ------------------------------------------------------------------
# The bullets to remove, and where each one still lives.
# ------------------------------------------------------------------

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
    "Part 2 Multi-File Changes; Part 3 Check All Parallel Pipelines [CRITICAL]",
    "Part 2 Anti-Patterns, 'Use unicode in code'; safe-file-editing Encoding Gate",
    "Part 2 Agentic vs Targeted Choice table",
    "Part 1 Mode 7 AI Roles table",
    "Part 2 Iterative Design Planning; Anti-Patterns 'Build first architecture'",
    "gallery-pipeline skill (fires on gallery work)",
    "Part 2 Anti-Patterns, 'Guard strips with if list:'; gallery-pipeline skill",
    "Part 2 Anti-Patterns, 'Duplicate rendering -> Extract to source module'",
    "Part 1 Context Priority 'Project file staleness'; Part 3 Uploads Before Project Files [CRITICAL]",
    "Part 1 Mode 7 Patterns table, 'Collegial'",
    "Part 2 Procedural Criticality, closing paragraph (LOTO, verbatim)",
    "Part 3 Verify Execution, Not Appearance [CRITICAL] -- verbatim",
    "Part 5 Quotables, 'fix the producer'; Part 2 Anti-Patterns",
    "Part 2 Anti-Patterns, 'handoff is a claim, render is fact'",
    "Part 3 Agentic Pre-Test [CRITICAL]; agentic-pre-test skill",
    "safe-file-editing skill, 'Transactional Patching for Clustered Edits'",
    "orrery-coding-conventions skill",
    "Part 3 Enumerate Uploads Before Claiming a Review [CRITICAL] -- verbatim",
    "Part 5 Quotables, 'Floating items get lost; capture on first mention'",
    "Part 5 Quotables, 'Grep, don't trust the narrative'",
    "Part 3 Session-Start Repo Pull [CRITICAL] -- states the loop verbatim",
    "Part 5 Quotables, 'Route around the store you don't control'",
    "Part 4 The Irreducibility Argument",
    "Part 4 The Hassabis Corroboration",
    "Part 4 The Double-Helix IS the Safety Mechanism",
    "Part 4 The Weasley Principle",
    "Part 4 Broad-First as Valid Methodology",
]

RECORD_HEADER = """LESSONS REMOVED FROM PROJECT_INSTRUCTIONS.md AT v3.37 -- REVIEW COPY

Built on {SHA}
at https://github.com/tonylquintanilla/palomas_orrery.

This file is a RECORD, not a store. Every bullet below was removed from
the protocol's Lessons Archive because the same instruction is already
stated somewhere that FIRES -- a Part 3 CRITICAL gate, a Part 2 or Part 4
section, an Anti-Patterns row, a Mode 7 table, a Quotable, or a skill that
loads on task match. Nothing here left the system; each entry names where
it still lives.

The lessons that exist in only one place were NOT touched. They are still
resident in the protocol, which is the point of the cut: what remains in
Part 5 is the material that is genuinely nowhere else.

If any line below turns out to be doing work its counterpart does not do,
put it back. That judgment is Tony's, and this file exists so it can be
made by reading rather than from memory.

"""

# ------------------------------------------------------------------
# The new Part 3 section.
# ------------------------------------------------------------------

ANCHOR_ENVELOPE_TAIL = """The cone is to an unknowable azimuth what "remove and note the gap" is to an
uncited number. (Tony: use it or the range where we have it; show the mechanic
and say so where we don't -- and no element NEEDS to exist; it earns its place
by what it teaches, not by completeness.)
"""

NEW_SECTION = """The cone is to an unknowable azimuth what "remove and note the gap" is to an
uncited number. (Tony: use it or the range where we have it; show the mechanic
and say so where we don't -- and no element NEEDS to exist; it earns its place
by what it teaches, not by completeness.)

The Artifact Bounds the Audit
Companion to Show the Envelope, one scope up: that rule governs how a single
value is STATED, this one governs which values are IN SCOPE at all. The
feature registry describes what the orrery RENDERS. It is not a model of the
solar system, and it is not trying to become one.
So a field is missing only when the orrery renders something that has no
recorded provenance. A published measurement the orrery does not draw is not
a gap -- it is outside the bound. An audit that counts those as missing can
never close, and an audit that can never close stops being read.
The bound is CLOSED at any moment and OPEN over time. Closed, because at any
given commit the set of rendered values is finite and countable -- that is
what makes the audit finishable. Open, because what the orrery renders is
itself an output of these conversations: osculating orbits entered as a Claude
suggestion, not as a gap being filled. Both halves are load-bearing. Without
the closed half the audit never converges; without the open half the rule
would quietly forbid the suggestion that added them.
The tell that this rule is being violated is an audit whose denominator grows
whenever someone thinks of something. (Tony's ruling, August 8 2026; the open
half is his nuance, and it is the half a completeness instinct will drop.)
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
        return 1

    text = data.decode('utf-8')
    crlf = '\r\n' in text
    if crlf:
        text = text.replace('\r\n', '\n')

    if len(REMOVE_BULLETS) != len(STILL_STATED_IN):
        print("ERROR: internal list mismatch. Nothing was written.")
        return 1

    # Every bullet must be present exactly once BEFORE anything is written.
    for b in REMOVE_BULLETS:
        n = text.count(b)
        if n != 1:
            print("ANCHOR FAIL: expected 1 match, found " + str(n) + " for:")
            print("             " + b[:70])
            print("             Nothing was written.")
            return 1

    # --- write the record first, so nothing is cut before it is captured ---
    out = [RECORD_HEADER.replace('{SHA}', SHA)]
    for i, b in enumerate(REMOVE_BULLETS):
        out.append(str(i + 1) + ". " + b[2:])
        out.append("   STILL STATED IN: " + STILL_STATED_IN[i])
        out.append("")
    with open(os.path.join(here, RECORD), 'wb') as f:
        f.write("\n".join(out).encode('ascii'))
    print("wrote " + RECORD + " (" + str(len(REMOVE_BULLETS)) + " entries)")

    # --- edit 1: new Part 3 section ---
    if text.count(ANCHOR_ENVELOPE_TAIL) != 1:
        print("ANCHOR FAIL: Show the Envelope tail matched "
              + str(text.count(ANCHOR_ENVELOPE_TAIL)) + " times.")
        return 1
    text = text.replace(ANCHOR_ENVELOPE_TAIL, NEW_SECTION)
    print("ok   Artifact Bounds the Audit added to Part 3")

    # --- edit 2: remove the duplicated bullets ---
    for b in REMOVE_BULLETS:
        text = text.replace(b + "\n", "", 1)
    print("ok   " + str(len(REMOVE_BULLETS))
          + " duplicated lessons removed, the rest left resident")

    # --- edit 3: trim version history v3.29 .. v3.33 ---
    a = text.find('v3.29 (June 22, 2026):')
    b2 = text.find('v3.34 (August 5, 2026):')
    if a == -1 or b2 == -1 or b2 <= a:
        print("ANCHOR FAIL: could not bracket version history v3.29..v3.34.")
        return 1
    text = text[:a] + text[b2:]
    print("ok   version history trimmed to v3.34 and later")

    # --- edit 4: non-ASCII to ASCII ---
    n_bad = sum(1 for ch in text if ord(ch) > 127)
    for bad, good in (('\u2014', ' -- '), ('\u2013', '-'),
                      ('\u201c', '"'), ('\u201d', '"'),
                      ('\u2018', "'"), ('\u2019', "'")):
        text = text.replace(bad, good)
    still = sum(1 for ch in text if ord(ch) > 127)
    if still:
        print("ANCHOR FAIL: " + str(still) + " non-ASCII characters remain.")
        return 1
    print("ok   " + str(n_bad) + " non-ASCII characters replaced")

    if crlf:
        text = text.replace('\n', '\r\n')
    with open(path, 'wb') as f:
        f.write(text.encode('ascii'))

    count = len(text.replace('\r\n', '\n').split('\n'))
    print("")
    print("patch applied -- " + TARGET + " is now " + str(count)
          + " lines (was 882).")
    print("")
    print("Read documentation/LESSONS_REMOVED_v337.md to check the cut.")
    print("The header still says v3.36; bump it when you are ready.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
