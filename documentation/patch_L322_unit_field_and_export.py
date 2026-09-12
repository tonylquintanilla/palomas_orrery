"""patch_L322_unit_field_and_export.py -- close L-305 Gap item 3, open
L-322, and restamp the master plan to v31.

Built on orrery 2432db648f317387527a920aa0f3d40c2ed2f3df
at https://github.com/tonylquintanilla/palomas_orrery

RUN:  save this file into the palomas_orrery repo ROOT (the folder that
holds LEDGER_CONSOLIDATED.md), open it in VS Code, click Run.
Equivalent command line: python patch_L322_unit_field_and_export.py

It edits TWO files:
  LEDGER_CONSOLIDATED.md                              (3 edits)
  documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md    (2 edits)

Then run ledger_index.py (Run button). Expect
"OK: 317 L-blocks parsed, no consistency problems."

WHAT IT DOES
  1. L-305 Gap item 3 CLOSES by reading, and its remediation half is
     re-homed to L-322 rather than left inside a closing item.
  2. L-305 gains one bullet: the two things the L-322 design round puts
     into this item now (a # Unit: line per new constant, and the bow
     shock standoff as an expression).
  3. NEW ITEM L-322 -- units declared in the store, and the orrery as
     producer. Nine rulings from the 2026-09-11 design session.
  4. Master plan: v31 stamp, and Section 5a gains the 2026-09-11
     subsection. The rolling stamp drops back to THREE entries (v31,
     v30, v29) as the ledger skill requires; it was carrying four.

GUARD: the ledger is fingerprinted OUTSIDE its ledger_index.py INDEX
zone and the master plan in full, both line-ending normalised, so this
runs on an LF or a CRLF working copy. All or nothing: on any failure
NOTHING is written to either file.
"""

import hashlib
import os
import sys

LEDGER = "LEDGER_CONSOLIDATED.md"
PLAN = os.path.join("documentation", "MASTER_PLAN_INTERACTIVE_GALLERY.md")
LEDGER_FP = "f53a18b307163f80c3d70f4b4268a57a"
PLAN_FP = "bce59a17f170a079ac65285075994f57"
INDEX_START = b"<!-- INDEX:START"
INDEX_END = b"<!-- INDEX:END -->"

