# Earth Exhibit -- Step 3 after the design round

Built on orrery `20750034c9fab71b7495bfca50f4039b699cd5c4`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `700b426d4cecc1f80fd6f9ca5758e5058ea497a6`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
Both confirmed against the live remotes before this was written.

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-08
Protocol v3.54. Ledger handles: L-291, L-303, L-305..L-308.
Master plan v28.

**Type: DESIGN SESSION (zero code).**

**Companion to** `documentation/HANDOFF_earth_step3_20260908.md`
(gallery repo), which remains the authoritative record of where step 2
left both repos. **This document supersedes that one's step 3 item 1
and part of item 5**, and nothing else in it.

A partner without this Project reads these first, live at the SHAs
above: `PROJECT_INSTRUCTIONS.md` (orrery root) and, for this task,
`skills/interactive-exhibit/SKILL.md`,
`skills/orrery-coding-conventions/SKILL.md`,
`skills/provenance-discipline/SKILL.md`. State back which you read.

---

## STEP 0 -- Gates

- No skill was bumped this session. Load `interactive-exhibit` (expect
  1.0), `gallery-assembler` (1.2), `ledger-and-session-records` (1.10),
  `orrery-coding-conventions` (1.7), `safe-file-editing` (1.10),
  `provenance-discipline` (2.10); each must match the manifest in
  PROJECT_INSTRUCTIONS.md Part 3.
- **v3.54's carried obligation is discharged.** That version bumped
  `ledger-and-session-records` to 1.10 from a session that had loaded
  1.9, and wrote the confirmation forward. This session loaded 1.10
  against a manifest expecting 1.10. Settled; do not carry it again.
- `git ls-remote` both repos and reconcile if either moved past the
  anchors above.

## WHAT CHANGED THIS ROUND

Zero code. Four rulings and a change order, all Tony's.

**Step 3 is split** (L-291). It proceeds on the ELEVEN sourced
features. The magnetosphere renderer is deferred to L-305. The exhibit
ships with the magnetosphere absent and named rather than approximate.
Tony's framing, which decided several things downstream: this is a
layperson's learning tool, not a research tool.

**The magnetosphere was never sourced** (L-305). Reading the code to
write one hover line found that the orrery's magnetopause is a half
ellipsoid with typed axes (12 equatorial, 10 polar), its bow shock a
conic with `eccentricity=1.05` typed at the call site and a sweep cap
the code itself labels a MODE-5 KNOB, and an 11 degree dipole tilt the
replacement models do not support. Farris & Russell (1994), cited in
`constants_new.py` as the bow shock's model form, is a standoff-distance
relation and not a shape.

**Approximations are not promoted** (L-306). Tony's ruling, stated
generally and awaiting a `provenance-discipline` bump. A number typed
into a renderer because the render looked right is not a constant
waiting for a home.

**The card model is ruled** (L-303). One card per orientation. The
viewer rule is ONE line, not the old device model: on a phone, hide a
landscape card THAT HAS A PORTRAIT SIBLING. Everything else is
unchanged, the sweep still serves the landscape-only majority, and the
per-slot editor work the alternative required evaporates.

## STEP 3 -- Code (next), six items

Read `interactive-exhibit` step 3 first. Then, in this order:

1. **ONE renderer in `gallery/feature_renderers.js`, not two.**
   `earth_geostationary`: a ring in the body's equatorial plane at
   `radius` (R_earth), oriented by `poleBasis(orientations[slug])` the
   way `renderRingSystem` is; warn and draw in the ecliptic if no
   orientation. Row shape is
   `{shape: "equatorial_ring", radius: {value, unit}, ...}`.
   `earth_magnetosphere` is NOT built here -- see L-305.
   In `documentation/smoke_features.js` the two expected warnings become
   ONE, not zero: `earth_magnetosphere` stays a named expected absence.
   Trace count 13 becomes 13 plus what the ring adds. Regenerate
   nothing. `pin_artifact1_known_failure.py` does not move.
2. **The `EXHIBIT === "earth"` branch in `interactive.html`.** Driver
   spec unchanged: `objects` Earth and Moon, `center` Earth, half-range
   floor 6.155e-5 AU. Eight shells lit on arrival: inner core, outer
   core, lower mantle, upper mantle, crust, lower atmosphere, upper
   atmosphere, LEO. Also on: axis with equator plane, Sun direction.
   Everything else a drawer row, unselected. The drawer should say the
   magnetosphere is not yet drawn rather than omit it silently.
3. **The terminator** is geometry: a great circle on the crust
   perpendicular to the Sun direction plus a subsolar marker carrying
   the hover. No lighting model.
4. **The Moon's orbit:** full ellipse faint, the trust-window arc
   brighter around the marker.
5. **Hovers that must say something:** the scene is one epoch, so the
   terminator is frozen and the axis implies a rotation the scene does
   not show. The tail line from the earlier handoff does not apply --
   there is no tail this step.
