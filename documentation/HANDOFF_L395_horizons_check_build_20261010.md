<!-- Doc-Kind: hand | Build record for L-395, the Horizons check: the orrery's list gains JPL's exact names, Halley keyed, Encke's own entry; the gallery's live check as Daily Run step 2, its offline checker and tests; Tony's first live run, 13 of 13. Written October 10, 2026. -->
# Handoff: L-395, the Horizons check, built

Built on orrery ca5bbe12cb8f1c48b134f6aadaa700d45ae9e39d ("L427
records") at https://github.com/tonylquintanilla/palomas_orrery and
gallery 050637c3688e1bfcff81848ad4780b8a9e975a9e ("daily run again") at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, both
pinned with `git ls-remote` at the session's start.
Middle push (the orrery half): orrery d83cc5e ("L395 horizons name and
encke"), then 32619f8d with Tony's run record.
Gallery pushed at 4a34221 and a7d1a542 ("daily run again to check").
This record lands with `patch_L395_7_records_20261010.py`, built on
orrery 32619f8d; its push is the next commit.

- Type: BUILD, two repos. From
  `documentation/HANDOFF_L395_horizons_check_build_brief_20261010.md`.
- Skills loaded, read back in the first reply, each matching the
  manifest of protocol v3.89: provenance-discipline 2.28 (L-414 closes
  on it), gallery-cache-builder 1.8, horizons-orbital-mechanics 1.1,
  safe-file-editing 1.13, agentic-pre-test 1.3,
  ledger-and-session-records 1.18.
- Ledger: L-395 (the Horizons check) gains the build, the first live
  run, the comets' names and three findings; L-414 (the scanner's
  window) closes.

Session written October 2026 with Anthropic's Claude Opus 5.5.

## Read this first

- *The Daily Run's step 2 asks JPL Horizons about each object the
  website serves. Its first live run: 13 of 13 agree; Halley's and
  Encke's pinned records are JPL's newest.*
- *Encke has its own entry in the orrery's list, and a checkbox under
  Halley's.*
- *Still to do: Tony's look at Encke and Halley in the orrery window
  (section 6).*

## 1. The orrery half

`patch_L395_5_horizons_name_and_encke_20261010.py`, run by Tony and
pushed in d83cc5e.

- `celestial_objects.py`: `horizons_name`, JPL's exact name, on the
  thirteen keyed entries (Sun, Mercury, Venus, Earth, Mars, Jupiter,
  Saturn, Uranus, Neptune, "Pluto Barycenter", "99942 Apophis",
  "1P/Halley", "2P/Encke"). `name` is untouched everywhere.
- Halley: key `halley`; Tony's words of 2026-10-08; NASA's 1P/Halley
  page.
- Encke: a new entry, key `encke`, record 90000091, id_type smallbody,
  with Tony's words and NASA's 2P/Encke page. Nothing else in the
  orrery looked Encke up by name except `celestial_coordinates.py`,
  which already had a row for it.
- `palomas_orrery.py`: `comet_encke_var` and an "Encke
  (1786-present, periodic)" checkbox, perihelion "October 22, 2023".
  Both dates come from JPL's answers G4 and G3.
- `info_dictionary.py`: INFO['Encke'], the checkbox's tooltip. Fixed in
  passing: the file's only non-ASCII, the s-acute of "Wierzchos", twice.
- `export_objects.py` and `test_objects_export.py`: the export carries
  `horizons_name` and `object_type`; a keyed entry without a
  `horizons_name` is refused, and the test's self-test shows that
  refusal before it trusts a pass.
- Encke draws in the default goldenrod: `constants_new.py` has no
  Encke colour and the patch did not touch the store.

## 2. The gallery half

`patch_L395_6_horizons_check_gallery_20261010.py`, run by Tony and
pushed in 4a34221 and a7d1a542.

- `tools/horizons_check.py`: the live check, the Daily Run's step 2.
  It reads the pulled `data/objects_export.json`, finds each entry in
  the three steps of the design, checks a pinned record through
  Horizons' main service, and records each confirmation in
  `data/horizons_confirmations.json`. One query at a time with a pause;
  after the first failure it asks JPL nothing more that run.
- `tools/check_horizons_confirmations.py`: offline, gating; fails on an
  entry never confirmed, 30 days old, or changed since confirmed.
- `tools/test_horizons_check.py`: offline, gating, 36 checks on
  `documentation/horizons_answers_L395.json`.
- `daily_run.py`: four steps. `gallery_maintenance_run.py`: two rows.
- `data/objects_config.json`: Encke's note no longer says "2022-epoch".
- The website's names for the two comets became "Halley" and "Encke"
  through the objects mirror, by Tony's ruling (section 4).

## 3. Verification

- In the sandbox, on copies:
  - the orrery window headless with Encke ticked, through the real
    plot_objects(): JPL was asked for record 90000091 as a small body,
    and Encke, its Keplerian orbit and its tail were drawn;
  - a planted entry with no `horizons_name`: the test and the export
    both fail, naming Earth;
  - the orrery maintenance run 21 of 21, gate path 0 Tier-1 on 13
    served objects (it was 11);
  - every patch twice (the second refuses) and on a CRLF copy;
  - the gallery maintenance run: the two expected reds only, "Horizons
    confirmations" and "Cache in step".
- The sandbox cannot reach JPL. The chat's web-fetch tool can, so JPL's
  answers were re-fetched on 2026-10-10, fields compared rather than
  bytes. 25 of 28 read the same; the three differences are section 5.
  Fifteen answers the tests needed and the design had not fetched were
  fetched the same way; the fixture names each answer's source.
- Tony's runs, from `documentation/WHERE_WE_ARE_10-10-26_1426_run_record.md`:
  the orrery run "21 of 21 gating checkers passed"; the gallery's two
  expected reds; then the Daily Run's step 2, the first live run,
  "Examined 13 entries: 13 due, 26 queries asked of JPL", every entry
  "agrees", "HORIZONS CHECK: PASS -- 13 checked today, 0 not due";
  after its build "26 of 26 gating checkers passed"; the live run "2 of
  2". Tony: "correct."

## 4. Ruled this session

- The website's names for the two comets: "Halley and Encke
  (Recommended)", over "1P/Halley and 2P/Encke". Neither name was shown
  on a page at the time.
- Tony's local folders go into the handoff skill:
  "palomas_orrery_for_github is the repo folder." Recorded in
  ledger-and-session-records 1.19.
- Tony asked for the Horizons checks on the dashboard; patch_L395_7
  adds the three buttons.

## 5. Found, and where each went

- A recent comet's record number is not stable: 90004956 held MAPS on
  2026-10-07 and PANSTARRS (C/2025 Y3) on 2026-10-10, with MAPS at
  90004957. The orrery finds MAPS by designation and is unaffected. A
  test case now; horizons-orbital-mechanics 1.2.
- JPL re-solved Encke's record on 2026-10-09 under the same number.
  horizons-orbital-mechanics 1.2.
- The recorded "sstr=9" answer is identical to the major-body-only one,
  probably a paste slip: live, "9" also finds asteroid 9 Metis. The
  design's line that "9" found no asteroid was wrong. The check is
  unaffected. On L-395.
- The dashboard still told Tony to pause OneDrive. Fixed in passing by
  patch_L395_7.

## 6. Mode 5, Tony's look in the orrery window

1. Under Comets, below Halley: "Encke (1786-present, periodic)"; its
   tooltip reads "Horizons: 2P/Encke. A short-period comet whose dust
   trail is the source of the Taurid meteor showers." and "Perihelion:
   October 22, 2023".
2. Tick only Encke, centre on the Sun, today, plot: its marker, orbit
   and tail. The marker is goldenrod, the default; a colour of its own
   is one line in `constants_new.py` if wanted.
3. Go: Perihelion under Encke frames the October 2023 perihelion. Needs
   the internet; not testable in the sandbox.
4. Halley's hover shows its new words and NASA's 1P/Halley link.

## 7. Tony's steps

1. **(do)** Run `patch_L395_7_records_20261010.py` in the orrery root,
   then `orrery_maintenance_run.py`; move the patch into
   `documentation/`; commit and push.
2. **(do)** Upload ledger-and-session-records and
   horizons-orbital-mechanics (each its SKILL.md); replace the
   Project's instructions with `PROJECT_INSTRUCTIONS.md` (v3.90).
3. **(do)** The Mode 5 look, section 6.

## 8. What travels

- ledger-and-session-records went to 1.19 and horizons-orbital-mechanics
  to 1.2 in a session that loaded 1.18 and 1.1. The next session
  confirms its loaded copies read 1.19 and 1.2 before ledger or Horizons
  work.
- The brief asked for at most one skill version this session; Tony's
  request for his folders made it two.
- Next on the road: the typed facts, the inner Oort cloud first (L-421),
  from `documentation/HANDOFF_L421_oort_orrery_build_brief_20261009.md`.
