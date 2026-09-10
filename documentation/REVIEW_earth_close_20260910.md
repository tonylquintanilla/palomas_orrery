# Review -- where the Earth exhibit stands, and what is left

Built on orrery `c427fb06da65af49ed0546fea17efb354aff6f2c`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `de191147b7cb4eebbc6f92a8028db0a041a4ab98`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-10
Type: REVIEW (zero code). Companion to
`documentation/HANDOFF_earth_step3_close_20260909.md` (orrery).
Protocol v3.55. Handles: L-291, L-303, L-168, L-292, L-305, L-310.
Not a relay document; no second anchor line.

---

## In one paragraph

The Earth exhibit is built and passed Tony's Mode 5. What is left is
the card that puts it in the gallery, and a card for it already exists
in a shape that hides it from the desktop lobby. Fixing that is a
GUI-only job for Tony. After his eyes on the lobby, one close patch
closes L-291 and L-303 and tidies five small record gaps named below.
**Tony**: The reason for that is that when i made the card i did not see the button visible in the studio for a new interactive card. so i made one using an existing card i copied to the moon section and transferred to Earth. i then selected the P button for the mode. so it shows up in mobile but not on desktop. checking the studio dashboard again. the studio refuses to create a duplicate card. Deleting the original in Editor first and pushing. minor point: i had to relaunch the Editor to see the new card added to Storage. Maybe a refresh button in Editor would be useful. Completed the card in Editor and pushed. 

## Gates (checked this session)

- Both repos moved past the handoff's anchors, and every move is
  accounted for:
  - orrery `bd738d8` "L291 handoff": `patch_L291_14` ran,
    `ledger_index.py` ran, the handoff was saved. `c427fb0` moved the
    spent patch into `documentation/`.
  - gallery `de19114` "nightly run 9-10-26": 13 objects, no guard
    warnings, structural validation pass.
- Loaded skills match the v3.55 manifest: ledger-and-session-records
  1.10, interactive-exhibit 1.0, gallery-assembler 1.3,
  provenance-discipline 2.11. PROJECT_INSTRUCTIONS.md at HEAD is v3.55.
- The uploaded master plan is byte-identical to orrery HEAD (md5
  `eeaa4241`).
- The handoff was saved to the ORRERY `documentation/`, while its
  rollup said the gallery. The orrery is right: both earlier step-3
  handoffs live there. Not a gap.

## Verified done

- L-291 steps 3-6. `gallery/earth_geometry.js` is at HEAD and the
  page's EXHIBITS table has `sun` and `earth` rows. Mode 5 passed
  2026-09-09 ("looks right").
- L-168 is DONE, in the web track's closed table (W.Done), which the
  ledger counts as closed.

---

## Gap 1 -- the Earth card exists, and the desktop lobby hides it

**What is there.** Card
`solar_system_20260907_earth_shells_moon_mobile__moon`, title "Earth
and Moon Interactive", room `solar_system/earth`, featured, live link
`interactive.html?exhibit=earth`. Added at gallery `97ed2012`
(2026-09-09 12:54), before the three Mode 5 rounds.

**How it was made.** The `__moon` id is the pattern the gallery
editor's "Copy Card to Room" produces. It is a copy of the static
portrait card `solar_system_20260907_earth_shells_moon_mobile` with
the live link added. The copy kept that card's `sibling` tag (the tag
that pairs a landscape card with its portrait card), its portrait
file and its size. L-303 recorded exactly this editor behaviour as not
yet guarded.

**What it does.** The lobby's Featured rule drops a 9:16 card when its
sibling is also featured and shown (index.html, lines 2349-2352). The
copy's sibling is the static landscape card, which is featured.
Replayed against the metadata at HEAD -- this is the viewer's code run
on the live data, not a render, so Tony's eyes are still the check:

| State | Desktop Featured | Phone Featured |
|---|---|---|
| Before the copy | 7, no Earth interactive card | 7, no Earth interactive card |
| Now | 7, **Earth interactive card missing** | 8, static "Earth and Moon" and "Earth and Moon Interactive" both |
| After the fix below | 8, Earth interactive card present | 8, Earth interactive card present |

After the fix, each screen shows the interactive card beside ONE static
"Earth and Moon" card (the landscape on desktop, the portrait on the
phone). Whether that static pair stays featured is Tony's call.

**Why the handoff missed it.** The session that wrote it never read
the metadata, so it still lists step 7 as not started.

**The fix, in order -- the order matters.** Studio refuses to make a
card for a scene another card already opens, and the editor has no
field for the sibling tag, so the copy cannot be repaired in place.

1. Open the gallery editor. Select the `__moon` card, Delete, save.
   **Close the editor.** Studio writes the same metadata file, and an
   editor left open could save its old copy over Studio's new card.
