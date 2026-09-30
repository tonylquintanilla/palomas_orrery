# Handoff -- L-363 The Solar System room: Half 1 done; Half 2 starts when L-322 Stage D closes

**Built on orrery `2a7d26b9fc200a1ceae6afb3af541e5d60c33f54` at
https://github.com/tonylquintanilla/palomas_orrery and gallery
`a484172fc17ec73ed801fbeab8eae2ebf0c945e1` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.** Both
HEADs read live with `git ls-remote` on 2026-09-28, after Tony pushed
patch 5. This session wrote nothing to either repository itself; every
change went through a patch Tony ran.

**Type: DESIGN, then BUILD.** Half 2 opens with a short design round
(section 5), one question at a time, then builds.

**Starts when L-322 Stage D closes.** Tony's ruling, 2026-09-28. At the
anchor above, Stage D's gallery patch for L-345 has landed (gallery
`7b230cf8`), and one piece remains: orrery patch D20, which retires the
13 conversion rows and restamps the master plan to v34. It is described
in `documentation/HANDOFF_L345_D19_done_gallery_next_20260928.md`,
section 4b. Before starting, confirm D20 has landed: its patch file in
the orrery's `documentation/`, and L-322's status in the ledger. If it
has not, Half 2 waits: it edits `data/objects_config.json` and rebuilds
the cache, which Stage D also touches.

**Supersedes** `documentation/HANDOFF_explorer_symbols_half1_20260926.md`
(rev 2) for what remains. That file stays the record of Half 1's brief;
Tony's run of patch 5 is appended to it.

**Companion records:** ledger L-363 (the room) and L-364 to L-367 (what
building it found), filed at orrery `0e3d05f`. The five gallery patches
in section 1.

**Rules this work ran under.** Protocol v3.68 at the start, v3.72 by
the end. This session LOADED interactive-exhibit 1.4, gallery-assembler
1.3, gallery-pipeline 1.2, orrery-coding-conventions 1.9,
safe-file-editing 1.11, agentic-pre-test 1.2 and
ledger-and-session-records 1.11. Its loaded provenance-discipline read
2.18; this session did no provenance work. Another session has since
shipped **interactive-exhibit 1.5 and provenance-discipline 2.22**
(protocol v3.72). A reinstall cannot be seen from inside a running
session, so **the next session confirms its loaded copies read
interactive-exhibit 1.5 and provenance-discipline 2.22 before any
exhibit or provenance work.** Half 2 is both.

Written for Tony, a retired professional engineer who is not a
programmer, and for the session that builds Half 2.

---

## 1. What Half 1 built, and how each piece was verified

Six gallery patches, each run by Tony, followed by the gallery
maintenance run, pushed, and checked on his phone. The page, Studio's
converter and the editor at gallery `a484172f` all carry their changes
[verified @a484172f].

| Patch (gallery) | What it did |
|---|---|
| `patch_solar_system_room_half1_20260926.py` | The room, `interactive.html?exhibit=solar-system`: the Sun, Earth, Jupiter, Saturn and Apophis as their symbols on their orbits, from the served cache, with no shells. Each drawer row carries the body's name and its Horizons source; naming a body opens its text box at the body. Pushed at `8545cbd7`. |
| `patch_L363_2_studio_lists_quoted_room_keys_20260926.py` | Studio's New Interactive Card (and the editor's live-link list) now reads a room key written in quotes. The room's key has a hyphen, so JavaScript needs the quotes, and the list had skipped it without saying so. |
| `patch_L363_3_date_line_and_editor_save_check_20260926.py` | The room draws **now**, the minute it is opened, and says so under its title. The gallery editor refuses to save over a file that changed on disk since it loaded it, and names the file it opened. |
| `patch_L363_4_date_line_every_room_20260927.py` | Every room has the line, shortened ("27 Sep 2026, 13:44 UTC"). The Earth room draws now too. The Sun room's line reads "Long-term averages . no date" (with a middle dot). Each room's note explains the line. |
| `patch_L363_5_short_scene_titles_20260927.py` | The title inside each scene drops "Paloma's Orrery --". On an upright phone the title and line centre between the zoom buttons and the arrow cross, and move below the cross only if they would still touch a button. Pushed at `a484172f`. Tony's phone: all three rooms correct. |
| `patch_L363_6_site_credit_and_camera_20260928.py` | (1) Every relayout the rooms and the Explorer make carries the live camera. Tony found the + and - buttons snapping the view back to its opening orientation after a finger turn; framing from the drawer, turning the phone, and the title and credit placement did the same. The rule was already in interactive-exhibit (the touch path) and the drawer label followed it; the zoom code never had. (2) A small grey link, palomasorrery.com, just under the grid chip in every room, drawn as part of the scene so the camera button's picture carries it. Built on `63e657f`; **not yet run** when this handoff was written -- check whether it landed. |

