"""
patch_L322_5_export_slice_lists_20260917.py -- ORRERY repo. L-322, the
gallery half, piece 0 of
documentation/BUILD_MANIFEST_L322_gallery_half_20260917.md.

Built on 9dabda96e289175aaff0e24b377083dace128530
at https://github.com/tonylquintanilla/palomas_orrery

RUN
---
Save this file in the orrery repo root, beside constants_new.py, and
click Run in VS Code.

    python patch_L322_5_export_slice_lists_20260917.py

WHAT IT DOES -- all or nothing
------------------------------
    export_constants.py       the export carries closed_slices and
                              transitional, read from constants_rows.py;
                              SCHEMA moves to 2
    test_constants_export.py  check 4 compares both lists against the
                              store, so the gallery cannot read a stale
                              copy of either
    LEDGER_CONSOLIDATED.md    one note on L-322 recording the four
                              decisions of 2026-09-17 and what the Earth
                              and Sun slices will meet

Why: the gallery's pointer join must know which slices are closed to
know whether a row that is not exported is a failure or a named gap,
and the store's own list is the only honest source.

Every file is checked before anything is written; if a check fails,
NOTHING is written. A second run refuses, because the files no longer
match the version this patch was built on.

SUCCESS looks like three "ok" lines, then "patch applied". Then:
    1. Move this script into documentation/.
    2. python ledger_index.py LEDGER_CONSOLIDATED.md   (twice; OK: 330)
    3. python orrery_maintenance_run.py
       Expect 16 of 16 gating checkers, and Constants export rewriting
       data/constants_export.json with the two new fields.
    4. Commit and push, and report the SHA: the gallery half pulls the
       export at that SHA.

UNDO: Discard Changes in GitHub Desktop.

Role: patch
Domain: dev_tools

Written September 17, 2026 with Anthropic's Claude Opus 5.
"""

import base64
import hashlib
import os
import sys

FINGERPRINTS = {'export_constants.py': '6ac22cd840898624258b16d6f514bbd1', 'test_constants_export.py': '8f8bfbaa4242a8dfd39eb1bbf48ac7f7', 'LEDGER_CONSOLIDATED.md': 'e10aa7da46afda9c972a3ff301df1a19'}

ANCHOR = '**Ref:** L-305, L-306 (approximations are not promoted), L-314,\n'

NOTE = ('**Note (2026-09-17) -- the gallery half is specified, reviewed and\n'
      'under build; four decisions recorded.** The order question of the\n'
      "previous note was answered by Fable's reply\n"
      '(`documentation/REPLY_L322_order_question_Fable_20260917.md`) with a\n'
      'third order, C: the gallery half is built now, and Store drift is not\n'
      'retired but NARROWED to the links the export cannot serve yet,\n'
      'retiring itself when that set is empty. Tony concurred. The build\n'
      'contract is `documentation/BUILD_MANIFEST_L322_gallery_half_20260917.md`,\n'
      "which SUPERSEDES section 9 of the mechanism manifest, plus Fable's\n"
      'addendum of the same day answering five findings Opus measured against\n'
      'it.\n'
      'TONY\'S RULING, 2026-09-17, in his words: "my ruling was intended to\n'
      'insure that constants_new.py remained the single source of truth.\n'
      'however, a tool reading and writing is not creating a second store, it\n'
      'is just transmitting. so, i concur with your option 2." The served\n'
      'numbers therefore stay in `data/objects_config.json`, the file the page\n'
      'reads at boot, written there by a tool from the export and never by\n'
      'hand; a hand edit fails the next run. Ruling 8 of 2026-09-11 is read in\n'
      'that light: its target was the hand copy, and a generated, checked\n'
      'mirror is not one.\n'
      'THE FIVE FINDINGS, measured at gallery `cb1762a7`, all accepted by the\n'
      "addendum: (1) the config's pointers sit in FIVE value-slot shapes, not\n"
      'three, and the two the manifest misplaced are served today, so the\n'
      'mirror finds a slot by the rule `config_value()` already uses rather\n'
      'than by a census of shapes; (2) the unit-token spelling is compared or\n'
      'asserted in SIX files, not two -- `feature_renderers.js`,\n'
      '`earth_geometry.js`, `tools/test_gallery_cache_builder_offline.py` and\n'
      'the three smoke suites; (3) a token change needs a guard, below; (4)\n'
      'the config is hand-formatted, so the mirror edits it IN PLACE, a\n'
      'scanner recording where each value sits and only the changed bytes\n'
      'replaced (measured: 30 insertions, 13 deletions, nothing else moved);\n'
      "(5) the manifest's five formatting sites were a reading, not a method,\n"
      'and the method is to trace each slot field to every print --\n'
      '`interactive.html` is out of scope by measurement, its ten formatting\n'
      'calls being propagated orbital elements, an axis label, SVG coordinates\n'
      'and a cache key.\n'
      "THE GUARD, two verdicts, Tony's decision of 2026-09-17 on Fable's\n"
      'proposal: a change of SPELLING is ordinary; a different token with the\n'
      'SAME number is a RELABEL, refused by default and written when the run\n'
      'names the link, because the page asserts the old name by hand; a\n'
      'different token with a DIFFERENT number is a UNIT CONFLICT, refused\n'
      'always, because nothing in the gallery converts units. The comparison\n'
      'allows for the export being rounded to declared figures while the\n'
      'config holds the unrounded hand copy. Refusal is per link: every other\n'
      'link is still written and the run exits non-zero.\n'
      "A LINK TO THE ROW THAT DEFINES ITS OWN UNIT IS EXACTLY 1, Tony's\n"
      "decision of 2026-09-17, choosing Fable's fix over Opus's reference-only\n"
      "marker. Earth's crust is 1.0 r_earth and points at\n"
      'EARTH_EQUATORIAL_RADIUS_KM, the row the token table names as one\n'
      'r_earth; the mirror transmits 1 with `# Figures: exact`, reading the\n'
      'defining constant from the token table the export already carries, so\n'
      'no factor is typed in the gallery and the 1.0 is sourced rather than\n'
      'asserted. The pointer keeps one meaning.\n'
      'WHAT THE SLICES WILL MEET, measured: four RELABELS in the Earth slice\n'
      '-- EARTH_MAGNETOPAUSE_SHUE_A6 (0.58), SHUE_A8 (0.024),\n'
      'EARTH_BOW_SHOCK_JELINEK_EPS (6.55) and JELINEK_LAMBDA (1.17) hold\n'
      '`dimensionless` in the config and the page asserts that name at\n'
      '`feature_renderers.js` 1642, 1644, 1703 and 1705, so the four rows, the\n'
      'four config links and the four asserts move in one commit. Two UNIT\n'
      'CONFLICTS in the Sun slice: CORE_AU (config 0.2 r_sun) and\n'
      'RADIATIVE_ZONE_AU (config 0.713 r_sun) are coefficients the store holds\n'
      'in au, and each wants a derived store row in solar radii. One CONFIG\n'
      'LINK MOVE in the Sun slice: the photosphere points at SOLAR_RADIUS_AU\n'
      'and should point at SUN_RADIUS_KM, the row that defines r_sun, so the\n'
      'definition rule can serve it as 1.\n'
      'BUILT SO FAR, tested in a sandbox, not yet delivered: piece 0 of the\n'
      'gallery manifest, in this patch -- the export carries `closed_slices`\n'
      'and `transitional` from `constants_rows.py` and its checker compares\n'
      "both against the store, so the gallery's pointer join reads the slice\n"
      'list from the one place that owns it; SCHEMA moves to 2. In the gallery\n'
      'repo: `tools/mirror_constants.py` and `tools/test_mirror_constants.py`,\n'
      '39 fixture checks covering every verdict. Still to build: the runner\n'
      'wiring (pull, mirror, mirror check, pointer join, export freshness,\n'
      "Store drift narrowed) and the page's unit vocabulary and figure\n"
      'formatting.\n'
      '**Ref:** L-305, L-306 (approximations are not promoted), L-314,\n')

