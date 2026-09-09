"""
patch_L304_L306_skill_bumps_20260908.py -- two skill bumps ahead of the build

Built on orrery 159c5a2cf43e3d9be1d6cd92a5ade0731aeb7bc5
at https://github.com/tonylquintanilla/palomas_orrery (main)
and gallery 700b426d4cecc1f80fd6f9ca5758e5058ea497a6
at https://github.com/tonylquintanilla/tonyquintanilla.github.io (main).
Both confirmed against the live remotes before this was written.

WHY BEFORE THE BUILD, NOT INSIDE IT
A reinstall is invisible to the session that made it -- the skill copy a
conversation loads is bound when the conversation starts. A build session
that bumped these would have loaded the OLD versions and could not verify
its own bump; it would write the confirmation forward as an obligation,
which is what v3.52 and v3.54 both had to do. Bumping here means the
build session loads 1.3 and 2.11 against a manifest that says 1.3 and
2.11, and the gate clears on something it can actually read.

Three-store check performed before writing: gallery-assembler reads 1.2
in the repo at 159c5a2c, 1.2 installed, 1.2 in the manifest;
provenance-discipline reads 2.10 in all three. No stale-skill stop.

WHAT THIS DOES (five files in the ORRERY repo, applied only if all guards pass)

skills/gallery-assembler/SKILL.md            1.2 -> 1.3
  Four field notes from the 2026-09-07/08 gallery session (L-304): three
  Plotly 2.35.2 behaviours read out of the shipped bundle, and one viewer
  lesson that is not Plotly's.

skills/provenance-discipline/SKILL.md        2.10 -> 2.11
  A Drawing Approximation Does Not Promote [CRITICAL] (L-306), placed
  directly after Measured Is the Goal, Declared Is the Fallback, whose
  direction of travel it bounds.

PROJECT_INSTRUCTIONS.md                      v3.54 -> v3.55
  The v3.55 entry naming both bumps (binding rule step 3, the one that
  stops firing). The header stamp and the SHA anchor move with it -- v3.52
  records that this header sat stale for three versions. The v3.52 entry
  moves down to keep three resident. The manifest zone is NOT touched
  here: Tony runs skills_index.py, which owns that zone.

documentation/PROJECT_INSTRUCTIONS_HISTORY.md
  Receives the v3.52 entry verbatim, with the moved-down note.

LEDGER_CONSOLIDATED.md
  L-304 closes DONE. L-306's Gap loses the provenance-discipline bump and
  keeps nothing else, so it closes DONE too.

Written September 2026 with Anthropic's Claude Opus 5.
"""
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FILES = {
    "skills/gallery-assembler/SKILL.md": "d17443c390d8af0762fcc1fe4e551b01",
    "skills/provenance-discipline/SKILL.md": "14f65e629ddb7e42c7d6b15f2888d38f",
    "PROJECT_INSTRUCTIONS.md": "c60ab44ab297337ad69e054a55db2959",
    "documentation/PROJECT_INSTRUCTIONS_HISTORY.md": "443f06460392d5eac5371da1c9e757d2",
    "LEDGER_CONSOLIDATED.md": "614bbb763514293744a29f5d97b5ffda",
}

# ---------------------------------------------------------------- assembler
GA_VERSION_OLD = (
    "Skill version: 1.2 | Cut from orrery @ 5b3fb6b4 (v1.2),\n"
    "earlier @ f83a3abc72c5516e6dc2ad264be53ce95b68cf38 (v1.1) | 2026-09-02\n"
)
GA_VERSION_NEW = (
    "Skill version: 1.3 | Cut from orrery @ 159c5a2c (v1.3),\n"
    "earlier @ 5b3fb6b4 (v1.2),\n"
    "@ f83a3abc72c5516e6dc2ad264be53ce95b68cf38 (v1.1) | 2026-09-08\n"
    "v1.3 (L-304) adds four field notes from the 2026-09-07/08 gallery\n"
    "session. Three are Plotly 2.35.2 behaviours READ OUT OF THE SHIPPED\n"
    "BUNDLE rather than inferred, and each one cost a real defect Tony\n"
    "found on the served Earth-and-Moon card. The fourth is not Plotly's\n"
    "at all. They sit beside the event-handler note because they are the\n"
    "same class: the library does something reasonable that is not what\n"
    "the calling code meant.\n"
)

