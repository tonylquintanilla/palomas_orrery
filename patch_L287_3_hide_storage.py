"""
patch_L287_3_hide_storage.py -- index.html: cards in Storage are not served.

RUN: save at the gallery repo root (next to index.html), open in VS Code,
Run. Guards on index.html matching the gallery repo at 969f8c24.

Tony's ruling 2026-09-04: Storage is visible only in the gallery editor.
The page now drops every card whose room is "other" after loading a
version-2 gallery_metadata.json, so the Desktop/Mobile lists show only
cards placed in rooms. The list is empty until the remodel begins.
The ?preview=<file> route is unaffected: it bypasses the index.

Written September 4, 2026 with Anthropic's Claude Fable 5.1. Built on
gallery 969f8c2412a6bb25f81fa9bddd961df7df84c9d8. Archive to
documentation/ once run.
"""
import hashlib, os, sys
EXPECT = "505af4e3b331f0ecb66fbdec1b176d9d"
EDITS = [
    (b'        var ROOM_LABELS = {};   // schema v2: room path -> label (filled from config doors)\n', b"        var ROOM_LABELS = {};   // schema v2: room path -> label (filled from config doors)\n        var STORAGE_KEY = 'other';   // the hidden room; never served (L-287)\n"),
    (b'                if (metadata && metadata.version === 2) {\n                    normalizeSchemaV2(metadata.visualizations || []);\n                }\n', b"                if (metadata && metadata.version === 2) {\n                    normalizeSchemaV2(metadata.visualizations || []);\n                    // Storage is hidden from visitors (Tony's ruling, L-287):\n                    // only cards placed in a room are served.\n                    metadata.visualizations = (metadata.visualizations || []).filter(\n                        function (v) { return v.room && v.room !== STORAGE_KEY; });\n                }\n"),
]
def die(m):
    print("ERROR: " + m); print("NOTHING was written."); sys.exit(1)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
raw = open("index.html", "rb").read()
crlf = b"\r\n" in raw
s = raw.replace(b"\r\n", b"\n") if crlf else raw
got = hashlib.md5(s).hexdigest()
if got != EXPECT:
    die("index.html does not match 969f8c24 (md5 %s, expected %s)" % (got, EXPECT))
print("ok  index.html matches 969f8c24" + (" (working copy is CRLF)" if crlf else ""))
for o, n in EDITS:
    if s.count(o) != 1:
        die("anchor not found exactly once: %r" % o[:60])
    s = s.replace(o, n)
if any(b > 127 for b in s):
    die("non-ASCII byte in result")
open("index.html", "wb").write(s.replace(b"\n", b"\r\n") if crlf else s)
print("index.html: 2 edits (STORAGE_KEY constant; storage cards dropped after load). Patch applied.")
print("Mode 5: reload palomasorrery.com after pushing; Desktop and Mobile should list no Storage cards.")