FILES = [
    ('export_constants.py', 'aa04d29631540dd2c296cefdd52fb8cd44deb638cdaf25fa13743efcb0d40055',
     (
        'IiIiCmV4cG9ydF9jb25zdGFudHMucHkgLS0gd3JpdGUgZGF0YS9jb25zdGFudHNfZXhw'
        'b3J0Lmpzb24gZnJvbQpjb25zdGFudHNfbmV3LnB5LiBUaGUgb3JyZXJ5IGlzIHRoZSBw'
        'cm9kdWNlciBvZiBpdHMgbnVtYmVyczsgdGhlIGdhbGxlcnkKcmVhZHMgdGhpcyBmaWxl'
        'IGFuZCBuZXZlciByZWFkcyBvcnJlcnkgc291cmNlLgoKUlVOIENPTU1BTkQKLS0tLS0t'
        'LS0tLS0KT3BlbiB0aGlzIGZpbGUgaW4gVlMgQ29kZSBhbmQgY2xpY2sgUnVuLiBJdCB0'
        'YWtlcyBubyBhcmd1bWVudHMuCgogICAgcHl0aG9uIGV4cG9ydF9jb25zdGFudHMucHkK'
        'Cm9ycmVyeV9tYWludGVuYW5jZV9ydW4ucHkgcnVucyBpdCBvbiBldmVyeSBtYWludGVu'
        'YW5jZSBydW4sIGFzIGEKR0VORVJBVE9SLCBzbyB0aGUgZXhwb3J0IGNhbm5vdCBmYWxs'
        'IGJlaGluZCB0aGUgc3RvcmUgd2l0aG91dCBhIGNoZWNrZXIKc2F5aW5nIHNvIChMLTMy'
        'MiBydWxpbmcgNykuIFJ1bm5pbmcgaXQgYnkgaGFuZCBpcyB0aGUgc2FtZSB0aGluZy4K'
        'CldIQVQgSVQgV1JJVEVTCi0tLS0tLS0tLS0tLS0tCk9uZSBKU09OIGZpbGUsIGRhdGEv'
        'Y29uc3RhbnRzX2V4cG9ydC5qc29uOgoKICAgIHN0b3JlX3NoYTI1NiAgIHRoZSBzaGEy'
        'NTYgb2YgY29uc3RhbnRzX25ldy5weSwgQ1JMRiBub3JtYWxpc2VkIHRvIExGLAogICAg'
        'ICAgICAgICAgICAgICAgc28gdGVzdF9jb25zdGFudHNfZXhwb3J0LnB5IGNhbiB0ZWxs'
        'IHdoZXRoZXIgdGhlIHN0b3JlCiAgICAgICAgICAgICAgICAgICBtb3ZlZCBhZnRlciB0'
        'aGUgZXhwb3J0IHdhcyBtYWRlCiAgICB0b2tlbnMgICAgICAgICBjb25zdGFudHNfdG9r'
        'ZW5zLlRPS0VOUywgdmVyYmF0aW06IHdoYXQgZWFjaCB1bml0CiAgICAgICAgICAgICAg'
        'ICAgICB0b2tlbiBtZWFucwogICAgY2xvc2VkX3NsaWNlcyAgdGhlIHNsaWNlcyB3aG9z'
        'ZSB3YWxrIGlzIGZpbmlzaGVkLCBmcm9tCiAgICAgICAgICAgICAgICAgICBjb25zdGFu'
        'dHNfcm93cy5DTE9TRURfU0xJQ0VTLiBUaGUgZ2FsbGVyeSdzIHBvaW50ZXIKICAgICAg'
        'ICAgICAgICAgICAgIGpvaW4gbmVlZHMgdGhlbSB0byBrbm93IHdoZW4gYSByb3cgdGhh'
        'dCBpcyBub3QKICAgICAgICAgICAgICAgICAgIGV4cG9ydGVkIGlzIGEgZmFpbHVyZSBy'
        'YXRoZXIgdGhhbiBhIG5hbWVkIGdhcCwgYW5kCiAgICAgICAgICAgICAgICAgICB0aGUg'
        'c3RvcmUncyBvd24gbGlzdCBpcyB0aGUgb25seSBob25lc3Qgc291cmNlCiAgICB0cmFu'
        'c2l0aW9uYWwgICB0aGUgcm93cyBzdG9yZWQgYXMgcm91bmRlZCBsaXRlcmFscyB1bnRp'
        'bCB0aGUKICAgICAgICAgICAgICAgICAgIGdhbGxlcnkgc3RvcHMgcGFyc2luZyB0aGUg'
        'c3RvcmUsIGZyb20KICAgICAgICAgICAgICAgICAgIGNvbnN0YW50c19yb3dzLlRSQU5T'
        'SVRJT05BTAogICAgcm93cyAgICAgICAgICAgb25lIGVudHJ5IHBlciBleHBvcnRlZCBy'
        'b3csIGluIHN0b3JlIG9yZGVyOgogICAgICAgICAgICAgICAgICAgICB2YWx1ZSAgICB0'
        'aGUgbnVtYmVyLCByb3VuZGVkIHRvIGl0cyBkZWNsYXJlZCBmaWd1cmVzCiAgICAgICAg'
        'ICAgICAgICAgICAgIHVuaXQgICAgIHRoZSB0b2tlbiBmcm9tIHRoZSByb3cncyAiIyBV'
        'bml0OiIgbGluZQogICAgICAgICAgICAgICAgICAgICBmaWd1cmVzICB0aGUgY291bnQg'
        'ZnJvbSAiIyBGaWd1cmVzOiIsICJleGFjdCIsIG9yCiAgICAgICAgICAgICAgICAgICAg'
        'ICAgICAgICAgIG51bGwgd2hlbiB0aGUgcm93IGhhcyBubyBzdWNoIGxpbmUgeWV0CiAg'
        'ICAgICAgICAgICAgICAgICAgIHN0YXR1cyAgIHRoZSAiIyBTdGF0dXM6IiB0ZXh0LCBv'
        'ciBudWxsCiAgICAgICAgICAgICAgICAgICAgIGRlcml2ZWQgIHRydWUgd2hlbiB0aGUg'
        'cm93IGlzIGNvbXB1dGVkIGZyb20gb3RoZXJzCiAgICBub3RfZXhwb3J0ZWQgICBldmVy'
        'eSByb3cgdGhhdCBpcyBOT1QgaW4gcm93cywgYnkgbmFtZSwgd2l0aCB0aGUgcmVhc29u'
        'CgpST1VORElORyBIQVBQRU5TIEhFUkUsIEFORCBPTkxZIEhFUkUKLS0tLS0tLS0tLS0t'
        'LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tClRoZSBzdG9yZSBob2xkcyBmdWxsIHByZWNp'
        'c2lvbjsgdGhlIGV4cG9ydCBpcyB0aGUgcmVwb3J0aW5nIHN0ZXAKKHByb3ZlbmFuY2Ut'
        'ZGlzY2lwbGluZSAyLjEzLCBSdWxlIDYpLiBBIHJvdyBkZWNsYXJpbmcgIiMgRmlndXJl'
        'czogNSIgaXMKZXhwb3J0ZWQgYXQgZml2ZSBzaWduaWZpY2FudCBmaWd1cmVzLCByb3Vu'
        'ZGVkIGhhbGYgdG8gZXZlbiB3aXRoCmZsb2F0KCIlLipnIiAlICg1LCB4KSkgKFJ1bGUg'
        'NSkuIEEgcm93IGRlY2xhcmluZyAiZXhhY3QiIGlzIGV4cG9ydGVkCnVucm91bmRlZC4g'
        'QSByb3cgd2l0aCBubyAiIyBGaWd1cmVzOiIgbGluZSB5ZXQgaXMgZXhwb3J0ZWQgdW5y'
        'b3VuZGVkCndpdGggImZpZ3VyZXMiOiBudWxsLCBzbyBhIGNvbnN1bWVyIGNhbiB0ZWxs'
        'IGEgZGVjbGFyZWQgY291bnQgZnJvbSBhCm1pc3Npbmcgb25lLiBOb3RoaW5nIGluIGNv'
        'bnN0YW50c19uZXcucHkgaXMgY2hhbmdlZC4KCldIQVQgSVMgTk9UIEVYUE9SVEVELCBB'
        'TkQgV0hZIElUIElTIE5BTUVECi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t'
        'LS0tLS0tLS0tCkEgcm93IHdpdGggbm8gIiMgVW5pdDoiIGxpbmUgaXMgbm90IGV4cG9y'
        'dGVkOiB0aGUgZ2FsbGVyeSBjYW5ub3Qgam9pbiB0bwphIHJvdyB0aGF0IGhhcyBub3Qg'
        'YmVlbiBtaWdyYXRlZCwgYW5kIGEgbnVtYmVyIHdpdGggbm8gdW5pdCBpcyBub3QKc2Vy'
        'dmVkLiBJdCBnb2VzIGluIG5vdF9leHBvcnRlZCB3aXRoIGl0cyByZWFzb24uIFNvIGRv'
        'ZXMgYSByb3cgd2hvc2UKdG9rZW4gaXMgUkVUSVJFRCAodG9kYXksICJkaW1lbnNpb25s'
        'ZXNzIjsgc2VlIGNvbnN0YW50c190b2tlbnMucHkpLiBUaGUKbGlzdCBzaHJpbmtzIGFz'
        'IGVhY2ggYm9keSdzIHNsaWNlIGlzIHdhbGtlZC4KCldIQVQgTUFLRVMgSVQgRkFJTCAo'
        'ZXhpdCAxLCBhbmQgTk9USElORyBpcyB3cml0dGVuKQotLS0tLS0tLS0tLS0tLS0tLS0t'
        'LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KICAgIC0gYSAiIyBVbml0OiIg'
        'dG9rZW4gdGhhdCBpcyBuZWl0aGVyIGRlZmluZWQgbm9yIHJldGlyZWQKICAgIC0gYSAi'
        'IyBVbml0OiIgb3IgIiMgRmlndXJlczoiIGxpbmUgdGhhdCBjYW5ub3QgYmUgcmVhZAog'
        'ICAgLSBhIHRva2VuIHdob3NlIGRlZmluaW5nX2NvbnN0YW50IGlzIG5vdCBhIHJvdyBp'
        'biB0aGUgc3RvcmUKICAgIC0gYW4gZXhwb3J0ZWQgdmFsdWUgdGhhdCBpcyBub3QgYSBu'
        'dW1iZXIsIGEgbGlzdCBvciBkaWN0IG9mCiAgICAgIG51bWJlcnMsIG9yIG51bGwKICAg'
        'IC0gY29uc3RhbnRzX25ldy5weSBkb2VzIG5vdCBwYXJzZSBvciBkb2VzIG5vdCBydW4K'
        'CkRFVEVSTUlOSVNUSUMgT04gUFVSUE9TRQotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0K'
        'VGhlIHNhbWUgc3RvcmUgYnl0ZXMgZ2l2ZSB0aGUgc2FtZSBleHBvcnQgYnl0ZXMuIFRo'
        'ZXJlIGlzIG5vIHRpbWVzdGFtcAphbmQgbm8gZ2l0IFNIQSBpbnNpZGUgdGhlIGZpbGUu'
        'IEEgZmlsZSBjYW5ub3QgbmFtZSB0aGUgY29tbWl0IHRoYXQKY29udGFpbnMgaXQsIGFu'
        'ZCBpbiB0aGUgbm9ybWFsIGxvb3AgdGhlIGV4cG9ydCBpcyBtYWRlIHdoaWxlIHRoZSB3'
        'b3JraW5nCmNvcHkgaGFzIHVuY29tbWl0dGVkIGVkaXRzLCBzbyBhIHJlY29yZGVkIEhF'
        'QUQgd291bGQgbmFtZSB0aGUgd3JvbmcKY29tbWl0IGV2ZXJ5IHRpbWUuIEEgdGltZXN0'
        'YW1wIHdvdWxkIHJld3JpdGUgdGhlIGZpbGUgb24gZXZlcnkgcnVuIGFuZApwdXQgYSBk'
        'aWZmIGluIGV2ZXJ5IGNvbW1pdC4gVGhlIGNvbnRlbnQgYW5jaG9yIGlzIHN0b3JlX3No'
        'YTI1NjsgdGhlCmNvbW1pdCBhbmNob3IgaXMgcmVjb3JkZWQgYnkgdGhlIGdhbGxlcnkg'
        'd2hlbiBpdCBwdWxscyB0aGlzIGZpbGUgYXQgYQpTSEEgaXQgbmFtZXMuIChCdWlsZCBt'
        'YW5pZmVzdCBjb3JyZWN0aW9uLCByZWNvcmRlZDogdGhlIG1hbmlmZXN0J3MKc2tldGNo'
        'IGNhcnJpZWQgImdlbmVyYXRlZCIgYW5kICJvcnJlcnlfc2hhIiBmaWVsZHMuKQoKVGhl'
        'IGZpbGUgaXMgb25seSB3cml0dGVuIHdoZW4gaXRzIGNvbnRlbnQgd291bGQgY2hhbmdl'
        'LCBhbmQgYWx3YXlzCndpdGggTEYgbGluZSBlbmRpbmdzLgoKUm9sZTogZGV2dG9vbApE'
        'b21haW46IGRldl90b29scwoKTW9kdWxlIGNyZWF0ZWQ6IFNlcHRlbWJlciAxNiwgMjAy'
        'NiB3aXRoIEFudGhyb3BpYydzIENsYXVkZSBPcHVzIDUKKEwtMzIyLCB0aGUgbWVjaGFu'
        'aXNtOiBwaWVjZSAyIG9mIHRoZSBidWlsZCBtYW5pZmVzdCwgdGhlIHNpeHRoCmdlbmVy'
        'YXRvcikuCk1vZHVsZSB1cGRhdGVkOiBTZXB0ZW1iZXIgMTcsIDIwMjYgd2l0aCBBbnRo'
        'cm9waWMncyBDbGF1ZGUgT3B1cyA1CihMLTMyMiwgdGhlIGdhbGxlcnkgaGFsZjogcGll'
        'Y2UgMCBvZgpkb2N1bWVudGF0aW9uL0JVSUxEX01BTklGRVNUX0wzMjJfZ2FsbGVyeV9o'
        'YWxmXzIwMjYwOTE3Lm1kLiBUaGUgZXhwb3J0CmNhcnJpZXMgY2xvc2VkX3NsaWNlcyBh'
        'bmQgdHJhbnNpdGlvbmFsLCBzbyB0aGUgZ2FsbGVyeSByZWFkcyBib3RoIGZyb20KdGhl'
        'IHN0b3JlIHJhdGhlciB0aGFuIGtlZXBpbmcgaXRzIG93biBjb3B5LiBTQ0hFTUEgbW92'
        'ZXMgdG8gMi4pCiIiIgoKaW1wb3J0IGpzb24KaW1wb3J0IG1hdGgKaW1wb3J0IG9zCmlt'
        'cG9ydCBzeXMKCmltcG9ydCBjb25zdGFudHNfcm93cwpmcm9tIGNvbnN0YW50c190b2tl'
        'bnMgaW1wb3J0IFJFVElSRURfVE9LRU5TLCBUT0tFTlMKCkVYUE9SVF9QQVRIID0gb3Mu'
        'cGF0aC5qb2luKCJkYXRhIiwgImNvbnN0YW50c19leHBvcnQuanNvbiIpClNDSEVNQSA9'
        'IDIKCgpkZWYgcm91bmRfdG8odmFsdWUsIGZpZ3VyZXMpOgogICAgIiIiUnVsZSA1OiBy'
        'b3VuZCBoYWxmIHRvIGV2ZW4gdG8gYGZpZ3VyZXNgIHNpZ25pZmljYW50IGZpZ3VyZXMu'
        'IiIiCiAgICByZXR1cm4gZmxvYXQoIiUuKmciICUgKGZpZ3VyZXMsIHZhbHVlKSkKCgpk'
        'ZWYgX2V4cG9ydF92YWx1ZSh2YWx1ZSwgZmlndXJlcywgd2hlcmUpOgogICAgIiIiKGV4'
        'cG9ydGFibGUgdmFsdWUsIHByb2JsZW0gb3IgTm9uZSkuIiIiCiAgICBpZiB2YWx1ZSBp'
        'cyBOb25lOgogICAgICAgIHJldHVybiBOb25lLCBOb25lCiAgICBpZiBpc2luc3RhbmNl'
        'KHZhbHVlLCBib29sKToKICAgICAgICByZXR1cm4gTm9uZSwgIiVzIGlzIGEgYm9vbGVh'
        'biwgbm90IGEgbnVtYmVyIiAlIHdoZXJlCiAgICBpZiBpc2luc3RhbmNlKHZhbHVlLCAo'
        'aW50LCBmbG9hdCkpOgogICAgICAgIG51bWJlciA9IGZsb2F0KHZhbHVlKQogICAgICAg'
        'IGlmIG1hdGguaXNuYW4obnVtYmVyKSBvciBtYXRoLmlzaW5mKG51bWJlcik6CiAgICAg'
        'ICAgICAgIHJldHVybiBOb25lLCAiJXMgaXMgbm90IGEgZmluaXRlIG51bWJlciIgJSB3'
        'aGVyZQogICAgICAgIGlmIGlzaW5zdGFuY2UoZmlndXJlcywgaW50KToKICAgICAgICAg'
        'ICAgcmV0dXJuIHJvdW5kX3RvKG51bWJlciwgZmlndXJlcyksIE5vbmUKICAgICAgICBy'
        'ZXR1cm4gbnVtYmVyLCBOb25lCiAgICBpZiBpc2luc3RhbmNlKHZhbHVlLCAobGlzdCwg'
        'dHVwbGUpKToKICAgICAgICBvdXQgPSBbXQogICAgICAgIGZvciBpbmRleCwgaXRlbSBp'
        'biBlbnVtZXJhdGUodmFsdWUpOgogICAgICAgICAgICBnb3QsIHByb2JsZW0gPSBfZXhw'
        'b3J0X3ZhbHVlKGl0ZW0sIGZpZ3VyZXMsCiAgICAgICAgICAgICAgICAgICAgICAgICAg'
        'ICAgICAgICAgICAgICAgIiVzWyVkXSIgJSAod2hlcmUsIGluZGV4KSkKICAgICAgICAg'
        'ICAgaWYgcHJvYmxlbToKICAgICAgICAgICAgICAgIHJldHVybiBOb25lLCBwcm9ibGVt'
        'CiAgICAgICAgICAgIG91dC5hcHBlbmQoZ290KQogICAgICAgIHJldHVybiBvdXQsIE5v'
        'bmUKICAgIGlmIGlzaW5zdGFuY2UodmFsdWUsIGRpY3QpOgogICAgICAgIG91dCA9IHt9'
        'CiAgICAgICAgZm9yIGtleSwgaXRlbSBpbiB2YWx1ZS5pdGVtcygpOgogICAgICAgICAg'
        'ICBnb3QsIHByb2JsZW0gPSBfZXhwb3J0X3ZhbHVlKGl0ZW0sIGZpZ3VyZXMsCiAgICAg'
        'ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIiVzWyVyXSIgJSAod2hl'
        'cmUsIGtleSkpCiAgICAgICAgICAgIGlmIHByb2JsZW06CiAgICAgICAgICAgICAgICBy'
        'ZXR1cm4gTm9uZSwgcHJvYmxlbQogICAgICAgICAgICBvdXRbc3RyKGtleSldID0gZ290'
        'CiAgICAgICAgcmV0dXJuIG91dCwgTm9uZQogICAgcmV0dXJuIE5vbmUsICIlcyBpcyBh'
        'ICVzLCBub3QgYSBudW1iZXIiICUgKHdoZXJlLCB0eXBlKHZhbHVlKS5fX25hbWVfXykK'
        'CgpkZWYgYnVpbGRfZXhwb3J0KHByb2plY3RfZGlyLCB0b2tlbnM9Tm9uZSwgcmV0aXJl'
        'ZD1Ob25lKToKICAgICIiIkJ1aWxkIHRoZSBleHBvcnQgaW4gbWVtb3J5LgoKICAgIFJl'
        'dHVybnMgKGV4cG9ydCwgZmFpbHVyZXMpLiBgZXhwb3J0YCBpcyBOb25lIHdoZW4gdGhl'
        'cmUgYXJlIGZhaWx1cmVzLgogICAgdGVzdF9jb25zdGFudHNfZXhwb3J0LnB5IGNhbGxz'
        'IHRoaXMgdG9vLCB0byByZS1yZWFkIHRoZSBzdG9yZSBhbmQKICAgIGNvbXBhcmUgYWdh'
        'aW5zdCB0aGUgZmlsZSBvbiBkaXNrLgogICAgIiIiCiAgICB0b2tlbnMgPSBUT0tFTlMg'
        'aWYgdG9rZW5zIGlzIE5vbmUgZWxzZSB0b2tlbnMKICAgIHJldGlyZWQgPSBSRVRJUkVE'
        'X1RPS0VOUyBpZiByZXRpcmVkIGlzIE5vbmUgZWxzZSByZXRpcmVkCiAgICBmYWlsdXJl'
        'cyA9IFtdCgogICAgcGF0aCA9IGNvbnN0YW50c19yb3dzLnN0b3JlX3BhdGgocHJvamVj'
        'dF9kaXIpCiAgICBpZiBub3Qgb3MucGF0aC5leGlzdHMocGF0aCk6CiAgICAgICAgcmV0'
        'dXJuIE5vbmUsIFsoIihzdG9yZSkiLCAiJXMgbm90IGZvdW5kIGJlc2lkZSB0aGlzIHNj'
        'cmlwdCIKICAgICAgICAgICAgICAgICAgICAgICAlIGNvbnN0YW50c19yb3dzLlNUT1JF'
        'KV0KICAgIHRyeToKICAgICAgICBfdGV4dCwgcm93cywgYnlfbmFtZSA9IGNvbnN0YW50'
        'c19yb3dzLnJlYWRfc3RvcmUocHJvamVjdF9kaXIpCiAgICBleGNlcHQgU3ludGF4RXJy'
        'b3IgYXMgZXhjOgogICAgICAgIHJldHVybiBOb25lLCBbKCIoc3RvcmUpIiwgIiVzIGRv'
        'ZXMgbm90IHBhcnNlOiAlcyIKICAgICAgICAgICAgICAgICAgICAgICAlIChjb25zdGFu'
        'dHNfcm93cy5TVE9SRSwgZXhjKSldCiAgICB0cnk6CiAgICAgICAgdmFsdWVzID0gY29u'
        'c3RhbnRzX3Jvd3MubG9hZF92YWx1ZXMocHJvamVjdF9kaXIpCiAgICBleGNlcHQgRXhj'
        'ZXB0aW9uIGFzIGV4YzogICAgICAgICAgICAgICAgICAgICAgICAgICMgbm9xYTogQkxF'
        'MDAxCiAgICAgICAgcmV0dXJuIE5vbmUsIFsoIihzdG9yZSkiLCAiJXMgZG9lcyBub3Qg'
        'cnVuOiAlcyIKICAgICAgICAgICAgICAgICAgICAgICAlIChjb25zdGFudHNfcm93cy5T'
        'VE9SRSwgZXhjKSldCgogICAgZm9yIHRva2VuLCBzcGVjIGluIHRva2Vucy5pdGVtcygp'
        'OgogICAgICAgIGRlZmluaW5nID0gc3BlYy5nZXQoImRlZmluaW5nX2NvbnN0YW50IikK'
        'ICAgICAgICBpZiBkZWZpbmluZyBpcyBub3QgTm9uZSBhbmQgZGVmaW5pbmcgbm90IGlu'
        'IGJ5X25hbWU6CiAgICAgICAgICAgIGZhaWx1cmVzLmFwcGVuZCgodG9rZW4sICJkZWZp'
        'bmluZ19jb25zdGFudCAlcyBpcyBub3QgYSByb3cgaW4gJXMiCiAgICAgICAgICAgICAg'
        'ICAgICAgICAgICAgICAgJSAoZGVmaW5pbmcsIGNvbnN0YW50c19yb3dzLlNUT1JFKSkp'
        'CgogICAgZXhwb3J0ZWQgPSB7fQogICAgbm90X2V4cG9ydGVkID0ge30KICAgIGZvciBy'
        'b3cgaW4gcm93czoKICAgICAgICBpZiByb3cudW5pdF9lcnJvcjoKICAgICAgICAgICAg'
        'ZmFpbHVyZXMuYXBwZW5kKChyb3cubmFtZSwgcm93LnVuaXRfZXJyb3IpKQogICAgICAg'
        'ICAgICBjb250aW51ZQogICAgICAgIGlmIHJvdy5maWd1cmVzX2Vycm9yOgogICAgICAg'
        'ICAgICBmYWlsdXJlcy5hcHBlbmQoKHJvdy5uYW1lLCByb3cuZmlndXJlc19lcnJvcikp'
        'CiAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgaWYgcm93LnVuaXQgaXMgTm9uZToK'
        'ICAgICAgICAgICAgbm90X2V4cG9ydGVkW3Jvdy5uYW1lXSA9ICJubyAjIFVuaXQ6IGxp'
        'bmUiCiAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgaWYgcm93LnVuaXQgaW4gcmV0'
        'aXJlZDoKICAgICAgICAgICAgbm90X2V4cG9ydGVkW3Jvdy5uYW1lXSA9ICgidW5pdCB0'
        'b2tlbiAnJXMnIGlzIHJldGlyZWQ6ICVzIgogICAgICAgICAgICAgICAgICAgICAgICAg'
        'ICAgICAgICAgICAgICUgKHJvdy51bml0LAogICAgICAgICAgICAgICAgICAgICAgICAg'
        'ICAgICAgICAgICAgICAgIHJldGlyZWRbcm93LnVuaXRdWyJyZWFzb24iXSkpCiAgICAg'
        'ICAgICAgIGNvbnRpbnVlCiAgICAgICAgaWYgcm93LnVuaXQgbm90IGluIHRva2VuczoK'
        'ICAgICAgICAgICAgZmFpbHVyZXMuYXBwZW5kKChyb3cubmFtZSwKICAgICAgICAgICAg'
        'ICAgICAgICAgICAgICAgICAidW5pdCB0b2tlbiAnJXMnIGlzIG5vdCBkZWZpbmVkIGlu'
        'ICIKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAiY29uc3RhbnRzX3Rva2Vucy5w'
        'eSAtLSBhZGQgaXQgdGhlcmUiCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJSBy'
        'b3cudW5pdCkpCiAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgdmFsdWUsIHByb2Js'
        'ZW0gPSBfZXhwb3J0X3ZhbHVlKHZhbHVlcy5nZXQocm93Lm5hbWUpLCByb3cuZmlndXJl'
        'cywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcm93Lm5hbWUp'
        'CiAgICAgICAgaWYgcHJvYmxlbToKICAgICAgICAgICAgZmFpbHVyZXMuYXBwZW5kKChy'
        'b3cubmFtZSwgcHJvYmxlbSkpCiAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgZXhw'
        'b3J0ZWRbcm93Lm5hbWVdID0gewogICAgICAgICAgICAidmFsdWUiOiB2YWx1ZSwKICAg'
        'ICAgICAgICAgInVuaXQiOiByb3cudW5pdCwKICAgICAgICAgICAgImZpZ3VyZXMiOiBy'
        'b3cuZmlndXJlcywKICAgICAgICAgICAgInN0YXR1cyI6IHJvdy5zdGF0dXMsCiAgICAg'
        'ICAgICAgICJkZXJpdmVkIjogcm93LmlzX2Rlcml2ZWQsCiAgICAgICAgfQoKICAgIGlm'
        'IGZhaWx1cmVzOgogICAgICAgIHJldHVybiBOb25lLCBmYWlsdXJlcwoKICAgIGV4cG9y'
        'dCA9IHsKICAgICAgICAiYWJvdXQiOiAoIkdlbmVyYXRlZCBieSBleHBvcnRfY29uc3Rh'
        'bnRzLnB5IGZyb20gY29uc3RhbnRzX25ldy5weSAiCiAgICAgICAgICAgICAgICAgICJp'
        'biB0aGUgcGFsb21hc19vcnJlcnkgcmVwb3NpdG9yeS4gRG8gbm90IGVkaXQgYnkgaGFu'
        'ZDsgIgogICAgICAgICAgICAgICAgICAidGhlIG5leHQgbWFpbnRlbmFuY2UgcnVuIHJl'
        'd3JpdGVzIGl0LiIpLAogICAgICAgICJzY2hlbWEiOiBTQ0hFTUEsCiAgICAgICAgInN0'
        'b3JlIjogY29uc3RhbnRzX3Jvd3MuU1RPUkUsCiAgICAgICAgInN0b3JlX3NoYTI1NiI6'
        'IGNvbnN0YW50c19yb3dzLnN0b3JlX3NoYTI1NihwYXRoKSwKICAgICAgICAic3RvcmVf'
        'aGFzaF9iYXNpcyI6ICgic2hhMjU2IG9mIGNvbnN0YW50c19uZXcucHkgd2l0aCBDUkxG'
        'IGxpbmUgIgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICJlbmRpbmdzIG5vcm1h'
        'bGlzZWQgdG8gTEYiKSwKICAgICAgICAicm91bmRpbmciOiAoInZhbHVlIGlzIHJvdW5k'
        'ZWQgaGFsZiB0byBldmVuIHRvIHRoZSByb3cncyBmaWd1cmVzOyAiCiAgICAgICAgICAg'
        'ICAgICAgICAgICJmaWd1cmVzICdleGFjdCcgb3IgbnVsbCBtZWFucyB0aGUgdmFsdWUg'
        'aXMgbm90ICIKICAgICAgICAgICAgICAgICAgICAgInJvdW5kZWQsIGFuZCBudWxsIG1l'
        'YW5zIHRoZSByb3cgaGFzIG5vdCBkZWNsYXJlZCBhICIKICAgICAgICAgICAgICAgICAg'
        'ICAgImNvdW50IHlldCIpLAogICAgICAgICJ0b2tlbnMiOiB0b2tlbnMsCiAgICAgICAg'
        'ImNsb3NlZF9zbGljZXMiOiBsaXN0KGNvbnN0YW50c19yb3dzLkNMT1NFRF9TTElDRVMp'
        'LAogICAgICAgICJ0cmFuc2l0aW9uYWwiOiBsaXN0KGNvbnN0YW50c19yb3dzLlRSQU5T'
        'SVRJT05BTCksCiAgICAgICAgInJvd3MiOiBleHBvcnRlZCwKICAgICAgICAibm90X2V4'
        'cG9ydGVkIjogbm90X2V4cG9ydGVkLAogICAgfQogICAgcmV0dXJuIGV4cG9ydCwgW10K'
        'CgpkZWYgcmVuZGVyKGV4cG9ydCk6CiAgICAiIiJUaGUgZXhhY3QgdGV4dCB3cml0dGVu'
        'IHRvIGRpc2suIiIiCiAgICByZXR1cm4ganNvbi5kdW1wcyhleHBvcnQsIGluZGVudD0y'
        'LCBlbnN1cmVfYXNjaWk9VHJ1ZSwKICAgICAgICAgICAgICAgICAgICAgIGFsbG93X25h'
        'bj1GYWxzZSkgKyAiXG4iCgoKZGVmIG1haW4oKToKICAgIHByb2plY3RfZGlyID0gb3Mu'
        'cGF0aC5kaXJuYW1lKG9zLnBhdGguYWJzcGF0aChfX2ZpbGVfXykpCiAgICBleHBvcnQs'
        'IGZhaWx1cmVzID0gYnVpbGRfZXhwb3J0KHByb2plY3RfZGlyKQoKICAgIHByaW50KCI9'
        'IiAqIDcwKQogICAgcHJpbnQoIiAgQ09OU1RBTlRTIEVYUE9SVCAtLSAlcyAtPiAlcyIK'
        'ICAgICAgICAgICUgKGNvbnN0YW50c19yb3dzLlNUT1JFLCBFWFBPUlRfUEFUSC5yZXBs'
        'YWNlKG9zLnNlcCwgIi8iKSkpCiAgICBwcmludCgiPSIgKiA3MCkKICAgIHByaW50KCIi'
        'KQoKICAgIGlmIGZhaWx1cmVzOgogICAgICAgIHByaW50KCJGQUlMVVJFUyAoJWQpIC0t'
        'IG5vdGhpbmcgd2FzIHdyaXR0ZW46IiAlIGxlbihmYWlsdXJlcykpCiAgICAgICAgZm9y'
        'IG5hbWUsIG1lc3NhZ2UgaW4gZmFpbHVyZXM6CiAgICAgICAgICAgIHByaW50KCIgICUt'
        'NDBzICVzIiAlIChuYW1lLCBtZXNzYWdlKSkKICAgICAgICBwcmludCgiIikKICAgICAg'
        'ICBwcmludCgiRXhwb3J0IE5PVCB3cml0dGVuOiAlZCBwcm9ibGVtKHMpIGluICVzIG9y'
        'ICIKICAgICAgICAgICAgICAiY29uc3RhbnRzX3Rva2Vucy5weS4iICUgKGxlbihmYWls'
        'dXJlcyksIGNvbnN0YW50c19yb3dzLlNUT1JFKSkKICAgICAgICByZXR1cm4gMQoKICAg'
        'IHRyeToKICAgICAgICB0ZXh0ID0gcmVuZGVyKGV4cG9ydCkKICAgIGV4Y2VwdCBWYWx1'
        'ZUVycm9yIGFzIGV4YzoKICAgICAgICBwcmludCgiRXhwb3J0IE5PVCB3cml0dGVuOiBh'
        'IHZhbHVlIGNvdWxkIG5vdCBiZSB3cml0dGVuIGFzICIKICAgICAgICAgICAgICAiSlNP'
        'TiAoJXMpLiIgJSBleGMpCiAgICAgICAgcmV0dXJuIDEKCiAgICB0YXJnZXQgPSBvcy5w'
        'YXRoLmpvaW4ocHJvamVjdF9kaXIsIEVYUE9SVF9QQVRIKQogICAgb2xkID0gTm9uZQog'
        'ICAgaWYgb3MucGF0aC5leGlzdHModGFyZ2V0KToKICAgICAgICB3aXRoIG9wZW4odGFy'
        'Z2V0LCAicmIiKSBhcyBoYW5kbGU6CiAgICAgICAgICAgIG9sZCA9IGhhbmRsZS5yZWFk'
        'KCkucmVwbGFjZShiIlxyXG4iLCBiIlxuIikuZGVjb2RlKCJ1dGYtOCIpCiAgICBpZiBv'
        'bGQgPT0gdGV4dDoKICAgICAgICBhY3Rpb24gPSAidW5jaGFuZ2VkLCBub3Qgd3JpdHRl'
        'biIKICAgIGVsc2U6CiAgICAgICAgb3MubWFrZWRpcnMob3MucGF0aC5kaXJuYW1lKHRh'
        'cmdldCksIGV4aXN0X29rPVRydWUpCiAgICAgICAgd2l0aCBvcGVuKHRhcmdldCwgInci'
        'LCBlbmNvZGluZz0idXRmLTgiLCBuZXdsaW5lPSIiKSBhcyBoYW5kbGU6CiAgICAgICAg'
        'ICAgIGhhbmRsZS53cml0ZSh0ZXh0KQogICAgICAgIGFjdGlvbiA9ICJ3cml0dGVuIiBp'
        'ZiBvbGQgaXMgbm90IE5vbmUgZWxzZSAiY3JlYXRlZCIKCiAgICByb3dzID0gZXhwb3J0'
        'WyJyb3dzIl0KICAgIHNraXBwZWQgPSBleHBvcnRbIm5vdF9leHBvcnRlZCJdCiAgICBu'
        'b191bml0ID0gW24gZm9yIG4sIHdoeSBpbiBza2lwcGVkLml0ZW1zKCkgaWYgd2h5ID09'
        'ICJubyAjIFVuaXQ6IGxpbmUiXQogICAgcmV0aXJlZCA9IFtuIGZvciBuIGluIHNraXBw'
        'ZWQgaWYgbiBub3QgaW4gbm9fdW5pdF0KICAgIGNvdW50ZWQgPSB7fQogICAgZm9yIG5h'
        'bWUgaW4gcm93czoKICAgICAgICBmaWd1cmVzID0gcm93c1tuYW1lXVsiZmlndXJlcyJd'
        'CiAgICAgICAga2V5ID0gKCJubyAjIEZpZ3VyZXM6IGxpbmUiIGlmIGZpZ3VyZXMgaXMg'
        'Tm9uZSBlbHNlCiAgICAgICAgICAgICAgICJleGFjdCIgaWYgZmlndXJlcyA9PSAiZXhh'
        'Y3QiIGVsc2UgInJvdW5kZWQgdG8gaXRzIGZpZ3VyZXMiKQogICAgICAgIGNvdW50ZWRb'
        'a2V5XSA9IGNvdW50ZWQuZ2V0KGtleSwgMCkgKyAxCgogICAgcHJpbnQoIkV4cG9ydGVk'
        'ICVkIHJvdyhzKToiICUgbGVuKHJvd3MpKQogICAgZm9yIGtleSBpbiAoInJvdW5kZWQg'
        'dG8gaXRzIGZpZ3VyZXMiLCAiZXhhY3QiLCAibm8gIyBGaWd1cmVzOiBsaW5lIik6CiAg'
        'ICAgICAgaWYgY291bnRlZC5nZXQoa2V5KToKICAgICAgICAgICAgcHJpbnQoIiAgJS0y'
        'NnMgJWQiICUgKGtleSwgY291bnRlZFtrZXldKSkKICAgIGZvciBsaW5lIGluIGNvbnN0'
        'YW50c19yb3dzLndyYXBfbmFtZXMobGlzdChyb3dzKSk6CiAgICAgICAgcHJpbnQobGlu'
        'ZSkKICAgIHByaW50KCIiKQogICAgcHJpbnQoIk5vdCBleHBvcnRlZCwgJWQgcm93KHMp'
        'OiIgJSBsZW4oc2tpcHBlZCkpCiAgICBpZiByZXRpcmVkOgogICAgICAgIHByaW50KCIg'
        'IHJldGlyZWQgdW5pdCB0b2tlbiAoJWQpIC0tIHJlcGxhY2VkIGF0IHRoZSBzbGljZSB2'
        'aXNpdDoiCiAgICAgICAgICAgICAgJSBsZW4ocmV0aXJlZCkpCiAgICAgICAgZm9yIGxp'
        'bmUgaW4gY29uc3RhbnRzX3Jvd3Mud3JhcF9uYW1lcyhyZXRpcmVkKToKICAgICAgICAg'
        'ICAgcHJpbnQobGluZSkKICAgIGlmIG5vX3VuaXQ6CiAgICAgICAgYnlfc2xpY2UgPSB7'
        'fQogICAgICAgIGZvciBuYW1lIGluIG5vX3VuaXQ6CiAgICAgICAgICAgIGJ5X3NsaWNl'
        'LnNldGRlZmF1bHQoY29uc3RhbnRzX3Jvd3Muc2xpY2Vfb2YobmFtZSksIFtdKS5hcHBl'
        'bmQoCiAgICAgICAgICAgICAgICBuYW1lKQogICAgICAgIHByaW50KCIgIG5vICMgVW5p'
        'dDogbGluZSAoJWQpLCBieSBzbGljZToiICUgbGVuKG5vX3VuaXQpKQogICAgICAgIGZv'
        'ciBrZXkgaW4gc29ydGVkKGJ5X3NsaWNlKToKICAgICAgICAgICAgcHJpbnQoIiAgICAl'
        'cyAoJWQpIiAlIChrZXksIGxlbihieV9zbGljZVtrZXldKSkpCiAgICAgICAgICAgIGZv'
        'ciBsaW5lIGluIGNvbnN0YW50c19yb3dzLndyYXBfbmFtZXMoYnlfc2xpY2Vba2V5XSwK'
        'ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBp'
        'bmRlbnQ9IiAgICAgICAgIik6CiAgICAgICAgICAgICAgICBwcmludChsaW5lKQogICAg'
        'cHJpbnQoIiIpCiAgICBwcmludCgiU3RvcmUgc2hhMjU2ICVzOyAlZCB0b2tlbihzKSBj'
        'YXJyaWVkLiIKICAgICAgICAgICUgKGV4cG9ydFsic3RvcmVfc2hhMjU2Il0sIGxlbihl'
        'eHBvcnRbInRva2VucyJdKSkpCiAgICBwcmludCgiRXhwb3J0ICVzOiAlZCBvZiAlZCBy'
        'b3dzIGV4cG9ydGVkLCAlZCBub3QgZXhwb3J0ZWQuIgogICAgICAgICAgJSAoYWN0aW9u'
        'LCBsZW4ocm93cyksIGxlbihyb3dzKSArIGxlbihza2lwcGVkKSwgbGVuKHNraXBwZWQp'
        'KSkKICAgIHJldHVybiAwCgoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIHN5'
        'cy5leGl0KG1haW4oKSkK')),
    ('test_constants_export.py', '50e445ee0c744aa74b146eed6e40f2db2e012f179809cfcf50932b8d39432f70',
     (
        'IiIiCnRlc3RfY29uc3RhbnRzX2V4cG9ydC5weSAtLSBkYXRhL2NvbnN0YW50c19leHBv'
        'cnQuanNvbiBzYXlzIHdoYXQKY29uc3RhbnRzX25ldy5weSBob2xkcy4KCldIWSBUSElT'
        'IEVYSVNUUwoKICAgIFRoZSByb3VuZCB0cmlwIGZyb20gdGhlIHN0b3JlIHRvIHRoZSBn'
        'YWxsZXJ5IGlzIHR3byBob3BzLiBUaGUgZ2FsbGVyeQogICAgc2VydmVzIHdoYXQgdGhl'
        'IG9ycmVyeSBwdWJsaXNoZWQsIGFuZCB0aGUgb3JyZXJ5IHB1Ymxpc2hlZCB3aGF0IHRo'
        'ZQogICAgc3RvcmUgaG9sZHMuIFRoaXMgY2hlY2tlciBpcyB0aGUgc2Vjb25kIGhvcCwg'
        'dGhlIG9ycmVyeSdzIG93biAoTC0zMjIsCiAgICB0aGUgZnJhbWluZyBjb3JyZWN0aW9u'
        'IGZyb20gdGhlIEZhYmxlIHJldmlldyBvZiAyMDI2LTA5LTExKS4gVGhlCiAgICBtYWlu'
        'dGVuYW5jZSBydW5uZXIgcmVnZW5lcmF0ZXMgdGhlIGV4cG9ydCBiZWZvcmUgaXQgcnVu'
        'cyB0aGlzLCBidXQgYQogICAgcHVzaCB3aXRob3V0IGEgcnVuLCBvciBhIHJ1biB3aG9z'
        'ZSBnZW5lcmF0b3IgZmFpbGVkLCBjYW4gbGVhdmUgYQogICAgc3RhbGUgZXhwb3J0IHdp'
        'dGggbm90aGluZyBlbHNlIHNheWluZyBzby4KClJVTiBDT01NQU5ECgogICAgcHl0aG9u'
        'IGV4cG9ydF9jb25zdGFudHMucHkgICAgICAgICAod3JpdGVzIHRoZSBleHBvcnQpCiAg'
        'ICBweXRob24gdGVzdF9jb25zdGFudHNfZXhwb3J0LnB5ICAgIChjaGVja3MgaXQpCgog'
        'ICAgT3BlbiBlaXRoZXIgaW4gVlMgQ29kZSBhbmQgY2xpY2sgUnVuLiBvcnJlcnlfbWFp'
        'bnRlbmFuY2VfcnVuLnB5IHJ1bnMKICAgIGJvdGgsIHRoZSBnZW5lcmF0b3IgZmlyc3Qu'
        'CgpXSEFUIElUIENIRUNLUywgZWFjaCBwcmludGluZyB3aGF0IGl0IGNvbXBhcmVkCgog'
        'ICAgMS4gVGhlIGV4cG9ydCdzIHN0b3JlX3NoYTI1NiBlcXVhbHMgdGhlIHNoYTI1NiBv'
        'ZiBjb25zdGFudHNfbmV3LnB5IG9uCiAgICAgICBkaXNrLCBDUkxGIG5vcm1hbGlzZWQg'
        'dG8gTEYuIEJvdGggaGFzaGVzIGFyZSBwcmludGVkLgogICAgMi4gUmUtcmVhZGluZyB0'
        'aGUgc3RvcmUgbm93IGdpdmVzIHRoZSBzYW1lIHJvd3MgYXMgdGhlIGZpbGU6IHZhbHVl'
        'LAogICAgICAgdW5pdCwgZmlndXJlcywgc3RhdHVzIGFuZCBkZXJpdmVkLCBmb3IgZXZl'
        'cnkgcm93LiBUaGUgY291bnQKICAgICAgIGV4YW1pbmVkIGlzIHByaW50ZWQgYW5kIGV2'
        'ZXJ5IGRpc2FncmVlbWVudCBpcyBuYW1lZC4KICAgIDMuIG5vdF9leHBvcnRlZCBuYW1l'
        'cyBleGFjdGx5IHRoZSByb3dzIHRoYXQgYXJlIG5vdCBleHBvcnRlZCwgbm8gbW9yZQog'
        'ICAgICAgYW5kIG5vIGZld2VyLCB3aXRoIHRoZSBzYW1lIHJlYXNvbnMuIEV2ZXJ5IHJv'
        'dyBpbiB0aGUgc3RvcmUgaXMgaW4KICAgICAgIGV4YWN0bHkgb25lIG9mIHRoZSB0d28g'
        'bGlzdHMuCiAgICA0LiBFdmVyeSB0b2tlbidzIGRlZmluaW5nX2NvbnN0YW50IGlzIGEg'
        'cm93IGluIHRoZSBzdG9yZS4gV2hldGhlciB0aGF0CiAgICAgICByb3cgaXMgaXRzZWxm'
        'IGV4cG9ydGVkIHlldCBpcyBwcmludGVkIGJlc2lkZSBpdC4gVGhlIGV4cG9ydCdzCiAg'
        'ICAgICBjbG9zZWRfc2xpY2VzIGFuZCB0cmFuc2l0aW9uYWwgbGlzdHMgZXF1YWwgdGhl'
        'IHN0b3JlJ3Mgb3duLCBzbyB0aGUKICAgICAgIGdhbGxlcnkgY2Fubm90IHJlYWQgYSBz'
        'dGFsZSBjb3B5IG9mIGVpdGhlci4KICAgIDUuIFRoZSBwZXItc2xpY2UgZ2F0ZSAoVG9u'
        'eSdzIHJ1bGluZyBvZiAyMDI2LTA5LTE0KTogYSByb3cgaW5zaWRlIGEKICAgICAgIENM'
        'T1NFRCBzbGljZSBtdXN0IGJlIGV4cG9ydGVkIGFuZCBjYXJyeSBhIHN0YXR1cyBhbmQg'
        'YSBmaWd1cmUKICAgICAgIGNvdW50LiBPdXRzaWRlIGEgY2xvc2VkIHNsaWNlIGEgbWlz'
        'c2luZyBmaWVsZCBpcyBhIG5hbWVkIGdhcCwgbm90IGEKICAgICAgIGZhaWx1cmUuIGNv'
        'bnN0YW50c19yb3dzLkNMT1NFRF9TTElDRVMgaXMgZW1wdHkgdW50aWwgdGhlIEVhcnRo'
        'IHdhbGsKICAgICAgIGZpbmlzaGVzLCBhbmQgdGhlIG91dHB1dCBzYXlzIHNvLgoKV0hB'
        'VCBNQUtFUyBJVCBGQUlMCgogICAgQW55IG9mIHRoZSBmaXZlLiBBbHNvOiB0aGUgZXhw'
        'b3J0IGZpbGUgaXMgbWlzc2luZywgaXMgbm90IEpTT04sIGxhY2tzCiAgICBhIGZpZWxk'
        'LCBvciB0aGUgZ2VuZXJhdG9yIGl0c2VsZiByZXBvcnRzIGEgcHJvYmxlbSB3aXRoIHRo'
        'ZSBzdG9yZS4KCldIQVQgQSBHUkVFTiBSVU4gUFJPVkVTCgogICAgSXRzIGxhc3QgbGlu'
        'ZSBuYW1lcyB0aGUgaGFzaCBpdCBjb21wYXJlZCBvbiBib3RoIHNpZGVzIGFuZCB0aGUg'
        'bnVtYmVyCiAgICBvZiByb3dzIGl0IHJlLXJlYWQuIEEgY2hlY2sgdGhhdCBkaWQgbm90'
        'IHJ1biBjYW5ub3QgcHJpbnQgdGhhdCBsaW5lLgoKUm9sZTogZGV2dG9vbApEb21haW46'
        'IGRldl90b29scwoKTW9kdWxlIGNyZWF0ZWQ6IFNlcHRlbWJlciAxNiwgMjAyNiB3aXRo'
        'IEFudGhyb3BpYydzIENsYXVkZSBPcHVzIDUKKEwtMzIyLCB0aGUgbWVjaGFuaXNtOiBw'
        'aWVjZSAzIG9mIHRoZSBidWlsZCBtYW5pZmVzdCkuCk1vZHVsZSB1cGRhdGVkOiBTZXB0'
        'ZW1iZXIgMTcsIDIwMjYgd2l0aCBBbnRocm9waWMncyBDbGF1ZGUgT3B1cyA1CihMLTMy'
        'MiwgdGhlIGdhbGxlcnkgaGFsZjogcGllY2UgMC4gQ2hlY2sgNCBhbHNvIGNvbXBhcmVz'
        'IHRoZSBleHBvcnQncwpjbG9zZWRfc2xpY2VzIGFuZCB0cmFuc2l0aW9uYWwgYWdhaW5z'
        'dCBjb25zdGFudHNfcm93cy5weS4pCiIiIgoKaW1wb3J0IGpzb24KaW1wb3J0IG9zCmlt'
        'cG9ydCBzeXMKCmltcG9ydCBjb25zdGFudHNfcm93cwppbXBvcnQgZXhwb3J0X2NvbnN0'
        'YW50cwoKUkVRVUlSRUQgPSAoInNjaGVtYSIsICJzdG9yZSIsICJzdG9yZV9zaGEyNTYi'
        'LCAidG9rZW5zIiwgImNsb3NlZF9zbGljZXMiLAogICAgICAgICAgICAidHJhbnNpdGlv'
        'bmFsIiwgInJvd3MiLCAibm90X2V4cG9ydGVkIikKUk9XX0ZJRUxEUyA9ICgidmFsdWUi'
        'LCAidW5pdCIsICJmaWd1cmVzIiwgInN0YXR1cyIsICJkZXJpdmVkIikKCgpkZWYgY2hl'
        'Y2socHJvamVjdF9kaXIsIGNsb3NlZD1Ob25lKToKICAgICIiIlJldHVybiAoZmFpbHVy'
        'ZXMsIGZhY3RzKS4gRWFjaCBmYWlsdXJlIGlzIChuYW1lLCBtZXNzYWdlKS4iIiIKICAg'
        'IGZhaWx1cmVzID0gW10KICAgIGZhY3RzID0ge30KICAgIHRhcmdldCA9IG9zLnBhdGgu'
        'am9pbihwcm9qZWN0X2RpciwgZXhwb3J0X2NvbnN0YW50cy5FWFBPUlRfUEFUSCkKCiAg'
        'ICBpZiBub3Qgb3MucGF0aC5leGlzdHModGFyZ2V0KToKICAgICAgICByZXR1cm4gWygi'
        'KGV4cG9ydCkiLCAiJXMgZG9lcyBub3QgZXhpc3QgLS0gcnVuIGV4cG9ydF9jb25zdGFu'
        'dHMucHkiCiAgICAgICAgICAgICAgICAgJSBleHBvcnRfY29uc3RhbnRzLkVYUE9SVF9Q'
        'QVRIKV0sIGZhY3RzCiAgICB0cnk6CiAgICAgICAgd2l0aCBvcGVuKHRhcmdldCwgInIi'
        'LCBlbmNvZGluZz0idXRmLTgiKSBhcyBoYW5kbGU6CiAgICAgICAgICAgIG9uX2Rpc2sg'
        'PSBqc29uLmxvYWQoaGFuZGxlKQogICAgZXhjZXB0IFZhbHVlRXJyb3IgYXMgZXhjOgog'
        'ICAgICAgIHJldHVybiBbKCIoZXhwb3J0KSIsICJub3QgdmFsaWQgSlNPTjogJXMiICUg'
        'ZXhjKV0sIGZhY3RzCiAgICBtaXNzaW5nID0gW2tleSBmb3Iga2V5IGluIFJFUVVJUkVE'
        'IGlmIGtleSBub3QgaW4gb25fZGlza10KICAgIGlmIG1pc3Npbmc6CiAgICAgICAgcmV0'
        'dXJuIFsoIihleHBvcnQpIiwgIm1pc3NpbmcgZmllbGQocyk6ICVzIiAlICIsICIuam9p'
        'bihtaXNzaW5nKSldLCBcCiAgICAgICAgICAgIGZhY3RzCgogICAgZnJlc2gsIHByb2Js'
        'ZW1zID0gZXhwb3J0X2NvbnN0YW50cy5idWlsZF9leHBvcnQocHJvamVjdF9kaXIpCiAg'
        'ICBpZiBwcm9ibGVtczoKICAgICAgICBmb3IgbmFtZSwgbWVzc2FnZSBpbiBwcm9ibGVt'
        'czoKICAgICAgICAgICAgZmFpbHVyZXMuYXBwZW5kKChuYW1lLCAidGhlIGdlbmVyYXRv'
        'ciBjYW5ub3QgZXhwb3J0IHRoZSBzdG9yZTogIgogICAgICAgICAgICAgICAgICAgICAg'
        'ICAgICAgICsgbWVzc2FnZSkpCiAgICAgICAgcmV0dXJuIGZhaWx1cmVzLCBmYWN0cwoK'
        'ICAgICMgMS4gaGFzaAogICAgZmFjdHNbImhhc2hfZGlzayJdID0gb25fZGlza1sic3Rv'
        'cmVfc2hhMjU2Il0KICAgIGZhY3RzWyJoYXNoX3N0b3JlIl0gPSBmcmVzaFsic3RvcmVf'
        'c2hhMjU2Il0KICAgIGlmIG9uX2Rpc2tbInN0b3JlX3NoYTI1NiJdICE9IGZyZXNoWyJz'
        'dG9yZV9zaGEyNTYiXToKICAgICAgICBmYWlsdXJlcy5hcHBlbmQoKCIoZXhwb3J0KSIs'
        'CiAgICAgICAgICAgICAgICAgICAgICAgICAic3RhbGU6IGV4cG9ydGVkIGZyb20gc3Rv'
        'cmUgJXMsIHRoZSBzdG9yZSBvbiBkaXNrICIKICAgICAgICAgICAgICAgICAgICAgICAg'
        'ICJpcyAlcyAtLSBydW4gZXhwb3J0X2NvbnN0YW50cy5weSIKICAgICAgICAgICAgICAg'
        'ICAgICAgICAgICUgKG9uX2Rpc2tbInN0b3JlX3NoYTI1NiJdWzoxMl0sCiAgICAgICAg'
        'ICAgICAgICAgICAgICAgICAgICBmcmVzaFsic3RvcmVfc2hhMjU2Il1bOjEyXSkpKQoK'
        'ICAgICMgMi4gcm93cwogICAgZGlza19yb3dzID0gb25fZGlza1sicm93cyJdCiAgICBu'
        'ZXdfcm93cyA9IGZyZXNoWyJyb3dzIl0KICAgIGZhY3RzWyJyb3dzX2V4YW1pbmVkIl0g'
        'PSBsZW4oc2V0KGRpc2tfcm93cykgfCBzZXQobmV3X3Jvd3MpKQogICAgZm9yIG5hbWUg'
        'aW4gbmV3X3Jvd3M6CiAgICAgICAgaWYgbmFtZSBub3QgaW4gZGlza19yb3dzOgogICAg'
        'ICAgICAgICBmYWlsdXJlcy5hcHBlbmQoKG5hbWUsICJleHBvcnRlZCBmcm9tIHRoZSBz'
        'dG9yZSBub3csIGFic2VudCAiCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgImZy'
        'b20gdGhlIGZpbGUiKSkKICAgICAgICAgICAgY29udGludWUKICAgICAgICBmb3IgZmll'
        'bGQgaW4gUk9XX0ZJRUxEUzoKICAgICAgICAgICAgaWYgZGlza19yb3dzW25hbWVdLmdl'
        'dChmaWVsZCkgIT0gbmV3X3Jvd3NbbmFtZV1bZmllbGRdOgogICAgICAgICAgICAgICAg'
        'ZmFpbHVyZXMuYXBwZW5kKChuYW1lLCAiJXMgaXMgJXIgaW4gdGhlIGZpbGUsICVyIGlu'
        'IHRoZSAiCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICJzdG9yZSIgJSAo'
        'ZmllbGQsIGRpc2tfcm93c1tuYW1lXS5nZXQoZmllbGQpLAogICAgICAgICAgICAgICAg'
        'ICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5ld19yb3dzW25hbWVdW2ZpZWxkXSkp'
        'KQogICAgZm9yIG5hbWUgaW4gZGlza19yb3dzOgogICAgICAgIGlmIG5hbWUgbm90IGlu'
        'IG5ld19yb3dzOgogICAgICAgICAgICBmYWlsdXJlcy5hcHBlbmQoKG5hbWUsICJpbiB0'
        'aGUgZmlsZSdzIHJvd3MsIG5vdCBleHBvcnRlZCBmcm9tICIKICAgICAgICAgICAgICAg'
        'ICAgICAgICAgICAgICAidGhlIHN0b3JlIG5vdyIpKQoKICAgICMgMy4gbm90X2V4cG9y'
        'dGVkCiAgICBkaXNrX3NraXAgPSBvbl9kaXNrWyJub3RfZXhwb3J0ZWQiXQogICAgbmV3'
        'X3NraXAgPSBmcmVzaFsibm90X2V4cG9ydGVkIl0KICAgIGZhY3RzWyJub3RfZXhwb3J0'
        'ZWQiXSA9IGxlbihuZXdfc2tpcCkKICAgIGZvciBuYW1lLCB3aHkgaW4gbmV3X3NraXAu'
        'aXRlbXMoKToKICAgICAgICBpZiBkaXNrX3NraXAuZ2V0KG5hbWUpICE9IHdoeToKICAg'
        'ICAgICAgICAgZmFpbHVyZXMuYXBwZW5kKChuYW1lLCAibm90X2V4cG9ydGVkIHJlYXNv'
        'biBpcyAlciBpbiB0aGUgZmlsZSwgIgogICAgICAgICAgICAgICAgICAgICAgICAgICAg'
        'ICIlciBpbiB0aGUgc3RvcmUiICUgKGRpc2tfc2tpcC5nZXQobmFtZSksIHdoeSkpKQog'
        'ICAgZm9yIG5hbWUgaW4gZGlza19za2lwOgogICAgICAgIGlmIG5hbWUgbm90IGluIG5l'
        'd19za2lwOgogICAgICAgICAgICBmYWlsdXJlcy5hcHBlbmQoKG5hbWUsICJsaXN0ZWQg'
        'YXMgbm90IGV4cG9ydGVkIGluIHRoZSBmaWxlLCAiCiAgICAgICAgICAgICAgICAgICAg'
        'ICAgICAgICAgImJ1dCB0aGUgc3RvcmUgZXhwb3J0cyBpdCBvciBsYWNrcyBpdCIpKQog'
        'ICAgX3RleHQsIHJvd3MsIGJ5X25hbWUgPSBjb25zdGFudHNfcm93cy5yZWFkX3N0b3Jl'
        'KHByb2plY3RfZGlyKQogICAgZmFjdHNbInN0b3JlX3Jvd3MiXSA9IGxlbihyb3dzKQog'
        'ICAgZm9yIHJvdyBpbiByb3dzOgogICAgICAgIHBsYWNlZCA9IChyb3cubmFtZSBpbiBk'
        'aXNrX3Jvd3MpICsgKHJvdy5uYW1lIGluIGRpc2tfc2tpcCkKICAgICAgICBpZiBwbGFj'
        'ZWQgIT0gMToKICAgICAgICAgICAgZmFpbHVyZXMuYXBwZW5kKChyb3cubmFtZSwgImFw'
        'cGVhcnMgaW4gJWQgb2YgdGhlIGZpbGUncyB0d28gIgogICAgICAgICAgICAgICAgICAg'
        'ICAgICAgICAgICJsaXN0czsgaXQgc2hvdWxkIGJlIGluIGV4YWN0bHkgb25lIiAlIHBs'
        'YWNlZCkpCiAgICBmb3IgbmFtZSBpbiBsaXN0KGRpc2tfcm93cykgKyBsaXN0KGRpc2tf'
        'c2tpcCk6CiAgICAgICAgaWYgbmFtZSBub3QgaW4gYnlfbmFtZToKICAgICAgICAgICAg'
        'ZmFpbHVyZXMuYXBwZW5kKChuYW1lLCAibmFtZWQgaW4gdGhlIGZpbGUsIG5vdCBhIHJv'
        'dyBpbiAlcyIKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAlIGNvbnN0YW50c19y'
        'b3dzLlNUT1JFKSkKCiAgICAjIDQuIGRlZmluaW5nIGNvbnN0YW50cyBhbmQgdGhlIHR3'
        'byBsaXN0cyB0aGUgZ2FsbGVyeSByZWFkcwogICAgZm9yIGZpZWxkLCBhY3R1YWwgaW4g'
        'KCgiY2xvc2VkX3NsaWNlcyIsIGNvbnN0YW50c19yb3dzLkNMT1NFRF9TTElDRVMpLAog'
        'ICAgICAgICAgICAgICAgICAgICAgICAgICgidHJhbnNpdGlvbmFsIiwgY29uc3RhbnRz'
        'X3Jvd3MuVFJBTlNJVElPTkFMKSk6CiAgICAgICAgaWYgbGlzdChvbl9kaXNrLmdldChm'
        'aWVsZCwgW10pKSAhPSBsaXN0KGFjdHVhbCk6CiAgICAgICAgICAgIGZhaWx1cmVzLmFw'
        'cGVuZCgoZmllbGQsICJ0aGUgZXhwb3J0IHNheXMgJXI7IGNvbnN0YW50c19yb3dzLnB5'
        'ICIKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAic2F5cyAlciIgJSAob25fZGlz'
        'ay5nZXQoZmllbGQpLCBsaXN0KGFjdHVhbCkpKSkKICAgIGZhY3RzWyJsaXN0cyJdID0g'
        'KGxpc3QoY29uc3RhbnRzX3Jvd3MuQ0xPU0VEX1NMSUNFUyksCiAgICAgICAgICAgICAg'
        'ICAgICAgICBsaXN0KGNvbnN0YW50c19yb3dzLlRSQU5TSVRJT05BTCkpCiAgICBkZWZp'
        'bmluZyA9IFtdCiAgICBpZiBvbl9kaXNrWyJ0b2tlbnMiXSAhPSBmcmVzaFsidG9rZW5z'
        'Il06CiAgICAgICAgZmFpbHVyZXMuYXBwZW5kKCgiKHRva2VucykiLCAidGhlIGZpbGUn'
        'cyB0b2tlbiB0YWJsZSBkaWZmZXJzIGZyb20gIgogICAgICAgICAgICAgICAgICAgICAg'
        'ICAgImNvbnN0YW50c190b2tlbnMucHkiKSkKICAgIGZvciB0b2tlbiwgc3BlYyBpbiBz'
        'b3J0ZWQoZnJlc2hbInRva2VucyJdLml0ZW1zKCkpOgogICAgICAgIG5hbWUgPSBzcGVj'
        'LmdldCgiZGVmaW5pbmdfY29uc3RhbnQiKQogICAgICAgIGlmIG5hbWUgaXMgTm9uZToK'
        'ICAgICAgICAgICAgY29udGludWUKICAgICAgICBpZiBuYW1lIG5vdCBpbiBieV9uYW1l'
        'OgogICAgICAgICAgICBmYWlsdXJlcy5hcHBlbmQoKHRva2VuLCAiZGVmaW5pbmdfY29u'
        'c3RhbnQgJXMgaXMgbm90IGEgcm93IgogICAgICAgICAgICAgICAgICAgICAgICAgICAg'
        'ICUgbmFtZSkpCiAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgZGVmaW5pbmcuYXBw'
        'ZW5kKCh0b2tlbiwgbmFtZSwgbmFtZSBpbiBuZXdfcm93cykpCiAgICBmYWN0c1siZGVm'
        'aW5pbmciXSA9IGRlZmluaW5nCgogICAgIyA1LiBjbG9zZWQgc2xpY2VzCiAgICBjbG9z'
        'ZWQgPSBjb25zdGFudHNfcm93cy5DTE9TRURfU0xJQ0VTIGlmIGNsb3NlZCBpcyBOb25l'
        'IGVsc2UgY2xvc2VkCiAgICBmYWN0c1siY2xvc2VkIl0gPSBjbG9zZWQKICAgIGdhdGVk'
        'ID0gMAogICAgZm9yIHJvdyBpbiByb3dzOgogICAgICAgIGlmIG5vdCBjb25zdGFudHNf'
        'cm93cy5pbl9jbG9zZWRfc2xpY2Uocm93Lm5hbWUsIGNsb3NlZCk6CiAgICAgICAgICAg'
        'IGNvbnRpbnVlCiAgICAgICAgZ2F0ZWQgKz0gMQogICAgICAgIGlmIHJvdy5uYW1lIG5v'
        'dCBpbiBuZXdfcm93czoKICAgICAgICAgICAgZmFpbHVyZXMuYXBwZW5kKChyb3cubmFt'
        'ZSwgIkdBVEU6IGluIGNsb3NlZCBzbGljZSAlcyBhbmQgbm90ICIKICAgICAgICAgICAg'
        'ICAgICAgICAgICAgICAgICAiZXhwb3J0ZWQgKCVzKSIKICAgICAgICAgICAgICAgICAg'
        'ICAgICAgICAgICAlIChyb3cuc2xpY2UsIG5ld19za2lwLmdldChyb3cubmFtZSkpKSkK'
        'ICAgICAgICBpZiByb3cuc3RhdHVzIGlzIE5vbmU6CiAgICAgICAgICAgIGZhaWx1cmVz'
        'LmFwcGVuZCgocm93Lm5hbWUsICJHQVRFOiBpbiBjbG9zZWQgc2xpY2UgJXMgd2l0aCBu'
        'byAiCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIiMgU3RhdHVzOiBsaW5lIiAl'
        'IHJvdy5zbGljZSkpCiAgICAgICAgaWYgcm93LmZpZ3VyZXMgaXMgTm9uZToKICAgICAg'
        'ICAgICAgZmFpbHVyZXMuYXBwZW5kKChyb3cubmFtZSwgIkdBVEU6IGluIGNsb3NlZCBz'
        'bGljZSAlcyB3aXRoIG5vICIKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAiIyBG'
        'aWd1cmVzOiBsaW5lIiAlIHJvdy5zbGljZSkpCiAgICBmYWN0c1siZ2F0ZWQiXSA9IGdh'
        'dGVkCiAgICBmYWN0c1sidG9rZW5zIl0gPSBsZW4oZnJlc2hbInRva2VucyJdKQogICAg'
        'cmV0dXJuIGZhaWx1cmVzLCBmYWN0cwoKCmRlZiBtYWluKCk6CiAgICBwcm9qZWN0X2Rp'
        'ciA9IG9zLnBhdGguZGlybmFtZShvcy5wYXRoLmFic3BhdGgoX19maWxlX18pKQogICAg'
        'ZmFpbHVyZXMsIGZhY3RzID0gY2hlY2socHJvamVjdF9kaXIpCgogICAgcHJpbnQoIj0i'
        'ICogNzApCiAgICBwcmludCgiICBDT05TVEFOVFMgRVhQT1JUIENIRUNLIC0tICVzIGFn'
        'YWluc3QgJXMiCiAgICAgICAgICAlIChleHBvcnRfY29uc3RhbnRzLkVYUE9SVF9QQVRI'
        'LnJlcGxhY2Uob3Muc2VwLCAiLyIpLAogICAgICAgICAgICAgY29uc3RhbnRzX3Jvd3Mu'
        'U1RPUkUpKQogICAgcHJpbnQoIj0iICogNzApCiAgICBwcmludCgiIikKICAgIGlmICJo'
        'YXNoX2Rpc2siIGluIGZhY3RzOgogICAgICAgIHByaW50KCIxLiBzdG9yZSBzaGEyNTYg'
        'aW4gdGhlIGV4cG9ydCAgJXMiICUgZmFjdHNbImhhc2hfZGlzayJdKQogICAgICAgIHBy'
        'aW50KCIgICBzdG9yZSBzaGEyNTYgb24gZGlzayBub3cgICAgICVzIiAlIGZhY3RzWyJo'
        'YXNoX3N0b3JlIl0pCiAgICAgICAgcHJpbnQoIjIuIHJvd3MgcmUtcmVhZCBmcm9tIHRo'
        'ZSBzdG9yZSBhbmQgY29tcGFyZWQ6ICVkIgogICAgICAgICAgICAgICUgZmFjdHNbInJv'
        'd3NfZXhhbWluZWQiXSkKICAgICAgICBwcmludCgiMy4gcm93cyBub3QgZXhwb3J0ZWQ6'
        'ICVkOyBzdG9yZSByb3dzIHBsYWNlZDogJWQiCiAgICAgICAgICAgICAgJSAoZmFjdHNb'
        'Im5vdF9leHBvcnRlZCJdLCBmYWN0c1sic3RvcmVfcm93cyJdKSkKICAgICAgICBwcmlu'
        'dCgiNC4gY2xvc2VkIHNsaWNlcyAlcjsgdHJhbnNpdGlvbmFsICVyIgogICAgICAgICAg'
        'ICAgICUgKGZhY3RzWyJsaXN0cyJdWzBdLCBmYWN0c1sibGlzdHMiXVsxXSkpCiAgICAg'
        'ICAgcHJpbnQoIiAgIGRlZmluaW5nIGNvbnN0YW50czoiKQogICAgICAgIGZvciB0b2tl'
        'biwgbmFtZSwgZXhwb3J0ZWQgaW4gZmFjdHNbImRlZmluaW5nIl06CiAgICAgICAgICAg'
        'IHByaW50KCIgICAgICUtOHMgJS0yOHMgJXMiICUgKHRva2VuLCBuYW1lLAogICAgICAg'
        'ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICJleHBvcnRlZCIgaWYgZXhw'
        'b3J0ZWQgZWxzZQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg'
        'ICJhIHJvdywgbm90IGV4cG9ydGVkIHlldCIpKQogICAgICAgIGlmIGZhY3RzWyJjbG9z'
        'ZWQiXToKICAgICAgICAgICAgcHJpbnQoIjUuIGNsb3NlZCBzbGljZXM6ICVzOyAlZCBy'
        'b3cocykgZ2F0ZWQiCiAgICAgICAgICAgICAgICAgICUgKCIsICIuam9pbihmYWN0c1si'
        'Y2xvc2VkIl0pLCBmYWN0c1siZ2F0ZWQiXSkpCiAgICAgICAgZWxzZToKICAgICAgICAg'
        'ICAgcHJpbnQoIjUuIGNsb3NlZCBzbGljZXM6IG5vbmUgeWV0LCBzbyBubyByb3cgaXMg'
        'Z2F0ZWQ7IHRoZSAiCiAgICAgICAgICAgICAgICAgICJnYXBzIGFyZSBuYW1lZCBieSBl'
        'eHBvcnRfY29uc3RhbnRzLnB5IikKICAgICAgICBwcmludCgiIikKCiAgICBpZiBmYWls'
        'dXJlczoKICAgICAgICBwcmludCgiRkFJTFVSRVMgKCVkKToiICUgbGVuKGZhaWx1cmVz'
        'KSkKICAgICAgICBmb3IgbmFtZSwgbWVzc2FnZSBpbiBmYWlsdXJlczoKICAgICAgICAg'
        'ICAgcHJpbnQoIiAgJS00MHMgJXMiICUgKG5hbWUsIG1lc3NhZ2UpKQogICAgICAgIHBy'
        'aW50KCIiKQogICAgICAgIGdhdGUgPSBbZiBmb3IgZiBpbiBmYWlsdXJlcyBpZiBmWzFd'
        'LnN0YXJ0c3dpdGgoIkdBVEU6IildCiAgICAgICAgb3RoZXIgPSBsZW4oZmFpbHVyZXMp'
        'IC0gbGVuKGdhdGUpCiAgICAgICAgcGFydHMgPSBbXQogICAgICAgIGlmIG90aGVyOgog'
        'ICAgICAgICAgICBwYXJ0cy5hcHBlbmQoIiVkIHdoZXJlIHRoZSBleHBvcnQgZG9lcyBu'
        'b3QgbWF0Y2ggJXMiCiAgICAgICAgICAgICAgICAgICAgICAgICAlIChvdGhlciwgY29u'
        'c3RhbnRzX3Jvd3MuU1RPUkUpKQogICAgICAgIGlmIGdhdGU6CiAgICAgICAgICAgIHBh'
        'cnRzLmFwcGVuZCgiJWQgdW5maW5pc2hlZCBmaWVsZChzKSBvbiByb3dzIGluIGEgY2xv'
        'c2VkIHNsaWNlIgogICAgICAgICAgICAgICAgICAgICAgICAgJSBsZW4oZ2F0ZSkpCiAg'
        'ICAgICAgcHJpbnQoIiVkIHByb2JsZW0ocyk6ICVzLiIgJSAobGVuKGZhaWx1cmVzKSwg'
        'IjsgIi5qb2luKHBhcnRzKSkpCiAgICAgICAgcmV0dXJuIDEKCiAgICBwcmludCgiRXhw'
        'b3J0IG1hdGNoZXMgdGhlIHN0b3JlOiBzaGEyNTYgJXMgb24gYm90aCBzaWRlczsgJWQg'
        'cm93cyAiCiAgICAgICAgICAicmUtcmVhZCwgJWQgbm90IGV4cG9ydGVkLCAlZCB0b2tl'
        'bnMuIgogICAgICAgICAgJSAoZmFjdHNbImhhc2hfc3RvcmUiXVs6MTJdLCBmYWN0c1si'
        'cm93c19leGFtaW5lZCJdLAogICAgICAgICAgICAgZmFjdHNbIm5vdF9leHBvcnRlZCJd'
        'LCBmYWN0c1sidG9rZW5zIl0pKQogICAgcmV0dXJuIDAKCgppZiBfX25hbWVfXyA9PSAi'
        'X19tYWluX18iOgogICAgc3lzLmV4aXQobWFpbigpKQo=')),
]