L322 = b'''#### [L-322] Units declared in the store, and the orrery as producer
<!-- L:322 status:OPEN upd:2026-09-11 section:A flag: rice:4/5/70/6 -->
- **Where this came from.** L-305 Gap item 3 asked a narrow question --
  how does `check_store_drift` treat a dimensionless pointer -- and the
  answer opened a wide one. Design session 2026-09-11, zero code. The
  record is `documentation/DESIGN_unit_field_and_export_rev2_20260911.md`,
  which supersedes revision 1 of the same date and folds in a Claude
  Fable 5.1 review.
- **What the read found.** `gallery_maintenance_run.py` infers a
  constant's unit from a SUFFIX on its name and knows four: `_RADII`,
  `_AU`, `_KM`, and an Earth-radii special case. Everything else returns
  NO UNIT, which is printed and counted as unexaminable but does NOT
  fail the run -- only DRIFT fails. Measured 2026-09-11 at gallery
  `9c056d1a` against orrery `2432db64`: 53 served pointers, 48 MATCH,
  0 DRIFT, 0 NO UNIT, 5 NOT IN STORE; of the 48 matches 44 compare in
  the same unit, 2 convert and 2 take a coefficient fast path. Of the
  88 top-level assignments in `constants_new.py`, 71 are suffix-readable
  and 17 are not. [measured]
- **Tony's rulings, 2026-09-11.** (1) A unit is a DECLARED FIELD beside
  the value -- `# Unit:` as a fifteenth comment key -- not a suffix on a
  name; in engineering he has always used units, not literals. (2) The
  suffix is DROPPED as a declaration, not kept as a cross-check, because
  two declarations of one fact can disagree. (3) Order: `# Unit:` lines
  land first, then missing-unit-fails and suffix-dropping land together
  -- dropping the suffix first puts 46 of 48 checks dark while the run
  stays green [measured]. (4) DIMENSIONAL ANALYSIS is the real check on
  a unit assignment, not a text match, and belongs as its own check in a
  maintenance runner. (5) A cited value is a NEW CONSTANT unless it can
  be DERIVED; a number a paper prints that our constants could compute
  is an expression. (6) The orrery EXPORTS; the gallery does not parse
  orrery source. (7) The export cannot go stale because the orrery
  runner keeps it current as a sixth GENERATOR. (8) The JOIN of orrery
  values with gallery presentation happens in the ASSEMBLER, not mixed
  in `data/objects_config.json`. (9) `constants_new.py` holds PHYSICAL
  VALUES ONLY -- the five non-measurements leave the file, so every line
  has a unit, a blank is unambiguously an error, and the export needs no
  skip list.
- **The five leaving the store, with import direction checked**
  [verified @2432db64]: `stellar_class_labels` -> `visualization_core.py`
  (2d and 3d already import from core); `HORIZONS_MAX_DATE` ->
  `celestial_objects.py` (194 objects with Horizons IDs, 65 date-range
  fields, already imports datetime, imports nothing from
  `constants_new`); `DEFAULT_MARKER_SIZE` and `CENTER_MARKER_SIZE` ->
  `palomas_orrery_helpers.py`. The marker sizes were first ruled into
  `palomas_orrery.py`; that fails, because `palomas_orrery.py` imports
  FROM helpers at line 84 and helpers cannot import back without a
  cycle. Tony re-ruled on being shown it. `spectral_subclass_temps`
  (kelvin) and `KNOWN_ORBITAL_PERIODS` (days) STAY -- they are physical
  and simply need `# Unit:` lines. Note: the four files importing
  `stellar_class_labels` are the only ones seen carrying CRLF.
- **Two additions from the Fable review, adopted.** Export the WHOLE
  store rather than the 53 pointed-at values, because exporting a subset
  means the orrery keeps a list of what the gallery wants and that list
  drifts. And the `# Unit:` walk is the `# Status:` walk -- only 2 of 88
  assignments carry a `# Status:` line today [measured], and one visit
  per assignment writes both.
- **The framing error the review caught, and it is the important one.**
  Revision 1 called the new gallery check "the SHA round trip" as though
  it were one hop. It is TWO: the gallery serving what the orrery
  published, and the orrery publishing what the store holds. The export
  therefore carries the hash of the `constants_new.py` bytes it was
  generated from, and a CHECKER in the orrery runner compares that hash
  to the file on disk. The runner informs the push but is not a hook, so
  a push without a run would otherwise leave a stale export with nothing
  saying so.
- **What the gallery's drift check becomes.** Two checks, neither of
  them today's: gallery side, the served export's bytes equal the
  orrery's export at a recorded orrery SHA, printing the SHA compared
  against so it cannot go green by never resolving; join side, every
  pointer resolves to a row in the export BY NAME and a pointer with no
  row FAILS. The per-value comparison is the hand copy's net kept after
  the hand copy is gone -- retire it.
- **The held patch.** `patch_L305_store_drift_units.py` extends the
  gallery's suffix table and makes L-305's fifteen pointers green. It
  was written, tested (15 of 15 MATCH, no regression on the existing 53)
  and HELD UNRUN, because it puts a naming vocabulary for orrery
  constants inside the gallery repo. It is NOT to be run. [Tony's
  ruling, 2026-09-11]
- **Sequencing, ruled.** L-305's renderer proceeds under today's
  architecture; this item is NOT a gate on it. Bounded cost: twelve of
  L-305's fifteen new values report NO UNIT until the export lands. That
  is THIS ROW, one row for the class, not fifteen.
- **Note (Claude):** RICE proposed 4/5/70/6. Reach is every served value
  and both repos; Effort is the export generator, the store migration
  over 88 assignments, two parsers deleted, the assembler join and two
  new checks. Confidence 70 because the design survived one review with
  all nine rulings intact and the measurements were run against live
  code, not recalled.
**Gap:** the whole item, in ruling 3's order. Still open and NOT ruled:
(a) the five non-top-level served values (`planet_poles` for Sun, Earth,
Jupiter and Saturn, and a `create_sun_galactic_tide` default) -- the
review proposes the Status Line dict scoping and One Value One Home,
moving them into the store, its lean being AFTER L-305 because two are
the Sun's and Earth's poles and a wrong move puts a closed exhibit back
under Mode 5; (b) which check a BARE LITERAL gets, now three
options rather than two. Fable's derive-and-compare is NOT available
here: Jelinek's R0 IS the standoff at 1 nPa, so deriving it is
circular, and Shue's redundancy sits in Table 1's SEED column, not the
fitted values being stored. What remains: Jelinek's eqs. 17-18 refit
(12.90 and 14.94 against the model's 12.82 and 15.02) as a
transcription check; provenance alone, stated on the row; or TONY'S OWN
READ of the paper against the row, recorded with the page or table, the
date, and that it was his (Tony's ruling, 2026-09-11). The third is the
only one that catches a correctly-cited, plausibly-rendering,
slightly-wrong digit. The three checks cover different failures and
none substitutes: Mode 5 sees a wrong UNIT instantly and a wrong third
decimal never, so it is a BACKSTOP and not the check; a cross-model
worksheet reads the digits and is blind to the render; Tony's read is
the only one that reaches precision. It needs a scope written once
("where critical") and a RECORDED verdict, or a lapsed habit reads
exactly like a performed check. A row verified by Tony is a different
provenance state from one verified by a model and the worksheet schema
should say which -- provenance-discipline at its next bump; (c) which runner hosts the dimensional check, and
what it checks for the 57 bare literals, where provenance may be the
only check a primary datum gets; (d) SIGNIFICANT FIGURES. The
`Derived:` discipline already rules that a derived value reports no
more figures than its numerator, but ruling 5 turns derived values into
EXPRESSIONS, so Python returns full float precision and nobody types a
rounded figure -- `15.02 * 2 ** (-1 / 6.55)` is 13.511736110493397
against four-figure inputs. Python can ROUND to significant figures
(`float("%.4g" % x)`, already used in `export_orbit_cache.py`) but
cannot TRACK them through arithmetic, so like the unit they have to be
DECLARED per constant. Dimensional analysis checks a dimension, never a
precision, so nothing else in this design would catch it. (e) whether
`astropy.units` hosts the dimensional check rather than a hand-rolled
one. Astropy is ALREADY a dependency -- five modules import it,
including `astropy.units` in `hr_diagram_distance.py` [verified
@2432db64]. It is Python-only, which costs nothing, because under
ruling 6 dimensional reasoning happens once in the orrery and the
gallery receives a number and a unit STRING. Two shapes, very different
sizes: store Quantities (`10.0 * u.R_earth`), which makes dimensional
errors impossible but returns Quantities to 29 importing modules over
37 import lines where Plotly wants floats; or keep floats and use
astropy only INSIDE the check, parsing each `# Unit:` line. The second
leaves the store untouched, and ruling 6 argues for it -- the export
unwraps to plain numbers at the boundary either way. Related and worth
asking in the same round: ruling 9's migration visits all 88
assignments, which is the natural moment to ask whether the store's
format should change at all.
**Tony-action (do):** commit
`documentation/DESIGN_unit_field_and_export_20260911.md` and
`documentation/DESIGN_unit_field_and_export_rev2_20260911.md`, and the
held `patch_L305_store_drift_units.py` into the GALLERY repo's
`documentation/` UNRUN.
**Ref:** L-305, L-306 (approximations are not promoted), L-314,
`constants_new.py`, `provenance_scanner.py`, `orrery_maintenance_run.py`,
`celestial_objects.py`, `visualization_core.py`,
`palomas_orrery_helpers.py`, gallery `gallery_maintenance_run.py`,
gallery `data/objects_config.json`, gallery `gallery/assembler/catalog.py`,
skills/provenance-discipline/SKILL.md (the Status Line, One Value One
Home), skills/gallery-cache-builder/SKILL.md,
skills/gallery-assembler/SKILL.md, skills/interactive-exhibit/SKILL.md.

'''

