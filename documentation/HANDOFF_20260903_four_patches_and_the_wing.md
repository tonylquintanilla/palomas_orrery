# HANDOFF -- 2026-09-03: Four patches waiting, and the wing designed

**Built on** orrery `faac433f138564d1426835b80ed56562a3ccb5c9` at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
gallery `8e5f0bddcc8378d399f32c8a277d2e85ec1e84de` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both confirmed against the live remote at session start. Nothing was
pushed during this session: Tony was away from his machine throughout.

**Type:** BUILD + DESIGN. Four patches were built and tested on
throwaway clones and are WAITING on Tony's machine. One design
conversation (the interactive wing, the lobby, the visual theme) is
captured in the last of those patches. Protocol goes to v3.53 when the
patches run.

---

## Confirm this first

Both repo HEADs against the anchors above. If orrery HEAD has moved past
`faac433f`, the four patches below have run (or something else landed);
check the ledger for L-280..L-284 before doing anything else.

Skills this session: `gallery-assembler` loaded as 1.2 and matched the
manifest, which discharges the obligation carried from 2026-09-02.
`safe-file-editing` 1.10 and `ledger-and-session-records` 1.9 loaded and
matched. No skill was bumped this session, so nothing carries.

The protocol will read **v3.53** after `patch_L276` runs and Tony
re-uploads it to the UI. Until then the UI copy is v3.52 and correct.

---

## The four patches, in run order

All four are in Tony's downloads from this conversation. None has run.
Each refuses with a reason rather than writing anything wrong; the three
orrery patches enforce their own order through fingerprints and
anchors.

**Gallery repo** (independent of the other three):

1. **`patch_L265_info_url_curated.py`** -- replaces all 22 placeholder
   links in `data/objects_config.json`: 20 `info_url` values plus the
   2-entry `info_urls` array on Earth's radiation belts. Rule (Tony): a
   NASA page where one is specific to the feature, else English
   Wikipedia; one exception by his word -- the corona shells take
   Wikipedia's Solar corona article because the only NASA corona page is
   Space Place, written for children. Result 5 NASA, 15 Wikipedia, both
   belts to NASA's Van Allen page. Every URL returned live on the day.
   Edits `objects_config.json` only; `feature_configs.json` and
   `coverage_index.json` are builder outputs and follow on the next
   builder run. **Then run the cache builder**, commit, push.
   Asserts zero placeholders remain anywhere in the file.

**Orrery repo**, in this order:

2. **`patch_L277_reanchor_site_stores.py`** -- the L-192 site store
   anchors by enclosing name instead of line number; the three live
   L-192 stores move to the repo ROOT with `Doc-Kind: hand` tags;
   `worksheet_keys.py`, `worksheet_checker.py`, `test_worksheet_keys.py`,
   `test_extractor_pins.py` updated; L-277 and L-265 amended. Tested:
   both L-192 tests green (52/52/29), 40 inserted comment lines no
   longer break anything, a renamed label goes red by name, a dropped
   pin goes red by name, an old-format row is refused, doc_index picks
   up the three stores. Expect README.md to change on the maintenance
   run.

