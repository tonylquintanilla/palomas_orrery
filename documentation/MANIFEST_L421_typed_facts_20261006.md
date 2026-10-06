<!-- Doc-Kind: hand | Build manifest: move the facts typed in the Earth and Sun rooms' code into the served data, with their sources (L-421), 2026-10-06. -->
# Build manifest: the facts typed in the rooms' code (L-421)

Written against orrery 51436054330aefd6be2a7efd93ebd58f06c4a2d2 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
ed48d078ceb639f5f98f13f4c6abc129f722c566 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, with the
gallery's `patch_L413_6_earth_website_20261006.py`, which Tony then ran
and pushed at gallery 38f1e7b058ac359d5b7806fc3d2fe7da77d48e64, with his
look on the phone "correct". The orrery has since moved to e7073fce (the
galactic plane and the panel colour, no change to these rooms). October
6, 2026, with Anthropic's Claude Opus 5.5.

THE BUILDING SESSION FIRST re-reads both repos' HEAD and confirms
patch_L413_6 landed: `tools/record_earth_scene.py` exists, Earth's belts
in `data/objects_config.json` carry `flux_peak_of`, and the gallery run
counts 24 checkers. It builds on that HEAD, never on this manifest's
base. If patch_L413_6 is not in, stop and ask.

## The goal

The Earth and Sun rooms are the current slice. When this is done, no
sentence in either room's hovers or info panel states something about
nature, about a paper, or names a source unless it is served, with its
source, beside the feature it describes. Tony's word, 2026-10-06: "the
work is here. We should handle it now," completing the Earth and Sun
slices under the Braid. He approved this plan "as recommended" the same
day.

## The rule (written into interactive-exhibit 1.12 by this session)

Code may type a sentence only when it is about OUR PICTURE: a drawing
choice ("drawn round", "our choice for the picture"), a frame limit
("drawn to the edge of the arrival frame"), or how to use the page. A
sentence about nature, about a paper, or naming a source is served with
its feature's words, with its source, and the renderer prints what it
is given. Where such a fact has no served row, the fix is a served row.

## How the list was found

Both rooms were built headless twice, once as served and once with
every served word replaced by a marker. Any sentence still present
without the marker was typed. The first run missed the `_model` key, so
it reported the magnetopause's and bow shock's formulas as typed; they
are served. The survey script is not in either repo; the building
session should turn it into a check (step 7 below).

## The items, and the decision for each

"Words kept" means Tony's existing wording moves unchanged. Any change
of wording is his call before it is built.

| # | Room, feature | Typed now | Decision |
|---|---|---|---|
| E1 | Earth, rotation axis (panel source) | Archinal et al. (2018) citation for the sense of rotation, in `earth_geometry.js` | Serve it on Earth's `orientation` entry, as the source of a new words row for the sense of rotation. The citation was read when it was written; re-read it before serving. |
| E2 | Earth, rotation axis (hover) | "prograde, west to east, counter-clockwise seen from above the north pole" | Words kept, served on the same row as E1. |
| E3 | Earth, rotation axis (hover) | "The axis slowly circles over thousands of years and nods slightly, so the pole and the tilt belong to that date." | Needs a source (precession and nutation; the IERS Conventions are the likely one). Serve on `orientation`, or remove and note the gap. |
| E4 | Earth, pole of date (panel source) | The Horizons query described in `earth_geometry.js` (quantity 32, target 399; target 3) | The served `pole_of_date` already carries `pole_source` and `orbit_source`. Print those; delete the typed copy. Check the two say the same before deleting. |
| E5 | Earth, geostationary ring (hover) | "satellites here keep pace with Earth's turning and hang over one longitude" | Needs a source for the definition. Serve as a hover word on the ring's row, or remove and note. |
| E6 | Earth, magnetopause (hover) | "Shue et al. (1998)"; "as far as the paper plots its model"; "the model is symmetric about the Sun line" | The served source and `_model` already cite Shue. Serve the sentence as a hover word with gaps for the served cut angle and conditions. Words kept. |
| E7 | Earth, bow shock (hover) | "Jelinek et al. (2012)"; "how far round the crossings the fit was made from actually reached"; "the fit is symmetric about the Sun line" | As E6, against the bow shock's served source. Words kept. |
| E8 | Earth, magnetotail (hover) | "which is how far the spacecraft went"; "Drawn round, its average shape; at any moment it is often flattened" | The served source already names Slavin et al. (1983) for 220 Earth radii and Sibeck and Lin (2014) for the flattening. Serve the sentences as hover words. "Drawn round" is a drawing choice and may stay typed; split the sentence there. |
| E9 | Earth, outer belt (hover) | "where the belt is most intense" | The served source (Li et al. 2025) says it. Serve in the belts' parallel lists. Words kept. |
| E10 | Earth, both belts (hover) | "2020" and "IGRF-13 model" | The served tilt's source states both. Serve them as fields on the `magnetic_tilt` row (an epoch and a model name), from the orrery store if the store can hold them. Already on L-322 as a class; this closes Earth's case. |
| E11 | Earth, terminator (hover) | "The real terminator sweeps around Earth once a day"; "the refraction and solar-disc corrections that define sunrise on the ground are not applied" | Needs a source for the sunrise definition (a refraction and solar-radius convention). The once-a-day sweep follows from the served rotation period; say so from the served row. |
| E12 | Earth, Moon arc (hover) | "the Moon's real path drifts from it as the Sun and Earth's shape perturb the two-body orbit" | Needs a source. Serve on the Moon's own entry in `data/objects_config.json`, or remove and note. |
| E13 | Earth, Sun direction and terminator (hover) | "the subsolar point, where the Sun is overhead" | A definition. Serve with a glossary source, or ask Tony whether a definition counts as the picture's own words. |
| S1 | Sun, inner Oort cloud (hover) | "Drawn flattened toward the ecliptic, as the inner cloud is thought to be" | The served note already says the inner cloud is flattened, with no source. Find one or remove and note; then serve the hover's words. "The thickness is chosen for the picture" stays typed. |
| S2 | Sun, outer Oort (clumpy) (hover) | "where the clumps really are is not known" | The served note says it. Print from the served words. |
| S3 | Sun, galactic tide (hover) | "how thick it is at each latitude follows how strongly the tide pulls there"; "Where the comets really are is not known" | The served note says both. Print from the served words. |
| S4 | Sun, streamer belt (hover) | "Its warp and width are drawn to show the shape, not measured" | A drawing choice. Stays typed. |

