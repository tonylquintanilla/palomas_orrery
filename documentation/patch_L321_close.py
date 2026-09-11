"""patch_L321_close.py -- close of the 2026-09-10 session: the ledger, the
master plan (v30) and the handoff. Replaces patch_L321_ledger.py, which
Tony held and which must not be run.

ORRERY repo (palomas_orrery). Built on orrery b2c77350 at
https://github.com/tonylquintanilla/palomas_orrery ; gallery state
recorded is 9c056d1a at
https://github.com/tonylquintanilla/tonyquintanilla.github.io

Run: save this file in the orrery repo root (beside LEDGER_CONSOLIDATED.md),
open it in VS Code, click Run.  Or from a terminal in the repo root:
    python patch_L321_close.py

What it does, all-or-nothing -- three files or none:
  LEDGER_CONSOLIDATED.md
    - header stamp;
    - L-318: the arrow takes the marker's outline colour (built) and
      passed Mode 5 ("perfect"); the Gap narrows to the marker-tap pointer;
    - L-320: DONE on Tony's Mode 5, moved to the end of section C;
    - L-321 opened on Tony's ruling: the orrery's hover text joins the
      provenance braid, Earth first, with the discovery counts.
  documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md
    - v29 -> v30; Section 5a gains the 2026-09-10 evening subsection.
      Appended, not merged. The plan carries sequencing; status stays in
      the ledger.
  documentation/HANDOFF_L316_L321_20260910.md
    - new: this session's handoff.

Guards: the ledger's text outside its generated INDEX zone and the plan's
text, line endings normalised, must match b2c77350; the handoff must not
exist yet. Windows line endings are kept.

Permanent: the three files. Disposable: this script.
Success prints one 'ok' per step and 'patch applied'. Any failure prints
one ERROR / ANCHOR FAIL line and writes nothing.
Undo is Discard Changes in GitHub Desktop (and delete the new handoff).

Then run ledger_index.py -- expect
"OK: 316 L-blocks parsed, no consistency problems."

Written September 10, 2026 with Anthropic's Claude Opus 5.
"""
import hashlib, os, sys

LEDGER = "LEDGER_CONSOLIDATED.md"
PLAN = os.path.join("documentation", "MASTER_PLAN_INTERACTIVE_GALLERY.md")
HANDOFF = os.path.join("documentation", "HANDOFF_L316_L321_20260910.md")
INDEX_START = b"<!-- INDEX:START"
INDEX_END = b"<!-- INDEX:END -->"
FP_LEDGER_BASE = "d6a7a2899747439c15f09f339d5a68fa"
FP_L320_BLOCK = "ead98a43a8556aa0ebc18571123b490a"
FP_LEDGER_FINAL = "1c091651196ff91f5d466ff60e7d0b1f"
FP_PLAN_BASE = "e3b4b9b8d320bc2a09133ffca7922e44"
FP_PLAN_FINAL = "bce59a17f170a079ac65285075994f57"

STAMP = (b"""(L-318 designed in conversation and built in the gallery: naming a shell
in the drawer opens its hover text as a label), built on b914c3f0.
""", b"""(L-318 designed in conversation and built in the gallery: naming a shell
in the drawer opens its hover text as a label), built on b914c3f0.
Module updated: September 10, 2026 with Anthropic's Claude Opus 5
(session close: L-318's arrow colour built and through Mode 5; L-320
closed on Tony's Mode 5; L-321 opened on Tony's ruling -- the orrery's
hover text joins the provenance braid, Earth first), built on b2c77350.
""")

L318 = (b"""**Gap:** Tony's Mode 5 on the phone, both rooms: name a shell and its
label points at its marker; turn the view and the label stays with it;
tap the scene and it closes; untick the shell and it closes. Then the
marker-tap pointer question above.
""", b"""- **Mode 5 passes on the phone, 2026-09-10.** Tony, to each check: name
  a shell and its label points at its marker -- "correct"; turn the view
  and it stays -- "correct"; tap the scene and it closes -- "correct";
  untick and it closes -- "correct"; tapping a marker works as before --
  "correct"; the label's size settings -- "they are correct".
  [render-confirmed Mode 5 @ gallery `ffcf1630`]
- **One change from the same look.** Tony: "i would make the arrow the
  color of the marker for contrast." The marker's fill is the shell's
  colour, which the arrow already had, so the colour that contrasts is
  the marker's outline. Built 2026-09-10 by
  `patch_L318_2_arrow_colour.py` in the gallery: the arrow takes the
  marker's outline colour, red or white under the two-standards rule,
  and the box border keeps the shell's colour. The label checks gained
  one, now 20: a white-outlined marker gets a white arrow and a
  red-outlined one a red arrow. [verified in the sandbox; render-gated]
- **The arrow colour passes on the phone, 2026-09-10.** Tony: "perfect".
  [render-confirmed Mode 5 @ gallery `9c056d1a`]
**Gap:** the marker-tap pointer question above.
""")
L320_META = (b"""<!-- L:320 status:OPEN upd:2026-09-10 section:A flag: rice:3/2/80/1 -->""",
             b"""<!-- L:320 status:DONE upd:2026-09-10 section:C flag: rice:3/2/80/1 -->""")