3. **`patch_L276_mode7_repo_access.py`** -- protocol to **v3.53**: Mode
   7's "zero independent repo access" clause replaced with the approved
   wording; a note under AI Roles on how each partner reads the repo
   (Gemini imports a public repo as a snapshot, cannot read a URL from a
   prompt, cannot fetch at a SHA, cannot see history, not on mobile --
   Google's own documentation); header, anchor, v3.53 history entry;
   v3.50 moved down to the history file; archive
   `documentation/project_instructions_v3_53.md`; L-276 DONE. Protocol
   and history are fingerprinted; the ledger edit is anchor-guarded.

4. **`patch_L280_284_interactive_wing_capture.py`** -- five new ledger
   items (below). Builds nothing. Anchor-guarded; refuses unless L-277's
   record and L-276's closure are present.

Then: maintenance run, commit, push, **re-upload PROJECT_INSTRUCTIONS.md
to the UI**.

---

## Ledger state after the patches run

| Handle | State | What |
|---|---|---|
| L-265 | OPEN | curation done, patch waiting; gates Stage C |
| L-276 | DONE | Mode 7 clause corrected, v3.53 |
| L-277 | OPEN until the maintenance run is green | site store reanchored, stores at root |
| L-280 | OPEN, 4.3 | The Interactive Wing: door, hall, two rooms, What's New |
| L-281 | OPEN, 4.2 | The guest book: no-account comments, approve-before-show |
| L-282 | OPEN, 3.8 | The lobby: the main page as an entrance hall |
| L-283 | OPEN, 3.2 | Visual theme: dark wall, paper placards, record mode |
| L-284 | OPEN, 1.9 | Retire the social export; the gallery owns publishing |

RICE scores on L-280..L-284 are proposed, not confirmed.
`ledger_index.py` on the test clone: 279 blocks, 172 live items.

---

## The decisions Tony made

- **L-265:** links are not scanned for provenance; Claude curates under
  Tony's rule (NASA if specific, else Wikipedia); corona to Wikipedia.
- **L-277 (b):** reanchor the store to names, not update it per slice.
  And move it: "This file should at least be located in the root not in
  documentation/ and it should be tracked by the document tracker."
  Widened to all three live L-192 stores.
- **L-276:** wording approved as proposed; add the Gemini note.
- **The wing:** the museum framing -- permanent collection plus a new
  wing under construction where the visitor chooses. "What's New", not
  "Next". Two rooms now; the premade planets room is eventually replaced
  by interactive planets. A guest book with a low bar: no sign-up to
  post, moderator can delete (Cusdis recommended; giscus fallback).
- **The lobby and visual theme:** "dark wall with paper placards -- let's
  go with this." Two breadcrumbs: wide Earth System exhibits are SWEPT
  sideways in portrait; views must record cleanly in Instagram Edits
  (record mode).
- **The collections room** carries a short placard on the provenance
  discipline as a scientific effort without claiming authority; text
  approved as drafted (in L-282).
- **L-284:** the social export is legacy, fully replaced by the gallery
  editor; retire it, correction to travel to all four consumer-list
  stores.
- **When to build:** in a new session, after the four patches have run
  and pushed (see below).

---

## What was found

- **The L-192 site store was ALREADY stale and the round trip could not
  see it.** All 23 `constants_new.py` rows pointed at lines that no
  longer held the named constant (August constants migration).
  `key_for_site` falls back to the label at a stale line, and for a
  constant the label IS the key, so the test stayed green. Three rows
  minted wrong keys (EARTH_POLAR_RADIUS_KM, SPEED_OF_LIGHT_KM_S,
  BENNU_RADIUS_KM sat inside other constants' statements) and the test
  never compared minted keys to the pins. A Check That Cannot Fail, in
  the test built to be the check. The L-277 patch closes it: the round
  trip re-mints from the located line and compares the minted set to
  the pins by name.
- **Claude miscounted the L-265 placeholders** (20, not 22) by walking
  only the singular `info_url` key and missing the belts' `info_urls`
  array. Caught by reading the L-265 ledger block, which said 22 and
  said why. The patch now asserts zero placeholders remain anywhere.
- **The served files are builder outputs.** `gallery_cache_builder.py`
  copies each object's `features` straight from `objects_config.json`
  into `feature_configs.json` and `coverage_index.json`; the builder ran
  2026-09-02 12:42 UTC. So one file to patch, not three.
- **Gemini's repo access is a snapshot import**, per Google's own
  documentation, which answers Tony's question of how it saw the repo
  without an upload or Drive. Written into Mode 7 so it is not
  rediscovered.
- **Nothing depends on `social_media_export.py`** in either repo; the
  gallery tools carry their own `_parse_hover_html()`.

---

## Tony-action list

- **(do)** Run the four patches in the order above; cache builder after
  the gallery patch; maintenance run after the orrery three; commit and
  push both repos; re-upload PROJECT_INSTRUCTIONS.md (v3.53) to the UI.
- **(do)** Mode 5 portrait pass on the Sun exhibit (Stages A and B are
  live and unverified on a small screen), once Stage C has something to
  show. Carried.
- **(decide)** L-281: Cusdis hosted free tier now, or wait until the
  hall exists.
- **(decide)** Confirm or adjust the proposed RICE scores on
  L-280..L-284.
- **(decide)** Whether `project_instructions_v3_50.md` and `_v3_51.md`
  get reconstructed from git. Carried; v3.53 is archived, v3.50 and
  v3.51 still are not.
- **(decide)** `MASTER_PLAN_INTERACTIVE_GALLERY.md`'s two stale NEXT
  statements; L-268's order; L-266's shape. All carried from
  2026-09-02.

---

## What the next session should build

**Stage C of the Sun GUI (L-267).** Once the L-265 patch has run and the
builder has carried the links into `feature_configs.json`, the i panel
has content: links, not prose. Confirm the served file carries the 22
links before building; the SHA is the round trip.

**Then the hall (L-280), designed in conversation first.** The design is
recorded in L-280/L-282/L-283 in enough detail to start from the ledger
alone; do not rebuild it from memory of this conversation. Iterate the
hall screen with Tony before writing it: each round simpler. Portrait
first; Mode 5 is his.

**Not next, but do not lose:** L-284's removal patch touches the protocol
and two skills, and it sits inside files L-254 and GUI work will open;
cluster it there.

---

*Session written September 3, 2026 with Anthropic's Claude Fable 5.1.
Built on orrery `faac433f`, gallery `8e5f0bdd`; both confirmed at
session start; nothing pushed. Four patches built and tested on
throwaway clones; all four waiting.*