## Where the drawn guides' words go (Tony's approval, 2026-10-06)

The axis, the Sun direction, the day-night line and the Moon's arc are
drawn by `earth_geometry.js` from served inputs and have no served entry
of their own.
- The axis: Earth's `features.orientation` entry, which already serves
  the pole and the rotation period.
- The Moon's arc: the Moon's own entry in `data/objects_config.json`.
- The Sun direction and the day-night line: a new words-only entry on
  Earth. The renderers must skip it as they skip `orientation`, and the
  checks that count served groups and shells must be read for what it
  does to them before it is added: `sweep_collapsed_features.py` (exit 2
  on a group it cannot classify), `tools/check_cache_in_step.py`, the
  geometry check's "every served group has a renderer", and the store
  writer's allow list.

## The mechanism, for the building session to settle

- A served hover word per feature, printed where the typed sentence
  was, with gaps the renderer fills from served numbers on the same row.
  The renderers already fill `{low}`, `{high}`, `{drawn}` and `{pc}` in
  notes (`fillNote`); widening that to name any numeric row of the same
  member is one way. The building session decides and writes the choice
  into interactive-exhibit, since it is method.
- The belts keep their words in parallel lists, as `flux_peak_of` does.
- `tools/store_writer.py` learns every new word field, and
  `tools/exhibit_store_editor.py` shows them, or says why it does not.
- `tools/record_earth_scene.py` was written this session to remake the
  saved Earth scene. interactive-exhibit already describes a headless
  recipe in `tools/headless/`. Read that first and fold the recorder
  into it if it duplicates it.

## The steps

1. Research: E3, E5, E11, E12, E13 and S1 each get a source read in
   full, or are removed with the gap noted. No source from memory.
2. Orrery store, if E10's epoch and model become rows: `constants_new.py`,
   then the export.
3. Gallery config: the new word fields and the guides' entries, written
   by the tools that own them (`mirror_constants.py` for numbers,
   `store_writer.py` for words) or by an anchored patch edit.
4. Renderers: `gallery/feature_renderers.js` and
   `gallery/earth_geometry.js` print the served words.
5. Checks: every check that pins a moved sentence follows it --
   `documentation/smoke_display_figures.js` (acceptance lines),
   `documentation/smoke_earth_geometry.js` (the axis and belt pins),
   the hover budget (no hover over 17 lines). The hover fixture and the
   saved Earth scene are re-recorded after an imitation cache rebuild.
6. Tony's look on the phone: both rooms, every hover that moved.
7. The survey becomes a gating check in the gallery run: it fails on any
   typed sentence in either room that is not on a short, named list of
   picture sentences. A check that cannot fail is not passing, so it is
   shown failing first.

## What this does not cover

- Each room's own description in `interactive.html`, which the skill
  allows as page text with its source in the page. Not yet read
  sentence by sentence; the survey in step 7 should read it too.
- The orrery's own hovers.
- Whether the citation in `data/objects_config.json` and the one in
  `constants_new.py` agree for each served number. Not yet checked;
  recorded on L-421 as its own question.
