#!/usr/bin/env python3
"""patch_L303_tab_shows_its_own_shape_20260922.py -- GALLERY repo.

Tony's ruling of 2026-09-22, from the card pass: the Desktop tab should
show the 16:9 view and the Mobile tab the 9:16 view. Until now both tabs
listed every card, so a figure with two cards appeared twice on the
desktop -- once as the landscape view and once as the portrait view whose
hover text only works in Mobile mode. Two changes, one transaction.

  1. THE TAB DECIDES WHICH CARDS IT LISTS. index.html has one function,
     inCurrentMode(), that decides list membership, and it returned true
     for everything. It now lists the cards whose file matches the tab --
     landscape for Desktop, portrait for Mobile -- plus two kinds that
     would otherwise disappear:
       - a card with no counterpart in the other shape lists in BOTH
         tabs. Without this, 46 landscape-only cards would leave the
         Mobile tab and 14 portrait-only cards the Desktop tab.
       - a live room (Solar System Explorer, Solar Structures, Earth and
         Moon) has no file at all and lists in both.
     Measured in a stand-in copy of the site, with change 2 applied:
     each tab lists 104 of the 145 cards instead of all 145. What leaves
     the Desktop tab is the 41 portrait twins, and what leaves the Mobile
     tab is their 41 landscape partners; 46 landscape-only cards, 14
     portrait-only cards and the 3 live rooms list in both. Three callers
     follow the same function -- the room lists, the lobby, and the
     exhibit count on the welcome line.

     This REPLACES L-287's rule of 2026-09-05, "every card shows in every
     mode; the mode only picks which file a card serves". That rule was
     written when one card could hold two files; since L-303 a figure's
     two shapes are two cards, which is what the two tabs are for.

     A phone is unaffected: it forces the Mobile tab, and it already
     drops a landscape card whose portrait twin is served. A deep link
     still opens the card it names, in either tab, as before.

  2. THE INNER SOLAR SYSTEM ANIMATION PAIR IS STAMPED. The rule above
     works off the "sibling" link between a figure's two cards. These two
     were converted on 2026-02-17, before the pairing existed, and their
     file names share no stem, so nothing ever linked them. Unstamped,
     both would have gone on showing in both tabs. This is the only
     unstamped pair in the metadata: every other card without a sibling
     exists in one shape only.

Built on tonyquintanilla.github.io 386a44ff4e0aa4b03624a3e1cf1f38c65081dfcd
at https://github.com/tonylquintanilla/tonyquintanilla.github.io .
(First cut on 83a72d11; see the Updated note at the bottom of this
docstring for why it moved.)

RUN IT LIKE THIS, from the GALLERY repo root (the folder that holds
index.html), by opening this file in VS Code and clicking Run:

    python patch_L303_tab_shows_its_own_shape_20260922.py

It edits two files and is all-or-nothing. Nothing under data/ changes, so
no cache rebuild is needed: the push alone puts it on the site.

What is permanent, once this script is filed away: the new inCurrentMode()
in index.html and the two "sibling" lines in gallery/gallery_metadata.json.

Module created: September 22, 2026 with Anthropic's Claude Opus 5.
Updated: September 22, 2026 with Anthropic's Claude Opus 5.5
  - The first cut refused with BASE MOVED on gallery_metadata.json. The
    edits it makes were still valid: between 83a72d11 and 386a44ff the
    only metadata changes were the Solar System Explorer's "featured"
    flag and the "last_updated" stamp, neither near either anchor. It
    refused because it fingerprinted the WHOLE metadata file, which the
    gallery editor rewrites on every save -- and this patch arrived in
    the middle of a card clean-up. (safe-file-editing, A Guard Must Not
    Fence What a Generator Rewrites.)
  - So index.html keeps its whole-file fingerprint (it is code, and the
    rule depends on all of it), while the metadata is now checked for
    what this patch actually needs: both animation cards exist, neither
    names a sibling yet, each holds only its own shape, and each anchor
    matches exactly once.
  - The tab counts in the closing instructions are now computed from
    the metadata as it stands when the script runs, instead of typed in,
    so a card edited or moved during the clean-up cannot make them stale.
  - A second run says the patch is already applied, instead of BASE
    MOVED.
"""

import hashlib
import json
import os
import sys

PROBE = "index.html"
PAGE = "index.html"
META = "gallery/gallery_metadata.json"

