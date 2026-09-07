"""
patch_L291_5_ledger_20260907.py -- ledger entries for the 2026-09-07 Earth session

Built on orrery 5170bec1c81a6a025c5499610e328e0f788e6a43
at https://github.com/tonylquintanilla/palomas_orrery (main)
and gallery 54432474ecbb81d7e20d04b9a2fd523c7e724685
at https://github.com/tonylquintanilla/tonyquintanilla.github.io (main).

WHAT THIS DOES (LEDGER_CONSOLIDATED.md only; detail blocks only)
  Closes:   L-290, L-296 (the 1.10 gate fired: this session's loaded copy
            reads 1.10), L-295 (both atmosphere shells now draw their
            sourced boundaries; Tony's Mode 5, 2026-09-07).
  Updates:  L-291 (step 0 passed; step 2's orrery half done in four
            patches; Gap now names the gallery patch).
  Adds:     L-297 Earth-Moon Lagrange points -- serving path sized, deferred
            L-298 Seeing the orrery-to-exhibit feature gap (Tony: discuss)
            L-299 A hover that quotes a number names its source
            L-300 sweep_collapsed_features.py joins the gallery runner
  Then Tony runs ledger_index.py (Run button) to regenerate the index and
  migrate the DONE blocks to section C. This script does not touch the
  index zone.

  Handles: highest in the file at 5170bec1 is L-296; the four new ones
  are the NEXT four. The script re-checks that before writing.

GUARDS
  Binary read, LF-normalised, md5 checked; every edit must match exactly
  once; inserted text is ASCII-only, LF.

Written September 2026 with Anthropic's Claude Fable 5.1.
"""
import hashlib
import re
import sys
from pathlib import Path

TARGET = Path(__file__).resolve().parent / "LEDGER_CONSOLIDATED.md"
EXPECTED_MD5 = "a5459a53eedc07de46639ff6b89232d9"
EXPECTED_MAX_HANDLE = 296