The first four scripts are in the gallery's `documentation/`. Patch 5's
script was committed in the gallery ROOT at `a484172f`; it moves to
`documentation/` at the next cleanup (Tony-action, section 8).

**The card.** "Solar System", 9:16, placed in the `solar_system` door,
live link `interactive.html?exhibit=solar-system`, placard "Live data
from JPL Horizons. Work in progress." Made in Studio once patch 2 let
Studio list the room; pushed at gallery `3f7f50ab`. Its placement gives
the room its top-bar chain ("Paloma's Orrery | Solar").

**Orrery.** `patch_L363_ledger_solar_system_room_20260926.py` filed
L-363 to L-367 at orrery `0e3d05f`.

## 2. Tony's rulings in Half 1

- **Symbols first**, the way the orrery itself grew; each body's shells
  arrive with its own room.
- **Two halves**, because Stage D shares `data/objects_config.json` and
  the cache rebuild. On 2026-09-28: Half 2 continues after Stage D
  completes, not merely after its section 6.
- **Plan B for the key.** `solar-system` is permanent; the Explorer
  keeps `solar-system-explorer` and stays the default until Tony
  decides otherwise at Half 2.
- **Only bodies the cache stands behind today.** The four moons are left
  out (at this scale each sits on its planet). Pluto, Voyager 1 and the
  comets are out for the reasons in L-363 to L-365.
- **The line under the title is the reason for the exhibits.** Tony:
  "it is the reason for the exhibit at all."
- **Now, not midnight.** A visitor cannot choose a time yet, so the
  rooms that show positions draw the minute they are opened.
- **UTC only**, no local time.
- **Every room has the line.** The Earth room draws now. The Sun room
  draws nothing that changes with time and fetches nothing from
  Horizons (Horizons serves no solar wind; that would be NOAA's space
  weather service), so its line says it has no date.
- **The notes** explain the line. JPL is a laboratory, not an
  observatory: Horizons is "the Jet Propulsion Laboratory's service for
  where solar system bodies are".
- **Titles drop "Paloma's Orrery --"**, which the top bar and the
  address already say.
- **The camera's picture is what the scene shows.** The download is
  drawn from the scene itself, so it carries the short title and the
  date line, and not the page's top bar. Claude asked whether to put
  "Paloma's Orrery" back into the download alone; Tony, 2026-09-28:
  "why would the camera button snapshot something that is not
  displayed?" So it is not added. A credit on a download would first
  have to be something the scene shows. Tony then ruled exactly that:
  a link to palomasorrery.com under the grid chip, in the scene, in
  every room (patch 6).

## 3. The lost card, and what now prevents it

Studio wrote the card into `gallery/gallery_metadata.json` at 22:03 on
2026-09-26, and Tony's commit at 22:05 captured it. At 22:06 the file
was rewritten from an older copy without the card. The file carried
the gallery editor's save signature, but Tony had answered No to the
editor's save prompt, and the cause was never found. Tony restored the
card with GitHub Desktop's Discard changes.

What is known is why it could happen at all: the editor saved whatever
it held in memory without checking the disk. Patch 3 closed that. Save
All now compares both files on disk with what it loaded, and if either
changed it saves nothing and says to Reload from disk. Tested headless:
a card written behind the editor's back survived a Save All attempt.

## 4. Where the room stands at the anchor

