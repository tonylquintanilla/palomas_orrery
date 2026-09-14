"""
patch_L327_L328_session_20260914.py

Captures the rulings of 2026-09-14 that exist nowhere but a chat window,
and amends the Register Rule on Tony's instruction.

WHAT IT DOES (three files)

  PROJECT_INSTRUCTIONS.md
  0a. The Register Rule is rewritten. Its old wording treated plain
      speech as a style Claude adopts and gave compressed prose a home
      in this document and the skills, which reads as a shared shorthand
      that simply belongs elsewhere. Tony's ruling of 2026-09-14: it is
      not shared. Claude can decompress it because it holds the session
      at once; Tony cannot, and by the time a sentence is dense enough
      to notice, reading it has already cost what it was meant to save.
  0b. Version history gains v3.59; the header stamp and the SHA anchor
      move with it; the v3.56 block is CUT and moved down.

  documentation/PROJECT_INSTRUCTIONS_HISTORY.md
  0c. The v3.56 block is inserted into PART 1. It is MOVED, not retyped:
      the same bytes cut above are pasted here, so the two copies cannot
      drift.

  LEDGER_CONSOLIDATED.md
  1. L-327 NEW -- the three tool changes from the rules-vs-reasoning round,
     and the test that replaced the one Claude proposed.
  2. L-328 NEW -- the subtraction pass on provenance-discipline. 20 of its
     section headings are [CRITICAL] against 8 [QUALITY]; the ledger and
     conventions skills carry zero [CRITICAL] headings between them.
  3. L-322 gains two notes of 2026-09-14: the sequencing ruling (build
     the mechanism whole, walk the store in slices, gate per slice), and
     the unit-token finding (`l_shell` is right, `dimensionless` is the
     defect, and a token's meaning has no home in the store today).
  4. L-323 gains the note that design revision 3 is filed, and the one
     place it is already stale.
  5. L-305 gains what item 7 has landed, the unconsumed-constant finding,
     and a correction about the dipole tilt.
  6. L-329 NEW -- the Register Rule amendment and why it was needed.

WHY THIS RUNS NOW RATHER THAN AT THE CLOSE
  Floating items get lost. Five rulings from this session lived only in
  the conversation, and one of them (significant figures per row) had
  already made a filed design record stale.

HOW TO RUN IT (Tony)
  Save into the orrery repo root, next to LEDGER_CONSOLIDATED.md, open in
  VS Code, click Run.

  Success: nine "ok" lines, then "patch applied".
  Failure: one ERROR or ANCHOR FAIL line. NOTHING is written. Undo is
           Discard Changes in GitHub Desktop.

AFTER IT RUNS
  Run ledger_index.py (Run button). Expect 324 L-blocks parsed, up from
  321, and no consistency problems.

BASE
  Built on orrery 773e5c2d084f8e269abc5700d33928e530902b29 at
  https://github.com/tonylquintanilla/palomas_orrery
  The guard fingerprints content OUTSIDE the INDEX zone, which
  ledger_index.py regenerates.

Written September 14, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = "LEDGER_CONSOLIDATED.md"
PROTOCOL = "PROJECT_INSTRUCTIONS.md"
HISTORY = os.path.join("documentation", "PROJECT_INSTRUCTIONS_HISTORY.md")
BASE_FP = "0f173283d82979dece2de99b37c44a99"
PROTOCOL_FP = "753f99f5dfd031c6fa0b3a9699e7aa64"
HISTORY_FP = "696a5d92b8d0958059227407d316975a"

INDEX_START = b"<!-- INDEX:START"
INDEX_END = b"<!-- INDEX:END -->"

# ---------------------------------------------------------------------------
# Edit 1 (lowest in the file): two new blocks, inserted after L-326 and
# before the section-C blocks that follow it.
# ---------------------------------------------------------------------------

NEW_BLOCKS_ANCHOR = b"#### [L-315] Chained ledger patches refuse"

NEW_BLOCKS = b'''#### [L-327] Tool repairs from the rules-vs-reasoning round (tooling track)
<!-- L:327 status:OPEN upd:2026-09-14 section:A flag: rice:3/4/80/2 -->
- **Where this came from.** Three problems in the 2026-09-14 session were
  caught by Tony or by a reviewer rather than by the session that made
  them. Claude proposed writing new rules into the skills. Tony's
  objection: "are more rules the answer? We already have complex rules.
  Shouldn't model reasoning cover this?" A review request went to Fable
  (`documentation/REVIEW_REQUEST_rules_vs_reasoning_20260914.md`,
  anchored at `773e5c2d`), which read the four named files cold and
  answered.
- **The three misses, named.** (1) A kilometre helper rounded every figure
  to two significant figures, ignoring the per-row REPORT instruction the
  store already carries. (2) The session built L-305 item 7 and never read
  item 5, four items above it, which retires the drawn shape parameters
  and drops the dipole tilt. (3) A hover sentence asserted that a second
  published fit puts the magnetopause farther out, naming neither the fit
  nor a source.
- **The finding that settled it, verified in the file.**
  `provenance-discipline` 2.12, Composed vs Transcribed On-Layer Text,
  already ends "A composed sentence that cannot be sourced does not
  ship." That covers miss (3) exactly. So all three were LOADED RULES
  MISSED, not gaps -- one kind, not three, and Claude had sorted them
  three ways. A second copy of a rule that was loaded and missed will be
  loaded and missed.
- **The test, replaced.** Claude proposed "would a careful reader with
  full attention still get this wrong?" Fable rejected it as
  unfalsifiable after the fact, and Tony agreed. The replacement, adopted:
  CAN A CHECK BE BUILT THAT FAILS ON THIS, AND TERMINATES? If yes, build
  the check and write no rule. If no, and the fact cannot be derived from
  anything loaded, write one line where it fires. If the rule already
  exists, write nothing and ask why a loaded rule did not fire.
- **Tony's ruling, 2026-09-14: zero new rules, three tool changes.**
  (a) `ledger_index.py` prints an item's sub-items with their statuses on
  lookup, so reading to the edge of one part and stopping is not possible.
  (b) A constants-without-consumers report: every top-level row in
  `constants_new.py` that no module imports, NAMED. It REPORTS and does
  NOT gate -- Claude's amendment, adopted -- because a row written ahead
  of its renderer is correct sequencing, not a defect. (c)
  `provenance_scanner.py` announces its own prose blind spot: it reads
  number-plus-unit tokens, so a factual sentence carrying no numeral is
  invisible to it and to every other check the project has. Make the blind
  spot announce.
- **What (b) would name today**, and it is the finding that earned it:
  `EARTH_BOW_SHOCK_JELINEK_LAMBDA` (line 606) and
  `EARTH_BOW_SHOCK_CUT_ANGLE_DEG` (line 618) have no consumer in either
  repo. They are correct -- L-305 item 4 wrote them for item 5, which has
  not run -- and nobody had noticed either way. [verified @773e5c2d]
- **Note (Claude):** RICE proposed 3/4/80/2. Reach is every session that
  reads the ledger or the store; Impact 4 because each of the three
  changes converts a miss that needs a reader into one a run reports;
  Confidence 80 because all three are additive reports over structures
  that already exist; Effort 2, three small changes in tools already in
  the routine.
**Gap:** build (a), (b) and (c). Each is independent of the others and of
L-305. (c) is the smallest and closes the most recent miss.
**Ref:** L-305 item 5, L-322(d), L-328,
`documentation/REVIEW_REQUEST_rules_vs_reasoning_20260914.md`,
`skills/provenance-discipline/SKILL.md` (Composed vs Transcribed),
`ledger_index.py`, `provenance_scanner.py`.

#### [L-329] The Register Rule rewritten: compression is a one-way channel (protocol track)
<!-- L:329 status:DONE upd:2026-09-14 section:C flag: rice:4/4/90/1 -->
- **Tony's instruction, 2026-09-14.** "On the register, the rule is
  simple, 'don't use compressed language' can we clarify the register
  rule? The reason is that I cannot follow compressed language. Only you
  can."
- **What the old wording got wrong.** It opened with "plain speech is
  the default" and then gave the compressed voice a home in the protocol
  and the skills. Those two sentences together describe a shared
  shorthand that belongs in a different place. It is not shared. One
  party can read it.
- **Why the rule kept decaying.** Compression costs Claude nothing to
  write and nothing to read back, because it holds the session at once.
  It costs Tony the reading, and noticing that a sentence is too dense
  is itself the cost. So there is no signal on the writing side that
  anything went wrong -- which is the same shape as a check that cannot
  fail.
- **Where it failed that evening: summaries.** Four closing round-ups in
  one session, each naming decisions rather than stating them. A list of
  names is compressed prose with bullet points on it. The rewrite names
  summaries, status lines and recaps as the hiding place, because they
  look like service.
- **What did NOT change:** the three checks, ANSWER FIRST / EVIDENCE ON
  REQUEST, CAPTURE GOES IN A FILE, and the backstop paragraph. Only the
  opening was rewritten, because that is the part that has to carry the
  rule when a session is moving.
- **Note (Claude):** RICE proposed 4/4/90/1. Reach is every message;
  Confidence 90 because the instruction was explicit and the failure was
  demonstrated in the same session rather than recalled.
**Ref:** L-261 (the August 2026 amendment this supersedes the opening
of), `PROJECT_INSTRUCTIONS.md` Register Rule, v3.59.

#### [L-328] Subtraction pass on the skill layer (protocol/skills track)
<!-- L:328 status:OPEN upd:2026-09-14 section:A flag: rice:3/3/70/3 -->
- **The measurement.** `provenance-discipline` 2.12 carries 20 section
  headings tagged [CRITICAL] against 8 tagged [QUALITY]. Four of the
  twenty landed in one bump. `ledger-and-session-records` 1.11 and
  `orrery-coding-conventions` 1.8 carry ZERO [CRITICAL] headings between
  them. [verified @773e5c2d]
- **Why it matters.** The protocol's own Procedural Criticality says the
  critical tier must stay short, and that if everything is critical
  nothing is. That was written about this document and now applies to the
  skill layer. The Braid applies too: provenance-discipline has grown by
  INSTANCE rather than by kind, which is the shape that rule exists to
  stop.
- **The job.** A pass that demotes, merges, or moves to Field Notes, with
  one row per class rather than one per section. A demotion is a
  **Tony-action (decide)** in every case -- a [CRITICAL] tag records that
  a failure proved a check load-bearing, and only Tony can rule that the
  proof no longer holds.
- **What this is NOT.** Not a rewrite, and not a rule cull by length. The
  question per section is whether its tier is still earned, not whether
  the skill is long.
- **Note (Claude):** RICE proposed 3/3/70/3. Confidence 70 because the
  measurement is mechanical but every judgment in the pass is Tony's.
**Gap:** the whole item. Sequence it after L-327, whose (c) may itself add
a line to the skill being pruned.
**Ref:** L-327, `PROJECT_INSTRUCTIONS.md` Procedural Criticality and The
Braid, `skills/provenance-discipline/SKILL.md`.

'''

# ---------------------------------------------------------------------------
# Edit 2: L-323 gains the revision-3 note.
# ---------------------------------------------------------------------------

L323_ANCHOR = b"**Gap:** send revision 3 to the checkers"

L323_NEW = b'''**Note (2026-09-14) -- revision 3 is written and filed, and one part of
it is already superseded.**
`documentation/DESIGN_a_figure_in_prose_needs_a_home_rev3_20260914.md`
carries ruling B amended a second time (the store holds geocentric
equatorial Earth radii, each belt row naming the paper its figure
follows), the four extents sourced rather than removed, row 9's reversal,
the magnetotail at 220, and the inner span moving from Koskinen and
Kilpua to Meredith on SCOPE -- Koskinen and Kilpua state 1.1 to 2 R_E for
the inner ELECTRON belt and put the protons over 1.1 to 3 R_E, so they
cannot carry a hover calling that belt mainly protons.
TWO THINGS IN IT ARE WRONG OR MISSING, recorded here rather than left for
a reader to trip over. Its altitude section rounds every derived kilometre
figure to two significant figures; Tony ruled on 2026-09-14 that the
figure count comes from each row's own source instead, which is what
shipped. And it does not mention L-305 item 5, which retires the drawn
shape parameters it discusses as settled. A revision 4 is not owed for
either -- this note is the correction, and item 7's as-built record
carries what was actually done.
'''

# ---------------------------------------------------------------------------
# Edit 3: L-322 gains the sequencing ruling.
# ---------------------------------------------------------------------------

L322_ANCHOR = b"**Gap:** the whole item, in ruling 3's order."

L322_NEW = b'''**Note (2026-09-14) -- Tony's sequencing ruling: the mechanism whole, the
store in slices.** Raised because tonight's misses all traced to values
held as prose rather than as data, and Tony asked why the whole item does
not simply run next.
THE MECHANISM IS COMPLETE WITHOUT THE UNITS and is built as one piece: the
export generator, the bytes-hash check, the join check that every pointer
resolves to a row by name, and the dimensional check. Only the last reads
units, and it runs on the rows that have them.
THE MIGRATION IS THE SWEEP and is walked by BODY, Earth first. Each row is
visited ONCE, writing `# Unit:`, `# Status:` and the figure count (d)
settles at that single visit -- so slicing decides WHEN a row is visited,
never how many times. What would create a second walk is taking (d)
separately from the unit field, which this avoids. Tony's own note on
adopting it: slices are consistent with the Braid.
THE GATE TURNS ON PER SLICE, which ruling 3's order does not yet provide
for. The runner holds a short list of CLOSED slices: a missing unit FAILS
for a row inside one, and a row outside one is NAMED as not yet migrated.
That answers the danger ruling 3 was protecting against -- dropping the
suffix reader before the units exist puts 46 of 48 checks dark while the
run stays green -- without waiting for a complete walk, because the check
knows what it is entitled to judge and says out loud what it is not.
Ruling 3's ORDER survives inside a slice; what changes is the denominator
it applies to.
THE NUMBERS, measured rather than recalled [verified @773e5c2d]:
`constants_new.py` holds 106 top-level assignments, 53 of them Earth's.
24 rows carry a `# Unit:` line and ALL 24 ARE EARTH ROWS, written as a
side effect of L-305's magnetosphere work. The store is already being
migrated in slices, Earth first, about 45 percent of the way through the
Earth slice. This ruling names what was happening rather than introducing
it.
COST, accepted: a non-Earth row can carry a wrong unit longer than it
would under one global walk. No non-Earth row carries a unit at all today,
so the exposure is smaller than it sounds.
**Note (2026-09-14) -- `l_shell` is the right token and `dimensionless`
is the defect.** Raised by Tony, against Claude, who proposed retiring
`l_shell` in favour of `dimensionless` and was wrong. His objection: a
dimensionless quantity is still a named quantity and has to be tied to
its name the way any other unit is.
THE STORE ALREADY SETTLED THIS ONCE, with `deg`. An angle is a ratio of
arc length to radius, so degrees are dimensionless in the strict sense,
and the store carries `# Unit: deg` rather than `# Unit: dimensionless`
because 105 degrees is not interchangeable with 105 of anything else.
`l_shell` follows that precedent exactly.
WHY THE WRONG ANSWER WAS TEMPTING, recorded because the reasoning is
the useful part. The unit field is asked two questions at once. Which
other numbers may this be compared with, and what algebra is legal on
it. For a dimensioned quantity one token answers both: `km` names the
kind AND carries the dimension. For a dimensionless one they separate.
`l_shell` answers the comparison question and leaves the dimensional
one open; `dimensionless` answers the dimensional one and throws the
comparison away, which is the greater loss, because comparison is what
catches a real error.
THE DEFECT IS THE FIVE ROWS THAT DECLARE `dimensionless`, among them
`EARTH_BOW_SHOCK_JELINEK_EPS` (a flaring exponent) and
`EARTH_BOW_SHOCK_JELINEK_LAMBDA` (a shape parameter). Two different
quantities wearing one label, and nothing in the check would object if
one were compared against the other. [verified @773e5c2d]
WHERE A TOKEN'S MEANING LIVES TODAY, and it is not the store. Two
pieces, both in `gallery_maintenance_run.py`: `store_conversions()`
builds factors for au, km, r_sun and r_earth out of the store, and
membership in that dict is the only thing that makes `r_earth` a
length; and a hardcoded `SCALAR_UNITS` frozenset (per_nt, nt, npa, deg,
km_s, dimensionless) meaning "refuse to convert". That encodes ONE
distinction -- length or not-length -- so a pressure and an angle sit
in the same bucket and compare by string equality. Both pieces are in
the gallery repo, which inverts ruling 6. [verified @eab070a9]
MEASURED, since the token changes the verdict: served as `l_shell` the
outer peak reports NO UNIT; served as `dimensionless` it reports UNIT
MISMATCH against the name's `_RADII`. The softer verdict is the one we
ship, and it is soft because the checker does not recognise the token
rather than because the row is right. [verified @773e5c2d]
WHAT THIS ITEM SHOULD BUILD, as a result: one entry per token, in the
orrery, carried out by the export -- each token declaring its dimension
and, where it has one, its factor. The comparison check then reads the
row's token and the dimensional check reads the token's dimension,
instead of both being inferred from whether a string appears in a
conversion dict. It REPLACES `SCALAR_UNITS` rather than adding to it,
and `dimensionless` retires as a token because it names no quantity.
BEARS ON (e): astropy has no `l_shell`, so a Quantity-based approach
would have to call it dimensionless and lose the same thing a token
table keeps.
**Tony-action (decide) 2026-09-14: (d) is prioritised** within the item.
It is unruled, so the first session on this item is a design round
settling (a) through (e), not a patch.
'''

# ---------------------------------------------------------------------------
# Edit 4 (highest in the file): L-305 gains item 7's as-built and two
# corrections.
# ---------------------------------------------------------------------------

L305_ANCHOR = b"(7) Hover text in `earth_visualization_shells.py`"

L305_NEW = b'''**Note (2026-09-14) -- item 7 in three parts, and what has landed.**
PART 1, the store, landed at `773e5c2d` via
`patch_L305_item7_belt_rows.py`: four belt edge rows in geocentric
equatorial Earth radii, `EARTH_MAGNETOTAIL_OBSERVED_RADII` at 220 on
Slavin et al. (1983), and the two peak rows corrected -- the outer moves
to `# Unit: l_shell` with `# Status: declared` because 4.5 is a midpoint
of an L band, and Baker comes OFF its citation, his figure 30 using
L* = 4.5 as a selected analysis location rather than a universal peak.
`test_status_lines.py` went 19 status lines to 26, none malformed; the
provenance scanner reported Tier-1 unchanged. [verified @773e5c2d]
PART 2, the strings, is `patch_L305_item7_strings.py`, pre-tested and
delivered. The four typed extents and both typed altitude pairs become
arithmetic on the rows through one helper whose `sig` argument is
REQUIRED, so a call site that forgets raises rather than inheriting a
choice. Two claims the L-321 round did not support are gone: "making
complex life possible" (three legs returned NO against Griessmeier et al.
2016) and "protects Earth from solar radiation", which reads as sunlight
rather than particles.
PART 3, the gallery's belt `note` fields in `data/objects_config.json`,
is the half item 6 was fenced off so they are edited once.
**Note (2026-09-14) -- two corrections to what item 5 owns.** Read while
building item 7 and recorded because a session that reads only item 7 will
get both wrong. The drawn shape parameters -- the half-ellipsoid axes, the
conic eccentricity, the tail's length and radii, the 0.92 flank cap -- are
NOT a settled convention to protect; item 5 retires them when it ports
Shue and Jelinek into the renderer. And item 5 says DROP
`magnetic_tilt_deg=11`; it is not a candidate for a store row, because
both fits are symmetric about the aberrated Sun-Earth line and the dipole
tilt is not part of that geometry.
'''


# ---------------------------------------------------------------------------
# Protocol: the Register Rule, rewritten.
# ---------------------------------------------------------------------------

REGISTER_OLD = b"""Register Rule
PLAIN SPEECH IS THE DEFAULT. Everything Claude says in conversation --
answers, delivery notes, findings, questions, the sentence explaining
why something was left out -- is written the way a knowledgeable person
talks.