EDITS = [
    # ---- L-290: close ----
    (
        "<!-- L:290 status:PENDING-GATE upd:2026-09-06 section:A flag: rice:4/3/90/1 -->",
        "<!-- L:290 status:DONE upd:2026-09-07 section:C flag: rice:4/3/90/1 -->",
    ),
    (
        "**Gap:** `skills_index.py`, the reinstall, the push; then the next\n"
        "session's load confirms 1.10 and this closes.\n",
        "- **Claude, 2026-09-07 -- GATE FIRED.** The next session loaded\n"
        "  `ledger-and-session-records` and it reads 1.10, cut from `50cbd2df`,\n"
        "  matching the manifest. That is the only check that could confirm\n"
        "  the install, and it passed. Closed.\n"
        "**Gap:** none.\n",
    ),
    # ---- L-296: close ----
    (
        "<!-- L:296 status:PENDING-GATE upd:2026-09-06 section:A flag: rice:3/3/90/1 -->",
        "<!-- L:296 status:DONE upd:2026-09-07 section:C flag: rice:3/3/90/1 -->",
    ),
    (
        "**Gap:** rides L-290's gate -- `skills_index.py`, the reinstall, the\n"
        "push, then the next session's load.\n",
        "- **Claude, 2026-09-07:** rode L-290's gate and it fired; the loaded\n"
        "  skill reads 1.10. Closed with it.\n"
        "**Gap:** none.\n",
    ),
    # ---- L-295: close (both shells, not one) ----
    (
        "#### [L-295] The upper atmosphere shell disagrees with its own hover text\n"
        "<!-- L:295 status:OPEN upd:2026-09-06 section:A flag: rice:2/2/90/1 -->",
        "#### [L-295] The upper atmosphere shell disagrees with its own hover text\n"
        "<!-- L:295 status:DONE upd:2026-09-07 section:C flag: rice:2/2/90/1 -->",
    ),
    (
        "**Gap:** decide which number is right, fix the other, source the one\n"
        "that survives.\n"
        "**Ref:** L-291, L-292, earth_visualization_shells.py.\n",
        "- **Claude, 2026-09-07 -- it was BOTH shells, and the drawn fraction was\n"
        "  the stale half.** The lower atmosphere had the same defect: drawn at\n"
        "  1.05 radii (about 319 km up) under a hover ending at the 50 km\n"
        "  stratopause. Both fractions were visibility choices. Tony's ruling:\n"
        "  remove the drawing choice and draw the physical boundary, as the\n"
        "  Sun's chromosphere does. `EARTH_STRATOPAUSE_ALTITUDE_KM` (50, NOAA\n"
        "  JetStream / NASA) and `EARTH_THERMOPAUSE_ALTITUDE_KM` (600, same)\n"
        "  entered the store at `c51761a0`; `SHELL_CONFIGS['Earth']` draws\n"
        "  their `_RADII` at `5170bec1`, info markers stepped to 20 and 30\n"
        "  degrees so the interior-to-atmosphere stack reads as four markers.\n"
        "  The live builders were `SHELL_CONFIGS`, not the\n"
        "  `create_earth_*_atmosphere_shell` functions the entry named --\n"
        "  those are L-254 dead code and were left alone.\n"
        "- **Mode 5, Tony, 2026-09-07:** \"correct\" on the shells hugging the\n"
        "  crust and on the three markers being separate.\n"
        "**Gap:** none.\n"
        "**Ref:** L-291, L-292, shell_configs.py, constants_new.py (Earth\n"
        "exhibit block).\n",
    ),
    # ---- L-291: progress ----
    (
        "<!-- L:291 status:OPEN upd:2026-09-06 section:A flag: rice:4/4/80/3 -->",
        "<!-- L:291 status:OPEN upd:2026-09-07 section:A flag: rice:4/4/80/3 -->",
    ),
    (
        "**Gap:** the skill install; then the served-data work (step 2), the\n"
        "build (step 3), and Mode 5 on the phone. Closes on Tony's eyes.\n",
        "- **Claude, 2026-09-07 -- step 0 passed, step 2's orrery half done.**\n"
        "  Both skills loaded at the versions the handoff required. Four\n"
        "  orrery patches, each md5-guarded, each Mode-5'd by Tony:\n"
        "  `patch_L291_1` (21 constants with sources, orrery `c51761a0`),\n"
        "  `patch_L291_2` (shell literals migrated onto them, `fe87147f`),\n"
        "  `patch_L291_3` (atmosphere shells draw the store, `5170bec1`, closes\n"
        "  L-295), `patch_L291_4` (every live Earth hover names its source;\n"
        "  SHA in Tony's next report). Sources were fetched, not recalled:\n"
        "  IERS Conventions 2010 TN36 Table 1.1; IADC-02-01 Rev. 3 sec. 3.3.2;\n"
        "  Baker et al. 2018 SSR 214:17; doi:10.1029/2024JA033504; Shue et al.\n"
        "  1998; Lugaz et al. 2016 Nat. Commun. 7:13001; Baliukin et al. 2019.\n"
        "- **Two values moved when sourced.** Bow shock 15 -> 12.5 radii\n"
        "  (midpoint of Lugaz's 11-14; a citation saying 11-14 cannot sit under\n"
        "  a 15 -- Tony agreed, and ruled the orrery migrate at once under one\n"
        "  store, one source of truth). LEO 6571/8371 -> 6578/8378 km (the old\n"
        "  figures were the 6371 km MEAN radius plus altitude).\n"
        "- **Lagrange points deferred** to L-297 on Tony's ruling; the drawer\n"
        "  row waits. **Sun-Earth L-points** stay with L-294.\n"
        "**Gap:** the GALLERY half of step 2 -- `data/objects_config.json`\n"
        "Earth entry: value/unit/source/orrery_constant on every feature,\n"
        "the new rows (magnetosphere as four served rows, LEO, geostationary,\n"
        "Hill sphere, geocorona), the `orientation` block, the exosphere shell\n"
        "(L-292) -- then store drift MATCH by name on the live run. Then steps\n"
        "3-8. Closes on Tony's eyes.\n",
    ),
]

