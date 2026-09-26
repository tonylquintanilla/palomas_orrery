"""patch_L286_4_exhibit_chain_20260925.py -- L-286, the chain in the exhibit rooms.

RUN COMMAND

    Save this file in the ROOT of the gallery repository
    (tonyquintanilla.github.io), beside index.html. Open it in VS Code
    and click Run.

WHAT IT CHANGES -- two files, all-or-nothing

    interactive.html
        The top bar reads "Paloma's Orrery | Solar : Earth", as the
        gallery's header does, with the room's title on a second line
        under it. "Paloma's Orrery" goes to the lobby and each part of
        the chain to that screen of the gallery. The "Gallery" link it
        replaces is gone.
        - The chain is read from the gallery's own files: the card whose
          live link opens this room gives the room's path, and
          gallery_config.json gives the short names and the door's
          colour. No room names are written into interactive.html, so a
          card moved in the editor moves its chain.
        - When the visitor came from the gallery and a link names the
          very screen they came from, it steps back in the browser's
          history instead of going forward, as the "Gallery" link did
          since L-282. So Back afterwards does not return to the room.
        - If either gallery file fails to load, only "Paloma's Orrery"
          shows.

    index.html
        Opening a live card records the screen it was opened from, for
        the step-back above (sessionStorage "po_gallery_from").

TESTED BEFORE DELIVERY, headless, on a copy of the gallery at a21680ab,
as a phone (390x844) and a desktop: lobby -> the Earth card -> the
exhibit shows "Solar : Earth" -> Earth opens the Earth room (forward,
since the lobby was behind it); the Earth room -> the Earth card ->
Earth steps back to the room (history did not grow); Solar opens the
door's screen; the Sun and the Explorer opened directly show "Solar :
Sun" and "Solar". No page errors. The gallery maintenance run passed 16
of 16 on the patched copy. Nothing here was seen on a real phone.

Built on gallery a21680ab at
https://github.com/tonylquintanilla/tonyquintanilla.github.io
Recorded on orrery c6cbacae, L-286.

Written September 25, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os
import sys

FILES = [('interactive.html', '27398ce7bc3a250d561bbe97fdf4e077', '8218f98498d405104f354a2d8832e042', [("the page's Updated stamp", b"        press in the plot closes Plotly's own hover box)\n     Architecture: Option C viewer", b'        press in the plot closes Plotly\'s own hover box)\n     Updated: September 25, 2026 with Anthropic\'s Claude Opus 5.5\n       (L-286: the gallery\'s chain comes to the exhibit rooms. The top\n        bar reads "Paloma\'s Orrery | Solar : Earth" as the gallery\'s\n        header does, each part a link to that screen of the gallery,\n        with the room\'s title under it; the "Gallery" link it replaces\n        is gone. The chain is built from the gallery\'s own config and\n        the card that opens this room, so a card moved in the editor\n        moves its chain. A link steps back in history instead of\n        forward when the gallery screen it names is the one the visitor\n        came from)\n     Architecture: Option C viewer'), ('styles for the chain in the top bar', b"        .top-title {\n            font-family: 'Cormorant Garamond', serif;\n            font-size: 16px;\n            font-weight: 600;\n            color: var(--text-primary);\n            text-align: center;\n        }", b"        /* The chain (L-286, 2026-09-25): the same top-left block as the\n           gallery's header, and the room's title on a second line. */\n        .top-bar { flex-wrap: wrap; row-gap: 2px; padding: 6px 16px; }\n        .top-left { display: flex; align-items: center; gap: 12px; min-width: 0; flex: 1; }\n        .site-home {\n            font-family: 'Cormorant Garamond', Georgia, serif;\n            font-size: 17px;\n            font-weight: 600;\n            color: var(--accent);\n            text-decoration: none;\n            white-space: nowrap;\n            padding: 6px 0;\n            flex-shrink: 0;\n        }\n        .top-sep { width: 1px; height: 18px; background: var(--border); flex-shrink: 0; }\n        .top-chain {\n            display: flex;\n            align-items: center;\n            gap: 6px;\n            min-width: 0;\n            font-size: 14px;\n            white-space: nowrap;\n            overflow: hidden;\n        }\n        .top-chain:empty { display: none; }\n        .top-chain a { text-decoration: none; padding: 6px 0; }\n        .top-chain .chain-colon { color: var(--text-dim); }\n        .top-title {\n            order: 3;\n            flex-basis: 100%;\n            font-family: 'DM Sans', sans-serif;\n            font-size: 12.5px;\n            font-weight: 400;\n            color: var(--text-secondary);\n            text-align: left;\n            white-space: nowrap;\n            overflow: hidden;\n            text-overflow: ellipsis;\n        }"), ("the phone's title size follows the new line", b'            .top-title { font-size: 14px; }\n        }', b'            .top-title { font-size: 12px; }\n            .top-bar { padding: 6px 12px; }\n            .top-left { gap: 10px; }\n            .site-home { font-size: 16px; }\n            .top-chain { font-size: 13.5px; }\n        }'), ("the top bar's markup", b'            <a href="index.html" class="back-link">\n                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>\n                Gallery\n            </a>\n            <div class="top-title" id="top-title">Solar System Explorer</div>', b'            <div class="top-left">\n                <a href="index.html" class="site-home" id="site-home">Paloma\'s Orrery</a>\n                <nav class="top-chain" id="top-chain" aria-label="Where you are"></nav>\n            </div>\n            <div class="top-title" id="top-title">Solar System Explorer</div>'), ("the chain replaces the Gallery link's code", b'// ====================================================================\n// BACK TO THE GALLERY (L-282, September 5, 2026)\n// ====================================================================\n// A plain link to index.html goes FORWARD, leaving lobby -> exhibit ->\n// lobby in the browser\'s history; Safari\'s back then lands on the\n// exhibit, which is what Tony saw on the phone. When the page behind\n// us is our own gallery, step back instead. Opened from a shared link\n// with no gallery behind, the link works as written. Runs on both\n// exhibit paths (the Sun never calls initControls).\n(function () {\n    const link = document.querySelector(".top-bar .back-link");\n    if (!link) { return; }\n    link.addEventListener("click", function (ev) {\n        let ref = null;\n        try { ref = document.referrer ? new URL(document.referrer) : null; } catch (e) { ref = null; }\n        const fromGallery = ref && ref.origin === window.location.origin &&\n            (/\\/index\\.html$/.test(ref.pathname) || /\\/$/.test(ref.pathname));\n        if (fromGallery && window.history.length > 1) {\n            ev.preventDefault();\n            window.history.back();\n        }\n    });\n})();', b'// ====================================================================\n// THE CHAIN (L-286, September 25, 2026; replaces BACK TO THE GALLERY,\n// L-282, September 5, 2026)\n// ====================================================================\n// "Paloma\'s Orrery" and each part of the chain link to a screen of the\n// gallery: the lobby, or index.html#room=<path>. A plain link goes\n// FORWARD, leaving gallery -> exhibit -> gallery in the history, and\n// Safari\'s back then lands on the exhibit (what Tony saw on the phone,\n// L-282). So when the page behind us is our own gallery AND the screen\n// a link names is the one the visitor came from -- index.html records\n// it in sessionStorage as "po_gallery_from" when it opens a live card\n// -- the link steps back instead. Otherwise it works as written.\n// The chain is read from the gallery\'s own files: the card whose live\n// link opens this room gives the room\'s path, and the config gives each\n// level\'s short name and the door\'s colour. No room names are kept\n// here. If either file fails to load, only "Paloma\'s Orrery" shows.\n// Runs on every exhibit path (the Sun never calls initControls).\n(function () {\n    const exhibitOf = (search) => (new URLSearchParams(search).get("exhibit") ||\n                                   "solar-system-explorer").toLowerCase();\n    const here = exhibitOf(window.location.search);\n    function stepBackIfCameFrom(ev, hash) {\n        let ref = null;\n        try { ref = document.referrer ? new URL(document.referrer) : null; } catch (e) { ref = null; }\n        const fromGallery = ref && ref.origin === window.location.origin &&\n            (/\\/index\\.html$/.test(ref.pathname) || /\\/$/.test(ref.pathname));\n        let from = null;\n        try { from = window.sessionStorage.getItem("po_gallery_from"); } catch (e) { from = null; }\n        if (fromGallery && from === hash && window.history.length > 1) {\n            ev.preventDefault();\n            window.history.back();\n        }\n    }\n    const home = document.getElementById("site-home");\n    if (home) { home.addEventListener("click", (ev) => stepBackIfCameFrom(ev, "")); }\n    const chainEl = document.getElementById("top-chain");\n    if (!chainEl) { return; }\n    Promise.all([\n        fetch("gallery/gallery_config.json").then((r) => r.json()),\n        fetch("gallery/gallery_metadata.json").then((r) => r.json())\n    ]).then(([config, metadata]) => {\n        const card = ((metadata && metadata.visualizations) || []).find((v) =>\n            v.live && /^interactive\\.html(\\?|$)/.test(v.live) &&\n            exhibitOf(v.live.split("?")[1] || "") === here);\n        if (!card || !card.room) { return; }\n        let level = (config && config.doors) || [];\n        let path = "";\n        let color = null;\n        const crumbs = [];\n        for (const key of card.room.split("/")) {\n            const node = level.find((r) => r.key === key);\n            if (!node) { return; }\n            path = path ? path + "/" + key : key;\n            if (!color) { color = node.color || null; }\n            crumbs.push({ path: path, label: node.short || node.label || node.key });\n            level = node.rooms || [];\n        }\n        chainEl.textContent = "";\n        const sep = document.createElement("span");\n        sep.className = "top-sep";\n        chainEl.parentNode.insertBefore(sep, chainEl);\n        crumbs.forEach((c, i) => {\n            if (i) {\n                const colon = document.createElement("span");\n                colon.className = "chain-colon";\n                colon.textContent = ":";\n                chainEl.appendChild(colon);\n            }\n            const a = document.createElement("a");\n            a.href = "index.html#room=" + c.path;\n            a.textContent = c.label;\n            if (color) { a.style.color = color; }\n            a.addEventListener("click", (ev) => stepBackIfCameFrom(ev, "#room=" + c.path));\n            chainEl.appendChild(a);\n        });\n    }).catch(() => {});\n})();')]), ('index.html', '7828c088e8f014ba832e37e0de1402fa', '2d06508b0570c3d39a02b8f8bb6a8bea', [("the page's Updated stamp", b'         in Tony\'s words: "Logo created with Gemini (Google)." -->\n<html lang="en">', b'         in Tony\'s words: "Logo created with Gemini (Google)."\n     Updated: September 25, 2026 with Anthropic\'s Claude Opus 5.5\n       - Opening a live card records the screen it was opened from\n         (sessionStorage "po_gallery_from"), so the chain in\n         interactive.html can step back to that screen instead of\n         going forward to a new copy of it (L-286). -->\n<html lang="en">'), ('a live card records where it was opened from', b"            if (!viz.live) history.pushState(null, '', '#' + vizId);\n            loadVisualization(vizId);", b"            if (!viz.live) history.pushState(null, '', '#' + vizId);\n            else {\n                try { sessionStorage.setItem('po_gallery_from', window.location.hash); } catch (e) {}\n            }\n            loadVisualization(vizId);")])]


def fail(msg):
    print("")
    print("FAILURE: %s" % msg)
    print("NOTHING was written.")
    print("Undo is Discard Changes in GitHub Desktop.")
    return 1


def main():
    here = os.path.basename(os.path.abspath(os.getcwd())).lower()
    if not os.path.isfile("index.html") or here in ("documentation", "gallery", "tools"):
        return fail(
            "index.html is not here (%s).\n"
            "         Run this from the GALLERY repo root -- the folder that\n"
            "         holds index.html -- not from gallery/, tools/ or\n"
            "         documentation/, and not from the orrery repo."
            % os.getcwd())

    results = []
    for name, expected, result, edits in FILES:
        if not os.path.isfile(name):
            return fail("%s is not here." % name)
        raw = open(name, "rb").read()
        was_crlf = b"\r\n" in raw
        content = raw.replace(b"\r\n", b"\n") if was_crlf else raw
        actual = hashlib.md5(content).hexdigest()
        if actual == result:
            return fail("this patch has already been applied: %s already\n"
                        "         has the chain." % name)
        if actual != expected:
            return fail(
                "BASE MOVED. %s is not the file this patch was built\n"
                "         against (gallery a21680ab).\n"
                "         expected %s\n"
                "         found    %s\n"
                "         Tell Claude; do not edit the file by hand."
                % (name, expected, actual))
        out = content
        for label, old, new in edits:
            count = out.count(old)
            if count != 1:
                return fail("ANCHOR FAIL in %s: expected 1 match, found %d for: %s"
                            % (name, count, label))
            out = out.replace(old, new)
            print("  ok  %s: %s" % (name, label))
        if any(byt > 127 for byt in out):
            return fail("non-ASCII text would be written to %s; refusing" % name)
        if hashlib.md5(out).hexdigest() != result:
            return fail("%s would not be the file this patch was built and\n"
                        "         tested to produce." % name)
        print("  ok  %s is the file that was tested, and ASCII" % name)
        results.append((name, out.replace(b"\n", b"\r\n") if was_crlf else out, was_crlf))

    for name, data, was_crlf in results:
        with open(name, "wb") as handle:
            handle.write(data)
        print("  wrote %s (%d bytes)%s" % (name, len(data),
                                            " [CRLF, as found]" if was_crlf else ""))

    print("")
    print("patch applied to 2 files")
    print("")
    print("Stamps updated: the 'Updated' lines at the top of interactive.html")
    print("and index.html.")
    print("")
    print("WHAT TO DO NEXT, in this order:")
    print("")
    print("  1. Move THIS script into documentation/. It has run.")
    print("  2. Run the gallery maintenance run:")
    print("         python gallery_maintenance_run.py")
    print("     Expect 16 of 16 gating checkers to pass, as before.")
    print("  3. In GitHub Desktop the change list should show index.html,")
    print("     interactive.html and this script under documentation/, plus")
    print("     whatever the maintenance run rewrites as usual. Commit and push.")
    print("  4. After the push: python gallery_maintenance_run.py --live")
    print("  5. On the phone, after about ten minutes, close the page and")
    print("     open it again, then:")
    print("       - Open the Earth room and its Earth and Moon card. The top")
    print("         bar reads Paloma's Orrery | Solar : Earth, with Earth")
    print("         under it.")
    print("       - Tap Earth in that bar: you are back in the Earth room.")
    print("         Swipe back: you should NOT land on the exhibit again.")
    print("       - Open the Sun from its room and tap Solar: the Solar")
    print("         System screen.")
    print("       - Check the room still works as before: the drawer, the")
    print("         i panel, a marker tap.")
    print("     The same on the desktop.")
    print("  6. Tell Claude the new gallery SHA and what you saw.")
    print("")
    print("TONY-ACTION ROLLUP for this patch:")
    print("  (do)     steps 1 to 6 above.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
