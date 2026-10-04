<!-- Doc-Kind: hand | Session record: the lobby's wide Solar System card (L-363), built beside the L-371 session. -->
# Handoff -- 2026-10-04: the lobby's wide Solar System card

Built on orrery 17ef66607cbe63ac5ed7bdbff15397fbe546ae42 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
df8bbabdb73a4e1b7f60b4d541e2e2a758e2f0ad at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Records written at orrery a841ab6ee36fbbcef936408bc87774bc32a7598d and
gallery d4b408e60b1d9a45252174ca4a2c861ca17b49a5, by
`patch_L363_12_orrery_session_records_20261004.py`.

Type: BUILD (gallery), plus this record.
Companion: the L-371 session ran at the same time in another chat. Its
record, `documentation/HANDOFF_L406_L407_L371_session_20261003.md`,
also holds Tony's run records for this session's two gallery patches.
Supersedes: nothing.

## 1. Check first

- Nothing. No skill or protocol changed this session.
- Loaded and matching the manifest: interactive-exhibit 1.10,
  gallery-pipeline 1.2, safe-file-editing 1.11,
  ledger-and-session-records 1.14. provenance-discipline 2.25 and
  earth-system-pipeline 1.2 were read for their version lines only.

## 2. What was done

- **Two sessions at once, on purpose.** Tony asked whether this session
  could build the lobby card while the other built the Sun's distance
  cards. The two touched no file in common. This session kept off
  `interactive.html`, so the swap of a bare `interactive.html` link
  (design section 7) was left out. Shared records were written last,
  after the other session's orrery push. Each patch names its repo in
  its file name and refuses to run in the other repo.
- **Gallery patch_L363_10, pushed at 3c65b8a7.** In the lobby the
  Solar System card is drawn full width at the top of Featured, above
  the grid, as in sketch C of Tony's canvas
  (https://claude.ai/artifact/ELfZfhvvyHjckJPY9829Ks): the picture,
  "SOLAR SYSTEM - START HERE", the title, the sentence, the Interactive
  tag. The same card comes first under "Exhibits here" on the door's
  page. The lobby's doors stop counting rooms under construction. The
  empty room `solar_system/solar_system` is removed from
  `gallery_config.json`.
  - How: four new fields on the card in `gallery_metadata.json` --
    `wide`, `kicker`, `picture`, `picture_alt` -- and one writer,
    `wideCardHtml()` in `index.html`, used by the lobby and the door
    page. Any card served `"wide": true` is drawn this way.
  - The gallery editor keeps fields it does not show:
    `tools/gallery_editor.py` updates a card in place rather than
    rebuilding it [verified @df8bbab, read].
  - Tested headless with jsdom on a copy: the lobby and the door page
    draw as above at 390 and 1280 px; a tap on the card opens the room.
    The gallery maintenance run passed 23 of 23 in the sandbox and on
    Tony's machine.
- **Gallery patch_L363_11, pushed at d4b408e6.** The picture zoomed so
  Mars's orbit spans 80% of its width, with no grid (Tony's version B).
- **Gallery patch_L363_13, not yet pushed when this was written.** The
  card's sentence ends "Daily updates from JPL Horizons." instead of
  "Live data from JPL Horizons." Its push SHA is in Tony's run record.
- **The picture is drawn, not a screenshot** (Tony's choice). The
  room's real Python driver, run on the served data for noon UTC on
  October 4, 2026, drawn by Plotly 5.24.1 (plotly.js 2.35.2, the
  page's version) with the room's camera and colours.
  `tools/headless/draw_room_still.py` redraws it byte-for-byte; it is
  Claude-only, like the rest of `tools/headless/`.
- **Tony's phone check** (run record, 2026-10-04): the doors, the tap
  into the room, the door page, sideways and desktop all correct. His
  one change was the zoom. His look at the zoomed picture is not
  recorded.

## 3. Tony's rulings this session

- This session may build the lobby card beside the L-371 session.
- Claude draws the picture from the room's data.
- The card's sentence: the sketch's, then "Live data from JPL
  Horizons." The title "The Solar System, live" was already his
  (2026-10-03).
- The empty `solar_system` room is removed.
- All three lobby doors drop "rooms under construction".
- Zoom so Mars's orbit is about 80% of the width; version B, no grid.
- "Daily updates from JPL Horizons." replaces "Live data from JPL
  Horizons.": the data comes from the daily run, not a continuous feed.
  The title's "live" stays.

## 4. Discrepancies surfaced

- **A count given wrong in chat.** Claude said the Solar System door's
  empty rooms would go from 7 to 6. The headless run showed 8 to 7.
  Corrected in chat; it now shows only on the door's own page.
- **No check reads the lobby.** No gating checker opens `index.html`'s
  lobby code, so the 23 passes say only that nothing else broke. The
  phone was the check. Recorded on L-363, not chased.
- **The stray folder again.** Tony's maintenance run reported
  `data/solar-system (1)` in his gallery copy, the same OneDrive shape
  as L-400, which he deleted on 2026-10-01. Recorded on L-216.

## 5. Open, next

- The front door's remaining step is unchanged: a bare
  `interactive.html` link opens the Solar System room and the Explorer
  gets its own address (design section 7), after the Sun's slice.
- The picture shows the planets on October 4; the room always shows
  now. Redraw with the tool when wanted, and change `picture_alt`'s
  date with it.
- For gallery-pipeline's next version, carried on L-363: the wide
  card's four fields and the picture's tool. No sentence in the
  current skill is wrong, so nothing is bumped now.

## Tony-actions

- (do) Delete the folder `data/solar-system (1)` in the gallery copy,
  with OneDrive paused, as on 2026-10-01.

Session written October 2026 with Anthropic's Claude Opus 5.5.
