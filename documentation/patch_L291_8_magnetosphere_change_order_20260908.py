"""
patch_L291_8_magnetosphere_change_order_20260908.py -- design session close

Built on orrery 20750034c9fab71b7495bfca50f4039b699cd5c4
at https://github.com/tonylquintanilla/palomas_orrery (main)
and gallery 700b426d4cecc1f80fd6f9ca5758e5058ea497a6
at https://github.com/tonylquintanilla/tonyquintanilla.github.io (main).
Both confirmed against the live remotes before this was written.

RUN THIS BEFORE ledger_index.py. The ledger at 20750034 is byte-identical
to what patch_L291_7 printed, so ledger_index.py has NOT been run yet:
the index zone does not list L-301..L-304 and the two DONE blocks have
not migrated to section C. Running this patch first means ONE index
regeneration covers both patches.

WHAT THIS DOES (two files in the ORRERY repo, applied only if both guards pass)

LEDGER_CONSOLIDATED.md
  Updates: L-291 (step 3 proceeds on the eleven sourced features; the
                  magnetosphere renderer is deferred to L-305),
           L-303 (RULED -- separate cards per orientation; the header and
                  the Gap change from "Tony to decide" to the build).
  Adds:    L-305 Earth's magnetosphere rebuilt on a sourced model
           L-306 Do not promote a drawing approximation into the store
           L-307 Export-age reporting for the surviving static cards
           L-308 A shell-legend surface for static cards (deferred)
  Then Tony runs ledger_index.py.

documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md -> v28
  The status line said step 3 is next without qualification; the design
  round split it. Section 5a gains the 2026-09-08 evening subsection.
  Restamp reason: a DESIGN BUILD (zero code), which is the countable
  unit the ledger skill 1.10 names. The rolling stamp keeps three and
  drops v25 and v24.

Handles: highest at 20750034 is L-304; the four new ones are the next
four. Re-checked before writing.

Written September 2026 with Anthropic's Claude Opus 5.
"""
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FILES = {
    "LEDGER_CONSOLIDATED.md": "1c224fcc7b0da47a0c7d5dfa091aa006",
    "documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md": "c5588ca23ace45fd5b8ed0d99c06c400",
}
EXPECTED_MAX_HANDLE = 304