The protocol's compressed voice ("the SHA is the round trip") keeps its
home in THIS document and in the skills, where a line is reference
somebody scans because they already own the idea. It does not belong in
chat. Plain speech is not a register Claude enters for explanations; it
is how Claude writes unless Tony asks for something else.
"""

REGISTER_NEW = b"""Register Rule
COMPRESSED LANGUAGE IS NOT A STYLE. IT IS A CHANNEL ONLY ONE OF US CAN
READ. Say the thing, not the name of the thing. A sentence that would
only be intelligible to somebody who had already been through the
conversation that produced it does not belong in chat, however accurate
it is.

The asymmetry is the whole reason this rule exists, and the earlier
wording missed it. Claude can unpack "the SHA is the round trip" or
"mechanism whole, store in slices" instantly, because it holds the
entire session at once. Tony cannot, and by the time a sentence is
dense enough to notice, reading it to the end has already cost what the
compression was supposed to save. So compression is free on Claude's
side and expensive on Tony's -- which is why it keeps coming back.
Nothing in the act of writing it tells Claude that anything went wrong.

Tony's words, 2026-09-14, and they are the rule: "I cannot follow
compressed language. Only you can."

WHERE IT FAILS IS SUMMARIES. Listing what was decided names each
decision instead of stating it, and a list of names is compressed prose
with bullet points on it. If a decision is worth restating, it is worth
a sentence. The same goes for a status line, a recap, or a closing
round-up -- those are exactly the places the failure hides, because
they look like service.

