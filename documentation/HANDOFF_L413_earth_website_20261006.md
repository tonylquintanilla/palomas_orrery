<!-- Doc-Kind: hand | Session record: Earth's website patch, the saved Earth scene, three hovers fitted to the phone, and the typed facts found (L-413, L-349, L-379, L-300, L-421), 2026-10-06. -->
# Handoff: Earth's website patch, and the facts typed in the rooms' code

Built on orrery 51436054330aefd6be2a7efd93ebd58f06c4a2d2 and gallery
ed48d078ceb639f5f98f13f4c6abc129f722c566; the gallery patch pushed at
38f1e7b058ac359d5b7806fc3d2fe7da77d48e64 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io; this
closing patch rebuilt on orrery e7073fce5cc214836d2175d3f7643ff0855c7064
at https://github.com/tonylquintanilla/palomas_orrery, after the first
build refused (below). Orrery pushed at: Tony's run record carries it. This
record is carried by `patch_L413_7_session_close_20261006.py`. Written
October 6, 2026, with Anthropic's Claude Opus 5.5.

## Opening checks [verified @ orrery 51436054, gallery ed48d078]

- All eleven skills the session loaded were byte for byte the repo's
  `skills/` copies, at the versions the last handoff named:
  provenance-discipline 2.26, interactive-exhibit 1.11, safe-file-editing
  1.13, orrery-coding-conventions 1.10, ledger-and-session-records 1.16,
  gallery-cache-builder 1.7, each opening with its contents list.
- The protocol in this session's context was already v3.83, from the
  parallel L-027 session, while the repo still read v3.82. This session
  did not notice the difference. It was the signal that another session
  had changed the protocol, and missing it is why the first closing
  patch was built on the wrong version.
- So L-419 and L-415 close, and L-369 closes on Tony's look of
  2026-10-05 ("beautiful"). L-418 does NOT close: its version check is
  done, but splitting provenance-discipline's two long procedures is
  still open on it.
- When the first closing patch was built, orrery HEAD was still
  51436054. A parallel session (L-420, then L-027) pushed e7073fce
  before Tony ran it, and took protocol v3.83 for agentic-pre-test 1.3.
  The first closing patch refused at the protocol's header line and
  wrote nothing, as built. This one is rebuilt on e7073fce: the skill
  change is v3.84, v3.81 moves down, and Where We Are carries that
  session's lines from its handoff.

## What was done

Gallery, `patch_L413_6_earth_website_20261006.py`, tested whole on a
copy of gallery ed48d078 with an imitation cache rebuild: 24 of 24
gating checks passed; without the rebuild, "Cache in step" and "Display
figures" fail, as they should.
- L-349: Earth's inner belt reads in Tony's approved words; the word
  "protons" comes from a new served list, `flux_peak_of`, beside the
  belts' other words, which `store_writer.py` may edit. A belt says
  "measured" only when its row has a source, so Jupiter's three belts
  make no claim.
- L-292: the geocorona note's sentence saying the orrery has no shell of
  its own is gone.
- L-379: `documentation/payload_earth_scene.json` re-recorded from the
  cache of 2026-10-05 by the new `tools/record_earth_scene.py`, which
  runs the Earth room's own Python out of `interactive.html`. The cache
  pieces three checks laid over the old recording are gone.
- Measured on the live scene, three hovers were over the 17-line limit:
  the rotation axis at 21 and the outer belt at 18, both already live,
  and the inner belt at 18 with the new words. With Tony's approved
  changes all three are 17: the axis hover's layout (a doubled break
  removed, the tilt sentence re-broken, one empty line gone, no word
  changed), and one shorter sentence on both belts.
- L-300: the "Collapsed features" checker in `gallery_maintenance_run.py`.
- The hover fixture re-recorded as
  `documentation/fixture_hovers_L349_on_ed48d078.json`.
- Run and pushed at 38f1e7b0: 24 of 24 after the cache build, the swap
  absorbing one refused rename. Tony's look on the phone: "correct";
  "Jupiter inner belt not in the room yet. correct in the orrery." So
  L-349 and L-300 close.

Orrery, this patch: the dashboard button for the new checker; the rule
below into interactive-exhibit 1.12; protocol v3.84; Tony's look at
L-420, from his run record, recorded on L-420; the ledger; the
manifest; this handoff; Where We Are.

## Tony's notes found in Where We Are when this patch ran

The lines below differed from the page at 51436054 when the patch
rewrote it, carried here word for word so nothing he wrote is lost:

    (none: the page was as pushed at e7073fce)

## Tony's rulings, 2026-10-06

- The word "protons" is served, not typed, on Claude's recommendation;
  Tony then set the frame: "I thought the only source of truth is the
  constants py and the objects list ... not from the code."
- The skill gets the clarification, unless he said otherwise; he did
  not.
- L-379 done properly, by re-recording the saved scene: "Proceed as
  recommended."
- The belts' tilt sentence, approved: "...which turns with Earth and in
  2020 was tilted 9.4105 degrees from it, shrinking 0.0493 degrees a
  year (IGRF-13 model)." The axis hover's layout change, approved.
- The typed facts are handled now, not backlogged: "the work is here.
  We should handle it now. What we are doing is working to make the
  earth and sun slices complete, following the braid." Claude had
  proposed a ledger row; that was the Braid read backwards, since these
  rooms are the current slice.
- The plan for them, including where the drawn guides' words go:
  "Approved as recommended." The build moves to a fresh session from
  the manifest: "Confirmed as recommended."

## Discrepancies surfaced

- Claude told Tony the interactive-exhibit skill already required
  served words for "protons". It does not: it requires served NUMBERS,
  and lets page-level text carry its source in the page. Corrected in
  chat; the skill now draws the line (1.12).
- Claude first offered "a rule in the page" as an option for the
  particle word. Tony's frame ruled it out; it should not have been
  offered.
- The old saved scene hid two live hovers that were over the phone's
  line limit, since the scene had no pole of date and no belt edges.
- The discovery's first pass called the magnetopause's and bow shock's
  formulas typed. They are served, under `_model`.
- `tools/record_earth_scene.py` may duplicate the headless recipe the
  skill describes in `tools/headless/`. The manifest asks the building
  session to read that first.

## Tony-actions, rolled up

(do)
- Gallery: done, pushed at 38f1e7b0.
- Orrery: run `patch_L413_7_session_close_20261006.py`, move it into
  `documentation/`, run `orrery_maintenance_run.py`, commit, push.
- Reinstall interactive-exhibit (1.12) in Settings > Skills, and replace
  the Project's instructions with `PROJECT_INSTRUCTIONS.md`, now v3.84.
- The first closing patch, `patch_L413_7` as first delivered, refused
  and wrote nothing; delete that copy and run this one.

## Next session

- Confirms its loaded interactive-exhibit reads 1.12 before any exhibit
  work.
- Builds the typed-facts move from
  `documentation/MANIFEST_L421_typed_facts_20261006.md`. patch_L413_6
  landed at gallery 38f1e7b0.
- Works L-420's two requests from Tony's look, and closes L-027 on his
  look at the panels (that session's handoff).
- Where We Are: the Horizons session leaves the page alone this round
  and puts its updates in its own handoff; the next rewrite picks them
  up from there.