LEDGER_EDITS = [
    # ---- L-291: the Gap splits ----
    (
        "**Gap:** STEP 3 -- the `EXHIBIT === \"earth\"` branch in\n"
        "`interactive.html` (driver spec: objects Earth + Moon, center Earth,\n"
        "half-range floor 6.155e-5 AU; eight shells lit on arrival; axis,\n"
        "equator plane, Sun direction on), the GEO ring and magnetosphere\n"
        "renderers, the terminator as geometry, the Moon's orbit with the\n"
        "trust-window arc, the frozen-epoch hovers, the `sun*` chrome by\n"
        "parameter, i-panel copy with sources. Then steps 4-8. Closes on\n"
        "Tony's eyes.\n",
        "- **Tony's ruling, 2026-09-08 (design round, zero code) -- STEP 3\n"
        "  PROCEEDS WITHOUT THE MAGNETOSPHERE.** Eleven of Earth's thirteen\n"
        "  drawn features are sourced and read MATCH. The two magnetosphere\n"
        "  features turned out to be pre-provenance DRAWING, not sourced\n"
        "  geometry, and rebuilding them on a cited model is a build of its\n"
        "  own (L-305). Holding a well-understood step behind an open\n"
        "  modelling question couples them; the exhibit ships with the\n"
        "  magnetosphere ABSENT AND NAMED rather than approximate. Tony's\n"
        "  framing: this is a layperson's learning tool, not a research\n"
        "  tool, and a learning tool may say \"not drawn yet\" without\n"
        "  failing its purpose.\n"
        "- **What that does to the smoke fixture.** The two pinned expected\n"
        "  warnings become ONE, not zero: `earth_geostationary` gets its\n"
        "  renderer in step 3, `earth_magnetosphere` stays a named,\n"
        "  expected absence until L-305 lands. An absence the dispatch\n"
        "  names is the check working.\n"
        "**Gap:** STEP 3, six items -- the `EXHIBIT === \"earth\"` branch in\n"
        "`interactive.html` (driver spec: objects Earth + Moon, center Earth,\n"
        "half-range floor 6.155e-5 AU; eight shells lit on arrival; axis,\n"
        "equator plane, Sun direction on), the GEO ring renderer, the\n"
        "terminator as geometry, the Moon's orbit with the trust-window arc,\n"
        "the frozen-epoch hovers, the `sun*` chrome by parameter, i-panel\n"
        "copy with sources. The magnetosphere renderer is NOT in this step;\n"
        "see L-305. Then steps 4-8. Closes on Tony's eyes.\n",
    ),
    # ---- L-303: ruled ----
    (
        "#### [L-303] One card with two files, or one card per orientation? (Tony to decide)\n"
        "<!-- L:303 status:OPEN upd:2026-09-08 section:A flag: rice:3/3/60/2 -->\n",
        "#### [L-303] Separate cards per orientation (RULED); the phone hides a landscape card that has a portrait sibling\n"
        "<!-- L:303 status:OPEN upd:2026-09-08 section:A flag: rice:4/4/80/3 -->\n",
    ),
    (
        "- Options: (a) keep one card, improve the editor's display of the two\n"
        "  files (show both shapes, per-file dates); (b) one card per\n"
        "  orientation, restore device filtering in the viewer, and undo the\n"
        "  three merges of L-301; (c) something else.\n"
        "**Gap:** Tony-action (decide). No build until ruled.\n"
        "**Ref:** L-287, L-301, L-286, `tools/gallery_editor.py`, index.html.\n",
        "- Options were: (a) keep one card, improve the editor's display of\n"
        "  the two files; (b) one card per orientation, restore device\n"
        "  filtering, undo the three merges of L-301; (c) something else.\n"
        "- **TONY'S RULING, 2026-09-08: (b), and the merge was never his.**\n"
        "  The two-card model was HIS workflow until L-287 replaced it on\n"
        "  2026-09-04 and paired 38 existing cards by title. He is being\n"
        "  asked to accept editor work whose only purpose is to make a merge\n"
        "  he did not request legible again. His words on the cost: \"the\n"
        "  issue of clutter is mine.\"\n"
        "- **The filter is NARROWER than the pre-L-287 device model.** Not a\n"
        "  per-card device tag. ONE rule: on a phone, hide a landscape card\n"
        "  IF IT HAS A PORTRAIT SIBLING. A landscape card with no sibling\n"
        "  still shows on the phone and still sweeps, which is the majority\n"
        "  of cards and the case the sweep exists for. Desktop shows\n"
        "  everything. Tony's correction, and it matters: he sees both views\n"
        "  on desktop, only the mobile view on mobile.\n"
        "- **The sibling flag is stamped by the CONVERTER, not matched at\n"
        "  render time.** L-301's pairing detection is kept and INVERTED:\n"
        "  same rule, different action -- create a separate card and stamp\n"
        "  the relationship on both, instead of joining into an empty slot.\n"
        "  The L-301 work is not wasted.\n"
        "- **The editor work from option (a) EVAPORATES.** Per-slot\n"
        "  `converted` dates, derived per-slot shape, and greying the shape\n"
        "  radio on a paired card were all needed only because two files\n"
        "  shared one card. One card, one file, one date, one shape, and the\n"
        "  16:9 / 9:16 radio is meaningful again on every card.\n"
        "- **What the radio actually does, checked at gallery `700b426d`:**\n"
        "  `sweepWanted()` in index.html returns false on `shape === '9:16'`,\n"
        "  so 16:9 IS the enable switch for the 2D landscape sweep on a\n"
        "  phone. Three further conditions gate it and none is a control:\n"
        "  phone width, portrait orientation, no portrait sibling, and\n"
        "  `layout.scene` absent (the 3D exclusion).\n"
        "- **The surviving population, Tony 2026-09-08:** the static card\n"
        "  system is not going away for the 16:9 2D exhibits -- the Earth\n"
        "  science cards and the star cards. The shell-heavy 3D bodies are\n"
        "  the ones migrating to interactive exhibits. So the split\n"
        "  migration is transitional work on a SHRINKING set, and the sweep\n"
        "  is the mechanism that keeps the PERMANENT set working on a phone.\n"
        "**Gap:** build it -- the converter's inverted pairing and sibling\n"
        "stamp; the one viewer rule; the split migration of L-287's 38 pairs\n"
        "plus L-301's 3. One known loss to accept: two of L-301's three\n"
        "merges had titles typed differently between L and P and the\n"
        "landscape title survived, so those portrait titles are gone and get\n"
        "retyped. Tony-action (do) at that point, not now.\n"
        "**Ref:** L-287, L-301, L-286, L-307, L-308, `tools/json_converter.py`,\n"
        "`tools/gallery_editor.py`, index.html.\n",
    ),
]

