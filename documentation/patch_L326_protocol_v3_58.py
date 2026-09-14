"""
patch_L326_protocol_v3_58.py

Records the provenance-discipline 2.12 bump in the protocol and the
ledger. Run this AFTER patch_L321_provenance_2_12.py and after
skills_index.py (or the maintenance run) has regenerated the manifest.

HOW TO RUN
    Save into the orrery repo ROOT (beside LEDGER_CONSOLIDATED.md),
    open in VS Code, click Run.
    Equivalent: python patch_L326_protocol_v3_58.py
    Archive it to documentation/ once it has run.

WHY
    skills_index.py owns only the zone between the SKILL-MANIFEST
    markers. The header stamp, the SHA anchor and the Version History
    are hand-authored prose, which is why the header still read v3.57
    after the manifest went to 2.12.

WHAT IT CHANGES -- three files, all-or-nothing
    PROJECT_INSTRUCTIONS.md
      1. header stamp v3.57 -> v3.58, date to September 14, 2026
      2. SHA anchor 1fa413d9 -> bfc0505e
      3. new v3.58 entry at the top of Version History
      4. the v3.55 entry REMOVED, to keep three resident
    documentation/PROJECT_INSTRUCTIONS_HISTORY.md
      5. the v3.55 entry appended to PART 1, after v3.54
    LEDGER_CONSOLIDATED.md
      6. a Module updated stamp
      7. L-326 opened DONE -- the 2.12 bump
      8. L-325's Gap amended: the rule landed; the L-305 item 6 half
         of that Gap is untouched and stays open

    The v3.55 entry is MOVED, not retyped: the script cuts the block
    out of PROJECT_INSTRUCTIONS.md and inserts those exact bytes into
    the history file, so the two halves cannot drift.

GENERATED ZONES
    Neither file's generated zone is edited or fingerprinted.
    PROJECT_INSTRUCTIONS.md is hashed OUTSIDE its SKILL-MANIFEST zone
    and LEDGER_CONSOLIDATED.md OUTSIDE its INDEX zone, so running
    skills_index.py or ledger_index.py before this patch does not
    make it refuse.

PERMANENT HALF
    The three files. The script is one-shot.

AFTER IT RUNS
    1. python ledger_index.py   (expect 321 L-blocks parsed)
    2. reinstall provenance-discipline in Settings > Skills
    3. commit and push -- SKILL.md, the manifest zone and this entry
       travel together
    A reinstall cannot be verified from inside the session that makes
    it, so the NEXT session confirms its loaded copy reads 2.12 before
    provenance work.

UNDO
    Discard Changes in GitHub Desktop.

Built on orrery bfc0505e070e70254892109e04b0cefbccbdd6bb at
https://github.com/tonylquintanilla/palomas_orrery

Written September 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

PI = "PROJECT_INSTRUCTIONS.md"
HIST = os.path.join("documentation", "PROJECT_INSTRUCTIONS_HISTORY.md")
LEDGER = "LEDGER_CONSOLIDATED.md"

FP_PI = "fc9c3b21acf0d4a934f0d78f0ab9a241"
FP_HIST = "b62f327d6a3439e7f0d6e6dae84432a2"
FP_LEDGER = "a5d23534c60bc786ecdbf6a19ce61cff"

PI_ZONE = (b"<!-- SKILL-MANIFEST:START", b"<!-- SKILL-MANIFEST:END -->")
LEDGER_ZONE = (b"<!-- INDEX:START", b"<!-- INDEX:END -->")

V355_START = b"v3.55 (September 8, 2026):"
V355_END = b"Functional for Claude, readable for human, signal preserved."

HIST_ANCHOR = b"""================================================================
PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37
================================================================"""

V358 = b"""v3.58 (September 14, 2026): No rule changed in this document. ONE
skill bump, taken as the session's FIRST action, ahead of the build it
serves.

provenance-discipline 2.11 -> 2.12 (L-326). Five rules from the L-321
cross-check round, and one that L-325 parked for this bump.

THE ROUND THAT EARNED THEM SURVIVED BECAUSE ITS LEGS FAILED
DIFFERENTLY, and that is the entry's one idea. Four checkers took the
same three worksheets on Earth's magnetosphere. One had the discipline
and marked three belt-extent rows UNSOURCED, where three open
full-text sources state those figures. One found the sources and lost
every URL in the clipboard. One could not fetch at all and said so
plainly. One found the thing nobody else did and misnamed two of the
three others. No single leg would have got there, and that was luck
rather than design.

Each rule is the shape of one of those failures. A Negative Verdict
Shows Its Search [CRITICAL], because UNSOURCED is the only verdict
pointing at no document anybody can open, so a DISCOVERY row carries
its search log. A Source Names What Was Opened, Not What It Cites
[CRITICAL], because the right URL under the wrong author name is
invisible without a second fetch. A Link Is an Object, Not Text
[QUALITY], with the file the checker exported kept as the record
rather than the paste. Two roster corrections: Gemini's fetching is
TIER-dependent, so L-276's constraint is about the interface and the
tier rather than the vendor, and a checker inside this Project is not
independent for a rerun, because past chats are searchable. And Route
the Effort Tier by Job Type [QUALITY], Tony's ruling of 2026-09-13.

