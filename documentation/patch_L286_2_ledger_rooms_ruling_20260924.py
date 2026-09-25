"""patch_L286_2_ledger_rooms_ruling_20260924.py -- L-286 and L-283, the record.

RUN COMMAND

    Save this file in the ROOT of the palomas_orrery repository, beside
    LEDGER_CONSOLIDATED.md. Open it in VS Code and click Run.

    Then run the orrery maintenance run, which regenerates the ledger's
    index tables. Then move this script into documentation/, commit and
    push.

WHAT IT CHANGES -- one file, all-or-nothing, text only

    LEDGER_CONSOLIDATED.md
        L-286: a dated note for 2026-09-24 -- the Moon's cards folding into
        Earth on the served page and why, how the item dropped out of the
        master plan's order, Tony's ruling to build it now, his ruling on
        the Desktop and Mobile tabs, the approved mockup and its one
        departure from the 2026-09-04 wording, and the build order. A new
        Gap; the old one is marked superseded. The line saying the phone
        shows every card is marked superseded by the 2026-09-22 tab ruling.
        L-283: a dated note -- the dusk-blue wall, the art more prominent,
        and the original art with its Gemini mark.
        Only detail blocks are edited; the index zone is left to
        ledger_index.py, and the fingerprint does not include it.

    The master plan is NOT edited. The Earth work, in another
    conversation, restamps it with Stage D; L-286's Gap asks that restamp
    to put step 2 back into the plan's "Next" paragraph.

IF IT SAYS "BASE MOVED": the ledger changed after this was built, most
likely from the Earth conversation's patch. Nothing is written. Bring the
output back and the patch is rebuilt on the new ledger.

Built on orrery fb8d927e1581f6ad2fe49aa04a8d30d50e7f8d71
at https://github.com/tonylquintanilla/palomas_orrery
with the gallery read at 9c61fb21 (tonyquintanilla.github.io).

Written September 24, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os
import sys

NAME = "LEDGER_CONSOLIDATED.md"
BASE_FP = 'b109008357d6005d9774597a325350fb'
WANT_FP = '044339bcffcbf89ef9c542c2ca5fa4b8'
HUNKS = [('<!-- L:286 status:OPEN upd:2026-09-08 ', '<!-- L:286 status:OPEN upd:2026-09-24 '), ('  note): every card shows on the phone, 105 not 56. Tested headless:\n', "  note): every card shows on the phone, 105 not 56. [SUPERSEDED\n  2026-09-22 by Tony's tab ruling in the gallery card pass: the Desktop\n  tab lists the 16:9 cards and the Mobile tab the 9:16 cards, and the\n  phone drops a 16:9 card whose 9:16 twin is served. See the\n  2026-09-24 note below for where the tabs now live.] Tested headless:\n"), ('**Gap:** the room-path reader in `index.html` (filter a grid to a room);\n', '- **2026-09-24 -- FOUND AGAIN, AND TONY RULED TO BUILD IT NOW.** Found\n  during the gallery card pass (orrery\n  `documentation/RUN_RECORD_gallery_card_pass_20260922.md`, section\n  3i), at gallery `9c61fb21`. Tony saw the editor show a Moon room under\n  Earth while the served page listed the Moon\'s six cards directly under\n  Earth. The cause is this item\'s unbuilt part: `normalizeSchemaV2()` in\n  `index.html` keeps only the first two parts of a card\'s room path, so\n  `solar_system/earth/moon` reads as `solar_system/earth`, and the menu\n  draws only a door and one level of room. The Moon room was added on\n  2026-09-04 and its cards moved in on 2026-09-05, so the page has folded\n  them into Earth since then. The editor was built ahead of the page.\n- **Why it was not seen.** The master plan\'s order of 2026-09-03 puts\n  this item third in step 2. The notes of 2026-09-05 and 2026-09-06 say\n  step 2 is two of three items done. Step 3, Earth, went ahead while\n  this waited, every later "what this does to the order" paragraph\n  discusses steps 3 to 5 only, and the plan\'s newest "Next" paragraph\n  (2026-09-17 to 22) goes from Stage D to Jupiter and Saturn. No update\n  ruled it dropped; it stopped being mentioned. Tony, 2026-09-24: "this\n  is the gallery sweep and we found L286 again, so i would say we should\n  build it so it is not left behind."\n- **Tony\'s ruling on the tabs, 2026-09-24.** Removing the side menu\n  would remove the Desktop and Mobile tabs, which sit at the top of its\n  panel and are hidden on phones. Tony: "why can\'t the desktop room keep\n  both views? both have positives and negatives. the phone is limited\n  the desktop is not." Asked to confirm the tabs in the header on every\n  desktop screen, lobby and rooms alike, and none on the phone: "yes".\n  This replaces decision 10 of the 2026-09-04 design session, which had\n  the tabs going away, and answers the card pass\'s finding that the\n  front page does not show the tab split.\n- **The mockup, approved 2026-09-24.** A Design canvas, private to Tony:\n  https://claude.ai/artifact/DLMy8Vu3nV5dNKPU4vFE8X, seven screens drawn\n  from the real cards at gallery `9c61fb21`: on the desktop the lobby,\n  the Solar System door, the Earth room and the Moon room; on the phone\n  the Earth room, the Moon room and an open card. Tony: "Yes."\n  - Each room is its own screen: its title and counts, its own cards,\n    then the rooms inside it. Cards come first, as the tree order rule\n    already lists a room\'s own cards before its rooms.\n  - A room with no cards stays in the list, greyed, marked "under\n    construction", as the lobby does today.\n  - A special exhibit is a room row marked "special exhibit" (Orbital\n    Mechanics, under the Solar System door).\n  - The header carries the chain on the left and, on the desktop, the\n    two tabs on the right. The chain uses the config\'s short labels as\n    they are stored ("Solar: Earth: Moon"). On the phone the cards stack\n    in one column, and an open card keeps the chain with the card\'s\n    title under it.\n  - ONE DEPARTURE FROM THE 2026-09-04 WORDING, shown in the mockup and\n    approved with it. This block said the chain\'s first crumb returns a\n    visitor to the lobby; then nothing in the chain reaches the door\'s\n    own screen. In the mockup "Paloma\'s Orrery" at the far left of the\n    header goes to the lobby, and the first crumb, the door\'s short\n    name, opens the door\'s screen.\n  - The side menu is retired, as the master plan\'s note of 2026-09-05\n    already said this item would do.\n- **The look changed with it** (Tony\'s ruling of the same day, recorded\n  on L-283): a dusk-blue wall and the logo art more prominent.\n- **Build order, agreed 2026-09-24.** Three `index.html` patches, each\n  applied and looked at on Tony\'s phone before the next: (1) rooms, each\n  its own screen, four levels, the side menu retired; (2) the header,\n  the chain and the tabs; (3) the look, from L-283\'s note. Then the\n  chain in `interactive.html`, after checking that file\'s latest commit,\n  since the Earth work runs in another conversation and may be changing\n  it.\n- **Found in the files this build opens** (Cluster the Tail by Topic),\n  all in `index.html` and all from the card pass\'s section 5: the\n  browser\'s back button does nothing useful on a card, because the page\n  replaces the address instead of adding one; a phone first opened\n  sideways gets the tablet layout with the tabs; the front page does not\n  show the tab split (answered above). Rooms with their own addresses\n  are the natural place to take the first; the second moves with the\n  tabs.\n**Gap (2026-09-24):** the four pieces above, then Mode 5 on phone and\ndesktop at all four levels. The room-shape field is done (every card\ncarries `shape`); the special-exhibit placement is settled by the\nmockup. The master plan\'s next restamp puts step 2 back into its "Next"\nparagraph; it is not edited now because the Earth work, in another\nconversation, restamps the plan with Stage D.\n**Gap (2026-09-04; SUPERSEDED by the 2026-09-24 Gap above):** the room-path reader in `index.html` (filter a grid to a room);\n'), ('<!-- L:283 status:OPEN upd:2026-09-03 ', '<!-- L:283 status:OPEN upd:2026-09-24 '), ('**Gap:** a shared stylesheet carrying the palette, the accents, the\n', '- **2026-09-24 -- THE WALL IS DUSK BLUE, NOT BLACK, AND THE ART IS\n  MORE PROMINENT.** Tony, looking at the L-286 rooms mockup\n  (https://claude.ai/artifact/DLMy8Vu3nV5dNKPU4vFE8X, private to him):\n  "make the background favicon image more prominent and maybe adopt its\n  dusk sky blue tone rather than pure black." Shown a revised mockup:\n  "i like it the way you have designed it." This changes "Dark void\n  background" in The bones stay above; the fonts do not change.\n  - As drawn: a vertical gradient from #050c1a at the top through\n    #0a1829 at 45% and #132a45 at 78% to #1d3a5a at the bottom, tones\n    sampled from the logo art. The art over it at 60% opacity on the\n    lobby, 35% on the room screens, 15% behind an open card. The header\n    and cards are tinted blue to match and slightly see-through. Today\n    the page shows the art at 14%, from `favicon.ico`, which at 256\n    pixels is too small to show larger.\n  - The art is Tony\'s original, uploaded 2026-09-24 as\n    `Gemini_palomas_orrery_logo.png`, 1024 by 1024, carrying Gemini\'s\n    mark in its lower right corner. Tony: "we should keep the Gemini\n    mark not the generic ai mark." The mockup had used\n    `palomas_orrery_logo.png` from the gallery repo, cropped to drop a\n    generic "ai" mark; the build uses the original with its mark.\n  - Not ruled: whether the exhibit rooms in `interactive.html` take the\n    dusk wall too; the mockup covered `index.html` only.\n  - Built as the third of L-286\'s `index.html` patches.\n**Gap:** a shared stylesheet carrying the palette, the accents, the\n')]


def fingerprint(lf):
    a = lf.index(b"<!-- INDEX:START")
    b = lf.index(b"<!-- INDEX:END -->") + len(b"<!-- INDEX:END -->")
    return hashlib.md5(lf[:a] + lf[b:]).hexdigest()


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(root, NAME)
    if os.path.basename(root) == "documentation" or not os.path.exists(path):
        print("ERROR: run this from the orrery repository ROOT. NOTHING was "
              "written.")
        return 1
    raw = open(path, "rb").read()
    crlf = b"\r\n" in raw
    lf = raw.replace(b"\r\n", b"\n")
    actual = fingerprint(lf)
    if actual == WANT_FP:
        print("FAILURE -- NOTHING was written: %s already carries this patch "
              "(a second run)." % NAME)
        return 1
    if actual != BASE_FP:
        print("FAILURE -- NOTHING was written: %s BASE MOVED (expected %s, "
              "found %s)." % (NAME, BASE_FP[:12], actual[:12]))
        print("Bring this output back; the patch is rebuilt on the new file.")
        return 1
    text = lf.decode("utf-8")
    for index, (old, new) in enumerate(HUNKS, 1):
        if text.count(old) != 1:
            print("FAILURE -- NOTHING was written: ANCHOR FAIL on edit %d of "
                  "%d." % (index, len(HUNKS)))
            return 1
        text = text.replace(old, new)
    try:
        out = text.encode("ascii")
    except UnicodeEncodeError:
        print("FAILURE -- NOTHING was written: the result is not ASCII.")
        return 1
    if fingerprint(out) != WANT_FP:
        print("FAILURE -- NOTHING was written: the result is not the file this "
              "patch was built to produce.")
        return 1
    if crlf:
        out = out.replace(b"\n", b"\r\n")
    open(path, "wb").write(out)
    print("ok  %s  %d edit(s): L-286 note and Gap, L-286 mode line marked, "
          "L-283 note" % (NAME, len(HUNKS)))
    print("")
    print("DO THESE, IN THIS ORDER:")
    print("  1. Run the orrery maintenance run. Its 'Ledger index' generator "
          "rewrites the index tables for L-286 and L-283.")
    print("  2. Move this script into documentation/.")
    print("  3. Move the new run record into documentation/, replacing "
          "RUN_RECORD_gallery_card_pass_20260922.md there.")
    print("  4. Commit and push.")
    print("Undo before committing is Discard Changes in GitHub Desktop.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