L320_GAP = (b"""**Gap:** Mode 5 on the phone, both rooms: a marker at the top of a zoomed
shell reads clear of the axis line.
""", b"""- **CLOSED 2026-09-10 on Tony's Mode 5:** a marker at the top of a
  zoomed shell reads clear of the axis line -- "desktop and phone are
  correct". [render-confirmed Mode 5 @ gallery `ffcf1630`] No loose ends:
  the gallery's steps differing from the orrery's per-shell angles is
  Tony's ruling, not open work.
**Gap:** none.
""")

SECTION_C_END = b"""`documentation/HANDOFF_L310_camera_step_20260910.md` (orrery).
## D. RECONCILED LEDGER -- OPEN"""
L321 = b"""#### [L-321] The orrery's hover text joins the provenance braid, Earth first
<!-- L:321 status:OPEN upd:2026-09-10 section:A flag: rice:3/3/60/3 -->
- **Found 2026-09-10, after the drawer label passed Mode 5.** Tony: "are
  these the same hovertext that are built for the orrery?" No. The
  orrery gives each shell a hand-written description -- `hover_text` in
  `shell_configs.py`, or an `*_info_hover` string in its shell module --
  which `build_sphere_shell` puts under "Body: Shell". The gallery
  composes its text from the served, provenance-checked row
  (`renderShellSet`): the name, the radius in body radii and in km and
  AU, the altitude where it applies, the `source` line and a short
  `note`. [verified @ orrery `436fa647` and gallery `ffcf1630`]
- **Tony's ruling, 2026-09-10:** "no, i don't want the orrery hovertext
  to come over. if anything we should do the reverse, pass the text that
  has gone through the provenance scanner only. L-321 should be
  integrated into the provenance braid. as we ensure that the
  interactive is correct, we should make sure that the orrery is
  correct. the orrery hovertext are fuller, which is interesting, but
  accuracy is more important. so for now, let's do this for Earth."
- **Discovery for the Earth slice, from `PROVENANCE_AUDIT.md` at orrery
  `b2c77350`.** 36 display strings hold Earth's hover text, none Tier 1,
  all Tier 2 at score 12. In `earth_visualization_shells.py`, 22 strings
  and 100 claims: 20 cited but not independently cross-checked, 2 of
  them date-sensitive. Inside Earth's two entries in `shell_configs.py`,
  14 strings and 54 claims: 7 cited only through an enclosing block
  citation, 5 cited but not cross-checked, 2 date-sensitive. Several are
  pairs, a shell's `hover_text` and `tooltip` carrying the same claims.
  The instance lists are those two files' sections of the audit. Cited
  is not the same as true: the cross-check is the gap Tony's ruling
  names. [read @ orrery `b2c77350`]
- **The shape of the slice, per the braid (provenance-discipline 2.11).**
  Discovery is done and fixed nothing; remediation comes in slices,
  beside the delivery work and not as a gate in front of it. Accuracy
  wins over fullness: a claim that cannot be sourced is removed and the
  gap noted, not kept because the prose reads well. Nothing moves from
  the orrery into the gallery; text that moves the other way has been
  through the scanner.
- **Note:** RICE 3/3/60/3 -> 1.8 proposed, not confirmed. One class row
  for Earth's slice; other bodies' hover text waits for its own.
**Gap:** design round for Earth's cross-check -- which of the 36 strings
first, how the worksheet pipeline takes them, and what a corrected string
looks like when a claim goes. Then remediation in slices.
**Ref:** L-317, L-318, L-320, `PROVENANCE_AUDIT.md`, `WORKSHEET_CHECK.md`,
`shell_configs.py` (`hover_text`, `tooltip`), `earth_visualization_shells.py`,
`orrery_rendering.py` (`build_sphere_shell`), `gallery/feature_renderers.js`
(`renderShellSet`), skills/provenance-discipline/SKILL.md (the braid).

"""
L278 = b"""#### [L-278] A relayout from inside a Plotly event handler re-enters the update machinery"""