LAND_ID = "inner_solar_system_animation_2-4-2005_21_years_gallery_landscape_copy"
POR_ID = "inner_solar_system_animation_2-4-2005_21_years_social_copy2"


# ==========================================================================
# 1. index.html
# ==========================================================================

P_STAMP_OLD = rb"""       - Menu and Featured follow the room tree (doors, loose cards,
         rooms, in config order); no invented "Other" heading (L-286). -->
"""
P_STAMP_NEW = rb"""       - Menu and Featured follow the room tree (doors, loose cards,
         rooms, in config order); no invented "Other" heading (L-286).
     Updated: September 22, 2026 with Anthropic's Claude Opus 5
       - The tab picks the cards (Tony's ruling from the card pass):
         the Desktop tab lists the 16:9 cards and the Mobile tab the
         9:16 cards, while a card with no counterpart in the other
         shape, and a live room, list in both. inCurrentMode() is the
         one place it is decided; the room lists, the lobby and the
         exhibit count all read it. It replaces L-287's "every card
         shows in every mode". -->
"""

P_TREE_OLD = rb"""        // Every card shows in every mode (L-287, 2026-09-05); the mode only
        // picks WHICH FILE a two-slot card serves (fileForMode).
"""
P_TREE_NEW = rb"""        // Which cards a tab lists: inCurrentMode() below, rewritten on
        // 2026-09-22. It replaced L-287's "every card shows in every
        // mode; the mode only picks WHICH FILE a card serves".
"""

P_MODE_OLD = rb"""        function inCurrentMode(v) {
            return !!v;
        }
"""
P_MODE_NEW = rb"""        // Which cards this tab lists (Tony's ruling, 2026-09-22). The
        // Desktop tab lists the 16:9 cards, the Mobile tab the 9:16 ones:
        // a figure with two cards is one card per tab, and the portrait
        // card, whose hover text reaches the visitor only through the info
        // card wired in Mobile mode, stops appearing on the desktop.
        //
        // Two kinds list in BOTH tabs. A card with no counterpart in the
        // other shape: without that, 46 landscape-only cards would leave
        // the Mobile tab and 14 portrait-only cards the Desktop tab. And a
        // live room, which has no file at all -- the Explorer and the two
        // exhibit rooms serve every screen themselves.
        //
        // The counterpart is the sibling link the converter stamps, not a
        // guess from titles, and it must be SERVED: a twin in Storage is
        // not shown to anyone, so its partner keeps its place in both tabs.
        // vizLookup holds the served cards and is built before the first
        // render, and on a phone it is already missing the landscape cards
        // that phone hides, which is the same answer by a shorter route.
        //
        // Three callers: renderNavList (the room lists), renderLobby (the
        // doors and the featured strip), updateWelcomeCount.
        function inCurrentMode(v) {
            if (!v) return false;
            var files = v.files || {};
            if (!files.landscape && !files.portrait) return true;
            var want = (currentMode === 'portrait') ? 'portrait' : 'landscape';
            if (files[want]) return true;
            var twin = v.sibling && vizLookup[v.sibling];
            return !(twin && (twin.files || {})[want]);
        }
"""

P_NAV_OLD = rb"""        function renderNavList(vizs) {
            // Every card shows (L-287); the mode picks the file, not the list.
"""
P_NAV_NEW = rb"""        function renderNavList(vizs) {
            // The tab picks the cards (2026-09-22): see inCurrentMode.
"""


# ==========================================================================
# 2. gallery/gallery_metadata.json
# ==========================================================================

M_LAND_OLD = rb"""      "converted": "2026-02-17 23:25",
      "size_kb": {
        "landscape": 10082.0
      }
    },
"""
M_LAND_NEW = rb"""      "converted": "2026-02-17 23:25",
      "size_kb": {
        "landscape": 10082.0
      },
      "sibling": "inner_solar_system_animation_2-4-2005_21_years_social_copy2"
    },
"""

M_POR_OLD = rb"""      "converted": "2026-02-17 23:24",
      "size_kb": {
        "portrait": 10857.8
      }
    },
"""
M_POR_NEW = rb"""      "converted": "2026-02-17 23:24",
      "size_kb": {
        "portrait": 10857.8
      },
      "sibling": "inner_solar_system_animation_2-4-2005_21_years_gallery_landscape_copy"
    },
"""