6. **The shared chrome, by parameter,** and **i-panel copy** with
   sources read from the served rows. Unchanged from the earlier
   handoff.

Steps 4-8 as in `HANDOFF_earth_build_order_20260906.md`.

## L-305 -- the deferred build, scoped

Not step 3. Its own session, and the orrery and the assembler move
TOGETHER (the braid) because
`EARTH_MAGNETOPAUSE_STANDOFF_RADII` is quoted to the visitor in two
hover strings in `earth_visualization_shells.py` today; changing the
constant while the ellipsoid still draws makes text and geometry
disagree.

- **Model: Jelinek, Nemecek and Safrankova 2012**, JGR 117,
  doi:10.1029/2011JA017252. ONE functional form fits BOTH boundaries.
  Read its fitted parameters FROM THAT PAPER; the numbers in L-305 came
  from the WDS'10 proceeding and may differ.
- **Lin et al. 2010** (JGR 115, A04207, doi:10.1029/2009JA014235) is
  the better physics -- tilt and distant tail in one model -- and is
  DEFERRED ON PORTABILITY, not rejected. The same mathematics has to
  live in Python and JavaScript and stay identical, and ten fitted
  coefficients cannot be checked by eye against published figures.
- **The tilt is dropped**, and that is a correction: the equatorial
  magnetopause does not lean.
- **The tail IS drawn**, with its extent separately sourced and the
  hover saying where the drawn surface stops -- the geocorona pattern
  already in the store. Jelinek is a dayside fit; extrapolating its
  paraboloid downtail is the error class L-306 rules out. That citation
  is not yet fetched.
- **Shape parameters are SERVED** with value / source /
  `orrery_constant`, and the VALIDITY RANGE travels with them, or the
  Mode-5 knob has just moved from Python to JavaScript.
- **Before the config change:** read how `check_store_drift` treats a
  DIMENSIONLESS pointer. Its unit table is all lengths, and a pointer it
  cannot examine looks exactly like one that passed.

## OPEN ITEMS THAT TOUCH THIS BUILD

- **L-303 (build, not decide any more):** the converter's inverted
  pairing and sibling stamp, the one viewer rule, the split migration of
  L-287's 38 pairs plus L-301's 3. Two portrait titles are lost in the
  split and get retyped.
- **L-307:** export-age reporting, deferred ON PRIORITY behind step 3 --
  NOT because the assembler absorbs it. The surviving static population
  is the 16:9 2D Earth science and star cards, which will still be
  frozen JSON in a year. One question blocks the design and is its own
  conversation: do the Earth science cards carry per-layer provenance,
  or is it only in the KMZ and the placard?
- **L-308:** a static-card legend surface, deferred with a stated
  trigger -- a shell-heavy body wanted on a phone that is not getting an
  exhibit. Workaround accepted meanwhile: a portrait sibling with fewer
  shells lit.
- **L-292, L-297, L-298, L-299, L-300, L-304** unchanged from the
  earlier handoff.

## TONY-ACTION ROLLUP

1. **(do)** Run `patch_L291_8_magnetosphere_change_order_20260908.py`
   (orrery root) BEFORE `ledger_index.py`.
2. **(do)** Run `ledger_index.py`. It has NOT been run since
   `patch_L291_7`: the ledger at `20750034` is byte-identical to that
   patch's output, so the index zone does not list L-301..L-304 and the
   two DONE blocks have not migrated to section C. One run now covers
   both patches.
3. **(do)** Commit and push the orrery; report the SHA.
4. **(do)** Save this file into the gallery repo's `documentation/`,
   commit and push.
5. **(do)** Re-export the Earth-and-Moon PORTRAIT scene through Studio
   and re-convert, so the grey box leaves the site (L-288). Under
   L-303's ruling this becomes its own card.
6. **(do)** `provenance-discipline` 2.10 -> 2.11 with L-306's rule, and
   `gallery-assembler` 1.2 -> 1.3 with L-304's four field notes -- each
   next session that opens that skill, one session one bump, four-step
   binding rule.

## WHAT THIS ROUND LEARNED

- **A hover requirement is a provenance audit in disguise.** The chain
  started with one sentence the handoff asked for and ended with two
  constants superseded and a build split. Writing a hover that names its
  source forces you to read what is actually drawn.
- **The prior handoff's framing was wrong and read first.** It called
  the magnetosphere renderer a step-3 item. It is a build. A later
  session reads the handoff before the ledger; say so in both.
- **Checking beat recalling, three times in one round.** The standoff
  was 10.0, not the 10.25 recalled; the orrery does not use Shue at all;
  the bow shock's flaring parameter already existed as 1.05. Every one
  of those was found by fetching the file at the SHA.

Written September 2026 with Anthropic's Claude Opus 5.
