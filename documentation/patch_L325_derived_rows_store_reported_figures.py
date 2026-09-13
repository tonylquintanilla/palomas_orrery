"""
patch_L325_derived_rows_store_reported_figures.py

Tony's ruling of 2026-09-12: a store carries the figures its sources
support, not the arithmetic result. This patch applies it to the only
two derived rows in the store, and installs the check that has to come
with it.

WHAT CHANGES (4 files)

  constants_new.py
    1. EARTH_MAGNETOPAUSE_STANDOFF_RADII: 10.251872972379905 -> 10.25.
    2. EARTH_BOW_SHOCK_STANDOFF_RADII: the expression -> 13.51.
       Both rows already declared REPORT 10.25 and REPORT 13.51, with
       the reason, so this stores what the rows already said to report.
       The arithmetic stays recorded in each Derived block.

  orrery_maintenance_run.py
    3. A "Derived figures" checker row, after Constants relations.

  palomas_orrery_dashboard.py
    4. A "Test Derived Figures" button, in the indented group under
       CHECKERS, alphabetically between Test Cross-Check Annotations
       and Test Orbit Cache.

  LEDGER_CONSOLIDATED.md
    5. L-325 opened, recording the ruling and what it cost.
    6. L-314 gains a note: solar wind speed and pressure may be served
       from the cache, and this decision is re-examined then.

WHY THE NEW TEST IS NOT OPTIONAL
    The bow shock held an expression, so it followed its inputs
    automatically. Turning it into a literal gives that up. The
    magnetopause was ALREADY a literal and already followed nothing --
    its Status line names EARTH_SOLAR_WIND_PRESSURE_NPA, that pressure
    is declared pending under L-314, and had it moved the row would
    have gone quietly stale with no test anywhere to catch it.
    test_derived_figures.py recomputes both rows from the inputs they
    name and fails when the rounding stops holding. It replaces an
    automatic recomputation with a check that announces.

RUN THE NEW TEST FILE INTO PLACE FIRST
    Save test_derived_figures.py into the orrery repo root before
    running this patch. The patch checks for it and stops if it is
    missing, because both the runner row and the dashboard button it
    adds would otherwise point at nothing.

WHAT IS PERMANENT AND WHAT IS NOT
    This script is disposable and one-shot. The rounded rows, the
    checker wiring and the ledger record are permanent.

HOW TO RUN IT (Tony)
    Save this file into the orrery repo root, open it in VS Code, and
    click Run.
    Equivalent command:
    python patch_L325_derived_rows_store_reported_figures.py

    Success: six "ok" lines, four "stamp updated" lines, then
             "patch applied".
    Failure: one ERROR or ANCHOR FAIL line. NOTHING is written, to ANY
             of the four files -- all four are written together or none
             is. Undo is Discard Changes in GitHub Desktop.

AFTER IT RUNS
    1. Run test_derived_figures.py (Run button). Expect both rows
       listed with OK, and "All 2 derived row(s) ... recompute to the
       figures they declare."
    2. Run ledger_index.py (Run button). A block was ADDED, so expect
       "OK: 320 L-blocks parsed" -- 320, not 319.
    3. Run orrery_maintenance_run.py. A new "Derived figures" row
       appears after "Constants relations"; the gating total goes
       13 -> 14. "Constants change" will report the two standoffs as
       changed, which is correct and clears on the push.
    4. Open the dashboard and check the new button sits under CHECKERS
       between Test Cross-Check Annotations and Test Orbit Cache.

    The gallery still serves 10.0 and 12.5, so its live Store drift
    check still reports 2 DRIFT. That is L-305 item 6, next.

BASE
    Built on orrery d243067695ccc55d44e0cf103f52ddf9a1bf64f7 at
    https://github.com/tonylquintanilla/palomas_orrery

Written September 12, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

INDEX_START = b"<!-- INDEX:START"
INDEX_END = b"<!-- INDEX:END -->"

STORE = "constants_new.py"
RUNNER = "orrery_maintenance_run.py"
DASH = "palomas_orrery_dashboard.py"
LEDGER = "LEDGER_CONSOLIDATED.md"
NEW_TEST = "test_derived_figures.py"

BASE_FP = {
    STORE: "ffbe836d8f901d011cb4bdf3bcef5ddb",
    RUNNER: "fbe5add20d0d7f841ab0f1532c8c3ee9",
    DASH: "eeea44debba63f769ae54fe51523616d",
    LEDGER: "c4d39ff1b7d4a674a01d3cc3d856c4ed",
}


def fingerprint(path, data):
    lf = data.replace(b"\r\n", b"\n")
    if path == LEDGER:
        a = lf.index(INDEX_START)
        b = lf.index(INDEX_END) + len(INDEX_END)
        lf = lf[:a] + lf[b:]
    return hashlib.md5(lf).hexdigest()


# ==================================================== constants_new.py

MP_OLD = (
    b"EARTH_MAGNETOPAUSE_STANDOFF_RADII = 10.251872972379905\n"
    b"# Unit: r_earth\n"
)

MP_NEW = (
    b"EARTH_MAGNETOPAUSE_STANDOFF_RADII = 10.25\n"
    b"# Unit: r_earth\n"
)

MP_NOTE_OLD = (
    b"# Note: typed as a literal rather than written as the expression it is,\n"
    b"# Note+: because the gallery's store parser evaluates only + - * / and **.\n"
    b"# Note+: A tanh assignment is left out of the parsed set, and the drift check\n"
    b"# Note+: then reports the pointer as NOT IN STORE. That is announced rather\n"
    b"# Note+: than silent, but it carries the wrong reason (\"not a top-level\n"
    b"# Note+: constant\"), it does not gate, and the value stops being compared at\n"
    b"# Note+: all. L-322 retires that parser and this becomes an expression then;\n"
    b"# Note+: the digits here are the expression's own value, so that swap\n"
    b"# Note+: changes nothing.\n"
)

MP_NOTE_NEW = (
    b"# Note: the STORED value is that reported figure, not the arithmetic\n"
    b"# Note+: result. Tony's ruling, 2026-09-12 (L-325): a store carries the\n"
    b"# Note+: figures its sources support. Sixteen digits on a value uncertain\n"
    b"# Note+: in the first decimal is calculator output, not precision. The\n"
    b"# Note+: arithmetic stays recorded above, so the row is still auditable.\n"
    b"# Note+: This row was ALREADY a literal and so already followed nothing:\n"
    b"# Note+: the Status line above names EARTH_SOLAR_WIND_PRESSURE_NPA, which\n"
    b"# Note+: is declared pending (L-314), and had it moved this value would\n"
    b"# Note+: have gone quietly stale with no test anywhere to catch it.\n"
    b"# Note+: test_derived_figures.py now recomputes this row from the inputs\n"
    b"# Note+: the Status line names and fails when the rounding stops holding.\n"
    b"# Note+: That check is what replaces an expression's automatic\n"
    b"# Note+: recomputation, and it announces rather than moving a published\n"
    b"# Note+: number quietly. An earlier Note here said L-322 would turn this\n"
    b"# Note+: row back into an expression once the gallery's parser is retired.\n"
    b"# Note+: That plan is superseded: the stored form is the reported figure\n"
    b"# Note+: whatever the parser can read.\n"
)

BS_OLD = (
    b"EARTH_BOW_SHOCK_STANDOFF_RADII = EARTH_BOW_SHOCK_JELINEK_R0_RADII"
    b" * EARTH_SOLAR_WIND_PRESSURE_NPA ** (-1 / EARTH_BOW_SHOCK_JELINEK_EPS)\n"
    b"# Unit: r_earth\n"
)

BS_NEW = (
    b"EARTH_BOW_SHOCK_STANDOFF_RADII = 13.51\n"
    b"# Unit: r_earth\n"
)

BS_NOTE_OLD = (
    b"# Note: superseded a typed 12.5 on 2026-09-12 (L-305). Two claims went with\n"
)

BS_NOTE_NEW = (
    b"# Note: the STORED value is that reported figure, not the arithmetic\n"
    b"# Note+: result. It was the expression\n"
    b"# Note+: EARTH_BOW_SHOCK_JELINEK_R0_RADII *\n"
    b"# Note+: EARTH_SOLAR_WIND_PRESSURE_NPA ** (-1 / EARTH_BOW_SHOCK_JELINEK_EPS)\n"
    b"# Note+: until 2026-09-12. Tony's ruling (L-325): a store carries the\n"
    b"# Note+: figures its sources support, and four of them against a crossing\n"
    b"# Note+: scatter of 0.69 R_E is already generous. Storing the expression\n"
    b"# Note+: bought an automatic recomputation when an input moved, which is\n"
    b"# Note+: a published number changing with nobody looking;\n"
    b"# Note+: test_derived_figures.py recomputes this row from its inputs and\n"
    b"# Note+: FAILS instead, which is the same protection said out loud.\n"
    b"# Note+: superseded a typed 12.5 on 2026-09-12 (L-305). Two claims went with\n"
)

STORE_STAMP_OLD = (
    b"\"# Unit:\" line, the fifteenth comment key, per L-322 ruling 1)\n"
    b"\"\"\"\n"
)

STORE_STAMP_NEW = (
    b"\"# Unit:\" line, the fifteenth comment key, per L-322 ruling 1)\n"
    b"Module updated: September 12, 2026 with Anthropic's Claude Opus 5\n"
    b"(L-325: the two derived rows now STORE the figure they already said\n"
    b"to report -- 10.25 and 13.51 -- rather than the arithmetic result.\n"
    b"test_derived_figures.py recomputes each from the inputs its Status\n"
    b"line names and fails when the rounding stops holding)\n"
    b"\"\"\"\n"
)

# ==================================================== the runner

RUNNER_ROW_OLD = (
    b"    ('Constants relations', ['test_constants_provenance.py'], None),\n"
)

RUNNER_ROW_NEW = (
    b"    ('Constants relations', ['test_constants_provenance.py'], None),\n"
    b"    # A derived row stores its reported figure, so nothing recomputes\n"
    b"    # it on import any more. This is what notices when an input moves\n"
    b"    # and the stored figure stops following from it. It also fails on\n"
    b"    # a derived row it does not cover, so it cannot pass while blind.\n"
    b"    # L-325.\n"
    b"    ('Derived figures', ['test_derived_figures.py'], None),\n"
)

RUNNER_STAMP_OLD = (
    b"Module updated: September 12, 2026 with Anthropic's Claude Opus 5 (L-324:\n"
    b"the CHECKERS list gains Row shape -- the same script run --shape-only --\n"
    b"so the row-shape guard reports its own numbers here instead of printing\n"
    b"them above another checker's verdict, where the dashboard never saw them.)\n"
)

RUNNER_STAMP_NEW = (
    b"Module updated: September 12, 2026 with Anthropic's Claude Opus 5 (L-324:\n"
    b"the CHECKERS list gains Row shape -- the same script run --shape-only --\n"
    b"so the row-shape guard reports its own numbers here instead of printing\n"
    b"them above another checker's verdict, where the dashboard never saw them.)\n"
    b"Module updated: September 12, 2026 with Anthropic's Claude Opus 5 (L-325:\n"
    b"the CHECKERS list gains Derived figures, which recomputes each derived\n"
    b"constant from the inputs it names and checks it against the figure it\n"
    b"declares -- the check that replaces a stored expression's automatic\n"
    b"recomputation.)\n"
)

# ==================================================== the dashboard

DASH_BUTTON_OLD = (
    b"        (\"Test Orbit Cache\",\n"
)

DASH_BUTTON_NEW = (
    b"        (\"Test Derived Figures\",\n"
    b"         \"test_derived_figures.py\",\n"
    b"         \"Recomputes every derived constant in constants_new.py from \"\n"
    b"         \"the inputs its Status line names, and checks the result \"\n"
    b"         \"against the figure the row declares it reports. A derived \"\n"
    b"         \"row stores its reported figure rather than the arithmetic \"\n"
    b"         \"result, so nothing recomputes it on import; this is what \"\n"
    b"         \"says so when an input moves. Fails on a derived row it does \"\n"
    b"         \"not cover, so it cannot pass while blind.\",\n"
    b"         SCRIPT_DIR,\n"
    b"         True,\n"
    b"         None,\n"
    b"         True),\n"
    b"        (\"Test Orbit Cache\",\n"
)

DASH_STAMP_OLD = (
    b"September 12, 2026 with Anthropic's Claude Opus 5 (L-324): added the two\n"
)

DASH_STAMP_NEW = (
    b"September 12, 2026 with Anthropic's Claude Opus 5 (L-325): added the Test\n"
    b"Derived Figures button, in the indented group under CHECKERS.\n"
    b"September 12, 2026 with Anthropic's Claude Opus 5 (L-324): added the two\n"
)

# ==================================================== the ledger

LEDGER_BLOCK_OLD = (
    b"`skills/orrery-coding-conventions/SKILL.md`.\n"
    b"\n"
)

LEDGER_BLOCK_NEW = (
    b"`skills/orrery-coding-conventions/SKILL.md`.\n"
    b"\n"
    b"#### [L-325] A derived row stores its reported figure, not the"
    b" arithmetic result\n"
    b"<!-- L:325 status:OPEN upd:2026-09-12 section:A flag: rice:3/3/90/2 -->\n"
    b"- **Where this came from.** L-305 item 6 was about to copy two"
    b" standoff\n"
    b"  values into the gallery config, and Claude proposed copying"
    b" them at full\n"
    b"  stored precision -- 10.251872972379905 and 13.511736110493397 --"
    b" on the\n"
    b"  reasoning that the served copy must equal the store exactly or the"
    b" live\n"
    b"  drift check reports DRIFT forever. Tony stopped it: \"the store"
    b" should\n"
    b"  only carry significant digits not what the calculator generates.\""
    b"\n"
    b"- **He was right, and the store already half agreed.** Both rows"
    b" already\n"
    b"  declared what to report, with the reason. The magnetopause row"
    b" says\n"
    b"  REPORT 10.25, because Shue's Table 1 gives a1 to +/- 0.10 R_E and"
    b" a5 to\n"
    b"  +/- 0.5 and either alone moves r0 by about +/- 0.09. The bow"
    b" shock row\n"
    b"  says REPORT 13.51, because Jelinek states no uncertainty on his"
    b" fitted\n"
    b"  numbers and what bounds the value is the 0.69 R_E crossing"
    b" scatter. The\n"
    b"  rows said what to report and then stored something else.\n"
    b"- **What the argument for the expression turned out to be worth.**"
    b" A\n"
    b"  stored expression recomputes when an input moves, which a literal"
    b" does\n"
    b"  not. That is real. But NOTHING TESTED EITHER ROW: the provenance"
    b" suite\n"
    b"  has a derived-constants section and neither standoff is in it. And"
    b" the\n"
    b"  magnetopause was already a literal inheriting"
    b" EARTH_SOLAR_WIND_PRESSURE_NPA,\n"
    b"  which is declared pending under L-314 -- so the failure mode the"
    b" ruling\n"
    b"  was accused of creating already existed in the store, unguarded."
    b" Two\n"
    b"  derived rows in the whole file, one of them already doing it"
    b" Tony's way.\n"
    b"- **What was built.** `constants_new.py`: both rows store 10.25 and"
    b" 13.51.\n"
    b"  `test_derived_figures.py`: recomputes each derived row from the"
    b" inputs\n"
    b"  its own Status line names, rounds to the figures its own REPORT"
    b" declares,\n"
    b"  and fails when the two stop agreeing -- and fails on any derived"
    b" row it\n"
    b"  does not cover, so it cannot pass while blind. Wired into"
    b"\n"
    b"  `orrery_maintenance_run.py` as Derived figures and into the"
    b" dashboard as\n"
    b"  Test Derived Figures, on Tony's instruction that a new test gets"
    b" both.\n"
    b"**Tony:** \"Why do we need to carry a full value that is not"
    b" supported? Why\n"
    b"does the calculation need to be re-derived every time creating this"
    b"\n"
    b"problem again? Why not do the arithmetic once, correct it to"
    b" significant\n"
    b"figures, store it and serve it?\"\n"
    b"**Note:** the trade is an automatic recomputation for a check that"
    b"\n"
    b"announces. That is the better half of the trade: a silent recompute"
    b"\n"
    b"changes a published number with nobody looking, while a literal plus"
    b" a\n"
    b"test FAILS when its inputs move.\n"
    b"**Note:** nothing visible changed. The only consumers are"
    b"\n"
    b"`shell_configs.py` and `earth_visualization_shells.py`, both of which"
    b"\n"
    b"already print these at `:.4g` -- which is 10.25 and 13.51. The drawn"
    b"\n"
    b"shells move by under 0.002 R_E against a 0.69 R_E scatter.\n"
    b"**Gap:** the rule belongs in `provenance-discipline` at its next"
    b" bump --\n"
    b"a derived row stores the figure its sources support, and a check"
    b" recomputes\n"
    b"it. Not taken this session: a skill bump cannot be verified from"
    b" inside the\n"
    b"session that makes it. Also open: L-305 item 6 still serves 10.0 and"
    b" 12.5,\n"
    b"so the gallery's live Store drift check reports 2 DRIFT until it"
    b" lands.\n"
    b"**Ref:** L-305, L-314, L-322, `constants_new.py`,\n"
    b"`test_derived_figures.py`, `orrery_maintenance_run.py`,\n"
    b"`palomas_orrery_dashboard.py`, `skills/provenance-discipline/SKILL.md`.\n"
    b"\n"
)

L314_NOTE_OLD = (
    b"**Gap:** the whole item; sequenced after L-305 closes.\n"
)

L314_NOTE_NEW = (
    b"**Note (2026-09-12, Tony) -- this item reopens L-325.** We are"
    b" considering\n"
    b"serving solar wind SPEED and PRESSURE from the cache. If"
    b" EARTH_SOLAR_WIND_PRESSURE_NPA\n"
    b"stops being a declared constant and becomes a fed value, the two"
    b" derived\n"
    b"standoffs stop being fixed numbers with a reported figure and become"
    b"\n"
    b"quantities that move with the feed. L-325's decision -- store the"
    b" reported\n"
    b"figure, let `test_derived_figures.py` catch an input that moves --"
    b" is\n"
    b"written for a pressure that changes rarely and deliberately. A feed"
    b" changes\n"
    b"it on a schedule, and a test that fails every time the wind blows is"
    b" a test\n"
    b"nobody reads. Re-examine both when this item is designed, not when"
    b" it is\n"
    b"built.\n"
    b"**Gap:** the whole item; sequenced after L-305 closes.\n"
)

LEDGER_STAMP_OLD = (
    b"built on 62ee5149.\n"
    b"Review and RICE update Tony 6-21-2026"
)

LEDGER_STAMP_NEW = (
    b"built on 62ee5149.\n"
    b"Module updated: September 12, 2026 with Anthropic's Claude Opus 5\n"
    b"(L-325 opened: the two derived rows store their reported figures and\n"
    b"test_derived_figures.py guards them; L-314 gains the note that a fed\n"
    b"pressure reopens that decision), built on d2430676.\n"
    b"Review and RICE update Tony 6-21-2026"
)

EDITS = {
    STORE: [
        ("store: magnetopause stores 10.25", MP_OLD, MP_NEW),
        ("store: magnetopause Note", MP_NOTE_OLD, MP_NOTE_NEW),
        ("store: bow shock stores 13.51", BS_OLD, BS_NEW),
        ("store: bow shock Note", BS_NOTE_OLD, BS_NOTE_NEW),
    ],
    RUNNER: [
        ("runner: Derived figures row", RUNNER_ROW_OLD, RUNNER_ROW_NEW),
    ],
    DASH: [
        ("dashboard: Test Derived Figures button",
         DASH_BUTTON_OLD, DASH_BUTTON_NEW),
    ],
    LEDGER: [
        ("ledger: L-325 opened", LEDGER_BLOCK_OLD, LEDGER_BLOCK_NEW),
        ("ledger: L-314 note on a fed pressure",
         L314_NOTE_OLD, L314_NOTE_NEW),
    ],
}

STAMPS = {
    STORE: (STORE_STAMP_OLD, STORE_STAMP_NEW),
    RUNNER: (RUNNER_STAMP_OLD, RUNNER_STAMP_NEW),
    DASH: (DASH_STAMP_OLD, DASH_STAMP_NEW),
    LEDGER: (LEDGER_STAMP_OLD, LEDGER_STAMP_NEW),
}


def main():
    here = os.path.dirname(os.path.abspath(__file__))

    if not os.path.exists(os.path.join(here, NEW_TEST)):
        print("ERROR: %s is not in the repo root yet." % NEW_TEST)
        print("This patch adds a maintenance-run row and a dashboard button")
        print("that both point at it, so save it beside this script first,")
        print("then Run again. NOTHING was written.")
        return 1

    originals = {}
    for path in (STORE, RUNNER, DASH, LEDGER):
        full = os.path.join(here, path)
        if not os.path.exists(full):
            print("ERROR: %s not found. Save this script into the orrery "
                  "repo root and Run again." % path)
            return 1
        with open(full, "rb") as handle:
            originals[path] = handle.read()

    for path, data in originals.items():
        try:
            fp = fingerprint(path, data)
        except ValueError:
            print("ERROR: INDEX zone markers not found in %s. NOTHING "
                  "written." % path)
            return 1
        if fp != BASE_FP[path]:
            print("ERROR: base moved. %s does not match the tree this patch "
                  "was built against." % path)
            print("  expected %s" % BASE_FP[path])
            print("  found    %s" % fp)
            print("NOTHING was written, to any of the four files.")
            return 1

    updated = {}
    applied = []
    stamped = []

    for path, data in originals.items():
        is_crlf = data.count(b"\r\n") > 0
        new = data
        todo = list(EDITS[path]) + [
            ("%s: currency stamp" % path,) + STAMPS[path]]
        for label, old, repl in todo:
            o, r = old, repl
            if is_crlf:
                o = o.replace(b"\n", b"\r\n")
                r = r.replace(b"\n", b"\r\n")
            n = new.count(o)
            if n != 1:
                print("ANCHOR FAIL: %s -- expected 1 match in %s, found %d."
                      % (label, path, n))
                print("NOTHING was written, to any of the four files.")
                print("Undo is Discard Changes in GitHub Desktop.")
                return 1
            new = new.replace(o, r)
            if label.endswith("currency stamp"):
                stamped.append(path)
            else:
                applied.append(label)
        non_ascii = sum(1 for ch in new if ch > 127)
        if non_ascii:
            print("ERROR: patch would introduce %d non-ASCII byte(s) into "
                  "%s. NOTHING written." % (non_ascii, path))
            return 1
        updated[path] = new

    for path, new in updated.items():
        with open(os.path.join(here, path), "wb") as handle:
            handle.write(new)

    for label in applied:
        print("ok  %s" % label)
    for path in stamped:
        print("stamp updated  %s" % path)
    print("patch applied (%d files)" % len(updated))
    print("")
    print("NEXT:")
    print("  1. Run test_derived_figures.py -- expect both rows OK.")
    print("  2. Run ledger_index.py -- expect 320 L-blocks, NOT 319.")
    print("  3. Run orrery_maintenance_run.py -- a 'Derived figures' row")
    print("     appears after 'Constants relations'; gating 13 -> 14, and")
    print("     'Constants change' reports the two standoffs as changed.")
    print("  4. Open the dashboard: Test Derived Figures sits under")
    print("     CHECKERS, between Test Cross-Check Annotations and Test")
    print("     Orbit Cache.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