2. Open Studio. New Interactive Card. Pick
   `interactive.html?exhibit=earth` -- checked against HEAD, the picker
   offers three scenes: the default explorer, earth, and sun. Give it
   a title and placard (the copy had "Earth and Moon Interactive" and
   "Earth and Moon"). Create. It lands in Storage, not featured.
3. Reopen the editor. Move the new card to `solar_system/earth`, tick
   Featured, save.
4. In the same editor visit, retype the two portrait titles (Gap 6).
5. GitHub Desktop: commit, push, report the SHA.

---

## Gap 2 -- the rotation period has no ledger home

L-291's Gap line and the close handoff both send "serve the rotation
period" to L-292. L-292 is "Earth shells the orrery does not draw"
(the geocorona shell, MEO, the Roche limit) and never mentions it. The
only record is one sentence in L-291's body, which moves to the closed
section when L-291 closes. Fix in the close patch: write it into L-292
as a line, or give it its own handle, and correct the pointer.

## Gap 3 -- follow-on work riding inside items that close

Two "not done, recorded" lines sit in items that are closed or about
to close, where nobody will look for them:

- L-168 (closed): the Python-side `as_of_today` test for a
  planetocentric body. L-168 carries the four numbers it would pin.
- L-303 (closes on Tony's eyes): the editor's Copy carries the sibling
  tag, and the editor can still put two files on one card. Gap 1 is
  this defect firing once already.

This is method, not a ruling for Tony. Proposed rule for
ledger-and-session-records: before an item closes, each of its "not
done" lines gets a home in an open item, or is struck with a reason.

## Gap 4 -- interactive-exhibit 1.0 describes the old scene picker

Step 7 of the skill says the picker reads `EXHIBIT === "<key>"`
literally, "so the key must appear in that form." Since step 3 the page
has an EXHIBITS table and zero such literals; `live_scene_urls` in
`tools/json_converter.py` reads the table (and the old form too). The
skill would mislead whoever builds the next exhibit. Bump to 1.1 in
the close session, before that build, with Gap 1's editor behaviour as
a field note.

## Gap 5 -- master plan still says Earth's code is not written

The plan is v28 (2026-09-08), and its Status block says Earth has "its
CODE NOT YET WRITTEN." By the plan's own pattern -- step 2 earned v27,
the design round earned v28 -- step 3's build earns v29. Its
2026-09-08 entry also places `HANDOFF_earth_step3_20260908.md` in the
gallery repo; the file is in the orrery repo.

## Gap 6 -- L-303's two portrait titles are not retyped yet

Both portrait cards still carry their landscape card's title. The
titles they had before the September merges, from the gallery metadata
before commit `b5622a8`:

| Portrait card | Title before the merge |
|---|---|
| `artemis_ii_20260402-0411_mission_moon_center2_mobile` | Artemis II - Earth to Moon Flyby April 6, 2026 |
| `maps_disintegration_20260403_07_structures_mobile` | MAPS - Disintegration April 4, 2026 |

The MAPS title differs from its landscape only by the hyphen. The
Artemis title differs in words.

**Minor, for the same patch:** L-168's title still reads "source fix
still open."

---

## Next steps, in order

1. **Tony, at the machine, GUI only.** Gap 1's five steps, including
   the two titles. Report the gallery SHA.
2. **Tony's eyes, desktop and phone.** The lobby's Featured strip shows
   "Earth and Moon Interactive" on both, and the card opens the Earth
   room. L-303's own check on the phone: one card per figure, the
   portrait file; on the desktop, paired cards side by side tagged 16:9
   and 9:16. These close L-291 and L-303.
3. **Claude writes, Tony runs: one close patch (orrery).** L-291 and
   L-303 to DONE on Tony's word; Gaps 2, 3 and 5 and the L-168 title;
   interactive-exhibit 1.1 (Gap 4) and the ledger-skill rule (Gap 3),
   one version per skill. The session after that confirms its loaded
   copies read the new versions before exhibit or ledger work.
4. **Then the next track -- Tony's choice.** Candidates already on the
   ledger:
   - L-310, camera step buttons on the nav cluster. Design round, zero
     code.
   - L-292, the rotation period and the orrery's geocorona shell. A
     small orrery patch.
   - L-305, the magnetosphere on Jelinek et al. 2012, both repos. Its
     own design session first.
   - The next exhibit in the plan's sequence, Artifact 2 (Jupiter and
     Saturn). Step 3's belt fix already carries to Jupiter.
   - L-282 and L-286, the lobby and room navigation.

## Fable

Steps 1-3 need no Fable. L-305's source check suits Gemini (fact
verification). The one ledger item tagged as a Fable candidate is
L-244, the conversion-factor sweep, and it can wait for the reset.

Written September 2026 with Anthropic's Claude Opus 5.
