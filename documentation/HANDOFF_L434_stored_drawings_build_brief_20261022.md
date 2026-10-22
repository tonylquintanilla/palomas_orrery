<!-- Doc-Kind: hand | Brief for one build session in the Sun's slice: the galactic tide and the Oort cloud's clumps as stored drawings (L-434, settling L-239 and the clumps' held end on L-466), with the corona's drawer text (L-468) and the magnetotail's drawer reading (L-460) in the same website patch; then, if the evening allows, the Alfven surface's two faint surfaces (L-454, the Sun's share). -->
# Brief: the tide and the clumps stored (L-434), then the Alfven surface's faint pair (L-454)

Built on orrery 1c591cf ("cleanup", 2026-10-22 00:16) at
https://github.com/tonylquintanilla/palomas_orrery and gallery
90cefa5 ("daily run again L460 corona base", 2026-10-21 23:28) at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Run
`git ls-remote` on both at the start; the Daily Run moves the gallery
every morning, so read the newest commit's message and build on the
new HEAD.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD. Written October 22, 2026 by Anthropic's Claude Fable 5.1,
in a coordination session, for a Claude Opus build session. Follows
`HANDOFF_sun_drawer_pairs_build_20261021.md`, section 8 ("Next
session"), and the design records `DESIGN_talks_rulings_20261020.md`
(talks 2 and 5) and `DESIGN_talks2_rulings_20261021.md` (talk B).

## 1. Read this first

- Last night's session is closed and pushed: the drawer order (L-460),
  the fourteen pairs (L-191), the Drawn ends check (L-466), the corona's
  base and the Hills cloud's edge fixed. Protocol v3.107.
- Skills: the manifest at 1c591cf expects interactive-exhibit 1.19 and
  provenance-discipline 2.33; Tony reinstalled both last night. Confirm
  the loaded copies read those before work that fires them (that is
  v3.107's obligation). Also orrery-coding-conventions 1.11,
  gallery-cache-builder 1.11 (the drawings pull and the cache),
  safe-file-editing 1.13, agentic-pre-test 1.3,
  ledger-and-session-records 1.21.
- Tony's latest run record:
  `documentation/WHERE_WE_ARE_10-21-26_1658_run_record.md`. His
  reading-list notes (Hipparcos saved into `papers/`; Delsemme timed
  out; Maezawa walled) are in his local copy of
  `READING_L456_tony_20261021.md`, pushed with his next commit.
- One Tony-action from last night's close is not marked done in the
  record: his look in the orrery at a few Sun checkboxes' tooltips
  beside their markers' hovers, the same words. Ask once, at the
  start; it closes L-191's Sun share.
- This session owns the ledger, Where We Are, the skills and the
  protocol for the day. No parallel build.

## 2. Job 1: the tide and the clumps as stored drawings (L-434; orrery, then the website)

The rulings, all made, none to re-ask:
- Talk 5, 2026-10-20 ("Confirmed"): the galactic tide and the Oort
  cloud's clumps become stored drawings, together; the streamer band
  does NOT (it is a grid from about twenty served numbers with a small
  jitter, and stays the website's own draw).
- Talk 2, 2026-10-20 ("Yes"): the phone's tide takes the orrery's L-420
  look: 5,000 dots at twice the size and opacity; the pink double cone
  worked out by the website from served numbers (the two edges, the
  served galactic pole, the angle where the tide peaks), not stored;
  the tide's hover line already approved for the orrery. The website's
  tide hover goes to Tony old and new side by side before it ships.
- L-239, settled by talk 5: the orrery places both from a seed, as the
  Hills cloud does (`hills_cloud_sampler.py`, seed 421; the Hills
  cloud, the belts, the exosphere, the corona and the dust cloud are
  the five stored drawings today).
- L-466 (Drawn ends), 2026-10-21: the clumps' near end is held OPEN by
  name because the 15 clumps are placed at random and the nearest dot
  lands at 21,363 AU where the row says they begin at 10,000 AU. The
  tide's near end (10,563 AU against its 10,000 AU edge) is held as
  sampling. This build makes the clumps start where their row says and
  takes that held end off the check's list.

The orrery half:
1. Read the three builders in `solar_visualization_shells.py`
   (`create_sun_outer_oort_clumpy`, `create_sun_galactic_tide`; the
   Hills one is already done) and the stored-drawing pattern in
   `hills_cloud_sampler.py`, `sun_corona_sampler.py` and
   `export_drawings.py` (`DRAWINGS`), with `test_drawings_export.py`'s
   planted faults.
2. Two new samplers, one per drawing, each with a seed in its config,
   placing dots between the rows' edges and checked there: the tide
   from its served edges and the galactic pole, 5,000 dots; the clumps
   from the row that says where they begin (10,000 AU) to the cloud's
   outer edge, every dot inside the edges, so the nearest dot is at or
   past 10,000 AU. Every edge a dot can reach is a served row or a
   sampling rule written on the row (provenance-discipline 2.33,
   principle 4); no number typed in the renderer.
3. The orrery draws from the same stored dots it exports (the Hills
   cloud's pattern), so the window and the website show the same
   cloud. Two entries in `export_drawings.DRAWINGS`; planted faults in
   `test_drawings_export.py` (a dot inside 10,000 AU for the clumps; a
   dot past an edge for the tide; a wrong tilt), each caught by name.
4. Agentic pre-test: py_compile, the xvfb run on a throwaway copy, the
   live-dispatch smoke test (the Sun's Oort checkboxes ticked, the
   traces read back). Check the file sizes against the talk's
   estimate (the tide about 80 kB, the clumps about 30 kB) and say
   them.
5. Tony: the orrery patch, moved into `documentation/`, the
   maintenance run (the drawings export rewrites two new files; the
   Drawings export check gains two names), commit, PUSH. His look in
   the orrery: the Oort cloud with the tide and the clumps ticked,
   the same cloud on every run.

The website half, one patch, built on the orrery's new push and the
gallery's HEAD after that morning's Daily Run:
6. `tools/pull_drawings.py`, the cache builder's `serve_drawings()`,
   `tools/check_drawings.py`: the two new drawings pulled, served by
   name and checked by their mechanism (inside their edges; the tide's
   plane against the galactic pole).
7. `gallery/feature_renderers.js`: the tide and the clumps drawn as
   stored (`drawing.dots`), the tide at the orrery's size and opacity;
   the pink double cone worked out from served numbers; the website's
   own seeded generators for these two shapes retired (the streamer
   band's stays). The tide's hover with the cone line, old and new
   side by side for Tony before it ships (the words list).
8. L-468, the corona's drawer text: a row opens its own feature's
   words. Since the belt joined the corona's row (Oct 20), naming the
   row opens the belt's cross, the first in trace order
   (`sunLabelMarker` in `interactive.html`). Fix: a member drawn with
   another yields the row to the host's cross. A headless check that
   each row in both rooms opens its own feature's words, with a
   planted swap caught by name.
9. L-460's last loose end: the magnetotail is placed in Earth's drawer
   by its width (30 Earth radii) instead of where it starts (30.6).
   Read the start; the order does not change; the check's expected
   list moves with it.
10. The Drawn ends check: the clumps' held end comes off the list with
    its reason, and the check now fails if a clump dot lands inside
    10,000 AU. Expect the gallery run at 34 gating with every row
    passing after the Daily Run (before it, the four cache-dependent
    rows fail, as last night).
11. Tony: the website patch, moved into the gallery's `documentation/`,
    the Daily Run (the pull brings the two new drawings), the offline
    run, commit, push, the live run. His phone: the Sun room, the Oort
    cloud's rows ticked, the tide's X and cone, the clumps; the corona's
    drawer row now opening the corona's words; Earth's drawer unchanged.

Not in this job: where the Hills cloud's tap cross goes (L-468's second
half) is a design-talk item; leave it. The streamer band stays as it
is.

## 3. Job 2, if the evening allows: the Alfven surface's two faint surfaces (L-454, the Sun's share)

Talk B's ruling, 2026-10-21: every real edge that moves keeps its sharp
model surface and gets two faint surfaces at the ends of the range its
model was fitted to, each pair on its own drawer row so they do not
clash by default; by kind, so the Sun's Alfven surface takes 10 and 20
solar radii from its existing rows (`ALFVEN_SURFACE_RANGE_LOW_RADII`,
`_HIGH_RADII`, Cranmer et al. 2023). Faint means fewer, dimmer dots
than the model surface: rendering settings, in the drawing code.

Two cautions from the design record:
- The Alfven's 10 and 20 are a different kind of range from Shue's and
  Jelinek's: where the surface spends most of its time, not a fit's
  validity. The words say which it is; do not call it a fitted range.
- The drawn surface at 19.7 sits next to the high end at 20. Whether
  the outer faint surface can be told from the drawn one is a Mode 5
  question for Tony's look; if it cannot, say so and ask whether the
  outer faint surface stays, is dropped, or is drawn differently. Do
  not decide it.

Both instruments, its own row in each drawer ("Alfven surface, range"
or words Tony approves), the hover saying what the two faint surfaces
are, from the rows. Earth's two pairs (the magnetopause's and the bow
shock's, with their four new measured rows) are NOT this job; they go
with Earth's builds after the Sun's slice.

If job 1 fills the session, job 2 waits; say so in the handoff.

## 4. The close (orrery)

One close patch on the HEAD after Tony's pushes: the ledger (L-434,
L-239 DONE on his looks; L-466's held list; L-468's first half DONE,
its second half carried; L-460 DONE; L-454's Sun share if built;
L-412's list), Where We Are by section (the box: what changed, do next,
needs you now; stage 7's line, which now ends the Sun's slice except
the ice lines (L-128) if job 2 is built; the marks reset), the
handoff. No skill bump is expected; if one is earned, one session, one
bump, with its protocol entry (v3.108) and the reinstall obligation.

## 5. Not this session

- Earth's builds from the talks: L-375's cone, L-454's two Earth pairs,
  L-356 with the offset sentence, L-458's report link. One Earth
  session after the Sun's slice.
- L-461, L-462, L-465, and L-468's cross placement: rulings first.
- L-128, the comet ice lines: waits, by Tony's ruling.
- Tony's reading list: if a new paper is in `papers/`, read it through
  the device mount and write its `# Read:` line; the Hipparcos volume
  may be there (section 1.5.3, book page 91, PDF page about 135).

## 6. At the close

- The handoff: what was built (verified, not claimed), the run order,
  the two drawings' sizes and seeds, the Drawn ends list as it now
  stands, what is still open by name, and what the next session starts
  with (Earth's builds, or job 2 if it did not fit).
- "Where this leaves us", two or three lines in Where We Are's words.

Brief written October 22, 2026 with Anthropic's Claude Fable 5.1.
