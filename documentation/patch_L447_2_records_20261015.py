#!/usr/bin/env python3
"""
patch_L447_2_records_20261015.py -- the records for L-447 (the front
page's words): its ledger item, its build record, and Where We Are.

Built on orrery 47d241bc32c4a21a9a183d7f58873bc75f157997 at
https://github.com/tonylquintanilla/palomas_orrery; the gallery's own
patch, patch_L447_1_front_page_words_20261015.py, is built on gallery
9f8569ee3125de27fed96c86c701e3c4d52d88e3 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\
Written October 15, 2026 with Anthropic's Claude Opus 5.5.

RUN COMMAND

    python patch_L447_2_records_20261015.py

    Save this file in the ORRERY folder above, open it in VS Code and
    click Run. It takes no arguments and asks no questions.

WHAT IT DOES, all or nothing

    New file:
      documentation/HANDOFF_L447_front_page_words_20261015.md
    Edited:
      LEDGER_CONSOLIDATED.md          L-447 opened; header stamp
      documentation/WHERE_WE_ARE.md   above the run-record marker only:
                                      the date, the box, the This session
                                      pointer

    L-447 must be free. If another session has taken it, this refuses and
    writes nothing, because the gallery patch carries the same number.
    Each file is checked only at the lines edited.

WHAT IT PRINTS

    Success: one "ok" line per edit, then "patch applied". Failure: one
    ERROR or ANCHOR FAIL line and "NOTHING was written."

Undo is Discard Changes in GitHub Desktop.
"""

import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
LEDGER = "LEDGER_CONSOLIDATED.md"
WWA = "documentation/WHERE_WE_ARE.md"
HANDOFF = "documentation/HANDOFF_L447_front_page_words_20261015.md"
MARKER = "--- Your run record below this line"
WWA_CAP = 130


class PatchError(Exception):
    pass


def read(rel):
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        raise PatchError("missing file: %s (is this the orrery folder?)" % rel)
    raw = open(path, "rb").read()
    return raw.replace(b"\r\n", b"\n").decode("utf-8"), (b"\r\n" in raw)


def rep(text, old, new, label, log, rel):
    n = text.count(old)
    if n != 1:
        raise PatchError("ANCHOR FAIL [%s %s]: expected 1 match, got %d: %r"
                         % (rel, label, n, old[:70]))
    log.append("ok  %-58s %s" % (rel, label))
    return text.replace(old, new)


ITEM = """#### [L-447] The website's front page says what the site is (gallery, lobby)
<!-- L:447 status:OPEN upd:2026-10-15 section:A flag: rice: -->
- **Asked 2026-10-15** by Tony: he showed palomasorrery.com to his
  brother, whose main comment was that from the front page he could not
  tell what the site is about. A coordination session the same day
  looked at the page on desktop and phone and agreed on why: "Paloma's
  Orrery" -- most people do not know the word "orrery", and "Paloma's"
  says whose it is, not what it is; the line under the title, "The
  solar system, the Earth and the stars, to explore." (gallery
  `gallery/gallery_config.json`, "sentence"), names subjects but not
  what kind of thing the site is; nothing says paloma is Spanish for
  dove, so a newcomer sees birds over space with no reason; "exhibits"
  and "interactive scenes" are the project's words, not a visitor's;
  and the sentence that explains the site sits behind the "i" button.
- **Designed and ruled the same day,** in the L-444 session: three
  versions of two lines, with Claude's pick, version A. Tony: "Confirmed
  as recommended, A and love in 3D" ("love" is "live"). The words:
  "Explore the solar system, the Earth and the nearby stars in 3D,
  built from real science data such as NASA JPL's Horizons." and, under
  it, "An orrery is a model of the solar system. I built this one for
  my daughter Paloma, whose name is Spanish for dove." No redesign: the
  title, the picture and the layout stay (L-428's design). "Interactive
  scenes" reads "live in 3D"; "exhibits" stays, the site speaking as a
  museum with rooms and doors. No number is in the words; each claim is
  one the site's own "i" card already makes.
- **Built 2026-10-15,** gallery
  `patch_L447_1_front_page_words_20261015.py` on 9f8569e: the sentence
  in `gallery_config.json` and a new "name_note" beside it, printed by
  `renderLobby()` in `index.html` under the sentence, smaller and in
  italics, in the lobby's near-white with its shadow; "live in 3D" on
  the doors, the subject pages and their room rows; the same sentence
  as the fallback, the no-script text and the link-preview
  descriptions (og and twitter), so a shared link says it too.
- **Verified on a throwaway copy:** headless Chromium screenshots at
  390 x 844 (phone) and 1280 x 800 (desktop), shown to Tony before he
  ran it; the Enter button still ends inside the phone's first screen;
  the gallery's maintenance run 27 of 27; the editor and the guest-book
  updater keep the new field (both load and write the whole config).
  The record is `documentation/HANDOFF_L447_front_page_words_20261015.md`.
**Gap:** Tony's look at the front page on his phone (the acceptance);
then close.
**Ref:** L-428 (the lobby's way in); L-282 (the lobby); gallery
`index.html` (`renderLobby`), `gallery/gallery_config.json`.

"""