NEW_BLOCKS = """#### [L-297] Earth-Moon Lagrange points: serving path sized, deferred from the Earth exhibit
<!-- L:297 status:OPEN upd:2026-09-07 section:A flag: rice:2/3/70/3 -->
- **Sized 2026-09-07 before any Earth code, on the build order's
  instruction.** Record:
  `documentation/SIZING_earth_moon_lagrange_20260907.md` (gallery repo).
- **The finding.** The builder serves three shapes and its validator
  enforces them: osculating elements (every non-spacecraft; fetch is
  unconditional, missing aborts on #3), a positions arc (spacecraft
  only), and features-only (the Sun). The assembler draws only objects
  with `osculating`. A Lagrange point fits none of the three, so this is
  not a config entry: it is a fourth serving shape (skip the elements
  fetch, keep the vector fetch so `as_of_today` is populated, trust
  method `epoch_marker`), a validator branch, a fallback branch, five
  config entries (3011-3015 @399), an assembler branch that renders
  `as_of_today` as the marker for that shape alone, and one nightly run
  before anything appears. One session of its own.
- **What helps:** the exhibit's epoch (today 00:00 UTC) and the cache's
  epoch are the same instant, so an epoch marker is exactly the scene's
  epoch, not a stale one.
- **Rejected:** computing them client-side from the Moon's propagated
  marker (CR3BP geometry, ~40 lines, no builder change). Smaller, but the
  orrery already draws these points from Horizons; an approximation of a
  value that can be fetched is a permanent apology for a shortcut, and
  it would be replaced later, so the forty lines are spent twice.
- **Tony's ruling, 2026-09-07:** defer (C) for the Earth build; serve
  from Horizons (A) as the follow-on. Not B.
- Sun-Earth L1-L5 transfer the same way when L-294 comes up.
**Gap:** the builder session described above, after the Earth exhibit
ships. Tony-action (decide): when.
**Ref:** L-291, L-294, gallery `tools/gallery_cache_builder.py` (lines
745-800, 910-935, 1135-1150 at `92e98ca9`), `gallery/assembler/assemble.py`
(line 54), the sizing note.

#### [L-298] Seeing the gap between what the orrery draws and what an exhibit serves
<!-- L:298 status:OPEN upd:2026-09-07 section:A flag: rice:3/3/60/2 -->
- **Tony's question, 2026-09-07:** when a new shell is added to the
  orrery, does the assembler skill pick it up and draw it too? **Answer:
  no, and by design.** A feature reaches an exhibit only by hand: a
  served row with value/unit/source/pointer, a renderer for its geometry
  type if new, and a ruling that it belongs in that room. Knowledge
  transfers between the two instruments; machinery does not; no element
  needs to exist. Neither gallery-assembler nor interactive-exhibit
  claims otherwise.
- **What is missing is not migration but VISIBILITY.** Earth had eleven
  shells in the orrery and two feature groups in the gallery, and nobody
  could have noticed without comparing the two by hand -- which is how
  this session found it, at the cost of most of an evening's reading.
- **Two candidate responses, and Tony has asked that this be DISCUSSED
  rather than built:**
  (a) a discovery tool in the L-268 shape -- per body, the orrery's shell
  keys against the served feature keys, difference printed by name,
  clean when reconciled or when the difference is on a recorded
  not-in-scope list; fixes nothing, forces nothing; joins the gallery
  maintenance runner; plus a rule in interactive-exhibit that a new
  orrery shell for a body with an exhibit is recorded as a candidate
  feature for that room and ruled in or out;
  (b) leave it to judgment, on the ground that a tool here is over-design.
- **Tony, 2026-09-07 (paraphrased from chat, not his hand):** "We don't
  want to over design either. It may be best to leave this migration to
  judgement. On the other hand the gap is hard to see due to the level
  of detail." Both halves are live.
- **Claude:** the honest test is whether judgment can act on something
  it cannot see. If a body's shell-versus-feature difference is short and
  named once per session start, judgment works; if it takes an evening
  to assemble, it does not get exercised. The tool's job would be only
  to make the list short and named. Recommendation offered, not ruled.
**Gap:** Tony-action (decide): (a), (b), or a third thing. If (a), build
after the Earth exhibit ships, when there are two bodies to test
against.
**Ref:** L-268 (the sweep this would resemble), L-291, L-292,
gallery-assembler SKILL.md, interactive-exhibit SKILL.md, the protocol's
"The Orrery and the Assembler".

#### [L-299] A hover that quotes a measured number names its source in the hover
<!-- L:299 status:OPEN upd:2026-09-07 section:A flag: rice:4/3/85/2 -->
- **Tony's ruling, 2026-09-07.** The scanner reads the citation in the
  code comment beside a string; the viewer never sees that comment. A
  visitor reading "6.61 Earth radii" should be able to read where it
  came from without opening the repo. Earth's hovers were inconsistent:
  the geostationary belt carried a Source line (added by hand once),
  the magnetosphere, bow shock, belts, LEO, Hill sphere and the four
  interior layers did not.
- **Applied to Earth** in `patch_L291_4_earth_hover_sources.py`: thirteen
  live Earth hovers now end in a Source line SCOPED to what it sources
  ("Source (radius):" where the same hover also quotes temperatures PREM
  does not give). Two lines were REPLACED under remove-and-note rather
  than annotated: the belt hovers' altitude ranges (1,000-6,000 km and
  13,000-60,000 km) matched no source consulted, so they now state the
  sourced peak distances and spans in Earth radii.
- **The rule belongs in orrery-coding-conventions** (1.7 -> 1.8), beside
  the hover-text AU convention. Not bumped this session: one session,
  one bump, and this session's bump budget is spent on none -- the rule
  is recorded here so the bump carries it whole.
- **Remediation for the other bodies is a sweep, in slices, by body**, on
  the braid: Jupiter and Saturn as their exhibits come up, not globally.
  Discovery (which hovers quote a number with no Source line) is one
  grep and terminates.
**Gap:** Tony-action (do): the skill bump when the next
orrery-coding-conventions session opens; then the per-body slices.
**Ref:** L-291, orrery-coding-conventions SKILL.md, provenance-discipline
SKILL.md ("A Breadcrumb Must Not Cite" -- the Source line must be TRUE,
so it is scoped).

#### [L-300] sweep_collapsed_features.py joins the gallery maintenance runner as a gating checker
<!-- L:300 status:OPEN upd:2026-09-07 section:A flag: rice:3/3/90/1 -->
- **Tony's question, 2026-09-07:** runner or dashboard? **Ruling, on
  Claude's recommendation: the runner, gating.** The script already has
  the right shape: it exits 2 only on a feature group it cannot classify
  -- exactly the case that should stop a push -- and a non-zero
  collapsed count exits 0 and prints the names, so the sixteen known
  items report without gating. A check in a store nobody opens cannot
  fail; the runner is the store that gets opened.
- Earth's step 2 splits the magnetosphere into four served rows, which
  retires four of L-268's sixteen; with the sweep in the routine, that
  delta appears by name the day it lands.
**Gap:** one small patch to `gallery_maintenance_run.py` registering the
checker; then a run to confirm it appears in the CHECKERS list with its
verdict line. Not yet written.
**Ref:** L-268, gallery `tools/sweep_collapsed_features.py`,
`gallery_maintenance_run.py`.

"""