PLAN_STAMP_OLD = b"""**Last updated:** September 10, 2026, evening (v30: L-305's paper read"""

PLAN_STAMP_NEW = b"""**Last updated:** September 11, 2026 (v31: a DESIGN SESSION, zero code.
Both magnetosphere papers read from the PDFs and L-305's Gap items 1 and
2 closed; every computed figure in that item reproduced from the
published equations. Gap item 3 asked how the drift check treats a
dimensionless pointer and opened an architecture: units become a
DECLARED FIELD in the store, the suffix reader is retired, the orrery
EXPORTS and the gallery stops parsing orrery source, and the join moves
to the assembler (L-322, nine rulings). `constants_new.py` becomes
physical values only. A gallery patch extending the suffix table was
written, tested and HELD UNRUN. One review round with Claude Fable 5.1;
all nine rulings held and it caught a two-hop error the record had
collapsed into one. Section 5a gains the 2026-09-11 subsection; with
Anthropic's Claude Opus 5. v30: L-305's paper read"""

PLAN_5A = b'''### 2026-09-11 -- units become a field, and the orrery becomes a producer

**A narrow question opened a wide one** (L-305 Gap item 3 -> L-322). The
gallery's store-drift check reads each constant's unit from a SUFFIX on
its name and knows four. L-305 is about to serve fifteen values of which
twelve are not lengths, so twelve would report NO UNIT -- printed,
counted as unexaminable, and NOT a failure, because only DRIFT fails.
The run would have gone green with twelve of fifteen unchecked.

**Tony's ruling: a unit is a field, not a literal in a name.** In
engineering he has always used units, not literals. `# Unit:` becomes a
fifteenth comment key in the store; the suffix reader is retired rather
than kept as a cross-check, because two declarations of one fact can
disagree. And the deeper move: the orrery EXPORTS its values, the
gallery stops parsing orrery source, and the join with gallery
presentation happens in the ASSEMBLER rather than mixed into
`data/objects_config.json`. `constants_new.py` becomes physical values
only, so every line in it has a unit and a blank is an error.

**What made the export architecture reachable rather than aspirational:**
nothing generates `objects_config.json` today -- it is hand-maintained,
and the gallery's per-value check is the net under that hand copy.
`orrery_maintenance_run.py` already runs five GENERATORS and fourteen
CHECKERS, so the export is a sixth generator on rails that exist, and
`doc_index.py`'s own comment already carries Tony's ruling that a
generator beats a checker because it fixes the producer.

**One review round with Claude Fable 5.1.** All nine rulings held. It
caught a two-hop error -- the export is the gallery serving what the
orrery published AND the orrery publishing what the store holds, and the
record had collapsed them -- and it contributed the whole-store export
and the one-walk migration. Two of its own numbers were wrong and are
corrected in the record.

**What this does to the order.** Nothing moves. L-322 is NOT a gate on
L-305, whose renderer proceeds under today's architecture; the bounded
cost is twelve values reporting NO UNIT, recorded as one class row. Two
cheap things go into L-305 now because the export will require them
anyway: a `# Unit:` line on each new constant, and the bow shock
standoff written as an expression rather than a typed number. Record:
`documentation/DESIGN_unit_field_and_export_rev2_20260911.md`.

'''