STAMP_ANCHOR = "Review and RICE update Tony 6-21-2026\n"
STAMP = ("Module updated: October 15, 2026 with Anthropic's Claude Opus 5.5\n"
         "(L-447 opened: the website's front page says what the site is),\n"
         "built on 47d241bc.\n" + STAMP_ANCHOR)

WWA_EDITS = [
    ("header",
     """Last updated: October 15, 2026, afternoon: L-444 (the missing periods) done.
- Written at orrery 9579fcd and gallery 9f8569e.
""",
     """Last updated: October 15, 2026, evening: the front page's words.
- Written at orrery 47d241b and gallery 9f8569e.
"""),
    ("changed since you last read this",
     """> - Ruled: Earth's period from the Earth-Moon barycentre: L-445.
> - Ruled: the website's daily run pulls before it builds: L-446.
""",
     """> - Ruled: L-445 (Earth's period) and L-446 (the daily run's order).
> - Built: the front page says what the site is: L-447 (its words).
"""),
    ("needs you now",
     """> - *Run patch_L444_2_close, then the maintenance run; commit; push.*
""",
     """> - *Run the two L-447 patches; look at the front page on your phone.*
"""),
    ("details: this session",
     """- This session: `HANDOFF_L444_missing_periods_build_20261015.md`
""",
     """- This session, last: `HANDOFF_L447_front_page_words_20261015.md`
"""),
]

HANDOFF_TEXT = """<!-- Doc-Kind: hand | Build record for L-447: the website's front page says what the site is, in Tony's words. Gallery only, words. -->
# Build record: the front page's words (L-447)

Built on gallery 9f8569ee3125de27fed96c86c701e3c4d52d88e3 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io; records
on orrery 47d241bc32c4a21a9a183d7f58873bc75f157997 at
https://github.com/tonylquintanilla/palomas_orrery.
Pushed at: (Tony's commits after his run).
Tony's local folders: orrery
`C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\`;
gallery `C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\`.
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
"""


def main():
    log = []
    try:
        led, led_crlf = read(LEDGER)
        if "#### [L-447]" in led:
            raise PatchError("L-447 already exists. If another session took "
                             "it, nothing is written; ask for the patches "
                             "to be renumbered")
        if os.path.exists(os.path.join(ROOT, HANDOFF)):
            raise PatchError("%s already exists" % HANDOFF)
        anchor = "#### [L-445] Earth's orbital period"
        if led.count(anchor) != 1:
            raise PatchError("ANCHOR FAIL [%s L-445 header]" % LEDGER)
        i = led.index(anchor)
        led = led[:i] + ITEM + led[i:]
        log.append("ok  %-58s %s" % (LEDGER, "L-447 opened"))
        led = rep(led, STAMP_ANCHOR, STAMP, "header stamp", log, LEDGER)

        wwa, wwa_crlf = read(WWA)
        if wwa.count(MARKER) != 1:
            raise PatchError("ANCHOR FAIL [%s run-record marker]" % WWA)
        cut = wwa.index(MARKER)
        top, bottom = wwa[:cut], wwa[cut:]
        for label, old, new in WWA_EDITS:
            top = rep(top, old, new, label, log, WWA)
        above = top.count("\n")
        if above > WWA_CAP:
            raise PatchError("%s would stand %d lines above the marker (cap %d)"
                             % (WWA, above, WWA_CAP))
        log.append("ok  %s: %d lines above the marker (cap %d)"
                   % (WWA, above, WWA_CAP))
        wwa = top + bottom
        for rel, text in ((LEDGER, led), (WWA, wwa), (HANDOFF, HANDOFF_TEXT)):
            bad = sum(1 for ch in text if ord(ch) > 127)
            if bad:
                raise PatchError("%s: %d non-ASCII character(s)" % (rel, bad))
    except PatchError as exc:
        print("ERROR: %s" % exc)
        print("NOTHING was written.")
        sys.exit(1)

    notes = []
    for rel, text, crlf in ((LEDGER, led, led_crlf), (WWA, wwa, wwa_crlf)):
        with open(os.path.join(ROOT, rel), "wb") as handle:
            handle.write(text.encode("utf-8"))
        if crlf:
            notes.append("note: %s was CRLF in the working copy; written LF"
                         % rel)
    with open(os.path.join(ROOT, HANDOFF), "w", encoding="utf-8",
              newline="") as handle:
        handle.write(HANDOFF_TEXT)
    log.append("ok  new   %s" % HANDOFF)
    for line in log + notes:
        print(line)
    print("stamps updated: the ledger's header; Where We Are's date")
    print("")
    print("patch applied (L-447 opened; 3 files)")
    print("")
    print("NEXT:")
    print("  1. Move this script into documentation/ first, so the scanner")
    print("     does not count it; then run orrery_maintenance_run.py.")
    print("  2. Commit and push the orrery.")
    print("Undo is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