THIS DOCUMENT AND THE SKILLS ARE WRITTEN THE OTHER WAY, and that is not
a licence. A line here is reference somebody scans because they already
own the idea. That voice stays in the files and never crosses into
chat.
"""

PROTOCOL_STAMP_OLD = b"""Tony Quintanilla, PE | Claude | v3.58 | September 14, 2026

Cut from bfc0505e at https://github.com/tonylquintanilla/palomas_orrery
"""

PROTOCOL_STAMP_NEW = b"""Tony Quintanilla, PE | Claude | v3.59 | September 14, 2026

Cut from 773e5c2d at https://github.com/tonylquintanilla/palomas_orrery
"""

VERSION_ANCHOR = b"v3.58 (September 14, 2026): No rule changed in this document. ONE"

VERSION_NEW = b"""v3.59 (September 14, 2026): ONE RULE REWRITTEN, the Register Rule, on
Tony's instruction of the same evening. No skill bumped.

WHAT THE OLD WORDING GOT WRONG. It opened "plain speech is the default"
and then gave the compressed voice a home in this document and in the
skills. Read together, those two sentences describe a shared shorthand
that simply belongs in a different place. Tony's correction: it is not
shared. He cannot read it and Claude can, so it is a channel with one
party on it.

THE ASYMMETRY IS NOW THE RULE'S REASON rather than a footnote to it.
Claude holds the whole session at once and unpacks a compressed phrase
without effort. Tony is living through the session and cannot, and
noticing that a sentence is too dense already costs him the reading.
Compression is therefore free on one side and expensive on the other,
which is why every earlier version of this rule decayed: nothing in
writing a compressed sentence tells the writer it failed.