GA_NOTES = """
## Field note: three Plotly 2.35.2 behaviours, read out of the bundle

Each of these cost a defect on the served gallery in one day, and each
was settled by grepping the shipped `plotly-2.35.2.min.js` rather than
by reasoning about what Plotly ought to do. npm can fetch that bundle
into the sandbox. Do that before theorising.

**A layout-level `dragmode` relayout kills 3D rotation, even to null.**
Relayout `dragmode` at the LAYOUT level on a figure with a `scene` and
gl3d's `updateFx` copies the layout dragmode -- default `"zoom"` --
into every scene. Turntable rotation is gone until a modebar button
restores it. On a phone there is no modebar button, so the card simply
does not rotate. Never touch `dragmode` on a 3D figure; for 2D, read an
absent dragmode as null rather than as undefined. (L-286, gallery
`1eb1e084`. The sweep ran `applySweep()` after every newPlot and
compared "restore null" against the layout's undefined.)

**`hoverlabel.bgcolor` at ZERO opacity renders as opaque grey.** Plotly
replaces a zero-opacity label background with `defaultLine`, `#444`.
"Transparent" is not transparent; it is a grey box. Use a small
non-zero opacity -- 0.01 works -- when suppressing a tooltip by
appearance. (L-288.)

**A per-trace `hoverlabel` overrides the layout's.** The orrery writes
`{font: {size: 11}}` on many traces, so a layout-level hover
suppression never reaches them. Strip the per-trace `hoverlabel` when
routing hover, rather than trying to beat it from the layout. (L-288.
The prior field note that `hoverinfo='none'` kills 3D events still
holds, which is why suppression is done by appearance at all.)

## Field note: a plotly_click bubbles as a DOM click

Not Plotly's doing, and the symptom does not look like a click problem.
`index.html` opened its info card from `plotly_click`; the same tap then
bubbled to the document-level listener whose rule is "a click outside
the card dismisses it," and it dismissed the card it had just opened.

The two accidental workarounds are the tell. A right click fires
`plotly_click` but no DOM click, so right-click kept the card. A tiny
drag on release is still a Plotly click and still no DOM click, so a
small upward swipe on the phone kept it too. Anything that separates
the two event streams looks like a fix and is not one.

Fix: stamp the open time and have the dismiss listener ignore a click
within 400 ms of it. (L-302, gallery `700b426d`.)

Live example: gallery `700b426d`, `index.html`.
"""

# ------------------------------------------------------------- provenance
PD_VERSION_OLD = (
    "Skill version: 2.10 | Cut from palomas_orrery @ 071a0a65 (v2.10),\n"
)
PD_VERSION_NEW = (
    "Skill version: 2.11 | Cut from palomas_orrery @ 159c5a2c (v2.11),\n"
    "earlier @ 071a0a65 (v2.10),\n"
)
PD_VERSION_NOTE_ANCHOR = "| August 29, 2026\n"
PD_VERSION_NOTE = (
    "| September 8, 2026\n"
    "v2.11 adds A Drawing Approximation Does Not Promote [CRITICAL],\n"
    "directly after Measured Is the Goal, Declared Is the Fallback,\n"
    "whose direction of travel it bounds. That section says a declared\n"
    "value is promoted to a measured one as soon as it can be; this one\n"
    "says a number that was never a value -- a shape typed into a\n"
    "renderer because the render looked right -- has nothing to promote\n"
    "and must not be moved into the store. Founding case: Earth's\n"
    "magnetosphere, where a half ellipsoid with typed axes, a conic\n"
    "eccentricity typed at the call site and a sweep cap the code itself\n"
    "labels a MODE-5 KNOB were all candidates for promotion into\n"
    "constants_new.py, and Tony refused it -- \"we are not promoting\n"
    "Mode 5 approximations.\" Handle L-306.\n"
)

