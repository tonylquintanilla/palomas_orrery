"""
patch_L224_1_open_band_redesign.py

Opens L-224 -- the streamer belt band redesign -- and closes L-221,
whose only remaining condition was met at the start of this session.

WHY THIS EXISTS
    The band redesign was designed across a long conversation on
    2026-08-21 and 2026-08-22 and exists nowhere but that chat. Every
    ruling below is Tony's; none of it is in a store yet. Nothing has
    been built: solar_visualization_shells.py last changed at e1c64dc,
    and STREAMER_BELT_RADII still reads 6.0.

    L-221 closes in the same patch because its Gap reads "close once a
    session confirms its loaded copy reads 1.8," and the session that
    wrote this patch loaded ledger-and-session-records at 1.8 against a
    manifest expecting 1.8. It is the highest-scored open item in the
    ledger at 10.8, and it has been waiting on a check that has now
    fired.

WHAT IT CHANGES  (LEDGER_CONSOLIDATED.md only -- three anchored edits)
    1. Currency stamp.
    2. L-221 metadata OPEN -> DONE, section A -> C, date 2026-08-22,
       and its Gap records what discharged it. The block stays where it
       is; ledger_index.py moves it into the closed bucket itself.
    3. L-224 inserted after L-221, status OPEN, section A.

    The INDEX zone is untouched. Run ledger_index.py after -- this time
    it WILL have work, because edits 2 and 3 both change metadata
    comments, which is the only thing the indexer reads.

RICE ON L-224 -- A PROPOSAL, NOT A RULING
    Scored 3/3/85/2. Reach 3: it is the visible corona, on screen in
    every solar view. Impact 3: it replaces a wrong shape with a right
    one and retires a defended number. Confidence 85: the geometry is
    settled and sourced; the fade profile is not, and needs the render.
    Effort 2: one new shape generator, one constant rename across eight
    consumers, one hover rewrite. Change it if it reads wrong -- RICE
    is Claude's proposal and unratified by convention.

HOW TO RUN
    Save into the repo ROOT, open in VS Code, click Run. Or:

        python patch_L224_1_open_band_redesign.py

    Then:

        python ledger_index.py

    Then commit, push, and archive this script to documentation/.

PERMANENT vs DISPOSABLE
    Disposable. The two ledger blocks are the permanent half.

Built on af09de628a9d993be8436f61efba40732d689846 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written August 22, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = "LEDGER_CONSOLIDATED.md"
EXPECTED_FP = "30a503cde4d4a5784d0cb33162b4cb23"


E1_OLD = b"""by patch_L209_4), built on 031f43e7.
Review and RICE update Tony 6-21-2026
"""

E1_NEW = b"""by patch_L209_4), built on 031f43e7.
Module updated: August 22, 2026 with Anthropic's Claude Opus 5 (L-224
opened -- streamer band redesign; L-221 closed on its skill-version
condition), built on af09de62.
Review and RICE update Tony 6-21-2026
"""


E2_OLD = b"""<!-- L:221 status:OPEN upd:2026-08-20 section:A flag: rice:3/2/90/0.5 -->"""
E2_NEW = b"""<!-- L:221 status:DONE upd:2026-08-22 section:C flag: rice:3/2/90/0.5 -->"""


E3_OLD = b"""`ledger-and-session-records` 1.8 by this patch. Close once a session
confirms its loaded copy reads 1.8.
**Ref:** `skills/ledger-and-session-records/SKILL.md` "The Document
Stack"; LEDGER_CONSOLIDATED.md "RICE scoring -- prioritization for
planning"; L-220 (Stamp What You Change); L-215 (the RICE tail
measurement); L-214 (the session this surfaced in).
"""

E3_NEW = b"""`ledger-and-session-records` 1.8 by this patch. Close once a session
confirms its loaded copy reads 1.8.
**CLOSED 2026-08-22.** The condition fired. The session that closed
this loaded `ledger-and-session-records` at 1.8 against a manifest
expecting 1.8, at session start, before any ledger work -- which is
the only place that check CAN fire, because the gate is load-triggered
and a skill copy is bound when the conversation starts. Deferred
verification, carried in writing, settled against the one thing a
later session can actually read. Same structure as the SHA round trip.
**Ref:** `skills/ledger-and-session-records/SKILL.md` "The Document
Stack"; LEDGER_CONSOLIDATED.md "RICE scoring -- prioritization for
planning"; L-220 (Stamp What You Change); L-215 (the RICE tail
measurement); L-214 (the session this surfaced in); L-224 (the first
item sequenced under this ruling).