NEW_BLOCKS = """#### [L-305] Earth's magnetosphere rebuilt on a sourced model, orrery and assembler together
<!-- L:305 status:OPEN upd:2026-09-08 section:A flag: rice:4/4/60/4 -->
- **Where this came from.** A design round on 2026-09-08 opened with one
  hover requirement from the L-291 handoff -- say that the tail is drawn
  to 100 radii against a real one past 1,000 -- and ended with two stored
  constants superseded, a miscitation found, and step 3 split. The
  handoff had framed the magnetosphere renderer as a small step-3 item.
  It is not, and the next session will read that framing first.
- **What was checked, at orrery `af4c604e`.** The orrery does NOT use
  Shue for the magnetopause. `create_magnetosphere_shape` is a half
  ELLIPSOID -- sunward 10, equatorial radius 12, polar radius 10 -- so
  not even a surface of revolution, with a separate flared cylinder tail
  (base 15, end 25, length 100) butted on at the terminator. The bow
  shock is a conic through `create_bow_shock_shape` with
  `eccentricity=1.05` typed at the call site and a sweep capped at 0.92
  of the asymptote, a literal the code itself labels a MODE-5 KNOB. An
  11 degree dipole tilt is applied via `rotate_to_sunward`. Seven drawn
  numbers there have no store name; L-291's "no drawn literal remains"
  was true of the shells, not of the magnetosphere.
- **Tony's ruling: none of that gets promoted.** Those are Mode 5
  approximations -- shapes chosen because they looked right. Promoting
  them into `constants_new.py` would launder an approximation into a
  sourced constant. See L-306, which is that rule stated generally.
- **Farris & Russell (1994) is a MISCITATION for a shape.** The bow
  shock constant's Note cites it as "Model form". Its abstract is a
  semiempirical Mach-number relation for the STANDOFF DISTANCE; obstacle
  shape is an input to it, not an output. Remove the claim.
- **The model taken: Jelinek, Nemecek and Safrankova.** ONE functional
  form fits BOTH boundaries from Themis crossings, parabolic coordinates
  with a per-boundary scaling factor. The conference proceeding (WDS'10)
  reports lambda_y = 1.17 for the bow shock and 1.54 for the
  magnetopause, R_MP = 12.82 p^(-1/5.26) and R_BS = 15.02 p^(-1/6.55)
  with R0 at 1 nPa -- about 11.2 and 13.5 R_E at the 2 nPa the store
  already names. CITE THE PEER-REVIEWED VERSION, Jelinek et al. 2012,
  JGR 117, doi:10.1029/2011JA017252, read from that paper: its fitted
  parameters may differ and the numbers above were read from the
  proceeding.
- **Why Jelinek and not Lin.** Lin et al. 2010 (JGR 115, A04207,
  doi:10.1029/2009JA014235) is the better physics -- three-dimensional,
  asymmetric, parameterized by pressure, IMF Bz AND dipole tilt, and its
  abstract says the extrapolation for the distant tail magnetopause is
  considered, so tilt and tail are reconciled inside one published
  model. It is DEFERRED ON PORTABILITY, not rejected. Jelinek is one
  formulation for two surfaces, so one function ported twice instead of
  two; it is simple enough that the port can be checked by eye against
  the published figures, which matters when the same mathematics has to
  live in Python and JavaScript and stay identical. Lin's ten-ish
  coefficients cannot be checked that way, and an unverifiable port in
  two languages is a defect generator. Tony's framing settled it: this
  is a layperson's learning tool, not a research tool.
- **The 11 degree tilt is DROPPED, and that is a correction.** Jelinek
  assumes a symmetric magnetosphere in GSE. A later study notes that in
  Lin2010 the dipole tilt does not affect the EQUATORIAL magnetopause at
  all -- it drives north-south asymmetry and cusp location. So the old
  drawing's leaning magnetosphere was conveying something the literature
  does not support.
- **The tail is drawn, with its extent sourced.** Not omitted: Tony's
  correction, and the pattern is already in the store -- the geocorona
  is drawn at a sourced DETECTION FLOOR with the hover saying it is not
  an edge. Jelinek is a DAYSIDE fit (within about +/- 7 hours of local
  time around noon); extrapolating its paraboloid to x = -100 R_E gives
  a cylindrical radius near 46 R_E, well outside what the fit supports.
  So the tail gets its OWN citation for extent and cross-section, drawn
  to the sourced figure, with the hover stating where the drawn surface
  stops against the real one. That citation is not yet fetched.
- **The flaring parameter is SERVED, not hardcoded** (Tony's ruling the
  same evening, before the model changed). A shape parameter with a
  citation behind it belongs in the store with value / source /
  `orrery_constant`, not in `feature_renderers.js`. The VALIDITY RANGE
  travels with it, or the Mode-5 knob has simply moved from Python to
  JavaScript.
- **Before the config change: read how `check_store_drift` treats a
  DIMENSIONLESS pointer.** Its unit table is all lengths. A pointer it
  cannot examine looks exactly like one that passed, which is what the
  runner's three states exist to prevent.
- **Orrery and assembler move TOGETHER -- the braid** (Tony's ruling).
  `EARTH_MAGNETOPAUSE_STANDOFF_RADII` is quoted to the visitor in two
  hover strings in `earth_visualization_shells.py`. Changing the
  constant while the old ellipsoid still draws makes the text and the
  geometry disagree, which is worse than either being stale.
**Gap:** fetch Jelinek et al. 2012 and read its fitted parameters from
the paper; fetch a magnetotail extent citation; supersede
`EARTH_MAGNETOPAUSE_STANDOFF_RADII` (10.0) and
`EARTH_BOW_SHOCK_STANDOFF_RADII` (12.5) with sources; remove the Farris
& Russell "Model form" claim; port the one formulation to
`planet_visualization_utilities.py` and `gallery/feature_renderers.js`;
serve shape parameters and validity range; drop the tilt; then Mode 5 on
both. Also clear now, in whichever patch opens the file: the bow shock
Note still says "the shell's 15 is a migration item" when line 825
already reads the store.
**Ref:** L-291, L-292, L-298 (the orrery-vs-exhibit gap, made concrete),
L-306, `constants_new.py`, `earth_visualization_shells.py`,
`planet_visualization_utilities.py`, `gallery/feature_renderers.js`,
`data/objects_config.json` (gallery), skills/interactive-exhibit/SKILL.md.

#### [L-306] Do not promote a drawing approximation into the constants store
<!-- L:306 status:OPEN upd:2026-09-08 section:A flag: rice:4/4/85/1 -->
- **Tony's ruling, 2026-09-08:** "We are not promoting Mode 5
  approximations." And: "not promoting approximations or rounded
  numbers."
- The rule generalises past its origin. A number typed into a renderer
  because the result LOOKED RIGHT is not a constant waiting for a home.
  Moving it into `constants_new.py` and attaching a plausible citation
  is worse than leaving it where it is, because the store is the thing
  the drift checker trusts and the hover quotes. It is the same failure
  as a `# Source:` over recalled data, one layer over: the promotion
  suppresses the suspicion that would catch it.
- Three outcomes for such a number, not two: source the SHAPE it belongs
  to and recompute; or draw the sourced range and say so in the hover
  (the geocorona pattern); or remove it and note the absence. Never
  promote as-is.
- The tell: a value whose only provenance is that a previous session
  accepted the render.
**Gap:** Tony-action (do): provenance-discipline 2.10 -> 2.11 carrying
this rule, next session that opens that skill (one session, one bump),
with the four-step binding rule -- version line, `skills_index.py`,
protocol version-history entry, one commit.
**Ref:** L-305 (the case that produced it), L-291, L-299,
skills/provenance-discipline/SKILL.md.

#### [L-307] Export-age reporting for the static cards that are not migrating
<!-- L:307 status:OPEN upd:2026-09-08 section:A flag: rice:3/3/70/2 -->
- **The gap, measured at gallery `700b426d`.** Nothing compares an
  exported card to anything. `gallery_maintenance_run.py` has two checks
  that SOUND like it and are not: its STALE verdict compares the bytes
  GitHub Pages serves against the working copy (deploy freshness), and
  store drift compares `data/objects_config.json` against the orrery's
  constants. Neither reads `gallery_metadata.json`. Grepped, not
  assumed.
- That is why the grey box lived on the site (L-288) and why a
  superseded number once served for hours: an exported card is a frozen
  JSON of Plotly traces and no check knows when it was frozen.
- **This does NOT get absorbed by the assembler, and the reason must
  survive.** The assembler answers staleness for the SOLAR SYSTEM cards
  -- which are the ones getting exhibits anyway. Tony's 2026-09-08 note:
  the surviving static population is the 16:9 2D Earth science cards and
  star cards. Those will still be frozen JSON in a year with no
  assembler behind them. Deferred ON PRIORITY, behind step 3. A later
  session reading "the assembler is the real answer" must not conclude
  this can be dropped.
- **It needs a per-slot or per-file date to have anything to compare.**
  `size_kb` is already a dict keyed by slot; `converted` is one
  card-level timestamp that whichever file converted last overwrites
  (`_v2_entry`, json_converter.py). Under L-303's ruling each card
  carries one file, so the date becomes per-card naturally and no
  schema work is needed -- one more reason the ruling simplifies rather
  than adds.
- **The open question that shapes the checker, and it is its own
  conversation:** do the Earth science cards carry per-layer data
  provenance the way the served rows do, or is the provenance only in
  the KMZ and the placard? If the latter, an AGE check is all that can
  be built. If the former, something closer to store drift is possible.
  Neither Tony nor Claude could answer it in the 2026-09-08 round.
**Gap:** after step 3. A report, not a gate, beside store drift in
`gallery_maintenance_run.py`; the provenance question above answered
first.
**Ref:** L-288, L-303, L-286, `gallery_maintenance_run.py`,
`tools/json_converter.py`, earth-system-pipeline SKILL.md.

#### [L-308] A shell-legend surface for static cards (deferred, with its trigger)
<!-- L:308 status:OPEN upd:2026-09-08 section:A flag: rice:2/3/60/3 -->
- **The problem, Tony 2026-09-08.** On a phone, a static card of a
  shell-heavy body -- Earth with its interior stack -- shows the inner
  shells completely obscured and not selectable, not even for their
  hover text. The static card has no toggleable drawer; the Plotly
  legend is the only way to reach an inner shell and it is unreachable.
- **Sweeping is NOT the answer, and the reason is worth keeping.** The
  sweep widens the plot and lets the room scroll sideways. A Plotly
  legend is anchored to the plot area, so widening moves the legend
  right along with everything else. And horizontal scroll over a 3D
  canvas collides with the turntable drag handler -- `applySweep`
  already skips 3D, and L-286 is the fresh reminder of what touching a
  3D figure's interaction layer from the sweep path costs.
- **The real fix would be a separate legend SURFACE** -- an HTML entry
  list below or over the figure driving `Plotly.restyle` on trace
  visibility. A drawer without the assembler. It would work off the
  served JSON's trace names, so it would reach every multi-shell static
  card.
- **Tony's current workaround, and it is accepted:** a portrait sibling
  card with fewer shells lit. Under L-303 that is a separate card with
  its own shell selection and the phone hides the landscape one, so it
  costs no new code. Two costs named and accepted: the portrait card is
  a DIFFERENT FIGURE rather than a re-layout, so every shell-heavy body
  needs two curated exports; and when a constant moves, both files need
  re-exporting, which doubles the exposure L-288 and L-307 describe.
- **TRIGGER CONDITION for building it:** a shell-heavy body wanted on a
  phone that is NOT getting an interactive exhibit. If that never
  happens, this is never built. Recorded so the question is not
  re-derived.
**Gap:** none until the trigger fires. Not a design decision awaiting
Tony; an option with a stated condition.
**Ref:** L-286, L-303, L-307, index.html (`sweepWanted`, `applySweep`),
skills/gallery-pipeline/SKILL.md.

"""
INSERT_BEFORE = "#### [L-278] A relayout from inside a Plotly event handler re-enters the update machinery\n"