PLAN_STATUS = (b"""**Status:** v29 -- Phase 2""", b"""**Status:** v30 -- Phase 2""")
PLAN_UPDATED = (b"""**Last updated:** September 10, 2026 (v29: the Earth BUILD closes.""",
b"""**Last updated:** September 10, 2026, evening (v30: L-305's paper read
landed, corrected; the camera-step track closed on Mode 5 and the phone
look that closed it added four chrome items, two of them solutions the
orrery already had; the orrery's hover text joins the braid, Earth first
(L-321); Section 5a gains the 2026-09-10 evening subsection; with
Anthropic's Claude Opus 5. v29, September 10, 2026: the Earth BUILD closes.""")
PLAN_SECTION = (b"""### What this section deliberately does not carry
""", b"""### 2026-09-10 (evening) -- the rooms' chrome after the phone, and the orrery's hover text joins the braid

Measured at orrery `b2c77350` and gallery `9c056d1a`, both confirmed
against the live remotes. Appended, not merged.

**L-305's paper read landed, corrected.** The Jelinek 2012 read and
Tony's split -- Shue (1998) for the magnetopause, Jelinek for the bow
shock -- are in the ledger. The session's design record could not be
pasted as written: its new item took a handle L-310 had already used,
and its replacement Gap dropped two open lines. The solar-wind item
became L-314, and why three chained patches refused became L-315.
L-305's build is unchanged in the order: read Shue's flaring
coefficients, then the port.

**The camera-step track closed and grew four items** (L-310, L-316,
L-317, L-318, L-320). The arrows passed Mode 5. The phone look that
closed them moved the cross to the top right with the title kept,
carried the orrery's two-standards marker outline into the gallery,
started every marker five degrees off the pole, and added a label that
opens when a shell is named in the drawer, pinned to its marker with an
arrow. Twice the fix already existed in the orrery and the interactive
had never received it (L-317, L-320); the first build of L-317 went the
wrong way until Tony said so.

**The orrery's hover text joins the braid** (L-321). The gallery's hover
text is built from served, provenance-checked rows; the orrery's is
fuller hand-written prose. Tony ruled against carrying the prose over:
accuracy over fullness, the orrery must be as correct as the
interactive, and the slice starts with Earth. Discovery at orrery
`b2c77350`: 36 display strings, none Tier 1, all cited but not
independently cross-checked.

**What this does to the order.** The five segments do not move. The
braid gains an orrery slice for Earth's hover text, worked beside the
delivery work and not in front of it: discovery is done, a design round
for the cross-check is next. L-305's build and L-318's last question (a
marker tap's own hover box still drops its pointer mid-screen) are the
Earth room's open data and chrome items; L-316's desktop look and
L-319's call are Tony's. Handoff:
`documentation/HANDOFF_L316_L321_20260910.md` in the orrery repo.

### What this section deliberately does not carry
""")
HANDOFF_TEXT = """# L-305 landed; L-310 closed; L-313 to L-321 -- the rooms' chrome after the phone

Built on orrery `5fea17955d5f2d57f8426da8446d7d1b76f7274f`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `4506fb48b8056e87cb4db439bdda90e0b0e116ce`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
(the session's first reads). Pushed at: gallery `9c056d1a`; orrery
`b2c77350` plus the commit carrying `patch_L321_close.py` (the next
session reads it from `git log`).

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-10
Type: BUILD + DESIGN (targeted patches, Mode 5 on the phone and desktop,
ledger, master plan v30). Protocol v3.56. Handles: L-305, L-310, L-313
to L-321.

## STEP 0 -- Gates for the next session

- Skills loaded this session, each matching the manifest:
  ledger-and-session-records 1.11 (the v3.56 obligation discharged),
  safe-file-editing 1.10, provenance-discipline 2.11,
  orrery-coding-conventions 1.7, gallery-assembler 1.3,
  interactive-exhibit 1.1, agentic-pre-test 1.2. No skill was bumped;
  nothing travels.
- `git ls-remote` both repos. Orrery one commit past `b2c77350`; gallery
  at `9c056d1a` unless the nightly run has committed since.

## WHAT HAPPENED

1. **L-305's patches refused, and one patch replaced them.** The brief
   and citation patches were fingerprinted between `ledger_index.py`
   runs and hashed raw bytes; the design record's new item took L-313,
   which L-310 had opened. `patch_L305_amendment.py` landed the paper
   read and Tony's Shue/Jelinek split, with the solar-wind item as L-314,
   the dropped Gap lines restored, and Shue's flaring coefficients marked
   unread. The refusal class is L-315.
2. **L-310 closed on Mode 5.** The camera steps passed on the phone.
3. **L-316, two rounds.** Round 1 put the arrow cross top-centre and
   dropped the title; it hid the marker at the top of a zoomed shell.
   Round 2 kept the title and moved the cross top-right on portrait
   phones. Passed on the phone; desktop not yet looked at.
4. **L-317.** A first build filled markers white and larger; Tony: the
   orrery already solves this. The gallery now serves the orrery's
   two-standards outline flags (white on saturated warm shells). Passed.
5. **L-320.** The orrery sets per-shell marker angles; the gallery steps
   20 degrees from the pole. Tony: keep the gallery's steps, shift all 5
   degrees. Nine markers left the axis; the terminator's steps along its
   line. Closed on Mode 5, desktop and phone.
6. **L-318.** Naming a shell in the drawer opens its hover text as a
   label pinned to its marker (a Plotly scene annotation); a tap in the
   scene or unticking closes it; the arrow takes the marker's outline
   colour. Passed on the phone.
7. **L-319 and L-321 opened.** L-319: focusing a smaller shell cuts
   larger lit shells at the box. L-321: Tony ruled that the orrery's
   fuller hover text does not come over; instead it joins the provenance
   braid, Earth first. Discovery: 36 display strings, none Tier 1, all
   cited but not cross-checked.

## LESSONS WORTH CARRYING

- **Check the orrery first.** Twice this session the interactive lacked
  a solution the orrery already had (L-317, L-320). The skill a gallery
  session loads for markers states neither; L-317's Gap carries the fix.
- **Plotly 2.35.2, read from its source.** A hover box keeps its pointer
  only when it fits on one side of its point (`fx/hover.js`). A 3D replot
  re-applies the camera stored in the layout (`gl3d/scene.js`,
  `setViewport`), which a touch rotation never updates: send the live
  camera with any scene relayout. `layout.scene.annotations` anchor to a
  3D point with an arrow.
- **Ledger patches fingerprint the text outside the INDEX zone, line
  endings normalised** (L-315). A chain that runs the indexer between
  patches refuses otherwise.

## OPEN

Order is Tony's; listed by what each waits on.

1. **L-305** -- read Shue et al. (1998) for the flaring coefficients and
   confirm Jelinek's values against the PDF; then the port.
2. **L-321** -- design round for Earth's hover-text cross-check: which of
   the 36 strings first, how the worksheet pipeline takes them, what a
   corrected string looks like when a claim goes.
3. **L-318** -- a marker tap's own hover box drops its pointer mid-screen
   at `HOVER_WIDTH` 70; narrowing trades a taller box.
4. **L-316** -- the desktop look; then interactive-exhibit's nav cluster
   row at its next bump.
5. **L-317** -- orrery-coding-conventions at its next bump: the
   two-standards rule, and the example corrected to the factory.
6. **L-319** -- Tony's call on the cut at the box.
7. **L-313** recentering design round; **L-314** live solar wind after
   L-305; **L-315** field note at safe-file-editing's next bump.

## TONY-ACTION ROLLUP

1. **(do)** Orrery root: run `patch_L321_close.py` (Run), then
   `ledger_index.py` (Run). Expect "OK: 316 L-blocks parsed, no
   consistency problems." Delete the held `patch_L321_ledger.py` without
   running it.
2. **(do)** Commit and push the orrery; report the SHA.
3. **(do)** Look at L-316 on the desktop: title and cross as before.
4. **(do)** Keep the Jelinek 2012 PDF where the L-305 session can read it.
5. **(decide)** L-319: keep the cut at the box as a cutaway, or another
   answer.
6. **(decide)** L-316's date question: whether the Earth room's date
   needs a visible place in the frame.

Written September 2026 with Anthropic's Claude Opus 5.
"""