#### [L-224] Streamer belt: one warped band, not a sphere
<!-- L:224 status:OPEN upd:2026-08-22 section:A flag: rice:3/3/85/2 -->
- **What is on screen now, and why it is wrong twice.**
  `create_sun_streamer_belt_shell` draws a full sphere of points at
  `STREAMER_BELT_RADII = 6.0`. Helmet streamers form only over the
  magnetic neutral line; the poles carry coronal holes instead. So the
  sphere asserts helmets exactly where there are none. And 6.0 is not
  a boundary of anything: L-210 withdrew its 4-6 R_sun range as
  unsourced and held 6.0 as a declared drawing choice above the closed
  structure and inside the open one.
- **The physical split, from Suess & Nerney (2004), Adv. Space Res.
  33:668-675, bibcode 2004AdSpR..33..668S.** Streamers reach many
  solar radii but the CLOSED-field helmet reaches no higher than 2-4.
  Above the cusp there is a stalk -- a thin sheet along the current
  sheet with no outer edge, thinning into the slow solar wind. Source
  record: `documentation/SOURCE_suess_nerney_2004_helmet_extent_
  20260821.md`. The figure is stated there as established background
  in a modelling paper, NOT measured by it.
- **DECISION -- one trace, not two.** Both halves are band-shaped, so
  this is one object whose character changes with radius, not two
  shells. One legend entry. Splitting the legend would undo the point.
- **DECISION -- the silhouette carries the physics.** Wide and dense
  at the base along the neutral line; pinching to a minimum width at
  the cusp; thin above it. The pinch is where the loops open, which is
  a claim a paper supports, unlike "where the belt ends." It is also
  the eclipse silhouette, so it reads as familiar and is correct.
- **DECISION -- cusp at 4.0 R_sun**, the top of the stated 2-4 range.
  `STREAMER_BELT_RADII = 6.0` becomes `HELMET_CUSP_RADII = 4.0`. The
  rename is Tony's call and load-bearing: a constant named for the
  belt while holding the helmet cusp is the same name-meaning drift
  that produced the citation failure. Eight live consumers across six
  modules -- `shell_configs.py`, `comet_visualization_shells.py` and
  its hover text, `solar_visualization_shells.py`,
  `test_constants_provenance.py`. MEASURED, not assumed: the suite's
  ordering assertion holds at 4.0 (3.0 < 3.45 < 4.0 < 19.7 < 50), all
  15 tests pass with the value substituted.
- **DECISION -- the stalk attenuates and never terminates.** Opacity
  AND point density both fall with radius; the outer edge dissolves.
  This is the one non-negotiable. DeForest's 15 R_sun is the
  coronagraph's FIELD OF VIEW, not an extent, so drawing an edge there
  would repeat the withdrawn 4-6 range in pixels. Points generate to
  roughly 20 R_sun with alpha already at zero before the array ends,
  so the terminus exists in code and never on screen.
- **DECISION -- it dissolves across the Alfven surface.** 19.7 R_sun
  (L-209) is the one real boundary out there. The stalk is seen losing
  definition as it crosses from corona into wind, which makes the
  Alfven shell mean something instead of hanging alone. Hover carries
  what happens next: it does not end, it becomes the heliospheric
  current sheet and runs to the heliopause.
- **DECISION -- warp: one configuration near solar minimum**, with the
  solar-cycle sweep explained in hover rather than drawn. The swept
  envelope is the more conservative claim but smears the skirt into a
  torus that teaches nothing, and the skirt's shape is the thing that
  teaches.