MP_EDITS = [
    (
        "**Status:** v27 -- Phase 2 (solar system assembler) BUILD UNDERWAY;\n",
        "**Status:** v28 -- Phase 2 (solar system assembler) BUILD UNDERWAY;\n",
    ),
    (
        "entry whose 24 pointers read MATCH on the live run; step 3, the\n"
        "`EXHIBIT === \"earth\"` branch, is next.\n",
        "entry whose 24 pointers read MATCH on the live run. Step 3, the\n"
        "`EXHIBIT === \"earth\"` branch, is next AND IS SPLIT: it proceeds on\n"
        "the eleven sourced features, and the magnetosphere is deferred to\n"
        "L-305 for a rebuild on a cited model, absent and named in the\n"
        "meantime rather than approximate.\n",
    ),
    (
        "**Last updated:** September 8, 2026 (v27: Earth's step 2 complete on\n",
        "**Last updated:** September 8, 2026 (v28, evening: a DESIGN BUILD,\n"
        "zero code. Step 3 split -- the magnetosphere is pre-provenance\n"
        "drawing, not sourced geometry, and gets its own build on Jelinek et\n"
        "al. 2012 with the dipole tilt dropped and the tail's extent sourced\n"
        "(L-305); approximations are not promoted into the store (L-306);\n"
        "the card model ruled to one card per orientation (L-303); export-age\n"
        "reporting and a static-card legend surface recorded with their\n"
        "conditions (L-307, L-308); Section 5a gains the 2026-09-08 evening\n"
        "subsection; with Anthropic's Claude Opus 5. v27, September 8, 2026:\n"
        "Earth's step 2 complete on\n",
    ),
    (
        "5. v25, September 6, 2026: Section 5a gains the 2026-09-06 subsection\n"
        "-- the phone passed the lobby and the sweep and failed the edge labels,\n"
        "rebuilt as the frame HUD; the order unchanged; Earth opens as a design\n"
        "conversation next; with Anthropic's Claude Fable 5.1. v24, September 5,\n"
        "2026: the 2026-09-05 subsection -- L-287 live; lobby, 2D sweep and\n"
        "twelve-edge labels built and render-gated.)\n",
        "5.)\n",
    ),
    (
        "### What this section deliberately does not carry\n",
        "### 2026-09-08 evening -- a design round splits step 3, and the\n"
        "magnetosphere turns out not to be sourced\n"
        "\n"
        "Measured at orrery `20750034` and gallery `700b426d`, both confirmed\n"
        "against the live remotes. Zero code. Appended, not merged.\n"
        "\n"
        "**The gate fired and discharged v3.54's carried obligation.** The\n"
        "session loaded `ledger-and-session-records` 1.10 against a manifest\n"
        "expecting 1.10 -- the check the 2026-09-06 session could not perform\n"
        "from inside itself.\n"
        "\n"
        "**One hover requirement unwound two constants.** The L-291 handoff\n"
        "asked only that the magnetosphere hover say the tail is drawn to 100\n"
        "radii against a real one past 1,000. Reading the code to write it\n"
        "found that the orrery's magnetopause is a half ellipsoid with typed\n"
        "axes, its bow shock a conic with an eccentricity typed at the call\n"
        "site and a sweep cap the code itself labels a Mode-5 knob, and its\n"
        "11 degree tilt unsupported by the models that would replace it.\n"
        "Farris & Russell, cited in the store as the bow shock's model form,\n"
        "is a standoff-distance relation and not a shape at all.\n"
        "\n"
        "**Tony's ruling: approximations are not promoted** (L-306). The\n"
        "seven drawn numbers stay where they are until a sourced model\n"
        "replaces the shape they belong to.\n"
        "\n"
        "**The model taken is Jelinek et al. 2012** -- one functional form\n"
        "for both boundaries -- with Lin et al. 2010 recorded as the better\n"
        "physics deferred on portability, since the same mathematics has to\n"
        "live in Python and JavaScript and stay identical, and ten\n"
        "coefficients cannot be checked by eye. Tony's framing decided it:\n"
        "a layperson's learning tool, not a research tool. The tail is drawn\n"
        "with its extent sourced, the geocorona pattern, because Jelinek is a\n"
        "dayside fit and its paraboloid extrapolated downtail is the error\n"
        "class just ruled out.\n"
        "\n"
        "**Step 3 splits rather than waits** (L-291). Eleven sourced features\n"
        "proceed; the magnetosphere is absent and named. Orrery and assembler\n"
        "move together on L-305 -- the braid -- because the standoff constant\n"
        "is quoted to the visitor in two hover strings today.\n"
        "\n"
        "**The card model is ruled** (L-303): one card per orientation, and\n"
        "the viewer rule is one line, not the old device model -- on a phone,\n"
        "hide a landscape card that has a portrait sibling. The merge was\n"
        "L-287's, not Tony's. The editor work the alternative required\n"
        "evaporates with the ruling. The surviving static population is the\n"
        "16:9 2D Earth science and star cards, which is also why export-age\n"
        "reporting is deferred on priority and not because the assembler\n"
        "absorbs it (L-307).\n"
        "\n"
        "**What this does to the order.** Nothing moves. Step 3 is next and\n"
        "is unblocked on six of its seven items. Handoff:\n"
        "`documentation/HANDOFF_earth_step3_20260908.md` in the gallery repo,\n"
        "superseded in part by this round.\n"
        "\n"
        "### What this section deliberately does not carry\n",
    ),
]


