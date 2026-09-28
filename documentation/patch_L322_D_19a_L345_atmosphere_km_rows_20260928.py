#!/usr/bin/env python3
"""
patch_L322_D_19a_L345_atmosphere_km_rows_20260928.py -- ORRERY repo.

L-345, patch D19a: the tops of the lower and upper atmosphere get
kilometre rows, so the gallery can point at them.

Built on orrery 807e9dd535211b2bdb91263b49988e1494c308a8
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 2df02f3baead894ff40922bcadef9cb84c49fa07
at https://github.com/tonylquintanilla/tonyquintanilla.github.io,
read only).
Rules: provenance-discipline 2.22, Rule 3 (a value in another unit is
computed, never stored); Tony's ruling of 2026-09-28 on the order:
this patch, then the gallery patch, then D20.

WHAT IT DOES

    constants_new.py gains two rows, each Earth's equatorial radius plus
    an altitude the store already holds:

        EARTH_STRATOPAUSE_RADIUS_KM   6428 km, 4 figures (50 km is good
                                      to the kilometre)
        EARTH_THERMOPAUSE_RADIUS_KM   6980 km, 3 figures (600 km is good
                                      to tens of kilometres)

    The export then serves each one's value in Earth radii and AU as
    "in": 1.0078 and 1.094 Earth radii. The gallery patch that follows
    moves the lower and upper atmosphere's pointers onto these rows.

    Nothing else changes. The two old rows, EARTH_STRATOPAUSE_RADII and
    EARTH_THERMOPAUSE_RADII, stay as they are until D20 turns them into
    conversions of the new rows. No orrery hover reads the new names.

    test_constants_export.py pins the two new values in Earth radii, so
    a change to the rule fails there by name (8 pins become 10).

    The ledger records the order on L-345, and the pre-build list of
    changed hovers is filed in documentation/.

FILES

    changed  constants_new.py, test_constants_export.py,
             LEDGER_CONSOLIDATED.md
    new      documentation/PREBUILD_L345_gallery_hover_changes_20260928.md

    Permanent: all of the above. This script is one-shot; file it in
    documentation/ once it has run.

    Generated afterwards by the maintenance run, not by this script:
    data/constants_export.json (91 rows exported, was 89) and the ledger
    index.

RUN COMMAND

    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code, and click Run.

        python patch_L322_D_19a_L345_atmosphere_km_rows_20260928.py

    Success: one "ok" line per edit, "PATCH APPLIED", then the next
    steps. Failure: "FAILURE: ..." and NOTHING is written; every file is
    checked before any is written. Undo after a success is Discard
    Changes in GitHub Desktop.

Written September 28, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# Fingerprints leave out the zones generators rewrite -- the ledger's
# INDEX and the protocol's SKILL-MANIFEST -- so running ledger_index.py
# is never a reason to refuse (safe-file-editing, A Guard Must Not Fence
# What a Generator Rewrites).
ZONES = [("<!-- INDEX:START", "<!-- INDEX:END -->"),
         ("<!-- SKILL-MANIFEST:START", "<!-- SKILL-MANIFEST:END -->")]

TARGETS = [('constants_new.py', 'a7c1252be902ee8094ebb9f0d95b1c65', [('two kilometre rows', 'EARTH_STRATOPAUSE_RADII = (EARTH_EQUATORIAL_RADIUS_KM', "EARTH_STRATOPAUSE_RADIUS_KM = EARTH_EQUATORIAL_RADIUS_KM + EARTH_STRATOPAUSE_ALTITUDE_KM\n# Derived: 6378.1366 + 50 = 6428 km from Earth's centre. A SUM is good\n# Derived+: to the coarsest decimal place among its measured inputs, and\n# Derived+: the 50 km altitude carries two figures, so the ones place.\n# Unit: km\n# Status: derived -- inherits EARTH_EQUATORIAL_RADIUS_KM,\n# Status+: EARTH_STRATOPAUSE_ALTITUDE_KM\n# Figures: 4 -- set by EARTH_STRATOPAUSE_ALTITUDE_KM (50, 2), good to the\n# Figures+: kilometre.\n# Note: the top of the lower atmosphere, measured from Earth's centre.\n# Note+: Its value in Earth radii and AU is computed from this row\n# Note+: (L-345); EARTH_STRATOPAUSE_RADII below becomes that conversion\n# Note+: at patch D20. Added at patch D19a.\nEARTH_THERMOPAUSE_RADIUS_KM = EARTH_EQUATORIAL_RADIUS_KM + EARTH_THERMOPAUSE_ALTITUDE_KM\n# Derived: 6378.1366 + 600 = 6980 km from Earth's centre. The 600 km\n# Derived+: altitude carries two figures, so the sum is good to tens.\n# Unit: km\n# Status: derived -- inherits EARTH_EQUATORIAL_RADIUS_KM,\n# Status+: EARTH_THERMOPAUSE_ALTITUDE_KM\n# Figures: 3 -- set by EARTH_THERMOPAUSE_ALTITUDE_KM (600, 2), good to\n# Figures+: tens of kilometres.\n# Note: the top of the upper atmosphere, measured from Earth's centre.\n# Note+: Its value in Earth radii and AU is computed from this row\n# Note+: (L-345); EARTH_THERMOPAUSE_RADII below becomes that conversion\n# Note+: at patch D20. Added at patch D19a.\nEARTH_STRATOPAUSE_RADII = (EARTH_EQUATORIAL_RADIUS_KM"), ('stamp', 'is typed with is Python\'s, not a figure (provenance-discipline 2.20,\nRule 2).)\n"""\n', 'is typed with is Python\'s, not a figure (provenance-discipline 2.20,\nRule 2).)\nModule updated: September 28, 2026 with Anthropic\'s Claude Opus 5.5\n(L-345, patch L322_D_19a: the tops of the lower and upper atmosphere\ngain kilometre rows, EARTH_STRATOPAUSE_RADIUS_KM (6428 km) and\nEARTH_THERMOPAUSE_RADIUS_KM (6980 km), each Earth\'s radius plus the\naltitude. The export works out their values in Earth radii and AU, so\nthe gallery can point at them; the two _RADII rows become conversions\nof them at D20.)\n"""\n')]), ('test_constants_export.py', '56334931b6d7020fab14ce470f060187', [('docstring: check 6 names the atmosphere cases', "       whose unit has none must not. Five worked cases of the count rule\n       (provenance-discipline 2.22, Rule 3) are pinned by value and\n       count, so a change to the rule fails here by name: the\n       chromosphere's top, the bow shock and magnetopause standoffs, the\n       LEO floor's print count, and one Earth radius in Earth radii.\n", "       whose unit has none must not. Six worked cases of the count rule\n       (provenance-discipline 2.22, Rule 3) are pinned by value and\n       count, so a change to the rule fails here by name: the\n       chromosphere's top, the bow shock and magnetopause standoffs, the\n       LEO floor's print count, one Earth radius in Earth radii, and the\n       tops of the lower and upper atmosphere in Earth radii.\n"), ('stamp', 'check 6 re-computes every served conversion and holds five worked cases\nof the count rule.)\n"""\n', 'check 6 re-computes every served conversion and holds five worked cases\nof the count rule.)\nModule updated: September 28, 2026 with Anthropic\'s Claude Opus 5.5\n(L-345, patch L322_D_19a: two more pins, the tops of the lower and\nupper atmosphere in Earth radii, 1.0078 at five figures and 1.094 at\nfour -- the numbers the gallery\'s two radius lines will print.)\n"""\n'), ('two pins', '    ("EARTH_EQUATORIAL_RADIUS_KM", "r_earth", 1.0, "exact", 1),\n)\n', '    ("EARTH_EQUATORIAL_RADIUS_KM", "r_earth", 1.0, "exact", 1),\n    # L-345, patch D19a: a sum good to the kilometre, and one good to\n    # tens of kilometres, each in Earth radii.\n    ("EARTH_STRATOPAUSE_RADIUS_KM", "r_earth", 1.0078, 5, None),\n    ("EARTH_THERMOPAUSE_RADIUS_KM", "r_earth", 1.094, 4, None),\n)\n')]), ('LEDGER_CONSOLIDATED.md', 'c12ad57378ca29dfc8a0942d818e6753', [('L-345: D19a and the order', '- **Still to build:** D20 retires the store\'s 13 conversion rows and\n  widens the figures checker; then one gallery patch prints from\n  `"in"`. The bow shock\'s hover then reads 86,000 km (0.00058 AU).\n', '- **Still to build:** D20 retires the store\'s 13 conversion rows and\n  widens the figures checker; then one gallery patch prints from\n  `"in"`. The bow shock\'s hover then reads 86,000 km (0.00058 AU).\n- **The order, Tony 2026-09-28 ("confirmed as recommended"):** patch\n  D19a, then the gallery patch, then D20. D19a only ADDS\n  `EARTH_STRATOPAUSE_RADIUS_KM` (6428 km) and\n  `EARTH_THERMOPAUSE_RADIUS_KM` (6980 km), so the gallery can move all\n  eleven of its conversion pointers in one patch and every visible\n  change reaches one phone check. Measured before building, the gallery\n  patch moves six hover lines beyond the handoff\'s seven: the\n  magnetotail\'s two km and AU figures, the inner belt\'s AU, the LEO\n  edges\' radii, and the two atmosphere radii (1.0078 and 1.094). All\n  six are the 2.22 rule; the list is\n  `documentation/PREBUILD_L345_gallery_hover_changes_20260928.md`.\n'), ('L-345 gap: the order', '**Gap (2026-09-28):** D20, then the gallery patch; closes when the gallery prints from `"in"`.\n', '**Gap (2026-09-28):** D19a, the gallery patch, then D20; closes when the gallery prints from `"in"` and D20 has landed.\n')])]

