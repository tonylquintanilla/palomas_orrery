"""
patch_L323_L324_session_20260912.py - the 2026-09-12 session, in the ledger.

Run it:
    Save this file into the ORRERY repo root (beside
    LEDGER_CONSOLIDATED.md), open it in VS Code and click Run, then run
    ledger_index.py.

What it does, in LEDGER_CONSOLIDATED.md and nowhere else:

  1. L-305: a dated bullet recording that Gap item 4 landed, what rode
     with it, and the one-assignment-per-line lesson. upd: -> 2026-09-12.
  2. L-321: a dated bullet recording the reframe -- the belts' figures
     are not a units problem but a states problem -- and that the slice
     gained the magnetotail extent. upd: -> 2026-09-12.
  3. Opens **L-323**, a figure in prose needs a home.
  4. Opens **L-324**, one assignment per line in constants_new.py.

New items go at the top of section A, immediately after the section
heading, which is where the indexer expects detail blocks to live.

The guard fingerprints the ledger's text OUTSIDE the INDEX zone, with
line endings normalised (L-315).

FAILURE: any assert fires and NOTHING is written.
Undo is Discard Changes in GitHub Desktop.

Module created: September 2026 with Anthropic's Claude Opus 5.

Role: devtool
Domain: dev_tools
"""

import hashlib
import os
import sys

TARGET = "LEDGER_CONSOLIDATED.md"
BASE_FINGERPRINT = "46fa8a2cef5e095269341daf8c96cfb8"

META_305_OLD = "<!-- L:305 status:OPEN upd:2026-09-11 section:A flag: rice:4/4/60/4 -->"
META_305_NEW = "<!-- L:305 status:OPEN upd:2026-09-12 section:A flag: rice:4/4/60/4 -->"
META_321_OLD = "<!-- L:321 status:OPEN upd:2026-09-10 section:A flag: rice:3/3/60/3 -->"
META_321_NEW = "<!-- L:321 status:OPEN upd:2026-09-12 section:A flag: rice:3/3/60/3 -->"

BULLET_305 = """- **2026-09-12, Gap item 4 LANDED** (`patch_L305_magnetosphere_constants.py`,
  four files, eighteen edits, pushed at `5b88007f`). Fifteen rows added
  -- Shue's eight coefficients, Jelinek's R0 / eps / lambda, the bow
  shock cut angle, three declared solar wind conditions. Both standoffs
  superseded: the magnetopause to 10.251872972379905 as a typed literal
  (the gallery's store parser evaluates only + - * / and **, so a tanh
  assignment leaves the CHECKED set and reports NOT IN STORE under a
  wrong reason), the bow shock to an EXPRESSION over the new rows.
  Every row written carries a `# Unit:` and a `# Status:` line.
  Removed: the Lugaz-midpoint derivation, the Farris & Russell "Model
  form" miscitation, the stale shell-migration Note.
  RIDING WITH IT, on Tony's rulings: six `:g` quotes became `:.4g` so
  the hovers report 10.25 and 13.51 rather than six figures; the
  Lugaz-midpoint SENTENCE was deleted from the bow shock hover and its
  attribution moved to Jelinek, because the new number made a cited
  sentence arithmetically false and a patch may not leave its own
  output untrue; `RADIATIVE_ZONE_AU`'s rung was added in passing.
  `test_status_lines.py` shipped with it and is wired into the
  maintenance run.
  **The lesson, and it is a convention nothing states.** The bow shock
  expression was first written as a parenthesised assignment over three
  lines -- the only multi-line assignment among 88 rows -- and
  `constants_change_report.py`, which matches `NAME = value` on ONE
  line, reported the constant REMOVED. See L-324.
  **Still open:** items 5 (the port), 6 (the gallery config, which
  carries THREE retired claims: the Lugaz midpoint, Farris & Russell,
  and the magnetotail's "past 1,000 radii"), 7 (the hovers, after
  L-321's verdicts), 8 (store drift then Mode 5, phone first).
"""

BULLET_321 = """- **2026-09-12, the slice reframed, and it is not a units problem.**
  Tony's ruling: units convert and significant figures already govern
  them, so radii-versus-kilometres is a convention and not a design
  question. What the viewer must be told is which STATE each number is
  in -- measured, an envelope with no sharp edge, or a stylization.
  For the belts that reads: the flux peak is measured and already
  interpolates; the span has no edge to find, because flux falls off
  and the boundary depends on threshold, instrument and epoch, and the
  outer belt's outer edge moves with activity (the store row says so);
  the drawn ring is a stylization of a field-line shell and has never
  claimed otherwise. So we are NOT picking a winning span and storing
  it. We store the envelope with its sources, or we state the absence.
  The worksheets change question accordingly: not "is 3 to 7 right" but
  "does your source state an edge -- at what flux threshold and from
  what epoch -- or does it say there is none." The magnetotail extent
  joined the slice. Design record and revision 3 prompts are OWED; the
  2026-09-11 prompts must not be sent as they stand (see L-323).
"""