def main():
    texts = {}
    for name, md5 in FILES.items():
        lf = (ROOT / name).read_bytes().replace(b"\r\n", b"\n")
        got = hashlib.md5(lf).hexdigest()
        if got != md5:
            print("STOP: %s md5 (LF) is %s, expected %s (at 20750034)." % (name, got, md5))
            print("      Either this patch already ran, or ledger_index.py ran first,")
            print("      or the file moved. Nothing written.")
            return 1
        texts[name] = lf.decode("utf-8")
    led = texts["LEDGER_CONSOLIDATED.md"]
    mx = max(int(h) for h in re.findall(r"^#### \[L-(\d+)\]", led, re.M))
    if mx != EXPECTED_MAX_HANDLE:
        print("STOP: highest handle is L-%d, expected L-%d. Nothing written." % (mx, EXPECTED_MAX_HANDLE))
        return 1
    for i, (old, new) in enumerate(LEDGER_EDITS, 1):
        if led.count(old) != 1:
            print("STOP: ledger edit %d matched %d time(s), expected 1. Nothing written." % (i, led.count(old)))
            return 1
    if led.count(INSERT_BEFORE) != 1:
        print("STOP: ledger insertion anchor not unique. Nothing written.")
        return 1
    mp = texts["documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md"]
    for i, (old, new) in enumerate(MP_EDITS, 1):
        if mp.count(old) != 1:
            print("STOP: master plan edit %d matched %d time(s), expected 1. Nothing written." % (i, mp.count(old)))
            return 1
    for old, new in LEDGER_EDITS:
        led = led.replace(old, new, 1)
    led = led.replace(INSERT_BEFORE, NEW_BLOCKS + INSERT_BEFORE, 1)
    for old, new in MP_EDITS:
        mp = mp.replace(old, new, 1)
    for t in (led, mp, NEW_BLOCKS):
        t.encode("ascii")
    (ROOT / "LEDGER_CONSOLIDATED.md").write_bytes(led.encode("utf-8"))
    (ROOT / "documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md").write_bytes(mp.encode("utf-8"))
    print("Patched LEDGER_CONSOLIDATED.md                            md5 %s" % hashlib.md5(led.encode()).hexdigest())
    print("Patched documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md  md5 %s (v28)" % hashlib.md5(mp.encode()).hexdigest())
    print("Updated: L-291 (step 3 splits; magnetosphere -> L-305), L-303 (RULED)")
    print("Added:   L-305 magnetosphere on a sourced model, orrery + assembler")
    print("         L-306 do not promote a drawing approximation into the store")
    print("         L-307 export-age reporting for the surviving static cards")
    print("         L-308 static-card legend surface (deferred, trigger stated)")
    print("Next: ledger_index.py (Run button), commit, push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