NEW_DOC = 'documentation/PREBUILD_L345_gallery_hover_changes_20260928.md'
NEW_DOC_TEXT = '# Pre-build note -- L-345 gallery patch: what a visitor will see change\n\n**Built on orrery `807e9dd535211b2bdb91263b49988e1494c308a8` at\nhttps://github.com/tonylquintanilla/palomas_orrery and gallery\n`2df02f3baead894ff40922bcadef9cb84c49fa07` at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io.** Both\nHEADs read live with `git ls-remote` on 2026-09-28. Loaded skills:\nprovenance-discipline 2.22, interactive-exhibit 1.5 (the handoff\'s\nobligation, discharged). Nothing has been built.\n\n**Type: PRE-BUILD NOTE.** The handoff asked for every changed hover,\ntoday and after, before building. This is that list, measured, and it\nis longer than the handoff expected.\n\n## 1. How it was measured\n\n- Today\'s hovers: built headless from gallery `2df02f3b`\'s served cache\n  with the page\'s own renderer.\n- After: each printed kilometre, AU or radii number read from the `"in"`\n  entry the orrery\'s export at `807e9dd5` serves for that row, as\n  interactive-exhibit 1.5 requires ("a hover prints a unit it is\n  served"). Kilometres at the served count; AU at the served count or\n  three figures, whichever is fewer (Rule 7\'s named AU exception).\n- Rows D20 has not built yet (the stratopause and thermopause kilometre\n  rows) are worked out by provenance-discipline 2.22 Rule 3 and marked\n  "expected". They are confirmed when those rows exist.\n\n## 2. The list\n\n| Room | Hover | Today | After | Why |\n|---|---|---|---|---|\n| Earth | Crust | Radius: 1.0000 Earth radii | Radius: 1 Earth radius | patch 4 |\n| Earth | Magnetopause | Bz 0.0 nT, dynamic pressure 2.0 nPa | Bz 0 nT, dynamic pressure 2 nPa | patch 4 |\n| Earth | Bow shock | at dynamic pressure 2.0 nPa | at dynamic pressure 2 nPa | patch 4 |\n| Earth | Bow shock | 86,200 km (0.000576 AU) | 86,000 km (0.00058 AU) | L-345 ruling |\n| Sun | Chromosphere | Radius: 1.002874802357338 solar radii | Radius: 1.003 solar radii | L-345 |\n| Sun | Chromosphere | = 697,700 km (0.00466 AU) | = 698,000 km (0.00466 AU) | L-345 |\n| Sun | Photosphere | Radius: 1 solar radii | Radius: 1 solar radius | singular at 1 |\n| Earth | Magnetotail | 770,000 km (0.0051 AU) | 800,000 km (0.005 AU) | NEW, see 3 |\n| Earth | Magnetotail | 380,000 km (0.0026 AU) | 400,000 km (0.003 AU) | NEW, see 3 |\n| Earth | Inner radiation belt | = 9,600 km (0.000064 AU) | = 9,600 km (0.00006 AU) | NEW, see 3 |\n| Earth | LEO inner edge | Radius: 1.0313571 Earth radii | Radius: 1.03135712 Earth radii | NEW, see 3 |\n| Earth | LEO outer edge | Radius: 1.3135712 Earth radii | Radius: 1.31357121 Earth radii | NEW, see 3 |\n| Earth | Lower atmosphere | Radius: 1.008 Earth radii | Radius: 1.0078 Earth radii (expected) | NEW, see 3 |\n| Earth | Upper atmosphere | Radius: 1.09 Earth radii | Radius: 1.094 Earth radii (expected) | NEW, see 3 |\n\nEvery other Earth and Sun hover line holds byte for byte: the interior,\nthe geocorona, geostationary, the Hill sphere, the outer belt, the\nmagnetopause\'s 65,000 km (0.00044 AU), every altitude line, and every\nSun shell outside the chromosphere and photosphere.\n\n## 3. Why the six new rows move\n\nAll six are the 2.22 rule doing what the ruling says it does ("the\nexception cuts both ways"), in places the design did not examine.\n\n- **Magnetotail and inner belt.** Their hovers multiply a served\n  Earth-radii number by Earth\'s radius to print kilometres\n  (`feature_renderers.js` lines 1143 and 2407). That is the conversion\n  interactive-exhibit 1.5 forbids. Read from `"in"` instead, they take\n  the count their source rows support. The tail\'s 120 Earth radii\n  carries a stated plus or minus 10, which is about 64,000 km, so its\n  kilometre figure keeps one figure.\n- **LEO edges.** The pointer moves from the Earth-radii conversion row\n  (8 figures) to the kilometre row, and the kilometre row\'s value in\n  Earth radii carries 9. The ruling\'s table already said 9 ("Inherit").\n- **Stratopause and thermopause.** Their radii become conversions of\n  kilometre sums at D20. 50 km is good to the kilometre and 600 km to\n  ten kilometres, so the radii keep ten-thousandths and thousandths,\n  as the chromosphere\'s did.\n\n## 4. The ordering question, with a recommendation\n\nThe stratopause and thermopause have no kilometre row until D20, so\ntheir two gallery pointers cannot move yet. Two ways:\n\n- **A.** Gallery patch now with 9 pointers; D20; a second small gallery\n  patch for the last 2. Two phone checks, and between D20\'s push and\n  the second gallery patch the two links point at rows the export no\n  longer serves.\n- **B (recommended).** A small orrery patch first that only ADDS the\n  two kilometre rows; then the gallery patch with all 11 pointers; then\n  D20 retires the old rows. One phone check covers every change above,\n  and no check sits failing between pushes. Cost: one extra orrery\n  commit and push before the gallery work.\n\n## 5. A second question, after the first: the three-figure AU line\n\nRule 7 lets the AU line print three figures when the served count is\nlonger. With `"in"`, the page would do that by rounding a served value\nthat is already rounded, which is the rounded intermediate Rule 4\nforbids. It can round a tie the wrong way. It already meets one: the\ninner core\'s AU is served as 0.000008165 (four figures); the true value\n0.0000081652 rounds to 0.00000817, and the page also prints 0.00000817,\nbut only because of how the computer stores 8.165 in binary. Today\nnothing would catch it going the other way.\n\nThis does not change any line in section 2 today. It needs settling\nbefore the build writes the AU code, and it comes after the ordering\nquestion.\n\n---\n\nWritten September 28, 2026 with Anthropic\'s Claude Opus 5.5.\n'
NEW_DOC_MD5 = 'e6b587b93242d6f2c171cbd639233b95'

