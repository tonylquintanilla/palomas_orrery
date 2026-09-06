"""
patch_L287_4_sentence_sources.py -- index.html shows room sentences and
card sources; fixes the "NaN KB" size on schema-v2 cards.

RUN: save at the gallery repo root (next to index.html), open in VS Code,
Run. Guards on index.html matching the gallery repo at 6a180d83.

Tony's finding 2026-09-04: a door's sentence and a card's sources, both
set in the editor, did not appear on the page. Today's selector had no
place for them. Now: the sentence sits under its door/room header; the
sources sit under each card's description, URLs clickable. Also: the
schema-v2 size_kb is a dict per file slot, which the old size line
printed as "NaN KB"; it now shows the larger slot's size.

Written September 4, 2026 with Anthropic's Claude Fable 5.1. Built on
gallery 6a180d83e0f8bc5878c6104be7e2ed3b47816992. Archive to
documentation/ once run.
"""
import hashlib, os, sys
EXPECT = "3c518762187eeeca295599d472cc537c"
EDITS = [(b'        .viz-card-size {\n            font-size: 0.62rem;', b'        .viz-card-sources {\n            font-size: 0.62rem;\n            color: var(--text-secondary);\n            opacity: 0.8;\n            margin-top: 3px;\n            word-break: break-all;\n        }\n        .viz-card-sources a { color: inherit; }\n\n        .category-sentence {\n            font-size: 0.78rem;\n            color: var(--text-secondary);\n            font-style: italic;\n            padding: 4px 12px 6px 12px;\n            line-height: 1.4;\n        }\n\n        .viz-card-size {\n            font-size: 0.62rem;'), (b"        var STORAGE_KEY = 'other';   // the hidden room; never served (L-287)\n", b"        var STORAGE_KEY = 'other';   // the hidden room; never served (L-287)\n        var ROOM_SENTENCES = {};     // schema v2: room path -> placard sentence\n"), (b'                    ROOM_LABELS[path] = r.label || r.key;\n                    if (r.rooms) walk(r.rooms, path);\n', b'                    ROOM_LABELS[path] = r.label || r.key;\n                    if (r.sentence) ROOM_SENTENCES[path] = r.sentence;\n                    if (r.rooms) walk(r.rooms, path);\n'), (b'                if (!v.filename && keys.length) v.filename = files[keys[0]];\n', b"                if (!v.filename && keys.length) v.filename = files[keys[0]];\n                if (v.size_kb && typeof v.size_kb === 'object') {\n                    var total = 0, sk = Object.keys(v.size_kb);\n                    for (var s = 0; s < sk.length; s++) total = Math.max(total, Number(v.size_kb[sk[s]]) || 0);\n                    v.size_kb = total;\n                }\n"), (b'                html += \'</div>\';\n                html += \'<div class="category-items" data-cat="\' + catKey + \'">\';\n', b'                html += \'</div>\';\n                html += \'<div class="category-items" data-cat="\' + catKey + \'">\';\n                if (ROOM_SENTENCES[catKey]) {\n                    html += \'<div class="category-sentence">\' + escapeHtml(ROOM_SENTENCES[catKey]) + \'</div>\';\n                }\n'), (b'                            if (item.description) {\n                                html += \'<div class="viz-card-desc">\' + escapeHtml(item.description) + \'</div>\';\n                            }\n', b'                            if (item.description) {\n                                html += \'<div class="viz-card-desc">\' + escapeHtml(item.description) + \'</div>\';\n                            }\n                            html += sourcesHtml(item);\n'), (b'                        if (item.description) {\n                            html += \'<div class="viz-card-desc">\' + escapeHtml(item.description) + \'</div>\';\n                        }\n', b'                        if (item.description) {\n                            html += \'<div class="viz-card-desc">\' + escapeHtml(item.description) + \'</div>\';\n                        }\n                        html += sourcesHtml(item);\n'), (b'        // ---- Initialize ----\n        async function init() {\n', b'        // Card sources (schema v2): one line, URLs clickable, each escaped.\n        function sourcesHtml(item) {\n            var src = item.sources;\n            if (!src || !src.length) return \'\';\n            var parts = [];\n            for (var i = 0; i < src.length; i++) {\n                var s = String(src[i]);\n                var e = escapeHtml(s);\n                parts.push(/^https?:\\/\\//.test(s)\n                    ? \'<a href="\' + e + \'" target="_blank" rel="noopener">\' + e + \'</a>\' : e);\n            }\n            return \'<div class="viz-card-sources">Sources: \' + parts.join(\'; \') + \'</div>\';\n        }\n\n        // ---- Initialize ----\n        async function init() {\n')]
def die(m):
    print("ERROR: " + m); print("NOTHING was written."); sys.exit(1)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
raw = open("index.html", "rb").read()
crlf = b"\r\n" in raw
s = raw.replace(b"\r\n", b"\n") if crlf else raw
got = hashlib.md5(s).hexdigest()
if got != EXPECT:
    die("index.html does not match 6a180d83 (md5 %s, expected %s)" % (got, EXPECT))
print("ok  index.html matches 6a180d83" + (" (working copy is CRLF)" if crlf else ""))
for o, n in EDITS:
    if s.count(o) != 1:
        die("anchor not found exactly once: %r" % o[:60])
    s = s.replace(o, n)
if any(b > 127 for b in s):
    die("non-ASCII byte in result")
open("index.html", "wb").write(s.replace(b"\n", b"\r\n") if crlf else s)
print("index.html: %d edits (CSS, ROOM_SENTENCES, tree read, size fix, sentence under header, sources on cards x2, sourcesHtml). Patch applied." % len(EDITS))
print("Mode 5: after pushing, the Solar System header should carry your remodel sentence and the placed cards their sources.")
