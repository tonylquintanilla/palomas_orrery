"""
patch_L287_5_live_cards.py -- index.html: a card with a live scene URL
opens that scene when clicked, wears a "Live scene" badge, and is listed
in both Desktop and Mobile even when it has no file.

RUN: save at the gallery repo root (next to index.html), open in VS Code,
Run. Guards on index.html matching the gallery repo at 1dabcf8f.

Tony 2026-09-05: "unclear how to create an interactive card." The
editor side: set Live scene URL (Pick...). This is the page side: the
click handler honours it. Rule from L-282: a live scene is one card in
the grid.

Written September 5, 2026 with Anthropic's Claude Fable 5.1. Built on
gallery 1dabcf8f704248a6afa96427329ee294253068dd. Archive to
documentation/ once run.
"""
import hashlib, os, sys
EXPECT = "fa74f049b823df201258e63eb40ace53"
EDITS = [(b'        async function loadVisualization(vizId) {\n            var viz = vizLookup[vizId];\n            if (!viz) return;\n', b'        async function loadVisualization(vizId) {\n            var viz = vizLookup[vizId];\n            if (!viz) return;\n            if (viz.live) {                 // a live card opens its scene (L-287)\n                window.location.href = viz.live;\n                return;\n            }\n'), (b'                            if (item.featured) {\n                                html += \'<div class="viz-card-featured">Featured</div>\';\n                            }\n', b'                            if (item.featured) {\n                                html += \'<div class="viz-card-featured">Featured</div>\';\n                            }\n                            if (item.live) {\n                                html += \'<div class="viz-card-featured">Live scene</div>\';\n                            }\n'), (b'                        if (item.featured) {\n                            html += \'<div class="viz-card-featured">Featured</div>\';\n                        }\n', b'                        if (item.featured) {\n                            html += \'<div class="viz-card-featured">Featured</div>\';\n                        }\n                        if (item.live) {\n                            html += \'<div class="viz-card-featured">Live scene</div>\';\n                        }\n'), (b"                if (!v.mode) {\n                    v.mode = keys.length > 1 ? 'both' : (keys[0] || 'landscape');\n                }\n", b"                if (!v.mode) {\n                    v.mode = (keys.length > 1 || (!keys.length && v.live)) ? 'both'\n                             : (keys[0] || 'landscape');\n                }\n")]
def die(m):
    print("ERROR: " + m); print("NOTHING was written."); sys.exit(1)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
raw = open("index.html", "rb").read()
crlf = b"\r\n" in raw
s = raw.replace(b"\r\n", b"\n") if crlf else raw
got = hashlib.md5(s).hexdigest()
if got != EXPECT:
    die("index.html does not match 1dabcf8f (md5 %s, expected %s)" % (got, EXPECT))
print("ok  index.html matches 1dabcf8f" + (" (working copy is CRLF)" if crlf else ""))
for o, n in EDITS:
    if s.count(o) != 1:
        die("anchor not found exactly once: %r" % o[:60])
    s = s.replace(o, n)
if any(b > 127 for b in s):
    die("non-ASCII byte in result")
open("index.html", "wb").write(s.replace(b"\n", b"\r\n") if crlf else s)
print("index.html: %d edits (live click opens scene; Live scene badge x2; scene-only cards list in both modes). Patch applied." % len(EDITS))
print("Mode 5: set a live URL on a card in the editor, save, push; the card should show a Live scene badge and open the scene.")