LEDGER = "LEDGER_CONSOLIDATED.md"
ZONE = (b"<!-- INDEX:START", b"<!-- INDEX:END -->")


def lf(data):
    return data.replace(b"\r\n", b"\n")


def md5_content(data):
    return hashlib.md5(lf(data)).hexdigest()


def ledger_fingerprint(data):
    data = lf(data)
    start = data.index(ZONE[0])
    end = data.index(ZONE[1]) + len(ZONE[1])
    return hashlib.md5(data[:start] + data[end:]).hexdigest()


def decode(name, sha, chunks):
    data = base64.b64decode("".join(chunks))
    if hashlib.sha256(data).hexdigest() != sha:
        raise SystemExit("ERROR: the embedded copy of %s is damaged. "
                         "NOTHING was written." % name)
    return data


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)
    if not os.path.exists("constants_new.py"):
        raise SystemExit("ERROR: this script is not in the orrery repo root "
                         "(no constants_new.py beside it). NOTHING was "
                         "written.")

    planned = []
    for name, sha, chunks in FILES:
        with open(name, "rb") as handle:
            old = handle.read()
        if md5_content(old) != FINGERPRINTS[name]:
            raise SystemExit("ERROR: %s is not the version this patch was "
                             "built on (9dabda96). NOTHING was written."
                             % name)
        new = decode(name, sha, chunks)
        was_crlf = b"\r\n" in old
        if was_crlf:
            new = new.replace(b"\n", b"\r\n")
        planned.append((name, new, "updated", was_crlf))

    with open(LEDGER, "rb") as handle:
        old = handle.read()
    if ledger_fingerprint(old) != FINGERPRINTS[LEDGER]:
        raise SystemExit("ERROR: %s is not the version this patch was built "
                         "on (9dabda96). NOTHING was written." % LEDGER)
    was_crlf = b"\r\n" in old
    text = lf(old).decode("utf-8")
    if text.count(ANCHOR) != 1:
        raise SystemExit("ANCHOR FAIL in %s: expected 1 match, found %d. "
                         "NOTHING was written." % (LEDGER, text.count(ANCHOR)))
    if NOTE.split("\n")[0] in text:
        raise SystemExit("ERROR: the L-322 note this patch adds is already "
                         "in %s -- it has run before. NOTHING was written."
                         % LEDGER)
    text = text.replace(ANCHOR, NOTE)
    out = text.encode("utf-8")
    if was_crlf:
        out = out.replace(b"\n", b"\r\n")
    planned.append((LEDGER, out, "one note added on L-322", was_crlf))

    for name, data, _what, _crlf in planned:
        try:
            lf(data).decode("ascii")
        except UnicodeDecodeError:
            raise SystemExit("ERROR: %s would contain non-ASCII text. "
                             "NOTHING was written." % name)

    for name, data, what, was_crlf in planned:
        with open(name, "wb") as handle:
            handle.write(data)
        print("ok  %-28s %s%s" % (name, what,
                                  " [CRLF kept]" if was_crlf else ""))
    print("")
    print("patch applied (%d bytes across %d files)"
          % (sum(len(d) for _n, d, _w, _c in planned), len(planned)))
    print("Next: move this script into documentation/, run")
    print("python ledger_index.py LEDGER_CONSOLIDATED.md twice, then")
    print("python orrery_maintenance_run.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
