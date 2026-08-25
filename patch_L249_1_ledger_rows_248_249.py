"""
patch_L249_1_ledger_rows_248_249.py -- write L-248 and L-249 into the ledger.

Run:  save into the repo root (the folder holding LEDGER_CONSOLIDATED.md),
      open in VS Code, click Run.  Or:  python patch_L249_1_ledger_rows_248_249.py

Built on 2bf0d06a -> cf865ffc12862eeaeee5c0d7b1a2627dc003d4bd
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT IT DOES
  1. Inserts the [L-248] and [L-249] detail blocks at the end of
     section A, immediately after [L-247] and before
     "## PENDING ACTION (Tony-side)".
  2. Fix in passing: restores the blank line before
     "## D. RECONCILED LEDGER -- OPEN", which patch_L250_1 removed when
     it appended L-250's block to the end of section C.

WHAT IS PERMANENT
  The two ledger rows.  The script is one-shot: it guards on a
  fingerprint of a tree that stops existing the moment it succeeds.

AFTER THIS RUN, in order:
  1. python ledger_index.py      (regenerates the INDEX zone)
  2. python maintenance_run.py

Success: one "ok" line per edit, then "patch applied".
Failure: a single "ERROR:" or "ANCHOR FAIL" line; nothing is written.
"""

import hashlib
import os
import sys

TARGET = "LEDGER_CONSOLIDATED.md"

# md5 of the content with CRLF normalized to LF -- line endings are not
# content (safe-file-editing 1.8).  The repo blob is LF; Tony's working
# copy is CRLF.  Both give this fingerprint.
BASE_FP = "4ca719021750915135f74bde35360967"

# ----------------------------------------------------------------------
# Edit 1 -- the two new rows, inserted before the PENDING ACTION heading.
# ----------------------------------------------------------------------

ANCHOR_1_OLD = b"""L-246 (S4714); No Shadow Constants [CRITICAL].

## PENDING ACTION (Tony-side)
"""