FILES = [
    (PAGE, "77d1225e04a0c1f475ac1e790c55376c", [
        ("index.html: header Updated stamp", P_STAMP_OLD, P_STAMP_NEW),
        ("index.html: the note above treeRank points at the new rule",
         P_TREE_OLD, P_TREE_NEW),
        ("index.html: inCurrentMode() lists the tab's own shape",
         P_MODE_OLD, P_MODE_NEW),
        ("index.html: renderNavList's note matches", P_NAV_OLD, P_NAV_NEW),
    ]),
    (META, None, [
        ("metadata: the 16:9 animation card names its 9:16 twin",
         M_LAND_OLD, M_LAND_NEW),
        ("metadata: the 9:16 animation card names its 16:9 twin",
         M_POR_OLD, M_POR_NEW),
    ]),
]


def meta_precheck(content):
    """What this patch needs from the metadata, checked by meaning rather
    than by a whole-file fingerprint. Returns an error string or None."""
    try:
        doc = json.loads(content.decode("utf-8"))
    except ValueError as err:
        return "%s is not valid JSON before the edit: %s" % (META, err)
    cards = {c.get("id"): c for c in doc.get("visualizations", [])}
    for cid, shape in ((LAND_ID, "landscape"), (POR_ID, "portrait")):
        card = cards.get(cid)
        if card is None:
            return ("the %s animation card is not in the metadata:\n"
                    "         %s" % (shape, cid))
        if "sibling" in card:
            if card["sibling"] in (LAND_ID, POR_ID):
                return ("this patch has already been applied: the %s\n"
                        "         animation card already names its twin."
                        % shape)
            return ("the %s animation card already names a different\n"
                    "         sibling (%s). Tell Claude." % (shape, card["sibling"]))
        if sorted((card.get("files") or {}).keys()) != [shape]:
            return ("the %s animation card no longer holds exactly one\n"
                    "         %s file: %s. Tell Claude."
                    % (shape, shape, card.get("files")))
    return None


def tab_counts(doc):
    """The same rule inCurrentMode() applies, on the cards the page serves
    (Storage, room "other", is never served). Returns
    (served, desktop, mobile, featured_desktop, featured_mobile)."""
    served = [v for v in doc.get("visualizations", [])
              if v.get("room") and v.get("room") != "other"]
    look = dict((v.get("id"), v) for v in served)

    def listed(v, want):
        files = v.get("files") or {}
        if not files.get("landscape") and not files.get("portrait"):
            return True
        if files.get(want):
            return True
        twin = v.get("sibling") and look.get(v.get("sibling"))
        return not (twin and (twin.get("files") or {}).get(want))

    def featured(want):
        shown = [v for v in served if listed(v, want)]
        ids = set(v.get("id") for v in shown)
        n = 0
        for v in shown:
            if not v.get("featured"):
                continue
            sib = v.get("sibling")
            if sib in ids and look[sib].get("featured") and \
                    v.get("shape") == "9:16":
                continue
            n += 1
        return n

    return (len(served),
            sum(1 for v in served if listed(v, "landscape")),
            sum(1 for v in served if listed(v, "portrait")),
            featured("landscape"), featured("portrait"))


def fail(msg):
    print("")
    print("FAILURE: %s" % msg)
    print("NOTHING was written -- neither file.")
    print("Undo is Discard Changes in GitHub Desktop.")
    return 1