SUMMARIES ARE NAMED as where it fails, because that is where it failed
on 2026-09-14. A closing list of decisions names each one rather than
stating it, and a list of names is compressed prose wearing bullet
points. The evening produced four of those before Tony said so.

The three checks, the two supporting defaults and the backstop are
unchanged. What changed is the opening, which is the part that has to
carry the rule when a session is moving.

The header stamp and the SHA anchor move with this entry.

Version history: v3.56 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

V356_START = b"v3.56 (September 10, 2026): No rule changed in this document. TWO skill"
PROTOCOL_TAIL = b"Functional for Claude, readable for human, signal preserved."
HISTORY_ANCHOR = b"================================================================\nPART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37"


def fail(message):
    print("ERROR: " + message)
    sys.exit(1)


def fingerprint(data):
    """md5 of the file with the generated INDEX zone removed."""
    lf = data.replace(b"\r\n", b"\n")
    a = lf.find(INDEX_START)
    b = lf.find(INDEX_END)
    if a == -1 or b == -1:
        fail("could not find the INDEX zone in %s" % TARGET)
    return hashlib.md5(lf[:a] + lf[b:]).hexdigest()


def apply_once(data, old, new, label):
    count = data.count(old)
    if count != 1:
        print("ANCHOR FAIL: %s matched %d times, expected 1" % (label, count))
        sys.exit(1)
    print("  ok  %s" % label)
    return data.replace(old, new)