def body_fp(lf):
    if lf.count(INDEX_START) != 1 or lf.count(INDEX_END) != 1:
        return None
    a = lf.index(INDEX_START)
    b = lf.index(INDEX_END) + len(INDEX_END)
    return hashlib.md5(lf[:a] + lf[b:]).hexdigest() if b > a else None


def edit_ledger(lf, steps):
    def one(pair, name):
        nonlocal lf
        n = lf.count(pair[0])
        if n != 1:
            raise ValueError("ANCHOR FAIL: ledger -- %s expected 1 match, got %d" % (name, n))
        lf = lf.replace(pair[0], pair[1])
        steps.append("ledger -- " + name)
    one(STAMP, "header stamp")
    one(L318, "L-318 arrow colour built and passed")
    head = b"#### [L-320]"
    if lf.count(head) != 1:
        raise ValueError("ANCHOR FAIL: ledger -- L-320 header")
    i = lf.index(head)
    j = lf.find(b"\n#### [", i + len(head)) + 1
    block = lf[i:j]
    if hashlib.md5(block).hexdigest() != FP_L320_BLOCK:
        raise ValueError("ERROR: ledger -- L-320's block is not the one at b2c77350")
    lf = lf[:i] + lf[j:]
    for pair, name in ((L320_META, "L-320 status DONE, section C"), (L320_GAP, "L-320 closing record")):
        if block.count(pair[0]) != 1:
            raise ValueError("ANCHOR FAIL: ledger -- %s" % name)
        block = block.replace(pair[0], pair[1])
        steps.append("ledger -- " + name)
    block = block.rstrip(b"\n") + b"\n"
    one((SECTION_C_END, b"`documentation/HANDOFF_L310_camera_step_20260910.md` (orrery).\n\n" + block +
         b"## D. RECONCILED LEDGER -- OPEN"), "L-320 moved to the end of section C")
    one((L278, L321 + L278), "L-321 opened")
    return lf


