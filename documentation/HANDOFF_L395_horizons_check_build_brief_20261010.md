<!-- Doc-Kind: hand | Brief for the L-395 build: the check of the orrery's object list against JPL Horizons, as designed on October 7 and ruled through October 8; Encke's list entry and Halley keyed; orrery first, then the gallery's Daily Run step and offline checker. Written October 10, 2026. -->
# Handoff: L-395 (the Horizons check), the build brief

Built on orrery ca5bbe12cb8f1c48b134f6aadaa700d45ae9e39d ("L427
records", 2026-10-10 13:41 CDT) at
https://github.com/tonylquintanilla/palomas_orrery and gallery
050637c3688e1bfcff81848ad4780b8a9e975a9e at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. The
session pins both HEADs itself at its start; the gallery has a daily
build each morning, so its HEAD will have moved. Written by the Fable
5.1 coordination session of October 10, which read both repos at HEAD
and wrote no patch.

- Type: BUILD, two repos, in order: the orrery first (the list, the
  export, its test), Tony's push, then the gallery (the live check as
  a Daily Run step, the offline checker in the maintenance run, the
  tests). One session can do both, with one stop for Tony's orrery
  push in the middle; the gallery half builds on that push, because
  the gallery pulls the orrery's export from HEAD.
- Why now, Tony's ruling of 2026-10-10: "I would like to finish the
  Horizons build first because it's part of our provenance
  discipline." It moves ahead of the Oort cloud build (L-421).
- The design is ruled and recorded. Read, in this order:
  `documentation/DESIGN_L395_horizons_check_20261007.md` (every
  ruling, and section 5, the build list),
  `documentation/HORIZONS_ANSWERS_L395_20261007.md` (JPL's answers,
  by letter, the offline tests' ground truth), and L-395's block in
  the ledger (the October 8 rulings: Halley keyed and checked, both
  comets' words and links, which are settled there word for word).
- Skills this session fires: horizons-orbital-mechanics 1.1 (Horizons
  queries, comet record pinning), provenance-discipline 2.28 (numbers
  in served descriptions, the export, the gate), gallery-cache-builder
  1.8 (daily_run.py, objects_config.json, the mirror),
  safe-file-editing 1.13, agentic-pre-test 1.3,
  ledger-and-session-records 1.18. In the first reply, read back each
  loaded version. Two obligations travel to this session and are
  discharged by that read-back: provenance-discipline must read 2.28
  (L-414, the scanner's window, closes on that confirmation) and
  gallery-cache-builder must read 1.8. The protocol is
  PROJECT_INSTRUCTIONS.md v3.89.

## Read this first

- *Nothing is left to design. Every question the design left open was
  ruled on October 8. This session builds.*
- *The check must be shown failing before it is trusted passing. The
  first live run will show every entry agreeing, because
  horizons_name is filled from JPL's own answers; only planted wrong
  entries prove the check can fail.*
- *The sandbox most likely cannot reach JPL. The build is tested
  against the companion file's recorded answers; Tony's first Daily
  Run after the push is the first live run, as the design says.*
- *One question for Tony, in one message, at the gallery half: the
  name the website shows for Encke (section 3).*

## 1. Settled, so the session does not ask

- The check finds an entry's object in three steps: search JPL's
  Lookup for the entry's `id` in the index its `id_type` points at;
  keep only the match whose primary id (major bodies) or primary
  designation (small bodies) equals the `id`; exactly one must remain.
- Fields compared: `id`, `id_type`, `horizons_name` (character for
  character), and `object_type` only for "barycenter" and the Sun.
  Descriptions and links are never compared.
- `horizons_name` is a new field on each keyed entry, JPL's exact
  name. `name` does not change anywhere; the display-name rename is a
  later round. Values for the twelve are in the design's section 5;
  Halley's is "1P/Halley" (the main service's form for a pinned
  record), Encke's "2P/Encke".
- Halley is keyed and checked too (Tony, 2026-10-08: "yes, and follow
  the new url rule"). Its link moves to NASA's 1P/Halley page; Encke's
  entry links NASA's 2P/Encke page. Both descriptions are the
  no-number sentences recorded on L-395; nothing in either carries a
  number (Tony: "No numbers unless they come from the store").
- Encke's new list entry: `name` "Encke", `id` 90000091, `id_type`
  "smallbody", `horizons_name` "2P/Encke", `key` "encke", and
  everything a list entry carries, following Halley's entry as the
  pattern. Check first what else in the orrery looks Encke up by
  name. The entry makes Encke selectable in the orrery's own window.
- Pinned records (Halley 90000030, Encke 90000091) are checked through
  Horizons' main service, not the Lookup: the record exists and its
  name equals `horizons_name`; the pin is the newest record for the
  designation, else "pin is stale" for Tony, never re-pinned; the
  solution date is recorded as information.
- Where it runs: the live check is a Daily Run step before the cache
  builder, with its own Dashboard button; the offline checker is in
  the gallery maintenance run and never touches the network. The
  Daily Run's OneDrive pause step was removed on 2026-10-10 (L-216,
  gallery-cache-builder 1.8), so the steps today are the guest book
  updater, the cache builder, the offline maintenance run; the check
  goes in after the guest book updater. The design's "ask Tony about
  the pause" is moot.
- Cadence: each object re-confirmed every 30 days and at once after
  its entry changes. One query at a time with a short pause; any error
  is "could not reach JPL" and never passes; no rapid retries.
- Confirmations are recorded in a small file in the gallery's data/
  (the design suggests `data/horizons_confirmations.json`): the date
  and what was confirmed, per entry. The offline checker fails when a
  served object was never confirmed, is overdue, or has had `id`,
  `id_type` or `horizons_name` changed since its confirmation.
- What each run prints is the design's Question 5, in full: the copy
  checked and the orrery commit; counts examined, due, queried; one
  line per entry; for a pinned comet, the pin's status and solution
  date; for each disagreement, the field, both values one above the
  other, and the exact query to paste into a browser; a closing PASS
  or FAIL naming every disagreeing entry and field.
- The check never edits the list. Simple errors it finds are fixed and
  reported by a session's patch; choices go to Tony.
- MAPS and 3I/ATLAS stay tested cases in the offline tests, not live
  checks, until the website serves them.

## 2. The orrery half

- `celestial_objects.py`: `horizons_name` on the thirteen keyed
  entries (the twelve plus Halley); Halley's `key` and the moved link;
  Encke's new entry. A credit line per module touched.
- `export_objects.py` and `test_objects_export.py`: the export carries
  `horizons_name` and `key` for Halley and Encke; the test fails on a
  keyed entry without a `horizons_name`, shown failing on a planted
  copy first.
- provenance: the two descriptions carry no number; the export's
  typed rows stay clear; the scanner's last line still reads "GATE
  PATH: 0 TIER-1".
- agentic-pre-test: py_compile; the xvfb run with Encke selected in
  the orrery's window, so the new entry is on the live path (the
  dispatch is the proof, not the dictionary); the maintenance run on a
  copy, 21 of 21; the patch twice over and on a CRLF copy.
- Then Tony's stop: run the orrery patch, the maintenance run, commit
  and push. The session re-reads HEAD before the gallery half.

## 3. The gallery half

- The live check: a new script in `tools/`, named for what it does
  (`horizons_check.py` or the like), with a Dashboard button the way
  Earth Pole Live Check has one, and the Daily Run step. It reads the
  pulled `data/objects_export.json`, never `celestial_objects.py`.
- The offline checker in `gallery_maintenance_run.py`, gating, shown
  failing on a copy with a confirmation deleted, one overdue, and one
  whose `horizons_name` was edited after its confirmation.
- The offline tests of the live check, built on the companion file's
  recorded answers and run without the network: every one of the
  thirteen agrees; then planted wrong entries, each caught by name: a
  wrong `id`, an `id_type` pointing at the other index, a
  `horizons_name` off by one character, a stale pin (an older record
  number), and JPL unreachable (which must fail, not pass). The
  companion file says to re-fetch each answer once first; if the
  sandbox cannot reach JPL, say so and record it, and Tony's first
  Daily Run is that re-fetch.
- The mirror: Encke's identity facts now come through the export like
  the other keyed objects; the gallery's own Encke note ("2022-epoch
  solution", wrong; JPL says 2023) goes. **The one question for Tony:**
  the mirror would write the list's `name` "Encke" over the gallery's
  current "2P/Encke" as the website's displayed name. Show him how
  Halley is displayed on the website today and ask, in one message,
  which form Encke should show. Record the answer on L-395.
- The gallery's Daily Run and dashboard words: plain, with the step's
  purpose in one sentence, the way the other steps say theirs.
- Then Tony's steps: run the gallery patch; run the Daily Run (its
  new step is the first live run; expect PASS with every entry
  agreeing, and the two pins current); the offline maintenance run;
  commit and push; the live maintenance run after the push.