def main():
    here = os.path.basename(os.path.abspath(os.getcwd())).lower()
    if not os.path.isfile(PROBE) or here in ("documentation", "gallery"):
        return fail(
            "%s is not here (%s).\n"
            "         Run this from the GALLERY repo root -- the folder that\n"
            "         holds index.html -- not from gallery/, not from\n"
            "         documentation/, and not from the orrery repo."
            % (PROBE, os.getcwd()))

    staged = []
    for path, expected, edits in FILES:
        if not os.path.isfile(path):
            return fail("%s is missing from this checkout." % path)
        raw = open(path, "rb").read()
        was_crlf = b"\r\n" in raw
        content = raw.replace(b"\r\n", b"\n") if was_crlf else raw
        if path == PAGE and P_MODE_NEW in content:
            return fail("this patch has already been applied: index.html\n"
                        "         already holds the new inCurrentMode().")
        if path == META:
            err = meta_precheck(content)
            if err:
                return fail(err)
        actual = hashlib.md5(content).hexdigest()
        if expected is not None and actual != expected:
            return fail(
                "BASE MOVED. %s is not the file this patch was built\n"
                "         against (gallery 386a44ff).\n"
                "         expected %s\n"
                "         found    %s\n"
                "         (Line endings were normalised before comparing, so\n"
                "         CRLF does not explain this -- the content differs.\n"
                "         Tell Claude; do not edit the file by hand.)"
                % (path, expected, actual))
        if was_crlf:
            print("note: %s is CRLF here; compared normalised, written back"
                  % path)
            print("      CRLF exactly as found.")
        out = content
        for label, old, new in edits:
            count = out.count(old)
            if count != 1:
                return fail("ANCHOR FAIL: expected 1 match, found %d for: %s"
                            % (count, label))
            out = out.replace(old, new)
            print("  ok  %s" % label)
        staged.append((path, out, content, was_crlf))

    inserted = b"".join(new for _, _, edits in FILES for _, _, new in edits)
    bad = sum(1 for byt in inserted if byt > 127)
    if bad:
        return fail("this patch would insert %d non-ASCII byte(s); refusing"
                    % bad)
    dirty = [(p, sum(1 for byt in c if byt > 127)) for p, _, c, _ in staged]
    dirty = [(p, n) for p, n in dirty if n]
    for path, n in dirty:
        print("note: %s already holds %d non-ASCII byte(s) this patch did"
              % (path, n))
        print("      not reach; they are unchanged.")
    if not dirty:
        print("  ok  encoding gate: inserted text is ASCII, and neither file")
        print("      holds a non-ASCII byte.")

    # The metadata must still parse, and the two cards must name each other.
    for path, out, _before, _crlf in staged:
        if path != META:
            continue
        try:
            doc = json.loads(out.decode("utf-8"))
        except ValueError as err:
            return fail("the edited metadata is not valid JSON: %s" % err)
        cards = {c.get("id"): c for c in doc.get("visualizations", [])}
        if cards.get(LAND_ID, {}).get("sibling") != POR_ID or \
                cards.get(POR_ID, {}).get("sibling") != LAND_ID:
            return fail("the two animation cards do not name each other "
                        "after the edit")
        print("  ok  metadata parses, and the two cards name each other")
        counts = tab_counts(doc)

    for path, out, _before, was_crlf in staged:
        final = out.replace(b"\n", b"\r\n") if was_crlf else out
        with open(path, "wb") as handle:
            handle.write(final)
        print("  wrote %s (%d bytes)%s"
              % (path, len(final), " [CRLF, as found]" if was_crlf else ""))

    print("")
    print("patch applied to 2 file(s)")
    print("")
    print("Stamps updated: the 'Updated' line at the top of index.html.")
    print("gallery_metadata.json's 'last_updated' is the editor's to set and")
    print("is left alone; no card was added, removed or moved.")
    print("")
    print("WHAT TO DO NEXT, in this order:")
    print("")
    print("  1. Move THIS script into documentation/. It has run.")
    print("  2. Run the gallery maintenance run:")
    print("         python gallery_maintenance_run.py")
    print("     Expect every gating checker to pass, as before. None of them")
    print("     reads the card lists, so a pass does not speak for this")
    print("     change; your eyes in step 5 do.")
    print("  3. In GitHub Desktop the change list should show exactly three")
    print("     files: index.html, gallery/gallery_metadata.json, and this")
    print("     script under documentation/. Commit and push.")
    print("  4. After the push, check what the live site serves:")
    print("         python gallery_maintenance_run.py --live")
    served, n_desk, n_mob, f_desk, f_mob = counts
    print("  5. Open https://palomasorrery.com/ on the desktop and look at")
    print("     both tabs. Desktop should list %d exhibits and Mobile %d,"
          % (n_desk, n_mob))
    print("     where both said %d before; the welcome line carries the"
          % served)
    print("     count. (These numbers were worked out just now from your")
    print("     metadata, so a card you edit later can change them.)")
    print("     The Featured strip should show %d cards on Desktop and %d on"
          % (f_desk, f_mob))
    print("     Mobile. Inner Solar System Animation should appear once in")
    print("     each, the 16:9 view on Desktop and the 9:16 on Mobile. On")
    print("     the phone the 16:9 animation card should now be gone --")
    print("     that is the other half of this patch -- and nothing else")
    print("     there should have changed.")
    print("  6. Tell Claude the new gallery SHA and what you saw.")
    print("")
    print("TONY-ACTION ROLLUP for this patch:")
    print("  (do)     steps 1 to 6 above.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