- **DECISION -- the boundary is drawn, its meaning is labelled.** Two
  claims ride together and they are not the same kind. That a sharp
  brightness boundary exists is a coronagraph OBSERVATION and needs no
  further source. What it divides is an INTERPRETATION -- Suess &
  Nerney state it is reasonable to ASSUME the boundary separates fast
  coronal-hole wind from slow, and slow-wind origin is unsettled in
  the field. So draw the edge; let hover attribute the flow-regime
  reading to them as a reading. Uncertainty stays first-class.
- **DECISION -- legend renamed to "Sun: Streamer Belt."** Drop
  "(Visible Corona)": the visible corona is broader than the belt and
  separating them is the point. The legendgroup is a key in
  `shell_configs.py`, the checkbox and the tooltip, so it ripples --
  but through files this work opens anyway.
- **Where the generator goes.** `planet_visualization_utilities.py`,
  beside `create_magnetosphere_shape` and `create_bow_shock_shape`,
  same signature shape: params dict in, body-frame `(x, y, z)` out,
  caller places it. The bow-shock generator was extracted in June 2026
  from four duplicated inline copies precisely so shaped geometry has
  one home; a one-off in the shells module would undo that.
- **Mechanism note.** Plotly's `marker.opacity` is scalar, but
  `marker.color` and `marker.size` both take per-point arrays, so
  radial fade, size taper and density thinning all fit one trace and
  one legend entry.
- **Already true in the hover text, which is ahead of the picture.**
  The current hover already cites Suess & Nerney for 2-4 R_sun and
  already says the eclipse edge divides two flow regimes rather than
  plasma from vacuum. The words describe the band. Only the geometry
  is still a sphere.