L323 = """#### [L-323] A figure in prose needs a home (the Note is not a store)
<!-- L:323 status:OPEN upd:2026-09-12 section:A flag: rice:3/4/70/3 -->
- **Where this came from.** A visitor opening Earth's magnetosphere can
  meet three figures for the outer radiation belt: the drawn torus at
  4.5 R_E (`EARTH_VAN_ALLEN_OUTER_RADII`, the flux peak), the plot hover
  saying it spans roughly 3 to 7 Earth radii, and the GUI tooltip and
  its `shell_configs.py` twin saying 13,000 to 60,000 km above the
  surface. Two of the three carry citations.
- **The diagnosis, corrected by a Fable review round on 2026-09-12.**
  These strings did not drift from the store. The span IS in the store
  -- as PROSE, in each belt row's `# Note:` line -- where nothing can
  interpolate it and nothing can check it, and every downstream copy was
  typed from that prose. The peak interpolates and therefore cannot
  disagree with the drawn torus; the span is typed because no VALUE
  holds it. **A Note became a store.** That is the class, and it recurs
  wherever a row carries a figure in its Note that the row's value does
  not hold.
- **It has already drifted inside one row.** The outer belt's own
  `# Source:` cites Baker et al. (2018) at r ~ 3 to 6.5 R_E geocentric
  from SAMPEX; its `# Note:` three lines below says L = 3 to 7. Different
  upper edge, different frame, same row, and NO Source line on that row
  states L = 3 to 7. The inner belt is quieter and worse: its Note gives
  L = 1.1 to 2 and not one of its Source lines states any span at all.
  The gallery's `van_allen_belts` feature repeats both Notes word for
  word. [verified @5b88007f]
- **The mechanism is already ruled and already worked in this file.**
  L-249 (2026-08-26): info strings stop typing boundary figures and
  interpolate the store, because the store is the only home for a
  numeric value "in prose as much as in code."
  `provenance-discipline`, When the Source Gives a Range: store the
  range as DATA, derive the drawn value by a stated rule, let display
  text interpolate the envelope. The worked pair is
  `GRAVITATIONAL_INFLUENCE_AU` with `GRAVITATIONAL_INFLUENCE_RANGE_AU`
  (L-179), interpolated at both ends in `solar_visualization_shells.py`.
- **Scope, ruled 2026-09-12.** First slice is the two belts plus the
  magnetotail extent -- what the artifact renders. OUT: Shue's and
  Jelinek's validity ranges (item 7 would add them), and Lugaz's
  corroborating 11 to 14 R_E, which L-305 left in the store Note.
  Units are a convention, not a design question. Values land with
  L-305 item 7, after L-321's verdicts.
- **The magnetotail is the sharpest case.** The orrery draws its tail
  from `params['tail_length'] = 100` typed at the call site; the gallery
  serves the same 100 again as `length_radii`. Two hand copies of one
  drawing choice in two repositories, no store row. The OBSERVED extent
  is in neither: the gallery's `_declared` says "past 1,000 radii",
  which the 2026-09-11 read record corrected to about 1,000 on Ness et
  al. (1967) -- a single Pioneer 7 crossing at 900 to 1,050 radii, title
  says "probable", no coherent tail observed. Fable's split, adopted:
  the drawn 100 stays where it is drawn (A Drawing Approximation Does
  Not Promote); the observed extent earns a store row, as an envelope.
- **Note:** two scalars, not a tuple, on Fable's reasoning -- provenance
  is per number (the outer belt's outer edge moves and its inner edge
  does not), the checker's derived rule resolves top-level scalars, and
  the gallery's parser drops tuples. `GRAVITATIONAL_INFLUENCE_RANGE_AU`
  is not migrated; it is one row of backlog by class.
- **Note:** two skills state the range rule and one is the superseded
  form. `orrery-coding-conventions` 1.8 (Visualization Constant vs Range
  Convention) still teaches best-value-in-code, range-in-the-comment,
  which is exactly what the belt rows did; `provenance-discipline` says
  in so many words that it supersedes that. A fresh session loading the
  coding skill for hover work would rebuild the failure. One class row:
  a rule stated in two skills, one superseded. RICE 3/4/70/3 -> 2.33
  proposed, not confirmed.
**Gap:** the design record and the revision 3 worksheet prompts are
OWED and were not written on 2026-09-12. The 2026-09-11 prompts must
NOT be sent as they stand: prompt 3 tells the checkers the inner belt
figures are consistent (converted, 1.1 R_E is 638 km against the
tooltip's 1,000, so they are not), row 5 hands the inner span a Baker
citation the string never makes (the string cites Baker for the PEAK;
row 11 gets the outer belt right), and the belt rows still ask which
span is correct rather than whether an edge exists at all.
**Ref:** L-321, L-305 items 6 and 7, L-322, L-249, L-179,
`constants_new.py` belt rows, `earth_visualization_shells.py`
`belt_texts`, gallery `data/objects_config.json` `van_allen_belts`,
`documentation/L321_slice1_magnetosphere_strings_20260911.md`.

"""