NEW_ROWS = b"""L-246 (S4714); No Shadow Constants [CRITICAL].

#### [L-248] The parsec-to-light-year factor is typed 36 times across the star pipeline
<!-- L:248 status:OPEN upd:2026-08-25 section:A flag: rice:3/3/85/3 -->
- **The same class as L-243 and a good deal larger.** The value is
  correct at every site; there are simply 36 of it, across 11 modules.
  The whole star pipeline types the parsec-to-light-year conversion by
  hand.
- **Measured at `cf865ffc`** by counting occurrences of the literal
  `3.26156` in tracked `.py` files outside `documentation/`:
  `messier_object_data_handler` 9, `incremental_cache_manager` 8,
  `exoplanet_coordinates` 3, `data_acquisition_distance` 3,
  `vot_cache_manager` 2, `visualization_3d` 2, `star_visualization_gui`
  2, `simbad_manager` 2, `data_processing` 2, `data_acquisition` 2,
  `visualization_2d` 1.
- **It needs no new constant.** Light-years per parsec is
  `PARSEC_TO_AU / AU_PER_LIGHT_YEAR`, both already in
  `constants_new.py`. With `PARSEC_TO_AU = 206265.0` (line 1018) and
  `AU_PER_LIGHT_YEAR` derived at line 125, the quotient is 3.2615668.
  The literal 3.26156 agrees to a relative 2.1e-06.
- **Recommended as the first Fable sweep**, on L-244's route.
  Mechanical, and the answer is a list rather than a judgment.
- **Six of the eleven modules are CRLF in the repo blob** --
  `messier_object_data_handler`, `data_acquisition_distance`,
  `visualization_3d`, `data_processing`, `data_acquisition` and
  `visualization_2d` -- so the sweeping patch must translate its
  anchors per safe-file-editing, Line Endings Are Not Content.
- **Deliberately NOT folded into `patch_L248_1`.** That script is named
  for this handle and carries none of this sweep; what it does is clear
  the constants-change gate so L-249 can land. Sweeping 3 of 36 sites
  because one file happened to be open would leave 33 shadows and a
  half-migrated constant, which is worse than not starting.
**Gap:** the sweep itself. Dispatch first, then patch -- detecting line
endings per file rather than assuming the repo's LF.
- **Note (correction to the source handoff).** Step 1 of
  `HANDOFF_20260825_evening_singularity_thread.md` states 38 sites and
  an exact quotient of 3.2615675. Both are superseded by the
  measurement above. The handoff is left unedited, being a session
  record; the correction lives here. The 38 is most probably 36 live
  sites plus two spent patch scripts in `documentation/` that quote the
  literal in their own text.
- **Note:** RICE 3/3/85/3 is Claude's proposed score, which the index
  renders as 2.5. **Tony-action (decide):** confirm or redirect, and
  whether Fable carries it.
**Ref:** L-243 (the AU factor -- the narrow precedent); L-244 (the
class, and the route); L-250 and PROJECT_INSTRUCTIONS Part 3, The
Braid; `constants_new.py` lines 104, 125, 1018.

#### [L-249] The Earth slice of L-181: interior boundaries as sourced constants
<!-- L:249 status:OPEN upd:2026-08-25 section:A flag: rice:4/4/90/2 -->
- **Confirmed by Tony on 2026-08-25 and then dropped.** The
  conversation moved to conversion factors and never came back, so it
  was agreed aloud and written down nowhere -- the same failure class
  the rest of that day was spent on. This row is the capture.
- **The shape.** Earth's interior boundary radii move into
  `constants_new.py` in km with their sources, and `shell_configs.py`
  derives its `radius_fraction` from them, following
  `CHROMOSPHERE_PHYSICAL_RADII`'s existing pattern:

      EARTH_INNER_CORE_KM    = <km>   # Source: ...
      EARTH_INNER_CORE_RADII = EARTH_INNER_CORE_KM / EARTH_EQUATORIAL_RADIUS_KM

- **What it fixes, measured at `cf865ffc`.** `shell_configs.py` stores
  `radius_fraction: 0.19` for the inner core while the hover prose
  beside it reads 1,220 km. Those disagree: 0.19 x 6378.1366 draws a
  sphere at 1,211.8 km, and 1,220 km would be a fraction of 0.19128.
  The outer core has the same shape -- 0.55 draws 3,508.0 km against a
  stated 3,500, which is 0.54875. Two copies of one number with nothing
  holding them together. Afterwards the drawing and the hover read from
  one place and cannot disagree.
- **It splits correctly for the scanner without anyone arranging it**
  (L-240): the km literal is scored, the fraction is a formula.
  Measured and declared fall out of the shape rather than being imposed
  on it.
- **What comes with it.** The km figures are round numbers in prose
  today, under a block-level `# Source:` header at `shell_configs.py`
  line 1316 naming USGS Interior of the Earth, the NASA Earth Fact
  Sheet, NOAA/NCEI, NASA Goddard, the NASA Van Allen Probes and NASA
  Solar System Dynamics, stamped "Verified: April 2026 provenance
  audit". Lifting each value gives it its OWN `# Source:` line, which
  then has to be true of that value specifically -- something a block
  header covering six sources and nine shells does not establish. That
  is the Earth slice of the verification loop, and by the 2026-08-22
  braid ruling it runs before Artifact 1 re-locks, not before the
  render.
**Gap:** blocked on `patch_L248_1`, confirmed 2026-08-25 and unbuilt.
That script clears three things: `constants_change_report.py`'s failure
on `NAME = EXPR` lines referencing other tracked names, the `4.74`
literal at `exoplanet_coordinates.py` line 373, and explicitly NOT
`3.26156` (L-248). The derived lines this item adds are precisely the
shape that gate cannot read, so building this first would trip it.
- **Note (measured while writing this row; unresolved).** The two
  mantle shells disagree with their own prose by far more than the
  cores do, and whether that is drift or a declared drawing choice
  under L-240 is not established either way. `lower_mantle` stores
  0.85, drawing 5,421 km, while its hover puts that boundary 660 km
  below the surface, which is 5,718 km or 0.8965. `upper_mantle` stores
  0.98, drawing 6,251 km, against a stated 30 km depth, which is 6,348
  km or 0.9953. Settle which of the two before the migration rather
  than during it: a derivation would silently move both spheres.
- **Note:** RICE 4/4/90/2 -> 7.2 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** L-181 (the parent); L-240 (measured vs declared); L-234 (the
Earth half of Artifact 1); `shell_configs.py` Earth block, lines
1316-1512; `constants_new.py` line 74 (`EARTH_EQUATORIAL_RADIUS_KM`);
`HANDOFF_20260825_evening_singularity_thread.md` step 2.

## PENDING ACTION (Tony-side)
"""

# ----------------------------------------------------------------------
# Edit 2 -- fix in passing: blank line before the section D heading.
# ----------------------------------------------------------------------

ANCHOR_2_OLD = b"""the Audit.
## D. RECONCILED LEDGER -- OPEN
"""

ANCHOR_2_NEW = b"""the Audit.

## D. RECONCILED LEDGER -- OPEN
"""