## 4. At the close

- The ledger: L-395 (the Horizons check) records the check built and
  its first live run from Tony's run record, by name; Encke's entry
  done; Halley keyed; its Gap narrows to what the design already
  lists as open (fields the list lacks, the remaining served objects,
  L-391 to L-394; the numbers in the other descriptions are L-403).
  L-414 (the scanner's window) closes on the 2.28 read-back, with the
  line saying so. L-216's re-homed `daily_run.py` note is answered by
  L-429's removal of the pause; strike or point.
- Tony's page, by section, handles labelled, nothing below the
  marker: road stage 8 becomes done; the box says what the Daily Run
  now checks and that the Oort cloud build is next. The page is at
  130 lines above the marker, the cap: trim before adding.
- The handoff: `documentation/HANDOFF_L395_horizons_check_build_20261010.md`
  in the orrery, anchored on both HEADs at start, at the middle push,
  and at the close.
- The obligation that travels: none new unless a skill is bumped. If
  horizons-orbital-mechanics gains a field note from this build (the
  Lookup cannot see record numbers; the three-step find), that is one
  version, 1.2, and the next session confirms it. Do not bump a second
  skill in the same session.

## 5. Not this session

- The display-name rename (names used as keys), the clean kind field,
  the remaining served objects: L-395's later rounds.
- The Oort cloud build (L-421), which follows this one, from
  `documentation/HANDOFF_L421_oort_orrery_build_brief_20261009.md`.
- L-425 (citation location checks) and L-424 (the checker's one
  word): Tony's decisions, not this build's.

Brief written October 10, 2026, with Anthropic's Claude Fable 5.1.