def fail(msg):
    print("FAILURE: " + msg)
    print("NOTHING was written to either file.")
    print("Undo is Discard Changes in GitHub Desktop.")
    sys.exit(1)


def load(path, fp_expected, skip_index_zone):
    if not os.path.exists(path):
        fail("%s not found. Run this from the palomas_orrery repo root."
             % path)
    raw = open(path, "rb").read()
    was_crlf = b"\r\n" in raw
    content = raw.replace(b"\r\n", b"\n") if was_crlf else raw
    if skip_index_zone:
        a = content.index(INDEX_START)
        b = content.index(INDEX_END) + len(INDEX_END)
        probe = content[:a] + content[b:]
    else:
        probe = content
    fp = hashlib.md5(probe).hexdigest()
    if fp != fp_expected:
        fail("BASE MOVED in %s. Fingerprint %s, expected %s."
             % (path, fp, fp_expected))
    print("ok   %s fingerprint matches%s"
          % (path, " (CRLF)" if was_crlf else ""))
    return content, was_crlf, len(raw)


def apply(path, content, edits):
    out = content
    for i, (old, new) in enumerate(edits, 1):
        n = out.count(old)
        if n != 1:
            fail("ANCHOR FAIL in %s, edit %d: expected 1 match, got %d.\n"
                 "         %r" % (path, i, n, old[:70]))
        out = out.replace(old, new)
        print("ok   %s edit %d applied" % (path, i))
    bad = [c for c in out if c > 127]
    if bad:
        fail("encoding gate: %d non-ASCII bytes in %s." % (len(bad), path))
    return out