def main():
    here = os.path.dirname(os.path.abspath(__file__))

    paths = {}
    for label, rel, want in (("ledger", TARGET, BASE_FP),
                             ("protocol", PROTOCOL, PROTOCOL_FP),
                             ("history", HISTORY, HISTORY_FP)):
        full = os.path.join(here, rel)
        if not os.path.exists(full):
            fail("%s not found beside this script. Put this file in the "
                 "orrery repo root." % rel)
        with open(full, "rb") as handle:
            blob = handle.read()
        if b"\r\n" in blob:
            fail("%s has CRLF line endings; this patch expects LF." % rel)
        got = fingerprint(blob) if label == "ledger" \
            else hashlib.md5(blob).hexdigest()
        if got != want:
            print("ERROR: %s is not the file this patch was built against."
                  % rel)
            print("  expected fingerprint %s" % want)
            print("  found               %s" % got)
            print("  Nothing was written, to any of the three files.")
            sys.exit(1)
        paths[label] = (full, blob)

    ledger = paths["ledger"][1]
    protocol = paths["protocol"][1]
    history = paths["history"][1]

    if b"#### [L-327]" in ledger:
        fail("L-327 is already present; this patch has run.")
    if b"v3.59 (September 14, 2026)" in protocol:
        fail("v3.59 is already in the protocol; this patch has run.")

    ledger = apply_once(ledger, NEW_BLOCKS_ANCHOR, NEW_BLOCKS + NEW_BLOCKS_ANCHOR,
                        "L-327, L-328 and L-329 inserted after L-326")
    ledger = apply_once(ledger, L323_ANCHOR, L323_NEW + L323_ANCHOR,
                        "L-323 note: revision 3 filed, and where it is stale")
    ledger = apply_once(ledger, L322_ANCHOR, L322_NEW + L322_ANCHOR,
                        "L-322 notes: slices, and the unit-token finding")
    ledger = apply_once(ledger, L305_ANCHOR, L305_NEW + L305_ANCHOR,
                        "L-305 note: item 7 as built, two item-5 corrections")

    protocol = apply_once(protocol, REGISTER_OLD, REGISTER_NEW,
                          "Register Rule rewritten")
    protocol = apply_once(protocol, PROTOCOL_STAMP_OLD, PROTOCOL_STAMP_NEW,
                          "header stamp to v3.59 and the anchor to 773e5c2d")
    protocol = apply_once(protocol, VERSION_ANCHOR, VERSION_NEW + VERSION_ANCHOR,
                          "v3.59 version-history entry added")

    # The v3.56 block is MOVED, not retyped, so the two copies cannot drift.
    start = protocol.find(V356_START)
    if start == -1:
        fail("could not find the v3.56 block in the protocol.")
    end = protocol.find(PROTOCOL_TAIL, start)
    if end == -1:
        fail("could not find the protocol's closing line after v3.56.")
    moved = protocol[start:end].rstrip() + b"\n"
    protocol = protocol[:start] + protocol[end:]
    print("  ok  v3.56 block cut from the protocol (%d bytes)" % len(moved))

    if V356_START in history:
        fail("the v3.56 block is already in the history file.")
    if history.count(HISTORY_ANCHOR) != 1:
        fail("could not find PART 2's heading in the history file.")
    history = history.replace(HISTORY_ANCHOR, moved + b"\n" + HISTORY_ANCHOR)
    print("  ok  v3.56 block inserted into the history file, PART 1")

    for label, blob in (("ledger", ledger), ("protocol", protocol),
                        ("history", history)):
        bad = [b for b in bytearray(blob) if b > 127]
        if bad:
            fail("the patched %s carries %d non-ASCII bytes; refusing to "
                 "write anything." % (label, len(bad)))

    for label, blob in (("ledger", ledger), ("protocol", protocol),
                        ("history", history)):
        with open(paths[label][0], "wb") as handle:
            handle.write(blob)

    print("patch applied to three files")
    print("  items added, and they are:")
    for name in ("L-327 tool repairs from the rules-vs-reasoning round",
                 "L-328 subtraction pass on the skill layer",
                 "L-329 the Register Rule rewritten"):
        print("    %s" % name)
    print("  items annotated, and they are:")
    for name in ("L-305 (item 7 as built, two item-5 corrections)",
                 "L-322 (slices, and the unit-token finding)",
                 "L-323 (revision 3 filed and where it is stale)"):
        print("    %s" % name)
    print("  protocol changes, and they are:")
    for name in ("Register Rule rewritten",
                 "v3.59 added to the version history",
                 "header stamp and SHA anchor moved",
                 "v3.56 moved down into PROJECT_INSTRUCTIONS_HISTORY.md"):
        print("    %s" % name)
    print("  next: run ledger_index.py -- expect 324 L-blocks, up from 321")


if __name__ == "__main__":
    main()
