<!-- Doc-Kind: hand | Session record: L-371's distance cards built, the Sun slice ordered. -->
# Handoff: the Sun's distance cards (L-371), and the Sun slice ordered

Built on orrery 17ef66607cbe63ac5ed7bdbff15397fbe546ae42 at
https://github.com/tonylquintanilla/palomas_orrery; pushed through
e38b86adb7d1b32696b759b3c8222f3742aa2bd4. Gallery
52659e04 at https://github.com/tonylquintanilla/tonyquintanilla.github.io;
pushed through ba68819937bae6089d104c9a370a0b84c8a87925 (the lobby
card's separate session also pushed in between, at d4b408e6).
The close patches below land after these, on orrery
d7f2a59440b49461a742a301777a67dc9bf49097 and gallery
ac81e7ce6257cfd6811df7d031f94ac3109d480c, where the lobby-card session's
records and license patches had landed first.

- Type: BUILD.
- Supersedes: `documentation/HANDOFF_L406_L407_L371_session_20261003.md`
  as the latest record. That file also holds this session's run records,
  which Tony appended to it.
- Session date: 2026-10-04. (Rows and credit lines were first stamped
  2026-10-03 by mistake; the close patches correct them.)

## What was done [verified @ orrery e38b86ad, gallery ba688199]

1. **patch_L371_1 (orrery).** The Sun's distance rows, each with its
   source opened this session, its figure count and its read line:
   termination shock 94.01 AU (Stone et al. 2005), heliopause 121 AU
   (Gurnett et al. 2013, p. 1489), the Oort cloud's two edges as range
   rows (NASA's facts page) drawn at 2,000 and 100,000 AU, the inner
   cloud's 20,000 AU (Portegies Zwart et al. 2021, sec. 2.2), the Sun's
   Hill radius 0.65 pc (the same paper), the helmet cusp's 2-4 as two
   rows, the Alfven surface, corona and Roche limit with units and
   counts. The unsourced 100,000-200,000 AU row removed; the outer
   corona's unfound citation removed. A pc token, KM_PER_PARSEC,
   `constants_rows.row_text()`, every orrery hover line that states
   these distances printed from its row, three relation tests, and
   exact_rows_report.py made to see `row_text()`.
2. **patch_L371_2 (orrery).** ROCHE_LIMIT_DRAWN_RADII, Tony's option B.
3. **patch_L371_3 (gallery).** The Sun's links, Tony's notes with their
   numbers from served range rows, `drawn_radius`, a far shell's
   "Radius: <n> AU", served counts on the Oort shapes and the streamer
   band, the Sun shells check, a re-recorded hover fixture.
4. Runs: orrery 20 of 20; gallery 23 of 23 after `daily_run.py`. Tony
   approved both wording files. On the phone: "Beautiful", and the
   Alfven surface at 0.092 AU inside the outer corona at 0.23 AU.

## Tony's rulings

- The Roche limit is drawn at 3.45 on both sites, described as "about
  3": at 3 it would sit on the inner corona, and which is further out
  is not known. An interim until fuzzy boundaries (L-410).
- The leading-1 shortcut is not adopted. The uncertainty test of
  2026-09-28 stands, so 100,000 AU prints as 10,000,000,000,000 km.
  Tony: "I don't want to violate my own rule!"
- Fuzzy boundaries are their own item, the outer corona first and
  designed with the dust cloud (L-410, L-131). The dust cloud joins the
  Sun's slice.
- The Sun's slice is the ordered list on L-412. The scattered disk
  (L-136) goes to the Solar System room.

## Discrepancies surfaced

- The orrery patch said the scanner would report 296 serious findings;
  Tony's machine reported 297. Tony's tree was already at 297, and the
  one new file flagged was the patch script itself in the root folder.
  Carried on L-371 as method for the next skill version.
- L-385 was offered as "one line" for this close and is not: the axis
  length and the shells switched on both set the width. Recorded on
  L-385; the Sun slice's next item.
- EXACT_ROWS_PRINTED.md lists 11 gallery pointers to exact Sun rows as
  not followed. The site prints them by the served count, but the check
  cannot yet confirm it. L-371's Gap.
- The previous handoff cited Figs. 3 and 4 for the 0.65 pc; it is
  Figs. 2 and 3. Duncan, Quinn and Tremaine's abstract does not print
  20,000 AU, so the row cites Portegies Zwart sec. 2.2 instead.

## Checked against the other session before closing

- The lobby-card session had taken L-409 (the licenses), so this
  session's new items are L-410, L-411 and L-412.
- It had rewritten Where We Are; this close merges both sessions into
  the page rather than replacing its words.
- Its drawer-fix patch, patch_L363_14, ran after its records patch and
  was not on the ledger; this close adds that note to L-363 from Tony's
  run record.
- No file this close edits had been touched by the other session
  besides those two.

## The close patches

- `patch_L371_4_session_close_orrery_20261004.py`: the ledger (L-371,
  L-385, L-386, L-228, L-241, L-131, L-136, L-128 and L-363 updated; L-209,
  L-224, L-227, L-229 closed; L-410, L-411, L-412 opened), this
  handoff, Where We Are, and the date corrections in ten orrery files.
- `patch_L371_5_dates_gallery_20261004.py`: the date corrections in
  three gallery files' comments. No hover or served value changes.

## Tony-actions, rolled up

- (do) Run the orrery close patch, then orrery_maintenance_run.py
  (every gating check passes), move the script into documentation/,
  commit and push.
- (do) Run the gallery close patch, then gallery_maintenance_run.py
  (23 of 23; no cache rebuild is needed, since no served value
  changes), move the script into documentation/, commit and push.

## Skills

- No skill changed this session, so there is no load to confirm next
  session.
- Carried to the next versions (on L-371): provenance-discipline's
  range-rule example names the removed range row; and a patch's
  "what the run should say" should predict the scanner's change, not
  its total.

## Next session

First, Earth's list (the section below). Then start at L-412 item 3,
the orrery's opening view of the Sun (L-385):
read the Sun's autoscale with its default shells and propose to Tony
before building. Then item 4, L-228: Claude reads Cranmer et al. (2007)
itself. Beside the list, L-371's own Gap.

## Next session also: Earth's list, for a ledger update

On 2026-10-04 Tony asked for the same sweep for Earth that L-412 is for
the Sun, to be recorded on the ledger next session. Do it
early: first read L-305 and L-292 against the code, so the list starts
accurate, then write it as one ledger item in the shape of L-412.

The sweep, as given to Tony:

- **Possibly finished but still open; read first.**
  - L-305, the magnetosphere on a sourced model: the Shue and Jelinek
    shapes are in both instruments, but its open list is long.
  - L-292, the shells the orrery does not draw: an exosphere shell
    naming the geocorona now exists; the other two may not.
  - L-383, the magnetosphere tooltip copy: if that SHELL_CONFIGS text
    is never shown (orrery-coding-conventions calls the tooltip field
    dead data), the copy goes.
- **Small, the Earth room reaches them.**
  - L-369, Earth's obliquity typed in four places outside the store.
  - L-350, the magnetotail's observed extent served and shown nowhere:
    Tony decides print it or stop serving it.
  - L-349 then L-383, the inner belt's "where the measured particle
    flux peaks": Tony's wording ruling, then the copy.
  - L-389, the atmosphere shells from the equatorial radius against the
    crust at the mean radius: Tony noted it "depends on the source".
  - L-379, the recorded Earth scene payload, aging: recapture it.
  - L-382, Tony's look at the magnetosphere's cost per animation frame.
- **Design talks first.**
  - L-231 then L-330, the belts tilted with the magnetic field, then
    their shape.
  - L-375, the eccentric dipole offset (depends on an unmodelled
    rotation phase).
  - L-356, IGRF-14 as a re-sourcing of the coefficient rows.
  - L-321, the orrery's 36 Earth hover strings into the provenance
    braid.
  - L-297 and L-294, the Lagrange points and Earth's heliocentric view,
    behind Tony's ruling on the Explorer room.
  - L-314 after L-305, live solar wind for the magnetosphere.
  - L-374 and L-061, precession over time and the seasonal roll:
    recorded ideas.
- **Not the Earth room:** L-001, L-060 (the Earth System climate
  track), L-157, L-173, L-186, L-252 (the cross-check programme), L-177
  (Mercury), L-347, L-348, L-360, L-367 (general checks).

Tony orders the list when it is put to him; the order above is the
sweep's, not his.

Session written October 2026 with Anthropic's Claude Opus 5.5.