- **Drawn:** the Sun (the scene's centre), Earth, Jupiter, Saturn,
  Apophis. The list is `SOLAR_SYSTEM_BODIES` in `interactive.html`,
  beside the room's row in `EXHIBITS`.
- **The room has no entry in `data/objects_config.json`.** Its choices
  live in the page's code, which is why no arrival block applies. The
  opening view is the rooms' rule: 1.1 times the largest thing drawn.
- **Each body's panel** shows its Horizons source and "No link on file
  for this body".
- **The info copy** says the room is being built up and names the
  bodies it draws. Half 2 rewrites both paragraphs.

## 5. Half 2: questions first, one at a time

Before asking Tony any of these, check whether a skill already answers
it (the protocol's "Method Belongs to the Skill"). Bring Tony only what
the skills cannot settle.

1. **The opening view.** With Uranus, Neptune and Pluto in, 1.1 times
   the largest orbit is about 54 AU, and Mercury to Mars shrink to a
   dot around the Sun. Open on everything, or frame something smaller
   first? Any answer other than the rooms' rule needs an opening
   setting for a room with no object entry, which no room has yet --
   check interactive-exhibit 1.5's arrival section first. This one is
   likely Tony's, and is visual (Mode 5).
2. **Pluto.** The served `pluto` is stored relative to the Pluto-Charon
   barycentre, and the assembler refuses by design to translate it into
   a Sun-centred scene. What the room draws as "Pluto" -- Pluto itself
   about the Sun, or the Pluto system's barycentre -- is likely method:
   orrery-coding-conventions (the barycenter rule) and
   horizons-orbital-mechanics.
3. **A link for each body.** No object carries a link of its own today;
   links live on features. Where a body's link lives in the config, and
   who may write it, is method: interactive-exhibit 1.5, "who may write
   `data/objects_config.json`".
4. **The default room (Tony's decision).** Under plan B, whether the
   new room becomes the default once it has every planet, and what
   happens to the Explorer's card and to the new room's card. Now that
   the new room has its own card in the `solar_system` door, "update
   the Explorer card's live link" may no longer be the right move.

## 6. Half 2: the build, in order

1. **Five planets and Pluto into `data/objects_config.json`:** Mercury,
   Venus, Mars, Uranus, Neptune, and the Pluto entry question 2 settles.
   Check each Horizons target and centre against
   horizons-orbital-mechanics before writing it. Then one cache rebuild
   (gallery-cache-builder; Tony pauses OneDrive first).
2. **Check each new body's OWN trust window covers today,** not only
   the cache's overall served window. That gap is L-364: the overall
   window passed while Halley's and Encke's own windows did not cover
   today.
3. **The room:** extend `SOLAR_SYSTEM_BODIES`, rewrite the two info
   paragraphs (the bodies drawn; what is still missing), and the links
   from question 3.
4. **The hovers under the bumped skills.** A body's hover comes from the
   assembler: its distance in AU to six decimals, then in km. Read it
   against interactive-exhibit 1.5 ("a hover prints a unit it is served
   and never converts a served number to print it") and
   provenance-discipline 2.22. Positions are computed, not served, so
   the rule may not reach them; decide from the skills, and bring Tony
   only a case they do not settle.
5. **Tony's Mode 5** on his phone, upright and sideways, and on the
   desktop, with every visitor-facing word listed before the build.
6. **Question 4's decision,** applied.

The comets (L-364), Voyager 1 (L-365) and the orbit info cross (L-366)
are not Half 2.

## 7. How this session tested the rooms headless

No checker in the maintenance run opens a room (L-367), so each patch
was tested by loading the page in a headless browser. The recipe, for
reuse:

- Chromium through Python Playwright, which the sandbox has.
- Pyodide `314.0.2` (npm package `pyodide`) and Plotly `2.35.2` (npm
  package `plotly.js-dist-min`), installed from npm, because the
  sandbox cannot reach the CDNs. A Playwright route answers the page's
  `cdn.jsdelivr.net/pyodide/v314.0.2/full/` and `cdn.plot.ly` requests
  from those local files.
- The page's consent gate is passed by setting localStorage
  `palomas_orrery_pyodide_consent` to `yes` before load.
- Phone: 390 x 844, mobile, touch. Desktop: 1400 x 900. A time zone can
  be set on the browser context.
- **Two limits.** The Explorer needs Pyodide's numpy, which the sandbox
  cannot fetch, so it cannot be rendered here. And Google Fonts cannot
  load, so text is drawn in wider fallback fonts: anything that depends
  on text width -- whether a title fits beside the buttons -- is decided
  on Tony's phone, not here.

This recipe is method. It belongs in interactive-exhibit as a field
note at its next bump (section 8).

## 8. For the ledger, and Tony-actions

**Ledger, owed by the next session** (one update to L-363, plus notes on
two existing rows; no new classes):

- L-363 gains: patches 2 to 6 and what each did (patch 6 includes the
  snap-back fix: a rule the skill already had, missed by one caller --
  worth a line in the skill's touch-path section naming every caller); the card and where it
  sits; the rulings in section 2; the lost card and the editor's save
  check (section 3).
  Its Gap becomes section 5 and 6 of this handoff.
- L-367 gains: the headless recipe in section 7 is how the rooms were
  checked meanwhile.
- L-378 (phone behaviour has no automated check) gains: the sandbox
  cannot load Google Fonts, so a text-width layout decision is settled
  only on the phone.

**Tony-actions:**

- (do) File this handoff in the orrery's `documentation/`.
- (do) Move `patch_L363_5_short_scene_titles_20260927.py` from the
  gallery root into the gallery's `documentation/`.
- (do) Tell the D20 session that Half 2 of L-363 comes next after Stage
  D, so the master plan's v34 critical path (section 5a) can show it.
- (decide) At Half 2, question 4: the default room and the two cards.
- (later) Add the section 7 recipe to interactive-exhibit as a field
  note at its next bump.

## 9. For the next session

- Confirm D20 has landed and L-322 Stage D is closed. If not, stop:
  Half 2 waits.
- Confirm the loaded interactive-exhibit reads **1.5** and
  provenance-discipline **2.22**, and the other skills match the
  manifest.
- Re-anchor both repositories. Read L-363 in the ledger and the room's
  code in `interactive.html`; line numbers will have moved.
- File the ledger update in section 8.
- Start with section 5, question 1.

---

Session written September 2026 with Anthropic's Claude Opus 5.5.
