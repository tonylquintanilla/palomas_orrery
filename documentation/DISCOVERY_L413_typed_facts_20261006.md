<!-- Doc-Kind: hand | Discovery list: facts and citations typed in code in the Earth and Sun rooms (L-413), 2026-10-06. -->
# Discovery: facts typed in code, Earth and Sun rooms

Built on gallery ed48d078ceb639f5f98f13f4c6abc129f722c566 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, with
`patch_L413_6_earth_website_20261006.py` applied (not yet pushed), and orrery
51436054330aefd6be2a7efd93ebd58f06c4a2d2 at
https://github.com/tonylquintanilla/palomas_orrery. Written October 6, 2026,
with Anthropic's Claude Opus 5.5.

This is DISCOVERY only, under the Braid: it lists, it fixes nothing.

## How it was found

Both rooms were built headless twice: once as served, and once with every
served word replaced by a marker (name, description, about, note, source,
info_url, the belts' parallel lists, `_model`, `_declared`, `_comment`).
Any hover or info-panel sentence that still appeared without the marker was
not served. Each one was then traced to the line that types it. Numbers were
left as served; the display-figures check already accounts for every number
in an Earth hover.

## The pattern

A sentence may be typed in code when it is about OUR PICTURE: a drawing
choice ("drawn round", "our choice for the picture"), a frame limit ("drawn
to the edge of the arrival frame"), or how to use the page ("click the i
button"). It may not be typed in code when it states something about NATURE,
about a PAPER, or names a SOURCE. Those belong with the feature's served
words, with their source, under the rule written for "protons" this session.

## Earth room

| # | Where it is typed | What it says | Kind |
|---|---|---|---|
| E1 | `earth_geometry.js`, axis panel source | Archinal et al. (2018) for the sense of rotation | citation |
| E2 | `earth_geometry.js`, axis hover | prograde, west to east, counter-clockwise seen from above the north pole | fact (E1's) |
| E3 | `earth_geometry.js`, axis hover | the axis slowly circles over thousands of years and nods slightly | fact, no source |
| E4 | `earth_geometry.js`, pole-of-date panel source | Horizons observer quantity 32, target 399; tilt against target 3 | description of the fetch |
| E5 | `feature_renderers.js`, GEO ring hover | satellites here keep pace with Earth's turning and hang over one longitude | fact, no source |
| E6 | `feature_renderers.js`, magnetopause hover | "Shue et al. (1998)"; as far as the paper plots its model; the model is symmetric about the Sun line | citation, facts about the paper |
| E7 | `feature_renderers.js`, bow shock hover | "Jelinek et al. (2012)"; how far round the crossings the fit was made from reached; the fit is symmetric about the Sun line | citation, facts about the paper |
| E8 | `feature_renderers.js`, magnetotail hover | how far the spacecraft went; at any moment the tail is often flattened | facts |
| E9 | `feature_renderers.js`, outer belt hover | where the belt is most intense | fact |
| E10 | `feature_renderers.js`, both belts' hovers | 2020, IGRF-13 model | epoch and model of a served number (already L-322) |
| E11 | `earth_geometry.js`, terminator hover | the real terminator sweeps around Earth once a day; refraction and solar-disc corrections define sunrise on the ground | facts, no source |
| E12 | `earth_geometry.js`, Moon arc hover | the real path drifts as the Sun and Earth's shape perturb the two-body orbit | fact, no source |
| E13 | `earth_geometry.js`, Sun direction and terminator hovers | the subsolar point is where the Sun is overhead | definition |

## Sun room

The Sun's info panel is wholly served. Four hover sentences are typed:

| # | Where it is typed | What it says | Kind |
|---|---|---|---|
| S1 | `feature_renderers.js`, inner Oort cloud hover | drawn flattened toward the ecliptic, as the inner cloud is thought to be | fact, no source |
| S2 | `feature_renderers.js`, outer Oort (clumpy) hover | where the clumps really are is not known | statement of the unknown |
| S3 | `feature_renderers.js`, galactic tide hover | its thickness at each latitude follows how strongly the tide pulls there; where the comets really are is not known | model statement, statement of the unknown |
| S4 | `feature_renderers.js`, streamer belt hover | its warp and width are drawn to show the shape, not measured | drawing choice (may stay) |

## Not in this list

- Each room's own description in `interactive.html` (the skill allows page
  text, with its source in the page). Not yet read sentence by sentence.
- The orrery's own hovers. This list is the website's two rooms only.
- Whether the citation in `objects_config.json` and the one in
  `constants_new.py` agree for each served number. Not yet checked.