def main():
    ledger, ledger_crlf, ledger_was = load(LEDGER, LEDGER_FP, True)
    plan, plan_crlf, plan_was = load(PLAN, PLAN_FP, False)

    ledger_edits = [
        # 1. Gap item 3 closes, and its remediation half is re-homed
        (b"""(3) Read
`check_store_drift` for dimensionless and non-length units and extend
its table before any new pointer is served.""",
         b"""(3) CLOSED 2026-09-11 by
reading the code. `check_store_drift` infers a constant's unit from a
SUFFIX on its name and knows four (`_RADII`, `_AU`, `_KM`, and an
Earth-radii special case); everything else returns NO UNIT, which is
printed and counted as unexaminable but does NOT fail the run, since
only DRIFT fails. Measured against this item's fifteen new pointers:
3 MATCH, 12 NO UNIT. The REMEDIATION half of this item, "extend its
table", is SUPERSEDED and re-homed to L-322: units are being declared
in the store instead and the suffix reader retired, so the patch that
would have extended the gallery's table is HELD UNRUN and is not to be
run. Until L-322 lands the twelve report NO UNIT, recorded as one class
row THERE, not fifteen here (Tony's sequencing ruling, 2026-09-11)."""),

        # 2. what L-305 now carries from the L-322 round
        (b"not a gap.\n**Gap:**",
         b"""not a gap.
- **2026-09-11, two things this item carries from the L-322 design
  round.** Each new constant gets a `# Unit:` line as it is written --
  the export will require one and writing it at creation is free. And
  the bow shock standoff is an EXPRESSION, not a typed 13.51: the
  store's own parser evaluates `15.02 * 2 ** (-1 / 6.55)` to 13.5117
  [computed 2026-09-11]. Shue's magnetopause standoff cannot follow --
  it needs a hyperbolic tangent, and the parser allows only add,
  subtract, multiply, divide and power, so the assignment is DROPPED
  silently. It stays a literal carrying a `# Calculation:` line until
  L-322 retires that parser. **Tony's ruling (2026-09-11):** a cited
  value is a new constant unless it can be derived.
**Gap:**"""),

        # 3. the new item
        (b"(`renderShellSet`), skills/provenance-discipline/SKILL.md (the braid).\n\n"
         b"#### [L-278] ",
         b"(`renderShellSet`), skills/provenance-discipline/SKILL.md (the braid).\n\n"
         + L322 + b"#### [L-278] "),
    ]

    # Drop v28 and v27 so the rolling stamp keeps THREE entries
    # (v31, v30, v29), which is what the ledger skill requires. It was
    # carrying four before v31 was added. git holds the dropped text.
    drop_start = b"Anthropic's Claude Opus 5. v28,"
    drop_end = b"Claude Fable 5.1.)"
    a = plan.index(drop_start) + len(b"Anthropic's Claude Opus 5.")
    b_ = plan.index(drop_end) + len(drop_end)
    old_tail = plan[a:b_]

    plan_edits = [
        (PLAN_STAMP_OLD, PLAN_STAMP_NEW),
        (old_tail, b")"),
        (b"### What this section deliberately does not carry",
         PLAN_5A + b"### What this section deliberately does not carry"),
    ]

    new_ledger = apply(LEDGER, ledger, ledger_edits)
    new_plan = apply(PLAN, plan, plan_edits)

    for path, out, crlf, was in ((LEDGER, new_ledger, ledger_crlf, ledger_was),
                                 (PLAN, new_plan, plan_crlf, plan_was)):
        final = out.replace(b"\n", b"\r\n") if crlf else out
        with open(path, "wb") as f:
            f.write(final)
        print("wrote %s (%d bytes, was %d)" % (path, len(final), was))

    print("")
    print("NOTE: the master plan's rolling stamp was carrying FOUR")
    print("      versions (v30-v27). It now carries THREE (v31, v30,")
    print("      v29), as the ledger skill requires. v28 and v27 are in")
    print("      git history.")
    print("")
    print("NEXT: run ledger_index.py (Run button). Expect")
    print("      'OK: 317 L-blocks parsed, no consistency problems.'")
    print("      Then commit and push.")


if __name__ == "__main__":
    main()
