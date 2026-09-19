#!/usr/bin/env python3
"""
patch_L322_8_ledger_stage_a_20260919.py -- ORRERY repo.

Run: save this file in the ORRERY repo ROOT (next to
LEDGER_CONSOLIDATED.md), open it in VS Code and click Run.  Or:
python patch_L322_8_ledger_stage_a_20260919.py

A patch is run from its repository's ROOT and filed in documentation/
AFTER it has run. Filed first and run second, it stops with one line,
writes nothing, and the push goes out without it. This script refuses to
run from documentation/.

Built on orrery 189c298755256b742f5f0cf9d26138b94be64235
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 2ebd001f2ec5d358aa6bb5fa1c6a573be99a502d
at https://github.com/tonylquintanilla/tonyquintanilla.github.io)

STAGE A of documentation/BUILD_MANIFEST_L322_earth_slice_20260919.md.
One patch, one file, four ledger blocks. It carries the corrections the
last two days produced so the Earth-slice walk starts from a ledger that
is true.

WHAT IT DOES (LEDGER_CONSOLIDATED.md only, 11 anchored edits):

  L-337  Tony's addition of 2026-09-19, quoted whole from the handoff,
         plus his confirmation of the same day naming where the orrery
         already draws it. The bullet that said nobody had looked at
         what the marker is is corrected, with its old wording kept in
         place so the correction is visible. upd date moves.

  L-249  a dated record of what was built on 2026-08-26 and where,
         measured at 189c2987; the stated blocker cleared; the mantle
         disagreement its Note left open recorded as settled; then
         CLOSED, with its one live residue re-homed to L-253 and to
         L-322's Earth slice by name. Its spent Tony-action is struck
         with the reason.

  L-322  Tony's ruling of 2026-09-19 on what "critical" means in ruling
         (b), in his words; and a new current Gap naming the Earth-slice
         manifest and its four stages. The 2026-09-16 Gap is relabelled
         as superseded rather than deleted. The deployment line this
         patch was asked to add was ALREADY HERE (the 2026-09-17 note
         naming gallery d2ca28b6 and the cache rebuild at 9ff39cc4), so
         nothing is duplicated.

  L-340  the three screenshot findings recorded as fixed, by
         patch_L340_1_editor_polish_20260919.py at gallery 2ebd001f;
         that patch's direct write of data/objects_config.json recorded
         as the exception it is, and owed to interactive-exhibit's next
         bump; why the record was missing until now; and a fourth
         finding, the arrival smoke check's hardcoded EXPECTED list.

WHAT IS PERMANENT AND WHAT IS NOT. This script is disposable -- its
fingerprint describes a tree that stops existing the moment it succeeds,
so a second run aborts and writes nothing. The ledger text it installs
is permanent.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written either way. Undo is Discard Changes in GitHub Desktop.
"""

import hashlib
import os
import sys

TARGET = "LEDGER_CONSOLIDATED.md"

# Content fingerprint of everything OUTSIDE the generated INDEX zone.
# The zone is rewritten by ledger_index.py, which this patch's own steps
# tell Tony to run, so fingerprinting it would refuse for a reason that
# is not about content (safe-file-editing, A Guard Must Not Fence What a
# Generator Rewrites).
BASE_FP = "1621907bdb06396aae36bfa52f5a3817"

INDEX_START = b"<!-- INDEX:START"
INDEX_END = b"<!-- INDEX:END -->"


def fail(msg):
    print(msg)
    print("NOTHING was written. Undo is Discard Changes in GitHub Desktop.")
    sys.exit(1)


def content_fingerprint(raw):
    lf = raw.replace(b"\r\n", b"\n")
    try:
        a = lf.index(INDEX_START)
        b = lf.index(INDEX_END) + len(INDEX_END)
    except ValueError:
        fail("ERROR: the INDEX:START / INDEX:END markers are not in "
             + TARGET + ".")
    return hashlib.md5(lf[:a] + lf[b:]).hexdigest()


# ---------------------------------------------------------------- edits
# Each entry is (label, old_bytes, new_bytes). Every old must match
# EXACTLY ONCE. Anchors are written LF and translated to the file's own
# convention below.

EDITS = []

# -- L-340 -------------------------------------------------------------