L324 = """#### [L-324] One assignment per line in constants_new.py
<!-- L:324 status:OPEN upd:2026-09-12 section:A flag: rice:2/2/90/1 -->
- **Where this came from.** L-305's item 4 patch wrote
  `EARTH_BOW_SHOCK_STANDOFF_RADII` as a parenthesised assignment over
  three lines. `constants_change_report.py` matches `NAME = value` on
  ONE line, saw the name with nothing readable after it, and reported
  `REMOVED (was 12.5)`. It then announced that two changed lines carried
  numbers it could not examine, and failed the run. The tool behaved
  correctly; the assignment did not. Fixed by
  `patch_L305_bow_shock_one_line.py`, 135 characters against a previous
  longest assignment line of 115.
- **Nothing states the convention.** It was the only multi-line
  assignment among 88 top-level rows, so the convention is real and
  unwritten. Not in `orrery-coding-conventions`, not in
  `provenance-discipline`.
- **Why it will recur.** L-322's migration visits all 88 assignments and
  its ruling 5 turns cited values into expressions over named constants.
  Those get long. The next one to exceed a comfortable line will be
  written the same way.
- **Note:** two ways to close it, and they are not equivalent. Write the
  convention into a skill, which costs a bump and leaves the tool
  brittle; or teach `constants_change_report.py` to read a parenthesised
  continuation, which `test_status_lines.py` and the gallery's `ast`
  parser already do. The second is the better fix and the larger change.
  Tony's call. RICE 2/2/90/1 -> 3.6 proposed, not confirmed.
- **Note:** the report's blind-spot announcement is the part to preserve
  whichever way this goes. It did not silently skip what it could not
  read; it named the lines and failed. That is A Check That Cannot Fail
  working as intended.
**Gap:** decide which fix, then do it.
**Ref:** L-305, L-322, `constants_change_report.py`,
`test_status_lines.py`, `skills/orrery-coding-conventions/SKILL.md`.

"""


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, TARGET)
    if not os.path.exists(path):
        print("ERROR: %s is not beside this script. NOTHING was written."
              % TARGET)
        return 1

    raw = open(path, "rb").read()
    was_crlf = b"\r\n" in raw
    text = raw.decode("utf-8").replace("\r\n", "\n")

    try:
        a = text.index("<!-- INDEX:START")
        b = text.index("<!-- INDEX:END -->") + len("<!-- INDEX:END -->")
    except ValueError:
        print("ERROR: INDEX zone markers not found. NOTHING was written.")
        return 1
    actual = hashlib.md5((text[:a] + text[b:]).encode("utf-8")).hexdigest()
    if actual != BASE_FINGERPRINT:
        print("ERROR: base moved. Ledger text outside the INDEX zone hashes")
        print("       to %s; built against %s." % (actual, BASE_FINGERPRINT))
        print("       NOTHING was written.")
        return 1
    print("ok   base fingerprint matches (text outside the INDEX zone)%s"
          % (" [CRLF]" if was_crlf else ""))

    # The two new blocks go directly above the L-322 block, which is the
    # first detail block after the index zone in section A.
    anchor_322 = "#### [L-322] Units declared in the store, and the orrery as producer\n"

    edits = [
        ("L-305 metadata upd:", META_305_OLD, META_305_NEW),
        ("L-321 metadata upd:", META_321_OLD, META_321_NEW),
        ("L-305 dated bullet",
         META_305_NEW + "\n", META_305_NEW + "\n" + BULLET_305),
        ("L-321 dated bullet",
         META_321_NEW + "\n", META_321_NEW + "\n" + BULLET_321),
        ("L-323 and L-324 opened", anchor_322, L323 + L324 + anchor_322),
    ]

    out = text
    for label, old, new in edits:
        n = out.count(old)
        if n != 1:
            print("ANCHOR FAIL: %s matched %d times, expected 1. NOTHING was "
                  "written." % (label, n))
            return 1
        out = out.replace(old, new)
        print("ok   %s" % label)

    added = BULLET_305 + BULLET_321 + L323 + L324
    try:
        added.encode("ascii")
    except UnicodeEncodeError as exc:
        print("ANCHOR FAIL: added text is not ASCII (%s). NOTHING was "
              "written." % exc)
        return 1
    print("ok   encoding gate: added text is ASCII")

    final = out.encode("utf-8")
    if was_crlf:
        final = final.replace(b"\n", b"\r\n")
    with open(path, "wb") as handle:
        handle.write(final)
    print("patch applied (%d bytes, was %d)" % (len(final), len(raw)))
    print("")
    print("NEXT: run ledger_index.py (Run button). Expect")
    print("      \"OK: 319 L-blocks parsed, no consistency problems.\"")
    return 0


if __name__ == "__main__":
    sys.exit(main())