EDITS = [
    (ANCHOR_1_OLD, NEW_ROWS, "insert [L-248] and [L-249] at the end of section A"),
    (ANCHOR_2_OLD, ANCHOR_2_NEW, "fix in passing: blank line before section D heading"),
]


def fail(msg):
    print("ERROR: " + msg)
    sys.exit(1)


def main():
    if not os.path.exists(TARGET):
        fail("%s not found. Run this from the folder that holds it." % TARGET)

    with open(TARGET, "rb") as f:
        data = f.read()

    is_crlf = data.count(b"\r\n") > 0
    norm = data.replace(b"\r\n", b"\n")
    fp = hashlib.md5(norm).hexdigest()

    if fp != BASE_FP:
        print("ERROR: BASE MOVED.")
        print("  expected content fingerprint %s" % BASE_FP)
        print("  found                        %s" % fp)
        print("  (line endings are normalized before hashing, so this is a")
        print("   content difference, not a CRLF/LF difference)")
        sys.exit(1)

    print("base ok  %-38s (%s)  %d bytes" % (TARGET, "CRLF" if is_crlf else "LF", len(data)))

    # Nothing may already be there.
    for token in (b"[L-248]", b"[L-249]", b"L:248", b"L:249"):
        if token in norm:
            fail("%r already present -- this patch has already run." % token)

    # ASCII gate on every byte this patch inserts (Encoding Gate,
    # safe-file-editing 1.8: prose is in scope, not only code).
    inserted = NEW_ROWS + ANCHOR_2_NEW
    bad = sorted({b for b in inserted if b > 127})
    if bad:
        fail("non-ASCII byte(s) in inserted text: %r" % bad)
    print("ok  encoding gate: inserted text is ASCII-only")

    # Report pre-existing non-ASCII rather than sweeping it: choosing a
    # replacement character is a reading of intent, not a mechanical fix.
    pre_existing = sum(1 for b in data if b > 127)
    print("ok  encoding scan: %d pre-existing non-ASCII byte(s) in %s"
          % (pre_existing, TARGET))

    # Freeze the generated INDEX zone -- this patch must not move it.
    start = norm.find(b"<!-- INDEX:START")
    end = norm.find(b"<!-- INDEX:END -->")
    if start < 0 or end < 0:
        fail("INDEX marker zone not found")
    index_before = norm[start:end]

    out = data
    for old, new, label in EDITS:
        o, n = old, new
        if is_crlf:
            o = o.replace(b"\n", b"\r\n")
            n = n.replace(b"\n", b"\r\n")
        count = out.count(o)
        if count != 1:
            print("ANCHOR FAIL (%d matches, expected 1): %s" % (count, label))
            print("  nothing written.")
            sys.exit(1)
        out = out.replace(o, n)
        print("ok  %s" % label)

    # Post-conditions, asserted before anything is written.
    out_norm = out.replace(b"\r\n", b"\n")
    for token, want in ((b"#### [L-248]", 1), (b"#### [L-249]", 1),
                        (b"<!-- L:248 ", 1), (b"<!-- L:249 ", 1),
                        (b"\n## PENDING ACTION (Tony-side)\n", 1)):
        got = out_norm.count(token)
        if got != want:
            fail("post-check: %r appears %d time(s), expected %d" % (token, got, want))
    print("ok  post-check: one header and one metadata line for each of L-248, L-249")

    s2 = out_norm.find(b"<!-- INDEX:START")
    e2 = out_norm.find(b"<!-- INDEX:END -->")
    if out_norm[s2:e2] != index_before:
        fail("post-check: the generated INDEX zone changed -- it must not")
    print("ok  post-check: generated INDEX zone byte-identical")

    if is_crlf and out.count(b"\n") != out.count(b"\r\n"):
        fail("post-check: mixed line endings introduced")
    print("ok  post-check: line endings preserved (%s)" % ("CRLF" if is_crlf else "LF"))

    with open(TARGET, "wb") as f:
        f.write(out)

    print("patch applied to %s  %+d bytes  (%s)"
          % (TARGET, len(out) - len(data), "CRLF" if is_crlf else "LF"))
    print("")
    print("CARRIED FORWARD -- corrections this row makes to a document that still")
    print("says otherwise (The Correction Does Not Travel):")
    print("  documentation/HANDOFF_20260825_evening_singularity_thread.md")
    print("    still reads '38 times' and 'exact quotient is 3.2615675'.")
    print("    L-248 now records 36 sites and 3.2615668. The handoff is a")
    print("    frozen session record and is deliberately NOT edited.")
    print("")
    print("NEXT, in order:")
    print("  1. python ledger_index.py")
    print("  2. python maintenance_run.py")


if __name__ == "__main__":
    main()