EDITS.append((
    "L-340  the three findings recorded as fixed, the config exception, "
    "and the arrival check",
    b"""- **AND THE MODE 5 PASS ITSELF**, which is the point of this item. Tony
""",
    b"""- **ALL THREE ARE FIXED**, by `patch_L340_1_editor_polish_20260919.py`
  at gallery `2ebd001f`, and two of the three were bigger than the
  screenshot suggested. The shell list now sizes itself to the room it is
  showing, between 24 and 58 characters: the longest Earth label is 54,
  "Exosphere / Geocorona (hydrogen halo, detected extent)", not the 36
  the Sun's room showed. The `source` field is a wrapped box like
  `description` and `about`, because the longest served citation is 489
  characters against a 54-character line. And the Sun's arrival block
  lost its `moon` key, while the window now draws the tick only where the
  key exists -- so it can never again offer a control with nowhere to
  save it. [verified @ gallery `2ebd001f`]
- **THAT PATCH WROTE `data/objects_config.json` DIRECTLY, AND THAT IS AN
  EXCEPTION WORTH NAMING.** interactive-exhibit 1.4 says two tools write
  that file: the mirror writes the numbers from the orrery's export, the
  store writer writes the words and the arrival settings. Neither can do
  this one. The writer replaces a value and cannot REMOVE a key, and it
  should not learn how for a single correction. So a one-off correction
  patch wrote the file and named itself the exception in its own
  description. **Owed to interactive-exhibit's next bump:** a one-off
  correction patch may write the file where the writer cannot express the
  change, and it says so in its own description.
  **Tony-action (decide):** whether that exception stays narrow in those
  words. Claude Fable 5.1's view, 2026-09-19, is that it should -- a
  deletion is rare enough that teaching the writer to delete buys less
  than the new ways it could go wrong.
- **THIS RECORD WAS MISSING UNTIL 2026-09-19, AND THE REASON IS TIMING.**
  `documentation/HANDOFF_L334_editor_built_20260919.md` states the
  exception is recorded on this item, and
  `documentation/BUILD_MANIFEST_L322_earth_slice_20260919.md` copied that
  and asked its builder to confirm it and add nothing. It was not here.
  The orrery ledger went out at `bb614c7f` at 22:07 on 2026-09-18 and the
  gallery patch at `2ebd001f` at 22:22, and no ledger patch followed.
  Fable's own words on finding it, 2026-09-19: "I trusted a handoff's
  claim over the file itself." A handoff is a claim; the file is the
  fact, and this is the same failure class the protocol names.
- **A FOURTH FINDING, NOT FROM THE SCREENSHOT**, from Claude Fable 5.1's
  review of 2026-09-19 and reproduced on a throwaway copy of gallery
  `2ebd001f`. `documentation/smoke_arrival.js` compares each room's
  opening against a list written into the check itself -- `EXPECTED`,
  keyed by slug and holding DISPLAY NAMES: "Sun: Photosphere" for the
  Sun, and four names for Earth including "Earth: Crust". So ticking
  another shell to open drawn in the editor, or renaming "Crust" or
  "Photosphere", turns the Arrival check red for a change that is
  correct. A cache build does not clear it and the editor does not
  explain it. The fix: the check reads what it expects from the config's
  own arrival block, BY KEY. Recorded, not built.
- **AND THE MODE 5 PASS ITSELF**, which is the point of this item. Tony
"""))

# -- L-337 -------------------------------------------------------------

EDITS.append((
    "L-340  the RICE note says what the score now covers",
    b"""  walks every row; the Mode 5 pass is Tony's time rather than build
  time.
""",
    b"""  walks every row; the Mode 5 pass is Tony's time rather than build
  time. (2026-09-19: the three layout items are now DONE, so what this
  score covers is the Mode 5 pass and the fourth finding above.
  Unratified either way.)
"""))

EDITS.append((
    "L-337  upd date moves to 2026-09-19",
    b"<!-- L:337 status:OPEN upd:2026-09-17 section:A flag: rice:3/2/60/2 -->",
    b"<!-- L:337 status:OPEN upd:2026-09-19 section:A flag: rice:3/2/60/2 -->"))

