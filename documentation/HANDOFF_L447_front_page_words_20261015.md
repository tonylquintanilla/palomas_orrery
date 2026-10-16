<!-- Doc-Kind: hand | Build record for L-447: the website's front page says what the site is, in Tony's words. Gallery only, words. -->
# Build record: the front page's words (L-447)

Built on gallery 9f8569ee3125de27fed96c86c701e3c4d52d88e3 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io; records
on orrery 47d241bc32c4a21a9a183d7f58873bc75f157997 at
https://github.com/tonylquintanilla/palomas_orrery.
Pushed at: (Tony's commits after his run).
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 15, 2026 with Anthropic's Claude Opus 5.5, in the L-444
session, which took this on at Tony's request.

- Type: DESIGN and BUILD, gallery only, words.
- Patches: gallery `patch_L447_1_front_page_words_20261015.py`; orrery
  `patch_L447_2_records_20261015.py` (this record, the ledger, Where
  We Are).
- Ledger: L-447, OPEN until Tony's look on the phone.

## 1. Skills, and what was read

- Loaded, each matching the manifest: gallery-pipeline 1.2,
  interactive-exhibit 1.15, provenance-discipline 2.29,
  safe-file-editing 1.13, ledger-and-session-records 1.21.
- L-428 (the lobby's way in), whose design this keeps: the title, the
  start card, the subject doors, Featured, the guest book.
- The front page as served at 9f8569e, screenshotted headless on a
  phone (390 x 844) and a desktop (1280 x 800).

## 2. The words, and Tony's ruling

Three versions of two lines went to Tony with a pick. His answer,
2026-10-15: "Confirmed as recommended, A and love in 3D" ("live").

    Explore the solar system, the Earth and the nearby stars in 3D,
    built from real science data such as NASA JPL's Horizons.

    An orrery is a model of the solar system. I built this one for my
    daughter Paloma, whose name is Spanish for dove.

"Interactive scenes" reads "live in 3D"; "exhibits" stays. No number is
in the words, and each claim is one the site's "i" card already makes
(JPL Horizons, the daughter, the subjects), so provenance asks nothing
more of them.

## 3. What was built

- `gallery/gallery_config.json`: "sentence" becomes the first line; a
  new "name_note" beside it holds the second. Both tools that rewrite
  the config, `tools/gallery_editor.py` and `tools/guestbook_updater.py`,
  load and write the whole file, so the new field survives them.
- `index.html`: `renderLobby()` prints the name note under the
  sentence, smaller and in italics, in the lobby's near-white with its
  shadow, padded on a phone as the sentence is; "live in 3D" at the
  three places a count was built from "interactive scene" (the doors,
  the subject page, its room rows); the same sentence as the fallback,
  the no-script text, and the og and twitter descriptions; the header
  comment stamped.

## 4. What was verified

- On a throwaway copy of 9f8569e with the patch applied: the screenshots
  Tony saw before running it; the Enter button ends about 660 px down
  on the phone, inside its first screen; the gallery's maintenance run,
  27 of 27 gating checkers; a second run of the patch refuses.
- The phone's look is Tony's, and is the acceptance.

## 5. Tony's actions

- (do) Save `patch_L447_1_front_page_words_20261015.py` in the gallery
  folder and click Run; run `gallery_maintenance_run.py`; move the patch
  into the gallery's `documentation/`; commit and push the gallery.
- (do) Save `patch_L447_2_records_20261015.py` in the orrery folder and
  click Run; move it into `documentation/`; run
  `orrery_maintenance_run.py`; commit and push the orrery.
- (do) Look at the front page on the phone, with the Home Screen clip's
  tab closed first.
- (decide) Close L-447, or change the words first.

Session record written October 2026 with Anthropic's Claude Opus 5.5.