A DERIVED ROW STORES THE FIGURE ITS SOURCES SUPPORT [CRITICAL] is the
sixth, and it is not from the round. It is L-325's Gap, parked on
2026-09-12 on the rule that a skill bump cannot be verified from
inside the session that makes it.

ONE ADDITION THE DRAFT DID NOT ASK FOR, recorded because a later
reader will find it and wonder. The draft's first and fifth notes both
use "DISCOVERY row" as established vocabulary. It was not: the term
was defined in the L-321 worksheet prompt and never travelled into the
skill. So Worksheet Types also gains the [CITATION] / [DISCOVERY]
definitions and the ten-column schema the three worksheets actually
ran, transcribed from the prompt rather than composed. This is v3.57's
lesson in a second store: A CONVENTION THAT IS NOT IN THE SKILL DOES
NOT TRAVEL.

THE ORDERING IS v3.55's, and this is the second entry to use it. The
bump is taken before the build it serves -- L-305 item 7, the citation
job on Earth's belt scalars -- so the stale-skill gate fires on a
matching manifest instead of on a promise carried in a handoff. The
2026-09-13 handoff made it the next session's first action for exactly
that reason, and declined to take it in the session that drafted it,
because a rushed edit to a CRITICAL skill is how a bad rule ships.
That gap earned its keep: the draft's third note was false when
written and was falsified four hours later in the same session.

The obligation still travels, because reinstalling is not something a
session can check on itself. This session loaded 2.11; the next
session confirms its loaded copy reads 2.12 before provenance work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.55 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

LEDGER_STAMP = b"""Module updated: September 14, 2026 with Anthropic's Claude Opus 5
(L-326: provenance-discipline 2.11 -> 2.12, protocol v3.58; L-325's
Gap half-closed -- the rule landed, the serving half stays open),
built on bfc0505e.
"""

L326 = b"""#### [L-326] provenance-discipline 2.11 -> 2.12, taken before the build it serves
<!-- L:326 status:DONE upd:2026-09-14 section:C flag: rice:3/3/90/2 -->
- **What landed.** Five rules from the L-321 cross-check round and one
  from L-325's Gap. A Negative Verdict Shows Its Search [CRITICAL] and
  Route the Effort Tier by Job Type [QUALITY] in Worksheet Types; A
  Source Names What Was Opened, Not What It Cites [CRITICAL] in The
  Access Standard; A Link Is an Object, Not Text [QUALITY] and the
  three things the prompt must require, in step 1 of the Review-Repair
  Protocol; two roster corrections under Model Roles; and A Derived Row
  Stores the Figure Its Sources Support [CRITICAL] under The Store
  Carries the Verified Figure.
- **One addition beyond the reviewed draft.** Notes 1 and 5 both used
  "DISCOVERY row" as established vocabulary and the skill did not
  define it -- the term lived in the L-321 prompt and never travelled.
  Worksheet Types therefore also gains the [CITATION] / [DISCOVERY]
  definitions and the ten-column schema the three worksheets ran,
  transcribed from `documentation/L321_slice1_prompts_rev3_20260912.md`
  and the worksheet tables, not composed. Same lesson as L-317: a
  convention that is not in the skill does not travel.
- **Why it was taken first.** v3.55's ordering. A bump before the build
  it serves is checked by the stale-skill gate against a matching
  manifest; a bump inside the build travels as a promise. The build it
  serves is L-305 item 7.
- **Why it was not taken on 2026-09-13.** The context was nearly spent
  and the target is a CRITICAL skill. The draft-then-review gap earned
  its keep in the same session: the draft's note 3 was false when
  written and was falsified four hours later, when twenty addresses
  came back out of a checker's own exported markdown.
- **Obligation.** The session that made this bump had loaded 2.11, and
  a reinstall is invisible to the session that makes it. The next
  session confirms its loaded copy reads 2.12 before provenance work.
- **Ref:** L-321, L-325, L-314, L-276, L-305 item 7,
  `skills/provenance-discipline/SKILL.md`,
  `documentation/DRAFT_provenance_discipline_2_12_field_notes_20260913.md`,
  `documentation/HANDOFF_L321_crosscheck_round_20260913.md`,
  `patch_L321_provenance_2_12.py`, `patch_L326_protocol_v3_58.py`.

"""

GAP_OLD = b"""**Gap:** the rule belongs in `provenance-discipline` at its next bump --
a derived row stores the figure its sources support, and a check recomputes
it. Not taken this session: a skill bump cannot be verified from inside the
session that makes it. Also open: L-305 item 6 still serves 10.0 and 12.5,
so the gallery's live Store drift check reports 2 DRIFT until it lands."""

GAP_NEW = b"""**Gap (half closed 2026-09-14).** The rule LANDED: A Derived Row Stores
the Figure Its Sources Support [CRITICAL] is in `provenance-discipline`
2.12, under The Store Carries the Verified Figure, carrying the scope
paragraph about L-314 unchanged. See L-326. Still open: L-305 item 6
still serves 10.0 and 12.5, so the gallery's live Store drift check
reports 2 DRIFT until it lands."""