**Note:** RICE is Claude's proposal, unratified. Confidence 85 rather
than higher because the fade PROFILE is unsettled -- linear will
probably read as a smear and something steeper as a stalk. Build it
adjustable and let Mode 5 pick; that is the render's call, not a
design one.
**Gap:** build it. The design is settled and sourced; nothing is
blocked and no further source read is owed. Two things want the render
rather than a decision: the fade curve, and whether the cusp pinch
reads at all at 4.0 against `INNER_CORONA_RADII` at 3.0 and
`ROCHE_LIMIT_RADII` at 3.45. Marker separation, if needed, is angular
and never radial.
**Ref:** `solar_visualization_shells.py::create_sun_streamer_belt_
shell`; `constants_new.py::STREAMER_BELT_RADII`;
`planet_visualization_utilities.py::create_magnetosphere_shape` and
`create_bow_shock_shape` (the pattern to follow);
`documentation/SOURCE_suess_nerney_2004_helmet_extent_20260821.md`;
L-210 (the withdrawn range and the held 6.0 this replaces); L-209 (the
Alfven surface it dissolves across); L-221 (the ruling that sequenced
it); `orrery-coding-conventions` (single info marker, marker
separation for near-equal radii, hover AU convention).
"""


EDITS = [
    ("1  currency stamp", E1_OLD, E1_NEW),
    ("2  L-221 metadata -> DONE / section C", E2_OLD, E2_NEW),
    ("3  L-221 closure note + L-224 block", E3_OLD, E3_NEW),
]


def fail(msg):
    print("ERROR: " + msg)
    sys.exit(1)


def main():
    if not os.path.exists(TARGET):
        fail("%s not found. Run this from the repo root." % TARGET)

    with open(TARGET, "rb") as f:
        data = f.read()
    original_len = len(data)

    normalized = data.replace(b"\r\n", b"\n")
    fp = hashlib.md5(normalized).hexdigest()
    if fp != EXPECTED_FP:
        print("ERROR: BASE MOVED. %s is not the file this patch was "
              "built against." % TARGET)
        print("  expected fingerprint : " + EXPECTED_FP)
        print("  this file            : " + fp)
        print("  size                 : %d bytes" % original_len)
        print("  Nothing was written.")
        sys.exit(1)

    is_crlf = data.count(b"\r\n") > 0
    print("base ok: fingerprint %s, %d bytes, line endings %s"
          % (fp, original_len, "CRLF" if is_crlf else "LF"))

    for label, _old, new in EDITS:
        bad = [b for b in new if b > 127]
        if bad:
            fail("edit %s would insert %d non-ASCII byte(s). Refusing."
                 % (label, len(bad)))
    print("note: %s holds %d non-ASCII byte(s) before and after"
          % (TARGET, len([b for b in normalized if b > 127])))

    working = data
    for label, old, new in EDITS:
        o, n = old, new
        if is_crlf:
            o = o.replace(b"\n", b"\r\n")
            n = n.replace(b"\n", b"\r\n")
        count = working.count(o)
        if count != 1:
            print("ANCHOR FAIL on edit %s: expected exactly 1 match, "
                  "found %d." % (label, count))
            print("  anchor began: %r" % o[:70])
            print("  Nothing was written.")
            sys.exit(1)
        working = working.replace(o, n)
        print("ok   edit %s  (+%d bytes)" % (label, len(n) - len(o)))

    with open(TARGET, "wb") as f:
        f.write(working)
    print("patch applied (%d bytes, was %d)" % (len(working), original_len))

    with open(TARGET, "rb") as f:
        rb = f.read().replace(b"\r\n", b"\n")

    checks = [
        ("L-224 heading present",
         b"#### [L-224] Streamer belt: one warped band, not a sphere", 1),
        ("L-224 metadata parses as OPEN / section A",
         b"<!-- L:224 status:OPEN upd:2026-08-22 section:A "
         b"flag: rice:3/3/85/2 -->", 1),
        ("L-224 has exactly one Gap",
         b"**Gap:** build it. The design is settled", 1),
        ("cusp decision recorded",
         b"**DECISION -- cusp at 4.0 R_sun**", 1),
        ("rename decision recorded",
         b"becomes `HELMET_CUSP_RADII = 4.0`", 1),
        ("no-terminus rule recorded as non-negotiable",
         b"This is the one non-negotiable.", 1),
        ("warp decision recorded",
         b"**DECISION -- warp: one configuration near solar minimum**", 1),
        ("legend rename recorded",
         b'**DECISION -- legend renamed to "Sun: Streamer Belt."**', 1),
        ("L-221 now reads DONE / section C",
         b"<!-- L:221 status:DONE upd:2026-08-22 section:C "
         b"flag: rice:3/2/90/0.5 -->", 1),
        ("no L-221 metadata still reads OPEN",
         b"<!-- L:221 status:OPEN", 0),
        ("L-221 closure names what discharged it",
         b"**CLOSED 2026-08-22.** The condition fired.", 1),
        ("currency stamp added",
         b"Module updated: August 22, 2026 with Anthropic's Claude "
         b"Opus 5 (L-224", 1),
        ("INDEX zone untouched -- no L-224 row yet",
         b"| L-224 |", 0),
    ]

    print("")
    print("verification, %d checks, each read back from disk:" % len(checks))
    failures = 0
    for desc, needle, want in checks:
        got = rb.count(needle)
        if got != want:
            failures += 1
        print("  %s  %s  (found %d, expected %d)"
              % ("PASS" if got == want else "FAIL", desc, got, want))

    if failures:
        print("")
        print("ERROR: %d check(s) failed AFTER writing. Restore "
              "LEDGER_CONSOLIDATED.md from git and report this."
              % failures)
        sys.exit(1)

    print("")
    print("NEXT: python ledger_index.py -- and unlike the last patch it")
    print("WILL have work this time, because edits 2 and 3 both changed")
    print("metadata comments, which is the only thing the indexer reads.")
    print("Expect an L-224 row to appear and L-221 to move to closed.")
    print("Then commit, push, and archive this script to documentation/.")


if __name__ == "__main__":
    main()