EDITS.append((
    "L-337  Tony's addition of 2026-09-19, in his words",
    b"""- **Recorded, not built.** L-334's build contract puts it out of scope
  for that build (its section 7).
""",
    b"""- **Recorded, not built.** L-334's build contract puts it out of scope
  for that build (its section 7).
- **Tony added to this on 2026-09-19,** and his words settle what the
  marker IS. Quoted as he typed them;
  `documentation/HANDOFF_L334_editor_built_20260919.md` asked the next
  ledger patch to carry this and transcribes the inner quotes as single:

      while it is not a shell or a tick, the "sun" object is useful for
      centering the scene nominally. the earth should have one too in
      case we wish to display no shells. this is an option in the
      orrery.

  And, confirming it the same day for this record, where the orrery
  already draws one:

      the orrery has this too. each object has a symbol, a circle for
      the sun and planets, without any dimension whether or not it has
      any shells. most objects have no drawn shells.

  So the marker is a CENTRING object: a symbol at the body's position
  carrying no dimension, drawn whether or not the body has shells, and
  most objects have none. It is not a shell and it is not a drawer tick.
  The orrery's own per-object symbol is the worked example, which is
  where to look for the shape of the answer.
"""))

EDITS.append((
    "L-337  the bullet that said nobody had looked is corrected",
    b"""- **What a build would have to settle first.** What the marker IS -- the
  Sun's centre object may already be that thing, or may be a shell like
  any other, and nobody has looked. Where it comes from: drawn by the
  renderer from the served record, or a served feature in its own right.
  What it says on hover, under the exhibit's provenance contract, since a
  marker at the centre of a body is a natural place to put the body's own
  numbers and those numbers have to be served with their source.
""",
    b"""- **What a build would have to settle first.** What the marker IS is
  ANSWERED as of 2026-09-19, by Tony above: a dimensionless centring
  symbol, not a shell. (Until his answer this bullet read "the Sun's
  centre object may already be that thing, or may be a shell like any
  other, and nobody has looked" -- kept here so the correction is
  visible rather than silent.) STILL OPEN: where it comes from -- drawn
  by the renderer from the served record, or a served feature in its own
  right. And what it says on hover, under the exhibit's provenance
  contract, since a marker at the centre of a body is a natural place to
  put the body's own numbers and those numbers have to be served with
  their source.
"""))

EDITS.append((
    "L-337  the RICE note's reason for Confidence 60 is corrected",
    b"""  room without it is complete, not broken; Confidence 60 because nothing
  above is settled; Effort 2.
""",
    b"""  room without it is complete, not broken; Confidence 60 because nothing
  above was settled when it was scored; Effort 2. Tony's answer of
  2026-09-19 settles what the marker is, which argues Confidence up; the
  score is unratified either way.
"""))

# -- L-249 -------------------------------------------------------------

EDITS.append((
    "L-249  status DONE, upd date moves",
    b"<!-- L:249 status:OPEN upd:2026-08-25 section:A flag: rice:4/4/90/2 -->",
    b"<!-- L:249 status:DONE upd:2026-09-19 section:A flag: rice:4/4/90/2 -->"))

EDITS.append((
    "L-249  a dated record of what was built, measured at 189c2987",
    b"""**Gap:** blocked on `patch_L248_1`, confirmed 2026-08-25 and unbuilt.
That script clears three things: `constants_change_report.py`'s failure
on `NAME = EXPR` lines referencing other tracked names, the `4.74`
literal at `exoplanet_coordinates.py` line 373, and explicitly NOT
`3.26156` (L-248). The derived lines this item adds are precisely the
shape that gate cannot read, so building this first would trip it.
""",
    b"""- **BUILT 2026-08-26, AND THIS ROW DID NOT SAY SO UNTIL 2026-09-19.**
  Measured at orrery `189c2987` rather than carried from a handoff. The
  four interior boundaries are in `constants_new.py` with their own
  `# Source:` lines: `EARTH_INNER_CORE_KM` 1221.5 and
  `EARTH_OUTER_CORE_KM` to PREM (Dziewonski and Anderson 1981),
  `EARTH_D660_DEPTH_KM` 660.0 to the 660-km seismic discontinuity, and
  `EARTH_UPPER_MANTLE_KM` 6346.6 to PREM's Mohorovicic discontinuity.
  `shell_configs.py`'s Earth block takes all four `radius_fraction`
  values from the matching `_RADII` expressions rather than from typed
  decimals, so the drawing and the hover read from one place and cannot
  disagree -- which is what this item was for. The five `patch_L249_*`
  scripts and
  `HANDOFF_20260826_L249_earth_interior_and_the_road_to_artifact_1.md`
  are filed in `documentation/`. [verified @189c2987]
- **THE BLOCKER CLEARED.**
  `patch_L248_1_constants_gate_and_au_yr.py` is filed in
  `documentation/`, so the gate this item waited on was built.
- **THE MANTLE DISAGREEMENT THE NOTE BELOW LEFT OPEN IS SETTLED IN THE
  CODE**, and settled the way that Note asked -- by derivation rather
  than by keeping two numbers that can drift apart.
  `EARTH_LOWER_MANTLE_KM` is `EARTH_MEAN_RADIUS_KM -
  EARTH_D660_DEPTH_KM`, carrying a `# Derived:` line saying that a
  subtraction is governed by decimal places and not by significant
  figures. `EARTH_UPPER_MANTLE_KM` is PREM's 6346.6 rather than a 30 km
  depth read off prose.
**Gap:** none -- move to section C. ONE LIVE RESIDUE, re-homed by name
rather than left inside a closed item: the cross-check owed on
`EARTH_D660_DEPTH_KM`. L-253 holds it (the +/-60 km lateral variation
and the depression to roughly 750 km under cold slabs, both held
unsourced), and L-322's Earth slice visits that row again when it
declares its figures and its read line.
**Gap (as it stood 2026-08-25, DISCHARGED):** blocked on
`patch_L248_1`, confirmed 2026-08-25 and unbuilt.
That script clears three things: `constants_change_report.py`'s failure
on `NAME = EXPR` lines referencing other tracked names, the `4.74`
literal at `exoplanet_coordinates.py` line 373, and explicitly NOT
`3.26156` (L-248). The derived lines this item adds are precisely the
shape that gate cannot read, so building this first would trip it.
"""))