PD_SECTION = """## A Drawing Approximation Does Not Promote [CRITICAL]

**A number typed into a renderer because the RESULT LOOKED RIGHT is not
a constant waiting for a home. It does not promote. It is replaced, or
it stays where it is.**

This bounds the section above. That one governs a DECLARED value --
something the store already holds, standing in for a measured value
that exists. This one governs a number that was never a value at all:
a shape parameter chosen by eye, an axis ratio that made the render
read well, a sweep cap whose only justification is that the flank
stopped flaring where somebody liked it.

Moving such a number into `constants_new.py` and attaching a plausible
citation is WORSE than leaving it in the renderer, and the reason is
mechanical. The store is the thing the drift checker follows, the
thing the hover quotes to a visitor, and the thing a later session
trusts without re-deriving. Promotion launders the approximation
through all three. It is the same failure as a `# Source:` over
recalled data, one layer over -- the promotion suppresses the
suspicion that would have caught it.

**Three outcomes, and promote-as-is is not among them.**

- **Source the SHAPE it belongs to and recompute.** The number was a
  parameter of a model nobody had chosen. Choose the model, cite it,
  and the parameter comes with it or is derived from it.
- **Draw the sourced range and say so** -- the geocorona pattern. Where
  the honest object is an extent rather than an edge, draw the sourced
  figure and let the hover state what it is.
- **Remove it and note the absence.** The remove-and-note rule,
  unchanged.

**The tell:** a value whose only provenance is that a previous session
accepted the render. Mode 5 is the acceptance gate for a VISUALIZATION.
It is not a source for a NUMBER, and a value that passed it has been
looked at, not measured.

**Two things this does not forbid**, and both matter or the rule
overreaches. A DECLARED drawing choice stays legal and stays in the
store -- opacity, point count, a pick from a sourced range with its
reason on the row. And a visibility stylization still promotes when the
physical value becomes drawable, which is the chromosphere precedent
and the direction the section above sets. The line is whether there is
a real value the number is standing in FOR. A stylization stands in for
a measurement. An eyeballed shape parameter stands in for nothing.

(Tony's ruling, 2026-09-08, on Earth's magnetosphere: "We are not
promoting Mode 5 approximations," and "not promoting approximations or
rounded numbers." Seven drawn numbers in that one renderer had no store
name and every one of them was a candidate. The rebuild on a cited
model is L-305; this rule is what stopped the shortcut. It is a SKILL
rule and not a decision because it resolves the same way next month,
for a different body, in a different file.)

"""
PD_INSERT_BEFORE = "## The Status Line [CRITICAL]\n"

# ---------------------------------------------------------------- protocol
PI_HEADER_OLD = "Tony Quintanilla, PE | Claude | v3.54 | September 6, 2026\n"
PI_HEADER_NEW = "Tony Quintanilla, PE | Claude | v3.55 | September 8, 2026\n"
PI_ANCHOR_OLD = "Cut from 50cbd2df at https://github.com/tonylquintanilla/palomas_orrery\n"
PI_ANCHOR_NEW = "Cut from 159c5a2c at https://github.com/tonylquintanilla/palomas_orrery\n"