NEXT_STEPS = """
NEXT STEPS, in this order:

  1. (do) Run the orrery maintenance run (orrery_maintenance_run.py).
     It rewrites data/constants_export.json with the two new rows.
     Expect 19 of 20 checkers passing, as before. "Constants export
     check" should end "... 220 conversions re-computed, 10 of 10 worked
     cases hold." "Derived figures" should say 44 derived rows read, 32
     OK. The one failure is still "Exact rows by the count", naming the
     Earth room's eleven lines; the gallery patch clears it.
  2. (do) Move this script into documentation/. Commit everything and
     push.
  3. Tell Claude the new orrery SHA. The gallery patch is built next,
     against it.
"""


def strip_zones(text):
    for start, end in ZONES:
        if start in text and end in text:
            a = text.index(start)
            b = text.index(end) + len(end)
            text = text[:a] + text[b:]
    return text


def fingerprint(data):
    text = data.replace(b"\r\n", b"\n").decode("utf-8")
    return hashlib.md5(strip_zones(text).encode("utf-8")).hexdigest()


def fail(msg):
    print("FAILURE: " + msg)
    print("NOTHING was written. Undo is not needed.")
    sys.exit(1)


def main():
    if os.path.basename(os.getcwd()) == "documentation" or \
            os.path.basename(HERE) == "documentation":
        fail("this is running from documentation/. Run it from the orrery "
             "repo root, then file it in documentation/.")
    if not os.path.exists(os.path.join(HERE, "constants_new.py")):
        fail("constants_new.py is not beside this script. Save it in the "
             "ORRERY repo root, not the gallery.")
    results = []
    for rel, fp, edits in TARGETS:
        path = os.path.join(HERE, rel)
        if not os.path.exists(path):
            fail("%s not found" % rel)
        with open(path, "rb") as handle:
            raw = handle.read()
        got = fingerprint(raw)
        if got != fp:
            fail("%s is not the file this patch was built on (fingerprint "
                 "%s, expected %s). Pull or discard local changes first."
                 % (rel, got, fp))
        crlf = b"\r\n" in raw
        text = raw.replace(b"\r\n", b"\n").decode("utf-8")
        for label, old, new in edits:
            n = text.count(old)
            if n != 1:
                fail('%s: "%s" -- expected 1 match, got %d' % (rel, label, n))
            text = text.replace(old, new)
            print("ok    %s: %s" % (rel, label))
        data = text.encode("utf-8")
        try:
            data.decode("ascii")
        except UnicodeDecodeError as exc:
            fail("%s would not be ASCII after the patch (%s)" % (rel, exc))
        if crlf:
            data = data.replace(b"\n", b"\r\n")
        results.append((path, data))
    doc = NEW_DOC_TEXT.encode("ascii")
    if hashlib.md5(doc).hexdigest() != NEW_DOC_MD5:
        fail("the embedded document does not match its checksum")
    doc_path = os.path.join(HERE, NEW_DOC)
    write_doc = True
    if os.path.exists(doc_path):
        with open(doc_path, "rb") as handle:
            held = handle.read().replace(b"\r\n", b"\n")
        if held != doc:
            fail("%s already exists and differs from this patch's copy"
                 % NEW_DOC)
        write_doc = False
        print("ok    %s: already filed, identical" % NEW_DOC)
    else:
        print("ok    %s: new, %d bytes" % (NEW_DOC, len(doc)))
    for path, data in results:
        with open(path, "wb") as handle:
            handle.write(data)
    if write_doc:
        with open(doc_path, "wb") as handle:
            handle.write(doc)
    print("stamp constants_new.py, test_constants_export.py: updated "
          "September 28, 2026 (patch D19a)")
    print("PATCH APPLIED: %d files changed, %d new."
          % (len(results), 1 if write_doc else 0))
    print(NEXT_STEPS)


if __name__ == "__main__":
    main()
