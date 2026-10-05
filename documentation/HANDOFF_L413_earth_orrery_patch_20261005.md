<!-- Doc-Kind: hand | Session record: Earth's orrery patch, the dashboard buttons, the skill limits and the skills' contents lists (L-413, L-416, L-417, L-418), 2026-10-05. -->
# Handoff: Earth's orrery patch, and the skills made readable

Built on orrery 72e3b55805c29f1f08a583864bd815a47e7434c6 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
624aa94557e16956b2fe022a467936ae2ccf3406 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Pushed
at: orrery d9f47a875 (the four build patches) and gallery
ed48d078ceb639f5f98f13f4c6abc129f722c566 (patch_L416_2), by Tony on
2026-10-05; this record is carried by patch_L413_4, built on d9f47a87.
Written October 5, 2026, with Anthropic's Claude Opus 5.5, mostly from
Tony's phone.

## What was done [verified @ orrery d9f47a87, gallery ed48d078]

Orrery, to run in this order from the repo root, each moved into
documentation/ before the maintenance run:
1. `patch_L413_2_earth_orrery_20261005.py` -- the geocorona shell and
   its checkbox (L-292); Earth's tilt said in words in four places and
   the star background reading the frame angle (L-369); notes on the
   atmosphere and LEO rows (L-389); the inner belt's words (L-349);
   the Upper Atmosphere tooltip showing its hover's words.
2. `patch_L416_1_dashboard_buttons_20261005.py` -- eleven buttons, so
   every step of both maintenance runs has one.
3. `patch_L417_1_skill_install_limits_20261005.py` -- the Skill
   headers check enforces Anthropic's documented limits.
4. `patch_L418_1_skill_contents_and_histories_20261005.py` -- six skills
   open with a contents list; history moved to
   documentation/SKILL_HISTORIES.md; protocol v3.81.
5. `patch_L413_4_session_close_20261005.py` -- this record, the
   Horizons handoff, the ledger, Where We Are. It replaces
   patch_L413_3, which refused and wrote nothing (L-419).
Gallery: `patch_L416_2_offline_check_wrapper_20261005.py` --
documentation/run_offline_check.py.

Tony ran the four build patches and the gallery patch and pushed both
repos. His orrery maintenance run passed 20 of 20 gating checkers with
the scanner at 296; his gallery offline run passed 23 of 23. Claude
compared the pushed dashboard, wrapper and six skills with the tested
copies: identical.

## Tony's run record and notes, 2026-10-05

Kept whole at `documentation/WHERE_WE_ARE_10-5-26_1627_run_record.md`.
His notes in it, each answered:
- On the Earth look: "unclear what the hover teal line refers to.
  otherwise correct." The teal-circle line is in the "Ecliptic
  Coordinates (J2000)" box at the plot's left, a box and not a hover;
  the step named it wrongly. The rest of the look is confirmed.
- On "then the gallery patch, which Claude builds after the push":
  "unclear, what 'after the push' means since i already have the
  patch." Two gallery patches were in play: patch_L416_2, the wrapper,
  which Tony had; and Earth's website patch, which is not built. The
  step meant the second.
- On the dashboard buttons: "please check. i cannot tell mode 5." The
  pushed dashboard is byte for byte the tested one, where all 92
  buttons found their scripts.
- On patch_L413_3: "refused. I am not sure why ... i though
  annotations would not be refused." It guarded Where We Are by a
  whole-file fingerprint, against Tony's rule of 2026-10-03; his
  "-- done" marks tripped it. L-419.
- "Reinstall the six skills ... -- done"; pushed orrery d9f47a875,
  gallery ed48d078.

## Tony's notes found in Where We Are when patch_L413_4 ran

The lines below differed from the page at d9f47a87 when the patch
rewrote it, carried here word for word so nothing he wrote is lost:

    (none: the page was as pushed at d9f47a87)

The page at d9f47a87 itself carried three: the header dated "-- **Tony**:
notes 10/5/26 --", and "-- done" on Needs you now and on Waiting on
you, both meaning the October 4 session's runs were done.

## Tony's rulings and confirmations, 2026-10-05

- L-349, the inner belt's words, "confirmed as recommended".
- The orrery patch's words: the geocorona shell, Earth's tilt in
  words, the Upper Atmosphere tooltip. "Approved."
- The exosphere is a candidate for fuzzy boundaries (L-410).
- L-389: the crust ruling of 2026-09-28 was about drawing a sphere;
  the equatorial radius stays the standard Earth radius, so heights
  stay measured from it. Claude had overstated the ruling; Tony
  corrected it.
- L-416: every maintenance-run step gets a dashboard button.
- L-417: Sonnet's skill-limit check rebuilt to project rules, without
  its 950-character warning.
- L-418: contents lists, three version entries, provenance-discipline
  in tier order, all six long skills including gallery-cache-builder.
- L-395: the Horizons check is verification of what is served; it gets
  a fresh session with its own handoff,
  `documentation/HANDOFF_L395_horizons_check_design_20261005.md`.

## Discrepancies surfaced

- The website's belt hover prints "where the measured particle flux
  peaks" for any belt with no band, including Jupiter's, whose
  distances are typed with no source. Recorded on L-349.
- The website's geocorona note says the orrery has no shell of its own;
  false after patch 1. For the website patch.
- Claude's first count of missing buttons was nine; matching against
  the runners' own lists found eleven.

## The website patch, not built this session

Planned, and left for a session at the machine because it needs care
this one could not give it from the phone:
- L-349 on the website: Tony's words for Earth's inner belt; the
  "measured" wording printed only for a belt whose row has a source,
  so Jupiter's belts make no claim. The approved words name protons,
  which is true of this belt only: the next session decides how the
  renderer knows that (a served field, or a rule on the row), and asks
  Tony if it needs a choice.
- The geocorona note: remove the sentence that patch 1 makes false.
- L-379: re-record documentation/payload_earth_scene.json from the
  current cache; the overlays retire. Read which smoke suites pin
  hover lines (smoke_display_figures.js's acceptance table does)
  before changing a word.
- L-300: register sweep_collapsed_features.py in
  gallery_maintenance_run.py, and give it a dashboard button.
Then Tony's look on the phone.

## Tony-actions, rolled up

(do)
- Delete patch_L413_3 from the orrery root; it wrote nothing.
- Run patch_L413_4, move it into documentation/, run
  orrery_maintenance_run.py, commit and push.
- Look at the "Ecliptic Coordinates (J2000)" box at the plot's left:
  its teal-circle line.

- Run patch_L419_1, reinstall ledger-and-session-records (1.16), and
  replace the Project's instructions with v3.82. Tony's word on
  L-419, 2026-10-05: write the rule now.

## Next session

- Confirms its loaded copies read provenance-discipline 2.26,
  interactive-exhibit 1.11, safe-file-editing 1.13,
  orrery-coding-conventions 1.10, ledger-and-session-records 1.15 and
  gallery-cache-builder 1.7, each opening with its contents list.
- Then the website patch above, or the Horizons design round, in
  Tony's order.