def fail(msg):
    print("ERROR: " + msg)
    sys.exit(1)


def read_lf(path):
    if not os.path.exists(path):
        fail("%s not found. Run this from the orrery repo ROOT." % path)
    with open(path, "rb") as f:
        raw = f.read()
    return raw, raw.replace(b"\r\n", b"\n")


def outside_zone(lf, zone, path):
    a = lf.find(zone[0])
    b = lf.find(zone[1])
    if a < 0 or b < 0:
        fail("%s: generated zone markers not found." % path)
    return lf[:a] + lf[b + len(zone[1]):]


def check(path, got, want):
    if want.startswith("PLACEHOLDER"):
        return
    if got != want:
        fail("%s does not match the tree this patch was built against.\n"
             "       expected md5 %s\n"
             "       found    md5 %s\n"
             "       Pull at bfc0505e, or the patch has already run."
             % (path, want, got))


def one(buf, old, new, label):
    n = buf.count(old)
    if n != 1:
        fail("ANCHOR FAIL %s: found %d matches, expected 1.\n       %r"
             % (label, n, old[:70]))
    return buf.replace(old, new, 1)


def main():
    pi_raw, pi = read_lf(PI)
    hi_raw, hi = read_lf(HIST)
    le_raw, le = read_lf(LEDGER)

    check(PI, hashlib.md5(outside_zone(pi, PI_ZONE, PI)).hexdigest(), FP_PI)
    check(HIST, hashlib.md5(hi).hexdigest(), FP_HIST)
    check(LEDGER,
          hashlib.md5(outside_zone(le, LEDGER_ZONE, LEDGER)).hexdigest(),
          FP_LEDGER)

    # --- cut the v3.55 block out of the protocol -----------------------
    a = pi.find(V355_START)
    b = pi.find(V355_END)
    if a < 0 or b < 0 or b <= a:
        fail("could not locate the v3.55 block in %s." % PI)
    v355 = pi[a:b].rstrip() + b"\n"
    pi = pi[:a] + pi[b:]

    # --- protocol edits ------------------------------------------------
    pi = one(pi,
             b"Tony Quintanilla, PE | Claude | v3.57 | September 11, 2026",
             b"Tony Quintanilla, PE | Claude | v3.58 | September 14, 2026",
             "header stamp")
    pi = one(pi,
             b"Cut from 1fa413d9 at https://github.com/tonylquintanilla/palomas_orrery",
             b"Cut from bfc0505e at https://github.com/tonylquintanilla/palomas_orrery",
             "SHA anchor")
    pi = one(pi, b"v3.57 (September 11, 2026):", V358 + b"v3.57 (September 11, 2026):",
             "v3.58 entry")

    # --- history: v3.55 appended to PART 1 -----------------------------
    hi = one(hi, HIST_ANCHOR, v355 + b"\n" + HIST_ANCHOR, "v3.55 into PART 1")

    # --- ledger --------------------------------------------------------
    prev_stamp = (b"Module updated: September 12, 2026 with Anthropic's Claude Opus 5\n"
                  b"(L-305 item 6a recorded after the live gallery run verified it at\n"
                  b"0f51ce4f: two drifted values corrected, three claims retired, and\n"
                  b"Gap (2)'s closing plan marked superseded by L-323), built on\n"
                  b"77eb1439.\n")
    le = one(le, prev_stamp, prev_stamp + LEDGER_STAMP, "ledger stamp")
    le = one(le, b"#### [L-315] Chained ledger patches refuse",
             L326 + b"#### [L-315] Chained ledger patches refuse",
             "L-326 block")
    le = one(le, GAP_OLD, GAP_NEW, "L-325 Gap")

    # --- encoding gate on all three ------------------------------------
    for name, buf in ((PI, pi), (HIST, hi), (LEDGER, le)):
        if b"\r" in buf:
            fail("%s: result carries CR bytes." % name)
        bad = sorted(set(c for c in buf if c > 127))
        if bad:
            fail("%s: result carries non-ASCII bytes %r" % (name, bad[:8]))

    # --- write, keeping each file's own line endings --------------------
    for name, raw, buf in ((PI, pi_raw, pi), (HIST, hi_raw, hi),
                           (LEDGER, le_raw, le)):
        out = buf.replace(b"\n", b"\r\n") if b"\r\n" in raw else buf
        with open(name, "wb") as f:
            f.write(out)

    print("ok  %s -- v3.58, anchor bfc0505e, v3.55 removed" % PI)
    print("ok  %s -- v3.55 appended to PART 1" % HIST)
    print("ok  %s -- stamp, L-326, L-325 Gap half closed" % LEDGER)
    print("patch applied")
    print("")
    print("Next: python ledger_index.py  (expect 321 L-blocks parsed),")
    print("      reinstall provenance-discipline in Settings > Skills,")
    print("      then commit and push all of it together.")


if __name__ == "__main__":
    main()
