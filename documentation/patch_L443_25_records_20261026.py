r"""patch_L443_25_records_20261026.py -- the records of the comets' runs and phone look, Oct 26,
evening (L-443): the gold comet, the class words, a comet's planets "so
far"; L-493 (a drawer search box) and L-494 (the i button's pointer)
opened; L-491 left with its one Tony-action.

Built on orrery 140db0ae0ff05badc17b85fc7c214d36505ace32 at
https://github.com/tonylquintanilla/palomas_orrery (branch main), with
gallery dd9d0faecd4fa9a8f5a433165681fdccf35a1748 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.

WHAT IT EDITS

    LEDGER_CONSOLIDATED.md: L-443's afternoon and evening, and its Gap;
        L-493 and L-494 new; L-491's Gap; the header stamp. It records
        that interactive-exhibit 1.26's "no companions" for a comet is
        wrong after the website's patch_L443_24, for the next session's
        first skill work.
    documentation/WHERE_WE_ARE.md: the header, the box, the road, the
        signals, the design-talk list, the run record's name.

    No code, no skill, no protocol change. No new file.

HOW TO RUN

    Save it in the orrery folder (palomas_orrery_for_github), open it in
    VS Code and press Run. It prints an "ok" line per file, then "patch
    applied". A second run refuses. Then orrery_maintenance_run.py (its
    ledger index step lists the two new items), move this file into
    documentation\, commit and push. Undo before a commit is Discard
    Changes in GitHub Desktop.

Written October 26, 2026 with Anthropic's Claude Opus 5.5.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DONE = "patch applied: the records of the comets' runs, Oct 26 (%d files edited, %d new)"
EDITS = [('LEDGER_CONSOLIDATED.md', [('1.26, horizons-orbital-mechanics 1.12, gallery-cache-builder 1.13,\nprotocol v3.114), built on 5398439 and gallery 9223cd1.\nReview and RICE update Tony 6-21-2026\n', '1.26, horizons-orbital-mechanics 1.12, gallery-cache-builder 1.13,\nprotocol v3.114), built on 5398439 and gallery 9223cd1.\nModule updated: October 26, 2026, evening, with Anthropic\'s Claude Opus\n5.5 (Tony\'s runs and phone look of the comets recorded on L-443, with\nthe gold comet, the class words, and a comet\'s planets "so far"; L-493,\na search box for the drawer, and L-494, the pointer to the i button,\nnew; L-491 left with its one Tony-action), built on 140db0a and gallery\ndd9d0fa.\nReview and RICE update Tony 6-21-2026\n'), ('#### [L-492] The orrery\'s stale "manual scale" and "MB per frame" sentences come out of its hovers, as a class (orrery, the words a visitor reads)\n', '#### [L-494] A pointer to the i button, so a visitor knows where more information is (gallery, the rooms\' chrome)\n<!-- L:494 status:OPEN upd:2026-10-26 section:A flag: rice: -->\n- **Tony, 2026-10-26,** at his phone look of the comets: "we should add\n  back the pointer to the i button for the visitor to know where to\n  look for more info either in the hover text box or maybe better in\n  the top banner next to the i button, like: "More information: (i)""\n  (`documentation/WHERE_WE_ARE_10-26-26_1451_run_record.md`).\n- "Add back": the Sun and Earth rooms\' hovers carry one pointer line to\n  the i panel (L-231); the Solar System room\'s text boxes do not.\n**Gap:** a design talk: where the pointer goes (the top banner beside\nthe i button, Tony\'s preference, or the text box), its words, and\nwhether every room gets it; words to Tony first.\n**Ref:** gallery `interactive.html` (the top bar, the i button, the\ntext boxes); L-231; L-443.\n\n#### [L-493] A search box to find a row in the Solar System room\'s drawer (gallery, the drawer)\n<!-- L:493 status:OPEN upd:2026-10-26 section:A flag: rice: -->\n- **Tony, 2026-10-26,** at his phone look of the comets: "as we create\n  more objects in the website, could we add a search window to find the\n  right row?" The drawer lists 94 bodies in 15 groups since slice 2.\n**Gap:** a design talk: where the box sits, what it matches (the label,\nJPL\'s name, the designation), and what a match does (open its group,\nscroll to the row); then a build with its own drawer check.\n**Ref:** gallery `interactive.html` (the drawer),\n`gallery/solar_system_drawer.js`; L-443; L-477.\n\n#### [L-492] The orrery\'s stale "manual scale" and "MB per frame" sentences come out of its hovers, as a class (orrery, the words a visitor reads)\n'), ("**Gap:** Tony's run of patch_L443_20 and the orrery maintenance run;\nthen this closes. Tony-action (do), not blocking: the gallery cards\nthat carry a comet hover were exported with the old sizes and change\nonly when re-exported through Gallery Studio.", "- **Tony's runs, 2026-10-26:** patch_L443_20 and the maintenance run,\n  pushed at 140db0a. The scanner at that run: 0 Tier-1 on the gate path;\n  the nine rows score 15, cited; `COMET_NUCLEUS_SIZES` is named only in\n  the exceptions entry's history.\n**Gap (replaces the one below, 2026-10-26, evening):** Tony-action (do),\nnot blocking: re-export through Gallery Studio the gallery cards that\ncarry a comet hover, which were exported with the old sizes; then this\ncloses.\n**Gap (superseded above, 2026-10-26, evening):** Tony's run of patch_L443_20 and the orrery maintenance run;\nthen this closes. Tony-action (do), not blocking: the gallery cards\nthat carry a comet hover were exported with the old sizes and change\nonly when re-exported through Gallery Studio."), ("  - **Not done here, by name:** the comets' companions (none; a\n    comet's own room is L-483); the ten gallery cards' sizes (L-491).\n**Gap (replaces the one below, 2026-10-26):** Tony's runs, in order:", '  - **Not done here, by name:** the comets\' companions (none; a\n    comet\'s own room is L-483); the ten gallery cards\' sizes (L-491).\n    Corrected the same evening: the comets\' companions were built, by\n    Tony\'s ruling below.\n- **The same afternoon, before Tony\'s runs, two more website patches:**\n  - patch_L443_22: ATLAS (C/2024 G3), the one white comet, goldenrod.\n    Tony: "change all white comets to gold for contrast." The orrery\n    keeps its white.\n  - patch_L443_23: each drawer group\'s JPL or IAU class name explained\n    in plain words, the first bullet in the text box and the i panel of\n    every body in the group, from a served "about" on the group\'s row;\n    and a comet\'s perihelion explained in its span sentence. Tony\'s\n    "Yes" to drafting them, after Claude Fable 5.1\'s\n    `COORD_jpl_words_ruling_20261026.md`, and "Approved" to\n    `documentation/WORDS_L443_glosses_20261026.md`, whose sources are\n    JPL\'s Small-Body Database orbit classes, the IAU\'s announcement\n    ann17045 and the Horizons manual.\n  - Tony asked whether "aphelion" in his ruling was autocorrect\'s: it is\n    JPL\'s own word (the Horizons manual: "Aphelion distance (au)").\n- **Tony\'s runs, 2026-10-26, afternoon**\n  (`documentation/WHERE_WE_ARE_10-26-26_1451_run_record.md`). The orrery\n  pushed at 140db0a: the path plan asked JPL for the fourteen and made a\n  plan for each, one perihelion event apiece, the spacecraft plans\n  unchanged; the Horizons check confirmed the fourteen, 89 of 89\n  entries in all. The website pushed at dd9d0fa: the Daily Run\'s pull\n  matched the push and the build served all fourteen paths, each 2.5 to\n  4.5 KB of positions (West\'s plan runs from 1975, a year before its\n  perihelion); the swap took two tries, absorbed. One check was red, the\n  builder suite\'s: its span check had typed the stand-in plan\'s dates and\n  failed on the real ones, with the builder right; fixed in\n  patch_L443_24.\n- **His phone look:** the groups in their places, "yes"; ATLAS gold,\n  "yes"; Go To on 3I/ATLAS fits its whole path, "yes". C/2025 K1\'s\n  space: he had not seen the underscore the orrery keys it by, which is\n  the change working. And: "i thought we were adding the farthest\n  planetary orbit for perspective? that would be saturn now." Asked\n  whether a comet\'s farthest planet counts the path so far or the whole\n  drawn path, the dashed year included as a spacecraft\'s does: "so far".\n  So a comet on an open path ticks, as a spacecraft does, the farthest\n  planet whose perihelion its served path has passed up to the minute\n  shown: West, McNaught, \'Oumuamua and 2I/Borisov tick Pluto; 3I/ATLAS\n  Saturn (its whole path would reach Uranus); the rest Jupiter. Built in\n  gallery patch_L443_24, walked on the real served cache (142 checks);\n  the website\'s maintenance run in the sandbox, 35 of 35 gating checks,\n  its pulls aside (no orrery folder there).\n  - Two more asks, opened as items for a design talk: L-493 (a search\n    box for the drawer) and L-494 (the pointer to the i button).\n- **For the skills\' next versions, carried here:** interactive-exhibit\n  1.26 says a comet on an open path has no companions, which patch 24\n  makes wrong; its next version says a comet ticks the farthest planet\n  its path has reached so far, and that a group row\'s about explains\n  its class first in each member\'s text box and panel. This session\n  already bumped interactive-exhibit once (One Session, One Bump), so the\n  correction is the next session\'s first skill work, before any other\n  work that fires the skill. provenance-discipline\'s What a Visitor\n  Reads takes the JPL-words rule, as above.\n**Gap (replaces the one below, 2026-10-26, evening):** Tony\'s run of\ngallery patch_L443_24 and the website\'s maintenance run, push; his phone\nlook: tick West and see Pluto come with it; Go To on 3I/ATLAS and see\nSaturn. Then slice 2 closes. Next session first: interactive-exhibit\n1.27, as above.\n**Gap (superseded above, 2026-10-26, evening):** Tony\'s runs, in order:')]), ('documentation/WHERE_WE_ARE.md', [('Last updated: October 26, 2026, afternoon: the comets, built to run.\n- Written at orrery 5398439 and gallery 9223cd1; patches L485_1, L443_20, L443_21.\n', 'Last updated: October 26, 2026, evening: the comets are live.\n- Written at orrery 140db0a and gallery dd9d0fa; patch L443_24 to run.\n'), ("> - The fourteen comets are built: a year before perihelion to a year\n>   after today, solid then dashed (L-443 (the objects)).\n> - One JPL class to a drawer row; JPL's words kept and explained.\n>   interactive-exhibit 1.26; protocol v3.114.\n> - Nucleus sizes sourced: nine kept, six removed (L-491 (the nucleus\n>   sizes)). New: L-492 (the stale scale sentences).\n", "> - The fourteen comets are live, ATLAS gold, each group's name\n>   explained (L-443 (the objects)). protocol v3.114.\n> - A comet ticks the farthest planet it has reached so far, your\n>   ruling; built, to run (patch L443_24).\n> - New: L-493 (a drawer search box), L-494 (the i button's pointer).\n"), ('> **Do next:** *your runs, in the order in\n> `HANDOFF_L443_slice2_buildB_comets_20261026.md`; then slice 2 closes.*\n', '> **Do next:** *patch L443_24 (website), push, the phone look; then\n> slice 2 closes.*\n'), ('> - *(do) patch_L485_1, patch_L443_20 and the orrery maintenance run,\n>   push; patch_L443_21 and the Daily Run, push; the phone look.*\n', "> - *(do) patch_L443_24 and the website's maintenance run, push. On\n>   the phone: tick West, Pluto comes too; Go To 3I/ATLAS, Saturn.*\n"), ('               the open-path comets built Oct 26, to run.*\n               << moved this session\n', '               the open-path comets live Oct 26.*\n               << moved this session\n'), ('- Last cache build: 20261026T143207Z, ok, first try (gallery 9223cd1).\n- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md at orrery\n  5398439, generated Oct 26).\n  Whole tree: 276: orrery 112, Earth System 149, stars 13, utilities 2.\n', '- Last cache build: 20261026T200851Z, ok, one retry (gallery dd9d0fa).\n- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md at orrery\n  140db0a). Whole tree: 277: orrery 112, Earth System 149, stars 13,\n  utilities 2, and 1 from a patch then in the root.\n'), ('- Compositions (L-489 (compositions)): the noun, "view" or "scene";\n', '- L-493 (a drawer search box) and L-494 (the i button\'s pointer).\n- Compositions (L-489 (compositions)): the noun, "view" or "scene";\n'), ('- Your run record: `WHERE_WE_ARE_10-24-26_1927_run_record.md`.\n', '- Your run record: `WHERE_WE_ARE_10-26-26_1451_run_record.md`.\n')])]
NEW_FILES = []
SENTINELS = {'LEDGER_CONSOLIDATED.md': '#### [L-494] A pointer to the i button', 'documentation/WHERE_WE_ARE.md': 'patch L443_24 to run.'}
POST_CALLS = []


def fail(msg):
    print(msg)
    print("NOTHING was written. Undo is not needed.")
    sys.exit(1)


def main():
    same_new = set()
    for rel, content in NEW_FILES:
        full = os.path.join(HERE, *rel.split("/"))
        if os.path.exists(full):
            have = open(full, "rb").read().replace(b"\r\n", b"\n")
            if have == content.encode("utf-8"):
                same_new.add(rel)
                continue
            fail("ERROR: %s already exists and differs from what this patch "
                 "writes. Most likely a copy of the same document saved from "
                 "a download or an attachment: delete it and run this patch "
                 "again." % rel)
    staged = []
    for rel, edits in EDITS:
        path = os.path.join(HERE, *rel.split("/"))
        if not os.path.isfile(path):
            fail("ERROR: not found: %s -- is this file in the right folder?"
                 % path)
        raw = open(path, "rb").read()
        crlf = b"\r\n" in raw
        text = raw.replace(b"\r\n", b"\n").decode("utf-8")
        if SENTINELS.get(rel) and SENTINELS[rel] in text:
            fail("ERROR: %s already carries this patch's change; this "
                 "patch has run." % rel)
        for k, (old, new) in enumerate(edits):
            n = text.count(old)
            if n != 1:
                if new and text.count(new) == 1 and old not in text:
                    fail("ERROR: %s already carries edit %d of %d; this "
                         "patch has run." % (rel, k + 1, len(edits)))
                fail("ANCHOR FAIL in %s, edit %d of %d: expected 1 match, "
                     "found %d" % (rel, k + 1, len(edits), n))
            text = text.replace(old, new)
        staged.append((rel, path, text, crlf, len(edits)))
    for rel, path, text, crlf, n in staged:
        open(path, "wb").write(text.encode("utf-8"))
        print("ok  %s (%d edits)" % (rel, n))
        if crlf:
            print("note: %s was CRLF in the working copy; written LF" % rel)
        bad = sum(1 for c in text if ord(c) > 127)
        if bad:
            print("note: %s holds %d non-ASCII character(s) this patch did "
                  "not add" % (rel, bad))
    for rel, content in NEW_FILES:
        full = os.path.join(HERE, *rel.split("/"))
        if rel in same_new:
            print("ok  %s: already there, identical" % rel)
            continue
        d = os.path.dirname(full)
        if d and not os.path.isdir(d):
            os.makedirs(d)
        open(full, "wb").write(content.encode("utf-8"))
        print("ok  %s: new" % rel)
    for name in POST_CALLS:
        for line in globals()[name](HERE):
            print(line)
    print(DONE % (len(staged), len(NEW_FILES)))


if __name__ == "__main__":
    main()