def edit_plan(lf, steps):
    for pair, name in ((PLAN_STATUS, "status v30"), (PLAN_UPDATED, "last-updated line"),
                       (PLAN_SECTION, "Section 5a subsection, 2026-09-10 evening")):
        n = lf.count(pair[0])
        if n != 1:
            raise ValueError("ANCHOR FAIL: plan -- %s expected 1 match, got %d" % (name, n))
        lf = lf.replace(pair[0], pair[1])
        steps.append("plan -- " + name)
    return lf


def read(path):
    with open(path, "rb") as f:
        raw = f.read()
    return raw.replace(b"\r\n", b"\n"), b"\r\n" in raw


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    fl, fp_, fh = (os.path.join(root, p) for p in (LEDGER, PLAN, HANDOFF))
    for p in (fl, fp_):
        if not os.path.exists(p):
            print("ERROR: not found: %s (run from the orrery repo root)" % p); return 1
    if os.path.exists(fh):
        print("ERROR: %s already exists -- already applied?; nothing written" % HANDOFF); return 1
    led, led_crlf = read(fl)
    plan, plan_crlf = read(fp_)
    got = body_fp(led)
    if got == FP_LEDGER_FINAL:
        print("ERROR: the ledger already carries this patch; nothing written"); return 1
    if got != FP_LEDGER_BASE:
        print("ERROR: %s does not match b2c77350 outside the index (got %s); nothing written" % (LEDGER, got)); return 1
    if hashlib.md5(plan).hexdigest() != FP_PLAN_BASE:
        print("ERROR: %s does not match b2c77350; nothing written" % PLAN); return 1
    steps = []
    try:
        led = edit_ledger(led, steps)
        plan = edit_plan(plan, steps)
    except ValueError as e:
        print(str(e) + "; nothing written"); return 1
    ho = HANDOFF_TEXT.encode("ascii")
    for name, data in (("ledger", led), ("plan", plan), ("handoff", ho)):
        if sum(1 for c in data if c > 127):
            print("ERROR: non-ASCII in the %s; nothing written" % name); return 1
    if body_fp(led) != FP_LEDGER_FINAL or hashlib.md5(plan).hexdigest() != FP_PLAN_FINAL:
        print("ERROR: result does not match the tested result; nothing written"); return 1
    for s in steps:
        print("ok  %s" % s)
    with open(fl, "wb") as f:
        f.write(led.replace(b"\n", b"\r\n") if led_crlf else led)
    with open(fp_, "wb") as f:
        f.write(plan.replace(b"\n", b"\r\n") if plan_crlf else plan)
    with open(fh, "wb") as f:
        f.write(ho)
    print("ok  wrote %s" % HANDOFF)
    print("stamped header: %s" % LEDGER)
    print("stamped header: %s" % PLAN)
    print("patch applied (3 files)")
    print('next: run ledger_index.py -- expect "OK: 316 L-blocks parsed, no consistency problems."')
    return 0


if __name__ == "__main__":
    sys.exit(main())