INSERT_BEFORE = "#### [L-278] A relayout from inside a Plotly event handler re-enters the update machinery\n"


def main():
    lf = TARGET.read_bytes().replace(b"\r\n", b"\n")
    got = hashlib.md5(lf).hexdigest()
    if got != EXPECTED_MD5:
        print("STOP: LEDGER_CONSOLIDATED.md md5 (LF) is %s, expected %s (at 5170bec1)." % (got, EXPECTED_MD5))
        print("      Either this patch already ran or the ledger moved. Nothing written.")
        return 1
    text = lf.decode("utf-8")
    mx = max(int(h) for h in re.findall(r"^#### \[L-(\d+)\]", text, re.M))
    if mx != EXPECTED_MAX_HANDLE:
        print("STOP: highest handle is L-%d, expected L-%d; new handles would collide. Nothing written." % (mx, EXPECTED_MAX_HANDLE))
        return 1
    for i, (old, new) in enumerate(EDITS, 1):
        c = text.count(old)
        if c != 1:
            print("STOP: edit %d matched %d time(s), expected 1. Nothing written." % (i, c))
            print("      old text begins: %r" % old[:70])
            return 1
    if text.count(INSERT_BEFORE) != 1:
        print("STOP: insertion anchor not unique. Nothing written.")
        return 1
    NEW_BLOCKS.encode("ascii")
    for old, new in EDITS:
        text = text.replace(old, new, 1)
    text = text.replace(INSERT_BEFORE, NEW_BLOCKS + INSERT_BEFORE, 1)
    TARGET.write_bytes(text.encode("utf-8"))
    print("Patched LEDGER_CONSOLIDATED.md, new md5 (LF) %s" % hashlib.md5(text.encode("utf-8")).hexdigest())
    print("Closed:  L-290, L-295, L-296 (status DONE, section C)")
    print("Updated: L-291")
    print("Added:   L-297 Lagrange serving path (deferred)")
    print("         L-298 orrery-to-exhibit gap visibility (Tony: discuss)")
    print("         L-299 hover names its source (rule pending skill 1.8)")
    print("         L-300 collapsed-features sweep into the gallery runner")
    print("Next: run ledger_index.py (Run button) to rebuild the index and migrate")
    print("  the DONE blocks; then commit and push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