PI_ENTRY_ANCHOR = "An entry lives in exactly one place, never both.\n\n"
PI_ENTRY = """v3.55 (September 8, 2026): No rule changed in this document. TWO skill
bumps, taken BEFORE the build they serve rather than inside it.

gallery-assembler 1.2 -> 1.3 (L-304) and provenance-discipline
2.10 -> 2.11 (L-306). The assembler skill gains four field notes from
the 2026-09-07/08 gallery session -- three Plotly 2.35.2 behaviours read
out of the shipped bundle, one viewer lesson that is not Plotly's. The
provenance skill gains A Drawing Approximation Does Not Promote
[CRITICAL].

THE SEQUENCING IS THE POINT, and it is a correction to a habit rather
than to a rule. This protocol already records, twice, that a bump made
mid-build cannot be verified from inside the session that made it: the
session loads the old copy, the reinstall lands invisibly, and the
confirmation has to be written forward as an obligation the NEXT
session discharges. v3.52 did that for gallery-assembler 1.2 and v3.54
for ledger-and-session-records 1.10. Both discharged correctly. But an
obligation that travels is a check deferred, and it only works because
somebody reads the handoff.

Tony asked whether the bump could be taken first. It can, and it is
strictly better: the build session loads 1.3 and 2.11 against a
manifest that says 1.3 and 2.11, and the gate fires on something it can
actually read rather than on a promise. Nothing travels. The obligation
paragraph is absent from this entry for the first time in four
versions, and that absence is the whole of the improvement.

Two bumps in one session is not a violation of ONE SESSION, ONE BUMP.
That rule is per SKILL -- a session does not ship two versions of one
skill. Two different skills ride one protocol entry, which is what this
one is.

THE RULE ADDED TO THE PROVENANCE SKILL, in one sentence: a number typed
into a renderer because the result looked right is not a constant
waiting for a home. Earth's magnetosphere is the founding case -- a half
ellipsoid with typed axes, a conic eccentricity typed at the call site,
and a sweep cap the code itself labels a MODE-5 KNOB, all of them
candidates for promotion into constants_new.py during L-291's
migration. Tony refused it. The rebuild on a cited model is L-305; the
step-3 split that followed is in L-291.

The header stamp and the SHA anchor move with this entry. v3.52 records
that they sat stale for three versions because the correction travelled
into the version history and stopped there.

Version history: v3.52 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

# ------------------------------------------------------------------ ledger
LEDGER_EDITS = [
    (
        "<!-- L:304 status:OPEN upd:2026-09-08 section:A flag: rice:3/2/90/1 -->",
        "<!-- L:304 status:DONE upd:2026-09-08 section:C flag: rice:3/2/90/1 -->",
    ),
    (
        "**Gap:** Tony-action (do): gallery-assembler 1.2 -> 1.3 with these four\n"
        "notes, when a session next has that skill open.\n",
        "- **DONE 2026-09-08, gallery-assembler 1.3.** Taken BEFORE the build\n"
        "  rather than inside it, so the build session loads 1.3 against a\n"
        "  manifest saying 1.3 and no confirmation has to travel forward.\n"
        "  Protocol v3.55 carries the entry.\n"
        "**Gap:** none. Tony-action (do) at the time: reinstall\n"
        "gallery-assembler to the account profile (Settings > Skills) -- a\n"
        "reinstall is invisible to a running session, so nothing inside the\n"
        "bumping session could confirm it.\n",
    ),
    (
        "<!-- L:306 status:OPEN upd:2026-09-08 section:A flag: rice:4/4/85/1 -->",
        "<!-- L:306 status:DONE upd:2026-09-08 section:C flag: rice:4/4/85/1 -->",
    ),
    (
        "**Gap:** Tony-action (do): provenance-discipline 2.10 -> 2.11 carrying\n"
        "this rule, next session that opens that skill (one session, one bump),\n"
        "with the four-step binding rule -- version line, `skills_index.py`,\n"
        "protocol version-history entry, one commit.\n",
        "- **DONE 2026-09-08, provenance-discipline 2.11.** The rule landed as\n"
        "  A Drawing Approximation Does Not Promote [CRITICAL], placed after\n"
        "  Measured Is the Goal, Declared Is the Fallback, whose direction of\n"
        "  travel it bounds -- that section promotes a declared value toward a\n"
        "  measured one; this one says a number that was never a value has\n"
        "  nothing to promote. Narrowed in the same breath against the two\n"
        "  cases it would damage: a declared drawing choice stays legal, and a\n"
        "  visibility stylization still promotes. Protocol v3.55.\n"
        "**Gap:** none. Tony-action (do) at the time: reinstall\n"
        "provenance-discipline to the account profile (Settings > Skills).\n",
    ),
]


def main():
    texts = {}
    for name, md5 in FILES.items():
        lf = (ROOT / name).read_bytes().replace(b"\r\n", b"\n")
        got = hashlib.md5(lf).hexdigest()
        if got != md5:
            print("STOP: %s md5 (LF) is %s, expected %s (at 159c5a2c)." % (name, got, md5))
            print("      Either this patch already ran or the file moved. Nothing written.")
            return 1
        texts[name] = lf.decode("utf-8")

    ga = texts["skills/gallery-assembler/SKILL.md"]
    pd = texts["skills/provenance-discipline/SKILL.md"]
    pi = texts["PROJECT_INSTRUCTIONS.md"]
    hi = texts["documentation/PROJECT_INSTRUCTIONS_HISTORY.md"]
    led = texts["LEDGER_CONSOLIDATED.md"]

    checks = [
        ("assembler version line", ga, GA_VERSION_OLD),
        ("provenance version line", pd, PD_VERSION_OLD),
        ("provenance date line", pd, PD_VERSION_NOTE_ANCHOR),
        ("provenance insert anchor", pd, PD_INSERT_BEFORE),
        ("protocol header", pi, PI_HEADER_OLD),
        ("protocol SHA anchor", pi, PI_ANCHOR_OLD),
        ("protocol entry anchor", pi, PI_ENTRY_ANCHOR),
        ("history insert anchor", hi, HI_INSERT_BEFORE),
    ]
    for label, blob, needle in checks:
        if blob.count(needle) != 1:
            print("STOP: %s matched %d time(s), expected 1. Nothing written."
                  % (label, blob.count(needle)))
            return 1
    for i, (old, new) in enumerate(LEDGER_EDITS, 1):
        if led.count(old) != 1:
            print("STOP: ledger edit %d matched %d time(s), expected 1. Nothing written."
                  % (i, led.count(old)))
            return 1

    # the v3.52 block, sliced rather than embedded
    s = pi.find(V52_START)
    e = pi.find(V52_END)
    if s < 0 or e < 0 or e <= s:
        print("STOP: could not bound the v3.52 block. Nothing written.")
        return 1
    if pi.count(V52_START) != 1 or pi.count(V52_END) != 1:
        print("STOP: v3.52 block markers are not unique. Nothing written.")
        return 1
    v52 = pi[s:e]
    if len(v52) < 1500 or len(v52) > 3500:
        print("STOP: v3.52 block is %d chars, outside the expected 1500-3500. Nothing written."
              % len(v52))
        return 1

    # ---- apply
    ga = ga.replace(GA_VERSION_OLD, GA_VERSION_NEW, 1)
    if not ga.endswith("\n"):
        ga += "\n"
    ga = ga + GA_NOTES

    pd = pd.replace(PD_VERSION_OLD, PD_VERSION_NEW, 1)
    pd = pd.replace(PD_VERSION_NOTE_ANCHOR, PD_VERSION_NOTE, 1)
    pd = pd.replace(PD_INSERT_BEFORE, PD_SECTION + PD_INSERT_BEFORE, 1)

    pi = pi[:s] + pi[e:]
    pi = pi.replace(PI_HEADER_OLD, PI_HEADER_NEW, 1)
    pi = pi.replace(PI_ANCHOR_OLD, PI_ANCHOR_NEW, 1)
    pi = pi.replace(PI_ENTRY_ANCHOR, PI_ENTRY_ANCHOR + PI_ENTRY, 1)

    moved = v52 + "\n(Moved down from the resident protocol on 2026-09-08 when v3.55\nmade a fourth entry.)\n\n\n"
    hi = hi.replace(HI_INSERT_BEFORE, moved + HI_INSERT_BEFORE, 1)

    for old, new in LEDGER_EDITS:
        led = led.replace(old, new, 1)

    for blob in (ga, pd, pi, hi, led):
        blob.encode("ascii")

    out = {
        "skills/gallery-assembler/SKILL.md": ga,
        "skills/provenance-discipline/SKILL.md": pd,
        "PROJECT_INSTRUCTIONS.md": pi,
        "documentation/PROJECT_INSTRUCTIONS_HISTORY.md": hi,
        "LEDGER_CONSOLIDATED.md": led,
    }
    for name, blob in out.items():
        (ROOT / name).write_bytes(blob.encode("utf-8"))
        print("Patched %-46s md5 %s" % (name, hashlib.md5(blob.encode()).hexdigest()))
    print()
    print("gallery-assembler     1.2 -> 1.3   four field notes (L-304)")
    print("provenance-discipline 2.10 -> 2.11 a drawing approximation does not promote (L-306)")
    print("PROJECT_INSTRUCTIONS  v3.54 -> v3.55, header and SHA anchor moved,")
    print("                      v3.52 (%d chars) moved down to the history file" % len(v52))
    print("LEDGER                L-304 DONE, L-306 DONE")
    print()
    print("Next, in order:")
    print("  1. skills_index.py   (Run button) -- it owns the manifest zone")
    print("  2. ledger_index.py   (Run button)")
    print("  3. commit and push")
    print("  4. REINSTALL both skills to the account profile (Settings > Skills).")
    print("     Nothing in this session can verify that step; the next one will.")
    return 0


V52_START = "v3.52 (September 2, 2026): No rule changed in this document. One skill\n"
V52_END = "\nFunctional for Claude, readable for human, signal preserved."
HI_INSERT_BEFORE = "### Preserved verbatim: v3.29 Technical lessons (now field notes in skills)\n"


if __name__ == "__main__":
    sys.exit(main())