EDITS.append((
    "L-249  the Note's 'unresolved' label is no longer true",
    b"- **Note (measured while writing this row; unresolved).** The two\n",
    b"""- **Note (measured while writing this row; it read "unresolved" until
  2026-09-19, and was in fact SETTLED on 2026-08-26 -- see the built
  record above).** The two
"""))

EDITS.append((
    "L-249  the spent Tony-action is struck with the reason",
    b"""- **Note:** RICE 4/4/90/2 -> 7.2 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
""",
    b"""- **Note:** RICE 4/4/90/2 -> 7.2 was Claude's proposed score. The
  **Tony-action (decide)** that stood here -- confirm or redirect that
  score -- is STRUCK on 2026-09-19 with the reason: the work is built
  and the item is closed, so there is no longer anything to prioritise.
"""))

# -- L-322 -------------------------------------------------------------

EDITS.append((
    "L-322  upd date moves to 2026-09-19",
    b"<!-- L:322 status:OPEN upd:2026-09-17 section:A flag: rice:4/5/70/6 -->",
    b"<!-- L:322 status:OPEN upd:2026-09-19 section:A flag: rice:4/5/70/6 -->"))

EDITS.append((
    "L-322  the new current Gap, and the 2026-09-16 Gap relabelled",
    b"""**Gap (current, 2026-09-16, after the orrery half of the build):** three
things remain, in this order, and none awaits a ruling.""",
    b"""**Gap (current, 2026-09-19):** the EARTH SLICE, contracted by
`documentation/BUILD_MANIFEST_L322_earth_slice_20260919.md` (written on
orrery `bb614c7f` and gallery `2ebd001f`; filed at `189c2987`). Four
stages. A: this ledger patch. B: provenance-discipline goes to 2.14 and
learns the `# Read:` field BEFORE the walk, with Tony approving its
wording, and the session ends there because a reinstall cannot be
verified from inside the session that makes it. C: the walk, in two
pushes -- first the 29 Earth rows carrying no fields at all, plus
`KM_PER_AU` and `GM_SUN_SI` which feed the Hill sphere and belong to no
body's slice; then the 28 magnetosphere rows, where the five
`dimensionless` tokens become real ones and the two standoffs revert to
expressions and leave `constants_rows.TRANSITIONAL`, ending with
`constants_rows.CLOSED_SLICES` set to ("EARTH",). D: Earth's pole moves
out of `idealized_orbits.py` into the store, its own push, because it
draws a closed room's axis. MEASURED at `bb614c7f` and unchanged at
`189c2987`: the store holds 112 top-level rows, 57 of them Earth's; unit
and status are on 28 of those 57; figures and read are on 0 of all 112.
On the gallery side, the config makes 70 links to store rows and 53 of
them still go through the older drift check, 24 of those Earth's.
**Gap (2026-09-16, after the orrery half of the build; SUPERSEDED by
the 2026-09-19 Gap above, which carries (2) and (3) -- (1) is DONE and
deployed, see the 2026-09-17 note below):** three
things remain, in this order, and none awaits a ruling."""))

