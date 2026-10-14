"""patch_L431_10_brief_both_sets_20261013.py -- L-431 (orbital periods):
build 3's brief says the export carries BOTH element sets for a body
drawn around the solar system's barycentre, the Sun-centred ones as well
as the barycentre ones, as Tony confirmed on 2026-10-13. Records only.

Built on orrery 084d0a65ffedb9191604b321797521c651459522 at
https://github.com/tonylquintanilla/palomas_orrery ("L431 close").
The gallery is not touched.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\;
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\.
Written October 13, 2026 with Anthropic's Claude Opus 5.5.

HOW TO RUN
    From the orrery repo's ROOT folder: open this file in VS Code and
    press Run, or from a terminal in that folder:
        python patch_L431_10_brief_both_sets_20261013.py
    Success prints one "ok" line per edit, then "patch applied". It asks
    nothing and fetches nothing.

WHAT IT CHANGES
    documentation/HANDOFF_L431_build3_website_brief_20261013.md: one
      bullet at the end of section 2a (the export).
    LEDGER_CONSOLIDATED.md: L-431's line about it now says the brief
      carries it; the header stamp.

SAFETY
    Each file is checked only at the lines this patch edits: every anchor
    must match exactly once, so your notes cannot make it refuse. If any
    check fails, NOTHING is written. A file found with Windows line
    endings is matched after turning them into LF and written back LF,
    and the patch says so. Undo after a run is Discard Changes in GitHub
    Desktop.
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
MARKER = '--- Your run record below this line'

EDITS = [
    ('documentation/HANDOFF_L431_build3_website_brief_20261013.md', "line 104: - **Added 2026-10-13, on Tony's confirmation",
     '  fingerprint it.\n\n',
     '  fingerprint it.\n- **Added 2026-10-13, on Tony\'s confirmation (L-431).** For a body\n  whose period record names the solar system\'s barycentre (Sedna), the\n  export carries BOTH element sets: the barycentre ones from the period\n  record, which are drawn, and the Sun-centred ones the orrery fetches\n  every time, at the same date. A barycentre ellipse is placed in a\n  Sun-centred scene by pairing the two (horizons-orbital-mechanics, The\n  Drawn Orbit Follows the Period\'s Centre): the body\'s position from\n  each set at that date gives where the barycentre sits seen from the\n  Sun, and the orbit is moved there. With the barycentre set alone the\n  website cannot place the orbit. The pair is exported only when both\n  sets are from one fetch date, as the orrery pairs them; otherwise the\n  body is drawn from its Sun-centred elements, as the orrery does, and\n  the export says so. `test_objects_export.py` refuses a barycentre\n  record exported without its Sun-centred set. Tony, 2026-10-13, asked\n  whether the heliocentric data should also be fetched, was told it\n  already is and must travel with the barycentre set: "confirmed."\n\n'),
    ('LEDGER_CONSOLIDATED.md', 'line 401: Module updated: October 13, 2026 with Anthro',
     'rose), built on ab96681.\nReview and RICE update Tony 6-21-2026\n',
     "rose), built on ab96681.\nModule updated: October 13, 2026 with Anthropic's Claude Opus 5.5\n(L-431: build 3's brief carries both element sets for a barycentre\nbody), built on 084d0a6.\nReview and RICE update Tony 6-21-2026\n"),
    ('LEDGER_CONSOLIDATED.md', 'line 1789: - **For build 3, confirmed by Tony; added to',
     "- **For build 3, confirmed by Tony and not yet in the brief's export\n  list.** A body drawn around the barycentre is placed in a Sun-centred\n",
     "- **For build 3, confirmed by Tony; added to the brief's section 2a\n  on 2026-10-13 (patch_L431_10).** A body drawn around the barycentre is placed in a Sun-centred\n"),
    ('LEDGER_CONSOLIDATED.md', 'line 1799: "confirmed." The brief\'s section 2a listed o',
     '  "confirmed." The brief\'s section 2a lists only "the elements around\n  that centre". (This line was in a later copy of patch_L431_8 than the\n  one that ran.)\n',
     '  "confirmed." The brief\'s section 2a listed only "the elements around\n  that centre" until patch_L431_10 added the rest at Tony\'s request.\n  (This line was in a later copy of patch_L431_8 than the one that\n  ran.)\n'),
]



def apply():
    texts, crlf, done = {}, set(), []
    for f, label, old, new in EDITS:
        path = os.path.join(ROOT, f)
        if f not in texts:
            if not os.path.exists(path):
                print('ERROR: %s not found in %s. NOTHING was written.' % (f, ROOT))
                return None
            raw = open(path, 'rb').read()
            if b'\r\n' in raw:
                crlf.add(f)
            texts[f] = raw.replace(b'\r\n', b'\n').decode('utf-8')
        t = texts[f]
        n = t.count(old)
        if n != 1:
            print('ANCHOR FAIL  %-45s %s (found %d times, expected 1). NOTHING was written.'
                  % (f, label, n))
            if n == 0 and 'BOTH element sets: the barycentre ones' in t:
                print('It looks as though this patch has already run.')
            return None
        if MARKER in t and t.index(old) > t.index(MARKER):
            print('ANCHOR FAIL  %-45s %s lies below the run-record marker. NOTHING was written.'
                  % (f, label))
            return None
        texts[f] = t.replace(old, new)
        done.append((f, label))
    for f, label, old, new in EDITS:
        if any(ord(c) > 127 for c in new):
            print('ERROR: an edit to %s would add non-ASCII. NOTHING was written.' % f)
            return None
    for f, t in texts.items():
        with open(os.path.join(ROOT, f), 'w', encoding='utf-8', newline='') as h:
            h.write(t)
    for f, label in done:
        print('ok  %-45s %s' % (f, label))
    for f in sorted(crlf):
        print('note: %s was CRLF in the working copy; written LF' % f)
    print()
    print('patch applied (%d edits in %d files)' % (len(done), len(texts)))
    print('Stamps updated: the ledger.')
    print()
    print("Build 3's brief, section 2a, now asks the export to carry both element sets for")
    print("a body drawn around the barycentre (Sedna): the Sun-centred ones and the")
    print('barycentre ones, from one fetch date.')
    return True


def main():
    if not apply():
        return 1
    print()
    print('NEXT:')
    print('  1. Run orrery_maintenance_run.py; it rebuilds the ledger index.')
    print('  2. Move this script into documentation/; commit and push.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