EDITS.append((
    "L-322  Tony's ruling of 2026-09-19 on what 'critical' means",
    b"""**Ref:** L-305, L-306 (approximations are not promoted), L-314,
`constants_new.py`, `provenance_scanner.py`, `orrery_maintenance_run.py`,""",
    b"""**Tony's ruling, 2026-09-19 -- what "critical" means in ruling (b).**
The 2026-09-11 scope said a typed-in number gets read against its source
"where critical", and that word was never defined. Asked on 2026-09-19,
his answer:

      what I meant by critical is where your own search tools cannot
      read a needed source but I can.

So the word is about ACCESS, not importance, and it splits three ways.
Where the builder can open the source, the builder reads it against the
row and the row's `# Read:` line names the model. Where the builder
cannot open it and Tony can, the row goes on a reading list for him, and
that list is his whole share of the reading. Where neither can open it,
the citation fails provenance-discipline's Access Standard: re-home it to
an open authority carrying the same value, or remove the claim and note
the gap. The SCOPE of rows needing a read at all is unchanged from ruling
(b): a measured row whose value is drawn in a published exhibit, and any
row that feeds one. One caution rides with it -- a model's read counts
only if the source was actually OPENED, with the title as printed and the
table or page recorded. A read reconstructed from training is worse than
no read, because it stops the next reader from looking.
**Ref:** L-305, L-306 (approximations are not promoted), L-314,
`constants_new.py`, `provenance_scanner.py`, `orrery_maintenance_run.py`,"""))


def main():
    here = os.path.basename(os.path.abspath(os.getcwd()))
    if here == "documentation":
        fail("ERROR: this patch is being run from documentation/. Run it "
             "from the ORRERY repo ROOT (next to " + TARGET + "), then "
             "move it into documentation/ afterwards.")

    if not os.path.exists(TARGET):
        fail("ERROR: " + TARGET + " is not in this folder. Run this patch "
             "from the ORRERY repo ROOT.")

    with open(TARGET, "rb") as handle:
        raw = handle.read()

    got = content_fingerprint(raw)
    if got != BASE_FP:
        fail("ERROR: " + TARGET + " is not the file this patch was built "
             "against.\n"
             "  expected content fingerprint " + BASE_FP + "\n"
             "  found                        " + got + "\n"
             "  (Line endings are excluded, and so is the generated INDEX "
             "zone.)\n"
             "  If this patch already ran, that is the expected result: it "
             "is one-shot.")

    is_crlf = raw.count(b"\r\n") > 0
    content = raw

    for label, old, new in EDITS:
        if is_crlf:
            old = old.replace(b"\n", b"\r\n")
            new = new.replace(b"\n", b"\r\n")
        n = content.count(old)
        if n != 1:
            fail("ANCHOR FAIL: expected exactly 1 match, found %d -- %s\n"
                 "  anchor began: %r" % (n, label, old[:70]))
        content = content.replace(old, new)

    try:
        content.decode("ascii")
    except UnicodeDecodeError as exc:
        fail("ERROR: the result is not ASCII (%s). Nothing written." % exc)

    with open(TARGET, "wb") as handle:
        handle.write(content)

    for label, _old, _new in EDITS:
        print("  ok  " + label)
    print("")
    print("patch applied (%d bytes -> %d bytes, %s line endings kept)"
          % (len(raw), len(content), "CRLF" if is_crlf else "LF"))
    print("")
    print("NOW, in order:")
    print("  1. Run ledger_index.py (VS Code Run button, or")
    print("     python ledger_index.py) from this same folder.")
    print("")
    print("     EXPECT THE FIRST RUN TO REPORT TWO PROBLEMS AND FIX")
    print("     THEM. This patch closes L-249, and the indexer moves a")
    print("     closed block into section C by itself. It prints two")
    print("     [auto-fix] lines naming L-249, then says it retagged 1")
    print("     block and physically moved 1 block. That is the")
    print("     migration working, not a failure.")
    print("")
    print("  2. Run ledger_index.py a SECOND time. THIS is the run that")
    print("     must print OK. Expect:")
    print("       OK: 335 L-blocks parsed, no consistency problems.")
    print("       Index regenerated (192 live items) in ...")
    print("     192 rather than 193 because L-249 closed. If the second")
    print("     run still reports problems, stop and tell Claude.")
    print("  3. Move this script into documentation/.")
    print("  4. Run the orrery maintenance run.")
    print("  5. Commit and push, then tell Claude the new orrery SHA.")
    print("")
    print("Undo at any point is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
